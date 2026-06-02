and the distance between two functions under this norm is

$$
\| f ( x ) - g ( x ) \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } ( f ( x ) - g ( x ) ) ^ { 2 } ~ d x } } .
$$

Ideally, we could try to solve the Tikhonov regularization problem

$$
\begin{array} { c } { \displaystyle \operatorname* { m i n } _ { { \mathbf \xi } } \| m ( x ) \| _ { 2 } } \\ { \displaystyle \left\| \displaystyle \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) \ d \xi - d ( x ) \right\| _ { 2 } \le \Delta . } \end{array}
$$

However, in practical cases,we do not fully know $d ( x )$ in the sense that we normally have a finite number of data points $d _ { 1 } = d ( x _ { 1 } )$ ， $d _ { 2 } = d ( x _ { 2 } )$ ，.， $d _ { m } = d ( x _ { m } )$ arranged in a vector d. An appropriate approach is thus to minimize the model norm $\| m ( x ) \| _ { 2 }$ subject to a constraint on the misfit at the data points:

$$
\begin{array} { c } { { \operatorname* { m i n } \| m ( x ) \| _ { 2 } } } \\ { { \| \mathbf { g } ( m ( x ) ) - \mathbf { d } \| _ { 2 } \leq \delta , } } \end{array}
$$

where

$$
\mathbf { g } ( m ) = \left[ \begin{array} { l } { b } \\ { \int _ { a } ^ { b } g ( x _ { 1 } , \xi ) m ( \xi ) \ d \xi } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { 2 } , \xi ) m ( \xi ) \ d \xi } } \\ { \int _ { a } ^ { b } g ( x _ { 2 } , \xi ) m ( \xi ) \ d \xi } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \end{array} \right] .
$$

Consider a finite dimensional subspace $H$ of $L _ { 2 } ( a , \ b )$ ,with the basis

$$
h _ { 1 } ( x ) , h _ { 2 } ( x ) , . . . . , h _ { n } ( x )
$$

so that any model $m ( x )$ in the subspace $H$ can be written uniquely as

$$
m ( x ) = \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( x ) .
$$

We will seek the model $m ( x )$ in $H$ that has minimum norm and adequately fits the data.

Substituting (5.9) into (5.1),and considering only those points $x _ { i }$ where we have data, we obtain

$$
d ( x _ { i } ) = \int _ { a } ^ { b } g ( x _ { i } , \xi ) \left( \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( \xi ) \right) d \xi \quad i = 1 , 2 , . . . , m .
$$

To simplify the notation, let

$$
g _ { i } ( \xi ) = g ( x _ { i } , \xi ) \quad i = 1 , 2 , . ~ . ~ . ~ , m
$$

and

$$
d _ { i } = d ( x _ { i } ) \quad i = 1 , 2 , \ldots , m .
$$

We interchange the integral and sum to get

$$
d _ { i } = \sum _ { j = 1 } ^ { n } \beta _ { j } \int _ { a } ^ { b } g _ { i } ( x ) h _ { j } ( x ) \ d x \quad i = 1 , 2 , . . . \ , m .
$$

If we let $\mathbf { G }$ be the $m \times n$ matrix with entries

$$
G _ { i , j } = \int _ { a } ^ { b } g _ { i } ( x ) h _ { j } ( x ) \ d x ,
$$

then the discretized inverse problem can be written as

$$
\mathbf { G } { \boldsymbol { \beta } } = \mathbf { d } ,
$$

which can be solved to find the functional expansion coefficients $\beta$ in (5.9) to construct the desired model.

Because of noise in the data, we do not normally desire, nor wil we be generally able, to solve (5.15) exactly. Furthermore,we typically need to regularize our solution to the inverse problem. We could try to solve

$$
\begin{array} { c } { { \operatorname* { m i n } \| \pmb { \beta } \| _ { 2 } } } \\ { { \| \mathbf { G } \pmb { \beta } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

However, $\| { \boldsymbol { \beta } } \| _ { 2 }$ is generally not proportional to $\| m ( x ) \| _ { 2 }$ . Instead, note that

$$
\begin{array} { l } { { \displaystyle \| m ( x ) \| _ { 2 } ^ { 2 } = \int _ { \quad \^ { d } } ^ { b } m ( x ) ^ { 2 } ~ d x } } \\ { { \displaystyle \qquad = \int _ { a } ^ { b } ~ \left( \sum _ { i = 1 } ^ { n } \beta _ { i } h _ { i } ( x ) \right) ~ \left( \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( x ) \right) ~ d x } } \\ { { \displaystyle \qquad = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \beta _ { i } \beta _ { j } \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) ~ d x . } } \end{array}
$$

If we let $\mathbf { H }$ be the $n$ by $n$ matrix with

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) \ d x ,
$$

then

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \pmb { \beta } ^ { T } \mathbf { H } \pmb { \beta } .
$$

The matrix $\mathbf { H }$ is called the Gram matrix of the functions $h _ { i } ( x )$ . It is relatively easy to show that $\mathbf { H }$ is a symmetric and positive definite matrix,and thus has a Cholesky factorization

$$
{ \displaystyle { \bf H } = { \bf R } ^ { T } { \bf R } } ,
$$

so that

$$
\begin{array} { c } { \| m ( \boldsymbol { x } ) \| _ { 2 } ^ { 2 } = \beta ^ { T } \mathbf { R } ^ { T } \mathbf { R } \beta } \\ { = \| \mathbf { R } \beta \| _ { 2 } ^ { 2 } . } \end{array}
$$

We can write the Tikhonov regularization problem as

$$
\operatorname* { m i n } _ { \| \mathbf { G } \pmb { \beta } - \mathbf { d } \| _ { 2 } } \interleave _ { 2 }
$$

We can use the Lagrange multiplier technique (Appendix $\textrm { C }$ ） to turn this into an unconstrained minimization problem

$$
\operatorname* { m i n } \ \| \mathbf { G } { \boldsymbol { \beta } } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { R } { \boldsymbol { \beta } } \| _ { 2 } ^ { 2 } ,
$$

where the regularization parameter $\alpha$ is selected so that we obtain a solution that adequately fits the data. This problem can easily be solved using the Cholesky factorization of the normal equations, the generalized singular value decomposition, or iterative methods discussed in Chapter 6.

Note that if we choose an orthonormal basis of functions, then

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) \ d x = { \left\{ \begin{array} { l l } { 1 } & { i = j } \\ { 0 } & { i \not = j } \end{array} \right. }
$$

or ${ \bf H } = { \bf R } = { \bf I }$ ,and the minimization problem simplifies to (5.16).

To minimize a model derivative norm (e.g., $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ instead of $\| m ( x ) \| _ { 2 } )$ , note that because

$$
m ^ { \prime \prime } ( x ) = \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ^ { \prime \prime } ( x ) ,
$$

we can simply use the second derivative Gram matrix

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ^ { \prime \prime } ( x ) h _ { j } ^ { \prime \prime } ( x ) \ d x
$$

instead of (5.18).

The simple collocation scheme described in Chapter 1 can also be thought of as a special case of this approach,in which the $h _ { i } ( x )$ basis functions are“boxcar” functions centered at the measurement points $x _ { i }$ .A variety of other bases have been used in practice.For example, sine and cosine functions can be used to produce solutions that are Fourier series,and,for problems involving spherical symmetries,the spherical harmonic functions are often used. In recent years, many researchers have investigated the use of wavelet bases in the solution of inverse problems.

The choice of the finite dimensional subspace $H$ and its basis is critical to the success of this method in solving practical problems.As we have seen, the method finds the model $m ( x )$ in the subspace $H$ that minimizes $\| m ( x ) \| _ { 2 }$ subject to fitting the data. There is no guarantee that the model we obtain will actually have the minimum norm over the entire space $L _ { 2 } ( a , \ b )$ . However, if the subspace includes a sufficiently large class of functions, the resulting solution may be an adequate approximation to the solution of (5.6).

# 5.2. USING REPRESENTERS AS BASIS FUNCTIONS

A particularly interesting choice of basis is to use the representers (1.33) themselves as the basis functions. This approach results in a solution that does effectively minimize $\| m ( x ) \| _ { 2 }$ over the entire space $L _ { 2 } ( a , \ b )$

Consider the space $G$ spanned by the representers

$$
g _ { j } ( \xi ) = g ( x _ { j } , \xi ) \quad j = 1 , 2 , . ~ . ~ . ~ , m .
$$

Let $G ^ { \perp }$ be the perpendicular complement of $G . \ G ^ { \perp }$ consists of the functions $f ( x )$ in $L _ { 2 } ( a , b )$ such that

$$
\int _ { a } ^ { b } f ( x ) g _ { j } ( x ) \ d x = 0 \quad j = 1 , 2 , . . . , m .
$$

Thus every function $f ( x )$ in $G ^ { \perp }$ is in the null space of the forward operator. Every function $m ( x )$ in $L _ { 2 } ( a , \ b )$ can be written uniquely as

$$
m ( x ) = m _ { 1 } ( x ) + m _ { 2 } ( x )
$$

where $m _ { 1 } ( x )$ is in $G$ and $m _ { 2 } ( x )$ is in $G ^ { \perp }$ . By the Pythagorean theorem,

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \| m _ { 1 } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ( x ) \| _ { 2 } ^ { 2 } .
$$

Since any nonzero function $m _ { 2 } ( x )$ would have no effect on the fit to the data but would increase $\| m ( x ) \| _ { 2 }$ ， the optimal norm-minimizing solution to (5.6） will always have $m _ { 2 } ( x ) = 0$ . This means that minimizing $\| m ( x ) \| _ { 2 }$ over our subspace $G$ will be equivalent to minimizing $\| m ( x ) \| _ { 2 }$ over all of $L _ { 2 } ( a , \ b )$

The Gram matrix of the representers, $\mathbf { \Gamma } ^ { \Gamma }$ ,has entries

$$
\Gamma _ { i , j } = \int _ { a } ^ { b } g _ { i } ( x ) g _ { j } ( x ) \ d x .
$$

In terms of this matrix,

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \pmb { \beta } ^ { T } \pmb { \Gamma } \pmb { \beta } ,
$$

so that the discretized Tikhonov regularization problem (5.22) becomes

$$
\begin{array} { l } { \operatorname* { m i n } \| \mathbf { R } \pmb { \beta } \| _ { 2 } } \\ { \| \mathbf { r } \pmb { \beta } - \mathbf { d } \| _ { 2 } \le \delta , } \end{array}
$$

where $\mathbf { R }$ is the Cholesky factorization of $\mathbf { \Gamma } ^ { \Gamma }$

Can we extend this approach to minimizing a derivative-based model roughness measure (e.g., $\| m ^ { \prime \prime } ( x ) ) \|$ as we did in (5.26)? It is still true that adding a nonzero function $m _ { 2 } ( x )$ from $G ^ { \perp }$ to $m ( x )$ will have no effect on the fit to the data. Unfortunately, derivatives of models in $G$ and $G ^ { \perp }$ will no longer generally satisfy the orthogonality relationship (5.30), that is,

$$
\| m ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } \neq \| m _ { 1 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } ,
$$

because orthogonality of two functions $f ( x )$ and $g ( x )$ does not imply orthogonality of $f ^ { \prime \prime } ( x )$ and $g ^ { \prime \prime } ( x )$ . Because adding a nonzero function $m _ { 2 } ( x )$ from $G ^ { \perp }$ might actually decrease $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ ，minimizing $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ over our subspace $G$ in this case will not be equivalent to minimizing over $L _ { 2 } ( a , b )$

# 5.3.THE METHOD OF BACKUS AND GILBERT

The method of Backus and Gilbert [2, 126] is applicable to continuous linear inverse problems of the form

$$
d ( x ) = \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) \ d \xi ,
$$

where we have observations at points $x _ { 1 } , x _ { 2 } , . . . . , x _ { n }$ .Let

$$
d _ { j } = d ( x _ { j } ) \quad j = 1 , 2 , \ldots , m
$$

and

$$
g _ { j } ( \xi ) = g ( x _ { j } , \xi ) \quad j = 1 , 2 , . ~ . ~ . ~ , m .
$$

Using (5.35), we can write the $d _ { j }$ in terms of the true model, $m _ { \mathrm { t r u e } }$ ,as

$$
\begin{array} { l } { { d _ { j } = \displaystyle \int _ { a } ^ { b } g ( x _ { j } , \xi ) m _ { \mathrm { t r u e } } ( \xi ) \ d \xi } } \\ { { \displaystyle \quad = \displaystyle \int _ { a } ^ { b } g _ { j } ( \xi ) m _ { \mathrm { t r u e } } ( \xi ) \ d \xi . } } \end{array}
$$

The Backus and Gilbert method estimates $m _ { \mathrm { t r u e } } ( x )$ at some point $\hat { x }$ ， given the $m$ data values $d _ { j }$ . The method produces model estimates that are linear combinations of the data elements

$$
\hat { m } = \sum _ { j = 1 } ^ { m } c _ { j } d _ { j } \approx m _ { \mathrm { t r u e } } ( \hat { x } )
$$

where the coefficients $c _ { j }$ are to be determined.

Combining (5.37) and (5.38) gives

$$
\begin{array} { l } { { \displaystyle { \hat { m } } = \sum _ { j = 1 } ^ { m } c _ { j } \int _ { a } ^ { b } g _ { j } ( x ) m _ { \mathrm { t r u e } } ( x ) ~ d x } } \\ { { \displaystyle ~ = \int _ { a } ^ { b } \left( \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) \right) m _ { \mathrm { t r u e } } ( x ) ~ d x } } \\ { { \displaystyle ~ = \int _ { a } ^ { b } A ( x ) m _ { \mathrm { t r u e } } ( x ) ~ d x } , } \end{array}
$$

where

$$
A ( x ) = \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) .
$$

The function $A ( x )$ is caled an averaging kernel. Ideally we would like the averaging kernel to closely approximate a delta function

$$
A ( x ) = \delta ( x - \hat { x } )
$$

because, assuming exact data, (5.4O) would then produce exact agreement between the true and estimated model $( \hat { m } = m _ { \mathrm { t r u e } } ( \hat { x } ) )$ . Since this is not possible,we will instead select the coefficients so that the area under the averaging kernel is one,and so that the width of the averaging kernel around $\hat { x }$ is as small as possible.

In terms of the coefficients $\mathbf { c }$ , the unit area constraint can be writen as

$$
\int _ { a } ^ { b } A ( x ) \ d x = \int _ { a } ^ { b } \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) \ d x = \sum _ { j = 1 } ^ { m } c _ { j } \ \left( \int _ { a } ^ { b } g _ { j } ( x ) \ d x \right) = 1 .
$$

Letting

$$
q _ { j } = \int _ { a } ^ { b } g _ { j } ( x ) \ d x ,
$$

the unit area constraint (5.43) can be writen as

$$
{ \mathbf { q } } ^ { T } { \mathbf { c } } = 1 .
$$

Averaging kernel widths can be usefully characterized in a variety of ways [126]. The most commonly used measure is the second moment of $A ( x )$ about $\hat { x }$ ：

$$
\nu = \int _ { a } ^ { b } A ( x ) ^ { 2 } ( x - { \hat { x } } ) ^ { 2 } \ d x .
$$

In terms of the coeffcients $\mathbf { c }$ ,this can be writen using (5.43) as

$$
\boldsymbol { w } = \mathbf { c } ^ { T } \mathbf { H } \mathbf { c }
$$

where

$$
H _ { j , k } = \int _ { a } ^ { b } g _ { j } ( x ) g _ { k } ( x ) ( x - \hat { x } ) ^ { 2 } ~ d x .
$$

Now, the problem of finding the optimal coefficients can be writen as

$$
\begin{array} { c } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { H } \mathbf { c } } \\ { \mathbf { c } ^ { T } \mathbf { q } = 1 , } \end{array}
$$

which can be solved using the Lagrange multiplier technique.

In practice, the data may be noisy, and the solution may thus be unstable. For mea-surements with independent errors,the standard deviation of the estimate is given by

$$
\mathrm { V a r } ( \hat { m } ) = \sum _ { j = 1 } ^ { m } c _ { j } ^ { 2 } \sigma _ { j } ^ { 2 } ,
$$

where $\sigma _ { j }$ is the standard deviation of the $j$ th observation.

The solution can be stabilized by adding a constraint on the variance to (5.49)

$$
\begin{array} { r } { \operatorname* { m i n } \mathbf { \epsilon } ^ { T } \mathbf { H } \mathbf { c } } \\ { \mathbf { q } ^ { T } \mathbf { c } = 1 } \\ { \displaystyle \sum _ { j = 1 } ^ { n } c _ { j } ^ { 2 } \sigma _ { j } ^ { 2 } \leq \delta . } \end{array}
$$

Again,this problem can be solved by the method of Lagrange multipliers.Smaller values of 8 decrease the variance of the estimate, but restrict the choice of coefficients so that the width of the averaging kernel increases. There is thus a trade-off between stability of the solution and the width of the averaging kernel.

The method of Backus and Gilbert produces a model estimate at a particular point $\hat { x }$ It is possible to use the method to compute estimates on a grid of points $x _ { 1 }$ ， $x _ { 2 }$ ，.， $x _ { n }$ However, since the averaging kernels may not be well localized around their associated grid points,and may vary and overlap in complicated ways, this is not equivalent to the simple collocation method of model representation introduced in Chapter 1. Furthermore, such an approach requires the computationally intensive solution of (5.51) for each point. For these reasons, the method does not receive wide use.

# Example 5.1

For a spherically symmetric Earth model, the mass $M _ { e }$ and moment of inertia $I _ { e }$ are determined by the radial density $\rho ( r )$ ,where

$$
M _ { e } = \int _ { 0 } ^ { R _ { e } } \left( 4 \pi r ^ { 2 } \right) \rho \left( r \right) d r
$$

and

$$
I _ { e } = \int _ { 0 } ^ { R _ { e } } { \left( { \frac { 8 } { 3 } } \pi r ^ { 4 } \right) \rho ( r ) d r } .
$$

Using $R _ { e } = 6 . 3 7 0 8 \times 1 0 ^ { 6 } \mathrm { ~ m ~ }$ as the radius of a spherical Earth, and supposing that from astronomical measurements we can infer that $M _ { e } = 5 . 9 7 3 \pm 0 . 0 0 0 5 \times 1 0 ^ { 2 4 } { \mathrm { ~ k g } }$ and $I _ { e } =$ $8 . 0 2 \pm 0 . 0 0 5 \times 1 0 ^ { 3 7 } \ \mathrm { k g \cdot m ^ { 2 } }$ ，we will estimate the density of the Earth in the lower mantle (e.g., at $r = 5 0 0 0 ~ \mathrm { k m } ,$ , and core (e.g., at $r = 1 0 0 0 \mathrm { k m } ,$ ).

Equations (5.52) and (5.53) include terms that span an enormous numerical range. Scaling so that

$$
\hat { r } = r / R _ { e } \quad \hat { \rho } = \rho / 1 0 0 0 \quad \hat { I } _ { e } = I _ { e } / 1 0 ^ { 3 7 } \quad \hat { M } _ { e } = M _ { e } / 1 0 ^ { 2 4 }
$$

gives

$$
\hat { M } _ { e } = 0 . 2 5 8 6 \intop _ { 0 } ^ { 1 } \left( 4 \pi \hat { r } ^ { 2 } \right) \hat { \rho } ( \hat { r } ) d \hat { r }
$$

and

$$
\hat { I } _ { e } = 1 . 0 4 9 2 \int _ { 0 } ^ { 1 } \left( \frac { 8 } { 3 } \pi \hat { r } ^ { 4 } \right) \hat { \rho } ( \hat { r } ) d \hat { r } .
$$

Applying (5.49) for $r = 5 0 0 0 { \mathrm { k m } }$ gives the coefficient values $\mathbf { c } ^ { T } = [ 1 . 1 8 0 9 , - 0 . 1 5 8 8 ]$ and a corresponding model density of $5 . 8 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . This is a fairly accurate estimate of density for this radius,where standard earth models estimated using seismological methods [96] infer densities of approximately $5 { \mathrm { g } } / { \mathrm { c m } } ^ { 3 }$ . The associated standard deviation (5.50) is $0 . 0 0 1 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ , so there is very litle sensitivity to data uncertainty.

At $r = 1 0 0 0 ~ \mathrm { k m }$ ，we obtain the coefficients $\mathbf { c } ^ { T } = [ 2 . 5 5 3 7 , - 1 . 0 0 4 7 ]$ ,and a corre-sponding density estimate of $7 . 2 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . This is not an accurate estimate for the density of the inner core,where standard earth models have densities of around $1 3 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . The corresponding standard deviation is just $0 . 0 0 5 \mathrm { g } / \mathrm { c m } ^ { 3 }$ , so this inaccuracy is not related to instability in the inverse problem.

Figure 5.1 shows the averaging kernels corresponding to these model element estimates,and explains both the successul mantle and failed core density estimates. In the mantle case, the averaging kernel has much of its area near the targeted radius of

$5 0 0 0 ~ \mathrm { k m }$ .In the core case, however, the averaging kernel has most of its area at much greater $r$ ,and little area near the target radius of $1 0 0 0 ~ \mathrm { k m }$ .The fundamental reason for this situation is that both the mass and moment of inertia are relatively insensitive to the density of the innermost earth.

# 5.4. EXERCISES

1. Consider the earth density estimation problem of Example 5.1. Apply the generalized inverse to estimate the density as a function of radius,using the given values of mass and moment of inertia. Obtain a density model composed of 2O spherical shells of equal thickness, and compare your results to a standard model.

2. Use the Gram matrix technique to discretize the integral equation from Example 5.1.

a. Solve the resulting linear system of equations,and plot the resulting model.

b. What was the condition number of $\Gamma ?$ What does this tell you about the accuracy of your solution?

3. Show that if the representers $g _ { i } ( t )$ are linearly independent, then the Gram matrix $\mathbf { \Gamma } ^ { \Gamma }$ is nonsingular.

4. Show that if the basis functions in (5.9) are orthonormal, then $\| m ( x ) \| _ { 2 } = \| \pmb { \beta } \| _ { 2 }$ Hint: Expand $\| m ( x ) \| _ { 2 } ^ { 2 }$ using (5.3),and then simplify using the orthogonality of the basis functions.

5.Recall the polynomial regression problem from Exercise 2.5. Instead of using the polynomials $1 , x , \ldots , x ^ { 1 9 }$ ,we will usethebasis ofLegendre polynomials,which are orthogonal on the interval $[ - 1 , 1 ]$ . These polynomials are generated by the recurrence relation

$$
p _ { n + 1 } ( x ) = \frac { ( 2 n + 1 ) x p _ { n } ( x ) - n p _ { n - 1 } ( x ) } { n + 1 } ,
$$

starting with

$$
p _ { 0 } ( x ) = 1
$$

and

$$
p _ { 1 } ( x ) = x .
$$

The next two Legendre polynomials are $p _ { 2 } ( x ) = ( 3 x ^ { 2 } - 1 ) / 2$ and $p _ { 3 } ( x ) = ( 5 x ^ { 3 } -$ $3 x ) / 2$ . This recurrence relation can be used both to compute coefficients of the Legendre polynomials and to compute values of the polynomials for particular values of $_ x$

Use the first 2O Legendre polynomials to ft a polynomial of degree 19 to the data from Exercise 2.5. Express your solution as a linear combination of the Legendre polynomials and also as a regular polynomial. How well-conditioned was this system of equations? Plot your solution and compare it with your solution to Exercise 2.5.

6. Construct specific examples of functions $m _ { 1 } ( x )$ and $m _ { 2 } ( x )$ in $L _ { 2 } ( - 1 , 1 )$ ，such that $m ( x ) = m _ { 1 } ( x ) + m _ { 2 } ( x )$ ， $m _ { 1 } ( x ) \perp m _ { 2 } ( x )$ ,but $\| m ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } \neq \| m _ { 1 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 }$

# 5.5.NOTES AND FURTHER READING

Techniques for discretizing integral equations are discussed in [45,126,166,172]. A variety of basis functions have been used to discretize integral equations including sines and cosines,spherical harmonics,B-splines,and wavelets.In selecting the basis functions,it is important to select a basis that can reasonably represent likely models. The basis functions must be linearly independent, so that a function can be written in terms of the basis functions in exactly one way, and (5.9) is thus unique. As we have seen, the use of an orthonormal basis has the further advantage that $\| { \pmb { \beta } } \| _ { 2 } = \| { \pmb { m } } ( { \boldsymbol { x } } ) \| _ { 2 }$

The selection of an appropriate basis for a particular problem is a fine art that requires detailed knowledge of the problem as well as of the behavior of the basis functions. Beware that a poorly selected basis may not adequately approximate the solution, resulting in an estimated model $m ( x )$ that is very wrong. The choice of basis can also have a very large effect on the condition number of the discretized problem, potentially making it very ill-conditioned.

An important theoretical question is whether the solutions to discretized versions of a continuous inverse problem with noise-free data will converge to a solution of the continuous inverse problem. Engl, Hanke,and Neubauer provide an explicit example showing that nonconvergence of a discretization scheme is possible [45]. They also provide conditions under which convergence is guaranteed. For Fredholm integral equa-tions of the first kind, the Gram matrix approach using representers can be shown to be convergent [45].

# Iterative Methods

# Synopsis

We present several methods for solving linear inverse problems that may be far too large for the methods previously discussed to be practical. These methods are iterative,in that a sequence of trial solutions is generated that converges to a final solution. Kacz-marz's algorithm and the related ART and SIRT methods form one class,while methods based on conjugate gradients form a second class. When the method of conjugate gradients is applied to the normal equations, the resulting conjugate gradient least squares (CGLS) method regularizes the solution to the inverse problem.Methods for estimat-ing model resolution for very large model spaces are described. Ilustrative examples involving tomography and image deblurring are given.

# 6.1.INTRODUCTION

Singular value decomposition (SVD)-based pseudoinverse and Tikhonov regularization solutions become impractical when we consider larger problems in which $\mathbf { G }$ has,for example,tens of thousands of rows and columns. Storing all of the elements in such a large $\mathbf { G }$ matrix can require a great deal of computer memory. If many of the elements in the $\mathbf { G }$ matrix are zero,as for example in ray-theory tomography, then $\mathbf { G }$ isa sparse matrix, and we can obviate this problem by storing only the nonzero elements of G and their locations. The density of G is the percentage of nonzero elements in the matrix.MATLAB can store sparse matrices and most built-in MATLAB functions operate eficiently on sparse matrices. Dense matrices contain enough nonzero elements that sparse storage schemes are not efficient.

Methods for the solution of linear systems of equations based on matrix factorizations such as the Cholesky factorization,QR factorization, or SVD do not tend to work well with sparse matrices. The problem is that the matrices that occur in the factorization of $\mathbf { G }$ are often more dense than $\mathbf { G }$ itself.In particular, the U and $\mathbf { v }$ matrices in the SVD and the $\mathbf { Q }$ matrix in the QR factorization are orthogonal matrices,which typically make these matrices dense.

The iterative methods discussed in this chapter do not require the storage of large dense matrices. Instead, they work by generating a sequence of models $\mathbf { m }$ that converge to an optimal solution. Steps in these algorithms typically involve multiplying $\mathbf { G }$ and $\mathbf { G } ^ { T }$ times vectors,which can be done without additional storage. Because iterative methods can also take advantage of the sparsity commonly found in the $\mathbf { G }$ matrix, they are often used for very large problems.

For example, consider a two-dimensional tomography problem where the model is of size 256 by 256 (65,536 model elements) and there are 100,000 ray paths.Each ray path will pass through less than $1 \%$ of the model cells, so the vast majority of the elements (e.g., more than $9 9 \%$ in $\mathbf { G }$ will be zero. If we stored $\mathbf { G }$ as a full matrix, it would require about 5O gigabytes (GB) of storage. Furthermore, if we wished to apply the SVD, the U matrix would require ${ 8 0 } \mathrm { G B }$ of storage, and the V matrix would require about 35 GB. Because of the extreme sparsity of $\mathbf { G }$ ,such a matrix can be stored in less than 1 GB using sparse storage.

At the time this book was written, computers with several gigabytes of main memory were common, while only computers classified as supercomputers would have hundreds or thousands of gigabytes of main memory. The point at which it becomes necessary to use sparse matrix storage depends on the computer that we are using. Although the memory capacity of computers has been increasing steadily for many years, it is safe to say that there will always be problems for which sparse matrix storage will be required. Furthermore, programs that use sparse matrix storage often run much faster than programs that do not take advantage of sparsity. Thus it is a good idea to consider using sparse storage even in cases where sufficient memory is available to store the full matrix.

# 6.2. ITERATIVE METHODS FOR TOMOGRAPHY PROBLEMS

We will concentrate in this section on Kaczmarz's algorithm and its ART and SIRT variants. These algorithms were originally developed for tomographic applications and are particularly effective for such problems.

Kaczmarz's algorithm is an easy-to-implement algorithm for solving a linear system of equations $\mathbf { G m } = \mathbf { d }$ . To understand the algorithm, note that each of the m equations $\mathbf { G } _ { i , \cdot } \mathbf { m } = d _ { i }$ defines an $n$ -dimensional hyperplane in $R ^ { m }$ . Kaczmarz's algorithm starts with an initial solution $\mathbf { m } ^ { ( 0 ) }$ ， and then moves to a solution $\mathbf { m } ^ { ( 1 ) }$ by projecting the initial solution onto the hyperplane defined by the first row in $\mathbf { G }$ Next $\mathbf { m } ^ { ( 1 ) }$ is similarly projected onto the hyperplane defined by the second row in $\mathbf { G }$ ，and so forth. The process is repeated until the solution has been projected onto all $m$ hyperplanes defined by the system of equations. At that point, a new cycle of projections begins. These cycles are repeated until the solution has converged sufficiently. Figure 6.1 shows an example in which Kaczmarz's algorithm is used to solve the system of equations

![](images/394c2b3299070a9e369969c3ebe77d4f56212b5450c52219416378694c3ff471.jpg)  
Figure 6.1 Kaczmarz's algorithm on a system of two equations.

$$
\begin{array} { c } { { \gamma = 1 } } \\ { { - x + \gamma = - 1 . } } \end{array}
$$

To implement the algorithm, we need a formula to compute the projection of a $i$ $\mathbf { G } _ { i + 1 , \cdot } \mathbf { m } = d _ { i + 1 }$ ${ \bf G } _ { i + 1 , } ^ { T }$ update to $\mathbf { m } ^ { ( i ) }$ from the constraint due to row $i + 1$ of $\mathbf { G }$ will be proportional to $\mathbf { G } _ { i + 1 , \cdot } ^ { T }$

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } + \beta \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

Using the fact that $\mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i + 1 ) } = d _ { i + 1 }$ to solve for $\beta$ , we obtain

$$
\begin{array} { c } { \displaystyle { \mathbf { G } _ { i + 1 , \cdot } \Big ( \mathbf { m } ^ { ( i ) } + \beta \mathbf { G } _ { i + 1 , \cdot } ^ { T } \Big ) = d _ { i + 1 } } } \\ { \displaystyle { \mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } = - \beta \mathbf { G } _ { i + 1 , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } } \\ { \displaystyle { \beta = - \frac { \mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } . } } \end{array}
$$

Thus the update formula is

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } - \frac { \mathbf { G } _ { i + 1 , } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , } \mathbf { G } _ { i + 1 , } ^ { T } } \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

It can be shown that if the system of equations $\mathbf { G m } = \mathbf { d }$ has a unique solution, then Kaczmarz's algorithm will converge to this solution. If the system of equations has many solutions, then the algorithm will converge to the solution that is closest to the point $\mathbf { m } ^ { ( 0 ) }$ . In particular, if we start with $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$ , we will obtain a minimum length solution. If there is no exact solution to the system of equations, then the algorithm will fail to converge, but will typically bounce around near an approximate solution.

A second important question is how quickly Kaczmarz's algorithm will converge to a solution. If the hyperplanes described by the system of equations are nearly orthogonal, then the algorithm will converge very quickly. However, if two or more hyperplanes are nearly parallel to each other, convergence can be extremely slow. Figure 6.2 shows a typical situation in which the algorithm zigzags back and forth without making much progress towards a solution. As the two lines become more nearly parallel, the problem becomes worse. This problem can be alleviated by picking an ordering of the equations such that adjacent equations describe hyperplanes that are nearly orthogonal to each other. In the context of tomography, this can be done by ordering the equations so that successive equations do not share common model cells.

![](images/d29f05fc218d4b3566648bd159e2fbed46bab3fe37354698091d2ebe86275797.jpg)  
Figure 6.2 Slow convergence occurs when hyperplanes are nearly parallel.

# Example 6.1

Consider a tomographic reconstruction problem with the same geometry used in Exercise 4.4,in which the slowness structure is parameterized in homogeneous blocks of size $l$ by l. The true model is shown in Figure 6.3. Synthetic data were generated, with normally distributed random noise added.The random noise had a standard deviation of 0.01. Figure 6.4 shows the TSVD solution. The two anomalies are apparent, but it is not possible to distinguish the small hole within the larger of the two.

![](images/bdfa8e508cabfe305b892d4d4d4ba45310fffcd82c752b63918350e6caf5475d.jpg)  
Figure 6.3 True model.   
Figure 6.4 Truncated SVD solution.

Figure 6.5 shows the solution obtained after 2OO iterations of Kaczmarz's algorithm. This solution is extremely similar to the TSVD solution,and both solutions are about the same distance from the true model.

The algebraic reconstruction technique (ART) is a version of Kaczmarz's algorithm that has been modified especially for the tomographic reconstruction problem. In (6.6), the updates to the solution always consist of adding a multiple of a row of $\mathbf { G }$ to the current solution. The numerator in the fraction is the difference between the right-hand side of equation $i + 1$ and the value of the $i + 1$ component of $\mathbf { G m }$ .The denominator in (6.6) is simply the square of the norm of $\mathbf { G } _ { i + 1 , \cdot }$ . Effectively, Kaczmarz's algorithm is determining the error in equation $i + 1$ , and then adjusting the solution by spreading the required correction over the elements of $\mathbf { m }$ that appear in equation $i + 1$

# Algorithm 6.1Kaczmarz's Algorithm

Given a system of equations $\mathbf { G m } = \mathbf { d }$

1. Let $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$   
2.For $i = 0$ ,1,..., $m - 1$ ,let

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } - \frac { \mathbf { G } _ { i + 1 , } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , } \mathbf { G } _ { i + 1 , } ^ { T } } \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

3. If the solution has not yet converged, return to step 2.

A crude approximation to the Kaczmarz update, used in ART, is to replace all of the nonzero elements in row $i + 1$ of $\mathbf { G }$ with ones. We define

$$
q _ { i + 1 } = \sum _ { \mathrm { \scriptsize ~ c e l l } ~ j ~ \mathrm { i n ~ r a y ~ p a t h } ~ i + 1 } \mathbf { m } _ { j } l
$$

as an approximation to the travel time along ray path $i + 1$ ,where $l$ is the cell dimension. The difference between $q _ { i + 1 }$ and $d _ { i + 1 }$ is roughly the residual for the predicted travel time of ray $i + 1$

Examining (6.6) for the ART-modified $\mathbf { G }$ ，we see that ART simply takes the total travel time misfit for ray $i + 1$ and divides it by $l$ times the number of cells in the ray path, $N _ { i + 1 }$ . This correction factor is then multiplied by a vector that has ones in cells along ray path $i + 1$ . This procedure has the effect of smearing the needed correction in travel time equally over all of the cels in the ray path.

The ART approximate update formula can thus be written as

$$
\begin{array} { r } { m _ { j } ^ { ( i + 1 ) } = \left\{ { \begin{array} { l l } { m _ { j } ^ { ( i ) } - \frac { q _ { i + 1 } - d _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n } \mathrm { r a y p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n r a y p a t h } i + 1 . } \end{array} } \right. } \end{array}
$$

The approximation can be improved by taking into account that the ray path lengths actually will vary from cell to cell. If $L _ { i + 1 }$ is the length of ray path $i + 1$ ，the corresponding improved update formula from (6.6) for the tomography problem is

$$
m _ { j } ^ { ( i + 1 ) } = \left\{ \begin{array} { l l } { m _ { j } ^ { ( i ) } + \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n \ r a y \ p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n \ r a y \ p a t h } i + 1 . } \end{array} \right.
$$

The main advantage of ART is that it saves storage. We need only store information about which rays pass through which cells,and we do not need to record the length of each ray in each cell. A second advantage of the method is that it reduces the number of floating-point multiplications compared to that required by Kaczmarz's algorithm. Although in current computers floating-point multiplications and additions require roughly the same amount of time,during the 197Os,when ART was first developed, multiplication was slower than addition.

# Algorithm 6.2 ART

Given a system of equations $\mathbf { G m } = \mathbf { d }$ arising from a tomography problem:

1.Let ${ \pmb m } ^ { ( 0 ) } = { \bf 0 }$   
2.For $i = 0$ ,1，...， $m$ ,let $N _ { i }$ be the number of cells traversed by ray path i.   
3.For $i = 0$ ,1，..., $m$ ,let $L _ { i }$ be the length of ray path i.

# Algorithm 6.2 (Continued)

4. For i=0,1,...,m-1,j=1,2,...,n,let

$$
\begin{array} { r } { m _ { j } ^ { ( i + 1 ) } = \left\{ \begin{array} { l l } { m _ { j } ^ { ( i ) } + \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n \ r a y \ p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n \ r a y \ p a t h } i + 1 . } \end{array} \right. } \end{array}
$$

5. If the solution has not yet converged,let ${ \pmb m } ^ { ( 0 ) } = { \pmb m } ^ { ( m ) }$ and return to step 4. Otherwise, return the solution $\pmb { m } = \pmb { m } ^ { ( m ) }$

One problem with ART is that the resulting tomographic images tend to be noisier than images produced by Kaczmarz's algorithm (6.7). The simultaneous iterative recon-struction technique (SIRT) is a variation on ART that gives slightly better images in practice,at the expense of a slightly slower algorithm. In the SIRT algorithm, all(up to m nonzero) updates using (6.1O) are computed for each cell $j$ of the model, for each ray that passes through cell $j$ . The set of updates for cell $j$ are then averaged before updating the coresponding model element $m _ { j }$

# Algorithm 6.3 SIRT

Given a system of equations $\mathbf { G m } = \mathbf { d }$ arising from a tomography problem:

1. Let $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$

2.For $j = 0$ ,1,..., $n$ let $K _ { j }$ be the number of ray paths that passthrough cell $j$

3. For $i = 0$ ,1,..., $m$ let $L _ { i }$ be the length of ray path i.

4.For $i = 0$ ,1,..., $m$ ,let $N _ { i }$ be the number of cells traversed by ray path i.

5.Let $\Delta { \pmb m } ^ { ( i + 1 ) } = { \pmb 0 }$

6.For $i = 0$ ,1,..., $m - 1 , j = 1$ ,2，...,n,let

$$
\begin{array} { r } { \Delta m _ { j } ^ { ( i + 1 ) } = \Delta m _ { j } ^ { ( i + 1 ) } + \left\{ \begin{array} { l l } { \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l ~ } j \mathrm { ~ i n ~ r a y ~ p a t h ~ } i + 1 } \\ { 0 } & { \mathrm { c e l l ~ } j \mathrm { ~ n o t ~ i n ~ r a y ~ p a t h ~ } i + 1 . } \end{array} \right. } \end{array}
$$

7. For $j = 1 , 2 , \dots , n ,$ let

$$
m _ { j } ^ { ( i + 1 ) } = m _ { j } ^ { ( i + 1 ) } + \frac { \Delta m _ { j } ^ { ( i + 1 ) } } { K _ { j } } .
$$

8. Ifthe solution has not yet converged,return to step 5. Otherwise, return the current solution.

# Example 6.2

Returning to our earlier tomography example, Figure 6.6 shows the ART solution obtained after 2OO iterations. Again, the solution is very similar to the TSVD solution.

![](images/b204a190823df5cf77077efc9485c9ddc3f0665a71d1a22b0f91cfbaf3e69b0e.jpg)  
Figure 6.6 ART solution.

![](images/5ffa21a61400d498b01bc17d579d811e1dd5a4d6bb93fbe2ac7d69b964352d26.jpg)  
Figure 6.7 shows the SIRT solution for our example tomography problem after 200 iterations. This solution is similar to the TSVD,Kaczmarz's,and ART solutions.   
Figure 6.7 SIRT solution.

# 6.3.THE CONJUGATE GRADIENT METHOD

We next consider the conjugate gradient (CG) method for solving a symmetric and positive definite system of equations $\mathbf { A x } = \mathbf { b }$ . We will later apply the CG method to solving the normal equations for $\mathbf { G m } = \mathbf { d }$ .Consider the quadratic optimization problem,

$$
\operatorname* { m i n } \ { \phi } ( { \mathbf { x } } ) = \frac { 1 } { 2 } { \mathbf { x } } ^ { T } { \mathbf { A } } { \mathbf { x } } - { \mathbf { b } } ^ { T } { \mathbf { x } } ,
$$

where $\mathbf { A }$ is an $n \times n$ symmetric and positive definite matrix. We require A be positive definite so that the function $\phi ( \mathbf { x } )$ will be convex and have a unique minimum. We can calculate $\nabla \phi ( \mathbf { x } ) = \mathbf { A } \mathbf { x } - \mathbf { b }$ and set it equal to zero to find the minimum. The minimum occurs at a point $\mathbf { x }$ that satisfies the equation

$$
\mathbf { A x } - \mathbf { b } = \mathbf { 0 }
$$

or

$$
\mathbf { A x } = \mathbf { b } .
$$

Thus solving the system of equations $\mathbf { A x } = \mathbf { b }$ is equivalent to minimizing $\phi ( \mathbf { x } )$

The conjugate gradient method approaches the problem of minimizing $\phi ( \mathbf { x } )$ by constructing a basis for $R ^ { n }$ in which the minimization problem is extremely simple. The basis vectors $\mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \dots . . . , \mathbf { p } _ { n - 1 }$ are selected so that

$$
\mathbf { p } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { j } = 0 \quad \mathrm { w h e n } i \neq j .
$$

A collection of vectors with this property is said to be mutually conjugate with respect to A. We express $\mathbf { x }$ in terms of these basis vectors as

$$
\mathbf { x } = \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i }
$$

so that

$$
\phi \left( \alpha \right) = \frac { 1 } { 2 } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i } \right) ^ { T } \mathbf { A } \left( \sum _ { j = 0 } ^ { n - 1 } \alpha _ { j } \mathbf { p } _ { j } \right) - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i } \right) .
$$

The product $\mathbf { x } ^ { T } \mathbf { A x }$ can be written as a double sum, so the equation becomes

$$
\phi ( \pmb { \alpha } ) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \sum _ { j = 0 } ^ { n - 1 } \alpha _ { i } \alpha _ { j } \pmb { \mathrm { p } } _ { i } ^ { T } \pmb { \mathrm { A } } \pmb { \mathrm { p } } _ { j } - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \pmb { \mathrm { p } } _ { i } \right) .
$$

Since the vectors are mutually conjugate with respect to A, this simplifies to

$$
\phi \left( \pmb { \alpha } \right) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } ^ { 2 } \pmb { \mathrm { p } } _ { i } ^ { T } \pmb { \mathrm { A } } \pmb { \mathrm { p } } _ { i } - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \pmb { \mathrm { p } } _ { i } \right)
$$

or

$$
\phi \left( { \pmb { \alpha } } \right) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \bigl ( \alpha _ { i } ^ { 2 } { \pmb { \mathrm { p } } } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { i } - 2 \alpha _ { i } \mathbf { b } ^ { T } \mathbf { p } _ { i } \bigr ) .
$$

Equation (6.22) shows that $\phi ( { \pmb { \alpha } } )$ consists of $n$ terms,each of which is independent of the other terms. Thus we can minimize $\phi ( { \pmb \alpha } )$ by selecting each $\alpha _ { i }$ to minimize the ith term,

$$
\alpha _ { i } ^ { 2 } \mathbf { p } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { i } - 2 \alpha _ { i } \mathbf { b } ^ { T } \mathbf { p } _ { i } .
$$

Differentiating with respect to $\alpha _ { i }$ and setting the derivative equal to zero, we find that the optimal value for $\alpha _ { i }$ is

$$
\alpha _ { i } = { \frac { \mathbf { b } ^ { T } \mathbf { p } _ { i } } { \mathbf { p } _ { i } ^ { T } \mathbf { A p } _ { i } } } .
$$

This shows that if we have a basis of vectors that are mutually conjugate with respect to A, then minimizing $\phi ( \mathbf { x } )$ is very easy. We have not yet shown how to construct the mutually conjugate basis vectors.

Our algorithm will actually construct a sequence of solution vectors $\mathbf { x } _ { i }$ ，residual vectors $\mathbf { r } _ { i } = \mathbf { b } - \mathbf { A x } _ { i }$ ，and basis vectors $\mathbf { p } _ { i }$ .The algorithm begins with $\mathbf { x } _ { \mathrm { 0 } } = \mathbf { 0 }$ ， $\mathbf { r } _ { 0 } = \mathbf { b }$ ， $\mathbf { p } _ { 0 } = \mathbf { r } _ { 0 }$ ,and $\alpha _ { 0 } = ( { \bf r } _ { 0 } ^ { T } { \bf r } _ { 0 } ) / ( { \bf p } _ { 0 } ^ { T } { \bf A } { \bf p } _ { 0 } )$

Suppose that at the start of iteration $k$ of the algorithm, we have constructed $\mathbf { x } _ { \mathrm { 0 } }$ ， $\mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { k } , \mathbf { r } _ { 0 } , \mathbf { r } _ { 1 } , \ldots , \mathbf { r } _ { k } , \mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \ldots , \mathbf { p } _ { k }$ and $\alpha _ { 0 } , \alpha _ { 1 } , \ldots , \alpha _ { k }$ ，We assume that the first $k + 1$ basis vectors $\mathbf { p } _ { i }$ are mutually conjugate with respect to $\mathbf { A }$ ,the first $k + 1$ residual vectors $\mathbf { r } _ { i }$ are mutually orthogonal, and that $\mathbf { r } _ { i } ^ { T } \mathbf { p } _ { j } = 0$ when $i \neq j$

We let

$$
\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k } .
$$

This effectively adds one more term of (6.18) into the solution. Next, we let

$$
\mathbf { r } _ { k + 1 } = \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } .
$$

This correctly updates the residual, because

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } = \mathbf { b } - \mathbf { A x } _ { k + 1 } } \\ & { \qquad = \mathbf { b } - \mathbf { A } \big ( \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k } \big ) } \\ & { \qquad = ( \mathbf { b } - \mathbf { A x } _ { k } ) - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } . } \end{array}
$$

We let

$$
\beta _ { k + 1 } = { \frac { \| \mathbf { r } _ { k + 1 } \| _ { 2 } ^ { 2 } } { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } } = { \frac { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } } { \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } } }
$$

and

$$
\mathbf { p } _ { k + 1 } = \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \mathbf { p } _ { k } .
$$

In the following calculations,it will be useful to know that $\mathbf { b } ^ { T } \mathbf { p } _ { k } = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k }$ . This is shown by

$$
\begin{array} { r l } & { \mathbf { b } ^ { T } \mathbf { p } _ { k } = ( \mathbf { r } _ { k } + \mathbf { A x } _ { k } ) ^ { T } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k } + \mathbf { x } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k } + \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { x } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } ( \mathbf { r } _ { k } + \beta _ { k } \mathbf { p } _ { k - 1 } ) + \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { x } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \beta _ { k } \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k - 1 } + \mathbf { p } _ { k } ^ { T } \mathbf { A } \big ( \alpha _ { 0 } \mathbf { p } _ { 0 } + \cdot \cdot \cdot + \alpha _ { k - 1 } \mathbf { p } _ { k - 1 } \big ) } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + 0 + 0 } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } . } \end{array}
$$

We will now show that $\mathbf { r } _ { k + 1 }$ is orthogonal to $\mathbf { r } _ { i }$ for $i \leq k$ For every $i < k$ ，

$$
\begin{array} { r } { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } ) ^ { T } \mathbf { r } _ { i } } \\ { = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { i } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { i } } \\ { = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { i } - \alpha _ { k } \mathbf { r } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { k } . } \end{array}
$$

Since $\mathbf { r } _ { k }$ is orthogonal to all of the earlier $\mathbf { r } _ { i }$ vectors,

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { k } .
$$

Also, since $\mathbf { p } _ { i } = \mathbf { r } _ { i } + \beta _ { i } \mathbf { p } _ { i - 1 }$

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 - \alpha _ { k } \big ( \mathbf { p } _ { i } - \beta _ { i } \mathbf { p } _ { i - 1 } \big ) ^ { T } \mathbf { A } \mathbf { p } _ { k } .
$$

Both $\mathbf { p } _ { i }$ and $\mathbf { p } _ { i - 1 }$ are conjugate with $\mathbf { p } _ { k }$ . Thus

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 .
$$

We also have o show that $\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k } = 0$

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k } = ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } ) ^ { T } \mathbf { r } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } ( \mathbf { p } _ { k } - \beta _ { k } \mathbf { p } _ { k - 1 } ) } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } ( \mathbf { p } _ { k } - \beta _ { k } \mathbf { p } _ { k - 1 } ) ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } + \alpha _ { k } \beta _ { k } \mathbf { p } _ { k - 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \alpha _ { k } \beta _ { k } 0 } \\ & { \quad \quad \quad = 0 . } \end{array}
$$

Next, we will show that $\mathbf { r } _ { k + 1 }$ is orthogonal to $\mathbf { p } _ { i }$ for $i \leq k$

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i } = \mathbf { r } _ { k + 1 } ^ { T } \big ( \mathbf { r } _ { i } + \beta _ { i } \mathbf { p } _ { i - 1 } \big ) } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } + \beta _ { i } \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = 0 + \beta _ { i } \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = \beta _ { i } \big ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } \big ) ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = \beta _ { i } ( \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { i - 1 } - \alpha _ { k } \mathbf { p } _ { i - 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } ) } \\ & { \qquad = \beta _ { i } ( 0 - 0 ) = 0 . } \end{array}
$$

Finally, we need to show that $\mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } = 0$ for $i \leq k$ For $i < k$ ，

$$
\begin{array} { r l } & { \mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } = ( \mathbf { r } _ { k + 1 } + \boldsymbol { \beta } _ { k + 1 } \mathbf { p } _ { k } ) ^ { T } \mathbf { A } \mathbf { p } _ { i } } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } + \boldsymbol { \beta } _ { k + 1 } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { i } } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } + 0 } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \left( \frac { 1 } { \alpha _ { i } } ( \mathbf { r } _ { i } - \mathbf { r } _ { i + 1 } ) \right) } \\ & { \qquad = \cfrac { 1 } { \alpha _ { i } } \left( \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i + 1 } \right) } \\ & { \qquad = 0 . } \end{array}
$$

For $i = k$

$$
\begin{array} { r l } & { \mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } = \left( \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \mathbf { p } _ { k } \right) ^ { T } \Bigg ( \frac { 1 } { \alpha _ { k } } ( \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ) \Bigg ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \Big ( \beta _ { k + 1 } \big ( \mathbf { r } _ { k } + \beta _ { k } \mathbf { p } _ { k - 1 } \big ) ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \Big ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \big ( \beta _ { k + 1 } \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \beta _ { k + 1 } \beta _ { k } \mathbf { p } _ { k - 1 } ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \big ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \big ( \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \beta _ { k } 0 - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \big ) } \\ & { \qquad = 0 . } \end{array}
$$

We have now shown that the algorithm generates a sequence of mutually conju-gate basis vectors. In theory, the algorithm will find an exact solution to the system of equations in $n$ iterations.In practice,due to round-off errors in the computation, the exact solution may not be obtained in $n$ iterations.In practical implementations of the algorithm, we iterate until the residual is smaler than some tolerance that we specify. The algorithm can be summarized as follows.

# Algorithm 6.4 Conjugate Gradient Method

Given a positive definite and symmetric system of equations $\mathbf { A x } = \mathbf { b }$ ，and an initial solution $\mathbf { x } _ { \mathrm { 0 } }$ ,let $\beta _ { - 1 } = 0$ ， $\mathbf { p } _ { - 1 } = \mathbf { 0 }$ ， $\mathbf { r } _ { 0 } = \mathbf { b } - \mathbf { A x } _ { 0 }$ ,and $k = 0$

1. Let $\mathbf { p } _ { k } = - \mathbf { r } _ { k } + \beta _ { k - 1 } \mathbf { p } _ { k - 1 }$   
2. Let $\begin{array} { r } { \alpha _ { k } = \frac { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } { \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } } } \end{array}$   
3. Let Xk+1 = Xk +αkPk.   
4. Let $\mathbf { r } _ { k + 1 } = \mathbf { r } _ { k } + \alpha _ { k } \mathbf { A } \mathbf { p } _ { k }$   
5.Let βk=1   
6.Let $k = k + 1$   
7. Repeat the previous steps until convergence.

A major advantage of the CG method is that it requires storage only for the vectors $\mathbf { x } _ { k }$ ， $\mathbf { p } _ { k }$ ， $\mathbf { r } _ { k }$ ， and the symmetric matrix A. If A is large and sparse, then sparse matrix techniques can be used to store A more efficiently. Unlike factorization methods such as QR, SVD, or Cholesky factorization, there will be no fill-in of the zero elements in A at any stage in the solution process. Thus it is possible to solve extremely large systems using CG in cases where direct factorization would require far too much storage. In fact, the only way in which the algorithm uses A is in one multiplication of $\mathbf { A } \mathbf { p } _ { k }$ for each iteration. In some applications of the CG method, it is possible to perform these matrix vector multiplications without explicitly constructing A.

# 6.4.THE CGLS METHOD

The CG method by itself can only be applied to positive definite systems of equations, and is thus not directly applicable to general least squares problems. In the conjugate gradient least squares (CGLS) method, we solve a least squares problem,

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ,
$$

by applying CG to the normal equations,

$$
\mathbf { G } ^ { T } \mathbf { G } \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } .
$$

In implementing this algorithm it is important to avoid round-off errors. One important source of error is the evaluation of the residual, $\mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - \mathbf { G } ^ { T } \mathbf { d } .$ It turns out that this calculation is more accurate when we factor out $\mathbf { G } ^ { T }$ and compute $\mathbf { G } ^ { T } ( \mathbf { G m - d } )$ We will use the notation $\mathbf { s } _ { k } = \mathbf { G } \mathbf { m } _ { k } - \mathbf { d }$ and $\mathbf { r } _ { k } = \mathbf { G } ^ { T } \mathbf { s } _ { k }$ . Note that we can compute $\mathbf { s } _ { k + 1 }$ recursively from $\mathbf { s } _ { k }$ as follows

$$
{ \begin{array} { r l } & { \mathbf { s } _ { k + 1 } = \mathbf { G m } _ { k + 1 } - \mathbf { d } } \\ & { \qquad = \mathbf { G } ( \mathbf { m } _ { k } + \alpha _ { k } \mathbf { p } _ { k } ) - \mathbf { d } } \\ & { \qquad = ( \mathbf { G m } _ { k } - \mathbf { d } ) + \alpha _ { k } \mathbf { G p } _ { k } } \\ & { \qquad = \mathbf { s } _ { k } + \alpha _ { k } \mathbf { G } \mathbf { p } _ { k } . } \end{array} }
$$

With this trick, we can now state the CGLS algorithm.

# Algorithm 6.5 CGLS

Given a least squares problem min $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ ,let $k = 0$ ， $\mathbf { m } _ { 0 } = \mathbf { 0 }$ ， $\mathbf { p } _ { - 1 } = \mathbf { 0 }$ ， $\beta _ { - 1 } = 0$ ， $\mathbf { s } _ { 0 } = - \mathbf { d } .$ and $\mathbf { r } _ { 0 } = \mathbf { G } ^ { T } \mathbf { s } _ { 0 }$

1. Let $\mathbf { p } _ { k } = - \mathbf { r } _ { k } + \beta _ { k - 1 } \mathbf { p } _ { k - 1 }$

3. Let $\mathbf { m } _ { k + 1 } = \mathbf { m } _ { k } + \alpha _ { k } \mathbf { p } _ { k }$

4. Let $\mathbf { s } _ { k + 1 } = \mathbf { s } _ { k } + \alpha _ { k } \mathbf { G } \mathbf { p } _ { k }$

5.Let $\mathbf { r } _ { k + 1 } = \mathbf { G } ^ { T } \mathbf { s } _ { k + 1 }$

6. Let $\beta _ { k } = { \frac { \| \mathbf { r } _ { k + 1 } \| _ { 2 } ^ { 2 } } { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } }$

7. Let $k = k + 1$

8. Repeat the previous steps until convergence.

Note that this algorithm only requires one multiplication of $\mathbf { G } \mathbf { p } _ { k }$ and one multiplication of $\mathbf { G } ^ { T } \mathbf { s } _ { k + 1 }$ per iteration. We never explicitly compute $\mathbf { G } ^ { T } \mathbf { G }$ ，which might require considerable time,and which might have far more nonzero elements than $\mathbf { G }$ itself.

The CGLS algorithm has an important property that makes it particularly useful for ill-posed problems. It can be shown that, for exact arithmetic, $\| \mathbf { m } _ { k } \| _ { 2 }$ increases monotonically and $\| \mathbf { G m } _ { k } - \mathbf { d } \| _ { 2 }$ decreases monotonically with increasing iterations [61, 65]. We can use the discrepancy principle together with this property to obtain a regularized solution. Simply stop the CGLS algorithm as soon as $\| \mathbf { G m } _ { k } - \mathbf { d } \| _ { 2 } < \delta$ . In practice, this algorithm typically gives good solutions after a very small number of iterations.

An alternative way to use CGLS is to solve the Tikhonov regularization problem (4.4) by applying CGLS to

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

For nonzero values of the regularization parameter $\alpha$ ,this least squares problem should be reasonably well-conditioned. By solving this problem for several values of $\alpha$ ,we can compute an L-curve. The disadvantage of this approach is that the number of CGLS iterations for each value of $\alpha$ may be large,and we need to solve the problem for several values of $\alpha$ . Thus the computational effort is far greater.

# Example 6.3

A commonly used mathematical model of image blurring involves the two-dimensional convolution of the true image $I _ { \mathrm { t r u e } } ( x , \gamma )$ with a point spread function, $\Psi ( u , \nu )$ [14]:

$$
I _ { \mathrm { b l u r r e d } } ( x , \gamma ) = \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } I _ { \mathrm { t r u e } } ( x - u , \gamma - \nu ) \Psi ( u , \nu ) \ d u \ d \nu .
$$

Here the point spread function shows how a point in the true image is altered in the blurred image. A point spread function that is commonly used to represent the blurring that occurs because an image is out of focus is the Gaussian point spread function

$$
\Psi ( u , \nu ) = e ^ { \frac { u ^ { 2 } + \nu ^ { 2 } } { 2 \sigma ^ { 2 } } } .
$$

Here the parameter $\sigma$ controls the relative width of the point spread function. In prac-tice, the blurred image and point spread function are discretized into pixels. In theory, $\Psi$ is nonzero for all values of $u$ and $\nu$ ，However, it becomes small quickly as $u$ and $\nu$ increase. If we set small values of $\Psi$ to O, then the $\mathbf { G }$ matrix in the discretized problem will be sparse.

![](images/b4153518e6eb49c6578a6bdfd9df42ff97bdb00e2e58e2a5ce2f9bd32d2fa8a9.jpg)  
Figure 6.8 Blurred image.

Figure 6.8 shows an image that has been blurred and also has a small amount of added noise. This image is of size 2OO pixels by 20O pixels,so the $\mathbf { G }$ matrix for the blurring operator is of size 4O,OOO by 40,OOO. Fortunately, the blurring matrix $\mathbf { G }$ is quite sparse, with less than $0 . 1 \%$ nonzero elements. The sparse matrix requires about $1 2 ~ \mathrm { M B }$ of storage. A dense matrix of this size would require about $1 3 \ \mathrm { G B }$ of storage. Using the SVD approach to Tikhonov regularization would require far more storage than many current computers have. However, CGLS works quite well on this problem.

Figure 6.9 shows the L-curve for the solution of this problem by CGLS without explicit regularization and by CGLS with explicit regularization. The line with circles shows the solutions obtained by CGLS without explicit regularization. For the first 30 or so iterations of CGLS without explicit regularization, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ decreases quickly. After that point, the improvement in misfit slows down, while $\| \mathbf { m } \| _ { 2 }$ increases rapidly.

Figure 6.1O shows the CGLS solution without explicit regularization after 3O iterations.The blurring has been greatly improved. Note that 3O iterations is far less than the size of the matrix $( n = 4 0 , 0 0 0 )$ . Unfortunately, further CGLS iterations do not significantly improve the image. In fact, noise builds up rapidly, both because of the accumulation of round-off errors and because the algorithm is converging slowly towards an unregularized least squares solution. Figure 6.11 shows the CGLS solution after 1OO iterations.In this image the noise has been greatly amplified, with little or no improvement in the clarity of the image.

We also computed CGLS solutions with explicit Tikhonov regularization for 22 values of $\alpha$ . For each value of $\alpha$ , 200 iterations of CGLS were performed. The resulting

![](images/48c406a95a64f6887326ec63e012ac1e3032e1d9791f9105616c6f2c0f38c97a.jpg)  
Figure 6.9 L-curves for CGLS deblurring.

![](images/4f4dfd492b3ff51d3f878bd9f2b11e6ece485db56ecbcce0a0755025446154c5.jpg)  
Figure 6.10 CGLS solution after 30iterations, no explicit regularization.

L-curve is shown in Figure 6.9 with “x”markers for each regularized solution that was obtained. This L-curve is slightly better than the L-curve from the CGLS solution without explicit regularization in that the values of $\| \mathbf { m } \| _ { 2 }$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ are smaller. However, it required 4O times as much computational effort. The corner solution for $\alpha = 7 . 0 \times 1 0 ^ { - 4 }$ is shown in Figure 6.12. This solution is similar to the one shown in Figure 6.10.

![](images/8334639ea5214e08d8e5d89d1d2cd90be6ffe5121d615fc5b6f8925ca4f622ed.jpg)  
Figure 6.11 CGLS solution after 100 iterations, no explicit regularization.

![](images/bd8bf87e8444b27a813f9e0e157e4a384b1e7097eb54836807232113cfbfa3b8.jpg)  
Figure 6.12 CGLS solution,explicit regularization, $\alpha = 7 . 0 \times 1 0 ^ { - 4 }$

We have focused on the CGLS method in this section because it is particularly easy to derive and because of the implicit regularization effect of the CGLS method. However, many other iterative methods have been developed for large-scale least squares problems [5,135]. An analysis of the implicit regularizing effects of these methods can be found in Hanke [61]. The LSQR method of Paige and Saunders has been very widely used in many geophysical applications [123,124]. MATLAB has an efcient and robust implementation of LSQR in its lsqr routine.

# 6.5.RESOLUTION ANALYSIS FOR ITERATIVE METHODS

Analyzing the resolution of a regularized solution computed by the iterative methods described in this chapter is a challenging problem. The formulas developed in Chapter 4 for the model resolution matrix under zeroth-order Tikhonov regularization were based on the SVD of the $\mathbf { G }$ matrix, but as we have seen it is often unfeasible to compute the SVD of a large matrix,and even when it is extremely sparse, the SVD is typically dense. For higher-order regularization,we have formulas for the resolution matrix based on the GSVD of the $\mathbf { G }$ matrix, such as (4.2O),but it is also impractical to compute the GSVD of very large matrices.

A brute force approach that offers some advantages over the computation of the SVD or GSVD is to use (4.52) with Cholesky factorization of $( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } )$ [19]. Cholesky factorization is considerably faster in practice than computing the SVD. However, since the Cholesky factor of this matrix is typically dense,this is still a very large-scale computation that would generally need to be performed in parallel on a computer with suficient memory to store a dense $n$ by $n$ matrix.

If we want to compute an individual column of the model resolution matrix, this can be accomplished by solving an additional least squares problem. Applying the expression for the least squares Tikhonov inverse operator $\mathbf { G } ^ { \sharp }$ (4.52), the ith column of $\mathbf { R } _ { m }$ can be expressed as

$$
\begin{array} { r l } & { \mathbf { R } _ { , i } = \mathbf { R } _ { m } \mathbf { e } _ { i } } \\ & { \quad \quad = \mathbf { G } ^ { \sharp } \mathbf { G } \mathbf { e } _ { i } } \\ & { \quad \quad = \mathbf { G } ^ { \sharp } \mathbf { G } _ { . , i } } \\ & { \quad \quad = \left( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { G } _ { . , i } . } \end{array}
$$

This is (4.26), a regularized least squares problem

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { R } _ { . , i } - \left[ \mathbf { \bar { G } } _ { . , i } \right] \right\| _ { 2 } ^ { 2 } }
$$

that can be solved for $\mathbf { R } _ { . , i }$ using CGLS, LSQR,or some other iterative method. We could conceivably solve (6.8O) to retrieve every column of the model resolution matrix in this manner, but this would require the solution of $n$ least squares problems.

A number of authors have considered iterative techniques for computing low-rank approximations to the resolution matrix in combination with iterative least squares solu-tion methods [12,13,174]. In such approaches, iterative methods are applied to compute the largest $k$ singular values of a matrix and the associated singular vectors. For a sparse matrix,these methods are vastly more effcient than standard algorithms for computing the SVD.

Suppose that we obtain a low-rank ( $k$ singular values and vectors) approximation to the SVD

$$
\mathbf { G } \approx \mathbf { U } _ { k } \mathbf { L } _ { k } \mathbf { V } _ { k } ^ { T }
$$

where $\mathbf { L } _ { k }$ is a $k$ by $k$ nonsingular matrix, and $\mathbf { U } _ { k }$ and $\mathbf { V } _ { k }$ are matrices with $k$ orthogonal columns. The pseudoinverse of $\mathbf { G }$ is then approximately

$$
\mathbf G ^ { \dagger } \approx \mathbf V _ { k } \mathbf L _ { k } ^ { - 1 } \mathbf U _ { k } ^ { T } .
$$

Combining these approximations,we have

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Note that we would not want to explicitly multiply out $\mathbf { V } _ { k } \mathbf { V } _ { k } ^ { T }$ ， creating a huge and dense $n$ by $n$ resolution matrix. Rather, we could store the relatively smal vector $\mathbf { V } _ { k }$ and use it to compute desired entries of the $\mathbf { R } _ { m }$ matrix as needed.

A more sophisticated version of this approach is to compute a low-rank approximation to the singular value decomposition of the augmented $\mathbf { G }$ matrix [173]. Consider an augmented system of equations

$$
\mathbf { A } = { \left[ \begin{array} { l } { \mathbf { G } } \\ { \alpha \mathbf { L } } \end{array} \right] }
$$

using truncated SVD approximations for $\mathbf { A }$ and its pseudoinverse, $\mathbf { A } ^ { \dagger }$ ，

$$
\mathbf { A } \approx \mathbf { U } _ { k } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T }
$$

and

$$
\mathbf { A } ^ { \dagger } \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { k } ^ { T } ,
$$

where $\mathbf { U } _ { k }$ and $\mathbf { V } _ { k }$ are composed of the frst $k$ columns of $\mathbf { U }$ and $\mathbf { v }$ ,and $\mathbf { S } _ { k }$ is a square $k$ by $k$ matrix diagonal matrix of the largest $k$ singular values.

It is convenient to write $\mathbf { U } _ { k }$ as

$$
\mathbf { U } _ { k } = \left[ \mathbf { U } _ { G } \right] ,
$$

where $\mathbf { U } _ { G }$ and $\mathbf { U } _ { L }$ contain the rows of $\mathbf { U } _ { k }$ corresponding to those of $\mathbf { G }$ and $\alpha \mathbf { L }$ ， respectively, in A. We can thus partition (.85)using

$$
\mathbf { G } \approx \mathbf { U } _ { G } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Given (6.88) and (6.86),we can calculate an approximation of the model resolution matrix

$$
\mathbf { R } _ { m } = \mathbf { A } ^ { \dagger } \begin{array} { c } { \left[ \mathbf { G } \right] } \\ { \mathbf { 0 } } \end{array} \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \begin{array} { c } { \left[ \mathbf { U } _ { G } ^ { T } \mathbf { U } _ { L } ^ { T } \right] } \\ { \mathbf { 0 } } \end{array} \left[ \begin{array} { c } { \mathbf { U } _ { G } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } } \\ { \mathbf { 0 } } \end{array} \right] ,
$$

which simplifies to

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { \mathrm { G } } ^ { T } \mathbf { U } _ { \mathrm { G } } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Using the identity

$$
\mathbf { U } _ { G } ^ { T } \mathbf { U } _ { G } = \mathbf { I } - \mathbf { U } _ { L } ^ { T } \mathbf { U } _ { L }
$$

we can alternatively write (6.90) as

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \Big ( \mathbf { I } - \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { L } ^ { T } \mathbf { U } _ { L } \mathbf { S } _ { k } \Big ) \mathbf { V } _ { k } ^ { T } .
$$

Depending on the relative sizes of $\mathbf { U } _ { G }$ and $\mathbf { U } _ { L }$ ,one or the other of (6.90) or (6.92) might be more easily evaluated. Again, we would probably not want to, or be able to, explicitly multiply out the matrices to obtain the entire dense $n$ by $n$ model resolution matrix for a large problem, but could instead use (6.9O) or (6.92) to compute specific desired elements of the resolution matrix.

In practice, it may not be feasible for very large problems to compute, or even store, a sufficient number of singular values and vectors to adequately approximate the model resolution matrix using low-rank, SVD-based approximations [37]. We will thus consider an alternative stochastic approach based on [9] that estimates solely the resolution matrix diagonal, but which is not limited by low-rank matrix approximations.

Consider a sequence of $s$ random vectors from $\mathbf { R } ^ { n }$ ， $\mathbf { v } _ { 1 }$ ，..， ${ \bf v } _ { s }$ ，with independent elements drawn from a standard normal distribution. The sth corresponding estimate for the diagonal of an $n$ by $n$ square matrix $\mathbf { A }$ is given by

$$
\mathbf { q } _ { s } = \left[ \sum _ { k = 1 } ^ { s } \mathbf { v } _ { k } \odot \mathbf { A } \mathbf { v } _ { k } \right] { \boldsymbol { \oslash } } \left[ \sum _ { k = 1 } ^ { s } \mathbf { v } _ { k } \odot \mathbf { v } _ { k } \right]
$$

where $\odot$ denotes element-wise multiplication and $\oslash$ denotes element-wise division of vectors. Note that the only way in which $\mathbf { A }$ is used within this algorithm is in matrix-vector multiplications, so as long as we have a function that can implement the matrix vector multiplication, then we can implement the algorithm. As we have already seen, the multiplication of a large matrix with a vector can be effected by solving a least squares problem (6.8O). Specifically, to solve for the kth product $\mathbf { y } = \mathbf { R } _ { m }$ , we solve [103]

$$
\operatorname* { m i n } { \left\| \left[ \begin{array} { c } { \mathbf { G } } \\ { \alpha \mathbf { L } } \end{array} \right] \mathbf { y } - \left[ \begin{array} { c } { \mathbf { G } \mathbf { v } _ { k } } \\ { \mathbf { 0 } } \end{array} \right] \right\| _ { 2 } ^ { 2 } } .
$$

It is necessary to solve $s$ least squares systems of equations (6.94) to calculate (6.93). In practice, relatively small values of $s$ in (6.93) (e.g.,100 to 1000) are adequate even when there are tens or hundreds of thousands of model parameters [103].

The stochastic algorithm (6.93) can also be used to implement generalized cros-validation. In (4.74), the most difficult computation is evaluation of the trace of $\mathbf { I } - \mathbf { G } \mathbf { G } ^ { \sharp }$ . Computing this matrix explicitly and then evaluating the trace would require excessive time and storage. Using (6.93) and evaluating the necessary $\mathbf { G } ^ { \sharp }$ matrix-vector multiplications by solving an associated least squares problem using an iterative method such as LSQR or CGLS makes it tractable to compute an approximation to the GCV function (4.74), where we solve $s$ least squares problems for each value of $\alpha$ [103].

# Example 6.4

We will examine the solution to a large-scale tomography problem involving 30,000 rays passing through a cubic volume discretized into a 30 by 30 by 3O model of 27,000 cells (Figure 6.13).

![](images/e3b1cf943a822f6c7f324ccaf72ec9983add02967f2752880d2dd55d16901731.jpg)  
Figure 6.13 A 30 by 30 by 30 block tomography model interrogated by 30,000 ray paths.

Ray path start and end points are uniformly randomly distributed across the sides of the volume with 10,OoO rays passing between each pair of parallel sides. The corresponding $\mathbf { G }$ matrix is 30,000 by 27,000,but only $0 . 2 \%$ of its entries are nonzero. Synthetic travel time data (with travel time perturbation values between approximately $- 2 0$ and 30 time units) were generated from a zero-mean smooth model with $N ( 0 , ( 0 . 5 ) ^ { 2 } )$ noise added. We implemented second-order Tikhonov regularization with a small amount of additional zeroth-order regularization to regularize the solution.

Figure 6.14 shows the L-curve for this problem. Figure 6.15 shows a plot of the GCV function (4.74) computed using stochastic estimates of the diagonal of $\mathbf { I } - \mathbf { G } \mathbf { G } ^ { \sharp }$ . The L-curve corner and GCV minimum both occur at about $\alpha = 0 . 5$ . For the solution obtained using $\alpha = 0 . 5$ , we computed a stochastic estimate of the diagonal of the reso-lution matrix using (6.93). For comparison, we also computed exact resolution matrix diagonal element values for 1OO randomly selected indices using (6.79). Figure 6.16 shows a scatter plot of the stochastic estimates compared with corresponding exact determinations, and indicates that the stochastic estimates are accurate to a few percentage points. It is common to use counts of the number of rays transecting each cell as a proxy for assessing the diagonal of the resolution matrix in tomographic problems. In general, the association between ray density and resolution in a tomography problem will depend on the specific ray path geometry. Figure 6.17 shows a scatter plot of the ray densities versus the accurately computed values of the diagonal elements of $\mathbf { R } _ { m }$ for the $1 0 0 \ \mathrm { r a n - }$ dom indices plotted in Figure 6.16. The relationship shows a nonlinear trend between ray density and the resolution diagonal element values, and there are also anomalously wel-resolved outliers in the plot with resolution diagonal element values greater than 0.9.Further examination shows that the anomalously well-resolved outliers correspond to cells that reside on the model exterior and are thus constrained by two-dimensional ray path geometries.

![](images/48f4101596b3e1d7173be50d493a723a14666c36d6d582ad9fa83e7684b8ec7f.jpg)  
Figure 6.14 L-curve for the tomography example of Figure 6.13 and its corner near $\alpha = 0 . 5$

![](images/983c4e6c66596e0f67ad288882ae450f299d970231d960ca37aa8578d317329a.jpg)  
Figure 6.15 GCV plot for the tomography example of Figure 6.13 and its minimum near $\alpha = 0 . 5$

![](images/2dc515ad9c4503c62e577513ee28805d1390e3c5617dab7be445821f95305057.jpg)  
Figure 6.16 Stochastic estimates versus computed values of the diagonal of $\mathbf { R } _ { m }$

![](images/032b28332994767fe93cc81222ad2c83f5da204f234893f408493c2db18c3762.jpg)  
Figure 6.17 Comparison of ray densities and resolution.

# 6.6. EXERCISES

1. Consider the cross-well tomography problem of Exercise 4.3.

a. Apply Kaczmarz's algorithm to this problem.   
b. Apply ART to this problem.   
c.Apply SIRT to this problem.   
d. Comment on the solutions that you obtained.

2. A very simple iterative regularization method is the Landweber iteration [67]. The algorithm begins with $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$ ,and then follows the iteration,

$$
\mathbf { m } ^ { ( k + 1 ) } = \mathbf { m } ^ { ( k ) } - \omega ( \mathbf { G } \mathbf { m } ^ { ( k ) } - \mathbf { d } ) .
$$

To ensure convergence, the parameter $\omega$ must be selected so that $0 < \omega < 2 / s _ { 1 } ^ { 2 }$ ， where $s _ { 1 }$ is the largest singular value of $\mathbf { G }$

In practice, the CGLS method generally works better than the Landweber iteration. However, it is easier to analyze the performance of the Landweber iteration. It can be shown that the kth iterate of the Landweber iteration is exactly the same as the SVD solution with filter factors of

$$
f _ { i } ^ { ( k ) } = 1 - ( 1 - \omega s _ { i } ^ { 2 } ) ^ { k } .
$$

a. Implement the Landweber iteration and apply it to the Shaw problem from Example 4.3.

b. Verify that $\mathbf { m } ^ { ( 1 0 ) }$ from the Landweber iteration matches the SVD solution with filter factors given by (6.96).   
c. Derive (6.96).

3.The Landweber iteration described in the previous exercise converges under the condition that $0 < \omega < 2 / s _ { 1 } ^ { 2 }$ ，where $s _ { 1 }$ is the largest singular value of $\mathbf { G }$ (or equivalently, $s _ { 1 } = \| \mathbf G \| _ { 2 } )$ . As a practical matter we typically cannot compute the full SVD of $\mathbf { G }$ . However, it is possible to rapidly estimate this quantity using an iterative method that we will derive in this exercise. Recall from Appendix A that $\| \mathbf G \| _ { 2 } = s _ { 1 }$ is the square root of the largest eigenvalue of the matrix $\mathbf { G } ^ { T } \mathbf { G }$

a. Using (A.77), diagonalize the matrix $\mathbf { A } = \mathbf { G } ^ { T } \mathbf { G }$ and use the diagonalization to show that

$$
\mathbf { A } ^ { n } = \mathbf { P } \mathbf { A } ^ { n } \mathbf { P } ^ { - 1 } .
$$

Assume that the eigenvalues of A are sorted so that $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdot \ \cdot \ \cdot \geq \lambda _ { n } \geq 0$

b. Take an arbitrary vector $\mathbf { x }$ in $\mathbf { R } ^ { n }$ , and write it in terms of the eigenvectors of $\mathbf { A }$ as

$$
\mathbf { x } = \alpha _ { 1 } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } \mathbf { v } _ { n } .
$$

Then show that

$$
\mathbf { A } ^ { k } x = \alpha _ { 1 } \lambda _ { 1 } ^ { k } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } \lambda _ { n } ^ { k } \mathbf { v } _ { n } .
$$

c. Starting with a random vector $\pmb { x } _ { 0 }$ ，and assuming that $\alpha _ { 1 } \neq 0$ (a reasonable assumption for a random vector $\pmb { x } _ { 0 }$ ),show that

$$
\operatorname* { l i m } _ { k  \infty } { \frac { \| \mathbf { A } ^ { k } \mathbf { x } _ { 0 } \| _ { 2 } } { \| \mathbf { A } ^ { k - 1 } \mathbf { x } _ { 0 } \| _ { 2 } } } = \lambda _ { 1 } .
$$

This leads to a simple iterative algorithm for estimating $s _ { 1 } = \sqrt { \lambda _ { 1 } }$ . Start with a random vector $\mathbf { x } _ { \mathrm { 0 } }$ . In each iteration, let

$$
\mathbf { x } _ { k + 1 } = \frac { \mathbf { G } ^ { T } ( \mathbf { G } \mathbf { x } _ { k } ) } { \| \mathbf { x } _ { k } \| _ { 2 } }
$$

and let

$$
\begin{array} { r } { \rho _ { k } = \sqrt { \| \mathbf G ^ { T } ( \mathbf G \mathbf x _ { k } ) \| _ { 2 } } . } \end{array}
$$

The sequence $\rho _ { k }$ converges to $s _ { 1 }$ . This function is implemented in MATLAB as the normest function. Write your own implementation of this function and compare the results you obtain with normest.

4.Use the Landweber iteration discussed in Exercise 6.2 to deblur the image from Example 6.3. In order to use the Landweber iteration, you will need to estimate $s _ { 1 } = \| \mathbf G \| _ { 2 }$ ， which can be done using the normest command discussed in Exercise 6.3.

5. In Example 6.3 we have included a function blur that computes the system matrix for the problem of deblurring an image that has been blurred by a Gaussian point spread function. The fle blur.mat contains a blur-inducing sparse $\mathbf { G }$ matrix and a data vector $\mathbf { d }$ ， where the 100 by 10O pixel gray-scale image is mapped into d using a column-by-column indexing convention.

a. How large is the $\mathbf { G }$ matrix? How many nonzero elements does it have? How much storage would be required for the $\mathbf { G }$ matrix if all of its elements were nonzero? How much storage would the SVD of $\mathbf { G }$ require?   
b. Plot the raw image.   
c. Using the MATLAB cgls algorithm with 10O iterations, deblur the image by solving $\mathbf { G m } = \mathbf { d }$ and interpret the evolution of your solutions with increasing iterations.

6. Show that if $\mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \dots . . . , \mathbf { p } _ { n - 1 }$ are nonzero and mutually conjugate with respect to an $n \times n$ symmetric and positive definite matrix A,then the vectors are also linearly independent. Hint: Use the definition of linear independence.

7. Recal the iteratively reweighted least squares method introduced in Chapter 2. The system of equations (2.92) solved in each iteration of the IRLS algorithm might well be dense, even if the matrix $\mathbf { G }$ is sparse. However, this system of equations can also be thought of as the normal equations for a particular least squares problem that will be sparse when $\mathbf { G }$ is sparse. Write down this least squares problem. Write a MATLAB function that uses the lsqr routine to solve these least squares problems in an IRLS scheme to minimize $\| \mathbf { G m } - \mathbf { d } \| _ { 1 }$ Hint: Use the fact that R is a diagonal matrix with positive elements; you can take its square root.

# 6.7. NOTES AND FURTHER READING

Iterative methods for the solution of linear systems of equations are an important topic in numerical analysis. Some basic references include [5,87,135,142].

Iterative methods for tomography problems including Kaczmarz's algorithm, ART, and SIRTare discussed in [84,115,163],and parallel algorithms based on these methodologies are discussed in [3O]. These methods are often referred to as row action methods because they access only one row of the matrix at a time, which makes them relatively easy to implement in parallel processing. In practice, the conjugate gradient and LSQR methods generally provide better performance than the row action methods. There are some interesting connections between SIRT and the conjugate gradient method discussed in [120,146,147].

Hestenes and Stiefel are generally credited with the invention of the conjugate gradient method [72]. However, credit is also due to Lanczos [92]. The history of the conjugate gradient method is discussed in [55,71]. Shewchuk's technical report [142] provides an introduction to the conjugate gradient method with illustrations that help to make the geometry of the method very clear. Filter factors for the CGLS method similar to those in Exercise 2 can be determined. These are derived in [65]. The LSQR method of Paige and Saunders [65,123,124] is an alternative way to apply the CG method to the normal equations. The resolution of LSQR solutions is discussed in [12,13]. Schemes have been developed for using CGLS with explicit regularization and dynamic adjustment of the regularization parameter $\alpha$ [85,86, 106]. This can poten-tially remove the computational burden of solving the problem for many values of $\alpha$ An alternative approach can be used to compute regularized solutions for several values of $\alpha$ at once [5O]. The performance of the CG algorithm degrades dramatically on poorly conditioned systems of equations. In such situations a technique called preconditioning can be used to improve the performance of CG. Essentially, preconditioning involves a change of variables $\bar { \boldsymbol { x } } = \mathbf { C } \boldsymbol { x }$ The matrix $\mathbf { C }$ is selected so that the resulting system of equations will be better conditioned than the original system of equations [38,53，164]. The conjugate gradient method can also be generalized to nonlinear minimization problems [58,142].

Inverse problems in image processing are a very active area of research. Some books on inverse problems in imaging include [14,115].

# Additional Regularization Techniques

# Synopsis

Alternatives or adjuncts to Tikhonov regularization are introduced. Bounds constraints allow the use of prior knowledge on the permissible range of parameter values. Sparsity regularization selects solutions with the minimum number of nonzero model parameters.A modification of the iteratively reweighted least squares algorithm presented in Chapter 2 for 1-norm parameter estimation is introduced to solve these problems.In compressive sensing, sparsity regularization is applied in association with a change of basis, where the basis is chosen so that the desired model will be sparse (i.e., have only a few nonzero coefficients in the model expansion). Total variation regularization uses a regularization term based on the 1-norm of the model gradient that allows for discontinuous jumps in the model to bias the solution towards piecewise-constant functions.

# 7.1. USING BOUNDS AS CONSTRAINTS

In many physical situations,bounds exist,or can be usefully estimated,on the maximum and/or minimum values of model parameters. For example, the model parameters may represent a physical quantity such as density that is inherently non-negative, establishing a strict lower bound for model parameters of 0. The problem of solving for a least squares solution that includes this constraint, referred to as non-negative least squares (NNLS), can be expressed as

$$
\begin{array} { r } { \operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \qquad } \\ { \mathbf { m } \geq \mathbf { 0 } , } \end{array}
$$

where $\mathbf { m } \geq \mathbf { 0 }$ means that every element of the vector m must be non-negative. This problem can be solved by an algorithm called non-negative least squares (NNLS) that was originally developed by Lawson and Hanson [94]. MATLAB includes a command, lsqnonneg, that solves the NNLS problem.

We might also declare a strict upper bound, so that model parameters may not exceed some value, for example,a density $3 5 0 0 \mathrm { k g } / \mathrm { m } ^ { 3 }$ for crustal rocks in a particular region.

Given the lower and upper bound vectors l and $\mathbf { u }$ , we can pose the bounded variables least squares (BVLS) problem:

$$
\begin{array} { r } { \operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } } \\ { \mathbf { m } \geq \mathbf { l } } \\ { \mathbf { m } \leq \mathbf { u } . } \end{array}
$$

Given a BVLS algorithm for solving (7.2),we can also perform Tikhonov regulariza-tion with bounds by augmenting the system of equations (e.g.，(4.5) and then solving the augmented system under bounding constraints. Stark and Parker [15O] developed an algorithm for solving the BVLS problem, which we employ here as a MATLAB function bvls.m. A similar algorithm is given in the 1995 edition of Lawson and Hanson's book [94].

A related optimization problem involves minimizing or maximizing a linear function of the model for a set of $n$ coefficients $c _ { i }$ , subject to bounds constraints and a constraint on the misfit. This problem can be formulated as

$$
\begin{array} { r } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { m } } \\ { \| \mathbf { G m } - \mathbf { d } \| _ { 2 } \leq \delta } \\ { \mathbf { m } \geq 1 } \\ { \mathbf { m } \leq \mathbf { u } . } \end{array}
$$

# Example 7.1

Recall the source history reconstruction problem of Example 1.7, where data are taken in concentration units at spatial positions, $_ x$ ,at a particular time (assumed dimensionless here), $T$ .Figure 7.1 shows the true (smooth) source model used to generate the data, and Figure 7.2 shows these data as a function of distance, $_ x$ ，at time $T = 3 0 0$ ，with $N ( 0 , 0 . 0 0 1 ^ { 2 } )$ noise added.

Figure 7.3 shows the least squares solution, which has the extremely large amplitudes and oscillatory behavior characteristic of an unregularized solution to an ill-posed problem. This solution is, furthermore, physically unrealistic in having negative concentrations. Figure 7.4 shows the non-negative least squares solution, which, although certainly more realistic in having all of the concentration values nonnegative, consists of high-amplitude spikes that do not accurately reconstruct the (smooth) true source history. Suppose that the solubility limit of the contaminant in water is known to be 1.1 units, thus providing a natural upper bound on model parameters. Figure 7.5 shows the corresponding BVLS solution,which exhibits spiky features similar to those of Figure 7.4. Further regularization is indicated if we believe that the true model is smooth.

![](images/4b1e6172ff84518030fb6c52d0a7d41f083edb02d9bdd87c19f1da3d7c113bd2.jpg)  
Figure 7.1 True source history.   
Figure 7.2 Concentration data as a function of position, $x ,$ taken at $T = 3 0 0$

Figure 7.6 shows the L-curve for a second-order Tikhonov regularization solution applied with bounds of $0 \leq \mathbf { m } \leq 1 . 1$ on the model vector elements. Figure 7.7 shows the regularized solution for $\alpha = 0 . 0 1$ . This solution correctly reveals the two major input concentration peaks. As is typical for cases of non-ideal model resolution,the solution peaks are somewhat lower and broader than those of the true model. This solution does not,however, resolve the smaller subsidiary peak near $t = 1 5 0$

![](images/74388ad4f919d3df0f47f1d98e0b32f5c2b7f083034920afa933bb59d05bed47.jpg)  
Figure 7.3 Least squares source history solution with true history (Figure 7.1) shown as a dashed curve. Because the least squares solution has extremely large amplitudes,the true model appears as aflat line at this scale.   
Figure 7.4 NNLS source history solution with true history (Figure 7.1) shown as a dashed curve.

We can additionally use (7.3) to establish bounds on linear combinations of the model parameters. For example, we might want to establish bounds on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . These concentrations appear in positions 51 through 60 of the model vector m. We let $c _ { i }$ be zero in positions 1 through 5O and 61 through 100,and let $c _ { i }$ be 0.1 in positions 51 through 6O to form a 1O-time-sample averaging function.

![](images/932d5d42c5f78d05208e947ccee6fedf5d731501e0d1c2004b4539e3fb2447fe.jpg)  
Figure7.5 BVLS source history solution $\mathbf { \left( 1 = 0 , u = 1 . 1 \right. }$ with true history(Figure7.1) shown as a dashed curve.   
Figure 7.6 L-curve for the second-order Tikhonov solution with BVLS $\mathbf { \Omega } ( \mathbf { l } = \mathbf { 0 }$ ， $\mathbf { u } = \mathbf { 1 . 1 }$ ) implementation, cornerat $\alpha = 0 . 0 1$ .

The value of $\mathbf { c } ^ { T } \mathbf { m }$ is the average of model parameters 51 through 60. The value of the solution to (7.3) will then be a lower bound on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . Similarly, by maximizing $\mathbf { c } ^ { T } \mathbf { m }$ or equivalently by minimizing $- \mathbf { c } ^ { T } \mathbf { m }$ we can obtain an upper bound on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . Solving the minimization problems for $\mathbf { c } ^ { T } \mathbf { m }$ and $- \mathbf { c } ^ { T } \mathbf { m }$ ，we obtain, respectively,a lower bound of O.36 and an upper bound of O.73 for the average concentration during this time period. The true concentration average over this interval (Figure 7.1) is 0.57.

![](images/d34b9b91375431103177537eb9f05c28f0392baab33c8dd79e9a9e248c8bd0b5.jpg)  
Figure7.7 Second-order Tikhonov regularization source history solution determined from the L-curve of Figure 7.6,with true history (Figure 7.1) shown as a dashed curve.

# 7.2. SPARSITY REGULARIZATION

In some situations there are reasons to expect that many of the unknown model parameters will be zero.Rather than using Tikhonov regularization to minimize $\| \mathbf { m } \| _ { 2 }$ ，we may choose to minimize the number of nonzero entries in m to obtain a sparse model.

The notation $\| \mathbf { m } \| _ { 0 }$ is commonly used to denote the number of nonzero entries in $\mathbf { m }$ (Note that this O-norm definition is nonstandard because it is inconsistent with the definition of the $p$ -norm in (A.85) and does not satisfy the requirements for a vector norm in Section A.7.） We can formulate a corresponding regularized inverse problem as

$$
\begin{array} { c } { { \operatorname* { m i n } \ \| \mathbf { m } \| _ { 0 } } } \\ { { \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

Unfortunately, these kinds of optimization problems can be extremely diffcult to solve.

A surprisingly effective alternative to (7.4) is to instead find the least squares solution that minimizes $\| \mathbf { m } \| _ { 1 }$ . To see that this is a reasonable approach,consider the set of models with $\| \mathbf { m } \| _ { 2 } = 1$ . Among the models with $\| \mathbf { m } \| _ { 2 } = 1$ , it turns out that the models with precisely one nonzero entry of $+ 1$ or $- 1$ have the smallest 1-norms (Figure 7.8). Thus,regularizing a least squares problem to minimize its model 1-norm will tend to produce sparse solutions. This tendency for 1-norm regularized models to be sparse becomes even more prominent in higher dimensions. The heuristic approach of minimizing $\| \mathbf { m } \| _ { 1 }$ instead of $\| \mathbf { m } \| _ { 0 }$ works very well in practice,and recent work [21] has demonstrated reasonable conditions under which the solution to the 1-norm regularized problem is identical to or at least close to the solution of the O-norm regularized problem (7.4).

![](images/af87b7d6cec6c3c76ce9cff3dc1c35a9618d4fb9e1c1e6d24f4d828a11f13476.jpg)  
Figure 7.8 Two-dimensional demonstration of the use of model 1-norm minimization (7.5) to obtain sparsity regularization.The square shaded area shows the region $\| \mathbf { m } \| _ { 1 } \leq c _ { 1 }$ ,while the circle shows the region with $\| \mathbf { m } \| _ { 2 } \leq c _ { 2 }$ .An arbitrary constraint equation in this 2-dimensional model space, $( \mathbf { G m } ) _ { i } -$ $d _ { i } = 0$ ,defines a line.The minimum 2-norm residual model satisfying the constraint $\mathbf { m } _ { 2 }$ ,will not generally be sparse. However,the minimum 1-norm model satisfying the constraint, $\mathbf { m } _ { 1 } = [ 0 c _ { 1 } ] ^ { T }$ , will tend to be sparse due to the presence of corners in the 1-norm contour.

The $L _ { 1 }$ regularized least squares problem can be written as

$$
\begin{array} { c } { { \operatorname* { m i n } \ \| \mathbf { m } \| _ { 1 } } } \\ { { \| \mathbf { G m } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

Using the standard approach of moving the constraint into the objective function, we can select a positive regularization parameter, $\alpha$ , so that this is equivalent to

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { m } \| _ { 1 } .
$$

This is a convex optimization problem that can be solved efficiently by many different algorithms. We next present an iterative least squares solution method.

# 7.3. USING IRLS TO SOLVE $L _ { 1 }$ REGULARIZED PROBLEMS

To solve problems of the form of (7.6) we extend the IRLS algorithm introduced in Chapter 2 for $L _ { 1 }$ regression. Let

$$
f ( \mathbf { m } ) = \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { L m } \| _ { 1 }
$$

and let

$$
\mathbf { y } = \mathbf { L m } .
$$

At points where any element of $\mathbf { L m }$ is zero, $f ( \mathbf { m } )$ is not differentiable because of the nondifferentiability of the absolute values in the $L _ { 1 }$ norm. However, at other points we can easily compute the gradient of $\boldsymbol { \mathsf { \Sigma } }$

$$
\nabla f ( \mathbf { m } ) = 2 \mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - 2 \mathbf { G } ^ { T } \mathbf { d } + \alpha \sum _ { i = 1 } ^ { m } \nabla | \gamma _ { i } | .
$$

For $\gamma _ { i }$ nonzero,

$$
\frac { \partial | \gamma _ { i } | } { \partial m _ { k } } = L _ { i , k } \mathrm { s g n } ( \gamma _ { i } ) .
$$

Writing $\operatorname { s g n } ( \gamma _ { i } )$ as $\gamma _ { i } / | \gamma _ { i } |$ , and using $\begin{array} { r } { \| \mathbf { L m } \| _ { 1 } = \sum _ { i = 1 } ^ { m } \| \gamma _ { i } \| } \end{array}$ , we obtain

$$
\frac { \partial \| \mathbf { L m } \| _ { 1 } } { \partial m _ { k } } = \sum _ { i = 1 } ^ { m } L _ { i , k } \frac { \gamma _ { i } } { | \gamma _ { i } | } .
$$

Let $\mathbf { w }$ be the diagonal matrix with elements

$$
W _ { i , i } = \frac { 1 } { | \gamma _ { i } | } .
$$

Then

$$
\nabla \mathbf { \Psi } ( \| \mathbf { L m } \| _ { 1 } ) = \mathbf { L } ^ { T } \mathbf { W } \mathbf { L m }
$$

and

$$
\boldsymbol { \nabla } f ( \mathbf { m } ) = 2 \mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - 2 \mathbf { G } ^ { T } \mathbf { d } + \alpha \mathbf { L } ^ { T } \mathbf { W } \mathbf { L } \mathbf { m } .
$$

Setting $\nabla f ( \mathbf { m } ) = \mathbf { 0 }$ ,we obtain

$$
\left( 2 \mathbf { G } ^ { T } \mathbf { G } + \alpha \mathbf { L } ^ { T } \mathbf { W } \mathbf { L } \right) \mathbf { m } = 2 \mathbf { G } ^ { T } \mathbf { d } .
$$

Because W depends on $\mathbf { L m }$ ,this is a nonlinear system of equations. Furthermore, $\mathbf { w }$ is not defined at any point where $\mathbf { L m }$ has a zero element.

To accommodate the nondifferentiability of the 1-norm at the origin，as in Chapter 2,we set a tolerance $\epsilon$ ,and let

$$
W _ { i , i } = \left\{ \begin{array} { l l } { 1 / | \gamma _ { i } | } & { | \gamma _ { i } | \geq \epsilon } \\ { 1 / \epsilon } & { | \gamma _ { i } | < \epsilon . } \end{array} \right.
$$

In the IRLS procedure, we solve (7.15), update $\mathbf { w }$ according to (7.16),and iterate until the solution has converged.

The system of equations (7.15) can be seen as the normal equations for the least squares problem,

$$
\begin{array} { r } { \operatorname* { m i n } \left\| \left[ \begin{array} { c } { \mathbf { G } } \\ { \sqrt { \frac { \alpha } { 2 } } \sqrt { \mathbf { W } } \mathbf { L } } \end{array} \right] \mathbf { m } - \left[ \begin{array} { c } { \mathbf { d } } \\ { \mathbf { 0 } } \end{array} \right] \right\| _ { 2 } . } \end{array}
$$

When $\mathbf { G }$ is large and sparse it can be extremely advantageous to apply LSQR to solve the least squares problem (7.17) rather than solving the system of equations (7.15).

# Example 7.2

Consider a deconvolution example in which a controlled surface source sends seismic waves down into the earth. Seismic reflections will occur from abrupt material discontinuities at various depths,and a seismogram of the reflected signals (which will generally include multiple reflections) is recorded at the surface. Here, $g ( t )$ is the known source signal, $d ( t )$ is the recorded seismogram, and $m ( t )$ is the unknown reflection response of the earth. We'd like to recover the times of these reflections to study the respon-sible earth structure. This is a linear forward problem characterized by a convolution (e.g., (1.11))

$$
d ( t ) = \int _ { - \infty } ^ { \infty } g ( t - \xi ) \ m ( \xi ) \ d \xi .
$$

In this highly simplified reflection seismology example,we will assume a onedimensional structure with depth and consider upward- and downward-traveling plane compressional seismic waves detected by a vertically oriented seismometer. In this case, the presence of horizontally oriented seismic structural discontinuities in an otherwise smooth medium will ideally be manifested in $m ( t )$ as a sequence of delta functions.As in Chapter 1, we will discretize $m ( t )$ as a model vector $\mathbf { m }$ . We seek models where m consists of an optimal sequence of spikes.

The source signal is a short pulse with a characteristic time of around $0 . 4 \ : s$

$$
g ( t ) = e ^ { - 5 t } \sin ( 1 0 t ) .
$$

We'll add independent normally distributed random noise to the corresponding recorded data (7.18) and attempt to recover $m ( t )$ in regularized inversions.All time series were sampled uniformly at 1OO samples/s to create model and data vectors of 1000 points spanning 1O-s time intervals. The true reflectivity model (Figure 7.9) is the response of a single subsurface reflector with a coefficient of $r = 0 . 4$ ,located at a depth corresponding to a two-way seismic travel time from the surface of $\tau = 1 . 5 s$ This source signal $g ( t )$ begins at $0 . 5 s$ ， and the primary reflection and surface-reflector multiples appear in Figure 7.9 as alternating-sign spikes at intervals of $\tau$ with amplitudes that decrease by a factor of $r$ upon each reflection. Figure 7.10 shows the corresponding data from (7.18) with $N ( 0 , ( 0 . 0 0 2 ^ { 2 } ) )$ noise added. The noise and smoothing from the convolution largely obscure the signal corresponding to the later impulses of Figure 7.9.

Figure 7.11 shows the L-curve for this problem with zeroth-order regularization, using the frequency-domain techniques described in Chapter 8,and Figure 7.12 shows a corresponding solution. The impulses are broadened relative to the true model due to the associated regularization bias,and there are noise-generated secondary peak. Figures 7.13, 7.14,and 7.15, however, show that using (7.5) produces excellent recovery of $m ( t )$ . Note that the spikes are correctly placed in time and that allare resolved save the tiny pulse at $7 . 5 \ : \mathrm { s }$ ,which has an amplitude of only $r ^ { 5 } \approx 0 . 0 1$ ,or just $1 \%$ of the amplitude of the source spike. The amplitude of the spikes is reduced and they are slightly broader than they should be,but the model is vastly better than that obtained with Tikhonov regularization.

![](images/1310c4404bddb190f759549757395b71c3c9a600a03dc2ceddd2cfc6b8c51db7.jpg)  
Figure 7.13 L-curve for the 1-norm regularized solution with corner at $\alpha = 2 . 4 \times 1 0 ^ { - 4 }$

![](images/149efb00f7b3be74675e4ba29229fc1610a8ff36b85855e6277c5180485f2e1c.jpg)  
Figure 7.14 1-norm regularized solutions corresponding to the range of regularization parameters used to construct Figure 7.13.Model corresponding to the L-curve corner is shown in bold.

In many situations, there is no reason to bias models to be sparse. If the true model is not sparse, then sparsity regularization will of course produce poor model recovery. However, it is possible in some cases to implement a change of variables so that the coefficients of the model with respect to the new basis wil be sparse, or can at least be well approximated by a sparse model.

Recall from Appendix A that if a set of vectors $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { n }$ form a basis for $R ^ { n }$ ， then any vector $\mathbf { m }$ in $R ^ { n }$ can be written as a linear combination of the basis vectors with $n$ coefficients, $x _ { i }$ ：

$$
\begin{array} { r } { { \bf m } = x _ { 1 } { \bf w } _ { 1 } + x _ { 2 } { \bf w } _ { 2 } + \cdot \cdot \cdot + x _ { n } { \bf w } _ { n } . } \end{array}
$$

In vector-matrix form, this can be writen as

$$
\mathbf { m } = \mathbf { W } \mathbf { x }
$$

where the basis vectors $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { n }$ are the columns of $\mathbf { w }$ . We can also perform the change of variables in the reverse direction as

$$
\mathbf { x } = \mathbf { W } ^ { - 1 } \mathbf { m } .
$$

In practice, linear transformation algorithms,such as the fast Fourier transform (FFT; Chapter 8) or discrete cosine transform (DCT),are often used in place of the matrixvector multiplications of (7.21） and (7.22) to effect the corresponding forward and inverse operations.

# Example 7.3

Figure 7.16 shows the 40,000-pixel image from Example 6.3. If we were to zero out any significant fraction of these pixels,the efect on the image would be quite obvious. However, if instead we encode the image in terms of the discrete cosine transform (DCT) of the pixel values,a sparser representation of the image is possible that closely approximates the original. Calculating the discrete cosine transform of the two-dimensional image using MATLAB's dct2 command produces a set of 40,000 coefficients. Of these 40,O0O coefficients, the 16,O0O coefficients ( $40 \%$ of the original coefficients) that were smallest in absolute value were set to zero.

After inverting the DCT, we produced the image shown in Figure 7.17. This second image appears to be very similar to the original image, yet $40 \%$ fewer coefficients were used to represent the image in terms of the DCT basis. This is because the coefficients associated with the 16,OOO unused basis vectors in the original image were small.

![](images/33e4d3d9dd9ce5e12fca16718c8193c8495902db4182ad9f623fb7a967571461.jpg)  
Figure 7.16 Image before discrete cosine transform threshholding.

![](images/6ee48c64c8caa51da21cf26064ff498763a4f7d5a48cb7c35379108689d80b97.jpg)  
Figure 7.17 Image after removing smallest $4 0 \%$ of DCT coefficients.

The discrete cosine transform is the basis for the widely used JPEG standard for image compression. Wavelet bases are also widely used in image processing,and threshholding the wavelet transform produces similar results in compressng images. The newer JPEG 2OOO standard for image compression uses wavelets rather than the discrete cosine transform.

In compressive sensing, we apply sparsity regularization using a basis chosen so that the model can be represented by a linear combination of the basis vectors with a sparse set of coefficients. The regularized problem can be written using (7.21) and (7.6) as

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { W } \mathbf { x } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { x } \| _ { 1 } ,
$$

where $\mathbf { G }$ is called the measurement matrix.

The recovery of a sparse solution using (7.23) depends on the details and appropriateness of the particular $\mathbf { G }$ and $\mathbf { w }$ used in (7.23). The analysis and implementation of compressive schemes become relatively simple if the measurement matrix is random [27].

# Example 7.4

Consider the recovery of a signal, $\mathbf { m }$ ，shown in Figure 7.18. This 10-s long time series of $n = 1 0 0 1$ time points, $t _ { i }$ ,is sampled at 1OO samples/s and consists of two sine waves at $f _ { 1 } = 2 5$ and $f _ { 2 } = 3 5 \mathrm { H z }$ ：

$$
m _ { i } = h _ { i } \cdot \left( 5 \cos ( 2 \pi f _ { 1 } t _ { i } ) + 2 \cos ( 2 \pi f _ { 2 } t _ { i } ) \right) 1 \leq i \leq n ,
$$

where the signal envelope has also been smoothed with term-by-term multiplication by a Hann taper function,

$$
h _ { i } = \frac { 1 } { 2 } \ \left( 1 - \cos ( 2 \pi ( i - 1 ) / n ) \right) \ 1 \leq i \leq n .
$$

In the standard basis, the signal (7.24),shown in Figure 7.18, is obviously not sparse. However, because it is constructed from two cosine components, this model has a very sparse representation in the DCT basis.

We use a random measurement matrix $\mathbf { G }$ that is $m = 1 0 0$ by $n = 1 0 0 1$ ，with entries chosen independently from $N ( 0 , 1 )$ to generate a synthetic set of 1OO data measurements, $\mathbf { d } = \mathbf { G } \mathbf { m }$ ，and then add independent $N ( 0 , 2 5 )$ noise. The matrix of basis vectors, $\mathbf { w }$ ，is constructed by applying the discrete cosine transform to standard basis vectors for the model space $R ^ { n }$ .

Figures 7.19 and 7.2O show solutions obtained by solving $\mathbf { G m } = \mathbf { d }$ using secondorder Tikhonov regularization.The highlighted solution $( \alpha = 1 0 0 )$ fits the data with a residual norm that approximately satisfies the discrepancy principle, so that $\| \mathbf G \mathbf m - \mathbf d \|$ $\approx 5 \cdot { \sqrt { m } } = 5 0 .$ However, this solution,and others across a wide range of $\alpha$ values, bear essentially no resemblance to the true signal shown in Figure 7.18.

![](images/2b1b88c17e560b9151b71d74fdd300b38c7d50f3a67c5ce2fbb73355d21d3295.jpg)  
Figure 7.18 A 1001-point signal consisting of 25-and $3 5 - 1 1 z$ cosines (7.24), multiplied bya Hann taper.

![](images/7220a3055d3e57a89de787f33b37f79d07b34664487489f83f94a106471da223.jpg)  
Figure 7.19 Signal recovery using second-order Tikhonov regularization. Solution amplitudes are normalized to improve legibility.

![](images/2cfc7ce42ed5d020f7abe6d58970e8520fd29f4378a3dc1e00bb60db0063e8be.jpg)  
Figure7.20 Arepresentative solution using second-order Tikhonov regularization that approximately satisfies the discrepancy principle from Figure 7.19 $( \alpha = 1 0 )$ .

An L-curve obtained by solving (7.23） for $n$ DCT coefficients $\mathbf { x }$ ，and subsequently constructing models $\mathbf { w _ { x } }$ for various $\alpha$ values， shows a very abrupt corner near $\alpha = 1 0 ^ { - 1 1 }$ . For very low levels of regularization beyond this corner, solutions rapidly transition from excellent model recovery to essentially random noise. For $\alpha$ values greater than a few hundred,on the other hand, solutions rapidly approach the zero model. For a wide range of $\alpha$ values between these extreme values, the recovered signal $\mathbf { w _ { x } }$ is stable and is quite close to the true signal (Figures 7.21 and 7.22).

It may seem paradoxical that we can recover a 1OO1-point signal so well from only 10O random linear combination measurements, when the Nyquist sampling theo-rem (8.4O) suggests that at least $1 0 \mathrm { s } \times 3 5 \mathrm { H z } \times 2 = 7 0 0$ equally spaced samples should be required to accurately represent it. This is possible in the current example because the measured signal is sparse with respect to the DCT basis,and just a few cosine basis functions are therefore necessary to represent it well. The corresponding sparse set of coefficients is easily recovered when sparsity regularization is employed.

# 7.4.TOTAL VARIATION

Total variation (TV) regularization is appropriate for problems where we expect there to be discontinuous jumps in the model. In the one-dimensional case, the TV regularization function is

$$
\begin{array} { c } { { \displaystyle \mathrm { T V } ( } { \bf m } ) = \sum _ { i = 1 } ^ { n - 1 } | m _ { i + 1 } - m _ { i } | } \\ { { \displaystyle = \| { \bf L m } \| _ { 1 } } , } \end{array}
$$

where, for one-dimensional models, $\mathbf { L } = \mathbf { L } _ { 1 }$ (4.27). In higher-dimensional problems, $\mathbf { L }$ is a discretization of the gradient operator.

In first- and second-order Tikhonov regularization, discontinuities in the model are smoothed out and do not show up well in the inverse solution.This is because smooth changes are penalized less by the regularization term than sharp ones. The particular feature of (7.27) is that the regularization term imposes a constraint to keep the number of discontinuous transitions to a minimum (i.e., keeping $\mathbf { L m }$ sparse). We can insert the TV regularization term (7.27) in place of $\| \mathbf { L m } \| _ { 2 } ^ { 2 }$ in the Tikhonov regularization optimization problem to obtain

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { L } \mathbf { m } \| _ { 1 } ,
$$

which is a convex optimization problem in the form of(7.6) that imposes a higher-order sparsity constraint.

![](images/6a01be28d916c84da9a05c7a193e281278f0ee42c4824d06e160babe0a29cb89.jpg)  
Figure 7.21 Signal recovery using compressive sensing with 100 signal measurements.Solution amplitudes are normalized to improve legibility.

![](images/f842765fb5f303b27d6e3adda3fb25812c0620f9add26f8742bfa151af09b1f8.jpg)  
Figure 7.22 A representative solution obtained from Figure 7.21 using compressive sensing with $\alpha = 1 0 0$ thatapproximately satisfies the discrepancy principle.

This approach has seen wide use in the problem of “denoising” a model [122]. Denoising is a linear inverse problem in which $\mathbf { G } = \mathbf { I }$ . In denoising,the general goal is to remove features considered to be spurious from a signal, while still retaining other key features, such as long-term trends and perhaps sharp discontinuities.

# Example 7.5

Figure 7.23 shows a signal that is smooth with the exception of two discontinuous jumps at 2 and $7 s .$ Figure 7.24 shows the signal after $N ( 0 , 4 )$ independent noise has been added. Our goal is to remove this noise from the signal while optimally recovering the discontinuities.

![](images/b296fa6116efce638719ef34e578a98030fbddf27efe2b03daa1e5c783a21f51.jpg)  
Figure 7.23 An otherwise smooth signal with two sharp discontinuities.

![](images/59c90c6adb615f5f9288e7b9b3adcebb658f0e29cadf160f252602312a39d7dd.jpg)  
Figure 7.24 The signal with $N ( 0 , 4 )$ noise added.

We first attempt to denoise the signal using second-order Tikhonov regularization with L given by (4.28). The L-curve is shown in Figure 7.25,and the resulting solution is shown in Figure 7.26. If the location of the large discontinuities is a feature that we wish to recover, this solution obviously does not do a good job because the regularization scheme biases the model based on smoothness.

![](images/3944424a11a61d7841da02b65520b251a3faabc49f1d4b9ac419a32c329824be.jpg)  
Figure 7.25 L-curve with second-order Tikhonov regularization with corner at $\alpha = 1 0 0 0$

![](images/4cfaa4afdec204beea8d0831571c0f30fa1844a031a0a7451647241b155ed298.jpg)  
Figure 7.26 Second-order Tikhonov solution $( \alpha = 1 0 0 0 )$ ）with the true model plotted as a dashed curve.

We next apply TV regularization to solve the problem. Figure 7.27 shows the L-curve trade-off between $\| \mathbf { m } - \mathbf { d } \| _ { 2 }$ and $\| \mathbf { L m } \| _ { 1 }$ , and the presence of a corner near $\alpha \approx 1 8$ . Figure 7.28 shows the corresponding models for various levels of regular-ization, with the optimal one selected from the L-curve shown in Figure 7.29. This piecewise-constant recovery of the original signal reveals the large discontinuities at $2 \thinspace s$ and $7 s$ quite well.

![](images/fbf26c7c06e076974fe2c54e189cbed858db71ccea266d5a2210a2c29ad4b5a7.jpg)  
Figure 7.27 L-curve for TV regularization with corner at $\alpha = 1 8$

![](images/210d70ce0c95e9b76e5056b4b8cb634d71fde98586cd1918313f3c8571fd8084.jpg)  
Figure 7.28 Signal recovered with TV regularization with model corresponding to the L-curve corner shown in bold.

![](images/51464e4e49057b18cfddda687fb0715465de6f484f1cdad1a7ebd90938087af9.jpg)  
Figure 7.29 Signal recovered with TV regularization for $\alpha = 1 8$ from Figure 7.28 with the true model plotted as a dashed curve.

# 7.5. EXERCISES

1. Using the method of Lagrange multipliers, develop a formula that can be used to solve

$$
\begin{array} { l } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { m } } \\ { \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \leq \delta . } \end{array}
$$

2.Noisy seismic travel time data (units of s) from equally spaced (every $2 0 \mathrm { m } )$ seismometers deployed in a $1 0 0 0 \mathrm { - m }$ deep vertical seismic profile experiment (the same geometry as in Example 4.4) are to be inverted to reveal the slowness of the earth as a function of depth. Invert the data in vsp.mat using TV regularization with an L-curve analysis and assess the presence of any likely discontinuities. Compare this with the least squares solution and with a direct finite-difference solution suggested by (1.22).

3.In many cases, it is valuable to implement multiple regularization constraints,such as smoothness combined with bounds. Consider the gravity anomaly data in the vector $\mathbf { d n }$ (units of $\mathrm { m } / \mathrm { s } ^ { 2 }$ ） found in the file gdata.mat. The data are taken at the surface above a $1 0 0 0 \mathrm { m }$ section of a partially debris-blocked buried pipe located with its center at a depth of $2 5 \mathrm { m }$ .Use the methodology of Example 1.4 to invert these data for subsurface density perturbations,assuming that the pipe has a cross-sectional area of $1 ~ \mathrm { m } ^ { 2 }$ . Anomalous density along the pipe relative to background density is parameterized as point masses located at 1OO equally spaced points along the section, as specified by the vector rhox. The noisy surface gravity anomaly observations contained in the vector $\mathbf { d n }$ are made at 5OO points along the same $1 0 0 0 \mathrm { m }$ span as the buried pipe section of interest at points specified in the vector $\mathbf { x }$ Invert the data for density perturbations along the buried pipe by assuming that all mass in each segment can be concentrated at the points specified by rhox.

a. Invert for density perturbations along the pipe transect in $\mathrm { k g } / \mathrm { m } ^ { 3 }$ using least squares.   
b. Invert for density perturbations along the pipe transect in $\mathrm { k g } / \mathrm { m } ^ { 3 }$ using secondorder Tikhonov regularization and an L-curve analysis.   
c. Solve the problem using second-order Tikhonov regularization combined with BVLS and an L-curve analysis. Employ the knowledge that density variations for $x < 9 1$ and $x > 8 9 9 \mathrm { ~ m ~ }$ are negligible, and that the density variations overall are bounded by $- 1 5 0 \mathrm { k g / m ^ { 3 } } \le \delta \rho \mathrm { ( x ) } \le 1 5 0 \mathrm { k g / m ^ { 3 } }$   
d. Compare and discuss your three solutions. Where are the prominent maxima and minima located?

4.Returning to the problem in Exercise 3.1,solve for the density profile using total variation regularization.How does your solution compare to the solutions obtained in Exercise 3.1 and Exercise 4.4?

# 7.6.NOTES AND FURTHER READING

Methods for bounded variables least squares problems and minimizing a linear function subject to a bound on the misfit are given in [15O]. Some applications of these techniques can be found in [73,125,128,148,149]. There is a long history of sparsity regularization in geophysical inverse problems. Claerbout and Muir were early advocates of this approach [31]; however, there was litle theoretical justification for this prior to the work of Candes, Romberg,and Tao,which brought about a resurgence of interest in this methodology [24,25,26]. In recent years there has been an explosion of interest in compressve (or compressed) sensing, with applications in many areas of signal and image processing and inverse problems. There are numerous surveys and tutorials on compressive sensing, including [21,27,1O4]. Methods for total variation regularization are discussed in [122,169].

# Fourier Techniques

# Synopsis

The formulation of a general linear forward problem as a convolution is derived. The Fourier transform, Fourier basis functions,and the convolution theorem are introduced for continuous- and discrete-time systems. The inverse problem of deconvolution is explored in the context of the convolution theorem. Water level and Tikhonov regularization in the frequency domain are employed to solve discrete deconvolution problems.

# 8.1.LINEAR SYSTEMS IN THE TIME AND FREQUENCY DOMAINS

A remarkable feature of linear time-invariant systems is that the forward problem can generally be described by a convolution (1.11),

$$
d ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau .
$$

Inverse problems involving such systems can be solved by deconvolution. Here, the independent variable $t$ is time,and the data $d$ ，model $m$ ，and system kernel $g$ are all time functions. However, the results here are equally applicable to spatial problems (e.g., Example 8.1) and to higher dimensions. We will first overview the essentials of Fourier theory in the context of performing convolutions and deconvolutions.

Consider a linear time-invariant forward operator, $G$ ,that maps an unknown model function, $m ( t )$ ,into an observable data function, $d ( t )$ ，

$$
d ( t ) = G [ m ( t ) ] .
$$

Because it is linear and time-invariant, (8.2) obeys the principles of superposition (1.5) and scaling (1.6). It is possible to show that any such system can be cast in the form of (8.1), by utilizing the sifting property of the impulse or delta function, $\delta ( t )$ . The delta function can be conceptualized as the limiting case of a pulse as its width goes to zero, its height goes to infinity,and its area stays constant and equal to one, for example, as the limiting case ofa unit area Gaussian pulse centered on the origin,

$$
\delta ( t ) = \operatorname* { l i m } _ { \sigma \to 0 } \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } / \sigma _ { . } ^ { 2 } } \nonumber
$$

The sifting property of the delta function extracts the value of a function at a particular point from within a definite integral

$$
\int _ { a } ^ { b } f ( t ) \delta ( t - t _ { 0 } ) \ d t = { \left\{ \begin{array} { l l } { f ( t _ { 0 } ) } & { a \leq t _ { 0 } \leq b } \\ { 0 } & { { \mathrm { e l s e w h e r e } } , } \end{array} \right. }
$$

for any $f ( t )$ that is continuous at finite $t = t _ { 0 }$ . The impulse response, or Green's function, $g ( t )$ , for a system where the model and data are related by an operator $G$ as in (8.2), is defined as the system output (data) for a delta function input (model),

$$
g ( t ) = G [ \delta ( t ) ] .
$$

The concept of the impulse response can be used to demonstrate our initial assertion in this chapter that linear time-invariant forward problems can generally be expressed as convolutions.

Theorem 8.1 We begin with a restatement of (8.2);

$$
d ( t ) = G [ m ( t ) ] .
$$

$m ( t )$ can be writen as a summation of impulse functions by invoking (8.4),

$$
m ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) \delta ( t - \tau ) \ d \tau ,
$$

and we can thus write

$$
d ( t ) = G \left[ \int _ { - \infty } ^ { \infty } m ( \tau ) \delta ( t - \tau ) \ d \tau \right] .
$$

Applying the definition ofthe integral as a limit of a sum of $\Delta t$ width rectangular areas as $\Delta t$ goes to zero, we have

$$
d ( t ) = G \Biggl [ \underbrace { l i m } _ { \Delta \tau  0 } \sum _ { n = - \infty } ^ { \infty } m ( \tau _ { n } ) \delta ( t - \tau _ { n } ) \Delta \tau \Biggr ] .
$$

Because $G$ is a linear and time-invariant operator, superposition allws us to move the operator inside of the summation in (8.9). Furthermore, using the scaling relation, we can factor out the

coeffcients $m ( \tau _ { n } )$ from inside of the operator to obtain

$$
d ( t ) = l i m \sum _ { \Delta \tau  0 } ^ { \infty } \sum _ { n = - \infty } ^ { \infty } m ( \tau _ { n } ) G [ \delta ( t - \tau _ { n } ) ] \Delta \tau .
$$

In the limit as $\Delta t \to 0$ and substituting (8.5)， (8.10) thus defines the integral

$$
d ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau ,
$$

which is identical to $( 8 . 1 )$ , the convolution of $m ( t )$ and $g ( t )$

Note that it is common to denote the convolution of two functions $h _ { 1 } ( t )$ and $h _ { 2 } ( t )$ simply as $h _ { 1 } ( t ) * h _ { 2 } ( t ) = h _ { 2 } ( t ) * h _ { 1 } ( t )$ . The indicated reciprocity is easily demonstrated from (8.11) with a change of variables.

Convolution can thus be used to describe the mapping of models to data for any linear time-invariant system. Important examples include the mapping between a physical process and a set of observables that occurs in a forward problem,or the output of a linear instrumentation system. For example,a perfect instrument that recorded some model $m ( t )$ with perfect fidelity, but imposed a time delay $t _ { \mathrm { 0 } }$ , would have a time-delayed delta function impulse response:

$$
\begin{array} { l } { d ( t ) = m ( t ) * \delta ( t - t _ { 0 } ) } \\ { \displaystyle \qquad \propto \qquad } \\ { \displaystyle \quad = \int _ { - \infty } m ( \tau ) \delta ( t - t _ { 0 } - \tau ) \ d \tau } \\ { \displaystyle \qquad \quad - \infty \qquad } \\ { \displaystyle \qquad = m ( t - t _ { 0 } ) . } \end{array}
$$

We define the Fourier transform of a function, $h ( t )$ ,as

$$
\begin{array} { l } { \displaystyle \mathcal { H } ( f ) = \mathcal { F } [ h ( t ) ] } \\ { \displaystyle \qquad \infty } \\ { \displaystyle \qquad = \int _ { - \infty } ^ { \infty } h ( t ) e ^ { - \imath 2 \pi f t } \ d t , } \\ { \displaystyle \qquad - \infty } \end{array}
$$

and the corresponding inverse Fourier transform as

$$
\begin{array} { c } { h ( t ) = \mathcal { F } ^ { - 1 } [ \mathcal { H } ( f ) ] } \\ { \displaystyle } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ( f ) e ^ { \imath 2 \pi f t } d f , } \end{array}
$$

where $f$ has units of reciprocal time (frequency) and $\imath$ is the square root of $- 1$

The impulse response of a linear system, $g ( t ) = G [ \delta ( t ) ]$ ， is commonly called the time domain response of the system when the independent variable is time. Note, however, that the impulse response concept and Fourier theory are trivially generalizable to functions of space or other variables. The Fourier transform or spectrum of the impulse response, $\mathcal { F } ( g ( t ) )$ , is variously referred to as the frequency response, or transfer function of the system.

The Fourier transform (8.16) provides a formula for evaluating the spectrum. The inverse Fourier transform (8.18) states that the time domain function $g ( t )$ can be exactly reconstructed via a weighted integration of functions of the form $e ^ { \imath 2 \pi f t }$ ，where the weighting is provided by the spectrum $\mathcal G ( f )$ . The essence of Fourier analysis expressed in the transforms (8.16) and (8.18) is that general functions can be expressed and ana-lyzed as a continuous weighted superposition of Fourier basis functions of the form $e ^ { \imath 2 \pi f t }$ . Note that this representation difers from the finite basis function sets considered in Chapter 5 in that the sets of Fourier basis functions in (8.16) and (8.18) are infinite.

Because the Fourier basis functions, $e ^ { \imath 2 \pi f t } = \cos ( 2 \pi f t ) + \imath \sin ( 2 \pi f t )$ , are complex, a general real-valued function $h ( t )$ will have a corresponding spectrum, $\mathcal { H } ( f )$ ， that can be complex valued. $| \mathcal { H } ( f ) |$ is called the spectral amplitude. It is commonly very convenient to express spectra in polar form,

$$
\mathcal { H } ( \boldsymbol { f } ) = | \mathcal { H } ( \boldsymbol { f } ) | e ^ { \imath \theta ( \boldsymbol { f } ) } ,
$$

where the angle that $\mathcal { H } ( f )$ makes in the complex plane,

$$
\theta ( f ) = \tan ^ { - 1 } \left( \frac { \operatorname* { i m a g } ( \mathcal { G } ( f ) ) } { \operatorname { r e a l } ( \mathcal { G } ( f ) ) } \right) ,
$$

is called the spectral phase.

A useful feature of the Fourier transform is that it is length preserving for the 2-norm measure, in the sense that the 2-norm of a function and its Fourier transform are identical. Consider a time domain norm of the form of (5.3) for a general complex function $h ( t )$

$$
\| h ( t ) \| _ { 2 } ^ { 2 } = \intop _ { - \infty } ^ { \infty } h ( t ) h ^ { \ast } ( t ) \ d t .
$$

Expressing $h ( t )$ using the inverse Fourier transform (8.18) and applying complex con-jugation (denoted by an asterisk) gives

$$
\| h ( t ) \| _ { 2 } ^ { 2 } = \int _ { - \infty } ^ { \infty } h ( t ) \left( \int _ { - \infty } ^ { \infty } { \mathcal { H } } ^ { * } ( f ) e ^ { - \imath 2 \pi f t } d f \right) d t .
$$

Interchanging the order of integration and utilizing (8.16), we have

$$
\begin{array} { l } { \displaystyle \| h ( t ) \| _ { 2 } ^ { 2 } = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \left( \int _ { - \infty } ^ { \infty } h ( t ) e ^ { - \imath 2 \pi f _ { l } } \ d t \right) d f } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \mathcal { H } ( f ) \ d f } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \mathcal { H } ( f ) \ d f } \\ { \displaystyle = \| \mathcal { H } ( f ) \| _ { 2 } ^ { 2 } , } \end{array}
$$

whichis the 2-norm ofthe Fourier transform of $h ( t )$ . Equation (8.23) is most commonly referred to as Parseval's theorem.

We have shown in (8.11) that the data produced by a linear time-invariant system for a model, $m ( t )$ , is the convolution of $m ( t )$ with the system impulse response. Evaluating the Fourier transform of this convolution produces an especially important result.

# Theorem 8.2

$$
\mathcal { F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } \left( \intop _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau \right) e ^ { - \imath 2 \pi f t } \ d t .
$$

Reversing the order of integration gives

$$
\mathcal { F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } m ( \tau ) \left( \intop _ { - \infty } ^ { \infty } g ( t - \tau ) e ^ { - \imath 2 \pi f t } \ d t \right) d \tau .
$$

Introducing a change of variables, $\xi = t - \tau$ , we obtain

$$
\begin{array} { l } { { \displaystyle { \mathcal F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } m ( \tau ) \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } g ( \xi ) e ^ { - \imath 2 \pi f ( \xi + \tau ) } \ d \xi } } \\ { { \displaystyle - \infty } } \end{array} \right) d \tau } } \\ { { \displaystyle \qquad = \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } m ( \tau ) e ^ { - \imath 2 \pi f \tau } \ d \tau } } \\ { { \displaystyle - \infty } } \end{array} \right) \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } g ( \xi ) e ^ { - \imath 2 \pi f \xi } \ d \xi } } \\ { { \displaystyle - \infty } } \end{array} \right) } } \\ { { \displaystyle \qquad = { \mathcal M } ( f ) { \mathcal G } ( f ) } . } \end{array}
$$

Equation (8.26),which applies to any pair of functions, is called the convolution theorem. The theorem states that convolution of two functions in the time domain corresponds to the multiplication of their Fourier transforms in the frequency domain. When the two functions are a model, $m ( t )$ , and an impulse response, $g ( t )$ , in a forward problem, (8.26) indicates that the corresponding data spectrum is simply the product of the model and impulse response spectra.

To examine the implications of the convolution theorem more explicitly, consider the data produced by a linear time-invariant system,characterized by the spectrum of the impulse response, $\mathcal G ( f )$ , for a model, $m _ { 0 } ( t )$ ,that is a Fourier basis function of frequency $f _ { 0 }$ ，

$$
m _ { 0 } ( t ) = e ^ { \imath 2 \pi f _ { 0 } t } .
$$

The spectrum of (8.27) is a delta function located at $f = f _ { 0 } , \delta ( f - f _ { 0 } )$ .This can be seen by constructing an inverse Fourier transform (8.18) that invokes the sifting property of the delta function

$$
e ^ { \imath 2 \pi f _ { 0 } } = \int _ { - \infty } ^ { \infty } \delta ( f - f _ { 0 } ) e ^ { \imath 2 \pi f _ { t } } d f .
$$

The spectrum of the corresponding data is thus, by (8.26),a delta function at $f = f _ { \mathrm { 0 } }$ ， scaled by the spectrum of $G ( t )$ ：

$$
\mathcal { F } \left[ G \left[ e ^ { \iota 2 \pi f _ { 0 } t } \right] \right] = \mathcal { F } \left[ \mathcal { G } ( f ) e ^ { \iota 2 \pi f _ { 0 } t } \right] = \delta ( f - f _ { 0 } ) \mathcal { G } ( f _ { 0 } ) .
$$

The corresponding time domain response is, by (8.18),

$$
\begin{array} { r l r } {  { \int _ { - \infty } ^ { \infty } \mathcal { G } ( f _ { 0 } ) \delta ( f - f _ { 0 } ) e ^ { \imath 2 \pi f t } \ d f = \mathcal { G } ( f _ { 0 } ) e ^ { \imath 2 \pi f _ { 0 } t } } } \\ & { } & { = \vert \mathcal { G } ( f _ { 0 } ) \vert e ^ { \imath \theta ( f _ { 0 } ) } e ^ { \imath 2 \pi f _ { 0 } t } } \\ & { } & { = \vert \mathcal { G } ( f _ { 0 } ) \vert e ^ { \imath \theta ( f _ { 0 } ) } m _ { 0 } ( t ) . } \end{array}
$$

Linear time-invariant systems thus transform the Fourier basis functions (8.27) to iden-tical functions,altering only their amplitude and phase by frequency-dependent factors $| \mathcal { G } ( f _ { 0 } ) | e ^ { \imath \theta ( f _ { 0 } ) }$ . Because the system is linear,the transformation for a general input function is just the superposition of all such components at all frequencies,where the appropriate functional weighting is $\mathcal G ( f )$ . Of particular relevance here when considering inverse methods is the result that model basis function amplitudes at frequencies that are weakly mapped to the data (frequencies where $| \mathcal { G } ( f ) |$ is small) in a forward problem, and/or are obscured by noise, may be difficult or impossible to recover in an inverse problem.

The spectrum of the impulse response (transfer function) can be evaluated in a particularly useful analytical manner when we can express the forward problem $d ( t ) = G [ m ( t ) ]$ as a linear differential equation,

$$
\begin{array} { c } { \iota _ { r } m ^ { ( r ) } + a _ { r - 1 } m ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } m ^ { ( 1 ) } + a _ { 0 } m } \\ { = b _ { q } d ^ { ( q ) } + b _ { q - 1 } d ^ { ( q - 1 ) } + \cdot \cdot \cdot + b _ { 1 } d ^ { ( 1 ) } + b _ { 0 } d , } \end{array}
$$

where the superscripts denote the order of time differentiation of $m$ and $d$ ,and the $a _ { i }$ and $b _ { i }$ are constant coefcients.Because each term in (8.31) is linear (there are no powers or other nonlinear functions of $m , d ,$ or their derivatives),and because differentiation is itself a linear operation, (8.31) expresses a linear time-invariant system obeying superposition and scaling.

If (8.31) operates on a model of the form $m ( t ) = e ^ { \imath 2 \pi f t }$ ，(8.30） indicates that the corresponding output will be $d ( t ) = \mathcal { G } ( \ f ) e ^ { \ i 2 \pi f t }$ Substituting this form of $m ( t )$ and differentiating each term,eachtimederivative, $m ^ { ( k ) }$ and $d ^ { ( k ) }$ , will generatecorresponding multipliers $( 2 \pi t f ) ^ { k }$ . Finally, dividing the resulting equation on both sides by $e ^ { \imath 2 \pi f t }$ ,and solving for $\mathcal G ( f )$ gives

$$
\begin{array} { c } { { \displaystyle \mathcal { G } ( f ) = \frac { \mathcal { D } ( f ) } { \mathcal { M } ( f ) } } } \\ { { = \frac { \sum _ { j = 0 } ^ { q } b _ { j } ( 2 \pi \imath f ) ^ { j } } { \sum _ { k = 0 } ^ { r } a _ { k } ( 2 \pi \imath f ) ^ { k } } . } } \end{array}
$$

The transfer function can thus be expressed as a ratio of two complex polynomials in $f$ for any system expressible in the form of (8.31). The $q + 1$ ， generally complex, frequencies $f _ { z }$ , for which the numerator of (8.33) is zero,are referred to as zeros of the transfer function (8.33). The predicted data for the forward problem will thus be zero for inputs of the form $e ^ { \imath 2 \pi f _ { z } t }$ ,regardlessof their amplitude. Any real-valued frequency, $f _ { z } = f _ { 0 }$ , corresponding to the Fourier model basis function $e ^ { \imath 2 \pi f _ { 0 } t }$ will thus lie in the model null space and be unrecoverable by any inverse methodology. The $r + 1$ ， generally complex, frequencies $f _ { p }$ for which the denominator of (8.33) is zero,are called poles of (8.33). The system will be unstable when excited by model basis functions $e ^ { \imath 2 \pi f _ { p } t }$ Along with a scalar gain factor, the transfer function (and hence the response) ofa general linear system that is expressible in the form of (8.31) can be completely characterized by tabulating the poles and zeros,along with a scalar gain factor. This characterization is commonly employed in specifying instrument responses.

# 8.2.LINEAR SYSTEMS IN DISCRETE TIME

To implement Fourier methods numerically,a discrete theory is required with properties that are analogous to the continuous transforms (8.16) and (8.18). This is achieved by the discrete Fourier transform, or DFT. In its most basic formulation, the DFT operates on a uniformly sampled (e.g., space or time) sequence with a specified number of terms $n$ The frequency, $f _ { s }$ , at which sampling occurs is called the sampling rate. The forward discrete Fourier transform of an $n \cdot$ -point sequence, $m _ { j } , j = 0$ ， $1 , \ldots , n - 1$ ,is

$$
\begin{array} { l } { \displaystyle \mathcal { M } _ { k } = ( { \mathrm { D F T } } [ { \mathbf { m } } ] ) _ { k } } \\ { \displaystyle = \sum _ { j = 0 } ^ { n - 1 } m _ { j } e ^ { - \imath 2 \pi j k / n } , } \end{array}
$$