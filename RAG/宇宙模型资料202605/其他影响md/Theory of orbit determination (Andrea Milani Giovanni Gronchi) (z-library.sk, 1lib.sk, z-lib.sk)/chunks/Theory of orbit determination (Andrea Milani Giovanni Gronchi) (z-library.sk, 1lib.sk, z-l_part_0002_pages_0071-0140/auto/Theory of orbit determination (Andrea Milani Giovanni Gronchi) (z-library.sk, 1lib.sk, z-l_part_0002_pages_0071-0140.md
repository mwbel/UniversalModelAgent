# LEAST SQUARES

In this chapter we give the basic formulation of orbit determination as a nonlinear least squares problem. First we introduce the linear least squares problem and the classical iterative methods: Newton’s method and differential corrections. The uncertainty of the result is described by confidence ellipsoids, with the optimization interpretation. We show that the probabilistic interpretation gives strictly analogous results, if the observation error is Gaussian; this assumption is also discussed. This chapter contains mostly classical material: the main reference is (Gauss 1809). Only Section 5.8 contains recent results, based on (Carpino et al. 2003).

# 5.1 Linear least squares

The basic idea of the least squares problem is to fit some model of an unknown function $f ( t )$ of time, given a finite number of observations. The problem is linear if the model can be expressed as a linear combination

$$
f ( t ) = \sum _ { k = 1 } ^ { N } x _ { k } f _ { k } ( t )
$$

of a set of $N$ base functions $f _ { k }$ ; then the coefficients $x _ { k }$ of the linear combinations are the fit parameters. The observational data are the $m \geq N$ pairs $( t _ { i } , \lambda _ { i } ) < i = 1 , m$ : let us introduce the vectors ${ \bf x } = ( x _ { k } ) \in \mathbb { R } ^ { N } , { \bf t } = ( t _ { i } ) , \lambda =$ $( \lambda _ { i } ) \in \mathbb { R } ^ { m }$ . Given the observations, we compute the vector of residuals1 $\pmb { \xi } = ( \xi _ { i } ) \in \mathbb { R } ^ { m }$ ,

$$
\xi _ { i } = \lambda _ { i } - f ( t _ { i } ) = \lambda _ { i } - \sum _ { k = 1 } ^ { N } x _ { k } f _ { k } ( t _ { i } ) = \xi _ { i } ( { \bf x } ) .
$$

1 The minus sign in front of the prediction is an old convention: residual= observed $-$ computed.

The problem is converted to an optimization one by defining a target function which is proportional to the sum of squares of the residuals

$$
Q ( \mathbf { x } ) = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \left[ \lambda _ { i } - \sum _ { k = 1 } ^ { N } x _ { k } f _ { k } ( t _ { i } ) \right] ^ { 2 } .
$$

By using the design matrix

$$
B = \frac { \partial \pmb { \xi } } { \partial \mathbf { x } } = ( b _ { i k } ) , b _ { i k } = - f _ { k } ( t _ { i } ) , i = 1 , m ; k = 1 , N
$$

we have the target function in vector/matrix notation:

$$
\mathbf { \Sigma } ( \mathbf { x } ) = \frac { 1 } { m } \left( \lambda + B \mathbf { x } \right) ^ { T } \left( \lambda + B \mathbf { x } \right) = \frac { 1 } { m } \left[ \lambda ^ { T } \lambda + 2 \lambda ^ { T } B \mathbf { x } + \mathbf { x } ^ { T } B ^ { T } B \mathbf { x } \right] .
$$

The stationary points of the target function are the solutions of

$$
m \ : \frac { \partial Q } { \partial \mathbf { x } } = 2 [ \mathbf { \lambda } ^ { T } \ : B + \mathbf { x } ^ { T } \ : B ^ { T } \ : B ] = \mathbf { 0 }
$$

that is the normal equation $B ^ { T } B \ \mathbf { x } = - B ^ { T } \boldsymbol { \lambda }$ where the normal matrix $C = B ^ { T } B$ is symmetric and defines a non-negative quadratic form. If this quadratic form is positive, the quadratic form $Q ( \mathbf { x } )$ defines level hypersurfaces $m \ Q ( { \bf x } ) = \sigma ^ { 2 }$ in $\mathbb { R } ^ { N }$ which are ellipsoids. The inverse $\Gamma = C ^ { - 1 }$ is the covariance matrix and provides the solution $\mathbf { x } ^ { * } = - \Gamma B ^ { T } \boldsymbol { \lambda }$ . The center of all these ellipsoids is $\mathbf { x } ^ { * }$ , that is

$$
m Q ( { \bf x } ) = m Q ^ { * } + ( { \bf x } - { \bf x } ^ { * } ) ^ { T } C ( { \bf x } - { \bf x } ^ { * } )
$$

where $Q ^ { * } = Q ( \mathbf { x } ^ { * } )$ is the minimum value of the target function; its value can be computed by comparing the expansions of $Q ( \mathbf { x } )$

$$
m Q ^ { * } = \lambda ^ { T } \lambda - \lambda ^ { T } B \Gamma B ^ { T } \lambda \leq \lambda ^ { T } \lambda .
$$

The vector of the residuals after the fit is

$$
\pmb { \xi } = \pmb { \lambda } + B \mathbf { x } ^ { * } = \pmb { \lambda } - B \Gamma B ^ { T } \pmb { \lambda }
$$

and $\mathrm { i s } \neq { \bf 0 }$ , unless $\pmb { \lambda }$ belongs to the subspace spanned by the columns of $B$ .

# Model problem

Let us consider the model problem introduced in Section 2.5, by using the variables $( n , \lambda )$ instead of $( a , \lambda )$ : the general solution is

$$
n ( t ) = n _ { 0 } , \lambda ( t ) = n _ { 0 } t + \lambda _ { 0 }
$$

where $( n _ { 0 } , \lambda _ { 0 } )$ are the initial conditions. The residuals and their partial derivatives are

$$
\xi _ { i } = \lambda _ { i } - n _ { 0 } t _ { i } - \lambda _ { 0 } , i = 1 , m , \frac { \partial \xi } { \partial ( n _ { 0 } , \lambda _ { 0 } ) } = B = [ - \mathbf { t _ { \delta } } - \mathbf { 1 } ]
$$

where the first column is just minus the times, the second one has $- 1$ in all the entries. The normal matrix is

$$
C = B ^ { T } B = \left[ \begin{array} { c c } { \mathbf { t } \cdot \mathbf { t } } & { \mathbf { t } \cdot \mathbf { 1 } } \\ { \mathbf { 1 } \cdot \mathbf { t } } & { \mathbf { 1 } \cdot \mathbf { 1 } } \end{array} \right] = \left[ \begin{array} { c c } { \sum t _ { i } ^ { 2 } } & { \sum t _ { i } } \\ { \sum t _ { i } } & { m } \end{array} \right] .
$$

Assuming as initial conditions $n _ { 0 } = 0 , \lambda _ { 0 } = 0$ , the residuals are the same as the observations and the right-hand side of the normal equation is

$$
D = - B ^ { T } \pmb { \xi } = - B ^ { T } \pmb { \lambda } = \left[ \begin{array} { c } { \sum t _ { i } \lambda _ { i } } \\ { \sum \lambda _ { i } } \end{array} \right] .
$$

By using the definition of mean, variance, and covariance for a finite set

$$
{ \frac { 1 } { m } } \sum _ { i = 1 } ^ { m } t _ { i } , \mathrm { { V a r } } ( \mathbf { t } ) = { \frac { 1 } { m } } \sum _ { i = 1 } ^ { m } \left( t _ { i } - { \bar { t } } \right) ^ { 2 } , \mathrm { { C o v } } ( \mathbf { t } , \lambda ) = { \frac { 1 } { m } } \sum _ { i = 1 } ^ { m } \left( t _ { i } - { \bar { t } } \right) \left( \lambda _ { i } - { \bar { \lambda } } \right)
$$

with $\bar { \lambda }$ the mean of the $\lambda _ { i }$ , and by the identities $\mathbf { t } \cdot \mathbf { t } = m \mathrm { V a r ( \mathbf { t } ) } + m \bar { t } ^ { 2 }$ , $\mathbf { t } \cdot \lambda = m \cos ( \lambda , \mathbf { t } ) + m \bar { t } \overline { { \lambda } }$ , we get

$$
C = m \left[ \begin{array} { c c } { \mathrm { V a r } ( { \bf t } ) + \bar { t } ^ { 2 } } & { \bar { t } } \\ { \bar { t } } & { 1 } \end{array} \right] , ~ D = m \left[ \begin{array} { c } { \mathrm { C o v } ( { \bf t } , { \bf \underline { { \lambda } } } ) + \bar { t } \overline { { \lambda } } } \\ { \overline { { \lambda } } } \end{array} \right] .
$$

If $\operatorname* { d e t } C = m ^ { 2 } \mathrm { V a r } ( \mathbf { t } ) > 0$ then the covariance matrix is

$$
\Gamma = \frac { 1 } { m \mathrm { V a r } ( \mathbf { t } ) } \left[ \begin{array} { c c } { 1 } & { - \bar { t } } \\ { - \bar { t } } & { \mathrm { V a r } ( \mathbf { t } ) + \bar { t } ^ { 2 } } \end{array} \right]
$$

and the solution $( n ^ { * } , \lambda ^ { * } )$ is the regression line, such that

$$
n ^ { * } = \mathrm { C o v } ( { \bf t } , \lambda ) / \mathrm { V a r } ( { \bf t } ) , ~ \lambda ^ { * } = \overline { { \lambda } } - n ^ { * } \overline { { t } } .
$$

The residuals $\pmb { \xi } = \lambda - n ^ { * } \ \mathbf { t } - \lambda ^ { * } \ \mathbf { 1 }$ are such that the mean $\bar { \xi } = 0$ and

$$
\operatorname { V a r } ( \pmb { \xi } ) = Q ^ { * } = \operatorname { V a r } ( \pmb { \lambda } ) - \frac { \operatorname { C o v } ^ { 2 } ( \mathbf { t } , \pmb { \lambda } ) } { \operatorname { V a r } ( \mathbf { t } ) } = \operatorname { V a r } ( \pmb { \lambda } ) \left[ 1 - \operatorname { C o r r } ^ { 2 } ( \mathbf { t } , \pmb { \lambda } ) \right]
$$

where the correlation

$$
\operatorname { C o r r } ( \mathbf { t } , \lambda ) = \frac { \operatorname { C o v } ( \mathbf { t } , \lambda ) } { \sqrt { \operatorname { V a r } ( \mathbf { t } ) \operatorname { V a r } ( \lambda ) } }
$$

is a parameter between $- 1$ and $1$ measuring the decrease in target function with respect to the pre-fit value $Q ( \mathbf { 0 } ) = \mathrm { V a r } ( \lambda )$ .

# 5.2 Nonlinear least squares

The target function of the nonlinear least squares problem

$$
Q ( \mathbf { x } ) = \frac { 1 } { m } \pmb { \xi } ^ { T } ( \mathbf { x } ) \pmb { \xi } ( \mathbf { x } )
$$

is a differentiable function of the fit parameters $\mathbf { x }$ , although it is not just a quadratic function. The partial derivatives of the residuals with respect to the fit parameters are assembled in the arrays

$$
B = \frac { \partial \pmb \xi } { \partial \mathbf { x } } ( \mathbf { x } ) , H = \frac { \partial ^ { 2 } \pmb \xi } { \partial \mathbf { x } ^ { 2 } } ( \mathbf { x } )
$$

where the design matrix $B$ is an $m \times N$ matrix, with $m \geq N$ , and $H$ is a three-index array of shape $m \times N \times N$ . In the context of orbit determination, the partial derivatives of the residuals are the partials of the prediction function (with sign changed). These can be computed by using the chain rule from the partials of the observation function $R$ and the partials of the general solution $\mathbf { y } ( t ) = \mathbf { y } ( \mathbf { y _ { 0 } } , t , \mu , \nu )$ of the equation of motion

$$
\frac { \partial \xi _ { i } } { \partial x _ { k } } = - \frac { \partial R } { \partial \mathbf { y } } \frac { \partial \mathbf { y } ( t _ { i } ) } { \partial x _ { k } } - \frac { \partial R } { \partial x _ { k } }
$$

where the first term is relevant if $x _ { k }$ is a component of the vector $( \mathbf { y _ { 0 } } , \pmb { \mu } )$ (either an initial condition or a dynamical parameter), the second one if $x _ { k }$ is a component of $\pmb { \nu }$ (a kinematical parameter). The formula for $H$ is less simple, containing first and second derivatives of the general solution of the equation of motion.

To find the minimum, we look for stationary points of $Q ( \mathbf { x } )$ :

$$
\frac { \partial Q } { \partial \mathbf { x } } = \frac { 2 } { m } \pmb { \xi } ^ { T } \boldsymbol { B } = \mathbf { 0 } .
$$

Two problems contribute in making this case not as simple as the linear one. First, the equation above is a system of nonlinear equations, and generally does not have an explicit solution. Second, a stationary point does not need to be the absolute minimum point: it could be a saddle, or a local minimum. The first problem can be handled by using some iterative method, such as the Newton method, or some modification of it. The second one requires us to check the Hessian matrix of second derivatives to exclude saddles; the methods to ensure that a local minimum found by some iterative method is the absolute minimum are computationally expensive.

# The Newton method

The standard Newton method involves the computation of the second derivatives of the target function:

$$
\frac { \partial ^ { 2 } Q } { \partial { \bf x } ^ { 2 } } = \frac { 2 } { m } \left( B ^ { T } B + \pmb { \xi } ^ { T } H \right) = \frac { 2 } { m } C _ { n e w }
$$

where $C _ { n e w }$ is an $N \times N$ matrix, non-negative in the neighborhood of a local minimum.2 Given the residuals $\pmb { \xi } ( \mathbf { x } _ { k } )$ obtained from the value $\mathbf { x } _ { k }$ of the parameters at iteration $k$ , the (non-zero) gradient is expanded around $\mathbf { x } _ { k }$

$$
{ \frac { \partial Q } { \partial \mathbf { x } } } ( \mathbf { x } ) = { \frac { \partial Q } { \partial \mathbf { x } } } ( \mathbf { x } _ { k } ) + { \frac { \partial ^ { 2 } Q } { \partial \mathbf { x } ^ { 2 } } } ( \mathbf { x } _ { k } ) \left( \mathbf { x } - \mathbf { x } _ { k } \right) + \cdot \cdot \cdot
$$

where the dots stand for terms of higher order in $\left( \mathbf { x } - \mathbf { x } _ { k } \right)$ . If this gradient has to be zero in $\mathbf { x } = \mathbf { x } ^ { * }$

$$
{ \bf 0 } = \frac { \partial Q } { \partial { \bf x } } ( { \bf x } _ { k } ) + \frac { \partial ^ { 2 } Q } { \partial { \bf x } ^ { 2 } } ( { \bf x } _ { k } ) ( { \bf x } ^ { * } - { \bf x } _ { k } ) + \cdot \cdot \cdot
$$

that is

$$
C _ { n e w } \left( \mathbf { x } ^ { * } - \mathbf { x } _ { k } \right) = - B ^ { T } \pmb { \xi } + \cdot \cdot \cdot
$$

Neglecting the higher order terms, if the matrix $C _ { n e w }$ , as computed at the point $\mathbf { x } _ { k }$ , is invertible then the iteration $k + 1$ of the Newton method provides a correction ${ \bf x } _ { k } \longrightarrow { \bf x } _ { k + 1 }$ with

$$
{ \bf x } _ { k + 1 } = { \bf x } _ { k } + C _ { n e w } ^ { - 1 } D , \quad D = - B ^ { T } \pmb { \xi } ,
$$

where also $D = D ( { \mathbf x } _ { k } )$ . The point $\mathbf { x } _ { k + 1 }$ should be a better approximation to $\mathbf { x } ^ { * }$ than $\mathbf { x } _ { k }$ . In practice, the Newton method may converge or not, depending upon the choice of the first guess $\mathbf { x } _ { \mathrm { 0 } }$ selected to start the iterations.

# Differential corrections

The most used method is a variant of the Newton method, known in this context as differential corrections, with each iteration making the correction

$$
{ \bf x } _ { k + 1 } = { \bf x } _ { k } - ( B ^ { T } \ B ) ^ { - 1 } \ B ^ { T } \boldsymbol \xi
$$

where the normal matrix $C = B ^ { T } \ B$ , computed at $\mathbf { x } _ { k }$ , replaces the matrix $C _ { n e w }$ . This amounts to neglecting, on top of the terms of order $\geq 2$ i n $\left( \mathbf { x } ^ { * } - \mathbf { x } _ { k } \right)$ , also the term $\pmb { \xi } ^ { T } \textbf { \cal H } ( \mathbf x ^ { * } - \mathbf x _ { k } )$ . The additional neglected term is of first order in $\left( \mathbf { x } ^ { * } - \mathbf { x } _ { k } \right)$ but contains also the residuals, thus it is smaller than $C$ $\left( \mathbf { x } ^ { * } - \mathbf { x } _ { k } \right)$ if the residuals are small enough. However, this qualitative argument does not always apply (see Section 10.2).

The main practical motivation for this simplification of the Newton method is that the computation of the three-index arrays of second derivatives $\partial B / \partial { \bf x } = \partial ^ { 2 } \pmb { \xi } / \partial { \bf x } ^ { 2 }$ for $P = p ^ { \prime } + p ^ { \prime \prime }$ dynamical parameters ( $p ^ { \prime }$ initial conditions and $p ^ { \prime \prime }$ parameters to be solved appearing in the equation of motion) requires us to solve $p ^ { \prime } \ P ^ { 2 }$ scalar differential equations on top of the usual $p ^ { \prime } + p ^ { \prime } P$ for the equation of motion and the variational equation.

One iteration of differential corrections is just the solution of a linear least squares problem, with normal equation

$$
C \left( { \bf { x } } _ { k + 1 } - { \bf { x } } _ { k } \right) = D
$$

where the right-hand side $D = - B ^ { T } \xi$ is the same as in the Newton method. This linear problem can be obtained by truncation of the target function

$$
Q ( { \bf x } ) \simeq Q ( { \bf x } _ { k } ) + \frac { 2 } { m } \ : \xi ^ { T } \ : \ : B \left( { \bf x } - { \bf x } _ { k } \right) + \frac { 1 } { m } \ : ( { \bf x } - { \bf x } _ { k } ) ^ { T } \ : C \left( { \bf x } - { \bf x } _ { k } \right) ,
$$

which is not the Taylor expansion to order 2, since $C _ { n e w }$ is replaced by $C$ .

# Convergence and comparison with the linear case

An iteration, that is a differential correction step, is possible if the covariance matrix, the inverse of the normal matrix $\Gamma = C ^ { - 1 }$ , can be computed. Since $C = B ^ { T } B$ , it is always positive semidefinite, and indeed positive definite if $B$ has rank $N$ (this requires $m \geq N$ ). All this applies in exact arithmetic: numerical problems can arise for badly conditioned matrices $C$ and $\Gamma$ . The conditioning number $c o n d ( A )$ , for a symmetric positive definite matrix $A$ , is $_ 3$ the ratio of the largest to the smallest eigenvalue of $A$ .

If $C$ is a badly conditioned matrix, that is its conditioning number is very large, comparable to the inverse of the rounding off, the computation of its inverse may become numerically unstable. There are methods such as the Cholewsky algorithm and the eigenvalues algorithm allowing us to handle badly conditioned cases in a numerically stable way. For a linear least squares fit this is a solution, although also the covariance matrix is badly conditioned (the small eigenvalues of $C$ corresponding to the large eigenvalues of $\Gamma$ ).

In an iterative procedure, to succeed in accurately inverting a badly conditioned normal matrix $C$ is by no means a guarantee of success. If $\Gamma$ has large eigenvalues then one step of differential corrections could apply a large correction $\mathbf { x } _ { k + 1 } - \mathbf { x } _ { k } = \Gamma \ D$ , in particular with large components along the weak direction corresponding to the largest eigenvalue of $\Gamma$ (see Chapter 10). With large corrections the approximations done by truncating the equation $\partial Q / \partial \mathbf { x } = \mathbf { 0 }$ are poor and the value $Q ( \mathbf { x } _ { k + 1 } )$ may fail to decrease with respect to $Q ( \mathbf { x } _ { k } )$ . If the target function begins to increase, often it goes on increasing, then the size of the successive corrections also increases, until physically meaningless values are reached for some of the parameters $\mathbf { x }$ .

In conclusion there are two main differences between solving a linear least squares problem and a nonlinear one. First, the linear problem always has a solution; if the normal matrix is badly conditioned, even with zero eigenvalues, it is always possible to find a solution algorithm.4

Second, the nonlinear problem requires a number of iterations, e.g., of the differential corrections step: experience shows that convergence may fail either catastrophically, by divergence passing from absurd values, or by undamped oscillations, or by correction steps of approximately constant size moving in the same weak direction. Thus we need criteria to terminate the iteration and to proclaim success, that is a good approximation to the convergence which would be achieved only at the limit for $k  + \infty$ . We also need criteria to decide when it is better to give up and to proclaim failure, i.e., when the iterations do not show any tendency to converge.

We can use two criteria to terminate the iterations with an acceptable approximation to $\mathbf { x } ^ { * }$ . One is based on the size of the last correction $\Delta \mathbf { x } =$ ${ \bf x } _ { k + 1 } - { \bf x } _ { k }$ . To decide $\Delta \mathbf { x }$ is small we need a metric in the $N$ -dimensional space of fit parameters. One such metric is defined by the normal matrix

$$
| | \Delta \mathbf { x } | | _ { C } = \sqrt { \Delta \mathbf { x } ^ { T } C \Delta \mathbf { x } / N } ,
$$

with an immediate interpretation either in terms of confidence ellipsoids (see Section 5.4) or probabilistic (see Section 5.7). If $| | \Delta \mathbf { x } | | _ { C } \ll 1$ the following iterations will not provide significant improvements of the solution. The second criterion uses the target function at each iteration $Q _ { k } = Q ( \mathbf { x } _ { k } )$ : if

$$
| Q _ { k + 1 } - Q _ { k } | / Q _ { k + 1 } \ll 1
$$

the change of the last step has not been very useful for the goal of minimizing the target function. However, one iteration with a small relative change in the value of $Q$ is not enough to predict that the value of $Q$ will not change significantly in the following iterations: to terminate the iterations, it is better to require either that there is no significant change in $Q$ for a number (3–5) of iterations, or that $| | \Delta \mathbf { x } | |$ is small.

The criteria to give up orbit determination can be selected depending upon the circumstances. If many orbits have to be computed, and failure in a fraction of them is acceptable, then the iterative procedure could be terminated under weaker conditions, e.g., when either the target function has increased for a number (3–5) of iterations, or the fit parameters $\mathbf { x }$ are outside of some acceptable region. If the orbit determination failure is considered unacceptable, the differential corrections iterations should be continued until either convergence or catastrophic divergence, in which case some other initial guess and/or some other iterative method should be attempted, as discussed in Chapters $7 - 1 0$ .

There are additional problems specific to nonlinear least squares. First, the nominal solutions are in general local minima of the target function and they could be more than one. In some cases there is only one minimum with an acceptable value of $Q ( \mathbf { x } ^ { * } )$ , but it is possible that two local minima have comparable values: see in particular the cases discussed in Chapter 9 and Section 10.2; then both nominal solutions, and the points in their neighborhoods, are possible solutions and neither of them can be discarded arbitrarily.

Second, the differential corrections search for stationary points of $Q ( \mathbf { x } )$ , thus there could be convergence to a saddle point, that is a stationary point in which the Hessian matrix $\partial ^ { 2 } Q / \partial \mathbf { x } ^ { 2 }$ has some negative eigenvalues. From eq. (5.3) we find that negative eigenvalues are due to the $H$ term containing the second derivatives of the residuals, not to the $B ^ { T }$ $B = C$ part, thus the presence of saddles can occur either for comparatively large $\xi$ or when the normal matrix $C$ is badly conditioned. If differential corrections are used, the array $H$ is not computed and the data to decide if the convergence point $\mathbf { x } ^ { * }$ is a saddle rather than a local minimum are not available. There are very few examples documented in the literature of a saddle point in an orbit determination problem (Sansaturio et al. 1996).

# 5.3 Weighting of the residuals

A simple generalization of the least squares problem is the weighted least squares problem, with a non-negative quadratic form as target function:

$$
\mathcal { Q } ( \boldsymbol { \xi } ) = \frac { 1 } { m } \ : \xi ^ { T } \ : W \ : \boldsymbol { \xi } = \frac { 1 } { m } \ : \sum _ { i = 1 } ^ { m } \ : \sum _ { k = 1 } ^ { m } w _ { i k } \ : \xi _ { i } \ : \xi _ { k }
$$

where $W = \left( w _ { i k } \right)$ is the weight matrix, a symmetric matrix with nonnegative eigenvalues. The only change in the formulae established so far is that the normal matrix and the right-hand side of the normal equation

become

$$
C = B ^ { T } W B , ~ D = - B ^ { T } W \xi .
$$

In the simplest case $W = 1 / s ^ { 2 } \ I$ ( $I$ the $m \times m$ identity matrix),

$$
C = \frac { 1 } { s ^ { 2 } } B ^ { T } B , D = - \frac { 1 } { s ^ { 2 } } B ^ { T } \pmb { \xi }
$$

and the parameter $s$ appears through the factor $s ^ { 2 }$ in the covariance matrix $\Gamma = C ^ { - 1 }$ and disappears in the differential correction $\Gamma D$ . That is, a uniform weight does not matter in the solution, although it matters in the uncertainty. A uniform weight is implicitly used anyway, to express the residuals in some appropriate units: e.g., residuals of angular observations could be expressed in arcseconds, of distances in km.

Non-uniform weights express the assumption that different observations are rated to have different accuracy: this changes the nominal solution as well as the covariance matrix. Non-uniform weights can be formally introduced by using a normalization of the residuals. If the weight matrix is diagonal W = diag[s−21 , s−22 , . . . , s−2m ] we can change notation and use ${ \pmb { \xi } } ^ { \prime } = ( { \pmb { \xi } } _ { i } ^ { \prime } )$ for the true residuals, ${ \pmb \xi } = ( \xi _ { i } )$ for the normalized ones:

$$
\pmb { \xi } = \sqrt { W } \ \pmb { \xi } ^ { \prime } , \quad \xi _ { i } = \frac { \xi _ { i } ^ { \prime } } { s _ { i } }
$$

and then $C = B ^ { T } \ B$ and $D = - B ^ { T } \xi$ as in the simple least squares case.

A slightly more complicated case can occur if the observation errors are correlated (see Section 5.8) and the weight matrix $W$ is not diagonal. In this case we cannot abuse the notation $\sqrt { W }$ because there are many possible “matrix square roots” which can be computed with a number of well known algorithms: we shall mention only two of them.

The Cholewsky algorithm is a procedure to find an upper triangular matrix $P$ such that $P ^ { T } P = W$ (Bini et al. 1988, Section 4.17). The eigenvalues algorithm uses a rotation matrix $R$ to diagonalize the matrix $W$ , then computes the square root of the diagonal matrix (that is, the square root of each eigenvalue), and rotates back to the original reference system (Bini et al. 1988, Section 4.15). In this way a matrix $P = R \sqrt { D } R ^ { T }$ is obtained with the property $P ^ { 2 } = W$ (also $P ^ { T } P = W$ because $P$ is symmetric). Both methods are used to solve the normal equation, because they have significant advantages with respect to computing the inverse of the matrix $W$ . With the Cholewsky decomposition the triangular $P$ can be inverted by successive substitutions, then $[ P ^ { I ^ { \prime } } P ] ^ { - 1 } = P ^ { - 1 } [ P ^ { I } ] ^ { - 1 }$ ; in this way badly conditioned matrices can be inverted by an algorithm with denominators of the order of the square root of the conditioning number. With the eigenvalue method, if $R ^ { I } \ W \ R = \mathrm { d i a g } [ \lambda _ { k } ]$ then $W ^ { - 1 } = R$ $\mathrm { d i a g } [ \lambda _ { k } ^ { - 1 } ] R ^ { T }$ . Given a numerically robust method to find the eigenvalues and eigenspaces, this allows us to handle cases with even higher conditioning numbers than Cholewsky.

Having computed such a matrix $P$ we can again change notation, with the normalized residuals $\boldsymbol { \xi }$ obtained from the true residuals ${ \pmb \xi } ^ { \prime }$ by $\pmb { \xi } = P \pmb { \xi } ^ { \prime }$ . The matrix of partial derivatives $B$ of the normalized residuals is obtained from the matrix of partial derivatives $B ^ { \prime }$ of the true residuals

$$
\begin{array} { r c l } { { \displaystyle B } } & { { = } } & { { \displaystyle \frac { \partial \pmb { \xi } } { \partial \mathbf { x } } = \frac { \partial \pmb { \xi } } { \partial \pmb { \xi } ^ { \prime } } \ \frac { \partial \pmb { \xi } ^ { \prime } } { \partial \mathbf { x } } = P \ B ^ { \prime } , } } \\ { { \displaystyle C } } & { { = } } & { { ( B ^ { \prime } ) ^ { T } \ W \ B ^ { \prime } = ( B ^ { \prime } ) ^ { T } \ P ^ { T } \ P \ B ^ { \prime } = B ^ { T } \ B , } } \\ { { \displaystyle D } } & { { = } } & { { \displaystyle - ( B ^ { \prime } ) ^ { T } \ W \ \pmb { \xi } ^ { \prime } = - ( B ^ { \prime } ) ^ { T } \ P ^ { T } \ P \ \pmb { \xi } ^ { \prime } = - B ^ { T } \ \pmb { \xi } } } \end{array}
$$

and the weight matrix again disappears from the normal equation. Thus we may use the formulae in which the weight matrix $W$ does not appear but still assume that the observations have been weighted, either with a diagonal matrix expressing non-uniform individual weights, or possibly with a full matrix $W$ expressing also correlations.

We have assumed the weight matrix $W$ has no negative eigenvalues (otherwise some combination of residuals would give a negative target function, and the existence of a minimum would be doubtful); however, $W$ could have a 0 eigenvalue. This can be used to handle an observation to be discarded, e.g., observation number $i$ is given a weight $w _ { i i } = 0$ ; if the observations are correlated, we also need to set $w _ { i j } = w _ { j i } = 0$ for $j \neq i$ . This is either because they are known a priori to be faulty as a result of some quality control (which precedes their use for orbit determination), or because they are found a posteriori to have residuals too large to be acceptable (see Section 5.8).

# 5.4 Confidence ellipsoids

In a neighborhood of a nominal solution $\mathbf { x } ^ { * }$ , the target function $Q$ has a value somewhat above the minimum $Q ^ { * } = Q ( \mathbf { x } ^ { * } )$ , that is $Q ( \mathbf { x } ) = Q ^ { * } + \Delta Q ( \mathbf { x } )$ ; we call $\Delta Q ( { \bf x } )$ the penalty. By expanding $Q$ around $\mathbf { x } ^ { * }$ , where the gradient $- \pmb { \xi } ^ { T } \pmb { B }$ is zero, the lowest order part of the penalty is a quadratic form in $\Delta \mathbf { x }$ , with $C _ { n e w } ( { \bf x } ^ { * } ) / m$ as coefficient matrix. As shown by eq. (5.3), if $\boldsymbol { \xi }$ is small enough, this quadratic form can be replaced by

$$
\Delta Q ( { \bf x } ) = \frac { 1 } { m } ( { \bf x } - { \bf x } ^ { * } ) ^ { T } { \cal C } ( { \bf x } - { \bf x } ^ { * } ) + \cdots ,
$$

where the dots stand for both terms of degree $\geq 3$ in $\Delta \mathbf { x }$ and for those of degree 2 in $\Delta \mathbf { x }$ containing also $\xi$ .

In Chapter 1 we have defined the confidence region as the set of $\mathbf { x }$ such that the penalty does not exceed a control value. By the expansion above the confidence region can be approximated by a confidence ellipsoid

$$
Z _ { L } ( \sigma ) = \left\{ \mathbf { x } \in \mathbb { R } ^ { N } | ( \mathbf { x } - \mathbf { x } ^ { * } ) ^ { T } C \left( \mathbf { x } - \mathbf { x } ^ { * } \right) \leq \sigma ^ { 2 } \right\}
$$

which is indeed the inside of an $( N - 1 )$ -dimensional ellipsoid if and only if $C$ is positive definite. How do the confidence ellipsoids describe the uncertainty of the parameters $x _ { k } , \ k = 1 , N$ , both one by one and by subsets? (See Section 3.2.) Let us suppose the vector of the parameters to be solved is split into two components, along orthogonal linear subspaces of the parameter space:

$$
\mathbf { x } = \left[ \begin{array} { l } { \mathbf { h } } \\ { \mathbf { g } } \end{array} \right] , \quad \mathbf { x } ^ { * } = \left[ \begin{array} { l } { \mathbf { h } ^ { * } } \\ { \mathbf { g } ^ { * } } \end{array} \right] .
$$

By decomposing the normal and covariance matrices as

$$
C = \left[ \begin{array} { l l } { C _ { \mathbf { h } \mathbf { h } } } & { C _ { \mathbf { h } \mathbf { g } } } \\ { C _ { \mathbf { g } \mathbf { h } } } & { C _ { \mathbf { g } \mathbf { g } } } \end{array} \right] , \quad \Gamma = \left[ \begin{array} { l l } { \Gamma _ { \mathbf { h } \mathbf { h } } } & { \Gamma _ { \mathbf { h } \mathbf { g } } } \\ { \Gamma _ { \mathbf { g } \mathbf { h } } } & { \Gamma _ { \mathbf { g } \mathbf { g } } } \end{array} \right]
$$

the quadratic approximation to the penalty is

$$
\begin{array} { l l l } { { m \displaystyle \Delta Q } } & { { \simeq } } & { { ( { \bf h } - { \bf h } ^ { * } ) \cdot C _ { \bf h \bf h } \left( { \bf h } - { \bf h } ^ { * } \right) } } \\ { { } } & { { } } & { { + 2 ( { \bf h } - { \bf h } ^ { * } ) \cdot C _ { \bf h g } \left( { \bf g } - { \bf g } ^ { * } \right) + ( { \bf g } - { \bf g } ^ { * } ) \cdot C _ { \bf g g } \left( { \bf g } - { \bf g } ^ { * } \right) } . } \end{array}
$$

The uncertainty of the component $\mathbf { g }$ of the solution is expressed by three different formulae, depending upon the assumption we make on the role of the orthogonal $\mathbf { h }$ subspace. In the particular case in which $\mathbf { g }$ has dimension 1 we obtain the uncertainty of one coordinate $x _ { k }$ .

# Conditional ellipsoids for nominal values

Case 1: uncertainty of $\mathbf { g }$ for fixed $\mathbf { h } = \mathbf { h } ^ { * }$ . We have

$$
m \Delta Q \simeq ( { \bf g } - { \bf g } ^ { * } ) \cdot C _ { { \bf g } { \bf g } } ( { \bf g } - { \bf g } ^ { * } )
$$

and the conditional confidence ellipsoid in the $\mathbf { g }$ subspace has matrix $C _ { \mathbf { g } \mathbf { g } }$ , the submatrix of $C$ corresponding to the subspace. $C _ { \mathbf { g } \mathbf { g } }$ is the normal matrix of the fit obtained by selecting $\mathbf { x } = \mathbf { g }$ and moving the $\mathbf { h }$ variables in the consider parameters, left at their nominal value. Note that the covariance matrix $\Gamma _ { \bf g } = C _ { \bf g g } ^ { - 1 }$ of the variables $\mathbf { g }$ considered in isolation does not coincide with the restriction $\Gamma _ { \mathbf { g } \mathbf { g } }$ of the covariance $\Gamma$ , unless $C _ { \mathbf { h g } } = \Gamma _ { \mathbf { h g } } = \mathbf { 0 }$ .

Geometrically this corresponds to the intersection of the confidence ellipsoid with the affine subspace parallel to the linear subspace of the $\mathbf { g }$ variables and passing through $\mathbf { h } ^ { * }$ , see Figure 5.1 and Section 3.3.

![](images/6ae234f6dd1265b9d079836ef0eee7a90c55ffd8a470259cc70f66cd24fb4239.jpg)  
Fig. 5.1. The regression line of $\mathbf { g }$ given $\mathbf { h }$ (dash dot) contains the centers of the $\textbf { h } = \ c o n s t$ sections, in this $N = 2$ case the midpoint of the horizontal intersection segments. The regression line of $\mathbf { h }$ given $\mathbf { g }$ (dotted) contains the midpoints of the vertical intersections segments, including the points of tangency of the ellipse with vertical lines.

# Marginal ellipsoids

Case 2: uncertainty of $\mathbf { g }$ for arbitrary $\mathbf { h }$ . Geometrically we are projecting the confidence ellipsoid onto the $\mathbf { g }$ subspace. To find the boundary of the projection we find the values of $\mathbf { g }$ corresponding to the points on the ellipsoids where the tangent linear space is parallel to the $\mathbf { h }$ subspace:

$$
\frac { \partial } { \partial { \bf h } } \left[ m \Delta Q \right] \simeq 2 ( { \bf h } - { \bf h } ^ { * } ) ^ { T } C _ { { \bf h } { \bf h } } + 2 ( { \bf g } - { \bf g } ^ { * } ) ^ { T } C _ { { \bf g } { \bf h } } = { \bf 0 }
$$

that is, if $C _ { \mathbf { h } \mathbf { h } }$ is invertible, which is the case if $C$ is positive definite,

$$
\mathbf { h } - \mathbf { h } ^ { * } = - C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } C _ { \mathbf { h g } } \left( \mathbf { g } - \mathbf { g } ^ { * } \right) .
$$

This is the parametric equation of the regression subspace of $\mathbf { h }$ given $\mathbf { g }$ , whose intersection with the confidence ellipsoid projects onto the marginal confidence ellipsoid of $\mathbf { g }$ , for arbitrary $\mathbf { h }$ (see Figure 5.1 and Section 3.3). Substituting into the quadratic approximation to $\Delta Q$

$$
m \Delta Q \simeq ( \mathbf { g - g } ^ { * } ) \cdot C ^ { \mathbf { g g } } ( \mathbf { g - g } ^ { * } ) , C ^ { \mathbf { g g } } = C _ { \mathbf { g g } } - C _ { \mathbf { g h } } C _ { \mathbf { h h } } ^ { - 1 } C _ { \mathbf { h g } } .
$$

The marginal confidence ellipsoid in the $\mathbf { g }$ subspace has matrix $C ^ { \mathrm { { g g } } }$ , which is not the corresponding submatrix of $C$ . The minus sign in the above formula, in front of a non-negative quadratic form, implies that the confidence ellipsoid for arbitrary $\mathbf { h }$ contains the ellipsoid of confidence for $\mathbf { h } = \mathbf { h } ^ { * }$ . The definition of $C ^ { \mathrm { { g g } } }$ can be deduced by a purely algebraic approach. We partition the normal system into two equations restricted to the subspaces:

$$
\left\{ \begin{array} { l l } { C _ { \mathbf { h } \mathbf { h } } \Delta \mathbf { h } + C _ { \mathbf { h } \mathbf { g } } \Delta \mathbf { g } = D _ { \mathbf { h } } } \\ { C _ { \mathbf { g } \mathbf { h } } \Delta \mathbf { h } + C _ { \mathbf { g } \mathbf { g } } \Delta \mathbf { g } = D _ { \mathbf { g } } } \end{array} \right.
$$

and then we solve it by eliminating $\Delta \mathbf { h }$ . From the first equation

$$
\Delta \mathbf { h } = C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } \left[ D _ { \mathbf { h } } - C _ { \mathbf { h } \mathbf { g } } \Delta \mathbf { g } \right] ,
$$

by substituting into the other equation, we obtain another linear system

$$
\mathrm { \it C ^ { g g } \Delta \Delta \mathbf { g } = \it D _ { g } - \it C _ { g h } C _ { h h } ^ { - 1 } \it D _ { h } }
$$

with the matrix $C ^ { \mathrm { { g g } } }$ as defined above; if $C ^ { \mathrm { { g g } } }$ is invertible, we have $\Gamma _ { \bf g g } =$ $( C ^ { \mathbf { g } \mathbf { g } } ) ^ { - 1 }$ and the solution, in terms of a partitioned covariance matrix, is

$$
\left\{ \begin{array} { l l } { \Delta \mathbf { g } = \Gamma _ { \mathbf { g } \mathbf { g } } D _ { \mathbf { g } } - \Gamma _ { \mathbf { g } \mathbf { g } } C _ { \mathbf { g } \mathbf { h } } C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } D _ { \mathbf { h } } } \\ { \Delta \mathbf { h } = \Gamma _ { \mathbf { h } \mathbf { h } } D _ { \mathbf { h } } - C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } C _ { \mathbf { h } \mathbf { g } } \Gamma _ { \mathbf { g } \mathbf { g } } D _ { \mathbf { g } } } \end{array} \right.
$$

where $\Gamma _ { \mathbf { h } \mathbf { h } } = C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } + C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } C _ { \mathbf { h } \mathbf { g } } \Gamma _ { \mathbf { g } \mathbf { g } } C _ { \mathbf { g } \mathbf { h } } C _ { \mathbf { h } \mathbf { h } } ^ { - 1 }$ . This solution by substitution is possible only if $C _ { \mathbf { h } \mathbf { h } }$ and $C ^ { \mathrm { { g g } } }$ are invertible; it is not required that $C _ { \mathbf { g } \mathbf { g } }$ be invertible. In this hypothesis, it is possible to describe the matrix of the confidence ellipsoid in the $\mathbf { g }$ space for arbitrary $\mathbf { h }$ in terms of the covariance matrix $C ^ { \bf g g } = \Gamma _ { \bf g g } ^ { - 1 }$ Γ−gg , where $\Gamma _ { \mathbf { g } \mathbf { g } }$ is the restriction of $\Gamma$ to the subspace. This has a probabilistic interpretation in terms of marginal probability distribution, see Section 3.2. By exchanging the role of $\mathbf { h }$ and $\mathbf { g }$ we obtain

$$
C ^ { \mathbf { h } \mathbf { h } } = C _ { \mathbf { h } \mathbf { h } } - C _ { \mathbf { h } \mathbf { g } } \ C _ { \mathbf { g } \mathbf { g } } ^ { - 1 } \ C _ { \mathbf { g } \mathbf { h } }
$$

and if it is invertible the inverse is $\Gamma _ { \mathbf { h } \mathbf { h } }$ , the restriction of the covariance matrix to the $\mathbf { h }$ subspace. This provides a complete solution computable for $C _ { \mathbf { g } \mathbf { g } }$ and $C ^ { \mathbf { h h } }$ invertible, but not requiring $C _ { \mathbf { h } \mathbf { h } }$ to be invertible. The choice of the matrices to be inverted can become important for numerical stability reasons when $C$ and $\Gamma$ are badly conditioned matrices.

# Conditional ellipsoids for non-nominal values

Case 3: uncertainty of $\mathbf { g }$ for fixed $\mathbf { h } = \mathbf { h } _ { 0 } \neq \mathbf { h } ^ { * }$ . The approximation is

$$
\begin{array} { l l l } { { m \Delta Q } } & { { \simeq } } & { { ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) \cdot C _ { \bf h h } \left( { \bf h } _ { 0 } - { \bf h } ^ { * } \right) } } \\ { { } } & { { } } & { { + 2 ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) \cdot C _ { \bf h g } \left( { \bf g } - { \bf g } ^ { * } \right) + ( { \bf g } - { \bf g } ^ { * } ) \cdot C _ { \bf g g } \left( { \bf g } - { \bf g } ^ { * } \right) , } } \end{array}
$$

and the minimum with respect to $\mathbf { g }$ is a solution of

$$
\frac { \partial } { \partial { \bf g } } \left[ m \Delta Q \right] = 2 ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) ^ { T } C _ { { \bf h g } } + 2 ( { \bf g } - { \bf g } ^ { * } ) ^ { T } C _ { { \bf g } { \bf g } } = { \bf 0 } .
$$

Provided $C _ { \mathbf { g } \mathbf { g } }$ is invertible, the minimum point for fixed $\mathbf { h } = \mathbf { h } _ { 0 }$ is

$$
{ \bf g } _ { 0 } = { \bf g } ^ { * } - C _ { { \bf g } { \bf g } } ^ { - 1 } C _ { { \bf g } { \bf h } } \left( { \bf h } _ { 0 } - { \bf h } ^ { * } \right)
$$

which is the regression subspace of ${ \bf g } _ { 0 }$ given $\mathbf { h } _ { 0 }$ . ${ \bf g } _ { 0 }$ is in general different from $\mathbf { g } ^ { * }$ , unless the subspaces are uncorrelated, that is unless $C _ { \mathbf { g h } }$ is a zero matrix. We can now compute the penalty $\Delta Q$ as a function of the displacement ${ \bf g } - { \bf g } _ { 0 }$ with respect to this minimum: upon substitution of

$$
\begin{array} { r l r } & { } & { { \bf g } - { \bf g } ^ { * } = ( { \bf g } - { \bf g } _ { 0 } ) + ( { \bf g } _ { 0 } - { \bf g } ^ { * } ) = ( { \bf g } - { \bf g } _ { 0 } ) - C _ { \bf g g } ^ { - 1 } C _ { \bf g h } ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) , } \\ & { } & \\ & { } & { m \Delta Q \simeq ( { \bf g } - { \bf g } _ { 0 } ) \cdot C _ { \bf g g } ( { \bf g } - { \bf g } _ { 0 } ) + ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) \cdot C ^ { \bf h h } ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) . } \end{array}
$$

This means that the constraint $\mathbf { h } = \mathbf { h } _ { 0 }$ implies a minimum penalty

$$
m ~ \Delta Q _ { \mathbf { h } } = ( \mathbf { h } _ { 0 } - \mathbf { h } ^ { * } ) \cdot C ^ { \mathbf { h h } } \left( \mathbf { h } _ { 0 } - \mathbf { h } ^ { * } \right)
$$

which is a quadratic form in the difference $\mathbf { h } _ { 0 } - \mathbf { h } ^ { * }$ with matrix $C ^ { \mathbf { h } \mathbf { h } } = \Gamma _ { \mathbf { h } \mathbf { h } } ^ { - 1 }$ The quadratic form expressing the supplementary penalty, for moving $\mathbf { g }$ from the constrained minimum $\mathbf { g } _ { 0 }$ , has matrix $C _ { \mathbf { g } \mathbf { g } }$ as in the $\mathbf { h } = \mathbf { h } ^ { * }$ case, but the conditional confidence ellipsoid in the $\mathbf { g }$ space is smaller because

$$
\Delta Q \simeq \sigma ^ { 2 } \Leftrightarrow ( { \bf g } - { \bf g } _ { 0 } ) \cdot C _ { \mathrm { g g } } ( { \bf g } - { \bf g } _ { 0 } ) = \sigma ^ { 2 } - ( { \bf h } _ { 0 } - { \bf h } ^ { * } ) \cdot C ^ { \bf h h } ( { \bf h } _ { 0 } - { \bf h } ^ { * } )
$$

and the last term to be subtracted is positive (for $\mathbf { h } _ { 0 } \neq \mathbf { h } ^ { * }$ ) when $C ^ { \mathbf { h h } }$ is positive definite, that is when $C$ and $\Gamma$ are positive definite. This has a probabilistic interpretation in terms of the conditional probability distribution.

# 5.5 Propagation of covariance

Let y represent the state vector at some time $t$ , the solution of the equation of motion. The differential of the integral flow $\Phi _ { t _ { 0 } } ^ { t } ( \mathbf { y _ { 0 } } )$ , where $\mathbf { y _ { 0 } } = \mathbf { y } ( t _ { 0 } )$ , is expressed by a matrix of partial derivatives, the state transition matrix

$$
\frac { \partial \mathbf { y } ( t ) } { \partial \mathbf { y _ { 0 } } } = D \Phi _ { t _ { 0 } } ^ { t _ { 1 } } ( \mathbf { y _ { 0 } } )
$$

which is in turn the solution of the variational equation, a system of linear ordinary differential equations. The variational equation has a solution

which can be computed numerically, simultaneously with the solution of the equation of motion. We shall use the semigroup property

$$
\Phi _ { t } ^ { t _ { 0 } } \left( \Phi _ { t _ { 0 } } ^ { t } ( \mathbf { y _ { 0 } } ) \right) = \Phi _ { t _ { 0 } } ^ { t _ { 0 } } ( \mathbf { y _ { 0 } } ) = \mathbf { y _ { 0 } } , \frac { \partial \mathbf { y } } { \partial \mathbf { y _ { 0 } } } \frac { \partial \mathbf { y _ { 0 } } } { \partial \mathbf { y } } = I .
$$

Let us first assume that the vector of fit variables $\mathbf { x }$ coincides with $\mathbf { y _ { 0 } }$ . By the use of the state transition matrix, the normal and covariance matrices for $\mathbf { y _ { 0 } }$ can be propagated from time $t _ { 0 }$ to an arbitrary time $t$ . We shall indicate with subscript 0 the quantities referring to the epoch $t _ { 0 }$ , with subscript $t$ the quantities for epoch $t$ ; for the normal matrix

$$
C _ { 0 } = \frac { \partial \pmb { \xi } ^ { T } } { \partial \mathbf { y _ { 0 } } } ^ { \frac { \partial \pmb { \xi } } { \partial \mathbf { \xi } } } \frac { \partial \pmb { \xi } } { \partial \mathbf { y _ { 0 } } }
$$

the propagation to time $t$ is obtained by assuming the fit variables are $\mathbf { y } ( t )$ , then by applying to the Jacobian matrix the chain rule

$$
\begin{array} { r c l } { { C _ { t } } } & { { = } } &  { \displaystyle {  { \frac { \partial { \pmb { \xi } } } { \partial { \bf y } } } ^ { T } \frac { \partial { \pmb { \xi } } } { \partial { \bf y } } = ( \frac { \partial \pmb { \xi } } { \partial { \bf y _ { 0 } } } \frac { \partial { \bf y _ { 0 } } } { \partial { \bf y } } ) ^ { T } ( \frac { \partial \pmb { \xi } } { \partial { \bf y _ { 0 } } } \frac { \partial { \bf y _ { 0 } } } { \partial { \bf y } } ) } } \\ { { } } & { { = } } &  { \displaystyle {  \frac { \partial { \bf y _ { 0 } } } { \partial { \bf y } } ^ { T } C _ { 0 } \frac { \partial { \bf y _ { 0 } } } { \partial { \bf y } } = ( \frac { \partial { \bf y } } { \partial { \bf y _ { 0 } } } ^ { T } ) ^ { - 1 } C _ { 0 } ( \frac { \partial { \bf y } } { \partial { \bf y _ { 0 } } } ) ^ { - 1 } . } } \end{array}
$$

The covariance matrices are the inverse of the normal matrices, thus

$$
\Gamma _ { 0 } = C _ { 0 } ^ { - 1 } , ~ \Gamma _ { t } = C _ { t } ^ { - 1 } = \frac { \partial \mathbf { y } } { \partial \mathbf { y _ { 0 } } } \Gamma _ { 0 } \frac { \partial \mathbf { y } } { \partial \mathbf { y _ { 0 } } } ^ { T } ,
$$

giving the covariance propagation formula, corresponding to eq. (3.9). In conclusion to propagate the normal and covariance matrix, and to compute the confidence ellipsoid for another epoch, it is not necessary to solve again the least square problem, but only to solve the variational equation. However, as we can see already in our model problem, the assumption of linearity is often questionable for this step of the computation.

If the fit parameters $\mathbf { x }$ include, besides $\mathbf { y _ { 0 } }$ , some of the constants $\mu , \nu$ , then the state transition matrix for $\mathbf { x }$ is of the form

$$
\frac { \partial \mathbf { x } ( t ) } { \partial \mathbf { x } ( t _ { 0 } ) } = \left[ \begin{array} { c c } { \partial \mathbf { y } ( t ) / \partial \mathbf { y _ { 0 } } } & { 0 } \\ { 0 } & { I } \end{array} \right]
$$

and the propagation formulae can be used in exactly the same way.

# Sources of nonlinearity

The problem of nonlinearity arises from two phenomena. First, the linear approximation may result in normal and covariance matrices with a large conditioning number. Then the confidence ellipsoids have a very elongated shape: if $\lambda _ { j }$ , $j = 1 , N$ , are the eigenvalues of the propagated normal matrix $C _ { t }$ , the lengths of the semiaxes of the confidence ellipsoid are $\sigma _ { j } = 1 / \sqrt { \lambda _ { j } }$ , and the ratio of the longest to the shortest is $\sqrt { \mathrm { c o n d } ( C ) }$ . Ratios such as $1 0 ^ { 5 } \simeq 1 0 ^ { 6 }$ are often found, thus the distance of points in the confidence ellipsoid from the nominal solution can become large. Second, the quadratic approximation can fail when it is used to describe a large region in the parameter space: that is, the confidence region is significantly different from the confidence ellipsoid. The two phenomena act together: nonlinearity is important when the longest axis of the ellipsoid is too long.

Both the wild increase in the size of the longest semiaxis, and the dominance of the nonlinear effects, can occur in each of the two steps in the computation of the propagated confidence region. The first step is the computation of the confidence region for the fit parameters $\mathbf { x }$ at epoch $t _ { 0 }$ , supposedly near to the center of the observations time span. Still, when the observational data are inadequate the normal matrix $C _ { 0 }$ (for epoch $t _ { 0 }$ ) is badly conditioned.

The second step is the propagation of the uncertainty to the time $t _ { 1 }$ . The integral flow $\Phi _ { t _ { 0 } } ^ { t _ { 1 } }$ is nonlinear, and its derivative, the state transition matrix, has some coefficients growing at least linearly with time. Then the propagation of the normal and covariance matrices, eq. (5.4) and (5.5), results in conditioning numbers increasing at least quadratically with time. In a chaotic dynamics, that is with positive Lyapounov exponents, some coefficients of the state transition matrix grow exponentially with time and the effects described above are enormously enhanced. This is the case for an asteroid on a planet-crossing orbit, see Chapter 12.

# 5.6 Model problem

Let us use as an example the model problem, discussed in Section 5.1, in the nonlinear formulation with variables $( a , \lambda )$ . The general solution is

$$
a ( t ) = a _ { 0 } , \lambda ( t ) = n ( a _ { 0 } ) t + \lambda _ { 0 }
$$

with $n ( a )$ a monotonically decreasing and convex function defined for $a > 0$

$$
n ( a ) = \frac { k } { a ^ { 3 / 2 } } , ~ \frac { d n } { d a } = - \frac { 3 } { 2 } ~ \frac { n } { a } < 0 , ~ \frac { d ^ { 2 } n } { d a ^ { 2 } } = \frac { 1 5 } { 4 } ~ \frac { n } { a ^ { 2 } } > 0 .
$$

The partial derivatives and the design matrix are

$$
\frac { \partial \xi _ { i } } { \partial a _ { 0 } } = \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } t _ { i } , \quad \frac { \partial \xi _ { i } } { \partial \lambda _ { 0 } } = - 1 , \quad B = \left[ \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } \mathbf { t _ { \nabla } } - \mathbf { 1 } \right] ,
$$

where $n _ { 0 } = n ( a _ { 0 } )$ . Let us select a suitable origin of time in such a way that $\bar { t } = 0$ , then $\sum t _ { i } ^ { 2 } = m \mathrm { V a r } ( \mathbf { t } )$ and $\sum t _ { i } \lambda _ { i } = m \mathrm { C o v } ( \mathbf { t } , \pmb { \lambda } )$ , thus by eq. (5.2)

$$
C = B ^ { T } B = m \left[ \begin{array} { c c } { { ( 9 n _ { 0 } ^ { 2 } / 4 a _ { 0 } ^ { 2 } ) \mathrm { V a r } ( { \bf t } ) } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right] .
$$

We have to start from a first guess $a ~ = ~ a _ { 0 }$ , $\lambda \ : = \ : \lambda _ { 0 }$ with $a _ { 0 } ~ > ~ 0$ and $n _ { 0 } = n ( a _ { 0 } ) > 0$ : the residuals are $\pmb { \xi } = \lambda - n _ { 0 } \textnormal { \bf t } - \lambda _ { 0 } \textnormal { \bf 1 }$ and taking into account $\mathbf { t } \cdot \pmb { \xi } = \mathbf { t } \cdot \pmb { \lambda } - n _ { 0 } \mathbf { t } \cdot \mathbf { t }$ the right-hand side of the normal equation is

$$
D = - B ^ { T } \xi = m \left[ \begin{array} { c } { { - \big ( 3 n _ { 0 } / 2 a _ { 0 } \big ) \big ( \mathrm { C o v } \big ( \mathbf { t } , \lambda \big ) - n _ { 0 } \mathrm { V a r } ( \mathbf { t } ) \big ) } } \\ { { \overline { { \lambda } } - \lambda _ { 0 } } } \end{array} \right] .
$$

The first differential correction, starting from the first guess $( a _ { 0 } , \lambda _ { 0 } )$ , is

$$
a _ { 1 } = a _ { 0 } - \frac { 2 } { 3 } \frac { a _ { 0 } } { n _ { 0 } } \left[ n _ { 0 } - \frac { \mathrm { C o v } ( \mathbf { t } , \lambda ) } { \mathrm { V a r } ( \mathbf { t } ) } \right] , \lambda _ { 1 } = \lambda _ { 0 } + ( \overline { { \lambda } } - \lambda _ { 0 } ) ;
$$

this first iteration needs to be compared with the results of the linear fit in the $( n , \lambda )$ variables, which was $n ^ { * } = \mathrm { C o v } ( \mathbf { t } , \pmb { \lambda } ) / \mathrm { V a r } ( \mathbf { t } )$ , $\lambda ^ { * } = \bar { \lambda }$ . Thus the first iteration corrects $\lambda$ at once to the right value, which is preserved in the following iterations. The correction to $a$ can be interpreted as

$$
a _ { 1 } = a _ { 0 } - \frac { n ( a _ { 0 } ) - n ^ { * } } { d n / d a } ,
$$

i.e., one step of the Newton method to solve the equation $n ( a ) - n ^ { * } = 0$ with first guess $a = a _ { 0 }$ . In this simple case we can find whether the iterative differential corrections are convergent. If $a _ { 1 } = [ \left( 5 / 2 \right) n _ { 0 } - n ^ { * } ] / ( 3 n _ { 0 } / 2 a _ { 0 } )$ i s negative the second iteration is impossible: this occurs for $a _ { 0 } > ( 5 / 2 ) ^ { 2 / 3 } a ^ { * } \simeq$ $1 . 8 4 \ a ^ { * }$ , where $a ^ { * }$ is the value such that $n ( a ^ { * } ) = n ^ { * }$ . Else, if $a _ { 0 } < a ^ { * }$ the iterations take place where the convex decreasing function $n ( a )$ has a value larger than $n ^ { * }$ , and convergence is guaranteed. Else, if $( 5 / 2 ) ^ { 2 / 3 } a ^ { * } > a _ { 0 } >$ $a ^ { * }$ we have $0 < a _ { 1 } < a ^ { * }$ and the following iterations are in the region of guaranteed convergence. We can conclude that the differential corrections are convergent for $0 < a _ { 0 } < ( 5 / 2 ) ^ { 2 / 3 } a ^ { * }$ , whatever $\lambda _ { 0 }$ .

We can see the effect of the nonlinearity also in the propagated confidence region (Figure 5.2). The propagation of the normal matrix $C _ { 0 }$ to $C _ { t }$ at time $t$ by eq. (5.4) uses the inverse of the state transition matrix

$$
\begin{array} { r l r } { \frac { \partial ( a , \lambda ) } { \partial ( a _ { 0 } , \lambda _ { 0 } ) } } & { = } & { \left[ \begin{array} { c c } { 1 } & { 0 } \\ { - ( 3 n _ { 0 } / 2 a _ { 0 } ) t } & { 1 } \end{array} \right] , \frac { \partial ( a _ { 0 } , \lambda _ { 0 } ) } { \partial ( a , \lambda ) } = \left[ \begin{array} { c c } { 1 } & { 0 } \\ { ( 3 n _ { 0 } / 2 a _ { 0 } ) t } & { 1 } \end{array} \right] , } \end{array}
$$

![](images/1a7013dc3671130f757c34abc86ac4ac011fd0ff033d5c872423f32dcfa27259.jpg)  
Fig. 5.2. Semilinear prediction compared with linear confidence ellipse for the model problem.

$$
{ \cal C } _ { t } = m \left[ \begin{array} { c c } { { ( 9 n _ { 0 } ^ { 2 } / 4 a _ { 0 } ^ { 2 } ) ( \mathrm { V a r } ( t ) + t ^ { 2 } ) } } & { { ( 3 n _ { 0 } / 2 a _ { 0 } ) t } } \\ { { ( 3 n _ { 0 } / 2 a _ { 0 } ) t } } & { { 1 } } \end{array} \right]
$$

which is the same as the normal matrix computed for time $t = 0$ when the average time is $\bar { t } = - t$ . Thus it is no longer diagonal, but the determinant is still the same: that is, the propagated confidence ellipse has the same area, but it is skewed along the $\lambda$ axis, and the ratio of the major semiaxis to the minor semiaxis increases. The image, by the full nonlinear integral flow, of the confidence ellipses for $a _ { 0 } , \lambda _ { 0 }$ , that is of the ellipses defined by $C _ { 0 }$ , becomes increasingly banana shaped as the time $t$ increases in absolute value (Figure 5.2). For large $t$ such a semilinear prediction can become strongly incompatible with the linear one, see Section 7.4.

# Observations of angle variables

The model problem can be made more realistic if we consider that $\lambda$ is an angle variable, that is defined mod $2 \pi$ . Indeed, when the satellite is observed at longitude $\lambda _ { i }$ at time $t _ { i }$ for $i = 1 , 2$ the observations do not contain the information about whether the orbital arc covered in the interval $[ t _ { 1 } , t _ { 2 } ]$ has been $\lambda _ { 2 } - \lambda _ { 1 }$ rather than $\lambda _ { 2 } - \lambda _ { 1 } + 2 p \pi$ , with $p$ integer.

As a simple example let us assume the $m = 2 h + 1$ observations are at constant time intervals of length $\Delta t$ , with $\bar { t } = 0$ , that is $t _ { i } = ( i - h - 1 ) \Delta t$ ; let the best fit mean motion be $n ^ { * }$ . Then $\lambda _ { i + 1 } - \lambda _ { i } \simeq n ^ { * } \Delta t$ if the satellite has done less than one revolution; but of course also $\lambda _ { i + 1 } - \lambda _ { i } \simeq n ^ { * } \Delta t + 2 \pi p$ for $p \in \mathbb Z$ provides a good fit, thus an alternative nominal solution with

$$
n _ { p } ^ { * } \simeq \frac { n ^ { * } \Delta t + 2 \pi p } { \Delta t } = n ^ { * } + \frac { 2 \pi } { \Delta t } p .
$$

There is no way to decide among these alternative solutions until a new observation, at time $t ^ { + }$ with $t ^ { + } / \Delta t$ not an integer, is available. In a simple numerical test, it is easy to get convergence to a value $a _ { 1 } ^ { * }$ , with $n ( a _ { 1 } ^ { * } ) \simeq n _ { 1 } ^ { * }$ . Then for a time not an integer multiple $\Delta t$ the predictions are completely off, which could result in a failed recovery.

This change in the topology of the problem, with multiple minima of the target function if the observable is an angle variable, is because the residuals are not $\lambda _ { i } - \lambda ( t _ { i } )$ but $\xi _ { i } = [ \lambda _ { i } - \lambda ( t _ { i } , a _ { 0 } , \lambda _ { 0 } ) + \pi ] \bmod ( 2 \pi ) - \pi$ where the shift by $\pi$ before reducing to the principal value has the purpose of ensuring that the function $\mathcal { Q }$ is smooth at $\xi _ { i } = 0$ ; however, it is not differentiable at $\xi _ { i } = \pi$ . Thus the target function $Q ( { a } _ { 0 } , \lambda _ { 0 } )$ is not differentiable everywhere, and separate minima can be found in each domain of differentiability. If differential corrections are started with a first guess far from the true solution, the Newton method on $a _ { 0 }$ can lead to the spurious values $a _ { p } ^ { * }$ (corresponding to $n _ { p } ^ { * }$ with $p = 1 , 2 , \ldots$ ). As we will see in Section 7.4, selecting an integer number of revolutions is a critical step of the identification problem.

# 5.7 Probabilistic interpretation

The probabilistic interpretation uses as source random variables the residuals themselves: the simplest assumption is that, after the best possible value has been found for the fit parameters $\mathbf { x }$ , each residual $\xi _ { i }$ is a continuous random variable $\Xi _ { i }$ with zero mean and unit variance (in some appropriate unit), independent of the index $i$ . It is also assumed that the error of each observation is a random variable independent (see Section 3.1) of those of the other observations. Under the additional hypothesis that the joint probability density is rotation invariant, thus it is a function depending only upon the target function, the only possible probability density is the Gaussian one $\mathsf { p } _ { \Xi i } ( \xi ) = N ( 0 , 1 ) ( \xi )$ (see Section 3.2). Then the residuals random vector $\boldsymbol { \xi }$ has probability density $\mathfrak { p } \equiv ( \pmb { \xi } ) = N ( \mathbf { 0 } , I ) ( \pmb { \xi } )$ , with $I$ the $m \times m$ identity matrix. Under these conditions the solution for the fit parameters $\mathbf { x }$ can be seen as a set of jointly distributed random variables $\mathbf { X }$ : the goal is to compute the probability density $\mathsf { p } \mathbf { x } ( \mathbf { x } )$ , given the probability density $\mathsf { p } \equiv ( \pmb { \xi } )$ . The residuals are a function of the fit parameters

$$
G : \mathbb { R } ^ { N } \longrightarrow \mathbb { R } ^ { m } , \quad \pmb { \xi } = G ( \mathbf { x } )
$$

obtained by subtracting from the observations the prediction function. Let $\mathbf { x } ^ { * }$ be the nominal solution and $\pmb { \xi } ^ { * } = G ( \mathbf { x } ^ { * } )$ the corresponding residuals. $G$ is a differentiable function, thus we can linearize at the nominal solution

$$
\pmb { \xi } - \pmb { \xi } ^ { * } = B ( \mathbf { x } ^ { * } ) ( \mathbf { x } - \mathbf { x } ^ { * } ) + \cdot \cdot \cdot
$$

where $B ( \mathbf { x } ^ { * } )$ is the design matrix, computed at convergence, and the dots stand for terms of order higher than $1$ in $\left| \mathbf { x } - \mathbf { x } ^ { * } \right|$ . The image of the fit parameters space $V = G ( \mathbb { R } ^ { N } )$ is an $N$ -dimensional submanifold of the residuals space $\mathbb { R } ^ { m }$ . This manifold can have singularities, but the point $\xi ^ { * }$ cannot be singular, because the matrix $B ( \mathbf { x } ^ { * } )$ has rank $N$ , otherwise differential corrections would fail and the nominal solution $\mathbf { x } ^ { * }$ could not be reached. Thus we can assume that the manifold $V$ is smooth, at least in a neighborhood of $\xi ^ { * }$ . We need to compute the conditional density function of $\Xi$ on $V$ , as a step to compute the probability density of $\mathbf { X }$ on $\mathbb { R } ^ { N }$ .

If we can neglect the higher order terms we can write a linearized equation

$$
\Delta \pmb { \xi } = B ( \mathbf { x } ^ { * } ) \Delta \mathbf { x } , \Delta \pmb { \xi } = \pmb { \xi } - \pmb { \xi } ^ { * } , \Delta \mathbf { x } = \mathbf { x } - \mathbf { x } ^ { * } ,
$$

which is the tangent map between $\mathbb { R } ^ { N }$ and the linear $N$ -plane $T V ( \pmb { \xi } ^ { * } )$ tangent to $V$ at the point $\xi ^ { * }$ . To use this linearization is the same as considering the linear least squares problem with quadratic target function

$$
Q ( { \bf x } ) = Q ^ { * } + \frac { 1 } { m } ( { \bf x } - { \bf x } ^ { * } ) ^ { T } C ( { \bf x } - { \bf x } ^ { * } )
$$

neglecting all higher order terms. Note that by using $C$ instead of $C _ { n e w }$ we are neglecting the $\pmb { \xi } ^ { T } \pmb { H }$ term in eq. (5.3).

By using a rotation $R$ in the residuals space as in eq. (3.11), that is with coordinates $( \xi ^ { \prime } , \xi ^ { \prime \prime } )$ such that $\pmb { \xi } ^ { \prime \prime }$ parameterizes $T V ( \xi ^ { * } )$ , the conditional probability density of $\Xi$ on $T V ( \xi ^ { * } )$ is Gaussian with the $N \times N$ identity matrix as covariance $\mathsf { p } _ { \Xi ^ { \prime \prime } } = N ( \mathbf { 0 } , I )$ . In these coordinates the linearized map $B ( \mathbf { x } ^ { * } )$ has a simpler structure, since the ${ \pmb \xi } ^ { \prime }$ component of the image is $\mathbf { 0 }$ :

$$
R B ( \mathbf { x } ^ { * } ) = { \left[ \begin{array} { l } { \mathbf { 0 } } \\ { A } \end{array} \right] }
$$

with $A = A ( \mathbf { x } ^ { * } )$ an invertible $N \times N$ matrix. Then the normal matrix

$C = C ( \mathbf { x } ^ { * } )$ i s

$$
\begin{array} { r } { C = B ^ { T } B = B ^ { T } R ^ { T } R B = A ^ { T } A . } \end{array}
$$

The inverse transformation from $T V ( \xi ^ { * } )$ to $\mathbb { R } ^ { N }$ is given by the matrix $A ^ { - 1 }$ : by the Gaussian transformation formula (3.9) the probability density of $\mathbf { X }$

$$
\mathsf { p } _ { \mathbf { X } } ( \mathbf { x } ) = N \left( \mathbf { x } ^ { * } , A ^ { - 1 } \ I \ [ A ^ { - 1 } ] ^ { T } \right)
$$

is Gaussian with covariance matrix

$$
\Gamma = A ^ { - 1 } [ A ^ { - 1 } ] ^ { T } = [ A ^ { T } A ] ^ { - 1 } = [ B ^ { T } B ] ^ { - 1 } = C ^ { - 1 } .
$$

This is the fundamental result obtained by Gauss (1809): the solution of a linear least squares problem has a Gaussian probability density, with mean equal to the nominal solution and covariance matrix equal to the inverse of the normal matrix. $\Gamma = C ^ { - 1 }$ is the matrix solving the normal equation, thus connecting the probabilistic interpretation, the differential corrections “last step”, and the optimization interpretation.

Additional connections between the two interpretations can be found by reviewing the results of Section 5.4 taking into account the probabilistic interpretation. The Gaussian probability density of the solution is

$$
\mathsf { p } _ { \mathbf { X } } ( \mathbf { x } ) = \frac { \sqrt { \operatorname* { d e t } C } } { ( 2 \pi ) ^ { N / 2 } } \ \exp \left[ - \frac { 1 } { 2 } ( \mathbf { x } - \mathbf { x } ^ { * } ) ^ { T } C \left( \mathbf { x } - \mathbf { x } ^ { * } \right) \right] .
$$

Then the probability density contains $\mathbf { x }$ only through the penalty function5 $\Delta Q = Q - Q ^ { * }$ . The boundaries of the confidence ellipsoids are the level surfaces of the probability density function. The boundaries of the conditional and marginal confidence ellipsoids are the level surfaces of the conditional and marginal probability densities, respectively. In short, the computations required by the optimization and by the probabilistic interpretation are exactly the same. We can decide which interpretation to adopt after having computed the result, which is defined by $\mathbf { x } ^ { * }$ , $C ( \mathbf { x } ^ { * } )$ , $\Gamma ( \mathbf { x } ^ { * } )$ , $Q ^ { * }$ .

# Normalization of the probability density

The hypotheses used above for the probabilistic interpretation are too restrictive to be applied in most cases. However, these hypotheses can be applied to the normalized residuals. For example, the variance of the true residuals $\xi _ { i } ^ { \prime }$ could change with the index $i$ , and even the mean could be non-zero:

$\mathsf { p } _ { \Xi _ { i } ^ { \prime } } ( \xi _ { i } ^ { \prime } ) = N ( b _ { i } , \sigma _ { i } ^ { 2 } ) ( \xi _ { i } ^ { \prime } )$ . In this case the normalized residuals $\xi _ { i } = ( \xi _ { i } ^ { \prime } - b _ { i } ) / \sigma _ { i }$ , iwith bias $b _ { i }$ removed and the scale changed by the standard deviations $\sigma _ { i }$ , would all be random variables with the same probability density $N ( 0 , 1 )$ .

Even the independence hypothesis can be relaxed: the joint random variables $\Xi ^ { \prime }$ could be a multivariate Gaussian with non-zero correlations $\mathsf { p } _ { \Xi ^ { \prime } } ( \pmb { \xi } ^ { \prime } ) = N ( \mathbf { b } , \Gamma _ { \pmb { \xi } ^ { \prime } } ) ( \pmb { \xi } ^ { \prime } )$ and the normalization can be obtained with a square matrix $P$ such that $P ^ { I ^ { \prime } }$ $P = C _ { \pmb { \xi } ^ { \prime } } = \Gamma _ { \pmb { \xi } ^ { \prime } } ^ { - 1 }$ . The normalized residuals are defined by ${ \pmb \xi } = P \left( { \pmb \xi } ^ { \prime } - { \bf b } \right)$ , thus $\mathfrak { p } \equiv ( \pmb { \xi } ) = N ( \mathbf { 0 } , I ) ( \pmb { \xi } )$ with $I$ the $m \times m$ identity matrix. This procedure to normalize the residuals probability density function uses the same algorithms, giving the matrix square root $P$ , to remove the weight matrix $W$ from the weighted least squares problem; indeed, the residual normalization has a probabilistic interpretation with $W = C _ { \pmb { \xi } ^ { \prime } } = \Gamma _ { \pmb { \xi } ^ { \prime } } ^ { - 1 }$ .

# 5.8 Gaussian error models and outlier rejection

That the errors in the observations, used for orbit determination, have a Gaussian distribution cannot be assumed a priori: it is an empirical fact to be confirmed by experience, by applying rigorous statistical tests. Experience shows that, whenever large data sets are processed, the error distribution cannot be described by a single normal distribution. There are two main reasons for this.

First, some observations are “wrong”, that is contain errors which arise from unusual circumstances, including human error, software bugs, exceptionally difficult observing conditions: poor weather, too low signal-tonoise ratio (S/N), very fast moving objects, and so on. It is too difficult to include these cases in a statistical error model, and besides it would not be beneficial to the accuracy of the least squares solution. The best strategy is to decompose the residuals $\xi _ { i }$ into two subsets, one for which a probabilistic error model is attempted, the other containing the outliers which are removed from the fit (they are given weights $w _ { i i } = 0$ , see Section 5.3).

Second, even for the subset of residuals whose distribution is ruled by some probabilistic model, we cannot assume that the same probability density function, depending only upon the residuals values, can be applied to all. This is because there are hidden parameters, e.g., the S/N, the size of the pixels in the detector, the amount of trailing in the image, the accuracy of the star catalog used in the astrometric reduction, and more: the RMS error cannot be the same for different values of these parameters. The values of the hidden parameters are not always available, and they are not constant even for a given observing station: the accuracy of a given observatory often improves with time, as a result of the “learning curve” of the astronomers and of sporadic hardware, software, and star catalog upgrades.

![](images/11c459e2caf9175d6fd082c59c6c461eafc0f247ecadff41d031cbfc5d04acad.jpg)  
Fig. 5.3. Histograms of residuals for the declination of numbered asteroids as measured from the LINEAR observing station. For each of the 400 bins of width 0.03 arcsec, the four lines show, starting from the higher to the lower on the left side: all the residuals 1997–2003; only the outliers, automatically removed by the algorithm discussed in this section; the residuals actually used in the orbit fits; the Gaussian distribution with the same mean and the same RMS of the residuals actually used (the vertical scale is logarithmic, thus the Gaussian is represented by a parabola).

To confirm this, we shall use as an example a large data set from population orbit determination; the collaborative case is discussed in Chapter 15.

In a typical population case, Figure 5.3 shows histograms of the residuals in one of the two angular coordinates, the declination $\delta$ , after fitting orbits of numbered asteroids, for which the orbit is over-determined: the residuals are essentially due to the astrometric errors, orbit errors giving a very small contribution. Only the residual from a single observatory, the most prolific producer of asteroid astrometry, are included: more than 9 million observations have been processed to produce this figure. The upper curve, showing the distribution of all the residuals, is clearly not a Gaussian, but has a significant tail of comparatively large residuals. For such a large data set, it is impossible to use human judgement to select the outliers, there needs to exist a fully automated outlier removal procedure, which is described below; these rejections remove the tail of large residuals. The other residuals have a distribution which is not a single Gaussian, but can be modeled as a combination of Gaussian distributions.

# Outlier removal for weak fit

To select the outliers, to be discarded from the fit, it is not always enough to pick up the residuals with the largest absolute values. This would work for a strongly over-determined fit, when the average sampling time of the observations is shorter than the time-scale of the real signal: a single “wrong” observation cannot significantly change the nominal solution, as in Figure 5.4, top. This is normally the case in collaborative orbit determination, when the sampling time is decided as a design parameter of the tracking instruments, knowing the time-scale of the changes in the signal.

![](images/1a45f83903d7ea7c650bdd5a0210b9b2f1ba671c5abb8ef5785b81014c9e1347.jpg)  
Fig. 5.4. The effect of an outlier on a fit. The points have a Gaussian distribution $N ( 0 , 1 )$ , the outlier (cross) is 4 RMS away from the mean. Above: for an over-determined fit with dense data (80 points, polynomial degree 10) the polynomial solution including the outlier (dashed) is different from the one without it (solid line), at least locally, but the outlier clearly has the largest residual. Below: for a weak fit with sparse data (10 points, polynomial degree 3) the fit with the outlier is bent towards it, thus making the residual much less prominent.

On the contrary, when the observations are sparse, the solutions with and without the “wrong” one are quite different, thus other residuals may become larger (see the residual at time 4 in Figure 5.4, bottom). This often happens in the population case, when the fits are only marginally over-determined.

To take this effect into account, we use eq. (5.1) for a linearized approximation of the post-fit residuals $\xi$ as a function of the pre-fit residuals $\xi _ { 0 }$

$$
\pmb { \xi } = \left[ I - B \Gamma _ { \mathbf { x } } B ^ { T } \right] \pmb { \xi } _ { 0 }
$$

where $B$ is the design matrix, and compute the corresponding covariance by the propagation formula (5.5), with the uncertainty of the pre-fit residuals6 given by the covariance matrix expressing the observation errors $\Gamma _ { \xi _ { 0 } } = I$

$$
\Gamma _ { \pm } = \left[ I - B \Gamma _ { \mathbf { x } } B ^ { T } \right] I \left[ I - B \Gamma _ { \mathbf { x } } B ^ { T } \right] = I - B \Gamma _ { \mathbf { x } } B ^ { T } .
$$

For an individual post-fit residual $\xi _ { i }$ , the variance is

$$
\gamma _ { \pm , i , i } = 1 - B _ { i } \Gamma _ { \mathbf { x } } B _ { i } ^ { T }
$$

where $B _ { i } = \partial \xi _ { i } / \partial \mathbf { x }$ is the relevant row of the design matrix. In a similar way it is possible to compute the covariance matrix of a discarded residual $\xi _ { k }$ , namely the residual (with respect to the orbital solution) of an observation which has not been used in the fit: the contribution from the orbital uncertainty is just $B _ { k } \Gamma _ { \mathbf { x } } B _ { k } ^ { I ^ { \prime } }$ . In this case, however, the prediction error and the measurement error can be considered uncorrelated, thus the discarded residual has variance which is the simple sum of the two error sources

$$
\gamma _ { \pm , k , k } = 1 + B _ { k } \Gamma _ { \mathbf { x } } B _ { k } ^ { T } .
$$

Thus, if a residual has been used in the fit, it has to be normalized by dividing by the square root of the variance (5.6), which is $\leq 1$ , else if it has already been discarded the normalized value is obtained by dividing by the square root of the variance (5.7), which is $\geq 1$ .

An algorithm for outlier rejection could be as follows: a residual $\xi _ { i }$ is discarded if its normalized absolute value is $\ge \chi d i s c$ ; a discarded residual $\xi _ { k }$ is recovered if its normalized absolute value is $\leq \chi _ { r e c }$ . The choice of the two parameters $\chi _ { r e c } < \chi _ { d i s c }$ is delicate, although the standard $\chi ^ { 2 }$ tables can be used to give an indication. Of course this is just a step of an iterative procedure, with the nominal solution recomputed between steps.

A practical implementation of a fully automated outlier rejection procedure needs to be complicated, to guarantee convergence of the differential corrections at each step and convergence of the subset of outliers: if there are very large residuals they have to be removed first, that is the values of $\chi _ { r e q } , \chi _ { d i s c }$ have to be adapted at each step: for a detailed description see (Carpino et al. 2003, Section 2.2.2). Moreover, the observations are often rejected by groups, as in the case of astrometric observations, where the two-dimensional observations $( \alpha _ { i } , \delta _ { i } )$ are rejected/recovered together: this requires the analog of eqs. (5.6) and (5.7) for $2 \times 2$ covariance matrices.

# Binning and local Gaussian models

Ideally, the weight matrix for the observations should be based upon complete information on the measurement process, including the assessment by the observer, who is generally the best judge of the data quality. In practice the information is always incomplete, or anyway it has not been made available to the orbit computer. A possible way out has been explored by Carpino et al. (2003): by using all the information actually available, the data are split into bins which should represent homogeneous observing and measuring conditions.

The data are binned first by observatory, by observing technology,7 and by time. The data with low accuracy warnings, as in the primitive method of storing less significant digits, are binned separately. They can be further split by using the available information on the conditions which make the measurement difficult, such as low S/N, fast proper motion, dense star fields (e.g., observations close to the galactic plane). If the S/N value is not available, the apparent magnitude can be used as a proxy (by assuming that the exposure time is uniform for a given station in the same time period).

Once the data are binned, for each bin $j$ a best fitting normal distribution $N ( b _ { j } , \sigma _ { j } ^ { 2 } )$ is computed (not using the outliers). It might be argued that the bias $b _ { j }$ should be 0, otherwise the data should be re-calibrated: in practice, this calibration has often to be done a posteriori. The kurtosis value can be used as a control that the distribution is not too far from a Gaussian. Then the error model is the list of bins (with their definitions, such that each observation can be classified in one and only one bin) with their values $b _ { j } , \sigma _ { j }$ . Such a model already contains useful information because the RMS values for different observatories and different years may differ by an order of magnitude, from 0.2 to 2 arcsec, and the biases can be very significant (Carpino et al. 2003, Figures 4–5); however, this is not enough.

# Correlations

Even after the residuals have been scaled with the appropriate weights, and shifted by the appropriate biases, it is not the case that their probability distributions are correctly represented by independent, unit variance Gaussian functions: they are found not to be independent. For Gaussian distributions, independence and zero correlation are equivalent, thus we can test the hypothesis of independence by measuring the correlation of a set of couples of residuals $( \xi _ { i } , \xi _ { j } )$ , with $( i , j ) \in B$ :

$$
\mathrm { C o r r } ( \pmb { \xi } , \boldsymbol { B } ) = \frac { 1 } { N _ { B } } \sum _ { ( i , j ) \in \boldsymbol { B } } \xi _ { i } \xi _ { j }
$$

where $N _ { B }$ is the total number of couples in the subset $B$ , and the residuals are already shifted by the bias and scaled by the RMS of their bin.

The question is how to select the sets $B$ of couples. Carpino et al. (2003) discuss several tests showing that the most significant correlations are timewise, appearing as a function of the time difference between the observations: they occur between observations of the same asteroid from the same station and with time differences of up to few weeks, with the largest values (typically in the range 0.2–0.4) for observations in the same night.

Correlations of this order cannot be safely neglected in the least squares fit: as the simplest example, let us suppose the covariance matrix of a set of $m$ observations taken in the same night has 1 on the diagonal and $\alpha < 1$ outside. Such a matrix has the vector 1 as eigenvector with the largest eigenvalue $1 + ( m - 1 ) \alpha$ . For a tracklet containing $m = 5$ observations, correlations $\alpha = 0 . 2 – 0 . 4$ correspond to a longest semiaxis of the confidence ellipsoid $Z _ { L } ( 1 )$ of $\sqrt { 1 . 8 } - \sqrt { 2 . 6 }$ , while neglecting correlations means replacing it with a sphere of radius 1. According to Carpino et al. (2003), spatial correlations, depending upon the position on the sky, did not need to be accounted for at the data quality level current at the time.

Thus the binning is done by time difference: from the values of the correlations (5.8) estimated for each time difference bin a linear model has to be fit, in such a way that the correlation $\mathrm { C o r r } ( \delta t , S )$ between two observations (from the same station $S$ and of the same asteroid) can be represented as $\begin{array} { r } { \mathrm { C o r r } ( \delta t , S ) = \sum _ { i } \ c _ { i } \ f _ { i } ( \delta t ) } \end{array}$ for any time difference $\delta t$ . However, we cannot use a linear combination of an arbitrary set of base functions $f _ { i }$ , because the covariance matrix of the observation errors has to be positive definite. It can be shown (Mussio 1984) that some functions of time have the property of ensuring that the correlation matrix is positive definite, so that also the covariance matrix is positive definite. One requirement is that all of these functions must decay to zero with time: $\begin{array} { r } { \operatorname* { l i m } _ { \delta t  + \infty } f _ { i } ( \delta t ) = 0 } \end{array}$ . The list includes exponential decaying functions $\exp ( - c \delta t )$ , Gaussian-like functions $\exp ( - c \delta t ^ { 2 } )$ , quadratic times exponential functions of the form $( 1 - d \delta t ^ { 2 } ) \ \exp ( - c T )$ , and all their linear combinations. Carpino et al. (2003) provide tables of the coefficients $c _ { i }$ for these base functions, applicable to the observatories providing the largest data sets, thus allowing us to compute the non-diagonal weight matrix $W$ to be used in the formulae of Section 5.3.

The above attempt to build an error model by processing incomplete information cannot give completely reliable results. Moreover, as the accuracy of the observations improves, the shortcomings of a “naive” error model (such as weighting all the observations at 1 arcsec) become more and more troublesome, especially for critical applications such as those of Chapter 12. A recent reanalysis of the set of residuals from all the astrometric observations of numbered asteroids (Baer et al. 2008) confirms the presence of significant biases and correlations reported by Carpino et al. (2003), but has also detected significant spatial correlations, such as declination biases depending upon the declination of the observations and found in the data of different observatories; the values of such biases can be as large as 0.2 arcsec. The most obvious interpretation is that there are regional systematic errors in the star catalogs mostly used by asteroid observers.8 Whatever the cause, the effect of biases which are not constant for a given observatory cannot be removed by binning by observatory. They need to be removed by binning by region on the celestial sphere all the observations astrometrically reduced with the same star catalog. At the time this book is being written, the information on star catalogs used has not yet been made available to the orbit computers, thus there is no rigorous solution to the astrometric error model problem which is immediately applicable. This is a serious limitation to the reliability of a probabilistic interpretation of the orbit determination problem, which has nothing to do with the mathematical formulation but with the real-world limitations of an incomplete open data policy.

6

# RANK DEFICIENCY

This chapter discusses the cases in which the standard differential correction procedure for orbit determination fails. The worst failure is when the normal matrix is degenerate: this can result from the action of a group of symmetries leaving the residuals unchanged. The differential corrections as an iterative process may fail even when each individual step can be computed. The most common cause is an approximate degeneracy, which can result from an approximate symmetry. Different methods to constrain and stabilize the differential corrections in such difficult cases are discussed. This chapter systematizes and generalizes the results published in several papers (Milani and Melchioni 1989, Milani et al. 1995, Bonanno and Milani 2002, Milani et al. 2002, Milani et al. 2005d).

# 6.1 Complete rank deficiency

If, at some step $\mathbf { x } _ { j }$ of the differential corrections, the normal matrix $C$ is not invertible, then the correction solving

$$
B ^ { T } \ B \ ( { \bf x } _ { j + 1 } - { \bf x } _ { j } ) = - B ^ { T } \ \pmb { \xi }
$$

cannot be computed by means of the covariance matrix $\Gamma$ . Nevertheless solutions of the normal equation always exist (but are not unique). Let us introduce the pseudo-inverse $C ^ { * }$ , defined as the matrix associated to the null map on the kernel of $C$ times the inverse of $C$ restricted to the subspace orthogonal to the kernel; $C ^ { * }$ provides the solution of minimum norm

$$
\begin{array} { r } { \mathbf { x } _ { j + 1 } = \mathbf { x } _ { j } - C ^ { * } B ^ { T } \pmb { \xi } . } \end{array}
$$

The pseudo-inverse $C ^ { * }$ can be used as generalized covariance matrix for some purposes (see Section 8.3). However, corrections based on the pseudo-inverse are unlikely to converge towards a minimum of the target function.

Under these conditions, the rank deficiency order $d$ is an integer such that the matrix $C$ has rank $N - d$ , that is a kernel of dimension $d$ . Then the matrix $B$ has the same rank $N - d$ , its column $m$ -vectors $\{ { \bf b } _ { j } \} , j = 1 , N$ , are linearly dependent: they span a linear subspace of dimension $N - d$ , and there is a subspace $K \subset \mathbb { R } ^ { N }$ of dimension $d$ , such that

$$
\mathbf { v } \in K \Longrightarrow B \mathbf { v } = \mathbf { 0 } .
$$

The effect on the residuals of a change in any one of the directions $\mathbf { v } \in K$ is of second order (with respect to the size of the change)

$$
\pmb { \xi } ( \mathbf { x } _ { i } + s \mathbf { v } ) - \pmb { \xi } ( \mathbf { x } _ { i } ) = s B \ \mathbf { v } + \mathcal { O } ( s ^ { 2 } ) = \mathcal { O } ( s ^ { 2 } ) .
$$

The intuitive interpretation is the following: some linear combinations of the parameters $\mathbf { x }$ are uninfluential on the residuals, thus they cannot be constrained by the least squares optimization.

All the above discussion assumes exact arithmetic, e.g., that the inverses of the matrices are computed exactly when the determinant is non-zero, and are not computable when the determinant is zero. With a digital computer, rounding-off effects could result either in inverse matrices being computed even when the exact determinant is zero or in failure of the computation even for small but non-zero determinant. In practice, when rank deficiency occurs the iterative procedure fails disastrously, e.g., with increasingly large corrections until a meaningless value for some of the parameters $\mathbf { x }$ is reached.

# Curing rank deficiency

The only solution in case of rank deficiency is to change the problem. Either fewer parameters are to be solved, or more observations are to be used.

If there is no way to increase the number of observations to be used, the only solution is descoping. That is, $d$ parameters have to be removed from the fit list $\mathbf { x }$ (and added to the consider parameter list $\mathbf { k }$ ) in such a way that the matrices $B$ and $C$ remain of rank $N - d$ . This implies that the values of the additional consider parameters are fixed at some nominal value, which are arbitrary unless a priori information is available (from other measurements). A more general procedure is as follows: change the basis in the space $\mathbb { R } ^ { N }$ of $\mathbf { x }$ in such a way that the first $d$ vectors $\{ \mathbf { v } _ { j } \} , j = 1 , d$ , are a basis of $K$ ; the other $N - d$ coordinates can be selected as the new fit parameters. By using Gram–Schmidt orthonormalization, it is possible to do this with an orthogonal $N \times N$ matrix as coordinate change: with a suitable selection of signs, the coordinate change is a rotation.

As we shall see in the examples of this book, this procedure is natural when the rotation is done among parameters of the same type, such as the initial conditions $\mathbf { y _ { 0 } }$ , the dynamical parameters $\pmb { \mu }$ , the kinematical parameters $\pmb { \nu }$ . When we are forced to “rotate” a mix of variables with different dimensions and physical interpretations this solution is far from intuitive.

Another option is the use of a priori observations. This is equivalent to assuming that some information was available, on at least some of the variables $\mathbf { x }$ , before processing the current set of observations. That is, we add to the set of observations constraints $\textbf { x } = \textbf { x } ^ { P }$ on the values of the parameters, with $\mathbf { x } ^ { P } \in \mathbb { R } ^ { N }$ a set of assumed values, and give to the a priori observations $x _ { i } = x _ { i } ^ { P }$ weights $1 / \sigma _ { i } , i = 1 , N$ corresponding to the assumption that the a priori standard deviation is $\sigma _ { i }$ . This is equivalent to adding the a priori normal equation

$$
\boldsymbol { C } ^ { P } \mathbf { x } = \boldsymbol { C } ^ { P } \mathbf { x } ^ { P }
$$

with $C ^ { P } = \mathrm { d i a g } [ \sigma _ { i } ^ { - 2 } ]$ ; a non-diagonal a priori normal matrix could be used if this is a better representation of the information already available. Thus an “a priori penalty” is added to the target function

$$
Q ( \mathbf { x } ) = \frac { 1 } { N + m } \left[ ( \mathbf { x } - \mathbf { x } ^ { P } ) ^ { T } C ^ { P } \left( \mathbf { x } - \mathbf { x } ^ { P } \right) + \pmb { \xi } ^ { T } \pmb { \xi } \right]
$$

and the complete normal equation becomes

$$
\left[ C ^ { P } + B ^ { T } B \right] \Delta \mathbf { x } = - B ^ { T } \pmb { \xi } + C ^ { P } \left( \mathbf { x } ^ { P } - \mathbf { x } _ { j } \right)
$$

with $\Delta \mathbf { x } = ( \mathbf { x } _ { j + 1 } - \mathbf { x } _ { j } )$ as unknown. If the a priori uncertainties $\sigma _ { i }$ are small enough, the new normal matrix $C = C ^ { P } + B ^ { T } \ B$ has rank $N$ and the problem is solved. The question is whether the a priori information used is reliable. For the parameters belonging to $\mathbf { y _ { 0 } }$ , this means assuming that some information on the orbit was already available. For the parameters belonging to $\mathbf { \Omega } _ { \mu , \nu }$ the a priori information could be available from measurements having nothing to do with the orbit. For example, the coefficients of the gravity field could be available from ground-based gravimetry; the position of the observing stations could have been measured by previous missions.

The a priori observations could be applied to only $N ^ { \prime } < N$ of the fit parameters $x _ { i }$ , with a minimum of $d$ (at least as many a priori observations as the rank deficiency). If $N ^ { \prime } = d$ and the a priori uncertainties tend to zero, the solution of the rank deficiency problem based upon a priori observations tends to the previous solution, based on assuming $d$ fit parameters as known with some exact value. In practice, assuming a very strong constraint is the same as assuming exact values; this allows us to handle both methods to solve the rank deficiency problem with the same formulae. On the contrary, a weak constraint is a way to introduce a non-exclusive preference for some portions of the parameter space: for example, in solving for an orbit in Keplerian elements, we can introduce an a priori observation of the eccentricity of the form $e = 0 \pm 1$ to force the solution to be elliptic, still allowing for hyperbolic orbits only if there are significantly larger residuals for all the $e < 1$ solutions. This corresponds to the a priori information that strongly hyperbolic orbits are very rare in the Solar System (indeed, none is known), thus assuming an $e < 1$ orbit is better in almost all cases, nevertheless the orbit determination algorithm should not be strongly biased against discovering objects belonging to a new orbital class.

The use of a priori information can take a more general form, as a priori constraints to the least squares solution: the search for a minimum of the target function is restricted to the set of parameters $\mathbf { x }$ fulfilling a set of $k$ equations $\mathbf { f } ( \mathbf { x } ) = \mathbf { 0 }$ . If $k \geq d$ functional constraints are suitably chosen, the rank deficiency can be removed. The general theory of constrained optimization is beyond the aim of this book; see, e.g., (Conn et al. 1992). We linearize the constraint by taking the differential of $\mathbf { f }$ at the current value $\mathbf { x } _ { k }$ of the parameters (at a given iteration of the differential corrections); let $A = \partial \mathbf { f } / \partial \mathbf { x } ( \mathbf { x } _ { k } )$ be the Jacobian matrix. Then the constraint can be described by adding to the target function a quadratic function of the correction ${ \bf x } _ { k + 1 } - { \bf x } _ { k }$ , defined by using $A$ (see Section 15.5).

# Model problem with degeneracy

The general solution of the model problem of Section 5.6 depends upon the parameter $k$ , proportional to the square root of the mass of the central body

$$
a ( t ) = a _ { 0 } , \lambda ( t ) = \frac { k } { a _ { 0 } ^ { 3 / 2 } } t + \lambda _ { 0 } ,
$$

the derivatives of the residuals with respect to the parameters $( { a } _ { 0 } , \lambda _ { 0 } , k )$ are

$$
B = \left[ \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } \textbf { t } - \mathbf { 1 } - \frac { n _ { 0 } } { k } \textbf { t } \right] ;
$$

the first and the last column are proportional. For $t = 0$ the normal matrix

$$
C = B ^ { T } B = m \left[ \begin{array} { c c c } { { \frac { 9 } { 4 } \frac { n _ { 0 } ^ { 2 } } { a _ { 0 } ^ { 2 } } \mathrm { V a r } ( { \bf t } ) } } & { { 0 } } & { { - \frac { 3 } { 2 } \frac { n _ { 0 } ^ { 2 } } { k a _ { 0 } } \mathrm { V a r } ( { \bf t } ) } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \frac { 3 } { 2 } \frac { n _ { 0 } ^ { 2 } } { k a _ { 0 } } \mathrm { V a r } ( { \bf t } ) } } & { { 0 } } & { { \frac { n _ { 0 } ^ { 2 } } { k ^ { 2 } } \mathrm { V a r } ( { \bf t } ) } } \end{array} \right]
$$

has determinant zero. In the normal equation

$$
{ \cal C } ~ \left[ \begin{array} { c } { { \Delta a _ { 0 } } } \\ { { \Delta \lambda _ { 0 } } } \\ { { \Delta k } } \end{array} \right] = { \cal D } = - { \cal B } ^ { T } \xi = m \left[ \begin{array} { c } { { - \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } \left[ \mathrm { C o v } ( { \bf t } , { \lambda } ) - n _ { 0 } \mathrm { V a r } ( { \bf t } ) \right] } } \\ { { \overline { { { \lambda } } } - \lambda _ { 0 } } } \\ { { \frac { n _ { 0 } } { k } \left[ \mathrm { C o v } ( { \bf t } , { \lambda } ) - n _ { 0 } \mathrm { V a r } ( { \bf t } ) \right] } } \end{array} \right]
$$

there are only two independent equations

$$
\Delta \lambda _ { 0 } = \overline { { \lambda } } - \lambda _ { 0 } , ~ \frac { n _ { 0 } } { 2 } ~ \left[ - 3 \frac { \Delta a _ { 0 } } { a _ { 0 } } + 2 \frac { \Delta k } { k } \right] = n ^ { * } - n _ { 0 }
$$

where $n ^ { * }$ is the solution of the linear model problem. Thus there are infinite solutions, with all the combinations of $\Delta a _ { 0 }$ and $\Delta k$ satisfying the second equation. The condition to be satisfied by the solution is $k / a _ { 0 } ^ { 3 / 2 }$ ; the equation (6.5) above constraining $\Delta a _ { 0 }$ and $\Delta k$ 0 is obtained by expanding and neglecting second-order terms. Fixing the value of either $a _ { 0 }$ or $k$ removes the problem. An a priori observation of either $a _ { 0 }$ or $k$ removes the rank deficiency, although it may leave an approximate one, see below.

# 6.2 Exact symmetries

An exact symmetry of an orbit determination problem is the action of a group on the space of the fit parameters $\mathbf { x }$ , such that all the residuals are invariant. Let $G$ be a group of transformations $g [ \mathbf { x } ]$ of $\mathbb { R } ^ { N }$ : if for every $g \in G$

$$
\pmb { \xi } ( \mathbf { x } ) = \pmb { \xi } ( g [ \mathbf { x } ] )
$$

then $G$ is a group of exact symmetries of the orbit determination. The simplest case is a one-parameter group of symmetries of the orbit determination: $G$ is either $\mathbb { R }$ or $\mathbb { R } / ( 2 \pi \mathbb { Z } )$ , that is $g ( s ) \in G$ is parameterized by either a real number or an angle variable; the internal operation in $G$ corresponds to the sum of the parameters. Moreover, we assume that there is a differentiable action, that is the map $( s , \mathbf { x } ) \mapsto g ( s ) [ \mathbf { x } ]$ is differentiable, and that $G$ has no isotropy, that is $g ( s ) [ \mathbf { x } ] \neq \mathbf { x }$ for every $\mathbf { x }$ unless $s = 0$ applies.1 As for the other form of symmetries discussed in Section 4.1, the same results apply to a local one-parameter group of symmetries, with the same properties only for $s$ in a neighborhood of 0.

If there is a (local) one-parameter group of exact symmetries the normal equation has rank deficiency $\geq 1$ . The residuals do not change with $s$ :

$$
\mathbf { 0 } = { \frac { \partial \pmb { \xi } ( s ) [ \mathbf { x } ] } { \partial s } } = { \frac { \partial \pmb { \xi } } { \partial \mathbf { x } } } { \frac { \partial g ( s ) [ \mathbf { x } ] } { \partial s } } = B { \frac { \partial g ( s ) [ \mathbf { x } ] } { \partial s } }
$$

and the hypothesis that the group has no isotropy implies that

$$
\mathbf { 0 } \neq \left. \frac { \partial g ( s ) [ \mathbf { x } ] } { \partial s } \right| _ { s = 0 } = \mathbf { v } _ { 1 } \in \mathbb { R } ^ { N } .
$$

The vector $\mathbf { v } _ { 1 }$ plays the same role as one of the $\mathbf { v } _ { k }$ in the previous section: it is orthogonal to each of the rows of $B$ , thus it belongs to the kernel of $C = B ^ { T ^ { \prime } } B$ . The hypothesis of no isotropy can be relaxed as follows: if

$$
\mathbf { 0 } \neq \left. \frac { \partial g ( s ) [ \mathbf { x } ^ { * } ] } { \partial s } \right. _ { s = 0 }
$$

the rank deficiency occurs for the normal matrix at the nominal solution $\mathbf { x } ^ { * }$ .

If there are $d$ groups of symmetries with one parameter and the vectors $\mathbf { v } _ { k }$ , defined by the derivative with respect to $s$ of each group action, are linearly independent, then the rank deficiency is $d$ .

The symmetries could be organized in higher dimension groups, such as the groups of translations and rotations. In such case we need to exploit the differentiable structure of the groups, that is they have to be Lie groups with differentiable actions on the parameter space $\mathbb { R } ^ { N }$ . The no-isotropy condition cannot in general be satisfied and the group internal operation may not be commutative (the rotation group $S O ( 3 )$ acting on $\mathbb { R } ^ { 3 }$ is an example of both difficulties). A theory of the Lie groups of symmetries would require some mathematical background, which is not worth presenting here. Thus in this book we shall replace, e.g., the symmetry group $S O ( 3 )$ , with three oneparameter symmetry groups, corresponding to the rotations around three orthogonal axes; this is analogous to what was done in Section 4.1.

If there is a symmetry group, then there is also a corresponding rank deficiency. If there is a rank deficiency, by (6.2) the one-parameter group of translations $\mathbf { x } \mapsto \mathbf { x } + s \mathbf { v }$ is such that the residuals change by quantities $\mathcal { O } ( s ^ { 2 } )$ , of higher order with respect to the change $s \textbf { v }$ , that is a “first order symmetry”. Is there also an exact symmetry, defined by a one-parameter group operating by transformations other than translations? Under somewhat more restrictive hypotheses, this can be guaranteed. If the normal matrix $C ( \mathbf { x } )$ , as computed at each value of the fit parameters $\mathbf { x }$ , always has rank $N - 1$ , then the eigenvector with zero eigenvalue defines a smooth vector field.2 The integral flow of such a vector field provides the symmetry group.

In conclusion, symmetries imply rank deficiencies, and (under some additional hypotheses) rank deficiencies imply symmetries. The two phenomena occur in the same cases: the examples in this and in the following chapters show that they occur often, and their understanding is critical.

# Model problem with scaling

In the model problem with integral flow (6.4) there is a symmetry with a multiplicative parameter $w \in \mathbb { R } ^ { + }$

$$
k \mapsto w ^ { 3 } k , \quad a _ { 0 } \mapsto w ^ { 2 } a _ { 0 }
$$

leaving $n$ invariant, thus the general solution of the equation of motion is also invariant, and so is the prediction function (the observation function being just a projection onto the second component of the state vector). This is a change of scale (see Section 4.1), e.g., could be obtained by changing the unit of length by a factor $L = w ^ { 2 }$ without changing the unit of time, then $k ^ { 2 }$ would change by a factor $L ^ { 3 } = w ^ { 6 }$ . The symmetry can be represented with an additive parameter $s$ by setting $w = \exp ( s )$ . The derivative of the symmetry group action with respect to $s$ is

$$
\frac { d a _ { 0 } } { d s } = 2 w ^ { 2 } a _ { 0 } , \frac { d k } { d s } = 3 w ^ { 3 } k
$$

and for $s = 0 , w = 1$ this gives a vector $( 2 a _ { 0 } , 3 k )$ orthogonal to $( - 3 / a _ { 0 } , 2 / k )$ which is the vector of coefficients of the equation constraining $\Delta a _ { 0 }$ and $\Delta k$ .

# 6.3 Approximate rank deficiency and symmetries

An approximate rank deficiency of order $d$ means there is a subspace $K$ of dimension $d$ in $\mathbb { R } ^ { N }$ , and a constant $\epsilon$ with $0 < \epsilon \ll 1$ , such that

$$
\mathbf { v } \in K , \ | \mathbf { v } | = 1 \Longrightarrow | { \boldsymbol { B } } \mathbf { v } | \leq \epsilon ,
$$

a generalization of (6.1). Moreover (6.7) must not apply to a subspace of dimension $> d$ . Equation (6.7) implies that the quadratic form defined by the normal matrix $C$ , restricted to $K$ , has values of order $\epsilon ^ { 2 }$ on unit vectors:

$$
\mathbf { v } \in K , \ | \mathbf { v } | = 1 \Longrightarrow \mathbf { v } ^ { T } C \mathbf { v } = ( B \mathbf { v } ) ^ { T } B \mathbf { v } \leq \epsilon ^ { 2 } .
$$

We shall now study the properties of the eigenvalues of $C$ . Let $\mathbf { v } _ { j }$ , for $j = 1 , N$ , be unit eigenvectors of the normal matrix $C$ , with non-negative eigenvalues $0 \le \lambda _ { 1 } \le \lambda _ { 2 } \le \dots \le \lambda _ { N }$ . The values of the quadratic form on the unit sphere are constrained by the spectrum of the matrix $C$ :

$$
\begin{array} { r } { \operatorname* { m i n } _ { | \mathbf { x } | = 1 } \mathbf { x } ^ { T } C \mathbf { x } = \lambda _ { 1 } , \ \quad \operatorname* { m a x } _ { | \mathbf { x } | = 1 } \mathbf { x } ^ { T } C \mathbf { x } = \lambda _ { N } , } \end{array}
$$

thus $\lambda _ { 1 } ~ \le ~ \epsilon ^ { 2 }$ . In the simple case $d \ : = \ : 1$ there is one eigenvalue of the normal matrix $\leq \epsilon ^ { 2 }$ , one eigenvalue of the covariance matrix $\geq 1 / \epsilon ^ { 2 }$ , and one semiaxis of the confidence ellipsoid $Z _ { L } ( 1 )$ of length $\geq 1 / \epsilon$ .

# Approximate rank deficiency of order $d > 1$

For $d > 1$ a similar result holds: if the subspace $K$ has dimension $d$ , and the quadratic form defined by $C$ , restricted to the unit vectors of $K$ , is $\leq \epsilon ^ { 2 }$ , then the matrix $C$ has at least $d$ eigenvalues $\leq \epsilon ^ { 2 }$ .

This can be proven by recursion on $d$ . The case $d = 1$ has been proven above. Let us prove the result for $d$ , assuming it applies to $d - 1$ .

Let $Z$ be the linear subspace of $\mathbb { R } ^ { N }$ orthogonal to the eigenvector $\mathbf { v } _ { 1 }$ . The intersection $K ^ { \prime } = K \cap Z$ does not contain $\mathbf { v } _ { 1 } \in K$ and has dimension $d - 1$ . Thus we can apply the same result to $K ^ { \prime } \subset Z$ : the quadratic form defined by $C$ restricted to $Z$ has values $\leq \epsilon ^ { 2 }$ on the unit vectors of $K ^ { \prime }$ . Thus the restriction of $C$ to $Z$ has $d - 1$ eigenvalues less than $\epsilon ^ { 2 }$ , but these eigenvalues are $\lambda _ { 2 } \le \lambda _ { 3 } \le \dots \le \lambda _ { N }$ : we conclude $\lambda _ { d } \leq \epsilon ^ { 2 }$ .

This has implications on the uncertainty of the results: in an approximate rank deficiency of order $d$ , there are $d$ eigenvalues of the covariance matrix $\Gamma = C ^ { - 1 }$ larger than $1 / \epsilon ^ { 2 }$ and the confidence ellipsoid $Z _ { L } ( 1 )$ has $d$ semiaxes longer than $1 / \epsilon$ . The converse is also true: if there are $d$ semiaxes longer than $1 / \epsilon$ , then there are $d$ eigenvalues of $C$ smaller than $\epsilon ^ { 2 }$ , and the subspace $K$ generated by the related eigenvectors $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , . . . , \mathbf { v } _ { d }$ fulfills the definition for approximate rank deficiency of order $d$ , with small parameter $\epsilon$ .

This implies that approximate rank deficiency can be found a posteriori by principal components analysis, that is, after computing the covariance matrix $\Gamma$ and its eigenvalues, by selecting the ones larger than some value, or anyway the few largest ones. As we shall see in the applications of this method, see Section 16.5, if the approximate rank deficiency is found a posteriori from the spectrum of the covariance matrix, we need additional effort to understand what is the source of the problem and whether it can be fixed or just needs to be swept under the carpet by descoping.

# Approximate symmetries

An approximate symmetry is a differentiable group action changing the residuals by $\mathcal { O } ( \epsilon )$ , where $\epsilon$ is a small parameter. If $G$ is a one-parameter group with a differentiable action on the fit parameters $\mathbf { x }$ , such that for each $g ( s ) \in G$

$$
\pmb { \xi } \left( g ( s ) [ \mathbf { x } ] \right) = \pmb { \xi } ( \mathbf { x } ) + \epsilon s \mathbf { a } + \mathcal { O } ( s ^ { 2 } ) , \quad \mathbf { a } \in \mathbb { R } ^ { m } ; ~ | \mathbf { a } | = 1
$$

and the no-isotropy condition applies, at least locally near $\mathbf { x } ^ { * }$ , then

$$
\epsilon { \bf a } = \left. \frac { d \pmb { \xi } ( g ( s ) [ { \bf x } ] ) } { d s } \right| _ { s = 0 } = \frac { \partial \pmb { \xi } } { \partial \mathbf { x } } ( \mathbf { x } ) \left. \frac { \partial g ( s ) [ { \bf x } ] } { \partial s } \right| _ { s = 0 } = B \ \mathbf { v } .
$$

Thus, if $| \mathbf { v } | = v$ for the corresponding unit vector

$$
B \hat { \mathbf { v } } = \frac { \epsilon } { v } \mathbf { a }
$$

and the small parameter is $\epsilon / v$ . We conclude that there is an eigenvalue of the covariance matrix $\ge v ^ { 2 } / \epsilon ^ { 2 }$ .

The case of a higher dimension group of symmetries is more delicate. We proceed as in Section 6.2 and assume that there are $d$ local one-parameter groups of approximate symmetries, resulting in $d$ weak directions $\mathbf { v } _ { i }$ :

$$
B \mathbf { v } _ { i } = \epsilon \mathbf { a } _ { i } , \quad | \mathbf { a } _ { i } | \leq 1 .
$$

To simplify the discussion, we assume the symmetry groups have been reparameterized in such a way that $| \mathbf { v } _ { i } | = v _ { i } = 1$ . Let $K$ be the subspace of dimension $d$ generated by the $\mathbf { v } _ { i }$ . Then the quadratic form defined by $C$ , restricted to $K$ , has values $\mathcal { O } ( \epsilon ^ { 2 } )$ . However, if we need an explicit estimate we have to find the value $p$ such that

$$
\mathbf { x } \in K , | \mathbf { x } | = 1 \Longrightarrow \mathbf { x } ^ { T } C \mathbf { x } \leq p \epsilon ^ { 2 } .
$$

In general $p \leq d ^ { 2 }$ , and a better estimate can be obtained in special cases. Then, by applying the same recursive argument as before, there are $d$ eigenvalues of $C$ which have to be $\leq p \ \epsilon ^ { 2 }$ . Thus there are $d$ semiaxes of the ellipsoid $Z _ { L } ( 1 )$ longer that $1 / ( \epsilon _ { \sqrt { p } } )$ .

Taking also into account the re-parameterization problem, the above result is weaker than the statement “ $d$ one-parameter approximate symmetry groups imply an approximate rank deficiency of order $d ^ { \mathrm { { v } } }$ , because the small parameter is not the same. Still, symmetries can be an effective heuristic method to find and explain rank deficiencies, even approximate ones.

This method can be effectively used in case of symmetry breaking, if the residuals can be expanded in power series of some small parameter $\epsilon$ :

$$
\pmb { \xi } = \pmb { \xi } _ { 0 } + \epsilon \pmb { \xi } _ { 1 } + \mathcal { O } ( \epsilon ^ { 2 } ) .
$$

This can occur for different reasons, e.g., $\xi _ { 0 }$ could be the residuals obtained for some unperturbed equation of motion, $\boldsymbol { \epsilon } \xi _ { 1 }$ could be the first-order change due to a minor perturbation containing $\epsilon$ . If a group $G$ is an exact symmetry of the unperturbed problem obtained for $\epsilon = 0$ , but the perturbation $\boldsymbol { \epsilon } \xi _ { 1 }$ is not symmetric, then $G$ is a group of approximate symmetries, although the explicit computation of the factor $p$ is far from trivial. We shall see many examples of this in Section 6.5, and in Chapters 15, 16, and 17.

# 6.4 Scaling and approximate rank deficiency

Rank deficiency and exact symmetries are topological properties, that is their definitions (6.1) and (6.6) are independent of the choice of a metric in the $\mathbf { x }$ space of fit parameters. Approximate rank deficiency (and approximate symmetries) are metric properties, that is, (6.7) and (6.8) are conditions on the Euclidean lengths of the vectors $\mathbf { v }$ and $B { \mathbf v }$ , with $\mathbf { v }$ in some subspace. If the Euclidean norms $| \mathbf { v } | , | B \mathbf { v } |$ are replaced by some other norms, such as $| | \mathbf { v } | | _ { W } = \sqrt { \mathbf { v } ^ { T } \ W \ \mathbf { v } }$ , with a symmetric positive definite weight matrix $W$ , the definitions for the same $\epsilon$ are changed.

Let $P$ be a diagonal matrix $P = \mathrm { d i a g } [ p _ { 1 } , p _ { 2 } , . . . , p _ { N } ]$ with all $p _ { i } ~ > ~ 0$ . By scaling we mean a linear transformation in the space $\mathbb { R } ^ { N }$ of the fit parameters $\mathbf { x } = P \mathbf { y }$ . A scaling changes the metric, that is $| \mathbf { x } | = | | \mathbf { y } | | _ { W }$ with $W = P ^ { 2 }$ , and has the following effects on the normal equation

$$
{ \boldsymbol { B } } _ { \mathbf { y } } = { \frac { \partial \pmb { \xi } } { \partial \mathbf { y } } } = { \boldsymbol { B } } { \boldsymbol { P } } , \quad { \boldsymbol { C } } _ { \mathbf { y } } = { \boldsymbol { B } } _ { \mathbf { y } } ^ { T } { \boldsymbol { B } } _ { \mathbf { y } } = { \boldsymbol { P C P } } , \quad \Gamma _ { \mathbf { y } } = { \boldsymbol { P } } ^ { - 1 } { \boldsymbol { \Gamma } } { \boldsymbol { P } } ^ { - 1 } ,
$$

thus also the eigenvalues of $C , \Gamma$ are changed by scaling. Scaling is implicit in the choice of units to convert the quantities to be determined into the numeric fit vector $\mathbf { x }$ . The problem is, the units used to measure dimensionally different quantities are not easy to be compared. Are the initial conditions measured in astronomical units, rather than in centimeters, more or less suitable to be compared with the normalized $^ 3$ harmonic coefficients of the gravity of some planet? This question has no firm answer, still the change introduces a factor $\simeq [ 1 . 5 \times 1 0 ^ { 1 3 } ] ^ { \cdot 2 }$ in the matrix $W$ .

We would like to define approximate rank deficiency in a way independent of the units used in the $\mathbf { x }$ space, that is invariant with respect to the choice of an arbitrary diagonal weight matrix. To this goal we need to define some standard metric, applicable to all orbit determination problems. There are two meaningful ways to do this.

# A posteriori scaling

The a posteriori scaling of the normal matrix $C$ is obtained by reducing to unitary length the columns of the design matrix $B$

$$
b _ { i } = \left| \frac { \partial \pmb { \xi } } { \partial x _ { i } } \right| = \sqrt { c _ { i i } } , p _ { i } = 1 / b _ { i } \mathrm { f o r } i = 1 , N ,
$$

with $C = \left( c _ { i j } \right)$ . Then the scaled normal matrix $C _ { \mathbf { y } }$ has all the main diagonal coefficient equal to 1, all the others less than 1 in absolute value. This is not possible if some $b _ { i } = 0$ , but then there would be exact rank deficiency.

A posteriori scaling is also used to increase the numerical stability of the matrix inversion $C ^ { - 1 } = \Gamma$ , by computing $\Gamma _ { \mathbf { y } } = C _ { \mathbf { y } } ^ { - 1 }$ and then rescaling it to $\Gamma = P \Gamma _ { y } P$ . The reason is that the conditioning number of $C _ { \mathbf { y } }$ is often much smaller than that of $C$ . For example, if the matrix $C$ is diagonal, whatever $\operatorname { c o n d } ( C )$ the inversion is trivial, indeed $C _ { \mathbf { y } } = I$ has conditioning number 1; if $C$ is diagonal dominant4 then $C _ { \mathbf { y } }$ is also diagonal dominant and the inversion is numerically stable, even when $\mathrm { c o n d } ( C )$ is very large. The scaled $\mathrm { c o n d } ( C _ { \bf y } )$ indeed characterizes the difficulty of inversion and the stability of the result: even if there are methods (discussed in Section 5.3) to perform the inversion for very large $\mathrm { c o n d } ( C _ { \bf y } )$ , the iterations of differential corrections may diverge if this is the case.

The approximate rank deficiencies could be analyzed for the a posteriori scaled matrix $C _ { \mathbf { y } }$ . They indicate aliasing, that there are some fit parameters $\mathbf { x }$ which cannot be accurately entangled, having equivalent effect on the residuals (to first order). They also measure the numerical difficulty of inversion, even with rescaling: since the eigenvalues of $C _ { \mathbf { y } }$ cannot be very large (they are anyway $\leq N$ ), if there is a large $\mathrm { c o n d } ( C _ { \bf y } )$ there needs to be at least one eigenvalue of $C _ { \mathbf { y } }$ smaller than $\epsilon = N / \mathrm { c o n d } ( C _ { y } )$ , thus an approximate rank deficiency for $C _ { y }$ of order $d \geq 1$ , with $\epsilon$ as small parameter.

The matrices $C _ { \mathbf { y } } , \Gamma _ { \mathbf { y } }$ have no obvious probabilistic interpretation. If we scale the covariance matrix so that the main diagonal has coefficients 1

$$
\operatorname { C o r r } ( \mathbf { x } ) = ( r _ { i j } ) , ~ r _ { i j } = \frac { \gamma _ { i j } } { \sqrt { \gamma _ { i i } \gamma _ { j j } } }
$$

we obtain the correlation matrix: $r _ { i j } ( { \bf x } ) \ : = \ : \mathrm { C o r r } ( x _ { i } , x _ { j } )$ measures the dependence of the random variables $x _ { i }$ and $x _ { j }$ ; if only these two were considered, there would be a simple interpretation in terms of regression line and of the size of the residuals (Section 5.1). Unfortunately, $\mathrm { c o n d } ( \mathrm { C o r r } ( \mathbf x ) ) \ne \mathrm { c o n d } ( \Gamma _ { \mathbf y } )$ , although numerical tests with random design matrices $B$ show that they are of the same order of magnitude.

# A priori scaling

The a priori scaling of the normal matrix $C$ is obtained by considering an a priori diagonal normal matrix $C _ { 0 }$ . It is not meant to represent a formal a priori knowledge, which could be handled with the addition of a priori observations according to eq. (6.3). The matrix $C _ { 0 }$ could be built from upper bounds, derived from theory and/or very weak observational constraints, e.g., of the form $| x _ { i } | \leq 1 / \sqrt { c _ { i i } }$ . Then the a priori scaling would be given by the diagonal matrix $P$ such that $P C _ { 0 } P = I$ ; i.e., each parameter $x _ { i }$ would be measured as a fraction of its upper bound.

The approximate rank deficiencies could be analyzed for the a priori scaled matrix $C _ { \mathbf { y } }$ . They are useful to identify the parameters, or group of parameters, which cannot be measured at all with the current experiment, to the point that the values formally determined may be absurd.

As the simplest example, if there is just one parameter such that the corresponding column of the a priori scaled design matrix $B _ { \mathbf { y } } = B P$ has a norm $< \epsilon$ , then the unit vector $\hat { \mathbf { v } }$ along the corresponding axis is such that $\hat { \mathbf { v } } ^ { T } C _ { \mathbf { y } } \hat { \mathbf { v } } < \epsilon ^ { 2 }$ and the confidence ellipsoid has at least one semiaxis larger than $1 / \epsilon$ . In this case it does not matter whether the matrix inversion is stable, anyway the result is going to be absurd, and the following iterations of differential corrections may destabilize the result for other parameters. In such cases either descoping or constraining needs to be applied.

In conclusion, approximate rank deficiencies and approximate symmetries are extremely valuable as heuristic tools, either to debug the design of an orbit determination experiment or to warn about the unreliable results of one actual test. However, in most cases they provide only order of magnitude estimates, and have to be used with a bit of common sense.

# 6.5 Planetary systems: extrasolar planets

Planets orbiting around a star different from the Sun are one of the most important astronomical discoveries of recent years. Most such extrasolar planets have been discovered by measuring the radial velocity of the star with respect to the Solar System. As of October 2007, this was the case for 245 extrasolar planets $5$ out of a confirmed total of 279. In most cases the radial velocity of the star was measured by spectrometry, with accuracies currently at a few m/s; in a few cases planets have been discovered around pulsars, where the radial velocity is measured by the Doppler shift of the pulsar. Anyway, the radial velocity needs to be measured with respect to the barycenter of the Solar System, thus the orbit of the Earth from which we observe must also be accurately computed in barycentric coordinates (see Section 4.3) and its radial velocity component along the line of sight has to be subtracted.6 In this section we will outline the procedure for orbit determination of an extrasolar planetary system.

# One planet

If there is only one planet, the dynamical model is the two-body problem with $m _ { 0 }$ , the mass of the observed star, significantly larger than $m _ { 1 }$ , the mass of the planet. Neglecting the interaction with the other stars (and with the galaxy) the center of mass of the system of two bodies with position vectors $\mathbf { r } _ { 0 }$ , $\mathbf { r } _ { 1 }$ has a constant velocity in any inertial system, such as the one we adopt, which is moving with the center of mass of the Solar System. We are also neglecting stellar and galactic perturbations on the Solar System barycenter motion. The acceleration of the Sun towards the galactic center is just a few $\mathrm { { m } / \mathrm { { d a y } ^ { 2 } } }$ , and if the star is much closer than the galactic center, the differential acceleration is much less.

With the standard reduction of the two-body problem, eq. (4.9),

$$
\mathbf b _ { 0 } = \mu _ { 1 } \ \mathbf r _ { 1 } + ( 1 - \mu _ { 1 } ) \mathbf r _ { 0 } , \quad \mu _ { 1 } = \frac { m _ { 1 } } { m _ { 0 } + m _ { 1 } } , \quad \mathbf b _ { 1 } = \mathbf r _ { 1 } - \mathbf r _ { 0 }
$$

the coordinate of the star is $\mathbf { s } = \mathbf { r } _ { 0 } - \mathbf { b } _ { 0 } = - \mu _ { 1 } \mathbf { b } _ { 1 }$ in the barycentric system, and ${ \bf r } _ { 0 } = { \bf b } _ { 0 } + { \bf s } = { \bf b } _ { 0 } - \mu _ { 1 } { \bf b } _ { 1 }$ , with respect to the center of mass of our Solar System. Let $( x , y , z )$ be the Cartesian coordinates of $\mathbf { b } _ { 1 }$ in a reference system with the $z$ axis in the direction $\hat { \mathbf { z } }$ of the Earth, $( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ the corresponding coordinates of the center of mass, and let $( a , e , I , \Omega , \omega , \boldsymbol { v } )$ be the Keplerian orbital elements of the two-body orbit of $\mathbf { b } _ { 1 }$ ; the mean motion is $n = \sqrt { G M _ { 0 } / a ^ { 3 } }$ , with $M _ { 0 } = m _ { 0 } + m _ { 1 }$ .

In an orthogonal reference system centered in $\mathbf { b } _ { 0 }$ , with the $x _ { 1 }$ axis directed along the Laplace–Lenz vector $\mathbf { e }$ and the $z _ { 1 }$ axis along the direction $\hat { \mathbf { c } } _ { 1 }$ of the angular momentum of $\mathbf { b } _ { 1 }$ , the coordinates of the Keplerian orbit are

$$
{ \left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] } = { \left[ \begin{array} { l } { r \cos v } \\ { r \sin v } \\ { 0 } \end{array} \right] } , \quad r = { \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos v } } .
$$

By rotating this vector around the angular momentum axis by an angle $\omega$

$$
{ \left[ \begin{array} { l } { x _ { 2 } } \\ { y _ { 2 } } \\ { z _ { 2 } } \end{array} \right] } = R _ { \omega { \hat { \mathbf { c } } } _ { 1 } } { \left[ \begin{array} { l } { x _ { 1 } } \\ { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right] } = { \left[ \begin{array} { l } { r \cos ( v + \omega ) } \\ { r \sin ( v + \omega ) } \\ { 0 } \end{array} \right] }
$$

we have the $x _ { 2 }$ axis along the ascending node $\hat { \bf N } = ( \hat { \bf z } \times \hat { \bf c } _ { 1 } ) / \sin I$ . Rotating by an angle $I$ around $\hat { \bf N }$

$$
\left[ \begin{array} { l } { x _ { 3 } } \\ { y _ { 3 } } \\ { z _ { 3 } } \end{array} \right] = R _ { I \hat { \bf N } } \left[ \begin{array} { l } { x _ { 2 } } \\ { y _ { 2 } } \\ { z _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { r \cos ( v + \omega ) } \\ { r \sin ( v + \omega ) \ \cos I } \\ { r \sin ( v + \omega ) \ \sin I } \end{array} \right]
$$

and finally, rotating by an angle $\Omega$ around the $\hat { \mathbf { z } }$ axis, we obtain the vector $\mathbf { b } _ { 1 }$ , but this is not necessary because $z = z _ { 3 }$ . In conclusion the observable radial velocity of the star is

$$
\dot { \bf r } _ { 0 } \cdot \hat { \bf z } = \dot { \bf b } _ { 0 } \cdot \hat { \bf z } - \mu _ { 1 } \dot { z } = \dot { z } _ { 0 } - \mu _ { 1 } \sin I \ \frac { d } { d t } \left[ r \sin ( v + \omega ) \right] ,
$$

with time derivative

$$
{ \frac { d } { d t } } \left[ r \sin ( v + \omega ) \right] = { \dot { r } } \ \sin ( v + \omega ) + r \ { \dot { v } } \ \cos ( v + \omega )
$$

where $\dot { v }$ is obtained from the angular momentum $c _ { 1 }$

$$
= \frac { c _ { 1 } } { r ^ { 2 } } = \sqrt { G M _ { 0 } a \left( 1 - e ^ { 2 } \right) } \frac { ( 1 + e \cos v ) ^ { 2 } } { [ a \left( 1 - e ^ { 2 } \right) ] ^ { 2 } } = \frac { n } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( 1 + e \cos v \right) ^ { 2 }
$$

$$
r \dot { v } = \frac { n a } { \sqrt { 1 - e ^ { 2 } } } \left( 1 + e \cos v \right)
$$

and $\dot { r }$ is obtained from the derivative of the conic section equation

$$
\dot { r } = \frac { a ( 1 - e ^ { 2 } ) } { ( 1 + e \cos v ) ^ { 2 } } e \sin v \dot { v } = \frac { n a } { \sqrt { 1 - e ^ { 2 } } } e \sin v .
$$

Then

$$
{ \frac { d } { d t } } \left[ r \sin ( v + \omega ) \right] = { \frac { n a } { \sqrt { 1 - e ^ { 2 } } } } \ \left[ \cos ( v + \omega ) + e \cos \omega \right] ,
$$

$$
\dot { { \bf r } } _ { 0 } \cdot \hat { { \bf z } } = \dot { z } _ { 0 } - \frac { \mu _ { 1 } \sin I n a } { \sqrt { 1 - e ^ { 2 } } } ~ [ \cos ( v + \omega ) + e \cos \omega ]
$$

is the observable as an explicit function of the orbital elements, dependent upon time only through the true anomaly $\boldsymbol { v }$ .

# Circular approximation

If we assume a circular orbit ( $e = 0$ ) then $\dot { v } = n$ , $\omega$ is just a phase, and

$$
\begin{array} { r l r } & { } & { \dot { \bf r } _ { 0 } \cdot \hat { \bf z } = \dot { z } _ { 0 } - K \cos ( v + \omega ) = \dot { z } _ { 0 } + ( - K \cos \omega ) \cos v + ( K \sin \omega ) \sin v , } \\ & { } & { \mathrm { w h e r e } \quad \qquad K = \mu _ { 1 } \sin I n a = \frac { G ^ { 1 / 3 } n ^ { 1 / 3 } m _ { 1 } \sin I } { M _ { 0 } ^ { 2 / 3 } } \quad \quad } \end{array}
$$

is a constant depending upon the masses $m , m _ { 1 }$ , the mean motion $n$ , and the inclination $I$ . If we have measured the mean motion $n$ as the main frequency of the signal, then eq. (6.11) is a linear model (Section 5.1) with three constants $k _ { 1 } = \dot { z } _ { 0 } , k _ { 2 } = - K \cos \omega , k _ { 3 } = K \sin \omega$ to be fitted.

If the observations were available for every time $t$ this would be the simplest problem of Fourier analysis, but in practice the observations are given at times sampled in a non-uniform way (only during the nights) and over a finite time span. Let the $m$ observations $\dot { \mathbf { r } } = \left( \dot { r } _ { i } \right)$ be at times $\mathbf { t } = \left( t _ { i } \right)$ and let us assemble the vectors of values $\cos { \mathbf { v } } = \cos ( v ( t _ { i } ) )$ , $\sin \mathbf { v } = \sin ( v ( t _ { i } ) )$ :

$$
\begin{array} { r c l } { { \pmb \xi } } & { { = } } & { { { \dot { \bf r } } - k _ { 1 } { \bf 1 } - k _ { 2 } \cos { \bf v } - k _ { 3 } \sin { \bf v } , } } \\ { { { \cal B } } } & { { = } } & { { \displaystyle \frac { \partial \pmb \xi } { \partial ( k _ { 1 } , k _ { 2 } , k _ { 3 } ) } = - [ { \bf 1 } \cos { \bf v } \sin { \bf v } ] . } } \end{array}
$$

If cos $\mathbf { v } \cdot \mathbf { 1 } = \sin \mathbf { v } \cdot \mathbf { 1 } = \cos \mathbf { v } \cdot \sin \mathbf { v } = 0$ the normal matrix is diagonal and the solution is

$$
k _ { 1 } = { \bar { r } } = { \frac { 1 } { m } } \sum _ { i = 1 } ^ { m } { \dot { r } } _ { i } , \quad k _ { 2 } = { \frac { { \dot { \mathbf { r } } } \cdot \cos \mathbf { v } } { \cos \mathbf { v } \cdot \cos \mathbf { v } } } , \quad k _ { 3 } = { \frac { { \dot { \mathbf { r } } } \cdot \sin \mathbf { v } } { \sin \mathbf { v } \cdot \sin \mathbf { v } } } .
$$

Moreover, if the data points are evenly distributed with respect to the phase of the signal sinusoidal terms, then $\cos \mathbf { v } \cdot \cos \mathbf { v } \simeq \sin \mathbf { v } \cdot \sin \mathbf { v } \simeq m / 2$ and the least squares solution is given by the classical Fourier analysis formulae, the integrals being replaced by finite sums over the available data points. In practice the base vectors are not orthogonal, the normal matrix is full and it has to be inverted. A solution could be obtained by Gram–Schmidt orthonormalization of the three vectors $\mathbf { 1 } , \cos { \mathbf { v } } , \sin { \mathbf { v } }$ (Ferraz-Mello 1981). If the time span of observations is not much longer than the period $2 \pi / n$ , the correlations between the constant and the sine wave are large and the solution is significantly different from the one obtained by the Fourier analysis formulae.

Anyway the result is that the radial velocity $\dot { z } _ { 0 }$ of the center of mass, the phase $\omega$ , and the amplitude $K$ can be independently determined. The problem is that, even assuming $n$ is known, $K$ contains three parameters $m _ { 1 } , m _ { 0 } , \sin I$ . Let us assume the mass of the star is measured independently from the spectrum, using the Hertzsprung–Russel relationship between color and mass, and let us approximate $M _ { 0 } \simeq m _ { 0 }$ . 7 Then only the product $m _ { 1 } \sin I$ appears in the signal. Inspection of eq. (6.10) shows that this has nothing to do with the circular orbit approximation, but is an intrinsic property of the observable radial velocity.

# First order in eccentricity

A solution applicable to eccentric orbits, but approximated by neglecting the terms of degree two in eccentricity, can be obtained by truncation from the formula for the time derivative of the true anomaly $\boldsymbol { v }$

$$
{ \frac { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } { 1 + e \cos v ) ^ { 2 } } } \stackrel { \cdot } { v } = n \Longrightarrow l = n ( t - t _ { 0 } ) = \int _ { 0 } ^ { v } \left( 1 - 2 e \cos v \right) d v + \mathcal { O } ( e ^ { 2 } )
$$

providing an approximate expression for the mean anomaly $l$

$$
v - 2 e \sin v + \mathcal { O } ( e ^ { 2 } ) = l
$$

and the inverse formula

$$
v = l + 2 e \sin l + \mathcal { O } ( e ^ { 2 } )
$$

implying

$$
\begin{array} { r } { \mathrm { ~ \ i ~ } v = \sin l + e \sin ( 2 l ) + \mathcal { O } ( e ^ { 2 } ) , \quad \cos v = \cos l + e \cos ( 2 l ) - e + \mathcal { O } ( e ^ { 2 } ) . } \end{array}
$$

Substituting into $\cos ( v + \omega )$ we obtain, neglecting $\mathcal { O } ( e ^ { 2 } )$ terms,

$$
\dot { \bf r } _ { 0 } \cdot \hat { \bf z } = \dot { z } _ { 0 } - \mu _ { 1 } \sin I n a ~ [ \cos ( l + \omega ) + e \cos ( 2 l + \omega ) ]
$$

and the signal appears as a constant plus two trigonometric terms, with frequencies $n$ and $2 n$ and phase constants $- n t _ { 0 } + \omega$ , $- 2 n t _ { 0 } { + } \omega$ , respectively. Assuming $n$ is known from frequency analysis, this suggests using a linear model with five base functions and five coefficients $k _ { i } , ~ i = 1 , 5$ :

$$
{ \dot { \bf r } } _ { 0 } \cdot { \hat { \bf z } } = k _ { 1 } + k _ { 2 } \cos ( n t ) + k _ { 3 } \sin ( n t ) + k _ { 4 } \cos ( 2 n t ) + k _ { 5 } \sin ( 2 n t ) .
$$

Thus it is possible to find a linear least squares solution for these parameters, determining $e , \omega , m _ { 1 } \sin I , t _ { 0 }$ and $\dot { z } _ { 0 }$ ; $a$ is determined from $n$ (again assuming $m _ { 0 }$ is known, and approximating $M _ { 0 } \simeq m _ { 0 }$ ). The orbital element $\Omega$ cannot be determined at all, and the mass $m _ { 1 }$ cannot be entangled from the orbit plane parameter $\sin I$ . Thus, if the problem were posed with eight parameters to be solved $( a , e , I , \Omega , \omega , t _ { 0 } , \dot { z } _ { 0 } , m _ { 1 } )$ there would be a rank deficiency of 2. Again, this is not due to the first-order truncation in $e$ .

# Rank deficiency of the exoplanet problem

In this problem there is an exact symmetry, even without any truncation to some power of $e$ : the rotations of the exoplanetary system around the $z$ axis $R _ { s \hat { \mathbf { z } } }$ , for each rotation angle $s$ , leave the $z$ component of $\dot { \mathbf { r } } _ { 0 }$ unchanged, thus the residuals are exactly the same. The effect of such rotation in the orbital elements, given that the inclination is measured with respect to the plane parallel to $( x , y )$ passing through the star, is simply $\Omega \longrightarrow \Omega + s$ . Thus $\partial \pmb { \xi } / \partial \Omega = \mathbf { 0 }$ , that is, if $\Omega$ is included in the list of parameters to be solved, the matrix $B$ has one column of zeros, and the normal matrix $C = B ^ { T }$ $B$ has one row and one column of zeros. This problem is easily solved by descoping, that is by determining a list of parameters not including $\Omega$ .

In the approximation $M _ { 0 } \simeq m _ { 0 }$ the observables of eq. (6.10) contain $m _ { 1 }$ and $\sin I$ only through their product $m _ { 1 } \sin I$

$$
m _ { 1 } \ \frac { \partial \pmb { \xi } } { \partial m _ { 1 } } = \sin I \ \frac { \partial \pmb { \xi } } { \partial ( \sin I ) } ,
$$

thus two rows of the matrix $B$ are always linearly dependent and there is one additional rank deficiency. A vector $\mathbf { v }$ satisfying $B { \textbf { v } } = \mathbf { 0 }$ is

$$
\mathbf { v } = \sin I \nabla ( m _ { 1 } ) + m _ { 1 } \nabla ( \sin I )
$$

where $\nabla ( m _ { 1 } )$ , $\nabla ( \sin I )$ are vectors pointing in the direction of change of $m _ { 1 }$ , $\sin I$ , respectively.

Again descoping is the only solution, that is the parameter to be solved is just the product $m _ { 1 } \sin I$ . This has a serious implication due to the fact that an extrasolar planet is, by definition, not a companion star. Thus to prove that an extrasolar system contains a planet it is necessary to provide an upper limit for the mass (e.g., 13 times the mass of Jupiter is estimated to be the lower mass limit for deuterium fusion, thus for a body shining by its own radiation). If only the combination $m _ { 1 }$ $\sin I$ is constrained by the observations, there is often no way to exclude a very low value of $I$ and a large mass. In some cases it is possible to exclude a low $I$ because partial occultations of the star by the planet are observable.

# Exoplanetary systems

The rank deficiencies described above can be found also in an extrasolar planetary system with more than one planet. Let us suppose there is a star and two planets, with masses $m , m _ { 1 } , m _ { 2 }$ and let $\mathbf { b } _ { 0 } , \mathbf { b } _ { 1 } , \mathbf { b } _ { 2 }$ be their positions in barycentric coordinates. Then the observable is

$$
\dot { \bf r } _ { 0 } \cdot \hat { \bf z } = [ \dot { \bf b } _ { 0 } + \dot { \bf s } ] \cdot \hat { \bf z }
$$

with the barycentric star position

$$
{ \bf s } = - { \frac { m _ { 1 } } { M _ { 0 } } } { \bf b } _ { 1 } - { \frac { m _ { 2 } } { M _ { 0 } } } { \bf b } _ { 2 } ,
$$

where $M _ { 0 }$ is the total mass. The rotations $R _ { s \hat { \mathbf { z } } }$ around the line of sight are exact symmetries of the equation of motion. If the two planets are

parameterized by Keplerian orbital elements $( a _ { j } , e _ { j } , I _ { j } , \Omega _ { j } , \omega _ { j } , v _ { j } ) , ~ j = 1 , 2$ , the effect of $R _ { s \hat { \mathbf { z } } }$ is $\Omega _ { j }  \Omega _ { j } + s$ . Thus a rank deficiency occurs with

$$
\frac { \partial \pmb { \xi } } { \partial \Omega _ { 1 } } + \frac { \partial \pmb { \xi } } { \partial \Omega _ { 2 } } = \mathbf { 0 } .
$$

The solution is to remove $\Omega _ { 1 }$ and $\Omega _ { 2 }$ from the list of parameters, replacing them with $\Omega _ { 2 } - \Omega _ { 1 }$ . However, even after this descoping by one parameter the system still has some approximate rank deficiencies, resulting from the smallness of the mass ratios $m _ { 1 } / m _ { 0 }$ , $m _ { 2 } / m _ { 0 }$ . If we were to neglect the mutual perturbations of the two planets (both direct and indirect), by using eq. (6.10) for each of the two planets we obtain

$$
\dot { \bf r } _ { 0 } \cdot \hat { \bf z } = \dot { z } _ { 0 } - \sum _ { j = 1 } ^ { 2 } \frac { m _ { j } \sin I _ { j } n _ { j } a _ { j } } { ( m _ { 0 } + m _ { j } ) \sqrt { 1 - e _ { j } ^ { 2 } } } \left[ \cos ( v _ { j } + \omega _ { j } ) + e _ { j } \cos \omega _ { j } \right]
$$

with $n _ { j } = \sqrt { G m _ { 0 } / a _ { j } ^ { 3 } }$ . Then both angles $\Omega _ { j }$ do not appear and the inclinations appear only in the combinations $m _ { j } / ( m _ { 0 } + m _ { j } ) \sin I _ { j }$ . If we were trying to solve for 15 parameters ( $2 \times 6$ orbital elements plus $m _ { 1 } , m _ { 2 } , { \dot { z } } _ { 0 } )$ the normal matrix would have rank 11.

The equation of motion for a three-body system in barycentric coordinates can be described as two two-body systems with perturbing accelerations containing the planetary masses $m _ { 1 } , m _ { 2 }$ . We define an adimensional small parameter $\mu = ( m _ { 1 } + m _ { 2 } ) / m _ { 0 }$ , which is contained in all perturbation terms. Then the short periodic perturbations of the two two-body subsystems are $\mathcal O ( \mu )$ and the perturbations in the observable due to these perturbations are $\scriptstyle \mathcal { O } ( \mu ^ { 2 } )$ . Hence the observable is $\dot { z } _ { 0 } + \mathcal { O } ( \mu ) + \mathcal { O } ( \mu ^ { 2 } )$ , the second-order part depending only upon the perturbations. Thus the coupling between two (or more) planets is an example of symmetry breaking with small parameter $\mu$ , and there is an approximate rank deficiency of order 3, with $\epsilon = \mathcal { O } ( \mu )$ ; however, an explicit computation of $\epsilon$ is not easy. The practical rule of thumb is that an observation time span of the order of $1 / \mu$ periods of the planets is required to determine $m _ { 1 } , m _ { 2 } , I _ { 1 } , I _ { 2 }$ in a robust way.8

# 6.6 Planetary systems: the Solar System

The orbits of the major planets of our Solar System can be the subject of orbit determination. From the discussion in Section 4.6, at least the eight major planets have significant interactions, thus their orbits need to be solved at once, with all their masses among the fit parameters. Some of the major satellites (especially the Moon) and the largest asteroids need to be taken into account. To control the complexity of the problem, it is possible to decouple the orbit determination for some satellites and asteroids.

# Symmetries

This orbit determination problem has symmetries and rank deficiencies depending upon the set of available observations. If the observations are only relative, between planets of our Solar System (e.g., if all the observations are from Earth), then all observables, be they either angles or distances between planets or their derivatives, are exactly symmetric with respect to the rotation group $S O ( 3 )$ . Thus it is essential to add three a priori constraints, that is to select an inertial reference system (see Appendix C).

If the observations are absolute, connected to some extrasolar inertial reference system, e.g., angles relative to “fixed stars” (in practice, a nonrotating astrometric catalog of stars), then the $S O ( 3 )$ symmetry disappears. If there are only angular observations the change of scale defined in Section 4.1 is an exact symmetry and rank deficiency of order 1 occurs. Thus the classical results on the orbit determination of the planets were only expressed in terms of a unit of length, the astronomical unit (AU), whose value in terrestrial units could not be accurately determined.9

The current state-of-the-art is more complex. Both absolute angular observations of the planets (with respect to star catalogs) and relative range/ range-rate observations are available. The latter are obtained by planetary radar, by Lunar laser ranging, by tracking landers on other planets, by the orbit determination of artificial satellites of other planets. In general, range observations are more accurate than angular observations, although there has been progress also in the latter. For example, in the case study of Chapter 17 the accuracy in range is expected to be 10 cm over a distance $\simeq ~ 1$ AU, with a relative accuracy $< 1 0 ^ { - 1 2 }$ . Thus there is an approximate $S O ( 3 )$ symmetry, in that the angular observations are by far less accurate.

The translations of the barycenter $\mathbf { b } _ { 0 }$ (see Section 4.3) do not affect observations between Solar System bodies. To remove the corresponding exact rank deficiency we can use an equation of motion in barycentric coordinates (4.16) with a priori constraints $\mathbf { b } _ { 0 } = \dot { \mathbf { b } } _ { 0 } = \mathbf { 0 }$ : the coordinates of the Sun are eliminated, being computed from (4.15).

# Relativistic effects

A full discussion of the complex problem of the planetary ephemerides is beyond the scope of this book. We would like to mention one key feature, which will be needed in Chapter 17. The equation of motion for the planets to be used for orbit determination, given the current observational accuracy, is not just that of the $N$ -body problem, but has to be fully compliant with general relativity. Also the observation functions have to be fully relativistic, taking into account the non-Newtonian properties of light propagation in a curved space-time, and the space-time coordinates have to be selected with care and computed with accurate transformation equations. We have used two simulations of an orbit determination experiment for a

![](images/7faf0535d9978069e4f00a48ac43bf8b85b6d90467fc5a977eb96a5705ee5ad7.jpg)  
Fig. 6.1. The relativistic signal in range (including dynamics and Shapiro effect) from a Mercury orbiter over a 1-year mission has a peak-to-peak amplitude of $\simeq 9 0 0 ~ \mathrm { k m }$ , with $\mathrm { S / N } \simeq 9 \times 1 0 ^ { 6 }$ (assuming the accuracy of the experiment described in Chapter 17). In range-rate the peak-topeak signal is $\simeq 1 ~ \mathrm { m / s }$ with $\mathrm { S } / \mathrm { N } \simeq 3 \times 1 0 ^ { 5 }$ .

Mercury orbiter, one with a pure Newtonian $N$ -body model for the orbits of the planets, the other with a fully relativistic model. The differences plotted in Figure 6.1 show that, with state-of-the-art tracking systems, there is a very large signal-to-noise ratio in the relativistic effects.

There is no way to really explain general relativity in short. We shall give the equation of motion by using the parametric post-Newtonian approach: the relativistic equation of motion is linearized with respect to the small parameters $v _ { i } ^ { 2 } / c ^ { 2 }$ and $G m _ { i } / r _ { i k }$ , where $v _ { i }$ is the barycentric velocity for each of the bodies of mass $m _ { i }$ , $c$ is the speed of light, and $r _ { i k }$ is a mutual distance, appearing in the metric of the curved space-time, hence in the equations for geodesic motion. This can be formalized by adding to the Lagrangian $L _ {  { \mathit { N E W } } }$ of the $N$ -body problem, given in eq. (4.2), some corrective terms of post-Newtonian (PN) order 1 in the small parameters

$$
L = L _ { N E W } + L _ { G R } .
$$

By using the notation (Moyer 2003)

$$
\begin{array} { r c l } { \mathbf { r } _ { i j } } & { = } & { \mathbf { r } _ { j } - \mathbf { r } _ { i } , \quad r _ { i j } = \left| \mathbf { r } _ { i j } \right| } \\ { \mathbf { v } _ { i j } } & { = } & { \dot { \mathbf { r } _ { j } } - \dot { \mathbf { r } _ { i } } = \mathbf { v } _ { j } - \mathbf { v } _ { i } , \quad v _ { i j } = \left| \mathbf { v } _ { i j } \right| , } \end{array}
$$

$L _ { G R }$ can be written in a synthetic way as

$$
\begin{array} { r c l } { { { \cal L } _ { G R } } } & { { = } } & { { \displaystyle { \frac { 1 } { 8 c ^ { 2 } } } \sum _ { i } m _ { i } v _ { i } ^ { 4 } - { \frac { 1 } { 2 c ^ { 2 } } } \sum _ { i } \sum _ { j \neq i } \sum _ { k \neq i } { \frac { G ^ { 2 } m _ { i } m _ { j } m _ { k } } { r _ { i j } r _ { i k } } } } } \\ { { } } & { { } } & { { \displaystyle { + { \frac { 1 } { 2 c ^ { 2 } } } \sum _ { i } \sum _ { j \neq i } { \frac { G m _ { i } m _ { j } } { r _ { i j } } } } } } \\ { { } } & { { } } & { { \displaystyle { \times \left[ { \frac { 3 } { 2 } } ( v _ { i } ^ { 2 } + v _ { j } ^ { 2 } ) - { \frac { 7 } { 2 } } ( { \bf v } _ { i } \cdot { \bf v } _ { j } ) - { \frac { 1 } { 2 r _ { i j } ^ { 2 } } } ( { \bf r } _ { i j } \cdot { \bf v } _ { i } ) \left( { \bf r } _ { i j } \cdot { \bf v } _ { j } \right) \right] } . } } \end{array}
$$

If the observations are between bodies of the Solar System, including space probes, the position and velocity of the Sun have to be constrained by the barycenter integrals to avoid an exact rank deficiency of order 6. However, the integrals for the Lagrangian system defined by $L$ are different from the ones of $L _ {  { \mathit { N E W } } }$ : by using the translations group of symmetries and Noether’s theorem we get a relativistic total linear momentum $\mathbf { p }$ :

$$
= \sum _ { i } { \frac { \partial L } { \partial \mathbf { v } _ { i } } } = \sum _ { i } m _ { i } \mathbf { v } _ { i } \left[ 1 + { \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { i } } { 2 c ^ { 2 } } } \right] - { \frac { 1 } { 2 c ^ { 2 } } } \sum _ { i } \sum _ { j \neq i } { \frac { G m _ { i } m _ { j } } { r _ { i j } ^ { 3 } } } \left( \mathbf { r } _ { i j } \cdot \mathbf { v } _ { j } \right)
$$

where $\begin{array} { r } { U _ { i } = \sum _ { k \neq i } ~ G m _ { k } / r _ { i k } } \end{array}$ is the potential at the $i$ -th body, neglecting terms of PN order 2. We have $\dot { \mathbf { p } } = \mathbf { 0 }$ , thus $\mathbf { p }$ is a vector integral. The vector

$$
\mathbf { P } = \sum _ { i } m _ { i } \mathbf { r } _ { i } \left[ 1 + { \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { i } } { 2 c ^ { 2 } } } \right]
$$

has the property, again neglecting $\mathcal { O } ( v ^ { 4 } / c ^ { 4 } )$ , that $\dot { \mathbf { P } } = \mathbf { p }$ , thus it moves in a linear uniform way like the Newtonian center of mass. A relativistic center

of mass can be defined as

$$
\mathbf { \mathbf { b } } _ { 0 } = { \frac { \sum _ { i } m _ { i } \mathbf { r } _ { i } \left[ 1 + { \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { i } } { 2 c ^ { 2 } } } \right] } { \sum _ { i } m _ { i } \left[ 1 + { \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { i } } { 2 c ^ { 2 } } } \right] } }
$$

where the denominator, neglecting PN order 2 terms, is $\textstyle \sum _ { i } m _ { i } + H / c ^ { 2 }$ , with $H$ the Hamiltonian, and it is also an integral. Thus we can use the constraint ${ \bf b } _ { 0 } = \dot { \bf b } _ { 0 } = { \bf 0 }$ to reduce the dimensionality of the vector of parameters to be solved: the position and velocity of the Sun can be eliminated from the equation of motion and computed from those of the other bodies by

$$
\mathbf { r } _ { 0 } = { \frac { - \sum _ { i \neq 0 } m _ { i } \mathbf { r } _ { i } \left[ 1 + { \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { i } } { 2 c ^ { 2 } } } \right] } { m _ { 0 } \left( 1 + { \frac { v _ { 0 } ^ { 2 } } { 2 c ^ { 2 } } } - { \frac { U _ { 0 } } { 2 c ^ { 2 } } } \right) } } .
$$

With this Lagrangian formalism, the relativistic equation of motion at the post-Newtonian order 1 are well defined and can be used for orbit determination of the planets, also of interplanetary space probes. Moreover, with state-of-the-art interplanetary tracking data, given the very large S/N ratio of the relativistic effects as shown in Figure 6.1, it is possible to test general relativity to great accuracy. The same formalism allows us to parameterize the equation of motion (and other relativistic effects) with constants having fixed values in Einstein’s theory, and to solve for their value, together with the initial conditions and instrumental parameters, in the orbit determination procedure. One such post-Newtonian parameter $\gamma$ , with value 1 in general relativity, controls how the space-time curvature depends upon the gravitational potential energy. A deviation from general relativity can be introduced with velocity-dependent terms

$$
L _ { \bar { \gamma } } = \frac { \bar { \gamma } } { 2 c ^ { 2 } } \sum _ { i } \sum _ { j \neq i } \frac { G m _ { i } m _ { j } } { r _ { i j } } v _ { i j } ^ { 2 } ,
$$

where $\bar { \gamma } ~ = ~ \gamma ~ - ~ 1$ . The Eddington parameter $\beta$ , equal to 1 in general relativity, appears in the three-body interactions, thus a violation can be introduced with

$$
{ \cal L } _ { \bar { \beta } } = - { \frac { \bar { \beta } } { c ^ { 2 } } } \sum _ { i } \sum _ { j \neq i } \sum _ { k \neq i } { \frac { G ^ { 2 } m _ { i } m _ { j } m _ { k } } { r _ { i j } r _ { i k } } } ,
$$

where $\beta = \beta - 1$ . In the general relativity theory of Einstein the only free parameter is $G$ , which is constant ( $\dot { G } = 0$ ); nevertheless, the product $G m _ { 0 }$ changes because of the mass shed by the Sun as radiation and charged

particles, see Section 4.6. This effect can be included in the dynamical model by the Lagrangian term

$$
L _ { \zeta } = ( t - t _ { 0 } ) \zeta \sum _ { i \neq 0 } { \frac { G m _ { 0 } m _ { i } } { r _ { i 0 } } } , ~ \zeta = { \frac { d ( G m _ { 0 } ) / d t } { G m _ { 0 } } } ,
$$

where $t _ { 0 }$ is a reference epoch for $m _ { 0 }$ . For an accurate orbit determination of Mercury, the non-spherical shape of the rotating Sun does matter, since $r _ { 1 0 } / R _ { \odot } \simeq 9 0 0$ : the corresponding Lagrangian term $L _ { J 2 \odot }$ is the zonal spherical harmonic of degree 2 of the Sun, with respect to the rotation axis of the Sun, see Section 13.2. Thus the equation of motion has to be deduced from the Lagrangian

$$
{ \cal L } = { \cal L } _ { N E W } + { \cal L } _ { G R } + { \cal L } _ { \bar { \gamma } } + { \cal L } _ { \bar { \beta } } + { \cal L } _ { \zeta } + { \cal L } _ { J 2 \odot } .
$$

Equation (6.14) for the total linear momentum does not change for the added terms, because the $\partial L _ { \gamma } / \partial \mathbf { v } _ { i }$ cancel in the sum $( \textstyle \sum _ { i } \partial L _ { \gamma } / \partial \mathbf { v } _ { i } = \mathbf { 0 } _ { \gamma }$ ), the other three terms do not depend upon the velocities, thus the equation (6.17) for the Sun is not changed.

Lagrangian terms can describe other violations, e.g., the violations of the strong equivalence principle and preferred frame effects (see Section 17.5). A violation of the equivalence principle is obtained by assuming that in the Newtonian Lagrangian $L _ { N E W }$ the gravitational masses $m _ { i } , m _ { j }$ , as they appear in the potential terms $G m _ { i } m _ { j } / r _ { i j }$ , are not the same as the inertial masses $m _ { j } ^ { I }$ appearing in the kinetic energy terms $m _ { j } ^ { I } v _ { j } ^ { 2 } / 2$ . The difference may depend upon the composition of the mass $m _ { j }$ , e.g., the fraction of the mass which results from the rest mass, from nuclear binding energy, from gravitational self-energy. While the dependence upon the nuclear binding energy has been excluded by laboratory experiments to very great accuracy (better than $1 0 ^ { - 1 2 }$ ), the dependence on gravitational self-energy is difficult to test because this fraction is very small for all bodies we can use: even for the Sun the fraction is $\Omega _ { 0 } \simeq - 3 . 5 2 \times 1 0 ^ { - 6 }$ . If we assume $m _ { 0 } ^ { I } = m _ { 0 } \left[ 1 - \eta \Omega _ { 0 } \right]$ , the parameter $\eta$ can be tested by orbit determination. However, in the equation of motion for the planets in barycentric coordinates the inertial mass of the Sun $m _ { 0 } ^ { I }$ does not appear directly. The change occurs in the integral of the center of mass, where $m _ { 0 }$ is replaced by $m _ { 0 } ^ { I }$ , resulting in a modified equation for the coordinates of the Sun

$$
{ \bf r } _ { 0 } = \frac { - \sum _ { i \neq 0 } m _ { i } { \bf r } _ { i } \left[ 1 + \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } - \frac { U _ { i } } { 2 c ^ { 2 } } \right] } { m _ { 0 } \left[ 1 - \eta \Omega _ { 0 } \right] \left( 1 + \frac { v _ { 0 } ^ { 2 } } { 2 c ^ { 2 } } - \frac { U _ { 0 } } { 2 c ^ { 2 } } \right) } .
$$

The indirect perturbation from this displacement of the Sun affects the

orbits of the other bodies: ${ \partial \ddot { \mathbf { r } } _ { j } } / { \partial \eta } \neq \mathbf { 0 }$ contains $\Omega _ { 0 } m _ { k }$ for each $k \neq 0$ , the contribution of Jupiter is as large as that of all the other planets together.

To model preferred frame effects requires us to add to the Lagrangian

$$
\begin{array} { c } { { { \cal L } _ { \alpha } = \displaystyle \frac { \alpha _ { 2 } - \alpha _ { 1 } } { 4 c ^ { 2 } } \sum _ { j } \sum _ { i \neq j } \frac { G m _ { i } m _ { j } } { r _ { i j } } \left( { \bf v } _ { i } + { \bf w } \right) \cdot \left( { \bf v } _ { j } + { \bf w } \right) } } \\ { { \displaystyle ~ - \frac { \alpha _ { 2 } } { 4 c ^ { 2 } } \sum _ { j } \sum _ { i \neq j } [ { \bf r } _ { j i } \cdot \left( { \bf v } _ { j } + { \bf w } \right) ] \left[ { \bf r } _ { j i } \cdot \left( { \bf v } _ { i } + { \bf w } \right) \right] \frac { G m _ { i } m _ { j } } { r _ { i j } ^ { 3 } } } } \end{array}
$$

with two additional post-Newtonian parameters $\alpha _ { 1 } , \alpha _ { 2 }$ and with w the velocity of the Solar System barycenter with respect to the preferred frame, usually assumed to be that of the cosmic microwave background, thus $| \mathbf { w } | = 3 7 0 \pm 1 0 ~ \mathrm { k m / s }$ in the direction $( \alpha , \delta ) = ( 1 6 8 ^ { \circ } , 7 ^ { \circ } )$ .

The problem arises from the presence of additional terms in the total linear momentum integral $\mathbf { p }$ : the Lagrangian $L + L _ { \alpha }$ , where $L$ is from eq. (6.18), is still invariant by translation. The integral from Noether’s theorem is

$$
\sum _ { i } { \frac { \partial ( L + L _ { \alpha } ) } { \partial \mathbf { v } _ { i } } } = \mathbf { p } + \sum _ { i } { \frac { \partial L _ { \alpha } } { \partial \mathbf { v } _ { i } } }
$$

with $\mathbf { p }$ from eq. (6.14). This integral is not the derivative of $\mathbf { P }$ and this cannot be fixed by changing the definition, that is, a center of mass integral does not exist (Will 1981, Section 4.4). A possible solution to formulate in a consistent way the equation of motion with preferred frame effects is still to use a reference system centered in $\mathbf { b } _ { 0 }$ as defined in eq. (6.15), which is however accelerated by

$$
\ddot { \bf b } _ { 0 } = - \frac { \frac { d } { d t } \sum _ { i } \frac { \partial { \cal L } _ { \alpha } } { \partial { \bf v } _ { i } } } { \sum _ { i } m _ { i } \left[ 1 + \frac { v _ { i } ^ { 2 } } { 2 c ^ { 2 } } - \frac { U _ { i } } { 2 c ^ { 2 } } \right] } ,
$$

and the equation of motion is the Lagrange equation with Lagrangian $L + L _ { \alpha }$ , with the additional “apparent acceleration” $- \ddot { \mathbf { b } } _ { 0 }$ .

There are many other possibilities of violations of the fundamental laws of gravitation and of inertia, including violations of the conservation of total linear momentum, of total angular momentum, and of total energy, and also violations of the action–reaction law, but most of these appear unlikely. Thus a list of parameters to be solved including $\gamma , \beta , \zeta , J _ { \mathrm { 2 \odot } } , \eta , \alpha _ { 1 } , \alpha _ { 2 }$ can be appropriate for a test of the theory of gravitation based on Solar System orbit determination. More on this subject is explained in Chapter 17.

# Part III

# Population Orbit Determination

#

# THE IDENTIFICATION PROBLEM

The identification problem is the attempt to find, among independent detections of celestial bodies, those belonging to the same physical object. The problem becomes more difficult as the population of observed objects increases (see Chapter 11). This chapter is based on (Milani 1999, Milani et al. 2000a, Milani et al. 2001a) and ongoing research. The main example is the population of small Solar System bodies. Most of the observable ones are asteroids, although the observed population contains a smaller fraction of comets and others. We will use the word asteroid in the following discussion, although it applies also to the other populations.

An asteroid is typically observed only over a time span of a few hours to a few weeks, and is bright enough to be visible only over the apparition, a time interval spanning at most a few months. If this time span is not exploited in full, the single apparition orbit determination either is impossible or results in a rapidly growing prediction uncertainty: by the time of the next apparition the asteroid could be in a portion of the sky larger than the field of view of the telescopes available for the recovery. Thus we have a lost asteroid, that is, it is more likely to be rediscovered by chance than by looking at the predicted position. The databases of detected Solar System objects contain many single apparition arcs: the goal is to join together those of the same object, allowing for an accurate orbit determination.

# 7.1 Classification of the problem

The identification problem deals with separate sets of observations, which might, and might not, belong to the same object. As a basic form of the problem, we assume that these observations are partitioned into exactly two arcs, and that the observations of the same arc are of the same object.1

# Orbit identification

The problem can be classified as orbit identification when the observations of both arcs are sufficient to separately solve for two least squares orbits, one for each arc: then the input data include two sets of orbital elements, with their covariance matrices and residuals. The identification is confirmed if the observations from both arcs can be fitted to a single orbit.

To test two given orbits for possible identification is not simple, because of the strong nonlinearity of the orbit determination problem: we need a first guess orbit to start the differential corrections procedure. Nevertheless, this basic problem is much less difficult than the global problem: given a catalog containing $N$ short arc orbits, we want to know which of the $N ( N - 1 ) / 2$ couples belong to the same object, and how to compute a catalog of all the orbits of the physically distinct objects. With the modern catalogs including hundreds of thousands of orbits, and the next-generation surveys expected to discover tens of millions of objects, such a problem could lead to unacceptable computational complexity, unless it is tackled with a smart algorithm. Thus there are three steps in the orbit identification problem:

(i) to propose identifications, by selecting a small subset of couples; (ii) to compute a preliminary orbit as first guess for each couple in (i); (iii) to iterate differential corrections for each couple of arcs together, checking convergence to an orbit solution with acceptable residuals.

# Attribution

The identification problem can be classified as attribution when an amount of data insufficient to compute a unique orbit for one arc (e.g., two twodimensional observations, that is $m = 4$ ) is compared to an orbit already computed for the other arc. Not enough information is available in the orbit space, thus we need to compare the data in the observation space: the predictions from the orbit with the observations from the other arc.

If there is a catalog of $N$ orbits and $M$ observed arcs, each one too short to compute an orbit, this global problem has to be decomposed into three steps similar to those of the orbit identification case. The number of proposed attributions in step (i) must be much smaller than $M \times N$ . Step (ii) can be less difficult in that the original orbit from the better arc could be good enough to serve as preliminary orbit, but this is not always the case. Step (iii) is the same as above, but the quality control to be applied to the residuals can take into account the asymmetry between the two arcs.

# Recovery and precovery

This is the procedure to search for other observations belonging to the same physical object, assuming they are not already in the databases of past observations. It can take two forms: recovery in the future and in the sky, by pointing a telescope at one or more predicted positions of an already known object, and precovery in the past and in the archives of images of the sky, looking for observations which were either not measured or not included in the observation databases.

The main problem of recovery/precovery is that the resources needed (telescope time for recovery, human labor, and/or computational resources for precovery) depend upon the uncertainty of the prediction. When recovery observations are performed, often intruder asteroids are found along with (sometimes instead of) the wanted one; the same for precovery. Thus an attribution problem has to be solved after obtaining the observations.

# Linkage

The most difficult kind of identification problem is linkage, when two arcs of observations, both too short to perform orbit determination, are to be joined into an arc good enough to compute an orbit. In this case there is no way to directly compare quantities of the same nature, such as orbits with orbits, observations with observations: orbits are not available, and observations at different times cannot be directly compared (unless the time difference is very short). Thus the sequence of steps has to be different:

(i) to compute one or more hypothetical orbit, compatible with the observations of the first arc, together with some replacement of the covariance matrix to assess uncertainty;   
(ii) to compare predictions of the observations from the hypothetical orbit(s) with the observations of the other arcs, selecting the couples proposed for identification;   
(iii) to compute a preliminary orbit compatible with both arcs;   
(iv) to check the convergence of differential corrections, with the data of both arcs, and the quality of the residuals.

Linkage may be a difficult problem even when there are just a few observed arcs. Thus, when dealing with a large database of observed arcs too short for orbit determination, it is especially necessary to keep under control the computational complexity of the global linkage problem. Since linkage is a more difficult problem than the other classes of identifications, it will be discussed in the dedicated Chapter 8.

# 7.2 Linear orbit identification

The starting point for the basic orbit identification problem is a set of two nominal orbits, obtained by convergent differential corrections, as described in Chapter 5, with the initial conditions as the only fit parameters. Let $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } \in \mathbb { R } ^ { 6 }$ be two separately determined vectors of initial conditions, and $C _ { 1 } , C _ { 2 } , \Gamma _ { 1 } , \Gamma _ { 2 }$ be the normal and covariance matrices computed at convergence, that is at $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 }$ , respectively. We assume that these initial conditions are at the same epoch; if this is not the case, the orbits and the matrices have to be propagated to some common epoch (see Section 5.5). To determine $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 }$ we have used two separate sets of observations

$$
( t _ { i } , r _ { i } ) , \ i = 1 , m _ { 1 } , ( t _ { i } , r _ { i } ) , \ i = m _ { 1 } + 1 , m _ { 1 } + m _ { 2 }
$$

with $m _ { 1 }$ observations in the first arc and $m _ { 2 }$ in the second arc; they have resulted in the residuals, with respect to the nominal solutions,

$$
{ \pmb \xi } _ { 1 } = ( \xi _ { i } ) , i = 1 , m _ { 1 } , \xi _ { 2 } = ( \xi _ { i } ) , i = m _ { 1 } + 1 , m _ { 1 } + m _ { 2 } .
$$

We can compute the two separate target functions for $i = 1 , 2$

$$
\mathbf { \boldsymbol { \mathsf { c } } } ) = { \frac { 1 } { m _ { i } } } \mathbf { \boldsymbol { \xi } } _ { i } \cdot \mathbf { \boldsymbol { \xi } } _ { i } = Q _ { i } ( \mathbf { \boldsymbol { x } } _ { i } ) + \Delta Q _ { i } ( \mathbf { \boldsymbol { x } } ) = Q _ { i } ( \mathbf { \boldsymbol { x } } _ { i } ) + { \frac { 1 } { m _ { i } } } \left( \mathbf { \boldsymbol { x } } - \mathbf { \boldsymbol { x } } _ { i } \right) \cdot C _ { i } \left( \mathbf { \boldsymbol { x } } - \mathbf { \boldsymbol { x } } _ { i } \right) + \cdot
$$

where the dots contain the terms of degree 3 in $\left( \mathbf { x } - \mathbf { x } _ { i } \right)$ and those of degree 2 containing the residuals, see Section 5.2. The two penalties $\Delta Q _ { i }$ would be zero if the nominal orbits could be assumed, but if a single physical body has been observed, there must be a single orbit fitting both sets of observations, and we cannot assume $\mathbf { x } = \mathbf { x } _ { 1 }$ and $\mathbf { x } = \mathbf { x } _ { 2 }$ . Then the joint target function $Q$ contains a linear combination $Q _ { 0 }$ of the two separate minima $Q _ { 1 } ( \mathbf { x } _ { 1 } ) , Q _ { 2 } ( \mathbf { x } _ { 2 } )$ plus a penalty $\Delta Q$ measuring the increase of the target function resulting from the hypothesis that the two objects are the same: with $m = m _ { 1 } + m _ { 2 }$

$$
\begin{array} { r c l } { { \mathrm {  ~ \nabla ~ } _ { 1 } Q ( { \bf x } ) } } & { { = } } & { { \xi _ { 1 } \cdot \xi _ { 1 } + \xi _ { 2 } \cdot \xi _ { 2 } = m _ { 1 } Q _ { 1 } ( { \bf x } ) + m _ { 2 } Q _ { 2 } ( { \bf x } ) = m Q _ { 0 } + m \Delta Q ( { \bf x } ) , } } \\ { { m Q _ { 0 } } } & { { = } } & { { \left[ m _ { 1 } Q _ { 1 } ( { \bf x } _ { 1 } ) + m _ { 2 } Q _ { 2 } ( { \bf x } _ { 2 } ) \right] } } \\ { { \Delta Q ( { \bf x } ) } } & { { = } } & { { m _ { 1 } \Delta Q _ { 1 } ( { \bf x } ) + m _ { 2 } \Delta Q _ { 2 } ( { \bf x } ) } } \\ { { } } & { { = } } & { { \left( { \bf x - x _ { 1 } } \right) \cdot C _ { 1 } \left( { \bf x - x _ { 1 } } \right) + \left( { \bf x - x _ { 2 } } \right) \cdot C _ { 2 } \left( { \bf x - x _ { 2 } } \right) + \cdot \cdot \cdot . } } \end{array}
$$

# Linear theory

The linear algorithm to solve the problem is obtained when the linear approximation can be used, not only locally, in the neighborhood of the two separate solutions $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ , but even globally for the joint solution. This is a strong assumption, because we cannot assume that the two separate solutions are near to each other. However, if the assumption is true, we can use the quadratic approximation for both penalties $\Delta Q _ { i }$ , and obtain an explicit formula for the solution of the identification problem (Milani et al. 2000a). Neglecting all the higher order terms (the dots in the previous formula)

$$
\begin{array} { r l } & { \mathrm { \ i } Q ( \mathbf { x } ) \simeq ( \mathbf { x } - \mathbf { x } _ { 1 } ) \cdot C _ { 1 } \left( \mathbf { x } - \mathbf { x } _ { 1 } \right) + ( \mathbf { x } - \mathbf { x } _ { 2 } ) \cdot C _ { 2 } \left( \mathbf { x } - \mathbf { x } _ { 2 } \right) } \\ & { \quad \quad \quad = \mathbf { x } \cdot ( C _ { 1 } + C _ { 2 } ) \mathbf { x } - 2 \mathbf { x } \cdot \left( C _ { 1 } \mathbf { x } _ { 1 } + C _ { 2 } \mathbf { x } _ { 2 } \right) + \mathbf { x } _ { 1 } \cdot C _ { 1 } \mathbf { x } _ { 1 } + \mathbf { x } _ { 2 } \cdot C _ { 2 } \mathbf { x } } \end{array}
$$

Then the minimum of the penalty $\Delta Q$ can be found by minimizing the non-homogeneous quadratic form of the formula above. If the new joint minimum is $\mathbf { x } _ { 0 }$ , then by expanding around $\mathbf { x } _ { 0 }$ we have

$$
m \Delta Q ( \mathbf { x } ) \simeq ( \mathbf { x } - \mathbf { x } _ { 0 } ) \cdot C _ { 0 } \left( \mathbf { x } - \mathbf { x } _ { 0 } \right) + K
$$

and by comparing the last two formulae we find:

$$
\begin{array} { r c l } { { { \cal C } _ { 0 } } } & { { = } } & { { { \cal C } _ { 1 } + { \cal C } _ { 2 } , } } \\ { { } } & { { } } & { { { \cal C } _ { 0 } { \bf x } _ { 0 } } } & { { = } } & { { { \cal C } _ { 1 } { \bf x } _ { 1 } + { \cal C } _ { 2 } { \bf x } _ { 2 } , } } \\ { { } } & { { } } & { { { \cal K } } } & { { = } } & { { { \bf x } _ { 1 } \cdot { \cal C } _ { 1 } { \bf x } _ { 1 } + { \bf x } _ { 2 } \cdot { \cal C } _ { 2 } { \bf x } _ { 2 } - { \bf x } _ { 0 } \cdot { \cal C } _ { 0 } { \bf x } _ { 0 } . } } \end{array}
$$

If the matrix $C _ { 0 }$ , which is the sum of the two separate normal matrices $C _ { 1 }$ and $C _ { 2 }$ , is positive definite, then it is invertible and we can solve for the new minimum point by using the covariance matrix $\Gamma _ { 0 } = C _ { 0 } ^ { - 1 }$ :

$$
\mathbf { x } _ { 0 } = \Gamma _ { 0 } \left( C _ { 1 } \mathbf { x } _ { 1 } + C _ { 2 } \mathbf { x } _ { 2 } \right) .
$$

This has a simple interpretation in terms of differential corrections: at convergence in each of the two iterations, ${ \bf x } \ \longrightarrow \ { \bf x } _ { i }$ with $C _ { i } = C _ { i } ( { \bf x } _ { i } )$ and the right-hand side of the normal equation $D _ { i } = D _ { i } ( \mathbf { x } _ { i } ) = C _ { i } \Delta \mathbf { x } _ { i }$ is $\mathbf { 0 }$ . Thus

$$
( \mathbf { x } - \mathbf { x } _ { 1 } ) = \mathbf { 0 } { \mathrm { ~ a n d ~ } } C _ { 2 } ( \mathbf { x } - \mathbf { x } _ { 2 } ) = \mathbf { 0 } \Longrightarrow ( C _ { 1 } + C _ { 2 } ) \mathbf { x } = C _ { 1 } \mathbf { x } _ { 1 } + C _ { 2 } \mathbf { x } _ { 2 } .
$$

By the linearity assumption $C _ { 1 } , C _ { 2 }$ have the same values at $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 }$ and at $\mathbf { x } _ { 0 }$ ; under these conditions $\mathbf { x } = \mathbf { x } _ { 0 }$ is the result of the first differential correction for the joint problem.

The identification penalty $K / m$ approximates the minimum of the penalty $\Delta Q ( { \bf x } )$ , normalized by the number of observations: in the linear approximation $K / m = \Delta Q ( \mathbf { x } _ { 0 } )$ . Since $K$ is translation invariant

$$
\begin{array} { r l } { \mathrm {  ~ \psi ~ } _ { 0 } } & { \to \mathrm {  ~ \psi ~ } _ { { \bf x } _ { 0 } } + { \bf v } , \quad { \bf x } _ { 1 } \to { \bf x } _ { 1 } + { \bf v } , \quad { \bf x } _ { 2 } \to { \bf x } _ { 2 } + { \bf v } } \\ { \hat { \mathrm {  ~ \psi ~ } } _ { C } } & { \to \mathrm {  ~ \cal { K } ~ } + 2 { \bf v } \cdot ( C _ { 1 } { \bf x } _ { 1 } + C _ { 2 } { \bf x } _ { 2 } - C _ { 0 } { \bf x } _ { 0 } ) + { \bf v } \cdot ( C _ { 1 } + C _ { 2 } - C _ { 0 } ) { \bf v } = K , } \end{array}
$$

we can compute $K$ after a translation by $- \mathbf { x } _ { 1 }$ , that is assuming ${ \bf x } _ { 1 }  { \bf 0 }$ ,

${ \bf x } _ { 2 }  { \bf x } _ { 2 } - { \bf x } _ { 1 } = \Delta { \bf x }$ , and ${ \bf x } _ { 0 }  \Gamma _ { 0 } C _ { 2 } \Delta { \bf x }$ :

$$
K = \Delta \mathbf { x } \cdot C _ { 2 } \Delta \mathbf { x } - ( \mathbf { x } _ { 0 } - \mathbf { x } _ { 1 } ) \cdot C _ { 0 } ( \mathbf { x } _ { 0 } - \mathbf { x } _ { 1 } ) = \Delta \mathbf { x } \cdot C \Delta \mathbf { x } ,
$$

with $C = C _ { 2 } - C _ { 2 } \Gamma _ { 0 } C _ { 2 }$ . Alternatively, translating by $- \mathbf { x } _ { 2 }$ , that is with ${ \bf x } _ { 2 } \to { \bf 0 }$ , $\mathbf { x } _ { 1 }  - \Delta \mathbf { x }$ and $\mathbf { x } _ { 0 }  \Gamma _ { 0 } C _ { 1 } ( - \Delta \mathbf { x } )$ :

$$
\mathbf { \partial } _ { \mathbf { x } } ^ { \prime } = \Delta \mathbf { x } \cdot C _ { 1 } \Delta \mathbf { x } - \left( \mathbf { x } _ { 0 } - \mathbf { x } _ { 2 } \right) \cdot C _ { 0 } \left( \mathbf { x } _ { 0 } - \mathbf { x } _ { 2 } \right) = \Delta \mathbf { x } \cdot \left( C _ { 1 } - C _ { 1 } \Gamma _ { 0 } C _ { 1 } \right) \Delta \mathbf { x }
$$

and the same matrix $C$ can be defined by the alternative expression $C =$ $C _ { 1 } - C _ { 1 } \Gamma _ { 0 } C _ { 1 }$ . Both these formulae only assume that $\Gamma _ { 0 } = C _ { 0 } ^ { - 1 }$ exists, then

$$
C = C _ { 2 } - C _ { 2 } \Gamma _ { 0 } C _ { 2 } = C _ { 1 } - C _ { 1 } \Gamma _ { 0 } C _ { 1 } .
$$

The above equality is true in exact arithmetic, but might be violated in a numerical computation if the matrix $C _ { 0 }$ is badly conditioned. We can summarize the conclusions by the formula

$$
Q ( \mathbf { x } ) \simeq Q _ { 0 } + \frac { 1 } { m } \Delta \mathbf { x } \cdot C \Delta \mathbf { x } + \frac { 1 } { m } \left( \mathbf { x } - \mathbf { x } _ { 0 } \right) \cdot C _ { 0 } \left( \mathbf { x } - \mathbf { x } _ { 0 } \right)
$$

which allows also to assess the uncertainty of the identified solution, by defining confidence ellipsoids with matrix $C _ { 0 }$ .

This algorithm has a geometrical interpretation in terms of intersections of the two families of confidence ellipsoids. To result in a low penalty, say $m \Delta Q < \epsilon$ , a compromise solution $\mathbf { x } _ { 0 }$ has to belong to the intersection of the two confidence ellipsoids $m _ { 1 } \Delta Q _ { 1 } < \epsilon$ and $m _ { 2 } ~ \Delta Q _ { 2 } < \epsilon$ .

# Probabilistic interpretation

If $\mathbf { x } _ { i } ^ { * }$ is the nominal solution of the differential corrections with normal matrix $C _ { i }$ and covariance matrix $\Gamma _ { i } = C _ { i } ^ { - 1 }$ , the probability density of the initial conditions $\mathbf { x } _ { i }$ according to the Gaussian model (see Section 5.7) is

$$
{ \sf p } _ { { \bf X } _ { i } } ( { \bf x } _ { i } ) = N ( { \bf x } _ { i } , \Gamma _ { i } ) = \frac { \sqrt { \operatorname* { d e t } C _ { i } } } { ( 2 \pi ) ^ { N / 2 } } \exp \left( - \frac { 1 } { 2 } ( { \bf x } _ { i } - { \bf x } _ { i } ^ { * } ) \cdot C _ { i } ( { \bf x } _ { i } - { \bf x } _ { i } ^ { * } ) \right) .
$$

Let us assume $\mathbf { X } _ { 1 }$ and $\mathbf { X } _ { 2 }$ are independent random variables, that is their joint probability density function is $\mathsf { p } _ { \mathbf { X } _ { 1 } \mathbf { X } _ { 2 } } ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } ) \ = \ \mathsf { p } _ { \mathbf { X } _ { 1 } } ( \mathbf { x } _ { 1 } ) \cdot \mathsf { p } _ { \mathbf { X } _ { 2 } } ( \mathbf { x } _ { 2 } )$ . This hypothesis is justified because the set of observations of the two independent discoveries is disjoint. Then the probability of the identification $P _ { I } = \mathcal { P } ( \mathbf { X } _ { 1 } = \mathbf { X } _ { 2 } )$ is obtained as

$$
P _ { I } = \int _ { \mathbb { R } ^ { 6 } } \ p _ { \mathbf { X } _ { 1 } , \mathbf { X } _ { 2 } } ( \mathbf { x } , \mathbf { x } ) \ d \mathbf { x } = \int _ { \mathbb { R } ^ { 6 } } \ p _ { \mathbf { X } _ { 1 } } ( \mathbf { x } ) \cdot \ p _ { \mathbf { X } _ { 2 } } ( \mathbf { x } ) \ d \mathbf { x } .
$$

The product $\mathsf { p } _ { \mathbf { X } _ { 1 } } ( \mathbf { x } ) \cdot \mathsf { p } _ { \mathbf { X } _ { 2 } } ( \mathbf { x } )$ is not the probability density of the identification orbit, because the integral over the entire initial conditions space is not equal to 1. Indeed, to obtain the conditional density function of the identification orbit (under the hypothesis $\mathbf { x } _ { 1 } = \mathbf { x } _ { 2 }$ ), the product has to be renormalized by dividing by the probability of the identification $P _ { I }$ .

Then both the probability $P _ { I }$ and the conditional density function of the identified orbit can be computed starting from the product

$$
\begin{array} { r c l } { { \sf p } _ { { \bf X } _ { 1 } } ( { \bf x } ) \cdot { \sf p } _ { { \bf X } _ { 2 } } ( { \bf x } ) } & { = } & { \displaystyle \frac { \sqrt { \operatorname* { d e t } ( C _ { 1 } C _ { 2 } ) } } { ( 2 \pi ) ^ { N } } \exp \Bigl \{ - \displaystyle \frac { 1 } { 2 } \Bigl [ ( { \bf x } - { \bf x } _ { 1 } ) \cdot C _ { 1 } ( { \bf x } - { \bf x } _ { 1 } ) } \\ & & { + ( { \bf x } - { \bf x } _ { 2 } ) \cdot C _ { 2 } ( { \bf x } - { \bf x } _ { 2 } ) \Bigr ] \Bigr \} } \end{array}
$$

and replacing the sum of two quadratic forms in the exponent with the single quadratic form centered in $\mathbf { x } _ { 0 }$ , with normal matrix $C _ { 0 }$ :

$$
\begin{array} { l l l } { { ( { \bf x } ) \cdot \mathsf { p } _ { { \bf x } _ { 2 } } ( { \bf x } ) } } & { { = } } & { { \displaystyle \frac { \sqrt { \operatorname* { d e t } ( C _ { 1 } C _ { 2 } ) } } { ( 2 \pi ) ^ { N } } \exp \left\{ - \frac { 1 } { 2 } \left[ ( { \bf x } - { \bf x } _ { 0 } ) \cdot C _ { 0 } ( { \bf x } - { \bf x } _ { 0 } ) + K \right] \right\} } } \\ { { } } & { { = } } & { { N ( { \bf x } _ { 0 } , \Gamma _ { 0 } ) ( { \bf x } ) \cdot \displaystyle \frac { \sqrt { \operatorname* { d e t } ( C _ { 1 } C _ { 2 } ) } } { ( 2 \pi ) ^ { N / 2 } \sqrt { \operatorname* { d e t } C _ { 0 } } } \exp \left( - \frac { K } { 2 } \right) . } } \end{array}
$$

To simplify this expression, let us assume both $C _ { 1 }$ and $C _ { 2 }$ are positive definite. Then they can be diagonalized simultaneously, that is, there is an orthogonal matrix $S$ such that

$$
\begin{array} { l l l } { { S C _ { 1 } S ^ { T } = \mathrm { d i a g } [ \lambda _ { 1 j } ] , } } & { { S C _ { 2 } S ^ { T } = \mathrm { d i a g } [ \lambda _ { 2 j } ] , } } & { { S C _ { 0 } S ^ { T } = \mathrm { d i a g } [ \lambda _ { 1 j } + \lambda _ { 2 j } ] , } } \end{array}
$$

$$
S C S ^ { T } = S C _ { 2 } S ^ { T } - S C _ { 2 } S ^ { T } S C _ { 0 } ^ { - 1 } S ^ { T } S C _ { 2 } S ^ { T } = \mathrm { { d i a g } } \left[ \frac { \lambda _ { 1 j } \lambda _ { 2 j } } { \lambda _ { 1 j } + \lambda _ { 2 j } } \right] .
$$

From this we can compute the determinants

$$
{ \frac { \operatorname* { d e t } ( C _ { 1 } C _ { 2 } ) } { \operatorname* { d e t } ( C _ { 1 } + C _ { 2 } ) } } = \operatorname* { d e t } ( S ) ^ { - 2 } { \frac { \prod _ { j = 1 } ^ { N } \lambda _ { 1 j } \prod _ { j = 1 } ^ { N } \lambda _ { 2 j } } { \prod _ { j = 1 } ^ { N } ( \lambda _ { 1 j } + \lambda _ { 2 j } ) } } = \operatorname* { d e t } ( C )
$$

and find that the factor multiplying $N ( \mathbf { x } _ { 0 } , \Gamma _ { 0 } )$ has a simple interpretation

$$
{ \begin{array} { l l l } { \mathsf { p } _ { \mathbf { X } _ { 1 } } ( \mathbf { x } ) \cdot \mathsf { p } _ { \mathbf { X } _ { 2 } } ( \mathbf { x } ) } & { = } & { N ( \mathbf { x } _ { 0 } , \Gamma _ { 0 } ) ( \mathbf { x } ) \cdot { \frac { \sqrt { \operatorname* { d e t } C } } { ( 2 \pi ) ^ { N / 2 } } } \exp \left[ - { \frac { 1 } { 2 } } K \right] } \\ & { = } & { N ( \mathbf { x } _ { 0 } , \Gamma _ { 0 } ) ( \mathbf { x } ) \cdot N ( \mathbf { 0 } , C ^ { - 1 } ) ( \Delta \mathbf { x } ) . } \end{array} }
$$

The probabilistic interpretation of the above formula is

$$
\frac { \mathsf { p } _ { \mathbf { X } _ { 1 } } ( \mathbf { x } ) \cdot \mathsf { p } _ { \mathbf { X } _ { 2 } } ( \mathbf { x } ) } { P _ { I } } = N ( \mathbf { x } _ { 0 } , \Gamma _ { 0 } )
$$

with the identification probability estimated as $P _ { I } = N ( \mathbf { 0 } , C ^ { - 1 } ) ( \Delta \mathbf { x } )$

In conclusion, the probability that the identification is true is the value of the Gaussian $N ( { \bf x } _ { 1 } , C ^ { - 1 } ) ( { \bf x } _ { 2 } ) = N ( { \bf x } _ { 2 } , C ^ { - 1 } ) ( { \bf x } _ { 1 } )$ , computed by using the normal matrix $C$ (the same used to compute the identification penalty $K$ ). Assuming the identification is true, the identification orbit has the normal distribution $N ( \mathbf { x } _ { 0 } , \Gamma _ { 0 } )$ . The correspondence between the probabilistic and the optimization interpretations is maintained in the linear identification theory, as in the linear orbit determination theory.

# 7.3 Semilinear orbit identification

The applicability of the linear identification algorithm depends upon the nonlinearity, that is upon the difference between the confidence regions and the confidence ellipsoids of the two separate solutions $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ .

# Nonlinearity

As discussed in Section 5.5, there are two main sources of nonlinearity in the confidence regions. First, each of the two separate confidence regions for the solutions $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ could be already strongly nonlinear. Second, even assuming that the two separate confidence regions are well approximated by the confidence ellipsoids, the initial conditions have to be determined at times $t _ { 1 }$ , close to the times of the first $m _ { 1 }$ observations, and $t _ { 2 }$ , close to the last $m _ { 2 }$ observations, respectively.2 When the orbits, determined at $t _ { 1 }$ and $t _ { 2 }$ , respectively, are propagated to a common time, say $t _ { 0 } = ( t _ { 1 } + t _ { 2 } ) / 2$ , the conditioning number of the propagated normal matrices increases at least quadratically with the time spans $| t _ { 0 } - t _ { i } |$ . Thus, as the time span between the two arcs increases, the confidence ellipsoids at the common time $t _ { 0 }$ become more and more elongated, they are worse and worse approximations of the confidence regions, and the intersection of the confidence regions may have nothing to do with the intersection of the confidence ellipsoids.

There is a third source of nonlinearity which is specific to the coordinates used to represent the initial conditions of the orbit (see Section 10.3 for a discussion of different coordinates). In the Keplerian orbital elements $( a , e , I , \Omega , \omega , \ell )$ the values $e = 0$ and $I = 0$ correspond to singularities, in which some of the angle variables $( \Omega , \omega , \ell )$ are not uniquely defined. If the values $e \ = \ 0$ and/or $I \ = \ 0$ are within the confidence ellipsoid, then linearity fails even when the confidence region is small. For this reason nonsingular elements like the equinoctial elements $( a , h , k , p , q , \lambda )$ are used, see (Broucke and Cefola 1972), with

$$
\begin{array} { c } { h = e \sin ( \Omega + \omega ) , \ k = e \cos ( \Omega + \omega ) } \\ { ~ } \\ { = \tan ( I / 2 ) \sin \Omega , \ q = \tan ( I / 2 ) \cos \Omega , \ \lambda = \ell + \Omega + \omega . } \end{array}
$$

The variables $( h , k , p , q , \lambda )$ are defined for $e = 0$ and/or $I = 0$ (by $h = k = 0$ for $e = 0$ and by $p = q = 0$ for $I = 0$ ) and they are smooth as functions of Cartesian initial conditions.

# Restricted orbit identification

To find the orbit identifications among a large catalog of orbits it is necessary to start from step (i) of the procedure outlined in Section 7.1: to select a small subset of the couples of orbit, and with a simple algorithm, not including any orbit propagation. Thus we would like to compare orbital elements which are constant in the two-body approximation, e.g., excluding $\lambda$ in equinoctial elements. This also removes the effect of the nonlinearity in the propagation of $\lambda$ , which occurs even in the two-body problem, as already appears from our model problem, see Section 5.6. We may also take advantage of the fact that some elements are typically better determined than others, even with a short observed arc: this is the case for the orbital plane variables, either $( I , \Omega )$ in Keplerian or $( p , q )$ in equinoctial ones.

Thus we need to perform a restricted identification, computing a penalty $K _ { 2 }$ in a two-dimensional space of elements $( p , q )$ and/or a penalty $K _ { 5 }$ in a five-dimensional space $( a , h , k , p , q )$ . In general, we split the vector $\mathbf { x }$ of estimated parameters into two components $\mathbf { h }$ and $\mathbf { g }$ , and let $\mathbf { g }$ contain the elements to which the comparison is restricted.

The normal and covariance matrices $C$ and $\Gamma$ are decomposed as in Section 5.4. Then the marginal uncertainty of $\mathbf { g }$ (for arbitrary $\mathbf { h }$ ) can be described by the penalty, with respect to the minimum point $\mathbf { g } ^ { * }$

$$
m \Delta Q \simeq ( \mathbf { g } - \mathbf { g } ^ { * } ) \cdot C ^ { \mathbf { g } \mathbf { g } } ( \mathbf { g } - \mathbf { g } ^ { * } ) , ~ C ^ { \mathbf { g } \mathbf { g } } = C _ { \mathbf { g } \mathbf { g } } - C _ { \mathbf { g } \mathbf { h } } C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } C _ { \mathbf { h } \mathbf { g } }
$$

and by the marginal covariance matrix $\Gamma _ { \bf g g } = ( C ^ { \bf g g } ) ^ { - 1 }$ . Note that this penalty as a function of $\mathbf { g }$ has been obtained by changing the value of $\mathbf { h }$ from the nominal $\mathbf { h } ^ { * }$ to a suitable point of the regression subspace.

We use this restricted penalty formula for the restricted identification problem: let $\mathbf { x } _ { 1 } = ( \mathbf { h } _ { 1 } , \mathbf { g } _ { 1 } )$ and $\mathbf { x } _ { 2 } = ( \mathbf { h } _ { 2 } , \mathbf { g } _ { 2 } )$ be the separate nominal solutions for the two arcs, and $C ^ { \bf g g } ( { \bf x } _ { 1 } )$ and $C ^ { \bf g g } ( { \bf x } _ { 2 } )$ the corresponding marginal

normal matrices. The variables $\mathbf { h }$ are given as a function of $\mathbf { g }$ by:

$$
\left\{ \begin{array} { r c l } { { \bf h } _ { 1 } ( { \bf g } ) } & { = } & { { \bf h } _ { 1 } - C _ { \bf h } ^ { - 1 } ( { \bf x } _ { 1 } ) C _ { \bf h g } ( { \bf x } _ { 1 } ) ( { \bf g } - { \bf g } _ { 1 } ) } \\ { { \bf h } _ { 2 } ( { \bf g } ) } & { = } & { { \bf h } _ { 2 } - C _ { \bf h } ^ { - 1 } ( { \bf x } _ { 2 } ) C _ { \bf h g } ( { \bf x } _ { 2 } ) ( { \bf g } - { \bf g } _ { 2 } ) . } \end{array} \right.
$$

By the same formalism of the previous section:

$$
\begin{array} { r c l } { { \displaystyle \frac { m } { 2 } \Delta Q } } & { { \simeq } } & { { ( { \bf g - g } _ { 0 } ) \cdot C _ { 0 } ^ { { \bf g g } } ( { \bf g - g } _ { 0 } ) + K _ { { \bf g } } } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle C _ { 0 } ^ { { \bf g g } } } } & { { = } } & { { C _ { 1 } ^ { { \bf g g } } ( { \bf x } _ { 1 } ) + C _ { 2 } ^ { { \bf g g } } ( { \bf x } _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { { \bf g } _ { 0 } } } & { { = } } & { { \left( C _ { 0 } ^ { { \bf g g } } \right) ^ { - 1 } \left( C _ { 1 } ^ { { \bf g g } } ( { \bf x } _ { 1 } ) { \bf g } _ { 1 } + C _ { 2 } ^ { { \bf g g } } ( { \bf x } _ { 2 } ) { \bf g } _ { 2 } \right) } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle C ^ { { \bf g } } } } & { { = } } & { { C _ { 2 } ^ { { \bf g g } } ( { \bf x } _ { 2 } ) - C _ { 2 } ^ { { \bf g g } } ( { \bf x } _ { 2 } ) \left( C _ { 0 } ^ { { \bf g g } } \right) ^ { - 1 } C _ { 2 } ^ { { \bf g g } } ( { \bf x } _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle } } & { { = } } & { { C _ { 1 } ^ { { \bf g g } } ( { \bf x } _ { 1 } ) - C _ { 1 } ^ { { \bf g g } } ( { \bf x } _ { 1 } ) \left( C _ { 0 } ^ { { \bf g g } } \right) ^ { - 1 } C _ { 1 } ^ { { \bf g g } } ( { \bf x } _ { 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle K _ { { \bf g } } } } & { { = } } & { { ( { \bf g } _ { 2 } - { \bf g } _ { 1 } ) \cdot C ^ { { \bf g } } \left( { \bf g } _ { 2 } - { \bf g } _ { 1 } \right) . } } \end{array}
$$

$K _ { \mathbf { g } }$ is not the same as the complete minimum penalty $K$ of the previous section, but it is obtained by assuming that ${ \bf x } _ { 1 } = ( { \bf h } _ { 1 } ( { \bf g } _ { 0 } ) , { \bf g } _ { 0 } )$ in the computation of $\Delta Q _ { 1 }$ , ${ \bf x } _ { 2 } = ( { \bf h } _ { 2 } ( { \bf g } _ { 0 } ) , { \bf g } _ { 0 } )$ in the computation of $\Delta Q _ { 2 }$ , ${ \bf g } _ { 0 }$ being the proposed restricted identification. Thus $K _ { \mathbf { g } } \ \leq \ K$ : $K _ { \mathbf { g } }$ is the minimum of the penalty over the space of variables $( \mathbf { g } , \mathbf { h } _ { 1 } , \mathbf { h } _ { 2 } )$ , while $K$ is the minimum under the additional constraint $\mathbf { h } _ { 1 } = \mathbf { h } _ { 2 }$ , and the minimum of a function can only increase when constraints are added.

The penalty $K _ { \mathbf { g } }$ can be used as a preliminary control, that is, if $K _ { \mathbf { g } } > \Sigma$ , for a positive parameter $\Sigma$ , then also $K > \Sigma$ and many couples can be discarded without doing a computation with the larger matrices. This allows us to select a subset of couples candidates for identification with the linear identification algorithm.

# Multistage identification procedure

An effective procedure for proposing orbit identifications can be obtained by a sequence of filtering stages:

(i) restricted identification comparing only $\mathbf { g } = ( p , q )$ , selecting the couples with two-dimensional penalty $K _ { 2 }$ below a control $\Sigma _ { 2 } > 0$ ;   
(ii) restricted identification comparing only $\mathbf { g } = ( a , h , k , p , q )$ , selecting the couples with five-dimensional penalty $K _ { 5 }$ below a control $\Sigma _ { 5 } > 0$ ;   
(iii) full identification between the orbits $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ propagated to a common time $t _ { 0 }$ , selecting the couples with full penalty $K$ below some control $\Sigma > 0$ .

The three filters are applied in series, that is each one is applied only to the couples passing the previous one. After passing all three filter stages, the proposed identification has to be confirmed by differential corrections, starting from the first guess $\mathbf { x } _ { 0 }$ of eq. (7.1), and quality control.

To control computational complexity, the most critical is filter 1, because it has to be applied to all the $\simeq N ^ { 2 } / 2$ couples in a catalog containing $N$ orbits. If $N$ is very large, it may be necessary to use an algorithm of computational complexity $\mathcal { O } ( N \log N )$ which could be very similar to the one discussed in Section 11.3. Because the orbital plane variables are indeed better determined, the control $\Sigma _ { 2 }$ can be quite tight (Milani et al. 2000a, Figure 2). This helps in decreasing the number of couples passed to filter 2: in a test reported by Milani et al. (2000a), with $\Sigma _ { 2 } = 3 0$ only a fraction $\simeq 0 . 0 0 6$ of the couples passed filter 1. The second filter with $\Sigma _ { 5 } = 5 0 0 0$ passed a fraction 0.07 of those passed by filter 1. The choice of the values for $\Sigma _ { 5 }$ and $\Sigma$ is not easy; a method to optimally select them for best performance is in (Milani et al. 2005c, Section 5).

The most tricky stage is filter 3, for two reasons. First, propagation of both $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ , with covariance and normal matrices, to a common time $t _ { 0 } = ( t _ { 1 } + t _ { 2 } ) / 2$ specifically for each couple passing filter 2 would be computationally expensive. A possible solution is to prepare in advance a number of propagated orbit catalogs at suitably selected times, in such a way that filter 3 can be applied to the catalog corresponding to the epoch most suitable for the given couple. Although the propagation of an orbit with a full $N$ -body model is computationally expensive, the complexity for propagating the entire catalog is $\mathcal { O } ( N )$ .

Second, the propagation including the variable $\lambda$ is anyway nonlinear. If the time spans $| t _ { 0 } - t _ { i } |$ are long, the shape of the confidence regions are different from the ellipsoids computed with the propagated normal matrices (see Figure 5.2), and the intersections of the confidence ellipsoids can be very different from those of the confidence regions. If the time interval between the two separate observed arcs is not too long, and the nonlinear effects are not too pronounced, this can be compensated by selecting a value of $\Sigma$ much larger than the linear identification algorithm would suggest. For example, by using the standard $\chi ^ { 2 }$ tables the probability of such an identification would be ridiculously small. Because of the exponential decrease of the normal probability density, the probabilistic interpretation based on the linear Gaussian formulae is incompatible with nonlinear effects, even if they are moderate; see Chapter 12. We call such an algorithm semilinear identification. In the test of Milani et al. (2000a) the value $\Sigma = 1 0 0 0 0 0 0$ was used, with a very large increase of the computational load because only a fraction 0.01 of the differential corrections attempted were convergent (low accuracy). The number of successful identifications was very encouraging, although this number was a small fraction of the single apparition orbits cataloged, leaving the suspicion that there might be many more to be discovered. For an even more intensive effort to find large numbers of identifications, see Section 10.2.

# 7.4 Nonlinear orbit identification

We would like to find algorithms allowing us to cope with fully nonlinear identification problems, e.g., with the case of two short observed arcs, with poorly determined orbits, separated in time by years. This is a very difficult problem, which has not been fully solved yet. To find such an algorithm we need a better understanding of the nonlinearity arising in the identification problem, and for this we restart from our model problem.

![](images/b7c3596d3a3af977eea55dec57999621c4a35588dc1ad8a9e7d44fd0c6d4c284.jpg)  
Fig. 7.1. The identification in the coordinates $( n , \lambda )$ , the latter being considered a real number. The two vertical segments at $\lambda \simeq 0$ and at $\lambda \simeq 2 0$ are in fact very thin confidence ellipses, representing the uncertainty (with confidence parameter $\sigma = 3$ ) at the central times of the two arcs. The slanted lines are also thin ellipses, the propagated confidence ellipses at the central time $t _ { 0 } \simeq 1 0$ . Their intersection contains the true identification orbit, which is easily found with the linear identification formula starting from the two nominal solutions (marked with small circles).

# Model identification problem

The main effect of nonlinearity can be illustrated in our model problem. In all the figures of this subsection we use an example with two arcs that are 20 orbital periods apart, each with four observations spanning $\simeq 0 . 0 0 5$ periods. The RMS observation error is 0.001 radians. The true orbit has $a = 1$ (in units such that $n = 1$ ).

If we attempt the identification of the two arcs in the space of the $( n , \lambda )$ coordinates, considering $\lambda$ as a real number (as if we could observe the number of revolutions), the problem is exactly linear (see Figure 7.1) and the linear formulae discussed above provide a very good first guess for the identification orbit. Indeed the first guess $\mathbf { x } _ { 0 }$ and the final nominal solution, obtained by differential corrections, are very close.

![](images/8c19a512c1c34bcfacb2ea7662aae5adec5c001015a57d19baa59eab959f52a0.jpg)  
Fig. 7.2. The identification in the coordinates $( a , \lambda )$ , the latter being considered a real number. The slanted lines are in fact thin confidence ellipses for the two orbits propagated to the time $t _ { 0 }$ , while the two curves (tangent at the nominal solutions) are thin semilinear confidence boundaries.

If we use the same algorithm in the space of the $( a , \lambda )$ coordinates (still considering $\lambda \in \mathbb R$ ), the problem becomes nonlinear. In Figure 7.2 we show the confidence ellipses of the two orbits, as obtained by propagating the normal matrices to the common time $t _ { 0 }$ (by the formula of Section 5.5) and also the curves obtained by propagation, point by point, of the confidence ellipses at the times $t _ { 1 }$ and $t _ { 2 }$ , respectively, to the common time $t _ { 0 }$ (the so-called semilinear approximation, further discussed in Section 7.5). The nonlinear confidence regions have a connected intersection, although it is disjoint from the intersection of the linear confidence ellipses. Nevertheless, the first guess $\mathbf { x } _ { 0 }$ computed with the linear identification formula, which belongs to the intersection of the linear confidence ellipses, is good enough to allow convergence of differential corrections to the true identification orbit, which belongs to the intersection of the nonlinear confidence regions.

![](images/131762576e44781e21dd8a6f28f4c371a5921cba88fd8e687d86de19edd99168.jpg)  
Fig. 7.3. The identification in the coordinates $( n , \lambda )$ , the latter being considered as an angle. The spurious solution with $n \simeq 0 . 6 9$ is near one of the four intersections of the wrapped confidence ellipses, the one which would be suggested by the linear identification formula.

The problem becomes more difficult if we take into account the fact that $\lambda$ is an angle: when, after many years, an asteroid is independently rediscovered there is no way to know a priori how many revolutions have been completed between the two discoveries. Figure 7.3 shows that the problem is no longer linear, not even in the $( n , \lambda )$ coordinates; indeed the confidence ellipses, linearly propagated to the common time $t _ { 0 }$ and then wrapped on the cylinder obtained by identification of $\lambda = - \pi$ with $\lambda = + \pi$ , have (in this example) an intersection with four connected components. The first guess for the identification orbit $\mathbf { x } _ { 0 }$ obtained by the linear identification formulae turns out, in this case, to belong to a different connected component from the one containing the true solution. Thus the differential corrections starting from $\mathbf { x } _ { 0 }$ converge to the spurious solution closest to $\mathbf { x } _ { 0 }$ .

Of course in the coordinates $( a , \lambda )$ the two nonlinear effects (from the nonlinearity of the integral flow and from the wrapping on a cylinder) combine and result in a geometrically complicated situation. As shown in Figure 7.4, the intersection of both the linear and the nonlinear confidence regions can have a dozen connected components; the number of connected components does not even need to be the same.

![](images/1317f638f326cbd847e929a2c129e722859790a669178ff9bc7e254a017e7f05.jpg)  
Fig. 7.4. The identification in the coordinates $( n , \lambda )$ , the latter as an angle. The spurious solution for $a ~ \simeq ~ 1 . 2 9$ corresponds to the one found in the other coordinates. The nonlinear confidence regions have an intersection with more connected components than the linear ones.

# Cycle slip estimation

We propose a solution to the nonlinearity problem as shown above in the model problem. Let us split the orbital elements, in equinoctial coordinates with $a$ replaced by the mean motion $n$ , into the part corresponding to our model problem and the part containing the variables connected with eccentricity and inclination:

$$
\mathbf { x } = \left[ \begin{array} { c } { \mathbf { g } } \\ { \mathbf { h } } \end{array} \right] , \quad \mathbf { g } = \left[ \begin{array} { c } { e \sin \varpi } \\ { e \cos \varpi } \\ { \tan ( I / 2 ) \sin \Omega } \\ { \tan ( I / 2 ) \cos \Omega } \end{array} \right] , \quad \mathbf { h } = \left[ \begin{array} { c } { n } \\ { \lambda } \end{array} \right] .
$$

Let the central times of the two separate arcs of observations be $t _ { 1 } , t _ { 2 }$ with $t _ { 1 } < t _ { 2 }$ , and $\mathbf { x } _ { i } , C _ { i } , \Gamma _ { i }$ for $i = 1 , 2$ be the nominal orbital elements, the normal and the covariance matrices corresponding to each arc. We want to find a partial identification based only upon $\mathbf { h } _ { 1 } = ( n _ { 1 } , \lambda _ { 1 } )$ and ${ \bf h } _ { 2 } = ( n _ { 2 } , \lambda _ { 2 } )$ . From each arc we have a marginal confidence interval for the mean motion

$$
n _ { i } ^ { - } = n _ { i } - \sigma \cdot \mathrm { R M S } ( n _ { i } ) \leq n \leq n _ { i } ^ { + } = n _ { i } + \sigma \cdot \mathrm { R M S } ( n _ { i } ) ;
$$

then the common range of values for $n$ is

$$
n ^ { - } = \operatorname* { m a x } ( n _ { 1 } ^ { - } , n _ { 2 } ^ { - } , 0 ) \leq n \leq n ^ { + } = \operatorname* { m i n } ( n _ { 1 } ^ { + } , n _ { 2 } ^ { + } ) .
$$

If the interval $[ n ^ { - } , n ^ { + } ]$ is not empty, let us select a time $t _ { 0 }$ such that $t _ { 1 } <$ $t _ { 0 } < t _ { 2 }$ . The two-body predictions for $\lambda ( t _ { 0 } )$ are

$$
\begin{array} { l l l } { { \lambda _ { 1 } + n ^ { - } \left( t _ { 0 } - t _ { 1 } \right) } } & { { \leq } } & { { \lambda _ { 1 0 } \leq \lambda _ { 1 } + n ^ { + } \left( t _ { 0 } - t _ { 1 } \right) } } \\ { { \lambda _ { 2 } + n ^ { + } \left( t _ { 0 } - t _ { 2 } \right) } } & { { \leq } } & { { \lambda _ { 2 0 } \leq \lambda _ { 2 } + n ^ { - } \left( t _ { 0 } - t _ { 2 } \right) } } \end{array}
$$

and by subtracting the inequalities

$$
n ^ { - } \Delta t - \Delta \lambda \le \lambda _ { 1 0 } - \lambda _ { 2 0 } \le n ^ { + } \Delta t - \Delta \lambda
$$

where $\Delta \lambda = \lambda _ { 2 } - \lambda _ { 1 }$ and $\Delta t = t _ { 2 } - t _ { 1 } > 0$ . To obtain an intersection of the two lines of possible predictions for the time $t _ { 0 }$ , that is a common possible orbit, the predictions $\lambda _ { 1 0 }$ and $\lambda _ { 2 0 }$ need to be equal as angle variables: $\lambda _ { 1 0 } - \lambda _ { 2 0 } = 2 \pi k$ , with $k$ an arbitrary integer (in fact $k \geq - 1$ ). From this equation it is possible to find the finite number of possible values $k$ for the number of cycles slipped

$$
\frac { n ^ { - } \Delta t - \Delta \lambda } { 2 \pi } \leq k \leq \frac { n ^ { + } \Delta t - \Delta \lambda } { 2 \pi }
$$

implying that $k ^ { - } \leq k \leq k ^ { + }$ with

$$
k ^ { - } = \mathrm { C e i l i n g } \left( \frac { n ^ { - } ~ \Delta t - \Delta \lambda } { 2 ~ \pi } \right) , ~ k ^ { + } = \mathrm { F l o o r } \left( \frac { n ^ { + } ~ \Delta t - \Delta \lambda } { 2 ~ \pi } \right) .
$$

![](images/a16d530e62d2e011f58b67f42feced178516c01a7a21656d73d7512baab53d9b.jpg)  
Fig. 7.5. The identification in the coordinates $( n , \lambda )$ , the latter being considered as an angle. For each intersection of the confidence ellipse, the cycle slip algorithm computes a separate first guess; all five of them lead to convergent differential corrections, with different quality of fit.