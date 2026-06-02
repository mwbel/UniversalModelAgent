# Chapter 11. Hermite Integral Formula

If there is a single most valuable mathematical tool in the analysis of accuracy of polynomial approximations, it is contour integrals in the complex plane.5 From a contour integral one can see why some approximations are extraordinarily good, like interpolation in Chebyshev points, and others are impossibly bad, like interpolation in equispaced points. This chapter presents the basics of the contour integrals, and the next applies them to take some first steps toward the subject of potential theory, which relates the accuracy of approximations to equipotential or minimal-energy problems for electrostatic charge distributions in the plane.

The starting ingredients have already appeared in Chapter 5. Following the formulation there, let $x _ { 0 } , \ldots , x _ { n }$ be a set of $n + 1$ distinct interpolation or “grid” points, which may be real or complex, and define the node polynomial $\ell \in \mathcal { P } _ { n + 1 }$ a s in (5.4) by

$$
\ell ( x ) = \prod _ { k = 0 } ^ { n } ( x - x _ { k } ) .
$$

Repeating (5.5), the function

$$
\ell _ { j } ( x ) = { \frac { \ell ( x ) } { \ell ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) } }
$$

is the Lagrange polynomial associated with $x _ { j }$ , that is, the unique polynomial in $\mathcal { P } _ { n }$ that takes the value 1 at $x _ { j }$ and $0$ at the other points $x _ { k }$ . Following (5.1), a linear combination of these functions gives the interpolant in $\mathcal { P } _ { n }$ to an arbitrary function

$f$ defined on the grid:

$$
p ( x ) = \sum _ { j = 0 } ^ { n } f ( x _ { j } ) \ell _ { j } ( x ) .
$$

We now make a crucial observation. Let $\Gamma _ { j }$ be a contour in the complex $x$ -plane that encloses $x _ { j }$ but none of the other grid points, nor the point $x$ . (By “encloses” we always mean that it winds around the specified set once in the counterclockwise direction, in the usual sense of complex variables.) Then the expression on the right in (11.2) can be written as

$$
{ \frac { \ell ( x ) } { \ell ^ { \prime } ( x _ { j } ) \left( x - x _ { j } \right) } } = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { j } } { \frac { \ell ( x ) } { \ell ( t ) ( x - t ) } } d t .
$$

To verify this formula we ignore the $\ell ( x )$ term on both sides, which has nothing to do with the integral, and use the fact that $1 / ( \ell ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) )$ is the residue of the function $1 / ( \ell ( t ) ( x - t ) )$ at the pole $t = x _ { j }$ .

From (11.2) and (11.4) we thus have an expression for $\ell _ { j } ( x )$ as a contour integral:

$$
\ell _ { j } ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { j } } { \frac { \ell ( x ) } { \ell ( t ) ( x - t ) } } d t ,
$$

where $\Gamma _ { j }$ encloses $x _ { j }$ . Now let $\Gamma ^ { \prime }$ be a contour that encloses all of the grid points $\{ x _ { j } \}$ , but still not the point $x$ , and let $f$ be a function analytic on and interior to $\Gamma ^ { \prime }$ . Then we can combine these integrals to get an expression for the interpolant $p$ to $f$ in $\{ x _ { j } \}$ :

$$
p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma ^ { \prime } } { \frac { \ell ( x ) f ( t ) } { \ell ( t ) ( x - t ) } } d t .
$$

Note how neatly this formula replaces the sum of (11.3) by a contour integral with contributions from the same points $x _ { j }$ .

Now suppose we enlarge the contour of integration to a new contour $\Gamma$ that encloses $x$ as well as $\{ x _ { j } \}$ , and we assume $f$ is analytic on and inside $\Gamma$ . The residue of the integrand of (11.6) at $t = x$ is $- f ( x )$ , so this brings in a new contribution $- f ( x )$ to the integral, yielding an equation for the error in polynomial interpolation:

$$
p ( x ) - f ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) f ( t ) } { \ell ( t ) ( x - t ) } } d t .
$$

And thus we have derived one of the most powerful formulas in all of approximation theory, the Hermite integral formula. This name comes from Hermite [1878], but nearly the same result was stated 52 years earlier by Cauchy [1826]. (Hermite, however, generalized the discussion significantly to nondistinct or “confluent” interpolation points and corresponding interpolation of derivatives as well as function values; see Exercise 11.2.)

Theorem 11.1. Hermite integral formula. Let $f$ be analytic in a region $\Omega$ containing distinct points $x _ { 0 } , \ldots , x _ { n }$ , and let $\Gamma$ be a contour in $\Omega$ enclosing these points in the positive direction. The polynomial interpolant $p \in \mathcal { P } _ { n }$ to $f$ at $\{ x _ { j } \}$ is

$$
p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { f ( t ) \left( \ell ( t ) - \ell ( x ) \right) } { \ell ( t ) \left( t - x \right) } } d t ,
$$

and if $_ { x }$ is enclosed by $\Gamma$ , the error in the interpolant is

$$
f ( x ) - p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) } { \ell ( t ) } } { \frac { f ( t ) } { ( t - x ) } } d t .
$$

Proof. Equation (11.9) is the same as (11.7). For (11.8), we note that if $\Gamma$ encloses $x$ , then $f ( x )$ can be written

$$
f ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( t ) f ( t ) } { \ell ( t ) ( t - x ) } } d t ,
$$

and combining this with (11.7) gives the result. But the integrand of (11.8) has no pole at $t = x$ , so the same result also applies if $\Gamma$ does not enclose $x$ .

It is perhaps interesting to sketch Cauchy’s slightly different derivation from 1826, outlined in [Smithies 1997, p. 117], which may have been influenced by Jacobi’s thesis a year earlier [Jacobi 1825]. Cauchy started from the observation that $p ( x ) / \ell ( x )$ is a rational function with denominator degree greater than the numerator degree. This implies that it must be equal to the sum of the $n + 1$ inverse-linear functions $r _ { j } / ( x - x _ { j } )$ , where $r _ { j }$ is the residue of $p ( t ) / \ell ( t )$ at $t = x _ { j }$ (a partial fraction decomposition, to be discussed further in Chapter 23). Since $p$ interpolates $f$ at $\{ x _ { j } \}$ , $r _ { j }$ is also the residue of $f ( t ) / \ell ( t )$ at $t = x _ { j }$ . By residue calculus we therefore have

$$
{ \frac { p ( x ) } { \ell ( x ) } } = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma ^ { \prime } } { \frac { f ( t ) } { \ell ( t ) \left( x - t \right) } } d t
$$

if $\Gamma ^ { \prime }$ is again a contour that encloses the points $\{ x _ { k } \}$ but not $x$ itself, or equivalently, (11.6).

Now let us see how Theorem 11.1 can be used to estimate the accuracy of polynomial interpolants.

Suppose $f$ and $x$ are fixed and we want to estimate $f ( x ) - p ( x )$ for various degrees $n$ and corresponding sets of $n + 1$ points $\{ x _ { j } \}$ . On a fixed contour $\Gamma$ , the quantities $f ( t )$ and $t - x$ in (11.9) are independent of $n$ . The ratio

$$
{ \frac { \ell ( x ) } { \ell ( t ) } } = { \frac { \prod _ { j = 0 } ^ { n } ( x - x _ { j } ) } { \prod _ { j = 0 } ^ { n } ( t - x _ { j } ) } } ,
$$

however, is another matter. If $\Gamma$ is far enough from $\{ x _ { j } \}$ , then for each $t \in \Gamma$ , this ratio will shrink exponentially as $n \to \infty$ , and if this happens, we may conclude from (11.9) that $p ( x )$ converges exponentially to $f ( x )$ as $n \to \infty$ . The crucial condition for this argument is that it must be possible for $f$ to be analytically continued as far out as $\Gamma$ .

Here is a warm-up example mentioned on p. 63 of [Gaier 1987]. Suppose the interpolation points $\{ x _ { j } \}$ lie in $[ - 1 , 1 ]$ for each $n$ and $x \in \left[ { - 1 , 1 } \right]$ also. Let $S$ be the “stadium” in the complex plane consisting of all numbers lying at a distance $\leq 2$ from $[ - 1 , 1 ]$ , and suppose $f$ is analytic in a larger region $\Omega$ that includes a contour $\Gamma$ enclosing $S$ . We can sketch the situation like this:

$$
\begin{array} { l } { { { \bf x } = { \bf c h e b f u n } ( { \bf \Phi } ^ { \prime } { \bf x } ^ { \prime } ) ; ~ { \bf p l o t } ( { \bf r e a l } ( { \bf x } ) , \mathrm { i m a g ( { \bf x } ) } , { \bf \Phi } ^ { \prime } { \bf r } ^ { \prime } ) } } \\ { { \bf s e m i } = 2 * \exp ( 0 . 5 \mathrm { i } * { \bf p i } * { \bf x } ) ; ~ { \bf S } = { \bf \Phi } [ { \bf x } - 2 \mathrm { i } ; ~ 1 + \mathrm { s e m i } ; ~ 2 \mathrm { i } - { \bf x } ; ~ - 1 - \mathrm { s e m i } ] ; }  \\ { { \bf h o l d ~ o n } , ~ { \bf p l o t } ( { \bf S } , { \bf \Phi } ^ { \prime } { \bf k } ^ { \prime } ) , ~ { \bf z } = { \bf e x p } ( 1 \mathrm { i } * { \bf p i } * { \bf x } ) ; } \\ { { \bf G a m m a } = ( 2 . 8 + . 2 \mathrm { i } ) * ( { \bf s i n h } ( { \bf z } ) + . 5 * { \bf r e a l } ( { \bf z } ) ) ; ~ { \bf p l o t } ( \mathrm { G a m m a } , { \bf \Phi } ^ { \prime } { \bf b } ^ { \prime } ) }  \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/090cff5c4738302a6fcbdad53de7cd8f1a2262647cb46fe39db17c40c333d410.jpg)

Under these assumptions, there is a constant $\gamma > 1$ such that for every $t \in \Gamma$ and every $x _ { j }$ , $| t - x _ { j } | \geq \gamma | x - x _ { j } |$ . This implies

$$
| \ell ( x ) / \ell ( t ) | \leq \gamma ^ { - n - 1 } ,
$$

and thus by (11.9),

$$
\| f - p \| = O ( \gamma ^ { - n } ) .
$$

Note that this conclusion applies regardless of the distribution of the interpolation points in $[ - 1 , 1 ]$ . They could be equally spaced or random, for example. (At least that is true in theory. In practice, such choices would be undone by rounding errors on a computer, as we shall see in Chapter 13.)

So convergence of polynomial interpolants to analytic functions on $[ - 1 , 1 ]$ is all about how small $\ell ( x )$ is on $[ - 1 , 1 ]$ , compared with how big it is on a contour $\Gamma$ inside which $f$ is analytic. From this point of view we can begin to see why Chebyshev points are so good: because a polynomial with roots at the Chebyshev points has approximately uniform magnitude on $[ - 1 , 1 ]$ . Suppose, for example, we consider the polynomial $\ell \in \mathcal { P } _ { 8 }$ with roots at 8 Chebyshev points. On $[ - 1 , 1 ]$ it has size $O ( 2 ^ { - 8 } )$ , roughly speaking, but it grows rapidly for $x$ outside this interval. Here is a plot for $x \in [ - 1 . 5 , 1 . 5 ]$ :

$\tt { n p } = 8$ ; xj = chebpts(np); d = domain([-1.5,1.5]); ell = poly(xj,d); plot(ell) hold on, plot(xj,ell(xj),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/afe169c097c908d62ba4b88cfbff7e960b0d4a932919f120384b9d8e1fa1f44c.jpg)

With the MATLAB contour command we can examine the size of $\ell ( x )$ for complex values of $x$ . The following code plots contours at $| \ell ( x ) | = 2 ^ { - 6 } , 2 ^ { - 5 } , \ldots , 1$ .

$\mathtt { p l o t } ( \mathtt { x j } , \mathtt { e l l } ( \mathtt { x j } ) , \mathtt { \xi ^ { \prime } . k ^ { \prime } } )$ , hold on xgrid $= - 1 . 5 \colon . 0 2 \colon 1 . 5$ ; ygrid $=$ -0.9:.02:0.9; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $= \ 2 . \widehat { \ } ( - 6 : 0 )$ ; contour(xx,yy,abs(ellzz),levels,'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c40f562791a686ecdce074397048601bf36943b6a91d23b2f186af2ac7560a97.jpg)

We can see a great deal in this figure. On $[ - 1 , 1 ]$ , it confirms that $\ell ( x )$ is small, with maximum value $| \ell ( x ) | = 2 ^ { - 6 }$ at $x = 0$ . Away from $[ - 1 , 1 ]$ , $| \ell ( x ) |$ grows rapidly and takes constant values on curves that look close to ellipses. For $t$ on the outermost of the curves plotted, the ratio $| \ell ( x ) / \ell ( t ) |$ will be bounded by $2 ^ { - 6 }$ for any $x \in [ - 1 , 1 ]$ .

Let us compare this to the very different behavior if we take points that are not close to the Chebyshev distribution. To make a specific and quite arbitrary choice, let us again take 8 points, four of them at $^ { - 1 }$ and four at 1. Here is the plot on the real axis.

xj = [-1 -1 -1 -1 1 1 1 1]; ell $=$ poly(xj,d); plot(ell), hold on, plot(xj,ell(xj),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/735248b016b94bc01c6ecb06875918eb06e82c81ea69dfd0573119617f4f1c3d.jpg)

And here are the contours in the complex plane.

plot(xj,ell(xj),'.k'), hold on, ellzz $=$ ell(zz); contour(xgrid,ygrid,abs(ellzz),levels, $" \Bbbk ^ { \prime }$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/9fc45111788ab22960429d13c7ae118b2fd5143e928513ab505ef2fc73aaee02.jpg)

These figures show that the size of $\ell ( x )$ on $[ - 1 , 1 ]$ is not at all uniform: it is far smaller than $2 ^ { - 6 }$ for $x \approx \pm 1$ , but as big as $1$ at $x = 0$ . Now, for $x \in [ - 1 , 1 ]$ and $t$ on the outermost curve shown, the maximum of the ratio $| \ell ( x ) / \ell ( t ) |$ is no better than 1 since that curve touches $[ - 1 , 1 ]$ . If we wanted to achieve $| \ell ( x ) / \ell ( t ) | \leq 2 ^ { - 6 }$ as in the last example, $\Gamma$ would have to be a much bigger curve—closer to the “stadium”:

xgrid = -2:.04:2; ygrid = -1.5:.04:1.5; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathsf { z } \mathsf { z } = \mathsf { x } \mathbf { x } \mathsf { + } 1 \mathrm { i } \ast \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $=$ $[ 2 \hat { \bf \Phi } 6 , 2 \hat { \bf \Phi } 6 ]$ ; hold on, contour(xgrid,ygrid,abs(ellzz),levels,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4e87f3763916a780709955cb00df5e640ab61cfe74abb1ec7b01d0710b1cc9a5.jpg)

The function $f$ would have to be analytic within this much larger region for the bound (11.9) to apply with a ratio $| \ell ( x ) / \ell ( t ) |$ as favorable as $2 ^ { - 6 }$ .

Summary of Chapter 11. The error of a polynomial interpolant can be represented by a contour integral in the complex plane, the Hermite integral formula. This provides the standard method for showing geometric convergence for certain approximations of analytic functions.

Exercise 11.1. Chebfun computation of Cauchy integrals. (a) Figure out (on paper) the polynomial $p \in \mathcal { P } _ { 2 }$ that takes the values $p ( - 1 ) = 1$ , $p ( 1 / 2 ) = 2$ , and $p ( 1 ) = 2$ . What is $p ( 2 )$ ? (b) Read about the numerical computation of Cauchy integrals in Chapter 5 of the online Chebfun Guide. Write a program to confirm Theorem 11.1 by computing $p ( 2 )$ numerically by a Cauchy integral for the function $f ( x ) = ( x + 1 ) ( x - 0 . 5 ) ( x - 1 ) e ^ { x } + 1 1 / 6 +$ $x / 2 - x ^ { 2 } / 3$ . Take both $| x | = 3 / 2$ and $| x | = 3$ as contours to confirm that it does not matter whether or not $\Gamma$ encloses $_ x$ . (c) Write an anonymous function $\mathfrak { p } \ : = \ : \mathfrak { Q } ( \mathbf { x } ) . . .$ to apply the above calculation not just for $x = 2$ but for arbitrary $_ x$ , and construct a chebfun on $[ - 1 , 1 ]$ from this anonymous function. Do its coefficients as reported by poly match your expectations?

Exercise 11.2. Confluent interpolation points. Modify the above problem to require $p ( - 1 ) = 1$ , $p ( 1 ) = 2$ , and $p ^ { \prime } ( 1 ) = 0$ . This is a Hermite interpolation problem, in which some interpolation points are specified multiply with corresponding values specified for derivatives. What is the analytic solution to this interpolation problem? Do the computations involving contour integrals and anonymous functions deliver the right result?

Exercise 11.3. Interpolation in a disk. Suppose a function $f$ is interpolated by polynomials in arbitrary points of the disk $| x | \leq r ^ { \prime }$ and we measure the accuracy $f ( x ) { - } p ( x )$ for $_ x$ in the disk $| x | \leq r$ . Show that geometric convergence is ensured (in exact arithmetic, ignoring rounding errors) if $f$ is analytic in the disk $| x | \le r + 2 r ^ { \prime }$ . Give the constant $\rho$ for convergence at the rate $O ( \rho ^ { - n } )$ . (This result originates with [M´eray 1884].)

Exercise 11.4. Working around a simple pole. Let $f$ be analytic on the closed Bernstein ellipse region $\overline { { E } } _ { \rho }$ for some $\rho > 1$ . It can be shown that $| \ell ( x ) / \ell ( t ) | = O ( \rho ^ { - n } )$ uniformly as $n \to \infty$ for $x \in [ - 1 , 1 ]$ and $t$ on the ellipse, and thus Theorem 11.1 can be used to show that $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as asserted by Theorem 8.2. Now suppose that $f$ has a finite number of singularities on the ellipse but these are just simple poles. Explain how the contour integral argument can be modified to show that the rate of convergence will still be $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as was established by another method in Exercise 8.15.
