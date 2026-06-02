and $B w _ { i } = 0$ ， $i = p + 1 , \ldots , n$ .These $n - p$ vectors form a basis for the nullspace of $B$ Furthermore, we have the orthogonality relations

$$
( A w _ { i } ) ^ { T } A w _ { j } = 0 , \quad i \ne j .
$$

When $B \in \mathbb { R } ^ { n \times n }$ is square and nonsingular the GSVD of $A$ and $B$ reduces to the SVD of $A B ^ { - 1 }$ , also called the quotient SVD (QSVD). Similarly the SVD of $A B$ is the product SVD. If $B$ were ill-conditioned, then forming $A B ^ { - 1 }$ (or $A B$ ） would give unnecessarily large errors in the SVD, so this approach should be avoided.Note also that when $B$ is not square or is singular, the SVD of $A B ^ { \dagger }$ does not always correspond to the GSVD.

An algorithm for computing the QSVD of $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { p \times n }$ was proposed by Paige [854,1986]. In the first phase, $A$ and $B$ are reduced to generalized triangular form by an RRQR factorization of $A$ with column pivoting $P$ .Next,a QR factorization is performed on $B P$ in which column pivoting is used on the last $p - r$ rows and $n - r$ columns of $B$ to reveal the rank $q$ of this block. In the second phase, two $n \times n$ upper triangular matrices are computed by a Kogbetliantz-type algorithm; see Section 7.2.2. Such algorithms can be extended to compute the GSVD for products and quotients of several matrices.

The generalized linear model where both $A$ and $V$ are allowed to be rank-deficient can be analysed by the GSVD; see Paige [860,1985l. We use the model (3.1.36) and assume that $V = B B ^ { T }$ is given in factored form, where $\boldsymbol { B } \in \mathbb { R } ^ { m \times p }$ ， $p \leq m$ . Since $A$ and $B$ have the same number of rows, the GSVD is applied to $A ^ { T }$ and $B ^ { T }$

Let $r = { \mathrm { r a n k } } ( A )$ ， $s = { \mathrm { r a n k } } ( B )$ ， $k = \mathrm { r a n k } ( ( A \quad B ) )$ , where $ r \leq n , s \leq p , k \leq r + s$ .Then there exist orthogonal matrices $U \in \mathbb { R } ^ { n \times n }$ ， $V \in \mathbb { R } ^ { p \times p }$ and a matrix $\boldsymbol { Z } \in \mathbb { R } ^ { m \times k }$ of rank $k$ such that

$$
A U = Z \left( \underbrace { 0 } _ { \begin{array} { l r } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { D _ { A } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { { I _ { k - s } } } } \end{array} } \right) \} q \qquad , \qquad B V = Z \left( \underbrace { I _ { k - r } } _ { \begin{array} { l r } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { D _ { B } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \underset { { p - s } } { 0 } } } \end{array} } \right) \underbrace  \} k - r \qquad ,
$$

where $q = r + s - k , D _ { A } ^ { 2 } + D _ { B } ^ { 2 } = I _ { q }$ and

$$
\begin{array} { r l } & { D _ { A } = \mathrm { d i a g } ( \alpha _ { 1 } , \ldots , \alpha _ { q } ) > 0 , \qquad 0 < \alpha _ { 1 } \leq \cdot \cdot \cdot \leq \alpha _ { q } < 1 , } \\ & { D _ { B } = \mathrm { d i a g } ( \beta _ { 1 } , \ldots , \beta _ { q } ) > 0 , \qquad 1 > \beta _ { 1 } \geq \cdot \cdot \cdot \geq \beta _ { q } > 0 . } \end{array}
$$

Note that the row partitionings in (3.1.54) are the same. Let the orthogonal matrices $U =$ $\left( U _ { 1 } \quad U _ { 2 } \quad U _ { 3 } \right)$ and $V = \left( \begin{array} { l l l } { V _ { 1 } } & { V _ { 2 } } & { V _ { 3 } } \end{array} \right)$ be partitioned conformally with the column blocks on the right-hand sides in (3.1.54). Then $A U _ { 1 } = 0$ ， $B V _ { 3 } = 0$ ,i.e., $U _ { 1 }$ and $V _ { 3 }$ span the nullspace of $A$ and $B$ ,respectively. The decomposition (3.1.54) separates out the common column space of $A$ and $B$ . Since $A U _ { 2 } = Z D _ { A }$ and $B V _ { 2 } = Z D _ { B }$ , we have $A U _ { 2 } D _ { B } = B V _ { 2 } D _ { A }$ ,and it follows that

$$
\mathcal { R } ( A U _ { 2 } ) = \mathcal { R } ( B V _ { 2 } ) = \mathcal { R } ( A ) \cap \mathcal { R } ( B )
$$

and has dimension $q$ .For the special case $B = I$ we have $s = k = m$ and then $q = { \mathrm { r a n k } } ( A )$ Now let the QR factorization of $Z$ in (3.1.54) be

$$
\begin{array} { r } { Q ^ { T } Z = \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) , \qquad Q = ( Q _ { 1 } , Q _ { 2 } ) , } \end{array}
$$

where $R \in \mathbb { R } ^ { k \times k }$ is upper triangular and nonsingular.In the model (3.1.36)we make the orthogonal transformations

$$
\tilde { x } = U ^ { T } x , \qquad \tilde { u } = V ^ { T } u .
$$

Then,from (3.1.54) and (3.1.56) the model (3.1.36) becomes

$$
\binom { R } { 0 } \left\{ \left( \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { D _ { A } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { I _ { k - s } } } \end{array} \right) \left( \begin{array} { c } { { \tilde { x } _ { 1 } } } \\ { { \tilde { x } _ { 2 } } } \\ { { \tilde { x } _ { 3 } } } \end{array} \right) + \left( \begin{array} { c c c } { { I _ { k - r } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { D _ { B } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { \tilde { u } _ { 1 } } } \\ { { \tilde { u } _ { 2 } } } \\ { { \tilde { u } _ { 3 } } } \end{array} \right) \right\} = \left( Q _ { 2 } ^ { T } b \right) ,
$$

where $\tilde { x } _ { i } = U _ { i } ^ { T } x _ { i }$ and $\tilde { u } _ { i } = V _ { i } ^ { T } u _ { i }$ ， $i = { 1 , 2 , 3 }$

It immediately follows that the model is correct only if $Q _ { 2 } ^ { T } b = 0$ ,which is equivalent to the condition $b \in \mathcal { R } ( A , B )$ . If this condition is not satisfied, then $b$ could not have come from the model. The remaining part of (3.1.58) can now be writen

$$
\left( \begin{array} { c c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } & { { R _ { 1 3 } } } \\ { { 0 } } & { { R _ { 2 2 } } } & { { R _ { 2 3 } } } \\ { { 0 } } & { { 0 } } & { { R _ { 3 3 } } } \end{array} \right) \left( \begin{array} { c } { { \tilde { u } _ { 1 } } } \\ { { D _ { A } \tilde { x } _ { 2 } + D _ { B } \tilde { u } _ { 2 } } } \\ { { \tilde { x } _ { 3 } } } \end{array} \right) = \left( \begin{array} { c } { { c _ { 1 } } } \\ { { c _ { 2 } } } \\ { { c _ { 3 } } } \end{array} \right) \} q _ { k - s } ^ { k - r } ,
$$

where we have partitioned $R$ and $c = Q _ { 1 } ^ { T } b$ conformally with the block rows of the two-block diagonal matrices in (3.1.58).

We first note that $\tilde { x } _ { 1 }$ has no effect on $b$ and therefore cannot be estimated. The decomposition $x = x _ { n } + x _ { e }$ with

$$
x _ { n } = U _ { 1 } \tilde { x } _ { 1 } , \qquad x _ { e } = U _ { 2 } \tilde { x } _ { 2 } + U _ { 3 } \tilde { x } _ { 3 }
$$

splits $x$ into a nonestimable part $x _ { n }$ and an estimable part $x _ { e }$ . Furthermore, ${ \tilde { x } } _ { 3 }$ can be determined exactly from $R _ { 3 3 } \tilde { x } _ { 3 } = c _ { 3 }$ . Note that ${ \tilde { x } } _ { 3 }$ has dimension $k - s = \mathrm { r a n k } ( ( A \quad B ) ) - \mathrm { r a n k } ( B )$ s0 that this can only occur when $\operatorname { r a n k } ( B ) < m$

The second block row in (3.1.59) gives the linear model

$$
D _ { A } \tilde { x } _ { 2 } + D _ { B } \tilde { u } _ { 2 } = R _ { 2 2 } ^ { - 1 } ( c _ { 2 } - R _ { 2 3 } \tilde { x } _ { 3 } ) ,
$$

where from (3.1.57) we have $V \tilde { u } _ { 2 } = \sigma ^ { 2 } I $ Here the right-hand side is known,and the best linear unbiased estimate of $\tilde { x } _ { 2 }$ is

$$
\hat { x } _ { 2 } = D _ { A } ^ { - 1 } R _ { 2 2 } ^ { - 1 } ( c _ { 2 } - R _ { 2 3 } \tilde { x } _ { 3 } ) .
$$

Since the error satisfies $D _ { A } ( \hat { x } _ { 2 } - \tilde { x } _ { 2 } ) = D _ { B } \tilde { u } _ { 2 }$ ,the error covariance is

$$
V ( \hat { x } _ { 2 } - \tilde { x } _ { 2 } ) = \sigma ^ { 2 } ( D _ { A } ^ { - 1 } D _ { B } ) ,
$$

and the components are uncorrelated. The random vector ${ \tilde { u } } _ { 3 }$ has no effect on $b$ ，The dimension of ${ \tilde { u } } _ { 3 }$ is $p - s = p - \mathrm { r a n k } ( B )$ ,and so is zero if $B$ has independent columns.Finally, the vector $\tilde { u } _ { 1 }$ can be obtained exactly from (3.1.59). Since $\tilde { u } _ { 1 }$ has zero mean and covariance matrix $\sigma ^ { 2 } I$ ,it can be used to estimate $\sigma ^ { 2 }$ . Note that $\tilde { u } _ { 1 }$ has dimension $k - r = \operatorname { r a n k } \left( A \quad B \right) - \operatorname { r a n k } ( A )$

A QR-like algorithm for computing the SVD of a product or quotient of two or more matrices is given by Golub, Splna,and Van Dooren [508,2ooo]. Let

$$
C = A _ { p } ^ { s _ { p } } \cdot \cdot \cdot A _ { 2 } ^ { s _ { 2 } } A _ { 1 } ^ { s _ { 1 } } , \quad s _ { i } = \pm 1 ,
$$

be a sequence of products or quotients of matrices $A _ { i }$ of compatible dimensions. To illustrate the idea, we consider for simplicity the case when $p = 2$ and $s _ { i } = 1$ . Then orthogonal matrices $Q _ { i }$ ， $i = 0 , 1 , 2$ ,can be constructed such that

$$
B = Q _ { 2 } ^ { T } A _ { 2 } Q _ { 1 } Q _ { 1 } ^ { T } A _ { 1 } Q _ { 0 }
$$

is bidiagonal. The SVD of $B$ can then be found by standard methods.Typically, the bidiagonal matrix will be graded and will allow small singular values to be computed with high relative precision by the QR algorithm. The generalization to the product and/or quotient of an arbitrary number of matrices is obvious.

# Notes and references

The first algorithms for computing the GSVD were developed by Stewart [1020,1982],[1021, $\mathrm { 1 9 8 3 } ]$ and Van Loan [1O80,1985]. Their algorithms use a QR factorization for the first phase. Heath et al. [597,1986] give a generalized Kogbetliantz algorithm for computing the SVD of the product $B ^ { T } A$ ,which computes very small singular values of the product $B ^ { T } A$ accurately. A more general theory for GSVD is developed by De Moor and Zha [299,1991].

Rao [912, 1973l called the augmented matrix in (3.1.11) the fundamental matrix. When both $A$ and $V$ are rank-deficient the solution of (3.1.11) can, in theory,be obtained from a generalized inverse of the fundamental matrix. Some results and proofs for the singular linear model are given by Searle [992,1994l. A unified treatment including a perturbation analysis of generalized and constrained least squares problems is given by Wedin [1110,1985]. The systematic use of GQR as a basic conceptual and computational tool is explored by Paige [861, 1990].Implementation aspects of GQR are considered in Anderson,Bai,and Dongarra [25, 1992],and routines for GQR are included in LAPACK. QR, URV,and SVD decompositions are generalized to any number of matrices by De Moor and Van Dooren [298,1992]. Rank-revealing GQR decompositions are developed by Luk and Qiao [763,1994].

# 3.2 - Weighted Least Squares

# 3.2.1 - Weighted Least Squares Problems

In many problems,the random errors in the data are uncorrelated but of variable accuracy. In geodetic surveys,recent observations may be much more accurate than older data. Such problems have diagonal covariance matrix $V$ and are called weighted least squares (WLS) problems,

$$
\operatorname* { m i n } _ { x } \| W ( A x - b ) \| _ { 2 } ^ { 2 } , \quad W = V ^ { - 1 / 2 } = \operatorname { d i a g } \big ( w _ { 1 } , w _ { 2 } , \ldots , w _ { m } \big ) ,
$$

where weights $w _ { i }$ are such that the weighted residuals $r _ { i } = w _ { i } ( b - A x ) _ { i }$ have equal variance. Note that the solution of (3.2.1) is scaling independent,i.e., it does not change if $W$ is multiplied by a nonzero scalar. Therefore,without restriction we can assume in the following that $w _ { i } \geq 1$ ， and that the rows of $A$ are normalized so that $\operatorname* { m a x } _ { 1 \leq j \leq n } | a _ { i j } | = 1$ ， $i = 1 , \ldots , m$

The solution to the WLS problem (3.2.1) satisfies the normal equations

$$
A ^ { T } W ^ { 2 } A x = A ^ { T } W ^ { 2 } b .
$$

A more stable solution method is to use the weighted QR factorization $W A = Q R$ . The solution to (3.2.1) is then obtained from

$$
R x = Q ^ { T } W b ,
$$

and squaring of the weight matrix $W$ is avoided.

For a consistent underdetermined system $A ^ { T } y ~ = ~ c$ ，the unique solution of the weighted least-norm problem

$$
\operatorname* { m i n } _ { y } \| W y \| _ { 2 } \ { \mathrm { s u b j e c t } } { \mathrm { t o } } \ A ^ { T } y = c
$$

is obtained from the generalized normal equations of the second kind,

$$
( A ^ { T } W ^ { 2 } A ) z = c , \quad y = W ^ { 2 } A z .
$$

The weighted QR factorization $W A = Q R$ gives the more accurate solution

$$
y = W Q R ^ { - T } c .
$$

In a linear model where some error components have much smaller variance than others, the weight matrix $W = \mathrm { d i a g } \left( w _ { i } \right)$ is ill-conditioned.Then $\kappa ( W A )$ can be large even when $A$ is well-conditioned. We call a weighted least squares problem stiff if

$$
\mu = { \frac { \operatorname* { m a x } _ { 1 \leq i \leq m } w _ { i } } { \operatorname* { m i n } _ { 1 \leq i \leq m } w _ { i } } } \gg 1 ,
$$

by analogy to the terminology used in differential equations. Stif problems arise,e.g.,in barrier and interior methods for optimization, electrical networks,and certain classes of finite element problems.In interior methods, $W$ becomes very ill-conditioned when the iterate approaches the boundary; see Wright [1132,1995]. Stiff problems occur also when the method of weighting is used to solve least squares problems with the linear equality constraints $A _ { 1 } x = b _ { 1 }$ . Often the interest is in a sequence of weighted problems where $W$ varies and $A$ is constant.

That a weighted least squares problem is stif does not in general imply that the problem of computing $x$ from the data $W , A$ and $b$ is ill-conditioned.For weighted least squares problems the componentwise Bauer-Skeel condition number (see Section 1.3.4)

$$
\operatorname { c o n d } ( A W ) = \| \mathbf { \Psi } | ( A W ) ^ { \dagger } | \mathbf { \Psi } | A W | \|
$$

is more relevant. This often depends only weakly on $W$ and when $\mu \to \infty$ can tend to a limit value; see Section 3.2.3.

To illustrate the possible failure of the method of normal equations for the weighted least squares problem (3.2.2)，we consider a problem where only the first $\textit { p } < \textit { n }$ equations are weighted by $w _ { i } = w \gg 1$ ， $i = 1 , \ldots , p$

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { c } { w A _ { 1 } } \\ { A _ { 2 } } \end{array} } \right) x - \left( { \begin{array} { c } { w b _ { 1 } } \\ { b _ { 2 } } \end{array} } \right) \right\| _ { 2 } ^ { 2 } , \quad A _ { 1 } \in \mathbb { R } ^ { p \times n } .
$$

The weighted normal equations are $C x = d$ ,where

$$
C = w ^ { 2 } A _ { 1 } ^ { T } A _ { 1 } + A _ { 2 } ^ { T } A _ { 2 } , \qquad d = w ^ { 2 } A _ { 1 } ^ { T } b _ { 1 } + A _ { 2 } ^ { T } b _ { 2 } .
$$

When $w \gg 1$ ， $C$ and $d$ will be dominated by the first term. If $w > \mathbf { u } ^ { - 1 / 2 }$ , then all information contained in $A _ { 2 }$ and $b _ { 2 }$ will be lost. But since $p < n$ ,the solution depends critically on this data. (The matrix in the Läuchli least squares problem in Example 2.1.1 is of this type.） Hence, the method of normal equations is generally not well behaved.

The Peters-Wilkinson method (see Section 2.4.1) can be used to solve weighted least squares problems even when $W$ is severely ill-conditioned. Assume that the rows of $A$ and $b$ are preordered by decreasing weights, $\infty > w _ { 1 } \ge \cdot \cdot \cdot \ge w _ { m } > 0$ .Compute an LDU factorization with complete pivoting of $A$ ，

$$
\Pi _ { 1 } A \Pi _ { 2 } = L D U ,
$$

where $\boldsymbol { L } \in \mathbb { R } ^ { m \times n }$ is unit lower trapezoidal, $| l _ { i j } | \le 1$ ,and $U \in \mathbb { R } ^ { n \times n }$ is upper unit triangular. In the transformed problem

$$
\operatorname* { m i n } _ { y } \| L y - \tilde { b } \| _ { 2 } , \quad \tilde { b } = \Pi _ { 1 } b , \quad D U \Pi _ { 2 } ^ { T } x = y ,
$$

$L$ and $U$ are usually well-conditioned, and the weight matrix $W$ is reflected only in $D$ The transformed problem can often be solved safely by the method of normal equations $\dot { L } ^ { T } L y = L ^ { T } \tilde { b }$ and back-substitution $D U x = D y$

Example 3.2.1. Consider the least squares problem $\begin{array} { r } { \operatorname* { m i n } _ { x } \| W A x - W b \| _ { 2 } . } \end{array}$

$$
W A = \left( \begin{array} { c c c } { { w } } & { { w } } & { { w } } \\ { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) , \qquad W b = \left( \begin{array} { c } { { w } } \\ { { 0 } } \\ { { 0 } } \\ { { 0 } } \end{array} \right)
$$

of Läuchli. For $w > \mathbf { u } ^ { - 1 / 2 }$ the normal equations become singular. The Peters-Wilkinson method computes the factorization $W A = L D U$ ，

$$
L = \left( \begin{array} { c c c } { { 1 } } & { { } } & { { } } \\ { { w ^ { - 1 } } } & { { 1 } } & { { } } \\ { { } } & { { - 1 } } & { { 1 } } \\ { { } } & { { } } & { { - 1 } } \end{array} \right) , \qquad U = \left( \begin{array} { c c c } { { 1 } } & { { 1 } } & { { 1 } } \\ { { } } & { { - 1 } } & { { - 1 } } \\ { { } } & { { } } & { { - 1 } } \end{array} \right) ,
$$

where $\boldsymbol { D } = \mathrm { d i a g } \left( \boldsymbol { w } , 1 , 1 \right)$ and $L$ and $U$ are well-conditioned. With $y \ = \ D U x$ the problem becomes $\begin{array} { r } { \operatorname* { m i n } _ { y } \| L y - W b \| _ { 2 } } \end{array}$ .The solution can be accurately computed from

$$
L ^ { T } L y = L ^ { T } W b , \qquad D U x = y .
$$

The weight $w$ only appears in the diagonal scaling of $y$ in the last step.Alternatively, $L$ can be transformed into lower triangular form by Householder reflections; see A. K. Cline [253,1973l.

# 3.2.2 - Weighted QR Factorization

Householder QR factorization can give unnecessarily poor accuracy for weighted least squares problems because of the large growth of intermediate elements during the factorization, even when column pivoting is used. This was first observed by Powell and Reid [9O3,196g], who considered the least squares problem for

$$
A = \left( \begin{array} { c c c } { { 0 } } & { { 2 } } & { { 1 } } \\ { { w } } & { { w } } & { { 0 } } \\ { { w } } & { { 0 } } & { { w } } \\ { { 0 } } & { { 1 } } & { { 1 } } \end{array} \right) , \qquad b = \left( \begin{array} { c } { { 3 } } \\ { { 2 w } } \\ { { 2 w } } \\ { { 2 } } \end{array} \right) , \quad w \gg 1 ,
$$

with exact solution $x = ( 1 , 1 , 1 ) ^ { T }$ . The first step of Householder QR factorization produces the reduced matrix

$$
\begin{array} { r } { \left( \begin{array} { c c c c } { - w \sqrt { 2 } } & { - w / \sqrt { 2 } } & { - w / \sqrt { 2 } } \\ { 0 } & { w / 2 - \sqrt { 2 } } & { - w / 2 - 1 / \sqrt { 2 } } \\ { 0 } & { - w / 2 - \sqrt { 2 } } & { w / 2 - 1 / \sqrt { 2 } } \\ { 0 } & { 1 } & { 1 } \end{array} \right) . } \end{array}
$$

If $w > 2 \sqrt { 2 } \mathbf { u } ^ { - 1 }$ , then in floating-point arithmetic,the terms $- { \sqrt { 2 } }$ and $- 1 / \sqrt { 2 }$ in the second and third rows of $\tilde { A } ^ { ( 2 ) }$ are lost. But this means that allinformation present in the first row of $A$ is lost. This is disastrous,because the number of rows in $A$ containing large elements is less than the number of components in $x$ .Hence there is a substantial dependence of the solution $x$ on both the first and fourth rows of $A$ . Still, this is better than the method of normal equations,which fails when $w > \mathbf { u } ^ { - 1 / 2 }$ for this problem. Van Loan [1081,1985] gives further examples where Householder QR without row interchanges gives poor accuracy for stiff least squares problems. Note that the insensitivity of fixed-precision IR to poor row scaling of $A$ can make it possible to relax the need to sort rows of large norm to the top.

For the first example above,failure can easily be avoided by interchanging the first two rows of $A$ before performing the QR factorization. More generally, rowwise stability can be achieved by using Householder QR with complete pivoting. By this we mean that in each step, first a pivot column of maximum norm is selected and then an element of largest absolute value is permuted into the pivot position. (Note the importance of interchanging columns before rows.) w $\hat { A } ^ { ( k ) } = ( a _ { i j } ^ { ( k ) } )$ $k$

$$
\omega _ { i } = \operatorname* { m a x } _ { j , k } | a _ { i j } ^ { ( k ) } | \leq ( 1 + \sqrt { 2 } ) ^ { n - 1 } \operatorname* { m a x } _ { j } | a _ { i j } | , \quad i = 1 , \ldots , m .
$$

This upper bound can nearly be attained, although in practice, usually $\omega _ { i } \approx 1$ . The following rowwise stability result is due to Powell and Reid,but a more accessible derivation is given by Cox and Higham [273,1998].

Theorem 3.2.2. Let $\hat { R } \in \mathbb { R } ^ { m \times n }$ denote the computed upper triangular matrix in the Householder QR factorization of $A \in \mathbb { R } ^ { m \times n }$ with complete pivoting. Let $\Pi$ be the permutation matrix that describes the column permutations. Then there exists an exactly orthogonal matrix $Q \in \mathbb { R } ^ { m \times m }$ such that

$$
( A + \Delta A ) \Pi = Q \left( \begin{array} { l } { \hat { R } } \\ { 0 } \end{array} \right) , \quad \lvert \Delta a _ { i } ^ { T } \rvert \leq \tilde { \gamma } _ { m } ( 1 , \ldots , n ^ { 2 } ) \omega _ { i } , \quad i = 1 , \ldots , m ,
$$

where $\widetilde { \gamma } _ { m }$ is defined as in (1.4.9).

Householder QR factorization with complete pivoting is expensive and not available in standard software. Bjorck [135,1996,p.169] conjectured that if the rows of $A$ are presorted by decreasing row $\infty$ -norm, i.e., so that $d _ { 1 } \geq d _ { 2 } \geq \dots \geq d _ { m }$ ，where $d _ { i } = \operatorname* { m a x } _ { 1 \leq j \leq n } \left| w _ { i } a _ { i j } \right|$ ,then the rowwise backward error bound holds for Householder QR with standard column pivoting. This conjecture was later proved by Cox [272,1997]. Then standard software can be used for stably solving strongly weighted least squares problems.

In contrast to the Householder QR method, Gram-Schmidt QR factorization is numerically invariant under row interchanges,except for second-order effects derived from different summation orders in inner products. However, numerical results for highly stiff problems show a loss of accuracy also for MGS.

Example 3.2.3. The stability of algorithms using QR factorization for stiff problems can be enhanced by iterative refinement.As test problems we take

$$
\begin{array} { r } { A = V D \in \mathbb { R } ^ { 2 1 \times 6 } , \quad v _ { i j } = ( i - 1 ) ^ { j - 1 } , } \end{array}
$$

with $D$ chosen so that the columns of $A$ have unit 2-norm. The right-hand side is taken to be

$$
b = A x + \theta h , \qquad x = D ^ { - 1 } ( 1 0 ^ { 5 } , 1 0 ^ { 4 } , \dots , 1 ) ,
$$

where $A ^ { T } h ~ = ~ 0$ and $h$ is normalized so that $\kappa _ { 2 } ( A ) \| h \| _ { 2 } ~ = ~ 1 . 5 \| A \| _ { 2 } \| x \| _ { 2 }$ .Problems with widely diferent row norms are obtained by taking $A _ { w } = D _ { w } A$ ， $b _ { w } = D _ { w } b$ ， $h _ { w } \ = \ D _ { w } ^ { - 1 } h$ ， and $D _ { w } = \mathrm { d i a g } \left( w _ { i } \right)$ ，where $w _ { i } = w$ for $i = { 1 , 1 1 , 2 1 }$ and $w _ { i } = 1$ otherwise. The tests were run on a UNIVAC 1108 with single precision equal to $2 ^ { - 2 6 } = 1 0 ^ { - 7 . 8 3 }$ and double precision $2 ^ { - 6 2 } = 1 0 ^ { - 1 8 . 6 6 }$ . Mixed-precision iterative refinement was carried out with three different QR factorizations: Modified Gram-Schmidt (MGS), Householder QR (HQR),and Householder QR with the weighted rows permuted to the top (HQRP).Table 3.2.1 shows the initial and final average numbers of correct significant decimal digits in the solution for $w = 1 , 2 ^ { 7 } , 2 ^ { 1 4 }$ .The numbers in parentheses indicate refinements carried out.

Table 3.2.1.Average number of correct significant decimal digits in the solution before and after iterative refinement with various QR factorizations. The number of refinement steps is shown in parentheses.   

<table><tr><td>Algorithm</td><td>w=1</td><td>w=27</td><td>w= 214</td></tr><tr><td>MGS</td><td>5.92</td><td>5.15</td><td>2.90</td></tr><tr><td rowspan="2">HQR</td><td>14.15 (3)</td><td>18.66 (4)</td><td>18.66 (9)</td></tr><tr><td>5.75</td><td>3.79</td><td>-0.44</td></tr><tr><td rowspan="2">HQRP</td><td>15.74 (4)</td><td>12.86 (3)</td><td>18.66 (8)</td></tr><tr><td>4.94</td><td>4.22</td><td>3.16</td></tr><tr><td></td><td>14.68 (5)</td><td>18.66 (4)</td><td>11.31 (4)</td></tr></table>

Anda and Park [22,1996] apply their fast self-scaling plane rotations to the QR factorization of stiff least squares problems.Their results show that regardless of row sorting, these produce accurate results even for extremely stiff least squares problems. No significant difference in accuracy is observed between different rotation orderings. This makes self-scaling plane rotations a method of choice for solving stiff problems.

# 3.2.3 - Limit Behavior of Weighted Least Squares

Let $x _ { W }$ be the unique solution to the weighted least squares problem

$$
\operatorname* { m i n } _ { x } \| W ( A x - b ) \| _ { 2 } , \quad A \in \mathbb { R } ^ { m \times n } , \quad \operatorname { r a n k } ( A ) = n ,
$$

where $W = \mathrm { d i a g } \left( w _ { 1 } , \dots , w _ { m } \right)$ is positive definite. Stewart [1022,1984] showed that there is a finite number $\chi _ { A }$ not depending on $W$ such that the weighted least squares solution $x _ { W }$ satisfies

$$
\| x _ { W } \| \leq \chi _ { A } \| b \| .
$$

This implies a bound for the perturbation of the solution that results from a perturbation of $b$ However, due to the combinatorial aspect of the bound $\chi _ { A }$ , it cannot be computed in polynomial time.

Ben-Tal and Teboulle [1O3,199o] show,using a formula derived from Cramer's rule and the Binet-Cauchy formula,that $x _ { W }$ is a convex combination of the basic solutions to nonsingular square subsystems of the original overdetermined system.

Theorem 3.2.4. Let $\mathcal { F }$ be the set of all subsets $I = \{ i _ { 1 } , i _ { 2 } , \ldots , i _ { n } \}$ from $\{ 1 , 2 , \ldots , m \}$ .Denote by $A _ { I }$ and $b _ { I }$ the submatrix of $A$ and $b$ whose rows correspond to $I$ Furthermore,let

$$
\mathcal F ^ { + } = \{ I \in \mathcal F | \mathrm { r a n k } ( A _ { I } ) = n \} ,
$$

and let $x _ { I }$ be the solution of $A _ { I } x _ { I } = b _ { I }$ . Then

$$
x _ { W } = \sum _ { I \in \mathcal { F } ^ { + } } \lambda _ { I } x _ { I } , \quad \lambda _ { I } > 0 , \quad \sum _ { I \in \mathcal { F } ^ { + } } \lambda _ { I } = 1 .
$$

It follows that $x _ { W } \in \operatorname { c o n v } { \{ x _ { I } \mid I \in { \mathcal { F } } ^ { + } \} } .$

This result is generalized to diagonally dominant symmetric and positive semidefinite weight matrices by Forsgren [420,1996].He also shows that it does not hold for general symmetric definite weight matrices.

# Notes and references

Vavasis [1091,1994] surveys equilibrium problems with extremely large weights and gives stable direct and iterative algorithms for their solution． Hough and Vavasis [643,1997l develop a special method based on a complete orthogonal decomposition that satisfies a strong type of stability. Iterative methods for accurate solution of weighted least squares are studied by Bobrovnikova and Vavasis [156, 2001].

# 3.2.4 - Indefinite Linear Least Squares

For $A \in \mathbb { R } ^ { m \times n }$ with $m \geq n$ ,and $b \in \mathbb { R } ^ { m }$ , the indefinite least squares (ILS) problem is

$$
\operatorname* { m i n } _ { x } { ( b - A x ) ^ { T } J ( b - A x ) } , \quad A = { \binom { A _ { 1 } } { A _ { 2 } } } , \quad b = { \binom { b _ { 1 } } { b _ { 2 } } } ,
$$

where $A _ { 1 } \in \mathbb { R } ^ { m _ { 1 } \times n }$ ， $A _ { 2 } \in \mathbb { R } ^ { m _ { 2 } \times n }$ ， $m _ { 1 } + m _ { 2 } = m$ ,and

$$
J = \left( \begin{array} { c c } { { I _ { m _ { 1 } } } } & { { 0 } } \\ { { 0 } } & { { - I _ { m _ { 2 } } } } \end{array} \right)
$$

is the signature matrix. Note that $J ^ { - 1 } = J$ . This problem arises in downdating,total least squares problems, and $H ^ { \infty }$ -smoothing; see Chandrasekaran, Gu, and Sayed [232,1998]. A necessary condition for $x$ to solve (3.2.13) is that the gradient be zero:

$$
A ^ { T } J ( b - A x ) = 0 .
$$

Hence the residual vector $r = b { - } A x$ is $J$ -orthogonal to $\mathcal { R } ( A )$ . Equivalently, $x$ solves the normal equations $A ^ { T } J A x = A ^ { T } J b$ . The indefinite least squares problem has a unique solution if and only if $A ^ { T } J A$ is positive definite. This implies that $m _ { 1 } \geq n$ and that $A _ { 1 }$ (and $A$ )has full column rank; see Bojanczyk, Higham,and Patel [166,2oo3]. In the following we assume that $A ^ { T } J A$ is positive definite.

In the method of normal equations for problem ILS the Cholesky factorization of $A ^ { T } J A =$ $R ^ { T } R$ is computed,and the solution is obtained by solving two triangular systems $R ^ { T } ( R x ) = c$ ， where $c = A ^ { T } J b$

If accuracy is important,an algorithm based on QR factorization is to be preferred.A backward stable algorithm was given by Chandrasekaran, $\mathrm { G u }$ ,and Sayed [232,1998]. The first step is to compute the compact QR factorization

$$
\begin{array} { r } { A = \left( \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right) = \left( \begin{array} { l } { Q _ { 1 } } \\ { Q _ { 2 } } \end{array} \right) R = Q R , \quad Q _ { 1 } \in \mathbb R ^ { m _ { 1 } \times n } , \quad Q _ { 2 } \in \mathbb R ^ { m _ { 2 } \times n } , } \end{array}
$$

where $Q ^ { T } Q = Q _ { 1 } ^ { T } Q _ { 1 } + Q _ { 2 } ^ { T } Q _ { 2 } = I _ { n }$ . Substituting this into (3.2.15) gives the equation

$$
( Q _ { 1 } ^ { T } Q _ { 1 } - Q _ { 2 } ^ { T } Q _ { 2 } ) R x = Q ^ { T } J b .
$$

Note that the orthogonality of $Q$ is not needed for this to hold. By computing the Cholesky factorization

$$
Q _ { 1 } ^ { T } Q _ { 1 } - Q _ { 2 } ^ { T } Q _ { 2 } = L L ^ { T } ,
$$

where $\ b { L } \in \mathbb { R } ^ { n \times n }$ is lower triangular,this linear system becomes

$$
L L ^ { T } R x = Q ^ { T } J b .
$$

The total cost for this QR-Cholesky algorithm is about $( 5 m - n ) n ^ { 2 }$ flops. Although $Q _ { 1 } ^ { T } Q _ { 1 } -$ $Q _ { 2 } ^ { T } Q _ { 2 }$ can be very ill-conditioned, this method can be shown to be backward stable.

Bojanczyk, Higham,and Patel [166, 2oo3l give a perturbation analysis of the ILS problem and develop an alternative ILS algorithm based on so-called hyperbolic QR factorization. For the perturbation analysis the normal equations can be rewritten in symmetric augmented form as

$$
\left( \begin{array} { c c } { { J } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { s } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { 0 } } \end{array} \right) ,
$$

where $s = J r = J ( b - A x )$ . The inverse of the augmented matrix is (cf. (3.1.15))

$$
\left( \begin{array} { c c } { { J } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { { J ( I - P ) } } & { { J A S ^ { - 1 } } } \\ { { S ^ { - 1 } A ^ { T } J } } & { { - S ^ { - 1 } } } \end{array} \right) ,
$$

where $S = A ^ { T } J A$ and $P = A S ^ { - 1 } A ^ { T } J$ is a projector. Consider perturbations that satisfy the componentwise bounds $| \delta A | \le \omega E$ ,and $| \delta b | \le \omega f$ . Then using (3.2.18) and proceeding as in Section 1.3.4 we obtain the first-order bound

$$
\begin{array} { r } { | \delta \boldsymbol { x } | \le \omega \big ( | S ^ { - 1 } A ^ { T } | ( f + E | \boldsymbol { x } | ) + | S ^ { - 1 } | E ^ { T } | r | \big ) . } \end{array}
$$

A matrix $Q \in \mathbb { R } ^ { n \times n }$ is said to be $J$ -orthogonal if $Q ^ { T } J Q = J$ Multiplying this by $Q J$ and using $J ^ { 2 } = I$ gives $Q J Q ^ { T } J = I$ and $Q J Q ^ { T } = J$ If $Q _ { 1 }$ and $Q _ { 2 }$ are $J$ -orthogonal, then

$$
Q _ { 2 } ^ { T } Q _ { 1 } ^ { T } J Q _ { 1 } Q _ { 2 } = Q _ { 2 } ^ { T } J Q _ { 2 } = J ,
$$

i.e., a product of $J$ -orthogonal matrices is $J$ -orthogonal. $J$ -orthogonal matrices are useful in the treatment of problems with an underlying indefinite inner product and also play a role in the solution of certain structured eigenvalue problems.

From $r ^ { T } J r = r ^ { T } Q ^ { T } J Q r$ it follows that the ILS problem (3.2.13) is invariant under $J$ 1 orthogonal transformations. A hyperbolic QR factorization has the form

$$
Q ^ { T } A = Q ^ { T } \left( { A _ { 1 } \atop A _ { 2 } } \right) = { \binom { R } { 0 } }
$$

where $R$ is upper triangular and $Q$ is $J$ orthogonal. Then it holds that

$$
\begin{array} { r l } & { ( b - A x ) ^ { T } J ( b - A x ) = ( b - A x ) ^ { T } Q J Q ^ { T } ( b - A x ) } \\ & { \qquad = \left( \begin{array} { c } { c _ { 1 } - R x } \\ { c _ { 2 } } \end{array} \right) ^ { T } J \left( \begin{array} { c } { c _ { 1 } - R x } \\ { c _ { 2 } } \end{array} \right) = \| c _ { 1 } - R x \| _ { 2 } ^ { 2 } - \| c _ { 2 } \| _ { 2 } ^ { 2 } , } \end{array}
$$

nd the solution to the ILS problem (3.2.13) is obtained by solving $R x = c _ { 1 }$

The simplest $J$ -orthogonal matrices are hyperbolic rotations of the form

$$
H = H ^ { T } = \left( \begin{array} { c c } { { c } } & { { - s } } \\ { { - s } } & { { c } } \end{array} \right) , \quad c ^ { 2 } - s ^ { 2 } = 1 .
$$

They are so named because $| c | = \cosh \theta$ and $s = \sinh \theta$ for some $\theta$ . It is easily verified that

$$
H ^ { T } J H = J , \quad J = \mathrm { d i a g } ( 1 , - 1 ) .
$$

Like plane rotations,hyperbolic rotations can be used to zero a selected component in a vector,

$$
H \left( { x _ { 1 } \atop x _ { 2 } } \right) = \left( { \sigma \atop 0 } \right) ,
$$

which requires $c x _ { 2 } = s x _ { 1 }$ . Provided $| x _ { 1 } | > | x _ { 2 } |$ , the solution is

$$
s = x _ { 2 } / \sqrt { x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } } , \qquad c = x _ { 1 } / \sqrt { x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } } .
$$

The elements of a hyperbolic rotation $H$ are unbounded and therefore must be used with care. As shown by Chambers [217,1971] direct computation of $y = H x$ is not stable.Instead,a mixed form that combines a hyperbolic rotation with a plane rotation should be used. This is based on the equivalence

$$
H \left( { x _ { 1 } } \right) = \left( { y _ { 1 } } \right) \quad \Leftrightarrow \quad G \left( { y _ { 1 } } \right) = \left( { x _ { 1 } } \right) , \quad G = \left( { c \cdot - s } \right) .
$$

First, $y _ { 1 } = H x _ { 1 }$ is computed using the hyperbolic rotation, and then $y _ { 2 } = G x _ { 2 }$ is computed from a plane rotation, i.e.,

$$
y _ { 1 } = ( x _ { 1 } - s x _ { 2 } ) / c , \qquad y _ { 2 } = c x _ { 2 } - s y _ { 1 } .
$$

An error analysis of Chambers’ algorithm is give by Bojanczyk et al. [164,1987].

Bojanczyk, Higham,and Patel [166,2oo3l give an algorithm for solving the ILS problem that combines standard Householder reflectors and hyperbolic rotations.In the first step,two Householder reflectors are used: $P _ { 1 , 1 }$ zeros the elements in rows $2 , \ldots , m _ { 1 }$ of the first column of $A _ { 1 }$ ,and $P _ { 1 , 2 }$ zeros the elements in rows $m _ { 1 } + 1 , \ldots , m$ in $A _ { 2 }$ . The remaining element in the first column of $A _ { 2 }$ is annihilated by a hyperbolic rotation in the plane $( 1 , m _ { 1 } + 1 )$ . The steps in this reduction to triangular form are shown below for the case $n = m _ { 1 } = m _ { 2 } = 3$

$$
\begin{array}{c}  \begin{array} { c c l l } { [ \begin{array} { c c c } { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \end{array} ] } & { \Rightarrow \ : H _ { 1 , 5 } } \\ { [ \begin{array} { c c c } { \times } & { \times } & { \times } \\ & & { \times } & { \times } \\ & & { \times } & { \times } \end{array} ] } & { \Rightarrow \ : \ : P _ { 2 , 1 } } \\ { \otimes } & { \times } & { \times } \end{array} [ \begin{array} { c c c } { \times } & { \times } & { \times } \\ & { \times } & { \times } \\ & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ & { \times } & { \times } \\ & & { \times } & { \times } \end{array} ]  \\ { \otimes } & { \times } & { \times } \end{array} ] \ : \ : \Rightarrow \ : P _ { 2 , 1 } \ : \ : \Rightarrow \ : P _ { 2 , 2 } [ \begin{array} { c c c } { \times } & { \times } & { \times } \\ & { \times } & { \times } \\ & { \otimes } & { \times } \\ & { \otimes } & { \times } \\ & { \times } & { \times } \\ & { \otimes } & { \times } \end{array} ]
$$

$$
\Rightarrow \begin{array} { c c } { [ \begin{array} { c c } { { \bf x } } & { { \bf x } } & { { \bf x } } \\ { { \bf x } } & { { \bf x } } & { { \bf x } } \\ { { \bf x } } & { { \bf x } } \\ { { \bf \otimes } } & { { \bf x } } \\ { { \bf \otimes } } & { { \bf x } } \\ { { \bf x } } & { { \bf x } } \end{array} ] } &  \Rightarrow \begin{array} { c } { P _ { 3 , 1 } } \\ { P _ { 3 , 2 } } \\ { P _ { 3 , 2 } } \\ { P _ { 3 , 2 } } \end{array} ] \xrightarrow [ ] { \bf { \otimes } } \begin{array} { c } { [ \begin{array} { c c c } { { \bf x } } & { { \bf x } } & { { \bf x } } \\ { { \bf x } } & { { \bf x } } \\ & { { \bf x } } \\ & { { \bf \otimes } } \\ & { { \bf x } } \\ & { { \bf \otimes } } \\ & { { \bf \otimes } } \end{array} ] } \end{array} \Rightarrow \begin{array} { c } { [ \begin{array} { c c c } { { \bf x } } & { { \bf x } } & { { \bf \times } } \\ { { \bf x } } & { { \bf x } } \\ & { { \bf x } } \\ & { { \bf \otimes } } \\ & { { \bf \otimes } } \\ & & { { \bf \otimes } } \\ & & { { \bf \otimes } } \end{array} ] } \end{array} \end{array}
$$

The remaining steps are similar. In step $k$ ， $k = 1 , \dots , n$ ,two Householder reflections are used to zero the last $m _ { 1 } - k$ elements in the $k$ th column of $A _ { 1 }$ and the last $m _ { 2 } - 1$ elements in the $k$ th column of $A _ { 2 }$ .Next,a hyperbolic rotation in the plane $( k , m _ { 1 } + 1 )$ is then used to zero the remaining element in the $k$ th column of $A _ { 2 }$ . If the problem is positive definite, the process will not break down and terminates with an upper triangular matrix $R$ after $n$ steps.The reduction can be combined with column interchanges so that at step $k$ the diagonal element $r _ { k k }$ in $R$ is maximized. The interchanges in the remaining steps are determined from the reduced matrices in a similar way. Since the operation count for the required $n$ hyperbolic rotations used in the reduction is $O ( n ^ { 2 } )$ flops,the total cost is about the same as for the standard Householder QR factorization.The algorithm can be shown to be forward stable.

A special case arises in total least squares problems (see Section 4.4), where the factorization $A ^ { T } A - \overline { { w ^ { 2 } I _ { n } } } = R ^ { T } R$ is required without forming the cross-product. This can be achieved by taking $A _ { 1 } = A$ and $A _ { 2 } = w I _ { n }$ in the above reduction. Since the hyperbolic rotations will cause the rows in $A _ { 2 }$ to fill in, the reduction is almost as expensive as when $A _ { 2 }$ is a full upper triangular matrix. There are two different ways to perform the reduction: process $I _ { n }$ either top down, which will use more memory but allows the use of Householder reflectors,or bottom up,which avoids fill-in but uses more hyperbolic rotations.

Bojanczyk, Higham,and Patel [165,2oo3l give a similar algorithm for the equality constrained ILS problem

$$
\operatorname* { m i n } _ { x } ( b - A x ) ^ { T } J ( b - A x ) \quad { \mathrm { s u b j e c t ~ t o } } \quad B x = d ,
$$

where $A \in \mathbb { R } ^ { ( p + q ) \times n }$ ， $B \in \mathbb { R } ^ { s \times n }$ ,and $J$ is the signature matrix. It is assumed that $\operatorname { r a n k } ( B ) = s$ and that $x ^ { T } ( A ^ { T } J A ) x > 0$ for all $x > 0$ in $\mathcal { N } ( B )$ . These conditions imply that $p \ge n - s$ The solution to problem (3.2.23) satisfies

$$
\left( \begin{array} { c c c } { { 0 } } & { { 0 } } & { { B } } \\ { { 0 } } & { { J } } & { { A } } \\ { { B ^ { T } } } & { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { \lambda } } \\ { { s } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { d } } \\ { { b } } \\ { { 0 } } \end{array} \right) ,
$$

where $s = J r = J ( b - A x )$

# Algorithm 3.2.1(Generalized Householder QR Method).

1. Compute the Householder QR factorization of $B ^ { T }$ ： $B Q = B \left( Q _ { 1 } \quad Q _ { 2 } \right) = \left( R ^ { T } \quad 0 \right)$ and form $C _ { 2 } = A Q _ { 2 }$

2. Solve the lower triangular system $R ^ { T } y _ { 1 } = d$

3. Compute the hyperbolic QL factorization $H C _ { 2 } = \left( 0 \quad L _ { 2 2 } ^ { T } \right) ^ { T }$ ，where $L _ { 2 2 }$ is lower triangular and $H$ is $J$ -orthogonal, using Chambers' method.

4. Compute $f = ( f _ { 1 } ^ { T } f _ { 2 } ^ { T } ) ^ { T } = H ( b - A Q _ { 1 } y _ { 1 } )$ using the factored form of $H$

5. Solve the lower triangular system $L _ { 2 2 } y _ { 2 } = f _ { 2 }$ and set $x = Q y$

$J$ -orthogonal matrices can be constructed from orthogonal matrices as follows. Consider the partitioned linear system

$$
Q x = { \left( \begin{array} { l l } { Q _ { 1 1 } } & { Q _ { 1 2 } } \\ { Q _ { 2 1 } } & { Q _ { 2 2 } } \end{array} \right) } { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right) } = { \left( \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \end{array} \right) } ,
$$

where $Q$ is orthogonal. Solving the first equation for $x _ { 1 }$ and substituting in the second equation will exchange $x _ { 1 }$ and $y _ { 1 }$ . This can be written as

$$
{ \binom { x _ { 1 } } { y _ { 2 } } } = \operatorname { e x c } \left( Q \right) { \binom { y _ { 1 } } { x _ { 2 } } } ,
$$

where

$$
\begin{array} { r } { \operatorname { e x c } \left( Q \right) = \left( \begin{array} { c c } { Q _ { 1 1 } ^ { - 1 } } & { - Q _ { 1 1 } ^ { - 1 } Q _ { 1 2 } } \\ { Q _ { 2 1 } Q _ { 1 1 } ^ { - 1 } } & { Q _ { 2 2 } - Q _ { 2 1 } Q _ { 1 1 } ^ { - 1 } Q _ { 1 2 } } \end{array} \right) } \end{array}
$$

is the exchange operator. The $( 2 , 2 )$ block in (3.2.26) is the Schur complement of $Q _ { 1 1 }$ in $Q$ . An early reference to the exchange operator is in network analysis; see the survey by Tsatsomeros [1069,2000].

Theorem 3.2.5. Let $Q \in \mathbb { R } ^ { n \times n }$ be partitioned as in (3.2.25) with $Q _ { 1 1 }$ nonsingular: If $Q$ is orthogonal, then exc $( Q )$ is $J$ -orthogonal. If $Q$ is $J$ -orthogonal, then exc $( Q )$ is orthogonal.

Proof. See Pan and Plemmons [874, 198g,Lemma 1].

# Notes and references

Golub [489,196gl gave an early version of hyperbolic downdating. He noted that deleting a row $w ^ { T }$ in a least squares problem is formally equivalent to adding a row $i w ^ { T }$ ,where $i ^ { 2 } = - 1$ The resulting algorithm can be expressed entirely in real arithmetic; see Lawson and Hanson [727, 1995, pp.229-231]. The use of hyperbolic rotations in signal processing for downdating least squares solutions is studied by Alexander, Pan,and Plemmons [16,1988]. Rader and Steinhardt [908,1988] introduced hyperbolic Householder reflectors to zero several components at a time in a vector. Higham [624, 2oo3l gives a systematic treatment of $J .$ -orthogonal matrices and their many applications.Linear algebra with an indefinite inner product and applications thereof are treated by Gohberg, Lancaster,and Rodman [483,2oo5]． An algorithm using orthogonal transformations to reduce an indefinite symmetric matrix to block antitriangular form is given by Mastronardi and Van Dooren [782,2013]. By applying this to (3.2.24) they derive in [783, 2014] a stable algorithm for solving constrained indefinite least squares problems.

# 3.3 - Modified Least Squares Problems

# 3.3.1 - Modified Linear Systems

Consider the $2 \times 2$ block matrix

$$
M = \left( \begin{array} { c c } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right) .
$$

If $A$ is nonsingular, then $M$ can be factored into a product of a block lower and a block upper triangular matrix as

$$
M = { \left( \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right) } = { \left( \begin{array} { l l } { I } & { 0 } \\ { C A ^ { - 1 } } & { I } \end{array} \right) } { \left( \begin{array} { l l } { A } & { B } \\ { 0 } & { S } \end{array} \right) } , \quad S = D - C A ^ { - 1 } B .
$$

This factorization is equivalent to block Gaussian elimination and is easily verified by performing the product. The matrix $S$ is called the Schur complement of $A$ in $M$ .From (3.3.2) and the product rule for determinants it follows that

$$
\operatorname* { d e t } ( M ) = \operatorname* { d e t } ( A ) \operatorname* { d e t } ( S ) .
$$

In particular, for the $2 \times 2$ block triangular matrices

$$
L = \left( \begin{array} { c c } { { L _ { 1 1 } } } & { { 0 } } \\ { { L _ { 2 1 } } } & { { L _ { 2 2 } } } \end{array} \right) , \qquad U = \left( \begin{array} { c c } { { U _ { 1 1 } } } & { { U _ { 1 2 } } } \\ { { 0 } } & { { U _ { 2 2 } } } \end{array} \right)
$$

with square diagonal blocks, it holds that

$$
\operatorname * { d e t } ( L ) = \operatorname * { d e t } ( L _ { 1 1 } ) \operatorname * { d e t } ( L _ { 2 2 } ) , \qquad \operatorname * { d e t } ( U ) = \operatorname * { d e t } ( U _ { 1 1 } ) \operatorname * { d e t } ( U _ { 2 2 } ) .
$$

Hence $L$ and $U$ are nonsingular if and only if their diagonal blocks are nonsingular. Furthermore,

$$
\begin{array} { r } { L ^ { - 1 } = \left( \begin{array} { c c } { L _ { 1 1 } ^ { - 1 } } & { 0 } \\ { - L _ { 2 2 } ^ { - 1 } L _ { 2 1 } L _ { 1 1 } ^ { - 1 } } & { L _ { 2 2 } ^ { - 1 } } \end{array} \right) , \qquad U ^ { - 1 } = \left( \begin{array} { c c } { U _ { 1 1 } ^ { - 1 } } & { - U _ { 1 1 } ^ { - 1 } U _ { 1 2 } U _ { 2 2 } ^ { - 1 } } \\ { 0 } & { U _ { 2 2 } ^ { - 1 } } \end{array} \right) . } \end{array}
$$

These formulas can easily be verified by forming the products $L ^ { - 1 } L$ and $U ^ { - 1 } U$ and using the rule for multiplying partitioned matrices.

Let $M$ in (3.3.1) have a nonsingular block $A$ . Then from $M ^ { - 1 } = ( L U ) ^ { - 1 } = U ^ { - 1 } L ^ { - 1 }$ and (3.3.5) the Schur-Banachiewicz formula follows:

$$
M ^ { - 1 } = \left( \begin{array} { c c } { { A ^ { - 1 } + A ^ { - 1 } B S ^ { - 1 } C A ^ { - 1 } } } & { { - A ^ { - 1 } B S ^ { - 1 } } } \\ { { - S ^ { - 1 } C A ^ { - 1 } } } & { { S ^ { - 1 } } } \end{array} \right) ,
$$

where $S$ is the Schur complement of $A$ in $M$ Similarly, if $D$ is nonsingular, then $M$ can be factored into a product of a block upper and a block lower triangular matrix as

$$
M = \left( \begin{array} { c c } { { I } } & { { B D ^ { - 1 } } } \\ { { 0 } } & { { I } } \end{array} \right) \left( \begin{array} { c c } { { T } } & { { 0 } } \\ { { C } } & { { D } } \end{array} \right) , \quad T = A - B D ^ { - 1 } C ,
$$

where $T$ is the Schur complement of $D$ in $M$ . This is equivalent to block Gaussian elimination in reverse order.From this we obtain the expression

$$
M ^ { - 1 } = \binom { T ^ { - 1 } } { - D ^ { - 1 } C T ^ { - 1 } } \binom { - T ^ { - 1 } B D ^ { - 1 } } { D ^ { - 1 } + D ^ { - 1 } C T ^ { - 1 } B D ^ { - 1 } } .
$$

Woodbury [1131, $\mathrm { 1 9 5 0 } ] ^ { 5 }$ gave a formula for the inverse of a square nonsingular matrix $A$ after it has been modifed by a matrix of rank $p$ .This is very useful when $p \ll n$

Theorem 3.3.1 (The Woodbury Formula). Let $A \in \mathbb { R } ^ { n \times n }$ and $D = I _ { p } , p < n$ $A$ and $S = D - C A ^ { - 1 } B \in \mathbb { R } ^ { p \times p }$ are nonsingular, then

$$
( A - B C ) ^ { - 1 } = A ^ { - 1 } + A ^ { - 1 } B S ^ { - 1 } C A ^ { - 1 } .
$$

# which is the Woodbury formula.

Proof.Equate the $( 1 , 1 )$ blocks in the two expressions (3.3.6) and (3.3.8) for the inverse $M ^ { - 1 }$ . □

f $A = I _ { n }$ , then (3.3.9) simplifies to

$$
( I _ { n } - B C ) ^ { - 1 } = I _ { n } + B ( I _ { p } - C B ) ^ { - 1 } C ,
$$

which is sometimes called the matrix inversion lemma. Higham [626,2o17] shows that this formula follows directly from the associative law for matrix multiplications.

Let $A x = b$ be a given system with known solution $x = A ^ { - 1 } b$ , and let $\hat { x }$ satisfy the system

$$
( A - B C ) \hat { x } = b , \quad B , C ^ { T } \in \mathbb { R } ^ { n \times p } ,
$$

where $A$ has been modified by a matrix of rank $p$ . Then the Woodbury formula gives

$$
\hat { x } = x + W ( I _ { p } - C W ) ^ { - 1 } C x , \quad W = A ^ { - 1 } B .
$$

If an LU factorization of $A$ is already available,then computing $W = A ^ { - 1 } B$ requires $2 n ^ { 2 } p$ flops. Forming $( I _ { p } - C W )$ and its LU factorization takes $2 ( n p ^ { 2 } + p ^ { 3 } / 3 )$ flops.Finally, $4 n p + 2 p ^ { 2 }$ flops are needed for computing $C x$ and the correction to $x$ .When $p \ll n$ this is computationally advantageous compared to solving the modified system from scratch. For symmetric $A$ and $C = B ^ { T }$ , the Woodbury formula can be further simplified.

Let $p = 1$ ， $B C = \sigma u v ^ { T }$ , where $u , v \in \mathbb { R } ^ { n }$ and $\sigma \neq 0$ . Then the Woodbury formula (3.3 becomes

$$
( A - \sigma u v ^ { T } ) ^ { - 1 } = A ^ { - 1 } + \rho A ^ { - 1 } u v ^ { T } A ^ { - 1 } , \quad \rho = 1 / ( \sigma ^ { - 1 } - v ^ { T } A ^ { - 1 } u ) ,
$$

which is also known as the Sherman-Morrison formula. Note that if $\sigma ^ { - 1 } = v ^ { T } A ^ { - 1 } u$ ，then modified matrix $A - \sigma u v ^ { T }$ is singular. Otherwise,the solution $\hat { x }$ of the modified linear system

$( A - \sigma u v ^ { T } ) \hat { x } = b$ can be expressed as

$$
\hat { x } = x + \frac { v ^ { T } x } { \sigma ^ { - 1 } - v ^ { T } w } w , \quad w = A ^ { - 1 } u .
$$

The evaluation of this expression only requires the solution of two linear systems $A x = b$ and $A w = u$ If the LU factorization of $A$ is known,the arithmetic cost is only about $2 n ^ { 2 }$

The following related result was first proved by Egervary [361,196o] and is included as Example 1.34 in the seminal book by Householder [645,1975l. The sufficient part appeared earlier in Wedderburn [1105,1964].

Theorem 3.3.2. Let $A \in \mathbb { R } ^ { m \times n }$ be an arbitrary matrix and $u \in \mathbb { R } ^ { m }$ and $v \in \mathbb { R } ^ { n }$ be vectors. Then the rank of $B = A - \sigma u v ^ { T }$ is less than that of $A$ if and only if there are vectors $x \in \mathbb { R } ^ { n }$ and $y \in \mathbb { R } ^ { m }$ such that $u = A x$ $v = A ^ { T } y ,$ and $\sigma ^ { - 1 } = \boldsymbol { y } ^ { T } \boldsymbol { A } \boldsymbol { x }$ , in which case

$$
\operatorname { r a n k } ( B ) = \operatorname { r a n k } ( A ) - 1 .
$$

Note that the Woodbury and Sherman-Morrison formulas do not always lead to numerically stable algorithms,and therefore they should be used with some caution. Stability is a problem whenever the unmodified problem is conditioned in a worse way than the modified problem.

# Notes and references

The history of the Woodbury and similar updating formulas and their applications is surveyed by Henderson and Searle 601,1981]. Chu,Funderlic,and Golub [248,1995] explore extensions of the Wedderburn rank reduction formula that lead to various matrix factorizations. Explicit expressions for the pseudoinverse $( A + u v ^ { H } ) ^ { \dagger }$ are given by Meyer [793,1973l. Depending on which of the three conditions $u \in { \mathcal { R } } ( A )$ ， $v \in \mathcal { R } ( A ^ { H } )$ ,and $1 + v ^ { H } A ^ { \dagger } u \ne 0$ are satisfied, there are no less than six different cases. Generalizations of Meyer's results to perturbations of higher rank are not known. Some results for the pseudoinverse of sums of matrices are given by R. E. Cline [257,1965]. For rectangular or square singular matrices, no formulas similar to the Woodbury formula (3.3.9) with $A ^ { - 1 }$ replaced by the pseudoinverse $A ^ { \dagger }$ seem to exist.

# 3.3.2 - Modifying QR Factorizations

Many applications require the solution of a least squares problem after the data have been modified by adding or deleting variables and/or observations. Examples arise in regression problems, nonlinear and constrained least squares, optimization, signal processng,and prediction in control theory. Algorithms for updating least squares solutions date back to Gauss; see Farebrother [397, 1999].The first systematic use of algorithms for modifying matrix factorization seems to have been in optimization; see Gill et al. [472,1974].

We consider mainly algorithms for updating the QR factorization

$$
A = Q \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) , \quad Q = \left( Q _ { 1 } \quad Q _ { 2 } \right) \in \mathbb { R } ^ { m \times m } ,
$$

of $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ . Note that only $R$ and $Q _ { 1 }$ are uniquely determined. Because no efficient way to update a product of Householder reflections is known, we assume that $Q \in \mathbb { R } ^ { m \times m }$ is explicitly stored. Primarily,we consider algorithms for modifying a QR factorization when $A$ is subject to a low-rank change. The important special cases of adding or deleting a column or a row of $A$ are considered separately. Such updating algorithms require $O ( m ^ { 2 } )$ multiplications.

One application where such algorithms are needed is stepwise regresson. This is a greedy technique for selecting a suitable subset of variables in a linear regression model

$$
A x \approx b , \quad A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) \in \mathbb { R } ^ { m \times n } .
$$

The regression model is built sequentially by adding or deleting one variable at a time. Initially, set $x ^ { ( 0 \bar { ) } } = 0$ and $r ^ { ( 0 ) } = b$ Assume that at the current step, $k$ variables have entered the regres-sion,and the current residual is $r ^ { ( k ) } = b - A x ^ { ( k ) }$ . In the next step,the column $a _ { p }$ to add is chosen so that the residual norm is maximally decreased or, equivalently, the column that makes the smallest acute angle with the residual $r ^ { ( k ) }$ . Hence,

$$
\cos ( a _ { j } , r ^ { ( k ) } ) = { \frac { \left| a _ { j } ^ { T } r ^ { ( k ) } \right| } { \left\| a _ { j } \right\| _ { 2 } \left\| r ^ { k ) } \right\| _ { 2 } } }
$$

is maximized for $j = p$ over all variables not yet in the model. After a new variable has entered the regression, it may be that the contribution of some other variable included in the regression is no longer significant. This variable is then deleted from the regression model using a similar technique.

Efroymson [360,196o] gave an algorithm for stepwise regression based on Gauss-Jordan elimination on the normal equations.This is sensitive to perturbations and not numerically stable. Miler [794, 2oo2] surveys subset selection in regresson and emphasizes the computational and conceptual advantages of using methods based on QR factorization rather than normal equations. Eldén [366,1972] describes a backward stable method that uses Householder QR factorization that has the drawback of needing storage for a square matrix $Q \in \mathbb { R } ^ { m \times m }$ . A stable implementation of stepwise regression based on MGS with reorthogonalization is given by Gragg,LeVeque, and Trangenstein [522,1979] and essentially uses only the storage needed for $A$ and $b$

Methods for updating least squares solutions are closely related to methods for modifying matrix factorizations. If $A \in \mathbb { R } ^ { m \times n }$ has full column rank,the least squares solution is obtained from the extended QR factorization

$$
\begin{array} { r l } { ( \boldsymbol { A } } & { \boldsymbol { b } ) = \boldsymbol { Q } \left( \begin{array} { c c } { \boldsymbol { R } } & { \boldsymbol { z } } \\ { \boldsymbol { 0 } } & { \rho \boldsymbol { e } _ { 1 } } \end{array} \right) , \quad \boldsymbol { Q } \in \mathbb { R } ^ { m \times m } , } \end{array}
$$

where the right-hand side $b$ has been appended to $A$ as a last column． The solution is then obtained by solving the triangular system $R x = z$ , and the residual norm $\| A x - b \| _ { 2 }$ equals $\rho$ The upper triangular matrix $R$ in (3.3.16) is the Cholesky factor of

$$
\left( \begin{array} { c } { { A ^ { T } } } \\ { { b ^ { T } } } \end{array} \right) ( A \quad b ) = \left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } b } } \\ { { b ^ { T } A } } & { { b ^ { T } b } } \end{array} \right) .
$$

By applying algorithms for updating a QR factorization to the extended QR factorization (3.3.16) of $( A b )$ , we obtain algorithms for updating the solution of least squares problems.

The algorithms given in the following for modifying the full QR factorization are minor modifications of those given in LINPACK; see Dongarra et al. [322,1979,p. 10.2]. It is fairly straightforward to extend these to cases where a block of rows/columns is added or deleted. Such block algorithms are more amenable to efcient implementation on modern computers.

We point out that adding rows and deleting columns are inherently stable operations in the sense that the smallest singular value cannot decrease. On the other hand,when adding columns or deleting rows the smallest singular value can decrease,and a solution may not exist. In particular, deleting a row can be a very ill-conditioned problem.

# Appending a Row

Without lossof generality, we assume that a row $v ^ { T }$ is appended to $A \in \mathbb { R } ^ { m \times n }$ after the last row. Then we have

$$
\left( \begin{array} { c } { { A } } \\ { { v ^ { T } } } \end{array} \right) = \left( \begin{array} { c c } { { Q } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c } { { R } } \\ { { v ^ { T } } } \\ { { 0 } } \end{array} \right) .
$$

Hence the problem is equivalent to appending $v ^ { T }$ as the $( n + 1 ) \mathrm { t h }$ row to $R$ . Now, plane rotations $G _ { k , n + 1 }$ ， $k = 1 { : } n$ ,are determined to annihilate $v ^ { T }$ ,giving

$$
G \left( \begin{array} { c } { { R } } \\ { { v ^ { T } } } \end{array} \right) = \left( \begin{array} { c } { { \widetilde { R } } } \\ { { 0 } } \end{array} \right) , \quad G = G _ { n , n + 1 } \cdot \cdot \cdot G _ { 1 , n + 1 } .
$$

This requires $3 n ^ { 2 }$ flops. The updated factor becomes

$$
\widetilde { Q } = \left( \begin{array} { c c } { { Q } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) I _ { n + 1 , m + 1 } G ^ { T }
$$

and can be computed in 6mn flops. Note that $R$ can be updated without $Q$ being available. From the interlacing property of the singular values it follows that the updating does not decrease the singular values of $R$ .By the general rounding error analysis of plane rotations and Householder transformations,this updating algorithm is backward stable.

# General Rank-One Change

Given the QR factorization of $A \in \mathbb { R } ^ { m \times n }$ and vectors $u \in \mathbb { R } ^ { m }$ and $v \in \mathbb { R } ^ { n }$ , we want to compute QR factors of

$$
\widetilde { A } = A + u v ^ { T } = \widetilde { Q } \left( { \overset { \sim } { \boldsymbol { R } } } \right) ,
$$

where $A$ is perturbedbykonematrix.Wefistopte $w = Q ^ { T } u$ Then with ${ \boldsymbol { w } } = { \left( \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right) }$ $w _ { 1 } \in \mathbb { R } ^ { n }$ , it holds for any orthogonal $P$ that

$$
A + u v ^ { T } = Q P ^ { T } P \left[ \left( { R \atop 0 } \right) + \left( { w _ { 1 } \atop w _ { 2 } } \right) v ^ { T } \right] .
$$

Determine $H$ as a Householder reflection such that $H w _ { 2 } ~ = ~ \beta e _ { 1 }$ .Next,let $G _ { k , n + 1 }$ ， $k \mathbf { \Omega } =$ $n , n - 1 , \ldots , 1$ ,be a sequence of plane transformations that zeros the elements in $w _ { 1 }$ from the bottom up and creates a nonzero row below the matrix $R$ Taking $P _ { 1 }$ as the combination of these transformations,we have

$$
\begin{array} { r } { P _ { 1 } \bigg [ \bigg ( \begin{array} { c } { R } \\ { 0 } \end{array} \bigg ) + \bigg ( \begin{array} { c } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \bigg ) v ^ { T } \bigg ] = \left( \begin{array} { c } { R } \\ { z ^ { T } + \beta v ^ { T } } \\ { 0 } \end{array} \right) , \quad \beta = \pm \| w _ { 2 } \| _ { 2 } . } \end{array}
$$

Finally, a product $P _ { 2 }$ of plane rotations $\widetilde { G } _ { k , k + 1 } ( \phi _ { k } )$ is determined that zeros the elements in row $n + 1$ as described in the algorithm for adding a row. This gives the factor $\widetilde { R }$ ，The orthogonal factor is $\widetilde Q = Q P _ { 1 } ^ { T } P _ { 2 } ^ { T }$

The work needed for updating $R$ is $6 n ^ { 2 }$ flops.Applying the Householder transformations to $Q$ takes $4 m ( m - n )$ flops,and applying the plane transformations from steps 2 and 3 takes $1 2 m n$ flops. This gives a total of $4 m ^ { 2 } + 8 n m + 4 n ^ { 2 }$ flops. The algorithm can be shown to be mixed backward stable.

Remark 3.3.1. In another version of this algorithm the matrix $R$ was modified into a Hessenberg matrix by using a sequence of rotations $G _ { k , k + 1 }$ ， $k = n , n - 1 , \ldots , 1 .$ ,in step 3. The version given here is easier to implement since the modified row can be held in a vector.This becomes even more important for large sparse problems.

# Deleting a Column

We first observe that deleting the last column of $A$ in the QR factorization

$$
A = \left( \begin{array} { c c } { { A _ { 1 } } } & { { a _ { n } } } \end{array} \right) = Q \left( \begin{array} { c c } { { \tilde { R } } } & { { u } } \\ { { 0 } } & { { r _ { n n } } } \end{array} \right)
$$

is trivial. The QR factorization of $A _ { 1 }$ is obtained simply by deleting the trailing column from the decomposition. Suppose now that we want to compute the QR factorization

$$
\widetilde { A } = { \big ( } a _ { 1 } , \ldots , a _ { k - 1 } , a _ { k + 1 } , \ldots , a _ { n } { \big ) } ,
$$

where the $k$ th column of $A$ is deleted, $k < n$ . From the above observation it follows that this decomposition can readily be obtained from the QR factorization of the matrix

$$
A P _ { L } = ( a _ { 1 } , \ldots , a _ { k - 1 } , a _ { k + 1 } , \ldots , a _ { n } , a _ { k } ) ,
$$

where $P _ { L }$ is a permutation matrix that performs a left circular shift of the columns $a _ { k } , \ldots , a _ { n }$ The matrix $R P _ { L }$ is upper Hessenberg, but the matrix $P _ { L } ^ { T } R P _ { L }$ is upper triangular, except in its last row. For example, if $k = 3$ ， $n = 6$ , then it has the structure

$$
P _ { L } ^ { T } R P _ { L } = [ \begin{array} { c c } { { \times } } & { { \times } } \\ { { 0 } } & { { \times } } \\ { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} ] \times \times \times \times \times ] _ { \begin{array} { c } { \times } \\ { { \times } } \\ { { \times } } \end{array} }
$$

The task has now been reduced to constructing plane rotations $G _ { i , n }$ ， $i = k : n - 1$ , that zero out the off-diagonal elements in the last row. Only the trailing principal submatrix of order $n - k + 1$ in $P _ { L } ^ { T } R P _ { L }$ , which has the form

$$
\left( \begin{array} { c c } { { R _ { 2 2 } } } & { { 0 } } \\ { { v ^ { T } } } & { { r _ { n n } } } \end{array} \right) ,
$$

participates in this transformation. After the last column is deleted , the remaining update of $R _ { 2 2 }$ is precisely the same as already described for adding a row. The updated Q factor is

$$
\widetilde { Q } = Q P _ { L } G _ { k , n } ^ { T } \cdot \cdot \cdot G _ { n - 1 , n } ^ { T } .
$$

By an obvious extension of the above algorithm, we obtain the QR factorization of the matrix resulting from a left circular shift applied to a set of columns $( a _ { 1 } , \ldots , a _ { k - 1 } , a _ { k + 1 } , \ldots , a _ { p } , a _ { k } .$ $a _ { p + 1 } , \ldots , a _ { n } )$

# Inserting a Column

Assume that the QR factorization

$$
A = ( a _ { 1 } , \ldots , a _ { k - 1 } , a _ { k + 1 } , \ldots , a _ { n } ) = Q \left( { R \atop 0 } \right) , \quad k \neq n ,
$$

is known. We want to compute the QR factorization of $\widetilde { A } = ( a _ { 1 } , \ldots , a _ { n } )$ ，where the $k$ th column $a _ { k }$ is inserted. We assume that $a _ { k } \notin \mathcal { R } ( A )$ ,because otherwise $\widetilde { A }$ is singular. Then

$$
w = Q ^ { T } a _ { k } = { \binom { u } { v } } , \quad u \in \mathbb { R } ^ { n } ,
$$

where $\gamma = \| v \| _ { 2 } \neq 0$ Let $H _ { n }$ be a Householder reflector such that $H _ { n } ^ { T } v = \gamma e _ { 1 }$ . Then we have the QR factorization

$$
\left( \begin{array} { l l } { \boldsymbol { A } } & { \boldsymbol { a } _ { k } } \end{array} \right) = \widetilde { Q } \left( \begin{array} { l } { \widetilde { R } } \\ { 0 } \end{array} \right) , \quad \widetilde { Q } = Q \left( \begin{array} { l l } { \boldsymbol { I } _ { n } } & { \boldsymbol { 0 } } \\ { 0 } & { \boldsymbol { H } _ { n } } \end{array} \right) , \quad \widetilde { R } = \left( \begin{array} { l l } { \boldsymbol { R } } & { \boldsymbol { u } } \\ { 0 } & { \gamma } \end{array} \right) .
$$

Let $P _ { R }$ be the permutation matrix tat performs arightcircularshift onthecolumns $a _ { k + 1 } , \ldots$ $a _ { n } , a _ { k }$ , so that

$$
\widetilde { A } = \left( A \quad a _ { k } \right) P _ { R } = \widetilde { Q } \left( \begin{array} { c } { { \widetilde { R } P _ { R } } } \\ { { 0 } } \end{array} \right) , \quad \widetilde { R } P _ { R } = \left( \begin{array} { c c c } { { R _ { 1 1 } } } & { { u _ { 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { u _ { 2 } } } & { { R _ { 2 2 } } } \\ { { 0 } } & { { \gamma } } & { { 0 } } \end{array} \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { ( k - 1 ) \times ( k - 1 ) }$ and $R _ { 2 2 } \ \in \ \mathbb { R } ^ { ( n - k ) \times ( n - k ) }$ are uppe triangular. For example,for $k = 4 , n = 6$ ,we have

$$
\widetilde { R } P _ { R } = \left[ \begin{array} { l l l } { { \times } } & { { \times } } & { { \times } } \\ { { 0 } } & { { \times } } & { { \times } } \\ { { 0 } } & { { 0 } } & { { \times } } \\ { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] \times \left[ \begin{array} { l l } { { \times } } & { { \times } } \\ { { \times } } & { { \times } } \\ { { \times } } & { { \times } } \\ { { \times } } & { { \times } } \\ { { 0 } } & { { \times } } \\ { { 0 } } & { { \times } } \\ { { 0 } } & { { 0 } } \end{array} \right] .
$$

Now determine plane rotations $G _ { i - 1 , i }$ ， $i = n \colon - 1 \colon k$ ,to zero the last $n - k$ elements in the $k$ th column of $\widetilde { R P } _ { R }$ . Then

$$
G _ { k - 1 , k } \cdot \cdot \cdot G _ { n - 1 , n } \left( \begin{array} { c c } { { u _ { 2 } } } & { { R _ { 2 2 } } } \\ { { \gamma } } & { { 0 } } \end{array} \right) = \widetilde { R } _ { 2 2 }
$$

is upper triangular, and the updated factors are

$$
\begin{array} { r } { \overline { { \boldsymbol { R } } } = \left( \begin{array} { c c } { R _ { 1 1 } } & { \widetilde { R } _ { 1 2 } } \\ { 0 } & { \widetilde { R } _ { 2 2 } } \end{array} \right) , \qquad \overline { { \boldsymbol { Q } } } = \widetilde { \boldsymbol { Q } } \boldsymbol { G } _ { n - 1 , n } ^ { T } \cdot \cdot \cdot \boldsymbol { G } _ { k - 1 , k } , } \end{array}
$$

where $\widetilde { R } _ { 1 2 } = \left( u _ { 1 } \quad R _ { 1 2 } \right)$

The above method easily generalizes to computing QR factors of

$$
( a _ { 1 } , \ldots , a _ { k - 1 } , a _ { p } , a _ { k } , \ldots , a _ { p - 1 } , a _ { p + 1 } , \ldots , a _ { n + 1 } ) ,
$$

i.e., of the matrix resulting from a right circular shift of the columns $a _ { k } , \dotsc , a _ { p }$ . Note that when a column is deleted, the new $R$ -factor can be computed without $Q$ being available. However, when a column is added, it is essential that $Q$ be known.

The algorithms given for appending and deleting a column correspond to the MATLAB functions qrinsert $( \mathtt { Q } , \mathtt { R } , \mathtt { k } , \mathtt { a k } )$ and qrdelete $( \mathbb { Q } , \mathbb { R } , \mathbb { k } )$

# Deleting a Row

Suppose we are given the QR factorization of $A \in \mathbb { R } ^ { m \times n }$ ，

$$
A = \left( \begin{array} { c } { { a _ { 1 } ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right) = Q \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) ,
$$

and want to find the QR factorization of $\widetilde { A }$ ,where the first row $a _ { 1 } ^ { T }$ of $A$ is deleted. This is known as the downdating problem. If $q ^ { T } = e _ { 1 } ^ { T } Q = \left( q _ { 1 } ^ { T } \quad q _ { 2 } ^ { T } \right)$ is the first row of $Q$ ,then

$$
\left( \begin{array} { c c } { { a _ { 1 } ^ { T } } } & { { 1 } } \\ { { \widetilde { A } } } & { { 0 } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { q _ { 1 } } } \\ { { 0 } } & { { q _ { 2 } } } \end{array} \right) .
$$

Let $H$ be a Householder reflection such that $H q _ { 2 } ~ = ~ \gamma e _ { 1 }$ ， $\gamma ~ = ~ \pm \| q _ { 2 } \| _ { 2 }$ .Next, let $G \ =$ $G _ { 1 , 2 } \cdot \cdot \cdot G _ { n , n + 1 }$ be plane rotations such that $G \left( { \begin{array} { c } { q _ { 1 } } \\ { \gamma } \end{array} } \right) \ = \ \alpha e _ { 1 }$ Since $q$ is a unit vector, we must have $| \alpha | = 1$ .It is no restriction to assume that $\alpha = 1$ . Then

$$
G \left( \begin{array} { c c } { { I _ { n } } } & { { 0 } } \\ { { 0 } } & { { H } } \end{array} \right) \left( \begin{array} { c c } { { R } } & { { q _ { 1 } } } \\ { { 0 } } & { { q _ { 2 } } } \end{array} \right) = \left( \begin{array} { c c } { { v ^ { T } } } & { { 1 } } \\ { { \widetilde { R } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $\widetilde { R } \in \mathbb { R } ^ { n \times n }$ is upper triangular, and the row vector $v ^ { T } = a _ { 1 } ^ { T }$ has been generated. To find the downdated factor $\bar { Q }$ we need not consider the transformation $H$ ,because it does not affect its first $n$ columns. The matrix $Q G ^ { T }$ is orthogonal,and by (3.3.23) its first row must equal $e _ { 1 } ^ { T }$ Therefore it must have the form

$$
Q G ^ { T } = \left( { \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { { \widetilde { Q } } } \end{array} } \right)
$$

with $\widetilde { Q }$ orthogonal. It then follows that

$$
\left( \begin{array} { c c } { { a _ { 1 } ^ { T } } } & { { 1 } } \\ { { \widetilde { A } } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \widetilde { Q } } } \end{array} \right) \left( \begin{array} { c c } { { v ^ { T } } } & { { 1 } } \\ { { \widetilde { R } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

which shows that $a _ { 1 } = v$ The desired factoriation $\widetilde { A } = \widetilde { Q } \left( \begin{array} { c c } { { \widetilde { R } } } \\ { { 0 } } \end{array} \right)$ is now obtained by deleting the first row and last column on both sides of the equation. Note the essential role played by the first row of $Q$ in this algorithm.

In downdating, the singular values of $R$ can decrease, and $\widetilde { R }$ can become singular. Paige [859, $1 9 8 0 ]$ has proved that the above downdating algorithm is mixed stable, i.e., the computed $\widetilde { R }$ is close to the corresponding exact factor of a nearby matrix $\widetilde A + E$ ，where $\| E \| < c \mathbf { u }$

# Block Downdating a QR Factorization

The algorithms for modifying the QR factorization can be extended to modifications of rank $k > 1$ . This applies in particular to cases when blocks of rows or columns are added or deleted. Compared to repeated applications of the corresponding rank-one algorithm, such algorithms can be implemented using matrix-matrix operations and hence should execute more efficiently.

We describe a downdating algorithm when $k > 1$ rows are to be deleted. The other algorithms can be similarly modified. Let the QR factorization of $A \in \mathbb { R } ^ { m \times n }$ be

$$
A = { \binom { A _ { 1 } } { A _ { 2 } } } = Q { \binom { R } { 0 } } = { \binom { Q _ { 1 1 } } { Q _ { 2 1 } } } { \binom { Q _ { 1 2 } } { Q _ { 2 2 } } } \left( { \binom { R } { 0 } } , \right) ,
$$

where $Q _ { 1 1 } \in \mathbb { R } ^ { k \times n }$ and $Q _ { 1 2 } \in \mathbb { R } ^ { k \times ( m - n ) }$ . We want to find the QR factors of $A _ { 2 }$ , where the first block of $k$ rows $A _ { 1 } \in \mathbb { R } ^ { k \times n }$ is deleted. From $Q Q ^ { T } = I _ { m }$ it follows that

$$
\left( \begin{array} { c c } { { A _ { 1 } } } & { { I _ { k } } } \\ { { A _ { 2 } } } & { { 0 } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { Q _ { 1 1 } ^ { T } } } \\ { { 0 } } & { { Q _ { 1 2 } ^ { T } } } \end{array} \right) .
$$

Compute the QR factorization of $Q _ { 1 2 } ^ { T }$ by finding a product $H$ of Householder reflections such that $H Q _ { 1 2 } ^ { T } = U \in \mathbb { R } ^ { k \times k }$ is upper triangular.Next,let $G$ be a productof plane rotations such that

$$
\binom { P } { 0 } = G \left( \begin{array} { c } { { Q _ { 1 1 } ^ { T } } } \\ { { U } } \end{array} \right) = G \left( \begin{array} { c c } { { I _ { n } } } & { { 0 } } \\ { { 0 } } & { { H } } \end{array} \right) \left( \begin{array} { c } { { Q _ { 1 1 } ^ { T } } } \\ { { Q _ { 1 2 } ^ { T } } } \end{array} \right) ,
$$

with $P \in \mathbb { R } ^ { k \times k }$ uppe triangular withpositive diagonal elements.Byorthogonalt,

$$
P P ^ { T } = \left( Q _ { 1 1 } \quad Q _ { 1 2 } \right) \left( { Q } _ { 1 1 } ^ { T } \right) = I _ { k } .
$$

Hence $P$ is orthogonal, and because it is triangular, it must equal $I _ { k }$ . Then

$$
G \left( \begin{array} { c c } { { I _ { n } } } & { { 0 } } \\ { { 0 } } & { { H } } \end{array} \right) \left( \begin{array} { c c } { { R } } & { { Q _ { 1 1 } ^ { T } } } \\ { { 0 } } & { { Q _ { 1 2 } ^ { T } } } \end{array} \right) = \left( \begin{array} { c c } { { V } } & { { I _ { k } } } \\ { { \widetilde { R } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $\widetilde { R } \in \mathbb { R } ^ { n \times n }$ is upper triangular, and $V$ has been generated. To find the downdated factor $\tilde { Q }$ we need not consider the transformation $H$ ,which does not affect its first $n$ columns.The matrix $Q G ^ { T }$ is orthogonal,and from (3.3.27) its $k$ first rows must equal $\left( \begin{array} { l l } { I _ { k } } & { 0 } \end{array} \right)$ . It follows that

$$
Q G ^ { T } = \left( \begin{array} { c c } { { I _ { k } } } & { { 0 } } \\ { { 0 } } & { { \widetilde Q } } \end{array} \right) ,
$$

where $\widetilde { Q }$ is orthogonal, and

$$
\left( \begin{array} { c c } { { A _ { 1 } } } & { { I _ { k } } } \\ { { A _ { 2 } } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { I _ { k } } } & { { 0 } } \\ { { 0 } } & { { \widetilde { Q } } } \end{array} \right) \left( \begin{array} { c c } { { V } } & { { I _ { k } } } \\ { { \widetilde { R } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) .
$$

This shows that $V = A _ { 1 }$ . Equating the last block of rows,we obtain the desired downdated factorization

$$
A _ { 2 } = \widetilde { Q } \left( \begin{array} { c c } { { \widetilde { R } } } \\ { { 0 } } \end{array} \right) .
$$

# 3.3.3 - Downdating the Cholesky Factorization

In the downdating problem of Section 3.3.2 we are given the QR factorization of

$$
A = \left( \begin{array} { c } { { z ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right)
$$

and want to determine the QR factors of $\widetilde { A }$ ，The downdating transformations are determined by the first row of the full matrix $Q \in \mathbb { R } ^ { m \times m }$ .In many applications,storing and modifying $Q$ is too costly. Then one would like to modify the upper triangular $R \in \mathbb { R } ^ { n \times n }$ without knowledge of $Q$ . This is the Cholesky downdating problem: Given $R$ and $z$ ,determine $\widetilde { R }$ such that

$$
\widetilde { R } ^ { T } \widetilde { R } = R ^ { T } R - z z ^ { T } .
$$

The Cholesky factor $R$ is mathematically the same as $R$ in the QR factorization. Any downdating algorithm that uses only $R$ and not $Q$ or the original data $A$ relies on less information and cannot be expected to give full accuracy.

In the LINPACK algorithm due to Saunders [963,1972], one seeks to recover the necessary information in $Q$ using the original data from $A$ . The first row of the QR factorization can be written

$$
e _ { 1 } ^ { T } A = q ^ { T } \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) , \quad q ^ { T } = e _ { 1 } ^ { T } Q = \left( q _ { 1 } ^ { T } \quad q _ { 2 } ^ { T } \right) ,
$$

giving $z ^ { T } = q _ { 1 } ^ { T } R$ Thus $q _ { 1 } \in \mathbb { R } ^ { n }$ can be found from $A$ by forward substitution in the lower triangular system $R ^ { T } q _ { 1 } = A ^ { T } e _ { 1 } = z$ Furthermore, $\| q \| _ { 2 } ^ { 2 } = \| q _ { 1 } \| _ { 2 } ^ { 2 } + \| q _ { 2 } \| _ { 2 } ^ { 2 } = 1$ , and hence

$$
\gamma = \| q _ { 2 } \| _ { 2 } = ( 1 - \| q _ { 1 } \| _ { 2 } ^ { 2 } ) ^ { 1 / 2 } .
$$

This allows the downdated factor $\widetilde { R }$ to be computed as described previously in Section 3.3.2 by a sequence of plane rotations $G _ { k , n + 1 }$ ， $k = n , n - 1 , \ldots , 1$ ,constructed so that

$$
G _ { 1 , n + 1 } \cdot \cdot \cdot G _ { n , n + 1 } \left( { q _ { 1 } \atop \gamma } \right) = \alpha e _ { n + 1 } , \quad \alpha = 1 ,
$$

and

$$
G _ { 1 , n + 1 } \cdot \cdot \cdot G _ { n , n + 1 } \left( { R \atop 0 } \right) = \left( { \widetilde R \atop v ^ { T } } \right) .
$$

Then,as in (3.3.24), $\widetilde { R }$ is the downdated factor,and $v = z$ ． As described, the LINPACK algorithm requires about $3 n ^ { 2 }$ flops.By interleaving the two phases,Pan [871,199o] gives an implementation that uses $40 \%$ fewer multiplications.

We can write

$$
\begin{array} { r } { R ^ { T } R - z z ^ { T } = R ^ { T } ( I _ { n } - q _ { 1 } q _ { 1 } ^ { T } ) R = \tilde { R } ^ { T } \tilde { R } . } \end{array}
$$

If we put $I - q _ { 1 } q _ { 1 } ^ { T } = L L ^ { T }$ , then $\tilde { R } = L ^ { T } R$ The matrix $I - q _ { 1 } q _ { 1 } ^ { T }$ has $n - 1$ eigenvalues equal to 1 and one equal to $\gamma ^ { 2 } = 1 - \| q _ { 1 } \| _ { 2 } ^ { 2 } \leq 1$ .Hence, $\sigma _ { n } ( L ) = \gamma$ If $\gamma$ is small, there will be severe cancellation in the computation of $1 - \| q _ { 1 } \| _ { 2 } ^ { 2 }$ . When $\gamma \approx { \bf u } ^ { 1 / 2 }$ the LINPACK algorithm can break down. In Saunders [963,1972] the downdate was used only on a square matrix $A$ Then we know that $\gamma = 0$ ,and there is no danger of breakdown. However, Example 3.3.3 below shows the danger of not having $Q$

Downdating the Cholesky factor $R$ is an inherently less stable operation than downdating both $Q$ and $R$ in the QR factorization. The best we can expect is that the computed downdated factor $\widetilde { R }$ is the exact Cholesky factor of

$$
( R + E ) ^ { T } ( R + E ) - ( z + f ) ( z + f ) ^ { T } ,
$$

where $\| E \| _ { 2 }$ and $\| f \| _ { 2 }$ are modest constants times machine precision.

Pan [872,1993l gives a first-order perturbation analysis that shows that the normwise relative sensitivity of the Cholesky downdating problem can be measured by

$$
\xi ( R , z ) = \kappa ( R ) + \kappa ^ { 2 } ( R ) ( 1 - \gamma ^ { 2 } ) / \gamma ^ { 2 } ,
$$

where $\gamma$ is defined as in (3.3.3O). Hence an ill-conditioned downdating problem is signaled by a small value of $\gamma$ ,but the condition number of $R$ also plays a role. Sun [1049,1995] derives two different condition numbers,

$$
\kappa ( R , z ) = \kappa ( R ) / \gamma ^ { 3 } , \qquad c ( R , z ) = \kappa ( \widetilde { R } ) / \gamma ^ { 2 } .
$$

Numerical tests show that in most cases, $c ( R , z )$ is the smallest. Note that the suggested condition numbers can be cheaply estimated using a standard condition estimator.

Example 3.3.3. Consider the least squares problem $\operatorname* { m i n } \| A x - b \| _ { 2 }$ , where

$$
A = { \binom { \tau } { 1 } } , \quad b = { \binom { 1 } { 1 } } , \quad \tau = 1 / { \sqrt { u } } ,
$$

and $u$ is the unit roundoff. We may think of the first row of $A$ as an outlier. The QR factorization of $A$ , correctly rounded to single precision, is

$$
A = \binom { \tau } { 1 } = \binom { 1 } { \epsilon } - \epsilon \biggr ) \binom { \tau } { 0 } ,
$$

where $\epsilon = 1 / \tau$ . The LINPACK algorithm computes $q _ { 1 } = \tau / \tau = 1$ ,giving $\gamma ^ { 2 } = 1 - 1 = 0$ ,and $G _ { 1 } = I$ .Hence it gives the downdated factor $\widetilde { R } = 0$ ,and the downdated least squares solution is not defined. It is easily verified that if we downdate using $Q$ , we get the correct result $\widetilde R = 1$ and the downdated solution $x = 1$

An alternative downdating method that uses both $R$ and $A$ but not $Q$ is given by Bjorck, Eldén,and Park [151,1994].Let $v$ be the solution of $\operatorname* { m i n } _ { v } \| A v - e _ { 1 } \| _ { 2 }$ .Then the $R$ -factor of $\left( \begin{array} { l l } { A } & { e _ { 1 } } \end{array} \right)$ is

$$
\left( { \begin{array} { c c } { R } & { q _ { 1 } } \\ { 0 } & { \gamma } \end{array} } \right) , \quad q _ { 1 } = R v .
$$

The connected seminormal equations (CSNE) downdating algorithm first computes $v$ from the so-called seminormal equations (SNE) $R ^ { T } R v \ : = \ : A ^ { T } e _ { 1 }$ ．A corrected solution $v + \delta v$ is then determined from

$$
r = A v , \quad R ^ { T } R \delta v = r , \quad v : = v + \delta v ,
$$

giving

$$
q _ { 1 } = R v , \quad \gamma = \| A v - e _ { 1 } \| _ { 2 } .
$$

The update of $R$ then proceeds as in the LINPACK algorithm. A similar procedure can be used to downdate the augmented $R$ -factor (3.3.16) by solving the least squares problem

$$
\operatorname* { m i n } _ { x , \phi } \left\| \left( { \overset { A } { A } } \quad b \right) \left( { \overset { x } { \phi } } \right) - e _ { 1 } \right\| _ { 2 }
$$

using the CSNE method. This leads to an accurate downdating algorithm for least squares problems.However, the modifications are not trivial, partly because the condition number of the augmented $R$ -factor is large when $\rho$ is small.An error analysis of the CSNE method is given in Section 2.5.4.

The CSNE downdating algorithm requires three more triangular solves than the LINPACK algorithm and an additional four matrix-vector products.Thus,a hybrid algorithm is preferable in which the CSNE algorithm is used only when the downdating problem is ill-conditioned.

It is often required to find the downdated Cholesky factor after a modification of rank $k > 1$ This can be performed as a sequence of $k$ rank-one modifications. However, block methods using matrix-matrix and matrix-vector operations can execute more efficiently. Let $R$ in $A ^ { T } A = R ^ { T } R$ and $Z \in \mathbb { R } ^ { k \times n }$ be given. The Cholesky block downdating problem seeks $\widetilde { R }$ such that

$$
\widetilde { R } ^ { T } \widetilde { R } = A ^ { T } A - Z ^ { T } Z .
$$

The LINPACK algorithm can be generalized as follows. Suppose the first $k$ rows $Z$ in $A$ are to be deleted. We have

$$
A = \left( \begin{array} { l } { Z } \\ { \tilde { A } } \end{array} \right) = Q \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) = \left( \begin{array} { l l } { Q _ { 1 1 } } & { Q _ { 1 2 } } \\ { Q _ { 2 1 } } & { Q _ { 2 2 } } \end{array} \right) \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) ,
$$

where $Q \in \mathbb { R } ^ { m \times m }$ has been partitioned so that $Q _ { 1 1 } \in \mathbb { R } ^ { k \times n }$ . It follows that

$$
Z = \left( I _ { k } \quad 0 \right) A = \left( I _ { k } \quad 0 \right) Q \left( { } _ { 0 } ^ { R } \right) = Q _ { 1 1 } R .
$$

Hence $Q _ { 1 1 } \in \mathbb { R } ^ { k \times n }$ can be determined as in LINPACK by solving the triangular matrix equation $R ^ { T } Q _ { 1 1 } ^ { T } = Z$ . Furthermore,using the orthogonality of $Q$ ,we have

$$
I _ { k } = \left( \begin{array} { l l } { Q _ { 1 1 } } & { Q _ { 1 2 } } \end{array} \right) \left( \begin{array} { l } { Q _ { 1 1 } ^ { T } } \\ { Q _ { 1 2 } ^ { T } } \end{array} \right) ,
$$

which shows that $Q _ { 1 2 } Q _ { 1 2 } ^ { T } = I _ { k } - Q _ { 1 1 } Q _ { 1 1 } ^ { T }$ . Hence we can take $Q _ { 1 2 } = \left( L \quad 0 \right) \in \mathbb { R } ^ { k \times ( m - n ) }$ ， where $L$ is the lower triangular Cholesky factor of $I _ { k } - Q _ { 1 1 } Q _ { 1 1 } ^ { T }$ . The downdating can then proceed as in block downdating of the QR factorization described in Section 3.3.2.

Algorithms for block downdating the Cholesky factorization using hyperbolic transformations are given by Bojanczyk and Steinhardt [168,1991] and Liu [756, 2O11]. They proceed in $n$ steps to compute

$$
P _ { n } \cdot \cdot \cdot P _ { 1 } \left( { Z } \atop { R } \right) = \left( { \begin{array} { l } { 0 } \\ { { { \widetilde R } } } \end{array} } \right) ,
$$

where each transformation $P _ { i }$ consists of a Householder reflection followed by a hyperbolic rotation; see Section 3.2.4. In step $i$ ， $i = 1 , \ldots , n$ ,a Householder reflection $H _ { i }$ is used to zero all elements in the $i$ th column of $Z$ ,except $z _ { k , i }$ which then is zeroed by a hyperbolic rotation $G _ { k , k + i }$ acting on rows $k , k + i$ .If the problem is positive definite,the process will not break down. The first two steps in the reduction are shown below for the case $n = 4$ ， $k = 3$

$$
H _ { 1 } \left[ \begin{array} { c c c c } { \otimes } & { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & & { \times } & { \times } \\ & & & { \times } \end{array} \right] \Rightarrow G _ { 3 , 4 } \left[ \begin{array} { c c c c } { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & & & { \times } & { \times } \end{array} \right] \Rightarrow G _ { 3 , 5 } H _ { 2 } \left[ \begin{array} { c c c c } { \otimes } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } \\ { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } \end{array} \right]
$$

# Notes and references

First-order perturbation analysis for the block downdating problem for the Cholesky factor is given by Eldén and Park [378,1994], Sun [1049,1995],and Chang and Paige [234,1998]. Olszanskyj,Lebak,and Bojanczyk [843,1994] extend the LINPACK, Gram-Schmidt, and CSNE downdating algorithms to block downdating and provide experimental results comparing their numerical accuracy. LAPACK-style codes for updating the QR factorization after a block of rows or columns are added or deleted are given by Hammarling et al. [565, 2006].

# 3.3.4 - Recursive Least Squares Methods

In signal processing,control systems,and communication, data often arrive continuously in real time for processing. Assume that a sequence of least squares problems $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ is to be solved, where new equations are added and old ones deleted. If $A \in \mathbb { R } ^ { m \times n }$ has full column rank, the unique solution is $x = C A ^ { T } b$ ，where $C = ( A ^ { T } A ) ^ { - 1 }$ is the covariance matrix apart from a scaling factor. Suppose now that a block of equations $B x = c$ ， $B \in \mathbb { R } ^ { p \times n }$ ,is appended. The updated normal equations are

$$
( A ^ { T } A + B ^ { T } B ) \widetilde x = A ^ { T } b + B ^ { T } c .
$$

Adding $B ^ { T } B x$ to both sides ofthe original normal equations $A ^ { T } A x = A ^ { T } b$ and subtracting gives

$$
( A ^ { T } A + B ^ { T } B ) ( \widetilde { x } - x ) = B ^ { T } r _ { p } , \quad r _ { p } = c - B x ,
$$

where $r _ { p }$ is the predicted residual for the added equations. Hence the updated solution becomes

$$
\widetilde { \boldsymbol { x } } = \boldsymbol { x } + \widetilde { C } \boldsymbol { B } ^ { T } \boldsymbol { r } _ { p } , \quad \widetilde { C } = ( \boldsymbol { A } ^ { T } \boldsymbol { A } + \boldsymbol { B } ^ { T } \boldsymbol { B } ) ^ { - 1 } ,
$$

where $\widetilde { C }$ is the updated covariance matrix. From the Woodbury formula (3.3.9) we obtain the expression

$$
\widetilde { C } = C - U ( I _ { p } + B U ) ^ { - 1 } U ^ { T } , \quad U = C B ^ { T } .
$$

In particular, adding a single equation $v ^ { T } x = \gamma$ gives $\rho = \gamma - v ^ { T } x$ ， $u = C v$ ,and

$$
\widetilde { C } = C - u u ^ { T } / ( 1 + v ^ { T } u ) , \quad \widetilde { x } = x + \rho \widetilde { C } v ,
$$

where $\rho$ is the predicted residual and $\widetilde { u } = \widetilde { C } v$ is the so-called Kalman gain vector. With slight modifications these equations can be used also for deleting an equation $w ^ { T } x = \gamma$ Provided that $1 - w ^ { T } u > 0$ , we obtain

$$
\widetilde { C } = C + u { u ^ { T } } / ( 1 - w ^ { T } u ) , \qquad \widetilde { x } = x - ( \gamma - w ^ { T } x ) \widetilde { C } w .
$$

The simplicity of this recursive least squares updating algorithm has made it popular for many applications. Because $C ~ = ~ ( R ^ { T } R ) ^ { - 1 }$ ， such schemes are called square root methods in the signal processing literature. However, such methods lack stability because they are based on the normal equation. When accuracy is important,an algorithm that updates the factor $R$ from a QR factorization should be preferred. Adding a single equation $v ^ { T } x = \gamma$ leads to the following recursive least squares (RLS) algorithm.

1. Compute the predicted residual $\rho = \gamma - v ^ { T } x$ and $v ^ { T } u = v ^ { T } C v = \lVert R ^ { - T } v \rVert _ { 2 } ^ { 2 } .$

2. Compute te updated QR factorizationof $\left( \begin{array} { l } { R } \\ { v ^ { T } } \end{array} \right)$ to obtain $\widetilde { R }$

3. Compute the updated solution $\widetilde { x } = x + \rho \widetilde { u }$ where $\widetilde { u } = \widetilde { R } ^ { - 1 } ( \widetilde { R } ^ { - T } v )$

Pan and Plemmons [874,198g] have developed alternative algorithms that instead update or downdate the inverse Cholesky factor $R ^ { - 1 }$ . Such schemes can be more easily parallelized, because no back-substitutions are involved. The vector $\widetilde { u }$ can be computed by matrix-vector multiplication, and the covariance matrix $( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }$ is more readily recovered. These are important considerations for applications in signal processing.

In nonstationary time series calculations it is necessary to suppress older data. Often a sliding window moving over the data is used in which a new observation is added and the oldest observation is deleted. Another method to suppress older data is called exponential windowing. Let $\beta \in ( 0 , 1 )$ be a forgetting factor. Then the rows in the current data matrix $X _ { m } = ( A _ { m } , \ b _ { m } ) \in \mathbb { R } ^ { m \times ( n + 1 ) }$ are weighted with

$$
D _ { m } = \mathrm { d i a g } ( \beta ^ { m - 1 } , \ldots , \beta , 1 ) ,
$$

and the QR factorization $D _ { m } X _ { m } = Q _ { m } R _ { m }$ is computed. Hence as $m$ increases,the older data influence the solution less and less. Then $R _ { m + 1 }$ can be computed as the QR factorization of

$$
\left( \begin{array} { l } { \beta R _ { m } } \\ { x _ { m + 1 } } \end{array} \right) .
$$

Exponential windowing makes it possible to look at arbitrarily long sequences of data. Stewart [1029,1995] shows that both the LINPACK and Chambers downdating algorithms are relationally stable in the sense that old rounding errors are damped along with the data.

# 3.3.5 - Modifying the Gram-Schmidt QR Factorization

For least squares problems with $m \gg n$ it is usually not feasible to store and update the full square matrix $Q \in \mathbb { R } ^ { m \times m }$ in the QR factorization.By instead modifying the compact Gram-Schmidt QR factorization

$$
A = Q _ { 1 } R , \quad Q _ { 1 } = ( q _ { 1 } , \dots , q _ { n } ) \in \mathbb { R } ^ { m \times n } ,
$$

storage and operation counts for a rank-one modification are reduced from $O ( m ^ { 2 } )$ to $O ( m n )$ Such algorithms for adding and deleting rows and columns in the compact QR factorization are developed by Daniel et al. [285,1976]. Their algorithms use Gram-Schmidt QR with reorthogonalization. Reichel and Gragg [917,199ol give optimized Fortran subroutines implementing similar methods.

Adding a column in the last position in the QR factorization is straightforward and equal to an intermediate step in a columnwise Gram-Schmidt. Similarly, deleting the last column of $A$ in the factorization $A = Q _ { 1 } R$ is trivial. Inserting or deleting a column in another position requires computing QR factors of a permuted triangular matrix. This can be done by a series of plane rotations as described for updating the full QR factorization; see Section 3.3.2. Adding a row in the QR factorization can also be performed similarly by a series of plane rotations.

We now describe an algorithm for a general rank-one update. Given $A = Q _ { 1 } R$ ，with orthonormal $Q _ { 1 } \in \mathbb { R } ^ { m \times n }$ ， we seek the compact QR factorization of the modified matrix $\widetilde { A } =$ $A + v u ^ { T }$ , where $v \in \mathbb { R } ^ { m }$ ,and $u \in \mathbb { R } ^ { n }$ . We then have

$$
\widetilde { A } = \left( Q _ { 1 } \quad v \right) \left( \begin{array} { c } { { R } } \\ { { u ^ { T } } } \end{array} \right) .
$$

The first step is to make $v$ orthogonal to $Q _ { 1 }$ using Gram-Schmidt and,if necessary,reorthogonalization. This produces vectors $r$ and a unit vector $q$ ， $\| q \| _ { 2 } = 1$ ,such that

$$
v = Q _ { 1 } r + \rho q , \quad Q _ { 1 } ^ { T } q = 0 .
$$

We then have

$$
\widetilde { A } = \left( Q _ { 1 } \quad q \right) \left[ \left( { R } \atop 0 \right) + \left( { r \atop \rho } \right) u ^ { T } \right] .
$$

The remaining step uses a sequence of plane rotations as in the algorithm for modifying the full QR factorization. With one reorthogonalization this rank-one update algorithm requires approximately $2 0 m n + 6 n ^ { 2 }$ flops.

A similar algorithm is used for downdating the compact QR factorization when the first row $z ^ { T }$ is deleted. Let $q _ { 1 } ^ { T } = e _ { 1 } ^ { T } Q _ { 1 }$ be the first row in $Q _ { 1 }$ . Then we have

$$
A = \left( \begin{array} { l } { { z ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right) = \left( \begin{array} { l } { { q _ { 1 } ^ { T } } } \\ { { \hat { Q } _ { 1 } } } \end{array} \right) R ,
$$

and appending the column $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T }$ to $Q _ { 1 }$ gives

$$
\left( \begin{array} { c } { { z ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right) = \left( \begin{array} { c c } { { q _ { 1 } ^ { T } } } & { { 1 } } \\ { { \hat { Q } _ { 1 } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) .
$$

We now use the Gram-Schmidt process—if necessary with reorthogonalization—to orthogonalize $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T }$ to $Q _ { 1 }$ . With $Q _ { 1 } ^ { T } Q _ { 1 } = I _ { n }$ , this gives

$$
v = e _ { 1 } - Q _ { 1 } ( Q _ { 1 } ^ { T } e _ { 1 } ) = e _ { 1 } - Q _ { 1 } q _ { 1 } .
$$

If $\| v \| _ { 2 } < 1 / \sqrt { 2 }$ ，then $v$ is reorthogonalized; otherwise, $v$ is accepted. Because of the special form of $e _ { 1 }$ , the result has the form

$$
\left( \begin{array} { c c } { q _ { 1 } ^ { T } } & { 1 } \\ { \hat { Q } _ { 1 } } & { 0 } \end{array} \right) = \left( \begin{array} { c c } { q _ { 1 } ^ { T } } & { \gamma } \\ { \hat { Q } _ { 1 } } & { h } \end{array} \right) \left( \begin{array} { c c } { I _ { n } } & { q _ { 1 } } \\ { 0 } & { \gamma } \end{array} \right) , \quad \left( \begin{array} { c } { \gamma } \\ { h } \end{array} \right) = v / \| v \| _ { 2 } .
$$

Using (3.3.46) gives

$$
\left( \begin{array} { c } { { z ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right) = \left( \begin{array} { c c } { { q _ { 1 } ^ { T } } } & { { \gamma } } \\ { { \hat { Q } _ { 1 } } } & { { h } } \end{array} \right) \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) .
$$

Next, a sequence of plane rotations $G _ { k , n + 1 }$ ， $k = n , n - 1 , \ldots , 1 .$ , is determined such that

$$
\begin{array} { r l } { \left( \begin{array} { l l } { q _ { 1 } ^ { T } } & { \gamma } \\ { \hat { Q } _ { 1 } } & { h } \end{array} \right) G = \left( \begin{array} { l l } { 0 } & { \tau } \\ { \widetilde { Q } _ { 1 } } & { \widetilde { h } } \end{array} \right) , } & { \quad G = G _ { n , n + 1 } \cdot \cdot \cdot G _ { 1 , n + 1 } . } \end{array}
$$

Since orthogonal transformations preserve length, we must have $| \tau | = 1$ Because the transformed matrix also must have orthonormal columns, it follows that $\widetilde { h } = 0$ in (3.3.49), and

$$
\left( \begin{array} { c } { { z ^ { T } } } \\ { { \widetilde { A } } } \end{array} \right) = \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { \widetilde { Q } _ { 1 } } } & { { 0 } } \end{array} \right) G ^ { T } \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) ,
$$

$G ^ { T } = G _ { 1 , n + 1 } ^ { T } \cdot \cdot \cdot G _ { n , n + 1 } ^ { T }$ This gives

$$
\left( \begin{array} { c } { \boldsymbol { z } ^ { T } } \\ { \widetilde { \boldsymbol { A } } } \end{array} \right) = \left( \begin{array} { c c } { \boldsymbol { 0 } } & { \boldsymbol { 1 } } \\ { \widetilde { \boldsymbol { Q } } _ { 1 } } & { \boldsymbol { 0 } } \end{array} \right) \left( \begin{array} { c } { \widetilde { \boldsymbol { R } } } \\ { \boldsymbol { w } ^ { T } } \end{array} \right) ,
$$

where $\widetilde { R }$ is upper triangular. Thus $w ^ { T } = z ^ { T }$ ,and the downdated QR factorization is $\widetilde { A } = \widetilde { Q } _ { 1 } \widetilde { R }$ With one reorthogonalization, this downdating algorithm requires about $7 m n + 2 . 5 n ^ { 2 }$ flops. The storage requirement is about $m n + 0 . 5 n ^ { 2 }$ for $Q _ { 1 }$ and $R$

In the above downdating algorithm the orthonormality of $Q _ { 1 }$ plays a decisive role.A more accurate downdating algorithm calld Householder Gram-Schmidt downdating (HGSD) for MGS has been devised by Yoo and Park [1140,1996]. This makes use of the numerical equivalence of MGS and Householder QR applied to $A$ augmented with an $n \times n$ zero matrix on top； see Section 2.2.6. Let $A = Q _ { 1 } R$ ， $Q _ { 1 } = ( q _ { 1 } , \dots , q _ { n } )$ be the computed MGS QR factorization. This is equivalent to the Householder QR decomposition

$$
{ \binom { 0 _ { n \times n } } { A } } = P \left( { \begin{array} { c } { R } \\ { 0 } \end{array} } \right) , \quad P = P _ { 1 } \cdot \cdot \cdot P _ { n } ,
$$

where

$$
P _ { k } = I - u _ { k } u _ { k } ^ { T } , \quad u _ { k } = \left( { \begin{array} { c } { - e _ { k } } \\ { q _ { k } } \end{array} } \right) .
$$

The equivalence is true also numerically. The matrix $P$ is orthogonal by construction and fully determined by $Q _ { 1 }$ and the strictly upper triangular matrix $P _ { 1 1 } \in \mathbb { R } ^ { n \times n }$ ，

$$
P = \left( { \begin{array} { c c } { P _ { 1 1 } } & { P _ { 1 2 } } \\ { P _ { 2 1 } } & { P _ { 2 2 } } \end{array} } \right) = \left( { \begin{array} { c c } { P _ { 1 1 } } & { ( I - P _ { 1 1 } ) { \bar { Q } } _ { 1 } ^ { T } } \\ { { \bar { Q } } _ { 1 } ( I - P _ { 1 1 } ) } & { I - { \bar { Q } } _ { 1 } ( I - P _ { 1 1 } ) { \bar { Q } } _ { 1 } ^ { T } } \end{array} } \right) .
$$

In particular, it can be shown that (see Theorem 2.2.12)

$$
\begin{array} { r l } & { P _ { 2 1 } = ( q _ { 1 } , M _ { 1 } q _ { 2 } , \ldots , M _ { 1 } \cdot \cdot \cdot M _ { n - 1 } q _ { n } ) \in \mathbb { R } ^ { m \times n } , } \\ & { P _ { 2 2 } = M _ { 1 } M _ { 2 } \cdot \cdot \cdot M _ { n } \in \mathbb { R } ^ { m \times m } , } \end{array}
$$

where $M _ { i } = I - q _ { i } q _ { i } ^ { T }$ . Yoo and Park note that downdating the MGS QR decomposition when the first row in $A$ is deleted is equivalent to downdating the corresponding Householder decomposition (3.3.51) when row $( n + 1 )$ is deleted.This can be done stably provided the $( n + 1 ) \mathrm { t h }$ row in $P$ is available. The HGSD algorithm starts by using (3.3.55) to recover the first row $g ^ { T }$ of $P _ { 2 2 }$ ：

$$
g = e _ { 1 } ^ { T } { \cal P } _ { 2 1 } = ( ( e _ { 1 } ^ { T } M _ { 1 } ) M _ { 2 } ) \cdot \cdot \cdot M _ { n } .
$$

This gives the recursion $g ^ { T } = e _ { 1 } ^ { T }$ $g ^ { T } = g ^ { T } - ( g ^ { T } q _ { k } ) q _ { k } ^ { T }$ ， $k = 1 , \ldots , n$ .Next, a Householder reflection $H$ such that $g ^ { T } H = ( \| g \| _ { 2 } , 0 , \ldots , 0 )$ is determined,and the firstcolumn $v$ of $P _ { 2 2 } H$ is computed from

$$
v = P _ { 2 2 } H e _ { 1 } = ( M _ { 1 } \cdot \cdot \cdot ( M _ { n } ( H e _ { 1 } ) ) ) ,
$$

giving the recursion $\boldsymbol { v } = H \boldsymbol { e } _ { 1 }$ ， $v = v - q _ { k } ( q _ { k } ^ { T } v )$ ， $k = n , n - 1 , \ldots , 1$ . These steps replace the steps for orthogonalization of $e _ { 1 }$ to $Q _ { 1 }$ in the previous algorithm and yield $\gamma ~ = ~ v _ { 1 }$ and $h = ( v _ { 2 } , \ldots , v _ { m } )$ . The first row $f$ of $P _ { 2 1 }$ could be recovered similarly from (3.3.54), but it is much cheaper to use

$$
e _ { n + 1 } ^ { T } P = ( ( ( e _ { n + 1 } ^ { T } P _ { 1 } ) P _ { 2 } ) \cdot \cdot \cdot P _ { n } ) ,
$$

where $\boldsymbol { e } _ { n + 1 } \in \mathbb { R } ^ { ( n + m ) }$ is a unit vector with one in its $( n + 1 ) \mathrm { t h }$ position. This leads to the recursion $f = e _ { n + 1 }$ ， $f ^ { T } = f ^ { T } - ( f ^ { T } u _ { k } ) u _ { k }$ ， $k = 1 , \dots , n$ ,where $u _ { k }$ is given by (3.3.52).

The remaining steps of the algorithm are similar to the steps (3.3.49)-(3.3.50) in the previous Gram-Schmidt downdating algorithm. An orthogonal matrix $G$ is determined as a product of plane rotations so that

$$
\left( \begin{array} { c c } { { f ^ { T } } } & { { \gamma } } \\ { { 0 } } & { { \hat { Q } _ { 1 } } } \end{array} \right) G = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \widetilde { Q } _ { 1 } } } \end{array} \right) .
$$

Finally, the upper triangular matrix $R$ is modified:

$$
G ^ { T } \left( { 0 \atop 0 } \right) = \left( { z \atop \widetilde { R } } \right) .
$$

A complete pseudocode of this Householder-MGS downdating algorithm is given by Yoo and Park [1140,1996]. The HGSD algorithm uses 4mn flops for computing $g$ and $v$ in (3.3.56) and (3.3.57). The total arithmetic work is approximately $2 0 m n + 4 n ^ { 2 }$ flops.

# Notes and references

Barlow, Smoktunowicz,and Erbay [77, 2oo5l develop a new family of more robust Gram-Schmidt downdating algorithms and give new bounds on the loss of orthogonality after downdating. They show that the HGSD algorithm of Yoo and Park can be obtained as a special case of this family and corresponds to taking two MGS steps, where the second goes through the columns in reverse order. Examples are given where the proposed new algorithms have a dramatic impact upon the accuracy of the downdated factorization. Barlow and Smoktunowicz [76, 2o13l give a block downdating algorithm using classical GS with reorthogonalization. Block Gram-Schmidt downdating is further studied by Barlow in [69,2014] and [70, 2019].

# 3.3.6 - Modifying URV Decompositions

Treating rank-deficient least squares problems requires a rank-revealing decomposition such as the SVD or URV decomposition. The high cost of updating the SVD (see Section 7.2.4) makes rank-revealing URV decompositions attractive. These have the form

$$
\boldsymbol { A } = \boldsymbol { U } \left( \begin{array} { l l } { \boldsymbol { R } } & { \boldsymbol { F } } \\ { \boldsymbol { 0 } } & { \boldsymbol { G } } \end{array} \right) \boldsymbol { V } ^ { T } ,
$$

where $U$ and $V$ are orthogonal and $R \in \mathbb { R } ^ { k \times k }$ ， $G \in \mathbb { R } ^ { ( m - k ) \times ( n - k ) }$ are upper triangular. Let $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { n }$ be the singular values of $A$ ,and assume that for some $k < n$ it holds that $\sigma _ { k } \gg \sigma _ { k + 1 } \le \delta$ ,where $\delta$ is a given tolerance. Then the numerical $\delta$ -rank of $A$ equals $k$ Also,if

$$
\sigma _ { k } ( R ) \geq \frac { 1 } { c } \sigma _ { k } , \qquad \left( \| F \| _ { F } ^ { 2 } + \| G \| _ { F } ^ { 2 } \right) ^ { 1 / 2 } \leq c \sigma _ { k + 1 }
$$

for some constant $c$ ,the decomposition (3.3.59) exhibits the rank and nullspace of $A$ .The URV decomposition can be updated in $O ( n ^ { 2 } )$ operations when a row is added to $A$ .Following the algorithm given by Stewart [1025,1992], we write

$$
\left( \begin{array} { c c } { { U ^ { T } } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c } { { A } } \\ { { w ^ { T } } } \end{array} \right) V = \left( \begin{array} { c c } { { R } } & { { F } } \\ { { 0 } } & { { G } } \\ { { x ^ { T } } } & { { y ^ { T } } } \end{array} \right) ,
$$

where $w ^ { T } V = ( x ^ { T } y ^ { T } )$ and $( \| F \| _ { F } ^ { 2 } + \| G \| _ { F } ^ { 2 } ) ^ { 1 / 2 } = \nu \leq \delta$ In thesimplestcase theinequality

$$
\sqrt { \nu ^ { 2 } + \| y \| _ { 2 } ^ { 2 } } \leq \delta
$$

is satisfied. Then it suffices to reduce the matrix in (3.3.6O) to upper triangular form by a sequence of left plane rotations.Note that the updated matrix $R$ cannot become effectively rank-deficient because its singular values cannot decrease.

If (3.3.61) is not satisfied, we first reduce $y ^ { T }$ in (3.3.60) so that it becomes proportional to $e _ { 1 } ^ { T }$ , while keeping the upper triangular form of $G$ . This can be done by a sequence of right and left plane rotations as illustrated below. (Note that here the $f$ 's represent entire columns of $F$ ）

$$
{ \begin{array} { c c c } { { ( \begin{array} { c c c c } { { } } & { { } } & { { \downarrow } } & { { \downarrow } } \\ { { } } & { { \begin{array} { c c c c } { { } } & { { } } & { { f } } & { { f } } \\ { { g } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { + } } & { { g } } \\ { { y } } & { { y } } & { { y } } & { { 0 } } \end{array} ) } } & { { \Rightarrow } } & { { ( \begin{array} { c c c c } { { f } } & { { f } } & { { f } } & { { f } } \\ { { g } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { \oplus } } & { { g } } \\ { { y } } & { { y } } & { { y } } & { { 0 } } \end{array} ) } } \end{array} } } \quad { \Rightarrow } } &  { ( \begin{array} { c c c c } { { f } } & { { f } } & { { f } } & { { f } } \\ { { g } } & { { f } } & { { f } } & { { f } } \\ { { 0 } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { + } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { g } } \\ { { y } } & { { y } } & { { 0 } } & { { 0 } } \end{array} ) } \quad \Rightarrow \quad  ( \begin{array} { c c c c } { { f } } & { { f } } & { { f } } & { { f } } \\ { { f } } & { { f } } & { { f } } & { { f } } \\ { { g } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { g } } & { { g } } & { { g } } \\ { { 0 } } & { { + } } & { { g } } & { { g } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { g } } \\   \end{array} \end{array}
$$

$$
\begin{array}{c} \begin{array} { r l } { \to \left( \begin{array} { c c c c } { f } & { f } & { f } & { f } \\ { g } & { g } & { g } & { g } \\ { 0 } & { g } & { g } & { g } \\ { 0 } & { \oplus } & { g } & { g } \\ { 0 } & { 0 } & { 0 } & { g } \\ { y } & { y } & { 0 } & { 0 } \end{array} \right) } & { \Rightarrow } & { \left( \begin{array} { c c c c } { f } & { f } & { f } & { f } \\ { g } & { g } & { g } & { g } \\ { + } & { g } & { g } & { g } \\ { 0 } & { \oplus } & { g } & { g } \\ { 0 } & { 0 } & { 0 } & { g } \\ { \sigma } & { 0 } & { 0 } & { 0 } \end{array} \right) } \end{array} \ \Rightarrow \ \ \to \left( \begin{array} { c c c c } { f } & { f } & { f } & { f } \\ { g } & { g } & { g } & { g } \\ { \oplus } & { g } & { g } & { g } \\ { 0 } & { 0 } & { 0 } & { g } \\ { 0 } & { 0 } & { g } & { g } \\ { \sigma } & { 0 } & { 0 } & { 0 } \end{array} \right) .  \end{array}
$$

In this part of the reduction, $R$ and $x ^ { T }$ are not involved. The system now has the form

$$
\left( \begin{array} { c c c } { { R } } & { { f } } & { { \tilde { F } } } \\ { { 0 } } & { { g } } & { { \tilde { G } } } \\ { { x ^ { T } } } & { { \sigma } } & { { 0 } } \end{array} \right) .
$$

This matrix is now reduced to triangular form using plane rotations from the left, and $k$ is increased by 1. Finally, the new $R$ is checked for degeneracy and possibly reduced by deflation. The complete update takes $O ( n ^ { 2 } )$ flops.

Stewart [1027,1993l has pointed out that although the decomposition (3.3.59) is very satisfactory for recursive least squares problems, it is less suited for applications where an approximate nullspace is to be recursively updated. Let $U = \left( U _ { 1 } \quad U _ { 2 } \right)$ and $V ~ = ~ ( ~ V _ { 1 } ~ V _ { 2 } )$ be

partitioned conformally with (3.3.59). Then we have

$$
\| A V _ { 2 } \| _ { 2 } = \left\| \left( { \begin{array} { c } { F } \\ { < G } \end{array} } \right) \right\| _ { 2 } .
$$

Hence the orthogonal matrix $V _ { 2 }$ can be taken as an approximation to the numerical nullspace $\mathcal { N } _ { k }$ On the other hand, we have $\| U _ { 2 } ^ { T } A \| _ { 2 } = \| G \| _ { 2 }$ ,and therefore the last $n - k$ singular values of $A$ are less than or equal to $\| G \| _ { 2 }$

Because $F$ is involved in the bound (3.3.62), $V _ { 2 }$ is not the best available approximate nulspace. This problem can be resolved by working instead with the corresponding rank-revealing ULV decomposition

$$
\boldsymbol { A } = \boldsymbol { U } \left( \begin{array} { l l } { \boldsymbol { L } } & { \boldsymbol { 0 } } \\ { \boldsymbol { H } } & { \boldsymbol { E } } \end{array} \right) \boldsymbol { V } ^ { T } ,
$$

where $L$ and $E$ have lower triangular form, and

$$
\sigma _ { k } ( L ) \geq { \frac { 1 } { c } } \sigma _ { k } , \qquad \left( \| H \| _ { F } ^ { 2 } + \| E \| _ { F } ^ { 2 } \right) ^ { 1 / 2 } = \nu \leq \delta .
$$

For this decomposition, $\| A V _ { 2 } \| _ { 2 } = \| E \| _ { F }$ ,where $V = \left( V _ { 1 } , V _ { 2 } \right)$ is a conformal partitioning of $V$ . Hence the size of $\| H \| _ { 2 }$ does not affect the nullspace approximation.

Stewart [1027,1993] has presented an updating scheme for the decomposition (3.3.63). With $w ^ { T } V = \left( x ^ { T } \quad y ^ { T } \right)$ ,the problem reduces to updating

$$
\left( \begin{array} { c c } { { L } } & { { 0 } } \\ { { H } } & { { E } } \\ { { x ^ { T } } } & { { y ^ { T } } } \end{array} \right) .
$$

We first reduce $y ^ { T }$ to $\lVert y \rVert _ { 2 } e _ { 1 } ^ { T }$ by right rotations while keeping the lower triangular form of $E$ At the end of this reduction the matrix will have the form

$$
\left[ \begin{array} { l l l l l } { l } & { 0 } & { 0 } & { 0 } & { 0 } \\ { l } & { l } & { 0 } & { 0 } & { 0 } \\ { l } & { l } & { l } & { 0 } & { 0 } \\ { h } & { h } & { h } & { e } & { 0 } \\ { h } & { h } & { h } & { e } & { e } \\ { x } & { x } & { x } & { y } & { 0 } \end{array} \right] .
$$

This last row is annihilated by a sequence of left rotations, and $k$ is increased by 1. (For the case above we would use $Q = G _ { 1 6 } G _ { 2 6 } G _ { 3 6 } G _ { 4 6 } .$ ）If there has been no effective increase in rank,a deflation process has to be applied. If (3.3.61) is satisfied,the rank cannot increase. Then the reduction is performed,but the first rotation $G _ { 4 6 }$ is skipped.This gives us a matrix of the form

$$
\left[ \begin{array} { l l l l l } { l } & { 0 } & { 0 } & { y } & { 0 } \\ { l } & { l } & { 0 } & { y } & { 0 } \\ { l } & { l } & { l } & { y } & { 0 } \\ { h } & { h } & { h } & { e } & { 0 } \\ { h } & { h } & { h } & { e } & { e } \\ { 0 } & { 0 } & { 0 } & { y } & { 0 } \end{array} \right] .
$$

The $y$ elements above the main diagonal can be eliminated using right rotations. This fills out the last row again,but with elements the same size as $y$ . Now the last row can be reduced by the procedure described above without destroying the rank-revealing structure; see again Stewart [1027, 1993].The main difference compared to the scheme for updating the URV decomposition is that there is not the same simplification when (3.3.61) is satisfied.

A complication with the above updating algorithm is that when $m \gg n$ , the extra storage for $U \in \mathbb { R } ^ { m \times m }$ may be prohibitive. If only $V$ and the triangular factor are stored,then we must use methods like the Saunders algorithm, possibly stabilized with the CSNE method. Alternatively, hyperbolic rotations may be used; see Section 7.2.4. Such methods will not be as satisfactory as methods using $Q$ or Gram-Schmidt-based methods using $Q _ { 1 }$ ; see Sections 3.3.2 and 3.3.5.

# Notes and references

Downdating algorithms for rank-revealing URV decompositions are also treated by Park and Eldén [880,1995l and Barlow, Yoon, and Zha [79,1996]. MATLAB templates for computing RRQR and UTV decompositions are given by Fierro,P. C. Hansen,and P. S.K. Hansen [408, 1999l and Fierro and Hansen [4O7,2oo5]. Algorithms for modifying and maintaining ULV decompositions are given in Barlow [67,2oo3], Barlow and Erbay[72,2oog],and Barlow,Erbay, and Slapnicar [73, 2O05]. Stewart and Van Dooren [1034,2Ooo] give updating schemes for quotient-type generalized URV decomposition. Methods for computing and updating product and quotient ULV decompositions are developed by Simonsson [999, 2006].

# 3.4 -Equality Constrained Problems

# 3.4.1 - Method of Direct Elimination

In least squares problems the solution is often subject to linear equality constraints.

# Problem LSE

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad B x = d ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ ， $B \in \mathbb { R } ^ { p \times n }$ ， $p \leq n$ ， $m + p \geq n$ . Such problems arise when models require some equations to be satisfied exactly. Applications include constrained optimization, surface fitting, signal processing,and various geodetic problems. Least squares problems with inequality constraints can often be reduced to solving a sequence of LSE problems; see Section 3.4. In beam-forming or spatial filtering the LSE problem has to be solved for fixed $A$ and many different $B$ matrices.

Assuming that the constraints $B x = d$ are consistent, problem LSE has a unique solution if and only if

$$
\operatorname { r a n k } \left( { A \atop B } \right) = n .
$$

This condition is equivalent to $\mathcal { N } ( A ) \cap \mathcal { N } ( B ) = \{ 0 \}$ ,i.e.,the nullspaces of $A$ and $B$ only intersect trivially. If this is not true,there is a vector $z \neq 0$ such that $A z = B z = 0$ Hence if $x$ solves (3.4.1), then $x + \alpha z$ is a different solution.The solution to problem LSE satisfies the augmented system

$$
\left( \begin{array} { c c c } { { 0 } } & { { 0 } } & { { B } } \\ { { 0 } } & { { I _ { m - p } } } & { { A } } \\ { { B ^ { T } } } & { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { \lambda } } \\ { { r } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { d } } \\ { { b } } \\ { { 0 } } \end{array} \right) ,
$$

where $\lambda$ are Lagrange multipliers for the constraint $B x = d$

A robust algorithm for problem LSE should check for a possible inconsistency in the constraints if $\operatorname { r a n k } ( B ) < p$ .If the constraints are inconsistent, problem LSE can be reformulated as a sequential least squares problem,

$$
\operatorname* { m i n } _ { x \in S } \| A x - b \| _ { 2 } , \qquad S = \{ x \mid \| B x - d \| _ { 2 } = \operatorname* { m i n } \} .
$$

This problem always has a unique solution of least-norm. Most of the methods described in the following for solving problem LSE can, with small modifications, be adapted to solve (3.4.4).

A natural way to solve problem LSE is to derive an equivalent unconstrained least squares problem of lower dimension. There are two different ways to perform this reduction: by direct elimination or by using the nullspace method. The method of direct elimination starts by reducing the matrix $B$ to upper trapezoidal form. It is essential that column pivoting be used in this step. To solve the more general problem (3.4.4) a QR factorization of $B$ with column pivoting can be used:

$$
Q _ { B } ^ { T } B \Pi _ { B } = \left( { \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { 0 } \end{array} } \right)  \} r = r = \operatorname { r a n k } ( B ) \leq p ,
$$

where $Q _ { B } \in \mathbb { R } ^ { p \times p }$ is orthogonal, $R _ { 1 1 }$ is upper triangular and nonsingular, and $\Pi _ { B }$ is a permutation matrix. With $\bar { x } = \Pi _ { B } ^ { T } x$ the constraints become

$$
\left( R _ { 1 1 } \quad R _ { 1 2 } \right) \bar { x } = \bar { d } _ { 1 } , \qquad \bar { d } = Q _ { B } ^ { T } d = \left( \frac { \bar { d } _ { 1 } } { \bar { d } _ { 2 } } \right) ,
$$

where $\bar { d } _ { 2 } = 0$ if the constraints are consistent. Applying the permutation $\Pi _ { B }$ to the columns of $A$ and partitioning the resulting matrix conformally with (3.4.5) gives

$$
A x = \bar { A } \bar { x } = ( \bar { A } _ { 1 } \quad \bar { A } _ { 2 } ) \left( \begin{array} { c } { { \bar { x } _ { 1 } } } \\ { { \bar { x } _ { 2 } } } \end{array} \right) ,
$$

where ${ \bar { A } } = A \Pi _ { B }$ . If (3.4.6) is used to eliminate $\bar { x } _ { 1 } = R _ { 1 1 } ^ { - 1 } ( \bar { d } _ { 1 } - R _ { 1 2 } \bar { x } _ { 2 } )$ from (3.4.7), we obtain $A x - b = \widehat { A } _ { 2 } \bar { x } _ { 2 } - \widehat { b }$ ,where

$$
\widehat { A } _ { 2 } = \bar { A } _ { 2 } - \bar { A } _ { 1 } R _ { 1 1 } ^ { - 1 } R _ { 1 2 } , \qquad \widehat { b } = b - \bar { A } _ { 1 } R _ { 1 1 } ^ { - 1 } \bar { d } _ { 1 } .
$$

This reduction can be interpreted as performing $r$ steps of Gaussian elimination on the system

$$
\left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { \bar { A } _ { 1 } } } & { { \bar { A } _ { 2 } } } \end{array} \right) \left( \begin{array} { c } { { \bar { x } _ { 1 } } } \\ { { \bar { x } _ { 2 } } } \end{array} \right) = \left( \begin{array} { c } { { \bar { d } _ { 1 } } } \\ { { b } } \end{array} \right) .
$$

Then $\bar { x } _ { 2 }$ is determined by solving the reduced unconstrained least squares problem

$$
\operatorname* { m i n } _ { \bar { \boldsymbol { x } } _ { 2 } } \| \widehat { A } _ { 2 } \bar { \boldsymbol { x } } _ { 2 } - \widehat { \boldsymbol { b } } \| _ { 2 } , \qquad \widehat { A } _ { 2 } \in \mathbb { R } ^ { m \times ( n - r ) } .
$$

We now show that if (3.4.2) holds,then $\mathrm { r a n k } ( \widehat { A } _ { 2 } ) = n - r$ ,and (3.4.9) has a unique solution. For if $\mathrm { r a n k } ( \widehat { A } _ { 2 } ) < n - r$ , there is a vector $v \neq 0$ such that

$$
\begin{array} { r } { \widehat { A } _ { 2 } v = \bar { A } _ { 2 } v - \bar { A } _ { 1 } R _ { 1 1 } ^ { - 1 } R _ { 1 2 } v = 0 . } \end{array}
$$

If we let $u = - R _ { 1 1 } ^ { - 1 } R _ { 1 2 } v$ then $R _ { 1 1 } u + R _ { 1 2 } v = 0$ and $\bar { A } _ { 1 } u + \bar { A } _ { 2 } v = 0$ Hence ${ \boldsymbol { w } } = \Pi _ { B } \left( { \boldsymbol { \mathscr { u } } } \right) \neq$ O is a null vector to both $B$ and $A$ . But this contradicts the assumption (3.4.2).

The solution to (3.4.9) can be obtained from the QR factorization

$$
\begin{array} { r } { Q _ { A } ^ { T } \widehat { A } _ { 2 } = \left( \begin{array} { c } { R _ { 2 2 } } \\ { 0 } \end{array} \right) , \qquad Q _ { A } ^ { T } \widehat { b } = \left( \begin{array} { c } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right) , } \end{array}
$$

where $R _ { 2 2 } \in \mathbb { R } ^ { ( n - r ) \times ( n - r ) }$ is upper triangular and nonsingular. Then $\bar { x }$ is obtained from the triangular system

$$
\left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) \bar { x } = \left( \begin{array} { c } { { \bar { d } _ { 1 } } } \\ { { c _ { 1 } } } \end{array} \right) ,
$$

and $x = \Pi _ { B } \bar { x }$ solves problem LSE.The coding of the direct elimination algorithm can be kept remarkably compact, as shown by the ALGOL program for Householder QR in Bjorck and Golub [143, $\mathbf { 1 9 6 7 } ]$ . Cox and Higham [271,1999] obtain a similar stable elimination method by taking the analytic limit of the weighted least squares problem

$$
\operatorname* { m i n } _ { x } \left\| \left( { \omega { \cal B } } \atop { \cal A } \right) x - \left( { \omega { \cal d } \atop { \cal b } } \right) \right\| _ { 2 } ^ { 2 }
$$

when $\omega$ tends to infinity and by rescaling the rows.

The set of vectors $x \ = \ \Pi _ { B } \bar { x }$ ，where $\bar { x }$ satisfies (3.4.6), is exactly the set of vectors that minimize $\| B x - d \| _ { 2 }$ . Thus,the algorithm outlined above solves the more general problem (3.4.4).If condition (3.4.2) is not satisfied, the reduced problem (3.4.9) does not have a unique solution. Then column permutations are needed also in the QR factorization of $\widehat { A } _ { 2 }$ .In this case we can compute either a least-norm solution or a basic solution to (3.4.4).

# 3.4.2 - The Nullspace Method

In the nullspace method for solving problem LSE,an orthogonal basis for the nullspace of the constraint matrix $B$ is used. Cox and Higham [274,1999] note that three different versions of this method are known. The first (used in LAPACK) is based on the generalized QR factorization of $A$ and $B$ ; see Section 3.1.5.This is slightly less efficient than the method described by Lawson and Hanson [727,1995] and Golub and Van Loan [512,1996].Here we describe yet another method, which has the lowest computational cost of the three versions. It starts by computing the QR factorization of $B ^ { T }$ or, equivalently,

$$
B Q _ { B } = \left( L _ { B } \quad 0 \right) ,
$$

where $L _ { B } \in \mathbb { R } ^ { p \times p }$ is lower triangular and $Q _ { B } = \left( \begin{array} { l l } { Q _ { 1 } } & { Q _ { 2 } } \end{array} \right) \in \mathbb { R } ^ { n \times n }$ ,with

$$
Q _ { 1 } \in \mathbb { R } ^ { n \times p } , \qquad Q _ { 2 } \in \mathbb { R } ^ { n \times ( n - p ) } .
$$

Here $Q _ { 2 }$ gives an orthogonal basis for the nullspace of $B$ ,i.e., $\mathcal { N } ( B ) = \mathcal { R } ( Q _ { 2 } )$ If $\operatorname { r a n k } ( B ) = p$ ， then $L _ { B }$ is nonsingular. Then any vector $x \in \mathbb { R } ^ { n }$ such that $B x \ = \ d$ can be represented as $x = x _ { 1 } + Q _ { 2 } y _ { 2 }$ , where

$$
x _ { 1 } = B ^ { \dagger } d , \quad B ^ { \dagger } = Q _ { 1 } L _ { B } ^ { - 1 } d ,
$$

and $y _ { 2 } \in \mathbb { R } ^ { ( n - p ) }$ is arbitrary. It remains to solve the reduced least squares problem

$$
\operatorname* { m i n } _ { y _ { 2 } } \| ( A Q _ { 2 } ) y _ { 2 } - ( b - A x _ { 1 } ) \| _ { 2 } .
$$

Let $y _ { 2 } = ( A Q _ { 2 } ) ^ { \dagger } ( b - A x _ { 1 } )$ be the minimum-length solution to (3.4.13). Since $x _ { 1 } \perp Q _ { 2 } y _ { 2 }$ ,it follows that $\| x \| _ { 2 } ^ { 2 } = \| x _ { 1 } \| _ { 2 } ^ { 2 } + \| Q _ { 2 } y _ { 2 } \| _ { 2 } ^ { 2 } = \| x _ { 1 } \| _ { 2 } ^ { 2 } + \| y _ { 2 } \| _ { 2 } ^ { 2 }$ .Hence, $x$ is the least-norm solution to problem LSE.From (3.4.12) it follows that $x$ can be expressed as

$$
\begin{array} { r l } & { x = B ^ { \dagger } d + Q _ { 2 } ( A Q _ { 2 } ) ^ { \dagger } ( b - A B ^ { \dagger } d ) } \\ & { \quad = ( I - Q _ { 2 } ( A Q _ { 2 } ) ^ { \dagger } A ) B ^ { \dagger } d + Q _ { 2 } ( A Q _ { 2 } ) ^ { \dagger } b . } \end{array}
$$

Assuming that $\mathcal { N } ( A ) \cap \mathcal { N } ( B ) = \{ 0 \}$ ,we have

$$
C = \left( { \begin{array} { c } { B } \\ { A } \end{array} } \right) Q _ { B } = \left( { \begin{array} { c c } { L _ { B } } & { 0 } \\ { A Q _ { 1 } } & { A Q _ { 2 } } \end{array} } \right) ,
$$

and $C$ must have rank $n$ . Hence $\mathrm { r a n k } ( A Q _ { 2 } ) = n - p$ ,and the QR factorization

$$
Q _ { A } ^ { T } ( A Q _ { 2 } ) = \binom { R _ { A } } { 0 }
$$

exists with $R _ { A }$ upper triangular and nonsingular. It follows that the unique solution to problem LSE is $x = x _ { 1 } + Q _ { 2 } y _ { 2 }$ ,where

$$
R _ { A } y _ { 2 } = c _ { 1 } , \quad c = { \binom { c _ { 1 } } { c _ { 2 } } } = Q _ { A } ^ { T } ( b - A x _ { 1 } ) .
$$

The method of direct elimination and all three nullspace methods are numerically stable and should give almost identical results. The method of direct elimination, which uses Gaussian elimination to derive the reduced unconstrained system, has the lowest operation count.

When $A$ is large and sparse,the nullspace method has the drawback that fill-in can be ex-pected when forming the matrix $A Q _ { 2 }$ .When $\operatorname { r a n k } ( B ) = p$ ,and $B \Pi = \left( B _ { 1 } B _ { 2 } \right)$ with $B _ { 1 }$ square and nonsingular, the nullspace matrix

$$
Z = \Pi \left( \begin{array} { c } { { - B _ { 1 } ^ { - 1 } B _ { 2 } } } \\ { { I } } \end{array} \right)
$$

satisfies $B Z = 0$ . In the reduced gradient method, $Z$ is used to solve problem LSE. This is both an elimination method and a nulspace method. The reduced gradient method is potentially more effcient because it can work with a sparse LU factorization of $B _ { 1 }$

# 3.4.3 - Perturbation Theory

A perturbation theory for problem LSE using representation (3.4.14) is given by Leringe and Wedin [734,197o], generalizing results given in Section 1.3.4. Their bounds show that problem LSE is well-conditioned if $\kappa ( B )$ and $\kappa ( A Q _ { 2 } )$ are small. Note that these two condition numbers can be small even when $\kappa ( A )$ is large. Gulliksson and Wedin [552,2ooo] use the augmented system(3.4.3) to obtain perturbation bounds and condition numbers for rank-deficient, weighted, and constrained problems.

A more complete perturbation theory for problem LSE is given by Eldén [368,198o], [369, $\mathbf { 1 9 8 2 } ]$ . This is based on a generalized pseudoinverse related to the least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { L } \quad S = \{ x \mid \| A x - b \| _ { M } { \mathrm { i s } } { \mathrm { m i n i m u m } } \} ,
$$

where $\| \cdot \| _ { L }$ and $\| \cdot \| _ { M }$ are the elliptic seminorms,

$$
\| x \| _ { L } ^ { 2 } = x ^ { H } L ^ { H } L x , \qquad \| y \| _ { M } ^ { 2 } = y ^ { H } M ^ { H } M y ,
$$

for some matrices $L$ and $M$ that are allowed to be rectangular.

Theorem 3.4.1. The solution of problem (3.4.16) can be written $x = A _ { M L } ^ { \dagger } b$ where

$$
A _ { M L } ^ { \dagger } = ( I - ( L P ) ^ { \dagger } L ) ( M A ) ^ { \dagger } M b , \quad P = I - ( M A ) ^ { \dagger } M A .
$$

Here $A _ { M L } ^ { \dagger } b$ is the ML-weighted pseudoinverse of $A$ . The solution is unique if and only if

$$
{ \mathcal { N } } ( M A ) \cap { \mathcal { N } } ( L ) = \{ 0 \} .
$$

Proof. See Elden [369,1982,Theorem 2.1]and Mitra and Rao [798,1974l.

$B _ { I A } ^ { \dagger }$

Theorem 3.4.2. If the constraints are consistent, the least-norm solution of problem LSE is given by

$$
x = B _ { I A } ^ { \dag } d + ( A P ) ^ { \dag } b , \quad P = I - L ^ { \dag } L .
$$

Proof. See Eldén [369,1982, Theorem 3.1].

# 3.4.4 - The Method of Weighting

In the method of weighting for solving problem LSE,the constraints are multiplied by a large weight $w \gg 1$ and appended at the top of the weighted LS problem,

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { c } { w B } \\ { A } \end{array} } \right) x - \left( { \begin{array} { c } { w d } \\ { b } \end{array} } \right) \right\| _ { 2 } ^ { 2 } ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ ， $B \in \mathbb { R } ^ { p \times n }$ .If $w$ is sufficiently large,the residual $B x - d$ becomes negligible, and the solution $x ( w )$ is a good approximation to the LSE solution $x _ { L S E }$ . This allows standard subroutines for unconstrained least squares problems to be used. This is particularly attractive when $A$ and $B$ are sparse. However, a large weight may be required to give acceptable accuracy even when the LSE problem is well-conditioned.

Van Loan [1081, $\mathbf { 1 9 8 5 } ]$ gives a method that allows a moderately large weight $w$ to be used. First, compute a solution $x ( w )$ to (3.4.21) from the QR factorization

$$
\left( \begin{array} { c c } { { w B } } & { { w d } } \\ { { A } } & { { b } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { c _ { 1 } } } \\ { { 0 } } & { { c _ { 2 } } } \end{array} \right) .
$$

Next,applythefoowingiterativerefiement schme: Set $x ^ { ( 1 ) } = x ( w )$ , and for $k = 1 , 2 , \ldots$

1. s(k)=d-Bx(k). 2 3. $x ^ { ( k + 1 ) } = x ^ { ( k ) } + \Delta x ^ { ( k ) } .$

No further QR factorization is needed to compute the corrections. The vectors $x ^ { ( k ) }$ generated can be shown to converge to $x _ { L S E }$ with linear rate equal to $\rho _ { w } = w _ { p } ^ { 2 } / ( w _ { p } ^ { 2 } + w ^ { 2 } )$ ,where $w _ { p }$ is the largest generalized singular value of $( A , B )$ . With the default value $w = \mathbf { u } ^ { - 1 / 2 }$ the method converges quickly unless the problem is ill-conditioned.

The method of weighting can be analyzed using the GSVD. In the following we assume that $\operatorname { r a n k } ( B ) = p$ and rank $\begin{array} { r l } { \left( A ^ { T } } & { { } B ^ { T } \right) = n } \end{array}$ , which ensures that the weighted problem (3.4.21) has a unique solution. By Theorem 3.1.5 the GSVD of $\{ A , B \}$ can be written

$$
A = U \left( \begin{array} { c } { { \Sigma _ { A } } } \\ { { 0 } } \end{array} \right) Z , ~ B = V ( \Sigma _ { B } 0 ) Z ,
$$

where $U$ and $V$ are orthogonal, $Z$ is nonsingular, and

$$
\Sigma _ { A } = \mathrm { d i a g } \left( \alpha _ { 1 } , \ldots , \alpha _ { n } \right) > 0 , \qquad \Sigma _ { B } = \mathrm { d i a g } \left( \beta _ { 1 } , \ldots , \beta _ { p } \right) > 0 .
$$

The generalized singular values of $\{ A , B \}$ are $\alpha _ { i } = 1$ ， $i > p$ ,and $\sigma _ { i } = \alpha _ { i } / \beta _ { i }$ . From (3.4.23) the normal equations $( A ^ { T } A + w ^ { 2 } B ^ { T } B ) x = A ^ { T } b + w ^ { 2 } B ^ { T } d$ are transformed into diagonal form,

$$
\left( \Sigma _ { A } ^ { 2 } + w ^ { 2 } \left( \begin{array} { c c } { { \Sigma _ { B } ^ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \right) y = \left( \Sigma _ { A } \quad 0 \right) c + w ^ { 2 } \left( \begin{array} { c } { { \Sigma _ { B } } } \\ { { 0 } } \end{array} \right) e ,
$$

where $Z x = y , c = U ^ { T } b , f = V ^ { T } d .$ It follows that

$$
y _ { i } = \left\{ \begin{array} { l l } { \frac { \alpha _ { i } c _ { i } + w ^ { 2 } \beta _ { i } e _ { i } } { \alpha _ { i } ^ { 2 } + w ^ { 2 } \beta _ { i } ^ { 2 } } , } & { i = 1 , \ldots , p , } \\ { c _ { i } , } & { i = p + 1 , \ldots , n . } \end{array} \right.
$$

Problem LSE is transformed into

$$
\operatorname* { m i n } _ { y } \left\| \left( { \begin{array} { c } { \Sigma _ { A } } \\ { 0 } \end{array} } \right) y - c \right\| _ { 2 } ^ { 2 } { \mathrm { s u b j e c t t o } } \left( \Sigma _ { B } \ 0 \right) y = f
$$

with solution $x _ { L S E } = Z ^ { - 1 } y$ ,where

$$
y _ { i } = \left\{ { \begin{array} { l l } { f _ { i } / \beta _ { i } , } & { i = 1 , \ldots , p , } \\ { c _ { i } , } & { i = p + 1 , \ldots , n . } \end{array} } \right.
$$

From (3.4.25) and (3.4.27) it follows that $\begin{array} { r } { \operatorname* { l i m } _ { w \to \infty } x ( w ) = x _ { L S E } } \end{array}$

The residual for the constraints is $s = V ^ { T } ( d - B x ) = f - \left( \Sigma _ { B } \quad 0 \right) y$ . From (3.4.25), we obtain

$$
s _ { i } = f _ { i } - \beta _ { i } \frac { \alpha _ { i } c _ { i } + w ^ { 2 } \beta _ { i } f _ { i } } { \alpha _ { i } ^ { 2 } + w ^ { 2 } \beta _ { i } ^ { 2 } } = \alpha _ { i } \frac { \alpha _ { i } f _ { i } - \beta _ { i } c _ { i } } { \alpha _ { i } ^ { 2 } + w ^ { 2 } \beta _ { i } ^ { 2 } } , \quad i = 1 , \dots , p .
$$

For large values of $w$ , we have $s _ { i } \approx \sigma _ { i } ( \sigma _ { i } f _ { i } - c _ { i } ) / w ^ { 2 }$ .Hence the residual norm $\| d - B x ( w ) \| _ { 2 }$ is proportional to $w ^ { - 2 }$ . We conclude that the criterion for choosing $w$ should have the form w > cu-1/2.

# Notes and references

Several methods for solving problem LSE are described by Lawson and Hanson [727,1995l; a detailed analysis of the method of weighting for LSE is given in Section 22. Wedin [1110, $\mathrm { 1 9 8 5 } ]$ gives perturbation bounds for LSE based on the augmented system formulation. Cox and Higham [274,1999l analyze the accuracy and stability of three different nullspace methods for problem LSE, give a perturbation theory,and derive practical error bounds. Rank-deficient LSE problems are studied by Wei [1113,1992]. An MGS algorithm for weighted and constrained problems is presented by Gulliksson [550,1995l. Barlow and Handy [74,1988] compare the method of weighting to that in Bjorck [126,1968]. Reid [921,2ooo] surveys the use of implicit scaling for linear least squares problems. Barlow and Vemulapati [78,1992] give a slightly modified improvement scheme for the weighting method.

# 3.5 - Inequality Constrained Problems

# 3.5.1 - Classification of Problems

Often, the solution $x \in \mathbb { R } ^ { n }$ of a least squares problem is subject to a set of linear inequality constraints $c _ { i } ^ { T } x \leq d _ { i }$ ， $i = 1 , \ldots , p$ ,and has the following form:

# Problem LSI

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad C x \leq d .
$$

Here $C \in \mathbb { R } ^ { p \times n }$ is a matrix with ith row $c _ { i } ^ { T }$ ,and the inequalities are to be interpreted componentwise.A solution to problem LSI exists only if the set of points satisfying $C x \leq d$ is not empty. Problem LSI is equivalent to the quadratic programming problem

$$
\operatorname* { m i n } _ { x } { \frac { 1 } { 2 } } x ^ { T } B x + c ^ { T } x \quad { \mathrm { s u b j e c t ~ t o } } \quad C x \leq d
$$

with $B = A ^ { T } A$ ， $c = - A ^ { T } b$ . This arises as a subproblem in general nonlinear programming algorithms and has been studied extensively. Algorithms for quadratic programming that form $B = A ^ { T } A$ explicitly should be avoided if possible.

If $A$ has full column rank, then problem LSI is a strictly convex optimization problem,and if the constraints are feasible,there is a unique solution. In this case, problem LSI is known to be solvable in polynomial time.The Lagrangian for problem LSI is

$$
L ( x , y ) = \| A x - b \| _ { 2 } ^ { 2 } + y ^ { T } ( C x - d ) ,
$$

where $y \in \mathbb { R } ^ { m }$ is the vector of Lagrange multipliers.The first-order optimality conditions are given by the Karush-Kuhn-Tucker (KKT) conditions.

Theorem 3.5.1 (Karush-Kuhn-Tucker). Let $x ^ { * }$ be a local minimizer of problem LSI (3.5.1) and assume that the Jacobian of the active constraints at $x ^ { * }$ has full rank. Then there exists Lagrange multipliers $y ^ { * }$ that satisfy $\nabla _ { x } L ( x , y ) = 0$ ， $C x - d \geq 0$ at $x = x ^ { * }$ ，and the KKT complementarity condition holds:

$$
y ^ { T } ( C x - d ) = 0 , \quad y \geq 0 .
$$

From the nonnegativity of $C x - d$ and $y$ it follows that either $y _ { i } = 0$ or the ith constraint is binding: $c _ { i } ^ { T } x - d = 0$ The vector y in the KKT conditions is called the dual solution.

An important special case of LSI is when the constraints are upper and lower bounds.

# Problem BLS

$$
\operatorname* { m i n } _ { x } \left\| A x - b \right\| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad l \leq x \leq u .
$$

This is an LSI problem with $C = ( I _ { n } , - I _ { n } ) ^ { T }$ ， $d = ( u , - l ) ^ { T }$ . Bound-constrained least squares (BLS) problems arise in many practical applications, e.g., reconstruction problems in geodesy and tomography,contact problems for mechanical systems,and modeling of ocean circulation. It can be argued that the linear model is only realistic when the variables are constrained within meaningful intervals.For computational eficiency it is essential that such constraints be considered separately from more general constraints,such as those in (3.5.1).

If only one-sided bounds on $x$ are specified in BLS,it is no restriction to assume that these are nonnegativity constraints. Then we have a linear nonnegative least squares problem.

# Problem NNLS

$$
\operatorname* { m i n } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad x \geq 0 .
$$

This problem arises when $x$ represents quantities such as amounts of material, chemical concentrations,and pixel intensities.Applications include geodesy, tomography,and contact problems for mechanical systems.The KKT conditions to be satisfied at an optimal NNLS solution are

$$
y = A ^ { T } ( A x - b ) , \quad x ^ { T } y = 0 , \quad x \geq 0 , \quad y \geq 0 ,
$$

where $y$ is the gradient of $\frac { 1 } { 2 } \| A x - b \| _ { 2 } ^ { 2 }$ .This is also known as a (monotone) linear complementarity problem (LCP).LSI appears to be a more general problem than NNLS, but this is not the case. Hanson and Haskell[588,1982] give a number of ways any LSI problem can be transformed into the form of NNLS.

If $A$ is rank-deficient, there may be an infinite manifold $M$ of optimal solutions with a unique global optimum. Then we can seek the unique solution of least norm that satisfies $\operatorname* { m i n } \| x \| _ { 2 }$ ， $x \in M$ . This can be formulated as a least distance problem.

# Problem LSD

$$
\operatorname* { m i n } _ { x } \| x \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad g \leq G x .
$$

The solution to problem LSD can be obtained by an appropriate normalization of the residual in a related NNLS problem. The following result is shown by Lawson and Hanson [727, 1995, Chap. 23].

Theorem 3.5.2. Let $u \in \mathbb { R } ^ { m + 1 }$ solve the NNLS problem

$$
\operatorname* { m i n } _ { u } \| E u - f \| _ { 2 } \quad s u b j e c t t o \quad u \geq 0 ,
$$

where

$$
E = \binom { G ^ { T } } { g ^ { T } } , \qquad f = \binom { 0 } { 1 } \frac  \} \mathrm { \large { J } } n .
$$

Let $r = ( r _ { 1 } , \ldots , r _ { n + 1 } ) ^ { T } = f - E u$ be the residual corresponding to the NNLS solution, and set $\sigma = \| r \| _ { 2 }$ f $\sigma \neq 0$ ,then the unique solution to problem LSD is

$$
\begin{array} { r } { x = ( x _ { 1 } , \ldots , x _ { n } ) ^ { T } , \qquad x _ { j } = r _ { j } / r _ { n + 1 } , \quad j = 1 , \ldots , n . } \end{array}
$$

f $\sigma = 0$ ,the constraints $g \leq G x$ are inconsistent, and problem LSD has no solution.

Two-step algorithms for solving the more general LSD problem,

$$
\operatorname* { m i n } _ { x } \| x _ { 1 } \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad g \leq G x ,
$$

where $x = \left( x _ { 1 } , x _ { 2 } \right) ^ { T }$ ,are given by A. K. Cline [254,1975], Haskell and Hanson [594,1981], and Hanson [587,1986]. Each step requires the solution of a problem of type NNLS,with the first step having additional linear equality constraints.

Haskell and Hanson [594,198i] implement two subprograms, LSEI and WNNLS, for solv-ing linearly constrained least squares problems with equality constraints (LSEI). This is more general than problem LSI in that some of the equations in $A x = b$ are to be satisfied exactly. A user's guide to the two subroutines LSEI and WNNLS is given in Haskell and Hanson [593, 1979]. WNNLS is based on solving a differentially weighted least squares problem. A penalty function minimization that is implemented in a numerically stable way is used.

Gradient projection methods and interior methods for problem NNLS are treated in Sections 8.3.1 and 8.3.2,respectively. General nonlinear optimization software can also be used to solve nonlinear least squares problems with inequality constraints; see,e.g., Schittkowski [970, $\mathrm { 1 9 8 5 } ]$ and Mahdavi-Amiri [768,1981].

# 3.5.2 - Active-Set Methods

Methods for solving problems with linear inequality constraints are,in general, iterative in nature.A point $x$ is called a feasible point if it satisfies all constraints $C x \leq d$ in (3.5.1). The constraints that are satisfied with equality at a feasible point are called active. In an active-set algorithm a working set of constraints is defined to be a linearly independent subset of the active set at the current approximation. In each iteration the value of the objective function is decreased, and the optimum is reached in finitely many steps (assuming the constraints are independent).

A first useful step in solving problem LSI (3.5.1) is to transform $A$ to upper triangular form. With standard column pivoting, a rank-revealing QR factorization

$$
\begin{array} { r } { Q ^ { T } A P = R = \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \frac { \ d } { \ d t } } \end{array}
$$

is computed with $R _ { 1 1 }$ upper triangular and nonsingular. The numerical rank $r$ of $A$ is determined using some specified tolerance,as discussed in Section 1.3.3.After the last $( m - r )$ rows in $R$ and $c$ are deleted, the objective function in (3.5.1) becomes

$$
\| \big ( R _ { 1 1 } , R _ { 1 2 } \big ) x - c _ { 1 } \| _ { 2 } , \quad c = \binom { c _ { 1 } } { c _ { 2 } } = Q ^ { T } b .
$$

By further orthogonal transformations from the right in (3.5.12),a complete orthogonal decomposition

$$
Q ^ { T } A P V = \left( \begin{array} { l l } { { T } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \Sigma ^ { r } _ { m - r }
$$

is obtained, where $T$ is upper triangular and nonsingular. With $x = P V y$ ,problem LSI (3.5 is then equivalent to

$$
\operatorname* { m i n } _ { y _ { 1 } } \| T y _ { 1 } - c _ { 1 } \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad E y \leq d ,
$$

where $E = C P V$ ， $y = { \binom { y _ { 1 } } { y _ { 2 } } }$ ,and $y _ { 1 } \in \mathbb { R } ^ { r }$

In general, a feasible point from which to start the algorithm is not known. An exception is the case when all constraints are simple bounds,as in BLS and NNLS.In a first phase of an active-set algorithm,a feasible point is determined by minimizing the sum of infeasibilities $\sum c _ { i } ^ { T } x - d _ { i }$ among violated constraints.

Let $x _ { k }$ be a feasible point that satisfies the working set of $n _ { k }$ linearly independent constraints with associated matrix $C _ { k }$ . The constraints in the working set are temporarily treated as equality constraints. An optimum solution to the corresponding problem exists because the least squares objective is bounded below. To solve this we take

$$
x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k } ,
$$

where $p _ { k }$ is a search direction and $\alpha _ { k }$ a nonnegative step length. The search direction is chosen so that $C _ { k } p _ { k } = 0$ ,which will cause the constraints in the working set to remain satisfied for all values of $\alpha _ { k }$ . If moving toward the solution encounters an inactive constraint, this constraint is added to the active set, and the process is repeated.

To satisfy the condition $C _ { k } p _ { k } = 0$ , a decomposition

$$
C _ { k } Q _ { k } = \left( 0 \quad T _ { k } \right) , \quad T _ { k } \in \mathbb { R } ^ { n _ { k } \times n _ { k } } ,
$$

is computed, where $T _ { k }$ is triangular and nonsingular, and $Q _ { k }$ is a product of orthogonal transformations. (This is essentially the QR factorization of $C _ { k } ^ { T }$ )If $Q _ { k }$ is partitioned conformally,

$$
Q _ { k } = ( \underbrace { Z _ { k } } _ { n - n _ { k } } \underbrace { Y _ { k } } _ { n _ { k } } ) ,
$$

the $n - n _ { k }$ columns of $Z _ { k }$ form a basis for the nullspace of $C _ { k }$ . The condition $C _ { k } p _ { k } = 0$ is satisfied if we take $p _ { k } = Z _ { k } q _ { k }$ ， $q _ { k } \in \mathbb { R } ^ { n - n _ { k } }$ . Now $q _ { k }$ is determined so that $x _ { k } + Z _ { k } q _ { k }$ minimizes the objective function. Hence $q _ { k }$ solves the unconstrained least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { q } _ { k } } \| A \boldsymbol { Z } _ { k } \boldsymbol { q } _ { k } - \boldsymbol { r } _ { k } \| _ { 2 } , \qquad \boldsymbol { r } _ { k } = \boldsymbol { b } - A \boldsymbol { x } _ { k } .
$$

To simplify the discussion we assume $A Z _ { k }$ has full rank, so that (3.5.15) has a unique solution. To compute this solution we need the QR factorization of $A Z _ { k }$ . This is obtained from the QR factorization of $A Q _ { k }$ , where

$$
P _ { k } ^ { T } A Q _ { k } = P _ { k } ^ { T } ( A Z _ { k } A Y _ { k } ) = \left( \begin{array} { c c } { { R _ { k } } } & { { S _ { k } } } \\ { { 0 } } & { { U _ { k } } } \\ { { 0 } } & { { 0 } } \end{array} \right) \} n _ { k } .
$$

Computing this larger decomposition has the advantage that the orthogonal matrix $P _ { k }$ need not be saved and can be discarded after being applied also to the residual vector $r _ { k }$ . The solution $q _ { k }$ to (3.5.15) can now be computed from

$$
R _ { k } q _ { k } = c _ { k } , \qquad P _ { k } ^ { T } r _ { k } = \left( { c _ { k } \atop d _ { k } } \right) \left. \right\} n - n _ { k }  .
$$

Denote by $\bar { \alpha }$ the maximum nonnegative step along $p _ { k }$ for which $x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k }$ remains feasible with respect to the constraints not in the working set. If $\bar { \alpha } \leq 1$ ,then we take $\alpha _ { k } = \bar { \alpha }$ and add the constraint that determines $\bar { \alpha }$ to the working set for the next iteration. If $\bar { \alpha } > 1$ ,then we set $\alpha _ { k } = 1$ . In this case, $x _ { k + 1 }$ will minimize the objective function when the constraints in the working set are treated as equalities,and the orthogonal projection of the gradient onto the subspace of feasible directions will be zero:

$$
\begin{array} { r } { Z _ { k } ^ { T } g _ { k + 1 } = 0 , \quad g _ { k + 1 } = - A ^ { T } r _ { k + 1 } . } \end{array}
$$

In this case we check the optimality of $x _ { k + 1 }$ by computing Lagrange multipliers for the constraints in the working set. At $x _ { k + 1 }$ these are defined by the equation

$$
C _ { k } ^ { T } \lambda = g _ { k + 1 } = - A ^ { T } r _ { k + 1 } .
$$

The residual vector $r _ { k + 1 }$ for the new unconstrained problem satisfies

$$
P _ { k } ^ { T } r _ { k + 1 } = { \binom { 0 } { d _ { k } } } .
$$

Hence, multiplying (3.5.17) by $Q _ { k } ^ { T }$ and using (3.5.13), we obtain

$$
Q _ { k } ^ { T } C _ { k } ^ { T } \lambda = \left( { 0 \atop T _ { k } ^ { T } } \right) \lambda = - Q _ { k } ^ { T } A ^ { T } P _ { k } \left( { 0 \atop d _ { k } } \right) ,
$$

so from (3.5.16),

$$
T _ { k } ^ { T } \lambda = - \left( U _ { k } ^ { T } \quad 0 \right) d _ { k } .
$$

The Lagrange multiplier $\lambda _ { i }$ for the constraint $c _ { i } ^ { T } x \geq d _ { i }$ in the working set is said to be optimal if $\lambda _ { i } \geq 0$ . If all multipliers are optimal, an optimal point has been found. Otherwise, the objective function can be decreased if we delete the corresponding constraint from the working set. When more than one multiplier is not optimal, it is normal to delete the constraint whose multiplier deviates the most from optimality.

At each iteration, the working set of constraints is changed, which leads to a change in $C _ { k }$ If a constraint is dropped, the corresponding row in $C _ { k }$ is deleted; if a constraint is added, a new row is introduced in $C _ { k }$ . An important feature of an active-set algorithm is efficient solution of the sequence of unconstrained problems (3.5.15). Techniques described in Section 7.2 can be used to update the matrix decompositions (3.5.13) and (3.5.16). In (3.5.13), $Q _ { k }$ is modified by a sequence of orthogonal transformations from the right. Factorization (3.5.16) and the vector $P _ { k } ^ { T } r _ { k + 1 }$ are updated accordingly.

If $x _ { k + 1 } = x _ { k }$ ,Lagrange multipliers are computed to determine if an improvement is possible by moving away from one of the active constraints (by deleting it from the working set). In each iteration,the value of the objective function is decreased until the KKT conditions are satisfied.

Active-set algorithms usually restrict the change in dimension of the working set by dropping or adding only one constraint at each iteration. For large-scale problems this implies many iterations when the set of active constraints at the starting point is far from the working set at the optimal point. Hence,unless a good approximation to the final set of active constraints is known, an active-set algorithm willrequire many iterations to converge.

In the rank-deficient case it can happen that the matrix $A Z _ { k }$ in (3.5.15) is rank-deficient, and hence $R _ { k }$ is singular. Note that if some $R _ { k }$ is nonsingular, it can only become singular during later iterations when a constraint is deleted from the working set. In this case only its last diagonal element can become zero. This simplifies the treatment of the rank-deficient case. To make the initial $R _ { k }$ nonsingular one can add artificial constraints to ensure that the matrix $A Z _ { k }$ has full rank.

A possible further complication is that the working set of constraints can become linearly dependent. This can cause possible cycling in the algorithm, so that its convergence cannot be ensured. A simple remedy that is often used is to enlarge the feasible region of the offending constraint by a small quantity.

If $A$ has full column rank,the active-set algorithm for problem LSI described here is essentially identical to an algorithm given by Stoer[1039,1971]. LSSOL by Gill et al. [473,1986] is a set of Fortran subroutines for solving a class of convex quadratic programming that includes LSI. It handles rank-deficiency in $A$ ,a combination of simple bounds,and general linear constraints. It allows for a linear term in the objective function and uses a two-phase active-set method. The minimizations in both phases are performed by the same subroutines.

For problems BLS and NNLS,active-set methods simplify. We outline an active-set algorithm for problem BLS in its upper triangular form

$$
\operatorname* { m i n } _ { x } \| R x - c \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } l \leq x \leq u .
$$

Divide the index set of $x$ according to $\{ 1 , 2 , \ldots , n \} = { \mathcal { F } } \cup { \mathcal { B } }$ ，where $i \in \mathcal { F }$ if $x _ { i }$ is a free variable, and $i \in \mathcal { B }$ if $x _ { i }$ is fixed at its lower or upper bound. We assume $\mathcal { F }$ and $\boldsymbol { B }$ are ordered sets with indices in increasing order. To this partitioning corresponds a permutation matrix $P =$ $\left( E _ { \mathcal { F } } , E _ { B } \right)$ ，where $E _ { \mathcal { F } }$ and $E _ { B }$ consist of the columns $e _ { i }$ of the unit matrix for which $i \in \mathcal { F }$ and $\textit { i } \in \textit { B }$ ，respectively. Choose an initial solution $x ^ { ( 0 ) }$ satisfying $l < x ^ { ( 0 ) } < u$ ，and take $\mathcal { F } _ { 0 } = \{ 1 , 2 , \dots , n \}$ ， $R _ { B _ { 0 } } = \varnothing$ ，so that $R _ { \mathcal { F } _ { 0 } } = R$ .(The reason, as will become apparent, is that it is cheaper and more stable to fix a free variable than the opposite operation.） Let $x ^ { ( k ) }$ be the iterate at the $k$ thstep $( k = 0 , 1 , \ldots )$ and write

$$
\begin{array} { r } { x _ { \mathcal { F } _ { k } } ^ { ( k ) } = E _ { \mathcal { F } _ { k } } ^ { T } x ^ { ( k ) } , \qquad x _ { \mathcal { B } _ { k } } ^ { ( k ) } = E _ { \mathcal { B } _ { k } } ^ { T } x ^ { ( k ) } } \end{array}
$$

for the free and fixed parts of the solution. The unconstrained problem (3.5.18) with variables $x _ { B _ { k } } ^ { ( k ) }$ fixed becomes

$$
\operatorname* { m i n } _ { { x } _ { \mathcal { F } _ { k } } } \| R _ { \mathcal { F } _ { k } } { x } _ { \mathcal { F } _ { k } } - c _ { k } \| _ { 2 } , \qquad c _ { k } = c - R _ { \mathcal { B } _ { k } } { x } _ { \mathcal { B } _ { k } } ^ { ( k ) } ,
$$

where $R P _ { k } = \left( R E _ { \mathcal { F } _ { k } } , R E _ { \mathcal { B } _ { k } } \right) = \left( R _ { \mathcal { F } _ { k } } , R _ { \mathcal { B } _ { k } } \right)$ . To simplify the discussion we assume $R _ { \mathcal { F } _ { k } }$ has full column rank,so that (3.5.2O) has a unique solution. This is always the case if $\operatorname { r a n k } ( A ) = n$

To solve (3.5.20) we need the QR factorization of $R _ { \mathcal { F } _ { k } }$ . We obtain this by considering the first block of columns of the QR factorization,

$$
\begin{array} { r } { Q _ { k } ^ { T } ( R _ { \mathcal { F } _ { k } } , R _ { \mathcal { B } _ { k } } ) = \left( \begin{array} { c c } { U _ { k } } & { S _ { k } } \\ { 0 } & { V _ { k } } \end{array} \right) , \qquad Q _ { k } ^ { T } c = \left( \begin{array} { c } { d _ { k } } \\ { e _ { k } } \end{array} \right) . } \end{array}
$$

The solution to (3.5.20)is givenby Ux $U _ { k } x _ { \mathcal { F } _ { k } } ^ { ( k ) } = d _ { k } - S _ { k } x _ { B _ { k } } ^ { ( k ) }$ , and we take

$$
\boldsymbol { x } ^ { ( k + 1 ) } = \boldsymbol { x } ^ { ( k ) } + \alpha ( \boldsymbol { z } ^ { ( k ) } - \boldsymbol { x } ^ { ( k ) } ) ,
$$

where z(k）= EFxχ $z ^ { ( k ) } = E _ { \mathcal { F } _ { k } } x _ { \mathcal { F } _ { k } } ^ { ( k ) } + E _ { B _ { k } } x _ { B _ { k } } ^ { ( k ) }$ and $\alpha$ is a nonnegative step length. (Note that, assuming $\operatorname { r a n k } ( R ) = n$ , $z ^ { ( 0 ) }$ is just the solution to the unconstrained problem.)

Let $\bar { \alpha }$ be the maximum value of $\alpha$ for which $x ^ { ( k + 1 ) }$ remains feasible. There are now two possibilities:

· If $\bar { \alpha } < 1$ ,then $z ^ { ( k ) }$ is not feasible. We take $\alpha = \bar { \alpha }$ and move al indices $q \in \mathcal { F } _ { k }$ for which   
x(+1）=lqorufroFtoB.Tustefreevariablesthathittheirowrpper bounds will be fixed for the next iteration step.   
·If $\bar { \alpha } \geq 1$ , we take $\alpha = \bar { \alpha }$ Then $x ^ { ( k + 1 ) } = z ^ { ( k ) }$ is the unconstrained minimum when the variables $x _ { B _ { k } }$ are kept fixed. The Lagrange multipliers are checked to see if the objective function can be decreased further by freeing one of the fixed variables. If not, we have found the global minimum.

At each iteration, the sets $\mathcal { F } _ { k }$ and $\boldsymbol { B } _ { k }$ change. If a constraint is dropped, a column from $R _ { B _ { k } }$ is moved to $R _ { \mathcal { F } _ { k } }$ ； if a constraint is added,a column is moved from $R _ { \mathcal { F } _ { k } }$ to $R _ { B _ { k } }$ . Solution of the sequence of unconstrained problems (3.5.2O) and computation of the corresponding Lagrange multipliers can be efficiently achieved, provided the QR factorization (3.5.21) can be updated.

In a similar active-set algorithm for problem NNLS,the index set of $x$ is divided as $\{ 1 , 2 , \dots , n \} = { \mathcal { F } } \cup B$ ，where $i \in \mathcal { F }$ if $x _ { i }$ is a free variable and $i \in \boldsymbol { B }$ if $x _ { i }$ is fixed at zero. $C _ { k }$ now consists of the rows $e _ { i } , i \in B$ ，of the unit matrix $I _ { n }$ . We let $C _ { k } = E _ { B } ^ { T }$ ,and if $E _ { \mathcal { F } }$ is similarly defined, then $P _ { k } = ( E _ { \mathcal { F } } ~ E _ { B } )$ ， $T _ { k } = I _ { n _ { k } }$ . Since $P _ { k }$ is a permutation matrix, the product

$$
A P _ { k } = ( A E _ { \mathcal { F } } A E _ { \mathcal { B } } ) = ( A _ { \mathcal { F } } A _ { \mathcal { B } } )
$$

corresponds to a permutation of the columns of $A$

To drop the bound corresponding to $x _ { q }$ , we take $A P _ { k + 1 } = A P _ { k } P _ { R } ( k , q )$ , where the permutation matrix $P _ { R } ( k , q ) , q > k + 1$ , performs a right circular shift of the columns

$$
k + 1 , \ldots , q - 1 , q \quad \Rightarrow \quad q , k + 1 , \ldots , q - 1 .
$$

Similarly，to add the bound corresponding to $x _ { q }$ to the working set we take $A Q _ { k + 1 } ~ =$ $A Q _ { k } P _ { L } ( q , k )$ , where $P _ { L } ( q , k )$ ， $q < k - 1$ , is a permutation matrix that performs a left circular shift of the columns

$$
q , q + 1 , \ldots , k \quad \Rightarrow \quad q + 1 , \ldots , k , q .
$$

Equation (3.5.17) for the Lagrange multipliers simplifies for NNLS to $\lambda = - E _ { B } ^ { T } A ^ { T } r _ { k + 1 } .$ where $- A ^ { T } r _ { k + 1 }$ is the gradient vector. As an initial feasible point we take $x = 0$ and set ${ \mathcal { F } } = \emptyset$

The least squares subproblems need not be solved from scratch. Instead, the QR factorization

$$
P ^ { T } A ( E _ { \mathcal { F } } , E _ { \mathcal { B } } ) = \left( \begin{array} { c c } { R } & { S } \\ { 0 } & { U } \end{array} \right) , \qquad P ^ { T } b = \left( \begin{array} { c } { c } \\ { d } \end{array} \right) ,
$$

is updated after a right or left circular shift, using the algorithms described in Section 3.3.2; cf.   
stepwise regression.

The pseudocode below is based on the NNLS algorithm given by Lawson and Hanson [727, 1995,Chapter 23]. The algorithm cannot cycle and terminates after a finite number of steps. However, the number of iterations needed can be large and cannot be estimated a priori.

# Algorithm 3.5.1 (Active-Set Algorithm for NNLS).

Initialization:   
$\begin{array} { l } { { \mathcal { F } = 0 ; \quad \mathcal { B } = \{ 1 , 2 , . . . , n \} ; } } \\ { { \quad x = 0 ; \quad w = A ^ { T } b ; } } \end{array}$   
Main loop:   
while $B \neq \varnothing$ and $\operatorname* { m a x } _ { i } w _ { i } \geq 0$ ， $p = \mathrm { a r g m a x } _ { i \in B } w _ { i } ;$ Move index $p$ from $\boldsymbol { B }$ to $\mathcal { F }$ , i.e., fre variable $x _ { p }$ ； Let $z$ solve $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ subject to $x _ { B } = 0$ ； while $\operatorname* { m i n } _ { i } z _ { i } \leq 0 \ \forall i \in \mathcal { F }$ ； Let $\alpha _ { i } = x _ { i } / ( x _ { i } - z _ { i } ) \ \forall i \in \mathcal { F }$ such that $z _ { i } < 0$ ； Find index $q$ such that $\alpha _ { q } = \operatorname* { m i n } _ { i \in \mathcal { F } } \alpha _ { i }$ $x = x + \alpha _ { q } ( z - x )$ ； Move all indices $q$ for which $x _ { q } = 0$ from $\mathcal { F }$ to $\boldsymbol { B }$ Let $x$ solve $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ subject to $z _ { B } = 0$ ： end $x = z ; \quad w = E _ { B } ^ { T } A ^ { T } ( b - A x ) ;$   
end

NNLS is also available in MATLAB as the function ls qn onneg. Fortran implementations of algorithms for the NNLS and LSD problems are given also in Appendix C in Lawson and Hanson [727,1995].

Perturbation bounds for the linear least squares problem subject to linear inequality con-straints are given by Lotstedt [758,1g83]. For solving a sequence of constrained problems with a slowly changing matrix $A$ ，iterative methods are particularly attractive. Lotstedt [759, 1984l gives an active-set algorithm for solving time-dependent simulation of contact problems in mechanical systems. His algorithm uses preconditioned CG with a preconditioner that is kept constant for several time steps.

# Notes and references

A survey of algorithms for enforcing nonnegativity constraints in scientific least squares computation is given by Chen and Plemmons [239, 2oo7]. The paper also surveys important application in science and engineering. Bro and de Jong [181,1997] modify the standard NNLS algorithm by precomputing some cross-product terms in the normal equations. Their algorithm, called fast NNLS, gives significant speed-up for problems with multiple right-hand sides, and targets applications such as multiway decomposition methods for tensor arrays; see Section 4.3.5. In a recent variant due to Van Benthem and Keenan [1O72, 2oo4], the performance is improved by identifying and grouping together observations at each stage that share a common pseudoinverse.

# 3.5.3 - Quadratically Constrained Least Squares

Least squares problems with a quadratic inequality constraint (LSQI) of the form

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| B x - d \| _ { 2 } \leq \gamma ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ ， $B \in \mathbb { R } ^ { p \times n }$ arise in many applications.For the solution to be unique it is necessary that the nullspaces of $A$ and $B$ intersect trivially, i.e.,

$$
{ \mathcal { N } } ( A ) \cap { \mathcal { N } } ( B ) = \{ 0 \} \ \Leftrightarrow \ \operatorname { r a n k } \left( { A \atop B } \right) = n .
$$

Conditions for existence and uniqueness of solutions to problem LSQI and the related problem LSQE with equality constraint $\| B x - d \| _ { 2 } = \gamma$ are given by Gander [438,1981]. For a solution to (3.5.22) to exist the set $\{ x : \| B x - d \| _ { 2 } \leq \gamma \}$ must not be empty. Furthermore,if $\| B x _ { B } - d \| _ { 2 } <$ $\gamma$ ,where $x _ { B }$ solves

$$
\operatorname* { m i n } _ { x \in S } \| B x - d \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| A x - b \| _ { 2 } = \operatorname* { m i n } \} ,
$$

the constraint is not binding.

Theorem 3.5.3. Assume that the constraint set $\{ x : \| B x - d \| _ { 2 } = \gamma \}$ is not empty. Then the solution to problem LSQE equals the solution $x ( \lambda )$ to the normal equations $( A ^ { T } A + \lambda B ^ { T } B ) x =$ $A ^ { T } b + B ^ { T } d$ or, equivalently, to the least squares problem

$$
\operatorname* { m i n } _ { x } \left\| \left( \overset { A } { \sqrt { \lambda } } _ { B } \right) x - \left( \overset { b } { \sqrt { \lambda } } _ { d } \right) \right\| _ { 2 } ,
$$

where $\lambda \geq 0$ solves the secular equation

$$
f ( \lambda ) = \| B x ( \lambda ) - d \| _ { 2 } - \gamma = 0 .
$$

Proof. By the method of Lagrange multipliers and minimize $\psi ( x , \lambda )$ , where

$$
\psi ( x , \lambda ) = \| A x - b \| _ { 2 } ^ { 2 } + \lambda ( \| B x - d \| _ { 2 } ^ { 2 } - \gamma ^ { 2 } ) .
$$

Only positive values of $\lambda$ are of interest. A necessary condition for a minimum is that the gradient of $\psi ( x , \lambda )$ with respect to $x$ equals zero. For $\lambda \geq 0$ this shows that $x ( \lambda )$ solves (3.5.25). It can be shown that $f ( \lambda )$ is a monotone decreasing function of $\lambda$ . Hence the secular equation has a unique positive solution. □

The standard case of LSQE is obtained by taking $B = I$ and $d = 0$ in (3.5.22):

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| x \| _ { 2 } = \gamma .
$$

Then $x ( \lambda )$ solves the regularized or damped least squares problem

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { c } { A } \\ { { \sqrt { \lambda } } I _ { n } } \end{array} } \right) x - \left( { \begin{array} { c } { b } \\ { 0 } \end{array} } \right) \right\| _ { 2 } ,
$$

where $\lambda > 0$ satisfies the secular equation

$$
f ( \lambda ) = \| x ( \lambda ) \| _ { 2 } - \gamma = 0 .
$$

Damped least squares problems were used by Levenberg [736,1944] in the solution of nonlinear least squares problems.Problem (3.5.28)can be solved by Householder QR factorization; see Golub [487,1965]. The structure of the initial and the transformed matrices after $k = 2$ steps of Householder QR factorization is shown below for $m = n = 4$

$$
\begin{array} { r l r } { \left[ \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & & & { } \\ { \times } & & & { } \\ & { \times } & & { \times } \\ & & & { \times } \end{array} \right] } & { \Longrightarrow } & { \left[ \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } & { \times } \\ { \otimes } & { \otimes } & { \times } & { \times } \\ { \otimes } & { \otimes } & { + } & { + } \\ { \oplus } & { + } & { + } & { + } \\ & & { \times } & { \times } \end{array} \right] } \\ & { } & { \times } & { \left[ \begin{array} { l l l l l } { \phantom { - } } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ { \otimes } & { \otimes } & { \times } & { \times } & { \times } \\ { \otimes } & { \oplus } & { + } & { + } & { \times } \\ & { \oplus } & { + } & { + } & { + } \\ & & & { \times } & { \times } & { \times } \\ & & & & { \times } & { \times } \end{array} \right] } \end{array}
$$

Only the first two rows of $\lambda I$ have filled in. In all steps,precisely $n$ elements in the current column are annihilated. Hence the Householder QR factorization requires $2 m n ^ { 2 }$ flops, which is $2 n ^ { 3 } / 3$ flops more than for the QR factorization of $A$ .A similar increase in arithmetic operations occurs for MGS.

The standard form of problem LSQE can also be formulated as a least squares problem on the unit sphere:

$$
\operatorname* { m i n } _ { \| \boldsymbol { x } \| _ { 2 } = \gamma } \| \boldsymbol { A } \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } .
$$

This is a problem on the Stiefel (or equivalently, Grassman) manifold. Newton-type algorithms for such problems are developed by Edelman,Arias,and Smith [358,1999]. The application of such methods to the regularized least squares problem has been studied by Elden [374, 2002].

# 3.5.4 - Solving Secular Equations

In order to solve the secular equation (3.5.29) numerically, we need to evaluate the function $f ( \lambda )$ and preferably its derivative.This requires the solution of (3.5.28) for a sequence of values of $\lambda$ 、As shown by Reinsch [923,1971], instead of applying Newton's method to (3.5.29), faster convergence can be obtained by applying it to the convex function

$$
g ( \lambda ) = \frac { 1 } { \| x ( \lambda ) \| _ { 2 } } - \frac { 1 } { \gamma } = 0 .
$$

If the initial approximation satisfies $0 < \lambda _ { 0 } < \lambda ^ { * }$ ，where $\lambda ^ { * }$ is the solution, then the iterates $\lambda _ { k }$ can be shown to converge monotonically from below. (In the optimization literature this observation is often credited to Hebden [598,1973l.） The asymptotic rate of convergence for Newton's method is quadratic. If derivatives are difficult to evaluate,the secant method can be used. Provided that the two initial iterates are nonnegative,this also converges monotonically.

The derivative with respect to $\lambda$ of $g ( \lambda )$ in (3.5.31) is

$$
\frac { d g ( \lambda ) } { d \lambda } = - \frac { x ^ { T } ( \lambda ) } { \| x ( \lambda ) \| _ { 2 } ^ { 3 } } \frac { d x ( \lambda ) } { d \lambda } .
$$

From $x ( \lambda ) = C ( \lambda ) ^ { - 1 } A ^ { T } b , C ( \lambda ) = A ^ { T } A + \lambda I ,$ , and the formula for the derivative of an inverse matrix, we obtain

$$
\ b x ( \lambda ) ^ { T } \frac { d \ b x ( \lambda ) } { d \lambda } = - \ b x ( \lambda ) ^ { T } ( \ b A ^ { T } \ b A + \lambda I ) ^ { - 1 } \ b x ( \lambda ) \equiv - \| \ b z ( \lambda ) \| _ { 2 } ^ { 2 } .
$$

Thus Newton's method for solving (3.5.31) becomes

$$
\lambda _ { k + 1 } = \lambda _ { k } + \left( \frac { \| x ( \lambda _ { k } ) \| _ { 2 } } { \gamma } - 1 \right) \frac { \| x ( \lambda _ { k } ) \| _ { 2 } ^ { 2 } } { \| z ( \lambda _ { k } ) \| _ { 2 } ^ { 2 } } .
$$

Each Newton iteration requires the solution of the damped least squares problem (3.5.28) for a new value of $\lambda$ .Hence a new QR decomposition must be computed. These QR factorizations account for the main cost of an iteration.

# Algorithm 3.5.2 (Reinsch's Algorithm).

function $\left[ { \bf x } , { \bf n x } \right] { \bf \Omega } = { \bf \Omega }$ reinsch(A,b,gamma,p)   
$\%$ REINSCH performs $< = \texttt { p }$ iterations to solve   
%min_xllA x - bll_2 subject to $| \mathbf { \partial } | ~ \mathbf { x } ~ | \mathbf { \partial } | \mathbf { \partial } \mathbf { \_ } 2 ~ = ~ \mathrm { g a m m a }$   
%-- [m,n] = size(A); rlam = m\*eps\*norm(A,1); for $\tt { k } = \tt { 1 } { : p }$ $\%$ Compute the compact $\mathbb { Q R }$ . ${ \begin{array} { r l } & { [ \mathbb { Q } , \mathbb { R } ] ~ = ~ \operatorname { \mathfrak { q r } } ( [ \mathbb { A } ; ~ \mathbf { r l a m } * \in \mathbf { y } \in ( \mathrm { n } ) ] , ~ 0 ) ; } \\ & { \mathrm { c ~ = ~ \mathbb { Q } ^ { \gamma } * b }  } \\ & { \mathrm { x ~ = ~ \mathbb { R } \backslash c ; ~ \operatorname { n x } ~ = ~ \operatorname { n o r m } ( x ) ; } } \end{array} }$ if nx $< =$ gamma，break，end $\%$ Perform Newton step. $\mathbf { \Sigma } _ { \mathbf { Z } } ~ = ~ \mathbb { R } ^ { \prime } \setminus \mathbf { x }$ ；nz = norm(z); $\begin{array} { r l } & { \mathrm { \Lambda ~ \sum ~ \omega ~ } = \mathrm { \Lambda } _ { 1 } \mathrm { a } _ { 1 } = \mathrm { \Lambda } _ { 1 } \mathrm { a } _ { 2 } = \mathrm { \Lambda } _ { 2 } \mathrm { a } _ { 1 } \mathrm { a } _ { 2 } = \mathrm { \Lambda } _ { 1 } \mathrm { \Lambda } _ { 2 } \mathrm { \Lambda } _ { 3 } \quad } \\ & { \mathrm { \Lambda } _ { \mathrm { r } 1 } \mathrm { a } _ { \mathrm { m } } = \mathrm { \Lambda } _ { \mathrm { s } } \mathrm { q } _ { \mathrm { r } } \mathrm { t } \left( \mathrm { { 1 } } \mathrm { a } _ { \mathrm { m } } \right) ; } \end{array}$ end   
end

$\left( \begin{array} { c c } { { A } } & { { b } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { c } } \\ { { 0 } } & { { d } } \end{array} \right)$

$$
\operatorname* { m i n } _ { x } \Big \| \left( { \begin{array} { c } { R } \\ { { \sqrt { \lambda } } I _ { n } } \end{array} } \right) x - \left( { c } \atop 0 \right) \Big \| _ { 2 } .
$$

For any fixed value of $\lambda$ this problem can be reduced by a second QR factorization to $\begin{array} { r } { \operatorname* { m i n } _ { x } \| R ( \lambda ) x - c _ { 1 } ( \lambda ) \| _ { 2 } } \end{array}$ . Then $x ( \lambda )$ and $z ( \lambda )$ can be computed from the two triangular systems

$$
R ( \lambda ) x ( \lambda ) = c _ { 1 } ( \lambda ) , \qquad R ( \lambda ) ^ { T } z ( \lambda ) = x ( \lambda ) .
$$

Eldén [367,1977] shows that further savings in the Newton iterations can be obtained by an initial transformation

$$
\begin{array} { r } { U ^ { T } A V = \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) , \qquad U ^ { T } b = \left( \begin{array} { l } { g _ { 1 } } \\ { g _ { 2 } } \end{array} \right) , } \end{array}
$$

where $B$ is upper bidiagonal; see Section 4.2.1. Computing $B$ and $V$ requires $4 m n ^ { 2 }$ flops; see Section 4.2.1. With $x = V y$ ,the least squares problem (3.5.28) is transformed into

$$
\operatorname* { m i n } _ { y } \biggl \| \left( \begin{array} { c } { B } \\ { \sqrt \lambda I _ { n } } \end{array} \right) y - \left( \begin{array} { c } { g _ { 1 } } \\ { 0 } \end{array} \right) \biggr \| _ { 2 } .
$$

To solve this for a given value of $\lambda$ , two sequences of plane rotations,

$$
G _ { k } = R _ { k , n + k } , \quad k = 1 , \ldots , n , \qquad J _ { k } = R _ { n + k , n + k + 1 } , \quad k = 1 , \ldots , n - 1 ,
$$

are determined that transform the matrix in (3.5.35) to upper bidiagonal form $B _ { \lambda }$ ：

$$
G _ { n } J _ { n - 1 } \cdot \cdot \cdot G _ { 2 } J _ { 1 } G _ { 1 } \left( \begin{array} { c c } { { B } } & { { g _ { 1 } } } \\ { { \sqrt \lambda I _ { n } } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { B _ { \lambda } } } & { { z _ { 1 } } } \\ { { 0 } } & { { z _ { 2 } } } \end{array} \right) .
$$

Here $G _ { 1 }$ zeros the element in position $( n + 1 , 1 )$ and creates a new nonzero element in position $( n + 2 , 2 )$ . This is annihilated by a second plane rotation $J _ { 1 }$ that transforms rows $n { \mathrel { + { 1 } } }$ and $n + 2$ All remaining steps proceed similarly. The solution is then obtained as

$$
B _ { \lambda } y ( \lambda ) = z _ { 1 } , \quad x ( \lambda ) = V y ( \lambda ) .
$$

The QR factorization in (3.5.36) and the computation of $y ( \lambda )$ take about $2 3 n$ flops. Eldén [367, 1977l gives a more detailed operation count and also shows how to compute the derivatives used in Newton's method of the equation $f ( \lambda ) = \| y _ { \lambda } \| _ { 2 } - \gamma = 0$

# 3.6 - Regularized Least Squares

# 3.6.1 - Discrete Ill-Posed Linear Systems

In many different branches of physics and engineering one tries to determine, e.g., the structure of a physical system from its behavior. Some important areas are medical imaging, geophysical prospecting,image deblurring,and deconvolution of signals. Such problems are called inverse problems and can often be modeled as a Fredholm integral equation of the first kind,

$$
\int _ { \Omega } k ( s , t ) f ( t ) d t = g ( s ) , \quad s , t \in \Omega ,
$$

where $f$ and $g$ are assumed to be real functions in the Hilbert space $L ^ { 2 } ( \Omega )$ ，and the kernel $k ( \cdot , \cdot ) \in L ^ { 2 } ( \Omega \times \Omega )$ Let $K \in L ^ { 2 } ( \Omega ) \to L ^ { 2 } ( \Omega )$ be a continuous linear operator defined by

$$
K f = \int _ { \Omega } k ( \cdot , t ) f ( t ) d t .
$$

By the Riemann-Lebesgue lemma there are rapidly oscillating functions $f$ that come arbitrarily close to being annihilated by $K$ ．Hence,the inverse of $K$ cannot be a continuous operator. Hence the solution of $f$ does not depend continuously on the data $g$ . Therefore (3.6.1) is called an ill-posed problem, a term introduced by Hadamard.

A compact operator $K$ admits a singular value expansion

$$
\begin{array} { r } { K v _ { i } = \sigma _ { i } u _ { i } , \quad K ^ { T } u _ { i } = \sigma _ { i } v _ { i } , \quad i = 1 , 2 , \ldots , } \end{array}
$$

where the functions $u _ { i }$ and $v _ { i }$ are orthonormal with respect to the inner product

$$
\langle u , v \rangle = \int _ { \Omega } u ( t ) v ( t ) d t , \quad \| u \| = \langle u , u \rangle ^ { 1 / 2 } .
$$

The infinitely many singular values $\sigma _ { i }$ quickly decay with $i$ and cluster at zero. Therefore (3.6.1) has a solution $f \in L ^ { 2 } ( \Omega )$ only for special right-hand sides $g$ .A known (Groetsch [539, $\mathrm { 1 9 8 4 }$ ,Theorem 1.2.6]) necessary and sufficient condition is that $g$ satisfies the Picard condition

$$
\sum _ { i = 1 } ^ { \infty } | u _ { i } ^ { T } g / \sigma _ { i } | ^ { 2 } < \infty .
$$

In most practical applications the kernel $K$ of integral equation (3.6.1) is usually given exactly by the mathematical model, while $g$ consists of measured quantities known with a certain accuracy at a finite set of points $s _ { 1 } , \ldots , s _ { n }$ . To solve the integral equation (3.6.1) numerically, it must first be reduced to a finite-dimensional matrix equation by discretization.This can be done in several ways, e.g.,by quadrature or collocation methods. Let $s _ { i } = - 1 + i h$ ， $t _ { j } = - 1 + j h$ ， $i , j = 0 , 1 , \ldots , n + 1$ , be a uniform mesh on $\Omega = [ - 1 , 1 ]$ with step size $h = 2 / ( n + 1 )$ .With the trapezoidal rule, the integral in (3.6.1) can be approximated by

$$
h \sum _ { j = 0 } ^ { n } w _ { j } K ( s _ { i } , t _ { j } ) f ( t _ { j } ) = g ( s _ { i } ) , \quad i = 0 : m + 1 ,
$$

where $w _ { j } = 1 , j \neq 0 , n$ ,and $w _ { 0 } = w _ { n } = 1 / 2$ Taking $m = n$ and $s _ { i } = t _ { i }$ gives a linear systemfor $x _ { j } = f ( t _ { j } )$ ：

$$
K f = g , \quad K _ { i j } = w _ { i } K ( s _ { i } , t _ { j } ) , \quad g _ { i } = g ( s _ { i } ) .
$$

In theGalerki $\textstyle f = \sum _ { i = 1 } ^ { n } x _ { i } \phi _ { i }$ in an $n$ dimensional subspace $V _ { n } =$ span $\{ \phi _ { 1 } , . . . , \phi _ { n } \}$ of $L ^ { 2 } ( \Omega )$ is determined by the condition

$$
\psi _ { j } ^ { T } ( K x - g ) , \quad j = 1 , \dots , n ,
$$

where $W _ { n } = \operatorname { s p a n } \left\{ \psi _ { 1 } , \dots , \psi _ { n } \right\}$ is a second $n$ -dimensional subspace of $L ^ { 2 } ( \Omega )$ . This leads again to a finite-dimensional linear system $K f = g$ for the vector $( f _ { 1 } , \ldots , f _ { n } )$ , where

$$
K _ { i j } = \psi _ { j } ^ { T } K \phi _ { i } , \qquad g _ { j } = \psi _ { j } ^ { T } g .
$$

The discretized system $K f = g$ or, more generally, the least squares problem $\operatorname* { m i n } _ { x } \| K f -$ $g \Vert _ { 2 }$ ,will inherit many properties of the integral equation (3.6.1). In the singular value decomposition

$$
K = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n } \sigma _ { i } u _ { i } v _ { i } ^ { T } ,
$$

the singular values $\sigma _ { i }$ will decay rapidly and cluster near zero with no evident gap between any two consecutive singular values. Such matrices have an ill-determined numerical rank, and the corresponding problem is a discrete ill-posed problem. The solution usually depends mainly on a few larger singular values $\sigma _ { 1 } , \ldots , \sigma _ { p } , p \ll n .$ .The effective condition number for the exact right-hand side $g$ ，

$$
\kappa _ { e } = \sigma _ { 1 } / \sigma _ { p } \ll \kappa ( K ) , \quad p \ll n ,
$$

is usually small. The concept of effective condition number was introduced by Varah [1086, 1973]; see also Chan and Foulser [226,1988].

Example 3.6.1. Consider the Fredholm integral equation (3.6.1) with kernel $K ( s , t ) = e ^ { - ( s - t ) ^ { 2 } }$ Let $K f = g$ be the system of linear equations obtained by discretization with the trapezoidal rule on a square mesh with $m = n = 1 0 0$ .The singular values of $K$ are displayed in logarithmic scale in Figure 3.6.1. They decay toward zero,and there is no distinct gap anywhere in the spectrum. For $i > 3 0$ ， $\sigma _ { i }$ are close to roundoff level, and in double precision the numerical rank of $K$ certainly is smaller than 30.

The discretized linear system $K f = g$ will only have a meaningful solution for right-hand sides $b$ that satisfy a discrete version of the Picard condition; see Hansen [573,199o]. If $g$ is affected by noise,then the exact solution for the noisy right-hand side $g = g _ { e x a c t } + e$ will bear no resemblance to the noise-free true solution. A consequence of the Picard condition for the continuous problem is that the coefficients $c _ { i } = u _ { i } ^ { T } g$ for $g _ { e x a c t }$ in the SVD solution of the discretized system

$$
f = K ^ { \dagger } g _ { e x a c t } = \sum _ { i = 1 } ^ { n } c _ { i } \sigma _ { i } ^ { - 1 } v _ { i }
$$

![](images/e3b20bb124cb59dddc24b1c482d3b412341f60feb14456eddd8fd24aeb6a8bce.jpg)  
Figure 3.6.1. Singular values $\sigma _ { i }$ of a discretized integral operator. Used with permission of Springer International Publishing;from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e ,$ 2015; permission conveyed through Copyright Clearance Center, Inc.

must eventually decrease faster than $\sigma _ { i }$ . However, when $g _ { e x a c t }$ is contaminated with errors, any attempt to solve the discrete ill-posed problem numerically without restriction of the solution space will give a meaningless result.

In many applications the kernel $k ( s , t )$ depends only on the difference $s - t$ , and the integral equation has the form

$$
\int _ { 0 } ^ { 1 } h ( s - t ) f ( t ) d t = g ( s ) , \quad 0 \leq s , t \leq 1 .
$$

The problem of computing $f$ given $h$ and $g$ is a deconvolution problem. An example is gravity surveying,where one wants to determine the unknown mass distribution $f$ underground from measurements of the vertical gravity field $g$ at the surface; see Hansen [577,2oo2]. Another example is the inverse heat equation; see Elden [373,1995]. If in the discretization the quadrature points $t _ { j }$ and the collocation points $s _ { i }$ are identical and equidistantly spaced, then the elements in $A$ form a Toeplitz matrix $K = ( k _ { i j } )$ with constant entries along each diagonal, i.e., $k _ { i j } = t _ { j - i }$ This allows very efficient solution algorithms to be developed.

# 3.6.2 - Truncated SVD

The purpose of a regularization method is to diminish the effect of noise in the data and produce a good approximation of the noise-free solution to an ill-conditioned linear system $A x = b$ .In truncated SVD (TSVD) the approximate solution is taken to be

$$
x _ { k } = A _ { k } ^ { \dagger } b = V _ { k } \Sigma _ { k } ^ { \dagger } U _ { k } ^ { T } b ,
$$

where $A _ { k } = U _ { k } \Sigma _ { k } V _ { k } ^ { T }$ is the SVD expansion (3.6.6) of $A \in \mathbb { R } ^ { m \times n }$ truncated to $k \ll n$ terms. Recall that $A _ { k }$ is the best rank- $k$ approximation of $A$ .Furthermore,for some tolerance $\delta _ { k }$ it holds that

$$
\| A - A _ { k } \| _ { 2 } = \| A V _ { k } ^ { \perp } \| _ { 2 } \leq \delta _ { k } , \quad V _ { k } ^ { \perp } = ( v _ { k + 1 } , \ldots , v _ { n } ) ,
$$

where the columns of $V _ { k } ^ { \perp }$ span an approximate nullspace of $A$ ．The number of terms to include in the SVD expansion depends on the noise level in the data. It should be chosen so that a large reduction in the norm of the residual $b - A x _ { k }$ is achieved without causing the norm of the approximate solution $x _ { k }$ to become too large. The TSVD method is widely used as a generalpurpose method for small to medium-sized ill-posed problems.For many ill-posed problems the solution can be well approximated by the TSVD solution with a small number of terms. Such problems are called effectively well-conditioned.

In statistical literature, TSVD is known as principal component regression (PCR) and often formulated in terms of the eigenvectors of $A ^ { T } A$ instead of the SVD of $A$ ; see Massy [781,1965]. The Gauss-Markov theorem (Theorem 1.1.4) states that the least squares solution is the best unbiased linear estimator of $x$ ,in the sense that it has minimum variance. If $A$ is ill-conditioned, this minimum variance is still large. In regularization the variance can be substantially decreased by allowing the estimator to be biased.

In TSVD the components selected from the SVD expansion correspond to the $k$ largest singular values. The right-hand side $b$ can have larger projections on some singular vectors corresponding to smaller singular values.In such a case,one could take into account also the size of the coefficients $c _ { i } = u _ { i } ^ { T } b$ when choosing which components of the SVD expansion to include in the approximation.

Hansen,Seki,and Shibahashi [585,1992] introduce the modified solution MTSVD $x _ { B , k }$ that solves the least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| B x \| _ { 2 } , \qquad S = \{ x \mid \| A _ { k } x - b \| _ { 2 } = \operatorname* { m i n } \} ,
$$

where $B \in \mathbb { R } ^ { p \times n }$ is a matrix that penalizes solutions that are not smooth. The TSVD solution is obtained by taking $B = I$ ．The MTsVD problem has the same form as (2.3.1O) used in Section 2.3.2 to resolve rank-deficiency. The solution can be written in the form

$$
x _ { B , k } = x _ { k } - V _ { k } ^ { \perp } z , \quad z \in \mathbb { R } ^ { n - k } ,
$$

where $x _ { k } = V _ { k } \Sigma _ { k } ^ { - 1 } U _ { k } ^ { T } b$ is the TSVD solution,andthecolums of $V _ { k } ^ { \perp }$ span the nullspace of $A _ { k }$ The vector $z$ can be computed from the QR factorization of $B V _ { k } ^ { \perp } \in \overset { \cdot \cdot } { \mathbb { R } } ^ { p \times ( n - k ) }$ as the solution to the least squares problem

$$
\operatorname* { m i n } _ { z } \| ( B V _ { k } ^ { \perp } ) z - B b _ { k } \| _ { 2 } .
$$

It is often desired to compute a sequence of MTSVD solutions for decreasing values of $k$ When $k$ is decreased, more columns are added to the left of $B V _ { k } ^ { \perp }$ . This makes it costly to update the QR factorization of $B V _ { k } ^ { \perp }$ . It is more efficient to work with

$$
\widetilde V _ { k } ^ { \perp } = V _ { k } ^ { \perp } P _ { k } = ( v _ { n } , \ldots , v _ { n - k } ) ,
$$

where $P _ { k }$ is the permutation matrix that reverses the columns in $V _ { k } ^ { \perp }$ . Then in the sequence of QR factorizations of $\widetilde { V } _ { k } ^ { \perp }$ ， $k = 1 , 2 , \dots$ ,columns are added to the right,

$$
v _ { n } , ( v _ { n } , v _ { n - 1 } ) , ( v _ { n } , v _ { n - 1 } , v _ { n - 2 } ) , \ldots .
$$

Hansen et al.[585,1992] illustrate the use of MTSVD for a problem in helioseismology in astrophysics. The fundamental equation is a Fredholm equation,and the regularizing operator is an approximation to the second-derivative operator. While the TSVD solution shows unrealistic oscillations, the MTSVD solution behaves much better.

# Notes and references

Methods for computing truncated SVD solutions by RRQR (see Section 2.3.5) are studied by Chan and Hansen [227,199o,228,1992]. Hansen [576,1998] surveys the use of RRQR factorizations for solving discrete ill-posed problems.He shows that when the ratio $\sigma _ { k + 1 } / \sigma _ { k }$ is small,

the subspaces spanned by the selected columns for such methods are almost identical to those from TSVD.

# 3.6.3 - Tikhonov Regularization

Tikhonov regularization is the most widely used regularization method for il-posed problems. In its general form the regularized solution is taken to be the solution of a least squares problem

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } ^ { 2 } + \lambda \| L x \| _ { 2 } ^ { 2 } .
$$

The parameter $\lambda > 0$ governs the balance between a small-residual norm and the regularity of the solution as measured by $\| L x \| _ { 2 }$ ．Attaching Tikhonov's name to the method is motivated by the groundbreaking work of Tikhonov [1O63,1963] and Tikhonov and Arsenin [1062, 1977].Early works by other authors on Tikhonov regularization are surveyed by Hansen [579, 2010,Appendix C]. Regularization methods of the form (3.6.11) have been used by many other authors for smoothing noisy data and in methods for nonlinear least squares; see Levenberg [736, 1944]. In statistics the method is known as ridge regression.

Often $L$ is chosen as a discrete approximation of some derivative operator. Typical choices are

$$
L _ { 1 } = \left( \begin{array} { c c c c } { { 1 } } & { { - 1 } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { - 1 } } \end{array} \right) , \qquad L _ { 2 } = \left( \begin{array} { c c c c } { { - 1 } } & { { 2 } } & { { - 1 } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } \\ { { } } & { { } } & { { - 1 } } & { { 2 } } & { { - 1 } } \end{array} \right) ,
$$

or a combination of these. These operators have a smoothing effect on the solution and are called smoothing-norm operators; see Hanke and Hansen [57O,1993]. Note that $L _ { 1 }$ and $L _ { 2 }$ are banded matrices with small bandwidth and full row rank. Their nullspaces are explicitly known:

$$
\begin{array} { r l } & { \mathcal { N } ( L _ { 1 } ) = w _ { 1 } = ( 1 , 1 , \ldots , 1 ) ^ { T } , } \\ & { \mathcal { N } ( L _ { 2 } ) = \mathrm { s p a n } ( w _ { 1 } , w _ { 2 } ) , \quad w _ { 2 } = ( 1 , 2 , \ldots , n ) ^ { T } . } \end{array}
$$

Clearly, any component of the solution in $\mathcal { N } ( L )$ will not be affected by the regularization term $\lambda ^ { 2 } \| L x \| _ { 2 }$ .Since the nullspaces are spanned by very smooth vectors, it will not be necessary to regularize this part of the solution.

Any combination of the matrices $L _ { 1 } , L _ { 2 }$ and the unit matrix can also be used. This corresponds to a discrete approximation of a Sobolev norm. It is no restriction to assume that $L \in$ $\mathbb { R } ^ { p \times n } , p \leq n$ If $p > n$ ,then a QR factorization of $L$ can be performed so that $\| L x \| _ { 2 } = \| R _ { 2 } x \| _ { 2 }$ ， where $R _ { 2 } = Q ^ { T } L$ has at most $n$ rows. Then $R _ { 2 }$ can be substituted for $L$ in (3.6.11).

The solution of (3.6.11) satisfies the normal equations

$$
( A ^ { T } A + \lambda L ^ { T } L ) x = A ^ { T } b .
$$

If $A$ and $L$ have no nullspace in common and $\lambda > 0$ ,there is a unique solution. Writing the normal equations as

$$
\begin{array} { r } { A ^ { T } r - \lambda L L ^ { T } x = 0 , \quad r = b - A x , } \end{array}
$$

shows that they are equivalent to the augmented system

$$
\begin{array} { r } { \left( \begin{array} { c c } { I } & { A } \\ { A ^ { T } } & { - \lambda L L ^ { T } } \end{array} \right) \left( \begin{array} { c } { r } \\ { x } \end{array} \right) = \left( \begin{array} { c } { b } \\ { 0 } \end{array} \right) . } \end{array}
$$

Forming the normal equations can be avoided by noting that problem (3.6.11) is equivalent to the least squares problem

$$
\operatorname* { m i n } _ { x } \Big \| \left( { \overset { A } { \sqrt { \lambda } } } _ { L } \right) x - \left( { \overset { b } { 0 } } \right) \Big \| _ { 2 } ,
$$

which can be solved by QR factorization.

The standard form of Tikhonov regularization is obtained for $L \ = \ I$ .Then condition (3.5.23) is trivially satisfied,and the normal equations are

$$
( A ^ { T } A + \lambda I ) x = A ^ { T } b .
$$

The solution of (3.6.16) can be written as the filtered sum

$$
x ( \lambda ) = \sum _ { i = 1 } ^ { n } \frac { u _ { i } ^ { T } b } { \sigma _ { i } } f _ { i } ( \lambda ) v _ { i } , \quad f _ { i } = \frac { \sigma _ { i } ^ { 2 } } { \sigma _ { i } ^ { 2 } + \lambda } ,
$$

where $\sigma _ { i }$ are the singular values and $u _ { i } , v _ { i }$ are the singular vectors of $A$ The quantities $f _ { i }$ ， $0 \leq f _ { i } < 1$ ,are called filter factors (in statistics, shrinkage factors) and are decreasing functions of $\lambda$ If $\lambda \ll \sigma _ { i }$ ，then $f _ { i } \approx 1$ , and the corresponding terms are almost the same as without regularization.On the other hand,if $\lambda \gg \sigma _ { i }$ ，then $f _ { i } \ll 1$ ，and the corresponding terms are damped. For a suitably chosen $\lambda$ ， $x ( \lambda )$ is approximately the same as the TSVD solution.

Often the Tikhonov problem (3.6.11) arises with $A$ and $L$ banded upper triangular matrices. For example,in fitting a polynomial smoothing spline of degree $2 p - 1$ to $m$ data points, the half-bandwidth will be $p$ and $p + 1$ ,respectively; see Reinsch [923,1971]. Eldén [370,1984] shows how to reduce such regularized problems to the form

$$
\operatorname* { m i n } _ { x } \biggl \| \biggl ( \begin{array} { c } { R _ { 1 } } \\ { \sqrt { \lambda } R _ { 2 } } \end{array} \biggr ) x - \biggl ( \begin{array} { c } { d _ { 1 } } \\ { 0 } \end{array} \biggr ) \biggr \| _ { 2 } ,
$$

where $R _ { 1 }$ and $R _ { 2 }$ are banded. For a fixed value of $\lambda$ the regularized problem can be reduced further to upper triangular form. Recall that the order in which the rows are processed in this QR factorization is important for efficiency； see Section 4.1. Unnecessary fill-in is avoided by first sorting the rows so the matrices are in standard form; see Section 4.1.4. The rows are then processed from the top down using plane rotations to give a matrix of banded upper triangular form. For a given value of $\lambda$ this requires $n ( w _ { 1 } + w _ { 2 } - 1 )$ rotations and $4 n ( w _ { 1 } ^ { 2 } + w _ { 2 } ^ { 2 } )$ flops. It can easily be generalized to problems involving several upper triangular band matrices $\lambda _ { 1 } R _ { 1 } , \lambda _ { 2 } R _ { 2 } , \lambda _ { 3 } R _ { 3 }$ ,etc.

Example 3.6.2. Consider the banded regularized least squares problem (3.6.18) where $R _ { 1 }$ and $R _ { 2 }$ are banded upper triangular matrices with bandwidth $w _ { 1 } = 3$ and $w _ { 2 } = 2$ ,respectively. First, let Givens QR factorization be carred out without reordering the rows. Below right is shown the reduced matrix after the first three columns have been brought into upper triangular form. Note that the upper triangular part $R _ { 2 }$ has completely filled in:

$$
\begin{array}{c} { \begin{array} { r l r l r l r } { \left[ \times \right]} & { \times } & { \times } & & { } & & { } \\ & { \times } & { \times } & { \times } & & { } \\ & { \times } & { \times } & { \times } & { } \\ & & { } & & { \times } & { } \\ { \times } & { \times } & & { } & & { } \\ & { \times } & { \times } & & { } & & { } \\ & { \times } & { \times } & { \times } & { } \\ & & { } & & { \times } & { } \end{array} }   & { \Rightarrow } & { { \left[ \begin{array} { l l l l } { \times } & { \times } & { \times } & { } \\ & { \times } & { \times } & { \times } \\ & & { \times } & { \times } \\ & & & { \times } & { \times } \\ { \otimes } & { \otimes } & { \ \oplus } & { + } & { + } \\ & { \otimes } & { \ \otimes } & { + } & { + } \\ & & { \otimes } & { \times } & { + } \\ & & & { \times } & { \times } \end{array} \right] } } \\ & { } & { } & { \times } & { \times } & { } \end{array} 
$$

For a similar problem of size $( 2 n - 1 , n )$ and bandwidth $w$ the complete QR factorization requires $n ( n + 1 ) / 2$ plane rotations and about $2 n ( n + 1 ) w$ flops.

Consider now the application of Givens QR factorization after the rows have been preordered to put $A$ in standard form as shown below left. To the right is shown the matrix after the first three columns have been brought into upper triangular form. Here the algorithm is optimal in the sense that no new nonzero elements are created, except in the final (uniquely determined) $R$ .For a similar matrix of size $( 2 n - 1 ) \times n$ the factorization only requires $n ( w + 1 ) / 2$ Given rotations, and a total of approximately $2 n ( w + 1 ) w$ flops,an improvement by a factor of $n / w$ ：

$$
\left[ { \begin{array} { r l r l r l r l } { \times } & { \times } & & & & & & \\ { \times } & { \times } & { \times } & & & \\ & { \times } & { \times } & & & \\ & { \times } & { \times } & & & \\ & { \times } & { \times } & & \\ & & { \times } & { \times } & \\ & & & { \times } & & \\ & & & { \times } & & \\ & & & { \times } & & \\ & & & & { \times } \end{array} } \right] \quad \Rightarrow \quad \left[ { \begin{array} { r l r l r l } { \times } & { \times } & { + } & & & \\ { \otimes } & { \times } & { \times } & { + } & \\ & { \otimes } & { \times } & { + } & \\ & { \otimes } & { \otimes } & { \times } & \\ & & { \otimes } & { \times } & \\ & & { \otimes } & { \times } & { \times } \\ & & & { \times } & { \times } \\ & & & & { \times } & { \times } \end{array} } \right]
$$

Groetsch [539, $\mathrm { 1 9 8 4 } ]$ has shown that when the exact solution is very smooth and in the presence of noisy data, Tikhonov regularization cannot reach the optimal solution that the data allows. In those cases the solution can be improved by using iterated Tikhonov regularization, suggested by Riley [929,1956]. In this method a sequence of improved approximate solutions is computed by

$$
\begin{array} { r } { x ^ { ( 0 ) } = 0 , \qquad x ^ { ( q + 1 ) } = x ^ { ( q ) } + \delta x ^ { ( q ) } , } \end{array}
$$

where $\delta x ^ { ( q ) }$ solves the regularized least squares problem

$$
\operatorname* { m i n } _ { \delta x } \left\| \left( \begin{array} { c } { { A } } \\ { { \sqrt \lambda I } } \end{array} \right) \delta x - \left( \begin{array} { c } { { r ^ { ( q ) } } } \\ { { 0 } } \end{array} \right) \right\| _ { 2 } , \quad r ^ { ( q ) } = b - A x ^ { ( q ) } .
$$

This iteration may be implemented very effectively because only one QR factorization is needed; see Golub [487,1965]. A related scheme is suggested by Rutishauser [952,1g68]. The convergence can be expressed in terms of the SVD of $A$ as

$$
x ^ { ( q ) } ( \lambda ) = \sum _ { i = 1 } ^ { n } \frac { c _ { i } f _ { i } ^ { ( q ) } } { \sigma _ { i } } v _ { i } , \quad f _ { i } ^ { ( q ) } = 1 - \bigg ( \frac { \lambda } { \sigma _ { i } ^ { 2 } + \lambda } \bigg ) ^ { q } .
$$

Thus, for $q = 1$ we have the standard regularized solution, and $x ^ { ( q ) }  A ^ { \dagger } b$ as $q  \infty$ When iterated sufficiently many times, Tikhonov regularization will reach an accuracy that cannot be improved significantly by any other method; see Hanke and Hansen [57O,1993l.

# 3.6.4 - Determining the Regularization Parameter

Determining a suitable value of the regularization parameter in TSVD or Tikhonov regularization is often a major difficulty. If the “noise level" $\eta$ in the data $b$ is known, the discrepancy principle of Morozov [814,1984] can be used. In TSVD the expansion is then truncated when the residual satisfies

$$
\| b - A x _ { k } \| _ { 2 } \leq \eta .
$$

Similarly,in Tikhonov regularization,

$$
\operatorname* { m i n } _ { x } \{ \| A x - b \| _ { 2 } ^ { 2 } + \lambda \| x \| _ { 2 } ^ { 2 } \} , \quad A \in \mathbb { R } ^ { m \times n } ,
$$

the parameter $\lambda$ is chosen as the smallest value for which(3.6.21) is satisfied. The attained accuracy can be very sensitive to the value of $\eta$ It has been observed that the discrepancy principle tends to give a slightly oversmoothed solution. This means that not allthe information presentin the datais recovered.

When no prior information about the noise level in the data is available,a great number of different methods have been proposed. All of them have the common property that they require the solution for many values of the regularization parameter $\lambda$ .TheL-curve method was first proposed by Lawson and Hanson [727,1995, Chapter 26]. It derives its name from a plot in a doubly logarithmic scale of the curve $( \| b - A x _ { \lambda } \| _ { 2 } , \| x _ { \lambda } \| _ { 2 } )$ ，which typically is shaped like the letter L. Choosing $\lambda$ near the“corner” of this L-curve represents a compromise between a small residual and a small solution. The L-curve method is further studied and refined by Hansen [574, 1992].Hansen and O'Leary [584,1993l propose choosing $\lambda$ more precisely as the point on the L-curve where the curvature has the largest magnitude. Advantages and shortcomings of this method are discussed by Hansen [576,1998]. For large-scale problems it may be too expensive to compute sufficiently many points on the L-curve. Calveti et al.[199,2oo2] show how to compute cheap upper and lower bounds in this case.

In generalized cross-validation(GCV） the parameter in Tikhonov regularization is estimated directly from the data. The underlying statistical model is that the components of $b$ are subject to random errors of zero mean and covariance matrix $\sigma ^ { 2 } I _ { m }$ ，where $\sigma ^ { 2 }$ may or may not be known. The predicted values of $b$ are written as $A x _ { \lambda } = P _ { \lambda } b$ ，where

$$
P _ { \lambda } = A A _ { \lambda } ^ { \dagger } , \quad A _ { \lambda } ^ { \dagger } = ( A ^ { T } A + \lambda I ) ^ { - 1 } A ^ { T }
$$

is the symmetric influence matrix. When $\sigma ^ { 2 }$ is known, Craven and Wahba [278,1979] suggest that $\lambda$ should be chosen to minimize an unbiased estimate of the expected true mean square error. When $m$ is large,this minimizer is asymptotically the same as for the GCV function

$$
\mathcal { G } _ { \lambda } = \frac { \| b - A x _ { \lambda } \| _ { 2 } ^ { 2 } } { \operatorname { t r a c e } \left( I _ { m } - P _ { \lambda } \right) ^ { 2 } }
$$

(see Golub, Heath,and Wahba [493,1979l). The GCV method can also be used in other applications,such as truncated SVD methods and subset selection. The GCV function is invariant under orthogonal transformations of $A$ . It can be very flat around the minimum,and localizing the minimum numerically can be difficult; see Varah [1088,1983].

Ordinary cross-validation is based on the following idea; see Allen [17,1974l. Let $x _ { \lambda , i }$ be the solution of the regularized problem when the $i$ th equation is left out. If this solution is a good approximation, then the error in the prediction of the $i$ th component of the right-hand side should be small. This is true for all $i = 1 { : } m$ .Generalized cross-validation is a rotation-invariant version of ordinary cross-validation.

For standard Tikhonov regularization the GCV function (3.6.24) can expressed in terms of the SVD $A = U \Sigma V ^ { T }$ as

$$
P _ { \lambda } = A A _ { \lambda } ^ { \dagger } = U \left( \begin{array} { c c } { { \Omega } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) U ^ { T } ,
$$

where $\boldsymbol { \Omega } = \mathrm { d i a g } ( \omega _ { 1 } , \dots , \omega _ { n } )$ ， $\omega _ { i } = \sigma _ { i } ^ { 2 } / ( \sigma _ { i } ^ { 2 } + \lambda )$ . An easy calculation shows that

$$
\| ( I _ { m } - P _ { \lambda } ) b \| _ { 2 } ^ { 2 } = \lambda \sum _ { i = 1 } ^ { n } \frac { c _ { i } ^ { 2 } } { \sigma _ { i } ^ { 2 } + \lambda } + \sum _ { i = n + 1 } ^ { m } c _ { i } ^ { 2 } ,
$$

where $U ^ { T } b = ( c _ { 1 } , c _ { 2 } \ldots , c _ { m } ) ^ { T }$ . Since $\omega _ { i }$ are the eigenvalues of $P _ { \lambda }$ , we further have

$$
\mathrm { t r a c e } \left( I _ { m } - P _ { \lambda } \right) = m - \sum _ { i = 1 } ^ { n } \omega _ { i } = m - n + \sum _ { i = 1 } ^ { n } \frac { \lambda } { \sigma _ { i } ^ { 2 } + \lambda } .
$$

For the general case $B \neq I$ ,formulas similar to (3.6.26) and (3.6.27) can be derived from the GSVD,or a transformation to the standard case can be used; see Section 3.6.5.

Example 3.6.3 (Golub and Van Loan [512,198g,Problem 12.1.5]). For $A = ( 1 , 1 , \ldots , 1 ) ^ { T } \in$ $\mathbb { R } ^ { m \times 1 }$ and $b \in \mathbb { R } ^ { m }$ the GCV function becomes

$$
\mathcal { G } _ { \lambda } = \frac { m ( m - 1 ) s ^ { 2 } + \nu ^ { 2 } m ^ { 2 } \bar { b } ^ { 2 } } { ( m - 1 + \nu ) ^ { 2 } } , \quad \nu = \frac { \lambda } { m + \lambda } ,
$$

where

$$
\bar { b } = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } b _ { i } , \qquad s ^ { 2 } = \frac { 1 } { m - 1 } \sum _ { i = 1 } ^ { m } ( b _ { i } - \bar { b } ) ^ { 2 } .
$$

It can be readily verifed that $\mathcal { G } _ { \lambda }$ is minimized for $\nu = s ^ { 2 } / ( m \bar { b } ^ { 2 } )$ ,and the optimal value of $\lambda$ is $\lambda _ { o p t } = \left( ( \bar { b } / s ) ^ { 2 } - 1 / m \right) ^ { - 1 }$

The GCV function can also be computed from the QR factorization

$$
\left( \begin{array} { c c } { { A } } & { { b } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { c _ { 1 } } } \\ { { 0 } } & { { c _ { 2 } } } \end{array} \right) .
$$

The regularized problem (3.6.22) is equivalent to $\begin{array} { r } { \operatorname* { m i n } _ { x } \| R x - c _ { 1 } \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| x \| _ { 2 } ^ { 2 } } \end{array}$ By a second QR factorization this can be reduced further to

$$
Q _ { \lambda } ^ { T } \left( { \begin{array} { c c } { R } & { c _ { 1 } } \\ { { \sqrt { \lambda } } I _ { n } } & { 0 } \end{array} } \right) = \left( { \begin{array} { c c } { R _ { \lambda } } & { d _ { 1 } } \\ { 0 } & { d _ { 2 } } \end{array} } \right) ,
$$

where $R _ { \lambda }$ is upper tridiagonal, and $R ^ { T } R + \lambda I _ { n } \ = \ R _ { \lambda } ^ { T } R _ { \lambda }$ . The solution of the regularized problem is then obtained by solving $R _ { \lambda } x ( \lambda ) = d _ { 1 }$ and the residual norm is given by

$$
\lVert b - A x _ { \lambda } \rVert _ { 2 } ^ { 2 } = \lVert c _ { 2 } \rVert _ { 2 } ^ { 2 } + \lVert d _ { 2 } \rVert _ { 2 } ^ { 2 } .
$$

To compute the trace term in the GCV function we first note that $A A _ { \lambda } ^ { \dagger } = A M _ { \lambda } ^ { - 1 } A ^ { T }$ ， where

$$
M _ { \lambda } ^ { - 1 } = ( A ^ { T } A + \lambda I ) ^ { - 1 } = ( R _ { \lambda } ^ { T } R _ { \lambda } ) ^ { - 1 }
$$

equals the covariance matrix. From elementary properties of the trace function,

$$
\begin{array} { r l } & { \operatorname { t r a c e } { ( I _ { m } - A M _ { \lambda } ^ { - 1 } A ^ { T } ) } = m - \operatorname { t r a c e } { ( M _ { \lambda } ^ { - 1 } A ^ { T } A ) } } \\ & { = m - \operatorname { t r a c e } { ( I _ { n } - \lambda M _ { \lambda } ^ { - 1 } ) } = m - n + \lambda \mathrm { t r a c e } { ( M _ { \lambda } ^ { - 1 } ) } . } \end{array}
$$

Hence,the trace computation is reduced to computing the sum of the diagonal elements of the covariance matrix $C = ( R _ { \lambda } ^ { T } R _ { \lambda } ) ^ { - 1 }$ . An efficient algorithm for this is given by Elden [371,1984]. By reducing $A$ to upper bidiagonal form $U ^ { T } A V = B$ and setting $y = V ^ { T } x$ ，a regularization problem of bidiagonal form is obtained. This can be further reduced by plane rotations to upper triangular form

$$
Q ^ { T } \left( \begin{array} { c c } { { B } } & { { g _ { 1 } } } \\ { { \sqrt \lambda I _ { n } } } & { { 0 } } \end{array} \right) = \left( \begin{array} { c c } { { B _ { \lambda } } } & { { z _ { 1 } } } \\ { { 0 } } & { { z _ { 2 } } } \end{array} \right)
$$

with $B _ { \lambda }$ upper bidiagonal:

$$
B _ { \lambda } = \left( \begin{array} { l l l l } { \rho _ { 1 } } & { \theta _ { 2 } } & & \\ & { \rho _ { 2 } } & { \ddots } & \\ & & { \ddots } & { \theta _ { n } } \\ & & & { \rho _ { n } } \end{array} \right) .
$$

If $b _ { i } ^ { T }$ denotes the $i$ th row of $B _ { \lambda } ^ { - 1 }$ , then trace $\begin{array} { r } { ( ( B _ { \lambda } ^ { T } B _ { \lambda } ) ^ { - 1 } ) = \sum _ { i = 1 } ^ { n } \| b _ { i } \| _ { 2 } ^ { 2 } } \end{array}$ From the identity $B _ { \lambda } \dot { B } _ { \lambda } ^ { - 1 } = I$ we obtain the recursion

$$
\rho _ { n } b _ { n } = e _ { n } , \qquad \rho _ { i } b _ { i } = e _ { i } - \theta _ { i + 1 } b _ { i + 1 } , \quad i = n - 1 , \ldots , 2 , 1 .
$$

Because $B _ { \lambda } ^ { - 1 }$ is upper triangular, $b _ { i + 1 }$ is orthogonal to $e _ { i }$ . Hence

$$
\| b _ { n } \| _ { 2 } ^ { 2 } = 1 / \rho _ { n } ^ { 2 } , \qquad \| b _ { i } \| _ { 2 } ^ { 2 } = ( 1 + \theta _ { i + 1 } ^ { 2 } \| b _ { i + 1 } \| _ { 2 } ^ { 2 } ) / \rho _ { i } ^ { 2 } , \quad i = n - 1 , n - 2 , \ldots , 1 .
$$

This algorithm for computing the trace term requires only $O ( n )$ flops.

Hutchinson and de Hoog [649,1985l give a similar method for computing the GCV function for smoothing noisy data with polynomial spline functions of degree $2 p - 1$ . It is based on the observation that only the elements in the central $2 p + 1$ bands of the inverse of the influence function $P _ { \lambda }$ (3.6.23)are needed. These elements can be computed efficiently from the Cholesky factor of $P _ { \lambda }$ . Their algorithm fully exploits the banded structure of the problem and only requires $\mathcal { O } ( p ^ { 2 } m )$ operations.A Fortran implementation for $p = 2$ is given in Hutchinson and de Hoog [650,1986].

# 3.6.5 -Transformation to Standard Form

Most methods for determining the regularization parameter require repeated solution of the regularized problem for a sequence of values of $\lambda$ .For generalized Tikhonov regularization

$$
\operatorname* { m i n } _ { x } \big \{ \| A x - b \| _ { 2 } ^ { 2 } + \lambda \| L x \| _ { 2 } ^ { 2 } \big \} ,
$$

this can be expensive. Great savings can be achieved by an initial transformation into a problem of standard form.If $L$ has full column rank,such a reduction can easily be made as follows. Let $L = Q _ { L } R _ { L }$ be the (thin) QR factorization. If $L$ has full column rank, then $R _ { L } \in \mathbb { R } ^ { n \times n }$ is nonsingular, and with $y = R _ { L } x$ ,problem (3.6.34) becomes

$$
\operatorname* { m i n } _ { \widetilde { x } } \| ( \widetilde { A } y - \widetilde { b } \| _ { 2 } ^ { 2 } + \lambda \| y \| _ { 2 } ^ { 2 } ,
$$

where $\widetilde { A } = A R _ { L } ^ { - 1 }$ and $R _ { L } x = y$

If $\operatorname { r a n k } ( L ) < n$ as for the smoothing matrices $L _ { 1 }$ and $L _ { 2 }$ in (3.6.12), the above transformation does not work, but one can proceed as in Eldén [367,1977]. Let

$$
L ^ { T } = \left( W _ { 1 } \quad W _ { 2 } \right) { \binom { R _ { L } } { 0 } } = W _ { 1 } R _ { L }
$$

be the QR factorization of $L ^ { T }$ . (When $L$ is banded,this QR factorization only requires $O ( n )$ flops.）Then $L ^ { \dagger } = W _ { 1 } R _ { L } ^ { - T }$ is the pseudoinverse of $L$ ,and $W _ { 2 } \in \mathbb { R } ^ { n \times t }$ is orthonormal and spans $\mathcal { N } ( L )$ . With

$$
x = L ^ { \dagger } y + W _ { 2 } z
$$

the solution $x$ is split into two orthogonal components with residual vector $r = b - A L ^ { \dagger } y -$ $( A W _ { 2 } ) z$ .If $A$ and $L$ have no nullspace in common, it follows that $\operatorname { r a n k } ( A W ) = t$ . Computing $A W _ { 2 }$ and its QR factorization gives

$$
A W _ { 2 } = Q \left( { U \atop 0 } \right) , \quad Q = ( Q _ { 1 } , Q _ { 2 } ) ,
$$

where $U \in \mathbb { R } ^ { t \times t }$ nonsingular. Then

$$
\begin{array} { r } { Q ^ { T } ( A x - b ) = \left( { Q } _ { 1 } ^ { T } ( A L ^ { \dagger } y - b ) - U z \right) = \binom { r _ { 1 } } { r _ { 2 } } , } \end{array}
$$

where for any given $y , z$ can be determined so that $r _ { 1 } = 0$ ．Thus,the generalized problem is reduced to the standard form (3.6.35) with

$$
\widetilde { A } = Q _ { 2 } ^ { T } ( A L ^ { \dagger } ) , \qquad \widetilde { b } = Q _ { 2 } ^ { T } b .
$$

Finally, $z$ is found from $U z = Q _ { 1 } ^ { T } ( A L ^ { \dagger } y - b )$ and $x$ is retrieved from (3.6.37).

The solution to (3.6.34)can also be expressed in terms of the GSVD (3.1.53) of the matrix pair $( A , L )$ ; see Varah [1087,1979]. If $\operatorname { r a n k } ( L ) = p$ ,the GSVD has the form

$$
A W = U \left( \begin{array} { c c } { { \mathrm { d i a g } \left( \alpha _ { i } \right) } } & { { 0 } } \\ { { 0 } } & { { I _ { n - p } } } \\ { { 0 } } & { { 0 } } \end{array} \right) , \qquad L W = V \left( \mathrm { d i a g } \left( \beta _ { i } \right) \quad 0 \right) ,
$$

where $U$ and $V$ are orthogonal and $\alpha _ { i } ^ { 2 } + \beta _ { i } ^ { 2 } = 1$ $i = 1 , \dotsc , p$ The columns of $W =$ $( w _ { 1 } , \ldots , w _ { n } )$ are $A ^ { T } A$ -orthogonal, i.e.,

$$
( A w _ { i } ) ^ { T } ( A w _ { j } ) = 0 , \quad i \neq j .
$$

The generalized normal equations $( A ^ { T } A + \lambda L ^ { T } L ) x = A ^ { T } b$ simplify to

$$
\left[ \left( \begin{array} { c c } { \mathrm { d i a g } \left( \alpha _ { i } ^ { 2 } \right) } & { 0 } \\ { 0 } & { I _ { n - p } } \end{array} \right) + \lambda \left( \begin{array} { c c } { \mathrm { d i a g } \left( \beta _ { i } ^ { 2 } \right) } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \right] y = \left( \begin{array} { c c } { \mathrm { d i a g } \left( \alpha _ { i } \right) } & { 0 } \\ { 0 } & { I _ { n - p } } \end{array} \right) U ^ { T } b ,
$$

where $y = W x$ .The solution to (3.6.34) can then be writen $x = x _ { 1 } + x _ { 2 }$ , where

$$
x _ { 1 } = \sum _ { i = 1 } ^ { p } \frac { ( u _ { i } ^ { T } b ) \sigma _ { i } } { \sigma _ { i } ^ { 2 } + \lambda } w _ { i } , \qquad x _ { 2 } = \sum _ { i = p + 1 } ^ { n } ( u _ { i } ^ { T } b ) w _ { i } ,
$$

and $\sigma _ { i } = \alpha _ { i } / \beta _ { i }$ . The second term $x _ { 2 } \in \mathcal { N } ( L )$ is the unregularized part of the solution. This GSVD splittng resembles expansion (3.6.17) of the solution for a problem in standard form and has the property that $A x _ { 1 } \perp A x _ { 2 }$

The two components in (3.6.40) are solutions to two independent least squares problems

$$
\operatorname* { m i n } _ { A ^ { T } A x _ { 1 } \perp \mathcal { N } ( L ) } \| A x _ { 1 } - b \| _ { 2 } ^ { 2 } + \lambda \| L x _ { 1 } \| _ { 2 } , \ \operatorname* { m i n } _ { x _ { 2 } \in \mathcal { N } ( L ) } \| A x _ { 2 } - b \| _ { 2 } ,
$$

where the second problem is independent of $\lambda$ .In the QR factorization of $L ^ { T }$ (3.6.36), the orthonormal columns of $W _ { 2 }$ in span $\mathcal { N } ( L )$ and the solution can be obtained from

$$
x _ { 2 } = W _ { 2 } z , \quad z = ( A W _ { 2 } ) ^ { \dagger } b .
$$

From the QR factorization of $A W _ { 2 }$ (3.6.38), we obtain

$$
x _ { 2 } = { \cal W } _ { 2 } U ^ { - 1 } ( Q _ { 1 } ^ { T } b ) .
$$

Usually, the dimension of $\mathcal { N } ( L )$ is very small and the cost of computing $x _ { 2 }$ is negligible.The first problem in (3.6.41) can be transformed into standard form using the $A$ -weighted pseudoinverse of $L$ introduced by Eldén [369,1982],

$$
{ \cal L } _ { A } ^ { \dagger } = ( I - P ) { \cal L } ^ { \dagger } , ~ P = ( A ( I - { \cal L } ^ { \dagger } { \cal L } ) ) ^ { \dagger } A ,
$$

where $I - L ^ { \dagger } L = P _ { \mathbf { \mathcal { N } } ( L ) }$ . Setting $x _ { 1 } = L _ { A } ^ { \dagger } y$ , we have $L x _ { 1 } = L L _ { A } ^ { \dagger } y = y$ , and the first problem in (3.6.41) becomes

$$
\operatorname* { m i n } _ { y } { \| A L _ { A } ^ { \dag } y - b \| _ { 2 } ^ { 2 } } + \lambda ^ { 2 } \| y \| _ { 2 } ^ { 2 } .
$$

Because $W _ { 2 }$ and $A W _ { 2 }$ have full column rank, it follows that

$$
( A P _ { \mathrm { \mathcal { N } ( \mathit { L } ) } } ) ^ { \dag } = ( A W _ { 2 } W _ { 2 } ^ { \dag } ) ^ { \dag } = W _ { 2 } ( A W _ { 2 } ) ^ { \dag } ,
$$

and hence

$$
\begin{array} { r } { L _ { A } ^ { \dag } = ( I - P ) L ^ { \dag } , \quad P = W _ { 2 } ( A W _ { 2 } ) ^ { \dag } A . } \end{array}
$$

It can be verified (Hansen [580,2013l) that $P ^ { 2 } = P$ and ${ \boldsymbol { P } } \neq { \boldsymbol { P } } ^ { T }$ Hence $P$ is an oblique projector onto $\mathcal { N } ( L )$ along the $A$ -orthogonal complement of $\mathcal { N } ( L )$ in $\mathbb { R } ^ { n }$ ; cf. Theorem 3.1.3. It can also be shown that $L _ { A } ^ { \dagger }$ satisfies four conditions similar to the Penrose conditions in Theorem 1.2.10.

The amount of work in the above reduction to standard form is often negligible compared to the amount required for solving the resulting standard form problem. The use of such a reduction in direct and iterative regularization methods is studied by Hanke and Hansen [570, 1993],where a slightly different implementation is used. The use of transformation to standard form in iterative regularization methods is treated in Section 6.4.

# Notes and references

Hansen [576,1998] gives an excellent survey of numerical aspects of solving rank-deficient and discrete ill-posed problems.Direct and iterative algorithms for discrete inverse problems are treated and illustrated by tutorial examples in Hansen [579,2o1o] as well as Hanke [569,2017]. Regularization methods for large-scale ill-posed problems are given by Hanke and Hansen [570, 1993l. Regularization methods for nonlinear il-posed problems are treated by Engl, Hanke, and Neubauer [386,1996]. Hansen, Nagy,and O'Leary [583,2oo6] consider applications to deblurring and filtering images. The use of RRQR factorizations for solving discrete ill-posed problems is analyzed by Hansen [576,1998]. The development of the MATLAB regularization toolboX is described in Hansen [575,1994, 578, 2oo7]. The current version can be downloaded from www.mathworks.com/mat labcentral/.A so-calld trust-region method for regularization of large-scale discrete ill-posed problems is described by Rojas and Sorensen [932,2oo2],with a MATLAB implementation given by Rojas, Santos,and Sorensen [931, 2008].

Chapter 4

# Special Least Squares Problems

# 4.1 - Band Least Squares Problems

# 4.1.1 - Properties of Band Matrices

Band matrices occur frequently in many algorithms for computing eigenvalues and singular values as well as in problems of approximations and differential equations.We define the bandwidth of a square matrix $A \in \mathbb { R } ^ { n \times n }$ to be

$$
w = \operatorname* { m a x } _ { a _ { i j } \neq 0 } | i - j | ,
$$

i.e., all nonzero elements in each row of $A$ lie in at most $w$ contiguous positions. If $w \ll n$ ， then only a small proportion of the $n ^ { 2 }$ elements are nonzero,and they are located in a band centered along the principal diagonal. Band linear systems and least squares problems with small bandwidth $w \ll n$ arise in applications where each variable $x _ { i }$ is coupled to only a few other variables $x _ { j }$ such that $| j - i |$ is small. Clearly, the bandwidth of a matrix depends on the ordering of its rows and columns.

The lower bandwidth $r$ and upper bandwidth $s$ are the smallest integers such that

$$
a _ { i j } = 0 { \mathrm { ~ i f ~ } } j < i - r { \mathrm { ~ o r ~ } } j > i + s , \quad i = 1 , \ldots , n .
$$

In other words,the number of nonzero diagonals below and above the main diagonal are $r$ and $s$ ,respectively. The maximum number of nonzero elements in any row is $w = r + s + 1$ .For example,the matrix

$$
\left( \begin{array} { l l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & & & & \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & & & \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } & { a _ { 3 4 } } & & \\ & { a _ { 4 2 } } & { a _ { 4 3 } } & { a _ { 4 4 } } & { a _ { 4 5 } } & \\ & & { a _ { 5 3 } } & { a _ { 5 4 } } & { a _ { 5 5 } } & { a _ { 5 6 } } \\ & & & { a _ { 6 4 } } & { a _ { 6 5 } } & { a _ { 6 6 } } \end{array} \right)
$$

has $r = 2$ ， $s = 1$ ,and $w = 4$ If $A$ is symmetric, then $r = s$ .Several frequently occurring classes of band matrices have special names, e.g., a matrix for which $r = s = 1$ is called tridiagonal. If $r = 0 , s = 1 ( r = 1 , s = 0 ) \mathrm { . }$ ,the matrix is called upper (lower) bidiagonal.

To avoid storage of zero elements,the diagonals of a band matrix can be stored either as columns in an array of dimension $n \times w$ or as rows in an array of dimension $w \times n$ . For example,

the matrix in (4.1.3) above can be stored as

$$
\left[ \begin{array} { c c c c } { { \ast } } & { { \ast } } & { { a _ { 1 1 } } } & { { a _ { 1 2 } } } \\ { { \scriptstyle a _ { 2 1 } } } & { { a _ { 2 2 } } } & { { a _ { 2 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { a _ { 3 3 } } } & { { a _ { 3 4 } } } \\ { { a _ { 4 2 } } } & { { a _ { 4 3 } } } & { { a _ { 4 4 } } } & { { a _ { 4 5 } } } \\ { { a _ { 5 3 } } } & { { a _ { 5 4 } } } & { { a _ { 5 5 } } } & { { a _ { 5 6 } } } \\ { { a _ { 6 4 } } } & { { a _ { 6 5 } } } & { { a _ { 6 6 } } } & { { \ast } } \end{array} \right] \quad \mathrm { o r } \quad \left[ \begin{array} { c c c c c } { { \ast } } & { { a _ { 1 2 } } } & { { a _ { 2 3 } } } & { { a _ { 3 4 } } } & { { a _ { 4 5 } } } & { { a _ { 5 6 } } } \\ { { a _ { 1 1 } } } & { { a _ { 2 2 } } } & { { a _ { 3 3 } } } & { { a _ { 4 4 } } } & { { a _ { 5 5 } } } & { { a _ { 6 6 } } } \\ { { a _ { 2 1 } } } & { { a _ { 3 2 } } } & { { a _ { 4 3 } } } & { { a _ { 5 4 } } } & { { a _ { 6 5 } } } & { { \ast } } \\ { { a _ { 3 1 } } } & { { a _ { 4 2 } } } & { { a _ { 5 3 } } } & { { a _ { 6 4 } } } & { { \ast } } & { { \ast } } \end{array} \right] .
$$

Except for a few elements indicated by asterisks in the initial and final rows,only nonzero elements of $A$ are stored. Passing along a column in the first storage scheme moves along a diagonal of the matrix,and the rows are aligned. Some elements in the lower right corner are not used. How to perform the subscript computations efciently in algorithms where the matrix is stored in band mode is described in“Contribution $\mathbf { I } / 4 ^ { \mathbf { \mathfrak { s } } }$ of Wilkinson and Reinsch [1123,1971] and in Chapter 4 of Dongarra et al. [322,1979].

It is convenient to use the following MATLAB notation for manipulating band matrices.

Definition 4.1.1. If $a \in \mathbb { R } ^ { n }$ is a vector, then $A = \mathrm { d i a g } \left( a , k \right)$ is a square matrix of order $n + | k |$ with the elements of a on its kth diagonal,where $k = 0$ is the main diagonal, $k > 0$ is above the main diagonal, and $k < 0$ is below the main diagonal. If $A$ is a square matrix of order $n$ ， then $\mathrm { d i a g } \left( A , k \right) \in \mathbb { R } ^ { \left( n - k \right) }$ ， $| k | < n$ , is the column vector consisting of the elements of the kth diagonal of $A$

For example, $\mathrm { d i a g } \left( A , 0 \right)$ is the main diagonal of $A$ ,and if $0 \leq k < n$ ,the $k$ th superdiagonal and subdiagonal of $A$ are

$$
\begin{array} { r } { \mathrm { d i a g } \left( A , k \right) = \left( a _ { 1 , k + 1 } , a _ { 2 , k + 2 } , \ldots , a _ { n - k , n } \right) ^ { T } , } \\ { \mathrm { d i a g } \left( A , - k \right) = \left( a _ { k + 1 , 1 } , a _ { k + 2 , 2 } , \ldots , a _ { n , n - k } \right) ^ { T } . } \end{array}
$$

Clearly, the product of two diagonal matrices $D _ { 1 }$ and $D _ { 2 }$ is another diagonal matrix whose elements are equal to the elementwise product of the diagonals.The following elementary but very useful result shows which diagonals in the product of two square band matrices are nonzero.

Theorem 4.1.2. Let $A \in \mathbb { R } ^ { n \times n }$ and $A _ { 2 } \in \mathbb { R } ^ { n \times n }$ have lower bandwidths $r _ { 1 }$ and $r _ { 2 }$ and upper bandwidths $s _ { 1 }$ and $s _ { 2 }$ ，respectively. Then the products $A B$ and $B A$ have lower and upper bandwidths $r _ { 3 } \le \operatorname* { m i n } \{ r _ { 1 } + r _ { 2 } \}$ and $s _ { 3 } \leq \operatorname* { m i n } \{ s _ { 1 } + s _ { 2 } \}$

Proof. The elements of $C = A B$ are $\begin{array} { r } { c _ { i j } = \sum _ { k = 1 } ^ { n } a _ { i k } b _ { j k } } \end{array}$ . By definition, $a _ { i k } = 0$ if $k > i + r _ { 1 }$ and $b _ { k j } = 0$ if $j > k + r _ { 2 }$ . It follows that $a _ { i k } b _ { j k } = 0$ unless $k \leq i + r _ { 1 }$ and $j \le k + r _ { 2 }$ . But this implies that $k + j \leq i + r _ { 1 } + k + r _ { 2 }$ or $j \leq i + ( r _ { 1 } + r _ { 2 } )$ ,i.e., $C$ has bandwidth at most $r _ { 1 } + r _ { 2 }$ ： The second case follows from the observations that if a matrix has lower bandwidth $r$ ，then $A ^ { T }$ has upper bandwidth $r$ ,and that $( A B ) ^ { T } = B ^ { T } A ^ { T }$ .□

Note that Theorem 4.1.2 holds also for negative values of the bandwidths. For example, a strictly upper triangular matrix $A$ can be said to have lower bandwidth $r = - 1$ . It follows that $A ^ { 2 }$ has lower bandwidth $r = - 2$ ,etc.,and $A ^ { n } = 0$

When the bandwidth of $A \in \mathbb { R } ^ { n \times n }$ and $B \in \mathbb { R } ^ { n \times n }$ are small compared to $n$ the usual algorithms for forming the product $A B$ are not effective on vector computers. Instead, the product can be formed by writing $A$ and $B$ as a sum of their diagonals and multiplying crosswise. For example, if $A$ and $B$ are tridiagonal, then by Theorem 4.1.2 the product $C = A B$ has upper and lower bandwidths two. The five nonzero diagonals of $C$ can be computed by $3 ^ { 2 } = 9$ pointwise vector multiplications independent of $n$

Definition 4.1.3. A square matrix $A \in \mathbb { R } ^ { n \times n }$ ， $n \geq 2$ ，is said to be reducible if there is a partitioning of the index set $\{ 1 , 2 , \ldots , n \}$ into two nonempty disjoint subsets $S$ and $T$ such that $a _ { i j } = 0$ whenever $i \in S$ and $j \in T$ . Otherwise, $A$ is called irreducible. Equivalently, $A$ is reducible if there is a permutation matrix $P$ such that

$$
P ^ { T } A P = \left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) ,
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ are nonempty square submatrices.

If $A$ is reducible,then after a permutation the linear system $A x = b$ is reduced to $P ^ { T } A P y =$ $P ^ { T } b = c$ ， $y = P ^ { T } x$ or

$$
A _ { 1 1 } y _ { 1 } + A _ { 1 2 } y _ { 2 } = c _ { 1 } , \qquad A _ { 2 2 } y _ { 2 } = c _ { 2 } .
$$

The original system has been reduced to two smaller sets of equations. Hence,only the diagonal blocks $A _ { 1 1 }$ and $A _ { 2 2 }$ need to be factorized. If again $A _ { 1 1 }$ or $A _ { 2 2 }$ is reducible,then such a reduction can be carried out again.This can be continued until a triangular block form with irreducible diagonal blocks is obtained. This observation motivates the term reducible.

It is well known (see Duf, Erisman,and Reid [344,1986]) that the inverse of any irreducible matrix $A$ is structurally full,i.e.,it is always possible to find numerical values such that all entries in $A ^ { - 1 }$ will be nonzero.In particular, the inverse of an irreducible band matrix in general has no Zero elements. Therefore,it is important to avoid computing the inverse explicitly. Even storing the elements of $A ^ { - 1 }$ may be infeasible.However, if theLU factorization of $A$ can be carried out without pivoting, then the band structure in $A$ is preserved in the LU factors.

Theorem 4.1.4. Let $A$ have lower bandwidth $r$ and upper bandwidth $s$ ， and assume that the factorization $A = L U$ exists.Then,assuming that LU factorization can be carried out without row and columns permutations, $L$ will have lower bandwidth $r$ and $U$ have upper bandwidth $s$

Proof. The proof is by induction. Assume that the first $k - 1$ columns of $L$ and rows of $U$ have bandwidths $r$ and $s$ .Then for $p = 1 { : } k - 1$ ，

$$
l _ { i p } = 0 , \quad i > p + r , \qquad u _ { p j } = 0 , \quad j > p + s .
$$

The assumption is trivially true for $k = 1$ . Since $a _ { k j } = 0$ for $j > k + s$ , (4.1.5) yields

$$
u _ { k j } = a _ { k j } - \sum _ { p = 1 } ^ { k - 1 } l _ { k p } u _ { p j } = 0 - 0 = 0 , \quad j > k + s .
$$

Similarly, it follows that $l _ { i k } = 0$ ， $i > k + r$ , which completes the induction step.

An important but hard problem is to find a reordering of the rows and columns of $A$ that minimizes the bandwidth of the LU or Cholesky factors. However, there are heuristic algorithms that give almost optimal results; see Section 5.1.5.

When $A$ is tridiagonal,

$$
A = \left( \begin{array} { c c c c c c } { { a _ { 1 } } } & { { c _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { b _ { 2 } } } & { { a _ { 2 } } } & { { c _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { b _ { n - 1 } } } & { { a _ { n - 1 } } } & { { c _ { n } } } \\ { { } } & { { } } & { { } } & { { b _ { n } } } & { { a _ { n } } } \end{array} \right) ,
$$

$L$ can be taken to be lower unit bidiagonal with subdiagonal elements $\gamma _ { 2 } , \ldots , \gamma _ { n }$ ,and $U$ to be upper bidiagonal with diagonal $d _ { 1 } , \ldots , d _ { n }$ and superdiagonal $c _ { 2 } , \ldots , c _ { n }$ .Equating elements in $A$ and $L U$ shows that the upper diagonal in $U$ equals that in $A$ . The other elements in $L$ and $U$ are obtained by the following recursion: $d _ { 1 } = a _ { 1 }$ ，

$$
\gamma _ { k } = b _ { k } / d _ { k - 1 } , \qquad d _ { k } = a _ { k } - \gamma _ { k } c _ { k } , \quad k = 2 : n .
$$

Here $\gamma _ { k }$ and $d _ { k }$ can overwrite $b _ { k }$ and $a _ { k }$ , respectively. The solution to the system $A x = L ( U x ) =$ $g$ is then obtained by solving $L y = f$ by forward substitution: $y _ { 1 } = g _ { 1 }$ ，

$$
y _ { i } = g _ { i } - \gamma _ { i } y _ { i - 1 } , \quad i = 2 , \ldots , n ,
$$

and then solving $U x = y$ by back-substitution: $x _ { n } = y _ { n } / d _ { n }$

$$
x _ { i } = ( y _ { i } - c _ { i + 1 } x _ { i + 1 } ) / d _ { i } , \quad i = n - 1 , \ldots , 2 , 1 .
$$

The total number of flops for the factorization is about $3 n$ and is $2 . 5 n$ for the solution of the triangular systems.Note that the divisions in the substitution can be avoided if(4.1.7) is modified to compute $d _ { k } ^ { - 1 }$ . This may be more eficient because on many computers a division takes more time than a multiplication.

# 4.1.2 - Band Cholesky Factorization

Taking advantage of a band structure of $A \in \mathbb { R } ^ { m \times n }$ in a least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ can lead to significant savings.The matrix of normal equations can be formed rowwise as

$$
C = A ^ { T } A = \sum _ { i = 1 } ^ { m } a _ { i } a _ { i } ^ { T }
$$

in about $m w ^ { 2 }$ flops, where $a _ { i } ^ { T }$ ， $i = 1 , \ldots , m$ , denotes the rows of $A$

Lemma 4.1.5. Assume that $A \in \mathbb { R } ^ { m \times n }$ has row bandwidth $w$ .Then $A ^ { T } A$ has upper and lower bandwidths $s = r = w - 1$

Proof. From the definition (4.1.1) of bandwidth it follows that $a _ { i j } a _ { i k } \neq 0 \Rightarrow | j - k | < w$ This implies that

$$
| j - k | \geq w \Rightarrow ( A ^ { T } A ) _ { j k } = \sum _ { i = 1 } ^ { m } a _ { i j } a _ { i k } = 0 ,
$$

and hence $s \leq w - 1$

Theorem 4.1.6. Let $C = L L ^ { T }$ be the Cholesky factorization of the symmetric positive definite band matrix $C$ 、Then the symmetric matrix $L + L ^ { T }$ inherits the band structure of $C$

Proof. The proof is similar to that of Theorem 4.1.4.

The next algorithm computes the Cholesky factor $L$ of a symmetric (Hermitian） positive definite matrix $C$ using a column sweep ordering. Recall that no pivoting is needed for stability. Only the lower triangular part of $A$ is used.

# Algorithm 4.1.1 (Band Cholesky Algorithm).

function L $=$ bcholf(A,r);   
$\%$ BCHOLF computes the lower triangular Cholesky $\%$ factor L of a positive definite Hermitian $\%$ matrix A of upper and lower bandwidth r.   
%   
$\mathrm { ~ n ~ } =$ size(A,1);   
$\begin{array} { r l } & { \mathrm { ~ f o r ~ j ~ = ~ 1 : n ~ } } \\ & { \mathrm { ~ p ~ = ~ m i n ( j + r , n ) ~ ; ~ q ~ = ~ m a x ( 1 , i - r ) ~ ; } } \\ & { \mathrm { ~ i \ k ~ = ~ q _ { \ell } ~ j - 1 ~ ; ~ j ~ n ~ = ~ j + 1 : p ~ ; } } \\ & { \mathrm { ~ A \left( j , j \right) ~ = ~ s q r t \left( A \left( j , j \right) ~ - ~ A \left( j , i k \right) \ast A \left( j , i k \right) ^ { \circ } \right) ~ ; } } \\ & { \mathrm { ~ A \left( j n , j \right) ~ = ~ \mathsf { \Lambda } \left( A \left( j n , j \right) ~ - ~ A \left( j n , i k \right) \ast A \left( j , i k \right) ^ { \circ } \right) / A \left( j , j \right) ~ ; } } \\ & { \mathrm { ~ e n d } } \\ & { \mathrm { ~ L ~ = ~ t r i \mathsf { 1 } \left( A \right) ~ ; } } \end{array}$

If $r \ll n$ , then this algorithm requires about $n r ( r { + 3 } )$ flops and $n$ square roots to compute the Cholesky factor $L$ When $s \ll n$ this is much less than the $n ^ { 3 } / 3$ flops required in the full case. In the semidefinite case, diagonal pivoting is required, which can destroy the band structure.

The least squares solution is obtained by solving the triangular systems $L y = c = A ^ { T } b$ and $L ^ { T } x = y$ by forward- and back-substitution:

$$
\begin{array} { l l } { { y _ { i } = b _ { i } - \displaystyle \sum _ { j = p } ^ { i - 1 } r _ { j i } y _ { j } , } } & { { i = 1 , \ldots , n , \quad p = \operatorname* { m a x } ( 1 , i - r ) , } } \\ { { { } } } & { { { } } } \\ { { { \displaystyle x _ { i } = \left( y _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { q } r _ { i j } x _ { j } \right) / r _ { i i } , } } } & { { i = n , \ldots , 1 , \quad q = \operatorname* { m i n } ( i + r , n ) . } } \end{array}
$$

Effcient band versions of band forward and back-substitution can be derived. Each requires about $2 ( 2 n - r ) ( r + 1 ) \approx 4 n r$ flops and can be organized so that $y$ and, finally, $x$ overwrite $c$ in storage. Thus,if full advantage is taken of the band structure of the matrices involved, the solution of a least squares problem where $A$ has bandwidth $w \ll n$ requires a total of about $( m + n ) w ^ { 2 } + 4 n w$ flops.

Let $A$ be symmetric positive definite and tridiagonal as in (4.1.6) with $c _ { i } = b _ { i }$ ， $i = 2 , \ldots , n$ ， and write the Cholesky factorization in symmetric form as $A = L D L ^ { T }$ ， $D = \operatorname* { d i a g } \left( d _ { 1 } , \ldots , d _ { n } \right)$ Then the elements in $D$ and $L$ are obtained as follows. Set $d _ { 1 } = a _ { 1 }$ ,and

$$
\gamma _ { k } = b _ { k } / d _ { k - 1 } , \qquad d _ { k } = a _ { k } - \gamma _ { k } b _ { k } , \quad k = 2 , \ldots , n .
$$

Eliminating $\gamma _ { k }$ gives

$$
d _ { k } = a _ { k } - b _ { k } ^ { 2 } / d _ { k - 1 } , \quad k = 2 , \ldots , n .
$$

Sometimes it is more convenient to set $L D = U ^ { T }$ and determine the factorization $A = U ^ { T } D ^ { - 1 } U$

# 4.1.3 - Computing Elements of the Covariance Matrix

Methods for computing the covariance matrix

$$
C _ { x } = ( A ^ { T } A ) ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }
$$

are given in Section 2.1.5. In the case when $R$ is banded, or generally sparse,an algorithm by Golub and Plemmons [505,1g8o] can be used with great savings to compute all elements of $C _ { x }$ in positions where $R$ has nonzero elements. This includes the diagonal elements of $C _ { x }$ that give the variances of least squares solution $x$ .We denote by $\kappa$ the index set $\{ ( i , j ) \in \mathcal { K } \mid r _ { i j } \neq 0 \}$ Note that because $R$ is the Cholesky factor of $A ^ { T } A$ ,its structure is such that $( i , j ) \in \mathcal { K }$ and $( i , k ) \in \mathcal { K }$ imply that $( j , k ) \in \mathcal { K }$ if $j < k$ and $( k , j ) \in \mathcal { K }$ if $j > k$ .From (4.1.12) it follows that

$$
R C _ { x } = R ^ { - T } ,
$$

where $R ^ { - T }$ is lower triangular with diagonal elements $1 / r _ { i i } , i = 1 , \ldots , n$ . Equating the last columns of the identity (4.1.13) gives

$$
R c _ { n } = r _ { n n } ^ { - 1 } e _ { n } , \quad e _ { n } = ( 0 , \ldots , 0 , 1 ) ^ { T } ,
$$

where $c _ { n }$ is the last column of $C _ { x }$ . From this equation the elements in $c _ { n }$ can be computed by back-substitution, ging $c _ { n n } = r _ { n n } ^ { - 2 }$ and

$$
c _ { i n } = - r _ { i i } \sum _ { \stackrel { j = i + 1 } { ( i , j ) \in { \cal K } } } ^ { n } r _ { i j } c _ { j n } , i = n - 1 , \ldots , 1 .
$$

By symmetry $c _ { n i } = c _ { i n }$ ， $i = 1 , \ldots , n - 1$ ,also the last row of $C _ { x }$ is determined. We only need to save the elements with row indices greater than or equal to the first nonzero element in the $k$ th column of $R$

Now assume that the elements $c _ { i j }$ ， $( i , j ) \in \mathcal { K }$ , in columns $j = n , \ldots , k + 1$ have been computed. Then

$$
c _ { k k } = r _ { k k } ^ { - 1 } \left[ r _ { k k } ^ { - 1 } - \sum _ { j = k + 1 \atop ( k , j ) \in { \cal K } } ^ { n } r _ { k j } c _ { k j } \right] .
$$

Similarly, for $i = k - 1 , \ldots , f _ { k }$ ，

$$
c _ { i k } = - r _ { i i } ^ { - 1 } \left[ \sum _ { \substack { j = i + 1 } } ^ { k } r _ { i j } c _ { j k } + \sum _ { \substack { j = k + 1 } } ^ { n } r _ { i j } c _ { k j } \right] , \quad ( i , k ) \in \mathcal { K } .
$$

If the Cholesky factor $R$ has bandwidth $p$ , then the elements of $C _ { x }$ in the $p + 1$ bands of the upper triangular part of $C _ { x }$ can be computed by the above algorithm in about ${ \scriptstyle { \frac { 2 } { 3 } } } n p ( p + 1 )$ flops. An important particular case is when $R$ is bidiagonal. Computing the two diagonals of $C _ { x }$ then requires only about ${ \begin{array} { l } { { \frac { 4 } { 3 } } n } \end{array} }$ flops.

# 4.1.4 - QR Factorization of a Band Matrix

We now consider how to use the more stable Householder and Givens QR factorizations to solve banded least squares problems. In the standard Householder QR,we set $A ^ { ( 1 ) } = A$ and

$$
A ^ { ( k + 1 ) } = P _ { k } A ^ { ( k ) } , \quad k = 1 , \dots , n ,
$$

where the sequence of Householder reflections $P _ { k }$ is chosen to annihilate the subdiagonal ele-ments in the $k$ th column of $A ^ { ( k ) }$ . As shown by Reid [919, $1 9 6 7 ]$ this will cause each column in the remaining unreduced part of the matrix that has a nonzero inner product with the column being reduced to take on the sparsity pattern of their union. Hence, even though the final $R$ retains the bandwidth of $A$ ,large intermediate fll can take place with consequent cost in operations and storage. Thus, Householder QR factorization of a banded matrix $A \in \mathbb { R } ^ { m \times n }$ of bandwidth $w$ can require as much as 2mnw flops, and the intermediate storage required can exceed by a large amount that needed for the final factors.Note also that forming $Q$ explicitly should be avoided, because this factor may contain an order of magnitude more nonzero elements than either $A$ and $R$ .This rules out the use of MGS (modified Gram-Schmidt) for banded matrices.

For QR factorization of a band matrix, the order in which the rows are processed is critical for efficiency. We say that a band matrix $A$ is in standard form if its rows are ordered so that $f _ { i } ( A ) , i = 1 , 2 , \ldots , m$ , form a nondecreasing sequence

$$
i \leq k \Rightarrow f _ { i } ( A ) \leq f _ { k } ( A ) .
$$

A band matrix $A$ in standard form can be writen in partitioned form as

$$
A = \left( \begin{array} { c } { { A } } \\ { { A _ { 2 } } } \\ { { \vdots } } \\ { { \dot { A } _ { q } } } \end{array} \right) , \qquad b = \left( \begin{array} { c } { { b _ { 1 } } } \\ { { b _ { 2 } } } \\ { { \vdots } } \\ { { b _ { q } } } \end{array} \right) ,
$$

where $A _ { k } \in \mathbb { R } ^ { ( m _ { k } , n ) }$ and $m = m _ { 1 } + \cdot \cdot \cdot + m _ { q }$ Here $A _ { k }$ consists of all rows of $A$ for which the first nonzero element is in column $k$ ， $k = 1 , \ldots , q$ . The row ordering within the blocks $A _ { k }$ may be specified by sorting the rows so that the column indices $l _ { i } ( A _ { k } )$ within each block form a nondecreasing sequence. In many applications, $A$ is naturally given in standard form.

The structure of $A ^ { T } A$ , and therefore of $R$ ,can be generated as follows.

Theorem 4.1.7. Assume that $A \in \mathbb { R } ^ { m \times n }$ is a band matrix in standard form partitioned as in (4.1.17), and let $w _ { k }$ be the bandwidth of the block $A _ { k }$ . Then the band structure of the upper triangular Cholesky factor $R$ is given by $l _ { 1 } ( R ) = w _ { 1 }$ ，

$$
l _ { k } ( R ) = \operatorname* { m a x } \{ w _ { k } + k - 1 , l _ { k - 1 } ( R ) \} , \quad k = 2 , \ldots , q .
$$

Proof. The proof is by induction.

The first efficient QR algorithm for band matrices was given in Chapter 27 of Lawson and Hanson [727,1995]. It uses Householder transformations and assumes that $A$ is partitioned in the form (4.1.17). First, $R = R _ { 0 }$ is initialized to be an empty upper triangular matrix of bandwidth $w$ .The QR factorization proceeds in $q$ steps, $k = 1 , 2 , \ldots , q$ In step $k$ the $k$ th block $A _ { k }$ is merged as follows into the previously computed upper triangular $( R _ { k - 1 } , d _ { k - 1 } )$ by an orthogonal transformation:

$$
\begin{array} { r } { Q _ { k } ^ { T } \left( { \cal A } _ { k } ^ { } - 1 { \cal \Delta } _ { } \right) = \left( { \cal R } _ { k } ^ { } \right) , } \end{array}
$$

where $Q _ { k }$ is a product of Householder reflections giving an upper trapezoidal $R _ { k }$ .Note that this and later steps do not involve the first $k - 1$ rows and columns of $R _ { k - 1 }$ . Hence,at the beginning of step $k$ the first $k - 1$ rows of $R _ { k - 1 }$ are rows in the final matrix $R$ .At termination we have obtained $( R _ { q } , d _ { q } )$ such that $R _ { q } x = d _ { q }$ . This Householder algorithm uses a total of about $2 w ( w + 1 ) ( m + 3 n / 2 )$ fops,

Example 4.1.8. The least squares approximation of a discrete set of data by a linear combination of cubic B-splines is often used for smoothing noisy data values observed at $m$ distinct points; see Reinsch $[ 9 2 2 , 1 9 6 7 ]$ and Craven and Wahba [278,1979]. Let $\begin{array} { r } { s ( t ) = \sum _ { j = 1 } ^ { n } x _ { j } B _ { j } ( t ) } \end{array}$ where

$B _ { j } ( t ) , j = 1 , \ldots , n$ , be normalized cubic B-splines,and let $( y _ { i } , t _ { i } )$ ， $i = 1 , \ldots , m$ , be given data points. Determine $x$ to minimize

$$
\sum _ { i = 1 } ^ { m } ( s ( t _ { i } ) - y _ { i } ) ^ { 2 } = \| A x - y \| _ { 2 } ^ { 2 } .
$$

The only B-splines with nonzero values for $t \in [ \lambda _ { k - 1 } , \lambda _ { k } ]$ are $B _ { j }$ ， $j = k , k + 1 , k + 2 , k + 3$ Hence $A$ will be a band matrix with $w = 4$ .For a problem with $m = 1 7$ ， $n = 1 0$ ， $A$ consists of blocks $A _ { k }$ ， $k = 1 , \ldots , 7 .$ ，The Householder QR factorization is illustrated in Figure 4.1.1,where $A$ is shown after the first three blocks have been reduced by Householder reflections $P _ { 1 } , \ldots , P _ { 9 }$ Elements zeroed by $P _ { j }$ are denoted by $j$ and fill elements by $^ +$

We now describe an alternative algorithm using plane rotations for the QR factorization of a band matrix.

# Algorithm 4.1.2 (Sequential Givens QR Factorization).

Let $A \in \mathbb { R } ^ { m \times n }$ be a band matrix in standard form with row bandwidth w. Initialize $R = R _ { 0 }$ to be an upper triangular matrix of bandwidth w with zero elements. For $i = 1 , \ldots , m$ plane rotations are used to merge the ith row with $R _ { i - 1 }$ ，giving $R _ { i }$

$$
[ c , s ] = \operatorname { g i v r o t } ( r _ { j j } , a _ { i j } ) ;
$$

$$
\binom { r _ { j } ^ { T } } { a _ { i } ^ { T } } : = \left( \begin{array} { l l } { c } & { s } \\ { - s } & { c } \end{array} \right) \left( \begin{array} { l } { r _ { j } ^ { T } } \\ { a _ { i } ^ { T } } \end{array} \right) ;
$$

The reduction is shown schematically in Figure 4.1.1. The ith step only involves the $w \times w$ upper triangular part of $R _ { i - 1 }$ formed by rows and columns $f _ { i } ( A )$ to $l _ { i } ( A )$ . If at some stage $r _ { i i } = 0$ ,then the whole ith row in $R _ { i - 1 }$ must be zero,and the remaining part of the current row $a _ { i } ^ { T }$ can just be copied into row $i$ of $R _ { i - 1 }$

If $A$ has constant bandwidth and is in standard form, then at step $i$ the last $\left( n - l _ { i } ( A ) \right)$ columns of $R$ have not been touched and are still zero as initialized. Furthermore,at this stage the first $\left( f _ { i } ( A ) - 1 \right)$ rows are final rows of $R$ and can be saved on secondary storage. Since primary storage is only needed for the active triangular part, shown in Figure 4.1.2, very large problems can be handled. Clearly, the number of plane rotations needed to process the $i$ th row isatmost $\operatorname* { m i n } ( i - 1 , w )$ and requires at most $4 w ^ { 2 }$ flops. Hence, the complete factorization requires $4 m w ^ { 2 }$ flops, and $\scriptstyle { \frac { 1 } { 2 } } w ( w + 3 )$ locations of storage.We remark that if $A$ is not in standard form,then the operation count can only be bounded by 4mnw flops.

![](images/eee64f745374c9543834497f509aff633e2fbac0b9051fe4a4af6853cbb67e25.jpg)  
Figure 4.1.2. Reduction of a band matrix.

The solution to a band least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ is obtained by applying QR factorization to the extended matrix $( A b )$ . The solution is then obtained from a band upper triangular system $R x = c _ { 1 }$ . In order to treat additional right-hand sides not available at the time of factorization,the plane rotations from the QR factorization need to be saved.As described in Section 2.2.1,a plane rotation can be represented by a single floating-point number. Since at most $w$ rotations are needed to process each row, it follows that $Q$ can be stored in no more space than that allocated for $A$

# 4.2 - Bidiagonalization

# 4.2.1 - Bidiagonal Decomposition

For a general $m \times n$ matrix $A$ ,the closest-to-diagonal form that can be achieved in a finite number of operations is a bidiagonal form. Golub and Kahan [495,1965] show that this form can be obtained by a sequence of two-sided Householder reflections $B = U ^ { T } A V$ ，where $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ are orthogonal. This preserves the singular values of $A$ ,and the singular vectors of $B$ are closely related to those of $A$ .Householder bidiagonalization (HHBD) is often the first step toward computing the SVD (singular value decomposition); see Section 7.1.1.

Theorem 4.2.1 (HHBD). For any matrix $A \in \mathbb { R } ^ { m \times n }$ , orthogonal matrices $U = ( u _ { 1 } , \ldots , u _ { m } ) \in$ $\mathbb { R } ^ { m \times m }$ and $V = ( v _ { 1 } , \ldots , v _ { n } ) \in \mathbb { R } ^ { n \times n }$ can be found such that $U ^ { T } A V$ is upper bidiagonal. If $m \geq n$ ,then

$$
U ^ { T } A V = \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) , \quad B = \left( \begin{array} { l l l l l } { \beta _ { 1 } } & { \alpha _ { 2 } } & & & \\ & { \beta _ { 2 } } & { \alpha _ { 3 } } & & \\ & & { \ddots } & { \ddots } & \\ & & & { \beta _ { p - 1 } } & { \alpha _ { p } } \\ & & & & { \beta _ { p } } \end{array} \right) \in \mathbb { R } ^ { p \times p } ,
$$

where $\beta _ { i } \ \ge \ 0 , \ \alpha _ { i } \ \ge \ 0 ,$ and $\textit { p } = \textit { n }$ if $m \ < \ n$ ，then $U ^ { T } A V = \left( \begin{array} { c c } { { B } } & { { 0 } } \end{array} \right)$ ，where $p \ = \ m$ B ∈ Rpx(p+1),and Bep+1 = ap+1ep.

Proof. $U$ and $V$ are constructed as products of Householder reflectors $Q _ { k } \in \mathbb { R } ^ { m \times m }$ from the left and $P _ { k } \in \mathbb { R } ^ { n \times n }$ ， $k = 1 , \hdots , p$ , from the right, applied alternately to $A$ .Here $Q _ { k }$ is chosen to zero out all elements in the $k$ th column below the main diagonal,and $P _ { k }$ is chosen to zero out all elements in the $k$ th row to the right of $B$ .First, $Q _ { 1 }$ is applied to $A$ to zero out all elements, except one in the first column of $Q _ { 1 } A$ .When $P _ { 1 }$ is next applied to zero out the elements in the first row not in $B$ ,the first column in $Q _ { 1 } A$ is left unchanged. These two transformations determine $\beta _ { 1 }$ and $\alpha _ { 2 }$ . All later steps are similar. With $A ^ { ( 1 ) } = \bar { A }$ set $A ^ { ( k + 1 ) } = ( Q _ { k } A ^ { ( k ) } ) P _ { k }$ . This determines not only the bidiagonal elements $\beta _ { k }$ and $\alpha _ { k + 1 }$ in the $k$ th row of $B$ but also the $k$ th columns in $U$ and $V$ ：

$$
u _ { k } = U e _ { k } = Q _ { 1 } \ldots Q _ { k } e _ { k } , \qquad v _ { k } = V e _ { k } = P _ { 1 } \ldots P _ { k } e _ { k } , \quad k = 1 , \ldots , p .
$$

Here, some of the transformations may be skipped. For example, if $m = n$ ,then $Q _ { n } = I _ { n }$ and $P _ { n - 1 } = P _ { n } = I _ { n }$ . Similarly,a complex matrix $A \in \mathbb { C } ^ { m \times n }$ can be reduced to real bidiagonal form using a sequence of complex Householder reflections. □

By applying the HHBD algorithm of Theorem 4.2.1 to $A ^ { T }$ , any matrix $A \in \mathbb { R } ^ { m \times n }$ can be transformed into lower bidiagonal form. (This is equivalent to starting the reduction of $A$ with a right transformation $P _ { 1 }$ instead of with $Q _ { 1 }$ .）

HHBD requires approximately $4 ( m n ^ { 2 } - { \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } )$ flops or roughly twice as many as needed for Householder QR factorization. If the matrices $U _ { p } = ( u _ { 1 } , \ldots , u _ { p } )$ and/or $V _ { p } = ( v _ { 1 } , \ldots , v _ { p } )$ are wanted,the corresponding products of Householder reflections can be accumulated at a cost of $2 ( m n ^ { 2 } - { \textstyle \frac { 1 } { 3 } } n ^ { 3 } ) $ and ${ \scriptstyle { \frac { 4 } { 3 } } } n ^ { 3 }$ fops, respectively. For a square matrix, these counts are ${ \scriptstyle { \frac { 8 } { 3 } } } n ^ { 3 }$ for the reduction and ${ \scriptstyle { \frac { 4 } { 3 } } } n ^ { 3 }$ for computing each of the matrices $U$ and $V$

HHBD is a backward stable algorithm, i.e.,the computed matrix $B$ is the exact result for a matrix $A + E$ ,where

$$
\| E \| _ { F } \leq c n ^ { 2 } \mathbf { u } \| A \| _ { F } ,
$$

and $c$ is a constant of order unity. Further,if the stored Householder vectors are used to generate $U$ and $V$ explicitly, the computed matrices are close to the exact matrices $U$ and $V$ that reduce $A + E$ . This guarantees that the computed singular values of $B$ and the transformed singular vectors of $B$ are those of a matrix close to $A$

An alternative two-step reduction to bidiagonal form was suggested by Lawson and Han-son [727,1995l and later analyzed by T. Chan [222,1982]. This first computes the pivoted QR factorization

$$
A P = Q \left( { \begin{array} { c } { R } \\ { 0 } \end{array} } \right)
$$

and then transforms the upper triangular $R \in \mathbb { R } ^ { n \times n }$ into bidiagonal form. Column pivoting in the initial QR factorization makes the two-step algorithm potentially more accurate. Householder bidiagonalization cannot take advantage of the triangular structure of $R$ ,but with plane rotations it can be done.In the first step the elements $r _ { 1 n } , \ldots , r _ { 1 3 }$ in the first row are annihilated in this order. To zero out element $r _ { 1 j }$ a plane rotation $G _ { j - 1 , j }$ is first applied from the right.This introduces a new nonzero element ${ r _ { j , j - 1 } }$ , which is annihilated by a rotation $\tilde { G } _ { j - 1 , j }$ from the left. The first few rotations in the process are pictured below. (Recall that $\oplus$ denotes the element to be zeroed,and fill-in elements are denoted by $^ +$ ）

$$
\left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \oplus } \\ { \times } & { \times } & { \times } & { \times } & { \oplus } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & { + } & { \times } & { \to } \end{array} } \right) \Rightarrow \quad \left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { 0 } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & & { \times } & { \times } \\ & & & { \oplus } & { \times } \end{array} } \right) \Rightarrow \quad \left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \oplus } & { 0 } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & { + } & { \times } & { \times } \\ & & { 0 } & { \times } \end{array} } \right) .
$$

Two plane rotations are needed to zero each element. The total cost is $6 n$ flops,and the operation count for the reduction of $R$ to bidiagonal form is $2 n ^ { 3 }$ flops and lower than for the Householder algorithm. However, if the product of either the left or right transformation is needed, then Householder reduction requires less work; see Chan [222,1982]. A similar “zero chasing" technique can be used to reduce the bandwidth of an upper triangular band matrix while preserving the band structure; see Golub,Luk,and Overton [498,1981].

The bidiagonal decomposition is a powerful tool for analyzing and solving least squares problems. Let $U ^ { T } A V = C$ ,where $U$ and $V$ are square orthogonal matrices. Then the pseudoinverses of $A$ and $C$ are related as $A ^ { \dagger } = V C ^ { \dagger } U ^ { T }$ ,and the pseudoinverse solution is

$$
x = A ^ { \dagger } b = V ( C ^ { \dagger } ( U ^ { T } b ) ) .
$$

In particular, consider the HHBD algorithm with $A \in \mathbb { R } ^ { m \times n }$ $m \ge n = \operatorname { r a n k } ( A )$ Setting $x = V y$ and using the orthogonal invariance of the 2-norm, we have

$$
\begin{array} { r l } & { \| A x - b \| _ { 2 } ^ { 2 } = \| U ^ { T } A V y - U ^ { T } b \| _ { 2 } ^ { 2 } = \bigg \| \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) y - \left( \begin{array} { l } { c } \\ { d } \end{array} \right) \bigg \| _ { 2 } ^ { 2 } } \\ & { \qquad = \| B y - c \| _ { 2 } ^ { 2 } + \| d \| _ { 2 } ^ { 2 } . } \end{array}
$$

Clearly, the minimum of $\| A x - b \| _ { 2 } ^ { 2 }$ is obtained when $\mathit { B y } \ : = \ : c$ ，The least squares solution $x = V y = P _ { 1 } \cdot \cdot \cdot P _ { n - 2 } y$ is computed by forming $U ^ { T } b = Q _ { n } \cdot \cdot \cdot Q _ { 1 } b$ and solving $B y = c$ by back-substitution:

$$
y _ { n } = c _ { n } / \beta _ { n } , y _ { k } = ( c _ { k } - \alpha _ { k + 1 } c _ { k - 1 } ) / \beta _ { k } , k = n - 1 : - 1 : 1 .
$$

This takes $2 ( m n + n ^ { 2 } )$ flops. Computing the residual vector

$$
r = Q _ { 1 } \cdot \cdot \cdot Q _ { n } \binom { 0 } { d }
$$

needs an additional $4 m n - 2 n ^ { 2 }$ flops. Computing $r = b - A x$ directly requires mn flops.

To be efficient on modern computers,a blocked version of Householder bidiagonalization is needed.This poses new diffculties that are not present in the blocked Householder QR factorization described in Section 2.6.1.A blocked implementation of Householder bidiagonalization is given by Dongarra, Sorensen,and Hammarling [327,1989l; see also Dongarra et al. [323, 2018,Algorithm 1]. Householder reflectors $H _ { k } = I - \tau _ { k } v _ { k } v _ { k } ^ { T }$ are used to eliminate elements below the diagonal in column $k$ ，while $G _ { k } = I - \pi _ { k } u _ { k } u _ { k } ^ { T }$ eliminate elements to the right of the superdiagonal in row $k$ ：

$$
\begin{array} { r l } & { A ^ { ( k ) } = H _ { k } A ^ { ( k - 1 ) } G _ { k } = ( I - \tau _ { k } v _ { k } v _ { k } ^ { T } ) A ^ { ( k - 1 ) } ( I - \pi _ { k } u _ { k } u _ { k } ^ { T } ) } \\ & { \qquad = A ^ { ( k - 1 ) } - v _ { k } y _ { k } ^ { T } - z _ { k } u _ { k } ^ { T } , } \end{array}
$$

where $y _ { k } = \tau _ { k } ( A ^ { ( k - 1 ) } ) ^ { T } v _ { k }$ and $z _ { k } = \pi _ { k } ( A ^ { ( k - 1 ) } u _ { k } - ( y _ { k } ^ { T } u _ { k } ) v _ { k } )$ . Blocking together $p$ applications gives

$$
A ^ { ( p ) } = H _ { p } \cdot \cdot \cdot H _ { 1 } A G _ { 1 } \cdot \cdot \cdot G _ { p } = A - V _ { p } Y _ { p } ^ { T } - X _ { p } U _ { p } ^ { T } .
$$

To determine $H _ { k }$ it suffices to update column $k$ of the trailing matrix $A ^ { ( k - 1 ) }$ ,and $G _ { k }$ can be determined after row $i$ of $H _ { k } A ^ { ( k - 1 ) }$ is updated. The remaining update of the trailing matrix can be delayed, but each step still requires two matrix-vector products involving the full trailing matrix. If $m = n$ ,then about one half of the total $8 n ^ { 3 } / 3$ flops in the decomposition will be matrix-vector and the other half matrix-matrix operations.

# Notes and references

Ralha [909,2oo3] developed a one-sided bidiagonalization algorithm that starts by computing the factorization $F = A V$ . Here $V$ is a product of Householder reflections chosen so that $T = V ^ { T } A ^ { T } A V$ is tridiagonal but without explicitly forming $A ^ { T } A$ Next, a Gram-Schmidt QR of $F$ is used to compute $F = A V = U B$ ，where $B$ is upper bidiagonal. Ralha's algorithm uses fewer arithmetic operations than the two-sided Householder algorithm but lacks numerical stability. A modified backward stable version of Ralha's algorithm was developed by Barlow, Bosner,and Drmac [71, 2005].

# 4.2.2 - Core Problems by Bidiagonalization

Consider the least squares problem

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } .
$$

Suppose $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ can be found so that

$$
U ^ { T } \left( \textit { b } | \textit { A V } \right) = \left( \begin{array} { c } { c _ { 1 } } \\ { 0 } \end{array} \bigg | \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) .
$$

Setting $x = V y$ ,the problem splits (4.2.8) into two independent approximation subproblems

$$
\operatorname* { m i n } _ { y _ { 1 } } \| A _ { 1 1 } y _ { 1 } - c _ { 1 } \| _ { 2 } , \quad \operatorname* { m i n } _ { y _ { 2 } } \| A _ { 2 2 } y _ { 2 } \| _ { 2 } , \quad y = \left( { y _ { 1 } } \atop { y _ { 2 } } \right) ,
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ may be rectangular. Clearly, the solution to the second subproblem is $y _ { 2 } = 0$ Hence,all information needed for solving the original approximation problem is contained in the first subproblem. The pseudoinverse solution $x ^ { \dagger }$ of the original problem (4.2.8) is related to the pseudoinverse solution $y ^ { \dagger }$ of the transformed problem (4.2.10) by

$$
x ^ { \dagger } = V _ { 1 } y _ { 1 } ^ { \dagger } , \quad V = \left( V _ { 1 } \quad V _ { 2 } \right) .
$$

Paige and Strakos [868, 2oo6] state the following definition.

Definition 4.2.2. The subproblem $\operatorname* { m i n } _ { y } \| A _ { 1 1 } y - c _ { 1 } \| _ { 2 }$ in (4.2.10) is said to be a core problem of $\operatorname* { m i n } _ { x }$ $\| A x - b \| _ { 2 }$ if $A _ { 1 1 }$ is minimally dimensioned for all orthogonal $U$ and $V$ that give the form (4.2.9).

We now show that a core subproblem can be found by bidiagonalization of the compound matrix $\left( \begin{array} { l l } { b } & { A } \end{array} \right)$ ，where $A \in \mathbb { R } ^ { m \times n }$ ， $m > n$ (Note that here $b$ is placed in front of $A$ contrary to our previous practice!) This yields an upper bidiagonal decomposition $U ^ { T } \left( \textit { b } | \textit { A } \right) \widetilde { V }$ Because $\widetilde { V }$ does not act on the first column $b$ , we can write

$$
U ^ { T } (  \ b \ | \ A \ ) ( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} ) = ( \ \beta _ { 1 } e _ { 1 } \ | \ U ^ { T } A V \ ) .
$$

Hence $U ^ { T } b = \beta _ { 1 } e _ { 1 }$ ， so that $\beta _ { 1 } = \| b \| _ { 2 }$ and $u _ { 1 } = U e _ { 1 } = b / \beta _ { 1 }$ .Further, we have the lower bidiagonal decomposition,

$$
U ^ { T } A V = { \binom { B } { 0 } } , \quad B = \left( { \begin{array} { c c c c c } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \ddots } & { \ddots } & & \\ & & { \beta _ { n } } & { \alpha _ { n } } \\ & & & & { \beta _ { n + 1 } } \end{array} } \right) \in \mathbb { R } ^ { ( n + 1 ) \times n } .
$$

The bidiagonalization process is terminated when the first zero bidiagonal element in $B$ is encountered. Then a core problem has been found. There are two possible cases. If $\alpha _ { k } > 0$ but $\beta _ { k + 1 } = 0$ ， $k \leq n$ , then the transformed matrix splits as follows:

$$
U ^ { T } \left( \textit { b } | \textit { A V } \right) = \left( \begin{array} { c c } { \beta _ { 1 } e _ { 1 } } \\ { 0 } \end{array} \left| \begin{array} { c c } { B _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} \right. \right) ,
$$

where

$$
B _ { 1 1 } = \left( \begin{array} { l l l l } { \alpha _ { 1 } } & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & \\ & { \ddots } & { \ddots } & \\ & & { \beta _ { k } } & { \alpha _ { k } } \end{array} \right) \in \mathbb { R } ^ { k \times k }
$$

has full row rank, and $A _ { 2 2 }$ is the part of $A$ that is not yet in bidiagonal form. The pseudoinverse solution $x = V y$ is now found by solving the square nonsingular lower bidiagonal core system

$$
B _ { 1 1 } y _ { 1 } = \beta _ { 1 } e _ { 1 }
$$

and setting $x ^ { \dagger } = V _ { 1 } y _ { 1 }$ ; see (4.2.11). Because the residual for (4.2.16) is zero,it follows that the original system $A x = b$ must be consistent.

If instead the bidiagonalization terminates with $\beta _ { k + 1 } ~ > ~ 0$ and $\alpha _ { k + 1 } = 0$ ，then the firs columns of the transformed matrix split with a rectangular lower bidiagonal matrix of ful :olumn rank,

$$
B _ { 1 1 } = \left( \begin{array} { l l l l l } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \ddots } & { \ddots } & & \\ & & { \beta _ { k } } & { \alpha _ { k } } \\ & & & & { \beta _ { k + 1 } } \end{array} \right) \in \mathbb { R } ^ { { ( k + 1 ) } \times { k } } .
$$