# Chapter 17

# Stationary Iterative Methods

I recommend this method to you for imitation.

You will hardly ever again eliminate directly, at least not when you have more than 2 unknowns.

The indirect [iterative] procedure can be done while half asleep,

or while thinking about other things.[15]

CARLFRIEDRICHGAUSS,LettertoC.L.Gerling(1823)

The iterative method is commonly called the "Seidel process,"

or the "Gauss-Seidel process."

But, as Ostrowski (1952) points out,

Seidel (1874) mentions the process but advocates not using it.

Gauss nowhere mentions it.

— GEORGE E. FORSYTHE,

Solving Linear Algebraic Equations Can Be Interesting (1953)

The spurious contributions in $\mathrm{null}(A)$

grow at worst linearly and

if the rounding errors are small the scheme can be quite effective.

— HERBERT B. KELLER,

On the Solution of Singular and Semidefinite Linear Systems by Iteration (1965)

Table 17.1. Dates of publication of selected iterative methods. Based on Young [1271, 1989].   

<table><tr><td>1845</td><td>Jacobi</td><td>Jacobi method</td></tr><tr><td>1874</td><td>Seidel</td><td>Gauss-Seidel method</td></tr><tr><td>1910</td><td>Richardson</td><td>Richardson&#x27;s method</td></tr><tr><td>1938–1939</td><td>Temple</td><td>Method of steepest descent</td></tr><tr><td>1940s</td><td>Various (analysis by Young and Frankel)</td><td>Successive overrelaxation (SOR) method</td></tr><tr><td>1952</td><td>Hestenes and Stiefel</td><td>Conjugate gradient method</td></tr></table>

Iterative methods for solving linear systems have a long history, going back at least to Gauss. Table 17.1 shows the dates of publication of selected methods. It is perhaps surprising, then, that rounding error analysis for iterative methods is not well developed. There are two main reasons for the paucity of error analysis. One is that in many applications accuracy requirements are modest and are satisfied without difficulty, resulting in little demand for error analysis. Certainly there is no point in computing an answer to greater accuracy than that determined by the data, and in scientific and engineering applications the data often has only a few correct digits. The second reason is that rounding error analysis for iterative methods is inherently more difficult than for direct methods, and the bounds that are obtained are harder to interpret.

In this chapter we consider a simple but important class of iterative methods, stationary iterative methods, for which a reasonably comprehensive error analysis can be given. The basic question that our analysis attempts to answer is, "What is the limiting accuracy of a method in floating point arithmetic?" Specifically, "How small can we guarantee that the backward or forward error will be over all iterations $k = 1,2,\ldots$ ?" Without an answer to this question we cannot be sure that a convergence test of the form $\| b - A\widehat{x}_k\| \leq \epsilon$ (say) will ever be satisfied, for any given value of $\epsilon < \| b - Ax_0\|!$

As an indication of the potentially devastating effects of rounding errors we present an example constructed and discussed by Hammarling and Wilkinson [541, 1976]. Here, $A$ is the $100 \times 100$ lower bidiagonal matrix with $a_{ii} \equiv 1.5$ and $a_{i,i-1} \equiv 1$ , and $b_i \equiv 2.5$ . The successive overrelaxation (SOR) method is applied in MATLAB with parameter $\omega = 1.5$ , starting with the rounded version of the exact solution $x$ , given by $x_i = 1 - (-2/3)^i$ . The forward errors $\| \widehat{x}_k - x \|_\infty / \| x \|_\infty$ and the $\infty$ -norm backward errors $\eta_{A,b}(\widehat{x}_k)$ are plotted in Figure 17.1. The SOR method converges in exact arithmetic, since the iteration matrix has spectral radius $1/2$ , but in the presence of rounding errors it diverges. The iterate $\widehat{x}_{238}$ has a largest element of order $10^{13}$ , $\widehat{x}_{k+2} \equiv \widehat{x}_k$ for $k \geq 238$ , and for $k > 100$ , $\widehat{x}_k(60:100) \approx (-1)^k \widehat{x}_{100}(60:100)$ . The divergence is not a result of ill conditioning of $A$ , since $\kappa_\infty(A) \approx 5$ . The reason for the initial rapid growth of the errors in this example is that the iteration matrix is far from normal; this allows the norms of its powers to become very large before they ultimately decay by a factor $\approx 1/2$ with each successive power. The effect of rounding errors is to cause the forward error curve in Figure 17.1 to level off near $k = 100$ , instead of decaying to zero as it would

![](images/cd54caafbe910181415489b3cc990191430b0af43deeb7fa77cd1748a2932fe3.jpg)  
Figure 17.1. SOR iteration.

in exact arithmetic. More insight into the initial behaviour of the errors can be obtained using the notion of pseudo-eigenvalues; see §18.3.

# 17.1. Survey of Error Analysis

Before analysing stationary iterative methods, we briefly survey the published error analysis for iterative methods. For symmetric positive definite systems, Golub [507, 1962] derives both statistical and nonstatistical bounds for the forward error and residual of the Richardson method. Benschop and Ratz [104, 1971] give a statistical analysis of the effect of rounding errors on stationary iteration, under the assumption that the rounding errors are independent random variables with zero mean. Lynn [802, 1964] presents a statistical analysis for the SOR method with a symmetric positive definite matrix.

Hammarling and Wilkinson [541, 1976] give a normwise error analysis for the SOR method. With the aid of numerical examples, they emphasize that while it is the spectral radius of the iteration matrix $M^{-1}N$ that determines the asymptotic rate of convergence, it is the norms of the powers of this matrix that govern the behaviour of the iteration in the early stages. This point is also explained by Trefethen [1154, 1992], using the tool of pseudospectra.

Dennis and Walker [335, 1984] obtain bounds for $\| x - \widehat{x}_{k + 1}\| /\| x - \widehat{x}_k\|$ for stationary iteration as a special case of error analysis of quasi-Newton methods for nonlinear systems. The bounds in [335, 1984] do not readily yield information about normwise or componentwise forward stability.

Bollen [149, 1984] analyses the class of "descent methods" for solving $Ax = b$ , where $A$ is required to be symmetric positive definite; these are obtained by iteratively using exact line searches to minimize the quadratic function $F(x) =$

$(A^{-1}b - x)^T A(A^{-1}b - x)$ . The choice of search direction $p_k = b - Ax_k \eqqcolon r_k$ yields the steepest descent method, while $p_k = e_j$ (unit vector), where $|r_k|_j = \| r_k\|_{\infty}$ , gives the Gauss-Southwell method. Bollen shows that both methods are normwise backward stable as long as a condition of the form $c_n\kappa(A)u < 1$ holds. If the $p_k$ are cyclically chosen to be the unit vectors $e_1, e_2, \ldots, e_n$ then the Gauss-Seidel method results, but unfortunately no results specific to this method are given in [149, 1984].

Wozniakowski [1256, 1977] shows that the Chebyshev semi-iterative method is normwise forward stable but not normwise backward stable, and in [1257, 1978] he gives a normwise error analysis of stationary iterative methods. Some of the assumptions in [1257, 1978] are difficult to justify, as explained by Higham and Knight [618, 1993].

In [1258, 1980] Wozniakowski analyses a class of conjugate gradient algorithms (which does not include the usual conjugate gradient method). He obtains a forward error bound proportional to $\kappa(A)^{3/2}$ and a residual bound proportional to $\kappa(A)$ , from which neither backward nor forward normwise stability can be deduced. We note that as part of the analysis in [1258, 1980] Wozniakowski obtains a residual bound for the steepest descent method that is proportional to $\kappa(A)$ , and is therefore much weaker than the bound obtained by Bollen [149, 1984].

Zawilski [1277, 1991] shows that the cyclic Richardson method for symmetric positive definite systems is normwise forward stable provided the parameters are suitably ordered. He also derives a sharp bound for the residual that includes a factor $\kappa(A)$ , and which therefore shows that the method is not normwise backward stable.

Arioli and Romani [36, 1992] give a statistical error analysis of stationary iterative methods. They investigate the relations between a statistically defined asymptotic stability factor, ill conditioning of $M^{-1}A$ , where $A = M - N$ is the splitting, and the rate of convergence.

Greenbaum [519, 1989] presents a detailed error analysis of the conjugate gradient method, but her concern is with the rate of convergence rather than the attainable accuracy. An excellent survey of work concerned with the effects of rounding error on the conjugate gradient method (and the Lanczos method) is given by Greenbaum and Strakos in the introduction of [523, 1992]; see also Greenbaum [520, 1994]. Notay [895, 1993] analyses how rounding errors influence the convergence rate of the conjugate gradient method for matrices with isolated eigenvalues at the ends of the spectrum. Van der Vorst [1201, 1990] examines the effect of rounding errors on preconditioned conjugate gradient methods with incomplete Cholesky preconditioners. Greenbaum [521, 1997] analyses the limiting backward error for a general class of iterative methods that compute the residual $b - Ax_{k}$ by an updating formula rather than explicitly; this class includes the conjugate gradient method and several more recent methods. Numerical stability of the GM-RES method is analysed in [355, 1995], while error analysis of Krylov solvers for symmetric indefinite systems is treated in [1045, 2000].

The analysis given in the remainder of this chapter is from Higham and Knight [618, 1993], [619, 1993], wherein more details are given. Error analysis of Kaczmarz's row-action method is given by Knight [739, 1993].

# 17.2. Forward Error Analysis

A stationary iterative method has the form

$$
M x _ {k + 1} = N x _ {k} + b,
$$

where $A = M - N \in \mathbb{R}^{n \times n}$ is nonsingular and $M$ is nonsingular. We assume that the spectral radius $\rho(M^{-1}N) < 1$ , so that in exact arithmetic the iteration converges for any starting vector $x_0$ . We are not concerned with the size of constants in this analysis, so we denote by $c_n$ a constant of order $n$ .

The computed vectors $\widehat{x}_k$ satisfy an equality of the form

$$
(M + \Delta M _ {k + 1}) \widehat {x} _ {k + 1} = N \widehat {x} _ {k} + b + f _ {k},
$$

which we write as

$$
M \widehat {x} _ {k + 1} = N \widehat {x} _ {k} + b - \xi_ {k}, \tag {17.1}
$$

where

$$
\xi_ {k} = \Delta M _ {k + 1} \widehat {x} _ {k + 1} - f _ {k}.
$$

We will assume that $M$ is triangular (as is the case for the Jacobi, Gauss-Seidel, SOR, and Richardson iterations), so that $|\Delta M_{k + 1}| \leq c_n' u|M|$ and $f_k$ accounts solely for the errors in forming $N\widehat{x}_k + b$ . Hence

$$
\left| \xi_ {k} \right| \leq c _ {n} u \left(\left| M \right| \left| \widehat {x} _ {k + 1} \right| + \left| N \right| \left| \widehat {x} _ {k} \right| + | b |\right) =: \mu_ {k}. \tag {17.2}
$$

Solving the recurrence (17.1) we obtain

$$
\widehat {x} _ {m + 1} = G ^ {m + 1} x _ {0} + \sum_ {k = 0} ^ {m} G ^ {k} M ^ {- 1} (b - \xi_ {m - k}), \tag {17.3}
$$

where $G = M^{-1}N$ . Since the iteration is stationary at $x$ ,

$$
x = G ^ {m + 1} x + \sum_ {k = 0} ^ {m} G ^ {k} M ^ {- 1} b, \tag {17.4}
$$

and so the error $e_{m + 1} \coloneqq x - \widehat{x}_{m + 1}$ satisfies

$$
e _ {m + 1} = G ^ {m + 1} e _ {0} + \sum_ {k = 0} ^ {m} G ^ {k} M ^ {- 1} \xi_ {m - k}. \tag {17.5}
$$

We have

$$
\left| e _ {m + 1} \right| \leq \left| G ^ {m + 1} e _ {0} \right| + \sum_ {k = 0} ^ {m} \left| G ^ {k} M ^ {- 1} \right| \mu_ {m - k}, \tag {17.6}
$$

where $\mu_{k}$ is the bound for $\xi_{k}$ defined in (17.2). The first term, $|G^{m + 1}e_0|$ , is the error of the iteration in exact arithmetic and is negligible for large $m$ . The accuracy that can be guaranteed by the analysis is therefore determined by the last term in (17.6), and it is this term on which the rest of the analysis focuses.

At this point we can proceed by using further componentwise inequalities or by using norms. First we consider the norm approach. By taking norms in (17.6) and defining

$$
\gamma_ {x} = \sup  _ {k} \frac {\| \widehat {x} _ {k} \| _ {\infty}}{\| x \| _ {\infty}}, \tag {17.7}
$$

we obtain

$$
\begin{array}{l} \| e _ {m + 1} \| _ {\infty} \leq \| G ^ {m + 1} e _ {0} \| _ {\infty} + \max  _ {0 \leq k \leq m} \| \mu_ {k} \| _ {\infty} \sum_ {k = 0} ^ {m} \| G ^ {k} M ^ {- 1} \| _ {\infty} \\ \leq \| G ^ {m + 1} e _ {0} \| _ {\infty} + c _ {n} u (1 + \gamma_ {x}) (\| M \| _ {\infty} + \| N \| _ {\infty}) \| x \| _ {\infty} \\ \times \sum_ {k = 0} ^ {\infty} \| G ^ {k} M ^ {- 1} \| _ {\infty}, \tag {17.8} \\ \end{array}
$$

where the existence of the sum is assured by the result of Problem 17.1.

If $\| G\|_{\infty} = \| M^{-1}N\|_{\infty} = q < 1$ then (17.8) yields

$$
\| e _ {m + 1} \| _ {\infty} \leq \| G ^ {m + 1} e _ {0} \| _ {\infty} + c _ {n} u (1 + \gamma_ {x}) (\| M \| _ {\infty} + \| N \| _ {\infty}) \| x \| _ {\infty} \frac {\| M ^ {- 1} \| _ {\infty}}{1 - q}.
$$

Thus if $q$ is not too close to 1 ( $q \leq 0.9$ , say), and $\gamma_{x}$ and $\| M^{-1}\|_{\infty}$ are not too large, a small forward error is guaranteed for sufficiently large $m$ .

Of more interest is the following componentwise development of (17.6). Defining

$$
\theta_ {x} = \sup  _ {k} \max  _ {1 \leq i \leq n} \left(\frac {\left| \widehat {x} _ {k} \right| _ {i}}{\left| x _ {i} \right|}\right), \tag {17.9}
$$

so that $|\widehat{x}_k| \leq \theta_x|x|$ for all $k$ , we have from (17.2),

$$
\left| \mu_ {k} \right| \leq c _ {n} u \left(1 + \theta_ {x}\right) \left(\left| M \right| + \left| N \right|\right) | x |. \tag {17.10}
$$

Hence (17.6) yields

$$
\left| e _ {m + 1} \right| \leq \left| G ^ {m + 1} e _ {0} \right| + c _ {n} u \left(1 + \theta_ {x}\right) \left(\sum_ {k = 0} ^ {\infty} \left| G ^ {k} M ^ {- 1} \right|\right) \left(| M | + | N |\right) | x |, \tag {17.11}
$$

where, again, the existence of the sum is assured by the result of Problem 17.1. Since $A = M - N = M(I - M^{-1}N)$ we have

$$
A ^ {- 1} = \left(\sum_ {k = 0} ^ {\infty} (M ^ {- 1} N) ^ {k}\right) M ^ {- 1}.
$$

The sum in (17.11) is clearly an upper bound for $|A^{-1}|$ . Defining $c(A) \geq 1$ by

$$
c (A) = \min  \left\{\epsilon : \sum_ {k = 0} ^ {\infty} \left| \left(M ^ {- 1} N\right) ^ {k} M ^ {- 1} \right| \leq \epsilon \left| \sum_ {k = 0} ^ {\infty} \left(M ^ {- 1} N\right) ^ {k} M ^ {- 1} \right| = \epsilon | A ^ {- 1} | \right\}, \tag {17.12}
$$

we have our final bound

$$
\left| e _ {m + 1} \right| \leq \left| G ^ {m + 1} e _ {0} \right| + c _ {n} u \left(1 + \theta_ {x}\right) c (A) \left| A ^ {- 1} \right| \left(\left| M \right| + \left| N \right|\right) | x |. \tag {17.13}
$$

An interesting feature of stationary iteration methods is that if the elements of $M$ and $N$ are multiples of the elements in the corresponding positions of $A$ , then any scaling of the form $Ax = b \rightarrow D_1AD_2 \cdot D_2^{-1}x = D_1b$ ( $D_i$ diagonal) leaves the eigenvalues of $M^{-1}N$ unchanged; hence the asymptotic convergence rate is independent of row and column scaling. This scale independence applies to the Jacobi and SOR iterations, but not, for example, to the stationary Richardson iteration, for which $M = I$ . One of the benefits of doing a componentwise analysis is that under the above assumptions on $M$ and $N$ the bound (17.13) largely shares the scale independence. In (17.13) the scalar $c(A)$ is independent of the row and column scaling of $A$ , and the term $|A^{-1}|(|M| + |N|)|x|$ scales in the same way as $x$ . Furthermore, $\theta_x$ can be expected to depend only mildly on the row and column scaling, because the bound in (17.2) for the rounding error terms has the correct scaling properties.

What can be said about $c(A)$ ? In general, it can be arbitrarily large. Indeed, $c(A)$ is infinite for the Jacobi and Gauss-Seidel iterations for any $n \geq 3$ if $A$ is the symmetric positive definite matrix with $a_{ij} = \min(i,j)$ , because $A^{-1}$ is tridiagonal and $(M^{-1}N)^k M^{-1}$ is not.

If $M^{-1}$ and $M^{-1}N$ both have nonnegative elements then $c(A) = 1$ ; as we will see in the next section, this condition holds in some important instances.

Some further insight into $c(A)$ can be obtained by examining the case where $M^{-1}N \in \mathbf{C}^{n \times n}$ is diagonal with eigenvalues $\lambda_i$ . It is easy to show that $c(A) = \max_i |1 - \lambda_i| / (1 - |\lambda_i|)$ , so $c(A)$ can be large only if $\rho(M^{-1}N)$ is close to 1. Although $M^{-1}N$ cannot be diagonal for the Jacobi or Gauss-Seidel methods, this formula can be taken as being indicative of the size of $c(A)$ when $M^{-1}N$ is diagonalizable with a well-conditioned matrix of eigenvectors. We therefore have the heuristic inequality, for general $A$ ,

$$
c (A) \geq \max  _ {i} \frac {\left| 1 - \lambda_ {i} \right|}{1 - \left| \lambda_ {i} \right|}, \quad \lambda_ {i} = \lambda_ {i} \left(M ^ {- 1} N\right). \tag {17.14}
$$

In practical problems where stationary iteration is used, we would expect $c(A)$ to be of modest size $(O(n), \text{say})$ for two reasons. First, to achieve a reasonable convergence rate, $\rho(M^{-1}N)$ has to be safely less than 1, which implies that the heuristic lower bound (17.14) for $c(A)$ is not too large. Second, even if $A$ is sparse, $A^{-1}$ will usually be full, and so there are unlikely to be zeros on the right-hand side of (17.12). (Such zeros are dangerous because they can make $c(A)$ infinite.)

Note that in (17.13) the only terms that depend on the history of the iteration are $|G^{m + 1}e_0|$ and $\theta_{x}$ . In using this bound we can redefine $x_0$ to be any iterate $\widehat{x}_k$ , thereby possibly reducing $\theta_{x}$ . This is a circular argument if used to obtain a priori bounds, but it does suggest that the potentially large $\theta_{x}$ term will generally be innocuous. Note that if $x_i = 0$ for some $i$ then $\theta_{x}$ is infinite unless $(\widehat{x}_k)_i = 0$ for all $k$ . This difficulty with zero components of $x$ can usually be overcome by redefining

$$
\theta_ {x} = \sup  _ {k} \max  _ {1 \leq i \leq n} \frac {\left(\left(| M | + | N |\right) | \widehat {x} _ {k} |\right) _ {i}}{\left(\left(| M | + | N |\right) | x |\right) _ {i}},
$$

Table 17.2. Jacobi method, $a = 1/2 - 8^{-j}$ .   

<table><tr><td></td><td>ρ(M-1N)</td><td>Iters.</td><td>cond(A,x)</td><td>minkφ(x̂k)</td><td>minkηA,b(x̂k)</td></tr><tr><td>j=1</td><td>0.75</td><td>90</td><td>3.40</td><td>2.22e-16</td><td>1.27e-16</td></tr><tr><td>j=2</td><td>0.97</td><td>352</td><td>4.76</td><td>1.78e-15</td><td>9.02e-16</td></tr><tr><td>j=3</td><td>0.996</td><td>1974</td><td>4.97</td><td>1.42e-14</td><td>7.12e-15</td></tr><tr><td>j=4</td><td>1.00</td><td>11226</td><td>5.00</td><td>1.14e-13</td><td>5.69e-14</td></tr><tr><td>j=5</td><td>1.00</td><td>55412</td><td>5.00</td><td>9.10e-13</td><td>4.55e-13</td></tr></table>

for which the above bounds remain valid if $\theta_{x}$ is replaced by $2\theta_{x}$ .

Finally, we note that (17.13) implies

$$
\left\| e _ {m + 1} \right\| _ {\infty} \leq \left\| G ^ {m + 1} e _ {0} \right\| _ {\infty} + c _ {n} u (1 + \theta_ {x}) c (A) \| | A ^ {- 1} | (| M | + | N |) | x | \| _ {\infty}. \tag {17.15}
$$

If $\theta_{x}c(A) = O(1)$ and $|M| + |N|\leq \alpha |A|$ , with $\alpha = O(1)$ , this bound is of the form $c_{n}\operatorname {cond}(A,x)u$ as $m\to \infty$ , and we have componentwise forward stability.

Now we specialize the forward error bound (17.15) to the Jacobi, Gauss-Seidel, and SOR iterations.

# 17.2.1. Jacobi's Method

For the Jacobi iteration, $M = D = \mathrm{diag}(A)$ and $N = \mathrm{diag}(A) - A$ . Hence $|M| + |N| = |M - N| = |A|$ , and so (17.15) yields

$$
\left\| e _ {m + 1} \right\| _ {\infty} \leq \left\| G ^ {m + 1} e _ {0} \right\| _ {\infty} + c _ {n} u \left(1 + \theta_ {x}\right) c (A) \| | A ^ {- 1} | | A | | x | \| _ {\infty}. \tag {17.16}
$$

If $A$ is an $M$ -matrix then $M^{-1} \geq 0$ and $M^{-1}N \geq 0$ , so $c(A) = 1$ . Hence in this case we have componentwise forward stability as $m \to \infty$ if $\theta_{x}$ is suitably bounded.

Wozniakowski [1257, 1978, Ex. 4.1] cites the symmetric positive definite matrix

$$
A = \left[ \begin{array}{c c c} 1 & a & a \\ a & 1 & a \\ a & a & 1 \end{array} \right], \quad 0 <   a <   \frac {1}{2}, \quad \kappa_ {2} (A) = \frac {1 + 2 a}{1 - a}, \quad \rho (M ^ {- 1} N) = 2 a,
$$

as a matrix for which the Jacobi method can be unstable, in the sense that there exist rounding errors such that no iterate has a relative error bounded by $c_n \kappa_{\infty}(A) u$ . Let us see what our analysis predicts for this example. Straightforward manipulation shows that if $a = 1/2 - \epsilon$ ( $\epsilon > 0$ ), then $c(A) \approx (3\epsilon)^{-1}$ , so $c(A) \to \infty$ as $\epsilon \to 0$ . (The heuristic lower bound (17.14) is approximately $3(2\epsilon)^{-1}$ in this case.) Therefore (17.16) suggests that the Jacobi iteration can be unstable for this matrix. To confirm the instability we applied the Jacobi method to the problem with $x = [1,1,1]^T$ and $a = 1/2 - 8^{-j}$ , $j = 1:5$ . We took a random $x_0$ with $\| x - x_0 \|_2 = 10^{-10}$ , and the iteration was terminated when there was no decrease in the norm of the residual for 50 consecutive iterations. Table 17.2 reports the smallest value of $\phi(\widehat{x}_k) = \| x - \widehat{x}_k \|_{\infty} / \| x \|_{\infty}$ over all iterations, for each $j$ ; the number of iterations is shown in the column "Iters."

Table 17.3. Jacobi method, $a = -(1/2 - 8^{-j})$ .   

<table><tr><td></td><td>ρ(M-1N)</td><td>Iters.</td><td>cond(A,x)</td><td>minkφ(xk)</td><td>minkηA,b(xk)</td></tr><tr><td>j=1</td><td>0.75</td><td>39</td><td>7.00</td><td>4.44e-16</td><td>5.55e-17</td></tr><tr><td>j=2</td><td>0.97</td><td>273</td><td>6.30e1</td><td>4.88e-15</td><td>7.63e-17</td></tr><tr><td>j=3</td><td>0.996</td><td>1662</td><td>5.11e2</td><td>4.22e-14</td><td>8.24e-17</td></tr><tr><td>j=4</td><td>1.00</td><td>9051</td><td>4.09e3</td><td>3.41e-13</td><td>8.32e-17</td></tr><tr><td>j=5</td><td>1.00</td><td>38294</td><td>3.28e4</td><td>2.73e-12</td><td>8.33e-17</td></tr></table>

The ratio $\min_k\phi (\widehat{x}_k)_{j + 1} / \min_k\phi (\widehat{x}_k)_j$ takes the values 8.02, 7.98, 8.02, 7.98 for $j = 1:4$ , showing excellent agreement with the behaviour predicted by (17.16), since $c(A)\approx 8^j /3$ . Moreover, $\theta_{x}\approx 1$ in these tests and setting $c_{n}\approx 1$ the bound (17.16) is at most a factor 13.3 larger than the observed error, for each $j$ .

If $-1/2 < a < 0$ then $A$ is an $M$ -matrix and $c(A) = 1$ . The bound (17.16) shows that if we set $a = -(1/2 - 8^{-j})$ and repeat the above experiment then the Jacobi method will perform in a componentwise forward stable manner (clearly, $\theta_{x} \approx 1$ is to be expected). We carried out the modified experiment, obtaining the results shown in Table 17.3. All the $\min_k \phi(\widehat{x}_k)_j$ values are less than $\operatorname{cond}(A, x)u$ , so the Jacobi iteration is indeed componentwise forward stable in this case. Note that since $\rho(M^{-1}N)$ and $\| M^{-1}N \|_2$ take the same values for $a$ and $-a$ , the usual rate of convergence measures cannot distinguish between these two examples.

# 17.2.2. Successive Overrelaxation

The SOR method can be written in the form $Mx_{k + 1} = Nx_k + b$ , where

$$
M = \frac {1}{\omega} (D + \omega L), \quad N = \frac {1}{\omega} ((1 - \omega) D - \omega U),
$$

and where $A = D + L + U$ , with $L$ and $U$ strictly lower triangular and upper triangular, respectively. The matrix $|M| + |N|$ agrees with $|A|$ everywhere except, possibly, on the diagonal, and the best possible componentwise inequality between these two matrices is

$$
| M | + | N | \leq \frac {1 + | 1 - \omega |}{\omega} | A | \equiv f (\omega) | A |. \tag {17.17}
$$

Note that $f(\omega) = 1$ for $1 \leq \omega \leq 2$ , and $f(\omega) \to \infty$ as $\omega \to 0$ . From (17.15) we have

$$
\left\| e _ {m + 1} \right\| _ {\infty} \leq \left\| G ^ {m + 1} e _ {0} \right\| _ {\infty} + c _ {n} u (1 + \theta_ {x}) c (A) f (\omega) \| | A ^ {- 1} | | A | | x | \| _ {\infty}.
$$

If $A$ is an $M$ -matrix and $0 \leq \omega \leq 1$ then $M^{-1} \geq 0$ and $M^{-1}N \geq 0$ , so $c(A) = 1$ . The Gauss-Seidel method corresponds to $\omega = 1$ , and it is interesting to note that for this method the forward error bound has exactly the same form as that for the Jacobi method (though $c(A)$ and $\theta_{x}$ are, of course, different for the two methods).

# 17.3. Backward Error Analysis

We now turn our attention to bounding the residual vector, $r_k = b - A\hat{x}_k$

From (17.3) and (17.4) we find that

$$
r _ {m + 1} = A G ^ {m + 1} (x - x _ {0}) + \sum_ {k = 0} ^ {m} A G ^ {k} M ^ {- 1} \xi_ {m - k}.
$$

It is easy to show that $AG^{k} = H^{k}A$ , where $H \coloneqq NM^{-1}$ (recall that $G = M^{-1}N$ ). Therefore

$$
r _ {m + 1} = H ^ {m + 1} r _ {0} + \sum_ {k = 0} ^ {m} H ^ {k} (I - H) \xi_ {m - k}. \tag {17.18}
$$

Taking norms and using (17.2) gives, similarly to (17.8),

$$
\left\| r _ {m + 1} \right\| _ {\infty} \leq \left\| H ^ {m + 1} r _ {0} \right\| _ {\infty} + c _ {n} u \sigma \left(1 + \gamma_ {x}\right) \left(\left\| M \right\| _ {\infty} + \left\| N \right\| _ {\infty}\right) \| x \| _ {\infty}, \tag {17.19}
$$

where

$$
\sigma = \left\| \sum_ {k = 0} ^ {\infty} | H ^ {k} (I - H) | \right\| _ {\infty}.
$$

The following bound shows that $\sigma$ is small if $\| H\|_{\infty} = q < 1$ , with $q$ not too close to 1:

$$
\sigma \leq \| I - H \| _ {\infty} \sum_ {k = 0} ^ {\infty} \| H \| _ {\infty} ^ {k} = \frac {\| I - H \| _ {\infty}}{1 - q}.
$$

A potentially much smaller bound can be obtained under the assumption that $H$ is diagonalizable. If $H = XDX^{-1}$ , with $D = \mathrm{diag}(\lambda_i)$ , then

$$
\begin{array}{l} \sigma = \left\| \sum_ {k = 0} ^ {\infty} | X (D ^ {k} - D ^ {k + 1}) X ^ {- 1} | \right\| _ {\infty} \\ \leq \left\| | X | \left(\sum_ {k = 0} ^ {\infty} \operatorname {d i a g} \left(| 1 - \lambda_ {i} | | \lambda_ {i} ^ {k} |\right)\right) | X ^ {- 1} | \right\| _ {\infty} \\ = \left\| | X | \operatorname {d i a g} \left(\frac {| 1 - \lambda_ {i} |}{1 - | \lambda_ {i} |}\right) | X ^ {- 1} | \right\| _ {\infty} \\ \leq \kappa_ {\infty} (X) \max  _ {i} \frac {\left| 1 - \lambda_ {i} \right|}{1 - \left| \lambda_ {i} \right|}. \tag {17.20} \\ \end{array}
$$

Note that $\lambda_{i} = \lambda_{i}(H) = \lambda_{i}(NM^{-1}) = \lambda_{i}(M^{-1}N)$ , so we see the reappearance of the term in the heuristic bound (17.14). The bound (17.20) is of modest size if the eigenproblem for $H$ is well conditioned ( $\kappa_{\infty}(X)$ is small) and $\rho(H)$ is not too close to 1. Note that real eigenvalues of $H$ near $+1$ do not affect the bound for $\sigma$ , even though they may cause slow convergence.

To summarize, (17.19) shows that, for large $m$ , the normwise backward error $\eta_{A,b}(\widehat{x}_m)$ for the $\infty$ -norm is certainly no larger than

$$
c _ {n} u (1 + \gamma_ {x}) \Big (\frac {\| M \| _ {\infty} + \| N \| _ {\infty}}{\| A \| _ {\infty}} \Big) \sigma .
$$

Note that $\| M\|_{\infty} + \| N\|_{\infty}\leq 2\| A\|_{\infty}$ for the Jacobi and Gauss-Seidel methods, and also for the SOR method if $\omega \geq 1$

A componentwise residual bound can also be obtained, but it does not lead to any identifiable classes of matrix or iteration for which the componentwise relative backward error is small.

To conclude, we return to our numerical examples. For the SOR example at the start of the chapter, $c(A) = O(10^{45})$ and $\sigma = O(10^{30})$ , so our error bounds for this problem are all extremely large. In this problem $\max_i |1 - \lambda_i| / (1 - |\lambda_i|) = 3$ where $\lambda_i = \lambda_i(M^{-1}N)$ , so (17.14) is very weak; (17.20) is not applicable since $M^{-1}N$ is defective.

For the first numerical example in §17.2.1, Table 17.2 reports the minimum $\infty$ -norm backward errors $\eta_{A,b}(\widehat{x}_k)$ . For this problem it is straightforward to show that $\sigma = (1 - \epsilon) / \epsilon = 8^j (1 - 8^{-j})$ . The ratios of backward errors for successive values of $j$ are 7.10, 7.89, 7.99, 8.00, so we see excellent agreement with the behaviour predicted by the bounds. Table 17.3 reports the normwise backward errors for the second numerical example in §17.2.1. The backward errors are all less than $u$ , which again is close to what the bounds predict, since it can be shown that $\sigma \leq 5$ for $-1/2 \leq a \leq 0$ . In both of the examples of §17.2.1 the componentwise backward error $\omega_{|A|,|b|}(\widehat{x}_k) \approx \eta_{A,b}(\widehat{x}_k)$ , and in our practical experience this behaviour is typical for the Jacobi and SOR iterations.

# 17.4. Singular Systems

Singular linear systems occur in a variety of applications, including the computation of the stationary distribution vector in a Markov chain [106, 1994], [717, 1983] and the solution of a Neumann boundary value problem by finite difference methods [943, 1976]. Because of the structure and the possibly large dimension of the coefficient matrices in these applications, iterative solution methods are frequently used. An important question is how the rather delicate convergence properties of the iterative methods are affected by rounding errors. In this section we extend the analysis of stationary iteration to singular systems.

# 17.4.1. Theoretical Background

A useful tool in analysing the behaviour of stationary iteration for a singular system is the Drazin inverse. This can be defined, for $A \in \mathbb{R}^{n \times n}$ , as the unique matrix $A^D$ such that

$$
A ^ {D} A A ^ {D} = A ^ {D}, \quad A A ^ {D} = A ^ {D} A, \quad \text {a n d} \quad A ^ {k + 1} A ^ {D} = A ^ {k},
$$

where $k = \operatorname{index}(A)$ . The index of $A$ is the smallest nonnegative integer $k$ such that $\operatorname{rank}(A^k) = \operatorname{rank}(A^{k+1})$ ; it is characterized as the dimension of the largest Jordan block of $A$ with eigenvalue zero. If $\operatorname{index}(A) = 1$ then $A^D$ is also known as the group inverse of $A$ and is denoted by $A^\#$ . The Drazin inverse is an "equation-solving inverse" precisely when $\operatorname{index}(A) \leq 1$ , for then $AA^D A = A$ , and so if $Ax = b$ is a consistent system then $A^D b$ is a solution. As we will see, however, the Drazin inverse of the coefficient matrix $A$ itself plays no role in the analysis. The

Drazin inverse can be represented explicitly as follows. If

$$
A = P \left[ \begin{array}{c c} B & 0 \\ 0 & N \end{array} \right] P ^ {- 1},
$$

where $P$ and $B$ are nonsingular and $N$ has only zero eigenvalues, then

$$
A ^ {D} = P \left[ \begin{array}{c c} B ^ {- 1} & 0 \\ 0 & 0 \end{array} \right] P ^ {- 1}.
$$

Further details of the Drazin inverse can be found in Campbell and Meyer's excellent treatise [199, 1979, Chap. 7].

Let $A \in \mathbb{R}^{n \times n}$ be a singular matrix and consider solving $Ax = b$ by stationary iteration with a splitting $A = M - N$ , where $M$ is nonsingular. First, we examine the convergence of the iteration in exact arithmetic. Since any limit point $x$ of the sequence $\{x_k\}$ must satisfy $Mx = Nx + b$ , or $Ax = b$ , we restrict our attention to consistent linear systems. (For a thorough analysis of stationary iteration for inconsistent systems see Dax [297, 1990].) As in the nonsingular case we have the relation (cf. (17.4)):

$$
x _ {m + 1} = G ^ {m + 1} x _ {0} + \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} b, \tag {17.21}
$$

where $G = M^{-1}N$ . Since $A$ is singular, $G$ has an eigenvalue 1, so $G^{m}$ does not tend to zero as $m \to \infty$ , that is, $G$ is not convergent. If the iteration is to converge for all $x_{0}$ then $\lim_{m \to \infty} G^{m}$ must exist. Following Meyer and Plemmons [846, 1977], we call a matrix $B$ for which $\lim_{m \to \infty} B^{m}$ exists semiconvergent.

We assume from this point on that $G$ is semiconvergent. It is easy to see [106, 1994, Lem. 6.9] that $G$ must have the form

$$
G = P \left[ \begin{array}{c c} I & 0 \\ 0 & \Gamma \end{array} \right] P ^ {- 1}, \tag {17.22}
$$

where $P$ is nonsingular and $\rho (\Gamma) < 1$ . Hence

$$
\lim _ {m \to \infty} G ^ {m} = P \left[ \begin{array}{l l} I & 0 \\ 0 & 0 \end{array} \right] P ^ {- 1}.
$$

To rewrite this limit in terms of $G$ , we note that

$$
I - G = P \left[ \begin{array}{c c} 0 & 0 \\ 0 & I - \Gamma \end{array} \right] P ^ {- 1}, \tag {17.23}
$$

and, since $I - \Gamma$ is nonsingular,

$$
(I - G) ^ {D} = P \left[ \begin{array}{c c} 0 & 0 \\ 0 & (I - \Gamma) ^ {- 1} \end{array} \right] P ^ {- 1}. \tag {17.24}
$$

Hence

$$
\lim  _ {m \rightarrow \infty} G ^ {m} = I - (I - G) ^ {D} (I - G). \tag {17.25}
$$

To evaluate the limit of the second term in (17.21) we note that, since the system is consistent, $M^{-1}b = M^{-1}Ax = (I - G)x$ , and so

$$
\begin{array}{l} \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} b = \sum_ {i = 0} ^ {m} G ^ {i} (I - G) x \\ = (I - G ^ {m + 1}) x \\ \rightarrow (I - G) ^ {D} (I - G) x = (I - G) ^ {D} M ^ {- 1} b. \\ \end{array}
$$

We note in passing that the condition that $G$ is semiconvergent is equivalent to $I - G$ having index 1, in view of (17.23), but that this condition does not imply that $A = M(I - G)$ has index 1.

The conclusion is that if $G$ is semiconvergent, stationary iteration converges to a solution of $Ax = b$ that depends on $x_0$ :

$$
\lim  _ {m \rightarrow \infty} x _ {m} = (I - (I - G) ^ {D} (I - G)) x _ {0} + (I - G) ^ {D} M ^ {- 1} b. \tag {17.26}
$$

The first term in this limit is in $\mathrm{null}(I - G)$ and the second term is in $\mathrm{range}(I - G)$ . To obtain the unique solution in $\mathrm{range}(I - G)$ we should take for $x_0$ any vector in $\mathrm{range}(I - G)$ ( $x_0 = 0$ , say).

# 17.4.2. Forward Error Analysis

We wish to bound $e_{m+1} = x - \widehat{x}_{m+1}$ , where $x$ is the limit in (17.26) corresponding to the given starting vector $x_0$ . The analysis proceeds as in the nonsingular case, up to the derivation of equation (17.5):

$$
e _ {m + 1} = G ^ {m + 1} e _ {0} + \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} \xi_ {m - i}.
$$

As before, the first term, $G^{m + 1}e_0$ , is negligible for large $m$ , because it is the error after $m + 1$ stages of the exact iteration and this error tends to zero. To obtain a useful bound for the second term, we cannot simply take norms or absolute values, because $\sum_{i = 0}^{m}G^{i}$ grows unboundedly with $m$ (recall that $G$ has an eigenvalue 1). Our approach is to split the vectors $\xi_{i}$ according to $\xi_{i} = \xi_{i}^{(1)} + \xi_{i}^{(2)}$ , where $M^{-1}\xi_i^{(1)}\in \mathrm{range}(I - G)$ and $M^{-1}\xi_i^{(2)}\in \mathrm{null}(I - G)$ ; this is a well-defined splitting because $\mathrm{range}(I - G)$ and $\mathrm{null}(I - G)$ are complementary subspaces (since index $(I - G) = 1$ , or equivalently, $G$ is semiconvergent). Using the properties of the splitting the error can be written as

$$
\begin{array}{l} e _ {m + 1} = G ^ {m + 1} e _ {0} + \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} \xi_ {m - i} ^ {(1)} + \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} \xi_ {m - i} ^ {(2)} \\ = G ^ {m + 1} e _ {0} + \sum_ {i = 0} ^ {m} G ^ {i} M ^ {- 1} \xi_ {m - i} ^ {(1)} + M ^ {- 1} \sum_ {i = 0} ^ {m} \xi_ {m - i} ^ {(2)}. \\ \end{array}
$$

We achieve the required splitting for $\xi_{i}$ via the formulae

$$
\xi_ {i} ^ {(1)} = M E M ^ {- 1} \xi_ {i}, \quad \xi_ {i} ^ {(2)} = M (I - E) M ^ {- 1} \xi_ {i},
$$

where

$$
E = (I - G) ^ {D} (I - G).
$$

Hence the error can be written as

$$
e _ {m + 1} = G ^ {m + 1} e _ {0} + \sum_ {i = 0} ^ {m} G ^ {i} E M ^ {- 1} \xi_ {m - i} + (I - E) M ^ {- 1} \sum_ {i = 0} ^ {m} \xi_ {m - i}. \tag {17.27}
$$

Clearly, as $m \to \infty$ the final term in this expression can become unbounded, but since it grows only linearly in the number of iterations it is unlikely to have a significant effect in applications where stationary iteration converges quickly enough to be of practical use.

Now we bound the term

$$
S _ {m} = \sum_ {i = 0} ^ {m} G ^ {i} E M ^ {- 1} \xi_ {m - i}. \tag {17.28}
$$

Using inequality (17.2) and the definition of $\gamma_{x}$ in (17.7) and $\theta_{x}$ in (17.9), we have

$$
\begin{array}{l} \| S _ {m} \| _ {\infty} \leq c _ {n} u (1 + \gamma_ {x}) (\| M \| _ {\infty} + \| N \| _ {\infty}) \| x \| _ {\infty} \sum_ {i = 0} ^ {m} \| G ^ {i} E M ^ {- 1} \| _ {\infty}, \\ \left| S _ {m} \right| \leq c _ {n} u \left(1 + \theta_ {x}\right) \sum_ {i = 0} ^ {m} \left| G ^ {i} E M ^ {- 1} \right| \left(\left| M \right| + \left| N \right|\right) | x |. \tag {17.29} \\ \end{array}
$$

The convergence of the two infinite sums is assured by the result of Problem 17.1, since by (17.22)-(17.24),

$$
\begin{array}{l} G ^ {i} E = G ^ {i} (I - G) ^ {D} (I - G) \\ = P \left[ \begin{array}{c c} I & 0 \\ 0 & \Gamma^ {i} \end{array} \right] P ^ {- 1} \cdot P \left[ \begin{array}{c c} 0 & 0 \\ 0 & (I - \Gamma) ^ {- 1} \end{array} \right] P ^ {- 1} \cdot P \left[ \begin{array}{c c} 0 & 0 \\ 0 & (I - \Gamma) \end{array} \right] P ^ {- 1} \\ = P \left[ \begin{array}{c c} 0 & 0 \\ 0 & \Gamma^ {i} \end{array} \right] P ^ {- 1} = (G E) ^ {i} \quad (i \geq 1), \tag {17.30} \\ \end{array}
$$

where $\rho (\varGamma) < 1$

We conclude that we have the normwise error bound

$$
\begin{array}{l} \left\| e _ {m + 1} \right\| _ {\infty} \leq \left\| G ^ {m + 1} e _ {0} \right\| _ {\infty} + c _ {n} u (1 + \gamma_ {x}) (\left\| M \right\| _ {\infty} + \left\| N \right\| _ {\infty}) \| x \| _ {\infty} \\ \times \left\{\sum_ {i = 0} ^ {\infty} \| G ^ {i} E M ^ {- 1} \| _ {\infty} + (m + 1) \| (I - E) M ^ {- 1} \| _ {\infty} \right\}. \tag {17.31} \\ \end{array}
$$

On setting $E = I$ we recover the result (17.8) for the nonsingular case. If we assume that $\Gamma$ is diagonal, so that $P$ in (17.30) is a matrix of eigenvectors of $G$ , then

$$
\sum_ {i = 0} ^ {\infty} \| G ^ {i} E M ^ {- 1} \| _ {\infty} \leq \kappa_ {\infty} (P) \| M ^ {- 1} \| _ {\infty} \frac {1}{1 - \rho (\Gamma)}.
$$

This bound shows that a small forward error is guaranteed if $\kappa(P) \| M^{-1} \| = O(1)$ and the second largest eigenvalue of $G$ is not too close to 1. (It is this subdominant eigenvalue that determines the asymptotic rate of convergence of the iteration.)

Turning to the componentwise case, we see from (17.24) and (17.30) that

$$
\sum_ {i = 0} ^ {\infty} G ^ {i} E = \left(I - G\right) ^ {D}.
$$

Because of the form of the sum in (17.29), this prompts us to define the scalar $c(A) \geq 1$ by

$$
c (A) = \operatorname * {m i n} \biggl \{\epsilon : \sum_ {i = 0} ^ {\infty} | G ^ {i} E M ^ {- 1} | \leq \epsilon | (I - G) ^ {D} M ^ {- 1} | \biggr \},
$$

in terms of which we have the componentwise error bound

$$
\begin{array}{l} \left| e _ {m + 1} \right| \leq \left| G ^ {m + 1} e _ {0} \right| + c _ {n} u \left(1 + \theta_ {x}\right) \left\{c (A) \mid \left(I - G\right) ^ {D} M ^ {- 1} \right| \\ + (m + 1) \left| (I - E) M ^ {- 1} \right| \} (| M | + | N |) | x |. \tag {17.32} \\ \end{array}
$$

Again, as a special case we have the result for nonsingular $A$ , (17.13).

To what should we compare this bound? A perturbation result for $Ax = b$ is given in [619, 1993] that projects the perturbations of $A$ and $b$ into $\text{range}(I - G)$ and thus can be thought of as gauging the effect of perturbations to the "nonsingular part of the system". For perturbations of order $\epsilon$ it gives an expression

$$
\Delta x = (I - G) ^ {D} M ^ {- 1} (\Delta b - \Delta A x) + O \left(\epsilon^ {2}\right).
$$

Hence we can deduce conditions on a stationary iterative method that ensure it is componentwise forward stable, in the sense of yielding a solution whose error is no larger than the uncertainty in $x$ caused by rounding the data. The constants $\theta_{x}$ and $c(A)$ should be bounded by $d_{n}$ , where $d_{n}$ denotes a slowly growing function of $n$ ; the inequality $|M| + |N| \leq d_n'|A|$ should hold, as it does for the Jacobi method and for the SOR method when $\omega \in [\beta, 2]$ , where $\beta$ is positive and not too close to zero; and the "exact error" $G^{m+1}e_{0}$ must decay quickly enough to ensure that the term $(m+1)|(I-E)M^{-1}|$ does not grow too large before the iteration is terminated.

Numerical results given in [619, 1993] show that the analysis can correctly predict forward and backward stability, and that for certain problems linear growth of the component of the error in $\mathrm{null}(A)$ can indeed cause an otherwise convergent iteration to diverge, even when starting very close to a solution.

# 17.5. Stopping an Iterative Method

What convergence test should be used to stop an iterative linear equation solver? In this section we explain how backward errors and condition numbers help answer this question. Note first that most iterative methods for solving $Ax = b$ compute all or part of a matrix-vector product $w = Av$ on each iteration, and in floating point arithmetic we have

$$
\widehat {w} = (A + \Delta A) v, \quad | \Delta A | \leq \gamma_ {m} | A |,
$$

where $m$ is the maximum number of nonzeros per row of $A$ . The method therefore cannot distinguish between $A$ and $A + \Delta A$ where $|\Delta A| \leq \gamma_m |A|$ , and so there is no point in trying to achieve a componentwise relative backward error less than $\gamma_m$ . Of course, instability of a method (or simply lack of convergence) may pose further restrictions on how small a backward error can be achieved.

It is worth keeping in mind throughout this discussion that in practical applications accuracy and stability requirements are often quite modest because of large errors or uncertainties in the data, or because the iteration is an "inner step" of some "outer" iterative process. Indeed, one of the advantages of iterative methods is that the slacker the convergence tolerance the less computational effort is required, though the relation between tolerance and work depends very much on the method.

Natural stopping criteria for an iterative method are that some measure of backward error or forward error does not exceed a tolerance, $\epsilon$ . We will assume that the residual $r = b - Ay$ is available for each iterate $y$ , and that norms of $y$ , $r$ , and $A$ can be computed or estimated. If $r$ is not computed directly, but is recurred by the method, as, for example, in the conjugate gradient method, then the norm of the computed residual may differ from that of the true residual by several orders of magnitude; clearly, this affects the way that the stopping tests are interpreted.

From Theorem 7.1 we have the following equivalences, for any subordinate matrix norm:

$$
\| r \| \leq \epsilon \| b \| \iff A y = b + \Delta b, \| \Delta b \| \leq \epsilon \| b \|, \tag {17.33a}
$$

$$
\| r \| \leq \epsilon \| A \| \| y \| \iff (A + \Delta A) y = b, \| \Delta A \| \leq \epsilon \| A \|, \tag {17.33b}
$$

$$
\begin{array}{l} \| r \| \leq \epsilon (\| A \| \| y \| + \| b \|) \iff (A + \Delta A) y = b + \Delta b, \\ \| \Delta A \| \leq \epsilon \| A \|, \quad \| \Delta b \| \leq \epsilon \| b \|. \tag {17.33c} \\ \end{array}
$$

These inequalities remain true with norms replaced by absolute values (Theorem 7.3), but then to evaluate (17.33b) and (17.33c) a matrix-vector product $|A||y|$ must be computed, which is a nontrivial expense in an iterative method.

Of these tests, (17.33c) is preferred in general, assuming it is acceptable to perturb both $A$ and $b$ . Note the importance of including both $\| A \|$ and $\| y \|$ in the test on $\| r \|$ ; a test $\| r \| \leq \epsilon \| A \|$ , though scale independent, does not bound any relative backward error. Test (17.33a) is commonly used in existing codes, but may be very stringent, and possibly unsatisfiable. To see why, note that the residual of the rounded exact solution $f l(x) = x + \Delta x$ , $|\Delta x| \leq u|x|$ , satisfies, for any absolute norm,

$$
\| r \| = \| b - A (x + \Delta x) \| \leq u \| A \| \| x \|,
$$

and

$$
\frac {\| A \| \| x \|}{\kappa (A)} \leq \| b \| \leq \| A \| \| x \|.
$$

If $A$ is ill conditioned and $x$ is a large-normed solution (that is, $\| x \| \approx \| A^{-1} \| \| b \|$ ), so that $\| b \|$ is close to its lower bound, then (17.33a) is much harder to satisfy than (17.33c).

If the forward error is to be bounded, then, for a nonsingular problem, tests can be derived involving the residual and $A^{-1}$ : the equality $x - y = A^{-1}r$ leads to normwise and componentwise forward error bounds, such as $\| x - y\| /\| y\| \leq \| A^{-1}\| \| r\| /\| y\|$ (cf. Problem 7.2). Since these bounds involve $A^{-1}$ , they are nontrivial to compute. Some iterative methods automatically produce estimates of the extremal eigenvalues, and hence of $\kappa_{2}(A) = \lambda_{\max}(A) / \lambda_{\min}(A)$ . For large, sparse symmetric positive definite matrices $\| A^{-1}\| _2$ can be cheaply estimated using the Lanczos method. Another possibility is to use condition estimation techniques (Chapter 15).

The discussion in this section has inevitably been very general. Other considerations in practice include detecting nonconvergence of a method (due to rounding errors or otherwise), adapting the tests to accommodate a preconditioner (the residual $r$ provided by the method may now be that for the preconditioned system), and using a norm that corresponds to a quantity being minimized by the method (a norm that may be nontrivial to compute). Moreover, it may be possible to design a stopping criterion that relates to the error or residual for the original problem that lead to the linear system; how to do this for the conjugate gradient method applied to linear systems produced by the finite element method is explained by Arioli [34, 2000].

# 17.6. Notes and References

The Gauss-Seidel method was chosen by Wilkinson [1224, 1948] as an "example of coding" for the ACE. Speaking of his experience at that time at the National Physical Laboratory, he explained that "In general, direct methods have been used on those equations which did not yield readily to relaxation, and hence those solved by direct methods have nearly always been of an ill-conditioned type".

Stationary iterative methods are relatively easy to program, although there are many issues to consider when complicated data structures or parallel machines are used. A good source of straightforward C, Fortran, and MATLAB implementations of the Jacobi, Gauss-Seidel, and SOR methods, and other nonstationary iterative methods, is the book Templates for the Solution of Linear Systems [80, 1994]; the software is available from netlib. The book contains theoretical discussions of the methods, together with practical advice on topics such as data structures and the choice of a stopping criterion. The choice of stopping criteria for iterative methods is also discussed by Arioli, Duff, and Ruiz [35, 1992].

Recent textbooks on iterative methods include those by Axelsson [42, 1994] and Greenbaum [522, 1997]. Numerical linear algebra textbooks that have good coverage of iterative methods include Demmel [317, 1997] and Trefethen and Bau [1156, 1997].

# Problems

17.1. Show that if $B \in \mathbb{R}^{n \times n}$ and $\rho(B) < 1$ , then the series $\sum_{k=0}^{\infty} |B^k|$ and $\sum_{k=0}^{\infty} \|B^k\|$ are both convergent, where $\| \cdot \|$ is any norm.
