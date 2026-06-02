\*11. The following algorithm implements Jacobi’s method for symmetric matrices.

INPUT: dimension $n$ , matrix $A = \left( a _ { i j } \right)$ , tolerance $T O L$ , maximum number of iterations $N$ .

$$
\begin{array} { r l } & { b = | a _ { i i } - a _ { j j } | ; } \\ & { c = 2 a _ { i j } \ \mathrm { s i g n } ( a _ { i i } - a _ { j j } ) ; } \\ & { \mathrm { C O = 0 . 5 } \left( 1 + b / \left( c ^ { 2 } + b ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) ^ { \frac { 1 } { 2 } } ; } \\ & { \mathrm { S I = 0 . 5 } c / \left( C O \left( c ^ { 2 } + b ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) . } \end{array}
$$

STEP 11 If $k 1 > N$ then OUTPUT (’Maximum number of iterations exceeded’); STOP.

12. Jacobi’s method produces the following eigenvalues, accurate to within the tolerance:

(a) 3.414214, 0.5857864, 2.0000000; 3 iterations (b) 2.722246, 5.346462, −0.06870782; 3 iterations (c) 4.732051, 3, 1.267949; 3 iterations (d) 0.2547188, 1.822717, 3.177283, 4.745281; 3 iterations (e) −1.488068, $-$ 3.778287, 0.8275517, 3.438803; 3 iterations (f) 0.1922421, 1.189091, 0.5238224, 0.9948440; 3 iterations

13. (a) To within $1 0 ^ { - 5 }$ , the eigenvalues are 2.618034, 3.618034, 1.381966, and 0.3819660. (b) In terms of $p$ and $\rho$ the eigenvalues are $- 6 5 . 4 5 0 8 5 p / \rho , - 9 0 . 4 5 0 8 5 p / \rho , - 3 4 . 5 4 9 1 5 p / \rho$ , and $- 9 . 5 4 9 1 5 0 p / \rho$ .

14. (a) When $\alpha = 1 / 4$ , we have 0.97972997, 0.92060076, 0.82741863, 0.70771852, 0.57114328, 0.42886719, 0.29232093, 0.17255567, 0.07939063, and 0.02025441. (b) When $\alpha = 1 / 2$ , we have 0.95945994, 0.84120152, 0.65483725, 0.41543703, 0.14228657, −0.14226561, −0.41535813, −0.65488866, $^ -$ 0.84121873, and −0.95949118. (c) When $\alpha = 3 / 4$ , we have 0.93918991, 0.76180227, 0.48225588, 0.12315555, −0.28657015, 0.71339842, 1.12303720, 1.48233299, 1.76182810, and 1.93923676. The method appears to be stable for $\alpha \leq \textstyle { \frac { 1 } { 2 } }$ .

15. The actual eigenvalues are as follows:

(a) When $\alpha ~ = ~ \textstyle { \frac { 1 } { 4 } }$ we have 0.97974649, 0.92062677, 0.82743037, 0.70770751, 0.57115742, 0.42884258, 0.29229249, 0.17256963, 0.07937323, and 0.02025351.   
(b) When $\alpha ~ = ~ \frac { 1 } { 2 }$ we have 0.95949297, 0.84125353, 0.65486073, 0.41541501, 0.14231484, −0.14231484, −0.41541501, −0.65486073, $-$ 0.84125353, and −0.95949297.   
(c) When $\alpha \ : = \ : \frac { 3 } { 4 }$ we have 0.93923946, 0.76188030, 0.48229110, 0.12312252, −0.28652774, −0.71347226, −1.12312252, −1.48229110, $^ -$ 1.76188030, and −1.93923946. The method appears to be stable for $\alpha \leq \textstyle { \frac { 1 } { 2 } }$ .

# Exercise Set 9.6, page 625

1. (a) $s _ { 1 } = 1 + { \sqrt { 2 } }$ , $s _ { 2 } = - 1 + { \sqrt { 2 } }$ \*(b) $s _ { 1 } = \sqrt { 4 + \sqrt { 1 0 } }$ , $s _ { 2 } = \sqrt { 4 - \sqrt { 1 0 } }$ (c) $s _ { 1 } = \sqrt { 1 0 }$ , $s _ { 2 } = 2$ (d) $s _ { 1 } = \sqrt { 7 } , s _ { 2 } = 1 , s _ { 3 } = 1$

2. (a) $s _ { 1 } = { \sqrt { 2 } } , s _ { 2 } = { \sqrt { 2 } }$ (b) $s _ { 1 } = 2$ , $s _ { 2 } = 1$ , $s _ { 3 } = 1$ (c) $s _ { 1 } = \sqrt { 5 }$ , $s _ { 2 } = \sqrt { 3 }$ (d) $s _ { 1 } = \sqrt { 5 }$ , s2 = √2, $s _ { 3 } = 1$

3. (a)

$$
U = \left[ \begin{array} { c c } { { - 0 . 9 2 3 8 8 0 } } & { { - 0 . 3 8 2 6 8 3 } } \\ { { - 0 . 3 8 2 6 8 3 1 } } & { { 0 . 9 2 3 8 8 0 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 2 . 4 1 4 2 1 4 } } & { { 0 } } \\ { { 0 } } & { { 0 . 4 1 4 2 1 4 } } \end{array} \right] ,
$$

$$
V ^ { t } = \left[ \begin{array} { r r } { { - 0 . 9 2 3 8 8 0 } } & { { - 0 . 3 8 2 6 8 3 } } \\ { { - 0 . 3 8 2 6 8 3 } } & { { 0 . 9 2 3 8 8 0 } } \end{array} \right]
$$

\*(b)

$$
U = \left[ \begin{array} { c c c } { { - 0 . 8 2 4 7 3 6 } } & { { 0 . 3 9 1 3 3 6 } } & { { 0 . 4 0 8 2 4 8 } } \\ { { - 0 . 5 2 1 6 0 9 } } & { { - 0 . 2 4 7 5 0 2 } } & { { - 0 . 8 1 6 4 9 7 } } \\ { { - 0 . 2 1 8 4 8 2 } } & { { - 0 . 8 8 6 3 4 0 } } & { { 0 . 4 0 8 2 4 8 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 2 . 6 7 6 2 4 3 } } & { { 0 } } \\ { { 0 } } & { { 0 . 9 1 5 2 7 2 } } \\ { { 0 } } & { { 0 } } \end{array} \right] .
$$

(c)

$$
V ^ { t } = \left[ \begin{array} { r r } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right]
$$

(d)

$$
U = \left[ \begin{array} { r r r r r } { { - 0 . 4 3 6 4 3 6 } } & { { 0 . 7 0 7 1 0 7 } } & { { 0 . 4 0 8 2 4 8 } } & { { - 0 . 3 7 7 9 6 4 } } \\ { { 0 . 4 3 6 4 3 6 } } & { { 0 . 7 0 7 1 0 7 } } & { { - 0 . 4 0 8 2 4 8 } } & { { 0 . 3 7 7 9 6 4 } } \\ { { - 0 . 4 3 6 4 3 6 } } & { { 0 } } & { { - 0 . 8 1 6 4 9 7 } } & { { - 0 . 3 7 7 9 6 4 } } \\ { { - 0 . 6 5 4 6 5 4 } } & { { 0 } } & { { 0 } } & { { 0 . 7 5 5 9 2 9 } } \end{array} \right] , \quad S = \left[ \begin{array} { r r r r } { { 2 . 6 4 5 7 5 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] ,
$$

4. (a)

$$
U = \left[ \begin{array} { c c } { { - 0 . 7 0 7 1 0 7 } } & { { 0 . 7 0 7 1 0 7 } } \\ { { 0 . 7 0 7 1 0 7 } } & { { 0 . 7 0 7 1 0 7 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 1 . 4 1 4 2 1 4 } } & { { 0 } } \\ { { 0 } } & { { 1 . 4 1 4 2 1 4 } } \end{array} \right] ,
$$

$$
V ^ { t } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }
$$

(b)

$$
U = \left[ \begin{array} { c c c } { { - 0 . 5 7 7 3 5 0 } } & { { 0 . 4 0 8 2 4 8 } } & { { 0 . 7 0 7 1 0 7 } } \\ { { - 0 . 5 7 7 3 5 0 } } & { { 0 . 4 0 8 2 4 8 } } & { { - 0 . 7 0 7 1 0 7 } } \\ { { - 0 . 5 7 7 3 5 0 } } & { { - 0 . 8 1 6 4 9 7 } } & { { 0 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c c } { { 2 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right] ,
$$

(c)

5. For the matrix $A$ in Example 2 we have

$$
A ^ { t } A = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 0 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 4 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] }
$$

So $\begin{array} { l } { { A ^ { t } A ( 1 , 2 , 1 ) ^ { t } = ( 5 , 1 0 , 5 ) ^ { t } = 5 ( 1 , 2 , 1 ) ^ { t } , A ^ { t } A ( 1 , - 1 , 1 ) ^ { t } = ( 2 , - 2 , 2 ) ^ { t } = 2 ( 1 , - 1 , 1 ) ^ { t } , } } \\ { { A ( - 1 , 0 , 1 ) ^ { t } = ( - 1 , 0 , 1 ) ^ { t } . } } \end{array}$ , and $^ { * } 6$ . The rank of $a$ is the number of linearly independent rows in $A$ , and the rank of $A ^ { t }$ is the number of linearly independent row of $A ^ { t }$ , which corresponds to the number of linearly independent columns of $A$ . By Theorem 9.25 the number of linearly independent rows of a matrix is the same as the number of independent columns, so the rank of $A$ is the same as the rank of $A ^ { t }$ .

$^ { * } 7$ . Let $A$ be an $m \times n$ matrix. Theorem 9.25 implies that $\operatorname { R a n k } ( A ) = \operatorname { R a n k } ( A ^ { t } )$ , so $\operatorname { N u l l i t y } ( A ) =$ $n { \mathrm { - R a n k } } ( A )$ and N $\mathrm { { l l i t y } } ( A ^ { t } ) = m { \mathrm { { - R a n k } } } ( A ^ { t } ) = m { \mathrm { { - R a n k } } } ( A )$ . Hence $\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( A ^ { t } )$ if and only if $n = m$ .

$^ { * } 8$ . The matrices $S$ and $S ^ { t }$ have nonzero values only on their diagonals, and the nonzero eigenvalues of $A ^ { t } A$ and $A A ^ { t }$ are the same, so the singular values of $A ^ { t }$ are on the diagonal of $S ^ { t }$ in decreasing order. In addition, the matrices $U$ and $V$ are both orthogonal, so a Singular Value Decomposition of $A ^ { t }$ is given by

$$
A ^ { t } = ( U S V ^ { t } ) ^ { t } = ( V ^ { t } ) ^ { t } S ^ { t } U ^ { t } = V S ^ { t } U ^ { t }
$$

9. $\mathrm { R a n k } ( S )$ is the number of nonzero entries on the diagonal of $S$ . This corresponds to the number of nonzero eigenvalues (counting multiplicities) of $A ^ { t } A$ . So $\operatorname { R a n k } ( S ) = \operatorname { R a n k } ( A ^ { t } A )$ , and by part (ii) of Theorem 9.26 this is the same as $\operatorname { R a n k } ( A )$ .

10. From Exercise 9 we know that $\operatorname { R a n k } ( A ) = \operatorname { R a n k } ( S )$ . Since $A$ and $S$ are both $m \times n$ ,

$$
\operatorname { R a n k } ( A ) + \operatorname { N u l l i t y } ( A ) = n = \operatorname { R a n k } ( S ) + \operatorname { N u l l i t y } ( S ) ,
$$

which implies that $\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( S )$ .

$^ *$ 11. The matrices $U$ and $V$ are orthogonal, so they are nonsingular with $U ^ { - 1 } = U ^ { t }$ and $V ^ { - 1 } = V ^ { t }$ . Since

$$
\operatorname* { d e t } A = \operatorname* { d e t } U \cdot \operatorname* { d e t } S \cdot \operatorname* { d e t } V ^ { t } ,
$$

with $\operatorname* { d e t } U$ and $\operatorname* { d e t } V ^ { t }$ both nonzero, $\operatorname* { d e t } A = 0$ if and only if $\operatorname* { d e t } S = 0$ . Hence $A$ in nonsingular if and only if $S$ is nonsingular.

When $A ^ { - 1 }$ exists we have the Singular Value Decomposition of $A ^ { - 1 }$ given by

$$
A ^ { - 1 } = \left( U S V ^ { t } \right) ^ { - 1 } = ( V ^ { t } ) ^ { - 1 } S ^ { - 1 } U ^ { - 1 } = \left( V ^ { - 1 } \right) ^ { - 1 } S ^ { - 1 } U ^ { t } = V S ^ { - 1 } U ^ { t } .
$$

12. If $A$ is $m \times n$ , then $A ^ { t }$ is $n \times m$ , $A A ^ { t }$ is $n \times n$ , and $A ^ { t } A$ is $m \times m$ . So

$$
n = \operatorname { R a n k } ( A ) + \operatorname { N u l l i t y } ( A ) = \operatorname { R a n k } ( A A ^ { t } ) + \operatorname { N u l l i t y } ( A A ^ { t } ) \quad { \mathrm { a n d } } \quad m = \operatorname { R a n k } ( A ^ { t } A ) + \operatorname { N u l l i t y } ( A ^ { t } A )
$$

Since $\operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( A ) = \operatorname { R a n k } ( A A ^ { t } )$ we have

$$
\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( A ^ { t } A ) = \mathrm { N u l l i t y } ( A A ^ { t } ) \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad m = n .
$$

13. Yes. By Theorem 9.25 we have $\operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( ( A ^ { t } A ) ^ { t } ) = \operatorname { R a n k } ( A A ^ { t } )$ . Applying part (iii) of Theorem 9.26 gives $\operatorname { R a n k } ( A A ^ { t } ) = \operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( A )$ .

14. Because $P$ is orthogonal, we have $P ^ { - 1 } = P ^ { t }$ , so $( P A ) ^ { t } ( P A ) = A ^ { t } ( P ^ { t } P ) A = A ^ { t } A$ . The singular values of $A$ are the eigenvalues of $A ^ { t } A$ , which must agree with those of $( P A ) ^ { t } ( P A )$ . Hence the singular values of $A$ and $P A$ are the same.

$^ *$ 15. The condition number is defined on page 470 as

$$
K _ { 2 } ( A ) = | | A | | _ { 2 } | | A ^ { - 1 } | | _ { 2 } .
$$

By Theorem 7.15 on page 447, we have $\lvert \lvert A \rvert \rvert _ { 2 } ^ { 2 } = \rho ( A ^ { t } A )$ , which is the largest eigenvalue of $A ^ { t } A$ , that is, $s _ { 1 } ^ { 2 }$ .

In addition, Exercise 15 on page 450 states that the eigenvalues of the inverse of a nonsingular matrix are the reciprocals of the eigenvalues of the matrix, so

$$
| | A ^ { - 1 } | | _ { 2 } ^ { 2 } = \rho ( ( A ^ { - 1 } ) ^ { t } A ^ { - 1 } ) = \rho ( ( A ^ { t } ) ^ { - 1 } A ^ { - 1 } ) = \rho ( ( A A ^ { t } ) ^ { - 1 } )
$$

is the largest eigenvalue of $( A A ^ { t } ) ^ { - 1 }$ . This is the reciprocal of the smallest eigenvalue $A A ^ { t }$ . By Theorem 9.26, the nonzero eigenvalues of $A ^ { t } A$ and $A A ^ { t }$ are the same, so this value is $1 / s _ { n } ^ { 2 }$ . As a consequence,

$$
K _ { 2 } ( A ) = | | A | | _ { 2 } | | A ^ { - 1 } | | _ { 2 } = { \frac { s _ { 1 } } { s _ { n } } } .
$$

16. For 1(a)the $l _ { 2 }$ condition number is ${ \frac { 1 + { \sqrt { 2 } } } { - 1 + { \sqrt { 2 } } } } = 3 + 2 { \sqrt { 2 } }$ , and for $1 ( \mathrm { d } )$ it is $\sqrt { 7 }$ . For $2 ( \mathrm { a } )$ the $l _ { 2 }$ condition number is $1$ , and for $2 ( \mathrm { b } )$ it is 2.

17. (a) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 3 } \\ { 3 . 5 } \\ { 4 . 2 } \\ { 5 . 0 } \\ { 7 . 0 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l } { 1 } & { x _ { 0 } } \\ { 1 } & { x _ { 1 } } \\ { 1 } & { x _ { 2 } } \\ { 1 } & { x _ { 3 } } \\ { 1 } & { x _ { 4 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 . 0 } \\ { 1 } & { 2 . 0 } \\ { 1 } & { 3 . 0 } \\ { 1 } & { 4 . 0 } \\ { 1 } & { 5 . 0 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

$$
\boldsymbol { S } = \left[ \begin{array} { c c } { 7 . 6 9 1 2 1 3 } & { 0 } \\ { 0 } & { 0 . 9 1 9 3 7 0 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] , \quad \boldsymbol { V } ^ { t } = \left[ \begin{array} { c c } { 0 . 2 6 6 9 3 4 } & { 0 . 9 6 3 7 1 5 } \\ { 0 . 9 6 3 7 1 5 } & { - 0 . 2 6 6 9 3 4 } \end{array} \right]
$$

and

So

$$
\mathbf { c } = U ^ { t } \mathbf { b } = \left[ \begin{array} { c } { 1 0 . 2 3 9 1 6 0 } \\ { - 0 . 0 2 4 1 9 6 } \\ { 0 . 2 1 9 0 1 3 } \\ { - 0 . 0 7 6 6 2 1 } \\ { 0 . 8 2 7 7 4 3 } \end{array} \right] ,
$$

and the components of $\mathbf { z }$ are

$$
z _ { 1 } = { \frac { c _ { 1 } } { s _ { 1 } } } = { \frac { 1 0 . 2 3 9 1 6 0 } { 7 . 6 9 1 2 1 3 } } = 1 . 3 3 , \quad { \mathrm { a n d } } \quad z _ { 2 } = { \frac { c _ { 2 } } { s _ { 2 } } } = { \frac { - 0 . 0 2 4 1 9 6 } { 0 . 9 1 9 3 7 0 } } = - 0 . 0 2 6 ,
$$

This gives the least squares coefficients in $P _ { 1 } ( x ) = a _ { 0 } + a _ { 1 } x$ a s

$$
\left[ \begin{array} { l } { a _ { 0 } } \\ { a _ { 1 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { l } { 0 . 3 3 } \\ { 1 . 2 9 } \end{array} \right] ,
$$

that is, $P _ { 1 } ( x ) = 0 . 3 3 + 1 . 2 9 x$ .

(b) We have the same vector $\mathbf { b }$ as in part(a) but the matrix $a$ is now

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 4 } \\ { 1 } & { 3 } & { 9 } \\ { 1 } & { 4 } & { 1 6 } \\ { 1 } & { 5 } & { 2 5 } \end{array} \right] } ~ .
$$

and

We now find the vector $\mathbf { c } = U ^ { t } \mathbf { b }$ , construct $\mathbf { z }$ by dividing the components of the vector $\mathbf { c }$ by the three singular values. Then the coefficients of the least squares polynomial are given by the components of the vector $V \mathbf { z }$ . This produces

$$
P _ { 2 } ( x ) = 0 . 1 8 + 1 . 4 1 8 5 7 1 x - 0 . 0 2 1 4 2 8 6 x ^ { 2 } .
$$

\*18. (a) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 8 4 } \\ { 1 . 9 6 } \\ { 2 . 2 1 } \\ { 2 . 4 5 } \\ { 2 . 9 4 } \\ { 3 . 1 8 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l l } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } \\ { 1 } & { x _ { 2 } } & { x _ { 2 } ^ { 2 } } \\ { 1 } & { x _ { 3 } } & { x _ { 3 } ^ { 2 } } \\ { 1 } & { x _ { 4 } } & { x _ { 4 } ^ { 2 } } \\ { 1 } & { x _ { 5 } } & { x _ { 5 } ^ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 } & { 1 . 0 } & { 1 . 0 } \\ { 1 } & { 1 . 1 } & { 1 . 2 1 } \\ { 1 } & { 1 . 3 } & { 1 . 6 9 } \\ { 1 } & { 1 . 5 } & { 2 . 2 5 } \\ { 1 } & { 1 . 9 } & { 3 . 6 1 } \\ { 1 } & { 2 . 1 } & { 4 . 4 1 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

So

and the components of $\mathbf { z }$ are

$$
z _ { 1 } = \frac { c _ { 1 } } { s _ { 1 } } = \frac { - 5 . 9 5 5 0 0 9 } { 7 . 8 4 4 1 2 7 } = - 0 . 7 5 9 1 6 8 , z _ { 2 } = \frac { c _ { 2 } } { s _ { 2 } } = \frac { - 1 . 1 8 5 5 9 1 } { 1 . 2 2 3 7 9 0 } = - 0 . 9 6 8 7 8 6 ,
$$

and

$$
z _ { 3 } = { \frac { c _ { 3 } } { s _ { 3 } } } = { \frac { - 0 . 0 4 4 9 8 5 } { 0 . 0 7 0 0 9 4 } } = - 0 . 6 4 1 7 8 4 .
$$

This gives the least squares coefficients in $P _ { 2 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 }$ a s

$$
\left[ \begin{array} { r } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { r } { 0 . 5 9 6 5 8 1 } \\ { 1 . 2 5 3 2 9 3 } \\ { - 0 . 0 1 0 8 5 3 } \end{array} \right] .
$$

The least squares error using these values uses the last three components of $\mathbf { c }$ , and is

$$
| | A \mathbf { x } - \mathbf { b } | | _ { 2 } = { \sqrt { c _ { 4 } ^ { 2 } + c _ { 5 } ^ { 2 } + c _ { 6 } ^ { 2 } } } = { \sqrt { ( - 0 . 0 0 3 7 3 2 ) ^ { 2 } + ( - 0 . 0 0 0 4 9 3 ) ^ { 2 } + ( - 0 . 0 0 1 9 6 3 ) ^ { 2 } } } = 0 . 0 0 4 2 4 4 .
$$

(b) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 8 4 } \\ { 1 . 9 6 } \\ { 2 . 2 1 } \\ { 2 . 4 5 } \\ { 2 . 9 4 } \\ { 3 . 1 8 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l l l } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } & { x _ { 0 } ^ { 3 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } & { x _ { 1 } ^ { 3 } } \\ { 1 } & { x _ { 2 } } & { x _ { 2 } ^ { 2 } } & { x _ { 2 } ^ { 3 } } \\ { 1 } & { x _ { 3 } } & { x _ { 3 } ^ { 2 } } & { x _ { 3 } ^ { 3 } } \\ { 1 } & { x _ { 4 } } & { x _ { 4 } ^ { 2 } } & { x _ { 4 } ^ { 3 } } \\ { 1 } & { x _ { 5 } } & { x _ { 5 } ^ { 2 } } & { x _ { 5 } ^ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l l l l } { 1 } & { 1 . 0 } & { 1 . 0 } & { 1 . 0 } \\ { 1 } & { 1 . 1 } & { 1 . 2 1 } & { 1 . 3 3 1 } \\ { 1 } & { 1 . 3 } & { 1 . 6 9 } & { 2 . 1 9 7 } \\ { 1 } & { 1 . 5 } & { 2 . 2 5 } & { 3 . 3 7 5 } \\ { 1 } & { 1 . 9 } & { 3 . 6 1 } & { 6 . 8 5 9 } \\ { 1 } & { 2 . 1 } & { 4 . 4 1 } & { 9 . 2 6 1 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

and

So

$$
\mathbf { c } = U ^ { t } \mathbf { b } = \left[ \begin{array} { c } { - 5 . 6 3 2 3 0 9 } \\ { - 2 . 2 6 8 3 7 6 } \\ { 0 . 0 3 6 2 4 1 } \\ { 0 . 0 0 5 7 1 7 } \\ { - 0 . 0 0 0 8 4 5 } \\ { - 0 . 0 0 4 0 8 6 } \end{array} \right] ,
$$

and the components of $\mathbf { z }$ are

$$
\begin{array} { l } { { z _ { 1 } = \displaystyle \frac { c _ { 1 } } { s _ { 1 } } = \displaystyle \frac { - 5 . 6 3 2 3 0 9 } { 1 4 . 5 0 6 8 0 8 } = - 0 . 3 8 8 2 5 3 , \quad z _ { 2 } = \displaystyle \frac { c _ { 2 } } { s _ { 2 } } = \displaystyle \frac { - 2 . 2 6 8 3 7 6 } { 2 . 0 8 4 9 0 9 } = - 1 . 0 8 7 9 9 8 , } } \\ { { z _ { 3 } = \displaystyle \frac { c _ { 3 } } { s _ { 3 } } = \displaystyle \frac { 0 . 0 3 6 2 4 1 } { 0 . 1 9 8 7 6 0 } = 0 . 1 8 2 3 3 6 , \quad \mathrm { a n d } \quad z _ { 4 } = \displaystyle \frac { c _ { 4 } } { s _ { 4 } } = \displaystyle \frac { 0 . 0 0 5 7 1 7 } { 0 . 8 6 8 3 2 8 } = 0 . 6 5 8 4 3 . } } \end{array}
$$

This gives the least squares coefficients in $P _ { 2 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 }$ as

$$
\left[ \begin{array} { r } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \\ { a _ { 3 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { r } { 0 . 6 2 9 0 1 9 } \\ { 1 . 1 8 5 0 1 0 } \\ { 0 . 0 3 5 3 3 3 } \\ { - 0 . 0 1 0 0 4 7 } \end{array} \right] .
$$

The least squares error using these values uses the last two components of $\mathbf { c }$ , and is

$$
| | A \mathbf { x } - \mathbf { b } | | _ { 2 } = { \sqrt { c _ { 5 } ^ { 2 } + c _ { 6 } ^ { 2 } } } = { \sqrt { ( - 0 . 0 0 0 8 4 5 ) ^ { 2 } + ( - 0 . 0 0 4 0 8 6 ) ^ { 2 } } } = 0 . 0 0 4 1 7 2 .
$$

# Numerical Solutions of Nonlinear Systems of Equations

Exercise Set 10.1, page 636

1. Use Theorem 10.5

\*2. One example is $\mathbf { F } ( x _ { 1 } , x _ { 2 } ) = { \bigg ( } 1 , { \frac { 1 } { ( x _ { 1 } - 1 ) ^ { 2 } + x _ { 2 } ^ { 2 } } } { \bigg ) } ^ { t } .$

3. Use Theorem 10.5 for each of the partial derivatives.

\*4. The solutions are near (−1.5, 10.5) and $( 2 , 1 1 )$ .

(a) The graphs are shown in the figure below.

![](images/e14debc4b243f75339d1e84fe814e6198f97b344b27bdbfa25b51e14310963d1.jpg)

(b) Use

$$
\mathbf { G } _ { 1 } ( \mathbf { x } ) = \left( - 0 . 5 + { \sqrt { 2 x _ { 2 } - 1 7 . 7 5 } } , 6 + { \sqrt { 2 5 - ( x _ { 1 } - 1 ) ^ { 2 } } } \right) ^ { t }
$$

and

$$
\mathbf { G } _ { 2 } ( \mathbf { x } ) = \left( - 0 . 5 - \sqrt { 2 x _ { 2 } - 1 7 . 7 5 } , 6 + \sqrt { 2 5 - ( x _ { 1 } - 1 ) ^ { 2 } } \right) ^ { t } .
$$

For ${ \bf G } _ { 1 } ( { \bf x } )$ with $\mathbf { x } ^ { ( 0 ) } = ( 2 , 1 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 1 . 5 4 6 9 4 6 6 , 1 0 . 9 6 9 9 9 4 ) ^ { t }$ , and for ${ \bf G } _ { 2 } ( { \bf x } )$ with $\mathbf { x } ^ { ( 0 ) } = ( - 1 . 5 , 1 0 . 5 )$ , we have $\mathbf { x } ^ { ( 3 4 ) } = ( - 2 . 0 0 0 0 0 3 , 9 . 9 9 9 9 9 6 ) ^ { t }$ .

$^ { * } 5$ . (a) Continuity properties can be easily shown. Moreover,

$$
\frac { 8 } { 1 0 } \leq \frac { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 8 } { 1 0 } \leq 1 . 2 5
$$

and

$$
\frac { 8 } { 1 0 } \leq \frac { x _ { 1 } x _ { 2 } ^ { 2 } + x _ { 1 } + 8 } { 1 0 } \leq 1 . 2 8 7 5 ,
$$

so $\mathbf { G } ( \mathbf { x } ) \in D$ , whenever $\mathbf { x } \in D$ .

Further,

$$
\frac { \partial g _ { 1 } } { \partial x _ { 1 } } = \frac { 2 x _ { 1 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 1 } ( \mathbf { x } ) } { \partial x _ { 1 } } \right| \leq \frac { 3 } { 1 0 } , \quad \frac { \partial g _ { 1 } } { \partial x _ { 2 } } = \frac { 2 x _ { 2 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 2 } } \right| \leq \frac { 3 } { 1 0 } ,
$$

$$
\frac { \partial g _ { 2 } } { \partial x _ { 1 } } = \frac { x _ { 2 } ^ { 2 } + 1 } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 1 } } \right| \leq \frac { 3 . 2 5 } { 1 0 } , \quad \mathrm { ~ a n d ~ } \ \frac { \partial g _ { 2 } } { \partial x _ { 2 } } = \frac { 2 x _ { 1 } x _ { 2 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 2 } } \right| \leq \frac { 4 . 5 } { 1 0 } .
$$

Since

$$
\left| \frac { \partial g _ { i } ( \mathbf { x } ) } { \partial x _ { j } } \right| \leq 0 . 4 5 = \frac { 0 . 9 } { 2 } ,
$$

for $i , j = 1 , 2$ , all hypothesis of Theorem 10.6 have been satisfied, and $\mathbf { G }$ has a unique fixed point in $D$ .

(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ and tolerance $1 0 ^ { - 5 }$ , we have $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 9 9 9 9 9 7 3 , 0 . 9 9 9 9 9 7 3 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ and tolerance $1 0 ^ { - 5 }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 9 9 9 9 9 8 4 , 0 . 9 9 9 9 9 9 1 ) ^ { t }$ .

6. (a) $\mathbf { G } = \left( x _ { 2 } / { \sqrt { 5 } } , 0 . 2 5 ( \sin x _ { 1 } + \cos x _ { 2 } ) \right) ^ { t }$ and $D = \{ ( x _ { 1 } , x _ { 2 } ) \mid 0 \leq x _ { 1 } , x _ { 1 } \leq 1 \}$ . (b) With $\begin{array} { r } { { \bf x } ^ { ( 0 ) } = \left( \frac { 1 } { 2 } , \frac { 1 } { 2 } \right) ^ { t } } \end{array}$ , we have $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 1 2 1 2 4 4 0 , 0 . 2 7 1 1 0 6 5 ) ^ { t }$ t. (c) With $\begin{array} { r } { { \bf x } ^ { ( 0 ) } = \left( \frac { 1 } { 2 } , \frac { 1 } { 2 } \right) ^ { t } } \end{array}$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 1 2 1 2 4 2 1 , 0 . 2 7 1 1 0 5 2 ) ^ { t }$ .

7. (a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 5 . 0 0 0 0 0 0 0 0 , 0 . 0 0 0 0 0 0 0 , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ . (b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 1 . 0 3 6 4 0 1 1 , 1 . 0 8 5 7 0 7 2 , 0 . 9 3 1 1 9 1 1 3 ) ^ { t }$ . (c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 . 5 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 0 0 0 0 0 0 0 0 0 , 0 . 0 9 9 9 9 9 9 9 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$ . (d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 9 8 1 4 4 7 1 , - 0 . 1 9 9 6 0 6 0 0 , - 0 . 5 2 8 8 2 5 9 5 ) ^ { i }$ t.

8. (a) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { x _ { 1 } - x _ { 2 } ^ { 2 } } , \sqrt { x _ { 1 } ^ { 2 } - x _ { 2 } } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 0 . 7 , 0 . 4 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 1 4 ) } = ( 0 . 7 7 1 8 4 6 4 7 , 0 . 4 1 9 6 5 1 3 1 )$ t.

(b) With

$$
\mathbf G ( \mathbf x ) = \left( x / \sqrt { 3 } , \sqrt { \left( 1 + x _ { 1 } ^ { 3 } \right) / ( 3 x _ { 1 } ) } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf x ^ { ( 0 ) } = ( 0 . 4 , 0 . 7 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 2 0 ) } = ( 0 . 4 9 9 9 9 8 0 , 0 . 8 6 6 0 2 2 1 ) ^ { t }$ t.

(c) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { 3 7 - x _ { 2 } } , \sqrt { x _ { 1 } - 5 } , 3 - x _ { 1 } - x _ { 2 } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 5 , 1 , - 1 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 1 0 ) } = ( 6 . 0 0 0 0 0 0 2 , 1 . 0 0 0 0 0 0 0 , - 3 . 9 9 9 9 9 7 1 ) ^ { t }$ .

(d) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { 2 x _ { 3 } + x _ { 2 } - 2 x _ { 2 } ^ { 2 } } , \sqrt { \left( 1 0 x _ { 3 } + x _ { 1 } ^ { 2 } \right) / 8 } , x _ { 1 } ^ { 2 } / ( 7 x _ { 2 } ) \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 0 . 5 , 0 . 5 , 0 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 6 0 ) } = ( 0 . 5 2 9 1 5 4 8 , 0 . 4 0 0 0 0 1 8 , 0 . 0 9 9 9 9 8 5 3 ) ^ { t }$ .

9. (a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 0 0 0 0 0 0 0 , 0 , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ . (b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t } .$ (c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 0 , 0 . 1 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$ . (d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$ .

10. (a) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { x _ { 1 } - { x _ { 2 } } ^ { 2 } } , \sqrt { { x _ { 1 } } ^ { 2 } } - x _ { 2 } ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 7 , 0 . 4 ) ^ { t }$ as in Exercise 8(a) gives a square root of a negative number as the first iteration. Thus, the method fails. (b) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = \left( x / \sqrt { 3 } , \sqrt { ( 1 + { x _ { 1 } } ^ { 3 } ) / ( 3 x _ { 1 } ) } \right) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 4 , 0 . 7 ) ^ { t }$ as in Exercise 8(b) gives $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 4 9 9 9 9 8 0 7 , 0 . 8 6 6 0 2 6 5 2 ) ^ { t }$ . The convergence is accelerated for this problem. (c) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { 3 7 - x _ { 2 } } , \sqrt { x _ { 1 } - 5 } , 3 - x _ { 1 } - x _ { 2 } ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 5 , 1 , - 1 ) ^ { t }$ as in Exercise 8(c) gives $\mathbf { x } ^ { ( 1 ) } = ( 6 , 1 , - 4 ) ^ { t }$ . The convergence very much accelerated for this problem. (d) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { 2 x _ { 3 } + x _ { 2 } - { 2 x _ { 2 } } ^ { 2 } } , \sqrt { ( { 1 0 x _ { 3 } + x _ { 1 } } ^ { 2 } ) / 8 } , { x _ { 1 } } ^ { 2 } / ( 2 x _ { 2 } ) ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 5 , 0 . 5 , 0 ) ^ { t }$ as in Exercise $8 ( \mathrm { d } )$ leads to division by zero as the first iteration. Thus, the method fails.

11. A stable solution occurs when $x _ { 1 } = 8 0 0 0$ and $x _ { 2 } = 4 0 0 0$ .

$^ { * } 1 2$ . Let $\mathbf { F } ( \mathbf { x } ) = ( f _ { 1 } ( \mathbf { x } ) , . . . , f _ { n } ( \mathbf { x } ) ) ^ { t }$ . Suppose $\mathbf { F }$ is continuous at $\mathbf { x _ { 0 } }$ . By Definition 10.3,

$$
\operatorname * { l i m } _ { \mathbf { x } \to \mathbf { x _ { 0 } } } f _ { i } ( \mathbf { x } ) = f _ { i } ( \mathbf { x } _ { 0 } ) , \quad \mathrm { f o r ~ e a c h } \ i = 1 , . . . , n .
$$

Given $\epsilon > 0$ , there exists $\delta _ { i } > 0$ such that

$$
| f _ { i } ( { \bf x } ) - f _ { i } ( { \bf x } _ { 0 } ) | < \epsilon ,
$$

whenever $0 < | | { \bf x } - { \bf x } _ { 0 } | | < \delta _ { i }$ and $\mathbf { x } \in D$ .

Let $\delta = \operatorname* { m i n } _ { 1 \leq i \leq n } \delta _ { i }$ . If $0 < | | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ , then $0 < | | { \bf x } - { \bf x } _ { 0 } | | < \delta _ { i }$ and $| f _ { i } ( { \bf x } ) - f _ { i } ( { \bf x } _ { 0 } ) | < \epsilon$ , for each $i = 1 , . . . , n$ , whenever $\mathbf { x } \in D$ . This implies that

$$
| | \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) | | _ { \infty } < \epsilon ,
$$

whenever $| | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ and $\mathbf { x } \in D$ . By the equivalence of vector norms, the result holds for all vector norms by suitably adjusting $\delta$ .

For the converse, let $\epsilon > 0$ be given. Then there is a $\delta > 0$ such that

$$
| | \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) | | < \epsilon ,
$$

whenever $\mathbf { x } \in D$ and $| | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ . By the equivalence of vector norms, a number $\delta ^ { \prime } > 0$ can be found with

$$
| | f _ { i } ( \mathbf { x } ) - f _ { i } ( \mathbf { x } _ { 0 } ) | | < \epsilon .
$$

whenever $\mathbf { x } \in D$ and $\| \mathbf { x } - \mathbf { x } _ { 0 } \| < \delta ^ { \prime }$ .

Thus, $\begin{array} { r } { \operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } f _ { i } ( \mathbf { x } ) = f _ { i } ( \mathbf { x } _ { 0 } ) } \end{array}$ , for $i = 1 , . . . , n$ . Since $\mathbf { F } ( \mathbf { x } _ { \mathrm { 0 } } )$ is defined, the conditions in Definition 10.3 hold, and $\mathbf { F }$ is continuous at $\mathbf { x } _ { \mathrm { 0 } }$ .

13. When $A = O$ , the zero matrix, the result follows immediately, because in this case $\mathbf { F } ( \mathbf { x } ) -$ $\mathbf { F } ( \mathbf { x } _ { \mathrm { 0 } } ) = \mathbf { 0 }$ for all $\mathbf { x }$ and $\mathbf { x } _ { \mathrm { 0 } }$ in $\mathbb { R } ^ { n }$ .

Suppose $A \neq O$ . Let $\mathbf { x } _ { \mathrm { 0 } }$ in $\mathbb { R } ^ { n }$ be arbitrary and $\varepsilon > 0$ . Choose $\delta = \varepsilon / | | A | |$ and $\mathbf { x } _ { 0 } - \mathbf { x } < \delta$ . Then

$$
| | F ( \mathbf { x } ) - F ( \mathbf { x } _ { 0 } ) | | = | | A \mathbf { x } - A \mathbf { x } _ { 0 } | | = | | A ( \mathbf { x } - \mathbf { x } _ { 0 } ) | | .
$$

so

$$
| | F ( \mathbf { x } ) - F ( \mathbf { x } _ { 0 } ) | | = | | A ( \mathbf { x } - \mathbf { x } _ { 0 } ) | | \leq | | A | | \cdot | | \mathbf { x } - \mathbf { x } _ { 0 } | | < | | A | | \cdot { \frac { \varepsilon } { | | A | | } } = \varepsilon .
$$

This, by Exercise 12, implies that $\mathbf { F }$ is continuous on $\mathbb { R } ^ { n }$ .

# Exercise Set 10.2, page 644

1. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 9 5 8 9 3 6 , 1 . 9 8 3 4 2 3 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 1 3 1 6 1 6 , - 0 . 0 1 8 3 7 6 2 2 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 2 3 . 9 4 2 6 2 6 , 7 . 6 0 8 6 7 9 7 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 1 ) }$ cannot be computed since $J ( 0 )$ is singular.

2. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 0 0 1 6 6 7 , 0 . 2 5 0 8 0 3 6 , - 0 . 5 1 7 3 8 7 4 ) ^ { t }$ \*(b) $\mathbf { x } ^ { ( 2 ) } = ( 4 . 3 5 0 8 7 7 , 1 8 . 4 9 1 2 3 , - 1 9 . 8 4 2 1 1 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 3 6 6 8 7 0 8 , 1 . 0 8 5 9 2 3 8 4 , 0 . 9 2 9 7 7 9 3 2 )$ t (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 0 7 1 6 6 8 7 , 1 . 3 0 9 4 4 3 7 7 , - 0 . 8 5 8 9 5 4 7 7 ) ^ { t }$ t

3. Graphing in Maple gives the following:

(a) $( 0 . 5 , 0 . 2 ) ^ { t }$ and (1.1, 6.1)t   
(b) $( - 0 . 3 5 , 0 . 0 5 ) ^ { t } , ( 0 . 2 , - 0 . 4 5 ) ^ { t } , ( 0 . 4 , - 0 . 5 ) ^ { t }$ and $( 1 , - 0 . 3 ) ^ { t }$   
\*(c) $( - 1 , 3 . 5 ) ^ { t }$ , $( 2 . 5 , 4 ) ^ { t }$   
(d) (0.11, 0.27)t

4. Graphing in Maple gives the following:

$$
\begin{array} { r l } & { ( 0 . 5 , 0 . 5 , - 0 . 5 ) ^ { t } } \\ & { ( 7 , - 1 , - 2 ) ^ { t } } \\ & { ( 1 , 1 , 1 ) ^ { t } } \\ & { ( 1 , - 1 , 1 ) ^ { t } \mathrm { ~ a n d ~ } ( 1 , 1 , - 1 ) ^ { t } } \end{array}
$$

5. Newton’s method gives the following:

$$
\mathbf { W i t h { x } } ^ { ( 0 ) } = ( 0 . 5 , 2 ) ^ { t } , { \mathbf { x } } ^ { ( 3 ) } = ( 0 . 5 , 2 ) ^ { t } \mathbf { W i t h { x } } ^ { ( 0 ) } = ( 1 . 1 , 6 . 1 ) , { \mathbf { x } } ^ { ( 3 ) } = ( 1 . 0 9 6 7 1 9 7 , 6 . 0 4 0 9 3 2 9 ) ^ { t }
$$

(b) With $\mathbf { x } ^ { ( 0 ) } = ( - 0 . 3 5 , 0 . 0 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 7 3 6 9 8 2 2 , 0 . 0 5 6 2 6 6 4 9 0 ^ { t } \mathrm { W i t h } \mathbf { x } ^ { ( 0 ) } = ( 0 . 2 , - 0 . 4 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( 0 . 3 , - 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 , 0 . 4 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 1 . 5 , 0 , 0 , 0 , 0 , 0 . 4 , 1 . 5 , 0 , 0 , 0 , 0 , 1 . 5 , 0 , 0 , 0 , 1 . 5 , 0 , 0 , 1 .$ ( $0 . 1 4 7 8 3 9 2 4 , - 0 . 4 3 6 1 7 7 6 2 ) ^ { t }$ With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 4 , - 0 . 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( 0 . 4 0 8 0 9 5 6 6 , - 0 . 4 9 2$ 62939)t With $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 0 . 3 ) ^ { t } , \mathbf { x } ^ { ( 4 ) } = ( 1 . 0 3 3 0 7 1 5 , - 0 . 2 7 9 9 6 1 8 4 ) ^ { t }$   
\*(c) With $\mathbf { x } ^ { ( 0 ) } = ( - 1 , 3 . 5 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 ) } = ( - 1 , 3 . 5 ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 2 . 5 , 4 ) ^ { t }$ , $\mathbf { x } ^ { ( 3 ) } = ( 2 . 5 4 6 9 4 7 , 3 . 9 8 4 9 9 8 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 1 2 1 2 4 1 9 , 0 . 2 7 1 1 0 5 1 ) ^ { t }$ .

6. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 1 2 ) } = ( 0 . 4 9 9 9 9 9 5 3 , 0 . 0 0 3 1 9 9 0 6 , - 0 . 5 2 3 5 1 8 8 6 ) ^ { t }$   
(b) $\mathfrak { c } ^ { ( 4 ) } = ( 6 . 1 7 1 0 7 4 6 2 , - 1 . 0 8 2 1 6 2 0 1 , - 2 . 0 8 8 9 1 2 5 1 )$ t   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 1 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } ~ = ~ ( 1 , - 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 5 ) } \ = \ ( 0 . 9 , - 1 , 0 . 5 ) ^ { t }$ ; and with $\mathbf { x } ^ { ( 0 ) } ~ = ~ ( 1 , - 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 5 ) } =$ $( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ .

7. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 5 ) } = ( 0 . 5 0 0 0 0 0 0 0 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 6 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$

8. (a) Suppose $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution to

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 . } } \end{array}
$$

Multiplying the first three equations by $^ { - 1 }$ and factoring gives

$$
\begin{array} { c } { { 4 ( - x _ { 1 } ) - ( - x _ { 2 } ) + ( - x _ { 3 } ) = ( - x _ { 1 } ) x _ { 4 } , } } \\ { { - ( - x _ { 1 } ) + 3 ( - x _ { 2 } ) - 2 ( - x _ { 3 } ) = ( - x _ { 2 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) - 2 ( - x _ { 2 } ) + 3 ( - x _ { 3 } ) = ( - x _ { 3 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) ^ { 2 } + ( - x _ { 2 } ) ^ { 2 } + ( - x _ { 3 } ) ^ { 2 } = 1 . } } \end{array}
$$

Thus, $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , x _ { 4 } ) ^ { t }$ is also a solution.

(b) Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 5 ) } = ( 0 , 0 . 7 0 7 1 0 6 7 8 , 0 . 7 0 7 1 0 6 7 8 , 1 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives $\mathbf { x } ^ { ( 6 ) } = ( 0 . 8 1 6 4 9 6 5 8 , 0 . 4 0 8 2 4 8 2 9 , - 0 . 4 0 8 2 4 8 2 9 , 3 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives x $\mathbf { \Phi } _ { \mathrm { * } } ^ { ( \mathsf { 0 } ) } = ( 0 . 5 7 7 3 5 0 2 7 , - 0 . 5 7 7 3 5 0 2 7 , 0 . 5 7 7 3 5 0 2 7 , 6 )$ t. The other three solutions follow easily from part (a).

9. With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 - 1 ) ^ { t }$ and $T O L = 1 0 ^ { - 6 }$ , we have $\mathbf { x } ^ { ( 2 0 ) } = ( 0 . 5 , 9 . 5 \times 1 0 ^ { - 7 } , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ .

10. Since $f _ { j } ( x _ { 1 } , \ldots , x _ { n } ) = a _ { j 1 } x _ { 1 } + a _ { j 2 } x _ { 2 } + \ldots + a _ { j n } x _ { n } - b _ { j }$ , we have ${ \frac { \dot { o } f _ { j } } { \partial x _ { 1 } } } = a _ { j i }$ . Hence,

$$
J ( \mathbf { x } ) = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \dots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \dots } & { a _ { 2 n } } \\ { \vdots } & { } & { } & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \dots } & { a _ { n n } } \end{array} \right] } = A .
$$

Further,

$$
\mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \dots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \dots } & { a _ { 2 n } } \\ { \vdots } & & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \dots } & { a _ { n n } } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } ^ { ( 0 ) } } \\ { x _ { 2 } ^ { ( 0 ) } } \\ { \vdots } \\ { x _ { n } ^ { ( 0 ) } } \end{array} \right] } - { \left[ \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right] } = J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } - \mathbf { b } .
$$

Thus, given $\mathbf { x } ^ { ( 0 ) }$ , we have

$$
\begin{array} { r l } & { \mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \left( J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } - \mathbf { b } \right) } \\ & { \qquad = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } + J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \mathbf { b } = J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \mathbf { b } = A ^ { - 1 } \mathbf { b } . } \end{array}
$$

So given any $\mathbf { x } ^ { ( 0 ) }$ , the solution to the linear system is $\mathbf { x } ^ { ( 1 ) }$ .

11. When the dimension $n$ is $1$ , $\mathbf { F } ( \mathbf { x } )$ is a one-component function $f ( \mathbf { x } ) = f _ { 1 } ( \mathbf { x } )$ , and the vector $\mathbf { x }$ has only one component $x _ { 1 } = x$ . In this case, the Jacobian matrix $J ( \mathbf { x } )$ reduces to the $1 \times 1$ matrix $[ \partial f _ { 1 } / \partial x _ { 1 } ( { \bf x } ) ] = f ^ { \prime } ( { \bf x } ) = f ^ { \prime } ( x )$ . Thus, the vector equation

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } - J ( \mathbf { x } ^ { ( k - 1 ) } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ^ { ( k - 1 ) } )
$$

becomes the scalar equation

$$
x _ { k } = x _ { k - 1 } - f ( x _ { k - 1 } ) ^ { - 1 } f ( x _ { k - 1 } ) = x _ { k - 1 } - { \frac { f ( x _ { k - 1 } ) } { f ^ { \prime } ( x _ { k - 1 } ) } } .
$$

$^ { \ast } 1 2$ . The constants required for the pressure equation are in part (a). The approximate radius is in part (b).

(a) $k _ { 1 } = 8 . 7 7 1 2 5 , k _ { 2 } = 0 . 2 5 9 6 9 0 , k _ { 3 } = - 1 . 3 7 2 1 7$

(b) Solving the equation

$$
{ \frac { 5 0 0 } { \pi r ^ { 2 } } } = k _ { 1 } e ^ { k _ { 2 } r } + k _ { 3 } r
$$

numerically, gives $r = \mathrm { 3 . 1 8 5 1 7 }$ .

13. With $\theta _ { i } ^ { ( 0 ) } = 1$ , for each $i = 1 , 2 , \ldots , 2 0$ , the following results are obtained.

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td></td><td>0.14062</td><td>0.19954</td><td>0.24522</td><td>0.28413</td><td>0.31878</td><td>0.35045</td></tr></table>

<table><tr><td>i</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td></td><td>0.37990</td><td>0.40763</td><td>0.43398</td><td>0.45920</td><td>0.48348</td><td>0.50697</td><td>0.52980</td></tr></table>

<table><tr><td>i</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td></td><td>0.55205</td><td>0.57382</td><td>0.59516</td><td>0.61615</td><td>0.63683</td><td>0.65726</td><td>0.67746</td></tr></table>

14. (a) We have

$$
{ \frac { \partial E } { \partial a } } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) \left( { \frac { 1 } { ( x _ { i } - b ) ^ { c } } } \right) = 0 ,
$$

$$
\frac { \partial E } { \partial b } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - \frac { a } { ( x _ { i } - b ) ^ { c } } \right) \left( \frac { - a c } { ( x _ { i } - b ) ^ { c + 1 } } \right) = 0 ,
$$

and

$$
{ \frac { \partial E } { \partial c } } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) \ln ( x _ { i } - b ) \left( { \frac { - a } { ( x _ { i } - b ) ^ { c } } } \right) = 0 .
$$

Solving for $a$ in the first equation and substituting into the second and third equations gives the linear system.

(b) With $\mathbf { x } ^ { ( 0 ) } = ( 2 6 . 8 , 8 . 3 ) ^ { t } = ( b _ { 0 } , c _ { 0 } ) ^ { t }$ , we have $\mathbf { x } ^ { ( 7 ) } = ( 2 6 . 7 7 0 2 1 , 8 . 4 5 1 8 3 1 ) ^ { t }$ . Thus, $a =$ $2 . 2 1 7 9 5 2 \times 1 0 ^ { 6 }$ , $b = 2 6 . 7 7 0 2 1$ , $c = 8 . 4 5 1 8 3 1$ , and

$$
\sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) ^ { 2 } = 0 . 7 8 2 1 1 3 9 .
$$

# Exercise Set 10.3, page 652

1. Broyden’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 7 7 7 9 2 0 , 1 . 9 2 7 5 5 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 2 5 0 0 7 0 , - 0 . 1 3 8 6 9 6 7 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 2 2 9 3 7 2 , 0 . 8 2 4 3 4 9 1 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 7 7 9 5 0 0 , 1 . 7 4 3 3 9 6 ) ^ { t }$

2. Broyden’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 0 0 2 3 1 2 3 , - 1 . 0 8 0 2 9 9 0 9 , - 0 . 5 2 3 8 2 3 9 4 ) ^ { t }$ . \*(b) $\mathbf { x } ^ { ( 2 ) } = ( - 6 7 . 0 0 5 8 2 8 , 3 8 . 3 1 4 9 3 5 , 3 1 . 6 9 0 8 9 3 ) ^ { t }$ . (c) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 4 0 3 6 0 2 4 2 , - 1 . 6 7 9 8 7 5 2 4 , 0 . 4 5 8 1 6 5 0 9 ) ^ { t }$ (d) $\mathfrak { c } ^ { ( 2 ) } = ( 0 . 4 9 8 4 0 5 8 0 , - 0 . 1 9 9 8 4 2 0 9 , - 0 . 5 2 8 5 1 3 5 3 )$ t

3. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 , 2 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 3 7 3 6 9 8 2 , 0 . 0 5 6 2 6 6 4 9 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 0 . 5 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ .

4. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathfrak { c } ^ { ( 1 8 ) } = ( 0 . 4 9 9 9 9 9 5 3 , 0 . 0 0 3 1 9 9 0 4 , - 0 . 5 2 3 5 1 8 8 6 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 1 , - 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 0 ) } = ( 6 . 0 0 0 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 0 0 0 , - 4 . 0 0 0 0 0 0 0 0 0 0 ) ^ { \circ }$ t.   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( - 1 , - 2 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 1 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$ .

5. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 2 . 5 , 4 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 2 . 5 4 6 9 4 7 , 3 . 9 8 4 9 9 8 ) ^ { t }$   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 1 2 1 2 4 1 9 , 0 . 2 7 1 1 0 5 2 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 1 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 9 , - 1 , 0 . 5 ) ^ { t }$ ; and with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , - 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ .

6. (a) Suppose $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution to

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 . } } \end{array}
$$

Multiplying the first three equations by $^ { - 1 }$ and factoring gives

$$
\begin{array} { c } { { 4 ( - x _ { 1 } ) - ( - x _ { 2 } ) + ( - x _ { 3 } ) = ( - x _ { 1 } ) x _ { 4 } , } } \\ { { - ( - x _ { 1 } ) + 3 ( - x _ { 2 } ) - 2 ( - x _ { 3 } ) = ( - x _ { 2 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) - 2 ( - x _ { 2 } ) + 3 ( - x _ { 3 } ) = ( - x _ { 3 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) ^ { 2 } + ( - x _ { 2 } ) ^ { 2 } + ( - x _ { 3 } ) ^ { 2 } = 1 . } } \end{array}
$$

Thus, $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , - x _ { 4 } ) ^ { t }$ is also a solution.

(b) Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 6 ) } = ( 0 , 0 . 7 0 7 1 0 6 7 8 , 0 . 7 0 7 1 0 6 7 8 , 1 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives $\mathfrak { c } ^ { ( \mathrm { ~ 1 5 } ) } = ( 0 . 8 1 6 4 9 6 5 9 , 0 . 4 0 8 2 4 8 2 1 , - 0 . 4 0 8 2 4 8 3 7 , 3 ) ^ { t } .$ Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 5 7 7 3 5 0 3 4 , - 0 . 5 7 7 3 5 0 2 3 , 0 . 5 7 7 3 5 0 2 5 , 6 ) ^ { i }$ t. The other three solutions follow easily from part (a).

7. With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 - 1 ) ^ { t }$ , Broyden’s method gives $\mathbf { x } ^ { ( 5 6 ) } = ( 0 . 5 0 0 0 5 9 1 , 0 . 0 1 0 5 7 2 3 5 , - 0 . 5 2 2 4 8 1 8 ) ^ { t }$ $^ { * } 8$ . If $\mathbf { z } ^ { t } \mathbf { y } = 0$ , then ${ \bf z } = { \bf z } _ { 1 } + { \bf z } _ { 2 }$ , where $\mathbf { z } _ { 1 } = \mathbf { 0 }$ and $\mathbf { z } _ { 2 } = \mathbf { z }$ . Otherwise, let

$$
\mathbf { z } _ { 1 } = \frac { \mathbf { y } ^ { t } \mathbf { z } } { \| \mathbf { y } \| _ { 2 } ^ { 2 } } \mathbf { y }
$$

be parallel to $\mathbf { y }$ and let ${ \bf z } _ { 2 } = { \bf z } - { \bf z } _ { 1 }$ . Then

$$
\mathbf { z } _ { 2 } ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \mathbf { z } _ { 1 } ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \left[ \frac { \mathbf { y } ^ { t } \mathbf { z } } { \mathbf { y } ^ { t } \mathbf { y } } \mathbf { y } \right] ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \frac { \mathbf { z } ^ { t } \mathbf { y } } { \mathbf { y } ^ { t } \mathbf { y } } \mathbf { y } ^ { t } \mathbf { y } = 0 .
$$

$^ { * } 9$ . Let $\lambda$ be an eigenvalue of $M = \left( I + \mathbf { u v } ^ { t } \right)$ with eigenvector $\mathbf { x } \neq \mathbf { 0 }$ . Then

$$
\lambda \mathbf { x } = M \mathbf { x } = \left( I + \mathbf { u } \mathbf { v } ^ { t } \right) \mathbf { x } = \mathbf { x } + \left( \mathbf { v } ^ { t } \mathbf { x } \right) \mathbf { u } .
$$

Thus, $( \lambda - 1 ) \mathbf { x } = ( \mathbf { v } ^ { t } \mathbf { x } ) \mathbf { u }$ . If $\lambda = 1$ , then $\mathbf { v } ^ { t } \mathbf { x } = 0$ . So $\lambda = 1$ is an eigenvalue of $M$ with multiplicity $n - 1$ and eigenvectors $\mathbf { x } ^ { ( 1 ) } , \ldots , \mathbf { x } ^ { ( n - 1 ) }$ where $\mathbf { v } ^ { t } \mathbf { x } ^ { ( j ) } = 0$ , for $j = 1 , \ldots , n - 1$ .

Assuming $\lambda \neq 1$ implies $\mathbf { x }$ and $\mathbf { u }$ are parallel, so for some number $\alpha$ , we have $\mathbf { x } = \alpha \mathbf { u }$ . Then

$$
( \lambda - 1 ) \alpha \mathbf { u } = \left( \mathbf { v } ^ { t } ( \alpha \mathbf { u } ) \right) \mathbf { u } \quad { \mathrm { a n d } } \quad \alpha ( \lambda - 1 ) \mathbf { u } = \alpha \left( \mathbf { v } ^ { t } \mathbf { u } \right) \mathbf { u } ,
$$

which implies that

$$
\lambda - 1 = { \bf v } ^ { t } { \bf u } \quad \mathrm { o r } \quad \lambda = 1 + { \bf v } ^ { t } { \bf u } .
$$

Hence, $M$ has eigenvalues $\lambda _ { i }$ , $1 \leq i \leq n$ where $\lambda _ { i } = 1$ , for $i = 1 , \ldots , n - 1$ and $\lambda _ { n } = 1 + \mathbf { v } ^ { t } \mathbf { u }$ .   
Since $\begin{array} { r } { \operatorname* { d e t } M = \prod _ { i = 1 } ^ { n } \lambda _ { i } } \end{array}$ , we have $\operatorname* { d e t } M = 1 + \mathbf { v } ^ { t } \mathbf { u }$ .

$^ { * } 1 0$ . (a) Since $A ^ { - 1 }$ exists we can write $\operatorname* { d e t } \left( A + \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } \left( A + A A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } A \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } A \operatorname* { d e t } \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) .$ But $A ^ { - 1 }$ exists so $\operatorname* { d e t } A \neq 0$ . By Exercise 9, $\operatorname* { d e t } \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x }$ . So $\left( A + \mathbf { x } \mathbf { y } ^ { t } \right) ^ { - 1 }$ exists if and only if $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ .

(b) Assume $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ so that $\left( A + \mathbf { x } \mathbf { y } ^ { t } \right) ^ { - 1 }$ exists. Therefore,

$$
\begin{array} { r l } & { A ^ { - 1 } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } \bigg ] \left( A + \mathbf { x y } ^ { t } \right) = A ^ { - 1 } A - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } A } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } + A ^ { - 1 } \mathbf { x y } ^ { t } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } + A ^ { - 1 } \mathbf { x y } ^ { t } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } - A ^ { - 1 } \mathbf { x y } ^ { t } - \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } A ^ { - 1 } \mathbf { x y } ^ { t } + A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I + \frac { \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } A ^ { - 1 } \mathbf { x y } ^ { t } - \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \left( A ^ { - 1 } \mathbf { x y } ^ { t } \right) } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } = I . } \end{array}
$$

11. With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 7 5 , 1 . 2 5 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 7 5 0 1 9 4 8 , 1 . 1 8 4 7 1 2 ) ^ { t }$ . Thus, $a = 0 . 7 5 0 1 9 4 8 , b =$ 1.184712, and the error is 19.796.

# Exercise Set 10.4, page 659

1. The Steepest Descent method gives the following:

\*(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 4 9 4 3 5 4 1 , 1 . 9 4 8 0 4 0 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 0 . 5 0 6 8 0 3 0 4 , 0 . 9 1 7 8 0 0 5 1 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 1 . 7 3 6 0 8 3 , 1 . 8 0 4 4 2 8 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 6 1 0 0 9 2 , 0 . 0 5 7 8 8 3 6 8 ) ^ { t }$ .

2. The Steepest Descent method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 4 ) } = ( 1 . 0 4 3 6 0 5 , 1 . 0 6 4 0 5 8 , 0 . 9 2 4 6 1 1 8 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 0 . 4 9 3 2 7 3 9 , 0 . 9 8 6 3 8 8 8 , - 0 . 5 1 7 5 9 6 4 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( - 1 . 6 0 8 2 9 6 , - 1 . 1 9 2 7 5 0 , 0 . 7 2 0 5 6 4 2 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 0 , 0 . 0 0 9 8 9 0 5 6 , 0 . 9 8 9 0 5 5 6 ) ^ { t }$ .

3. The Steepest Descent method with Newton’s method gives the following:

\*(a) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 2 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 7 3 6 9 8 2 , 0 . 0 5 6 2 6 6 4 9 ) ^ { t }$

4. The Steepest Descent method with Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 0 0 0 0 0 0 0 , 0 . 1 0 0 0 0 0 0 1 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$

5 . The Steepest Descent method gives the following:

(a) $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { i }$ t (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 0 0 0 0 0 0 0 , 0 . 1 0 0 0 0 0 0 1 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$

$^ { * } 6$ . (a) We have $\alpha _ { 1 } = 0$ , $g _ { 1 } = g ( x _ { 1 } , . . . , x _ { n } ) = g \left( \mathbf { x } ^ { ( 0 ) } \right) = h ( \alpha _ { 1 } )$ , $\begin{array} { r } { g _ { 3 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) = } \end{array}$ $h \big ( \alpha _ { 3 } \big )$ , $g _ { 2 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) = h ( \alpha _ { 2 } )$ ,

$$
\begin{array} { r l } & { h _ { 1 } = \displaystyle \frac { \left( g _ { 2 } - g _ { 1 } \right) } { \left( \alpha _ { 2 } - \alpha _ { 1 } \right) } = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 1 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 1 } , \alpha _ { 2 } ] , } \\ & { h _ { 2 } = \displaystyle \frac { \left( g _ { 3 } - g _ { 2 } \right) } { \left( \alpha _ { 3 } - \alpha _ { 2 } \right) } = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 2 } , \alpha _ { 3 } ] , } \\ & { h _ { 3 } = \displaystyle \frac { \left( h _ { 2 } - h _ { 1 } \right) } { \left( \alpha _ { 3 } - \alpha _ { 1 } \right) } } \\ & { \quad = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 1 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } ] . } \end{array}
$$

The Newton divided-difference form of the second interpolating polynomial is

$$
\begin{array} { l } { { P ( \alpha ) = h [ \alpha _ { 1 } ] + h [ \alpha _ { 1 } , \alpha _ { 2 } ] ( \alpha - \alpha _ { 1 } ) + h [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } ] ( \alpha - \alpha _ { 1 } ) ( \alpha - \alpha _ { 2 } ) } } \\ { { \qquad = g _ { 1 } + h _ { 1 } ( \alpha - \alpha _ { 1 } ) + h _ { 3 } ( \alpha - \alpha _ { 1 } ) ( \alpha - \alpha _ { 2 } ) } } \\ { { \qquad = g _ { 1 } + h _ { 1 } \alpha + h _ { 3 } \alpha ( \alpha - \alpha _ { 2 } ) . } } \end{array}
$$

(b) $P ^ { \prime } ( \alpha ) = h _ { 1 } - \alpha _ { 2 } h _ { 3 } + 2 h _ { 3 } \alpha$ , so $P ^ { \prime } ( \alpha ) = 0$ when $\alpha = 0 . 5 ( \alpha _ { 2 } - h _ { 1 } / h _ { 3 } )$ .

# Exercise Set 10.5, page 666

1. The Continuation method and Eulers method gives:

(a) (3, −2.25)t (b) (0.42105263, 2.6184211)t (c) (2.173110, −1.3627731)t

2. The Continuation method and Eulers method gives:

(a) (2.3039880, −2.0010995)t (b) (0.59709702, 2.2579684)t (c) (2.1094460, −1.3345633)t

3. Using the Continuation method and Eulers method gives:

\*(a) (0.44006047, 1.8279835)t (b) $( - 0 . 4 1 3 4 2 6 1 3 , 0 . 0 9 6 6 9 4 6 8 ) ^ { \tau }$ (c) $( 0 . 4 9 8 5 8 9 0 9 , 0 . 2 4 9 9 9 0 9 1 , - 0 . 5 2 0 6 7 9 7 8 ) ^ { v }$ (d) $( 6 . 1 9 3 5 4 8 4 , 1 8 . 5 3 2 2 5 8 , - 2 1 . 7 2 5 8 0 6 ) ^ { u }$

4. (a) ( $- 1 5 . 7 8 4 3 2 7 2 4 , 5 . 2 9 9 7 4 5 8 9 ) ^ { t }$ is not comparable using $\mathbf { x } ( 0 ) \ : = \ : ( 0 , 0 ) ^ { t }$ as starting value. Using the starting values as in 10.2 Exercise $5 ( \mathrm { c } )$ gives: $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ leads to $( - 1 , 3 . 5 ) ^ { t }$ , and $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ leads to (2.54694647, 3.9849976) $t$ (b) $( 0 . 1 2 1 2 4 1 9 5 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ using $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ is comparable to Newton’s method. Using $\mathbf { x } ( 0 ) = ( 0 , 0 ) ^ { t }$ leads to an error in the program. (c) $( 1 . 0 3 6 4 5 8 8 0 , 1 . 0 8 5 7 2 5 0 2 , 0 . 9 3 1 3 6 7 1 4 ) ^ { t }$ is comparable to Newton’s method. (d) Using $\mathbf { x } ( 0 ) = ( 0 , 0 , 0 ) ^ { t }$ does not allow computation of $\mathbf { x } ( 1 )$ . Using $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ gives $( 0 . 9 0 0 1 6 0 7 4 , - 1 . 0 0 2 3 8 0 0 8 , 0 . 4 9 6 6 1 0 9 3 ) ^ { u }$ which is nearly comparable to Newton’s method.

5. The Continuation method and the RungeKutta method of order four gives:

(a) With $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ the result is $( - 1 , 3 . 5 ) ^ { t }$ . \* With $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ the result is (2.54694647, 3.98499746)t.   
(b) With $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ the result is $( 0 . 1 2 1 2 4 1 9 5 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ .   
(c) With $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 ) ^ { t }$ the result is $( 1 . 0 3 6 4 0 0 4 7 , 1 . 0 8 5 7 0 6 5 5 , 0 . 9 3 1 1 9 1 4 4 ) ^ { \iota } .$ .

(d) With $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ the result is $( 0 . 9 0 0 1 6 0 7 4 , - 1 . 0 0 2 3 8 0 0 8 , 0 . 4 9 6 6 1 0 9 3 7 ) ^ { \tau } .$ With $\mathbf { x } ( 0 ) = ( 1 , 1 , - 1 ) ^ { t }$ the result is $( 0 . 5 0 1 0 4 0 3 5 , 1 . 0 0 2 3 8 0 0 8 , - 0 . 4 9 6 6 1 0 9 3 ) ^ { v }$ .

6. The Continuation method and the RungeKutta method of order four gives:

(a) $\left( 0 . 4 9 9 5 0 4 5 1 , 0 . 8 6 6 3 5 6 9 1 \right)$ t. This result is comparable since it required only 4 matrix inversions to obtain an answer almost as accurate as in Section 10.2 Exercise 3a with 5 iterations.   
(b) (1.7730066, 1.7703057)t. This result is comparable since it required only 4 matrix inversions to obtain an answer almost as accurate as in Section 10.2 Exercise 3b with 6 iterations.   
(c) $( - 1 . 4 5 6 9 2 1 7 , - 1 . 6 6 4 5 2 9 2 , 0 . 4 2 1 3 8 6 1 6 ) ^ { v }$ . This result is comparable to the result obtained in Section 10.2 Exercise 3c since it required only 4 matrix inversions as compared to 5 iterations of Newton’s method.   
(d) $( 0 . 4 9 8 1 3 3 6 4 , - 0 . 1 9 9 5 7 9 1 7 , - 0 . 5 2 8 8 2 7 7 3 ) ^ { \tau }$ . This result is comparable to the result obtained in Section 10.2 Exercise 3d.

7. The Continuation method and the RungeKutta method of order four gives:

(a) With $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ the result is $( - 1 , 3 . 5 ) ^ { t }$ . With $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ the result is $( 2 . 5 4 6 9 4 6 5 , 3 . 9 8 4 9 9 7 5 ) ^ { t }$ .   
(b) With $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ the result is $( 0 . 1 2 1 2 4 1 9 1 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ .   
(c) With $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 ) ^ { t }$ the result is $( 1 . 0 3 6 4 0 0 4 7 , 1 . 0 8 5 7 0 6 5 5 , 0 . 9 3 1 1 9 1 4 4 ) ^ { \upsilon }$ .   
(d) With $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ the result is $( 0 . 9 0 0 1 5 9 6 4 , - 1 . 0 0 0 2 1 8 2 6 , 0 . 4 9 9 6 8 9 4 4 ) ^ { \iota }$ . With $\mathbf { x } ( 0 ) = ( 1 , 1 , - 1 ) ^ { t }$ the result is $( 0 . 5 0 0 9 6 5 3 , 1 . 0 0 0 2 1 8 2 6 , - 0 . 4 9 9 6 8 9 4 4 ) ^ { u }$ .

8. Using $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives

$$
\mathbf { x } ( 1 ) = \left( 1 0 ^ { - 1 0 } , 0 . 7 0 4 7 6 1 9 0 4 9 , 0 . 7 0 4 7 6 1 9 0 4 9 , 1 \right) ^ { t } .
$$

Using $\mathbf { x } ( 0 ) = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives

x(1) = (0.8171787148, 0.4035113851, −0.4035113850, 2.993229684)t.

Using $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives

$$
\mathbf { x } ( 1 ) = ( 0 . 5 7 6 9 8 4 1 3 8 7 , - 0 . 5 7 6 9 8 4 1 2 3 9 , 0 . 5 7 6 9 8 4 1 2 4 6 , 6 . 0 1 9 6 0 3 1 6 2 ) ^ { t }
$$

The other three solutions follow easily from Exercise 6(a) of Section 10.2.

9. The Continuation method and the RungeKutta method of order four gives the approximate solution, (0.50024553, 0.078230039, −0.52156996)t

$^ { * } 1 0$ . The system of differential equations to solve by Euler’s method is

$$
\begin{array} { r } { \mathbf { x } ^ { \prime } ( \lambda ) = - [ J ( \mathbf { x } ( \lambda ) ) ] ^ { - 1 } F ( \mathbf { x } ( 0 ) ) . } \end{array}
$$

With $N = 1$ , we have $h = 1$ and

$$
\mathbf { x } ( 1 ) = \mathbf { x } ( 0 ) + h [ - J ( \mathbf { x } ( 0 ) ) ] ^ { - 1 } F ( \mathbf { x } ( 0 ) ) = \mathbf { x } ( 0 ) - h J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) = \mathbf { x } ( 0 ) - J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) )
$$

However, Newton’s method gives

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } F \left( \mathbf { x } ^ { ( 0 ) } \right) .
$$

Since $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ , we have $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$ .

11. For each $\lambda$ , we have

$$
0 = G ( \lambda , { \bf x } ( \lambda ) ) = F ( { \bf x } ( \lambda ) ) - e ^ { - \lambda } F ( { \bf x } ( 0 ) ) ,
$$

so

$$
0 = \frac { \partial F ( \mathbf { x } ( \lambda ) ) } { \partial \mathbf { x } } \frac { d \mathbf { x } } { d \lambda } + e ^ { - \lambda } F ( \mathbf { x } ( 0 ) ) = J ( \mathbf { x } ( \lambda ) ) \mathbf { x } ^ { \prime } ( \lambda ) + e ^ { - \lambda } F ( \mathbf { x } ( 0 ) )
$$

and

$$
J ( { \bf x } ( \lambda ) ) { \bf x } ^ { \prime } ( \lambda ) = - e ^ { - \lambda } F ( { \bf x } ( 0 ) ) = - F ( { \bf x } ( 0 ) ) .
$$

Thus

$$
\begin{array} { r } { \mathbf { x } ^ { \prime } ( \lambda ) = - J ( \mathbf { x } ( \lambda ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) . } \end{array}
$$

With $N = 1$ , we have $h = 1$ so that

$$
\mathbf { x } ( 1 ) = \mathbf { x } ( 0 ) - J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) .
$$

However, Newton’s method gives

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J ( \mathbf { x } ^ { ( 0 ) } ) ^ { - 1 } F ( \mathbf { x } ^ { ( 0 ) } ) .
$$

Since $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ , we have $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$

12. (a) The CMRK4 algorithm with $N = 1$ requires the solution of 4 linear systems, which is almost as much work as required for 4 iterations of Newton’s method. Exercises 5, 6, and 8 yield appropriate comparisons. In only 5a, 5b, and 5c was CMRK4 competitive with Newton’s method. This suggests that CMRK4 with $N = 1$ is not as good as Newton’s Method. (b) Generally, the CMRK4 algorithm would yield good initial approximations for Newton’s method. This is well illustrated in Exercises 4b, 4c, 4d, 5, 6, and 8. (c) The CMRK4 algorithm with $N = 2$ requires the solution of 8 linear systems, which is almost as much work as required for 8 iterations of Newton’s method. Exercises 7 and 9 yield appropriate comparisons. Newton’s method outperformed CMRK4 in Exercise 7. The CMRK4 algorithm worked well in Exercise 9 which had the singular Jacobian. The results here suggest that CMRK4 with $N = 2$ is not as good as Newton’s method. (d) Since the CMRK4 algorithm with $N = 1$ generally yields good initial approximations for Newton’s method, we would not need to use the CMRK4 algorithm with $N = 2$ for this purpose.

# Boundary-Value Problems for Ordinary Differential Equations

Exercise Set 11.1, page 677

1. The Linear Shooting Algorithm gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.5</td><td>0.82432432</td><td>0.82402714</td></tr></table>

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.3937095</td><td>0.3936767</td></tr><tr><td>2</td><td>0.50</td><td>0.8240948</td><td>0.8240271</td></tr><tr><td>3</td><td>0.75</td><td>1.337160</td><td>1.337086</td></tr></table>

2. The Linear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.78539816</td><td>-0.28245222</td><td>-0.28284271</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>π/8</td><td>-0.31541496</td><td>-0.31543220</td></tr><tr><td>2</td><td>π/4</td><td>-0.2828507</td><td>-0.282842712</td></tr><tr><td>3</td><td>3π/8</td><td>-0.20718437</td><td>-0.20719298</td></tr></table>

3. The Linear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>0.7833204</td><td>0.7831923</td></tr><tr><td>6</td><td>0.6</td><td>0.6023521</td><td>0.6022801</td></tr><tr><td>9</td><td>0.9</td><td>0.8568906</td><td>0.8568760</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.1676179</td><td>0.1676243</td></tr><tr><td>10</td><td>1.50</td><td>0.4581901</td><td>0.4581935</td></tr><tr><td>15</td><td>1.75</td><td>0.6077718</td><td>0.6077740</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>-0.5185754</td><td>-0.5185728</td></tr><tr><td>6</td><td>0.6</td><td>-0.2195271</td><td>-0.2195247</td></tr><tr><td>9</td><td>0.9</td><td>-0.0406577</td><td>-0.0406570</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.0655336</td><td>0.06553420</td></tr><tr><td>6</td><td>1.6</td><td>0.0774590</td><td>0.07745947</td></tr><tr><td>9</td><td>1.9</td><td>0.0305619</td><td>0.03056208</td></tr></table>

4. The Linear Shooting Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>W2i</td></tr><tr><td>1</td><td>0.15707963</td><td>1.05248506</td><td>0.25267869</td></tr><tr><td>2</td><td>0.31415927</td><td>1.07905470</td><td>0.08492370</td></tr><tr><td>3</td><td>0.47123890</td><td>1.07905469</td><td>-0.08492234</td></tr><tr><td>4</td><td>0.62831853</td><td>1.05248505</td><td>-0.25267729</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>W2i</td></tr><tr><td>1</td><td>0.15707963</td><td>-0.06061198</td><td>-0.29443007</td></tr><tr><td>2</td><td>0.31415927</td><td>-0.09117479</td><td>-0.09251254</td></tr><tr><td>3</td><td>0.47123890</td><td>-0.08959214</td><td>0.11091096</td></tr><tr><td>4</td><td>0.62831853</td><td>-0.05748564</td><td>0.29239128</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>W2i</td></tr><tr><td>5</td><td>1.25000000</td><td>0.64314227</td><td>0.28800448</td></tr><tr><td>10</td><td>1.50000000</td><td>0.68324209</td><td>0.07407700</td></tr><tr><td>15</td><td>1.75000000</td><td>0.69226853</td><td>0.01166358</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>W2i</td></tr><tr><td>3</td><td>0.60000000</td><td>-0.71219638</td><td>-1.82098025</td></tr><tr><td>5</td><td>1.00000000</td><td>-1.64068454</td><td>-2.81187530</td></tr><tr><td>8</td><td>1.60000000</td><td>-3.52051591</td><td>-2.83551329</td></tr></table>

\*5. The Linear Shooting Algorithm with $h = 0 . 0 5$ gives the following results.

<table><tr><td colspan="2"></td></tr><tr><td>i</td><td>Xi W1i</td></tr><tr><td>6 0.3</td><td>0.04990547</td></tr><tr><td>10 0.5</td><td>0.00673795</td></tr><tr><td>16 0.8</td><td>0.00033755</td></tr></table>

The Linear Shooting Algorithm with $h = 0 . 1$ gives the following results.

<table><tr><td>i Xi</td><td>W1i</td></tr><tr><td>3 0.3</td><td>0.05273437</td></tr><tr><td>5</td><td>0.5 0.00741571</td></tr><tr><td>8 0.8</td><td>0.00038976</td></tr></table>

$^ { * } 6$ . For Eq. (11.3), let $u _ { 1 } ( x ) = y$ and $u _ { 2 } ( x ) = y ^ { \prime }$ . Then

$$
u _ { 1 } ^ { \prime } ( x ) = u _ { 2 } ( x ) , \quad a \leq x \leq b , \quad u _ { 1 } ( a ) = \alpha
$$

and

$$
u _ { 2 } ^ { \prime } ( x ) = p ( x ) u _ { 2 } ( x ) + q ( x ) u _ { 1 } ( x ) + r ( x ) , \quad a \leq x \leq b , \quad u _ { 2 } ( a ) = 0 .
$$

For Eq. (11.4), let $v _ { 1 } ( x ) = y$ and $v _ { 2 } ( x ) = y ^ { \prime }$ . Then

$$
v _ { 1 } ^ { \prime } ( x ) = v _ { 2 } ( x ) , \quad a \leq x \leq b , \quad v _ { 1 } ( a ) = 0
$$

and

$$
v _ { 2 } ^ { \prime } ( x ) = p ( x ) v _ { 2 } ( x ) + q ( x ) v _ { 1 } ( x ) , \quad a \leq x \leq b , \quad v _ { 2 } ( a ) = 1 .
$$

Using the notation $u _ { 1 , i } = u _ { 1 } ( x _ { i } )$ , $u _ { 2 , i } = u _ { 2 } ( x _ { i } )$ , $v _ { 1 , i } = v _ { 1 } ( x _ { i } )$ and $v _ { 2 , i } = v _ { 2 } ( x _ { i } )$ leads to the equations in Step 4 of Algorithm 11.1.

7. (a) The approximate potential is $u ( 3 ) \approx 3 6 . 6 6 7 0 2$ using $h = 0 . 1$ . (b) The actual potential is $u ( 3 ) = 3 6 . 6 6 6 6 7$ .

$^ { * } 8$ . Since $y _ { 2 } ( a ) = 0$ and $y _ { 2 } ( b ) = 0$ , the boundary value problem

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y , \quad a \leq x \leq b , \quad y ( a ) = 0 , \quad y ( b ) = 0
$$

has $y = 0$ as a unique solution, so $y _ { 2 } \equiv 0$ .

9. (a) There are no solutions if $b$ is an integer multiple of $\pi$ and $B \neq 0$ . (b) A unique solution exists whenever $b$ is not an integer multiple of $\pi$ . (c) There is an infinite number of solutions if $b$ is an multiple integer of $\boldsymbol { \mathscr { u } }$ and $B = 0$ .

$^ *$ 10. The unique solution is $y ( x ) = B \left( e ^ { x } - e ^ { - x } \right) / \left( e ^ { b } - e ^ { - b } \right)$ . For Exercise 9, we have $q ( x ) < 0$ , so Corollary 11.2 does not apply.

# Exercise Set 11.2, page 684

$^ { * } 1$ . The Nonlinear Shooting Algorithm gives $w _ { 1 } = 0 . 4 0 5 5 0 5 \approx \ln 1 . 5 = 0 . 4 0 5 4 6 5$ . 2. The Nonlinear Shooting Algorithm with $h = 0 . 2 5$ requires 4 iterations and gives:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>-0.75</td><td>0.44444651</td><td>0.44444444</td></tr><tr><td>2</td><td>-0.5</td><td>0.40000229</td><td>0.4</td></tr><tr><td>3</td><td>-0.25</td><td>0.36363809</td><td>0.36363636</td></tr></table>

3. The Nonlinear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>1.1</td><td>0.09530982</td><td>0.09531018</td></tr><tr><td>2</td><td>1.2</td><td>0.18232094</td><td>0.18232156</td></tr><tr><td>3</td><td>1.3</td><td>0.26236347</td><td>0.26236426</td></tr><tr><td>4</td><td>1.4</td><td>0.33647129</td><td>0.33647224</td></tr><tr><td>5</td><td>1.5</td><td>0.40546403</td><td>0.40546511</td></tr><tr><td>6</td><td>1.6</td><td>0.47000243</td><td>0.47000363</td></tr><tr><td>7</td><td>1.7</td><td>0.53062693</td><td>0.53062825</td></tr><tr><td>8</td><td>1.8</td><td>0.58778522</td><td>0.58778666</td></tr><tr><td>9</td><td>1.9</td><td>0.64185232</td><td>0.64185389</td></tr><tr><td>10</td><td>2.0</td><td>0.69314549</td><td>0.69314718</td></tr></table>

Convergence in 4 iterations gives $t = 1 . 0 0 0 0 0 1 7$

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>1.16934027</td><td>1.16933413</td></tr><tr><td>2</td><td>0.31415927</td><td>1.36209813</td><td>1.36208552</td></tr><tr><td>3</td><td>0.47123890</td><td>1.57460167</td><td>1.57458304</td></tr><tr><td>4</td><td>0.62831853</td><td>1.80002060</td><td>1.79999746</td></tr><tr><td>5</td><td>0.78539816</td><td>2.02814008</td><td>2.02811498</td></tr><tr><td>6</td><td>0.94247780</td><td>2.24572329</td><td>2.24569937</td></tr><tr><td>7</td><td>1.09955743</td><td>2.43760187</td><td>2.43758190</td></tr><tr><td>8</td><td>1.25663706</td><td>2.58845757</td><td>2.58844295</td></tr><tr><td>9</td><td>1.41371669</td><td>2.68503045</td><td>2.68502044</td></tr><tr><td>10</td><td>1.57079633</td><td>2.71829004</td><td>2.71828183</td></tr></table>

Convergence requires 4 iterations and gives $t = 1 . 0 0 0 0 3 0 1$ .

(c)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.83775804</td><td>0.86205941</td><td>0.86205848</td></tr><tr><td>2</td><td>0.89011792</td><td>0.88156057</td><td>0.88155882</td></tr><tr><td>3</td><td>0.94247780</td><td>0.89945618</td><td>0.89945372</td></tr><tr><td>4</td><td>0.99483767</td><td>0.91579268</td><td>0.91578959</td></tr><tr><td>5</td><td>1.04719755</td><td>0.93060849</td><td>0.93060486</td></tr></table>

Convergence requires 3 iterations and gives $t = 0 . 4 2 0 4 6 7 2 5$ .

(d)

<table><tr><td>i</td><td>Xi</td><td>W1i</td></tr><tr><td>1</td><td>0.15707963</td><td>2.15645346 2.15643446</td></tr><tr><td>2</td><td>0.31415927</td><td>2.30905208 2.30901699</td></tr><tr><td>3</td><td>0.47123890</td><td>2.45403919 2.45399050</td></tr><tr><td>4</td><td>0.62831853</td><td>2.58784539 2.58778525</td></tr><tr><td>5</td><td>0.78539816</td><td>2.70717651 2.70710678</td></tr><tr><td>6</td><td>0.94247780</td><td>2.80909468 2.80901699</td></tr><tr><td>7</td><td>1.09955743</td><td>2.89109072 2.89100652</td></tr><tr><td>8</td><td>1.25663706</td><td>2.95114591 2.95105652</td></tr><tr><td>9</td><td>1.41371669</td><td>2.98778172 2.98768834</td></tr><tr><td>10</td><td>1.57079633</td><td>3.00009624 3.00000000</td></tr><tr><td>11</td><td>1.72787596</td><td>2.98778634 2.98768834</td></tr><tr><td>12</td><td>1.88495559</td><td>2.95115520 2.95105652</td></tr><tr><td>13</td><td>2.04203522</td><td>2.89110479 2.89100652</td></tr><tr><td>14</td><td>2.19911486</td><td>2.80911373 2.80901699</td></tr><tr><td>15</td><td>2.35619449</td><td>2.70720082 2.70710678</td></tr><tr><td>16</td><td>2.51327412</td><td>2.58787536 2.58778525</td></tr><tr><td>17</td><td>2.67035376</td><td>2.45407537 2.45399050</td></tr><tr><td>18</td><td>2.82743339</td><td>2.30909523 2.30901699</td></tr><tr><td>19</td><td>2.98451302</td><td>2.15650454 2.15643446</td></tr><tr><td>20</td><td>3.14159265</td><td>2.00006028 2.00000000</td></tr></table>

Convergence requires 8 iterations and gives $t = 1 . 0 0 0 1 2 5 3$ .

4. The Nonlinear Shooting Algorithm gives the results in the following tables.

\*(a) 4 iterations are required, giving:

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.4347835</td><td>0.4347826</td></tr><tr><td>6</td><td>1.6</td><td>0.3846170</td><td>0.3846154</td></tr><tr><td>9</td><td>1.9</td><td>0.3448300</td><td>0.3448276</td></tr></table>

(b) 6 iterations are required, giving:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi</td></tr><tr><td>3</td><td>1.3</td><td>2.069249</td><td>2.069231</td></tr><tr><td>6</td><td>1.6</td><td>2.225013</td><td>2.225000</td></tr><tr><td>9</td><td>1.9</td><td>2.426317</td><td>2.426316</td></tr></table>

(c) 3 iterations are required, giving:

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>2.3</td><td>1.2676912</td><td>1.2676917</td></tr><tr><td>6</td><td>2.6</td><td>1.3401256</td><td>1.3401268</td></tr><tr><td>9</td><td>2.9</td><td>1.4095359</td><td>1.4095383</td></tr></table>

(d) To apply the algorithm we need to redefine the initial value of $T K$ to be 2. Then 7 iterations are required, giving:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>5</td><td>1.25</td><td>0.4358290</td><td>0.4358272</td></tr><tr><td>10</td><td>1.50</td><td>1.3684496</td><td>1.3684447</td></tr><tr><td>15</td><td>1.75</td><td>2.9992010</td><td>2.9991909</td></tr></table>

5. \*(a) Modify Algorithm 11.2 as follows:

STEP 1 Set $h = ( b - a ) / N$ ; $k = 2$ ; $T K 1 = ( \beta - \alpha ) / ( b - a ) .$ .   
STEP 2 Set $w _ { 1 , 0 } = \alpha$ ; $w _ { 2 , 0 } = T K 1$ .   
STEP 3 For $i = 1 , \ldots , N$ do Steps 4 and 5.

STEP 4 Set $x = a + ( i - 1 ) h$ . STEP 5 Set

$$
\begin{array} { r l } & { k _ { 1 , 1 } = h w _ { 2 , i - 1 } ; } \\ & { k _ { 1 , 2 } = h f ( x , w _ { 1 , i - 1 } , w _ { 2 , i - 1 } ) ; } \\ & { k _ { 2 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 1 , 2 } / 2 ) ; } \\ & { k _ { 2 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 1 , 1 } / 2 , w _ { 2 , i - 1 } + k _ { 1 , 2 } / 2 ) ; } \\ & { k _ { 3 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 2 , 2 } / 2 ) ; } \\ & { k _ { 3 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 2 , 1 } / 2 , w _ { 2 , i - 1 } + k _ { 2 , 2 } / 2 ) ; } \\ & { k _ { 4 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 3 , 2 } / 2 ) ; } \\ & { k _ { 4 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 3 , 1 } , w _ { 2 , i - 1 } + k _ { 3 , 2 } ) ; } \\ & { w _ { 1 , i } = w _ { 1 , i - 1 } + \big ( k _ { 1 , 1 } + 2 k _ { 2 , 1 } + 2 k _ { 3 , 1 } + k _ { 4 , 1 } \big ) / 6 ; } \\ & { w _ { 2 , i } = w _ { 2 , i - 1 } + \big ( k _ { 1 , 2 } + 2 k _ { 2 , 2 } + 2 k _ { 3 , 2 } + k _ { 4 , 2 } \big ) / 6 . } \end{array}
$$

STEP 6 Set $T K 2 = T K 1 + ( \beta - w _ { 1 , N } ) / ( b - a )$ .   
STEP 7 While $k \leq M )$ do Steps 8–15.   
STEP 8 Set $w _ { 2 , 0 } = T \kappa 2$ ; HOLD = w1,N.   
STEP 9 For i = 1, . . . , N do Steps 10 and 11. STEP 10 (Same as STEP 4 ) STEP 11 (Same as STEP 5 )   
STEP 12 If $| w _ { 1 , N } - \beta | \leq T O L$ then do Steps 13 and 14. STEP 13 For $i = 0 , \ldots , N$ set $x = a + i h$ ; $\operatorname { O U T P U T } ( x , w _ { 1 , i } , w _ { 2 , i } )$ . STEP 14 STOP.   
STEP 15 Set $\begin{array} { r l } & { T K = T K 2 - ( w _ { 1 , N } - \beta ) ( T K 2 - T K 1 ) / ( w _ { 1 . N } - H O L D ) ; } \\ & { T K 1 = T K 2 ; } \\ & { T K 2 = T K ; } \\ & { k = k + 1 . } \end{array}$

STEP 16 OUTPUT(’Maximum number of iterations exceeded.’); STOP.

(b) For 3(a), 3 iterations give:

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>1.2</td><td>0.45453896</td><td>0.45454545</td></tr><tr><td>2</td><td>1.4</td><td>0.41665348</td><td>0.41666667</td></tr><tr><td>3</td><td>1.6</td><td>0.38459538</td><td>0.38461538</td></tr><tr><td>4</td><td>1.8</td><td>0.35711592</td><td>0.35714286</td></tr></table>

For 3(c), 3 iterations give:

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>2.2</td><td>1.24299575</td><td>1.24300281</td></tr><tr><td>2</td><td>2.4</td><td>1.29211897</td><td>1.29213540</td></tr><tr><td>3</td><td>2.6</td><td>1.34009800</td><td>1.34012683</td></tr><tr><td>4</td><td>2.8</td><td>1.38671706</td><td>1.38676227</td></tr></table>

# Exercise Set 11.3, page 689

$^ { * } 1$ . The Linear Finite-Difference Algorithm gives following results.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>1</td><td>0.5</td><td>0.83333333</td><td>0.82402714</td></tr></table>

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.39512472</td><td>0.39367669</td></tr><tr><td>2</td><td>0.5</td><td>0.82653061</td><td>0.82402714</td></tr><tr><td>3</td><td>0.75</td><td>1.33956916</td><td>1.33708613</td></tr></table>

(c) Extrapolation gives

$$
y \left( { \frac { 1 } { 2 } } \right) \approx { \frac { 4 ( 0 . 8 2 6 5 3 0 6 1 ) - 0 . 8 3 3 3 3 3 3 3 } { 3 } } = 0 . 8 2 4 2 6 3 0 4
$$

2. The Linear Finite-Difference Algorithm gives following results.

(a)

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>T/4</td><td>-0.28287080</td><td>-0.282842712</td></tr><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>π/8</td><td>-0.31568540</td><td>-0.31543220</td></tr><tr><td>2</td><td>π/4</td><td>-0.28290585</td><td>-0.282842712</td></tr><tr><td>3</td><td>3π/8</td><td>-0.20699563</td><td>-0.20719298</td></tr></table>

(c) Extrapolation gives

$$
y \left( { \frac { \pi } { 4 } } \right) \approx { \frac { 4 ( - 0 . 2 8 2 9 0 5 8 5 ) - ( - 0 . 2 8 2 8 7 0 8 0 ) } { 3 } } = - 0 . 2 8 2 9 1 7 5 3 3
$$

3. The Linear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>0.2</td><td>1.018096</td><td>1.0221404</td></tr><tr><td>5</td><td>0.5</td><td>0.5942743</td><td>0.59713617</td></tr><tr><td>7</td><td>0.7</td><td>0.6514520</td><td>0.65290384</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.16797186</td><td>0.16762427</td></tr><tr><td>10</td><td>1.50</td><td>0.45842388</td><td>0.45819349</td></tr><tr><td>15</td><td>1.75</td><td>0.60787334</td><td>0.60777401</td></tr></table>

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>-0.5183084</td><td>-0.5185728</td></tr><tr><td>6</td><td>0.6</td><td>-0.2192657</td><td>-0.2195247</td></tr><tr><td>9</td><td>0.9</td><td>-0.0405748</td><td>-0.04065697</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>1.3</td><td>0.0654387</td><td>0.0655342</td></tr><tr><td>6</td><td>1.6</td><td>0.0773936</td><td>0.0774595</td></tr><tr><td>9</td><td>1.9</td><td>0.0305465</td><td>0.0305621</td></tr></table>

4. The Linear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>1.05260081</td><td>1.05248562</td></tr><tr><td>2</td><td>0.31415927</td><td>1.07922974</td><td>1.07905555</td></tr><tr><td>3</td><td>0.47123890</td><td>1.07922974</td><td>1.07905555</td></tr><tr><td>4</td><td>0.62831853</td><td>1.05260081</td><td>1.05248562</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>-0.06141845</td><td>-0.06062540</td></tr><tr><td>2</td><td>0.31415927</td><td>-0.09240491</td><td>-0.09119581</td></tr><tr><td>3</td><td>0.47123890</td><td>-0.09080499</td><td>-0.08961338</td></tr><tr><td>4</td><td>0.62831853</td><td>-0.05825827</td><td>-0.05749950</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.64328225</td><td>0.64314355</td></tr><tr><td>10</td><td>1.50</td><td>0.68332838</td><td>0.68324289</td></tr><tr><td>15</td><td>1.75</td><td>0.69230217</td><td>0.69226885</td></tr><tr><td>3</td><td>0.6</td><td>-0.70664241</td><td>-0.71228492</td></tr><tr><td>5</td><td>1.0</td><td>-1.63674050</td><td>-1.64085909</td></tr><tr><td>8</td><td>1.6</td><td>-3.52936107</td><td>-3.52075148</td></tr></table>

$^ { * } 5$ . The Linear Finite-Difference Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>xXi</td><td>wi(h = 0.1)</td><td>i</td><td>Mi</td><td>wi(h = 0.05)</td></tr><tr><td>3</td><td>0.3</td><td>0.05572807</td><td>6</td><td>0.3</td><td>0.05132396</td></tr><tr><td>6</td><td>0.6</td><td>0.00310518</td><td>12</td><td>0.6</td><td>0.00263406</td></tr><tr><td>9</td><td>0.9</td><td>0.00016516</td><td>18</td><td>0.9</td><td>0.00013340</td></tr></table>

6. The Linear Finite-Difference Algorithm with the extrapolation in Example 2 gives:

(a)

<table><tr><td>Xi</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td><td>Wi(h = 0.025)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>0.2</td><td>1.01809654</td><td>1.02113909</td><td>1.02189067</td><td>1.02215327</td><td>1.02214120</td><td>1.02214039</td></tr><tr><td>0.4</td><td>0.64736665</td><td>0.65004438</td><td>0.65070691</td><td>0.65093696</td><td>0.65092775</td><td>0.65092714</td></tr><tr><td>0.6</td><td>0.60014996</td><td>0.60175137</td><td>0.60214815</td><td>0.60228517</td><td>0.60228041</td><td>0.60228009</td></tr><tr><td>0.8</td><td>0.73896130</td><td>0.73961176</td><td>0.73977312</td><td>0.73982858</td><td>0.73982691</td><td>0.73982680</td></tr></table>

(b)

<table><tr><td>xi</td><td>Wi(h = 0.05)</td><td>Wi(h = 0.025)</td><td>Wi(h = 0.0125)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>1.2</td><td>0.07795820</td><td>0.07769625</td><td>0.07763091</td><td>0.07760893</td><td>0.07760913</td><td>0.07760914</td></tr><tr><td>1.4</td><td>0.36654278</td><td>0.36632776</td><td>0.36627411</td><td>0.36625609</td><td>0.36625623</td><td>0.36625624</td></tr><tr><td>1.6</td><td>0.52914512</td><td>0.52901406</td><td>0.52898134</td><td>0.52897037</td><td>0.52897043</td><td>0.52897044</td></tr><tr><td>1.8</td><td>0.62871452</td><td>0.62865682</td><td>0.62864241</td><td>0.62863759</td><td>0.62863761</td><td>0.62863761</td></tr></table>

7. (a) The approximate deflections are shown in the following table.

<table><tr><td>i</td><td>Xi</td><td>W1i</td></tr><tr><td>5</td><td>30</td><td>0.0102808</td></tr><tr><td>10</td><td>60</td><td>0.0144277</td></tr><tr><td>15</td><td>90</td><td>0.0102808</td></tr></table>

(b) Yes, the maximum error on the interval is within 0.2 in.   
(c) Yes, the maximum deflection occurs at $x = 6 0$ . The exact solution is within tolerance, but the approximation is not.

8. The approximate deflection at 1-in. intervals is give in the following table.

<table><tr><td>i Wi</td><td></td></tr><tr><td>Xi</td><td></td></tr><tr><td>10 20</td><td>10.0 0.1098549 20.0 0.1761424</td></tr><tr><td>25</td><td>25.0 0.1849608</td></tr><tr><td>30</td><td>30.0 0.1761424</td></tr><tr><td>40</td><td>40.0 0.1098549</td></tr></table>

$^ { * } 9$ . First we have

$$
\left| { \frac { h } { 2 } } p ( x _ { i } ) \right| \leq { \frac { h L } { 2 } } < 1 ,
$$

so

$$
\Bigg | - 1 - \frac { h } { 2 } p ( x _ { i } ) \Bigg | = 1 + \frac { h } { 2 } p ( x _ { i } ) \quad \mathrm { a n d } \quad \Bigg | - 1 + \frac { h } { 2 } p ( x _ { i } ) \Bigg | = 1 - \frac { h } { 2 } p ( x _ { i } ) .
$$

Therefore,

$$
\left| - 1 - { \frac { h } { 2 } } p ( x _ { i } ) \right| + \left| - 1 + { \frac { h } { 2 } } p ( x _ { i } ) \right| = 2 \leq 2 + h ^ { 2 } q ( x _ { i } ) ,
$$

for $2 \leq i \leq N - 1$ .

Since

$$
\left| - 1 + \frac { h } { 2 } p ( x _ { 1 } ) \right| < 2 \leq 2 + h ^ { 2 } q ( x _ { 1 } ) \quad \mathrm { ~ a n d ~ } \ \left| - 1 - \frac { h } { 2 } p ( x _ { N } ) \right| < 2 \leq 2 + h ^ { 2 } q ( x _ { N } ) ,
$$

Theorem 6.31 implies that the linear system (11.19) has a unique solution.

$^ { * } 1 0$ . Let $q ( x ) \geq w > 0$ on $[ a , b ]$ . Then using the sixth Taylor polynomial gives

$$
{ \frac { y ( x _ { i + 1 } ) - y ( x _ { i - 1 } ) } { 2 h } } = y ^ { \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 6 } } y ^ { \prime \prime \prime } ( x _ { i } ) + { \frac { h ^ { 4 } } { 1 2 0 } } y ^ { ( 5 ) } ( x _ { i } ) + O \left( h ^ { 5 } \right)
$$

and

$$
{ \frac { y ( x _ { i + 1 } ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) } { h ^ { 2 } } } = y ^ { \prime \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 1 2 } } y ^ { ( 4 ) } ( x _ { i } ) + O \left( h ^ { 4 } \right) .
$$

Thus

$$
\big ( 2 + h ^ { 2 } q ( x _ { i } ) \big ) y ( x _ { i } ) - \bigg ( 1 - \frac { h } { 2 } p ( x _ { i } ) \bigg ) y ( x _ { i + 1 } ) - \bigg ( 1 + \frac { h } { 2 } p ( x _ { i } ) \bigg ) y ( x _ { i - 1 } ) + h ^ { 2 } r ( x _ { i } )
$$

$$
= p ( x _ { i } ) \frac { h ^ { 4 } } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { h ^ { 4 } } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) + ] O \left( h ^ { 6 } \right) .
$$

Subtracting $h ^ { 2 }$ times Equation (11.18) gives

$$
\begin{array} { l } { { \displaystyle \left( 2 + h ^ { 2 } q ( x _ { i } ) \right) ( y ( x _ { i } ) - w _ { i } ) = \left( 1 - \frac { h } { 2 } p ( x _ { i } ) \right) ( y ( x _ { i + 1 } ) - w _ { i + 1 } ) } } \\ { { \displaystyle \qquad + \left( 1 + \frac { h } { 2 } p ( x _ { i } ) \right) ( y ( x _ { i - 1 } ) - w _ { i - 1 } ) } } \\ { { \displaystyle \qquad + \left[ \frac { p ( x _ { i } ) } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { 1 } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) \right] h ^ { 4 } + { \cal O } \left( h ^ { 6 } \right) . } } \end{array}
$$

Let $E = \textstyle \operatorname* { m a x } _ { 0 \leq i \leq N + 1 } | y ( x _ { i } ) - w _ { i } |$ . Then since $\begin{array} { r } { \Big | \frac { h } { 2 } p ( x _ { i } ) \Big | < 1 } \end{array}$

$$
\left( 2 + h ^ { 2 } q ( x _ { i } ) \right) \left( y ( x _ { i } ) - w _ { i } \right) \leq 2 E + h ^ { 4 } \biggl | \frac { p ( x _ { i } ) } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { 1 } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) \biggr | + O \left( h ^ { 6 } \right) .
$$

Let $K _ { 1 } = \operatorname* { m a x } _ { a \leq x \leq b } | y ^ { \prime \prime \prime } ( x ) |$ and $K _ { 2 } = \mathrm { m a x } _ { a \leq x \leq b } \left| y ^ { ( 4 ) } ( x ) \right| .$ If $q ( x _ { i } ) \geq w$ , then

$$
\left( 2 + h ^ { 2 } w \right) E \leq 2 E + h ^ { 4 } \biggl [ \frac { L K _ { 1 } } { 6 } + \frac { K _ { 2 } } { 1 2 } \biggr ] + O \left( h ^ { 6 } \right)
$$

and

$$
E \leq h ^ { 2 } \left[ \frac { 2 L K _ { 1 } + K _ { 2 } } { 1 2 w } \right] + O \left( h ^ { 4 } \right) .
$$

# Exercise Set 11.4, page 696

$^ { * } 1$ . The Nonlinear Finite-Difference method gives the following results.

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>1.5</td><td>0.4067967</td><td>0.4054651</td></tr></table>

2. The Nonlinear Finite-Difference method gives the following results.   

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>-0.75</td><td>0.44458639</td><td>0.44444444</td></tr><tr><td>2</td><td>-0.5</td><td>0.40015723</td><td>0.4</td></tr><tr><td>3</td><td>-0.25</td><td>0.36373152</td><td>0.36363636</td></tr></table>

3. The Nonlinear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>1.20000000</td><td>0.18220299</td><td>0.18232156</td></tr><tr><td>4</td><td>1.40000000</td><td>0.33632929</td><td>0.33647224</td></tr><tr><td>6</td><td>1.60000000</td><td>0.46988413</td><td>0.47000363</td></tr><tr><td>8</td><td>1.80000000</td><td>0.58771808</td><td>0.58778666</td></tr></table>

Convergence in 3 iterations.

(b)

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>0.31415927</td><td>1.36244080</td><td>1.36208552</td></tr><tr><td>4</td><td>0.62831853</td><td>1.80138559</td><td>1.79999746</td></tr><tr><td>6</td><td>0.94247780</td><td>2.24819259</td><td>2.24569937</td></tr><tr><td>8</td><td>1.25663706</td><td>2.59083695</td><td>2.58844295</td></tr></table>

Convergence in 3 iterations.

(c)

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>0.83775804</td><td>0.86205907</td><td>0.86205848</td></tr><tr><td>2</td><td>0.89011792</td><td>0.88155964</td><td>0.88155882</td></tr><tr><td>3</td><td>0.94247780</td><td>0.89945447</td><td>0.89945372</td></tr><tr><td>4</td><td>0.99483767</td><td>0.91579005</td><td>0.91578959</td></tr></table>

Convergence in 2 iterations.

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y（xi)</td></tr><tr><td>4</td><td>0.62831853</td><td>2.28968807</td><td>2.58778525</td></tr><tr><td>8</td><td>1.25663706</td><td>2.41412603</td><td>2.95105652</td></tr><tr><td>12</td><td>1.88495559</td><td>2.41412603</td><td>2.95105652</td></tr><tr><td>16</td><td>2.51327412</td><td>2.28968807</td><td>2.58778525</td></tr></table>

Convergence in 4 iterations.

4. The Nonlinear Finite-Difference Algorithm gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.4347972</td><td>0.4347826</td></tr><tr><td>6</td><td>1.6</td><td>0.3846286</td><td>0.3846154</td></tr><tr><td>9</td><td>1.9</td><td>0.3448316</td><td>0.3448276</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>2.0694081</td><td>2.0692308</td></tr><tr><td>6</td><td>1.6</td><td>2.2250937</td><td>2.2250000</td></tr><tr><td>9</td><td>1.9</td><td>2.4263387</td><td>2.4263158</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>2.3</td><td>1.2677078</td><td>1.2676917</td></tr><tr><td>6</td><td>2.6</td><td>1.3401418</td><td>1.3401268</td></tr><tr><td>9</td><td>2.9</td><td>1.4095432</td><td>1.4095383</td></tr><tr><td>5</td><td>1.25</td><td>0.4345979</td><td>0.4358273</td></tr><tr><td>10</td><td>1.50</td><td>1.3662119</td><td>1.3684447</td></tr><tr><td>15</td><td>1.75</td><td>2.9969339</td><td>2.9991909</td></tr></table>

5. (b) For ( $^ *$ 4a) the complete results are:

For (4c) we have:   

<table><tr><td>Xi</td><td>Wi(h = 0.2)</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td></tr><tr><td>1.00</td><td>0.5000000000</td><td>0.5000000000</td><td>0.5000000000</td></tr><tr><td>1.05</td><td></td><td></td><td>0.4878058215</td></tr><tr><td>1.10</td><td></td><td>0.4761972439</td><td>0.4761921720</td></tr><tr><td>1.15</td><td></td><td></td><td>0.4651185619</td></tr><tr><td>1.20</td><td>0.4545886201</td><td>0.4545563382</td><td>0.4545481813</td></tr><tr><td>1.25</td><td></td><td></td><td>0.4444474908</td></tr><tr><td>1.30</td><td></td><td>0.4347956122</td><td>0.4347858663</td></tr><tr><td>1.35</td><td></td><td></td><td>0.4255352892</td></tr><tr><td>1.40</td><td>0.4167206681</td><td>0.4166802725</td><td>0.4166700749</td></tr><tr><td>1.45</td><td></td><td></td><td>0.4081666349</td></tr><tr><td>1.50</td><td></td><td>0.4000130439</td><td>0.4000032672</td></tr><tr><td>1.55</td><td></td><td></td><td>0.3921599714</td></tr><tr><td>1.60</td><td>0.3846613728</td><td>0.3846269650</td><td>0.3846182851</td></tr><tr><td>1.65</td><td></td><td></td><td>0.3773611389</td></tr><tr><td>1.70</td><td></td><td>0.3703797826</td><td>0.3703727277</td></tr><tr><td>1.75</td><td></td><td></td><td>0.3636383953</td></tr><tr><td>1.80</td><td>0.3571694307</td><td>0.3571495457</td><td>0.3571445322</td></tr><tr><td>1.85</td><td></td><td></td><td>0.3508784839</td></tr><tr><td>1.90</td><td></td><td>0.3448311085</td><td>0.3448284683</td></tr><tr><td>1.95</td><td></td><td></td><td>0.3389835019</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>2.00</td><td>0.3333333333</td><td>0.3333333333</td><td>0.3333333333</td></tr></table>

<table><tr><td>Xi</td><td>Wi(h = 0.2)</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td><td>EXT1,i</td><td>EXT2,i</td><td>EXT3,i</td></tr><tr><td>1.2</td><td>2.0340273</td><td>2.0335158</td><td>2.0333796</td><td>2.0333453</td><td>2.0333342</td><td>2.0333334</td></tr><tr><td>1.4</td><td>2.1148732</td><td>2.1144386</td><td>2.1143243</td><td>2.1142937</td><td>2.1142863</td><td>2.1142858</td></tr><tr><td>1.6</td><td>2.2253630</td><td>2.2250937</td><td>2.2250236</td><td>2.2250039</td><td>2.2250003</td><td>2.2250000</td></tr><tr><td>1.8</td><td>2.3557284</td><td>2.3556001</td><td>2.3555668</td><td>2.3555573</td><td>2.3555556</td><td>2.3355556</td></tr></table>

6. The approximate deflections using the Nonlinear Finite Difference Algorithm are shown in the following table.

<table><tr><td>i</td><td>Xi</td></tr><tr><td>5</td><td>30 0.01028080</td></tr><tr><td>10</td><td>60 0.01442767</td></tr><tr><td>15</td><td>90 0.01028080</td></tr></table>

The results from Exercise 7 in Section 11.3 are:

<table><tr><td>i</td><td>Ci W1i</td></tr><tr><td>5 30</td><td>0.0102808</td></tr><tr><td>10</td><td>60 0.0144277</td></tr><tr><td>15</td><td>90 0.0102808</td></tr></table>

Since the results are the same we can conclude that adding the nonlinear term to the differential equation makes no difference.

$^ { * } 7$ . The Jacobian matrix $J = \left( a _ { i , j } \right)$ is tridiagonal with entries given in (11.21). So

$$
\begin{array} { r l } & { \quad \alpha _ { 1 , 1 } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { 1 1 } , w _ { 1 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) , } \\ & { \quad \alpha _ { 1 , 2 } = - 1 + \frac { b } { 2 } f _ { 9 } \left( x _ { 1 1 } , w _ { 1 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) , } \\ & { \quad \alpha _ { i , i - 1 } = - 1 - \frac { b } { 2 } f _ { 9 } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { i , i } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { i } , w _ { i + 1 } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { i , i + 1 } = - 1 + \frac { b } { 2 } f _ { 9 } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { N , N - 1 } = - 1 - \frac { b } { 2 } f _ { 9 } \left( x _ { N } , w _ { N } , \frac { 1 } { 2 h } ( \delta - w _ { N - 1 } ) \right) , } \\ & { \quad \alpha _ { N , N - 1 } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { N } , w _ { N } , \frac { 1 } { 2 h } ( \delta - w _ { N - 1 } ) \right) . } \end{array}
$$

Thus, $| a _ { i , i } | \geq 2 + h ^ { 2 } \delta$ , for $i = 1 , \ldots , N$ . Since $| f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) | \leq L$ and $h < 2 / L$ ,

$$
\left| \frac { h } { 2 } f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) \right| \leq \frac { h L } { 2 } < 1 .
$$

So

$$
\begin{array} { r l } & { \quad | a _ { 1 , 2 } | = \displaystyle { \bigg | - 1 + \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { 1 } , w _ { 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) \bigg | < 2 < | a _ { 1 , 1 } | } , } \\ & { \quad | a _ { i , i - 1 } | + | a _ { i , i + 1 } | = - a _ { i , i - 1 } - a _ { i , i + 1 } } \\ & { \qquad = 1 + \displaystyle { \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) + 1 - \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) } } \\ & { \qquad = 2 \le | a _ { i , i } | , } \end{array}
$$

and

$$
\left| a _ { N , N - 1 } \right| = - \ a _ { N , N - 1 } = 1 + { \frac { h } { 2 } } f _ { y ^ { \prime } } \left( x _ { N } , w _ { N } , { \frac { 1 } { 2 h } } ( \beta - w _ { N - 1 } ) \right) < 2 < | a _ { N , N } | .
$$

By Theorem 6.31, the matrix $J$ is nonsingular.

# Exercise Set 11.5, page 710

\*1. The Piecewise Linear Algorithm gives

$$
\phi ( x ) = - 0 . 0 7 7 1 3 2 7 4 \phi _ { 1 } ( x ) - 0 . 0 7 4 4 2 6 7 8 \phi _ { 2 } ( x ) .
$$

The actual values are

$$
y ( x _ { 1 } ) = - 0 . 0 7 9 8 8 5 4 5 \quad \mathrm { a n d } \quad y ( x _ { 2 } ) = - 0 . 0 7 7 1 2 9 0 3 .
$$

2. The Piecewise Linear Algorithm gives

$$
\phi ( x ) = - 0 . 2 5 5 2 6 2 9 \phi _ { 1 } ( x ) - 0 . 1 6 3 3 5 6 5 \phi _ { 2 } ( x ) .
$$

The actual values are

$$
y ( x _ { 1 } ) = - 0 . 2 4 \quad { \mathrm { a n d } } \quad y ( x _ { 2 } ) = - 0 . 1 6 .
$$

3. The Piecewise Linear Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>（xi）</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>-0.212333</td><td>-0.21</td></tr><tr><td>6</td><td>0.6</td><td>-0.241333</td><td>-0.24</td></tr><tr><td>9</td><td>0.9</td><td>-0.090333</td><td>-0.09</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>0.1815138</td><td>0.1814273</td></tr><tr><td>6</td><td>0.6</td><td>0.1805502</td><td>0.1804753</td></tr><tr><td>9</td><td>0.9</td><td>0.05936468</td><td>0.05934303</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>5</td><td>0.25</td><td>-0.3585989</td><td>-0.3585641</td></tr><tr><td>10</td><td>0.50</td><td>-0.5348383</td><td>-0.5347803</td></tr><tr><td>15</td><td>0.75</td><td>-0.4510165</td><td>-0.4509614</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>5</td><td>0.25</td><td>-0.1846134</td><td>-0.1845204</td></tr><tr><td>10</td><td>0.50</td><td>-0.2737099</td><td>-0.2735857</td></tr><tr><td>15</td><td>0.75</td><td>-0.2285169</td><td>-0.2284204</td></tr></table>

4. The Cubic Spline Algorithm gives the results in the following tables. \*(a)

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>-0.0712415</td><td>-0.0712308</td></tr><tr><td>2</td><td>0.5</td><td>-0.0944237</td><td>-0.0944091</td></tr><tr><td>3</td><td>0.75</td><td>-0.0681742</td><td>-0.0681651</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>（xi)</td><td>yi</td></tr><tr><td>1</td><td>0.25</td><td>-0.1875</td><td>-0.1875</td></tr><tr><td>2</td><td>0.5</td><td>-0.25</td><td>-0.25</td></tr><tr><td>3</td><td>0.75</td><td>-0.1875</td><td>-0.1875</td></tr></table>

5. The Cubic Spline Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>-0.2100000</td><td>-0.21</td></tr><tr><td>6</td><td>0.6</td><td>-0.2400000</td><td>-0.24</td></tr><tr><td>9</td><td>0.9</td><td>-0.0900000</td><td>-0.09</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi</td></tr><tr><td>3</td><td>0.3</td><td>0.1814269</td><td>0.1814273</td></tr><tr><td>6</td><td>0.6</td><td>0.1804753</td><td>0.1804754</td></tr><tr><td>9</td><td>0.9</td><td>0.05934321</td><td>0.05934303</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi)</td></tr><tr><td>5</td><td>0.25</td><td>-0.3585639</td><td>-0.3585641</td></tr><tr><td>10</td><td>0.50</td><td>-0.5347779</td><td>-0.5347803</td></tr><tr><td>15</td><td>0.75</td><td>-0.4509109</td><td>-0.4509614</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>（xi） y(xi)</td></tr><tr><td>5</td><td>0.25</td><td>-0.1845191 -0.1845204</td></tr><tr><td>10</td><td>0.50</td><td>-0.2735833 -0.2735857</td></tr><tr><td>15</td><td>0.75</td><td>-0.2284186 -0.2284204</td></tr></table>

$^ { * } 6$ . With $z ( x ) = y ( x ) - \beta x - \alpha ( 1 - x )$ , we have

$$
z ( 0 ) = y ( 0 ) - \alpha = \alpha - \alpha = 0 \quad { \mathrm { a n d } } \quad z ( 1 ) = y ( 1 ) - \beta = \beta - \beta = 0 .
$$

Further, $z ^ { \prime } ( x ) = y ^ { \prime } ( x ) - \beta + \alpha$ . Thus

$$
y ( x ) = z ( x ) + \beta x + \alpha ( 1 - x ) \quad { \mathrm { a n d } } \quad y ^ { \prime } ( x ) = z ^ { \prime } ( x ) + \beta - \alpha .
$$

Substituting for $y$ and $y ^ { \prime }$ in the differential equation gives

$$
- \frac { d } { d x } ( p ( x ) z ^ { \prime } + p ( x ) ( \beta - \alpha ) ) + q ( x ) ( z + \beta x + \alpha ( 1 - x ) ) = f ( x ) .
$$

Simplifying gives the differential equation

$$
- \frac { d } { d x } ( p ( x ) z ^ { \prime } ) + q ( x ) z = f ( x ) + ( \beta - \alpha ) p ^ { \prime } ( x ) - [ \beta x + \alpha ( 1 - x ) ] q ( x ) .
$$

7. Exercise 6 and the Piecewise Linear Algorithm give:

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>y（(xi）</td></tr><tr><td>3</td><td>0.3</td><td>1.0408182</td><td>1.0408182</td></tr><tr><td>6</td><td>0.6</td><td>1.1065307</td><td>1.1065306</td></tr><tr><td>9</td><td>0.9</td><td>1.3065697</td><td>1.3065697</td></tr></table>

8. The Cubic Spline Algorithm gives the results in the following table.

<table><tr><td>i(x) Xi</td><td></td><td>y(xi)</td></tr><tr><td>0.3</td><td>1.0408183</td><td>1.0408182</td></tr><tr><td>0.5</td><td>1.1065307</td><td>1.1065301</td></tr><tr><td>0.9</td><td>1.3065697</td><td>1.3065697</td></tr></table>

$^ { * } 9$ . A change in variable $w = ( x - a ) / ( b - a )$ gives the boundary value problem

$$
- \frac { d } { d w } ( p ( ( b - a ) w + a ) y ^ { \prime } ) + ( b - a ) ^ { 2 } q ( ( b - a ) w + a ) y = ( b - a ) ^ { 2 } f ( ( b - a ) w + a ) ,
$$

where $0 < w < 1$ , $y ( 0 ) = \alpha$ , and $y ( 1 ) = \beta$ . Then Exercise 6 can be used.

\*10. If $\sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) = 0$ , for $0 \leq x \leq 1$ , then for any $j$ , we have $\sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x _ { j } ) = 0 ,$

But

$$
\phi _ { i } ( x _ { j } ) = { \left\{ \begin{array} { l l } { 0 } & { i \neq j , } \\ { 1 } & { i = j , } \end{array} \right. }
$$

so $c _ { j } \phi _ { j } ( x _ { j } ) = c _ { j } = 0$ . Hence the functions are linearly independent.

11. Suppose $\begin{array} { r } { \phi ( x ) = \sum _ { i = 0 } ^ { n + 1 } c _ { i } \phi _ { i } ( x ) = 0 } \end{array}$ , for all $x$ in $\lfloor 0 , 1 \rfloor$ . At the nodes $x _ { i } , i = 0 , \ldots , n + 1$ , we have

$$
\begin{array} { r l } & { \phi _ { 0 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } i = 1 } \\ { 1 / 4 , } & { \mathrm { i f ~ } i = 2 } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } i = n } \\ { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n + 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n + 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { i f ~ } i = n } \end{array} \right. } \end{array}
$$

and for $j = \mathopen { } \mathclose \bgroup  , \aftergroup \egroup 3 , \ldots , n - 1$ ,

$$
\phi _ { j } ( x _ { i } ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } i = j } \\ { 1 / 4 , } & { { \mathrm { i f ~ } } i = j - 1 { \mathrm { ~ o r ~ } } i = j + 1 } \\ { 0 , } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Thus

$$
\begin{array} { l } { \displaystyle 0 = \phi ( { x } _ { 1 } ) = \frac { 1 } { 4 } c _ { 0 } + c _ { 1 } + \frac { 1 } { 4 } c _ { 2 } } \\ { \displaystyle 0 = \phi ( { x } _ { 2 } ) = \frac { 1 } { 4 } c _ { 1 } + c _ { 2 } + \frac { 1 } { 4 } c _ { 3 } } \\ { \displaystyle \phantom { \frac { 1 } { 4 } c _ { 0 } + \phi ( { x } _ { 1 } ) } \vdots \qquad } \\ { \displaystyle 0 = \phi ( { x } _ { n - 1 } ) = \frac { 1 } { 4 } c _ { n - 2 } + c _ { n - 1 } + \frac { 1 } { 4 } c _ { n } } \\ { \displaystyle 0 = \phi ( { x } _ { n } ) = \frac { 1 } { 4 } c _ { n - 1 } + c _ { n } + \frac { 1 } { 4 } c _ { n + 1 } . } \end{array}
$$

Since $\phi ^ { \prime } ( 0 ) = \phi ^ { \prime } ( 1 ) = 0$ , we have

$$
0 = \frac { 3 } { h } c _ { 0 } + \frac { 1 . 5 } { h } c _ { 1 } , \quad \mathrm { s o } \quad 0 = 3 c _ { 0 } + 1 . 5 c _ { 1 }
$$

and

$$
0 = - \frac { 1 . 5 } { h } c _ { n } - \frac { 3 } { h } c _ { n + 1 } , \quad \mathrm { s o } \quad 0 = 1 . 5 c _ { n } + 3 c _ { n + 1 } .
$$

Thus,

$$
\left[ \begin{array} { c c c c c c c c c c c } { 3 } & { 1 . 5 } & { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { \ddots } & & & & & { \vdots } \\ { 0 } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { \ddots } & & & & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & & & { \vdots } \\ { \vdots } & & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { 0 } \\ { \vdots } & & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } \\ { \vdots } & & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } \\ { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } & { 1 . 5 } & { 3 } \end{array} \right] \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { c _ { n - 1 } } \\ { c _ { n + 1 } } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] ,
$$

which can be written as the linear system $A \mathbf { c } \ = \ \mathbf { 0 }$ . The matrix $A$ is strictly diagonally dominant and, hence, nonsingular. So the only solution to the linear system is $\mathbf c = \mathbf 0$ , and $\left\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } , \phi _ { n + 1 } \right\}$ is linearly independent.

$^ { \ast } 1 2$ . Let $\mathbf { c } = ( c _ { 1 } , \ldots , c _ { n } ) ^ { t }$ be any vector and let $\begin{array} { r } { \phi ( x ) = \sum _ { j = 1 } ^ { n } c _ { j } \phi _ { j } ( x ) } \end{array}$ . Then

$$
\begin{array} { l } { { \displaystyle c ^ { t } A \mathbf { c } = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } a _ { i j } c _ { i } c _ { j } = \sum _ { i = 1 } ^ { n } \sum _ { j = i - 1 } ^ { i + 1 } a _ { i j } c _ { i } c _ { i } } } \\ { { \displaystyle \ - \sum _ { i = 1 } ^ { n } \left[ \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } \phi _ { i } ^ { \prime } ( x ) c _ { i - 1 } \phi _ { i - 1 } ^ { \prime } ( x ) + q ( x ) c _ { i } \phi _ { i } ( x ) c _ { i - 1 } \phi _ { i - 1 } ( x ) \right\} d x \right. } } \\ { { \displaystyle \left. \ + \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } ^ { 2 } [ \phi _ { i } ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) c _ { i } ^ { 2 } [ \phi _ { i } ^ { \prime } ( x ) ] ^ { 2 } \right\} d x } \ ~ } \\ { { \displaystyle \ + \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } \phi _ { i } ^ { \prime } ( x ) c _ { i + 1 } \phi _ { i + 1 } ^ { \prime } ( x ) + q ( x ) c _ { i } \phi _ { i } ( x ) c _ { i + 1 } \phi _ { i + 1 } ( x ) \right\} d x \right] } } \\ { { \displaystyle \ - \int _ { 0 } ^ { 1 } \left\{ p ( x ) [ \phi ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ \phi ( x ) ] ^ { 2 } \right\} d x } . } \end{array}
$$

So $\mathbf { c } ^ { t } A \mathbf { c } \geq 0$ with equality only if $\mathbf c = \mathbf 0$ . Since $A$ is also symmetric, $A$ is positive definite.

$^ \mathrm { * _ { 1 3 } }$ . For $\mathbf { c } = ( c _ { 0 } , c _ { 1 } , \hdots , c _ { n + 1 } ) ^ { t }$ and $\begin{array} { r } { \phi ( x ) = \sum _ { i = 0 } ^ { n + 1 } c _ { i } \phi _ { i } ( x ) } \end{array}$ , we have

$$
\mathbf { c } ^ { t } A \mathbf { c } = \int _ { 0 } ^ { 1 } p ( x ) [ \phi ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ \phi ( x ) ] ^ { 2 } d x .
$$

But $p ( x ) > 0$ and $q ( x ) [ \phi ( x ) ] ^ { 2 } \geq 0$ , so $\mathbf { c } ^ { t } A \mathbf { c } \geq 0$ , and it can be $0$ , for $\mathbf x \neq 0$ , only if $\phi ^ { \prime } ( x ) \equiv 0$ on $[ 0 , 1 ]$ . However, $\{ \phi _ { 0 } ^ { \prime } , \phi _ { 1 } ^ { \prime } , . . . , \phi _ { n + 1 } ^ { \prime } \}$ is linearly independent, so $\phi ^ { \prime } ( x ) \neq 0$ on $[ 0 , 1 ]$ and $\mathbf { c } ^ { t } A \mathbf { c } = 0$ if and only if $\mathbf c = \mathbf 0$ .

# Numerical Solutions to Partial Differential Equations

Exercise Set 12.1, page 723

$^ { * } 1$ . The Poisson Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.5</td><td>0.0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>1.0</td><td>0.25</td><td>0.25</td></tr><tr><td>1</td><td>3</td><td>0.5</td><td>1.5</td><td>1.0</td><td>1</td></tr></table>

2. The Poisson Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td><td>u(xi,yi)</td></tr><tr><td>1</td><td>1</td><td>1.33333333</td><td>0.33333333</td><td>0.6348043</td><td>0.6359888</td></tr><tr><td>1</td><td>2</td><td>1.33333333</td><td>0.66666667</td><td>0.7985001</td><td>0.7985077</td></tr><tr><td>2</td><td>1</td><td>1.66666667</td><td>0.33333333</td><td>1.0599924</td><td>1.0687200</td></tr><tr><td>2</td><td>2</td><td>1.66666667</td><td>0.66666667</td><td>1.1698208</td><td>1.1700713</td></tr></table>

3. The Poisson Equation Finite-Difference Algorithm gives the following results.

(a) 30 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.4</td><td>0.1599988</td><td>0.16</td></tr><tr><td>2</td><td>4</td><td>0.4</td><td>0.8</td><td>0.3199988</td><td>0.32</td></tr><tr><td>4</td><td>2</td><td>0.8</td><td>0.4</td><td>0.3199995</td><td>0.32</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.8</td><td>0.6399996</td><td>0.64</td></tr></table>

(b) 29 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>1</td><td>1.256637</td><td>0.3141593</td><td>0.2951855</td><td>0.2938926</td></tr><tr><td>2</td><td>3</td><td>1.256637</td><td>0.9424778</td><td>0.1830822</td><td>0.1816356</td></tr><tr><td>4</td><td>1</td><td>2.513274</td><td>0.3141593</td><td>-0.7721948</td><td>-0.7694209</td></tr><tr><td>4</td><td>3</td><td>2.513274</td><td>0.9424778</td><td>-0.4785169</td><td>-0.4755283</td></tr></table>

(c) 126 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>4</td><td>3</td><td>0.8</td><td>0.3</td><td>1.2714468</td><td>1.2712492</td></tr><tr><td>4</td><td>7</td><td>0.8</td><td>0.7</td><td>1.7509414</td><td>1.7506725</td></tr><tr><td>8</td><td>3</td><td>1.6</td><td>0.3</td><td>1.6167917</td><td>1.6160744</td></tr><tr><td>8</td><td>7</td><td>1.6</td><td>0.7</td><td>3.0659184</td><td>3.0648542</td></tr></table>

(d) 127 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>2</td><td>1.2</td><td>1.2</td><td>0.5251533</td><td>0.5250861</td></tr><tr><td>4</td><td>4</td><td>1.4</td><td>1.4</td><td>1.3190830</td><td>1.3189712</td></tr><tr><td>6</td><td>6</td><td>1.6</td><td>1.6</td><td>2.4065150</td><td>2.4064186</td></tr><tr><td>8</td><td>8</td><td>1.8</td><td>1.8</td><td>3.8088995</td><td>3.8088576</td></tr></table>

4. The Poisson Equation Finite-Difference Algorithm with extrapolation gives the following results.   

<table><tr><td>xi</td><td>yj</td><td>Wij(h = 0.2)</td><td>Wij(h = 0.1)</td><td>Wij(h = 0.05)</td><td>Ext1i,j</td><td>Ext2i,j</td><td>Ext3i,j</td></tr><tr><td>0.4</td><td>0.4</td><td>0.15999914</td><td>0.15999579</td><td>0.15998414</td><td>0.159994673</td><td>0.15998026</td><td>0.15997930</td></tr><tr><td>0.4</td><td>0.8</td><td>0.31999888</td><td>0.31999384</td><td>0.31997558</td><td>0.319992160</td><td>0.31996949</td><td>0.31996798</td></tr><tr><td>0.8</td><td>0.4</td><td>0.31999952</td><td>0.31999588</td><td>0.31997997</td><td>0.319994667</td><td>0.31997467</td><td>0.31997333</td></tr><tr><td>0.8</td><td>0.8</td><td>0.63999955</td><td>0.63999689</td><td>0.63998633</td><td>0.639996003</td><td>0.63998281</td><td>0.63998193</td></tr></table>

\*5. To incorporate the SOR method, make the following changes to Algorithm 12.1:

$$
\begin{array} { r l r } { S T E P \ 1 } & { \mathrm { S e t ~ } h = ( b - a ) / n ; } \\ & { } & { k = ( d - c ) / m ; } \\ & { } & { \omega = 4 / \left( 2 + \sqrt { 4 - ( \cos \pi / m ) ^ { 2 } - ( \cos \pi / n ) ^ { 2 } } \right) ; } \\ & { } & { \omega _ { 0 } = 1 - w ; } \end{array}
$$

In each of Steps 7, 8, 9, 11, 12, 13, 14, 15, and 16 after

insert

$$
\begin{array} { r l } & { \mathrm { s e t } ~ E = w _ { \alpha , \beta } - z ; } \\ & { ~ \mathrm { i f } ~ ( | E | > \mathrm { N O R M } ) \mathrm { ~ t h e n ~ s e t ~ N O R M } = | E | ; } \\ & { \mathrm { s e t } ~ w _ { \alpha , \beta } = \omega _ { 0 } E + z . } \end{array}
$$

where $\alpha$ and $\beta$ depend on which step is being changed.

6. Using $T O L = 1 0 ^ { - 6 }$ , the results are the same for both methods. The number of iterations required are listed for each method.

(a) SOR 14 iterations, Gauss–Seidel 30 iterations, $\omega = 1 . 2 5 9 6 1 6$   

<table><tr><td colspan="6"></td></tr><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>1</td><td>1</td><td>0.2</td><td>0.2</td><td>0.03999975</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.4</td><td>0.15999994</td></tr><tr><td>3</td><td>3</td><td>0.6</td><td>0.6</td><td>0.35999994</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.8</td><td>0.63999998</td></tr></table>

(b) SOR 14 iterations, Gauss–Seidel 29 iterations, $\omega = 1 . 2 5 9 6 1 6$   

<table><tr><td>i</td><td>j</td><td>Ci</td><td>yj</td><td>Wij</td></tr><tr><td>2</td><td>1</td><td>1.256637</td><td>0.3141593</td><td>0.29518499</td></tr><tr><td>2</td><td>3</td><td>1.256637</td><td>0.9424778</td><td>0.18308118</td></tr><tr><td>4</td><td>1</td><td>2.513274</td><td>0.3141593</td><td>-0.77219505</td></tr><tr><td>4</td><td>3</td><td>2.513274</td><td>0.9424778</td><td>-0.47851735</td></tr></table>

(c) SOR 30 iterations, Gauss–Seidel 126 iterations, $\omega = 1 . 5 2 7 8 6 4$   

<table><tr><td></td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>1</td><td>1</td><td>0.2</td><td>0.1</td><td>1.0202140</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.2</td><td>1.0833400</td></tr><tr><td>3</td><td>3</td><td>0.6</td><td>0.3</td><td>1.1973456</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.4</td><td>1.3773776</td></tr><tr><td>5</td><td>5</td><td>1.0</td><td>0.5</td><td>1.6491565</td></tr><tr><td>6</td><td>6</td><td>1.2</td><td>0.6</td><td>2.0550775</td></tr><tr><td>7</td><td>7</td><td>1.4</td><td>0.7</td><td>2.6653128</td></tr><tr><td>8</td><td>8</td><td>1.6</td><td>0.8</td><td>3.5975766</td></tr><tr><td>9</td><td>9</td><td>1.8</td><td>0.9</td><td>5.0537432</td></tr></table>

(d) SOR 30 iterations, Gauss–Seidel 127 iterations, $\omega = 1 . 5 2 7 8 6 4$   

<table><tr><td></td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>2</td><td>2</td><td>1.2</td><td>1.2</td><td>0.52515626</td></tr><tr><td>4</td><td>4</td><td>1.4</td><td>1.4</td><td>1.3190907</td></tr><tr><td>6</td><td>6</td><td>1.6</td><td>1.6</td><td>2.4065227</td></tr><tr><td>8</td><td>8</td><td>1.8</td><td>1.8</td><td>3.8089025</td></tr></table>

7. The approximate potential at some typical points gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td></tr><tr><td>1</td><td>4</td><td>0.1</td><td>0.4</td><td>88</td></tr><tr><td>2</td><td>1</td><td>0.2</td><td>0.1</td><td>66</td></tr><tr><td>4</td><td></td><td>0.4</td><td>0.2</td><td>66</td></tr></table>

8. Approximations for the temperature are given in the following table. Convergence was obtained with 293 iterations using the tolerance $1 0 ^ { - 6 }$ .

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>5</td><td>9</td><td>2.0</td><td>3.0</td><td>5.959624</td></tr><tr><td>8</td><td>3</td><td>3.2</td><td>1.0</td><td>7.916551</td></tr><tr><td>10</td><td>9</td><td>4.0</td><td>3.0</td><td>4.679948</td></tr><tr><td>12</td><td>12</td><td>4.8</td><td>4.0</td><td>2.060342</td></tr></table>

# Exercise Set 12.2, page 736

1. The Heat Equation Backward-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi，tj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.05</td><td>0.632952</td><td>0.652037</td></tr><tr><td>2</td><td>1</td><td>1.0</td><td>0.05</td><td>0.895129</td><td>0.883937</td></tr><tr><td>3</td><td>1</td><td>1.5</td><td>0.05</td><td>0.632952</td><td>0.625037</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>0.1</td><td>0.566574</td><td>0.552493</td></tr><tr><td>2</td><td>2</td><td>1.0</td><td>0.1</td><td>0.801256</td><td>0.781344</td></tr><tr><td>3</td><td>2</td><td>1.5</td><td>0.1</td><td>0.566574</td><td>0.552493</td></tr></table>

\*2. The Heat Equation Backward-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>1/3</td><td>0.05</td><td>1.59728</td><td>1.53102</td></tr><tr><td>2</td><td>1</td><td>2/3</td><td>0.05</td><td>-1.59728</td><td>-1.53102</td></tr><tr><td>1</td><td>2</td><td>1/3</td><td>0.1</td><td>1.47300</td><td>1.35333</td></tr><tr><td>2</td><td>2</td><td>2/3</td><td>0.1</td><td>-1.47300</td><td>-1.35333</td></tr></table>

3. The Crank-Nicolson Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.05</td><td>0.628848</td><td>0.652037</td></tr><tr><td>2</td><td>1</td><td>1.0</td><td>0.05</td><td>0.889326</td><td>0.883937</td></tr><tr><td>3</td><td>1</td><td>1.5</td><td>0.05</td><td>0.628848</td><td>0.625037</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>0.1</td><td>0.559251</td><td>0.552493</td></tr><tr><td>2</td><td>2</td><td>1.0</td><td>0.1</td><td>0.790901</td><td>0.781344</td></tr><tr><td>3</td><td>2</td><td>1.5</td><td>0.1</td><td>0.559252</td><td>0.552493</td></tr></table>

\*4. The Crank-Nicolson Algorithm gives the following results.

For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>1/3</td><td>0.05</td><td>1.59728</td><td>1.53102</td></tr><tr><td>2</td><td>1</td><td>2/3</td><td>0.05</td><td>-1.59728</td><td>-1.53102</td></tr><tr><td>1</td><td>2</td><td>1/3</td><td>0.1</td><td>1.47300</td><td>1.35333</td></tr><tr><td>2</td><td>2</td><td>2/3</td><td>0.1</td><td>-1.47300</td><td>-1.35333</td></tr></table>

5. The Forward-Difference Algorithm gives the following results.

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>3.035630</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>-3.035630</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>1.876122</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>0</td><td>0</td></tr></table>

(b) For $h = \frac { \pi } { 1 0 }$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>J</td><td>xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4864823</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5728943</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1858197</td><td>0.1874283</td></tr></table>

6. The Forward-Difference Algorithm gives the following results.

(a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi，tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.166149</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.252413</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4681813</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1027637</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5397009</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6344565</td><td>0.6375122</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2061474</td><td>0.2071403</td></tr></table>

7. The Backward-Difference Algorithm gives:

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>-0.00258</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>0.00258</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>-0.00159</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>-4.93 × 10-4</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>4.93 ×10-4</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>-3.05 ×10-4</td><td>0</td></tr></table>

(b) For $\begin{array} { r } { h = \frac { \pi } { 1 0 } } \end{array}$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4986092</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5861503</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1904518</td><td>0.1874283</td></tr></table>

8. (a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.176752</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.259495</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4628134</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1123064</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5482691</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6445290</td><td>0.6375123</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2094202</td><td>0.2071403</td></tr></table>

9. The Crank-Nicolson Algorithm gives the following results.

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>8.2 ×10-7</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>-8.2 × 10-7</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>5.1 ×10-7</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>-2.6 × 10-6</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>2.6×10-6</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>-1.6 × 10-6</td><td>0</td></tr></table>

(b) For $\begin{array} { r } { h = \frac { \pi } { 1 0 } } \end{array}$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4926589</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5791553</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1881790</td><td>0.1874283</td></tr></table>

10. The Crank-Nicolson Algorithm gives the following results.

(a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.171532</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.256005</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4654499</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1076139</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5440532</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6395728</td><td>0.6375122</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2078098</td><td>0.2071403</td></tr></table>

11. Using Richardson’s method gives:

(a) Using $h = 0 . 4$ and $k = 0 . 1$ leads to meaningless results. Using $h = 0 . 4$ and $k = 0 . 0 5$ again gives meaningless answers. Letting $h = 0 . 4$ and $k = 0 . 0 0 5$ produces the following:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>1</td><td>100</td><td>0.4</td><td>0.5</td><td>-165.405</td></tr><tr><td>2</td><td>100</td><td>0.8</td><td>0.5</td><td>267.613</td></tr><tr><td>3</td><td>100</td><td>1.2</td><td>0.5</td><td>-267.613</td></tr><tr><td>4</td><td>100</td><td>1.6</td><td>0.5</td><td>165.405</td></tr></table>

(b)

The instability of Richardson’s method gives very poor results.   

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>w(xij)</td></tr><tr><td>3</td><td>10</td><td>0.9424778</td><td>0.5</td><td>0.46783396</td></tr><tr><td>6</td><td>10</td><td>1.8849556</td><td>0.5</td><td>0.54995267</td></tr><tr><td>9</td><td>10</td><td>2.8274334</td><td>0.5</td><td>0.17871220</td></tr></table>

12. Using Richardson’s method gives:

(a) For $h = 0 . 2$ and $k = 0 . 0 4$

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>w(xi)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.1406275</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.2315952</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.47267557</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.08733023</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>w(xij)</td></tr><tr><td>2</td><td>10</td><td>0.2</td><td>0.4</td><td>0.37945980</td></tr><tr><td>4</td><td>10</td><td>0.4</td><td>0.4</td><td>0.61397885</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.61397885</td></tr><tr><td>8</td><td>10</td><td>0.8</td><td>0.4</td><td>0.37945980</td></tr></table>

$^ *$ 13. We have

$$
a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = ( 1 - 2 \lambda ) \sin \frac { i \pi } { m } + \lambda \sin \frac { 2 \pi i } { m }
$$

and

$$
\begin{array} { l } { { \mu _ { i } v _ { 1 } ^ { ( i ) } = \left[ 1 - 4 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \sin { \frac { i \pi } { m } } = \left[ 1 - 4 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \left( 2 \sin { \frac { i \pi } { 2 m } } \cos { \frac { i \pi } { 2 m } } \right) } } \\ { { \phantom { \mu _ { i } v _ { 1 } ^ { ( i ) } = } = 2 \sin { \frac { i \pi } { 2 m } } \cos { \frac { i \pi } { 2 m } } - 8 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 3 } \cos { \frac { i \pi } { 2 m } } . } } \end{array}
$$

However,

$$
\begin{array} { c } { { \displaystyle \left( 1 - 2 \lambda \right) \sin \displaystyle \frac { i \pi } { m } + \lambda \sin \displaystyle \frac { 2 \pi i } { m } = 2 ( 1 - 2 \lambda ) \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } + 2 \lambda \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i \pi } { m } } } \\ { { = 2 ( 1 - 2 \lambda ) \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } } } \\ { { + 2 \lambda \displaystyle \left[ 2 \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } \right] \left[ 1 - 2 \left( \sin \displaystyle \frac { i \pi } { 2 m } \right) ^ { 2 } \right] } } \\ { { = 2 \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } - 8 \lambda \cos \displaystyle \frac { i \pi } { 2 m } \left[ \sin \displaystyle \frac { i \pi } { 2 m } \right] ^ { 3 } . } } \end{array}
$$

Thus

$$
a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = \mu _ { i } v _ { 1 } ^ { ( i ) } .
$$

Further,

$$
\begin{array} { r l } & { a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j + 1 } ^ { ( i ) } = \lambda \sin \frac { i ( j - 1 ) \pi } { m } + ( 1 - 2 \lambda ) \sin \frac { i j \pi } { m } + \lambda \sin \frac { i ( j + 1 ) \pi } { m } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a } = \lambda \biggl ( \sin \frac { i j \pi } { m } \cos \frac { i \pi } { m } - \sin \frac { i \pi } { m } \cos \frac { i j \pi } { m } \biggr ) + ( 1 - 2 \lambda ) \sin \frac { i j \pi } { m } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } + \lambda \biggl ( \sin \frac { i j \pi } { m } - 2 \lambda \sin \frac { i j \pi } { m } + 2 \lambda \biggr ) } \\ & { = \sin \frac { i j \pi } { m } - 2 \lambda \sin \frac { i j \pi } { m } + 2 \lambda \sin \frac { i \pi } { m } \biggr ( \cos \frac { i \pi } { m } - 1 \biggr ) } \end{array}
$$

and

$$
\begin{array} { l } { { \mu _ { i } v _ { j } ^ { ( i ) } = \left[ 1 - 4 \lambda \left( \sin { \displaystyle \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \sin \displaystyle \frac { i j \pi } { m } = \left[ 1 - 4 \lambda \left( \displaystyle \frac { 1 } { 2 } - \displaystyle \frac { 1 } { 2 } \cos { \displaystyle \frac { i \pi } { m } } \right) \right] \sin \displaystyle \frac { i j \pi } { m } } } \\ { { = \left[ 1 + 2 \lambda \left( \cos { \displaystyle \frac { i \pi } { m } } - 1 \right) \right] \sin \displaystyle \frac { i j \pi } { m } , } } \end{array}
$$

so

$$
a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j } ^ { ( i ) } = \mu _ { i } v _ { j } ^ { ( i ) } .
$$

Similarly,

$$
a _ { m - 2 , m - 1 } v _ { m - 2 } ^ { ( i ) } + a _ { m - 1 , m - 1 } v _ { m - 1 } ^ { ( i ) } = \mu _ { i } v _ { m - 1 } ^ { ( i ) } ,
$$

so $A \mathbf { v } ^ { ( i ) } = \mu _ { i } \mathbf { v } ^ { ( i ) }$ .

$^ { * } 1 4$ . We have

$$
\begin{array} { l } { { a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = \left( 1 + 2 \lambda \right) \sin { \displaystyle \frac { i \pi } { m } } - \lambda \sin { \displaystyle \frac { 2 \pi i } { m } } = \left( 1 + 2 \lambda \right) \sin { \displaystyle \frac { i \pi } { m } } - 2 \lambda \sin { \displaystyle \frac { i \pi } { m } } \cos { \displaystyle \frac { i \pi } { m } } } } \\ { { = \sin { \displaystyle \frac { i \pi } { m } } \left[ 1 + 2 \lambda \left( 1 - \cos { \displaystyle \frac { i \pi } { m } } \right) \right] } } \end{array}
$$

and

$$
\mu _ { i } v _ { 1 } ^ { ( i ) } = \left[ 1 + 4 \lambda \left( \sin \frac { i \pi } { 2 m } \right) ^ { 2 } \right] \sin \frac { i \pi } { m } = \left[ 1 + 2 \lambda \left( 1 - \cos \frac { i \pi } { m } \right) \right] \sin \frac { i \pi } { m } = a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } .
$$

In general,

$$
\begin{array} { l } { { a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j + 1 } ^ { ( i ) } = - \lambda \sin \displaystyle \frac { i ( j - 1 ) \pi } { m } + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } - \lambda \sin \displaystyle \frac { i ( j + 1 ) \pi } { m } } } \\ { { \displaystyle \qquad = - \lambda \left( \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } - \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i j \pi } { m } \right) + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } } } \\ { { \displaystyle \qquad - \lambda \left( \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } + \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i j \pi } { m } \right) } } \\ { { \displaystyle \qquad = - 2 \lambda \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } } } \\ { { \displaystyle \qquad = \left[ 1 + 2 \lambda \left( 1 - \cos \displaystyle \frac { i \pi } { m } \right) \right] \sin \displaystyle \frac { i j \pi } { m } = \mu _ { i } v _ { j } ^ { ( i ) } . } } \end{array}
$$

Similarly,

$$
a _ { m - 2 , m - 1 } v _ { m - 2 } ^ { ( i ) } + a _ { m - 1 , m - 1 } v _ { m - 1 } ^ { ( i ) } = \mu _ { i } v _ { m - 1 } ^ { ( i ) } .
$$

Thus, $A \mathbf { v } ^ { ( i ) } = \mu _ { i } \mathbf { v } ^ { ( i ) }$ . Since $A$ is symmetric with positive eigenvalues, $A$ is positive definite. Further,

$$
\sum _ { j = 1 , j \neq i } ^ { n } \left| a _ { i j } \right| = 2 \lambda < 1 + 2 \lambda = | a _ { i i } | , \quad { \mathrm { f o r } } 1 \leq i \leq n ,
$$

so $A$ is diagonally dominant.

$^ \mathrm { * _ { 1 5 } }$ . To modify Algorithm 12.2, change the following:

Step 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { w _ { 0 } = \phi ( t ) ; } \\ & { z _ { 1 } = ( w _ { 1 } + \lambda w _ { 0 } ) / l _ { 1 } . } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

Step $^ { 8 }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = ( w _ { i } + \lambda z _ { i - 1 } ) / l _ { i } ;
$$

Set

$$
z _ { m - 1 } = ( w _ { m - 1 } + \lambda w _ { m } + \lambda z _ { m - 2 } ) / l _ { m - 1 } .
$$

Step 11 OUTPUT $\mathbf { \rho } ( t )$ ;

To modify Algorithm 12.3, change the following:

Step 1 Set

Step 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { z _ { 1 } = \left[ ( 1 - \lambda ) w _ { 1 } + \frac { \lambda } { 2 } w _ { 2 } + \frac { \lambda } { 2 } \displaybreaks _ { 0 } + \frac { \lambda } { 2 } \phi ( t ) \right] / l _ { 1 } ; } \\ & { w _ { 0 } = \phi ( t ) . } \end{array}
$$

Step $^ { 8 }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = \left[ ( 1 - \lambda ) w _ { i } + { \textstyle \frac { \lambda } { 2 } } ( w _ { i + 1 } + w _ { i - 1 } + z _ { i - 1 } ) \right] / l _ { i } ;
$$

Set

$$
\begin{array} { r l } & { z _ { m - 1 } = \left[ ( 1 - \lambda ) w _ { m - 1 } + \frac { \lambda } { 2 } ( w _ { m } + w _ { m - 2 } + z _ { m - 2 } + \psi ( t ) ) \right] / l _ { m - 1 } ; } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

Step 11 OUTPUT $( t )$ ;

16. The modifications of Algorithms 12.2 and 12.3 give the following results:

(a) For modified Algorithm 12.2 we have

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>3</td><td>25</td><td>0.3</td><td>0.25</td><td>0.2883460</td></tr><tr><td>5</td><td>25</td><td>0.5</td><td>0.25</td><td>0.3468410</td></tr><tr><td>8</td><td>25</td><td>0.8</td><td>0.25</td><td>0.2169217</td></tr></table>

(b) For modified Algorithm 12.3 we have

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>3</td><td>25</td><td>0.3</td><td>0.25</td><td>0.2798737</td></tr><tr><td>5</td><td>25</td><td>0.5</td><td>0.25</td><td>0.3363686</td></tr><tr><td>8</td><td>25</td><td>0.8</td><td>0.25</td><td>0.2107662</td></tr></table>

17. To modify Algorithm 12.2, change the following:

STEP 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { w _ { 0 } = \phi ( t ) ; } \\ & { z _ { 1 } = ( w _ { 1 } + \lambda w _ { 0 } ) / l _ { 1 } . } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

STEP $\boldsymbol { \vartheta }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = ( w _ { i } + \lambda z _ { i - 1 } ) / l _ { i } ;
$$

$$
z _ { m - 1 } = ( w _ { m - 1 } + \lambda w _ { m } + \lambda z _ { m - 2 } ) / l _ { m - 1 } .
$$

STEP 11 OUTPUT $\mathbf { \rho } ( t )$

To modify Algorithm 12.3, change the following:

STEP 1 Set

STEP 7 Set

$$
\begin{array} { r l } & { h = l / m ; } \\ & { k = T / N ; } \\ & { \lambda = \alpha ^ { 2 } k / h ^ { 2 } ; } \\ & { w _ { m } = \psi ( 0 ) ; } \\ & { w _ { 0 } = \phi ( 0 ) . } \\ & { t = j k ; } \\ & { z _ { 1 } = \left[ ( 1 - \lambda ) w _ { 1 } + \frac { \lambda } { 2 } w _ { 2 } + \frac { \lambda } { 2 } _ { 0 } + \frac { \lambda } { 2 } \phi ( t ) \right] / l _ { 1 } ; } \\ & { w _ { 0 } = \phi ( t ) . } \end{array}
$$

STEP $\boldsymbol { \vartheta }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = \left[ ( 1 - \lambda ) w _ { i } + { \textstyle \frac { \lambda } { 2 } } ( w _ { i + 1 } + w _ { i - 1 } + z _ { i - 1 } ) \right] / l _ { i } ;
$$

Set

$$
\begin{array} { r l } & { z _ { m - 1 } = \left[ ( 1 - \lambda ) w _ { m - 1 } + \frac { \lambda } { 2 } ( w _ { m } + w _ { m - 2 } + z _ { m - 2 } + \psi ( t ) ) \right] / l _ { m - 1 } ; } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

STEP 11 OUTPUT $( t )$ ;

18. The approximations to the temperature distributions using Algorithms 12.2 and 12.3 are given in the following table:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij(Algorithm 12.3)</td><td>Wij (Algorithm 12.2)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.225</td><td>1.223279</td><td>1.207730</td></tr><tr><td>6</td><td>10</td><td>0.75</td><td>0.225</td><td>1.862358</td><td>1.836564</td></tr><tr><td>10</td><td>10</td><td>1.35</td><td>0.225</td><td>0.701087</td><td>0.692834</td></tr></table>

19. (a) The approximate temperature at some typical points is given in the table.

<table><tr><td>i</td><td>j</td><td>ri</td><td>tj</td><td>Wi,j</td></tr><tr><td>1</td><td>20</td><td>0.6</td><td>10</td><td>137.6753</td></tr><tr><td>2</td><td>20</td><td>0.7</td><td>10</td><td>245.9678</td></tr><tr><td>3</td><td>20</td><td>0.8</td><td>10</td><td>340.2862</td></tr><tr><td>4</td><td>20</td><td>0.9</td><td>10</td><td>424.1537</td></tr></table>

(b) The strain is approximately $I = 1 2 4 2 . 5 3 7$ .

# Exercise Set 12.3, page 744

$^ { * } 1$ . The Wave Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>4</td><td>0.25</td><td>1.0</td><td>-0.7071068</td><td>-0.7071068</td></tr><tr><td>3</td><td>4</td><td>0.50</td><td>1.0</td><td>-1.0000000</td><td>-1.0000000</td></tr><tr><td>4</td><td>4</td><td>0.75</td><td>1.0</td><td>-0.7071068</td><td>-0.7071068</td></tr></table>

2. The Wave Equation Finite-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,ti)</td></tr><tr><td>2</td><td>4</td><td>0.125</td><td>0.5</td><td>0.48428862</td><td>0.47942554</td></tr><tr><td>3</td><td>4</td><td>0.250</td><td>0.5</td><td>0.00000000</td><td>0</td></tr><tr><td>4</td><td>4</td><td>0.375</td><td>0.5</td><td>-0.48428862</td><td>0.47942554</td></tr></table>

3. The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 1 0 }$ and $k = 0 . 0 5$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>π/5</td><td>0.5</td><td>0.5163933</td><td>0.5158301</td></tr><tr><td>5</td><td>10</td><td>π/2</td><td>0.5</td><td>0.8785407</td><td>0.8775826</td></tr><tr><td>8</td><td>10</td><td>4π/5</td><td>0.5</td><td>0.5163933</td><td>0.5158301</td></tr></table>

The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 2 0 }$ and $k = 0 . 1$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>5</td><td>π/5</td><td>0.5</td><td>0.5159163</td></tr><tr><td>10</td><td>5</td><td>π/2</td><td>0.5</td><td>0.8777292</td></tr><tr><td>16</td><td>5</td><td>4π/5</td><td>0.5</td><td>0.5159163</td></tr></table>

The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 2 0 }$ and $k = 0 . 0 5$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>10</td><td>π/5</td><td>0.5</td><td>0.5159602</td></tr><tr><td>10</td><td>10</td><td>π/2</td><td>0.5</td><td>0.8778039</td></tr><tr><td>16</td><td>10</td><td>4π/5</td><td>0.5</td><td>0.5159602</td></tr></table>

4. The Wave Equation Finite-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>2</td><td>10</td><td>0.62831853</td><td>0.5</td><td>0.5233857</td></tr><tr><td>5</td><td>10</td><td>1.57079633</td><td>0.5</td><td>0.8904370</td></tr><tr><td>8</td><td>10</td><td>2.51327412</td><td>0.5</td><td>0.5233857</td></tr></table>

For $h = 0 . 0 5$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>5</td><td>0.62831853</td><td>0.5</td><td>0.53000146</td></tr><tr><td>10</td><td>5</td><td>1.57079633</td><td>0.5</td><td>0.90169234</td></tr><tr><td>16</td><td>5</td><td>2.51327412</td><td>0.5</td><td>0.53000146</td></tr></table>

For $h = 0 . 0 5$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>10</td><td>0.62831853</td><td>0.5</td><td>0.52299419</td></tr><tr><td>10</td><td>10</td><td>1.57079633</td><td>0.5</td><td>0.88977086</td></tr><tr><td>16</td><td>10</td><td>2.51327412</td><td>0.5</td><td>0.52299419</td></tr></table>

5. The Wave Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>3</td><td>0.2</td><td>0.3</td><td>0.6729902</td><td>0.61061587</td></tr><tr><td>5</td><td>3</td><td>0.5</td><td>0.3</td><td>0</td><td>0</td></tr><tr><td>8</td><td>3</td><td>0.8</td><td>0.3</td><td>-0.6729902</td><td>-0.61061587</td></tr></table>

6. Algorithm 12.4 gives the following results:

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td></tr><tr><td>2</td><td>5</td><td>0.2</td><td>0.5</td><td>-1</td></tr><tr><td>5</td><td>5</td><td>0.5</td><td>0.5</td><td>0</td></tr><tr><td>8</td><td>5</td><td>0.8</td><td>0.5</td><td>1</td></tr></table>

7. (a) The air pressure for the open pipe is $p ( 0 . 5 , 0 . 5 ) \approx 0 . 9$ and $p ( 0 . 5 , 1 . 0 ) \approx 2 . 7$ . (b) The air pressure for the closed pipe is $p ( 0 . 5 , 0 . 5 ) \approx 0 . 9$ and $p ( 0 . 5 , 1 . 0 ) \approx 0 . 9 1 8 7 9 2 7$

\*8. Approximate voltages and currents are given in the following table.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Voltage</td><td>Current</td></tr><tr><td>5</td><td>2</td><td>50</td><td>0.2</td><td>77.769</td><td>3.88845</td></tr><tr><td>12</td><td>2</td><td>120</td><td>0.2</td><td>104.60</td><td>-1.69931</td></tr><tr><td>18</td><td>2</td><td>180</td><td>0.2</td><td>33.986</td><td>-5.22995</td></tr><tr><td>5</td><td>5</td><td>50</td><td>0.5</td><td>77.702</td><td>3.88510</td></tr><tr><td>12</td><td>5</td><td>120</td><td>0.5</td><td>104.51</td><td>-1.69785</td></tr><tr><td>18</td><td>5</td><td>180</td><td>0.5</td><td>33.957</td><td>-5.22453</td></tr></table>

# Exercise Set 12.4, page 758

$^ * 1$ . With $E _ { 1 } = ( 0 . 2 5 , 0 . 7 5 )$ , $E _ { 2 } = ( 0 , 1 )$ , $E _ { 3 } = ( 0 . 5 , 0 . 5 )$ , and $E _ { 4 } = ( 0 , 0 . 5 )$ , the basis functions are

$$
\begin{array} { r c l } { \phi _ { 1 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 4 x } & { \mathrm { o n ~ } T _ { 1 } } \\ { - 2 + 4 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 2 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { - 1 - 2 x + 2 y } & { \mathrm { o n ~ } T _ { 1 } } \\ { 0 } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 3 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 0 } & { \mathrm { o n ~ } T _ { 1 } } \\ { 1 + 2 x - 2 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 4 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 2 - 2 x - 2 y } & { \mathrm { o n ~ } T _ { 1 } } \\ { 2 - 2 x - 2 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \end{array}
$$

and $\gamma _ { 1 } = 0 . 3 2 3 8 2 5$ , $\gamma _ { 2 } = 0$ , $\gamma _ { 3 } = 1 . 0 0 0 0$ , and $\gamma _ { 4 } = 0$ .

2. With $E _ { 1 } ~ = ~ ( 0 . 2 5 , 0 . 7 5 )$ , $E _ { 2 } ~ = ~ ( 0 , 1 )$ , $E _ { 3 } ~ = ~ ( 0 . 5 , 0 . 5 )$ , $E _ { 4 } ~ = ~ ( 0 , 0 . 5 )$ , $E _ { 5 } ~ = ~ ( 0 , 0 . 7 5 )$ , and $E _ { 6 } = ( 0 . 2 5 , 0 . 5 )$ , the following results are obtained:

<table><tr><td>i</td><td>j</td><td>蜀</td><td>福</td><td>S</td><td></td><td>node</td></tr><tr><td>1</td><td>1</td><td>0</td><td>4</td><td></td><td>0</td><td>1</td></tr><tr><td>1</td><td>2</td><td>一 -3</td><td></td><td>0</td><td>4</td><td>2</td></tr><tr><td>1</td><td>3</td><td>4</td><td></td><td>-4</td><td>-4</td><td>5</td></tr><tr><td>2</td><td>1</td><td>-2</td><td></td><td>0</td><td>4</td><td>1</td></tr><tr><td>2</td><td>2</td><td>-1</td><td></td><td>4</td><td>0</td><td>3</td></tr><tr><td>2</td><td>3</td><td>4</td><td>-4</td><td></td><td>-4</td><td>6</td></tr><tr><td>3</td><td>1</td><td>0</td><td>4</td><td></td><td>0</td><td>1</td></tr><tr><td>3</td><td>2</td><td>3</td><td>0</td><td></td><td>-4</td><td>4</td></tr><tr><td>3</td><td>3</td><td>一 -2</td><td>-4</td><td></td><td>4</td><td>5</td></tr><tr><td>4</td><td>1</td><td>一 -2</td><td></td><td>0</td><td>4</td><td>1</td></tr><tr><td>4</td><td>2</td><td>1</td><td></td><td></td><td>0</td><td>4</td></tr><tr><td>4</td><td>3</td><td>2</td><td></td><td>4</td><td>-4</td><td>6</td></tr></table>

So $\gamma _ { 1 } = 0 . 3 2 3 8 2 5 5$ , $\gamma _ { 2 } = 0$ , $\gamma _ { 3 } = 1 . 0$ , $\gamma _ { 4 } = 0$ , $\gamma _ { 5 } = 0$ , and $\gamma _ { 6 } = 0 . 5$ .

3. The Finite-Element Algorithm with $K = 8 , N = 8 , M = 3 2 , n = 9 , m = 2 5$ , and $N L = 0$ gives the following results, where the labeling is as shown in the diagram.

![](images/cfea5d3e7412aa6ae2d2e015ab75c164394bf683fe8f4a29552d3046bc76b073.jpg)

With the labeling shown in the figure:

$\gamma _ { 1 } = 0 . 5 1 1 0 2 3$ , $\gamma _ { 2 } = 0 . 7 2 0 4 7 6$ , $\gamma _ { 3 } = 0 . 5 0 7 8 9 9$ , $\gamma _ { 4 } = 0 . 7 2 0 4 7 6$ ,   
$\gamma _ { 5 } = 1 . 0 1 8 8 5$ , $\gamma _ { 6 } = 0 . 7 2 0 4 7 6$ , $\gamma _ { 7 } = 0 . 5 0 7 8 9 6$ , $\gamma _ { 8 } = 0 . 7 2 0 4 7 6$ ,   
$\gamma _ { 9 } = 0 . 5 1 1 0 2 3 \mathrm { a n d } \gamma _ { i } = 0 , \mathrm { f o r } 1 0 \leq i \leq 2 5 $   
$u ( 0 . 1 2 5 , 0 . 1 2 5 ) \approx 0 . 6 1 4 1 8 7$ , $u ( 0 . 1 2 5 , 0 . 2 5 ) \approx 0 . 6 9 0 3 4 3 , u ( 0 . 2 5 , 0 . 1 2 5 ) \approx 0 . 6 9 0 3 4 3$ , and $u ( 0 . 2 5 , 0 . 2 5 ) \approx$   
0.720476

4. The Finite-Element Algorithm with $K = 8$ , $N = 2 2$ , $M = 3 2$ , $n = 2 5$ , $m = 2 5$ , and $N L = 1 6$ gives the results shown below, where the labeling is as shown in the figure for Exercise 3:

$\gamma _ { 1 } = - 0 . 4 8 9 6 9 5$ , $\gamma _ { 2 } = 0 . 0 1 6 3 2 5 0$ , $\gamma _ { 3 } = 0 . 5 2 4 2 4 3$ , $\gamma _ { 4 } = 0 . 0 1 6 3 2 5 0$ ,   
$\gamma _ { 5 } = 0 . 0 0 8 6 8 5 1 8$ , $\gamma _ { 6 } = 0 . 0 1 6 3 2 5 0$ , $\gamma _ { 7 } = 0 . 5 2 4 2 4 3$ , $\gamma _ { 8 } = 0 . 0 1 6 3 2 5 0$ ,   
$\gamma _ { 9 } = - 0 . 4 8 9 6 9 5$ , $\gamma _ { 1 0 } = - 1 . 0 6 9 1 3$ , $\gamma _ { 1 1 } = - 0 . 6 8 4 3 0 8$ , $\gamma _ { 1 2 } = 0 . 0 5 8 1 5 8 3$ ,   
$\gamma _ { 1 3 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 1 4 } = 0 . 9 6 \dot { 2 } 8 0 1$ , $\gamma _ { 1 5 } = - 0 . 6 8 4 3 0 8$ , $\gamma _ { 1 6 } = 0 . 7 5 2 8 7 1$ ,   
$\gamma _ { 1 7 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 1 8 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 1 9 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 2 0 } = - 0 . 6 8 4 3 0 8$ ,   
$\gamma _ { 2 1 } = 0 . 9 6 2 8 0 1$ , $\gamma _ { 2 2 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 2 3 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 2 4 } = - 0 . 6 8 4 3 0 8$ ,   
and $\gamma _ { 2 5 } = - 1 . 0 6 9 1 3$ .   
$u ( 0 . 1 2 5 , 0 . 1 2 5 ) \approx 0 . 2 7 0 2 8 4$ , $u ( 0 . 1 2 5 , 0 . 2 5 ) \approx - 0 . 2 3 8 5 9 5$ , $u ( 0 . 2 5 , 0 . 1 2 5 ) \approx - 0 . 2 3 8 5 9 5$ , and $u ( 0 . 2 5 , 0 . 2 5 ) \approx 0 . 0 1 6 3 2 5 0$

$^ { * } 5$ . The Finite-Element Algorithm with $K = 0 , N = 1 2 , M = 3 2 , n = 2 0 , m = 2 7$ , and $N L = 1 4$ gives the following results, where the labeling is as shown in the diagram.

![](images/c86ee0a0da42a53813869b66754c05b870f97d11c64d3ec45f22b472f0fc8061.jpg)

$u ( 1 , 0 ) \approx 2 2 . 9 2 8 2 4$ , $u ( 4 , 0 ) \approx 2 2 . 8 4 6 6 3$ , and $u \left( { \frac { 5 } { 2 } } , { \frac { \sqrt { 3 } } { 2 } } \right) \approx 1 8 . 8 5 8 9 5$ .