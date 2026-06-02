has a unique solution. No further decomposition of $\pmb { R }$ is required because of its upper triangular structure. The components of $\boldsymbol { x }$ can be obtained directly from the back-substitution

$$
\begin{array} { l } { { x _ { m } } } \end{array} = \ d _ { m } / R _ { m , m } \nonumber
$$

because all components $R _ { i j }$ with $i > j$ vanish. The normal equations are not required anymore when using the orthogonal transformation and the corresponding numerical problems can therefore be avoided completely.

The same method of orthogonal transformations may also be applied to weighted observations, if $A$ and $\pmb { b }$ are replaced by

$$
A ^ { \prime } = \mathrm { d i a g } ( \sigma _ { 1 } ^ { - 1 } , \ldots , \sigma _ { n } ^ { - 1 } ) A \quad \mathrm { a n d } \quad b ^ { \prime } = \mathrm { d i a g } ( \sigma _ { 1 } ^ { - 1 } , \ldots , \sigma _ { n } ^ { - 1 } ) b \quad .
$$

Following (8.47), an a priori information matrix $\pmb { \varDelta }$ can further be considered by an appropriate extension

$$
A ^ { \prime \prime } = \binom { S } { A ^ { \prime } } \qquad \mathrm { a n d } \qquad b ^ { \prime \prime } = \binom { S x ^ { \mathrm { a p r } } } { b ^ { \prime } } ,
$$

where $s$ denotes a square root of $\pmb { \varDelta }$ (cf. (8.47)). $s$ can easily be computed for diagonal matrices, but a Cholesky factorization or similar operation is required to obtain a representation of the form $\mathbf { A } = S ^ { T } S$ for an arbitrary information matrix (see e.g. Schwarz 1988, Press et. al. 1992).

Finally, the QR decomposition may be employed to facilitate the computation of the covariance matrix by writing

$$
\operatorname { C o v } ( \pmb { x } , \pmb { x } ) = ( \pmb { A } ^ { T } \pmb { A } ) ^ { - 1 } = ( \pmb { R } ^ { T } \pmb { R } ) ^ { - 1 } = ( \pmb { R } ^ { - 1 } ) ( \pmb { R } ^ { - 1 } ) ^ { T } \quad .
$$

Since $\pmb { R }$ is an upper triangular matrix, the same holds for its inverse $\pmb { R } ^ { - 1 }$ , which may conveniently be obtained by solving $R R ^ { - 1 } = 1$ with the back-substitution algorithm described above (cf. Lawson & Hanson 1974).

# 8.2.2 Householder Transformations

The most efficient method for performing the QR factorization is due to Householder (1958). It involves a total of $m$ orthonormal transformations (cf. Fig. 8.3), which subsequently annihilate the sub-diagonal elements of $A$ yielding

$$
\begin{array} { l c l c c } { { ( U _ { m } U _ { m - 1 } \ldots U _ { 2 } U _ { 1 } ) A } } & { { = } } & { { Q ^ { T } A } } & { { = } } & { { { \binom { R } { \bf 0 } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { ( U _ { m } U _ { m - 1 } \ldots U _ { 2 } U _ { 1 } ) b } } & { { = } } & { { Q ^ { T } b } } & { { = } } & { { { \binom { d } { r } } . } } \end{array}
$$

$$
\begin{array} { r l r } { A } & { = } & { \left( \begin{array} { l } { { \sf X } \ { \sf X } \ { \sf X } } \\ { { \sf X } \ { \sf X } \ { \sf X } } \\ { { \sf X } \ { \sf X } } \\ { { \sf X } \ { \sf X } } \end{array} \right) \qquad { \cal U } _ { 1 } A } & { = } & { \left( \begin{array} { l } { { \sf X } \ { \sf X } \ { \sf X } \ { \sf X } } \\ { { \sf 0 } \ { \sf X } \ { \sf X } } \\ { { \sf 0 } \ { \sf X } \ { \sf X } } \\ { { \sf X } \ { \sf X } } \end{array} \right) } \\ & { } & { \quad \times \ { \sf X } } \end{array}
$$

$$
\begin{array} { r l r } { U _ { 2 } U _ { 1 } A } & { = } & { \left( \begin{array} { l l } { \times \times \times } \\ { 0 \times \times } \\ { 0 0 \times } \\ { 0 0 \times } \\ { 0 0 \times } \end{array} \right) \quad U _ { 3 } U _ { 2 } U _ { 1 } A = \left( \begin{array} { l l } { \times \times \times } \\ { 0 \times \times } \\ { 0 0 \times } \\ { 0 0 0 } \\ { 0 0 0 } \end{array} \right) } \end{array}
$$

An individual Householder transformation is defined as

$$
\pmb { U } = ( \mathbf { 1 } - 2 \pmb { w } \pmb { w } ^ { T } ) = \pmb { U } ^ { T }
$$

where ${ \mathbf { } } w { \mathbf { } } w ^ { T }$ denotes the outer product of a unit vector $\pmb { w }$ and its transpose. The orthonormality of $U$ follows from the fact that

$$
\begin{array} { r } { { \cal U } ^ { T } { \cal U } = { \cal U } ^ { 2 } = \mathbf { 1 } - 4 { \pmb { w } } { \pmb { w } } ^ { T } + 4 { \pmb { w } } { \pmb { w } } ^ { T } { \pmb { w } } { \pmb { w } } ^ { T } = \mathbf { 1 } } \end{array}
$$

for ${ \pmb w } ^ { T } { \pmb w } = | { \pmb w } | ^ { 2 } = 1$ , which also means that $U$ is its own inverse. Since vectors at right angles to $\pmb { w }$ are not affected by $U$ , while $\pmb { w }$ is mapped into $- { \pmb w }$ , it may seen that $U$ corresponds to a reflection at a hyperplane perpendicular to $\pmb { w }$ (cf. Fig. 8.4).

![](images/289337f4e627e2f1c17f33699ddfea60adbea53845e4c0b0785fd0fb4d6f4a5c.jpg)  
Fig. 8.3. Triangularization of a $5 \times 3$ matrix by a sequence of Householder Transformations   
Fig. 8.4. Householder Transformation

By a proper choice of $\pmb { w }$ , a vector $\pmb { h }$ of length $h$ can be mapped into a multiple he of the unit vector $\pmb { e } = ( 1 , 0 , \dots , 0 ) ^ { T }$ , which is zero except for the first component. For this purpose $\pmb { w }$ must be a unit vector in the direction of the difference vector $\pmb { h } / h - e$ and is therefore given by

$$
{ \pmb w } = \frac { { \pmb h } / h - { \pmb e } } { | { \pmb h } / h - { \pmb e } | } = \frac { { \pmb h } / h - { \pmb e } } { \sqrt { 2 ( 1 - h _ { 1 } / h ) } } .
$$

Using the same expression with $\pmb { h }$ replaced by the first column vector of $A$ , one obtains the first transformation matrix $\pmb { U } _ { 1 } = \mathbf { 1 } - 2 \pmb { w } _ { 1 } \pmb { w } _ { 1 } ^ { T }$ that eliminates all subdiagonal elements in the first column of $A$ . The same principle may then be applied to determine the transformations $U _ { 2 } , \ldots , U _ { n }$ that convert the remaining columns and yield the desired upper triangular matrix $\pmb { R }$ .

For further details on the algorithm and an efficient computer implementation of Householder transformations in least-squares problems the reader is referred to standard text books like Golub & van Loan (1989) or Schwarz (1988).

# 8.2.3 Givens Rotations

A second type of orthonormal transformations that may be used to perform a QR factorization is known as Givens rotations (Givens 1958). A single $n$ -dimensional transformation matrix

$$
U _ { i , k } ( \phi ) = \left( \begin{array} { c c c c c c c } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + c } } & { { } } & { { + s } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - s } } & { { } } & { { + c } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right)
$$

is an identity matrix except for the elements

$$
\begin{array} { r }  \binom { U _ { i i } } { U _ { k i } } U _ { i k } \atop U _ { k i } \end{array} \quad \left( \begin{array} { l l } { + c } & { + s } \\ { - s } & { + c } \end{array} \right) = \left( \begin{array} { l l } { + \cos \phi } & { + \sin \phi } \\ { - \sin \phi } & { + \cos \phi } \end{array} \right) \quad ,
$$

which define a rotation by an angle $\phi$ in the $( i k )$ -plane. Since $U _ { i k } ^ { T } \pmb { U } _ { i k } = \mathbf { 1 }$ , the matrix is in fact orthonormal and therefore does not change the Euclidean norm of a vector.

When applied to an $n \times m$ matrix $A = ( A _ { i j } )$ from the left, $U _ { i k }$ affects only lines $i$ and $k$ , while the remaining lines are unchanged. The new elements of $\pmb { A } ^ { \prime } = \pmb { U } _ { i k } \pmb { A }$ are given by

$$
\begin{array} { r c l c r c l } { { A _ { i j } ^ { \prime } } } & { { = } } & { { + c \cdot A _ { i j } + s \cdot A _ { k j } } } & { { } } & { { ( j = 1 , \ldots , m ) } } \\ { { A _ { k j } ^ { \prime } } } & { { = } } & { { - s \cdot A _ { i j } + c \cdot A _ { k j } } } & { { . } } & { { } } & { { } } \end{array}
$$

If $c$ and $s$ are chosen as

$$
{ \binom { c } { s } } = { \frac { 1 } { \sqrt { A _ { i i } ^ { 2 } + A _ { k i } ^ { 2 } } } } { \binom { A _ { i i } } { A _ { k i } } }
$$

then

$$
\begin{array} { r c l } { { A _ { i i } ^ { \prime } } } & { { = } } & { { \sqrt { A _ { i i } ^ { 2 } + A _ { k i } ^ { 2 } } } } \\ { { A _ { k i } ^ { \prime } } } & { { = } } & { { 0 \quad . } } \end{array}
$$

$$
\begin{array}{c} { \begin{array} { r l } & { { \left( \times \times \times \times \right) } } \\ & { \times \times \times } \\ & { \times \times \times } \\ & { \times \times } \\ & { \left\{ \vdots \ \vdots \ \vdots \right\} } \end{array} } { \begin{array} { r l } & { U _ { 1 , 2 } } \\ & { 0 \times \times } \\ & { \times \times } \\ & { \times \ \times } \\ & { \left\{ \begin{array} { r l r } { \times \times } & { \times } \\ { 0 \ \ \times } & { \times } \\ { \cdot \ \vdots \ \vdots } \end{array} \right\} } } & { U _ { 1 , 3 } } \\ & { \left( \cdot \ \times \times \right) } & { \left( \begin{array} { r l r } { \times } & { \times } & { \times } \\ { 0 \ \ \times } & { \times } \\ { 0 \ \ \times } & { \times } \\ { \times \ \times } & { \times } \end{array} \right) } & { U _ { 2 , 3 } } \\ & { \left( \cdot \ \times \times \ \right) } & { \left( \begin{array} { r l r } { \times } & { \times } & { \times } \\ { 0 \ } & { \times } & { \times } \\ { 0 \ } & { 0 \ } & { \times } \\ { \vdots \ \vdots } & { \vdots } \end{array} \right) } \end{array}   \\ & { } \end{array} 
$$

In other words, the element $A _ { k i } ^ { \prime }$ vanishes.

While the Householder transformation which eliminates all sub-diagonal elements in a column of $A$ , a Givens rotation reduces only one element to zero at a time. This gives the freedom to process one row after another as indicated in Fig. 8.5. The complete transformation is then given by

$$
\begin{array} { l c l } { { ( U _ { n } U _ { n - 1 } \ldots U _ { 3 } U _ { 2 } ) A } } & { { = } } & { { Q ^ { T } A } } & { { = } } & { { { \binom { R } { \bf 0 } } } } \\ { { } } & { { } } & { { } } \\ { { ( U _ { n } U _ { n - 1 } \ldots U _ { 3 } U _ { 2 } ) b } } & { { = } } & { { Q ^ { T } b } } & { { = } } & { { { \binom { d } { r } } . } } \end{array}
$$

Here

$$
U _ { i } = U _ { \operatorname* { m i n } ( i - 1 , m ) , i } \ . \ . \ . U _ { 2 , i } U _ { 1 , i }
$$

denotes the sequence of rotations required to eliminate the sub-diagonal elements in the $i$ th row of $A$ .

The advantage of a row-by-row transformation is that the QR factorization can already be computed with parts of the design matrix $A$ and the vector $\pmb { b }$ . Denoting the $i$ th row of $A$ by $\pmb { a } _ { i } ^ { T }$ and the $i$ th element of $\pmb { b }$ by $b _ { i }$ , the measurement equations

$$
{ \pmb a } _ { i } ^ { T } { \pmb x } = b _ { i } \qquad i = 1 , \ldots , n \quad ,
$$

can be processed one-by-one with the sequential accumulation algorithm. This is illustrated in Fig. 8.6.

A sequence of $m$ Givens rotations for each measurement transforms the given upper triangular system of linear equations $\boldsymbol { R } \boldsymbol { x } \ = \ d$ and a single data equation ${ \pmb a } ^ { T } { \pmb x } = b$ into the upper triangular system $\pmb { R } ^ { \prime } \pmb { x } = \pmb { d } ^ { \prime }$ and the scalar $b ^ { \prime }$ . Assuming that the sum of the residuals squared before the triangularization was $| r | ^ { 2 }$ , its value after processing of the new measurement equation is given by

$$
| { \boldsymbol r } ^ { \prime } | ^ { 2 } = | { \boldsymbol r } | ^ { 2 } + ( b ^ { \prime } ) ^ { 2 } ~ .
$$

![](images/3b23b3a4e9ffd51aefb72d7c3d002a2445b9fd3ce0a956518fc73e314aa51d31.jpg)  
Fig. 8.6. Accumulation of a data equation by Givens rotations. For each step, boxes indicate the values affected by the transformation that annihilates the leading non-zero element of the data equation.

With start values of $\pmb { R } = \pmb { 0 }$ and $\mathbf b = \mathbf 0$ the algorithm can be applied to process all data equations recursively.

The only quantities which have to be stored during the sequential accumulation of all measurement equations are the upper triangular $m { \times } m$ matrix $\pmb { R }$ , the vector $\mathbf { \Delta } _ { d }$ , and the Euclidean norm of the residual vector $| r |$ . The overall storage requirements are therefore considerably smaller than for Householder factorization of an $n \times m$ design matrix $A$ .

# 8.2.4 Singular Value Decomposition

Aside from the QR decomposition discussed so far, a singular value decomposition may be used to analyze a given least-squares problem and solve it in a numerically stable manner. The method is well suited to detecting and overcoming a possible singularity or near singularity of the least-squares equations and is therefore recommended for all ill-conditioned problems despite an increased computational effort as compared to other techniques (Lawson 1971).

The singular value decomposition of the $n \times m$ partial derivative matrix $A$ is denoted by

$$
\mathbf { A } = \pmb { U } \pmb { D } \pmb { V } ^ { T } \quad ,
$$

where

$$
\pmb { { \cal D } } = \mathrm { d i a g } ( d _ { 1 } , \dots , d _ { m } )
$$

is a diagonal $m \times m$ matrix. $U$ and $V$ are orthonormal matrices of dimension $n \times m$ and $m \times m$ , which means that both $U ^ { T } U$ and $V ^ { T } V$ are equal to the $m$ dimensional identity matrix.

The quantities $d _ { 1 } \geq d _ { 2 } . . . \geq d _ { m } \geq 0$ are known as singular values. There are exactly $k$ positive singular values for a matrix of rank $k \leq m$ , whereas the remaining $m - k$ values $d _ { k + 1 } , \ldots , d _ { m }$ are zero. Since

$$
{ \cal A } ^ { T } { \cal A } = V { \cal D } ^ { 2 } V ^ { T } = V \mathrm { d i a g } ( d _ { 1 } ^ { 2 } , \ldots , d _ { m } ^ { 2 } ) V ^ { T } ~ ,
$$

each column vector ${ \boldsymbol { v } } _ { i }$ of $V$ is an eigenvector of the normal equations matrix and the singular value $d _ { i }$ is the non-negative square root of the associated eigenvalue $\lambda _ { i } = d _ { i } ^ { 2 }$ .

In view of the effort required for an eigenvalue analysis it is not surprising that the computation of the singular value decomposition is also much more involved than that of a simple QR factorization. By a sequence of Householder transformations, which are alternately applied from the left and right, $A$ is first converted into a bi-diagonal matrix, in which all elements are zero except those in the diagonal and immediately above it. Next an iterative sequence of orthogonal transformations is applied, which retains the bi-diagonal form but tends to eliminate the elements in the upper diagonal and finally converges to a diagonal matrix containing the singular values. For a detailed discussion of the algorithm, which is beyond the scope of this presentation, the reader is referred to Golub & Reinsch (1970) or Golub & van Loan (1989). Useful computer implementations are furthermore described in Lawson & Hanson (1974) or Press et al. (1992).

In order to illustrate the application of singular value decomposition to leastsquares problems, the loss function

$$
J = ( \pmb { b } - \pmb { A } \pmb { x } ) ^ { T } ( \pmb { b } - \pmb { A } \pmb { x } )
$$

is considered. Making use of the singular value decomposition of $A$ and of the definitions

$$
{ \pmb x } = { \pmb V } ^ { T } { \pmb x } \qquad t = { \pmb U } ^ { T } { \pmb b }
$$

the condition

$$
( A ^ { T } A ) \pmb { x } = A ^ { T } b
$$

for the loss function minimum can be replaced by the equivalent expression

$$
D ^ { 2 } s = D t \quad .
$$

For non-singular normal equations the inverse of $\pmb { D }$ exists and the solution of the least-squares problem is then given by $\mathbf { \boldsymbol { s } } = \mathbf { \boldsymbol { D } } ^ { - 1 } \boldsymbol { t }$ or

$$
{ \boldsymbol { \mathbf { \mathit { x } } } } = V { \boldsymbol { \mathbf { \mathit { D } } } } ^ { - 1 } { \boldsymbol { \mathbf { \mathit { U } } } } ^ { T } { \boldsymbol { \mathbf { \mathit { b } } } } = \sum _ { i = 1 } ^ { m } { \frac { { \boldsymbol { \mathbf { u } } } _ { i } ^ { T } { \boldsymbol { \mathbf { b } } } } { d _ { i } } } { \boldsymbol { \mathbf { \mathit { v } } } } _ { i } \quad .
$$

Here $\pmb { u } _ { i }$ and ${ \boldsymbol { v } } _ { i }$ are used to denote the column vectors of $U$ and $V$ , respectively.

If the rank of $A$ is less than $m$ , however, only the first $k$ components of $\pmb { S }$ can be determined from (8.82) according to

$$
\left( \begin{array} { c } { { s _ { 1 } } } \\ { { \vdots } } \\ { { s _ { k } } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right) = \left( \begin{array} { c } { { t _ { 1 } / d _ { 1 } } } \\ { { \vdots } } \\ { { t _ { k } / d _ { k } } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right) .
$$

The remaining components are arbitrary, but can be fixed by the additional requirement of choosing $\boldsymbol { x }$ in such a way that the norm $| { \boldsymbol { x } } | = { \sqrt { { \boldsymbol { x } } ^ { T } { \boldsymbol { x } } } }$ is as small as possible. Since $\pmb { x } ^ { T } \pmb { x } = \pmb { s } ^ { T } \pmb { s }$ , this requirement is equivalent to setting $s _ { i } = 0$ for all $i > k$ . The solution of the degenerate least-squares problem is therefore given by

$$
{ \pmb x } = \sum _ { i = 1 } ^ { k } \frac { { \pmb u } _ { i } ^ { T } { \pmb b } } { d _ { i } } { \pmb v } _ { i } \quad ,
$$

which is the same as (8.83), except that all terms corresponding to zero singular values are discarded.

The same principle may also be applied in the case that $A$ has full rank but is nevertheless near-singular as indicated by a high ratio $d _ { 1 } / d _ { m }$ of the largest and smallest singular value. This ratio, which is also known as the condition number of the normal equations matrix, gives a general indication of the quality with which the solution is defined by the given measurements. Since the singular values appear in the denominator of (8.83), it is evident that $x$ is particularly sensitive to changes in the measurement vector $\pmb { b }$ for small $d _ { i }$ . In order to avoid a deterioration of the solution it may therefore be preferable to neglect contributions associated with small singular values. A useful solution (Lawson 1971) of the least-squares problem may then be obtained by replacing all singular values below a given limit $d _ { \mathrm { m i n } }$ by zero and proceeding as in the case of degenerate normal equations. As a result the loss function is slightly higher than the exact minimum. This is preferable, however, to a solution that is far off the correct value due to the strong influence of measurement errors.

As a general means for avoiding singularities one may employ a fixed limit $d _ { \mathrm { m i n } } / d _ { 1 } = \alpha$ for truncating the singular values, where $\alpha$ is a predefined value some orders of magnitude above the machine accuracy $\epsilon _ { \mathrm { m a c h } }$ . Improved results for a particular least-squares problem may furthermore be obtained from an analysis of the sequence of singular values as well as the associated solution and loss function value. Considering

$$
\begin{array} { r l r } { x } & { } & { d _ { 1 } \qquad d _ { 2 } \qquad \ldots \qquad d _ { m } } \\ { x } & { = } & { \displaystyle \frac { u _ { 1 } ^ { T } b } { d _ { 1 } } v _ { 1 } + \frac { u _ { 2 } ^ { T } b } { d _ { 2 } } v _ { 2 } + \ldots + \frac { u _ { m } ^ { T } b } { d _ { m } } v _ { m } } \\ { J ( x ) } & { = } & { b ^ { T } b - ( u _ { 1 } ^ { T } b ) ^ { 2 } - ( u _ { 2 } ^ { T } b ) ^ { 2 } - \ldots - ( u _ { m } ^ { T } b ) ^ { 2 } v _ { m } } \end{array}
$$

one may then select a value for $d _ { \mathrm { m i n } }$ , which reduces the loss function to an acceptable value but does not give rise to a large value of $x$ .

# 8.3 Kalman Filtering

The least-squares or batch estimation method yields an estimate of the epoch state vector by processing the complete set of observations in each iteration. Therefore, it requires that all measurements to be considered in an orbit determination are available before the a priori information can be improved. This makes least-squares estimation less convenient for real-time or near-real-time applications that call for a quasi-continuous update of the state information with each observation. In addition, the least-squares method requires the estimate of the epoch state vector to fit the entire data span, which makes it suceptible to dynamical model errors and the assumption of constant measurement biases. An alternative estimation method which copes with these problems, is known as sequential estimation or Kalman filter referring to the pioneering work of Kalman (1960) and Kalman & Bucy (1961).

# 8.3.1 Recursive Formulation of Least-Squares Estimation

Despite evident differences between least-squares estimation and the Kalman filter, both methods can be related to each other by a variety of intermediate formulations. In order to derive the filter equations from the least-squares method, one may consider a situation in which the whole set of observations is partitioned into statistically independent batches or subsets and ask how the estimated epoch state changes by including successive batches into the estimation.

Upon processing a single batch of measurements $z$ , an a priori estimate $x _ { 0 } ^ { - } =$ $\pmb { x } _ { 0 } ^ { \mathrm { r e f } } + \varDelta \pmb { x } _ { 0 } ^ { - }$ and its covariance $P _ { 0 } ^ { - }$ 0 are assumed to be available either from the processing of previous data batches or from initial information. As usual, all quantities are linearized about a common reference state $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ . Based on the solution (8.50) of the general least-squares problem, the measurements and the a priori estimate can now be combined into an improved estimate

$$
\Delta \pmb { x } _ { 0 } ^ { + } = \pmb { P } _ { 0 } ^ { + } \left( ( \pmb { P } _ { 0 } ^ { - } ) ^ { - 1 } \Delta \pmb { x } _ { 0 } ^ { - } + \pmb { H } ^ { T } \pmb { W } \Delta z \right) .
$$

Here, the a-posteriori covariance matrix

$$
( \pmb { P } _ { 0 } ^ { + } ) = \left( ( \pmb { P } _ { 0 } ^ { - } ) ^ { - 1 } + ( \pmb { H } ^ { T } \pmb { W } \pmb { H } ) \right) ^ { - 1 }
$$

represents the increased knowledge of $x _ { 0 }$ resulting from both the a priori information and the latest data batch.

In order to relate the new estimate $\boldsymbol { x } _ { 0 } ^ { + }$ to the previous estimate $\boldsymbol { x } _ { 0 } ^ { - }$ , one substitutes the a priori information matrix by the difference

$$
( \pmb { P } _ { 0 } ^ { - } ) ^ { - 1 } = ( \pmb { P } _ { 0 } ^ { + } ) ^ { - 1 } - ( \pmb { H } ^ { T } \pmb { W } \pmb { H } )
$$

of the a-posteriori information matrix and the measurement information matrix. This yields the basic expression

$$
\Delta \pmb { x } _ { 0 } ^ { + } = \Delta \pmb { x } _ { 0 } ^ { - } + \pmb { P } _ { 0 } ^ { + } \pmb { H } ^ { T } \pmb { W } ( \Delta z - \pmb { H } \Delta \pmb { x } _ { 0 } ^ { - } )
$$

for a recursive formulation of least-squares estimation. The matrix

$$
\pmb { K } = \pmb { P } _ { 0 } ^ { + } \pmb { H } ^ { T } \pmb { W }
$$

maps the residuals

$$
\rho = \varDelta z - H \varDelta x _ { 0 } ^ { - } = z - h ( x _ { 0 } ^ { \mathrm { r e f } } ) - H \varDelta x _ { 0 } ^ { - }
$$

into an appropriate correction of the estimate $\boldsymbol { x } _ { 0 } ^ { - }$ and is known as Kalman gain. The vector $\pmb { \rho }$ represents residuals with respect to reference values defined by the estimate $\boldsymbol { x } _ { 0 } ^ { - }$ . It is computed from the measurements $z$ , the reference-model observations $\pmb { h } ( \pmb { x } _ { 0 } ^ { \mathrm { r e f } } )$ and a linear correction ${ \pmb { H } } ( { \pmb x } _ { 0 } ^ { - } { - \pmb x } _ { 0 } ^ { \mathrm { r e f } } )$ that accounts for the difference between $\boldsymbol { x } _ { 0 } ^ { - }$ and the reference state.

A recursive formulation of the orbit determination problem as given above has already been suggested by Swerling (1959) but could not gain widespread acceptance. For practical applications (8.90) suffers from the fact that the direct computation of the covariance matrix $P _ { 0 } ^ { + }$ from (8.88) requires the inversion of an $m \times m$ -matrix in each step with $m$ denoting the dimension of the estimation vector $x _ { 0 }$ . To remove this deficiency the product $\pmb { K } = \pmb { P } _ { 0 } ^ { + } \pmb { H } ^ { T } \pmb { W }$ can be replaced by the equivalent expression

$$
{ \cal K } = P _ { 0 } ^ { - } H ^ { T } \left( W ^ { - 1 } + H P _ { 0 } ^ { - } H ^ { T } \right) ^ { - 1 } .
$$

Even though this expression seems to be more involved at first sight, it turns out to be more efficient, if the size of each data set is small compared to the dimension $m$ . In particular, this is the case when each batch consists of a single observation only. The matrix is then reduced to a scalar quantity and the inverse is obtained by a simple division.

The validity of substitution (8.93) follows from the relation

$$
\begin{array} { l c l } { { } } & { { { \cal H } ^ { T } + { \cal H } ^ { T } W { \cal H } P { \cal H } ^ { T } } } & { { = } } & { { { \cal H } ^ { T } + { \cal H } ^ { T } W { \cal H } P { \cal H } ^ { T } } } \\ { { \Leftrightarrow } } & { { { \cal H } ^ { T } W ( W ^ { - 1 } + { \cal H } P { \cal H } ^ { T } ) } } & { { = } } & { { ( P ^ { - 1 } + { \cal H } ^ { T } W { \cal H } ) P { \cal H } ^ { T } } } \\ { { \Leftrightarrow } } & { { ( P ^ { - 1 } + { \cal H } ^ { T } W { \cal H } ) ^ { - 1 } { \cal H } ^ { T } W } } & { { = } } & { { P { \cal H } ^ { T } ( W ^ { - 1 } + { \cal H } P { \cal H } ^ { T } ) ^ { - 1 } , } } \end{array}
$$

which is based on a matrix inversion lemma attributed to A. S. Householder (see Bierman 1977). Considering, furthermore, the identities

$$
\begin{array} { r c l } { { P _ { 0 } ^ { - } } } & { { = } } & { { P _ { 0 } ^ { + } ( P _ { 0 } ^ { + } ) ^ { - 1 } P _ { 0 } ^ { - } } } \\ { { } } & { { = } } & { { P _ { 0 } ^ { + } \left( ( P _ { 0 } ^ { - } ) ^ { - 1 } + H ^ { T } W H \right) P _ { 0 } ^ { - } } } \\ { { } } & { { = } } & { { P _ { 0 } ^ { + } + ( P _ { 0 } ^ { + } H ^ { T } W ) H P _ { 0 } ^ { - } } } \\ { { } } & { { = } } & { { P _ { 0 } ^ { + } + K H P _ { 0 } ^ { - } \ , } } \end{array}
$$

the Kalman gain $\pmb { K }$ may also be employed to compute the updated covariance matrix

$$
P _ { 0 } ^ { + } = ( { \bf 1 } { - } { K } H ) P _ { 0 } ^ { - }
$$

without the need to invert the normal equations matrix.

Combining the results obtained so far, the recursive least-squares estimation algorithm proceeds in the following way. Given the a priori and reference state $ { \boldsymbol { { x } } } _ { 0 } ^ { 0 }$ , the associated covariance $\pmb { P } _ { 0 } ^ { 0 }$ and the measurement batches $z _ { I }$ $( I = 1 , \ldots , N )$ recursive estimates $\boldsymbol { x } _ { 0 } ^ { I }$ of the epoch state $x _ { 0 }$ as well as the associated covariance matrices $P _ { 0 } ^ { I }$ are computed for each batch $( I = 1 , \ldots , N )$ via the steps Kalman-gain computation, epoch state vector update and epoch covariance update

$$
\begin{array} { l c l } { { K _ { I } } } & { { = } } & { { { \pmb P } _ { 0 } ^ { I - 1 } { \pmb H } _ { I } ^ { T } ( W _ { I } ^ { - 1 } + H _ { I } { \pmb P } _ { 0 } ^ { I - 1 } { \pmb H } _ { I } ^ { T } ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { { \pmb x } _ { 0 } ^ { I } } } & { { = } } & { { { \pmb x } _ { 0 } ^ { I - 1 } + K _ { I } ( z _ { I } - h _ { I } ( { \pmb x } _ { 0 } ^ { 0 } ) - { \pmb H } _ { I } ( { \pmb x } _ { 0 } ^ { I - 1 } - { \pmb x } _ { 0 } ^ { 0 } ) ) } } \\ { { } } & { { } } & { { } } \\ { { { \pmb P } _ { 0 } ^ { I } } } & { { = } } & { { ( { \bf 1 } - K _ { I } { \pmb H } _ { I } ) { \pmb P } _ { 0 } ^ { I - 1 } . } } \end{array}
$$

While the above expressions are general enough to handle an arbitrary number of measurements per batch, the Kalman-gain computation is optimized for processing only a small number of measurements per step. Thus each batch will usually comprise a vector of measurement taken at a common epoch with possible correlations or a single, scalar observation. Uncorrelated measurements can always be processed one at a time3, in which case the vector $z _ { I }$ is replaced by the scalar measurement $z _ { i }$ , the weighting matrix $W _ { I }$ is replaced by the scalar weighting factor $w _ { i } = \sigma _ { i } ^ { - 2 }$ and the Kalman gain matrix $K _ { I }$ becomes a vector $k _ { i }$ with the same dimension $( m )$ ) as the state vector $x _ { 0 }$ . Similarly, the Jacobian ${ \pmb H } _ { I } = \partial z _ { I } / \partial { \pmb x } _ { 0 }$ reduces to a $1 \times m$ matrix (i.e. a row vector), which means that products of the form ${ \pmb { H } } { \pmb { P } } { \pmb { H } } ^ { T }$ or $\pmb { H x }$ are scalar quantities, too. The resulting set of equations may then be written as

$$
\begin{array} { l l l } { { k _ { i } } } & { { = } } & { { P _ { 0 } ^ { i - 1 } H _ { i } ^ { T } ( \sigma _ { i } ^ { 2 } + H _ { i } P _ { 0 } ^ { i - 1 } H _ { i } ^ { T } ) ^ { - 1 } } } \\ { { { \bf x } _ { 0 } ^ { i } } } & { { = } } & { { { \bf x } _ { 0 } ^ { i - 1 } + k _ { i } ( z _ { i } - h _ { i } ( { \bf x } _ { 0 } ^ { 0 } ) - H _ { i } ( { \bf x } _ { 0 } ^ { i - 1 } - { \bf x } _ { 0 } ^ { 0 } ) ) } } \\ { { { \bf P } _ { 0 } ^ { i } } } & { { = } } & { { ( { \bf 1 } - k _ { i } H _ { i } ) P _ { 0 } ^ { i - 1 } . } } \end{array}
$$

In the expression for the covariance update care should be taken that $\pmb { k } _ { i } \pmb { H } _ { i }$ denotes the dyadic product of the Kalman gain (a column vector) and the measurement partials (a row vector). Unlike the dot product that results in a scalar value, the dyadic product yields an $m \times m$ matrix.

Independent of the subdivision of the measurement vector into individual batches the state estimate and covariance obtained after processing the last observation is identical to the one that would have been obtained in the first iteration of the standard least-squares method. The recursive formulation may be used, however, to obtain state estimates and covariances after each measurement without the need to collect all observations before inverting the normal equations.

# 8.3.2 Sequential Estimation

Even though the recursive least-squares estimation allows an on-line monitoring of the way in which each observation improves the epoch state estimate, the method cannot readily be used to obtain estimates of the state vector at the measurement times. This requires a propagation of both the state vector and its covariance between the times of successive observations and yields the classical sequential estimation or Kalman filter algorithm.

In the sequel it is assumed that a single data set $z _ { i }$ contains only observations taken at the same time $t _ { i }$ . As an example a batch of measurements may consist of a pair of azimuth/elevation values that have been obtained simultaneously from the antenna or it may consist of a single range measurement taken independently. Starting from the state and covariance at a previous epoch $t _ { i - 1 }$ the measurement vector $z _ { i }$ can then be used to obtain an improved state vector at the measurement epoch $t _ { i }$ together with the associated covariance. For that purpose let

$$
\pmb { x } _ { i } ^ { \mathrm { r e f } } = \pmb { x } ( t _ { i } ; \pmb { x } ( t _ { 0 } ) = \pmb { x } _ { 0 } ^ { \mathrm { r e f } } ) = \pmb { x } ( t _ { i } ; \pmb { x } ( t _ { i - 1 } ) = \pmb { x } _ { i - 1 } ^ { \mathrm { r e f } } )
$$

denote the state vector that is obtained by propagating the epoch reference state $\pmb { x } _ { 0 } ^ { \mathrm { r e f } }$ from $t _ { 0 }$ to $t _ { i }$ or, alternatively, by propagating ${ \boldsymbol x } _ { i - 1 } ^ { \mathrm { r e f } }$ from $t _ { i - 1 }$ to $t _ { i }$ . Furthermore, let

$$
\mathbf { \varPhi } _ { i } = \mathbf { \varPhi } ( t _ { i } , t _ { i - 1 } ) = \frac { \partial \mathbf { x } _ { i } ^ { \mathrm { r e f } } } { \partial \mathbf { x } _ { i - 1 } ^ { \mathrm { r e f } } } = \mathbf { \varPhi } ( t _ { i } , t _ { 0 } ) \mathbf { \varPhi } ( t _ { i - 1 } , t _ { 0 } ) ^ { - 1 }
$$

denote the state transition matrix from epoch $t _ { i - 1 }$ to epoch $t _ { i }$ , which follows from the solution of the appropriate variational equations.

Using these quantities, the state vector $\pmb { x } _ { i - 1 } ^ { + }$ (obtained from data up to and including time $t _ { i - 1 }$ ) may be employed to predict an a priori state vector

$$
\pmb { x } _ { i } ^ { - } = \pmb { x } _ { i } ^ { \mathrm { r e f } } + \pmb { \phi } _ { i } ( \pmb { x } _ { i - 1 } ^ { + } - \pmb { x } _ { i - 1 } ^ { \mathrm { r e f } } )
$$

at epoch $t _ { i }$ . The corresponding a priori covariance at that epoch follows from

$$
\begin{array} { r c l } { P _ { i } ^ { - } } & { = } & { \operatorname { E } \left( ( \pmb { x } _ { i } ^ { - } - \mathrm { E } ( \pmb { x } _ { i } ^ { - } ) ) ( \pmb { x } _ { i } ^ { - } - \mathrm { E } ( \pmb { x } _ { i } ^ { - } ) ) ^ { T } \right) } \\ & { = } & { \operatorname { E } \left( \pmb { \phi } _ { i } ( \pmb { x } _ { i - 1 } ^ { + } - \mathrm { E } ( \pmb { x } _ { i - 1 } ^ { + } ) ) ( \pmb { x } _ { i - 1 } ^ { + } - \mathrm { E } ( \pmb { x } _ { i - 1 } ^ { + } ) ) ^ { T } \pmb { \phi } _ { i } ^ { T } \right) } \\ & { = } & { \pmb { \phi } _ { i } \pmb { P } _ { i - 1 } ^ { + } \pmb { \phi } _ { i } ^ { T } ~ , } \end{array}
$$

where $P _ { i - 1 } ^ { + }$ is the covariance of $\boldsymbol { x } _ { i - 1 } ^ { + }$ . Since the observations $z _ { i }$ have not yet been taken into account, the information contained in $\boldsymbol { x } _ { i } ^ { - }$ and ${ P } _ { i } ^ { - }$ is exactly the same as that in $\pmb { x } _ { i - 1 } ^ { + }$ and $P _ { i - 1 } ^ { + }$ except for the epoch to which these values refer.

In order to incorporate the new measurements and update the a priori information, the residual vector $\pmb { \rho } _ { i }$ is expressed as a function of quantities referring to $t _ { i }$ instead of $t _ { 0 }$ :

$$
\begin{array} { r c l } { { \pmb \rho _ { i } } } & { { = } } & { { z _ { i } - { \pmb h } _ { i } ( { \pmb x } _ { 0 } ^ { \mathrm { r e f } } ) - { \pmb H } _ { i } ( { \pmb x } _ { 0 } ^ { - } - { \pmb x } _ { 0 } ^ { \mathrm { r e f } } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { z _ { i } - g _ { i } ( { \pmb x } _ { i } ^ { \mathrm { r e f } } ) - { \pmb G } _ { i } ( { \pmb x } _ { i } ^ { - } - { \pmb x } _ { i } ^ { \mathrm { r e f } } ) . } } \end{array}
$$

Here $\pmb { h } _ { i }$ , which models the observations at time $t _ { i }$ in terms of the state at epoch $t _ { 0 }$ has been replaced by the equivalent function

$$
{ \pmb g } _ { i } ( t _ { i } , { \pmb x } ( t _ { i } ) ) = { \pmb h } _ { i } ( t _ { i } , { \pmb x } ( t _ { 0 } ) ) \quad ,
$$

which models the observations in terms of the state vector at the measurement time (cf. (8.5)). Accordingly, the Jacobian $H _ { i }$ has been factored into

$$
H _ { i } = \frac { \partial h _ { i } } { \partial x _ { 0 } ^ { \mathrm { r e f } } } = \frac { \partial g _ { i } } { \partial x _ { i } ^ { \mathrm { r e f } } } \frac { \partial x _ { i } ^ { \mathrm { r e f } } } { \partial x _ { 0 } ^ { \mathrm { r e f } } } = G _ { i } \phi \left( t _ { i } , t _ { 0 } \right) \mathrm { w i t h } G _ { i } = \frac { \partial g _ { i } } { \partial x _ { i } ^ { \mathrm { r e f } } }
$$

to obtain the desired expression for the residual vector. Similarly, the Kalman gain is formulated as

$$
{ \cal K } _ { i } = P _ { i } ^ { - } G _ { i } ^ { T } ( W _ { i } ^ { - 1 } + G _ { i } P _ { i } ^ { - } G _ { i } ^ { T } ) ^ { - 1 } ~ ,
$$

which maps the residuals into a state vector correction at the measurement epoch $t _ { i }$ .

# Linearized Kalman Filter

Combining the results obtained so far, the sequential estimation algorithm or Kalman filter proceeds by computing estimates $\boldsymbol { x } _ { i } ^ { + }$ of the state vector at the measurement times $t _ { i }$ $( i = 1 , \ldots , n )$ as well as the associated covariance matrices ${ { { { \cal P } } } } _ { i } ^ { + }$ via sequential time and measurement update steps (Fig. 8.7).

The time update phase starts with the integration of the equation of motion and the variational equations from $t _ { i - 1 }$ to $t _ { i }$ in order to obtain the reference state $\pmb { x } _ { i } ^ { \mathrm { r e f } }$ and the transition matrix ${ \bf \Phi } { \bf { \Phi } } \Phi _ { i } = \partial { \bf x } _ { i } ^ { \mathrm { r e f } } / \partial x _ { i - 1 } ^ { \mathrm { r e f } }$ i. Using these quantities the previous estimate $\pmb { x } _ { i - 1 } ^ { + }$ and the associated covariance matrix $P _ { i - 1 } ^ { + }$ may then be propagated to the time $t _ { i }$ of the most recent measurement:

![](images/6b964319fe898c2cc1bec341c484adcf6080e408d0d3b6383553b844f00abab3.jpg)  
Fig. 8.7. The linearized Kalman filter (LKF) refers all measurements and state corrections to a common reference trajectory. Initially, when the covariance is still small, the filter output closely matches the observations (shaded circles). Later on, the filter approaches the true trajectory and becomes less sensitive to new data. Due to the increasing difference between the reference state and the estimated trajectory the filter output may become erroneous in case of non-linearities.

$$
\begin{array} { r c l } { { { \pmb x } _ { i } ^ { - } } } & { { = } } & { { { \pmb x } _ { i } ^ { \mathrm { r e f } } + { \pmb \phi } _ { i } ( { \pmb x } _ { i - 1 } ^ { + } - { \pmb x } _ { i - 1 } ^ { \mathrm { r e f } } ) } } \\ { { { \pmb P } _ { i } ^ { - } } } & { { = } } & { { { \pmb \phi } _ { i } { \pmb P } _ { i - 1 } ^ { + } { \pmb \phi } _ { i } ^ { T } . } } \end{array}
$$

The subsequent measurement update phase comprises the computation of the Kalman gain as well the state and covariance update:

$$
\begin{array} { l c l } { { { \cal K } _ { i } } } & { { = } } & { { { \cal P } _ { i } ^ { - } G _ { i } ^ { T } ( W _ { i } ^ { - 1 } + G _ { i } { \cal P } _ { i } ^ { - } G _ { i } ^ { T } ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { { \bf x } _ { i } ^ { + } } } & { { = } } & { { { \bf x } _ { i } ^ { - } + { \cal K } _ { i } \left( z _ { i } - g _ { i } ( x _ { i } ^ { \mathrm { r e f } } ) - G _ { i } ( x _ { i } ^ { - } - x _ { i } ^ { \mathrm { r e f } } ) \right) } } \\ { { } } & { { } } & { { { \cal P } _ { i } ^ { + } } } \\ { { } } & { { = } } & { { ( { \bf 1 } - { \cal K } _ { i } G _ { i } ) { \cal P } _ { i } ^ { - } . } } \end{array}
$$

The filter starts with ${ \pmb x } _ { 0 } ^ { + } = { \pmb x } _ { 0 } ^ { \mathrm { r e f } }$ and $P _ { 0 } ^ { + } = P _ { 0 } ^ { \mathrm { r e f } }$

# 8.3.3 Extended Kalman Filter

The sequential processing of a given set of measurements corresponds essentially to a single iteration of the least-squares estimation method. For a successful application of the basic Kalman filter the deviations between the reference state and the estimated state must therefore be small enough to neglect any non-linearities in the system dynamics and the measurement modeling. In order to avoid this restriction and make full use of the advantages of sequential estimation for orbit determination purposes the Extended Kalman Filter has been developed (Fig. 8.8). It may be derived from the basic Kalman filter by resetting the reference state ${ \boldsymbol { x } } _ { i - 1 } ^ { \mathrm { r e f } }$ to the estimate $\boldsymbol x _ { i - 1 } ^ { + }$ at the start of each step.

The time update phase of the extended filter thus comprises the propagation of the previous estimate $\pmb { x } _ { i - 1 } ^ { + }$ from $t _ { i - 1 }$ to $t _ { i }$ and the simultaneous solution of the variational equations for the state transition matrix. As a result one obtains the predicted state vector $\boldsymbol { x } _ { i } ^ { - }$ and the associated covariance matrix ${ P } _ { i } ^ { - }$ :

![](images/b45850fa5ef4ea2beb38ef38521b927815e74bb11550501458dd8d84e58a2f0f.jpg)  
Fig. 8.8. The extended Kalman filter (EKF) makes use of the latest estimate to propagate the state vector and the state transition matrix. This makes the EKF less sensitive to non-linearities than the linearized Kalman filter.

$$
\begin{array} { r c l } { { { \pmb x } _ { i } ^ { - } } } & { { = } } & { { { \pmb x } ( t _ { i } ; { \pmb x } ( t _ { i - 1 } ) = { \pmb x } _ { i - 1 } ^ { + } ) } } \\ { { { \pmb P } _ { i } ^ { - } } } & { { = } } & { { { \pmb \phi } _ { i } { \pmb P } _ { i - 1 } ^ { + } { \pmb \phi } _ { i } ^ { T } . } } \end{array}
$$

The measurement update phase remains the same as for the basic Kalman filter, except for the simplified state update equation:

$$
\begin{array} { r c l } { { { \bf { \cal K } } _ { i } } } & { { = } } & { { P _ { i } ^ { - } { \bf { \cal G } } _ { i } ^ { T } ( W _ { i } ^ { - 1 } + { \cal G } _ { i } P _ { i } ^ { - } { \bf { \cal G } } _ { i } ^ { T } ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { { \bf { \cal x } } _ { i } ^ { + } } } & { { = } } & { { { \bf { \cal x } } _ { i } ^ { - } + { \cal K } _ { i } \left( z _ { i } - { \bf g } _ { i } ( { \bf x } _ { i } ^ { - } ) \right) } } \\ { { } } & { { } } & { { { \bf P } _ { i } ^ { + } ~ = ~ ( { \bf 1 } - { \cal K } _ { i } { \bf G } _ { i } ) { \cal P } _ { i } ^ { - } ~ . } } \end{array}
$$

The filter starts with x0 = xap and $\mathbf { \mathit { P } } _ { 0 } = \mathbf { \mathit { P } } _ { 0 } ^ { \mathrm { a p r } }$ P apr0 . Due to the regular update of the reference state non-linearities are reduced to a minimum and within a few steps the filter may arrive at a solution that would otherwise require multiple iterations.

Some price has to be paid, however, for the improved performance of the extended Kalman filter that results from an increased computational effort for the state and covariance propagation. When using the same reference orbit for the processing of all measurements in the basic Kalman filter, only one initial value problem has to be solved by numerical integration. The reference state and state transition matrix at the time of a particular measurement can then be obtained by interpolation independent of the stepsize control employed for the integration. In case of the extended filter a separate initial value problem has to be solved for each measurement to be processed, and the required restart of the integration method may then result in a considerable increase in computing time. Typically, low-order single-step integration methods like the 4th-order Runge–Kutta scheme are therefore employed in real-time orbit determination programs based on extended Kalman filters.

# 8.3.4 Factorization Methods

As with the batch least-squares method the performance of a Kalman filter may deteriorate considerably under certain conditions unless special care is taken to reduce the impact of numerical errors in the computation. The problem is more serious, however, in case of the Kalman filter, since it must often be implemented in single precision arithmetic to speed up the computation in real-time or on-board applications.

A simple, but efficient method of coping with these difficulties consists of using the Joseph algorithm (Bucy & Joseph 1968) for the update of the covariance matrix. Since the covariance $P _ { i }$ becomes smaller and smaller as new observations are processed, round-off errors in the update formulas

$$
{ \pmb P } _ { i } ^ { + } = ( { \bf 1 } - { \pmb K } _ { i } { \pmb G } _ { i } ) { \pmb P } _ { i } ^ { - }
$$

may ultimately result in a matrix with small negative or zero eigenvalues, which does not represent the true covariance matrix anymore and leads to a failure of the filtering algorithm. Rewriting the update formula as

$$
\begin{array} { l l l } { { { \pmb P } _ { i } ^ { + } } } & { { = } } & { { ( { \bf 1 } - K _ { i } { \pmb G } _ { i } ) { \pmb P } _ { i } ^ { - } } } \\ { { } } & { { = } } & { { ( { \bf 1 } - K _ { i } { \pmb G } _ { i } ) { \pmb P } _ { i } ^ { - } - { \pmb P } _ { i } ^ { + } { \pmb G } _ { i } ^ { T } { \pmb K } _ { i } ^ { T } + { \pmb P } _ { i } ^ { + } { \pmb G } _ { i } ^ { T } { \pmb K } _ { i } ^ { T } } } \\ { { } } & { { = } } & { { ( { \bf 1 } - K _ { i } { \pmb G } _ { i } ) { \pmb P } _ { i } ^ { - } ( { \bf 1 } - K _ { i } { \pmb G } _ { i } ) { \ o { \cal T } } + { \pmb P } _ { i } ^ { + } { \pmb G } _ { i } ^ { T } { \pmb K } _ { i } ^ { T } } } \end{array}
$$

and making use of $\pmb { K } _ { i } = \pmb { P } _ { i } ^ { + } \pmb { G } _ { i } ^ { T } \pmb { W } _ { i }$ one may, however, obtain an alternative update formula

$$
P _ { i } ^ { + } = ( { \bf 1 } - K _ { i } G _ { i } ) P _ { i } ^ { - } ( { \bf 1 } - K _ { i } G _ { i } ) ^ { T } + K _ { i } W _ { i } ^ { - 1 } K _ { i } ^ { T } ~ ,
$$

which ensures that ${ { { { \cal P } } } } _ { i } ^ { + }$ is always positive definite irrespective of errors in $K _ { i }$ or $\mathbf { 1 } - \pmb { K } _ { i } \pmb { G } _ { i }$ . With minor modifications the stabilized update, which has here been derived for the extended Kalman filter, may equally well be applied to other forms of recursive and sequential estimators.

Further methods, which are more closely related to techniques employed for a numerical stable solution of the least-squares problem, make use of an appropriate factorization of the covariance matrix (or information matrix). By updating the factorization instead of the covariance matrix an annihilation of near-equal numbers is avoided and the filter becomes less sensitive to round-off errors. Single precision arithmetic may then be used to obtain an accuracy that would otherwise require twice the word length.

The square root factorization method due to Potter and Andrews (see Battin 1987, Bierman 1977) utilizes a factorization of the form

$$
{ \pmb P } _ { i } = { \pmb S } _ { i } { \pmb S } _ { i } ^ { T }
$$

and replaces the update formula for $\mathbf { \nabla } P _ { i }$ by an update formula for its square root $\boldsymbol { S } _ { i }$ . An equally stable but computationally more efficient method is the $U D U ^ { T }$ -Filter developed by Bierman (1977), which makes use of a factorization into an upper triangular matrix $U$ and a diagonal matrix $\pmb { D }$ .

Further details and reviews of various types of square root filters and factorization methods for sequential estimation are given in Kaminsky et al. (1971) and Bierman (1977). As regards the computer performance and resource requirements, factorization methods have been shown to be fully compatible with simple formulations of the Kalman filter provided that they are coded in an optimal way (cf. Bierman 1977, Campbell et al. 1983). For practical applications the use of advanced Kalman filter implementations is considerably facilitated by appropriate software libraries (see e.g. Bierman & Bierman 1984, Branyon et al. 1988).

# 8.3.5 Process Noise

A phenomenon that is likely to occur in the practical application of a Kalman filter is the filter’s divergence from the actual solution after processing a certain amount of data. Initially, the state uncertainty and the corresponding covariance matrix is sufficiently high to allow an appropriate correction of the state vector with each new observation. As more and more measurements are processed, however, both the covariance matrix and the Kalman gain approach zero, which may ultimately inhibit further improvements of the state vector. Any errors that arise from small nonlinearities, round-off errors or simplifications of the force and measurement model will then be propagated without further correction by subsequent measurements and result in an erroneous and diverging state estimate.

A possible way of coping with this problem consists of adding a small noise term to the covariance matrix in each step that inhibits the matrix from getting smaller and smaller. The method arises from the concept of process noise, which affects the system dynamics in much the same way as the measurement noise affects the observations. The differential equation describing the evolution of the state vector is supplemented by a term $\pmb { u } ( t )$ to represent stochastic modeling errors inherent in the description of the dynamical system:

$$
\dot { \pmb { x } } = \pmb { f } ( t , \pmb { x } ) + \pmb { u } ( t ) \quad .
$$

As an approximation of the actual modeling errors, $\pmb { u } ( t )$ is assumed to be a random variable with mean value

$$
\begin{array} { r } { \mathrm { E } ( \pmb { u } ( t ) ) = \pmb { 0 } } \end{array}
$$

and covariance

$$
\begin{array} { r } { \mathrm { E } ( { \pmb u } ( t ) { \pmb u } ( t ^ { \prime } ) ) = \pmb { Q } ( t ) \delta ( t - t ^ { \prime } ) ~ . } \end{array}
$$

The covariance may be time-dependent, but no time correlation is assumed to exist as expressed by the Dirac delta function $\delta ( t - t ^ { \prime } )$ . Frequently, the latter property is expressed by the term white noise in contrast to colored noise which exhibits a correlation in time.

Since the expected value of the process noise is zero, it does not affect the orbit on the average. The state estimate may therefore be propagated as usual by solving the equation of motion without consideration of the noise term. The covariance propagation formula is modified, however, to account for an increased state uncertainty due to the presence of process noise. Since each time interval $[ t , t { + } d t ]$ within $t _ { i - 1 }$ and $t _ { i }$ gives rise to a contribution $Q ( t ) d t$ to the covariance at time $t$ , the predicted covariance at $t _ { i }$ is given by

$$
P _ { i } ^ { - } = \Phi ( t _ { i } , t _ { i - 1 } ) P _ { i - 1 } ^ { + } \Phi ^ { T } ( t _ { i } , t _ { i - 1 } ) + \int _ { t _ { i - 1 } } ^ { t _ { i } } \Phi ( t _ { i } , t ) \mathcal { Q } ( t ) \Phi ^ { T } ( t _ { i } , t ) d t \quad ,
$$

where the integral can be obtained analytically for simple dynamical systems (Brown & Hwang 1997). Alternatively, the matrix differential equation

$$
\frac { d \boldsymbol { P } ( t ) } { d t } = \left( \frac { \partial \boldsymbol { f } } { \partial \boldsymbol { x } } \right) \boldsymbol { P } ( t ) + \boldsymbol { P } ( t ) \left( \frac { \partial \boldsymbol { f } } { \partial \boldsymbol { x } } \right) ^ { T } + \boldsymbol { Q } ( t )
$$

with initial conditions $P ( t _ { i - 1 } ) = P _ { i - 1 } ^ { + }$ is integrated along with the state vector in the continuous discrete Kalman filter to obtain continuous covariance information between the measurement updates (see. e.g. Halain et al. 1998).

If $\varrho$ does not depend on $t$ and if the interval between subsequent measurements is small enough to neglect deviations of the state transition matrix from unity, the covariance propagation may further be simplified yielding

$$
{ \pmb P } _ { i } ^ { - } = \pmb \phi ( t _ { i } , t _ { i - 1 } ) { \pmb P } _ { i - 1 } ^ { + } \pmb \phi ^ { T } ( t _ { i } , t _ { i - 1 } ) + \pmb Q \left( t _ { i } - t _ { i - 1 } \right) .
$$

The $Q$ -matrix thus contributes to an increase of the covariance in each step and can be used to balance the subsequent decrease due to the processing of a measurement.

Taking into account process noise gives the filter a fading memory characteristics, which means that past observations have a gradually decreasing effect on the state estimate. By increasing the $Q$ -matrix, both the covariance and the Kalman gain increase, thus making the filter more sensitive to new observations. A small value of the $Q$ -matrix is necessary, on the other hand, to avoid large state corrections in the event of erroneous observations. In practical applications the $Q$ -matrix may be determined by simulations in order to find a proper balance between process and measurement noise and ensure an optimum filter performance.

An alternative approach has been developed by Wright (1981), which builds a covariance based on physical models of error contributions such as drag, gravity, and propulsion system performance as well as measurement characteristics. This technique is particularly robust and overcomes problems encountered in the traditional modeling of process noise.

# 8.4 Comparison of Batch and Sequential Estimation

As has been pointed out in the introduction, the common estimation techniques employed for orbit determination purposes are closely related to each other and a smooth transition is possible from the batch least-squares method to the various forms of Kalman filter. Each type of estimator has inherent advantages and disadvantages and a trade-off is usually required to select the most suitable estimation method for a particular application:

Measurement processing and state correction: The classic batch least-squares method computes the epoch state estimate after processing the full set of observations. If improved epoch state estimates are required after each measurement, a formulation involving Givens rotations or the recursive least-squares method may be used. The Kalman filter in contrast processes a single scalar or vector measurement at a time and yields sequential state estimates at the measurement times.

• Treatment of non-linearities: Due to the non-linear relation between the epoch state vector and the modeled measurements, multiple iterations are required in the least-squares method to compute a state estimate that actually minimizes the loss function. Using the extended Kalman filter these iterations may in general be avoided, since the reference solution is changed with each observation. Problems are more likely, however, in the case of large deviations between the a priori state and the actual state as well as poor management of the covariance.

Computer implementation: When using a Kalman filter for orbit determination there is no need for storing measurements from previous time steps. Storage requirements are therefore smaller than for the least-squares method, in which various data have to be stored for subsequent iterations.

Numerical stability: Both filters and least-squares estimators may be subject to numerical problems in the case of bad observability as indicated by an ill-conditioned normal equations matrix or covariance matrix. Numerically stable algorithms employing different types of matrix factorizations are available, however, for both estimation techniques. The increase in computing effort and storage requirement is generally negligible and the stabilized algorithms can therefore be recommended for most applications.

Divergence: A divergence of the least-squares solution from one iteration to the next may occur in rare instances of bad observability, a bad initial state estimate and high non-linearities. All of these could also cause a Kalman filter to diverge. In addition divergence of the state estimate from the true solution is likely to occur in a Kalman filter, when the covariance becomes small and the filter gets insensitive to new observations. Process noise may be incorporated into the filter to avoid divergence but heuristic assumptions and simulations are often required to determine the appropriate noise model for a particular situation, unless a physical description of the process noise density matrix is available.

Process noise: A unique feature of Kalman filters as compared to the leastsquares method is the incorporation of process noise into the estimation process. Aside from being required to avoid filter divergence problems, it may be employed to get more realistic covariance predictions in the presence of unmodeled accelerations. Furthermore, it may be used to reduce the influence of past observations on the state estimate as compared to more recent observations.

Influence of bad data points: The batch estimator and the recursive leastsquares method process all data points using a common reference trajectory. This facilitates the handling of bad data points, which may be recognized by residuals that are considerably larger than the average value. In general the least-squares technique is therefore more robust and easier to handle than the Kalman filter. The latter requires a careful balancing between a priori covariance, measurement weighting and process noise to allow a rejection of bad data points. For example, a $Q$ -matrix, which is too large, will allow larger measurement errors to be accepted. One which is too small may allow good measurements to be rejected.

Traditional applications in which Kalman filters are preferred to batch least-squares techniques include the on-board navigation of manned or unmanned spacecraft requiring a real-time state estimate (Battin & Levine 1970). Filtering techniques are, furthermore, used in the field of interplanetary orbit determination and navigation. By incorporating appropriate process noise, unmodeled statistical accelerations due to attitude thruster activities or radiation pressure modeling simplifications may be accounted for, which provides more realistic estimates of the injection error near the target planet (Campbell et al. 1983).

The batch least-squares method on the other hand is commonly employed for off-line orbit determination of Earth-bound satellites (Long et al. 1989, Soop 1983) and for the estimation of geodetic parameters from satellite orbits (McCarthy et al. 1993). A comparison indicating a good agreement of orbit determination results from precision batch least-squares and sequential estimation programs (GTDS, RTOD/E) for satellites tracked by the Tracking Data and Relay Satellite System (TDRSS) has recently been established by a study conducted on behalf of the Goddard Space Flight Center (Oza et al. 1992). Similar conclusions have been obtained by Halain et al. (1998) for single and multi-station tracking of geostationary satellites.

# Exercises

Exercise 8.1 (Givens Rotations) The following sequence of measurements $z _ { i }$ of a physical quantity $z ( t )$ has been collected at non-equidistant times $t _ { i }$ :

$$
\begin{array} { c c c c c c c c c c c c } { i } & { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 5 } & { 6 } \\ { t _ { i } } & { 0 . 0 4 } & { 0 . 3 2 } & { 0 . 5 1 } & { 0 . 7 3 } & { 1 . 0 3 } & { 1 . 4 2 } & { 1 . 6 0 } \\ { z _ { i } } & { 2 . 6 3 } & { 1 . 1 8 } & { 1 . 1 6 } & { 1 . 5 4 } & { 2 . 6 5 } & { 5 . 4 1 } & { 7 . 6 7 } \end{array}
$$

From a graphical representation of the measurements a quadratic relation between $z$ and $t$ may be suspected. Employ a least-squares estimation with Givens rotations to adjust a second-order polynomial

$$
\boldsymbol { z } ( t ) = \boldsymbol { c } _ { 0 } + \boldsymbol { c } _ { 1 } \cdot t + \boldsymbol { c } _ { 2 } \cdot t ^ { 2 }
$$

to the data points (adopted from Schwarz 1988).

Solution: Inserting the measurement $z _ { i }$ and times $t _ { i }$ into (8.121) yields an overdetermined linear system of equations $\boldsymbol { A } \boldsymbol { x } = \boldsymbol { b }$ with

$$
A = \left( \begin{array} { l l l l } { 1 . 0 } & { 0 . 0 4 } & { 0 . 0 0 1 6 } \\ { 1 . 0 } & { 0 . 3 2 } & { 0 . 1 0 2 4 } \\ { 1 . 0 } & { 0 . 5 1 } & { 0 . 2 6 0 1 } \\ { 1 . 0 } & { 0 . 7 3 } & { 0 . 5 3 2 9 } \\ { 1 . 0 } & { 1 . 0 3 } & { 1 . 0 6 0 9 } \\ { 1 . 0 } & { 1 . 4 2 } & { 2 . 0 1 6 4 } \\ { 1 . 0 } & { 1 . 6 0 } & { 2 . 5 6 0 0 } \end{array} \right) \qquad x = \left( \begin{array} { l } { c _ { 0 } } \\ { c _ { 1 } } \\ { c _ { 2 } } \\ { c _ { 2 } } \end{array} \right) \qquad b = \left( \begin{array} { l } { 2 . 6 3 } \\ { 1 . 1 8 } \\ { 1 . 1 6 } \\ { 1 . 5 4 } \\ { 2 . 6 5 } \\ { 5 . 4 1 } \\ { 7 . 6 7 } \end{array} \right) \quad .
$$

Upon processing each individual data equation using Givens rotations, the following values for the square-root information matrix $\pmb { R }$ and the transformed measurement vector $\mathbf { \Delta } _ { d }$ are obtained:

$$
\begin{array} { r l r } { R _ { 0 } } & { = ( \begin{array} { c c } { + 1 . 0 0 0 0 0 + 0 . 6 4 0 0 + 0 . 0 0 1 6 } \\ { 0 . 0 0 0 0 + 0 . 0 0 0 0 + 0 . 0 0 0 0 } \\ { + 0 . 0 0 0 0 0 + 0 . 0 0 0 0 + 0 . 0 0 0 0 } \end{array} ) } & { d _ { 0 } = ( \begin{array} { c c } { + 2 . 6 3 0 0 } \\ { + 0 . 0 0 0 0 } \\ { + 0 . 0 0 0 0 } \\ { + 0 . 0 0 0 0 } \end{array} ) } & \\ { R _ { 1 } } & { = ( \begin{array} { c c } { + 1 . 0 4 0 4 0 + 0 . 0 0 5 6 + 0 . 0 0 3 6 } \\ { + 0 . 0 0 0 0 + 0 . 1 9 8 6 + 0 . 0 7 1 5 } \\ { + 0 . 0 0 0 0 0 + 0 . 1 9 8 6 + 0 . 0 7 1 5 } \end{array} ) } & { d _ { 1 } = ( \begin{array} { c c } { + 2 . 6 9 4 1 1 } \\ { - 1 . 0 2 5 5 } \\ { - 1 . 0 2 5 } \\ { + 0 . 0 0 0 0 } \end{array} ) } & \\ { R _ { 2 } } & { = ( \begin{array} { c c } { + 1 . 7 5 2 1 + 0 . 5 0 2 3 + 0 . 2 1 0 0 } \\ { + 0 . 0 0 0 0 + 0 . 3 3 4 0 + 0 . 0 7 1 2 } \\ { + 0 . 0 0 0 0 + 0 . 0 0 0 2 } \end{array} ) } & { d _ { 2 } = ( \begin{array} { c c } { + 2 . 6 9 6 4 1 } \\ { - 1 . 0 4 7 8 } \\ { - 0 . 0 0 0 0 } \end{array} ) } & \\ { R _ { 3 } } & { = ( \begin{array} { c c } { + 2 . 0 0 1 1 4 0 + 0 . 6 0 0 1 + 0 . 3 4 8 8 } \\ { + 0 . 0 0 0 1 4 0 + 0 . 5 7 0 7 + 0 . 3 8 6 0 } \\ { + 0 . 0 0 0 0 + 0 . 5 7 0 7 } \\ { + 0 . 0 0 0 0 + 0 . 0 0 0 0 + 0 . 1 0 9 } \end{array} ) } & { d _ { 3 } = ( \begin{array} { c c } { + 3 . 2 5 9 } \\ { + 0 . 0 8 8 0 } \\ { + 0 . 0 5 9 1 } \\ { + 0 . 8 8 0 } \end{array} ) } \\ { R _ { 5 } } &  = ( \begin{array} { c c }  + 2 . 6 1 0 + 0 . 7 8 7 + 2 . \end{array} \end{array}
$$

Using backsubstitution, one finally obtains the solution:

$$
{ \binom { c _ { 0 } } { c _ { 1 } } } = R _ { 6 } ^ { - 1 } d _ { 6 } = { \binom { + 2 . 7 4 9 1 9 8 } { - 5 . 9 5 4 6 5 7 } }
$$

Exercise 8.2 (Least-Squares Orbit Determination) The Bangalore ground station, located in India at $\pmb { R } = ( + 1 3 4 4 . 0$ , $+ 6 0 6 9 . 0$ , 1429.0) km, has collected six sets of range and angle tracking data of a telecommunications satellite in geostationary transfer orbit:

<table><tr><td>Date</td><td>UTC</td><td>A[]</td><td>E[]</td><td>p[km]</td></tr><tr><td>1995/03/30</td><td>00:20:00.0</td><td>196.280</td><td>49.179</td><td>6606.330</td></tr><tr><td>1995/03/30</td><td>00:40:00.0</td><td>148.760</td><td>55.273</td><td>11459.583</td></tr><tr><td>1995/03/30</td><td>01:00:00.0</td><td>133.129</td><td>53.164</td><td>15939.297</td></tr><tr><td>1995/03/30</td><td>01:20:00.0</td><td>126.894</td><td>52.313</td><td>19747.028</td></tr><tr><td>1995/03/30</td><td>01:40:00.0</td><td>124.077</td><td>52.575</td><td>22978.426</td></tr><tr><td>1995/03/30</td><td>02:00:00.0</td><td>122.943</td><td>53.574</td><td>25728.145</td></tr></table>

According to the launcher agency, the nominal position and velocity with respect to the Earth equator and equinox are given by

$$
\begin{array} { r c l } { { \pmb r ( t _ { 0 } ) } } & { { = } } & { { ( - 6 3 3 5 . 0 , \quad - 3 7 2 8 . 0 , \quad - 5 7 9 . 0 ) \mathrm { k m } } } \\ { { \pmb v ( t _ { 0 } ) } } & { { = } } & { { ( + 2 . 1 6 8 0 , \quad - 9 . 2 6 3 0 , \quad - 1 . 0 7 9 5 ) \mathrm { k m / s } } } \end{array}
$$

at the time $t _ { 0 } = 1 9 9 5 / 0 3 / 3 0 0 0 { : } 0 0 1$ UTC of injection. Determine the achieved injection state from the above observations using a batch least-squares fit. How many iterations are required and how accurate is your result, assuming that the standard deviation of the measurements amounts to $\sigma _ { \mathrm { A } } = 0 . 0 1 ^ { \circ } \cdot \cos ( E )$ , $\sigma _ { \mathrm { E } } = 0 . 0 1 ^ { \circ }$ and $\sigma _ { \rho } = 1 0 \mathrm { m } ?$

Hint: The above observations match a Keplerian orbit with epoch state vector

$$
\begin{array} { r c l } { { \pmb r ( t _ { 0 } ) } } & { { = } } & { { ( - 6 3 4 5 . 0 , \quad - 3 7 2 3 . 0 , \quad - 5 8 0 . 0 ) \mathrm { k m } } } \\ { { \pmb v ( t _ { 0 } ) } } & { { = } } & { { ( + 2 . 1 6 9 0 , \quad - 9 . 2 6 6 0 , \quad - 1 . 0 7 9 0 ) \mathrm { k m / s } } } \end{array}
$$

neglecting precession, nutation, UT1-UTC, light time and refraction. The same model is recommended for the orbit determination process.

Solution: The following residuals are obtained in the first and second iteration:

<table><tr><td colspan="5">1st Iteration</td><td colspan="3">2nd Iteration</td></tr><tr><td>Date</td><td>UTC</td><td>A[]</td><td>E[]</td><td>p[m]</td><td>A[]</td><td>E[]</td><td>p[m]</td></tr><tr><td>1995/03/30</td><td>00:20:00.0</td><td>0.100</td><td>-0.002</td><td>5479.1</td><td>0.001</td><td>0.002</td><td>-4.5</td></tr><tr><td>1995/03/30</td><td>00:40:00.0</td><td>0.063</td><td>0.044</td><td>14250.5</td><td>-0.001</td><td>0.001</td><td>0.8</td></tr><tr><td>1995/03/30</td><td>01:00:00.0</td><td>0.055</td><td>0.063</td><td>28320.9</td><td>-0.001</td><td>0.001</td><td>10.0</td></tr><tr><td>1995/03/30</td><td>01:20:00.0</td><td>0.065</td><td>0.081</td><td>45272.4</td><td>-0.001</td><td>0.000</td><td>24.7</td></tr><tr><td>1995/03/30</td><td>01:40:00.0</td><td>0.083</td><td>0.100</td><td>64708.7</td><td>-0.001</td><td>0.000</td><td>43.7</td></tr><tr><td>1995/03/30</td><td>02:00:00.0</td><td>0.108</td><td>0.120</td><td>86542.9</td><td>-0.000</td><td>0.000</td><td>66.1</td></tr></table>

Thereafter, all residuals vanish to the given number of digits. Likewise, the a priori state vector is corrected to the final value within two iterations:

<table><tr><td>Parameter</td><td>A priori</td><td>A1</td><td>Δ2</td><td>Final</td><td>0</td></tr><tr><td>x [m]</td><td>-6335000.0</td><td>-9946.9</td><td>-53.1</td><td>-6345000.0</td><td>276.9</td></tr><tr><td>y[m]</td><td>-3728000.0</td><td>5188.3</td><td>-188.3</td><td>-3723000.0</td><td>737.0</td></tr><tr><td>z[m]</td><td>-579000.0</td><td>-1124.8</td><td>124.8</td><td>-580000.0</td><td>829.8</td></tr><tr><td>x[m/s]</td><td>2168.0000</td><td>0.8918</td><td>0.1082</td><td>2169.0000</td><td>0.6520</td></tr><tr><td>y[m/s]</td><td>-9263.0000</td><td>-3.0983</td><td>0.0983</td><td>-9266.0000</td><td>0.5226</td></tr><tr><td>z[m/s]</td><td>-1079.5000</td><td>0.3216</td><td>0.1784</td><td>-1079.0000</td><td>0.3695</td></tr></table>

The standard deviation of the achieved estimate amounts to roughly $1 \mathrm { k m }$ in position and $1 \mathrm { m / s }$ in velocity.

Exercise 8.3 (Orbit Determination by Extended Kalman Filter) Process the measurements and auxiliary data given in Exercise 8.2 in an extended Kalman filter to determine the spacecraft state vector at the time of each measurement. To initialize the filter, assume an a priori standard deviation of $1 0 \mathrm { k m }$ viz. $1 0 \mathrm { m / s }$ in each axis. Compute the position and velocity error with respect to the true Keplerian orbit after each time and measurement update and compare your results with the standard deviation obtained from the diagonal elements of the covariance matrix.

Hint: Instead of processing the simultaneous azimuth, elevation and range measurements in a three-dimensional vector update of the Kalman filter, three consecutive scalar updates can be employed. This saves the need for a three-dimensional matrix inversion in the computation of the Kalman gain.

Solution: The uncertainty of the epoch state vector propagates into a $3 0 \mathrm { k m }$ and $2 4 \mathrm { m } / \mathrm { s }$ standard deviation of position and velocity at the time of the first measurement. Because the combination of two angle measurements and a range measurement provides a three-dimensional position fix, the position uncertainty is decreased to less than $2 \mathrm { k m }$ after processing the first set of observations. The velocity knowledge, on the other hand, is only improved after processing the next data set. Due to the absence of measurement and model errors in the given example, the filter finally achieves an actual accuracy in the range of $1 0 0 \mathrm { m }$ and $1 { - } 1 0 \mathrm { c m } / \mathrm s$ , which may be compared to the statistical uncertainties of $3 \ \mathrm { k m }$ and $0 . 5 \mathrm { m } / \mathrm { s }$ .

<table><tr><td colspan="4"></td><td colspan="2">σ(lrl)</td><td>σ(lv|)</td></tr><tr><td>Date</td><td>UTC</td><td>Update</td><td>△|rl [m]</td><td>[m/s]</td><td>△| [m]</td><td>[m/s]</td></tr><tr><td>1995/03/30</td><td>00:20:00.0</td><td>t</td><td>9321.4</td><td>29905.8</td><td>10.2672</td><td>24.0682</td></tr><tr><td rowspan="6">1995/03/30</td><td rowspan="6">00:40:00.0</td><td>A</td><td>1113.8</td><td>22177.0</td><td>8.3429</td><td>19.8879</td></tr><tr><td>E</td><td>498.8</td><td>18155.2</td><td>8.6497</td><td>18.8681</td></tr><tr><td>p</td><td>44.2</td><td>1623.6</td><td>8.5132</td><td>12.2137</td></tr><tr><td>t</td><td>10320.2</td><td>14727.9</td><td>8.9699</td><td>12.1528</td></tr><tr><td>A</td><td>6599.9</td><td>12044.8</td><td>5.9084</td><td>10.1173</td></tr><tr><td>E</td><td>5786.9 237.5</td><td>8548.2 2713.7</td><td>5.3129 0.3564</td><td>7.7209</td></tr><tr><td>1995/03/30</td><td>p 01:00:00.0 t</td><td></td><td></td><td></td><td></td><td>2.5002</td></tr><tr><td rowspan="6">1995/03/30</td><td></td><td>A</td><td>646.0</td><td>5338.6</td><td>0.3368</td><td>2.2941</td></tr><tr><td>E</td><td></td><td>292.4</td><td>4435.5</td><td>0.1985</td><td>1.9658</td></tr><tr><td></td><td></td><td>275.6</td><td>3256.8</td><td>0.1939</td><td>1.5474</td></tr><tr><td>01:20:00.0</td><td>p</td><td>66.7 98.3</td><td>2767.3 3924.7</td><td>0.0318 0.0297</td><td>1.1352</td></tr><tr><td>t</td><td></td><td>100.2</td><td>3642.8</td><td></td><td>1.0344</td></tr><tr><td></td><td>A</td><td></td><td></td><td>0.0315</td><td>0.9723</td></tr><tr><td rowspan="5">1995/03/30</td><td></td><td>E</td><td>62.6</td><td>2979.8</td><td>0.0201</td><td>0.8003</td></tr><tr><td>01:40:00.0</td><td>p</td><td>61.1</td><td>2969.9</td><td>0.0191</td><td>0.7867</td></tr><tr><td>t</td><td></td><td>80.1</td><td>3779.6</td><td>0.0178</td><td>0.7179</td></tr><tr><td>A</td><td></td><td>80.7</td><td>3556.2</td><td>0.0186</td><td>0.6812</td></tr><tr><td>E</td><td></td><td>57.2</td><td>3094.4</td><td>0.0135</td><td>0.5955</td></tr><tr><td rowspan="5">1995/03/30</td><td>02:00:00.0</td><td>p</td><td>56.1</td><td>3087.9</td><td>0.0125</td><td>0.5862</td></tr><tr><td></td><td>t</td><td>68.7</td><td>3696.8</td><td>0.0117</td><td>0.5349</td></tr><tr><td>A</td><td></td><td>68.8</td><td>3513.9</td><td>0.0121</td><td>0.5113</td></tr><tr><td>E</td><td></td><td>52.2</td><td>3159.3</td><td>0.0093</td><td>0.4608</td></tr><tr><td>p</td><td></td><td>52.3</td><td>3153.0</td><td>0.0089</td><td>0.4571</td></tr></table>

# 9. Applications

The presentation of statistical estimation methods given in the previous chapter forms the final building block in the derivation of fundamental models and methods for satellite orbit prediction and determination. Focus is now given to the practical aspects by discussing selected applications, each of which emphasizes certain key elements:

an Orbit Determination Error Analysis illustrates the use of consider covariance studies in the design of tracking systems for geostationary communications satellites, • a section on Real-Time Orbit Determination discusses the design and application of a dynamical Kalman filter for autonomous orbit determination based on on-board navigation measurements and, finally, concepts of satellite-satellite tracking and multi-satellite orbit adjustment are demonstrated in the section on Relay Satellite Orbit Determination.

Each section comprises a dedicated computer program, which deepens the understanding of the interaction of numerical trajectory models, measurement processing, and estimation methods in related software systems. Upon performing realistic case studies and processing real-life data, the reader should be able to collect hands-on experience and gain a better understanding of the underlying models and methods.

# 9.1 Orbit Determination Error Analysis

In the mission design of geostationary satellite projects, certain requirements on the orbit determination accuracy are commonly imposed to ensure safe and fueloptimal spacecraft control. Each satellite must be maintained within given limits of the sub-satellite longitude and latitude that have been assigned by international agreement. A minimum position knowledge is required e.g. to avoid violations of the specified deadband and to avoid proximities with other satellites. A consider covariance analysis is helpful to answer the following questions:

Can a given knowledge of the orbital elements be achieved with the planned tracking configuration?   
• What is the impact of the systematic errors in the station location or the ranging calibration onto the resulting orbit determination accuracy?   
How quickly, and to what accuracy can the orbit be recovered after a maneuver and how does the maneuver calibration uncertainty affect the evolution of the predicted spacecraft orbit?

While answers to the above questions might also be obtained from a Monte-Carlo simulation, a large number of cases would be required to obtain the desired statistical information. Using the type of orbit determination error analysis described below, results can generally be obtained much faster and with less computational effort.

![](images/0027ad1350281c4557c03fa56b701391e923986431c52605316a44e49caaf2af.jpg)  
Fig. 9.1. Motion of a satellite in the vicinity of a geostationary point

# 9.1.1 A Linearized Orbit Model

As their name implies, geostationary satellites maintain an essentially fixed position with respect to the surface of the Earth. This is made possible by inserting the spacecraft into a circular, equatorial orbit at an altitude of roughly $3 6 0 0 0 \mathrm { k m }$ . Here its mean motion matches the Earth’s rotation rate of one revolution per $2 3 ^ { \mathrm { h } } 5 6 ^ { \mathrm { m } }$ and the spacecraft thus remains fixed with respect to the surface of the Earth. While an ideal geostationary motion is prevented by the perturbations of the Earth’s aspherical gravity field, the lunisolar gravity and the solar radiation pressure, it is common practice to actively control a satellite in a box of $1 0 0 { \mathrm { - } } 1 5 0 \mathrm { k m }$ width around a nominal geostationary longitude.

Due to its special nature the actual motion of a (near-)geostationary satellite may conveniently be described in a co-rotating equatorial reference frame, which is centered at the ideal geostationary position (Fig. 9.1). The coordinates $r =$ $( x , y , z ) ^ { T }$ in this frame are related to the inertial coordinates $\hat { r }$ (as referred to the true equator and equinox) by the relation

$$
\pmb { r } = \pmb { R } _ { z } ( \Theta + \lambda _ { 0 } ) \hat { \pmb { r } } - ( a _ { 0 } , 0 , 0 ) ^ { T } .
$$

Here $\lambda _ { 0 }$ and $a _ { 0 } = 4 2 1 6 4 . 0 \mathrm { k m }$ denote the geographic longitude and the radius of the geostationary reference point.

The transformation into the rotating reference frame gives rise to Coriolis terms and centripetal accelerations, which may, however, be simplified by linearization around the circular reference orbit. The resulting equations of motion

$$
\begin{array} { l r } { { \ddot { x } - 2 n \dot { y } - 3 n ^ { 2 } x } } & { { = } } & { { a _ { x } } } \\ { { \ddot { y } + 2 n \dot { x } } } & { { = } } & { { a _ { y } } } \\ { { \ddot { z } } } & { { + } } & { { n ^ { 2 } z = a _ { z } } } \end{array}
$$

relate the coordinates $x$ (radial direction), $y$ (along-track direction), and z (crosstrack direction) to the perturbing accelerations $( a _ { x } , a _ { y } , a _ { z } )$ and are known as Hill’s equations or Clohessy–Wiltshire equations (Clohessy & Wiltshire 1960). The quantity $n$ denotes the mean motion of the reference orbit and is equal to the Earth’s rotation rate when considering the motion near a geostationary point.

In the simplifying case of unperturbed, Keplerian motion the equations can be integrated in closed form (cf. Vallado 1997). For given initial conditions $y _ { 0 } =$ $( x _ { 0 } , y _ { 0 } , z _ { 0 } , \dot { x } _ { 0 } , \dot { y } _ { 0 } , \dot { z } _ { 0 } ) ^ { T }$ the position at time $t$ after the initial epoch is given by

$$
\begin{array} { l l } { { x ( t ) = - ( 3 x _ { 0 } + 2 \dot { y } _ { 0 } / n ) \mathrm { c o s } ( n t ) + } } & { { ( \dot { x } _ { 0 } / n ) \mathrm { s i n } ( n t ) + ( 4 x _ { 0 } + 2 \dot { y } _ { 0 } / n ) } } \\ { { y ( t ) = + ( 6 x _ { 0 } + 4 \dot { y } _ { 0 } / n ) \mathrm { s i n } ( n t ) + ( 2 \dot { x } _ { 0 } / n ) \mathrm { c o s } ( n t ) } } \\ { { } } & { { - ( 6 x _ { 0 } + 3 \dot { y } _ { 0 } / n ) ( n t ) + ( y _ { 0 } - 2 \dot { x } _ { 0 } / n ) } } \\ { { z ( t ) = } } & { { ( z _ { 0 } ) \mathrm { c o s } ( n t ) + } } \end{array}
$$

As may already be recognized from the Clohessy–Wiltshire equations, the motion along the $z$ -axis (i.e. in north-south direction) is a harmonic oscillation that is completely decoupled from the motion in the $x$ -y-plane. The motion within the equatorial plane is more complex and comprises a constant offset from the geostationary reference point, a linear drift in the along-track direction $y$ -axis) and a superimposed oscillation. The latter results in an ellipse which is twice as large in the along-track direction as in the radial direction. The constant offset

$$
\varDelta a = 4 x _ { 0 } + 2 \dot { y } _ { 0 } / n
$$

in radial direction corresponds to a difference between the actual semi-major axis and the geostationary radius. It is responsible for the observed drift of

$$
a \varDelta n = - \frac { 3 } { 2 } n \varDelta a = - ( 6 n x _ { 0 } + 3 \dot { y } _ { 0 } )
$$

in the $+ y$ -direction (see (9.3)).

The above equations may be supplemented by the corresponding expressions for the velocity vector and rearranged to obtain a linear relation

$$
\mathbf { y } ( t ) = \pmb { \phi } ( t ) \mathbf { y } _ { 0 }
$$

between the instantaneous state vector $\boldsymbol { \mathbf { y } }$ and the epoch state vector $\scriptstyle { y _ { 0 } }$ . The state transition matrix $\Phi$ , which maps the initial state to the state at time $t$ , does not depend on the actual orbit and involves time-dependent terms only. It is given by the expression

$$
\Phi ( t ) = \left( \begin{array} { c c c c c c } { { 4 - 3 c } } & { { 0 } } & { { 0 } } & { { s / n } } & { { 2 ( 1 - c ) / n } } & { { 0 } } \\ { { 6 ( s - n t ) } } & { { 1 } } & { { 0 } } & { { 2 ( c - 1 ) / n } } & { { 4 s / n - 3 t } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { c } } & { { 0 } } & { { 0 } } & { { s / n } } \\ { { 3 n s } } & { { 0 } } & { { 0 } } & { { c } } & { { 2 s } } & { { 0 } } \\ { { 6 n ( c - 1 ) } } & { { 0 } } & { { 0 } } & { { - 2 s } } & { { 4 c - 3 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { - n s } } & { { 0 } } & { { 0 } } & { { c } } \end{array} \right) ,
$$

where $s$ and $c$ denote the sine and cosine of phase angle nt, respectively. Within the linearized orbit model, the motion of a (near-)geostationary satellite may conveniently be described in terms of the epoch state vector using elementary linear and harmonic functions of time. Even more, the partial derivatives with respect to the initial values are obtained at no extra cost along with the prediction of the trajectory itself.

Based on the description of the spacecraft orbit in the geostationary reference frame, one may compute the modeled observations (azimuth $A$ , elevation $E$ , and range $\rho$ ) using suitably adapted relations for the topocentric position of the satellite. For a station at longitude $\lambda = \lambda _ { 0 } + \varDelta \lambda$ , latitude $\varphi$ and Greenwich coordinates $\pmb { R }$ , the spacecraft position $\pmb { S }$ measured in the local east, north, and zenith direction is given by

$$
s ~ = ~ s _ { 0 } + E r
$$

with

$$
{ \boldsymbol { s } } _ { 0 } ~ = ~ E ~ \left( ( a _ { 0 } , 0 , 0 ) ^ { T } - R _ { z } ( \lambda _ { 0 } ) { \pmb R } \right)
$$

and

$$
{ \cal E } = \left( \begin{array} { c c c } { { - \sin \varDelta \lambda } } & { { + \cos \varDelta \lambda } } & { { 0 } } \\ { { - \sin \varphi \cos \varDelta \lambda - \sin \varphi \sin \varDelta \lambda + \cos \varphi } } \\ { { + \cos \varphi \cos \varDelta \lambda + \cos \varphi \sin \varDelta \lambda + \sin \varphi } } & { { } } \end{array} \right) .
$$

Here $\varDelta \lambda$ is the ground station longitude relative to the direction of geostationary point, which is offset from the Greenwich meridian by the angle $\lambda _ { 0 }$ . Azimuth, elevation, and range as well as the associated partial derivatives with respect to the spacecraft position in the geostationary frame are then obtained using relations presented earlier (cf. Chaps. 6 & 7).

Due to the near-constant observation geometry, the partial derivatives can be evaluated at the nominal geostationary point (i.e. $\mathbf { \nabla } \mathbf { r } = \mathbf { 0 }$ ) without sacrificing accuracy. As a consequence the partial derivatives

$$
{ \frac { \partial ( A , E , \rho ) } { \partial y _ { 0 } } } \approx \left. { \frac { \partial ( A , E , \rho ) } { \partial r } } \right| _ { r = 0 } { \frac { \partial r } { \partial y _ { 0 } } } = \left[ { \frac { \partial ( A , E , \rho ) } { \partial s _ { 0 } } } E \right] \Phi _ { 1 . . 3 , 1 . . 6 }
$$

may be factored into the product of a term that depends only on the station geometry and a second term that depends only on the measurement time with respect to initial epoch. This factorization unveils a fundamental degeneracy of the geostationary orbit determination problem, which is discussed in more detail in Soop (1983, 1994). Each component of the spacecraft position vector (9.3) and the state transition matrix (9.7) exhibits a time dependence, which is fully described by the superposition

$$
f ( t ) = f _ { 0 } + f _ { 1 } t + f _ { c } \cos ( n t ) + f _ { s } \sin ( n t )
$$

of a sinusoidal and a linear motion with corresponding parameters $f _ { i }$ . Based on the above assumption of a constant observation geometry, the variation of the measurements with time is a linear combination of state transition matrix elements.

Therefore, the general time dependence of each measurement type is also fully described by a four-parameter model comprising e.g. a sine and cosine amplitude, a drift and an offset. This is illustrated by a sample set of azimuth and elevation measurements shown in Fig. 9.2.

![](images/62ecb29b43c8928625bf292f9d5a660779954a5e26d5eb3630848d644d5e34de.jpg)  
Fig. 9.2. Sample azimuth and elevation measurements of a geostationary satellite.

Evidently, it is impossible to uniquely determine six orbital elements or state vector components from a single set of measurements that depends on four parameters only, irrespective of the length of the data arc. To cope with this problem, it is mandatory to combine different measurement types (e.g. range and angles) or to use more than one tracking station (e.g. dual station ranging) in the orbit determination of geostationary satellites. Even though the degeneracy described above is strictly valid only for the linearized orbit model, the conclusions are likewise applicable to the practice. Both perturbations and non-linearities in the true orbit model are generally insufficient to allow a well-conditioned adjustment of all orbital parameters from a single measurement type.

# 9.1.2 Consider Covariance Analysis

The orbit and measurement model derived in the previous section provides the basis for a consider covariance analysis of geostationary satellite orbit determination. In accordance with common practice, range and angle tracking from up to two ground stations is discussed in the sequel. Among the possible set of consider parameters, focus is given to measurement biases, i.e. systematic offsets of the range and angle measurements from their true values. Besides having a major impact on the achievable orbit determination accuracy, these parameters are easily treated in the error analysis due to the simple structure of the associated partial derivatives. They are thus well suited to illustrating and understanding the concepts behind more sophisticated consider covariance studies.

In total, the problem formulation comprises up to twelve parameters, including the epoch state vector $\scriptstyle { y _ { 0 } }$ as well as the biases $\varDelta A _ { 1 }$ , $\varDelta E _ { 1 }$ , $\varDelta \rho _ { 1 }$ and $\varDelta A _ { 2 } , \varDelta E _ { 2 } , \varDelta \rho _ { 2 }$ of the range and angle measurements from the first and second ground stations. The whole set may be partitioned into a vector $x$ of estimation parameters and a vector $c$ of consider parameters. As an example one might study tracking from a single station, in which the estimation parameter vector $\mathbf { \boldsymbol { x } } ^ { T } = ( \mathbf { \boldsymbol { y } } _ { 0 } ^ { T } , \varDelta A , \varDelta E )$ comprises the epoch state vector and the azimuth and elevation biases of the tracking station, whereas the range bias $\varDelta \rho$ is the only consider parameter vector.

Partial derivatives $H _ { y _ { 0 } } = \mathrm { { \partial } } \partial z / \partial y _ { 0 }$ of the measurements with respect to the epoch state vector are computed as outlined in the previous section. Biases constitute additive terms in the respective measurement equation, which e.g. takes the form

$$
z = h _ { \rho } ( \mathbf { y } _ { 0 } , t ) + \varDelta \rho + \epsilon
$$

for a range measurement. The partial derivatives $H _ { \varDelta } = \partial z / \partial \varDelta$ with respect to a bias parameter are thus equal to one if the station and type of the bias matches that of the respective measurement (e.g. $\partial A _ { 1 } / \partial \varDelta A _ { 1 } = 1 )$ but zero otherwise (e.g. $\partial A _ { 1 } / \partial \varDelta \rho _ { 1 } = 0$ , $\partial A _ { 2 } / \partial \varDelta A _ { 1 } = 0 )$ .

For an assumed tracking schedule, as defined by the time and type of each measurement as well as the applied ground station, one can thus form the partial derivatives

$$
\pmb { H } = ( \pmb { H } _ { x } , \pmb { H } _ { c } )
$$

of the full measurement vector $z$ with respect to the selected estimation vector $x$ and the consider parameters $c$ . Using these, the noise-only covariance and the consider covariance as defined in (8.41) and (8.42) can be computed for given values of the measurements weights $\sigma _ { i }$ and the consider parameter covariance $C = \mathrm { C o v } ( c , c )$ . In the practical implementation a QR decomposition is preferred, however, which is based on a sequential processing of the partial derivatives using Givens rotations (Fig. 8.6). Subject to proper ordering of the various parameters (estimation parameters first, consider parameters last), the transformation yields an upper triangular matrix

$$
Q ^ { T } ( \mathrm { d i a g } ( \sigma _ { i } ^ { - 1 } ) \cdot H ) = R = \left( \begin{array} { c c } { R _ { x x } } & { R _ { x c } } \\ { \mathbf { 0 } } & { R _ { c c } } \end{array} \right) \quad ,
$$

which, as a sub-block, contains the upper triangular square-root information matrix $\pmb { R } _ { x x }$ of the estimation parameters. Together with the rectangular sub-block $\pmb { R } _ { x c }$ , it may be used to form both the noise-only covariance

$$
\pmb { P } = \pmb { R } _ { x x } ^ { - 1 } \pmb { R } _ { x x } ^ { - T }
$$

and the consider covariance

$$
\pmb { P } ^ { \mathrm { c } } = \pmb { P } + ( \pmb { R } _ { x x } ^ { - 1 } \pmb { R } _ { x c } ) \pmb { C } ( \pmb { R } _ { x x } ^ { - 1 } \pmb { R } _ { x c } ) ^ { T } \quad .
$$

In view of its shape, the required inversion of ${ \pmb R } _ { x x }$ may again be performed by the back-substitution algorithm for triangular matrices.

For further analysis it is useful to compute the variance of the semi-major $a$ axis from the state vector covariance. Making use of (9.4) the partial derivatives of $a$ with respect to the epoch state vector are given by

$$
\partial a / \partial y _ { 0 } = ( 4 , 0 , 0 , 0 , 2 / n , 0 ) .
$$

This, finally, yields the desired variance

$$
\begin{array} { r } { \mathrm { C o v } ( a , a ) = ( \partial a / \partial \mathbf { y } _ { 0 } ) \mathrm { C o v } ( \mathbf { y } _ { 0 } , \mathbf { y } _ { 0 } ) ( \partial a / \partial \mathbf { y } _ { 0 } ) ^ { T } \quad , } \end{array}
$$

as a function of the $6 \times 6$ covariance matrix of the state vector components. In contrast to other orbital elements, errors in the semi-major axis affect the mean motion and thus give rise to secularly increasing errors in the predicted spacecraft orbit. Based on Kepler’s third law, a semi-major axis error $\varDelta a$ results in an alongtrack position offset of $3 \pi \varDelta a$ per day for a geostationary satellite. The semi-major axis variance is thus particularly important to assess the accuracy with which an orbit can be propagated based on the estimated epoch state vector.

In a similar fashion, pre- and post-multiplication with the state transition matrix yields the covariance

$$
\operatorname { C o v } ( \boldsymbol { y } ( t ) , \boldsymbol { y } ( t ) ) = \pmb { \phi } ( t ) \operatorname { C o v } ( \boldsymbol { y } _ { 0 } , \boldsymbol { y } _ { 0 } ) \pmb { \varPhi } ^ { T } ( t )
$$

of the state vector at an arbitrary epoch $t$ . Concerning the interpretation of the velocity covariance, care has to be taken of the fact that the results refer to the rotating reference system used to describe the geostationary satellite motion. In order to obtain the covariance of the inertial velocity vector $\hat { \pmb { v } }$ in the radial, alongtrack and cross-track direction, the above results have to be properly mapped using the differential relation

$$
\begin{array} { r } { \frac { \partial \hat { \pmb { y } } } { \partial \pmb { y } } = \left( \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - n } & { 0 } & { 1 } & { 0 } & { 0 } \\ { + n } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right) \quad , } \end{array}
$$

between the state vector in the inertial system and the rotating system, which is a direct consequence of (9.1).

# 9.1.3 The GEODA Program

The algorithms discussed so far are implemented in the GEODA program for orbit determination error analysis of geostationary satellites. The user may choose a combination of range and angle tracking data from up to two stations at a specified data rate. In addition to the measurement standard deviation, the standard deviation of a systematic bias may be specified for each data type. Depending on the choice of the user, biases are either treated as estimation parameters or consider parameters.

GEODA can thus be used to assess a wide range of tracking configurations and orbit determination concepts.

All input parameters are collated in the GEODA.inp file, a sample of which is reproduced below:

Subsatellite longitude [deg] -72.0   
Station 1 (lon [deg], lat [deg], alt [m]) -58.7 -34.4 0.0   
Angles (noise & bias [deg], step [h], est.bias) 0.02 0.05 0.1 1   
Range (noise & bias [m], step [h], est.bias) 2.0 20.0 3.0 0   
Station 2 (lon [deg], lat [deg], alt [m]) -64.6 +31.6 1000.0   
Angles (noise & bias [deg], step [h], est.bias) 0.02 0.05 0.0 0   
Range (noise & bias [m], step [h], est.bias) 2.0 20.0 0.0 0   
Tracking interval [h] 24.0   
Prediction interval [h] 336.0

Each line starts with a 50 character comment field describing the contents of the subsequent data. The actual input starts in column 51 and blanks are used to separate individual items. Following the input of the subsatellite longitude of the geostationary satellite, the user has to specify the geodetic coordinates and the applicable tracking types for up to two stations. Aside from the standard deviations of the measurement noise $( \sigma _ { A } , \sigma _ { E } , \sigma _ { \rho } )$ and bias $( \sigma _ { \Delta A } , \sigma _ { \Delta E } , \sigma _ { \Delta \rho } )$ the time between subsequent measurements and an estimation flag are given independently for angle tracking (azimuth and elevation) and ranging. The estimation flag is set to 1, if the respective measurement bias shall be adjusted along with the state vector component. A value of 0 indicates that the bias is treated as consider parameter with the specified uncertainty. Finally the total tracking interval and a prediction interval have to be entered. The latter one specifies the time over which predicted position and velocity uncertainties are generated by the program at discrete three-hour steps.

# 9.1.4 Case Studies

The following case studies illustrate the analysis of the achievable orbit determination performance for an Argentinian communications satellite near $7 2 ^ { \circ }$ West longitude. Two ground stations at Buenos Aires and Cordoba are considered with geodetic coordinates and assumed tracking parameters as given in Table 9.1. Various configurations are analyzed, which are based on single-station range and angle tracking as well as dual-station ranging. Special consideration is, furthermore, given to short-arc orbit determination. The full set of test cases is summarized in Table 9.2.

Table 9.1. Station parameters for GEODA case studies   

<table><tr><td>Name</td><td>入</td><td>?</td><td>h</td><td>A,E</td><td>O△A,△E</td><td>op</td><td>△p</td></tr><tr><td>BUA</td><td>-58.7°</td><td>-34.4°</td><td>0m</td><td>0.02°</td><td>0.05°</td><td>2m</td><td>20m</td></tr><tr><td>CDB</td><td>-64.6°</td><td>-31.6°</td><td>1000 m</td><td>0.02°</td><td>0.05°</td><td>2m</td><td>20m</td></tr></table>

Table 9.2. Tracking configuration for individual GEODA study cases   

<table><tr><td>Case</td><td>Description</td></tr><tr><td>A1 A2</td><td>One day of angle measurements (1/6m)and ranging(1/3h) from BUA station; bias parameters considered Same asA1,but azimuth&amp; elevation biases estimated</td></tr><tr><td>A3 B1</td><td>Same as A2,but for CDB station One day ranging (1/3h) from BUA and CDB stations; range biases considered</td></tr><tr><td>B2 C1</td><td>Same as B1,but CDB range bias estimated</td></tr><tr><td>C2</td><td>12 hours angle measurements (1/6m) and ranging(1/3om） from BUA station;angle biases estimated,range bias considered 6 hours ranging(1/3om) from BUA and CDB stations; range biases considered</td></tr></table>

Table 9.3. Epoch state vector accuracies for individual GEODA study cases   

<table><tr><td>Case</td><td>Type</td><td>0x [m]</td><td>Jy [m]</td><td>O [m]</td><td>Jx [m/s]</td><td>[m/s]</td><td>0 [m/s]</td><td>ga [m]</td></tr><tr><td rowspan="2">A1</td><td>Noise</td><td>104.0</td><td>347.0</td><td>1073.9</td><td>0.0215</td><td>0.0076</td><td>0.0785</td><td>7.8</td></tr><tr><td>Consider</td><td>170.5</td><td>4463.3</td><td>1088.4</td><td>0.3234</td><td>0.0093</td><td>0.0792</td><td>123.6</td></tr><tr><td rowspan="2">A2</td><td>Noise</td><td>104.1</td><td>368.9</td><td>1073.9</td><td>0.0234</td><td>0.0076</td><td>0.0785</td><td>8.5</td></tr><tr><td>Consider</td><td>104.1</td><td>716.6</td><td>1073.9</td><td>0.0505</td><td>0.0076</td><td>0.0785</td><td>8.5</td></tr><tr><td rowspan="2">A3</td><td>Noise</td><td>99.5</td><td>863.7</td><td>1087.4</td><td>0.0616</td><td>0.0072</td><td>0.0795</td><td>14.6</td></tr><tr><td>Consider</td><td>99.5</td><td>1363.0</td><td>1087.4</td><td>0.0985</td><td>0.0072</td><td>0.0795</td><td>14.6</td></tr><tr><td rowspan="2">B1</td><td>Noise</td><td>1.9</td><td>76.7</td><td>6.9</td><td>0.0056</td><td>0.0001</td><td>0.0006</td><td>1.8</td></tr><tr><td>Consider</td><td>52.5</td><td>2207.8</td><td>7.0</td><td>0.1607</td><td>0.0019</td><td>0.0010</td><td>52.3</td></tr><tr><td rowspan="2">B2</td><td>Noise</td><td>7.4</td><td>262.3</td><td>6.9</td><td>0.0191</td><td>0.0003</td><td>0.0006</td><td>7.4</td></tr><tr><td>Consider</td><td>7.4</td><td>668.0</td><td>6.9</td><td>0.0487</td><td>0.0003</td><td>0.0006</td><td>7.4</td></tr><tr><td rowspan="2">C1</td><td>Noise</td><td>168.8</td><td>2208.8</td><td>1553.1</td><td>0.1579</td><td>0.0115</td><td>0.2233</td><td>65.7</td></tr><tr><td>Consider</td><td>168.8</td><td>2292.7</td><td>1553.1</td><td>0.1641</td><td>0.0115</td><td>0.2233</td><td>65.7</td></tr><tr><td rowspan="2">C2</td><td>Noise</td><td>13.4</td><td>519.0</td><td>31.0</td><td>0.0379</td><td>0.0005</td><td>0.0021</td><td>13.5</td></tr><tr><td>Consider</td><td>58.7</td><td>2199.6</td><td>31.3</td><td>0.1605</td><td>0.0022</td><td>0.0021</td><td>57.2</td></tr></table>

The use of single-station range and angle measurements (cases A1 to A3) allows the orbit to be determined with an accuracy of roughly $1 0 0 \mathrm { m }$ in radial direction $( x )$ as well as $1 \mathrm { k m }$ in along-track (y) and normal (z) direction. A comparison of cases A1 and A2 (Table 9.3) shows that the estimation of angle biases is essential to reduce the impact of systematic measurement errors on the resulting orbit. The range bias cannot, however, be estimated together with the angle biases in a single station configuration, since the resulting least squares equations would be close to singular. It mainly affects the accuracy by which the along-track position and the radial velocity component can be determined. As may be recognized from cases A2 and A3, use of the Buenos Aires station promises better orbit determination results than that of Cordoba despite an equal tracking performance. This fact may be attributed to a more favorable tracking geometry of the Buenos Aires station caused by the larger longitude and latitude offset with respect to the sub-satellite point.

![](images/30cd814911fdc6585377596f34bf2ae41f7e3bbac2b5a7c3ea9fdd84c8c44ff7.jpg)  
Fig. 9.3. Evolution of the predicted position accuracy for single station range and angle tracking (Case A2)

The evolution of the radial, along-track, cross-track and total position accuracy for case A2 is illustrated in Fig. 9.3. The individual errors exhibit little to no orbital periodicity due to the continuous coverage of the tracking arc. While the uncertainty in the radial and normal component remains essentially constant, the tangential component varies in a quadratic way as a consequence of the semi-major axis error.

Dual-station ranging (cases B1 and B2) allows for a notable improvement of the radial and cross-track position vector component as well as the tangential and cross-track velocity over the single-station scenario. The along-track position and the radial velocity, however, remain sensitive to the range bias and are 1–2 orders of magnitude less accurate than the other components. The estimation of one range bias (Case B2) is possible in the dual-station configuration and recommended to minimize the impact of systematic errors on the solution.

While one or two-day tracking is generally considered as a standard for the determination of a geostationary satellite orbit, shorter data arcs may be desirable e.g. after maneuvers or in contingency situations. As shown by cases C1 and C2 a reasonable accuracy can already be achieved with half a day of single-station range and angle measurements or even six hours of dual-station ranging. In the latter case care should be taken, not to a estimate any bias at all, since the resulting normal equations would be ill-conditioned and result in a large formal covariance. For even shorter data arcs, it is difficult to separate the periodic and linear part in the daily variation of each measurement, which severely reduces the overall condition of the estimation problem.

# 9.2 Real-Time Orbit Determination

The increasing number of GPS receivers for spaceborne applications has revitalized the interest in real-time and on-board orbit determination to increase the spacecraft autonomy and reduce the required amount of ground operations. Aside from high-precision applications that require a direct processing of raw code and phase measurements, the orbit determination can be based on the navigation solution generated by most of the GPS receivers. In general position values are provided with a spherical $1 \sigma$ accuracy of about $1 0 0 \mathrm { m }$ (cf. Table 6.2), whereas velocity is only1 accurate to $1 \mathrm { m / s }$ in representative spaceborne receivers. Using a Kalman filter and an appropriate dynamical model, the inherent measurement noise may be reduced considerably and much more accurate state vectors be obtained.

The filtering of the SPS (Standard Positioning Service) data provides various benefits for on-board navigation. These are mainly related to the fact that the resulting trajectory is constrained by the dynamical laws of motion, whereas subsequent GPS position solutions are essentially uncorrelated. As such, the adjusted orbit information is less sensitive to the intentional deterioration of the GPS measurements (Selective Availability) than the navigation solution itself. In addition, the dynamical modeling allows a smooth interpolation of the trajectory, a bridging of data gaps and a detection of erroneous measurements. Finally, the Kalman filter provides precise velocity information as part of the estimated state vector, which results from the accumulation of position knowledge over extended data arcs.

# 9.2.1 Model and Filter Design

For on-board applications, computer resources are generally much more constrained than for ground operations due to limitations of processor speed and memory. A careful selection of dynamical models, reference systems, integration methods, and estimation methods is therefore required in the design of onboard navigation systems.

Force Model: The GPS navigation data to be processed in the present application have been collected as part of the GPS/MET experiment (Hajj et al. 1995) on-board the MicroLab-1 satellite. The spacecraft was launched in 1995 and orbits the Earth at an altitude of roughly $7 4 0 \mathrm { k m }$ . At this altitude, the acceleration is dominated by the gravity field of the Earth including higher-order terms in the spherical harmonics expansion. Lunisolar gravity on the other hand provides only minor perturbations for satellites in low-Earth orbits as does the solar radiation pressure for satellites with representative area-to-mass ratios (cf. Fig. 3.1). From the Harris–Priester density tables (Table 3.8) it may further be concluded that atmospheric drag does not impose major perturbations in the relevant altitude range. To illustrate these considerations, the orbit of MicroLab-1 has been integrated over a period of 6 hours, taking into account various force models of increasing complexity.

Table 9.4. Maximum impact of perturbative forces onto the MicroLab-1 trajectory for orbit predictions up to 6 hours: (a) Earth oblateness $( J _ { 2 } )$ , (b) difference of $4 \times 4$ gravity field and $J _ { 2 }$ , (c) difference of $1 0 \times 1 0$ and $4 \times 4$ gravity field, (d) difference of $1 5 \times 1 5$ and $1 0 \times 1 0$ gravity field, (e) difference of $2 0 \times 2 0$ and $1 5 \times 1 5$ gravity field, (f) solar gravity, (g) lunar gravity, (h) solar radiation pressure, (i) drag. All values in [m]   

<table><tr><td>t[h]</td><td>(a)</td><td>(b)</td><td>（c）</td><td>(d</td><td>(e)</td><td>(f)</td><td>（g）</td><td>(h)</td><td>(i</td></tr><tr><td>0.5</td><td>8700</td><td>210</td><td>91</td><td>11</td><td>3</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>1.0</td><td>10000</td><td>680</td><td>240</td><td>22</td><td>6</td><td>1</td><td>2</td><td>0</td><td>0</td></tr><tr><td>1.5</td><td>21000</td><td>750</td><td>240</td><td>22</td><td>6</td><td>3</td><td>4</td><td>0</td><td>1</td></tr><tr><td>3.0</td><td>33000</td><td>1600</td><td>340</td><td>69</td><td>6</td><td>5</td><td>7</td><td>1</td><td>4</td></tr><tr><td>6.0</td><td>71000</td><td>1800</td><td>570</td><td>130</td><td>18</td><td>9</td><td>14</td><td>2</td><td>14</td></tr></table>

Based on the results collected in Table 9.4, the lunisolar gravitational perturbations (f, g) are certainly smaller than the measurement accuracy of about $1 0 0 \mathrm { m }$ over the times of interest and the same holds for the effect of solar radiation pressure (h) as well as aerodynamic drag (i). Measurable effects on the spacecraft trajectory are caused by harmonic terms up to degree and order 15 in the Earth’s gravity field (a-d), if one considers propagation times of up to 6 hours. Restricting oneself to half-hour intervals or tolerating errors up to $1 \mathrm { k m }$ , it is possible, however, to apply a reduced model of degree and order 10. Considering, furthermore, that the computational workload for evaluating the acceleration is essentially proportional to the square of the maximum order, the reduced model offers a factor-of-two performance gain at a tolerable loss in accuracy. A $1 0 \times 1 0$ gravity model is, therefore, considered as a baseline for the implementation of a real-time orbit determination process.

Reference System: Since GPS based position measurements refer to an Earth-fixed (WGS84) reference an appropriate transformation to (or from) the inertial frame must be applied in the data processing. The same holds for the computation of the acceleration vector, which is most easily formulated in the Earth-fixed frame but must be expressed in the inertial frame for integrating the equation of motion. A proper choice of the reference system is therefore advisable to minimize the overall computational effort. For the present purpose an almost inertial coordinate system is suggested, which is aligned with the instantaneous Earth equator and the mean equinox. Taking into account that polar motion introduces offsets of about ten meters only, at the surface of the Earth, the transformation from Earth-fixed WGS84 positions rWGS to inertial coordinates $r$ may then be established as

$$
r = R _ { z } ^ { - 1 } ( { \mathrm { G M S T } } ( t ) ) r _ { \mathrm { W G S } } ~ .
$$

Here GMST denotes the Greenwich Mean Sidereal Time at a given instant $t$ . Deviations from a truly inertial coordinate system arise from the neglect of precession and nutation that slightly alter the orientation of the equator and equinox. The time scale of these changes is much longer, however, than the typical data span of several revolutions required for a reliable orbit adjustment. As such, the associated changes of the reference system have no practical impact on the performance of the orbit determination process.

Estimation and Integration: Before discussing the choice of a suitable numerical integration method for the equation of motion, a brief consideration of the overall estimation concept is required. While a least-squares method would ensure a high degree of robustness in the handling of non-linearities or the rejection of erroneous measurements, it would necessitate an on-board storage of a large measurement batch to allow multiple iterations. A Kalman filter is therefore preferable, which processes each measurement exactly once as soon as it is collected. In this case, however, an extended Kalman filter must be selected to cope with the non-linearity of the orbit determination problem. The associated change of the reference trajectory in each update step does, however, imply a frequent restart of the numerical integration. Even for a data rate of only one value per five minutes, a high-order integration method would be forced to work at a non-optimal stepsize. Considering in addition the complexity and storage requirements of elaborate single-step methods, low-order Runge–Kutta methods turn out to be best suited for the envisaged usage. Furthermore, no stepsize control is required for near-circular orbits. In the sequel the well-known 4th-order Runge–Kutta method will be applied, which provides a particularly simple set of coefficients. As a baseline, a 30 s step size is adequate to integrate the orbit to the desired accuracy.

State Transition Matrix: Another issue that has to be addressed in the design of the orbit determination process concerns the modeling of the state transition matrix between consecutive steps. While a rigorous integration of the variational equations would ensure full consistency between the trajectory model and the associated partial derivatives, it is generally too cumbersome to be applied in real-time systems. Simple Taylor expansions may, on the other hand, cause problems if the time between consecutive data points covers a notable fraction of the orbit. As a compromise, a Keplerian formulation of the state transition matrix is therefore applied in the RTOD program.

Process Noise: Last but not least, a suitable process noise model has to be considered in the design of the extended Kalman filter. For the present purpose a simple model is adequate, since measurements are provided at almost equidistant time steps throughout the whole data arc. It is therefore sufficient to add a constant processnoise matrix $Q = \mathrm { d i a g } ( w _ { \mathrm { p o s } } ^ { 2 } , w _ { \mathrm { v e l } } ^ { 2 } )$ to the predicted covariance in each time update step. Position and velocity variances as given by the diagonal elements of $\varrho$ are selected in accordance with the expected trajectory modeling errors arising in the propagation from one measurement to the next. All off-diagonal elements of $\varrho$ are set to zero. Suitable values of $w _ { \mathrm { p o s } }$ and $w _ { \mathrm { v e l } }$ are best found by experiment and depend on the data interval, the assumed measurement accuracy, and the accuracy of the dynamical model. In the present application nominal process-noise parameters of $0 . 5 \mathrm { m }$ and $0 . 5 \mathrm { m m } / \mathrm { s }$ are applied for a five-minute data interval, which helps to avoid a filter divergence without sacrificing the achievable accuracy.

# 9.2.2 The RTOD Program

The RTOD program processes a sequence of GPS navigation data and auxiliary information provided in the RTOD.dat file. Aside from a single header line that may be skipped on reading, the file contains one record per time with a structure as described in Table 9.5. Following the date and GPS time tag, the position and velocity vector in the WGS84 system as determined by the GPS receiver are given in the initial columns. To evaluate the filter performance, the actual spacecraft position and velocity in the rotating, Earth-fixed system is furthermore provided as determined from a least-squares orbit determination with an elaborate force model. Both position and velocity measurements from the first data record are used to derive the inertial state vector of the spacecraft, which is required to initialize the filter and to start the trajectory integration. Subsequent measurement updates make use of the position measurements only, which provide a much better relative accuracy than the velocity data.

Table 9.5. Structure of the RTOD data file   

<table><tr><td>Cols.</td><td>Description</td></tr><tr><td>1-10 13-24 28- 37 39- 48 50- 59 63- 72 74 83 85-94 98-107 109-118 120-129 133-142</td><td>Date (yyyy/mm/dd) GPS time (hh:mm:ss.sss) Measured position x (WGS84 system,in [m]) Measured position y (WGS84 system,in [m]) Measured position z (WGS84 system,in [m]) Measured velocity x (WGS84 system,in [m/s]) Measured velocity j (WGS84 system,in [m/s]) Measured velocity  (WGS84 system,in [m/s]) True position x (WGS84 system,in [m])</td></tr></table>

A supplementary setup file RTOD.inp is used to control and modify the filter performance. The individual parameters comprise the gravity-field order and the step size applied in the numerical trajectory integration as well as the measurement standard deviation, the a priori statevector uncertainty and two state-noise parameters for controlling the addition of process noise. An edit (or culling) level is, furthermore, specified, to allow the rejection of bad measurements. It serves as a threshold for the identification of outliers and is specified in units of the measurement standard deviation $\sigma$ . Assuming a Gaussian error distribution, more than $9 9 \%$ of all measurements should exhibit errors of less than $3 \sigma$ . Measurements, for which the ratio of the residual and the standard deviation exceeds an edit level of about three should therefore be considered as erroneous data points and discarded.

Each line of the input file provides a single parameter following a 30-character comment. Representative parameter values are given in the subsequent listing:

Gravity model order ( $\scriptstyle < = 2 0$ ) ： 10   
Integration step size [s] 30   
Measurement sigma [m] 100   
A priori sigma position [m] : 1000   
A priori sigma velocity [m/s]: 10   
State noise position [m] ： 0.5   
State noise velocity [m/s] : 0.0005   
Edit level (sigma) : 3.0

The output of the RTOD program comprises a copy of the setup parameters and a table of filter outputs at each step. The table is made up of 13 blank separated columns, giving the time $t$ since epoch (Col. 1, in [s]), the filtered Earth-fixed position $r$ (Col. 2–4, in $[ \mathrm { m } ]$ ) and the measurement and solution errors. The latter parameters comprise the difference $| r _ { \mathrm { G P S } } - r _ { \mathrm { r e f } } |$ between the measured position and the reference orbit (Col. 5), the standard deviation $\sigma _ { r }$ of the estimated position (Col. 6) and the error $| \boldsymbol { r } - \boldsymbol { r } _ { \mathrm { r e f } } |$ of the estimated position (Col. 7). Corresponding quantities are provided for the errors of the velocity (Col. 8–10) and the semi-major axis (Col. 11–13). For information, measurements rejected by the filter are marked by an asterisk immediately following the measurement error.

# 9.2.3 Case Studies

The following case studies are based on a 24-hour data arc of GPS measurements collected by a TurboStar receiver as part of the GPS/MET experiment on October 1, 1996. The measurements are sampled at a rate of one point per five minutes, yielding an average of 20 measurements per orbit. The data noise as derived from the root-mean-square deviation from the reference trajectory amounts to roughly $1 1 0 \mathrm { m }$ in position and $2 . 5 \mathrm { m } / \mathrm { s }$ in velocity.

Table 9.6. Filter parameters for selected case studies   

<table><tr><td colspan="2">Parameter</td><td>Case A</td><td>Case B</td><td>Case C</td></tr><tr><td colspan="2">Gravity model order n</td><td>10</td><td>10</td><td>4</td></tr><tr><td colspan="2">Integration step size △t [s]</td><td>30</td><td>60</td><td>30</td></tr><tr><td colspan="2">Measurement standard deviation Oxyz [m] Opos [m]</td><td>100</td><td>100</td><td>100</td></tr><tr><td colspan="2">A priori std. dev.position</td><td>1000</td><td>1000</td><td>1000</td></tr><tr><td colspan="2">A priori std. dev.velocity Ovel [m/s]</td><td>10</td><td>10</td><td>10</td></tr><tr><td colspan="2">State noise position Wpos [m]</td><td>0.5</td><td>0.0</td><td>10.0</td></tr><tr><td colspan="2">State noise velocity Wvel [m/s]</td><td>0.0005</td><td>0.0000</td><td>0.0100</td></tr><tr><td colspan="2">Edit level</td><td>3.0</td><td>3.0</td><td>3.0</td></tr></table>

To start with, the nominal filter performance is illustrated in case A (cf. Table 9.6). The equation of motion is integrated in 30 s steps and includes perturbations due to the harmonic gravity field of the Earth up to degree and order 10. The a priori standard deviation of the initial state taken from the first data point is assumed to be $1 \mathrm { k m }$ and $1 0 \mathrm { m / s }$ , respectively, for the position and velocity coordinates. While this is about a factor of 10 worse than the actual measurement standard deviation, the adopted values ensure that the filter starts properly, even if the initial measurement is affected by larger than average errors.

![](images/3c7726e209b3329ef3ff8cb8cde8196bab266a34ce3f95ddbe89bb7798de247f.jpg)  
Fig. 9.4. Nominal filter performance for GPS/MET orbit determination (case A): error of the estimated position (bold line), standard deviation of the estimate (narrow line) and GPS measurement errors (dots).

Results of the corresponding RTOD run are summarized in Fig. 9.4, which shows the measurement residuals, the error of the estimated position and the standard deviation computed by the filter. The filter takes about three hours (two revolutions) before it converges to a steady-state behavior. During the initial phase the filter is affected by pronounced errors of two consecutive measurements that amount to $2 5 0 \mathrm { m }$ and $5 0 0 \mathrm { m }$ , respectively. The latter value exceeds the $3 \sigma$ $\scriptstyle ( = 3 0 0 \mathrm { m } )$ data editing criterion, which results in a rejection of the corresponding measurement and an associated increase in the propagated position covariance. During the steadystate phase the filter approaches a constant position standard deviation of roughly $5 0 \mathrm { m }$ . This equilibrium value results from a balance between the information gain due to the processing of new measurements and the covariance increase caused by the addition of process noise in the state update phase. The deviation between the estimated position and the reference trajectory is generally less than the computed standard deviation and amounts to $2 5 \mathrm { m }$ on average (r.m.s.) after the initial two hours. Thus, the filtered positions are more accurate than the measured positions by a factor of four to five, which clearly illustrates the advantage of a dynamical orbit determination over the purely kinematic GPS position solutions. The benefit is even more pronounced for the velocity determined by the filter, which is approximately 100 times more accurate ( $2 . 5 \mathrm { c m } / \mathrm { s }$ r.m.s.) than the velocity values provided by the

![](images/9ce8beb46023a0fde95d6d4c5fcd0fb84d8908307440c9ad0b3fd27775487b3b.jpg)  
Fig. 9.5. Nominal filter performance for GPS/MET orbit determination (case A): error of the estimated velocity (bold line), standard deviation of the estimate (narrow line) and GPS measurement errors (dots).

![](images/b58be09922cb558d10aadca1463b5798c4b454a3c4ea5f4271c56c1ce1b48c73.jpg)  
Fig. 9.6. Nominal filter performance for GPS/MET orbit determination (case A): error of the estimated semi-major axis (bold line), standard deviation of the estimate (narrow line) and error of the semi-major axis computed from the GPS position/velocity measurements (dots).

![](images/dec6c92a0416c414aee61a90a6f700944bd6957eea777ad8464f95bd3334dda8.jpg)  
Fig. 9.7. Filter divergence due to numerical integration errors in the absence of process noise (case B): error of the estimated position (bold line), standard deviation of the estimate (narrow line) and measurement errors (dots).

![](images/07333380806713d07462bba843728d1f574d331fa50580aeffeaa40614c3dafb.jpg)  
Fig. 9.8. Compensation of low-order gravity model errors by increased process noise (case C): error of the estimated position (bold line), standard deviation of the estimate (narrow line) and measurement errors (dots).

![](images/7e0460d714ef680811cb240715f9c4eecf9c760a80ee5c8b236699c4797c87a8.jpg)  
Fig. 9.9. Compensation of low order gravity model errors by increased process noise (case C): error of the estimated semi-major axis (bold line), standard deviation of the estimate (narrow line) and error of the semi-major axis computed from the position/velocity measurements (dots).

GPS receiver itself (Fig. 9.5). The semi-major axis derived from the estimated state vector is accurate to about $3 \mathrm { m } \mathrm { r . m . s }$ . (cf. Fig. 9.6).

An example of moderate filter divergence is given by case B, in which slight propagation errors have been introduced by selecting a larger than nominal integration step size. At the same time, no process noise is added, which makes the filter continuously less receptive to new measurements. For up to seven hours (4–5 revolutions) the filter output closely matches that of case A. Thereafter, however, the position error starts to increase past the formal standard deviation and the solution differs from the true position by up to $1 0 0 \mathrm { m }$ (Fig. 9.7). Case B obviously lacks a sufficient amount of process noise to compensate the inherent model errors, whereas both factors are properly balanced in case A.

An extreme case of model error compensation is, furthermore, presented in case C, where the degree and order of the gravity field have been reduced from ten to four. At the same time the process noise has been increased by a factor of 20 over case A, which results in a steady-state position uncertainty of about $1 0 0 \mathrm { m }$ . While the root-mean-square position and velocity errors are approximately doubled during the steady-state phase in comparison to case A, the filtered solution and its variance become sensitive to erroneous data and data gaps (Fig. 9.8). More importantly one may note a ten-fold increase of the semi-major axis error and standard deviation in comparison to case A (Figs. 9.6 and 9.9). As a rule of thumb, the observed peak error of $\varDelta a = 5 0 \mathrm { m }$ would result in a $5 0 0 \mathrm { m }$ along-track error after one orbit or about $7 \mathrm { k m }$ after one day.

# 9.3 Relay Satellite Orbit Determination

The United States’ Tracking and Data Relay Satellite System (TDRSS) provides tracking services for all major US space observatories and research satellites as well as the manned Space Shuttle. Even though the system is essentially unique, it provides a representative example of satellite-satellite tracking techniques and is discussed here to illustrate the modeling of signal paths across multiple transponders as well as the adjustment of multiple spacecraft trajectories.

![](images/25055a7bd3cecd851e286b4b096b59e3f3844f73602920fb846c8df0fe4368ea.jpg)  
Fig. 9.10. Principle of TDRS four-way ranging measurements.

# 9.3.1 Mathematical Models

As illustrated in Fig. 9.10, TDRS ranging measurements are initiated by sending a ranging signal to one of the geostationary relay satellites. From here it is forwarded to the desired user spacecraft, retransmitted and linked back to the ground station after passing the relay satellite a second time. Designating the time of signal reception at the ground station by $t$ and by $r _ { \mathrm { S / C } }$ , rTDRS, and $r _ { \mathrm { G / S } }$ the inertial position vectors of the user satellite, the TDRS satellite, and the ground station, respectively, one obtains the implicit equations

$$
\begin{array} { r c l } { \tau _ { 1 } } & { = } & { 1 / c \cdot | r _ { \mathrm { T D R S } } ( t - \tau _ { 1 } ) - r _ { \mathrm { G } / \mathrm { S } } ( t ) | } \\ { \tau _ { 2 } } & { = } & { 1 / c \cdot | r _ { \mathrm { S } / \mathrm { C } } ( t - \tau _ { 1 } - \tau _ { 2 } ) - r _ { \mathrm { T D R S } } ( t - \tau _ { 1 } ) | } \\ { \tau _ { 3 } } & { = } & { 1 / c \cdot | r _ { \mathrm { T D R S } } ( t - \tau _ { 1 } - \tau _ { 2 } - \tau _ { 3 } ) - r _ { \mathrm { S } / \mathrm { C } } ( t - \tau _ { 1 } - \tau _ { 2 } ) | } \\ { \tau _ { 4 } } & { = } & { 1 / c \cdot | r _ { \mathrm { G } / \mathrm { S } } ( t - \tau _ { 1 } - \tau _ { 2 } - \tau _ { 3 } - \tau _ { 4 } ) - r _ { \mathrm { T D R S } } ( t - \tau _ { 1 } - \tau _ { 2 } - \tau _ { 3 } ) | } \end{array}
$$

for the individual light times. Starting from initial values of zero, the light times are consecutively determined from these relations using a simple fixed-point iteration. The resulting values then yield the modeled four-way range

$$
\rho = \frac { c } { 2 } \cdot ( \tau _ { 1 } + \tau _ { 2 } + \tau _ { 3 } + \tau _ { 4 } ) ~ .
$$

Neglecting the relative motion of the station and the two satellites, the 4-way range is equal to the sum of the distances from the ground station to the relay satellite and from the relay satellite to the user satellite.

The measurement noise and the systematic errors of the TDRS ranging system are generally less than $1 0 \mathrm { m }$ , which implies that the motion of the user spacecraft, the relay satellite, and the ground station must be modeled to a similar level of accuracy. Since most of the user satellites tracked by the TDRS system orbit the Earth at altitudes of several hundreds of kilometers, the force model must as a minimum, comprise the harmonic gravity field of the Earth as well as the acceleration due to atmospheric drag. The geostationary relay satellite, on the other hand, is notably affected by lunisolar gravitational perturbations and solar radiation pressure. In order to avoid different models for the various satellites concerned, a common model comprising all of the above-mentioned perturbations should be considered. A gravity field model up to degree and order 20 is recommended to describe the motion of user satellites at altitudes of $5 0 0 { - } 1 0 0 0 { \mathrm { k m } }$ with the desired accuracy.

For a compatible modeling of the ground station position, polar motion and true sidereal time must be considered to describe the Earth’s rotation. In addition, nutation and precession need to be accounted in the transformation to a common inertial reference frame (e.g. the mean equator and equinox of J2000). For an adequate modeling of the Greenwich hour angle, knowledge of Universal Time UT1 is required to better than 0.01 s.

In accordance with Sect. 7.2.3, the variational equations for the state transition matrix may be based on a simplified force model comprising only the second-order zonal harmonics in the gravity field. Along with the state transition matrix, the sensitivity matrix describing the state vector partials with respect to the drag and solar radiation pressure coefficients is integrated to allow an adjustment of these parameters within the orbit determination.

# 9.3.2 The TDRSOD Program

The TDRSOD program performs a least-squares orbit determination using TDRS four-way range measurements. Based on an appropriate set of measurements the orbital parameters of a single user spacecraft and up to two relay satellites can be adjusted simultaneously. Tracking data are provided in the TDRSOD.dat file, which contains one record per time with a structure as described in Table 9.7. A single header line serves to label each column and is skipped upon reading. Following the epoch of the measurement the ground station and spacecraft identification numbers as well as the four-way relay range are given in each line.

Table 9.7. Structure of the TDRSOD tracking data file   

<table><tr><td>Cols.</td><td>Description</td></tr><tr><td>1-10</td><td>Date (yyyy/mm/dd)</td></tr><tr><td>13-24</td><td>UTC time (hh:mm:ss.sss) of signal reception</td></tr><tr><td>26-30</td><td>Station number</td></tr><tr><td>32-34</td><td>TDRS identification number (ID)</td></tr><tr><td>36-46</td><td>Range measurement (in [m]) corrected for refraction</td></tr></table>

A supplementary setup file TDRSOD.inp provides a priori state vectors and spacecraft-related parameters for the user and TDRS satellites as well as relevant auxiliary information. The individual parameters comprise the total number $( \leq 2 )$ and IDs of the TDRS satellites, the total number $( \leq 2 )$ ) and IDs of the employed ground stations, the desired number of iterations, the UT1 UTC and UTC TAI time differences, as well as the current pole coordinates, all of which are given at the beginning of the input file. Following the initial epoch, the state vectors of the user spacecraft and the specified number of TDRS satellites are provided together with the associated a priori standard deviations. The spacecraft-related information is complemented by the specification of each satellite’s mass, area, drag coefficient, and radiation pressure coefficient, as well as the related a priori uncertainties of the latter parameters. The file closes with a section providing the coordinates of the specified number of ground stations.

Each line provides a single parameter starting at column 26. The initial characters are ignored on input and serve to describe the meaning of the respective quantities. Representative parameter values are given in the subsequent listing:

<table><tr><td>TDRS</td><td></td><td>2</td><td>4</td><td>5</td></tr><tr><td>Stations</td><td></td><td>2</td><td rowspan="2">161</td><td rowspan="2">162</td></tr><tr><td>Iterations</td><td></td><td>4</td></tr><tr><td>UT1-UTC，UTC-TAI [s]</td><td></td><td>+0.49</td><td>-32.00</td><td></td></tr><tr><td>x-pole,y-pole [&quot;]</td><td></td><td>-0.00651</td><td>+0.36588</td><td></td></tr><tr><td>Epoch (UTC)</td><td></td><td>1999/09/01</td><td>00:00:00.000</td><td></td></tr><tr><td>X UARS [m]</td><td></td><td>1476200.0</td><td>1000.0</td><td></td></tr><tr><td>y UARS [m]</td><td></td><td>5996200.0</td><td>1000.0</td><td></td></tr><tr><td>Z UARS [m]</td><td></td><td>-3209000.0</td><td>1000.0</td><td></td></tr><tr><td>VX UARS [m/s]</td><td></td><td>-3854.0000</td><td>1.0</td><td></td></tr><tr><td>vy UARS [m/s]</td><td>：</td><td>3778.5000</td><td>1.0</td><td></td></tr><tr><td>VZ UARS [m/s]</td><td></td><td>5302.2000</td><td>1.0</td><td></td></tr><tr><td>m [kg]，A[m^2]</td><td></td><td>5968.3</td><td>27.22</td><td></td></tr><tr><td>CD，sigma(CD)</td><td></td><td>2.3</td><td>1.0</td><td></td></tr><tr><td>CR，sigma(CR)</td><td></td><td>1.3</td><td>0.1</td><td></td></tr><tr><td>X TDRS-4 [m]</td><td></td><td>+20174293.6</td><td>1.0</td><td></td></tr><tr><td>y TDRS-4 [m]</td><td></td><td>-37024903.8</td><td>1.0</td><td></td></tr><tr><td>Z TDRS-4 [m]</td><td></td><td>-982925.2</td><td>1.0</td><td></td></tr><tr><td>VX TDRS-4 [m/s]</td><td></td><td>+2696.9634</td><td>0.001</td><td></td></tr><tr><td>vy TDRS-4 [m/s]</td><td></td><td>+1471.5074</td><td>0.001</td><td></td></tr><tr><td>VZ TDRS-4 [m/s]</td><td></td><td>-100.5261</td><td>0.001</td><td></td></tr><tr><td>m [kg]，A [m^2]</td><td></td><td>1668.9</td><td>40.0</td><td></td></tr><tr><td>CD，sigma(CD)</td><td></td><td>2.3</td><td>0.001</td><td></td></tr></table>

<table><tr><td>CR，sigma(CR)</td></tr><tr><td>1.3915 0.001 -40783913.5 100.0</td></tr><tr><td>TDRS-5 [m] X TDRS-5 10622599.3 100.0</td></tr><tr><td>y [m]</td></tr><tr><td>Z TDRS-5 [m] 992633.1 100.0 VX TDRS-5 [m/s] -774.3896 0.1</td></tr><tr><td>vy TDRS-5 [m/s] -2976.0955 0.1</td></tr><tr><td>TDRS-5 [m/s] 18.8994 0.1</td></tr><tr><td>VZ m [kg]，A[m^2] 1718.4 40.0</td></tr><tr><td>CD，sigma(CD) 2.3 0.1</td></tr><tr><td>CR，sigma(CR) 1.4062 0.1</td></tr><tr><td>Sta WHSK/161 (xyz）[m] -1539385.74 -5160953.12 +3408202.16</td></tr><tr><td>Sta WH2K/162（xyz）[m] -1539390.43 -5160968.83 +3408176.45</td></tr></table>

The TDRSOD program uses the DE multistep method to integrate the state vector as well as the state transition and sensitivity matrix for each individual satellite from specified initial conditions. Considering the widely different orbital periods of the low-Earth user satellite and the geostationary relay satellites, the respective trajectories are integrated independently of each other using the most appropriate integration stepsize for each orbit. Interpolation over multiple steps is used to interpolate the solution during the light time iteration.

The least-squares adjustment is performed over the specified number of iterations, during each of which the observation residuals and the computed parameter corrections are output. No data editing or convergence check is performed to maintain a simple overall program structure. A priori standard deviations are expected for all estimation parameters, which should be selected in accordance with the expected uncertainty of the respective state vector component or force model parameter.

# 9.3.3 Case Study

In the subsequent application TDRS range measurements of NASA’s Upper Atmosphere Research Satellite (UARS) are processed, which were collected on September 1, 1999. The data set comprises 14 batches of 10–15 minutes duration each, which are evenly distributed over the entire day. Out of these, three batches have been obtained via the TDRS-4 satellite, located at $4 1 . 0 ^ { \circ }$ West longitude, while the remaining measurements were performed with TDRS-5 at $1 7 4 . 3 ^ { \circ }$ West longitude. All data have previously been corrected for refraction.

Orbits of the two TDRS satellites have independently been derived from groundbased tracking and serve as a priori information for the UARS orbit determination. The corresponding state vectors, as referred to the Earth’s mean equator and equinox (EME2000), are collated in Table 9.8 together with relevant spacecraft parameters. In addition, Table 9.9 provides the coordinates of the WHSK and WH2K antennas of the White Sands ground station complex, which were employed in the four-way ranging measurements via TDRS-4 and TDRS-5, respectively.

For a proper performance of the least-squares orbit determination, a priori standard deviations need to be specified for the state vector components as well as the drag and solar radiation pressure coefficients. In the absence of actual a priori statistics, appropriate values may be obtained from a consideration of the orbital characteristics, the tracking geometry, and the data distribution. In the case of the user satellite, which is tracked over roughly 15 revolutions with a sufficient coverage during each orbit, one may expect a reliable determination of its orbital elements from the given measurements. In accord with the given number of digits, an uncertainty of $1 \mathrm { k m }$ and $1 \mathrm { m / s }$ in each axis is therefore assumed for the initial position and velocity of the UARS satellite. Neither of these values puts a stringent constraint on the resulting least-squares solution, as does the assumed standard deviation of 1.0 for the drag coefficient. For the solar radiation pressure coefficient, on the other hand, the a priori standard deviation is set to 0.1, in accordance with the uncertainty in the knowledge of relevant material properties.

Table 9.8. A priori orbit and spacecraft parameters of UARS, TDRS-4, and TDRS-5 for the epoch 1999/09/01 00:00 UTC   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>UARS</td><td rowspan=1 colspan=1>TDRS-4</td><td rowspan=1 colspan=2>TDRS-5</td></tr><tr><td rowspan=1 colspan=1>x [m]</td><td rowspan=1 colspan=1>+1476200.0</td><td rowspan=1 colspan=1>+20174293.6</td><td rowspan=2 colspan=2>+40783913.5+10622599.3</td></tr><tr><td rowspan=1 colspan=1>y[m]</td><td rowspan=1 colspan=1>+5996200.0</td><td rowspan=1 colspan=1>-37024903.8</td><td rowspan=1 colspan=2>+10622599.3</td></tr><tr><td rowspan=1 colspan=1>z[m]</td><td rowspan=1 colspan=1>-3209000.0</td><td rowspan=2 colspan=1>-982925.2+2696.9634</td><td rowspan=2 colspan=2>+992633.1-774.3896</td></tr><tr><td rowspan=1 colspan=1>x [m/s]</td><td rowspan=1 colspan=1>-3854.0000</td></tr><tr><td rowspan=2 colspan=1>y [m/s][m/s]</td><td rowspan=1 colspan=1>+3778.5000</td><td rowspan=2 colspan=1>+1471.5074-100.5261</td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>+5302.2000</td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>m [kg]</td><td rowspan=1 colspan=1>5968.3</td><td rowspan=1 colspan=1>1668.9</td><td rowspan=3 colspan=2>1718.440.02.31.4062</td></tr><tr><td rowspan=1 colspan=1>A[m]</td><td rowspan=1 colspan=1>27.22</td><td rowspan=1 colspan=1>40.0</td></tr><tr><td rowspan=1 colspan=1>CDCR</td><td rowspan=1 colspan=1>2.31.3</td><td rowspan=1 colspan=1>2.31.3915</td></tr></table>

Table 9.9. White Sands antenna locations   

<table><tr><td rowspan=1 colspan=1>Station</td><td rowspan=1 colspan=1>No.</td><td rowspan=1 colspan=1>x [m]</td><td rowspan=1 colspan=1>y[m]</td><td rowspan=1 colspan=1>z[m]</td></tr><tr><td rowspan=1 colspan=1>WHSKWH2K</td><td rowspan=1 colspan=1>161162</td><td rowspan=1 colspan=1>-1539385.74-1539390.43</td><td rowspan=1 colspan=1>-5160953.12-5160968.83</td><td rowspan=1 colspan=1>+3408202.16+3408176.45</td></tr></table>

For the Tracking and Data Relay Satellites, which orbit the Earth at geostationary altitude, drag does not impose any orbit perturbations and thus cannot be calibrated during the orbit determination. An a priori standard deviation of 0.1 for the respective $C _ { D }$ coefficients therefore merely serves to avoid a singularity of the resulting normal equations. In fact, the a priori value (2.3) will not be changed at all within the least-squares adjustment. Concerning the other parameters, it is recalled that TDRS-4 tracking data are only available for a limited number of data arcs, while TDRS-5 tracking essentially covers the whole day. In view of the even sampling of the TDRS-5 orbit, the four-way range measurements performed via this satellite can therefore be employed to improve its orbit along with that of the user satellite. This is accomplished by assuming a priori standard deviations of $1 0 0 \mathrm { m }$ and $0 . 1 \mathrm { m } / \mathrm { s }$ for position and velocity as well as 0.1 for the $C _ { R }$ coefficient. These figures take care of the fact that the TDRS-5 orbit has already been determined with good accuracy from independent tracking data and, at the same time, avoid unrealistic parameter corrections in case of potential correlations between orbital parameters of the user satellite and the TDRS satellite. Finally, a priori standard deviations of $1 \mathrm { m }$ (position), $1 \mathrm { m m / s }$ (velocity), and 0.001 $( C _ { D } , C _ { R } )$ are adopted for the TDRS-4 satellite, which essentially constrains its orbit to the given a priori trajectory. Due to the inadequate coverage of this satellite’s 24-hour orbital period with tracking data, it would not be possible to independently determine or improve its trajectory from the given UARS ranging measurements.

Table 9.10. Adjusted orbit and spacecraft parameters of UARS, TDRS-4 and TDRS-5 for epoch 1999/09/01 00:00 UTC   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>UARS</td><td rowspan=1 colspan=1>TDRS-4</td><td rowspan=1 colspan=1>TDRS-5</td></tr><tr><td rowspan=2 colspan=1>x [m]y[m]z[m]</td><td rowspan=1 colspan=1>+1476163.0± 12.9</td><td rowspan=1 colspan=1>+20174293.6±  1.0</td><td rowspan=4 colspan=1>+40783910.4±13.5+10622602.5±43.5+992611.7±55.1-774.3906±0.0031-2976.0954±0.0007+18.8998±0.0050</td></tr><tr><td rowspan=1 colspan=1>+5996245.6±11.5-3208799.5±17.2</td><td rowspan=1 colspan=1>-37024903.8±  1.0-982925.2±  1.0</td></tr><tr><td rowspan=1 colspan=1>x[m/s]y [m/s]</td><td rowspan=2 colspan=1>-3854.0030±0.0071+3778.3897±0.0163+5302.2419±0.0136</td><td rowspan=2 colspan=1>+2696.9636±0.0003+1471.5076±0.0004-100.5264±0.0010</td></tr><tr><td rowspan=1 colspan=1>[m/s]</td></tr><tr><td rowspan=1 colspan=1>CDCR</td><td rowspan=1 colspan=1>2.6125±0.16321.3002±0.1000</td><td rowspan=1 colspan=1>2.3000±0.00101.3915±0.0010</td><td rowspan=1 colspan=1>2.3000±0.10001.4538±0.0366</td></tr></table>

![](images/5c128695f5a24b07a423a1693244a51c8e7d3895871faa5f18d23c80f380fa35.jpg)  
Fig. 9.11. Residuals of TDRS four-way ranging measurements of the UARS satellite collected on Sept. 1, 1999. Triangles indicate measurements taken via TDRS-4, while diamonds refer to the TDRS-5 relay satellite.

Representative values for the adjusted orbital parameters are given in Table 9.10, while the corresponding residuals are shown in Fig. 9.11. In total, the a priori state vector of the user spacecraft is corrected by about $2 0 0 \mathrm { m }$ and $0 . 1 \mathrm { m } / \mathrm { s }$ , with formal uncertainties being a factor 5 to 10 smaller. The initial state vectors of the TDRS satellites remain essentially unchanged, except for the z-component of the TDRS-5 satellite that is modified by $2 5 \mathrm { m }$ . As expected, the drag coefficients of the geostationary relay satellites are completely unaffected, while the user satellite’s solar radiation pressure coefficient is virtually the same as before the adjustment. On the other hand, the drag coefficient of the user satellite and the solar radiation pressure coefficient of TDRS-5 can be adjusted with good confidence and improved significantly over the default a priori values.

The residuals obtained during the final iteration exhibit an overall measurement and modeling accuracy of $5 { - } 1 0 \mathrm { m }$ . Obviously, the distribution of residuals does not comply with the assumption of random noise but indicates the presence of systematic errors. In the absence of independent tracking data for either the user satellite or the TDRS satellites, it is not, however, possible to uniquely attribute these errors to either an incomplete modeling of perturbative forces, an incomplete account of media corrections in the preprocessing, or systematic errors in the measurement process.

# Appendix A

# A.1 Calendrical Calculations

The civilian calendar which measures time in terms of years, months, and days provides a convenient and well-established time scale for our daily life. It is not, however, well suited to finding the time difference between two dates or advancing a date by a certain time increment. To cope with this difficulty, a continuous day count is often used in astronomical computations, which is known as the Julian Date. It is attributed to Joseph Justus Scaliger, who introduced a “Julian Period” of 7 980 Julian years for chronological purposes (see Derwshowitz & Reingold 1997, Moyer 1981).

The Julian Date (JD) is the number of days since noon January 1, 4 713 BC including the fraction of day. It thus provides a continuous time scale which, for all practical purposes, is always positive. Counting starts at noon for historical reasons, to avoid a change of date in the middle of astronomical observations. Presently, the Julian Day numbers are already quite large (well over two millions) and it is also desirable to start counting at midnight. Therefore, a Modified Julian Date (MJD) is defined as:

$$
\mathrm { M J D } = \mathrm { J D } - 2 4 0 0 0 0 0 . 5 .
$$

A table of Modified Julian Dates for the beginning of each month between 1975 and 2020 is given in Table A.1.

Interconversion to civil calendar date and time is often done by tables, however, there also exist a number of numerical algorithms. The method described here is based upon Meeus (1978, 1991) and requires several points to be considered:

• Civil time is expressed in year $( Y )$ , month $( M )$ , and day $( D )$ . Both $D$ and Julian Day may include fraction of days.   
The years BC are counted astronomically in all formulas. E.g. 1 BC would be the year $Y = 0$ and $1 0 \mathrm { B C }$ corresponds to the year $Y = - 9$ .   
The Julian Day begins at $1 2 ^ { \mathrm { h } }$ o’clock midday.   
The Julian calendar is used until $4 ^ { \mathrm { t h } }$ October 1582 AD, which corresponds to $\mathrm { J D } < 2 2 9 9 1 6 0 . 5$ . The average length of the year in the Julian calendar was taken as 365.25 days which implied one extra day every fourth year. The true length of the mean solar year, however, is about eleven minutes less. By

Table A.1. Modified Julian Date at day 0.0 of each month. To obtain the MJD of a given date, add the day and fractions of day to the tabulated value for the respective month and year. Example: $\mathrm { M J D } ( \dot { 2 } 0 0 0 \mathrm { J a n . } 1 , 1 2 ^ { \mathrm { h } } ) = 5 \dot { 1 } 5 4 3 + 1 . 5 = 5 1 5 4 4 . 5$ .   

<table><tr><td rowspan=1 colspan=1>Year</td><td rowspan=1 colspan=11>JanFebMarAprMay JunJulAugSep OctNov Dec</td></tr><tr><td rowspan=1 colspan=1>19751976</td><td rowspan=10 colspan=11>42412 42443 42471 42502 42532 42563 42593 42624 42655 42685 42716 4274642777 42808 42837 42868 42898 42929 42959 42990 43021 43051 43082 4311243143 43174 43202 43233 43263 43294 43324 43355 43386 43416 43447 4347743508 43539 43567 43598 43628 43659 43689 43720 4375143781 43812 4384243873 43904 43932 43963 43993 44024 44054 44085 44116 44146 44177 4420744238 44269 44298 44329 44359 44390 44420 44451 44482 44512 44543 4457344604 44635 44663 44694 44724 44755 44785 44816 44847 44877 44908 4493844969 45000 45028 45059 45089 45120 45150 45181 45212 45242 45273 4530345334 45365 45393 45424 45454 45485 45515 45546 45577 45607 45638 4566845699 45730 45759 45790 45820 45851 45881 45912 45943 45973 46004 4603446065 46096 46124 46155 46185 46216 46246 46277 46308 46338 46369 46399</td></tr><tr><td rowspan=1 colspan=1>1977</td></tr><tr><td rowspan=1 colspan=1>1978</td></tr><tr><td rowspan=1 colspan=1>1979</td></tr><tr><td rowspan=1 colspan=1>1980</td></tr><tr><td rowspan=1 colspan=1>1981</td></tr><tr><td rowspan=1 colspan=1>1982</td></tr><tr><td rowspan=1 colspan=1>1983</td></tr><tr><td rowspan=1 colspan=1>1984</td></tr><tr><td rowspan=1 colspan=1>1985</td><td rowspan=3 colspan=11>46065 46096 46124 46155 46185 46216 46246 46277 46308 46338 46369 4639946430 46461 46489 46520 46550 46581 46611 46642 46673 46703 46734 4676446795 46826 46854 46885 46915 46946 46976 47007 47038 47068 47099 47129</td></tr><tr><td rowspan=1 colspan=1>1986</td></tr><tr><td rowspan=1 colspan=1>1987</td></tr><tr><td rowspan=1 colspan=1>1988</td><td rowspan=6 colspan=11>47160 47191 47220 4725147281 47312 47342 47373 47404 47434 47465 4749547526 47557 47585 47616 47646 47677 47707 47738 47769 47799 47830 4786047891 47922 47950 47981 48011 48042 48072 48103 48134 48164 48195 4822548256 48287 48315 48346 48376 48407 48437 48468 48499 48529 48560 4859048621 48652 48681 48712 48742 48773 48803 48834 48865 48895 48926 48956</td></tr><tr><td rowspan=1 colspan=1>1989</td><td rowspan=1 colspan=1>475264755747585</td></tr><tr><td rowspan=1 colspan=1>1990</td><td rowspan=1 colspan=1>4789147922 47950</td><td rowspan=6 colspan=4>48256 48287 48315 48346 48376 48407 48437 48468 48499 48529 48560 4859048621 48652 48681 48712 48742 48773 48803 48834 48865 48895 48926 4895648987 49018 49046 49077 49107 49138 49168 49199 49230 49260 49291 49321</td><td rowspan=1 colspan=2>44819548225</td></tr><tr><td rowspan=2 colspan=1>1991</td><td rowspan=2 colspan=1>482564828748315</td></tr><tr><td rowspan=1 colspan=2>485604859</td></tr><tr><td rowspan=1 colspan=1>1992</td><td rowspan=1 colspan=1>486214865248681</td><td rowspan=1 colspan=1>48712</td><td rowspan=2 colspan=5>49742 48773 49803</td></tr><tr><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>489874901849046</td><td rowspan=1 colspan=1>49077</td></tr><tr><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>493524938349411</td><td rowspan=1 colspan=1>49442</td><td rowspan=1 colspan=5>494724950349533</td></tr><tr><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>497174974849776</td><td rowspan=1 colspan=1>49807</td><td rowspan=1 colspan=3>4983749868</td><td rowspan=1 colspan=3>4986849898</td><td rowspan=3 colspan=3>50082 50113 50142 50173 50203 50234 50264 50295 50326 50356 50387 50417</td></tr><tr><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>50082 5011350142</td><td rowspan=1 colspan=1>50173</td><td rowspan=1 colspan=3>5020350234</td><td rowspan=1 colspan=2>50264</td><td></td></tr><tr><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>50448 50479 50507</td><td rowspan=1 colspan=1>50538</td><td rowspan=1 colspan=1>50568</td><td rowspan=1 colspan=2>50599</td><td rowspan=1 colspan=2>50629</td><td></td><td rowspan=3 colspan=3>310563148651171141</td><td rowspan=1 colspan=1>50782</td></tr><tr><td rowspan=1 colspan=1>1998</td><td rowspan=1 colspan=1>50813 5084450872</td><td rowspan=1 colspan=1>50903</td><td rowspan=1 colspan=1>50933</td><td rowspan=1 colspan=2>50964</td><td rowspan=1 colspan=2>50994</td><td rowspan=1 colspan=1>51025</td><td rowspan=1 colspan=2>5105651086 51117 51</td></tr><tr><td rowspan=1 colspan=1>1999</td><td rowspan=1 colspan=1>51178 51209 51237</td><td rowspan=1 colspan=1>51268</td><td rowspan=1 colspan=1>51298</td><td rowspan=1 colspan=2>51329</td><td rowspan=1 colspan=2>51359</td><td rowspan=1 colspan=1>51390</td></tr><tr><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>515435157451603</td><td rowspan=1 colspan=1>51634</td><td rowspan=1 colspan=1>51664</td><td rowspan=2 colspan=4>51695 51725</td><td rowspan=1 colspan=1>51756</td><td rowspan=2 colspan=3>51787 51817 51843 51878</td></tr><tr><td rowspan=1 colspan=1>2001</td><td rowspan=1 colspan=1>51909 51940 51968</td><td rowspan=1 colspan=1>51999</td><td rowspan=1 colspan=1>52029</td><td rowspan=1 colspan=1>52121</td></tr><tr><td rowspan=1 colspan=1>2002</td><td rowspan=1 colspan=1>5227452305 52333</td><td rowspan=1 colspan=1>52364</td><td rowspan=1 colspan=1>52394</td><td rowspan=1 colspan=2>52425</td><td rowspan=1 colspan=2>52455</td><td rowspan=1 colspan=1>52486</td><td rowspan=1 colspan=3>52517525475257852608</td></tr><tr><td rowspan=1 colspan=1>2003</td><td rowspan=1 colspan=1>526395267052698</td><td rowspan=1 colspan=1>52729</td><td rowspan=1 colspan=1>52759</td><td rowspan=1 colspan=4>5279052820</td><td rowspan=1 colspan=1>52851</td><td rowspan=1 colspan=3>52882529125294352973</td></tr><tr><td rowspan=1 colspan=1>2004</td><td rowspan=1 colspan=1>530045303553064</td><td rowspan=1 colspan=6>53095531255315653186</td><td rowspan=1 colspan=1>53217</td><td rowspan=1 colspan=3>53248532785330953339</td></tr><tr><td rowspan=1 colspan=1>2005</td><td rowspan=1 colspan=1>53370 53401 53429</td><td rowspan=1 colspan=6>53460 53490 53521 53551</td><td rowspan=1 colspan=1>53582</td><td rowspan=1 colspan=3>：53613 53643536745370</td></tr><tr><td rowspan=1 colspan=1>2006</td><td rowspan=1 colspan=1>537355376653794</td><td rowspan=1 colspan=1>53825</td><td rowspan=1 colspan=5>538555388653916</td><td rowspan=1 colspan=1>53947</td><td rowspan=1 colspan=3>53978540085403954069</td></tr><tr><td rowspan=1 colspan=1>2007</td><td rowspan=1 colspan=1>54100 54131 54159</td><td rowspan=1 colspan=1>54190</td><td rowspan=1 colspan=5>54220 54251 54281</td><td rowspan=1 colspan=1>54312</td><td rowspan=2 colspan=3>5434354373 54470 54434</td></tr><tr><td rowspan=1 colspan=1>2008</td><td rowspan=1 colspan=1>54465 54496 54525</td><td rowspan=1 colspan=7>5455654586546175464754678</td></tr><tr><td rowspan=1 colspan=1>2009</td><td rowspan=1 colspan=1>548315486254890</td><td rowspan=1 colspan=6>54921549515498255012</td><td rowspan=1 colspan=1>55043</td><td rowspan=1 colspan=3>55074551045513555165</td></tr><tr><td rowspan=1 colspan=1>2010</td><td rowspan=2 colspan=8>55196 55227 55255 55286 55316 55347 55377 55408 55439 55469 55500 5553055561 55592 55620 55651 55681 55712 55742 55773 55804 55834 55865 55895</td><td rowspan=1 colspan=1>55408</td><td rowspan=2 colspan=2>55439 55469 55500536</td></tr><tr><td rowspan=1 colspan=1>2011</td><td></td></tr><tr><td rowspan=1 colspan=1>2012</td><td rowspan=1 colspan=8>55926 55957 55986 56017 56047 56078 56108 56139 56170 56200 56231 56261</td><td rowspan=9 colspan=3>55926 55957 55986 56017 56047 56078 56108 56139 56170 56200 56231 5626156292 56323 56351 56382 56412 56443 56473 56504 56535 56565 56596 5662656657 56688 56716 56747 56777 56808 56838 56869 56900 56930 56961 5699157022 57053 57081 57112 57142 57173 57203 57234 57265 57295 57326 5735657387 57418 57447 57478 57508 57539 57569 57600 57631 57661 57692 5772257753 57784 57812 57843 57873 57904 57934 57965 57996 58026 58057 5808758118 58149 58177 58208 58238 58269 58299 58330 58361 58391 58422 5845258483 58514 58542 58573 58603 58634 58664 58695 58726 58756 58787 5881758848 58879 58908 58939 58969 59000 59030 59061 59092 59122 59153 59183</td></tr><tr><td rowspan=1 colspan=1>2013</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2014</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2015</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2016</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2017</td><td rowspan=1 colspan=5>57753 5778457812578435787357904</td><td rowspan=1 colspan=2>04579</td><td></td></tr><tr><td rowspan=2 colspan=1>20182019</td><td rowspan=1 colspan=4>581185814958177582085823858</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=5>58483 58514 58542 58573 58603 58634 58664 58695 58726 58756 58787 58817</td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>2020</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

1582 AD the error in the Julian calendar, which was introduced in $4 5 ~ \mathrm { B C }$ , had accumulated to more than ten days. This led to the calendar reform under Pope Gregory XIII.

The Gregorian calendar is used from $1 5 ^ { \mathrm { t h } }$ October 1582 AD onwards corresponding to $\mathrm { J D } \geq 2 2 9 9 1 6 0 . 5 .$ The average length of the year in this calendar is 365.2425 days which deviates by less than half a minute from the mean solar year of 365.2422 days. In practice this is accomplished by inserting one extra day every fourth year, but omitting this three times per four hundred years. By convention, every year whose number can be divided by four is a leap year except when it is also divisible by one hundred. However, those years where the year number is divisible by four hundred are again leap years. In leap years the intercalary day $2 9 ^ { \mathrm { t h } }$ February is inserted.

The function entier $( x )$ or, briefly, $[ x ]$ will be used extensively in the subsequent algorithms. It is defined as the smallest integer which is smaller than or equal to $x$ , i.e.

$$
[ x ] \leq x < [ x ] + 1 .
$$

For positive numbers $[ x ]$ is equal to the integral part $\operatorname { i n t } ( x )$ of $x$ . For negative (noninteger) numbers, however, it is the integral part of $x$ minus one. Negative arguments have been carefully avoided in the expressions given below. The entier $( x )$ function can therefore also be written as $\operatorname { i n t } ( x )$ for all permitted dates.

# A.1.1 Modified Julian Date from the Calendar Date

The handling of leap years in the computation of the Modified Julian Date is facilitated by letting the year run from March 1 until the end of February. To this end $Y$ and $M$ are replaced by the quantities

$$
y = { \left\{ \begin{array} { l l } { Y - 1 } & { { \mathrm { i f ~ } } M \leq 2 } \\ { Y } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

and

$$
m = \left\{ \begin{array} { l l } { { M + 1 2 } } & { { \mathrm { i f } \ M \leq 2 } } \\ { { M } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. .
$$

The number of days since March 1 at the beginning of a month $M$ can then be expressed as $[ 3 0 . 6 ( m + 1 ) ] - 1 2 2$ as illustrated in Table A.2.

Leap days in the Julian and Gregorian Calendar are taken into account by the auxiliary quantity

$$
B = \left\{ \begin{array} { l l } { { - 2 + [ ( y + 4 7 1 6 ) / 4 ] - 1 1 7 9 } } & { { \mathrm { u n t i l ~ } 4 \mathrm { O c t . ~ } 1 5 8 2 } } \\ { { + [ y / 4 0 0 ] - [ y / 1 0 0 ] + [ y / 4 ] } } & { { \mathrm { f r o m ~ } 1 0 \mathrm { O c t . ~ } 1 5 8 2 } } \end{array} \right. .
$$

The Modified Julian Date including the fraction of day, is then given by:

$$
\mathrm { M J D } = 3 6 5 y - 6 7 9 0 0 4 + B + [ 3 0 . 6 0 0 1 ( m + 1 ) ] + D
$$

Table A.2. Annual day count   

<table><tr><td>Month</td><td>Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>M</td><td>34</td><td>5</td><td>678</td><td></td><td></td><td>8 9</td><td>1011</td><td></td><td>12</td><td></td><td></td></tr><tr><td>Days</td><td>31</td><td>30 31</td><td></td><td>30313</td><td>31</td><td></td><td>3031</td><td>30 </td><td></td><td>3131</td><td></td></tr><tr><td>[30.6(m+1)]- 122</td><td>0</td><td>31 61</td><td></td><td></td><td></td><td>92 122 153 184 214 245 275 306 337</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Here, the multiplication factor of $m + 1$ is taken as 30.6001 rather than 30.6 in order to avoid numerical errors in case of limited floating-point accuracy.

Some simplifications are possible, if only a limited time interval is considered. E.g. $B$ can be replaced by a fixed value of $- 1 5 + [ Y / 4 ]$ between 1 March 1900 and 28 February 2100, because the year 2000 is a regular leap year.

# A.1.2 Calendar Date from the Modified Julian Date

The computation of the calendar date from the Modified Julian Date requires a number of intermediate steps. First, the integer Julian Day (i.e. the Julian Date at noon) is determined:

$$
a = [ \mathrm { M J D } ] + 2 4 0 0 0 0 1 ~ .
$$

At the same time the fraction of day, $q$ , is given by the decimal part of the Modified Julian Date:

$$
q = \mathrm { M J D } - \mathrm { [ M J D ] } \quad .
$$

Two auxiliary quantities $b$ and $c$ are defined as

$$
b = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } a < 2 2 9 9 1 6 1 { \mathrm { ~ ( J u l i a n ~ c a l e n d a r ) } } } \\ { \operatorname { [ } ( a - 1 8 6 7 2 1 6 . 2 5 ) / 3 6 5 2 4 . 2 5 { \mathrm { ] } } } & { { \mathrm { o t h e r w i s e ~ ( G r e g o r i a n ~ c a l e n d a r ) } } } \end{array} \right. }
$$

and

$$
c = { \left\{ \begin{array} { l l } { a + 1 5 2 4 } & { { \mathrm { ~ i f ~ } } a < 2 2 9 9 1 6 1 { \mathrm { ~ ( J u l i a n ~ c a l e n d a r ) } } } \\ { a + b - [ b / 4 ] + 1 5 2 5 } & { { \mathrm { ~ o t h e r w i s e ~ ( G r e g o r i a n ~ c a l e n d a r ) } } \quad . } \end{array} \right. }
$$

The next step is to calculate the auxiliary quantities

$$
\begin{array} { l } { d = \left[ \left( c - 1 2 1 . 1 \right) / 3 6 5 . 2 5 \right] } \\ { \ } \\ { e = \left[ 3 6 5 . 2 5 d \right] } \end{array} \mathrm { ~ , ~ }
$$

and

$$
f = [ ( c - e ) / 3 0 . 6 0 0 1 ] ~ .
$$

Finally, the calendar date is obtained from the following three steps: the day of the month $( D )$ is given by

$$
D = c - e - [ 3 0 . 6 0 0 1 f ] + q ,
$$

the month of the year $( M )$ follows from

$$
M = f - 1 - 1 2 [ f / 1 4 ]
$$

and the year $( Y )$ in astronomical reckoning is determined by

$$
Y = d - 4 7 1 5 - [ ( 7 + M ) / 1 0 ] .
$$

It is again possible to simplify the computation somewhat if only a limited time interval is considered. E.g. the computation of the auxiliary quantities $a , b$ , and $c$ can be focussed into $c = [ ( \mathrm { J D } + 0 . 5 ) ] + 1 5 3 7$ if only the interval March 1900 until 2100 is taken into account.

# A.2 GPS Orbit Models

The Global Positioning System (GPS) makes use of two dedicated representations of the GPS satellite orbits, which are known as almanac and (broadcast) ephemeris1. Both parameter sets are transmitted as part of the GPS navigation message and enable a GPS receiver to compute positions of the GPS satellites with different levels of accuracy. Almanac data are mainly used to determine the constellation of visible satellites above the horizon, to select the best satellites for navigation, and to determine approximate Doppler shifts for improved signal acquisition. The ephemeris parameters, on the other hand, provide a much more accurate description of the spacecraft trajectory that is essential for the computation of precise user-position fixes. In accord with the envisaged usage, the low-accuracy almanac parameters are always provided for the full constellation of active satellites, whereas each satellite transmits ephemeris parameters for itself, only.

Conceptionally, both the almanac and the ephemeris model are based on a Keplerian elements representation of the orbit with a suitably chosen set of correction terms modeling any deviation from an unperturbed ellipse. This enables a particularly compact parameter set at the price of a moderate computational burden. For further details the reader is referred to the respective Navstar GPS Interface Control Document (ICD-GPS-200 1997) as well as van Dierendonck et al. (1978). The latter reference addresses the rational behind the design of the GPS navigation message and the recommended computational algorithms.

Table A.3. Conventional values of specific constants employed in GPS almanac and ephemeris models (ICD-GPS-200, 1997)   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>GM</td><td rowspan=2 colspan=1>398600.5.109 m/s²7.2921151467:10-5s-13.1415926535898</td><td rowspan=2 colspan=1>WGS84 Gravitational coefficientWGS84 Earth rotation rate</td></tr><tr><td rowspan=1 colspan=1>Wπ</td></tr></table>

By convention a specific set of constants based on the (old) WGS84 system is to be applied in both the almanac and ephemeris models that is reproduced in Table A.3. Readers should be aware that the latest refinement of WGS84 constants (NIMA 1997) has not resulted in an update of the above standard.

Times are referred to the GPS system time, which differs from TAI by a constant offset of $1 9 \mathrm { s }$ and matched UTC when it was introduced in January 1980. The standard epoch 6.0 January 1980 GPS Time (JD(GPS) 2 444 244.5) serves as origin for the GPS specific week count. A GPS week starts on Sunday 0.00 GPS Time and the first week, starting at the standard epoch, is assigned the week count 0.

Accordingly, the week number for arbitrary dates is given by

$$
\mathrm { W N } = \left[ { \frac { \mathrm { J D } ( \mathrm { G P S } ) - 2 4 4 4 2 4 4 . 5 } { 7 } } \right]
$$

where brackets denote the entier function introduced in (A.2). Vice versa, GPS week WN starts at Julian Date

$$
\mathrm { J D } ( \mathrm { G P S } ) = 2 4 4 4 2 4 4 . 5 + 7 \cdot \mathrm { W N } .
$$

Within a GPS week, times are typically specified in seconds past the start of week, yielding a count of at most $6 0 4 8 0 0 { \mathrm { s } }$ .

# A.2.1 Almanac Model

Aside from the reference epoch, the almanac message of each satellite comprises a total of seven orbit-related parameters (Table A.4). These resemble the classical Keplerian elements but differ in various GPS-specific details. Instead of the semimajor axis, its square root is given in the almanac to simplify computation of the mean motion. The inclination is specified relative to a reference value of $i _ { \mathrm { r e f } } =$ $5 4 ^ { \circ }$ , which is about one degree smaller than the nominal inclination of the GPS constellation. All angular elements are given in units of semi-circles equivalent to $\pi$ radians or $1 8 0 ^ { \circ }$ . Special care is required in the interpretation of $\varOmega _ { 0 }$ which must not be confused with the inertial right ascension $\varOmega$ of the ascending node as used with classical Keplerian elements. To be precise, $\varOmega _ { 0 }$ defines the orientation of the orbital plane at the almanac reference epoch, but referred to the Greenwich meridian at the start of the respective GPS week. The parameter is thus related to the right ascension of the ascending node $\varOmega$ and the Greenwich Sidereal Time $\Theta$ by the expression

$$
\varOmega _ { 0 } = \varOmega ( t _ { \mathrm { a } } ) - \theta ( t _ { 0 } ) \quad ,
$$

where $t _ { 0 }$ denotes the start of the GPS week and $t _ { \mathrm { a } }$ is the almanac reference epoch (as defined by the $\mathrm { W N _ { o a } }$ and $t _ { \mathrm { o a } }$ counts). Due to the Earth’s oblateness the inertial right ascension of the ascending node experiences a secular change of $\dot { \Omega } \approx - 0 . 0 4 ^ { \circ } / \mathrm { d }$ , which is also specified as part of the almanac message. This allows the instantaneous Greenwich longitude $\lambda _ { \varOmega }$ of the ascending node to be computed from

$$
\begin{array} { l l l } { \lambda _ { \Omega } ( t ) } & { = } & { \Omega ( t ) - \theta ( t ) } \\ & { \approx } & { \Omega ( t _ { \mathrm { a } } ) + \dot { \Omega } ( t - t _ { \mathrm { a } } ) - \theta ( t _ { 0 } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \\ & { = } & { \Omega _ { 0 } + \dot { \Omega } ( t - t _ { \mathrm { a } } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \end{array}
$$

for arbitrary times $t$ . After solving Kepler’s equation

$$
E - e \sin ( E ) = M = M _ { 0 } + { \sqrt { \frac { G M _ { \oplus } } { a ^ { 3 } } } } ( t - t _ { \mathrm { a } } )
$$

Table A.4. GPS almanac parameters   

<table><tr><td>Parameter</td><td>Description</td><td>Units</td></tr><tr><td>WNoa</td><td>Almanac reference epoch (part 1): GPS week number (mod 256) Almanac reference epoch (part 2):</td><td>[s]</td></tr><tr><td>√a</td><td>fraction of current GPS week Square root of semi-major axis</td><td>[√m]</td></tr><tr><td>e Si</td><td>Eccentricity Inclination offset from reference value of</td><td>[semi-circles]</td></tr><tr><td></td><td>iref = O.3 semi-circles</td><td></td></tr><tr><td>小</td><td>Longitude of the ascending node at the weekly epoch</td><td>[semi-circles]</td></tr><tr><td></td><td>Rate of change of the right ascension of the ascending node</td><td>[semi-circles/s]</td></tr><tr><td>w Mo</td><td>Argument of perigee Mean anomaly at reference epoch</td><td>[semi-circles] [semi-circles]</td></tr><tr><td>ao a1</td><td>Spacecraftclock offset from GPS time Clock frequency offset</td><td>[s] [s/s]</td></tr></table>

for the eccentric anomaly at the time of interest, the position of the GPS satellite in the Earth-fixed WGS84 system can be computed from the common expressions

$$
r _ { \mathrm { W G S 8 4 } } = R _ { z } ( - \lambda _ { \itOmega } ) R _ { x } ( - i _ { \mathrm { r e f } } - \delta _ { i } ) R _ { z } ( - \omega ) \left( \begin{array} { c } { { a \left( \cos { E } - e \right) } } \\ { { a \sqrt { 1 - e ^ { 2 } } \sin { E } } } \\ { { 0 } } \end{array} \right)
$$

of the two-body problem (cf. Chap. 2). An alternative, but mathematically equivalent computational scheme is specified in ICD-GPS-200 (1997) for use within GPS receivers. It takes care of the GPS specific data representation and should be used instead of the generalized formulation introduced above whenever full consistency with the ICD is desired.

# A.2.2 Broadcast Ephemeris Model

The model associated with the GPS ephemeris parameters is essentially similar to the almanac model introduced above, but provides for a better representation of the GPS orbits by additional secular and periodic perturbations. For reference, the full parameters set is reproduced in Table A.5.

The ephemeris model first applies a correction $\varDelta n$ to the computed mean motion. Accordingly, Kepler’s equation for the eccentric anomaly is solved with a value

$$
M = M _ { 0 } + \left( \sqrt { \frac { G M _ { \oplus } } { a ^ { 3 } } } + \varDelta n \right) \left( t - t _ { \mathrm { e } } \right)
$$

Table A.5. GPS broadcast ephemeris parameters   

<table><tr><td rowspan=1 colspan=3>Parameter</td><td rowspan=1 colspan=4>Description</td><td rowspan=1 colspan=1>Units</td></tr><tr><td rowspan=1 colspan=3>WNoe</td><td rowspan=2 colspan=4>Ephemeris reference epoch (part 1):GPS week number (mod 1024)Ephemeris reference epoch (part2):fraction of current GPS week</td><td rowspan=2 colspan=1>[s]</td></tr><tr><td rowspan=1 colspan=3>toe</td></tr><tr><td rowspan=1 colspan=3>√a</td><td rowspan=2 colspan=4>Square root of semi-major axisCorrection to mean motion</td><td rowspan=2 colspan=1>[√m][semi-circles/s]</td></tr><tr><td rowspan=1 colspan=3>△n</td></tr><tr><td rowspan=1 colspan=3>e</td><td rowspan=2 colspan=4>EccentricityInclination at reference epoch</td><td rowspan=2 colspan=1>[semi-circles]</td></tr><tr><td rowspan=1 colspan=3>io</td></tr><tr><td rowspan=1 colspan=3>di/dt</td><td rowspan=3 colspan=4>Rate of change of inclinationLongitude of the ascending node at theweekly epoch</td><td rowspan=3 colspan=1>[semi-circles/s][semi-circles]</td></tr><tr><td rowspan=1 colspan=3>20</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=3 colspan=1></td><td rowspan=3 colspan=4>Rate of change of the right ascension of theascending node</td><td rowspan=4 colspan=1>[semi-circles/s][semi-circles]</td></tr><tr><td></td><td></td><td rowspan=2 colspan=2></td></tr><tr><td></td><td></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=3>w</td><td rowspan=1 colspan=4>Argument of perigee</td></tr><tr><td rowspan=1 colspan=3>Mo</td><td rowspan=1 colspan=4>Mean anomaly at reference epoch</td><td rowspan=3 colspan=1>[semi-circles][m][rad]</td></tr><tr><td rowspan=1 colspan=3>Crc,Crs</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the orbital radius</td></tr><tr><td rowspan=1 colspan=3>Cuc,Cus</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the argument of latitude</td></tr><tr><td rowspan=1 colspan=3>Cic,Cis</td><td rowspan=1 colspan=4>Amplitude of (co)sine harmonic correctionterm to the inclination</td><td rowspan=1 colspan=1>[rad]</td></tr><tr><td rowspan=1 colspan=3>afo</td><td rowspan=1 colspan=4>Spacecraft clock offset from GPS time</td><td rowspan=1 colspan=1>[s]</td></tr><tr><td rowspan=1 colspan=3>af1</td><td rowspan=1 colspan=4>Clock frequency offset</td><td rowspan=1 colspan=1>[s/s]</td></tr><tr><td rowspan=1 colspan=3>af2</td><td rowspan=1 colspan=4>Clock frequency drift</td><td rowspan=1 colspan=1>[s/s2]</td></tr></table>

of the mean anomaly. Here $t _ { \mathrm { e } }$ is the ephemeris reference epoch as defined by the counters $\mathrm { W N _ { o e } }$ and $t _ { \mathrm { o e } }$ . Based on the perifocal coordinates

$$
\begin{array} { l c l } { { \hat { x } } } & { { = } } & { { a \left( \cos E - e \right) } } \\ { { \hat { y } } } & { { = } } & { { a { \sqrt { 1 - e ^ { 2 } } } \sin E } } \end{array}
$$

one obtains the (uncorrected) argument of latitude

$$
\bar { u } = \omega + \arctan ( \hat { y } / \hat { x } )
$$

from which the periodic corrections

$$
\begin{array} { c c c c c } { { \delta r } } & { { = } } & { { C _ { r s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { r c } \cos ( 2 \bar { u } ) } } \\ { { \delta u } } & { { = } } & { { C _ { u s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { u c } \cos ( 2 \bar { u } ) } } \\ { { \delta i } } & { { = } } & { { C _ { i s } \sin ( 2 \bar { u } ) } } & { { + } } & { { C _ { i c } \cos ( 2 \bar { u } ) } } \end{array}
$$

to the argument of latitude $( u )$ , the radius $( r )$ , and the inclination $( i )$ can be computed. Making use of the appropriately corrected elements

$$
\begin{array} { l c l } { r } & { = } & { a \left( 1 - e \cos E \right) + \delta r } \\ { u } & { = } & { \bar { u } + \delta u } \\ { i } & { = } & { i _ { 0 } + d i / d t \left( t - t _ { \mathrm { e } } \right) + \delta i } \\ { \lambda _ { \Omega } } & { = } & { \Omega _ { 0 } + \dot { \Omega } ( t - t _ { \mathrm { e } } ) - \omega _ { \oplus } ( t - t _ { 0 } ) } \end{array}
$$

one finally obtains the desired position

$$
r _ { \mathrm { W G S 8 4 } } = R _ { z } ( - \lambda _ { \itOmega } ) { \bf R } _ { x } ( - i ) \left( \begin{array} { c } { { r \cos u } } \\ { { r \sin u } } \\ { { 0 } } \end{array} \right) .
$$

Again, a slightly different, but mathematically equivalent formulation is specified in ICD-GPS-200 (1997). It should be applied whenever full consistency with the ICD is desired.

# Appendix B

As a supplement to this book, additional resources are provided on Springer’s Extra Materials Server http://extra.springer.com/. Owners of the printed book can download a zip archive SatOrbEM.zip after entering the ISBN number. .Downloading this content should require a code given in the printed book

# B.1 Internet Resources

A wealth of data as well as software that could not be provided within this book is available via the Internet and the World Wide Web. We have, therefore, compiled a set of useful URL resources with a focus on data that require frequent updates. All addresses may conveniently be accessed via the hyperlink file SAT.html available in the SatOrbEM.zip archive. Links are ordered by topics and accompanied by brief textual descriptions (cf. Fig. B.1). It is emphasized, however, that the given list is in no way comprehensive and that server names and files are subject to changes without further notice.

![](images/a8485a6c91ac1ffe406d69724622b04f8ff11d202b0fc2888bacceda77cb36f5.jpg)  
Fig. B.1. Useful internet links provided in SAT.html

# B.2 Source Codes on Springer’s Extra Materials Server

# B.2.1 Contents

The SatOrbEM.zip archive on the Extra Materials server provides a comprehensive library of $\mathrm { C } { + + }$ modules as well as programs to solve the exercises given at the end of each chapter. After downloading the archive and unapcking it to a working directory (here C:\Sat) the following directories and files are obtained.

Directory Description   
C:\Sat\Source\ Source codes of library modules (header and implementatio files) SAT_Const.h, SAT_DE.h, SAT_DE.cpp, SAT_Filter.h, SAT_Filter.cpp, SAT_Force.h, SAT_Force.cpp, SAT_Kepler.h, SAT_Kepler.cpp, SAT_RefSys.h, SAT_RefSys.cpp, SAT_Time.h, SAT_Time.cpp, SAT_VecMat.h, SAT_VecMat.cpp Source codes for solutions to exercises Exercise_2_1.cpp, …, Exercise_2_6.cpp, Exercise_3_1.cpp, …, Exercise_3_4.cpp, Exercise_4_1.cpp, …, Exercise_4_3.cpp, Exercise_5_1.cpp, …, Exercise_5_3.cpp, Exercise_6_1.cpp, …, Exercise_6_4.cpp, Exercise_7_1.cpp, Exercise_8_1.cpp, …, Exercise_8_3.cpp Application programs GEODA.cpp, RTOD.cpp, TDRSOD.cpp \InOut\ Output of exercise programs Exercise_2_1.out, …, Exercise_8_3.out Input data for application programs GEODA_A1.inp, …, GEODA_C2.inp, RTOD_A.inp, …, RTOD_C.inp, RTOD.dat, TDRSOD.inp, TDRSOD.dat Output of application programs GEODA_A1.out, …, GEODA_C2.out, RTOD_A.out, …, RTOD_C.out TDRSOD.out \Win32\ Executable programs (Windows 32-bit Version) GEODA.exe, RTOD.exe, TDRSOD.exe \Linux\ Executable programs (Linux Version) GEODA, RTOD, TDRSOD Unix archives of input/output files, executable programs (Linu only) and source code (incl. makefile) satio.tar, satexe.tar, satsrc.tar

The SAT_Lib library comprises elementary operators, functions, and classes, which are common to the various exercises but may also be applied by the reader to develop his/her own applications. In total the library comprises nine modules, each covering a specific and well defined scope:

SAT_Const.h Mathematical and astronomical constants   
SAT_DE.h Numerical integration of differential equations   
SAT_Filter.h Kalman filtering and least-squares estimation   
SAT_Force.h Satellite force model   
SAT_Kepler.h Keplerian orbit computation   
SAT_RefSys.h Reference system transformations   
SAT_Time.h Calendrical computations   
SAT_VecMat.h Vector and matrix arithmetics

Making use of the header files $\mathrm { S A T _ { - } } * .$ h, the required modules can be included into the application programs in an easy way. The associated implementations are provided in the corresponding files SAT_ $^ *$ .cpp , which can be compiled separately and linked in the form of object or library files. Excluded from this is the SAT_Const module, which requires no implementation part and consists of a header file only.

# B.2.2 System Requirements

For a painless application of the programs we recommend the installation on a personal computer with the following minimum characteristics:

• Intel processor 1 GHz or equivalent,   
• 256 MB memory, $1 0 0 \mathrm { M B }$ free hard disk space, CD drive,   
Windows XP/7 or OpenSuSE Linux 10.3 operating system,   
Microsoft Visual Studio 2005 (Windows) or GNU $\mathrm { C } { + } { + } 4 . 2$ (Linux).

# B.2.3 Executing the Programs

The SatOrbEM.zip archive on the Extra Materials server contains pre-compiled versions of the application programs described in Chap. 9. To run these programs on a PC with the Windows operating system unpack the archive as discussed above and copy the files in the C:\Sat\Win32 folder to an appropriate working directory (e.g., C:\Sat\Exe) on the hard disk. The input data files from the folder Sat\InOut folder should then be copied to the same folder. After the command interpreter has been started (by running cmd.exe) and switching to the chosen program folder, the individual programs may be run as in the following example:

Iteration 1

<table><tr><td>Date</td><td>UTC</td><td>Sta TDRS</td><td></td><td>obs</td><td>[m]</td><td>comp [m]</td><td>o-c[m]</td></tr><tr><td></td><td>1999/09/01 00:22:01.000</td><td>162</td><td>5</td><td></td><td></td><td>79010.2586 79010.2408</td><td>17.78</td></tr></table>

For all programs the input files may be specified in the command line (see Table B.1). Using the redirection operator $( > )$ , the default screen output may, furthermore, be written to an arbitrary output file.

Table B.1. Executing the application programs with optional command-line arguments   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Arguments</td><td rowspan=1 colspan=1>Default setup</td><td rowspan=1 colspan=1>Default data</td></tr><tr><td rowspan=1 colspan=1>GEODARTODTDRSOD</td><td rowspan=1 colspan=1>[setup-file] [&gt;output-file][setup-file[data-file]] [&gt;output-file][setup-file[data-file]] [&gt;output-file]</td><td rowspan=1 colspan=1>GEODA.inpRTOD.inpTDRSOD.inp</td><td rowspan=1 colspan=1>RTOD.datTDRSOD.dat</td></tr></table>

The advice just given applies in a similar manner to running the programs under Linux. After creating a suitable directory and copying the files from the unpacked archive, the programs may be started by entering the corresponding program names, provided the working directory is contained in the path. As under Windows, input and output files may be specified in the command line under Linux.

If the names of the input data files are not correctly reproduced under Linux upon reading the CD, there is a Unix tar archive available. This may be unpacked with the commands

tar -xvf /cdrom/Sat/Linux/satio.tar and copied into the current working directory.

# B.2.4 Compilation and Linking

In the sequel, the basic steps for generating executable programs under the Windows and Linux operating systems are described.

For use under the Windows operating system, we assume that all source files are available in a subdirectory C:\Sat\Source\ after unpacking the archive from the Extra Materials Server. Within with Microsoft Visual Studio 2005, the various programs (for exercises and applications) as well as a common library are treated as individual “projects”. These projects are combined in a common workspace or “solution”. After starting Visual Studio, a first project is created through the Project.New Project menu to build the library from the generic modules. This library can later be linked to the individual programs. Within the New Project dialog, an Empty Project is selected from the available templates. Furthermore, the project’s Name (SAT_Lib) as well the desired Location (C:\Sat) and Solution Name (Prj) need to be specified. The latter items define the root directory (C:\Sat\Prj)

for all files maintained by Visual Studio within the current set of projects. Confirm by $O K$ to complete the allocation of this project and the overall workspace. Subsequently the source and header files of the library modules are added to the SAT_Lib project by calling the menu Project.Add Existing Item ... and selecting all files within the C:\Sat\Source\ folder, which adhere to the naming scheme $\mathrm { S A T \_ } * . *$ . By default, Visual Studio will try to build an exectuable program from these source files. Therefore, it is necessary to change the Configuration type in the Configuration Properties.General.Project Defaults field of the Project.Properties menu of the SAT_Lib project from Application (\*.exe) to Static Library (.lib). Now, the library can be completed by selecting the Build.Build SAT_Lib menu. Visual Studio compiles all source files and then links the resulting object files into a static library SAT_Lib.lib.

The Exercises Exercise_2_1 to Exercise_8_3 and the application programs (GEODA, RTOD, TDRSOD) are treated as independent projects within the Sat\Prj workspace. In the sequel this is illustrated for the RTOD program. Start the New Project dialog from the File.Add.New Project menu. Then select an Empty Project, specify its Name (RTOD) and Location (C:\Sat\Prj). Select the new project in the “Solution Explorer”, then add the source file RTOD from the source directory via the Project.Add Existing Item ... dialog. Finally, select the Project.Project dependencies ... menu and check the SAT_Lib check box in the resulting dialog. This makes the respective header files known to the compiler and informs the builder that this library is required for linking the RTOD program. The executable module RTOD.exe is finally created by selecting Build.Build RTOD and can subsequently be found in the C:\Sat\Prj\debug folder. For further hints we refer to the comprehensive documentation of the Microsoft $\mathrm { C } { + } { + }$ compiler and the Visual Studio environment.

Under the Linux operating system the individual programs can directly by built from a console using the GNU $\mathrm { C } { + + }$ compiler. Again, it is advisable to combine all modules $\mathtt { S A T \_ * }$ in a library libSAT.a using the shell commands:

$> \mathrm { g + + \Delta \mathcal { - } c } \ \mathrm { S A T * . c }$ pp # Compilation of library modules $>$ ar rc libSAT.a $\mathtt { S A T * }$ .o # Generation of library from object files

Assuming that all relevant files are contained in the same directory, the main programs can subsequently be built by the commands

$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ Exercise_2_1.cpp -o Exercise_2_1 -lSAT -L.   
$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ Exercise_2_2.cpp -o Exercise_2_2 -lSAT -L.   
$>$ ...   
$\mathrm { ~ \tt ~ { ~ E ^ { + + } } ~ }$ TDRSOD.cpp -o TDRSOD -lSAT -L.

For ease of use, a make file is provided as part of the satsrc.tar archive, which performs all steps in a single run.

# B.2.5 Index of Library Functions

The following compilation summarizes all identifiers of public types, constants, functions, and classes provided by the individual modules.

$< <$ Output operator for dates, vectors, and matrices   
() Access to vector and matrix components   
$=$ Assignment of vectors and matrices   
$^ +$ Addition of vectors and matrices   
$+ =$ Vector addition   
- Subtraction of vectors and matrices   
- Unary minus (vector, matrix)   
-= Vector subtraction   
$^ *$ Multiplication (scalar, vector, matrix)   
/ Division by a scalar   
abserr Public element of DE class specifying the absolute accuracy requirement   
AccelDrag Acceleration due to atmospheric drag   
AccelHarmonic Acceleration due to harmonic gravity field of central body   
AccelMain Total acceleration of an Earth-orbiting satellite   
AccelPointMass Acceleration due to point-mass perturbation   
AccelSolrad Acceleration due to solar radiation pressure   
Accumulate Method of class LSQ for accumulation of data equations   
Arcs Arcseconds per radian   
AU Astronomical unit [m]   
AzEl Azimuth, elevation and, optionally, partials from local tangential coordinates [m]   
CalDat Calendar date and time   
c_light Velocity of light [m/s]   
Col Column vector of a matrix   
Cov Method of class EKF returning the current covariance   
Cov Method of class LSQ for covariance computation   
Cross Cross product of 3-dimensional vectors   
Date Auxiliary class for output of dates   
Data Method of class LSQ returning the transformed right-hand side of the data equations   
DE Class for numerical solution of differential equations   
DE_BADACC Enumerator of type DE_STATE (Flag for too stringent accuracy requirements)   
DE_DONE Enumerator of type DE_STATE (Flag for successful integration step)   
Define Method of DE class defining the differential equation   
DEfunct Function prototype for differential equations   
Deg $1 8 0 ^ { \circ } / \pi$   
DE_INIT Enumerator of type DE_STATE (Integrator restart)   
DE_INVPARAM Enumerator of type DE_STATE (invalid input parameters)   
Density_HP Atmospheric density based on Harris–Priester model   
DE_NUMSTEPS Enumerator of type DE_STATE (Permitted number of steps exceeded)   
DE_STATE Enumeration type for status codes of class DE inegrator   
DE_STIFF Enumerator of type DE_STATE (Suspect of stiff problem)   
Diag Diagonal matrix from vector of diagonal elements   
Diag Method of Matrix class returning the vector of diagonal elements   
Dot Dot product of two vectors   
Dyadic Dyadic vector product   
EccAnom Eccentric anomaly for elliptic orbits   
EclMatrix Transformation matrix from equator to ecliptic   
EKF Extended Kalman filter class   
Elements Orbital elements from position and velocity   
Elements Orbital elements from two positions   
EqnEquinox Equation of the equinoxes [rad]   
f_Earth Flattening of the Earth   
FindEta Sector–triangle ratio   
GAST Greenwich Apparent Sidereal Time   
Geodetic Class for handling geodetic coordinates   
GHAMatrix Earth rotation matrix   
GM_Earth Product of gravitational constant $\times$ mass of Earth $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GM_Moon Product of gravitational constant $\times$ lunar mass $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GM_Sun Product of gravitational constant $\times$ solar mass $[ \mathrm { m } ^ { 3 } / \mathrm { s } ^ { 2 } ]$   
GMST Greenwich Mean Sidereal Time   
GPS_TAI Method of IERS returning GPS–TAI time difference [s]   
GPS_UTC Method of IERS returning GPS–UTC time difference [s]   
Grav Earth gravity model   
GravModel Data structure for gravity model parameters   
Id Identity matrix   
IERS Class for handling of Earth rotation parameters   
Illumination Fractional illumination of a spacecraft near the Earth   
Init Method of DE class for initialization of a new initial value problem   
Init Method of class EKF for initialization of a Kalman filter   
Init Method of class LSQ for initialization of a least-squares problem (with or without a priori information)   
Integ Method of class DE for performing an integration step   
Intrp Method of class DE for interpolation of solution   
Inv Inversion of general square matrix   
InvUpper Inversion of upper triangular matrix   
LSQ Least-squares estimation class   
LTCMatrix   
LTC_Matrix   
Matrix   
MeanObliquity   
MeasUpdate   
Mjd   
MJD_J2000   
Moon   
Norm   
NutMatrix   
omega_Earth   
PermitTOUT   
pi   
pi2   
PoleMatrix   
Position   
PrecMatrix   
P_Sol   
R_Earth   
R_Moon   
R_Sun   
R_x   
R_y   
R_z   
Rad   
relerr   
RK4   
RK4funct   
Row   
Set   
SetCol   
SetRow   
size   
size1   
Transformation from Greenwich coordinates to local tangential   
coordinates   
Method of class geodetic returning the transformation to local   
tangential coordinates   
Matrix class   
Mean obliquity of the ecliptic   
Method of class EKF performing the measurement update of   
Kalman filter parameters   
Modified Julian Date   
Modified Julian Date at epoch J2000   
Low-precision lunar coordinates   
Euclidean norm of a vector   
Nutation matrix   
Earth rotation rate [rad/s]   
Public element of DE class controlling integration past the spec  
ified output point   
$\pi$   
$2 \pi$   
Polar motion matrix   
Method of class Geodetic computing Cartesian from geodetic   
coordinates   
Precession matrix   
Solar radiation pressure at 1 AU $[ \mathrm { N } / \mathrm { m } ^ { 2 } ]$ 1   
Earth radius [m]   
Lunar radius [m]   
Solar radius [m]   
Matrix describing elementary $x$ -axis rotation   
Matrix describing elementary $y$ -axis rotation   
Matrix describing elementary $z$ -axis rotation   
$\pi / 1 8 0 ^ { \circ }$   
Public element of DE class specifying the relative accuracy re  
quirement   
Class for 4th-order Runge–Kutta integration   
Function prototype for differential equations   
Row vector of a matrix   
Method of class IERS for initialization of Earth orientation pa  
rameters   
Method of Matrix class for assignment of a column vector   
Method of Matrix class for assignment of a row vector   
Method of Vector class returning the number of vector ele  
ments   
Method of Matrix class returning the first dimension (number   
of rows)   
size2 Method of Matrix class returning the second dimension (number of columns)   
slice Method of Vector class for extraction of a sub-vector   
slice Method of Matrix class for extraction of a sub-matrix   
Solve Method of class LSQ for solution of a least-squares problem by backsubstitution   
Sqrt Method of Vector class returning the square-roots of all vector elements   
SRIM Method of class LSQ returning the square-root information matrix   
State Method of class EKF returning the current state vector   
State Position and velocity from Keplerian elements   
State Public element of DE class specifying the current integrator status   
StatePartials Partial derivatives of state vector w.r.t. Keplerian elements   
StdDev Method of class EKF returning the current standard deviation   
StdDev Method of class LSQ for computing the standard deviation of the solution   
Step Method of RK4 class performing a single integration step   
Sun Low-precision solar coordinates   
Time Method of class EKF returning the current time   
TimeUpdate Method of class EKF performing the time update of Kalman filter parameters   
T_J2000 Epoch J2000 (in Julian centuries since J2000)   
Transp Matrix transposition   
TT_TAI Method of IERS class returning TT–TAI time difference [s]   
TT_UTC Method of IERS class returning TT–UTC time difference [s]   
TwoBody State vector propagation and transition matrix for Keplerian orbits   
UTC_TAI Method of IERS returning UTC–TAI time difference [s]   
UT1_UTC Method of IERS returning UT1–UTC time difference [s]   
VecPolar Three-dimensional vector from polar coordinates   
Vector Vector class   
x_pole Matrix of class IERS returning the $x$ -coordinate of the Earth’s pole [rad]   
y_pole Matrix of class IERS returning the $y$ -coordinate of the Earth’s pole [rad]   
A Runge–Lenz vector   
A Cross-section (surface area)   
A Avogadro number   
A Moment of inertia with respect to the $x { - } / y$ -axes   
$A$ Azimuth   
$C$ Moment of inertia with respect to the $z$ -axis   
CD Drag coefficient   
CR Radiation pressure coefficient   
Cnm Potential coefficient   
$\pmb { D }$ Torque vector   
$\pmb { D }$ Diagonal matrix   
D Solar torque vector Mean solar torque vector   
$D$ Mean elongation of the Moon from the Sun   
$E$ Earth-fixed to local-tangent transformation matrix   
E Expectation value   
$E$ Eccentric anomaly   
$E$ Elevation   
$E$ Energy   
ET Ephemeris Time   
$F$ Force vector   
$F$ Mean distance of the Moon from the ascending node of its orbit   
F10.7 Index measuring solar UV radiation at $1 0 . 7 \mathrm { c m }$   
$\textbf { \textit { G } }$ Jacobian matrix (partial derivatives of measurement vector with respect to the state vector)   
$G$ Gravitational constant   
GMST Greenwich Mean Sidereal Time   
$\pmb { H }$ Jacobian matrix (partial derivatives of measurement vector with respect to the epoch state)   
$H _ { 0 }$ Atmospheric density scale height   
$H$ Sun-satellite hour angle   
$H$ Macro step size   
$I$ Moment of inertia   
$J$ Loss function   
$J _ { n }$ Zonal potential coefficient of degree n   
$\mathrm { J D }$ Julian Date   
$\pmb { K }$ Kalman gain   
$K$ Knudsen number   
$K _ { p }$ Three-hourly planetary geomagnetic index   
L0 Mean longitude of the Moon   
$M$ Mean anomaly   
$M$ Mass   
$M _ { 0 }$ Mean anomaly at reference epoch   
MJD Modified Julian Date   
$N$ Nutation matrix   
$N$ Particles per unit volume   
$N$ Auxiliary quantity for transformation of geodetic coordinate   
$N$ Accumulated Doppler counts   
$N$ Integer cycle ambiguity   
$P$ Gaussian vector (in direction of perigee)   
$P$ Precession matrix   
$P$ Covariance matrix   
$P$ Period   
$P _ { n }$ Legendre polynomial of degree n   
Pnm Associated Legendre polynomial of degree $n$ and order $m$   
$P _ { \odot }$ Solar radiation pressure at 1 AU   
$\varrho$ Gaussian vector (perpendicular to perigee)   
$\varrho$ Orthonormal matrix   
$\varrho$ Process-noise covariance matrix   
$\pmb { R }$ Upper triangular matrix   
$\pmb { R }$ Station position vector   
$R _ { x } , R _ { y }$ , $\pmb { R } _ { z }$ Matrices describing rotations around the $x$ , y, z-axes   
$\mathcal { R }$ Universal gas constant   
$R$ Radius of a celestial body   
$R$ Upper triangular matrix   
$R _ { \oplus }$ Equatorial radius of the Earth   
$s$ Sensitivity matrix   
$s$ Square root of the weighting matrix   
$s _ { A }$ Square root of the information matrix   
S Area of sector bounded by two position vectors   
$S _ { n m }$ Potential coefficient   
$T$ Time in Julian centuries since J2000   
$T$ Absolute temperature   
T1,2 Satellite transponder turn-around ratio   
Teqx Epoch of reference equinox in Julian centuries since J2000   
$T _ { n }$ Chebyshev polynomial of order $n$   
$T _ { \infty }$ Exospheric temperature   
TAI International Atomic Time   
TCB Barycentric Coordinate Time   
TCG Geocentric Coordinate Time   
TDB Barycentric Dynamic Time   
TDT Terrestrial Dynamic Time   
TT Terrestrial Time   
$U$ Transformation matrix (inertial to Earth-fixed)   
$U$ Orthonormal matrix   
$U _ { i }$ Elementary Householder transformation matrix   
$U _ { i k }$ Elementary Givens rotation matrix   
$U$ Potential   
$U _ { 2 }$ Potential due to tides   
$U _ { T }$ Potential of tide-induced gravity   
UT Universal Time   
UTC Coordinated Universal Time   
$V$ Orthonormal matrix   
$V _ { n m }$ Potential function   
W Gaussian vector perpendicular to the orbital plane   
W Weighting matrix   
$W _ { n m }$ Potential function   
$X _ { \mathrm { E W } } , Y _ { \mathrm { E W } }$ X/Y-angles using antenna with East/West mount   
$X _ { \mathrm { N S } } , Y _ { \mathrm { N S } }$ X/Y-angles using antenna with North/South mount   
$Z$ Height   
$Z _ { x }$ Height of inflection point   
a Acceleration vector   
$a$ Semi-major axis   
$a$ Ambiguity   
$a$ Albedo of the Earth   
$a _ { i }$ Coefficient of Chebyshev expansion   
aij Runge–Kutta(–Nystrøm) coefficients   
$a _ { p }$ Three-hourly planetary amplitude index   
$a _ { i } ^ { \prime }$ Chebyshev coefficient for derivative of a function   
$^ b$ Ecliptic latitude   
$b _ { i }$ Runge–Kutta(–Nystrøm) coefficients   
$c$ Aerial velocity or specific angular momentum vector   
$c$ Velocity of light ( $c = 2 9 9 7 9 2 4 5 8 { \mathrm { m } } / { \mathrm { s } }$ )   
$c$ Element of Givens rotation matrix   
$c _ { i }$ Runge–Kutta coefficients   
$d _ { i }$ Singular value   
$e$ Unit vector   
$e$ Orbital eccentricity   
$e$ Local truncation error   
$e$ Eccentricity of reference ellipsoid   
$f$ Vector function