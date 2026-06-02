The least squares core problem is then

$$
\operatorname* { m i n } _ { y _ { 1 } } \| B _ { 1 1 } y _ { 1 } - \beta _ { 1 } e _ { 1 } \| _ { 2 } .
$$

The solution can be found effciently by a QR factorization of $B _ { 1 1 }$ .Proof that systems (4.2.16) and (4.2.18) are minimally dimensioned, and therefore core problems,is given by Paige and Strakos [868,20o6,Theorems 3.2 and 3.3].

# Notes and references

Core problems play an important role in a unified treatment of the scaled TLS (STLS) problem; see Paige and Strakos [867,2002],[868, 20o6]. Hnetynková et al. [630,2011] give a new clas-sification of multivariate TLS problems $A X \approx B$ that reveals subtleties not captured previously. The definition of the core problem is extended to the multiple right-hand side case $A X \approx B$ by Plesinger [899,20o8] and Hnetynkova, Plesinger, and Strakos [632,2013], [633, 2015].

# 4.2.3 - Golub-Kahan-Lanczos Bidiagonalization

When $A$ is large and sparse,Householder bidiagonalization is not effcient because any sparsity in $A$ is usually destroyed in the early intermediate steps. Golub and Kahan [495,1965l give an alternative algorithm that generates the elements in $B$ and the columns of $U$ and $V$ sequentially and only uses matrix-vector products with $A$ and $A ^ { T }$ . We call this algorithm Golub-Kahan-Lanczos bidiagonalization (GKLBD） because of its close relationship to symmetric Lanczos tridiagonalization of the symmetric matrix

$$
\left( \begin{array} { l l } { 0 } & { A } \\ { A ^ { T } } & { 0 } \end{array} \right)
$$

with special starting vectors.

By Theorem 4.2.1 it follows that the existence of orthogonal $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ is such that $U ^ { T } A V$ is upper or lower bidiagonal. Then we have

$$
\begin{array} { r l } & { A \left( \begin{array} { l } { v _ { 1 } , v _ { 2 } , v _ { 3 } , \ldots } \end{array} \right) = \left( \begin{array} { l l } { u _ { 1 } , u _ { 2 } , u _ { 3 } , \ldots } \end{array} \right) \left( \begin{array} { l l } { B } & { 0 } \\ { 0 } & { 0 } \end{array} \right) , } \\ & { A ^ { T } \left( \begin{array} { l l } { u _ { 1 } , u _ { 2 } , u _ { 3 } , \ldots } \end{array} \right) = \left( \begin{array} { l l } { v _ { 1 } , v _ { 2 } , v _ { 3 } , \ldots } \end{array} \right) \left( \begin{array} { l l } { B ^ { T } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) , } \end{array}
$$

where some of the zero blocks may be empty. Assume now that $B$ is lower bidiagonal,

$$
B = \left( \begin{array} { c c c c c } { { \alpha _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \beta _ { 2 } } } & { { \alpha _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \beta _ { 3 } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { \alpha _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { \beta _ { n + 1 } } } \end{array} \right) .
$$

Equating columns on both sides of equations (4.2.19)-(4.2.20) gives $\alpha _ { 1 } v _ { 1 } = A ^ { T } u _ { 1 }$ ，

$$
\begin{array} { l } { A v _ { k } = \beta _ { k + 1 } u _ { k + 1 } + \alpha _ { k } u _ { k } , } \\ { A ^ { T } u _ { k + 1 } = \alpha _ { k + 1 } v _ { k + 1 } + \beta _ { k + 1 } v _ { k } , \quad k = 1 , \ldots , n . } \end{array}
$$

Given an initial unit vector $u _ { 1 } \in \mathbb { R } ^ { m }$ , this yields an iterative process for generating $U$ and $V$ columnwise and $B$ rowwise from

$$
\begin{array} { l } { \beta _ { k + 1 } u _ { k + 1 } = A v _ { k } - \alpha _ { k } u _ { k } , } \\ { \alpha _ { k + 1 } v _ { k + 1 } = A ^ { T } u _ { k + 1 } - \beta _ { k + 1 } v _ { k } , \quad k = 1 , 2 , \ldots , } \end{array}
$$

where $\beta _ { k + 1 }$ and $\alpha _ { k + 1 }$ are normalization constants.As long as no zero bidiagonal element occurs, the choice of $u _ { 1 }$ uniquely determines this process. It terminates with a core subproblem when the first zero bidiagonal element is encountered. After $k$ steps the recurrence relations (4.2.23)- (4.2.24) can be summarized in matrix form as

$$
\begin{array} { l } { A V _ { k } = U _ { k + 1 } B _ { k } , } \\ { A ^ { T } U _ { k + 1 } = V _ { k } B _ { k } ^ { T } + \alpha _ { k + 1 } v _ { k + 1 } e _ { k + 1 } ^ { T } . } \end{array}
$$

The Bidiag1 algorithm of Paige and Saunders [866,1982] is obtained for the special starting vector

$$
u _ { 1 } = b / \beta _ { 1 } , \quad \beta _ { 1 } = \| b \| _ { 2 } .
$$

In exact arithmetic, it generates the same lower bidiagonal decomposition of $A$ as HHBD, transforming $\left( \begin{array} { l l } { b } & { A } \end{array} \right)$ into upper bidiagonal form.Bidiag1 is the basis of the important iterative least squares algorithm LSQR of Paige and Saunders [866,1982].

A similar GKLBD processcan be devisedfor the case when $U ^ { T } A V = R$ is upper bidiagonal,

$$
R = \left( \begin{array} { c c c c c c } { { \rho _ { 1 } } } & { { \gamma _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \rho _ { 2 } } } & { { \gamma _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \rho _ { 3 } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \ddots } } & { { \gamma _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \rho _ { n } } } \end{array} \right) .
$$

Given an initial unit vector $v _ { 1 } \in \mathbb { R } ^ { n }$ ,equating columns in(4.2.19)-(4.2.20)yields $A v _ { 1 } = \rho _ { 1 } u _ { 1 }$ ，

$$
\begin{array} { l } { { A ^ { T } u _ { k } = \rho _ { k } v _ { k } + \gamma _ { k + 1 } v _ { k + 1 } , } } \\ { { \ } } \\ { { A v _ { k } = \gamma _ { k } u _ { k - 1 } + \rho _ { k } u _ { k } , \quad k = 1 , 2 , \ldots , n - 1 . } } \end{array}
$$

These equations can be used to generate not only successive columns in $U$ and $V$ but also the columns of $R$ . As long as no zero bidiagonal element is encountered,we have

$$
\begin{array} { l } { \gamma _ { k + 1 } v _ { k + 1 } = A ^ { T } u _ { k } - \rho _ { k } v _ { k } , } \\ { \qquad } \\ { \rho _ { k + 1 } u _ { k + 1 } = A v _ { k + 1 } - \gamma _ { k + 1 } u _ { k } , \quad k = 1 , 2 , \ldots . } \end{array}
$$

These equations uniquely determine $v _ { k + 1 }$ and $u _ { k + 1 }$ as_ well as $\gamma _ { k + 1 }$ and $\rho _ { k + 1 }$ After $k$ steps this process has generated $U _ { k } \in \mathbb { R } ^ { m \times k }$ and $V _ { k } \in \mathbb { R } ^ { n \times k }$ and a square upper bidiagonal matrix $R _ { k } \in \mathbb { R } ^ { k \times k }$ such that

$$
\begin{array} { l } { { A V _ { k } = U _ { k } R _ { k } , } } \\ { { \ A ^ { T } U _ { k } = V _ { k } R _ { k } ^ { T } + \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } . } } \end{array}
$$

Taking the initial vector to be $v _ { 1 } = A ^ { T } b / \gamma _ { 1 }$ ， $\gamma _ { 1 } = \| A ^ { T } b \| _ { 2 }$ , gives the Bidiag2 algorithm of Paige and Saunders [866,1982]. In exact arithmetic, this generates the same quantities as HHBD, transforming $\left( A ^ { T } b \quad A ^ { T } \right)$ into upper bidiagonal form.

In finite-precision arithmetic there can be a severe loss of orthogonality in $U _ { k }$ and $V _ { k }$ computed by both forms of GKLBD. One effect is that the finite termination property of HHBD is lost; see Section 6.2.5.

# 4.2.4 - Bidiagonalization and Krylov Subspaces

GKLBD generates vectors by repeated matrix-vector products with a fixed matrix. Such vectors span subspaces of a particular structure called Krylov subspaces. Let $C \in \mathbb { R } ^ { n \times n }$ be a given square matrix,and let $v \in \mathbb { R } ^ { n }$ be a given nonzero vector. The sequence of vectors $v , C v , C ^ { 2 } v$ ， $C ^ { 3 } v , \ldots$ is called a Krylov sequence and is easily generated recursively by $v _ { 1 } = v$ ， $v _ { k } = C v _ { k - 1 }$ ， $k = 2 , 3 , \ldots .$ The subspace spanned by the frst $k$ vectors is called a Krylov subspace, denoted by

$$
{ \mathcal K } _ { k } ( C , v ) = \operatorname { s p a n } \{ v , C v , \ldots , C ^ { k - 1 } v \} .
$$

Such subspaces with $C = A ^ { T } A$ or $C = A A ^ { T }$ play a fundamental role in methods for solving large-scale least squares problems.

There can be at most $n$ linearly independent vectors in $\mathbb { R } ^ { n }$ . Hence,in any Krylov sequence $v , C v , C ^ { 2 } v , C ^ { 3 } v , \ldots$ there is a first vector ${ \cal C } ^ { p + 1 } v , p \le n$ ,that is a linear combination of the preceding ones.Then

$$
\begin{array} { r } { \mathcal { K } _ { p + 1 } ( C , v ) = \mathcal { K } _ { p } ( C , v ) , } \end{array}
$$

and the Krylov sequence terminates. The maximum dimension $p$ of $\mathcal { K } _ { k } ( C , v )$ is called the grade of $v$ with respect to $C$ .From (4.2.34) it follows that at termination, ${ \cal { K } } _ { p } ( C , v )$ is an invariant subspace of $C$ . Conversely, if the vector $v$ lies in an invariant subspace of $C$ of dimension $p$ ,its Krylov sequence terminates for $k = p$

Krylov subspaces satisfy the following easily verified invariance properties:

1. Scaling: $\mathcal { K } _ { m } ( \beta C , \alpha v ) = \mathcal { K } _ { m } ( C , v ) , \alpha \neq 0 , \beta \neq 0 .$

2. Translation: $\begin{array} { r } { \mathcal { K } _ { m } ( C - \mu I , v ) = \mathcal { K } _ { m } ( C , v ) . } \end{array}$ 3. Similarity: $\begin{array} { r } { \mathcal { K } _ { m } ( U ^ { H } C U , U ^ { H } v ) = U ^ { H } \mathcal { K } _ { m } ( C , v ) } \end{array}$ for any unitary matrix $U$

Theorem 4.2.3. As long as no zero bidiagonal element is encountered, the orthonormal vectors $( u _ { 1 } , \ldots , u _ { k } )$ and $( v _ { 1 } , \ldots , v _ { k } )$ generated by Bidiagl are bases for the Krylov subspaces

$$
\begin{array} { r } { \mathcal { R } ( U _ { k } ) = { \mathcal K } _ { k } ( A A ^ { T } , b ) , \qquad { \mathcal R } ( V _ { k } ) = { \mathcal K } _ { k } ( A ^ { T } A , A ^ { T } b ) , \quad k = 1 , 2 , \dots . } \end{array}
$$

Proof. We have $\beta _ { 1 } u _ { 1 } = b$ and $\alpha _ { 1 } v _ { 1 } = A ^ { T } u _ { 1 }$ If $\beta _ { 1 } \alpha _ { 1 } \neq 0$ ，then $( \beta _ { 1 } \alpha _ { 1 } ) v _ { 1 } = A ^ { T } b$ Hence (4.2.35) holds for $k = 1$ . Assume now that (4.2.35) is true for some $k \geq 1$ .If $\beta _ { k + 1 } \alpha _ { k + 1 } \neq 0$ ,it follows fr0m (4.2.23)-(4.2.24) that

$$
\begin{array} { r l } & { \mathcal { R } ( U _ { k + 1 } ) = \mathcal { R } ( U _ { k } ) \cup A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b ) = \mathcal { K } _ { k + 1 } ( A A ^ { T } , b ) , } \\ & { \mathcal { R } ( V _ { k + 1 } ) = \mathcal { R } ( V _ { k } ) \cup A ^ { T } \mathcal { K } _ { k } ( A A ^ { T } , b ) = \mathcal { K } _ { k + 1 } ( A ^ { T } A , A ^ { T } b ) . } \end{array}
$$

Hence (4.2.35) holds for $k + 1$ . The theorem now follows by induction in $k$

By Theorem 4.2.3 the matrices $U _ { k }$ and $V _ { k }$ can also be obtained by Gram-Schmidt orthogonalization of the Krylov sequences

$$
u _ { 1 } , A A ^ { T } u _ { 1 } , ( A A ^ { T } ) ^ { 2 } u _ { 1 } , \ldots , \qquad v _ { 1 } , A ^ { T } A v _ { 1 } , ( A ^ { T } A ) ^ { 2 } v _ { 1 } , \ldots .
$$

Hence, the uniqueness of the bases is a consequence of the uniqueness (up to a diagonal scaling with elements $\pm 1$ ) of the QR factorization of a real matrix of full column rank.

Bidiagl terminates for some $k \leq \mathrm { r a n k } ( A )$ when the subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have reached maximum rank. Then the subspaces

$$
\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) = A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )
$$

have also reached maximal rank. At termination the pseudoinverse solution $x _ { k } = V _ { k } y _ { k }$ is obtained for some $y _ { k } \in \mathbb { R } ^ { k }$ , where $\mathcal { R } ( V _ { k } ) = \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$

Bidiag2 terminates with $\beta _ { k + 1 } = 0$ for some $k \leq \mathrm { r a n k } ( A )$ when the subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have reached maximum rank. Then the subspaces $\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) = A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have also reached maximal rank. Bidiag2 generates vectors giving orthogonal bases for

$$
\begin{array} { r } { \mathcal { R } ( V _ { k } ) = \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b ) , \qquad \mathcal { R } ( U _ { k } ) = \mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) . } \end{array}
$$

Bidiagl and Bidiag2 generate the same $V _ { k }$ ,but $U _ { k }$ differs. The upper bidiagonal matrix $R _ { k }$ in Bidiag2 is the same as the matrix obtained by QR factorization of the lower bidiagonal $B _ { k }$ in Bidiagl; see Paige and Saunders [866,1982].

Collecting previous results we can now state the following.

Theorem 4.2.4 (Krylov Subspace Approximations). Let p be the grade of $A ^ { T } b$ with respect to $A ^ { T } A .$ Then the projected least squares problems

$$
\operatorname* { m i n } _ { \boldsymbol { x } _ { k } } \| A \boldsymbol { x } _ { k } - \boldsymbol { b } \| _ { 2 } ~ s u b j e c t ~ t o ~ \boldsymbol { x } _ { k } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } \boldsymbol { b } ) , \quad 1 \leq k \leq p ,
$$

have full rank. The solutions $x _ { k }$ are uniquely determined, and the residuals satisfy $r _ { k } = b -$ $A x _ { k } \perp \mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b )$ Independent of $b$ and the size or rank of $A$ ，the Krylov subspace approximations terminate with the pseudoinverse solution $x _ { p } = A ^ { \dagger } b$ for some $p \leq \mathrm { r a n k } ( A )$

From the nested property of the Krylov subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ ， $k = 1 , 2 , \dots$ , it follows that the sequence of residual norms $\| r _ { k } \| _ { 2 } , k = 1 , 2 , . . .$ ，are monotonically decreasing. For $k < p$ the Krylov subspace approximations depend nonlinearly on $b$ in a highly complicated way.

At termination,all bidiagonal elements in $B$ and $R$ of Bidiagl and Bidiag2 are positive. Such bidiagonal matrices are said to be unreduced and have the following property.

Lemma 4.2.5. For any unreduced bidiagonal matrix $B$ , all singular values $\sigma _ { i }$ must be distinct.

Proof. If $B$ is unreduced, then $T = B ^ { T } B$ is symmetric tridiagonal with positive off-diagonal elements $\gamma _ { i } = \rho _ { i } \gamma _ { i + 1 }$ . Such a tridiagonal matrix is also called unreduced and, by Parlett [884, 1998,Lemma 7.7.1], has distinct eigenvalues $\lambda _ { i }$ . The lemma now follows from the fact that $\lambda _ { i } = \sigma _ { i } ^ { 2 }$ □

Theorem 4.2.6. Let $A$ have p distinct, possibly multiple, nonzero singular values. Then,Bidiagl and Bidiag2 terminate with an unreduced bidiagonal matrix $B _ { k } = U _ { k } ^ { T } A V _ { k }$ of rank $k \leq p .$

Proof. Since $B _ { k }$ is unreduced, it follows from Lemma 4.2.5 that all its singular values must be distinct: $\sigma _ { 1 } > \sigma _ { 2 } > \cdot \cdot \cdot > \sigma _ { k } > 0$ .But these are also singular values of $A$ ，and hence $k \leq p$ □

Theorem 4.2.6 states that if $A$ has singular values of multiplicity greater than one,then Bidiagl and Bidiag2 terminate in less than $\operatorname { r a n k } ( A )$ steps. For example,let square $A = I _ { n } + u v ^ { T }$ ， $u , v \ne 0$ ，and $\operatorname { r a n k } ( A ) = n$ . The singular values of $A$ are the square roots of the eigenvalues of $A ^ { T } A = I _ { n } + u v ^ { T } + v u ^ { T } + ( u ^ { T } u ) v v ^ { T }$ $A ^ { T } A$ has one eigenvalue equal to 1 of multiplicity $( n - 2 )$ corresponding to eigenvectors $x$ that are orthogonal to $u$ and $v$ .Hence, $A$ has at most three distinct singular values,and, in exact arithmetic, bidiagonalization must terminate after at most three steps.

If $b$ is orthogonal to the left singular subspaces corresponding to some of the singular values, Bidiagl terminates in $k \leq p$ steps; see Bjorck [137, 2014,Lemma 2.1].

# 4.2.5 - Partial Least Squares Algorithms

The NIPALS (Nonlinear Iterative PArtial Least Squares) method was devised by H. Wold [1127, 1966] to model relations between sets of observed variables and a number of latent (not directly observed variables. Initially, the main applications were prediction and cause-effect inference in statistics and economics. S. Wold et al.[1128,1984] developed the recursive NIPALS-PLS algorithm for use in chemometrics and pointed out its equivalence to Krylov subspace approximations. Today, partial least squares (PLS) is a widely used multivariate regression technique with a broad spectrum of applications in research and industry, such as bioinformatics, food science, medicine, pharmacology, social sciences,and physiology; see Vinzi et al.[1093, 2010].

NIPALS-PLS. Set $A _ { 0 } = A$ ， $b _ { 0 } = b$ ,and for $k = 1 , 2 , \ldots$

$$
\begin{array} { r l } & { \hat { v } _ { k } = A _ { k - 1 } ^ { T } b _ { k - 1 } , \quad v _ { k } = \hat { v } _ { k } / \| \hat { v } _ { k } \| _ { 2 } , } \\ & { \hat { u } _ { k } = A _ { k - 1 } v _ { k } , \quad u _ { k } = \hat { u } _ { k } / \| \hat { u } _ { k } \| _ { 2 } , } \\ & { p _ { k } ^ { T } = u _ { k } ^ { T } A _ { k - 1 } , \quad \zeta _ { k } = u _ { k } ^ { T } b _ { k - 1 } , } \\ & { ( A _ { k } , b _ { k } ) = ( A _ { k - 1 } , b _ { k - 1 } ) - u _ { k } ( p _ { k } ^ { T } , \zeta _ { k } ) . } \end{array}
$$

The $k$ th PLS approximation is $x _ { k } = V _ { k } y _ { k }$ ,where $y _ { k }$ satisfies

$$
( P _ { k } ^ { T } V _ { k } ) y _ { k } = z _ { k } , \quad z _ { k } = ( \zeta , . . . , \zeta _ { k } ) ^ { T } ,
$$

$V _ { k } ~ = ~ ( v _ { 1 } , \ldots , v _ { k } )$ ， $U _ { k } \ = \ ( u _ { 1 } , \ldots , u _ { k } )$ ，and $P _ { k } = \left( p _ { 1 } , \ldots , p _ { k } \right)$ .Note that in (4.2.41） the orthogonal projections of $A _ { k - 1 }$ and $b _ { k - 1 }$ onto $u _ { k }$ are subtracted:

$$
( A _ { k } , b _ { k } ) = ( I - u _ { k } u _ { k } ^ { T } ) ( A _ { k - 1 } , b _ { k - 1 } ) .
$$

The process terminates when either $\| \hat { v } _ { k } \| _ { 2 }$ or $\| \hat { u } _ { k } \| _ { 2 }$ is zero. Note that if $u _ { k } ^ { T } A _ { k - 1 } v _ { k } \neq 0$ ,the rank of $A _ { k }$ is exactly one less than that of $A _ { k - 1 }$

In the PLS literature, $u _ { k }$ are called score vectors, $v _ { k }$ loading weights, and $p _ { k }$ loading vectors. Summing the equations in (4.2.41) gives

$$
A = U _ { k } P _ { k } ^ { T } + A _ { k } , \qquad b = U _ { k } z _ { k } ^ { T } + b _ { k } .
$$

Then $\begin{array} { r } { U _ { k } P _ { k } ^ { T } = \sum _ { i = 1 } ^ { k } u _ { i } p _ { i } ^ { T } } \end{array}$ is a rank $k$ approximation to te da atix $A$ . The data residuals are given by

$$
A _ { k } = A - U _ { k } P _ { k } ^ { T } = ( I - U _ { k } U _ { k } ^ { T } ) A .
$$

# Algorithm 4.2.1 (NIPALS-PLS Algorithm).

function [x,U,P,V] $=$ nipalspls(A,b,k)   
$\%$ NIPALSPLS computes the first $\mathtt { k }$ PLS factors for the   
$\%$ least squares problem min $| \mathbf { | } \mathbf { A x } \ \textrm { - } \mathbf { b } | \mathbf { | } \ \mathbf { - } 2$ ·   
$\%$ --- [m,n] = size(A)； U = zeros(m,k); $\begin{array} { r l } { \texttt { V } = } \end{array}$ zeros $( \mathtt { n } , \mathtt { k } )$ ； $\mathrm { ~ \mathsf ~ { ~ P ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ V ~ } ~ }$ ； $_ z =$ zeros(k,1); for ${ \\\texttt { i } } = { \texttt { 1 : k } }$ $\begin{array} { r l } & { \mathrm { ~ \tt ~ v ~ = ~ \tt ~ A ^ { \tt ~ 7 } * b } ; \quad \mathrm { ~ n ~ \tt ~ v ~ = ~ \tt ~ n o r m ( v ) ~ } ; } \\ & { \mathrm { ~ i ~ f ~ \tt ~ n ~ v ~ = ~ 0 ~ } , \quad \mathrm { ~ b ~ r e a k , ~ \ e n d ~ \tt ~ } } \\ & { \mathrm { ~ \tt ~ v ~ = ~ \tt ~ v / n v } ; } \\ & { \mathrm { ~ u _ \tt ~ = ~ \tt ~ A ^ { \tt ~ * } v } ; \quad \mathrm { ~ u _ \tt ~ = ~ u _ \tt / n o r m ( u ) ~ } ; } \\ & { \mathrm { ~ \tt ~ \tt ~ 9 _ e ~ I \textmu a t e ~ \tt ~ A ^ \tt ~ a n d ~ b _ \tt ~ } } \\ & { \mathrm { ~ \tt ~ p ~ = ~ \tt ~ A ^ { \tt ~ * } * u _ \tt ~ ; ~ { \tt ~ z } ( i ) ~ = ~ b _ \tt ~ > ~ u _ \tt ~ ; ~ } } \\ & { \mathrm { ~ \tt ~ A ~ = ~ \tt ~ A ^ \tt ~ - ~ u * \mathrm { p } ~ } ; \quad \mathrm { ~ b ~ \tt ~ = ~ b ~ - ~ u * z \mathrm { ~ ( ~ i ) ~ } ; ~ \mathrm { ~ \tt ~ \forall ~ } _ \mathrm { \tt ~ 0 } ~ } } \\ & { \mathrm { ~ \tt ~ V \left( : ~ , ~ i ~ \right) ~ = ~ v _ \tt ~ ; ~ \ u ( \tt ~ ; ~ i ) ~ = ~ u _ \tt ~ ; ~ \ u _ \tt ~ P ( : , ~ i ) ~ = ~ p _ \tt ~ ; ~ } } \end{array}$ ate data end $\mathrm {  ~ x ~ } = \mathrm {  ~ V } * \left( \left( \mathrm { P } ^ { \prime } * \mathrm { v } \right) \setminus \mathrm { z } \right) ;$ % Regression coefficients   
end

NIPALS-PLS uses three matrix-vector products and one rank-one deflation that together require 8mn flops per PLS factor. The flop counts for the additional scalar products and the final back-substitution for solving the upper triangular systems are negligible in comparison. For $k \ll \operatorname* { m i n } ( m , n )$ this is the same number of flops per step as required using Householder bidiagonalization.

In exact arithmetic, NIPALS-PLS computes the sequence of Krylov subspace approximations defined in Theorem 4.2.4. The following important result is due to Eldén [375, 2004].

Theorem 4.2.7. The vectors $\{ v _ { 1 } , \ldots , v _ { k } \}$ and $\{ u _ { 1 } , \ldots , u _ { k } \}$ generated by NIPALS-PLS form orthonormal bases for $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ and $\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b )$ ,respectively. In exact arithmetic, these vectors are the same as the columns of $V _ { k }$ and $U _ { k }$ from the Bidiag2 algorithm. It also follows that $P _ { k } ^ { T } V _ { k }$ is an upper bidiagonal matrix, and $x _ { k }$ is the kth Krylov subspace approximation.

In floating-point arithmetic there will be a progressive loss of orthogonality in $U _ { k }$ and $V _ { k }$ in NIPALS-PLS,and the computed off-bidiagonal elements in $P _ { k } ^ { T } V _ { k }$ will not be negligible. The loss of orthogonality is approximately proportional to the condition number $\kappa ( P _ { k } ^ { T } V _ { k } )$ ; see Bjorck [137, 2014]._However, relations (4.2.43) still hold to working precision. Although in theory the matrix $P _ { k } ^ { T } V _ { k }$ is upperbidiagonal,thiswillnotbethecaseinfloating-poitopu-tation. It is not clear if neglecting the of-bidiagonal elements in $P _ { k } ^ { T } V _ { k }$ improves the accuracy of the solution. In the implementation above we follow the original NIPALS-PLS algorithm and treat $P _ { k } ^ { T } V _ { k }$ as afull matrix. This increases the arithmetic cost of solving the subproblem (4.2.42) from $2 k$ flops to $2 k ^ { 3 } / 3$ flops. Tests show only marginal differences in accuracy for these options.

The high accuracy of NIPALS-PLS seems to be partly due to the fact that the augmented data matrix $( A , b )$ is deflated before the next step of orthogonalization is carried out.In exact arithmetic,the vectors $u _ { 1 } , \ldots , u _ { k }$ are mutually orthogonal. Then $\zeta _ { k } = u _ { k } ^ { T } b _ { k - 1 } = u _ { k } ^ { T } b$ and NIPALS-PLS can be“simplified”by omitting the deflation of $b$ .In floating-point arithmetic this omission can substantially increase the loss of orthogonality in $U _ { k }$ and $V _ { k }$ and cause a loss of accuracy in the computed $x _ { k }$ . It is unfortunate that omitting the deflation of $b$ seems to have become the norm rather than the exception.For example,Manne [771, $\mathrm { 1 9 8 7 } ]$ proposes a marginally faster PLS algorithm by omitting the deflation of $b$ .The implementation of NIPALS tested by Andersson [29,2oog] also omits this deflation. Unfortunately, this practice has spread even to some commercial statistical software packages.

In the context of iterative methods for least squares problems, the Bidiag2 process is known to lead to a less stable algorithm than Bidiag1; see Paige and Saunders [866,1g82]. For PLS it is more direct to use the Bidiag2 process.In the implementation below,orthogonality in the computed basis vectors $u _ { k }$ and $v _ { k }$ is preserved by reorthogonalizing the new basis vectors $u _ { k + 1 }$ and $v _ { k + 1 }$ against all previous basis vectors.Then there is no difference in stability between Bidiagl and Bidiag2,as confrmed by tests in Bjorck and Indahl [148,2o17].The additional cost of reorthogonalizing is about $4 ( m + n ) k ^ { 2 }$ flops for $k$ factors. Unless $k$ is very large, this overhead is acceptable.

# Algorithm 4.2.2 (Bidiag2-PLS).

$[ \mathrm { x } , \mathrm { U } , \mathrm { B } , \mathrm { V } ] = \mathrm { b i d i a g 2 p 1 s ( \mathrm { A } , \mathrm { b } , \mathrm { k } ) }$   
$\%$ BIDIAG2-PLS computes the first k PLS factors using Golub--Kahan bidiagonalization   
%--- $\mathtt { [ m , n ] } \ = \ \mathtt { s i z e ( A ) }$ ； $\tt { B } \thinspace =$ zeros(k,2)；% B stored by diagonals $\begin{array} { l } { { \mathrm {  ~ x ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) ; \mathrm {  ~ { \cal ~ U } ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) ; \mathrm {  ~ { \cal ~ V } ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) } } \\ { { \mathrm {  ~ v ~ } = \mathrm {  ~ A ~ } ^ { \prime } * { \mathrm {  ~ b ~ } } ; \mathrm {  ~ { \cal ~ V } ~ } = \mathrm {  ~ v / n o r m ~ } ( \mathrm {  ~ v } ) ; } } \\ { { \mathrm {  ~ w ~ } = \mathrm {  ~ A ~ } { \ast \mathrm {  ~ v ~ } } ; \mathrm {  ~ { \cal ~ r h o } ~ } = \mathrm { \ n o r m ~ } ( \mathrm {  ~ w ~ } ) ; \mathrm {  ~ { \cal ~ U } ~ } = ( \mathrm {  ~ 1 / r h o ~ } ) { \ast \mathrm {  ~ w ~ } } ; } } \\ { { \mathrm {  ~ V ~ } ( : , { \bf ~ 1 } ) = \mathrm {  ~ v } ; \mathrm {  ~ { \cal ~ U } ~ } ( : , { \bf ~ 1 } ) = \mathrm {  ~ w ~ } ; \mathrm {  ~ { \cal ~ B } ~ } ( 1 , { \bf ~ 1 } ) = \mathrm {  ~ r h o ~ } ; } } \\ { { \mathrm {  ~ z ~ } = \mathrm {  ~ v / r h o ~ } ; \mathrm {  ~ { \cal ~ x } ~ } ( : , { \bf ~ 1 } ) = ( \mathrm {  ~ { \cal ~ { \cal ~ G } } ~ } ^ { \prime } * { \mathrm {  ~ b } } ) * { \bf z } ; } } \end{array}$ ； for $\dot { \mathtt { \_ { \lambda } } } = 2 : \mathtt { k }$ % Bidiagonalization V = A'\*w - rho\*v; $\begin{array} { l l l l l } { \dot { \mathrm {  ~ \gamma ~ } } } & { \dot { \mathrm {  ~ \dots ~ } } } & { \mathrm {  ~ \Im ~ } } & { \dot { \mathrm {  ~ \Im ~ } } } & { \mathrm {  ~ \gamma ~ } } \\ { \mathrm {  ~ \nabla ~ } } & { = \mathrm {  ~ \nabla ~ } \mathrm { V } \ast \left( \mathrm { V } ^ { \prime } \ast \mathrm {  ~ \times ~ } \mathrm {  ~ \nabla ~ } \right) ; } & { \mathrm {  ~ \sqrt { \eta } _ { \mathrm { \tiny ~ a } } ~ } \mathrm { R e o r t h o g } } \\ { \mathrm {  ~ \mathrm { g a m m a ~ } } } & { = \mathrm {  ~ \ n o r m } \left( \mathrm { v } \right) ; } & { \mathrm {  ~ \mathrm { \cal ~ B } \left( i - 1 , 2 \right) ~ } } & { = \mathrm {  ~ \ g a m m a ~ } ; } \\ { \mathrm {  ~ \nabla ~ } } & { = \mathrm {  ~ \Gamma ~ } ( 1 / \mathrm { g a m m a } ) \ast \mathrm {  ~ \nabla ~ } \mathrm { V } \left( \mathrm {  ~ \cdot ~ } , \mathrm {  ~ i ~ } \right) } & { = \mathrm {  ~ \ v ~ } ; } \\ { \mathrm {  ~ \overline { { \cal ~ } } } } & { \dot { \mathrm {  ~ \nabla ~ } } } & { \dot { \mathrm {  ~ A } } \ast \mathrm {  ~ \nabla ~ } - \mathrm {  ~ \ g a m m a \ast \mathrm {  ~ \nabla ~ } } ; } \\ { \mathrm {  ~ \nabla ~ } } & { \dot { \mathrm {  ~ \nabla ~ } } } & { = \mathrm {  ~ \nabla ~ } \mathrm { V } \ast \left( \mathrm { U } ^ { \prime } \ast \mathrm {  ~ \times ~ } \mathrm {  ~ \nabla ~ } \right) ; } & { \mathrm {  ~ \nabla ~ } \mathrm { \sqrt { \eta } _ { \mathrm { \tiny ~ R } } \ e o r t h o g } } \\ { \mathrm {  ~ \mathrm { \texttt ~ { ~ r h o ~ } } } } & { = \mathrm {  ~ \ n o r m } \left( \mathrm { u } \right) ; } & { \mathrm {  ~ \mathrm { \cal ~ B } \left( i ~ \right)} , 1  } & { = \mathrm {  ~ \ r h o ~ } \mathrm {  ~ \nabla ~ } \mathrm { r h o ~ } ; } \end{array}$ onalize onalize if rho $\ c = ~ 0$ ，break，end $\begin{array} { r } { \texttt { w } = \ ( 1 / \mathrm { r h o } ) * _ { \texttt { W } } ; \quad \mathrm { U } \left( : , \mathtt { i } \right) \ = \ \texttt { w } ; } \end{array}$ $\mathrm { \Lambda ~ z ~ = ~ ( 1 / r h o ) * ( v ~ - ~ \ g a m m a * z ) ~ ; ~ \% ~ U p d \hat { \Lambda } ~ }$ ite solution $\mathbf { x } \left( : , \mathbf { i } \right) \ = \ \mathbf { x } \left( : , \mathbf { i } - 1 \right) \ \ + \ \left( \mathbf { w } ^ { \prime } * \mathbf { b } \right) * \mathbf { z } ;$ end   
end

Example 4.2.8. Like TSVD (truncated SVD) approximations, the PLS approximations are orthogonal projections of the pseudoinverse solution onto a nested sequence of subspaces of dimension $k \ll n$ ； see Section 3.6.2. Both sequences have regularization properties. However, because PLS only requires a partial bidiagonalization of $A$ , it is much less expensive to compute than TSVD.Further, for PLS the subspaces depend (nonlinearly) on the right-hand side $b$ and are tailored to the specific right-hand side.Therefore,the minimum error for an illconditioned problem is often achieved with a lower dimensional subspace for PLS rather than for TSVD.Consider the discretized problem $K f = g$ in Example 3.6.1 for the linear operator $K ( s , t ) = e ^ { - ( s - t ) ^ { 2 } }$ with $m = n = 1 0 0$ Let $f$ be known, set $g = K f$ ,and let ${ \widehat { g } } = g + e$ be a perturbed right-hand side, where $e$ is normally distributed with zero mean and variance $1 0 ^ { - 4 }$ . Figure 4.2.1 shows the relative error $\| f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ and the relative residual norm $\| { K f _ { k } - g } \| _ { 2 } / \| g \| _ { 2 }$ for the PLS and TSVD solutions as a function of $k$ . The results are almost identical.For PLS the smallest error occurs for $k = 1 0$ and for TSVD occurs for $k = 1 2$ .For larger values of $k$ the error increases rapidly, but the residual norm is almost constant.

![](images/61b0c8c7de0103a9631a1bdf865bcb6db1887abcc06ca715fb2666b081d5604a.jpg)  
Figure 4.2.1. Relative error $\| f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ (solid line)and relative residual $\| K f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ (dashed line) after k steps. PLS (left) and TSVD (right). Used with permission of Springer International Publishing;from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e _ { : }$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

Many algorithms that differ greatly in speed and accuracy have been proposed for PLS. Both NIPALS-PLS and HHBD perform transformations on $A$ that require $A$ to be explicitly available. This makes them less suitable for large-scale problems. Andersson [29, 2oog] tested nine different PLS algorithms on a set of contrived benchmark problems.The only provably backward stable method among them, HHBD, was much slower than NIPALS-PLS,which also was one of the most accurate,even though it was used here without deflation of $b$ .The version of Bidiag2- PLS used did not employ reorthogonalization and gave poor accuracy. In further tests by Bjorck and Indahl [148, 2O17] the most accurate algorithms were HHBD,NIPALS-PLS with deflation, and Bidiag2-PLS with reorthogonalization. For large-scale problems, Bidiag2-PLS is the method of choice. On some large simulated data sets of size $3 0 , 0 0 0 \times 1 0 , 0 0 0$ and 100 extracted com-ponents, Bidiag2-PLS was about seven times faster than NIPALS. Notably, the popular SIMPLS algorithm by de Jong [295,1993l, used by the MATLAB function plsregres s, gave poor accuracy. This was true even when it was improved by reorthogonalization, as suggested by Faber and Ferré [390, 2008].

# Notes and references

The close relationship between PLS and bidiagonalization is explored by Manne [771,1987] and Helland [599,1988]. Many extensions of the basic PLS algorithm treated here have been devised; see S.Wold, Sjostrom,and Eriksson [1129,2oo1]. An overview of advances in PLS is given by Rosipal and Krämer [937, 2005].

Simon and Zha [996, 2ooo] show that in many applications it may suffice to reorthogonalize either $u _ { k }$ or $v _ { k }$ . However, tests by Bjorck and Indahl [148,2o17] show that such onesided reorthogonalization could lead to a substantial loss of precision compared to full reorthogonalization.

# 4.3 - Some Structured Problems

# 4.3.1 - Two-Block Least Squares Problems

It is sometimes useful to partition a least squares problem into two blocks as

$$
\operatorname* { m i n } _ { y , z } \left\| \left( \begin{array} { l l } { A } & { B } \end{array} \right) \left( \begin{array} { l } { y } \\ { z } \end{array} \right) - b \right\| _ { 2 } ^ { 2 } ,
$$

where $A \in \mathbb { R } ^ { m \times n _ { 1 } }$ ， $B \in \mathbb { R } ^ { m \times n _ { 2 } }$ . One example is periodic spline approximation, which leads to a problem of augmented band form, where $A$ is a band matrix and $B$ is a full matrix with a small number of columns.

If $z$ is given, then $y$ must solve the problem

$$
\operatorname* { m i n } _ { y } \| A y - ( b - B z ) \| _ { 2 } .
$$

Substituting the solution $y = A ^ { \dagger } ( b - B z )$ into (4.3.2) to eliminate $y$ ，we see that $z$ solves the problem

$$
\operatorname* { m i n } _ { z } \| ( I - A A ^ { \dagger } ) ( B z - b ) \| _ { 2 } ,
$$

where $I - A A ^ { \dag } = P _ { \mathcal { N } ( A ^ { T } ) }$ is the orthogonal projector onto $\mathcal { N } ( A ^ { T } )$ . Thus (4.3.1) has been split into two separate least squares problems (4.3.3) and (4.3.2).

One advantage of this is that different methods can be used to solve the two least squares subproblems for $z$ and $y$ .Moreover, the subproblem for $z$ is always better conditioned than the original problem.Hence, $z$ can sometimes be computed with sufficient accuracy by the method of normal equations;see Foster [427,1991]. Another application is when $n _ { 2 } \gg n _ { 1 }$ and the subproblem for $z$ can be solved by an iterative method; see Section 6.3.6.

The normal equations of (4.3.1) are

$$
\left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } B } } \\ { { B ^ { T } A } } & { { B ^ { T } B } } \end{array} \right) \left( \begin{array} { c } { { y } } \\ { { z } } \end{array} \right) = \left( \begin{array} { c } { { A ^ { T } b } } \\ { { B ^ { T } b } } \end{array} \right) .
$$

Eliminating $y$ gives $S z = s$ ，where $S$ is the Schur complement of $A ^ { T } A$ . This can be written

$$
\begin{array} { r } { S = B ^ { T } P _ { N ( A ^ { T } ) } B , \quad s = B ^ { T } P _ { N ( A ^ { T } ) } b , } \end{array}
$$

where $P _ { \mathcal { N } ( A ^ { T } ) } = I - A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ . When $z \in \mathbb { R } ^ { n _ { 2 } }$ has been determined, we obtain $y \in \mathbb { R } ^ { n _ { 1 } }$ from

$$
A ^ { T } A y = A ^ { T } ( b - B z ) .
$$

For beter stability, methods based on orthogonal factorizations should be used. After $n _ { 1 }$ steps,a partial Householder QR factorization reduces the first block in $\left( \begin{array} { l l } { A } & { B } \end{array} \right)$ to the upper triangular form,

$$
Q _ { 1 } ^ { T } \left( \begin{array} { c c c } { { A } } & { { B } } & { { b } } \end{array} \right) = \left( \begin{array} { c c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } & { { c _ { 1 } } } \\ { { 0 } } & { { A _ { 2 2 } } } & { { c _ { 2 } } } \end{array} \right) ,
$$

where $Q _ { 1 } = P _ { 1 } \cdot \cdot \cdot P _ { n _ { 1 } }$ .By the orthogonal invariance of the 2-norm,

$$
\begin{array} { r } { \| A x - b \| _ { 2 } = \left\| \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) \left( \begin{array} { c } { y } \\ { z } \end{array} \right) - \left( \begin{array} { c } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right) \right\| _ { 2 } . } \end{array}
$$

This gives for $z$ and $y$ the subproblems

$$
\operatorname* { m i n } _ { z } \| A _ { 2 2 } z - c _ { 2 } \| _ { 2 } , \qquad R _ { 1 1 } y = c _ { 1 } - R _ { 1 2 } z .
$$

Similarly, after $n _ { 1 }$ steps of MGS we have obtained the partial factorization

$$
\left( \begin{array} { c c } { A } & { b } \end{array} \right) = \left( Q _ { 1 } \quad A ^ { ( n _ { 1 } + 1 ) } \quad b ^ { ( n _ { 1 } + 1 ) } \right) \left( \begin{array} { c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { c _ { 1 } } \\ { 0 } & { I } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) ,
$$

where $Q _ { 1 } ^ { T } A ^ { ( n _ { 1 } + 1 ) } = 0 $ The original problem then decomposes into (compare (4.3.7))

$$
\operatorname* { m i n } _ { z } \| A ^ { ( n _ { 1 } + 1 ) } z - b ^ { ( n _ { 1 } + 1 ) } \| _ { 2 } , \qquad R _ { 1 1 } y = c _ { 1 } - R _ { 1 2 } z .
$$

The following lemma gives an alternative formulation without explicitly referring to orthogonal projections.

Lemma 4.3.1. Let $z \in \mathbb { R } ^ { n _ { 2 } }$ and $W \in \mathbb { R } ^ { n _ { 2 } \times n _ { 1 } }$ be the solutions to the least squares problems

$$
\operatorname* { m i n } _ { \boldsymbol { w } } \| \boldsymbol { A } \boldsymbol { w } - \boldsymbol { b } \| _ { 2 } , \qquad \operatorname* { m i n } _ { \boldsymbol { W } } \| \boldsymbol { A } \boldsymbol { W } - \boldsymbol { B } \| _ { F } .
$$

Then the solution to (4.3.1) is given by $y = z - W z ,$ where $z$ solves

$$
\operatorname* { m i n } _ { z } \| ( B - A W ) z - ( b - A w ) \| _ { 2 } .
$$

Proof. If $w$ and $W$ solve (4.3.8), then $A w = P _ { A } b$ and $A W = P _ { A } B$ .Hence the least squares problems (4.3.9) and (4.3.3) are equivalent. Further, $y = z - W x$ solves (4.3.2),because $A y =$ $A ( z - W z ) = P _ { A } ( b - A z )$ □

A common practice in linear regression is to preprocess the data by centering the data, i.e., subtracting out the means. This can be interpreted as a simple case of a two-block least squares problem, where

$$
( e \quad B ) \left( { \begin{array} { l } { \xi } \\ { z } \end{array} } \right) = b , \quad e = ( 1 , \ldots , 1 ) ^ { T } .
$$

Multiplying $B \in \mathbb { R } ^ { m \times n }$ and $b \in \mathbb { R } ^ { m }$ with the projection matrix $( I - e e ^ { T } / m )$ gives

$$
\bar { B } = B - \frac { 1 } { m } e ( e ^ { T } B ) , \quad \bar { b } = b - \frac { e ^ { T } b } { m } e .
$$

This makes the columns of $\bar { B }$ and $\bar { b }$ orthogonal to $e$ .The reduced least squares problem becomes $\mathrm { m i n } _ { x } \| \bar { B } z - \bar { b } \| _ { 2 }$ . After solving the reduced problem for $z$ ,we obtain $\xi = e ^ { T } ( b - B z ) / m$

Example 4.3.2. The Hald cement data (see [561,1952,p. 647]) are used in Draper and Smith [331,1998,Appendix B] and several other books as an example of regression analysis. The right-hand side consists of $m = 1 3$ observations of the heat evolved in cement during hardening. The explanatory variables are four different ingredients of the mix and a constant term:

For the least squares problem $\| A x - b \| _ { 2 }$ ， $\kappa ( A ) \approx 3 . 2 4 5 \cdot 1 0 ^ { 3 }$ indicates that about six digits may be lost when using the normal equations. The first column of ones in $A = ( e , B )$ is added to extract the mean values. The first variable $\xi$ in $x = ( \xi , y )$ can be eliminated by setting

$$
\bar { B } = B - e p ^ { T } , \quad c = b - \beta e ,
$$

where $p = ( e ^ { T } B ) / m$ ， $\beta = e ^ { T } b / m$ ,and $\xi = \beta - p ^ { T } y$ ，The reduced problem $\begin{array} { r } { \operatorname* { m i n } _ { y } \| \bar { B } y - c \| _ { 2 } } \end{array}$ is much better conditioned: $\kappa ( \bar { B } ) = 2 3 . 0$ . Normalizing the columns of $B$ to have unit length decreases the condition number by only a small amount to $\kappa ( B D ) = 1 9 . 6 $

# 4.3.2 - Block-Angular Problems

As noted by Rice [925, 1983], many large sparse least squares problems possess a natural multi-level block structure. An early example is geodetic survey problems. A technique for breaking down such problems into geographically defined subproblems was introduced by Helmert [600, 1880]; see Golub and Plemmons [505,198o]). Other examples are photogrammetry (Golub, Luk,and Pagano [499,1979l), Doppler radar positioning (Manneback, Murigande,and Toint [773,1985l),and economic models (Duchin and Szyld [339,1979l).

The substructuring can reflect a “local connection” in the underlying physical problem. For example, a geodetic position network consists of geodetic stations connected through observations.To each station corresponds a set of unknown coordinates to be determined. This data may naturally be arranged by counties, then by states, then by countries. Let $\boldsymbol { B }$ be sets of stations that separate the other stations into $p$ blocks $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ in such a way that station variables in $A _ { i }$ are not connected by observations to station variables in $A _ { j }$ if $i \neq j$ . Order the variables so that those in $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ appear first and those in $\boldsymbol { B }$ last. The dissection can also be continued by dissecting each of the regions $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ into separate subregions,and so on in a recursive fashion. The blocking of the region for one and two levels of dissection for $p = 2$ is pictured in Figure 4.3.1. In such a nested dissection, it is advantageous to perform the dissection in such a way that in each stage of the dissection,the numbers of variables in the two partitions are roughly the same. Also,the number of variables in the separator nodes should be as small as possible.

![](images/3f9b9eac12fc1a07cec687b47abb257808fe2b33f99a3636a16f89e072d896b0.jpg)  
Figure 4.3.1. One and two levels of dissection of a region.

The block structure in the matrix of the corresponding linear system induced by one and two levels of dissection for $p = 2$ is shown here:

$$
A = \left( \begin{array} { l l l } { { A _ { 1 } } } & { { } } & { { B _ { 1 } } } \\ { { } } & { { A _ { 2 } } } & { { B _ { 2 } } } \end{array} \right) , \qquad A = \left( \begin{array} { l l l l l l l } { { A _ { 1 } } } & { { } } & { { } } & { { B _ { 1 } } } & { { } } & { { D _ { 1 } } } \\ { { } } & { { A _ { 2 } } } & { { } } & { { B _ { 2 } } } & { { } } & { { D _ { 2 } } } \\ { { } } & { { } } & { { A _ { 3 } } } & { { } } & { { C _ { 3 } } } & { { D _ { 3 } } } \\ { { } } & { { } } & { { } } & { { A _ { 4 } } } & { { } } & { { C _ { 4 } } } & { { D _ { 4 } } } \end{array} \right) .
$$

There is a finer structure in $A$ not shown here. For example, in one level of dissection most of the equations involve variables in $A _ { 1 }$ or $A _ { 2 }$ only but not in $B$

For a least squares problems $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ arising from a one-level dissection into $p$ regions,the matrix has a bordered block diagonal or block-angular form,

$$
A = \left( \begin{array} { c c c c c } { A _ { 1 } } & & & & { B _ { 1 } } \\ & { A _ { 2 } } & & & { B _ { 2 } } \\ & & { \ddots } & & & { \vdots } \\ & & & { A _ { p } } & { B _ { p } } \end{array} \right) , \quad x = \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { p } } \\ { x _ { p + 1 } } \end{array} \right) , \quad b = \left( \begin{array} { c } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { p } } \end{array} \right) ,
$$

where

$$
A _ { i } \in \mathbb { R } ^ { m _ { i } \times n _ { i } } , \quad B _ { i } \in \mathbb { R } ^ { m _ { i } \times n _ { p + 1 } } , \quad i = 1 , \dots , p ,
$$

and $m = m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { p }$ ， $n = n _ { 1 } + n _ { 2 } + \cdot \cdot \cdot + n _ { p + 1 }$ . For some problems,the blocks $A _ { i }$ and/or $B _ { i }$ are themselves large sparse matrices,often of the same general sparsity pattern as $A$ .There is a wide variation in the number and size of blocks. Some problems have large blocks with $p$ of moderate size (1O-1OO),while others have many more but smaller blocks.

The normal matrix $A ^ { T } A$ ，with $A$ given as in (4.3.14), has a doubly bordered block diagonal form

$$
\boldsymbol { A } ^ { T } \boldsymbol { A } = \left( \begin{array} { c c c c } { \boldsymbol { A } _ { 1 } ^ { T } \boldsymbol { A } _ { 1 } } & & & { \boldsymbol { A } _ { 1 } ^ { T } \boldsymbol { B } _ { 1 } } \\ & { \boldsymbol { A } _ { 2 } ^ { T } \boldsymbol { A } _ { 2 } } & & { \boldsymbol { A } _ { 2 } ^ { T } \boldsymbol { B } _ { 2 } } \\ & & { \ddots } & & { \vdots } \\ & & & { \boldsymbol { A } _ { p } ^ { T } \boldsymbol { A } _ { p } } & { \boldsymbol { A } _ { p } ^ { T } \boldsymbol { B } _ { p } } \\ { \boldsymbol { B } _ { 1 } ^ { T } \boldsymbol { A } _ { 1 } } & { \boldsymbol { B } _ { 2 } ^ { T } \boldsymbol { A } _ { 2 } } & { \cdots } & { \boldsymbol { B } _ { p } ^ { T } \boldsymbol { A } _ { p } } & { \boldsymbol { C } } \end{array} \right) ,
$$

where $\begin{array} { r } { C = \sum _ { i = 1 } ^ { p } B _ { i } ^ { T } B _ { i } } \end{array}$ . The right-hand side $f = ( f _ { 1 } , \dots , f _ { p + 1 } )$ of the normal equations is

$$
f _ { i } = A _ { i } ^ { T } b _ { i } , \quad i = 1 , \ldots , p , \quad f _ { p + 1 } = \sum _ { i = 1 } ^ { p } B _ { i } ^ { T } b _ { i } .
$$

f $\operatorname { r a n k } ( A ) = n$ ,the upper triangular Cholesky factor $R$ of $A ^ { T } A$ exists and has a block structure similar to that of $A$ ：

$$
R = \left( \begin{array} { c c c c c c } { { R _ { 1 } } } & { { } } & { { } } & { { } } & { { S _ { 1 } } } \\ { { } } & { { R _ { 2 } } } & { { } } & { { } } & { { S _ { 2 } } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { R _ { p } } } & { { S _ { p } } } \\ { { } } & { { } } & { { } } & { { } } & { { R _ { p + 1 } } } \end{array} \right) .
$$

Equating the blocks in $R ^ { T } R = A ^ { T } A$ gives

$$
\begin{array} { r l } & { R _ { i } ^ { T } R _ { i } = A _ { i } ^ { T } A _ { i } , \qquad R _ { i } ^ { T } S _ { i } = A _ { i } ^ { T } B _ { i } , \quad i = 1 , \ldots , p , } \\ & { R _ { p + 1 } ^ { T } R _ { p + 1 } = C - \displaystyle \sum _ { i = 1 } ^ { p } S _ { i } ^ { T } S _ { i } , } \end{array}
$$

where the Cholesky factors $R _ { i } \in \mathbb { R } ^ { n _ { i } \times n _ { i } }$ and $S _ { i }$ can be computed independently and in parallel. The least squares solution is then obtained from the two-block triangular systems $R ^ { T } z = A ^ { T } b =$ $f$ and $R x = z$ .This amounts to first solving the lower triangular systems

$$
R _ { i } ^ { T } z _ { i } = A _ { i } ^ { T } b _ { i } , \quad i = 1 , \ldots , p , \qquad R _ { p + 1 } ^ { T } z _ { p + 1 } = f _ { p + 1 } - \sum _ { i = 1 } ^ { p } S _ { i } ^ { T } z _ { i } ,
$$

and then the upper triangular systems

$$
R _ { p + 1 } x _ { p + 1 } = z _ { p + 1 } , \qquad R _ { i } x _ { i } = z _ { i } - S _ { i } x _ { p + 1 } , \quad i = 1 , \ldots , p .
$$

Again, nearly all of these systems can be solved in parallel.

A more accurate algorithm based on QR factorization for solving block-angular least squares algorithms is given by Golub,Luk,and Pagano [499,1979]. This proceeds in the following three steps:

1.Reduce the diagonal block $A _ { i }$ to upper triangular form by a sequence of orthogonal transformations applied to $( A _ { i } , B _ { i } )$ and the right-hand side $b _ { i }$ ,yielding

$$
Q _ { i } ^ { T } ( A _ { i } , B _ { i } ) = \left( { \begin{array} { c c } { R _ { i } } & { S _ { i } } \\ { 0 } & { T _ { i } } \end{array} } \right) , \qquad Q _ { i } ^ { T } b _ { i } = \left( { \begin{array} { c } { c _ { i } } \\ { d _ { i } } \end{array} } \right) , \quad i = 1 , \dots , p .
$$

Any sparse structure in the blocks $A _ { i }$ should be exploited.

2. Form

$$
T = \left( \begin{array} { c } { { T _ { 1 } } } \\ { { \vdots } } \\ { { \vdots } } \\ { { T _ { p } } } \end{array} \right) , \qquad d = \left( \begin{array} { c } { { d _ { 1 } } } \\ { { \vdots } } \\ { { \vdots } } \\ { { d _ { p } } } \end{array} \right) ,
$$

and compute the QR factorization

$$
\begin{array} { r l } { Q _ { p + 1 } ^ { T } \left( T \right. } & { { } d ) = \left( \begin{array} { c c } { R _ { p + 1 } } & { c _ { p + 1 } } \\ { 0 } & { d _ { p + 1 } } \end{array} \right) . } \end{array}
$$

The residual norm is given by $\rho = \| d _ { p + 1 } \| _ { 2 }$

3. Solve $x _ { p + 1 } , x _ { p } , \dotsc , x _ { 1 }$ from the upper triangular systems

$$
R _ { p + 1 } x _ { p + 1 } = c _ { p + 1 } , \qquad R _ { i } x _ { i } = c _ { i } - S _ { i } x _ { p + 1 } , \quad i = 1 , \ldots , p .
$$

There are several ways to organize this algorithm. In steps 1 and 3 the computations can be performed in parallel on the $p$ subsystems. It is then advantageous to continue the reduction in step 1 so that the matrices $T _ { i }$ ， $i = 1 , \ldots , p$ ,are brought into upper trapezoidal form.

Large problems may require too much memory,even if we take into account the block-angular structure. Cox [275,199o] suggests two modifications by which the storage requirement can be reduced. By merging steps 1 and 2, it is not necessary to hold all blocks $T _ { i }$ simultaneously in memory. Even more storage can be saved by discarding $R _ { i }$ and $S _ { i }$ after they have been computed in step 1 and recomputing them for step 3. Indeed,only $R _ { i }$ needs to be recomputed, because after $y$ has been computed in step 2, $x _ { i }$ is the solution to the least squares problems

$$
\operatorname* { m i n } _ { x _ { i } } \| A _ { i } x _ { i } - g _ { i } \| _ { 2 } , \qquad g _ { i } = b _ { i } - B _ { i } y .
$$

Hence,to determine $x _ { i }$ we only need to (re)compute the QR factorizations of $( A _ { i } , g _ { i } )$ ， $i \ =$ $1 , \ldots , p$ . In some practical problems this modification can reduce the storage requirement by an order of magnitude,while recomputation of $R _ { i }$ only increases the operation count by a small percentage.

From the structure of the $R$ -factor in (4.3.15), the diagonal blocks of the covariance matrix $C = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }$ can be writen as (see Golub, Plemmons,and Sameh [506,1988])

$$
\begin{array} { r l } & { C _ { p + 1 , p + 1 } = R _ { p + 1 } ^ { - 1 } R _ { p + 1 } ^ { - T } , } \\ & { C _ { i , i } = R _ { i } ^ { - 1 } ( I + W _ { i } ^ { T } W _ { i } ) R _ { i } ^ { - T } , \quad W _ { i } ^ { T } = S _ { i } R _ { p + 1 } ^ { - 1 } , \quad i = 1 , \ldots , p . } \end{array}
$$

Hence,if we compute the QR factorizations

$$
Q _ { i } \left( { \begin{array} { c } { W _ { i } } \\ { I } \end{array} } \right) = \left( { \begin{array} { c } { U _ { i } } \\ { 0 } \end{array} } \right) , \quad i = 1 , \ldots , p ,
$$

we have $I + W _ { i } ^ { T } W _ { i } = U _ { i } ^ { T } U _ { i }$ and

$$
\begin{array} { r } { C _ { i , i } = ( U _ { i } R _ { i } ^ { - T } ) ^ { T } ( U _ { i } R _ { i } ^ { - T } ) , \quad i = 1 , \ldots , p . } \end{array}
$$

This method assumes that all the matrices $R _ { i }$ and $S _ { i }$ have been retained. For a discussion of how to compute variances and covariances when the storage saving algorithm is used, see Cox [275, 1990].

In some applications the matrices $R _ { i }$ will be sparse,but a lot of fill occurs in the blocks $B _ { i }$ in step 1. Then the triangular matrix $R _ { p + 1 }$ will be full and expensive to compute. For such problems a block-preconditioned iterative method may be more efcient; see Section 6.3. Then an iterative method,such as CGLS or LSQR,is applied to the problem

$$
\operatorname* { m i n } _ { y } \| ( A M ^ { - 1 } ) y - b \| _ { 2 } , \quad y = M x ,
$$

where a suitable preconditioner is $M = \operatorname { d i a g } \left( R _ { 1 } , \dotsc , R _ { p } , R _ { p + 1 } \right)$ ; see Golub, Manneback, and Toint [500, 1986].

# Notes and references

Dissection and orthogonal decompositions in geodetic survey problems are treated by Golub and Plemmons [505,198o]. Avila and Tomlin [44,1979] discuss parallelism in the solution of very large least squares problems by nested dissection and the method of normal equations. Weil and Kettler [1116,1971] give a heuristic algorithm for permuting a general sparse matrix into blockangular form. The dissection procedure described above is a variation of the nested dissection orderings developed for general sparse positive definite systems; see Section 5.1.5.

# 4.3.3 - Kronecker Product Structure

Sometimes least squares problems occur with a highly regular block structure. Here we consider least squares problems of the form

$$
\operatorname* { m i n } _ { x } \| ( A \otimes B ) x - f \| _ { 2 } ,
$$

where $A \otimes B$ is the Kronecker product of $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { p \times q }$ . This product is the $m p \times n q$ block matrix

$$
A \otimes B = \left( \begin{array} { c c c c } { { a _ { 1 1 } B } } & { { a _ { 1 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { 1 n } B } } \\ { { a _ { 2 1 } B } } & { { a _ { 2 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { 2 n } B } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } \\ { { a _ { m 1 } B } } & { { a _ { m 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { m n } B } } \end{array} \right) .
$$

Problems with Kronecker structure arise in several application areas, including signal and image processing, photogrammetry,and multidimensional approximation; see Fausett and Fulton [399, 1994]. Grosse $[ 5 4 0 , 1 9 8 0 ]$ describes a tensor factorization algorithm and how it applies to least squares fiting of multivariate data on a rectangular grid. Such problems can be solved with great savings in storage and operations. These savings are essential for problems where $A$ and $B$ are large. It is not unusual to have several hundred thousand equations and unknowns.

The Kronecker product and its relation to linear matrix equations, such as Lyapunov's equation,are treated in Horn and Johnson [640,1991, Chapter 4]. See also Henderson and Searle [602, $\mathbf { 1 9 8 1 } ]$ and Van Loan [1O83, 2ooo]. We now state some elementary facts about Kronecker products that follow from its definition:

$$
\begin{array} { r l } & { ( A + B ) \otimes C = ( A \otimes C ) + ( B \otimes C ) , } \\ & { A \otimes ( B + C ) = ( A \otimes B ) + ( A \otimes C ) , } \\ & { A \otimes ( B \otimes C ) = ( A \otimes B ) \otimes C , } \\ & { ( A \otimes B ) ^ { T } = A ^ { T } \otimes B ^ { T } . } \end{array}
$$

A further important relation, which is not so obvious,is given next.

Lemma 4.3.3. If the ordinary products $A C$ and $B D$ are defined, then

$$
( A \otimes B ) ( C \otimes D ) = A C \otimes B D .
$$

Proof. See Lancaster and Tismenetsky [713,1985, Chap. 12.1].

As a corollary of this lemma we obtain the identity

$$
( A _ { 1 } \otimes B _ { 1 } ) ( A _ { 2 } \otimes B _ { 2 } ) \cdot \cdot \cdot ( A _ { p } \otimes B _ { p } ) = ( A _ { 1 } A _ { 2 } \cdot \cdot \cdot A _ { n } ) \otimes ( B _ { 1 } B _ { 2 } \cdot \cdot \cdot B _ { n } ) ,
$$

assuming al the products are defined. We can also conclude that if $P$ and $Q$ are orthogonal $n \times n$ matrices, then $P \otimes Q$ is an orthogonal $n ^ { 2 } \times n ^ { 2 }$ matrix. Furthermore,if $A$ and $B$ are square and nonsingular, it follows that $A \otimes B$ is nonsingular and

$$
( A \otimes B ) ^ { - 1 } = A ^ { - 1 } \otimes B ^ { - 1 } .
$$

This generalizes to pseudoinverses, as shown in the following lemmas.

Lemma 4.3.4. Let $A ^ { \dagger }$ and $B ^ { \dagger }$ be the pseudoinverses of $A$ and $B$ Then

$$
( A \otimes B ) ^ { \dagger } = A ^ { \dagger } \otimes B ^ { \dagger } .
$$

Proof. The lemma follows by verifying that $X = A ^ { \dagger } \otimes B ^ { \dagger }$ satisfies the four Penrose conditions in Theorem 1.2.11. □

We now introduce a function, closely related to the Kronecker product, that converts a matrix into a vector. For a matrix $C = ( c _ { 1 } , c _ { 2 } , \ldots , c _ { n } ) \in \mathbb { R } ^ { m \times n }$ we define

$$
\operatorname { v e c } \left( C \right) = \left( { c _ { 2 } } \right) .
$$

Hence vec $( C )$ is the vector formed by stacking the columns of $C$ into one column vector of length mn.We now state a result that shows how the vec-function is related to the Kronecker product.

Lemma 4.3.5. If $A \in \mathbb { R } ^ { m \times n }$ ， $B \in \mathbb { R } ^ { p \times q }$ ,and $F \in \mathbb { R } ^ { q \times n }$ ,then

$$
( A \otimes B ) \mathrm { v e c } ( F ) = \mathrm { v e c } ( B F A ^ { T } ) .
$$

By Lemma 4.3.5, we can write the solution to the Kronecker least squares problem (4.3.23 as

$$
\begin{array} { r } { x = ( A \otimes B ) ^ { \dagger } f = ( A ^ { \dagger } \otimes B ^ { \dagger } ) f = \mathrm { v e c } ( B ^ { \dagger } F ( A ^ { \dagger } ) ^ { T } ) , } \end{array}
$$

where $f = \operatorname { v e c } \left( F \right)$ . This allows a great reduction in the cost of solving (4.3.23). For example, if both $A$ and $B$ are $m \times n$ matrices, the cost of computing the least squares solution is reduced from $O ( m ^ { 2 } n ^ { 4 } )$ to $O ( m n ^ { 2 } )$ .

In some areas, the most common approach to computing the least squares solution to (4.3.23) is from normal equations.If we assume that both $A$ and $B$ have full column rank,we can use the expressions

$$
A ^ { \dagger } = ( A ^ { T } A ) ^ { - 1 } A ^ { T } , \qquad B ^ { \dagger } = ( B ^ { T } B ) ^ { - 1 } B ^ { T } .
$$

However, because of the instability associated with the explicit formation of $A ^ { T } A$ and $B ^ { T } B$ ,an approach based on orthogonal decompositions should generally be preferred. From the complete QR factorizations of $A$ and $B$ ，

$$
A \Pi _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { R _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V _ { 1 } ^ { T } , \qquad B \Pi _ { 2 } = Q _ { 2 } \left( \begin{array} { c c } { { R _ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V _ { 2 } ^ { T } ,
$$

with $R _ { 1 } , R _ { 2 }$ upper triangular and nonsingular, we obtain

$$
\begin{array} { r } { A ^ { \dagger } = \Pi _ { 1 } V _ { 1 } \left( \begin{array} { c c } { R _ { 1 } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) Q _ { 1 } ^ { T } , \qquad B ^ { \dagger } = \Pi _ { 2 } V _ { 2 } \left( \begin{array} { c c } { R _ { 2 } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) Q _ { 2 } ^ { T } . } \end{array}
$$

These expressions can be used in (4.3.27) to compute the pseudoinverse solution of problem (4.3.23),even in the rank-deficient case.

From Lemma 4.3.5, the following simple expression for the singular values and vectors of the Kronecker product $A \otimes B$ ,in terms of the singular values and vectors of $A$ and $B$ ,is obtained.

Lemma 4.3.6. Let $A$ and $B$ have the SVDs $A = U _ { 1 } \Sigma _ { 1 } V _ { 1 } ^ { T }$ and $B = U _ { 2 } \Sigma _ { 2 } V _ { 2 } ^ { T }$ . Then

$$
A \otimes B = ( U _ { 1 } \otimes U _ { 2 } ) ( \Sigma _ { 1 } \otimes \Sigma _ { 2 } ) ( V _ { 1 } \otimes V _ { 2 } ) ^ { T }
$$

is the SVD of $A \otimes B$

Barrlund [84,1998] develops an efficient solution method for constrained least squares problems with Kronecker structure:

$$
\operatorname* { m i n } _ { x } \| ( A _ { 1 } \otimes A _ { 2 } ) x - f \| _ { 2 } { \mathrm { s u b j e c t } } \operatorname { t o } ( B _ { 1 } \otimes B _ { 2 } ) x = g .
$$

With $\operatorname { v e c } \left( X \right) = x$ ， $\operatorname { v e c } \left( F \right) = f$ , and vec $( G ) = g$ , this becomes

$$
\operatorname* { m i n } _ { X } \| A _ { 2 } X A _ { 1 } ^ { T } - F \| _ { F } \quad { \mathrm { s u b j e c t ~ t o } } \quad B _ { 2 } X B _ { 1 } ^ { T } = G .
$$

This problem can be solved by a nulspace method; cf. Section 3.4.2. By a change of variables the unknowns are split into two sets.The first set is determined by the constraints,and the other set belongs to the nullspace of the constraints.

# 4.3.4 - Strongly Rectangular Systems

The least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| b - A x \| _ { 2 } = \operatorname* { m i n } \} ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ , is said to be strongly overdetermined if $m \gg n$ and strongly underdetermined if $m \ll n$ . Candes et al. [2O5, 2o11] mentions a case in stationary video background subtraction, where $n$ is about $1 0 ^ { 3 }$ and $m$ can exceed $1 0 ^ { 6 }$ ．Examples from other application areas,such as seismology, natural language processing, and analysis of the human genome,are given by Meng [788,2014].

Demmel et al. [306, 2o12] give a family of stable, efcient, and communication-reducing algorithms called TSQR for computing the QR factorization of a strongly overdetermined matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \gg n$ . (Such matrices are also called “tall-and-skinny."） In TSQR a rowwise partitioning of $A$ into blocks $A _ { i }$ ， $i = 0 , \ldots , N - 1$ , is used.In the first stage,factorizations

$$
A _ { i } = Q _ { i } R _ { i } , \quad i = 0 , \dots , N - 1 ,
$$

are computed. Subsequent stages merge pairs of the resulting upper triangular matrices in a divide-and-conquer fashion until a single factor $R$ has been obtained. This requires about $\log _ { 2 } N$ stages. The algorithm is exemplified below for $N = 4$ .After the first step we have obtained

$$
A = \left( \begin{array} { l } { A _ { 0 } } \\ { A _ { 1 } } \\ { A _ { 2 } } \\ { A _ { 3 } } \end{array} \right) = \left( \begin{array} { l } { Q _ { 0 } R _ { 0 } } \\ { Q _ { 1 } R _ { 1 } } \\ { Q _ { 2 } R _ { 2 } } \\ { Q _ { 3 } R _ { 3 } } \end{array} \right) = \left( \begin{array} { l l l l } { Q _ { 0 } } & & & \\ & { Q _ { 1 } } & & \\ & & { Q _ { 2 } } & \\ & & & { Q _ { 2 } } \end{array} \right) \left( \begin{array} { l } { R _ { 0 } } \\ { R _ { 1 } } \\ { R _ { 2 } } \\ { R _ { 3 } } \end{array} \right) .
$$

In the next two steps the QR factorizations of the stacked upper triangular factors are merged into one upper triangular matrix

$$
\left( \begin{array} { l } { { \left( \begin{array} { l } { { R _ { 0 } } } \\ { { R _ { 1 } } } \end{array} \right) } } \\ { { \left( \begin{array} { l } { { R _ { 2 } } } \\ { { R _ { 3 } } } \end{array} \right) } } \end{array} \right) = \left( \begin{array} { l l } { { Q _ { 0 1 } } } & { { } } \\ { { } } & { { Q _ { 2 3 } } } \end{array} \right) \left( \begin{array} { l } { { R _ { 0 1 } } } \\ { { R _ { 2 3 } } } \end{array} \right) , \qquad \left( \begin{array} { l } { { R _ { 0 1 } } } \\ { { R _ { 2 3 } } } \end{array} \right) = Q _ { 0 , 1 , 2 , 3 } R .
$$

The representation of the factor $Q$ in TSQR is different from the standard Householder QR factorization. It is implicitly given by a tree of smaller Householder transformations

$$
Q = \left( \begin{array} { c c c c } { { Q _ { 0 } } } & { { } } & { { } } & { { } } \\ { { } } & { { Q _ { 1 } } } & { { } } & { { } } \\ { { } } & { { } } & { { Q _ { 2 } } } & { { } } \\ { { } } & { { } } & { { } } & { { Q _ { 2 } } } \end{array} \right) \left( \begin{array} { c c c } { { Q _ { 0 1 } } } & { { } } & { { } } \\ { { } } & { { Q _ { 2 3 } } } \end{array} \right) Q _ { 0 , 1 , 2 , 3 } .
$$

In general, the combination process in TSQR forms a tree with the row blocks $A _ { i }$ as leaves and the final $R$ as a root. The version pictured above corresponds to a binary tree. The tree shape can be chosen to minimize either the communication between processors or the volume of memory trafic between the main memory and the cache memory of each processor.

The initial Householder QR factorizations of the $N$ blocks $A _ { i }$ require $2 N n ^ { 2 } ( p - n / 3 )$ flops. Merging two triangular QR factorizations of dimension $n \times n$ takes $2 n ^ { 3 } / 3$ flops．The total arithmetic cost of TSQR is higher than that for the direct Householder QR factorization of $A$ ， but for strongly rectangular systems most of the arithmetic work is spent in computing the QR factorizations of the submatrices,which can be done in parallel.

An implementation of TSQR using the message passage interface (MPI) operation AllReduce for multiple processors is given by Langou [719, 2oo7]. Experiments show that the AllReduce QR algorithm obtains nearly linear speed-up. As shown by Mori et al.[811, 2o12],although the number of floating-point operations is larger, the bounds for the backward error and the deviation from orthogonality are smaller for the AllReduce QR algorithm than for standard Householder QR.

Another communication-avoiding QR algorithm suitable for tall-and-skinny matrices is the Cholesky QR algorithm. Let $A \in \mathbb { R } ^ { m \times n }$ have full column rank and $A ^ { T } A = R ^ { T } R$ be its Cholesky factorization. The Cholesky QR algorithm then computes $Q _ { 1 } = A R ^ { - 1 }$ by block forward substitution, giving

$$
A = Q _ { 1 } R ;
$$

see Section 1.2.1. The arithmetic cost of this algorithm is $2 m n ^ { 2 } + n ^ { 3 } / 3$ flops. The Cholesky QR algorithm is ideal from the viewpoint of high performance computing. It requires only one global reduction between parallel processing units,and most of the arithmetic work can be performed as matrix-matrix operations.However, the loss of orthogonality $\| I - Q _ { 1 } ^ { T } Q _ { 1 } \| _ { F }$ can only be bounded by the squared condition number of $A$

Yamamoto et al.[1136, 2015] suggest a modified Cholesky QR2 algorithm, where $R$ and $Q _ { 1 }$ from Cholesky QR are refined as follows.First,compute $E = Q _ { 1 } ^ { T } Q _ { 1 }$ and its Cholesky factorization $E = S ^ { T } S$ .The refined factorization is taken to be $A = P U$ ,where

$$
P = Q S ^ { - 1 } , \quad U = S R .
$$

This updating step doubles the arithmetic cost. The Cholesky QR2 algorithm has good stability properties provided the initial Cholesky factorization does not break down. However, the QR2 algorithm may fail for matrices with a condition number roughly greater than $\mathbf { u } ^ { - 1 / 2 }$

Yamazaki, Tomov,and Dongarra [1137, 2o15] extend the applicability of the Cholesky QR2 algorithm as follows. An initial Cholesky factorization of $R ^ { T } R = A ^ { T } A + s I$ is computed, where $s \geq 0$ is a shift that guarantees that the factorization runs to completion. Further, some intermediate results are accumulated in higher precision. The resulting Cholesky QR3 algorithm uses three Cholesky QR steps and yields a computed $Q$ with loss of orthogonality $\lVert I - Q _ { 1 } ^ { T } Q _ { 1 } \rVert _ { F }$ and residual $\| A - Q R \| _ { F } / \| A \| _ { F }$ of order u. See also Fukaya et al. [435, 2020].

# 4.3.5 - Multilinear and Tensor Calculus

In many science and engineering applications,the data encountered have a multidimensional structure with more than two dimensions. Consider vector spaces $X _ { 1 }$ ， $X _ { 2 } , \ldots$ ， $X _ { d }$ and $Y$ ，and let $x _ { \nu } \in X _ { \nu }$ . A function $A \colon X _ { 1 } \times X _ { 2 } \times \cdots \times X _ { d } \to Y$ is called $d$ -multilinearif itis linear in each of its arguments $x _ { i }$ separately. For example, the expression $( P x _ { 1 } ) ^ { T } Q x _ { 2 } + ( R x _ { 3 } ) ^ { T } S x _ { 4 }$ defines a four-linear function, mapping or operator, provided the constant matrices $P , Q , R , S$ have appropriate size. If $d = 2$ ,the term bilinear function is used.

Let $X _ { \nu } = \mathbb { R } ^ { n _ { \nu } }$ ， $\nu = 1 , 2 , \ldots , d$ ， $Y = \mathbb { R } ^ { m }$ ,and let $e _ { j _ { i } }$ be one of the basis vectors of $X _ { i }$ Thensuperscriptscanbeused todenotecoordinates inthesespaces.For example,@.jd denotes the ith coordinate of $A ( e _ { j _ { 1 } } , e _ { j _ { 2 } } , \dots , e _ { j _ { d } } )$ .Because of the linearity, the $i$ th coordinate of $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { d } )$ ， $x _ { \nu } \in X _ { \nu }$ ,reads

$$
\sum _ { j _ { 1 } = 1 } ^ { n _ { 1 } } \sum _ { j _ { 2 } = 1 } ^ { n _ { 2 } } \ldots \sum _ { j _ { k } = 1 } ^ { n _ { k } } a _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { d } } ^ { i } x _ { 1 } ^ { j _ { 1 } } x _ { 2 } ^ { j _ { 2 } } \ldots x _ { d } ^ { j _ { d } } .
$$

The following sum convention is often used. If an index occurs as both a subscript and a su-perscript, the product should be summed over the range of this index. For example, the ith coordinate of $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { d } )$ is writen $a _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { d } } ^ { i } x _ { 1 } ^ { j _ { 1 } } x _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot x _ { k } ^ { j _ { d } } .$ 2.. (Remember the superscripts are not exponents.)

Suppose $X _ { i } = X$ ， $i = 1 , 2 , \ldots , d$ 、Then the set of $d$ -linear mappings from $X ^ { k }$ to $Y$ is itself a linear space, denoted by $L _ { k } ( X , Y )$ . For $k = 1$ ,we have the space of linear functions.Linear functions can,of course, be described in vector-matrix notation as a set of matrices $L ( \mathbb { R } ^ { n } , \mathbb { R } ^ { m } ) =$ $\mathbb { R } ^ { m \times n }$ . Matrix notation can also be used for each coordinate of a bilinear function. Norms of multilinear operators are defined analogously to subordinate matrix norms. For example,

$$
\begin{array} { r } { \| A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { k } ) \| _ { \infty } \leq \| A \| _ { \infty } \| x _ { 1 } \| _ { \infty } \| x _ { 2 } \| _ { \infty } \ldots \| x _ { k } \| _ { \infty } , } \end{array}
$$

where

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { i = 1 } ^ { m } \sum _ { j _ { 1 } = 1 } ^ { n _ { 1 } } \sum _ { j _ { 2 } = 1 } ^ { n _ { 2 } } \cdot \cdot \cdot \sum _ { j _ { k } = 1 } ^ { n _ { k } } | a _ { j _ { 1 } , j _ { 2 } , \dots , j _ { k } } ^ { i } | .
$$

A multilinear function $A$ is called symmetric if $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { k } )$ is symmetric with respect to its arguments. In the cases mentioned above, where matrix notation can be used, the matrix becomes symmetric if the multilinear function is symmetric.

Multidimensional data can be represented by a tensor or, using a coordinate representation, a hypermatrix. Mathematical theory and computational methods for tensor problems are still being developed, and notation may vary among papers. In the following, we denote tensors by calligraphic letters; e.g., we refer to

$$
\mathcal { A } = ( a _ { i _ { 1 } , . . . , i _ { d } } ) \in \mathbb { R } ^ { n _ { 1 } \times \cdots \times n _ { d } }
$$

as a $d$ -mode tensor, $d > 2$ The case $d = 2$ corresponds to matrices. In the following we emphasize the case $d = 3$ because the main difference between matrices and hypermatrices comes in the transition from $d = 2$ to 3.Subarrays are formed by keeping a subset of the indices constant.A 3-mode tensor (4.3.38) can be thought of as being built up by matrix slices in three ways by fixing one of the indices, e.g.,

$$
\begin{array} { r } { ( a _ { : , : , j } ) \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } } , \quad j = 1 : n _ { 3 } . } \end{array}
$$

Similarly,by fixing any two indices, we get a vector or fiber

$$
\begin{array} { r } { ( a _ { : , j , k } ) \in \mathbb { R } ^ { n _ { 1 } } , \quad j = 1 : n _ { 2 } , \quad k = 1 : n _ { 3 } . } \end{array}
$$

A tensor is said to be symmetric if its elements are equal under any permutations of the indices, i.e., for a 3-mode tensor,

$$
a _ { i , j , k } = a _ { i , k , j } = a _ { j , k , i } = a _ { j , i , k } = a _ { k , i , j } = a _ { k , j , i } \ \forall { i , j , k } ;
$$

see Comon et al.[263,2oo8]. A tensor is diagonal if $a _ { i _ { 1 } , i _ { 2 } , \dots , i _ { d } } \neq 0$ only if $i _ { 1 } = i _ { 2 } = \cdot \cdot \cdot = i _ { d }$

Elementwise addition and scalar multiplication trivially extend to hypermatrices of arbitrary order. The tensor or outer product is denoted by $\circ$ (not to be confused with the Hadamard product of matrices). For example, if $A = ( a _ { i j } ) \in \mathbb { R } ^ { m \times n }$ and $B = ( b _ { k l } ) \in \mathbb { R } ^ { p \times q }$ are matrices, then

$$
\mathcal { C } = A \circ B = ( a _ { i , j , k , l } )
$$

is a 4-mode tensor. The 1-mode contraction product of two 3-mode hypermatrices ${ \mathcal { A } } =$ $( a _ { i , j , k } ) \in \mathbb { R } ^ { n \times n _ { 2 } \times n _ { 3 } }$ and $\boldsymbol { B } = ( b _ { i , l , m } ) \in \mathbb { R } ^ { n \times m _ { 2 } \times m _ { 3 } }$ with conforming first dimension is the 4-mode tensor $\mathcal { C } \in \mathbb { R } ^ { n _ { 2 } \times n _ { 3 } \times m _ { 2 } \times m _ { 3 } }$ defined as

$$
\mathcal { C } = \langle \mathcal { A } , \mathcal { B } \rangle _ { 1 } , \quad c _ { j , k , l , m } = \sum _ { i = 1 } ^ { n } a _ { i , j , k } b _ { i , l , m } .
$$

Contractions need not be restricted to one pair of indices at a time.The inner product of two 3-mode tensors of the same size and the Frobenius norm of a tensor are defined as

$$
\langle \boldsymbol { A } , \boldsymbol { B } \rangle = \sum _ { i , j , k } a _ { i j k } b _ { i j k } , \qquad \| \boldsymbol { A } \| _ { F } ^ { 2 } = \langle \boldsymbol { A } , \boldsymbol { A } \rangle ^ { 1 / 2 } = \sum _ { i , j , k } a _ { i j k } ^ { 2 } .
$$

The matrix Holder norm for $p = 1 , \infty$ is similarly generalized.

The columns of $A$ can be stacked or unfolded into a column vector by the operation $\mathrm { v e c } ( A )$ A second way would be to unfold its rows into a row vector. Similarly,a 3-mode tensor $\mathcal { A }$ can be unfolded or matricized by stacking in some order the matrix slices obtained by fixing one of its three modes.Following Eldén and Savas [380,2oog],we use the notation

$$
\begin{array} { r l } & { A _ { ( 1 ) } = ( A _ { : , 1 , : } , A _ { : , 2 , : } , \ldots , A _ { : , n _ { 2 } , : } ) \in \mathbb R ^ { n _ { 1 } \times n _ { 2 } n _ { 3 } } , } \\ & { A _ { ( 2 ) } = ( A _ { : , : , 1 } ^ { T } , A _ { : , : , 2 } ^ { T } , \ldots , A _ { : : , n _ { 3 } } ^ { T } ) \in \mathbb R ^ { n _ { 2 } \times n _ { 1 } n _ { 3 } } , } \\ & { A _ { ( 3 ) } = ( A _ { 1 , : , : } ^ { T } , A _ { 2 , : , : } ^ { T } , \ldots , A _ { n _ { 1 } , : , : } ^ { T } ) \in \mathbb R ^ { n _ { 3 } \times n _ { 1 } n _ { 2 } } , } \end{array}
$$

where a colon indicates all elements of a mode. Different papers sometimes use different orderings of the columns. The specific permutation is not important as long as it is consistent.

A matrix $C \in \mathbb { R } ^ { p \times q }$ can be multiplied from the left and right by other matrices $\ b X \in \mathbb { R } ^ { m \times p }$ and $Y \in \mathbb { R } ^ { n \times q }$ , and we write

$$
A = X C Y ^ { T } , \qquad a _ { i j } = \sum _ { \alpha = 1 } ^ { p } \sum _ { \beta = 1 } ^ { q } x _ { i \alpha } y _ { j \beta } c _ { \alpha \beta } .
$$

The corresponding tensor-matrix multiplication of a 3-mode tensor $\mathcal { C } \in \mathbb { R } ^ { p \times q \times r }$ by three matrices $\boldsymbol { X } \in \mathbb { R } ^ { l \times p }$ ， $Y \in \mathbb { R } ^ { m \times q }$ ,and $Z \in \mathbb { R } ^ { n \times r }$ transforms $\mathcal { C }$ into the 3-mode tensor $\mathcal { A } \in \mathbb { R } ^ { l \times m \times n }$ with entries

$$
a _ { i j k } = \sum _ { \alpha = 1 } ^ { p } \sum _ { \beta = 1 } ^ { q } \sum _ { \gamma = 1 } ^ { r } x _ { i , \alpha } y _ { j , \beta } z _ { k \gamma } c _ { \alpha \beta \gamma } .
$$

A notation for this operation suggested by Silva and Lim [993, 2008] is

$$
{ \mathcal { C } } = ( X , Y , Z ) \cdot A ,
$$

where the mode of each multiplication is understood from the ordering of the matrices. It is convenient to use a separate notation for multiplication by transposed matrices. For ${ \mathcal { C } } =$ $( X ^ { T } , Y ^ { T } , Z ^ { T } ) \cdot { \mathcal { A } }$ we also write

$$
{ \mathcal { C } } = { \mathcal { A } } \cdot ( X , Y , Z ) .
$$

For a matrix $A \in \mathbb { R } ^ { m \times n }$ there are three ways to define the rank $r$ ,all of which yield the same value. The rank is equal to the dimension of the subspace of $\mathbb { R } ^ { m }$ spanned by its columns and the dimension of the subspace of $\mathbb { R } ^ { n }$ spanned by its rows.Also,the rank is the minimum number of terms in the expansion of $A$ as a sum of rank-one matrices; cf. the SVD expansion. For a tensor of mode $d > 2$ ,these three definitions yield different results.

The column rank and row rank of a matrix are generalized as follows. For a 3-mode tensor $\mathcal { A } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } \times n _ { 3 } }$ ,let $r _ { 1 }$ be the dimension of the subspace of $\mathbb { R } ^ { n _ { 1 } }$ spanned by the $n _ { 2 } n _ { 3 }$ vectors with entries $a _ { : , i _ { 2 } , i _ { 3 } } , i _ { 2 } = 1 : n _ { 2 } , i _ { 3 } = 1 : n _ { 3 }$ . In other words, $r _ { 1 } ( \mathcal { A } ) = \mathrm { r a n k } ( A _ { ( 1 ) } )$ , with similar interpretations for $r _ { 2 }$ and $r _ { 3 }$ . The triple $( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ is called the multirank of $\mathcal { A }$ and $r _ { 1 } , r _ { 2 } , r _ { 3 }$ can all be different.

The outer product of vectors $\boldsymbol { x } \in \mathbb { R } ^ { \ell }$ ， $y \in \mathbb { R } ^ { m }$ ,and $z \in \mathbb { R } ^ { n }$ is the 3-mode hypermatrix

$$
\mathcal { T } = x \circ y \circ z \in \mathbb { R } ^ { l \times m \times n } , \quad t _ { i _ { 1 } i _ { 2 } i _ { 3 } } = x _ { i _ { 1 } } y _ { i _ { 2 } } z _ { i _ { 3 } } .
$$

If nonzero, we call this a rank-one tensor. The tensor rank of $\mathcal { A }$ is the smallest number $r$ such that $\mathcal { A }$ may be written as a sum of rank-one hypermatrices:

$$
\mathcal { A } = \sum _ { p = 1 } ^ { r } x _ { p } \circ y _ { p } \circ z _ { p } .
$$

When $d = 2$ this definition agrees with the usual definition of the rank of a matrix. Generalization of this definition of rank to higher order tensors is straightforward.However, for $d \geq 3$ there is no algorithm for determining the rank of a given tensor,and this problem is NP-hard.Furthermore, de Silva and Lim [993,2oo8] show that the problem of finding the best rank- $p$ approximation in general has no solution, even for $d = 3$

Tensor decompositions originated with Hitchcock [629,1927] and much later were taken up and used to analyze data in psychometrics (Tucker [1O70,1966]). In the last decades the use of tensor methods has spread to other fields,such as chemometrics (Bro [180,1997l),signal and image processing,data mining,and patern recognition (Eldén [376, 2o19]). Tensor decompositions are used in machine learning and parameter estimation.

Low-rank approximations of a given two-dimensional array of data can be found from the SVD of a matrix. In many applications one would like to approximate a given tensor $\mathcal { A }$ with a sum of rank-one tensors to minimize

$$
\left. \boldsymbol { \mathcal { A } } - \sum _ { i = 1 } ^ { p } \lambda _ { i } \boldsymbol { x } _ { i } \circ y _ { i } \circ z _ { i } \right. _ { F } .
$$

Weights $\lambda _ { i }$ are introduced to let us assume that vectors $x _ { i } , y _ { i }$ ，and $z _ { i }$ are normalized to have length one.Hillar and Lim [628,2O13] have shown that this problem (and indeed, most other tensor problems) are NP-hard. Therefore,we assume that the number $p < r$ of factors is fixed. A popular algorithm for computing such an approximate decomposition is alternating least squares (ALS). First, the vectors $y _ { i }$ and $z _ { i }$ are fixed, and $x _ { i }$ is determined to minimize (4.3.46). Next, $x _ { i } , z _ { i }$ are fixed,and we solve for $y _ { i }$ .Finally, $x _ { i } , y _ { i }$ are fixed,and we solve for $z _ { i }$ .Define the matrices

$$
\begin{array} { r } { X = ( x _ { 1 } , \dotsc , x _ { p } ) \in \mathbb { R } ^ { n _ { 1 } \times p } , \quad Y = ( y _ { 1 } , \dotsc , y _ { p } ) \in \mathbb { R } ^ { n _ { 2 } \times p } , \quad Z = ( z _ { 1 } , \dotsc , z _ { p } ) \in \mathbb { R } ^ { n _ { 3 } \times p } . } \end{array}
$$

With $y _ { i } , z _ { i }$ fixed, the minimizing problem can be written in matrix form as

$$
\operatorname* { m i n } _ { X } \| A _ { ( 1 ) } - \widehat { X } ( Z \odot Y ) ^ { T } \| _ { F } ,
$$

where $A _ { ( 1 ) } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } n _ { 3 } }$ is the matrix obtained by unfolding $\mathcal { A }$ along the first mode, and

$$
Z \odot Y = ( z _ { 1 } \otimes y _ { 1 } , \dots , z _ { p } \otimes y _ { p } ) \in \mathbb { R } ^ { n _ { 2 } n _ { 3 } \times p }
$$

is the matching columnwise Kronecker product, also called the Khatri-Rao product, of $Z$ and $Y$ The solution can be written

$$
\hat { X } = A _ { ( 1 ) } [ ( Z \odot Y ) ^ { T } ] ^ { \dagger } ,
$$

and then the columns of $\hat { X }$ are normalized to give $\hat { X } = X \mathrm { d i a g } \left( \lambda _ { i } \right)$ .Because of the special form of the Khatri-Rao product, the solution can also be written as

$$
\hat { X } = X _ { ( 1 ) } ( Z \odot Y ) ( Z ^ { T } Z . * Y ^ { T } Y ) ^ { \dagger } ,
$$

where $^ *$ is the Hadamard (elementwise） matrix product. This version is not always suitable because of the squared condition number. Similar formulas for the two other modes are easily derived. At each inner iteration a pseudoinverse must be computed. ALS can take many iterations and is not guaranteed to converge to a global minimum. Also,the solution obtained depends on the starting point.

The idea of expressing a tensor as a sum of rank-one tensors has been proposed under different names by several authors. In psychometrics it was called CANDECOMP (canonical decom-position) and PARAFAC (parallel factors); see Kolda and Bader [7O5, 2oo9]. Here, following Leurgans,Ross,and Abel [735,1993l, we callit the CP decomposition. In matrix computations, the SVD expansion

$$
A = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { r } \sigma _ { i } u _ { i } v _ { i } ^ { T } \in \mathbb { R } ^ { m \times n } , \quad r \leq \operatorname* { m i n } \{ m , n \} ,
$$

expresses a matrix $A$ of rank $r$ as the weighted sum of rank-one matrices $u _ { i } v _ { i } ^ { T }$ ,where $u _ { i } \in \mathbb { R } ^ { m }$ and $v _ { i } \in \mathbb { R } ^ { n }$ ， $i = 1 : r$ ，are mutually orthogonal. This expansion has the desirable property that for any unitarily invariant norm, the best approximation of $A$ by a matrix of rank $r < n$ is obtained by truncating the expansion; see the Eckart-Young-Mirksy Theorem 1.3.8.

The high-order SVD (HOSVD) is a generalization of the SVD to 3-mode hypermatrices

$$
\mathcal { A } = \left( U , V , W \right) \cdot \mathcal { C } ,
$$

where $U , V$ ，and $W$ are square and orthogonal, and $\mathcal { C }$ has the same size as $\mathcal { A }$ .Further, the different matrix slices of $\mathcal { C }$ are mutually orthogonal (with respect to the standard inner product on matrix spaces） and with decreasing Frobenius norm. Because of the imposed orthogonality conditions, the HOsVD of $\mathcal { A }$ is essentially unique. It is rank-revealing in the sense that if $\mathcal { A }$ has multirank $( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ , then the last $n _ { 1 } - r _ { 1 } , n _ { 2 } - r _ { 2 }$ and $n _ { 3 } - r _ { 3 }$ slices along the different modes of the core tensor $\mathcal { C }$ are zero matrices. Algorithms for computing the HOsVD are described by Lathauwer,De Moor, and Vandewalle [296, 2ooo]. The matrix $U$ is obtained from the SVD of the $l \times m n$ matrix obtained from unfolding ${ \mathcal { A } } , V$ and $W$ are obtained similarly. Since $U , V$ ,and $W$ are orthogonal, $\mathcal { C } = \left( c _ { i j k } \right)$ is easily computed from $\mathcal { C } = ( U ^ { T } , V ^ { T } , W ^ { T } ) \cdot \mathcal { A }$

Suppose we want to approximate tensor $\mathcal { A }$ by another tensor $\boldsymbol { B }$ of lower multirank. Then we want to solve

$$
\operatorname* { m i n } _ { \operatorname { r a n k } ( \mathcal { B } ) = ( p , q , r ) } \| \mathcal { A } - \mathcal { B } \| _ { F } ,
$$

where the Frobenius tensor norm is defined as in (4.3.4O).This is the basis of the Tucker model [1O7O,1966]. Unlike the matrix case,this problem cannot be solved by truncating the HOSVD of $\mathcal { A }$ .It is no restriction to assume that $\boldsymbol { \mathcal { B } } \ : = \ : ( \boldsymbol { U } , \boldsymbol { V } , \boldsymbol { W } ) \cdot \boldsymbol { \mathcal { C } }$ ，where $U \in \mathbb { R } ^ { n \times p }$ ， $V \in \mathbb { R } ^ { n _ { 2 } \times q }$ ,and $W \in \mathbb { R } ^ { n _ { 3 } \times p }$ are orthogonal matrices. Because of the orthogonal invariance of the Frobenius norm, $U , V$ ,and $W$ are only determined up to a rotation. With the core tensor $\mathcal { C }$ eliminated, problem (4.3.48) can be rewritten as a maximization problem with objective function

$$
\Phi ( U , V , W ) = \frac { 1 } { 2 } \big \| ( U ^ { T } , V ^ { T } , W ^ { T } ) \cdot \boldsymbol { \mathcal { A } } \big \| _ { F } ^ { 2 }
$$

subject to $U ^ { T } U = I$ $V ^ { T } V = I$ ,and $W ^ { T } W = I$ (compare with the corresponding matrix problem for $d = 2$ ). This can be formulated and solved as an optimization problem on a Grassmann manifold; see Eldén and Savas [380, 2oog] and Savas and Lim [968,2010].

# Notes and references

An extensive survey of tensor methods is given by Kolda and Bader [7O5, 2oog]. The theory of tensors and hypermatrices is surveyed by Lim [747,2o13]. An introduction to the theory and computation of tensors is given by Wei and Ding [1114,2o16]. Tensor rank problems are studied by de Silva and Lim [993,20o8] and Comen et al. [264,20o9]. A tutorial on CP decomposition and its applications is given by Bro [180,1997]. The N-way Toolbox for MATLAB (Andersson and Bro [28,2oool) for analysis of multiway data can be downloaded from http://www.models.kvl.dk/source/. MATLAB tools for tensor computations have also been developed by Bader and Kolda [52,2oo6],[53,20o7]. A MATLAB Tensor toolbox supported by Sandia National Labs and MathSci.ai is available on the web.Hankel tensors arise from signal processing and data fiting; see Papy, De Lauthauwer, and Van Huffel [878, 2005]. Tensors with Cauchy structure are also of interest; see Chen,Li,and Qi [240, 2016].

# 4.4 - Total Least Squares

# 4.4.1- Errors-in-Variables Models

In the standard linear model it is assumed that the observed vector $b \in \mathbb { R } ^ { m }$ is related to the unknown parameter vector $x$ by the linear equation $A x = b + e$ ,where $A \in \mathbb { R } ^ { m \times n }$ is known and $e$ is a vector of random errors.If the components of $e$ are uncorrelated and have zero means and the same variance,then by the Gauss-Markov theorem (Theorem 1.1.4) the best linear unbiased estimate of $x$ is given by the solution of the least squares problem

$$
\operatorname* { m i n } _ { r } \| r \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b + r .
$$

The assumption that all errors are confined to $b$ is frequently unrealistic. Sampling or modeling errors will often affect both $A$ and $b$ . In the errors-in-variables model it is assumed that

$$
( A + E ) x = b + f ,
$$

where the rows of the error matrix $\textbf { ( } E \textbf { ~ } f \textbf { ) }$ are independently and identically distributed with zero mean and the same variance. This model has independently been developed in statistics, where it is known as “latent root regression.” The optimal estimates of the parameters $x$ in this model satisfy the total least squares7 (TLS) problem

$$
\operatorname* { m i n } _ { E , f } \parallel ( E \quad f ) \parallel _ { F } \quad \mathrm { s u b j e c t t o } \quad ( A + E ) x = b + f ,
$$

where $\| \cdot \| _ { F }$ denotes the Frobenius matrix norm. The TLS problem is equivalent to finding the “nearest’consistent linear system, where the distance is measured in the Frobenius norm of $\left( \begin{array} { l l } { E } & { f } \end{array} \right)$ . When a minimizing perturbation has been found, any $x$ satisfying (4.4.2) is said to solve the TLS problem.

A complete and rigorous treatment of both theoretical and computational aspects of the TLS problem is developed in the monograph by Van Huffel and Vandewalle [1O77,1991]. They find that in typical applications, gains of $1 0 { - } 1 5 \%$ in accuracy can be obtained by using TLS instead of standard least squares methods.

The TLS solution depends on the relative scaling of the data $A$ and $b$ .Paige and Strakos [867, 2002] study the scaled TLS(STLS) problem

$$
\operatorname* { m i n } _ { E , f } \parallel ( E \quad \gamma f ) \parallel _ { F } \quad \mathrm { s u b j e c t t o } \quad ( A + E ) x = b + f ,
$$

where $\gamma$ is a given positive scaling parameter. For small values of $\gamma$ ，perturbations in $b$ will be favored. In the limit when $\gamma  0$ in (4.4.4), the solution equals the ordinary least squares

solution.On the other hand, large values of $\gamma$ favor perturbations in $A$ .In the limit when $1 / \gamma \to 0$ , we obtain the data least squares (DLS) problem

$$
\operatorname* { m i n } _ { E } \| E \| _ { F } \quad { \mathrm { s u b j e c t ~ t o } } \quad ( A + E ) x = b ,
$$

where perturbations are restricted to the data matrix $A$

# 4.4.2 - Total Least Squares and SVD

Writing the constraint $( A + E ) x = b + f$ as

$$
\begin{array} { r } { ( A + E \quad b + f ) \left( \begin{array} { c } { x } \\ { - 1 } \end{array} \right) = 0 } \end{array}
$$

shows that the matrix $\left( { \begin{array} { l l } { A + E } & { b + f } \end{array} } \right)$ is rank-deficient and that $\begin{array} { r l } { \left( x ^ { T } } & { { } - 1 \right) ^ { T } } \end{array}$ is a right singular vector corresponding to a zero singular value. The TLS problem can be analyzed in terms of the SVD

$$
C = ( \boldsymbol { A } \quad \boldsymbol { b } ) = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n + 1 } \sigma _ { i } u _ { i } v _ { i } ^ { T } .
$$

Assume that $\sigma _ { n + 1 } > 0$ . Then,by the Eckart-Young-Mirsky theorem (Theorem 1.3.8) the unique perturbation $\scriptscriptstyle \left( E \_ f \right)$ of minimum Frobenius norm that makes $( A + E ) x = b + f$ consistent is the rank-one perturbation

$$
\begin{array} { r l } { ( E } & { { } f ) = - \sigma _ { n + 1 } u _ { n + 1 } v _ { n + 1 } ^ { T } , } \end{array}
$$

ind $\begin{array} { r } { \operatorname* { m i n } _ { E , f } \| ( E \textrm { ~ \textit { f } } ) \| _ { F } = \sigma _ { n + 1 } } \end{array}$ .Multiplying (4.4.8) from the right with $v _ { n + 1 }$ and using 4.4.7) gives

$$
\left( \begin{array} { l l } { E } & { f } \end{array} \right) v _ { n + 1 } = - \sigma _ { n + 1 } u _ { n + 1 } = - \left( \begin{array} { l l } { A } & { b } \end{array} \right) v _ { n + 1 } ,
$$

i.e., $\begin{array} { r l } { ( A + E } & { { } b + f ) v _ { n + 1 } = 0 } \end{array}$ If $v _ { n + 1 , n + 1 } \neq 0$ ,the problem is called generic, and the TLS solution is obtained by scaling $v _ { n + 1 }$ so that its last component is $- 1$ ：

$$
\binom { x } { - 1 } = - \frac { 1 } { \gamma } v _ { n + 1 } , \quad \gamma = e _ { n + 1 } ^ { T } v _ { n + 1 } .
$$

Otherwise, the TLS problem has no solution and is called nongeneric.

Let $\hat { \sigma } _ { i }$ ， $i = 1 , \ldots , n$ ,be the singular values of $A$ . By Theorem 1.3.5 these interlace the singular values of $( A b )$ ：

$$
\sigma _ { 1 } \geq \hat { \sigma } _ { 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq \hat { \sigma } _ { n } \geq \sigma _ { n + 1 } .
$$

The condition $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ ensures that $A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I$ is symmetric positive definite and that the TLS problem has a unique solution.

If $A$ is rank-deficient, then so is $( A b )$ ，and $\hat { \sigma } _ { n } = \sigma _ { n + 1 } = 0$ Assume now that $\sigma _ { p } >$ $\sigma _ { p + 1 } = \cdot \cdot \cdot = \sigma _ { n + 1 }$ for some $p < n$ .Let $V _ { 2 } = ( v _ { p + 1 } , \ldots , v _ { n + 1 } )$ be the corresponding right singular vectors. Then the minimum is attained for any rank-one perturbation of the form

$$
\begin{array} { r } { \left( \begin{array} { l l } { E } & { f } \end{array} \right) = - \left( \begin{array} { l l } { \boldsymbol A + E } & { \boldsymbol b + f } \end{array} \right) \boldsymbol v \boldsymbol v ^ { T } , \quad \boldsymbol v = V _ { 2 } \boldsymbol z . } \end{array}
$$

Assume that a unit vector $z$ can be found such that

$$
V _ { 2 } z = { \binom { y } { \gamma } } , \quad \gamma \neq 0 .
$$

Then $x = - \gamma ^ { - 1 } y$ is a TLS solution. In this case the TLS solution is not unique. A unique TLS solution of least-norm can be found as follows. Since $V _ { 2 } z$ has unit length, minimizing $\| x \| _ { 2 }$ is equivalent to choosing the unit vector $z \in \mathbb { R } ^ { n - p + 1 }$ to maximize $\gamma$ in (4.4.11). Set $z = Q e _ { 1 }$ ， where $Q$ is a Householder reflector such that

$$
V _ { 2 } Q = \left( { \begin{array} { c c } { { y } } & { { { \hat { V } } _ { 2 } } } \\ { { \gamma } } & { { 0 } } \end{array} } \right) .
$$

Then the least-norm TLS solution is $x = - \gamma ^ { - 1 } y$ f $e _ { n + 1 } ^ { T } V _ { 2 } \ = \ 0$ ， then the TLS problem is nongeneric. This case can only occur when $\hat { \sigma } _ { n } = \sigma _ { n + 1 }$ .By an argument similar to that for $p = n$ ,it then holds that $b \perp u _ { j }$ ， $j = p : n$ . Nongeneric TLS problems can be treated by adding constraints on the solution; see Van Huffel and Vandewalle [1O77,1991].

From the relationship between the SVD of $\widetilde { A } = \left( A \quad b \right)$ and the eigendecomposition of the symmetric matrix $\widetilde { A } ^ { T } \widetilde { A }$ (see Section 1.2.2) it follows that the TLS solution $x$ can be characterized by

$$
\left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } b } } \\ { { b ^ { T } A } } & { { b ^ { T } b } } \end{array} \right) v = \sigma _ { n + 1 } ^ { 2 } v , \quad v = \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) ,
$$

where $\sigma _ { n + 1 } ^ { 2 }$ is the smallest eigenvalue of the matrix $\widetilde { A } ^ { T } \widetilde { A }$ ,and $v$ is a corresponding eigenvector. From (4.4.12) it follows that

$$
\begin{array} { r } { ( A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I _ { n } ) x = A ^ { T } b , \qquad b ^ { T } ( b - A x ) = \sigma _ { n + 1 } ^ { 2 } . } \end{array}
$$

In the first equation of (4.4.13) a positive multiple of the unit matrix is subtracted from the matrix of normal equations $A ^ { T } A x = A ^ { T } b$ ，This shows that TLS can be considered as a procedure for deregularizing the LS problem. (Compare with Tikhonov regularization, where a multiple of the unit matrix is added to improve the conditioning;see Section 3.5.3.） From a statistical point of view, TLS can be interpreted as removing bias by subtracting the error covariance matrix estimated by $\sigma _ { n + 1 } ^ { 2 } I$ from the data covariance matrix $A ^ { T } A$

Because of the nonlinear dependence of $x _ { \mathrm { { T L S } } }$ on the data $A , \ b$ ,a strict analysis of the sensitivity and conditioning of the TLS problem is more complicated than for the least squares problem. Golub and Van Loan [511,198o] show that an approximate condition number for the TLS problem is

$$
\kappa _ { T L S } ( A b ) = \kappa ( A ) \frac { \hat { \sigma } _ { n } } { \hat { \sigma } _ { n } - \sigma _ { n + 1 } } .
$$

This shows that the condition number for the TLS problem willbe much larger than $\kappa ( A )$ when the relative distance $1 - \sigma _ { n + 1 } / \hat { \sigma } _ { n }$ between $\sigma _ { n + 1 }$ and $\hat { \sigma } _ { n }$ is small. Subtracting the normal equations from (4.4.13), we obtain

$$
x _ { \mathrm { T L S } } - x _ { \mathrm { L S } } = \sigma _ { n + 1 } ^ { 2 } ( A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I ) ^ { - 1 } x _ { \mathrm { L S } } ,
$$

where $x _ { \mathrm { { T L S } } }$ and $x _ { \mathrm { L S } }$ denote the TLS and LS solutions. Taking norms in (4.4.15), we obtain the upper bound

$$
\| x _ { \mathrm { T L S } } - x _ { \mathrm { L S } } \| _ { 2 } \leq \frac { \sigma _ { n + 1 } ^ { 2 } } { \hat { \sigma } _ { n } ^ { 2 } - \sigma _ { n + 1 } ^ { 2 } } \| x _ { \mathrm { L S } } \| _ { 2 } \leq \frac { \sigma _ { n + 1 } } { 2 ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) } \| x _ { \mathrm { L S } } \| _ { 2 } ,
$$

where the last inequality follows from

$$
\hat { \sigma } _ { n } ^ { 2 } - \sigma _ { n + 1 } ^ { 2 } = ( \hat { \sigma } _ { n } + \sigma _ { n + 1 } ) ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) \geq 2 \sigma _ { n + 1 } ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) .
$$

From this we deduce that when the errors in $A$ and $b$ are small the difference between the LS and TLS solutions is small. Otherwise,the solutions can differ considerably.

In many parameter estimation problems,some of the columns of $A$ are known exactly. It is no loss of generality to assume that the $n _ { 1 }$ error-free columns are the first in $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right) \in$ $\mathbb { R } ^ { m \times n }$ ， $n = n _ { 1 } + n _ { 2 }$ . The mixed LS-TLS model is

$$
\left( A _ { 1 } \quad A _ { 2 } + E _ { 2 } \right) { \binom { x _ { 1 } } { x _ { 2 } } } = b + f , \qquad A _ { 1 } \in \mathbb { R } ^ { m \times n _ { 1 } } ,
$$

where the rows of the errors $\left( \begin{array} { l l } { E _ { 2 } } & { f } \end{array} \right)$ are independently and identically distributed with zero mean and the same variance.The problem can then be expressed as

$$
\operatorname* { m i n } _ { E _ { 2 } , f } \Vert \left( E _ { 2 } \quad f \right) \Vert _ { F } , \qquad \left( A _ { 1 } \quad A _ { 2 } + E _ { 2 } \right) \binom { x _ { 1 } } { x _ { 2 } } = b + f .
$$

When $A _ { 2 }$ is empty, this reduces to solving an ordinary least squares problem with multiple right-hand sides.When $A _ { 1 }$ is empty,this is the standard TLS problem.When the columns of $A _ { 1 }$ are linearly independent, the mixed LS-TLS can be solved as a two-block problem; see Section 4.3.1. First, compute the QR factorization

$$
Q ^ { T } \left( \begin{array} { l l l } { A _ { 1 } } & { A _ { 2 } } & { b } \end{array} \right) = \left( \begin{array} { c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { c _ { 1 } } \\ { 0 } & { R _ { 2 2 } } & { c _ { 2 } } \end{array} \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 1 } }$ is upper triangular and $R _ { 2 2 } \ \in \ \mathbb { R } ^ { ( m - n _ { 1 } ) \times n _ { 2 } }$ . Next, compute $x _ { 2 }$ as the solution to the TLS problem

$$
\operatorname* { m i n } _ { E , G } \parallel ( E _ { \mathrm { ~ \it ~ \ / ~ g ~ } } ) \parallel _ { F } , \qquad ( R _ { 2 2 } + E ) x _ { 2 } = c _ { 2 } + g .
$$

Finally, $x _ { 1 }$ is obtained from the triangular system $R _ { 1 1 } x _ { 1 } = c _ { 1 } - R _ { 1 2 } x _ { 2 }$

# 4.4.3 - Multidimensional TLS

In this section we consider some generalizations of the TLS problem. The errors-in-variable model has been used in statistics for a long time.Multivariate problems were treated much later in the statistical literature.In the multidimensional TLS problem with multiple right-hand sides $B = ( b _ { 1 } , \ldots , b _ { d } ) \in \mathbb { R } ^ { m \times d }$ ， $d > 1$ ,the rows of $\left( \begin{array} { l l } { A } & { B } \end{array} \right)$ are assumed to be independently and identically distributed with zero mean and the same variance:

$$
\operatorname* { m i n } _ { E , F } \| \left( E \quad F \right) \| _ { F } , \qquad ( A + E ) X = B + F .
$$

Hence we consider perturbations $\left( \begin{array} { l l } { E } & { F } \end{array} \right)$ such that

$$
\begin{array} { r } { ( A + E \quad B + F ) \left( \begin{array} { c } { X } \\ { - I _ { d } } \end{array} \right) = 0 . } \end{array}
$$

Note that $A$ is similarly perturbed for all right-hand sides.Hence,the multidimensional TLS problem is different from separately solving $d$ one-dimensional TLS problems with right-hand sides $b _ { 1 } , \ldots , b _ { d }$ .This gives improved predictive power of the multidimensional TLS solution.

The solution to the multidimensional TLS problem can be expressed in terms of the SVD

$$
\boldsymbol { C } = \left( \boldsymbol { A } \quad \boldsymbol { B } \right) = \boldsymbol { U } \boldsymbol { \Sigma } \boldsymbol { V } ^ { T } = \boldsymbol { U } _ { 1 } \boldsymbol { \Sigma } _ { 1 } \boldsymbol { V } _ { 1 } ^ { T } + \boldsymbol { U } _ { 2 } \boldsymbol { \Sigma } _ { 2 } \boldsymbol { V } _ { 2 } ^ { T } ,
$$

where $\Sigma _ { 1 } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { n } \right)$ ， $\Sigma _ { 2 } = \operatorname { d i a g } \left( \sigma _ { n + 1 } , \ldots , \sigma _ { n + d } \right)$ . By the Eckart-Young-Mirsky theorem, $\| \left( \begin{array} { l l } { E } & { F } \end{array} \right) \| _ { F } ^ { 2 }$ is minimized for the perturbation

$$
\begin{array} { r } { \left( \begin{array} { l l } { E } & { F } \end{array} \right) = - U _ { 2 } \Sigma _ { 2 } V _ { 2 } ^ { T } = - C V _ { 2 } V _ { 2 } ^ { T } , } \end{array}
$$

$\scriptstyle \sum _ { i = n + 1 } ^ { n + d } { \boldsymbol { \sigma } } _ { i } ^ { 2 }$ Ii $\sigma _ { n } ~ > ~ \sigma _ { n + 1 }$ $V _ { 2 }$

$$
V _ { 2 } = { \binom { V _ { 1 2 } } { V _ { 2 2 } } }
$$

and $V _ { 2 2 } \in \mathbb { R } ^ { d \times d }$ is nonsingular,then the TLS solution is

$$
\begin{array} { r } { X = - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } = ( A ^ { T } A - \sigma _ { n + 1 } I ) ^ { - 1 } A ^ { T } B \in \mathbb { R } ^ { n \times d } . } \end{array}
$$

The last formula generalizes (4.4.13). For $d = 1$ , we recover the previous expression (4.4.10) for the TLS solution.

We now show that if $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ , then $V _ { 2 2 }$ is nonsingular. From (4.4.20) it follows that

$$
A V _ { 1 2 } + B V _ { 2 2 } = U _ { 2 } \Sigma _ { 2 } .
$$

If $V _ { 2 2 }$ is singular, then $V _ { 2 2 } z = 0$ for some unit vector $z$ ,and hence $U _ { 2 } \Sigma _ { 2 } z = A V _ { 1 2 } z$ From

$$
V _ { 2 } ^ { T } V _ { 2 } = V _ { 1 2 } ^ { T } V _ { 1 2 } + V _ { 2 2 } ^ { T } V _ { 2 2 } = I
$$

it follows that $V _ { 2 2 } ^ { T } V _ { 2 2 } z = z$ and $\| V _ { 2 2 } x \| _ { 2 } = 1$ . But then

$$
\sigma _ { n + 1 } \geq \| U _ { 2 } \Sigma _ { 2 } x \| _ { 2 } = \| A V _ { 1 2 } x \| _ { 2 } \geq \hat { \sigma } _ { n } .
$$

This is a contradiction,and hence $V _ { 2 2 }$ is nonsingular.

A unique solution to the multidimensional TLS problem exists if $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ .If this condition is not satisfied, then the TLS problem can stillhave a solution, but it is no longer unique. As for the case $d = 1$ ,we then seek a solution of minimum norm $\| X \| _ { F }$ .Wei [1112,1992] shows that a sufficient condition for a least-norm multidimensional TLS solution to exist is that

$$
\hat { \sigma } _ { p } > \sigma _ { p + 1 } = \cdot \cdot \cdot = \sigma _ { n } = \cdot \cdot \cdot = \sigma _ { n + d } .
$$

When this condition is satisfied,the following extension of the classical SVD algorithm computes the least-norm solution; see Van Huffel and Vandevalle [1077,1991, Section 3.6.1].For $d = 1$ and $p = n$ the algorithm coincides with the classical SVD algorithm described earlier.

# Algorithm 4.4.1.

Given a data matrix $A \in \mathbb { R } ^ { m \times n }$ and an observation matrix $B \in \mathbb { R } ^ { m \times d }$ , do the following:

1. Compute the SVD of the extended matrix $C = ( \boldsymbol { A } \quad \boldsymbol { B } ) \in \mathbb { R } ^ { m \times ( n + d ) } .$

$$
C = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n + d } u _ { i } \sigma _ { i } v _ { i } ^ { T } .
$$

2. Suppose $p \leq \operatorname* { m i n } \{ n , \operatorname { r a n k } ( C ) ) \}$ , and partition $V$ so that

$$
V = \stackrel { n } { d } \left( \stackrel { p } { V _ { 2 1 } } \stackrel { q } { V _ { 2 2 } } \right) \in \mathbb { R } ^ { ( n + d ) \times ( n + d ) } ,
$$

where $V _ { 1 1 } \in \mathbb { R } ^ { n \times p }$ and $V _ { 2 2 } \in \mathbb { R } ^ { d \times q }$ ， $q = n - p + d $

3.If $V _ { 2 2 } = 0$ ，then the problem is nongeneric. Otherwise,if $V _ { 2 2 }$ has full row rank, compute the least-norm TLS solution as

$$
X = - V _ { 1 2 } V _ { 2 2 } ^ { \dag } = ( V _ { 1 1 } ^ { T } ) ^ { \dag } V _ { 2 1 } ^ { T } .
$$

From the CS decomposition it follows that if $V _ { 2 2 }$ has full column rank,then so has $V _ { 1 1 }$ For a proof of the equivalence of the formulas in (4.4.25),see Van Huffel and Vandevalle[1077, 1991,Theorem 3.10]. The second expression for $X$ only requires computation of the $k$ largest right singular vectors of $( A b )$ and is advantageous when $k$ is small.

Algorithm 4.4.1 for solving the multidimensional TLS problem only requires a small part of the full SVD, namely the $d \ll n$ right singular vectors corresponding to the smallest singular values. For this purpose Van Huffel, Vandewalle,and Haegemans [1O78,1987] developed a modified partial QRSVD (PSVD) algorithm. In the Householder bidiagonalization phase the singular vectors $U$ and $V$ are initialized by the accumulated products of the Householder reflections.During the QRSVD iterations, plane rotations are applied to $U$ and $V$ to generate the left and right singular values. A great amount of work is saved in the PSVD algorithm by delaying the initializing of $U$ and $V$ until the end of the diagonalizing phase.The Householder reflections are then applied only to the (small number of) desired singular vectors of the bidiagonal matrix. A second modification in PSVD is to perform only a partial diagonalization of the bidiagonal matrix.The iterative process is stopped as soon as convergence has occurred to all desired singular values. Assume that at the $i$ th step of the diagonalization phase,we have the block bidiagonal form

$$
B ^ { ( i ) } = \left( \begin{array} { c c c c c } { { B _ { 1 } ^ { ( i ) } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { B _ { 2 } ^ { ( i ) } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { B _ { s } ^ { ( i ) } } } \end{array} \right) ,
$$

where $B _ { j } ^ { ( i ) }$ $j = 1 , \dots , s$ areunreducedupperbidiagonalmatrices.Supposethatabasisfora singular subspace corresponding to the singular values $\sigma _ { i } \leq \theta$ is desired. Then spectrum slicing (see Section 7.2.1) can be used to partition these blocks into three classes:

$$
\begin{array} { r l } & { C _ { 1 } = \{ B _ { j } \mid \mathrm { a l l ~ s i n g u l a r ~ v a l u e s } > \theta \} , } \\ & { C _ { 2 } = \{ B _ { j } \mid \mathrm { a l l ~ s i n g u l a r ~ v a l u e s } \leq \theta \} , } \\ & { C _ { 3 } = \{ B _ { j } \mid \mathrm { a t ~ l e a s t ~ o n e ~ s i n g u l a r ~ v a l u e } > \theta \mathrm { a n d ~ a t ~ l e a s t ~ o n e } \leq \theta \} . } \end{array}
$$

If $C _ { 3 }$ is empty, then the algorithm stops. Otherwise, one QR iteration is applied to each block in $C _ { 3 }$ ,and the partition is reclassified. If no bound on the singular values can be given but, instead, the dimension $p$ of the desired subspace is known, then a bound $\theta$ can be computed with the bisection method from Section 7.2.1. A complete description of the PSVD algorithm is given in Van Huffel and Vandevalle [1077,1991, Section 4.3]. A Fortran 77 implementation of PSVD is available from Netlib.

# 4.4.4 - Solving Large-Scale TLS Problems

For large or structured TLS problems,computing the PSVD may be prohibitive because the sparsity or structure of the matrix is lost in the reduction to bidiagonal form. Then an iterative algorithm may be advantageous. Similarly, this applies when a sequence of slowly varying TLS problems has to be solved. In this case the solution of the previous problem can be used as an initial approximation.

Let $\sigma _ { n + 1 } ^ { 2 }$ be the smallest eigenvalue of $\widetilde { A } ^ { T } \widetilde { A }$ where $\widetilde { \cal A } = ( \cal { A } b )$ If $\begin{array} { r l } { \left( x ^ { T } } & { { } - 1 \right) ^ { T } } \end{array}$ is a corresponding eigenvector, then

$$
\widetilde { A } ^ { T } \widetilde { A } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = \sigma _ { n + 1 } ^ { 2 } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) .
$$

This characterization of the TLS solution suggests the following alternative formulation of the TLS problem. The unique minimum $\sigma _ { n + 1 } ^ { 2 }$ of the Rayleigh quotient $\rho ( x ) = v ^ { T } \widetilde { A } v / \| v \| _ { 2 } ^ { 2 }$ , where

$$
{ \widetilde { A } } = \left( A \quad b \right) , \qquad v = \left( { x \atop - 1 } \right) ,
$$

is attained for $x = x _ { T L S }$ . Hence the TLS problem is equivalent to $\operatorname* { m i n } _ { x } \rho ( x )$ , where

$$
\rho ( x ) = \frac { \| r \| _ { 2 } ^ { 2 } } { \| x \| _ { 2 } ^ { 2 } + 1 } , \quad r = - \widetilde { A } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = b - A x .
$$

In the algorithm of Bjorck, Heggernes,and Matstoms [147,2ooo] the TLS solution $x$ is computed by applying inverse iteration to the symmetric eigenvalue problem (4.4.26). Let $x ^ { ( k ) }$ be the current approximation. Then $x ^ { ( k + 1 ) }$ and the scalars $\beta _ { k } , k = 0 , 1 , 2 , \ldots$ ,are computed by solving

$$
\widetilde { A } ^ { T } \widetilde { A } \left( { \begin{array} { c } { x ^ { ( k + 1 ) } } \\ { - 1 } \end{array} } \right) = \beta _ { k } \left( { \begin{array} { c } { x ^ { ( k ) } } \\ { - 1 } \end{array} } \right) .
$$

If the compact QR factorization

$$
\begin{array} { r } { \widetilde { A } = \left( A \begin{array} { l l } { b } & { b } \end{array} \right) = Q \left( \begin{array} { l l } { R } & { c } \\ { 0 } & { \eta } \end{array} \right) , \quad Q \in \mathbb { R } ^ { m \times ( n + 1 ) } , } \end{array}
$$

is known,then the solution of (4.4.28)is obtained by solving the two triangular systems

$$
\begin{array} { r l } { \left( \begin{array} { c c } { R ^ { T } } & { 0 } \\ { c ^ { T } } & { \eta } \end{array} \right) \left( \begin{array} { c } { z ^ { ( k ) } } \\ { - \gamma _ { k } } \end{array} \right) = \left( \begin{array} { c } { x ^ { ( k ) } } \\ { - 1 } \end{array} \right) , } & { { } \qquad \left( \begin{array} { c c } { R } & { c } \\ { 0 } & { \eta } \end{array} \right) \left( \begin{array} { c } { x ^ { ( k + 1 ) } } \\ { - 1 } \end{array} \right) = \beta _ { k } \left( \begin{array} { c } { z ^ { ( k ) } } \\ { - \gamma _ { k } } \end{array} \right) . } \end{array}
$$

After eliminating $\gamma _ { k }$ , this becomes

$$
x ^ { ( k + 1 ) } = x _ { L S } + \beta _ { k } R ^ { - 1 } ( R ^ { - T } x ^ { ( k ) } ) , \quad \beta _ { k } = \eta ^ { 2 } / ( 1 + x _ { L S } ^ { T } x ^ { ( k ) } ) .
$$

The iterations are initialized by taking

$$
x ^ { ( 0 ) } = x _ { L S } = R ^ { - 1 } c , \quad \beta _ { 0 } = \eta ^ { 2 } / ( 1 + \| x _ { L S } \| ^ { 2 } ) .
$$

From classical convergence results for symmetric inverse iteration it follows that

$$
| | x ^ { ( k ) } - x _ { T L S } | | _ { 2 } = O ( ( \sigma _ { n + 1 } / \sigma _ { n } ) ^ { 2 k } ) , \qquad | \rho ( x ^ { ( k ) } ) - \sigma _ { n + 1 } ^ { 2 } | = O ( ( \sigma _ { n + 1 } / \sigma _ { n } ) ^ { 4 k } ) .
$$

By using Rayleigh-quotient iteration (RQI), a better rate of convergence can be obtained. For properties of the Rayleigh quotient of symmetric matrices, see Section 7.3.1.

Fasino and Fazzi [398,2o18] note that by the characterization (4.4.27) the TLS problem is equivalent to the nonlinear least squares problem $\operatorname* { m i n } _ { x } \| f ( x ) \| _ { 2 }$ ，where

$$
f ( x ) = \mu ( x ) ( b - A x ) , \quad \mu ( x ) = ( 1 + x ^ { T } x ) ^ { - 1 / 2 } ,
$$

and solved by a Gauss-Newton method (see Section 8.1.2). If $x _ { k }$ is the current approximation, this requires solution of a sequence of linear least squares problems

$$
\operatorname* { m i n } _ { h _ { k } } \| f ( x _ { k } ) + h _ { k } J ( x _ { k } ) \| _ { 2 } , \quad x _ { k + 1 } = x _ { k } + h _ { k } ,
$$

where $J ( x _ { k } ) = \mu ( x _ { k } ) \big \lrcorner ( A + \mu ( x _ { k } ) ^ { 2 } r _ { k } x _ { k } ^ { T } \big )$ ，with $r _ { k } = b - A x _ { k }$ is the Jacobian of $f ( x )$ at $x _ { k }$ Since $A + \mu ( x _ { k } ) ^ { 2 } r _ { k } x _ { k } ^ { T }$ is a rank-one modification of $A$ , its QR factorization can be cheaply computed by modifying the QR factorization of $A$ ； see Section 3.3.2. In fact, this method is closely related to inverse iteration and has a rate of convergence similar to that shown by Peters and Wilkinson [891,1979].

# 4.4.5 - Regularized TLS

When $A$ is nearly rank-deficient,regularization is required to stabilize the TLS solution. Similar to TSVD, truncated TLS (TTLS) reduces an il-conditioned problem to an exactly rank-deficient problem by treating small singular values of $( A , b )$ as zeros. Fierro and Bunch [405,1994] show that under certain conditions,TTLS is superior to TSVD in suppressing noise in $A$ and $b$ ；see also [406,1996].

Let $k \leq \mathrm { r a n k } ( A )$ be the number of singular values to be retained. Then the TTLS solution

$$
x _ { k } = - V _ { 1 2 } V _ { 2 2 } ^ { \dagger } = ( V _ { 1 1 } ^ { T } ) ^ { \dagger } V _ { 2 1 } ^ { T }
$$

can be computed by Algorithm 4.4.1. The second expression for is better to use when $k$ is smal The rorm of $x _ { k }$ is $\| x _ { k } \| _ { 2 } = \left( \| V _ { 2 2 } \| _ { 2 } ^ { - 2 } - 1 \right) ^ { 1 / 2 }$ Irincreaes ith $k$ wile henomofthe residual matrix

$$
\Vert \left( \begin{array} { l l } { A } & { b } \end{array} \right) - \left( \begin{array} { l l } { \tilde { A } } & { \tilde { b } } \end{array} \right) \Vert _ { F } = \left( \sigma _ { k + 1 } ^ { 2 } + \cdot \cdot \cdot + \sigma _ { n + 1 } ^ { 2 } \right) ^ { 1 / 2 }
$$

decreases with $k$ . The TTLS solution $x _ { k }$ can be written as a filtered sum

$$
x _ { k } = \sum _ { i = 1 } ^ { n } f _ { i } \frac { \hat { u } _ { i } ^ { T } b } { \hat { \sigma } _ { i } } \hat { v } _ { i } ,
$$

where $A = \hat { U } \hat { \Sigma } \hat { V } ^ { T }$ is the SVD of $A$ . Fierro et al. [404,1997] show that when $\hat { u } _ { i } ^ { T } b \neq 0$ and $i \leq k$ ,the filter factors $f _ { i }$ are close to one,and for $i > k$ they are small.

Another approach to regularization is to restrict the TLS solution by a quadratic constraint. The RTLS problem is

$$
\operatorname* { m i n } _ { E , f } \| \left( E \quad f \right) \| _ { F } \quad \mathrm { s u b j e c t ~ t o } \quad ( A + E ) x = b + f , \quad \| L x \| _ { 2 } \leq \delta ,
$$

where $\delta > 0$ is a regularization parameter, and the matrix $L \in \mathbb { R } ^ { p \times n }$ defines a seminorm on the solution space.In practice, the parameter $\delta$ is usually not exactly specified but has to be estimated from the given data using the techniques discussed for the TLS problem in Section 3.6.4.

The optimal solution of the RTLS problem is different from $x _ { \mathrm { T L S } }$ only when the quadratic constraint is active,i.e.,

$$
\| L x _ { \mathrm { T L S } } \| _ { 2 } > \delta .
$$

In this case the constraint in (4.4.35) holds with equality at the optimal solution,and the RTLS solution can be characterized by the following first-order optimality conditions for (4.4.35); see Golub,Hansen,and O'Leary [492,1999].

Theorem 4.4.1. The solution to the regularized TLS problem (4.4.35) with the inequality constraint replaced by equality is a solution to the eigenvalue problem

$$
( A ^ { T } A - \lambda _ { I } I + \lambda _ { L } L ^ { T } L ) x = A ^ { T } b ,
$$

where

$$
\lambda _ { I } = \phi ( x ) = \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| ^ { 2 } } , \qquad \lambda _ { L } = \frac { 1 } { \delta ^ { 2 } } \big ( b ^ { T } ( b - A x ) - \phi ( x ) \big ) .
$$

Sima, Van Hufel,and Golub [994,2o04l give methods for solving the RTLS problem using an iterative method that in each step solves a quadratic eigenvalue problem. In practice, very few steps are required. Their method can be applied to large problems using existing fast methods based on projection onto Krylov subspaces for solving quadratic eigenvalue problems.

The first-order conditions for RTLS given in Theorem 4.4.1 are the same as for the constrained minimization problem

$$
\operatorname* { m i n } _ { x } { \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| _ { 2 } ^ { 2 } } } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| L x \| _ { 2 } \leq \delta .
$$

This Rayleigh quotient formulation of the RTLS problem is closely related to Tikhonov regularization of TLS,

$$
\operatorname* { m i n } _ { E , r } \| \left( E \quad f \right) \| _ { F } + \rho \| L x \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t } \ \mathrm { t o } \quad ( A + E ) x = b + f ,
$$

and equivalent to the nonconvex minimization problem

$$
\operatorname* { m i n } _ { x } \left\{ \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| _ { 2 } ^ { 2 } } + \rho \| L x \| _ { 2 } ^ { 2 } \right\} .
$$

Beck and Ben-Tal [96,2oo6] show that this problem can be reduced to a sequence of trust-region problems and give detailed algorithms. Algorithms for large-scale Tikhonov regularization of TLS are developed by Lampe and Voss [712, 2013].

Guo and Renaut [554, 2oo2] show that the eigenvalue problem in Theorem 4.4.1 can be formulated as

$$
( M + \lambda _ { L } N ) \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = \lambda _ { I } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) ,
$$

where $\lambda _ { L }$ is given as in (4.4.37), and

$$
M = \left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } b } } \\ { { b ^ { T } A } } & { { b ^ { T } b } } \end{array} \right) , \qquad N = \left( \begin{array} { c c } { { L ^ { T } L } } & { { 0 } } \\ { { 0 } } & { { - \delta ^ { 2 } } } \end{array} \right) .
$$

Based on this formulation, they suggest an algorithm using shifted inverse iteration to solve the eigenvalue problem (4.4.41). As an initial solution, the corresponding regularized LS solution $x ^ { ( 0 ) } = x _ { R L S }$ is used.Anadditional complication is that the matrix $B$ depends on the RTLS solution. Their algorithm is further analyzed and refined in Renaut and Guo [924, 2oo5]. Lampe and Voss [711, 2oo8] develop a related but faster method that uses a nonlinear Arnoldi process (see Section 6.4.5) and a modified root-finding method.

# Notes and references

M. Wei [1111,1992] gives algebraic relations between the total least squares and least squares problems with more than one solution. Several papers study the sensitivity and conditioning of the TLS problem and give bounds for the condition number; see Zhou et al.[1149, 2009], Baboulin and Gratton [51,2o11], Jia and Li [670,2o13],and Xie, Xiang,and Y. Wei [1134,2O17]. A perturbation analysis of TTLS is given by Gratton，Titley-Peloquin,and Ilunga [529, 2013].

De Moor [297, 1993l studies more general structured and weighted TLS problems and considers applications in systems and control theory. These problems can be solved via a nonlinear GSVD.A review of developments and extensions of the TLS method to weighted and struc-tured approximation is given by Markovsky and Van Huffel [777,2oo7]. A recent bibliography on total least squares is given by Markovsky [776, 2O1o]. Standard TLS methods may not be appropriate when $A$ has a special structure such as Toeplitz or Vandermonde. The structured least-norm problem (STLN) preserves structure and can minimize errors also in the $\ell _ { 1 }$ -norm and others; see Rosen,Park,and Glick [936,1996] and Van Huffel,Park,and Rosen [1076,1996].

# 4.5 - Least Squares Problems with Special Bases

# 4.5.1 $-$ Approximation by Orthogonal Polynomials

It is frequently desired to model a given function $y = f ( x )$ by a linear combination of basis functions:

$$
\bar { f } = \sum _ { k = 0 } ^ { n } c _ { k } \phi _ { k } ( x ) .
$$

It is often convenient to choose the $n + 1$ basis functions as a triangle family of polynomials, where

$$
\phi _ { k } ( x ) = \sum _ { j = 0 } ^ { k } a _ { k j } x ^ { j }
$$

is a polynomial of degree $k$ with nonzero leading coeficient $a _ { k k }$ . The coefficients of such a family form a nonsingular lower triangular matrix $A = \left( a _ { i , j } \right)$ ， $0 \leq j \leq i \leq n$ .Then the monomials $x ^ { k }$ ， $k = 0 , \ldots , n$ ,can be expressed recursively and uniquely as linear combinations $x ^ { k } = b _ { k , 0 } p _ { 0 } + b _ { k , 1 } p _ { 1 } + \cdot \cdot \cdot + b _ { k , k } p _ { k }$ , where the associated matrix is $B = ( b _ { i , j } ) = A ^ { - 1 }$

Definition 4.5.1. Let thereal-valued functions $f$ and $g$ be defined on a finite grid $G = \{ x _ { i } \} _ { i = 0 } ^ { m }$ of distinct points. Then, the inner product of $( f , g )$ is defined by

$$
( f , g ) = \sum _ { i = 0 } ^ { m } f ( x _ { i } ) g ( x _ { i } ) w _ { i } ,
$$

where $\{ w _ { i } \} _ { i = 0 } ^ { m }$ are given positive weights. The norm of $f$ is $\| f \| = ( f , f ) ^ { 1 / 2 }$

An important consideration is the choice of a proper basis for the space of approximating functions. The functions $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ are said to form an orthogonal system if $( \phi _ { i } , \phi _ { j } ) = 0$ for $i \neq j$ and $\| \phi _ { i } \| \neq 0$ for all $i$ ，If,in addition, $\lVert \phi _ { i } \rVert = 1$ for all $i$ ，then the sequence is called an orthonormal system.We remark that the notation used is such that the results can be generalized with minor changes to cover the least squares approximation when $f$ is approximated by an infinite sequence of orthogonal functions $\phi _ { 0 } , \phi _ { 1 } , \phi _ { 2 } , . . . .$

We study the least squares approximation problem to determine coeficients $c _ { 0 } , c _ { 1 } , \ldots , c _ { n }$ in (4.5.1) such that the weighted Euclidean norm

$$
\| \overline { { f } } - f \| ^ { 2 } = \sum _ { i = 0 } ^ { m } w _ { i } | \overline { { f } } ( x _ { i } ) - f ( x _ { i } ) | ^ { 2 }
$$

of the error is minimized. Note that interpolation is a special case ( ${ \bf \Phi } _ { n } = m $ ）of this problem. By a family of orthogonal polynomials we mean here a triangle family of polynomials, which is an orthogonal system with respect to the inner product (4.5.2) for some given weights.

Theorem 4.5.2. Let $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ be linearly independent functions. Then the least squares approximation problem has the unique solution

$$
f ^ { * } = \sum _ { j = 0 } ^ { n } c _ { j } \phi _ { j } ,
$$

which is characterized by the orthogonality property $( f ^ { * } - f , \phi _ { j } ) = 0$ ， $j = 0 , 1 , \ldots , n$ .The coefficients $c _ { j }$ ,called orthogonal coefcients or Fourier coefcients, satisfy the normal equations

$$
\sum _ { j = 0 } ^ { n } ( \phi _ { j } , \phi _ { k } ) c _ { j } = ( f , \phi _ { k } ) , \quad k = 0 , \ldots , n .
$$

Ifthe functions form an orthogonal system, the coeffcients are given by

$$
c _ { j } = ( f , \phi _ { j } ) / ( \phi _ { j } , \phi _ { j } ) , \quad j = 0 , \ldots , n .
$$

Expansions of functions in terms of orthogonal polynomials are easy to manipulate, have good convergence properties,and give a well-conditioned representation (with the exception of weight distributions on certain grids). We now prove some results from the general theory of orthogonal polynomials.

Theorem 4.5.3. Let $\{ x _ { i } \} _ { i = 0 } ^ { m } \in ( a , b )$ be distinct points, and let $\{ w _ { i } \} _ { i = 0 } ^ { m }$ be a set of weights. Then there is an associated triangle family of orthogonal polynomials $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { m }$ . The family is uniquely determined apart from the fact that the leading coefficients $a _ { 0 } , a _ { 1 } , a _ { 2 } , \dotsc$ can be given arbitrary nonzero values. The orthogonal polynomials satisfy $a$ three-term recursion formula, $\phi _ { - 1 } ( x ) = 0$ ， $\phi _ { 0 } ( x ) = a _ { 0 }$ ，

$$
\phi _ { n + 1 } ( x ) = \alpha _ { n } ( x - \beta _ { n } ) \phi _ { n } ( x ) - \gamma _ { n } \phi _ { n - 1 } ( x ) , \quad n \ge 0 ,
$$

where $\alpha _ { n } = { a _ { n + 1 } } / { a _ { n } }$ and

$$
\beta _ { n } = \frac { ( x \phi _ { n } , \phi _ { n } ) } { \| \phi _ { n } \| ^ { 2 } } , \qquad \gamma _ { n } = \frac { \alpha _ { n } \| \phi _ { n } \| ^ { 2 } } { \alpha _ { n - 1 } \| \phi _ { n - 1 } \| ^ { 2 } } \quad ( n > 0 ) .
$$

If the weight distribution is symmetric about $x = \beta$ ,then $\beta _ { n } = \beta$ for all $n$

Proof. Suppose that the $\phi _ { j }$ have been constructed for $0 \leq j \leq n , \phi _ { j } \neq 0 ( n \geq 0 )$ . We now seek a polynomial of degree $n + 1$ with leading coefficient $a _ { n + 1 }$ that is orthogonal to $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ For a triangle family of polynomials $\{ \phi _ { j } \} _ { j = 0 } ^ { n }$ , we can write

$$
\phi _ { n + 1 } = \alpha _ { n } x \phi _ { n } - \sum _ { i = 0 } ^ { n } c _ { n , i } \phi _ { i } .
$$

Hence $\phi _ { n + 1 }$ is orthogonal to $\phi _ { j }$ $0 \leq j \leq n$ , if and only if

$$
\alpha _ { n } ( x \phi _ { n } , \phi _ { j } ) - \sum _ { i = 0 } ^ { n } c _ { n , i } ( \phi _ { i } , \phi _ { j } ) = 0 , \quad j = 0 , 1 , \ldots , n .
$$

Since $( \phi _ { i } , \phi _ { j } ) = 0$ ， $i \neq j$ , it follows that

$$
c _ { n , j } \| \phi _ { j } \| ^ { 2 } = \alpha _ { n } ( x \phi _ { n } , \phi _ { j } ) , \quad 0 \leq j \leq n ,
$$

which determines the coefficients $c _ { n , j }$ ．From the definition of inner product it follows that $( x \phi _ { n } , \phi _ { j } ) = ( \phi _ { n } , x \phi _ { j } )$ . But $x \phi _ { j }$ is a polynomial of degree $j + 1$ and is therefore orthogonal to $\phi _ { n }$ if $j + 1 < n$ So $c _ { n j } = 0$ ， $j < n - 1$ ,and thus

$$
\phi _ { n + 1 } = \alpha _ { n } x \phi _ { n } - c _ { n , n } \phi _ { n } - c _ { n , n - 1 } \phi _ { n - 1 } .
$$

This has the same form as (4.5.5) if we set $\beta _ { n } = c _ { n , n } / \alpha _ { n }$ ， $\gamma _ { n } = c _ { n , n - 1 }$ . To get the expression in (4.5.6) for $\gamma _ { n }$ , we take the inner product of equation (4.5.7） with $\phi _ { n + 1 }$ . From orthogonal-ity it follows that $\left( \phi _ { n + 1 } , \phi _ { n + 1 } \right) = \alpha _ { n } ( \phi _ { n + 1 } , x \phi _ { n } )$ . Decreasing all indices by one, we obtain $( \phi _ { n } , x \phi _ { n - 1 } ) = \| \phi _ { n } \| ^ { 2 } / \alpha _ { n - 1 }$ ， $n \geq 1$ .Substituting this in the expression for $\gamma _ { n }$ gives the desired result. □

The proof of the above theorem shows a way to construct $\beta _ { n }$ ， $\gamma _ { n }$ ,and the values of the polynomials $\phi _ { n }$ at the grid points for $n = 1 , 2 , 3 , \ldots .$ This is called the Stieltjes procedure. For $n = m$ , the constructed polynomial must be equal to $a _ { m + 1 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdots ( x - x _ { m } )$ ， because this polynomial is zero at all the grid points and thus orthogonal to all functions on the grid. Since $\| \phi _ { m + 1 } \| = 0$ ,the construction stops at $n = m$ . This is natural because there cannot be more than $m + 1$ orthogonal (or even linearly independent) functions on a grid with $m + 1$ points.

Given the coefcients in an orthogonal expansion, the values of $f$ can be efficiently computed using the following algorithm. (The proof is left as a somewhat difficult exercise.)

$\begin{array} { r } { p _ { k } \ = \ \sum _ { j = 0 } ^ { k } c _ { j } \phi _ { j } } \end{array}$ $\phi _ { j } ( x )$ gonal $p ( x ) \stackrel { \textstyle - } { = } A _ { 0 } y _ { 0 }$ $y _ { n + 2 } = y _ { n + 1 } = 0$

$$
y _ { k } = \alpha _ { k } ( x - \beta _ { k } ) y _ { k + 1 } - \gamma _ { k + 1 } y _ { k + 2 } + c _ { k } , \quad k = n , n - 1 , \ldots , 0 .
$$

From Theorem 4.5.2 follows the important result that the coefcients in the best approximating polynomial $p _ { k }$ of degree $k$ are independent of $k$ and given by $c _ { j } = ( f , \phi _ { j } ) / ( \phi _ { j } , \phi _ { j } )$ . Hence approximations of increasing degree can be recursively generated as follows.Assume that $\phi _ { i }$ ， $i = 1 , \ldots , k$ ,and $p _ { k }$ have been computed. In the next step the coefficients $\beta _ { k } , \gamma _ { k }$ are computed from (4.5.6) and $\phi _ { k + 1 }$ by (4.5.5). The next approximation of $f$ is then given by

$$
p _ { k + 1 } = p _ { k } + c _ { k + 1 } \phi _ { k + 1 } , \quad c _ { k + 1 } = ( f , \phi _ { k + 1 } ) / \| \phi _ { k + 1 } \| ^ { 2 } .
$$

The coefficients $\{ \beta _ { k } , \gamma _ { k } \}$ in the recursion formula (4.5.5) and the orthogonal functions $\phi _ { j }$ at the grid points are computed using the Stieltjes procedure together with the orthogonal coefficients $\{ c _ { j } \}$ for $j = 1 , 2 , \dots , n$ . The total work required is about 4mn flops, assuming unit weights and that the grid is symmetric. If there are differing weights,then about mn additional operations are needed; similarly,mn additional operations are required if the grid is not symmetric.If the orthogonal coefficients are determined simultaneously for several functions on the same grid,then only about mn additional operations per function are required. (In the above, we assume that $m \gg 1$ ， $n \gg 1 .$ ）Hence,the procedure is much more economical than the general methods based on normal equations or QR factorization,which all require $O ( m n ^ { 2 } )$ flops.

In practice the computed $\phi _ { k + 1 }$ will gradually lose orthogonality to the previously computed $\phi _ { j }$ . Since $\phi _ { k + 1 } ^ { T } p _ { k } = 0$ ,an alternative expression for the new coefficient is

$$
c _ { k + 1 } = { \left( r _ { k } , \phi _ { k + 1 } \right) } / { \| \phi _ { k + 1 } \| ^ { 2 } } , \quad r _ { k } = f - p _ { k } .
$$

This expression, which involves the residual $r _ { k }$ , will give better accuracy in the computed coefficients. Indeed, when using the classical formula,one sometimes finds that the residual norm increases when the degree of the approximation is increased! Note that the difference between the two variants discussed here is similar to the difference between CGS and MGS.

The Stieltjes procedure may be sensitive to propagation of roundoff errors. An alternative procedure for computing the recurrence coeficients in (4.5.5) and the values of the orthogonal polynomials has been given by Gragg and Harrod [523,1984l; see also Boley and Golub [169, $\mathrm { 1 9 8 7 } ]$ . In this procedure these quantities are computed from an inverse eigenvalue problem for a certain symmetric tridiagonal matrix. Reichel [916,1991] compares this scheme with the Stieltjes procedure and shows that the Gragg-Harrod procedure generally yields better accuracy.

Expansions in orthogonal polynomials also have the very important advantage of avoiding the difficulties with ill-conditioned systems of equations that occur even for moderate $n$ when the coefficientsinapolyomial $\textstyle \sum _ { j = 0 } ^ { n } c _ { j } x ^ { j }$ andthectiot For equidistant data, te Gram polynomials $\{ P _ { n , m } \} _ { n = 0 } ^ { m }$ , which are orthogonal withrespectto the inner product

$$
( f , g ) = \sum _ { i = 0 } ^ { m } f ( x _ { i } ) g ( x _ { i } ) , \quad x _ { i } = - 1 + 2 i / m ,
$$

are relevant. These satisfy the recursion formula $P _ { - 1 , m } ( x ) = 0$ ， $P _ { 0 , m } = ( m + 1 ) ^ { - 1 / 2 }$ ，

$$
P _ { n + 1 , m } ( x ) = \alpha _ { n , m } x P _ { n , m } ( x ) - \gamma _ { n , m } P _ { n - 1 , m } ( x ) , \quad n \ge 0 ,
$$

where the coefficients are given by $( n < m )$

$$
\alpha _ { n , m } = \frac { m } { n + 1 } \left( \frac { 4 ( n + 1 ) ^ { 2 } - 1 } { ( m + 1 ) ^ { 2 } - ( n + 1 ) ^ { 2 } } \right) ^ { 1 / 2 } , \qquad \gamma _ { n , m } = \frac { \alpha _ { n , m } } { \alpha _ { n - 1 , m } } .
$$

When $n \ll m ^ { 1 / 2 }$ , these polynomials are well behaved. However, when $n \gg m ^ { 1 / 2 }$ , they have very large oscillations between the grid points,and a large maximum norm in $[ - 1 , 1 ]$ . Related to this is the fact that when fitting a polynomial to equidistant data, one should never choose $n$ larger than about $2 m ^ { 1 / 2 }$

One of the motivations for the method of least squares is that it effectively reduces the influence of random errors in measurements. Suppose that the values of a function have been measured at points $x _ { 0 } , x _ { 1 } , \ldots , x _ { m }$ Let $f ( x _ { p } )$ be the measured value,and let ${ \bar { f } } ( x _ { p } )$ be the “true”(unknown) function value, which is assumed to be the same as the expected value of the measured value. Thus,no systematic errors are assumed to be present. Suppose further that the errors in measurement at the various points are statistically independent. Then we have $f ( x _ { p } ) = { \bar { f } } ( x _ { p } ) + \epsilon$ ,where

$$
\mathcal { E } ( \epsilon ) = 0 , \qquad \mathcal { V } ( \epsilon ) = s ^ { 2 } I ,
$$

and $\mathcal { E }$ denotes expected value and $\nu$ variance. The problem is to use the measured data to estimate the coeficients in the series $\begin{array} { r } { f ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } \phi ( x ) } \end{array}$

According to the Gauss-Markov theorem (Theorem 1.1.4) the least squares estimates $c _ { j } ^ { * }$ have a smaller variance than the values one gets by any other linear unbiased estimation method. This minimum property holds not only for estimates of the coeffcients $c _ { j }$ but also for every linear function of the coefficients, such as the estimate of the value $f ( \alpha )$ at an arbitrary point $\alpha$ .By Lemma 1.1.1, the covariance matrix of the estimates $c _ { j } ^ { * }$ equals $s ^ { 2 } I$ and $c _ { j } ^ { * }$ and $c _ { k } ^ { * }$ are uncorrelated if $j \neq k$ and the variance of the estimate $c _ { j } ^ { * }$ is $s ^ { 2 }$ .From this it follows that

$$
\mathcal { V } \{ f _ { n } ^ { * } ( \alpha ) \} = \mathcal { V } \bigg \{ \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } ( \alpha ) \bigg \} = \sum _ { j = 0 } ^ { n } \mathcal { V } \{ c _ { j } ^ { * } \} | \phi _ { j } ( \alpha ) | ^ { 2 } = s ^ { 2 } \sum _ { j = 0 } ^ { n } | \phi _ { j } ( \alpha ) | ^ { 2 } .
$$

As an average, taken over the grid of measurement points, the variance of the smoothed function values is

$$
\frac { 1 } { m + 1 } \sum _ { j = 0 } ^ { n } \mathcal { V } \{ f _ { n } ^ { * } ( x _ { i } ) \} = \frac { s ^ { 2 } } { m + 1 } \sum _ { j = 0 } ^ { n } \sum _ { i = 0 } ^ { m } | \phi _ { j } ( x _ { i } ) | ^ { 2 } = s ^ { 2 } \frac { n + 1 } { m + 1 } .
$$

Between the grid points, however, the variance can, in many cases, be significantly larger: For $j \gg m ^ { 1 / 2 }$ the Gram polynomials can be much larger between the grid points. Set

$$
s _ { I } ^ { 2 } = s ^ { 2 } \sum _ { j = 0 } ^ { n } { \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } | \phi _ { j } ( \alpha ) | ^ { 2 } d \alpha .
$$

Thus, $s _ { I } ^ { 2 }$ is an average variance for $f _ { n } ^ { * } ( \alpha )$ taken over the entire interval $[ - 1 , 1 ]$ . The following values were obtained for the ratio $k$ between $s _ { I } ^ { 2 }$ and $s ^ { 2 } ( n + 1 ) / ( m + 1 )$ when $m = 4 1$ ；see Dahlquist and Bjorck [283,1974, Section 4.4.5]:

$$
\left[ { \begin{array} { c c c c c c c } { n } & { 5 } & { 1 0 } & { 1 5 } & { 2 0 } & { 2 5 } & { 3 0 } & { 3 5 } \\ { k } & { 1 . 0 } & { 1 . 1 } & { 1 . 7 } & { 2 6 } & { 7 \cdot 1 0 ^ { 3 } } & { 1 . 7 \cdot 1 0 ^ { 7 } } & { 8 \cdot 1 0 ^ { 1 1 } } \end{array} } \right]
$$

These results are related to the recommendation that one should choose $n < 2 m ^ { 1 / 2 }$ when fitting a polynomial to equidistant data. This recommendation seems to contradict the Gauss-Markov theorem, but in fact it only means that one gives up the requirement that the estimate be unbiased. Still,it is remarkable that this can lead to such a drastic reduction of the variance of the estimates $f _ { n } ^ { * }$

# 4.5.2 - Chebyshev Interpolation

The most important family of orthogonal polynomials is perhaps the Chebyshev polynomials.8 The easily verified formula

$$
\cos ( n + 1 ) \phi + \cos ( n - 1 ) \phi = 2 \cos \phi \cos ( n \phi ) , \quad n \geq 1 ,
$$

can be used recursively to express $\cos ( n \phi )$ as a polynomial in $\cos \phi$ . If we set $x = \cos \phi$ ,then $\phi \ : = \ : \operatorname { a r c c o s } \ : x$ ，and we obtain the Chebyshev polynomials for $- 1 \leq x \leq 1$ by the formula $T _ { n } ( x ) = \cos ( n \operatorname { a r c c o s } x )$ ， $n \geq 0$ . From trigonometric formulas it follows that the Chebyshev polynomials satisfy the recursion formula

$$
T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x , \quad T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) , \quad n \geq 0 .
$$

The leading coefficient of $T _ { n } ( x )$ is $2 ^ { n - 1 }$ for $n \geq 1$ and 1 for $n = 0$ . The symmetry property $T _ { n } ( - x ) = ( - 1 ) ^ { n } T _ { n } ( x )$ also follows from the recurrence formula.

Theorem 4.5.5. $T _ { n } ( x )$ has $n$ zeros in $[ - 1 , 1 ]$ given by the Chebyshev abscissae,

$$
x _ { k } = \cos \Big ( \frac { 2 k + 1 } { n } \frac \pi 2 \Big ) , \quad k = 0 , 1 , \dots , n - 1 ,
$$

and $n + 1$ extrema $T _ { n } ( x _ { k } ^ { \prime } ) = ( - 1 ) ^ { k }$ attained at $x _ { k } ^ { \prime } = \cos ( k \pi / n )$ ， $k = 0 , \ldots , n$ These results follow directly by noting that $| \cos ( n \phi ) |$ has maxima for $\phi _ { k } ^ { \prime } = k \pi / n$ ，and $\cos ( n \phi _ { k } ) = 0$ for $\phi _ { k } = ( 2 k + 1 ) \pi / ( 2 n )$

The Chebyshev polynomials $T _ { 0 } , T _ { 1 } , \dots , T _ { n - 1 }$ are orthogonal with respect to the inner product

$$
( f , g ) = \sum _ { k = 0 } ^ { n - 1 } f ( x _ { k } ) g ( x _ { k } ) ,
$$

where $\{ x _ { k } \}$ are the Chebyshev abscissae (4.5.15) for $T _ { n }$ .If $i \neq j$ ,then $( T _ { i } , T _ { j } ) = 0 , 0 \leq i , j <$ $n$ ,and

$$
( T _ { i } , T _ { j } ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } n } & { { \mathrm { i f ~ } } i = j \neq 0 , } \\ { n } & { { \mathrm { i f ~ } } i = j = 0 . } \end{array} \right. }
$$

If one intends to approximate a function in the entire interval $[ - 1 , 1 ]$ by a polynomial and can choose the points at which the function is computed or measured, one should choose the Chebyshev abscissae.With these points, interpolation is a fairly well-conditioned problem in the entire interval,and one can conveniently fit a polynomial of lower degree than $m$ if one wishes to smooth errors in measurement. The risk of disturbing surprises between the grid points is insignificant.

Let $p ( x )$ denote the interpolation polynomial of a function $f ( x )$ at the Chebyshev abscissae $x _ { k }$ (4.5.15). From Theorem 4.5.3 we get

$$
p ( x ) = \sum _ { j = 0 } ^ { n - 1 } c _ { j } T _ { j } ( x ) , \quad c _ { i } = { \frac { 1 } { \| T _ { i } \| ^ { 2 } } } \sum _ { k = 0 } ^ { n - 1 } f ( x _ { k } ) T _ { i } ( x _ { k } ) ,
$$

where $\Vert T _ { i } \Vert _ { 2 }$ is given as in (4.5.16).

Expansions in terms of Chebyshev polynomials are an important aid in the study of functions on the interval $[ - 1 , 1 ]$ . If one is working in terms of a parameter $t$ that varies in the interval $[ a , b ]$ ， then one should make the substitution

$$
t = { \frac { 1 } { 2 } } ( a + b ) + { \frac { 1 } { 2 } } ( a - b ) x
$$

$( t \in [ a , b ] \Leftrightarrow x \in [ - 1 , 1 ] )$ and work with the Chebyshev points

$$
t _ { k } = { \frac { 1 } { 2 } } ( a + b ) + { \frac { 1 } { 2 } } ( a - b ) x _ { k } , \quad k = 0 , \ldots , n - 1 .
$$

The remainder term in interpolation using the values of the function $f$ at the points $x _ { i } , i =$ $0 , 1 , \ldots , n - 1$ , is equal to

$$
\frac { f ^ { ( n ) } ( \xi ) } { ( n ) ! } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } ) .
$$

Here $\xi$ depends on $x$ ,but one can say that the error curve behaves for the most part like a polynomial curve $y = a ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } )$ . A similar oscillating curve is typical for error curves arising from least squares approximation. The zeros of the error are then about the same as the zeros for the first neglected term in the orthogonal expansion. This contrasts sharply with the error curve for Taylor approximation at $x _ { 0 }$ ,whose usual behavior is described approximately by the formula $y = a ( x - x _ { 0 } ) ^ { n - 1 }$ . From the min-max property of the Chebyshev polynomials it follows that placing the interpolation points of the Chebyshev abscissae will minimize the maximum magnitude of

$$
q ( x ) = ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } )
$$

in the interval $[ - 1 , 1 ]$ . This corresponds to choosing $q ( x ) = T _ { m + 1 } ( x ) / 2 ^ { m }$

For computing $p ( x )$ , one can use Clenshaw's recursion formula; see the previous section. (Note that $\alpha _ { k } \ = \ 2$ for $k > 0$ ，but $\alpha _ { 0 } \ = \ 1 .$ ）Occasionally,one is interested in the partial sums of the expansion. To smooth errors in measurement, it can be advantageous to break off the summation before the last term.If the values of the function are afflicted with statistically independent errors in measurement with standard deviation $s$ ，then (see the next section） the series can be broken off when,for the first time,

$$
\left\| \boldsymbol { f } - \sum _ { j = 0 } ^ { k } c _ { j } T _ { j } \right\| < s n ^ { 1 / 2 } .
$$

If the measurement points are the Chebyshev abscisse,then no difficulties arise in fitting a polynomial to the data. In this case the Chebyshev polynomials have a magnitude between the grid points that is not much larger than their magnitude at the grid points.The average variance for $f _ { n } ^ { * } ( \alpha )$ becomes the same both on the interval $[ - 1 , 1 ]$ and the grid of measurement points: $s ^ { 2 } ( n + 1 ) / ( m + 1 )$

The choice of $n$ ,when $m$ is given, is a question of compromising between taking into account the systematic error, i.e., the truncation error (which decreases when $n$ increases) and taking into account the random errors (which grow as $n$ increases). In the Chebyshev case, $\left| c _ { j } \right|$ decreases quickly with $j$ if $f$ is a sufficiently smooth function, while the part of $c _ { j } ^ { * }$ that comes from errors in measurement varies randomly with magnitude about $s ( 2 / ( m + 1 ) ) ^ { 1 / 2 }$ . The expansion should then be broken off when the coefficients begin to “behave randomly.”The coeficients in an expansion in terms of the Chebyshev polynomials can hence be used for filtering away the“noise” from the signal, even when $s$ is initially unknown.

# 4.5.3 - Discrete Fourier Analysis

According to a mathematical theorem first given by Fourier (1768-1830), every periodic function $f ( t )$ with period $2 \pi / \omega$ can, under certain very general conditions, be expanded into a series of the form

$$
f ( t ) = \sum _ { k = 0 } ^ { \infty } ( a _ { k } \cos k \omega t + b _ { k } \sin k \omega t ) ,
$$

where $a _ { k } , b _ { k }$ are real constants.Fourier analysis is one of the most useful and valuable tools in applied mathematics.It has applications also to problems that are not a priori periodic. One important area of application is in digital signal processing, e.g.,in interpreting radar and sonar signals. Another application is statistical time series,which arise in communications theory, control theory,and the study of turbulence.

An expansion of the form (4.5.17) can be expressed in several equivalent ways. Another form, more convenient for manipulations,is

$$
f ( t ) = \sum _ { - \infty } ^ { \infty } c _ { k } e ^ { i k \omega t } ,
$$

where $c _ { 0 } = a _ { 0 }$ $a _ { 0 } , c _ { k } = ( a _ { k } - i b _ { k } ) / 2 , c _ { - k } = ( a _ { k } + i b _ { k } ) / 2 , k > 0$ .This form allows the function to have complex values.Function $f$ with period $2 \pi$ can be approximated by partial sums of these series.We call these finite sums trigonometric polynomials. If a function of $t$ has period $p$ ， then the substitution $x = 2 \pi t / p$ transforms the function into a function of $x$ with period $2 \pi$

When the functions to be modeled are known only on a discrete equidistant set of sampling points,a discrete version of the Fourier analysis can be used. The discrete inner product of two complex-valued functions $f$ and $g$ of period $2 \pi$ is defined as follows (the bar over $g$ indicates complex conjugation):

$$
( f , g ) = \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) \bar { g } ( x _ { \beta } ) , \quad x _ { \beta } = 2 \pi \beta / N .
$$

Theorem 4.5.6. With inner product (4.5.19) the following orthogonality relations hold for the functions $\phi _ { j } ( x ) = e ^ { i j x }$ ， $j = 0 , \pm 1 , \pm 2 , . . .$ ：

$$
\left( \phi _ { j } , \phi _ { k } \right) = \left\{ \begin{array} { l l } { N } & { i f ( j - k ) / N i s a n i n t e g e r , } \\ { 0 } & { o t h e r w i s e . } \end{array} \right.
$$

Proof. With $h = 2 \pi / N$ ， $x _ { \beta } = h \beta$ , we have

$$
\left( \phi _ { j } , \phi _ { k } \right) = \sum _ { \beta = 0 } ^ { N - 1 } e ^ { i j x _ { \beta } } e ^ { - i k x _ { \beta } } = \sum _ { \beta = 0 } ^ { N - 1 } e ^ { i ( j - k ) h \beta } .
$$

This is a geometric series with ratio $q = e ^ { i ( j - k ) h }$ $( j - k ) / N$ is an integer, then $q = 1$ and the sum is $N$ . Otherwise, $q \neq 1$ but $q ^ { N } = e ^ { i ( j - k ) 2 \pi } = 1$ From the summation formula of a geometric series, $( \phi _ { j } , \phi _ { k } ) = ( q ^ { N } - 1 ) / ( q - 1 ) = 0$ □

$f$ has a expnsionof the form $\begin{array} { r } { f = \sum _ { j = 0 } ^ { N - 1 } c _ { j } \phi _ { j } } \end{array}$

$$
( f , \phi _ { k } ) = \sum _ { j = a } ^ { b } c _ { j } ( \phi _ { j } , \phi _ { k } ) = c _ { k } ( \phi _ { k } , \phi _ { k } ) , \quad a \leq k \leq b ,
$$

because $( \phi _ { j } , \phi _ { k } ) = 0$ for $j \neq k$ . Thus, changing $k$ to $j$ , we have

$$
c _ { j } = \frac { ( f , \phi _ { j } ) } { ( \phi _ { j } , \phi _ { j } ) } = \frac { 1 } { N } \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) e ^ { - i j x _ { \beta } } .
$$

Note that the calculations required to compute the coeficients $c _ { j }$ according to (4.5.20), called Fourier analysis,are of essentially the same type as in the calculations needed to tabulate $f ^ { * } ( x )$ for $x = 2 \pi \beta / N$ ， $\beta = 0 , 1 , \ldots , N - 1$ , when the expansion in (4.5.21) is known, the so-called Fourier synthesis.

Theorem 4.5.7. Every function $f ( x )$ defined on the grid $x _ { \beta } = 2 \pi \beta / N _ { ; }$ $\beta = 0 , \ldots , N - 1$ can be interpolated by a trigonometric polynomial

$$
f ( x ) = \sum _ { j = - k } ^ { k + \theta } c _ { j } e ^ { i j x } ,
$$

where

$$
\theta = \left\{ \begin{array} { l l } { { 1 } } & { { i f N e \nu e n , } } \\ { { 0 } } & { { i f N o d d , } } \end{array} \right. \qquad k = \left\{ \begin{array} { l l } { { N / 2 - 1 } } & { { i f N e \nu e n , } } \\ { { ( N - 1 ) / 2 } } & { { i f N o d d . } } \end{array} \right.
$$

If the sum in (4.5.21) is terminated when $j < k + \theta _ { \mathrm { { i } } }$ ， one obtains the trigonometric polynomial that is the best least squares approximation, among alltrigonometric polynomials with the same number of terms,to $f$ on the grid.

Proof. The expression for $c _ { j }$ was formally derived previously (see (4.5.20)). Because

$$
e ^ { - i ( N - j ) x _ { \beta } } = e ^ { i j x _ { \beta } } , \quad c _ { - j } = c _ { N - j } ,
$$

$f ( x )$ coincidesonthegrid withtefunction $\begin{array} { r } { f ^ { * } ( x ) = \sum _ { j = 0 } ^ { N - 1 } c _ { j } e ^ { i j x } } \end{array}$ However,between the grid points, $f$ and $f ^ { * }$ are not identical. Functions of several variables can be treated analogously by taking one variable at a time. □

By (4.5.20), the discrete Fourier coefficients $c _ { j }$ for a function

$$
f ( x ) = \sum _ { j = 0 } ^ { N - 1 } c _ { j } e ^ { i j x } ,
$$

whose values are known at the points $x = 2 \pi \beta / N , \beta = 0 , \ldots , N - 1$ are

$$
c _ { j } = \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) \omega ^ { j \beta } , \quad f _ { \beta } = \frac { 1 } { N } f ( x _ { \beta } ) , \quad j = 0 , \ldots , N - 1 ,
$$

where $\omega = e ^ { - 2 \pi i / N }$ is the $n$ th root of unity $\boldsymbol { \omega } ^ { N } = 1 \dot { }$ ). Hence $c _ { j }$ is a polynomial of degree $N - 1$ in $\omega ^ { j }$ .Let $F _ { N } \in \mathbb { R } ^ { N \times N }$ be the Fourier matrix with elements

$$
( F _ { N } ) _ { j \beta } = \omega ^ { j \beta } , \quad j , \beta = 0 , \dots , N - 1 .
$$

It folows that the discrete Fourier transform can be expressed as a matrix-vector multiplication $c = F _ { N } f$ ，where the discrete Fourier transform (DFT) matrix $F _ { N }$ is a complex symmetric Vandermonde matrix. Furthermore,

$$
\frac { 1 } { N } F _ { N } ^ { H } F _ { N } = I ,
$$

i.e., $N ^ { - 1 / 2 } F _ { N }$ is a unitary matrix, and the inverse transform is

$$
f = \frac { 1 } { N } F _ { N } ^ { H } c .
$$

If implemented in a naive way, the DFT will take $N ^ { 2 }$ operations to compute all $c _ { j }$ (here, one operation equals one complex addition and one complex multiplication). The application of discrete Fourier analysis to large-scale problems became feasible only with the invention of the so-called fast Fourier transform (FFT) that reduces the computational complexity to $O ( N \log N )$ The FFT,developed in 1965 by Cooley and Tukey [269,1965],is based on the divide-andconquer strategy. Consider the special case when $N = 2 ^ { p }$ and set

$$
\beta = \left\{ \begin{array} { l l } { 2 \beta _ { 1 } } & { \mathrm { i f ~ } \beta \mathrm { ~ e v e n } , } \\ { 2 \beta _ { 1 } + 1 } & { \mathrm { i f ~ } \beta \mathrm { ~ o d d } , } \end{array} \right. \quad 0 \leq \beta _ { 1 } \leq \frac { 1 } { 2 } N - 1 .
$$

Then the sum in (4.5.22) can be split into an even part and an odd part:

$$
c _ { j } = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } + \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } + 1 } ( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } \omega ^ { j } .
$$

Let $\alpha$ be the quotient and $j _ { 1 }$ the remainder when $j$ is divided by ${ \scriptstyle { \frac { 1 } { 2 } } } N$ ,i.e., $j = \alpha _ { 2 } ^ { \underline { { { 1 } } } } N + j _ { 1 }$ Then, because $\omega ^ { N } = 1$ ，

$$
( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } = ( \omega ^ { 2 } ) ^ { \alpha ( 1 / 2 ) N \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } = ( \omega ^ { N } ) ^ { \alpha \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } = ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } .
$$

Thus, if for $j _ { 1 } = 0 , 1 , \ldots , \textstyle { \frac { 1 } { 2 } } N - 1$ we set

$$
\phi ( j _ { 1 } ) = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } , \quad \psi ( j _ { 1 } ) = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } + 1 } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } ,
$$

where $\left( \omega ^ { 2 } \right) ^ { \frac { 1 } { 2 } N } = 1$ , then by (4.5.24),

$$
c _ { j } = \phi ( j _ { 1 } ) + \omega ^ { j } \psi ( j _ { 1 } ) , \quad j = 0 , 1 , \ldots , N - 1 .
$$

The two sums on the right are elements of the DFTs of length $N / 2$ applied to the parts of $f$ with odd and even subscripts. The DFT of length $N$ is obtained by combining these two DFTs. Since (N/2)=-1,it follows that

$$
\begin{array} { l } { y _ { j _ { 1 } } = \phi _ { j _ { 1 } } + \omega _ { N } ^ { j _ { 1 } } \psi _ { j _ { 1 } } , } \\ { y _ { j _ { 1 } + N / 2 } = \phi _ { j _ { 1 } } - \omega _ { N } ^ { j _ { 1 } } \psi _ { j _ { 1 } } , \quad j _ { 1 } = 0 , \hdots , N / 2 - 1 . } \end{array}
$$

These expressions are called the butterfly relations because of the data flow pattern. The computation of $\phi _ { j _ { 1 } }$ and $\psi _ { j _ { 1 } }$ is equivalent to two Fourier transforms with $m = N / 2$ terms instead of one with $N$ terms. If $N / 2$ is even,the same idea can be applied to these two Fourier transforms. One then gets four Fourier transforms,each of which has $N / 4$ terms. If $N = 2 ^ { p }$ , this reduction can be continued recursively until we get $N$ DFTs with one term. Each step involves an evenodd permutation. In the first step the points with last binary digit equal to O are ordered first, and those with last digit equal to 1 are ordered last. In the next step the two resulting subsequences of length $N / 2$ are reordered according to the second binary digit, etc.

The number of complex operations (one multiplication and one addition) required to compute $\{ y _ { j } \}$ from the butterfly relations when $\{ \phi _ { j _ { 1 } } \}$ and $\{ \psi _ { j _ { 1 } } \}$ have been computed is $2 ^ { p }$ , assuming that the powers of $\omega$ are precomputed and stored. If we denote by $q _ { p }$ the total number of operations needed to compute the DFT when $N = 2 ^ { p }$ ， we have $q _ { p } \leq 2 q _ { p - 1 } + 2 ^ { p }$ ， $p \geq 1$ Since $q _ { 0 } = 0$ ,it follows by induction that

$$
q _ { p } \leq p 2 ^ { p } = N \log _ { 2 } N .
$$

Hence, when $N$ is a power of two,the FFT solves the problem with at most $N \cdot \log _ { 2 } N$ complex operations. For example, when $N = 2 ^ { 2 0 } = 1 , 0 4 8 , 5 7 6$ the FFT algorithm is theoretically a factor of 84,00o faster than the “conventional” $O ( N ^ { 2 } )$ algorithm. The FFT algorithm not only uses fewer operations to evaluate the DFT, it also is more accurate.For the conventional method, the roundoff error is proportional to $N$ .For the FFT algorithm,the roundoff error is proportional to $\log _ { 2 } N$

Most implementations of FFT avoid explicit recursion and instead use two stages.

· A reordering stage in which the data vector $f$ is permuted in bit-reversal order. ·A second stage in which first $N / 2$ FFT transforms of length 2 are computed on adjacent elements,followed by $N / 4$ transforms of length 4,etc., until the final result is obtained by merging two FFTs of length $N / 2$

It is not difficult to see that the combined effect of the reordering in the first stage is a bitreversal permutation of the data points. For $i = 0 : N - 1$ ,let the index $i$ have the binary expansion $i = b _ { 0 } + b _ { 1 } \cdot 2 + \cdot \cdot \cdot + b _ { t - 1 } \cdot 2 ^ { t - 1 }$ ,and set

$$
r ( i ) = b _ { t - 1 } + \cdot \cdot \cdot + b _ { 1 } \cdot 2 ^ { t - 2 } + b _ { 0 } \cdot 2 ^ { t - 1 } .
$$

That is, $r ( i )$ is the index obtained by reversing the order of the binary digits.If $i < r ( i )$ ,then exchange $f _ { i }$ and $f _ { r ( i ) }$ . We denote the permutation matrix performing the bit-reversal ordering by $P _ { N }$ . Note that if an index is reversed twice,we end up with the original index. This means that $P _ { N } ^ { - 1 } = P _ { N } ^ { T } = P _ { N }$ ,i.e., $P _ { N }$ is symmetric. The permutation can be carred out“in place" by a sequence of pairwise interchanges or transpositions of the data points. For example, for $N =$ 16,the pairs (1,8), (2,4), (3,12),(5,10), (7,14),and (11,13) are interchanged. The bit-reversal permutation can take a substantial fraction of the total time to do the FFT. Which implementation is best depends strongly on the computer architecture.

When $N = 2 ^ { p }$ the FFT algorithm can be interpreted as a sparse factorization of the DFT matrix,

$$
F _ { N } = A _ { k } \cdot \cdot \cdot A _ { 2 } A _ { 1 } P _ { N } ,
$$

where $P _ { N }$ is the bit-reversal permutation matrix, and $A _ { 1 } , \ldots , A _ { k }$ are block diagonal matrices:

$$
A _ { q } = \mathrm { d i a g } ( \underbrace { B _ { L } , \ldots , B _ { L } } _ { r } ) , \quad L = 2 ^ { q } , \quad r = N / L .
$$

Here the matrix $B _ { k } \in \mathbb { C } ^ { L \times L }$ is theradix-2buterfly matrix defied by

$$
\begin{array} { r } { B _ { L } = \left( \begin{array} { c c } { I _ { L / 2 } } & { \Omega _ { L / 2 } } \\ { I _ { L / 2 } } & { - \Omega _ { L / 2 } } \end{array} \right) , } \end{array}
$$

$$
\Omega _ { L / 2 } = \mathrm { d i a g } \left( 1 , \omega _ { L } , . . . , \omega _ { L } ^ { L / 2 - 1 } \right) , \quad \omega _ { L } = e ^ { - 2 \pi i / L } . \nonumber
$$

This is usually referred to as the Cooley-Tukey FFT algorithm.

The discrete cosine transform (DCT) was discovered in 1974 by Ahmed, Natarajan, and Rao [11,1974l; see also Rao and Yio [913,199o]. The DCT has real entries as opposed to the complex entries of the FFT matrix.Depending on the type of boundary condition (Dirichlet or Neumann, centered at a mesh point or midpoint) there are different variants. The DCT-2 transform is used extensively in image processing. It uses the real basis vectors

$$
v _ { i , j } = { \sqrt { \frac { N } { 2 } } } \cos { \big ( } ( j - 1 ) ( i + { \textstyle { \frac { 1 } { 2 } } } ) { \big ) } \pi ,
$$

divided by $\sqrt { 2 }$ if $j = 1$ . Strang [1044,1999] surveys the four possible variants of cosine transforms DCT-1,..,DCT-4 and their use for different boundary conditions.

# Notes and references

The computational advantage of the Stieltjes approach for polynomial approximation was pointed out by Forsythe [422,1956]. Van Loan [1082,1992] gives a unified treatment of FFT algorithms based on the factorization of the Fourier matrix $F _ { N }$ into a product of sparse matrix factors. Ideas related to the FFT can be found in many previous works;see Cooley [267,199o]. Excellent surveys of the use of the discrete Fourier transform are given by Cooley,Lewis,and Welsh [268, 1969] and Henrici [604,1979].

# 4.5.4 - Vandermonde Systems

A Vandermonde matrix has the form

$$
V = V ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ) = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { x _ { 0 } } } & { { x _ { 1 } } } & { { \cdots } } & { { x _ { n } } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { x _ { 0 } ^ { n } } } & { { x _ { 1 } ^ { n } } } & { { \cdots } } & { { x _ { n } ^ { n } } } \end{array} \right) ,
$$

where {xk}κ=0 is a sequence of $n + 1$ distinct real numbers. Vandermonde matrices arise in many applications,such as interpolation and approximation of linear functionals. Consider first the problem of constructing a polynomial

$$
p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }
$$

that interpolates data

$$
( x _ { i } , f _ { i } ) , \quad i = 0 , 1 , \ldots , n .
$$

It is easily shown that coefficients $a = ( a _ { 0 } , a _ { 1 } , \ldots , a _ { n } ) ^ { T }$ satisfy the dual Vandermonde system $V ^ { T } a = f$ . The primal system $V w = b$ arises from the problem of determining the weights $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ in a quadrature formula when given the moments

$$
w _ { 0 } x _ { 0 } ^ { i } + w _ { 1 } x _ { 1 } ^ { i } + \cdot \cdot \cdot + w _ { n } x _ { n } ^ { i } = b _ { i } , \quad i = 1 , \dots , n .
$$

Vandermonde systems are often extremely ill-conditioned because they correspond to an interpolation problem with a monomial basis. An accurate and fast algorithm for solving primal or dual Vandermonde systems in $O ( n ^ { 2 } )$ multiplications and $O ( n )$ is given by Bjorck and Pereyra [152,197o]. This algorithm corresponds to decomposition of the inverse $V ^ { - 1 }$ into a product

$$
V ^ { - 1 } = { \cal U } _ { 0 } \cdot \cdot \cdot { \cal U } _ { n - 1 } L _ { n - 1 } \cdot \cdot \cdot L _ { 0 }
$$

of upper and lower bidiagonal matrices. These algorithms are generalized to confluent Vandermonde systems by Bjorck and Elfving [140,1973]. The corresponding dual system then is a Hermite interpolation problem.

The fast Bjorck-Pereyra algorithms often achieve better accuracy in the computed solution than standard (and more expensive) methods like Gaussian elimination with partial pivoting. Indeed, some problems connected with Vandermonde systems that,traditionally,have been thought to be too ill-conditioned to be attacked, can be solved with good precision.

The determinant of a square submatrix of a matrix $A$ is called a minor of $A$ . If all minors of $A$ are positive, then $A$ is called totally positive.Let the Vandermonde matrix $V$ have points $\{ x _ { k } \} _ { k = 0 } ^ { n }$ that are positive and monotonically ordered: $0 < x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n }$ . Then from the well-known formula

$$
\operatorname* { d e t } ( V ) = \prod _ { i > j } ( x _ { i } - x _ { j } )
$$

it follows that $V = V ( x _ { 0 } , x _ { 1 } , \dots , x _ { n } )$ has positive determinant and positive leading principal minors. More generally, it is known that $V$ is totally positive. For such Vandermonde systems, Higham [612, $\mathbf { 1 9 8 7 } ]$ shows that if the right-hand side is sign-interchanging, $( - 1 ) ^ { k } b _ { k } \geq 0$ ,then the error in the solution computed by the Bjorck-Pereyra algorithm can be bounded by a quantity independent of $\kappa ( V )$

A Vandermonde-like matrix $V = \left( v _ { i j } \right)$ has elements $v _ { i j } = \phi _ { i } ( x _ { j } )$ ， $0 \leq i , j \leq n$ ，where $\{ \phi _ { i } \} _ { 0 } ^ { n }$ is a family of orthonormal polynomials that satisfy a three-term recurrence of the form (4.5.5). Such matrices generally have much smaller condition numbers than the classical Vandermonde matrices. Higham [613,1988] and Reichel [916,1991] give fast algorithms of Bjorck-Pereyra type for such systems. Demmel and Koev [311, 2oo5l prove that Bjorck-Pereyra-type algorithms exist not only for such systems but also for any totally positive linear system for which the initial minors can be computed accurately.

Let $V \in \mathbb { R } ^ { m \times n }$ be a rectangular Vandermonde matrix consisting of the first $n < m$ columns of $V ( x _ { 0 } , x _ { 1 } , \dots , x _ { m } )$ . It is natural to ask whether fast methods exist for solving the primal Vandermonde least squares problem

$$
\operatorname* { m i n } _ { x } \| V x - b \| _ { 2 } .
$$

Demeure [301,198g],[302,199o] has given an algorithm of complexity $O ( m n )$ for computing the QR factorization of $V$ ，which can be used to solve problem (4.5.34).However, because this algorithm forms $V ^ { T } V$ , it is likely to be unstable.A fast algorithm based on the Gragg-Harrod scheme [523, $\mathrm { 1 9 8 4 } ]$ for computing the QR factorization of transposed Vandermonde-like matrices is given by Reichel [916,1991]. This algorithm can be used to solve overdetermined dual Vandermonde-like systems in the least squares sense in $O ( m n )$ operations.

# Notes and references

A survey of properties of totally positive matrices is given by Fallat [393, 2Oo1]. Higham [623, 2002,Chapter 22],surveys algorithms for Vandermonde systems. The remarkable numerical stability obtained for Vandermonde systems has counterparts for other classes of structured ma-trices. Boros, Kailath,and Olshevsky [171,1999l derive fast paralel Bjorck-Pereyra-type algorithms for solving Cauchy linear equation $C x = d$ ，

$$
C = \left( \begin{array} { c c c } { \frac { 1 } { x _ { 0 } - y _ { 0 } } } & { \cdots } & { \frac { 1 } { x _ { 0 } - y _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { 1 } { x _ { n } - y _ { 0 } } } & { \cdots } & { \frac { 1 } { x _ { n } - y _ { n } } } \end{array} \right) .
$$

This class of systems includes Hilbert linear systems with sign-interchanging right-hand side. Martinez and Pena [780,1998] discuss algorithms of similar type for Cauchy-Vandermonde matrices of the form $( C V )$

# 4.5.5 - Toeplitz and Hankel Least Squares Problems

A Toeplitz matrix $T = ( t _ { i j } )$ is a matrix with constant entries along each diagonal parallel to the main diagonal. A rectangular Toeplitz matrix

$$
T = \left( \begin{array} { c c c c c c } { t _ { 0 } } & { t _ { 1 } } & { \dots } & { t _ { n } } \\ { t _ { - 1 } } & { t _ { 0 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { t _ { 1 } } \\ { t _ { - n } } & { \dots } & { t _ { - 1 } } & { t _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { t _ { - m } } & { t _ { - m + 1 } } & { \dots } & { t _ { - m + n } } \end{array} \right) \in \mathbb { R } ^ { ( m + 1 ) \times ( n + 1 ) }
$$

is defined by its $n + m + 1$ elements $t _ { - m } , \ldots , t _ { 0 } , \ldots , t _ { n }$ in the first row and column. Toeplitz matrices arise from discretization of convolution-type integral equations and play a fundamental role in signal processing, time-series analysis, econometrics,and image deblurring; see Hansen, Nagy,and O'Leary [583,2006].

The BBH algorithm of Bojanczyk,Brent,and de Hoog [162,1986] is a fast algorithm for computing the QR factorization of a Toeplitz matrix. It is related to a classical algorithm of Schur and requires $O ( m n + n ^ { 2 } )$ instead of $O ( m n ^ { 2 } )$ operations．The basic idea of the BBH algorithm is to partition $T$ in two different ways,

$$
T = \left( \begin{array} { c c } { { t _ { 0 } } } & { { u ^ { T } } } \\ { { v } } & { { T _ { 0 } } } \end{array} \right) = \left( \begin{array} { c c } { { T _ { 0 } } } & { { \tilde { u } } } \\ { { \tilde { v } ^ { T } } } & { { t _ { m - n } } } \end{array} \right) ,
$$

where $T _ { 0 }$ is a submatrix of $T$ ， $u$ and $\tilde { v }$ are $n - 1$ dimensional vectors, $v$ and $\tilde { u }$ are $m - 1$ vectors, and $t _ { 0 }$ and $t _ { m - n }$ are scalars. Let $R$ be the Cholesky factor of $T ^ { T } T$ , and partition $R$ as

$$
R = \left( \begin{array} { c c } { { r _ { 1 1 } } } & { { z ^ { T } } } \\ { { 0 } } & { { R _ { b } } } \end{array} \right) = \left( \begin{array} { c c } { { R _ { t } } } & { { \tilde { z } } } \\ { { 0 } } & { { r _ { n n } } } \end{array} \right) ,
$$

where $r _ { 1 1 }$ and $r _ { n n }$ are scalars.The factor $R$ in the QR factorization of $T$ is implicitly derived from the cross-product $T ^ { T } T$ Setting $R ^ { T } R \ : = \ : T ^ { T } T$ and using the partitioning (4.5.36) and (4.5.37), we get

$$
\left( \begin{array} { c c } { { r _ { 1 1 } ^ { 2 } } } & { { r _ { 1 1 } z ^ { T } } } \\ { { r _ { 1 1 } z } } & { { z z ^ { T } + R _ { b } ^ { T } R _ { b } } } \end{array} \right) = \left( \begin{array} { c c } { { t _ { 0 } ^ { 2 } + v ^ { T } v } } & { { t _ { 0 } u ^ { T } + v ^ { T } T _ { 0 } } } \\ { { t _ { 0 } u + T _ { 0 } ^ { T } v } } & { { u u ^ { T } + T _ { 0 } ^ { T } T _ { 0 } } } \end{array} \right)
$$

and

$$
\left( \begin{array} { l l } { R _ { t } ^ { T } R _ { t } } & { R _ { t } ^ { T } \tilde { z } } \\ { \tilde { z } ^ { T } R _ { t } } & { \tilde { z } ^ { T } \tilde { z } + r _ { n n } ^ { 2 } } \end{array} \right) = \left( \begin{array} { c c } { T _ { 0 } ^ { T } T _ { 0 } + \tilde { v } \tilde { v } ^ { T } } & { T _ { 0 } ^ { T } \tilde { u } + t _ { m - n } \tilde { v } } \\ { \tilde { u } ^ { T } T _ { 0 } + t _ { m - n } \tilde { v } ^ { T } } & { \tilde { u } ^ { T } \tilde { u } + t _ { m - n } ^ { 2 } } \end{array} \right) .
$$

From (4.5.38) and (4.5.39) we see that

$$
z z ^ { T } + R _ { b } ^ { T } R _ { b } = u u ^ { T } + T _ { 0 } ^ { T } T _ { 0 } , \qquad R _ { t } ^ { T } R _ { t } = T _ { 0 } ^ { T } T _ { 0 } + \tilde { v } \tilde { v } ^ { T } .
$$

Eliminating the term $T _ { 0 } ^ { T } T _ { 0 }$ , we obtain

$$
\boldsymbol { R _ { b } ^ { T } } \boldsymbol { R _ { b } } = \boldsymbol { R _ { t } ^ { T } } \boldsymbol { R _ { t } } + \boldsymbol { u u ^ { T } } - \boldsymbol { \tilde { v } } \boldsymbol { \tilde { v } ^ { T } } - \boldsymbol { z z ^ { T } } ,
$$

which is the basic equality used by the BBH algorithm. This shows that if $R _ { t }$ were known, $R _ { b }$ would be computed by one Cholesky updating step and two Cholesky downdating steps; see Section 3.3.4. Moreover, because updating and downdating can proceed by rows, the first $k$ rows of $R _ { b }$ can be obtained from the frst $k$ rows of $R _ { b }$ . But the $k \mathrm { t h }$ row of $R _ { b }$ defines the $( k + 1 ) \operatorname { t h }$ row of $R _ { t }$ ,and the first row of $R$ can be obtained from (4.5.38):

$$
r _ { 1 1 } = \sqrt { t _ { 0 } ^ { 2 } + v ^ { T } v } , \qquad z ^ { T } = ( t _ { 0 } u ^ { T } + v ^ { T } T _ { 0 } ) / r _ { 1 1 } .
$$

It follows that (4.5.40) provides a method for computing $R$ one row at a time.

The BBH algorithm requires $m n ^ { 2 } + 6 n ^ { 2 }$ multiplications and is more effcient than the $O ( m n ^ { 2 } )$ methods when $n > 2 5 6$ .Nagy [818,1993] modified the BBH algorithm to compute $R ^ { - 1 }$ ， $Q ^ { T } b$ ， and the solution $x$ using a linear amount of storage and $2 m n + 1 4 n ^ { 2 }$ multiplications.Another possibility is to use the corrected seminormal equations to obtain $x$ ，This can also be implemented in linear storage (see Nagy [818,1993l). Another fast algorithm by Chun, Kailath,and Lev-Ari [249, $\mathrm { 1 9 8 7 } ]$ is essentially equivalent to the BBH algorithm.

For ill-conditioned problems the BBH algorithm does not perform well, because it uses the explicit cross-product matrix. Park and Eldén [881，1997l give a forward error analysis that allows the conditioning of the problem to be monitored. For ill-conditioned problems their algorithm uses the corrected seminormal equations to produce more accurate triangular factors than those of other fast algorithms.

Discretization of a convolution-type Volterra integral equations of the first kind,

$$
\int _ { 0 } ^ { t } K ( t - s ) f ( t ) d t = g ( s ) , \quad 0 \leq t \leq T ,
$$

gives a linear system with an upper triangular Toeplitz matrix

$$
T = \left( \begin{array} { c c c c c c } { { t _ { 1 } } } & { { t _ { 2 } } } & { { \dots } } & { { t _ { n - 1 } } } & { { t _ { n } } } \\ { { } } & { { t _ { 1 } } } & { { t _ { 2 } } } & { { } } & { { t _ { n - 1 } } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { t _ { 1 } } } & { { t _ { 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { t _ { 1 } } } \end{array} \right) .
$$

For the Tikhonov regularization problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| T \boldsymbol { x } - b \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| L \boldsymbol { x } \| _ { 2 } ^ { 2 } ,
$$

where both $T$ and $L$ are upper triangular and Toeplitz, Eldén [370,1984l gives an algorithm that only requires $9 n ^ { 2 }$ flops for computing the solution for a given value of $\lambda$ .His algorithm can be modified to handle also the case when $T$ and $L$ have a few nonzero diagonals below the main diagonal. Eldén's algorithm uses $n ^ { 2 } / 2$ storage locations.A modification that only uses $O ( n )$ storage locations is given by Bojanczyk and Brent [161,1986].

An alternative to direct methods for Toeplitz least squares problems is to use iterative methods,such as the preconditioned conjugate gradient method; see Section 6.2.2. This requires in each iteration step one matrix-vector multiplication with $T$ and $T ^ { H }$ . Such products can be implemented in $O ( m \log m )$ operations and $O ( m + n )$ storage using FFT; see Section 6.3.7.

Let $T = ( t _ { i j } )$ be a Toeplitz matrix, and let $J$ denote the reverse permutation matrix. Then $H = T J$ has constant entries along each antidiagonal, i.e., $H$ is a Hankel matrix. For example, if $n = 2$ ， $m = 3$ ,then

$$
H = T J = \left( \begin{array} { c c c } { { t _ { 2 } } } & { { t _ { 1 } } } & { { t _ { 0 } } } \\ { { t _ { 1 } } } & { { t _ { 0 } } } & { { t _ { - 1 } } } \\ { { t _ { 0 } } } & { { t _ { - 1 } } } & { { t _ { - 2 } } } \\ { { t _ { - 1 } } } & { { t _ { - 2 } } } & { { t _ { - 3 } } } \end{array} \right) .
$$

Since the reverse permutation matrix satisfies $J ^ { - 1 } = J$ we have $H J = T$ Hence,methods discussed in this section for solving Toeplitz least squares problems apply to Hankel least squares problems as well.

# Notes and references

There is an extensive literature on Toeplitz matrices.Bunch [186,1985] investigates the stability properties of classical and fast algorithms for solving Toeplitz systems. Surveys can be found in Brent [179,1988] and Bojanczyk,Brent,and de Hoog [163,1993]. An $O ( m n )$ algorithm for QR factorization of Toeplitz and block Toeplitz matrices was given by Sweet [i053,1984] but was later shown to be unstable.A different approach is used by Cybenko [282,1987], who gives an algorithm for computing $R ^ { - 1 }$ and $Q \in \mathbb { R } ^ { m \times n }$ based on the so-called lattice algorithm. This algorithm requires that all submatrices $T _ { : , 1 : i }$ ， $i = 1 , \ldots , n$ ,be well-conditioned,which is not always the case in applications.Hansen and Gesmar [581,1993l give a modification of Cybenko's algorithm in which a block step is used to skip over linearly dependent columns. For solving symmetric positive definiteToeplitz linear systems,a “superfast” algorithm that only requires $\bar { O ( m \log ^ { 2 } n ) }$ operations has been proposed; see Ammar and Gragg [2O,1988].

Chapter 5

# Direct Methods for Sparse Problems

A sparse matrix is any matrix with enough zeros that it pays to take advantage of them.

—J. H. Wilkinson

# 5.1 - Tools for Sparse Matrix Computations

# 5.1.1 - Introduction

A band matrix,whose nonzero elements are concentrated near the main diagonal, is a simple example of a sparse matrix.Methods for solving band least squares problems have been treated in Section 4.1. A significant part of large-scale scientific computing applications involves sparse matrices with more irregular sparsity paterns. By only storing and operating on nonzero elements in sparse matrices,large savings in computing time and memory can be achieved and can make otherwise intractable problems practical to solve.Examples include the fields of structural analysis,geodetic surveying, management science,and power systems analysis. This chapter treats effective direct methods for the solution of sparse least squares problems using Cholesky and QR factorizations. As the computation proceeds,one must try to minimize fill,which is the term used to denote the creation of new nonzero elements within sparse factors of the sparse matrix.

We initially assume that $A \in \mathbb { R } ^ { m \times n }$ has full column rank, although problems where rank $( A )$ $\mathbf { \mu } = m < n$ or $\operatorname { r a n k } ( A ) < \operatorname* { m i n } ( m , n )$ do occur in practice.Other issues,such as dimension, sparsity structure,and conditioning,should be considered when choosing the method to be used. Occurrence of weighted rows,the number of right-hand sides,and constraints on the solution must also be considered. If only part of the solution vector $x$ is needed, savings can be achieved. It may also be possible to take advantage of a sparse right-hand side $b$

An example of a symmetric irregular pattern arising from a structural problem in aerospace is illustrated in Figure 5.1.1. Other application areas can give patterns with quite diferent characteristics.

Solving a sparse least squares problem $\operatorname* { m i n } \| A x - b \| _ { 2 }$ of full column rank using the method of normal equations is usually performed in several steps as follows.

1. A symbolic phase in which a column permutation $P _ { c }$ is determined that approximately minimizes the number of nonzeros elements in the Cholesky factor $R$ of $( A P _ { c } ) ^ { T } ( A P _ { c } )$

![](images/5af3228f08edad849f19dc8b4f70608f4763c5c7f14a6e8a3caa0d61df185b98.jpg)  
Figure 5.1.1. Nonzero patern of a matrix arising from a structural problem and its Cholesky factor.

This step only works on the nonzero structure of $A$ and also generates a storage structre for $R$

2. A numerical phase in which $C = ( A P _ { c } ) ^ { T } ( A P _ { c } )$ is formed numerically and its Cholesky factor $R$ is computed and stored in the data structure generated in the symbolic phase.

3.For the given right-hand side $b$ form $c = P _ { c } ^ { T } A ^ { T } b$ solve $R ^ { T } z = c$ $R y \ : = \ : z$ and set $x = P _ { c } y$

Sparse QR factorization can give substantial improvements in accuracy compared to Cholesky factorization.As the factor $R$ is mathematically the same for both factorizations,the symbolic phase from the Cholesky factorization can be used. However,as for band least squares problems, the intermediate filland arithmetic cost for QR depend strongly on the row ordering.

There are several collections of sparse matrices arising from a wide range of applications that are used for development, testing,and performance evaluation for sparse matrix computations. One of the first was the Harwell-Boeing collection by Duff, Grimes,and Lewis [346,1989]. This was followed by the Matrix Market collection by Boisvert et al.[160,1997l, which has now been incorporated into the larger SuiteSparse collection by Davis and Hu [291, 2o11]. Whereas the largest matrix in Matrix Market has dimension 90,449 with 2.5 million nonzeros,the largest in the SuiteSparse collection has dimension 28 million with 76O million nonzeros!

# Notes and references

The literature on sparse matrix algorithms is extensive. George and Liu [457,1981] is an early classical text on sparse Cholesky factorization. Graph theory and its connections to sparse matrix computations are treated in George, Gilbert, and Liu [454,1993]. An excelent survey of the state of the art of direct methods for sparse linear systems is given by Davis [289,2oo6]; see also Davis,Rajamanickam,and Sid-Lakhdar [292,2o16] and Duff, Erisman,and Reid [345,2017]. A recent addition that complements theory with detailed outlines of algorithms and emphasizes the importance of sparse matrix factorizations for constructing preconditioners for iterative least squares methods is Scott and Tüma [991, 2023].

# 5.1.2 - Storage and Operations on Sparse Matrices

The main objective of storage schemes for sparse vectors and matrices is to economize on storage while facilitating subsequent operations.An important distinction is between static storage structures that remain fixed and a dynamic structure that can accommodate fill. A static structure like the general sparse storage scheme can be used when the number and location of the nonzeros in the matrix factors can be predicted. Otherwise,the data structure for the factors must dynamically allocate sufficient space for fill during the elimination.

It is useful to be able to predict fill that will occur in a matrix factorization so that storage structures can be fixed in advance.To do this,one usually appeals to a no-cancellation assumption: when two nonzero numerical quantities are added or subtracted, the result is assumed to be nonzero. The structural rank of a matrix is defined to be the maximum rank of all numerical matrices with the same nonzero pattern. For example, the matrix

$$
\left( \begin{array} { c c c } { { c _ { 1 1 } } } & { { 0 } } & { { c _ { 1 3 } } } \\ { { 0 } } & { { 0 } } & { { 0 } } \\ { { c _ { 3 1 } } } & { { 0 } } & { { c _ { 3 3 } } } \end{array} \right)
$$

has structural rank two, but if $c _ { 1 1 } c _ { 3 3 } - c _ { 1 3 } c _ { 3 1 } = 0$ ,the numerical rank is one.

In the following we denote the number of nonzero elements in a sparse matrix (or vector) by $n n z$ . A sparse vector $x$ can be stored in compressed form as the triple $( x C , i x , n n z )$ . Its $n n z$ nonzero elements are stored in the vector $x C$ . The indices of the elements in $x C$ are stored in the integer vector $_ { i x }$ ,so that

$$
x C _ { k } = x _ { i x ( k ) } , \quad k = 1 , \ldots , n n z .
$$

For example, in compressed form the vector $x = ( 0 , 4 , 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 )$ is stored as

$$
x C = ( 1 , 4 , 6 ) , \quad i x = ( 5 , 2 , 9 ) , \quad n n z = 3 .
$$

Note that it is not necessary to store the nonzero elements in any particular order in $x C$ This makes it easy to add further nonzero elements in $x$ —they can be appended in the last positions of $x C$ and $_ { i x }$

In the general sparse storage scheme for a sparse matrix $A$ ,nonzero elements are stored in coordinate form $( A C , i x , j x , n n z )$ ,that is,as an unordered one-dimensional array $A C$ with two integer vectors $_ { i x }$ and $j x$ containing the corresponding row and column indices,

$$
A C ( k ) = a _ { i j } , \quad i = i x ( k ) , \quad j = j x ( k ) , \quad k = 1 , \ldots , n n z ,
$$

where $n n z$ is the number of nonzero elements in $A$ ．This scheme is very convenient for the initial representation of a general sparse matrix because additional nonzero elements can be easily added to the structure.A drawback is that it is diffcult to access $A$ by rows or columns, as is usually needed in later operations. Also,the storage overhead is large because two integer vectors of length $n n z$ are required. This overhead can be decreased by using a clever compressed scheme due to Sherman; see George and Liu [457,1981,pp. 139-142].

In compressed storage by rows (CSR) a sparse matrix is stored as the collection of its sparse rows. For each row, the nonzeros are stored in $A C$ in compressed form. The corresponding column subscripts are stored in integer vector $j a$ ,so that the column subscript of element $A C ( k )$ is in $j a ( k )$ ．A third vector $i p$ gives the position in $A C$ of the first element in the ith row of $A$

In CSR the matrix

$$
A = \left( \begin{array} { c c c c c } { a _ { 1 1 } } & { 0 } & { a _ { 1 3 } } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { 0 } & { a _ { 2 4 } } & { 0 } \\ { 0 } & { 0 } & { a _ { 3 3 } } & { 0 } & { 0 } \\ { 0 } & { a _ { 4 2 } } & { 0 } & { a _ { 4 4 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { a _ { 5 4 } } & { a _ { 5 5 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { a _ { 6 5 } } \end{array} \right)
$$

would be stored as

$$
\begin{array} { r l } & { A C = ( a _ { 1 1 } , \ a _ { 1 3 } \ | \ a _ { 2 2 } , \ a _ { 2 1 } \ a _ { 2 4 } \ | \ a _ { 3 3 } \ | \ a _ { 4 2 } , \ a _ { 4 4 } \ | \ a _ { 5 4 } , \ a _ { 5 5 } \ | \ a _ { 6 5 } ) , } \\ & { \ j a = ( 1 , \ 3 , \ 2 , \ 1 , \ 4 , \ 3 , \ 2 , \ 4 , \ 4 , \ 5 , \ 5 ) , } \\ & { \ i p = ( 1 , \ 3 , \ 6 , \ 7 , \ 9 , \ 1 1 ) . } \end{array}
$$

The components in each row need not be ordered. To access a nonzero $a _ { i j }$ there is no direct way to calculate the corresponding index in the vector $A C$ ； some testing is needed on the subscripts in $j a$ . In CSR storage form,a complete row of $A$ can be retrieved efficiently,but elements in a particular column cannot be retrieved without a search of nearly all elements. Alternatively, a similar compressed storage by columns (CsC) form can be used.

For a sparse symmetric matrix it suffices to store either its upper or its lower triangular part, including the main diagonal. If the matrix is positive definite,then allits diagonal elements are positive,and it may be convenient to store them in a separate vector.

For problems in which all the nonzero matrix elements lie along a few subdiagonals the compressed diagonals storage mode is suitable.A matrix $A$ is then stored in two rectangular arrays $A D$ and a vector $l a$ of pointers. The array $A D$ has $n$ rows and nd columns,where $^ { n d }$ is the number of diagonals. $A D$ contains the diagonals of $A$ that have at least one nonzero element, and $l a$ contains the corresponding diagonal numbers. The superdiagonals are padded to length $n$ with $k$ trailing zeros,where $k$ is the diagonal number. The subdiagonals are padded to length $n$ with $| k |$ leading zeros.This storage scheme is particularly useful if the matrices come from a finite element or finite discretization on a tensor product grid. The matrix $A$ in (5.1.1) would be stored as

$$
A D = \left( \begin{array} { c c c c } { { a _ { 1 1 } } } & { { a _ { 1 3 } } } & { { a _ { 2 1 } } } & { { 0 } } \\ { { a _ { 2 2 } } } & { { a _ { 2 4 } } } & { { 0 } } & { { a _ { 4 2 } } } \\ { { a _ { 3 3 } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { a _ { 4 4 } } } & { { 0 } } & { { a _ { 5 4 } } } & { { 0 } } \\ { { a _ { 5 5 } } } & { { 0 } } & { { a _ { 6 5 } } } & { { 0 } } \end{array} \right) , \qquad l a = ( 0 \ 2 \ - 1 \ - 2 ) .
$$

Operations on sparse vectors are simplified if one of the vectors is first uncompressed, i.e., stored as a dense vector. This can be done in time proportional to the number of nonzeros,and it allows direct random access to specified elements in the vector. Vector operations, such as adding a multiple of a sparse vector $x$ to an uncompressed sparse vector $y$ or computing an inner product $x ^ { T } y$ ,can then be performed in constant time per nonzero element. For example,assume $x$ is held in compressed form and $y$ in a full-length array. Then the operation $y : = a * x + y$ may be expressed as

$$
\begin{array} { c } { { \mathrm { f o r } k = 1 , \ldots , n n z } } \\ { { i = i x ( k ) ; \quad y ( i ) : = a * x ( k ) + y ( i ) ; } } \end{array}
$$

end

Efficient implementations of sparse matrix-vector products such as $A v$ and $A ^ { T } u$ are important in both direct and iterative methods for sparse linear least squares problems.The storage structure for $A$ should be chosen so that hardware features like vector registers can be exploited.

Some of the more common structures are described below. Let $u \in \mathbb { R } ^ { m }$ and $v \in \mathbb { R } ^ { n }$ be uncom-pressed vectors,and let $A$ be stored in CSR mode. Then the matrix-vector product $u = A v$ can be implemented as

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { y r } i = 1 : m , } } \\ { { } } & { { } } & { { u ( i ) = 0 ; } } \\ { { } } & { { } } & { { \mathrm { f o r } k = i p ( i ) : i p ( i + 1 ) - 1 , } } \\ { { } } & { { } } & { { u ( i ) = u ( i ) + A C ( k ) * v ( j a ( k ) ) ; } } \end{array}
$$

For the product $v = A ^ { T } u$ a similar code would access the elements of $A$ column by column, which is very inefficient. The product is better performed as

$$
\begin{array} { r l } & { v ( 1 : n ) = 0 ; } \\ & { \mathrm { f o r } i = 1 : m } \\ & { \quad \mathrm { f o r } k = i p ( i ) : i p ( i + 1 ) - 1 , } \\ & { \quad \quad j = j a ( k ) ; \quad v ( j ) = v ( j ) + A C ( k ) \ast u ( i ) ; } \end{array}
$$

A proposal for standard computational kernels (BLAS) aimed at iterative solvers is given by Duff et al. [349,1997]. The interface of the sparse BLAS in the standard from the BLAS technical forum is designed to shield one from concern over specific storage schemes; see Duff, Heroux,and Pozo [347, 2002].

# 5.1.3 - Graphs and Sparse Matrices

A graph $G = ( V , E )$ consists of a set of vertices or nodes $V = \{ v _ { 1 } , \ldots , v _ { n } \}$ and a set of edges $E$ . In an undirected graph an edge is an unordered pair of its vertices $( v _ { i } , v _ { j } )$ . A graph is directed if the edges $( v _ { i } , v _ { j } )$ are directed from $v _ { i }$ to $v _ { j }$ . Two vertices $v _ { i }$ and $v _ { j }$ in a graph $G$ are said to be adjacent if there is an edge $( v _ { i } , v _ { j } ) \in E$ .The edge is incident to the vertices $v _ { i }$ and $v _ { j }$

The nonzero structure of a symmetric matrix $C \in \mathbb { R } ^ { n \times n }$ can be modeled by an undirected adjacency graph $G ( C ) = ( V , E )$ with $n$ vertices $V = \{ 1 , \ldots , n \}$ and edges

$$
E = \{ ( i , j ) \mid c _ { i j } = c _ { j i } \neq 0 , i \neq j \} .
$$

The structure of a square unsymmetric matrix $C$ can be represented by a directed graph $G =$ $( X , E )$ ,where $( v _ { i } , v _ { j } )$ is a directed edge from $v _ { i }$ to $v _ { j }$ if and only if $c _ { i j } \neq 0$

The adjacency set of a vertex $v _ { i }$ in $G$ is defined as

$$
\mathrm { A d j } _ { G } ( v _ { i } ) = \{ v _ { j } \in V \mid v _ { i } \mathrm { a n d } v _ { j } \mathrm { a r e } \mathrm { a d j a c e n t } \} .
$$

The degree of a vertex $v _ { i }$ is the number of vertices adjacent to $v _ { i }$ and is denoted by $| \mathrm { A d j } _ { G } ( v _ { i } ) |$ A graph $\bar { G } = ( \bar { V } , \bar { E } )$ is a subgraph of $G = ( V , E )$ if $\bar { V } \subset V$ and $\bar { E } \subset E$ A walk of length $k$ in an undirected graph is an ordered sequence of $k + 1$ vertices $v _ { 1 } , \ldots , v _ { k + 1 }$ such that

$$
( v _ { i } , v _ { i + 1 } ) \in E , \quad i = 1 , \dots , k .
$$

A walk is a path if all edges are distinct. If $v _ { 1 } = v _ { k + 1 }$ , the walk is closed and called a cycle. Two nodes are said to be connected if there is a path between them. The distance between two vertices in a graph is the number of edges in the shortest path connecting them.A graph is said to be connected if every pair of distinct vertices is connected by a path. A graph that is not connected consists of at least two separate connected subgraphs.If $G = ( X , E )$ is a connected graph, then $Y \subset V$ is called a separator if $G$ becomes disconnected after removal of the nodes $Y$ . A directed graph is strongly connected if there is a path between every pair of distinct nodes along directed edges.

Graphs that do not contain cycles are called acyclic. A connected acyclic graph is called a tree; see Figure 5.1.2. In a tree,any pair of vertices is connected by exactly one path. A tree has at least two vertices of degree 1. Such vertices are called leaf vertices. If a graph $G$ is connected, then a spanning tree is a subgraph of $G$ that is a tree.In a tree an arbitrary vertex $r$ can be specified as the root of the tree. Then the tree becomes a directed rooted tree. An edge $( v _ { i } , v _ { j } ) \in G$ in a directed rooted tree is a directed edge from $v _ { i }$ to $v _ { j }$ if there is a path from $v _ { i }$ to $r$ such that the first edge of this path is from $v _ { i }$ t0 $v _ { j }$ . If there is a directed edge from $v _ { i }$ t0 $v _ { j }$ ， then $v _ { j }$ is called the parent of $v _ { i }$ ,and $v _ { i }$ is said to be a child of $v _ { j }$

A labeling(or ordering) of a graph $G$ with $n$ vertices is a mapping of the integers $\{ 1 , 2 , \ldots , n \}$ onto the vertices of $G$ .The integer $i$ assigned to a vertex is called the label (or number) of that vertex.A labeling of the adjacency graph of a symmetric matrix $C$ corresponds to a particular ordering of its rows and columns. For example, the graph of the structurally symmetric matrix

$$
\left( \begin{array} { l l l l l l } { \times } & { \times } & { } & { \times } & { \times } & { } \\ { \times } & { \times } & { \times } & { } & { } & { } \\ { } & { \times } & { \times } & { } & { } & { \times } & { \times } \\ { \times } & { } & { } & { \times } & { } & { } \\ { \times } & { } & { } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { } & { \times } & { } \\ { } & { } & { } & { } & { } & { \times } & { } \end{array} \right)
$$

is given in Figure 5.1.2.

![](images/804461651ff765da2ee2acbb913fb71835cfbd8efd901e65a12b612a7a5fa53d.jpg)  
Figure 5.1.2. The labeled graph $G ( C )$ of the matrix in (5.1.2).

The matrix of normal equations can be written as

$$
C = A ^ { T } A = \sum _ { i = 1 } ^ { m } a _ { i } a _ { i } ^ { T } ,
$$

where $a _ { i } ^ { T }$ is the $i$ th row of $A$ . This expresses $A ^ { T } A$ as the sum of $m$ matrices of rank one. By the no-cancellation assumption, the nonzero structure of $A ^ { T } A$ is the direct sum of the nonzero elements of the matrices $a _ { i } a _ { i } ^ { T }$ ， $i = 1 , \ldots , m$ . It follows that the graph $G ( A ^ { T } A )$ is the direct sum of the graphs $G ( a _ { i } a _ { i } ^ { T } )$ ， $i = 1 , \ldots , m$ . That is,its edges are the union of all edges not counting multiple edges. In $G ( a _ { i } a _ { i } ^ { T } )$ all pairs of vertices are connected. Such a graph is called a clique and corresponds to a dense submatrix in $A ^ { T } A$ .Clearly, the structure of $A ^ { T } A$ is not changed by dropping any row of $A$ whose nonzero structure is a subset of another row.

By the no-cancellation assumption,an alternative characterization of $G ( A ^ { T } A )$ is that $( A ^ { T } A ) _ { j k } \ \ne \ 0$ if and only if columns $j$ and $k$ intersect, i.e., if $a _ { i j } \neq 0$ and $a _ { i k } \neq 0$ for at least one row $i \in \{ 1 , \ldots , m \}$ . Therefore, $G ( A ^ { T } A )$ is also known as the column intersection graph of $A$

# 5.1.4- A Graph Model of Cholesky Factorization

The use of graphs to symbolically model the Cholesky factorization of a sparse symmetric matrix $C$ is due to Parter [886,1g61], although the details were later given by Rose [935,1972]. In sparse Cholesky factorization each row of the Cholesky factor $R$ depends on only a subset of the previous rows. The fill in the factorization can be analyzed by recursively forming a sequence of elimination graphs

$$
G _ { 0 } = G ( C ) , \quad G _ { i } ( C ) , \quad i = 1 , \ldots , n - 1 ,
$$

where $G _ { i } ( C )$ is formed from $G _ { i - 1 } ( C )$ by removing vertex $i$ and its incident edges and adding fill edges that make adjacent vertices in $G _ { i - 1 } ( C )$ pairwise adjacent. The sequence of elimination graphs for the matrix in (5.1.2) is pictured in Figure 5.1.3.It can be verified that the number of fill elements (edges) is 10.

![](images/3acd0062d6ec14b69034a957ca018f6ce4d05d49d85e79bc250f45b107227b3c.jpg)  
Figure 5.1.3. Sequence of elimination graphs of the matrix in (5.1.2).

The filled graph $G _ { F } ( C )$ is a graph with $n$ vertices and edges corresponding to al graphs $G _ { 0 } = G , G _ { i } , i = 1 , \ldots , n - 1$ . It bounds the structure of the Cholesky factor $R$ ：

$$
G ( R ^ { T } + R ) \subset G _ { F } ( C ) .
$$

Under a no-cancelltion assumption, (5.1.4) holds with equality.

Theorem 5.1.1. Let $G ( C ) = ( V , E )$ be the undirected graph of the symmetric matrix $C$ Then $( v _ { i } , v _ { j } )$ is an edge of the filled graph $G _ { F } ( C )$ if and only $i f \left( v _ { i } , v _ { j } \right) \in E$ ，or there is a path in $G ( C )$ from vertex $i$ to vertex $j$ passing only through vertices $v _ { k }$ with $k < \operatorname* { m i n } ( i , j )$

The filled graph $G _ { F } ( C )$ can be characterized by an elimination tree $T ( C )$ that captures the row dependencies in the Cholesky factorization.

Definition 5.1.2. The elimination tree of a symmetric matrix $C \in \mathbb { R } ^ { n \times n }$ with Cholesky factor $R$ is a directed rooted tree $T ( C )$ with $n$ vertices labeled from $1$ to $n _ { \ast }$ ，where vertex $p$ is the parent of node i if and only if

$$
p = \operatorname* { m i n } _ { j } \{ j > i | r _ { i j } \neq 0 \} .
$$

$T ( C )$ is uniquely represented by the parent vector $P A R E N T [ i ]$ ， $i = 1 , \ldots , n$ ，of the vertices of the tree. For example,the parent vector of the elimination tree in Figure 5.1.3 is $5 , 5 , 6 , 6 , 7 , 7 , 8 , 0$

$T ( C )$ can be obtained from the filled graph $G _ { F } ( C )$ by introducing directed edges from lower to higher numbered vertices.A directed edge from node $j$ to node $i > j$ indicates that row $i$ depends on row $j$ . This row dependency is exhibited by the following transitive reduction of $G _ { F } ( C )$ . If there is a directed path from $j$ to $i$ of length greater than one,the edge from $j$ to $i$ is redundant and thus removed. The elimination tree is generated by the removal of all such redundant edges.For the matrix $A$ in (5.1.2) the filled graph $G _ { F } ( A ^ { T } A )$ equals $G ( A ^ { T } A )$ with an added edge between vertices 7 and 9. The result of the transitive reduction and the elimination tree is shown in Figure 5.1.4.

![](images/5c0c60cc6aa8010bdc25b46016262df7f06342e7ae39b0e4b9f297312d760412.jpg)  
Figure 5.1.4. The transitive reduction and elimination tree $T ( A ^ { T } A )$

The node ordering of an elimination tree is such that children vertices are numbered before their parent node. Such orderings are called topological orderings. Al topological orderings of the elimination tree are equivalent in the sense that they give the same triangular factor $R$ A postordering is a topological ordering in which a parent node $j$ always has node $j - 1$ as one of its children. For example,the ordering of the vertices in the tree in Figure 5.1.4 can be made into a postordering by exchanging labels 3 and 5. Postorderings can be determined by a depth-first search; see Liu [755,199o]. An important advantage of using a postordering is that it simplifies data management, and the storage is reduced.

Elimination trees play a fundamental role in symmetric sparse matrix factorization and provide,in compact form,all information about the row dependencies. Schreiber [974,1982] was the first to note this and to define elimination trees formally. In the excellent review of the generation and use of elimination trees by Liu [755,199o] an eficient algorithm is given that determines the elimination tree of $C$ in time proportional to $\mathrm { n n z } ( R )$ and in storage proportional t0 $\mathtt { n n z } ( C )$ . When $C = A ^ { T } A$ it is possible to predict the structure of $R$ directly without forming $C$ ； see Gilbert,Moler,and Schreiber [469,1992].

# 5.1.5 - Minimizing Fillin Cholesky Factorization

The sparsity of the Cholesky factor $R$ of $A ^ { T } A$ depends on the ordering of the columns of $A$ but not on the ordering of the rows. In the symbolic phase of sparse Cholesky factorization a column permutation $P$ is determined that tries to limit the fill in $R$ .It would be desirable to find a column ordering that minimizes the number of nonzeros in $R$ .However, this is known to be an NP-complete problem,i.e.,it cannot be solved in polynomial time. Even the problem of finding an ordering that minimizes the bandwidth of $R$ is NP-complete; see Papadimitriou [876,1976]. Hence we have to rely on heuristic methods.A simple algorithm is to order the columns in $A$ after increasing the number of nonzero elements in the columns. More effective methods can be obtained by using information from successively reduced submatrices.

We first consider ordering methods that have the objective of minimizing the bandwidth of $A ^ { T } A$ or rather the number of elements in the envelope of $C = A ^ { T } A$ Recall that by Theorem 4.1.6, zeros outside the envelope of $C$ will not suffer fill in the Cholesky factorization. Such ordering methods often perform well for matrices that come from one-dimensional problems or problems that are in some sense tall and thin. The most widely used such method is the Cuthill-McKee (CM) algorithm [281,1969]. It starts by finding a peripheral vertex $r$ (i.e., a vertex with lowest degree) in $G ( C )$ and numbering this as vertex 1. It then performs a breadth-first search using a level structure rooted at $r$ .This partitions the vertices into disjoint levels

$$
L _ { 1 } = r , L _ { 2 } ( r ) , \ldots , L _ { h } ( r ) ,
$$

where $L _ { i } ( r ) , i \le h$ ， is the set of all vertices adjacent to $\boldsymbol { L } _ { i - 1 } ( \boldsymbol { r } )$ that are not in $L _ { j } ( r ) , j =$ $1 , \ldots , i - 1$ . The search ends when all vertices are numbered.

# Algorithm 5.1.1 (Cuthill-McKee Ordering).

1. Select a peripheral vertex $r$ , and set $L _ { 1 } = { \binom { r } { } }$

2. for $i = 1 , 2 , \dots$ until all vertices are numbered do:

Find all unnumbered vertices in Adj $( L _ { i } )$ and number them

after increasing degrees.

George [453,1971] observed that the ordering obtained by reversing the Cuthill-McKee (RCM) ordering gives the same bandwidth and usually results in less fill. An implementation of the RCM algorithm with run-time proportional to the number of nonzeros in the matrix is given by Chan and George [230,198o]. The performance of the RCM ordering strongly depends on the choice of the starting peripheral node. George and Liu [457,1981] recommend a strategy where a node of maximal or nearly maximal eccentricity is chosen as a starting node. The eccentricity of a node is defined as

$$
l ( x ) = \operatorname* { m a x } _ { y \in X } d ( x , y ) ,
$$

where $d ( x , y )$ is the length of the shortest path between the two vertices $x$ and $y$ in $G = ( \boldsymbol { X } , E )$

A substantially faster algorithm for bandwidth minimization is the GPS algorithm by Gibbs, Poole,and Stockmeyer [467,1976].Lewis [738,1982], [737,1982] describes some improvements to the implementation of the GPS and other profile reduction algorithms. Sloan [1004, 1986] gives a new algorithm that generally results in a smaller profile. Among other proposed methods for envelope reduction,we mention the spectral method of Barnard,Pothen, and Simon [81,1995]. This uses the eigenvector of the smallest positive eigenvalue of the Laplacian matrix corresponding to the given matrix.

The minimum degree (MD) ordering is the most widely used heuristic method for limiting fill. The name “minimum degree” comes from the graph-theoretic formulation of the Cholesky algorithm first given by Rose [935,1972]; see Section 5.1.3. MD is a greedy method that in each step of the Cholesky factorization selects the next pivot as the sparsest row and column. It is a symmetric analogue of an ordering algorithm proposed by Markowitz [778,1957] for unsymmetric matrices with applications to linear programming. This algorithm was adapted for symmetric matrices by Tinney and Walker [1O64,1967]. The MD ordering minimizes the local arithmetic and amount of fillthat occurs but in general will not minimize the global arithmetic or fill. However, it has proved to be very effective in reducing both of these objectives. If the graph of $C = A ^ { T } A$ is a tree, then the MD ordering results in no fill.

# Algorithm 5.1.2 (Minimum Degre Ordering).

Set $G ^ { ( 0 ) } = G ( C )$ and determine the degrees ofits vertices.

for $i = 1 , \ldots , n - 1$ do

1. Select a vertex of minimal degree in $G ^ { ( i - 1 ) }$ as pivot.

2. Construct the elimination graph $G ^ { ( i ) }$ and update the degrees of its vertices.

For the matrix $C$ in (5.1.2) the initial elimination order indicated gives 1O fll-in elements. A minimum degree ordering such as $4 , 5 , 6 , 7 , 1 , 2 , 3$ will result in no fill-in.Because several vertices in the graph have degree 1, the minimum degree ordering is not unique.

If there is more than one node of minimum degree at a particular step, the node is chosen from the set of all vertices of minimum degree. The way this tie-breaking is done can be important. Examples are known for which the minimum degree ordering will give poor results if the tiebreaking is systematically done poorly. It is an open question how good the orderings are if ties are broken randomly. A matrix for which the minimum degree algorithm is not optimal is given by Duff,Erisman,and Reid [344,1g86]. If the minimum degree node 5 is eliminated first, fill will occur in position $( 4 , 6 )$ . But with the elimination ordering shown in Figure 5.1.5,there is no fill. In the multiple minimum degree algorithm (MMD) by George and Liu [459,1989] a refinement of the elimination graph model is used to decrease the number of degree updates. The vertices $Y = \{ y _ { 1 } , \dots , y _ { p } \}$ are called indistinguishable if they have the same adjacency sets (including the node itself),i.e.,

$$
\operatorname { A d j } \left( v _ { i } \right) \cup v _ { i } = \operatorname { A d j } \left( v _ { j } \right) \cup v _ { j } , \quad 1 \leq i , j \leq p .
$$

If one of these vertices is eliminated,the degrees of the remaining vertices in the set will decrease by one,and they all will become of minimum degree. Hence,all vertices in $Y$ can be eliminated simultaneously,and the graph transformation needs to be updated only once. Indeed, indistinguishable vertices can be merged and treated as one supernode. For example,the graph in Figure 5.1.5 contains two sets $\{ 1 , 2 , 3 \}$ and $\{ 7 , 8 , 9 \}$ of supervertices.

![](images/b142a4bae7be4f6ec5f97d9214638d3a1e44fd663fa9c44df34572f96622c8e1.jpg)  
Figure 5.1.5.The graph of a matrix for which minimum degree is not optimal.

The structure of each row in $A \in \mathbb { R } ^ { m \times n }$ corresponds to a clique in the graph of $C = A ^ { T } A$ Thus,the generalized element approach can be used to represent $C$ as a sequence of cliques. This allows the minimum degree algorithm for $A ^ { T } A$ to be implemented directly from $A$ without forming the structure of $C = A ^ { T } A$ , with resulting savings in work and storage.

The most costly part of the minimum degree algorithm is recomputation of the degree of the vertices adjacent to the new pivot column. In the approximate minimum degree (AMD) algorithm an upper bound on the exact minimum degree is used instead, which leads to substantial savings in run-time, especially for very irregularly structured matrices. It has no effect on the quality of the ordering; see Amestoy, Davis,and Duff [18, 2004].

# 5.2 - Sparse QR Factorization

# 5.2.1 - Predicting Structure in Sparse QR

The factor $R$ in the QR factorization of $A$ is the same as the Cholesky factor of $A ^ { T } A$ Therefore, it may seem that the same symbolic algorithm can be used to determine the structure of $R$ in both Cholesky and QR factorizations.If $A$ contains at least one dense row, then by the nocancellation assumption it follows that $A ^ { T } A$ is full,and we conclude that the Cholesky factor $R$ is full.However, this may considerably overestimate the number of nonzeros in $R$ .For example, consider the matrices with nonzero structures,

$$
A _ { 1 } = \left( \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & & & \\ & { \times } & { \times } & & \\ & & { \times } & { \times } & \\ & & & { \times } & { \times } \end{array} \right) , \qquad A _ { 2 } = \left( \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & & \\ & & { \times } & { \times } & \\ & & & { \times } & { \times } \\ & & & & { \times } \end{array} \right) .
$$

For both $A _ { 1 }$ and $A _ { 2 }$ the matrix of normal equations is full. But $A _ { 2 }$ is already upper triangular, and hence $R = A _ { 2 }$ is sparse.For $A _ { 2 }$ there will be cancellation in the Cholesky factorization of $A _ { 2 } ^ { T } A _ { 2 }$ that will occur irrespective of the numerical values of the nonzero elements. This is called structural cancellation, in contrast to numerical cancellation that occurs only for certain values of the nonzero elements. Coleman, Edenbrandt,and Gilbert [262,1986] prove that if $A$ has the so-called strong Hall property, then structural cancellation cannot occur.

Definition 5.2.1. A matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ , is said to have the strong Hall property if for every subset of $k$ columns, $0 < k < n$ ，the corresponding submatrix has nonzeros in at least $k + 1$ rows. That is, when $m > n$ ,every subset of $k \leq n$ columns has the required property, and when $m = n$ ,every subset of $k < n$ columns has the property.

Theorem 5.2.2. Let $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ ， have the strong Hall property. Then the structure of $A ^ { T } A$ correctly predicts that of $R$ ,excluding numerical cancellations.

Note that $A _ { 2 }$ in (5.2.1) does not have the strong Hall property because the first column has only one nonzero element. However, the matrix $\tilde { A }$ obtained by deleting the first column has this property.

The structure of $R$ in QR factorization can also be predicted by performing the Givens or Householder QR algorithm symbolically. In Givens QR factorization, the intermediate fill can be modeled using the bipartite graph $G ( A ) = \{ R , C , E \}$ 、Here the two sets of vertices

$$
\mathcal { R } = ( r _ { 1 } , \ldots , r _ { k } ) , \quad \mathcal { C } = ( c _ { 1 } , \ldots , c _ { k } )
$$

correspond to the sets of rows and columns of $A$ $E$ is a set of edges $\{ r _ { i } , c _ { j } \}$ that connects a node in $\mathcal { R }$ to one in $\mathcal { C }$ ,and $\{ r _ { i } , c _ { j } \} \in E$ if and only if $a _ { i j }$ is nonzero; see George, Liu, and $\mathrm { N g }$ [465, $\mathrm { 1 9 8 4 } ]$ and Ostrouchov [851,1987]. The following result is due to George and Heath [455, 1980].

Theorem 5.2.3. The structure of $R$ as predicted by a symbolic factorization of $A ^ { T } A$ includes the structure of $R$ as predicted by the symbolic Givens method.

Manneback [772,1985] proves that the structure predicted by a symbolic Householder algorithm is strictly included in the structure predicted from $A ^ { T } A$ .Symbolic Givens and Householder factorizations can also overestimate the structure of $R$ .An example where structural cancellation occurs for the Givens rule is shown by Gentleman [452,1976].

# 5.2.2 - The Row Sequential QR Algorithm

One of the first algorithms for sparse QR factorization was given by George and Heath [455, 1980]. In this,a symbolic factorization of $A ^ { T } A$ is used to form a static data structure for $R$ .Then $A$ is merged into this data structure row by row using Givens rotations,avoiding intermediate fill-in.

Although the final factor $R$ in QR factorization is independent of the ordering of the rows in $A$ ，the row ordering can significantly affect the intermediate fll and the number of Givens rotations needed to compute the factorization. This fact was stressed in the treatment of QR algorithms for band matrices; see Section 4.1. An extreme example is shown below, where the cost for factorizing $A$ is reduced from $O ( m n ^ { 2 } )$ to $O ( n ^ { 2 } )$ ：

$$
A = \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ { \times } & & & \\ { \vdots } & & & \\ { \times } & & & \\ { \times } & & & \\ & { \times } & & \\ & & { \times } & \\ & & & { \times } \end{array} \right) , \qquad P A = \left( \begin{array} { l l l l } { \times } & & & \\ { \times } & & & \\ { \vdots } & & & \\ { \times } & & { \times } & \\ & { \times } & { \times } & { \times } \\ & & { \times } & \\ & & & { \times } \end{array} \right) .
$$

Several heuristic algorithms for determining a row ordering have been suggested. The following is an extension of the row ordering recommended for band sparse matrices.

# Algorithm 5.2.1 (Row-Ordering Algorithm).

Denote the column index for the first and last nonzero elements in the ith row of $A$ by $f _ { i } ( A )$ and $\ell _ { i } ( A )$ ,respectively.

1. Sort the rows by increasing $f _ { i } ( A )$ ,so that $f _ { i } ( A ) \leq f _ { k } ( A )$ if $i < k$

2. For each group of rows with $f _ { i } ( A ) = k ,$ $k = 1 , \dots , \operatorname* { m a x } _ { i } f _ { i } ( A )$ ，sort all the rows by increasing $\ell _ { i } ( A )$

If Algorithm 5.2.1 is applied to $A$ in (5.2.2),the good row ordering $P A$ is obtained. The algorithm will not in general determine a unique ordering. One way to resolve ties is to consider the cost of symbolically rotating a row $a _ { i } ^ { T }$ into all other rows with a nonzero element in column $\ell _ { i } ( A )$ . By cost we mean the total number of new nonzero elements created. The rows are then ordered according to ascending cost.With this ordering it follows that rows $1 , \ldots , f _ { i } ( A ) - 1$ in $R _ { i - 1 }$ will not be afected when the remaining rows are processed. Therefore these rows are the final first $f _ { i } ( A ) - 1$ rows in $R$

An alternative that has been found to_work well in some contexts is to order the rows by increasing values of $\ell _ { i } ( A )$ . When row $a _ { i } ^ { T }$ is processed using this ordering,all previous rows processed have nonzeros only in columns up to at most $\ell _ { i } ( A )$ . Hence,only columns $f _ { i } ( A )$ to $\ell _ { i } ( A )$ of $R _ { i - 1 }$ will be involved, and $R _ { i - 1 }$ has zeros in columns $\ell _ { i + 1 } ( A ) , \ldots , n$ No fill will be generated in row $a _ { i } ^ { T }$ in these columns.

Liu [754,1986] introduced the notion of row merge tree for structuring this operation. Let $R _ { 0 }$ be initialized to have the structure of the final $R$ with all elements equal to zero.Denote by $R _ { k - 1 } \in \mathbb { R } ^ { n \times n }$ the upper triangular matrix obtained after processing the first $k - 1$ rows. At step $k$ the $k$ th row of $A$ is first uncompressed into a full vector $a _ { k } ^ { T } = ( a _ { k 1 } , a _ { k 2 } , \ldots , a _ { k n } )$ The nonzero elements $a _ { k j } \neq 0$ are annihilated from left to right by plane rotations involving rows $j < k$ in $R _ { k - 1 }$ . This may create new nonzeros in both $R _ { k - 1 }$ and in the current row $a _ { k } ^ { T }$ Note that if $r _ { j j } = 0$ in $R _ { k - 1 }$ ,this means that this row in $R _ { k - 1 }$ has not yet been touched by any rotation,and hence the entire $j$ th row must be zero.When this occurs the remaining part of row $k$ can just be inserted as the $j$ th row in $R _ { k - 1 }$ . The algorithm is illustrated below using an example from George and $\mathrm { N g } \ [ 4 6 0 , 1 9 8 3 ]$

Assume that the first $k$ rows of $A$ have been processed to generate $R _ { k }$ . Nonzero elements of $R _ { k - 1 }$ are denoted by $\times$ ， nonzeros introduced into $R _ { k }$ and $a _ { k } ^ { T }$ during the elimination $a _ { k } ^ { T }$ are denoted by $^ +$ ，and elements involved in the elimination of $a _ { k } ^ { T }$ are circled. Nonzero elements created in $a _ { k } ^ { T }$ during the elimination are ultimately annihilated. The sequence of row indices involved in the elimination is $\{ 2 , 4 , 5 , 7 , 8 \}$ ,where 2 is the column index of the first nonzero in $a _ { k } ^ { T }$ Note that unlike in the Householder method,intermediate fill only takes place in the row being processed:

$$
\left[ \begin{array} { c c c c c c c c c c } { R _ { k - 1 } } \\ { a } \\ { \mathbf { \Gamma } } \\ { \otimes } & { 0 } & { \otimes } & { \oplus } & { \otimes } & { 0 } & { 0 } & { 0 } & { 0 } \\ & { \otimes } & { 0 } & { \oplus } & { \otimes } & { 0 } & { 0 } & { 0 } & { 0 } \\ & { \times } & { 0 } & { \times } & { 0 } & { 0 } & { 0 } & { \times } & { 0 } \\ & & { \otimes } & { \oplus } & { 0 } & { \otimes } & { 0 } & { 0 } & { 0 } \\ & & & { \otimes } & { \oplus } & { 0 } & { 0 } & { 0 } & { 0 } \\ & & & & & { \otimes } & { \otimes } & { 0 } & { 0 } \\ & & & & & & & { \times } & { \times } \\ { 0 } & { \otimes } & { 0 } & { \otimes } & { \oplus } & { 0 } & { \oplus } & { 0 } & { 0 } \end{array} \right] .
$$

From Theorem 5.2.3 it follows that if the structure of $R$ has been predicted from that of $A ^ { T } A$ , any intermediate matrix $R _ { i - 1 }$ willft into the predicted structure. The plane rotations can be applied simultaneously to a right-hand side $b$ to form $Q ^ { T } b$ 、In the original implementation the Givens rotations are discarded after use.Hence,only enough storage to hold the final $R$ and a few extra vectors for the current row and right-hand side(s) is needed in main memory.

Gilbert et al. [468, 2oo1] give an algorithm to predict the structure of $R$ working directly from $G ( A )$ . This algorithm runs in time proportional to $\mathtt { n n z } ( A )$ and makes the step of determining the structure of $A ^ { T } A$ redundant.

Variable row pivoting methods are studied by Gentleman [450,1973], Duff [340,1974l,and Zlatev [1151,1982]. These schemes have never become very popular because they require a dynamic storage structure and are complicated to implement.

# 5.2.3 - Multifrontal methods

The multifrontal method, introduced by Duff and Reid [352,1983l, is a method for solving a linear system $A x = b$ that organizes the factorization of a sparse matrix into a sequence of partial factorizations of smaller independent dense subproblems that can be solved in parallel. This gives good data locality and lower communication costs. The following theorem, which is the basis for the multifrontal method, is due to Duff [343,1986].

Theorem 5.2.4. Let $T [ j ]$ denote the subtree rooted in node $j$ Then if $k \notin T [ j ]$ ,columns $k$ and $j$ can be eliminated independently of each other.

If $T [ i ]$ and $T [ j ]$ are two disjoint subtrees of $T ( C )$ , columns $s \in T [ i ]$ and $t \in T [ j ]$ can be eliminated in any order. The elimination tree prescribes an order relation for the elimination of columns in the QR factorization,i.e., a column associated with a child node must be eliminated before the parent column. On the other hand,columns associated with different subtrees of $T ( C )$ are independent and can be eliminated in parallel.

Liu [754,1986] developed a multifrontal QR algorithm that generalizes the row-oriented Givens QR algorithm by using submatrix rotations. It achieves a significant reduction in time at the cost of a modest increase in working storage. A modified version of this algorithm that uses Householder reflections is given by George and Liu [458,1987]. Supervertices and other essential modifications of multifrontal methods are treated by Liu [755,1990].

Nested dissection orderings have been discussed in Section 4.3.2. Such orderings for solving general sparse positive definite systems have been analyzed by George, Poole, and Voigt [462, 1978] and George and Liu [457,1g81]. The use of such orderings for sparse least squares problems is treated in George,Heath,and Plemmons $[ 4 6 4 , \ 1 9 8 1 ]$ and George and $\mathrm { N g }$ [460, $\mathrm { 1 9 8 3 } ]$ . A planar graph is a graph that can be drawn in the plane without two edges crossing. Planar graphs are known to have small balanced separators. Lipton, Rose,and Tarjan [753,1979] show that for any planar graph with $n$ vertices there exists a separator with $O ( \sqrt { n } )$ vertices such that each subgraph has at most $n / 2$ vertices.

We illustrate the multifrontal QR factorization by the small $1 2 \times 9$ matrix

$$
\scriptstyle A = { \left( \begin{array} { l l l l l l } { \times } & & { \times } & & { \times } & { \times } \\ { \times } & & { \times } & & { \times } & { \times } \\ { \times } & & & { \times } & & { \times } & \\ & { \times } & & & { \times } & & { \times } \\ & { \times } & & & { \times } & & { \times } \\ & & { \times } & & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \\ & { \times } & & & { \times } & { \times } & \\ & & { \times } & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \\ & & & & { \times } & & { \times } \\ & & { \times } & & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \end{array} \right) } .
$$

This matrix arises from a $3 \times 3$ mesh problem using a nested dissection ordering. The graph $G ( A ^ { T } A )$ is

![](images/4b85d8991798130c2cb4aaecc6a540edd07d04ab0ba79386c5e68ffab686ea1a.jpg)

First, a QR factorization of rows 1-3 is performed. These rows have nonzeros only in columns $\{ 1 , 5 , 7 , 8 \}$ . With the zero columns omitted, this operation can be carried out as a QR factorization of a small dense matrix of size $3 \times 4$ ，The resulting first row equals the first of the final $R$ of the complete matrix and can be stored away. The remaining two rows form an update matrix $F _ { 1 }$ and will be processed later. The other three block rows 4-6,7-9,and 1O-12 can be reduced similarly in parallel. After this first stage the matrix has the form

$$
\begin{array} { r } { \left( \begin{array} { l l l l l l } { \times } & { } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { \times } \\ { } & { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { } & { \times } & { } & { \times } & { } \end{array} \right) . } \end{array}
$$

In the second stage, $F _ { 1 } , F _ { 2 }$ and $F _ { 3 } , F _ { 4 }$ are simultaneously merged into two upper trapezoidal matrices by eliminating columns 5 and 6. In merging $F _ { 1 }$ and $F _ { 2 }$ , only the set of columns $\{ 5 , 7 , 8 , 9 \}$ needs to be considered. Reordering the rows by the index of the first nonzero element and performing a QR decomposition, we get

$$
\begin{array} { r } { Q ^ { T } \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & \\ { \times } & & { \times } & { \times } \\ & { \times } & { \times } & \\ & & { \times } & { \times } \end{array} \right) = \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & & { \times } & { \times } \\ & & & { \times } \end{array} \right) . } \end{array}
$$

The first row in each of the four blocks is a final row in $R$ and can be removed, which leaves four upper trapezoidal update matrices, $F _ { 1 } { - } F _ { 4 }$ . The merging of $F _ { 3 }$ and $F _ { 4 }$ is performed similarly. The first row in each reduced matrix is a final row in $R$ and is removed.In the final stage the remaining two upper trapezoidal (in this example, triangular) matrices are merged, giving the final factor $R$ .This corresponds to eliminating columns 7,8,and 9.

In the multifrontal method the vertices in the elimination tree are visited in turn given by the ordering.Each node $x _ { j }$ in the tree is associated with a frontal matrix $F _ { j }$ that consists of the set of rows $A _ { j }$ in $A$ ,with the first nonzero in location $j$ ,together with one update matrix contributed by each child node of $x _ { j }$ . After variable $j$ in the frontal matrix is eliminated,the first row in the reduced matrix is the $j$ th row of the upper triangular factor $R$ .The remaining rows form a new update matrix $U _ { j }$ that is stored in a stack until needed.

For $j = 1 , \dotsc , n$ do

1. Form the frontal matrix $F _ { j }$ by combining the set of rows $A _ { j }$ and the update matrix $U _ { s }$ for each child $x _ { s }$ of the node $x _ { j }$ in the elimination tree $T ( A ^ { T } A )$ .

2.By an orthogonal transformation, eliminate variable $x _ { j }$ in $F _ { j }$ to get $\bar { U } _ { j }$ .Remove the first row in $\bar { U } _ { j }$ ,which is the $j$ th row in the final matrix $R$ . The rest of the matrix is the update matrix $U _ { j }$

The frontal matrices in the multifrontal method are often too small for the efficient use of vector processors and matrix-vector operations in the solution of the subproblems. Therefore, a useful modification of the multifrontal method is to amalgamate several vertices into one large supernode. Instead of eliminating one column in each node,the decomposition of the frontal matrices then involves the elimination of several columns,and it may be possible to use Level 2 or even Level 3 BLAS; see Dongarra et al. [328,199o]. Vertices can be grouped together to form a supernode if they correspond to a block of contiguous columns in the Cholesky factor, where the diagonal block is fully triangular,and these rows all have identical off-block diagonal column structures. Because of the computational advantages of having large supervertices, it is advantageous to relax this condition and also amalgamate vertices that satisfy this condition if some local zeros are treated as nonzeros. A practical restriction is that if too many vertices are amalgamated, then the frontal matrices become sparse. Note also that nonnumerical operations often make up a large part of the total decomposition time,which limits the possible gain. For a discussion of supervertices and other modifications of the multifrontal method, see Liu [755,1990].

For a $K$ by $K$ grid problem with $n = K ^ { 2 }$ ， $m = s ( K - 1 ) ^ { 2 }$ it is known that $\mathtt { n n z } ( R ) =$ $O ( n \log n )$ ,but $Q$ has $O ( n { \sqrt { n } } )$ nonzeros; see George and $\mathrm { N g }$ [461, 1988]. Hence if $Q$ is needed, it should not be stored explicitly but represented by the Householder vectors of the frontal orthogonal transformations.Lu and Barlow [761,1996] show that these require only $O ( n \log n )$ storage. In many implementations the orthogonal transformations are not stored. Then the corrected seminormal equations (see Section 2.5.4) can be used to treat additional right-hand sides.

# 5.2.4 - Software for Sparse Least Squares Problems

Early software, such as YSMP by Eisenstat et al.[362,1982] and SPARSPAK by George and $\mathrm { N g } [ 4 6 3 , 1 9 8 4 ]$ ,focused on the Cholesky algorithm.A Fortran subroutine LLSSO1 that performs sparse QR factorization by fast Givens rotations was developed by Zlatev and Nielsen [1152, 1979]. The orthogonal matrix $Q$ is not stored,and elements in $R$ smaller than a user-specified tolerance are dropped. Other early QR factorization codes were developed by Lewis,Pierce, and Wah[739,1989],Matstoms [784,1992],and Puglisi [907,1993]. Matstoms [785,1994] develops multifrontal concepts for QR factorization such as the use of supernode elimination tree and node amalgamation for increasing the effciency. Sun [1O46,1996] gives a parallel multifrontal algorithm for sparse QR factorization suitable for distributed-memory multiprocessors.A multifrontal sparse rank-revealing QR factorization/least squares solution module by Pierce and Lewis [894,1997l is included in the commercial software package BCSLIB-EXT from Boeing Information and Support Services. This library is also available to researchers in laboratories and academia for testing.

The SuiteSparse collection by Davis [290,2o11] includes a “state-of-the-art” sparse Cholesky factorization and a multithreaded multifrontal sparse QR algorithm and is available at www. netlib .org. The Ceres nonlinear least squares solver for three-dimensional imagery in Google Earth relies on the sparse Cholesky factorization in SuiteSparse.The multithreaded multifrontal sparse QR factorization QR MUMPS by Buttari [195,2o13] builds on earlier implementations of Puglisi and Matstoms; see Amestoy, Duff,and Puglisi [19,1996].

The design of sparse matrix storage and computations for MATLAB is described by Gilbert, Moler,and Schreiber [469,1992]. A matrix is stored as either full or sparse. Conversion between full and sparse storage modes is done by the inbuilt functions spar se and full. A sparse matrix is stored in CSC format as the concatenation of the sparse vectors representing its columns. This makes it efcient to scan the columns of a sparse matrix but very inefficient to scan its rows. To facilitate a basic sparse operation, a sparse accumulator (SPA) that allows random access to the currently active column or row of a matrix is used. The SPA consists of a dense vector of real (or complex) values,a dense vector of true/false “occupied flags,” and an unordered list of the indices whose occupied flags are true. Almost all sparse operations are performed as operations between the SPA and a sparse vector. This allows many vector operations to be carried out in time proportional to the number of nonzero element in the vector. Factorizations such as LU, Cholesky,and QR of a sparse matrix yield sparse results but, otherwise,behave as the corresponding dense MATLAB operations.

Several column reorderings of the column are available in MATLAB for making the Cholesky and QR factors more sparse. MATLAB stores a permutation as a vector p containing a permutation of $1 , 2 , \ldots , n$ such that $\mathbb { A } \left( : , \thinspace \mathfrak { p } \right)$ is the matrix with permuted columns.The function $\mathtt { p } \ = \ \mathtt { c o l p e r m } ( \mathtt { A } )$ computes a permutation that sorts the columns so that they have increas-ing nonzero count. An approximate minimum degree ordering for the columns is given by $\mathtt { p } \ = \ \mathtt { c o l m m d } ( \mathtt { A }$ .

To solve a sparse least squares problem using a minimum degree ordering of the columns of $A$ and the corrected seminormal equations (CSNE; see Section 2.5.4), one writes the following in MATLAB.

# Algorithm 5.2.2 (Sparse Least Squares Solution by CSNE).

$$
{ \begin{array} { l l l } { \arcsin { \mathrm { ~ ( x , r ) ~ } } = { \mathrm { ~ s p a r s e l s e d s e q ( A , b ) ~ } } ; } \\ { { \begin{array} { l l l l } { \gamma _ { \mu } } & { \operatorname { - --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- } \\ { \mathrm { ~ q _ { \mu } ~ } } = { \mathrm { ~ c o l m m d ~ ( A ) ~ } } ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { M i n i m i m u ~ d e g r e e ~ o r d e r i n g ~ o f ~ A ~ } } } \\ { \mathrm { ~ A } } & { \mathrm { ~ A } ( : , \mathrm { q } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { R e o r d e r ~ c o l u m s ~ o f ~ A e c o m p o s i t i o n } } } \\ { \mathrm { ~ R } } & { = { \mathrm { ~ c h o l ~ } } ( \mathrm { A } ^ { \prime } * \mathrm { k } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { S p a r s e ~ c h o ~ c h o l e s k y ~ d e c o m p o s i t i o n } } } \\ { \mathrm { ~ x } } & { \mathrm { ~ R } } & { \mathrm { ( ~ A } ^ { \prime } * \mathrm { b } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { L e a s t ~ } } \mathrm { ~ s q u a r e s ~ s o l u t i o n } } \\ { \mathrm { ~ x } } & { \mathrm { ~ + ~ \mathrm { ~ R } ~ } \mathrm { { ~ ( ~ A } ^ { \prime } * ( \mathrm { b } ~ - ~ \mathrm { ~ A } * \mathrm { x } ) ) } } & { \quad \forall _ { \mu } } & { { \mathrm { C o r r e c t i o n ~ s t e p } } } \\ { \mathrm { ~ x } } & { \mathrm { ~ ( q ) } } & { = \mathrm { ~ x } ; } & { } & { \gamma _ { \mathrm { { o } } } { \mathrm { ~ P e r m u t e ~ s o l u t i o n } } } \end{array} } } \\ { { \mathrm { ~ x } } } \end{array} }
$$

SuiteSparseQR is also available in MATLAB. This allows large-scale sparse least squares problems to be solved. The function $[ \mathbb { Q } , \mathbb { R } , \mathbb { p } ] \ = \ \mathsf { q r } \left( \mathbb { A } , \mathbf { \ell } ^ { \prime } \mathsf { v e c t o r } ^ { \prime } \right)$ returns the $m \times n$ factor $\mathtt { R }$ and $m \times m$ factor $\mathsf { Q }$ such that $\mathsf { A } \left( : , \mathsf { p } \right) \ = \ \mathsf { q } * \mathsf { R } .$ Because $\mathsf { Q }$ often is not very sparse,a better choice is to solve one or more least squares problems m $\mathrm { i n } \| A X - B \|$ using $[ { \mathsf C } , { \mathsf R } , { \mathsf p } ] \ = \ { \mathsf { q r } } ( { \mathsf { A } } , { \mathsf { B } } , 0 )$ and $\mathbb { X } \left( \mathbb { p } , : \right) \ = \ \mathbb { R } \backslash \mathbb { C }$

Example 5.2.5. We study the effect of two different column orderings in the QR factorization of a sparse matrix $A$ arising in a study of substance transport in rivers by Elfving and Skoglund [384, 2007]. Figures 5.2.1 and 5.2.2 show the location of nonzero elements in $A P$ and $R$ using two different column orderings available in MATLAB.With colperm the columns are ordered by increasing nonzero elements and give $\mathrm { n n z } ( R ) = 3 2 { , } 3 5 5$ .The colamd ordering gives $\mathtt { n n z } ( R ) =$ 15,903,a great improvement. □

# 5.2.5 - Rank-Revealing Sparse QR Factorization

For dense matrices $A$ ,rank-deficient problems are handled by column pivoting in the QR factorization of $A$ ； see Section 2.3.2. In sparse QR factorization the initial column ordering is chosen to produce a sparse $R$ -factor in advance of any numerical computation. If the columns are reordered, the updated $R$ will in general not fit into the previously generated storage structure.

If the row sequential QR algorithm is applied in exact arithmetic to a matrix $A$ of rank $r < n$ ， a row is inserted into $R$ only when it makes the diagonal entry nonzero. Hence the resulting $R \mathrm { . }$ - factor must have $n - r$ zero diagonal elements. Processing additional rows can only increase the absolute value of the diagonal elements. Hence if the final $R$ has a zero diagonal element, all elements in this row are zero,and the final $R$ will have the form depicted in Figure 5.2.3. By permuting the zero rows of $R$ to the bottom,and the columns of $R$ corresponding to the zero diagonal elements to the right, we obtain $R$ in rank-revealing form.

![](images/cde83a6231e8dfa601b66784832f0d627326a8cc7c7f738f0318e07241bb0c35.jpg)  
Figure 5.2.1. Nonzero pattern of a sparse matrix $A$ and the factor $R$ in its QR factorization using the MATLAB colperm reordering. Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations, Bjorck, $\mathring { A } k e$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

![](images/6f31bf357e0ff249396b349f7f2527ceca94cc0617ba0d5bd341aa9ebf9b3250.jpg)  
Figure 5.2.2. Nonzero pattern of a sparse matrix $A$ and the factor $R$ in its QR factorization using the MATLAB colamd column ordering. Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e ,$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

![](images/15048f066a8f6ab72982ea9ea23ed3e1dc01f856eb2ce9e7dbe4d3e457e223ec.jpg)  
Figure 5.2.3. Structure of upper triangular matrix R for a rank-deficient matrix.

In finite-precision, the computed $R$ usually will not have any zero diagonal element, even when $\operatorname { r a n k } ( A ) \ < \ n$ .Although the rank is often revealed by the presence of small diagonal elements, this does not imply that the rest of the rows are negligible. Heath [596,1982] suggests the following postprocessing of $R$ Starting from the top, the diagonal of $R$ is examined for small elements. In each row whose diagonal element fals below a certain tolerance, the diagonal element is set to zero. The rest of the row is then reprocessed,zeroing out all its other nonzero elements. This might increase some previously small diagonal elements in rows below, which is why one has to start from the top. We again end up with a matrix of the form shown in Figure 5.2.3.However, it may be that $R$ is numerically rank-deficient yet has no small diagonal element.

Pierce and Lewis [894,1997] develop a rank-revealing algorithm for sparse QR factorizations based on techniques similar to those in Section 2.3.5. The factorization proceeds by columns, and inverse iteration is used to determine ill-conditioning. Let $R _ { j } = ( r _ { 1 } , \ldots , r _ { j } )$ be the matrix formed by the first $j$ columns of the final $R$ 、Assume that $R _ { j }$ is not too ill-conditioned,but $R _ { j + 1 } = { \left( \begin{array} { l l } { R _ { j } } & { r _ { j + 1 } } \end{array} \right) }$ is found to be almost rank-deficient. Then column $r _ { j + 1 }$ is permuted to the last position,and the algorithm is continued. This may happen several times during the numerical factorization.At the end we obtain a QR factorization

$$
\left( A _ { 1 } \quad A _ { 2 } \right) = Q \left( { R _ { 1 1 } } \quad R _ { 1 2 } \atop 0 \quad S \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is well-conditioned. In general $R _ { 1 2 }$ and $S$ will be dense,but provided $r \ll n$ ， this is often acceptable.An important fact stated in the theorem below is that $R _ { 1 1 }$ will always fit into the storage structure predicted for $R$ .The following theorem is implicit in Foster [424, 1986].

Theorem 5.2.6. Let $A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ , and let

$$
A _ { { \mathcal { F } } _ { k } } = [ a _ { j _ { 1 } } , a _ { j _ { 2 } } , \dotsc , a _ { j _ { r } } ] , \qquad 1 \leq j _ { 1 } < j _ { 2 } < \dotsc < j _ { r } \leq n
$$

be a submatrix of $A$ Denote the Cholesky factors of $A ^ { T } A$ and $A _ { \mathcal { F } _ { k } } ^ { T } A _ { \mathcal { F } _ { k } }$ by $R$ and $R _ { \mathcal { F } _ { k } }$ ,respectively. Then the nonzero structure of $R _ { \mathcal { F } _ { k } }$ is included in the nonzero structure predicted for $R$ under the no-cancellation assumption.

Proof. Let $G = G ( \boldsymbol { X } , E )$ be the ordered graph of $A ^ { T } A$ . The ordered graph $G _ { \mathcal { F } _ { k } } = G _ { \mathcal { F } _ { k } } ( X _ { \mathcal { F } _ { k } }$ $E _ { \mathcal { F } _ { k } } )$ of $A _ { \mathcal { F } _ { k } } ^ { T } A _ { \mathcal { F } _ { k } }$ is obtained by deleting all vertices in $G$ not in $\mathcal { F } _ { k } = [ j _ { 1 } , j _ { 2 } , \dotsc , j _ { r } ]$ and all edges leading to the deleted vertices. Then $( R \mathcal { F } ) _ { i j } \neq 0$ only if there exists a path in $G _ { \mathcal { F } _ { k } }$ from node $i$ to node $j$ $( i < j )$ through vertices with numbers less than $i$ . If such a path exists in $G _ { \mathcal { F } _ { k } }$ ， it must exist also in $G$ ,and hence we will have predicted $R _ { i j } \neq 0$ □

# 5.3 - Special Topics

# 5.3.1 - Mixed Sparse-Dense Least Squares Problems

In some applications,least squares problems arise in which $A \in \mathbb { R } ^ { m \times n }$ is sparse, except for a small number of dense rows representing additional coupling terms. If the dense rows are ordered last,such problems have the form

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } = \operatorname* { m i n } _ { x } \left\| \left( A _ { d } \right) x - \left( { b } _ { s } \right) \right\| _ { 2 } ,
$$

where $A _ { s } \in \mathbb { R } ^ { m _ { s } \times n }$ is sparse, $A _ { d } \in \mathbb { R } ^ { m _ { d } \times n }$ is dense, and $m = m _ { s } + m _ { d }$ with $m _ { d } \ll n$ .Then $A ^ { T } A = A _ { s } ^ { T } A _ { s } + A _ { d } ^ { T } A _ { d }$ , and its Cholesky factor willbe dense. For large-scale mixed sparse-dense least squares problems, standard sparse Cholesky and QR methods are not practical because of their high memory and computing demands. We remark that finding a good partitioning between sparse and dense equations can be a nontrivial problem.

We now describe an updating method by Heath [596,1982] in which dense rows are first withheld from the QR factorization. The solution (not the factorization) to the sparse subproblem is then updated to incorporate the dense rows.Let the QR factorization of the sparse subproblem be

$$
\begin{array} { r } { \left( \begin{array} { c c } { A _ { s } } & { b _ { s } } \end{array} \right) = Q _ { s } \left( \begin{array} { c c } { R _ { s } } & { c _ { s } } \\ { 0 } & { d _ { s } } \end{array} \right) , } \end{array}
$$

where $Q _ { s }$ need not be formed or saved. If $\operatorname { r a n k } ( A _ { s } ) = n$ ，then $R _ { s }$ is nonsingular, and the solution $y$ to the sparse subproblem can be obtained from $R _ { s } y = c _ { s }$ . Setting $x = y + z$ and noting that $c _ { s } - R _ { s } y = 0$ , we can write the residuals to the sparse subproblem as

$$
r _ { s } = b _ { s } - A _ { s } ( y + z ) = Q _ { s } \left( \begin{array} { c } { - R _ { s } z } \\ { d _ { s } } \end{array} \right) .
$$

It follows that $z$ solves

$$
\operatorname* { m i n } _ { z } \left\| \left( \begin{array} { l } { R _ { s } } \\ { A _ { d } } \end{array} \right) z - \left( \begin{array} { l } { 0 } \\ { r _ { d } } \end{array} \right) \right\| _ { 2 } , \quad r _ { d } = b _ { d } - A _ { d } y .
$$

By the change of variables

$$
u = R _ { s } z , \quad v = r _ { d } - C _ { d } u , \quad C _ { d } = A _ { d } R _ { s } ^ { - 1 } \in \mathbb { R } ^ { m _ { d } \times n } ,
$$

this problem is seen to be that of finding the least-norm solution to the linear system

$$
\begin{array} { r l } { ( I _ { m _ { d } } } & { { } C _ { d } ) \left( \begin{array} { l } { v } \\ { u } \end{array} \right) = r _ { d } . } \end{array}
$$

This problem is the same as the small least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { v } } \left\| \left( \begin{array} { c } { I _ { m _ { d } } } \\ { C _ { d } ^ { T } } \end{array} \right) \boldsymbol { v } - \left( \begin{array} { c } { r _ { d } } \\ { 0 } \end{array} \right) \right\| _ { 2 } , \quad \boldsymbol { u } = C _ { d } ^ { T } \boldsymbol { v } ,
$$

which can be solved by QR factorization of the $( m _ { d } + n ) \times m _ { d }$ matrix.Note that for both problems the normal equations for $v$ are

$$
( C _ { d } C _ { d } ^ { T } + I _ { m _ { d } } ) v = r _ { d } .
$$

Finally, the solution $x$ to problem (5.3.1) is $x = y + z$ ，where $z$ is found by solving $R _ { s } z = u$ The algorithm is summarized below.

# Algorithm 5.3.1 (Solving a Sparse-Dense Lease Squares Problem by Updating).

1. Compue spaseQRfatriaton $\begin{array} { r } { ( \ A _ { s } \quad b _ { s } ) = Q _ { s } \left( \begin{array} { c c } { R _ { s } } & { c _ { s } } \\ { 0 } & { d _ { s } } \end{array} \right) . } \end{array}$

2. Solve $R _ { s } y = c _ { s }$ for y and form residual $r _ { d } = b _ { d } - A _ { d } y$

3. Compute $C _ { d } \in \mathbb { R } ^ { m _ { d } \times n }$ from $R _ { s } ^ { T } C _ { d } ^ { T } = A _ { d } ^ { T }$

4. Solve thefulranklastsaresproblm(.)for $v$ and form $u = C _ { d } ^ { T } v$

5. Form the solution $x = y + z$ ,where $R _ { s } z = u$

A fundamental diffculty arises with this updating method if $A _ { s }$ is ill-conditioned or singular. f $\operatorname { r a n k } ( A _ { s } ) < n$ ,then $R _ { s }$ is singular, and the algorithm breaks down. If $\sigma _ { \operatorname* { m i n } } ( A _ { s } ) \ll \sigma _ { \operatorname* { m i n } } ( A )$ ， then Algorithm 5.3.1 is not stable.

It is not unusual in practice for $A _ { s }$ to have $n _ { 2 } \ll n$ null columns. If the null columns are permuted to the last positions and $x$ is partitioned conformally, the problem becomes

$$
A = \left( A _ { 1 } \quad A _ { 2 } \right) = \left( \begin{array} { c c } { { A _ { s _ { 1 } } } } & { { 0 } } \\ { { A _ { d _ { 1 } } } } & { { A _ { d _ { 2 } } } } \end{array} \right) , \quad x = \left( \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \end{array} \right) ,
$$

where $A _ { 1 }$ has full column rank, $x _ { 1 } \in \mathbb { R } ^ { n _ { 1 } }$ and $x _ { 2 } ~ \in ~ \mathbb { R } ^ { n _ { 2 } }$ ，and $n = n _ { 1 } + n _ { 2 }$ . The previous updating scheme is generalized to this case by Heath [596,1982]. Let $z \in \mathbb { R } ^ { n _ { 1 } }$ and $W \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } }$ be the solutions of the least squares problems

$$
\operatorname* { m i n } _ { z } \| A _ { 1 } z - b \| _ { 2 } , \qquad \operatorname* { m i n } _ { z } \| A _ { 1 } W - A _ { 2 } \| _ { 2 } ,
$$

respectively. In both least squares problems (5.3.7), $A _ { 1 }$ has full rank and $m _ { d }$ has dense rows and, thus problems (5.3.7) can be solved by the previous algorithm. Then $x _ { 2 }$ is obtained as the solution of the small dense least squares problem

$$
\operatorname* { m i n } _ { x _ { 2 } } \| ( A _ { 2 } - A _ { 1 } W ) x _ { 2 } - ( b - A _ { 1 } z ) \| _ { 2 }
$$

of size $m \times n _ { 2 }$ ,and $x _ { 1 } = z - W x _ { 2 }$ ; see Lemma 4.3.1.

Another approach for treating mixed sparse-dense least squares problems is matrix stretch-ing; see Grcar [530,199o] and Adlers and Bjorck [8,2ooo].In this approach,dense rows are replaced by several much sparser rows connected by additional linking variables. The strength and limitations of this approach are studied by Scott and Tüma [990, 2o1g9]. They propose a new stretching strategy that better limits the fillin the normal matrix and its Cholesky factorization.

Avron, $\mathrm { N g }$ ,and Toledo [45,2oo9] propose using an iterative method, such as LSQR, preconditioned by $R _ { s }$ from the sparse QR factorization of $A _ { s }$ . This requires $A _ { s }$ to have full column rank and be not too ill-conditioned. A Schur complement approach to preconditioning mixed sparse-dense problems is studied by Scott and Tuma [989,2o18]. In image reconstruction and certain other inverse problems, $A$ may be fairly sparse in all rows and columns, but $A ^ { T } A$ may be practically dense. Such problems are usually solved by preconditioned iterative methods; see Scott and Tuma [988, 2017].

# 5.3.2 - Canonical Block Triangular Form

Sometimes it can be helpful to permute $A$ into the canonical block upper triangular form discovered by Dulmageand Mendelsohn [353,1958], [354,1959],[355,1963l,and Johnson,Dulmage,

and Mendelsohn [675,1963]:

$$
P A Q = \left( \begin{array} { c c c } { { A _ { h } } } & { { U _ { h s } } } & { { U _ { h v } } } \\ { { } } & { { A _ { s } } } & { { U _ { s v } } } \\ { { } } & { { } } & { { A _ { v } } } \end{array} \right) .
$$

Here the block $A _ { h }$ is underdetermined (has more columns than rows), $A _ { s }$ is square, and $A _ { v }$ is overdetermined (has more rows than columns). All three blocks have a nonzero diagonal, and the submatrices $A _ { v }$ and $A _ { h } ^ { T }$ both have the strong Hall property. One or two of the diagonal blocks may be absent in the decomposition. The example below shows the coarse block triangular decomposition of a matrix $A \in \mathbb { R } ^ { 1 1 \times 1 0 }$ with structural rank 8.

<table><tr><td>×</td><td>8 ×</td><td>× 8</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td></td><td></td><td>? ×</td><td>× 8</td><td></td><td>×</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td>8 ×</td><td>× 8</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>8</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>×</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>×</td></tr></table>

It may be possible to further decompose the blocks $A _ { h }$ and $A _ { v }$ in the coarse decomposition (5.3.9) so that

$$
A _ { h } = \left( \begin{array} { c c c } { { A _ { h 1 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { A _ { h p } } } \end{array} \right) , \qquad A _ { v } = \left( \begin{array} { c c c } { { A _ { v 1 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { A _ { v q } } } \end{array} \right) ,
$$

where each $A _ { h 1 } , \ldots , A _ { h p }$ is underdetermined and each $A _ { v 1 } , \ldots , A _ { v q }$ is overdetermined. The submatrix $A _ { s }$ may be decomposable into block upper triangular form

$$
A _ { s } = \left( \begin{array} { c c c c } { A _ { s 1 } } & { U _ { 1 2 } } & { . . . } & { U _ { 1 , t } } \\ & { A _ { s 2 } } & { . . . } & { U _ { 2 , t } } \\ & & { \cdot . } & { \vdots } \\ & & & { A _ { s t } } \end{array} \right)
$$

with square diagonal blocks $A _ { s 1 } , \ldots , A _ { s t }$ that have nonzero diagonal elements. The resulting fine decomposition can be shown to be essentially unique. Any block triangular form can be obtained from any other by applying row permutations that involve the rows of a single block row, column permutations that involve the columns of a single block column, and symmetric permutations that reorder the blocks.

A square matrix that can be permuted to the form (5.3.1O), with $t > 1$ ,is said to be reducible; otherwise, it is called irreducible; see Definition 4.1.3.All the diagonal blocks $A _ { s 1 } , \ldots , A _ { s t }$ in the fine decomposition are irreducible.This implies that they have the strong Hal property; see Coleman, Edenbrandt,and Gilbert [262,1g86]. A two-stage algorithm for permuting a square and structurally nonsingular matrix $A$ to block upper triangular is given by Tarjan [1O57,1972]; see also Gustavson [555,1976],and Duff [341,1977], [342,1981]. The algorithm depends on the concept of matching in the bipartite graph of $A$ . This is a subset of its edges with no common end points and corresponds to a subset of nonzeros in $A$ such that no two belong to the same row or column. A maximum matching is one where the maximum number of edges equals the structural rank $r ( A )$

Pothen and Fan [902,1990],[901, $\mathrm { 1 9 8 4 } ]$ give an algorithm for the general case. The program MC13D by Duff and Reid [351,1978] in the HSL Mathematical Software Library implements the fine decomposition of $A _ { s }$ . It proceeds in three steps:

1. Find a maximum matching in the bipartite graph $G ( A )$ with row set $\mathcal { R }$ and column set $\mathcal { C }$   
2.According to the matching, partition $\mathcal { R }$ into sets $\mathcal { V R } , \mathcal { S R } , \mathcal { H R }$ and $\mathcal { C }$ into sets $\nu \mathcal { C } , S \mathcal { C }$ ， HC corresponding to the vertical, square,and horizontal blocks.   
3.Find the diagonal blocks of the submatrices $A _ { v }$ and $A _ { h }$ from the connected components in the subgraphs $G ( A _ { v } )$ and $G ( A _ { h } )$ . Find the block upper triangular form of $A _ { s }$ from the strongly connected components in the associated directed subgraph $G ( A _ { s } )$ , with edges directed from columns to rows.

In MATLAB the algorithm is available through the function $\mathrm { [ p , q , r , s , c c , r r ] ~ = ~ d m p e r m \left( A \right) }$ The output consists of row and column permutation vectors $p$ and $q$ ，such that $A ( p , q )$ has Dulmage-Mendelsohn block triangular form． The vectors $r$ and $s$ are index vectors indicating the block boundaries for the fine decomposition,while the vectors $c c$ and $r r$ indicate the boundaries of the coarse decomposition.

The reordering to block triangular form in a preprocessing phase can save work and intermediate storage in solving least squares problems. If $A$ has structural rank $n$ ,the first block row in (5.3.9) must be empty,and the original least squares problem can,after a reordering,be solved by a form of block back-substitution. First,partition $\tilde { x } = Q ^ { T } x$ and $\tilde { b } = P b$ conformally with $P A Q$ in (5.3.9) and compute the solution $\tilde { x } _ { v }$ of

$$
\operatorname* { m i n } _ { \tilde { \boldsymbol { x } } _ { v } } \| \boldsymbol { A } _ { v } \tilde { \boldsymbol { x } } _ { v } - \tilde { \boldsymbol { b } } _ { v } \| _ { 2 } .
$$

Next, compute the remaining part of the solution $\tilde { x } _ { k } , \ldots , \tilde { x } _ { 1 }$ from

$$
A _ { s i } \tilde { x } _ { i } = \tilde { b } _ { i } - \sum _ { j = i + 1 } ^ { k } U _ { i j } \tilde { x } _ { j } , \quad i = k , \ldots , 2 , 1 .
$$

Finally, set $x = Q \tilde { x }$ .We can solve subproblems (5.3.11) and (5.3.12) by computing the QR factorizations of $A _ { v }$ and $A _ { s , i }$ ， $i = 1 , \ldots , k$ .As $A _ { s 1 } , \ldots , A _ { s k }$ and $A _ { v }$ have the strong Hall property, the structures of the matrices $R _ { i }$ are correctly predicted by the structures of the corresponding normal matrices.

If $A$ has structural rank $n$ but is numerically rank-deficient, it will not be possible to factorize all the diagonal blocks in (5.3.1O). In this case the block triangular structure given by the Dulmage-Mendelsohn form cannot be preserved,or some blocks may become severely ilconditioned. If the structural rank is less than $n$ ,there isan underdetermined block $A _ { h }$ .In this case we can still obtain the form (5.3.1O) with a square block $A _ { 1 1 }$ by permuting the extra columns in the first block to the end.The least squares solution is then not unique,but there is a unique solution of minimum length.

The block triangular form of the matrices in the Harwell-Boeing test collection (Duff, Grimes,and Lewis [346,1989l) and the time required to compute them are given in Pothen and Fan [902,1990].