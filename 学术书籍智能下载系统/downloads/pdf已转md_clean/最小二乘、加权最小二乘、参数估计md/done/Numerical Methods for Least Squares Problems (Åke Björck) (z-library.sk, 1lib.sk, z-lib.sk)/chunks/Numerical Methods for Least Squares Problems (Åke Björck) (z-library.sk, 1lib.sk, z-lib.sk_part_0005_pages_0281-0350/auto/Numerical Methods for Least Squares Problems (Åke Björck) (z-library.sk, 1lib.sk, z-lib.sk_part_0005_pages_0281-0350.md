# Chapter 6

# Iterative Methods

# 6.1 - Basic Iterative Methods

# 6.1.1 - Iterative versus Direct Methods

Direct methods for solving linear equations $A x = b$ and least squares problems $\operatorname* { m i n } { \| A x - b \| _ { 2 } }$ are reliable when they can be used. For huge problems,direct methods can be prohibitively expensive in terms of storage and operations.Then it becomes essential to use iterative solvers, in which an initial approximation is successively improved until an acceptable accuracy is achieved.

An important feature of iterative methods is that $A$ itself need not be stored; it suffices to be able to compute matrix-vector products $A v$ for arbitrary vectors $v$ ，Hence,iterative methods automatically speed up when $A$ is a sparse matrix or a fast linear operator. (Most iterative methods for least squares problems also need products $A ^ { T } u$ for arbitrary vectors $u$ ） The main weakness of iterative methods is their unpredictable robustness and range of applicability. Often, a particular iterative solver may be efcient for a specific class of problems,but for other cases it may be excessively slow or break down. The rate of convergence depends in a complex way on the spectrum of $A$ (or sometimes the singular values of $A$ )and can be prohibitively slow when $A$ is ill-conditioned. Usually, it is essential to use a preconditioner $M$ such that $A M ^ { - 1 }$ or $M ^ { - 1 } A$ is better conditioned and systems $M w = c$ can be solved efficiently with arbitrary vectors $c$

For least squares problems, any iterative method for solving symmetric positive definite sys-tems can be applied to the normal equations $A ^ { T } A x = A ^ { T } b$ However, explicit formation of $A ^ { T } A$ and $A ^ { T } b$ can and should be avoided by using the factored form

$$
\begin{array} { r } { A ^ { T } r = 0 , \quad r = b - A x . } \end{array}
$$

Working with $A$ and $A ^ { T }$ separately has important advantages. As emphasized earlier, small perturbations in $A ^ { T } A$ ,e.g., by roundoff, may_change the solution much more than perturbations of similar size in $A$ itself.Working with $A ^ { T } b$ instead of $b$ as input data can also cause a loss of accuracy. Fill that can occur in the formation of $A ^ { T } A$ is also avoided (although occasionally $A ^ { T } A$ is more sparse than $A$ ).

Iterative methods can also be applied to the least-norm problem

$$
\operatorname* { m i n } \| y \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A ^ { T } y = c .
$$

If $A$ has full row rank, the unique solution is $y = A z$ ，where $z$ satisfies the normal equations of the second kind (see (1.1.17)):

$$
A ^ { T } A z = c .
$$

Again, explicit formation of the cross-product matrix $A ^ { T } A$ should be avoided.

Example 6.1.1. A problem where $A$ is sparse but $A ^ { T } A$ is significantly more dense is shown in Figure 6.1.1. In such a case the Cholesky factor willin general also be nearly dense. This rules out the use of sparse direct methods based on QR decomposition of $A$ . Consider the case when $A$ has a random sparsity structure such that an element $a _ { i j }$ is nonzero with probability $p < 1$ Ignoring numerical cancellation, it follows that $( A ^ { T } A ) _ { j k } \neq 0$ with probability

$$
q = 1 - ( 1 - p ^ { 2 } ) ^ { m } \approx 1 - e ^ { - m p ^ { 2 } } .
$$

Therefore, $A ^ { T } A$ will be almost dense when $m p \approx m ^ { 1 / 2 }$ , i.e., when the average number of non-zero elements in a column is about $m ^ { 1 / 2 }$ . This type of structure is common in reconstruction problems.An example is the inversion problem for the velocity structure for the Central California Microearthquake Network. In 198O this generated a matrix $A$ with dimensions $m = 5 0 0 , 0 0 0$ ， $n = 2 0 { , } 0 0 0$ ,and about $1 0 ^ { 7 }$ nonzero elements.The nonzero structure of $A$ is very irregular and $A ^ { T } A$ is almost dense. Today similar problems of much higher dimensions are common.

![](images/b2158b529749e4364ad79fbf6c29140936b691ce592200eec91f7c5f05ad82f1.jpg)  
Figure 6.1.1. Structure of a sparse matrix $A$ (left) and $A ^ { T } A$ (right) fora simple image reconstruction problem. Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e ,$ 2015;permission conveyed through Copyright Clearance Center, Inc.

Another approach is to apply an iterative method to the augmented system

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { b } } \\ { { c } } \end{array} \right) .
$$

This system combines both kinds of normal equations. Taking $c = 0$ gives the least squares problem.Taking $b = 0$ gives the least-norm problem with $z = - x$ . The augmented system is symmetric and indefinite,which makes its solution more challenging. Recall that the condition of (6.1.4) can be improved by working with

$$
\left( \begin{array} { c c } { { \alpha I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { y / \alpha } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { c / \alpha } } \end{array} \right) ,
$$

where $\alpha \approx \sigma _ { \mathrm { m i n } } ( A )$ ; see Section 2.4.4.

# Notes and references

A good survey of iterative methods for solving linear systems is the comprehensive text by Saad [957, 2oo3]. The main research developments of the 2Oth century are surveyed by Saad and van der Vorst [960,2ooo]. Other notable textbooks on iterative methods include Axelsson [48, 1994], Greenbaum [534,1997l, and van der Vorst [1075,20o3]. Templates for implementation of iterative methods for linear systems are found in Barret et al.[82,1994]. A PDF file of an unpublished second edition of this book can be downloaded from http : //www .net lib .org/ temp lates/temp lates .pdf. Among older textbooks,we mention Varga [1090,1962] and Hageman and Young [559, 2004].

# 6.1.2 - Stationary Iterative Methods

The idea of solving systems of linear equations $A x = b$ by an iterative method dates at least as far back as Gauss (1823)． In the days of “hand’computations,rather unsophisticated relaxation methods were used. For a given approximation $x _ { k }$ , an equation $i$ with a residual of large magnitude is picked,and the corresponding component of $x _ { k }$ is adjusted so that this equation is satisfied.(This is always possible if $A$ is symmetric positive definite.） On computers, cyclic relaxation methods are more suitable,because the search for the largest residual is too time-consuming.

For a linear system $A x = b$ ， $A \in \mathbb { R } ^ { n \times n }$ , a stationary iterative method has the general form

$$
M x _ { k + 1 } = N x _ { k } + b , \quad k = 0 , 1 , \ldots ,
$$

where $x _ { 0 }$ is an initial approximation. Here $A = M - N$ is a splitting of $A$ ,with $M$ nonsingular. For the iteration to be practical, linear systems with $M$ should be easy to solve.To analyze the convergence, we rewrite (6.1.6) as

$$
x _ { k + 1 } = G x _ { k } + d , \quad G = M ^ { - 1 } N = I - M ^ { - 1 } A , \quad d = M ^ { - 1 } b ,
$$

where $G$ is the iteration matrix.

The iterative method (6.1.6) is said to be convergent if the sequence $\{ x _ { k } \}$ converges for all initial vectors $x _ { 0 }$ . If the method converges and $\scriptstyle \operatorname* { l i m } _ { k \to \infty } x _ { k } = x$ ,then $x$ satisfies $x = G x + d$ ， and $x$ satisfies $A x = b$ .Subtracting $x = G x + d$ from (6.1.7) gives

$$
x _ { k + 1 } - x = G ( x _ { k } - x ) = \cdots = G ^ { k + 1 } ( x _ { 0 } - x ) .
$$

It follows that the iteration method is convergent if and only if $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } G ^ { k } = 0 } \end{array}$

Theorem 6.1.2. The stationary iterative method $x _ { k + 1 } = G x _ { k } + d $ is convergent for all initial vectors $x _ { 0 }$ if and only if the spectral radius of $G$ satisfies

$$
\rho ( G ) = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } | \lambda _ { i } ( G ) | < 1 ,
$$

where $\lambda _ { i }$ are the eigenvalues of $G$

For any consistent matrix norm,we have $\rho ( G ) \ \leq \ \| G \|$ Thus a sufficient condition for convergence is that $\| G \| < 1$ holds for some consistent matrix norm.From (6.1.8) it follows that for any consistent matrix norm,

$$
\| x _ { k } - x \| \leq \| G ^ { k } \| \| x _ { 0 } - x \| \leq \| G \| ^ { k } \| x _ { 0 } - x \| .
$$

Definition 6.1.3. Assume that the iterative method (6.1.6) is convergent. The average rate $R _ { k } ( G )$ and asymptotic rate $R _ { \infty } ( G )$ of convergence are defined as

$$
R _ { k } ( G ) = - \frac { 1 } { k } \ln \| G ^ { k } \| , \qquad R _ { \infty } ( G ) = - \ln \rho ( G ) ,
$$

respectively, where $\| \cdot \|$ is any consistent matrix norm.

To reduce the norm of the error by a fixed factor $\delta$ ,at most $k$ iterations are needed where $\| G ^ { k } \| \leq \delta$ or, equivalently, $k$ satisfies

$$
k \geq - \ln \delta / R _ { k } ( G ) .
$$

It is desirable for the iteration matrix $G = I - M ^ { - 1 } A$ to have real eigenvalues. This will be the case if the iterative method is symmetrizable.

Definition 6.1.4. The stationary iterative method (6.1.6) is said to be symmetrizable if there is a nonsingular matrix $W$ such that

$$
W ( I - G ) W ^ { - 1 } = W M ^ { - 1 } A W ^ { - 1 }
$$

is symmetric positive definite.

f $A$ and the splitting matrix $M$ are both symmetric positive definite, then the corresponding stationary method is symmetrizable.To show this,let $R$ be the Cholesky factor of $A$ and set $W = R$ .Then

$$
R ( M ^ { - 1 } A ) R ^ { - 1 } = R M ^ { - 1 } R ^ { T } R R ^ { - 1 } = R M ^ { - 1 } R ^ { T } .
$$

If $M$ is symmetric positive definite, then so is $M ^ { - 1 }$ and also $R M ^ { - 1 } R ^ { T }$

# Notes and references

The convergence of (6.1.6） when $\operatorname { r a n k } ( A ) ~ < ~ n$ is investigated by Keller [690,1965] and Young [1141, 2oo3]. Dax [293,199o] investigates the convergence properties of stationary iter-ative methods,with the emphasis is on properties that hold for singular and possibly inconsistent systems for a square matrix $A$ ．Tanabe [1O56,1971] considers stationary iterative methods of the form (6.1.1O) for computing more general solutions $x = A ^ { - } b$ ,where $A ^ { - }$ is any generalized inverse of $A$ such that $A A ^ { - } A = I$ 、He shows that the iteration can always be written in the form

$$
x _ { k + 1 } = x _ { k } + B ( b - A x _ { k } )
$$

for some matrix $B$ , and characterizes the solution in terms of $\mathcal { R } ( A B )$ and $\mathcal { N } ( B A )$

The concept of splitting has been extended to rectangular matrices by Plemmons [896,1972]. Berman and Plemmons [112,1974l define $A = M - N$ to be a proper splitting if the ranges and nullspaces of $A$ and $M$ are equal. They show that for a proper splitting,the iteration

$$
x _ { k + 1 } = M ^ { \dagger } ( N x _ { k } + b )
$$

converges to the pseudoinverse solution $x = A ^ { \dagger } b$ for every $x _ { 0 }$ if and only if the spectral radius $\rho ( M ^ { \dagger } N ) < 1$ . The iterative method (6.1.10) avoids explicit use of the normal system.

# 6.1.3 - Richardson's Method for the Normal Equations

A stationary iteration method for solving the normal equations $A ^ { T } A x \ = \ A ^ { T } b$ has the form $M x _ { k + 1 } = N x _ { k } + A ^ { T } b$ where $A ^ { T } A = M - N$ is a splitting. Explicit use of $A ^ { T } A$ can be avoided by noting that $N = M - A ^ { T } A$ and rewriting the iteration as

$$
x _ { k + 1 } = x _ { k } + M ^ { - 1 } A ^ { T } ( b - A x _ { k } ) , \quad k = 0 , 1 , \ldots .
$$

This iteration is symmetrizable if $A$ has full column rank and $M$ is symmetric positive definite.

For solving the minimum norm problem(6.1.2),the same splitting is applied to solve $A ^ { T } A z =$ $c$ ， giving the iteration $z _ { k + 1 } = z _ { k } + M ^ { - 1 } ( c - A ^ { T } A z _ { k } )$ After multiplying with $A$ and using $y _ { k } = A z _ { k }$ ,we obtain

$$
y _ { k + 1 } = y _ { k } + A M ^ { - 1 } ( c - A ^ { T } y _ { k } ) , \quad k = 0 , 1 , \ldots .
$$

In the following we assume that $A ^ { T } A$ is positive definite.In (6.1.11),the particular choice $M = \omega ^ { - 1 } I$ gives Richardson's first-order method

$$
x _ { k + 1 } = x _ { k } + \omega A ^ { T } ( b - A x _ { k } ) , \quad k = 0 , 1 , 2 , \ldots ,
$$

where $\omega > 0$ is a relaxation parameter. Richardson's method is often used for solving least squares problems originating from discretized il-posed problems.In this context (6.1.13) is also known as Landweber's method; see Section 6.4.1. If $x _ { 0 } \in \mathcal { R } ( A ^ { T } )$ (e.g., $x _ { 0 } = 0 \textrm { \textrm { } }$ )，then by construction $x _ { k } \in \mathcal { R } ( A ^ { T } )$ for all $k > 0$ .Hence,in exact arithmetic,Richardson's method converges to the pseudoinverse solution when $A$ is rank-deficient,

For the iteration (6.1.13) the error satisfies

$$
x _ { k } - x = G ( x _ { k - 1 } - x ) , \quad G = I - \omega A ^ { T } A .
$$

The eigenvalues of the iteration matrix $G$ are $\lambda _ { i } ( G ) = 1 - \omega \sigma _ { i } ^ { 2 }$ ， $i = 1 , \ldots , n$ , where $\sigma _ { i }$ are the singular values of $A$

Theorem 6.1.5. Assume that the singular values $\sigma _ { i }$ of $A$ satisfy $0 < a \le \sigma _ { i } ^ { 2 } \le b _ { \cdot }$ $i = 1 , \ldots , n$ Then Richardson's method converges if and only if $0 < \omega < 2 / b$

Proof. By the assumption, $1 - \omega b \leq \lambda _ { i } ( G ) \leq 1 - \omega a$ for all $i$ Hence,if $1 - \omega a \textless 1$ and $1 - \omega b > - 1$ ,then $\rho ( G ) < 1$ Since $a > 0$ ,the first condition is satisfied for all $\omega > 0$ ,while the second condition is satisfied if $\omega < 2 / b$ □

To maximize the asymptotic rate of convergence, $\omega$ should be chosen so that the spectral radius

$$
\rho ( G ) = \operatorname* { m a x } \{ | 1 - \omega a | , | 1 - \omega b | \}
$$

is minimized. The optimal $\omega$ lies in the intersection of the graphs of $| 1 - \omega a |$ and $| 1 - \omega b |$ ， $\omega \in ( 0 , 2 / b )$ . Setting $1 - \omega a = \omega b - 1$ ,we obtain

$$
\begin{array} { r } { \omega _ { \mathrm { o p t } } = 2 / ( b + a ) , \quad \rho _ { \mathrm { o p t } } ( G ) = ( b - a ) / ( b + a ) . } \end{array}
$$

Since $\kappa ^ { 2 } ( A ) = b / a$ , we have

$$
\rho _ { \mathrm { o p t } } ( G ) = \frac { \kappa ^ { 2 } ( A ) - 1 } { \kappa ^ { 2 } ( A ) + 1 } = 1 - \frac { 2 } { \kappa ^ { 2 } ( A ) + 1 } .
$$

This illustrates a typical property of iterative methods in which they converge more slowly for ill-conditioned systems.

# Richardson's nonstationary method is

$$
x _ { k + 1 } = x + \omega _ { k } A ^ { T } ( b - A x _ { k } ) , \quad k = 0 , 1 , \ldots ,
$$

where $\omega _ { k } > 0$ .Sufficient conditions for convergence of this iteration are known, which we state below without proof.

Theorem 6.1.6. The iterates (6.1.16) converge for all vectors $b$ to a least squares solution ${ \hat { x } } = \arg \operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ iffor some $\epsilon > 0$ it holds that

$$
0 < \epsilon \leq \omega _ { k } \leq ( 2 - \epsilon ) / \sigma _ { 1 } ^ { 2 } \quad \forall k ,
$$

where $\sigma _ { 1 }$ is the largest singular value of $A$ If $x _ { 0 } \in \mathcal { R } ( A ^ { H } )$ ，then $\hat { x }$ is the unique least-norm solution.

# 6.1.4 - The Jacobi and Gauss-Seidel Methods

In the following we use the standard spliting

$$
\boldsymbol { A } ^ { T } \boldsymbol { A } = \boldsymbol { L } + \boldsymbol { D } + \boldsymbol { L } ^ { T } , \quad \boldsymbol { D } = \mathrm { d i a g } \left( \boldsymbol { A } ^ { T } \boldsymbol { A } \right) ,
$$

where $A = ( a _ { 1 } , \ldots , a _ { n } ) \in \mathbb { R } ^ { m \times n }$ ， $D = \operatorname { d i a g } \left( d _ { 1 } , \ldots , d _ { n } \right)$ is diagonal, and $L$ is strictly lower triangular. In Jacobi's method for the normal equations $A ^ { T } A x = A ^ { T } b$ the splitting $M = D$ is used, giving the iteration

$$
x _ { k + 1 } = x _ { k } + D ^ { - 1 } A ^ { T } \big ( b - A x _ { k } \big ) .
$$

The minimum norm solution of $A ^ { T } y = c$ is $y = A z$ where $z$ satisfies $A ^ { T } A z = c$ Applying Jacobi's method to these equations gives

$$
z _ { k + 1 } = z _ { k } + D ^ { - 1 } ( c - A ^ { T } A z _ { k } ) .
$$

Multiplying by $A$ and setting $A z _ { k } = y _ { k }$ ,we obtain the iteration

$$
y _ { k + 1 } = y _ { k } + A D ^ { - 1 } ( c - A ^ { T } y _ { k } ) .
$$

Since $M = D$ is symmetric positive definite, Jacobi's method is symmetrizable. If the columns of $A$ are scaled to have unit norm, then $D = I$ ，and Jacobi's method becomes Richardson's method with $\omega = 1$

The Gauss-Seidel method for the normal equations $A ^ { T } A = A ^ { T } b$ uses the splitting $M =$ $L + D$ ，where $D$ is the diagonal and $L$ is the strictly lower triangular part of $A ^ { T } A$ In matrix form the iteration becomes

$$
x _ { k + 1 } = x _ { k } + ( L + D ) ^ { - 1 } A ^ { T } { \big ( } b - A x _ { k } { \big ) } .
$$

For the minimum norm problem, the Gauss-Seidel iteration method is

$$
y _ { k + 1 } = y _ { k } + A ( L + D ) ^ { - 1 } ( c - A ^ { T } y _ { k } ) , \quad k = 0 , 1 , \ldots .
$$

The method is not symmetrizable. Each step requires the solution of a lower triangular system by forward substitution and splits into $n$ minor steps. Note that the ordering of the columns of $A$ will influence the convergence.To implement the Gauss-Seidel method the key observation is that it differs from the Jacobi method only in the following respect. As soon as a new component of $x _ { k + 1 }$ has been computed, t is used for computing the remaining part of $x _ { k + 1 }$

Björck and Elfving [141,1979l show that the Gauss-Seidel method applied to the normal equations of the first and second kinds are special cases of two classes of projection methods for square nonsingular linear systems studied by Householder and Bauer [646,196o]. In the first class of methods for $A x = b$ ,let $p _ { 1 } , p _ { 2 } , \ldots \notin \mathcal { N } ( A )$ be a sequence of $n$ -vectors. Let $x ^ { ( 1 ) }$ be an initial approximation,and for $j = 1 , 2 , \dots$ , compute

$$
\boldsymbol { x } ^ { ( j + 1 ) } = \boldsymbol { x } ^ { ( j ) } + \alpha _ { j } \boldsymbol { p } _ { j } , \quad q _ { j } = A \boldsymbol { p } _ { j } , \quad \alpha _ { j } = q _ { j } ^ { T } \boldsymbol { r } _ { j } / \| q _ { j } \| _ { 2 } ^ { 2 } ,
$$

where $r ^ { ( j ) } = b - A x ^ { ( j ) }$ is the residual vector. Then $r ^ { ( j + 1 ) } \perp q _ { j }$ and

$$
\| r ^ { ( j + 1 ) } \| _ { 2 } ^ { 2 } = \| r ^ { ( j ) } \| _ { 2 } ^ { 2 } - | \alpha _ { j } | ^ { 2 } \| q _ { j } \| _ { 2 } ^ { 2 } \leq \| r ^ { ( j ) } \| _ { 2 } ^ { 2 } .
$$

This shows that (6.1.22) is a residual-reducing iteration method. This method was originally devised by de la Garza 442,1951].

One step of the Gauss-Seidel method for $A ^ { T } A x = A ^ { T } b$ is obtained by taking $p _ { j }$ in (6.1.22) to be the unit vectors $e _ { j } \in \mathbb { R } ^ { n } , j = 1 , \dots , n$ , in cyclic order. Then $q _ { j } = A e _ { j } = a _ { j }$ ,and one iteration splitsinto $n$ minr steps flws.Let $x _ { k } ^ { ( 1 ) } = x _ { k }$ be the currenieaea $r _ { k } ^ { ( 1 ) } = b - A x _ { k } ^ { ( 1 ) }$ be the corresponding residual. The Gauss-Seidel iteration becomes the following: For $j = 1 , \dotsc , n$ ， compute

$$
\begin{array} { r l } & { x _ { k } ^ { ( j + 1 ) } = x _ { k } ^ { ( j ) } + \delta _ { j } e _ { j } , \quad \delta _ { j } = a _ { j } ^ { T } r _ { k } ^ { ( j ) } / \| a _ { j } \| _ { 2 } ^ { 2 } , } \\ & { r _ { k } ^ { ( j + 1 ) } = r _ { k } ^ { ( j ) } - \delta _ { j } a _ { j } . } \end{array}
$$

Then $x _ { k + 1 } = x _ { k } ^ { ( n + 1 ) }$ and $r _ { k + 1 } = r _ { k } ^ { ( n + 1 ) }$ In the $j$ th minor step.only the $j$ th component is changed,and only the $j$ th column $a _ { j } = A e _ { j }$ is accessed. The iteration simplifies if the columns are prescaled to have unit norm.

The second class of projection methods finds the minimum norm solution of $A ^ { T } y = c =$ $( c , \ldots , c _ { n } ) ^ { T }$ .Let $p _ { 1 } , p _ { 2 } , \dotsc \notin { \mathcal { N } } ( A )$ be a sequence of $n$ -vectors, and set $q _ { j } = A p _ { j }$ . Compute

$$
y ^ { ( j + 1 ) } = y ^ { ( j ) } + \delta _ { j } q _ { j } , \quad \delta _ { j } = p _ { j } ^ { T } ( c - A ^ { T } y ^ { ( j ) } ) / \| q _ { j } \| _ { 2 } ^ { 2 } , \quad j = 1 , 2 , \ldots .
$$

By construction we have $d ^ { ( j + 1 ) } \perp q _ { i }$ ，where $d ^ { ( j ) } = y - y ^ { ( j ) }$ denotes the error. It follows that

$$
\begin{array} { r } { \| d ^ { ( j + 1 ) } \| _ { 2 } ^ { 2 } = \| d ^ { ( j ) } \| _ { 2 } ^ { 2 } - | \delta _ { j } | ^ { 2 } \| q _ { j } \| _ { 2 } ^ { 2 } \leq \| d ^ { ( j ) } \| _ { 2 } ^ { 2 } . } \end{array}
$$

Hence this class of methods is error-reducing.

The Gauss-Seidel method for the minimum norm solution of $A ^ { T } y = c$ is obtained by taking $p _ { j }$ in (6.1.24) to be the unit vectors $e _ { j }$ in cyclic order. Then $p _ { j } ^ { T } A = a _ { j } ^ { T }$ and $p _ { j } ^ { T } c = c _ { j }$ . Let the curret iterate be $y _ { k } \in { \mathcal { R } } ( A )$ , and set $y _ { k } ^ { ( 1 ) } = y _ { k }$ The Gus-Seidelmethod issfollows: For $j = 1 , \dotsc , n$ ,compute

$$
y _ { k } ^ { ( j + 1 ) } = y _ { k } ^ { ( j ) } + \delta _ { j } a _ { j } , \quad \delta _ { j } = ( c _ { j } - a _ { j } ^ { T } y _ { k } ^ { ( j ) } ) / d _ { j } ,
$$

and set yk+1 = yk For a square matrix $A$ , this method was originally devised by Kaczmarz [678, 1937].

Cimmino [250,1938] devised another notable error-reducing iterative method for the approx-imate solution of a linear system $A x = b$ ，where initially $A \in \mathbb { R } ^ { n \times n }$ is assumed to be square and nonsingular; see Benzi [1O7,2oo5] for an English translation. Cimmino notes that the unique solution $x = A ^ { - 1 } b$ lies on the intersection of the $m$ hyperplanes

$$
a _ { i } ^ { T } x = b _ { i } , \quad i = 1 , \ldots , n ,
$$

where $a _ { i } ^ { T } = e _ { i } ^ { T } A$ is the ith row of $A$ . Given an initial approximation $x ^ { ( 0 ) }$ , he forms

$$
x _ { i } ^ { ( 0 ) } = x ^ { ( 0 ) } + 2 \frac { ( b _ { i } - a _ { i } ^ { T } x ^ { ( 0 ) } ) } { \| a _ { i } \| _ { 2 } ^ { 2 } } a _ { i } , \quad i = 1 , \ldots , n .
$$

This has a nice geometrical interpretation. Subtracting $x$ from both sides of (6.1.27) and using $b _ { i } = a _ { i } ^ { T } x$ gives

$$
x _ { i } ^ { ( 0 ) } - x = P _ { i } ( x ^ { ( 0 ) } - x ) , \quad P _ { i } = I - 2 ( a _ { i } a _ { i } ^ { T } ) / \| a _ { i } \| _ { 2 } ^ { 2 } .
$$

This $i = 1 , \dots$ $x ^ { ( 0 ) }$ with rspetto

$$
\| x _ { i } ^ { ( 0 ) } - x \| _ { 2 } = \| x ^ { ( 0 ) } - x \| _ { 2 } , \quad i = 1 , \ldots , n .
$$

Hencethe initial point x(anditsn reflectiosx all lie on a hypersphere. If $A$ is square and nonsingular, the center of this hypersphere is the unique solution of $A x = b$ .The next iterate $x ^ { ( 1 ) }$ in Cimmino's method is taken as the center of gravity of the mass system formed by placing $n$ positive masses $w _ { i }$ at the points $x _ { i } ^ { ( 0 ) }$ ， $i = 1 , \ldots , n$

$$
x ^ { ( 1 ) } = \frac { 1 } { \mu } \sum _ { i = 1 } ^ { n } w _ { i } x _ { i } ^ { ( 0 ) } , \quad \mu = \sum _ { i = 1 } ^ { m } w _ { i } .
$$

Because the center of gravity of the system of masses $w _ { i }$ must fall inside this hypersphere, Cimmino's method is error-reducing,i.e., $\| x ^ { ( 1 ) } - x \| _ { 2 } < \| x ^ { ( 0 ) } - x \| _ { 2 }$ In matrix form Cimmino's method can be written

$$
x ^ { ( k + 1 ) } = x ^ { ( k ) } + \frac { 2 } { m } A ^ { T } D ^ { T } D ( b - A x ^ { ( k ) } ) ,
$$

where

$$
D = \operatorname { d i a g } \left( d _ { 1 } , \ldots , d _ { n } \right) , \quad d _ { i } = \sqrt { w _ { i } } / \| a _ { i } \| _ { 2 } .
$$

Cimmino notes that if $\operatorname { r a n k } ( A ) > 2$ , the iterates converge even when $A \in \mathbb { R } ^ { n \times n }$ is singular and the linear system is inconsistent. Then Cimmino's method will converge to a solution of the weighted least squares problem $\operatorname* { m i n } _ { x } \| D ( A x - b ) \| _ { 2 }$ If $w _ { i } = \| a _ { i } \| _ { 2 } ^ { 2 }$ ,then $D = I$ ,and (6.1.30) is Richardson's method with $\omega = 2 / \mu$

# Notes and references

Kaczmarz's method was rediscovered by Gordon,Bender,and Herman [518,197o] and given the name ART (Algebraic Reconstruction Technique). ART was successfully used in the first computerized tomography (CT) scanner patented by Houndsfield in 1972; see Censor and Zenios [214, 1997].It is still extensively used for this purpose. Iterative methods such as Kaczmarz's and Cimmino's that require access to only one row of $A$ at each minor step are sometimes called “row-action methods.” A survey of this class of methods is given by Censor [213,1981].

# 6.1.5 - Successive Overrelaxation Methods

The rate of convergence of the Gauss-Seidel method can be improved by introducing a relaxation parameter $\omega > 1$ . The successive overrelaxation method (SOR) for the normal equations $A ^ { T } A = A ^ { T } b$ is obtained simply by changing $\delta _ { j }$ to $\omega \delta _ { j }$ in (6.1.24). Similarly, SOR for the normal equations of the second kind $A ^ { T } y = c$ ， $y = A z$ ,is obtained by changing $\delta _ { j }$ to $\omega \delta _ { j }$ in (6.1.25). The symmetric SOR (SSOR) method is obtained by following each step of SOR with another

SOR step where the columns of $A$ are taken in reverse order, $j = n , \ldots , 2 , 1$ .The SSOR iteration is symmetrizable. SOR and SSOR share with the Gauss-Seidel method the advantages of simplicity and small storage requirements.

For positive definite $A ^ { T } A$ ，SOR converges if and only if $0 < \omega < 2$ ，The parameter $\omega$ in SOR should,if possible, be chosen to maximize the asymptotic rate of convergence. If $A ^ { T } A$ has the following special property, the optimal $\omega$ is known.

Definition 6.1.7. A square matrix $A$ with the decomposition $A = D ( I + L + U )$ ，where $D$ is nonsingular and $L \left( U \right)$ are strictly lower (upper) triangular, is said to be consistently ordered if it has the property that the eigenvalues of $J ( \alpha ) \equiv \alpha L + \alpha ^ { - 1 } U , \alpha \neq$ $\alpha \neq 0$ ， are independent of $\alpha$

A block tridiagonal matrix $A$ whose diagonal blocks are nonsingular diagonal matrices can be shown to be consistently ordered. In particular, this is true if there exists a permutation matrix $P$ such that $P A ^ { T } A P ^ { T }$ has the form

$$
\left( \begin{array} { c c } { { D _ { 1 } } } & { { U _ { 1 } } } \\ { { L _ { 1 } } } & { { D _ { 2 } } } \end{array} \right) ,
$$

where $D _ { 1 }$ and $D _ { 2 }$ are nonsingular diagonal matrices. Such a matrix is said to have property A.   
The following result is due to Young [1141, 2003].

Theorem 6.1.8. Let $A$ be a consistently ordered matrix, and assume that the eigenvalues $\mu$ of the Jacobi iteration matrix $G _ { J } = L + U$ are real, and its spectral radius satisfies $\rho ( G _ { J } ) < 1$ Then the optimal relaxation parameter $\omega$ in SOR is given by

$$
\omega _ { \mathrm { o p t } } = \frac { 2 } { 1 + \sqrt { 1 - \rho _ { J } ^ { 2 } } } , \qquad \rho ( G _ { \omega _ { \mathrm { o p t } } } ) = \omega _ { \mathrm { o p t } } - 1 .
$$

If $A$ is consistently ordered, then using $\omega _ { \mathrm { o p t } }$ in SOR gives a great improvement in the rate of convergence.Otherwise, SOR may not be effective for any choice of $\omega$ .In contrast to SOR, the rate of convergence of SSOR is not very sensitive to the choice of $\omega$ .Taking $\omega = 1$ ,i.e., using the symmetric Gauss-Seidel method,is often close to optimal; see Axelsson [48,1994].

# Notes and references

Bramley and Sameh [175,1992] develop row projection methods related to Kaczmarz's method for large unsymmetric linear systems.For a three-dimensional grid problem with $n ^ { 3 }$ unknowns, each iteration can be split into $n ^ { 2 } / 9$ subproblems．Arioli et al.[35,1992],[38,1995] develop a block projection method for accelerating the block Cimmino method. A robust and efficient solver for ellptic equations by Gordon and Gordon [517, 2oo8] is based on a similar technique.

# 6.1.6 - The Chebyshev Semi-iterative Method

Consider a stationary iterative method $\tilde { x } _ { 0 } = x _ { 0 }$

$$
\tilde { x } _ { k + 1 } = \tilde { x } _ { k } + M ^ { - 1 } A ^ { T } ( b - A \tilde { x } _ { k } ) , \quad k = 0 , 1 , \ldots ,
$$

for solving the normal equations $A ^ { T } A x = A ^ { T } b$ ,associated with the splitting $A ^ { T } A = M - N$ with $M$ symmetric positive definite. Then the eigenvalues $\{ \lambda _ { i } \} _ { i = 1 } ^ { n }$ of $M ^ { - 1 } A ^ { T } A$ are real. Assume that lower and upper bounds are known such that

$$
0 < a \leq \lambda _ { i } ( G ) < b , \quad i = 1 , \ldots , n ,
$$

where $G = I - M ^ { - 1 } A ^ { T } A$ is the iteration matrix. Then the eigenvalues $\{ \rho _ { i } \} _ { i = 1 } ^ { n }$ of $G$ are real and satisfy

$$
1 - b = c < \rho _ { i } \leq d = 1 - a < 1 .
$$

(Note that we allow $c \leq - 1$ ,even though then $\rho ( G ) \geq 1$ ,and the iteration (6.1.34) is divergent!) To attempt to accelerate convergence of the basic iteration we take a linear combination of the first $k$ iterations,

$$
x _ { 0 } = \tilde { x } _ { 0 } , \quad x _ { k } = \sum _ { i = 0 } ^ { k } c _ { k i } \tilde { x } _ { i } , \quad k = 1 , 2 , \ldots ,
$$

where, for consistency, we require that $\textstyle \sum _ { i = 0 } ^ { k } c _ { k i } = 1$ The resulting iteration is known as a semi-iterative method; see Varga [1090,1962]. The error equation for the basic iteration method (6.1.34) is

$$
\tilde { x } _ { k } - x = G ^ { k } ( \tilde { x } _ { 0 } - x ) ,
$$

and from (6.1.37) it follows for the semi-iterative method that

$$
x _ { k } - x = P _ { k } ( G ) ( x _ { 0 } - x ) ,
$$

where

$$
P _ { k } ( t ) = \sum _ { i = 0 } ^ { k } c _ { k i } t ^ { i } , \quad P _ { k } ( 1 ) = 1 ,
$$

is a polynomial of degree $k$ .Such a polynomial is called a residual polynomial. Hence,a measure of the rate of convergence for the accelerated sequence (6.1.37) is given by the spectral radius $\rho ( P _ { k } ( G ) ) \leq \operatorname* { m a x } _ { t \in [ c , d ] } | P _ { k } ( t ) |$ .To minimize this quantity, we seek the polynomial that solves

$$
\operatorname* { m i n } _ { P _ { k } \in \Pi _ { k } ^ { } ^ { 1 } } \operatorname* { m a x } _ { t \in [ c , d ] } | P _ { k } ( t ) | ,
$$

where $\Pi _ { k } ^ { 1 }$ denotes the set of all polynomials of degree $k$ such that $P _ { k } ( 1 ) = 1$

The solution to the minimization problem (6.1.40) can be expressed in terms of the Chebyshev polynomials $T _ { k } ( z )$ of the first kind; see Section 4.5.2. These are defined by the three-term recurrence relation $T _ { 0 } ( z ) = 1$ ， $T _ { 1 } ( z ) = z$ ,and

$$
T _ { k + 1 } ( z ) = 2 z T _ { k } ( z ) - T _ { k - 1 } ( z ) , \quad k \geq 1 .
$$

By induction it follows that the leading coefficient of $T _ { k } ( z )$ is $2 ^ { k - 1 }$ $T _ { k } ( z )$ may also be expressed explicitly as

$$
\begin{array} { r } { T _ { k } ( z ) = \left\{ \begin{array} { l l } { \cos ( k \phi ) ) , } & { z = \cos \phi \quad \mathrm { ~ i f ~ } | z | \le 1 , } \\ { \cosh ( k \gamma ) , } & { z = \cosh \gamma \quad \mathrm { ~ i f ~ } | z | > 1 . } \end{array} \right. } \end{array}
$$

Thus, $| T _ { k } ( z ) | \le 1$ for $| z | \le 1$ .For $| z | \geq 1$ we have $\begin{array} { r } { z = \frac { 1 } { 2 } ( w + w ^ { - 1 } ) } \end{array}$ , where $w = e ^ { \gamma }$ . By solving a quadratic equation in $w$ ,we get

$$
\begin{array} { r } { T _ { k } ( z ) = \frac { 1 } { 2 } ( w ^ { k } + w ^ { - k } ) , \quad w = z \pm \sqrt { z ^ { 2 } - 1 } > 1 . } \end{array}
$$

This shows that outside the interval $[ - 1 , 1 ]$ ， $T _ { k } ( z )$ grows exponentially with $k$ .The Chebyshev polynomial $T _ { k } ( z )$ has the following extremal property.

Theorem 6.1.9. Let $\mu$ be any fixed number such that $\mu > 1$ If we let $P _ { k } ( z ) = T _ { k } ( z ) / T _ { k } ( \mu )$ ， then $P _ { k } ( \mu ) = 1$ and

$$
\operatorname* { m a x } _ { 1 \leq z \leq 1 } | P _ { k } ( z ) | = 1 / T _ { k } ( \mu ) .
$$

Moreover,if $Q ( z )$ is any polynomial of degree $k$ or less such that $Q ( \mu ) = 1$ and $\operatorname* { m a x } _ { 1 \leq z \leq 1 } | Q ( z ) |$ $\leq 1 / T _ { k } ( \mu )$ ,then $Q ( z ) = P _ { k } ( z )$

Proof. See Young [1141, 2003, Theorem 3.1].

From this result it follows that the solution to the minmax problem (6.1.4O) is a scaled and shifted Chebyshev polynomial. Let

$$
z ( t ) = ( 2 t - ( d + c ) ) / ( d - c )
$$

be the linear transformation that maps the interval $t \in [ c , d ]$ onto $z \in [ - 1 , 1 ]$ . Then the solution to the minimization problem (6.1.40) is given by

$$
P _ { k } ( t ) = \frac { T _ { k } ( z ( t ) ) } { T _ { k } ( z ( 1 ) ) } , \quad \mu = z ( 1 ) = ( 2 - ( d + c ) ) / ( d - c ) = \frac { b + a } { b - a } ,
$$

where we have used the facts that $a = 1 - d$ and $b = 1 - c$ ; see (6.1.36). It follows that a bound for the spectral radius of $P _ { k } ( G )$ is given by

$$
\rho ( P _ { k } ( G ) ) \leq 1 / T _ { k } ( \mu ) = 1 / \cosh ( k \gamma ) , \quad \cosh \gamma = \mu .
$$

If the splitting matrix $M$ is symmetric and positive definite, then $\kappa ^ { 2 } = b / a > 1$ is an approximate upper bound for the condition number of $M ^ { - 1 } A ^ { T } A$ .From (6.1.35) it follows that

$$
\mu = ( \kappa + 1 ) / ( \kappa - 1 ) , \quad \kappa = b / a ,
$$

is an upper bound for the spectral condition number of $A$ . An elementary calculation shows that

$$
w = \mu + \sqrt { \mu ^ { 2 } - 1 } = \frac { \kappa + 1 } { \kappa - 1 } + \frac { 2 \sqrt { \kappa } } { \kappa - 1 } = \frac { \sqrt { \kappa } + 1 } { \sqrt { \kappa } - 1 } > 1 .
$$

From (6.1.43) it follows that $\rho ( q _ { k } ( A ) ) \leq 1 / T _ { k } ( \mu ) < 2 e ^ { - k \gamma }$ , where

$$
\gamma = \log { \left( \frac { \sqrt { \kappa } + 1 } { \sqrt { \kappa } - 1 } \right) } > \frac { 2 } { \sqrt { \kappa } } .
$$

Hence, to reduce the error norm by at least a factor of $\delta < 1$ it suffices to perform $k$ iterations, where

$$
k > \frac { 1 } { 2 } \sqrt { \kappa } \log \left( \frac { 2 } { \delta } \right) .
$$

Hence,the number of iterations required for the Chebyshev accelerated method to achieve a certain accuracy is proportional to $\sqrt { \kappa }$ rather than $\kappa$ as for Richardson's method; see Section 6.1.3. This is a great improvement but assumes that the upper and lower bounds in (6.1.35) for the eigenvalues are suficiently accurate.

The Chebyshev Semi-iterative (CSI) method by Golub and Varga [513,1961] is an efficient and stable way to implement Chebyshev acceleration. Itcan be applied to accelerate any stationary iterative method for the normal equations

$$
x _ { k + 1 } = x _ { k } + M ^ { - 1 } A ^ { T } ( b - A x _ { k } ) , \quad k = 0 , 1 , \ldots ,
$$

provided it is symmetrizable. CSI also has the advantage that the number of iterations need not be fixed in advance. CSI uses a clever rewriting of the three-term recurrence relation for the Chebyshev polynomials to compute $x ^ { ( k ) }$ directly.

# Algorithm 6.1.1 (The Chebyshev Semi-iterative Method).

Set $\alpha = 2 / ( a + b )$ ， $\mu = ( b - a ) / ( b + a ) ,$ and let

$$
r _ { k } = b - A x _ { k } , \qquad s _ { k } = M ^ { - 1 } A ^ { T } r _ { k } , \quad k \ge 0 .
$$

Take $x _ { 1 } = x _ { 0 } + \alpha s _ { 0 }$ ， $\omega _ { 1 } = 2 ,$ and for $k \geq 1$ compute

$$
x _ { k + 1 } = x _ { k - 1 } + \omega _ { k + 1 } \big ( \alpha s _ { k } + x _ { k } - x _ { k - 1 } \big ) ,
$$

where $\begin{array} { r } { \omega _ { k + 1 } = \left( 1 - \frac { \mu ^ { 2 } } { 4 } \omega _ { k } \right) ^ { - 1 } } \end{array}$

Each iteration requires two matrix-vector multiplications $A x _ { k }$ and $A ^ { T } r _ { k }$ ,and the solution of $M s ^ { ( k ) } = A ^ { T } r _ { k }$ . The second-order Richardson method can also be described by (6.1.49) with $\alpha$ and $\mu$ as above,and

$$
\omega _ { k } = \widehat { \omega } = \frac { 2 } { ( 1 + \sqrt { 1 - \mu ^ { 2 } } ) } .
$$

It can be shown that in the CSI method, $\omega _ { k }  \widehat { \omega }$ as $k \to \infty$

For SOR, the eigenvalues of the iteration matrix $B _ { \omega _ { \mathrm { o p t } } }$ are al complex with modulus $| \omega _ { \mathrm { o p t } } |$ In this case, convergence acceleration is of no use; see Young [1141, 2oo3]. On the other hand, for SSOR, Chebyshev acceleration often achieves a substantial gain in convergence rate.

# 6.2 - Krylov Subspace Methods

# 6.2.1 - The Conjugate Gradient Method

Iterative methods that minimize an error functional over a sequence of Krylov subspaces play a fundamental role in solving large-scale linear systems and least squares problems. Basic properties of Krylov subspaces are given in Section 4.2.3. The prototype for such methods is the conjugate gradient (CG) method for solving symmetric positive definite linear systems $A x = b$ ， $A \in \mathbb { C } ^ { n \times n }$ . It was developed independently by Hestenes and Stiefel and published in their joint seminal paper [608,1952].

Given an initial approximation $x _ { 0 }$ , CG generates a sequence of approximate solutions $x _ { k }$ as follows. Set $p _ { 0 } = r _ { 0 } = b - A x _ { 0 }$ ,and for $k = 1 , 2 , \ldots$ , compute

$$
x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k } , \quad r _ { k + 1 } = r _ { k } - \alpha _ { k } A p _ { k } , \quad p _ { k + 1 } = r _ { k + 1 } + \beta _ { k } p _ { k } ,
$$

where $\alpha _ { k }$ and $\beta _ { k }$ are parameters to be chosen. A simple induction argument using (6.2.1) shows that $r _ { k }$ and $p _ { k }$ lie in the Krylov subspaces

$$
\mathcal { K } _ { k } ( A , r _ { 0 } ) = \operatorname { s p a n } \big \{ r _ { 0 } , A r _ { 0 } , \ldots , A ^ { k - 1 } r _ { 0 } \big \} , \quad k = 1 , 2 , \ldots .
$$

In CG, $\alpha _ { k }$ is chosen to make $r _ { k + 1 }$ orthogonal to $p _ { k }$ . From $p _ { k } ^ { H } ( r _ { k } - \alpha _ { k } A p _ { k } ) = 0$ we obtain

$$
\alpha _ { k } = \frac { p _ { k } ^ { H } r _ { k } } { p _ { k } ^ { H } A p _ { k } } .
$$

The parameter $\beta _ { k }$ is chosen to make $p _ { k + 1 }$ $A$ orthogonal or conjugate to $p _ { k }$

$$
( p _ { k + 1 } , p _ { k } ) _ { A } = 0 ,
$$

where the $A$ -inner product and $A$ -norm, also called energy norm, are defned by

$$
( \boldsymbol { u } , \boldsymbol { v } ) _ { A } = \boldsymbol { u } ^ { H } \boldsymbol { A } \boldsymbol { v } , \qquad \| \boldsymbol { u } \| _ { A } = ( \boldsymbol { u } ^ { H } \boldsymbol { A } \boldsymbol { u } ) ^ { 1 / 2 } .
$$

This explains the name “conjugate gradient method.” Multiplying (6.2.1) by $p _ { k } ^ { H } A$ ,we obtain

$$
\beta _ { k } = - \frac { p _ { k } ^ { H } A r _ { k + 1 } } { p _ { k } ^ { H } A p _ { k } } .
$$

Equations (6.2.1), (6.2.3),and (6.2.6) fuly define the CG method.

Theorem 6.2.1. In CG, the residual vector $r _ { k }$ is orthogonal to all previous direction vectors and residual vectors:

$$
r _ { k } ^ { H } p _ { j } = 0 , \quad \quad r _ { k } ^ { H } r _ { j } = 0 , \quad j = 0 : k - 1 .
$$

The direction vectors are mutually $A$ -conjugate:

$$
p _ { k } ^ { H } A p _ { j } = 0 , \quad j = 0 { : } k - 1 .
$$

Proof. We prove (6.2.7) and (6.2.8) jointly by induction. The choice of $\alpha _ { k }$ ensures that $r _ { k }$ is orthogonal to $p _ { k - 1 }$ ,and (6.2.4) shows that (6.2.8) holds also for $j = k - 1$ Hence these relations are true for $k = 1$ . Assume now that the relations are true for some $k > 1$ .From $p _ { k } ^ { H } r _ { k + 1 } = 0$ ， changing the index and taking the scalar product with $p _ { j }$ ， $0 \leq j < k$ ,we get

$$
r _ { k + 1 } ^ { H } p _ { j } = r _ { k } ^ { H } p _ { j } - \alpha _ { k } p _ { k } ^ { H } A p _ { j } .
$$

iise $r _ { k + 1 } ^ { H } p _ { k } = 0$ it fllous ht()62.) ho for $k + 1$ .From (6.2.1),the induction hypothesis,and (6.2.8),we find that

$$
\begin{array} { r l } & { p _ { k + 1 } ^ { H } A p _ { j } = r _ { k + 1 } ^ { H } A p _ { j } + \beta _ { k } p _ { k } ^ { H } A p _ { j } = \alpha _ { j } ^ { - 1 } r _ { k + 1 } ^ { H } ( r _ { j } - r _ { j + 1 } ) } \\ & { \qquad = \alpha _ { j } ^ { - 1 } r _ { k + 1 } ^ { H } ( p _ { j } - \beta _ { j - 1 } p _ { j - 1 } - p _ { j + 1 } + \beta _ { j } p _ { j } ) . } \end{array}
$$

By (6.2.7), this is zero for $0 < j < k$ For $j = 0$ we use $b = p _ { 0 }$ in forming the last line of the equation. For $j = k$ we use (6.2.4), which yields (.2.8). Since the vectors $r _ { 0 } , \ldots , r _ { k - 1 }$ and $p _ { 0 } , \ldots , p _ { k - 1 }$ span the same Krylov subspace $\kappa _ { k } ( A , b )$ , the second orthogonality relation in (6.2.7) also holds. □

We now use these orthogonality properties to derive alternative expressions for $\alpha _ { k }$ and $\beta _ { k }$ From (6.2.1), we have $r _ { k } ^ { H } p _ { k } = r _ { k } ^ { H } ( r _ { k } + \beta _ { k - 1 } p _ { k - 1 } ) = r _ { k } ^ { H } r _ { k }$ giving

$$
\alpha _ { k } = \frac { r _ { k } ^ { H } r _ { k } } { p _ { k } ^ { H } A p _ { k } } .
$$

Similarly, $r _ { k + 1 } ^ { H } r _ { k + 1 } = r _ { k + 1 } ^ { H } ( r _ { k } - \alpha _ { k } A p _ { k } ) = - \alpha _ { k } r _ { k + 1 } ^ { H } A p _ { k }$ Now from (.2.6) we get $r _ { k + 1 } ^ { H } A p _ { k }$ $= \beta _ { k } p _ { k } ^ { H } A p _ { k }$ ,and (6.2.9) gives

$$
\beta _ { k } = \frac { r _ { k + 1 } ^ { H } r _ { k + 1 } } { r _ { k } ^ { H } r _ { k } } .
$$

Theorem 6.2.1 and the property $r _ { k } \in \mathcal { K } _ { k } ( A , b )$ imply that in theory the residual vectors $r _ { 0 } , r _ { 1 }$ ， $r _ { 2 } , \ldots .$ are the vectors that would be obtained from the sequence $b , A b , A ^ { 2 } b , \ldots$ by Gram-Schmidt orthogonalization. The vectors $p _ { 0 } , p _ { 1 } , p _ { 2 } , . . .$ may be constructed similarly from the conjugacy relation (6.2.8).

The orthogonality relations (6.2.7) ensure that in exact arithmetic, CG terminates with $r _ { k } = 0$ after at most $n$ steps. Indeed,suppose $r _ { k } \neq 0$ ， $k = 0 : n$ . Then by (6.2.7) these $n + 1$ nonzero vectors in $\mathbb { C } ^ { n }$ are mutually orthogonal and hence linearly independent. Since this is impossible, we have a contradiction.

Theorem 6.2.2. $I n$ CG the vector $x _ { k }$ minimizes the energy norm

$$
E ( x ) = ( x - x ^ { * } ) ^ { H } A ( x - x ^ { * } ) = \| x - x ^ { * } \| _ { A } ^ { 2 }
$$

of the error over all vectors $x \in x _ { 0 } + \mathcal { K } _ { k } ( A , r _ { 0 } )$ ，where $r _ { 0 } = b - A x _ { 0 }$ and $x ^ { * } = A ^ { - 1 } b$ is the exact solution.

We have $x _ { k } = x _ { 0 } + Q _ { k - 1 } ( A ) b$ for some polynomial $Q _ { k - 1 }$ of degree $k - 1$ Substituting $b = A x$ and subtracting $x$ from both sides gives

$$
x - x _ { k } = ( I - Q _ { k - 1 } ( A ) A ) ( x - x _ { 0 } ) = P _ { k } ( A ) ( x - x _ { 0 } ) ,
$$

where $P _ { 0 } ( A ) = 1$ . As long as $r _ { k } \neq 0$ ,the“energy”norm $\| x _ { k } - x ^ { * } \| _ { A }$ is strictly decreasing. It can be shown (Hestenes and Stiefel [608, $\mathrm { 1 9 5 2 }$ ,Theorem 6.3]) that the error norm $\| \boldsymbol { x } _ { k } - \boldsymbol { x } ^ { * } \| _ { 2 }$ is also strictly decreasing. However, the residual norm $\| b - A x _ { k } \| _ { 2 }$ typically oscillates and may increase initially.

CG also works for Hermitian semidefinite consistent systems $A x = b$ ， $b \in { \mathcal { R } } ( A )$ .With $x _ { 0 } = 0$ ,it follows that $x _ { k } \in { \mathcal { R } } ( A )$ ， $k > 0$ .Then CG converges to the unique least-norm solution. A more general result is shown by Kammerer and Nashed [683,1972].

An implementation of CG is given by the following MATLAB function.

# Algorithm 6.2.1 (CG).

function $[ { \bf x } , { \bf r } ] = { \tt c g } ( { \tt A } , { \tt b } , { \tt x 0 } , \tt { m a x i t } )$   
$\%$ CG performs at most maxit CG iterations   
$\%$ on the linear system $\mathtt { A x } ~ = ~ \mathtt { b }$   
$\%$ $\mathrm { ~ \tt ~ x ~ } = \mathrm { ~ \tt ~ x 0 ~ }$ ； $\mathrm { ~  ~ r ~ } = \mathrm { ~  ~ b ~ } - \mathrm { ~  ~ A ~ } + \tt { x } _ { i }$ $\mathrm { ~ \tt ~ p ~ } = \mathrm { ~ \tt ~ r ~ }$ ： $\mathtt { n r m } = \mathtt { r } ^ { \prime } * \mathtt { r }$ ； for $\texttt { k } = \texttt { 1 }$ : maxit if nrm $\ c = ~ 0$ ，break；end; $\mathsf { q } = \mathsf { A } * \mathsf { p }$ ； alpha $\mathbf { \Sigma } = \ \mathrm { n r m } / \left( \mathsf { q } ^ { \prime } \ast \mathsf { p } \right)$ ； $\mathrm {  ~ x ~ } = \mathrm {  ~ x ~ } + \mathrm {  ~ a l p h a * p ~ } ;$ r = r - alpha\*q; $\mathtt { n r m o l d } = \mathtt { n r m }$ ； $\mathrm {  ~ n r m ~ } = \mathrm {  ~ r ~ } ^ { \prime } * \mathrm {  ~ r ~ } _ { \mathrm { { i } } }$ beta $\mathbf { \tau } = \mathrm { \ n r m / n r m o { 1 } d }$ ； $\mathrm { ~ \tt ~ p ~ } = \mathrm { ~ \tt ~ r ~ } + \mathrm { ~ \tt ~ b e t a * p ~ } ;$ end   
end

The computational requirements for each iteration of CG are constant. Each step requires one matrix-vector multiplication with $A$ ,two inner products,and two vector updates of length $n$ Storage is needed for four $n$ -vectors $x , r , p , q$

Originally, the CG method was viewed primarily as a direct method; see Householder [645, 1964,Sect.5.7]. It soon became evident that the finite termination property is valid only in exact arithmetic.In floating-point computation it could take many more than $n$ iterations before convergence occurred. This led to a widespread disregard of the method for more than a decade after its publication. Interest was renewed when Reid [920,1971] showed that it could be highly efficient if used as an iterative method for solving large, sparse, well-conditioned linear systems.

# 6.2.2 - CGLS and Related Methods

A Krylov subspace method CGLS for solving the least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| \boldsymbol { A } \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } , \quad \boldsymbol { A } \in \mathbb { R } ^ { m \times n } ,
$$

is obtained by applying CG to the normal equations $A ^ { T } A x = A ^ { T } b$ .These are Hermitian positive definite or semidefinite.From Theorem 6.2.1 it follows that the residual vectors

$$
s _ { k } = A ^ { T } r _ { k } = A ^ { T } ( b - A x _ { k } )
$$

in CGLS are mutually orthogonal. In exact arithmetic, the CGLS iterations terminate with $s _ { k } = 0$ after at most rank $( A )$ steps.Let $x ^ { \dagger }$ denote the pseudoinverse solution,and let $r ^ { \dagger } = b - A x ^ { \dagger }$ .If $A ^ { T } A$ is positive definite, it follows from Theorem 6.2.2 that $x _ { k }$ minimizes the error norm

$$
E ( \boldsymbol { x } ) = \| \boldsymbol { x } - \boldsymbol { x } ^ { \dag } \| _ { A ^ { T } A } ^ { 2 } = \| A ( \boldsymbol { x } - \boldsymbol { x } ^ { \dag } ) \| _ { 2 } ^ { 2 } = \| \boldsymbol { r } - \boldsymbol { r } ^ { \dag } \| _ { 2 } ^ { 2 }
$$

over the Krylov subspace $x - x _ { 0 } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } r _ { 0 } )$ ， $r _ { 0 } = b - A x _ { 0 }$ .Hence, both $\lVert \boldsymbol { r } ^ { \dagger } - \boldsymbol { r } _ { k } \rVert _ { 2 }$ and $\lVert \boldsymbol { x } ^ { \dagger } - \boldsymbol { x } _ { k } \rVert _ { 2 }$ decrease monotonically. The error functional (6.2.12) can be written

$$
E ( \boldsymbol { x } ) = \| \boldsymbol { r } - \boldsymbol { r } ^ { \dag } \| _ { 2 } ^ { 2 } = \| \boldsymbol { r } \| _ { 2 } ^ { 2 } - \| \boldsymbol { r } ^ { \dag } \| _ { 2 } ^ { 2 } ,
$$

where the last equality follows from the Pythagorean theorem and the identity

$$
r = ( r - r ^ { \dagger } ) + r ^ { \dagger } , \qquad r - r ^ { \dagger } \perp r ^ { \dagger } .
$$

Thus $\| r _ { k } \| _ { 2 }$ also decreases monotonically. However, the residual norm $\| s _ { k } \| _ { 2 } = \| A ^ { T } r _ { k } \| _ { 2 }$ will usually oscillate, especially when $A$ is ill-conditioned.

Consider a straightforward application of CG to the normal equation $A ^ { T } A x \ : = \ : A ^ { T } b$ with $x _ { 0 } = 0$ . The only information about $b$ available is from the initialization $s = A ^ { T } b$ because no more reference to $b$ is made in the iterative phase.Hence the bound on the achievable accuracy will include a term of size

$$
\begin{array} { r } { | \delta x | \leq m \mathbf { u } \kappa ( A ) | A ^ { \dagger } | | b | , } \end{array}
$$

coming from the roundoff error in computing $A ^ { T } b .$ If $| r | \ll | b |$ ,this term is much larger than for perturbations of $A$ and $b$ .For reasons of numerical stability, the following two simple algebraic rearrangements should be performed:

1. Explicit formation of the matrix $A ^ { T } A$ should be avoided.

2.The residual $r = b - A x$ should be recurred instead of the residual $s = A ^ { T } r$ of the normal equations.This is crucial for stability because of the cancellation that occurs in $r$ before multiplication by $A ^ { T }$

The resulting method, here called CGLS,appeared as Algorithm (10:2) in the original paper by Hestenes and Stiefel [608,1952].9

# Algorithm 6.2.2 (CGLS).

function $[ { \bf x } , { \bf r } , { \bf s t s } ] = { \tt c g l s } \left( { \tt A } , { \bf b } , { \bf x } 0 , \mathrm { m a x i t } \right)$   
$\%$ CGLS performs at most maxit CG iterations   
$\%$ for the normal equations $\mathbb { A } ^ { \prime } \mathbb { A } \mathbb { x } \ = \ \mathbb { A } ^ { \prime } \mathbb { b }$ .   
$\%$ --- $\mathrm { ~ \tt ~ x ~ } = \mathrm { ~ \tt ~ x 0 ~ }$ ； $\mathrm { ~  ~ r ~ } = \mathrm { ~  ~ b ~ } - \mathrm { ~  ~ A ~ } + \tt { x } _ { i }$ $\mathrm { ~ \tt ~ s ~ } = \mathrm { ~ \tt ~ A ~ } ^ { \ u , } * \mathrm { r }$ ； $\mathrm { ~ \tt ~ p ~ } = \mathrm { ~ \tt ~ s ~ }$ ； $\mathtt { s t s } ~ = ~ \mathtt { s } ^ { \prime } \ast \mathtt { s }$ ； for $\mathtt { \lambda } \mathtt { k } \mathtt { \lambda } = \mathtt { \lambda } 0$ : maxit if sts $\ c = ~ 0$ ，break；end $\mathsf { q } = \mathsf { A } * \mathsf { p }$ ； alpha $=$ sts/(q'\*q); $\mathrm {  ~ x ~ } = \mathrm {  ~ x ~ } + \mathrm {  ~ a l p h a * p } ;$ r = r - alpha\*q; $\mathrm { ~ \tt ~ s ~ } = \mathrm { ~ \tt ~ A ~ } ^ { \ u , } * \mathrm { r }$ ； stsold $=$ sts； $\mathtt { s t s } ~ = ~ \mathtt { s } ^ { \prime } \ast \mathtt { s }$ ； beta $=$ sts/stsold; $\mathrm { ~ \mathsf ~ { ~ p ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ s ~ } ~ } ^ { + }$ beta\*p; end   
end

Each iteration of CGLS requires two matrix-vector products,one with $A$ and the other with $A ^ { T }$ ,as well as two inner products or vector updates of length $m$ and three of length $n$ Storage is needed for two $m$ -vectors $r , q$ and two $n$ -vectors $x , p$ .(Note that $s$ can share storage with $q$ ）

When $\operatorname { r a n k } ( A ) < n$ the least squares solution is not unique. However, it is easily verified that if $x _ { 0 } \in \mathcal { R } ( A ^ { T } )$ ,e.g., $x _ { 0 } = 0$ ,then in CGLS $x _ { k } \in \mathcal { R } ( A ^ { T } )$ ， $k = 0 , 1 , 2 , \ldots$ Hence, in exact arithmetic, CGLS terminates with the pseudoinverse solution $x ^ { \dag } = A ^ { \dag } b \in { \mathcal { R } } ( A ^ { T } )$ .We conclude that in theory CGLS works for least squares problems of any rank and shape, overdetermined as well as underdetermined. A version of CGLS that solves the regularized normal equations $( A ^ { T } A + \mu ^ { 2 } I ) x = A ^ { T } b$ is given in Section 6.4.2.

For a linear model $A x = b + e$ with positive definite covariance matrix $\sigma ^ { 2 } V \in \mathbb { R } ^ { m \times m }$ ,the generalized normal equations in factored form are $A ^ { T } V ^ { - 1 } ( b - A x ) = 0$ .These can be solved by the following generalized version of CGLS.

# Algorithm 6.2.3 (GCGLS).

function $[ { \bf x } , { \bf r } ] ~ = ~ \mathrm { g c g l s } \left( { \tt A } , { \tt V } , { \tt b } , { \tt x 0 } , \mathrm { m a x i t } \right)$   
$\%$ GCGLS performs at most maxit CG iterations   
$\%$ for the normal equations $\mathbb { A } ^ { \prime } \mathbb { V } \left( \mathbb { b } \ - \ \mathbb { A } \mathbb { x } \right) \ = \ 0$ with   
$\%$ SPD covariance matrix $\mathtt { V }$ .   
%-- $\mathrm { ~ \tt ~ x ~ } = \mathrm { ~ \tt ~ x 0 ~ }$ ； $\mathrm { ~ \bf ~ r ~ } = \mathrm { ~ \bf ~ ( ~ b ~ \mathrm ~ - ~ } \mathrm { ~ \bf ~ A * x ~ } )$ ； $\begin{array} { r } {  { \mathrm { ~  ~ y ~ } } =  { \mathrm { ~  ~ V ~ } } \backslash  { \mathrm { ~  ~ r ~ } } ; \quad  { \mathrm { ~  ~ s ~ } } =  { \mathrm { ~  ~ A ~ } } ^ { \prime } *  { \mathrm { ~  ~ y ~ } } ; \quad  { \mathrm { ~  ~ p ~ } } =  { \mathrm { ~  ~ s ~ } } ; } \end{array}$ sts $\mathbf { \Psi } = \mathbf { \Psi } \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \mathbf { s } ^ { \mathrm { ~ } \dagger } \ast \mathbf { s }$ ； for $\mathtt { \lambda } \mathtt { k } \mathtt { \lambda } = \mathtt { \lambda } 0$ : maxit if sts $\ c = ~ 0$ ，break；end $\begin{array} { r } { \mathrm { ~  ~ q ~ } = \mathrm { ~  ~ A ~ } * \mathrm { ~  ~ p ~ } ; \mathrm { ~  ~ \Delta ~ t ~ } = \mathrm { ~  ~ V ~ } \backslash \mathrm { q } ; } \end{array}$ alpha $=$ sts/(q'\*t); $\mathrm {  ~ x ~ } = \mathrm {  ~ x ~ } + \mathrm {  ~ a l p h a * p ~ } ;$ $\texttt { y } = \texttt { y }$ - alpha\*t;

$\tt { s } = \tt { A } ^ { \prime } * \tt { y } _ { \mathrm { { i } } }$ stsold $=$ sts； $\begin{array} { r } { \{ { \tt S t s } \ = \ { \tt S } ^ { \ 3 } * { \tt S } \ ; } \end{array}$ beta $=$ sts/stsold; p = s + beta\*p; end end

For an underdetermined system $A x = b$ of full row rank, the problem

$$
\operatorname* { m i n } _ { y } \| x \| _ { 2 } ^ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A x = b
$$

has a unique solution that satisfies

$$
A A ^ { T } z = b , \quad x = A ^ { T } z .
$$

By assumption, $A A ^ { T }$ is symmetric positive definite,so CG can be applied to $A A ^ { T } z = b$ With $z _ { 0 } = 0$ this generates approximations

$$
\begin{array} { r } { x _ { k } = A ^ { T } z _ { k } , \quad z _ { k } \in { \mathcal K } _ { k } ( A A ^ { T } , b ) . } \end{array}
$$

Eliminating $z _ { k }$ , we obtain algorithm CGME expressed in terms of $x _ { k }$ . The generated approximations minimize

$$
\| z ^ { \dagger } - z _ { k } \| _ { A ^ { T } A } = \| A ( z ^ { \dagger } - z _ { k } ) \| _ { 2 } = \| y ^ { \dagger } - y _ { k } \| _ { 2 } .
$$

Note that $x _ { k }$ lies in the same Krylov subspace as $x _ { k }$ in CGLS but minimizes a different error norm, namely $\| x _ { k } - x ^ { \dagger } \| _ { 2 }$

By construction, the error norm $\lVert \boldsymbol { x } _ { k } - \boldsymbol { x } ^ { \dagger } \rVert _ { 2 }$ for CGME decreases monotonically, but the residual norm $\| r _ { k } \| _ { 2 }$ can oscillate.Because the stopping criterion for consistent systems is usually based on the size of $\| r _ { k } \| _ { 2 }$ , it may often be preferable to use CGLS also for underdetermined systems.When applied to an inconsistent system $A x = b$ ,CGME may break down; see Choi [244, 2006, Sect. 2.2.1].

# Algorithm 6.2.4 (CGME).

function $[ { \bf x } , { \bf r } ] { \bf \theta } = { \bf \theta }$ cgme(A,b,xO,maxit)   
$\%$ CGME performs at most maxit steps of Craig's   
$\%$ algorithm on a consistent linear system $\mathtt { A x } ~ = ~ \mathtt { b }$ ·   
$\%$ $\mathrm { ~ \tt ~ x ~ } = \mathrm { ~ \tt ~ x 0 ~ }$ ； $\begin{array} { r } { \tt { \tt { r } = b \mathrm { ~ \tt ~ - ~ } \tt { A } * \tt { x } ; } } \end{array}$ nrm = r'\*r; $\mathrm { ~ \tt ~ p ~ } = \mathrm { ~ \tt ~ r ~ }$ ； for $\texttt { k } = \texttt { 1 }$ : maxit if $\mathrm { { n r m } ~ } = = \mathrm { ~ 0 ~ }$ ，break；end $\mathsf { q } = \mathsf { A } ^ { \prime } \ast \mathsf { p }$ ； alpha $\mathbf { \Sigma } = \mathbf { \Sigma } \mathrm { n r m } / ( \mathsf { q } ^ { \prime } \ast \mathsf { q } )$ ； $\mathrm {  ~ x ~ } = \mathrm {  ~ x ~ } + \mathrm {  ~ a l p h a * q } ;$ $\mathrm {  ~ r ~ } = \mathrm {  ~ r ~ } - \mathrm {  ~ a ~ } \mathrm {  ~ \ a ~ } \mathrm {  ~ \ a ~ } + ( \mathrm {  ~ A * q } ) \ ;$ nrmold $=$ nrm； $\mathtt { n r m } = \mathtt { r } ^ { \prime } * \mathtt { r }$ ； beta $=$ nrm/nrmold; $\mathrm { ~ p ~ = ~ r ~ + ~ b e t a * p } ;$ end   
end

For $A \in \mathbb { R } ^ { m \times n }$ , CGME needs storage for two vectors $x$ and $q$ of length $n$ and two vectors $r$ and $p$ of length $m$ .Three inner products or vector updates of length $n$ and two of length $m$ are required per step.

The vector $p$ in CGME can be eliminated. Then the algorithm becomes identical to an al-gorithm due to Craig [277,1955l; see Saad [956,1996,Sect. 8.3.2]. We prefer to keep the algorithm in the form given above,because this makes it possble to include a regularization term; see Section 6.4.2.

In exact arithmetic, CGLS generates the sequence of Krylov_subspace approximations $x _ { k }$ ， $k = 1 , 2 , \ldots$ ,defined in Section 4.2.3 for solving $A ^ { T } A x \stackrel { \cdot } { = } A ^ { T } b$ ．By Theorem 4.2.4,CGLS terminates after at most $r = { \mathrm { r a n k } } ( A )$ steps with the pseudoinverse solution $x ^ { \dagger } = A ^ { \dagger } b$ More precisely, if $A$ has $p$ distinct (possibly multiple) nonzero singular values $\sigma _ { 1 } > \sigma _ { 2 } > \cdots > \sigma _ { p }$ then in exact arithmetic,CGLS terminates after $p$ steps.For example,if $A$ is the unit matrix plus a matrix of rank $p$ ,at most $p { + 1 }$ steps are needed. Even fewer steps are required if $b$ is orthogonal to some of the left singular vectors $u _ { i }$ corresponding to $\sigma _ { i }$ . If the original system is such that the exact solution $\textstyle x = \sum _ { i = 1 } ^ { n } ( c _ { i } / \sigma _ { i } ) v _ { i }$ $c _ { i } = u _ { i } ^ { T } b$ has small projections $c _ { i }$ onto singular vectors $u _ { i }$ ， $i > p$ ,then $p$ steps can be expected to give good approximations. However, the intermediate Krylov subspace approximations $x _ { k }$ depend nonlinearly on $A$ and $b$ in a highly complicated way.

We now derive an upper bound for the number of iterations needed to reduce the residual norm by a certain amount. We assume exact arithmetic,but the bound holds also for finiteprecision computation.The residual of the normal equation can be written

$$
\begin{array} { r } { s _ { k } = \left( I - A ^ { T } A P _ { k - 1 } ( A ^ { T } A ) \right) A ^ { T } r _ { 0 } = R _ { k } ( A ^ { T } A ) A ^ { T } r _ { 0 } , } \end{array}
$$

where $P _ { k - 1 }$ is a polynomial of degree $k - 1$ ,and $\begin{array} { r } { R _ { k } ( \lambda ) = \sum _ { i = 0 } ^ { k } c _ { k i } \lambda ^ { i } } \end{array}$ is a residual polynomial, i.e., $R _ { k } ( 1 ) = 1$ Let $s$ contain all the nonzero singular values $\sigma$ of $A$ ,and assume that for some residual polynomial $\tilde { R } _ { k }$ we have

$$
\operatorname* { m a x } _ { \sigma \in S } | \tilde { R } _ { k } ( \sigma ^ { 2 } ) | \le M _ { k } .
$$

Then from the minimum property (6.2.12) of $x _ { k }$ , it follows that

$$
\| s _ { k } \| _ { ( A ^ { T } A ) ^ { - 1 } } ^ { 2 } = \| r - r _ { k } \| ^ { 2 } \leq M _ { k } ^ { 2 } \sum _ { i = 1 } ^ { n } \gamma _ { i } ^ { 2 } \sigma _ { i } ^ { - 2 } = M _ { k } ^ { 2 } \| s _ { 0 } \| _ { ( A ^ { T } A ) ^ { - 1 } } ^ { 2 } .
$$

We can now select a set $S$ on the basis of some assumption regarding the singular value distribution of $A$ and seek a polynomial $\tilde { R } _ { k } \in \tilde { \Pi } _ { k } ^ { 1 }$ such that $\bar { M } _ { k } = \operatorname* { m a x } _ { \sigma \in S } \bar { | } \tilde { R } _ { k } ( \sigma ^ { 2 } ) \bar { | }$ is small. A simple choice is to take $S$ to be the interval $[ \sigma _ { n } ^ { 2 } , \sigma _ { 1 } ^ { 2 } ]$ and seek the polynomial $\tilde { R } _ { k } \in \tilde { \Pi } _ { k } ^ { 1 }$ that minimizes

$$
\operatorname* { m a x } _ { \sigma _ { n } ^ { 2 } \leq \sigma ^ { 2 } \leq \sigma _ { 1 } ^ { 2 } } | R _ { k } ( \sigma ^ { 2 } ) | .
$$

The solution to this problem is the shifted Chebyshev polynomials introduced in the analysis of the CSI method in Section 6.1.6. This gives the following upper bound for the norm of the residual error after $k$ steps:

$$
\| r - r _ { k } \| _ { 2 } \leq 2 { \bigg ( } { \frac { \kappa ( A ) - 1 } { \kappa ( A ) + 1 } } { \bigg ) } ^ { k } \| r - r _ { 0 } \| _ { 2 } , \quad k = 0 , 1 , 2 , \ldots .
$$

It follws that an upper bound on the number of iterations $k$ needed to reduce the relative error by a factor $\epsilon$ is

$$
\frac { \| r - r _ { k } \| _ { 2 } } { \| r - r _ { 0 } \| _ { 2 } } < \epsilon \iff k < \frac { 1 } { 2 } \kappa ( A ) \log \frac { 2 } { \epsilon } .
$$

This is the same as for the CSI method and the second-order Richardson method. However,these methods require that accurate lower and upper bounds for the singular values of $A$ be known. Furthermore,the estimate (6.2.19) tends to be sharp asymptotically for CSI, while for CGLS the error usually decreases much faster. On the other hand,the inner products in CGLS can be a bottleneck when implemented on parallel computers.

Although useful in the analysis of many model problems,the bound(6.2.18) in terms of $\kappa ( A )$ cannot be expected to describe the highly nonlinear complexity of the convergence behavior of CGLS. The convergence depends on the distribution of all singular values of $A$ ,as well as on the projection of the right-hand side $b$ onto the left singular vectors of $A$ . In practice the rate of convergence often accelerates as the number of steps increases.

In floating-point arithmetic the finite termination property no longer holds,and it can take much more than $n$ steps before the desired final accuracy is reached; see Section 6.2.6.

# Notes and references

The theory of the CG method was published in the seminal paper by Hestenes and Stiefel [608, 1952].The story of its development is recounted by Hestenes [6O7,199o]. One of the first applications of CGLS to a least squares problem was for solving geodetic network problems; see Stiefel [1035,1952]. The early history of Krylov subspace methods is documented by Golub and O'Leary [502,198g]. Early discussions of CG methods for least squares problems are given by Lawson [726,1973l and Chen [242,1975l. A more recent survey of Krylov subspace methods is given by van der Vorst [1O75,2oo3]. Modern treatments of the Lanczos and CG methods are found in Greenbaum [534,1997], Meurant [791,20o6], Meurant and Strakos [792, 20o6]),and Liesen and Strakos [746, 2012].

# 6.2.3 - Preconditioned Iterative Methods

The rate of convergence of iterative least squares methods can be very slow, and the use of a preconditioner to accelerate convergence is often essential. For a linear system $A x = b$ ,let $A = B - E$ be a splitting such that $B$ is nonsingular and $\| E \|$ is small. Then the linear systems

$$
\begin{array} { l l } { { B ^ { - 1 } A x = ( I - B ^ { - 1 } E ) x = c , } } & { { B c = b , } } \\ { { } } & { { } } \\ { { A B ^ { - 1 } y = ( I - E B ^ { - 1 } ) B x = b , \quad B x = y , } } & { { } } \end{array}
$$

are the left- and right-preconditioned systems. If $B$ is chosen so that $B ^ { - 1 } A$ or $A B ^ { - 1 }$ is better conditioned than $A$ ,faster convergence may be expected when the iterative method is applied to one of the preconditioned systems. Note that the products $B ^ { - 1 } A$ and $A B ^ { - 1 }$ need not be formed explicitly, since iterative methods only require that matrix-vector products such as $B ^ { - 1 } ( A x )$ and $A ( B ^ { - 1 } y )$ can be formed for arbitrary $x$ and $y$ ．This is possible if linear systems with $B$ can be solved. Preconditioned iterative methods may be viewed as a compromise between a direct and an iterative solver. To be effcient, a preconditioner should have the following, partly contradictory properties:

· The norm of the defect matrix $E$ should be small, and $A B ^ { - 1 } \left( B ^ { - 1 } A \right)$ should be better conditioned than $A$ and have well clustered eigenvalues.   
· Linear systems with matrices $B$ and $B ^ { T }$ should be cheap to solve, and $B$ should not have many more nonzero elements than $A$

For solving a least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ the right-preconditioned problem

$$
\operatorname* { m i n } _ { y } \| A B ^ { - 1 } y - b \| _ { 2 } , \quad y = B x ,
$$

should be used,because a left-preconditioner would change the objective function. This is equivalent to a symmetric preconditioning of the normal equations:

$$
B ^ { - T } A ^ { T } A B ^ { - 1 } y = B ^ { - T } A ^ { T } b , \quad x = B ^ { - 1 } y .
$$

For the preconditioned CGLS (PCGLS） method the approximations minimize the error functional $\| r _ { k } \| _ { 2 } ^ { 2 }$ ， $r _ { k } = b - A x _ { k }$ , over the Krylov subspace

$$
x _ { k } - x _ { 0 } \in \mathcal { K } _ { k } ( B ^ { - T } A ^ { T } A B ^ { - 1 } , B ^ { - T } A ^ { T } r _ { 0 } ) .
$$

For PCGLS, the required matrix-vector product $u = A B ^ { - 1 } y$ is computed by solving $B w = y$ and forming $u = A w$ Similarly, $v = B ^ { - T } A ^ { T } z$ is computed by solving $B ^ { T } v = A ^ { T } z$ Hence, the extra work is one solve with $B$ and one with $B ^ { T }$ . Below we give an implementation of preconditioned CGLS (PCGLS).

# Algorithm 6.2.5 (PCGLS).

function $[ { \bf x } , { \bf r } , { \bf s } ] = \mathrm { p c g } 1 { \bf s } \left( { \tt A } , { \bf b } , { \tt B } , \mathrm { m a x i t } \right)$   
$\%$ Solves consistent system $\mathtt { A x } ~ = ~ \mathtt { b }$   
$\%$ with left preconditioner B.   
$\%$ --- $\begin{array} { r l } & { \mathbf { x _ { \lambda } } = \mathbf { \lambda } _ { 0 } ; ~ \mathbf { r _ { \lambda } } = \mathbf { \lambda } _ { \mathbf { b } } ; } \\ & { \mathbf { s _ { \lambda } } = \mathbf { \lambda } _ { \mathbf { B } } \mathbf { \Omega } \backslash \left( \mathbf { A } ^ { \prime } \ast \mathbf { r } \right) ; } \\ & { \mathbf { p _ { \lambda } } = \mathbf { \lambda } _ { \mathbf { s } } ; ~ \mathbf { s t s _ { \lambda } } = \mathbf { \lambda } _ { \mathbf { s } } \mathbf { \Omega } \mathbf { \ast } _ { \mathbf { s } } ; } \end{array}$ for $\mathtt { \lambda } \mathtt { k } \mathtt { \lambda } = \mathtt { \lambda } 0$ :maxit ${ \sf t } = { \sf B } \backslash { \sf p } ; \mathrm { ~  ~ { ~ \sf ~ q ~ } ~ } = { \sf ~ A } * { \sf t } ;$ $\mathsf { a l p h a \ = \ p t s / ( q ^ { \prime } * q ) }$ ； $\mathrm { \textbf { x } = \mathrm { \textbf { x } + \ a l p h a * t { ; } } }$ r = r - alpha\*q; S = B"\(A'\*r); stsold $=$ sts； $\mathtt { s t s } ~ = ~ \mathtt { s } ^ { \prime } \ast \mathtt { s }$ ； beta $=$ sts/stsold; $\mathrm { ~  ~ p ~ } = \mathrm { ~ \bf ~ s ~ } + \mathrm { ~ \bf ~ b e t a * p ~ } ;$ end   
end

A simple preconditioner for the normal equations is the diagonal matrix $B \ = \ \mathrm { d i a g } \left( d _ { 1 } \quad \right.$ ， $\ldots , d _ { m } )$ ，where $d _ { j } = \| a _ { j } \| _ { 2 }$ . Then the columns of the preconditioned matrix $A B ^ { - 1 }$ will have unit length. By Theorem 2.1.2 this preconditioner approximately minimizes $\kappa _ { 2 } ( A D ^ { - 1 } )$ over all diagonal $D > 0$ . Using this preconditioner can significantly improve the convergence rate with almost no cost in terms of time and memory. The column norms can be obtained cheaply if $A$ is a sparse matrix (stored columnwise or rowwise). For CGLS the iterations are usually terminated when $\| A ^ { T } r _ { k } \| _ { 2 } / ( \| A \| _ { 2 } \| r _ { k } \| _ { 2 } ) \le \eta$ ，where $\eta$ is a small tolerance (see stopping criteria (6.2.59) and (6.2.6O). This guarantees a backward stable solution. In PCGLS, $\| r _ { k } \| _ { 2 }$ and $\| A B ^ { - 1 } \|$ can be estimated, but usually not $\| A \| _ { 2 }$ . Instead, we use the stopping criterion

$$
\frac { \| ( A B ^ { - 1 } ) ^ { T } r _ { k } \| _ { 2 } } { \| A B ^ { - 1 } \| _ { 2 } \| r _ { k } \| _ { 2 } } \leq \eta .
$$

To solve a consistent underdetermined problem $\operatorname* { m i n } _ { x } \| x \| _ { 2 }$ subject to $A x = b$ , we can apply CGME (Craig's method) to the left-preconditioned problem

$$
\operatorname* { m i n } _ { x } \| x \| _ { 2 } { \mathrm { ~ } } { \mathrm { s u b j e c t ~ t o ~ } } B ^ { - 1 } A x = B ^ { - 1 } b .
$$

This iteration method minimizes the rror functional $\lVert x - x _ { k } \rVert _ { 2 }$ over the Krylov subspaces

$$
x - x _ { k } \in { \mathcal { K } } _ { k } \big ( A ^ { T } ( B B ^ { T } ) ^ { - 1 } A , A ^ { T } ( B B ^ { T } ) ^ { - 1 } b \big ) .
$$

Note that although the residual vectors are transformed,the algorithm can be formulated in terms of the original residuals $r _ { k } = b - A x _ { k }$

# Algorithm 6.2.6 (PCGME).

function $\ [ { \bf x } , { \bf r } ] ~ = ~ \mathrm { p c g m e } \left( { \tt A } , { \tt B } , { \tt b } , \mathrm { m a x i t } \right)$   
$\%$ Solves consistent system $\mathtt { A x } ~ = ~ \mathtt { b }$   
$\%$ with left preconditioner B.   
$\%$ - $\texttt { x } = \texttt { 0 }$ ； $\texttt { r } = \texttt { b }$ ； $\begin{array} { l } { \mathrm { { n r m ~ = ~ \overset { \cdot } { \mathtt { r } } ^ { \mathtt { \prime } } * r ; ~ \overset { \cdot } { \mathtt { z } } ~ = ~ B \backslash r ; } } } \\ { \mathrm { ~ \overset { \mathtt { q } } { \mathtt { q } } ~ = ~ \overset { \cdot } { A } ^ { \mathtt { \prime } } * ( B ^ { \mathtt { \prime } } \backslash z ) ; } } \end{array}$ for $\texttt { k } = \texttt { 1 }$ : maxit $\begin{array} { l } { { \mathrm { a 1 p h a ~ = ~ n r m / \left( q ^ { \prime } * q \right) ~ ; } } } \\ { { \mathrm { ~ x ~ = ~ x ~ + ~ a 1 p h a * q ; } } } \\ { { \mathrm { ~ r ~ = ~ r ~ - ~ a 1 p h a * ( A * q ) ~ ; } } } \\ { { \mathrm { ~ z ~ = ~ B \backslash { r } ~ ; } } } \\ { { \mathrm { n r m o l d ~ = ~ n r m ; ~ n r m ~ = ~ z ^ { \prime } * z ; } } } \\ { { \mathrm { b e t a ~ = ~ n r m / n r m o l d ; } } } \\ { { \mathrm { ~ q ~ = ~ A ^ { \prime } * ( B ^ { \prime } \backslash z ) ~ + ~ b e t a * p ; } } } \end{array}$ end   
end

Preconditioners for least squares problems are treated in Section 6.3. Benzi [1O6,2002] gives an excellent survey of preconditioning techniques for the iterative solution of large linear systems,with a focus on algebraic methods for general sparse matrices.Wathen [1O95,2o15] and Pearson and Pestana [888, 2o2o] survey a range of preconditioners for use with partial differential equations and optimization problems and for other purposes as well.

# 6.2.4 - The Lanczos Process

Lanczos [715,195o] developed a method for computing selected eigenvalues and eigenvectors of a Hermitian matrix $A \in \mathbb { C } ^ { n \times n }$ . The method is based on the Lanczos process, a recursive algorithm for reducing a Hermitian matrix $A \in \mathbb { C } ^ { n \times n }$ to tridiagonal form by a unitary similarity,

$$
U _ { n } ^ { H } A U _ { n } = T _ { n } = \left( \begin{array} { r r r r r } { \alpha _ { 1 } } & { \beta _ { 2 } } & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & { \beta _ { 3 } } & & \\ & { \beta _ { 3 } } & { \ddots } & { \ddots } & \\ & & { \ddots } & { \alpha _ { n - 1 } } & { \beta _ { n } } \\ & & & { \beta _ { n } } & { \alpha _ { n } } \end{array} \right) \in \mathbb { R } ^ { n \times n } ,
$$

where $U _ { n } = ( u _ { 1 } , u _ { 2 } , . . . , u _ { n } )$ . (Note that $\alpha _ { k }$ and $\beta _ { k }$ are not the same as in the CG method.) Taking $\beta _ { 1 } = \beta _ { n + 1 } = 0$ and equating columns in $A U _ { n } = U _ { n } T _ { n }$ gives

$$
A u _ { k } = \beta _ { k } u _ { k - 1 } + \alpha _ { k } u _ { k } + \beta _ { k + 1 } u _ { k + 1 } , \quad k = 1 : n .
$$

The requirement that $u _ { k } \perp u _ { k - 1 }$ and $u _ { k + 1 } \perp u _ { k }$ yields $\alpha _ { 1 } = u _ { 1 } ^ { H } A u _ { 1 }$ and

$$
\alpha _ { k } = u _ { k } ^ { H } v _ { k } , \quad v _ { k } = A u _ { k } - \beta _ { k } u _ { k - 1 } , \quad k = 2 , \ldots , n .
$$

Solving (6.2.28) for $u _ { k + 1 }$ gives $\beta _ { k + 1 } u _ { k + 1 } = r _ { k }$ and $r _ { k } = v _ { k } - \alpha _ { k } u _ { k }$ If $r _ { k } = 0$ , the process stops. Otherwise,

$$
\beta _ { k + 1 } = \| r _ { k } \| _ { 2 } , \qquad u _ { k + 1 } = r _ { k } / \beta _ { k + 1 } .
$$

Thus,as long as all $\beta _ { k } \neq 0$ ,the elements in the tridiagonal matrix $T _ { k }$ and the unitary matrix $U _ { k + 1 } \in { \mathcal { K } } _ { k + 1 } ( A , u _ { 1 } )$ are uniquely determined. Furthermore, it holds that

$$
A U _ { k } = U _ { k } T _ { k } + \beta _ { k + 1 } u _ { k + 1 } e _ { k } ^ { T } = U _ { k + 1 } { \hat { T } } _ { k } , \qquad { \hat { T } } _ { k } = \left( { \begin{array} { c } { T _ { k } } \\ { \beta _ { k + 1 } e _ { 1 } ^ { T } } \end{array} } \right) ,
$$

which is the Lanczos decomposition. It is easy to verify that $U _ { k }$ is an orthonormal basis in the Krylov subspace $\textstyle { \mathcal { K } } _ { k } ( A , b )$

The Lanczos process requires storage for $T _ { k }$ and three $n$ -vectors $u _ { k - 1 }$ ， $u _ { k }$ ,and $u _ { k + 1 }$ .The eigenvalues of $T _ { k }$ are approximations to the eigenvalues of $A$ . The process stops when $\beta _ { k + 1 } = 0$ Then by (6.2.31), $A U _ { k } = U _ { k } T _ { k }$ ,i.e., $U _ { k }$ is an invariant subspace of $A$

Lanczos [716,1952] noted that his process can be used to solve positive definite systems of linear equations by a method he called the method of minimized iterations.With

$$
\beta _ { 1 } = \| b \| _ { 2 } , \qquad u _ { 1 } = b / \beta _ { 1 } ,
$$

an approximate solution $x _ { k } = U _ { k } y _ { k } \in \mathcal { K } _ { k } ( A , b )$ is determined by the Galerkin condition

$$
\begin{array} { r } { U _ { k } ^ { H } r _ { k } = 0 , \quad r _ { k } = b - A x _ { k } . } \end{array}
$$

The Lanczos decomposition (6.2.31) gives

$$
r _ { k } = \beta _ { 1 } u _ { 1 } - A U _ { k } y _ { k } = U _ { k + 1 } ( \beta _ { 1 } e _ { 1 } - \hat { T } _ { k } y _ { k } ) .
$$

If $y _ { k }$ is determined from $T _ { k } y _ { k } = \beta _ { 1 } e _ { 1 }$ , it follows that $r _ { k } = - ( e _ { k } ^ { T } y _ { k } ) \beta _ { k + 1 } u _ { k + 1 }$ and Uk+1Tk=0 as required. Because $A$ is positive definite, so is $T _ { k }$ .Hence the Cholesky factorization $T _ { k } =$ $L _ { k } L _ { k } ^ { T }$ exists, with

$$
L _ { k } = \left( \begin{array} { c c c c c c } { { l _ { 1 1 } } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { l _ { 2 1 } } } & { { l _ { 2 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { l _ { 3 2 } } } & { { l _ { 3 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { l _ { k , k - 1 } } } & { { l _ { k k } } } \end{array} \right) .
$$

Because $L _ { k }$ is the $k \times k$ principal submatrix of $L _ { k + 1 }$ , the Cholesky factorization can be cheaply updated. The equation $T _ { k } y _ { k } = \beta _ { 1 } e _ { 1 }$ is equivalent to the bidiagonal equations

$$
L _ { k } z _ { k } = \beta _ { 1 } e , ~ L _ { k } ^ { T } y _ { k } = z _ { k } .
$$

It follows that

$$
z _ { k } = \left( \begin{array} { c } { { z _ { k - 1 } } } \\ { { \xi _ { k } } } \end{array} \right) , \quad \xi _ { k } = - l _ { k , k - 1 } \xi _ { k - 1 } / l _ { k k } .
$$

If we define $P _ { k }$ from $L _ { k } P _ { k } ^ { T } = U _ { k } ^ { T }$ ,then

$$
x _ { k } = U _ { k } y _ { k } = P _ { k } L _ { k } ^ { T } y _ { k } = P _ { k } z _ { k } ,
$$

and $l _ { k - 1 , k } p _ { k - 1 } + l _ { k k } p _ { k } = u _ { k }$ .Hence,

$$
x _ { k } = x _ { k - 1 } + \zeta _ { k } p _ { k } , \qquad p _ { k } = ( u _ { k } - l _ { k , k - 1 } p _ { k - 1 } ) / l _ { k k }
$$

can be obtained without saving all the vectors $u _ { 1 } , \ldots , u _ { k }$ or computing $y _ { k }$

In exact arithmetic, this method computes the same sequence of approximations $x _ { k } \in { \mathsf { \Gamma } }$ $\textstyle { \mathcal { K } } _ { k } ( A , b )$ as CG and is therefore often called the Lanczos-CG method. The residual vectors $r _ { 0 } , \ldots , r _ { k - 1 }$ in CG are mutually orthogonal and form a basis for the Krylov space $\textstyle { \mathcal { K } } _ { k } ( A , b )$ Hence by uniqueness, the columns of $U _ { k }$ in the Lanczos process equal the residual vectors normalized to unit length.

# Notes and references

The Lanczos process is closely connected to the theory of orthogonal polynomials,Gauss-Christofel quadrature,and the Stieltjes moment problem; see Golub and Meurant [501,1994] and Liesen and Strakos [746, 2012]. Let $\mathcal { P } _ { n - 1 }$ be the space of polynomials of degree at most $n - 1$ ,equipped with the inner product

$$
\langle p , q \rangle _ { u _ { 1 } } = ( p ( A ) u _ { 1 } ) ^ { H } q ( A ) u _ { 1 } .
$$

Then the Lanczos process is just the Stieltjes algorithm for computing the corresponding sequence of orthogonal polynomials. The vectors $u _ { k }$ are of the form $q _ { k - 1 } ( A ) u _ { 1 }$ ,and the orthogonality of these vectors translates into the orthogonality of the polynomials with respect to the inner product (6.2.33).

# 6.2.5 - LSQR and Related Algorithms

The LSQR algorithm of Paige and Saunders [866,1982] is a Lanczos-type algorithm for solving least squares problems. LSQR uses the Bidiag1 variant of GKL bidiagonalization; see Section 4.2.3. Starting from

$$
\beta _ { 1 } u _ { 1 } = b , \qquad \alpha _ { 1 } v _ { 1 } = A ^ { T } u _ { 1 } ,
$$

Bidiagl generates two orthonormal sequences of unit vectors $u _ { 1 } , u _ { 2 } , \ldots$ in $\mathbb { R } ^ { m }$ and $v _ { 1 } , v _ { 2 } , \ldots$ in $\mathbb { R } ^ { n }$ ，

$$
\begin{array} { r l } & { \beta _ { k + 1 } u _ { k + 1 } = A v _ { k } - \alpha _ { k } u _ { k } , } \\ & { \alpha _ { k + 1 } v _ { k + 1 } = A ^ { T } u _ { k + 1 } - \beta _ { k + 1 } u _ { k } , \quad k = 1 , 2 , \ldots , } \end{array}
$$

where the scalars $\alpha _ { k }$ and $\beta _ { k }$ are normalization constants. The recurrences can be summarized as

$$
A V _ { k } = U _ { k + 1 } B _ { k } , \qquad A ^ { T } U _ { k + 1 } = V _ { k } B _ { k } ^ { T } + \alpha _ { k + 1 } v _ { k + 1 } e _ { k + 1 } ^ { T } ,
$$

where $V _ { k } = ( v _ { 1 } , \ldots , v _ { k } )$ ， $U _ { k + 1 } = ( u _ { 1 } , \dots , u _ { k + 1 } )$ , and

$$
B _ { k } = \left( \begin{array} { l l l l l } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \beta _ { 3 } } & { \ddots } & & \\ & & { \ddots } & & \\ & & & { \beta _ { k + 1 } } \end{array} \right) \in \mathbb { R } ^ { ( k + 1 ) \times k }
$$

is lower bidiagonal. The columns of $U _ { k }$ and $V _ { k }$ are orthonormal bases for the Krylov subspaces

$$
{ \mathcal K } _ { k } ( A A ^ { T } , b ) \quad \mathrm { a n d } \quad { \mathcal K } _ { k } ( A ^ { T } A , A ^ { T } b ) , \quad k = 1 , 2 , \ldots .
$$

Approximations $x _ { k } = V _ { k } y _ { k } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ are obtained as follows. By construction, $b =$ $\beta _ { 1 } u _ { 1 } = \beta _ { 1 } U _ { k + 1 } e _ { 1 }$ . With $x _ { k } = V _ { k } y _ { k }$ and using (6.2.36) we get

$$
r _ { k } = \beta _ { 1 } u _ { 1 } - A V _ { k } y _ { k } = U _ { k + 1 } t _ { k + 1 } , \quad t _ { k + 1 } = \beta _ { 1 } e _ { 1 } - B _ { k } y _ { k } .
$$

From the orthogonality of $U _ { k + 1 }$ and $V _ { k }$ it follows that $\| r _ { k } \| _ { 2 } = \| t _ { k + 1 } \| _ { 2 }$ is minimized over all $x _ { k } \in \operatorname { s p a n } ( V _ { k } )$ if $y _ { k }$ solves the bidiagonal least squares subproblem

$$
\operatorname* { m i n } _ { y _ { k } } \| B _ { k } y _ { k } - \beta _ { 1 } e _ { 1 } \| _ { 2 } .
$$

The special form of the right-hand side $\beta _ { 1 } e _ { 1 }$ holds because the starting vector was taken as $b$ .By uniqueness, it follows that in exact arithmetic, this generates the same Krylov subspace approximations $x _ { k } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ as CGLS.

Subproblem (6.2.39) can be solved by the QR factorization

$$
Q _ { k } ( B _ { k } \ \beta _ { 1 } e _ { 1 } ) = \left( \begin{array} { c c } { { R _ { k } } } & { { f _ { k } } } \\ { { 0 } } & { { \bar { \phi } _ { k + 1 } } } \end{array} \right) ,
$$

where

$$
R _ { k } = \left( \begin{array} { c c c c c c } { { \rho _ { 1 } } } & { { \gamma _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \rho _ { 2 } } } & { { \gamma _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \rho _ { k - 1 } } } & { { \gamma _ { k } } } \\ { { } } & { { } } & { { } } & { { } } & { { \rho _ { k } } } \end{array} \right) , \qquad f _ { k } = \left( \begin{array} { c } { { \phi _ { 1 } } } \\ { { \phi _ { 2 } } } \\ { { \vdots } } \\ { { \phi _ { k - 1 } } } \\ { { \phi _ { k } } } \end{array} \right) .
$$

The matrix $Q _ { k } = G _ { k , k + 1 } G _ { k - 1 , k } \cdot \cdot \cdot G _ { 1 2 }$ is a product of plane rotations chosen to eliminate the subdiagonal elements $\beta _ { 2 } , \ldots , \beta _ { k + 1 }$ of $B _ { k }$ . The solution $y _ { k }$ satisfies

$$
R _ { k } y _ { k } = f _ { k } .
$$

In exact arithmetic, the LSQR approximations $x _ { k } = V _ { k } y _ { k }$ are the same as for CGLS.

The factorization (6.2.4O) can be computed by a recurrence relation. Assume that we have computed the QR factorization of $B _ { k - 1 }$ , so that

$$
\begin{array} { r } { \left( \begin{array} { c c c } { Q _ { k - 1 } } & \\ & { 1 } \end{array} \right) \left( \begin{array} { c c c } { 0 } & { \beta _ { 1 } e _ { 1 } } \\ { \alpha _ { k } } & { 0 } \\ { \beta _ { k + 1 } } & { 0 } \end{array} \right) = \left( \begin{array} { c c c } { \gamma _ { k } e _ { k - 1 } } & { f _ { k - 1 } } \\ { \bar { \rho } _ { k } } & { \bar { \phi } _ { k } } \\ { \beta _ { k + 1 } } & { 0 } \end{array} \right) . } \end{array}
$$

To eliminate $\beta _ { k + 1 }$ in the $k$ th column of $B _ { k }$ , a plane rotation $G _ { k , k + 1 }$ is determined:

$$
G _ { k , k + 1 } \left( \begin{array} { c c } { \bar { \rho } _ { k } } & { \bar { \phi } _ { k } } \\ { \beta _ { k + 1 } } & { 0 } \end{array} \right) = \left( \begin{array} { c c } { \rho _ { k } } & { \phi _ { k } } \\ { 0 } & { \bar { \phi } _ { k + 1 } } \end{array} \right) .
$$

(Note that the previous rotations $G _ { k - 2 , k - 1 } , \ldots , G _ { 1 2 }$ do not act on the $k$ th column.)

If $x _ { k }$ were formed as $x _ { k } = V _ { k } y _ { k }$ , it would be necessary to save (or recompute) the vectors $v _ { 1 } , \ldots , v _ { k }$ . This can be avoided by defining $Z _ { k }$ from the triangular system $Z _ { k } R _ { k } = V _ { k }$ ,so that

$$
x _ { k } = Z _ { k } R _ { k } y _ { k } \equiv Z _ { k } f _ { k } .
$$

The columns of $Z _ { k } = ( z _ { 1 } , \ldots , z _ { k } )$ can be found successively by identifying columns in $Z _ { k } R _ { k } =$ $V _ { k }$ with $R _ { k }$ as in (6.2.41). This yields

$$
v _ { 1 } = \rho _ { 1 } z _ { 1 } , \quad v _ { k } = \gamma _ { k } z _ { k - 1 } + \rho _ { k } z _ { k } , \quad k > 1 .
$$

If $\rho _ { k } \neq 0$ , we obtain the recursion $z _ { 0 } = 0 , x _ { 0 } = 0$

$$
z _ { k } = \frac { 1 } { \rho _ { k } } \big ( v _ { k } - \gamma _ { k } z _ { k - 1 } \big ) , \qquad x _ { k } = x _ { k - 1 } + \phi _ { k } z _ { k } .
$$

Only one extra $n$ -vector needs to be stored. Some work can be saved by using the vectors $w _ { k } \equiv \rho _ { k } z _ { k }$ instead of $z _ { k }$ . A basic MATLAB implementation of the LSQR is given below. Note that all quantities needed to update the approximation $x _ { k - 1 }$ are computed by forward recurrence relations,where only the last term needs to be saved.

For use in stopping criteria, LSQR computes the estimates

$$
\| r _ { k } \| _ { 2 } = { \bar { \phi } } _ { k + 1 } = \beta _ { 1 } s _ { k } s _ { k - 1 } \cdot \cdot \cdot s _ { 1 } , \qquad \| A ^ { T } r _ { k } \| _ { 2 } = { \bar { \phi } } _ { k + 1 } \alpha _ { k + 1 } | c _ { k } | .
$$

These are obtained essentially for free.An estimate of $\| x _ { k } \| _ { 2 }$ can be obtained from a QR factorization of $R _ { k } ^ { T }$ ; see Paige and Saunders [866, $\mathbf { 1 9 } 8 2$ , Section 5.2].

# Algorithm 6.2.7 (LSQR).

fur $\begin{array} { r l } & { \mathrm { ~ \gamma _ \mathrm { { l } \in \dot { ~ i } o n ~ \Gamma _ \mathrm { { l } \bullet , n \Upsilon _ \mathrm { { l } \bullet } } ~ } } ] \mathrm { ~ = ~ \gamma _ \mathrm { l s q r } ( \mathbb { A } , \mathtt { b } , \mathtt { k } ) ~ } } \\ & { \mathrm { ~ \gamma _ \mathrm { { / _ \sigma _ \mathrm { { l } \bullet ~ L S Q R ~ \xi _ \mathrm { f } \circ r _ \sigma _ \mathrm { { - } \bullet } } } ~ } } \mathrm { ~ s o l ~ \gamma _ \mathrm { { l } \bullet ~ L \bullet ~ \lambda = ~ \ b ~ \ o r ~ \ m i n ~ | ~ | ~ \mathbb { A } \mathbb { X } ~ - ~ \mathtt { b } | ~ } } \mid \mathrm { ~ \dotsc ~ } } \\ & { \mathrm { ~ \gamma _ \mathrm { { / _ \sigma _ \mathrm { { \ell } \mathrm { - } ~ -- } ~ } } } \mathrm { ~ , ~ \ } } \\ & { \mathrm { ~ \gamma _ \mathrm { { [ m , n ] } ~ } ~ } = \mathrm { ~ \mathtt { s i } ~ z e ~ ( \mathbb { A } ) ~ } ; \quad \mathrm { ~ \mathbb { X } ~ = ~ \ z e r o s ~ ( n , \mathtt { 1 } ) ~ } ; } \\ & { \mathrm { ~ \gamma _ \mathrm { { b e t a } ~ } = ~ \mathrm { \ n o r m ( b ) ~ } } ; \quad \mathrm { ~ \mathbb { u } ~ = ~ \left( 1 / b \mathtt { e t a } \right) * b ; } } \\ & { \mathrm { ~ \gamma _ \mathrm { ~ { \sigma _ \mathrm { { ~ L } \bullet } ~ } } } \mathrm { ~ a l ~ } ; \quad \mathrm { ~ a l p h a ~ = ~ \mathrm { n o r m ( v ) } ~ } ; } \\ & { \mathrm { ~ v ~ = ~ \left( 1 / a \mathtt { l p h a } \right) * v ; ~ } \quad \mathrm { ~ w ~ = ~ v ~ } \mathrm { , ~ } } \end{array}$ rhobar $=$ alpha； phibar $=$ beta;  
for ${ \\mathrm { ~ i ~ } } = { \mathrm { ~ 1 } } \colon { \mathtt { k } }$   
$\%$ Continue bidiagonalization  
$\mathrm {  ~ u ~ } = \mathrm {  ~ A * v ~ } - \mathrm {  ~ a l p h a * u }$   
$\begin{array} { l r c l } { { \mathrm { \bf ~ u ~ - \Gamma _ { \mathrm { { A } } } \times v ~ \mathrm { { \bf ~ - \Gamma _ { \mathrm { { a } } } \bot p ~ \mathrm { { \bf ~ u } } \otimes \pi _ { \mathrm { { i } } } \pi _ { \mathrm { { \bf ~ u } } } ~ } } } } } \\ { { \mathrm { \bf ~ b e t a ~ = ~ \ n o r m \left( u \right) ~ ; ~ \mathrm {  ~ u ~ = ~ \Gamma _ { \mathrm { { ( 1 / b e t a ) } } } \ast u ~ ; ~ \pi _ { \mathrm { { i } } } ~ } } } } \\  { \mathrm {  ~ v ~ \mathrm { { \bf ~ - \Gamma _ { \mathrm { { A } } } } \mathrm { { \bf ~ \cdot \ n u ~ - \hbar \ b e t a \ast v ; } ~ \pi _ { \mathrm { { \bullet } } } ~ } } } } \\   \mathrm  \bf ~ a \mathrm { { 1 } } \mathrm   p h a ~ = ~ \ n o r m \left( v \right) ~ ; ~ \mathrm   ~ v ~ \mathrm   \bf ~ \Lambda ~ = ~ \Gamma _ { \mathrm { { ( 1 / a } \mathrm { 1 } \ p h a ) } } \ast v ; ~ \pi _ { \mathrm { { a } } } \Lambda _ { \mathrm { { r } } } \mathrm  { \bf ~ ; \Lambda \Lambda } _ { \mathrm { { r } } } \mathrm   \bf ~ \Lambda _ { \mathrm { { a } } } \Lambda _ { \mathrm { { r } } } \mathrm   \bf  \Lambda _ { \mathrm { { i } } } \Lambda _  \mathrm { \tilde { { r } } } \mathrm  { \bf { a } } \Lambda _  \mathrm { { r } } \mathrm   \bf { \Lambda } _ { \tilde { \Lambda } } \mathrm   \bf { \Lambda } _ { \tilde { \Lambda } } \mathrm { { \bf { u } } } \Lambda _  \mathrm { \tilde { \Lambda } } \mathrm  { \bf { \Lambda } _ { r } } \mathrm  { \bf { a } } \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm  \Lambda _ { \tilde { \Lambda } } \mathrm   \end{array}$   
% Construct and apply i:th plane rotationrho $=$ norm([rhobar,beta]）;  
c = rhobar/rho； s = beta/rho;  
gamma $=$ s\*alpha； rhobar $=$ -c\*alpha;  
phi $=$ c\*phibar； phibar $=$ s\*phibar;  
$\%$ Update the solution and residual norms  
$\begin{array} { l } { \mathrm {  ~ x ~ } = \mathrm {  ~ x ~ } + \mathrm {  ~ \left( p h i / r h o \right) * w } ; } \\ { \mathrm {  ~ w ~ } = \mathrm {  ~ v ~ } - \mathrm {  ~ \left( g a m m a / r h o \right) * w } ; } \\ { \mathrm {  ~ n ~ r ~ } = \mathrm {  ~ p h i b a r } ; } \\ { \mathrm {  ~ n ~ s ~ } = \mathrm {  ~ n r * a l p h a * a b s } \mathrm {  ~ \left( c \right) ~ } ; } \end{array}$   
end  
end

LSQR requires $3 m + 5 n$ multiplications and storage of two $m$ -vectors $u$ and $A v$ and three $n$ -vectors $x , v ,$ and $w$ . This can be compared to CGLS,which requires $2 m + 3 n$ multiplications, two $m$ -vectors, and two $n$ -vectors.Unlike in CGLS,the residual vector $r _ { k } = U _ { k + 1 } t _ { k + 1 }$ is not computed in LSQR.

Benbow [104,1999] generalized GKL lower bidiagonalization and LSQR to solve the generalized normal equations $A ^ { T } M ^ { - 1 } A x = A ^ { T } M ^ { - 1 } b$ where $M = L L ^ { T }$ . When vectors $\tilde { u } _ { i } = L u _ { i }$ are introduced into LSQR,only matrix-vector operations with $A$ ， $A ^ { T }$ ,and $M ^ { - 1 }$ are needed:

$$
A v _ { i } \mathrm { a n d } A ^ { T } L ^ { - T } L ^ { - 1 } u _ { i + 1 } = A ^ { T } M ^ { - 1 } \tilde { u } _ { i + 1 } .
$$

Algorithm LSME of Paige [852,1974] is an algorithm for solving consistent systems $A x = b$ using the same bidiagonalization process as LSQR. Let

$$
L _ { k } = \left( \begin{array} { l l l l l } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \beta _ { 3 } } & { \alpha _ { 3 } } & & \\ & & { \ddots } & { \ddots } & \\ & & & { \beta _ { k } } & { \alpha _ { k } } \end{array} \right) \in \mathbb { R } ^ { k \times k }
$$

be the lower bidiagonal matrix consisting of the first $k$ rows of $B _ { k }$ in (6.2.37). Then the bidiagonalization recurrence relations (6.2.36) can be written as

$$
A V _ { k } = U _ { k } L _ { k } + \beta _ { k + 1 } u _ { k + 1 } e _ { k } ^ { T } , \qquad A ^ { T } U _ { k } = V _ { k } L _ { k } ^ { T } .
$$

The LSME approximations $x _ { k }$ are given by v

$$
x _ { k } = V _ { k } z _ { k } , \quad z _ { k } = \beta _ { 1 } L _ { k } ^ { - 1 } e _ { 1 } ,
$$

where $z _ { k }$ and $x _ { k }$ are obtained by the recurrences

$$
\zeta _ { k } = - ( \beta _ { k } / \alpha _ { k } ) \zeta _ { k - 1 } , \quad x _ { k } = x _ { k - 1 } + \zeta _ { k } v _ { k } .
$$

Since the increments $v _ { k }$ form an orthogonal set, the step lengths are bounded by $| \zeta _ { k } | _ { 2 } \le \| x _ { k } \| _ { 2 } \le$ $\| x \| _ { 2 }$ . The LSME approximations $x _ { k }$ lie in $\mathcal { K } _ { k } ( A A ^ { T } , r _ { 0 } )$ and minimize $\lVert \boldsymbol { x } ^ { \dagger } - \boldsymbol { x } _ { k } \rVert _ { 2 }$ . By uniqueness,LSME is mathematically equivalent to Craig's method and CGME.

# Algorithm 6.2.8 (LSME).

$$
 \begin{array} { r l } & { { \mathrm {  ~ { \cal ~ C } ~ i s o n ~ } } } \\ & { { \mathrm {  ~ { \cal ~ C } ~ i s o p t ~ } } } \\ & { { \mathrm {  ~ { \cal ~ C } ~ i s o p t ~ f o r ~ s t o : ~ s t : ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal \mu ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal \mu ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Z } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Z } ~ e ~ n ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Z } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ &  { \mathrm {  ~ { \cal ~ X } ~ } } \\ & { { \mathrm {  ~ { \cal ~ X } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ &  { \mathrm {  ~ { \cal ~ X } ~ } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ & { { \mathrm {  ~ { \cal ~ Y } ~ } } } \\ &   \mathrm   ~  \cal ~ Z \end{array}
$$

end

The residual vector $r _ { k } = b - A x _ { k }$ is obtained from

$$
r _ { k } = b - A V _ { k } z _ { k } = - \zeta _ { k } \beta _ { k + 1 } u _ { k + 1 } , \zeta _ { k } = e _ { k } ^ { T } z _ { k } .
$$

LSME needs storage for two $n$ -vectors $x , v$ and one $m$ -vector $u$ .It requires five scalar products or vector updates of length $n$ and three of length $m$ per step.ForLSME (and Craig's method) the error functionals $\| r _ { k } \| _ { 2 }$ and $\Vert \boldsymbol { A } ^ { T } \boldsymbol { r } _ { k } \Vert _ { 2 }$ will not decrease monotonically. LSME has the advan-tage over CGME that it is easily possible to transfer to the LSQR approximation at any step; see Saunders [965,1995]. As for CGLS and LSQR,almost no additional work or storage is required to apply LSME to regularized problems.

For LSQR the residual norms $\| r _ { k } \| _ { 2 }$ decrease monotonically, but $\Vert \boldsymbol { A } ^ { T } \boldsymbol { r } _ { k } \Vert _ { 2 }$ in general oscillates.The oscillations can be large for ill-conditioned problems.Such behavior is undesirable, because practical stopping criteria are based on $\| A ^ { T } r _ { k } \| _ { 2 }$ ； see Section 6.2.6. The LSMR algorithm by Fong and Saunders [417, 2O11] uses the same Bidiagl process as LSQR but computes the Krylov subspace approximations that solve

$$
\operatorname* { m i n } _ { x _ { k } } \| A ^ { T } ( b - A x _ { k } ) \| _ { 2 } , \quad x _ { k } = V _ { k } y _ { k } .
$$

Hence for LSMR, $\| A ^ { T } r _ { k } \| _ { 2 }$ is monotonically decreasing by design.This allows the iterations to be terminated more safely. The residual norm $\| r _ { k } \| _ { 2 }$ of LSQR will be smaller but,usually, not by much.

We now describe how subproblems (6.2.50) can be solved efficiently. After $k$ steps, we have

$$
A V _ { k } = U _ { k + 1 } B _ { k } , \quad \quad A ^ { T } U _ { k + 1 } = V _ { k + 1 } L _ { k + 1 } ^ { T } ,
$$

where $B _ { k }$ is given as in (6.2.37), and $\begin{array} { r l } { L _ { k + 1 } = \left( \begin{array} { l l l } { B _ { k } } & { \alpha _ { k + 1 } e _ { k + 1 } } \end{array} \right) } \end{array}$ . Also,

$$
r _ { k } = b - A V _ { k } y _ { k } = U _ { k + 1 } ( \beta _ { 1 } e _ { 1 } - B _ { k } y _ { k } ) .
$$

From $b = \beta _ { 1 } u _ { 1 }$ and $A ^ { T } u _ { 1 } = \alpha _ { 1 } v _ { 1 }$ , we obtain $A ^ { T } b = \beta _ { 1 } A u _ { 1 } = \bar { \beta } _ { 1 } v _ { 1 }$ , where $\bar { \beta } _ { k } \equiv \alpha _ { k } \beta _ { k }$ . Hence $A x _ { k } = V _ { k } y _ { k } = U _ { k + 1 } B _ { k } y _ { k }$ ,and

$$
\begin{array} { r l } & { A ^ { T } V _ { k } y _ { k } = A ^ { T } U _ { k + 1 } B _ { k } y _ { k } = V _ { k + 1 } L _ { k + 1 } ^ { T } B _ { k } y _ { k } } \\ & { \qquad = V _ { k + 1 } \left( { \begin{array} { c } { B _ { k } ^ { T } } \\ { \alpha _ { k + 1 } e _ { k + 1 } ^ { T } } \end{array} } \right) B _ { k } y _ { k } . } \end{array}
$$

Because $e _ { k + 1 } ^ { T } B _ { k } = \beta _ { k + 1 } e _ { k } ^ { T }$ ,the LSMR subproblem becomes

$$
\operatorname* { m i n } _ { y _ { k } } \| A ^ { T } r _ { k } \| _ { 2 } = \operatorname* { m i n } _ { y _ { k } } \left\| \bar { \beta } _ { 1 } e _ { 1 } - \left( \frac { B _ { k } ^ { T } B _ { k } } { \bar { \beta } _ { k + 1 } e _ { k } ^ { T } } \right) y _ { k } \right\| _ { 2 } .
$$

To solve this,a sequence of plane rotations is first used to compute the QR factorization

$$
Q _ { k } B _ { k } = { \binom { R _ { k } } { 0 } }
$$

as in LSQR. Here $R _ { k }$ is upper bidiagonal, and $R _ { k } ^ { T } R _ { k } \ : = \ : B _ { k } ^ { T } B _ { k }$ .If $R _ { k } ^ { T } q _ { k } \ = \ \bar { \beta } _ { k + 1 } e _ { k }$ ，then $q _ { k } = ( \bar { \beta } _ { k + 1 } / \rho _ { k } ) e _ { k } \equiv \varphi _ { k } e _ { k }$ . If we define $t _ { k } = R _ { k } y _ { k }$ ,subproblem (6.2.53) can be written

$$
\operatorname* { m i n } _ { y _ { k } } \| \boldsymbol { A } ^ { T } \boldsymbol { r } _ { k } \| _ { 2 } = \operatorname* { m i n } _ { t _ { k } } \left\| \bar { \beta } _ { 1 } e _ { 1 } - \left( \begin{array} { c } { \boldsymbol { R } _ { k } ^ { T } } \\ { \varphi _ { k } e _ { k } ^ { T } } \end{array} \right) t _ { k } \right\| _ { 2 } ,
$$

Next, perform the QR factorization

$$
\bar { Q } _ { k } \left( \begin{array} { c c } { { R _ { k } ^ { T } } } & { { \bar { \beta } _ { 1 } e _ { 1 } } } \\ { { \varphi _ { k } e _ { k } ^ { T } } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { \bar { R } _ { k } } } & { { z _ { k } } } \\ { { 0 } } & { { \zeta _ { k + 1 } } } \end{array} \right) ,
$$

where $\bar { R } _ { k }$ is upper bidiagonal. The subproblem can now be writen

$$
\operatorname* { m i n } _ { y _ { k } } \| \boldsymbol { A } ^ { T } \boldsymbol { r } _ { k } \| _ { 2 } = \operatorname* { m i n } _ { t _ { k } } \left\| \left( \begin{array} { c } { z _ { k } } \\ { \zeta _ { k + 1 } } \end{array} \right) - \left( \begin{array} { c } { \bar { R } _ { k } } \\ { 0 } \end{array} \right) t _ { k } \right\| _ { 2 } .
$$

The solution $t _ { k }$ is obtained by solving $\bar { R } _ { k } t _ { k } = z _ { k }$ ,and $\lVert A ^ { T } r _ { k } \rVert _ { 2 } = | \zeta _ { k + 1 } |$ is monotonically decreasing.

Let $W _ { k } = ( w _ { 1 } , \dots , w _ { k } )$ and ${ \bar { W } _ { k } } = ( \bar { w } _ { 1 } , \dots , \bar { w } _ { k } )$ be computed by forward substitution from $R _ { k } ^ { T } W _ { k } ^ { T } = V _ { k } ^ { T }$ and $\bar { R } _ { k } ^ { T } \bar { W } _ { k } ^ { T } = W _ { k } ^ { T }$ .Then,from

$$
x _ { k } = V _ { k } y _ { k } , \quad R _ { k } y _ { k } = t _ { k } , \quad \bar { R } _ { k } t _ { k } = z _ { k } ,
$$

we have

$$
x _ { k } = W _ { k } R _ { k } y _ { k } = W _ { k } t _ { k } = { \bar { W } } _ { k } { \bar { R } } _ { k } t _ { k } = { \bar { W } } _ { k } z _ { k } = x _ { k - 1 } + \zeta _ { k } { \bar { w } } _ { k } .
$$

As for LSQR, all quantities needed to update the approximation $x _ { k - 1 }$ can be computed by forward recurrence relations, where only the last term needs to be saved. Also, $\| r _ { k } \| _ { 2 }$ and $\| x _ { k } \| _ { 2 }$ can be obtained by using formulas that can be updated cheaply. For details see Fong and Saunders [417,2o11], where a detailed pseudocode forLSMR is given. LSMR shares with LSQR the property that for rank-deficient problems,it terminates with the least-norm solution.

LSMR requires storage for one $m$ -vector and seven $n$ -vectors.The number of floating-point multiplications is $8 n$ per iteration step. The corresponding figures for LSQR are two $m$ -vectors, three $n$ -vectors and $3 m + 5 n$ ,respectively.LSMR is easily extended to solve regularized least squares problems (6.4.8).

The three algorithms LSME,LSQR,and LSMR all use the same bidiagonalization algorithm and generate approximations in the same Krylov subspaces $x _ { k } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ The algorithms minimize different error quantities, $\| x _ { k } - x \|$ ， $\| r _ { k } - r \|$ ,and $\| A ^ { T } ( r _ { k } - r ) \|$ , respectively (where the last two are equivalent to minimizing $\| r _ { k } \| _ { 2 }$ and $\| A ^ { T } r _ { k } \| _ { 2 } )$ .LSME can only be used for consistent systems.LSMR is the only algorithm for which all three error measures are monotonically decreasing. This makes LSMR the method of choice in terms of stability. However, at any given iteration,LSQR has a slightly smaller residual norm. It has been suggested that LSMR should be used until the iterations can be terminated. Then a switch can be made to the corresponding LSQR solution.

Similar comments apply to CGME and CGLS. A CGLS-type algorithm, CRLS,correspond-ing to LSMR that minimizes $\| A ^ { T } r _ { k } \| _ { 2 }$ is derived by Bjorck [129,1979] by using a modified inner product in CGLS. The same algorithm is derived by Fong [416, 2o11] by applying the conjugate residual (CR) algorithm to the normal equations $A ^ { T } A x = A ^ { T } b$ .Tests have shown that CRLS achieves much lower final accuracy in $x _ { k }$ than CGLS and LSMR,and therefore its use cannot be recommended.

Fortran, C, Python,and MATLAB implementations of LSQR,LSMR,and other iterative solvers are available from Systems Optimization Laboratory, Stanford University. Julia implementations are available at http://dpo.github.io/sof tware/.

# 6.2.6-Effects of Finite Precision

Due to loss of orthogonality in the computed basis vectors in LSQR and the residual vectors $s _ { k } = A ^ { T } b$ in CGLS,the finite termination property is not valid in floating-point arithmetic. In many practical applications the desired accuracy can be obtained in far less than $n$ iterations. However, when $A$ is ill-conditioned and $b$ has substantial components along singular vectors corresponding to small singular values,many more than $n$ iterations may be needed. The first analysis of the properties of the symmetric Lanczos process in finite-precision arithmetic was given in the pioneering thesis of Paige [857,1971]. This predicts that the main effect of finite precision is a delay in convergence without loss of stability.

In CGLS the residual vector $r = b - A x$ is recursively computed as $r _ { k } = r _ { k - 1 } - A p _ { k }$ at each iteration step.In finite-precision arithmetic,this residual will differ from the true residual. Greenbaum [534,1997] gives estimates of the attainable accuracy of recursively computed residual methods. Extending these results,the limiting accuracy of different implementations of CGLS- and LSQR-type methods is analyzed by Bjorck, Elfving,and Strakos [142,1998]. They find that in the limit the computed solution's accuracy is at least as good as for a backward stable method.

Greenbaum [533,198g] observed that Krylov subspace algorithms seem to behave in finiteprecision like the exact algorithm applied to a larger problem $\boldsymbol { B } \boldsymbol { \widehat { x } } \ = \ \boldsymbol { c }$ ，where $B$ has many eigenvalues distributed in tiny intervals about the eigenvalues of $A$ .Hence $\kappa ( B ) \approx \kappa ( A )$ ,which could explain why the error bound (6.2.18) has been observed to apply also in finite precision. Some theoretical properties of CGLS and LSQR,such as monotonic decrease of $\| r _ { k } \| _ { 2 }$ ,remain valid in floating-point arithmetic.

Krylov subspace methods, such as CGLS and LSQR,typically “converge" in three phases as follows (see, e.g.,Axelsson [48,1994]):

1.An initial phase in which convergence depends essentially on the initial vector $b$ and can be rapid.   
2.A middle phase,where the convergence is linear with a rate depending on the spectral condition number $\kappa ( A )$   
3.A final phase,where the method converges superlinearly, i.e.,the rate of convergence accelerates as the number of steps increases. This may take place after considerably less than $n$ iterations.

In a particular case,any of these phases can be absent or appear repeatedly. The behavior can be supported by heuristic arguments about the spectrum of $A$ ； see Nevanlinna [829,1993]. For example,superlinear convergence in the third phase can be explained by the effects of the smaller and larger singular values of $A$ being eliminated.

A typical behavior is shown in Figure 6.2.1, which plots $\lVert x ^ { \dagger } - x _ { k } \rVert$ and $\| A ^ { T } r _ { k } \|$ for LSQR and CGLS applied to the sparse least squares problem ILLC1850 from Matrix Market (Boisvert et al. [160,1997l). This problem originates from a surveying application and has dimensions $1 8 5 0 \times$ 712 with 8636 nonzeros. The condition number is $\kappa ( A ) = 1 . 4 0 5 \times 1 0 ^ { 3 }$ ,and the inconsistent right-hand side $b$ is scaled so that the true solution $x$ has unit norm and $\| r \| _ { 2 } = 0 . 7 9 \times 1 0 ^ { - 4 }$ Paige and Saunders [866,1982] remark that LSQR is often numerically somewhat more reliable than CGLS when $A$ is ill-conditioned and many iterations have to be carried out. In Figure 6.2.1 the plots are similar, and both CGLS and LSQR converge after about $2 5 0 0 \approx 3 . 5 n$ iterations to a final error $\| x - x _ { k } \| < 1 0 ^ { - 1 4 }$ . The superlinear convergence phase is clearly visible. Note that the oscillations in $\| A ^ { T } r _ { k } \|$ are not caused by the finite precision.

![](images/20a0ec30925843b6f3d247ca42fd3451fb202dcf997c9ccd31ca6b0a9496d7a8.jpg)  
Figure 6.2.1. $\| x ^ { \dagger } - x _ { k } \|$ and $\| A ^ { T } r _ { k } \|$ for problem ILLC1850: LSQR (blue and green solid lines) LS(black and magenta dash-dot lines).

It might be tempting to restart CGLS or LSQR after a certain number of iterations from a very good approximation to the solution and an accurately computed residual. However, after such a restart, any previously achieved superlinear convergence is lost and often not recovered until after many additional iterations.

Ideally, the iterations should be stopped when the backward error in $x _ { k }$ is sufficiently small. Evaluating the expression given in Section 2.5.2 for the optimal backward error is generally too expensive. In practice, stopping criteria are based on the two upper bounds

$$
\| E _ { 1 } \| _ { 2 } = \| r - { \bar { r } } \| _ { 2 } / \| { \bar { x } } \| _ { 2 } , \qquad \| E _ { 2 } \| _ { 2 } = \| A ^ { T } { \bar { r } } \| _ { 2 } / \| { \bar { r } } \| _ { 2 } ,
$$

where $\bar { x }$ and $\bar { r }$ are the current approximate solution and residual. This motivates terminating the iterations as soon as one of the following two conditions are satisfied:

$$
\begin{array} { r l } & { \mathrm { S 1 : ~ } \| \bar { \boldsymbol { r } } _ { k } \| _ { 2 } < \eta _ { A } \| A \| \| \boldsymbol { x } _ { k } \| _ { 2 } + \eta _ { b } \| b \| _ { 2 } , } \\ & { } \\ & { \mathrm { S 2 : ~ } \| A ^ { T } \bar { \boldsymbol { r } } _ { k } \| _ { 2 } < \eta _ { A } \| A \| \| \boldsymbol { r } _ { k } \| _ { 2 } , } \end{array}
$$

where $\eta _ { A }$ and $\eta _ { b }$ are user-specified tolerances. S1 is relevant for consistent problems; otherwise, S2 is used. Note that it is possble for $x _ { k }$ to be a solution of a slightly perturbed least squares problem and yet for both $\| E _ { 1 } \| _ { 2 }$ and $\| E _ { 2 } \| _ { 2 }$ to be orders of magnitude larger than the norm of the optimal perturbation bound. LSQR and LSMR also terminate if an estimate of $\kappa _ { 2 } ( A )$ exceeds a specified limit. This option is useful when $A$ is ill-conditioned or rank-deficient.Because the stopping criterion S2 is normally used for inconsistent least squares problems, the oscillations in $\| A ^ { T } r _ { k } \|$ that occur for LSQR and CGLS are undesirable. This is one reason to use LSMR, for which this quantity is monotonically decreasing.

Figure 6.2.2 compares LSQR and LSMR applied to the same problem as before. The final accuracy is similar for both algorithms. As predicted by theory, $\| A ^ { T } r _ { k } \|$ is monotonically decreasing for LSMR and always smaller than for LSQR. (In many cases the difference is much more obvious.） Hence criterion S2 will terminate the iterations sooner than for LSQR. On the other hand, both $\lVert x - x _ { k } \rVert _ { 2 }$ and $\| r _ { k } \| _ { 2 }$ are typically larger for LSMR than for LSQR.

![](images/ea1db25bcf838f40e91a28e13fc27dc080adfb3d649695bc51721ca2636012a5.jpg)  
Figure 6.2.2. $\| x ^ { \dagger } - x _ { k } \|$ and $\| A ^ { T } r _ { k } \|$ for problem ILLC1850: LSQR (blue and green solid lines) MR (black and magenta dashed lines).

Fong and Saunders [417,2o11] tested LSQR and LSMR on 127 different least squares problems of widely varying origin, structure,and size from the SuiteSparse matrix collection (Davis and Hu [291, 2o11]). They make similar observations about the accuracy achieved. With $\eta _ { 2 } = 1 0 ^ { - 8 }$ in stopping rule S2, the iterations terminated sooner for LSMR. They suggest the strategy of running LSMR until termination, then transferring to the LSQR solution. In tests by Gould and Scott[520,2o17] on 921 problems from the same collection,LSMR had fewer failures with a given iteration limit and faster execution than LSQR.

If $\operatorname { r a n k } ( A ) < n$ ， CGLS and LSQR in theory will converge to the pseudoinverse solution provided $x _ { 0 } \in \mathcal { R } ( A ^ { T } )$ (e.g., $x _ { 0 } = 0$ ). In floating-point arithmetic,rounding errors will introduce a growing component in ${ \mathcal { N } } ( A )$ in the iterates $x _ { k }$ . Initially this component will remain small, but eventually divergence sets in,and $\| x _ { k } \|$ will grow quite rapidly. The vectors $x _ { k } / \Vert x _ { k } \Vert$ then become increasingly close to a null-vector of $A$ ; see Paige and Saunders [866,1982, Section 6.4].

In Figure 6.2.3 plots of $\lVert x ^ { \dagger } - x _ { k } \rVert$ and $\| r _ { k } \|$ for CGME and LSME are applied to a consistent underdetermined system with the transpose of the matrix ILLC1850. The algorithms perform almost identically. A final accuracy of $\| x - x _ { k } \| = 6 . 2 \times 1 0 ^ { - 1 4 }$ is achieved after about 2500 iterations. Superlinear convergence sets in slightly earlier for CGME.As predicted, $\lVert x ^ { \dagger } - x _ { k } \rVert$ converges monotonically, while $\| r _ { k } \|$ Oscillates. For consistent systems $A x = b$ with stopping rule S1, the oscillation in $\| r _ { k } \|$ that occurs for CGME and LSME is not an attractive feature. For CGLS and LSQR, $\| r _ { k } \|$ converges monotonically. These methods apply also to underdetermined systems,and,unlike CGME and LSME, they will not break down if $A x = b$ turns out to be inconsistent.

![](images/9e172d798f873f5c28b71dd6693ab79d2043cbe3d61059bf48652c1f7d5f60bf.jpg)  
Figure 6.2.3. Underdetermined consistent problem with the transpose of ILLC1850: $\lVert x ^ { \dagger } - x _ { k } \rVert$ and $\| r _ { k } \|$ ; CGME (blue and red solid lines); LSME (black and green dashed lines).

As shown in Figure 6.2.4 the convergence of $\lVert \boldsymbol { x } ^ { \dagger } - \boldsymbol { x } _ { k } \rVert$ for CGLS is only marginally slower than for CGME. The residual norm is always smaller and behaves monotonically. Thus, CGLS achieves similar final accuracy with only slightly more work and storage than CGME and can be terminated earlier. Therefore, CGLS or LSQR are usually preferred also for underdetermined systems.

![](images/3ba73c242aeb687af35bfe424ca4606e7f5c12337adfc1a79337e1ba859b6429.jpg)  
Figure 6.2.4. Problem ILLC1850 overdetermined consistent: $\lVert x ^ { \dagger } - x _ { k } \rVert$ and $\| r _ { k } \|$ : CGME (blue and red solid lines) and CGLS (black and green dash-dot lines).

Although the two sets of basis vectors $U _ { k }$ and $V _ { k }$ generated by GKL bidiagonalization are theoretically orthogonal, this property is lost in floating-point arithmetic. The algorithm behavior therefore deviates from the theoretical. Reorthogonalization maintains a certain level of orthogonality and accelerates convergence at the expense of more arithmetic and storage; see Simon [995,1984]. In full reorthogonalization, newly computed vectors $u _ { k + 1 }$ and $v _ { k + 1 }$ are reorthogonalized against all previous basis vectors. If $U _ { k }$ and $V _ { k }$ are orthonormal to working accuracy, this involves computing

$$
u _ { k + 1 } - U _ { k } ( U _ { k } ^ { T } u _ { k + 1 } ) , \qquad v _ { k + 1 } - V _ { k } ( V _ { k } ^ { T } v _ { k + 1 } )
$$

and normalizing the resulting vectors. $U _ { k }$ and $V _ { k }$ must be saved,and the cost is roughly $4 k ( m +$ $n$ ) flops.After $k$ steps the accumulated cost is about $2 k ^ { 2 } ( m + n )$ flops.Thus,full reorthogonalization is not practical for larger values of $k$ . The cost can be limited by using local reorthogonalization, where $u _ { k + 1 }$ and $v _ { k + 1 }$ are reorthogonalized against the $p$ last vectors, where $p \geq 0$ is an input parameter.

Because $U _ { k }$ and $V _ { k }$ are generated by coupled two-term recurrences, these two sets of vectors have closely related orthogonality. Simon and Zha [996, 2ooo] show that keeping $V _ { k }$ orthonormal to machine precision $\mathbf { u }$ will make $U _ { k }$ roughly orthonormal to a precision of at least $O ( \sqrt { \mathbf { u } } )$ and vice versa if $U _ { k }$ is orthogonalized. Such one-sided reorthogonalization saves at least half the cost of full reorthogonalization. For strongly overdetermined systems ( $m \gg n$ ）the savings are highest if only $V _ { k }$ is orthogonalized.

Tests by Fong and Saunders [417,2o11] show that for more difficult problems,reorthogonalization can make a huge difference in the number of iterations needed by LSMR. When comparing ful reorthogonalization and the two versions of one-sided reorthogonalization, they (unexpectedly) found that the results from these three versions were indistinguishable in all test cases.The current implementation of LSMR includes the option of local one-sided reorthogonalization.

Barlow [68, 2o13] showed that one-sided reorthogonalization is a very effective strategy for preserving the desired behavior of GKL bidiagonalization. In exact arithmetic, GKL generates the factorization

$$
A = U B V ^ { T } \in \mathbb { R } ^ { m \times n } , \quad m \geq n ,
$$

with orthonormal $U \in \mathbb { R } ^ { m \times n }$ and orthogonal $V \in \mathbb { R } ^ { n \times n }$ . In finite precision,orthogonality is lost.Assume now that

$$
\begin{array} { r } { \eta = \frac { 1 } { 2 } \lVert I - V ^ { T } V \rVert _ { F } , } \end{array}
$$

where $V$ is the matrix to be reorthogonalized. Then GKL produces Krylov subspaces generated by a nearby matrix $A + \delta A$ ,where

$$
\| \delta A \| _ { F } = O ( \mathbf { u } + \boldsymbol \eta ) \| A \| _ { F } .
$$

A key result is that the singular values of the bidiagonal matrix $B _ { k }$ produced after $k$ steps of this procedure are the exact result for the Rayleigh-Ritz approximation of a nearby matrix.

# Notes and references

Arioli,Duff,and Ruiz [37,1992] developed possible stopping criteria for iterative methods. StrakoS and Tichy [1O40, 2oo2] consider theoretical error estimates in CG methods that work in finite precision. Meurant and Strakos [792, 2oo6] give error bounds for CG to justify stop-ping criteria. Estimates of the optimal backward error have been studied by Chang,Paige, and Titley-Peloquin [235,2oog], Grcar, Saunders,and Su [532, 2oo7],and Jiranek and Titley-Péloquin [673, 2o1o]. The occurrence of superlinear convergence in general Krylov subspace methods is analyzed by Simoncini and Szyld [997,2oo5]. Composite convergence bounds for finite-precision CG computations are derived by Gergelits and Strakos [466, 2o14]. Paige [863, 2019l proves the highly accurate behavior of the finite-precision Lanczos process for symmetric matrices. The theory of block Krylov subspace methods for linear systems with multiple right-hand sides is discussed by Gutknecht [556, 2007].

# 6.2.7 - The MINRES and MINARES Algorithms

For linear systems $A x = b$ ,where $A$ is symmetric and nonsingular but possibly indefinite, the CG method cannot be used. The MINRES (minimal residual) algorithm of Paige and Saunders [855, 1975] computes minimum residual approximations $x _ { k }$ ， $k = 1 , 2 , \ldots$ ，as the solution of the problem

$$
\operatorname* { m i n } _ { x _ { k } } \| A x _ { k } - b \| _ { 2 } , \quad x _ { k } \in { \mathcal { K } } _ { k } ( A , b ) .
$$

The Lanczos process is defined for any symmetric matrix $A$ It generates an orthogonal basis $U _ { k } = ( u _ { 1 } , u _ { 2 } , \ldots , u _ { k } )$ for the Krylov subspaces $\textstyle { \mathcal { K } } _ { k } ( A , b )$ . Setting $x _ { k } = U _ { k } y _ { k }$ , we obtain from (6.2.31) that

$$
\begin{array} { r } { b - A x _ { k } = \beta _ { 1 } u _ { 1 } - A U _ { k } y _ { k } = U _ { k + 1 } \big ( \beta _ { 1 } e _ { 1 } - \hat { T } _ { k } y _ { k } \big ) . } \end{array}
$$

By the orthogonality of $U _ { k + 1 }$ ,the least squares problem (6.2.62) is seen to be equivalent to

$$
\operatorname* { m i n } _ { y _ { k } } \| \beta _ { 1 } e _ { 1 } - \hat { T } _ { k } y _ { k } \| _ { 2 } .
$$

This subproblem is best solved using the QR factorization

$$
G _ { k , k + 1 } \cdot \cdot \cdot G _ { 2 3 } G _ { 1 2 } \hat { T } _ { k } = \left( \begin{array} { l } { R _ { k } } \\ { 0 } \end{array} \right) = \left( \begin{array} { l l l l l } { \gamma _ { 1 } } & { \delta _ { 2 } } & { \epsilon _ { 3 } } & & \\ & { \gamma _ { 2 } } & { \delta _ { 3 } } & { \ddots } & \\ & & { \gamma _ { 3 } } & { \ddots } & { \epsilon _ { k } } \\ & & & { \ddots } & { \delta _ { k } } \\ & & & & { \gamma _ { k } } \\ & & & & { 0 } \end{array} \right) \in \mathbb { R } ^ { ( k + 1 ) \times k } ,
$$

where the plane rotations $G _ { j , j + 1 }$ annihilate the subdiagonal elements in $\hat { T } _ { k }$ . The same rotations are applied to the right-hand side, giving

$$
G _ { k , k + 1 } \cdot \cdot \cdot G _ { 2 3 } G _ { 1 2 } \beta _ { 1 } e _ { 1 } = { \binom { t _ { k } } { \bar { \tau } _ { k + 1 } } } ,
$$

where $t _ { k } = ( \tau _ { 1 } , \ldots , \tau _ { k } ) ^ { T }$ . The factorization (6.2.64) can be updated easily, as we now show. In the next step, a row and a column are added to $\hat { T } _ { k }$ . The only new nonzero elements

$$
\left( \begin{array} { l } { \beta _ { k + 1 } } \\ { \alpha _ { k + 1 } } \\ { \beta _ { k + 2 } } \end{array} \right)
$$

are in column $k + 1$ and rows $k , k + 1$ ,and $k + 2$ . To get column $k + 1$ in $R _ { k + 1 }$ , the two last rotations from the previous steps are first applied to column $k + 1$ and rows $k - 1 , k , k + 1$ . The element $\beta _ { k + 2 }$ is then annihilated by anew rotation $G _ { k + 1 , k + 2 }$

We have $x _ { k } = U _ { k } y _ { k }$ , where $y _ { k }$ satisfies the upper triangular system $R _ { k } y _ { k } = t _ { k }$ .To compute $x _ { k }$ without having tosave all of $U _ { k }$ we define $D _ { k } = \left( d _ { 1 } , \ldots , d _ { k } \right)$ from $R _ { k } ^ { T } D _ { k } ^ { T } = U _ { k } ^ { T }$ . This yields the recurrence relation $\dot { \mathcal { A } } _ { 0 } = \mathcal { d } _ { - 1 } = 0$ ）

$$
\gamma _ { k } d _ { k } = u _ { k } - \delta _ { k } d _ { k - 1 } - \epsilon _ { k } d _ { k - 2 } , \quad k \geq 1 .
$$

Hence, $x _ { k }$ can be updated using

$$
x _ { k } = U _ { k } y _ { k } = D _ { k } R _ { k } y _ { k } = \left( D _ { k - 1 } \quad d _ { k } \right) { \binom { t _ { k - 1 } } { \tau _ { k } } } = x _ { k - 1 } + \tau _ { k } d _ { k } .
$$

When $A$ is singular, MINRES computes a least squares solution but not, in general, the minimum-length solution

$$
\operatorname* { m i n } \| x \| _ { 2 } { \mathrm { ~ } } \operatorname { s u b j e c t { \mathrm { ~ t o ~ } } } x \in \arg \operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } ;
$$

see Choi [245, 2oo6]. If the system is inconsistent, then MINRES converges to a least squares solution but not, in general, to the solution of minimum length. Choi, Paige,and Saunders [245, 2011] develop MINRES-QLP for that purpose. MINRES-QLP uses a QLP decomposition of the tridiagonal matrix from the Lanczos process and converges to the pseudoinverse solution. MINRES-QLP requires slightly more operations per iteration step but can give more accurate solutions than MINRES on illconditioned problems.An implementation is given by Choi and Saunders [246,2014].

Applying MINRES to the augmented system could be an alternative approach for solving least squares problems. However,as shown by Fischer, Silvester,and Wathen [409,1998],MIN-RES makes progress only in every second iteration, and LSQR and CGLS converge twice as fast. Indeed,applying the Lanczos process to the augmented system leads to the GLK process (Paige and Saunders [866,1982, Section 2.1]) and hence to LSQR.

MINARES by Montoison, Orban,and Saunders [802, 2023] completes the family of Krylov methods based on the symmetric Lanczos process (CG, SYMMLQ, MINRES,MINRES-QLP). For any symmetric system $A x = b$ ,MINARES minimizes $\| A r _ { k } \| _ { 2 } ^ { 2 }$ ，within the $k$ th Krylov subspace $\textstyle { \mathcal { K } } _ { k } ( A , b )$ . As this quantity converges to zero even if $A$ is singular,MINARES is well suited to singular symmetric systems.

At iteration $k$ , MINARES solves the least squares subproblem

$$
\operatorname* { m i n } _ { x _ { k } \in { \mathcal K } _ { k } ( A , b ) } \| A r _ { k } \| _ { 2 } ^ { 2 } , \quad r _ { k } = b - A x _ { k } .
$$

The quantities $\| A r _ { k } \| _ { 2 } ^ { 2 } , \ \| r _ { k } \| _ { 2 } ^ { 2 } , \ \| x _ { k } - x \| _ { 2 } ^ { 2 }$ ，and $\| x _ { k } - x \| _ { A } ^ { 2 }$ all decrease monotonically. On consistent systems, the number of iterations is similar to MINRES and MINRES-QLP when the stopping criterion is based on $\| r _ { k } \| _ { 2 } ^ { 2 }$ ,and significantly faster when the stopping criterion is based on $\| A r _ { k } \| _ { 2 } ^ { 2 }$

LSMR is a more general solver for the least squares problem $\mathrm { m i n } _ { x } \| b - A x \| _ { 2 } ^ { 2 }$ of square or rectangular systems. If $A$ were symmetric, LSMR would minimize $\| A r _ { k } \| _ { 2 } ^ { 2 }$ and appear at first glance to be equivalent to MINARES.However, $r _ { k }$ is defined within different Krylov subspaces, and LSMR would require two matrix-vector products $A v$ and $A u$ per iteration. (LSMR solving symmetric $A x = b$ is equivalent to MINRES solving $A ^ { 2 } x = A b .$ ）MINARES is more reliable than MINRES or MINRES-QLP on singular systems and more efficient than LSMR.

# 6.2.8 - The GMRES Algorithm

The generalized minimal residual (GMRES) method of Saad and Schultz [959,1986] is one of the most widely used Krylov subspace methods. GMRES computes a sequence of approximate solutions to an unsymmetric nonsingular system $A x \ = \ b$ .It is based on an extension of the Lanczos process of Arnoldi [39,1951] to non-Hermitian matrices. Given a unit vector $v _ { 1 } \in \mathbb { C } ^ { n }$ ， the Arnoldi process computes an orthonormal basis $\{ v _ { 1 } , \ldots , v _ { k } \}$ for the sequence of Krylov subspaces

$$
\mathcal { K } _ { k } ( A , v _ { 1 } ) = \operatorname { s p a n } \big \{ v _ { 1 } , A v _ { 1 } , \ldots , A ^ { k - 1 } v _ { 1 } \big \} , \quad k = 1 , 2 , \ldots .
$$

Assume that the process has generated $V _ { k } = \left( v _ { 1 } , v _ { 2 } , \ldots , v _ { k } \right)$ with orthonormal columns. In the next step the vector $w _ { k } = A v _ { k }$ is formed and orthogonalized against $v _ { 1 } , v _ { 2 } , \ldots , v _ { k }$ . Using MGS we compute

$$
w _ { k } = A v _ { k } , \quad h _ { i k } = w _ { k } ^ { T } v _ { i } , \quad w _ { k } : = w _ { k } - h _ { i k } v _ { i } , \quad i = 1 , \ldots , k .
$$

f $h _ { k + 1 , k } = \| w _ { k } \| _ { 2 } > 0$ we set $v _ { k + 1 } = w _ { k } / h _ { k + 1 , k }$ . Otherwise,the process terminates. In matrix form this process yields the Arnoldi decomposition

$$
A V _ { k } = V _ { k + 1 } H _ { k + 1 , k } ,
$$

where $H _ { k + 1 , k }$ is the upper Hessenberg matrix

$$
\begin{array} { r } { H _ { k + 1 , k } = \left( \begin{array} { c c c c c } { h _ { 1 1 } } & { h _ { 1 2 } } & { \hdots } & { h _ { 1 k } } \\ { h _ { 2 1 } } & { h _ { 2 2 } } & { \hdots } & { h _ { 2 k } } \\ & { \ddots } & { \ddots } & { \vdots } \\ & & { h _ { k , k - 1 } } & { h _ { k k } } \\ & & & & { h _ { k + 1 , k } } \end{array} \right) \in \mathbb { C } ^ { ( k + 1 ) \times k } . } \end{array}
$$

In GMRES the Arnoldi process is applied to

$$
v _ { 1 } = r _ { 0 } / \beta , \quad \beta = \| r _ { 0 } \| _ { 2 } ,
$$

where $x _ { 0 }$ is a given starting approximation, and $r _ { 0 } = b - A x _ { 0 }$ For $k = 1 , 2 , \ldots$ , GMRES

determines an approximation $x _ { k } = V _ { k } y _ { k } \in K _ { k } ( A , b )$ of minimum residual norm $\| r _ { k } \| _ { 2 } , r _ { k } =$ $b - A x _ { k }$ .From the Arnoldi decomposition (6.2.69) we have

$$
r _ { k } = b - A V _ { k } y _ { k } = \beta v _ { 1 } - V _ { k + 1 } H _ { k + 1 , k } y _ { k } = V _ { k + 1 } ( \rho _ { 1 } e _ { 1 } - H _ { k + 1 , k } y _ { k } ) ,
$$

where $V _ { k + 1 }$ has orthonormal columns. It follows that the minimum of $\| r _ { k } \| _ { 2 }$ is obtained when $y _ { k }$ solves the small Hessenberg least squares subproblem

$$
\operatorname* { m i n } _ { y _ { k } } \| \rho _ { 1 } e _ { 1 } - H _ { k + 1 , k } y _ { k } \| _ { 2 } .
$$

Since all $V _ { k }$ and $H _ { k + 1 , k }$ must be stored, this is solved only at the final step of GMRES by determining a product of plane rotations such that

$$
\begin{array} { r l } { Q _ { k } H _ { k + 1 , k } = \left( \begin{array} { c } { R _ { k } } \\ { 0 } \end{array} \right) , } & { { } \quad \left( \begin{array} { c } { g _ { k } } \\ { \gamma _ { k } } \end{array} \right) = \rho _ { 1 } Q _ { k } e _ { 1 } . } \end{array}
$$

Then the solution is obtained by solving $R _ { k } y _ { k } = g _ { k }$ and forming $x _ { k } = V _ { k } y _ { k }$ . The plane rotations can be used and then discarded.

GMRES terminates at step $k$ if $h _ { k + 1 , k } \ = \ 0$ Then from (6.2.69), $A V _ { k } ~ = ~ V _ { k } H _ { k , k }$ and $\mathrm { r a n k } ( A V _ { k } ) = \mathrm { r a n k } ( V _ { k } ) = k$ Hence $H _ { k , k }$ must be nonsingular, and

$$
r _ { k } = V _ { k } ( \beta _ { 1 } e _ { 1 } - H _ { k , k } y _ { k } ) = 0 , \quad H _ { k , k } y _ { k } = \beta _ { 1 } e _ { 1 } .
$$

It follows that $x _ { k } = V _ { k } y _ { k }$ is the exact solution of $A x = b$ .In exact arithmetic,GMRES terminates if and only if the exact solution has been found.

With all vectors $v _ { 1 } , \ldots , v _ { k }$ being stored, the memory is proportional to the number of steps. This limits the number of steps that can be taken. Usually GMRES is restarted after a fixed number of steps, typically between 10 and 30. Restarting usually slows down the convergence, and it can happen that restarted GMRES never reaches an accurate solution.

If the orthogonalization in GMRES is performed by MGS,as described above,a loss of orthogonality of size $v _ { k + 1 }$ will occur at step $k$ if $| h _ { k + 1 , k } |$ is small. This motivated Walker [1097, 1988] to develop an implementation HH-GMRES using the more expensive Householder orthogonalization. However, Greenbaum,Rozloznik,and Strakos [535,1997] observe that the conver-gence behavior and,ultimately,attainable precision of HH-GMRES do not differ from MGS-GMRES. In the MGS-GMRES version, orthogonality will be lost completely only when the residual norm $\| r _ { k } \| _ { 2 }$ has been reduced close to its final level. Paige,Rozloznik,and Strakos [865, 2006] were finally able to prove the backward stability of MGS-GMRES.

The rate of convergence of GMRES is closely related to the behavior of the sequence $\{ h _ { k + 1 , k } \}$ . In practice GMRES usually shows superlinear convergence. Unlike CG, upper bounds for the convergence of GMRES cannot be derived in terms of the condition number of $A$ The situation is more complicated because the eigensystem of an unsymmetric matrix may have complex eigenvalues and in general no orthogonal eigensystem. The residuals can be expressed as $r _ { k } = P _ { k } ( A ) r _ { 0 }$ , where $P _ { k }$ is a polynomial such that $P _ { k } ( 0 ) = 1$ . GMRES implicitly generates the polynomials for which $\| r _ { k } \| _ { 2 }$ is minimal. If $A$ is diagonalizable, $A = X \Lambda X ^ { - 1 }$ ， $\boldsymbol { \Lambda } = \operatorname { d i a g } \left( \lambda _ { j } \right)$ ， then

$$
\| r _ { k } \| _ { 2 } = \operatorname* { m i n } _ { P _ { k } ( 0 ) = 1 } \| P _ { k } ( A ) r _ { 0 } \| _ { 2 } \leq \| X \| _ { 2 } \| X ^ { - 1 } \| _ { 2 } \operatorname* { m i n } _ { P _ { k } ( 0 ) = 1 } \operatorname* { m a x } _ { j } | P _ { k } ( \lambda _ { j } ) | \| r _ { 0 } \| _ { 2 } .
$$

However, this upper bound is not very useful because the minimization of a polynomial with $P _ { k } ( 0 ) = 1$ over a set of complex numbers is an unsolved problem. Information about the eigenvalues alone does not suffice for determining the rate of convergence.

GMRES usually needs a good preconditioner in order to work. A right preconditioner,

$$
A M ^ { - 1 } u = b , \quad x = M ^ { - 1 } u ,
$$

has the advantage that the residuals of the preconditioned system are identical to the original residuals. For a right-preconditioned system the GMRES algorithm constructs an orthogonal basis for the subspace $\{ r _ { 0 } , A M ^ { - 1 } r _ { 0 } , \ldots , ( A M ^ { - 1 } ) ^ { m - 1 } r _ { 0 } \}$ . We summarize the algorithm below.

# Algorithm 6.2.9 (GMRES with Right Preconditioning).

$$
\begin{array} { r l } & { \boldsymbol { r _ { 0 } } = b - A x _ { 0 } ; \beta = \| \boldsymbol { r _ { 0 } } \| ; v _ { 1 } = r _ { 0 } / \beta ; } \\ & { \mathrm { f o r ~ } j = 1 , \ldots , m } \\ & { z _ { j } = M ^ { - 1 } v _ { j } ; w = A z _ { j } ; } \\ & { \mathrm { f o r ~ } i = 1 , \ldots , j } \\ & { \quad \boldsymbol { h _ { i j } } = w ^ { T } v _ { i } ; w = w - h _ { i j } v _ { i } } \\ & { \quad \boldsymbol { h _ { j + 1 , j } } = \| w \| _ { 2 } ; v _ { j + 1 } = w / h _ { j + 1 , j } ; } \end{array}
$$

$$
\begin{array} { r l } & { V _ { m } = ( v _ { 1 } , \ldots , v _ { m } ) ; } \\ & { y _ { m } = \operatorname * { a r g m i n } _ { y } \lVert \beta e _ { 1 } - \bar { H } _ { m } y _ { m } \rVert ; } \\ & { x _ { m } = x _ { 0 } + M ^ { - 1 } V _ { m } y _ { m } ; } \end{array}
$$

For many applications an effective fixed preconditioner $M$ is not available. Then one would like to be able to use a preconditioner defined as an arbitrary number of steps of another iterative method applied to solve $M z _ { j } = v _ { j }$ . For example,another Krylov subspace based on the normal equations could be used. It is desirable that the preconditioner be alowed to change without restarting GMRES so that $z _ { j } = M _ { j } ^ { - 1 } v _ { j }$ .Flexible GMRES is a simple modification of standard GMRES by Saad [955,1993] that alows the use of variable preconditioning.

# Algorithm 6.2.10 (FGMRES with Variable Right Preconditioning).

$$
\begin{array} { r l } & { { \boldsymbol r } _ { 0 } = b - A x _ { 0 } ; ~ \beta = { \| \boldsymbol r _ { 0 } \| } ; ~ { \boldsymbol v } _ { 1 } = r _ { 0 } / \beta ; } \\ & { \mathrm { f o r ~ } j = 1 , \dots , m } \\ & { ~ z _ { j } = M _ { j } ^ { - 1 } { \boldsymbol v } _ { j } ; ~ { \boldsymbol w } = A z _ { j } ; } \\ & { \mathrm { ~ f o r ~ } i = 1 , \dots , j } \\ & { ~ h _ { i j } = w ^ { T } { \boldsymbol v } _ { i } ; ~ { \boldsymbol w } = { \boldsymbol w } - h _ { i j } { \boldsymbol v } _ { i } } \\ & { ~ h _ { j + 1 , j } = { \| \boldsymbol w \| } _ { 2 } ; ~ { \boldsymbol v } _ { j + 1 } = w / h _ { j + 1 , j } ; } \end{array}
$$

$$
\begin{array} { r l } & { Z _ { m } = ( z _ { 1 } , \ldots , z _ { m } ) ; } \\ & { y _ { m } = \arcsin _ { y } \lVert \beta e _ { 1 } - \bar { H } _ { m } y _ { m } \rVert ; } \\ & { x _ { m } = x _ { 0 } + Z _ { m } y _ { m } ; } \end{array}
$$

The only diference from the standard version is that we now must save $Z _ { m } = ( z _ { 1 } , \dots , z _ { m } )$ and use it for the update of $x _ { 0 }$ . This doubles the storage cost, but the arithmetic cost is the same. Note that $z _ { 1 } , \ldots , z _ { m }$ in FGMRES is not a Krylov subspace.

By Propositions 2.1 and 2.2 in Saad [955,1993], $x _ { m }$ obtained at step $m$ in flexible GMRES minimizes the residual norm $\| b - A x _ { m } \| _ { 2 }$ over $x _ { 0 } + \mathrm { s p a n } \left( Z _ { m } \right)$ . Assuming that $j - 1$ steps of FGMRES have been successfully performed and that $H _ { j }$ is nonsingular, $x _ { j }$ is the exact solution if and only if $h _ { j + 1 , j } ~ = ~ 0$ .Note that the nonsingularity of $H _ { j }$ is no longer implied by the nonsingularity of $A$

# 6.2.9 - Orthogonal Tridiagonalization

The simultaneous solution of a linear system and its adjoint,

$$
A x \approx b , \qquad A ^ { H } y \approx c ,
$$

has interesting applications in design optimization, aeronautics,weather prediction,and signal processing; see Giles and Suli [471, 2002] and Montoison and Orban [800,202o]. More generally, let $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ , be rectangular. Applying two sequences of Householder transformations alternately on the left and right, we can compute an orthogonal tridiagonalization

$$
\left( \begin{array} { c c } { { 1 } } & { { } } \\ { { } } & { { U ^ { H } } } \end{array} \right) \left( \begin{array} { c c } { { 0 } } & { { c ^ { H } } } \\ { { b } } & { { A } } \end{array} \right) \left( \begin{array} { c c } { { 1 } } & { { } } \\ { { } } & { { V } } \end{array} \right) = \left( \begin{array} { c c } { { 0 } } & { { \gamma _ { 1 } e _ { 1 } ^ { T } } } \\ { { \beta _ { 1 } e _ { 1 } } } & { { U ^ { H } A V } } \end{array} \right) .
$$

The first transformation in each sequence is chosen to reduce $b$ and $c$ , respectively, to a multiple of $e _ { 1 }$ ,so that

$$
U ^ { H } b = \beta _ { 1 } e _ { 1 } , \qquad c ^ { H } V = \gamma _ { 1 } e _ { 1 } ^ { T } ,
$$

and hence $b = \beta _ { 1 } U e _ { 1 }$ and $c = \gamma _ { 1 } V e _ { 1 }$ . Later transformations are chosen to reduce $A$ to tridiagonal form

$$
U ^ { H } A V = \binom { T _ { n + 1 , n } } { 0 } , T _ { n + 1 , n } = \left( \begin{array} { r r r r r r } { \alpha _ { 1 } } & { \gamma _ { 2 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & { \gamma _ { 3 } } & & & \\ & { \ddots } & { \ddots } & { \ddots } & & \\ & & { \beta _ { n - 1 } } & { \alpha _ { n - 1 } } & { \gamma _ { n } } \\ & & & { \beta _ { n } } & { \alpha _ { n } } \\ & & & & { \beta _ { n + 1 } } \end{array} \right) \in \mathbb { R } ^ { ( n + 1 ) \times n } ,
$$

with nonnegative off-diagonal elements. (If $m = n$ , the last row of $T _ { n + 1 , n }$ is void.） Note that this transformation preserves the singular values of $A$

Knowing the existence of factorization (6.2.78), we can derive recurrence relations to com-pute the nonzero elements of the tridiagonal matrix $T _ { n + 1 , n }$ and the columns of $U$ and $V$ We already have $b = \beta _ { 1 } u _ { 1 }$ and $c = \gamma _ { 1 } v _ { 1 }$ ,so that $u _ { 1 } = b / \lVert b \rVert _ { 2 }$ and $v _ { 1 } = c / \lVert c \rVert _ { 2 }$ . Following Golub, Stoll,and Wathen [509, 20o8],we write

$$
\begin{array} { r } { A ( v _ { 1 } , \ldots , v _ { k } ) = ( u _ { 1 } , \ldots , u _ { k } , u _ { k + 1 } ) T _ { k + 1 , k } , } \\ { A ^ { H } ( u _ { 1 } , \ldots , u _ { k } ) = ( v _ { 1 } , \ldots , v _ { k } , v _ { k + 1 } ) T _ { k + 1 , k } ^ { H } . } \end{array}
$$

Comparing the last columns on both sides and solving for vectors $u _ { k + 1 }$ and $v _ { k + 1 }$ , respectively, gives

$$
\begin{array} { r l } & { \beta _ { k + 1 } u _ { k + 1 } = A v _ { k } - \alpha _ { k } u _ { k } - \gamma _ { k } u _ { k - 1 } , } \\ & { } \\ & { \gamma _ { k + 1 } v _ { k + 1 } = A ^ { H } u _ { k } - \alpha _ { k } v _ { k } - \beta _ { k } v _ { k - 1 } . } \end{array}
$$

Orthogonality gives $\alpha _ { k } = u _ { k } ^ { H } A v _ { k }$ , and the elements $\beta _ { k + 1 } > 0$ and $\gamma _ { k + 1 } > 0$ are determined as normalization constants.

Approximate solutions of $A x = b$ and $A ^ { H } y = c$ can be obtained in the form

$$
x _ { k } = V _ { k } z _ { k } , \qquad y _ { k } = U _ { k } w _ { k } .
$$

The norm of the residuals $r _ { k } = b - A V _ { k } z _ { k }$ and $s _ { k } = c - A ^ { H } U _ { k } w _ { k }$ at step $k$ are

$$
\begin{array} { l } { \| r _ { k } \| _ { 2 } = \| b - U _ { k + 1 } T _ { k + 1 , k } z _ { k } \| _ { 2 } = \| \beta _ { 1 } e _ { 1 } - T _ { k + 1 , k } z _ { k } \| _ { 2 } , } \\ { \| s _ { k } \| _ { 2 } = \| c - V _ { k + 1 } T _ { k + 1 , k } ^ { H } w _ { k } \| _ { 2 } = \| \gamma _ { 1 } e _ { 1 } - T _ { k , k + 1 } ^ { H } w _ { k } \| _ { 2 } . } \end{array}
$$

Determining $z _ { k }$ and $w _ { k }$ so that these residual norms are minimized is equivalent to solving two tridiagonal least squares problems. This ensures that the residual norms for both the prid $T _ { k + 1 , k }$ ennd $T _ { k , k + 1 } ^ { H }$   
Let $T _ { k + 1 , k } = Q _ { k } \widehat { R } _ { k }$ ，where $\widehat { R } _ { k }$ is upper triangular with three nonzero diagonals. The QR factors can be updated so that only one plane rotation is needed in each step. The rotations are applied also to the right-hand side. The solution $z _ { k }$ can then be obtained by back-substitution. Storing the whole bases $U _ { k }$ and $V _ { k }$ can be avoided. Let

$$
Q _ { k } ( T _ { k + 1 , k } ~ \beta _ { 1 } e _ { 1 } ) = \left( \begin{array} { c c } { { \widehat { R } _ { k } } } & { { f _ { k } } } \\ { { 0 } } & { { \bar { \phi } _ { k + 1 } } } \end{array} \right) ,
$$

so that $\widehat { R } _ { k } z _ { k } = f _ { k }$ , and define $C _ { k }$ from the triangular system $C _ { k } \widehat { R } _ { k } = V _ { k }$ . Then the solution can be updated as

$$
x _ { k } = V _ { k } z _ { k } = C _ { k } \widehat { R } _ { k } z _ { k } = C _ { k } f _ { k } = x _ { k - 1 } + \phi _ { k } c _ { k } .
$$

$T _ { k , k + 1 } ^ { H } w _ { k } = \gamma _ { 1 } e _ { 1 }$

From the recursion formulas (6.2.79)and (6.2.80) it can be seen that the vectors $u _ { k }$ and $v _ { k }$ lie in the union of two Krylov subspaces:

$$
\begin{array} { r l } & { u _ { 2 k } \in { \mathcal K } _ { k } ( A A ^ { H } , b ) \cup { \mathcal K } _ { k } ( A A ^ { H } , A c ) , \quad u _ { 2 k + 1 } \in { \mathcal K } _ { k + 1 } ( A A ^ { H } , b ) \cup { \mathcal K } _ { k } ( A A ^ { H } , A c ) , } \\ & { } \\ & { v _ { 2 k } \in { \mathcal K } _ { k } ( A ^ { H } A , c ) \cup { \mathcal K } _ { k } ( A ^ { H } A , A ^ { H } b ) , \quad v _ { 2 k + 1 } \in { \mathcal K } _ { k + 1 } ( A ^ { H } A , c ) \cup { \mathcal K } _ { k } ( A ^ { H } A , A ^ { H } b ) } \end{array}
$$

The tridiagonalization process is defined as long as no element $\beta _ { k }$ of $\gamma _ { k }$ becomes zero. If $\beta _ { k } = 0$ ， this signals that the solution of $A x = b$ can be recovered from the computed partial decomposition. Similarly, the solution of $A ^ { H } y = c$ can be obtained if $\gamma _ { k } = 0$ . Indeed, the process can be continued simply as follows. If $\beta _ { k } = 0$ , then in recurrence (6.2.80) we set $\beta _ { j } = 0$ ， $j > k$ Similarly, if $\gamma _ { k } = 0$ ,then in (6.2.79) we set $\gamma _ { j } = 0$ ， $j > k$ . Finally, note that if $c = 0$ , then all $\gamma _ { j }$ are zero, $T _ { n , n + 1 }$ is lower bidiagonal, and the process equals Bidiag1. Similarly, if $b = 0$ ,all $\beta _ { j }$ are zero,and $T _ { n , n + 1 }$ is upper bidiagonal.

# Notes and references

Parlett observed in 1987 that orthogonal tridiagonalization can be interpreted as a block Lanczos process for the Jordan-Wielandt matrix with initial vectors $\left( \begin{array} { l l } { 0 } & { b } \end{array} \right) ^ { T }$ and $\left( \begin{array} { l l } { c } & { 0 } \end{array} \right) ^ { T }$ . Orthogonal tridiagonalization of a square matrix $A$ with starting vectors $b$ and $c$ originated with Saunders, Simon,and Yip. This led to the iterative solvers USYMQR and USYMLQ for solving square $A x = b$ and $A ^ { H } = c$ simultaneously given in Saunders, Simon,and Yip [966,1988]. Reichel and Ye [918,2oo8] recognized that orthogonal tridiagonalization also applies to rectangular $A$ and named their associated solver GLSQR.For square $A x = b$ they show that the special choice $c = { \widehat { x } }$ ,where $\widehat { x }$ is an approximation to $x$ ,can improve convergence.

There are many possible generalizations of orthogonal tridiagonalization, with applications, e.g., to least squares problems with multiple right-hand sides and block bidiagonal decompositions.Plesinger [899,20o8] and Hnetynkova,Plesinger,and Strakos [633,2015] consider applications to core system theory and TLS problems.

# 6.3 - Preconditioners for Least Squares Problems

# 6.3.1 - Gauss-Seidel and SSOR Preconditioners

Finding good preconditioners for least squares problems is often difficult. Problems arise from a wide variety of sources and lack properties that make some techniques successful for linear systems arising from partial differential equations. Surveys of preconditioners for least squares problems are given by Bru et al. [183, 2o14] and Gould and Scott [520,2017].

Some simple preconditioners can be derived from some classic iterative methods. In Section 6.1.6 it was shown that the Chebyshev Semi-iterative (CSI) method can be used to accelerate the convergence of SSOR. A different interpretation of this is to view SSOR as a preconditioner for CSI. Let

$$
A ^ { T } A = L + D + L ^ { T }
$$

be the standard splitting with $L$ strictly lower triangular. The SSOR preconditioner corresponds to taking

$$
B = D ^ { - 1 / 2 } ( D + \omega L ^ { T } ) , \quad 0 \leq \omega < 2 .
$$

Note that $\omega = 0$ corresponds to diagonal scaling such that $A$ has columns of unit norm. The SSOR preconditioner can be implemented without explicitly forming $A ^ { T } A$ or $L$ The vectors $t = ( t _ { 1 } , \ldots , t _ { n } ) ^ { T } = B ^ { - 1 } p$ and $q = A B ^ { - 1 } p = q _ { 0 }$ can be computed simultaneously as follows. Set $q _ { n } = 0$ ,and for $j = n , n - 1 , \ldots , 1$ ,compute

$$
t _ { j } = \left( { d } _ { j } ^ { 1 / 2 } p _ { j } - \omega { a } _ { j } ^ { T } q _ { j } \right) / { d } _ { j } , \quad q _ { j - 1 } = q _ { j } + t _ { j } { a } _ { j } .
$$

The vector $s = ( s _ { 1 } , . . . , s _ { n } ) ^ { T } = B ^ { - T } A ^ { T } r$ is computed as follows. Set $h _ { 1 } = r$ ,and for $j =$ $1 , 2 , \ldots , n$ compute

$$
\begin{array} { r } { s _ { j } = a _ { j } ^ { T } h _ { j } / d _ { j } ^ { 1 / 2 } , \quad h _ { j + 1 } = h _ { j } - \omega ( d _ { j } ^ { - 1 / 2 } s _ { j } ) a _ { j } . } \end{array}
$$

Hence to apply the SSOR preconditioner, only one column of $A$ is needed at a time.The number of arithmetic operations per step approximately doubles when $\omega \neq 0$ ，compared to diagonal scaling ( $\omega = 0$ ). Evans [389,1g68] reports SSOR preconditioning for solving symmetric positive definite systems $A x = b$ as very promising. Jennings and Malik [665,1978] also consider Jacobi and SSOR-preconditioned CG methods.

Theory and numerical experiments indicate that the choice $\omega = 1$ is often close to optimal. However, the gain is usually small and often upset by the increased complexity of each itera-tion. Convergence may be affected by reordering the columns. Also,reordering may be used to introduce parallelism.

In many sparse least squares problems arising from multidimensional models, $A$ has a natural column block structure,

$$
A = \left( A _ { 1 } \quad A _ { 2 } \quad \ldots \quad A _ { N } \right) , \quad A _ { j } \in \mathbb { R } ^ { m \times n _ { j } } ,
$$

where $n _ { 1 } + \cdots + n _ { N } = n$ .A special example of such block structure is the block-angular form described in Section 4.3.2.For problems with the structure (6.3.5), block versions of the preconditioners (6.3.2)are particularly suitable.Let the QR factorizations of the blocks be

$$
A _ { j } = Q _ { j } R _ { j } , \quad Q _ { j } \in \mathbb { R } ^ { m \times n _ { j } } , \quad j = 1 , \dots , N .
$$

Then (6.3.2) with $\omega = 0$ corresponds to the block diagonal preconditioner

$$
B = R _ { B } = \mathrm { d i a g } ( R _ { 1 } , R _ { 2 } , \ldots , R _ { N } ) .
$$

For this choice we have $A B ^ { - 1 } = ( Q _ { 1 } , Q _ { 2 } , \ldots , Q _ { N } )$ ,i.e.,the columns of each block are orthonormal. If $A ^ { T } A$ is split according to $A ^ { T } A = L _ { B } + D _ { B } + L _ { B } ^ { T }$ ，where $L _ { B }$ is strictly lower block triangular, the block SSOR preconditioner becomes

$$
B = R _ { B } ^ { - 1 } ( D _ { B } + \omega L _ { B } ^ { T } ) ;
$$

see Bjorck [128,1979]. As with the corresponding point preconditioner, it can be implemented without forming $A ^ { T } A$

f $x$ and $y = B x$ are partitioned conformally with (6.3.7),

$$
\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , . . . , x _ { N } ) ^ { T } , \quad \boldsymbol { y } = ( y _ { 1 } , y _ { 2 } , . . . , y _ { N } ) ^ { T } ,
$$

then Jacobi's method (6.1.18) applied to the preconditioned problem (6.2.22) becomes

$$
y _ { j } ^ { ( k + 1 ) } = y _ { j } ^ { ( k ) } + Q _ { j } ^ { T } ( b - A B ^ { - 1 } y _ { k } ) , \quad j = 1 , \ldots , N ,
$$

or in terms of the original variables,

$$
\boldsymbol { x } _ { j } ^ { ( k + 1 ) } = \boldsymbol { x } _ { j } ^ { ( k ) } + \boldsymbol { R } _ { j } ^ { - 1 } \boldsymbol { Q } _ { j } ^ { T } ( { \boldsymbol { b } } - { \boldsymbol { A x } } _ { k } ) , \quad j = 1 , \ldots , N .
$$

Tiis tebmeeleqasotet $z _ { j } = x _ { j } ^ { ( k + 1 ) } -$ $x _ { j } ^ { ( k ) }$ solves the problem

$$
\operatorname* { m i n } _ { z _ { j } } \| A _ { j } z _ { j } - r ^ { ( k ) } \| _ { 2 } , \quad r ^ { ( k ) } = b - A x ^ { ( k ) } ,
$$

and these corrections can be computed in parallel. Often $Q _ { j }$ is not available and we have to use $Q _ { j } = A _ { j } R _ { j } ^ { - 1 }$ . This is equivalent to using the method of seminormal equations (2.5.26) for solving (6.3.1O). It can lead to some loss of accuracy,and a correction step is recommended unless all the blocks $A _ { j }$ are well-conditioned.

A block SOR methodfor the normalequations canbe derived similarly. Let $r _ { 1 } ^ { ( k ) } = b - A x _ { k }$ and for $j = 1 , \ldots , N$ compute

$$
x _ { j } ^ { ( k + 1 ) } = x _ { j } ^ { ( k ) } + \omega z _ { j } , \qquad r _ { j + 1 } ^ { ( k ) } = r _ { j } ^ { ( k ) } - \omega A _ { j } z _ { j } ,
$$

where $z _ { j }$ solves $\begin{array} { r } { \operatorname* { m i n } _ { z _ { j } } \| A _ { j } z _ { j } - r _ { j } ^ { ( k ) } \| _ { 2 } } \end{array}$ . Taking $\omega = 1$ in (6.3.11) gives the block GaussSeidel method.

To use the block SSOR preconditioner (6.3.8) for the_conjugate gradient method, we have to be able to compute vectors $q = A B ^ { - 1 } p$ and $s = B ^ { - T } A ^ { T } r$ efficiently, given $p$ and $r$ .The following algorithms for this generalize the point SSOR algorithms (6.3.3) and (6.3.4):

· Set $\boldsymbol q ^ { ( N ) } = 0$ and solve $B ( z _ { 1 } , \ldots , z _ { N } ) ^ { T } = p$ For $j = N , \dots , 2 , 1$ solve

$$
R _ { j } z _ { j } = p _ { j } - R _ { j } ^ { - T } A _ { j } ^ { T } q ^ { ( j ) } , \qquad q ^ { ( j - 1 ) } = q ^ { ( j ) } - A _ { j } z _ { j } .
$$

· Set $r ^ { ( 1 ) } = r$ and compute $\boldsymbol { s } = ( s _ { 1 } , \ldots , s _ { N } ) ^ { T }$ For $j = 1 , 2 , \dots , N$ ,solve

$$
R _ { j } ^ { T } s _ { j } = A _ { j } ^ { T } r ^ { ( j ) } , \qquad r ^ { ( j + 1 ) } = r ^ { ( j ) } - A _ { j } R _ { j } ^ { - 1 } s _ { j } .
$$

The choice of partitioning $A$ into blocks is important for the storage and computational efficiency of the methods.An important criterion is that it should be possible to compute the factorizations $A _ { j } = Q _ { j } R _ { j }$ (or at least the factors $R _ { j }$ ） without too much fill. Note that if $A _ { j }$ is

block diagonal, the computation of $z _ { j }$ in SOR splits into independent subproblems. This makes it possible to achieve efficiency through parallelization.

The case $N = 2$ ， $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right)$ is of special interest. For the block diagonal preconditioner (6.3.7) we have $\begin{array} { r } { B ^ { - 1 } = \left( \begin{array} { l l } { Q _ { 1 } } & { Q _ { 2 } } \end{array} \right) } \end{array}$ ,and the matrix of normal equations for the preconditioned system becomes

$$
( A B ^ { - 1 } ) ^ { T } A B ^ { - 1 } = \left( \begin{array} { c c } { { I } } & { { K } } \\ { { K ^ { T } } } & { { I } } \end{array} \right) , \quad K = Q _ { 1 } ^ { T } Q _ { 2 } .
$$

This matrix is consistently ordered. Hence,it is possible to reduce the work per iteration by approximately half for many iterative methods. This preconditioner is also called the cyclic Jacobi preconditioner.

For consistently ordered matrices,the SOR theory holds. Hence,as shown by Elfving [383, $1 9 8 0 ]$ , the optimal $\omega$ in the block SOR method (6.3.11) for $N = 2$ is

$$
\omega _ { \mathrm { o p t } } = 2 / ( 1 + \sin { \theta _ { \mathrm { m i n } } } ) , \qquad \cos { \theta _ { \mathrm { m i n } } } = \sigma _ { \mathrm { m a x } } ( Q _ { 1 } ^ { T } Q _ { 2 } ) ,
$$

where $\theta _ { \mathrm { m i n } }$ is the smallest principalangle between $\mathcal { R } ( A _ { 1 } )$ and $\mathcal { R } ( A _ { 2 } )$ .Block SOR with $\omega _ { \mathrm { o p t } }$ reduces the number of iterations by a factor of $2 / \sin \theta _ { \mathrm { m i n } }$ compared to $\omega = 1$

For $N = 2$ ,the preconditioner (6.3.8） with $\omega = 1$ has special properties; see Golub, Manneback,and Toint [500,1986]. From

$$
B = \left( \begin{array} { c c } { { R _ { 1 } } } & { { \omega Q _ { 1 } ^ { T } A _ { 2 } } } \\ { { 0 } } & { { R _ { 2 } } } \end{array} \right) ,
$$

it follows that for $\omega = 1$

$$
\left( A _ { 1 } \quad A _ { 2 } \right) B ^ { - 1 } = \left( Q _ { 1 } \quad ( I - P _ { 1 } ) Q _ { 2 } \right) ,
$$

where ${ P } _ { 1 } ~ = ~ { Q } _ { 1 } { Q } _ { 1 } ^ { T }$ is the orthogonal projector onto ${ \mathrm { R a n g e } } ( A _ { 1 } )$ .Hence the two blocks in (6.3.15) are mutually orthogonal,and the preconditioned problem (6.2.22) can be split into

$$
\begin{array} { r } { y _ { 1 } = Q _ { 1 } ^ { T } b , \quad \underset { y _ { 2 } } { \operatorname* { m i n } } \left\| ( I - P _ { 1 } ) Q _ { 2 } y _ { 2 } - b \right\| _ { 2 } . } \end{array}
$$

This effectively reduces the original problem to one of size $n _ { 2 }$ .Hence,this preconditioner is also called the reduced system preconditioner. The matrix of normal equations is

$$
( A B ^ { - 1 } ) ^ { T } A B ^ { - 1 } = \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { Q _ { 2 } ^ { T } ( I - P _ { 1 } ) Q _ { 2 } } } \end{array} \right) = I - \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { K ^ { T } K } } \end{array} \right) ,
$$

where $K = Q _ { 1 } ^ { T } Q _ { 2 }$ . This reduction of variables corresponding to the first block of columns can also be performed when $N > 2$

Manneback $[ 7 7 2 , 1 9 8 5 ]$ shows that for $N = 2$ the optimal choice with respect to the number of iterations is $\omega = 1$ ,i.e., the reduced system preconditioning. Further,as shown by Hageman, Luk,and Young [558,198o], the reduced system preconditioning is equivalent to cyclic Jacobi preconditioning ( $\omega = 0$ ）for Chebyshev semi-iteration and the conjugate gradient method. The reduced system preconditioning essentially generates the same approximations in half the number of iterations. Since the work per iteration is about doubled for $\omega \neq 0$ ,this means that cyclic Jacobi preconditioning is optimal for CG in the class of SSOR preconditioners.

The use of SSOR preconditioners for Krylov subspace methods was first proposed by Axelsson [47,1972]. SSOR-preconditioned CG methods for the least squares and least-norm problems are developed by Bjorck and Elfving [141,1979].Experimental results for block SSOR preconditioning with $N > 2$ are given by Bjorck [128,1979]. Tests show that the number of iterations required is nearly constant for values around $\omega = 1$ . For certain grid problems,a high degree of parallelism can be achieved. Kamath and Sameh [682, $1 9 8 9 ]$ give a scheme for a threedimensional $n \times n \times n$ mesh and a seven-point difference star,for which $N = 9$ and each block consists of $n ^ { 2 } / 9$ separate subblocks of columns. Hence each subproblem can be solved with a parallelism of $n ^ { 2 } / 9$

# Notes and references

Ordering algorithms based on graph theory are given by Dennis and Steihaug [317,1g86]. Golub, Manneback, and Toint [500,1g86] apply block SSOR-preconditioned CG to the Doppler positioning problem, for which the matrix has block-angular form． Morikuno and Hayami [812, 2013],[813,2o15] use one or several steps of SOR and SSOR as an inner iteration precondi-tioner for GMRES applied to the normal equations (see Section 4.3.2).

# 6.3.2 - Incomplete Cholesky and QR

Incomplete Cholesky (IC) factorizations are an important class of preconditioners for solving large sparse symmetric positive definite linear systems $C x = d$ In these methods,some fill ele-ments that would occur in the exact Cholesky factorization $C = L L ^ { T }$ are dropped. The resulting sparse approximate Cholesky factor is used as a preconditioner. This idea has yielded very effective solvers,especially for symmetric positive definite systems arising from finite-difference stencils. Note that if $L$ is the exact Cholesky factor, $L ^ { - T } C L ^ { - 1 } = I$ ,and CG converges in one step.

For least squares problems $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ , IC factorizations are used as right-preconditioners,and CGLS,LSQR,or LSMR is applied to $\mathrm { m i n } _ { y } \parallel A L ^ { - 1 } y - b \parallel _ { 2 }$ Let $L$ be a lower triangular IC factor of $C = A ^ { T } A$ such that

$$
C = L L ^ { T } - E , \quad \| E \| _ { 2 } / \| A \| _ { 2 } ^ { 2 } < \epsilon \ll 1 ,
$$

where $E$ is the residual matrix. It follows that $\| A L ^ { - 1 } - I \| _ { 2 } < \epsilon \kappa ( A ) ^ { 2 }$ , and we can expect rapid convergence. However, since $A ^ { T } A$ is often significantly denser than $A$ , it can be difficult to find a sufficiently sparse and effective IC preconditioner for least squares problems.

In the pioneering paper by Meijerink and van der Vorst [786,1977],an IC factorization for the class of symmetric M-matrices is shown to exist. More generally, IC factorizations exist when $C$ is an $_ \mathrm { H }$ -matrix but may fail for a general symmetric positive definite matrix because of a zero or negative pivot. Numerical instabilities can be expected if pivots have small magnitudes. To avoid breakdown,Manteuffel [774,198o] proposed factorizing a diagonally shifted matrix $C + \alpha I$ for some sufficiently large $\alpha > 0$ . This modification can be very effective, but its success depends critically on the choice of $\alpha$ . In general the only way to find a suitable $\alpha$ is by trial and error.

During the last fifty years, many variations of IC preconditioners have been developed. They differ in the strategies used to determine which elements are dropped.In a level-based IC method,the nonzero pattern of $L$ is based on the nonzero pattern of $C$ and prescribed in advance.A symbolic factorization is used to assign each fl entry a level. In an $\operatorname { I C } ( \ell )$ incomplete factorization,a nonzero element in $L$ is kept in the numerical factorization only if its level is at most $\ell$ .This has the advantage that the memory required for the preconditioner $L$ is known in advance. In an $\mathbf { I C } ( 0 )$ factorization, the nonzero structure of $L$ is the same as for the lower triangular part of $C$ .An $\mathrm { I C } ( 1 )$ factorization also includes any nonzeros directly introduced by the elimination of the level-zero elements.Higher-level incomplete factorizations are defined recursively. However, memory requirements may grow quickly as $\ell$ is increased.An improved strategy by Scott and Tüma [984,2o11] is to consider individual matrix elements and restrict contributions of small elements to fewer levels of fill than for larger elements.

Another widely used class of IC factorizations is called incomplete threshold $\mathrm { I C } ( \tau )$ factorization. In these, elements in the computed IC factor whose magnitude falls below a preset threshold $\tau$ are discarded. A choice of $\tau = 0$ will retain all elements, giving a complete Cholesky factorization of $C$ . It can be shown that a choice of $\tau = 1$ will cause all off-diagonal elements to be rejected and give a diagonal preconditioner. In practice,an intermediate value of $\tau$ in the interval [0.O1,0.02] is recommended by Ajiz and Jennings [13,1984]. Several of the above classes of IC factorizations are available in the ichol function supplied by MATLAB.

A suitable symmetric permutation $P C P ^ { T }$ can improve the performance of an IC factorization.When a drop tolerance is used,good orderings for direct methods,such as the minimum degree algorithm, can be expected to perform well because with these orderings fewer elements need to be dropped; see Munksgaard [815,198o]. Duff and Meurant [350,1989] study the effect of different ordering strategies on the convergence of CG when it is preconditioned by IC. They conclude that the rate of convergence is not related to the number of fill-ins that are dropped but rather almost directly related to the norm of the residual matrix $\| E \|$ .They show that several orderings that give a small number of fill-ins do not perform well when used with a level-zero or level-one incomplete factorization.

An alternative strategy to avoid breakdown of an IC factorization is proposed by Ajiz and Jennings [13, $\mathrm { 1 9 8 4 } ]$ ． To compensate for dropped off-diagonal elements,corrections are added to the diagonal elements. To delete the element $c _ { i j }$ ， $i \neq j$ ,a residual matrix $E _ { i j }$ with nonzero elements

$$
\left( \begin{array} { c c } { { c _ { i i } } } & { { - c _ { i j } } } \\ { { - c _ { j i } } } & { { c _ { j j } } } \end{array} \right)
$$

is added, where $c _ { i i } c _ { j j } - c _ { i j } ^ { 2 } \geq 0$ .Then $E _ { i j }$ is positive semidefinite,and the eigenvalues of the modified matrix $C + E _ { i j }$ cannot be smaller than those of $C$ .Hence if $C$ is positive definite and $E$ is the sum of such modifications, it follows that $C + E$ is positive definite, and the incomplete factorization cannot break down. In the algorithm of Ajiz and Jennings, modifications to $c _ { i i }$ and $c _ { j j }$ of equal relative magnitude are made,

$$
c _ { i i } = c _ { i i } + \rho | c _ { i j } | , \qquad c _ { j j } = c _ { j j } + ( 1 / \rho ) | c _ { i j } | ,
$$

where $\rho = \sqrt { c _ { i i } / c _ { j j } }$ . After all the off-diagonal elements in column $i$ have been computed, all additions are made to $c _ { i i }$ ,and

$$
r _ { i i } = \bigg ( c _ { i i } - \sum _ { k = 1 } ^ { i - 1 } r _ { k i } ^ { 2 } \bigg ) ^ { 1 / 2 } , \qquad r _ { i j } = c _ { i j } ^ { * } / r _ { i i } , \quad j > i .
$$

A difficulty with threshold Cholesky factorization is that the amount of storage needed to hold the factorization for a given $\tau$ cannot be determined in advance.One solution is to stop and restart with a larger value of $\tau$ if the allocated memory does not suffice.Alternatively, only the $p$ largest off-diagonal elements in each column of $L$ can be kept, for some parameter $p$ .Lin and Moré [748,1999] use no drop tolerance and retain the $n _ { j } + p$ largest elements in the $j$ th column of $L$

Tismenetsky [1065,1991] proposes a different modification scheme. Intermediate memory is used during construction of the preconditioner $L$ but then discarded.A decomposition of the form

$$
\begin{array} { r } { C = ( L + R ) ( L + R ) ^ { T } = L L ^ { T } + L R ^ { T } + R L ^ { T } + E } \end{array}
$$

is used,where $L$ is lower triangular with positive diagonal elements,and $R$ is strictly lower triangular. The matrix $L$ is used as a preconditioner,and $R$ is used to stabilize the factorization process. The residual matrix has the positive semidefinite form $E = R R ^ { T }$ . At step $j$ ,the first column of the $j$ th Schur complement can be decomposed as the sum $l _ { j } + r _ { j }$ ，where $l _ { j } ^ { T } r _ { j } = 0$ In a right-looking implementation, the Schur complement is updated by subtracting $E _ { j } = ( l _ { j } +$ $r _ { j } ) ( l _ { j } + r _ { j } ) ^ { T }$ ，where $r _ { j }$ is not retained in the incomplete factorization. Hence,at step $j$ the positive semidefinite modification $r _ { j } r _ { j } ^ { T }$ is implicitly added to $A$ ，which prevents breakdowns. Tismenetsky takes $r _ { j }$ as the vector of off-diagonal elements that are smaller than a chosen drop tolerance.The good performance of Tismenetsky's preconditioner is partly explained by the form of the error matrix that depends on the square of the elements in $R$ The fill in $L$ can be controlled by the choice of drop tolerance.The most serious drawback is that the total memory requirement needed to compute $L$ can be prohibitively high.

Kaporin [684,1998] modifies Tismenetsky's method in several respects. A left-looking algorithm is used,and the memory requirement is controlled by using two tolerances. Elements larger than $\tau _ { 1 }$ are kept in $L$ ,and those smaller than $\tau _ { 2 }$ are dropped from $R$ ，The error matrix now has the structure

$$
\boldsymbol { E } = \boldsymbol { R } \boldsymbol { R } ^ { T } + \boldsymbol { F } + \boldsymbol { F } ^ { T } ,
$$

where $F$ is a strictly lower triangular matrix that is not computed. Kaporin's method is not breakdown-free and has to be stabilized,e.g.,by restarting the factorization after a diagonal shift $A : = A + \alpha I$ ，More than one restart may be required.

Further developments of the Tismenetsky-Kaporin method are proposed by Scott and Tüma [986, 2014]. Memory is limited by using two extra parameters lsize and rsize to control the maximal number of fill elements in each column of $L$ and $R$ ,respectively. The lsize largest elements are kept in $l _ { j }$ provided they are at least $\tau _ { 1 }$ in magnitude,and the rs ize largest elements are in $r _ { j }$ provided they are at least $\tau _ { 2 }$ in magnitude.An implementation MI28 is described in Scott and Tuma [985,2O14], where extensive test are described on a large set of problems from the SuiteSparse collection. The code is available as part of the HSL Mathematical Software Library; see www.hsl.rl.ac.uk.

As described in Section 2.5.3, iterative refinement (IR) can be regarded as a preconditioned iterative method, where the preconditioner is the full factor $\bar { R }$ computed from Cholesky of $A ^ { T } A$ (or a QR factorization of $A$ )，possibly in lower precision．The iteration method in IR is the simple power method. This can require several iterations to converge,and often some other iterative solver such as CGLS can be used with advantage. Zhang and $\mathrm { W u }$ [1147, 2019] use a QR factorization in IEEE half precision as a preconditioner for CGLS to achieve high accuracy least squares solutions on GPUs.

By Theorem 2.1.2, the computed ful Cholesky factorization satisfies

$$
\bar { R } ^ { T } \bar { R } = A ^ { T } A + E , \quad \| E \| _ { 2 } < 2 . 5 n ^ { 3 / 2 } { \bf u } \| A \| _ { 2 } ^ { 2 }
$$

provided $2 n ^ { 3 / 2 } { \bf u } \kappa ( A ) ^ { 2 } < 0 . 1$ Hence,

$$
\| A \bar { R } ^ { - 1 } - I \| < 2 . 5 n ^ { 3 / 2 } { \bf u } \kappa ( A ) ^ { 2 } ,
$$

and with $\bar { R }$ as a preconditioner, CGLS or LSQR willconverge rapidly.

Bellavia, Gondzio,and Morini [97,2o13] discuss a new class of limited-memory preconditioners for CGLS for solving weighted large-scale least squares problems arising in optimization. The largest eigenvalues of the symmetric positive definite normal equation matrix $H$ are identified by a partial Cholesky factorization ${ \boldsymbol { P } } = L { \boldsymbol { L } } ^ { T }$ that uses only a few columns corre-sponding to the largest diagonal elements of $H$ . This is used as a preconditioner to reduce the condition number of $H$ . The smallest eigenvalues of $H$ are handled by the deflated CG algorithm of Saad et al. [961, 2ooo]; see Section 6.4.6. This requires computing approximate eigenvectors corresponding to some of the smallest eigenvalues of the preconditioned matrix $P ^ { - 1 } H$ by a Rayleigh-Ritz procedure.

Myre et al. [816, 2018] use CGLS preconditioned with the computed complete Cholesky factorization to solve dense least squares problems.They calltheir algorithm TNT because it is a “dynamite method"(!). For problems in rock magnetism with tens of thousands of variables it outperformed other tested methods,including dense QR factorizatin.

Alternatively,an incomplete factor $R$ can be generated by modifying a QR factorization of $A$ ． This normally involves more computation but is less subject to the effect of rounding errors. Jennings and Ajiz [664, $\mathrm { 1 9 8 4 } ]$ describe an incomplete modified Gram-Schmidt (IMGS) factorization in which the magnitude of each off-diagonal element $r _ { i j }$ is compared against a chosen drop tolerance $\tau$ ，scaled by the norm of the corresponding column in $A = \left( a _ { 1 } , \ldots , a _ { n } \right)$ That is,elements in $R$ such that

$$
| r _ { i j } | < \tau d _ { j } , \quad d _ { j } = \| a _ { j } \| _ { 2 } , \quad j = 1 , \ldots , n ,
$$

are dropped. If $\tau = 0$ ,all elements in $R$ are retained,and the MGS process is complete. If $\tau = 1$ ， all off-diagonal elements in $R$ are dropped, thus making $R$ diagonal. In IMGS factorization the preconditioner $R$ is formed by the coefficients in a series of vector orthogonalizations, and $A$ is converted into $Q$

# Algorithm 6.3.1 (IMGS Factorization).

$$
r _ { i i } = \| a _ { i } \| _ { 2 } ; ~ q _ { i } : = a _ { i } / r _ { i i } ; ~
$$

$$
r _ { i j } : = q _ { i } ^ { T } a _ { j } ;
$$

$$
\mathrm { e l s e } a _ { j } : = a _ { j } - r _ { i j } q _ { i }
$$

If $A$ has full column rank, the IMGS algorithm cannot break down. Column $a _ { j }$ is only modified by subtracting a linear combination of previous columns $a _ { 1 } , \dotsc , a _ { j - 1 }$ and cannot vanish. Therefore,we have at each stage $A = { \hat { Q } } { \hat { R } }$ ，where $\hat { Q }$ is orthogonal, and upper triangular $\hat { R }$ has positive diagonal elements. Normalization will give a nonzero $q _ { j }$ ,and the process can be continued. A drawback of IMGS is that for a sparse $A$ , the intermediate storage requirement can be much larger than for the final preconditioner $\hat { R }$

Wang [1101，1993] (see also Wang,Gallivan,and Bramley [1102,1997l) gives a compressed algorithm (CIMGS） for computing the IMGS preconditioner. CIMGS is similar to an incomplete Cholesky factorization. In exact arithmetic, it can be shown to produce the same incomplete factor $R$ for $C = A ^ { T } A$ as IMGS.Thus it inherits the robustness of IMGS. CIMGS is also equivalent to Tismenetsky's IC decomposition applied to the matrix $A ^ { T } A$ ; see Bru et al. [183,2014].

# Algorithm 6.3.2 (CIMGS).

for $i = 1 , 2 , \dots , n$   
$r _ { i i } = \sqrt { c _ { i i } } ;$ for $j = i + 1 , \ldots , n$ $c _ { i j } = c _ { i j } / r _ { i i } ;$ if $( i , j ) \notin P$ then $r _ { i j } = 0$ else $r _ { i j } = c _ { i j }$ ; end end for $j = i + 1 , \ldots , n$ for $k = i + 1 , \ldots , n$ if $( i , j ) \in P$ or $( i , k ) \in P$ then $c _ { k j } = c _ { k j } - c _ { i k } * c _ { i j } \mathrm { ~ e n d }$ end end   
end

Jennings and Ajiz [664, $\mathrm { 1 9 8 4 } ]$ also consider an incomplete Givens QR factorization. The rows of $A$ are processed sequentially. The nonzero elements in the $i$ th row $( a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } )$ are scanned,and each nonzero element $a _ { i j }$ is annihilated by a plane rotation involving row $j$ in $R$ A rotation to eliminate an element in $A$ is skipped if

$$
| a _ { i j } | < \tau \| a _ { j } \| _ { 2 } ,
$$

where $a _ { j }$ is the $j$ th column of $A$ . If such an element $a _ { i j }$ were simply discarded, the final incomplete factor $R$ would become singular. Instead, these elements are rotated into the diagonal element $r _ { j j }$ by setting

$$
r _ { j j } = \sqrt { r _ { j j } ^ { 2 } + a _ { i j } ^ { 2 } } .
$$

This guarantees that $R$ is nonsingular and that the residual matrix $E = A ^ { T } A - R ^ { T } R$ has zero diagonal elements.

Zlatev and Nielsen [1153,1988] compute sparse incomplete QR factors of $A$ by discarding computed elements that are smaller than a drop tolerance $\tau \geq 0$ .The initial tolerance is succes-sively reduced if the iterative solver converges too slowly. This approach can be very efficient for some classes of problems, especially when storage is a limiting factor.

A different dropping criterion suggested by Saad [953,1g88] is to keep the $p _ { R }$ largest elements in a row of $R$ and the $p _ { Q }$ largest elements in a column of $Q$ . The sparsity structure of $R$ can also be limited to a prescribed index set $P$ ,as in the incomplete Cholesky algorithm. This version can be obtained from Algorithm 6.3.1 by modifying it so that $r _ { i j } = 0$ when $( i , j ) \notin P$

A multilevel incomplete Gram-Schmidt QR (MIQR) preconditioner is given by Li and Saad [741,2oo6]. This exploits the fact that when a matrix is sparse,many of its columns will be orthogonal because of their structure. The algorithm first finds a set of structurally orthogonal columns in $A$ and permutes them into the first positions $A _ { 1 } = \left( a _ { 1 } , \ldots , a _ { k } \right)$ . Normalizing these columns gives $A _ { 1 } = Q _ { 1 } D _ { 1 }$ ,with $Q _ { 1 }$ orthogonal. The remaining columns $A _ { 2 }$ are then orthogonalized against the first set, giving $B = A _ { 2 } - Q _ { 1 } F _ { 1 }$ and the partial QR factorization

$$
A P _ { 1 } ^ { T } = \left( Q _ { 1 } B \right) \left( { D _ { 1 } } F _ { 1 } \right) ,
$$

where $F _ { 1 }$ is usually sparse and has structurally independent columns. Hence, the process can be repeated recursively on $B$ until the reduced matrix is small enough or no longer suficiently

sparse. This orthogonalization process can be turned into an incomplete QR factorization by relaxing the orthogonality and applying dropping strategies.

# 6.3.3 - Approximate Inverse Preconditioners

Preconditioners based on incomplete LU or Cholesky factorization have the disadvantage that they are implicit, i.e., their application requires the solution of a linear system. Therefore they can be difficult to implement efficiently. For a nonsingular system $A x = b$ ,an alternative is to compute an explicit sparse approximate inverse (SPAI) preconditioner $M$ such that $M \approx A ^ { - 1 }$ Application of such a preconditioner is a matrix-vector operation and therefore amenable to parallelization.

It is not clear if a good sparse approximate inverse of a sparse matrix $A$ exists, given that the inverse of a sparse irreducible matrix in general has no zero elements.For example, the inverse of an irreducible band matrix $A \in \mathbb { R } ^ { n \times n }$ is dense. However, if $A$ is strongly diagonally dominant, an SPAI preconditioner consisting of the main diagonal and a few other diagonals can be very efficient.

An SPAI preconditioner can be found by considering the constrained optimization problem

$$
\operatorname* { m i n } _ { M \in { \mathcal G } } \| I - A M \| _ { F } ,
$$

where $M$ is allowed to have nonzero elements only in a subset $\mathcal { G }$ of indices $( i , j ) , 1 \leq i , j \leq n$ ， and $\| \cdot \| _ { F }$ is the Frobenius matrix norm. If $m _ { j }$ is the $j$ th column of $M$ ,then

$$
\lVert I - A M \rVert _ { F } ^ { 2 } = \sum _ { j = 1 } ^ { n } \lVert e _ { j } - A m _ { j } \rVert _ { 2 } ^ { 2 } .
$$

The optimization problem reduces to solving $n$ independent least squares subproblems min $\| e _ { j } -$ $A m _ { j } \| _ { 2 } ^ { 2 }$ for $m _ { j }$ subject to the sparsity constraints on $m _ { j }$ . Rows with no nonzero elements can be discarded. Thus,when $M$ is constrained to be a sparse matrix the least squares subproblems are of small dimension. A simple method for solving the subproblems is coordinate descent on the function

$$
\begin{array} { r } { \frac 1 2 \| r _ { j } \| _ { 2 } ^ { 2 } , \quad r _ { j } = e _ { j } - A m _ { j } . } \end{array}
$$

Chow and Saad [247,1998] reduce the cost of computing the SPAI by using a few steps of an iterative method to reduce the residuals for each column.

For matrices with a general sparsity pattern it is difficult to prescribe a good nonzero pattern for $M$ For $A \in \mathbb { R } ^ { n \times n }$ a common choice is to let $M$ have the same sparsity structure as $A$ . Therefore,adaptive strategies have been developed. These start with a simple initial guess for the sparsity patern (for example, a diagonal structure) and successively augment this until some criterion is satisfied.The algorithm by Grote and Huckle [544,1997] is one of the most successful of these.A detailed discussion is given in Benzi[1O6,2002].

For a least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ of full column rank,we could seek an SPAI for the normal equations matrix $C = A ^ { T } A$ . Several algorithms for computing a SPAI for posi-tive definite systems have been suggested. Two basic types can be distinguished, depending on whether the preconditioner is expressed as a single matrix $M \approx C ^ { - 1 }$ or as the product of two or more matrices.For use with CGLS a symmetric positive definite preconditioner $M$ is required. Symmetry can be achieved by using the symmetric part $\begin{array} { r } { \frac { 1 } { 2 } ( M ^ { T } + M ) } \end{array}$ of $M$ . Regev and Saunders [915, 2022] give a modified PCGLS method that detects indefiniteness or near singularity of $M$ and restarts PCGLS with a more positive definite preconditioner.

Another way of computing an approximate inverse is by a procedure related to the bicon-jugation algorithm of Fox [429,1964]. Given a symmetric positive definite matrix $C$ and a set of linearly independent vectors $w _ { 1 } , w _ { 2 } , \ldots , w _ { n } \in \mathbb { R } ^ { n }$ , the AINV algorithm constructs a set of $C$ -conjugate vectors $z _ { 1 } , z _ { 2 } , \ldots , z _ { n } \in \mathbb { R } ^ { n }$ using a modified Gram-Schmidt orthogonalization process; se Benzi, Meyer,and Tima[109,1996]. The algorithm sets $z _ { i } ^ { ( 0 ) } = w _ { i }$ and then iterates

$$
z _ { i } ^ { ( j ) } : = z _ { i } ^ { ( j - 1 ) } - \frac { ( z _ { j } ^ { ( j - 1 ) } ) ^ { T } C z _ { i } ^ { ( j - 1 ) } } { ( z _ { j } ^ { ( j - 1 ) } ) ^ { T } C z _ { j } ^ { ( j - 1 ) } } z _ { j } ^ { ( j - 1 ) } ,
$$

where $j = 1 : n - 1$ and $i = j + 1 : n$ With $z _ { i } = z _ { i } ^ { ( i - 1 ) }$ and $Z = ( z _ { 1 } , z _ { 2 } , \ldots , z _ { n } )$ , we now have $z _ { i } ^ { T } C z _ { j } = 0$ ， $i \neq j$ ,and

$$
Z ^ { T } C Z = D = \operatorname { d i a g } { \big ( } d _ { 1 } , \ldots , d _ { n } { \big ) } ,
$$

where

$$
d _ { j } = z _ { j } ^ { T } C z _ { j } > 0 , \quad 1 \leq j \leq n .
$$

In exact arithmetic,the process can be completed without encountering zero divisors if and only if all the leading principal minors of $C$ are symmetric positive definite. In this case the matrix $Z ^ { T } = L ^ { - 1 }$ is unit lower triangular. By uniqueness, $C = L D L ^ { T }$ is the square-root-free Cholesky factorization.

Applications to sparse least squares problems are considered by Benzi and Tuma[110, 2003l, [111, 2003]. Setting $C = A ^ { T } A$ ,we have

$$
z _ { j } ^ { T } C z _ { i } = ( A z _ { j } ) ^ { T } ( A z _ { i } ) .
$$

Hence (6.3.20) does not require $C$ explicitly. For a typical sparse $A$ ,most of the inner products will be structurally zero （ $( A z _ { j }$ and $A z _ { i }$ will have no nonzeros in the same positions). Incom-pleteness canbeimposed bydropping elements in $Z$ The elements of $z _ { i } ^ { ( j ) }$ are scanned after each update,and those smaller in absolute value than a drop tolerance $\tau \in ( 0 , 1 )$ are discarded. Alternatively, a prescribed nonzero structure on $Z$ can be enforced to give a factorized SPAI of the form

$$
( A ^ { T } A ) ^ { - 1 } \approx \bar { Z } \bar { D } ^ { - 1 } \bar { Z } ^ { T } , \qquad \bar { D } \mathrm { i s d i a g o n a l } .
$$

Since the elements $\bar { d } _ { j } = \| A \bar { z _ { j } } \| _ { 2 } ^ { 2 }$ are positive, such a preconditioner is always symmetric positive lefinite.

The process (6.3.20) produces not only $L ^ { - 1 }$ but also $L$ at no extra cost. It holds that

$$
l _ { i j } = \frac { ( z _ { j } ^ { ( j - 1 ) } ) ^ { T } C z _ { i } ^ { ( j - 1 ) } } { ( z _ { j } ^ { ( j - 1 ) } ) ^ { T } C z _ { j } ^ { ( j - 1 ) } } z _ { j } ^ { ( j - 1 ) } , \quad i > j .
$$

The vector $z _ { i }$ is discarded as soon as it has been used to form the corresponding parts of $L =$ $( l _ { i j } )$ . Recall that in the first version, the multipliers $l _ { i j }$ are discarded and $z _ { i }$ are kept. Dropping elements of $z _ { i } ^ { ( j ) }$ as above gives an incomplete Cholesky factorization

$$
C = A ^ { T } A \approx \bar { L } \bar { D } ^ { - 1 } \bar { L } ^ { T } .
$$

If $A$ has full column rank, the pivots $\bar { d } _ { j } = \| A \bar { z _ { j } } \| _ { 2 } ^ { 2 }$ are guaranteed to be positive. Hence the preconditioner (6.3.23) is positive definite.

# Notes and references

Preconditioners for augmented systems are developed by Scott and Tüma [985, 2o14]. A survey of methods based on incomplete QR factorization is given by Bai,Duff,and Wathen [64,2001]. Papadoupolos, Duff,and Wathen [877, 2oo5] discuss implementations and give many practical results. Scott and Tuma [987,2o16] develop preconditioners by robust incomplete factorization (RIF). Cholesky-based factorizations for rank-deficient problems are given by Scott [983, 2017].

# 6.3.4 - Submatrix Preconditioners

An important class of preconditioners for the least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ is based on selecting a subset of rows from $A \in \mathbb { R } ^ { m \times n }$ forming a submatrix $A _ { 1 }$ of full column rank. If the selected rows are permuted to the top, the least squares problem becomes

$$
\operatorname* { m i n } _ { x } \left\| \left( { A _ { 1 } } _ { \right) } x - \left( { b _ { 1 } } _ { \right) } \right\| , \quad A _ { 1 } \in \mathbb { R } ^ { m _ { 1 } \times n } .
$$

Läuchli [724,1961] was the frst to use CGLS with $A _ { 1 }$ as a preconditioner for solving (6.3.24). He took $A _ { 1 }$ to be square and nonsingular and solved the preconditioned problem $\operatorname* { m i n } _ { x }$ $\parallel A A _ { 1 } ^ { - 1 } y -$ $b \Vert _ { 2 }$ ， $y = A _ { 1 } x$ or, equivalently,

$$
\operatorname* { m i n } _ { y } \left\| \left( \begin{array} { l } { I } \\ { C } \end{array} \right) y - \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \end{array} \right) \right\| _ { 2 } , \quad C = A _ { 2 } A _ { 1 } ^ { - 1 } \in \mathbb { R } ^ { m _ { 2 } \times n } ,
$$

with normal equations

$$
( I _ { n } + C C ^ { T } ) y = b _ { 1 } + C ^ { T } b _ { 2 } .
$$

Läuchli used Gauss-Jordan elimination with complete pivoting to form $C$ explicitly. This can be avoided by computing the LU factorization of $A$ with an efficient sparse LU factorization code and then implementing the matrix-vector products as

$$
\begin{array} { r } { C p = A _ { 2 } ( A _ { 1 } ^ { - 1 } p ) , \qquad C ^ { T } t = A _ { 1 } ^ { - T } ( A _ { 2 } ^ { T } t ) . } \end{array}
$$

# Algorithm 6.3.3 (LU Preconditioned CGLS I).

Initialize: $r _ { 0 } = b _ { 1 } , \ t _ { 0 } = b _ { 2 } , \ p _ { 0 } = s _ { 0 } = r _ { 0 } + C ^ { T } t _ { 0 } , \ \gamma _ { 0 } = \| s _ { 0 } \| _ { 2 } ^ { 2 } .$

for $k = 0 , 1 , 2 , \ldots$ while $\gamma _ { k } > \tau$ do

$$
\begin{array} { r l } & { q _ { k } = C p _ { k } , } \\ & { \alpha _ { k } = \gamma _ { k } / ( \| p _ { k } \| _ { 2 } ^ { 2 } + \| q _ { k } \| _ { 2 } ^ { 2 } ) , } \\ & { r _ { k + 1 } = r _ { k } - \alpha _ { k } p _ { k } , } \\ & { t _ { k + 1 } = t _ { k } - \alpha _ { k } q _ { k } , } \\ & { s _ { k + 1 } = r _ { k + 1 } + C ^ { T } t _ { k + 1 } , } \\ & { \gamma _ { k + 1 } = \| s _ { k + 1 } \| _ { 2 } ^ { 2 } , } \\ & { \beta _ { k } = \gamma _ { k + 1 } / \gamma _ { k } , } \\ & { p _ { k + 1 } = s _ { k + 1 } + \beta _ { k } p _ { k } ; } \end{array}
$$

At termination, $x _ { k }$ is retrieved from $A _ { 1 } x _ { k } = b _ { 1 } - t _ { k }$ ，The convergence of Algorithm 6.3.3 has been studied by Freund [433,1987]. The eigenvalues of $I _ { n } + C ^ { T } C$ are $\lambda _ { i } = 1 + \sigma _ { i } ^ { 2 } ( C )$ ， $i = 1 , \ldots , n$ ,where $\sigma _ { i }$ are the singular values of $C$ .It follows that

$$
\kappa ( A A _ { 1 } ^ { - 1 } ) \leq \sqrt { 1 + \sigma _ { 1 } ^ { 2 } ( C ) } ,
$$

where $\sigma _ { 1 } ( C ) = \| C \| _ { 2 } = \| A _ { 2 } A _ { 1 } ^ { - 1 } \| _ { 2 }$ . From (6.2.18) we obtain the following upper bound for the rate of convergence:

$$
\| A ( x - x _ { k } ) \| _ { 2 } \leq 2 \biggl ( \frac { \sigma _ { 1 } } { 1 + \sqrt { 1 + \sigma _ { 1 } ^ { 2 } } } \biggr ) ^ { 2 k } \| A ( x - x _ { 0 } ) \| _ { 2 } .
$$

Fast convergence is obtained when $\sigma _ { 1 }$ is small, e.g., when $A _ { 1 }$ is well-conditioned and $\| A _ { 2 } \| _ { 2 }$ is small. Because $C$ has at most $m _ { 2 } = m - n$ distinct singular values,the iterations will terminate in at most $m _ { 2 }$ steps,assuming exact arithmetic. Rapid convergence can be expected if $m _ { 2 }$ is small.

Subset preconditioners can also be constructed from QR factorization. Let $A _ { 1 } \in \mathbb { R } ^ { m _ { 1 } \times n }$ ， $m _ { 1 } \geq n$ , be a subset of rows in $A \in \mathbb { R } ^ { m \times n }$ such that $A _ { 1 }$ has full column rank. Assume that the QR factorization

$$
Q _ { 1 } ^ { T } \left( A _ { 1 } P \quad b _ { 1 } \right) = { \binom { R _ { 1 } \quad c _ { 1 } } { 0 } }
$$

is known, where $P$ is a sparsity-preserving column permutation. Then $R _ { 1 } \in \mathbb { R } ^ { n \times n }$ can be used as a preconditioner to solve $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ .The least squares problem is equivalent to

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { c } { R _ { 1 } } \\ { A _ { 2 } P } \end{array} } \right) y - \left( { \begin{array} { c } { c _ { 1 } } \\ { b _ { 2 } } \end{array} } \right) \right\| .
$$

Setting $x = R _ { 1 } ^ { - 1 } y$ and suppressing the column permutation gives the preconditioned problem

$$
\operatorname* { m i n } _ { y } \left\| \left( \begin{array} { l } { I _ { n } } \\ { C } \end{array} \right) y - \left( \begin{array} { l } { c _ { 1 } } \\ { b _ { 2 } } \end{array} \right) \right\| _ { 2 } , \quad C = A _ { 2 } R _ { 1 } ^ { - 1 } \in \mathbb { R } ^ { m _ { 2 } \times n } ,
$$

which has the same form as (6.3.25).

The choice of rows forming $A _ { 1 }$ is decisive for the efficiency of subset preconditioning. When $A$ is sparse, a good basis $A _ { 1 }$ may be obtained from a sparse LU factorization of $A$ (where it is important that $L$ be well-conditioned).A preliminary pass through the rows of $A$ can be made to select a subset with maximal diagonal elements; see Duff and Koster [348, 2oo1]. In some problems a natural selection may follow from the structure of $A$ .Plemm0ns [898,1979] shows that for some geodetic applications, $A _ { 1 }$ can be chosen during collection of the data.

In the Peters-Wilkinson method (Section 2.2.6), LU factorization with row pivoting is used to compute a factorization

$$
\Pi A = { \binom { A _ { 1 } } { A _ { 2 } } } = L U = { \binom { L _ { 1 } } { L _ { 2 } } } U ,
$$

where $U \in \mathbb { R } ^ { n \times n }$ is upper triangular, and $\boldsymbol { L } \in \mathbb { R } ^ { m \times n }$ is unit lower trapezoidal with bounded off-diagonal elements.(If $A$ is sparse, the row permutation $\Pi$ and also a column permutation preserve the sparsity of $L$ and $U$ while bounding the elements of $L$ ）With $A _ { 1 }$ as right preconditioner, we have

$$
C = A _ { 2 } A _ { 1 } ^ { - 1 } = L _ { 2 } L _ { 1 } ^ { - 1 } .
$$

A matrix-vector multiply can be performed as $\begin{array} { r } { C v = L _ { 2 } ( L _ { 1 } ^ { - 1 } v ) } \end{array}$

If the pivoting strategy maintains $| L _ { i j } | \le \tau$ for some $\tau \in [ 1 , 4 ]$ ,say,any ill-conditioning in $A$ will usually be reflected in $U$ . Hence $U$ can be used as a right preconditioner. This approach, suggested by Bjorck [127,1976], has the advantage that the lower triangular factor $L$ need not be stored,and the additional work per iteration depends only on the density of $U$ . Saunders [964, 1979] used a rowwise elimination with a preliminary pass through the rows to select a triangular subset with maximal diagonal elements. Subsequent use of the operator $A U ^ { - 1 }$ involves only back-substitutions with $U$ and multiplications with $A$ When $A$ has many more rows than columns it may be preferable to factorize only $A _ { 1 } = L _ { 1 } U _ { 1 }$ and operate with $C = A _ { 2 } ( L _ { 1 } U _ { 1 } ) ^ { - 1 }$ in CGLS.

For sparse problems,a standard pivoting strategy in LU factorization is to choose a pivot $a _ { i j }$ that minimizes the product of the number of nonzeros in its row and column. The product is called the Markowitz merit function and bounds the number of fil-ins that can occur during an elimination. For the purpose of stability, $a _ { i j }$ is required to satisfy

$$
| a _ { i j } | \geq u \operatorname* { m a x } _ { k } | a _ { k j } | ,
$$

where $u$ is a threshold parameter in the range $0 < u \leq 1$ .Taking $u$ in the range $0 . 1 \leq u \leq 0 . 9$ (not too small) normally keeps $L$ well-conditioned while promoting some degree of sparsity. This is threshold partial pivoting. Threshold rook pivoting and threshold complete pivoting are also implemented in LUSOL (Gill et al. [475,2oo5l) to balance stability and sparsity more carefully for demanding cases.

In a related approach, Howell and Baboulin 647,2o16] use LU factorization with partial pivoting and apply CGLS to

$$
\operatorname* { m i n } \| L y - b \| , \quad U x = y .
$$

The problem is often sufficiently well-conditioned to give rapid convergence. In their MIQR algorithm, Li and Saad [741, 2oo6] further precondition $L$ using incomplete QR factors.

Problem (6.3.25) can be writen in augmented form as

$$
r _ { 1 } + y = b _ { 1 } , \quad r _ { 2 } + C y = b _ { 2 } , \quad r _ { 1 } + C ^ { T } r _ { 2 } = 0 .
$$

Eliminating $r _ { 1 }$ from the first and third equations gives $y = b _ { 1 } + C ^ { T } r _ { 2 }$ ,and then using the second equation yields the symmetric positive definite system

$$
( C C ^ { T } + I _ { m - n } ) r _ { 2 } = b _ { 2 } - C b _ { 1 }
$$

of size $( m - n ) \times ( m - n )$ . This can be interpreted as the normal equations for the least squares problem

$$
\operatorname* { m i n } _ { r _ { 2 } } \left\| \left( { \begin{array} { c } { - C ^ { T } } \\ { I _ { m _ { 2 } } } \end{array} } \right) r _ { 2 } - \left( { \begin{array} { c } { b _ { 1 } } \\ { b _ { 2 } } \end{array} } \right) \right\| .
$$

When $m _ { 2 }$ is sufficiently smal, problem (6.3.35) can be solved by QR factorization. Applying CGLS to (6.3.35) yields the following algorithm; see Bjorck and Yuan [153,1999].

# Algorithm 6.3.4 (LU Preconditioned CGLS II).

$$
r _ { 0 } = b _ { 1 } , \ t _ { 0 } = b _ { 2 } , \ p _ { 0 } = s _ { 0 } = t _ { 0 } - C r _ { 1 } , \ \gamma _ { 0 } = \| s _ { 0 } \| _ { 2 } ^ { 2 } .
$$

for $k = 0 , 1 , 2 , \ldots$ while $\gamma _ { k } > \tau$ do

$$
\begin{array} { r l } & { q _ { k } = - { C ^ { T } } p _ { k } , } \\ & { \alpha _ { k } = \gamma _ { k } / ( | p _ { k } | | _ { 2 } ^ { 2 } + | | q _ { k } | | _ { 2 } ^ { 2 } ) , } \\ & { r _ { k + 1 } = r _ { k } - \alpha _ { k } q _ { k } , } \\ & { t _ { k + 1 } = t _ { k } - \alpha _ { k } p _ { k } , } \\ & { s _ { k + 1 } = t _ { k + 1 } - { C r _ { k + 1 } } , } \\ & { \gamma _ { k + 1 } = | | s _ { k + 1 } | | _ { 2 } ^ { 2 } , } \\ & { \beta _ { k } = \gamma _ { k + 1 } / \gamma _ { k } , } \\ & { p _ { k + 1 } = s _ { k + 1 } + \beta _ { k } p _ { k } . } \end{array}
$$

At termination $x _ { k }$ is retrieved from $A _ { 1 } x _ { k } = b _ { 1 } + C ^ { T } t _ { k }$

This requires about the same storage and work per step as Algorithm 6.3.3. However, as shown by Yuan [1142,1993l, the last formulation is advantageous for generalized least squares

problems with a covariance matrix $V \neq I$ .The generalized normal equations for problem (6.3.25) are

$$
\begin{array} { r l } { ( I _ { n } } & { { } C ^ { T } ) V ^ { - 1 } \left[ \left( \begin{array} { l } { I _ { n } } \\ { C } \end{array} \right) y - b \right] , \quad A _ { 1 } x = y . } \end{array}
$$

On the other hand,the generalized problem for(6.3.35) only involves $V$ ：

$$
\left( - C \quad I _ { m _ { 2 } } \right) V \left( \begin{array} { c } { { - C ^ { T } } } \\ { { I _ { m _ { 2 } } } } \end{array} \right) r _ { 2 } = b _ { 2 } - C b _ { 1 } , \quad y = b _ { 1 } - \left( \begin{array} { c c } { { I _ { m _ { 2 } } } } & { { 0 } } \end{array} \right) V \left( \begin{array} { c } { { - C ^ { T } } } \\ { { I _ { m _ { 2 } } } } \end{array} \right) r _ { 2 } ,
$$

# Notes and references

Arioli and Duff [34, 2o15] discuss several aspects of submatrix preconditioning and describe a wealth of experiments with real least squares problems. Submatrix preconditioners for equality constrained least squares problems are given by Barlow, Nichols,and Plemmons [75,1988].

# 6.3.5 - Preconditioners from Randomized Algorithms

Randomized algorithms have become indispensable in areas such as combinatorial optimization, cryptography,and machine learning. Recently, fast randomized algorithms have been developed that act as preconditioners for very large strongly over- or underdetermined systems that arise in geophysics, genetics, natural language processing,and high-frequency trading. An excellent introduction to randomization and low-rank matrix factorization is given by Halko,Martinsson, and Tropp [562, 2011].

Drineas et al. [332, 2o11] introduce two randomized algorithms in which the rows of $A$ and $b$ are first preprocessed by a randomized Hadamard transform (also known as the Walsh-Hadamard transform). A Hadamard matrix is a symmetric orthogonal $2 ^ { m } \times 2 ^ { m }$ matrix $H = H _ { m }$ recursively defined by $H _ { 0 } = 1$ and

$$
H _ { m + 1 } = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { { H _ { m } } } & { { H _ { m } } } \\ { { H _ { m } } } & { { - H _ { m } } } \end{array} \right) , \quad m \ge 0 .
$$

The Hadamard matrix can be computed by $n \log n$ additions and subtractions. The randomized Hadamard transform is the product $H D$ ,where $D$ is a diagonal matrix formed by setting its elements to $+ 1$ or $- 1$ with equal probability. When applied to a vector it has the useful property of “spreading out its energy,” in the sense of providing a bound for its infinity norm. The Hadamard transform is used in data encryption as well as many signal processing and data compression algorithms.

In their first algorithm,Drineas et al. form a smaller $s \times n$ subproblem( $s \ll m ,$ ）from a uniform random sampling of the preprocessed system. In their second algorithm, a random projection $G = \mathrm { r a n d n } ( s , m ) \ \in \ \mathbb { R } ^ { s \times m }$ is applied, whose elements are independent random normal variables following the standard normal distribution. In both cases,the solution of the smaller system is shown to be a good approximation to the solution of the full problem.

Rokhlin and Tygert [934, 2oo8] describe a related algorithm based on random transformations.They use a row-mixing method that consists of random Givens transformations,a random diagonal scaling, and a fast Fourier transform (FFT). A preconditioner for a Krylov subspace method, such as CGLS,is then obtained from QR factors of a smaler subsystem obtained by random sampling. They report that for $s = 4 n$ the condition number of the preconditioned system is practically always less than 3.A drawback is that the solver must work with complex numbers.

Coakley,Rokhlin,and Tygert [259,2o11] introduce the algorithm CRT11 for orthogonal projection also based on random normal projection $G \in \mathbb { R } ^ { ( n + 4 ) \times \bar { m } }$ . It solves the overdetermined least squares problem as an intermediate step. CRT1l requires $3 n + 6$ matrix-vector products with $A$ or $A ^ { T }$ . It is very reliable on a broad range of problems because the condition of the preconditioned system is limited to about $1 0 ^ { 3 }$ for full-rank problems.

Avron，Maymonoukov,and Toledo [46,2o1o] develop a least squares algorithm called Blendenpik. They note that a uniform random sample of rows of $A$ gives a good subset preconditioner only when the coherence or statistical leverage score $\mu ( A )$ of $A$ is small. If $Q$ forms an orthonormal basis for the column space of $A$ ,then

$$
\mu ( \boldsymbol { A } ) \equiv \operatorname* { m a x } _ { i } \| Q _ { i , 1 : n } \| _ { 2 } ^ { 2 } .
$$

To achieve low coherence,a random-mixing preprocessing phase is performed before the random sampling. The rows of $A$ are first multiplied by a diagonal matrix $D$ with random elements $+ 1$ or $- 1$ . Next,a fast transform is applied to each column of $D A$ and $D b$ .This can bea Walsh-Hadamard transform (WHT),a discrete cosine transform (DCT),or a discrete Hartley transform (DHT); see Hartley [592,1942] and Bracewell [174,1984]. For example,the DCT can be achieved by the following MATLAB script:

$$
\begin{array} { r c l }   \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm  \end{array}
$$

With high probability the coherence of the resulting row-mixed matrix $B$ is small. After the row-mixing step, a random sample $B _ { 1 }$ of $s > \gamma n$ rows of $B$ is taken, where $\gamma > 1$ is an oversampling factor. The QR factorization $B _ { 1 } = Q _ { 1 } R _ { 1 }$ then gives a preconditioner $R _ { 1 }$ for LSQR. With a suitable sample size $s$ ， $\mathcal { R } ( Q ) _ { 1 }$ is a good approximation of $\mathcal { R } ( A )$ , and LSQR converges rapidly. With one preprocessing phase, $\gamma = 4$ was found to be near-optimal for a large range of problems. Since DHT needs less memory than WHT and works bettr than DCT, this is the preferred choice. A solver for underdetermined systems is included. Blendenpik often beats LAPACK's DGELS on dense highly overdetermined problems.

The iterative solver LSRN by Meng, Saunders,and Mahoney [789,2o14] is based on random normal projection. LSRN works for both highly over- and underdetermined systems and can handle rank-deficient systems.For an overdetermined least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| b - A x \| _ { 2 } = \operatorname* { m i n } \} ,
$$

with $A \in \mathbb { R } ^ { m \times n }$ and $\operatorname { r a n k } ( A ) = r \leq n < m$ ,LSRN performs the following steps:

1. Choose an oversampling factor $\gamma > 1$ and set $s = \gamma n$   
2. Compute $\widetilde { A } = G A$ ,where $G \in \mathbb { R } ^ { s \times m }$ is a random matrix whose elements are independent random variables following the standard normal distribution.   
3. Compute the compact SVD $\widetilde { A } = \widetilde { U } \widetilde { \Sigma } \widetilde { V } ^ { T }$ ,where $\widetilde { \Sigma } \in \mathbb { R } ^ { r \times r }$ $\widetilde { U }$ is not needed).   
4. Set $N = \widetilde { V } \Sigma ^ { - 1 }$ and compute the least-norm solution of $\begin{array} { r } { \operatorname* { m i n } _ { y } \| A N y - b \| _ { 2 } } \end{array}$ using a Krylovtype method such as LSQR. Return $x = N y$

A similarly structured algorithm works for strongly underdetermined systems.Note that $A$ is used by LSRN only for matrix-vector and matrix-matrix operations. Hence LSRN is effcient if $A$ is sparse or a fast linear operator.LSRN can easily be extended to handle Tikhonov regularization.

A reasonable choice for $\gamma$ in step 1 is 2.O. The random normal projection in step 2 takes $\mathcal { O } ( m n ^ { 2 } )$ time.This is more than the fast transforms used by some of the other methods.However, the random normal projection scales well in parallel environments. An important property of LSRN is that the singular values of $A N$ are the same as for random matrix $( G U ) ^ { \dagger }$ of size $s \times n$ and independent of the spectrum $A$ ； see Theorem 4.2 in Meng, Saunders,and Mahoney [789,2014]. The spectrum of such a random matrix is a well-studied problem in random matrix theory,and it is possible to give strong probability bounds on the condition number of $A N$ .To reach precision $1 0 ^ { - 1 4 }$ , the maximum number of iterations needed by LSQR is $\approx 6 6 / \log ( s / r )$ Thus the running time for LSRN is fully predictable.

The LSRN package can be downloaded from http: //www.stanf ord.edu/group /SOL/ sof tware/lsrn.html. On dense overdetermined problems with $n = 1 0 ^ { 3 }$ ,LSRN is compared with solvers DGELSD and DGELSY from LAPACK and Blendenpik. For full-rank problems, Blendenpik is the overall winner and LSRN the runner-up.Blendenpik is not designed for rankdeficient problems,while LSRN can take advantage of rank-deficiency. For underdetermined problems, the LAPACK solvers run much slower, while LSRN works equally well On sparse problems, LSRN is also compared to SPQR from SuiteSparseQR. On generated sparse test problems, SPQR works well for $m < 1 0 ^ { 5 }$ ．For larger problems,LSRN is the fastest solver. The advantage of LSRN becomes greater for underdetermined systems.

# 6.3.6- Two-Level Preconditioners

In two-level subspace preconditioners for solving $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ , the solution is split as

$$
x = V x _ { 1 } + W x _ { 2 } , \quad V \in \mathbb { R } ^ { n \times k } , \quad W \in \mathbb { R } ^ { n \times ( n - k ) } ,
$$

where rank $( \boldsymbol { V } ^ { \mathrm { ~ \scriptsize ~ W ~ } } ) = \boldsymbol { n }$ With $A _ { 1 } \equiv A V$ and $A _ { 2 } \equiv A W$ , this is a two-block least squares problem of the form

$$
\operatorname* { m i n } _ { x _ { 1 } , x _ { 2 } } \left\| A \left( V ~ W \right) \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right) - b \right\| _ { 2 } ^ { 2 } ,
$$

studied in Section 4.3.1. Such methods for solving Tikhonov regularized problems were proposed by Hanke and Vogel [572,1999]. Usually, $k \ll n$ ,and a direct method is used to compute $x _ { 1 }$ .For $x _ { 2 }$ a Krylov subspace method, such as LSQR,is used that acts in the space complementary to ${ \mathcal { R } } ( V )$ . The rate of convergence is determined by the singular values of $W$ ,and the reduced condition number is

$$
\kappa = \operatorname* { m a x } _ { x \in \mathcal { R } ( W ) } \| A x \| _ { 2 } \Big / \operatorname* { m i n } _ { x \in \mathcal { R } ( W ) } \| A x \| _ { 2 } .
$$

An efficient implementation of such a method is given by Jacobsen, Hansen,and Saunders [661, 2oo3]. First, the Householder QR factorization

$$
A V = \left( Q _ { 1 } \quad Q _ { 2 } \right) { \binom { R } { 0 } } , \quad { \binom { c _ { 1 } } { c _ { 2 } } } = { \binom { Q _ { 1 } ^ { T } b } { Q _ { 2 } b } }
$$

is computed, where $R \in \mathbb { R } ^ { k \times k }$ is upper triangular. The matrices $Q _ { 1 }$ and $Q _ { 2 }$ are not explicitly formed but (as usual) are represented by the $k$ corresponding Householder vectors. The problem then becomes

$$
\operatorname* { m i n } _ { x _ { 1 } , x _ { 2 } } \left\| \left( \begin{array} { l l } { R } & { Q _ { 1 } ^ { T } A W } \\ { 0 } & { Q _ { 2 } ^ { T } A W } \end{array} \right) \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right) - \left( \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right) \right\| _ { 2 } .
$$

The subproblem for $x _ { 2 }$

$$
\operatorname* { m i n } _ { x _ { 2 } } \| Q _ { 2 } ^ { T } A W x _ { 2 } - c _ { 2 } \| _ { 2 } ,
$$

is independent of $x _ { 1 }$ and can be solved by LSQR or CGLS. Then $x _ { 1 }$ is found from

$$
R x _ { 1 } = c _ { 1 } - Q _ { 1 } ^ { T } A W x _ { 2 } .
$$

If operations with $W$ and $W ^ { T }$ are expensive, an alternative is to set $p = W x _ { 2 }$ in (6.3.40)- (6.3.41) and solve for $p$ .This has the drawback that $Q _ { 2 } ^ { T } A$ has a nontrivial nullspace spanned by the $k$ columns of $V$ ．Although LSQR still works for singular least squares problems,a divergent component will arise as an effect of rounding errors; see Paige and Saunders [866, $\mathrm { 1 9 8 2 }$ ,Sect. 6.2]. An effective stopping criterion is needed to terminate the iterations before divergence sets in.

The generalized Tikhonov regularization problem is

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| L x \| _ { 2 } ^ { 2 } .
$$

When $L \in \mathbb { R } ^ { p \times n }$ ， $p < n$ ,and has a nontrivial nullspace spanned by the matrix $W _ { 2 }$ , this can be transformed into standard form as follows; see Section 3.6.5. Let $\overset { \vartriangle } { \bar { A } } = A L _ { A } ^ { \dag }$ , where

$$
\begin{array} { r } { L _ { A } ^ { \dag } = ( I - P ) L ^ { \dag } , \quad P = W _ { 2 } ( A W _ { 2 } ) ^ { \dag } A , } \end{array}
$$

is the $A$ weighted pseudoinverse (3.6.46) of $L$ . The solution can be split into two parts as

$$
x = L _ { A } ^ { \dag } y + z , \quad z = ( A W _ { 2 } ) ^ { \dag } b ,
$$

where $z \in \mathcal { N } ( L )$ is the unregularized part of the solution. An iterative method is used to solve for $y$ where $L _ { A } ^ { \dagger }$ acts as a right preconditioner. The matrix $L _ { A } ^ { \dagger }$ is not formed explicitly but kept in the factored form (6.3.42). The implementation of this two-level method is discussed in more detail by Hansen [576,19g8] and Hansen and Jensen [582,2006].

When $L \ = \ I$ the optimal choice of columns for $V$ consists of the right singular vectors corresponding to the $k$ largest singular values of $A$ . This will minimize the condition number of the reduced subproblem (6.3.40). The choice is usually not practical; instead, singular vectors from a related simpler problem of reduced size can be used to form $V$ .Another possibility is to perform products by $V$ and $V ^ { T }$ with fast transforms. Two examples are the cosine transform DC-2 and the wavelet transform. Extensive numerical experiments with two-level preconditioners are given by Jacobsen [660, 2000].

Bunse-Gerstner, Guerra-Ones,and de La Vega [189,2oo6] give a modification of the twolevel LSQR algorithm that makes it considerably less expensive when the solution, as is often the case,is needed for a large number of regularization parameters.

# 6.3.7 - Preconditioners for Toeplitz Problems

Least squares problems $\mathrm { m i n } _ { x } \| T x - b \| _ { 2 }$ , where $T$ is a rectangular Toeplitz matrix

$$
T = \left( \begin{array} { c c c c } { t _ { 0 } } & { t _ { 1 } } & { \ldots } & { t _ { n - 1 } } \\ { t _ { - 1 } } & { t _ { 0 } } & { \ldots } & { t _ { n - 2 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { t _ { 1 - m } } & { t _ { 2 - m } } & { \ldots } & { t _ { n - m } } \end{array} \right) \in \mathbb { R } ^ { m \times n } , \quad m \geq n ,
$$

of very large dimensions arise,e.g., in signal restoration,seismic explorations, and image processing.

A matrix-vector product $T x$ is essentially a discrete convolution operation. As will be shown in the following,by embedding the Toeplitz matrix into a circulant matrix,a matrix-vector product $T x$ can be computed via the fast Fourier transform in $O ( n \log n )$ operations.Provided a good preconditioner can be found, iterative methods such as CGLS or LSQR can be competitive with the fast direct methods given in Section 4.5.5.

A circulant matrix is square and has the form

$$
C _ { n } = \operatorname { c i r c } ( c _ { 0 } , c _ { 1 } , \ldots , c _ { n - 1 } ) = \left( { \begin{array} { c c c c } { c _ { 0 } } & { c _ { 1 } } & { \cdots } & { c _ { n - 1 } } \\ { c _ { n - 1 } } & { c _ { 0 } } & { \cdots } & { c _ { n - 2 } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { c _ { 1 } } & { c _ { 2 } } & { \cdots } & { c _ { 0 } } \end{array} } \right) \in \mathbb { R } ^ { n \times n } .
$$

It is defined by the elements in its first row. Each column in $C _ { n }$ is a cyclic up-shifted version of the previous column. If $e _ { i }$ is the $i$ th unit vector and

$$
P _ { n } = \left( \begin{array} { c c } { { 0 } } & { { I _ { n - 1 } } } \\ { { e _ { 1 } ^ { T } } } & { { 0 } } \end{array} \right)
$$

is the circulant shift matrix, then $P _ { n } e _ { 1 } = e _ { n }$ ， $P _ { n } e _ { 2 } = e _ { 1 } , . . . , P _ { n } e _ { n } = e _ { n - 1 }$ ,and it follows that $P _ { n } ^ { n } = I$ . Hence, the eigenvalues of $P _ { n }$ are the $n$ roots of unity,

$$
\omega _ { j } = e ^ { - 2 \pi i j / n } , \quad j = 0 : n - 1 ,
$$

and the eigenvectors are the columns of the discrete Fourier matrix,

$$
F = ( f _ { j k } ) , \quad f _ { j k } = \frac { 1 } { \sqrt { n } } e ^ { 2 \pi i j k / n } , \quad 0 \leq j , k \leq n ,
$$

where $i = \sqrt { - 1 }$ The cireulant matix $C _ { n }$ can e writen asa rolynomial $\begin{array} { r } { C _ { n } = \sum _ { k = 0 } ^ { n - 1 } c _ { k } P _ { n } ^ { k } } \end{array}$ in . Hence it has the same eigenvectors as , and its eigenvalues are given by

$$
F ( c _ { 0 } , c _ { n - 1 } , \ldots , c _ { - 1 } ) ^ { T } = ( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } ) ^ { T } .
$$

The matrix $C _ { n }$ can thus be factorized as

$$
\begin{array} { r } { C _ { n } = F \Lambda F ^ { H } , \quad \Lambda = \operatorname { d i a g } { \left( \lambda _ { 1 } , \lambda _ { 2 } \dots , \lambda _ { n } \right) } . } \end{array}
$$

It follows that operations with a circulant matrix $C _ { n }$ can be performed in $O ( n \log n )$ operations using the FFT.

We now show how any Toeplitz matrix $T$ can be expanded into a circulant matrix. For illustration, set $m = n = 3$ ,and define

$$
C _ { T } = ( \begin{array} { c c } { T } & { V } \\ { V } & { T } \end{array} ) = ( \begin{array} { c c c c c } { t _ { 0 } } & { t _ { 1 } } & { t _ { 2 } } & { | } & { 0 } & { t _ { - 2 } } & { t _ { - 1 } } \\ { t _ { - 1 } } & { t _ { 0 } } & { t _ { 1 } } & { | } & { t _ { 2 } } & { 0 } & { t _ { - 2 } } \\ { t _ { - 2 } } & { t _ { - 1 } } & { t _ { 0 } } & { t _ { 1 } } & { t _ { 2 } } & { 0 } \\ { 0 } & { t _ { - 2 } } & { t _ { - 1 } } & { | } & { t _ { 0 } } & { t _ { 1 } } & { t _ { 2 } } \\ { t _ { 2 } } & { 0 } & { t _ { - 2 } } & { | } & { t _ { - 1 } } & { t _ { 0 } } & { t _ { 1 } } \\ { t _ { 1 } } & { t _ { 2 } } & { 0 } & { t _ { - 2 } } & { t _ { - 1 } } & { t _ { 0 } } \end{array}  ) \in \mathbb { R } ^ { 6 \times 6 } .
$$

A similar construction works for rectangular Toeplitz matrices. For the Toeplitz matrix (6.3.44), the circulant

$$
C _ { T } = \operatorname { c i r c } ( t _ { 0 } , \dots , t _ { n - 1 } , 0 , t _ { - m + 1 } , \dots , t _ { - 1 } ) \in \mathbb { R } ^ { ( n + m ) \times ( n + m ) }
$$

can be used. To form $y = T x \in \mathbb { R } ^ { m + 1 }$ for arbitrary $x \in \mathbb { R } ^ { n }$ ， $x$ is padded with zeros to length $n + m$ , and we calculate

$$
\boldsymbol { z } = \boldsymbol { C } _ { T } \left( \begin{array} { l } { \boldsymbol { x } } \\ { \boldsymbol { 0 } } \end{array} \right) = \boldsymbol { F } \boldsymbol { \Lambda } \boldsymbol { F } ^ { H } \left( \begin{array} { l } { \boldsymbol { x } } \\ { \boldsymbol { 0 } } \end{array} \right) , \quad \boldsymbol { y } = \left( \boldsymbol { I _ { m } } \quad \boldsymbol { 0 } \right) \boldsymbol { z } .
$$

This can be done with two FFTs and one multiplication with a diagonal matrix. The cost is $O ( n \log _ { 2 } n )$ multiplications. A similar scheme enables fast computation of $T ^ { H } y$

Strang[1O42,1986] obtained a circulant matrix as a preconditioner for symmetric positive definite Toeplitz systems by copying the central diagonals of $T$ and “bringing them around.” He showed that the eigenvalues of $T C ^ { - 1 }$ cluster around 1,except for the largest and smallest eigenvalues. T. Chan [225,1988] gave an improved circulant preconditioner that is optimal in the sense of minimizing $\| C - T \| _ { F }$

Theorem 6.3.1. Let $T \in \mathbb { R } ^ { n \times n }$ be a square (not necessarily symmetric positive definite)Toeplitz matrix. Then the circulant matrix $C = ( c _ { 0 } , c _ { 1 } , \dots , c _ { n - 1 } )$ with

$$
c _ { i } = \frac { i t _ { - ( n - i ) } + ( n - i ) t _ { i } } { n } , \quad i = 0 : n - 1 ,
$$

minimizes $\| C - T \| _ { F }$

The best approximation $C$ has a simple structure. It is obtained by averaging the correspond-ing diagonal of $T$ extended to length $n$ by wraparound. For a Toeplitz matrix of order $n = 4$ we obtain

$$
T = \left( \begin{array} { l l l l } { t _ { 0 } } & { t _ { 1 } } & { t _ { 2 } } & { t _ { 3 } } \\ { t _ { - 1 } } & { t _ { 0 } } & { t _ { 1 } } & { t _ { 2 } } \\ { t _ { - 2 } } & { t _ { - 1 } } & { t _ { 0 } } & { t _ { 1 } } \\ { t _ { - 3 } } & { t _ { - 2 } } & { t _ { - 1 } } & { t _ { 0 } } \end{array} \right) , \qquad C = \left( \begin{array} { l l l l } { t _ { 0 } } & { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } \\ { c _ { 1 } } & { t _ { 0 } } & { c _ { 3 } } & { c _ { 2 } } \\ { c _ { 2 } } & { c _ { 1 } } & { t _ { 0 } } & { c _ { 3 } } \\ { c _ { 3 } } & { c _ { 2 } } & { c _ { 1 } } & { t _ { 0 } } \end{array} \right) ,
$$

where

$$
c _ { 1 } = ( t _ { - 3 } + 3 t _ { 1 } ) / 4 , \quad c _ { 2 } = ( t _ { - 1 } + t _ { 1 } ) / 2 , \quad c _ { 3 } = ( 3 t _ { - 1 } + t _ { 3 } ) .
$$

The convergence rate of CGLS applied to a preconditioned Toeplitz system $T C ^ { - 1 } y = b$ de-pends on the distribution of the singular values of $T C ^ { - 1 }$ . R. Chan, Nagy,and Plemmons [219, 1994] show that if the generating functions of the blocks $T _ { j }$ are $2 \pi$ -periodic continuous functions,and if one of these functions has no zeros,then the singular values of the preconditioned matrix $T C ^ { - 1 }$ are clustered around 1,and PCGLS converges very quickly. The class of $2 \pi \cdot$ periodic continuous functions contains a class of functions that arises in many signal processing applications.

Similar ideas can be applied to problems where the least squares matrix $T$ has a general Toeplitz block or block Toeplitz structure; see Nagy [817,1991] and R. Chan,Nagy,and Plemmons [218,1993l. Hence the method can be applied also to multidimensional problems. Consider a least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| T \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } , \qquad T = \left( \begin{array} { l } { T _ { 1 } } \\ { \vdots } \\ { T _ { q } } \end{array} \right) \in \mathbb { R } ^ { m \times n } ,
$$

where each block $T _ { j }$ ， $j = 1 , \dotsc , q$ , is a square Toeplitz matrix. (Note that if $T$ itself is a rectangular Toeplitz matrix, then each block $T _ { j }$ is necessarily Toeplitz.) In the first step,a circulant approximation $C _ { j }$ is constructed for each block $T _ { j }$ . Each circulant matrix $C _ { j }$ ， $j = 1 , \dotsc , q$ ,is then diagonalized by the Fourier matrix $F$ ： $C _ { j } = F \Lambda _ { j } F ^ { H }$ . The eigenvalues $\Lambda _ { j }$ can be found from the first column of $C _ { j }$ ; cf. (6.3.48). Hence, the spectrum of $C _ { j }$ ， $j = 1 , \dotsc , q$ ，can be computed in $O ( m \log n )$ operations using the FFT.

The preconditioner for $T$ is then defined as a square circulant matrix $C$ such that

$$
C ^ { T } C = \sum _ { j = 1 } ^ { q } C _ { j } ^ { T } C _ { j } = F ^ { H } \sum _ { j = 1 } ^ { q } ( \Lambda _ { j } ^ { H } \Lambda _ { j } ) F .
$$

Thus, $C ^ { T } C$ is also circulant, and its spectrum can be computed in $O ( m \log n )$ operations. Now $C$ is taken to be the Hermitian positive definite matrix

$$
C \equiv F ^ { H } \biggl ( \sum _ { j = 1 } ^ { q } \Lambda _ { j } ^ { H } \Lambda _ { j } \biggr ) ^ { 1 / 2 } F .
$$

Then CGLS with right preconditioner $C$ is applied to solve $\begin{array} { r } { \operatorname* { m i n } _ { x } \| T x - b \| _ { 2 } } \end{array}$ Note that to use $C$ as a preconditioner we need only know its eigenvalues, because the factorization (6.3.54) can be used to solve linear systems involving $C$ and $C ^ { T }$ . The generalization to block Toeplitz matrices is straightforward.

# Notes and references

Construction of circulant preconditioners for constrained and weighted Toeplitz least squares problems is studied by Jin [672,1996]． Iterative methods for solving Toeplitz problems are surveyed by R. Chan and $\mathrm { N g } \ [ 2 2 0 , 1 9 9 6 ]$ and R. Chan and Jin [221, 2007].

# 6.4 - Regularization by Iterative Methods

# 6.4.1 - Landweber's Method

Discrete ill-posed linear systems $A x = b$ are characterized by $A$ having a large group of numerically zero singular values with a sizeable gap to the rest of the spectrum. Furthermore, $b$ has small projections onto the right singular vectors associated with the smal singular values. Multidimensional il-posed problems lead to large-scale discrete ill-posed systems with structured or sparse matrices that are well suited for iterative solution methods.Many of these methods have intrinsic regularization properties,where the number of iterations $k$ plays the role of regularization parameter.

One of the earliest iterative regularization methods for ill-posed linear systems is to apply Richardson's method (see Section 6.1.2) to the normal equations $A ^ { T } ( A x - b ) = 0$ ，

$$
x _ { k } = x _ { k - 1 } + \omega A ^ { T } ( b - A x _ { k - 1 } ) , \quad k = 1 , 2 , \ldots ,
$$

where $\omega$ is chosen so that $\omega \approx 1 / \sigma _ { 1 } ( A ) ^ { 2 }$ . In this context the method is known as Landweber's method [718,1951]. From the standard theory of stationary iterative methods it follows that the error in $x _ { k }$ satisfies

$$
x - x _ { k } = ( I - \omega A ^ { T } A ) ( x - x _ { k - 1 } ) = ( I - \omega A ^ { T } A ) ^ { k } ( x - x _ { 0 } ) .
$$

Taking $x _ { 0 } = 0$ and expanding the error in terms of the SVD (singular value decomposition) $\begin{array} { r } { A = \sum _ { i = 1 } ^ { n } \sigma _ { i } u _ { i } v _ { i } ^ { T } } \end{array}$ showsthat(6.4.2)canbe writeas

$$
x _ { k } = \sum _ { i = 1 } ^ { n } \varphi _ { k } ( \sigma _ { i } ^ { 2 } ) \frac { u _ { i } ^ { T } b } { \sigma _ { i } } v _ { i } , \qquad \varphi _ { k } ( \sigma ^ { 2 } ) = 1 - ( 1 - \omega \sigma ^ { 2 } ) ^ { k } .
$$

It follows that the effect of terminating the iteration with $x _ { k }$ is to damp the component of the solution along $v _ { i }$ by the factor $\varphi _ { k } ( \sigma _ { i } ^ { 2 } )$ , where $\varphi _ { k } ( \sigma ^ { 2 } )$ is the filter factor for Landweber's method; see Section 3.5.3. After $k$ iterations,only the components of the solution corresponding to $\sigma _ { i } \geq 1 / k ^ { 1 / 2 }$ have converged. If the noise level in $b$ is known, the discrepancy principle can be used as a stopping criterion; see Section 3.6.4.

When an iterative method is applied to an il-posed problem,the error in $x _ { k }$ will initially decrease, but eventually the unwanted irregular part of the solution will grow and cause the process to diverge. Such behavior is called semiconvergence.The iterations should be stopped before divergence starts. Terminating the Landweber method after $k$ iterations gives roughly the same result as using truncated SVD (see Section 3.6.2) where components corresponding to $\sigma _ { i } \le \mu \sim k ^ { - 1 / 2 }$ are dropped. The square root means that usually many iterations are required. For this reason,Landweber's method cannot in general be recommended; see Hanke [566,1991].

If $A \ \in \ R ^ { m \times n }$ is rank-deficient, $x _ { k }$ in Landweber's method can be split into orthogonal components:

$$
\begin{array} { r } { x _ { k } = y _ { k } + z _ { k } , \quad y _ { k } \in \mathcal { R } ( A ^ { T } ) , \quad z _ { k } \in \mathcal { N } ( A ) . } \end{array}
$$

The orthogonal projection of $x _ { k } - x _ { 0 }$ onto ${ \mathcal { N } } ( A )$ can then be shown to be zero.Hence,in exact arithmetic, the iterates converge to the unique least squares solution that minimizes $\| x - x _ { 0 } \| _ { 2 }$ Strand [1O41,1974] analyzed the more general iteration

$$
x _ { k + 1 } = x _ { k } + p ( A ^ { T } A ) A ^ { T } ( b - A x _ { k } ) ,
$$

where $p ( \lambda )$ is a polynomial of order $d$ in $\lambda$ A special case is the iteration suggested by Riley [929, 1956]: $x _ { k + 1 } = x _ { k } + \Delta x _ { k }$ ，where

$$
\operatorname* { m i n } _ { \Delta x _ { k } } { \left\| \left( \begin{array} { l } { A } \\ { \mu I } \end{array} \right) \Delta x _ { k } - \left( \begin{array} { l } { r _ { k } } \\ { 0 } \end{array} \right) \right\| _ { 2 } } , \quad r _ { k } = b - A x _ { k } .
$$

This corresponds to taking $p ( \lambda ) = ( \lambda + \mu ^ { 2 } ) ^ { - 1 }$ . Riley's method is sometimes called the iterated Tikhonov method.

Iteration (6.4.4) can be performed more effciently as follows. If

$$
1 - \lambda p ( \lambda ) = \prod _ { j = 1 } ^ { d } ( 1 - \gamma _ { j } \lambda )
$$

is the factorized polynomial, then one iteration step can be performed in $d$ minor steps of a nonstationary Landweber method:

$$
x _ { j + 1 } = x _ { j } + \gamma _ { j } A ^ { T } ( b - A x _ { j } ) , \quad j = 0 , 1 , \ldots , d - 1 .
$$

Assume that $\sigma _ { 1 } = \beta ^ { 1 / 2 }$ and that the aim is to compute an approximation to the truncated sin-gular value solution with a cut-off for singular values $\sigma _ { i } \le \sigma _ { c } = \alpha ^ { 1 / 2 }$ . Then, as shown by Rutishauser[948,1959l,in acertai sense the optimal parameters touse in (6.4.5)are $\gamma _ { j } = 1 / \xi _ { j }$ ， where $\xi _ { j }$ are the zeros of the Chebyshev polynomial of degree $d$ on the interval $[ \alpha , \beta ]$ ：

$$
\xi _ { j } = \frac { 1 } { 2 } ( \alpha + \beta ) + \frac { 1 } { 2 } ( \alpha - \beta ) x _ { j } , \quad x _ { j } = \cos { \Big ( \frac { \pi } { 2 } \frac { 2 j + 1 } { d } \Big ) } ,
$$

$j = 0 , 1 , \ldots , d - 1$ . This choice leads to a filter function $R ( t )$ of degree $d$ with $R ( 0 ) = 0$ ,and of least maximum deviation from 1 on $[ \alpha , \beta ]$ . Note that $\alpha$ must be chosen in advance,but the regularization can be varied by using a decreasing sequence $\alpha = \alpha _ { 1 } > \alpha _ { 2 } > \cdots$

From standard results for Chebyshev polynomials it can be shown that if $\alpha \ll \beta$ ,then $k$ steps of iteration (6.4.5)-(6.4.6) reduce the regular part of the solution by the factor

$$
\delta _ { k } \approx 2 e ^ { - 2 k ( \alpha / \beta ) ^ { 1 / 2 } } .
$$

Thus, the cut-off $\sigma _ { c }$ for this method is related to $j$ in (6.4.5) as $j \approx 1 / \sigma _ { c }$ This is a great improvement over the standard Landweber's method, for which the number of steps needed is $k \approx ( 1 / \sigma _ { c } ) ^ { 2 }$

Iteration (6.4.5) with parameters (6.4.6) suffers severely from roundoff errors. This instability can be overcome by a reordering of the parameters $\xi _ { j }$ ； see Anderson and Golub [24,1972]. Alternatively, (6.4.5)-(6.4.6) can be writen as a three-term recursion,as in the CSI method of Section 6.1.6.

# 6.4.2 - Regularized CGLS and CGME

For ill-conditioned least squares and least-norm problems it is often beneficial to include a regularization term.In the least squares case the standard regularized problem (defining Tikhonov regularization) is

$$
\operatorname* { m i n } _ { x } \| b - A x \| ^ { 2 } + \mu ^ { 2 } \| x \| _ { 2 } ^ { 2 } ,
$$

where $\mu > 0$ is a suitably chosen parameter. This problem has a unique solution that satisfies the regularized normal equations $( A ^ { \bar { T } } A + \mu ^ { 2 } I _ { n } ) x = \bar { A } ^ { T } b$ or, in factored form,

$$
A ^ { T } r - \mu ^ { 2 } x = 0 , \quad r = b - A x .
$$

The regularized least squares problem (6.4.8) can be solved by applying CGLS to the least squares problem $\mathrm { m i n } _ { x } \| \tilde { \boldsymbol { A } } \boldsymbol { x } - \tilde { \boldsymbol { b } } \| _ { 2 }$ ,where

$$
\widetilde { A } = \left( { \begin{array} { c } { A } \\ { \mu I _ { n } } \end{array} } \right) \in \mathbb { R } ^ { ( m + n ) \times n } , \qquad \widetilde { b } = \left( { \begin{array} { c } { b } \\ { 0 } \end{array} } \right) \in \mathbb { R } ^ { ( m + n ) } .
$$

However, it is preferable to use the modified version of CGLS given below,where the following changes have been made: alpha $\mathbf { \Sigma } = \mathbf { \Sigma } { \bf s t s } / \left( { \bf q } ^ { , } * { \bf q } \right)$ is changed to alpl $\mathsf { \Omega } _ { 1 } \mathsf { a } \ = \mathsf { \Omega } _ { \mathsf { S } } \mathsf { t s } / ( \mathsf { q } ^ { \prime } \ast$ $( \mathsf { q } ^ { \prime } \ast \mathsf { q } ^ { \mathrm { ~ + ~ } }$ $\mathtt { m u 2 * p } ^ { \mathtt { 1 } } \ast \mathtt { p } )$ ,and $\mathrm { ~ \tt ~ s ~ } = \mathrm { ~ \tt ~ A ~ } ^ { \ u , } * \mathrm { r }$ is changed to $\mathbf { s } ~ = ~ \mathrm { ~ A ~ } ^ { \prime } { * } \mathrm { r ~ \mathbf ~ { ~ - ~ } ~ } \mathtt { m u } 2 { * } \mathbf { x }$

RCGLS requires one more scalar product than CGLS per step but no extra storage.

# Algorithm 6.4.1 (RCGLS).

function $[ \mathrm { x } , \mathrm { r } , \mathrm { n r m } ] = \mathrm { r c g } { 1 } { \bf s } \left( \mathrm { A } , \mathrm { b } , \mathrm { m } 2 , \mathrm { x } 0 , \mathrm { m } \mathrm { a x } \mathrm { i } { \mathrm { t } } \right)$   
$\%$ RCGLS performs at most maxit CG iterations   
$\%$ for the normal equations ${ \mathbb A } ^ { \mathrm { ~ \tiny ~ 3 ~ } } ( { \mathtt b } \mathrm { ~ \tiny ~ - ~ } { \mathtt A } { \mathtt x } ) = { \mathtt m } { \mathtt u } 2 \mathrm { ~ \tiny ~ x ~ } .$   
%-- $\mathrm { ~ \tt ~ x ~ } = \mathrm { ~ \tt ~ x 0 ~ }$ ； $\mathrm { ~  ~ r ~ } = \mathrm { ~  ~ b ~ } - \mathrm { ~  ~ A ~ } + \tt X ;$ $\begin{array} { r } { \textbf { s } = \textrm { A } ^ { \prime } * \mathtt { r } \ \textbf { - } \ \mathtt { m } \mathbf { u } 2 * \mathtt { x } \ ; } \end{array}$ $\mathrm { n r m ~ } = \textbf { s } ^ { \prime } \ast \bf { s } ; \quad \mathtt { p } ~ = ~ \bf { s } ;$ for $\mathtt { \lambda } \mathtt { k } \mathtt { \lambda } = \mathtt { \lambda } 0$ :maxit if nrm $\ c = ~ 0$ ，break，end $\begin{array} { r l } & { \mathrm { ~ q ~ = ~ A ^ { * } P ~ ; } } \\ & { \mathrm { ~ a \perp p h a ~ = ~ n r m / ~ ( q ' * q ~ + ~ m u 2 * ( p ' * p ) ) ~ ; } } \\ & { \mathrm { ~ x ~ = ~ x ~ + ~ a l p h a * \mit p ; } } \\ & { \mathrm { ~ r ~ = ~ r ~ - ~ a l \mathrm { ~ p h a * \mit q ; } ~ } } \\ & { \mathrm { ~ s ~ = ~ A ^ { \prime } * r ~ - ~ m u 2 * x ; } } \\ & { \mathrm { ~ n r m o \mit d ~ d ~ = ~ n r m ; ~ \mit \ n r m ~ = ~ s ^ { \prime } * s ; } } \\ & { \mathrm { ~ b e t a ~ = ~ n r m / n r m o \mit 1 d ; } } \\ & { \mathrm { ~ p ~ = ~ s ~ + ~ b e t a \ast \mit p ; } } \end{array}$ end   
end

The regularized least-norm problem is

$$
\operatorname* { m i n } _ { x , y } \left\| \left( { x \atop y } \right) \right\| _ { 2 } ^ { 2 } { \mathrm { s u b j e c t  t o ~ ( } } A \quad \mu I _ { m } { \mathrm { \Omega } } ) \left( { x \atop y } \right) = b .
$$

The linear system $A x + \mu y = b$ is always consistent if $\mu \neq 0$ . Its solution is $x = A ^ { T } z$ ， $y = \mu z$ ， where $z$ solves the normal equations

$$
\left( A \quad \mu I _ { m } \right) \left( { \cal { A } } ^ { T } \right) z = ( { \cal { A } } { \cal { A } } ^ { T } + \mu ^ { 2 } I _ { m } ) z = b .
$$

This can be solved by setting

$$
\widetilde { A } = \left( A \quad \mu I _ { m } \right) \in \mathbb { R } ^ { m \times ( n + m ) } , \qquad \widetilde { x } = \left( { x \atop y } \right) \in \mathbb { R } ^ { n + m }
$$

and applying CGME to the least-norm problem

$$
\operatorname* { m i n } _ { \widetilde { x } } \| \widetilde { x } \| _ { 2 } \ \mathrm { s u b j e c t } \ t \mathrm { o } \ \widetilde { A } \widetilde { x } = b .
$$

Since $y$ is not of interest, the regularized version RCGME of CGME given below is to be preferred. This needs only a small amount of extra arithmetic work and no extra storage.

# Algorithm 6.4.2 (RCGME).

function $[ \mathbf { x } , \mathbf { r } ] \ = \ \mathbf { r c g m e } ( \mathtt { A } , \mathtt { b } , \mathtt { m u } 2 , \mathtt { m a x i t } )$   
$\%$ RCGME performs at most maxit steps of Craig's   
$\%$ algorithm on the regularized system $\mathrm { A x ~ + ~ \ m u ~ \ y ~ = ~ b ~ }$   
$\%$ $\texttt { x } = \texttt { 0 }$ ； $\texttt { r } = \texttt { b }$ ； $\mathrm { ~ \tt ~ p ~ } = \mathrm { ~ \tt ~ r ~ }$ $\mathtt { n r m } = \mathtt { r } ^ { \prime } * \mathtt { r }$ ； for $\texttt { k } = \texttt { 1 }$ : maxit if nrm $\ c = ~ 0$ ，break，end $\mathsf { q } = \mathsf { A } ^ { \flat } { * } \mathsf { p }$ ； $\begin{array} { r l } & { \mathrm { ~ \gamma _ \mathrm { ~ d ~ } ~ ^ \mathrm { ~ a ~ } ~ ~ \gamma _ \mathrm { ~ r ~ } ~ } , } \\ & { \mathrm { ~ a ~ \mathrm { ~ l ~ p ~ h ~ a ~ } ~ = ~ \mathrm { { \ n r m } / { ( \check { q } ^ { \gamma } * q _ { \tau } ~ + ~ \mathrm { { \ m u } } 2 * { ( \check { p } ^ { \gamma } * p ) } ) } ~ } } ; } \\ &  \mathrm { ~ \gamma ~ = ~ \check { \tau } ~ + ~ \mathrm { { a } } ~ \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } } \\ &  \mathrm { ~ \gamma ~ = ~ \check { \tau } ~ - \mathrm { { \ a } } ~ \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } } \\ & { \mathrm { ~ \mathrm { { \ n r m o } 1 } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { { } } \mathrm { } = \mathrm { { \ n r m } } ; \mathrm { { \quad } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } } } \\ &  \mathrm { ~ \mathrm { \ b e t a } ~ = \mathrm { { \ n r m } / \mathrm { n r m o 1 } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } } } \\ & { \mathrm { ~ \gamma ~ = ~ \check { \tau } ~ + \mathrm { { \ b e t a } } { * \mathrm { { p } } } ~ } ; } \end{array}$ end   
and

From the convergence analysis of CG (Section 6.2.2) it follows that the convergence of RCGLS and RCGME depends on the distribution of the nonzero eigenvalues of $\left( A ^ { T } A + \mu ^ { 2 } I _ { n } \right)$ and $\left( A A ^ { T } + \mu ^ { 2 } I _ { m } \right)$ , respectively. These are $\lambda _ { i } = \sigma _ { i } ^ { 2 } + \mu ^ { 2 }$ ,where $\sigma _ { i }$ are the nonzero singular values of $A$

As noted by Saunders [965,1995], for $\mu > 0$ and $A$ of arbitrary dimensions,the regularized least-norm problem (6.4.9) is the same as the regularized least squares problem (6.4.8). From (6.4.9) we have $\mu y = b - A x = r$ .Using this to eliminate $y$ we see that both problems are equivalent to the augmented system

$$
\left( \begin{array} { c c } { { I _ { m } } } & { { A } } \\ { { A ^ { T } } } & { { - \mu ^ { 2 } I _ { n } } } \end{array} \right) \left( \begin{array} { c } { { r } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { 0 } } \end{array} \right) .
$$

Saunders derives regularized versions of LSQR and LSME that require litle additional work or storage. The bidiagonalizations of

$$
\tilde { A } = { \binom { A } { \mu I _ { n } } } \mathrm { a n d } \tilde { A } = \left( A \mu I _ { m } \right)
$$

can be obtained efficiently from the bidiagonalization of $A$ used in LSQR and LSME. In regularized LSQR the bidiagonal subproblem defining $x _ { k } = V _ { k } y _ { k }$ is

$$
\operatorname* { m i n } _ { y _ { k } } \left\| \left( \begin{array} { c } { B _ { k } } \\ { \mu I } \end{array} \right) y _ { k } - \left( \begin{array} { c } { \beta _ { 1 } e _ { 1 } } \\ { 0 } \end{array} \right) \right\| ,
$$

where $B _ { k }$ is lower bidiagonal. Orthogonal matrices $\tilde { Q } _ { k }$ can be constructed from $2 k - 1$ plane rotations so that

$$
\tilde { Q } _ { k } \left( \begin{array} { c c } { B _ { k } } & { \beta _ { 1 } e _ { 1 } } \\ { \mu I } & { 0 } \end{array} \right) = \left( \begin{array} { c c } { \tilde { R } _ { k } } & { f _ { k } } \\ { 0 } & { \phi _ { k + 1 } } \end{array} \right) ,
$$

where $\tilde { R } _ { k } \in \mathbb { R } ^ { k \times k }$ is upper bidiagonal. The basis matrices $U _ { k + 1 }$ and $V _ { k }$ are modified accordingly. For LSME the regularized bidiagonal subproblem is

$$
\operatorname* { m i n } { \left\| \left( \begin{array} { l } { y _ { k } } \\ { t _ { k } } \end{array} \right) \right\| _ { 2 } ^ { 2 } } \mathrm { s u b j e c t ~ t o ~ } \left( \begin{array} { l l } { { L _ { k } } } & { { \mu I } } \end{array} \right) \left( \begin{array} { l } { { y _ { k } } } \\ { { t _ { k } } } \end{array} \right) = \beta _ { 1 } e _ { 1 } .
$$

Orthogonal matrices $\hat { Q } _ { k }$ are constructed so that

$$
\left( L _ { k } \quad \mu I \right) \hat { Q } _ { k } = \left( \hat { L } _ { k } \quad 0 \right) ,
$$

where $L _ { k } \in \mathbb { R } ^ { k \times k }$ and $\tilde { L } _ { k }$ are lower bidiagonal. Numerical tests indicate that regularized LSQR is more reliable and effcient than regularized LSME.

# 6.4.3 - Symmetric Quasi-Definite Systems

Linear systems of the form

$$
\left( \begin{array} { c c } { { M } } & { { A } } \\ { { A ^ { T } } } & { { - N } } \end{array} \right) \left( \begin{array} { c } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { c } } \end{array} \right)
$$

with $M \in \mathbb { R } ^ { m \times m }$ and $N \in \mathbb { R } ^ { n \times n }$ symmetric positive definite are called symmetric quasidefinite or SQD systems. These systems give the first-order optimality conditions for the two dual convex quadratic problems

$$
\begin{array} { r l } & { \underset { x \in \mathbb { R } ^ { n } } { \operatorname* { m i n } } \| A x - b \| _ { M ^ { - 1 } } ^ { 2 } + \| x \| _ { N } ^ { 2 } + 2 c ^ { T } x , } \\ & { \underset { y \in \mathbb { R } ^ { m } } { \operatorname* { m i n } } \| A ^ { T } y - c \| _ { N ^ { - 1 } } ^ { 2 } + \| y \| _ { M } ^ { 2 } - 2 b ^ { T } y , } \end{array}
$$

where quantities like $\| x \| _ { N } ^ { 2 } = x ^ { T } N x$ are elliptc norms. SQD systems arise in sequential quadratic programming and interior-point methods for convex optimization. Another source is in stabilized mixed finite element methods.

The SQD matrix in (6.4.12) is indefinite and has $m$ positive and $n$ negative eigenvalues. It is nonsingular,and its inverse is also SQD. The following properties of SQD matrices are established by Vanderbei [1085,1995] and George,Ikramov,and Kucherov [456,2000]:

1. An SQD matrix $K$ is strongly factorizable,i.e., for every permutation matrix $P$ there exists a diagonal matrix $D$ and a unit lower triangular matrix $L$ such that

$$
P K P ^ { T } = L D L ^ { T } ,
$$

where $D$ may have both positive and negative diagonals.

2. For any SQD matrix $K$ , the unsymmetric matrix

$$
\tilde { K } = K J = \left( \begin{array} { c c } { { M } } & { { - A } } \\ { { A ^ { T } } } & { { N } } \end{array} \right) , \quad J = \left( \begin{array} { c c } { { I _ { n } } } & { { 0 } } \\ { { 0 } } & { { - I _ { m } } } \end{array} \right) ,
$$

has a positive definite symmetric part $\begin{array} { r } { \frac 1 2 ( \tilde { K } + \tilde { K } ^ { T } ) } \end{array}$ . Gill, Saunders,and Shinnerl [477, 1996] analyze the stability of an indefinite Cholesky-type factorization using the results of Golub and Van Loan [486,1979l on LU factorization of positive definite matrices.

One approach to solving the SQD system (6.4.12) is to use Krylov methods for indefinite systems such as SYMMLQ and MINRES.However, as shown by Fischer et al. [409,1998], these make progress only in every second iteration and do not exploit the structure of SQD systems.

Eliminating either $y \in \mathbb { R } ^ { m }$ or $x \in \mathbb { R } ^ { n }$ in (6.4.12) gives the Schur complement equations

$$
\begin{array} { l } { { ( A ^ { T } M ^ { - 1 } A + N ) x = A ^ { T } M ^ { - 1 } b - c , } } \\ { { \ } } \\ { { ( A N ^ { - 1 } A ^ { T } + M ) y = A N ^ { - 1 } c + b . } } \end{array}
$$

Both of these systems are symmetric positive definite and hence can be solved by CG. After $x$ or $y$ is computed,the remaining part of the solution can be recovered from

$$
y = M ^ { - 1 } ( b - A x ) \mathrm { o r } x = N ^ { - 1 } ( A ^ { T } y - c ) .
$$

The algorithm ECGLS below solves the Schur complement equation (6.4.16). The iterates are mathematically the same as those generated by the standard CG method applied to (6.4.16). Beter numerical stability is obtained by not forming $A ^ { T } M ^ { - 1 } A$ and instead using

$$
A ^ { T } y = N x + c , \qquad y = M ^ { - 1 } ( b - A x ) .
$$

Only matrix-vector products with $A , A ^ { T } , N$ , and solves with $M$ are required.

# Algorithm 6.4.3 (Extended CGLS).

function $\begin{array} { r l } { [ { \mathbf x } , { \mathbf y } , \mathbf { s } \mathbf { t } { \mathbf s } ] } & { = \mathbf { \pi } \in \mathbf { \mathrm { e c g l s } } \left( { \textrm A } , { \textrm M } , { \textrm N } , \mathbf { b } , \mathbf { c } , \mathbf { x } 0 , \mathbf { m } \mathbf { a } \mathbf { x } \mathbf { i } \mathbf { t } \right) } \end{array}$   
$\%$ ECGLS performs maxit steps of extended CGLS on the   
$\%$ Schur complement system $\Delta ^ { \prime } * \Delta \mathsf { X } \left( \mathsf { b } - \Delta { \boldsymbol { * } } \mathbf { x } \right) \ = \ \mathbb { N } \mathbf { x } \ + \ \mathsf { c }$   
% $\begin{array} { l } { { \bf { x } _ { \alpha } = { \bf { x } } { \boldsymbol { 0 } } ; ~ { \bf { y } } = { \bf { \Theta } } { \bf { M } } \setminus \left( { \bf { b } } { \bf { \Theta } } - { \bf { \Theta } } { \bf { A } } { \bf { * } } { \bf { x } } \right) ; } } \\ { { \bf { s } _ { \alpha } = { \bf { \Theta } } { \bf { A } } ^ { \prime } { \bf { * } } { \bf { y } } - { \bf { \Theta } } { \bf { c } } - { \bf { \Theta } } { \bf { N } } { \bf { * } } { \bf { x } } ; } } \\ { { \bf { p } _ { \alpha } = { \bf { \Theta } } { \bf { s } } ; ~ \mathrm { { n r m ~ = ~ { \bf { s } } ^ { \prime } { \bf { * } } { \bf { s } } } } ; } } \\  { \bf { f } _ { \alpha } { \bf { r } } ~ { \bf { \Theta } } { \bf { \Theta } } { \bf { \Theta } } { \bf { { \bar { x } } } } = { \bf { \Theta } } { \bf { 1 } } \cdot { \bf { m } } { \bf { z } } { \bf { x } } { \bf { i } } + { \bf { \Theta } } } \end{array}$ if $\mathtt { n r m \ = \ 0 }$ ，break;end $\begin{array} { r l } & { \mathrm { ~ q ~ = ~ A \ast p ; ~ t ~ = ~ M \times q ; } } \\ & { \mathrm { ~ a l ~ p h a ~ = ~ n r m / \left( q ' \ast t ~ + ~ p ' \ast ( N \ast p ) \right) ; } } \\ & { \mathrm { ~ x ~ = ~ x ~ + ~ a l p h a \ast p ; } } \\ & { \mathrm { ~ y ~ = ~ y ~ - ~ a l \cdot p h a \ast t ; } } \\ & { \mathrm { ~ s ~ = ~ A ^ \ast \ast y ~ - ~ c ~ - ~ N \ast x ; } } \\ & { \mathrm { ~ n r m o l { \mathrm { ~ d } } = ~ n r m ; ~ n r m ~ = ~ s ~ ^ { \ast } \ast s ; } } \\ & { \mathrm { ~ b e t a ~ = ~ n r m / n r m o l { \mathrm { ~ d } } ; } } \\ & { \mathrm { ~ p ~ = ~ s ~ + ~ b e \ t a \ast p ; } } \end{array}$ end   
end

From the convergence analysis of CG it follows that the convergence of ECGLS is governed by the distribution of the nonzero eigenvalues of $( A ^ { T } M ^ { - 1 } A + N )$ .If $A$ has full column rank, ECGLS works also for $N = 0$ For $M = I$ ， $N = \mu ^ { 2 } I$ ， $\mu \neq 0$ ,and $c = 0$ ,ECGLS is equal to RCGLS.Hence,ECGLS can be viewed as an extended version of CGLS.

The Schur complement equations (6.4.17) have a similar structure to (6.4.16) and can be obtained from (6.4.16) by making the substitutions

$$
A \Longleftrightarrow A ^ { T } , \quad M \Longleftrightarrow N , \quad x \Longleftrightarrow y , \quad b \to c \quad c \to - b .
$$

Hence (6.4.17) can be solved by

$$
[ \mathbf { y } , \mathbf { x } ] = \mathtt { E C G L S } ( \mathtt { A } ^ { \prime } , \mathtt { N } , \mathtt { M } , \mathbf { c } , - \mathtt { b } , \mathtt { m a x i t } ) .
$$

The convergence is then governed by the distribution of the nonzero eigenvalues of $( A N ^ { - 1 } A ^ { T } +$ $M$ ). The SQD system (6.4.12) can be transformed as

$$
\left( \begin{array} { c c } { { L ^ { - 1 } } } & { { 0 } } \\ { { 0 } } & { { R ^ { - T } } } \end{array} \right) \left( \begin{array} { c c } { { M } } & { { A } } \\ { { A ^ { T } } } & { { - N } } \end{array} \right) \left( \begin{array} { c c } { { L ^ { - T } } } & { { 0 } } \\ { { 0 } } & { { R ^ { - 1 } } } \end{array} \right) \left( \begin{array} { c } { { L ^ { T } y } } \\ { { R x } } \end{array} \right) = \left( \begin{array} { c } { { L ^ { - 1 } b } } \\ { { R ^ { - T } c } } \end{array} \right) ,
$$

where $M = L L ^ { T }$ and $N = R ^ { T } R$ are the Cholesky factorizations. With new variables $\widetilde { y } = L ^ { T } y$ and $\widetilde { x } = R x$ ,the transformed system becomes

$$
\left( \begin{array} { c c } { { I _ { m } } } & { { \widetilde { A } } } \\ { { \widetilde { A } ^ { T } } } & { { - I _ { n } } } \end{array} \right) \left( \begin{array} { c } { { \widetilde { y } } } \\ { { \widetilde { x } } } \end{array} \right) = \left( \begin{array} { c } { { \widetilde { b } } } \\ { { \widetilde { c } } } \end{array} \right) ,
$$

where

$$
\widetilde { A } = L ^ { - 1 } A R ^ { - 1 } , \quad \widetilde { b } = L ^ { - 1 } b , \quad \widetilde { c } = R ^ { - T } c .
$$

For $c = 0$ ，problem (6.4.20) can be solved by Algorithm RCGLS or RCGME of Section 6.4.2. Each iteration requires triangular solves with $L , \bar { L } ^ { T } , R ^ { T }$ and $R$ .The rate of convergence de-pends on the eigenvalues $\lambda _ { i } = 1 + \sigma _ { i } ^ { 2 }$ , where $\sigma _ { i }$ are the singular values of $L ^ { - 1 } A R ^ { - 1 }$ . Arioli [31, 2013] calls these elliptic singular values. They are the critical points of the functional

$$
\operatorname* { m i n } _ { x , y } y ^ { T } A x { \mathrm { ~ s u b j e c t ~ t o ~ } } \| x \| _ { N } = \| y \| _ { M } = 1 .
$$

Note that since $\| \widetilde { \boldsymbol { x } } \| _ { 2 } ^ { 2 } = \| \boldsymbol { x } \| _ { N }$ and $\| \widetilde { \boldsymbol { y } } \| _ { 2 } ^ { 2 } = \| \boldsymbol { y } \| _ { M }$ , the convergence rates for $x$ and $y$ are measured in the corresponding elliptic error norm.

Arioli [31, 2o13] develops elliptic versions of upper and lower GKL bidiagonalization that generalize results by Benbow [1O4,1999]. These generate left and right basis vectors $u _ { i }$ and $v _ { i }$ that are orthonormal with respect to the inner products defined by $M$ and $N$ ,respectively. Each step of the bidiagonalizations requires solves with both $M$ and $N$ . Based on these bidiagonaliza-tion processes, Arioli and Orban [844, 2O17] derive versions of LSQR and related algorithms for solving SQD systems with either $c = 0$ or $b = 0$ . When both $b \neq 0$ and $c \neq 0$ , it is necessary to either shift the right-hand side to obtain one of these special cases or solve two special systems and add the solutions.

# Notes and references

In some applications the Cholesky factorization of $M$ and $N$ is not available, but matrix-vector products with $M ^ { - 1 }$ can be performed efficiently. Friedlander and Orban [434, 2o12] give such an example from interior methods for nonlinear programs, where a limited-memory approximation is used to represent $M ^ { - 1 }$ . For the special case when $A$ has full column rank and $N = 0$ ,Calandra et al.[198,2o2o] derive an algorithm similar to ECGLS and analyze its stability.Montoison and Orban [801, 2021] develop two new iterative methods, TRICG and TRIMR, that handle SQD systems with general $b$ and $c$ ，These methods are based on the orthogonal tridiagonalization process of Saunders, Simon,and Yip [966,1988].

# 6.4.4 - Hybrid Regularization and LSQR

Krylov subspace methods, such as CGLS and LSQR,applied to an (unregularized) least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ often tend to converge quickly to an approximate solution corre-sponding to the dominating singular values of $A$ .Hence they are well suited to ill-posed problems.Theoretical results predict similar bounds for the optimal accuracy of LSQR to those for truncated SVD (TSVD); see Example 4.2.8. Because the approximations in LSQR are tailored to the specific right-hand side $b$ ,the minimum error is often achieved with a subspace of much lower dimension compared to TSVD.For LSQR the iterations also diverge more quickly after the optimal accuracy has been reached.For very il-conditioned problems, partial reorthogonalization of the $u$ and $v$ vectors in LSQR (or LSMR) may help to preserve stability. This is costly in terms of storage and operations but may be acceptable when the number of iterations is small; see Section 6.2.6.

For iterative regularization methods,it is essential to terminate the iterations before diver-gence starts. Using a hybrid method that combines the iterative method with an inner regularization can be an effective solution; see Hanke [568,2oo1]. For example,the iterative method can be applied to the Tikhonov regularized problem

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { l } { A } \\ { \lambda L } \end{array} } \right) x - \left( { \begin{array} { l } { b } \\ { 0 } \end{array} } \right) \right\| .
$$

Such hybrid methods require two regularization parameters: the number of iterations $k$ and $\lambda$ With an appropriate choice of $L$ ,difficulties related to semiconvergence may be overcome. The iterations can be continued until all relevant information available from the data has been captured.

Taking $L = I$ in (6.4.23) gives the standard Tikhonov regularization. Then it can be verified that the iterate $x _ { k , \lambda }$ obtained by LSQR is the same as that obtained by first performing $k$ steps of LSQR on the unregularized problem ( $\lambda = 0$ ）and then solving the regularized subproblem

$$
\operatorname* { m i n } _ { y _ { k , \lambda } } \left\| \left( { \begin{array} { c } { B _ { k } } \\ { \lambda I _ { k } } \end{array} } \right) y _ { k , \lambda } - \left( { \begin{array} { c } { \beta _ { 1 } e _ { 1 } } \\ { 0 } \end{array} } \right) \right\| _ { 2 }
$$

and setting $x _ { k , \lambda } = V _ { k } y _ { k , \lambda }$ . In other words, for $L = I$ ，iteration and regularization commute. This observation allows $\lambda$ to be varied without restarting LSQR. The subproblems (6.4.24) can be solved in $O ( k )$ operations using plane rotations, and $y _ { k , \lambda }$ can be determined for several values of $\lambda$ at each step. However, to get the corresponding $x _ { k , \lambda }$ the vectors $v _ { 1 } , \ldots , v _ { k }$ are needed. If there is not enough space to store these vectors,they can be generated anew by running the bidiagonalization again for each $\lambda$

Several alternative regularization methods besides Tikhonov regularization have been pro-posed for LSQR's bidiagonal subproblem

$$
\operatorname* { m i n } _ { y _ { k } } \| B _ { k } y _ { k } - \beta _ { 1 } e _ { 1 } \| _ { 2 } , \quad B _ { k } \in \mathbb { R } ^ { ( k + 1 ) \times k } .
$$

O'Leary and Simmons [840,1981] use a TSVD solution to (6.4.25). At each step of the bidiagonalization process, the SVD of $\left( \begin{array} { l l } { B _ { k } } & { \beta _ { 1 } e _ { 1 } } \end{array} \right)$ is computed. This can be done by standard methods in $O ( k ^ { 2 } )$ operations. Computational details of this and similar schemes are considered by Bjorck [131,1g88]. When no a priori information about the solution is available, generalized cross-validation (GCV) can be used to determine the number of terms in the TSVD solution as suggested by Bjorck, Grimme,and Van Dooren [145,1994].

When $L \neq I$ , iteration and regularization no longer commute. Restarting LSQR when $\lambda$ is changed is usually too demanding computationally,and an initial transformation to standard form is to be preferred. When $\ b { L } \in \mathbb { R } ^ { n \times n }$ is nonsingular, this is achieved by setting $y = L x$ and $\bar { A } = A L ^ { - 1 }$ . Otherwise, if $L \in \mathbb { R } ^ { p \times n }$ and $p < n$ ， $L$ has a nontrivial nullspace. Then we take $\bar { A } = A L _ { A } ^ { \dagger }$ , where

$$
\boldsymbol { L } _ { A } ^ { \dagger } = ( I - ( A ( I - \boldsymbol { L } ^ { \dagger } \boldsymbol { L } ) ) ^ { \dagger } \boldsymbol { A } ) \boldsymbol { L } ^ { \dagger }
$$

is the $A$ -weighted (oblique) pseudoinverse; see Section 3.6.5. The standard form problem then becomes

$$
\operatorname* { m i n } _ { y } \| A L _ { A } ^ { \dag } y - b \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| y \| _ { 2 } ^ { 2 } , \qquad x ( \lambda ) = L _ { A } ^ { \dag } y _ { \lambda } + x _ { 2 } ,
$$

where $x _ { 2 } \in \mathcal { N } ( L )$ is the unregularized component of the solution. For several frequently used regularization matrices,this transformation can be implemented so that the extra work is negligible. Assume that $L$ has full row rank $n - p$ ,and compute the two QR factorizations

$$
L ^ { T } = \left( W _ { 1 } W _ { 2 } \right) { \binom { R } { 0 } } = W _ { 1 } R , A W _ { 2 } = Q _ { 1 } U ,
$$

where $W _ { 2 }$ gives an orthogonal basis for $\mathcal { N } ( L )$ .If $p \ll n$ ,the work in the QR factorization of $A W _ { 2 }$ is negligible. Then,

$$
{ \cal L } _ { \cal A } ^ { \dagger } = ( I - P ) W _ { 1 } R ^ { - 1 } , \qquad P = W _ { 2 } ( A W _ { 2 } ) ^ { \dagger } A = W _ { 2 } U ^ { - 1 } Q _ { 1 } ^ { T } A ,
$$

and

$$
x _ { 2 } = W _ { 2 } ( A W _ { 2 } ) ^ { \dagger } b = W _ { 2 } U ^ { - 1 } Q _ { A W } ^ { T } b .
$$

For several discrete smoothing norms, $L$ can be partitioned as $L = \left( \begin{array} { c c } { { L _ { 1 } } } & { { L _ { 2 } } } \end{array} \right)$ ，where $L _ { 1 }$ is square and of full rank. Then the computationally simpler expression

$$
L _ { A } ^ { \dag } = \left( I - P \right) \binom { L _ { 1 } ^ { - 1 } } { 0 }
$$

can be used; see Hanke and Hansen [570,1993].

In high-dimensional problems,e.g., when $L$ is a sum of Kronecker products, the matrix $A L _ { A } ^ { \dagger }$ may become too complicated to work with. For this case,an alternative projection approach that only uses products with $L$ and $L ^ { T }$ has been suggested by Kilmer, Hansen,and Espanol [695, 2007]. Inspired by work of Zha [1145,1996], this uses a joint bidiagonalization of $Q _ { A }$ and $Q _ { L }$ in the QR factorization

$$
\binom { A } { L } = \binom { Q _ { A } } { Q _ { L } } R .
$$

# 6.4.5 - Regularization with GMRES and MINRES

The regularizing properties of GMRES and MINRES (see Section 6.2.7) are not well understood. The large eigenvalues of $A$ are usually simulated rapidly by those of the Hessenberg matrices $H _ { k + 1 , k }$ in GMRES (for small values of $k$ ). In discrete il-posed problems,the spectrum of $A$ is characterized by a sizeable gap between a large group of numerically zero eigenvalues and the rest of the spectrum. As shown by Calveti, Lewis,and Reichel [2O2, 2oo2], GMRES equipped with a suitable stopping rule can deliver better approximations than TSVD.For severely ilconditioned problems with singular values $\sigma _ { k } ~ = ~ O ( e ^ { - \alpha k } )$ it holds that $h _ { k + 1 , k } \ = \ O ( n \sigma _ { k } )$ For symmetric matrices, GMRES and MINRES have regularization properties similar to CGLS; see Jensen and Hansen [666, 2oo7]. However, for nonsymmetric matrices the regularization properties of GMRES are highly problem dependent. For some problems,GMRES does not produce regularized solutions.

In the Arnoldi-Tikhonov regularization method, the regularized problem

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| L x \| _ { 2 } ^ { 2 }
$$

is approximated by taking $x _ { k } = V _ { k } y _ { k } \in { \mathcal { K } } _ { k } ( A , b )$ and using (6.2.69) to obtain the projected problem

$$
\operatorname* { m i n } _ { y \in \mathbb { R } ^ { k } } \left\| \left( \begin{array} { c } { H _ { k + 1 , k } } \\ { \lambda L V _ { k } } \end{array} \right) y _ { k } - \left( \begin{array} { c } { \beta _ { 1 } e _ { 1 } } \\ { 0 } \end{array} \right) \right\| _ { 2 } .
$$

For the standard case $L = I$ ，this method was introduced by Calvetti et al.[2O3,2ooo].The regularization term simplifies because $\| L V _ { k } y _ { k } \| _ { 2 } ^ { 2 } = \| y _ { k } \| _ { 2 } ^ { 2 }$ . Then (6.4.32) is equivalent to an inner regularization of the projected problem and may be used in a hybrid method. This simplifies the use of parameter choice rules for $\lambda$ ,such as the GCV and L-curve criteria.

The choice of a regularization term with $L \neq I$ in (6.4.31) is known to be potentially much more useful. If $L \in \mathbb { R } ^ { p \times n }$ ,the system has dimension $( k + p ) \times k$ ， where often $p \gg k$ To solve subproblem (6.4.32) one may first compute the compact QR factorization $L V _ { k } = Q _ { k } R _ { k }$ ， $R _ { k } \in \mathbb { R } ^ { k \times k }$ , and use the identity $\| { L V _ { k } y _ { k } } \| _ { 2 } = \| { R _ { k } y _ { k } } \| _ { 2 }$ . The reduced subproblem is then solved by a sequence of Givens transformations.

GMRES applied to a singular system can break down before a solution has been found. The following property is proved by Brown and Walker [182,1997].

Theorem 6.4.1. For all $b$ and starting approximations $x _ { 0 }$ ，GMRES determines a least squares solution $x ^ { * }$ of a singular system $A x = b$ without breakdown if and only if ${ \mathcal { N } } ( A ) = { \mathcal { R } } ( A ^ { T } )$ Furthermore,if the system is consistent and $x _ { 0 } \in \mathcal { R } ( A ^ { T } )$ ，then $x ^ { * }$ is a least-norm solution.

A variant of MINRES called MR-II and introduced by Hanke [567,1995] has starting vector $A b$ and generates approximations $x _ { k } \in \mathcal { K } ( A , A b )$ . The multiplication with $A$ acts as a smoothing operator and dampens high-frequency noise in $b$ . Range-restricted GMRES is a similar method for the nonsymmetric case due to Calveti, Lewis,and Reichel [2O0, 2ooo]. This is based on the Arnoldi process and also generates approximations $x _ { k } \in \mathcal { K } _ { k } ( A , A b )$ . These methods sometimes provide better regularized solutions than GMRES and MINRES but can cause a loss of information in the data $b$ ； see Calvetti, Lewis,and Reichel [2O1, 2001].

If $\operatorname { r a n k } ( A ) < n$ , it is no restriction to assume the structure

$$
\left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right) = \left( \begin{array} { c } { b _ { 1 } } \\ { b _ { 2 } } \end{array} \right) ,
$$

where $A _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is nonsingular. Then the condition in Theorem 6.4.1 where ${ \mathcal { N } } ( A ) = { \mathcal { R } } ( A ^ { T } )$ is equivalent to $A _ { 1 2 } = 0$ ,and the system is consistent if and only if $b _ { 2 } = 0$ . If these conditions are satisfied,applying GMRES to (6.4.33) is equivalent to applying GMRES to the nonsingular system $A _ { 1 1 } x _ { 1 } = b _ { 1 }$ . In practice it is usually the case that $A _ { 1 2 }$ and $b _ { 2 }$ are nonzero but small.

A common approach is to choose $M$ as an approximation to $A$ in which the small eigenvalues are replaced by ones.Eldén and Simoncini [382, 2O12] show that a similar effect is obtained by taking $M$ to be a singular preconditioner equal to a low-rank approximation to $A$ and applying GMRES to

$$
A M ^ { \dagger } y = b , \quad x = M ^ { \dagger } y .
$$

In the initial iterations the residual components corresponding to large eigenvalues will be reduced in norm.This approach is particularly suitable for il-posed problems from partial differential equations in two or three dimensions,such as the Cauchy problem with variable coefficients. A fast solver for a nearby problem can then be used as a singular preconditioner.

# Notes and references

Surveys of methods for regularization of large-scale problems are given by Hanke and Hansen [570,1993] and Hansen [579,2o1o]. Nemirovskii [826,1986] gives a strict proof of the regular-izing properties of CG methods and shows that CGLS and LSQR reach about the same accuracy as Landweber's method before divergence starts. Hanke [568, 2oo1] compares the regularizing properties of CGLS and CGME,and Jia [669,202o] studies the regularizing effects of CGME, LSQR,and LSMR. Wei, Xie,and Zhang [1115, 2o16] propose combining Tikhonov regularization with a randomized algorithm for truncated GSVD.

Fierro et al. [404,1997] propose using GKL bidiagonalization for computing truncated TLS (TTLS) solutions. The use of bidiagonalization in Tikhonov regularization of large linear problems is further analyzed by Calveti and Reichel [2O4, 2oo3]. The choice of regularization parameters in iterative methods is studied by Kilmer and O'Leary [696, 2oo1]. Hnetynkova, Plesinger, and Strakos [631,2oog] use bidiagonalization to estimate the noise level in the data.

Novati and Russo [834, 2o14] give theoretical results on convergence properties of the Arnoldi-Tikhonov method with $L \neq I$ 、Gazzola,Novati,and Russo [449, 2015] survey hybrid Krylov projection methods for Tikhonov regularized problems. They observe experimentally that the method is very efficient for discrete il-posed problems where the singular values cluster at zero. They also investigate use of the GCV criterion within the Arnoldi-Tikhonov method. A MATLAB package of iterative regularization methods called IR Tools is implemented by Gazzola, Hansen, and Nagy [448, 2o18]. This package also contains a set of large-scale test problems.

# 6.4.6 - Augmented and Deflated CGLS

Deflation and augmentation techniques have been used in a variety of contexts to accelerate the convergence of Krylov subspace methods. In augmentation, a subspace is added to the Krylov subspace.For example,for linear systems with multiple right-hand sides,the Krylov subspace can be augmented to include information from previously solved systems.In deflation, the system to be solved is multiplied by a projection that removes certain parts from the operator. For example, components corresponding to small singular values that may slow down convergence can be removed. This reduces the effective condition number and can significantly improve convergence. Often,deflation is combined with augmentation to compensate for the singularity of the operator.

Let $C x = d$ be a symmetric positive definite linear system,and let

$$
W = ( w _ { 1 } , w _ { 2 } , \ldots , w _ { p } ) \in \mathbb { R } ^ { n \times p }
$$

be a set of $p$ linearly independent vectors that span a subspace to be added or removed. Then both $C$ and $W ^ { T } C W$ are symmetric positive definite. The deflated Lanczos process is obtained by applying the standard Lanczos process auxiliary matrix

$$
\boldsymbol { B } = \boldsymbol { C } \boldsymbol { H } , \quad \boldsymbol { H } = \boldsymbol { I } - \boldsymbol { W } ( \boldsymbol { W } ^ { T } \boldsymbol { C } \boldsymbol { W } ) ^ { - 1 } ( \boldsymbol { C } \boldsymbol { W } ) ^ { T } ,
$$

where $B$ is symmetric positive semidefinite and satisfes $W ^ { T } B = 0$ .Furthermore, $H ^ { 2 } = H$ ， and $H$ is the $C$ -orthogonal oblique projection onto $W ^ { \perp _ { C } }$ . The matrix

$$
\begin{array} { r } { H ^ { T } = I - C W ( W ^ { T } C W ) ^ { - 1 } W ^ { T } } \end{array}
$$

is the $C ^ { - 1 }$ orthogonal projection onto $W ^ { \perp }$ . It is easily verified that

$$
B = C H = H ^ { T } C = H ^ { T } C H .
$$

Let $v _ { 1 }$ be a unit vector such that $W ^ { T } v _ { 1 } = 0$ . Then the standard Lanczos process applied to $B$ with starting vector $v _ { 1 }$ generates a sequence $\{ v _ { j } \}$ of mutually orthogonal unit vectors $v _ { j }$ such that

$$
v _ { j + 1 } \perp \operatorname { s p a n } \left\{ W \right\} + { \mathcal { K } } _ { j } ( C , v _ { 1 } ) \equiv { \mathcal { K } } _ { j } ( C , W , v _ { 1 } ) .
$$

The generated vectors satisfy

$$
B V _ { j } = V _ { j } T _ { j } + \beta _ { j + 1 } v _ { j + 1 } e _ { j } ^ { T } ,
$$