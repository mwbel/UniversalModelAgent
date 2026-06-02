which implies that

The choice $x _ { 1 } = 1$ produces the eigenvector $( 1 , 1 , 0 ) ^ { t }$ corresponding to the eigenvalue $\lambda _ { 1 } = 1$ . For this choice, we have $\| ( 1 , 1 , 0 ) ^ { t } \| _ { \infty } = 1$

The choice $x _ { 1 } = \sqrt { 2 } / 2$ produces an eigenvector corresponding to $\lambda$ with

$$
\left\| \left( { \frac { \sqrt { 2 } } { 2 } } , { \frac { \sqrt { 2 } } { 2 } } , 0 \right) ^ { t } \right\| _ { 2 } = 1 .
$$

Since $\lambda _ { 2 }$ and $\lambda _ { 3 }$ are complex numbers, their corresponding eigenvectors are also complex. To find an eigenvector for $\lambda _ { 2 }$ , we solve the system

$$
\left[ \begin{array} { c c c } { 1 - ( 1 + \sqrt { 3 } i ) } & { 0 } & { 2 } \\ { 0 } & { 1 - ( 1 + \sqrt { 3 } i ) } & { - 1 } \\ { - 1 } & { 1 } & { 1 - ( 1 + \sqrt { 3 } i ) } \end{array} \right] \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] .
$$

One solution to this system is the vector

$$
\left( - \frac { 2 \sqrt { 3 } } { 3 } i , \frac { \sqrt { 3 } } { 3 } i , 1 \right) ^ { t } .
$$

Similarly, the vector

$$
\left( \frac { 2 \sqrt { 3 } } { 3 } i , - \frac { \sqrt { 3 } } { 3 } i , 1 \right) ^ { t }
$$

is an eigenvector corresponding to the eigenvalue λ3 = 1- √3i.

Maple provides the function Eigenvals to compute eigenvalues and, optionally, eigenvectors of a matrix. For the example we enter the following:

>with(linalg);   
>A: $=$ matrix(3,3,[1,0,2,0,1,-1,-1,1,1]);   
>evalf(Eigenvals(A));

[1.000000000+1.7320508071，1.000000000－1.732050807I，1.000000000]

This computes the eigenvalues

$$
\lambda _ { 2 } = 1 + \sqrt { 3 } i , \quad \lambda _ { 3 } = 1 - \sqrt { 3 } i , \quad \lambda _ { 1 } = 1 .
$$

To compute both the eigenvalues and eigenvectors, use

>evalf(Eigenvals(A,B)）;

The eigenvalues are computed and displayed as before,and the eigenvectors are indicated in the columns of $B$ . If the eigenvalues are all real, each column of $B$ gives an eigenvector. However,for our example we display $B$ using

>evalm(B);

$$
B = \left[ \begin{array} { c c c } { 1 . 1 5 4 7 0 0 5 3 8 } & { . 6 3 2 4 5 5 3 2 1 1 0 ^ { - 1 0 } } & { . 7 4 5 3 5 5 9 9 2 5 } \\ { - . 5 7 7 3 5 0 2 6 8 0 } & { . 1 2 6 4 9 1 1 0 6 4 1 0 ^ { - 9 } } & { . 7 4 5 3 5 5 9 9 2 6 } \\ { - . 2 5 8 1 9 8 8 8 9 6 1 0 ^ { - 1 9 } } & { 1 . 0 0 0 0 0 0 0 0 0 } & { - . 7 2 5 7 2 7 7 6 1 0 ^ { - 1 1 } } \end{array} \right]
$$

The first two columns correspond to the real and imaginary parts of the eigenvectors corresponding to eigenvalues $\lambda _ { 2 }$ and $\lambda _ { 3 }$ . Thus, an eigenvector for $\lambda _ { 2 }$ is

$$
\begin{array} { r } { 1 . 1 5 4 7 0 0 5 3 8 } \\ { - . 5 7 7 3 5 0 2 6 8 0 } \\ { . 2 5 8 1 9 8 8 8 9 6 1 0 ^ { - 1 9 } } \end{array} \left[ \begin{array} { c } { 1 . 6 3 2 4 5 5 5 3 2 1 1 0 ^ { - 1 0 } } \\ { 1 . 2 6 4 9 1 1 0 6 4 1 0 ^ { - 9 } } \\ { 1 . 0 0 0 0 0 0 0 0 } \end{array} \right] i \approx \left[ \begin{array} { c } { 1 . 1 5 4 7 0 0 5 3 8 } \\ { - . 5 7 7 3 5 0 2 6 8 0 } \\ { 0 } \end{array} \right] + \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 1 } \end{array} \right] i ;
$$

that is,

$$
( 1 . 1 5 4 7 0 0 5 3 8 , - 0 . 5 7 7 3 5 0 2 6 8 0 , i ) ^ { t } = \left( { \frac { 2 { \sqrt { 3 } } } { 3 } } , - { \frac { \sqrt { 3 } } { 3 } } , i \right) ^ { t } .
$$

Since any multiple of an eigenvector is also an eigenvector, we have

$$
( 1 , - 0 . 5 , 0 . 8 6 6 0 2 5 4 i )
$$

as aneigenvector. Multiplyingeachcoordinateby $- ( 2 \sqrt { 3 } / 3 ) i$ gives the eigenvector in Example 1:

$$
\left( - \frac { 2 \sqrt { 3 } } { 3 } i , \frac { \sqrt { 3 } } { 3 } i , 1 \right) ^ { t } .
$$

Since λ1 is real, the third column of B is an eigenvector corresponding to λ1.

The notions of eigenvalues and eigenvectors are introduced here for a specific computational convenience, but these concepts arise frequently in the study of physical systems. In fact, they are of sufcient interest that Chapter 9 is devoted to their numerical approximation.

Definition 7.14The spectral radius $\rho ( A )$ of a matrix A is defined by (Recall that for complex $\lambda = \alpha + \beta i$ , we have $| \lambda | = ( \alpha ^ { 2 } + \beta ^ { 2 } ) ^ { 1 / 2 } .$ ）

For the matrix considered in Example 1,

$$
\rho ( A ) = \operatorname* { m a x } \{ 1 , | 1 + { \sqrt { 3 } } i | , | 1 - { \sqrt { 3 } } i | \} = \operatorname* { m a x } \{ 1 , 2 , 2 \} = 2 .
$$

The spectral radius is closely related to the norm of a matrix,as shown in the following theorem.

Theorem 7.15 If $A$ is an $n \times n$ matrix, then

i $\| A \| _ { 2 } = [ \rho ( A ^ { t } A ) ] ^ { 1 / 2 } ,$ (ii) $\rho ( A ) \leq \| A \|$ , for any natural norm $\| \cdot \|$

ProofThe proof of part (i) requires more information concerning eigenvalues than we presently have available.For the details involved in the proof,see $[ 0 \mathbf { r } 2$ , p. 21].

To prove part (ii), suppose $\lambda$ is an eigenvalue of $A$ with eigenvector $\mathbf { x }$ and $\| \mathbf { x } \| = 1$ (Exercise 6 ensures that such an eigenvector exists.） Since $A \mathbf { x } = \lambda \mathbf { x }$ ，

$$
| \lambda | = | \lambda | \cdot \| \mathbf { x } \| = \| \lambda \mathbf { x } \| = \| A \mathbf { x } \| \leq \| A \| \| \mathbf { x } \| = \| A \| .
$$

Thus,

$$
\rho ( A ) = \operatorname* { m a x } | \lambda | \leq \| A \| .
$$

Part (i) of Theorem 7.15 implies that if $A$ is symmetric, then $\| A \| _ { 2 } ~ = ~ \rho ( A )$ (see Exercise 10).

An interesting and useful result, which is similar to part (ii) of Theorem 7.15, is that for any matrix $A$ and any $\varepsilon > 0$ , there exists a natural norm $\| \cdot \|$ with the property that $\rho ( A ) < \| A \| < \rho ( A ) + \varepsilon$ . Consequently, $\rho ( A )$ is the greatest lower bound for the natural norms on $A$ . The proof of this result can be found in $[ 0 \mathbf { r } 2$ p.23].

# EXAMPLE 2 If

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 1 } \\ { - 1 } & { 1 } & { 2 } \end{array} } \right] ,
$$

then

$$
A ^ { t } A = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 1 } \\ { 1 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 2 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 1 } \\ { - 1 } & { 1 } & { 2 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 3 } & { 2 } & { - 1 } \\ { 2 } & { 6 } & { 4 } \\ { - 1 } & { 4 } & { 5 } \end{array} \right] } .
$$

To calculate $\rho ( A ^ { t } A )$ we need the eigenvalues of $A ^ { t } A$ .If

$$
{ \begin{array} { r l } & { 0 = \operatorname* { d e t } ( A ^ { t } A - \lambda I ) } \\ & { \quad = \operatorname* { d e t } { \left[ \begin{array} { l l l } { 3 - \lambda } & { 2 } & { - 1 } \\ { 2 } & { 6 - \lambda } & { 4 } \\ { - 1 } & { 4 } & { 5 - \lambda } \end{array} \right] } } \\ & { \quad = - \lambda ^ { 3 } + 1 4 \lambda ^ { 2 } - 4 2 \lambda = - \lambda ( \lambda ^ { 2 } - 1 4 \lambda + 4 2 ) , } \end{array} }
$$

then

$$
\lambda = 0 \quad { \mathrm { ~ o r ~ } } \quad \lambda = 7 \pm { \sqrt { 7 } } ,
$$

So

$$
| | A | | _ { 2 } = { \sqrt { \rho ( A ^ { t } A ) } } = { \sqrt { \operatorname* { m a x } \{ 0 , 7 - { \sqrt { 7 } } , 7 + { \sqrt { 7 } } \} } } = { \sqrt { 7 + { \sqrt { 7 } } } } \approx 3 . 1 0 6 .
$$

The operations in Example 2 can also be performed using Maple with

>with(linalg);   
>A:=matrix(3,3,[1,1,0,1,2,1,-1,1,2]）;   
>B:=transpose(A);   
>C:=multiply(A,B);   
>evalf(Eigenvals(C));

$\{ 0 . 1 0 9 7 6 7 8 4 6 5 1 0 ^ { - 8 }$ ,4.354248690, 9.645751311]

Since |A|l2 = √p(AA)= p(C),we have

$$
| | A | | _ { 2 } = { \sqrt { 9 . 6 4 5 7 5 1 3 1 1 } } = 3 . 1 0 5 7 6 0 9 8 7 .
$$

Maple also computes |/All2 = √7+ √7 directly with the command >norm(A,2);

To determine the loo norm of A, replace the last command with

>norm(A,infinity);

In studying iterative matrix techniques, it is of particular importance to know when powers of a matrix become small(that is, when all the entries approach zero). Matrices of this type are called convergent.

Definition 7.16

We call an $n \times n$ matrix A convergent if

$$
\operatorname* { l i m } _ { k \to \infty } ( A ^ { k } ) _ { i j } = 0 , \quad { \mathrm { f o r e a c h } } i = 1 , 2 , \dots , n { \mathrm { ~ a n d ~ } } j = 1 , 2 , \dots .
$$

# EXAMPLE 3

Let

$$
A = \left[ \begin{array} { l l } { \frac { 1 } { 2 } } & { 0 } \\ { \frac { 1 } { 4 } } & { \frac { 1 } { 2 } } \end{array} \right] .
$$

Computing powers of $A$ , we obtain:

$$
A ^ { 2 } = { \left[ \begin{array} { l l } { { \frac { 1 } { 4 } } } & { 0 } \\ { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \end{array} \right] } , \quad A ^ { 3 } = { \left[ \begin{array} { l l } { { \frac { 1 } { 8 } } } & { 0 } \\ { { \frac { 3 } { 1 6 } } } & { { \frac { 1 } { 8 } } } \end{array} \right] } , \quad A ^ { 4 } = { \left[ \begin{array} { l l } { { \frac { 1 } { 1 6 } } } & { 0 } \\ { { \frac { 1 } { 8 } } } & { { \frac { 1 } { 1 6 } } } \end{array} \right] } ,
$$

and,in general,

$$
A ^ { k } = \left[ { \begin{array} { c c } { ( { \frac { 1 } { 2 } } ) ^ { k } } & { 0 } \\ { { \frac { k } { 2 ^ { k + 1 } } } } & { ( { \frac { 1 } { 2 } } ) ^ { k } } \end{array} } \right] .
$$

Since

$$
\operatorname * { l i m } _ { k \to \infty } \left( { \frac { 1 } { 2 } } \right) ^ { k } = 0 \quad { \mathrm { a n d } } \quad \operatorname* { l i m } _ { k \to \infty } { \frac { k } { 2 ^ { k + 1 } } } = 0 ,
$$

A is a convergent matrix.

Notice that the convergent matrix A in Example 3 has p(A)= ,since  is the only eigenvalue of A. This ilustrates the important connection that exists between the spectral radius of a matrix and the convergence of the matrix, as detailed in the following result.

# Theorem 7.17

The following statements are equivalent.

i $A$ is a convergent matrix. () $\textstyle \operatorname* { l i m } _ { n \to \infty } \| A ^ { n } \| = 0$ ,for some natural norm. (ii)） $\operatorname* { l i m } _ { n \to \infty } \| A ^ { n } \| = 0$ ,for all natural norms. (iv） $\rho ( A ) < 1 .$ （v） $\operatorname* { l i m } _ { n \to \infty } A ^ { n } \mathbf { x } = \mathbf { 0 }$ , for every $\mathbf { x }$

The proof of this theorem can be found in [IK, p. 14].

# ExERcisE SEt 7.2

1.Compute the eigenvalues and associated eigenvectors of the following matrices.

$\begin{array} { r l } { \mathbf { a } \cdot { \mathbf { \xi } } } & { \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] } \\ { \mathbf { c } . } & { \left[ \begin{array} { l l } { 0 } & { \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } & { 0 } \end{array} \right] } \\ { \mathbf { e } . } & { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} \right] } \\ { \mathbf { g } . } & { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 2 } & { 3 } & { 2 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] } \end{array}$ $\begin{array} { r l } { \mathbf { b } . } & { { } \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } \\ { \mathbf { d } . } & { { } \left[ \begin{array} { l l } { 1 } & { 1 } \\ { - 2 } & { - 2 } \end{array} \right] } \\ { \mathbf { f } . } & { { } \left[ \begin{array} { l l l } { - 1 } & { 2 } & { 0 } \\ { 0 } & { 3 } & { 4 } \\ { 0 } & { 0 } & { 7 } \end{array} \right] } \\ { \mathbf { h } . } & { { } \left[ \begin{array} { l l l l } { 3 } & { 2 } & { - 1 } \\ { 1 } & { - 2 } & { 3 } \\ { 2 } & { 0 } & { 4 } \end{array} \right] } \end{array}$

2.Find the spectral radius for each matrix in Exercise 1.

3.Which of the matrices in Exercise 1 are convergent?

4.Let $A _ { 1 } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 2 } } } \end{array} \right] }$ and $A _ { 2 } = { \left[ \begin{array} { l l } { { \frac { 1 } { 2 } } } & { 0 } \\ { 1 6 } & { { \frac { 1 } { 2 } } } \end{array} \right] }$ .Show that $\pmb { A } _ { 1 }$ is not convergent, but $A _ { 2 }$ is convergent.

5.Find the $| | \cdot | | _ { 2 }$ norm for the matrices in Exercise 1.

6. Show that if $\lambda$ is a eigenvalue of a matrix $A$ and $\| \cdot \|$ is a vector norm, then an eigenvector x associated with $\lambda$ exists with $| | \mathbf { x } | | = 1$

7.Show that the characteristic polynomial $p ( \lambda ) = \operatorname* { d e t } ( A - \lambda I )$ for the $n \times n$ matrix $A$ is an nth-degree polynomial. [Hint: Expand de $\operatorname { \pmb { t } } ( \pmb { A } - \lambda \pmb { I } )$ along the first row,and use mathematical induction on $\pmb { n }$ .]

8.a.Show that if $\pmb { A }$ is an $n \times n$ matrix, then

$$
\operatorname* { d e t } A = \prod _ { i = 1 } ^ { n } \lambda _ { 1 } ,
$$

where $\lambda _ { i } , \ldots , \lambda _ { n }$ are the eigenvalues of A. [Hint: Consider $p ( 0 )$ ] b.Show that $\pmb { A }$ is singular if and only if $\lambda = 0$ is an eigenvalue of $\pmb { A }$

9.Let $\lambda$ be an eigenvalue of the $n \times n$ matrix $A$ and $\mathbf { x } \neq \mathbf { 0 }$ be an associated eigenvector.

a. Show that $\lambda$ is also an eigenvalue of $A ^ { t }$   
$\mathbf { b } .$ Show that for any integer $k \geq 1 , \lambda ^ { k }$ is an eigenvalue of $A ^ { k }$ with eigenvector $\mathbf { X }$   
c. Show that if $A ^ { - 1 }$ exists, then $1 / \lambda$ is an eigenvector of $A ^ { - 1 }$ with eigenvector $\mathbf { X }$   
d. Generalize parts (b) and (c) to $( A ^ { \lnot \to 1 } ) ^ { k }$ for integers $k \geq 2$   
e. Given the polynomial $q ( x ) = q _ { 0 } + q _ { 1 } x + \cdot \cdot \cdot + q _ { k } x ^ { k }$ ，define $q ( A )$ to be the matrix $q ( A ) = q _ { 0 } I + q _ { 1 } A + \cdot \cdot \cdot + q _ { k } A ^ { k }$ . Show that $q ( \lambda )$ is an eigenvalue of $q ( A )$ with eigenvector $\mathbf { x }$   
f. Let $\alpha \neq \lambda$ be given. Show that if $A - \alpha I$ is a nonsingular, then $1 / ( \lambda - \alpha )$ is an eigenvalue of $( A - \alpha I ) ^ { - 1 }$ with eigenvector $\mathbf { x }$

10.Show that if $A$ is symmetric, then $| | A | | _ { 2 } = \rho ( A )$

11.In Exercise 11 of Section 6.3,we assumed that the contribution a female beetle of a certain type made to the future years’ beetle population could be expressed in terms of the matrix

$$
A = \left[ { \begin{array} { l l l } { 0 } & { 0 } & { 6 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 3 } } } & { 0 } \end{array} } \right] ,
$$

where the entry in the ith row and $j$ th column represents the probabilistic contribution of a beetle of age $j$ onto the next year's female population of age i.

a. Does the matrix $A$ have any real eigenvalues? If so,determine them and any associated eigenvectors.   
b. If a sample of this species was needed for laboratory test purposes that would have a constant proportion in each age group from year to year, what criteria could be imposed on the initial population to ensure that this requirement would be satisfied?

12. Find matrices $A$ and $B$ for which $\rho ( A + B ) > \rho ( A ) + \rho ( B )$ . (This shows that $\rho ( A )$ cannot be a matrix norm.)

13. Show that if $| | \cdot | |$ is any natural norm, then $( 1 / | | A ^ { - 1 } | | ) \leq | \lambda | \leq | | A | |$ for any eigenvalue $\lambda$ 01 the nonsingular matrix $A$

# 7.3 Iterative Techniques for Solving Linear Systems

In this section we describe the Jacobi and the Gauss-Seidel iterative methods, classic methods that date to the late eighteenth century. Iterative techniques are seldom used for solving linear systems of small dimension since the time required for sufficient accuracy exceeds that required for direct techniques such as Gaussian elimination.For large systems with a high percentage of O entries,however, these techniques are efficient in terms of both com-puter storage and computation. Systems of this type arise frequently in circuit analysis and in the numerical solution of boundary-value problems and partial-differential equations.

An iterative technique to solve the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ starts with an initial approximation $\mathbf { x } ^ { ( 0 ) }$ to the soution $\mathbf { x }$ andgeneraessequeceofeco $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ that converges to $\mathbf { x }$ . Iterative techniques involve a process that converts the system $\pmb { A } \mathbf { x } = \mathbf { b }$ into an equivalent system of the form ${ \bf x } = T { \bf x } + { \bf c }$ for some fixed matrix $T$ and vector c.

After the initial vector $\mathbf { x } ^ { ( 0 ) }$ is selected, the sequence of approximate solution vectors is generated by computing

$$
\begin{array} { r } { \mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } , } \end{array}
$$

for each $k = 1 , 2 , 3 , \dots$ . This result should be reminiscent of the fixed-point iteration studied in Chapter 2.

# EXAMPLE 1

The linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ given by

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } 1 0 x _ { 1 } - \mathrm {  ~ \sigma ~ } x _ { 2 } + \mathrm {  ~ 2 } x _ { 3 } \mathrm {  ~ \sigma ~ } } & { = 6 , } \\ { E _ { 2 } : } & { { } - x _ { 1 } + 1 1 x _ { 2 } - \mathrm {  ~ \sigma ~ } x _ { 3 } + 3 x _ { 4 } = 2 5 , } \\ { E _ { 3 } : } & { { } 2 x _ { 1 } - \mathrm {  ~ \sigma ~ } x _ { 2 } + 1 0 x _ { 3 } - \mathrm {  ~ \sigma ~ } x _ { 4 } = - 1 1 , } \\ { E _ { 4 } : } & { { } 3 x _ { 2 } - \mathrm {  ~ \sigma ~ } x _ { 3 } + 8 x _ { 4 } = 1 5 } \end{array}
$$

las the unique solution $\mathbf { x } = ( 1 , 2 , - 1 , 1 ) ^ { t }$ . To convert $\pmb { A } \mathbf { x } = \mathbf { b }$ to the form ${ \bf x } = T { \bf x } + { \bf c }$ solve equation $E _ { i }$ for $x _ { i }$ ,for each $i = 1 , 2 , 3 , 4$ , to obtain

$$
\begin{array} { l } { x _ { 1 } = { } } \\ { x _ { 2 } = { } } \\ { x _ { 2 } = { } } \\ { x _ { 3 } = - { \displaystyle \frac { 1 } { 5 } } x _ { 1 } + { \displaystyle \frac { 1 } { 1 0 } } x _ { 2 } { } } \\ { x _ { 4 } = { } } \end{array} \begin{array} { r } { \displaystyle \frac { 1 } { 1 0 } x _ { 2 } - { \displaystyle \frac { 1 } { 5 } } x _ { 3 } { } } \\ { { } } \\ { { } + { \displaystyle \frac { 1 } { 1 1 } } x _ { 3 } - { \displaystyle \frac { 3 } { 1 1 } } x _ { 4 } + { \displaystyle \frac { 2 5 } { 1 1 } } , } \\ { { } } \\ { { } + { \displaystyle \frac { 1 } { 1 0 } } x _ { 4 } - { \displaystyle \frac { 1 1 } { 1 0 } } , } \\ { { } } \\ { { } + { \displaystyle \frac { 3 } { 8 } } x _ { 2 } + { \displaystyle \frac { 1 } { 8 } } x _ { 3 } { } } \end{array}
$$

Then $\pmb { A } \mathbf { x } = \mathbf { b }$ can be rewritten in the form ${ \mathbf x } = T { \mathbf x } + { \mathbf c }$ ,with

$$
T = \left[ \begin{array} { c c c c } { 0 } & { \frac 1 { 1 0 } } & { - \frac 1 5 } & { 0 } \\ { \frac 1 { 1 1 } } & { 0 } & { \frac 1 { 1 1 } } & { - \frac 3 { 1 1 } } \\ { - \frac 1 5 } & { \frac 1 { 1 0 } } & { 0 } & { \frac 1 { 1 0 } } \\ { 0 } & { - \frac 3 8 } & { \frac 1 8 } & { 0 } \end{array} \right] \quad \mathrm { a n d } \quad \mathbf { c } = \left[ \begin{array} { c } { \frac 3 5 } \\ { \frac { 2 5 } { 1 1 } } \\ { - \frac { 1 1 } { 1 0 } } \\ { \frac { 1 5 } { 8 } } \end{array} \right] .
$$

For an initial aproximation, we let $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 , 0 ) ^ { t }$ . Then $\mathbf { x } ^ { ( 1 ) }$ is given by

$$
\begin{array} { l l l } { { x _ { 1 } ^ { ( 1 ) } = } } & { { { \displaystyle { \frac { 1 } { 1 0 } } x _ { 2 } ^ { ( 0 ) } - { \frac { 1 } { 5 } } x _ { 3 } ^ { ( 0 ) } } } } & { { + { \ \displaystyle { \frac { 3 } { 5 } } = } } } & { { { 0 . 6 0 0 0 , } } } \\ { { x _ { 2 } ^ { ( 1 ) } = { \ \displaystyle { \frac { 1 } { 1 1 } } x _ { 1 } ^ { ( 0 ) } } } } & { { + { \displaystyle { \frac { 1 } { 1 1 } } x _ { 3 } ^ { ( 0 ) } - { \frac { 3 } { 1 1 } } x _ { 4 } ^ { ( 0 ) } + { \frac { 2 5 } { 1 1 } } = } } } & { { 2 . 2 7 2 7 , } } \\ { { x _ { 3 } ^ { ( 1 ) } = - { \displaystyle { \frac { 1 } { 5 } } x _ { 1 } ^ { ( 0 ) } + { \frac { 1 } { 1 0 } } x _ { 2 } ^ { ( 0 ) } } } } & { { + { \ \displaystyle { \frac { 1 } { 1 0 } } x _ { 4 } ^ { ( 0 ) } - { \frac { 1 1 } { 1 0 } } = - 1 . 1 0 0 0 , } } } \\ { { x _ { 4 } ^ { ( 1 ) } = } } & { { - { \ \displaystyle { \frac { 3 } { 8 } } x _ { 2 } ^ { ( 0 ) } + { \ \frac { 1 } { 8 } } x _ { 3 } ^ { ( 0 ) } } } } & { { + { \ \displaystyle { \frac { 1 5 } { 8 } } = } } } & { { 1 . 8 7 5 0 . } } \end{array}
$$

Additional iterates, $\mathbf { x } ^ { ( k ) } = ( x _ { 1 } ^ { ( k ) } , x _ { 2 } ^ { ( k ) } , x _ { 3 } ^ { ( k ) } , x _ { 4 } ^ { ( k ) } ) ^ { t }$ , are generatedinasimilarmanerand are presented in Table 7.1.

Table 7.1   

<table><tr><td>k</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>司</td><td>0.000</td><td>0.6000</td><td>1.0473</td><td>0.9326</td><td>1.0152</td><td>0.9890</td><td>1.0032</td><td>0.9981</td><td>1.0006</td><td>0.9997</td><td>1.0001</td></tr><tr><td></td><td>0.0000</td><td>2.2727</td><td>1.7159</td><td>2.053</td><td>1.9537</td><td>2.0114</td><td>1.9922</td><td>2.0023</td><td>1.9987</td><td>2.0004</td><td>1.9998</td></tr><tr><td></td><td>0.0000</td><td>-1.1000</td><td>-0.8052</td><td>-1.0493</td><td>-0.9681</td><td>-1.0103</td><td>-0.9945</td><td>-1.0020</td><td>-0.9990</td><td>-1.0004</td><td>-- 0.9998</td></tr><tr><td></td><td>0.0000</td><td>1.8750</td><td>0.8852</td><td>1.1309</td><td>0.9739</td><td>1.0214</td><td>0.9944</td><td>1.0036</td><td>0.9989</td><td>1.0006</td><td>0.9998</td></tr></table>

The decision to stop after ten iterations was based on the criterion

$$
\frac { \| \mathbf { x } ^ { ( 1 0 ) } - \mathbf { x } ^ { ( 9 ) } \| _ { \infty } } { \| \mathbf { x } ^ { ( 1 0 ) } \| _ { \infty } } = \frac { 8 . 0 \times 1 0 ^ { - 4 } } { 1 . 9 9 9 8 } < 1 0 ^ { - 3 } .
$$

In fact, $\lVert \mathbf { x } ^ { ( 1 0 ) } - \mathbf { x } \rVert _ { \infty } = 0 . 0 0 0 2$

The method of Example 1 is called the Jacobi iterative method. It consists of solving the ith equation in $\pmb { A } \pmb { X } = \pmb { \mathrm { b } }$ for $x _ { i }$ to obtain (provided $a _ { i i } \neq 0$ ）

$$
x _ { i } = \sum _ { \stackrel { j = 1 } { j \neq i } } ^ { n } \left( - { \frac { a _ { i j } x _ { j } } { a _ { i i } } } \right) + { \frac { b _ { i } } { a _ { i i } } } , \qquad { \mathrm { f o r ~ } } i = 1 , 2 , \ldots , n
$$

and generating each $x _ { i } ^ { ( k ) }$ from components of $\mathbf { x } ^ { ( k - 1 ) }$ for $k \geq 1$ by

$$
x _ { i } ^ { ( k ) } = \frac { \sum _ { j = 1 } ^ { n } \left( - a _ { i j } x _ { j } ^ { ( k - 1 ) } \right) + b _ { i } } { a _ { i i } } , \qquad \mathrm { f o r } i = 1 , 2 , \dots , n .
$$

The method is written in the form $\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c }$ by splitting $\pmb { A }$ into its diagonal and off-diagonal parts. To see this,let $D$ be the diagonal matrix whose diagonal entries are those of $A$ ， $- L$ be the strictly lower-triangular part of $A$ ,and $- U$ be the strictly uppertriangular part of $\pmb { A }$ . With this notation,

$$
A = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 n } } \\ { \quad } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n n } } \end{array} \right] }
$$

is split into

$$
= \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { 0 ; \cdots } & { \cdots } & { 0 } \\ { 0 } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \partial } & { \cdots } & { \cdots } & { \cdots } & { 0 } \end{array} \right] - \left[ \begin{array} { l } { 0 ; \cdots } & { \cdots } \\ { \cdots } \\ { - a _ { 2 1 } } & { \ddots } \\ { \vdots } & { \ddots } \\ { \vdots } & { \ddots } \\ { - \dot { a } _ { n 1 } \cdots - \dot { a } _ { n , n - 1 } } & { \vdots } \end{array} \right] - \left[ \begin{array} { l } { 0 ; \cdots - \cdots } \\ { \vdots } \\ { \vdots } \\ { \ddots } \\ { \ddots } \\ { \vdots } \\ { \partial } & { \cdots } \end{array} \right] .
$$

$$
= D - L - U .
$$

The equation $\pmb { A } \mathbf { x } = \mathbf { b }$ ,or $( D - L - U ) \mathbf { x } = \mathbf { b }$ , is then transformed into

$$
D \mathbf { x } = ( L + U ) \mathbf { x } + \mathbf { b } ,
$$

and,if $D ^ { - 1 }$ exists,that is, if $a _ { i i } \neq 0$ for each $i$ ,then

$$
{ \bf x } = D ^ { - 1 } ( L + U ) { \bf x } + D ^ { - 1 } { \bf b } .
$$

This results in the matrix form of the Jacobi iterative technique:

$$
\mathbf { x } ^ { ( k ) } = { D } ^ { - 1 } ( L + U ) \mathbf { x } ^ { ( k - 1 ) } + { D } ^ { - 1 } \mathbf { b } , \quad k = 1 , 2 , \ldots .
$$

Introducing the notation $T _ { j } = D ^ { - 1 } ( L + U )$ and $\mathbf { c } _ { j } = D ^ { - 1 } \mathbf { b }$ , the Jacobi technique has the form

$$
\mathbf { x } ^ { ( k ) } = T _ { j } \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } _ { j } .
$$

n practice, Eq. (7.4) is used in computation and Eq. (7.6) for theoretical purposes.

Algorithm 7.1 implements the Jacobi iterative technique.

# Jacobi Iterative

To solve $\pmb { A } \pmb { \mathrm { x } } = \pmb { \mathrm { b } }$ given an initial approximation $\mathbf { x } ^ { ( 0 ) }$ ：

INPUT the number of equations and unknowns $\pmb { n }$ ; the entries $a _ { i j } , 1 \leq i , j \leq n$ of the matrix $A$ ; the entries $b _ { i }$ ， $1 \leq i \leq n$ of $\mathbf { b }$ ; the entries $X O _ { i }$ ， $1 \leq i \leq n$ of $\mathbf { X 0 } = \mathbf { x } ^ { ( 0 ) }$ ； tolerance TOL; maximum number of iterations $N$

OUTPUTthe approximate solution $x _ { 1 } , \ldots , x _ { n }$ or a message that the number of iterations was exceeded.

Step 1 Set $k = 1$

.Step 2 While $( k \leq N )$ do Steps 3-6.

Step 3 $\operatorname { F o r } i = 1 , \dots , n$

$$
\sec x _ { i } = { \frac { - \sum _ { j = 1 } ^ { n } ( a _ { i j } X O _ { j } ) + b _ { i } } { a _ { i i } } } .
$$

Step 4 If $| | \mathbf { x } - \mathbf { X O } | | < T O L$ then OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ； (The procedure was successful.) STOP.

Step 5 Set $k = k + 1$

Step 6 For $i = 1 , \ldots , n$ set $X O _ { i } = x _ { i }$ Step 7OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was successful.) STOP.

Step 3 of the algorithm requires that $a _ { i i } \neq 0$ , for each $i = 1 , 2 , \dots , n$ . If one of the $a _ { i i }$ entries is O and the system is nonsingular, a reordering of the equations can be performed so that no $a _ { i i } = 0$ .To speed convergence, the equations should be arranged so that $a _ { i i }$ is as large as possible. This subject is discussed in more detail later in this chapter.

Another possible stopping criterion in Step 4 is to iterate until

$$
\frac { \| \mathbf { x } ^ { ( k ) } - \mathbf { x } ^ { ( k - 1 ) } \| } { \| \mathbf { x } ^ { ( k ) } \| }
$$

is smaller than some prescribed tolerance. For this purpose, any convenient norm can be used, the usual being the $l _ { \infty }$ norm.

A possible improvement in Algorithm 7.1 can be seen by reconsidering Eq. (7.4). The components of $\mathbf { x } ^ { ( k - 1 ) }$ are used to compute $x _ { i } ^ { ( k ) }$ . Since, for $i > 1$ ， $x _ { 1 } ^ { ( k ) } , \ldots , x _ { i - 1 } ^ { ( k ) }$ have already been computed and are_probably better approximations to the actual solutions $x _ { 1 } , \ldots , x _ { i - 1 }$ than $\mathbf { \widehat { x } } _ { 1 } ^ { ( k - 1 ) } , \dots , \mathbf { x } _ { i - 1 } ^ { ( k - 1 ) }$ , it seems more reasonable to compute $x _ { i } ^ { ( k ) }$ using these most recently calculated values. That is, we can use

$$
x _ { i } ^ { ( k ) } = \frac { - \displaystyle \sum _ { j = 1 } ^ { i - 1 } ( a _ { i j } x _ { j } ^ { ( k ) } ) - \displaystyle \sum _ { j = i + 1 } ^ { n } ( a _ { i j } x _ { j } ^ { ( k - 1 ) } ) + b _ { i } } { a _ { i i } } ,
$$

for each $i = 1 , 2 , \ldots , n$ ,instead of Eq. (7.4). This modification is called the Gauss-Seidel iterative technique and is illustrated in the following example.

# EXAMPLE 2

The linear system given by

$$
\begin{array} { r l } & { 1 0 x _ { 1 } - x _ { 2 } + 2 x _ { 3 } = 6 , } \\ & { - x _ { 1 } + 1 1 x _ { 2 } - x _ { 3 } + 3 x _ { 4 } = 2 5 , } \\ & { 2 x _ { 1 } - x _ { 2 } + 1 0 x _ { 3 } - x _ { 4 } = - 1 1 , } \\ & { 3 x _ { 2 } - x _ { 3 } + 8 x _ { 4 } = 1 5 } \end{array}
$$

was solved in Example 1 by the Jacobi iterative method. Incorporating Eq. (7.7) into Algorithm 7.1 gives the equations to be used for each $k = 1 , 2 , \ldots$

$$
\begin{array} { l c c } { { x _ { 1 } ^ { ( k ) } = } } & { { \displaystyle \frac { 1 } { 1 0 } x _ { 2 } ^ { ( k - 1 ) } - } } & { { \displaystyle \frac { 1 } { 5 } x _ { 3 } ^ { ( k - 1 ) } } } & { { + \displaystyle \frac { 3 } { 5 } , } } \\ { { x _ { 2 } ^ { ( k ) } = \displaystyle \frac { 1 } { 1 1 } x _ { 1 } ^ { ( k ) } } } & { { + \displaystyle \frac { 1 } { 1 1 } x _ { 3 } ^ { ( k - 1 ) } - \displaystyle \frac { 3 } { 1 1 } x _ { 4 } ^ { ( k - 1 ) } + \displaystyle \frac { 2 5 } { 1 1 } , } } \\ { { x _ { 3 } ^ { ( k ) } = - \displaystyle \frac { 1 } { 5 } x _ { 1 } ^ { ( k ) } + \displaystyle \frac { 1 } { 1 0 } x _ { 2 } ^ { ( k ) } } } & { { + \displaystyle \frac { 1 } { 1 0 } x _ { 4 } ^ { ( k - 1 ) } - \displaystyle \frac { 1 1 } { 1 0 } , } } \\ { { x _ { 4 } ^ { ( k ) } = } } & { { - \displaystyle \frac { 3 } { 8 } x _ { 2 } ^ { ( k ) } + \displaystyle \frac { 1 } { 8 } x _ { 3 } ^ { ( k ) } } } & { { + \displaystyle \frac { 1 5 } { 8 } . } } \end{array}
$$

Letting $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 , 0 ) ^ { t }$ , we generate the iterates in Table 7.2.

Table 7.2

<table><tr><td>k</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td></td><td>0.0000</td><td>0.6000</td><td>1.030</td><td>1.0065</td><td>1.0009</td><td>1.0001</td></tr><tr><td>（k） x2</td><td>0.0000</td><td>2.3272</td><td>2.037</td><td>2.0036</td><td>2.0003</td><td>2.0000</td></tr><tr><td>(k） x3</td><td>0.0000</td><td>-0.9873</td><td>-1.014</td><td>-1.0025</td><td>-1.0003</td><td>-1.0000</td></tr><tr><td>（k） x4</td><td>0.0000</td><td>0.8789</td><td>0.9844</td><td>0.9983</td><td>0.9999</td><td>1.0000</td></tr></table>

Since

$$
\frac { | | { \bf x } ^ { ( 5 ) } - { \bf x } ^ { ( 4 ) } | | _ { \infty } } { | | { \bf x } ^ { ( 5 ) } | | _ { \infty } } = \frac { 0 . 0 0 0 8 } { 2 . 0 0 0 } = 4 \times 1 0 ^ { - 4 } ,
$$

$\mathbf { x } ^ { ( 5 ) }$ is accepted as a reasonable approximation to the solution. Note that Jacobi's method in Example 1 required twice as many iterations for the same acuracy.

To write the Gauss-Seidel method in matrix form, multiply both sides of Eq. (7.7)by $a _ { i i }$ and collect all $k$ th iterate terms, to give

$$
a _ { i 1 } x _ { 1 } ^ { ( k ) } + a _ { i 2 } x _ { 2 } ^ { ( k ) } + \cdot \cdot \cdot + a _ { i i } x _ { i } ^ { ( k ) } = - a _ { i , i + 1 } x _ { i + 1 } ^ { ( k - 1 ) } - \cdot \cdot \cdot - a _ { i n } x _ { n } ^ { ( k - 1 ) } + b _ { i } ,
$$

for each $i = 1 , 2 , \ldots , n$ . Writing all $\pmb { n }$ equations gives

$$
\begin{array} { r l r } { a _ { 1 1 } x _ { 1 } ^ { ( k ) } } & { = - a _ { 1 2 } x _ { 2 } ^ { ( k - 1 ) } - a _ { 1 3 } x _ { 3 } ^ { ( k - 1 ) } - \cdot \cdot \cdot - a _ { 1 n } x _ { n } ^ { ( k - 1 ) } + b _ { 1 } , } \\ { a _ { 2 1 } x _ { 1 } ^ { ( k ) } + a _ { 2 2 } x _ { 2 } ^ { ( k ) } } & { = } & { - a _ { 2 3 } x _ { 3 } ^ { ( k - 1 ) } - \cdot \cdot \cdot - a _ { 2 n } x _ { n } ^ { ( k - 1 ) } + b _ { 2 } , } \\ { \vdots } & { } & \\ { a _ { n 1 } x _ { 1 } ^ { ( k ) } + a _ { n 2 } x _ { 2 } ^ { ( k ) } + \cdot \cdot \cdot + a _ { n n } x _ { n } ^ { ( k ) } = } & { b _ { n } ; } \end{array}
$$

with the definitions of $D , L$ ,and $U$ given previously, we have the Gauss-Seidel method represented by

$$
( D - L ) \mathbf { x } ^ { ( k ) } = U \mathbf { x } ^ { ( k - 1 ) } + \mathbf { b }
$$

or

$$
\mathbf { x } ^ { ( k ) } = ( D - L ) ^ { - 1 } U \mathbf { x } ^ { ( k - 1 ) } + ( D - L ) ^ { - 1 } \mathbf { b } , \quad \mathrm { f o r e a c h } k = 1 , 2 , \dots .
$$

Letting $T _ { g } = ( D - L ) ^ { - 1 } U$ and $\mathbf { c } _ { g } = ( D - L ) ^ { - 1 } \mathbf { b }$ ,the Gauss-Seidel technique has the form

$$
\mathbf { x } ^ { ( k ) } = T _ { g } \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } _ { g } .
$$

For the lower-triangular matrix $D - L$ to be nonsingular,it is necessary and sufficient that $a _ { i i } \neq 0$ ,for each $i = 1 , 2 , \dots , n$

Algorithm 7.2 implements the Gauss-Seidel method.

# Gauss-Seidel Iterative

To solve $\pmb { A } \mathbf { x } = \mathbf { b }$ given an initial approximation $\mathbf { x } ^ { ( 0 ) }$ ：

INPUT the number of equations and unknowns $\pmb { n }$ ; the entries $a _ { i j }$ ， $1 \leq i , j \leq n$ of the matrix $A$ ; the entries $b _ { i }$ ， $1 \leq i \leq n$ of $\mathbf { b }$ ; the entries $X O _ { i }$ ， $1 \leq i \leq n$ of $\mathbf { X 0 } = \mathbf { x } ^ { ( 0 ) }$ ； tolerance $T O L$ ; maximum number of iterations $N$

OUTPUTthe approximate solution $x _ { 1 } , \ldots , x _ { n }$ or a message that the number of iterations was exceeded.

Step 1 Set $k = 1$

Step 2 While $( k \le N )$ do Steps 3-6.

Step3F $\operatorname { i o r } i = 1 , \dots , n$

$$
\cot x _ { i } = { \frac { - \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } - \displaystyle \sum _ { j = i + 1 } ^ { n } a _ { i j } X O _ { j } + b _ { i } } { a _ { i i } } } .
$$

Step 4 If $| | \mathbf { x } - \mathbf { X O } | | < T O L$ then OUTPUT $\left( x _ { 1 } , \ldots , x _ { n } \right)$ ：

Step 5Set $k = k + 1$

Step 6For $i = 1 , \ldots , n$ set $X O _ { i } = x _ { i }$

Step 7OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was successful.) STOP.

The comments following Algorithm 7.1 regarding reordering and stopping criteria also apply to the Gauss-Seidel Algorithm 7.2.

The results of Examples 1 and 2 appear to imply that the Gauss-Seidel method is superior to the Jacobi method. This is almost always true, but there are linear systems for which the Jacobi method converges and the Gauss-Seidel method does not (see Exercises 9 and 10).

To study the convergence of general iteration techniques,we consider the formula

$$
\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } , \quad \mathrm { f o r } \operatorname { e a c h } k = 1 , 2 , \ldots { } .
$$

where $\mathbf { x } ^ { ( 0 ) }$ is arbitrary.

If the spectral radius $\rho ( T )$ satisfies $\rho ( T ) < 1$ ,then $( I - T ) ^ { - 1 }$ exists,and

$$
( I - T ) ^ { - 1 } = I + T + T ^ { 2 } + \cdot \cdot \cdot = \sum _ { j = 0 } ^ { \infty } T ^ { j } .
$$

Proof Since $T \mathbf { x } = \lambda \mathbf { x }$ is true precisely when $( I - T ) \mathbf { x } = ( 1 - \lambda ) \mathbf { x }$ ,we have $\lambda$ as an eigenvalue of $T$ precisely when $1 - \lambda$ is an eigenvalue of $I - T$ .But $| \lambda | \le \rho ( T ) < 1$ ，s0 $\lambda = 1$ is not an eigenvalue of $T$ , and O cannot be an eigenvalue of $I - T$ . Hence, $( I - T ) ^ { - 1 }$ exists.

Let $S _ { m } = I + T + T ^ { 2 } + \cdot \cdot \cdot + T ^ { m }$ . Then

$$
( I - T ) S _ { m } = ( 1 + T + T ^ { 2 } + \cdot \cdot \cdot + T ^ { m } ) - ( T + T ^ { 2 } + \cdot \cdot \cdot + T ^ { m + 1 } ) = I - T ^ { m + 1 } .
$$

and, since $T$ is convergent, the result at the end of Section 7.2 implies that

$$
\operatorname* { l i m } _ { m \to \infty } ( I - T ) S _ { m } = \operatorname* { l i m } _ { m \to \infty } ( I - T ^ { m + 1 } ) = I .
$$

$$
\begin{array} { r } { ( I - T ) ^ { - 1 } = \operatorname* { l i m } _ { m  \infty } S _ { m } = I + T + T ^ { 2 } + \cdot \cdot \cdot = \sum _ { j = 0 } ^ { \infty } T ^ { j } . } \end{array}
$$

For any $\mathbf { x } ^ { ( 0 ) } \in \mathbb { R } ^ { n }$ , the sequence $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ defined by

$$
\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } , \quad \operatorname { f o r } \operatorname { e a c h } k \geq 1 ,
$$

converges to the unique solution of ${ \bf x } = T { \bf x } + { \bf c }$ if and only if $\rho ( T ) < 1$

Proof First assume that $\rho ( T ) < 1$ . Then,

$$
{ \begin{array} { r l } & { \mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } } \\ & { \qquad = T ( T \mathbf { x } ^ { ( k - 2 ) } + \mathbf { c } ) + \mathbf { c } } \\ & { \qquad = T ^ { 2 } \mathbf { x } ^ { ( k - 2 ) } + ( T + I ) \mathbf { c } } \\ & { \qquad \vdots } \\ & { \qquad = T ^ { k } \mathbf { x } ^ { ( 0 ) } + ( T ^ { k - 1 } + \cdots + T + I ) \mathbf { c } . } \end{array} }
$$

Since $\rho ( T ) < 1$ , the matrix $T$ is convergent and

$$
\operatorname * { l i m } _ { k  \infty } T ^ { k } { \bf x } ^ { ( 0 ) } = { \bf 0 } . \qquad .
$$

Lemma 7.18 implies that

$$
\operatorname* { l i m } _ { k \to \infty } \mathbf { x } ^ { ( k ) } = \operatorname* { l i m } _ { k \to \infty } T ^ { k } \mathbf { x } ^ { ( 0 ) } + \left( \sum _ { j = 0 } ^ { \infty } T ^ { j } \right) \mathbf { c } = \mathbf { 0 } + ( I - T ) ^ { - 1 } \mathbf { c } = ( I - T ) ^ { - 1 } \mathbf { c } .
$$

Hence, the sequence $\{ \mathbf { x } ^ { ( k ) } \}$ converges to the vector ${ \bf x } \equiv ( I - T ) ^ { - 1 } { \bf c }$ and ${ \mathbf x } = T { \mathbf x } + { \mathbf c }$

To prove the converse, we show that for any $\mathbf { z } \in \mathbb { R } ^ { n }$ ， we have $\scriptstyle \operatorname* { l i m } _ { k \to \infty } T ^ { k } \mathbf { z } = \mathbf { 0 }$ .By Theorem 7.17, this is equivalent to $\rho ( T ) < 1$

Let $\mathbf { z }$ be an arbitrary vector, and $\pmb { \mathrm { x } }$ be the unique solution to $\mathbf { x } = T \mathbf { x } + \mathbf { c }$ .Define $\mathbf { x } ^ { ( 0 ) } = \mathbf { x } - \mathbf { z }$ and,for $k \geq 1$ ， $\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c }$ . Then $\{ \mathbf { x } ^ { ( k ) } \}$ converges to $\mathbf { x }$ . Also,

$$
\mathbf { x } - \mathbf { x } ^ { ( k ) } = \left( T \mathbf { x } + \mathbf { c } \right) - \left( T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } \right) = T \left( \mathbf { x } - \mathbf { x } ^ { ( k - 1 ) } \right) ,
$$

so

$$
\mathbf { x } - \mathbf { x } ^ { ( k ) } = T \left( \mathbf { x } - \mathbf { x } ^ { ( k - 1 ) } \right) = T ^ { 2 } \left( \mathbf { x } - \mathbf { x } ^ { ( k - 2 ) } \right) = \cdot \cdot \cdot = T ^ { k } \left( \mathbf { x } - \mathbf { x } ^ { ( 0 ) } \right) = T ^ { k } \mathbf { z } .
$$

Hence $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } T ^ { k } \mathbf { z } = \operatorname* { l i m } _ { k  \infty } T ^ { k } ( \mathbf { x } - \mathbf { x } ^ { ( 0 ) } ) = \operatorname* { l i m } _ { k  \infty } ( \mathbf { x } - \mathbf { x } ^ { ( k ) } ) = \mathbf { 0 } . } \end{array}$

Since $\textbf { z } \in \mathbb { R } ^ { n }$ was arbitrary,this implies that $T$ is a convergent matrix and that $\rho ( T ) < 1$ ■ ■ ■

The proof of the following corollary is similar to the proofs in Corollary 2.4. It is considered in Exercise 11.

If $\| T \| < 1$ forayatualmatidisite $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ defined by $\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c }$ converges, for any $\mathbf { x } ^ { ( 0 ) } \in \mathbb { R } ^ { n }$ , to a vector $\mathbf { x } \in \mathbb { R } ^ { n }$ ,and the following error bounds hold:

$$
\begin{array} { r l } & { \| { \mathbf x } - { \mathbf x } ^ { ( k ) } \| \leq \| T \| ^ { k } \| { \mathbf x } ^ { ( 0 ) } - { \mathbf x } \| ; } \\ & { \| { \mathbf x } - { \mathbf x } ^ { ( k ) } \| \leq \frac { \| T \| ^ { k } } { 1 - \| T \| } \| { \mathbf x } ^ { ( 1 ) } - { \mathbf x } ^ { ( 0 ) } \| . } \end{array}
$$

We have seen that the Jacobi and Gauss-Seidel iterative techniques can be written

$$
\mathbf { x } ^ { ( k ) } = T _ { j } \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } _ { j } \quad { \mathrm { a n d } } \quad \mathbf { x } ^ { ( k ) } = T _ { g } \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } _ { g } ,
$$

using the matrices

$$
T _ { j } = D ^ { - 1 } ( L + U ) \quad \mathrm { a n d } \quad T _ { g } = ( D - L ) ^ { - 1 } U .
$$

If $\rho ( T _ { j } )$ or $\rho ( T _ { g } )$ is less than1, then the corresponding sequence $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ will converge to the solution $\mathbf { x }$ of $A \mathbf { x } = \mathbf { b }$ .For example, the Jacobi scheme has

$$
\mathbf { x } ^ { ( k ) } = { D ^ { - 1 } ( L + U ) } \mathbf { x } ^ { ( k - 1 ) } + { D ^ { - 1 } } \mathbf { b } ,
$$

and, if $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ converges to $\mathbf { X }$ , then

$$
\mathbf { x } = D ^ { - 1 } ( L + U ) \mathbf { x } + D ^ { - 1 } \mathbf { b } .
$$

This implies that

$$
D \mathbf { x } = ( L + U ) \mathbf { x } + \mathbf { b } \quad { \mathrm { a n d } } \quad ( D - L - U ) \mathbf { x } = \mathbf { b } .
$$

Since $D - L - U = A$ , the solution $\mathbf { x }$ satisfies $\pmb { A } \mathbf { x } = \mathbf { b }$

We can now give easily verified sufficiency conditions for convergence of the Jacobi and Gauss-Seidel methods. (To prove convergence for the Jacobi scheme, see Exercise 12, and for the Gauss-Seidel scheme,see [Or,p. 120].)

# Theorem 7.21

f $A$ is strictly diagonally dominant, then for any choice of $\mathbf { x } ^ { ( 0 ) }$ ,both the Jacobi and Gauss-Seidel methods give sequences $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 0 } ^ { \infty }$ that converge to the unique solution of $A \mathbf { x } = \mathbf { b }$

The relationship of the rapidity of convergence to the spectral radius of the iteration matrix $T$ can be seen from Corollary 7.2O. Since the inequalities hold for any natural matrix norm, it follows from the statement after Theorem 7.15 that

$$
\lVert \mathbf { x } ^ { ( k ) } - \mathbf { x } \rVert \approx \rho ( T ) ^ { k } \lVert \mathbf { x } ^ { ( 0 ) } - \mathbf { x } \rVert .
$$

Thus. it is desirable to select the iterative technique with minimal $\rho ( T ) < 1$ for a particular system $A \mathbf { x } = \mathbf { b }$ . No general results exist to tell which of the two techniques, Jacobi or Gauss-Seidel, will be most successful for an arbitrary linear system. In special cases, however, the answer is known,as is demonstrated in the following theorem. The proof of this result can be found in [Y, pp.120-127].

# Theorem 7.22 (Stein-Rosenberg)

If $a _ { i j } \leq 0$ , for each $i \neq j$ and $a _ { i i } > 0$ , for each $i = 1 , 2 , \dots , n$ , then one and only one of the following statements holds:

a. $0 \le \rho ( T _ { g } ) < \rho ( T _ { j } ) < 1 ;$   
b. $1 < \rho ( T _ { j } ) < \rho ( T _ { g } )$   
c. $\rho ( T _ { j } ) = \rho ( T _ { g } ) = 0 ;$   
d. $\rho ( T _ { j } ) = \rho ( T _ { g } ) = 1$

For the special case described in Theorem 7.22, we see from part (a) that when one method gives convergence, then both give convergence, and the Gauss-Seidel method converges faster than the Jacobi method. Part (b) indicates that when one method diverges then both diverge,and the divergence is more pronounced for the Gauss-Seidel method.

Since the rate of convergence of a procedure depends on the spectral radius of the matrix associated with the method, one way to select a procedure to accelerate conver-gence is to choose a method whose associated matrix has minimal spectral radius. Before describing a procedure for selecting such a method, we need to introduce a new means of measuring the amount by which an approximation to the solution to a linear system differs from the true solution to the system. The method makes use of the vector described in the following definition.

Suppose $\tilde { \mathbf { x } } \in \mathbb { R } ^ { n }$ is an approximation to the solution of the linear system defined by $A \mathbf { x } = \mathbf { b }$ · The residual vector for $\tilde { \mathbf { x } }$ with respect to this system is $\mathbf { r } = \mathbf { b } - A \tilde { \mathbf { x } }$

In procedures such as the Jacobi or Gauss-Seidel methods,a residual vector is associated with each calculation of an approximation component to the solution vector. The object is to generate a sequence of approximations that will cause the residual vectors to converge rapidly to zero. Suppose we let

$$
\mathbf { r } _ { i } ^ { ( k ) } = ( r _ { 1 i } ^ { ( k ) } , r _ { 2 i } ^ { ( k ) } , . . . , r _ { n i } ^ { ( k ) } ) ^ { t }
$$

denote the residual vector for the Gauss-Seidel method corresponding to the approximate solution vector $\mathbf { x } _ { i } ^ { ( k ) }$ defined by

$$
\mathbf { x } _ { i } ^ { ( k ) } = ( x _ { 1 } ^ { ( k ) } , x _ { 2 } ^ { ( k ) } , \ldots , x _ { i - 1 } ^ { ( k ) } , x _ { i } ^ { ( k - 1 ) } , \ldots , x _ { n } ^ { ( k - 1 ) } ) ^ { t } .
$$

The mth component of $\mathbf { r } _ { i } ^ { ( k ) }$ is

$$
r _ { m i } ^ { ( k ) } = b _ { m } - \sum _ { j = 1 } ^ { i - 1 } a _ { m j } x _ { j } ^ { ( k ) } - \sum _ { j = i } ^ { n } a _ { m j } x _ { j } ^ { ( k - 1 ) } ,
$$

or, equivalently,

$$
r _ { m i } ^ { ( k ) } = b _ { m } - \sum _ { j = 1 } ^ { i - 1 } a _ { m j } x _ { j } ^ { ( k ) } - \sum _ { j = i + 1 } ^ { n } a _ { m j } x _ { j } ^ { ( k - 1 ) } - a _ { m i } x _ { i } ^ { ( k - 1 ) } ,
$$

for each $m = 1 , 2 , \ldots , n$

In particular, the $i$ th component of $\mathbf { r } _ { i } ^ { ( k ) }$ is

$$
r _ { i i } ^ { ( k ) } = b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } - a _ { i i } x _ { i } ^ { ( k - 1 ) } ,
$$

so

$$
a _ { i i } x _ { i } ^ { ( k - 1 ) } + r _ { i i } ^ { ( k ) } = b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k \cdot 1 ) } .
$$

Recall, however, thatin the Gauss-Seidel method, $x _ { i } ^ { ( k ) }$ is chosen to be

$$
x _ { i } ^ { ( k ) } = \frac { 1 } { a _ { i i } } \left[ b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } \right] ,
$$

so Eq.(7.13) can be rewritten as

$$
a _ { i i } x _ { i } ^ { ( k - 1 ) } + r _ { i i } ^ { ( k ) } = a _ { i i } x _ { i } ^ { ( k ) } .
$$

Consequently,the Gauss-Seidel method can be characterized as choosing $x _ { i } ^ { ( k ) }$ to satisfy

$$
x _ { i } ^ { ( k ) } = x _ { i } ^ { ( k - 1 ) } + \frac { r _ { i i } ^ { ( k ) } } { a _ { i i } } .
$$

We can derive another connection between the residual vectors and the Gauss-Seidel technique. Consider the residual vector $\mathbf { r } _ { i + 1 } ^ { ( k ) }$ , associated with the vector $\mathbf { x } _ { i + 1 } ^ { ( k ) } = ( x _ { 1 } ^ { ( k ) } , \cdot \cdot \cdot ,$ $x _ { i } ^ { ( k ) } , x _ { i + 1 } ^ { ( k - 1 ) } , \dots , x _ { n } ^ { ( k - 1 ) } ) ^ { t }$ . By(7.12), the ihcooto $\mathbf { r } _ { i + 1 } ^ { ( k ) }$ i is

$$
\begin{array} { l } { { r _ { i , i + 1 } ^ { ( k ) } = b _ { i } - \displaystyle \sum _ { j = 1 } ^ { i } a _ { i j } x _ { j } ^ { ( k ) } - \displaystyle \sum _ { j = i \mathrm { ~ i ~ } 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } } } \\ { { = b _ { i } - \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } - \displaystyle \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } - a _ { i i } x _ { i } ^ { ( k ) } . } } \end{array}
$$

Equation (7.14) implies that $r _ { i , i + 1 } ^ { ( k ) } = 0$ . In a sense,then,the Gauss-Seidel technique is also characterized choosing $x _ { i + 1 } ^ { ( k ) }$ in such a way that the $i$ th component of $\mathbf { r } _ { i + 1 } ^ { ( k ) }$ is zero.

Choosing xi+1 so that one coordinate of the residual vector is zero, however, is not the mosteffcentwatoreducetenofhee $\mathbf { r } _ { i + 1 } ^ { ( k ) }$ .If we modifythe Gauss-Seidel procedure,as given by Eq. (7.15), to

$$
x _ { i } ^ { ( k ) } = x _ { i } ^ { ( k - 1 ) } + \omega \frac { r _ { i i } ^ { ( k ) } } { a _ { i i } } ,
$$

for certain choices of positive $\omega$ , we can reduce the norm of the residual vector and obtain significantly faster convergence.

Methods involving Eq.(7.16) are called relaxation methods. For choices of $\omega$ with $0 ~ < ~ \omega ~ < ~ 1$ ， the procedures are called under-relaxation methods and can be used to obtain convergence of some systems that are not convergent by the Gauss-Seidel method. For choices of $\omega$ with $1 < \omega$ ， the procedures are called over-relaxation methods, which are used to accelerate the convergence for systems that are convergent by the Gauss-Seidel technique.These methods are abbreviated SOR,for Successive Over-Relaxation, and are particularly useful for solving the linear systems that occur in the numerical solution of certain partial-differential equations.

Beforeillustrating the advantages of the SOR method,wenotethatby using Eq (7.13), Eq. (7.16) can be reformulated for calculation purposes to

$$
x _ { i } ^ { ( k ) } = ( 1 - \omega ) x _ { i } ^ { ( k - 1 ) } + \frac { \omega } { a _ { i i } } \left[ b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } \right] .
$$

To determine the matrix of the SOR method, we rewrite this as

$$
a _ { i i } x _ { i } ^ { ( k ) } + \omega \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ^ { ( k ) } = ( 1 - \omega ) a _ { i i } x _ { i } ^ { ( k - 1 ) } - \omega \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ^ { ( k - 1 ) } + \omega b _ { i } ,
$$

so that in vector form, we have

$$
( D - \omega L ) \mathbf { x } ^ { ( k ) } = \left\{ ( 1 - \omega ) D + \omega U ] \mathbf { x } ^ { ( k - 1 ) } + \omega \mathbf { b } \right.
$$

or

$$
\mathbf { x } ^ { ( k ) } = ( D - \omega L ) ^ { - 1 } [ ( 1 - \omega ) D + \omega U ] \mathbf { x } ^ { ( k - 1 ) } + \omega ( D - \omega L ) ^ { - 1 } \mathbf { b } .
$$

If we let $T _ { \omega } = ( D - \omega L ) ^ { - 1 } [ ( 1 - \omega ) D + \omega U ]$ and $\mathbf { c } _ { \omega } = \omega ( D - \omega L ) ^ { - 1 } \mathbf { b }$ , the SOR technique has the form

$$
\mathbf { x } ^ { ( k ) } = T _ { \omega } \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } _ { \omega } .
$$

The linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ given by

$$
\begin{array} { c c } { { 4 x _ { 1 } + 3 x _ { 2 } } } & { { = 2 4 , } } \\ { { } } & { { } } \\ { { 3 x _ { 1 } + 4 x _ { 2 } - x _ { 3 } = 3 0 , } } \\ { { } } & { { } } \\ { { - } } & { { x _ { 2 } + 4 x _ { 3 } = - 2 4 , } } \end{array}
$$

has the solution $( 3 , 4 , - 5 ) ^ { i }$ . The Gauss-Seidel method and the SOR method with $\omega = 1 . 2 5$ will be used to solve this system, using $\mathbf { x } ^ { ( 0 ) } = \left( 1 , 1 , 1 \right) ^ { t }$ for both methods.For each $k =$ $1 , 2 , \ldots$ , the equations for the Gauss-Seidel method are

$$
\begin{array} { l } { { x _ { 1 } ^ { ( k ) } = - 0 . 7 5 x _ { 2 } ^ { ( k - 1 ) } + 6 , } } \\ { { x _ { 2 } ^ { ( k ) } = - 0 . 7 5 x _ { 1 } ^ { ( k ) } + 0 . 2 5 x _ { 3 } ^ { ( k - 1 ) } + 7 . 5 , } } \\ { { x _ { 3 } ^ { ( k ) } = 0 . 2 5 x _ { 2 } ^ { ( k ) } - 6 , } } \end{array}
$$

and the equations for the SOR method with $\omega = 1 . 2 5$ are

$$
\begin{array} { r l } & { x _ { 1 } ^ { ( k ) } = - 0 . 2 5 x _ { 1 } ^ { ( k - 1 ) } - 0 . 9 3 7 5 x _ { 2 } ^ { ( k - 1 ) } + 7 . 5 , } \\ & { x _ { 2 } ^ { ( k ) } = - 0 . 9 3 7 5 x _ { 1 } ^ { ( k ) } - 0 . 2 5 x _ { 2 } ^ { ( k - 1 ) } + 0 . 3 1 2 5 x _ { 3 } ^ { ( k - 1 ) } + 9 . 3 7 5 , } \\ & { x _ { 3 } ^ { ( k ) } = 0 . 3 1 2 5 x _ { 2 } ^ { ( k ) } - 0 . 2 5 x _ { 3 } ^ { ( k - 1 ) } - 7 . 5 . } \end{array}
$$

The first seven iterates for each method are listed in Tables 7.3 and 7.4.For the iterates to be accurate to seven decimal places, the Gauss-Seidel method requires 34 iterations, as opposed to 14 iterations for the over-relaxation method with $\omega = 1 . 2 5$

Table 7.3 Gauss-Seidel   

<table><tr><td>k</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>x</td><td>1</td><td>5.250000</td><td>3.1406250</td><td>3.0878906</td><td>3.0549316</td><td>3.0343323</td><td>3.0214577</td><td>3.0134110</td></tr><tr><td></td><td>1</td><td>3.812500</td><td>3.8828125</td><td>3.9267578</td><td>3.9542236</td><td>3.9713898</td><td>3.9821186</td><td>3.9888241</td></tr><tr><td></td><td>1</td><td>-5.046875</td><td>-5.0292969</td><td>-5.0183105</td><td>−5.0114441</td><td>-5.0071526</td><td>-5.0044703</td><td>-5.0027940</td></tr></table>

Table 7.4 SOR with $\omega = 1 . 2 5$   

<table><tr><td>k</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>x</td><td>1</td><td>6.312500</td><td>2.6223145</td><td>3.1333027</td><td>2.9570512</td><td>3.0037211</td><td>2.9963276</td><td>3.0000498</td></tr><tr><td></td><td>1</td><td>3.5195313</td><td>3.9585266</td><td>4.0102646</td><td>4.0074838</td><td>4.0029250</td><td>4.0009262</td><td>4.0002586</td></tr><tr><td></td><td>1</td><td>-6.6501465</td><td>-4.6004238</td><td>-5.0966863</td><td>-4.9734897</td><td>-5.0057135</td><td>-4.9982822</td><td>-5.0003486</td></tr></table>

The obvious question to ask is how the appropriate value of $\omega$ is chosen. Although no complete answer to this question is known for the general $n \times n$ linear system, the following results can be used in certain situations.

# Theorem 7.24 (Kahan)

If $a _ { i i } \neq 0$ , for each $i = 1 , 2 , \dots , n$ ,then $\rho ( T _ { \omega } ) \ge | \omega - 1 |$ . This implies that the SOR method can converge only if $0 < \omega < 2$

The proof of this theorem is considered in Exercise 13. The proof of the next two results can be found in $[ 0 \mathbf { r } 2$ , pp.123-133]. These results will be used in Chapter 12.

# Theorem 7.25 (Ostrowski-Reich)

If $A$ is a positive definite matrix and $0 < \omega < 2$ , then the SOR method converges for any choice of initial approximate vector x(0).

# Theorem 7.26

If $A$ is positive definite and tridiagonal, then $\rho ( T _ { g } ) = [ \rho ( T _ { j } ) ] ^ { 2 } < 1$ , and the optimal choice of $\omega$ for the SOR method is

$$
\omega = \frac { 2 } { 1 + \sqrt { 1 - [ \rho ( T _ { j } ) ] ^ { 2 } } } .
$$

With this choice of $\omega$ , we have $\rho ( T _ { \omega } ) = \omega - 1$

# EXAMPLE 4

The matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} } \right] { \mathrm { , } }
$$

given in Example 3,is positive definite and tridiagonal, so Theorem 7.26 applies. Since

$$
T _ { j } = D ^ { - 1 } ( L + U ) = \left[ { \begin{array} { c c c } { { \frac { 1 } { 4 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \frac { 1 } { 4 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \frac { 1 } { 4 } } } \end{array} } \right] \left[ { \begin{array} { c c c } { { 0 } } & { { - 3 } } & { { 0 } } \\ { { - 3 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \end{array} } \right] = \left[ { \begin{array} { c c c } { { 0 } } & { { - 0 . 7 5 } } & { { 0 } } \\ { { - 0 . 7 5 } } & { { 0 } } & { { 0 . 2 5 } } \\ { { 0 } } & { { 0 . 2 5 } } & { { 0 } } \end{array} } \right] .
$$

we have

$$
T _ { j } - \lambda I = \left[ \begin{array} { c c c } { { - \lambda } } & { { - 0 . 7 5 } } & { { 0 } } \\ { { - 0 . 7 5 } } & { { - \lambda } } & { { 0 . 2 5 } } \\ { { 0 } } & { { 0 . 2 5 } } & { { - \lambda } } \end{array} \right] ,
$$

so

$$
\operatorname* { d e t } ( T _ { j } - \lambda I ) = - \lambda ( \lambda ^ { 2 } - 0 . 6 2 5 ) .
$$

Thus,

$$
\rho ( T _ { j } ) = \sqrt { 0 . 6 2 5 }
$$

and

$$
\omega = \frac { 2 } { 1 + \sqrt { 1 - [ \rho ( T _ { j } ) ] ^ { 2 } } } = \frac { 2 } { 1 + \sqrt { 1 - 0 . 6 2 5 } } \approx 1 . 2 4 .
$$

This explains the rapid convergence obtained in Example 1 when using $\omega = 1 . 2 5$

We close this section with Algorithm 7.3 for the SOR method.

# SOR

To solve $\pmb { A } \mathbf { x } = \mathbf { b }$ given the parameter $\omega$ and an initial approximation $\mathbf { x } ^ { ( 0 ) }$ ：

INPUT the number of equations and unknowns $\pmb { n }$ ; the entries $a _ { i j }$ ， $1 \leq i , j \leq n$ ,of the matrix A; the entries $b _ { i }$ ， $1 \leq i \leq n$ ,of $\mathbf { b }$ ; the entries $X O _ { i }$ ， $1 \leq i \leq n$ ,of $\mathbf { X 0 } = \mathbf { x } ^ { ( 0 ) }$ : the parameter $\omega$ ; tolerance $T O L$ ; maximum number of iterations $N$

OUTPUTthe approximate solution $x _ { 1 } , \ldots , x _ { n }$ or a message that the number of iterations was exceeded.

Step 1 Set $k = 1$

Step 2 While $( k \leq N )$ do Steps 3-6.

Step 3 $\operatorname { F o r } i = 1 , \ldots , n$

$$
\mathsf { s e t } x _ { i } = ( 1 - \omega ) X O _ { i } + \frac { \omega ( - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } - \sum _ { j = i + 1 } ^ { n } a _ { i j } X O _ { j } + b _ { i } ) } { a _ { i i } } .
$$

Step 4 If $| | { \mathbf { x } } - { \mathbf { X 0 } } | | < T O L$ then OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ； (The procedure was successful.) STOP.

Step 5 Set $k = k + 1$

Step 6 For $i = 1 , \ldots , n$ set $X O _ { i } = x _ { i }$

Step 7OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was successful.) STOP.

# EXERCISE SET 7.3

1.Find the first two iterations of the Jacobi method for the following linear systems, using $\mathbf { X } ^ { ( 0 ) } = \mathbf { 0 }$

$$
\begin{array} { r l r } & { } & { 3 x _ { 1 } - x _ { 2 } + x _ { 3 } = 1 , } \\ & { } & \\ & { } & { 3 x _ { 1 } + 6 x _ { 2 } + 2 x _ { 3 } = 0 . } \\ & { } & \\ & { } & { 3 x _ { 1 } + 3 x _ { 2 } + 7 x _ { 3 } = 4 . } \end{array}
$$

$$
\begin{array} { r l r } { 1 0 x _ { 1 } - } & { { } x _ { 2 } } & { = 9 , } \\ { - x _ { 1 } + 1 0 x _ { 2 } - } & { { } 2 x _ { 3 } = 7 , } & { } \\ { - } & { { } 2 x _ { 2 } + 1 0 x _ { 3 } = 6 . } & { } \end{array}
$$

c. $\begin{array} { r l r } { 1 0 x _ { 1 } + } & { 5 x _ { 2 } } & { = 6 , } \\ { } & { 5 x _ { 1 } + 1 0 x _ { 2 } - 4 x _ { 3 } } & { = 2 5 , } \\ { } & { - } & { 4 x _ { 2 } + 8 x _ { 3 } - } & { x _ { 4 } = - 1 1 , } \\ { } & { - } & { x _ { 3 } + 5 x _ { 4 } = - 1 1 . } \end{array}$ d. $\begin{array} { r } { \begin{array} { r c l } { 4 x _ { 1 } + } & { x _ { 2 } - } & { x _ { 3 } + } & { x _ { 4 } = - 2 , } \\ & { x _ { 1 } + 4 x _ { 2 } - } & { x _ { 3 } - } & { x _ { 4 } = - 1 , } \\ & { - x _ { 1 } - } & { x _ { 2 } + 5 x _ { 3 } + } & { x _ { 4 } = 0 , } \\ & { x _ { 1 } - } & { x _ { 2 } + } & { x _ { 3 } + 3 x _ { 4 } = 1 . } \end{array} } \end{array}$

$$
\begin{array} { r } { \left. \begin{array} { c c c c } { . } & { 4 x _ { 1 } + \ x _ { 2 } + \ x _ { 3 } + } & { x _ { 5 } = 6 . } \\ { . } & { - x _ { 1 } - 3 x _ { 2 } + \ x _ { 3 } + } & { x _ { 4 } } & { = 6 . } \\ { } & { 2 x _ { 1 } + \ x _ { 2 } + 5 x _ { 3 } - } & { x _ { 4 } - } & { x _ { 5 } = 6 , } \\ { } & { - x _ { 1 } - } & { x _ { 2 } - } & { x _ { 3 } + 4 x _ { 4 } } & { = 6 , } \\ { } & { 2 x _ { 2 } - } & { x _ { 3 } + } & { x _ { 4 } + 4 x _ { 5 } = 6 . } \end{array} \right. } \end{array}
$$

$$
{ \begin{array} { r l r l } & { 4 x _ { 1 } - \ x _ { 2 } } & { - \ x _ { 4 } } & & { = 0 , } \\ & { - x _ { 1 } + 4 x _ { 2 } - \ x _ { 3 } } & & { - \ x _ { 5 } } & { = 5 , } \\ & { - \ x _ { 2 } + 4 x _ { 3 } } & & { - \ x _ { 6 } = 0 , } \\ & { - x _ { 1 } } & & { + 4 x _ { 4 } - \ x _ { 5 } } & { = 6 , } \\ & { - \ x _ { 2 } } & { - \ x _ { 4 } + 4 x _ { 5 } - \ x _ { 6 } = - 2 , } \\ & { - \ x _ { 3 } } & & { - \ x _ { 5 } + 4 x _ { 6 } = 6 . } \end{array} }
$$

2.Repeat Exercise 1 using the Gauss-Seidel method.

3.Use the Jacobi method to solve the linear systems in Exercise 1, with $T O L = 1 0 ^ { - 3 }$ in the ${ \mathit { l } } _ { \infty }$ norm.

4.Repeat Exercise 3 using the Gauss-Seidel Algorithm.

5. Find the first two iterations of the SOR method with $\omega = 1 . 1$ for the following linear systems, using ${ \bf { X } } ^ { ( 0 ) } = { \bf { 0 } }$ ：

$$
\begin{array} { r l r } { { 3 } x _ { 1 } - \mathrm {  ~ \nabla ~ } x _ { 2 } + \mathrm {  ~ \nabla ~ } x _ { 3 } = 1 , } & { \qquad } & { { \bf b } . \quad 1 0 x _ { 1 } - \mathrm {  ~ \nabla ~ } x _ { 2 } \quad \mathrm {  ~ \Gamma ~ } = 9 , } \\ { 3 x _ { 1 } + 6 x _ { 2 } + 2 x _ { 3 } = 0 , } & { \qquad } & { { } - x _ { 1 } + 1 0 x _ { 2 } - \mathrm {  ~ \nabla ~ } 2 x _ { 3 } = 7 , } \\ { 3 x _ { 1 } + 3 x _ { 2 } + 7 x _ { 3 } = 4 . } & { \qquad } & { { } - \mathrm {  ~ \nabla ~ } 2 x _ { 2 } + 1 0 x _ { 3 } = 6 . } \end{array}
$$

$$
\begin{array} { r l } { { 1 0 x _ { 1 } + \ 5 x _ { 2 } \qquad } } & { { = 6 , } } \\ { { 5 x _ { 1 } + 1 0 x _ { 2 } - 4 x _ { 3 } \qquad } } & { { = 2 5 , } } \\ { { - \ 4 x _ { 2 } + 8 x _ { 3 } - \ x _ { 4 } = - 1 1 , } } & { { \qquad } } & { { - x _ { 1 } - \ x _ { 2 } + 5 x _ { 3 } + \ x _ { 4 } = 0 , } } \\ { { \qquad - \ x _ { 3 } + 5 x _ { 4 } = - 1 1 . } } & { { \qquad } } & { { \ x _ { 1 } - \ x _ { 2 } + \ x _ { 3 } + 3 x _ { 4 } = 1 . } } \end{array}
$$

$$
\begin{array} { r l r } { 4 x _ { 1 } + } & { x _ { 2 } + } & { x _ { 3 } + } & { x _ { 5 } = 6 , } \\ { } & { } & { - x _ { 1 } - 3 x _ { 2 } + } & { x _ { 3 } + } & { x _ { 4 } \qquad = 6 , } \\ { } & { } & { 2 x _ { 1 } + } & { x _ { 2 } + 5 x _ { 3 } - } & { x _ { 4 } - } & { x _ { 5 } = 6 , } \\ { } & { } & { - x _ { 1 } - } & { x _ { 2 } - } & { x _ { 3 } + 4 x _ { 4 } \qquad = 6 , } \\ { } & { } & { 2 x _ { 2 } - } & { x _ { 3 } + } & { x _ { 4 } + 4 x _ { 5 } = 6 . } \end{array}
$$

$$
\begin{array} { r l r l } & { \begin{array} { r l r l r l } { { 4 } x _ { 1 } - } & { x _ { 2 } } & & { - } & { x _ { 4 } } & & & { = 0 , } \\ & { - x _ { 1 } + 4 x _ { 2 } - } & { x _ { 3 } } & & { - } & { x _ { 5 } } & & { = 5 , } \\ & { - } & { x _ { 2 } + 4 x _ { 3 } } & & { - } & { x _ { 6 } = 0 , } \end{array} } \\ & { \begin{array} { r l r l } & { - x _ { 1 } } & & { + 4 x _ { 4 } - } & { x _ { 5 } } & & { = 6 , } \\ & { - } & { x _ { 2 } } & & { - } & { x _ { 4 } + 4 x _ { 5 } - } & { x _ { 6 } = - 2 , } \\ & { - } & { x _ { 3 } } & & { - } & { x _ { 5 } + 4 x _ { 6 } = 6 . } \end{array} } \end{array}
$$

6. Repeat Exercise l using $\omega = 1 . 3$

7.Use the SOR method with $\omega = 1 . 2$ to solve the linear systems in Exercise 5 with a tolerance $T O L = 1 0 ^ { - 3 }$ in the ${ l } _ { \infty }$ norm.

8. Determine which matrices in Exercise 5 are tridiagonal and positive definite. Repeat Exercise 7 for these matrices using the optimal choice of $\omega$

9. The linear system

$$
\begin{array} { c } { 2 x _ { 1 } - x _ { 2 } + x _ { 3 } = - 1 , } \\ { \qquad } \\ { 2 x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 4 , } \\ { \qquad } \\ { - x _ { 1 } - x _ { 2 } + 2 x _ { 3 } = - 5 } \end{array}
$$

has the solution $( 1 , 2 , - 1 ) ^ { t }$

a. Show that $\begin{array} { r } { \rho ( T _ { j } ) = \frac { \sqrt { 5 } } { 2 } > 1 } \end{array}$   
$\mathbf { b } _ { \bullet }$ Show that the Jacobi method with $\mathbf { X } ^ { ( 0 ) } = \mathbf { 0 }$ fails to give a good approximation after 25 iterations.   
c. Show that $\begin{array} { r } { \rho ( T _ { g } ) = \frac { 1 } { 2 } } \end{array}$   
d. Use the Gauss-Seidel method with $\mathbf { x } ^ { ( 0 ) } = \mathbf { 0 }$ to approximate the solution to the linear system to within $1 0 ^ { - 5 }$ in the ${ { l } _ { \infty } }$ norm.

10. The linear system

$$
\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } - 2 x _ { 3 } = 7 , } \\ { x _ { 1 } + x _ { 2 } + x _ { 3 } = 2 , } \\ { 2 x _ { 1 } + 2 x _ { 2 } + x _ { 3 } = 5 } \end{array}
$$

has the solution $( 1 , 2 , - 1 ) ^ { t }$

a. Show that $\rho ( T _ { j } ) = 0$ .   
$\mathbf { b } .$ Use the Jacobi method with $\mathbf { x } ^ { ( 0 ) } = \mathbf { 0 }$ to approximate the solution to the linear system to within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm.   
c. Show that $\rho ( T _ { g } ) = 2$   
d. Show that the Gauss-Seidel method applied as in part (b) fails to give a good approximation in 25 iterations.

11.a.Prove that

$$
\| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| \leq \| T \| ^ { k } \ \| { \mathbf { x } } ^ { ( 0 ) } - { \mathbf { x } } \| \quad { \mathrm { a n d } } \quad \| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| \leq \frac { \| T \| ^ { k } } { 1 - \| T \| } \| { \mathbf { x } } ^ { ( 1 ) } - { \mathbf { x } } ^ { ( 0 ) } \| .
$$

where $T$ is an $n \times n$ matrix with $\| T \| < 1$ and

$$
\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c } , \quad k = 1 , 2 , \ldots ,
$$

with $\mathbf { x } ^ { ( 0 ) }$ arbitrary, $\mathbf { c } \in \mathbb { R } ^ { n }$ ,and ${ \mathbf { x } } = T { \mathbf { x } } + { \mathbf { c } }$ b.Apply the bounds to Exercise 1, when possible,using the $l _ { \infty }$ norm.

12.Show that if $A$ is strictly diagonally dominant, then $| | T _ { j } | | _ { \infty } < 1$

13.Prove Theorem 7.24.[Hint: If $\lambda _ { 1 } , \ldots , \lambda _ { n }$ are eigenvalues of $T _ { \omega }$ , then det $\begin{array} { r } { T _ { \omega } = \prod _ { i = 1 } ^ { n } \lambda _ { i } } \end{array}$ .Since det $D ^ { - 1 } = \operatorname* { d e t } ( D - \omega L ) ^ { - 1 }$ and the determinant of a product of matrices is the product of the determinants of the factors,the result follows from Eq. (7.17).]

14. Suppose that an object can be at any one of $n + 1$ equally spaced points $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ . When an object is at location $x _ { i }$ , it is equally likely to move to either $x _ { i - 1 }$ or $x _ { i + 1 }$ and cannot directly move to any other location. Consider the probabilities $\{ { P } _ { i } \} _ { i = 0 } ^ { n }$ that an object starting at location $x _ { i }$ will reach the left endpoint $x _ { 0 }$ before reaching the right endpoint $x _ { n }$ . Clearly, $P _ { 0 } = 1$ and $P _ { n } = 0$ . Since the object can move to $x _ { i }$ only from $x _ { i - 1 }$ or $x _ { i + 1 }$ and does so with probability $\frac { 1 } { 2 }$ for each of these locations,

$$
P _ { i } = \frac { 1 } { 2 } P _ { i - 1 } + \frac { 1 } { 2 } P _ { i + 1 } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , n - 1 .
$$

a. Show that

$$
\left[ { \begin{array} { c c c c c c c } { 1 } & { - { \frac { 1 } { 2 } } } & { 0 { \div } \cdots \cdots \cdots \cdots } & { 0 } \\ { - { \frac { 1 } { 2 } } } & { 1 } & { - { \frac { 1 } { 2 } } \cdots } & & & { \vdots } \\ { 0 { \cdot } } & { - { \frac { 1 } { 2 } } { \cdot } _ { \cdot } } & { 1 . . . } & & & { \vdots } \\ { { \cdot } } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { { \cdot } } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { { \cdot } } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { { \cdot } } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { { \cdot } } & { \ddots } & { \ddots } & { \ddots } & { 1 } & { - { \frac { 1 } { 2 } } } \end{array} } \right] \left[ { \begin{array} { c } { P _ { 1 } } \\ { P _ { 2 } } \\ { \vdots } \\ { P _ { n - 1 } } \end{array} } \right] = \left[ { \begin{array} { c } { { \frac { 1 } { 2 } } } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} } \right] .
$$

b. Solve this system using $n = 1 0 , 5 0$ , and 100.   
$\mathbf { c } .$ Change the probabilities to $\pmb { \alpha }$ and $1 - \alpha$ for movement to the left and right, respectively, and derive the linear system similar to the one in part (a).   
d. Repeat part (b) with $\begin{array} { r } { \alpha = \frac { 1 } { 3 } } \end{array}$

15.Use all the applicable methods in this section to solve the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ to within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm, where the entries of $A$ are

$$
a _ { i , j } = \left\{ \begin{array} { l l } { 2 i , } & { \mathrm { w h e n ~ } j = i \mathrm { ~ a n d ~ } i = 1 , 2 , \dots , 8 0 , } \\ & { } \\ { 0 . 5 i , } & { \mathrm { w h e n } \left\{ { j = i + 2 \mathrm { ~ a n d ~ } i = 1 , 2 , \dots , 7 8 , } \right. } \\ & { } \\ { 0 . 5 i , } & { \mathrm { ~ w h e n } \left\{ { j = i - 2 \mathrm { ~ a n d ~ } i = 3 , 4 , \dots , 8 0 , } \right. } \\ & { } \\ { 0 . 2 5 i , } & { \mathrm { w h e n } \left\{ { j = i + 4 \mathrm { ~ a n d ~ } i = 1 , 2 , \dots , 7 6 , } \right. } \\ & { } \\ { 0 , } & { \mathrm { ~ o t h e r w i s e , } } \end{array} \right.
$$

and those of $\mathbf { b }$ are $b _ { i } = \pi$ , for each $i = 1 , 2 , \dots , 8 0$

16. Suppose that $A$ is a positive definite.

a. Show that we can write $A = D - L - L ^ { t }$ ，where $D$ is diagonal with $d _ { i i } \ > \ 0$ for each $1 \leq i \leq n$ and $L$ is lower triangular. Further, show that $D - L$ is nonsingular.   
b. Let $T _ { g } = ( D - L ) ^ { - 1 } L ^ { t }$ and $P = A - T _ { g } ^ { t } A T _ { g }$ . Show that $P$ is symmetric.   
$\mathbf { c } .$ Show that $T _ { g }$ can also be written as $T _ { \xi } = I - ( D - L ) ^ { - 1 } A$   
d. Let $Q = ( D - L ) ^ { - 1 } A$ . Show that $T _ { g } = I - Q$ and $P = Q ^ { t } [ A Q ^ { - 1 } - A + ( Q ^ { t } ) ^ { - 1 } A ] Q$   
e. Show that $P = Q ^ { \prime } D Q$ and $P$ is positive definite.   
f. Let $\lambda$ be an eigenvalue of $T _ { g }$ with eigenvector $\mathbf { x } \neq \mathbf { 0 }$ . Use part (b) to show that $\mathbf { x } ^ { t } P \mathbf { x } > 0$ implies that $| \lambda | < 1$   
g. Show that $T _ { g }$ is convergent and prove that the Gauss-Seidel method converges.

17.Extend the method of proof in Exercise 16 to the SOR method with $0 < \omega < 2$

18. The forces on the bridge trussdescribed in the opening to this chapter satisfy the equations in the following table:

<table><tr><td>JointHorizontal Component</td><td>Vertical Component</td></tr><tr><td>-F+√f+f=0 ①</td><td>Vf1-F2=0</td></tr><tr><td>-f+f=0 ②</td><td>-f-f+2f4=0</td></tr><tr><td>③ -f+fs=0</td><td>f-10,000= 0</td></tr><tr><td>-f4-fs=0 ④</td><td>2f4-F=0</td></tr></table>

This linear system can be placed in the matrix form

$$
\begin{array} { r } { \left[ \begin{array} { c c c c c c c c c } { - 1 } & { 0 } & { 0 } & { \frac { \sqrt { 2 } } { 2 } } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 0 } & { \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { - 1 } & { \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 0 } & { \frac { \sqrt { 3 } } { 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - \frac { \sqrt { 3 } } { 2 } } & { - 1 } \end{array} \right] \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { F _ { 3 } } \\ { f _ { 1 } } \\ { f _ { 2 } } \\ { f _ { 3 } } \\ { f _ { 4 } } \\ { f _ { 5 } } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 0 } \\ { 0 } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] . } \end{array}
$$

a. Explain why the system of equations was reordered.

b. Approximate the solution of the resulting linear system to within $1 0 ^ { - 2 }$ in the $l _ { \infty }$ norm using as initial approximation the vector all of whose entries are 1s and (i) the Gauss-Seidel method, (ii) the Jacobi method, and (iii) the SOR method with $\omega = 1 . 2 5$

# 7.4 Error Bounds and Iterative Refinement

It seems intuitively reasonable that if $\tilde { \mathbf { x } }$ is an approximation to the solution $\mathbf { X }$ of $A \mathbf { x } = \mathbf { b }$ and the residual vector $\mathbf { r } = \mathbf { b } - A \tilde { \mathbf { x } }$ has the property that $\| \mathbf { r } \| = \| \mathbf { b } - A \tilde { \mathbf { x } } \|$ is small, then $\| \mathbf { X } - { \tilde { \mathbf { X } } } \|$ would be small as well This is often the case, but certain systems, which occur frequently in practice, fail to have this property.

The linear system $A \mathbf { x } = \mathbf { b }$ given by

$$
\left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 1 } & { 2 } \end{array} \right] \left[ \begin{array} { c c } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { 3 } \\ { 3 . 0 0 0 1 } \end{array} \right]
$$

has the unique solution $\mathbf { x } = ( 1 , 1 ) ^ { t }$ . The poor approximation $\tilde { \mathbf { x } } = ( 3 , 0 ) ^ { t }$ has the residual vector

$$
\mathbf { r } = \mathbf { b } - A \tilde { \mathbf { x } } = \left[ \begin{array} { c } { 3 } \\ { 3 . 0 0 0 1 } \end{array} \right] - \left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 1 } & { 2 } \end{array} \right] \left[ \begin{array} { c } { 3 } \\ { 0 } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { - 0 . 0 0 0 2 } \end{array} \right] ,
$$

s0 $\| \mathbf { r } \| _ { \infty } = 0 . 0 0 0 2$ . Although the norm of the residual vector is small, the approximation $\tilde { \mathbf { x } } = ( 3 , 0 ) ^ { t }$ is obviously quite poor; in fact, $\| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } = 2$

The diffculty in Example 1 is explained quite simply by noting that the solution to the system represents the intersection of the lines

$$
l _ { 1 } : \quad x _ { 1 } + 2 x _ { 2 } = 3 \quad { \mathrm { a n d } } \quad l _ { 2 } : \quad 1 . 0 0 0 1 x _ { 1 } + 2 x _ { 2 } = 3 . 0 0 0 1 .
$$

The point (3,0) lies on $l _ { 1 }$ , and the lines are nearly parallel. This implies that $( 3 , 0 )$ also lies close to $l _ { 2 }$ , even though it differs significantly from the solution of the system, given by the intersection point (1,1). (See Figure 7.7.)

![](images/f162992b539711344f4d5c515dbf77102ee245f7c7bb82548cc73d7d62a9f0b2.jpg)  
Figure 7.7

Example 1 was clearly constructed to show the difficulties that can-and,in fact, do— arise.Had the lines not been nearly coincident, we would expect a smallresidual vector to imply an accurate approximation.

In the general situation, we cannot rely on the geometry of the system to give an indication of when problems might occur. We can, however,obtain this information by considering the norms of the matrix $A$ and its inverse.

Suppose that $\tilde { \mathbf { x } }$ is an approximation to the solution of $A \mathbf { x } = \mathbf { b } , A$ is a nonsingular matrix, and $\mathbf { r }$ is the residual vector for $\tilde { \mathbf { x } }$ . Then for any natural norm,

$$
\| \mathbf { x } - { \tilde { \mathbf { x } } } \| \leq \| \mathbf { r } \| \cdot \| A ^ { - 1 } \|
$$

and if $\mathbf { x } \neq \mathbf { 0 }$ and $\mathbf { b } \neq \mathbf { 0 }$ ，

$$
{ \frac { \| \mathbf { x } - { \tilde { \mathbf { x } } } \| } { \| \mathbf { x } \| } } \leq \| A \| \cdot \| A ^ { - 1 } \| { \frac { \| \mathbf { r } \| } { \| \mathbf { b } \| } } .
$$

Proof Since $\mathbf { r } = \mathbf { b } - A \tilde { \mathbf { x } } = A \mathbf { x } - A \tilde { \mathbf { x } }$ and $A$ is nonsingular, $\mathbf { x } - \tilde { \mathbf { x } } = A ^ { - 1 } \mathbf { r }$ . Theorem 7.11 in Section 7.1 implies that

$$
\left\| \mathbf { x } - { \tilde { \mathbf { x } } } \right\| = \left\| A ^ { - 1 } \mathbf { r } \right\| \leq \left\| A ^ { - 1 } \right\| \cdot \left\| \mathbf { r } \right\| .
$$

Moreover,since $\mathbf { b } = A \mathbf { x }$ ,we have $\| \mathbf { b } \| \leq \| A \| \cdot \| \mathbf { x } \| , \operatorname { s o } 1 / \| \mathbf { x } \| \leq \| A \| / \| \mathbf { b } \|$ and

$$
{ \frac { \| \mathbf { x } - { \tilde { \mathbf { x } } } \| } { \| \mathbf { x } \| } } \leq { \frac { \| A \| \cdot \| A ^ { - 1 } \| } { \| \mathbf { b } \| } } \| \mathbf { r } \| .
$$

The inequalities in Theorem 7.27 imply that $\| A ^ { - 1 } \|$ and $\left\| A \right\| \cdot \left\| A ^ { - 1 } \right\|$ provide an indication of the connection between the residual vector and the accuracy of the approximation. In general, the relative error $\| { \bf x } - \tilde { { \bf x } } \| / \| { \bf x } \|$ is of most interest, and, by Inequality (7.19), this error is bounded by the product of $\| A \| \cdot \| A ^ { - 1 } \|$ with the relative residual for this approximation, $\| \mathbf { r } \| / \| \mathbf { b } \|$ . Any convenient norm can be used for this approximation; the only requirement is that it be used consistently throughout.

Definition 7.28The condition number of the nonsingular matrix $A$ relative to a norm $1 1 . 1 1$ is

$$
K ( A ) = \| A \| \cdot \| A ^ { - 1 } \| .
$$

With this notation, the inequalities in Theorem 7.27 become

$$
\| \mathbf { x } - { \tilde { \mathbf { x } } } \| \leq K ( A ) { \frac { \| \mathbf { r } \| } { \| A \| } }
$$

and

$$
{ \frac { \| \mathbf { x } - { \tilde { \mathbf { x } } } \| } { \| \mathbf { x } \| } } \leq K \left( A \right) { \frac { \| \mathbf { r } \| } { \| \mathbf { b } \| } } .
$$

For any nonsingular matrix $A$ and natural norm $\Vert \cdot \Vert$ ，

$$
1 = \| I \| = \| A \cdot A ^ { - 1 } \| \leq \| A \| \cdot \| A ^ { - 1 } \| = K ( A ) .
$$

A matrix A is well-conditioned if K(A) is close to 1,and is il-conditioned when K(A） is significantly greater than 1. Conditioning in this context refers to the relative security that a small residual vector implies a correspondingly accurate approximate solution.

# EXAMPLE 2

The matrix for the system considered in Example 1 was

$$
A = \left[ { \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 1 } & { 2 } \end{array} } \right] ,
$$

which has $\| A \| _ { \infty } = 3 . 0 0 0 1$ . This norm would not be considered large. However,

$$
A ^ { - 1 } = { \left[ \begin{array} { l l } { - 1 0 0 0 0 } & { 1 0 0 0 0 } \\ { 5 0 0 0 . 5 } & { - 5 0 0 0 } \end{array} \right] } , \quad \mathbf { s o } \quad \| A ^ { - 1 } \| _ { \infty } = 2 0 0 0 0 ,
$$

and for the infinity norm, $K ( A ) = ( 2 0 0 0 0 ) ( 3 . 0 0 0 1 ) = 6 0 0 0 2$ . The size of the condition number for this example should certainly keep us from making hasty accuracy decisions based on the residual of an approximation.

In Maple the condition number $K _ { \infty }$ can be computed as follows:

>with(linalg);   
>A:=matrix(2,2,[1,2,1.0001,2]);   
>cond(A);

# 60002.00000

Although the condition number of a matrix depends totally on the norms of the matrix and its inverse,in practice the calculation of the inverse is subject to roundoff error and is dependent on the accuracy with which the calculations are performed.If the operations involve arithmetic with $t$ digits of accuracy,the approximate condition number for the matrix $A$ is the norm of the matrix times the norm of the approximation to the inverse of $A$ ,which is obtained using $t$ -digit arithmetic.In fact,this condition number also depends on the method used to calculate the inverse of $A$

If we assume that the approximate solution to the linear system $A \mathbf { x } \ = \ \mathbf { b }$ is being determined using $t$ -digit arithmetic and Gaussian elimination, it can be shown (see [FM, pp. 45-47]) that the residual vector r for the approximation $\tilde { \mathbf { x } }$ has

$$
\lVert \mathbf { r } \rVert \approx 1 0 ^ { - t } \lVert A \rVert \cdot \lVert \tilde { \mathbf { x } } \rVert .
$$

From this approximation,an estimate for the effective condition number in $t$ -digit arithmetic can be obtained without having to invert the matrix $A$ . In actuality,this approximation assumes that all the arithmetic operations in the Gaussian elimination technique are performed using $t$ -digit arithmetic but that the operations needed to determine the residual are done in double-precision (that is, $2 t$ -digit) arithmetic. This technique does not add significantly to the computational effort and eliminates much of the loss of accuracy involved with the subtraction of the nearly equal numbers that occur in the calculation of the residual.

The approximation for the $t$ -digit condition number $K ( A )$ comes from consideration of the linear system

$$
A \mathbf { y } = \mathbf { r } .
$$

The solution to this system can be readily approximated since the multipliers for the Gaussian elimination method have already been calculated. In fact $\tilde { \mathbf { y } }$ ,the approximate solution of $A \mathbf { y } = \mathbf { r }$ ,satisfies

$$
\tilde { \mathbf { y } } \approx A ^ { - 1 } \mathbf { r } = A ^ { - 1 } ( \mathbf { b } - A \tilde { \mathbf { x } } ) = A ^ { - 1 } \mathbf { b } - A ^ { - 1 } A \tilde { \mathbf { x } } = \mathbf { x } - \tilde { \mathbf { x } } ;
$$

and

$$
\begin{array} { r } { \mathbf { x } \approx \tilde { \mathbf { x } } + \tilde { \mathbf { y } } . } \end{array}
$$

So $\tilde { \mathbf { y } }$ is an estimate of the error produced when $\tilde { \mathbf { x } }$ approximates the solution $\mathbf { X }$ to the original system. Equations (7.20) and (7.21) imply that

$$
| { \tilde { \mathbf { y } } } \| \approx \| \mathbf { x } - { \tilde { \mathbf { x } } } \| = \| A ^ { - 1 } \mathbf { r } \| \leq \| A ^ { - 1 } \| \cdot \| \mathbf { r } \| \approx \| A ^ { - 1 } \| \left( 1 0 ^ { - t } \| A \| \cdot \| { \tilde { \mathbf { x } } } \| \right) = 1 0 ^ { - t } \| { \tilde { \mathbf { x } } } \| K ( A ) ,
$$

This gives an approximation for the condition number involved with solving the system $A \mathbf { x } = \mathbf { b }$ using Gaussian elimination and the $t$ -digit type of arithmetic just described:

$$
K ( A ) \approx \frac { \| \tilde { \mathbf { y } } \| } { \| \tilde { \mathbf { x } } \| } 1 0 ^ { t } .
$$

# EXAMPLE 3

The linear system given by

$$
\left[ { \begin{array} { c c c } { 3 . 3 3 3 0 } & { 1 5 9 2 0 } & { - 1 0 . 3 3 3 } \\ { 2 . 2 2 2 0 } & { 1 6 . 7 1 0 } & { 9 . 6 1 2 0 } \\ { 1 . 5 6 1 1 } & { 5 . 1 7 9 1 } & { 1 . 6 8 5 2 } \end{array} } \right] \left[ { \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } \right] = \left[ { \begin{array} { c } { 1 5 9 1 3 } \\ { 2 8 . 5 4 4 } \\ { 8 . 4 2 5 4 } \end{array} } \right]
$$

has the exact solution $\mathbf { x } = ( 1 , 1 , 1 ) ^ { t }$

Using Gaussian elimination and five-digit rounding arithmetic leads successively to the augmented matrices

$$
\left[ { \begin{array} { r r r r r } { 3 . 3 3 3 0 } & { 1 5 9 2 0 } & { - 1 0 . 3 3 3 } & { \colon } & { 1 5 9 1 3 } \\ { 0 } & { - 1 0 5 9 6 } & { 1 6 . 5 0 1 } & { \colon } & { 1 0 5 8 0 } \\ { 0 } & { - 7 4 5 1 . 4 } & { 6 . 5 2 5 0 } & { \colon - 7 4 4 4 . 9 } \end{array} } \right]
$$

and

$$
\left[ { \begin{array} { c c c c } { 3 . 3 3 3 0 } & { 1 5 9 2 0 } & { - 1 0 . 3 3 3 } & { \colon } & { 1 5 9 1 3 } \\ { 0 } & { - 1 0 5 9 6 } & { 1 6 . 5 0 1 } & { \vdots } & { - 1 0 5 8 0 } \\ { 0 } & { 0 } & { - 5 . 0 7 9 0 } & { \vdots } & { - 4 . 7 0 0 0 } \end{array} } \right] .
$$

The approximate solution to this system is

$$
\tilde { \mathbf { x } } = ( 1 . 2 0 0 1 , 0 . 9 9 9 9 1 , 0 . 9 2 5 3 8 ) ^ { t } .
$$

The residual vector corresponding to $\tilde { \mathbf { x } }$ is computed in double precision to be

$$
\begin{array} { r l } & { \mathbf { r } = \mathbf { b } - A \tilde { \mathbf { x } } } \\ & { \quad = \left[ \begin{array} { l } { 1 5 9 1 3 } \\ { 2 8 . 5 4 4 } \\ { 8 . 4 2 5 4 } \end{array} \right] - \left[ \begin{array} { l l l } { 3 . 3 3 3 0 } & { 1 5 9 2 0 } & { - 1 0 . 3 3 3 } \\ { 2 . 2 2 2 0 } & { 1 6 . 7 1 0 } & { 9 . 6 1 2 0 } \\ { 1 . 5 6 1 1 } & { 5 . 1 7 9 1 } & { 1 . 6 8 5 2 } \end{array} \right] \left[ \begin{array} { l } { 1 . 2 0 0 1 } \\ { 0 . 9 9 9 9 1 } \\ { 0 . 9 2 5 3 8 } \end{array} \right] } \\ & { \quad = \left[ \begin{array} { l } { 1 5 9 1 3 } \\ { 2 8 . 5 4 4 } \\ { 8 . 4 2 5 4 } \end{array} \right] - \left[ \begin{array} { l } { 1 5 9 1 3 . 0 0 5 1 8 } \\ { 2 8 . 2 6 9 8 7 0 8 6 } \\ { 8 . 6 1 1 5 6 0 3 6 7 } \end{array} \right] = \left[ \begin{array} { l } { - 0 . 0 0 5 1 8 } \\ { 0 . 2 7 4 1 2 9 1 4 } \\ { - 0 . 1 8 6 1 6 0 3 6 7 } \end{array} \right] , } \end{array}
$$

So

$$
\| \mathbf { r } \| _ { \infty } = 0 . 2 7 4 1 3 .
$$

The estimate for the condition number given in the preceding discussion is obtained by first solving the system $A \mathbf { y } = \mathbf { r }$ for $\tilde { \bf y }$ ：

$$
\left[ { \begin{array} { r r r r } { 3 . 3 3 3 0 } & { 1 5 9 2 0 } & { - 1 0 . 3 3 3 } \\ { 2 . 2 2 2 0 } & { 1 6 . 7 1 0 } & { 9 . 6 1 2 0 } \\ { 1 . 5 6 1 1 } & { 5 . 1 7 9 1 } & { 1 . 6 8 5 2 } \end{array} } \right] { \left[ \begin{array} { r } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right] } = \left[ { \begin{array} { r } { - 0 . 0 0 5 1 8 } \\ { 0 . 2 7 4 1 3 } \\ { - 0 . 1 8 6 1 6 } \end{array} } \right] .
$$

This implies that $\tilde { \textbf { y } } = ~ ( - 0 . 2 0 0 0 8 , 8 . 9 9 8 7 \times 1 0 ^ { - 5 } , 0 . 0 7 4 6 0 7 ) ^ { t }$ . Using the estimate in Eq. (7.22) gives

$$
K ( A ) \approx 1 0 ^ { 5 } \frac { | | \tilde { \mathbf { y } } | | _ { \infty } } { | | \tilde { \mathbf { x } } | | _ { \infty } } = \frac { 1 0 ^ { 5 } ( 0 . 2 0 0 0 8 ) } { 1 . 2 0 0 1 } = 1 6 6 7 2 .
$$

To determine the exact condition number of $A$ , we first must construct $A ^ { - 1 }$ . Using five-digit rounding arithmetic for the calculations gives the approximation:

$$
A ^ { - 1 } = \left[ \begin{array} { c c c c } { { - 1 . 1 7 0 1 \times 1 0 ^ { - 4 } } } & { { - 1 . 4 9 8 3 \times 1 0 ^ { - 1 } } } & { { 8 . 5 4 1 6 \times 1 0 ^ { - 1 } } } \\ { { 6 . 2 7 8 2 \times 1 0 ^ { - 5 } } } & { { 1 . 2 1 2 4 \times 1 0 ^ { - 4 } } } & { { - 3 . 0 6 6 2 \times 1 0 ^ { - 4 } } } \\ { { - 8 . 6 6 3 1 \times 1 0 ^ { - 5 } } } & { { 1 . 3 8 4 6 \times 1 0 ^ { - 1 } } } & { { - 1 . 9 6 8 9 \times 1 0 ^ { - 1 } } } \end{array} \right] .
$$

Theorem 7.11 implies that $\| A ^ { - 1 } \| _ { \infty } = 1 . 0 0 4 1$ and $\| A \| _ { \infty } = 1 5 9 3 4$

As a consequence, the ill-conditioned matrix $A$ has

$$
K ( A ) = ( 1 . 0 0 4 1 ) ( 1 5 9 3 4 ) = 1 5 9 9 9 .
$$

The estimate in (7.23) is quite close to $K ( A )$ and requires considerably less computational effort.

Since the actual solution $\mathbf { x } = ( 1 , 1 , 1 ) ^ { t }$ is known for this system, we can calculate both

$$
\| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } = 0 . 2 0 0 1 \quad \mathrm { a n d } \quad \frac { \| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } } { \| \mathbf { x } \| _ { \infty } } = \frac { 0 . 2 0 0 1 } { 1 } = 0 . 2 0 0 1 .
$$

The error bounds given in Theorem 7.27 for these values are

$$
\| \mathbf { x } - { \tilde { \mathbf { x } } } \| _ { \infty } \leq K ( A ) { \frac { \| \mathbf { r } \| _ { \infty } } { \| A \| _ { \infty } } } = { \frac { ( 1 5 9 9 9 ) ( 0 . 2 7 4 1 3 ) } { 1 5 9 3 4 } } = 0 . 2 7 5 2 5
$$

and

$$
{ \frac { \| \mathbf { x } - { \tilde { \mathbf { x } } } \| _ { \infty } } { \| \mathbf { x } \| _ { \infty } } } \leq K ( A ) { \frac { \| \mathbf { r } \| _ { \infty } } { \| \mathbf { b } \| _ { \infty } } } = { \frac { ( 1 5 9 9 9 ) ( 0 . 2 7 4 1 3 ) } { 1 5 9 1 3 } } = 0 . 2 7 5 6 1 .
$$

In Eq. (7.21), we used the estimate $\tilde { \mathbf { y } } \approx \mathbf { x } - \tilde { \mathbf { x } } ,$ where $\tilde { \mathbf { y } }$ is the approximate solution to the system $A \mathbf { y } = \mathbf { r }$ . In general, $\tilde { \mathbf { x } } + \tilde { \mathbf { y } }$ is a more accurate approximation to the solution of the linear system $A \mathbf { x } = \mathbf { b }$ than the original approximation $\tilde { \mathbf { x } }$ .The method using this assumption is called iterative refinement, or iterative improvement, and consists of performing iterations on the system whose right-hand side is the residual vector for successive approximations until satisfactory accuracy results.

If the process is applied using $t$ -digit arithmetic and if $K _ { \infty } ( A ) \approx 1 0 ^ { q }$ , then after $k$ iterations of iterative refinement the solution has approximately the smaller of $t$ and $k ( t { - } q )$ correct digits. If the system is well-conditioned,one or two iterations will indicate that the solution is accurate. There is the possibility of significant improvement on ill-conditioned systems unless the matrix $A$ is so ill-conditioned that $K _ { \infty } ( A ) \ > \ 1 0 ^ { t }$ . In that situation, increased precision should be used for the calculations.

Algorithm 7.4 implements the Iterative Refinement technique.

# Iterative Refinement

To approximate the solution to the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ ：

INPUT the number of equations and unknowns $\pmb { n }$ ; the entries $a _ { i j } , 1 \le i , j \le n$ of the matrix $A$ ; the entries $b _ { i }$ ， $1 \leq i \leq n$ of $\mathbf { b }$ ; the maximum number of iterations $N$ ; tolerance TOL; number of digits of precision $t$ ·

OUTPUT the approximation $\mathbf { x x } = ( x x _ { i } , \ldots , x x _ { n } ) ^ { t }$ or a message that the number of iterations was exceeded,and an approximation COND to $K _ { \infty } ( A )$ ·

Step O Solve the system $\pmb { A } \mathbf { x } = \mathbf { b }$ for $x _ { 1 } , \ldots , x _ { n }$ by Gaussian elimination saving the multipliers $m _ { j i } , j = i + 1 , i + 2 , \ldots , n , i = 1 , 2 , \ldots , n - 1$ and noting row interchanges.

Step 1 Set $k = 1$

Step 2 While $( k \leq N )$ do Steps 3-9.

Step 3For $i = 1 , 2 , \dots , n$ (Calculate r.)

$$
\sec r _ { i } = b _ { i } - \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } .
$$

(Perform the computations in double-precision arithmetic.)

Step 4 Solve the linear system $\boldsymbol { A } \mathbf { y } = \mathbf { r }$ by using Gaussian elimination in the same order as in Step 0.

Step 5For $i = 1$ ,... ,n set $x x _ { i } = x _ { i } + y _ { i }$

Step $6$ If $k = 1$ then set $C O N D = \frac { \| \mathbf { y } \| _ { \infty } } { \| \mathbf { x x } \| _ { \infty } } 1 0 ^ { t } .$

Step 7 If $\| \mathbf { x } - \mathbf { x x } \| _ { \infty } < T O L$ then OUTPUT $\mathbf { \Psi } ( \mathbf { x x } )$ ； OUTPUT (COND); (The procedure was successful.) STOP.

Step 8 Set $k = k + 1$

Step 9 Fori = 1,...,n set $x _ { i } = x x _ { i }$

Step 10OUTPUT(Maximum number of iterations exceeded'); OUTPUT (COND); (The procedure was unsuccessful.) STOP.

If $t$ -digit arithmetic is used, a recommended stopping procedure in Step 7 is to iterate until $| y _ { i } ^ { ( k ) } | \leq 1 0 ^ { - t }$ , for each $i = 1 , 2 , \dots , n$

# EXAMPLE 4

In Example 3 we found the approximation to the problem we have been considering, using five-digit arithmetic and Gaussian elimination, to be

$$
\tilde { \mathbf { x } } ^ { ( 1 ) } = ( 1 . 2 0 0 1 , 0 . 9 9 9 9 1 , 0 . 9 2 5 3 8 ) ^ { t }
$$

and the solution to $\mathbf { A } \mathbf { y } = \mathbf { r } ^ { ( 1 ) }$ to be

$$
\tilde { \mathbf { y } } ^ { ( 1 ) } = ( - 0 . 2 0 0 0 8 , 8 . 9 9 8 7 \times 1 0 ^ { - 5 } , 0 . 0 7 4 6 0 7 ) ^ { t } .
$$

By Step 5 in this algorithm,

$$
\tilde { \mathbf { x } } ^ { ( 2 ) } = \tilde { \mathbf { x } } ^ { ( 1 ) } + \tilde { \mathbf { y } } ^ { ( 1 ) } = ( 1 . 0 0 0 0 , 1 . 0 0 0 0 , 0 . 9 9 9 9 ) ^ { t } ,
$$

and the actual error in this approximation is

$$
\lVert { \bf x } - \tilde { { \bf x } } ^ { ( 2 ) } \rVert _ { \infty } = 1 \times 1 0 ^ { - 5 } .
$$

Using the suggested stopping technique for the algorithm, we compute $\mathbf { r } ^ { ( 2 ) } = \mathbf { b } - A \tilde { \mathbf { x } } ^ { ( 2 ) }$ and solve the system $A \mathbf { y } ^ { ( 2 ) } = \mathbf { r } ^ { ( 2 ) }$ , which gives

$$
\tilde { \mathbf { y } } ^ { ( 2 ) \prime } = ( 1 . 5 0 0 2 \times 1 0 ^ { - 9 } , 2 . 0 9 5 1 \times 1 0 ^ { - 1 0 } , 1 . 0 0 0 0 \times 1 0 ^ { - 5 } ) ^ { t } .
$$

Since $\| \tilde { \mathbf { y } } ^ { ( 2 ) } \| _ { \infty } \le 1 0 ^ { - 5 }$ , we conclude that

$$
\tilde { \mathbf { x } } ^ { ( 3 ) } = \tilde { \mathbf { x } } ^ { ( 2 ) } + \tilde { \mathbf { y } } ^ { ( 2 ) } = ( 1 . 0 0 0 0 , 1 . 0 0 0 0 , 1 . 0 0 0 0 ) ^ { t }
$$

is sufficiently accurate, which is certainly correct.

Throughout this section it has been assumed that in the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ ， $A$ and b can be represented exactly. Realistically, the entries $a _ { i j }$ and $b _ { j }$ will be altered or perturbed by an amount $\delta \boldsymbol { a } _ { i j }$ and $\delta b _ { j }$ , causing the linear system

$$
( A + \delta A ) \mathbf { x } = \mathbf { b } + \delta \mathbf { b }
$$

to be solved in place of $A \mathbf { x } = \mathbf { b }$ .Normally, if $\| \delta A \|$ and $\| \delta \mathbf { b } \|$ are small (on the order of $1 0 ^ { - t } )$ ,the $t$ -digit arithmetic should yield a solution $\tilde { \mathbf { x } }$ for which $\lVert \mathbf { x } - \tilde { \mathbf { x } } \rVert$ is correspondingly small. However, in the case of ill-conditioned systems,we have seen that even if $A$ and $\mathbf { b }$ are represented exactly, rounding errors can cause $| | \mathbf { x } - \tilde { \mathbf { x } } | |$ to be large. The following theorem relates the perturbations of linear systems to the condition number of a matrix. The proof of this result can be found in [Or2, p. 33].

Theorem 7.29 Suppose $A$ is nonsingular and

$$
\lVert \delta A \rVert < \frac { 1 } { \lVert A ^ { - 1 } \rVert } .
$$

The solution $\tilde { \mathbf { x } }$ to $( A + \delta A ) \tilde { \mathbf { x } } = \mathbf { b } + \delta \mathbf { b }$ approximates the solution $\mathbf { x }$ of $A \mathbf { x } = \mathbf { b }$ with the error estimate

$$
{ \frac { \| \mathbf { x } - { \tilde { \mathbf { x } } } \| } { \| \mathbf { x } \| } } \leq { \frac { K ( A ) \| A \| } { \| A \| - K ( A ) \| \delta A \| } } \left( { \frac { \| \delta \mathbf { b } \| } { \| \mathbf { b } \| } } + { \frac { \| \delta A \| } { \| A \| } } \right) .
$$

The estimate in inequality (7.24) states that if the matrix A is well-conditioned (that is, $K ( A )$ is not too large), then small changes in $A$ and b produce correspondingly small changes in the solution x. If,on the other hand, $A$ is ill-conditioned,then smallchangesin $A$ and b may produce large changes in $\mathbf { x }$

The theorem is independent of the particular numerical procedure used to solve $\pmb { A } \pmb { \mathrm { x } } =$ b. It can be shown, by means of a backward error analysis (see [Wil1] or [Wil2]), that if Gaussian elimination with pivoting is used to solve $A \mathbf { x } = \mathbf { b }$ in $t$ -digit arithmetic,the numerical solution $\tilde { \bf x }$ is the actual solution of a linear system:

$$
( A + \delta A ) \tilde { \mathbf { x } } = \mathbf { b } , \quad \mathrm { w h e r e \ } \| \delta A \| _ { \infty } \leq f ( n ) 1 0 ^ { 1 - t } \operatorname* { m a x } _ { i , j , k } | a _ { i j } ^ { ( k ) } | .
$$

Wilkinson found in practice that $f ( n ) \approx n$ and, at worst, $f ( n ) \leq 1 . 0 1 ( n ^ { 3 } + 3 n ^ { 2 } )$

# Exercise Set 7.4

1.Compute the condition numbers of the following matrices relative to $\| \cdot \| _ { \infty }$

$\begin{array} { r l } { \mathbf { a } . \ } & { \left[ \begin{array} { l l } { \frac { 1 } { 2 } } & { \frac { 1 } { 3 } } \\ { \frac { 1 } { 3 } } & { \frac { 1 } { 4 } } \end{array} \right] } \\ { \mathbf { c } . \ } & { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 1 . 0 0 0 0 1 } & { 2 } \end{array} \right] } \\ { \mathbf { e } . \ } & { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { - 1 } \\ { 0 } & { 1 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } \end{array} \right] } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \ } & { \left[ \begin{array} { l l } { 3 . 9 } & { 1 . 6 } \\ { 6 . 8 } & { 2 . 9 } \end{array} \right] } \\ { \mathbf { d } . \ } & { \left[ \begin{array} { l l l } { 1 . 0 0 3 } & { 5 8 . 0 9 } \\ { 5 . 5 5 0 } & { 3 2 1 . 8 } \end{array} \right] } \\ { \mathbf { f } . \ } & { \left[ \begin{array} { l l l } { 0 . 0 4 } & { 0 . 0 1 } & { - 0 . 0 1 } \\ { 0 . 2 } & { 0 . 5 } & { - 0 . 2 } \\ { 1 } & { 2 } & { 3 } \end{array} \right] } \end{array}$

2. The following linear systems $\pmb { A } \pmb { \mathrm { x } } = \pmb { \mathrm { b } }$ have $\mathbf { x }$ as the actual solution and $\tilde { \mathbf { x } }$ as_ an approximate solution. Usingtheresults ofExercise1,compute $\| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty }$ and $K _ { \infty } ( A ) \frac { \| \boldsymbol { \mathsf { b } } - \boldsymbol { A } \tilde { \mathbf { x } } \| _ { \infty } } { \| \boldsymbol { A } \| _ { \infty } }$ ·

a. ${ \begin{array} { r l } & { { \frac { 1 } { 2 } } x _ { 1 } + { \frac { 1 } { 3 } } x _ { 2 } = { \frac { 1 } { 6 3 } } , } \\ & { { \frac { 1 } { 3 } } x _ { 1 } + { \frac { 1 } { 4 } } x _ { 2 } = { \frac { 1 } { 1 6 8 } } , } \\ & { \mathbf { x } = \left( { \frac { 1 } { 7 } } , - { \frac { 1 } { 6 } } \right) ^ { t } , } \end{array} }$ $\tilde { \mathbf { x } } = ( 0 . 1 4 2 , - 0 . 1 6 6 ) ^ { t } .$

$$
\begin{array} { r l } & { 3 . 9 x _ { 1 } + 1 . 6 x _ { 2 } = 5 . 5 , } \\ & { 6 . 8 x _ { 1 } + 2 . 9 x _ { 2 } = 9 . 7 , } \\ & { \mathbf { x } = ( 1 , 1 ) ^ { t } , } \\ & { \tilde { \mathbf { x } } = ( 0 . 9 8 , 1 . 1 ) ^ { t } . } \end{array}
$$

c. $x _ { 1 } + 2 x _ { 2 } = 3 ,$ $1 . 0 0 0 1 x _ { 1 } + 2 x _ { 2 } = 3 . 0 0 0 1 ,$ $\mathbf { x } = ( 1 , 1 ) ^ { \iota }$ ，$\tilde { \mathbf { x } } = ( 0 . 9 6 , 1 . 0 2 ) ^ { t } .$

d. $1 . 0 0 3 x _ { 1 } + 5 8 . 0 9 x _ { 2 } = 6 8 . 1 2$ $5 . 5 5 0 x _ { 1 } + 3 2 1 . 8 x _ { 2 } = 3 7 7 . 3$ ，$\mathbf { x } = ( 1 0 , 1 ) ^ { t }$ ，$\tilde { \mathbf { x } } = ( - 1 0 , 1 ) ^ { t }$

$$
\begin{array} { c } { { . \begin{array} { r l } { { x _ { 1 } - x _ { 2 } - x _ { 3 } = 2 \pi , } } \\ { { x _ { 2 } - x _ { 3 } = 0 , } } \\ { { - x _ { 3 } = \pi . } } \end{array} } } \end{array}
$$

$$
\begin{array} { l } { { { \bf x } = ( 0 , - \pi , - \pi ) ^ { t } , } } \\ { { \tilde { \bf x } = ( - 0 . 1 , - 3 . 1 5 , - 3 . 1 4 ) ^ { t } . } } \end{array}
$$

3. The linear system

f. $0 . 0 4 x _ { 1 } + 0 . 0 1 x _ { 2 } - 0 . 0 1 x _ { 3 } = 0 . 0 6 ,$ $\begin{array} { r l } { 0 . 2 x _ { 1 } + } & { { } 0 . 5 x _ { 2 } - } \\ { x _ { 1 } + } & { { } 2 x _ { 2 } + } \end{array} \quad 4 x _ { 3 } = 0 . 3 ,$ $\begin{array} { r l } & { \mathbf { x } = ( 1 . 8 2 7 5 8 6 , 0 . 6 5 5 1 7 2 4 , 1 . 9 6 5 5 1 7 ) ^ { t } , } \\ & { \tilde { \mathbf { x } } = ( 1 . 8 , 0 . 6 4 , 1 . 9 ) ^ { t } . } \end{array}$

$$
 \begin{array} { r l } { \left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 1 } & { 2 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l } { 3 } \\ { 3 . 0 0 0 1 } \end{array} \right] } \end{array}
$$

has solution $( 1 , 1 ) ^ { t }$ . Change $\pmb { A }$ slightly to

$$
\left[ { \begin{array} { c c } { 1 } & { 2 } \\ { 0 . 9 9 9 9 } & { 2 } \end{array} } \right] ,
$$

and consider the linear system

$$
\left[ \begin{array} { c c } { 1 } & { 2 } \\ { 0 . 9 9 9 9 } & { 2 } \end{array} \right] \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { 3 } \\ { 3 . 0 0 0 1 } \end{array} \right] .
$$

Compute the new solution using five-digit rounding arithmetic,and compare the actual error to the estimate (7.24). Is $\pmb { A }$ ill-conditioned?

4. The linear system $\mathbf { A x } = \mathbf { b }$ given by

$$
\left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 0 1 } & { 2 } \end{array} \right] \left[ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { 3 } \\ { 3 . 0 0 0 0 1 } \end{array} \right]
$$

has solution $( \mathbb { 1 } , 1 ) ^ { t }$ . Use seven-digit rounding arithmetic to find the solution of the perturbed system

$$
\begin{array} { r } { \left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 0 1 1 } & { 2 } \end{array} \right] \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { 3 . 0 0 0 0 1 } \\ { 3 . 0 0 0 0 3 } \end{array} \right] , } \end{array}
$$

and compare the actual error to the estimate (7.24). Is A ill-conditioned?

5.a.Use single precision on a computer to solve the following linear system using the Gaus-sian Elimination with Backward Substitution Algorithm 6.1.

$$
{ \begin{array} { r } { { \frac { 1 } { 3 } } x _ { 1 } - { \frac { 1 } { 3 } } x _ { 2 } - { \frac { 1 } { 3 } } x _ { 3 } - { \frac { 1 } { 3 } } x _ { 4 } - { \frac { 1 } { 3 } } x _ { 5 } = 1 } \\ { { \frac { 1 } { 3 } } x _ { 2 } - { \frac { 1 } { 3 } } x _ { 3 } - { \frac { 1 } { 3 } } x _ { 4 } - { \frac { 1 } { 3 } } x _ { 5 } = 0 } \\ { { \frac { 1 } { 3 } } x _ { 3 } - { \frac { 1 } { 3 } } x _ { 4 } - { \frac { 1 } { 3 } } x _ { 5 } = - 1 } \\ { { \frac { 1 } { 3 } } x _ { 4 } - { \frac { 1 } { 3 } } x _ { 5 } = 2 } \\ { { \frac { 1 } { 3 } } x _ { 4 } - { \frac { 1 } { 3 } } x _ { 5 } = 2 } \\ { { \frac { 1 } { 3 } } x _ { 5 } = 7 } \end{array} }
$$

b.Compute the condition number of the matrix for the system relative to $\| \cdot \| _ { \infty }$ c.Find the exact solution to the linear system.

6. The $n \times n$ Hilbert matrix $H ^ { ( n ) }$ defined by

$$
H _ { i j } ^ { ( n ) } = \frac { 1 } { i + j - 1 } , \quad 1 \le i , j \le n ,
$$

is an ill-conditioned matrix that arises in solving the normal equations for the coeficients of the least-squares polynomial (see Example 1 of Section 8.2).

a. Show that

$$
[ H ^ { ( 4 ) } ] ^ { - 1 } = \left[ { \begin{array} { r r r r } { 1 6 } & { - 1 2 0 } & { 2 4 0 } & { - 1 4 0 } \\ { - 1 2 0 } & { 1 2 0 0 } & { - 2 7 0 0 } & { 1 6 8 0 } \\ { 2 4 0 } & { - 2 7 0 0 } & { 6 4 8 0 } & { - 4 2 0 0 } \\ { - 1 4 0 } & { 1 6 8 0 } & { - 4 2 0 0 } & { 2 8 0 0 } \end{array} } \right] ,
$$

and compute $K _ { \infty } ( H ^ { ( 4 ) } )$ ·

b. Show that

$$
[ H ^ { ( 5 ) } ] ^ { - 1 } = \left[ \begin{array} { r r r r r r } { { 2 5 } } & { { - 3 0 0 } } & { { 1 0 5 0 } } & { { - 1 4 0 0 } } & { { 6 3 0 } } \\ { { - 3 0 0 } } & { { 4 8 0 0 } } & { { - 1 8 9 0 0 } } & { { 2 6 8 8 0 } } & { { - 1 2 6 0 0 } } \\ { { 1 0 5 0 } } & { { - 1 8 9 0 0 } } & { { 7 9 3 8 0 } } & { { - 1 1 7 6 0 0 } } & { { 5 6 7 0 0 } } \\ { { - 1 4 0 0 } } & { { 2 6 8 8 0 } } & { { - 1 1 7 6 0 0 } } & { { 1 7 9 2 0 0 } } & { { - 8 8 2 0 0 } } \\ { { 6 3 0 } } & { { - 1 2 6 0 0 } } & { { 5 6 7 0 0 } } & { { - 8 8 2 0 0 } } & { { 4 4 1 0 0 } } \end{array} \right] ,
$$

and compute $K _ { \infty } ( H ^ { ( 5 ) } )$

c. Solve the linear system

$$
H ^ { ( 4 ) } \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right] = \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \\ { 1 } \end{array} \right]
$$

using five-digit rounding arithmetic,and compare the actual error to that estimated in (7.24).

7. Show that if $\pmb { B }$ is singular, then

$$
{ \frac { 1 } { K ( A ) } } \leq { \frac { | | A - B | | } { | | A | | } } .
$$

[Hint: There exists a vector with $| | \mathbf { x } | | = 1$ ， such that $B \mathbf { x } \ = \ \mathbf { 0 }$ . Derive the estimate using $\lvert \lvert A \mathbf { x } \rvert \rvert \geq \lvert \lvert \mathbf { x } \rvert \rvert / \lvert \lvert A ^ { - 1 } \rvert \rvert . \rvert$

8.Using Exercise 7,estimate the condition numbers for the following matrices:

$\left[ \begin{array} { c c } { 1 } & { 2 } \\ { 1 . 0 0 0 1 } & { 2 } \end{array} \right]$ ${ \begin{array} { r l } { \mathbf { b } . \ } & { { } { \left[ \begin{array} { l l } { 3 . 9 } & { \ 1 . 6 } \\ { 6 . 8 } & { \ 2 . 9 } \end{array} \right] } } \end{array} }$

9. Use four-digit rounding arithmetic to compute the inverse $H ^ { - 1 }$ of the $3 \times 3$ Hilbert matrix $H$ ， and then compute $\hat { H } = ( H ^ { - 1 } ) ^ { - 1 }$ . Determine $| | H - { \hat { H } } | | _ { \infty }$

# 7.5 The Conjugate Gradient Method

The conjugate gradient method of Hestenes and Stiefel [HS] was originally developed as a direct method designed to solve an $n \times n$ positive definite linear system. As a direct method it is generally inferior to Gaussian elimination with pivoting since both methods require n steps to determine a solution, and the steps of the conjugate gradient method are more computationally expensive than those in Gaussian elimination.

However, the conjugate gradient method is very useful when employed as an itera-tive approximation method for solving large sparse systems with nonzero entries occurring in predictable patterns. These problems frequently arise in the solution of boundary-value problems. When the matrix has been preconditioned to make the calculations more effective, good results are obtained in only about $\sqrt { n }$ steps. Employed in this way, the method is preferred over Gaussan elimination and the previously-discussed iterative methods.

Throughout this section we assume that the matrix $A$ is positive definite. We will use the inner product notation

$$
\langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } \mathbf { y } ,
$$

where $\mathbf { x }$ and $\mathbf { y }$ are $n$ -dimensional vectors. We will also need some additional standard results from linear algebra. A review of this material is found in Section 9.1.

The next result folows easily from the properties of transposes (see Exercise 12).

# Theorem 7.30

For any vectors $\mathbf x , \mathbf y$ ,and $\mathbf { z }$ and any real number $\pmb { \alpha }$ , we have

(i） i） $\begin{array} { r l } & { \langle \mathbf { x } , \mathbf { y } \rangle = \langle \mathbf { y } , \mathbf { x } \rangle ; } \\ & { \langle \alpha \mathbf { x } , \mathbf { y } \rangle = \langle \mathbf { x } , \alpha \mathbf { y } \rangle = \alpha \langle \mathbf { x } , \mathbf { y } \rangle ; } \\ & { \langle \mathbf { x } + \mathbf { z } , \mathbf { y } \rangle = \langle \mathbf { x } , \mathbf { y } \rangle + \langle \mathbf { z } , \mathbf { y } \rangle ; } \\ & { \langle \mathbf { x } , \mathbf { x } \rangle \ge 0 ; } \end{array}$ (ii）   
(iv）   
（v） $\langle \mathbf { x } , \mathbf { x } \rangle = 0$ if and only if $\mathbf { x } = \mathbf { 0 }$

When $A$ is positive definite, $\langle { \bf x } , A { \bf x } \rangle = { \bf x } ^ { t } A { \bf x } > 0$ unless $\textbf { x } = \textbf { 0 }$ .Also, since $A$ is symmetric, we have $\mathbf { x } ^ { t } A \mathbf { y } = \mathbf { x } ^ { t } A ^ { t } \mathbf { y } = ( A \mathbf { x } ) ^ { t } \mathbf { y }$ ， so in addition to the results in Theorem 7.30, we have for each $\mathbf { X }$ and $\mathbf { y }$ ，

$$
\langle \mathbf { x } , A \mathbf { y } \rangle = \langle A \mathbf { x } , \mathbf { y } \rangle .
$$

The following result is a basic tool in the development of the conjugate gradient method.

The vector $\mathbf { x } ^ { \ast }$ is a solution to the positive definite linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ if and only if $\mathbf { x } ^ { * }$ minimizes

$$
g ( \mathbf { x } ) = \langle \mathbf { x } , A \mathbf { x } \rangle - 2 \langle \mathbf { x } , \mathbf { b } \rangle .
$$

Proof Let $\mathbf { x }$ and $\mathbf { v } \neq \mathbf { 0 }$ be fixed vectors and $t$ a real number variable. We have

$$
{ \begin{array} { r l } & { g ( \mathbf { x } + t \mathbf { v } ) = \langle \mathbf { x } + t \mathbf { v } , A \mathbf { x } + t A \mathbf { v } \rangle - 2 \langle \mathbf { x } + t \mathbf { v } , \mathbf { b } \rangle } \\ & { \qquad = \langle \mathbf { x } , A \mathbf { x } \rangle + t \langle \mathbf { v } , A \mathbf { x } \rangle + t \langle \mathbf { x } , A \mathbf { v } \rangle + t ^ { 2 } \langle \mathbf { v } , A \mathbf { v } \rangle - 2 \langle \mathbf { x } , \mathbf { b } \rangle - 2 t \langle \mathbf { v } , \mathbf { b } \rangle } \\ & { \qquad = \langle \mathbf { x } , A \mathbf { x } \rangle - 2 \langle \mathbf { x } , \mathbf { b } \rangle + 2 t \langle \mathbf { v } , A \mathbf { x } \rangle - 2 t \langle \mathbf { v } , \mathbf { b } \rangle + t ^ { 2 } \langle \mathbf { v } , A \mathbf { v } \rangle , } \end{array} }
$$

so

$$
g ( \mathbf { x } + t \mathbf { v } ) = g ( \mathbf { x } ) + 2 t \langle \mathbf { v } , A \mathbf { x } - \mathbf { b } \rangle + t ^ { 2 } \langle \mathbf { v } , A \mathbf { v } \rangle .
$$

Since $\mathbf { x }$ and $\mathbf { v }$ are fixed, we can define the quadratic function $h$ in $t$ by

$$
h ( t ) = g ( \mathbf { x } + t \mathbf { v } ) .
$$

Then $h$ assumes a minimal value when $h ^ { \prime } ( t ) = 0$ ,because its $t ^ { 2 }$ coefficient, $\langle \boldsymbol { \mathbf { v } } , A \boldsymbol { \mathbf { v } } \rangle$ ,is positive. Since

$$
h ^ { \prime } ( t ) = 2 \langle \mathbf { v } , A \mathbf { x } - \mathbf { b } \rangle + 2 t \langle \mathbf { v } , A \mathbf { v } \rangle ,
$$

the minimum occurs when

$$
\hat { t } = - \frac { \langle \mathbf { v } , A \mathbf { x } - \mathbf { b } \rangle } { \langle \mathbf { v } , A \mathbf { v } \rangle } = \frac { \langle \mathbf { v } , \mathbf { b } - A \mathbf { x } \rangle } { \langle \mathbf { v } , A \mathbf { v } \rangle } ,
$$

and,from Equation (7.27),

$$
\begin{array} { r l } & { h ( \hat { t } ) = g ( \mathbf x ) - 2 \frac { \langle \mathbf v , \mathbf b - A \mathbf x \rangle } { \langle \mathbf v , A \mathbf v \rangle } \langle \mathbf v , \mathbf b - A \mathbf x \rangle + \left( \frac { \langle \mathbf v , \mathbf b - A \mathbf x \rangle } { \langle \mathbf v , A \mathbf v \rangle } \right) ^ { 2 } \langle \mathbf v , A \mathbf v \rangle } \\ & { \quad \quad = g ( \mathbf x ) - \frac { \langle \mathbf v , \mathbf b - A \mathbf x \rangle ^ { 2 } } { \langle \mathbf v , A \mathbf v \rangle } . } \end{array}
$$

So, for any vector $\mathbf { v } \neq \mathbf { 0 }$ , we have $g ( \mathbf { x } + t \mathbf { \hat { v } } ) < g ( \mathbf { x } )$ unless $\langle \mathbf { v } , \mathbf { b } - A \mathbf { x } \rangle = 0$ , in which case $g ( \mathbf { x } ) = g ( \mathbf { x } + t \mathbf { \hat { v } } )$ . This is the basic result we need to prove Theorem 7.31.

Suppose $\mathbf { x } ^ { \ast }$ satisfies $A \mathbf { x } ^ { * } = \mathbf { b }$ . Then $\langle \mathbf { v } , \mathbf { b } - A \mathbf { x } ^ { * } \rangle = 0$ for any vector $\mathbf { v }$ and $g ( \mathbf { x } )$ cannot be made any smaller than $g ( \mathbf { x } ^ { * } )$ . Thus, $\mathbf { x } ^ { \ast }$ minimizes $\pmb { \mathscr { E } }$

On the other hand, suppose that $\mathbf { X } ^ { \ast }$ is a vector that minimizes $\pmb { g }$ . Then for any vector v, we have $g ( \mathbf { x } ^ { * } + \hat { t } \mathbf { v } ) \geq g ( \mathbf { x } ^ { * } )$ . Thus, $\langle \mathbf { v } , \mathbf { b } - A \mathbf { x } ^ { * } \rangle = 0$ . This implies that $\mathbf { b } - A \mathbf { x } ^ { * } = \mathbf { 0 }$ and, consequently,that $A \mathbf { x } ^ { * } = \mathbf { b }$ □ ■ ■

To begin the conjugate gradient method,we choose $\mathbf { x }$ ,an approximate solution to $\boldsymbol { A } \boldsymbol { \mathbf { x } } ^ { * } = \boldsymbol { \mathbf { b } }$ ,and $\mathbf { v } \neq \mathbf { 0 }$ , which gives a search direction in which to move away from $\mathbf { x }$ to improve the approximation. Let $\mathbf { r } = \mathbf { b } - A \mathbf { x }$ be the residual vector associated with $\mathbf { x }$ and

$$
t = { \frac { \langle \mathbf { v } , \mathbf { b } - A \mathbf { x } \rangle } { \langle \mathbf { v } , A \mathbf { v } \rangle } } = { \frac { \langle \mathbf { v } , \mathbf { r } \rangle } { \langle \mathbf { v } , A \mathbf { v } \rangle } } .
$$

f $\mathbf { r } \neq \mathbf { 0 }$ and if $\pmb { \nu }$ and $\pmb { \mathrm { r } }$ are not orthogonal, then $\mathbf { x } + t \mathbf { v } .$ gives a smaller value for $\pmb { g }$ than $g ( \mathbf { x } )$ and is presumably closer to $\mathbf { x } ^ { \ast }$ than is $\mathbf { x }$ . This suggests the following method.

Let $\mathbf { x } ^ { ( 0 ) }$ be an initial approximation to $\mathbf { X } ^ { \ast }$ , and let $\mathbf { v } ^ { ( 1 ) } \neq \mathbf { 0 }$ be an initial search direction. For $k = 1$ ,2,3.,..., we compute

$$
t _ { k } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } ,
$$

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) }
$$

and choose a new search direction $\mathbf { v } ^ { ( k + 1 ) }$ . The object is to make this selection so that the sequence of approximations $\{ \mathbf { x } ^ { ( k ) } \}$ converges rapidly to $\mathbf { x } ^ { * }$

To choose the search directions, we view $g$ as a function of the components of ${ \textbf { x } } =$ $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ . Thus,

$$
g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = \langle \mathbf { x } , A \mathbf { x } \rangle - 2 \langle \mathbf { x } , \mathbf { b } \rangle = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } a _ { i j } x _ { i } x _ { j } - 2 \sum _ { i = 1 } ^ { n } x _ { i } b _ { i } .
$$

Taking partial derivatives with respect to the component variables $x _ { k }$ gives

$$
{ \frac { \partial g } { \partial x _ { k } } } ( { \bf x } ) = 2 \sum _ { i = 1 } ^ { n } a _ { k i } x _ { i } - 2 b _ { k } .
$$

Therefore, the gradient of $g$ is

$$
\nabla g ( { \bf x } ) = \left( \frac { \partial g } { \partial x _ { 1 } } ( { \bf x } ) , \frac { \partial g } { \partial x _ { 2 } } ( { \bf x } ) , \ldots , \frac { \partial g } { \partial x _ { n } } ( { \bf x } ) \right) ^ { t } = 2 ( A { \bf x } - { \bf b } ) = - 2 { \bf r } ,
$$

where the vector r is the residual vector for $\mathbf { x }$

From multivariable calculus,we know that the direction of greatest decrease in the value of $g ( \mathbf { x } )$ is the direction given by $- \nabla g ( \mathbf { x } )$ ; that is, in the direction of the residual $\mathbf { r }$ The method that chooses

$$
\mathbf { v } ^ { ( k + 1 ) } = \mathbf { r } ^ { ( k ) } = \mathbf { b } - A \mathbf { x } ^ { ( k ) }
$$

is called the method of steepest descent. Although we will see in Section 10.4 that this method has merit for nonlinear systems and optimization problems,it is not used for linear systems because of slow convergence.

An alternative approach uses a set of nonzero direction vectors $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ that satisfy

$$
\langle \mathbf { v } ^ { ( i ) } , A \mathbf { v } ^ { ( j ) } \rangle = 0 , \quad \mathrm { i f } \quad i \neq j .
$$

This is called an A-orthogonality condition,and the set of vectors $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ is said to be A-orthogonal. It is not difficult to show that a set of $\pmb { A }$ -orthogonal vectors associated with the positive definite matrix $A$ is linearly independent. (See Exercise 13(a).） This set of search directions gives

$$
t _ { k } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle }
$$

and $\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) }$

The following theorem shows that this choice of search directions gives convergence in at most $\pmb { n }$ -steps,so as a direct method it produces the exact solution, assuming that the arithmetic is exact.

# Theorem 7.32

Let $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ be an $A$ -orthogonalset of nonzerovectrs assciated withthepositive definite matrix $A$ ,and let $\mathbf { x } ^ { ( 0 ) }$ be arbitrary. Define

$$
t _ { k } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) } ,
$$

for $k = 1 , 2 , \ldots , n$ . Then, assuming exact arithmetic, $\boldsymbol { A } \boldsymbol { \mathbf { x } } ^ { ( n ) } = \boldsymbol { \mathbf { b } }$

Proof Since,for each $k = 1 , 2 , \dots , n$

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) } ,
$$

we have

$$
\begin{array} { l } { A \mathbf { x } ^ { ( n ) } = A \mathbf { x } ^ { ( n - 1 ) } + t _ { n } A \mathbf { y } ^ { ( n ) } } \\ { \qquad = ( A \mathbf { x } ^ { ( n - 2 ) } + t _ { n - 1 } A \mathbf { v } ^ { ( n - 1 ) } ) + t _ { n } A \mathbf { v } ^ { ( n ) } } \\ { \qquad \vdots \qquad \vdots } \\ { \qquad \quad } \\ { = A \mathbf { x } ^ { ( 0 ) } + t _ { 1 } A \mathbf { v } ^ { ( 1 ) } + t _ { 2 } A \mathbf { v } ^ { ( 2 ) } + \cdot \cdot \cdot + t _ { n } A \mathbf { v } ^ { ( n ) } , } \end{array}
$$

and subtracting b from this result yields

$$
A \mathbf { x } ^ { ( n ) } - \mathbf { b } = A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } + t _ { 1 } A \mathbf { v } ^ { ( 1 ) } + t _ { 2 } A \mathbf { v } ^ { ( 2 ) } + \cdot \cdot \cdot + t _ { n } A \mathbf { v } ^ { ( n ) } .
$$

We now take the inner product of both sides with the vector $\mathbf { v } ^ { ( k ) }$ and use the properties of inner products and the fact that $A$ is symmetric to obtain

$$
\begin{array} { r } { \langle A \mathbf { x } ^ { ( n ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle + t _ { 1 } \langle A \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( k ) } \rangle + \cdot \cdot \cdot + t _ { n } \langle A \mathbf { v } ^ { ( n ) } , \mathbf { v } ^ { ( k ) } \rangle } \\ { = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle + t _ { 1 } \langle \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( k ) } \rangle + \cdot \cdot \cdot + t _ { n } \langle \mathbf { v } ^ { ( n ) } , A \mathbf { v } ^ { ( k ) } \rangle . } \end{array}
$$

The $A$ -orthogonality property gives,for each $k$ ，

$$
\langle A \mathbf { x } ^ { ( n ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle + t _ { k } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle .
$$

However,

$$
t _ { k } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } ,
$$

so

$$
\begin{array} { r l } & { t _ { k } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } \\ & { \qquad = \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } \\ & { \qquad = \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } + A \mathbf { x } ^ { ( 0 ) } - A \mathbf { x } ^ { ( 1 ) } + \cdots - A \mathbf { x } ^ { ( k - 2 ) } + A \mathbf { x } ^ { ( k - 2 ) } - A \mathbf { x } ^ { ( k - 1 ) } \rangle } \\ & { \qquad = \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } \rangle + \langle \mathbf { v } ^ { ( k ) } , A \mathbf { x } ^ { ( 0 ) } - A \mathbf { x } ^ { ( 1 ) } \rangle + \cdots + \langle \mathbf { v } ^ { ( k ) } , A \mathbf { x } ^ { ( k - 2 ) } - A \mathbf { x } ^ { ( k - 1 ) } \rangle . } \end{array}
$$

But for any $i$ ，

$$
\mathbf { x } ^ { ( i ) } = \mathbf { x } ^ { ( i - 1 ) } + t _ { i } \mathbf { v } ^ { ( i ) } \quad \mathrm { a n d } \quad A \mathbf { x } ^ { ( i ) } = A \mathbf { x } ^ { ( i - 1 ) } + t _ { i } A \mathbf { v } ^ { ( i ) } ,
$$

S0

$$
A \mathbf { x } ^ { ( i - 1 ) } - A \mathbf { x } ^ { ( i ) } = - t _ { i } A \mathbf { v } ^ { ( i ) } .
$$

Thus,

$$
t _ { k } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle = \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } \rangle - t _ { 1 } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( 1 ) } \rangle - \cdot \cdot \cdot - t _ { k - 1 } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k - 1 ) } \rangle .
$$

Because of the $A$ -orthogonality, $\langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( i ) } \rangle = 0$ ,for $i \neq k$ ,s0

$$
\langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle t _ { k } = \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } \rangle .
$$

From Eq.(7.28),

$$
\begin{array} { r l } & { \langle A \mathbf { x } ^ { ( n ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle + \langle \mathbf { v } ^ { ( k ) } , \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } \rangle } \\ & { \qquad = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle + \langle \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } , \mathbf { v } ^ { ( k ) } \rangle } \\ & { \qquad = \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle - \langle A \mathbf { x } ^ { ( 0 ) } - \mathbf { b } , \mathbf { v } ^ { ( k ) } \rangle } \\ & { \qquad = 0 . } \end{array}
$$

The vector $A \mathbf { x } ^ { ( n ) } \sim \mathbf { b }$ is orthogonal to the $\pmb { A }$ -orthogonal set of vectors $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ From this,it follows (see Exercise 13(b) that $A \mathbf { x } ^ { ( n ) } \lnot \mathbf { b } = \mathbf { 0 }$ □ ■

# EXAMPLE 1

Consider the positive definite matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} } \right] .
$$

Let $\mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ ， $\mathbf { v } ^ { ( 2 ) } = ( - 3 / 4 , 1 , 0 ) ^ { t }$ ,and $\mathbf { v } ^ { ( 3 ) } = ( - 3 / 7 , 4 / 7 , 1 ) ^ { t }$ . By direct calculation,

$$
\langle \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 2 ) } \rangle = \mathbf { v } ^ { ( 1 ) t } A \mathbf { v } ^ { ( 2 ) } = ( 1 , 0 , 0 ) { \left[ \begin{array} { l l l } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l } { - { \frac { 3 } { 4 } } } \\ { 1 } \\ { 0 } \end{array} \right] } = 0 ,
$$

$$
\langle \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 3 ) } \rangle = ( 1 , 0 , 0 ) \left[ { \begin{array} { r r r } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} } \right] \left[ { \begin{array} { r r } { - { \frac { 3 } { 7 } } } \\ { \frac { 4 } { 7 } } \\ { 1 } \end{array} } \right] = 0 ,
$$

and

$$
\langle \mathbf { v } ^ { ( 2 ) } , A \mathbf { v } ^ { ( 3 ) } \rangle = \left( - { \frac { 3 } { 4 } } , 1 , 0 \right) { \left[ \begin{array} { l l l } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l } { - { \frac { 3 } { 7 } } } \\ { { \frac { 4 } { 7 } } } \\ { 1 } \end{array} \right] } = 0 .
$$

Thus, $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } \}$ is an $\pmb { A }$ -orthogonal set.

The linear system

$$
{ \left[ \begin{array} { l l l } { 4 } & { 3 } & { 0 } \\ { 3 } & { 4 } & { - 1 } \\ { 0 } & { - 1 } & { 4 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 2 4 } \\ { 3 0 } \\ { - 2 4 } \end{array} \right] } ,
$$

has the exact solution $\mathbf { x } ^ { * } = ( 3 , 4 , - 5 ) ^ { t }$ . To approximate this solution, let $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ Since $\mathbf { b } = ( 2 4 , 3 0 , - 2 4 ) ^ { t }$ , we have

$$
\mathbf { r } ^ { ( 0 ) } = \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } = \mathbf { b } = ( 2 4 , 3 0 , - 2 4 ) ^ { t } ,
$$

so

$$
\langle { \bf v } ^ { ( 1 ) } , { \bf r } ^ { ( 0 ) } \rangle = { \bf v } ^ { ( 1 ) t } { \bf r } ^ { ( 0 ) } = 2 4 , \quad \langle { \bf v } ^ { ( 1 ) } , A { \bf v } ^ { ( 1 ) } \rangle = 4 , \quad \mathrm { a n d } \quad t _ { 0 } = \frac { 2 4 } { 4 } = 6 .
$$

Thus,

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + t _ { 0 } \mathbf { v } ^ { ( 1 ) } = ( 0 , 0 , 0 ) ^ { t } + 6 ( 1 , 0 , 0 ) ^ { t } = ( 6 , 0 , 0 ) ^ { t } .
$$

Continuing, we have

$$
{ \bf r } ^ { ( 1 ) } = { \bf b } - A { \bf x } ^ { ( 1 ) } = ( 0 , 1 2 , - 2 4 ) ^ { t } ; \quad t _ { 1 } = \frac { \langle { \bf v } ^ { ( 2 ) } , { \bf r } ^ { ( 1 ) } \rangle } { \langle { \bf v } ^ { ( 2 ) } , A { \bf v } ^ { ( 2 ) } \rangle } = \frac { 1 2 } { 7 / 4 } = \frac { 4 8 } { 7 } ;
$$

$$
\mathbf { x } ^ { ( 2 ) } = \mathbf { x } ^ { ( 1 ) } + t _ { 1 } \mathbf { v } ^ { ( 2 ) } = ( 6 , 0 , 0 ) ^ { t } + \frac { 4 8 } { 7 } \left( - \frac { 3 } { 4 } , 1 , 0 \right) ^ { t } = \left( \frac { 6 } { 7 } , \frac { 4 8 } { 7 } , 0 \right) ^ { t } ;
$$

$$
\mathbf { r } ^ { ( 2 ) } = \mathbf { b } - A \mathbf { x } ^ { ( 2 ) } = \left( 0 , 0 , - \frac { 1 2 0 } { 7 } \right) ; \quad t _ { 2 } = \frac { \langle \mathbf { v } ^ { ( 3 ) } , \mathbf { r } ^ { ( 2 ) } \rangle } { \langle \mathbf { v } ^ { ( 3 ) } , A \mathbf { v } ^ { ( 3 ) } \rangle } = \frac { - 1 2 0 / 7 } { 2 4 / 7 } = - 5 ;
$$

and

$$
\mathbf { x } ^ { ( 3 ) } = \mathbf { x } ^ { ( 2 ) } + t _ { 2 } \mathbf { v } ^ { ( 3 ) } = { \biggl ( } { \frac { 6 } { 7 } } , { \frac { 4 8 } { 7 } } , 0 { \biggr ) } ^ { t } + ( - 5 ) \left( - { \frac { 3 } { 7 } } , { \frac { 4 } { 7 } } , 1 \right) ^ { t } = ( 3 , 4 , - 5 ) ^ { t } .
$$

Since we applied the technique $n = 3$ times,this is the actual solution.

Before discussing how to determine the $A$ -orthogonal set, we will continue the devel-opment. The use of an $\pmb { A }$ -orthogonal set $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ of direction vectors gives what is called aconjugate direction method. The following theorem shows the orthogonality of the residual vectors $\mathbf { r } ^ { ( k ) }$ and the direction vectors $\mathbf { v } ^ { ( j ) }$ . A proof of this result using mathematical induction is considered in Exercise 14.

The residual vectors $\mathbf { r } ^ { ( k ) }$ , where $k = 1 , 2 , \ldots , n$ , for a conjugate direction method, satisfy the equations

$$
\langle \mathbf { r } ^ { ( k ) } , \mathbf { v } ^ { ( j ) } \rangle = 0 , \quad \mathrm { f o r e a c h } \quad j = 1 , 2 , \ldots , k .
$$

The conjugate gradient method of Hestenes and Stiefel chooses the search directions $\{ \mathbf { v } ^ { ( k ) } \}$ during the iterative process so that the residual vectors $\{ \mathbf { r } ^ { ( k ) } \}$ are mutually orthogonal. To construct the direction vectors $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \ldots \}$ and the approximations $\{ \mathbf { x } ^ { ( 1 ) } , \mathbf { x } ^ { ( 2 ) } , \ldots \} ,$ we start with an initial approximation $\mathbf { x } ^ { ( 0 ) }$ and use the steepest descent direction $\mathbf { r } ^ { ( 0 ) } =$ $\mathbf { b } - A \mathbf { x } ^ { ( 0 ) }$ as the first search direction $\mathbf { v } ^ { ( 1 ) }$

Assume that the conjugate directions $\mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( k - 1 ) }$ and the approximations $\mathbf { x } ^ { ( 1 ) }$ ， ：，, $\mathbf { x } ^ { ( k - 1 ) }$ have been computed with

$$
\mathbf { x } ^ { ( k - 1 ) } = \mathbf { x } ^ { ( k - 2 ) } + t _ { k - 1 } \mathbf { v } ^ { ( k - 1 ) } ,
$$

where

$$
\langle \mathbf { v } ^ { ( i ) } , A \mathbf { v } ^ { ( j ) } \rangle = 0 \quad \mathrm { a n d } \quad \langle \mathbf { r } ^ { ( i ) } , \mathbf { r } ^ { ( j ) } \rangle = 0 , \quad \mathrm { f o r } \quad i \neq j .
$$

If $\mathbf { x } ^ { ( k - 1 ) }$ is the solution to $\pmb { A } \mathbf { x } = \mathbf { b }$ ,we are done. Otherwise, $\mathbf { r } ^ { ( k - 1 ) } = \mathbf { b } - A \mathbf { x } ^ { ( k - 1 ) } \neq \mathbf { 0 }$ and Theorem 7.33 implies that $\langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { v } ^ { ( i ) } \rangle = 0$ ,for $i = 1 , 2 , \ldots , k - 1$ . We then use $\mathbf { r } ^ { ( k - 1 ) }$ to generate $\mathbf { v } ^ { ( k ) }$ by setting

$$
\mathbf { v } ^ { ( k ) } = \mathbf { r } ^ { ( k - 1 ) } + s _ { k - 1 } \mathbf { v } ^ { ( k - 1 ) } .
$$

We want to choose $s _ { k - 1 }$ so that

$$
\begin{array} { r } { \langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { v } ^ { ( k ) } \rangle = 0 . } \end{array}
$$

Since

$$
A \mathbf { v } ^ { ( k ) } = A \mathbf { r } ^ { ( k - 1 ) } + s _ { k - 1 } A \mathbf { v } ^ { ( k - 1 ) }
$$

and

$$
\langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { v } ^ { ( k ) } \rangle = \langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { r } ^ { ( k - 1 ) } \rangle + s _ { k - 1 } \langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { v } ^ { ( k - 1 ) } \rangle ,
$$

we will have $\langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { v } ^ { ( k ) } \rangle = 0$ when

$$
\begin{array} { r } { s _ { k - 1 } = - \frac { \langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k - 1 ) } , A \mathbf { v } ^ { ( k - 1 ) } \rangle } . } \end{array}
$$

It can also be shown that with this choice of $\pmb { S } _ { k - 1 }$ we have $\langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( i ) } \rangle ~ = ~ 0$ , for each $i = 1 , 2 , \ldots , k - 2$ (see [Lu, p. 245]). Thus, $\{ \mathbf { v } ^ { ( 1 ) } , \ldots \mathbf { v } ^ { ( k ) } \}$ is an $A$ -orthogonal set.

Having chosen $\mathbf { v } ^ { ( k ) }$ , we compute

$$
\begin{array} { r l } & { t _ { k } = \frac { \langle \mathbf { v } ^ { ( k ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } = \frac { \langle \mathbf { r } ^ { ( k - 1 ) } + s _ { k - 1 } \mathbf { v } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } } \\ & { \qquad = \frac { \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } + s _ { k - 1 } \frac { \langle \mathbf { v } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } . } \end{array}
$$

By Theorem 7.33, $\langle \mathbf { v } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle = 0$ s0

$$
t _ { k } = { \frac { \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } } .
$$