and

$$
\begin{array} { r l } & { \mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 2 } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { d } . } \end{array}
$$

This solution is unique, but cannot fit general data exactly. As with (3.38), it is better in practice to use the generalized inverse solution than to use (3.47) because of numerical accuracy issues.

4. $p < m$ and $p < n$ Both $N ( \mathbf G ^ { T } )$ and $N ( \mathbf G )$ are nontrivial. In this case, the generali-zed inverse solution encapsulates the behavior of both of the two previous cases, minimizing both $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ and $\| \mathbf { m } \| _ { 2 }$

As in case 3,

$$
\begin{array} { r l } & { \mathbf { G m } _ { \dagger } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathrm { p r o j } _ { R ( \mathbf { G } ) } \mathbf { d } . } \end{array}
$$

Thus $\mathbf { m } _ { \dagger }$ is a least squares solution to $\mathbf { G m } = \mathbf { d }$

As in case 2 we can write the model and its norm using (3.33) and (3.34). Thus $\mathbf { m } _ { \dagger }$ is the least squares solution of minimum length.

We have shown that the generalized inverse provides an inverse solution (3.22) that always exists,is both least squares and minimum length,and properly accommodates the rank and dimensions of $\mathbf { G }$ .Relationships between the subspaces $R ( \mathbf G )$ ， $N ( \mathbf G ^ { T } )$ ， $R ( \mathbf G ^ { T } )$ ， $N ( \mathbf G )$ , and the operators $\mathbf { G }$ and $\mathbf { G } ^ { \dagger }$ , are schematically depicted in Figure 3.1. Table 3.1 summarizes the SVD and its properties.

The existence of a nontrivial model null space (one that includes more than just the zero vector) is at the heart of solution nonuniquenes. There are an infinite number of solutions that will fit the data equally well, because model components in $N ( \mathbf G )$ have no effect on data fit. To select a particular preferred solution from this infinite set thus requires more constraints (such as minimum length or smoothing constraints) than are encoded in the matrix $\mathbf { G }$

Table 3.1 Summary of the SVD and its associated scalars and matrices.   

<table><tr><td>Object</td><td>Size</td><td>Properties</td></tr><tr><td>p</td><td>scalar</td><td>rank(G)= p; Number of nonzero singular values</td></tr><tr><td>m</td><td>scalar</td><td>Dimension of the data space</td></tr><tr><td>n</td><td>scalar</td><td>Dimension of the model space</td></tr><tr><td>G</td><td>m by n</td><td></td></tr><tr><td>U</td><td>m by m</td><td>Orthogonal matrix; U= [Up, Uo]</td></tr><tr><td>Si</td><td>scalar</td><td>ith singular value</td></tr><tr><td>S</td><td>m by n</td><td>Diagonal matrix of singular values; Si,i = si</td></tr><tr><td>V</td><td>n by n</td><td>Orthogonal matrix; V= [Vp, Vo]</td></tr><tr><td>Up</td><td>m by p</td><td>Columns form a basis for R(G)</td></tr><tr><td>Sp</td><td>p by p</td><td>Diagonal matrix of nonzero singular values</td></tr><tr><td>Vp</td><td>n by p</td><td>Columns form an orthonormal basis for R(GT)</td></tr><tr><td>Uo</td><td>m by m-p</td><td>Columns form an orthonormal basis for N(GT)</td></tr><tr><td>Vo</td><td>n by n-p</td><td>Columns form an orthonormal basis for N(G)</td></tr><tr><td>U.,i</td><td>m by 1</td><td>Eigenvector of GGT with eigenvalue s2</td></tr><tr><td>V.i Gf</td><td>n by 1</td><td></td></tr><tr><td></td><td>n by m</td><td>Pseudoinverse of G; G† = VpS-1UT p</td></tr><tr><td>mt</td><td>m by 1</td><td>Generalized inverse solution; m† = G†d</td></tr></table>

To see the significance of the $N ( \mathbf G ^ { T } )$ subspace, consider an arbitrary data vector, $\mathbf { d } _ { \mathrm { 0 } }$ ， which lies in $N ( \mathbf G ^ { T } )$ ：

$$
{ \bf d } _ { 0 } = \sum _ { i = p + 1 } ^ { m } \beta _ { i } { \bf U } . _ { , i } .
$$

The generalized inverse operating on such a data vector gives

$$
\begin{array} { r l } & { \mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } _ { 0 } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \displaystyle \sum _ { i = p + 1 } ^ { n } \beta _ { i } \mathbf { U } _ { p } ^ { T } \mathbf { U } _ { \cdot , i } = \mathbf { 0 } } \end{array}
$$

because the $\mathbf { U } _ { \cdot , i }$ are orthogonal. $N ( \mathbf G ^ { T } )$ is a subspace of $R ^ { m }$ consisting of all vectors $\mathbf { d } _ { 0 }$ that have no influence on the generalized inverse model, $\mathbf { m } _ { \dagger }$ .If $p < n$ ，there are an infinite number of potential data sets that will produce the same model when (3.22) is applied.

# 3.2.COVARIANCE AND RESOLUTION OF THE GENERALIZED INVERSE SOLUTION

The generalized inverse always gives us a solution, $\mathbf { m } _ { \dagger }$ , with well-determined properties, but it is essential to investigate how faithful a representation any model is likely to be of the true situation.

In Chapter 2, we found that under the assumption of independent and normally distributed measurement errors with constant standard deviation, the least squares solution was an unbiased estimator of the true model, and that the estimated model parameters had a multivariate normal distribution with covariance

$$
\begin{array} { r } { \mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = \sigma ^ { 2 } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } . } \end{array}
$$

We can attempt the same analysis for the generalized inverse solution $\mathbf { m } \dagger$ . The covariance matrix would be given by

$$
\begin{array} { l } { \displaystyle \mathrm { C o v } ( { \bf m } _ { \dagger } ) = { \bf G } ^ { \dagger } \mathrm { C o v } ( { \bf d } ) ( { \bf G } ^ { \dagger } ) ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } { \bf G } ^ { \dagger } ( { \bf G } ^ { \dagger } ) ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } { \bf V } _ { p } \mathbb { S } _ { p } ^ { - 2 } { \bf V } _ { p } ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } \sum _ { i = 1 } ^ { p } \frac { V _ { \cdot , i } V _ { \cdot , i } ^ { T } } { s _ { i } ^ { 2 } } . } \end{array}
$$

Since the $s _ { i }$ are decreasing, successive terms in this sum make larger and larger contributions to the covariance. If we were to truncate (3.58), we could actually decrease the variance in our model estimate! This is discussed further in Section 3.3.

Unfortunately, unless ${ \boldsymbol { p } } = n$ ,the generalized inverse solution is not an unbiased estimator of the true solution. This occurs because the true solution may have nonzero projections onto those basis vectors in $\mathbf { v }$ that are unused in the generalized inverse solu-tion. In practice, the bias introduced by restricting the solution to the subspace spanned by the columns of $\mathbf { V } _ { p }$ may be far larger than the uncertainty due to measurement error.

The concept of model resolution is an important way to characterize the bias of the generalized inverse solution. In this approach we see how closely the generalized inverse solution matches a given model, assuming that there are no errors in the data. We begin with a model $\mathbf { m } _ { \mathrm { t r u e } }$ . By multiplying $\mathbf { G }$ times $\mathbf { m _ { \mathrm { t r u e } } }$ , we can find a corresponding data vector $\mathbf { d } _ { \mathrm { t r u e } }$ . If we then multiply $\mathbf { G } ^ { \dagger }$ times ${ \bf d } _ { \mathrm { t r u e } }$ ,we obtain a generalized inverse solution

$$
\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { G m } _ { \mathrm { t r u e } } .
$$

We would obviously like to recover the original model, so that $\mathbf { m } ^ { \dagger } = \mathbf { m } _ { \mathrm { { t r u e } } }$ . However, because $\mathbf { m } _ { \mathrm { t r u e } }$ may have had a nonzero projection onto the model null space

$N ( \mathbf G )$ ， $\mathbf { m } _ { \dagger }$ will not in general be equal to $\mathbf { m _ { \mathrm { t r u e } } }$ . The model resolution matrix that characterizes this effect is

$$
\begin{array} { r l } & { \mathbf { R } _ { \mathrm { m } } = \mathbf { G } ^ { \dagger } \mathbf { G } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { V } _ { p } ^ { T } . } \end{array}
$$

If $N ( \mathbf G )$ is trivial, then $\operatorname { r a n k } ( \mathbf G ) = p = n$ and $\mathbf { R } _ { \mathrm { m } }$ is the $n$ by $n$ identity matrix. In this case the original model is recovered exactly and we say that the resolution is perfect. If $N ( \mathbf G )$ is a nontrivial subspace of $R ^ { n }$ ，then $p = { \mathrm { r a n k } } ( \mathbf G ) < n$ ，so that $\mathbf { R } _ { \mathrm { m } }$ is not the identity matrix. The model resolution matrix is instead a nonidentity symmetric matrix that characterizes how the generalized inverse solution smears out the original model, $\mathbf { m _ { \mathrm { t r u e } } }$ , into a recovered model, $\mathbf { m } _ { \dagger }$ . The trace of $\mathbf { R } _ { \mathrm { m } }$ is often used as a simple quantitative measure of the resolution. If $\operatorname { T r } ( \mathbf { R } _ { \mathrm { m } } )$ is close to $n$ ，then $\mathbf { R } _ { \mathrm { m } }$ is relatively close to the identity matrix.

The model resolution matrix can be used to quantify the bias introduced by the pseudoinverse when $\mathbf { G }$ does not have full column rank. We begin by showing that the expected value of $\mathbf { m } _ { \dagger }$ is $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$

$$
\begin{array} { r l } & { E [ \mathbf { m } _ { \dagger } ] = E [ \mathbf { G } ^ { \dagger } \mathbf { d } ] } \\ & { \qquad = \mathbf { G } ^ { \dagger } E [ \mathbf { d } ] } \\ & { \qquad = \mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } } } \\ & { \qquad = \mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } } . } \end{array}
$$

Thus the bias in the generalized inverse solution is

$$
\begin{array} { r } { E [ \mathbf { m } _ { \dagger } ] - \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { \mathrm { t r u e } } } \\ { = ( \mathbf { R } _ { \mathrm { m } } - \mathbf { I } ) \mathbf { m } _ { \mathrm { t r u e } } \quad } \end{array}
$$

where

$$
\begin{array} { c } { { { \bf R } _ { \mathrm { m } } - { \bf I } = { \bf V } _ { p } { \bf V } _ { p } ^ { T } - { \bf V } { \bf V } ^ { T } } } \\ { { = - { \bf V } _ { 0 } { \bf V } _ { 0 } ^ { T } . } } \end{array}
$$

We can formulate a bound on the norm of the bias using (3.68) as

$$
\begin{array} { r } { \| E [ \mathbf { m } _ { \dagger } ] - \mathbf { m } _ { \mathrm { t r u e } } \| \leq \| \mathbf { R } _ { \mathrm { m } } - \mathbf { I } \| \| \mathbf { m } _ { \mathrm { t r u e } } \| . } \end{array}
$$

$\| \mathbf { R } _ { \mathrm { m } } - \mathbf { I } \|$ thus characterizes the bias introduced by the generalized inverse solution. However, the detailed effects of limited resolution on the recovered model will depend on $\| \mathbf { m } _ { \mathrm { t r u e } } \|$ , about which we may have quite limited a priori knowledge.

In practice, the model resolution matrix is commonly used in two different ways. First,we can examine diagonal elements of $\mathbf { R } _ { \mathrm { m } }$ . Diagonal elements that are close to one correspond to parameters for which we can claim good resolution. Conversely, if any of the diagonal elements are small, then the corresponding model parameters will be poorly resolved. Second,we can multiply $\mathbf { R } _ { \mathrm { m } }$ times a particular test model m to see how that model would be resolved by the inverse solution. This strategy is called a resolution test. One commonly used test model is a spike model, which is a vector with all zero elements,except for a single entry which is one.Multiplying $\mathbf { R } _ { \mathrm { m } }$ times a spike model effectively picks out the corresponding column of the resolution matrix. These columns of the resolution matrix are called resolution kernels. Such functions are also similar to the averaging kernels in the method of Backus and Gilbert discussed in Chapter 5.

We can multiply $\mathbf { G } ^ { \dagger }$ and $\mathbf { G }$ in the opposite order from (3.62) to obtain the data space resolution matrix, $\mathbf { R } _ { \mathrm { d } }$

$$
\begin{array} { c } { \mathbf { d } _ { \dagger } = \mathbf { G m } _ { \dagger } } \\ { \mathbf { \Lambda } = \mathbf { G G } ^ { \dagger } \mathbf { d } } \\ { \mathbf { \Lambda } = \mathbf { R } _ { \mathrm { d } } \mathbf { d } } \end{array}
$$

where

$$
\begin{array} { r } { \mathbf { R } _ { \mathrm { d } } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } } \\ { = \mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } . \qquad } \end{array}
$$

If $N ( \mathbf G ^ { T } )$ contains only the zero vector, then $p = m$ ,and $\mathbf { R } _ { \mathrm { d } } = \mathbf { I }$ In this case, $\mathbf { d } _ { \dagger } = \mathbf { d }$ and the generalized inverse solution $\mathbf { m } \dagger$ fits the data exactly. However, if $N ( \mathbf G ^ { T } )$ is nontrivial, then $p < m$ and $\mathbf { R } _ { \mathrm { d } }$ is not the identity matrix. In this case $\mathbf { m } _ { \dagger }$ does not exactly fit the data.

Note that model and data space resolution matrices (3.62) and (3.76) do not depend on specific data or models, but are exclusively properties of $\mathbf { G }$ .They reflect the physics and geometry of a problem,and can thus be assessed during the design phase of an experiment.

# 3.3.INSTABILITY OF THE GENERALIZED INVERSE SOLUTION

The generalized inverse solution $\mathbf { m } _ { \dagger }$ has zero projection onto $N ( \mathbf G )$ . However, it may include terms involving column vectors in $\mathbf { V } _ { p }$ with very small nonzero singular values. In analyzing the generalized inverse solution it is useful to examine the singular value spectrum, which is simply the range of singular values. Small singular values cause the generalized inverse solution to be extremely sensitive to small amounts of noise in the data.As a practical matter, it can also be difficult to distinguish between zero singular values and extremely small singular values. We can quantify the instabilities created by small singular values by recasting the generalized inverse solution to make the effect of small singular values explicit. We start with the formula for the generalized inverse solution,

$$
\begin{array} { r } { \mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } . } \end{array}
$$

The elements of the vector $\mathbf { U } _ { p } ^ { T } \mathbf { d }$ are the dot products of the first $p$ columns of $\mathbf { U }$ with d

$$
\mathbf { U } _ { p } ^ { T } \mathbf { d } = \left[ \begin{array} { c } { ( \mathbf { U } _ { \cdot , 1 } ) ^ { T } \mathbf { d } } \\ { ( \mathbf { U } _ { \cdot , 2 } ) ^ { T } \mathbf { d } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { ( \mathbf { U } _ { \cdot , p } ) ^ { T } \mathbf { d } } \end{array} \right] .
$$

When we left-multiply $\mathbf { S } _ { p } ^ { - 1 }$ times (3.78), we obtain

$$
\mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \left[ \begin{array} { c } { \frac { ( \mathbf { U } _ { \cdot , 1 } ) ^ { T } \mathbf { d } } { s _ { 1 } } } \\ { \frac { ( \mathbf { U } _ { \cdot , 2 } ) ^ { T } \mathbf { d } } { s _ { 2 } } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { \frac { ( \mathbf { U } _ { \cdot , p } ) ^ { T } \mathbf { d } } { s _ { p } } } \end{array} \right] .
$$

Finally, when we left-multiply $\mathbf { V } _ { p }$ times (3.79),we obtain a linear combination of the columns of $\mathbf { V } _ { p }$ that can be written as

$$
\mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \sum _ { i = 1 } ^ { p } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i } .
$$

In the presence of random noise, $\mathbf { d }$ will generally have a nonzero projection onto each of the directions specified by the columns of $\mathbf { U }$ .The presence of a very small $s _ { i }$ in the denominator of (3.8O) can thus give us a very large coefficient for the corresponding model space basis vector $\mathbf { V } _ { \cdot , i }$ ,and these basis vectors can dominate the solution.In the worst case,the generalized inverse solution is just a noise amplifier,and the answer is practically useless.

A measure of the instability of the solution is the condition number. Note that the condition number considered here for an $m$ by $n$ matrix is a generalization of the condition number for an $n$ by $n$ matrix (A.1O7),and the two formulations are equivalent when $m = n$

Suppose that we have a data vector $\mathbf { d }$ and an associated generalized inverse solution $\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d }$ . If we consider a slightly perturbed data vector $\mathbf { d } ^ { \prime }$ and its associated generalized inverse solution $\mathbf { m } _ { \dagger } ^ { \prime } = \mathbf { G } ^ { \dagger } \mathbf { d } ^ { \prime }$ ，then

$$
\mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } = \mathbf { G } ^ { \dagger } ( \mathbf { d } - \mathbf { d } ^ { \prime } )
$$

and

$$
\lVert \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \rVert _ { 2 } \leq \lVert \mathbf { G } ^ { \dagger } \rVert _ { 2 } \lVert \mathbf { d } - \mathbf { d } ^ { \prime } \rVert _ { 2 } .
$$

From (3.8O), it is clear that the largest difference in the inverse models will occur when $\mathbf { d } - \mathbf { d } ^ { \prime }$ is in the direction $\mathbf { U } _ { \cdot , p }$ If

$$
\mathbf { d } - \mathbf { d } ^ { \prime } = \alpha \mathbf { U } _ { \cdot , p } ,
$$

then

$$
\|  { \mathbf { d } } -  { \mathbf { d } } ^ { \prime } \| _ { 2 } = \alpha .
$$

We can then compute the effect on the generalized inverse solution as

$$
\mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } = \frac { \alpha } { s _ { p } } \mathbf { V } _ { \cdot , p }
$$

with

$$
\| \mathbf { m } _ { \dag } - \mathbf { m } _ { \dag } ^ { \prime } \| _ { 2 } = \frac { \alpha } { s _ { p } } .
$$

Thus,we have a bound on the instability of the generalized inverse solution

$$
\| \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \| _ { 2 } \leq \frac { 1 } { s _ { p } } \| \mathbf { d } - \mathbf { d } ^ { \prime } \| _ { 2 } .
$$

Similarly, we can see that the generalized inverse model is smallest in norm when d points in a direction parallel to $\mathbf { V } _ { \cdot , 1 }$ . Thus

$$
\| \mathbf { m } _ { \dagger } \| _ { 2 } \geq \frac { 1 } { s _ { 1 } } \| \mathbf { d } \| _ { 2 } .
$$

Combining these inequalities, we obtain

$$
\frac { \| \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \| _ { 2 } } { \| \mathbf { m } _ { \dagger } \| _ { 2 } } \leq \frac { s _ { 1 } } { s _ { p } } \frac { \| \mathbf { d } - \mathbf { d } ^ { \prime } \| _ { 2 } } { \| \mathbf { d } \| _ { 2 } } .
$$

The bound (3.89) is applicable to pseudoinverse solutions, regardless of what value of $p$ we use. If we decrease $p$ and thus eliminate model space vectors associated with small singular values,then the solution becomes more stable. However, this stability comes at the expense of reducing the dimension of the subspace of $R ^ { n }$ where the solution lies.

As a esult, the model resolution matrix for the stabilized solution obtained by decreasing $p$ becomes less like the identity matrix,and the fit to the data worsens.

The condition number of $\mathbf { G }$ is the coefficient in (3.89)

$$
\mathrm { c o n d } ( \mathbf { G } ) = \frac { s _ { 1 } } { s _ { k } }
$$

where $k = \operatorname* { m i n } ( m , n )$ . The MATLAB command cond can be used to compute (3.90). If $\mathbf { G }$ is of full rank,and we use all of the singular values in the pseudoinverse solution $( p = k )$ , then the condition number is exactly (3.90). If $\mathbf { G }$ is of less than full rank, then the condition number is effectively infinite. As with the model and data resolution matrices (3.62) and (3.76)), the condition number is a property of $\mathbf { G }$ that can be computed in the design phase of an experiment before any data are collected.

A condition that insures solution stability and arises naturally from consideration of (3.80) is the discrete Picard condition [67]. The discrete Picard condition is satisfied when the dot products of the columns of $\mathbf { U }$ and the data vector decay to zero more quickly than the singular values, $s _ { i }$ . Under this condition,we should not see instability due to small singular values. The discrete Picard condition can be assessed by plotting the ratios of $\mathbf { U } _ { . , i } ^ { T } \mathbf { d }$ to $s _ { i }$ across the singular value spectrum.

If the discrete Picard condition is not satisfied, we may stillbe able to recover a useful model by truncating the series for $\mathbf { m } \dagger$ (3.80) at term $\boldsymbol { p } ^ { \prime } < \boldsymbol { p }$ ， to produce a truncated SVD,or TsVD solution. One way to decide where to truncate the series is to apply the discrepancy principle. Under the discrepancy principle, we choose $p ^ { \prime }$ so that the model fits the data to a specified tolerance, $\delta$ ,that is,

$$
\lVert \mathbf { G } _ { w } \mathbf { m } - \mathbf { d } _ { w } \rVert _ { 2 } \leq \delta ,
$$

where $\mathbf { G } _ { \boldsymbol { w } }$ and $\mathbf { d } _ { \boldsymbol { w } }$ are the weighted system matrix and data vector, respectively.

How should we select $\delta \ ?$ We discussed in Chapter 2 that when we estimate the solu-tion to a full column rank least squares problem, $\| \mathbf { G } _ { u } \mathbf { m } _ { L _ { 2 } } - \mathbf { d } _ { u } \| _ { 2 } ^ { 2 }$ has a $\chi ^ { 2 }$ distribution with $m - n$ degrees of freedom, so we could set $\delta$ equal to $m - n$ if $m > n$ .However, when the number of model parameters $n$ is greater than or equal to the number of data $m$ ,this formulation fails because there is no $\chi ^ { 2 }$ distribution with fewer than one degree of freedom. In practice, a common heuristic is to require $\lVert \mathbf { G } _ { u } \mathbf { m } - \mathbf { d } _ { u } \rVert _ { 2 } ^ { 2 }$ to be smaller than $m$ , because the approximate median of a $\chi ^ { 2 }$ distribution with $m$ degrees of freedom is m (Figure B.4).

A TSVD solution willnot fit the data as well as solutions that include the model space basis vectors with small singular values.However, fitting the data vector too precisely in ill-posed problems (sometimes referred to as over-fiting) will allow data noise to control major features, or even completely dominate, the model.

The TSVD solution is but one example of regularization,where solutions are selected to sacrifice fit to the data in exchange for solution stability. Understanding the trade-off between fiting the data and solution stability involved in regularization is of fundamental importance.

# 3.4.A RANK DEFICIENT TOMOGRAPHY PROBLEM

A linear least squares problem is said to be rank deficient if there is a clear distinction between the nonzero and zero singular values and $\operatorname { r a n k } ( \mathbf G )$ is less than $n$ Numerically computed singular values will often include some that are extremely small but not quite zero,because of round-off errors. If there is a substantial gap between the largest of these tiny singular values and the first truly nonzero singular value, then it can be easy to distinguish between the two populations.Rank deficient problems can often be solved in a straightforward manner by applying the generalized inverse solution. After truncating the effectively zero singular values,a least squares model of limited resolution will be produced,and stability will seldom be an issue.

# Example 3.1

Using the SVD,let us revisit the straight ray path tomography example that we con-sidered earlier in Examples 1.6 and 1.12 (Figure 3.2). We introduced a rank deficient system in which we were constraining an $n = 9$ -parameter slowness model with $m = 8$ travel time observations. We map the two-dimensional grid of slownesses into a model vector by using a row-by-row indexing convention to obtain

![](images/ffe016010ef7080307e3aafd9798121add77c22786d59bf23f1b0d8baa0ce683.jpg)  
Figure 3.2 A simple tomography example (revisited).

$$
\mathbf { G m } = { \left[ \begin{array} { l l l l l l l l l } { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } \\ { { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } \end{array} \right] } { \left[ \begin{array} { l } { s _ { 1 1 } } \\ { s _ { 1 2 } } \\ { s _ { 3 1 } } \\ { s _ { 2 1 } } \\ { s _ { 2 2 } } \\ { s _ { 2 3 } } \\ { s _ { 3 1 } } \\ { s _ { 3 2 } } \\ { s _ { 3 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { t _ { 1 } } \\ { t _ { 2 } } \\ { t _ { 3 } } \\ { t _ { 4 } } \\ { t _ { 5 } } \\ { t _ { 6 } } \\ { t _ { 7 } } \\ { t _ { 8 } } \end{array} \right] } .
$$

The eight singular values of $\mathbf { G }$ are, numerically evaluated,

$$
\operatorname { d i a g } ( \mathbf { S } ) = { \left[ \begin{array} { l } { 3 . 1 8 0 } \\ { 2 . 0 0 0 } \\ { 1 . 7 3 2 } \\ { 1 . 7 3 2 } \\ { 1 . 7 3 2 } \\ { 1 . 6 0 7 } \\ { 0 . 5 5 3 } \\ { 1 . 4 2 9 \times 1 0 ^ { - 1 6 } } \end{array} \right] } .
$$

The smallest singular value, $s _ { 8 }$ , is nonzero in numerical evaluation only because of round-off errors in the SVD algorithm. It is zero in an analytical solution and is effectively zero in numerical computation relative to the other singular values. The ratio of the largest to smallest of the other singular values is about 6,and the generalized inverse solution (3.8O) will thus be stable in the presence of noise. Because $\operatorname { r a n k } ( \mathbf G ) = p = 7$ is less than both $m$ and $n$ ，the problem is both rank deficient and will in general have no exact solution. The model null space, $N ( \mathbf G )$ , is spanned by the two orthonormal vectors that form the 8th and 9th columns of $\mathbf { v }$ . An orthonormal basis for the nullspace is

$$
\mathbf { V } _ { 0 } = \left[ \mathbf { V } _ { , 8 } , \mathbf { V } _ { , 9 } \right] = \left[ \begin{array} { c c } { - 0 . 0 6 2 0 } & { - 0 . 4 0 3 5 } \\ { - 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } \\ { 0 . 4 6 5 5 } & { 0 . 3 4 1 5 } \\ { 0 . 4 0 3 5 } & { - 0 . 0 6 2 0 } \\ { 0 . 0 6 2 0 } & { 0 . 4 0 3 5 } \\ { - 0 . 4 6 5 5 } & { - 0 . 3 4 1 5 } \\ { - 0 . 3 4 1 5 } & { 0 . 4 6 5 5 } \\ { 0 . 3 4 1 5 } & { - 0 . 4 6 5 5 } \\ { 0 . 0 0 0 0 } & { 0 . 0 0 0 0 } \end{array} \right] .
$$

To obtain a geometric appreciation for the two model null space vectors in this exam-ple,we can reshape them into 3 by 3 matrices corresponding to the geometry of the blocks (e.g., by using the MATLAB reshape command) to plot their elements in proper physical positions. Here,we have

$$
\begin{array} { r l } { \mathrm { r e s h a p e } ( \mathbf { V } _ { \mathrm { . 8 } } , \ 3 , \ 3 ) ^ { \prime } = \left[ \begin{array} { c c c } { - 0 . 0 6 2 0 } & { - 0 . 4 0 3 5 } & { 0 . 4 6 5 5 } \\ { 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } & { - 0 . 4 6 5 5 } \\ { - 0 . 3 4 1 5 } & { 0 . 3 4 1 5 } & { 0 . 0 0 0 0 } \end{array} \right] } & { } \\ { \mathrm { r e s h a p e } ( \mathbf { V } _ { \mathrm { . 9 } } , \ 3 , \ 3 ) ^ { \prime } = \left[ \begin{array} { c c c } { - 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } & { 0 . 3 4 1 5 } \\ { - 0 . 0 6 2 0 } & { 0 . 4 0 3 5 } & { - 0 . 3 4 1 5 } \\ { 0 . 4 6 5 5 } & { - 0 . 4 6 5 5 } & { 0 . 0 0 0 0 } \end{array} \right] } & { } \end{array}
$$

(Figures 3.3 and 3.4).

Recall that if $\mathbf { m } _ { 0 }$ is in the model null space, then (because $\mathbf { G m } _ { 0 } = \mathbf { 0 }$ ）we can add such a model to any solution and not change the fit to the data (3.33). When mapped to their physical locations, three common features of the model null space basis vector elements in this example stand out:

1. The sums along all rows and columns are zero.   
2. The upper left to lower right diagonal sum is zero.   
3. There is no projection in the $m _ { 9 } = s _ { 3 3 }$ model space direction.

The zero sum conditions (1） and (2) arise because paths pasing through any thre horizontal or vertical sets of blocks can only constrain the sum of those block values. The condition (3) that $m \mathrm { { g } } = 0$ occurs because that model element is uniquely constrained by the 8th ray, which passes exclusively through the $s _ { 3 , 3 }$ block. Thus,any variation in m9 will clearly affect the predicted data, and any vector in the model nul space must have a value of zero in m9.

![](images/bd9f712fa8d119d99be74f0ef68875edb24dc6aad53a18e1dfe9715e2164c989.jpg)  
Figure 3.3 Image of the nullspace model $\mathbf { V } _ { \cdot , 8 }$

The single basis vector spanning the data null space in this example is

$$
\mathbf { U } _ { 0 } = \mathbf { U } _ { , 8 } = { \left[ \begin{array} { l } { - 0 . 4 0 8 } \\ { - 0 . 4 0 8 } \\ { - 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 0 0 0 } \\ { 0 . 0 0 0 } \end{array} \right] } .
$$

This indicates that increasing the times $t _ { 1 } , t _ { 2 }$ ,and $t _ { 3 }$ and decreasing the times $t _ { 4 } , \ t _ { 5 }$ ,and $t _ { 6 }$ by equal amounts wil result in no change in the pseudoinverse solution.

Recall that, even for noise-free data, we will not recover a general $\mathbf { m _ { \mathrm { t r u e } } }$ in a rank deficient problem using (3.22)， but will instead recover a “smeared’ model $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$ Because $\mathbf { R } _ { \mathrm { m } }$ for a rank deficient problem is itself rank deficient, this smearing is irreversible. The full $\mathbf { R } _ { \mathrm { m } }$ matrix dictates precisely how this smearing occurs. The elements of $\mathbf { R } _ { \mathrm { m } }$ for this example are shown in Figure 3.5.

Examining the entire $n$ by $n$ model resolution matrix becomes cumbersome in large problems.The $n$ diagonal elements of $\mathbf { R } _ { \mathrm { m } }$ can be examined more easily to provide basic information on how well recovered each model parameter will be. The reshaped

![](images/4c28c082ecbc2c0ca4f2e2c7f6839985388066c0538737ecae71cf85205489e5.jpg)  
Figure 3.5 Elements of the model resolution matrix, $\mathbf { R } _ { \mathrm { m } }$ (3.62), for the generalized inverse solution.

![](images/7d69b4c6054a45bacbfc729fba73560c0bdc9587d7b5b7895c44676f06df2af0.jpg)  
Figure 3.6 Diagonal elements of the resolution matrix plotted in their respective geometric model locations.

diagonal of $\mathbf { R } _ { \mathrm { m } }$ from Figure 3.5 is

$$
\mathrm { r e s h a p e } ( \mathrm { d i a g } ( \mathbf { R } _ { \mathrm { m } } ) , 3 , 3 ) ^ { \prime } = \left[ { \begin{array} { l l l } { 0 . 8 3 3 } & { 0 . 8 3 3 } & { 0 . 6 6 7 } \\ { 0 . 8 3 3 } & { 0 . 8 3 3 } & { 0 . 6 6 7 } \\ { 0 . 6 6 7 } & { 0 . 6 6 7 } & { 1 . 0 0 0 } \end{array} } \right] .
$$

These values are plotted in Figure 3.6.

Figure 3.6 and (3.98) tellus that m9 is perfectly resolved, but that we can expect loss of resolution (and hence smearing of the true model into other blocks) for all of the other solution parameters.

We next assess the smoothing effects of limited model resolution by performing a resolution test using synthetic data for a test model of interest, and assessing the recovery of the test model by examining the corresponding inverse solution. Consider a spike model consisting of the vector with its 5th element equal to one and zeros elsewhere (Figure 3.7). Forward modeling gives the predicted data set for $\mathbf { m } _ { \mathrm { t e s t } }$

$$
\mathbf { d } _ { \mathrm { t e s t } } = \mathbf { G } \mathbf { m } _ { \mathrm { t e s t } } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \\ { 0 } \\ { 1 } \\ { 0 } \\ { \sqrt { 2 } } \\ { 0 } \end{array} \right] }
$$

and the corresponding (reshaped) generalized inverse model is the fifth column of $\mathbf { R } _ { \mathrm { m } }$ ， which is

$$
\mathrm { r e s h a p e } ( \mathbf { m } _ { \mathord { \left/ { \vphantom { \mathrm { 0 . 1 6 7 } } } \right. \kern - delimiterspace } 3 } , 3 , 3 ) ^ { \prime } = \left[ \begin{array} { r r r } { 0 . 1 6 7 } & { 0 } & { - 0 . 1 6 7 } \\ { 0 } & { 0 . 8 3 3 } & { 0 . 1 6 7 } \\ { - 0 . 1 6 7 } & { 0 . 1 6 7 } & { 0 . 1 } \end{array} \right]
$$

![](images/fced92ee9a6018d658e945d7a56e510f975fec2b68561f56efb097c9b086bcb3.jpg)  
Figure 3.7 A spike test model.

(Figure 3.8). The recovered model in this spike test shows that limited resolution causes information about the central block slowness to smear into some,but not all, of the adjacent blocks even for noise-free data, with the exact form of the smearing dictated by the model resolution matrix.

It is important to reemphasize that the ability to recover the true model in practice is affected both by the bias caused by limited resolution,which is a characteristic of the matrix $\mathbf { G }$ and hence applies even to noise-free data,and by the mapping of any data noise into the model parameters.In specific cases one effect or the other may dominate.

# 3.5.DISCRETE ILL-POSED PROBLEMS

In many problems the singular values decay gradually toward zero and do not show an obvious jump between nonzero and zero singular values. This happens frequently when we discretize Fredholm integral equations of the first kind as in Chapter 1. In particular, as we increase the number of points in the discretization,we typically find that $\mathbf { G }$ becomes more and more poorly conditioned. We will refer to these as discrete ill-posed problems.

The rate of singular value spectrum decay can be used to characterize a discrete ill-posed problem as mildly, moderately, or severely ill-posed. If $s _ { j } = O ( j ^ { - \alpha } )$ for $\alpha \leq 1$ (where $O$ means “on the order of") then we call the problem mildly il-posed. If $s _ { j } =$ $O ( j ^ { - \alpha } )$ for $\alpha > 1$ ,then the problem is moderately ill-posed. If $s _ { j } = O ( e ^ { - \alpha j } )$ for some $\alpha > 0$ , then the problem is severely ill-posed.

In discrete ill-posed problems, singular vectors $\mathbf { V } _ { \cdot , j }$ associated with large singular values are typically smooth，while those corresponding to smaller singular values are highly oscillatory [67]. The influence of rough basis functions becomes increasingly apparent in the character of the generalized inverse solution as more singular values and vectors are included. When we attempt to solve such a problem with the TSVD in the presence of data noise,it is critical to decide where to truncate (3.8O). If we truncate the sum too early, then our solution will lack details that require model vectors associated with the smallr singular values for their representation. However, if we include too many terms,then the solution becomes dominated by the influence of the data noise.

# Example 3.2

Consider an inverse problem where we have a physical process (e.g., seismic ground motion） recorded by a linear instrument of limited bandwidth (e.g.，a vertical seismometer; Figure 3.9). The response of such a device is commonly characterized by an instrument impulse response, which is the response of the system to a delta function input. Consider the instrument impulse response

$$
g ( t ) = \left\{ { \begin{array} { l l } { g _ { 0 } t e ^ { - t / T _ { 0 } } } & { ( t \geq 0 ) } \\ { 0 } & { ( t < 0 ) . } \end{array} } \right.
$$

Figure 3.9 shows the displacement response of a critically damped seismometer with a characteristic time constant $T _ { 0 }$ and gain, $g _ { 0 }$ , to a unit area $( 1 ~ \mathrm { m } / \mathrm { s } ^ { 2 } \cdot \mathrm { s } )$ impulsive ground acceleration input.

Assuming that the displacement of the seismometer is electronically converted to output volts, we conveniently choose $g _ { 0 }$ to be $T _ { 0 } e ^ { - 1 } \ : \mathrm { V / m \cdot s }$ to produce a 1-V maximum output value for the impulse response,and $T _ { \mathrm { 0 } } = 1 0 ~ \mathrm { s }$

The seismometer output (or seismogram), $\nu ( t )$ , is a voltage record given by the convolution of the true ground acceleration, $m _ { \mathrm { t r u e } } ( t )$ , with (3.101)

$$
\nu ( t ) = \intop _ { - \infty } ^ { \infty } g ( \tau - t ) m _ { \mathrm { t r u e } } ( \tau ) d \tau .
$$

We are interested in the inverse deconvolution operation that wil remove the smoothing effect of $g ( t )$ in (3.1O2) and allow us to recover the true ground acceleration $m _ { \mathrm { t r u e } }$

Discretizing (3.102) using the midpoint rule with a time interval $\Delta t$ ，we obtain

$$
\mathbf { d } = \mathbf { G } \mathbf { m }
$$

where

$$
G _ { i , j } = \left\{ \begin{array} { l l } { ( t _ { i } - t _ { j } ) e ^ { - ( t _ { i } - t _ { j } ) / T _ { 0 } } \Delta t } & { ( t _ { i } \geq t _ { j } ) } \\ { 0 } & { ( t _ { i } < t _ { j } ) . } \end{array} \right.
$$

The rows of $\mathbf { G }$ in (3.104) are time-reversed,and the columns of $\mathbf { G }$ are non-timereversed, sampled representations of the impulse response $g ( t )$ ，lagged by $i$ and $j$ respectively. Using a time interval of $[ - 5 , 1 0 0 ]$ s,outside of which (3.101) and any model, $\mathbf { m }$ ,of interest are assumed to be very small or zero,and a discretization interval of $\Delta t = 0 . 5 \mathrm { ~ s ~ }$ ，we obtain a discretized $m$ by $n$ system matrix $\mathbf { G }$ with $m = n = 2 1 0$

The singular values of $\mathbf { G }$ are all nonzero and range from about 25.3 to 0.017, giving a condition number of ${ \approx } 1 4 8 0$ ， and showing that this discretization has produced a discrete system that is mildly ill-posed (Figure 3.1O). However, adding noise at the level of 1 part in 1OOO will be sufficient to make the generalized inverse solution unstable. The reason for this can be seen by examining successive rows of $\mathbf { G }$ ,which are nearly but not quite identical, with

$$
\frac { \mathbf { G } _ { i , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } { \| \mathbf { G } _ { i , \cdot } \| _ { 2 } \| \mathbf { G } _ { i + 1 , \cdot } \| _ { 2 } } \approx 0 . 9 9 9 .
$$

This near-identicalnessof the rows of $\mathbf { G }$ makes the system of equations nearly singular, hence resulting in a large condition number.

Now, consider a true ground acceleration signal that consists of two acceleration pulses with widths of $\sigma = 2 ~ \mathrm { s }$ ，centered at $t = 8 :$ Sand $t = 2 5$ S

$$
m _ { \mathrm { t r u e } } ( t ) = e ^ { - ( t - 8 ) ^ { 2 } / ( 2 \sigma ^ { 2 } ) } + 0 . 5 e ^ { - ( t - 2 5 ) ^ { 2 } / ( 2 \sigma ^ { 2 } ) } .
$$

We sample $\mathbf { m } _ { \mathrm { t r u e } } ( t )$ on the time interval $[ - 5 , 1 0 0 ]$ s to obtain a 210-element vector $\mathbf { m _ { \mathrm { t r u e } } }$ , and generate the noise-free data set

$$
\mathbf { d } _ { \mathrm { t r u e } } = \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } }
$$

and a second data set with independent $N ( 0 , ( 0 . 0 5 \mathrm { ~ V } ) ^ { 2 } )$ noise added. The data set with noise is shown in Figure 3.12.

The recovered least squares model from the full $( p = 2 1 0 )$ generalized inverse solution,

$$
\mathbf { m } = \mathbf { V } \mathbf { S } ^ { - 1 } \mathbf { U } ^ { T } \mathbf { d } _ { \mathrm { t r u e } }
$$

is shown in Figure 3.13. The model fits its noiseless data vector, ${ \bf d } _ { \mathrm { t r u e } }$ ， perfectly, and is essentially identical to the true model (Figure 3.11).

The least squares solution for the noisy data vector, $\mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta }$ ，

$$
\mathbf { m } = \mathbf { V } \mathbf { S } ^ { - 1 } \mathbf { U } ^ { T } ( \mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta } )
$$

is shown in Figure 3.14.

Although this solution fits its particular data vector, $\mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta }$ ,exactly, it is worthless in divining information about the true ground motion. Information about $\mathbf { m } _ { \mathrm { t r u e } }$ is overwhelmed by the small amount of added noise,amplified enormously by the inversion process.

Can a useful model be recovered by the TSVD? Using the discrepancy principle as our guide and selecting a range of solutions by varying $p ^ { \prime }$ ，we can in fact obtain an appropriate solution when we use just $p ^ { \prime } = 2 6$ columns of $\mathbf { v }$ to obtain a solution (Figure 3.15).

Essential features of the true model are resolved in the solution of Figure 3.15,but the solution technique introduces oscillations and loss of resolution. Specifically, we see that the widths of the inferred pulses are somewhat wider,and the inferred amplitudes somewhat less,than those of the true ground acceleration. These effects are both hallmarks of limited resolution,as characterized by a nonidentity model resolution matrix.

An image of the model resolution matrix in Figure 3.16 shows a finite-width central band and oscillatory side lobes.

A typical (8Oth) column of the model resolution matrix displays the smearing of the true model into the recovered model for the choice of the $p = 2 6$ inverse operator (Figure 3.17). The smoothing is over a characteristic width of about $5 \ { \mathrm { s } } ,$ ，which is why our recovered model, although it does a decent job of rejecting noise, underestimates the amplitude and narrowness of the pulses in the true model (Figure 3.11). The oscillatory behavior of the resolution matrix is attributable to our abrupt truncation of the model space.

![](images/d9585f8bc274ecbfeb6f6b6cab7efac1059302fedfebb9772d9eda004da64649.jpg)  
Figure 3.15 TSVD solution using $p ^ { \prime } = 2 6$ singular values for the noisy data shown in Figure 3.12.   
Figure 3.16 The model resolution matrix elements, $\mathbf { R } _ { \mathrm { m } i , j } ,$ for the TSVD solution including $p ^ { \prime } = 2 6$ singular values.

Each of the $n$ columns of $\mathbf { v }$ is an oscillatory model basis function,with $j - 1$ zero crossings，where $j$ is the column number. In truncating (3.8O) at 26 terms to stabilize the inverse solution,we place a limit on the most oscillatory model space basis vectors that we wil allow. This truncation gives us a model, and model resolution, that contain

![](images/8356189117ac108c0ea8f880f51160ff8641fa7c3f04f126473a4cdfbe183ad9.jpg)  
Figure 3.17 The (80th) column of the model resolution matrix, $\mathbf { R } _ { \mathrm { m } } ,$ for the TSVD solution including $p ^ { \prime } = 2 6$ singular values.

Oscillatory structure with up to around $p - 1 = 2 5$ zero crossings. We will examine this perspective further in Chapter 8,where issues associated with oscillatory model basis functions will be revisited in the context of Fourier theory.

# Example 3.3

Recall the Shaw problem from Examples 1.6 and 1.10. Figure 3.18 shows the singular value spectrum for the corresponding G matrix with $n = m = 2 0$ ,which is characterized by very rapid singular value decay to zero.

This is a severely ill-posed problem,and there is no obvious break point above which the singular values can reasonably be considered to be nonzero and below which the singular values can be considered to be O. The MATLAB rank command gives $p ^ { \prime } = 1 8$ ， suggesting that the last two singular values are effectively O. The condition number of this problem is enormous (larger than $1 0 ^ { 1 4 }$ ）.

The 18th column of V, which corresponds to the smallest nonzero singular value, is shown in Figure 3.19.In contrast, the first column of $\mathbf { v }$ ，which corresponds to the largest singular value, represents a much smoother model (Figure 3.2O). This behavior is typical of discrete ill-posed problems.

Next, we wil perform a simple resolution test. Suppose that the input to the system is given by

$$
m _ { i } = { \left\{ \begin{array} { l l } { 1 } & { i = 1 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

![](images/4465c7c3d979d354f7148534e3759dbcfdd0b3d2c0d75874107b8dbc7f637256.jpg)  
Figure 3.18 Singular values of Gfor the Shaw example $\mathrm { \Delta } n = m = 2 0 \mathrm { \Delta }$

![](images/7fcdf655fae26aa2902861e2eb68897f44cd30eff1b973a92aa8dc648ddbfc7d.jpg)  
Figure 3.19 $\mathbf { V } _ { \cdot , 1 8 }$ for the Shaw example problem.

(Figure 3.21). We use the model to obtain noise-free data and then apply the generalized inverse (3.22) with various values of $p$ to obtain TSVD inverse solutions. The corresponding data are shown in Figure 3.22. If we compute the generalized inverse from these data using MATLAB's double-precision algorithms, we get fairly good recovery of (3.11O),although there are still some lower amplitude negative intensity values (Figure 3.23).

![](images/ad012a711b8f95db99ea6dd534b648f4f85f8cf9c758aa3ae99cb809143c74f5.jpg)  
Figure 3.20 $\mathbf { V } _ { \cdot , 1 }$ for the Shaw example problem.

![](images/81c621b228dc15332de44039fef8f462b54c71de0b917f49f2b3f1a2774a279e.jpg)  
Figure 3.21 The spike model.

However, if we add a very small amount of noise to the data in Figure 3.22, things change dramatically. Ading $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise to the data of Figure 3.22 and com-puting a generalized inverse solution using $p ^ { \prime } = 1 8$ produces the wild solution of Figure 3.24,which bears no resemblance to the true model. Note that the vertical scale in Figure 3.24 is multiplied by $1 0 ^ { 6 } !$ Furthermore, the solution includes negative intensities, which are not physically possible. This inverse solution is even more sensitive to noise than that of the previous deconvolution example, to the extent that even noise on the order of 1 part in $1 0 ^ { 6 }$ will destabilize the solution.

![](images/60e2d15173461dd7c661c7c43cff68fa386b6cda80a3305f5f0d740d8281ab72.jpg)  
Figure 3.22 Noise-free data predicted for the spike model.

![](images/2fc8e52c0def4a7471af9fe71b67db883b0a10f75cec4eaadc15f6cbd228f215.jpg)  
Figure 3.23 The generalized inverse solution for the spike model, no noise.

Next, we consider what happens when we use only the 1O largest singular values and their corresponding model space vectors to construct a TSVD solution. Figure 3.25 shows the solution using 1O singular values with the same noise as Figure 3.24. Because we have cut off a number of singular values,we have reduced the model resolution. The inverse solution is smeared out, but it is still possble to conclude that there is some significant spike-like feature near $\theta = 0$ . In contrast to the situation that we observed in Figure 3.24, the model recovery is not visibly affected by the noise. The trade-off is that we must now accept the imperfect resolution of this solution and its attendant bias towards smoother models.

![](images/b5e2637412061598956e769d516f808cd818621ee0fddd39dd2d2d874314449e.jpg)  
Figure 3.24 Recovery of the spike model with $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise using the TSVD method $( p ^ { \prime } = 1 8 )$ Note that the intensity scale ranges from $- 4 \times 1 0 ^ { 6 }$ to $4 \times 1 0 ^ { 6 }$

![](images/df4b3c4281874c1701171de35515e2d56e6ca3b4cde6dbdd9121b24f2f147283.jpg)  
Figure 3.25 Recovery of the spike model with noise using the TSVD method $( p ^ { \prime } = 1 0 )$

What happens if we discretize the problem with a larger number of intervals? Figure 3.26 shows the singular values for the $\mathbf { G }$ matrix with $n = m = 1 0 0$ intervals. The first 20 or so singular values are apparently nonzero, while the last 8O or so singular values are effectively zero.

![](images/f1cc8e1196f9662c60f7bd93d16cb16d375b8efffbbaaf7196cda308ee89c14d.jpg)  
Figure 3.26 Singular values of Gfor the Shaw example $\mathrm { { \Delta } } n = m = 1 0 0 \mathrm { { \Delta } }$   
Figure 3.27 Recovery of the spike model with noise using the TSVD method $( n = m = 1 0 0 , p ^ { \prime } = 1 0 )$

Figure 3.27 shows the inverse solution for the spike model with $n = m = 1 0 0$ and $p = 1 0$ . This solution is very similar to the solution shown in Figure 3.24. In general, discretizing over more intervals does not hurt as long as the solution is appropriately regularized and the additional computation time is acceptable.

![](images/54824c0f4d49a31c3fdca986a37c6c1243cdfbd9b194fb4f537059f7ad663708.jpg)  
Figure 3.28 Singular values of Gfor the Shaw example $( n = m = 6 )$

What about a smaller number of intervals? Figure 3.28 shows the singular values of the $\mathbf { G }$ matrix with $n = m = 6$ . In this case there are no terribly small singular values. However, with only 6 elements in the model vector, we cannot hope to resolve the details of a source intensity distribution with a complex structure. This is an example of regularization by discretization (see also Exercise 1.3).

This example again demonstrates a fundamental dilemma. If we include small singular values in the series solution (3.8O),then our solution becomes unstable in the presence of data noise. If we do not include these terms, our solution is less sensitive to data noise, but we sacrifice resolution and introduce bias.

# 3.6. EXERCISES

1. The pseudoinverse of a matrix $\mathbf { G }$ was originally defined by Moore and Penrose as the unique matrix $\mathbf { G } ^ { \dagger }$ with the properties

a. $\mathbf { G } \mathbf { G } ^ { \dagger } \mathbf { G } = \mathbf { G }$   
b. $\mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { G } ^ { \dagger } = \mathbf { G } ^ { \dagger }$   
c. $( \mathbf { G } \mathbf { G } ^ { \dagger } ) ^ { T } = \mathbf { G } \mathbf { G } ^ { \dagger }$   
d. $( \mathbf { G } ^ { \dagger } \mathbf { G } ) ^ { T } = \mathbf { G } ^ { \dagger } \mathbf { G }$

Show that $\mathbf { G } ^ { \dagger }$ as given by (3.20)satisfies these four properties.

2. Another resolution test commonly performed in tomography studies is a checkerboard test, which consists of using a test model composed of alternating positive and negative perturbations. Perform a checkerboard test on the tomography problem

in Example 3.1 using the test model,

$$
\mathbf { m } _ { \mathrm { t r u e } } = \left[ { \begin{array} { r r r } { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { 1 } \\ { - 1 } & { 1 } & { - 1 } \end{array} } \right] .
$$

Evaluate the difference between the true (checkerboard) model and the recovered model in your test,and interpret the pattern of differences. Are any block values recovered exactly? If so, does this imply perfect resolution for these model parameters?

3. Using the parameter estimation problem described in Example 1.1 for determining the three parameters defining a ballistic trajectory, construct synthetic examples that demonstrate the following four cases using the SVD. In each case, display and interpret the SVD components U,V,and S in terms of the rank, $p$ ，of your forward problem $\mathbf { G }$ matrix. Display and interpret any model and data null space vector(s) and calculate model and data space resolution matrices.

a. Three data points that are exactly fit by a unique model. Plot your data points and the predicted data for your model.   
b. Two data points that are exactly fit by an infinite suite of parabolas. Plot your data points and the predicted data for a suite of these models.   
c.Four data points that are only approximately fit by a parabola. Plot your data points and the predicted data for the least squares model.   
d. Two data points that are only approximately fit by any parabola, and for which there are an infinite number of least squares solutions. Plot your data points and the predicted data for a suite of least squares models.

4. A large north-south by east-west-oriented, nearly square plan view, sandstone quarry block ( $1 6 ~ \mathrm { m }$ by $1 6 ~ \mathrm { m } ,$ ） with a bulk compressional wave seismic velocity of approximately $3 0 0 0 ~ \mathrm { m / s }$ is suspected of harboring higher-velocity dinosaur remains. An ultrasonic tomography scan is performed in a horizontal plane bisecting the boulder, producing a data set consisting of $1 6 { \mathrm { ~ E } } {  } \mathbb { W } ,$ $1 6 ~ \mathrm { N { \to } S }$ $3 1 \mathrm { \ N E {  } S W } ,$ and 31 $\mathrm { N W } {  } \mathrm { S E }$ travel times (see Figure 3.29). The travel time data (units of s) have statistically independent errors,and the travel time contribution for a uniform background model (with a velocity of $3 0 0 0 \ \mathrm { m / s } ,$ ）has been subtracted from each travel time measurement.

The MATLAB data files that you will need to load containing the travel time data follow: rowscan.mat, colscan.mat, diag1scan.mat, and diag2scan.mat. The standard deviations of all data measurements are $1 . 5 \times 1 0 ^ { - 5 } \mathrm { s }$ Because the travel time contributions for a uniform background model (with a velocity of $3 0 0 0 ~ \mathrm { m / s }$ ）have been subtracted from each travel time measurement, you will be solving for slowness and velocity perturbations relative to a uniform slowness model of $1 / 3 0 0 0 ~ \mathrm { { s / m } }$ Use a row-by-row mapping between the slowness grid and the model vector (e.g.,Exam-ple 1.12). The row format of each data file is $( x _ { 1 } , \ \gamma _ { 1 } , \ x _ { 2 } , \ \gamma _ { 2 } , \ t )$ where the starting point coordinate of each source is $( x _ { 1 } , \gamma _ { 1 } )$ , the end point coordinate is $( x _ { 2 } , \gamma _ { 2 } )$ ,and the travel time along a ray path between the source and receiver points is a path integral (in seconds).

![](images/458e93df153564af5502db5b0b4ce76f887fb6a62794b4811ece8846e7ef4445.jpg)  
Figure 3.29 Tomography exercise, showing block discretization, block numbering convention,and representative ray paths going east-west (a), north-south (b),southwest-northeast (c),and northwestsoutheast (d).

Parameterize the slowness structure in the plane of the survey by dividing the boulder into a $1 6 \times 1 6$ grid of 256 1-m-square,north-by-east blocks and construct a linear system for the forward problem (Figure 3.29). Assume that the ray paths through each homogeneous block can be represented by straight lines, so that the travel time expression is

$$
\begin{array} { l } { { \displaystyle t = \int _ { \ell } s ( { \bf x } ) d \ell } } \\ { { \displaystyle \ = \sum _ { \mathrm { b l o c k s } } s _ { \mathrm { b l o c k } } \cdot \Delta l _ { \mathrm { b l o c k } } } , } \end{array}
$$

where $\Delta l _ { \mathrm { b l o c k } }$ is $1 ~ \mathrm { m }$ for the row and column scans and $\sqrt { 2 } \mathrm { m }$ for the diagonal scans.

Use the SVD to find a minimum-length/least squares solution, $\mathbf { m } _ { \dagger }$ ,for the 256 block slowness perturbations that fit the data as exactly as possible. Perform two inversions in this manner:

1. Use the row and column scans only.

2.Use the complete data set.

For each inversion:

a. Note the rank of your $\mathbf { G }$ matrix relating the data and model.   
b. State and discuss the general solution and/or data fit significance of the elements and dimensions of the data and model null spaces. Plot and interpret an element of each space and contour or otherwise display a nonzero model that fits the trivial data set $\mathbf { G m } = \mathbf { d } = \mathbf { 0 }$ exactly.   
c. Note whether there are any model parameters that have perfect resolution.   
d.Produce a 16 by 16 element contour or other plot of your slowness perturbation model, displaying the maximum and minimum slowness perturbations in the title of each plot. Interpret any internal structures geometrically and in terms of seismic velocity $( \mathrm { i n ~ m } / \mathrm { s } )$ ).   
e. Show the model resolution by contouring or otherwise displaying the 256 diagonal elements of the model resolution matrix, reshaped into an appropriate 16 by 16 grid.   
f. Describe how one could use solutions to $\mathbf { G m } = \mathbf { d } = \mathbf { 0 }$ to demonstrate that very rough models exist that will fit any data set just as well as a generalized inverse model. Show one such wild model.

5. Consider the data in Table 3.2 (also found in the file ifk.mat).

The function $d ( \gamma )$ ， $0 \leq \gamma \leq 1$ , is related to an unknown function $m ( x ) , 0 \leq x \leq 1$ ， by the mathematical model

$$
d ( \gamma ) = \int _ { 0 } ^ { 1 } x e ^ { - x \gamma } m ( x ) d x .
$$

a. Using the data provided, discretize the integral equation using simple collocation to create a square $\mathbf { G }$ matrix and solve the resulting system of equations.

Table 3.2 Data for Exercise 3.5.   

<table><tr><td>y d(y)</td><td>0.0250 0.07500.12500.1750 0.2250 0.2750 0.32500.37500.4250 0.4750 0.2388 0.2319 0.2252 0.21880.2126 0.2066 0.20080.1952 0.1898</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>80.1846</td></tr><tr><td>y</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.5250 0.5750 0.62500.6750 0.7250 0.77500.8250 0.8750 0.9250 0.9750</td><td></td><td></td></tr><tr><td>d(y)</td><td>0.1795</td><td></td><td></td><td></td><td></td><td>0.1746 0.1699 0.1654 0.16100.1567（</td><td>0.1526</td><td>0.1486</td><td>0.1447</td><td>0.1410</td></tr></table>

b.What is the condition number for this system of equations? Given that the data $d ( \gamma )$ are only accurate to about four digits,what does this tell you about the accuracy of your solution?   
c. Use the TSVD to compute a solution to this problem. You may find a plot of the Picard ratios $\mathbf { U } _ { . , i } ^ { T } \mathbf { d } / s _ { i }$ to be especially useful in deciding how many singular values to include.

# 3.7. NOTES AND FURTHER READING

The Moore-Penrose generalized inverse was independently discovered by Moore in 1920 and Penrose in 1955 [11O,129]. Penrose is generally credited with first showing that the SVD can be used to compute the generalized inverse [129]. Books that discuss the linear algebra of the generalized inverse in more detail include [10, 23].

There was significant early work on the SVD in the 19th century by Beltrami, Jordan, Sylvester, Schmidt,and Weyl [151]. However, the singular value decomposition in matrix form is typically credited to Eckart and Young [41]. Some books that discuss the properties of the SVD and prove its existence include [53,109,152]. Lanczos presents an alternative derivation of the SVD [93]. Algorithms for the computation of the SVD are discussed in [38, 53,164].Books that discuss the use of the SVD and truncated SVD in solving discrete linear inverse problems include [65, 67, 1O8,153].

Resolution tests with spike and checkerboard models as in Example 3.1 are commonly used in practice.However, Leveque, Rivera,and Wittlinger discuss some serious problems with such resolution tests [97]. Complementary information can be acquired by examining the diagonal elements of the resolution matrix,which can be efficiently calculated in isolation from off-diagonal elements even for very large inverse problems [9,103] (Chapter 6).

Matrices like those in Example 3.2 in which the elements along diagonals are con-stant are called Toeplitz matrices [74]. Specialized methods for regularization of problems involving Toeplitz matrices are available [66].

It is possble to effectively regularize the solution to a discretized version of a continuous inverse problem by selecting a coarse discretization (e.g.，Exercise 1.3 and Example 3.3). This approach is analyzed in [45]. However, in doing so we lose the ability to analyze the bias introduced by the regularization. In general, we prefer to use a fine discretization that is consistent with the physics of the forward problem and explicitly regularize the resulting discretized problem.

# Tikhonov Regularization

# Synopsis

The method of Tikhonov regularization for stabilizing inverse problem solutions is introduced and illustrated with examples. Zeroth-order Tikhonov regularization is explored, including its resolution, bias,and uncertainty properties. The concepts of filter factors (which control the contribution of singular values and their corresponding singular vec-tors to the solution) and the discrepancy and L-curve criteria (strategies for selecting the regularization parameter) are presented. Higher-order Tikhonov regularization techniques and their computation by the generalized singular value decomposition (GSVD) and truncated GSVD are discussed.

# 4.1. SELECTING GOOD SOLUTIONS TO ILL-POSED PROBLEMS

We saw in Chapter 3 that, given the SVD of $\mathbf { G }$ (3.1),we can express a generalized inverse solution by a series (3.81)

$$
\mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \sum _ { i = 1 } ^ { p } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i } .
$$

We also saw that the generalized inverse solution can become extremely unstable when one or more of the singular values, $s _ { i }$ ，is small. One approach for dealing with this difficulty, the truncated singular value decomposition (TSVD), was to truncate the series to remove singular vectors, $\mathbf { V } _ { \cdot , i }$ ,associated with smaller singular values, $s _ { i }$ This stabilized, or regularized,the solution in the sense that it made the result less sensitive to data noise.The cost of this stabilization approach is that the regularized solution had reduced resolution and was no longer unbiased.

In this chapter we will introduce and discuss Tikhonov regularization, a very widely applied and easily implemented technique for regularizing discrete ill-posed problems. We will show a series formula for the Tikhonov solution that is a modified version of the generalized inverse series (3.81). The Tikhonov series solution has coefficients that are functions of the regularization parameter controlling the degree of regularization and which give greater weight to model elements associated with larger singular values.

For a general linear least squares problem there may be infinitely many least squares solutions. If we consider that the data contain noise,and that there is no point in fitting such noise exactly, it becomes evident that there can be many solutions that can adequately fit the data in the sense that $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ is small enough.

In zeroth-order Tikhonov regularization，we consider all solutions with $\| \mathbf { G m } -$ $\mathbf { d } \| _ { 2 } \leq \delta$ ,and select the one that minimizes the norm of m

$$
\begin{array} { c } { { \operatorname* { m i n } \lVert \mathbf { m } \rVert _ { 2 } } } \\ { { \lVert \mathbf { G m } - \mathbf { d } \rVert _ { 2 } \leq \delta . } } \end{array}
$$

The fundamental motivation for minimizing the norm of $\mathbf { m }$ is to arrive at a solution that contains just sufficient feature complexity, as quantified by a norm measure, to adequately fit the data. Note that as $\delta$ increases,the set of feasible models expands,and the minimum value of $\| \mathbf { m } \| _ { 2 }$ decreases. In other words,as we allow a poorer fit to the data,a smaller norm model will suffice to fit the data. We can thus trace out a curve of minimum values of $\| \mathbf { m } \| _ { 2 }$ versus $\delta$ (Figure 4.1). It is also possible to trace out this curve by considering problems of the form

$$
\begin{array} { r l } & { \operatorname* { m i n } \| \mathbf G \mathbf { m } - \mathbf { d } \| _ { 2 } } \\ & { \| \mathbf { m } \| _ { 2 } \leq \epsilon . } \end{array}
$$

As $\epsilon$ decreases, the set of feasible solutions becomes smaller,and the minimum value of $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ increases. Again,as we adjust $\epsilon$ we trace out the curve of optimal values of $\| \mathbf { m } \| _ { 2 }$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ (Figure 4.2).

A third option is to consider the damped least squares problem

$$
\operatorname* { m i n } \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { m } \| _ { 2 } ^ { 2 } ,
$$

which arises when we apply the method of Lagrange multipliers to (4.2),where $\alpha$ is a regularization parameter. It can be shown that for appropriate choices of $\delta , \epsilon .$ and $\alpha$ , the three problems (4.2), (4.3),and (4.4) yield the same solution [65]. We will concentrate on solving the damped least squares form of the problem (4.4). Solutions to (4.2) and (4.3) can be obtained using (4.4) by adjusting the regularization parameter $\alpha$ until the constraints are just satisfied.

![](images/7ba02eb4974021e24c59cedd42adabd16a92d51800d190fe983ddcd0ff19fa71.jpg)  
Figure 4.1 A particular misfit norm, $\delta ,$ and its position on the trade-off curve between residual misfit, $\| \mathbf { G m - d } \| _ { 2 } ,$ and model norm, $\| \mathbf { m } \| _ { 2 }$

![](images/ca350e9af79ca396a79b6a2a6ad452db8c7ac5b315cd319c566ab2fb02bf8c06.jpg)  
Figure 4.2 A particular model norm, $\epsilon _ { i }$ ,and its position on the trade-off curve between residual misfit, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } ,$ and model norm, $\| \mathbf { m } \| _ { 2 }$

When plotted on a log-log scale, the curve of optimal values of $\| \mathbf { m } \| _ { 2 }$ versus $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ often takes on a characteristic“L” shape in linear problems. This happens because $\| \mathbf { m } \| _ { 2 }$ is a strictly decreasing function of $\alpha$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ is a strictly increasing function of $\alpha$ . The sharpness of the“corner” varies from problem to problem, but it is frequently well-defined. For this reason, the curve is called an L-curve [63]. In addition to the discrepancy principle, another popular criterion for picking the value of $\alpha$ is the L-curve criterion, in which the value of $\alpha$ that gives the solution closest to the corner of the L-curve is selected.

# 4.2.SVD IMPLEMENTATION OF TIKHONOV REGULARIZATION

The damped least squares problem (4.4) is equivalent to the ordinary least squares prob-lem obtained by augmenting the least squares problem for $\mathbf { G m } = \mathbf { d }$ in the following manner:

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

As long as $\alpha$ is nonzero, the last $n$ rows of the augmented matrix in (4.5) are obviously linearly independent. Equation (4.5) is thus a full rank least squares problem that can be solved by the method of normal equations, that is,

$$
\begin{array} { r } { \left[ { \mathbf G } ^ { T } \quad \alpha { \mathbf I } \right] \bigg [ \mathbf { G } ^ { } \bigg ] \mathbf { m } = \left[ { \mathbf G } ^ { T } \quad \alpha { \mathbf I } \right] \bigg [ \mathbf { 0 } ^ { } \bigg ] . } \end{array}
$$

Equation (4.6) simplifies to

$$
( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } ,
$$

which is the set of constraint equations for a zeroth-order Tikhonov regularization solution of $\mathbf { G m } = \mathbf { d }$

Employing the SVD of $\mathbf { G }$ ， (4.7) can be written as

$$
\begin{array} { c } { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } } \\ { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \end{array}
$$

A simple substitution diagonalizes this system of equations and makes it straightforward to write out the solution. Let $\mathbf { x } = \mathbf { V } ^ { T } \mathbf { m }$ and $\mathbf { m } = \mathbf { V } \mathbf { x }$ Since $\mathbf { V } \mathbf { V } ^ { T } = \mathbf { I }$ ，we can write (4.9) as

$$
\begin{array} { r } { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { V } \mathbf { V } ^ { T } ) \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \\ { \mathbf { V } ( \mathbf { S } ^ { T } \mathbf { S } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { V } ^ { T } \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \\ { ( \mathbf { S } ^ { T } \mathbf { S } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { x } = \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \end{array}
$$

The matrix on the left-hand side of this equation is diagonal,so it is trivial to solve the system of equations,

$$
x _ { i } = \frac { s _ { i } \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } .
$$

Since $\mathbf { m } = \mathbf { V } \mathbf { x }$ ,we obtain the solution

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } \ { \frac { s _ { i } \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } } \mathbf { V } _ { \cdot , i }
$$

vhere $k = \operatorname* { m i n } ( m , n )$ so that all of the nonzero singular values and vectors are included. To relate this formula to (4.1),we can rewrite it slightly as

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } \ { \frac { s _ { i } ^ { 2 } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i }
$$

or

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } f _ { i } \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } \mathbf { V } _ { \cdot , i } \ .
$$

Here, the filter factors

$$
f _ { i } = \frac { s _ { i } ^ { 2 } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } }
$$

control the contribution to the sum from different terms.For $s _ { i } \gg \alpha , f _ { i } \approx 1$ ，and for $s _ { i } \ll \alpha$ ， $f _ { i } \approx 0$ . For singular values between these two extremes,as the $s _ { i }$ decrease,

the $f _ { i }$ produce a monotonically decreasing contribution of corresponding model space vectors, $\mathbf { V } _ { \cdot , i }$

A related method called the damped SVD method [65] uses the filter factors

$$
\hat { f } _ { i } = \frac { s _ { i } } { s _ { i } + \alpha } .
$$

This has a similar effect to using (4.17),but transitions more slowly with the index i.

# Example 4.1

We revisit the severely ill-posed Shaw problem,which was previously introduced in Examples 1.6 and 1.1O,and was analyzed using the SVD in Example 3.3. The true model in this synthetic example is a spike of unit amplitude in the 1Oth model element, and independent $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise has been added to the data vector. We begin by computing the L-curve at 1OOO points and finding its corner by estimating the point of maximum curvature. Figure 4.3 shows the L-curve. The corner of the curve corresponds to α ≈ 6.40 × 10-6.

Next, we compute the Tikhonov regularization solution corresponding to this value of $\alpha$ . This solution is shown in Figure 4.4. Note that this solution is much better than the wild solution obtained by the TSVD with $p ^ { \prime } = 1 8$ (Figure 3.24).

Alternatively, we can use the discrepancy principle to find an appropriate $\alpha$ to obtain a Tikhonov regularized solution. Because independent $N ( 0 , ( 1 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise was added to these $m = 2 0$ data points,we search for a solution for which the square of the norm of the residuals is $2 0 \times 1 0 ^ { - 1 2 }$ ， which corresponds to a residual norm $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ of $\sqrt { 2 0 } \times 1 0 ^ { - 6 } \approx 4 . 4 7 \times 1 0 ^ { - 6 }$ .

![](images/a9ebe060d1668a5eb321a42b9d4a29b55ac160a263470df58029ea0b1dd667ed.jpg)  
Figure 4.3 Zeroth-order Tikhonov regularization L-curve for the Shaw problem, with corner estimated using maximum functional curvature.

![](images/20c8b526e76fc434fde128cfc29a20b5ea504def66e62d24f89ab0a0ae0db411.jpg)  
Figure 4.4 Recovery of the spike model with noise, zeroth-order Tikhonov solution $( \alpha = 6 . 4 0 \times 1 0 ^ { - 6 }$ determined from the L-curve corner).

![](images/57f0b6a7fa4c9116880ac5f653a324084a06e3df0f7388221e09740533490729.jpg)  
Figure 4.5 Recovery of the spike model with noise,zeroth-order Tikhonov solution $( \alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ determined from the discrepancy principle).

The discrepancy principle results in a somewhat larger value of the regularization parameter, $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ ， than that obtained using the L-curve technique above. The corresponding solution, shown in Figure 4.5, thus has a smaller model norm, but the two models are quite close.

It is interesting to note that the norm of the residual of the true (spike) model in this particular case, $3 . 8 6 \times 1 0 ^ { - 6 }$ , is actually slightly smaller than the tolerance that we specified via the discrepancy principle $( 4 . 4 7 \times 1 0 ^ { - 6 } )$ . The discrepancy principle method did not recover the original spike model because the spike model has a norm of 1, while the solution obtained by the discrepancy principle has a norm of only 0.67.

Plotting the singular values $s _ { i }$ ，the values of $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } |$ ,and the ratios $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } | / s _ { i }$ allows us to examine the discrete Picard condition for this problem (Figure 4.6). $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } |$ reaches a noise floor of about $1 \times 1 0 ^ { - 6 }$ after $i = 1 1$ . The singular values continue to decay. As a consequence, the ratios increase rapidly. It is clear from this plot that we cannot expect to obtain useful information from the singular values beyond $i = 1 1$ .The 11th singular value is ${ \approx } 5 . 1 \times 1 0 ^ { - 6 }$ , which is comparable to the values of $\alpha$ in Figures 4.4 and 4.5.

# 4.3.RESOLUTION, BIAS, AND UNCERTAINTY IN THE TIKHONOV SOLUTION

As in our earlier TSVD approach,we can compute a model resolution matrix for the Tikhonov regularization method. Using equation (4.7) and the SVD, the solution can be written as

$$
\begin{array} { r } { { \bf { m } } _ { \alpha } = ( { \bf { G } } ^ { T } { \bf { G } } + \alpha ^ { 2 } { \bf { I } } ) ^ { - 1 } { \bf { G } } ^ { T } { \bf { d } } } \\ { = { \bf { G } } ^ { \sharp } { \bf { d } } } \\ { = { \bf { V } } { \bf { F } } { \bf { S } } ^ { \dagger } { \bf { U } } ^ { T } { \bf { d } } , } \end{array}
$$

where $\mathbf { F }$ is an $n$ by $n$ diagonal matrix with diagonal elements given by the filter factors $f _ { i }$ of (4.17), and $\mathbf { S } ^ { \dagger }$ is the pseudoinverse of S. $\mathbf { G } ^ { \sharp }$ is a generalized inverse matrix that can be used to construct model and data resolution matrices as was done for the SVD solution in (3.63) and (3.77). The resolution matrices are

$$
{ \bf { R } } _ { \mathrm { { m } } } = { \bf { G } } ^ { \sharp } { \bf { G } } = { \bf { V } } { \bf { F } } { \bf { V } } ^ { T }
$$

and

$$
\mathbf { R } _ { \mathrm { d } } = \mathbf { G } \mathbf { G } ^ { \sharp } = \mathbf { U } \mathbf { F } \mathbf { U } ^ { T } .
$$

Note that the resolution matrices are dependent on the particular value of $\alpha$ (4.19).

# Example 4.2

In Example 4.1, with $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ as selected using the discrepancy principle, the model resolution matrix for zeroth-order Tikhonov regularization has the following diagonal elements:

$$
\begin{array} { l } { { \mathrm { l i a g } ( { \bf R } _ { \mathrm { m } } ) \approx [ 0 . 9 1 , 0 . 4 9 , 0 . 4 5 , 0 . 3 9 , 0 . 4 2 , 0 . 4 1 , 0 . 4 3 , 0 . 4 4 , 0 . 4 4 , . . . . } } \\ { { \mathrm { 0 . 4 5 , ~ 0 . 4 5 , ~ 0 . 4 4 , 0 . 4 4 , 0 . 4 3 , 0 . 4 1 , 0 . 4 2 , 0 . 3 9 , 0 . 4 5 , 0 . 4 9 , 0 . 9 1 ] } ^ { T } } } \end{array} .
$$

indicating that most model parameters are not well resolved. Figure 4.7 displays the effect of this limited resolution by applying $\mathbf { R } _ { \mathrm { m } }$ to the (true) spike model (3.63) or, equiva-lently, inverting noise-free spike model data using (4.6) for the regularization parameter value estimated using the discrepancy principle. Note that the result of limited resolution is that the true model “leaks”or“smears” into adjacent model parameters and is reduced in its maximum amplitude in the recovered model. In this example,the noise-free spike model recovery obtained in this resolution test is nearly identical to the recovery from the noisy spike model data using zeroth-order Tikhonov regulariza-tion (Figure 4.5), indicating that noise has only a very slight effect on model recovery accuracy. Thus, the diferences between the true and recovered models here are essentially entirely due to the regularization that was necessry to stabilize the solution, rather than from noise propagation from data to model (see Example 4.3). Figure 4.7 displays just a single row or column from the (symmetric) $\mathbf { R } _ { \mathrm { m } }$ ,but effects of limited resolu-tion can be examined more comprehensively by imaging the entire resolution matrix (Figure 4.8).

![](images/63f45a4ce048b065e1066a1c2dfc9f6f750c22924ae7d2ee08bd59c736e3a244.jpg)  
Figure4.7 Resolution test using the spike model $( \alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ determined from the discrepancy principle). Note that this model is nearly equivalent to that shown in Figure 4.5.

As in Chapter 2,we can compute a covariance matrix for the estimated model parameters using (B.65). Since

$$
\mathbf { m } _ { \alpha } = \mathbf { G } ^ { \sharp } \mathbf { d } ,
$$

the model covariance is

$$
\mathrm { C o v } ( { \bf m } _ { \alpha } ) = { \bf G } ^ { \sharp } \mathrm { C o v } ( { \bf d } ) ( { \bf G } ^ { \sharp } ) ^ { T } .
$$

![](images/aadb5e094a9db60d1c424d64e8d7d577a0cd1b451796453707fe9a87167ef1f8.jpg)  
Figure 4.9 Tikhonov solution and confidence intervals for the Shaw problem,estimated using (4.24), wherethe true model isaspikeandthedata noiseis independentand $N ( 0 , ( 1 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ The regularization parameter $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ was chosen using the discrepancy principle. The confidence interval is barely visible at this scale because inaccuracy in the model recovery is dominated by limited resolution.

Note that, as with the TSVD solution of Chapter 3, the Tikhonov regularized solution will generally be biased,and differences between the regularized solution values and the true model may actually be much larger than the confidence intervals obtained from the covariance matrix of the model parameters.Rather, the confidence intervals reflect the difference between $\mathbf { m } _ { \alpha }$ and $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$ . See Figure 4.9.

# Example 4.3

Recall our earlier example of the Shaw problem with the true spike model. Figure 4.9 shows the true model, the solution obtained using $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ chosen using the discrepancy principle,and $9 5 \%$ confidence intervals for the estimated parameters.Note that the confidence intervals are extremely tight,and that very few of the true model parameters are included within the confidence intervals. In this case,the regularization bias,which is not estimated by the covariance matrix,is far larger than the propagated data uncertainty. In other words, the inaccuracy in model recovery in this case is dominated by limited resolution rather than by noise propagation from data to model. The solution shown in Figure 4.9 is essentially identical to the product of $\mathbf { R } _ { \mathrm { m } }$ and $\mathbf { m } _ { \mathrm { t r u e } }$ shown in Figure 4.7 or the 1Oth column of the resolution matrix of Figure 4.8.

# 4.4.HIGHER-ORDER TIKHONOV REGULARIZATION

So far in our discussions of Tikhonov regularization we have minimized an objective function involving $\| \mathbf { m } \| _ { 2 }$ . In many situations,we would prefer to obtain a solution that minimizes some other measure of $\mathbf { m }$ ，expressed as $\mathbf { L m }$ ，such as the norm of the first or second derivative of $\mathbf { m }$ ,reflectinga preference for a“flat”or “smooth” model. We then solve the regularized least squares problem

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 } .
$$

As with (4.5),this can be rewritten as a standard linear least squares problem:

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

For example, if we have discretized our problem using simple collocation and our model is one-dimensional, then we can approximate, to a multiplicative constant, the first derivative of the model by a finite-difference operation $\mathbf { L } _ { 1 } \mathbf { m }$ ，where

$$
\mathbf { L } _ { 1 } = \left[ { \begin{array} { r r r r r r r } { - 1 } & { 1 } & & & & \\ & { - 1 } & { 1 } & & & \\ & & { \ddots } & { \ddots } & & \\ & & & { - 1 } & { 1 } & \\ & & & & & { - 1 } & { 1 } \end{array} } \right] .
$$

The matrices that are used to differentiate $\mathbf { m }$ for the purposes of regularization are commonly referred to as roughening matrices. In (4.27), $\mathbf { L } _ { 1 } \mathbf { m }$ is a finite-difference approximation that is proportional to the first derivative of m.By penalizing $\| \mathbf { L } _ { 1 } \mathbf { m } \| _ { 2 }$ ， we will favor solutions that are relatively flat (i.e.,in the limit, constant). Note that $\| \mathbf { L } _ { 1 } \mathbf { m } \| _ { 2 }$ is a seminorm because it is zero for any constant model, not just for $\mathbf { m } = \mathbf { 0 }$

In applying second-order Tikhonov regularization to a one-dimensional problem, we use a roughening matrix of the form

$$
\mathbf { L } _ { 2 } = \left[ { \begin{array} { r r r r r r r } { 1 } & { - 2 } & { 1 } & & & & \\ & { 1 } & { - 2 } & { 1 } & & & \\ & & { \ddots } & { \ddots } & { \ddots } & & \\ & & & { 1 } & { - 2 } & { 1 } & \\ & & & & { 1 } & { - 2 } & { 1 } \end{array} } \right] .
$$

Here, $\mathbf { L } _ { 2 } \mathbf { m }$ is a finite-difference approximation that is proportional to the second derivative of $\mathbf { m }$ ,and the seminorm term $\| \mathbf { L } _ { 2 } \mathbf { m } \| _ { 2 }$ in (4.25) penalizes solutions that are rough in a squared second derivative sense. We will refer to regularization strategies of the form of (4.25) that use $\mathbf { L } _ { 1 }$ and $\mathbf { L } _ { 2 }$ roughening matrices as first- and second-order Tikhonov regularization, respectively.

If our model is higher dimensional (e.g.,two or three dimensions), then the roughening matrices described here would not be appropriate. In such cases,second-order Tikhonov regularization is often implemented using a finite-difference approximation to the Laplacian operator of appropriate dimensionality (see Exercise 4.3).

To ensure that the least squares problem (4.26) has a unique solution, we wil require that the matrix

$$
A = \left[ \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } &  & & & & & & & & & & & & & & & & & & & & & & & & & \\ & & & & & & & & & & & & & & & & & & \\ & & & & & & & & & & & & & & & & & & \end{array} \right]
$$

has full column rank or equivalently that $N ( { \bf G } ) \cap N ( { \bf L } ) = \{ { \bf 0 } \}$

We have already seen how to apply zeroth-order Tikhonov regularization to solve (4.25), with $\mathbf { L } = \mathbf { I }$ , using the singular value decomposition (4.16). To solve and analyze higher-order Tikhonov regularization problems, we employ the generalized singular value decomposition, or GSVD [54, 62, 65]. The GSVD enables the solution (4.25) to be expressed as a sum of filter factors times generalized singular vectors in a manner that is analogous to the series representation of the generalized inverse solution (4.16).

Unfortunately, the definition of the GSVD and associated notation are not presently standardized. In the following,we will adhere to the conventions used by the MATLAB gsvd command where $\mathbf { G }$ is an $m$ by $n$ matrix and $\mathbf { L }$ isa $p$ by $n$ matrix. Although MATLAB's implementation of the GSVD can handle matrices $\mathbf { G }$ and $\mathbf { L }$ that have overlapping null spaces, we assume in the following derivation that the matrix in (4.29) has full column rank so that the solution to (4.26) will be unique.To further simplify the derivation we will also assume that rai $ \mathbf { \nabla } \mathrm { 1 k } ( \mathbf { L } ) = p$ .This is certainly true for the $\mathbf { L }$ matrices in (4.27) and (4.28). In general we can eliminate redundant rows from $\mathbf { L }$ to make $\mathbf { L }$ have full row rank.

Under the above assumptions there exist matrices U, V, X, $\pmb { \Lambda }$ , and M with the following properties and relationships:

： $\mathbf { U }$ is $m$ by $m$ and orthogonal. $\mathbf { v }$ is $p$ by $p$ and orthogonal. $\mathbf { x }$ is $n$ by $n$ and nonsingular. $\pmb { \Lambda }$ is an $m$ by $n$ matrix with diagonal entries that may be shifted from the main diagonal of the matrix. The diagonal entries are

$$
0 \leq \Lambda _ { 1 , k + 1 } \leq \Lambda _ { 2 , k + 2 } \leq \cdot \cdot \cdot \leq \Lambda _ { m , k + m } \leq 1
$$

where $k = 0$ when $m > n$ ,and $k = n - m$ when $m \leq n$

· $\mathbf { M }$ is a $p$ by $n$ diagonal matrix with

$$
M _ { 1 , 1 } \geq M _ { 2 , 2 } \geq \cdot \cdot \cdot \geq M _ { p , p } \geq 0 ,
$$

and

$$
\mathbf { M } ^ { T } \mathbf { M } + \mathbf { A } ^ { T } \mathbf { A } = \mathbf { I } .
$$

· The matrices $\mathbf { G }$ and $\mathbf { L }$ can be written as

$$
\mathbf { G } = \mathbf { U } \mathbf { A } \mathbf { X } ^ { T }
$$

and

$$
\mathbf { L } = \mathbf { V } \mathbf { M } \mathbf { X } ^ { T } .
$$

The generalized singular values of $\mathbf { G }$ and $\mathbf { L }$ are

$$
\gamma _ { i } = \frac { \lambda _ { i } } { \mu _ { i } }
$$

where

$$
\boldsymbol { \lambda } = \sqrt { \operatorname { d i a g } ( \mathbf { A } ^ { T } \mathbf { A } ) }
$$

and

$$
\begin{array} { r } { { \boldsymbol \mu } = \sqrt { \mathop { \mathrm { d i a g } } ( \mathbf { M } ^ { T } \mathbf { M } ) } . } \end{array}
$$

These definitions may seem somewhat odd, since the diagonal elements of $\pmb { \Lambda } ^ { T } \pmb { \Lambda }$ and $\mathbf { M } ^ { T } \mathbf { M }$ are simply squares of the diagonal elements of $\pmb { \Lambda }$ and $\mathbf { M }$ .The issue here is that the diagonals of $\pmb { \Lambda }$ and $\mathbf { M }$ are not of the same length. The effect of these definitions is to create vectors $\lambda$ and $\mu$ that are of length $n$ ， padding with zeros as needed.

Because of the ordering of $\lambda$ and $\mu$ ， the generalized singular values appear in ascending order with

$$
\gamma _ { 1 } \leq \gamma _ { 2 } \leq \cdot \cdot \cdot \leq \gamma _ { n } .
$$

Also note that if $\mu _ { i } = 0$ , then the corresponding generalized singular value $\gamma _ { i }$ is infinite or undefined.

Letting ${ \bf Y } = { \bf X } ^ { - T }$ (the inverse transpose), we can apply (4.33)and the orthogonality of $\mathbf { U }$ to show that

$$
\mathbf { Y } ^ { T } \mathbf { G } ^ { T } \mathbf { G } \mathbf { Y } = \mathbf { A } ^ { T } \mathbf { A } .
$$

Note that

$$
\lambda _ { i } = \sqrt { \mathbf { Y } _ { \cdot , i } ^ { T } \mathbf { G } ^ { T } \mathbf { G } \mathbf { Y } _ { \cdot , i } } = \Vert \mathbf { G } \mathbf { Y } _ { \cdot , i } \Vert _ { 2 } .
$$

Whenever $\lambda _ { i }$ is O,this means that the corresponding column of $\mathbf { Y }$ is in $N ( \mathbf G )$ . However, when $\lambda _ { i }$ is nonzero, the corresponding column of $\mathbf { Y }$ is not in $N ( \mathbf G )$ . Since $\mathbf { Y }$ is nonsingular, the columns of $\mathbf { Y }$ are linearly independent. If we pick $r$ so that $\lambda _ { r } = 0$ ,but $\lambda _ { r + 1 } \neq 0$ ，then $r$ is the dimension of $N ( \mathbf G )$ , and the vectors $\mathbf { Y } _ { \cdot , 1 } , \ \mathbf { Y } _ { \cdot , 2 } , \ \ldots \ , \ \mathbf { Y } _ { \cdot , r }$ form a basis for $N ( \mathbf G )$ . Note that because rank $( { \bf G } ) + \mathrm { d i m } ( N ( { \bf G } ) ) = n$ ，we have determined that rank $( \mathbf { G } ) = n - r$

Similarly, it is easy to use (4.34) and the orthogonality of $\mathbf { v }$ to show that

$$
\mathbf { Y } ^ { T } \mathbf { L } ^ { T } \mathbf { L } \mathbf { Y } = \mathbf { M } ^ { T } \mathbf { M } .
$$

Since rank $( \mathbf { L } ) = p$ , the dimension of the null space of $\mathbf { L }$ is $n - p$ .Thus $\mu _ { p + 1 }$ ， $\begin{array} { r } { \mu _ { p + 2 } , \ldots . } \end{array}$ $\mu _ { n }$ are O,and the vectors $\mathbf { Y } _ { \cdot , p + 1 }$ ， $\mathbf { Y } _ { \cdot , p + 2 }$ $\mathbf { Y } _ { \cdot , n }$ form a basis for $N ( \mathbf { L } )$ . Note that the columns of $\mathbf { Y }$ are not generally orthogonal, so we have not found orthonormal bases for the null spaces of $\mathbf { G }$ and $\mathbf { L }$

The GSVD may be computationally expensive (or intractable for very large problems) to evaluate. However, as with the SVD, once the decomposition matrices are computed, solutions to least squares problems may be calculated very easily. We begin by introducing the change of variables

$$
\mathbf { Y } \mathbf { x } = \mathbf { m } .
$$

With this substitution, the normal equations for (4.26) become

$$
\left( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) \mathbf { Y } \mathbf { x } = \mathbf { G } ^ { T } \mathbf { d } .
$$

Using (4.33) and (4.34), and ${ \bf Y } = { \bf X } ^ { - T }$ ,we have

$$
\begin{array} { r } { \left( \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { Y } ^ { - 1 } + \alpha ^ { 2 } \mathbf { Y } ^ { - T } \mathbf { M } ^ { T } \mathbf { V } ^ { T } \mathbf { V } \mathbf { M } \mathbf { Y } ^ { - 1 } \right) \mathbf { \Psi } \mathbf { Y } \mathbf { x } = \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } , } \\ { \left( \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { A } \mathbf { Y } ^ { - 1 } + \alpha ^ { 2 } \mathbf { Y } ^ { - T } \mathbf { M } ^ { T } \mathbf { M } \mathbf { Y } ^ { - 1 } \right) \mathbf { \Psi } \mathbf { Y } \mathbf { x } = \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } , } \end{array}
$$

and, finally,

$$
\left( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } \right) \mathbf { x } = \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } .
$$

The matrix on the left-hand side of this system of equations is diagonal. Multiplying both sides by the inverse of this diagonal matrix gives the solution

$$
x _ { i } = \frac { \lambda _ { i } \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } ^ { 2 } + \alpha ^ { 2 } \mu _ { i } ^ { 2 } } ,
$$

where,as in (4.30), $k = 0$ when $m > n$ ，and $k = n - m$ when $m \leq n$ . In terms of the generalized singular values,this can be written as

$$
x _ { i } = \frac { \gamma _ { i } ^ { 2 } } { \gamma _ { i } ^ { 2 } + \alpha ^ { 2 } } \frac { \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } } .
$$

Substituting this expression for $x _ { i }$ into $\mathbf { m } = \mathbf { Y } \mathbf { x }$ ,we obtain the summation formula

$$
{ \bf { m } } _ { \alpha , L } = \sum _ { i = 1 } ^ { n } { \frac { { \gamma } _ { i } ^ { 2 } } { { \gamma } _ { i } ^ { 2 } + { \alpha } ^ { 2 } } } \frac { { \bf { U } } _ { \cdot , i + k } ^ { T } \bf { d } } { { \lambda } _ { i } } { Y } _ { \cdot , i }
$$

where

$$
f _ { i } = \frac { \gamma _ { i } ^ { 2 } } { \gamma _ { i } ^ { 2 } + \alpha ^ { 2 } }
$$

are GSVD flter factors that are analogous to the filter factors obtained in the series expression for the zeroth-order Tikhonov regularized solution (4.17). In evaluating this sum,we sometimes encounter situations in which $\gamma _ { i }$ is infinite.In those cases, the filter factor $f _ { i }$ should be set to 1. Similarly, there are situations in which $\lambda _ { i } = 0$ and $\gamma _ { i } = 0$ ， producing an expression of the form $0 ^ { 2 } / 0$ in the sum. These terms should be treated as O.

When $\mathbf { G }$ comes from a Fredholm integral equation of the first kind, the GSVD typically has two properties that were also characteristic of the SVD. First, the $m$ nonzero generalized singular values $\prime _ { n } , \gamma _ { n - 1 } , \gamma _ { n - m + 1 }$ from (4.35) trend toward zero without any obvious break. Second, the vectors $\mathbf { U } _ { \cdot , i } , \mathbf { V } _ { \cdot , i } , \mathbf { X } _ { \cdot , i } ,$ and $\mathbf { Y } _ { \cdot , i }$ tend to become rougher as $\gamma _ { i }$ decreases.

# Example 4.4

We return to the vertical seismic profiling example previously discussed in Examples 1.3 and 1.9. Here, consider a $1 { - } \mathrm { k m }$ deep borehole experiment discretized using $m = n = 5 0$ observation and model points, corresponding to sensors every $2 0 ~ \mathrm { m }$ and $2 0 ~ \mathrm { m }$ thick, constant-slowness model layers. Figure 4.1O shows the test model that we will try to recover. A synthetic data set was generated with $N ( 0 , ( 2 \times 1 0 ^ { - 4 } \mathrm { s } ) ^ { 2 } )$ noise added.

The discretized system of equations $\mathbf { G m } = \mathbf { d }$ has a small condition number (64). This happens in part because we have chosen a very coarse discretization, which effectively regularizes the problem by discretization. Another reason is that the vertical seismic profiling problem is only mildly ill-posed [45]. Figure 4.11 shows the least squares solution, together with $9 5 \%$ confidence intervals.

From the statistical point of view, this solution is completely acceptable. However, suppose that from other information,we believe the slowness should vary smoothly with depth. We will next apply higher-order Tikhonov regularization to obtain smooth solutions to this problem.

Figure 4.12 shows the first-order Tikhonov regularization L-curve for this problem. The L-curve has a distinct corner near $\alpha \approx 1 2 2$ . Figure 4.13 shows the corresponding solution. The first-order regularized solution is much smoother than the least squares solution,and is much closer to the true solution.

Figure 4.14 shows the L-curve for second-order Tikhonov regularization, which has a corner near $\alpha \approx 1 9 6 5$ . Figure 4.15 shows the corresponding solution. This solution is smoother still compared to the first-order regularized solution.Both the first- and second-order solutions depart most from the true solution at shallow depths where the true slowness has the greatest slope and curvature. This happens because the first- and second-order Tikhonov regularized solutions are biased towards flatness and secondderivative smoothness, respectively.

Figure 4.16 shows filter factors corresponding to these first- and second-order solu-tions. Higher-order terms in (4.49)are severely downweighted in both cases, particularly in the second-order case. Because of the smoothness of the true model, the model seminorms can be reduced considerably through the selection of relatively large regularization parameters, $\alpha$ , without large data misfit increases. In this example the 2-norms of the difference between the first- and second-order solutions and the true model (discretized into 5O values) are approximately $1 . 2 \times 1 0 ^ { - 5 } ~ \mathrm { s / k m }$ and $1 . 0 \times 1 0 ^ { - 5 } \ \mathrm { s / k m }$ ， respectively.

![](images/f8ac13daf3af33e06fd6c1c81c52a29a19d9560452ca39467edc800c4d7db11c.jpg)  
Figure 4.12 L-curve and corner for the VSP problem,first-order regularization.   
Figure 4.13 Tikhonov solution for the VSP problem,first-order regularization, $\alpha = 1 2 2$ ，shown in comparison with the true model (Figure 4.10).

![](images/c5cc24f7455bbaa000256f0282a82f439e35c6a814170531921ae613d64436fa.jpg)  
Figure 4.14 L-curve and corner for the VSP problem,second-order regularization.   
Figure 4.15 Tikhonov solution for the VSP problem,second-order regularization, $\alpha = 2 3 4 1$ , shown in comparison with the true model (Figure 4.10).

# 4.5. RESOLUTION IN HIGHER-ORDER TIKHONOV REGULARIZATION

As with zeroth-order Tikhonov regularization, we can compute a resolution matrix for higher-order Tikhonov regularization. For a particular roughening matrix $\mathbf { L }$ and value of $\alpha$ , the Tikhonov regularization solution can be written as

$$
\mathbf { m } _ { \alpha , L } = \mathbf { G } ^ { \sharp } \mathbf { d }
$$

where

$$
\mathbf { G } ^ { \sharp } = ( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } ) ^ { - 1 } \mathbf { G } ^ { T } .
$$

Using the GSVD, we can write this expression as

$$
\begin{array} { r l } & { \mathbf { G } ^ { \sharp } = ( \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { X } ^ { T } + \alpha ^ { 2 } ( \mathbf { X } \mathbf { M } ^ { T } \mathbf { V } ^ { T } \mathbf { V } \mathbf { M } \mathbf { X } ^ { T } ) ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = ( \mathbf { X } \mathbf { A } ^ { T } \mathbf { A } \mathbf { X } ^ { T } + \alpha ^ { 2 } ( \mathbf { X } \mathbf { M } ^ { T } \mathbf { M } \mathbf { X } ^ { T } ) ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = ( \mathbf { X } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) \mathbf { X } ^ { T } ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = \mathbf { X } ^ { - T } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) ^ { - 1 } \mathbf { A } ^ { T } \mathbf { U } ^ { T } . } \end{array}
$$

The model resolution matrix is then

$$
\begin{array} { r l } & { \mathbf { R } _ { \mathrm { m } } = \mathbf { G } ^ { \sharp } \mathbf { G } } \\ & { \quad \quad = \mathbf { X } ^ { - T } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) ^ { - 1 } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { X } ^ { T } } \\ & { \quad \quad = \mathbf { X } ^ { - T } \mathbf { F } \mathbf { X } ^ { T } , } \end{array}
$$

where

$$
\mathbf { F } = \left( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } \right) ^ { - 1 } \mathbf { \Lambda } \mathbf { A } ^ { T } \mathbf { A }
$$

is a diagonal matrix of GSVD filter factors (4.50).

# Example 4.5

To examine the resolution of the Tikhonov regularized inversions of Example 4.4, we perform a spike test using (4.59). Figure 4.17 shows the effect of multiplying $\mathbf { R } _ { \mathrm { m } }$ times a unit amplitude spike model (at depth $5 0 0 ~ \mathrm { m } ,$ ）under first-and second-order Tikhonov regularization using $\alpha$ values of 122 and 2341,respectively. These curves can equivalently be conceptualized as rows/columns of the full resolution matrix at the index corresponding to $5 0 0 ~ \mathrm { m }$ .The spike test results indicate that these Tikhonov regularized solutions are smoothed versions of the spike model. Under first- or second-order regularization, the resolution of various model features will depend critically on how smooth or rough these features are in the true model. In Figures 4.13 and 4.15, the higher-order solutions recover the true model better because the true model is smooth. Conversely, the spike model is not well recovered because of its rapid variation.

# 4.6.THE TGSVD METHOD

In the discussion of the SVD in Chapter 3, we examined the TSVD method of regularization,which rejects model space basis vectors associated with smaller singular values. Equivalently, this can be thought of as a damped SVD solution in which filter factors of one are used for basis vectors associated with larger singular values,and filter factors of zero are used for basis vectors associated with smaller singular values.This approach can be extended to the GSVD solution (4.49) to produce a truncated generalized singular value decomposition or TGSVD solution. In the TGSVD solution we simply assign filter factors (4.5O) of one to the $q$ largest generalized singular values terms in the sum to obtain

$$
\mathbf { m } _ { q , L } = \sum _ { i = n - q + 1 } ^ { n } \frac { \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } } Y _ { \cdot , i }
$$

# Example 4.6

Applying the TGSVD method to the VSP problem, we find L-curve corners near $q = 8$ in the first-order case shown in Figure 4.18,and $q = 7$ in the second-order case shown in Figure 4.19. Examining the filter factors obtained for the corresponding Tikhonov solu-tions shown in Figure 4.16, we find that they decay precipitously with decreasing index near these locations.Figures 4.2O and 4.21 show the corresponding TGSVD solutions.

![](images/2e904022208bc3e41f3cb3b6c9716a902920b0c7e0c5f1bdc728d01afe3a9054.jpg)  
Figure 4.18 TGSVD L-curve for the VSP problem as a function of $q$ for first-order regularization with the $q = 8$ solution indicated.

![](images/5a7d99b6d7868ca8cd365bc44b210ca1ed29a67e389513f892042449e5844e43.jpg)  
Figure 4.19 TGSVD L-curve for the VSP problemas a function of $q$ for second-order regularization with the $q = 7$ solution indicated.   
Figure 4.20 TGSVD solution of the VSP problem, $q = 8$ ,first-order regularization,shown in comparison with the true model.

The model recovery is comparable to that obtained with the Tikhonov method. The 2-norms of the difference between the first- and second-order solutions and the true model are approximately $1 . 0 \times 1 0 ^ { - 2 } \mathrm { s / k m }$ and $7 . 1 \times 1 0 ^ { - 3 } \mathrm { s / k m }$ , respectively, which are similar to the Tikhonov solutions in Example 4.4.

# 4.7. GENERALIZED CROSS-VALIDATION

Generalized cross-validation (GCV) is an alternative method for selecting a regularization parameter, $\alpha$ , that has a number of desirable statistical properties.

In ordinary or“leave-one-out” cross-validation,we consider the models that are obtained by leaving one of the $m$ data points out of the fitting process.Consider the modified Tikhonov regularization problem in which we ignore a data point $d _ { k }$ ，

$$
\operatorname* { m i n } \sum _ { i \neq k } ( ( \mathbf G \mathbf { m } ) _ { i } - d _ { i } ) ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 }
$$

Call the solution tothis roblem $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ ， where the superscript indicates that $d _ { k }$ was left out ofthecomputation.Ideallythemodel $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ would accurately predict themsing data value $d _ { k }$ . In the leave-one-out approach, we select the regularization parameter $\alpha$ so as to minimize the predictive errors for all $k$ ：

$$
\operatorname* { m i n } g ( \alpha ) = \frac { 1 } { m } \sum _ { k = 1 } ^ { m } ( ( \mathbf { G } \mathbf { m } _ { \alpha , L } ^ { [ k ] } ) _ { k } - d _ { k } ) ^ { 2 } .
$$

Unfortunately, computing $g ( \alpha )$ involves solving $m$ problems of the form (4.62). Generalized cros-validation is a way to speed up this computation.

First, let

$$
\widetilde { d } _ { i } = \left\{ \begin{array} { l l } { ( { \bf G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } } & { i = k } \\ { d _ { i } } & { i \neq k . } \end{array} \right.
$$

Note that because $( \mathbf { G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } = \tilde { d } _ { k }$ ， $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ also solves

$$
\mathrm { m i n } ( ( { \bf G m } ) _ { k } - \tilde { d } _ { k } ) ^ { 2 } + \sum _ { i \neq k } ( ( { \bf G m } ) _ { i } - \tilde { d } _ { i } ) ^ { 2 } + \alpha ^ { 2 } \| { \bf L m } \| _ { 2 } ^ { 2 } ,
$$

which is equivalent to

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \tilde { \mathbf { d } } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 } .
$$

This result is known as the leave-one-out lemma. By this lemma,

$$
\mathbf { m } _ { \alpha , L } ^ { [ k ] } = \mathbf { G } ^ { \sharp } \tilde { \mathbf { d } } .
$$

We will use (4.67) to eliminate $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ from (4.63), because

$$
\frac { ( \mathbf { G } \mathbf { G } ^ { \sharp } \tilde { \mathbf { d } } ) _ { k } - ( \mathbf { G } \mathbf { G } ^ { \sharp } \mathbf { d } ) _ { k } } { \tilde { d } _ { k } - d _ { k } } = ( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } ,
$$

where $( \mathbf { G G } ^ { \sharp } ) _ { k , k }$ are the diagonal elements of the data resolution matrix (4.21). Subtracting both sides of the equation from 1 gives

$$
\frac { \tilde { d } _ { k } - d _ { k } - ( { \bf G } { \bf G } ^ { \sharp } \tilde { \bf d } ) _ { k } + ( { \bf G } { \bf G } ^ { \sharp } { \bf d } ) _ { k } } { \tilde { d } _ { k } - d _ { k } } = 1 - ( { \bf G } { \bf G } ^ { \sharp } ) _ { k , k } .
$$

Since $( \mathbf { G } \mathbf { G } ^ { \sharp } \mathbf { d } ) _ { k } = ( \mathbf { G } \mathbf { m } _ { \alpha , L } ) _ { k }$ $( \mathbf { G G } ^ { \sharp } \mathbf { \tilde { d } } ) _ { k } = \mathbf { \tilde { d } } _ { k } .$ and $( \mathbf { G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } = \tilde { d } _ { k } ,$ ，quation (4.69) simplifies to

$$
\frac { ( \mathbf { G } \mathbf { m } _ { \alpha , L } ) _ { k } - d _ { k } } { ( \mathbf { G } \mathbf { m } _ { \alpha , L } ^ { [ k ] } ) _ { k } - d _ { k } } = 1 - ( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } .
$$

Rearranging this formula and substituting into (4.63), we obtain

$$
g ( \alpha ) = \frac { 1 } { m } \sum _ { k = 1 } ^ { m } \left( \frac { ( { \bf G m } _ { \alpha , L } ) _ { k } - d _ { k } } { 1 - ( { \bf G } { \bf G } ^ { \sharp } ) _ { k , k } } \right) ^ { 2 } .
$$

We can simplify the formula further by replacing the $( \mathbf { G G } ^ { \sharp } ) _ { k , k }$ with the average value

$$
( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } \approx \frac { 1 } { m } \mathrm { T r } ( \mathbf { G } \mathbf { G } ^ { \sharp } ) ,
$$

which gives an expression for the (4.63) that can be evaluated as a function of $\alpha$ ：

$$
\begin{array} { c l } { { \displaystyle g ( { \boldsymbol \alpha } ) \approx \frac { 1 } { m } \sum _ { k = 1 } ^ { m } \frac { ( ( { \bf G m } _ { { \boldsymbol \alpha } , L } ) _ { k } - d _ { k } ) ^ { 2 } } { ( \frac { 1 } { m } ( m - \mathrm { T r } ( { \bf G G } ^ { \sharp } ) ) ) ^ { 2 } } } } \\ { { \displaystyle = \frac { m \| { \bf G m } _ { { \boldsymbol \alpha } , L } - { \bf d } \| _ { 2 } ^ { 2 } } { \mathrm { T r } ( { \bf I } - { \bf G G } ^ { \sharp } ) ^ { 2 } } . } } \end{array}
$$

It can be shown that under reasonable assumptions regarding the noise and smoothness of $\mathbf { m _ { \mathrm { t r u e } } }$ , the value of $\alpha$ that minimizes (4.74) approaches the value that minimizes $E [ \mathbf { G m } _ { \alpha , L } - \mathbf { d } _ { \mathrm { t r u e } } ]$ as the number of data points $m$ goes to infinity, and that under the same assumptions, $E [ \| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { \alpha , L } \| _ { 2 } ]$ goes to O as $m$ goes to infinity [36,170]. In practice,the size of the data set is fixed in advance,so the limit is not directly applicable. However, these results provide a theoretical justification for using the GCV method to select the Tikhonov regularization parameter.

# Example 4.7

Figures 4.22 and 4.23 show $g ( \alpha )$ for the VSP test problem, using first- and second-order Tikhonov regularization, respectively. Respective GCV function (4.74) minima occur

![](images/d7eb388b07f0c55e61b9f80de22d73af50a55424c8d2e847750115e3586a481f.jpg)  
Figure 4.22 GCV curve for the VSP problem and its minimum,first-order regularization.

![](images/b2efae813f9c2f7a285d82ceb0d12f028b38ad3d01ac0e295b5c2744b864297a.jpg)  
Figure 4.23 GCV curve for the VSP problem and its minimum,second-order regularization.   
Figure 4.24 GCV solution for the VSP problem,first-order, $\alpha = 7 6 . 3$ ,shown in comparison with the true model.

![](images/2ebdf2b563581777c3ca81a7d151ee59d6d31106b352be34f6f625b2272d70c2.jpg)  
Figure 4.25 GCV solution for the VSP problem,second-order, $\alpha = 9 8 1$ , shown in comparison with the true model.

near $\alpha = 7 6 . 3$ and $\alpha = 9 8 1$ ，which are somewhat smaller than the $\alpha$ values estimated previously using the L-curve (Example 4.4). The corresponding models (Figures 4.24 and 4.25) thus have somewhat larger seminorms.

# 4.8.ERROR BOUNDS

We next present two theoretical results that help to address the accuracy of Tikhonov regularization solutions. We will present these results in a simplified form, covering only zeroth-order Tikhonov regularization.

The first question is whether for a particular value of the regularization parameter, $\alpha$ ,we can establish a bound on the sensitivity of the regularized solution to the noise in the observed data d and/or errors in the system matrix $\mathbf { G }$ ，This would provide a sort of condition number for the inverse problem. Note that this does not tell us how far the regularized solution is from the true model, since Tikhonov regularization has introduced a bias in the solution. Under Tikhonov regularization with a nonzero $\alpha$ ，we would not obtain the true model even if the noise was O.

The following theorem gives a bound for zeroth-order Tikhonov regularization [65].A slightly more complicated formula is available for higher-order Tikhonov regularization [65].

Theorem 4.1 Suppose that the problems

$$
m i n \ \| \mathbf G \mathbf m - \mathbf d \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf m \| _ { 2 } ^ { 2 }
$$

and

$$
m i n \ \| \bar { \bf G } { \bf m } - \bar { \bf d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| { \bf m } \| _ { 2 } ^ { 2 }
$$

are solved to obtain $\mathbf { m } _ { \alpha }$ and $\bar { \mathbf { m } } _ { \alpha }$ . Then

$$
\frac { \| \mathbf { m } _ { \alpha } - \bar { \mathbf { m } } _ { \alpha } \| _ { 2 } } { \| \mathbf { m } _ { \alpha } \| _ { 2 } } \leq \frac { \bar { \kappa } _ { \alpha } } { 1 - \epsilon \bar { \kappa } _ { \alpha } } \left( 2 \epsilon + \frac { \| \mathbf { e } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } + \epsilon \bar { \kappa } _ { \alpha } \frac { \| \mathbf { r } _ { \alpha } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } \right)
$$

where

$$
\begin{array} { r l } & { \bar { \kappa } _ { \alpha } = \frac { \| \mathbf { G } \| _ { 2 } } { \alpha } } \\ & { \mathbf { E } = \mathbf { G } - \bar { \mathbf { G } } } \\ & { \mathbf { e } = \mathbf { d } - \bar { \mathbf { d } } } \\ & { \epsilon = \frac { \| \mathbf { E } \| _ { 2 } } { \| \mathbf { G } \| _ { 2 } } } \end{array}
$$

$$
\mathbf { d } _ { \alpha } = \mathbf { G } \mathbf { m } _ { \alpha }
$$

and

$$
\mathbf { r } _ { \alpha } = \mathbf { d } - \mathbf { d } _ { \alpha } .
$$

In the particular_case when $\mathbf { G } = \bar { \mathbf { G } }$ ， and the only difference between the two problems is $\mathbf { e } = \mathbf { d } - \bar { \mathbf { d } }$ ,the inequality becomes even simpler

$$
\frac { \| \mathbf { m } _ { \alpha } - \bar { \mathbf { m } } _ { \alpha } \| _ { 2 } } { \| \mathbf { m } _ { \alpha } \| _ { 2 } } \leq \bar { \kappa } _ { \alpha } \frac { \| \mathbf { e } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } .
$$

The condition number $\bar { \kappa } _ { \alpha }$ is inversely proportional to $\alpha$ . Thus increasing $\alpha$ will decrease the sensitivity of the solution to perturbations in the data.Of course, increasing $\alpha$ also increases the error in the solution due to regularization bias and decreases resolution.

The second question is whether we can establish any sort of bound on the norm of the difference between the regularized solution and the true model. This bound would incorporate both sensitivity to noise and the bias introduced by Tikhonov regularization. Such a bound must of course depend on the magnitude of the noise in the data. It must also depend on the particular regularization parameter chosen. Tikhonov developed a beautiful theorem that addresses this question in the context of inverse problems involving IFKs [161]. More recently, Neumaier has developed a version of Tikhonov's theorem that can be applied directly to discretized problems [116].

Recall that in a discrete ill-posed linear inverse problem,the matrix $\mathbf { G }$ commonly has a smoothing effect, in that when we multiply $\mathbf { G m }$ ，the result is smoother than m. Similarly, if we multiply $\mathbf { G m }$ by $\mathbf { G } ^ { T }$ , the result will be even smoother than $\mathbf { G m }$ This smoothing in such problems is a consequence of the fact that the singular vectors corresponding to the larger singular values of $\mathbf { G }$ are smooth.Note, however, that this is not a universal property of all matrices; for example, if $\mathbf { G }$ is a matrix that approximates the differentiation operator, then $\mathbf { G m }$ will be rougher than $\mathbf { m }$

For discrete ill-posed problems,models in the range of $\mathbf { G } ^ { T }$ will form a relatively smooth subspace of all possible models in $R ^ { n }$ . Models in this subspace can be written using the range of $\mathbf { G } ^ { T }$ as a basis as $\mathbf { m } = \mathbf { G } ^ { T } \mathbf { w }$ ,using the coefficients w. Furthermore, models in the range of $\mathbf { G } ^ { T } \mathbf { G }$ form a subspace of $R ( \mathbf { G } ^ { T } )$ , since any model in $R ( \mathbf G ^ { T } \mathbf G )$ can be written as $\mathbf { m } = \mathbf { G } ^ { T } ( \mathbf { G } \mathbf { w } )$ ， which is a linear combination of columns of $\mathbf { G } ^ { T }$ Because of the smoothing effect of $\mathbf { G }$ and $\mathbf { G } ^ { T }$ ， we would expect these models to be even smoother than the models in $R ( \mathbf G ^ { T } )$ . We could construct smaller subspaces of $R ^ { n }$ that contain even smoother models, but it turns out that with zeroth-order Tikhonov regularization these are the only subspaces of interest.

There is another way to see that models in $R ( \mathbf G ^ { T } )$ will be relatively smooth. Recall that the vectors $\mathbf { V } _ { \cdot , 1 } , \mathbf { V } _ { \cdot , 2 } , \ldots . \cdot , \mathbf { V } _ { \cdot , p }$ from the SVD of $\mathbf { G }$ form an orthonormal basis for $R ( \mathbf { G } ^ { T } )$ . For discrete ill-posed problems, we know from Chapter 3 that these basis vectors will be relatively smooth,so linear combinations of these vectors in $R ( \mathbf G ^ { T } )$ should be smooth.

The following theorem gives a bound on the total error including bias due to regularization and error due to noise in the data for zeroth-order Tikhonov regularization [116].

Theorem 4.2 Suppose that we use zeroth-order Tikhonov regularization with regularization parameter α to solve $\mathbf { G m } = \mathbf { d }$ ，and that $\mathbf { m _ { \mathrm { t r u e } } }$ can be expressed as one of the following distinct cases, for some W, and as parameterized by $p$ ，

$$
\mathbf { m } _ { \mathrm { t r u e } } = \left\{ \begin{array} { l l } { \mathbf { G } ^ { T } \mathbf { w } } & { p = 1 } \\ { \mathbf { G } ^ { T } \mathbf { G } \mathbf { w } } & { p = 2 } \end{array} \right.
$$

and that

$$
\| \mathbf { G m } _ { \mathrm { t r u e } } - \mathbf { d } \| _ { 2 } \leq \Delta \| \mathbf { w } \| _ { 2 }
$$

for some $\Delta > 0$ . Then

$$
\| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { G } ^ { \sharp } \mathbf { d } \| _ { 2 } \leq \left( \frac { \Delta } { 2 \alpha } + \gamma \alpha ^ { p } \right) \| \mathbf { w } \| _ { 2 } ,
$$

where

$$
\gamma = \left\{ { \begin{array} { l l } { 1 / 2 } & { p = 1 } \\ { 1 } & { p = 2 } \end{array} } . \right.
$$

Furthermore, if we begin with the bound

$$
\| \mathbf { G m } _ { \mathrm { t r u e } } - \mathbf { d } \| _ { 2 } \leq \delta ,
$$

we can let

$$
\Delta = { \frac { \delta } { \| \mathbf { w } \| _ { 2 } } } .
$$

Under this condition the optimal value ofα is

$$
\hat { \alpha } = \left( \frac { \Delta } { 2 \gamma p } \right) ^ { \frac { 1 } { p + 1 } } = { \cal O } ( \Delta ^ { \frac { 1 } { p + 1 } } ) .
$$

With this choice of $\alpha$

$$
\Delta = 2 \gamma p \hat { \alpha } ^ { p + 1 }
$$

and the eror bound simplifes to

$$
\begin{array} { r } { \| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { G } _ { \hat { \alpha } } ^ { \sharp } \mathbf { d } \| _ { 2 } \leq \gamma ( p + 1 ) \hat { \alpha } ^ { p } | | \mathbf { w } | | _ { 2 } = O ( \Delta ^ { \frac { p } { p + 1 } } ) . } \end{array}
$$

Theorem 4.2 tels us that the error in the Tikhonov regularization solution depends on both the noise level $\delta$ and on the regularization parameter $\alpha$ . For larger values of $\alpha$ , the error due to regularization in recovering the true model will be dominant. For smaller values of $\alpha$ ,the error due to noise in the data will be dominant.We seek the optimal value of $\alpha$ that best balances these effects.Using the optimal $\alpha$ , (4.93) indicates that we can obtain an error bound of $O ( \Delta ^ { 2 / 3 } )$ if $p = 2$ ,and an error bound of $O ( \Delta ^ { 1 / 2 } )$ if $p = 1$

Of course, the above result can only be applied when our true model lives in the restricted subspace of $R ( \mathbf { G } ^ { T } )$ . In practice,even if the model does lie in $R ( \mathbf { G } ^ { T } )$ ，the vector w could have a very large norm, making the bound uninformative.

Thus, applying this theorem in a quantitative fashion is typically impractical. However, the theorem does provide some useful insight into the ability of Tikhonov regularization to recover a true model. The first point is that the accuracy of the regu-larized solution depends very much on the smoothness of the true model. If $\mathbf { m _ { \mathrm { t r u e } } }$ is not smooth, then Tikhonov regularization simply will not give an accurate solution. Furthermore, if the model $\mathbf { m _ { \mathrm { t r u e } } }$ is smooth, then we can hope for an error in the Tikhonov regularized solution which is ${ \cal O } ( \delta ^ { 1 / 2 } )$ or $O ( \delta ^ { 2 / 3 } )$ . Another way of saying this is that we can hope at best for an answer with about two thirds as many correct significant digits as the data.

# Example 4.8

Recall the Shaw problem previously considered in Examples 4.1 and 4.3. Because $\mathbf { G } ^ { T }$ is a nonsingular matrix, the spike model should lie in $R ( \mathbf { G } ^ { T } )$ . However, $\mathbf { G } ^ { T }$ is numerically singular due to the ill-posedness of the problem,and the spike model thus lies outside of the effective range of $\mathbf { G } ^ { T }$ . Any unregularized attempt to find w produces a meaningless answer due to numerical instability. Because the spike model does not lie in $R ( \mathbf { G } ^ { T } )$ ， Theorem 4.2 does not apply.

Figure 4.26 shows a smooth model that does lie in the range of $\mathbf { G } ^ { T }$ . For this model we constructed a synthetic data set with noise as before at $\delta = 4 . 4 7 \times 1 0 ^ { - 6 }$ . Equa-tion (4.93) suggests using $\alpha = 8 . 0 \times 1 0 ^ { - 4 }$ . The resulting error bound is $8 . 0 \times 1 0 ^ { - 4 }$ ， while the actual norm of the model error is $6 . 6 \times 1 0 ^ { - 4 }$ . Here the data were accurate to roughly six digits, while the solution was accurate to roughly four digits. Figure 4.27 shows the reconstruction of the model with $N ( 0 , ( 1 . 0 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise added to the data vector, showing that the solution is well recovered. This example once again demon-strates the importance of smoothness in the true model in determining how accurately it can be reconstructed with Tikhonov regularization.

![](images/cc5b2bc8fd6eb25c5fa55d6ba69da8f997e56f36af13a84d013edde4181da312.jpg)  
Figure 4.26 A smooth model in $R ( \mathbf G ^ { T } )$

![](images/b062e076f44b41c3975a13218efdf102a7802527e9396824482b6b551cdd66a5.jpg)  
Figure 4.27 Reconstruction of the smooth model with $N ( 0 , ( 1 . 0 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise.

# 4.9. EXERCISES

1. Use the method of Lagrange multipliers (Appendix C) to derive the damped least squares problem (4.4) from the discrepancy principle problem (4.2),and demonstrate that (4.4) can be written as (4.5).

2. Consider the integral equation and data set from Problem 3.5. You can find a copy of this data set in the file ifk.mat.

a. Discretize the problem using simple collocation.

b.Using the data supplied,and assuming that the numbers are accurate to four significant figures, determine a reasonable bound δ for the misfit.

c.Use zeroth-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

d.Use first-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

e.Use second-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

f.Analyze the resolution of your solutions. Are the features you see in your inverse solutions unambiguously real? Interpret your results. Describe the size and location of any significant features in the solution.

3. Consider the following problem in cross-well tomography. Two vertical wells are located $1 6 0 0 \mathrm { ~ m ~ }$ apart.A seismic source is inserted in one well at depths of 50,150,. ．．, $1 5 5 0 ~ \mathrm { m }$ . A string of receivers is inserted in the other well at depths of $5 0 ~ \mathrm { m }$ ， $1 5 0 \ \mathrm { m }$ 。.， $1 5 5 0 \mathrm { ~ m ~ }$ . See Figure 4.28. For each source-receiver pair,a travel time is recorded, with a measurement standard deviation of $0 . 5 ~ \mathrm { m s }$ . There are 256 ray paths and 256 corresponding data points. We wish to determine the velocity structure in the two-dimensional plane between the two wells.

Discretizing the problem into a 16 by 16 grid of 10O meter by 10O meter blocks gives 256 model parameters. The $\mathbf { G }$ matrix and noisy data,d, for this problem (assuming straight ray paths) are in the file crosswell.mat. The order of parameter indexing from the slowness grid to the model vector is row by row (e.g., Example 1.12).

a.Use the TSVD to solve this inverse problem using an L-curve. Plot the result.   
b. Use zeroth-order Tikhonov regularization to solve this problem and plot your solution.Explain why it is difficult to use the discrepancy principle to select the regularization parameter. Use the L-curve criterion to select your regularization parameter. Plot the L-curve as well as your solution.   
c.Use second-order Tikhonov regularization to solve this problem and plot your solution.Because this is a two-dimensional problem, you wil need to implement a finite-difference approximation to the Laplacian (second derivative in the

horizontal direction plus the second derivative in the vertical direction） in the roughening matrix. The $\mathbf { L }$ matrix can be generated using the following MATLAB code:

L=zeros( $1 4 \star 1 4 , 2 5 6 )$ ；   
$k { = } 1$ ；   
for $\mathsf { i } = 2 : 1 5$ ， for $\mathrm { j } = 2 : 1 5$ ， $\mathsf { M } =$ zeros(16,16); $\mathsf { M } ( \mathrm { ~ i ~ } , \mathrm { ~ j ~ } ) = - 4$ ； M(i, $\mathrm { j } + 1 ) = 1$ ； M $1 ( \mathrm { ~ i ~ } , \mathrm { ~ j ~ } \cdot 1 ) { = } 1$ ； $\mathsf { M } ( \mathrm { ~ i + 1 ~ } , \mathrm { ~ j ~ } ) { = } \mathrm { 1 }$ ； $\mathsf { M } ( \mathrm { ~ i ~ } - 1 , \mathrm { ~ j ~ } ) { = } \mathrm { 1 }$ ； L(k，:) $=$ reshape(M,256,1)'; $k { = } k { + } 1$ ； end   
end

What, if any, problems did you have in using the L-curve criterion on this problem? Plot the L-curve as well as your solution.

d. Discuss your results. If vertical bands appeared in some of your solutions, can you explain why?

4.Apply second-order Tikhonov regularization to solve the problem of finding a smooth curve that approximately fits a set of noisy data points. Write a MAT-LAB program to find a function specified at the 191 points $x = 1$ ,1.1,1.2,  . . ,20 that approximately fits the 2O data points specified at $x = 1$ ,2,3,..．,20 given in the file interpdata.mat. Construct an appropriate 2O by $1 9 1 \textbf { G }$ matrix,and use the library function get_lrough to obtain the necessary second-order roughening matrix, L. Produce solutions for regularization parameter values of $\alpha =$ 0.2, 0.4, O.6,...，1O and show the tradeoff curve between 2-norm data misfit and model seminorm on a linear-linear plot. If the data noise is independent and normally distributed with a standard deviation of O.3,use the discrepancy principle to find and plot an optimal interpolated curve along with the data points. What is the $\chi ^ { 2 }$ value of this solution? Is it reasonable?

5. In some situations it is appropriate to bias the regularized solution toward a particular model $\mathbf { m } _ { 0 }$ . In this case, we would solve

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L ( m - m } _ { 0 } ) \| _ { 2 } ^ { 2 } .
$$

Write this as an ordinary linear least squares problem. What are the normal equations? Can you find a solution for this problem using the GSVD?

# 4.10.NOTES AND FURTHER READING

Hansen’s book [65] is a very complete reference on the linear algebra of Tikhonov regularization. Arnold Neumaier's tutorial [116] is also a very useful reference. Two other surveys of Tikhonov regularization are [44, 45]. Vogel [169] includes an extensive discussion of methods for selecting the regularization parameter. Hansen's MATLAB Regularization Tools [64] is a collection of software for performing regularization within MATLAB.

The GSVD was first defined by Van Loan [1O1]. References on the GSVD and algorithms for computing the GSVD include [3, 53, 62, 65].

Selecting the regularization parameter is an important problem in both theory and practice.Much of the literature on functional analytic approaches assumes that the noise level is known. When the noise level is known, the discrepancy principle provides a scheme for selecting the regularization parameter for il-posed problems that is conver-gent in the sense that, in the limit as the noise level goes to zero, the regularized solution goes to $\mathbf { m _ { \mathrm { t r u e } } }$ [45].

In practice, the noise level is often unknown, so there has been a great deal of interest in schemes for selecting the regularization parameter without its prior knowledge. The two most popular approaches are the L-curve method and GCV. The L-curve method was introduced by Hansen [63, 65]. GCV was introduced by Craven and Wahba [36, 170]. The formula for GCV given here is very expensive to compute for large problems. A GCV algorithm for large-scale problems is given by Golub and von Matt [54]. Vogel has shown that the L-curve method can fail to converge [168]. It can be shown that no scheme that depends only on noisy data without knowledge of the noise level can be convergent in the limit as the noise level goes to zero [45].

Within statistics, poorly conditioned linear regression problems are said to sufer from “multicollinearity”A method called“ridge regression,” which is identical to Tikhonov regularization,is often used to deal with such problems [4O]. Statisticians also use a method called “principal components regression” (PCR)，which is identical to the TSVD method [113].

# Discretizing Problems Using Basis Functions

# Synopsis

Techniques for discretizing continuous inverse problems characterized by Fredholm integral equations of the first kind using continuous basis functions are discussed,both for general basis functions and for representers. The Gram matrix is defined and used in analyzing these problems. The method of Backus and Gilbert is also introduced.

# 5.1.DISCRETIZATION BY EXPANSION OF THE MODEL

To this point,we have discretized continuous inverse problems using the collocation scheme discussed in Chapter 1. In this chapter, we discuss an alternative approach in which we expand the unknown model $m ( x )$ in terms of a set of basis functions.

We begin with a Fredholm integral equation of the first kind,

$$
d ( x ) = \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) d \xi .
$$

Note from Section A.11 that we can generalize linear algebra, including the concepts of linear independence, dot products,orthogonality, and the 2-norm, to spaces defined by functions. We will assume that our model $m ( x )$ lies in the space $L _ { 2 } ( a , \ b )$ of functions that are square integrable on $[ a , b ]$

In $L _ { 2 } ( a , \ b )$ , the dot product of two functions $f ( x )$ and $g ( x )$ is defined as

$$
\langle f ( x ) , g ( x ) \rangle = \intop _ { a } ^ { b } f ( x ) g ( x ) \ d x ,
$$

the 2-norm of $f ( x )$ is

$$
\| f ( x ) \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } f ( x ) ^ { 2 } ~ d x } } ,
$$