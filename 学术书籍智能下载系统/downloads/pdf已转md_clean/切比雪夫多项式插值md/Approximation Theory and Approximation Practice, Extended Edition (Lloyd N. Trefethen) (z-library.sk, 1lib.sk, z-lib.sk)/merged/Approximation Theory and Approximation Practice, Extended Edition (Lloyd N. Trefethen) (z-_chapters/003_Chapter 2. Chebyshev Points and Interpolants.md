# Chapter 2. Chebyshev Points and Interpolants

Any interval $[ a , b ]$ can be scaled to $[ - 1 , 1 ]$ , so most of the time, we shall just talk about $[ - 1 , 1 ]$ .

Let $n$ be a positive integer:

Consider $n + 1$ equally spaced angles $\{ \theta _ { j } \}$ from $0$ to $\pi$ :

tt = linspace(0,pi,n+1);

We can think of these as the arguments of $n + 1$ points $\{ z _ { j } \}$ on the upper half of the unit circle in the complex plane. These are the $( 2 n ) \mathrm { t h }$ roots of unity lying in the closed upper half-plane:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/a4907fa20ca2c90fb551bb4661e603bf39b0e9c031af17981b2d92ce0445c966.jpg)

The Chebyshev points associated with the parameter $n$ are the real parts of these points,

$$
x _ { j } = \operatorname { R e } z _ { j } = { \frac { 1 } { 2 } } ( z _ { j } + z _ { j } ^ { - 1 } ) , \quad 0 \leq j \leq n ,
$$

xx = real(zz);

Some authors use the terms Chebyshev–Lobatto points, Chebyshev extreme points, or Chebyshev points of the second kind, but as these are the points most often used in practical computation, we shall just say Chebyshev points.

Another way to define the Chebyshev points is in terms of the original angles,

$$
x _ { j } = \cos ( j \pi / n ) , \quad 0 \leq j \leq n ,
$$

xx = cos(tt);

and the problem of polynomial interpolation in these points was considered at least as early as [Jackson 1913]. There is also an equivalent Chebfun command chebpts:

xx = chebpts(n+1);

Actually, this result isn’t exactly equivalent, as the ordering is left-to-right rather than right-to-left. Concerning rounding errors when these numbers are calculated numerically, see Exercise 2.3.

Let us add the Chebyshev points to the plot:

hold on, for ${ \mathfrak { j } } ~ = ~ 2 { : } \mathtt { n }$ , plot( $\left[ \mathbf { x x } \left( \mathbf { n } + 2 - j \right. \right]$ ) zz(j)],'k'), endplot(xx,0\*xx,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/089a3422b2298919e2a08410d5fb117384299dae94c663faf66b12d4af6c0320.jpg)

They cluster near $^ { 1 }$ and $^ { - 1 }$ , with the average spacing as $n \to \infty$ being given by a density function with square root singularities at both ends (Exercise 2.2).

Let $\{ f _ { j } \}$ , $0 \leq j \leq n$ , be a set of numbers, which may or may not come from sampling a function $f ( x )$ at the Chebyshev points. Then there exists a unique polynomial $p$ of degree $n$ that interpolates these data, i.e., $p ( x _ { j } ) = f _ { j }$ for each $j$ . When we say “of degree $n$ ,” we mean of degree less than or equal to $n$ , and we let $\mathcal { P } _ { n }$ denote the set of all such polynomials:

$$
{ \mathcal { P } } _ { n } = \{ { \mathrm { p o l y n o m i a l s ~ o f ~ d e g r e e ~ a t ~ m o s t ~ } } n \} .
$$

As we trust the reader already knows, the existence and uniqueness of polynomial interpolants apply for any distinct set of interpolation points. In the case of Chebyshev points, we call the polynomial the Chebyshev interpolant.

Polynomial interpolants through equally spaced points have terrible properties, as we shall see in Chapters 11–15. Polynomial interpolants through Chebyshev points, however, are excellent. It is the clustering near the ends of the interval that makes the difference, and other sets of points with similar clustering, like Legendre points (Chapter 17), have similarly good behavior. The explanation of this fact has a lot to do with potential theory, a subject we shall introduce in Chapter 12. Specifically, what makes Chebyshev or Legendre points effective is that each one has approximately the same average distance from the others, as measured in the sense of the geometric mean. On the interval $[ - 1 , 1 ]$ , this average distance is about $1 / 2$ (Exercise 2.6).

Chebfun is built on Chebyshev interpolants [Battles $\&$ Trefethen 2004]. For example, here is a certain step function:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/da9403ad7939323187e0f7e46c26b3b43ca380954178231da4330fd326ed12e2.jpg)

By calling chebfun with a second explicit argument of 6, we can construct the Chebyshev interpolant to $f$ through 6 points, that is, of degree 5:

$_ { \mathrm { ~ p ~ } } =$ chebfun(f,6); hold on, plot(p,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/306ce5cebfd233191ff303f096d666529c76fef06adfceafdcfdd1e946014890.jpg)

Similarly, here is the Chebyshev interpolant of degree 25:

plot(f,'k'), p = chebfun(f,26); hold on, plot(p,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/1f6a7ddf24f12aa216eb5805c2fdf961a36cccf4160adfafb15b347982c2748a.jpg)

Here are a more complicated function and its interpolant of degree 100:

f = sin( $6 * \mathbf { x } .$ ) $^ +$ sign(sin(x+exp(2\*x))); plot(f,'k'), $_ { \mathrm { ~ p ~ } } =$ chebfun(f,101); hold on, plot(p)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/988a66496449bbfc0ad7d7054054c3e5f991576cf4ff4fe747cd807963b78830.jpg)

Another way to use the chebfun command is by giving it an explicit vector of data rather than a function to sample, in which case it interprets the vector as data for a Chebyshev interpolant of the appropriate order. Here, for example, is the interpolant of degree 99 through random data values at 100 Chebyshev points in $[ - 1 , 1 ]$ :

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/ed9a30cce97abab6bb5c7f3e8ca10ac81f79e8aa8d7756b71c6d25fedbc5a71d.jpg)

This experiment illustrates how robust Chebyshev interpolation is. If we had taken a million points instead of 100, the result would not have been much different mathematically, though it would have been harder to plot. We shall return to this figure in Chapter 15.

For illustrations like these it is interesting to pick data with jumps or wiggles, and Chapter 9 discusses such interpolants systematically. In applications where polynomial interpolants are most useful, however, the data will typically be smooth.

Summary of Chapter 2. Polynomial interpolants in equispaced points in $[ - 1 , 1 ]$ have very poor approximation properties, but interpolants in Chebyshev points, which cluster near $\pm 1$ , are excellent.

Exercise 2.1. Chebyshev interpolants through random data. (a) Repeat the experiment of interpolation through random data for 10, 100, 1000, and 10000 points. In each case use minandmax(p) to determine the minimum and maximum values of the interpolant and measure the computer time required for this computation (e.g., using tic and toc). (b) In addition to the four plots over $[ - 1 , 1 ]$ , use xlim([0.9999 1]) to zoom in the 10000-point plot to the interval [0.9999, 1]. How many of the 10000 grid points fall in this interval?

Exercise 2.2. Limiting density as $n \to \infty$ . (a) Suppose $x _ { 0 } , \ldots , x _ { n }$ are $n + 1$ points equally spaced from $^ { - 1 }$ to 1. If $- 1 \leq a < b \leq 1$ , what fraction of the points fall in the interval $[ a , b ]$ in the limit $n \to \infty$ ? Give an exact formula. (b) Give the analogous formula for the case where $x _ { 0 } , \ldots , x _ { n }$ are the Chebyshev points. (c) How does the result of (b) match the number found in [0.9999, 1] in the last exercise for the case $n = 9 9 9 9 9$ ? (d) Show that in the limit $n \to \infty$ , the density of the Chebyshev points near $x \in ( - 1 , 1 )$ approaches $n / ( \pi \sqrt { 1 - x ^ { 2 } } )$ (see (12.10)).

Exercise 2.3. Rounding errors in computing Chebyshev points. On a computer in floating point arithmetic, the formula (2.2) for the Chebyshev points is not so good, because it lacks the expected symmetry. (a) Write a MATLAB program that finds the smallest even value $n \geq 2$ for which, on your computer as computed by this formula, $x _ { n / 2 } \neq 0$ . (You will probably find that $n = 2$ is the first such value.) (b) Find the line in the code chebpts.m where Chebfun computes Chebyshev points. What alternative formula does it use? Explain why this formula achieves perfect symmetry for all $n$ in floating point arithmetic. (c) Show that this formula is mathematically equivalent to (2.2).

Exercise 2.4. Chebyshev points of the first kind. The Chebyshev points of the first kind, also known as Gauss–Chebyshev points, are obtained by taking the real parts of points on the unit circle midway between those we have considered, i.e., $x _ { j } = \cos ( ( j + \textstyle \frac { 1 } { 2 } ) \pi / ( n + 1 ) )$ for integers $0 \leq j \leq n$ . Call help chebpts and help legpts to find out how to generate these points in Chebfun and how to generate Legendre points for comparison (these are roots of Legendre polynomials—see Chapter 17). For $n + 1 = 1 0 0$ , what is the maximum difference between a Chebyshev point of the first kind and the corresponding Legendre point? Draw a plot to illustrate as informatively as you can how close these two sets of points are.

Exercise 2.5. Convergence of Chebyshev interpolants. (a) Use Chebfun to produce a plot on a log scale of $\| f - p _ { n } \|$ as a function of $n$ for $f ( x ) = e ^ { x }$ on $[ - 1 , 1 ]$ , where $p _ { n }$ is the Chebyshev interpolant in $\mathcal { P } _ { n }$ . Take $\| \cdot \|$ to be the supremum norm, which can be computed by $\mathtt { n o r m } ( \mathtt { f } \mathtt { - p } , \mathtt { i n f } )$ . How large must $n$ be for accuracy at the level of machine precision? What happens if $n$ is increased beyond this point? (b) The same questions for $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ . Convergence rates like these will be analyzed in Chapters 7 and 8.

Exercise 2.6. Geometric mean distance between points. Write a code meandistance that takes as input a vector of points $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ and produces a plot with $x _ { j }$ on the horizontal axis and the geometric mean of the distances of $x _ { j }$ to the other points on the vertical axis. (The MATLAB command prod may be useful.) (a)

What are the results for Chebyshev points with $n = 5 , 1 0 , 2 0 !$ (b) The same for Legendre points (see Exercise 2.4). (c) The same for equally spaced points from $x _ { 0 } = - 1$ to $x _ { n } = 1$ . Exercise 2.7. Chebyshev points scaled to the interval $[ a , b ]$ . (a) Use chebpts(10) to print the values of the Chebyshev points in $[ - 1 , 1 ]$ for $n = 9$ . (b) Use chebfun(@sin,10) to compute the degree 9 interpolant $p ( x )$ to $\sin ( x )$ in these points. Make a plot showing $p ( x )$ and $\sin ( x )$ over the larger interval $[ - 6 , 6 ]$ , and also a semilog plot of $| f ( x ) - p ( x ) |$ over that interval. Comment on the results. (c) Now use chebpts(10,[0 6]) to print the values of the Chebyshev points for $n = 9$ scaled to the interval [0, 6]. (d) Use chebfun(@sin, [0 6],10) to compute the degree 9 interpolant to $\sin ( x )$ in these points, and make the same two plots as before over $[ - 6 , 6 ]$ . Comment.
