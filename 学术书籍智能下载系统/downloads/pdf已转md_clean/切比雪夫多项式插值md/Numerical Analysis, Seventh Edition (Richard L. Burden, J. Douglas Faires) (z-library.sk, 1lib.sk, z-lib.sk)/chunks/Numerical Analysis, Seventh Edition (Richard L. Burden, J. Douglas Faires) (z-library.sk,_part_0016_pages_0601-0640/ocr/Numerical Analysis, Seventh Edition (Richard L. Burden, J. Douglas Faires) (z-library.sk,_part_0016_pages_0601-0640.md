which has eigenvalues $\mu _ { 1 } = 2 . 7 8 0 2 1 4 0$ and $\mu _ { 2 } = 1 . 3 6 5 4 2 1 8$ . Adding the shifts gives the approximations

$$
\lambda _ { 1 } \approx 4 . 4 1 4 1 8 8 6 \quad \mathrm { a n d } \quad \lambda _ { 2 } \approx 2 . 9 9 9 3 9 6 4 .
$$

Since the actual eigenvalues of the matrix A are 4.41420, 3.00000,and 1.58579, the QR method gave four significant digits of accuracy in only two iterations.

Algorithm 9.6 implements the QR method.

# QR

To obtain the eigenvalues of the symmetric, tridiagonal $n \times n$ matrix

$$
A \equiv A _ { 1 } = \left[ \begin{array} { l l l l l } { a _ { 1 } ^ { ( 1 ) } } & { b _ { 2 } ^ { ( 1 ) } } & { 0 . . . . } & { . . . } & { . } \\ { b _ { 2 } ^ { ( 1 ) } } & { a _ { 2 } ^ { ( 1 ) } } & { . . . } & { . . } & { . } \\ { 0 . . . } & { a _ { 2 } ^ { ( 1 ) } . . . } & { . . } & { . . } & { . . } \\ { . . . } & { . . . } & { . . . } & { . . } & { . } \\ { . . . } & { . . . } & { . . . } & { . . } & { . } \\ { . } & { . . . } & { . . . } & { . . } & { . } \\ { 0 . . . . } & { . . . } & { . . } & { . } & { a _ { n } ^ { ( 1 ) } } \end{array} \right]
$$

INPUT $n ; a _ { 1 } ^ { ( 1 ) } , \ldots , a _ { n } ^ { ( 1 ) } , b _ { 2 } ^ { ( 1 ) } , \ldots , b _ { n } ^ { ( 1 ) }$ ; tolerance TOL； maximum number of itera-tions $M$ .

OUTPUTeigenvalues of A,or recommended splitting of A, or a message that the maxi-mum number of iterations was exceeded.

Step 1 Set $k = 1$ ； $S H I F T = 0$ (Accumulated shift.)

Step 2 While $k \leq M$ do Steps 3-19. (Steps 3-7 test for success.)

Step 3 If |b)| ≤TOL then set λ = ak）+SHIFT;OUTPUT $( \lambda )$ ；set $n = n - 1$ ，

Step 4 If $| b _ { 2 } ^ { ( k ) } | \leq T O L$ then set $\lambda = a _ { 1 } ^ { ( k ) } + S H I F T ;$

Step 5If $n = 0$ then STOP.

Step $\sigma$ If $n = 1$ then set $\lambda = a _ { 1 } ^ { ( k ) } + S H I F T ;$ OUTPUT (λ); STOP.

Step 7For $j = 3 , \ldots , n - 1$ if $| b _ { j } ^ { ( k ) } | \leq T O L$ then OUTPUT ('split int', $a _ { 1 } ^ { ( k ) } , \ldots , a _ { j - 1 } ^ { ( k ) } , b _ { 2 } ^ { ( k ) } , \ldots , b _ { j - 1 } ^ { ( k ) } ,$ ‘and', $a _ { j } ^ { ( k ) } , \ldots , a _ { n } ^ { ( k ) } , b _ { j + 1 } ^ { ( k ) } , \ldots , b _ { n } ^ { ( k ) } , S H I F T ) ;$ STOP.

Step 8 (Compute shift.)

$$
\begin{array} { l } { { c = a _ { n } ^ { ( k ) } a _ { n - 1 } ^ { ( k ) } - \left[ b _ { n } ^ { ( k ) } \right] ^ { 2 } ; } } \\ { { d = ( b ^ { 2 } - 4 c ) ^ { 1 / 2 } . } } \end{array}
$$

Step 9If $b > 0$ then set $\mu _ { 1 } = - 2 c / ( b + d )$

$\mu _ { 2 } = - ( b + d ) / 2$ else set $\mu _ { 1 } = ( d - b ) / 2$ $\mu _ { 2 } = 2 c / ( d - b ) .$

Step 10 If $n = 2$ then set $\lambda _ { 1 } = \mu _ { 1 } + S H I F T ;$

$$
\lambda _ { 2 } = \mu _ { 2 } + S H I F T ;
$$

Step 11 Choose s so that $\lvert s - a _ { n } ^ { ( k ) } \rvert = \operatorname* { m i n } \{ \lvert \mu _ { 1 } - a _ { n } ^ { ( k ) } \rvert , \lvert \mu _ { 2 } - a _ { n } ^ { ( k ) } \rvert \} .$

Step 12 (Accumulate the shift.) Set $S H I F T = S H I F T + s$

Step 13 (Perform shift.) F ${ \mathrm { o r ~ } } j = 1 , \ldots , n , { \mathrm { s e t } } d _ { j } = a _ { j } ^ { ( k ) } - s .$

Step 14 (Steps 14 and 15 compute $R ^ { ( k ) }$ ）Set $x _ { 1 } = d _ { 1 }$ ；$y _ { 1 } = b _ { 2 }$

Step 15For $j = 2 , \ldots , n$

$$
\begin{array} { r l r } {  { \sec { z _ { j - 1 } } = \{ x _ { j - 1 } ^ { 2 } + [ b _ { j } ^ { ( k ) } ] ^ { 2 } \} ^ { 1 / 2 } ; } } \\ & { } & \\ & { c _ { j } = \frac { x _ { j - 1 } } { z _ { j - 1 } } ; } \\ & { } & \\ & { s _ { j } = \frac { b _ { j } ^ { ( k ) } } { z _ { j - 1 } } ; } \\ & { } & \\ & { q _ { j - 1 } = c _ { j } y _ { j - 1 } + s _ { j } d _ { j } ; } \\ & { } & \\ & { x _ { j } = - s _ { j } y _ { j - 1 } + c _ { j } d _ { j } ; } \end{array}
$$

$j \neq n$ then set $r _ { j - 1 } = s _ { j } b _ { j + 1 } ^ { ( k ) }$

$$
y _ { j } = c _ { j } b _ { j + 1 } ^ { ( k ) } .
$$

$\left( A _ { j } ^ { ( k ) } = P _ { j } A _ { j - 1 } ^ { ( k ) } \right.$ has just be computd and $R ^ { ( k ) } = A _ { n } ^ { ( k ) }$

Step 16 (Steps 16-18 compute $A ^ { ( k + 1 } .$ ）

$$
\begin{array} { l } { { a _ { 1 } ^ { ( k + 1 ) } = s _ { 2 } q _ { 1 } + c _ { 2 } z _ { 1 } ; } } \\ { { b _ { 2 } ^ { ( k + 1 ) } = s _ { 2 } z _ { 2 } . } } \end{array}
$$

Step 17For $j = 2 , 3 , \dots , n - 1$

$$
b _ { j + 1 } ^ { ( k + 1 ) } = s _ { j + 1 } z _ { j + 1 } .
$$

Step 18 Set $a _ { n } ^ { ( k + 1 ) } = c _ { n } z _ { n }$

Step 19 Set $k = k + 1$

Step 20 OUTPUT(Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

A similar procedure can be used to find approximations to the eigenvalues of a non-symmetric $n \times n$ matrix. The matrix is first reduced to a similar upper-Hessenberg matrix $H$ using the Householder Algorithm for nonsymmetric matrices.

The QR factoring process assumes the following form. First

$$
H \equiv H ^ { ( 1 ) } = { { \cal Q } ^ { ( 1 ) } } { \cal R } ^ { ( 1 ) } .
$$

Then $H ^ { ( 2 ) }$ is defined by

$$
H ^ { ( 2 ) } = R ^ { ( 1 ) } Q ^ { ( 1 ) }
$$

and factored into

$$
H ^ { ( 2 ) } = { Q } ^ { ( 2 ) } R ^ { ( 2 ) } .
$$

The method of factoring proceeds with the same aim as the QR Algorithm. The matrices are chosen to introduce zeros at appropriate entries of the matrix,and a shifting procedure is used similar to that in the QR method.However, the shifting is somewhat more complicated for nonsymmetric matrices since complex eigenvalues with the same modulus can occur. The shifting process modifies the calculations in Eqs. (9.19), (9.20), and (9.21)to obtain the double QR method $H ^ { ( 1 ) } - s _ { 1 } I = { Q } ^ { ( 1 ) } R ^ { ( 1 ) }$ ， $H ^ { ( 2 ) } = R ^ { ( 1 ) } { \cal Q } ^ { ( 1 ) } + s _ { 1 } I ,$ ， $H ^ { ( 2 ) } - s _ { 2 } I = { Q } ^ { ( 2 ) } R ^ { ( 2 ) }$ , and $H ^ { ( 3 ) } = R ^ { ( 2 ) } \mathcal { Q } ^ { ( 2 ) } + s _ { 2 } I$ , where ${ \pmb S } _ { \mathbf { i } }$ and $\pmb { S } _ { 2 }$ are complex conjugates and $H ^ { ( 1 ) }$ ， $H ^ { ( 2 ) }$ ,... are real upper-Hessenberg matrices.

A complete description of the QR method can be found in [Wil2]. Detailed algorithms and programs for this method and most other commonly employed methods are given in [WR]. We refer the reader to these works if the method we have discussed does not give satisfactory results.

The QR method can be performed in a manner that wil produce the eigenvectors of a matrix as well as its eigenvalues, but Algorithm 9.6 has not been designed to accomplish this. If the eigenvectors of a symmetric matrix are needed as well as the eigenvalues, we suggest either using the Inverse Power method after Algorithms 9.5 and 9.6 have been employed or using one of the more powerful techniques listed in [WR].

# Exercise set 9.4

1.Apply two iterations of the QR Algorithm to the following matrices.

$\begin{array} { r l } { \mathrm { a . } \ } & { { } \left[ \begin{array} { r r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right] } \\ { \mathrm { c . } \ } & { { } \left[ \begin{array} { r r r r } { 4 } & { - 1 } & { 0 } \\ { - 1 } & { 3 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right] } \end{array}$ b. d. $\left[ { \begin{array} { r r r r } { 1 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 4 } \end{array} } \right]$   
e. $\left[ { \begin{array} { r r r r r } { - 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { - 3 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 3 } \end{array} } \right]$ f. $\left[ \begin{array} { l l l l } { 0 . 5 } & { 0 . 2 5 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 0 . 8 } & { 0 . 4 } & { 0 } \\ { 0 } & { 0 . 4 } & { 0 . 6 } & { 0 . 1 } \\ { 0 } & { 0 } & { 0 . 1 } & { 1 } \end{array} \right]$

2.Use the QR Algorithm to determine,to within $1 0 ^ { - 5 }$ ,all the eigenvalues of the following matrices.

a. $\left[ { \begin{array} { r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { - 1 } & { - 2 } \\ { 0 } & { - 2 } & { 3 } \end{array} } \right]$ b. [ 1 ] c. $\left[ { \begin{array} { l l l l l } { 4 } & { 2 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 4 } & { 2 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 4 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } & { 4 } & { 2 } \\ { 0 } & { 0 } & { 0 } & { 2 } & { 4 } \end{array} } \right]$ $\mathbf { d . } \left[ \begin{array} { c c c c c c } { 5 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 4 . 5 } & { 0 . 2 } & { 0 } & { 0 } \\ { 0 } & { 0 . 2 } & { 1 } & { - 0 . 4 } & { 0 } \\ { 0 } & { 0 } & { - 0 . 4 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 3 } \end{array} \right]$

3.Use the QR Algorithm to determine,to within $1 0 ^ { - 5 }$ , all the eigenvalues for the matrices given in Exercise 1.

4.Use the Inverse Power method to determine, to within $1 0 ^ { - 5 }$ , the eigenvectors of the matrices in Exercise 1.

5.a.Show that the rotation matrix $\left[ \begin{array} { l l } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \phantom { - } \cos \theta } \end{array} \right]$ applied to the vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } ) ^ { t }$ has the geometric effect of rotating $\pmb { \mathrm { x } }$ through the angle $\theta$ without changing its magnitude with respect to $\| \cdot \| _ { 2 }$ b. Show that the magnitude of $\pmb { \mathrm { x } }$ with respect to $\| \cdot \| _ { \infty }$ can be changed by a rotation matrix.

6. Let $P$ be the rotation matrix with $p _ { i i } = p _ { j j } = \cos \theta$ and $p _ { i j } = - p _ { j i } = \sin \theta$ ,for $j < i$ . Show that for any $n \times n$ matrix A:

$$
\begin{array} { r l } & { ( A P ) _ { p q } = \left\{ \begin{array} { l l } { a _ { p q } , } & { \mathrm { i f ~ } q \neq i , j , } \\ { ( \cos { \theta } ) a _ { p j } + ( \sin { \theta } ) a _ { p i } , } & { \mathrm { i f ~ } q = j , } \\ { ( \cos { \theta } ) a _ { p i } - ( \sin { \theta } ) a _ { p j } , } & { \mathrm { i f ~ } q = i . } \end{array} \right. } \\ & { ( P A ) _ { p q } = \left\{ \begin{array} { l l } { a _ { p q } , } & { \mathrm { i f ~ } p \neq i , j , } \\ { ( \cos { \theta } ) a _ { j q } - ( \sin { \theta } ) a _ { i q } , } & { \mathrm { i f ~ } p = j , } \\ { ( \sin { \theta } ) a _ { j q } + ( \cos { \theta } ) a _ { i q } , } & { \mathrm { i f ~ } p = i . } \end{array} \right. } \end{array}
$$

7.Show that the product of an upper triangular matrix (on the left) and an upper Hessenberg matrix produces an upper Hessenberg matrix.

8.Let $P _ { k }$ denote a rotation matrix of the form given in (9.16).

a. Show that $P _ { 2 } ^ { t } P _ { 3 } ^ { t }$ differs from an upper triangular matrix only in at most the (2,1) and (3,2) positions.   
b. Assume that $P _ { 2 } ^ { i } P _ { 3 } ^ { t } \cdots P _ { k } ^ { t }$ differs from an upper triangular matrix only in at most the (2,1), (3,2),  , $( k , k - 1 )$ positions. Show that $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k } ^ { t } P _ { k + 1 } ^ { t }$ differs from an upper triangular matrix only in at most the (2,1), (3,2),..., $( k , k - 1 )$ ， $( k + 1 , k )$ positions.   
c. Show that the matrix $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdots P _ { n } ^ { t }$ is upper Hessenberg.

9.Jacobi's method for a symmetric matrix $\pmb { A }$ is described by

$$
\begin{array} { l } { { A _ { 1 } = A , } } \\ { { \ } } \\ { { A _ { 2 } = P _ { 1 } A _ { 1 } P _ { 1 } ^ { t } } } \end{array}
$$

and, in general,

$$
{ \bf \mu } , \qquad { \bf A } _ { i + 1 } = P _ { i } A _ { i } P _ { i } ^ { t } .
$$

The matrix $A _ { i + 1 }$ tends to a diagonal matrix, where $P _ { i }$ is a rotation matrix chosen to eliminate a large off-diagonal element in $A _ { i }$ . Suppose $a _ { j , k }$ and $a _ { k , j }$ are to be set to O, where $j \neq k$ .If $a _ { j j } \neq a _ { k k }$ ，then

$$
( P _ { i } ) _ { j j } = ( P _ { i } ) _ { k k } = \sqrt { \frac { 1 } { 2 } \left( 1 + \frac { b } { \sqrt { c ^ { 2 } + b ^ { 2 } } } \right) } ,
$$

$$
( P _ { i } ) _ { k j } = { \frac { c } { 2 ( P _ { i } ) _ { j j } \sqrt { c ^ { 2 } + b ^ { 2 } } } } = - ( P _ { i } ) _ { j k } ,
$$

where

$$
c = 2 a _ { j k } \thinspace \mathrm { s g n } ( a _ { j j } - a _ { k k } ) \quad \mathrm { a n d } \quad b = | a _ { j j } - a _ { k k } | ,
$$

or if $a _ { j j } = a _ { k k }$

$$
( P _ { i } ) _ { j j } = ( P _ { i } ) _ { k k } = \frac { \sqrt { 2 } } { 2 }
$$

and

$$
( P _ { i } ) _ { k j } = - ( P _ { i } ) _ { j k } = \frac { \sqrt { 2 } } { 2 } .
$$

Develop an algorithm to implement Jacobi's method by seting $a _ { 2 1 } = 0$ . Then set $a _ { 3 1 } , a _ { 3 2 } , a _ { 4 1 }$ ， $a _ { 4 2 } , a _ { 4 3 } , \dots , a _ { n , 1 } , \dots , a _ { n , n - 1 }$ in turn to zero. This is repeated until a matrix $A _ { k }$ is computed

with

$$
\sum _ { i = 1 } ^ { n } \sum _ { { j = 1 } \atop { j \not = i } } ^ { n } | a _ { i j } ^ { ( k ) } |
$$

sufficiently small. The eigenvalues of $A$ can then be approximated by the diagonal entries of $A _ { k }$

10.Repeat Exercise 3 using the Jacobi method.

11.In the lead example of this chapter, the linear system $A \mathbf { w } = - 0 . 0 4 ( \rho / p ) \lambda \mathbf { w }$ must be solved for w and $\lambda$ in order to approximate the eigenvalues $\lambda _ { k }$ of the Strum-Liouville system.

a.Find all four eigenvalues $\mu _ { 1 } , \ldots , \mu _ { 4 }$ of the matrix

$$
A = \left[ { \begin{array} { r r r r } { 2 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { 2 } \end{array} } \right]
$$

to within $1 0 ^ { - 5 }$

b.Approximate the eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { 4 }$ of the system in terms of $\rho$ and $p$

12.The $( m - 1 ) \times ( m - 1 )$ tridiagonal matrix

$$
A = \left[ \begin{array} { l } { 1 - 2 \alpha \qquad \alpha \qquad 0 \div \cdots \cdots \cdots 0 } \\ { \vdots \qquad \vdots } \\ { \alpha \cdot \qquad 1 - 2 \alpha \quad \alpha \qquad \ddots \qquad \vdots } \\ { \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } \\ { \vdots \qquad \ddots \qquad \ddots \qquad \ddots \qquad \ddots \qquad \vdots } \\ { \vdots \qquad \ddots \qquad \ddots \qquad \ddots \qquad \ddots \qquad \ddots } \\ { \vdots \qquad \ddots \qquad \ddots \qquad \cdot \cdot \cdot \cdot \cdot } \\ { \vdots \qquad \vdots \qquad \ddots \qquad \ddots \qquad \cdot \cdot \cdot \cdot \cdot } \\ { \partial \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \alpha \qquad \overset { . } { \overbrace { 1 } } ^ { \cdot } - 2 \alpha } \end{array} \right]
$$

is involved in the Forward Diference method to solve the heat equation (scc Scction 12.2). For the stability of the method we need $\rho ( A ) < 1$ . With $m = 1 1$ , approximate the eigenvalues of $A$ for each of the following.

a. $\alpha = \frac { 1 } { 4 }$ $\mathbf { b . } \quad \alpha = { \frac { 1 } { 2 } }$ $\mathbf { c } . \quad \alpha = \frac { 3 } { 4 }$

When is the method stable?

13.The eigenvalues of the matrix $A$ in Exercise 12 are

$$
\lambda _ { i } = 1 - 4 \alpha \left( \sin \frac { \pi i } { 2 m } \right) ^ { 2 } , \quad \mathrm { f o r } i = 1 , \dots , m - 1 .
$$

Compare the approximations in Exercise 12 to the actual eigenvalues. Again, when is the method stable?

# 9.5 Survey of Methods and Software

This chapter discussed the approximation of eigenvalues and eigenvectors. The Gerschgorin circles give a crude approximation to the location of the eigenvalues of a matrix. The Power method can be used to find the dominant eigenvalue and an associated eigen-vector for an arbitrary matrix $A$ .If $A$ is symmetric,the Symmetric Power method gives faster convergence to the dominant eigenvalue and an associated eigenvector. The Inverse Power method will find the eigenvalue closest to a given value and an associated eigenvector. This method is often used to refine an approximate eigenvalue and to compute an eigenvector once an eigenvalue has been found by some other technique.

Deflation methods,such as Wielandt deflation, obtain other eigenvalues once the dom-inant eigenvalue is known. These methods are used if only a few eigenvalues are required since they are susceptible to roundoff error. The Inverse Power method should be used to improve the accuracy of approximate eigenvalues obtained from a deflation technique.

Methods based on similarity transformations, such as Householder's method,are used to convert a symmetric matrix into a similar matrix that is tridiagonal (or upper Hessenberg if the matrix is not symmetric). Techniques such as the QR method can then be applied to the tridiagonal (or upper-Hessenberg) matrix to obtain approximations to all the eigenvalues.The associated eigenvectors can be found by using an iterative method,such as the Inverse Power method,or by modifying the QR method to include the approximation of eigenvectors.We restricted our study to symmetric matrices and presented the QR method only to compute eigenvalues for the symmetric case.

The subroutines in the IMSL and NAG libraries are based on those contained in EIS-PACK and LAPACK, packages that were discussed in Section 1.4. In general, the subroutines transform a matrix into the appropriate form for the QR method or one of its modifications, such as the QL method.The subroutines approximate all the eigenvalues and can approximate an associated eigenvector for each eigenvalue. There are special routines that find all the eigenvalues within an interval or region or that find only the largest or smallest eigenvalue. Subroutines are also available to determine the accuracy of the eigenvalue approximation and the sensitivity of the process to roundoff error.

The LAPACK routine SGEBAL prepares a real nonsymmetric matrix $A$ for further processing. It tries to use permutation matrices to transform $A$ to a similar block upper triangular form. Similarity transformations are used to balance the rows and columns in norm. The routine SGEHRD can then be used to convert A to a similar upper Hessenberg matrix $H$ . The matrix $H$ is then reduced via SHSEQR to Schur form $S T S ^ { t }$ ,where $S$ is orthogonal and the diagonal of $T$ holds the eigenvalues of $A$ . STREVC can then be used to obtain the corresponding eigenvectors.

The LAPACK routine SSYTRD is used to reduce a real symmetric matrix $A$ to a similar tridiagonal matrix via Householder's method. The routine SSTEQR uses an implicity shifted QR algorithm to obtain all the eigenvalues and eigenvectors of $A$ ·

The IMSL subroutine EVLRG produces all eigenvalues of $A$ in increasing order of magnitude.This subroutine first balances the matrix A using a version of the EISPACK routine BALANC,so that the sums of the magnitudes of the entries in each row and in each column are approximately the same. This leads to greater stability in the ensuing computations.EVLRG next performs orthogonal similarity transformations,such as in Householder's method, to reduce A to a similar upper Hessenberg matrix. This portion is similar to the EISPACK subroutine ORTHES.Finally, the shifted QR algorithm is performed to obtain all the eigenvalues.This part is similar to the subroutine HQR in EISPACK.The IMSL subroutine EVCRG is the same as EVRLG, except that corresponding eigenvec-tors are computed. The subroutine EVLSF computes the eigenvalues of the real symmetric matrix A.The matrix A is first reduced to tridiagonal form using a modification of the EISPACK routine TRED2. Then the eigenvalues are computed using a modification of the EISPACK routine IMTQL2, which is a variation of the QR method called the implicit QL method. The subroutine EVCSF is the same as EVLSF except that the eigenvectors are also calculated. Finally, EVLRH and EVCRH compute all eigenvalues of the upper Hessenberg matrix A and,additionally,EVCRH computes the eigenvectors.These subroutines are based on the subroutines HQR and HQR2, respectively, in EISPACK.

The NAG library has similar subroutines based on the EISPACK routines. The subroutine FO2EBF computes the eigenvalues of a real matrix and, optionally, the eigenvectors. The matrix is first balanced and then is reduced to upper-Hessenberg form for the QR method. If only the eigenvalues are required, then the algorithm uses a Hessenberg QR method to compute the eigenvalues; if the eigenvectors are also required,then a Schur factorization is used. The subroutine FO2FAF is used on a real symmetric matrix to compute the eigenvalues in increasing order of magnitude and optionally the eigenvectors. The subroutine first reduces the matrix to tridiagonal form using Householder's method. The eigenvalues are then computed using a variant of the symmetric tridiagonal QR algorithm. The subroutine FO8FEF implements Householder's algorithm directly for symmetric matrices to produce a similar tridiagonal symmetric matrix. Routines are also available in the NAG library for directly balancing real matrices,recovering eigenvectors if a matrix was first balanced, and performing other operations on special types of matrices.

The Maple procedure Eigenvals (A); computes the eigenvalues of $A$ by first balanc-ing and then transforming A to upper Hessenberg form. The QR method is then applied to obtain all eigenvalues and eigenvectors. The tridiagonal form, as in Algorithm 9.6, is used for a symmetric matrix.

The MATLAB procedure eig computes the eigenvalues and, optionally, eigenvectors of $A$ by using the EISPACK routines. It uses BALANC to balance the matrix, ORTHES to transform the matrix to upper Hessenberg,and finally a modified HQR2 routine to find the eigenvalues and, optionally, the eigenvectors of a real upper Hessenberg matrix by the QR method. MATLAB also has a procedure eigs that computes a selected number of eigenvalues and eigenvectors. The procedure eigs is based on the implicitly restarted Arnoldi method by Sorensen [So]. The software package contained in Netlib, ARPACK [ARP] to solve large sparse eigenvalue problems,is also based on the implicitly restarted Arnoldi method.The implicitly restarted Arnoldi method is a Krylov subspace method that finds a sequence of Krylov subspaces that converge to a subspace containing the eigenvalues.

The books by Wilkinson [Wil2] and Wilkinson and Reinsch [WR] are classcs in the study of eigenvalue problems. Stewart [Stew2] is also a good source of information on the general problem, and Parlett [Par] considers the symmetric problem. A study of the nonsymmetric problem can be found in Saad [Sa1].

CHAPTER

10

# Numerical Solutions of Nonlinear Systems of Equations

homogeneous soil lying above a hard base soil can be predicted by the amount of pressure required to sink smaller objects in the same soil. Specifically, the amount of pressure $\pmb { p }$ to sink a circular plate of radius r a distance d in the soft soil, where the hard base soil lies a distance $D > d$ below the surface, can be approximated by an equation of the form

$$
p = k _ { 1 } e ^ { k _ { 2 } r } + k _ { 3 } r ,
$$

where $k _ { 1 } , k _ { 2 }$ , and $\pmb { k _ { 3 } }$ are constants depending on $\pmb { d }$ and the consistency of the soil, but not on the radius of the plate.

To determine the minimal size of plate required to sustain a large load, three small plates with differing radi are sunk to the same distance, and the loads required for this sinkage are recorded, as shown in the accompanying figure.

This produces the three nonlinear equations

$$
\begin{array} { r } { m _ { 1 } = k _ { 1 } e ^ { k _ { 2 } r _ { 1 } } + k _ { 3 } r _ { 1 } , } \\ { m _ { 2 } = k _ { 1 } e ^ { k _ { 2 } r _ { 2 } } + k _ { 3 } r _ { 2 } , } \\ { m _ { 3 } = k _ { 1 } e ^ { k _ { 2 } r _ { 3 } } + k _ { 3 } r _ { 3 } , } \end{array}
$$

![](images/8f8415867e2be2971ac0652ee9d8be2c4ca42fc3a1ba81a61bf01aee52632e99.jpg)

![](images/957dc450910b755829084e3fe18c478c914447c214e2b3fb6f75ab1647bdd3bd.jpg)

in the three unknowns $k _ { 1 } , k _ { 2 } ,$ and $k _ { 3 }$ . Numerical approximation methods are usually needed for solving systems of equations when the equations are nonlinear. Exercise 10 of Section 10.2 concerns an application of the type described here.

Solving a system of nonlinear equations is a problem that is avoided when possible, customarily by approximating the nonlinear system by a system of linear equations.When this is unsatisfactory, the problem must be tackled directly. The most straightforward ap-proach is to adapt the methods from Chapter 2, which approximate the solutions of a single nonlinear equation in one variable,to apply when the single-variable problem is replaced by a vector problem that incorporates all the variables.

The principal tool in Chapter 2 was Newton's method, a technique that is generally quadratically convergent. This is the first technique we modify to solve systems of nonlinear equations.Newton's method, as modified for systems of equations,is quite costly to apply,so in Section 10.3 we describe how a modified Secant method can be used to obtain approximations more easily,although with a loss of the extremely rapid convergence that Newton's method provides.

Section 10.4 describes the method of Steepest Descent. It is only linearly conver-gent, but it does not require the accurate starting approximations needed for more rapidly converging techniques. It is often used to find a good initial approximation for Newton's method or one of its modifications.

In Section 10.5,we give an introduction to continuation methods,which use a parameter to move from a problem with an easily determined solution to the solution of the original nonlinear problem.

Most of the proofs of the theoretical results in this chapter are omited since they involve methods that are usually studied in advanced calculus.A good general reference for this material is Ortega's book entitled Numerical Analysis-A Second Course [Or2]. A more complete reference is [OR].

# 10.1Fixed Points for Functions of Several Variables

A system of nonlinear equations has the form

$$
\begin{array} { r l r } & { } & { f _ { 1 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \\ & { } & { f _ { 2 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \\ & { } & { \vdots \qquad \vdots } \\ & { } & { f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \end{array}
$$

where each function $f _ { i }$ can be thought of as mapping a vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ of the $\pmb { n }$ -dimensional space $\mathbb { R } ^ { n }$ into the real line $\mathbb { R }$ . A geometric representation of a nonlinear system when $n = 2$ is given in Figure 10.1.

![](images/0304b6abe8628b1a1f64029cbbc22c5c8ea145a4357e6ddf7e7293d92b990771.jpg)  
Figure 10.1

This system of $\pmb { n }$ nonlinear equations in $\pmb { n }$ unknowns can also be represented by defin-ing a function $\mathbf { F }$ mapping $\mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ as

$$
{ \bf F } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = ( f _ { 1 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) , f _ { 2 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) , \ldots , f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) , \ldots , f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ) .
$$

If vector notation is used to represent the variables $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ ,system (10.1) assumes the form

$$
\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 } { \mathrm { . } }
$$

The functions $f _ { 1 } , f _ { 2 } , \ldots , f _ { n }$ are the coordinate functions of $\mathbf { F }$

The $3 \times 3$ nonlinear system

$$
3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \frac { 1 } { 2 } = 0 ,
$$

$$
\begin{array} { r } { x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { \displaystyle e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \frac { 1 0 \pi - 3 } { 3 } = 0 } \end{array}
$$

can be placed in the form (10.2) by defining the three coordinate functions $f _ { 1 } , f _ { 2 }$ ，and $f _ { 3 }$ from ${ \mathbb { R } } ^ { 3 }$ to $\mathbb { R }$ as

$$
\begin{array} { l } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \displaystyle 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \frac 1 2 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 , } \\ { f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \frac { 1 0 \pi - 3 } { 3 } , } \end{array}
$$

and then defining $\mathbf { F }$ from $\mathbb { R } ^ { 3 } \to \mathbb { R } ^ { 3 }$ by

$$
{ \begin{array} { r l } & { \mathbf { F } ( \mathbf { x } ) = \mathbf { F } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) } \\ & { \qquad = ( f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ) ^ { t } } \\ & { \qquad = \left( 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - { \cfrac { 1 } { 2 } } , x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 , \right. } \\ & { \qquad \left. e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + { \cfrac { 1 0 \pi - 3 } { 3 } } \right) ^ { t } . } \end{array} }
$$

Before discussing the solution of a system given in the form (10.1） or (10.2),we need some results concerning continuity and differentiability of functions from $\mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ ， Although this study could be presented directly (see Exercise 1O),we use an alternative method that allows us to present the more theoretically difficult concepts of limits and continuity in terms of functions from $\mathbb { R } ^ { n }$ into $\mathbb { R }$

Let $f$ be a function defined on a set $D \subset \mathbb { R } ^ { n }$ and mapping into $\mathbb { R }$ . The function $f$ is said to have the limit $L$ at ${ \bf x } _ { 0 }$ ,written

$$
\operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } f ( \mathbf { x } ) = L ,
$$

if, given any number $\varepsilon > 0$ ,a number $\delta > 0$ exists with

$$
| f ( \mathbf { x } ) - L | < \varepsilon ,
$$

whenever $\pmb { \mathrm { x } } \in \pmb { D }$ and

$$
0 < \lvert \lvert \mathbf { x } - \mathbf { x } _ { 0 } \rvert \rvert < \delta .
$$

The existence of a limit is independent of the particular vector norm being used, as discussed in Section 7.1. Any convenient norm can be used to satisfy the condition in this definition. The specific value of $\pmb { \delta }$ will depend on the norm chosen, but the existence of a $\delta$ is independent of the norm.

# Definition 10.2

Let $f$ be a function from a set $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R }$ . The function $f$ is continuous at $\mathbf { x } _ { 0 } \in \mathbf { \Omega } D$ provided $\scriptstyle \operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } f ( \mathbf { x } )$ exists and

$$
\operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } f ( \mathbf { x } ) = f ( \mathbf { x } _ { 0 } ) .
$$

Moreover, $f$ is continuous on a set $D$ if $f$ is continuous at every point of $D$ . This concept is expressed by writing $f \in C ( D )$ ·

We can now define the limit and continuity concepts for functions from $\textstyle { \mathbb { R } } ^ { n }$ into $\mathbb { R } ^ { n }$ by considering the coordinate functions from $\mathbb { R } ^ { n }$ into $\mathbb { R }$

Definition 10.3 Let $\mathbf { F }$ be a function from $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ of the form

$$
\mathbf { F } ( \mathbf { x } ) = ( f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { n } ( \mathbf { x } ) ) ^ { t } ,
$$

where $f _ { i }$ is a mapping from $\mathbb { R } ^ { n }$ into $\mathbb { R }$ for each $i$ . We define

$$
\operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } \mathbf { F } ( \mathbf { x } ) = \mathbf { L } = ( L _ { 1 } , L _ { 2 } , \dots , L _ { n } ) ^ { t } ,
$$

if and only if $\begin{array} { r } { \operatorname* { l i m } _ { \mathbf { x }  \mathbf { x } _ { 0 } } f _ { i } ( \mathbf { x } ) = L _ { i } } \end{array}$ , for each $i = 1 , 2 , \dots , n .$

The function $\mathbf { F }$ is continuous at ${ \bf x } _ { 0 } \in { \cal D }$ provided $\scriptstyle \operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } \mathbf { F } ( \mathbf { x } )$ exists and $\mathrm { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } }$ $\mathbf { F } ( \mathbf { x } ) \mathbf { \Psi } = \mathbf { F } ( \mathbf { x } _ { 0 } )$ . In addition, $\mathbf { F }$ is continuous on the set $D$ if $\mathbf { F }$ is continuous at each $\mathbf { x }$ in $D$ This concept is expressed by writng $\mathbf { F } \in C ( D )$ ·

For functions from $\mathbb { R }$ into $\mathbb { R }$ ， continuity can often be shown by demonstrating that the function is differentiable (see Theorem 1.6).Although this theorem generalizes to functions of several variables,the derivative (or total derivative) of a function of several variables is quite involved and will not be presented here. Instead we state the following theorem,which relates the continuity of a function of $\pmb { n }$ variables at a point to the partial derivatives of the function at the point.

# Theorem 10.4

Let $f$ be a function from $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R }$ and $\mathbf { x } _ { 0 } \in D$ . If constants $\delta > 0$ and $K > 0$ exist so that whenever $\| \mathbf { x } - \mathbf { x _ { 0 } } \| < \delta$ and $\mathbf { x } \in D$ , we have

$$
\left| { \frac { \partial f ( \mathbf { x } ) } { \partial x _ { j } } } \right| \leq K , \quad { \mathrm { f o r } } \operatorname { e a c h } j = 1 , 2 , \ldots , n ,
$$

then $f$ is continuous at ${ \bf x } _ { 0 }$

In Chapter 2,an iterative process for solving an equation $f ( x ) = 0$ was developed by first transforming the equation into the fixed-point form ${ \pmb x } = { \pmb g } ( { \pmb x } )$ . A similar procedure will be investigated for functions from $\mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$

Definition 10.5 A function $\mathbf { G }$ from $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ has a fixed point at $\pmb { \mathrm { p } } \in D$ if $\mathbf { G } ( \mathbf { p } ) = \mathbf { p }$ ·

The following theorem extends the Fixed-Point Theorem 2.3 to the n-dimensional case. This theorem is a special case of the Contraction Mapping Theorem, and its proof can be found in [Or2, p. 153].

# Theorem 10.6

Let $D = \{ ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) ^ { t } \mid a _ { i } \leq x _ { i } \leq b _ { i }$ , for each $i = 1 , 2 , \dots , n \ \}$ for some collection of constants $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and $b _ { 1 } , b _ { 2 } , \ldots , b _ { n }$ . Suppose $\mathbf { G }$ is a continuous function from $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ with the property that ${ \bf G } ( { \bf x } ) \in { \cal D }$ whenever $\textbf { x } \in \textbf { \textit { D } }$ . Then $\mathbf { G }$ has a fixed point in $D$

Suppose, in addition, that allthe component functions of $\mathbf { G }$ have continuous partial derivatives and a constant $K < 1$ exists with

$$
\left| \frac { \partial g _ { i } ( \mathbf { x } ) } { \partial x _ { j } } \right| \leq \frac { K } { n } , \quad \mathrm { w h e n e v e r ~ } \mathbf { x } \in D ,
$$

for each $j = 1 , 2 , \dots , n$ and each component function $g _ { i }$ . Then the sequence $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ defined by an arbitrarily selected $\mathbf { x } ^ { ( 0 ) }$ in $D$ and generated by

$$
\mathbf { x } ^ { ( k ) } = G ( \mathbf { x } ^ { ( k - 1 ) } ) , \quad \mathrm { f o r } \operatorname { e a c h } k \geq 1 ,
$$

converges to the unique fixed point $\pmb { \operatorname { \mathbf { p } } } \in D$ and

$$
\left\| \mathbf { x } ^ { ( k ) } - \mathbf { p } \right\| _ { \infty } \leq \frac { K ^ { k } } { 1 - K } \left\| \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right\| _ { \infty } .
$$

Consider the nonlinear system from Example 1 given by

$$
\begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \displaystyle \frac { 1 } { 2 } = 0 , } \\ { x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 . } \end{array}
$$

If the ith equation is solved for $x _ { i }$ , the system is changed into the fixed-point problem

$$
\begin{array} { l } { \displaystyle x _ { 1 } = \frac 1 3 \cos ( x _ { 2 } x _ { 3 } ) + \frac 1 6 , } \\ { \displaystyle x _ { 2 } = \frac 1 9 \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } - 0 . 1 , } \\ { \displaystyle x _ { 3 } = - \frac 1 { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } - \frac { 1 0 \pi - 3 } { 6 0 } . } \end{array}
$$

Let $\mathbf { G } : \mathbb { R } ^ { 3 }  \mathbb { R } ^ { 3 }$ be defined by $\mathbf { G } ( \mathbf { x } ) = ( g _ { 1 } ( \mathbf { x } ) , g _ { 2 } ( \mathbf { x } ) , g _ { 3 } ( \mathbf { x } ) ) ^ { t }$ ,where

$$
\begin{array} { l } { \displaystyle { g _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \frac { 1 } { 3 } \cos ( x _ { 2 } x _ { 3 } ) + \frac { 1 } { 6 } , } } \\ { \displaystyle { g _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \frac { 1 } { 9 } \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } - 0 . 1 , } } \\ { \displaystyle { g _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = - \frac { 1 } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } - \frac { 1 0 \pi - 3 } { 6 0 } . } } \end{array}
$$

Theorems 10.4 and 10.6 willbe used to show that $\mathbf { G }$ has a unique fixed point in

$$
D = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } | \longrightarrow ^ { 1 } \leq x _ { i } \leq 1 , \quad \mathrm { f o r } \cosh i = 1 , 2 , 3 \} .
$$

For $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t }$ in $D$ ，

$$
\begin{array} { l } { \displaystyle \left. \begin{array} { l } { \displaystyle { g _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) | \le \frac { 1 } { 3 } | \cos ( x _ { 2 } x _ { 3 } ) | + \frac { 1 } { 6 } \le 0 . 5 0 , } } \\ { \displaystyle { g _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) | = \left| \frac { 1 } { 9 } \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } - 0 . 1 \right| \le \frac { 1 } { 9 } \sqrt { 1 + \sin 1 + 1 . 0 6 } - 0 . 1 < 0 . 0 } } \end{array} \right. } \end{array}
$$

and

$$
| g _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) | = \frac { 1 } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } + \frac { 1 0 \pi - 3 } { 6 0 } \le \frac { 1 } { 2 0 } e + \frac { 1 0 \pi - 3 } { 6 0 } < 0 . 6 1 ;
$$

$\mathbf { s o } - 1 \leq g _ { i } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) \leq 1$ ,for each $i = 1$ ,2, 3. Thus, $\mathbf { G } ( \mathbf { x } ) \in D$ whenever $\mathbf { x } \in D$

Finding bounds for the partial derivatives on $D$ gives

$$
\left| \frac { \partial g _ { 1 } } { \partial x _ { 1 } } \right| = 0 , \quad \left| \frac { \partial g _ { 2 } } { \partial x _ { 2 } } \right| = 0 , \quad \mathrm { a n d } \quad \left| \frac { \partial g _ { 3 } } { \partial x _ { 3 } } \right| = 0 ,
$$

as well as

$$
\begin{array} { r l r } {  {  \frac { \partial g _ { 1 } } { \partial x _ { 2 } }  \leq \frac { 1 } { 3 } \vert x _ { 3 } \vert \cdot \vert \sin x _ { 2 } x _ { 3 } \vert \leq \frac { 1 } { 3 } \sin 1 < 0 . 2 8 1 , } } \\ & { } & \\ & { } & {  \frac { \partial g _ { 1 } } { \partial x _ { 3 } }  \leq \frac { 1 } { 3 } \vert x _ { 2 } \vert \cdot \vert \sin x _ { 2 } x _ { 3 } \vert \leq \frac { 1 } { 3 } \sin 1 < 0 . 2 8 1 , } \\ & { } & \\ & { } & {  \frac { \partial g _ { 2 } } { \partial x _ { 1 } }  = \frac { \vert x _ { 1 } \vert } { 9 \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } } < \frac { 1 } { 9 \sqrt { 0 . 2 1 8 } } < 0 . 2 3 8 , } \end{array}
$$

$$
\left| \frac { \partial g _ { 2 } } { \partial x _ { 3 } } \right| = \frac { | \cos x _ { 3 } | } { 1 8 \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } } < \frac { 1 } { 1 8 \sqrt { 0 . 2 1 8 } } < 0 . 1 1 9 ,
$$

$$
\left| \frac { \partial g _ { 3 } } { \partial x _ { 1 } } \right| = \frac { | x _ { 2 } | } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } \leq \frac { 1 } { 2 0 } e < 0 . 1 4 ,
$$

and

$$
\left| \frac { \partial g _ { 3 } } { \partial x _ { 2 } } \right| = \frac { | x _ { 1 } | } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } \leq \frac { 1 } { 2 0 } e < 0 . 1 4 .
$$

Since the partial derivatives of ${ \pmb { \cal B } } 1 , { \pmb { \cal g } } 2$ ,and $g _ { 3 }$ are bounded on $D$ ,Theorem 10.4 implies that these functions are continuous on $D$ . Consequently, $\mathbf { G }$ is continuous on $D$ . Moreover, for every $\pmb { \mathrm { x } } \in \pmb { D }$ ，

$$
\left. \frac { \partial g _ { i } ( \mathbf { x } ) } { \partial x _ { j } } \right. \le 0 . 2 8 1 , \quad \mathrm { f o r } \operatorname { e a c h } i = 1 , 2 , 3 \quad \mathrm { a n d } \quad j = 1 , 2 , 3 ,
$$

and the condition in the second part of Theorem 10.6 holds with $K = 3 ( 0 . 2 8 1 ) = 0 . 8 4 3$

In the same manner it can also be shown that $\partial g _ { i } / \partial x _ { j }$ is continuous on $D$ for each $i = 1 , 2 , 3$ and $j = 1 , 2 , 3$ .（This is considered in Exercise 3.) Consequently, $\mathbf { G }$ has a unique fixed point in $D$ ,and the nonlinear system has a solution in $D$

Note that $\mathbf { G }$ having a unique fixed point in $D$ does not imply that the solution to the original system is unique on this domain, since the solution for $x _ { 2 }$ in (10.4) involved the choice of the principal square root. Exercise 7(d) examines the situation that occurs if, instead, the negative square root is chosen in this step.

To approximate the fixed point $\mathbf { p }$ ,we choose $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 , 0 . 1 , - 0 . 1 ) ^ { t }$ . The sequence of vectors generated by

$$
\begin{array} { l } { \displaystyle x _ { 1 } ^ { ( k ) } = \frac 1 3 \cos x _ { 2 } ^ { ( k - 1 ) } x _ { 3 } ^ { ( k - 1 ) } + \frac 1 6 , } \\ { \displaystyle x _ { 2 } ^ { ( k ) } = \frac 1 9 \sqrt { \left( x _ { 1 } ^ { ( k - 1 ) } \right) ^ { 2 } + \sin x _ { 3 } ^ { ( k - 1 ) } + 1 . 0 6 } - 0 . 1 , } \\ { \displaystyle x _ { 3 } ^ { ( k ) } = - \frac 1 { 2 0 } e ^ { - x _ { 1 } ^ { ( k - 1 ) } x _ { 2 } ^ { ( k - 1 ) } } - \frac { 1 0 \pi - 3 } { 6 0 } } \end{array}
$$

converges to the unique solution of (10.4). The results in Table 10.1 were generated until

$$
\left\| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \right\| _ { \infty } < 1 0 ^ { - 5 } .
$$

# Table 10.1

<table><tr><td>k</td><td>x）</td><td>x</td><td>海</td><td>x(k） -x(k-1） 0</td></tr><tr><td>0</td><td>0.10000000</td><td>0.10000000</td><td>-0.10000000</td><td></td></tr><tr><td>1</td><td>0.49998333</td><td>0.00944115</td><td>-0.52310127</td><td>0.423</td></tr><tr><td>2</td><td>0.49999593</td><td>0.00002557</td><td>-0.52336331</td><td>9.4 × 10-3</td></tr><tr><td>3</td><td>0.50000000</td><td>0.00001234</td><td>-0.52359814</td><td>2.3 × 10-4</td></tr><tr><td>4</td><td>0.50000000</td><td>0.00000003</td><td>-0.52359847</td><td>1.2 × 10-5</td></tr><tr><td>5</td><td>0.50000000</td><td>0.00000002</td><td>-0.52359877</td><td>3.1×10-7</td></tr></table>

Using the error bound (10.3） with $K = 0 . 8 4 3$ gives

$$
\| \mathbf { x } ^ { ( 5 ) } - \mathbf { p } \| _ { \infty } \leq \frac { ( 0 . 8 4 3 ) ^ { 5 } } { 1 - 0 . 8 4 3 } ( 0 . 4 2 3 ) < 1 . 1 5 ,
$$

which does not indicate the true accuracy of $\mathbf { x } ^ { ( 5 ) }$ because of the inaccurate initial approximation. The actual solution is

$$
\mathbf { p } = \left( 0 . 5 , 0 , - { \frac { \pi } { 6 } } \right) ^ { t } \approx ( 0 . 5 , 0 , - 0 . 5 2 3 5 9 8 7 7 5 7 ) ^ { t } ,
$$

so the true error is

$$
\| \mathbf { x } ^ { ( 5 ) } - \mathbf { p } \| _ { \infty } \leq 2 \times 1 0 ^ { - 8 } .
$$

One way to accelerate convergence of the fixed-point iteration is to use the latest estimates xk $x _ { 1 } ^ { ( k ) } , \ldots , x _ { i - 1 } ^ { ( k ) }$ instead of $x _ { 1 } ^ { ( \overline { { k } } - 1 ) } , \mathrm { ~ . ~ . ~ . ~ } , x _ { i - 1 } ^ { ( k - 1 ) }$ to compute $x _ { i } ^ { ( k ) }$ , as in the Gauss-Seidel method for linear systems. The component equations then become

$$
\begin{array} { l } { \displaystyle x _ { 1 } ^ { ( k ) } = \frac 1 3 \cos \left( x _ { 2 } ^ { ( k - 1 ) } x _ { 3 } ^ { ( k - 1 ) } \right) + \frac 1 6 , } \\ { \displaystyle x _ { 2 } ^ { ( k ) } = \frac 1 9 \sqrt { \left( x _ { 1 } ^ { ( k ) } \right) ^ { 2 } + \sin x _ { 3 } ^ { ( k - 1 ) } + 1 . 0 6 } - 0 . 1 , } \\ { \displaystyle x _ { 3 } ^ { ( k ) } = - \frac 1 { 2 0 } e ^ { - x _ { 1 } ^ { ( k ) } x _ { 2 } ^ { ( k ) } } - \frac { 1 0 \pi - 3 } { 6 0 } . } \end{array}
$$

With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 , 0 . 1 , - 0 . 1 ) ^ { t }$ , the results of these calculations are listed in Table 10.2.

The iterate $\mathbf { X } ^ { ( 4 ) }$ is accurate to within $1 0 ^ { - 7 }$ in the $l _ { \infty }$ norm; so the convergence was indeed accelerated for this problem by using the Gauss-Seidel method. However, this method does not always accelerate the convergence.

# Table 10.2

<table><tr><td>k</td><td>x(</td><td>x</td><td>X</td><td>1x）-x(-1)</td></tr><tr><td>0</td><td>0.10000000</td><td>0.10000000</td><td>-0.10000000</td><td></td></tr><tr><td>1</td><td>0.49998333</td><td>0.02222979</td><td>-0.52304613</td><td>0.423</td></tr><tr><td>2</td><td>0.49997747</td><td>0.00002815</td><td>-0.52359807</td><td>2.2 × 10-2</td></tr><tr><td>3</td><td>0.50000000</td><td>0.00000004</td><td>-0.52359877</td><td>2.8 × 10-5</td></tr><tr><td>4</td><td>0.50000000</td><td>0.00000000</td><td>-0.52359877</td><td>3.8 × 10-8</td></tr></table>

Maple provides the function fsolve to solve systems of equations. The fixed-point problem of Example 2 can be solved with the following commands:

$$
\begin{array} { r l } & { > \underline { { 8 } } 1 : = \mathbf { x } 1 = \left( 2 \ast \cos \left( \mathbf { x } 2 \ast \mathbf { x } 3 \right) + 1 \right) / 6 : } \\ & { > \underline { { 9 } } 2 : = \mathbf { x } 2 = \mathbf { s } \underline { { \mathsf { q r t } } } \left( \mathbf { x } 1 \cdot 2 + \mathbf { s } \ln \left( \mathbf { x } 3 \right) + 1 . 0 6 \right) / 9 - 0 . 1 : } \\ & { > \underline { { 8 } } 3 : = \mathbf { x } 3 - \left( 3 \ast \mathbf { x } \mathbf { p } \left( - \mathbf { x } 1 \ast \mathbf { x } 2 \right) + 1 0 \ast \mathbf { p } \mathbf { i } - 3 \right) / 6 0 : } \\ & { > \mathbf { f s o l v e } \left( \left\{ \underline { { 6 } } 1 , \mathbf { g } 2 , \mathbf { g } 3 \right\} , \left\{ \mathbf { x } 1 , \mathbf { x } 2 , \mathbf { x } 3 \right\} , \left\{ \mathbf { x } 1 = - 1 . \mathbf { \sigma } 1 , \mathbf { x } 2 = - 1 . \mathbf { \sigma } 1 , \mathbf { x } 3 = - 1 . \mathbf { \sigma } 1 \right\} \right) ; } \end{array}
$$

The first three commands define the system, and the last command invokes the procedure fsolve. The answer displayed is

$$
\{ x 3 = - . 5 2 3 5 9 8 7 7 5 8 , \ x 1 = . 5 0 0 0 0 0 0 0 0 0 , \ x 2 = - . 2 1 0 2 4 5 4 4 0 9 \ 1 0 ^ { - 1 0 } \}
$$

In general, fsolve(eqns,vars,options) solves the systemof equations represented by the parameter eqns for the variables represented by the parameter vars under optional parameters represented by options. Under options we specify a region in which the routine is required to search for a solution. This specification is not mandatory,and Maple determines its own search space if the options are omitted.

# ExERCIsE SEt 10.1

1.Show that the function $\mathbf { F } : \mathbb { R } ^ { 3 }  \mathbb { R } ^ { 3 }$ defined by

$$
{ \bf F } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = ( x _ { 1 } + 2 x _ { 3 } , x _ { 1 } \cos x _ { 2 } , x _ { 2 } ^ { 2 } + x _ { 3 } ) ^ { t }
$$

is a continuous at each point of ${ \mathbb { R } } ^ { 3 }$

2. Give an example of a function $\mathbf { F } : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ that is continuous at each point of $\mathbb { R } ^ { 2 }$ ,except at (1,0).

3.Show that the first partial derivatives in Example 2 are continuous on $D$

4. The nonlinear system

$$
\begin{array} { r l r } & { } & { - x _ { 1 } ( x _ { 1 } + 1 ) + 2 x _ { 2 } = 1 8 , } \\ & { } & { ( x _ { 1 } - 1 ) ^ { 2 } + ( x _ { 2 } - 6 ) ^ { 2 } = 2 5 } \end{array}
$$

has two solutions.

a. Approximate the solutions graphically. b. Use the approximations from part (a) as initial approximations for an appropriate function iteration,and determine the solutions to within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm.

5. The nonlinear system

$$
\begin{array} { r } { x _ { 1 } ^ { 2 } - 1 0 x _ { 1 } + \quad x _ { 2 } ^ { 2 } + 8 = 0 , } \\ { x _ { 1 } x _ { 2 } ^ { 2 } + \quad x _ { 1 } - 1 0 x _ { 2 } + 8 = 0 } \end{array}
$$

can be transformed into the fixed-point problem

$$
\begin{array} { l } { \displaystyle { x _ { 1 } = g _ { 1 } ( x _ { 1 } , x _ { 2 } ) = \frac { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 8 } { 1 0 } , } } \\ { \displaystyle { x _ { 2 } = g _ { 1 } ( x _ { 1 } , x _ { 2 } ) = \frac { x _ { 1 } x _ { 2 } ^ { 2 } + x _ { 1 } + 8 } { 1 0 } . } } \end{array}
$$

a. Use Theorem 10.6 to show that $\mathbf { G } = ( g _ { 1 } , g _ { 2 } ) ^ { t }$ mapping $D \subset \mathbb { R } ^ { 2 }$ into $\mathbb { R } ^ { 2 }$ has a unique fixed point in

$$
D = \{ ( x _ { 1 } , x _ { 2 } ) ^ { t } \mid 0 \leq x _ { 1 } , x _ { 2 } \leq 1 . 5 \} .
$$

b. Apply functional iteration to approximate the solution. c. Does the Gauss-Seidel method accelerate convergence?

6. The nonlinear system

$$
\begin{array} { r } { 5 x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } = 0 , } \\ { x _ { 2 } - 0 . 2 5 ( \sin x _ { 1 } + \cos x _ { 2 } ) = 0 } \end{array}
$$

has a solution near $\left( { \frac { 1 } { 4 } } , { \frac { 1 } { 4 } } \right) ^ { t }$

a. Find a function $\mathbf { G }$ and a set $D$ in $\mathbb { R } ^ { 2 }$ such that $\mathbf { G } : D  \mathbb { R } ^ { 2 }$ and $\mathbf { G }$ has a unique fixed point in $D$ ：   
$\mathbf { b } _ { \bullet }$ Apply functional iteration to approximate the solution to within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm.   
$\pmb { \mathbb { c } } _ { \pmb { \nu } }$ Does the Gauss-Seidel method accelerate convergence?

7. Use Theorem 10.6 to show that $\mathbf { G } : D \subset \mathbb { R } ^ { 3 } \to \mathbb { R } ^ { 3 }$ has a unique fixed point in $D$ .Apply functional iteration toapproximate the solution to within $1 0 ^ { - 5 }$ , using $\| \cdot \| _ { \infty }$

$$
\begin{array} { r l } { { } } & { { \displaystyle \mathbf { 0 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \left( \frac { \cos ( x _ { 2 } , x _ { 3 } ) + 0 . 5 } { 3 } , \frac { 1 } { 2 5 } \sqrt { x _ { 1 } ^ { 2 } + 0 . 3 1 2 5 } - 0 . 0 3 , \right. } } \\ { { } } & { { \displaystyle \left. - \frac { 1 } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } - \frac { 1 0 \pi - 3 } { 6 0 } \right) ^ { t } ; } } \end{array}
$$

$$
D = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } \mid - 1 \leq x _ { 1 } \leq 1 , i = 1 , 2 , 3 \}
$$

$$
\mathbf { G } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \left( { \frac { 1 3 - x _ { 2 } ^ { 2 } + 4 x _ { 3 } } { 1 5 } } , { \frac { 1 1 + x _ { 3 } - x _ { 1 } ^ { 2 } } { 1 0 } } , { \frac { 2 2 + x _ { 2 } ^ { 3 } } { 2 5 } } \right) ;
$$

$$
D = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } \mid 0 \leq x _ { 1 } \leq 1 . 5 , i = 1 , 2 , 3 \}
$$

$$
\mathbf { G } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = ( 1 - \cos ( x _ { 1 } x _ { 2 } x _ { 3 } ) , 1 - ( 1 - x _ { 1 } ) ^ { 1 / 4 } - 0 . 0 5 x _ { 3 } ^ { 2 } + 0 . 1 5 x _ { 3 } , x _ { 1 } ^ { 2 }
$$

$$
+ 0 . 1 x _ { 2 } ^ { 2 } - 0 . 0 1 x _ { 2 } + 1 ) ^ { t } ;
$$

$$
D = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } \mid - 0 . 1 \leq x _ { 1 } \leq 0 . 1 , - 0 . 1 \leq x _ { 2 } \leq 0 . 3 , 0 . 5 \leq x _ { 3 } \leq 1 . 1 \}
$$

$$
\mathbf { G } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \left( { \frac { 1 } { 3 } } \cos ( x _ { 2 } , x _ { 3 } ) + { \frac { 1 } { 6 } } , - { \frac { 1 } { 9 } } { \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } } - 0 . 1 , \right.
$$

$$
- \frac { 1 } { 2 0 } e ^ { - x _ { 1 } x _ { 2 } } - \frac { 1 0 \pi - 3 } { 6 0 } \biggr ) ^ { \prime } ;
$$

$$
D = \{ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } \mid - 1 \leq x _ { 1 } \leq 1 , i = 1 , 2 , 3 \}
$$

8.Use the Gauss-Seidel method to approximate the fixed points in Exercise 7 to within $1 0 ^ { - 5 }$ ， using $\| \cdot \| _ { \infty }$

9. Use functional iteration to find solutions to the following nonlinear systems,accurate to within $1 0 ^ { - 5 }$ ,using $1 1 \cdot 1 1 _ { \infty }$

$$
\begin{array} { r l } { x _ { 2 } ^ { 2 } + x _ { 2 } ^ { 2 } - x _ { 1 } = 0 \qquad } & { { } \mathbf { b } . \qquad 3 x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } = 0 , } \\ { x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } - x _ { 2 } = 0 . } & { { } \qquad \quad 3 x _ { 1 } x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } - 1 = 0 . } \\ { x _ { 1 } ^ { 2 } + x _ { 2 } - 3 7 = 0 , } & { { } \qquad \quad \mathbf { d } . \quad x _ { 1 } ^ { 2 } + 2 x _ { 2 } ^ { 2 } - x _ { 2 } - 2 x _ { 3 } = 0 , } \\ { x _ { 1 } - x _ { 2 } ^ { 2 } - 5 = 0 , } & { { } \qquad \quad x _ { 1 } ^ { 2 } - 8 x _ { 2 } ^ { 2 } + 1 0 x _ { 3 } = 0 , } \\ { x _ { 1 } + x _ { 2 } + x _ { 3 } - 3 = 0 . } & { { } \qquad \quad \frac { x _ { 1 } ^ { 2 } } { 7 x _ { 2 } x _ { 3 } } - 1 = 0 . } \end{array}
$$

10. Show that a function $\mathbf { F }$ mapping $D \subset \mathbb { R } ^ { n }$ into $\mathbb { R } ^ { n }$ is continuous at $\mathbf { x } _ { 0 } \in \mathbf { \Omega } D$ precisely when, given any number $\varepsilon > 0$ ,a number $\delta > 0$ can be found with property that for any vector norm $\| \cdot \|$ ，

$$
\| \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) \| < \varepsilon ,
$$

whenever $\pmb { \mathrm { x } } \in \pmb { D }$ and ${ \| \mathbf { x } - \mathbf { x } _ { 0 } \| } < \delta$

11.In Exercise 8 of Section 5.9, we considered the problem of predicting the population of two species that compete for the same food supply. In the problem, we made the assumption that the populations could be predicted by solving the system of equations

$$
\frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) ( 4 - 0 . 0 0 0 3 x _ { 1 } ( t ) - 0 . 0 0 0 4 x _ { 2 } ( t ) )
$$

and

$$
\frac { d x _ { 2 } ( t ) } { d t } = x _ { 2 } ( t ) ( 2 - 0 . 0 0 0 2 x _ { 1 } ( t ) - 0 . 0 0 0 1 x _ { 2 } ( t ) ) .
$$

In this exercise, we would like to consider the problem of determining equilibrium populations of the two species.The mathematical criteria that must be satisfied in order for the populations to be at equilibrium is that, simultaneously,

$$
{ \frac { d x _ { 1 } ( t ) } { d t } } = 0 \quad { \mathrm { a n d } } \quad { \frac { d x _ { 2 } ( t ) } { d t } } = 0 .
$$

This occurs when the first species is extinct and the second species has a population of 20.000 or when the second species is extinct and the first species has a population of 13,333. Can an equilibrium occur in any other situation?

# 10.2 Newton's Method

The problem in Example 2 of the previous section is transformed into a convergent fixed-point problem by algebraically solving the three equations for the three variables $x _ { 1 } , x _ { 2 }$ ， and $x _ { 3 }$ . It is,however, rather unusual for this technique to be successful. In this section, we consider an algorithmic procedure to perform the transformation in a more general situation.

To construct the algorithm that led to an appropriate fixed-point method in the onedimensional case,we found a function $\phi$ with the property that

$$
g ( x ) = x - \phi ( x ) f ( x )
$$

gives quadratic convergence to the fixed point $p$ of the function $g$ (see Section 2.4). From this condition Newton's method evolved by choosing $\phi ( x ) ~ = ~ 1 / f ^ { \prime } ( x )$ ，assuming that $f ^ { \prime } ( x ) \neq 0$

Using a similar approach in the $\pmb { n }$ -dimensional case involves a matrix

$$
A ( \mathbf { x } ) = \left[ \begin{array} { c c c c } { a _ { 1 1 } ( \mathbf { x } ) } & { a _ { 1 2 } ( \mathbf { x } ) } & { \ldots } & { a _ { 1 n } ( \mathbf { x } ) } \\ { a _ { 2 1 } ( \mathbf { x } ) } & { a _ { 2 2 } ( \mathbf { x } ) } & { \ldots } & { a _ { 2 n } ( \mathbf { x } ) } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { a _ { n 1 } ( \mathbf { x } ) } & { a _ { n 2 } ( \mathbf { x } ) } & { \ldots } & { a _ { n n } ( \mathbf { x } ) } \end{array} \right] ,
$$

where each of the entries $a _ { i j } ( { \bf x } )$ is a function from ${ \mathbb { R } } ^ { n }$ into $\mathbb { R }$ . This requires that $A ( \mathbf { x } )$ be found so that

$$
\mathbf { G } ( \mathbf { x } ) = \mathbf { x } - A ( \mathbf { x } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } )
$$

gives quadratic convergence to the solution of $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ ,assuming that $A ( \mathbf { x } )$ is nonsingular at the fixed point p of $\mathbf { G }$

The following theorem parallels Theorem 2.8 in Section 2.4. Its proof requires being able to express $\mathbf { G }$ in terms of its Taylor series in $\pmb { n }$ variables about $\mathbf { p }$

Theorem 10.7

Let p be a solution of $\mathbf { G } ( \mathbf { x } ) = \mathbf { x }$ . Suppose a number $\delta > 0$ exists with

i $\partial g _ { i } / \partial x _ { j }$ is continuous on $N _ { \delta } = \{ \mathbf { x } \mid \| \mathbf { x } - \mathbf { p } \| < \delta \}$ ,for each $i = 1 , 2 , \dots , n$ and $j = 1 , 2 , \dots , n ;$ (i) $\partial ^ { 2 } g _ { i } ( { \bf x } ) / ( \partial x _ { j } \partial x _ { k } )$ is continuous, and $| \partial ^ { 2 } g _ { i } ( { \bf x } ) / ( \partial x _ { j } \partial x _ { k } ) | \le M$ for some constant $M$ ，whenever $\textbf { x } \in \ N _ { \delta }$ ， for each $i = 1 , 2 , . . . , n$ ， $j = 1 , 2 , \dots , n$ ，and $k = 1 , 2 , \ldots , n ;$ (ii） $\partial g _ { i } ( \mathbf { p } ) / \partial x _ { k } = 0$ , for each $i = 1 , 2 , \dots , n$ and $k = 1 , 2 , \ldots , n .$

Then a number $\hat { \delta } \le \delta$ exists such that the sequence generated by $\mathbf { x } ^ { ( k ) } = \mathbf { G } ( \mathbf { x } ^ { ( k - 1 ) } )$ converges quadratically to p for any choice of $\mathbf { x } ^ { ( 0 ) }$ , provided that $\left\| \mathbf { x } ^ { ( 0 ) } - \mathbf { p } \right\| < \hat { \delta }$ . Moreover,

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { p } \| _ { \infty } \leq \frac { n ^ { 2 } M } { 2 } \| \mathbf { x } ^ { ( k - 1 ) } - \mathbf { p } \| _ { \infty } ^ { 2 } , \quad \mathrm { f o r } \mathrm { e a c h } k \geq 1 .
$$

To use Theorem 10.7,suppose that $A ( \mathbf { x } )$ is an $n \times n$ matrix of functions from $\mathbb { R } ^ { n }$ into $\mathbb { R }$ in the form of Eq. (10.5), where the specific entries will be chosen later. Assume, moreover, that $A ( \mathbf { x } )$ is nonsingular near a solution p of $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ , and let $b _ { i j } ( { \bf x } )$ denote the entry of $A ( \mathbf { x } ) ^ { - 1 }$ in the ith row and $j$ th column.

Since $\mathbf { G } ( \mathbf { x } ) = \mathbf { x } - A ( \mathbf { x } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } )$ , we have $\begin{array} { r } { g _ { i } ( \mathbf { x } ) = x _ { i } - \sum _ { j = 1 } ^ { n } b _ { i j } ( \mathbf { x } ) f _ { j } ( \mathbf { x } ) } \end{array}$ and

$$
\frac { \partial g _ { i } } { \partial x _ { k } } ( \mathbf { x } ) = \left\{ \begin{array} { l l } { \displaystyle 1 - \sum _ { j = 1 } ^ { n } \left( b _ { i j } ( \mathbf { x } ) \frac { \partial f _ { j } } { \partial x _ { k } } ( \mathbf { x } ) + \frac { \partial b _ { i j } } { \partial x _ { k } } ( \mathbf { x } ) f _ { j } ( \mathbf { x } ) \right) \mathrm { , ~ \ ~ i f ~ } i = k \mathrm { , ~ \ } } & \\ { \displaystyle - \sum _ { j = 1 } ^ { n } \left( b _ { i j } ( \mathbf { x } ) \frac { \partial f _ { j } } { \partial x _ { k } } ( \mathbf { x } ) + \frac { \partial b _ { i j } } { \partial x _ { k } } ( \mathbf { x } ) f _ { j } ( \mathbf { x } ) \right) \mathrm { , ~ \ ~ i f ~ } i \neq k \mathrm { . ~ \ } } & \end{array} \right.
$$

Theorem 10.7 implies that we need $\partial g _ { i } ( \mathbf { p } ) / \partial x _ { k } = 0$ , for each $i = 1 , 2 , \dots , n$ and $k =$ $1 , 2 , \ldots , n$ . This means that for $i = k$ ，

$$
0 = 1 - \sum _ { j = 1 } ^ { n } b _ { i j } ( \mathbf { p } ) { \frac { \partial f _ { j } } { \partial x _ { i } } } ( \mathbf { p } ) ,
$$

So

$$
\sum _ { j = 1 } ^ { n } b _ { i j } ( \mathbf { p } ) \frac { \partial f _ { j } } { \partial x _ { i } } ( \mathbf { p } ) = 1 .
$$

When $k \neq i$ ，

$$
0 = - \sum _ { j = 1 } ^ { n } b _ { i j } ( \mathbf { p } ) { \frac { \partial f _ { j } } { \partial x _ { k } } } ( \mathbf { p } ) ,
$$

So

$$
\sum _ { j = 1 } ^ { n } b _ { i j } ( \mathbf { p } ) { \frac { \partial f _ { j } } { \partial x _ { k } } } ( \mathbf { p } ) = 0 .
$$

Defining the matrix $J ( \mathbf { x } )$ by

$$
J ( \mathbf { x } ) = \left[ \begin{array} { c c c c } { \frac { \partial f _ { 1 } } { \partial x _ { 1 } } ( \mathbf { x } ) } & { \frac { \partial f _ { 1 } } { \partial x _ { 2 } } ( \mathbf { x } ) } & { \cdots } & { \frac { \partial f _ { 1 } } { \partial x _ { n } } ( \mathbf { x } ) } \\ { \frac { \partial f _ { 2 } } { \partial x _ { 1 } } ( \mathbf { x } ) } & { \frac { \partial f _ { 2 } } { \partial x _ { 2 } } ( \mathbf { x } ) } & { \cdots } & { \frac { \partial f _ { 2 } } { \partial x _ { n } } ( \mathbf { x } ) } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { \frac { \partial f _ { n } } { \partial x _ { 1 } } ( \mathbf { x } ) } & { \frac { \partial f _ { n } } { \partial x _ { 2 } } ( \mathbf { x } ) } & { \cdots } & { \frac { \partial f _ { n } } { \partial x _ { n } } ( \mathbf { x } ) } \end{array} \right] ,
$$

we see that conditions (10.6) and (10.7) require

$$
A ( { \bf p } ) ^ { - 1 } J ( { \bf p } ) = I , \quad \mathrm { t h e ~ i d e n t i t y ~ m a t r i x , }
$$

so

$$
A ( \mathbf { p } ) = J ( \mathbf { p } ) .
$$

An appropriate choice for $A ( \mathbf { x } )$ is, consequently, $A ( \mathbf { x } ) = J ( \mathbf { x } )$ since this satisfies condition (i) in Theorem 10.7.

The function $\mathbf { G }$ is defined by

$$
\mathbf { G } ( \mathbf { x } ) = \mathbf { x } - J ( \mathbf { x } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ) ,
$$

and the functional iteration procedure evolves from selecting $\mathbf { x } ^ { ( 0 ) }$ and generating, for $k \geq 1$ ，

$$
\mathbf { x } ^ { ( k ) } = \mathbf { G } ( \mathbf { x } ^ { ( k - 1 ) } ) = \mathbf { x } ^ { ( k - 1 ) } - J ( \mathbf { x } ^ { ( k - 1 ) } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ^ { ( k - 1 ) } ) .
$$

This is called Newton's method for nonlinear systems, and it is generally expected to give quadratic convergence, provided that a sufficiently accurate starting value is known and $J ( \mathbf { p } ) ^ { - 1 }$ exists.

The matrix $J ( \mathbf { x } )$ is called the Jacobian matrix and has a number of applications in analysis.It might, in particular,be familiar to the reader due to its application in the mul-tiple integration of a function of several variables over a region that requires a change of variables to be performed.

The weakness in Newton's method arises from the need to compute and invert the matrix $J ( \mathbf { x } )$ at each step. In practice, explicit computation of $J ( \mathbf { x } ) ^ { - 1 }$ is avoided by performing the operation in a two-step manner. First, a vector $\mathbf { y }$ is found that satisfies $J ( \mathbf { x } ^ { ( k - 1 ) } ) \mathbf { y } =$ $- \mathbf { F } ( \mathbf { \bar { x } } ^ { ( k - 1 ) } )$ . Then the new approximation, $\mathbf { x } ^ { ( k ) }$ , is obtained by adding y to $\mathbf { x } ^ { ( k - 1 ) }$ . Algorithm 10.1 uses this two-step procedure.

# Newton's Method for Systems

To approximate the solution of the nonlinear system $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ given an initial approximation x:

INPUTnumber $\pmb { n }$ of equations and unknowns; initial approximation $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ ， tolerance TOL; maximum number of iterations $N$

OUTPUTapproximate solution $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ or a message that the number of iterations was exceeded.

Step 1 Set $k = 1$

Step 2 While $( k \leq N )$ do Steps 3-7.

Step 3 Calculate $\mathbf { F } ( \mathbf { x } )$ and $J ( \mathbf { x } )$ , where $J ( \mathbf { x } ) _ { i , j } = ( \partial f _ { i } ( \mathbf { x } ) / \partial x _ { j } )$ for $1 \leq i , j \leq n$   
Step 4 Solve the $n \times n$ linear system $J ( \mathbf { x } ) \mathbf { y } = - \mathbf { F } ( \mathbf { x } )$ ·   
Step 5Set $\mathbf { x } = \mathbf { x } + \mathbf { y }$   
Step 6If $| | \mathbf { y } | | < T O L$ then OUTPUT $\mathbf { \Psi } ( \mathbf { X } )$ ； (The procedure was successful.) STOP.

Step 7Set $k = k + 1$

Step 8OUTPUT(‘Maximum number of iterations exceeded); (The procedure was unsuccessful.) STOP.

The nonlinear system

$$
\begin{array} { c } { { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - { \displaystyle { \frac { 1 } { 2 } } } = 0 , } } \\ { { } } \\ { { x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } } \\ { { } } \\ { { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle { \frac { 1 0 \pi - 3 } { 3 } } = 0 } } \end{array}
$$

was shown in Example 2 of Section 10.1 to have an approximate solution at (0.5,0, $- 0 . 5 2 3 5 9 8 7 7 ) ^ { t }$ . Newton's method willbe used to obtain this approximation when the initial approximation is $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 , 0 . 1 , - 0 . 1 ) ^ { t }$ and

$$
{ \bf F } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = ( f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ) ^ { t } ,
$$

where

$$
\begin{array} { l } { \displaystyle f _ { 1 } ( \boldsymbol { x } _ { 1 } , \boldsymbol { x } _ { 2 } , \boldsymbol { x } _ { 3 } ) = 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \frac { 1 } { 2 } , } \\ { \displaystyle f _ { 2 } ( \boldsymbol { x } _ { 1 } , \boldsymbol { x } _ { 2 } , \boldsymbol { x } _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 , } \end{array}
$$

and

$$
f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \frac { 1 0 \pi - 3 } { 3 } .
$$

The Jacobian matrix $J ( \mathbf { x } )$ for this system is

$$
J ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \left[ { \begin{array} { c c c } { 3 } & { x _ { 3 } \sin x _ { 2 } x _ { 3 } } & { x _ { 2 } \sin x _ { 2 } x _ { 3 } } \\ { 2 x _ { 1 } } & { - 1 6 2 ( x _ { 2 } + 0 . 1 ) } & { \cos x _ { 3 } } \\ { - x _ { 2 } e ^ { - x _ { 1 } x _ { 2 } } } & { - x _ { 1 } e ^ { - x _ { 1 } x _ { 2 } } } & { 2 0 } \end{array} } \right]
$$

and

$$
\begin{array} { r } { \left[ \begin{array} { l } { x _ { \mathrm { I } } ^ { ( k ) } } \\ { x _ { 2 } ^ { ( k ) } } \\ { x _ { 3 } ^ { ( k ) } } \end{array} \right] = \left[ \begin{array} { l } { x _ { \mathrm { I } } ^ { ( k - 1 ) } } \\ { x _ { 2 } ^ { ( k - 1 ) } } \\ { x _ { 3 } ^ { ( k - 1 ) } } \end{array} \right] + \left[ \begin{array} { l } { y _ { \mathrm { I } } ^ { ( k - 1 ) } } \\ { y _ { 2 } ^ { ( k - 1 ) } } \\ { y _ { 3 } ^ { ( k - 1 ) } } \end{array} \right] , } \end{array}
$$

where

$$
\left[ \begin{array} { l } { y _ { 1 } ^ { ( k - 1 ) } } \\ { y _ { 2 } ^ { ( k - 1 ) } } \\ { y _ { 3 } ^ { ( k - 1 ) } } \end{array} \right] = - \left( J \left( x _ { 1 } ^ { ( k - 1 ) } , x _ { 2 } ^ { ( k - 1 ) } , x _ { 3 } ^ { ( k - 1 ) } \right) \right) ^ { - 1 } \mathbf { F } \left( x _ { 1 } ^ { ( k - 1 ) } , x _ { 2 } ^ { ( k - 1 ) } , x _ { 3 } ^ { ( k - 1 ) } \right) .
$$

Thus, at the $k$ th step, the linear system $J \left( \mathbf { x } ^ { ( k - 1 ) } \right) \mathbf { y } ^ { ( k - 1 ) } = - \mathbf { F } \left( \mathbf { x } ^ { ( k - 1 ) } \right)$ must be solved, where

$$
\begin{array} { r } { \boldsymbol { \mathrm { \mathrm {  ~ \cal ~ r ~ } } } ( { \bf x } ^ { ( k - 1 ) } ) = \left[ \begin{array} { c c c c } { 3 } & { x _ { 3 } ^ { ( k - 1 ) } \sin x _ { 2 } ^ { ( k - 1 ) } x _ { 3 } ^ { ( k - 1 ) } } & { x _ { 2 } ^ { ( k - 1 ) } \sin x _ { 2 } ^ { ( k - 1 ) } x _ { 3 } ^ { ( k - 1 ) } } \\ { 2 x _ { 1 } ^ { ( k - 1 ) } } & { - 1 6 2 \left( x _ { 2 } ^ { ( k - 1 ) } + 0 . 1 \right) } & { \cos x _ { 3 } ^ { ( k - 1 ) } } \\ { - x _ { 2 } ^ { ( k - 1 ) } e ^ { - x _ { 4 } ^ { ( k - 1 ) } x _ { 2 } ^ { ( k - 1 ) } } } & { - x _ { 1 } ^ { ( k - 1 ) } e ^ { - x _ { 1 } ^ { ( k - 1 ) } x _ { 2 } ^ { ( k - 1 ) } } } & { 2 0 } \end{array} \right] } \\ { \left[ \begin{array} { c c c c } { y _ { 1 } ^ { ( k - 1 ) } \rceil } & { } & { } & { } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r } { \mathbf { y } ^ { ( k - 1 ) } = \left[ \begin{array} { l } { y _ { 1 } ^ { ( k - 1 ) } } \\ { y _ { 2 } ^ { ( k - 1 ) } } \\ { y _ { 3 } ^ { ( k - 1 ) } } \end{array} \right] , } \end{array}
$$

and

$$
\mathbf { F } \left( \mathbf { x } ^ { ( k - 1 ) } \right) = \left[ \left( x _ { 1 } ^ { ( k - 1 ) } \right) ^ { 2 } - 8 1 \left( x _ { 2 } ^ { ( k - 1 ) } + 0 . 1 \right) ^ { 2 } + \sin x _ { 3 } ^ { ( k - 1 ) } + 1 . 0 6 \right] .
$$

The results using this iterative procedure are shown in Table 10.3.

Table 10.3

<table><tr><td>k</td><td>x</td><td>x</td><td>炒</td><td>1x(）-x(-1）8</td></tr><tr><td>0</td><td>0.10000000</td><td>0.10000000</td><td>-0.10000000</td><td></td></tr><tr><td>1</td><td>0.50003702</td><td>0.01946686</td><td>-0.52152047</td><td>0.422</td></tr><tr><td>2</td><td>0.50004593</td><td>0.00158859</td><td>-0.52355711</td><td>1.79 × 10-2</td></tr><tr><td>3</td><td>0.50000034</td><td>0.00001244</td><td>-0.52359845</td><td>1.58 × 10-3</td></tr><tr><td>4</td><td>0.50000000</td><td>0.00000000</td><td>-0.52359877</td><td>1.24 × 10-5</td></tr><tr><td>5</td><td>0.50000000</td><td>0.00000000</td><td>-0.52359877</td><td>0</td></tr></table>

The previous example illustrates that Newton's method can converge very rapidly once an approximation is obtained that is near the true solution. However, it is not always easy to determine starting values that wil lead to a solution,and the method is comparatively expensive to employ. In the next section, we consider a method for overcoming the latter weakness.Good starting values can usually be found by the method that will be discussed in Section 10.4.

Initial approximation to the solutions of $2 \times 2$ and often $3 \times 3$ nonlinear systems can also be obtained using the graphing facilities of Maple. The nonlinear system

$$
\begin{array} { r } { x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } + 2 x _ { 2 } = 0 , } \\ { 2 x _ { 1 } + x _ { 2 } ^ { 2 } - 6 = 0 } \end{array}
$$

has two solutions, (0.625204094,2.179355825) and (2.109511920,-1.334532188).To use Maple we first define the two equations

>eq1 $: = \mathbf { x } \mathbf { 1 } \hat { \mathbf { \phi } } 2 \mathbf { - x } 2 \hat { \mathbf { \phi } } 2 \mathbf { + } 2 \mathbf { * } \mathbf { x } 2 = 0 $ $> \mathrm { e q } 2 : = 2 * \mathrm { x } 1 + \mathrm { x } 2 ^ { \setminus } 2 ^ { \neg } 6 = 0$ ；

To obtain a graph of the two equations for $- 3 \leq x _ { 1 } , x _ { 2 } \leq 3$ ,enter the commands

>with(plots); $\mathrm { > i m p l i c i t p l o t } ( \{ \mathsf { e q } 1 , \mathsf { e q } 2 \} , \mathbf { x } 1 \mathrm { = } - 3 . \ . 3 , \mathbf { x } 2 \mathrm { = } - 3 . \ . 3 ) \ ;$

From the graph shown in Figure 1O.2,we are able to estimate that there are solutions near (0.64,2.2)' and $( 2 . 1 , - 1 . 3 ) ^ { t }$ . This gives us good starting values for Newton's method.

![](images/44207fb08fd30c13905b9824de81bb2c21bd46808f81c5948db0b102e86e6792.jpg)  
Figure 10.2

The problem is more difficult in three dimensions. Consider the nonlinear system

$$
\begin{array} { r } { 2 x _ { 1 } - 3 x _ { 2 } + x _ { 3 } - 4 = 0 , } \\ { 2 x _ { 1 } + x _ { 2 } - x _ { 3 } + 4 = 0 , } \\ { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } - 4 = 0 . } \end{array}
$$

Define three equations using the Maple commands>eq1: $= 2 * \mathbf { x } 1 - 3 * \mathbf { x } 2 + \mathbf { x } 3 - 4 = 0$ ；>ec $\scriptstyle \mathtt { j } 2 : = 2 \ast \mathbf { x } 1 + \mathbf { x } 2 - \mathbf { x } 3 + 4 = 0$ >eq3:=x1^2+x2^2+x3^2-4=0;

The third equation describes a sphere of radius 2 and center $( 0 , 0 , 0 ) , \ \mathrm { s o } \ \mathbf { x } 1 , \mathbf { x } 2$ , and x3 are in [-2,2]. The Maple commands to obtain the graph in this case are

>with(plots);  
>implicitplot3d({eq1,eq2,eq3},x1=-2..2,x2=-2..2,x3=-2..2);

Various three-dimensional ploting options are available in Maple for isolating a solution to the nonlinear system. For example,we can rotate the graph to beter view the sections of the surfaces. Then we can zoom into regions where the intersections lie and alter the display form of the axes for a more accurate view of the intersection's coordinates. For this problem, a reasonable initial approximation is $( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } = ( - 0 . 5 , - 1 . 5 , 1 . 5 ) ^ { t }$

1.Use Newton's method with $\mathbf { x } ^ { ( 0 ) } = \mathbf { 0 }$ to compute $\mathbf { x } ^ { ( 2 ) }$ for each of the following nonlinear systems.

$\begin{array} { r l } { { \mathrm { a . } \mathrm { ~ } } } & { { \mathrm { ~ } 4 x _ { 1 } ^ { 2 } - 2 0 x _ { 1 } + \cfrac { 1 } { 4 } x _ { 2 } ^ { 2 } + 8 = 0 , } } \\ { { \mathrm { a . ~ } } } & { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } & { { \displaystyle \frac { 1 } { 2 } x _ { 1 } x _ { 2 } ^ { 2 } + 2 x _ { 1 } - 5 x _ { 2 } + 8 = 0 . } } \end{array} \qquad \begin{array} { r l } { { \mathrm { b . ~ } } } & { { \mathrm { ~ s i n ( } 4 \pi x _ { 1 } x _ { 2 } ) - 2 x _ { 2 } - x _ { 1 } = 0 , } } \\ { { \mathrm { ~ } } } & { { } } \\ { { \mathrm { ~ } } } & { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } & { { \displaystyle \left( \frac { 4 \pi - 1 } { 4 \pi } \right) ( e ^ { 2 x _ { 1 } } - e ) + 4 e x _ { 2 } ^ { 2 } - 2 e x _ { 1 } = 0 . } } \end{array}$ ：0,c. $\begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \cfrac { 1 } { 2 } = 0 , \qquad \mathrm { ~ d . ~ } \qquad x _ { 1 } ^ { 2 } + x _ { 2 } - 3 7 = 0 , } \\ { 4 x _ { 1 } ^ { 2 } - 6 2 5 x _ { 2 } ^ { 2 } + 2 x _ { 2 } - 1 = 0 , \qquad \quad x _ { 1 } - x _ { 2 } ^ { 2 } - 5 = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \cfrac { 1 0 \pi - 3 } { 3 } = 0 . \qquad \quad x _ { 1 } + x _ { 2 } + x _ { 3 } - 3 = 0 . } \end{array}$

2.Use the graphing facilities of Maple to approximate solutions to the follwing nonlinear systems.

a. $\begin{array} { r l r } { x _ { 1 } ( 1 - x _ { 1 } ) + 4 x _ { 2 } = 1 2 , } & { \qquad } & { { \bf b . } } \\ { ( x _ { 1 } - 2 ) ^ { 2 } + ( 2 x _ { 2 } - 3 ) ^ { 2 } = 2 5 . } & { \qquad } & { { x _ { 2 } } - 0 . 2 5 ( \sin x _ { 1 } + \cos x _ { 2 } ) = 0 . } \end{array}$ c. $\begin{array} { c } { { 1 5 x _ { 1 } + x _ { 2 } ^ { 2 } - 4 x _ { 3 } = 1 3 , } } \\ { { x _ { 1 } ^ { 2 } + 1 0 x _ { 2 } - x _ { 3 } = 1 1 , } } \\ { { x _ { 2 } ^ { 3 } - 2 5 x _ { 3 } = - 2 2 . } } \end{array}$ （ $\begin{array} { r l r } { \mathbb { 1 } . } & { } & { 1 0 x _ { 1 } - 2 x _ { 2 } ^ { 2 } + x _ { 2 } - 2 x _ { 3 } - 5 = 0 , } \\ & { } & { 8 x _ { 2 } ^ { 2 } + 4 x _ { 3 } ^ { 2 } - 9 = 0 , } \\ & { } & { 8 x _ { 2 } x _ { 3 } + 4 = 0 . } \end{array}$

3. Use Newton's method to find a solution to the following nonlinear systems in the given domain. Iterate until $\| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \| _ { \infty } < 1 0 ^ { - 6 }$

a. $\begin{array} { c } { { 3 x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } = 0 , } } \\ { { } } \\ { { 3 x _ { 1 } x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } - 1 = 0 . } } \\ { { } } \\ { { \mathrm { U s e \ } \mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t } . } } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \ } & { \ln ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) - \sin ( x _ { 1 } x _ { 2 } ) = \ln 2 + \ln \pi , } \\ & { \qquad e ^ { x _ { 1 } - x _ { 2 } } + \cos ( x _ { 1 } x _ { 2 } ) = 0 . } \end{array}$ Use $\mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { \prime }$

$$
\begin{array} { c } { { x _ { 1 } ^ { 3 } + x _ { 1 } ^ { 2 } x _ { 2 } - x _ { 1 } x _ { 3 } + 6 = 0 , } } \\ { { { } } } \\ { { e ^ { x _ { 1 } } + e ^ { x _ { 2 } } - x _ { 3 } = 0 , } } \\ { { x _ { 2 } ^ { 2 } - 2 x _ { 1 } x _ { 3 } = 4 . } } \\ { { { } } } \\ { { \mathrm { U s e \ } \mathbf { x } ^ { ( 0 ) } = ( - 1 , - 2 , 1 ) ^ { t } . } } \end{array}
$$

d. $\begin{array} { r l r } & { } & { 6 x _ { 1 } - 2 \cos ( x _ { 2 } x _ { 3 } ) - 1 = 0 , } \\ & { } & { 9 x _ { 2 } + \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } + 0 . 9 = 0 , } \\ & { } & { 6 0 x _ { 3 } + 3 e ^ { - x _ { 1 } x _ { 2 } } + 1 0 \pi - 3 = 0 . } \end{array}$ Use $\mathbf { \boldsymbol { \cdot } \mathbf { x } ^ { ( 0 ) } } = ( \mathbf { 0 } , \mathbf { 0 } , \mathbf { 0 } ) ^ { t }$

4. Use the answers obtained in Exercise 2 as initial approximations to Newton's method. Iterate until $\Big \| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \Big \| _ { \infty } < 1 0 ^ { - 6 }$

5. The nonlinear system

$$
\begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \displaystyle \frac { 1 } { 2 } = 0 , } \\ { x _ { 1 } ^ { 2 } - 6 2 5 x _ { 2 } ^ { 2 } - \displaystyle \frac { 1 } { 4 } = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 } \end{array}
$$

has a singular Jacobian matrix at the solution. Apply Newton's method with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 - 1 ) ^ { t }$ · Note that convergence may be slow or may not occur within a reasonable number of iterations.

6. The nonlinear system

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 } } \end{array}
$$

has six solutions.

a. Show that if $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution then $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , - x _ { 4 } ) ^ { t }$ is a solution. b. Use Newton's method three times to approximate all solutions. Iterate until |x()_ $\mathbf { x } ^ { ( k - 1 ) } \big \| _ { \infty } < 1 0 ^ { - 5 }$

7.Show that when $n = 1$ ,Newton's method given by Eq. (10.9) reduces to the familiar Newton's method given by Eq. (2.5).

8.What does Newton's method reduce to for the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ given by

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ { \qquad \quad } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ { \qquad \quad } \\ { \qquad \vdots \qquad } \end{array}
$$

$$
a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = b _ { n } ,
$$

where $\pmb { A }$ is a nonsingular matrix?

9.In calculating'the shape of a gravity-flow discharge chute that will minimize transit time of discharged granular particles, C. Chiarella,W. Charlton, and A.W.Roberts [CCR] solve the following equations by Newton's method:

(i） $\begin{array} { l } { { f _ { n } ( \theta _ { 1 } , \dots , \theta _ { N } ) ~ = ~ { \displaystyle \frac { \sin \theta _ { n + 1 } } { v _ { n + 1 } } } ( 1 ~ - ~ \mu w _ { n + 1 } ) ~ { \displaystyle - \frac { \sin \theta _ { n } } { v _ { n } } } ( 1 ~ - ~ \mu w _ { n } ) ~ = ~ 0 , } } \\ { { 1 , 2 , \dots , N - 1 . } } \end{array}$ for each $n =$ (ii） $\begin{array} { r } { f _ { N } ( \theta _ { 1 } , \dots , \theta _ { N } ) = \Delta y \sum _ { i = 1 } ^ { N } \tan \theta _ { i } - X = 0 } \end{array}$ ，where$\begin{array} { r l } & { \mathbf { a } , \quad v _ { n } ^ { 2 } = v _ { 0 } ^ { 2 } + 2 g n \Delta y - 2 \mu \Delta y \sum _ { j = 1 } ^ { n } \displaystyle \frac { 1 } { \cos \theta _ { j } } , \quad \mathbf { f o r } \operatorname { e a c h } n = 1 , 2 , \ldots , N , a } \\ & { \mathbf { b } . \quad w _ { n } = - \Delta y v _ { n } \sum _ { i = 1 } ^ { N } \displaystyle \frac { 1 } { v _ { i } ^ { 3 } \cos \theta _ { i } } , \quad \mathbf { f o r } \operatorname { e a c h } n = 1 , 2 , \ldots , N . } \end{array}$ nd

The constant $\upsilon _ { 0 }$ is the initial velocity of the granular material, $X$ is the $x$ -coordinate of the end of the chute, $\mu$ is the friction force, $N$ is the number of chute segments,and $g = 3 2 . 1 7 \mathrm { f t } / \mathrm { s } ^ { 2 }$ is the gravitational constant. The variable $\theta _ { i }$ is the angle of the ith chute segment from the vertical, as shown in the following figure,and $v _ { i }$ is the particle velocity in the ith chute segment.Solve (i) and (ii) for $\theta = ( \theta _ { 1 } , \dots , \theta _ { N } ) ^ { t }$ with $\mu = 0 , X = 2 , \Delta y = 0 . 2 , N = 2 0$ ,and $v _ { 0 } = 0$ ,where the values for $\upsilon _ { n }$ and $w _ { n }$ can be obtained directly from (a) and (b). Iterate until $\lvert | \theta ^ { ( k ) } - \theta ^ { ( k - 1 ) } \rvert | _ { \infty } < 1 0 ^ { - 2 }$

![](images/d0a9945f741b492f65679479189b6924cc802c334b144ca94990528b7c1780ee.jpg)

10. The amount of pressure required to sink a large, heavy object in a soft homogeneous soil that lies above a hard base soil can be predicted by the amount of pressure required to sink smaller objects in the same soil. Specifically, the amount of pressure $p$ required to sink a circular plate of radius $\boldsymbol { r }$ a distance $d$ in the soft soil, where the hard base soil lies a distance $D > d$ below the surface, can be approximated by an equation of the form

$$
p = k _ { 1 } e ^ { k _ { 2 } r } + k _ { 3 } r ,
$$

where ki,k2,and k3 are constants,with k2 > O,depending on d and the consistency of the soil but not on the radius of the plate. (See [Bek, pp. 89-94].)

a. Find the values of $k _ { 1 }$ ， $k _ { 2 }$ ,and $k _ { 3 }$ if we assume that a plate of radius 1 in. requires a pressure of 10 lb/in.² to sink 1 ft in a muddy feld, a plate of radius 2 in. requires a pressure of 12 lb/in.² to sink 1 ft,and a plate of radius 3 in. requires a pressure of $1 5 ~ \mathrm { l b } / \mathrm { i n }$ .2 to sink this distance (assuming that the mud is more than 1 ft deep).   
b. Use your calculations from part (a) to predict the minimal size of circular plate that would be required to sustain a load of 5oo lb on this feld with sinkage of less than 1 ft.

11. An interesting biological experiment (see [Schr2]) concerns the determination of the maximum water temperature, Xm,at which various species of hydra can survive without shortened life expectancy. One approach to the solution of this problem uses a weighted least squares fit of the form f(x)= y = α/(x -b) to a collection of experimental data.The x-values of the data refer to water temperature. The constant b is the asymptote of the graph of f and as such is an approximation to $X _ { M }$ ·

a. Show that choosing $a , b$ ,and $c$ to minimize

$$
\sum _ { i = 1 } ^ { n } \left[ w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right] ^ { 2 }
$$

reduces to solving the nonlinear system

$$
\begin{array} { l } { \displaystyle a = \sum _ { i = 1 } ^ { n } \frac { w _ { i } y _ { i } } { ( x _ { i } - b ) ^ { c } } \bigg / \sum _ { i = 1 } ^ { n } \frac { 1 } { ( x _ { i } - b ) ^ { 2 c } } , } \\ { \displaystyle 0 = \sum _ { i = 1 } ^ { n } \frac { w _ { i } y _ { i } } { ( x _ { i } - b ) ^ { c } } \cdot \sum _ { i = 1 } ^ { n } \frac { 1 } { ( x _ { i } - b ) ^ { 2 c + 1 } } - \sum _ { i = 1 } ^ { n } \frac { w _ { i } y _ { i } } { ( \star _ { i } - b ) ^ { c + 1 } } \cdot \sum _ { i = 1 } ^ { n } \frac { 1 } { ( x _ { i } - b ) ^ { 2 c } } , } \\ { \displaystyle 0 = \sum _ { i = 1 } ^ { n } \frac { w _ { i } y _ { i } } { ( x _ { i } - b ) ^ { c } } \cdot \sum _ { i = 1 } ^ { n } \frac { \ln ( x _ { i } - b ) } { ( x _ { i } - b ) ^ { 2 c } } - \sum _ { i = 1 } ^ { n } \frac { w _ { i } y _ { i } \ln ( x _ { i } - b ) } { ( x _ { i } - b ) ^ { c } } \cdot \sum _ { i = 1 } ^ { n } \frac { 1 } { ( x _ { i } - b ) ^ { 2 c } } } \end{array}
$$

b.Solve the nonlinear system for the species with the following data. Use the weights $w _ { i } =$ $\ln y _ { i }$

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>yi</td><td>2.40</td><td>3.80</td><td>4.75</td><td>21.60</td></tr><tr><td>Xi</td><td>31.8</td><td>31.5</td><td>31.2</td><td>30.2</td></tr></table>

# 10.3 Quasi-Newton Methods

A significant weakness of Newton's method for solving systems of nonlinear equations is that, for each iteration, a Jacobian matrix must be computed and an $n \times n$ linear system solved that involves this matrix. Consider the amount of computation associated with one iteration of Newton's method. The Jacobian matrix associated with a system of n nonlinear equations written in the form F(x) = O requires that the n² partial derivatives of the n component functions of F be determined and evaluated. In most situations, the exact evaluation of the partial derivatives is inconvenient, although the problem has been made more tractable with the widespread use of symbolic computation systems,such as Maple.

When the exact evaluation is not practical, we can use finite difference approximations to the partial derivatives. For example,

$$
\frac { \partial f _ { j } } { \partial x _ { k } } ( \mathbf { x } ^ { ( i ) } ) \approx \frac { f _ { j } ( \mathbf { x } ^ { ( i ) } + \mathbf { e } _ { k } h ) - f _ { j } ( \mathbf { x } ^ { ( i ) } ) } { h } ,
$$

where $h$ is small in absolute value and $\mathbf { \widehat { e } } _ { k }$ is the vector whose only nonzero entry is a 1 in the $k$ th coordinate. This approximation, however, still requires that at least $n ^ { 2 }$ scalar functional evaluations be performed to approximate the Jacobian and does not decrease the amount of calculation, in general $O ( n ^ { 3 } )$ , required for solving the linear system involving this approximate Jacobian. The total computational effort for just one iteration of Newton's method is consequently at least $n ^ { 2 } + n$ scalar functional evaluations ( $\cdot n ^ { 2 }$ for the evaluation of the Jacobian matrix and $\pmb { n }$ for the evaluation of $\mathbf { F }$ ） together with $O ( n ^ { 3 } )$ arithmetic operations to solve the linear system. This amount of computational effort is extensive, except for relatively small values of $n$ and easily evaluated scalar functions.

In this section we consider a generalization of the Secant method to systems of nonlinear equations,a technique known as Broyden's method (see [Broyl). The method requires only $n$ scalar functional evaluations per iteration and also reduces the number of arithmetic calculations to $O ( n ^ { 2 } )$ . It belongs to a class of methods known as least-change secant updates that produce algorithms called quasi-Newton. These methods replace the Jacobian matrix in Newton's method with an approximation matrix that is updated at each iteration. The disadvantage of the methods is that the quadratic convergence of Newton's method is lost, being replaced, in general, by a convergence called superlinear, which implies that

$$
\operatorname* { l i m } _ { i \to \infty } { \frac { \left\| \mathbf { x } ^ { ( i + 1 ) } - \mathbf { p } \right\| } { \left\| \mathbf { x } ^ { ( i ) } - \mathbf { p } \right\| } } = 0 ,
$$

where p denotes the solution to $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ and $\mathbf { x } ^ { ( i ) }$ and $\mathbf { x } ^ { ( i + 1 ) }$ are consecutive approximations to p.

In most applications,the reduction to superlinear convergence is a more than acceptable trade-off for the decrease in the amount of computation.An additional disadvantage of quasi-Newton methods is that, unlike Newton's method, they are not self-correcting. Newton's method will generally correct for roundoff error with successive iterations, but unless special safeguards are incorporated, Broyden's method will not.

To describe Broyden's method, suppose that an initial approximation $\mathbf { x } ^ { ( 0 ) }$ is given to the solution p of $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ . We calculate the next approximation $\mathbf { X } ^ { ( 1 ) }$ in the same manner as Newton's method, or, if it is inconvenient to determine ${ \cal J } ( { \bf x } ^ { ( 0 ) } )$ exactly, we use the dif-ference equations given by (10.10) to approximate the partial derivatives. To compute x(2), however,we depart from Newton's method and examine the Secant method for a single nonlinear equation. The Secant method uses the approximation

$$
f ^ { \prime } ( x _ { 1 } ) \approx { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } }
$$

as a replacement for $f ^ { \prime } ( x _ { 1 } )$ in Newton's method. For nonlinear systems, $\mathbf { X } ^ { ( 1 ) } - \mathbf { X } ^ { ( 0 ) }$ is a vec-tor, and the corresponding quotient is undefined. However, the method proceeds similarly in that we replace the matrix $J \left( \mathbf { x } ^ { ( 1 ) } \right)$ in Newton's method for systems by a matrix $A _ { 1 }$ with the property that

$$
A _ { 1 } \left( \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right) = \mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) - \mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) .
$$

Any nonzero vector in $\mathbb { R } ^ { n }$ can be written as the sum of a multiple of $\mathbf { X } ^ { ( 1 ) } - \mathbf { X } ^ { ( 0 ) }$ and a multiple of a vector in the orthogonal complement of $\mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) }$ . So, to uniquely define the matrix $\varLambda _ { 1 }$ , we need to specify how it acts on the orthogonal complement of $\mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) }$ . Since no information is available about the change in $\mathbf { F }$ in a direction orthogonal to $\mathbf { X } ^ { ( 1 ) } - \mathbf { X } ^ { ( 0 ) }$ ， we require that

$$
\begin{array} { r } { A _ { 1 } \mathbf { z } = J ( \mathbf { x } ^ { ( 0 ) } ) \mathbf { z } , \quad \mathrm { w h e n e v e r } \left( \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right) ^ { t } \mathbf { z } = 0 . } \end{array}
$$

Thus,any vector orthogonal to $\mathbf { X } ^ { ( 1 ) } - \mathbf { X } ^ { ( 0 ) }$ is unaffected by the update from $J ( \mathbf { x } ^ { ( 0 ) } )$ ,which was used to compute $\mathbf { x } ^ { ( 1 ) }$ ,to $A _ { 1 }$ , which is used in the determination of $\mathbf { x } ^ { ( 2 ) }$

Conditions (10.11) and (10.12) uniquely define $A _ { 1 }$ (see [DM]) as

$$
A _ { 1 } = J ( \mathbf { x } ^ { ( 0 ) } ) + \frac { \left[ \mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) - \mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) - J \left( \mathbf { x } ^ { ( 0 ) } \right) \left( \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right) \right] \left( \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right) ^ { t } } { \left\| \mathbf { x } ^ { ( 1 ) } - \mathbf { x } ^ { ( 0 ) } \right\| _ { 2 } ^ { 2 } } .
$$

It is this matrix that is used in place of $J \left( \mathbf { x } ^ { ( 1 ) } \right)$ to determine $\mathbf { x } ^ { ( 2 ) }$ as

$$
\mathbf { x } ^ { ( 2 ) } = \mathbf { x } ^ { ( 1 ) } - A _ { 1 } ^ { - 1 } \mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) .
$$

Once $\mathbf { x } ^ { ( 2 ) }$ has been determined, the method is repeated to determine $\mathbf { X } ^ { ( 3 ) }$ ,using $A _ { \downarrow }$ in place of $A _ { 0 } \equiv J \left( \mathbf { x } ^ { ( 0 ) } \right)$ ,and with $\mathbf { x } ^ { ( 2 ) }$ and $\mathbf { x } ^ { ( 1 ) }$ in place of $\mathbf { x } ^ { ( 1 ) }$ and $\mathbf { x } ^ { ( 0 ) }$ . In general, once $\mathbf { X } ^ { ( i ) }$ has been determined, $\mathbf { \boldsymbol { x } } ^ { ( i + 1 ) }$ is computed by

$$
A _ { i } = A _ { i - 1 } + { \frac { { \bf y } _ { i } - A _ { i - 1 } { \bf s } _ { i } } { | \vert { \bf s } _ { i } \vert \vert _ { 2 } ^ { 2 } } } { \bf s } _ { i } ^ { t }
$$

and

$$
\mathbf { x } ^ { ( i + 1 ) } = \mathbf { x } ^ { ( i ) } - A _ { i } ^ { - 1 } \mathbf { F } \left( \mathbf { x } ^ { ( i ) } \right) ,
$$

where the notation $\mathbf { y } _ { i } = \mathbf { F } \left( \mathbf { x } ^ { ( i ) } \right) - \mathbf { F } \left( \mathbf { x } ^ { ( i - 1 ) } \right)$ and $\mathbf { s } _ { i } = \mathbf { x } ^ { ( i ) } - \mathbf { x } ^ { ( i - 1 ) }$ is introduced to simplify the equations.

If the method is performed as outlined in Eqs. (10.13)and (10.14), the number of scalar functional evaluations is reduced from $n ^ { 2 } + n$ to $\pmb { n }$ (those required for evaluating $\mathbf { F } \left\{ \mathbf { x } ^ { ( i ) } \right\} )$ ， but $O ( n ^ { 3 } )$ calculations are still required to solve the associated $n \times n$ linear system (see Step 4 in Algorithm 10.1)

$$
A _ { i } \mathbf { s } _ { i + 1 } = - \mathbf { F } \left( \mathbf { x } ^ { ( i ) } \right) .
$$

Employing the method in this form would not be justified because of the reduction to superlinear convergence from the quadratic convergence of Newton's method.

A considerable improvement can be incorporated, however, by employing a matrix inversion formula of Sherman and Morrison (see,for example,[DM, p. 55]).

# Theorem 10.8 (Sherman-Morrison Formula)

If $A$ is a nonsingular matrix and $\mathbf { x }$ and $\mathbf { y }$ are vectors, then $\boldsymbol { A } + \mathbf { x y } ^ { t }$ is nonsingular, provided that $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ , and

$$
\left( A + \mathbf { x y } ^ { t } \right) ^ { - 1 } = A ^ { - 1 } - { \frac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } .
$$

TheSheas $A _ { i } ^ { - 1 }$ to e computedirel om $A _ { i - 1 } ^ { - 1 }$ eliminating the need for a matrix inversion with each iteration. By letting $A \ = \ A _ { i - 1 }$ ， $\mathbf { x } = ( \mathbf { y } _ { i } - A _ { i - 1 } \mathbf { s } _ { i } ) / \vert \vert \mathbf { s } _ { i } \vert \vert _ { 2 } ^ { 2 }$ ,and $\mathbf { y } = \mathbf { s } _ { i }$ ,Eq.(10.13) together with Theorem 10.8 imply that

$$
\begin{array} { r l r } {  { A _ { i } ^ { - 1 } = ( A _ { i - 1 } + \frac { \mathbb { Y } _ { i } - A _ { i - 1 } \mathbb { S } _ { i } } { \| { \bf S } _ { i } \| _ { 2 } ^ { 2 } } { \bf s } _ { i } ^ { t } ) ^ { - 2 } } } \\ & { } & \\ & { } & { = A _ { i - 1 } ^ { - 1 } - \frac { A _ { i - 1 } ^ { - 1 } ( \frac { \mathbb { Y } _ { i } - A _ { i - 1 } \mathbb { S } _ { i } } { \| { \bf S } _ { i } \| _ { 2 } ^ { 2 } } s _ { i } ^ { t } ) A _ { i - 1 } ^ { - 1 } } { 1 + s _ { i } ^ { \ell } A _ { i - 1 } ^ { - 1 } ( \frac { \mathbb { Y } _ { i } - A _ { i - 1 } \mathbb { S } _ { i } } { \| { \bf S } _ { i } \| _ { 2 } ^ { 2 } } ) } } \\ & { } & \\ & { } & { = A _ { i - 1 } ^ { - 1 } - \frac { ( A _ { i - 1 } ^ { - 1 } \mathbb { Y } _ { i } - \mathbb { S } _ { i } ) s _ { i } ^ { t } A _ { i - 1 } ^ { - 1 } } { \| { \bf S } _ { i } \| _ { 2 } ^ { 2 } + s _ { i } ^ { \ell } A _ { i - 1 } ^ { - 1 } \mathbb { Y } _ { i } - \| { \bf S } _ { i } \| _ { 2 } ^ { 2 } } , } \end{array}
$$

so

$$
A _ { i } ^ { - 1 } = A _ { i - 1 } ^ { - 1 } + { \frac { \left( { \bf s } _ { i } - A _ { i - 1 } ^ { - 1 } { \bf y } _ { i } \right) { \bf s } _ { i } ^ { t } A _ { i - 1 } ^ { - 1 } } { { \bf s } _ { i } ^ { t } A _ { i - 1 } ^ { - 1 } { \bf y } _ { i } } } .
$$

This computation involves only matrix-vector multiplication at each step and therefore requires only $O ( n ^ { 2 } )$ arithmetic calculations. The calculation of $A _ { i }$ is bypassed,as is the necessity of solving the linear system (10.15). Algorithm 10.2 follows directly from this construction, incorporating (10.16) into the iterative technique (10.14).

# Broyden

To approximate the solution of the nonlinear system $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ given an initial approximation x:

INPUTnumber $\pmb { n }$ of equations and unknowns; initial approximation $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ ； tolerance TOL; maximum number of iterations $N$

OUTPUT approximate solution $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ or a message that the number of iterations was exceeded.

Step1 Set $\begin{array} { r l } & { A _ { 0 } = J ( \mathbf { x } ) \mathrm { ~ w h e r e ~ } J ( \mathbf { x } ) _ { i , j } = \frac { \partial f _ { i } } { \partial x _ { j } } ( \mathbf { x } ) \mathrm { ~ f o r ~ } 1 \leq i , j \leq n ; } \\ & { \mathbf { v } = \mathbf { F } ( \mathbf { x } ) . ( N o t e . \mathbf { \ v } = \mathbf { F } ( \mathbf { x } ^ { ( 0 ) } ) . ) } \end{array}$

Step 2 Set $A = A _ { 0 } ^ { - 1 }$ .(Use Gaussian elimination.)

Step3 Set $\begin{array} { l l } { { ; } \mathbf { s } = - A \mathbf { v } ; \quad ( N o t e \colon \mathbf { s } = \mathbf { s } _ { 1 } . ) } \\ { { \mathbf { x } } = \mathbf { x } + \mathbf { s } ; \quad ( N o t e \colon \mathbf { x } = \mathbf { x } ^ { ( 1 ) } . ) } \\ { { k } = 2 . } \end{array}$

Step 4 While $( k \leq N )$ do Steps 5-13.

$$
\begin{array} { r l } { { 2 } p ^ { \zeta } } & { \operatorname { S e t } \mathbf { w } = \mathbf { v } ; \quad ( S a \nu e ~ \mathbf { v } . ) } \\ & { \qquad \mathbf { v } = \mathbf { F } ( \mathbf { x } ) ; \quad ( N o t e . \mathbf { v } = \mathbf { F } ( \mathbf { x } ^ { ( k ) } ) . ) } \\ & { \qquad \mathbf { y } = \mathbf { v } - \mathbf { w } . \quad ( N o t e . \mathbf { y } = \mathbf { y } _ { k } . ) } \end{array}
$$

Step 6 Set $\mathbf { z } = - A \mathbf { y }$ $( N o t e ; { \mathbf z } = - A _ { k - 1 } ^ { - 1 } { \mathbf y } _ { k } . )$   
Step 7 Set ${ \boldsymbol { p } } = - \mathbf { s } ^ { t } \mathbf { z }$ $( N o t e \colon p = s _ { k } ^ { t } A _ { k - 1 } ^ { - 1 } \mathbf { y } _ { k } . )$   
Step 8 Set ${ \mathbf { u } } ^ { t } = { \mathbf { s } } ^ { t } A$   
Step 9 Set $\begin{array} { r } { A = A + \frac { 1 } { p } ( \mathbf { s } + \mathbf { z } ) \mathbf { u } ^ { t } . \quad ( N o t e . ~ A = A _ { k } ^ { - 1 } . ) } \end{array}$   
Step 10 $\mathrm { S e t } \ \mathbf { s } = - A \mathbf { v } . ( N o t e { \cdot } \ \mathbf { s } = - A _ { k } ^ { - 1 } \mathbf { F } ( \mathbf { x } ^ { ( k ) } ) . )$   
Step 11 Set $\mathbf { x } = \mathbf { x } + \mathbf { s }$ $( N o t e ; { \bf x } = { \bf x } ^ { ( k + 1 ) } .$ ）   
Step 12 If $| | \mathbf { s } | | < T O L$ then OUTPUT $\mathbf { \mu } ( \mathbf { x } )$ ； (The procedure was successful. STOP.

Step 13 Set $k = k + 1$

Step 14OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

The nonlinear system

$$
{ \begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - { \frac { 1 } { 2 } } = 0 , } \\ { x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + { \frac { 1 0 \pi - 3 } { 3 } } = 0 } \end{array} }
$$

was solved by Newton's method in Example 1 of Section 10.2. The Jacobian matrix for this system is

$$
J ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \left[ { \begin{array} { c c c } { 3 } & { x _ { 3 } \sin x _ { 2 } x _ { 3 } } & { x _ { 2 } \sin x _ { 2 } x _ { 3 } } \\ { 2 x _ { 1 } } & { - 1 6 2 ( x _ { 2 } + 0 . 1 ) } & { \cos x _ { 3 } } \\ { - x _ { 2 } e ^ { - x _ { 1 } x _ { 2 } } } & { - x _ { 1 } e ^ { - x _ { 1 } x _ { 2 } } } & { 2 0 } \end{array} } \right] .
$$

Let $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 , 0 . 1 , - 0 . 1 ) ^ { t }$ and

$$
\mathbf { F } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = ( f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) , f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ) ^ { t } ,
$$

where

$$
\begin{array} { l } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \displaystyle 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \frac 1 2 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 , } \end{array}
$$

and

$$
f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \frac { 1 0 \pi - 3 } { 3 } .
$$

Then

$$
\begin{array} { r } { \mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) = \left[ \begin{array} { c } { - 1 . 1 9 9 9 5 0 } \\ { - 2 . 2 6 9 8 3 3 } \\ { 8 . 4 6 2 0 2 5 } \end{array} \right] , } \end{array}
$$

and since

$$
\begin{array} { c c } { A _ { 0 } = J \left( x _ { 1 } ^ { \left( 0 \right) } , x _ { 2 } ^ { \left( 0 \right) } , x _ { 3 } ^ { \left( 0 \right) } \right) } \\ { \ } \\ { = \left[ \begin{array} { c c c c } { 3 } & { 9 . 9 9 9 8 3 3 \times 1 0 ^ { - 4 } } & { - 9 . 9 9 9 8 3 3 \times 1 0 ^ { - 4 } } \\ { 0 . 2 } & { - 3 2 . 4 } & { 0 . 9 9 5 0 0 4 2 } \\ { - 9 . 9 0 0 4 9 8 \times 1 0 ^ { - 2 } } & { - 9 . 9 0 0 4 9 8 \times 1 0 ^ { - 2 } } & { 2 0 } \end{array} \right] , } \end{array}
$$

we have

$$
\begin{array} { r l } { A _ { 0 } ^ { - 1 } = J \left( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , x _ { 3 } ^ { ( 0 ) } \right) ^ { - 1 } } & { } \\ { = \left[ \begin{array} { c c c } { 0 . 3 3 3 3 3 3 2 } & { 1 . 0 2 3 8 5 2 \times 1 0 ^ { - 5 } } & { 1 . 6 1 5 7 } \\ { 2 . 1 0 8 6 0 7 \times 1 0 ^ { - 3 } } & { - 3 . 0 8 6 8 8 3 \times 1 0 ^ { - 2 } } & { 1 . 5 3 5 8 } \\ { 1 . 6 6 0 5 2 0 \times 1 0 ^ { - 3 } } & { - 1 . 5 2 7 5 7 7 \times 1 0 ^ { - 4 } } & { 5 . 0 0 0 7 } \end{array} \right. } \end{array}
$$

So

$$
\begin{array} { r } { \mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - A _ { 0 } ^ { - 1 } \mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) = \left[ \begin{array} { c } { 0 . 4 9 9 8 6 9 7 } \\ { 1 . 9 4 6 6 8 5 \times 1 0 ^ { - 2 } } \\ { - 0 . 5 2 1 5 2 0 5 } \end{array} \right] , } \end{array}
$$

$$
\mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) = \left[ \begin{array} { c } { - 3 . 3 9 4 4 6 5 \times 1 0 ^ { - 4 } } \\ { - 0 . 3 4 4 3 8 7 9 } \\ { 3 . 1 8 8 2 3 8 \times 1 0 ^ { - 2 } } \end{array} \right] ,
$$

$$
\mathbf { y } _ { 1 } = \mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) - \mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) = \left[ \begin{array} { l } { 1 . 1 9 9 6 1 1 } \\ { 1 . 9 2 5 4 4 5 } \\ { - 8 . 4 3 0 1 4 3 } \end{array} \right] ,
$$

$$
\mathbf { s } _ { 1 } = \left[ \begin{array} { c } { 0 . 3 9 9 8 6 9 7 } \\ { - 8 . 0 5 3 3 1 5 \times 1 0 ^ { - 2 } } \\ { - 0 . 4 2 1 5 2 0 4 } \end{array} \right] ,
$$

$\mathbf { s } _ { 1 } ^ { t } A _ { 0 } ^ { - 1 } \mathbf { y } _ { 1 } = 0 . 3 4 2 4 6 0 4$

$$
A _ { 1 } ^ { - 1 } = A _ { 0 } ^ { - 1 } + ( 1 / 0 . 3 4 2 4 6 0 4 ) \left[ \left( \mathfrak { s } _ { 1 } - A _ { 0 } ^ { - 1 } \mathbf { y } _ { 1 } \right) \mathbf { s } _ { 1 } ^ { t } A _ { 0 } ^ { - 1 } \right]
$$

and

$$
\mathbf { x } ^ { ( 2 ) } = \mathbf { x } ^ { ( 1 ) } - A _ { 1 } ^ { - 1 } \mathbf { F } \left( \mathbf { x } ^ { ( 1 ) } \right) = \left[ \begin{array} { c } { 0 . 4 9 9 9 8 6 3 } \\ { 8 . 7 3 7 8 3 3 \times 1 0 ^ { - 3 } } \\ { - 0 . 5 2 3 1 7 4 6 } \end{array} \right] .
$$

Additional iterations are listed in Table 1O.4. The fifth iteration of Broyden's method is slightly less accurate than was the fourth iteration of Newton's method given in the example at the end of the preceding section.

# Table 10.4

<table><tr><td>k</td><td>x（</td><td>海</td><td>海</td><td>/x(k）-x(k-1)1|2</td></tr><tr><td>3</td><td>0.5000066</td><td>8.672157 × 10-4</td><td>-0.5236918</td><td>7.88×10-3</td></tr><tr><td>4</td><td>0.5000003</td><td>6.083352 10-5 ×</td><td>-0.5235954</td><td>8.12 ×10-4</td></tr><tr><td>5</td><td>0.5000000</td><td>--1.448889 10-6 ×</td><td>-0.5235989</td><td>6.24× 10-5</td></tr><tr><td>6</td><td>0.5000000</td><td>6.059030 10-9 ×</td><td>-0.5235988</td><td>1.50 × 10-6</td></tr></table>

Procedures are also available that maintain quadratic convergence but significantly reduce the number of required functional evaluations. Methods of this type were originally proposed by Brown [Brow,K]. A survey and comparison of some commonly used methods of this type can be found in [MC]. In general, however, these methods are much more difficult to implement efficiently than Broyden's method.

# EXERCISE SET 10.3

1. Use Broyden's method with $\mathbf { x } ^ { ( 0 ) } = \mathbf { 0 }$ to compute $\mathbf { x } ^ { ( 2 ) }$ for each of the following nonlinear systems.

$\begin{array} { r l r } { \mathrm { \small ~ \displaystyle ~ \frac ~ { \small ~ 1 } ~ { \Omega ~ } ~ } } & { { } 4 x _ { 1 } ^ { 2 } - 2 0 x _ { 1 } + \frac { 1 } { 4 } x _ { 2 } ^ { 2 } + 8 = 0 , \qquad } & { \mathrm { \small ~ \displaystyle ~ b . ~ } } & { \sin ( 4 \pi x _ { 1 } x _ { 2 } ) - 2 x _ { 2 } - x _ { 1 } = 0 , } \\ { \mathrm { \small ~ \displaystyle ~ \frac { 1 } { 2 } ~ } x _ { 1 } x _ { 2 } ^ { 2 } + 2 x _ { 1 } - 5 x _ { 2 } + 8 = 0 . } & { { } \qquad } & { \left( \frac { 4 \pi - 1 } { 4 \pi } \right) ( e ^ { 2 x _ { 1 } } - e ) + 4 e x _ { 2 } ^ { 2 } - 2 e x _ { \mathrm { t } } = 0 . } \end{array}$   
c. $\begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \displaystyle \frac { 1 } { 2 } = 0 , } \\ { 4 x _ { 1 } ^ { 2 } - 6 2 5 x _ { 2 } ^ { 2 } + 2 x _ { 2 } - 1 = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 . } \end{array}$ $\begin{array} { r l r } { \mathbf { d . } } & { } & { x _ { 1 } ^ { 2 } + x _ { 2 } - 3 7 = 0 , } \\ & { } & { x _ { 1 } - x _ { 2 } ^ { 2 } - 5 = 0 , } \\ & { } & { x _ { 1 } + x _ { 2 } + x _ { 3 } - 3 = 0 . } \end{array}$

2. Use Broyden's method to approximate solutions to the nonlinear systems in Exercise 1. Iterate until $\| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \| _ { \infty } < 1 0 ^ { - 6 }$ . The initial approximations $\mathbf { X } ^ { ( 0 ) }$ in Exercise 1 may not lead to convergence. If it does not, use a different value of $\mathbf { x } ^ { ( 0 ) }$ ，

3. Use Broyden's method to find a solution to the following nonlinear systems.Iterate until $\| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \| _ { \infty } < 1 0 ^ { - 6 }$

a. $3 x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } = 0 ,$ $\begin{array} { r l } { \mathbf { b . } } & { \ln ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) - \sin ( x _ { 1 } x _ { 2 } ) = \ln 2 + \ln \pi . } \\ & { \qquad e ^ { x _ { 1 } - x _ { 2 } } + \cos ( x _ { 1 } x _ { 2 } ) = 0 . } \end{array}$ $3 x _ { 1 } x _ { 2 } ^ { 2 } - x _ { 1 } ^ { 3 } - 1 = 0 .$ Use $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t }$ $\operatorname { U s e } \mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { t }$

$$
\begin{array} { r l } { x _ { 1 } ^ { 3 } + x _ { 1 } ^ { 2 } x _ { 2 } - x _ { 1 } x _ { 3 } + 6 = 0 , } & { \qquad \mathbf { d . } } \\ { e ^ { x _ { 1 } } + e ^ { x _ { 2 } } - x _ { 3 } = 0 , } & { \qquad 9 x _ { 2 } + \sqrt { x _ { 1 } ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 } + 0 . 9 = 0 , } \\ { x _ { 2 } ^ { 2 } - 2 x _ { 1 } x _ { 3 } = 4 . } & { \qquad 6 0 x _ { 3 } + 3 e ^ { - x _ { 1 } x _ { 2 } } + 1 0 \pi - 3 = 0 . } \\ { s e \mathbf { x } ^ { \scriptscriptstyle ( 0 ) } = ( - 1 , - 2 , 1 ) ^ { t } . } & { \qquad \mathrm { U s e \ } \mathbf { x } ^ { \scriptscriptstyle ( 0 ) } = ( 0 , 0 , 0 ) ^ { t } . } \end{array}
$$

4. Use Broyden's method to approximate solutions to the following nonlinear systems. Iterate until $\left\| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \right\| _ { \infty } < 1 0 ^ { - 6 }$

$$
\begin{array} { r l } { \qquad x _ { 1 } ( 1 - x _ { 1 } ) + 4 x _ { 2 } = 1 2 , } & { \qquad \mathbf { b } . } \\ { ( x _ { 1 } - 2 ) ^ { 2 } + ( 2 x _ { 2 } - 3 ) ^ { 2 } = 2 5 . } \\ { 1 5 x _ { 1 } + x _ { 2 } ^ { 2 } - 4 x _ { 3 } = 1 3 , } & { \qquad \mathbf { d } . } \\ { x _ { 1 } ^ { 2 } + 1 0 x _ { 2 } - x _ { 3 } = 1 1 , } & { \qquad \mathbf { 8 } x _ { 2 } ^ { 2 } + 4 x _ { 3 } ^ { 2 } - 9 = 0 , } \\ { x _ { 2 } ^ { 3 } - 2 5 x _ { 3 } = - 2 2 . } \end{array}
$$

5. The nonlinear system

$$
\begin{array} { r } { 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \displaystyle \frac { 1 } { 2 } = 0 , } \\ { x _ { 1 } ^ { 2 } - 6 2 5 x _ { 2 } ^ { 2 } - \displaystyle \frac { 1 } { 4 } = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 } \end{array}
$$

has a singular Jacobian matrix at the solution. Apply Broyden's method with $\mathbf { x } ^ { ( 0 ) } = \left( 1 , 1 - \mathbb { 1 } \right) ^ { t }$ Note that convergence may be slow or may not occur within a reasonable number of iterations.

6. The nonlinear system

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 } } \end{array}
$$

has six solutions.

a. Show that if $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution then $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , - x _ { 4 } ) ^ { t }$ is a solution. $\mathbf { b } .$ Use Broyden's method three times to approximate each solution. Iterate until $\left\| \mathbf { X } ^ { ( k ) } - \right.$ $\mathbf { x } ^ { ( k - 1 ) } \big \| _ { \infty } < 1 0 ^ { - 5 }$

7. Exercise 13 of Section 8.1 dealt with determining an exponential least squares relationship of the form $R \ : = \ : b w ^ { a }$ to approximate a collection of data relating the weight and respira-tion rule of Modest sphinx moths. In that exercise, the problem was converted to a log-log relationship,and in part (c),a quadratic term was introduced in an attempt to improve the approximation. Instead of converting the problem, determine the constants $\pmb { a }$ and $b$ that minimize $\scriptstyle \sum _ { i = 1 } ^ { n } ( R _ { i } - b w _ { i } ^ { \alpha } ) ^ { 2 }$ for the data listed in Exercise 13 of 8.1. Compute the error associated with this approximation,and compare this to the error of the previous approximations for this problem.

8.Show that if $\mathbf { 0 } \neq \mathbf { y } \in \mathbb { R } ^ { n }$ and $\mathbf { z } \in \mathbb { R } ^ { n }$ ,then ${ \bf z } = { \bf z } _ { 1 } + { \bf z } _ { 2 }$ , where $\mathbf { z } _ { 1 } = ( \mathbf { y } ^ { t } \mathbf { z } / \| \mathbf { y } \| _ { 2 } ^ { 2 } ) \mathbf { y }$ is parallel to$\mathbf { y }$ and $\pmb { z } _ { 2 }$ is orthogonal to $\mathbf { y }$ ：

9.Show that if u, $\boldsymbol { \mathsf { v } } \in \mathbb { R } ^ { n }$ ,then $\mathrm { d e t } ( I + \mathbf { u } \mathbf { v } ^ { t } ) = 1 + \mathbf { v } ^ { t } \mathbf { u } .$

10.a.Use the result in Exercise 9 to show that if $A ^ { - 1 }$ exists and $\mathbf { x } , \mathbf { y } \in \mathbb { R } ^ { n }$ ,then $( A + \mathbf { x } \mathbf { y } ^ { t } ) ^ { - 1 }$ exists if and only if $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ b.By multiplying on the right by $\boldsymbol { A } + \mathbf { x y } ^ { t }$ , show that when $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ we have

$$
( A + \mathbf { x y } ^ { t } ) ^ { - 1 } = A ^ { - 1 } - { \frac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } .
$$

# 10.4 Steepest Descent Techniques

The advantage of the Newton and quasi-Newton methods for solving systems of nonlinear equations is their speed of convergence once a suficiently accurate approximation is known. A weakness of these methods is that an accurate initial approximation to the solution is needed to ensure convergence. The Steepest Descent method considered in this section converges only linearly to the solution, but it will usually converge even for poor initial approximations.As a consequence,this method is used to find sufficiently accurate starting approximations for the Newton-based techniques in the same way the Bisection method is used for a single equation.

The method of Steepest Descent determines a local minimum for a multivariable function of the form $g : \mathbb { R } ^ { n } \to \mathbb { R }$ . The method is valuable quite apart from the application as a starting method for solving nonlinear systems. (Some other applications are considered in the exercises.)

The connection between the minimization of a function from $\textstyle \mathbb { R } ^ { n }$ to $\mathbb { R }$ and the solution of a system of nonlinear equations is due to the fact that a system of the form

$$
\begin{array} { r } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) = 0 , } \end{array}
$$

$$
f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 ,
$$

has a solution at $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ precisely when the function $\pmb { g }$ defined by

$$
g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = \sum _ { i = 1 } ^ { n } [ f _ { i } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ] ^ { 2 }
$$

has the minimal value 0.

The method of Steepest Descent for finding a local minimum for an arbitrary function $g$ from $\textstyle \mathbb { R } ^ { n }$ into $\mathbb { R }$ can be intuitively described as follows:

1. Evaluate $\pmb { g }$ at an il aproxinaion $\mathbf { x } ^ { ( 0 ) } = \left( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , \ldots , x _ { n } ^ { ( 0 ) } \right) ^ { t } ,$

2. Determine a direction from $\mathbf { x } ^ { ( 0 ) }$ that results in a decrease in the value of $g$ 3. Move an appropriate amount in this direction and call the new value $\mathbf { x } ^ { ( 1 ) }$

4.Repeat steps 1 through 3 with $\mathbf { x } ^ { ( 0 ) }$ replaced by $\mathbf { x } ^ { ( 1 ) }$ .

Before describing how to choose the correct direction and the appropriate distance to move in this direction, we need to review some results from calculus. The Extreme Value Theorem states that a differentiable single-variable function can have a relative minimum only when the derivative is zero. To extend this result to multivariable functions, we need the following definition.

# Definition 10.9

For $g : { \mathbb { R } ^ { n } }  { \mathbb { R } } \quad$ , the gradient of $g$ at $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ is denoted $\nabla g ( { \pmb x } )$ and defined by

$$
\nabla g ( { \mathbf x } ) = \left( \frac { \partial g } { \partial x _ { 1 } } ( { \mathbf x } ) , \frac { \partial g } { \partial x _ { 2 } } ( { \mathbf x } ) , \dots , \frac { \partial g } { \partial x _ { n } } ( { \mathbf x } ) \right) ^ { t } .
$$

The gradient for a multivariable function is analogous to the derivative of a singlevariable function in the sense that a diffrentiable multivariable function can have a relative minimum at $\mathbf { x }$ only when the gradient at $\mathbf { x }$ is the zero vector.

The gradient hasanother important propertyconnected with the minimization of multivariable functions. Suppose that $\mathbf { v } = ( v _ { 1 } , v _ { 2 } , \ldots , v _ { n } ) ^ { t }$ is a unit vector in $\mathbb { R } ^ { n }$ ; that is,

$$
| | \mathbf { v } | | _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } v _ { i } ^ { 2 } = 1 .
$$

The directional derivative of $\pmb { g }$ at $\mathbf { x }$ in the direction of v is defined by

$$
D _ { \mathbf { v } } g ( \mathbf { x } ) = \operatorname* { l i m } _ { h  0 } \frac { 1 } { h } [ g ( \mathbf { x } + h \mathbf { v } ) - g ( \mathbf { x } ) ] = \mathbf { v } ^ { t } \cdot \nabla g ( \mathbf { x } ) .
$$

The directional derivative of $\pmb { g }$ at $\bf { x }$ in the direction of $\pmb { \nu }$ measures the change in the value of the function $\pmb { g }$ relative to the change in the variable in the direction of $\pmb { \gamma }$

![](images/3f5fa18824bccc4c2d3e0ddf257be8af60a6137c30fa35651f82ec5c56032b87.jpg)  
Figure 10.3

A standard result from the calculus of multivariable functions states that, when $\pmb { g }$ is differentiable, the direction that produces the maximum value for the directional derivative occurs when $\pmb { \ v }$ is chosen to be parallel to $\nabla g ( \mathbf { x } )$ ， provided that $\nabla g ( \mathbf { x } ) \neq \mathbf { 0 }$ . As a con-sequence, the direction of greatest decrease in the value of ${ \pmb g }$ at $\pmb { \mathrm { x } }$ is the direction given by $- \nabla g ( \mathbf { x } )$ . (See Figure 10.3 on page 629 for an illustration when $\pmb { g }$ is a function of two variables.)

The object is to reduce $g ( \mathbf { x } )$ to its minimal value of zero, so an appropriate choice for $\mathbf { x } ^ { ( 1 ) }$ is

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - \alpha \nabla g ( \mathbf { x } ^ { ( 0 ) } ) , \quad \mathrm { f o r ~ s o m e ~ c o n s t a n t } \alpha > 0 .
$$

The problem now reduces to choosing $\pmb { \alpha }$ so that $g \left( \mathbf { x } ^ { ( 1 ) } \right)$ will be significantly less than $g \left( \mathbf { x } ^ { ( 0 ) } \right)$ .To determine anappropriate choice for the value $\pmb { \alpha }$ ,we consider the single-variable function

$$
h ( \alpha ) = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) .
$$

The value of $\pmb { \alpha }$ that minimizes $h$ is the value needed for Eq. (10.17).

Finding a minimal value for $h$ directly would require differentiating $h$ and then solving a root-finding problem to determine the critical points of $h$ . This procedure is generally too costly. Instead, we choose three numbers α1 < α2 < α3 that, we hope,are close to where the minimum value of $h ( \alpha )$ occurs. Then we construct the quadratic polynomial $P ( x )$ that interpolates $h$ at $\pmb { \alpha } _ { 1 } , \pmb { \alpha } _ { 2 }$ ,and $\pmb { \alpha _ { 3 } }$ . We define $\hat { \pmb { \alpha } }$ in $[ \alpha _ { 1 } , \alpha _ { 3 } ]$ so that $P ( \hat { \alpha } )$ is a minimum in $\{ \alpha _ { 1 } , \alpha _ { 3 } \}$ and use $P ( \hat { \alpha } )$ to approximate the minimal value of $h ( \alpha )$ . Then $\hat { \pmb { \alpha } }$ is used to determine the new iterate for approximating the minimal value of $\pmb { g }$ ：

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - \hat { \alpha } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) .
$$

Since $g \left( \mathbf { x } ^ { ( 0 ) } \right)$ is available,we first choose ${ \pmb { \alpha } } _ { 1 } = 0$ to minimize the computation. Next a number ${ \pmb { \alpha } } _ { 3 }$ is found with $h ( \alpha _ { 3 } ) < h ( \alpha _ { 1 } )$ . (Since ${ \pmb { \alpha } } _ { 1 }$ does not minimize $h$ , such a number $\pmb { \alpha } _ { 3 }$ does exist.) Finally, $\pmb { \alpha _ { 2 } }$ is chosen to be $\alpha _ { 3 } / 2$

The minimum value of $P$ on $[ \alpha _ { 1 } , \alpha _ { 3 } ]$ occurs either at the only critical point of $P$ 0r at the right endpoint α3 because,by assumption, P(α3) = h(α3) < h(α1) = P(α1). The critical point is easily determined since $P$ is a quadratic polynomial.

To find a reasonable starting approximation to the solution of the nonlinear system

$$
\begin{array} { l } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \displaystyle 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \frac 1 2 = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \frac { 1 0 \pi - 3 } { 3 } = 0 , } \end{array}
$$

we use the Steepest Descent method with $\mathbf { x } ^ { ( 0 ) } = ( \mathbf { 0 } , \mathbf { 0 } , \mathbf { 0 } ) ^ { t }$ ·

$$
\colon g ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = [ f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ] ^ { 2 } + [ f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ] ^ { 2 } + [ f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ] ^ { 2 }
$$

$$
\nabla g ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) \equiv \nabla g ( \mathbf { x } ) = \left( 2 f _ { 1 } ( \mathbf { x } ) \frac { \partial f _ { 1 } } { \partial x _ { 1 } } ( \mathbf { x } ) + 2 f _ { 2 } ( \mathbf { x } ) \frac { \partial f _ { 2 } } { \partial x _ { 1 } } ( \mathbf { x } ) + 2 f _ { 3 } ( \mathbf { x } ) \frac { \partial f _ { 3 } } { \partial x _ { 1 } } ( \mathbf { x } ) , \right.
$$

$$
2 f _ { 1 } ( { \bf x } ) \frac { \partial f _ { 1 } } { \partial x _ { 2 } } ( { \bf x } ) + 2 f _ { 2 } ( { \bf x } ) \frac { \partial f _ { 2 } } { \partial x _ { 2 } } ( { \bf x } ) + 2 f _ { 3 } ( { \bf x } ) \frac { \partial f _ { 3 } } { \partial x _ { 2 } } ( { \bf x } ) ,
$$

$$
2 f _ { 1 } ( { \bf x } ) \frac { \partial f _ { 1 } } { \partial x _ { 3 } } ( { \bf x } ) + 2 f _ { 2 } ( { \bf x } ) \frac { \partial f _ { 2 } } { \partial x _ { 3 } } ( { \bf x } ) + 2 f _ { 3 } ( { \bf x } ) \frac { \partial f _ { 3 } } { \partial x _ { 3 } } ( { \bf x } ) \bigg )
$$

$$
= 2 \mathbf { J } ( \mathbf { x } ) ^ { t } \mathbf { F } ( \mathbf { x } ) .
$$

For $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have

$$
g \left( \mathbf { x } ^ { ( 0 ) } \right) = 1 1 1 . 9 7 5 \quad \mathrm { a n d } \quad z _ { 0 } = | | \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) | | _ { 2 } = 4 1 9 . 5 5 4 .
$$

Let

$$
{ \bf z } = \frac { 1 } { z _ { 0 } } \nabla g \left( { \bf x } ^ { ( 0 ) } \right) = ( - 0 . 0 2 1 4 5 1 4 , - 0 . 0 1 9 3 0 6 2 , 0 . 9 9 9 5 8 3 ) ^ { t } .
$$

With ${ \pmb { \alpha } } _ { 1 } = 0$ , we have $g _ { 1 } = g \left( { \bf x } ^ { ( 0 ) } - \alpha _ { 1 } z \right) = g \left( { \bf x } ^ { ( 0 ) } \right) = 1 1 1 . 9 7 5$ . We arbitrarily let $\alpha _ { 3 } = 1$ so that

$$
g _ { 3 } = g \left( { \bf x } ^ { ( 0 ) } - \alpha _ { 3 } { \bf z } \right) = 9 3 . 5 6 4 9 .
$$

Since $g _ { 3 } < g _ { 1 }$ , we accept $\pmb { \alpha _ { 3 } }$ and set $\alpha _ { 2 } = 0 . 5$ .Thus,

$$
\begin{array} { r } { g _ { 2 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \mathbf { z } \right) = 2 . 5 3 5 5 7 . } \end{array}
$$

We now form the Newton's forward divided-difference interpolating polynomial

$$
P ( \alpha ) = g _ { 1 } + h _ { 1 } \alpha + h _ { 3 } \alpha ( \alpha - \alpha _ { 2 } )
$$

that interpolates

$$
g \left( \mathbf { x } ^ { ( 0 ) } - \alpha \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha \mathbf { z } \right)
$$

at ${ \pmb { \alpha } } _ { 1 } = 0$ ， $\alpha _ { 2 } = 0 . 5$ ,and $\alpha _ { 3 } = 1$ as follows:

$$
\begin{array} { l } { { \begin{array} { l l l l } { { ^ { \mathrm { \tiny ~ \times ~ } } } } & { { ^ { \mathrm { \tiny ~ \times ~ } } } } & { { ^ { \mathrm { \tiny ~ \times ~ } } } } & { { ^ { \mathrm { \tiny ~ \times ~ } } } } \\ { { } } & { { \alpha _ { 2 } = 0 . 5 , } } & { { g _ { 2 } = 2 . 5 3 5 5 7 , } } & { { h _ { 1 } = \displaystyle \frac { g _ { 2 } - g _ { 1 } } { \alpha _ { 2 } - \alpha _ { 1 } } = - 2 1 8 . 8 7 8 , } } \\ { { } } & { { } } & { { } } \\ { { \alpha _ { 3 } = 1 , } } & { { g _ { 3 } = 9 3 . 5 6 4 9 , } } & { { h _ { 2 } = \displaystyle \frac { g _ { 3 } - g _ { 2 } } { \alpha _ { 3 } - \alpha _ { 2 } } = 1 8 2 . 0 5 9 , } } & { { h _ { 3 } = \displaystyle \frac { h _ { 2 } - h _ { 1 } } { \alpha _ { 3 } - \alpha _ { 1 } } = 4 0 0 . 5 } } \end{array} } } \end{array}
$$

Thus,

$$
P ( \alpha ) = 1 1 1 . 9 7 5 - 2 1 8 . 8 7 8 \alpha + 4 0 0 . 9 3 7 \alpha ( \alpha - 0 . 5 ) .
$$

We have $P ^ { \prime } ( \pmb { \alpha } ) = \mathbf { 0 }$ when $\alpha = \alpha _ { 0 } = 0 . 5 2 2 9 5 9$ . Since $g _ { 0 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 0 } \mathbf { z } \right) = 2 . 3 2 7 6 2$ is smaller than ${ \pmb g } _ { 1 }$ and ${ \pmb g } _ { 3 }$ , we set

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - \alpha _ { 0 } \mathbf { z } = \mathbf { x } ^ { ( 0 ) } - 0 . 5 2 2 9 5 9 \mathbf { z } = ( 0 . 0 1 1 2 1 8 2 , 0 . 0 1 0 0 9 6 4 , - 0 . 5 2 2 7 4 1 ) ^ { t }
$$