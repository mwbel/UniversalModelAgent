# Chapter 9. Gibbs Phenomenon

Polynomial interpolants and projections oscillate and overshoot near discontinuities. We have observed this Gibbs phenomenon already in Chapter 2, and now we shall look at it more carefully. We shall see that the Gibbs effect for interpolants can be regarded as a consequence of the oscillating inverse-linear tails of Lagrange polynomials, i.e., interpolants of Kronecker delta functions. Chapter 15 will show that these same tails, combined together in a different manner, are also the origin of Lebesgue constants of size $O ( \log n )$ , with implications throughout approximation theory.

To start, consider $\mathtt { s i g n } ( \mathtt { x } )$ , interpolated in $n + 1 = 1 0$ and 20 Chebyshev points. We take $n$ odd to avoid a grid point at the middle of the step.

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun $( \mathbf { \partial } ^ { \prime } \mathbf { x } ^ { \prime } )$ ; f = sign(x); subplot(1,2,1) plot(f,'k') hold on $\mathtt { f 9 } =$ chebfun(f,10); plot(f9,'.-') subplot(1,2,2) plot(f,'k'), hold on, $\yen 19 ~ =$ chebfun(f,20); plot(f19,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/a41920a9115a68882886a5a5d6c6cfb20cacf995fedafa34b1e1d789705c5eb3.jpg)

Both of these figures show a substantial overshoot near the jump. As $n$ increases from 9 to 19, the overshoot gets narrower, but not shorter, and it will not go away as $n \to \infty$ . Let us zoom in and look at the plot on subintervals:

subplot(1,2,1), plot(f,'k'), hold on plot(f9,'.-','interval',[0 0.8]) subplot(1,2,2), plot(f,'k'), hold on plot(f19,'.-','interval',[0 0.4])

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3e74bbafa1851a7007123be0b0d13fe831ca66da32948f2d4bf759b0904bc286.jpg)

We now zoom in further with analogous plots for $n = 9 9$ and 999.

subplot(1,2,1), plot(f, $^ { 1 } \mathtt { k } ^ { \prime } )$ , hold on   
$\mathtt { f 9 9 } =$ chebfun(f,100); plot(f99,'.-','interval',[0 0.08])   
subplot(1,2,2), plot(f,'k'), hold on   
$\mathbf { f } 9 9 9 ~ =$ chebfun(f,1000); plot(f999,'.-','interval',[0 0.008])

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c1e5465a9e980e49e1325bfe0cab6fbb30233e4b9d5ceaa568f8e81052b9882c.jpg)

Notice that in these figures, the vertical scale is always fixed while the horizontal scale is adjusted proportionally, confirming that the Gibbs overshoot gets narrower but approaches a constant height in the limit $n \to \infty$ .

What is this height? We can measure it numerically with the max command:

for $\mathtt { n } ~ = ~ 2 . \hat { \ } ( 1 : 8 ) - 1$ gibbs $=$ max(chebfun(f,n+1)); fprintf('%7d %17.8f\n', n, gibbs)   
end

<table><tr><td>n</td><td>Gibbs amplitude</td></tr><tr><td>1</td><td>1.00000000</td></tr><tr><td>3</td><td>1.18807518</td></tr><tr><td>7</td><td>1.26355125</td></tr><tr><td>15</td><td>1.27816423</td></tr><tr><td>31</td><td>1.28131717</td></tr><tr><td>63</td><td>1.28204939</td></tr><tr><td>127</td><td>1.28222585</td></tr><tr><td>255</td><td>1.28226917</td></tr></table>

Clearly as $n \to \infty$ , the maximum of the Chebyshev interpolant to the sign function converges to a number bigger than 1. The total variation of the interpolant, meanwhile, diverges slowly to $\infty$ , at a rate proportional to $\log n$ , and this is the effect we shall examine further in Chapter 15.

for n = 2.^(1:8)-1 tv $=$ norm(diff(chebfun(f,n+1)),1); fprintf('%7d %14.2f\n', n, tv)   
end

<table><tr><td>n</td><td>variation</td></tr><tr><td>1</td><td>2.00</td></tr><tr><td>3</td><td>2.75</td></tr><tr><td>7</td><td>3.64</td></tr><tr><td>15</td><td>4.56</td></tr><tr><td>31</td><td>5.47</td></tr><tr><td>63</td><td>6.37</td></tr><tr><td>127</td><td>7.26</td></tr><tr><td>255</td><td>8.15</td></tr></table>

The following theorem summarizes the Gibbs phenomenon for Chebyshev interpolants. Well, perhaps it is a little bold to call it a “theorem,” since it is not clear that a proof has ever been written down. The formulas necessary to represent the interpolant (in the equivalent trigonometric case—see Exercise 9.4) can be found in various forms in [Runck 1962] and in [Helmberg & Wagner 1997], which relates the interpolating polynomial to the beta function and reports the numbers 1.282 and 1.066 to 3 digits of accuracy. The more precise results presented here have been privately communicated to me by Wagner based on calculations to more than 500 digits.

Theorem 9.1. Gibbs phenomenon for Chebyshev interpolants. Let $p _ { n }$ be the degree $n$ Chebyshev interpolant of the function $f ( x ) = \mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ . Then as $n \to \infty$ ,

$$
\operatorname* { l i m } _ { n \to \infty , n o d d } \| p _ { n } \| = c _ { 1 } = 1 . 2 8 2 2 8 3 4 5 5 7 7 5 4 2 8 5 4 8 1 3 \dots ,
$$

$$
\operatorname* { l i m } _ { n \to \infty , n e v e n } \| p _ { n } \| = c _ { 2 } = 1 . 0 6 5 7 8 3 8 8 8 2 6 6 4 4 8 0 9 9 0 5 \dots .
$$

(The case of n even differs in having a grid point at the middle of the jump.)

Although we are not going to prove Theorem 9.1, we do want to indicate where the fixed-overshoot effect comes from. Everything falls into place when we consider the Lagrange polynomials introduced in Chapter 5. Recall from (5.2) that the $j$ th Lagrange polynomial $\ell _ { j } ( x )$ for the $( n + 1 )$ -point Chebyshev grid is the unique polynomial in $\mathcal { P } _ { n }$ that takes the values $1$ at $x _ { j }$ and $0$ at the other grid points $x _ { k }$ . On the 20-point grid, i.e., $n = 1 9$ , here are the Lagrange polynomials $\ell _ { 1 0 }$ and $\ell _ { 1 1 }$ with a dashed line marked at $x = - 0 . 1 5$ , which we will take as our point of special interest:

yl = [-0.3 1.3]; xc = -0.15\*[1 1];   
$\mathtt { p 1 0 ~ = ~ }$ chebfun([zeros(1,10) 1 zeros(1,9)]);   
${ \tt p } 1 1 \ =$ chebfun([zeros(1,11) 1 zeros(1,8)]);   
subplot(1,2,1), plot(p10,'.-'), hold on, plot(xc,yl,'--r') subplot(1,2,2), plot(p11,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/7c8788999043c554c7c2767b5dbad514d61ff969c97559c83ba6dcf5ea12398b.jpg)

Here are $\ell _ { 1 2 }$ and $\ell _ { 1 3 }$ :

$\mathtt { p } 1 2 \ =$ chebfun([zeros(1,12) 1 zeros(1,7)]);   
$\mathtt { p 1 3 } =$ chebfun([zeros(1,13) 1 zeros(1,6)]);   
subplot(1,2,1), plot(p12,'.-'), hold on, plot(xc,yl,'--r') subplot(1,2,2), plot(p13,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/22a86db9515be1639567a9ad59e767e6c78a64bbab701f6b15ab4579d3ad838c.jpg)

Following (5.1), we note that by taking the sum of a sequence of such Lagrange functions, we get the interpolant to the function that jumps from 0 for $x < 0$ to $^ { 1 }$ for $x > 0$ . Here is the sum of the four just plotted, which is beginning to look like a square wave:

plot(p10+p11+p12+p13,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d20ed3ca107e1bcd81584662cbad935f8a0fe28d570f54fafd59402a32e277c1.jpg)

If we went all the way to the last grid point we would get the interpolant

$$
p ( x ) = \sum _ { j = ( n + 1 ) / 2 } ^ { n } \ell _ { j } ( x ) .
$$

Note that for any fixed $x < x _ { ( n - 1 ) / 2 }$ , this is an alternating series of small terms whose amplitudes decrease inverse-linearly to zero. The finite but nonzero sum of such a series in the limit $n  \infty$ is what gives rise to the fixed-overshoot Gibbs effect in polynomial interpolation.

In particular, suppose we focus on the dashed line at $x = - 0 . 1 5$ in the figures. Notice the alternating signs of the values of $\ell _ { 1 0 } , \ell _ { 1 1 } , \ell _ { 1 2 } , \ell _ { 1 3 }$ at this value of $x$ . In the figure for $\ell _ { 1 0 } + \ell _ { 1 1 } + \ell _ { 1 2 } + \ell _ { 1 3 }$ we accordingly see the Gibbs overshoot beginning to converge to its asymptotic amplitude $\approx 0 . 1 4 1$ . This number is half of the value 0.282 . . . of Theorem 9.1, since the jump for this function is of amplitude 1 instead of 2.

In Chapter 15 we shall consider the same alternating series but with signs multiplied by $( - 1 ) ^ { j }$ . This eliminates the alternation, so that we have approximately a harmonic series of inverse-linear terms. The partial sums of such a series grow at a logarithmic rate, as we saw above in the calculation of the variation.

Our discussion so far has concerned interpolants, but there is a parallel theory of the Gibbs phenomenon for projections—in the notation of this book, polynomials $f _ { n }$ rather than $p _ { n }$ . (The required Chebyshev coefficients are defined by the same integral (3.12) of Theorem 3.1, even though we are now dealing with functions $f$ that are not Lipschitz continuous as in the assumption stated for that theorem.) As always, though the interpolants are closer to practical computation, the projections may appear to be more fundamental mathematically. Historically speaking, it was the case of Fourier (trigonometric) projection that was analyzed first. The original discoverer was not Gibbs but Henry Wilbraham, a 22-year-old fellow of Trinity College, Cambridge, in 1848, who unfortunately made the mistake of publishing his fine paper in the short-lived Cambridge and Dublin Journal of Mathematics [Wilbraham 1848]. Fourier series for certain functions with jumps were already long known in Wilbraham’s day—in fact they go back to Euler, half a century before Fourier. The particular series studied by Wilbraham, originally due to Euler in 1772, is

$$
\cos ( t ) - { \frac { 1 } { 3 } } \cos ( 3 t ) + { \frac { 1 } { 5 } } \cos ( 5 t ) - \cdot \cdot \cdot ,
$$

which approximates a square wave of height $\pm \pi / 4$ (compare Exercise 3.6(a)):

t = chebfun('t',[-6,6]); f = (pi/4)\*sign(cos(t)); plot(f,'k') f9 $=$ cos(t) - cos(3\*t)/3 + cos(5\*t)/5 - cos(7\*t)/7 $^ +$ cos(9\*t)/9; hold on, plot(f9)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d47b726b556cb9c50e111d3ad41a9e075aa075ca74734581f44e4d52c496431a.jpg)

Wilbraham worked out the magnitude of the overshoot, and thus the following analogue of Theorem 9.1 is due to him.

Theorem 9.2. Gibbs phenomenon for Chebyshev projections. Let $f _ { n }$ be the degree $n$ Chebyshev projection of the sign function $f ( x ) = \mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ . Then as $n \to \infty$ ,

$$
\operatorname* { l i m } _ { n \to \infty } \| f _ { n } \| = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } { \frac { \sin { x } } { x } } d x = 1 . 1 7 8 9 7 9 7 4 4 4 7 2 1 6 7 \ldots .
$$

(The function $\begin{array} { r } { \mathrm { S i } ( x ) = \int _ { 0 } ^ { x } t ^ { - 1 } \sin { t } d t } \end{array}$ is known as the sine integral; see Exercise 9.6.) To see this number experimentally we can use the 'trunc' option in the Chebfun constructor. The overshoots look similar to what we saw before, but with smaller amplitude.

f = sign(x); subplot(1,2,1), plot(f,'k'), hold on $\begin{array} { r l } { \mathbf { f } 9 } & { { } = } \end{array}$ chebfun(f,'trunc',10); plot(f9,'-') subplot(1,2,2), plot(f,'k'), hold on $\yen 19 ~ =$ chebfun(f,'trunc',20); plot(f19,'-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/05db5756b4d57edfa7e5fe80873c79ffbffb6c7ba97a600becc9070fe0747966.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/34f5a32f7a0ced3afff4edf602eebbd45a8d3b210eeb4a1286dc8a8a64eaab85.jpg)

The numbers behave as predicted:

for np = 2.^(4:7) g = chebfun(f,'trunc',np);

fprintf('%7d %17.8f\n', np, max(g{0,5/np})) end limit $=$ (2/pi)\*sum(chebfun('sin(x)/x',[0 pi]))

n Gibbs amplitude 16 1.18028413 32 1.17930541 64 1.17906113 128 1.17900009 limit = 1.178979744472167

In all the experiments of this chapter we have worked with polynomials rather than trigonometric series, but the effects are the same (Exercise 9.4).

It is worth commenting on a particular property of series such as (9.3) that we have taken for granted throughout this discussion: even though each partial sum is continuous, a series may converge pointwise to a discontinuous limit, everywhere except at the points of discontinuity themselves. This kind of behavior seems familiar enough nowadays, but in the century beginning with Fourier’s work in 1807, it often seemed paradoxical and confusing to mathematicians. The same pointwise convergence to discontinuous functions can also occur with interpolants, as in Theorem 9.1.

In this chapter we have focused on the height of the overshoot of a Gibbs oscillation, because this is the effect so readily seen in plots. Perhaps the most important property of Gibbs oscillations for practical applications, however, is not their height but their slow decay as one moves away from the point of discontinuity. If $f$ has a jump, the oscillations at a distance $k$ grid points away must be expected to be of size $O ( k ^ { - 1 } )$ ; if $f ^ { \prime }$ has a jump, we expect oscillations of size $O ( k ^ { - 2 } )$ , and so on. (See Exercise 9.8. Exercise 26.5 will look at the analogous exponents for interpolation by rational functions rather than polynomials.) This algebraic rate of decay of information in polynomial interpolants can be contrasted with the exponential decay that one gets with spline approximations, which is the key advantage of splines for certain applications. Chebfun responds to this problem by representing functions with discontinuities by piecewise polynomials rather than global ones, with breakpoints at the discontinuities. For example, the location of the discontinuity in the function $\exp ( | x - 0 . 1 | )$ will be determined automatically in response to the command

The result is a chebfun consisting of two pieces each of degree 3, and the break in the middle appears at the right place:

f.ends(2)

# ans $=$ 0.100000000000000

Let us return to 22-year-old Mr. Wilbraham. Unfortunately, his published paper had little impact, and the effect was rediscovered and discussed in the pages of Nature during 1898–1899 by James Michelson, A. E. H. Love, and J. Willard

Gibbs. These authors got more attention for a number of reasons. First, they were leading scientists. Second, their problem arose at a time when applied mathematics had advanced much further and in a practical application, a mechanical graphing machine called a “harmonic analyzer” used by Michelson and Stratton. Third, they published their observations in a major journal. Fourth, they failed to get it right at first, so several publications appeared in succession! Other mathematicians got involved too, notably Poincar´e. Finally, they were lucky enough to have “Gibbs’s phenomenon” named and highlighted a few years later in a major research article on Fourier analysis by the mathematician Maxime Bˆocher [1906]. For a fascinating discussion of the history of the Gibbs phenomenon (for projection, not interpolation), which they more properly call the Gibbs–Wilbraham phenomenon, see [Hewitt & Hewitt 1979].

Summary of Chapter 9. Chebyshev projections and interpolants, as well as other polynomial and trigonometric approximations, tend to oscillate near discontinuities. The oscillations decay algebraically, not exponentially, with distance from the discontinuity.

Exercise 9.1. Calculations for larger $\textbf { \em n }$ . We measured the height of the Gibbs overshoot for a step function for $n = 1 , 3 , 7 , \dotsc , 2 5 5$ . Larger values of $n$ get a bit slow, but knowing that the maximum occurs around $x = 3 / n$ , compute these numbers up to $n = 4 0 9 5$ using a command of the form $\mathtt { m a x } ( \mathtt { g } \{ 0 , 5 / \mathtt { n } \} )$ . How great a speedup does this trick produce?

Exercise 9.2. A function with many jumps. Use Chebfun to produce a plot of the degree 200 Chebyshev interpolant to the function round $\mathbf { \tilde { e } } \mathbf { x p } ( \mathbf { s i n } ( 2 \ast \mathbf { p i } \ast \mathbf { x } ) ) )$ on $[ - 1 , 1 ]$ .

Exercise 9.3. Lagrange polynomials. Take $n \geq 2$ to be even and let $p$ be the degree $_ n$ Chebyshev interpolant to the Kronecker delta function at $x = x _ { n / 2 } = 0$ . (a) Use the barycentric formula of Theorem 5.2 to obtain a simple formula for $p$ . (b) Derive a formula for the values of $p$ at the “Chebyshev midpoints” defined by the usual formula $x _ { j } = \cos ( j \pi / n )$ of Chapter 2 except with half-integer values of $j$ . (c) For $n = 1 0 0$ , use Chebfun to produce an elegant plot showing the inverse-linear amplitudes of these values. (You can get the Chebyshev midpoints from chebpts $( \mathtt { n } , 1 )$ or from $\mathbf { x } =$ chebpts $^ { 2 * \mathtt { n } + 1 }$ ), $\mathtt { x } { = } \mathtt { x } ( 2 { : } 2 { : } \mathtt { e n d } )$ .)

Exercise 9.4. Fourier and Chebyshev Gibbs phenomena. We have repeatedly made the connection between Chebyshev polynomials $T _ { n } ( x )$ on the unit interval, Laurent polynomials $( z ^ { n } + z ^ { - n } ) / 2$ on the unit circle, and trigonometric polynomials $\cos ( n \theta )$ on $[ - \pi , \pi ]$ . Use these connections to show that the Gibbs overshoot in Chebyshev interpolation of $\mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ , with $n$ even, is identical to the overshoot for a certain problem of trigonometric interpolation in $\theta$ .

Exercise 9.5. Local minima of a truncated sine series. (a) Plot $\phi _ { n }$ with $n = 1 0 , 1 0 0$ , and 1000 for a sum going back to Euler in 1755,

$$
\phi _ { n } ( x ) = \sum _ { k = 1 } ^ { n } { \frac { \sin ( k x ) } { k } } .
$$

What function does the sum evidently converge to? Is the Gibbs overshoot of the same relative magnitude as for (9.3)? (b) For each case, determine the first four local minimum values of $\phi _ { n } ( x )$ in $( 0 , \pi )$ . (c) Write an elegant Chebfun program that determines the smallest value of $_ n$ for which these minima are not monotonically decreasing. (This effect was investigated by Gronwall [1912].)

Exercise 9.6. Sine integral. (a) Construct and plot a chebfun for the sine integral $\begin{array} { r } { \mathrm { S i } ( x ) = \int _ { 0 } ^ { x } t ^ { - 1 } \sin { t } d t } \end{array}$ for $x \in [ 0 , 1 0 ]$ . What is its length? (b) Same for $x \in [ 0 , 1 0 0 ]$ . (c) Same for $\dot { \boldsymbol { x } } \in [ 0 , 1 0 0 0 ]$ .

Exercise 9.7. An unresolvable function. The polynomial interpolant to $\sin ( 1 / x )$ through 100,000 Chebyshev points can be produced by the command $\textbf { f } = \mathtt { c h e b f u n } ( \mathbb { Q } ( \textbf x )$ $\mathtt { s i n } ( 1 / \mathtt { x } )$ ,100000). The plot produced by plot(f) looks as if there is a bug in the computation somewhere. Produce similar plots for 10000, 1000, and smaller even numbers of points and explain why, in fact, there is no bug.

Exercise 9.8. Decay away from discontinuity. (a) Plot the function $f ( x ) \ =$ $\cos ( 7 x ) \sin ( 3 x ) + \sin ( \sin ( x / 2 ) ) e ^ { x }$ on $[ - 1 , 1 ]$ as well as its interpolating polynomial $p _ { n } ( x )$ in $n + 1 = 1 0 0$ Chebyshev points. (b) Confirm the algebraic rate of decay away from the discontinuity by plotting $| f ( x ) - p _ { n } ( x ) |$ together with the function $c / | x |$ for a suitable value of $c$ . (c) Using the spline command as in Exercise 7.6 with a sufficiently fine equispaced grid, confirm that the rate of decay is exponential for spline interpolants.
