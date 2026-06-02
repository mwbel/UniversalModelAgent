where $V _ { j } = ( v _ { 1 } , v _ { 2 } , \ldots , v _ { j } )$ and

$$
T _ { j } = \left( \begin{array} { c c c c c c } { { \alpha _ { 1 } } } & { { \beta _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \beta _ { 2 } } } & { { \alpha _ { 2 } } } & { { \beta _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \beta _ { j - 1 } } } & { { \alpha _ { j - 1 } } } & { { \beta _ { j } } } \\ { { } } & { { } } & { { } } & { { } } & { { \beta _ { j } } } & { { \alpha _ { j } } } \end{array} \right) .
$$

From (6.4.35) it follows that

$$
\beta _ { j + 1 } v _ { j + 1 } = B v _ { j } - \beta _ { j } v _ { j - 1 } - \alpha _ { j } v _ { j } .
$$

With induction and noting that $W ^ { T } B = 0$ , we see that $W ^ { T } v _ { j + 1 } = 0$ ， $j = 1 , 2 , \dots { }$

Saad et al. [961, 2ooo] derive a deflated CG method for solving a symmetric positive definite system $C x = d$ from the deflated Lanczos process.The resulting method is defined by the conditions

$$
\begin{array} { r } { x _ { j + 1 } - x _ { j } \in { \cal K } _ { j } ( C , W , r _ { 0 } ) , } \end{array}
$$

where

$$
r _ { 0 } = d - C x _ { 0 } \perp W , \quad r _ { j } \perp K _ { j } ( C , W , r _ { 0 } ) .
$$

An $x _ { 0 }$ such that $W ^ { T } r _ { 0 } = 0$ is given by

$$
x _ { 0 } = x _ { - 1 } + { \cal W } ( { \cal W } ^ { T } { \cal C } { \cal W } ) ^ { - 1 } { \cal W } ^ { T } r _ { - 1 } , \quad r _ { - 1 } = d - { \cal C } x _ { - 1 } ,
$$

where $x _ { - 1 }$ is arbitrary. In particular, setting $x _ { - 1 } = 0$ gives $x _ { 0 } = W ( W ^ { T } C W ) ^ { - 1 } W ^ { T } d .$ The residual vectors $s _ { j }$ in deflated CG satisfy $r _ { j } / \| r _ { j } \| _ { 2 } = v _ { j }$ , where vectors $v _ { j }$ are from the Lanczos process applied to $B$ ．It follows that the residuals $r _ { j }$ are mutually orthogonal. The descent directions $p _ { j }$ are $C$ -orthogonal to each other and also $C$ -orthogonal to all vectors $w _ { i }$ ,i.e.,

$$
\begin{array} { r } { P _ { j } ^ { T } C P _ { j } = 0 , \qquad W ^ { T } C P _ { j } = 0 . } \end{array}
$$

The deflated CG method can be viewed as a preconditioned CG (PCG) method with singular preconditioner $H H ^ { T }$ . In the taxonomy definedby Ashby,Manteuffel,and Saylor [40,1990], it is equivalent to the version $\mathrm { O m i n } ( C , H H ^ { T } , C )$ of PCG started with $r _ { 0 } \perp W$

A deflated version of CGLS is_obtained by taking $C = A ^ { T } A$ ， $d = A ^ { T } b$ and applying the deflated CG method to $A ^ { T } A x = A ^ { T } b$ ，with the special starting point $x _ { 0 } = P b$ ,where

$$
P = W ( W ^ { T } A ^ { T } A W ) ^ { - 1 } ( A W ) ^ { T }
$$

is a projector. Each iteration requires one application of $P$ to a vector. This operation can be sped up by initially computing the product $A W$ and its thin QR factorization $A W = Q R$ giving $P = W R ^ { - 1 } Q ^ { T }$ . The following properties of the deflated CGLS algorithm follow from results shown by Saad et al. [961,2ooo]; see Theorem 4.2 and Theorem 4.3.

Theorem 6.4.2. Let $A \in \mathbb { R } ^ { m \times n }$ and $W \in \mathbb { R } ^ { m \times p }$ have full column rank. Let $x ^ { * }$ be the exact solution of the least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ . Then the deflated CGLS algorithm will not break down at any step. The approximate solution $x _ { k }$ is the unique minimizer of the error norm $\| r _ { k } - r ^ { * } \| _ { 2 }$ ， $r _ { k } = b - A x _ { k }$ ,over the affine solution space $x _ { 0 } + \mathcal { K } _ { p , k } \mathopen { } \mathclose \bgroup \left( A ^ { T } A , W , r _ { 0 } \aftergroup \egroup \right)$ .Further, an upper bound for the residual error after $k$ iterations is given by

$$
\| r _ { k } - r ^ { * } \| _ { 2 } \leq 2 { \biggl ( } { \frac { \kappa ( A H ) - 1 } { \kappa ( A H ) + 1 } } { \biggr ) } ^ { k } \| r - r _ { 0 } \| _ { 2 } ,
$$

where $H$ is the oblique projector defined in (6.4.35).

# Notes and references

Nicolaides [830, $\mathbf { 1 9 8 7 } ]$ derives a deflated CG method that uses the three-term recurrence of Lanc-Zos. The idea of augmenting a Krylov subspace method with vectors to improve the convergence is discussed by Morgan [810,1995]. Variations and applications of deflated and augmented Krylov subspace methods are surveyed by Simoncini and Szyld [998, 2oo7,Section 9]. A general framework for augmented and deflated Krylov subspace methods is given by Gaul et al. [443, 2013].Baglama,Reichel,and Richmond [58,2o13] describe an LSQR algorithm augmented with harmonic Ritz vectors associated with small singular values for accelerating il-posed least squares problems.

Chapter 7

# SVD Algorithms and Matrix Functions

# 7.1 - The QRSVD Algorithm

# 7.1.1 - The LR and QR Iterations

Suppose that $A \in \mathbb { C } ^ { n \times n }$ has the LU factorization $A = L U$ .Then $U = L ^ { - 1 } A$ , and multiplying the factors in reverse order performs the similarity transformation

$$
\widetilde { A } = U L = L ^ { - 1 } A L .
$$

Hence $A$ and $\widetilde { A }$ have the same eigenvalues,and the eigenvectors are related by $\widetilde { X } = L ^ { - 1 } X$ In the LR algorithm of Rutishauser [947,1958] this process is iterated. Setting $A _ { 1 } = A$ and

$$
A _ { k } = L _ { k } U _ { k } , \qquad A _ { k + 1 } = U _ { k } L _ { k } , \quad k = 1 , 2 , \ldots ,
$$

generates a sequence of similar matrices such that

$$
A _ { k } = L _ { k - 1 } ^ { - 1 } \cdot \cdot \cdot L _ { 2 } ^ { - 1 } L _ { 1 } ^ { - 1 } A L _ { 1 } L _ { 2 } \cdot \cdot \cdot L _ { k - 1 } , \quad k = 2 , 3 , \ldots .
$$

Define the lower and upper triangular matrices

$$
T _ { k } = L _ { 1 } \cdot \cdot \cdot L _ { k - 1 } L _ { k } , \qquad S _ { k } = U _ { k } U _ { k - 1 } \cdot \cdot \cdot U _ { 1 } , \quad k = 1 , 2 , \ldots .
$$

Then $T _ { k - 1 } A _ { k } = A T _ { k - 1 }$ , and forming the product $T _ { k } S _ { k }$ ,we obtain

$$
T _ { k } S _ { k } = T _ { k - 1 } ( L _ { k } U _ { k } ) S _ { k - 1 } = T _ { k - 1 } A _ { k } S _ { k - 1 } = A T _ { k - 1 } S _ { k - 1 } .
$$

By induction it follows that

$$
T _ { k } S _ { k } = A ^ { k } , \quad k = 1 , 2 , \ldots .
$$

This exhibits the close relationship between the LR algorithm and the power method. This is one of the oldest methods for computing eigenvalues and eigenvectors of a matrix. It is particularly suitable for finding a few extreme eigenvalues and the corresponding eigenvectors； see Section 7.3.1. It is also directly or indirectly the basis for many other algorithms for singular values and vectors.

When $A$ is real symmetric and positive definite the Cholesky factorization $A = L L ^ { T }$ can be used in the LR algorithm. Then the algorithm becomes

$$
A _ { k } = L _ { k } L _ { k } ^ { T } , \qquad A _ { k + 1 } = L _ { k } ^ { T } L _ { k } , \quad k = 1 , 2 , \ldots .
$$

Clearly, $A _ { k + 1 }$ is again symmetric and positive definite,and therefore the recurrence is well defined. Repeated application of (7.1.5) gives

$$
A _ { k } = T _ { k - 1 } ^ { - 1 } A _ { 1 } T _ { k - 1 } = T _ { k - 1 } ^ { T } A _ { 1 } ( T _ { k - 1 } ^ { - 1 } ) ^ { T } ,
$$

where $T _ { k } = L _ { 1 } L _ { 2 } \cdot \cdot \cdot L _ { k }$ .Further, we have

$$
A ^ { k } = ( L _ { 1 } L _ { 2 } \cdot \cdot \cdot L _ { k } ) ( L _ { k } ^ { T } \cdot \cdot \cdot L _ { 2 } ^ { T } L _ { 1 } ^ { T } ) = T _ { k } T _ { k } ^ { T } .
$$

Under certain restrictions the sequence of matrices $A _ { k }$ converges to a diagonal matrix whose elements are the eigenvalues of $A$

The QR algorithm is similar to the LR algorithm but uses orthogonal similarity transformations

$$
A _ { k } = Q _ { k } R _ { k } , \qquad A _ { k + 1 } = R _ { k } Q _ { k } = Q _ { k } ^ { H } A _ { k } Q _ { k } , \quad k = 1 , 2 , \dots .
$$

The resulting matrix $A _ { k + 1 }$ is similar to $A _ { 1 } = A$ .Successive iterates of the QR algorithm satisfy relations similar to those derived for the LR algorithm. By repeated application of (7.1.8) it follows that

$$
P _ { k } A _ { k + 1 } = A P _ { k } , \quad P _ { k } = Q _ { 1 } Q _ { 2 } \cdot \cdot \cdot Q _ { k } .
$$

Furthermore, setting $U _ { k } = R _ { k } \cdot \cdot \cdot R _ { 2 } R _ { 1 }$ , we have

$$
P _ { k } U _ { k } = P _ { k - 1 } ( Q _ { k } R _ { k } ) U _ { k - 1 } = P _ { k - 1 } A _ { k } U _ { k - 1 } = A P _ { k - 1 } U _ { k - 1 } ,
$$

and by induction,

$$
P _ { k } U _ { k } = A ^ { k } , \quad k = 1 , 2 , . . . .
$$

For the QR algorithm we have $A _ { k } ^ { T } = A _ { k } = R _ { k } ^ { T } Q _ { k } ^ { T }$ and hence

$$
A _ { k } ^ { T } A _ { k } = A _ { k } ^ { 2 } = R _ { k } ^ { T } Q _ { k } ^ { T } Q _ { k } R _ { k } = R _ { k } ^ { T } R _ { k } ,
$$

i.e., $R _ { k } ^ { T }$ is the lower triangular Cholesky factor of $A _ { k } ^ { 2 }$ . For the Cholesky LR algorithm we have from (7.1.7) that

$$
A _ { k } ^ { 2 } = L _ { k } L _ { k + 1 } ( L _ { k } L _ { k + 1 } ) ^ { T } .
$$

By uniqueness, the Cholesky factorizations (7.1.11) and (7.1.12) of $A _ { k } ^ { 2 }$ must be the same, and therefore $R _ { k } ^ { T } = L _ { k } L _ { k + 1 }$ . Thus

$$
A _ { k + 1 } = R _ { k } Q _ { k } = R _ { k } A _ { k } R _ { k } ^ { - 1 } = L _ { k + 1 } ^ { T } L _ { k } ^ { T } A _ { k } ( L _ { k + 1 } ^ { T } L _ { k } ^ { T } ) ^ { - 1 } .
$$

Comparing this with (7.1.6) shows that two steps ofthe Cholesky $L R$ algorithm are equivalent to one step in the QR algorithm.

# 7.1.2 - Reduction to Compact Form

For a matrix $A \in \mathbb { R } ^ { n \times n }$ ,one step of the symmetric QR algorithm requires $O ( n ^ { 3 } )$ flops, which is too much and makes the algorithm impractical. We start by noting that the orthogonal similarity of a real symmetric matrix $A$ is again real symmetric.Furthermore, the QR iteration preserves the upper and lower bandwidths of a band matrix. In particular, the QR algorithm preserves the real symmetric tridiagonal form

$$
Q ^ { H } A Q = T = \left( \begin{array} { c c c c c c } { { \alpha _ { 1 } } } & { { \beta _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \beta _ { 2 } } } & { { \alpha _ { 2 } } } & { { \beta _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \beta _ { n - 1 } } } & { { \alpha _ { n - 1 } } } & { { \beta _ { n } } } \\ { { } } & { { } } & { { } } & { { \beta _ { n } } } & { { \alpha _ { n } } } \end{array} \right) .
$$

Matrix shapes invariant under symmetric QR algorithms are studied by Arbentz and Golub [30, 1995l. An initial reduction to real tridiagonal form reduces the arithmetic cost per step in the QR algorithm to $O ( n )$ flops.The reduction can be carried out by a sequence of Householder reflections

$$
P = I - \beta u u ^ { H } , \quad \beta = 2 / u ^ { H } u .
$$

In the $k$ th step, $A ^ { ( k + 1 ) } = P _ { k } A ^ { ( k ) } P _ { k }$ ，where $P _ { k }$ is chosen to zero the last $n - k - 1$ elements in the $k$ th column. Dropping the subscripts $k$ ,we write

$$
\boldsymbol { P } \boldsymbol { A } \boldsymbol { P } = \boldsymbol { A } - \boldsymbol { u } \boldsymbol { p } ^ { H } - \boldsymbol { p } \boldsymbol { u } ^ { H } + \beta \boldsymbol { u } ^ { H } \boldsymbol { p } \boldsymbol { u } \boldsymbol { u } ^ { H } = \boldsymbol { A } - \boldsymbol { u } \boldsymbol { q } ^ { H } - \boldsymbol { q } \boldsymbol { u } ^ { H } ,
$$

where $p = \beta A u$ ， $q = p - \gamma u$ ,and $\gamma = \beta u ^ { H } p / 2$ .The operation count for this reduction is about $2 n ^ { 3 } / 3$ flops. A complex Hermitian matrix $A \in \mathbb { C } ^ { n \times n }$ can be reduced to real tridiagonal form $T$ by a sequence of similarity transformations with complex Householder reflections.

The reduction to symmetric tridiagonal form is normwise backward stable.This ensures that the larger eigenvalues will be computed with high relative accuracy. However, if the reduction is performed starting from the top row,then the matrix should be ordered so that the larger elements occur in the top left corner. This ensures the errors in the orthogonal reduction correspond to small relative errors in the elements of $A$ ,and the small eigenvalues will not be destroyed.

If the reduction to tridiagonal form is carried out for a symmetric band matrix $A$ in a similar way, then the band structure will be destroyed in the intermediate matrices.By annihilating pairs of elements using plane rotations in an ingenious order,the reduction can be performed without increasing the intermediate bandwidth; see Rutishauser [949,1963] and Schwarz [977,1968].

For computing the SVD of a matrix $A \in \mathbb { C } ^ { m \times n }$ it is advantageous to reduce it initially to real bidiagonal form:

$$
A = Q _ { B } \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) P _ { B } ^ { T } , \quad B = \left( \begin{array} { l l l l l } { \rho _ { 1 } } & { \gamma _ { 2 } } & & & \\ & { \rho _ { 2 } } & { \gamma _ { 3 } } & & \\ & & { \ddots } & { \ddots } & \\ & & & { \rho _ { n - 1 } } & { \gamma _ { n } } \end{array} \right) \in \mathbb { R } ^ { n \times n } .
$$

As described in Section 4.2.1, this can be achieved by taking $P$ and $Q$ as products of Householder matrices. The resulting matrix $B$ has the same singular values as $A$ ,and the singular vectors of $B$ and $A$ are simply related. Note that both $B ^ { T } B$ and $B B ^ { T }$ are tridiagonal.

The QR factorization of $A \in \mathbb { R } ^ { m \times n }$ requires $2 ( m n ^ { 2 } - n ^ { 3 } / 3 )$ flops or twice as many if $Q$ is needed explicitly. This cost usually dominates the total cost of computing the SVD.If only the singular values are required, then the cost of bidiagonalization typically is $90 \%$ of the total cost. If singular vectors are wanted, then the explicit transformation matrices are needed, but the reduction still accounts for more than half the total cost.

The errors from the bidiagonal reduction may often account for most of the errors in the computed singular values.To minimize these errors the reduction should preferably be done as a two-step procedure. In the first step a QR factorization with column pivoting of $A$ is performed:

$$
A \Pi = Q _ { R } \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) , \quad R \in \mathbb { R } ^ { n \times n } .
$$

Next, $R$ is reduced to upper bidiagonal form, which takes $8 n ^ { 3 } / 3$ flops, or twice as many if the left and right transformation matrices are wanted explicitly. Presorting the rows of $A$ by decreasing norms before the QR factorization can also reduce the relative errors in the singular values; see Higham [622, 2000] and Drmac [335, 2017].

Note that a bidiagonal matrix with complex elements can always be transformed into real form by a sequence of unitary diagonal scalings from the left and right. In the first step, $D _ { 1 } =$ $\mathrm { d i a g } \left( e ^ { i \alpha _ { 1 } } , 1 , \ldots , 1 \right)$ is chosen to make the $( 1 , 1 )$ element in $D _ { 1 } B$ real. Next, $D _ { 2 } = \mathrm { d i a g } \left( 1 , e ^ { i \alpha _ { 2 } } \right.$ $1 , \ldots , 1 )$ is chosen to make the $( 1 , 2 )$ element in $( D _ { 1 } B ) D _ { 2 }$ real, and so on.

Let $\sigma _ { i }$ ， $i = 1 : n$ ,be the singular values,and let $u _ { i }$ and $v _ { i }$ be the corresponding left and right singular vectors of the upper bidiagonal matrix $B$ in (7.1.15). Then the eigenvalues and eigenvectors of the Jordan-Wielandt matrix $W$ are given by

$$
W \left( \begin{array} { c } { { u _ { i } } } \\ { { \pm v _ { i } } } \end{array} \right) = \pm \sigma _ { i } \left( \begin{array} { c } { { u _ { i } } } \\ { { \pm v _ { i } } } \end{array} \right) , \quad W = \left( \begin{array} { c c } { { 0 } } & { { B } } \\ { { B ^ { T } } } & { { 0 } } \end{array} \right) .
$$

By an odd-even permutation the matrix $W$ can be brought into the special real symmetric tridiagonal form

$$
G = P W P ^ { T } = \left( \begin{array} { c c c c c c c } { 0 } & { \rho _ { 1 } } & & & & & \\ { \rho _ { 1 } } & { 0 } & { \gamma _ { 2 } } & & & & \\ & { \gamma _ { 2 } } & { 0 } & { \rho _ { 2 } } & & & \\ & & { \rho _ { 2 } } & { \ddots } & { \ddots } & & \\ & & & { \ddots } & { \ddots } & { \gamma _ { n } } & \\ & & & & { \gamma _ { n } } & { 0 } & { \rho _ { n } } \\ & & & & & { \rho _ { n } } & { 0 } \end{array} \right) \in \mathbb { R } ^ { 2 n \times 2 n } ,
$$

with zero diagonal elements first considered by Golub and Kahan [495,1965].

# 7.1.3- Zero-Shift QRSVD Algorithm

Let $A = Q R \in \mathbb { R } ^ { m \times n }$ be the QR factorization of $A$ Set $R _ { 0 } = R$ , and compute the sequence $R _ { 1 } , R _ { 2 } , \dotsc$ of upper triangular matrices by

$$
R _ { k - 1 } ^ { T } = Q _ { k } R _ { k } , \quad k = 1 , 2 , \ldots .
$$

That is, the upper triangular $R _ { k }$ is obtained from the QR factorization of the lower triangular matrix $R _ { k - 1 } ^ { T }$ Combining two steps of (7.1.18) gives $R _ { k + 1 } = Q _ { k + 1 } ^ { T } R _ { k } ^ { T } = Q _ { k + 1 } ^ { T } R _ { k - 1 } Q _ { k }$ Hence $R _ { k + 1 }$ has the same singular values as $R _ { k - 1 }$ and

$$
R _ { k + 1 } ^ { T } R _ { k + 1 } = R _ { k } R _ { k } ^ { T } = Q _ { k } ^ { T } ( R _ { k - 1 } ^ { T } R _ { k - 1 } ) Q _ { k } .
$$

This amounts to one step of the QR algorithm applied to $R _ { k - 1 } ^ { T } R _ { k - 1 }$ . Similarly,

$$
R _ { k + 1 } R _ { k + 1 } ^ { T } = R _ { k } ^ { T } R _ { k } = Q _ { k + 1 } ^ { T } ( R _ { k - 1 } R _ { k - 1 } ^ { T } ) Q _ { k + 1 } ,
$$

which shows that also one step of the classical QR algorithm on $R _ { k - 1 } R _ { k - 1 } ^ { T }$ has been performed. Notably, this has been achieved without explicitly forming either $A ^ { T } A$ or $A A ^ { T }$ , which could have resulted in a loss of accuracy.

One step of the iteration (7.1.18) requires about $O ( n ^ { 3 } )$ flops. This is too much to make it a practical algorithm.By initially reducing $A$ to bidiagonal form, the iteration (7.1.19) becomes $B _ { 0 } = B$ ，

$$
B _ { k - 1 } ^ { T } = Q _ { k } B _ { k } , \quad k = 1 , 2 , \ldots .
$$

This can be performed by applying a sequence of plane rotations to the lower bidiagonal matrix $B _ { k - 1 } ^ { T }$ of(7.5)ode in the first column is zeroed, giving

$$
\left( \begin{array} { c c } { { c } } & { { s } } \\ { { - s } } & { { c } } \end{array} \right) \left( \begin{array} { c c } { { \rho _ { 1 } } } & { { 0 } } \\ { { \gamma _ { 2 } } } & { { \rho _ { 2 } } } \end{array} \right) = \left( \begin{array} { c c } { { \hat { \rho } _ { 1 } } } & { { \hat { \gamma } _ { 2 } } } \\ { { 0 } } & { { \hat { \rho } _ { 2 } } } \end{array} \right) ,
$$

where $c = \rho _ { 1 } / \hat { \rho } _ { 1 }$ ， $s = \gamma _ { 2 } / \hat { \rho } _ { 1 }$ . The new elements are

$$
\begin{array} { r } { \hat { \rho } _ { 1 } = \sqrt { \rho _ { 1 } ^ { 2 } + \gamma _ { 2 } ^ { 2 } } , \quad \hat { \gamma } _ { 2 } = \gamma _ { 2 } \big ( \rho _ { 2 } / \hat { \rho } _ { 1 } \big ) , \quad \hat { \rho } _ { 2 } = \rho _ { 1 } \big ( \rho _ { 2 } / \hat { \rho } _ { 1 } \big ) . } \end{array}
$$

The remaining steps are similar. Note that $s$ and $c$ in the plane rotations are not needed and that two successive steps of the algorithm will transform a lower bidiagonal matrix back into lower bidiagonal form. The work in one step of the bidiagonal zero-shift SVD algorithm is $4 n$ multiplications, $n$ divisions,and $n$ square roots. The algorithm uses no addition or subtraction. Therefore no cancellation can take place,and each entry of the transformed matrix is computed to high relative accuracy. By merging the two steps,we obtain the zero-shift algorithm used by Demmel and Kahan [310,1990].

The repeated transformation from lower to upper triangular form, or flipping of a triangular matrix,was first analyzed by Faddeev,Kublanovskaya,and Faddeeva [392,1968]; see also Chandrasekaran and Ipsen [233,1995].

The following remarkably compact MATLAB function by Fernando and Parlett [403,1994] is simpler and more efficient. It performs one step of the unshifted QRSVD algorithm on a lower or upper bidiagonal matrix $B$ whose elements are stored in q[1:n] and e[2:n].

# Algorithm 7.1.1 (Zero-Shift Bidiagonal QRSVD).

funct n ${ \begin{array} { l } { { \mathrm { i o n ~ } } \left[ { \mathrm { r h o ~ } } , { \mathrm { g a m } } \right] \ = \ { \mathrm { b i d q r } } \left( { \mathrm { r h o ~ } } , { \mathrm { g a m } } \right) } \\ { = \ { \mathrm { l e n g t h } } \left( { \mathrm { q } } \right) ; } \\ { { \mathrm { ~ r ~ } } { \mathrm { ~ i ~ } } = \ 1 : { \mathrm { n - 1 } } } \\ { { \mathrm { ~ r h o ~ } } ( { \mathrm { i } } ) \ = \ { \mathrm { n o r m } } \left( { \mathrm { r h o ~ } } ( { \mathrm { i } } ) , { \mathrm { g a m } } \left( { \mathrm { i } } + 1 \right) \right) ; } \\ { { \mathrm { ~ t ~ } } = \ { \mathrm { r h o ~ } } ( { \mathrm { i } } + 1 ) / { \mathrm { r h o ~ } } ( { \mathrm { i } } ) ; } \\ { { \mathrm { ~ g a m } } ( { \mathrm { i } } + 1 ) \ = \ { \mathrm { g a m } } ( { \mathrm { i } } + 1 ) * { \mathrm { t } } ; } \\ { { \mathrm { ~ r h o ~ } } ( { \mathrm { i } } + 1 ) \ = \ { \mathrm { r h o ~ } } ( { \mathrm { i } } ) * { \mathrm { t } } ; } \end{array} }$   
fo   
end   
end

If some element $\gamma _ { i } = 0$ ，where $i < n$ , then the bidiagonal matrix splits into a direct sum of two smaller bidiagonal matrices

$$
B = \left( \begin{array} { c c } { { B _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { B _ { 2 } } } \end{array} \right) ,
$$

which the algorithm can treat separately. In particular, if $\gamma _ { n } = 0$ , then $\sigma = \rho _ { n }$ is a singular value. If a diagonal element $\rho _ { i } = 0$ ， $i < n$ ,then $B$ is singular and must have a zero singular value. Then in the next iteration the algorithm will drive this zero element to the last position, giving $\gamma _ { n } = 0$

Demmel and Kahan [310,19go] show that the singular values of a bidiagonal matrix are determined to full relative accuracy by their elements, independent of their magnitudes,while the error bounds for the associated singular vectors depend on the relative gap $\gamma _ { i }$ between $\sigma _ { i }$ and other singular values.

Theorem 7.1.1. Let $B$ and $\bar { B } = B + \delta B , | \delta B | \leq \omega | B | ,$ be upper bidiagonal matrices in $\mathbb { R } ^ { n \times n }$ ， with singular values $\sigma _ { 1 } \geq \cdots \geq \sigma _ { n }$ and $\bar { \sigma } _ { 1 } \geq \cdot \cdot \cdot \geq \bar { \sigma } _ { n }$ ,respectively. If $\eta = ( 2 n - 1 ) \omega < 1$ ， then for $i = 1 , \ldots , n$ ，

$$
\begin{array} { r l } & { | \bar { \sigma } _ { i } - \sigma _ { i } | \le \displaystyle \frac { \eta } { 1 - \eta } | \sigma _ { i } | , } \\ & { \operatorname* { m a x } \left\{ \sin \theta ( u _ { i } , \bar { u } _ { i } ) , \sin \theta ( v _ { i } , \bar { v } _ { i } ) \right\} \le \displaystyle \frac { \sqrt { 2 } \eta ( 1 + \eta ) } { \gamma _ { i } - \eta } , } \\ & { \gamma _ { i } = \displaystyle \operatorname* { m i n } _ { j \neq i } \frac { | \sigma _ { i } - \sigma _ { j } | } { \sigma _ { i } + \sigma _ { j } } . } \end{array}
$$

More generally, Demmel et al. [307,1999] show that high relative accuracy in the computed SVD can be achieved for matrices that are diagonal scalings of a well-conditioned matrix. They consider rank-revealing decompositions of the form

$$
A = X D Y ^ { T } , \quad X \in \mathbb { R } ^ { m \times r } , \quad Y \in \mathbb { R } ^ { r \times n } ,
$$

where $X$ and $Y$ are well-conditioned and $D$ is diagonal. Such a decomposition can be obtained, e.g., using Gaussian elimination with rook or complete pivoting.

In the zero-shift QRSVD algorithm the diagonal elements of $B$ will converge to the singular values $\sigma _ { i }$ arranged in order of decreasing absolute magnitude. The superdiagonal elements will behave asymptotically like $c _ { i j } ( \sigma _ { i } / \sigma _ { j } ) ^ { 2 k }$ for some constants $c _ { i j }$ . Hence, the rate of convergence is slow unless there is a substantial gap between the singular values; see Theorem 7.3.4. The remedy is to introduce suitable chosen shifts in the QR algorithm. However,to do this stably is a nontrivial task,and hence it is the subject of the next section.

# 7.1.4 - The Implicitly Shifted QR Algorithm

The rate of convergence of the QR algorithm for a real symmetric tridiagonal matrix $T \in \mathbb { R } ^ { n \times n }$ depends on the ratios $\lambda _ { i + 1 } / \lambda _ { i }$ of its eigenvalues $\lambda _ { 1 } \geq \cdots \geq \lambda _ { n }$ of $T$ By introducing shifts in the algorithm, the convergence rate can be improved. The shifted matrix $T - \tau I$ has the same invariant subspaces as $T$ ,and the eigenvalues are $\lambda _ { i } - \tau$ ， $i = 1 , \ldots , n$ .With variable shifts the shifted QR algorithm becomes $T _ { 1 } = T$ ，

$$
T _ { k } - \tau I = Q _ { k } R _ { k } , \qquad R _ { k } Q _ { k } + \tau I = T _ { k + 1 } , \quad k = 1 , 2 , \ldots .
$$

Since the shift is restored,each iteration is an orthogonal similarity transformation,and it holds that $T _ { k + 1 } = Q _ { k } ^ { T } T _ { k } Q _ { k }$ .Further,the eigenvectors of $T$ can be found by accumulating the product $P _ { k } = Q _ { 1 } \cdots Q _ { k }$ ， $k = 1 , 2 , \ldots .$ If the shift is chosen to approximate a simple eigenvalue $\lambda$ of $T$ ， convergence of the QR algorithm to this eigenvalue will be fast.

Performing the shift $\tau$ in (7.1.27) explicitly will affect the accuracy of the smaller eigenvalues for which $| \lambda _ { i } | \ll | \tau |$ . This is avoided in the implicitly shifted QR algorithm due to Francis [431, 1961], [432,1961], where algorithmic details for performing the shifts implicitly are described. A crucial role is played by the following theorem.

Theorem 7.1.2 (Implicit $Q$ Theorem).Let $A \ \in \ \mathbb { R } ^ { n \times n }$ and an orthogonal matrix $Q \ =$ $( q _ { 1 } , \ldots , q _ { n } )$ be given such that $H = Q ^ { T } A Q$ is upper Hessenberg with real positive subdiagonal elements. Then $H$ and $Q$ are uniquely determined by the first column $q _ { 1 } = Q e _ { 1 }$

Proof. Assume that the first $k$ columns $q _ { 1 } , \ldots , q _ { k }$ in $Q$ and the first $k - 1$ columns in $H$ have been computed. (Since $q _ { 1 }$ is known, this assumption is valid for $k = 1 ,$ ）Equating the $k$ th columns in $Q H = A Q$ gives

$$
h _ { 1 , k } q _ { 1 } + \cdot \cdot \cdot + h _ { k , k } q _ { k } + h _ { k + 1 , k } q _ { k + 1 } = A q _ { k } , \quad k = 1 : n - 1 .
$$

Multiplying this by $q _ { i } ^ { H }$ and using the orthogonality of $Q$ gives $h _ { i k } = q _ { i } ^ { H } A q _ { k }$ ， $i = 1 { : } k$ . Since $H$ is unreduced, $h _ { k + 1 , k } \neq 0$ and

$$
q _ { k + 1 } = h _ { k + 1 , k } ^ { - 1 } \Big ( A q _ { k } - \sum _ { i = 1 } ^ { k } h _ { i k } q _ { i } \Big ) , \quad \| q _ { k + 1 } \| _ { 2 } = 1 .
$$

This and the condition that $h _ { k + 1 , k }$ is real positive determine $q _ { k + 1 }$ uniquely.

In the implicit shift tridiagonal QR algorithm, the QR step (7.1.27) is performed as follows. The first plane rotation $P _ { 1 } = G _ { 1 2 }$ is chosen so that

$$
\begin{array} { r } { P _ { 1 } t _ { 1 } = \pm \| t _ { 1 } \| _ { 2 } e _ { 1 } , \quad t _ { 1 } = ( \alpha _ { 1 } - \tau , \beta _ { 2 } , 0 , . . . , 0 ) ^ { T } , } \end{array}
$$

where $t _ { 1 }$ is the first column in $T _ { k } - \tau _ { k } I$ The result of applying this transformation is pictured below (for $n = 5$ ）：

$$
P _ { 1 } ^ { T } T _ { k } = \begin{array} { l } {  } \\ {  } \\ { \times \quad \times \quad \times \quad \times \quad } \\ { \times \quad \times \quad \times \quad \times \quad } \\ { \quad \times \quad \times \quad \times \quad \times \quad } \\ { \quad \times \quad \times \quad \times \quad } \end{array} ) , \quad \quad P _ { 1 } ^ { T } T _ { k } P _ { 1 } = \begin{array} { l } { \downarrow } { \downarrow \quad \downarrow } \\ { \times \quad \times \quad + \quad } \\ { \times \quad \times \quad \times \quad } \\  \quad P _ { 1 } ^ { T } T _ { k } P _ { 1 } = \quad ( \begin{array} { l l l l } { \hdots } & { \hslash } & { \ddots } & { \hslash } \\ { + \quad \times \quad \times } & { \hslash } & { \times \quad } \\ { \hslash } & { \times } & { \hslash } & { \times \quad } \\ { \quad \times } & { \hslash } & { \times } & { \times } \\ { \quad \times } & { \hslash } & { \times } & { \times } \end{array} ) . \end{array}
$$

To preserve the tridiagonal form, a transformation $P _ { 2 } = G _ { 2 3 }$ is used to zero out the new nonzero elements:

$$
P _ { 2 } ^ { T } ( P _ { 1 } ^ { T } T P _ { 1 } ) P _ { 2 } = \left( \begin{array} { l l l l l l } { { \times } } & { { \times } } & { { 0 } } & { { } } & { { } } & { { } } \\ { { \times } } & { { \times } } & { { \times } } & { { + } } & { { } } & { { } } \\ { { 0 } } & { { \times } } & { { \times } } & { { \times } } & { { } } & { { } } \\ { { } } & { { + } } & { { \times } } & { { \times } } & { { \times } } & { { } } \\ { { } } & { { } } & { { } } & { { \times } } & { { \times } } & { { \times } } \end{array} \right) .
$$

This creates two new nonzero elements, which in turn are moved further down the diagonal with plane rotations. This process is known as chasing. Eventually, the nonzeros outside the diagonal will disappear outside the border. By Theorem 7.1.3 the resulting symmetric tridiagonal matrix $Q ^ { T } T _ { k } Q$ must equal $T _ { k + 1 }$ , because the first column in $Q _ { k }$ is $P _ { 1 } P _ { 2 } \cdot \cdot \cdot P _ { n - 1 } e _ { 1 } = P _ { 1 } e _ { 1 }$

The shift $\tau$ in the QR algorithm is usually taken to be the eigenvalue of the trailing principal $2 \times 2$ submatrix of $T$

$$
\left( \begin{array} { c c } { { \alpha _ { n - 1 } } } & { { \beta _ { n } } } \\ { { \beta _ { n } } } & { { \alpha _ { n } } } \end{array} \right) ,
$$

closest to $\alpha _ { n }$ ,the so-called Wilkinson shift. In the case of a tie $\left( \alpha _ { n - 1 } \ = \ \alpha _ { n } \right)$ the smaller eigenvalue $\alpha _ { n } - | \beta _ { n } |$ is chosen. Wilkinson [1121,1968] shows that, neglecting rounding errors, this shift guarantees global convergence and that local convergence is nearly always cubic.A stable formula for computing the shift is

$$
\tau = \alpha _ { n } - \mathrm { s i g n } \left( \delta \right) \beta _ { n } ^ { 2 } \Big / \Big ( | \delta | + \sqrt { \delta ^ { 2 } + \beta _ { n } ^ { 2 } } \Big ) , \quad \delta = ( \alpha _ { n - 1 } - \alpha _ { n } ) / 2 ;
$$

see Parlett [884, 1998, Section 8.9].

The QRsVD algorithm for computing the SVD is obtained by applying the implicitly shifted QR algorithm to the symmetric positive definite tridiagonal matrix

$$
T = B ^ { T } B = \left( \begin{array} { c c c c c c } { \alpha _ { 1 } } & { \beta _ { 2 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & { \beta _ { 3 } } & & & \\ & { \ddots } & { \ddots } & { \ddots } & & \\ & & { \beta _ { n - 1 } } & { \alpha _ { n - 1 } } & { \beta _ { n } } \\ & & & { \beta _ { n } } & { \alpha _ { n } } \end{array} \right) \in \mathbb { R } ^ { n \times n } ,
$$

where $B$ is the bidiagonal matrix (7.1.15).Then $\alpha _ { 1 } = \rho _ { 1 } ^ { 2 }$ ，

$$
\alpha _ { i } = \rho _ { i } ^ { 2 } + \gamma _ { i } ^ { 2 } , \quad \beta _ { i } = \rho _ { i - 1 } \gamma _ { i } , \quad i = 2 , \ldots , n .
$$

If $B ^ { T } B$ is explicitly formed, the accuracy of smal singular values is destroyed. Furthermore,it is not clear how to stably obtain the left singular vectors $u _ { i }$ .However, the implicit QR iterations on $B ^ { T } B$ can be performed without explicitly forming $B ^ { T } B$ by using the following result.

Theorem 7.1.3. Let $Q = ( q _ { 1 } , \dots , q _ { n } )$ and $V = ( v _ { 1 } , \ldots , v _ { n } )$ be orthogonal matrices such that $Q ^ { T } M Q \ = \ T$ and $V ^ { T } M V = S$ are real, symmetric, and tridiagonal. If $v _ { 1 } = q _ { 1 }$ and $T$ is unreduced, then $v _ { i } = \pm q _ { i }$ $i = 2 , \ldots , n$

For a shift $\tau$ ,let $t _ { 1 }$ be the first column of $B ^ { T } B \mathrm { ~ - ~ } \tau I$ ，and determine the plane rotation $T _ { 1 } = R _ { 1 2 }$ so that

$$
T _ { 1 } ^ { T } t _ { 1 } = \pm \| t _ { 1 } \| _ { 2 } e _ { 1 } , \qquad t _ { 1 } = ( \rho _ { 1 } ^ { 2 } - \tau , \rho _ { 1 } \gamma _ { 2 } , 0 , \dots , 0 ) ^ { T } .
$$

Next, apply a sequence of plane rotations to make

$$
T _ { n - 1 } ^ { T } \cdot \cdot \cdot T _ { 2 } ^ { T } T _ { 1 } ^ { T } B ^ { T } B T _ { 1 } T _ { 2 } \cdot \cdot \cdot T _ { n - 1 }
$$

tridiagonal. To do this implicitly, start by applying the transformation $T _ { 1 }$ to $B$ . This gives (take $n = 5$ ）

$$
B T _ { 1 } = \begin{array} { c } { \downarrow \downarrow } \\ { \left( \begin{array} { c c c c c } { \times } & { \times } & { } & { } & { } \\ { + } & { \times } & { \times } & { } & { } \\ { } & { } & { \times } & { \times } & { } \\ { } & { } & { } & { \times } & { \times } \\ { } & { } & { } & { } & { \times } \end{array} \right) . } \end{array}
$$

Next, premultiply by a plane rotation $S _ { 1 } ^ { T } = R _ { 1 2 }$ to zero out the $^ +$ element. This creates a new nonzero element in the $( 1 , 3 )$ position. To preserve the upper bidiagonal form, choose a rotation $T _ { 2 } = R _ { 2 3 }$ to zero out the element $^ +$ ：

$$
S _ { 1 } ^ { T } B T _ { 1 } = \begin{array} { l } { {  } } \\ { {  } } \\ { { \quad \times \quad \times \quad \times \quad } } \\ { { \quad \times \quad \times \quad \times \quad } } \\ { { \quad \times \quad \times \quad \times \quad } } \\ { { \quad \times \quad \times \quad \times \quad } } \end{array}  , \quad \quad S _ { 1 } ^ { T } B T _ { 1 } T _ { 2 } = \quad ( \begin{array} { l l l l } { { \times \quad \times \quad + \quad } } & { { \quad \times \quad } } & { { \quad } } \\ { { \times \quad \times \quad } } & { { \times \quad } } & { { \quad } } \\ { { \quad + \quad \times \quad \times \quad } } & { { \times \quad } } & { { \quad } } \\ { { \quad \times \quad } } & { { \times \quad } } & { { \times \quad } } \\ { { \quad \times \quad } } & { { \quad \times \quad } } & { { \times \quad } } \end{array} ) .
$$

Then continue to chase the element $^ +$ down, with transformations alternately from the right and left until a new upper bidiagonal matrix

$$
\hat { B } = S _ { n - 1 } ^ { T } \cdot \cdot \cdot S _ { 1 } ^ { T } B T _ { 1 } \cdot \cdot \cdot T _ { n - 1 } = U ^ { T } B P
$$

is obtained. But then $\begin{array} { r } { \hat { T } = \hat { B } ^ { T } \hat { B } = P ^ { T } B ^ { T } U U ^ { T } B P = P ^ { T } T P } \end{array}$ is a tridiagonal matrix, where the first column of $P$ equals the first column of $T _ { 1 }$ .If $T$ is unreduced, $\hat { T }$ must be the result of a QR iteration on $T$ with shift equal to $\tau$

When the shift $\tau$ approximates an eigenvalue of $B ^ { T } B$ ,the element $\gamma _ { n }$ in the last row and last column of $T$ in (7.1.29) will approach zero very quickly. The Wilkinson shift is determined from the trailing $2 \times 2$ submatrix of $B ^ { T } B$ , namely

$$
\left( \begin{array} { c c } { \rho _ { n - 1 } ^ { 2 } + \gamma _ { n - 1 } ^ { 2 } } & { \rho _ { n - 1 } \gamma _ { n } } \\ { \rho _ { n - 1 } \gamma _ { n } } & { \rho _ { n } ^ { 2 } + \gamma _ { n } ^ { 2 } } \end{array} \right) .
$$

When $| \rho _ { n } | \leq \delta$ where $\delta$ is a prescribed tolerance, $\rho _ { n }$ is accepted as a singular value, and the order of the matrix $B$ is reduced by one. This automatic deflation is an important property of the QR algorithm.

In practice,after each QR step the convergence criterion

$$
| \gamma _ { i } | \leq 0 . 5 \mathbf { u } ( | \rho _ { i - 1 } | + | \rho _ { i } | ) , \quad i = 2 , \ldots , n ,
$$

is checked.If this is satisfied for some $i < n$ , the matrix splits into a direct sum of two smaller bidiagonal matrices $B _ { 1 }$ and $B _ { 2 }$ for which the QR iterations can be continued independently. Furthermore, if $q _ { i } = 0$ for some $i \leq n$ ，then $B$ must have at least one singular value equal to zero. Therefore also a second convergence criterion

$$
| \rho _ { i } | \leq 0 . 5 \mathbf { u } ( | \gamma _ { i } | + | \gamma _ { i + 1 } | ) , \quad i = 2 , \ldots , n ,
$$

is checked.If this is satisfied for some $i < n$ , then the $i$ th row can be zeroed out by a sequence of plane rotations $G _ { i , i + 1 } , G _ { i , i + 2 } , \ldots , G _ { i , n }$ applied from the left to $B$ . The new elements generated in the ith column can be discarded without introducing an error in the singular values that is larger than some constant times $u \| B \| _ { 2 }$ . Then the matrix $B$ again splits into two smaller bidiagonal matrices $B _ { 1 }$ and $B _ { 2 }$

The criteria (7.1.32)-(7.1.33) ensure backward stability of the QRSVD algorithm in the normwise sense, i.e., the computed singular values $\bar { \sigma } _ { k }$ are the exact singular values of a nearby matrix $B + \delta B$ ，where $\| \delta B \| _ { 2 } \le c ( n ) \cdot { \bf u } \sigma _ { 1 }$ .Here $c ( m , n )$ is a constant depending on $m$ and $n$ ，and $\mathbf { u }$ is the machine unit. Thus,if $T$ is nearly rank-deficient,this will always be revealed by the computed singular values. The penalty for not spotting a negligible element is not loss of accuracy but a slowdown of convergence. However, the smaller singular values may not be computed with high relative accuracy. When all off-diagonal elements in $B$ have converged to zero, we have $Q _ { S } ^ { T } B T _ { S } = \Sigma = \operatorname { d i a g } \left( \sigma _ { 1 } , . . . , \sigma _ { n } \right)$ . The left and right singular vectors of $T$ are given by accumulating the product of transformations in the QRSVD iterations.

Each QRSVD iteration requires $1 4 n$ multiplications and $2 n$ calls to givrot. If singular vectors are desired, accumulating the rotations into $U$ and $V$ requires 6mn and $6 n ^ { 2 }$ flops, respectively, and the overall cost goes up to $O ( m n ^ { 2 } )$ . Usually less than $2 n$ QR iterations are needed. When singular vectors are desired, the number of QR iterations can be reduced by first computing the singular values without accumulating singular vectors. Then the QRSVD algorithm is run a second time with shifts equal to the computed singular values,the so-called perfect shifts. Then convergence occurs in at most $n$ iteration. This may reduce the cost of the overall computations by about $40 \%$

A variant of the QRSVD algorithm is proposed by Chan [222,1982]. This differs in that a QR factorization is performed before the bidiagonalization. In Table 7.1.1 operation counts are shown for standard QRSVD and Chan's version. Four different cases are considered depending on whether $U _ { 1 } \in \mathbb { R } ^ { m \times n }$ and $V \in \mathbb { R } ^ { n \times n }$ are explicitly required or not. Only the highest order terms in $m$ and $n$ are kept. It is assumed that the iterative phase takes on average two complete QR iterations per singular value and that standard plane rotations are used. Case (a) arises in the computation of the pseudoinverse,case (c) in least squares applications,and case (d) in the estimation of condition numbers and rank determination.

Table 7.1.1. Comparison of multiplications for SVD algorithms.   

<table><tr><td>Case</td><td>Required</td><td>Golub-Reinsch SVD</td><td>Chan SVD</td></tr><tr><td>(a)</td><td>,U1,V</td><td>12mn²+22n³/3</td><td>6mn²+16n3</td></tr><tr><td>(b)</td><td>£,U1</td><td>12mn² -2n³</td><td>6mn² + 26n³/3</td></tr><tr><td>（c）</td><td>£,V</td><td>4mn² +8n³</td><td>2mn² +28n³/3</td></tr><tr><td>(d)</td><td>£</td><td>4mn² -4n³/3</td><td>2mn² + 2n³</td></tr></table>

The QL algorithm is a variant of the QR algorithm based on the iteration

$$
A _ { k } = Q _ { k } L _ { k } , \qquad L _ { k } Q _ { k } = A _ { k + 1 } , \qquad k = 1 , 2 , \ldots ,
$$

with $L _ { k }$ lower triangular. This is merely a reorganization of the QR algorithm. Let $J \in \mathbb { R } ^ { n \times n }$ be the symmetric permutation matrix $J = \left( e _ { n } , \ldots , e _ { 2 } , e _ { 1 } \right)$ .Then $J A$ reverses the rows of $A$ ， $A J$ reverses the columns of $A$ ,and $J A J$ reverses both rows and columns. If $R$ is upper triangular, then $J R J$ is lower triangular. It follows that if $A = Q R$ is the QR factorization of $A$ ，then $J A J = ( J Q J ) ( J R J )$ is the QL factorization of $J A J$ . Hence,the QR algorithm applied to $A$ is the same as the QL algorithm applied to $J A J$ .Therefore the convergence theory is essentially the same for both algorithms. But in the QL algorithm,inverse iteration is taking place in the top left corner of $A$ ,and direct iteration in the lower right corner.

A bidiagonal matrix is said to be graded if the elements are large at one end and small at the other. If the bidiagonalization uses an initial QR factorization with column pivoting,then the matrix is usually graded from large at upper left to small at lower right, as illustrated here:

$$
\left( \begin{array} { c c c c } { { 1 } } & { { 1 0 ^ { - 1 } } } & { { } } & { { } } \\ { { } } & { { 1 0 ^ { - 2 } } } & { { 1 0 ^ { - 3 } } } & { { } } \\ { { } } & { { } } & { { 1 0 ^ { - 4 } } } & { { 1 0 ^ { - 5 } } } \\ { { } } & { { } } & { { } } & { { 1 0 ^ { - 6 } } } \end{array} \right) .
$$

This is advantageous for the QR algorithm, which tries to converge to the singular values from smallest to largest and “chases the bulge” from top to bottom. Convergence will usually be fast if the matrix is graded this way. However, if $B$ is graded the opposite way, the QR algorithm may require many more steps,and the QL algorithm should be used instead. Alternatively, the rows and columns of $B$ could be reversed. When the matrix breaks up into diagonal blocks that are graded in different ways,the bulge should be chased in the appropriate direction.

The QRSVD algorithm by Demmel and Kahan [310,199o] is substantially improved compared to the Golub-Reinsch algorithm. It computes the smallest singular values to maximal relative accuracy and the others to maximal absolute accuracy. This is achieved by using the zero-shift QR algorithm on any submatrix whose condition number $\kappa = \sigma _ { \mathrm { m a x } } / \sigma _ { \mathrm { m i n } }$ is so large that the shifted QR algorithm would make unacceptably large changes in the computed $\sigma _ { \mathrm { m i n } }$ . Although the zero-shift algorithm has only a linear rate of convergence, it converges quickly when ${ \sigma _ { \operatorname* { m i n } } } / { \sigma _ { \operatorname* { m a x } } }$ is very small. The zero-shift algorithm uses only about a third of the operations per step as the shifted version. This makes the Demmel-Kahan algorithm faster and,occasionally, much faster than the original Golub-Reinsch algorithm. Other important features of the new al-gorithm are stricter convergence criteria and the use of a more accurate algorithm for computing singular values and vectors of an upper triangular $2 \times 2$ matrix; see Section 7.2.2.

# Notes and references

The QR algorithm was independently discovered by Kublanovskaya [7O9,1g61]. The story of the QR algorithm and its later developments is told by Golub and Uhlig [510,2oo9]． An exposition of Francis's work on the QR algorithm is given in Watkins [1104,2o11]. A two-stage bidiagonalization algorithm where the matrix is first reduced to band form is developed by GroBer and Lang [541,1999].

Initially, Golub [488,1g68] applied the Francis implicit QR algorithm to the special symmetric tridiagonal matrix $K$ in (7.1.17),whose eigenvalues are $\pm \sigma _ { i }$ . If double QR steps with shifts $\pm \tau _ { i }$ are taken,then the zero diagonals in $K$ are preserved. This makes it possible to remove the redundancy caused by the doubling of the dimensions. The resulting algorithm is outlined also in the Stanford CS report of Golub and Businger [485,1967], which contains an ALGOL implementation by Businger.

The algorithm given by Golub and Reinsch [5O7,1971] for computing the SVD is one of the most elegant and reliable in numerical linear algebra and has been cited over 46Oo times (as of 2023). The FORTRAN program for the SVD of a complex matrix of Businger and Golub [194, $1 9 6 9 ]$ is an adaptation of the same code. The LINPACK implementation of the QRSVD algorithm (see Dongarra et al. [322,1979, Chap.11]) follows the Handbook algorithm, except it determines the shift from (7.1.31).

The QRSVD algorithm can be considered as a special instance of a product eigenvalue problem,where two matrices $A$ and $B$ are given,and one wishes to find the eigenvalues of a product matrix $C = A B$ or quotient matrix $C = A B ^ { - 1 }$ . For stability reasons,one wants to operate on the factors $A$ and $B$ separately,without forming $A B$ or $A B ^ { - 1 }$ explicitly;see Heath et al. [597,1986]. The relationship between the product eigenvalue problem and the QRSVD algorithm is discussed by Kressner [707,2005],[706, 20o5]. An overview of algorithms and software for computing eigenvalues and singular values is given by Bai et al. [61, 200o].

# 7.2 - Alternative SVD Algorithms

# 7.2.1 - Bisection-Type Methods

The number of eigenvalues of a symmetric tridiagonal matrix

$$
T = \left( \begin{array} { c c c c c c } { \alpha _ { 1 } } & { \beta _ { 2 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & { \beta _ { 3 } } & & & \\ & { \beta _ { 3 } } & { \ddots } & { \ddots } & & \\ & & { \ddots } & { \alpha _ { n - 1 } } & { \beta _ { n } } \\ & & & { \beta _ { n } } & { \alpha _ { n } } \end{array} \right) \in \mathbb { R } ^ { n \times n }
$$

that are greater than or less than a specified value can be determined by the method of bisection or spectrum slicing. Early implementations of such methods were based on computing the leading principal minors of the shifted matrix $\operatorname* { d e t } ( T _ { k } - \lambda I )$ of $T$ .Expanding the determinant along the last row and defining $p _ { 0 } = 1$ gives

$$
\begin{array} { r l } & { p _ { 1 } ( \lambda ) = ( \alpha _ { 1 } - \lambda ) p _ { 0 } , } \\ & { p _ { k } ( \lambda ) = ( \alpha _ { k } - \lambda ) p _ { k - 1 } ( \lambda ) - \beta _ { k } ^ { 2 } p _ { k - 2 } ( \lambda ) , \quad k = 2 , \ldots , n . } \end{array}
$$

For a given numerical value of $\lambda$ , the so-called Sturm sequence $p _ { 1 } ( \lambda ) , \ldots , p _ { n } ( \lambda )$ can be evaluated in $3 n$ flops using (7.2.2).

Lemma 7.2.1. If the tridiagonal matrix $T$ is irreducible, i.e., $\beta _ { i } \neq 0$ ， $i = 2 , \ldots , n$ , then the zeros of $p _ { k - 1 } ( \lambda )$ strictly separate those of $p _ { k } ( \lambda )$

Proof. By Cauchy's interlacing theorem, the eigenvalues of any leading principal minor of a Hermitian matrix $A \in \mathbb { R } ^ { n \times n }$ interlace the eigenvalues of $A$ . In particular, the zeros of each $p _ { k - 1 } ( \lambda )$ separate those of $p _ { k } ( \lambda )$ ，at least in the weak sense. Suppose now that $\mu$ is a zero of both $p _ { k } ( \lambda )$ and $p _ { k - 1 } ( \lambda )$ . Since $\beta _ { k } \neq 0$ ,it follows from(7.2.2） that $\mu$ is also a zero of $p _ { k - 2 } ( \lambda )$ . Continuing in this way shows that $\mu$ is a zero of $p _ { 0 }$ . This is a contradiction because $p _ { 0 } = 1$ □

Theorem 7.2.2.Let $s ( \tau )$ be the number of agreements in sign of consecutive members in the Sturm sequence $p _ { 1 } ( \tau )$ ， $p _ { 2 } ( \tau )$ ，.， $p _ { n } ( \tau )$ If $p _ { i } ( \tau ) = 0 \quad$ ，the sign is taken to be opposite that of $p _ { i - 1 } ( \tau )$ . (Note that two consecutive $p _ { i } ( \tau )$ cannot be zero.） Then $s ( \tau )$ is the number of eigenvalues of $T$ strictly greater than $\mu$

Proof. See Wilkinson [1120,1965, pp.300-301].

Bisection can be used to locate an individual eigenvalue $\lambda _ { k }$ independent of any of the others and is therefore suitable for parallel computing. The Sturm sequence algorithm is very stable when carred out in IEEE floating-point arithmetic but is susceptible to underflow and overflow and other numerical problems. There are ways to overcome these problems as shown by Barth, Martin,and Wilkinson [93,1971].

More recent implementations of bisection methods are developments of the inertia algorithm analyzed by Kahan $[ 6 8 0 , 1 9 6 6 ]$ ; see Fernando [4O2,19g8]. The inertia of a symmetric matrix $A$ is defined as the triple $( \tau , \nu , \delta )$ of positive, negative, and zero eigenvalues of $T$ . Sylvester's law (Horn and Johnson [639,1985l) says that the inertia is preserved under congruence transformations.If symmetric Gaussian elimination is carried out for $A - \tau I$ ,it yields the factorization

$$
A - \tau I = L D L ^ { T } , \quad D = \mathrm { d i a g } ( d _ { 1 } , \dots , d _ { n } ) .
$$

where $L$ is unit lower bidiagonal and $D = \operatorname { d i a g } \left( d _ { 1 } , \ldots , d _ { n } \right)$ . Since $A - \sigma I$ is congruent to $D$ , it follows from Sylvester's law that the number of eigenvalues of $A$ smaller than $\tau$ equals the number of negative elements $\pi ( D )$ in the sequence $d _ { 1 } , \ldots , d _ { n }$ . Applied to a symmetric and tridiagonal matrix $T - \tau I = L D L ^ { T }$ , this procedure becomes particularly effcient and reliable. A remarkable fact is that provided over- or underflow is avoided,element growth will not affect the accuracy. For example, the LDLT factorization

$$
A - I = { \left( \begin{array} { l l l } { 1 } & { 2 } & { } \\ { 2 } & { 2 } & { - 4 } \\ { - 4 } & { - 6 } \end{array} \right) } = { \left( \begin{array} { l l l } { 1 } & { } & { } \\ { 2 } & { 1 } & { } \\ { } & { 2 } & { 1 } \end{array} \right) } \left( { \begin{array} { l l l } { 1 } & { } & { } \\ { } & { - 2 } & { } \\ { } & { } & { 2 } \end{array} } \right) \left( { \begin{array} { l l l } { 1 } & { 2 } & { } \\ { } & { 1 } & { 2 } \\ { } & { } & { 1 } \end{array} } \right)
$$

shows that $A$ has two eigenvalues greater than 1.

The bisection method can be used to locate singular values of a bidiagonal matrix $B$ by applying it to compute the eigenvalues of one of tridiagonal matrices $B ^ { T } B$ and $B B ^ { T }$ . This can be done without forming these matrix products explicitly. However, the best option is to apply bisection to the special symmetric tridiagonal matrix $T$ of Golub-Kahan form (7.1.17) with zero diagonal and eigenvalues $\pm \sigma _ { i }$ . It gives the highest relative accuracy in the computed singular value.

By applying the bisection procedure to the special symmetric tridiagonal matrix $G \in \mathbb { R } ^ { 2 n \times 2 n }$ in

$$
G = \left( \begin{array} { c c c c c c } { 0 } & { \rho _ { 1 } } & & & & & \\ { \rho _ { 1 } } & { 0 } & { \gamma _ { 2 } } & & & & \\ & { \gamma _ { 2 } } & { 0 } & { \rho _ { 2 } } & & & \\ & & { \rho _ { 2 } } & { \ddots } & { \ddots } & & \\ & & & { \ddots } & { \ddots } & { \gamma _ { n } } & \\ & & & & { \gamma _ { n } } & { 0 } & { \rho _ { n } } \\ & & & & & { \rho _ { n } } & { 0 } \end{array} \right) \in \mathbb { R } ^ { 2 n \times 2 n }
$$

with zero diagonal, we obtain a method for computing selected singular values $\sigma _ { i }$ of an irreducible bidiagonal matrix $B _ { n }$ with elements $\rho _ { 1 } , \ldots , \rho _ { n }$ and $\gamma _ { 2 } , \ldots , \gamma _ { n }$ . Recall that $G$ is permutationally equivalent to the Jordan-Wielandt matrix and has eigenvalues equal to $\pm \sigma _ { i } ( B _ { n } )$ ， $i = 1 , \ldots , n$

Following Fernando 402,19g8], the diagonal elements in the $\mathrm { L D L } ^ { T }$ factorization of $G - \tau I$ are obtained by Gaussian elimination as

$$
d _ { 1 } = - \tau , d _ { i } = - \tau - z _ { i } / d _ { i - 1 } , i = 2 , \ldots , 2 n ,
$$

where $z _ { i } = \rho _ { i } ^ { 2 }$ if $i$ is odd, and $z _ { i } = \gamma _ { i } ^ { 2 }$ if $i$ is even and $z _ { 0 } = 0$

# Algorithm 7.2.1 (Bisection for Singular Values).

Let $\rho _ { 1 } , \gamma _ { 2 } , \rho _ { 2 } , \gamma _ { 3 } , . ~ . ~ . ~ , \rho _ { n }$ be the off-diagonal elements of the tridiagonal matrix $G$ in (7.2.4). Set $z _ { i } = \rho _ { i } ^ { 2 }$ ，if $i$ is odd and $z _ { i } = \gamma _ { i } ^ { 2 }$ ，if $i$ is even. On exit $\pi$ is the number of singular values of $B$ that are less than $\tau > 0$

$$
\begin{array} { r l } & { \pi : = 0 ; ~ d : = - \tau ; } \\ & { \mathrm { i f } ~ d < 0 \mathrm { ~ t h e n } \pi = 1 ; } \\ & { \mathrm { f o r } i = 1 : 2 n - 1 } \\ & { ~ d : = - \tau - z _ { i } / d ; } \\ & { \mathrm { i f } ~ | d | < 0 \mathrm { ~ t h e n } \pi : = \pi + 1 ; } \end{array}
$$

end

One step in Algorithm 7.2.1 requires $2 n$ flops,and only the elements $d _ { k }$ need be stored. The number of multiplications can be halved by precomputing $\alpha _ { k } ^ { 2 }$ ,but this may cause unnecessary over- or underflow. To prevent breakdown of the recursion,the algorithm should be modified so that a small $| d _ { k } |$ is replaced by $\sqrt { \omega }$ ，where $\omega$ is the underflow threshold.

Kahan [68O,1966] gives a detailed error analysis of the bisection algorithm. Assuming that no over- or underflow occurs,he proves the monotonicity of the inertia counts in IEEE floatingpoint arithmetic.He shows that the computed number $\bar { \pi }$ is the exact number of singular values greater than $\sigma$ of a tridiagonal matrix $T ^ { \prime }$ , where the elements of $T ^ { \prime }$ have elements satisfying

$$
| \sigma ^ { \prime } - \sigma | \leq u \sigma , \qquad | \alpha _ { k } ^ { \prime } - \alpha _ { k } | \leq 2 u | \alpha _ { k } | ,
$$

a very satisfactory backward error bound. Combined with Theorem 7.1.1, this shows that the bisection algorithm computes singular values of a bidiagonal matrix $B$ with small relative errors.

The bisection algorithm is related to the famous quotient difference (qd) algorithm of Rutishauser [946,1954] for finding roots of polynomials or the poles of meromorphic functions; see Henrici [6O3,1958]. The differential qd (dqds) algorithm for computing singular values of a bidiagonal matrix is due to Fernando and Parlett [403,1994l. This algorithm evolved from trying to find a faster square-root-free version of the Demmel-Kahan zero-shift bidiagonal QR Algorithm 7.1.1. Recall that one step of the zero-shift Demmel-Kahan QR algorithm applied to a bidiagonal matrix $B$ with elements $q _ { i } , e _ { i + 1 }$ gives another bidiagonal matrix $\widehat { B }$ with elements $\widehat { q } _ { i } , \widehat { e } _ { i + 1 }$ such that $B B ^ { T } = \widehat { B } ^ { T } \widehat { B }$ Equating the $( k , k )$ and $( k , k + 1 )$ elements on both sides of this equation gives

$$
q _ { k } ^ { 2 } + e _ { k } ^ { 2 } = \widehat { e } _ { k - 1 } ^ { 2 } + \widehat { q } _ { k } ^ { 2 } , \qquad e _ { k } q _ { k + 1 } = \widehat { q } _ { k } \widehat { e } _ { k } .
$$

These are similar to the rhombus rules of the qd algorithm and connect the four elements

$$
\hat { e } _ { k - 1 } ^ { 2 } \begin{array} { c c } { { \hat { q } _ { k } ^ { 2 } } } & { { } } \\ { { } } & { { } } \\ { { \hat { e } _ { k - 1 } ^ { 2 } } } & { { } } \\ { { } } & { { \hat { q } _ { k + 1 } ^ { 2 } } } \end{array} \begin{array} { c c } { { \hat { \sigma } _ { k } ^ { 2 } } } & { { } } \\ { { } } & { { } } \\ { { \hat { e } _ { k } ^ { 2 } . } } & { { } } \end{array}
$$

To keep the high relative accuracy property,Fernando and Parlett had to use the so-called differential form of the progressive dqds algorithm This version also allows a stable way to introduce

explicit shifts in the algorithm. One step of dqds with shift $\tau \leq \sigma _ { \operatorname* { m i n } } ( B )$ computes a bidiagonal $\widetilde { B }$ such that

$$
\widehat { B } ^ { T } \widehat { B } = B B ^ { T } - \tau ^ { 2 } I .
$$

The choice of $\tau$ ensures that $\widehat { B }$ exists. A nonrestoring orthogonal similarity transformation can be performed without forming $B B ^ { T } - \tau ^ { 2 } I$ , using a hyperbolic QR factorization (see Section 3.2.4). Alternatively, if

$$
Q \left( \begin{array} { c } { B ^ { T } } \\ { 0 } \end{array} \right) = \left( \begin{array} { c } { \widehat { B } } \\ { \tau I } \end{array} \right) \in \mathbb { R } ^ { 2 n \times n }
$$

with $Q$ orthogonal, then $B B ^ { T } = \widehat { B } ^ { T } \widehat { B } + \tau ^ { 2 } I$ as required. In the frst step,a plane rotation is constructed that affects only rows $( 1 , n + 1 )$ and makes the $( n + 1 , 1 )$ element equal to $\tau$ . This is possible because $\tau \leq \sigma _ { \operatorname* { m i n } } ( B ) \leq q _ { 1 }$ ,and it changes the first diagonal element to $t _ { 1 } = \sqrt { q _ { 1 } ^ { 2 } - \tau ^ { 2 } }$ Next, a rotation in rows $( 1 , 2 )$ is used to annihilate $e _ { 2 }$ ,giving

$$
\widehat { q } _ { 1 } = \sqrt { q _ { 1 } ^ { 2 } - \tau ^ { 2 } + e _ { 2 } ^ { 2 } }
$$

and changing $q _ { 2 }$ to $\widehat { q } _ { 2 }$ . The first column and row now have their final form:

$$
\left( \begin{array} { c c c c } { { q _ { 1 } } } & { { } } & { { } } & { { } } \\ { { e _ { 2 } } } & { { q _ { 2 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { e _ { n } } } & { { q _ { n } } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right) \Rightarrow \left( \begin{array} { c c c c } { { t _ { 1 } } } & { { } } & { { } } & { { } } \\ { { e _ { 2 } } } & { { q _ { 2 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { e _ { n } } } & { { q _ { n } } } \\ { { \tau } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right) \Rightarrow \left( \begin{array} { c c c c } { { \widehat { q _ { 1 } } } } & { { \widehat { e _ { 2 } } } } & { { } } & { { } } \\ { { 0 } } & { { \widetilde { q _ { 2 } } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { e _ { n } } } & { { q _ { n } } } \\ { { \tau } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right) .
$$

All remaining steps are similar. The $k$ th step only acts on the last $n - k + 1$ rows and columns and will produce an element $\tau$ in position $( n + k , n + k )$ . One can show that this algorithm does not introduce large relative errors in the singular values.By working instead with squared quantities, square roots can be eliminated. More details are given in Fernando and Parlett [4O3,1994l and Parlett [883,1995l. The dqds algorithm is available in LAPACK as the routine DLASQ and is considered to be the fastest SVD algorithm when only singular values are required. The error bounds for dqds are significantly smaller than those for the Demmel-Kahan QRSVD algorithm. A further benefit is that it can be implemented in either parallel or pipelined format.

The multiple relatively robust representation (MRRR or $\mathrm { { M R ^ { 3 } } }$ ）algorithm by Dhillon [320, 1997] and Dhillon and Parlett [321, 2oo4] accurately computes the eigenvalue decomposition of a symmetric tridiagonal matrix $M \in \mathbb { R } ^ { n \times n }$ in only $\mathcal { O } ( n ^ { 2 } )$ operations. It overcomes some difficulties with the dqds algorithm for computing the eigenvectors.Applying the ${ \mathrm { { M R } } } ^ { 3 }$ algorithm to compute the eigenvalue decompositions of $B ^ { T } B$ and $B B ^ { T }$ separately gives a fast algorithm for computing the full SVD of a bidiagonal matrix $B$ .GroBer and Lang [542,2003] show that this may lead to poor results regarding the residual $\| B V - U \Sigma \|$ and give a coupling strategy that resolves this diffculty. The resulting algorithm is analyzed in GroBer and Lang [543, 2005]. An implementation of the $\mathrm { { M R ^ { 3 } } }$ algorithm for the bidiagonal SVD is given by Willems, Lang, and Vomel [1125,2oo7]. Later developments of the bidiagonal $\mathrm { { M R ^ { 3 } } }$ algorithm are described in Willems and Lang [1124, 2012].

# 7.2.2 - Jacobi-Type Methods

Jacobi's method [659,1846] is one of the oldest methods for solving the eigenvalue problem for a real symmetric (or Hermitian) matrix $A$ of order $n$ .Jacobi's method solves the eigenvalue problem by performing a sequence of similarity transformations

$$
A _ { 0 } = A , \qquad A _ { k + 1 } = J _ { k } ^ { T } A _ { k } J _ { k } , \quad k = 0 , 1 , 2 , \ldots ,
$$

such that $A _ { k }$ ， $k = 1 , 2 , \dots$ , converges to a diagonal matrix. Here $J _ { k } = G _ { p q } ( \theta )$ is chosen as a rotation in the plane $( p , q )$ ， $p < q$ .The elements $c = \cos \theta$ and $s = \sin \theta$ are determined so that

$$
\left( \begin{array} { c c } { { a _ { p p } ^ { \prime } } } & { { 0 } } \\ { { 0 } } & { { a _ { q q } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { c c } { { c } } & { { - s } } \\ { { s } } & { { c } } \end{array} \right) \left( \begin{array} { c c } { { a _ { p p } } } & { { a _ { p q } } } \\ { { a _ { p q } } } & { { a _ { q q } } } \end{array} \right) \left( \begin{array} { c c } { { c } } & { { s } } \\ { { - s } } & { { c } } \end{array} \right) ,
$$

i.e.,the off-diagonal elements $a _ { p q } = a _ { q p }$ are reduced to zero.

There are special situations when Jacobi's method is very efcient, e.g.,when $A$ is nearly diagonal or when the eigenvalue problems for a sequence of matrices differ only slightly from one another. After the QR algorithm was introduced, Jacobi's method fell out of favor for a time. It was revived when Demmel and Veselic [312,1992] showed that with a proper stopping criterion, Jacobi's method computes the eigenvalues of symmetric positive definite matrices with uniformly better relative accuracy than any algorithm that first reduces the matrix to tridiagonal form; see also Dopico, Koev,and Molera [330, 2oo9]. Newer implementations of Jacobi's method for computing the SVD were then developed that could also compete in speed with the QR algorithm.

Only the elements in rows and columns $p$ and $q$ of $A$ will change. Since symmetry is pre-served, only the upper triangular part of each $A$ needs to be computed. The 2 by 2 symmetric eigenvalue problem (7.2.8) is a key subproblem in Jacobi's method.Equating the off-diagonal elements gives

$$
( a _ { p p } - a _ { q q } ) c s + a _ { p q } ( c ^ { 2 } - s ^ { 2 } ) = 0 .
$$

f $a _ { p q } \neq 0$ ，we obtain $\tau \equiv \cot 2 \theta = ( a _ { q q } - a _ { p p } ) / ( 2 a _ { p q } )$ .From (7.2.9) and the trigonometric formula tan $2 \theta = { 2 \tan \theta } / { ( 1 - \tan ^ { 2 } \theta ) }$ ，it follows that $t = \tan \theta$ is a root of the quadratic equation $t ^ { 2 } + 2 \tau t - 1 = 0$ . Choosing the root of smallest modulus

$$
t = \tan ( \theta ) = \mathrm { s i g n } ( \tau ) \Big / \Big ( | \tau | + \sqrt { 1 + \tau ^ { 2 } } \Big )
$$

ensures that $\pi / 4 < \theta \leq \pi / 4$ and minimizes the difference $\| A ^ { \prime } - A \| _ { F }$ . Note that $a _ { p p } ^ { \prime } + a _ { q q } ^ { \prime } =$ trace $( A )$ . The eigenvalues are

$$
a _ { p p } ^ { \prime } = a _ { p p } - t a _ { p q } , \qquad a _ { q q } ^ { \prime } = a _ { q q } + t a _ { p q } ,
$$

and the eigenvectors are defined by $c = 1 / \sqrt { 1 + t ^ { 2 } }$ and $s = t c$ .The computed transformation is also applied to the remaining elements in rows and columns $p$ and $q$ of the full matrix $A$ .With $r = s / ( 1 + c ) = \tan ( \theta / 2 )$ and $j \neq p , q$ ,these are obtained from

$$
\begin{array} { r } { a _ { j p } ^ { \prime } = a _ { p j } ^ { \prime } = c a _ { p j } - s a _ { q j } = a _ { p j } - s ( a _ { q j } + r a _ { p j } ) , } \\ { a _ { j q } ^ { \prime } = a _ { q j } ^ { \prime } = s a _ { p j } + c a _ { q j } = a _ { q j } + s ( a _ { p j } - r a _ { q j } ) . } \end{array}
$$

These formulas are chosen to reduce roundoff errors; see Rutishauser [950,1971]. If symmetry is exploited, then one Jacobi transformation takes about $^ { 8 n }$ flops.Note that an off-diagonal element made zero at one step will in general become nonzero at some later stage. The Jacobi method also destroys any band structure in $A$

The convergence of the Jacobi method depends on the fact that in each step the Frobenius norm of the off-diagonal elements

$$
S ( A ) = \sum _ { i \neq j } a _ { i j } ^ { 2 } = \| A - D \| _ { F } ^ { 2 }
$$

is reduced. To see this,note that because the Frobenius norm is orthogonally invariant and $a _ { p q } ^ { \prime } \neq 0$ , it holds that

$$
\begin{array} { r } { S ( A ^ { \prime } ) = S ( A ) - 2 a _ { p q } ^ { 2 } . } \end{array}
$$

For simplicity of notation we set in the following $A \ : = \ : A _ { k }$ and $A ^ { \prime } = A _ { k + 1 }$ .There are various strategies for choosing the order in which the of-diagonal elements are annihilated. In the classical Jacobi method the of-diagonal element of largest magnitude is annihilated—the optimal choice. Then $2 a _ { p q } ^ { 2 } \geq S ( A _ { k } ) / N$ ， $N = n ( n - 1 ) / 2$ ,and

$$
S ( A _ { k + 1 } ) \leq ( 1 - 1 / N ) S ( A _ { k } ) .
$$

This shows that for the classical Jacobi method, $A _ { k + 1 }$ converges at least linearly with rate $1 - 1 / N$ to a diagonal matrix. It can be shown that ultimately the rate of convergence is quadratic, i.e., for $k$ large enough, $S ( A _ { k + 1 } ) < c S ( A _ { k } ) ^ { 2 }$ for some constant $c$ .The iterations are repeated until $S ( A _ { k } ) \ : < \ : \delta \| A \| _ { F }$ ，where $\delta$ is a tolerance that can be chosen equal to the unit roundoff $u$ .Then it follows from the Bauer-Fike theorem that the diagonals of $A _ { k }$ approximate the eigenvalues of $A$ with an error less than $\delta \| A \| _ { F }$

In the classical Jacobi method,a large amount of effort is spent on searching for the largest off-diagonal element. Even though it is possble to reduce this time by taking advantage of the fact that only two rows and columns are changed at each step,the classical Jacobi method is almost never used. Instead a cyclic Jacobi method is used,where the $N = { \textstyle { \frac { 1 } { 2 } } } n ( n - 1 )$ offdiagonal elements are annihilated in some predetermined order. Each element is rotated exactly once in any sequence of $N$ rotations,called a sweep. Convergence of any cyclic Jacobi method can be guaranteed if any rotation $( p , q )$ is omitted for which

$$
| a _ { p q } | < \mathrm { t o l } ( a _ { p p } a _ { q q } ) ^ { 1 / 2 }
$$

for some threshold $\tau$ ； see Forsythe and Henrici [423,1g6o]. To ensure a good rate of convergence, $\tau$ should be successively decreased after each sweep. For sequential computers, the most popular cyclic ordering is rowwise,i.e., the rotations are performed in the order

$$
\begin{array} { c c c c c } { { ( 1 , 2 ) , } } & { { ( 1 , 3 ) , } } & { { \ldots } } & { { ( 1 , n ) , } } \\ { { } } & { { ( 2 , 3 ) , } } & { { \ldots } } & { { ( 2 , n ) , } } \\ { { } } & { { \ldots } } & { { } } & { { \ldots } } \\ { { } } & { { } } & { { } } & { { ( n - 1 , n ) . } } \end{array}
$$

Jacobi's method is very suitable for parallel computation because rotations $( p _ { i } , q _ { i } )$ and $( p _ { j } , q _ { j } )$ can be performed simultaneously when $p _ { i } , q _ { i }$ are distinct from $p _ { j } , q _ { j }$ .If $n$ is even, $n / 2$ transformations can be performed simultaneously,and a sweep needs at least $n - 1$ such parallel steps. Several parallel schemes that use this minimum number of steps have been constructed; see Eberlein and Park [356,199o]. A possible choice is the round-robin ordering,illustrated here for $n = 8$ ：

$$
\begin{array} { r l } { { ( 1 , 2 ) , } } & { { ( 3 , 4 ) , } } \\ { { ( 1 , 4 ) , } } & { { ( 2 , 6 ) , ( 3 , 8 ) , ( 5 , 7 ) , } } \\ { { ( 1 , 6 ) , } } & { { ( 4 , 8 ) , ( 2 , 7 ) , ( 3 , 5 ) , } } \\ { { ( p , q ) = ( 1 , 8 ) , ( 6 , 7 ) , ( 4 , 5 ) , ( 2 , 3 ) , } } \\ { { ( 1 , 7 ) , } } & { { ( 8 , 5 ) , ( 6 , 3 ) , ( 4 , 2 ) , } } \\ { { ( 1 , 5 ) , } } & { { ( 7 , 3 ) , ( 8 , 2 ) , ( 6 , 4 ) , } } \\ { { ( 1 , 3 ) , } } & { { ( 5 , 2 ) , ( 7 , 4 ) , ( 8 , 6 ) . } } \end{array}
$$

The rotations assciated with each such row can be computed simultaneously.

Convergence of any cyclic Jacobi method can be guaranteed if rotations are omitted when the off-diagonal element is smaller in magnitude than some threshold. To ensure a good rate of convergence, the threshold should be successively decreased after each sweep. It has been shown that the rate of convergence is ultimately quadratic,so that for $k$ large enough, we have

$S ( A _ { k + 1 } ) < c S ( A _ { k } ) ^ { 2 }$ for some constant $c$ .The iterations are repeated until $S ( A _ { k } ) < \delta \| A \| _ { F }$ ， where $\delta$ is a tolerance,which can be chosen equal to the unit roundoff $\mathbf { u }$ ：The Bauer-Fike theorem (see Golub and Van Loan [512,1996,Theorem 7.2.2]) shows that the diagonal elements of $A _ { k }$ then approximate the eigenvalues of $A$ with an error less than $\delta \| A \| _ { F }$ . About $4 n ^ { 3 }$ flops are required for one sweep. In practice, the cyclic Jacobi method needs no more than about 3-5 sweeps to obtain eigenvalues of more than single precision accuracy, even when $n$ is large. The number of sweeps grows approximately as $O ( \log n )$ . About $1 0 n ^ { 3 }$ flops are needed to compute all the eigenvalues of $A$ . This is about 3-5 times more than required for the QR algorithm.

An orthogonal system $X = \dim _ { k \to \infty } X _ { k }$ , of eigenvectors of $A$ is obtained by accumulating the product of all Jacobi transformations $J _ { k }$ ：

$$
X _ { 0 } = I , \qquad X _ { k } = X _ { k - 1 } J _ { k } , \quad k = 1 , 2 , \dots .
$$

For each rotation $J _ { k }$ the associated columns $p$ and $q$ of $X _ { k - 1 }$ are modified, which requires $8 n$ flops. Hence, computing the eigenvectors doubles the operation count.

Hestenes [606,1958l) gave a one-sided Jacobi-type method for computing the SVD. It uses a sequence of plane rotations from the right to find an orthogonal matrix $V$ such that $A V = U \Sigma$ has orthogonal columns. From this the SVD $A = U \Sigma V ^ { T }$ is readily obtained. Hestenes's method is mathematically equivalent to applying Jacobi's method to $A ^ { T } A$ .In a basic step of the method, two columns in $A$ are rotated,

$$
\begin{array} { r } { \left( \begin{array} { l l } { \hat { a } _ { p } } & { \hat { a } _ { q } } \end{array} \right) = \left( \begin{array} { l l } { a _ { p } } & { a _ { q } } \end{array} \right) \left( \begin{array} { c c } { c } & { s } \\ { - s } & { c } \end{array} \right) , \quad p < q . } \end{array}
$$

The rotation parameters $c , s$ are determined so that the rotated columns are orthogonal or, equivalently, so that

$$
\left( \begin{array} { l l } { c } & { s } \\ { - s } & { c } \end{array} \right) ^ { T } \left( \begin{array} { l l } { \| a _ { p } \| _ { 2 } ^ { 2 } } & { a _ { p } ^ { T } a _ { q } } \\ { a _ { q } ^ { T } a _ { p } } & { \| a _ { q } \| _ { 2 } ^ { 2 } } \end{array} \right) \left( \begin{array} { l l } { c } & { s } \\ { - s } & { c } \end{array} \right)
$$

is diagonal. This is a $2 \times 2$ symmetric eigenproblem and can be solved as in Jacobi's method. However, because parts of the matrix are squared, this approach can lead to numerical error. Instead, first the $m \times 2$ QR factorization

$$
\left( \begin{array} { c c } { { a _ { p } } } & { { a _ { q } } } \end{array} \right) = \left( \begin{array} { c c } { { q _ { 1 } } } & { { q _ { 2 } } } \end{array} \right) \left( \begin{array} { c c } { { r _ { p p } } } & { { r _ { p q } } } \\ { { 0 } } & { { r _ { q q } } } \end{array} \right)
$$

is computed,and then the $2 \times 2$ SVD

$$
\left( { \begin{array} { c c } { c _ { l } } & { s _ { l } } \\ { - s _ { l } } & { c _ { l } } \end{array} } \right) \left( { \begin{array} { c c } { r _ { p p } } & { r _ { p q } } \\ { 0 } & { r _ { q q } } \end{array} } \right) \left( { \begin{array} { c c } { c _ { r } } & { - s _ { r } } \\ { s _ { r } } & { c _ { r } } \end{array} } \right) = \left( { \begin{array} { c c } { \sigma _ { p } } & { 0 } \\ { 0 } & { \sigma _ { q } } \end{array} } \right) .
$$

The singular values of $R$ are

$$
\sigma _ { 1 } = \frac { 1 } { 2 } \left| \sqrt { ( r _ { p p } + r _ { q q } ) ^ { 2 } + r _ { p q } ^ { 2 } } + \sqrt { ( r _ { p p } - r _ { q q } ) ^ { 2 } + r _ { p q } ^ { 2 } } \right| , \qquad \sigma _ { 2 } = | r _ { p p } r _ { q q } | / \sigma _ { p } .
$$

The right singular vector $\left( - s _ { r } , c _ { r } \right)$ in (7.2.16) isparale to $( r _ { p p } ^ { 2 } - \sigma _ { p } ^ { 2 } , r _ { p p } r _ { p q } )$ The left singular vectors are determined by $( c _ { l } , s _ { l } ) = ( r _ { p p } c _ { r } - r _ { p q } s _ { r } , r _ { q q } s _ { r } ) / { \bar { \sigma _ { p } } }$ ，These expressions suffer from possible over- or underflow in the squared subexpressions but can be reorganized to provide results with nearly ful machine precision; see the MATLAB code below.

# Algorithm 7.2.2 (SVD of 2 by 2 Upper Triangular Matrix).

function [cu,su,cv,sv,sig1,sig2] $=$ svd22(r11,r12,r22) $\%$ SVD22 computes the SvD of an upper triangular $\% ~ 2$ by 2 matrix with abs $( \mathbf { r } 1 1 ) \ > =$ abs(r22). % $\begin{array} { r l } { \mathrm { ~ \iota ~ ^ { q } ~ \_ -- ~ } } & { \_ \_ { \mathfrak { a } \_ { - } \_ \_ \{ - - } \_ \{ - } \_ \{ -  \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { - } \_ { } \  _ { - } \  \\ { \mathrm { ~ \_ { q } ~ \_ = \ \ \left( \mathtt { a b s \left( \ r 1 1 \mathtt { \mathtt { I } } \right) ~ \_ - \ r } \_ { \_ \_ \mathrm { { e q } \_ \_ \_ \_ \_ \mathrm { e q } \_ \_ \_ \_ \_ \_ \mathrm { e q } \_ \_ \_ \_ \_ { \_ } \_ \_ \mathrm { e q } \_ \_ \_ { } \_ \_ \_ \_ { \mathrm { e q } \_ \_ \_ \_ { e q } \_ \_ \_ \_ \_ { e q } \_ \_ \_ } }  ~ } } & { \\right)_ \_ } & { \_ } \\ { \mathrm { ~ \_ { \mathfrak { m } ~ = \ } ~ \_ { \mathtt { c } \_ \_ \{ \mathtt { p } \_ \_ \{ c } \_ \_ \{ + } \_ \_ \{ + } \_ { } \mathtt { p } \_ \_ \{ e q } \_ \_ \{ \mathtt { p } \_ \_ \{ e q  \_ \_ \mathrm { e q } \_ \_ { e q } \_ \_ { \mathtt { p } \_ \_ \{ e q } \_ \_ \mathrm { e q } \_ \_ { e q } \_ \_ { e q } \_ \_ { \mathtt { p } \_ \_ \{ e q } \_ \_ \mathrm { e q } \_ { e q } \_ \_ { \mathtt { p } \_ \_ \{ e q } \_ \mathrm { e q } \_  \mathtt  \end{array}$

A Fortran program based on the same formula that guards against overflow and underflow and always gives high relative accuracy in both singular values and vectors is given by Demmel and Kahan [310,199o]. An error analysis is sketched in the appendix of Bai and Demmel [59, 1993]. There also is a special subroutine SLAS2 in the BLAS for the accurate computation of the singular values of the $2 \times 2$ bidiagonal matrix.

By construction, the SVD $A = U \Sigma V ^ { T }$ produced by Hestenes's method gives $U$ orthogonal to working accuracy. A loss of orthogonality may occur in $V$ ，and the columns of $V$ should therefore be reorthogonalized at the end. Convergence of Hestenes's method is related to the fact that each step reduces the sum of squares of the off-diagonal elements

$$
\boldsymbol { S } ( \boldsymbol { C } ) = \sum _ { i \neq j } \boldsymbol { c } _ { i j } ^ { 2 } , \qquad \boldsymbol { C } = \boldsymbol { A } ^ { T } \boldsymbol { A } .
$$

The strategies for choosing the order in which the off-diagonal elements are annihilated are similar to those for Jacobi's method.A sequence of $N = n ( n - 1 ) / 2$ rotations in which each column is rotated exactly once is called a sweep. No more than about five sweeps are needed to obtain singular values of more than single precision accuracy, even when $n$ is large.

To apply Hestenes's method to a real $m \times n$ matrix when $m > n$ ,an initial QR factorization with column pivoting and row sorting of $A$ is first performed,and the algorithm is applied to $R \in$ $\mathbb { R } ^ { n \times n }$ . This tends to speed up convergence and simplify the transformations and is recommended also when $A$ is square. Hence,without restriction we can assume in the following that $m = n$ Initial implementations of Jacobi's method were slower than the QR algorithm but were able to compute singular values of a general matrix more accurately. With further improvements by Drmac [333,1997] and Drmac and Veselic [336, 20o8],[337,20o8], Jacobi's method becomes competitive also in terms of speed.

In the method of Kogbetliantz (see Kogbetliantz [702,1955l) for computing the SVD of a square matrix $A$ ,the off-diagonal elements of $A$ are successively reduced in size by a sequence of two-sided plane rotations

$$
A ^ { \prime } = J _ { p q } ^ { T } ( \phi ) A J _ { p q } ( \psi ) ,
$$

where $J _ { p q } ( \phi )$ d $J _ { p q } ( \psi )$ aredeterind s shat $a _ { p q } ^ { \prime } = a _ { q p } ^ { \prime } = 0$ N nl and $p$ $q$ $A$ $J _ { p q } ( \phi )$ $J _ { p q } ( \psi )$ determined by computing the SVD of a $2 \times 2$ submatrix

$$
A _ { p q } = \left( \begin{array} { l l } { a _ { p p } } & { a _ { p q } } \\ { a _ { q p } } & { a _ { q q } } \end{array} \right) , \qquad a _ { p p } \geq 0 , \quad a _ { q q } \geq 0 .
$$

The assumption of nonnegative diagonal elements is no restriction because the sign of these elements can be changed by premultiplication with an orthogonal matrix diag $( \pm 1 , \pm 1 )$ . From the invariance of the Frobenius norm under orthogonal transformations it follows that

$$
S ( A ^ { \prime } ) = S ( A ) - ( a _ { p q } ^ { 2 } + a _ { q p } ^ { 2 } ) , \qquad S ( A ) = \| A - D \| _ { F } ^ { 2 } .
$$

This is the basis for a proof that the matrices generated by Kogbetliantz's method converge to a diagonal matrix containing the singular values of $A$ .Orthogonal sets of left and right singular vectors can be obtained by accumulating the product of all the transformations. Convergence is analyzed in Paige and Van Dooren [869,1g86] and Fernando [401,1989].

Kogbetliantz's method should not be applied directly to $A$ but to the triangular matrix $R$ obtained by an initial pivoted QR factorization. It can be shown that one sweep of the row cyclic algorithm (7.2.13) applied to an upper triangular matrix generates a lower triangular matrix and vice versa. The annihilation of the elements in the first row for $n = 4$ by plane rotations $( 1 , 2 ) , ( 1 , 3 ) , ( 1 , 4 )$ from the left is pictured below:

$$
\left( \begin{array} { l l l l } { x } & { a _ { 0 } } & { b _ { 0 } } & { c _ { 0 } } \\ { 0 } & { x } & { d _ { 0 } } & { e _ { 0 } } \\ { 0 } & { 0 } & { x } & { f _ { 0 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { l l l l } { x } & { 0 } & { b _ { 1 } } & { c _ { 1 } } \\ { 0 } & { x } & { d _ { 1 } } & { e _ { 1 } } \\ { 0 } & { 0 } & { x } & { f _ { 0 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { l l l l } { x } & { 0 } & { 0 } & { c _ { 2 } } \\ { g _ { 0 } } & { x } & { d _ { 2 } } & { e _ { 1 } } \\ { 0 } & { 0 } & { x } & { f _ { 1 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { l l l l } { x } & { 0 } & { 0 } & { 0 } \\ { g _ { 1 } } & { x } & { d _ { 2 } } & { e _ { 2 } } \\ { h _ { 0 } } & { 0 } & { x } & { f _ { 2 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) .
$$

The switching between upper and lower triangular format can be avoided by a simple permutation scheme; see Fernando [401,198g]. This makes it possible to reorganize the algorithm so that at each stage of the recursion one only needs to store and process a triangular matrix. The resulting algorithm is highly suitable for parallel computing. The reorganization of the row cyclic scheme is achieved by the following algorithm (see also Luk [762,1986] and Charlier, Vanbegin,and Van Dooren [236,1988]):

$$
\begin{array} { c } { \mathrm { ~ : o r ~ } i = 1 : n - 1 } \\ { \mathrm { ~ f o r ~ } i _ { k } = 1 : n - i } \\ { A = P _ { i _ { k } } J _ { i _ { k } , i _ { k } + 1 } ( \phi _ { k } ) A J _ { i _ { k } , i _ { k } + 1 } ^ { T } ( \psi _ { k } ) P _ { i _ { k } } ^ { T } } \end{array}
$$

where $P _ { i _ { k } }$ denotes a permutation matrix that interchanges rows $i _ { k }$ and $i _ { k } + 1$ . The permutations will shuffle the rows and columns of $A _ { k }$ so that each index pair $( i _ { k } , j _ { k } )$ in the row cyclic scheme becomes an adjacent pair of type $( i _ { k } , i _ { k } + 1 )$ when it is its turn to be processed. The permutations involved are performed simultaneously with the rotations at no extra cost. In this scheme,only rotations on adjacent rows and columns occur.

Below we picture the annihilation of the elements in the first row for $n = 4$ for the reorganized scheme.After elimination of $a _ { 0 }$ , the first and second rows and columns are interchanged. Element $b _ { 1 }$ is now in the first superdiagonal and can be annihilated. Again, by interchanging the third and fourth rows and columns, $c _ { 2 }$ is brought to the superdiagonal and can be eliminated. The resulting matrix is still upper triangular:

$$
\left( \begin{array} { c c c c } { x } & { a _ { 0 } } & { b _ { 0 } } & { c _ { 0 } } \\ { 0 } & { x } & { d _ { 0 } } & { e _ { 0 } } \\ { 0 } & { 0 } & { x } & { f _ { 0 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { c c c c } { x } & { 0 } & { d _ { 1 } } & { e _ { 1 } } \\ { 0 } & { x } & { b _ { 1 } } & { c _ { 1 } } \\ { 0 } & { 0 } & { x } & { f _ { 0 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { c c c c } { x } & { d _ { 2 } } & { g _ { 0 } } & { e _ { 1 } } \\ { 0 } & { x } & { 0 } & { f _ { 1 } } \\ { 0 } & { 0 } & { x } & { c _ { 2 } } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) \Rightarrow \left( \begin{array} { c c c c } { x } & { d _ { 2 } } & { e _ { 2 } } & { g _ { 1 } } \\ { 0 } & { x } & { f _ { 2 } } & { h _ { 0 } } \\ { 0 } & { 0 } & { x } & { 0 } \\ { 0 } & { 0 } & { 0 } & { x } \end{array} \right) .
$$

Because of its simplicity, Kogbetliantz's algorithm has been adapted to computation of the generalized singular value decomposition. Further developments of the Kogbetliantz SVD algorithm are given by Hari and Veselic [591,1987]. Bujanovic and Drma& [184, 2012] study the convergence and practical applications of the block version of Kogbetliantz's method.

# 7.2.3 - Divide-and-Conquer Methods

The first divide-and-conquer algorithm for the symmetric tridiagonal eigenproblem is due to Cuppen [280,1g81]. The basic idea is to split the tridiagonal matrix

$$
T = \left( \begin{array} { c c c c c c } { \alpha _ { 1 } } & { \beta _ { 2 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & { \beta _ { 3 } } & & & \\ & { \beta _ { 3 } } & { \ddots } & { \ddots } & & \\ & & { \ddots } & { \alpha _ { n - 1 } } & { \beta _ { n } } \\ & & & { \beta _ { n } } & { \alpha _ { n } } \end{array} \right) \in \mathbb { R } ^ { n \times n }
$$

into two smaller symmetric tridiagonal matrices $T _ { 1 }$ and $T _ { 2 }$ by a symmetric rank-one modification chosen to annihilate the elements $\beta _ { k }$ in positions $( k , k + 1 )$ and $( k + 1 , k )$ . This is achieved by setting

$$
T = \left( \begin{array} { c c } { T _ { 1 } } & { \beta _ { k } e _ { k } e _ { 1 } ^ { T } } \\ { \delta _ { k } e _ { 1 } e _ { k } ^ { T } } & { T _ { 2 } } \end{array} \right) = \left( \begin{array} { c c } { \hat { T } _ { 1 } } & { 0 } \\ { 0 } & { \hat { T } _ { 2 } } \end{array} \right) + \beta _ { k } \left( \begin{array} { c } { e _ { k } } \\ { e _ { 1 } } \end{array} \right) \left( e _ { k } ^ { T }  &  e _ { 1 } ^ { T } \right) ,
$$

where $1 \leq k \leq n$ The $k$ th diagonal element of $T _ { 1 }$ and the first diagonal element of $T _ { 2 }$ are modified to give $\hat { T } _ { 1 }$ and $\hat { T } _ { 2 }$ . If the eigenvalue decompositions of $\hat { T } _ { 1 }$ and $\hat { T } _ { 2 }$ are known, the eigenvalue decomposition of $T$ could be found by finding the eigensystem of a diagonal matrix modified by a symmetric rank-one matrix. In the divide-and-conquer algorithm,this idea is recursively applied to $T _ { 1 }$ and $T _ { 2 }$ until the subproblem sizes are sufficiently small. This requires at most $\log _ { 2 } n$ steps and gives a fully parallel algorithm.

After modifications given by Dongarra and Sorensen $[ 3 2 4 , 1 9 8 7 ]$ and Gu and Eisenstat [547, 1995],the divide-and-conquer algorithm is competitive in terms of speed and accuracy with the QR algorithm. A divide-and-conquer algorithm for the bidiagonal SVD was given by Jessup and Sorensen [667,1994]. In the following we describe an improved variant by Gu and Eisenstat [546, 1995].

The SVD of a square upper bidiagonal matrix $B \in \mathbb { R } ^ { n \times n }$ can be divided into two independent subproblems as follows:

$$
B = \left( \begin{array} { c c c c c } { { q _ { 1 } } } & { { r _ { 1 } } } & { { } } & { { } } & { { } } \\ { { } } & { { q _ { 2 } } } & { { r _ { 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { q _ { n - 1 } } } & { { r _ { n - 1 } } } \\ { { } } & { { } } & { { } } & { { } } & { { q _ { n } } } \end{array} \right) = \left( \begin{array} { c c } { { B _ { 1 } } } & { { 0 } } \\ { { q _ { k } e _ { k } ^ { T } } } & { { r _ { k } e _ { 1 } ^ { T } } } \\ { { 0 } } & { { B _ { 2 } } } \end{array} \right) ,
$$

where $B _ { 1 } \in \mathbb { R } ^ { ( k - 1 ) \times k }$ and $B _ { 2 } \in \mathbb { R } ^ { ( n - k ) \times ( n - k ) }$ . Substituting the SVD

$$
B _ { 1 } = U _ { 1 } \left( D _ { 1 } \quad 0 \right) V _ { 1 } ^ { T } , \qquad B _ { 2 } = U _ { 2 } D _ { 2 } V _ { 2 } ^ { T }
$$

into (7.2.20) gives

$$
\begin{array} { r } { B = \left( \begin{array} { c c c } { U _ { 1 } } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { U _ { 2 } } \end{array} \right) \left( \begin{array} { c c c } { D _ { 1 } } & { 0 } & { 0 } \\ { q _ { k } l _ { 1 } ^ { T } } & { q _ { k } \lambda _ { 1 } } & { r _ { k } f _ { 2 } ^ { T } } \\ { 0 } & { 0 } & { D _ { 2 } } \end{array} \right) \left( \begin{array} { c c c } { V _ { 1 } } & { 0 } \\ { 0 } & { V _ { 2 } } \end{array} \right) ^ { T } \equiv U C V ^ { T } , } \end{array}
$$

where $( l _ { 1 } ^ { T } \quad \lambda _ { 1 } ) = e _ { k } ^ { T } V _ { 1 }$ is the last row of $V _ { 1 }$ ,and $f _ { 2 } ^ { T } = e _ { 1 } ^ { T } V _ { 2 }$ is the first row of $V _ { 2 }$ .If a permutation matrix $P _ { k }$ interchanges row $k$ and the first block row, then

$$
P _ { k } C P _ { k } ^ { T } = M = \left( \begin{array} { c c c } { { q _ { k } \lambda _ { 1 } } } & { { q _ { k } l _ { 1 } ^ { T } } } & { { r _ { k } f _ { 2 } ^ { T } } } \\ { { 0 } } & { { D _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { D _ { 2 } } } \end{array} \right) .
$$

Let $M = X \Sigma Y ^ { T }$ be the SVD of $M$ . Then the SVD of $B$ is

$$
B = Q \Sigma W ^ { T } , \qquad Q = U P _ { k } ^ { T } X , \quad W = V P _ { k } ^ { T } Y .
$$

The matrix in (7.2.22) has the form

$$
M = \left( \begin{array} { c c c c } { { z _ { 1 } } } & { { z _ { 2 } } } & { { \cdots } } & { { z _ { n } } } \\ { { } } & { { d _ { 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { d _ { n } } } \end{array} \right) = D + e _ { 1 } z ^ { T } ,
$$

where $D = \operatorname { d i a g } \left( d _ { 1 } , d _ { 2 } , \dotsc , d _ { n } \right)$ contains the elements of $D _ { 1 }$ and $D _ { 2 }$ ,and $d _ { 1 } = 0$ is introduced to simplify the notation. We further assume that $0 = d _ { 1 } \leq d _ { 2 } \leq d _ { 3 } \leq \cdot \cdot \cdot \leq d _ { n }$ ,which can be achieved by a reordering of rows and columns.

To compute the SVD $M = D + e _ { 1 } z ^ { T } = X \Sigma Y ^ { T }$ ，we use the fact that the square of the singular values $\Sigma ^ { 2 }$ are the eigenvalues and the right singular vectors $Y$ are the eigenvectors of

$$
M ^ { T } M = X \Sigma ^ { 2 } X ^ { T } = D ^ { 2 } + z e _ { 1 } ^ { T } e _ { 1 } z ^ { T } = D ^ { 2 } + z z ^ { T } .
$$

If $y _ { i }$ is a right singular vector, then $M y _ { i }$ is a vector in the direction of the corresponding left singular vector.

We note that if $z _ { i } = 0$ ,or $d _ { i } = d _ { i + 1 }$ for some $i \in [ 2 , n - 1 ]$ ,then $d _ { i }$ is a singular value of $M$ ， and the degree of the characteristic equation of $M ^ { T } M$ may be reduced by one. We can therefore assume that $| z _ { i } | \neq 0$ ， $i = 1 : n$ ,and that $d _ { i } \neq d _ { i + 1 }$ ， $i = 1 \colon n - 1$ . In practice,the assumptions above must be replaced by

$$
d _ { j + 1 } - d _ { j } \geq \tau \| M \| _ { 2 } , \qquad | z _ { j } | \geq \tau \| M \| _ { 2 } ,
$$

where $\tau$ depends on the unit roundoff.

The above facts gives the following characterization of the singular values and vectors of $M$ ； see Jessup and Sorensen [667,1994].

Lemma 7.2.3. Let the SVD of the matrix in (7.2.24) be $M = X \Sigma Y ^ { T }$ ,with

$$
X = ( x _ { 1 } , \ldots , x _ { n } ) , \quad \Sigma = \operatorname { d i a g } \big ( \sigma _ { 1 } , \ldots , \sigma _ { n } \big ) , \quad Y = ( y _ { 1 } , \ldots , y _ { n } ) .
$$

Then the singular values have the interlacing property

$$
0 = d _ { 1 } < \sigma _ { 1 } < d _ { 2 } < \sigma _ { 2 } < \cdots < d _ { n } < \sigma _ { n } < d _ { n } + \| z \| _ { 2 } ,
$$

where $z = ( z _ { 1 } , \ldots , z _ { n } ) ^ { T }$ , and they are roots of the characteristic equation

$$
f ( \sigma ) = 1 + \sum _ { k = 1 } ^ { n } { \frac { z _ { k } ^ { 2 } } { d _ { k } ^ { 2 } - \sigma ^ { 2 } } } = 0 .
$$

The characteristic equation can be solved eficiently and accurately by the algorithm of Li [743,1994]. The singular values of $M$ are always well-conditioned. The singular vectors are $x _ { i } = { \tilde { x } } _ { i } / \| { \tilde { x } } _ { i } \| _ { 2 } , y _ { i } = { \tilde { y } } _ { i } / \| { \tilde { y } } _ { i } \| _ { 2 } , i = 1 { : } n _ { \mathrm { ~ } }$ ，where

$$
\tilde { y } _ { i } = \left( \frac { z _ { 1 } } { d _ { 1 } ^ { 2 } - \sigma _ { i } ^ { 2 } } , \ldots , \frac { z _ { n } } { d _ { n } ^ { 2 } - \sigma _ { i } ^ { 2 } } \right) , \qquad \tilde { x } _ { i } = \left( - 1 , \frac { d _ { 2 } z _ { 2 } } { d _ { 2 } ^ { 2 } - \sigma _ { i } ^ { 2 } } , \ldots , \frac { d _ { n } z _ { n } } { d _ { n } ^ { 2 } - \sigma _ { i } ^ { 2 } } \right) ,
$$

and

$$
\| \tilde { y } _ { i } \| _ { 2 } ^ { 2 } = \sum _ { j = 1 } ^ { n } \frac { z _ { j } ^ { 2 } } { ( d _ { j } ^ { 2 } - \sigma _ { i } ^ { 2 } ) ^ { 2 } } , \qquad \| \tilde { x } _ { i } \| _ { 2 } ^ { 2 } = 1 + \sum _ { j = 2 } ^ { n } \frac { ( d _ { j } z _ { j } ) ^ { 2 } } { ( d _ { j } ^ { 2 } - \sigma _ { i } ^ { 2 } ) ^ { 2 } } .
$$

The singular vectors can be extremely sensitive to the presence of close singular values. To get accurately orthogonal singular vectors without resorting to extended precision is a dificult problem; see Gu and Eisenstat [546,1995].

# Notes and references

Van Zee,van de Geijn, and Quintana-Orti [1084, 2O14] describe ways to restructure the plane rotations in the QRSVD algorithm to achieve better parallel performance. Dongarra et al. [323, 2018] survey the history of SVD algorithms.In particular, they review reformulations designed to take advantage of new computer architectures,such as cache-based memory hierarchies and distributed computing.

# 7.2.4 - Modifying the SVD

Suppose the SVD of a matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$

$$
A = U \left( \begin{array} { l } { { \Sigma } } \\ { { 0 } } \end{array} \right) V ^ { T } , \quad \Sigma = \mathrm { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { n } \right) ,
$$

with orthogonal $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ is known. In many applications it is desirable to update the SVD when $A$ is modified by a matrix of low rank to incorporate new data. Exam-ples are subspace tracking in signal processing and latent semantic indexing; see Moonen, Van Dooren,and Vandewalle [803,1992] and Zha and Simon [1146,1999].

The goal is to take advantage of knowledge of the SVD of $A$ to reduce the work required. However, many of the proposed updating schemes for the SVD can be as expensive as computing the SVD from scratch. The costliest part of the updating is the rotation and reorthogonalization of $U$ and $V$ ,and most updating algorithms for the SVD require $O ( m n ^ { 2 } )$ flops. Although this is the same order of complexity as for recomputing the SVD from scratch,there can still be a gain if the order constant is less.

In the SVD,rows and columns are treated the same. Hence,appending or deleting a column in $A$ can be treated by appending or deleting a row in $A ^ { T }$ . This simplifies the updating problem in that only modifications of rows need be considered. (Of course, in the least squares updating, there is a lack of symmetry.） In particular, if the SVD of $A$ is to be used for solving the least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ via

$$
\begin{array} { r } { x = V \Sigma ^ { \dagger } c , \quad c = U ^ { T } b , } \end{array}
$$

then we would like to update $U , V , \Sigma$ ,and $c$ in order to update $x$

Given the SVD $A = U \Sigma V ^ { T }$ ,consider the problem of computing the SVI

$$
\tilde { A } = \left( \begin{array} { c } { A } \\ { w ^ { T } } \end{array} \right) , \quad w \in \mathbb { R } ^ { n } ,
$$

when a row $w ^ { T }$ is appended to $A$ . From the relationship between the SVD of $A$ and the symmetric eigenvalue problem for $A ^ { T } A$ we have

$$
\begin{array} { r } { \tilde { A } ^ { T } \tilde { A } = A ^ { T } A + w w ^ { T } = V \Sigma ^ { 2 } V ^ { T } + w w ^ { T } = V ( \Sigma ^ { 2 } + \rho ^ { 2 } z z ^ { T } ) V ^ { T } = \tilde { V } \tilde { \Sigma } ^ { 2 } \tilde { V } ^ { T } , } \end{array}
$$

where $z = ( \zeta _ { 1 } , . . . , \zeta _ { n } ) = V ^ { T } w / \rho$ and $\rho ~ = ~ \| w \| _ { 2 }$ .Hence $\tilde { \Sigma } ^ { 2 }$ and $\tilde { V }$ are the solution to a symmetric eigenvalue problem modified by a perturbation of rank one. Such problems can be solved by using the observation (see Golub 490,1973l) that the eigenvalues $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdot \cdot \cdot \geq$ $\lambda _ { n }$ of

$$
C = D + \rho ^ { 2 } z z ^ { T } , \quad D = \mathrm { d i a g } \left( d _ { 1 } , d _ { 2 } , \ldots , d _ { n } \right) , \quad \| z \| _ { 2 } = 1 ,
$$

where $d _ { 1 } \geq d _ { 2 } \geq \cdot \cdot \cdot \geq d _ { n }$ , are the values of $\lambda$ for which

$$
g ( \lambda ) = 1 + \rho ^ { 2 } \sum _ { j = 1 } ^ { n } \frac { \zeta _ { j } ^ { 2 } } { ( d _ { j } - \lambda ) } = 0 .
$$

Good initial approximations to the roots can be obtained from the interlacing property (see Theorem 1.3.5)

$$
\lambda _ { 1 } \geq d _ { 1 } \geq \lambda _ { 2 } \geq \cdot \cdot \cdot \geq d _ { n - 1 } \geq \lambda _ { n } \geq d _ { n } .
$$

To solve equation (7.2.28) a method based on rational approximation safeguarded with bisection is used. The subtle details in a stable implementation of such an algorithm are treated by Li [743, 1994].

When the modified eigenvalues $\tilde { d } _ { i } = \tilde { \sigma } _ { i } ^ { 2 }$ have been calculated, the corresponding eigenvectors are found by solving

$$
( D _ { i } + \rho ^ { 2 } z z ^ { T } ) x _ { i } = 0 , \quad D _ { i } = D - \tilde { d } _ { i } ^ { 2 } I .
$$

Provided $D _ { i }$ is nonsingular (this can be ensured by an initial deflation),we have $x _ { i } = D _ { i } ^ { - 1 } z /$ $\| D _ { i } ^ { - 1 } z \| _ { 2 }$ . (Note that forming $D _ { i } ^ { - 1 } z$ explicitly should be avoided in practice; see Bunch and Nielsen [188,1978].) The updated right singular vectors are $\tilde { V } = V X$ ,where $X = ( x _ { 1 } , \ldots , x _ { n } )$ If $A$ (or $\tilde { A }$ ） is still available,the updated left singular vectors $\tilde { U }$ can be computed from $\tilde { U } =$ $\tilde { A } \tilde { V } \tilde { \Sigma } ^ { - 1 }$ .

An alternative approach for appending a row is given by Businger [192,197o]. We have

$$
\begin{array} { r } { \left( \begin{array} { c c } { U ^ { T } } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c } { A } \\ { w ^ { T } } \end{array} \right) V = \Pi _ { n + 1 , m + 1 } \left( \begin{array} { c } { L } \\ { 0 } \end{array} \right) , \qquad L = \left( \begin{array} { c } { \Sigma } \\ { w ^ { T } V } \end{array} \right) , } \end{array}
$$

where $\Pi _ { n + 1 , m + 1 }$ denotes a permutation matrix interchanging rows $n + 1$ and $m + 1$ ,and $L$ is a special lower triangular matrix. Businger's updating algorithm consists of two major phases. The first phase isafinite process that trasforms $L \in \bar { \mathbb { R } ^ { ( n + 1 ) \times n } }$ into upper bidiagonal form using plane rotations from left and right:

$$
G _ { 1 } L G _ { 2 } = \left( \begin{array} { l } { \tilde { B } } \\ { 0 } \end{array} \right) , \qquad \tilde { B } \in \mathbb { R } ^ { n \times n } .
$$

The second phase is an implicit QR diagonalization of $\tilde { B }$ (see Section 7.1.1) that reduces $\tilde { B }$ to diagonal form $\tilde { \Sigma }$

In the $k$ th step of phase 1, the $k$ th element of $w ^ { T } V$ $k = 1 : n - 1 )$ is eliminated using plane rotations and a chasing scheme on rows and columns. This is pictured below for $n = 5$ and $k = 3$ ：

$$
( \begin{array} { l l l l l } { \times } & { \times } & { \downarrow } & { \downarrow } & { } \\ { \times } & { \times } & { \times } & { + } \\ & { \times } & { \times } & { + } \\ & { + } & { \times } & { } \\ { 0 } & { 0 } & { \oplus } & { \times } & { \times } \end{array} ) \Rightarrow \begin{array} { l } { \to } \\ { \to } \\ { \to } \\ { \to } \\ { 0 } \end{array} \to ( \begin{array} { l l l l } { \times } & { \times } & { } & { \times } & { } \\ { \times } & { \times } & { \times } & { \times } \\ { } & { \times } & { \times } & { } \\ { } & { \oplus } & { \times } & { } \\ { 0 } & { 0 } & { 0 } & { \times } & { \times } \end{array} ) \Rightarrow \begin{array} { l } { \to } \\ { \to } \\ { \to } \\ { \to } \\ { \Uparrow } & { \Uparrow } & { \times } & { \times } \end{array} )
$$

$$
\left( \begin{array} { l l l l l l l } { { } } & { { } } & { { \downarrow } } & { { \downarrow } } & { { } } & { { } } & { { } } & { { } } \\ { { \times } } & { { \times } } & { { + } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \times } } & { { \times } } & { { } } & { { } } & { { } } \\ { { \oplus } } & { { \times } } & { { \times } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \times } } & { { } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \times } } & { { \times } } \end{array} \right) \Rightarrow \quad \left( \begin{array} { l l l l l } { { \times } } & { { \times } } & { { \oplus } } & { { } } & { { } } & { { } } \\ { { + } } & { { \times } } & { { \times } } & { { } } & { { } } & { { } } \\ { { } } & { { \times } } & { { \times } } & { { \times } } & { { } } & { { } } \\ { { } } & { { } } & { { \times } } & { { \times } } & { { } } & { { } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \times } } & { { \times } } \end{array} \right) \Rightarrow \quad \left( \begin{array} { l l l l l } { { \times } } & { { \times } } & { { } } & { { } } & { { } } & { { } } \\ { { \oplus } } & { { \times } } & { { \times } } & { { } } & { { } } & { { } } \\ { { } } & { { \times } } & { { \times } } & { { \times } } & { { } } & { { } } \\ { { } } & { { } } & { { \times } } & { { } } & { { } } \\ { { } } & { { } } & { { \times } } & { { \times } } & { { } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \times } } & { { \times } } \end{array} \right) .
$$

Phase 1 uses $n ( n - 1 ) / 2$ row and column rotations. Most of the work is used to apply these rotations to $U$ and $V$ . This requires $2 n ^ { 2 } ( m + n )$ flops if standard plane rotations are used. For updating least squares solutions we only need to update $V , \Sigma$ and $c = U ^ { T } b$ ，The dominating term is then reduced to $2 n ^ { 3 }$ flops. Zha [1144,1992] shows that the work can be halved by using a two-way chasing scheme in the reduction to bidiagonal form. Phase 2 typically requires about $3 n ^ { 3 }$ flops. Note that $\Sigma$ and $V$ can be updated without $U$ being available. From the interlacing property (Theorem 1.3.5) it follows that the smallest singular value willincrease. Hence the rank cannot decrease.

When the SVD is to be modified by deleting a row, with no loss of generality we can assume that the first row of $A$ is to be deleted. Then we wish to determine the SVD of $\tilde { A } \in \mathbb { R } ^ { ( m - 1 ) \times n }$ when the SVD

$$
A = \left( \begin{array} { c } { { z ^ { T } } } \\ { { \tilde { A } } } \end{array} \right) = U \left( \begin{array} { c c } { { \Sigma } } \\ { { 0 } } \end{array} \right) V ^ { T }
$$

is known. This problem can be reduced to a modified eigenvalue problem of the form

$$
C = D - \rho ^ { 2 } z z ^ { T } , \quad D = \mathrm { d i a g } \left( d _ { 1 } , d _ { 2 } , \ldots , d _ { n } \right) , \quad \| z \| _ { 2 } = 1 .
$$

The interlacing property now gives $d _ { 1 } \geq \tilde { d } _ { 1 } \geq d _ { 2 } \geq \cdots \geq \tilde { d } _ { n - 1 } \geq d _ { n } \geq \tilde { d } _ { n } \geq 0 .$ Hence the Bunch-Nielsen scheme is readily adapted to solving this problem.

Park and Van Hufel [882,1995l give a backward stable algorithm based on finding the SVD of $( e _ { 1 } , A )$ ,where $e _ { 1 }$ is an added dummy column. Then

$$
U ^ { T } ( e _ { 1 } , A ) \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} \right) = \left( \begin{array} { c c } { { u _ { 1 } } } & { { \Sigma } } \\ { { u _ { 2 } } } & { { 0 } } \end{array} \right) ,
$$

where $( u _ { 1 } ^ { T } , u _ { 2 } ^ { T } )$ is the first row of $U$ . First, determine left and right plane rotations $G _ { 1 }$ and $G _ { 2 }$ S0 that

$$
G _ { 1 } \left( \begin{array} { c c } { { u _ { 1 } } } & { { \Sigma } } \\ { { u _ { 2 } } } & { { 0 } } \end{array} \right) G _ { 2 } = \left( \begin{array} { c c } { { 1 } } & { { w ^ { T } } } \\ { { 0 } } & { { \tilde { B } } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

with $\tilde { B }$ upper bidiagonal. This can be achieved by a chasing scheme similar to that used when adding a row. The desired bidiagonal form is built from bottom to top, while nonzeros are chased into the lower-right corner. The reduction is pictured below for $k = 3$ ， $n = 4$ ：

$$
\begin{array} { r l r } { \to \left( \begin{array} { l l l l } { \times } & { \times } & & \\ { \times } & & { \times } & { + } \\ { \oplus } & & { + } & { \times } \\ { 0 } & & & { \times } & { \times } \\ { 0 } & & & { \times } & { \times } \end{array} \right) \Rightarrow } & { \left( \begin{array} { l l l l } { \times } & { \times } & & { \downarrow } & { \downarrow } \\ { \times } & & { \times } & { \oplus } \\ { 0 } & & { \times } & { \times } \\ { 0 } & & { + } & { \times } & { \times } \\ { 0 } & & & { \times } \end{array} \right) \Rightarrow \to \left( \begin{array} { l l l l } { \times } & { \times } & & \\ { \times } & & { \times } & \\ { 0 } & & { \times } & { \times } \\ { 0 } & & & { \oplus } & { \times } \\ { 0 } & & & { \times } \end{array} \right) } \\ & { } & { \times } & { \left( \begin{array} { l l l l } { \times } & & { \times } & \\ & & { \times } & \\ & & & { \times } \end{array} \right) } \end{array}
$$

$$
\begin{array} { r l r } { ( \begin{array} { l l l l l l } { { \times } } & { { \times } } & { { } } & { { } } & { { } } & { { } } \\ { { \times } } & { { } } & { { \times } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { } } & { { \times } } & { { \times } } & { { \oplus } } \\ { { 0 } } & { { } } & { { } } & { { \times } } & { { \times } } \\ { { 0 } } & { { } } & { { + } } & { { \times } } \end{array} ) } & { { } \Rightarrow } & { { } et { } { ' } \begin{array} { l l l l l } { { \times } } & { { \times } } & { { } } & { { } } & { { } } \\ { { \times } } & { { } } & { { \times } } & { { } } & { { } } \\ { { 0 } } & { { } } & { { \times } } & { { \times } } & { { } } \\ { { 0 } } & { { } } & { { } } & { { \times } } & { { \times } } \\ { { 0 } } & { { } } & { { } } & { { \oplus } } & { { \times } } \end{array} ) . } \end{array}
$$

A total of $( n - 1 ) ^ { 2 } + 1$ plane rotations are needed to make the first column of $G _ { 1 } U ^ { T }$ equal to $e _ { 1 } ^ { T }$ . From orthogonality it follows that this matrix must have the form

$$
G _ { 1 } U ^ { T } = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \bar { U } ^ { T } } } \end{array} \right) ,
$$

with $\bar { U }$ orthogonal. Since no rotation from the right involves the first column, the transformed matrix has the form

$$
\left( { \begin{array} { c c } { { \alpha } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} } \right) G _ { 2 } = \left( { \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \bar { V } } } \end{array} } \right) .
$$

It now follows that

$$
\left( { \begin{array} { c c } { \alpha } & { 0 } \\ { 0 } & { { \bar { U } } ^ { T } } \end{array} } \right) \left( { \begin{array} { c c } { 1 } & { z ^ { T } } \\ { 0 } & { { \tilde { A } } } \end{array} } \right) \left( { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { { \bar { V } } } \end{array} } \right) = \left( { \begin{array} { c c } { \alpha } & { w ^ { T } } \\ { 0 } & { { \tilde { B } } } \\ { 0 } & { 0 } \end{array} } \right) ,
$$

which gives $\bar { U } ^ { T } \tilde { A } \bar { V } = \binom { \tilde { B } } { 0 }$ . In the second phase,the implicit QRsVD is used toreduce $\tilde { B }$ t0 diagonal form $\tilde { \Sigma }$ . Simultaneously $\bar { U }$ and $\bar { V }$ are updated.

# Notes and references

Bunch and Nielsen [188,1978] develop updating methods related to updating symmetric eigenvalue decompositions. The technique used by Businger to update the SVD is related to that for updating the QR decomposition; see Barlow, Zha, and Yoon [80,1993l. An approximate updating algorithm for the SVD is developed by Moonen, Van Dooren, and Vandewalle [8O3,1992]. In the first step, a row is appended or deleted,and the resulting matrix is reduced to triangular form. Jacobi-type sweeps are then applied to restore approximate diagonal form. Gu and Eisenstat [545,1993], [548,1995] reduce the updating and downdating of the SVD to the problem of computing the SVD of a matrix of simple structure that can be solved by computing the roots of a secular equation. Brand [176,2oo6] develops an effcient scheme for low-rank modification of the thin SVD of streaming data.

# 7.3- Computing Selected Singular Triplets

# 7.3.1 - Shifted Inverse Iteration

In many applications,e.g.,low-rank approximations, information retrieval,and seismic tomogra-phy,a few, singular values $\sigma _ { i }$ and the corresponding left and right singular vectors $u _ { i } \in C m$ ,and $v _ { i } \in C n$ of a large Hermitian matrix $A$ are required. A related problem is to compute selected eigenpairs $\lambda _ { i } = \sigma _ { i } ^ { 2 }$ of the Hermitian matrices

$$
A ^ { H } A v _ { i } = \lambda v _ { i } \quad { \mathrm { a n d } } \quad A A ^ { H } u _ { i } = \lambda u _ { i } .
$$

In general it is not necessary,or even advisable, to form $A ^ { H } A$ or $A A ^ { H }$ . The squaring of the singular values is a drawback,as it willforce the clustering of smal singular values. Instead, one may consider the equivalent Hermitian eigenvalue problem

$$
\left( \begin{array} { c c } { { 0 } } & { { A } } \\ { { A ^ { H } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { u } } \\ { { \pm v } } \end{array} \right) = \pm \sigma \left( \begin{array} { c } { { u } } \\ { { \pm v } } \end{array} \right) .
$$

This yields the singular values and both the left and right singular vectors. If $r = { \mathrm { r a n k } } ( A )$ ， then $M$ has $2 r$ nonzero eigenvalues, $\pm \sigma _ { 1 } ( A ) , \ldots , \pm \sigma _ { r } ( A )$ .Here the small singular values of $A$ correspond to interior eigenvalues of the Hermitian matrix.

Let $A \in \mathbb { C } ^ { n \times n }$ be a Hermitian matrix with eigenpairs $\lambda _ { i } , x _ { i } , i = 1 , . ~ . . , n$ . Given a unit initial vector $z ^ { ( 0 ) }$ , the power method forms the vector sequence $z ^ { ( k ) } = A ^ { k } z ^ { ( 0 ) }$ using the recursion

$$
z ^ { ( k ) } = A z ^ { ( k - 1 ) } , \quad k = 1 , 2 , \dots .
$$

This only requires the ability to form products $\left| { \lambda } _ { 1 } \right| > \left| { \lambda } _ { 2 } \right| \geq \cdot \cdot \cdot \geq \left| { \lambda } _ { n } \right|$ expanding $z ^ { ( 0 ) }$ alon the eigenvectorsgives $A z$ for given vectors $z$ . If the eigenvalues satisfy $\begin{array} { r } { z ^ { ( 0 ) } = \sum _ { j = 1 } ^ { n } \alpha _ { j } x _ { j } } \end{array}$ and

$$
z ^ { ( k ) } = A ^ { k } z ^ { ( 0 ) } = \sum _ { j = 1 } ^ { n } \lambda _ { j } ^ { k } \alpha _ { j } x _ { j } = \lambda _ { 1 } ^ { k } \bigg ( \alpha _ { 1 } x _ { 1 } + \sum _ { j = 2 } ^ { n } \bigg ( \frac { \lambda _ { j } } { \lambda _ { 1 } } \bigg ) ^ { k } \alpha _ { j } x _ { j } \bigg ) ,
$$

$k = 1 , 2 , \ldots .$ If $\alpha _ { 1 } \neq 0$ and $| \lambda _ { j } | / | \lambda _ { 1 } | < 1 ( j \neq 1 )$ , it follows from (7.3.4) that $z ^ { ( k ) }$ converges with linear rate $| \lambda _ { 2 } | / | \lambda _ { 1 } |$ to the normalized eigenvector $x _ { 1 }$ as $k  \infty$ .To avoid overflow or underflow, recursion (7.3.3) should be modified to

$$
\widehat { z } ^ { ( k ) } = A z ^ { ( k - 1 ) } , \quad z ^ { ( k ) } = \widehat { z } ^ { ( k ) } / \| \widehat { z } ^ { ( k ) } \| _ { 2 } , \quad k = 1 , 2 , \ldots .
$$

Let $x \in \mathbb { C } ^ { n }$ be a given approximate eigenvector for a Hermitian matrix $A \in \mathbb { C } ^ { n \times n }$ . Then $( \lambda , x )$ is an exact eigenpair of $A$ if and only if the residual $r = A x - \lambda x = 0$ By continuity, we can expect that $\| r \| _ { 2 }$ can be used as a measure of the accuracy of the eigenpair. Hence it makes sense to determine $\lambda$ as the solution to the linear least squares problem $\mathrm { m i n } _ { \lambda } \| A x - \lambda x \| _ { 2 }$ .The solution has the property that $A x - \lambda x \perp x$ and is given by the Rayleigh quotient

$$
\lambda = \frac { x ^ { H } A x } { x ^ { H } x } .
$$

Theorem 7.3.1. Let x be given a unit vector and $A$ be a Hermitian matrix. Then $( \mu , x )$ ，where $\mu = x ^ { H } A x$ is the Rayleigh quotient, is an exact eigenpair of $\widetilde { A } = A + E$ ，where

$$
E = - ( r x ^ { H } + x r ^ { H } ) , \qquad r = A x - \mu x , \qquad \| E \| _ { 2 } = \| r \| _ { 2 } .
$$

Proof. Since $r$ is orthogonal to $x$ , it follows that $E x = - r$ and

$$
( A + E ) x = A x - r = \mu x .
$$

Hence $( \mu , x )$ is an exact eigenpair of $A + E$ .Furthermore, $\| E \| _ { 2 } ^ { 2 } = \| E ^ { H } E \| _ { 2 }$ is the largest eigenvalue of the rank-two matrix

$$
\begin{array} { r } { { E ^ { H } E } = r { r ^ { H } + \| r \| _ { 2 } ^ { 2 } x { x ^ { H } } } . } \end{array}
$$

This shows that $r$ and $x$ are orthogonal eigenvectors of $E ^ { H } E$ ，with both eigenvalues equal to $r ^ { H } r = \| r \| _ { 2 } ^ { 2 }$ .The other eigenvalues are zero,and hence $\| E \| _ { 2 } = \| r \| _ { 2 }$ □

The gradient of the Rayleigh quotient is

$$
{ \frac { 1 } { 2 } } \nabla \mu ( x ) = { \frac { A x } { x ^ { H } x } } - { \frac { x ^ { H } A x } { ( x ^ { H } x ) ^ { 2 } } } x = { \frac { 1 } { x ^ { H } x } } ( A x - \lambda x ) .
$$

Hence the Rayleigh quotient $\mu ( x )$ is stationary if and only if $x$ is an eigenvector of $A$ Hence $\mu ( x )$ usually is a far more accurate approximate eigenvalue than $x$ is an approximate eigenvector. If we apply the Rayleigh quotient to the Hermitian system (7.3.2) we obtain

$$
\mu ( u , v ) = \frac { 1 } { 2 } ( u ^ { T } , \pm v ^ { T } ) \left( \begin{array} { c c } { { 0 } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { u } } \\ { { \pm v } } \end{array} \right) = \pm u ^ { T } A v ,
$$

where $u$ and $v$ are unit vectors. Here $\mathrm { s i g n } ( v )$ can be chosen to give a real nonnegative value of

$\mu ( u , v )$ . Given approximate right and left singular vectors of $A \in \mathbb { R } ^ { m \times n }$ , the Rayleigh quotient approximations to the dominant singular value are

$$
\mu ^ { 1 / 2 } ( \boldsymbol { v } ) = \| \boldsymbol { A v } \| _ { 2 } / \| \boldsymbol { v } \| _ { 2 } , \qquad \mu ^ { 1 / 2 } ( \boldsymbol { u } ) = \| \boldsymbol { A } ^ { T } \boldsymbol { u } \| _ { 2 } / \| \boldsymbol { u } \| _ { 2 } ,
$$

respectively. Theorem 7.3.1 implies the following residual error bound.

Theorem 7.3.2. For any scalar $\alpha$ and unit vectors $u , v _ { \mathrm { { i } } }$ ， there is a singular value $\sigma$ of $A$ such that

$$
\left| \sigma - \alpha \right| \leq \frac { 1 } { \sqrt { 2 } } \left\| \left( \begin{array} { c } { { A v - u \alpha } } \\ { { A ^ { T } u - v \alpha } } \end{array} \right) \right\| _ { 2 } .
$$

For fixed $u , v$ this error bound is minimized by taking $\alpha$ equal to the Rayleigh quotient given in (7.3.9).

The power method computes approximate eigenvectors of a Hermitian matrix $A$ for the ei-genvalue of largest magnitude. Approximations at the other end of the spectrum can be obtained by applying the power method to $A ^ { - 1 }$ .Given an initial unit vector $v ^ { ( 0 ) }$ ， the inverse power method computes the normalized sequence ${ \boldsymbol { v } } ^ { ( 1 ) } , { \boldsymbol { v } } ^ { ( 2 ) } , { \boldsymbol { v } } ^ { ( 3 ) } , \dots$ , by the recursion

$$
A \widehat { \boldsymbol { v } } ^ { ( k ) } = \boldsymbol { v } ^ { ( k - 1 ) } , \quad \boldsymbol { v } ^ { ( k ) } = \widehat { \boldsymbol { v } } ^ { ( k ) } / \| \widehat { \boldsymbol { v } } ^ { ( k ) } \| _ { 2 } , \quad k = 1 , 2 , \ldots .
$$

Here $v ^ { ( k ) }$ will converge to a unit eigenvector corresponding to the Rayleigh quotient

$$
\mu _ { n } ^ { - 1 } \approx ( v ^ { ( k - 1 ) } ) ^ { H } A ^ { - 1 } v ^ { ( k - 1 ) } = ( v ^ { ( k - 1 ) } ) ^ { H } \widehat { v } ^ { ( k ) } .
$$

This gives an approximation of the eigenvalue $\lambda _ { n }$ of $A$ of smallest magnitude.

The inverse power method (7.3.11) assumes that an appropriate factorization of $A$ is known so that the linear system for $\widehat { v } ^ { ( k ) }$ can be solved. If the QR factorization $A = Q R$ is known, the inverse power method applied to $A = A ^ { T } A$ simplifies to

$$
\widehat { R } ^ { T } w ^ { ( k ) } = z ^ { ( k ) } , \qquad R z ^ { ( k - 1 ) } = w ^ { ( k ) } .
$$

Each step requires two triangular solves.

More generally, for a shift $\mu \neq \lambda _ { i }$ the power method can be applied to the matrix $( A - \mu I ) ^ { - 1 }$ ， with eigenvalues

$$
\theta _ { i } = 1 / ( \lambda _ { i } - \mu ) , \qquad \lambda _ { i } = \mu + 1 / \theta _ { i } , \quad i = 1 , \ldots , n .
$$

By this spectral transformation, eigenvalues close to the shift $\mu$ are transformed into large and well-separated eigenvalues of $( A - \mu I ) ^ { - 1 }$ ; see Figure 7.3.1. Given an initial vector $v _ { 0 }$ ,the shifted inverse power method computes the sequence of vectors

$$
( A - \mu I ) \widehat { v } _ { k } = v _ { k - 1 } , \quad k = 1 , 2 , \ldots .
$$

The corresponding Rayleigh quotient approximation of $\sigma _ { i }$ becomes

$$
\sigma _ { i } ^ { 2 } \approx \mu + 1 / ( v _ { k - 1 } ^ { H } \widehat { v _ { k } } ) .
$$

An a posteriori error bound is $\| r _ { k } \| _ { 2 } / \| \widehat { v } _ { k } \| _ { 2 }$ ,where

$$
r _ { k } = A \widehat { v } _ { k } - \big ( \mu + 1 / \big ( v _ { k - 1 } ^ { H } \widehat { v } _ { k } \big ) \big ) \widehat { v } _ { k } = v _ { k - 1 } - \widehat { v } _ { k } / \big ( v _ { k - 1 } ^ { H } \widehat { v } _ { k } \big ) .
$$

Shifted inverse iteration is usually attributed to Wielandt [1117,1944] but can be traced back to Jacobi's work in 1844. It is a powerful method for computing an eigenvalue in a neighborhood of the shift $\mu$ but requires computing a factorization of the shifted matrix $A - \mu I$

![](images/ef4e9acf30bcb6a15d6c4aa874e55703c5d76c63373aabc7fbb1fb0a948ee5c3.jpg)  
Figure 7.3.1. Spectral transformation with shift $\mu = 1$ Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e ,$ 2015;permission conveyed through Copyright Clearance Center, Inc.

So far we have considered inverse iteration with a fixed shift $\mu$ In Rayleigh-quotient iteration (RQI) a variable shift is used equal to the Rayleigh quotient of the current eigenvector approximation.

# Algorithm 7.3.1 (Rayleigh-Quotient Iteration).

Let $v _ { 0 } \in \mathbb { C } ^ { n }$ be an initial vector ofunit length. Set $\mu _ { 0 } = v _ { 0 } ^ { H } A v _ { 0 }$ , and for $k = 0 , 1 , 2 , \ldots$

1. 1f $A - \mu _ { k } I$ is singular, then solve $( A - \mu _ { k } I ) v _ { k + 1 } = 0$ for unit vector $v _ { k + 1 }$ and stop. Otherwise solve $( A - \mu _ { k } I ) v = v _ { k }$

2. Compute $\eta = \| v \| _ { 2 }$ and set $v _ { k + 1 } = v / \eta , \mu _ { k + 1 } = ( v ^ { H } A v ) / \eta ^ { 2 } .$

3.If $\eta$ is sufficiently large, accept eigenpair $\left( \mu _ { k + 1 } , v _ { k + 1 } \right)$ and stop.

Note that $A v = \mu _ { k } v + v _ { k }$ allows the Rayleigh quotient in step 3 to be updated as

$$
\mu _ { k + 1 } = ( v ^ { H } A v ) / \eta ^ { 2 } = \mu _ { k } + ( v _ { k + 1 } ^ { H } v _ { k } ) / \eta .
$$

If $A$ is Hermitian,the Rayleigh quotient is stationary at eigenvectors,and the local rate of conver-gence is cubic; see Parlett [884,1998,Theorem 4.7.1]. This ensures that the number of correct digits in $v _ { k }$ triples at each step for $k$ large enough.

The norm of the residual $r _ { k } = A v _ { k } - \mu _ { k } v _ { k }$ is the best measure of the accuracy of $( \mu _ { k } , v _ { k } )$ as an eigenpair. A key fact in the global analysis of RQI is that for a Hermitian $A$ the residual norms decrease.

Theorem 7.3.3. For a Hermitian matrix $A$ ， the residual norms in RQI are monotonically decreasing: $\| r _ { k + 1 } \| _ { 2 } \le \| r _ { k } \| _ { 2 }$ . Equality holds only if $\mu _ { k + 1 } = \mu _ { k }$ and $v _ { k }$ is an eigenvector of $( A - \mu _ { k } I ) ^ { 2 }$

Proof. See Parlett [884,1998, Theorem 4.8.1].

In the Hermitian case it is not necessary to assume that RQI converges to an eigenvector corresponding to a simple eigenvalue. Either the iterates $v _ { k }$ will converge cubically to an eigenvector of $A$ ，or the odd and even iterates will converge linearly to the bisectors of a pair of eigenvectors of $A$ ，The latter situation is unstable under small perturbations,so RQI converges from any starting vector; see Parlet [884,1998,Sect. 4.9]. Note that RQI may not converge to an eigenvalue closest to $\mu ( v _ { 0 } )$ . It is not in general obvious how to choose the starting vector to make RQI converge to a particular eigenvalue.

Rayleigh-quotient iteration requires a new factorization of the shifted matrix $A - \mu _ { k } I$ for each iteration. It is therefore considerably more costly than inverse iteration. For a dense matrix the cost for a factorization is $O ( n ^ { 3 } )$ operations.For problems where $A$ is large and sparse it may not be feasible. Then $( A - \mu _ { k } I ) v = v _ { k }$ can be solved inexactly using an iterative solution method.

# 7.3.2 - Subspace Iteration

Let $S = ( s _ { 1 } , \ldots , s _ { p } ) \in \mathbb { R } ^ { n \times p }$ be a given initial matrix of rank $p > 1$ .In subspace iteration a sequence $\{ Z _ { k } \}$ of matrices is generated by

$$
Z _ { 0 } = S , \quad Z _ { k } = M Z _ { k - 1 } , \quad k = 1 , 2 , \ldots ,
$$

where $M \in \mathbb { R } ^ { n \times n }$ is a given symmetric matrix. Then it holds that

$$
Z _ { k } = M ^ { k } S = ( M ^ { k } s _ { 1 } , \ldots , M ^ { k } s _ { p } ) .
$$

In applications, $M$ is often a very large sparse matrix, and $p \ll n$ .If $M$ has a dominant eigenvalue $\lambda _ { 1 }$ , then all columns of $Z _ { k }$ will converge to a scalar multiple of the dominant eigenvector $x _ { 1 }$ . Therefore, $Z _ { k }$ will be close to a matrix of numerical rank one,and it is not clear that much will be gained. If $\begin{array} { r } { S = \operatorname { s p a n } \left( S \right) } \end{array}$ , subspace iteration is actually computing a sequence of subspaces $M ^ { k } S = \mathrm { s p a n } \left( M ^ { k } S \right)$ ．The problem is that $Z _ { k } \ = \ M ^ { k } S$ becomes an increasingly ill-conditioned basis for $M ^ { k } S$ . To avoid this, orthogonality can be maintained between the basis columns as follows. Orthogonal iteration starts with an orthonormal matrix $Q _ { 0 }$ and computes

$$
Z _ { k } = M Q _ { k - 1 } , \qquad Z _ { k } = Q _ { k } R _ { k } , \quad k = 1 , 2 , \ldots .
$$

Here $R _ { k }$ plays the role of a normalizing matrix, and $Q _ { 1 } = Z _ { 1 } R _ { 1 } ^ { - 1 } = M Q _ { 0 } R _ { 1 } ^ { - 1 }$ . By induction, it can be shown that

$$
Q _ { k } R _ { k } \cdot \cdot \cdot R _ { 1 } = M ^ { k } Q _ { 0 } .
$$

Hence the iterations (7.3.16)and(7.3.17) generate the same sequence of subspaces, $\mathcal { R } ( M ^ { k } Q _ { 0 } ) =$ $\mathcal { R } ( Q _ { k } )$ . Since iteration (7.3.16) is less costly, it is sometimes preferable to perform the orthogonalization in (7.3.17) only occasionally as needed. Bauer [94,1957] suggests a procedure called treppen-iteration (staircase iteration) to maintain linear independence of the basis vectors.This is similar to orthogonal iteration but uses LU instead of QR factorizations.

Orthogonal iteration overcomes several disadvantages of the power method. Provided $| \lambda _ { p + 1 } / \lambda _ { p } |$ is small, it can be used to determine the invariant subspace corresponding to the dominant $p$ eigenvalues. Assume that the eigenvalues of $M$ satisfy

$$
| \lambda _ { 1 } | \geq \cdots \geq | \lambda _ { p } | > | \lambda _ { i } | , \quad i = p + 1 , \ldots , n ,
$$

and let

$$
\binom { U _ { 1 } ^ { H } } { U _ { 2 } ^ { H } } M ( U _ { 1 } U _ { 2 } ) = \binom { T _ { 1 1 } } { 0 } T _ { 2 2 } \Biggr )
$$

be a Schur decomposition of $M$ ，where $\mathrm { d i a g } ( T _ { 1 1 } ) = ( \lambda _ { 1 } , \ldots , \lambda _ { p } ) ^ { H }$ .Then the subspace $\mathcal { U } _ { 1 } =$ ${ \mathcal { R } } ( U _ { 1 } )$ is a dominant invariant subspace of $M$ . It can be shown that in orthogonal iteration, the subspaces $\mathcal { R } ( Q _ { k } )$ almost always converge to $\mathcal { U } _ { 1 }$ as $k \to \infty$

The accuracy of an invariant subspace is measured by the distance to the exact invariant subspace; see Definition 1.2.14.

Theorem 7.3.4. Let $\mathcal { U } _ { 1 } = \mathcal { R } ( U _ { 1 } )$ be a dominant invariant subspace of $M$ , as defined in (7.3.19). Let $s$ be a $p$ -dimensional subspace of $\mathbb { C } ^ { n }$ such that ${ \cal S } \cap { \cal U } _ { 1 } ^ { \perp } = \{ 0 \}$ Then there exists a constant $M$ such that

$$
\begin{array} { r } { \theta _ { \operatorname* { m a x } } ( M ^ { k } S , { \mathcal U } _ { 1 } ) \le M | \lambda _ { p + 1 } / \lambda _ { p } | ^ { k } , } \end{array}
$$

where $\theta _ { \mathrm { { m a x } } } ( \mathcal { X } , \mathcal { Y } )$ denotes the largest angle between the two subspaces.

Proof. See Golub and Van Loan [512,1996,p. 333].

Subspace iteration on $p$ vectors simultaneously performs subspace iteration on the nested sequence of subspaces span $\left( { { s _ { 1 } } } \right)$ ,span $( s _ { 1 } , s _ { 2 } )$ ,..., span $( s _ { 1 } , s _ { 2 } , \ldots , s _ { p } )$ . This is also true for orthogonal iteration, because the property is not changed by the orthogonalization procedure. Hence Theorem 7.3.4 shows that whenever $| \lambda _ { q + 1 } / \lambda _ { q } |$ is small for some $q \leq p$ ，convergence to the corresponding dominant invariant subspace of dimension $q$ will be fast.There is a duality between direct and inverse subspace iteration.

Lemma 7.3.5 (Watkins [1103, $\mathbf { 1 9 8 2 } ]$ ). Let $s$ and $\boldsymbol { S ^ { \perp } }$ be orthogonal complementary subspaces of $\mathbb { C } ^ { n }$ . Then for all integers $k$ the spaces $M ^ { k } S$ and $( M ^ { H } ) ^ { - k } S ^ { \perp }$ are also orthogonal.

Proof. Let $x \in S$ and $y \in S ^ { \perp }$ . Then $( M ^ { k } x ) ^ { H } ( M ^ { H } ) ^ { - k } y = x ^ { H } y = 0$ ，and thus $M ^ { k } x \perp$ $( M ^ { H } ) ^ { - k } y$ □

This duality property means that the two sequences of subspaces

$$
S , \ M S , \ M ^ { 2 } S , \ldots \ \mathrm { a n d } \quad S ^ { \perp } , ( M ^ { H } ) ^ { - 1 } S ^ { \perp } , ( M ^ { H } ) ^ { - 2 } S ^ { \perp } , \ldots
$$

are equivalent in the sense that the orthogonal complement of a subspace in one sequence equals the corresponding subspace in the other. This result is important for understanding convergence properties of the QR algorithm. A geometric theory for QR and LR iterations is given by Parlett and Poole [885,1973].

# 7.3.3 - The Rayleigh-Ritz Procedure

Let $M \in \mathbb { C } ^ { n \times n }$ be a given Hermitian matrix with eigenvalues $\lambda _ { i }$ and eigenvectors $x _ { i }$ ， $i = 1 \colon n$ ， and let $\scriptstyle { S _ { k } }$ be a $k$ -dimensional subspace of $\mathbb { C } ^ { n }$ . An approximate eigenpair $( \theta , y )$ of $M$ with $y \in S _ { k }$ can be determined by imposing the Galerkin condition

$$
M y - \theta y \perp S _ { k } .
$$

Let $S _ { k } = \mathcal { R } ( Q _ { k } )$ for some orthonormal matrix $Q _ { k }$ , and set $y = Q _ { k } z$ .Then condition (7.3.20) can be written

$$
Q _ { k } ^ { H } ( M - \theta I ) Q _ { k } z = 0
$$

or, equivalently, as the projected eigenvalue problem

$$
( H _ { k } y - \theta I ) z = 0 , \quad H _ { k } = Q _ { k } ^ { H } M Q _ { k } .
$$

The matrix $H _ { k } \in \mathbb { C } ^ { k }$ is Hermitian and is the matrix Rayleigh quotient of $M$ .Note that the condition of this projected eigenvalue problem is not degraded. In practice, $M$ is often large and sparse,and one is only interested in approximating part of its spectrum. If $k \ll n$ ,the Hermitian eigenvalue problem (7.3.21) is small and can be solved by a standard method, such as the QR algorithm.The solution yields $k$ approximate eigenvalues and eigenvectors of $M$ as described in the procedure below.

# Algorithm 7.3.2 (The Rayleigh-Ritz Procedure).

Let $M \in \mathbb { C } ^ { n \times n }$ be a given Hermitian matrix, and let $Q _ { k } = ( q _ { 1 } , \ldots , q _ { k } )$ be an orthonormal basis for a given $k$ -dimensional subspace of $\mathbb { C } ^ { n }$ ， $k \ll n$

1. Compute the matrix $M Q _ { k } = \left( M q _ { 1 } , \dots , M q _ { k } \right)$ and the matrix Rayleigh quotient

$$
H _ { k } = Q _ { k } ^ { H } ( M Q _ { k } ) \in \mathbb { R } ^ { k \times k } .
$$

2. Compute the Ritz values (the eigenvalues of $H _ { k }$ ） and select from them $p \leq k$ desired approximate eigenvalues $\theta _ { i }$ ， $i = 1 , \ldots , p$ ，Then compute the corresponding eigenvectors $z _ { i }$ ：

$$
H _ { k } z _ { i } = \theta _ { i } z _ { i } , \quad i = 1 , \ldots , p .
$$

3. Compute the Ritz vectors $y _ { i } = Q _ { k } z _ { i }$ $i = 1 , \ldots , p ,$ which are approximate eigenvectors of $M$

Backward error bounds for the approximate eigenvalues $\theta _ { i }$ ， $i = 1 : p$ ,are obtained from the residuals

$$
r _ { i } = M y _ { i } - y _ { i } \theta _ { i } = ( M Q _ { k } ) z _ { i } - y _ { i } \theta _ { i } , \quad i = 1 { : } p .
$$

The Ritz value $\theta _ { i }$ is an exact eigenvalue for a matrix $M + E _ { i }$ ，with $\| E _ { i } \| _ { 2 } ~ \leq ~ \| r _ { i } \| _ { 2 }$ .The corresponding forward error bound is $| \theta _ { i } - \lambda _ { i } | \leq \| r _ { i } \| _ { 2 }$ .The Rayleigh-Ritz procedure is optimal in the sense that the residual norm $\| M Q _ { k } - Q _ { k } H _ { k } \|$ is minimized for all unitarily invariant norms by taking $H _ { k }$ equal to the matrix Rayleigh quotient (7.3.22).

No bound for the error in a Ritz vector $y _ { i }$ can be given without more information. This is to be expected, because if another eigenvalue is close to the Ritz value,the eigenvector is very sensitive to perturbations. If the Ritz value $\theta _ { i }$ is known to be well separated from other eigenvalues of $M$ except the closest one,then a bound on the error in the Ritz vector and also an improved error bound for the Ritz value $y _ { i }$ can be obtained. If $\lambda _ { i }$ is the eigenvalue of $M$ closest to $\theta _ { i }$ ,then

$$
| \theta _ { i } - \lambda _ { i } | \leq \| r _ { i } \| _ { 2 } ^ { 2 } / { \operatorname { g a p } \left( \theta _ { i } \right) } , \qquad \mathrm { g a p } \left( \theta _ { i } \right) = \operatorname* { m i n } _ { j \neq i } ^ { \mathrm { m i n } } | \lambda _ { j } - \theta _ { i } | .
$$

Furthermore, if $x _ { i }$ is an eigenvector of $M$ associated with $\lambda _ { i }$ , then

$$
\sin \angle ( y _ { i } , x _ { i } ) \leq \| r _ { i } \| _ { 2 } / \{ \arg { ( \theta _ { i } ) } .
$$

When some of the intervals $[ \theta _ { i } - \| r _ { i } \| _ { 2 } , \theta _ { i } + \| r _ { i } \| _ { 2 } ]$ ， $i = 1 , \ldots , k$ ,overlap, we cannot be sure of having an eigenvalue of $M$ in each of these intervals.When the Ritz values are clustered, the following theorem provides useful bounds for individual eigenvalues of $M$

Theorem 7.3.6. Let $M \in \mathbb { C } ^ { n \times n }$ be Hermitian, let $Q _ { k } \in \mathbb { C } ^ { n \times p }$ be any orthonormal matrix, and set

$$
H = Q _ { k } ^ { H } M Q _ { k } , \qquad R = M Q _ { k } - Q _ { k } B .
$$

Then to the eigenvalues $\theta _ { 1 } , \ldots , \theta _ { k }$ of $H$ there correspond eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ of $M$ such that $| \lambda _ { i } - \theta _ { i } | \leq \| R \| _ { 2 }$ ， $i = 1 { : } p$ Furthermore, there are eigenvalues $\lambda _ { i }$ of $M$ such that

$$
\sum _ { i = 1 } ^ { p } ( \lambda _ { i } - \theta _ { i } ) ^ { 2 } \leq 2 \| R \| _ { F } ^ { 2 } .
$$

Proof. See Parlett [884,1998, Sect. 11.5].

Unless the Ritz values are well separated, there is no guarantee that the Ritz vectors are good approximations to an eigenvalue of $M$ .This difficulty arises because $B$ may have spurious eigenvalues bearing no relation to the spectrum of $M$ . This problem can be resolved by using a refined Ritz vector as introduced by Jia [668,2ooo]. This is the solution $y$ to the problem

$$
\operatorname* { m i n } _ { \| y \| _ { 2 } = 1 } \| M y - \theta y \| _ { 2 } , \quad y = Q _ { k } z ,
$$

where $\theta$ is a computed Ritz value. This is equivalent to

$$
\operatorname* { m i n } _ { z } \| ( M Q _ { k } - \theta Q _ { k } ) z \| _ { 2 } \ \mathrm { s u b j e c t } \ \mathrm { t o } \ \| z \| _ { 2 } = 1 .
$$

The solution is given by a right singular vector $z$ corresponding to the smallest singular value of $M Q _ { k } - \theta Q _ { k }$ . Since $M Q _ { k }$ must be formed anyway in the Rayleigh-Ritz procedure,the extra cost is only that of computing the SVD of a matrix of size $n \times k$ . In the Hermitian case the Ritz vectors can be chosen so that $Z = ( z _ { 1 } , \ldots , z _ { k } )$ is unitary and the projected matrix $B$ is Hermitian. Then,for each Ritz value $\theta _ { i }$ there is an eigenvalue $\lambda _ { i }$ of $A$ such that

$$
\lvert \theta _ { i } - \lambda _ { i } \rvert \leq \lVert r _ { i } \rVert _ { 2 } , \quad j = 1 { : } k .
$$

For determining interior and small eigenvalues of $M$ it is more appropriate to use the harmonic Ritz values introduced by Paige,Parlett,and van der Vorst [864,1995]. Given the subspace span $\left( Q _ { k } \right)$ , the harmonic projection method requires that

$$
( M - \theta I ) Q _ { k } z \perp \mathrm { s p a n } ( M Q _ { k } ) .
$$

This is a generalized symmetric eigenvalue problem, and the eigenvalues are the harmonic Ritz values.If the basis matrix $Q _ { k }$ is chosen so that ${ V _ { k } = M Q _ { k } }$ is orthonormal, then (7.3.29) becomes $( M Q _ { k } ) ^ { H } ( M Q _ { k } - \theta Q _ { k } ) z = 0$ , or because $Q _ { k } = M ^ { - 1 } V _ { k }$ ，

$$
( \theta ^ { - 1 } I - V _ { k } ^ { H } M ^ { - 1 } V _ { k } ) z = 0 .
$$

This is a standard eigenvalue problem for $M ^ { - 1 }$

The Lanczos process [715,195o] for reducing a Hermitian matrix $M$ to tridiagonal form (Section 6.2.4) is a natural way to realize the Rayleigh-Ritz procedure on a sequence of Krylov subspaces; see Parlett [884,1998, Chapter 13]. It is a matrix-free algorithm,i.e., it only requires the ability to form matrix-vector products with $M$ ：An implementation（irbleigs） is given by Baglama, Calveti, and Reichel [54, 2oo3]. This can be used to compute a few selected singular values and associated vectors of $A$ by applying it to one of the equivalent Hermitian eigenproblems in (7.3.1) or (7.3.2).

More directly, the GKL bidiagonalization (Section 4.2.3) of a rectangular matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ ， can be used to implement the Rayleigh-Ritz procedure. Starting with a unit vector $v _ { 1 } \in \mathbb { R } ^ { n }$ , this computes $u _ { 1 } = A v _ { 1 } / \| A v _ { 1 } \| _ { 2 } \in \mathbb { R } ^ { m }$ ,and for $i = 1 , 2 , \dots$ ，

$$
\begin{array} { r l } & { \gamma _ { i + 1 } v _ { i + 1 } = A ^ { T } u _ { i } - \rho _ { i } v _ { i } , } \\ & { \rho _ { i + 1 } u _ { i + 1 } = A v _ { i + 1 } - \gamma _ { i + 1 } u _ { i } . } \end{array}
$$

Here $\gamma _ { i + 1 }$ and $\rho _ { i + 1 }$ are nonnegative scalars chosen so that $u _ { i + 1 }$ ， $v _ { i + 1 }$ are unit vectors. With $U _ { k } = ( u _ { 1 } , \ldots , u _ { k } )$ ， $V _ { k } = ( v _ { 1 } , \ldots , v _ { k } )$ , the recurrence relations can be summarized as

$$
A V _ { k } = U _ { k } B _ { k } , \quad \quad A ^ { T } U _ { k } = V _ { k } B _ { k } ^ { T } + \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } ,
$$

where

$$
B _ { k } = \left( \begin{array} { c c c c c c } { \rho _ { 1 } } & { \gamma _ { 2 } } & & & & \\ & { \rho _ { 2 } } & { \gamma _ { 3 } } & & & \\ & & & { \ddots } & { \ddots } & & \\ & & & & { \rho _ { k - 1 } } & { \gamma _ { k } } \\ & & & & & & { \rho _ { k } } \end{array} \right) \in \mathbb { R } ^ { k \times k }
$$

is upper bidiagonal. Note that

$$
\gamma _ { k + 1 } = \| r _ { k + 1 } \| _ { 2 } , \quad r _ { k + 1 } = A ^ { T } u _ { k } - \rho _ { k } v _ { k } .
$$

If $\gamma _ { k + 1 } = 0$ , it follows from (7.3.33) that the singular values of $B _ { k }$ are singular values of $A$ ,and the associated singular vectors can be obtained from the SVD of $B _ { k }$ and $U _ { k }$ and $V _ { k }$

The columns of $U _ { k }$ and $V _ { k }$ form orthonormal bases for the Krylov subspaces $\mathcal { K } _ { k } ( A ^ { T } A , v _ { 1 } )$ and $\mathcal { K } _ { k } ( A A ^ { T } , A v _ { 1 } )$ ,respectively. From (7.3.33) the factorization for the equivalent Hermitian problem (7.3.2) is

$$
\left( \begin{array} { c c } { { 0 } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c c } { { U _ { k } } } & { { 0 } } \\ { { 0 } } & { { V _ { k } } } \end{array} \right) = \left( \begin{array} { c c } { { U _ { k } } } & { { 0 } } \\ { { 0 } } & { { V _ { k } } } \end{array} \right) \left( \begin{array} { c c } { { 0 } } & { { B _ { k } } } \\ { { B _ { k } ^ { T } } } & { { 0 } } \end{array} \right) + \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } } } \end{array} \right) .
$$

To avoid spurious singular values caused by loss of orthogonality in $U _ { k }$ and $V _ { k }$ in floating-point arithmetic,a selective reorthogonalization scheme can be used. As shown by Simon and Zha [996, 2ooo] it may suffice to reorthogonalize either $V _ { k }$ or $U _ { k }$ , with considerable savings in storage and operations.

After $k$ steps of the bidiagonalization process the projected Rayleigh quotient matrix is given by $B _ { k } = U _ { k } ^ { T } A V _ { k }$ . The Rayleigh-Ritz procedure for the Krylov subspaces $\mathcal { K } _ { k } ( A ^ { T } A , v _ { 1 } )$ and $\mathcal { K } _ { k } ( A A ^ { T } , A v _ { 1 } )$ computes the SVD

$$
B _ { k } = P _ { k } \Omega _ { k } Q _ { k } ^ { T } , \quad \Omega = \mathrm { d i a g } ( \omega _ { 1 } , \ldots , \omega _ { k } ) ,
$$

to obtain Ritz values $\omega _ { i }$ and left/right Ritz vectors $\hat { v } _ { i } = V _ { k } Q _ { k } e _ { i }$ and $\hat { u } _ { i } = U _ { k } P _ { k } e _ { i }$ . The largest singular values of $A$ tend to be quite well approximated by $\omega _ { i }$ for $k \ll n$ .Hochstenbach [635, 2004] shows that for nested subspaces the Ritz values approach the largest singular values monotonically from above.

Small singular values are approached irregularly, but harmonic Ritz values converge to the smallest singular values from above.Different extraction methods for singular values and vectors are compared by Hochstenbach [635,2oo4]. His numerical experiments confirm that for extracting large singular values,the standard method works well. For interior or small singular values, harmonic Ritz values perform better. The harmonic Ritz values $\theta _ { i }$ satisfy the generalized eigenproblem

$$
\left( \begin{array} { c c } { { 0 } } & { { B _ { k } } } \\ { { B _ { k } ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { s _ { i } } } \\ { { w _ { i } } } \end{array} \right) = \frac { 1 } { \theta _ { i } } \left( \begin{array} { c c } { { B _ { k } B _ { k } ^ { T } + \gamma _ { k + 1 } ^ { 2 } e _ { k } e _ { k } ^ { T } } } & { { 0 } } \\ { { 0 } } & { { B _ { k } ^ { T } B _ { k } } } \end{array} \right) \left( \begin{array} { c } { { s _ { i } } } \\ { { w _ { i } } } \end{array} \right) ,
$$

where $B _ { k }$ is nonsingular or, equivalently,

$$
\begin{array} { r } { ( B _ { k } B _ { k } ^ { T } + \gamma _ { k + 1 } ^ { 2 } e _ { k } e _ { k } ^ { T } ) s _ { i } = \theta _ { i } ^ { 2 } s _ { i } , \qquad w _ { i } = \theta _ { i } B _ { k } ^ { - 1 } s _ { i } ; } \end{array}
$$

see Jia and Niu 671,2o1o]. This result can also be obtained from similar formulas for the Lanczos method given by Baglama, Calveti,and Reichel [54, 2oo3]. It follows that the harmonic Ritz value $\theta _ { i }$ and Ritz vectors $s _ { i } , w _ { i }$ can be obtained more simply from the singular values and right singular vectors of the lower bidiagonal matrix

$$
\left( \begin{array} { c } { B _ { k } ^ { T } } \\ { \gamma _ { k + 1 } e _ { k } ^ { T } } \end{array} \right) = \left( \begin{array} { c c c c c } { \rho _ { 1 } } & & & & \\ { \gamma _ { 2 } } & { \rho _ { 2 } } & & \\ & { \gamma _ { 3 } } & { \ddots } & & \\ & & { \ddots } & { \rho _ { k - 1 } } & \\ & & & { \gamma _ { k } } & { \rho _ { k } } \\ & & & & { \gamma _ { k + 1 } } \end{array} \right) \in \mathbb { R } ^ { ( k + 1 ) \times k } .
$$

With $\tilde { s } _ { i } = s _ { i } / \lVert s _ { i } \rVert _ { 2 }$ and $\tilde { w } _ { i } = w _ { i } / \| w _ { i } \| _ { 2 }$ , the Ritz vectors are

$$
\begin{array} { r } { \tilde { u } _ { i } = U _ { k } \tilde { s } _ { i } , \qquad \tilde { v } _ { i } = V _ { k } \tilde { w } _ { i } . } \end{array}
$$

To improve convergence and reliability, Jia recommends that the Rayleigh quotient $\rho _ { i } = \tilde { s } _ { i } B _ { k } \tilde { w } _ { i }$ be used as an approximation of $\sigma _ { i }$ rather than $\theta _ { i }$ .

The computed Ritz vectors may exhibit slow and irregular convergence even though the Ritz value has converged. Jia and Niu [671, 2O1o] propose a refined strategy that combines harmonic extraction with the refined projection principle. After using harmonic extraction to compute $\rho _ { i } = \tilde { s } _ { i } B _ { k } \tilde { w } _ { i } ,$ $\tilde { u } _ { i }$ ，and $\tilde { v } _ { i }$ it computes the smallest singular value $\sigma _ { \mathrm { m i n } }$ and the corresponding right singular vector $z _ { i } = ( x _ { i } ^ { T } , y _ { i } ^ { T } ) ^ { T }$ of the matrix

$$
\left( \begin{array} { c c } { { 0 } } & { { B _ { k } } } \\ { { B _ { k } ^ { T } } } & { { 0 } } \\ { { \gamma _ { k } e _ { k } ^ { T } } } & { { 0 } } \end{array} \right) - \rho _ { i } \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { I } } \\ { { 0 } } & { { 0 } } \end{array} \right) .
$$

Then the new left and right approximate singular vectors are taken to be

$$
\hat { u } _ { i } = U _ { k } \tilde { x } _ { i } , \qquad \hat { v } _ { i } = V _ { k } \tilde { y } _ { i } ,
$$

where $\tilde { x } _ { i } = x _ { i } / \| x _ { i } \| _ { 2 }$ and $\tilde { y } _ { i } = y _ { i } / \| y _ { i } \| _ { 2 }$

Because of the storage and arithmetic costs,the number of steps in the bidiagonalization process must be limited. To enhance convergence to the desired part of the SVD spectrum, the process can be restarted with a new initial vector $( A ^ { T } A - \mu I ) v _ { 1 }$ ，where $\mu$ is a shift. The goal of restarting is to replace the initial vector $v _ { 1 } = V _ { k } e _ { 1 }$ with a vector that is as near as possible to a linear combination of the right singular vectors associated with the desired singular values. Given the unique upper bidiagonal decomposition (7.3.31)-(7.3.32), we want to generate a new bidiagonal decomposition corresponding to the starting vector $( A ^ { T } A - \mu ^ { 2 } I ) v _ { 1 }$ . Combining the equations in (7.3.33) and using $\alpha _ { k } = e _ { k } ^ { T } B _ { k }$ gives

$$
( A ^ { T } A ) V _ { k } = V _ { k } ( B _ { k } ^ { T } B _ { k } ) + \rho _ { k } \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } ,
$$

where the matrix $T _ { k } \ = \ B _ { k } ^ { T } B _ { k }$ is symmetric and tridiagonal. Hence, the implicitly restarted Lanczos algorithm by Sorensen [1011, 1992] could be applied to $\hat { T } _ { k } = B _ { k } ^ { T } B _ { k } - \mu ^ { 2 } I$

Bjorck, Grimme,and Van Dooren [145,1994] show that forming $B _ { k } ^ { T } B _ { k }$ can be avoided by applying Golub-Reinsch QRSVD steps to $B _ { k }$ directly; see Section 7.1.4. First,a Givens rotation $\bar { G } _ { l } ^ { ( 1 ) }$ is determined so that

$$
G _ { l } ^ { ( 1 ) } \left( \rho _ { 1 } ^ { 2 } - \mu ^ { 2 } \right) = { \binom { * } { 0 } } .
$$

This creates in $G _ { l } ^ { ( 1 ) } B _ { k } ^ { T }$ anunantednonzeroclementinposion $( 1 , 2 )$ . Next, the bidiagonal fomf $G _ { l } ^ { ( 1 ) } B _ { k } ^ { T }$ isresels $k - 1$

$$
\widehat { B } _ { k } ^ { T } = G _ { l } ^ { ( k ) } \cdot \cdot \cdot G _ { l } ^ { ( 2 ) } G _ { l } ^ { ( 1 ) } B _ { k } ^ { T } G _ { r } ^ { ( 2 ) } \cdot \cdot \cdot G _ { r } ^ { ( k ) } = P _ { k } ^ { T } B _ { k } ^ { T } Q _ { k } .
$$

With $\widehat { U } _ { k } \equiv U _ { k } Q _ { k }$ and $\widehat { V } _ { k } \equiv V _ { k } P _ { k }$ , the bidiagonal relations $A V _ { k } = U _ { k } B _ { k }$ and $A ^ { T } U _ { k } = V _ { k } B _ { k } ^ { T } +$ $\gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T }$ become

$$
A \widehat { V } _ { k } = \widehat { U } _ { k } \widehat { B } _ { k } , \qquad A ^ { T } \widehat { U } _ { k } = \widehat { V } _ { k } \widehat { B } _ { k } ^ { T } + \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } Q _ { k } .
$$

However, the last relation is not a valid relation for the bidiagonalization algorithm because the residual term takes on the invalid form

$$
r _ { k } = \gamma _ { k + 1 } v _ { k + 1 } \left( 0 \quad \cdots \quad 0 \quad q _ { ( k + 1 , k ) } \quad q _ { ( k + 1 , k + 1 ) } \right) ,
$$

where $q _ { ( i , j ) }$ is the $( i , j )$ th element in $Q _ { k }$ . This can be dealt with bysacrificing one step. Equating the first $\left( k - 1 \right)$ columns of the second relation in (7.3.4O), we obtain

$$
\begin{array} { r } { \boldsymbol A ^ { T } \widehat U _ { k - 1 } = \widehat V _ { k - 1 } \widehat B _ { k - 1 } ^ { T } + \widehat r _ { k } \boldsymbol e _ { k } ^ { T } , \quad \widehat r _ { k } = \widehat \gamma _ { k } \boldsymbol v _ { k } + \gamma _ { k + 1 } \boldsymbol q _ { ( k + 1 , k ) } \boldsymbol v _ { k + 1 } . } \end{array}
$$

Similarly, taking the first $k { - } 1$ columns of the first relation in (7.3.40) gives the restarted analogue $A \widehat { V } _ { k - 1 } \stackrel { \cdot } { = } \widehat { U } _ { k - 1 } \stackrel { \cdot } { B } _ { k - 1 }$ . It can be shown that $\widehat { U } _ { k - 1 } , \widehat { V } _ { k - 1 }$ ,and $\widehat { B } _ { k - 1 }$ are what would have been obtained after $k - 1$ steps of bidiagonalization with a unit starting vector proportional to

$$
{ \widehat { v } } _ { 1 } = ( A ^ { T } A - \mu ^ { 2 } I ) v _ { 1 } .
$$

It follows that if repeated restarts are performed with $p$ shifts $\mu _ { 1 } , \ldots , \mu _ { p }$ , a bidiagonalization of size $k - p$ corresponding to a unit starting vector proportional to

$$
\hat { v } _ { 1 } = \prod _ { i = 1 } ^ { p } ( A ^ { T } A - \mu _ { i } ^ { 2 } I ) v _ { 1 }
$$

is obtained. An efficient strategy for restarting the Arnoldi or Lanczos process, proposed by Sorensen [1011,1992] and Lehoucq, Sorensen,and Yang [731,1998], is to use unwanted Ritz values as shifts to cause the resulting subspaces to contain more information about the desired singular values.For example,to compute the $p$ largest (smallest) singular triples,the shifts are chosen as the $k - p$ smallest (largest) singular values of $B _ { k }$

The standard implicitly restarted Lanczos tridiagonalization can sufer from numerical instabilities caused by propagated round-off errors； see Lehoucq, Sorensen, and Yang [735,1998]. An alternative is to perform the implicit restarts by augmenting the Krylov subspaces by certain Ritz vectors.This process is mathematically equivalent to standard implicit restarts but is more stable.A description of how to restart the bidiagonalization process by this method is found in Baglama and Reichel [56, 2005].

PROPACK is a software package that uses bidiagonalization to compute selected singular triplets.The initial work on PROPACK is described by Larsen [722,1998]. Later versions include implicit restarts and partial reorthogonalization; see Larsen [723,2ooo]. An overview of PROPACK versions is found at http://soi.stanford.edu/\~rmunk/PROPACK/. The al-gorithm IRLANB of Kokiopoulou, Bekas,and Gallopoulos [703, 2oo4] computes a few of the smallst singular values.It uses an implicitly restarted bidiagonalization process with partial reorthogonalization and harmonic Ritz values. A refinement process is applied to converged singular vectors.Deflation is applied directly on the bidiagonalization process.The implic-itly restarted block-Lanczos algorithm irbleigs of Baglama, Calvetti, and Reichel [55, 2003] computes a few eigenpairs of a Hermitian matrix. It can be used to obtain singular triplets by applying it an equivalent Hermitian eigenproblem. The algorithm irlba of Baglama and Reichel [56,2oo5] is directly based on the bidiagonalization process with standard or harmonic Ritz values. A block bidiagonalization version is given by Baglama and Reichel [57, 2006].

# 7.3.4- Jacobi-Davidson Methods

Let $( \theta _ { k } , y _ { k } )$ be a Ritz pair over a subspace $\mathcal { U } _ { k }$ of dimension $k$ ，approximating an eigenpair of interest of a matrix $A$ . The method of Davidson proposed in [287,1975] is a projection algorithm in which the space $\mathcal { U } _ { k }$ is enlarged until it contains an acceptable approximation to the desired eigenvalue. Let

$$
r _ { k } = A y _ { k } - \theta _ { k } y _ { k }
$$

be the residual of the current Rayleigh-Ritz approximation. Then $\mathcal { U } _ { k }$ is enlarged by a vector determined by the (diagonal) linear system

$$
\begin{array} { r } { ( D - \theta _ { k } I ) v = r _ { k } , ~ D = \mathrm { d i a g } ( A ) . } \end{array}
$$

The new vector $u _ { k + 1 }$ is taken to be the projection of $v$ orthogonal to $\mathcal { U } _ { k }$ . New Rayleigh-Ritz ap-proximations are then computed using the extended subspace $\mathcal { U } _ { k + 1 }$ spanned by $u _ { 1 } , \ldots , u _ { k } , u _ { k + 1 }$ Davidson's method originated in computational chemistry,where it was used to find dominant eigenvalues of large symmetric, diagonally dominant matrices. For this class of problems it frequently works well, but on other problems it can fail completely.

It is tempting to view $D \mathrm { ~ - ~ } \theta _ { k } I$ in （7.3.43） as an approximation to $A \mathrm { ~ - ~ } \theta _ { k } I$ However, attempts to improve the method by using a better approximation willin general not work. This is not surprising, because using the exact inverse $( A - \theta _ { k } I ) ^ { - 1 }$ will map $r _ { k }$ to the vector $y _ { k }$ and will not expand the subspace.

The Jacobi-Davidson method, proposed in 1996 by Sleijpen and van der Vorst [1002,1996], is a great improvement over Davidson's method. In this method the vector $v$ is required to lie in the orthogonal complement of the last Ritz vector $y _ { k }$ . (The idea to restrict the expansion of the current subspace to vectors orthogonal to $y _ { k }$ was used in a method by Jacobi; see [659,1846].) The basic equation for determining the update $v$ now uses the orthogonal projection of $A$ onto the subspace $y _ { k } ^ { \perp }$ . This leads to the equation

$$
( I - y _ { k } y _ { k } ^ { H } ) ( A - \theta _ { k } I ) ( I - y _ { k } y _ { k } ^ { H } ) v = - r _ { k } , \quad v \perp y _ { k } ,
$$

where, as before, $r _ { k } = A y _ { k } - \theta _ { k } y _ { k }$ is the residual of the current Rayleigh-Ritz approximation. If $\theta _ { k }$ is a good approximation to a simple eigenvalue, then $A - \theta _ { k } I$ is almost singular but the projected matrix in (7.3.44) is not.Since $\textit { v } \perp \textit { y } _ { k }$ ，we have $( I - y _ { k } y _ { k } ^ { H } ) v ~ = ~ v$ ，and hence $( I - y _ { k } y _ { k } ^ { H } ) ( A - \theta _ { k } I ) v = - r _ { k }$ . It follows that the update satisfies

$$
v = ( A - \theta _ { k } I ) ^ { - 1 } ( \alpha y _ { k } - r _ { k } ) ,
$$

where $\alpha = y _ { k } ^ { H } ( A - \theta I ) v$ can be determined using the condition $v \perp y _ { k }$ . An approximate solution $\widetilde { v }$ to (7.3.45) orthogonal to $y _ { k }$ can be constructed as follows. Let $M \approx A - \theta _ { k } I$ be an approximation,and take

$$
\widetilde { v } = \alpha M ^ { - 1 } y _ { k } - M ^ { - 1 } r _ { k } ,
$$

where the condition $\widetilde { v } \perp y _ { k }$ gives

$$
\alpha = \frac { y _ { k } ^ { H } M ^ { - 1 } r _ { k } } { y _ { k } ^ { H } M ^ { - 1 } y _ { k } } .
$$

f $M = A - \theta _ { k } I$ ， then (7.3.46) reduces to $v = \alpha ( A - \theta _ { k } I ) ^ { - 1 } y _ { k } - y _ { k }$ . Since $v$ is made orthogonal to $y _ { k }$ ,the last term can be discarded. Hence, this choice is mathematically equivalent to the RQI. Since $( A - \theta _ { k } I ) ^ { - 1 } y _ { k }$ may make a very small angle with $y _ { k }$ , it is not worthwhile to accelerate it further in the manner of Davidson.

Another approach is to use a preconditioned iterative method to solve (7.3.44). Let $M \approx$ $A - \theta _ { k } I$ be a preconditioner, and let

$$
M _ { d } = ( I - y _ { k } y _ { k } ^ { H } ) M ( I - y _ { k } y _ { k } ^ { H } )
$$

be the corresponding projected matrix. Then in each step of the iteration an equation of the form $M _ { d } z = u$ ,where $z , u \perp y _ { k }$ , has to be solved. This can be done as in (7.3.46) by computing

$$
z = \alpha M ^ { - 1 } y _ { k } - M ^ { - 1 } u , \quad \alpha = \frac { y _ { k } ^ { H } M ^ { - 1 } u } { y _ { k } ^ { H } M ^ { - 1 } y _ { k } } .
$$

Here $M ^ { - 1 } y _ { k }$ and $y _ { k } ^ { H } M ^ { - 1 } y _ { k }$ need only be computed in the first iteration step. Only one application of the preconditioner $M$ is needed in later steps.

The Jacobi-Davidson method is among the most effective methods for computing a few interior eigenvalues of a large sparse matrix,particularly when a preconditioner is available or generalized eigenvalue problems are considered. Other methods,such as the“shift-and-invert" variants of Lanczos and Arnoldi,require factorization of the shifted matrix. Moreover, the re-sulting linear systems need to be solved accurately. Therefore,these methods are not well suited to combinations with iterative methods as solvers for the linear systems.In Jacobi-Davidson methods,such expensive factorizations can be avoided. Efcient preconditioned iterative solvers can be used in inner iterations.

The Jacobi-Davidson method was introduced by Sleijpen and van der Vorst [1OO2,1996], [1003,2ooo]. For a survey of variations and applications of this method,see Hochstenbach and Notay [636,2oo6]. Jacobi-Davidson algorithms for the generalized eigenvalue problem are given in Fokkema, Sleijpen,and van der Vorst [415,1998]. Variable preconditioners for eigenproblems are studied by Eldén and Simoncini [381, 2002].

ARPACK is an implementation of the implicitly restarted Arnoldi method. It has become the most successful and best known public domain software package for solving large-scale eigenvalue problems. ARPACK can be used for finding a few eigenvalues and eigenvectors of large symmetric or unsymmetric standard or generalized eigenvalue problems; see the users’ guide of Lehoucq, Sorensen,and Yang [731,1998]. In MATLAB the eigs function is an interface to ARPACK. The block Lanczos code of Grimes,Lewis,and Simon [538,1994l and its updates are often used for structural analysis problems in industrial applications.A selection of other software packages freely available are listed in Sorensen [1O12, 2oo2]. An ARPACK-based iterative method for solving large-scale quadratic problems with a quadratic constraint is developed in Rojas, Santos,and Sorensen [931, 2008].

# Notes and references

Numerical methods for large-scale eigenvalue problems are treated in Saad [958, 2o11], which is a much modified revision of [954,1992]. Bai et al. [61, 2ooo] give surveys and templates for the solution of different eigenvalue problems.

An account of the historical development of the Rayleigh-Ritz method and its relation to variational calculus is given by Gander and Wanner [436, 2o12]. Ritz gave a complete description of his method in [930,1go8]. Lord Rayleigh incorrectly claimed in 1911 that allthe ideas in Ritz's work were present in his earlier paper [914,1899].

Golub,Luk,and Overton [498,1981] develop a block Lanczos method for computing selected singular values and vectors of a matrix. Other Krylov subspace algorithms for computing singular triplets are given by Cullm, Willoughby,and Lake [279,1983]. Codes for partial sin-gular value decompositions of sparse matrices for application to information retrieval problems and seismic tomography are given by Berry [113,1992],[114,1993],[115,1994]. Sleijpen and van der Vorst [1OO2,1996] develop an alternative Jacobi-Davidson algorithm for the partial Her-mitian eigenproblem. A similar algorithm called JDsVD for computing singular triplets is given by Hochstenbach [634,2001].

Traditional inverse iterations use several Rayleigh quotient shifts for each singular value, or just one factorization,and apply bidiagonalization on the shifted and inverted problem. In Ruhe [941,1998] and a series of other papers the Rational Krylov subspace methods are developed, which attempt to combine the virtues of these two approaches. Ruhe iterates with several shifts to build up one basis from which several singular values can be computed.

Oksa, Yamamoto,and Vajtersic [836, 2o22] show the convergence to singular triplets for a two-sided block-Jacobi method with dynamic ordering.

# 7.4 - Matrix Functions and SVD

# 7.4.1 - Basic Definitions

Let $f ( z )$ be a scalar function of a complex variable $z \in \mathbb { C }$ . Suppose the expansion

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }
$$

has radius of convergence $r \in ( 0 , \infty )$ . Then (7.4.1) converges uniformly for any $| z | < r$ and diverges for any $| z | > r$ . In the interior of the circle of convergence,formal operations such as termwise differentiation and integration with respect to $z$ are valid. Consider now the related matrix power series

$$
f ( A ) = \sum _ { k = 0 } ^ { \infty } a _ { k } A ^ { k } .
$$

f $A$ is diagonalizable as $A = X D X ^ { - 1 }$ , then $A ^ { k } = X D ^ { k } X ^ { - 1 }$ . If the spectral radius $\rho ( A ) < r$ the series (7.4.2) converges and defines a matrix function

$$
f ( A ) = X f ( D ) X ^ { - 1 } .
$$

Furthermore, $A f ( A ) = f ( A ) A$ ,i.e., $f ( A )$ commutes with $A$ . An important example of a matrix function is the matrix exponential $e ^ { A }$ . This can be defined by its series expansion

$$
e ^ { A } = I + A + { \frac { 1 } { 2 ! } } A ^ { 2 } + { \frac { 1 } { 3 ! } } A ^ { 3 } + \cdot \cdot \cdot
$$

for any matrix $A \in \mathbb { C } ^ { n \times n }$ . Other examples are the matrix square root and sign functions, which are treated next.

The previous assumption that $A$ is diagonalizable is not necessary. Any matrix $A \in \mathbb { C } ^ { n \times n }$ is similar to a block diagonal matrix with almost diagonal matrices,which reveals its algebraic properties. This is the Jordan canonical form named after the French mathematician Marie Ennemond Camille Jordan (1838-1922).

Theorem 7.4.1 (Jordan Canonical Form). Any matrix $A \ \in \ \mathbb { C } ^ { n \times n }$ is similar to the block diagonal matrix

$$
A = X J X ^ { - 1 } = X \operatorname { d i a g } \left( J _ { m _ { 1 } } ( \lambda _ { 1 } ) , \ldots , J _ { m _ { t } } ( \lambda _ { t } ) \right) X ^ { - 1 } ,
$$

where

$$
J _ { m _ { i } } ( \lambda _ { i } ) = \left( \begin{array} { l l l l } { \lambda _ { i } } & { 1 } & & \\ & { \lambda _ { i } } & { \ddots } & \\ & & { \ddots } & { 1 } \\ & & & { \lambda _ { i } } \end{array} \right) = \lambda _ { i } I + S _ { i } \in \mathbb { C } ^ { m _ { i } \times m _ { i } } , \quad i = 1 : t ,
$$

are Jordan blocks and $S _ { i }$ are shift matrices. The numbers $\begin{array} { r } { m _ { 1 } , \ldots , m _ { t } } \end{array}$ are unique and $\begin{array} { r } { \sum _ { i = 1 } ^ { t } m _ { i } = } \end{array}$ $n$ The form (7.4.4) is called the Jordan canonical form and is unique up to the ordering of the Jordan blocks.

A proof of this fundamental theorem is given in Horn and Johnson [639,1985,Sect. 3.1]. It is quite long and is therefore omitted here. The following result follows from an explicit expression of the powers of a single Jordan block.

Theorem 7.4.2. Let $A$ have the Jordan canonical form (7.4.4). Assume that $f ( \lambda )$ and its first $m _ { k } - 1$ derivatives are defined for $\lambda = \lambda _ { k }$ ， $k = 1 { : } t$ Then the function $f ( A )$ is said to be defined on the spectrum of $A$ ,and

$$
f ( A ) = X \mathrm { d i a g } \Big ( f \big ( J _ { m _ { 1 } } ( \lambda _ { 1 } ) \big ) , \dots , f \big ( J _ { m _ { t } } ( \lambda _ { t } ) \big ) \Big ) X ^ { - 1 } ,
$$

where

$$
\begin{array} { l } { { \displaystyle f ( J _ { m _ { k } } ) = f ( \lambda _ { k } ) I + \sum _ { p = 1 } ^ { m - 1 } \frac { 1 } { p ! } f ^ { ( p ) } ( \lambda _ { k } ) S ^ { p } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = \left( \begin{array} { c c c c } { { f ( \lambda _ { k } ) } } & { { f ^ { \prime } ( \lambda _ { k } ) } } & { { \cdots } } & { { \displaystyle \frac { f ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) } { ( m _ { k } - 1 ) ! } } } \\ { { f ( \lambda _ { k } ) } } & { { \ddots } } & { { \vdots } } \\ { { } } & { { \ddots } } & { { f ^ { \prime } ( \lambda _ { k } ) } } \\ { { } } & { { } } & { { f ( \lambda _ { k } ) } } \end{array} \right) . } } \end{array}
$$

If $f$ is a multivalued function, and a repeated eigenvalue of $A$ occurs in more than one Jordan block, then the same branch of $f$ and its derivatives is usually taken. This choice gives a primary matrix function that is expressible as a polynomial in $A$ . In the following it is assumed that $f ( A )$ is a primary matrix function unless stated otherwise. Then the Jordan canonical form definition (7.4.6) does not depend on the ordering of the Jordan blocks.

There are several equivalent ways to define a function of a matrix. One definition, due to Sylvester (1883), uses polynomial interpolation. Denote by $\lambda _ { 1 } , \ldots , \lambda _ { t }$ the distinct eigenvalues of $A$ ,and let $m _ { k }$ be the index of $\lambda _ { k }$ ,i.e., the order of the largest Jordan block containing $\lambda _ { k }$ Assume that the function is defined on the spectrum $\Lambda ( A )$ of $A$ Then $f ( A ) = p ( A )$ ,where $p$ is the unique Hermite interpolating polynomial of degree less than $\begin{array} { r } { n = \sum _ { k = 1 } ^ { t } m _ { k } } \end{array}$ that satisfies the interpolating conditions

$$
p ^ { ( i ) } ( \lambda _ { k } ) = f ^ { ( j ) } ( \lambda _ { k } ) , \quad j = 0 { : } m _ { k } - 1 , \quad k = 1 { : } t .
$$

Note that the coefficients of the interpolating polynomial depend on $A$ and that $f ( A )$ commutes with $A$ .It is well known that this interpolating polynomial exists and can be computed by Newton's interpolation formula

$$
f ( A ) = f ( \lambda _ { 1 } ) I + \sum _ { j = 1 } ^ { n ^ { * } } f ( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { j } ) ( A - \lambda _ { 1 } I ) \cdots ( A - \lambda _ { j } I ) ,
$$

where $\lambda _ { j }$ ， $j = 1 { : } n ^ { * }$ are the distinct eigenvalues of $A$ ,each counted with the same multiplicity as in the minimal polynomial. Thus, $n ^ { * }$ is the degree of the minimal polynomial of $A$ .Formulas for complex Hermite interpolation are given in Dahlquist and Bjorck [284, 2oo8,Sect. 4.3.2]. The definitions by the Jordan canonical form and polynomial interpolation can be shown to be equivalent. Theory and computation of matrix functions are admirably surveyed in the seminal monograph of Higham [625, 2008].

# 7.4.2- Matrix Square Root and Sign Function

A matrix $X$ is called a square root of $A \in \mathbb { C } ^ { n \times n }$ if it satisfies

$$
X ^ { 2 } = A .
$$

If $A$ has no eigenvalues on the closed negative real axis, then there is a unique principal square root such that $- \pi / 2 < \arg ( \lambda ( X ) ) < \pi / 2$ .The principal square root is denoted by $\bar { A } ^ { 1 / 2 }$ . When it exists,it is a polynomial in $A$ .If $A$ is Hermitian and positive definite,then the principal square root is the unique Hermitian and positive definite square root. If $A$ is real and has a square root, then $A ^ { 1 / 2 }$ is real.

The square root of a matrix may not exist. For example, it is easy to verify that

$$
A = { \left( \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right) }
$$

cannot have a square root. To ensure that a square root exists, it sufces to assume that $A$ has at most one zero eigenvalue. If $A$ is nonsingular and has $s$ distinct eigenvalues,then it has precisely $2 ^ { s }$ square roots that are expressible as polynomials in the matrix $A$

The principal square root of $A$ can be computed directly using only the Schur decomposition $A = Q T Q ^ { H }$ with $T$ upper triangular; see Bjorck and Hammarling [146, 1983]. Then

$$
A ^ { 1 / 2 } = Q S Q ^ { T } , \quad S = T ^ { 1 / 2 } .
$$

From $T = S ^ { 2 }$ we obtain $t _ { i i } = s _ { i i } ^ { 2 }$ and

$$
t _ { i j } = \sum _ { k = i } ^ { j } s _ { i k } s _ { k j } , \quad 1 \leq i < j \leq n .
$$

Starting with Si = t1/2 ， $i = 1 { : } n$ ,the off-diagonal elementsof $S$ can be computed one diagonal at a time from these relations in $n ^ { 3 } / 3$ flops:

$$
s _ { i j } = \Biggl ( t _ { i j } - \sum _ { k = i + 1 } ^ { j - 1 } s _ { i k } s _ { k j } \Biggr ) \Bigl / ( s _ { i i } + s _ { j j } ) , \quad 1 \le i < j \le n .
$$

If $t _ { i i } = t _ { j j }$ we take $s _ { i i } = s _ { j j }$ ， so this recursion does not break down. (Recall that we have assumed that at most one diagonal element of $T$ is zero.） The arithmetic cost of this algorithm is dominated by the $2 5 n ^ { 3 }$ flops required for computing $Q$ and $T$ in the Schur decomposition. When $A$ is a normal matrix $( A ^ { H } A = A A ^ { H }$ ）， $T$ is diagonal. In this case, $S$ is diagonal and the flop count is reduced to $9 n ^ { 3 }$ . A modified algorithm by Higham [611, $\mathrm { 1 9 8 7 } ]$ avoids complex arithmetic for real matrices with some complex eigenvalues by using the real Schur decomposition.

In applications where it is too costly to compute the Schur decomposition, an iterative method can be used. Assume that $A \in \mathbb { C } ^ { n \times n }$ has a principal square root, and let $X _ { k }$ be an approximation t0 $A ^ { 1 / 2 }$ .If $X _ { k + 1 } = X _ { k } + H _ { k }$ ,then

$$
A = ( X _ { k } + H _ { k } ) ^ { 2 } = X _ { k } ^ { 2 } + X _ { k } H _ { k } + H _ { k } X _ { k } + H _ { k } ^ { 2 } .
$$

Ignoring the term $H _ { k } ^ { 2 }$ gives the Newton iteration

$$
X _ { k + 1 } = X _ { k } + H _ { k } , ~ X _ { k } H _ { k } + H _ { k } X _ { k } = A - X _ { k } ^ { 2 } .
$$

To solve for the correction $H _ { k }$ requires solving the Sylvester equation (7.4.13), which is expensive. If the initial approximation $X _ { 0 }$ in (7.4.13) is chosen as a polynomial in $A$ ,e.g., $X _ { 0 } = I$ or $X _ { 0 } = A$ ,then all subsequent iterates $X _ { k }$ commute with $A$ .Then (7.4.13) simplifies to

$$
X _ { k + 1 } = \frac { 1 } { 2 } \big ( X _ { k } + A X _ { k } ^ { - 1 } \big ) ,
$$

which is the matrix version of the well-known scalar iteration $z _ { k + 1 } = ( z _ { k } + a / z _ { k } ) / 2$ for the square root of $a$ .Unfortunately, iteration (7.4.14) is unstable and converges only if $A$ is very wellconditioned. Divergence is caused by rounding errors that make the computed approximation $X _ { k }$ fail to commute with $A$ ; see Higham [610,1986].

Several stable modifications of the simplified Newton iteration (7.4.14) have been suggested; see Iannazzo [653, 20o3]. Denman and Beavers [313,1976] rewrite (7.4.14) as

$$
X _ { k + 1 } = { \frac { 1 } { 2 } } \left( X _ { k } + A ^ { 1 / 2 } X _ { k } ^ { - 1 } A ^ { 1 / 2 } \right) .
$$

With $Y _ { k } = A ^ { - 1 / 2 } X _ { k } A ^ { - 1 / 2 }$ , this gives the coupled iteration: $X _ { 0 } = A , Y _ { 0 } = I ,$

$$
X _ { k + 1 } = { \frac { 1 } { 2 } } \left( X _ { k } + Y _ { k } ^ { - 1 } \right) , \qquad Y _ { k + 1 } = { \frac { 1 } { 2 } } \left( Y _ { k } + X _ { k } ^ { - 1 } \right) .
$$

This iteration is stable with a quadratic rate of convergence, and $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } X _ { k } = A ^ { 1 / 2 } } \end{array}$ ， $\scriptstyle \operatorname* { l i m } _ { k \to \infty } Y _ { k }$ $= A ^ { - 1 / 2 }$ . Another stable modification of Newton's iteration due to Meini [787, 2oo4] can be written: $X _ { 0 } = A$ ， $\begin{array} { r } { H _ { 0 } = \frac 1 2 ( I - A ) } \end{array}$ ，

$$
X _ { k + 1 } = X _ { k } + H _ { k } , \quad H _ { k + 1 } = - { \frac { 1 } { 2 } } { \big ( } H _ { k } X _ { k + 1 } ^ { - 1 } H _ { k } { \big ) } , \quad k = 0 , 1 , 2 , \ldots .
$$

The convergence rate of Meini's iteration is quadratic and can be improved by scaling. Similar Newton methods for computing the $p$ th root of a matrix $A ^ { 1 / p }$ for $p > 2$ can be developed; see Iannazzo [654, 2006].

Newton-type methods need the inverse of $X _ { k }$ or its LU(or Cholesky) factorization in each iteration. Another possibility is to use an inner iteration for computing the needed inverses. The Schulz iteration [976,1933] for computing $A ^ { - 1 }$ is

$$
X _ { 0 } = A , \qquad X _ { k + 1 } = X _ { k } + ( I - A X _ { k } ) X _ { k } , \quad k = 0 , 1 , 2 , \dots .
$$

It can be shown that if $A \in \mathbb { C } ^ { n \times n }$ is nonsingular and if

$$
X _ { 0 } = \alpha _ { 0 } A ^ { T } , \quad 0 < \alpha _ { 0 } < 2 / \| A \| _ { 2 } ^ { 2 } ,
$$

then $\scriptstyle \operatorname* { l i m } _ { k \to \infty } X _ { k } = A ^ { - 1 }$ .Convergence is ultimately quadratic: $E _ { k + 1 } = E _ { k } ^ { 2 }$ ，where $E _ { k } \ =$ $I - A X _ { k }$ . About $2 \log _ { 2 } \kappa _ { 2 } ( A )$ iterations are needed for convergence; see Soderstrom and Stewart[1010,1974]. In general, the Schulz iteration cannot compete with direct methods for dense matrices.However, performing a few steps of the iteration (7.4.17) can be used to improve an approximate inverse.

The sign function is defined by

$$
\mathrm { s i g n } ( z ) = \left\{ { \begin{array} { l l } { - 1 } & { \mathrm { i f ~ } \Re z < 0 , } \\ { + 1 } & { \mathrm { i f ~ } \Re z > 0 } \end{array} } \right.
$$

for all $z \in \mathbb { C }$ not on the imaginary axis. We assume in the following that $A \in \mathbb { C } ^ { n \times n }$ isa matrix with no eigenvalues on the imaginary axis. Its Jordan canonical form can be written $A = X \mathrm { d i a g } ( J _ { + } , J _ { - } ) X ^ { - 1 }$ ，where the eigenvalues of $J _ { + }$ lie in the open right-hand plane and those of $J _ { - }$ lie in the open left-hand plane. Then

$$
S = \operatorname { s i g n } ( A ) = X \left( \begin{array} { c c } { { I _ { k } } } & { { 0 } } \\ { { 0 } } & { { - I _ { n - k } } } \end{array} \right) X ^ { - 1 }
$$

is diagonalizable with eigenvalues equal to $\pm 1$ If $S$ is defined, then $S ^ { 2 } = I$ and hence $S ^ { - 1 } = S$ Furthermore, $S$ commutes with $A$ (so $S A = A S$ ,and if $A$ is real, so is $S$ From (7.4.19) it follows that

$$
A = S N , \quad S = A ( A ^ { 2 } ) ^ { - 1 / 2 } , \quad N = ( A ^ { 2 } ) ^ { 1 / 2 } ,
$$

which is the matrix sign decomposition; see Higham [619,1994]. Note that if $A$ is Hermitian, then $A ^ { 2 } = A ^ { H } A$ ,and the polar and the sign decompositions are the same. The sign decomposition generalizes the scalar identity $\mathrm { s i g n } ( z ) \stackrel { - } { = } z / ( z ^ { 2 } ) ^ { 1 / 2 }$ . It is easy to verify that

$$
\mathrm { s i g n } \left( \begin{array} { c c } { { 0 } } & { { A } } \\ { { I } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { 0 } } & { { A ^ { 1 / 2 } } } \\ { { A ^ { - 1 / 2 } } } & { { 0 } } \end{array} \right) .
$$

If $z$ does not lie on the imaginary axis, then

$$
\mathrm { s i g n } \left( z \right) = z / ( z ^ { 2 } ) ^ { 1 / 2 } = z ( 1 - \xi ) ^ { - 1 / 2 } , \quad \xi = 1 - z ^ { 2 } .
$$

An important property of the sign function of $A$ is that

$$
P _ { - } = \frac { 1 } { 2 } ( I - S ) , \qquad P _ { + } = \frac { 1 } { 2 } ( I + S )
$$

are the spectral projectors onto the invariant subspaces associated with the eigenvalues of $A$ in the left and right half-planes,respectively. That is,if the leading columns of an orthogonal matrix $Q$ span the column space of $P _ { + }$ , then

$$
\begin{array} { r } { Q ^ { H } A Q = \left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) . } \end{array}
$$

It follows that the eigenvalues of $A$ in the right half-plane equal $\Lambda ( A _ { 1 1 } )$ and those in the left half-plane are $ { \Lambda } ( A _ { 2 2 } )$ ． This can be used to design spectral divide-and-conquer algorithms for computing eigenvalue decompositions and other fundamental matrix decompositions via the matrix sign function. The problem is recursively decoupled into two smaller subproblems by using the sign function to compute an invariant subspace for a subset of the spectrum. This type of algorithm can achieve more parallelism and have lower communication costs than other standard eigenvalue algorithms; see Bai and Demmel [6O,1998].

For Hermitian (and real symmetric) matrices $A \in \mathbb { C } ^ { m \times n }$ ， the eigenvalue decomposition can be written $A = V \mathrm { d i a g } \left( \Lambda _ { + } , \Lambda _ { - } \right) V ^ { H }$ , where the diagonal matrices $\Lambda _ { + }$ and $\Lambda _ { - }$ contain the positive and negative eigenvalues, respectively. Then,

$$
A = V \mathrm { d i a g } \left( I _ { k } , - I _ { n - k } \right) V ^ { H } V \mathrm { d i a g } \left( \Lambda _ { + } , | \Lambda _ { - } | \right) \equiv P H ,
$$

where $A = P H$ is the polar decomposition. If the unitary polar factor $P$ is known, then

$$
\boldsymbol { P } + \boldsymbol { I } = \left( \begin{array} { l l } { V _ { 1 } } & { V _ { 2 } } \end{array} \right) \mathrm { d i a g } \left( 2 I _ { k } , \boldsymbol { 0 } \right) \left( \begin{array} { l l } { V _ { 1 } } & { V _ { 2 } } \end{array} \right) ^ { H } = 2 V _ { 1 } \boldsymbol { V } _ { 1 } ^ { H } .
$$

It follows that the symmetric matrix

$$
\begin{array} { r } { C = \frac { 1 } { 2 } ( P + I ) = V _ { 1 } V _ { 1 } ^ { H } } \end{array}
$$

is an orthogonal projector onto the subspace corresponding to the positive eigenvalues of $A$

Nakatsukasa and Higham [822,2o13] develop a technique for computing the eigenvalue decomposition of Hermitian matrices that can be used also for computing the SVD. The first step computes the polar decomposition $A = P H$ ，where $P \in \mathbb { C } ^ { m \times n }$ is unitary( $\langle P ^ { H } P = I )$ and $H \in \mathbb { C } ^ { n \times n }$ is Hermitian positive semidefinite. In the second step the symmetric eigenvalue decomposition $H = V \Sigma V ^ { H }$ is computed. The desired SVD is then

$$
\begin{array} { r } { A = ( P V ) \Sigma V ^ { H } = U \Sigma V ^ { H } . } \end{array}
$$

The matrix sign function can be computed by a scaled version of the Newton iteration for $X ^ { 2 } = I$ ：

$$
X _ { 0 } = A , \quad X _ { k + 1 } = { \frac { 1 } { 2 } } \left( X _ { k } + X _ { k } ^ { - 1 } \right) , \quad k = 0 , 1 , 2 , \ldots .
$$

The corresponding scalar iteration $\lambda _ { k + 1 } = { \left( \lambda _ { k } + \lambda _ { k } ^ { - 1 } \right) } / { 2 }$ is Newton's iteration for the square root of 1. It converges quadratically to 1 if $\Re ( \lambda _ { 0 } ) > 0$ ,and to $- 1$ if $\Re ( \lambda _ { 0 } ) < 0$ The matrix iteration (7.4.25) is globally and quadratically convergent to $\mathrm { s i g n } \left( A \right)$ , provided $A$ has no eigenvalues on the imaginary axis.From the Jordan canonical form it follows that the eigenvalues are decoupled and obey the scalar iteration with $\lambda _ { j } ^ { ( 0 ) } = \lambda _ { j } ( A )$ . Il-conditioning of a matrix $X _ { k }$ can destroy the convergence or cause misconvergence.

Higher order iterative methods for $\mathrm { s i g n } \left( A \right)$ can be derived from matrix analogues of Taylor or Padé approximations of the function $h ( \xi ) = ( 1 - \xi ) ^ { - 1 / 2 }$ . The Padé approximations of a function $f ( z )$ are rational functions

$$
r _ { \ell , m } ( z ) = \frac { P _ { \ell , m } ( z ) } { Q _ { \ell , m } ( z ) } \equiv \frac { \sum _ { j = 0 } ^ { \ell } p _ { j } z ^ { j } } { \sum _ { j = 0 } ^ { m } q _ { j } z ^ { j } } ,
$$

with numerator of degree at most $\ell$ and denominator of degree at most $m$ ,such that

$$
f ( z ) - r _ { \ell , m } ( z ) = R z ^ { \ell + m + 1 } + O ( z ^ { \ell + m + 2 } ) , \quad z \to 0 .
$$

For the function

$$
h ( \xi ) = ( 1 - \xi ) ^ { - 1 / 2 }
$$

these are explicitly known. For $\ell = m - 1$ and $\ell = m$ they are called principal Padé approximations and have the special property that

$$
r _ { \ell , m } = \frac { ( 1 + z ) ^ { p } - ( 1 - z ) ^ { p } } { ( 1 + z ) ^ { p } + ( 1 - z ) ^ { p } } ,
$$

where $p = \ell + m + 1$ .That is, the numerator and denominator are,respectively, the odd and even parts of $( 1 + z ) ^ { p }$ . This makes it easy to write down the corresponding rational approximations. The principal Padé approximations have the following properties； see Kenney and Laub [691, 1991, Theorem 5.3].

Theorem 7.4.3. If $A$ has no purely imaginary eigenvalues, then a Padé approximation with $\ell = m$ or $\ell = m - 1$ gives the rational iteration $X _ { 0 } = A$ ，

$$
X _ { k + 1 } = X _ { k } { \frac { p _ { \ell , m } ( 1 - X _ { k } ^ { 2 } ) } { q _ { \ell , m } ( 1 - X _ { k } ^ { 2 } ) } } , \quad k = 0 , 1 , 2 , \ldots .
$$

This converges to $S = \mathrm { s i g n } \left( A \right)$ ,and

$$
( S - X _ { k } ) ( S + X _ { k } ) ^ { - 1 } = \left[ ( S - A ) ( S + A ) ^ { - 1 } \right] ^ { ( \ell + m + 1 ) ^ { k } } .
$$

In particular, taking $\ell = m = 1$ , we have $( 1 - z ) ^ { 3 } = 1 - 3 z + 3 z ^ { 2 } - z ^ { 3 } , - z p _ { 1 1 } = - z ( 3 + z ^ { 2 } ) ,$ $q _ { 1 1 } = 1 + 3 z ^ { 2 }$ .This gives the iteration

$$
X _ { 0 } = A , \quad X _ { k + 1 } = X _ { k } \left( 3 I + X _ { k } ^ { 2 } \right) \left( I + 3 X _ { k } ^ { 2 } \right) ^ { - 1 } , \quad k = 0 , 1 , 2 , \ldots ,
$$

which is Halley's method for $\mathrm { s i g n } \left( A \right)$ and has cubic convergence rate.

# Notes and references

Early work on spectral dichotomy has been done by Godunov [482,1g86] and Malyshev [769, 1993].Bai,Demmel,and Gu [62,1997] develop an inverse-free spectral divide-and-conquer algorithm for the generalized eigenvalue problem that uses only rank-revealing QR factorization and multiplication. The algorithm of Bai and Demmel 60,1998] is based on the matrix sign function and a scaled Newton iteration. Divide-and-conquer algorithms for Hermitian matrices have been developed in the PRISM project by Zhang, Zha,and Ying [1148, 2oo7]. Nakatsukasa and Freund [821, 2o16] give fast methods for computing the matrix sign function based on optimal rational approximations of very high order due to Zolotarev [1154, $\mathbf { 1 8 7 7 } ]$ ·

# 7.4.3 - Polar Decomposition

Although the factors of the polar decomposition of a matrix $A$ are not matrix functions,the decomposition has strong connections to the matrix square root and sign function.

Theorem 7.4.4 (Polar Decomposition). Suppose $A \in \mathbb { C } ^ { m \times n }$ with $m \geq n$ There exists $a$ matrix $P \in \mathbb { C } ^ { m \times n }$ with orthogonal columns and a unique Hermitian positive semidefinite matrix $H \in \mathbb { C } ^ { n \times n }$ such that

$$
A = P H , \quad P ^ { H } P = I .
$$

The Hermitian polar factor $H$ is unique for any $A$ If $r = { \mathrm { r a n k } } ( A ) = n$ ，then $H$ is positive definite and the polar factor $P$ is uniquely determined.

Proof. Let $A$ have the singular value decomposition

$$
A = U \Sigma V ^ { H } = ( U V ^ { H } ) ( V \Sigma V ^ { H } ) ,
$$

where $U \in \mathbb { R } ^ { m \times n }$ and $V \in \mathbb { R } ^ { n \times n }$ are unitary. Then (7.4.30) holds with

$$
A = P H , \quad P = U V ^ { H } , \quad H = V \Sigma V ^ { H } .
$$

For a square nonsingular matrix, the polar decomposition was first given by Autonne [41, 1902]. The factor $P$ in the polar decomposition is the orthogonal (unitary) matrix closest to $A$

Theorem 7.4.5. Let $A \in \mathbb { C } ^ { m \times n }$ $\mid m \geq n \mid$ ） have the polar decomposition $A = P H$ Then, for any unitarily invariant norm,

$$
\| A - P \| = \operatorname* { m i n } _ { Q ^ { H } Q = I _ { n } } \| A - Q \| .
$$

$I f \operatorname { r a n k } ( A ) = n ;$ ， the minimizer is unique for the Frobenius norm, and

$$
\| A - P \| _ { F } = \Big ( \sum _ { i = 1 } ^ { n } ( 1 - \sigma _ { i } ) ^ { 2 } \Big ) ^ { 1 / 2 } .
$$

Theorem 7.4.5 suggests that computing the polar factor $P$ is the “optimal orthogonalizing” of a given matrix. In contrast to other orthogonalization methods it treats the columns of $A$ symmetrically,i.e.,if the columns of $A$ are permuted, the same $P$ with permuted columns is obtained. In quantum chemistry this orthogonalization method was pioneered by Lowdin [760, 1970] and is called Lowdin orthogonalization； see Bhatia and Mukherjea [117,1986]. Other applications of the polar decomposition arise in aerospace computations, factor analysis, satellite tracking,and the Procrustes problem; see Section 7.4.4.

The Hermitian polar factor $H$ also has a certain optimal property. Let $A \in \mathbb { C } ^ { n \times n }$ be a Hermitian matrix with at least one negative eigenvalue. Consider the problem of finding a perturbation $E$ such that $A + E$ is positive semidefinite.

Theorem 7.4.6. Let $A \in \mathbb { C } ^ { n \times n }$ be Hermitian, $A = P H$ be its polar decomposition, and

$$
B = \frac { 1 } { 2 } ( A + H ) , \quad E = \frac { 1 } { 2 } ( A - H ) .
$$

Then $\| A - B \| _ { 2 } = \| E \| _ { 2 } \leq \| A - X \| _ { 2 }$ for any positive semidefinite Hermitian matrix $X$

Proof. See Higham [610,1986].

The theorem was proved for $m = n$ by Fan and Hoffman [395,1955].For the generalization to $m > n$ , see Higham [625,20o8,Theorem 8.4].

The polar decomposition can be regarded as a generalization of the polar decomposition $z = e ^ { i \theta } | z |$ of a complex number $z$ .Thus

$$
e ^ { i \theta } = z / | z | = z ( | z | ^ { 2 } ) ^ { - 1 / 2 } = z ( 1 - \xi ) ^ { - 1 / 2 } , \quad \xi = 1 - | z | ^ { 2 } .
$$

Expanding $h ( \xi ) = ( 1 - \xi ) ^ { - 1 / 2 }$ in a Taylor series and terminating the series after the term of degree $p$ gives

$$
e ^ { i \theta } = z \left( 1 + { \textstyle { \frac { 1 } { 2 } } } \xi + { \textstyle { \frac { 3 } { 8 } } } \xi ^ { 2 } + \cdot \cdot \cdot + { \binom { - 1 / 2 } { p } } \xi ^ { p } \right) .
$$

This series is convergent for $| \xi | < 1$

A family of iterative methods for computing the unitary polar factor $P$ is derivedbyBjorck and Bowie [138,1971]. By a well-known analogy between matrices and complex numbers, we get

$$
P = A ( A ^ { H } A ) ^ { - 1 / 2 } = A ( I - E ) ^ { - 1 / 2 } , \quad E = I - A ^ { H } A .
$$

The matrix series corresponding to (7.4.34),

$$
P = A \left( 1 + { \textstyle { \frac { 1 } { 2 } } } E + { \textstyle { \frac { 3 } { 8 } } } E ^ { 2 } + \dots + { \binom { - 1 / 2 } { p } } E ^ { p } \right) ,
$$

converges to $P$ if the spectral radius $\rho ( E ) < 1$ . Terminating the expansion after the term of order $p$ gives an iterative method of order $p { + 1 }$ for computing $P$ For $p = 1$ the following simple iteration is obtained: $P _ { 0 } = A$ ，

$$
\begin{array} { r } { P _ { k + 1 } = P _ { k } \big ( I + \frac { 1 } { 2 } E _ { k } \big ) , \quad E _ { k } = I - P _ { k } ^ { H } P _ { k } , \quad k = 0 , 1 , 2 , \dots . } \end{array}
$$

This only uses matrix-matrix products. If $\sigma _ { m a x } ( A ) < \sqrt { 3 }$ ,then $P _ { k }$ converges to $P$ with quadratic rate.In applications where $A$ is already close to an orthogonal matrix, sufficient accuracy will be obtained after just a few iterations.

There are more rapidly converging iterative methods that work even when $A$ is far from orthogonal. Newton's method applied to the equation $P ^ { H } P = I$ yields the iteration

$$
P _ { 0 } = A , \quad P _ { k + 1 } = { \frac { 1 } { 2 } } \bigl ( P _ { k } + P _ { k } ^ { - H } \bigr ) , \quad k = 0 , 1 , 2 , \ldots .
$$

This converges globally to the unitary polar factor $P$ of $A$ with quadratic rate:

$$
\begin{array} { r } { \| P _ { k + 1 } - P \| _ { 2 } \leq \frac { 1 } { 2 } \| P _ { k } \| _ { 2 } \| P _ { k } - P \| _ { 2 } ^ { 2 } ; } \end{array}
$$

see Higham [625,2oo8,Theorem 8.12]. The iteration (7.4.37) cannot be applied to a rectangular matrix $A$ ．This is easily dealt with by first computing the QR factorization $A = Q R$ ， $Q \in \mathbb { R } ^ { m \times n }$ (preferably with column pivoting). Apply the Newton iteration (7.4.37) with initial approximation $P _ { 0 } = R$ to compute the polar factor $P$ of $R$ . Then $Q P$ is the unitary polar factor of $A$

If $A$ is il-conditioned, the convergence of the Newton iteration can be very slow initially. Convergence can be accelerated by taking advantage of the fact that the orthogonal polar factor of the scaled matrix $\gamma A , \gamma \neq 0$ , is the same as for $A$ .The scaled Newton iteration is

$$
\begin{array} { r } { P _ { 0 } = A , \quad P _ { k + 1 } = \frac { 1 } { 2 } \big ( \gamma P _ { k } + \gamma ^ { - 1 } P _ { k } ^ { - H } \big ) , \quad k = 0 , 1 , 2 , \ldots , } \end{array}
$$

where $\gamma _ { k }$ are scale factors. Scale factors that minimize $\lVert P _ { k + 1 } - P \rVert _ { 2 }$ are determined by the condition that $\gamma _ { k } \sigma _ { 1 } ( P _ { k } ) = 1 / ( \gamma _ { k } \sigma _ { n } ( P _ { k } ) )$ ,i.e.,

$$
\begin{array} { r } { \gamma _ { k } = ( \sigma _ { 1 } ( P _ { k } ) \sigma _ { n } ( P _ { k } ) ) ^ { - 1 / 2 } . } \end{array}
$$

Because the singular values of $P _ { k }$ are not known, the cheaply computable approximations $\gamma _ { k } =$ $( \alpha _ { k } / \beta _ { k } ) ^ { - 1 / 2 }$ ,where

$$
\alpha _ { k } = \sqrt { \| P _ { k } \| _ { 1 } \| P _ { k } \| _ { \infty } } , \qquad \beta _ { k } = \sqrt { \| P _ { k } ^ { - 1 } \| _ { 1 } \| P _ { k } ^ { - 1 } \| _ { \infty } } ,
$$

are used instead; see Higham 610,1986]. The resulting iteration converges in at most nine iterations to full IEEE double precision of $1 0 ^ { - 1 6 }$ even for matrices with a condition number as large as $\kappa _ { 2 } ( A ) = 1 0 ^ { 1 6 }$ ； see Higham [625, 2oo8, Section 8.9]. Kielbasinski and Zietak [694, 2003] show that using the suboptimal scale factors

$$
\gamma _ { 0 } = 1 / \sqrt { a b } , \quad \gamma _ { 1 } = \sqrt { \frac { 2 \sqrt { a b } } { a + b } } , \quad \gamma _ { k + 1 } = 1 / \sqrt { \frac { 1 } { 2 } ( \gamma _ { k } + 1 / \gamma _ { k } ) } , \quad k = 1 , 2 , \ldots ,
$$

where $a = \| A ^ { - 1 } \| _ { 2 }$ and $b = \| A \| _ { 2 }$ , works nearly as well.

Iterative methods of higher order for the polar decomposition can be derived from Padé ap-proximations of the hypergeometric function $\bar { h } ( \xi ) = ( 1 - \bar { \xi } ) ^ { - 1 / 2 }$ In particular, Halley’s method becomes $P _ { 0 } = A$ ，

$$
P _ { k + 1 } = P _ { k } \big ( 3 I + P _ { k } ^ { H } P _ { k } \big ) \big ( I + 3 P _ { k } ^ { H } P _ { k } \big ) ^ { - 1 } .
$$

The initial rate of convergence of this iteration is very slow when $\kappa ( A )$ is large. A dynamically weighted Halley (QDWH) algorithm, where $P _ { 0 } = A / \| A \| _ { 2 }$ ，

$$
P _ { k + 1 } = P _ { k } { \left( { a _ { k } I + b _ { k } X _ { k } ^ { H } X _ { k } } \right) } { \left( { I + c _ { k } X _ { k } ^ { H } X _ { k } } \right) } ^ { - 1 } ,
$$

is proposed by Nakatsukasa, Bai,and Gygi [82O, 2o1o]. The singular values of $X _ { k + 1 }$ are given by $\sigma _ { i } ( X _ { k + 1 } ) = g _ { k } ( \sigma _ { i } ( X _ { k } )$ ,where

$$
g _ { k } ( x ) = x \frac { a _ { k } + b _ { k } x ^ { 2 } } { 1 + c _ { k } x ^ { 2 } } .
$$

Ideally, the weighting parameters $a _ { k } , ~ b _ { k }$ ，and $c _ { k }$ should be chosen to maximize $l _ { k + 1 }$ ，where $[ l _ { k + 1 } , 1 ]$ contains all singular values of $X _ { k + 1 }$ . A suboptimal choice makes the function $g _ { k }$ satisfy the bounds $0 < g _ { k } ( x ) \ll 1$ for $x \in [ l _ { k } , 1 ]$ and attain the max-min

$$
\operatorname* { m a x } _ { a _ { k } , b _ { k } , c _ { k } } { \Big \{ } \operatorname* { m i n } _ { [ l _ { k } , 1 ] } g _ { k } ( x ) { \Big \} } .
$$

The solution of this optimization problem is given in Appendix A of [820].

An inverse-free implementation of the QDWH iteration can be obtained by first rewriting it as

$$
X _ { k + 1 } = \frac { b _ { k } } { c _ { k } } X _ { k } + \left( a _ { k } - \frac { b _ { k } } { c _ { k } } \right) X _ { k } \big ( I + c _ { k } X _ { k } ^ { H } X _ { k } \big ) ^ { - 1 } .
$$

From the QR factorization

$$
\binom { \sqrt { c _ { k } } X _ { k } } { I } = \binom { Q _ { 1 } } { Q _ { 2 } } R ,
$$

we have $( I + c _ { k } X _ { k } ^ { H } X _ { k } ) = R ^ { H } R$ 、Examining the blocks of the QR factorization, we see that $I = Q _ { 1 } R$ and ${ \sqrt { c _ { k } } } X _ { k } = Q _ { 1 } R$ . Hence the matrix in the second term of (7.4.41) can be computed as

$$
X _ { k } \big ( I + c _ { k } X _ { k } ^ { H } X _ { k } \big ) ^ { - 1 } = Q _ { 1 } R R ^ { - 1 } R ^ { - H } = Q _ { 1 } Q _ { 2 } ^ { H } .
$$

The QDWH method has the advantage that it requires at most six iterations for convergence to the unitary polar factor of $A$ to full IEEE double precision $1 0 ^ { - 1 6 }$ for any matrix with $\kappa ( A ) \leq 1 0 ^ { 1 6 }$ .A proof of the backward stability of the QDWH method is given by Nakatsukasa and Higham [822, 2013].

The sensitivity of the factors in the polar decomposition to perturbations in $A$ has been studied by Barrlund [83,199o] and Chaitin-Chatelin and Gratton [216, 2ooo]. The absolute condition number in the Frobenius norm for the orthogonal factor $P$ is $1 / \sigma _ { n } ( A )$ .If $A$ is real and $m = n$ ， this can be improved to

$$
2 / ( \sigma _ { n } ( A ) + \sigma _ { n - 1 } ( A ) ) .
$$

For the Hermitian factor $H$ ,an upper bound on the condition number is $\sqrt { 2 }$

# 7.4.4 - The Procrustes Problem

Given $A$ and $B$ in $\mathbb { R } ^ { m \times n }$ ,the orthogonal Procrustes problem is10

$$
\operatorname* { m i n } _ { Q ^ { T } Q = I } \| A - B Q \| _ { F } .
$$

The solution to this problem can be computed from the polar decomposition of $B ^ { T } A$ ,as shown by the following generalization of Theorem 7.4.5.

Theorem 7.4.7 (Schonemann [973,1966]). Let $\mathcal { M } _ { m \times n }$ be the set of all matrices in $\mathbb { R } ^ { m \times n }$ ， $m \geq n$ ,with orthogonal columns. Let $A$ and $B$ be given matrices in $\mathbb { R } ^ { m \times n }$ such that1 $\operatorname { \dot { \mathrm { { a n k } } } } ( B ^ { T } A ) =$ $n$ .Then

$$
\lVert A - B Q \rVert _ { F } \geq \lVert A - B P \rVert _ { F }
$$

for any matrix $Q \in \mathcal { M } _ { m \times n }$ ，where $B ^ { T } A = P H$ is the polar decomposition.

Proof. From $\| A \| _ { F } ^ { 2 } = \operatorname { t r a c e } \left( A ^ { T } A \right)$ and trace $( X ^ { T } Y ) = \operatorname { t r a c e } \left( Y X ^ { T } \right)$ and the orthogonality of $Q$ , it follows that

$$
\| A - B Q \| _ { F } ^ { 2 } = \operatorname { t r a c e } \left( A ^ { T } A \right) + \operatorname { t r a c e } \left( B ^ { T } B \right) - 2 \operatorname { t r a c e } \left( Q ^ { T } B ^ { T } A \right) .
$$

It follows that problem (7.4.42) is equivalent to maximizing trace $( Q ^ { T } B ^ { T } A )$ . From the SVD $B ^ { T } A = U \Sigma V ^ { T }$ ,set $Q = U Z V ^ { T }$ with $Z$ orthogonal. Then $\| Z \| _ { 2 } = 1$ ,and the diagonal elements of $Z$ must satisfy $| z _ { i i } | \leq 1$ ， $i = 1 { : } n$ . Hence,

$$
\begin{array} { c } { \displaystyle \mathrm { t r a c e } \left( Q ^ { T } B ^ { T } A \right) = \mathrm { t r a c e } \left( V Z ^ { T } U ^ { T } B ^ { T } A \right) = \mathrm { t r a c e } \left( Z ^ { T } U ^ { T } B ^ { T } A V \right) } \\ { \displaystyle = \mathrm { t r a c e } \left( Z ^ { T } \Sigma \right) = \displaystyle \sum _ { i = 1 } ^ { n } z _ { i i } \sigma _ { i } \leq \displaystyle \sum _ { i = 1 } ^ { n } \sigma _ { i } , } \end{array}
$$

where $\Sigma = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { n } \right)$ .The upper bound is obtained for $Q = U V ^ { T }$ .If $\operatorname { r a n k } ( A ) = n$ ， this solution is unique. □

The orthogonal Procrustes problem arises in factor analysis and multidimensional scaling methods in statistics; see Cox and Cox [276,1994]. In these applications the matrices $A$ and $B$ represent sets of experimental data,and the question is whether these are identical up to a rotation.Another application is in determining rigid body movements.Let $a _ { 1 } , a _ { 2 } , \ldots , a _ { m }$ be measured positions of $m \geq n$ landmarks of a rigid body in $\mathbb { R } ^ { n }$ ，and let $b _ { 1 } , b _ { 2 } , \dots , b _ { m }$ be the measured positions after the body has been rotated. We seek an orthogonal matrix $Q \in \mathbb { R } ^ { n \times n }$ representing the rotation of the body; see Soderkvist and Wedin [1009,1994]. This has important applications in radiostereometric analysis (Soderkvist and Wedin [1008,1993l） and subspace alignment in molecular dynamics simulation of electronic structures.

In many applications it is important that $Q$ correspond to a pure rotation, i.e., $\operatorname* { d e t } ( Q ) = 1$ If $\operatorname* { d e t } ( U V ^ { T } ) = 1$ , the optimal $Q = U V ^ { T }$ as before. Otherwise, if $\operatorname* { d e t } ( U V ^ { T } ) = - 1$ ,the optimal solution can be shown to be (see Hanson and Norris [590,1981])

$$
\begin{array} { r } { Q = U Z V ^ { T } , \quad Z = \operatorname { d i a g } { \left( 1 , \dots , 1 , - 1 \right) } , } \end{array}
$$

with $\operatorname* { d e t } ( Q ) = + 1$ For this choice, $\textstyle \sum _ { i = 1 } ^ { n } z _ { i i } \sigma _ { i } = \operatorname { t r a c e } \left( \Sigma \right) - 2 \sigma _ { n }$ I both cases the optimal solution can be written

$$
\begin{array} { r } { Q = U Z V ^ { T } , \quad Z = \mathrm { d i a g } \left( 1 , \dots , 1 , \mathrm { d e t } ( U V ^ { T } ) \right) . } \end{array}
$$

In the analysis of rigid body movements,a translation vector $c \in \mathbb { R } ^ { n }$ is also involved. We then have the model $A = B Q + e c ^ { T }$ ， $e = ( 1 , 1 , \ldots , 1 ) ^ { T } \in \mathbb { R } ^ { m }$ To estimate $c \in \mathbb { R } ^ { n }$ we solve the problem

$$
\operatorname* { m i n } _ { Q , c } \| A - B Q - e c ^ { T } \| _ { F } \quad \mathrm { s u b j e c t } \ \mathrm { t o } \quad Q ^ { T } Q = I , \quad \operatorname * { d e t } ( Q ) = 1 .
$$

For any $Q$ , including the optimal $Q$ not yet known, the best least squares estimate of $c$ is characterized by the condition that the residual be orthogonal to $e$ . Multiplying by $e ^ { T }$ we obtain

$$
0 = e ^ { T } ( A - B Q - e c ^ { T } ) = e ^ { T } A - ( e ^ { T } B ) Q - m c ^ { T } = 0 ,
$$

where $e ^ { T } A / m$ and $e ^ { T } B / m$ are the mean values of the rows in $A$ and $B$ . Hence the optimal translation is

$$
\boldsymbol { c } = \frac { 1 } { m } ( ( B ^ { T } \boldsymbol { e } ) \boldsymbol { Q } - \boldsymbol { A } ^ { T } \boldsymbol { e } ) .
$$

Substituting into (7.4.43) gives the problem $\operatorname* { m i n } _ { Q } \| \widetilde { A } - \widetilde { B } Q \| _ { F }$ ,where

$$
\widetilde { A } = A - \frac { 1 } { m } e ( e ^ { T } A ) , \qquad \widetilde { B } = B - \frac { 1 } { m } e ( e ^ { T } B ) ,
$$

which is a standard orthogonal Procrustes problem.

A perturbation analysis of the orthogonal Procrustes problem is given by Soderkvist [1007, 1993]. If $A \in \mathbb { R } ^ { m \times n }$ ， $\boldsymbol { B } \in \mathbb { R } ^ { m \times l }$ ， $m > l$ , in (7.4.42),then the Procrustes problem is called unbalanced. In this case, $Q \in \mathbb { R } ^ { m \times l }$ is rectangular with orthonormal columns and no longer satisfies trace $( Q ^ { T } A ^ { T } A Q ) = \operatorname { t r a c e } \left( A ^ { T } A \right)$ . Algorithms for this more diffcult problem are given by Park [879,1991] and Elden and Park [379,1999]. Several other generalizations are treated in the monograph by Gower and Dijksterhuis [521, 2004].

Chapter 8

# Nonlinear Least Squares Problems

Anyone who deals with nonlinear problems knows that everything works sometimes and nothing works every time.   
John E.Dennis, Jr.

# 8.1 - Newton-Type Methods

# 8.1.1 - Vector Space Calculus

Consider a function $f \colon X \ \to \ Y$ ，where $X$ and $Y$ are normed vector spaces. The function is continuous at the point $x _ { 0 } \in X$ if $\| f ( x ) - f ( x _ { 0 } ) \| \to 0$ as $x  x _ { 0 }$ . It satisfies a Lipschitz condition in a domain $D \subset X$ if a constant $\alpha$ ,called a Lipschitz constant, can be chosen so that

$$
\| f ( x ) - f ( y ) \| \leq \alpha \| x - y \|
$$

for all points $x$ ， $y \in D$ . The function $f$ is differentiable at $x _ { 0 }$ , in the sense of Fréchet,if there exists a linear mapping $A$ such that

$$
\| f ( x ) - f ( x _ { 0 } ) - A ( x - x _ { 0 } ) \| = o ( \| x - x _ { 0 } \| ) , \quad x \to x _ { 0 } .
$$

This linear mapping is called the Fréchet derivative of $f$ at $x _ { 0 }$ ， and we write $A = f ( x _ { 0 } )$ or $A = f _ { x } ( x _ { 0 } )$ . Similar definitions apply to infinite-dimensional spaces.In the finite-dimensional case,the Fréchet derivative is represented by the Jacobian, a matrix whose elements are the partial derivatives $\partial f ^ { i } / \partial x _ { j }$ .If vector-matrix notation is used, it is important to note that the derivative $g ^ { \prime }$ of a real-valued function $g$ is a row vector, because

$$
g ( x ) = g ( x _ { 0 } ) + g ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + o ( \| x - x _ { 0 } \| ) .
$$

The transpose of $g ^ { \prime } ( x )$ is called the gradient,or grad $g$

Many results from elementary calculus carry over to vector space calculus, such as the rules for the differentiation of products. The proofs are in principle the same. If $z = f ( x , y )$ with $\boldsymbol { x } \in \mathbb { R } ^ { k }$ ， $\boldsymbol { y } \in \mathbb { R } ^ { \ell }$ ， $z \in \mathbb { R } ^ { m }$ , then the partial derivatives $f _ { x } = \partial f / \partial x$ ， $f _ { y } = \partial f / \partial y$ with respect to the vectors $x , y$ are defined by the differential formula

$$
d z = f _ { x } d x + f _ { y } d y \quad \forall d x \in \mathbb { R } ^ { k } , \quad d y \in \mathbb { R } ^ { \ell } .
$$

If $x$ and $y$ are functions of $s \in \mathbb { R } ^ { n }$ , then a general version of the chain rule reads

$$
f ^ { \prime } ( x ( s ) , y ( s ) ) = f _ { x } x ^ { \prime } ( s ) + f _ { y } y ^ { \prime } ( s ) ,
$$

where $f ^ { \prime }$ denotes the first derivative. It can be derived in the same way as for real-valued variables,and the extension to longer chains is straightforward.

Let $f \colon \mathbb { R } ^ { k } \ \to \ \mathbb { R } ^ { k } , \ k > \ 1$ ,be a function,and consider the equation $x = f ( y )$ . By formal differentiation, $d x = f ^ { \prime } ( y ) d y$ ，and we obtain $d y = \left( f ^ { \prime } ( y ) \right) ^ { - 1 } d x$ ，provided that the Jacobian matrix $f ^ { \prime } ( y )$ with elements $( \partial x _ { i } / \partial y _ { j } )$ ， $1 \leq i , j \leq k$ ,is nonsingular. If $f ( x , y ) = 0$ ,then by (8.1.2), $f _ { x } d x + f _ { y } d y = 0$ If $f _ { y } ( x _ { 0 } , y _ { 0 } )$ is a nonsingular matrix, then $y$ becomes, under certain additional conditions,a differentiable function of $x$ in a neighborhood of $( x _ { 0 } , y _ { 0 } )$ , and we obtain $d y = - ( f _ { y } ) ^ { - 1 } f _ { x } d x$ ;hence

$$
y ^ { \prime } ( x ) = - ( f _ { y } ) ^ { - 1 } f _ { x } | _ { y = y ( x ) } .
$$

One can also show that

$$
\operatorname* { l i m } _ { \epsilon \to + 0 } { \frac { f ( x _ { 0 } + \epsilon v ) - f ( x _ { 0 } ) } { \epsilon } } = f ^ { \prime } ( x _ { 0 } ) v .
$$

There are,however, functions $f$ for which such a directional derivative exists for any $v$ ,but $f$ is not a linear function of $v$ for some $x _ { 0 }$ . An important example is $f ( x ) = \| x \| _ { \infty }$ ，where $x \in \mathbb { R } ^ { n }$ (Look at the case $n = 2 .$ ）

Consider the set of $k$ -linear mappings from vector spaces $X _ { i } = X$ ， $i = 1 , \ldots , k$ ,which we also write as $X ^ { k }$ ,to $Y$ . This is itself a linear space,which we here denote by $L _ { k } ( X , Y )$ .For $k = 1$ we write it more briefly as $L ( X , Y )$ .If $f ^ { \prime } ( x )$ is a differentiable function of $x$ at the point $x _ { 0 }$ , its derivative is denoted by $f ^ { \prime \prime } ( x _ { 0 } )$ . This is a linear function that maps $X$ into the space $L ( X , Y )$ of mappings from $X$ to $Y$ that contains $f ^ { \prime \prime } ( x _ { 0 } )$ ,i.e., $f ^ { \prime \prime } ( x _ { 0 } ) \in L ( X , L ( X , Y ) )$ . This space may be identified in a natural way with the space $L _ { 2 } ( X , Y )$ of bilinear mappings $X ^ { 2 }  Y$ If $A \in L ( X , L ( X , Y ) )$ , then the corresponding $\bar { A } \in L _ { 2 } ( X , Y )$ is defined by $( A u ) v = \bar { A } ( u , v )$ for all $u , v \in X$ . In the following it is not necessary to distinguish between $A$ and $\bar { A }$ ,S0

$$
f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) \in Y , \qquad f ^ { \prime \prime } ( x _ { 0 } ) u \in L ( X , Y ) , \qquad f ^ { \prime \prime } ( x _ { 0 } ) \in L _ { 2 } ( X , Y ) .
$$

It can be shown that $f ^ { \prime \prime } ( x _ { 0 } )$ ： $X ^ { 2 }  Y$ is a symmetric bilinear mapping, i.e, $f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) =$ $f ^ { \prime \prime } ( x _ { 0 } ) ( v , u )$ . The second-order partial derivatives are denoted $f _ { x x } , f _ { x y } , f _ { y x } , f _ { y y }$ We can show that $f _ { x y } = f _ { y x }$

If $X = \mathbb { R } ^ { n }$ ， $Y = \mathbb { R } ^ { m }$ ， $m > 1$ ，then $f ^ { \prime \prime } ( x _ { 0 } )$ reads $f _ { i j } ^ { p } ( x _ { 0 } ) = f _ { j i } ^ { p } ( x _ { 0 } )$ in tensor notation. It is thus characterized by a three-dimensional array, which one rarely needs to store or write. Fortunately,most of the numerical work can be done on a lower level,e.g.,with directional derivatives.For each fixed value of $p$ ，we obtain a symmetric $n \times n$ matrix $H ( x _ { 0 } )$ called the Hessian matrix; note that $f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) = u ^ { T } H ( x _ { 0 } ) v$ . The Hessian can be looked upon as the derivative of the gradient. An element of the Hessian is, in multilinear mapping notation, the $p$ th coordinate of the vector $f ^ { \prime \prime } ( x _ { 0 } ) ( e _ { i } , e _ { j } )$

Higher derivatives are recursively defined. If $f ^ { ( k - 1 ) } ( x )$ is differentiable at $x _ { 0 }$ , its derivative at $x _ { 0 }$ is denoted by $f ^ { ( k ) } ( x _ { 0 } )$ and called the $k$ th derivative of $f$ at $x _ { 0 }$ . One can show that $f ^ { ( k ) } ( x _ { 0 } ) :$ $X ^ { k }  Y$ is a symmetric $k$ -linear mapping. Taylor's formula then reads,when $a$ ， $u \in X$ ， $f : X \to Y$ ，

$$
\begin{array} { c } { { f ( a + u ) = f ( a ) + f ^ { \prime } ( a ) u + \displaystyle \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) u ^ { 2 } + \cdots + \displaystyle \frac { 1 } { k ! } f ^ { ( k ) } ( a ) u ^ { k } + R _ { k + 1 } , } } \\ { { R _ { k + 1 } = \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \frac { ( 1 - t ) ^ { k } } { k ! } f ^ { ( k + 1 ) } ( a + u t ) d t u ^ { k + 1 } . } } \end{array}
$$

Here we have used $u ^ { 2 } , u ^ { k } , \ldots$ as abbreviations for the lists ofinput vectors $( u , u ) , ( u , u , \dots , u )$ ..., etc. It follows that

$$
\left\| { R _ { k + 1 } } \right\| \le \operatorname* { m a x } _ { 0 \le t \le 1 } \left\| { f ^ { ( k + 1 ) } ( a + u t ) } \right\| \frac { \| u \| ^ { k + 1 } } { ( k + 1 ) ! } ,
$$

where norms of multilinear operators are defined analogously to subordinate matrix norms; see (4.3.37). Such simplifications are often convenient to use.The mean value theorem of differential calculus and Lagrange's form for the remainder of Taylor's formula do not hold,but in many places they can be replaced by the above integral form of the remainder. Allthis holds in complex vector spaces too.

# 8.1.2 - The Gauss-Newton Method

The unconstrained nonlinear least squares (NLS) problem is to find a global minimizer of

$$
\phi ( x ) = \frac 1 2 \sum _ { i = 1 } ^ { m } f _ { i } ^ { 2 } ( x ) = \frac 1 2 f ( x ) ^ { T } f ( x ) , \quad m \ge n ,
$$

where $f ( x ) \in \mathbb { R } ^ { m }$ and $x \in \mathbb { R } ^ { n }$ . Such problems arise, e.g.， when fiting given data $( y _ { i } , t _ { i } )$ ， $i = 1 , \ldots , m$ ，to a nonlinear model function $g ( x , t )$ .If only $y _ { i }$ are subject to errors,and the values $t _ { i }$ of the independent variable $t$ are exact, we take

$$
f _ { i } ( x ) = y _ { i } - g ( x , t _ { i } ) , \quad i = 1 , \ldots , m .
$$

The choice of the least squares measure is justified here,as for the linear case,by statistical considerations; see Bard [66,1974]. The case when there are errors in both $y _ { i }$ and $t _ { i }$ is discussed in Section 8.2.3.

The NLS problem (8.1.4) is a special case of the general unconstrained optimization problem in $\mathbb { R } ^ { n }$ . Although $\phi ( x )$ is bounded below, it is usually convex only near a local minimum. Hence, solution methods willin general not be globally convergent. The methods are iterative in nature. Starting from an initial guess $x _ { 0 }$ ，a sequence of approximations $x _ { 1 } , x _ { 2 } , \dotsc$ is generated that ideally converges to a solution. Each iteration step usually requires the solution of a related linear or quadratic subproblem.

In the following we assume that $f ( x )$ is twice continuously differentiable. Because of the special structure of $\phi ( x )$ in (8.1.4), the gradient $\nabla \phi ( x )$ of $\phi ( x )$ has the special structure

$$
\nabla \phi ( x ) = ( \partial \phi / \partial x _ { 1 } , \ldots , \partial \phi / \partial x _ { n } ) ^ { T } = J ( x ) ^ { T } f ( x ) ,
$$

where $J ( \boldsymbol { x } ) \in \mathbb { R } ^ { m \times n }$ is the Jacobian of $f ( x )$ with elements $( \partial f _ { i } ( x ) / \partial x _ { j } \partial x _ { k } )$ . Furthermore, the Hessian of $\phi ( x )$ is

$$
\nabla ^ { 2 } \phi ( x ) = J ( x ) ^ { T } J ( x ) + G ( x ) , \quad G ( x ) = \sum _ { i = 1 } ^ { m } f _ { i } ( x ) G _ { i } ( x ) ,
$$

where $G _ { i } ( x ) \in \mathbb { R } ^ { n \times n }$ ， $i = 1 , \ldots , n$ , is the Hessian of $f _ { i } ( x )$ , i.e., the symmetric matrix with elements $\left( \partial ^ { 2 } f _ { i } ( x ) / \partial x _ { j } \partial x _ { k } \right)$

A necessary condition for $x ^ { * }$ to be a local minimum of $f ( x )$ is that $\nabla \phi ( x ^ { * } ) = J ( x ^ { * } ) ^ { T } f ( x ^ { * } )$ $= 0$ . Such a point $x ^ { * }$ is called a critical point. Finding a critical point is equivalent to solving the system of nonlinear algebraic equations

$$
F ( x ) \equiv J ( x ) ^ { T } f ( x ) = 0 .
$$

The basic method for solving such a system is Newton's method for nonlinear equations:

$$
F ^ { \prime } ( x _ { k } ) p _ { k } = - F ( x _ { k } ) , \quad x _ { k + 1 } = x _ { k } + p _ { k } .
$$

Newton's method can atain a quadratic rate of convergence and is invariant under a linear transformation of variables $x = S z$ ； see Dennis and Schnabel [316,1996]).With $F ( x )$ given by (8.1.8), $p _ { k }$ solves

$$
\bigl ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + G ( x _ { k } ) \bigr ) p = - J ( x _ { k } ) ^ { T } f ( x _ { k } ) .
$$

The method can also be derived by using a quadratic approximation for the function $\phi ( x ) = $ $\textstyle { \frac { 1 } { 2 } } \parallel f ( x ) \parallel _ { 2 } ^ { 2 }$ and taking $p _ { k }$ as the minimizer of

$$
\phi _ { k } ( x _ { k } + p ) = \phi ( x _ { k } ) + \nabla \phi ( x _ { k } ) ^ { T } p + \frac { 1 } { 2 } p ^ { T } \nabla ^ { 2 } \phi ( x _ { k } ) p .
$$

This is Newton's method for unconstrained optimization. It has several atractive properties. In particular,if the Hessian $\nabla ^ { 2 } f ( x )$ is positive definite at $x _ { k }$ , then $p _ { k }$ is a descent direction for $\phi ( x )$

Newton's method is seldom used for NLS because the $m n ^ { 2 }$ second derivatives in the term $G ( x _ { k } )$ in (8.1.1O) are rarely available at a reasonable cost. An exception is in curve-fitting problems where the function values $f _ { i } ( x ) = y _ { i } - g ( x , t _ { i } )$ and derivatives can be obtained from the single function $g ( x , t )$ . If $g ( x , t )$ is composed of simple exponential and trigonometric functions, for example, then second derivatives can sometimes be computed cheaply.

In the Gauss-Newton method, $f ( x )$ is approximated in a neighborhood of $x _ { k }$ by the linear function $f ( x ) = f ( x _ { k } ) + J ( x _ { k } ) ( x - x _ { k } )$ . Then the condition that $x$ be a critical point can be written

$$
J ( x _ { k } ) ^ { T } ( f ( x _ { k } ) + J ( x _ { k } ) ( x - x _ { k } ) ) = 0 .
$$

The next approximation is taken as $x _ { k + 1 } = x _ { k } + p _ { k }$ ，where $p _ { k }$ solves the linear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| \boldsymbol { f } ( \boldsymbol { x } _ { k } ) + \boldsymbol { J } ( \boldsymbol { x } _ { k } ) \boldsymbol { p } \| _ { 2 } .
$$

f $J ( x _ { k } )$ has full column rank, then $p _ { k }$ is uniquely determined by the condition

$$
J ( x _ { k } ) ^ { T } ( J ( x _ { k } ) p _ { k } + f ( x _ { k } ) ) = 0 .
$$

If $x _ { k }$ is not a critical point, then $p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } )$ is a descent direction. Then,for sufficiently small $\tau > 0 , \| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } < \| f ( x _ { k } ) \| _ { 2 }$ .To verify this, note that

$$
\| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } ^ { 2 } = \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - 2 \alpha \| P _ { J _ { k } } f ( x _ { k } ) \| _ { 2 } ^ { 2 } + { \cal O } ( \alpha ^ { 2 } ) ,
$$

where $P _ { J _ { k } } = J ( x _ { k } ) J ^ { \dagger } ( x _ { k } )$ is the orthogonal projector onto the range of $J ( x _ { k } )$ . Moreover, since $x _ { k }$ is not a critical point, it follows that $P _ { J _ { k } } f ( x _ { k } ) \neq 0$

As the following simple example shows, the Gauss-Newton method may not be locally convergent. Consider minimizing $f _ { 1 } ^ { 2 } ( x ) + f _ { 2 } ^ { 2 } ( x )$ ,where

$$
f _ { 1 } ( x ) = x + 1 , \qquad f _ { 2 } ( x ) = \lambda x ^ { 2 } + x - 1 ,
$$

and $\lambda$ is a parameter. The minimizer is $x ^ { * } = 0$ . The Gauss-Newton method gives $x _ { k + 1 } =$ $\lambda x _ { k } + 0 ( x _ { k } ^ { 2 } )$ . Hence this method diverges when $| \lambda | > 1$ . To ensure global convergence, Newton's method can be used with a line search: $x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k }$ ,where $p _ { k }$ is the Newton step (8.1.10).

The Gauss-Newton method is first-order invariant under a change of parametrization of the least squares problem

$$
\operatorname* { m i n } _ { z \in \mathbb { R } ^ { n } } \frac { 1 } { 2 } \| f ( x ( z ) ) \| _ { 2 } ^ { 2 } ,
$$

where $z$ is a function from $\mathcal { R } ^ { n }$ to $\mathcal { R } ^ { n }$ with a nonsingular Jacobian. To verify this property, note that if $p _ { x } = - J ^ { \dagger } ( x ) f ( x )$ is the Gauss-Newton step in the original variables, then $p _ { z } =$

$( J ( x ) x ^ { \prime } ) ^ { \dagger } f ( x )$ is the step after the change of variables, where $x ^ { \prime }$ is the Jacobian of $x ( z )$ . Then $p _ { x } = x ^ { \prime } p _ { z }$ ,which is the desired relation.

The Gauss-Newton method can also be thought of as arising from neglecting the term $G ( x )$ in Newton's method (8.1.1O). This term is small if the quantities

$$
| f _ { i } ( x _ { k } ) | \| G _ { i } ( x _ { k } ) \| , \quad i = 1 , \ldots , m ,
$$

are small, i.e., if either the residuals $f _ { i } ( x _ { k } )$ ， $i = 1 , \ldots , m$ ，are small or $f _ { i } ( x )$ is only mildly nonlinear at $x _ { k }$ . In this case the behavior of the Gauss-Newton method can be expected to be similar to that of Newton's method.

The Gauss-Newton method can be written as a fixed-point iteration

$$
x _ { k + 1 } = F ( x _ { k } ) , \quad F ( x ) = x - J ( x ) ^ { \dagger } f ( x ) .
$$

Assume there exists an $x ^ { * }$ such that $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ and $J ( x ^ { * } )$ has full column rank. Then

$$
F ( x ) = x - ( J ( x ) ^ { T } J ( x ) ) ^ { - 1 } J ( x ) ^ { T } f ( x ) ,
$$

and using the chain rule gives

$$
\frac { \partial F } { \partial x _ { i } } = I - ( J ^ { T } J ) ^ { - 1 } J ^ { T } \frac { \partial f } { \partial x _ { i } } - ( J ^ { T } J ) ^ { - 1 } \frac { \partial } { \partial x _ { i } } ( J ^ { T } ) f - \frac { \partial } { \partial x _ { i } } ( ( J ^ { T } J ) ^ { - 1 } ) J ^ { T } f ,
$$

$i = 1 , \ldots , n$ Here the second and third terms cancel,and the last term vanishes at $x ^ { * }$ because $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ .We obtain

$$
\nabla F ( x ^ { * } ) = - ( J ( x ^ { * } ) ^ { T } J ( x ^ { * } ) ) ^ { - 1 } \sum _ { i = 1 } ^ { m } f _ { i } ( x ^ { * } ) G _ { i } ( x ^ { * } ) .
$$

Sufficient conditions for local convergence and error bounds for the Gauss-Newton method can be obtained from Ostrowski's fixed-point theorem; see Pereyra [890,1967l, Ortega and Rheinboldt [845,20oo,Theorem 10.1.3],and Dennis and Schnabel [316,1996, Theorem 10.2.1].

Theorem 8.1.1. Let $f ( x )$ be a twice continuously Fréchet differentiable function. Assume there exists $x ^ { * }$ such that $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ and the Jacobian $J ( x ^ { * } )$ has full rank. Then the Gauss-Newton iteration converges locally to $x ^ { * }$ if the spectral radius

$$
\rho = \rho ( \nabla F ( x ^ { * } ) ) < 1 .
$$

The asymptotic convergence is linear with rate bounded by $\rho$ In particular, the local convergence rate is superlinear if $f ( x ^ { * } ) = 0$

Wedin [1107,1972] gives a geometrical interpretation of this convergence result. Minimizing $\begin{array} { r } { \phi ( x ) = \frac { 1 } { 2 } \| f ( x ) \| _ { 2 } ^ { 2 } } \end{array}$ is equivalent to finding a point on the $n$ -dimensional surface $y = f ( x )$ in $\mathbb { R } ^ { m }$ closest to the origin.The normalized vector

$$
w = - f ( x ^ { * } ) / \gamma , \quad \gamma = \| f ( x ^ { * } ) \| _ { 2 } ,
$$

is orthogonal to the tangent plane of the surface $y = f ( x ^ { * } ) + J ( x ^ { * } ) h , h \in$ $\boldsymbol { h } \in \mathbb { R } ^ { n }$ ，at $x ^ { * }$ .The normal curvature matrix of the surface with respect to $w$ is the symmetric matrix

$$
K = ( J ( x ^ { * } ) ^ { \dag } ) ^ { T } G _ { w } ( x ^ { * } ) J ( x ^ { * } ) ^ { \dag } , \quad G _ { w } = \sum _ { i = 1 } ^ { m } w _ { i } G _ { i } ( x ^ { * } ) .
$$

Denote the eigenvalues of $K$ by $\kappa _ { 1 } ~ \geq ~ \kappa _ { 2 } ~ \geq ~ \cdot ~ \cdot ~ \geq ~ \kappa _ { n }$ .The quantities $1 / \kappa _ { i }$ ， $\kappa _ { i } ~ \neq ~ 0$ are the principal radii of curvature of the surface $y = f ( x )$ with respect to the normal $w$ ；see Willmore [1126,1959]. Since

$$
( J ( x ^ { * } ) ^ { T } J ( x ^ { * } ) ) ^ { - 1 } = J ( x ^ { * } ) ^ { \dag } ( J ( x ^ { * } ) ^ { \dag } ) ^ { T } ,
$$

the matrix $\nabla F ( x ^ { * } )$ has the same nonzero eigenvalues as $\gamma K$ ,where $\gamma$ is given as in (8.1.17). It follows that

$$
\rho = \rho ( \nabla F ( { x ^ { * } } ) ) = \gamma \operatorname* { m a x } ( \kappa _ { 1 } , - \kappa _ { n } ) = \gamma \| K \| _ { 2 } .
$$

This relation indicates that the local convergence of the Gauss-Newton method is invariant under a local transformation of the nonlinear least squares problem.

If $J ( x ^ { * } )$ has full column rank, then $\nabla ^ { 2 } f ( x ^ { * } ) = J ^ { T } ( I - \gamma K ) J$ is positive definite. It follows that $x ^ { * }$ is a local minimum of $\phi ( x )$ if and only if $I - \gamma K$ is positive definite at $x ^ { * }$ . This is the case when

$$
1 - \gamma \kappa _ { 1 } > 0
$$

or, equivalently, $\gamma < 1 / \kappa _ { 1 }$ . Furthermore, if $1 - \gamma \kappa _ { 1 } \leq 0$ ，then $\phi ( x )$ has a saddle point at $x ^ { * }$ ； if $1 - \gamma \kappa _ { n } < 0$ ，then $\phi ( x )$ has a local maximum at $x ^ { * }$ .If $x ^ { * }$ is a saddle point, then $\kappa _ { 1 } \geq 1$ Hence using the Gauss-Newton method,one is generally repelled from a saddle point, which is an excellent property.

$$
P _ { J } ( x ) = J ( x ) J ( x ) ^ { \dag } = J ( x ) ( J ( x ) ^ { T } J ( x ) ) ^ { - 1 } J ( x ) ^ { T }
$$

is the orthogonal projection onto the range space of $J ( x )$ . Hence at a critical point $x ^ { * }$ it holds that $P _ { J } ( x ^ { * } ) f ( x ^ { * } ) = 0$ .The rate of convergence for the Gauss-Newton method can be estimated during the iterations from

$$
\| P _ { J } ( x _ { k + 1 } ) f _ { k + 1 } \| _ { 2 } / \| P _ { J } ( x _ { k } ) f _ { k } \| _ { 2 } \leq \rho + O ( \| x _ { k } - x ^ { * } \| _ { 2 } ^ { 2 } ) ,
$$

where $\rho$ is defined as in Theorem 8.1.1. (Recall that $\begin{array} { r } { \operatorname* { l i m } _ { x _ { k } \to x ^ { * } } P _ { J } ( x _ { k } ) f _ { k } = 0 . } \end{array}$ ）Since

$$
P _ { J } ( x _ { k } ) f _ { k } = J ( x _ { k } ) J ( x _ { k } ) ^ { \dagger } f _ { k } = - J ( x _ { k } ) p _ { k } ,
$$

the cost of computing this estimate is only one matrix-vector multiplication. When the estimated $\rho$ is greater than O.5 (say),one should consider switching to a method using second-derivative information.

If the radius of curvature at a critical point satisfies $1 / | \kappa _ { i } | \ll \| f ( x ^ { * } ) \| _ { 2 }$ , the nonlinear least squares problems will be ill-behaved,and many insignificant local minima may exist. Poor performance of Gauss-Newton methods often indicates poor quality of the underlying model or insufficient accuracy in the observed data. Then it would be beter to improve the model rather than use more costly methods of solution.Wedin [1109,1974] shows that the estimate (8.1.21) of the rate of convergence of the Gauss-Newton method is often a good indication of the quality of the underlying model. Deuflhard and Apostolescu [318,198o] call problems for which divergence occurs “inadequate problems.” Many numerical examples leading to poor behavior of Gauss-Newton methods are far from realistic; see Hiebert [6O9,1981] and Fraley $[ 4 3 0 , 1 9 8 9 ]$

As the following simple example shows,the Gauss-Newton method may not even be locally convergent. Consider minimizing $f _ { 1 } ^ { 2 } ( x ) + f _ { 2 } ^ { 2 } ( x )$ ,where

$$
f _ { 1 } ( x ) = x + 1 , \qquad f _ { 2 } ( x ) = \lambda x ^ { 2 } + x - 1 ,
$$

and $\lambda$ is a parameter. The minimizer is $x ^ { * } = 0$ The Gauss-Newton method gives $x _ { k + 1 } =$ $\lambda x _ { k } + 0 ( x _ { k } ^ { 2 } )$ . Hence this method diverges when $| \lambda | > 1$

To ensure global convergence,a useful modification of the Gauss-Newton method is to use a line search in which the next approximation is taken as

$$
x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k } ,
$$

where $\alpha _ { k } > 0$ is a step length to be determined. There are two common algorithms for choosing $\alpha _ { k }$ ; see Ortega and Rheinboldt [845, 2ooo] and Gill, Murray,and Wright [476,1981].

1. Armijo-Goldstein line search, where $\alpha _ { k }$ is taken to be the largest number in the sequence $1 , { \frac { 1 } { 2 } } , { \frac { 1 } { 4 } } , \dotsb$ for which the inequality

$$
\| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } + \alpha _ { k } p _ { k } ) \| _ { 2 } ^ { 2 } \geq { \frac { 1 } { 2 } } \alpha _ { k } \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 }
$$

holds (notice that $- J ( x _ { k } ) p _ { k } = P J _ { k } f ( x _ { k } ) )$

2. “Exact” line search, i.e., taking $\alpha _ { k }$ as the solution to the one-dimensional minimization problem

$$
\operatorname* { m i n } _ { \alpha > 0 } \| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } ^ { 2 } .
$$

Note that a solution $\alpha _ { k }$ may not exist, or there may be a number of local solutions.

A theoretical analysis of the Gauss-Newton method with exact line search has been given by Ruhe [939,1979]. The asymptotic rate of convergence is shown to be

$$
\widetilde { \rho } = \gamma ( \kappa _ { 1 } - \kappa _ { n } ) / ( 2 - \gamma ( \kappa _ { 1 } + \kappa _ { n } ) ) .
$$

A comparison with (8.1.19) shows that $\widetilde { \rho } = \rho$ if $\kappa _ { n } = - \kappa _ { 1 }$ ,and $\widetilde { \rho } < \rho$ otherwise. We also have that $\gamma \kappa _ { 1 } < 1$ implies $\widetilde \rho < 1$ ,i.e.,we always get convergence close to a local minimum. This is in contrast to the Gauss-Newton method, which may fail to converge to a local minimum.

Lindstrom and Wedin [751,1984] develop an alternative line-search algorithm. In this, $\alpha$ is chosen to minimize $\| p _ { k } ( \boldsymbol { \alpha } ) \| _ { 2 }$ , where $p ( \alpha )$ approximates the curve $f ( \alpha ) = f ( x _ { k } + \alpha p _ { k } ) \in \mathbb { R } ^ { m }$ One possibility is to choose $p ( \alpha )$ to be the unique circle (in the degenerate case, a straight line) determined by the conditions

$$
\begin{array} { r } { p _ { k } ( 0 ) = f ( 0 ) , \qquad \nabla p ( 0 ) = \nabla f ( 0 ) , \qquad p _ { k } ( \alpha _ { 0 } ) = f _ { k } ( \alpha _ { 0 } ) , } \end{array}
$$

where $\alpha _ { 0 }$ is a guess of the step length.

Ruhe also develops a way to obtain second-derivative information by using a nonlinear con-jugate gradient acceleration of the Gauss-Newton method with exact line searches. This method achieves quadratic convergence and often gives much faster convergence on difficult problems. When exact line search is used,conjugate gradient acceleration amounts to a negligible amount of extra work. However, for small-residual problems,exact line search is a waste of time,and then a simpler damped Gauss-Newton method is superior.

# 8.1.3 - Regularization and Trust-Region Methods

In practice it often happens that $J ( x )$ is numerically rank-deficient at an intermediate point $x _ { k }$ Then a natural choice is to take $p _ { k }$ as the pseudoinverse solution $p _ { k } = - J ^ { \dagger } ( x _ { k } ) f ( x _ { k } )$ of (8.1.12); see Ben-Israel [99, $1 9 6 7 ]$ ,Fletcher [410,1968],and Boggs [157,1976]． Such a situation is usually complicated by the difficulty in making decisions about the rank.The following example shows that this may be critical. Let

$$
\begin{array} { r } { J = \left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { \epsilon } \end{array} \right) , \qquad f = \left( \begin{array} { l } { f _ { 1 } } \\ { f _ { 2 } } \end{array} \right) , } \end{array}
$$

where $0 < \epsilon \ll 1$ and $f _ { 1 }$ and $f _ { 2 }$ are of order unity. If $J$ is considered to be of rank two,then the search direction is $p _ { k } = s _ { 1 }$ ,whereas if the assigned rank is one, $p _ { k } = s _ { 2 }$ ,where

$$
s _ { 1 } = - \left( { f _ { 1 } \atop f _ { 2 } / \epsilon } \right) , \qquad s _ { 2 } = - \left( { f _ { 1 } \atop 0 } \right) .
$$

Clearly the two directions $s _ { 1 }$ and $s _ { 2 }$ are almost orthogonal, and $s _ { 1 }$ is almost orthogonal to the gradient vector $J ^ { T } f$ . A strategy for estimating the rank of $J ( x _ { k } )$ can be based on QR factorization or SVD of $J ( x _ { k } )$ ； see Section 2.5.Usually an underestimate of the rank is preferable, except when $f ( x )$ is close to an ill-conditioned quadratic function.

An alternative approach that avoids the rank determination is to take $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ is the unique solution to

$$
\operatorname* { m i n } _ { p } \left\| f ( x _ { k } ) + J ( x _ { k } ) p \right\| _ { 2 } ^ { 2 } + \mu _ { k } ^ { 2 } \| p \| _ { 2 } ^ { 2 } ,
$$

and $\mu _ { k } > 0$ is a regularization parameter. Then $p _ { k }$ is defined even when $J _ { k }$ is rank-deficient. This method was first used by Levenberg [736,1944l and later modified by Marquardt [779,1963] and is therefore called the Levenberg-Marquardt method. The solution to problem (8.1.25) satisfies

$$
\left( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + \mu _ { k } ^ { 2 } I \right) p _ { k } = - J ( x _ { k } ) ^ { T } f ( x _ { k } )
$$

or, equivalently,

$$
\operatorname* { m i n } _ { p } \left\| \left( { \boldsymbol { J } } ( { \boldsymbol { x } } _ { k } ) \right) p + \left( { \boldsymbol { f } } ( { \boldsymbol { x } } _ { k } ) \right) \right\| _ { 2 } ,
$$

and can be solved stably by QR factorization (or CGLS or LSQR).

The regularized Gauss-Newton method always takes descent steps. Hence it is localy convergent on almost all nonlinear least squares problems, provided an appropriate line search is carried out. We remark that as $\mu _ { k } \to 0 ^ { + }$ ， $p _ { k } \to J ( x _ { k } ) ^ { \dagger } f _ { k }$ , the pseudoinverse step. For large values of $\mu$ the direction $p _ { k }$ becomes parallel to the steepest descent direction $- J ( x _ { k } ) ^ { T } f _ { k }$ . Hence $p _ { k }$ interpolates between the Gauss-Newton and steepest descent direction. This property makes the Levenberg-Marquardt method preferable to damped Gauss-Newton for many problems.

A useful modification of the Levenberg-Marquardt algorithm is to change the penalty term in (8.1.25) to $\| \mu _ { k } D \| _ { 2 } ^ { 2 }$ ,where $D$ is a diagonal scaling matrix. A frequently used choice is $D ^ { 2 } =$ $\mathrm { d i a g } \left( J ( x _ { 0 } ) ^ { T } J ( x _ { 0 } ) \right)$ . This choice makes the Levenberg-Marquardt algorithm scaling invariant, i.e. it generates the same iterations if applied to $f ( D x )$ for any nonsingular diagonal matrix $D$

From the discussion of problem LSQI in Section 3.5.3, it follows that the regularized least squares problem (8.1.25) is equivalent to the least squares problem with a quadratic constraint,

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } \mathrm { ~ s u b j e c t ~ t o ~ } \| D p \| _ { 2 } \leq \Delta _ { k } ,
$$

for some $\Delta _ { k } > 0$ . If the constraint in (8.1.27) is binding, then $p _ { k }$ is a solution to (8.1.25) for some $\mu _ { k } > 0$ ．The set of feasible vectors $p$ $\| D p \| _ { 2 } \le \Delta _ { k }$ in (8.1.27) can be thought of as a region of trust for the linear model $f ( x ) \approx f ( x _ { k } ) + J ( x _ { k } ) p$ ， $p = x - x _ { k }$ . There has been much research on so-called trust-region methods based on the formulation (8.1.27) as an alternative to a line-search strategy. Combined with a suitable active-set strategy, such a technique can be extended to handle problems with nonlinear inequality constraints; see Lindstrom [749,1983].

Several versions of the Levenberg-Marquardt algorithm have been proved to be globally convergent; see, e.g., Fletcher [411,1971] and Osborne [847,1976]. A general description of scaled trust-region methods for nonlinear optimization is given by Moré [806,1978],[807,1983]. Moré proves that the algorithm will converge to a critical point $x ^ { * }$ if $f ( x )$ is continuously differentiable, $J ( x )$ is uniformly continuous in a neighborhood of $x ^ { * }$ ,and $J ( x _ { k } )$ remains bounded.

# Algorithm 8.1.1 (Trust-Region Method).

Given $x _ { 0 }$ ， $D , \Delta$ and $\beta \in ( 0 , 1 )$ for $k = 0 , 1 , 2 , \ldots$ ，

1. Determine $p _ { k }$ as a solution to the subproblem

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } \| D p \| _ { 2 } \leq \Delta .
$$

2. Compute the ratio between the actual and predicted reduction:

$$
\rho _ { k } = \frac { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } + p _ { k } ) \| _ { 2 } ^ { 2 } } { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } ) + J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } } .
$$

3.If $\rho _ { k } > \beta$ set $x _ { k + 1 } = x _ { k } + p _ { k }$ ; otherwise, set $x _ { k + 1 } = x _ { k }$

4. Update the scaling matrix $D$ and the trust-region radius $\Delta$ $\rho _ { k } \ \ge \ 3 / 4$ ，then $\Delta$ is increased by a factor of 2; if $\rho _ { k } < 1 / 4 \Delta _ { \cdot }$ ，then $\Delta$ is reduced by a factor of 2.

To compute $\rho ( p _ { k } )$ stably in step 2, note that because $p _ { k }$ satisfies (8.1.26), the predicted reduction can be computed from

$$
\begin{array} { r l } & { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } ) + J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } = - 2 p _ { k } ^ { T } J ( x _ { k } ) ^ { T } f ( x _ { k } ) - \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } } \\ & { \qquad = 2 \mu ^ { 2 } \| D p _ { k } \| _ { 2 } ^ { 2 } + \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } . } \end{array}
$$

The ratio $\rho _ { k }$ measures the agreement between the linear model and the nonlinear function. If $J _ { k }$ has full rank, then $\rho _ { k } \to 1$ as $\| p _ { k } \| _ { 2 } \to 0$ .The parameter $\beta$ in step 3 can be chosen quite small, e.g., $\beta = 0 . 0 0 0 1$

Assume that the Jacobian $J ( x )$ is rank-deficient with constant rank $r < n$ in a neighborhood of a local minimum $x ^ { * }$ . Then the appropriate formulation of the problem is

$$
\operatorname* { m i n } _ { x } \| x \| _ { 2 } ^ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } \| f ( x ) \| _ { 2 } ^ { 2 } = \operatorname* { m i n } .
$$

Boggs [157,1976] notes that the choice $p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } )$ gives the least-norm correction to the linearized problem. Instead, $p _ { k }$ should be taken as the least-norm solution to the linearized problem

$$
\operatorname* { m i n } _ { p } \| x _ { k } + p \| _ { 2 } ^ { 2 } \ { \mathrm { s u b j e c t ~ t o } } \ \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } ^ { 2 } = \operatorname* { m i n } .
$$

This has the solution

$$
p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } ) - P _ { \mathit { N } ( J _ { k } ) } x _ { k } ,
$$

where $P _ { \mathcal { N } ( J _ { k } ) } = I - J ( x _ { k } ) ^ { \dagger } J ( x _ { k } )$ is the orthogonal projector onto the nulspace of $J ( x _ { k } )$ Eriksson et al. [388,2oo5] derive necessary and sufficient optimality conditions for the above method. Applying Tikhonov regularization to problem (8.1.28) gives $\begin{array} { r } { \operatorname* { m i n } _ { x } \| f ( x ) \| _ { 2 } ^ { 2 } + \mu ^ { 2 } \| x \| _ { 2 } ^ { 2 } } \end{array}$ or, equivalently,

$$
\operatorname* { m i n } _ { x } \left\| { \binom { f ( x ) } { \mu x } } \right\| _ { 2 } ^ { 2 } .
$$

Linearization of (8.1.31) at $x _ { k }$ gives the subproblem

$$
\operatorname* { m i n } _ { p } \left\| \left( { \boldsymbol { J } } ( { \boldsymbol { x } } _ { k } ) \right) p + \left( { \boldsymbol { f } } ( { \boldsymbol { x } } _ { k } ) \right) \right\| _ { 2 } ^ { 2 } .
$$

For $\mu _ { k } > 0$ thisisafullnkastsapobqesoutio $p _ { k } = p _ { k } ^ { T i k }$ can be computed by QR factorization.

Lemma 8.1.2. The search directions pTi computedntheGuss-Newtonmethodaretedto those in (8.1.30) by

$$
\operatorname* { l i m } _ { \mu _ { k } \to 0 ^ { + } } p _ { k } ^ { \mathrm { T i k } } = p _ { k } .
$$

This result implies that if $\mu _ { k } \to 0 ^ { + }$ , the two Gauss-Newton methods have the same local convergence properties.

# 8.1.4 - Quasi-Newton Methods

Convergence of the Gauss-Newton method and trust-region methods can be slow for largeresidual problems and strongly nonlinear problems. These methods may also have difficulty at points where the Jacobian is rank-deficient. Several methods have been suggested for partially taking the second derivatives into account, either explicitly or implicitly.

In quasi-Newton methods an approximation to the second-derivative matrix is built up successively from evaluations of the gradient. Many of those methods are known to possess superlinear convergence. Let $S _ { k - 1 }$ be a symmetric approximation to the Hessian at step $k$ .The updated $S _ { k }$ is required to approximate the curvature of $f$ along $x _ { k } \mathrm { ~ - ~ } x _ { k - 1 }$ ,i.e., $S _ { k } ( x _ { k } - x _ { k - 1 } ) = y _ { k }$ ， where

$$
y _ { k } = \nabla f ( x _ { k } ) - \nabla f ( x _ { k - 1 } ) = J ( x _ { k } ) ^ { T } f ( x _ { k } ) - J ( x _ { k - 1 } ) ^ { T } f ( x _ { k - 1 } ) .
$$

This is called the quasi-Newton relation. We further require $S _ { k }$ to differ from $S _ { k - 1 }$ by a matrix of small rank. The search direction $p _ { k }$ for the next step is then computed from

$$
S _ { k } p _ { k } = - g ( x _ { k } ) , \qquad g ( x _ { k } ) = J ( x _ { k } ) ^ { T } r ( x _ { k } ) .
$$

As a starting approximation, ${ \cal S } _ { 0 } = J ( x _ { 0 } ) ^ { T } J ( x _ { 0 } )$ is usually recommended.

Ramsin and Wedin [910,1977] gave the following rule for the choice between Gauss-Newton and quasi-Newton methods based on the observed rate (8.1.21) of convergence $\rho$ for the Gauss-Newton method:

1. For $\rho \leq 0 . 5$ ,Gauss-Newton is better.   
2. For globally simple problems,quasi-Newton is better for $\rho > 0 . 5$   
3.For globally difficult problems, Gauss-Newton is much faster for $\rho \leq 0 . 7$ But for larger values of $\rho$ ,quasi-Newton is safer.

This can be used to construct a hybrid method with automatic switching between the two methods.

The application of quasi-Newton methods to the NLS problem as outlined above has not been very efcient in practice. One reason is that often $J ( x _ { k } ) ^ { T } J ( x _ { k } )$ is the dominant part of $\nabla ^ { 2 } f ( x _ { k } )$ , and this information is disregarded. A more successul approach, used by Dennis, Gay,and Welsch [315,198i], is to estimate $\nabla ^ { 2 } f ( x _ { k } )$ by $J ( x _ { k } ) ^ { T } J ( x _ { k } ) + B _ { k }$ ，where $B _ { k }$ isa symmetric quasi-Newton approximation to $B ( x _ { k } )$ . The quasi-Newton relation then becomes

$$
( J _ { k } ^ { T } J _ { k } + B _ { k } ) ( x _ { k } - x _ { k - 1 } ) = y _ { k } ,
$$

but it is preferable to use the alternative formula

$$
B _ { k } ( x _ { k } - x _ { k - 1 } ) = z _ { k } , \quad z _ { k } = ( J ( x _ { k } ) - J ( x _ { k - 1 } ) ) ^ { T } f ( x _ { k } ) .
$$

The solution to (8.1.35) that minimizes $\| B _ { k } - B _ { k - 1 } \| _ { F }$ is given by the rank-two update formula

$$
B _ { k } = B _ { k - 1 } + \frac { w _ { k } z _ { k } ^ { T } + z _ { k } w _ { k } ^ { T } } { z _ { k } ^ { T } s _ { k } } - \frac { w _ { k } ^ { T } s _ { k } z _ { k } z _ { k } ^ { T } } { ( z _ { k } ^ { T } s _ { k } ) ^ { 2 } } ,
$$

where $s _ { k } = x _ { k } - x _ { k - 1 }$ and $w _ { k } = z _ { k } - B _ { k - 1 } s _ { k }$ ; see Dennis and Schnabel [316,1996, pp. $2 3 1 -$ 232]. In some cases the update (8.1.36) gives inadequate results. This motivates the inclusion of a“sizing” in which $B _ { k }$ is replaced by $\tau _ { k } B _ { k }$ ，where $\tau _ { k } = \operatorname* { m i n } \{ | s _ { k } ^ { T } z _ { k } | / | s _ { k } ^ { T } B _ { k } s _ { k } | , 1 \}$ . This heuristic ensures that $S _ { k }$ converges to zero for zero-residual problems,which has been shown to improve the convergence behavior. Note that in the quasi-Newton step, $J _ { k } ^ { T } J _ { k } + B _ { k }$ may need to be modified to be positive so that Cholesky factorization can be used.

The update (8.1.36) is used by the popular subroutine NL2SOL by Dennis, Gay,and Welsch $[ 3 1 5 , 1 9 8 1 ]$ to maintain the approximation $B _ { k }$ and adaptively decide whether to use it or a Gauss-Newton method. In each iteration,NL2SOL computes the reduction predicted by both models and compares it with the observed actual reduction $f ( x _ { k + 1 } ) - f ( x _ { k } )$ . The next step uses the model whose predicted reduction best approximates the actual reduction. Usually this causes NL2SOL to use Gauss-Newton steps until the information in $B _ { k }$ becomes useful. To achieve global convergence, a trust-region strategy is used.

In the quasi-Newton method of Gill and Murray [474,1978], $J ( x _ { k } ) ^ { T } J ( x _ { k } )$ is regarded as a good estimate of the Hessian in the invariant subspace corresponding to the large singular values of $J ( x _ { k } )$ . The second-derivative term $B ( x _ { k } )$ is taken into account only in the complementary subspace.Let the SVD of Jacobian $J = J ( x _ { k } )$ be partitioned as

$$
\begin{array} { r } { J = \left( \begin{array} { c c } { U _ { 1 } } & { U _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { \Sigma _ { 1 } } & { 0 } \\ { 0 } & { \Sigma _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { V _ { 1 } ^ { T } } \\ { V _ { 2 } ^ { T } } \end{array} \right) , } \end{array}
$$

where $\Sigma _ { 1 } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { p } \right)$ contains the large singular values of $J$ and $\Sigma _ { 2 } = \mathrm { d i a g } \left( \sigma _ { p + 1 } , \dots , \right.$ $\sigma _ { n }$ ).Set $B \ : = \ : B ( x _ { k } )$ ,and let $\bar { s }$ denote the first $n$ components of the vector $s = U ^ { T } f ( x _ { k } )$ Equation (8.1.1O) for the Newton direction can then be split into two sets.The first $p$ equations are

$$
( \Sigma _ { 1 } ^ { 2 } + V _ { 1 } ^ { T } B V _ { 1 } ) q _ { 1 } + V _ { 1 } ^ { T } B V _ { 2 } q _ { 2 } = - \Sigma _ { 1 } \bar { s } _ { 1 } .
$$

If the terms involving $B = B _ { k }$ can be neglected compared to $\Sigma _ { 1 } ^ { 2 } q _ { 1 }$ ，we get $q _ { 1 } = - \Sigma _ { 1 } ^ { - 1 } \bar { s } _ { 1 }$ Substituting this into the last $( n - p )$ equations, we obtain

$$
( \Sigma _ { 2 } ^ { 2 } + V _ { 2 } ^ { T } B V _ { 2 } ) q _ { 2 } = - \Sigma _ { 2 } \bar { s } _ { 2 } + V _ { 2 } ^ { T } B V _ { 1 } \Sigma _ { 1 } ^ { - 1 } \bar { s } _ { 1 } .
$$

The approximate Newton direction is taken to be $p _ { k } = V _ { 1 } q _ { 1 } + V _ { 2 } q _ { 2 }$ . The split of the singular values is updated at each iteration,and $p$ is maintained close to $n$ as long as sufficient progress is made.A finite-difference approximation to $V _ { 2 } ^ { T } B _ { k } V _ { 2 }$ is obtained as follows. Let $v _ { j }$ be a column of $V _ { 2 }$ and $h$ be a small positive scalar. Then, by differentiating the gradient along the columns of $V _ { 2 }$ ，

$$
( \nabla f _ { i } ( x _ { k } + h v _ { j } ) - \nabla f _ { i } ( x _ { k } ) ) / h = v _ { j } ^ { T } G _ { i } ( x _ { k } ) + O ( h ) .
$$

The vector on the left-hand side is the $i$ th row of $( J ( x _ { k } + h v _ { j } ) - J ( x _ { k } ) ) / h$ . Multiplying by $f _ { i } ( x _ { k } )$ and adding gives

$$
\begin{array} { r l r } {  { f ( x _ { k } ) ^ { T } ( J ( x _ { k } + h v _ { j } ) - J ( x _ { k } ) ) / h = v _ { j } ^ { T } \sum _ { i = 1 } ^ { m } f _ { i } ( x _ { k } ) G _ { i } ( x _ { k } ) + O ( h ) } } \\ & { } & \\ & { } & { = v _ { j } ^ { T } B _ { k } + O ( h ) , \quad j = p + 1 , \ldots , n . } \end{array}
$$

This gives an approximation for $V _ { 2 } ^ { T } B _ { k }$ , and then $( V _ { 2 } ^ { T } B _ { k } ) V _ { 2 }$ can be formed.

Various other possibilities for hybrid Gauss-Newton/quasi-Newton methods are considered by Al-Baali and Fletcher [14, $\mathbf { 1 9 8 5 } ]$ . They use an approach in which the choice of method and parameters is made by estimating the error in an inverse Hessian approximation.A Newton-like search direction is computed from (8.1.34),where $S _ { k }$ is a symmetric positive definite approximation to the Hessian. This ensures that $p _ { k }$ is a descent direction and makes it possible to use a simpler line-search technique rather than a trust-region approach.

Al-Baali and Fletcher [15,1986] determine $\alpha _ { k }$ to satisfy the conditions

$$
\begin{array} { r l } & { f ( x _ { k } + \alpha _ { k } p _ { k } ) \leq \rho \alpha _ { k } g ( x _ { k } ) ^ { T } p _ { k } , \quad \rho \in ( 0 , 1 / 2 ) , } \\ & { | g ( x _ { k } + \alpha _ { k } p _ { k } ) ^ { T } p _ { k } | \leq - \sigma g ( x _ { k } ) ^ { T } p _ { k } , \quad \sigma \in ( \rho , 1 ) , } \end{array}
$$

and suggest an algorithm to find such a point. Fletcher and $\mathrm { X u }$ [413,1987] develop a hybrid method called HY2 in which a quasi-Newton step is taken when $( f ( x _ { k } ) - f ( x _ { k + 1 } ) ) / f ( x _ { k } ) < \epsilon$ otherwise, a Gauss-Newton step is taken. The quasi-Newton step uses (8.1.36) to update the approximate Hessian but includes a safeguard to maintain positive definiteness. HY2 is superlinearly convergent under mild conditions.A review of quasi-Newton methods for nonlinear least squares is given by Eriksson [387,1999].

Extending the quasi-Newton method to large sparse optimization problems has proved to be difficult. For certain types of large,“partially separable” nonlinear least squares problems,a promising approach is suggested by Toint [1O66,1987]. A typical case is when every function $f _ { i } ( x )$ only depends on a small subset of the set of $n$ variables．Then the Jacobian $J ( x )$ and the element Hessian matrices $G _ { i } ( x )$ are sparse,and it may be possible to store approximations to all $G _ { i } ( x )$ ， $i = 1 , \ldots , m$ ．An implementation is available as the Fortran subroutine VE10 in the Harwell Software Library; see Toint [1O67,1987]. Another subroutine suitable for such problems is LANCELOT by Conn, Gould, and Toint [265,1991], [266,1992].

In a more general setting the solution to nonlinear least squares problems may be subject to nonlinear equality constraints,

$$
\operatorname* { m i n } _ { x } { \frac { 1 } { 2 } } \| f ( x ) \| _ { 2 } ^ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } h ( x ) = 0 ,
$$

where $x \in \mathbb { R } ^ { n } , f ( x ) \in \mathbb { R } ^ { m } , h \in \mathbb { R } ^ { p }$ ,and $p < n$ . The Gauss-Newton method can be generalized to constrained problems by linearization of (8.1.38) at a point $x _ { k }$ ．A search direction $p _ { k }$ is then computed as a solution to the linearly constrained problem

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } \ { \mathrm { s u b j e c t ~ t o } } \ h ( x _ { k } ) + C ( x _ { k } ) p = 0 ,
$$

where $J$ and $C$ are the Jacobians for $f ( x )$ and $h ( x )$ ,respectively. This problem can be solved by the methods described in Section 4.5.The search direction $p _ { k }$ obtained from (8.1.39) can be shown to be a descent direction for the merit function

$$
\psi ( x , \mu ) = \| f ( x ) \| _ { 2 } ^ { 2 } + \mu \| h ( x ) \| _ { 2 } ^ { 2 }
$$

at the point $x _ { k }$ , provided $\mu$ is chosen large enough.

# 8.1.5 - Inexact Gauss-Newton Methods

In large-scale applications, the Gauss-Newton linear subproblems

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| J ( \boldsymbol { x } _ { k } ) \boldsymbol { p } + f ( \boldsymbol { x } _ { k } ) \| _ { 2 }
$$

may be too costly to solve accurately. In any case, far from the solution $x ^ { * }$ , it may not be worth solving these subproblems to high accuracy. To solve (8.1.40) for $p _ { k }$ ,a truncated inner iterative method such as CGLS or LSQR can be applied. A class of inexact Newton methods for solving a system of nonlinear equations $F ( x ) = 0$ is studied by Dembo,Eisenstat,and Steihaug [300, 1982]. A sequence $\{ x _ { k } \}$ of approximations is generated as follows. Given an initial guess $x _ { 0 }$ ， set $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ satisfies

$$
F ^ { \prime } ( x _ { k } ) p _ { k } = - F ( x _ { k } ) + r _ { k } , \quad \frac { \| r _ { k } \| _ { 2 } } { \| F ( x _ { k } ) \| _ { 2 } } \leq \eta _ { k } < 1 .
$$

Here $\{ \eta _ { k } \}$ is a nonnegative forcing sequence used to control the level of accuracy. Taking $\eta _ { k } = 0$ gives the Newton method. Note that the requirement $\eta _ { k } < 1$ is natural because $\eta _ { k } \geq 1$ would allow $p _ { k } = 0$

Theorem 8.1.3 (Dembo,Eisenstat,and Steihaug [300,1982, Theorem 3]). Assume that there exists an $x ^ { * }$ such that $F ( x ^ { * } ) = 0$ with $F ^ { \prime } ( x ^ { * } )$ nonsingular. Let $F$ be continuously differentiable in a neighborhood of $x ^ { * }$ ，and let $\eta _ { k } \ \leq \ \hat { \eta } \ < \ t \ < \ 1 .$ ，Then there exists $\epsilon > 0$ such that if $\| x ^ { * } - x _ { 0 } \| _ { 2 } \leq \epsilon ,$ the sequence $\{ x _ { k } \}$ generated by (8.1.41) converges linearly to $x ^ { * }$ in the sense that

$$
\| x _ { k + 1 } - x _ { k } \| _ { * } \leq t \| x _ { k } - x _ { k } \| _ { * } ,
$$

where the norm is defined by $\| y \| _ { * } \equiv \| F ^ { \prime } ( x ^ { * } ) y \| _ { 2 }$

First,we note that the exact Gauss-Newton method can be considered as an incomplete Newton method for the equation $F ( x ) = J ( x ) ^ { T } f ( x ) = 0$ . This is of the form (8.1.41),where $p _ { k }$ satisfies $J ( x _ { k } ) ^ { T } J ( x _ { k } ) p _ { k } = - J ( x _ { k } ) ^ { T } f ( x _ { k } )$ and

$$
f _ { k } = ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + G ( x _ { k } ) ) p _ { k } + J ( x _ { k } ) ^ { T } f ( x _ { k } ) = G ( x _ { k } ) p _ { k } ,
$$

where $G _ { i } ( x _ { k } )$ is the Hessian of $f _ { i } ( x _ { k } )$ . By Theorem 8.1.3 a sufficient condition for convergence .s that

$$
\begin{array} { r } { \bigg \| G ( x _ { k } ) \big ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) \big ) ^ { - 1 } \bigg \| _ { 2 } = t _ { k } \leq t < 1 . } \end{array}
$$

This is more restrictive than the condition given in Theorem 8.1.1.

A class of inexact Gauss-Newton methods can be defined as follows. Given an initial guess $x _ { 0 }$ ,set $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ satisfies

$$
f _ { k } = J ( \boldsymbol { x } _ { k } ) ^ { T } ( J ( \boldsymbol { x } _ { k } ) \boldsymbol { p } _ { k } + \boldsymbol { f } ( \boldsymbol { x } _ { k } ) ) , \quad \| \boldsymbol { f } _ { k } \| _ { 2 } \leq \beta _ { k } \| J ( \boldsymbol { x } _ { k } ) ^ { T } \boldsymbol { f } ( \boldsymbol { x } _ { k } ) \| _ { 2 } .
$$

The condition on $\| f _ { k } \| _ { 2 }$ is a natural stopping condition on an iterative method for solving the linear subproblem. Gratton,Lawless,and Nichols [526, 2oo7] give conditions on the sequence of tolerances $\{ \beta _ { k } \}$ needed to ensure convergence and investigate the use of such methods for variational data assimilation in meteorology.

Theorem 8.1.4 (Gratton,Lawless,and Nichols [526,2oo7,Theorem 5]). Let $f ( x )$ bea twice continuously Fréchet differentiable function. Assume that there exists an $x ^ { * }$ such that $J ^ { T } ( x ^ { * } ) f ( x ^ { * } ) = 0$ and $J ( x ^ { * } )$ has full column rank. Assume $t _ { k } < \hat { \beta } < 1$ ,where $t _ { k }$ is given as in (8.1.43). Assume $\beta _ { k }$ ， $k = 0 , 1 , \ldots$ , are chosen so that

$$
0 \leq \beta _ { k } \leq ( \hat { \beta } - t _ { k } ) / ( 1 + t _ { k } ) .
$$

Then there exists $\epsilon > 0$ such that if $\| x ^ { * } - x _ { 0 } \| _ { 2 } \leq \epsilon ,$ the sequence $\{ x _ { k } \}$ of the inexact Gauss-Newton method (8.1.44) converges linearly to $x ^ { * }$

Note that the requirement $t _ { k } < \hat { \beta } < 1$ is the sufficient condition for convergence given for the exact Gauss-Newton method. The more highly nonlinear the problem,the larger $t _ { k }$ and the more accurate the linear subproblems to be solved. Accelerated schemes for inexact Newton methods using GMRES for large systems of nonlinear equations are given by Fokkema, Sleijpen,and van der Vorst [414, 1998].

# Notes and references

Dennis [314,1977] gives an early insightful survey of methods for solving nonlinear least squares and equations. Excellent standard references on numerical methods for optimization and systems of nonlinear equations are Dennis and Schnabel [316,1996] and Nocedal and Wright [833, 2006]. Ortega and Rheinboldt [845,2ooo] give a general treatment of theory and algorithms for solving systems of nonlinear equations. General treatments of methods for nonlinear opti-mization problems are given by Gill, Murray,and Wright [476,1981] and Fletcher [412, 2000]. Schwetlick [979,1992] surveys models and algorithms for general nonlinear parameter estimation. Continuation methods are an alternative approach for solving difficult large-residual NLS problems. Salane [962,1987] develops such algorithms and shows they can be competitive with trust-region algorithms.

Methods and software for the NLS problem are described by Wedin and Lindstrom [752, 1988].A useful guide to optimization software is available at the NEOS Guide website. It is constantly updated to reflect new packages and changes to existing software. A trust-region algorithm that has proven to be very successful in practice is included in the $\mathrm { C } { + + }$ software package MINPACK available from netlib. For a user's guide,see Moré, Garbow,and Hillstrom [808, 198o]. See also the PROC NLP Library of the SAS Institute. The Ceres nonlinear least squares solver by Agarwal et al. (see http : //ceres- solver .org) has been used since 2010 by Google for the construction of three-dimensional models in its street-view sensor fusion.

# 8.2 - Separable Least Squares Problems

# 8.2.1 - Variable Projection Method

Suppose we want to solve a nonlinear least squares problem of the form

$$
\operatorname* { m i n } _ { y , z } \| g - \Phi ( z ) y \| _ { 2 } ^ { 2 } , \quad \Phi ( z ) \in \mathbb { R } ^ { m \times p } ,
$$

where $\Phi ( z ) \in \mathbb { R } ^ { m , p }$ ， $y \in \mathbb { R } ^ { p }$ ,and $z \in \mathbb { R } ^ { q }$ are unknown parameters, and $g \in \mathbb { R } ^ { m }$ are given data. For a fixed value of the nonlinear parameter $z$ , problem (8.2.1) is a linear least squares problem in $y$ .Such least squares problems are called separable and arise frequently in applications. One example is when one wants to approximate given data by a linear combination of given nonlinear functions $\phi _ { j } ( z )$ ， $j = 1 , \dotsc , p$

A simple method for solving separable problems is the alternating least squares (ALS) algorithm. Let $z _ { 1 }$ be an initial approximation, and solve the linear problem $\operatorname* { m i n } _ { y } \| g - \Phi ( z _ { 1 } ) y \| _ { 2 }$ to obtain $y _ { 1 }$ . Next, solve the nonlinear problem $\operatorname* { m i n } _ { z } \| g - \Phi ( z ) y _ { 1 } \| _ { 2 }$ to obtain $z _ { 2 }$ .Repeat both steps until convergence. The rate of convergence of ALS is linear and can be very slow. It does not always converge.

For a fixed value of $z$ , the least-norm least squares solution of (8.2.1) can be expressed as

$$
y ( z ) = \Phi ( z ) { } ^ { \dagger } g ,
$$

where $\Phi ^ { \dagger }$ is the pseudoinverse of $\Phi ( z )$ .In the variable projection method of Golub and Pereyra [5O3,1973l, this is used to eliminate the linear parameters $y$ ，giving a reduced nonlinear

least squares problem

$$
\operatorname* { m i n } _ { z } \| g - P _ { \Phi ( z ) } g \| ^ { 2 } , \quad P _ { \Phi ( z ) } = \Phi ( z ) \Phi ( z ) ^ { \dagger } ,
$$

where $P _ { \Phi ( z ) }$ is the orthogonal projector onto the column space of $\Phi ( z )$ . This is a pure nonlinear problem of reduced dimension. An important advantage is that initial values are only needed for the nonlinear parameters $z$

In order to solve (8.2.3) using a Gauss-Newton-Marquardt method,a formula for the gradient of the function $f ( z ) = ( I - P _ { \Phi ( z ) } ) g = P _ { \Phi ( z ) } ^ { \perp } g$ in (8.2.3)is neded.The following lemma giveser $P _ { \Phi ( z ) } ^ { \perp }$ . It must be assumed that the rank of $\Phi ( z )$ is locally constant, because otherwise the pseudoinverse would not be differentiable.

Lemma 8.2.1 (Golub and Pereyra [503,1973,Lemma 4.1]). Let $\Phi ( z ) \in \mathbb { R } ^ { m \times p }$ be a matrix of local constant rank $r$ and $\Phi ^ { \dagger }$ be its pseudoinverse. Denote by $P _ { \Phi } = \Phi \Phi ^ { \dagger }$ the orthogonal projector onto $\mathcal { R } ( \Phi )$ ,and set $P _ { \Phi } ^ { \bot } = 1 - P _ { \Phi }$ . Then, using the product rule for differentiation, we get

$$
\frac { d } { d z } ( P _ { \Phi } ) = - \frac { d } { d z } ( P _ { \Phi } ^ { \perp } ) = P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z } \Phi ^ { \dagger } + \left( P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z } \Phi ^ { \dagger } \right) ^ { T } .
$$

More generally, Golub and Pereyra show that (8.2.4) is valid for any generalized inverse that satisfies $\Phi \Phi ^ { - } \Phi = \Phi$ and $( \Phi \Phi ^ { - } ) ^ { T } = \Phi \Phi ^ { - }$ . Note that the derivative $d \Phi / d z$ in (8.2.4) is a threedimensional tensor with elements $\partial \phi _ { i j } / \partial z _ { k }$ . The transposition in (8.2.4) is done in the $( i , j )$ directions for fixed $k$

In many applications, each component function $\phi _ { j } ( z )$ depends on only a few of the parameters $z _ { 1 } , \ldots , z _ { q }$ . Hence the derivative will often contain many zeros. Golub and Pereyra develop a storage scheme that avoids waste storage and computations. Let $E = ( e _ { i j } )$ be a $q \times p$ incidence matrix such that $e _ { i j } ~ = ~ 1$ if function $\phi _ { j }$ depends on the parameter $z _ { i }$ ，and O otherwise.This incidence matrix can be retrieved from an $m \times p$ array $B$ $\begin{array} { r } { 3 , p = \sum _ { i , j } e ( i , j ) } \end{array}$ ,in which the nonzero derivatives are stored sequentially.

Example 8.2.2. A problem of great importance is the fiting of a linear combination of exponential functions with different time constants,

$$
g ( t ) = y _ { 0 } + \sum _ { j = 1 } ^ { p } y _ { j } e ^ { z _ { j } t } ,
$$

to observations $g _ { i } = g ( t _ { i } ) + \epsilon _ { i }$ ， $i = 0 { : } m$ .Since $g ( t )$ in (8.2.5) depends on $p { + 1 }$ linear parameters $y _ { j }$ and $p$ nonlinear parameters $z _ { j }$ ,at least $m = 2 p + 1$ observations for $t _ { 0 } , \ldots , t _ { m }$ are needed. Clearly this problem is separable,and $\phi _ { i , j } ( z ; t ) \ : = \ : e ^ { z _ { j } t _ { i } }$ ， $j = 1 , \dotsc , p$ .Here the number of nonvanishing derivatives is $p$

The quantities required to solve the reduced nonlinear problem can be expressed in terms of a complete QR decomposition

$$
\Phi = U \left( \begin{array} { c c } { { R } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V ^ { T } , \quad U = \left( U _ { 1 } \quad U _ { 2 } \right) ,
$$

where $R \in \mathbb { R } ^ { r \times r }$ $( r = \mathrm { r a n k } ( \Phi ) )$ is upper triangular and nonsingular, and $U$ and $V$ are orthogonal. The solution to the linear least squares problem (8.2.1) is then ${ y = \Phi ^ { \dag } g }$ ,where

$$
\Phi ^ { \dagger } = V \left( \begin{array} { c } { { R ^ { - 1 } } } \\ { { 0 } } \end{array} \right) U _ { 1 } ^ { T }
$$

is the generalized inverse. The orthogonal projectors onto the range of $\Phi$ and its orthogonal complement are

$$
P _ { \Phi } = \Phi \Phi ^ { \dag } = U _ { 1 } U _ { 1 } ^ { T } , \qquad P _ { \Phi } ^ { \perp } = I - P _ { \Phi } = U _ { 2 } U _ { 2 } ^ { T } .
$$

The least squares residual is $r = P _ { \Phi } ^ { \perp } g = U _ { 2 } ( U _ { 2 } ^ { T } g )$ , and its norm is

$$
\| r \| _ { 2 } = \| U _ { 2 } ( U _ { 2 } ^ { T } g ) \| _ { 2 } = \| c _ { 2 } \| _ { 2 } , \quad U ^ { T } g = { \binom { c _ { 1 } } { c _ { 2 } } } .
$$

Denote by $D _ { k }$ the $m \times n$ matrix of $\Phi$ derivatives with respect to the single parameter $z _ { k }$

$$
D _ { k } = - \left[ P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z _ { k } } \Phi ^ { \dagger } + ( \Phi ^ { \dagger } ) ^ { T } \frac { d \Phi ^ { T } } { d z _ { k } } P _ { \Phi } ^ { \perp } \right] g , \quad k = 1 , \ldots , q .
$$

The $k$ th column of the first part of the Jacobian becomes

$$
- { \cal P } _ { \Phi } ^ { \perp } { \cal D } _ { k } \Phi ^ { \dagger } g = - U _ { 2 } ( U _ { 2 } ^ { T } ( { \cal D } _ { k } y ) ) , \quad k = 1 , \ldots , q .
$$

The second part becomes

$$
- ( P _ { \Phi } ^ { \perp } D _ { k } \Phi ^ { \dagger } ) ^ { T } g - ( \Phi ^ { \dagger } ) ^ { T } D _ { k } ^ { T } P _ { \Phi } ^ { \perp } g = U R ^ { - 1 } ( P ^ { T } ( D _ { k } ^ { T } r ) ) .
$$

Both columns can be computed using matrix-vector products and triangular solves. The second part is somewhat more expensive to compute.

The variable projection approach reduces the dimension of the parameter space and leads to a more well-conditioned problem. Furthermore, because no starting values have to be provided for the linear parameters, convergence to a global minimum is more likely. Krogh [7O8,1974] reports that at the Jet Propulsion Laboratory (JPL) the variable projection algorithm solved several problems that methods not using separability could not solve.

Kaufman [686,1975l gave a simplified version of the variable projection algorithm that uses an approximate Jacobian matrix obtained by dropping the second term in (8.2.4). This simplification was motivated by the observation that the second part of the Jacobian is negligible when the residual $r$ is small. Kaufman's simplification reduces the arithmetic cost per iteration by about $2 5 \%$ , with only a marginal increase in the number of iterations. Kaufman and Pereyra [688,1978] extend the simplified scheme to problems with separable equality constraints. Their approach is further refined by Corradi [270,1981].

Ruhe and Wedin [942,198o] consider variable projection methods for more general separable problems, where one set of variables can be easily eliminated. They show that the asymptotic rate of convergence of the variable projection method is essentially the same as for the Gauss-Newton method applied to the full problem.Both converge quadratically for zero-residual problems, whereas ALS always converges linearly.

Several implementations of the variable projection method are available.An improved ver-sion of the original program VARPRO was given by John Bolstad in 1977. This uses Kaufman's modification that allows for weights on the observations and also computes the covariance matrix.A version called VARP2 by LeVeque handles multiple right-hand sides. Both VARPRO and VARP2 are available in the public domain at http://www.netlib. $\mathsf { o r g } / \mathsf { o p t } /$ . Another implementation was written by Linda Kaufman and David Gay for the Port Library. A welldocumented implementation in MATLAB written by O'Leary and Rust [839,2o13] uses the full Jacobian as in the original Golub-Pereyra version.The motivation is that in many current applications,the increase in the number of function evaluations in Kaufman's version outweighs the savings gained from using an approximate Jacobian.

# Notes and references

The variable projection method is an extension of ideas first presented by Scolnik [982,1972] and Guttman,Pereyra,and Scolnik [557,1973]. Osborne [846,1975] showed how to eliminate the linear parameters in separable problems. Golub and LeVeque [497,1979] extend variable projection algorithms to the case when several data sets are to be fitted to a model with the same nonlinear parameter vector; see also Kaufman and Sylvester [689,1992]. A review of developments and applications of the variable projection approach for separable nonlinear least squares problems is given by Golub and Pereyra [5O4, 2003].

# 8.2.2 - Bilinear Least Squares Problems

Given data $A _ { i } \in \mathbb { R } ^ { p \times q }$ and $b _ { i }$ ， $i = 1 , \ldots , m$ , the bilinear least squares (BLSQ) problem is to determine parameters $x \in \mathbb { R } ^ { p }$ and $y \in \mathbb { R } ^ { q }$ that minimize

$$
\sum _ { i = 1 } ^ { m } ( x ^ { T } A _ { i } y - b _ { i } ) ^ { 2 } , \quad m \geq p + q .
$$

This is a nonlinear least squares problem with objective function

$$
f ( x , y ) = \| r ( x , y ) \| _ { 2 } ^ { 2 } , \quad r _ { i } ( x , y ) = b _ { i } - x ^ { T } A _ { i } y \in \mathbb { R } ^ { p } , \quad i = 1 , \ldots , m ,
$$

that is separable in each of the variables $x$ and $y$ .In system theory,the identification of a Hammerstein model leads to a BLSQ problem; see Wang, Zhang,and Ljung [11O0, 2oog]. Related multilinear problems are used in statistics,chemometrics,and tensor regression.

The data matrices $A _ { i }$ formathre-dimensional tensor $\mathcal { A } \in \mathbb { R } ^ { m \times p \times q }$ with elements $a _ { i , j , k }$ Slicing the tensor in the two other possible directions,we obtain matrices

$$
R _ { j } \in \mathbb R ^ { m \times q } , \quad j = 1 , \dots , p , \qquad S _ { k } \in \mathbb R ^ { m \times p } , \quad k = 1 , \dots , q .
$$

The BLSQ problem is linear in each of the variables $x$ and $y$ If $( x , y )$ is a solution to problem BLSQ, $x$ solves the linear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| \boldsymbol { B } \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } , \quad \boldsymbol { B } = \sum _ { k = 1 } ^ { q } y _ { k } \boldsymbol { S } _ { k } \in \mathbb { R } ^ { m \times p } ,
$$

where the matrices $S _ { k }$ are given as in (8.2.14). Similarly, $y$ solves

$$
\operatorname* { m i n } _ { y } \| C y - b \| _ { 2 } , \quad C = \sum _ { j = 1 } ^ { p } x _ { j } R _ { j } \in \mathbb { R } ^ { m \times q } .
$$

We deduce that the Jacobian of $r ( x , y )$ is

$$
J ( x , y ) = ( J _ { x } \quad J _ { y } ) = ( B \quad C ) \in \mathbb { R } ^ { m \times ( p + q ) } .
$$

For $\alpha \neq 0$ , the residuals $r _ { i } ( x , y ) = b _ { i } - x ^ { T } A _ { i } y$ of the bilinear problem (8.2.12) are invariant under the scaling $( \alpha x , \alpha ^ { - 1 } y )$ of the variables. This shows that the bilinear problem(8.2.12) is singular. The singularity can be handled by imposing a quadratic constraint $\| { \boldsymbol { x } } \| _ { 2 } = 1$ . Alternatively,a linear constraint $x _ { i } = e _ { i } ^ { T } x = 1$ for some $i$ $, 1 \leq i \leq m$ can be used. For convenience, we assume in the following that $i = 1$ $\mathbf { \boldsymbol { x } } _ { 1 } = 1$ ）and use the notation

$$
x = \binom { 1 } { \bar { x } } \in \mathbb { R } ^ { p } , \quad \bar { x } \in \mathbb { R } ^ { p - 1 } .
$$