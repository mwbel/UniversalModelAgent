# Theorem 9.2

f $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ is a set of $\pmb { n }$ linearly independent vectors in $\mathbb { R } ^ { n }$ , then any vector $\mathbf { x } \in \mathbb { R } ^ { n }$ can be written uniquely as

$$
{ \bf x } = \beta _ { 1 } { \bf v } ^ { ( 1 ) } + \beta _ { 2 } { \bf v } ^ { ( 2 ) } + \beta _ { 3 } { \bf v } ^ { ( 3 ) } + \cdot \cdot \cdot + \beta _ { n } { \bf v } ^ { ( n ) } ,
$$

for some collection of constants $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$

Proof Suppose that A is the matrix whose columns are the vectors v(l), v(2),.., v(n). Then the set {v(l),v(2),..., is linearly independent if and only if the matrix equation $A { \pmb { \alpha } } = { \pmb 0 }$ has the unique solution $\alpha = 0$ . But by Theorem 6.16, this is equivalent to the matrix equation $A { \boldsymbol { \beta } } = \mathbf { x }$ ,having a unique solution for any vector $\textbf { x } \in \mathbb { R } ^ { n }$ . This, in turn, equivalent to the statement that for any $\mathbf { x } \in \mathbb { R } ^ { n }$ ，

$$
\mathbf { x } = \beta _ { 1 } \mathbf { v } ^ { ( 1 ) } + \beta _ { 2 } \mathbf { v } ^ { ( 2 ) } + \cdot \cdot \cdot + \beta _ { n } \mathbf { v } ^ { ( n ) } ,
$$

for some unique set of constants $\beta _ { 1 } , \beta _ { 2 } , \cdots , \beta _ { n }$

Any collection of $n$ linearly independent vectors in $\mathbb { R } ^ { n }$ is called a basis for $\mathbb { R } ^ { n }$

Let $\mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ ， $\mathbf { v } ^ { ( 2 ) } = ( - 1 , 1 , 1 ) ^ { t }$ ,and $\mathbf { v } ^ { ( 3 ) } = ( 0 , 4 , 2 ) ^ { t }$ .If $\alpha _ { 1 } , \alpha _ { 2 }$ ,and $\alpha _ { 3 }$ are numbers with

$$
{ \bf 0 } = \alpha _ { 1 } { \bf v } ^ { ( 1 ) } + \alpha _ { 2 } { \bf v } ^ { ( 2 ) } + \alpha _ { 3 } { \bf v } ^ { ( 3 ) } ,
$$

then

$$
\begin{array} { c } { { ( 0 , 0 , 0 ) ^ { t } = \alpha _ { 1 } ( 1 , 0 , 0 ) ^ { t } + \alpha _ { 2 } ( - 1 , 1 , 1 ) ^ { t } + \alpha _ { 3 } ( 0 , 4 , 2 ) ^ { t } } } \\ { { { } } } \\ { { = ( \alpha _ { 1 } - \alpha _ { 2 } , \alpha _ { 2 } + 4 \alpha _ { 3 } , \alpha _ { 2 } + 2 \alpha _ { 3 } ) ^ { t } , } } \end{array}
$$

so

$$
\alpha _ { 1 } - \alpha _ { 2 } = 0 , \quad \alpha _ { 2 } + 4 \alpha _ { 3 } = 0 , \quad \mathrm { a n d } \quad \alpha _ { 2 } + 2 \alpha _ { 3 } = 0 .
$$

Since the only solution to this system is $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = 0$ , the set $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } \}$ is linearly independent in $\mathbb { R } ^ { 3 }$ and is a basis for $\mathbb { R } ^ { 3 }$

Any vector ${ \bf x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t }$ in $\mathbb { R } ^ { 3 }$ can be written as

$$
{ \bf x } = \beta _ { 1 } { \bf v } ^ { ( 1 ) } + \beta _ { 2 } { \bf v } ^ { ( 2 ) } + \beta _ { 3 } { \bf v } ^ { ( 3 ) } ,
$$

by choosing

$$
\beta _ { 1 } = x _ { 1 } - x _ { 2 } + 2 x _ { 3 } , \quad \beta _ { 2 } = 2 x _ { 3 } - x _ { 2 } , \quad \mathrm { a n d } \quad \beta _ { 3 } = \frac { 1 } { 2 } ( x _ { 2 } - x _ { 3 } ) .
$$

The next result will be used in the following section to develop the Power method for approximating eigenvalues. A proof of this result is considered in Exercise 8.

If $A$ is a matrix and $\lambda _ { 1 } , \ldots , \lambda _ { k }$ are distinct eigenvalues of $A$ with associated eigenvectors $\mathbf { x } ^ { ( 1 ) } , \mathbf { x } ^ { ( 2 ) } , \ldots , \mathbf { x } ^ { ( k ) }$ ，then $\{ \mathbf { x } ^ { ( 1 ) } , \mathbf { x } ^ { ( 2 ) } , \ldots , \mathbf { x } ^ { ( k ) } \}$ is linearly independent.

In Section 8.2 we considered orthogonal and orthonormal sets of functions. Vectors with these properties are defined in a similar manner.

# Definition 9.4

A set of vectors $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ is called orthogonal if $( \mathbf { v } ^ { ( i ) } ) ^ { t } \mathbf { v } ^ { ( j ) } = 0$ ,for all $i \neq j$ If, in addition, $( \mathbf { v } ^ { ( i ) } ) ^ { t } \mathbf { v } ^ { ( i ) } = 1$ ,for all $i = 1 , 2 , \dots , n$ ,then the set is orthonormal. ■

Since $\mathbf { x } ^ { t } \mathbf { x } = \| \mathbf { x } \| _ { 2 } ^ { 2 }$ ,a set of orthogonal vectors $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ is orthonormal if and only if

$$
\| \mathbf { v } ^ { ( i ) } \| _ { 2 } = 1 , \quad { \mathrm { f o r } } \operatorname { e a c h } i = 1 , 2 , \ldots , n .
$$

# EXAMPLE 2

The vectors $\mathbf { v } ^ { ( 1 ) } = ( 0 , 4 , 2 ) ^ { t }$ ， $\mathbf { v } ^ { ( 2 ) } = ( - 1 , - \frac { 1 } { 5 } , \frac { 2 } { 5 } ) ^ { t }$ , and $\mathbf { v } ^ { ( 3 ) } = ( \frac { 1 } { 6 } , - \frac { 1 } { 6 } , \frac { 1 } { 3 } ) ^ { t }$ form an ortogonal set. The $l _ { 2 }$ norms of these vectors are

$$
\| \mathbf { v } ^ { ( 1 ) } \| _ { 2 } = 2 \sqrt { 5 } , \quad \| \mathbf { v } ^ { ( 2 ) } \| _ { 2 } = \frac { \sqrt { 3 0 } } { 5 } , \quad \mathrm { a n d } \quad \| \mathbf { v } ^ { ( 3 ) } \| _ { 2 } = \frac { \sqrt { 6 } } { 6 } .
$$

As a consequence, the vectors

$$
\begin{array} { r l } & { \mathbf { u } ^ { ( 1 ) } = \frac { \mathbf { v } ^ { ( 1 ) } } { \| \mathbf { v } ^ { ( 1 ) } \| _ { 2 } } = \left( 0 , \frac { 2 \sqrt { 5 } } { 5 } , \frac { \sqrt { 5 } } { 5 } \right) ^ { t } , } \\ & { \mathbf { u } ^ { ( 2 ) } = \frac { \mathbf { v } ^ { ( 2 ) } } { \| \mathbf { v } ^ { ( 2 ) } \| _ { 2 } } = \left( - \frac { \sqrt { 3 0 } } { 6 } , - \frac { \sqrt { 3 0 } } { 3 0 } , \frac { \sqrt { 3 0 } } { 1 5 } \right) ^ { t } , } \end{array}
$$

and

$$
\mathbf { u } ^ { ( 3 ) } = \frac { \mathbf { v } ^ { ( 3 ) } } { \| \mathbf { v } ^ { ( 3 ) } \| _ { 2 } } = \left( \frac { \sqrt { 6 } } { 6 } , - \frac { \sqrt { 6 } } { 6 } , \frac { \sqrt { 6 } } { 3 } \right) ^ { t }
$$

form an orthonormal set, since they inherit orthogonality from $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) }$ ,and $\mathbf { v } ^ { ( 3 ) }$ ,and, in addition,

$$
\lVert \mathbf { u } ^ { ( 1 ) } \rVert _ { 2 } = \lVert \mathbf { u } ^ { ( 2 ) } \rVert _ { 2 } = \lVert \mathbf { u } ^ { ( 3 ) } \rVert _ { 2 } = 1 .
$$

The proof of the next result is considered in Exercise 5.

# Theorem 9.5

An orthogonal set of nonzero vectors is linearly independent.

The terminology in the next definition follows from the fact that the columns of an orthogonal matrix will form an orthogonal (in fact, orthonormal) set of vectors.(See Exercise 6.)

# Definition 9.6

A matrix $Q$ is said to be an orthogonal matrix if $Q ^ { - 1 } = Q ^ { \prime }$

The permutation matrices discussed in Section 6.5 have this property, so they are orthogonal.

The orthogonal matrix $Q$ formed from the orthonormal set of vectors found in Example 2 is

$$
Q = [ \mathbf { u } ^ { ( 1 ) } , \mathbf { u } ^ { ( 2 ) } , \mathbf { u } ^ { ( 3 ) } ] = \left[ \begin{array} { c c c } { 0 } & { - \frac { \sqrt { 3 0 } } { 6 } } & { \frac { \sqrt { 6 } } { 6 } } \\ { \frac { 2 \sqrt { 5 } } { 5 } } & { - \frac { \sqrt { 3 0 } } { 3 0 } } & { - \frac { \sqrt { 6 } } { 6 } } \\ { \frac { \sqrt { 5 } } { 5 } } & { \frac { \sqrt { 3 0 } } { 1 5 } } & { \frac { \sqrt { 6 } } { 3 } } \end{array} \right] .
$$

Note that

$$
\begin{array} { r } { Q Q ^ { t } = \left[ \begin{array} { c c c } { 0 } & { \frac { - \sqrt { 3 0 } } { 6 } } & { \frac { \sqrt { 6 } } { 6 } } \\ { 2 \sqrt { 5 } } & { - \frac { \sqrt { 3 0 } } { 3 0 } } & { - \frac { \sqrt { 6 } } { 6 } } \\ { \frac { \sqrt { 5 } } { 5 } } & { \frac { \sqrt { 3 0 } } { 1 5 } } & { \frac { \sqrt { 6 } } { 3 } } \end{array} \right] \cdot \left[ \begin{array} { c c c } { 0 } & { \frac { 2 \sqrt { 5 } } { 5 } } & { \frac { \sqrt { 5 } } { 5 } } \\ { - \frac { \sqrt { 3 0 } } { 6 } } & { - \frac { \sqrt { 3 0 } } { 3 0 } } & { \frac { \sqrt { 3 0 } } { 1 5 } } \\ { \frac { \sqrt { 6 } } { 6 } } & { - \frac { \sqrt { 6 } } { 6 } } & { \frac { \sqrt { 6 } } { 3 } } \end{array} \right] = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

It is also true that $Q ^ { t } Q = I$ ,s0 $Q ^ { t } = Q ^ { - 1 }$

# Definition 9.7

Two matrices $A$ and $B$ are said to be similar if a nonsingular matrix $s$ exists with $A =$ $S ^ { - 1 } B S$ ■

The important feature of similar matrices is that they have the same eigenvalues.

# Theorem 9.8

Suppose $A$ and $B$ are similar matrices with $A = S ^ { - 1 } B S$ and $\lambda$ is an eigenvalue of $A$ with associated eigenvector $\mathbf { x }$ . Then $\lambda$ is an eigenvalue of $B$ with associated eigenvector $\mathbf { \nabla } S \mathbf { x }$ ■

Proof Suppose that $\mathbf { x } \neq \mathbf { 0 }$ is such that

$$
\begin{array} { r } { S ^ { - 1 } B S \mathbf { x } = A \mathbf { x } = \lambda \mathbf { x } . } \end{array}
$$

Multiplying on the left by the matrix $s$ gives

$$
B S \mathbf { x } = \lambda S \mathbf { x } .
$$

Since $\mathbf { x } \neq \mathbf { 0 }$ and $s$ is nonsingular, $S \mathbf { x } \neq \mathbf { 0 }$ . Hence, $\pmb { S } \mathbf { x }$ is an eigenvector of $B$ corresponding to its eigenvalue $\lambda$ ■ ■

The Maple command issimilar(A,B) returns true if $A$ and $B$ are similar and false otherwise.

The determination of eigenvalues is easy for a triangular matrix $A$ , for in this case $\lambda$ is a solution to the equation

$$
0 = \operatorname * { d e t } ( A - \lambda I ) = \prod _ { i = 1 } ^ { n } ( a _ { i i } - \lambda )
$$

if and only if $\lambda = a _ { i i }$ for some i. The next result describes a relationship, called a similarity transformation, between arbitrary matrices and triangular matrices.

# Theorem 9.9

# (Schur)

Let $A$ be an arbitrary matrix. A nonsingular matrix $U$ exists with the property that

$$
T = U ^ { - 1 } A U ,
$$

where $T$ is an upper-triangular matrix whose diagonal entries consist of the eigenvalues of $A$ ·

The matrix $U$ whose existence is ensured in Theorem 9.9 satisfies the condition $\| U \mathbf { x } \| _ { 2 } = \| \mathbf { x } \| _ { 2 }$ for any vector x. Matrices with this property are called unitary. Although we will not make use of this norm-preserving property, it does significantly increase the application of Schur's Theorem.

Theorem 9.9 is an existence theorem that ensures that the triangular matrix $T$ exists, but it does not provide a constructive means for finding $T$ ， since it requires a knowledge of the eigenvalues of $A$ . In most instances, the similarity transformation $U$ is too difficult to determine. The following restriction of Theorem 9.9 to symmetric matrices reduces the complication, since in this case the transformation matrix is orthogonal.

# Theorem 9.10

If $A$ is a symmetric matrix and $D$ is a diagonal matrix whose diagonal entries are the eigenvalues of $A$ , then there exists an orthogonal matrix $Q$ such that $D = Q ^ { - 1 } A Q \ =$ $Q ^ { t } A Q$

The following corollries to Theorem 9.10 demonstrate some of the interesting properties of symmetric matrices.

# Corollary 9.11

If $A$ is a symmetric $n \times n$ matrix then there exist $n$ eigenvectors of $A$ that form an orthonormal set, and the eigenvalues of $A$ are real numbers.

Proof If $Q = ( q _ { i j } )$ and $D = ( d _ { i j } )$ are the matrices specified in Theorem 9.10, then

$$
D = Q ^ { - 1 } A Q \quad { \mathrm { i m p l i e s ~ t h a t } } \quad A Q = Q D .
$$

Let $1 \leq i \leq n$ and $\mathbf { v } _ { i } = ( q _ { 1 i } , q _ { 2 i } , \dots , q _ { n i } ) ^ { t }$ be the $i$ th column of $Q$ . Then

$$
A \mathbf { v } _ { i } = d _ { i i } \mathbf { v } _ { i } ,
$$

and $d _ { i i }$ is an eigenvalue of $A$ with eigenvector, $\mathbf { v } _ { i }$ , the ith column of $Q$ . Since the columns of $Q$ are orthonormal, the eigenvectors of $A$ are orthonormal.

Multiplying this equation on the left by $\mathbf { v } _ { i } ^ { t }$ gives

$$
\mathbf { v } _ { i } ^ { t } A \mathbf { v } _ { i } = d _ { i i } \mathbf { v } _ { i } ^ { t } \mathbf { v } _ { i } .
$$

Since $\mathbf { v } _ { i } ^ { t } A \mathbf { v } _ { i }$ and $\mathbf { v } _ { i } ^ { t } \mathbf { v } _ { i }$ are real numbers and $\mathbf { v } _ { i } ^ { t } \mathbf { v } _ { i } = 1$ , the eigenvalue $d _ { i i } = \mathbf { v } _ { i } ^ { t } A \mathbf { v } _ { i }$ is a real number, for each $i = 1 , 2 , \dots , n$ ■

Recall from Section 6.6 that a symmetric matrix $A$ is called positive definite if for all nonzero vectors $\mathbf { x }$ we have $\mathbf { x } ^ { t } A \mathbf { x } > 0$ .The following theorem characterizes positive definite matrices in terms of eigenvalues. This eigenvalue property makes positive definite matrices important in applications.

A symmetric matrix $\pmb { A }$ is positive definite if and only if all the eigenvalues of $\pmb { A }$ are positive.

Proof First suppose that $A$ is positive definite and that $\lambda$ is an eigenvalue of $A$ with associated eigenvector $\pmb { \mathrm { x } }$ . Then

$$
0 < \mathbf { x } ^ { t } A \mathbf { x } = \lambda \mathbf { x } ^ { t } \mathbf { x } = \lambda \| \mathbf { x } \| _ { 2 } ^ { 2 } ,
$$

so $\lambda > 0$ . Hence, every eigenvalue of a positive definite matrix is positive.

To show the converse, suppose that $\pmb { A }$ is symmetric with positive eigenvalues. By Corollary 9.11, A has $\pmb { n }$ eigenvectors, $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( n ) }$ ,that form an orthonormal and, by Theorem 9.5, linearly independent set. Hence, for any $\mathbf { x } \neq 0$ there exists a unique set of nonzero constants $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$ for which

$$
\mathbf { x } = \sum _ { i = 1 } ^ { n } \beta _ { i } \mathbf { v } ^ { ( i ) } .
$$

Multiplying by $\mathbf { x } ^ { t } A$ gives

$$
\mathbf { x } ^ { t } A \mathbf { x } = \mathbf { x } ^ { t } \left( \sum _ { i = 1 } ^ { n } \beta _ { i } A \mathbf { v } ^ { ( i ) } \right) = \mathbf { x } ^ { t } \left( \sum _ { i = 1 } ^ { n } \beta _ { i } \lambda _ { i } \mathbf { v } ^ { ( i ) } \right) = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n } \beta _ { j } \beta _ { i } \lambda _ { i } ( \mathbf { v } ^ { ( j ) } ) ^ { t } \mathbf { v } ^ { ( i ) } .
$$

But the vectors $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \ldots , \mathbf { v } ^ { ( n ) }$ form an orthonormal set, so

$$
( \mathbf { v } ^ { ( j ) } ) ^ { t } \mathbf { v } ^ { ( i ) } = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f } } \ i \neq j , } \\ { 1 , } & { { \mathrm { i f } } \ i = j . } \end{array} \right. }
$$

This, together with the fact that the $\lambda _ { i }$ are all positive,implies that

$$
\mathbf { x } ^ { t } A \mathbf { x } = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n } \beta _ { j } \beta _ { i } \lambda _ { i } ( \mathbf { v } ^ { ( j ) } ) ^ { t } \mathbf { v } ^ { ( i ) } = \sum _ { i = 1 } ^ { n } \lambda _ { i } \beta _ { i } ^ { 2 } > 0 .
$$

Hence, $\pmb { A }$ is positive definite.

The final result of the section concerns bounds for the approximation of eigenvalues.

# Theorem 9.13 (Gerschgorin Circle)

Let $A$ be an $n \times n$ matrix and $R _ { i }$ denote the circle in the complex plane with center $a _ { i i }$ and radius $\sum _ { j = 1 \atop j \not = i } ^ { n } \lvert a _ { i j } \rvert$ ; that is,

$$
R _ { i } = \left\{ z \in \mathcal { C } \Bigg | | z - a _ { i i } | \leq \sum _ { j = 1 , \atop j \neq i } ^ { n } | a _ { i j } | \Bigg \} , \right.
$$

where C denotes the complex plane. The eigenvalues of A are contained within R = $\cup _ { i = 1 } ^ { n } R _ { i }$ . Moreover, the union of any $k$ of these circles that do not intersect the remaining $( n - k )$ contains precisely $k$ (counting multiplicities) of the eigenvalues.

Proof Suppose that $\lambda$ is an eigenvaue of $A$ with associaed eigenvector $\mathbf { x }$ , where $\| \mathbf { x } \| _ { \infty } =$ 1. Since $A \mathbf { x } = \lambda \mathbf { x }$ , the equivalent component representation is

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = \lambda x _ { i } , \quad { \mathrm { f o r } } \operatorname { e a c h } i = 1 , 2 , \ldots , n .
$$

If $k$ is an integer with $| x _ { k } | = \| \mathbf { x } \| _ { \infty } = 1$ , this equation, with $i = k$ , implies that

$$
\sum _ { j = 1 } ^ { n } a _ { k j } x _ { j } = \lambda x _ { k } .
$$

Thus,

$$
\sum _ { \stackrel { j = 1 , } { j \neq k } } ^ { n } a _ { k j } x _ { j } = \lambda x _ { k } - a _ { k k } x _ { k } = ( \lambda - a _ { k k } ) x _ { k } ,
$$

and

$$
| \lambda - a _ { k k } | \cdot | x _ { k } | = \left| \sum _ { j = 1 , \atop j \neq k } ^ { n } a _ { k j } x _ { j } \right| \leq \sum _ { j = 1 , \atop j \neq k } ^ { n } | a _ { k j } | | x _ { j } | .
$$

Since $| x _ { j } | \leq | x _ { k } | = 1$ , for all $j = 1 , 2 , \dots , n ,$

$$
| \lambda - a _ { k k } | \leq \sum _ { j = 1 , \atop j \neq k } ^ { n } | a _ { k j } | .
$$

Thus, $\lambda \in R _ { k }$ , which proves the first assertion in the theorem. The second part of this theorem requires a clever continuity argument. A quite readable proof is contained in $[ \mathbf { O r } 2 ,$ p. 48].

# EXAMPLE 4

For the matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { 1 } & { 1 } \\ { 0 } & { 2 } & { 1 } \\ { - 2 } & { 0 } & { 9 } \end{array} } \right] ,
$$

the circles in the Gerschgorin Theorem are (see Figure 9.1 on page 558)

$$
\begin{array} { r } { R _ { 1 } = \{ z \in \mathcal { C } \mid \vert z - 4 \vert \leq 2 \} , } \\ { R _ { 2 } = \{ z \in \mathcal { C } \mid \vert z - 2 \vert \leq 1 \} , } \end{array}
$$

and

$$
R _ { 3 } = \{ z \in \mathcal { C } \mid | z - 9 | \leq 2 \} .
$$

Since $R _ { 1 }$ and $R _ { 2 }$ are disjoint from $R _ { 3 }$ , there are precisely two eigenvalues within $R _ { 1 } \cup$ $R _ { 2 }$ and one within $R _ { 3 }$ . Moreover, since $\rho ( A ) = \mathbf { m } \mathbf { a x } _ { 1 \leq i \leq 3 } | \lambda _ { i } |$ , we have $7 \leq \rho ( A ) \leq 1 1$

![](images/164797d448b6c7fed398363b3c647f887b4a27a69230ea0013d59eb3e2c6d7b1.jpg)  
Figure 9.1

# ExErcise Set 9.1

1. Find the eigenvalues and associated eigenvectors of the following $3 \times 3$ matrices. Is there a set of three linearly independent eigenvectors?

$\begin{array} { r l } { \mathbf { a } . \mathbf { \xi } } & { { } A = { \left[ \begin{array} { l l l } { 2 } & { - 3 } & { 6 } \\ { 0 } & { 3 } & { - 4 } \\ { 0 } & { 2 } & { - 3 } \end{array} \right] } } \\ { \mathbf { c } . \mathbf { \xi } } & { { } A = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 1 } \\ { 0 } & { 2 } & { 0 } \\ { 1 } & { 0 } & { 2 } \end{array} \right] } } \\ { \mathbf { e } . \mathbf { \xi } } & { { } A = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \end{array} \right] } } \end{array}$ $\begin{array} { r l } { \mathbf { b . ~ } } & { { } A = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 1 } \\ { - 1 } & { - 1 } & { 2 } \end{array} \right] } \\ { \mathbf { d . ~ } } & { { } A = \left[ \begin{array} { c c c } { 2 } & { - 1 } & { - 1 } \\ { - 1 } & { 2 } & { - 1 } \\ { - 1 } & { - 1 } & { 2 } \end{array} \right] } \end{array}$ f. $A = { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] }$

2.The matrices in Exercise 1(c), (d),(e),and (f) are symmetric.

a. Are any positive definite? b. Consider the positive definite matrices in part (a). Construct an orthogonal matrix $Q$ for which $Q ^ { t } A Q = D$ ,a diagonal matrix,using the eigenvectors found in Exercise 1.

3.Use the Gerschgorin Circle Theorem to determine bounds for the eigenvalues of the following matrices.

$\begin{array} { r l } { \mathrm { a . } } & { { } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 1 } \\ { - 1 } & { - 1 } & { 2 } \end{array} \right] } } \\ { \mathrm { c . } } & { { } { \left[ \begin{array} { l l l } { 3 } & { 2 } & { 1 } \\ { 2 } & { 3 } & { 0 } \\ { 1 } & { 0 } & { 3 } \end{array} \right] } } \end{array}$ $\begin{array} { r l } { \mathbf { b } . } & { { } \left[ \begin{array} { r r r } { 4 } & { - 1 } & { 0 } \\ { - 1 } & { 4 } & { - 1 } \\ { - 1 } & { - 1 } & { 4 } \end{array} \right] } \\ { \mathbf { d } . } & { { } \left[ \begin{array} { r r r } { 4 . 7 5 } & { 2 . 2 5 } & { - 0 . 2 5 } \\ { 2 . 2 5 } & { 4 . 7 5 } & { 1 . 2 5 } \\ { - 0 . 2 5 } & { 1 . 2 5 } & { 4 . 7 5 } \end{array} \right] } \end{array}$

$$
\begin{array} { r } { \mathrm { ~ e ~ . ~ } \quad \left[ \begin{array} { r r r r } { - 4 } & { 0 } & { 1 } & { 3 } \\ { 0 } & { - 4 } & { 2 } & { 1 } \\ { 1 } & { 2 } & { - 2 } & { 0 } \\ { 3 } & { 1 } & { 0 } & { - 4 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } { \mathbf { f } . } & { { } \left[ \begin{array} { l l l l } { 1 } & { 0 } & { - 1 } & { 1 } \\ { 2 } & { 2 } & { - 1 } & { 1 } \\ { 0 } & { 1 } & { 3 } & { - 2 } \\ { 1 } & { 0 } & { 1 } & { 4 } \end{array} \right] } \end{array}
$$

4.Show that any four vectors in ${ \mathbb { R } } ^ { 3 }$ are linearly dependent.

i.Show that a set $\{ \mathbf { v } _ { 1 } , \ldots , \mathbf { v } _ { k } \}$ of $k$ nonzero orthogonal vectors is linearly independent.

6.Let $Q$ be an orthogonal matrix.

a. Show that the columns of $Q$ form an orthogonal set of vectors. b. Show that $\| Q \| _ { 2 } = 1$ and $\| Q ^ { t } \| _ { 2 } = 1$

7.Let $\{ \mathbf { v } _ { 1 } , \ldots , \mathbf { v } _ { n } \}$ be a set of orthonormal nonzero vectors in $\mathbb { R } ^ { n }$ and $\mathbf { x } \in \mathbb { R } ^ { n }$ . Determine the values of $c _ { k }$ ,for $k = 1 , 2 , \ldots , n$ ,if

$$
\mathbf { x } = \sum _ { k = 1 } ^ { n } c _ { k } \mathbf { v } _ { k } .
$$

8. Show that if $\pmb { A }$ is an $n \times n$ matrix with $\pmb { n }$ distinct eigenvalues,then $A$ has $\pmb { n }$ linearly independent eigenvectors.

9.In Exercise 25 of Section 6.6,a symmetric matrix

$$
A = { \left[ \begin{array} { l l l } { 1 . 5 9 } & { 1 . 6 9 } & { 2 . 1 3 } \\ { 1 . 6 9 } & { 1 . 3 1 } & { 1 . 7 2 } \\ { 2 . 1 3 } & { 1 . 7 2 } & { 1 . 8 5 } \end{array} \right] }
$$

was used to describe the average wing lengths of fruit flies that were offspring resulting from the mating of three mutants of the flies. The entry $a _ { i j }$ represents the average wing length of a fly that is the offspring of a male fly of type $i$ and a female fly of type $j$

a. Find the eigenvalues and associated eigenvectors of this matrix.   
b. Use Theorem 9.12 to answer the question posed in part (b) of Exercise 25 Section 6.6. Is this matrix positive definite?

10.A persymmetric matrix is a matrix that is symmetric about both diagonals; that is, an $N \times N$ matrix $A = ( a _ { i j } )$ is persymmetric if $a _ { i j } = a _ { j i } = a _ { N + 1 - i , N + 1 - j }$ ,for ail $i = 1 , 2 , \dots , N$ and $j = 1 , 2 , \dots , N .$ . A number of problems in communication theory have solutions that involve the eigenvalues and eigenvectors of matrices that are in persymmetric form. For example, the eigenvector corresponding to the minimal eigenvalue of the $4 \times 4$ persymmetric matrix

$$
A = \left[ { \begin{array} { r r r r } { 2 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { 2 } \end{array} } \right]
$$

gives the unit energy-channel impulse response for a given error sequence of length 2,and subsequently the minimum weight of any possible error sequence.

a. Use the Gerschgorin Circle Theorem to show that if $A$ is the matrix given above and $\lambda$ is its minimal eigenvalue,then $| \lambda - 4 | = \rho ( A - 4 I )$ , where $\rho$ denotes the spectral radius.   
b. Find the minimal eigenvalue of the matrix $\pmb { A }$ by finding all the eigenvalues $A - 4 I$ and computing its spectral radius. Then find the corresponding eigenvector.   
c. Use the Gerschgorin Circle Theorem to show that if $\lambda$ is the minimal eigenvalue of the matrix

$$
B = \left[ { \begin{array} { r r r r } { 3 } & { - 1 } & { - 1 } & { 1 } \\ { - 1 } & { 3 } & { - 1 } & { - 1 } \\ { - 1 } & { - 1 } & { 3 } & { - 1 } \\ { 1 } & { - 1 } & { - 1 } & { 3 } \end{array} } \right] ,
$$

then $| \lambda - 6 | = \rho ( B - 6 I )$

d.Repeat part (b) using the matrix $B$ and the result in part (c).

# 9.2 The Power Method

The Power method is an iterative technique used to determine the dominant eigenvalue of a matrix--that is, the eigenvalue with the largest magnitude. By modifying the method slightly, it can also used to determine other eigenvalues. One useful feature of the Power method is that it produces not only an eigenvalue, but an associated eigenvector. In fact, the Power method is often applied to find an eigenvector for an eigenvalue that is determined by some other means.

To apply the Power method, we assume that the $n \times n$ matrix $A$ has $\pmb { n }$ eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ with an associated collection of linearly independent eigenvectors $\{ \mathbf { v } ^ { ( 1 ) }$ ， $\mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ . Moreover, we assume that $A$ has precisely one eigenvalue, $\lambda _ { 1 }$ ,that is largest in magnitude, so that $| \lambda _ { 1 } | > | \lambda _ { 2 } | \geq | \lambda _ { 3 } | \geq \cdot \cdot \cdot \geq | \lambda _ { n } | \geq 0 .$

f $\mathbf { x }$ is any vector in $\mathbb { R } ^ { n }$ , the fact that $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ is linearly independent implies that constants $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$ exist with

$$
\mathbf { x } = \sum _ { j = 1 } ^ { n } \beta _ { j } \mathbf { v } ^ { ( j ) } .
$$

Multiplying both sides of this equation by $A , A ^ { 2 } , \ldots , A ^ { k }$ gives

$$
A \mathbf { x } = \sum _ { j = 1 } ^ { n } \beta _ { j } A \mathbf { v } ^ { ( j ) } = \sum _ { j = 1 } ^ { n } \beta _ { j } \lambda _ { j } \mathbf { v } ^ { ( j ) } ,
$$

$$
A ^ { 2 } \mathbf { x } = \sum _ { j = 1 } ^ { n } \beta _ { j } \lambda _ { j } A \mathbf { v } ^ { ( j ) } = \sum _ { j = 1 } ^ { n } \beta _ { j } \lambda _ { j } ^ { 2 } \mathbf { v } ^ { ( j ) } ,
$$

$$
A ^ { k } \mathbf { x } = \sum _ { j = 1 } ^ { n } \beta _ { j } \lambda _ { j } ^ { k } \mathbf { v } ^ { ( j ) } .
$$

If $\lambda _ { 1 } ^ { k }$ is factored from each term on the right side of the last equation, then

$$
A ^ { k } \mathbf { x } = \lambda _ { 1 } ^ { k } \sum _ { j = 1 } ^ { n } \beta _ { j } \left( \frac { \lambda _ { j } } { \lambda _ { 1 } } \right) ^ { k } \mathbf { v } ^ { ( j ) } .
$$

Since $| \lambda _ { 1 } | > | \lambda _ { j } |$ ,for all $j = 2 , 3 , \dots , n ,$ ,we have $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } ( \lambda _ { j } / \lambda _ { 1 } ) ^ { k } = 0 } \end{array}$ ,and

$$
\operatorname* { l i m } _ { k \to \infty } A ^ { k } \mathbf { x } = \operatorname* { l i m } _ { k \to \infty } \lambda _ { 1 } ^ { k } \beta _ { 1 } \mathbf { v } ^ { ( 1 ) } . )
$$

This sequence converges to 0 if $| \lambda _ { 1 } | < 1$ and diverges if $| \lambda _ { 1 } | > 1$ , provided,of course, that $\beta _ { 1 } \neq 0$

Advantage can be made of the relationship expressed in Eq. (9.1) by scaling the powers of $A ^ { k } \mathbf { x }$ in an appropriate manner to ensure that the limit in Eq. (9.1) is finite and nonzero. The scaling begins by choosing $\pmb { \mathrm { x } }$ to be a unit vector $\mathbf { x } ^ { ( 0 ) }$ relative to $\sharp \cdot \lVert _ { \infty }$ and choosing a component $\boldsymbol { x } _ { p _ { 0 } } ^ { ( 0 ) }$ of $\mathbf { x } ^ { ( 0 ) }$ with

$$
x _ { p _ { 0 } } ^ { ( 0 ) } = 1 = \| \mathbf { x } ^ { ( 0 ) } \| _ { \infty } .
$$

Let $\mathbf { y } ^ { ( 1 ) } = A \mathbf { x } ^ { ( 0 ) }$ , and define $\mu ^ { ( 1 ) } = y _ { p _ { 0 } } ^ { ( 1 ) }$ . Then

$$
) = y _ { p _ { 0 } } ^ { ( 1 ) } = \frac { y _ { p _ { 0 } } ^ { ( 1 ) } } { x _ { p _ { 0 } } ^ { ( 0 ) } } = \frac { \beta _ { 1 } \lambda _ { 1 } \nu _ { p _ { 0 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } \lambda _ { j } \nu _ { p _ { 0 } } ^ { ( j ) } } { \beta _ { 1 } \nu _ { p _ { 0 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } \nu _ { p _ { 0 } } ^ { ( j ) } } = \lambda _ { 1 } \left[ \frac { \beta _ { 1 } \nu _ { p _ { 0 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } ( \lambda _ { j } / \lambda _ { 1 } ) v _ { p _ { 0 } } ^ { ( j ) } } { \beta _ { 1 } \nu _ { p _ { 0 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } \nu _ { p _ { 0 } } ^ { ( j ) } } \right]
$$

Let $p _ { \mathrm { { I } } }$ be the least integer such that

$$
| y _ { p _ { 1 } } ^ { ( 1 ) } | = \| \mathbf { y } ^ { ( 1 ) } \| _ { \infty } ,
$$

and define $\mathbf { x } ^ { ( 1 ) }$ by

$$
\mathbf { x } ^ { ( 1 ) } = \frac { 1 } { y _ { p _ { 1 } } ^ { ( 1 ) } } \mathbf { y } ^ { ( 1 ) } = \frac { 1 } { y _ { p _ { 1 } } ^ { ( 1 ) } } A \mathbf { x } ^ { ( 0 ) } .
$$

Then

$$
x _ { p _ { 1 } } ^ { ( 1 ) } = 1 = \| \mathbf { x } ^ { ( 1 ) } \| _ { \infty } .
$$

Now define

$$
\mathbf { y } ^ { ( 2 ) } = A \mathbf { x } ^ { ( 1 ) } = \frac { 1 } { y _ { p _ { 1 } } ^ { ( 1 ) } } A ^ { 2 } \mathbf { x } ^ { ( 0 ) }
$$

and

$$
\begin{array} { c } { { \mu ^ { ( 2 ) } = y _ { p _ { 1 } } ^ { ( 2 ) } = \displaystyle \frac { y _ { p _ { 1 } } ^ { ( 2 ) } } { x _ { p _ { 1 } } ^ { ( 1 ) } } = \displaystyle \frac { \left[ \beta _ { 1 } \lambda _ { 1 } ^ { 2 } v _ { p _ { 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } \lambda _ { j } ^ { 2 } v _ { p _ { 1 } } ^ { ( j ) } \right] \Bigg / y _ { p _ { 1 } } ^ { ( 1 ) } } { \left[ \beta _ { 1 } \lambda _ { 1 } v _ { p _ { 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } \lambda _ { j } v _ { p _ { 1 } } ^ { ( j ) } \right] \Bigg / y _ { p _ { 1 } } ^ { ( 1 ) } } } } \\ { { = \lambda _ { 1 } \left[ \displaystyle \frac { \beta _ { 1 } v _ { p _ { 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } ( \lambda _ { j } / \lambda _ { 1 } ) ^ { 2 } v _ { p _ { 1 } } ^ { ( j ) } } { \beta _ { 1 } v _ { p _ { 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } \beta _ { j } ( \lambda _ { j } / \lambda _ { 1 } ) v _ { p _ { 1 } } ^ { ( j ) } } \right] . } } \end{array}
$$

Let $p _ { 2 }$ be the smallest integer with

$$
| y _ { p _ { 2 } } ^ { ( 2 ) } | = \| \mathbf { y } ^ { ( 2 ) } \| _ { \infty } ,
$$

and define

$$
\mathbf { x } ^ { ( 2 ) } = \frac { 1 } { y _ { p _ { 2 } } ^ { ( 2 ) } } \mathbf { y } ^ { ( 2 ) } = \frac { 1 } { y _ { p _ { 2 } } ^ { ( 2 ) } } A \mathbf { x } ^ { ( 1 ) } = \frac { 1 } { y _ { p _ { 2 } } ^ { ( 2 ) } y _ { p _ { 1 } } ^ { ( 1 ) } } A ^ { 2 } \mathbf { x } ^ { ( 0 ) } .
$$

Inasiilafieseqesofto $\{ \mathbf { x } ^ { ( m ) } \} _ { m = 0 } ^ { \infty }$ and $\{ \mathbf { y } ^ { ( m ) } \} _ { m = 1 } ^ { \infty }$ , and a sequence of scalars $\{ \mu ^ { ( m ) } \} _ { m = 1 } ^ { \infty }$ inductively by

$$
\mathbf { y } ^ { ( m ) } = A \mathbf { x } ^ { ( m - 1 ) } ,
$$

$$
\mu ^ { ( m ) } = y _ { p _ { m - 1 } } ^ { ( m ) } = \lambda _ { 1 } \left[ \frac { \beta _ { 1 } v _ { p _ { m - 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } ( \lambda _ { j } / \lambda _ { 1 } ) ^ { m } \beta _ { j } v _ { p _ { m - 1 } } ^ { ( j ) } } { \beta _ { 1 } v _ { p _ { m - 1 } } ^ { ( 1 ) } + \sum _ { j = 2 } ^ { n } ( \lambda _ { j } / \lambda _ { 1 } ) ^ { m - 1 } \beta _ { j } v _ { p _ { m - 1 } } ^ { ( j ) } } \right] ,
$$

and

$$
\mathbf { x } ^ { ( m ) } = \frac { \mathbf { y } ^ { ( m ) } } { y _ { p _ { m } } ^ { ( m ) } } = \frac { A ^ { m } \mathbf { x } ^ { ( 0 ) } } { \displaystyle \prod _ { k = 1 } ^ { m } y _ { p _ { k } } ^ { ( k ) } } ,
$$

where at each step, $p _ { m }$ is used to represent the smallest integer for which

$$
\begin{array} { r } { | \boldsymbol { y } _ { p _ { m } } ^ { ( m ) } | = \| \boldsymbol { \mathbf { y } } ^ { ( m ) } \| _ { \infty } . } \end{array}
$$

By examining Eq. (9.2), we see that since $| \lambda _ { j } / \lambda _ { 1 } | < 1$ ,for each $j = 2 , 3 , \dots , n .$ $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } \mu ^ { ( m ) } = \lambda _ { 1 } } \end{array}$ , provided that $\mathbf { x } ^ { ( 0 ) }$ is chosen so that $\beta _ { 1 } \neq 0$ . Moreover, the sequence of vectors $\{ \mathbf { x } ^ { ( m ) } \} _ { m = 0 } ^ { \infty }$ convergestoaveoedwit $\lambda _ { 1 }$ that has ${ l } _ { \infty }$ norm one.

The Power method has the disadvantage that it is unknown at the outset whether or not the matrix has a single dominant eigenvalue.Nor is it known how $\mathbf { x } ^ { ( 0 ) }$ should be chosen so as to ensure that its representation in terms of the eigenvectors of the matrix will contain a nonzero contribution from the eigenvector associated with the dominant eigenvalue,should it exist.

Algorithm 9.1 implements the Power method.

# Power Method

To approximate the dominant eigenvalue and an associated eigenvector of the $n \times n$ matrix $A$ given a nonzero vector x:

INPUT dimension $\pmb { n }$ ; matrix $A$ ； vector $\mathbf { x }$ ； tolerance TOL; maximum number of itera-tions $N$

OUTPUTapproximate eigenvalue $\mu$ ; approximate eigenvector $\mathbf { x }$ (with $| | \mathbf { x } | | _ { \infty } = 1$ ora message that the maximum number of iterations was exceeded.

Step 1 Set $k = 1$   
Step 2 Find the smallest integer $p$ with $1 \leq p \leq n$ and $| x _ { p } | = | | \mathbf { x } | | _ { \infty }$ Step 3 Set $\mathbf { x } = \mathbf { x } / x _ { p }$   
Step 4 While $( k \leq N )$ do Steps 5-11.

Step 5 Set $\mathbf { y } = \pmb { A } \mathbf { x }$

Step 6 Set $\mu = y _ { p }$

Step 7 Find the smallest integer $p$ with $1 \leq p \leq n$ and $| y _ { p } | = \| \mathbf { y } \| _ { \infty }$

Step 8If $y _ { p } = 0$ then OUTPUT ('Eigenvector', x); OUTPUT ( $^ { \circ } A$ has the eigenvalue O, select a new vector $\mathbf { x }$ and restart'); STOP.

Step 9 Set $E R R = \{ | \mathbf { x } - ( \mathbf { y } / y _ { p } ) | | _ { \infty } ;$

$$
\mathbf { x } = \mathbf { y } / y _ { p } .
$$

Step 10 If $E R R < T O L$ then OUTPUT $( { \boldsymbol { \mu } } , { \bf x } )$ ；

Step 11 Set $k = k + 1$

Step 12 OUTPUT('The maximum number of iterations exceeded); (The procedure was unsuccessful.) STOP.

Chosi $p _ { m }$ for which $| y _ { p _ { m } } ^ { ( m ) } | = \| \mathbf { y } ^ { ( m ) } \| _ { \infty }$ will gen-erally ensure that this index eventually becomes invariant. The rate at which $\{ \mu ^ { ( m ) } \} _ { m = 1 } ^ { \infty }$ converges to $\lambda _ { 1 }$ is determined by the ratios $| \lambda _ { j } / \lambda _ { 1 } | ^ { m }$ ,for $j = 2 , 3 , \dots , n$ ,and in particular by $| \lambda _ { 2 } / \lambda _ { 1 } | ^ { m }$ . The rate of convergence is $O ( | \lambda _ { 2 } / \lambda _ { 1 } | ^ { m } )$ (see [IK,p.148]), so there is a constant $k$ such that for large $\pmb { m }$ ，

$$
| \mu ^ { ( m ) } - \lambda _ { 1 } | \approx k \left| \frac { \lambda _ { 2 } } { \lambda _ { 1 } } \right| ^ { m } ,
$$

which implies that

$$
\operatorname* { l i m } _ { m \to \infty } \frac { | \mu ^ { ( m + 1 ) } - \lambda _ { 1 } | } { | \mu ^ { ( m ) } - \lambda _ { 1 } | } \approx \left| \frac { \lambda _ { 2 } } { \lambda _ { 1 } } \right| < 1 .
$$

Hence, the sequence $\{ \mu ^ { ( m ) } \}$ converges linearly to $\lambda _ { 1 }$ , and Aitken's $\Delta ^ { 2 }$ procedure discussed in Section 2.5 can be used to speed the convergence. Implementing the $\Delta ^ { 2 }$ procedure in Algorithm 9.1 is accomplished by modifying the algorithm as follows:

Step 1 Set $\begin{array} { c } { { ; k = 1 ; } } \\ { { \mu _ { 0 } = 0 ; } } \\ { { \mu _ { 1 } = 0 . } } \end{array}$

Step 6 Set $\mu = y _ { p }$ ；

$$
\hat { \mu } = \mu _ { 0 } - \frac { ( \mu _ { 1 } - \mu _ { 0 } ) ^ { 2 } } { \mu - 2 \mu _ { 1 } + \mu _ { 0 } } .
$$

Step 10 If $E R R < T O L$ and $k \geq 4$ then OUTPUT $( \hat { \mu } , \mathbf { x } )$ ；STOP.

Step 11 Set ；

$$
\begin{array} { c } { { ; k = k + 1 } } \\ { { \mu _ { 0 } = \mu _ { 1 } ; } } \\ { { \mu _ { 1 } = \mu . } } \end{array}
$$

In actuality,it is not necessary for the matrix to have distinct eigenvalues for the Power method to converge. If the matrix has a unique dominant eigenvalue, $\lambda _ { 1 }$ , with multiplicity $r$ greater than 1 and $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( r ) }$ are linearly independent eigenvectors asociated with $\lambda _ { 1 }$ ,theproceueil $\lambda _ { 1 }$ . The sequence of vectors $\{ \mathbf { x } ^ { ( m ) } \} _ { m = 0 } ^ { \infty }$ will,i his case,converge to an eigenvector of $\lambda _ { 1 }$ of $l _ { \infty }$ norm one that depends on the choice of the initial vector $\mathbf { x } ^ { ( 0 ) }$ and is a linear combination of $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( r ) }$

# EXAMPlE 1

The matrix

$$
\begin{array} { r } { A = \left[ \begin{array} { c c c } { - 4 } & { 1 4 } & { 0 } \\ { - 5 } & { 1 3 } & { 0 } \\ { - 1 } & { 0 } & { 2 } \end{array} \right] } \end{array}
$$

has eigenvalues $\lambda _ { 1 } = 6$ ， $\lambda _ { 2 } = 3$ ,and $\lambda _ { 3 } = 2$ , so the Power method described in Algorithm 9.1 will converge. Let $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { \mathtt { t } }$ , then

$$
\mathbf { y } ^ { ( 1 ) } = A \mathbf { x } ^ { ( 0 ) } = ( 1 0 , 8 , 1 ) ^ { t } ,
$$

So

$$
| | \mathbf { y } ^ { ( \mathrm { I } ) } | | _ { \infty } = 1 0 , \quad \mu ^ { ( \mathrm { I } ) } = y _ { 1 } ^ { ( \mathrm { 1 } ) } = 1 0 , \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( \mathrm { 1 } ) } = \frac { \mathbf { y } ^ { ( \mathrm { 1 } ) } } { 1 0 } = ( 1 , 0 . 8 , 0 . 1 ) ^ { t } .
$$

Continuing in this manner leads to the values in Table 9.1，where $\hat { \mu } ^ { ( m ) }$ represents the sequence generated by the Aitken's $\Delta ^ { 2 }$ procedure. An approximation to the domi-nant eigenvalue,6,at this stage is $\hat { \mu } ^ { ( 1 0 ) } = 6 . 0 0 0 0 0 0$ with approximate unit eigenvector $( 1 , 0 . 7 1 4 3 1 6 , - 0 . 2 4 9 8 9 5 ) ^ { t }$ . Although the approximation to the eigenvalue is correct to the

# Table 9.1

<table><tr><td>m</td><td>X</td><td>从(m)</td><td>(m)</td></tr><tr><td>0</td><td colspan="3">(1, 1,1)</td></tr><tr><td>1</td><td>(1,0.8, 0.1)</td><td>10</td><td>6.266667</td></tr><tr><td>2</td><td>(1, 0.75, -0.111)</td><td>7.2</td><td>6.062473</td></tr><tr><td>3</td><td>(1,0.730769, -0.188803)</td><td>6.5</td><td>6.015054</td></tr><tr><td>4</td><td>(1,0.722200,-0.220850)</td><td>6.230769</td><td>6.004202</td></tr><tr><td>5</td><td>(1,0.718182,-0.235915)</td><td>6.111000</td><td>6.000855</td></tr><tr><td>6</td><td>(1,0.716216, -0.243095)</td><td>6.054546</td><td>6.000240</td></tr><tr><td>7</td><td>(1, 0.715247, -0.246588)</td><td>6.027027</td><td>6.000058</td></tr><tr><td>8</td><td>(1, 0.714765,-0.248306)</td><td>6.013453</td><td>6.000017</td></tr><tr><td>9</td><td>(1,0.714525, -0.249157)</td><td>6.006711</td><td>6.000003</td></tr><tr><td>10</td><td>(1,0.714405, -0.249579)</td><td>6.003352</td><td>6.000000</td></tr><tr><td>11</td><td>(1, 0.714346, -0.249790)</td><td>6.001675</td><td></td></tr><tr><td>12</td><td>(1,0.714316,-0.249895)</td><td>6.000837</td><td></td></tr></table>

places listed, the eigenvector approximation is considerably less accurate to the true eigenvector, $( 1 , 0 . 7 1 4 2 8 6 , - 0 . 2 5 ) ^ { t }$

When $A$ is symmetric,a variation in the choice of the vectors $\mathbf { X } ^ { ( m ) } , \mathbf { y } ^ { ( m ) }$ , and scalars $\mu ^ { ( m ) }$ can bemade tosignficantlyimprove therateof convergence ofthesequence $\{ \mu ^ { ( m ) } \} _ { m = 1 } ^ { \infty }$ ro thedominant igenvalue $\lambda _ { 1 }$ the general Power method is $O ( | \lambda _ { 2 } / \lambda _ { 1 } | ^ { m } )$ , the rate of convergence of the modified pro-cedure given in Algorithm 9.2 for symmetric matrices is $O ( | \lambda _ { 2 } / \lambda _ { 1 } | ^ { 2 m } )$ .(See [IK, pp.149 ff].） Because the sequence $\{ \mu ^ { ( m ) } \}$ is still linearly convergent,Aitken's $\Delta ^ { 2 }$ procedure can be applied.

# Symmetric Power Method

To approximate the dominant eigenvalue and an associated eigenvector of the $n \times n$ symmetric matrix $A$ ， given a nonzero vector $\mathbf { x }$ ：

INPUTdimension $_ { n }$ ; matrix $A$ ; vector x; tolerance TOL; maximum number of itera· tions $N$

OUTPUTapproximate eigenvalue $\mu$ ; approximate eigenvector $\mathbf { x }$ (with $\| \mathbf { x } \| _ { 2 } = \mathbb { I } .$ ora message that the maximum number of iterations was exceeded.

Step1 Set $\begin{array} { r } { \mathbf { \xi } ^ { ; k = 1 ; } \mathbf { \xi } } \\ { \mathbf { x } = \mathbf { x } / \| \mathbf { x } \| _ { 2 } . } \end{array}$

Step 2 While $( k \leq N )$ do Steps 3-8.

Step 3Set $\mathbf { y } = A \mathbf { x }$

Step 4 Set ${ \boldsymbol { \mu } } = \mathbf { x } ^ { t } \mathbf { y }$

Step 5If $\| \mathbf { y } \| _ { 2 } = 0$ , then OUTPUT(‘Eigenvector', x); OUTPUT( $^ { \circ } A$ has eigenvalue O, select new vector x and restart');

STOP.

Step6 Set $E R R = \left. \mathbf { x } - { \frac { \mathbf { y } } { \Vert \mathbf { y } \Vert _ { 2 } } } \right. _ { 2 } ;$

$$
\mathbf { x } = \mathbf { y } / \| \mathbf { y } \| _ { 2 } .
$$

Step 7If $E R R < T O L$ then OUTPUT $( { \boldsymbol { \mu } } , \mathbf { x } )$ ；

Step 8 Set $k = k + 1$

Step 9OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

# EXAMPLE 2 The matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { - 1 } & { 1 } \\ { - 1 } & { 3 } & { - 2 } \\ { 1 } & { - 2 } & { 3 } \end{array} } \right]
$$

is symmetric with eigenvalues $\lambda _ { 1 } = 6 , \lambda _ { 2 } = 3$ ，and $\lambda _ { 3 } = 1$ . Table 9.2 lists the results the Power method,and the results in Table 9.3 come from the Symmetric Power method, assuming in each case that $\mathbf { y } ^ { ( 0 ) } \ = \ \mathbf { x } ^ { ( 0 ) } \ = \ ( 1 , 0 , 0 ) ^ { t }$ . Notice the significant improvement that the Symmetric Power method provides. The approximations to the eigenvectors produced in the Power method converge to $( 1 , - 1 , 1 ) ^ { t }$ ，a vector with $\| ( 1 , - 1 , 1 ) ^ { t } \| _ { \infty } = 1$ . In the Symmetric Power method, the convergence is to the parallel vector $( { \sqrt { 3 } } / 3 , - { \sqrt { 3 } } / 3 , { \sqrt { 3 } } / 3 ) ^ { t }$ ,with $\| ( \sqrt { 3 } / 3 , - \sqrt { 3 } / 3 , \sqrt { 3 } / 3 ) ^ { t } \| _ { 2 } = 1$ □

Table 9.2   

<table><tr><td>m</td><td>(y(m)</td><td>从（m）</td><td>n（m)</td><td>（x(m）‘ with |x(m）|=1</td></tr><tr><td>0</td><td></td><td></td><td></td><td>(1,0,0)</td></tr><tr><td>1</td><td>(4,-1,1)</td><td>4</td><td></td><td>(1,-0.25,0.25)</td></tr><tr><td>2</td><td>(4.5,-2.25,2.25)</td><td>4.5</td><td>7</td><td>(1, -0.5,0.5)</td></tr><tr><td>3</td><td>(5,-3.5,3.5)</td><td>5</td><td>6.2</td><td>(1, -0.7, 0.7)</td></tr><tr><td>4</td><td>(5.4,-4.5,4.5)</td><td>5.4</td><td>6.047617</td><td>(1,-0.8333,0.8333)</td></tr><tr><td>5</td><td>(5.666,-5.1666,5.1666)</td><td>5.666</td><td>6.011767</td><td>(1,-0.911765, 0.911765)</td></tr><tr><td>6</td><td>(5.823529, -5.558824, 5.558824)</td><td>5.823529</td><td>6.002931</td><td>(1, -0.954545, 0.954545)</td></tr><tr><td>7</td><td>(5.909091, -5.772727, 5.772727)</td><td>5.909091</td><td>6.000733</td><td>(1,-0.976923,0.976923)</td></tr><tr><td>8</td><td>(5.953846, -5.884615, 5.884615)</td><td>5.953846</td><td>6.000184</td><td>(1,-0.988372,0.988372)</td></tr><tr><td>9</td><td>(5.976744, -5.941861, 5.941861)</td><td>5.976744</td><td></td><td>(1,-0.994163,0.994163)</td></tr><tr><td>10</td><td>(5.988327, -5.970817, 5.970817)</td><td>5.988327</td><td></td><td>(1,-0.997076,0.997076)</td></tr></table>

Table 9.3   

<table><tr><td>m</td><td></td><td>(y(m)</td><td>u(m)</td><td>p(m）</td><td>（x(m）‘ with |x(m）|12=1</td></tr><tr><td>0</td><td>(1,0,0)</td><td></td><td></td><td></td><td>(1,0,0)</td></tr><tr><td>1</td><td>(4,-1,1)</td><td></td><td>4</td><td>7</td><td>(0.942809,-0.235702, 0.235702)</td></tr><tr><td>2</td><td></td><td>(4.242641,-2.121320,2.121320</td><td>5</td><td>6.047619</td><td>(0.816497, -0.408248, 0.408248)</td></tr><tr><td>3</td><td></td><td>(4.082483, --2.857738, 2.857738)</td><td>5.666667</td><td>6.002932</td><td>(0.710669, -0.497468, 0.497468)</td></tr><tr><td>4</td><td></td><td>(3.837613, -3.198011, 3.198011)</td><td>5.909091</td><td>6.000183</td><td>(0.646997, -0.539164, 0.539164)</td></tr><tr><td>5</td><td></td><td>(3.666314, -3.342816, 3.342816)</td><td>5.976744</td><td>6.000012</td><td>(0.612836, --0.558763, 0.558763)</td></tr><tr><td>6</td><td></td><td>(3.568871, -3.406650, 3.406650)</td><td>5.994152</td><td>6.000000</td><td>(0.595247, -0.568190, 0.568190)</td></tr><tr><td>7</td><td></td><td>(3.517370, -3.436200,3.436200)</td><td>5.998536</td><td>6.000000</td><td>(0.586336, -0.572805,0.572805)</td></tr><tr><td>8</td><td></td><td>(3.490952, -3.450359, 3.450359)</td><td>5.999634</td><td></td><td>(0.581852, -0.575086, 0.575086)</td></tr><tr><td>9</td><td></td><td>(3.477580, -3.457283, 3.457283)</td><td>5.999908</td><td></td><td>(0.579603, -0.576220, 0.576220)</td></tr><tr><td>10</td><td></td><td>(3.470854, -3.460706, 3.460706)</td><td>5.999977</td><td></td><td>(0.578477, -0.576786, 0.576786)</td></tr></table>

The following gives an error bound for approximating the eigenvalues of a symmetric matrix.

$A$ is an $n \times n$ symmetric matrix with eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ and $\| A \mathbf { x } - \lambda \mathbf { x } \| _ { 2 } < \varepsilon$ for some real number $\lambda$ and vector $\mathbf { x }$ with $\| \mathbf { x } \| _ { 2 } = 1$ ,then

$$
\operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } - \lambda | < \varepsilon .
$$

Proof Suppose that $\mathbf { v } ^ { ( 1 ) }$ ， $\mathbf { v } ^ { ( 2 ) }$ ，..， $\mathbf { v } ^ { ( n ) }$ form an orthonormal set of eigenvectors of $A$ associated,respectively, with the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ . By Theorems 9.5 and 9.2, $\mathbf { x }$ can be expressed, for some unique set of constants $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$ ,as

$$
\mathbf { x } = \sum _ { j = 1 } ^ { n } \beta _ { j } \mathbf { v } ^ { ( j ) } .
$$

Thus,

$$
\| A \mathbf { x } - \lambda \mathbf { x } \| _ { 2 } ^ { 2 } = \left\| \sum _ { j = 1 } ^ { n } \beta _ { j } ( \lambda _ { j } - \lambda ) \mathbf { v } ^ { ( j ) } \right\| _ { 2 } ^ { 2 } = \sum _ { j = 1 } ^ { n } | \beta _ { j } | ^ { 2 } | \lambda _ { j } - \lambda | ^ { 2 } \geq \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } - \lambda | ^ { 2 } \sum _ { j = 1 } ^ { n } | \beta _ { j } | ^ { 2 } \lambda _ { j } - \lambda | ^ { 2 } .
$$

But

$$
\sum _ { j = 1 } ^ { n } | \beta _ { j } | ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } = 1 ,
$$

so

$$
\varepsilon \geq \| A \mathbf { x } - \lambda \mathbf { x } \| _ { 2 } > \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } - \lambda | .
$$

The Inverse Power method is a modification of the Power method that gives faster convergence. It is used to determine the eigenvalue of $\pmb { A }$ that is closest to a specified number $q$

Suppose the matrix $A$ has eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ with linearly independent eigenvectors $\mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) }$ . The eigenvalues of $( A - q I ) ^ { - 1 }$ ，where $q \ne \lambda _ { i }$ ,for $i = 1 , 2 , \dots , n ,$ are

$$
{ \frac { 1 } { \lambda _ { 1 } - q } } , \quad { \frac { 1 } { \lambda _ { 2 } - q } } , \quad \ldots , \quad { \frac { 1 } { \lambda _ { n } - q } } ,
$$

with eigenvectors $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( n ) }$ (See Exercise 9 of Section 7.2.). Applying the Power method to $( A - q I ) ^ { - 1 }$ gives

$$
\mathbf { y } ^ { ( m ) } = ( A - q I ) ^ { - 1 } \mathbf { x } ^ { ( m - 1 ) } ,
$$

$$
\mu ^ { ( m ) } = y _ { p _ { m - 1 } } ^ { ( m ) } = \frac { y _ { p _ { m - 1 } } ^ { ( m ) } } { x _ { p _ { m - 1 } } ^ { ( m - 1 ) } } = \frac { \sum _ { j = 1 } ^ { n } \beta _ { j } \frac { 1 } { ( \lambda _ { j } - q ) ^ { m } } v _ { p _ { m - 1 } } ^ { ( j ) } } { \sum _ { j = 1 } ^ { n } \beta _ { j } \frac { 1 } { ( \lambda _ { j } - q ) ^ { m - 1 } } v _ { p _ { m - 1 } } ^ { ( j ) } } ,
$$

and

$$
\mathbf { x } ^ { ( m ) } = \frac { \mathbf { y } ^ { ( m ) } } { y _ { p _ { m } } ^ { ( m ) } } ,
$$

where, at each step, $p _ { m }$ represents the smallest integer for which $| y _ { p _ { m } } ^ { ( m ) } | = | | \mathbf { y } ^ { ( m ) } | | _ { \infty }$ . The sequence $\{ \mu ^ { ( m ) } \}$ in Eq. (9.3) converges to $1 / ( \lambda _ { k } - q )$ , where

$$
\frac { 1 } { | \lambda _ { k } - q | } = \operatorname* { m a x } _ { 1 \leq i \leq n } \frac { 1 } { | \lambda _ { i } - q | } ,
$$

and $\lambda _ { k } \approx q + 1 / \mu ^ { ( m ) }$ is the eigenvalue of $A$ closest to $q$

With $k$ known, Eq. (9.3) can be writen as

$$
\mu ^ { ( m ) } = \frac { 1 } { \lambda _ { k } - q } \left[ \frac { \beta _ { k } v _ { p _ { m - 1 } } ^ { ( k ) } + \sum _ { j = 1 } ^ { n } \beta _ { j } \left[ \frac { \lambda _ { k } - q } { \lambda _ { j } - q } \right] ^ { m } v _ { p _ { m - 1 } } ^ { ( j ) } } { \beta _ { k } v _ { p _ { m - 1 } } ^ { ( k ) } + \sum _ { j = 1 } ^ { n } \beta _ { j } \left[ \frac { \lambda _ { k } - q } { \lambda _ { j } - q } \right] ^ { m - 1 } v _ { p _ { m - 1 } } ^ { ( j ) } } \right] .
$$

Thus, the choice of $q$ determines the convergence, provided that $1 / ( \lambda _ { k } - q )$ is a unique ominant eigenvalue of $( A - q I ) ^ { - 1 }$ (although it may be a multiple eigenvalue). The closer $q$ is to an eigenvalue $\lambda _ { k }$ ,the faster the convergence since the convergence is of order

$$
O \left( \left| \frac { ( \lambda - q ) ^ { - 1 } } { ( \lambda _ { k } - q ) ^ { - 1 } } \right| ^ { m } \right) = O \left( \left| \frac { ( \lambda _ { k } - q ) } { ( \lambda - q ) } \right| ^ { m } \right) ,
$$

where $\lambda$ represents the eigenvalue of $A$ that is second closest to $q$

The vector $\mathbf { y } ^ { ( m ) }$ is obtained from the equation

$$
( A - q I ) \mathbf { y } ^ { ( m ) } = \mathbf { x } ^ { ( m - 1 ) } .
$$

In general, Gaussian elimination with pivoting can be used to solve this system.

Although the Inverse Power method requires the solution of an $n \times n$ system at each step,the multipliers can be saved to reduce the computation. The selection of $q$ can be based on the Gerschgorin Circle Theorem or on another means of localizing an eigenvalue.

Algorithm 9.3 computes $q$ from an initial approximation to the eigenvector $\mathbf { x } ^ { ( 0 ) }$ by

$$
\begin{array} { r } { q = \frac { \mathbf { x } ^ { ( 0 ) t } A \mathbf { x } ^ { ( 0 ) } } { \mathbf { x } ^ { ( 0 ) t } \mathbf { x } ^ { ( 0 ) } } . } \end{array}
$$

This choice of $q$ results from the observation that if $\mathbf { x }$ is an eigenvector of $A$ with respect to the eigenvalue $\lambda$ , then $A \mathbf { x } = \lambda \mathbf { x }$ .So $\mathbf { x } ^ { t } A \mathbf { x } = \lambda \mathbf { x } ^ { t } \mathbf { x }$ and

$$
\lambda = \frac { \mathbf { x } ^ { t } A \mathbf { x } } { \mathbf { x } ^ { t } \mathbf { x } } = \frac { \mathbf { x } ^ { t } A \mathbf { x } } { \| \mathbf { x } \| _ { 2 } ^ { 2 } } .
$$

If $q$ is close to an eigenvalue, the convergence willbe quite rapid, but a pivoting technique should be used in Step 6 to avoid contamination by roundoff error.

Algorithm 9.3 is often used to approximate an eigenvector when an approximate eigenvalue $q$ is known.

# Inverse Power Method

To approximate an eigenvalue and an associated eigenvector of the $n \times n$ matrix $A$ given a nonzero vector x:

INPUT dimension $\pmb { n }$ ; matrix $\pmb { A }$ ; vector $\mathbf { x }$ ; tolerance TOL; maximum number of iterations $N$

OUTPUTapproximate eigenvalue $\mu$ ; approximate eigenvector $\mathbf { x }$ (with $\| \mathbf { x } \| _ { \infty } = 1 ,$ ora message that the maximum number of iterations was exceeded.

$$
\zeta t e p \ 1 \quad \mathrm { S e t } q = { \frac { { \bf x } ^ { t } A { \bf x } } { { \bf x } ^ { t } { \bf x } } } .
$$

Step 2 Set $k = 1$

Step 3Find the smalestinteger $p$ with $1 \leq p \leq n$ and $| x _ { p } | = \| \mathbf { x } \| _ { \infty }$

Step 4 Set $\mathbf { x } = \mathbf { x } / x _ { p }$

Step 5While $( k \le N )$ do Steps 6-12.

Step 6Solve the linear system $( A - q I ) \mathbf { y } = \mathbf { x }$

Step 7 If the system does not have a unique solution, then OUTPUT ( $\because q$ is an eigenvalue', $q$ ； STOP.

Step 8 Set $\mu = y _ { p }$

Step 9Find the smallest integer $p$ with $1 \leq p \leq n$ and $| y _ { p } | = \| \mathbf { y } \| _ { \infty }$

Step 10 Set

$$
\begin{array} { c } { E R R = \left\| \mathbf { x } - ( \mathbf { y } / y _ { p } ) \right\| _ { \infty } ; } \\ { \mathbf { x } = \mathbf { y } / y _ { p } . } \end{array}
$$

Step 11 If $E R R < T O L$ then set $\mu = ( 1 / \mu ) + q$ ：

Step 12 Set $k = k + 1$

Step 13OUTPUT (‘Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

Since theconvergence of the Inverse Power method is linear, Aitken $\Delta ^ { 2 }$ procedure can again be used to speed convergence. The following example illstrates the fast convergence of the Inverse Power method if $q$ is close to an eigenvalue.

# EXAMPLE 3 The matrix

$$
A = { \left[ \begin{array} { l l l } { - 4 } & { 1 4 } & { 0 } \\ { - 5 } & { 1 3 } & { 0 } \\ { - 1 } & { 0 } & { 2 } \end{array} \right] }
$$

was considered in Example 1. Algorithm 9.1 gave the approximation $\mu ^ { ( 1 2 ) } = 6 . 0 0 0 8 3 7$ using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ .With $\mathbf { x } ^ { ( 0 ) } = \left( 1 , 1 , 1 \right) ^ { t }$ , we have

$$
q = \frac { { \bf x } ^ { ( 0 ) t } A { \bf x } ^ { ( 0 ) } } { { \bf x } ^ { ( 0 ) t } { \bf x } ^ { ( 0 ) } } = \frac { 1 9 } { 3 } = 6 . 3 3 3 3 3 3 .
$$

The results of applying Algorithm 9.3 are listed in Table 9.4,and the right column lists the results of Aitken's $\Delta ^ { 2 }$ method applied to the $\mu ^ { ( m ) }$ ·

Table 9.4   

<table><tr><td>m</td><td>x(m)</td><td>从(m)</td><td>(m)</td></tr><tr><td>0</td><td>(1, 1, 1)</td><td></td><td></td></tr><tr><td>1</td><td>(1,0.720727, -0.194042)</td><td>6.183183</td><td>6.000116</td></tr><tr><td>2</td><td>(1, 0.715518, -0.245052)</td><td>6.017244</td><td>6.000004</td></tr><tr><td>3</td><td>(1, 0.714409, -0.249522)</td><td>6.001719</td><td>6.000004</td></tr><tr><td>4</td><td>(1, 0.714298,-0.249953)</td><td>6.000175</td><td>6.000003</td></tr><tr><td>5</td><td>(1, 0.714287, -0.250000)</td><td>6.000021</td><td></td></tr><tr><td>6</td><td>(1, 0.714286, -0.249999)</td><td>6.000005</td><td></td></tr></table>

If $A$ is symmetric, then for any real number $q$ ， $( A - q I ) ^ { - 1 }$ is also symmetric, so the Symmetric Power method, Algorithm 9.2,can be applied to $( A - q I ) ^ { - 1 }$ to speed the convergence to

$$
O \left( \left| { \frac { \lambda _ { k } - q } { \lambda - q } } \right| ^ { 2 m } \right) .
$$

Numerous techniques are available for obtaining approximations to the other eigenvalues of a matrix once an approximation to the dominant eigenvalue has been computed. We will restrict our presentation to deflation techniques.

Deflation techniques involve forming a new matrix $B$ whose eigenvalues are the same as those of $A$ , except that the dominant eigenvalue of $\pmb { A }$ is replaced by the eigenvalue O in $B$ . The following result justifies the procedure. The proof of this theorem can be found in [Wil2, p. 596].

# Theorem 9.15

Suppose $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are eigenvalues of $A$ with associated eigenvectors $\mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) }$ ， $\mathbf { v } ^ { ( n ) }$ and that $\lambda _ { 1 }$ has multiplicity 1. Let $\pmb { \mathrm { x } }$ be a vector with $\mathbf { x } ^ { t } \mathbf { v } ^ { ( 1 ) } = 1$ . Then the matrix

$$
B = A - \lambda _ { 1 } \mathbf { v } ^ { ( 1 ) } \mathbf { x } ^ { t }
$$

has eigenvalues $0 , \lambda _ { 2 } , \lambda _ { 3 } , \ldots , \lambda _ { n }$ with associated eigenvectors $\mathbf { v } ^ { ( 1 ) } , \mathbf { w } ^ { ( 2 ) } , \mathbf { w } ^ { ( 3 ) } , \dots , \mathbf { w } ^ { ( n ) }$ ， where $\mathbf { v } ^ { ( i ) }$ and $\mathbf { w } ^ { ( i ) }$ are related by the equation

$$
\mathbf { v } ^ { ( i ) } = ( \lambda _ { i } - \lambda _ { 1 } ) \mathbf { w } ^ { ( i ) } + \lambda _ { 1 } ( \mathbf { x } ^ { t } \mathbf { w } ^ { ( i ) } ) \mathbf { v } ^ { ( 1 ) } ,
$$

for each $i = 2 , 3 , \dots , n$

There are many choices of the vector $\pmb { \mathrm { x } }$ that could be used in Theorem 9.15. Wielandt deflation proceeds from defining

$$
\mathbf { x } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } ( a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } ) ^ { t } ,
$$

where $\boldsymbol { v } _ { i } ^ { ( 1 ) }$ is $\mathbf { v } ^ { ( 1 ) }$ , and the values $a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n }$ are the entries in the ith row of $A$ .

With this definition,

$$
\mathbf { x } ^ { t } \mathbf { v } ^ { ( 1 ) } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } [ a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } ] ( v _ { 1 } ^ { ( 1 ) } , v _ { 2 } ^ { ( 1 ) } , \ldots , v _ { n } ^ { ( 1 ) } ) ^ { t } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } \sum _ { j = 1 } ^ { n } a _ { i j } v _ { j } ^ { ( 1 ) } ,
$$

where the sum is the ith coordinate of the product $\boldsymbol { A } \boldsymbol { \mathbf { v } } ^ { ( 1 ) }$ . Since $A \mathbf { v } ^ { ( 1 ) } = \lambda _ { 1 } \mathbf { v } ^ { ( 1 ) }$ , we have

$$
\sum _ { j = 1 } ^ { n } a _ { i j } \upsilon _ { j } ^ { ( 1 ) } = \lambda _ { 1 } \upsilon _ { i } ^ { ( 1 ) } ,
$$

which implies that

$$
\mathbf { x } ^ { t } \mathbf { v } ^ { ( 1 ) } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } ( \lambda _ { 1 } v _ { i } ^ { ( 1 ) } ) = 1 .
$$

So x satisfies the hypotheses of Theorem 9.15. Moreover (see Exercise 12), the ith row of $B = A - \lambda _ { 1 } \mathbf { v } ^ { ( 1 ) } \mathbf { x } ^ { t }$ consists entirely of zero entries.

If $\lambda \neq 0$ is an eigenvalue with associated eigenvector $\mathbf { w }$ , the relation $B \mathbf { w } = \lambda \mathbf { w }$ implies that the ith coordinate of w must also be zero. Consequently the ith column of the matrix $B$ makes no contribution to the product $B \mathbf { w } = \lambda \mathbf { w }$ .Thus, the matrix $B$ can be replaced by an $( n \mathrm { ~ - ~ } 1 ) \times ( n \mathrm { ~ - ~ } 1 )$ matrix $B ^ { \prime }$ obtained by deleting the ith row and column from $B$ . The matrix $B ^ { \prime }$ has eigenvalues $\lambda _ { 2 } , \lambda _ { 3 } , \ldots , \lambda _ { n }$ .If $| \lambda _ { 2 } | > | \lambda _ { 3 } |$ ，the Power method is reapplied to the matrix $B ^ { \prime }$ to determine this new dominant eigenvalue and an eigenvector, $\mathbf { w } ^ { ( 2 ) ^ { \prime } }$ , associated with $\lambda _ { 2 }$ , with respect to the matrix $B ^ { \prime }$ . To find the associated eigenvector $\mathbf { w } ^ { ( 2 ) }$ for the matrix $B$ , insert a zero coordinate between the coordinates ${ w _ { i - 1 } ^ { ( 2 ) ^ { \prime } } }$ and $w _ { i } ^ { ( 2 ) ^ { \prime } }$ of the $( n - 1 )$ -dimensional vector $\mathbf { w } ^ { ( 2 ) ^ { \prime } }$ and then calculate $\mathbf { v } ^ { ( 2 ) }$ by the use of Eq. (9.5).

EXAMPLE 4 From Example 2, we know that the matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { - 1 } & { 1 } \\ { - 1 } & { 3 } & { - 2 } \\ { 1 } & { - 2 } & { 3 } \end{array} } \right]
$$

has eigenvalues $\lambda _ { 1 } = 6 , \lambda _ { 2 } = 3$ ,and $\lambda _ { 3 } = 1$ . Assuming that the dominant eigenvalue $\lambda _ { 1 } =$ 6 and associated unit eigenvector $\mathbf { v } ^ { ( 1 ) } = ( 1 , - 1 , 1 ) ^ { t }$ have been calculated, the procedure just outlined for obtaining $\lambda _ { 2 }$ proceeds as follows:

$$
\mathbf { x } = { \frac { 1 } { 6 } } { \left[ { \begin{array} { l } { \quad 4 } \\ { - 1 } \\ { \quad 1 } \end{array} } \right] } = \left( { \frac { 2 } { 3 } } , - { \frac { 1 } { 6 } } , { \frac { 1 } { 6 } } \right) ^ { t } ,
$$

$$
\mathbf { v } ^ { ( 1 ) } \mathbf { x } ^ { t } = \left[ { \begin{array} { r } { 1 } \\ { - 1 } \\ { 1 } \end{array} } \right] \left[ { \begin{array} { r r r r } { { \frac { 2 } { 3 } } , } & { - { \frac { 1 } { 6 } } , } & { { \frac { 1 } { 6 } } } \end{array} } \right] = \left[ { \begin{array} { r r r r } { { \frac { 2 } { 3 } } } & { - { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } \\ { - { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { - { \frac { 1 } { 6 } } } \\ { { \frac { 2 } { 3 } } } & { - { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } \end{array} } \right] ,
$$

and

$$
\begin{array} { r l } & { B = A - \lambda _ { 1 } \mathbf { v } ^ { ( 1 ) } \mathbf { x } ^ { t } = \left[ \begin{array} { r r r } { 4 } & { - 1 } & { 1 } \\ { - 1 } & { 3 } & { - 2 } \\ { 1 } & { - 2 } & { 3 } \end{array} \right] - 6 \left[ \begin{array} { r r r } { \frac { 2 } { 3 } } & { - \frac { 1 } { 6 } } & { \frac { 1 } { 6 } } \\ { - \frac { 2 } { 3 } } & { \frac { 1 } { 6 } } & { - \frac { 1 } { 6 } } \\ { \frac { 2 } { 3 } } & { - \frac { 1 } { 6 } } & { \frac { 1 } { 6 } } \end{array} \right] } \\ & { \quad \quad \quad = \left[ \begin{array} { r r r } { 0 } & { 0 } & { 0 } \\ { 3 } & { 2 } & { - 1 } \\ { - 3 } & { - 1 } & { 2 } \end{array} \right] . } \end{array}
$$

Deleting the first row and column gives

$$
B ^ { \prime } = \left[ { \begin{array} { r r } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} } \right] ,
$$

which has eigenvalues $\lambda _ { 2 } = 3$ and $\lambda _ { 3 } = 1$ .For $\lambda _ { 2 } = 3$ ， the eigenvector $\mathbf { w } ^ { ( 2 ) ^ { \prime } }$ can be obtained by solving the linear system

$$
( B ^ { \prime } - 3 I ) { \bf w } ^ { ( 2 ) ^ { \prime } } = { \bf 0 } ,
$$

resulting in

$$
\begin{array} { r } { \mathbf { w } ^ { ( 2 ) ^ { \prime } } = ( 1 , - 1 ) ^ { t } . } \end{array}
$$

Adding a zero for the first component gives $\mathbf { w } ^ { ( 2 ) } = ( 0 , 1 , - 1 ) ^ { t }$ and, from Eq. (9.5), we have the eigenvector ${ \bf v } ^ { ( 2 ) }$ of $\pmb { A }$ corresponding to $x _ { 2 } = 3$ ：

$$
{ \bf \mathrm {  ~ \Lambda ~ } } ^ { ( 2 ) } = ( 3 - 6 ) ( 0 , 1 , - 1 ) ^ { t } + 6 \left[ \left( \frac { 2 } { 3 } , - \frac { 1 } { 6 } , \frac { 1 } { 6 } \right) ( 0 , 1 , - 1 ) ^ { t } \right] ( 1 , - 1 , 1 ) ^ { t } = ( - 2 , - 1 , 1 ) ^ { t } .
$$

Although this deflation process can be used to find approximations to all of the eigenvalues and eigenvectors of a matrix, the process is susceptible to roundoff error. After deflation is used to approximate an eigenvalue of a matrix,the approximation should be used as a starting value for the Inverse Power method applied to the original matrix. This will ensure convergence to an eigenvalue of the original matrix, not to one of the reduced matrix,which likely contains errors.When all the eigenvalues of a matrix are required, techniques considered in Section 9.4,based on similarity transformations,should be used.

We close this section with Algorithm 9.4,which calculates the second most dominant eigenvalue and associated eigenvector for a matrix,once the dominant eigenvalue and associated eigenvector have been determined.

# Wielandt Deflation

To approximate the second most dominant eigenvalue and an associated eigenvector of the $n \times n$ matrix $\pmb { A }$ given an approximation $\lambda$ to the dominant eigenvalue, an approximation v to a corresponding eigenvector, and a vector $\mathbf { x } \in \mathbb { R } ^ { n - 1 }$ ：

INPUT dimension $\pmb { n }$ ; matrix $A$ ； approximate eigenvalue $\lambda$ with eigenvector $\textbf { v } \in \mathbb { R } ^ { n }$ ； vector $\mathbf { x } \in \mathbb { R } ^ { n - 1 }$ , tolerance $T O L ,$ maximum number of iterations $N$

OUTPUT.approximate eigenvalue $\mu$ ; approximate eigenvector u or a message that the method fails.

Step 1 Let i be the smallest integer with $1 \leq i \leq n$ and $\lvert \boldsymbol { \nu } _ { i } \rvert = \operatorname* { m a x } _ { 1 \leq j \leq n } \lvert \boldsymbol { \nu } _ { j } \rvert$

Step 2 If $i \neq 1$ then for $k = 1 , \dots , i - 1$ $\mathrm { f o r } \ j = 1 , \dots , i - 1$ $\sec b _ { k j } = a _ { k j } - { \frac { \upsilon _ { k } } { \upsilon _ { i } } } a _ { i j } .$

Step 3If $i \neq 1$ and $i \neq n$ thenfor $k = i , \ldots , n - 1$ $\operatorname { f o r } j = 1 , \dots , i - 1$ $\begin{array} { r } { \mathrm { s e t } b _ { k j } = a _ { k + 1 , j } - \frac { v _ { k + 1 } } { v _ { i } } a _ { i j } ; } \\ { b _ { j k } = a _ { j , k + 1 } - \frac { v _ { j } } { v _ { i } } a _ { i , k + 1 } . } \end{array}$

Step 4 If $i \neq n$ then for $k = i , \ldots , n - 1$ fo ${ \mathfrak { r } } j = i , \dotsc , n - 1$

$$
\mathrm { s e t } b _ { k j } = a _ { k + 1 , j + 1 } - \frac { \upsilon _ { k + 1 } } { \upsilon _ { i } } a _ { i , j + 1 } .
$$

Step 5 Perform the power method on the $( n - 1 ) \times ( n - 1 )$ matrix $B ^ { \prime } = ( b _ { k j } )$ with $\mathbf { x }$ as initial approximation.

Step 6If the method fails, then OUTPUT(‘Method fails'); STOP else let $\mu$ be the approximate eigenvalue and $\mathbf { w ^ { \prime } } = ( w _ { 1 } ^ { \prime } , \ldots , w _ { n - 1 } ^ { \prime } ) ^ { t }$ the approximate eigenvector.

Step 7 If $i \neq 1$ then for $k = 1 , \dots , i - 1$ set $w _ { k } = w _ { k } ^ { \prime }$

Step8 Set $w _ { i } = 0$

Step 9 If $i \neq n$ then for $k = i + 1 , \ldots , n \operatorname { s e t } w _ { k } = w _ { k - 1 } ^ { \prime }$

Step 10 For $k = 1 , \ldots , n$

$$
\sec u _ { k } = ( \mu - \lambda ) w _ { k } + \left( \sum _ { j = 1 } ^ { n } a _ { i j } w _ { j } \right) { \frac { v _ { k } } { v _ { i } } } .
$$

(Compute the eigenvector using $E q$ .(9.5).)

Step 11 OUTPUT $( \mu , { \bf u } )$ ; (The procedure was successful.) STOP.

# ExErcise Set 9.2

1.Find the first three iterations obtained by the Power method applied to the following matrices.

$\begin{array} { r l } { \mathbf { a } , } & { { } \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] ; } \end{array}$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( \mathbf { i } , - 1 , 2 ) ^ { t } .$ $\mathbf { b } , \quad { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \end{array} \right] } ;$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( - 1 , 0 , 1 ) ^ { t }$ $\begin{array} { r l } { \mathrm { c } . } & { { } \left[ \begin{array} { c c c } { 1 } & { - 1 } & { 0 } \\ { - 2 } & { 4 } & { - 2 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right] ; } \end{array}$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( - 1 , 2 , 1 ) ^ { t } .$

d. ${ \left[ \begin{array} { l l l l } { 4 } & { } & { 1 } & { } & { 1 } \\ { 1 } & { } & { 3 } & { - 1 } & { 1 } \\ { 1 } & { - 1 } & { } & { 2 } & { 0 } \\ { 1 } & { } & { 1 } & { } & { 0 } & { 2 } \end{array} \right] } ;$ Use $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 2 , 0 , 3 ) ^ { t }$

$a . \quad \left[ { \begin{array} { r r r r } { 5 } & { - 2 } & { - { \frac { 1 } { 2 } } } & { { \frac { 3 } { 2 } } } \\ { - 2 } & { 5 } & { { \frac { 3 } { 2 } } } & { - { \frac { 1 } { 2 } } } \\ { - { \frac { 1 } { 2 } } } & { { \frac { 3 } { 2 } } } & { 5 } & { - 2 } \\ { { \frac { 3 } { 2 } } } & { - { \frac { 1 } { 2 } } } & { - 2 } & { 5 } \end{array} } \right] ;$ ${ \mathrm { U s e ~ } } \mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 0 , - 3 ) ^ { t }$ f $\begin{array}{c} { \bf \underline { { \boldsymbol { \mathsf { T } } } } } ^ { - 4 } \quad \quad { \bf 0 } \quad \quad { \frac { 1 } { 2 } } \quad \quad { \frac { 1 } { 2 } } { \bf \underline { { \boldsymbol { \mathsf { T } } } } }  \\ { \quad \quad { \frac { 1 } { 2 } } \quad - 2 \quad { \bf 0 } \quad { \frac { 1 } { 2 } } } \\ { \quad \quad { \frac { 1 } { 2 } } \quad \quad { \frac { 1 } { 2 } } \quad { \bf 0 } \quad { \bf 0 } } \\ { \quad \quad { \bf 0 } \quad \quad 1 \quad 1 \quad 4 } \end{array} \} ;$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 , 1 ) ^ { t } .$

2.Repeat Exercise 1 using the Inverse Power method.

3.Findthe firstthreeiterations obtained by the Symmetric Power method applied to the following matrices.

$\mathbf { a } . { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] } ;$ ${ \bf b . } \quad \left[ \begin{array} { c c c } { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 1 } } \end{array} \right] ;$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 2 ) ^ { t } .$ $\begin{array} { r } { \mathrm { U s e } \mathbf { x } ^ { ( 0 ) } = ( - 1 , 0 , 1 ) ^ { t } . } \end{array}$ c $\begin{array} { r } { \left[ { \begin{array} { r r r } { 4 . 7 5 } & { 2 . 2 5 } & { - 0 . 2 5 } \\ { 2 . 2 5 } & { 4 . 7 5 } & { 1 . 2 5 } \\ { - 0 . 2 5 } & { 1 . 2 5 } & { 4 . 7 5 } \end{array} } \right] ; } \end{array}$ d. $\left[ { \begin{array} { r r r r } { 4 } & { 1 } & { - 1 } & { 0 } \\ { 1 } & { 3 } & { - 1 } & { 0 } \\ { - 1 } & { - 1 } & { 5 } & { 2 } \\ { 0 } & { 0 } & { 2 } & { 4 } \end{array} } \right] ;$ $\mathsf { J s e x } ^ { ( 0 ) } = ( 0 , 1 , 0 ) ^ { t }$ Use $\mathbf { x } ^ { ( 0 ) } = ( 0 , 1 , 0 , 0 ) ^ { t }$

e. ${ \left[ \begin{array} { l l l l } { 4 } & { } & { 1 } & { } & { 1 } \\ { 1 } & { 3 } & { - 1 } & { 1 } \\ { 1 } & { - 1 } & { 2 } & { 0 } \\ { 1 } & { 1 } & { 0 } & { 2 } \end{array} \right] } ;$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 0 ) ^ { t } .$

$$
\mathbf { f } . \quad \left[ \begin{array} { r r r r } { 5 } & { - 2 } & { - \frac { 1 } { 2 } } & { \frac { 3 } { 2 } } \\ { - 2 } & { 5 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { - \frac { 1 } { 2 } } & { \frac { 3 } { 2 } } & { 5 } & { - 2 } \\ { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } & { - 2 } & { 5 } \end{array} \right] ;
$$

$$
\mathrm { U s e } \ : \mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 0 , - 3 ) ^ { t } .
$$

4.Develop an algorithm to incorporate the Inverse Power method into the Symmetric Powei method. Repeat Exercise 3 using the new algorithm. ：

5.Use the Power method and Wielandt deflation to approximate the two most dominant eigenvalues for the matrices in Exercise 1. Iterate until a tolerance of $1 0 ^ { - 4 }$ is achieved or until the number of iterations exceeds 25.

6. Repeat Exercise 5 using Aitken's $\Delta ^ { 2 }$ technique and the Power method for the most dominant eigenvalue.

7．Use the Symmetric Power method to compute the largest eigenvalue (in absolute value) of the matrices given in Exercise 3. Iterate until a tolerance of $1 0 ^ { - 4 }$ is achieved or until the number of iterations exceeds 25.

8.Repeat Exercise 6 using the Inverse Power method.

9.Repeat Exercise 7 using the Inverse Power method.

10.Annihilation Technique Suppose the $n \times n$ matrix $A$ has eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ ordered by

$$
| \lambda _ { 1 } | > | \lambda _ { 2 } | > | \lambda _ { 3 } | \geq \cdot \cdot \cdot \geq | \lambda _ { n } | ,
$$

with linearly independent eigenvectors v(1), v(2)..., v(n).

a.Show that if the Power method is applied with an initial vector $\mathbf { x } ^ { ( 0 ) }$ given by

$$
\begin{array} { r } { \mathbf { x } ^ { ( 0 ) } = \beta _ { 2 } \mathbf { v } ^ { ( 2 ) } + \beta _ { 3 } \mathbf { v } ^ { ( 3 ) } + \cdot \cdot \cdot + \beta _ { n } \mathbf { v } ^ { ( n ) } , } \end{array}
$$

then the sequence $\{ \mu ^ { ( m ) } \}$ described in Algorithm 9.1 will converge to $\lambda _ { 2 }$

11. Hotelling Deflation Assume that the largest eigenvalue $\lambda _ { 1 }$ in magnitude and an associated eigenvector $\mathbf { v } ^ { ( 1 ) }$ have been obtained for the $n \times n$ symmetric matrix $A$ . Show that the matrix

$$
\begin{array} { r } { B = A - \frac { \lambda _ { 1 } } { ( \mathbf { v } ^ { ( 1 ) } ) ^ { t } \mathbf { v } ^ { ( 1 ) } } \mathbf { v } ^ { ( 1 ) } ( \mathbf { v } ^ { ( 1 ) } ) ^ { t } } \end{array}
$$

has the same eigenvalues λ2,.. ,λn as A,except that B has eigenvalue O with eigenvector v(1) instead of eigenvector λ1. Use this deflation method to find λ2 for each matrix in Exercise 3. Theoretically, this method can be continued to find more eigenvalues,but roundoff error soon makes the effort worthless.

12. Show that the ith row of $B = A - \lambda _ { 1 } \mathbf { v } ^ { ( 1 ) } \mathbf { x } ^ { t }$ is zero, where $\lambda _ { 1 }$ is the largest value of $A$ in absolute value, $\mathbf { v } ^ { ( 1 ) }$ is the associated eigenvector of $A$ for $\lambda _ { 1 }$ ,and $\pmb { \ X }$ is the vector defined in Eq. (9.6).

13.Following along the line of Exercise 11 in Section 6.3 and Exercise 11 in Section 7.2,suppose that a species of beetle has a life span of 4 years,and that a female in the first year has a survival rate of $\frac { 1 } { 2 }$ , in the second year a survival rate of $\frac { 1 } { 4 }$ ,and in the third year a survival rate of $\frac { 1 } { 8 }$ . Suppose additionally that a female gives birth, on the average, to two new females in the third year and to four new females in the fourth year. The matrix describing a single female's contribution in one year to the female population in the succeeding year is

$$
A = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 2 } & { 4 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 4 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { { \frac { 1 } { 8 } } } & { 0 } \end{array} \right] } ,
$$

where again the entry in the ith row and jth column denotes the probabilistic contribution that a female of age $j$ makes on the next year's female population of age $i$

a. Use the Gerschgorin Circle Theorem to determine a region in the complex plane containing all the eigenvalues of $\pmb { A }$   
b. Use the Power method to determine the dominant eigenvalue of the matrix and its associated eigenvector.   
c. Use Algorithm 9.4 to determine any remaining eigenvalues and eigenvectors of $A$ ·   
d. Find the eigenvalues of $\pmb { A }$ by using the characteristic polynomial of $A$ and Newton's method.   
e. What is your long-range prediction for the population of these beetles?

14.A linear dynamical system can be represented by the equations

$$
\frac { d { \mathbf { x } } } { d t } = A ( t ) { \mathbf { x } } ( t ) + B ( t ) { \mathbf { u } } ( t ) , \quad { \mathbf { y } } ( t ) = C ( t ) { \mathbf { x } } ( t ) + D ( t ) { \mathbf { u } } ( t ) ,
$$

where $A$ is an $n \times n$ variable matrix, $\pmb { B }$ is an $n \times r$ variable matrix, $C$ is an $m \times n$ variable matrix, $D$ is an $m \times r$ variable matrix, $\mathbf { x }$ is an $\pmb { n }$ -dimensional vector variable, $\mathbf { y }$ is an $m$ -dimensional vector variable, and $\mathbf { u }$ is an $\boldsymbol { r }$ -dimensional vector variable. For the system to be stable, the matrix $\pmb { A }$ must have all its eigenvalues with nonpositive real part for all $\pmb { \mathrm { \downarrow } }$

a.Is the system stable if

$$
A ( t ) = \left[ { \begin{array} { c c c } { - 1 } & { 2 } & { 0 } \\ { - 2 . 5 } & { - 7 } & { 4 } \\ { 0 } & { 0 } & { - 5 } \end{array} } \right] ;
$$

b.Is the system stable if

$$
A ( t ) = \left[ \begin{array} { r r r r } { { - 1 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { - 5 } } & { { 1 } } \\ { { - 1 } } & { { - 1 } } & { { - 2 } } & { { - 3 } } \end{array} \right] \stackrel { , } { , }
$$

15.The $( m - 1 ) \times ( m - 1 )$ tridiagonal matrix

$$
\begin{array} { r } { A = \left[ { \begin{array} { l l l l l } { 1 + 2 \alpha } & { - \alpha } & { 0 . \cdot \cdots } & { \cdots } & { 0 } \\ { \qquad \vdots } & { \qquad \vdots } & { \qquad \vdots } \\ { - \alpha . \cdot _ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot } } & { - \alpha } & { \cdot \cdot \cdot \cdot } & { \vdots } \\ { \qquad \cdot \cdot \cdot \cdot \cdot \cdot _ { \cdot \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot } } } } & { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot } } } & { \cdot } \\ { \vdots \qquad \cdot \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot } } } } } } & { \cdot \cdot \cdot \cdot _ { \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot } } } } & { \cdot } \\ { \vdots \qquad \cdot \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot _ { \cdot \cdot \cdot } } } } } } } & { \cdot \cdot \cdot \cdot _ { \cdot \cdot _ { \cdot \cdot } } } & { - \alpha } \\ { \vdots \qquad \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot _ { 0 } } & { - \cdot \cdot _ { \cdot \cdot \cdot } } & { \cdot \cdot _ { + 2 \alpha } } \end{array} } \right] } \end{array}
$$

is involved in the Backward Diference method to solve the heat equation. (See Section 12.2.) For the stability of the method we need $\rho ( A ^ { - 1 } ) < 1$ . With $m = 1 1$ , approximate $\rho ( A ^ { - 1 } )$ for

each of the following.

a. $\begin{array} { r } { \alpha = \frac { 1 } { 4 } } \end{array}$ $\begin{array} { r l } { \mathbf { b } , } & { { } \ \alpha = \frac { 1 } { 2 } } \end{array}$ $\begin{array} { r l } { \mathbf { c } _ { \ast } } & { { } \alpha = \frac { 3 } { 4 } } \end{array}$

When is the method stable?

16.The eigenvalues of the matrix $A$ in Exercise 15 are

$$
\lambda _ { i } = 1 + 4 \alpha \left( \sin \frac { \pi i } { 2 m } \right) ^ { 2 } , \quad \mathbf { f o r } i = 1 , \dots , m - 1 .
$$

Compare the approximation in Exercise 15 to the actual value of $\rho ( A ^ { - 1 } )$ . Again, when is the method stable?

17.The $( m - 1 ) \times ( m - 1 )$ matrices A and $\pmb { B }$ given by

$$
\left[ \begin{array} { l l l l l } { 1 + \alpha } & { - \frac { \alpha } { 2 } } & { 0 ; \cdots } & { \cdots } & { \cdots } & { 0 } \\ { - \frac { \alpha } { 2 } \cdot 1 + \alpha } & { - \frac { \alpha } { 2 } \cdot \ddots } & { \vdots } \\ { - \frac { \alpha } { \ddots } \cdot 1 \cdot \cdots } & { \cdots } & { \ddots } & { \ddots } \\ { 0 \cdot \qquad \cdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots \quad \cdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots \quad \cdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots \quad \cdots } & { \cdots } & { \ddots } & { \ddots } \\ { 0 \cdot \cdots } & { \cdots } & { \cdots } & { - \frac { \alpha } { 2 } } & { 1 + \alpha } \end{array} \right] \quad \mathrm { a n d } \quad B = \left[ \begin{array} { l l l l l l } { 1 - \alpha } & { \frac { \alpha } { 2 } } & { 0 ; \cdots } & { \cdots } & { \cdots } \\ { \frac { \alpha } { 2 } \cdot 1 - \alpha } & { \frac { \alpha } { 2 } } & { \ddots } & { \ddots } & { \vdots } \\ { 0 \cdot \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { 0 \cdot \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots \quad \cdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots \quad \cdots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { 0 \cdot \cdots } & { \cdots } & { \cdots } & { 0 } & { \frac { \alpha } { 2 } } & { 1 - \alpha } \end{array} \right]
$$

are involved in the Crank-Nicolson method to solve the heat equation (see Section 12.2). With $m = 1 1$ , approximate $\rho ( A ^ { - 1 } B )$ for each of the following.

a. $\begin{array} { r } { \alpha = \frac { 1 } { 4 } } \end{array}$ b. $\begin{array} { r } { \alpha = \frac { 1 } { 2 } } \end{array}$ $\begin{array} { r l } { \mathfrak { c } _ { \bullet } } & { { } \ : \alpha = \frac { 3 } { 4 } } \end{array}$

# 9.3 Householder's Method

In Section 9.4 we will use the QR method to reduce a symmetric tridiagonal matrix to a similar matrix that is nearly diagonal. The diagonal entries of the reduced matrix are approximations to the eigenvalues of the given matrix. In this section, we present a method devised by Alton Householder for reducing an arbitrary symmetric matrix to a similar tridi-agonal matrix. Although there is a clear connection between the problems we are solving in these two sections, Householder's method has a wide application in areas other than eigenvalue approximation.

Householder's method is used to find a symmetric tridiagonal matrix $B$ that is similar to a given symmetric matrix A. Theorem 9.10 implies that $\pmb { A }$ is similar to a diagonal matrix $D$ since an orthogonal matrix $Q$ exists with the property that $D = Q ^ { - 1 } A Q = Q ^ { t } A Q$ . Because the matrix $Q$ (and consequently $D$ ) is generally difficult to compute, Householder's method offers a compromise. After Householder's method has been implemented, efficient methods such as the QR algorithm can be used for accurate approximation of the eigenvalues of the resulting symmetric tridiagonal matrix.

Definition 9.16 Let $\mathbf { w } \in \mathbb { R } ^ { n }$ with $\mathbf { w } ^ { t } \mathbf { w } = 1$ .The $n \times n$ matrix

$$
P = I - 2 \mathbf { w } \mathbf { w } ^ { t }
$$

is called a Householder transformation.

Householder transformations are used to selectively zero out blocks of entries in vectors or columns of matrices in a manner that is extremely stable with respect to roundoff error. (See [Wil2, pp. 152-162], for further discussion.) Properties of Householder transformations are given in the following theorem.

# Theorem 9.17

A Householder transformation, $P = I - 2 \mathbf { w } \mathbf { w } ^ { t }$ , is symmetric and orthogonal, so $P ^ { - 1 } = P$

# Proof Since

$$
( \mathbf { w } \mathbf { w } ^ { t } ) ^ { t } = ( \mathbf { w } ^ { t } ) ^ { t } \mathbf { w } ^ { t } = \mathbf { w } \mathbf { w } ^ { t } ,
$$

it follows that

$$
P ^ { t } = ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) ^ { t } = I - 2 \mathbf { w } \mathbf { w } ^ { t } = P .
$$

Further, since $\mathbf { w } ^ { t } \mathbf { w } = 1$ ，

$$
\begin{array} { r l } & { P P ^ { t } = ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) = I - 2 \mathbf { w } \mathbf { w } ^ { t } - 2 \mathbf { w } \mathbf { w } ^ { t } + 4 \mathbf { w } \mathbf { w } ^ { t } \mathbf { w } \mathbf { w } ^ { t } } \\ & { \qquad = I - 4 \mathbf { w } \mathbf { w } ^ { t } + 4 \mathbf { w } \mathbf { w } ^ { t } = I , } \end{array}
$$

so

$$
P ^ { - 1 } = P ^ { t } = P .
$$

Householder's method begins by determining $\mathbf { \dot { a } }$ transformation $P ^ { ( 1 ) }$ with the property that $A ^ { ( 2 ) } = P ^ { ( 1 ) } A P ^ { ( 1 ) }$ has

$$
a _ { j 1 } ^ { ( 2 ) } = 0 , \quad \mathrm { f o r e a c h } j = 3 , 4 , \dots , n ,
$$

and by symmetry, $a _ { 1 j } ^ { ( 2 ) } = 0$

The vector $\mathbf { w } = ( w _ { 1 } , w _ { 2 } , \dots , w _ { n } ) ^ { t }$ is chosen so that $\mathbf { w } ^ { t } \mathbf { w } = 1$ ,Eq. (9.7) holds, and in the matrix

$$
A ^ { ( 2 ) } = P ^ { ( 1 ) } A P ^ { ( 1 ) } = ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) A ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) ,
$$

we have a(2) $a _ { 1 1 } ^ { ( 2 ) } = a _ { 1 1 }$ and $a _ { j 1 } ^ { ( 2 ) } = 0$ ,for each $j = 3 , 4 , \dots , n$ . This choice imposes n conditions on the $\pmb { n }$ unknowns $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$

$w _ { \mathfrak { l } } = \mathbf { 0 }$ $a _ { 1 1 } ^ { ( 2 ) } = a _ { 1 1 }$

$$
P ^ { ( 1 ) } = I - 2 \mathbf { w } \mathbf { w } ^ { t }
$$

to satisfy

$$
P ^ { ( 1 ) } ( a _ { 1 1 } , a _ { 2 1 } , a _ { 3 1 } , \ldots , a _ { n 1 } ) ^ { t } = ( a _ { 1 1 } , \alpha , 0 , \ldots , 0 ) ^ { t } ,
$$

where $\pmb { \alpha }$ will be chosen later. To simplify notation, let

$$
\hat { \mathbf { w } } = ( w _ { 2 } , w _ { 3 } , \ldots , w _ { n } ) ^ { t } \in \mathbb { R } ^ { n - 1 } , \quad \hat { \mathbf { y } } = ( a _ { 2 1 } , a _ { 3 1 } , \ldots , a _ { n 1 } ) ^ { t } \in \mathbb { R } ^ { n - 1 } ,
$$

and $\hat { P }$ be the $( n - 1 ) \times ( n - 1 )$ Householder transformation

$$
\hat { P } = I _ { n - 1 } - 2 \hat { \mathbf { w } } \hat { \mathbf { w } } ^ { t } .
$$

Eq. (9.8) then becomes

$$
P ^ { ( 1 ) } \left[ \begin{array} { l } { a _ { 1 1 } } \\ { a _ { 2 1 } } \\ { a _ { 3 1 } } \\ { \vdots } \\ { a _ { n 1 } } \\ { a _ { n 1 } } \end{array} \right] = \left[ \begin{array} { l } { 1 ^ { : } 0 \cdot \cdots \cdots \cdots 0 } \\ { \cdots \cdots \cdots \cdots \cdots \cdots } \\ { 1 } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} \right] \cdot \left[ \begin{array} { l } { a _ { 1 1 } } \\ { \cdots \cdots \cdots } \\ { \cdots } \\ { \hat { \mathbf { y } } } \\ { \hat { P } } \end{array} \right] = \left[ \begin{array} { l } { a _ { 1 1 } } \\ { a _ { 1 1 } } \\ { \cdots \cdots } \\ { \hat { P } \hat { \mathbf { y } } } \\ { \vdots } \\ { a _ { n 1 } } \end{array} \right] = \left[ \begin{array} { l } { a _ { 1 1 } } \\ { \cdots \cdots } \\ { \alpha } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} \right]
$$

with

$$
\hat { P } \hat { \mathbf { y } } = ( I _ { n - 1 } - 2 \hat { \mathbf { w } } \hat { \mathbf { w } } ^ { t } ) \hat { \mathbf { y } } = \hat { \mathbf { y } } - 2 ( \hat { \mathbf { w } ^ { t } } \hat { \mathbf { y } } ) \hat { \mathbf { w } } = ( \alpha , 0 , \ldots , 0 ) ^ { t } .
$$

Let $\boldsymbol { r } = \hat { \mathbf { w } } ^ { t } \hat { \mathbf { y } }$ . Then

$$
( \alpha , 0 , \ldots , 0 ) ^ { t } = ( a _ { 2 1 } - 2 r w _ { 2 } , a _ { 3 1 } - 2 r w _ { 3 } , \ldots , a _ { n 1 } - 2 r w _ { n } ) ^ { t } ,
$$

and we can determine all of the $w _ { i }$ once we know $\pmb { \alpha }$ and $r$ . Equating components gives

$$
\alpha = a _ { 2 1 } - 2 r w _ { 2 }
$$

and

$$
0 = a _ { j 1 } - 2 r w _ { j } , \quad \mathrm { f o r } \operatorname { e a c h } j = 3 , \ldots , n .
$$

Thus,

and

$$
\begin{array} { l } { 2 r w _ { 2 } = a _ { 2 1 } - \alpha } \\ { \qquad } \\ { 2 r w _ { j } = a _ { j 1 } , \quad \mathrm { f o r e a c h } j = 3 , \ldots , n . } \end{array}
$$

Squaring both sides of each of the equations and adding gives

$$
4 r ^ { 2 } \sum _ { j = 2 } ^ { n } w _ { j } ^ { 2 } = ( a _ { 2 1 } - \alpha ) ^ { 2 } + \sum _ { j = 3 } ^ { n } a _ { j 1 } ^ { 2 } .
$$

Since $\mathbf { w } ^ { t } \mathbf { w } = 1$ and $w _ { \mathrm { 1 } } = 0$ ， we have $\textstyle \sum _ { j = 2 } ^ { n } w _ { j } ^ { 2 } = 1$ ,and

$$
4 r ^ { 2 } = \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } - 2 \alpha a _ { 2 1 } + \alpha ^ { 2 } .
$$

Equation (9.9) and the fact that $P$ is orthogonal imply that

$$
\alpha ^ { 2 } = ( \alpha , 0 , \ldots , 0 ) ( \alpha , 0 , \ldots , 0 ) ^ { t } = ( \hat { P } \hat { \mathbf { y } } ) ^ { t } \hat { P } \hat { \mathbf { y } } = \hat { \mathbf { y } } ^ { t } \hat { P } ^ { t } \hat { P } \hat { \mathbf { y } } = \hat { \mathbf { y } } ^ { t } \hat { \mathbf { y } } ^ { t } \hat { \mathbf { y } } .
$$

Thus,

$$
\alpha ^ { 2 } = \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } ,
$$

which, when substituted into Eq. (9.12), gives

$$
2 r ^ { 2 } = \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } - \alpha a _ { 2 1 } .
$$

To ensure that $2 r ^ { 2 } = 0$ only if $a _ { 2 1 } = a _ { 3 1 } = \cdot \cdot \cdot = a _ { n 1 } = 0$ ,we choose

$$
\alpha = - \mathrm { s g n } ( a _ { 2 1 } ) \left( \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } \right) ^ { 1 / 2 } ,
$$

which implies that

$$
2 r ^ { 2 } = \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } + | a _ { 2 1 } | \left( \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } \right) ^ { 1 / 2 } .
$$

With this choice of $\pmb { \alpha }$ and $2 r ^ { 2 }$ ,we solve Eqs. (9.10) and (9.11) to obtain

$$
w _ { 2 } = { \frac { a _ { 2 1 } - \alpha } { 2 r } } \quad { \mathrm { a n d } } \quad w _ { j } = { \frac { a _ { j 1 } } { 2 r } } , \quad { \mathrm { f o r ~ e a c h ~ } } j = 3 , \ldots , n .
$$

To summarize the choice of $P ^ { ( 1 ) }$ , we have

$$
\begin{array} { l } { \displaystyle \alpha = - s \mathbf { g n } ( a _ { 2 1 } ) \left( \displaystyle \sum _ { j = 2 } ^ { n } a _ { j 1 } ^ { 2 } \right) ^ { 1 / 2 } , } \\ { \displaystyle r = \left( \frac 1 2 \alpha ^ { 2 } - \frac 1 2 a _ { 2 1 } \alpha \right) ^ { 1 / 2 } , } \\ { \displaystyle w _ { 1 } = 0 , } \\ { \displaystyle w _ { 2 } = \frac { a _ { 2 1 } - \alpha } { 2 r } , } \end{array}
$$

and

$$
{ \pmb w } _ { j } = \frac { a _ { j 1 } } { 2 r } , \quad \mathrm { f o r e a c h } \ j = 3 , \ldots , n .
$$

With this choice,

$$
A ^ { ( 2 ) } = P ^ { ( 1 ) } A P ^ { ( 1 ) } = \left[ \begin{array} { c c c c c } { a _ { 1 1 } ^ { ( 2 ) } } & { a _ { 1 2 } ^ { ( 2 ) } } & { 0 } & { \cdots } & { 0 } \\ { a _ { 2 1 } ^ { ( 2 ) } } & { a _ { 2 2 } ^ { ( 2 ) } } & { a _ { 2 3 } ^ { ( 2 ) } } & { \cdots } & { a _ { 2 n } ^ { ( 2 ) } } \\ { 0 } & { a _ { 3 2 } ^ { ( 2 ) } } & { a _ { 3 3 } ^ { ( 2 ) } } & { \cdots } & { a _ { 3 n } ^ { ( 2 ) } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { a _ { n 2 } ^ { ( 2 ) } } & { a _ { n 3 } ^ { ( 2 ) } } & { \cdots } & { a _ { n n } ^ { ( 2 ) } } \end{array} \right] .
$$

Having found $P ^ { ( 1 ) }$ and computed $\pmb { A } ^ { ( 2 ) }$ , the process is repeated for $k = 2 , 3 , \ldots , n - 2$ as follows:

$$
\begin{array} { r l } & { \alpha = - 8 \Re ( a _ { k + 1 , k } ^ { ( k ) } ) \left( \displaystyle \sum _ { j = k + 1 } ^ { n } ( a _ { j k } ^ { ( k ) } ) ^ { 2 } \right) ^ { 1 / 2 } , } \\ & { \quad r = \left( \displaystyle \frac 1 2 \alpha ^ { 2 } - \displaystyle \frac 1 2 \alpha \alpha _ { k + 1 , k } ^ { ( k ) } \right) ^ { 1 / 2 } , } \\ & { w _ { 1 } ^ { ( k ) } = w _ { 2 } ^ { ( k ) } = \hdots = w _ { k } ^ { ( k ) } = 0 , } \\ & { w _ { k + 1 , k } ^ { ( k ) } = \frac { a _ { k + 1 , k } ^ { ( k ) } - \alpha } { 2 r } , } \\ & { w _ { j } ^ { ( k ) } = \displaystyle \frac { a _ { j k } ^ { ( k ) } } { 2 r } , \quad \mathrm { f o r ~ a c h ~ } \ j = k + 2 , k + 3 , \hdots , n , } \\ & { P ^ { ( k ) } = l - 2 w ^ { ( k ) } \cdot ( \Psi ^ { ( k ) } ) . } \end{array}
$$

and

$$
A ^ { ( k + 1 ) } = P ^ { ( k ) } A ^ { ( k ) } P ^ { ( k ) } ,
$$

where

$$
\begin{array} { r } { A ^ { ( k + 1 ) } = \left[ \begin{array} { c c c c c c c c c } { a _ { 1 1 } ^ { ( k + 1 ) } \cdot \underbrace { a _ { 1 2 } ^ { ( k + 1 ) } } _ { \ddots \ddots \ddots \ddots \ddots \ddots \ddots \ddots } \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots } \right]} & { 0 } \\ { a _ { 2 1 } ^ { ( k + 1 ) } \cdot \ddots \ldots \ldots \ldots \ldots \ldots \ldots } & { \vdots } \\ { 0 \cdot \ddots \ldots \ldots \ldots \ldots } & { \ldots \ldots \ldots } & { \ldots } \\ { \vdots } & { \ddots \ddots \ldots \ldots \ldots } & { \ldots } & { \ldots } \\ { \vdots } & { \ddots \ddots \ldots \ldots \underbrace { a _ { k + 1 } ^ { ( k + 1 ) } } \cdot \ddots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots } & { 0 } \\ { \vdots } & { \ddots \ddots \underbrace { a _ { k + 1 , k } ^ { ( k + 1 ) } } _ { \ddots \ddots \ddots \ddots } a _ { k + 1 , k + 1 } ^ { ( k + 1 ) } \cdot a _ { k + 1 , k + 2 } ^ { ( k + 1 ) } \ldots \ldots \ldots a _ { k + 1 , n } ^ { ( k + 1 ) } } \\ { \vdots } & { \ddots \ddots \underbrace { \vdots } _ { \vdots } } & { \vdots } & { \ddots \ddots \ldots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots \ddots \ldots } & { \vdots } \\ { 0 \cdot \ldots \ldots \ldots \ldots \ldots \ldots \ldots } & { 0 } & { a _ { n , k + 1 } ^ { ( k + 1 ) } \ldots \ldots \ldots \ldots \ldots \ldots } & { a _ { n } ^ { ( k + 1 ) } } \end{array}  .  \end{array}
$$

Continuing in this manner,the tridiagonal and symmetric matrix $A ^ { ( n - 1 ) }$ is formed, where

$$
A ^ { ( n - 1 ) } = P ^ { ( n - 2 ) } P ^ { ( n - 3 ) } \cdot \cdot \cdot P ^ { ( 1 ) } A P ^ { ( 1 ) } \cdot \cdot \cdot P ^ { ( n - 3 ) } P ^ { ( n - 2 ) } .
$$

# EXAMPLE 1 The $4 \times 4$ matrix

$$
A = \left[ { \begin{array} { r r r r } { 4 } & { 1 } & { - 2 } & { 2 } \\ { 1 } & { 2 } & { 0 } & { 1 } \\ { - 2 } & { 0 } & { 3 } & { - 2 } \\ { 2 } & { 1 } & { - 2 } & { - 1 } \end{array} } \right]
$$

is symmetric.For the first application of a Householder transformation,

$$
\alpha = - ( 1 ) \left( \sum _ { j = 2 } ^ { 4 } a _ { j 1 } ^ { 2 } \right) ^ { 1 / 2 } = - 3 , ~ r = \left( \frac { 1 } { 2 } ( - 3 ) ^ { 2 } - \frac { 1 } { 2 } ( 1 ) ( - 3 ) \right) ^ { 1 / 2 } = \sqrt { 6 } ,
$$

$$
\mathbf { w } = \left( 0 , \frac { \sqrt { 6 } } { 3 } , - \frac { \sqrt { 6 } } { 6 } , \frac { \sqrt { 6 } } { 6 } \right) ,
$$

$$
P ^ { ( 1 ) } = \left[ { \begin{array} { r r r r } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] - 2 \left( { \frac { \sqrt { 6 } } { 6 } } \right) ^ { 2 } \left[ { \begin{array} { r } { 0 } \\ { 2 } \\ { - 1 } \\ { 1 } \end{array} } \right] \cdot ( 0 , 2 , - 1 , 1 )
$$

$$
\mathbf { \Sigma } = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - \frac { 1 } { 3 } } & { \frac { 2 } { 3 } } & { - \frac { 2 } { 3 } } \\ { 0 } & { \frac { 2 } { 3 } } & { \frac { 2 } { 3 } } & { \frac { 1 } { 3 } } \\ { 0 } & { - \frac { 2 } { 3 } } & { \frac { 1 } { 3 } } & { \frac { 2 } { 3 } } \end{array} \right] ,
$$

and

$$
A ^ { ( 2 ) } = \left[ { \begin{array} { r r r r } { 4 } & { - 3 } & { 0 } & { 0 } \\ { - 3 } & { { \frac { 1 0 } { 3 } } } & { 1 } & { { \frac { 4 } { 3 } } } \\ { 0 } & { 1 } & { { \frac { 5 } { 3 } } } & { - { \frac { 4 } { 3 } } } \\ { 0 } & { { \frac { 4 } { 3 } } } & { - { \frac { 4 } { 3 } } } & { - 1 } \end{array} } \right] .
$$

Continuing to the second iteration,

$$
\alpha = - \frac { 5 } { 3 } , \quad r = \frac { 2 \sqrt { 5 } } { 3 } , \quad \mathbf { w } = \left( 0 , 0 , 2 \sqrt { 5 } , \frac { \sqrt { 5 } } { 5 } \right) ^ { t } ,
$$

$$
P ^ { ( 2 ) } = \left[ { \begin{array} { r r r r } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - { \frac { 3 } { 5 } } } & { - { \frac { 4 } { 5 } } } \\ { 0 } & { 0 } & { - { \frac { 4 } { 5 } } } & { { \frac { 3 } { 5 } } } \end{array} } \right] ,
$$

and the symmetric tridiagonal matrix is

$$
A ^ { ( 3 ) } = \left[ { \begin{array} { r r r r } { 4 } & { - 3 } & { 0 } & { 0 } \\ { - 3 } & { { \frac { 1 0 } { 3 } } } & { - { \frac { 5 } { 3 } } } & { 0 } \\ { 0 } & { - { \frac { 5 } { 3 } } } & { - { \frac { 3 3 } { 2 5 } } } & { { \frac { 6 8 } { 7 5 } } } \\ { 0 } & { 0 } & { { \frac { 6 8 } { 7 5 } } } & { { \frac { 1 4 9 } { 7 5 } } } \end{array} } \right] .
$$

Algorithm 9.5 performs Householder's method as described here, although the actual matrix multiplications are circumvented.

# Householder's

To obtain a symmetric tridiagonal matrix $A ^ { ( n - 1 ) }$ similar to the symmetric matrix $\boldsymbol { A } = \boldsymbol { A } ^ { ( 1 ) }$ ， construt the followig matrices $A ^ { ( 2 ) }$ ， $A ^ { ( 3 ) }$ ，， $A ^ { ( n - 1 ) }$ , where $\dot { A } ^ { ( k ) } = ( a _ { i j } ^ { ( k ) } )$ for each $k =$ $1 , 2 , \ldots , n - 1$ ：

INPUT dimension $\pmb { n }$ ; matrix $A$ .

OUTPUT $A ^ { ( n - 1 ) }$ . (At each step, A can be overwriten.)

Step1Fo $\mathfrak { r } k = 1 , 2 , \ldots , n - 2$ do Steps 2-14.

Step 2 Set

$$
q = \sum _ { j = k + 1 } ^ { n } \left( a _ { j k } ^ { ( k ) } \right) ^ { 2 } .
$$

$a _ { k + 1 , k } ^ { ( k ) } = 0$ then set $\alpha = - q ^ { 1 / 2 }$

Step 4 Set $R S Q = \alpha ^ { 2 } - \alpha a _ { k + 1 , k } ^ { ( k ) } . ( N o t e \cdot R S Q = 2 r ^ { 2 } )$

Step 5Set $\boldsymbol { v } _ { k } = 0$ ；(Note $: v _ { 1 } = \cdot \cdot \cdot = v _ { k - 1 } = 0$ , but are not needed.) $\upsilon _ { k + 1 } = a _ { k + 1 , k } ^ { ( k ) } - \alpha ;$ For j =k +2,...,n set vj = ajk. ${ \bigg ( } N o t e \colon \mathbf { w } = { \bigg ( } { \frac { 1 } { \sqrt { 2 R S Q } } } { \bigg ) } \mathbf { v } = { \frac { 1 } { 2 r } } \mathbf { v } . { \bigg ) }$

$j = k , k + 1 , \ldots , n \mathrm { \ s e t } u _ { j } = \left( \frac { 1 } { R S Q } \right) \sum _ { i = k + 1 } ^ { n } a _ { j i } ^ { ( k ) } v _ { i } .$

$$
\left( N o t e ; { \bf u } = \left( \frac { 1 } { R S Q } \right) A ^ { ( k ) } { \bf v } = \frac { 1 } { 2 r ^ { 2 } } A ^ { ( k ) } { \bf v } = \frac { 1 } { r } A ^ { ( k ) } { \bf w } . \right)
$$

Step 7 Set $P R O D = \sum _ { i = k + 1 } ^ { n } \upsilon _ { i } u _ { i }$ ·

$$
\left( N o t e \colon P R O D = { \bf v } ^ { t } { \bf u } = \frac { 1 } { 2 r ^ { 2 } } { \bf v } ^ { t } A ^ { ( k ) } { \bf v } . \right)
$$

Step 8 For $j = k , k + 1 , \ldots , n { \mathrm { ~ s e t ~ } } z _ { j } = u _ { j } - \left( { \frac { P R O D } { 2 R S Q } } \right) v _ { j } .$

$$
\begin{array} { l } { \displaystyle \bigg ( N o t e              : \mathbf { z } = \mathbf { u } - \frac { 1 } { 2 R S Q } \mathbf { v } ^ { t } \mathbf { u } \mathbf { v } = \mathbf { u } - \frac { 1 } { 4 r ^ { 2 } } \mathbf { v } ^ { t } \mathbf { u } \mathbf { v } } \\ { \displaystyle = \mathbf { u } - \mathbf { w } \mathbf { w } ^ { t } \mathbf { u } = \frac { 1 } { r } A ^ { ( k ) } \mathbf { w } - \mathbf { w } \mathbf { w } ^ { t } \frac { 1 } { r } A ^ { ( k ) } \mathbf { w } . \bigg ) } \end{array}
$$

Step 9 For $l = k + 1 , k + 2 , \ldots , n - 1$ do Steps 10 and 11. (Note: Compute $A ^ { ( k + 1 ) } = A ^ { ( k ) } - \mathbf { v } \mathbf { z } ^ { t } - \mathbf { \bar { z } } \mathbf { v } ^ { t } = ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) A ^ { ( k ) } ( I - 2 \mathbf { w } \mathbf { w } ^ { t } ) . )$

$$
\begin{array} { r l } { { 5 t e p ~ 1 0 } } & { { \mathrm { F o r ~ } j = l + 1 , \ldots , n ~ \mathrm { s e t } } } \\ { { } } & { { a _ { j l } ^ { ( k + 1 ) } = a _ { j l } ^ { ( k ) } - v _ { l } z _ { j } - v _ { j } z _ { l } ; } } \\ { { } } & { { a _ { l j } ^ { ( k + 1 ) } = a _ { j l } ^ { ( k + 1 ) } . } } \end{array}
$$

Step 11 Set $a _ { l l } ^ { ( k + 1 ) } = a _ { l l } ^ { ( k ) } - 2 \upsilon _ { l } z _ { l }$

Step 12 Set $a _ { n n } ^ { ( k + 1 ) } = a _ { n n } ^ { ( k ) } - 2 \upsilon _ { n } z _ { n }$

Step 13 For j = k +2,..,n set ak $a _ { k j } ^ { ( k + 1 ) } = a _ { j k } ^ { ( k + 1 ) } = 0 .$

Step 14 Set $\begin{array} { r l } & { \boldsymbol { a } _ { k + 1 , k } ^ { ( k + 1 ) } = \boldsymbol { a } _ { k + 1 , k } ^ { ( k ) } - \boldsymbol { \upsilon } _ { k + 1 } \boldsymbol { z } _ { k } ; } \\ & { \boldsymbol { a } _ { k , k + 1 } ^ { ( k + 1 ) } = \boldsymbol { a } _ { k + 1 , k } ^ { ( k + 1 ) } . } \end{array}$

(Note: The other elements of $A ^ { ( k + 1 ) }$ are the same as $A ^ { ( k ) }$ ）

Step 15OUTPUT $( A ^ { ( n - 1 ) } )$ ； (The processis complete. $A ^ { ( n - 1 ) }$ is symmetric,trdiagonal,nditA.) STOP.

To apply Householder's Algorithm to an arbitrary $n \times n$ matrix, the following modifications must be made to account for a possible lack of symmetry.

$$
\mathit { S t e p 6 } \quad \mathrm { F o r ~ } j = 1 , 2 , \ldots , n \mathrm { \ s e t } u _ { j } = \frac { 1 } { R S Q } \sum _ { i = k + 1 } ^ { n } a _ { j i } ^ { ( k ) } v _ { i } ;
$$

$$
y _ { j } = \frac { 1 } { R S Q } \sum _ { i = k + 1 } ^ { n } a _ { i j } ^ { ( k ) } v _ { i } .
$$

$j = 1 , 2 , \ldots , n \mathrm { \ s e t \ } z _ { j } = u _ { j } - \frac { P R O D } { R S Q } v _ { j } .$

Step 9For $l = k + 1 , k + 2 , \ldots , n$ do Steps 10 and 11.

Step 10 For j=1,2,..,k seta+ $a _ { j l } ^ { ( k + 1 ) } = a _ { j l } ^ { ( k ) } - z _ { j } v _ { l } ;$

$$
a _ { l j } ^ { ( k + 1 ) } = a _ { l j } ^ { ( k ) } - y _ { j } v _ { l } .
$$

Step 11 For $j = k + 1 , \ldots , n$ set $a _ { j l } ^ { ( k + 1 ) } = a _ { j l } ^ { ( k ) } - z _ { j } v _ { l } - y _ { l } v _ { j } .$ After these steps are modified, delete Steps 12 through 14 and output $A ^ { ( n - 1 ) }$

The resulting matrix $A ^ { ( n - 1 ) }$ will not be tridiagonal unless the original matrix $\pmb { A }$ is symmetric. However, all the entries below the lower subdiagonal will be O. A matrix of this type is called upper Hessenberg. That is, $H = ( h _ { i j } )$ is upper Hessenberg if $h _ { i j } = 0$ ， for all $i \geq j + 2$

In the next section, we willexamine how the QR algorithm can be applied to determine the eigenvalues of $\pmb { A } ^ { ( n - 1 ) }$ , which are the same as those of the original matrix $\pmb { A }$

# ExErcIse Set 9.3

1.Use Householder's method to place the following matrices in tridiagonal form.

$$
\begin{array} { r l } { \mathbf { a } . } & { { } { \left[ \begin{array} { l l l } { 1 2 } & { 1 0 } & { 4 } \\ { 1 0 } & { 8 } & { - 5 } \\ { 4 } & { - 5 } & { 3 } \end{array} \right] } } \\ { \mathbf { c } . } & { { } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \end{array} \right] } } \end{array}
$$

-1 -1   
b. 2 -1   
-1 -1 2   
4.75 2.25 -0.25   
d. 2.25 4.75 1.25   
-0.25 1.25 4.75

2.Use Householder's method to place the following matrices in tridiagonal form.

$\left[ { \begin{array} { r r r r r } { 4 } & { - 1 } & { - 1 } & { 0 } \\ { - 1 } & { 4 } & { 0 } & { - 1 } \\ { - 1 } & { 0 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { - 1 } & { 4 } \end{array} } \right]$ 5 -2 -0.5 1.57  
a. b. 二2.5 15 15 -0.51.5 -0.5 -2 58 0.25 0.5 2 -10.25 -4 0 1 2  
c. 0.5 0 5 0.75 -12 1 0.75 5 -0.5-1 2 -1 -0.5 6 1  
$\mathbf { d . } \quad \left[ \begin{array} { r r r r r } { 2 } & { - 1 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 3 } & { 0 } & { - 2 } & { 0 } \\ { - 1 } & { 0 } & { 4 } & { 2 } & { 1 } \\ { 0 } & { - 2 } & { 2 } & { 8 } & { 3 } \\ { 0 } & { 0 } & { 1 } & { 3 } & { 9 } \end{array} \right]$

3. Modify Householder's Algorithm 9.5 to compute similar upper Hessenberg matrices for the following nonsymmetric matrices.

a. b. 1   
c. 5 1 d. $\left[ { \begin{array} { r r r r } { 4 } & { - 1 } & { - 1 } & { - 1 } \\ { - 1 } & { 4 } & { 0 } & { - 1 } \\ { - 1 } & { - 1 } & { 4 } & { - 1 } \\ { - 1 } & { - 1 } & { - 1 } & { 4 } \end{array} } \right]$ -1

# 9.4 The QR Algorithm

The deflation methods discussd in Section 9.2 are not generall suitable for calculating allthe eigenvalues of a matrix because of the growth of roundoff error. In this section we consider the QR Algorithm, a matrix reduction technique used to simultaneously determine all the eigenvalues of a symmetric matrix.

To apply the QR method, we begin with a symmetric matrix in tridiagonal form; that is,the only nonzero entries in the matrix lie either on the diagonal or on the subdiagonals directly above or below the diagonal. If this is not the form of the symmetric matrix, the first step is to apply Householder's method to compute a symmetric,tridiagonal matrix similar to the given matrix.

In the remainder of this section it willbe assumed that the symmetric matrix for which these eigenvalues are to be calculated is tridiagonal. If we let $A$ denote a matrix of this type, we can simplify the notation somewhat by labeling the entries of $A$ as follows:

$$
A = \left[ \begin{array} { l l l l l } { a _ { 1 } } & { b _ { 2 } } & { 0 . . . . . . . } & { . . } \\ & & & { . . . } & { . . . } \\ { b _ { 2 } } & { a _ { 2 } } & { b _ { 3 } } & { . . . } & { . . } \\ & & { . . } & { b _ { 3 } } & { a _ { 3 } } & { . . . } \\ { . . . } & { . . } & { . . } & { . . } & { . . } \\ { . . } & { . . . } & { . . } & { . . } & { . } \\ { . . } & { . . . } & { . . } & { . . } & { . } \\ { 0 . . . . . . . } & { . . . } & { . } & { . } \end{array} \right] .
$$

f $b _ { 2 } = 0$ or $b _ { n } = 0$ , then the $1 \times 1$ matrix $[ a _ { 1 } ]$ 0r $[ a _ { n } ]$ immediately produces an eigenvalue $a _ { 1 }$ or $a _ { n }$ of $A$

When $b _ { j } = 0$ for some $j$ , where $2 < j < n$ , the problem can be reduced to considering, instead of $A$ , the smaller matrices

$$
\left[ \begin{array} { l l l l l } { a _ { 1 } } & { b _ { 2 } } & { 0 : \dots \dots \dots } & { 0 } \\ { b _ { 2 } } & { a _ { 2 } } & { b _ { 3 } } & { \dots } & { \vdots } \\ { 0 } & { b _ { 3 } } & { a _ { 3 } } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { b _ { j - 1 } } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { 0 } & { \dots \dots \dots } & { 0 } & { b _ { j - 1 } } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { l l l l } { a _ { j } } & { b _ { j + 1 } } & { 0 : \dots \dots } & { \dots } \\ { b _ { j + 1 } } & { a _ { j + 1 } } & { b _ { j + 2 } } & { \ddots } \\ { 0 \ddots } & { b _ { j + 2 } } & { a _ { j + 2 } } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \dots \dots } & { \ddots } & { \ddots } \\ { 0 } & { \dots \dots \dots } & { \dots } & { \ddots } \\ { 0 } & { \dots \dots } & { \dots } & { \ddots } \end{array} \right] .
$$

If none of the $b _ { j }$ are zero, the QR method proceeds by forming a sequence of matrices ${ \cal A } = { \cal A } ^ { ( 1 ) } , { \cal A } ^ { ( 2 ) } , { \cal A } ^ { ( 3 ) } ,$ ..,as follows:

1. $\pmb { A } ^ { ( 1 ) } = \pmb { A }$ is factored as a product $A ^ { ( 1 ) } = Q ^ { ( 1 ) } R ^ { ( 1 ) }$ , where ${ Q } ^ { ( 1 ) }$ is orthogonal and $R ^ { ( 1 ) }$ is upper triangular.   
2. $A ^ { ( 2 ) }$ is defined as $A ^ { ( 2 ) } = R ^ { ( 1 ) } Q ^ { ( 1 ) }$ .

In general, $A ^ { ( i ) }$ is factored as a product $A ^ { ( i ) } = Q ^ { ( i ) } R ^ { ( i ) }$ of an orthogonal matrix $Q ^ { ( i ) }$ and an upper triangular matrix $R ^ { ( i ) }$ .Then $A ^ { ( i + \hat { 1 } ) }$ is defined by the product of $R ^ { ( i ) }$ and $Q ^ { ( i ) }$ in the reverse direction $A ^ { ( i + 1 ) } = R ^ { ( i ) } Q ^ { ( i ) }$ . Since $Q ^ { ( i ) }$ is orthogonal, $R ^ { ( i ) } = \boldsymbol { Q } ^ { ( i ) ^ { t } } \boldsymbol { A } ^ { ( i ) }$ and

$$
A ^ { ( i + 1 ) } = R ^ { ( i ) } Q ^ { ( i ) } = ( Q ^ { ( i ) ^ { t } } A ^ { ( i ) } ) Q ^ { ( i ) } = Q ^ { ( i ) ^ { t } } A ^ { ( i ) } Q ^ { ( i ) } .
$$

So $A ^ { ( i + 1 ) }$ is symmetric with the same eigenvalues as $\pmb { A } ^ { ( i ) }$ . By the manner in which we define $R ^ { ( i ) }$ and $Q ^ { ( i ) }$ , we also ensure that $A ^ { ( i + 1 ) }$ is tridagonal.

Continuing by induction, $A ^ { ( i + 1 ) }$ has the same eigenvalues as the original matrix $A$ , and $A ^ { ( i + 1 ) }$ tends to a diagonal matrix with the eigenvalues of $\pmb { A }$ along the diagonal.

To describe the construction of the factoring matrices $Q ^ { ( i ) }$ and $R ^ { ( i ) }$ , we need the notion of a rotation matrix.

A rotation matrix $P$ differs from the identity matrix in at most four elements. These four elements are of the form

$$
p _ { i i } = p _ { j j } = \cos \theta \quad { \mathrm { a n d } } \quad p _ { i j } = - p _ { j i } = \sin \theta ,
$$

for some $\theta$ and some $i \neq j$

It is easy to show (see Exercise 6) that, for any rotation matrix $P$ ，the matrix $A P$ differs from $A$ only in the ith and $j$ th columns and the matrix $P A$ differs from $A$ only in the ith and $j$ th rows. For any $i \neq j$ , the angle $\theta$ can be chosen so that the product $P A$ has a zero entry for $( P A ) _ { i j }$ . In addition, every rotation matrix $P$ is orthogonal, since the definition implies that $P P ^ { t } = I$ ，

The factorization of $\pmb { A } ^ { ( 1 ) }$ into $A ^ { ( 1 ) } = Q ^ { ( 1 ) } R ^ { ( 1 ) }$ uses a product of $n - 1$ rotation matrices to construct

$$
R ^ { ( 1 ) } = P _ { n } P _ { n - 1 } \cdot \cdot \cdot P _ { 2 } A ^ { ( 1 ) } .
$$

We first choose the rotation matrix $P _ { 2 }$ with

$$
p _ { 1 1 } = p _ { 2 2 } = \cos \theta _ { 2 } \quad \mathrm { a n d } \quad p _ { 1 2 } = - p _ { 2 1 } = \sin \theta _ { 2 } ,
$$

where

$$
\sin \theta _ { 2 } = \frac { b _ { 2 } } { \sqrt { b _ { 2 } ^ { 2 } + a _ { 1 } ^ { 2 } } } \quad \mathrm { a n d } \quad \cos \theta _ { 2 } = \frac { a _ { 1 } } { \sqrt { b _ { 2 } ^ { 2 } + a _ { 1 } ^ { 2 } } } .
$$

Then the matrix

$$
A _ { 2 } ^ { ( 1 ) } = P _ { 2 } A ^ { ( 1 ) }
$$

has a zero in the (2,1) position,that is, in the second row and first column,since the (2,1) entry in ${ A } _ { 2 } ^ { ( 1 ) }$ is

$$
( - \sin \theta _ { 2 } ) a _ { 1 } + ( \cos \theta _ { 2 } ) b _ { 2 } = \frac { - b _ { 2 } a _ { 1 } } { \sqrt { b _ { 2 } ^ { 2 } + a _ { 1 } ^ { 2 } } } + \frac { a _ { 1 } b _ { 2 } } { \sqrt { b _ { 2 } ^ { 2 } + a _ { 1 } ^ { 2 } } } = 0 .
$$

Since the multiplication $P _ { 2 } A ^ { ( 1 ) }$ affects both rows 1 and 2 of $\boldsymbol { A } ^ { ( 1 ) }$ , the new matrix does not necessarily retain zero entries in positions (1,3),(1,4),...,and (1,n). However, A() is tridiagonal, so the $( 1 , 4 ) , \ldots , ( 1 , n )$ entries of ${ A } _ { 2 } ^ { ( 1 ) }$ must be O. Only the (1,3)-entry,the one in the first row and third column, can become nonzero.

In general, the matrix $P _ { k }$ is chosen so that the $( k , k - 1 )$ entry in $A _ { k } ^ { ( 1 ) } = P _ { k } A _ { k - 1 } ^ { ( 1 ) }$ is zero, which results in the $( k - 1 , k + 1 )$ -entry becoming nonzero. The matrix ${ A } _ { k } ^ { ( 1 ) }$ has the form

$$
\begin{array} { r }  A _ { k } ^ { ( 1 ) } = [ \begin{array} { l l l l l l l } { z _ { 1 } } & { z _ { 1 } } & { z _ { 1 } } & { r _ { 1 } } & { \dots } & { 0 } & { z _ { k } ^ { ( - 1 ) } } & { \dots } & { \dots } & { \dots } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { z _ { k - 1 } } & { \dots } & { \dots } & { \dots } & { 0 } \\ { 0 } & { \dots } & { 0 } & { z _ { k - 1 } } & { \dots } & { \dots } & { \dots } & { 0 } \\ { 0 } & { \dots } & { \dots } & { 0 } & { z _ { k - 1 } } & { \dots } & { \dots } & { 0 } \\ { 0 } & { \dots } & { \dots } & { 0 } & { z _ { k } } & { \dots } & { 0 } & { \dots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } & { \dots } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } \\ { 0 } & { \dots } & { 0 } & { \dots } & { 0 } \\ { 0 } &  \end{array} \end{array}
$$

and $P _ { k + 1 }$ has the form

$$
P _ { k + 1 } = { [ \begin{array} { l l l l } { { \frac { I _ { k - 1 } } { O } } } & { O } & { | } & { O } \\ { O } & { ^ { c _ { k + 1 } } } & { ^ { s _ { k + 1 } } } \\ { - ^ { o } { [ \begin{array} { l l l l } { - s _ { k + 1 } } & { } & { c _ { k + 1 } } \\ { O } & { O } & { ^ { c _ { k - 1 } } } \end{array} ] } } & {  { \mathrm { ~ r o w ~ } } k } \end{array} ] } \quad  { \mathrm { ~ r o w ~ } } k
$$

where O denotes the appropriately dimensional matrix with all zero entries.

The constants $c _ { k + 1 } = \cos \theta _ { k + 1 }$ and $s _ { k + 1 } = \sin \theta _ { k + 1 }$ in $P _ { k + 1 }$ are chosen so that the $( k + 1 , k )$ -entry in $A _ { k + 1 } ^ { ( 1 ) }$ is zero; hat is, $s _ { k + 1 } x _ { k } - c _ { k + 1 } b _ { k + 1 } = 0$ Since $c _ { k + 1 } ^ { 2 } + s _ { k + 1 } ^ { 2 } = 1$ ,the solution to this equation is

$$
s _ { k + 1 } = \frac { b _ { k + 1 } } { \sqrt { b _ { k + 1 } ^ { 2 } + x _ { k } ^ { 2 } } } \quad \mathrm { a n d } \quad c _ { k + 1 } = \frac { x _ { k } } { \sqrt { b _ { k + 1 } ^ { 2 } + x _ { k } ^ { 2 } } } ,
$$

and $A _ { k + 1 } ^ { ( 1 ) }$ has the form

$$
A _ { k } ^ { ( 1 ) } = [ \begin{array} { l l l l l l l } { z _ { 1 } , } & { q _ { 1 } } & { r _ { 1 } , } & { 0 } & { 0 } & { \ddots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } \\ { \vdots } & { \ldots } & { \ldots } & { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } \\ { 0 } & { \ldots } & { \ldots } & { 0 } & { x _ { k + 1 } } & { y _ { k } } & { 0 } & { \ldots } & { \ldots } \\ { \vdots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { \vdots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { \vdots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { 0 } & { \ldots } &  \end{array}
$$

Proceeding with this construction in the sequence $P _ { 2 } , \ldots , P _ { n }$ produces the upper triangular matrix

$$
\begin{array} { r } { R ^ { ( 1 ) } \equiv A _ { n } ^ { ( 1 ) } = \left[ \begin{array} { l } { z _ { 1 } , \dotsc , z _ { 1 } , \dotsc , 0 ; \dotsc , \dotsc \dotsc 0 } \\ { 0 , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , } \\ { \vdots , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , } \\ { \vdots , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc } \\ { \vdots , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , } \\ { \vdots , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc , } \\ { \vdots , \dotsc , \dotsc , \dotsc , \dotsc , \dotsc } \\ { \vdots , \dotsc , \dotsc , z _ { n - 1 } } \\ { \dotsc , \dotsc , \dotsc , \dotsc , \dotsc } \\ { \dotsc , \dotsc , \dotsc , \dotsc , \dotsc } \\ { \textnormal { o } , \dotsc , \dotsc , \dotsc , \dotsc , } \end{array} \right] . } \end{array}
$$

The other half of the QR factorization is the matrix

$$
Q ^ { ( 1 ) } = P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { n } ^ { t } ,
$$

since the orthogonality of the rotation matrices implies that

$$
\_ Q ^ { ( 1 ) } R ^ { ( 1 ) } = ( P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { n } ^ { t } ) \cdot ( P _ { n } \cdot \cdot \cdot P _ { 3 } P _ { 2 } ) { \cal A } ^ { ( 1 ) } = { \cal A } ^ { ( 1 ) } .
$$

The matrix $Q ^ { ( 1 ) }$ is orthogonal since

$$
( Q ^ { ( 1 ) } ) ^ { t } Q ^ { ( 1 ) } = ( P _ { 2 } ^ { i } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { n } ^ { t } ) ^ { t } ( P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { n } ^ { t } ) = ( P _ { n } \cdot \cdot \cdot P _ { 3 } P _ { 2 } ) \cdot ( P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { n } ^ { t } ) = I .
$$

In addition, ${ Q ^ { ( 1 ) } }$ is an upper-Hessenberg matrix. To see why this is true, you can follow the steps in Exercises 7 and 8.

As a consequence, $A ^ { ( 2 ) } = R ^ { ( 1 ) } Q ^ { ( 1 ) }$ is also an upper-Hessenberg matrix, since multiplying ${ Q } ^ { \left( 1 \right) }$ on the left by the upper triangular matrix ${ \pmb R } ^ { ( 1 ) }$ does not affect the entries in the lower triangle. This implies that $A ^ { ( 2 ) }$ is in fact tridiagonal, since we already know that it is symmetric.

The entries off the diagonal of $A ^ { ( 2 ) }$ will generally be smaller in magnitude than the corresponding entries of ${ A ^ { ( 1 ) } }$ ,so $\boldsymbol { A } ^ { ( 2 ) }$ is closer to being a diagonal matrix than is $A ^ { ( 1 ) }$ . The process is repeated to construct A(3), A(4),

If the eigenvalues of $A$ have distinct moduli with $| \lambda _ { 1 } | > | \lambda _ { 2 } | > \cdots > | \lambda _ { n } |$ ，then the rate of convergence of the entry $b _ { j + 1 } ^ { ( i + 1 ) }$ to 0 in the matrix $A ^ { ( i + 1 ) }$ depends on the ratio |/jl(seeFr])eatefovergenceofb+1t to O determines the rate at which the entry $a _ { j } ^ { ( i + 1 ) }$ converges to the $j$ th eigenvalue $\lambda _ { j }$ . Thus,the rate of convergence can be slow if $\{ \lambda _ { j + 1 } / \lambda _ { j } \}$ is close to unity.

To accelerate this convergence, a shifting technique is employed similar to that used with the Inverse Power method in Section 9.2.A constant $\pmb { \mathscr { s } }$ is selected close to an eigenvalue of $\pmb { A }$ .This modifies the factorization in Eq.(9.15) to choosing $Q ^ { ( i ) }$ and $R ^ { ( i ) }$ so that

$$
\boldsymbol { A } ^ { ( i ) } - s \boldsymbol { I } = \boldsymbol { Q } ^ { ( i ) } \boldsymbol { R } ^ { ( i ) } ,
$$

and, correspondingly,the matrix $A ^ { ( i + 1 ) }$ is defined to be

$$
A ^ { ( i + 1 ) } = R ^ { ( i ) } Q ^ { ( i ) } + s I .
$$

Withthis modification,terateofconvergenceofb+1 to O depends on the ratio $| ( \lambda _ { j + 1 } -$ $s ) / ( \lambda _ { j } - s ) |$ . This can result in a significant improvement over the original rate of convergence of $a _ { j } ^ { ( i + 1 ) } \mathbf { t o } \lambda _ { j }$ if $\pmb { \mathscr { s } }$ is close to $\lambda _ { j + 1 }$ but not close to $\lambda _ { j }$

We change $\pmb { S }$ at each step so that when $A$ has eigenvalues of distinct modulus, $b _ { n } ^ { ( i + 1 ) }$ converges to 0 faster than $b _ { j } ^ { ( i + 1 ) }$ for any integer $j$ less than $\pmb { n }$ . When $b _ { n } ^ { ( i + 1 ) }$ is sufficiently small, we assume that $\lambda _ { n } ~ \tilde { \approx } ~ a _ { n } ^ { ( i + 1 ) }$ , delete the nth row and column of the matrix, and proceed in the same manner to find an approximation to $\lambda _ { n - 1 }$ . The process is continued until an approximation has been determined for each eigenvalue.

The shifting technique chooses,at the ith step,the shifting constant $\pmb { S } _ { i }$ ，where $s _ { i }$ is the eigenvalue of the matrix

$$
E ^ { ( i ) } = { \left[ \begin{array} { l l } { a _ { n - 1 } ^ { ( i ) } } & { b _ { n } ^ { ( i ) } } \\ { b _ { n } ^ { ( i ) } } & { a _ { n } ^ { ( i ) } } \end{array} \right] }
$$

that is closest to $a _ { n } ^ { ( i ) }$ . This shift translates the eigenvalues of $A$ by a factor $\pmb { S } _ { i }$ . With this shifting technique, the convergence is usually cubic. (See [WR, p. 270].) The method accumulates these shifts until $b _ { n } ^ { ( i + 1 ) } \approx 0$ and then adds the shifts to $a _ { n } ^ { ( i + 1 ) }$ to approximate the eigenvalue $\lambda _ { n }$ ·

f $A$ has eigenvalues of the same modulus, $b _ { j } ^ { ( i + 1 ) }$ may tend to O for some $j \neq n$ at a faster rate than $b _ { n } ^ { ( i + 1 ) }$ . In this case,the matrix-splitting technique described in (9.14) can be employed to reduce the problem to one involving a pair of matrices of reduced order.

$$
A = { \left[ \begin{array} { l l l } { 3 } & { 1 } & { 0 } \\ { 1 } & { 3 } & { 1 } \\ { 0 } & { 1 } & { 3 } \end{array} \right] } = { \left[ \begin{array} { l l l } { a _ { 1 } ^ { ( 1 ) } } & { b _ { 2 } ^ { ( 1 ) } } & { 0 } \\ { b _ { 2 } ^ { ( 1 ) } } & { a _ { 2 } ^ { ( 1 ) } } & { b _ { 3 } ^ { ( 1 ) } } \\ { 0 } & { b _ { 3 } ^ { ( 1 ) } } & { a _ { 3 } ^ { ( 1 ) } } \end{array} \right] } .
$$

To find the acceleration parameter for shifting requires finding the eigenvalues of

$$
\left[ \begin{array} { l l } { a _ { 2 } ^ { ( 1 ) } } & { b _ { 3 } ^ { ( 1 ) } } \\ { b _ { 3 } ^ { ( 1 ) } } & { a _ { 3 } ^ { ( 1 ) } } \end{array} \right] = \left[ \begin{array} { l l } { 3 } & { 1 } \\ { 1 } & { 3 } \end{array} \right] ,
$$

which are $\mu _ { 1 } = 4$ and $ \mu _ { 2 } = 2$ Techcefeigeneostto $a _ { 3 } ^ { ( 1 ) } = 3$ is arbitrary, and we choose $\mu _ { 2 } = 2$ and shift by this amount. Then $s _ { 1 } = 2$ and

$$
\left[ \begin{array} { c c c } { { d _ { 1 } } } & { { b _ { 2 } ^ { ( 1 ) } } } & { { 0 } } \\ { { b _ { 2 } ^ { ( 1 ) } } } & { { d _ { 2 } } } & { { b _ { 3 } ^ { ( 1 ) } } } \\ { { 0 } } & { { b _ { 3 } ^ { ( 1 ) } } } & { { d _ { 3 } } } \end{array} \right] = \left[ \begin{array} { c c c } { { 1 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { 1 } } \\ { { 0 } } & { { 1 } } & { { 1 } } \end{array} \right] .
$$

Continuing the computation gives

$$
x _ { 1 } = 1 , \quad y _ { 1 } = 1 , \quad z _ { 1 } = { \sqrt { 2 } } , \quad c _ { 2 } = { \frac { \sqrt { 2 } } { 2 } } , \quad s _ { 2 } = { \frac { \sqrt { 2 } } { 2 } } ,
$$

$$
q _ { 1 } = { \sqrt { 2 } } , \quad x _ { 2 } = 0 , \quad r _ { 1 } = { \frac { \sqrt { 2 } } { 2 } } , \quad \mathrm { a n d } \quad y _ { 2 } = { \frac { \sqrt { 2 } } { 2 } } ,
$$

so

$$
A _ { 2 } ^ { ( 1 ) } = \left[ \begin{array} { c c c } { { \sqrt { 2 } } } & { { \sqrt { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \\ { { 0 } } & { { 0 } } & { { \sqrt { 2 } } } \\ { { 0 } } & { { 1 } } & { { 1 } } \end{array} \right] .
$$

Further,

$$
z _ { 2 } = 1 , \quad c _ { 3 } = 0 , \quad s _ { 3 } = 1 , \quad q _ { 2 } = 1 , \quad \mathrm { a n d } \quad x _ { 3 } = - \frac { \sqrt { 2 } } { 2 } ,
$$

so

$$
R ^ { ( 1 ) } = A _ { 3 } ^ { ( 1 ) } = \left[ { \begin{array} { c c c } { { \sqrt { 2 } } } & { { \sqrt { 2 } } } & { { { \frac { \sqrt { 2 } } { 2 } } } } \\ { { 0 } } & { { 1 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { - { \frac { \sqrt { 2 } } { 2 } } } } \end{array} } \right] .
$$

To compute ${ \pmb A } ^ { ( 2 ) }$ , we have

$$
z _ { 3 } = - \frac { \sqrt { 2 } } { 2 } , \quad a _ { 1 } ^ { ( 2 ) } = 2 , \quad b _ { 2 } ^ { ( 2 ) } = \frac { \sqrt { 2 } } { 2 } , \quad a _ { 2 } ^ { ( 2 ) } = 1 , \quad b _ { 3 } ^ { ( 2 ) } = - \frac { \sqrt { 2 } } { 2 } ,
$$

so

$$
A ^ { ( 2 ) } = R ^ { ( 1 ) } Q ^ { ( 1 ) } = \left[ \begin{array} { c c c } { { 2 } } & { { \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } \\ { { \frac { \sqrt { 2 } } { 2 } } } & { { 1 } } & { { - \frac { \sqrt { 2 } } { 2 } } } \\ { { 0 } } & { { - \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } \end{array} \right] .
$$

One iteration of the QR method is complete. Since neither $b _ { 2 } ^ { ( 2 ) } = \sqrt { 2 } / 2 \operatorname { n o r } b _ { 3 } ^ { ( 2 ) } = - \sqrt { 2 } / 2$ is small,another iteration of the QR method is performed. For this iteration, we calculate the eigenvalues $\textstyle { \frac { 1 } { 2 } } \pm { \frac { 1 } { 2 } } { \sqrt { 3 } }$ of the matrix

$$
\begin{array} { r } { \left[ \begin{array} { c c } { a _ { 2 } ^ { ( 2 ) } } & { b _ { 3 } ^ { ( 2 ) } } \\ { b _ { 3 } ^ { ( 2 ) } } & { a _ { 3 } ^ { ( 2 ) } } \end{array} \right] = \left[ \begin{array} { c c } { 1 } & { - \frac { \sqrt { 2 } } { 2 } } \\ { - \frac { \sqrt { 2 } } { 2 } } & { 0 } \end{array} \right] , } \end{array}
$$

and choose $\begin{array} { r } { s _ { 2 } = \frac { 1 } { 2 } - \frac { 1 } { 2 } \sqrt { 3 } } \end{array}$ , the closest eigenvalue to $a _ { 3 } ^ { ( 2 ) } = 0$ . Completing the calculations gives

$$
A ^ { ( 3 ) } = \left[ \begin{array} { c c c } { { 2 . 6 7 2 0 2 7 7 } } & { { 0 . 3 7 5 9 7 4 4 8 } } & { { 0 } } \\ { { 0 . 3 7 5 9 7 4 4 8 } } & { { 1 . 4 7 3 6 0 8 0 } } & { { 0 . 0 3 0 3 9 6 9 6 4 } } \\ { { 0 } } & { { 0 . 0 3 0 3 9 6 9 6 4 } } & { { - 0 . 0 4 7 5 5 9 5 3 0 } } \end{array} \right] .
$$

If $b _ { 3 } ^ { ( 3 ) } = 0 . 0 3 0 3 9 6 9 6 4$ is suffciently small, ten the approximation to theeigenvalue $\lambda _ { 3 }$ is 1.5864151, the sum of ${ a _ { 3 } } ^ { ( 3 ) }$ and the shifts $s _ { 1 } + s _ { 2 } = 2 + ( 1 - \sqrt { 3 } ) / 2$ . Deleting the third row and column gives

$$
A ^ { ( 3 ) } = \left[ { \begin{array} { c c } { 2 . 6 7 2 0 2 7 7 } & { 0 . 3 7 5 9 7 4 4 8 } \\ { 0 . 3 7 5 9 7 4 4 8 } & { 1 . 4 7 3 6 0 8 0 } \end{array} } \right] ,
$$