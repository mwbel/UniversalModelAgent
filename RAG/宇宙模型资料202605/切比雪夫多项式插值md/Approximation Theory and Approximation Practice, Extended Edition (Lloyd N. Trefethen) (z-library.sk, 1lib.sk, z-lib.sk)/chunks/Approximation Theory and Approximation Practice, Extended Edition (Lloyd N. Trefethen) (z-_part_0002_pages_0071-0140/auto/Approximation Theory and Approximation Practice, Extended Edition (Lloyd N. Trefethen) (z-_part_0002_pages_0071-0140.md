# Chapter 9. Gibbs Phenomenon

Polynomial interpolants and projections oscillate and overshoot near discontinuities. We have observed this Gibbs phenomenon already in Chapter 2, and now we shall look at it more carefully. We shall see that the Gibbs effect for interpolants can be regarded as a consequence of the oscillating inverse-linear tails of Lagrange polynomials, i.e., interpolants of Kronecker delta functions. Chapter 15 will show that these same tails, combined together in a different manner, are also the origin of Lebesgue constants of size $O ( \log n )$ , with implications throughout approximation theory.

To start, consider $\mathtt { s i g n } ( \mathtt { x } )$ , interpolated in $n + 1 = 1 0$ and 20 Chebyshev points. We take $n$ odd to avoid a grid point at the middle of the step.

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun $( \mathbf { \partial } ^ { \prime } \mathbf { x } ^ { \prime } )$ ; f = sign(x); subplot(1,2,1) plot(f,'k') hold on $\mathtt { f 9 } =$ chebfun(f,10); plot(f9,'.-') subplot(1,2,2) plot(f,'k'), hold on, $\yen 19 ~ =$ chebfun(f,20); plot(f19,'.-')

![](images/a41920a9115a68882886a5a5d6c6cfb20cacf995fedafa34b1e1d789705c5eb3.jpg)

Both of these figures show a substantial overshoot near the jump. As $n$ increases from 9 to 19, the overshoot gets narrower, but not shorter, and it will not go away as $n \to \infty$ . Let us zoom in and look at the plot on subintervals:

subplot(1,2,1), plot(f,'k'), hold on plot(f9,'.-','interval',[0 0.8]) subplot(1,2,2), plot(f,'k'), hold on plot(f19,'.-','interval',[0 0.4])

![](images/3e74bbafa1851a7007123be0b0d13fe831ca66da32948f2d4bf759b0904bc286.jpg)

We now zoom in further with analogous plots for $n = 9 9$ and 999.

subplot(1,2,1), plot(f, $^ { 1 } \mathtt { k } ^ { \prime } )$ , hold on   
$\mathtt { f 9 9 } =$ chebfun(f,100); plot(f99,'.-','interval',[0 0.08])   
subplot(1,2,2), plot(f,'k'), hold on   
$\mathbf { f } 9 9 9 ~ =$ chebfun(f,1000); plot(f999,'.-','interval',[0 0.008])

![](images/c1e5465a9e980e49e1325bfe0cab6fbb30233e4b9d5ceaa568f8e81052b9882c.jpg)

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

![](images/7c8788999043c554c7c2767b5dbad514d61ff969c97559c83ba6dcf5ea12398b.jpg)

Here are $\ell _ { 1 2 }$ and $\ell _ { 1 3 }$ :

$\mathtt { p } 1 2 \ =$ chebfun([zeros(1,12) 1 zeros(1,7)]);   
$\mathtt { p 1 3 } =$ chebfun([zeros(1,13) 1 zeros(1,6)]);   
subplot(1,2,1), plot(p12,'.-'), hold on, plot(xc,yl,'--r') subplot(1,2,2), plot(p13,'.-'), hold on, plot(xc,yl,'--r')

![](images/22a86db9515be1639567a9ad59e767e6c78a64bbab701f6b15ab4579d3ad838c.jpg)

Following (5.1), we note that by taking the sum of a sequence of such Lagrange functions, we get the interpolant to the function that jumps from 0 for $x < 0$ to $^ { 1 }$ for $x > 0$ . Here is the sum of the four just plotted, which is beginning to look like a square wave:

plot(p10+p11+p12+p13,'.-'), hold on, plot(xc,yl,'--r')

![](images/d20ed3ca107e1bcd81584662cbad935f8a0fe28d570f54fafd59402a32e277c1.jpg)

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

![](images/d47b726b556cb9c50e111d3ad41a9e075aa075ca74734581f44e4d52c496431a.jpg)

Wilbraham worked out the magnitude of the overshoot, and thus the following analogue of Theorem 9.1 is due to him.

Theorem 9.2. Gibbs phenomenon for Chebyshev projections. Let $f _ { n }$ be the degree $n$ Chebyshev projection of the sign function $f ( x ) = \mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ . Then as $n \to \infty$ ,

$$
\operatorname* { l i m } _ { n \to \infty } \| f _ { n } \| = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } { \frac { \sin { x } } { x } } d x = 1 . 1 7 8 9 7 9 7 4 4 4 7 2 1 6 7 \ldots .
$$

(The function $\begin{array} { r } { \mathrm { S i } ( x ) = \int _ { 0 } ^ { x } t ^ { - 1 } \sin { t } d t } \end{array}$ is known as the sine integral; see Exercise 9.6.) To see this number experimentally we can use the 'trunc' option in the Chebfun constructor. The overshoots look similar to what we saw before, but with smaller amplitude.

f = sign(x); subplot(1,2,1), plot(f,'k'), hold on $\begin{array} { r l } { \mathbf { f } 9 } & { { } = } \end{array}$ chebfun(f,'trunc',10); plot(f9,'-') subplot(1,2,2), plot(f,'k'), hold on $\yen 19 ~ =$ chebfun(f,'trunc',20); plot(f19,'-')

![](images/05db5756b4d57edfa7e5fe80873c79ffbffb6c7ba97a600becc9070fe0747966.jpg)

![](images/34f5a32f7a0ced3afff4edf602eebbd45a8d3b210eeb4a1286dc8a8a64eaab85.jpg)

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

# Chapter 10. Best Approximation

An old idea, going back to Chebyshev himself and earlier to Poncelet, is to look for a polynomial $p ^ { * }$ of specified degree $n$ that is the best approximation to a given continuous function $f$ in the sense of minimizing the $\infty$ -norm of the difference on an interval [Poncelet 1835, Chebyshev 1854 & 1859]. (A best approximation is also called a Chebyshev approximation, but we shall avoid this usage to minimize confusion. Other terms are minimax and equiripple.) It is known that $p ^ { * }$ exists and is unique, as we shall prove below. There is a Chebfun command minimax for computing these approximants, due to Silviu Filip and others: if $f$ is a chebfun, then minimax(f,n) is the chebfun corresponding to its best approximation of degree $n$ . For details see [Filip et al. 2018].

We shall argue in Chapter 16 that best approximations in the $\infty$ -norm are not always as useful as one might imagine; Chebyshev interpolants are often as good or even better. Nevertheless, they represent an elegant and fundamental idea and a line of investigation going back more than 150 years. So for the moment, let us enjoy them.

For example, here are the best approximants of degrees 2 and 4 to $| x |$ , together with their error curves $( f - p ^ { * } ) ( [ - 1 , 1 ] )$ :

x = chebfun $( \because \tt X ^ { \prime } )$ ; f = abs(x);   
for $\texttt { n } = \texttt { 2 : 2 : 4 }$ subplot(1,2,1), plot(f,'k') [p,err] $=$ minimax(f,n); hold on, plot(p,'b') subplot(1,2,2), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')   
end

![](images/305d97302ff976bf6e62aa896a493ed9f96bcf70060e2746ea4e69758baac280.jpg)

Notice the equioscillation property: the error curve attains its extreme magnitude with alternating signs at a succession of values of $x$ . Chebyshev appears to have known this in the 1850s, and indeed suggested he was not the first to know it (“comme on le sait,” p. 114 of [Chebyshev 1854]), but he did not explicitly address questions of existence, uniqueness, or even alternation of signs. More systematic treatments came at the beginning of the 20th century with work by Blichfeldt [1901], Kirchberger [1902], and Borel [1905]. It seems to have been Kirchberger, in his PhD thesis written under Hilbert, who first stated and proved the characterization theorem that is now so well known [Kirchberger 1902], proving in particular that a best approximation $p ^ { * }$ exists. Note that in the characterization part of this theorem, $f$ is assumed to be real, whereas most of the discussion in this book allows $f$ to be real or complex. Existence and uniqueness in the complex case were established by Tonelli [1908]. Complex generalizations of the characterization originate with [Kolmogorov 1948] and [Remez 1951]. Many further generalizations can also be found in the approximation theory literature, for example, with the set of polynomials on an interval replaced by a more general set of functions satisfying a property known as the Haar condition.

Theorem 10.1. Equioscillation characterization of best approximants. A continuous function $f$ on $[ - 1 , 1 ]$ has a unique best approximation $p ^ { * } \in \mathcal { P } _ { n }$ . If $f$ is real, then $p ^ { * }$ is real too, and in this case a polynomial $p \in \mathcal { P } _ { n }$ is equal to $p ^ { * }$ if and only if $f - p$ equioscillates in at least $n + 2$ extreme points.

Proof. A set of $n + 2$ points of equioscillation of this kind is called an alternant, though we shall not make much use of this term.

To prove existence of a best approximation, we note that $\| f - p \|$ is a continuous function of $p \in \mathcal { P } _ { n }$ . Since one candidate approximation is the zero function, we know that if $p ^ { * }$ exists, it lies in $\{ p \in { \mathcal { P } } _ { n } : \| f - p \| \leq \| f \| \}$ . This is a closed and bounded subset of a finite-dimensional space, hence compact (the Heine–Borel property), and thus the minimum is attained. (This argument originates with $\mathrm { F }$ . Riesz [1918].)

Next we show that equioscillation implies optimality. Suppose $f$ and $p$ are real and $( f - p ) ( x )$ takes equal extreme values with alternating signs at $n + 2$ points $x _ { 0 } < x _ { 1 } < \cdots < x _ { n + 1 }$ , and suppose $\| f - q \| < \| f - p \|$ for some real polynomial $q \in \mathcal { P } _ { n }$ . Then $p - q$ must take nonzero values with alternating signs at the equioscillation points, implying that it takes the value zero in at least $n { \mathrel { + { 1 } } }$ points in between. This implies that $p - q$ is identically zero, which is a contradiction.

The third step is to show that optimality implies equioscillation (this part of the argument was given in [Blichfeldt 1901]). Suppose $f - p$ equioscillates at fewer than $n + 2$ points, and set $E = \| f - p \|$ . Without loss of generality suppose the leftmost extremum is one where $f - p$ takes the value $- E$ . Then there are numbers $- 1 < x _ { 1 } < \cdot \cdot \cdot < x _ { k } < 1$ with $k \leq n$ such that $( f - p ) ( x ) < E$ for $x \in [ - 1 , x _ { 1 } ] \cup$ $[ x _ { 2 } , x _ { 3 } ] \cup [ x _ { 4 } , x _ { 5 } ] \cup \ldots$ and $( f - p ) ( x ) > - E$ for $x \in [ x _ { 1 } , x _ { 2 } ] \cup [ x _ { 3 } , x _ { 4 } ] \cup \cdot \cdot \cdot .$ If we define $\delta p ( x ) = ( x _ { 1 } - x ) ( x _ { 2 } - x ) \cdot \cdot \cdot ( x _ { k } - x )$ , then $( p - \varepsilon \delta p ) ( x )$ will be a better approximation than $p$ to $f$ for all sufficiently small $\varepsilon > 0$ .

Finally, to prove uniqueness of best approximations—we treat the real case only—we refine the argument that equioscillation implies optimality. Suppose $p$ is a best approximation with equioscillation extreme points $x _ { 0 } < x _ { 1 } < \cdots < x _ { n + 1 }$ , and suppose $\| f - q \| ~ \leq ~ \| f - p \|$ for some real polynomial $q \in \mathcal { P } _ { n }$ . Then (without loss of generality) $( p - q ) ( x )$ must be $\leq 0$ at $x _ { 0 } , x _ { 2 } , x _ { 4 } , \ldots$ and $\geq 0$ at $x _ { 1 } , x _ { 3 } , x _ { 5 } , \dotsc .$ This implies that $p - q$ has roots in each of the $n + 1$ closed intervals $[ x _ { 0 } , x _ { 1 } ] , [ x _ { 1 } , x _ { 2 } ] , \dotsc , [ x _ { n } , x _ { n + 1 } ]$ . We wish to conclude that $p - q$ has at least $n + 1$ roots in total, counted with multiplicity, implying that $p = q$ . To make the argument we prove by induction that $p - q$ has at least $k$ roots in $[ x _ { 0 } , x _ { k } ]$ for each $k$ . The case $k = 1$ is immediate. For the general case, suppose $p - q$ has at least $j$ roots in $[ x _ { 0 } , x _ { j } ]$ for each $j \le k - 1$ but only $k - 1$ roots in $[ x _ { 0 } , x _ { k } ]$ . Then there must be a simple root at $x _ { k - 1 }$ . By the induction hypothesis, $p - q$ must have exactly $k - 2$ roots in $[ x _ { 0 } , x _ { k - 2 } ]$ with a simple root at $x _ { k - 2 }$ , $k - 3$ roots in $[ x _ { 0 } , x _ { k - 3 } ]$ with a simple root at $x _ { k - 3 }$ , and so on down to 1 root in $[ x _ { 0 } , x _ { 1 } ]$ , with a simple root at $x _ { 1 }$ . It follows that $p - q$ must be nonzero at $x _ { 0 }$ and at $x _ { k }$ , and since the sign of $p - q$ changes at each of the simple roots $x _ { 1 } , \ldots , x _ { k - 1 }$ , the signs at $x _ { 0 }$ and $x _ { k }$ must be the same if $k$ is odd and opposite if $k$ is even. On the other hand, from the original alternation condition we know that $p - q$ must take the same signs at $x _ { 0 }$ and $x _ { k }$ if $k$ is even and opposite signs if $k$ is odd.

There is a simpler proof of uniqueness than the one just given, in which one supposes $p$ and $q$ are distinct best approximations and considers $( p + q ) / 2$ (Exercise 10.10). However, that proof does not generalize to the problem of rational approximation (Theorem 24.1).

Note that the error curve for a best approximation may have more than $n + 2$ points of equioscillation, and indeed this will always happen if $f$ and $n$ are both even or both odd (Exercise 10.4). For example, for the function $f ( x ) = \left| x \right|$ considered above, the degree 2 approximation equioscillates at 5 points, not 4, and the degree 4 approximation equioscillates at 7 points, not 6. This phenomenon of “extra” points of equioscillation will become important in the generalization to rational approximation in Chapter 24.

Here is another example, the degree 10 best approximation to $\exp ( x )$ . There are 12 points of equioscillation.

f = exp(x); [p,err] $=$ minimax(f,10); plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/8e2e0618097c13d769454a2b0be72f9d2f0c0714f3644ade1d8d25529b4834c8.jpg)

And here is another example. The Chebfun cumsum command returns the indefinite integral, producing in this case a zigzag function.

f = cumsum(sign(sin(20\*exp(x)))); plot(f,'k'), hold on [p,err] $=$ minimax(f,20); plot(p)

![](images/7e60c660203476097b15f215657c12a267cb7ca11a74416508c3af3200082041.jpg)

The corresponding error curve reveals $2 0 + 2 = 2 2$ points of equioscillation:

plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/ce8e5be65aa0e3ce8ba127374c5394c0f01ca8b05df5dda292cb52f4814ca2cf.jpg)

Here’s the analogous curve for degree 30, plotted on the same scale.

[p,err] $=$ minimax(f,30); plot $( \tt f - p )$ , hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/8ae0b68648d55d83481ff1b590333b589f91c45076e247be52091368be8dd475.jpg)

The algorithm underlying minimax, known as the Remez algorithm or the exchange algorithm, goes back to the Soviet mathematician Evgeny Remez in 1934 and is based on iteratively adjusting a trial alternant until it converges to a correct one [Remes 1934a, 1934b, Remez 1957; Powell 1981]. We shall not give details here, but in fact, Chebfun is an excellent platform for such computations since the algorithm depends on repeatedly finding the local extrema of trial error curves, an operation carried out easily via the roots command (see Chapter 18). Also crucial to the success of minimax is the use of the barycentric representation (5.11) for all polynomials, based not at Chebyshev points but at the points of each trial alternant [Filip et al. 2018]. (The observations of [Webb, Trefethen & Gonnet 2012] suggest that it might be better to use the “first barycentric formula” (5.9).)

The history of the Remez algorithm is interesting, or perhaps we should say the sociology. It stands out as one of the preeminent examples of a nontrivial algorithm for a nonlinear computational problem that was developed before the invention of computers. Perhaps in part because of this early appearance, it became remarkably well known, a fixture in numerical analysis courses worldwide. One might imagine, based on its fame, that the Remez algorithm must be very important in practice, but in fact it seems there is not much software and just a moderate amount of use of these ideas. One application has been in the design of routines for computing special functions [Cody, Fraser & Hart 1968, Cody 1993, Muller 2006]. Another is in the field of digital signal processing, where variants of the Remez ideas were developed by Parks and McClellan beginning in 1971 with tremendous success for designing low-pass, high-pass, and other digital filters [Parks & McClellan 1972]. Parks and McClellan too found that the use of a barycentric representation was crucial, as they describe memorably in [McClellan & Parks 2005].

Chapter 16 will show that Chebyshev interpolants are often as good as best approximations in practice, and this fact may have something to do with why the Remez algorithm is used rather rarely. Chapter 20 will show that if you really want a best approximation, it may be more practical to compute it by CF approximation than by the Remez algorithm, at least if $f$ is smooth. There are also other algorithms for computing best approximations, based, for example, on linear programming, which we shall not discuss.

Summary of Chapter 10. Any $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $p ^ { * } \in \mathcal { P } _ { n }$ with respect to the $\infty$ -norm. If $f$ is real, $p ^ { * }$ is characterized by having an error curve that equioscillates between at least $n + 2$ extreme points.

Exercise 10.1. A function with spikes. Compute numerically the degree 10 polynomial best approximation to $\mathrm { s e c h } ^ { 2 } ( 5 ( x + 0 . 6 ) ) + \mathrm { s e c h } ^ { 4 } ( 5 0 ( x + 0 . 2 ) ) + \mathrm { s e c h } ^ { 6 } ( 5 0 0 ( x - 0 . 2 ) )$ on $[ - 1 , 1 ]$ and plot $f$ together with $p ^ { * }$ as well as the error curve. What is the error? How does this compare with the error in 11-point Chebyshev interpolation?

Exercise 10.2. Best approximation of $| x |$ . (a) Use Chebfun to determine the errors $E _ { n } \ = \ \| f - p _ { n } \|$ in the degree $n$ best approximation of $f ( x ) \ = \ | x |$ on $[ - 1 , 1 ]$ for $n =$ $2 , 4 , 8 , \ldots , 2 5 6$ , and make a table of the values $\beta _ { n } ~ = ~ n E _ { n }$ as a function of $n$ . (b) Use Richardson extrapolation to improve your data. How many digits can you estimate for the limiting number $\beta = \mathrm { l i m } _ { n  \infty } \beta _ { n } \mathrm { : }$ (We shall discuss this problem in detail in Chapter 25.)

Exercise 10.3. de la Vall´ee Poussin lower bound. Suppose an approximation $p \in \mathcal { P } _ { n }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } <$ $s _ { 1 } < \cdot \cdot \cdot < s _ { n + 1 } \leq 1$ at which $f - p$ alternates in sign with $| f ( s _ { j } ) - p ( s _ { j } ) | \geq \varepsilon$ for some $\varepsilon > 0$ . Show that $\| f - p ^ { * } \| \geq \varepsilon$ . (This estimate originates in [de la Vall´ee Poussin 1910].)

Exercise 10.4. Best approximation of even functions. Let $f \in C ( [ - 1 , 1 ] )$ be an even function, i.e., $f ( - x ) = f ( x )$ for all $_ x$ . (a) Prove as a corollary of Theorem 10.1 that for any $n \geq 0$ , the best approximation $\boldsymbol { p } _ { n } ^ { * }$ is even. (b) Prove that for any $n \geq 0$ , $p _ { 2 n } ^ { * } = p _ { 2 n + 1 } ^ { * }$ . (c) Conversely, suppose $f \in C ( [ - 1 , 1 ] )$ is not even. Prove that for all sufficiently large $n$ , its best approximations $\boldsymbol { p } _ { n } ^ { * }$ are not even.

Exercise 10.5. An invalid theorem. The first two figures of this chapter suggest the following “theorem”: if $f$ is an even function on $[ - 1 , 1 ]$ and $p ^ { * }$ is its best approximation of some degree $_ n$ , then one of the extreme points of $| ( f - p ^ { * } ) ( x ) |$ occurs at $x = 0$ . Pinpoint the flaw in the following “proof.” By the argument of Exercise 10.4(b), $p ^ { * }$ is the best approximation to $f$ for all $n$ in some range of the form even $\leq n \leq$ odd, such as $4 \leq n \leq 5$ or $1 0 \leq n \leq 1 3$ . By Theorem 10.1, the maximal number of equioscillation points of $f - p ^ { * }$ must accordingly be of the form $\mathrm { o d d } + 2$ , that is, odd. By symmetry, 0 must be one of these points. Exactly which of these three logical steps is invalid, and why?

Exercise 10.6. Nonlinearity of best approximation operator. We have mentioned that for given $_ n$ , the operator that maps a function $f \in C ( [ - 1 , 1 ] )$ to its best degree $n$ approximation $p _ { n } ^ { * }$ is nonlinear. Prove this (on paper, not numerically) by finding two functions $f _ { 1 }$ and $f _ { 2 }$ and an integer $n \geq 0$ such that the best approximation of the sum in $\mathcal { P } _ { n }$ is not the sum of the best approximations.

Exercise 10.7. Bernstein’s lethargy theorem. Exercise 6.1 considered a function of Weierstrass, continuous but nowhere differentiable. A variant of the same function based on Chebyshev polynomials would be

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } 2 ^ { - k } T _ { 3 ^ { k } } ( x ) .
$$

(a) Show that the polynomial $f _ { 3 ^ { k } }$ obtained by truncating (10.1) to degree $3 ^ { k }$ is the best approximation to $f$ in the spaces $\mathcal { P } _ { n }$ for certain $n$ . What is the complete set of $_ n$ for which this is true? What is the error? (b) Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Prove that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - p _ { n } ^ { * } \| \geq \varepsilon _ { n }$ for all $_ n$ . (Hint: Change the coefficients $2 ^ { - k }$ of (10.1) to values related to $\left\{ \varepsilon _ { n } \right\}$ .)

Exercise 10.8. Continuity of best approximation operator. For any $n \geq 0$ , the mapping from functions $f \in C ( [ - 1 , 1 ] )$ to their best approximants $p ^ { * } \in \mathcal { P } _ { n }$ is continuous with respect to the $\infty$ -norm in $C ( [ - 1 , 1 ] )$ . Prove this by an argument combining the uniqueness of best approximations with compactness. (This continuity result appears in Section I.5 of [Kirchberger 1902]. In fact, the mapping is not just continuous but Lipschitz continuous, a property known as strong uniqueness, but this is harder to prove.)

Exercise 10.9. Approximation of $e ^ { x }$ . Truncating the Taylor series for $e ^ { x }$ gives polynomial approximations with maximum error $E _ { n } \sim 1 / ( n + 1 ) !$ ! on $[ - 1 , 1 ]$ , but the best

approximations do better by a factor of $2 ^ { n }$ :

$$
E _ { n } \sim \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } , \quad n \to \infty .
$$

(a) Derive (10.2) by combining Exercises 3.15 and 10.3 with the asymptotic formula $I _ { k } ( 1 ) \sim$ $1 / ( 2 ^ { n } n ! )$ . (b) Make a table comparing this estimate with the actual values $E _ { n }$ computed numerically for $0 \leq n \leq 1 0$ .

Exercise 10.10. Alternative proof of uniqueness. Prove uniqueness of the degree $_ n$ best approximant to a real continuous function $f$ by a simpler argument than the one given in the proof of Theorem 10.1: suppose $p$ and $q$ are best approximants, and apply the equioscillation characterization to $r = ( p + q ) / 2$ .

Exercise 10.11. Chebyshev polynomials and best approximations. (a) What is the best degree $n$ polynomial approximation to $x ^ { n + 1 }$ on $[ - 1 , 1 ]$ ? What is the error? Derive the answers from Theorem 10.1, using the fact that $T _ { n + 1 }$ oscillates between values $\pm 1$ at $n + 2$ points in $[ - 1 , 1 ]$ . (b) What is the best approximation to 0 among monic polynomials of degree $n + 1$ ? What is the error?

Exercise 10.12. Every best approximant is an interpolant. Let $p$ be the best approximation in $\mathcal { P } _ { n }$ to a real function $f \in C ( [ - 1 , 1 ] )$ . Show that there exist $n + 1$ distinct points $- 1 < x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < 1$ such that $p$ is the interpolant in $\mathcal { P } _ { n }$ to $f$ in the points $\{ x _ { j } \}$ .

Exercise 10.13. A contrast to Faber’s theorem. Although Faber showed that there does not exist an array of nodes in $[ - 1 , 1 ]$ whose polynomial interpolants converge for every $f \in C [ - 1 , 1 ]$ , for any fixed $f$ there exists an array whose interpolants converge to $f$ [Marcinkiewicz 1936–37]. Prove this by combining the Weierstrass approximation theorem with the result of the previous exercise.

Exercise 10.14. Asymptotics of the leading coefficient. Let $\{ p _ { n } ^ { * } \}$ be the sequence of best approximations of a function $f \in C ( [ - 1 , 1 ] )$ , and let $p _ { n } ^ { * }$ have leading Chebyshev coefficient $a _ { n } ^ { * }$ . It is known that $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n  \infty } | a _ { n } ^ { * } | ^ { 1 / n } \leq 1 } \end{array}$ , with strict inequality if and only if $f$ is analytic on $[ - 1 , 1 ]$ [Blatt $\&$ Saff 1986, Thm. 2.1]. Verify this result numerically by estimating $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } | a _ { n } ^ { * } | ^ { 1 / n } } \end{array}$ for $f ( x ) = \left| x \right|$ and $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ .

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

![](images/090cff5c4738302a6fcbdad53de7cd8f1a2262647cb46fe39db17c40c333d410.jpg)

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

![](images/afe169c097c908d62ba4b88cfbff7e960b0d4a932919f120384b9d8e1fa1f44c.jpg)

With the MATLAB contour command we can examine the size of $\ell ( x )$ for complex values of $x$ . The following code plots contours at $| \ell ( x ) | = 2 ^ { - 6 } , 2 ^ { - 5 } , \ldots , 1$ .

$\mathtt { p l o t } ( \mathtt { x j } , \mathtt { e l l } ( \mathtt { x j } ) , \mathtt { \xi ^ { \prime } . k ^ { \prime } } )$ , hold on xgrid $= - 1 . 5 \colon . 0 2 \colon 1 . 5$ ; ygrid $=$ -0.9:.02:0.9; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $= \ 2 . \widehat { \ } ( - 6 : 0 )$ ; contour(xx,yy,abs(ellzz),levels,'k')

![](images/c40f562791a686ecdce074397048601bf36943b6a91d23b2f186af2ac7560a97.jpg)

We can see a great deal in this figure. On $[ - 1 , 1 ]$ , it confirms that $\ell ( x )$ is small, with maximum value $| \ell ( x ) | = 2 ^ { - 6 }$ at $x = 0$ . Away from $[ - 1 , 1 ]$ , $| \ell ( x ) |$ grows rapidly and takes constant values on curves that look close to ellipses. For $t$ on the outermost of the curves plotted, the ratio $| \ell ( x ) / \ell ( t ) |$ will be bounded by $2 ^ { - 6 }$ for any $x \in [ - 1 , 1 ]$ .

Let us compare this to the very different behavior if we take points that are not close to the Chebyshev distribution. To make a specific and quite arbitrary choice, let us again take 8 points, four of them at $^ { - 1 }$ and four at 1. Here is the plot on the real axis.

xj = [-1 -1 -1 -1 1 1 1 1]; ell $=$ poly(xj,d); plot(ell), hold on, plot(xj,ell(xj),'.k')

![](images/735248b016b94bc01c6ecb06875918eb06e82c81ea69dfd0573119617f4f1c3d.jpg)

And here are the contours in the complex plane.

plot(xj,ell(xj),'.k'), hold on, ellzz $=$ ell(zz); contour(xgrid,ygrid,abs(ellzz),levels, $" \Bbbk ^ { \prime }$ )

![](images/9fc45111788ab22960429d13c7ae118b2fd5143e928513ab505ef2fc73aaee02.jpg)

These figures show that the size of $\ell ( x )$ on $[ - 1 , 1 ]$ is not at all uniform: it is far smaller than $2 ^ { - 6 }$ for $x \approx \pm 1$ , but as big as $1$ at $x = 0$ . Now, for $x \in [ - 1 , 1 ]$ and $t$ on the outermost curve shown, the maximum of the ratio $| \ell ( x ) / \ell ( t ) |$ is no better than 1 since that curve touches $[ - 1 , 1 ]$ . If we wanted to achieve $| \ell ( x ) / \ell ( t ) | \leq 2 ^ { - 6 }$ as in the last example, $\Gamma$ would have to be a much bigger curve—closer to the “stadium”:

xgrid = -2:.04:2; ygrid = -1.5:.04:1.5; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathsf { z } \mathsf { z } = \mathsf { x } \mathbf { x } \mathsf { + } 1 \mathrm { i } \ast \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $=$ $[ 2 \hat { \bf \Phi } 6 , 2 \hat { \bf \Phi } 6 ]$ ; hold on, contour(xgrid,ygrid,abs(ellzz),levels,'r')

![](images/4e87f3763916a780709955cb00df5e640ab61cfe74abb1ec7b01d0710b1cc9a5.jpg)

The function $f$ would have to be analytic within this much larger region for the bound (11.9) to apply with a ratio $| \ell ( x ) / \ell ( t ) |$ as favorable as $2 ^ { - 6 }$ .

Summary of Chapter 11. The error of a polynomial interpolant can be represented by a contour integral in the complex plane, the Hermite integral formula. This provides the standard method for showing geometric convergence for certain approximations of analytic functions.

Exercise 11.1. Chebfun computation of Cauchy integrals. (a) Figure out (on paper) the polynomial $p \in \mathcal { P } _ { 2 }$ that takes the values $p ( - 1 ) = 1$ , $p ( 1 / 2 ) = 2$ , and $p ( 1 ) = 2$ . What is $p ( 2 )$ ? (b) Read about the numerical computation of Cauchy integrals in Chapter 5 of the online Chebfun Guide. Write a program to confirm Theorem 11.1 by computing $p ( 2 )$ numerically by a Cauchy integral for the function $f ( x ) = ( x + 1 ) ( x - 0 . 5 ) ( x - 1 ) e ^ { x } + 1 1 / 6 +$ $x / 2 - x ^ { 2 } / 3$ . Take both $| x | = 3 / 2$ and $| x | = 3$ as contours to confirm that it does not matter whether or not $\Gamma$ encloses $_ x$ . (c) Write an anonymous function $\mathfrak { p } \ : = \ : \mathfrak { Q } ( \mathbf { x } ) . . .$ to apply the above calculation not just for $x = 2$ but for arbitrary $_ x$ , and construct a chebfun on $[ - 1 , 1 ]$ from this anonymous function. Do its coefficients as reported by poly match your expectations?

Exercise 11.2. Confluent interpolation points. Modify the above problem to require $p ( - 1 ) = 1$ , $p ( 1 ) = 2$ , and $p ^ { \prime } ( 1 ) = 0$ . This is a Hermite interpolation problem, in which some interpolation points are specified multiply with corresponding values specified for derivatives. What is the analytic solution to this interpolation problem? Do the computations involving contour integrals and anonymous functions deliver the right result?

Exercise 11.3. Interpolation in a disk. Suppose a function $f$ is interpolated by polynomials in arbitrary points of the disk $| x | \leq r ^ { \prime }$ and we measure the accuracy $f ( x ) { - } p ( x )$ for $_ x$ in the disk $| x | \leq r$ . Show that geometric convergence is ensured (in exact arithmetic, ignoring rounding errors) if $f$ is analytic in the disk $| x | \le r + 2 r ^ { \prime }$ . Give the constant $\rho$ for convergence at the rate $O ( \rho ^ { - n } )$ . (This result originates with [M´eray 1884].)

Exercise 11.4. Working around a simple pole. Let $f$ be analytic on the closed Bernstein ellipse region $\overline { { E } } _ { \rho }$ for some $\rho > 1$ . It can be shown that $| \ell ( x ) / \ell ( t ) | = O ( \rho ^ { - n } )$ uniformly as $n \to \infty$ for $x \in [ - 1 , 1 ]$ and $t$ on the ellipse, and thus Theorem 11.1 can be used to show that $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as asserted by Theorem 8.2. Now suppose that $f$ has a finite number of singularities on the ellipse but these are just simple poles. Explain how the contour integral argument can be modified to show that the rate of convergence will still be $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as was established by another method in Exercise 8.15.

# Chapter 12. Potential Theory and Approximation

The explorations of the last chapter are glimmerings of potential theory in the complex plane, a subject that has been connected with approximation of functions at least since the work of Walsh early in the 20th century [Walsh 1969]. In this chapter we shall outline this connection. Potential theory in the complex plane is presented in [Ransford 1995] and [Finkelshtein 2006], and a survey of applications in approximation theory can be found in [Levin & Saff 2006].

We begin by looking again at (11.10), the formula giving the ratio of the size of the node polynomial $\ell$ at an approximation point $x$ to its size at a point $t$ o n a contour $\Gamma$ . Notice that the numerator and the denominator of this formula each contain a product of $n + 1$ terms. With this in mind, let us define $\gamma _ { n } ( x , t )$ as the following $( n + 1 ) \mathrm { s t }$ root:

$$
\gamma _ { n } ( x , t ) = { \frac { \left( \prod _ { j = 0 } ^ { n } | t - x _ { j } | \right) ^ { 1 / ( n + 1 ) } } { \left( \prod _ { j = 0 } ^ { n } | x - x _ { j } | \right) ^ { 1 / ( n + 1 ) } } } .
$$

Then the magnitude of the quotient in (11.10) becomes

$$
\left| \frac { \ell ( x ) } { \ell ( t ) } \right| = \gamma _ { n } ( x , t ) ^ { - n - 1 } .
$$

This way of writing things brings out a key point: if $\gamma _ { n } ( x , t )$ is bounded above $1$ , we will get exponential convergence as $n \to \infty$ . With this in mind, let us define $\alpha _ { n }$ to be the scalar

$$
\alpha _ { n } = \operatorname* { m i n } _ { x \in X , t \in \Gamma } \gamma _ { n } ( x , t ) ,
$$

where $x$ ranges over a domain $X$ where we wish to approximate $f$ (say, $X = [ - 1 , 1 ]$ ) and $t$ ranges over a contour $\Gamma$ enclosing that domain. If $\alpha _ { n } \geq \alpha$ for some $\alpha > 1$ for all sufficiently large $n$ , and if $f$ is analytic in the region bounded by $\Gamma$ , then (11.9) tells us that $p ( x )$ must converge to $f ( x )$ at the rate $O ( \alpha ^ { - n } )$ .

The condition $\alpha _ { n } > 1$ has a geometric interpretation. The numerator of (12.1) is the geometric mean distance of $t$ to the grid points $\{ x _ { j } \}$ , and the denominator is the geometric mean distance of $x$ to the same points. If $\alpha _ { n } > 1$ , then every point $t \in \Gamma$ is at least $\alpha _ { n }$ times farther from the grid points, in the geometric mean sense, than every point $x$ in the approximation domain. It is this property that allows the Hermite integral formula to show exponential convergence.

To bring these observations into potential theory, we linearize the products by taking logarithms. From (12.1) we find

$$
\log \gamma _ { n } ( x , t ) = \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \log | t - x _ { j } | - \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \log | x - x _ { j } | .
$$

Let us define the discrete potential function associated with the points $x _ { 0 } , \ldots , x _ { n }$ by

$$
u _ { n } ( s ) = { \frac { 1 } { n + 1 } } \sum _ { j = 0 } ^ { n } \log | s - x _ { j } | .
$$

Note that $u _ { n }$ is a harmonic function throughout the complex $s$ -plane away from the grid points, that is, a solution of the Laplace equation $\Delta u _ { n } = 0$ . We may think of each $x _ { j }$ as a point charge of strength $1 / ( n + 1 )$ , like an electron, and of $u _ { n }$ as the potential generated by all these charges, whose gradient defines an “electric” field. A difference from the electrical case is that whereas electrons repel one another with an inverse-square force, whose potential function is inverse-linear, here in the twodimensional plane the repulsion is inverse-linear and the potential is logarithmic. (Some authors put a minus sign in front of (12.5), so that the potential approaches $\infty$ rather than $- \infty$ as $s  x _ { j }$ , making $u _ { n }$ an energy rather than the negative of an energy.)

From (12.4) and (12.5) we find

$$
\log { \gamma _ { n } ( x , t ) } = u _ { n } ( t ) - u _ { n } ( x ) ,
$$

and hence by (12.2),

$$
\left| \frac { \ell ( x ) } { \ell ( t ) } \right| = e ^ { ( n + 1 ) [ u _ { n } ( x ) - u _ { n } ( t ) ] } .
$$

If $\alpha _ { n } \geq \alpha > 1$ for all sufficiently large $n$ , as considered above, then $\log { \gamma _ { n } ( x , t ) } \geq$ $\log \alpha _ { n } \geq \log \alpha > 0$ , so we have

$$
\operatorname* { m i n } _ { t \in \Gamma } u _ { n } ( t ) - \operatorname* { m a x } _ { x \in X } u _ { n } ( x ) \geq \log \alpha .
$$

Together with (11.9) this implies

$$
\| f - p \| = O ( e ^ { - n \log \alpha } ) .
$$

Notice the flavor of this result: the interpolants converge exponentially, with a convergence constant that depends on the difference of the values taken by the potential function on the set of points where the interpolant is to be evaluated and on a contour inside which $f$ is analytic.

We now take the step from discrete to continuous potentials. Another way to write (12.5) is as a Lebesgue–Stieltjes integral [Stein $\&$ Shakarchi 2005],

$$
u ( s ) = \int _ { - 1 } ^ { 1 } \log | s - \tau | d \mu ( \tau ) ,
$$

where $\mu$ is a measure consisting of a sum of Dirac delta functions, each of strength $1 / ( n + 1 )$ ,

$$
\mu ( \tau ) = \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \delta ( \tau - x _ { j } ) .
$$

This is the potential or logarithmic potential associated with the measure $\mu$ . The same formula (12.7) also applies if $\mu$ is a continuous measure, which will typically be obtained as the limit of a family of discrete measures as $n  \infty$ . (The precise notion of convergence appropriate for this limit is known as weak $^ *$ convergence, pronounced “weak-star.”) Equally spaced grids in $[ - 1 , 1 ]$ converge to the limiting measure

$$
\mu ( \tau ) = \frac { 1 } { 2 } .
$$

Chebyshev grids in $[ - 1 , 1 ]$ converge to the Chebyshev measure identified in Exercise 2.2,

$$
\mu ( \tau ) = \frac { 1 } { \pi \sqrt { 1 - \tau ^ { 2 } } } ,
$$

and so do other grids associated with zeros or extrema of orthogonal polynomials on $[ - 1 , 1 ]$ , such as Legendre, Jacobi, or Gegenbauer polynomials (see Chapter 17).

And now we can identify the crucial property of the Chebyshev measure (12.10): The potential (12.7) it generates is constant on $[ - 1 , 1 ]$ . The measure is known as the equilibrium measure for $\lfloor - 1 , 1 \rfloor$ , and physically, it corresponds to one unit of charge adjusting itself into an equilibrium, minimal-energy distribution. Given a unit charge distribution $\mu$ with support on $[ - 1 , 1 ]$ , the associated energy is the integral

$$
I ( \mu ) = - \int _ { - 1 } ^ { 1 } u ( s ) d \mu ( s ) = - \int _ { - 1 } ^ { 1 } \int _ { - 1 } ^ { 1 } \log | s - \tau | d \mu ( \tau ) d \mu ( s ) .
$$

It is clear physically, and can be proved mathematically, that for $I ( \mu )$ to be minimized, $u ( s )$ must be constant, so the gradient of the potential is zero and there are no net forces on the points in $( - 1 , 1 )$ [Ransford 1995].

This discussion has gone by speedily, and the reader may have to study these matters several times to appreciate how naturally ideas associated with electric charges connect with the accuracy of polynomial approximations. Potential theory is also of central importance in the study of approximation by rational functions; see [Levin $\&$ Saff 2006] and [Stahl $\&$ Schmelzer 2009].

We have just characterized the equilibrium measure $\mu$ for interpolation on $[ - 1 , 1 ]$ as the unit measure on $[ - 1 , 1 ]$ that generates a potential $u$ that takes a constant value. To be precise, $u$ is the solution to the following problem involving a Green’s function: find a function $u ( s )$ in the complex $s$ -plane that is harmonic outside $[ - 1 , 1 ]$ , approaches a constant value as $s  [ - 1 , 1 ]$ , and is equal to $\log | s | + O ( s ^ { - 1 } )$ as $s \to \infty$ . (This last condition comes from the property that the total amount of charge is 1.) Quite apart from the motivation from approximation theory, suppose we are given this Green’s function problem to solve. Since Laplace’s equation is invariant under conformal maps, the solution can be derived by introducing a conformal map that transplants the exterior of the interval to the exterior of a disk, taking advantage of the fact that the Green’s function problem is trivial on a disk. Such a mapping is the function

$$
z = \phi ( s ) = { \frac { 1 } { 2 } } ( s + i \sqrt { 1 - s ^ { 2 } } ) ,
$$

which maps the exterior of $[ - 1 , 1 ]$ in the $s$ -plane onto the exterior of the disk $| z | \leq$ $1 / 2$ in the $z$ -plane. There, the solution of the potential problem is $\log | z |$ . Mapping back to $s$ , we find that the Chebyshev potential is given by $u ( s ) = \log | \phi ( s ) |$ , that is,

$$
u ( s ) = \log | s + i \sqrt { 1 - s ^ { 2 } } | - \log 2 ,
$$

with constant value $u ( s ) = - \log 2$ on $[ - 1 , 1 ]$ .

By definition, the Green’s function has a constant value on $[ - 1 , 1 ]$ , namely $u ( s ) =$ $- \log 2$ . For values $u _ { 0 } > - \log 2$ , the equation $u ( s ) = u _ { 0 }$ defines an equipotential curve enclosing $[ - 1 , 1 ]$ that is exactly the Bernstein ellipse $E _ { \rho }$ with $\rho = 2 \exp ( u _ { 0 } )$ , as defined in Chapter 8. Here is a contour plot of (12.13), confirming that the contours look the same as the ellipses plotted there. The factor $\mathtt { s i g n } ( \mathrm { i m a g } ( \mathbf { s } ) )$ is included to make $\mathbf { u }$ return the correct branch of the square root for $\mathrm Ḋ s Ḍ < 0$ .

u = @(s) log(abs(s+1i\*sign(imag(s)).\*sqrt(1-s.^2))) - log(2);   
xgrid = -1.5:.02:1.5; ygrid $=$ -0.91:.02:0.91;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); ss $=$ xx+1i\*yy; uss $=$ u(ss);   
levels $=$ -log(2) + log(1.1:0.1:2);   
contour(xgrid,ygrid,uss,levels,'k')

![](images/f02a656d73d03252be05c615386be61c1403cddad82c6f977c049a4c1974549c.jpg)

The constant $- \log 2$ in (12.13) is a reflection of the length of the interval $[ - 1 , 1 ]$ . Specifically, this constant is the logarithm of the capacity (or logarithmic capacity or transfinite diameter ) of $[ - 1 , 1 ]$ ,

$$
c = { \frac { 1 } { 2 } } .
$$

The capacity is a standard notion of potential theory, and in a simply connected two-dimensional case like this one, it can be defined as the radius of the equivalent disk. The associated minimal energy is the Robin constant of $[ - 1 , 1 ]$ :

$$
\operatorname* { m i n } _ { \mu } I ( \mu ) = - \log ( c ) = \log 2 .
$$

The fact that the capacity of $[ - 1 , 1 ]$ is $1 / 2$ has the following interpretation, explored earlier in Exercise 2.6. For Chebyshev or other asymptotically optimal grids on $[ - 1 , 1 ]$ , in the limit $n  \infty$ , each grid point lies at a distance $1 / 2$ from the others in the geometric mean sense.

This is a book about approximation on intervals, but it is worth noting that all these ideas of equilibrium measure, minimal energy, Robin constant, and capacity generalize to other compact sets $E$ in the complex plane. If $E$ is connected, then $\mu$ and $u$ can be obtained from a conformal map of its exterior onto the exterior of a disk, whereas if it is disconnected, a more general Green’s function problem may be solved. In any case, the equilibrium measure, which is supported on the outer boundary of $E$ , describes a good asymptotic distribution of interpolation points as $n \to \infty$ , and the limiting geometric mean distance from one point to the others is equal to the capacity, which is related to the Robin constant by $c ( E ) =$ $\mathrm { e x p } ( - \mathrm { m i n } _ { \mu } I ( \mu ) )$ .

Having discussed the continuous limit, let us return to the finite problem of finding good sets of $n + 1$ points $\{ x _ { j } \}$ for interpolation by a polynomial $p \in \mathcal { P } _ { n }$ on a compact set $E$ in the complex plane. Three particular families of points have received special attention. We say that $\{ x _ { j } \}$ is a set of Fekete points for the given $n$ and $E$ if the quantity

$$
{ \bigg ( } \prod _ { j < k } | x _ { j } - x _ { k } | { \bigg ) } ^ { 2 / n ( n + 1 ) } ,
$$

which is the geometric mean of the distances between the points, is as large as possible, that is, the points are exactly in a minimal-energy configuration. As $n  \infty$ , these maximal quantities decrease monotonically to $c ( E )$ , the fact which gives rise to the expression “transfinite diameter.” As a rule Fekete points have some of the cleanest mathematical properties for a given set $E$ but are the hardest to compute numerically. Next, if $E$ is connected and $\phi ( x )$ is a map of its exterior to the exterior of a disk in the $z$ -plane centered at the origin, a set of Fej´er points is a set $\phi ^ { - 1 } ( \{ z _ { j } \} )$ , where $\{ z _ { j } \}$ consists of any $n + 1$ points spaced equally around the boundary circle. Fej´er points are more readily computable since it is often possible to get one’s hands on a suitable mapping $\phi$ . Finally, Leja points are approximations to Fekete points obtained by a “greedy algorithm.” Here, one starts with an arbitrary first point $x _ { 0 } \in E$ and then computes successive points $x _ { 1 } , x _ { 2 } , \dotsc$ by an incremental version of the Fekete condition: with $x _ { 0 } , \ldots , x _ { n - 1 }$ known, $x _ { n }$ is chosen to maximize the same quantity (12.14) or, equivalently, to maximize

$$
\prod _ { j = 0 } ^ { n - 1 } | x _ { j } - x _ { n } | .
$$

All three of these families of points can be shown, under reasonable assumptions, to converge to the equilibrium measure as $n \to \infty$ , and all work well in practice for interpolation. A result showing near-optimality of Leja points for interpolation on general sets in the complex plane can be found in [Taylor $\&$ Totik 2010].

In Chapter 8 we proved a precise theorem (Theorem 8.2): if $f$ is analytic and bounded by $M$ in the Bernstein ellipse $E _ { \rho }$ , then $\| f - p _ { n } \| \leq 4 M \rho ^ { - n } / ( \rho - 1 )$ , where $p _ { n } \in \mathcal { P } _ { n }$ is the interpolant in $n + 1$ Chebyshev points. The proof made use of the Chebyshev expansion of $f$ and the aliasing properties of Chebyshev polynomials at

Chebyshev points. By the methods of potential theory and the Hermite integral formula discussed in this chapter one can derive a much more general theorem to similar effect. For any set of $n + 1$ nodes in $\lfloor - 1 , 1 \rfloor$ , let $\ell \in \mathcal P _ { n + 1 }$ be the node polynomial (5.4), and let $\begin{array} { r } { M _ { n } = \operatorname* { s u p } _ { x \in [ - 1 , 1 ] } | \ell ( x ) | } \end{array}$ . A sequence of grids of $1 , 2 , 3 , \ldots$ interpolation nodes is said to be uniformly distributed on $[ - 1 , 1 ]$ if it satisfies

$$
\operatorname* { l i m } _ { n  \infty } M _ { n } ^ { 1 / n } = \frac { 1 } { 2 } .
$$

(On a general set $E$ , the number $1 / 2$ becomes the capacity.)

Theorem 12.1. Interpolation in uniformly distributed points. Given $f \in C ( [ - 1 , 1 ] )$ , let $\rho$ ( $1 \le \rho \le \infty$ ) be the parameter of the largest Bernstein ellipse $E _ { \rho }$ to which $f$ can be analytically continued, and let $\{ p _ { n } \}$ be the interpolants to $f$ in any sequence of grids in $[ - 1 , 1 ]$ uniformly distributed as defined above. Then the errors satisfy

$$
\operatorname* { l i m } _ { n \to \infty } \| f - p _ { n } \| ^ { 1 / n } = \rho ^ { - 1 } .
$$

Proof. See Chapter 2 of [Gaier 1987].

A set of polynomials satisfying (12.16) is said to be maximally convergent. Examples of such polynomials are interpolants through most systems of roots or extrema of Legendre, Chebyshev, or Gauss–Jacobi points; the convergence rates of such systems differ only at the margins, in possible algebraic factors like $n$ or $\log n$ .

Summary of Chapter 12. Potential theory provides a powerful tool for studying the behavior of polynomial approximations in the limit $n  \infty$ . Polynomial interpolants to analytic functions on $[ - 1 , 1 ]$ converge geometrically if the grids are uniformly distributed according to the Chebyshev distribution.

Exercise 12.1. Fekete points in an interval. It can be shown that the equilibrium configuration for $n + 1$ points in $[ - 1 , 1 ]$ consists of the roots of $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ , where $P _ { n - 1 } ^ { ( 1 , 1 ) }$ is the degree $n - 1$ Jacobi polynomial with parameters $( 1 , 1 )$ [Stieltjes 1885] (see Chapter 17). (An equivalent statement is that the points lie at the local extrema in $[ - 1 , 1 ]$ of the Legendre polynomial of degree $n + 1$ .) Thus $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ is the degree $n - 1$ Fekete polynomial in $[ - 1 , 1 ]$ . Verify numerically using the Chebfun jacpts command that in the case $n = 1 0$ , the net forces on the 9 interior points are zero.

Exercise 12.2. Capacity of an ellipse. Let $E$ be an ellipse in the complex plane of semiaxis lengths $a$ and $^ { b }$ . Show that $c ( E ) = ( a + b ) / 2$ .

Exercise 12.3. Leja points and capacity. Let $E$ be the “half-moon” set consisting of the boundary of the right half of the unit disk. Write a code to compute a sequence of 100 Leja points for this set. To keep things simple, begin by approximating the boundary by a discrete set of 1000 points. What approximation of the capacity of $E$ do your points provide? (The exact answer is $4 / 3 ^ { 3 / 2 }$ , as discussed with other examples and algorithms in [Ransford 2010].)

# Chapter 13. Equispaced Points, Runge Phenomenon

So far in this book, we have considered three good methods for approximating functions by polynomials: Chebyshev interpolation, Chebyshev projection, and best approximation. Now we shall look at a catastrophically bad method!—interpolation in equally spaced points. This procedure is so unreliable that, for generations, it has tainted people’s views of the whole subject of polynomial interpolation. The mathematical tools we will need to understand what is going on are the Hermite integral formula and potential theory, as discussed in the last two chapters.

As mentioned in Chapter 5, polynomial interpolation was an established tool by the 19th century. The question of whether polynomial interpolants would converge to an underlying function as $n  \infty$ was not given much attention. Presumably many mathematicians would have supposed that if the function was analytic, the answer would be yes. In 1884 and 1896, M´eray published a pair of papers in which he identified the fact that certain interpolation schemes do not converge [M´eray 1884 & 1896]. In the first paper he writes

It is rather astonishing that practical applications have not yet turned up any cases in which the interpolation is illusory.6

M´eray’s derivations had the key idea of using the Hermite integral formula. However, the examples he devised were rather contrived, and his idiosyncratically written papers had little impact. It was Runge in 1901 who made the possibility of divergence famous by showing that divergence of interpolants occurs in general even for equispaced points in a real interval and evaluation points in the interior of that interval [Runge 1901].

Runge illustrated his discovery with an example that has become known as the Runge function: $1 / ( 1 + x ^ { 2 } )$ on $[ - 5 , 5 ]$ or, equivalently, $1 / ( 1 + 2 5 x ^ { 2 } )$ on $[ - 1 , 1 ]$ :

We already know from Chapter 8 that there is nothing wrong with this function for polynomial interpolation in Chebyshev points: $f$ is analytic, and the polynomial interpolants converge geometrically. Now, however, let us follow Runge and look at interpolants in equally spaced points, which we can compute using the Chebfun overload of the MATLAB interp1 command.

Here is what we get with 8 points:

s = linspace(-1,1,8); $\mathrm { ~ p ~ } =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](images/220391880c7937795d2a9af13b48ce80b6fa12e0d2e8136eeb3914781a7ef305.jpg)

Here is the result for 16 points:

s = linspace(-1,1,16); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](images/272777894d27087f9e71a2990d29c2cf75494c5ceeda3cb53c0548f33b6447c4.jpg)

Is this going to converge as $n \to \infty$ ? Things look pretty good in the middle but not so good at the edges. Here is the result for 20 points:

s = linspace(-1,1,20); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](images/9c9ccb320d97d2b57b1ec070a2ef7573c0bc77d622225af921e473a48166ef48.jpg)

What is happening is exponential convergence in the middle of the interval but exponential divergence near the ends. The next figure shows the maximum error over $[ - 1 , 1 ]$ as a function of the number of points. We get a hint of convergence at first, but after $n = 1 0$ , things just get worse. Note the log scale.

f $\begin{array} { r l } & { \mathsf { e } ~ = ~ \left[ \mathsf { J } \right] ; ~ \mathrm { n n } ~ = ~ 2 { : 2 : 5 0 } ; } \\ & { \mathsf { o r } ~ \mathrm { n p } ~ = ~ \mathrm { n n } } \\ & { ~ \mathsf { s } ~ = ~ \mathrm { 1 i n s p a c e } ( - 1 , 1 , \mathrm { n p } ) ; ~ \mathsf { p } ~ = ~ \mathrm { c h e b f u n . i n t e r p 1 } ( \mathsf { s } , \mathsf { f } ) ; } \\ & { \mathsf { e e } ~ = ~ \left[ \mathsf { e e } ~ \mathrm { n o r m } ( \mathsf { f } \mathrm { - p } , \mathrm { i n f } ) \right] ; } \end{array}$   
end   
semilogy(nn,ee,'.-')

![](images/7b0de94fd102b98c6ad7e5f80670335e81c7c370a08e420e707bdfb4f86efd8e.jpg)

By now the reader may have suspected that what is going wrong here can be understood by looking at potentials, as in the last two chapters. Here is an adaptation of a code segment from Chapter 11 to plot equipotential curves for $n + 1 = 8$ and 20.

d = domain([-1.5,1.5]);   
xgrid $=$ -1.5:.02:1.5; ygrid $=$ -1:.02:1;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
for np $=$ [8 20] xj $=$ linspace(-1,1,np); ell $=$ poly(xj,d); plot(xj,ell(xj),'.k') hold on, ellzz $=$ ell(zz); levels $=$ ((1.25:.25:3)/exp(1)).^np; contour(xx,yy,abs(ellzz),levels,'k')   
end

![](images/3742bbf26473d69b848b293749f91a2c79ff984b9790bb0715ec8cfeb35e8ac7.jpg)  
Level curves of $\| ( { \boldsymbol { \mathsf { x } } } ) \|$ for 8 equispaced points

What we see here is that $[ - 1 , 1 ]$ is very far from being a level curve for equispaced interpolation points. From the last two chapters, we expect serious consequences of this irregularity. In the second plot just shown, for example, it is the fourth curve (from inside out) that approximately touches the endpoints $\pm 1$ . For Theorem 11.1 to be of any use in such a landscape, $f$ will have to be analytic in a region larger than the “football” enclosed by that curve. Analyticity on $[ - 1 , 1 ]$ is not enough for convergence; we will need analyticity in a much bigger region of the complex plane. This is what Runge discovered in 1901.

Following the method of the last chapter, we now consider the limit $n  \infty$ , where the distribution of interpolation points approaches the constant measure (12.9),

$$
\mu ( \tau ) = \frac { 1 } { 2 } .
$$

The potential (12.7) associated with this measure is

$$
u ( s ) = - 1 + { \frac { 1 } { 2 } } \mathrm { R e } \left[ ( s + 1 ) \log ( s + 1 ) - ( s - 1 ) \log ( s - 1 ) \right] .
$$

Here is a code that plots just one level curve of this potential, the one passing through $\pm 1$ , where the value of the potential is $- 1 + \log 2$ .

$\begin{array} { r l } & { \mathrm { x 1 ~ = ~ - 1 . 6 5 : ~ } . 0 2 : 1 . 6 5 ; \mathrm { y 1 ~ = ~ - 0 . 7 : ~ } . 0 2 : 0 . 7 ; } \\ & { \mathrm { [ x x , y y ] ~ = ~ m e s h g r i d } ( \mathrm { x 1 } , \mathrm { y 1 } ) ; \mathrm { s s ~ = ~ x x + 1 i * y y ; } } \\ & { \mathrm { u ~ = ~ } \varnothing ( \mathtt { s } ) - 1 + 0 . 5 * \mathrm { r e a l } ( ( \mathtt { s } + 1 ) . * \mathrm { l o g } ( \mathtt { s } + 1 ) - ( \mathtt { s } - 1 ) . * \mathrm { l o g } ( \mathtt { s } - 1 ) ) ; } \\ & { \mathrm { c o n t o u r } ( \mathrm { x 1 } , \mathrm { y 1 } , \mathrm { u } ( \mathtt { s } \mathtt { s } ) , ( - 1 + \mathrm { l o g } ( 2 ) ) * [ 1 \ 1 ] , \mathrm { \xi } ^ { \mathrm { , ~ } } \mathrm { k } ^ { \prime } ) } \end{array}$ hold on, plot(.5255i,'.k')

![](images/d5b237d98f9f8c9cc5858e8678ca2e39b45fc99a482b8bada4b7addf7223900b.jpg)

For the interpolants to a function $f$ in equispaced nodes to converge as $n \to \infty$ for all $x \in [ - 1 , 1 ]$ , $f$ must be analytic, not just on $[ - 1 , 1 ]$ but throughout this Runge region, which crosses the real axis at $\pm 1$ and the imaginary axis at $\pm 0 . 5 2 5 5 2 4 9 1 4 5 7 \ldots i$ . Runge reports this number correctly to 4 digits and writes

The curve has somewhat the shape of an ellipse. At the ends of the long axis, however, our curve is more pointed than an ellipse.7

Here are the values of (13.2) at the endpoints and the middle:

$$
u ( \pm 1 ) = - 1 + \log 2 , \quad u ( 0 ) = - 1 ;
$$

thus

$$
\exp ( u ( \pm 1 ) ) = \frac { 2 } { e } , \quad \exp ( u ( 0 ) ) = \frac { 1 } { e } .
$$

These numbers indicate that in the limit $n  \infty$ , the endpoints of an equispaced grid in $[ - 1 , 1 ]$ lie at an average distance $2 / e$ from the other grid points, in the geometric mean sense, whereas the midpoint lies at an average distance of just $1 / e$ . As emphasized in the last chapter, notably in (12.6), the effect of such a discrepancy grows exponentially with $n$ .

Here are some examples. Equispaced interpolation will converge (in the absence of rounding errors) throughout $[ - 1 , 1 ]$ for $f ( x ) = \exp ( - x ^ { 2 } )$ , which is analytic everywhere, and for $f ( x ) = ( 1 + x ^ { 2 } ) ^ { - 1 }$ , which has poles at $\pm i$ . On the other hand, it will not converge for $f ( x ) = ( 1 + 1 6 x ^ { 2 } ) ^ { - 1 }$ , which has poles at $\pm i / 4$ . It will converge slowly for $f ( x ) = ( 1 + ( x / 0 . 5 3 ) ^ { 2 } ) ^ { - 1 }$ and diverge slowly for $f ( x ) = ( 1 + ( x / 0 . 5 2 ) ^ { 2 } ) ^ { - 1 }$ (Exercise 13.3).

The worst-case rate of divergence is $2 ^ { n }$ , and this rate will generally appear if $f$ is not analytic on $[ - 1 , 1 ]$ . To be precise, for such a function the errors will be of size $O ( 2 ^ { n } )$ as $n \to \infty$ but not of size $O ( C ^ { n } )$ for any $C < 2$ . Here, for example, we take $f$ to be a hat function, with just one derivative of bounded variation. The dots show errors in Chebyshev interpolation, converging at the rate $O ( n ^ { - 1 } )$ in keeping with Theorem 7.2, and the crosses show errors in equispaced interpolation, with a dashed line parallel to $2 ^ { n }$ for comparison.

pequi $=$ chebfun.interp1(s,f); eequi $=$ [eequi norm(f-pequi,inf)]; pcheb $=$ chebfun(f, $\tt { n } { + } 1$ ); echeb $=$ [echeb norm(f-pcheb,inf)]; end semilogy(nn,2.^(nn-12),'--r'), hold on semilogy(nn,eequi,'x-r'), semilogy(nn,echeb,'.-b')

![](images/1cd234b3c0d20801cabea992bcbeb832a43c65b31b0f5d428fad9289ebf4d9fb.jpg)

All of the above remarks about equispaced interpolation concern the ideal mathematics of the problem. On a computer in floating point arithmetic, however, a further complication arises: even if convergence ought to take place in theory, rounding errors will be amplified by $O ( 2 ^ { n } )$ , causing divergence in practice. Here, for example, are the errors in equispaced and Chebyshev interpolation of the entire function $\exp ( x )$ :

${ \textbf { f } } = \exp \left( \mathbf { x } \right)$ ; eequi $=$ []; echeb $=$ []; nn = 2:2:80;   
for $\texttt { n } = \texttt { n n }$ s $=$ linspace(-1,1,n+1); pequi $=$ chebfun.interp1(s,f); eequi $=$ [eequi norm(f-pequi,inf)]; pcheb $=$ chebfun(f, $\ n { + } 1 $ ); echeb $=$ [echeb norm(f-pcheb,inf)];   
end   
semilogy $\left( \operatorname { n n } , 2 . { \hat { \mathbf { \phi } } } ( \operatorname { n n - 5 0 } ) , \mathbf { \mu } ^ { * } - \mathbf { - r } \mathbf { \mu } ^ { * } \right)$ , hold on   
semilogy(nn,eequi, $\mathbf { \partial } ^ { \prime } \mathbf { x } \mathbf { - } \mathbf { r } ^ { \prime } \mathbf { \partial } .$ ), semilogy(nn,echeb,'.-b')

![](images/4d86eea9a01b201af78e3728e92ab79faf74d1ad29b4d948372bcae93131ed96.jpg)

In exact arithmetic we would see convergence for both sets of points, but on the computer the divergence for equispaced points sets in early. The rate is cleanly $O ( 2 ^ { n } )$ until we reach $O ( 1 )$ . Notice that the line of crosses, if extended backward to $n = 0$ , meets the $y$ -axis at approximately $1 0 ^ { - 1 8 }$ , i.e., a digit or two below machine precision.

The $2 ^ { n }$ divergence of equispaced polynomial interpolants is a fascinating subject, and we must remind ourselves that one should only go into so much detail in analyzing a method that should never be used! But perhaps we should qualify that “never” in one respect. As Runge himself emphasized, though interpolants in equispaced points do not converge on the whole interval of interpolation, they may still do very well near the middle. In the numerical solution of differential equations, for example, higher-order centered difference formulas are successfully used based on 5 or 7 equally spaced grid points. A less happy example would be Newton–Cotes quadrature formulas, based on polynomial interpolation in equally spaced points, where the $O ( 2 ^ { n } )$ effect is unavoidable and causes serious problems for larger $n$ and divergence as $n \to \infty$ , as first proved by P´olya [1933]. We shall discuss quadrature in Chapter 19.

We close this chapter with an observation that highlights the fundamental nature of the Runge phenomenon and its associated mathematics. Suppose you want to persuade somebody that it is important to know something about complex variables, even for dealing with real functions. I still remember the argument my calculus teacher explained to me: to understand why the Taylor series for $1 / ( 1 + x ^ { 2 } )$ converges only for $- 1 < x < 1$ , you need to know that Taylor series converge within disks in the complex plane, and that this function has poles at $\pm i$ .

Runge’s observation is precisely a generalization of this fact to interpolation points equispaced in an interval rather than all at $x \ = \ 0$ . The convergence or divergence of polynomial interpolants to a function $f$ again depends on whether $f$ is analytic in a certain region; the change is that the region is now not a disk but elongated. Even the phenomenon of divergence in floating point arithmetic for functions whose interpolants “ought” to converge is a generalization of familiar facts from real arithmetic. Just try to evaluate $\exp ( x )$ on a computer for $x = - 2 0$ using the Taylor series!

Summary of Chapter 13. Polynomial interpolation in equispaced points is exponentially ill-conditioned: the interpolant $p _ { n }$ may have oscillations near the edge of the interval nearly $2 ^ { n }$ times larger than the function $f$ being interpolated, even if $f$ is analytic. In particular, even if $f$ is analytic and the interpolant is computed exactly without rounding errors, $p _ { n }$ need not converge to $f$ as $n \to \infty$ .

Exercise 13.1. Three examples. Draw plots comparing accuracy of equispaced and Chebyshev interpolants as functions of $n$ for $\exp ( x ^ { 2 } )$ , $\exp ( - x ^ { 2 } )$ , $\exp ( - 1 / x ^ { 2 } )$ .

Exercise 13.2. Computing geometric means in Chebfun. (a) What output is produced by the program below? (b) Why?

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x',[0 1]);   
f $=$ chebfun(@(y) prod(abs(x-1i\*y)),[0.1 1]); roots(f-2/exp(1))

Exercise 13.3. Borderline convergence. The claim was made in the text that equispaced polynomial interpolants on $[ - 1 , 1 ]$ converge for $f ( x ) = ( 1 + ( x / 0 . 5 3 ) ^ { 2 } ) ^ { - 1 }$ and diverge for $f ( x ) = ( 1 + ( x / 0 . 5 2 ) ^ { 2 } ) ^ { - 1 }$ . Can you observe this difference numerically? Run appropriate experiments and discuss the results.

Exercise 13.4. Approaching the sinc function. The sinc function is defined for all $_ x$ by $S ( x ) = \sin ( \pi x ) / ( \pi x )$ (and $S ( 0 ) = 1$ ). For any $n \geq 1$ , an approximation to $S$ is given

by

$$
S _ { n } = \prod _ { k = 1 } ^ { n } ( 1 - x ^ { 2 } / k ^ { 2 } ) .
$$

Construct $S _ { 2 0 }$ in Chebfun on the interval $[ - 2 0 , 2 0 ]$ and compare it with $S$ . On what interval around $x = 0$ do you find $| S _ { 2 0 } ( x ) - S ( x ) | < 0 . 1 ?$ (It can be shown that for every $_ x$ , $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } S _ { n } ( x ) = S ( x ) } \end{array}$ .)

Exercise 13.5. Barycentric weights and ill-conditioning. (a) Suppose a function is interpolated by a polynomial in $n + 1$ equispaced points in $[ - 1 , 1 ]$ , with $n$ even. From the result of Exercise 5.6, derive a formula for the ratio of the barycentric weights at the midpoint $x = 0$ and the endpoint $x = 1$ . (b) With reference to the barycentric formula (5.11), explain what this implies about sensitivity of these polynomial interpolants to perturbations in the data at $x = 0$ .

# Chapter 14. Discussion of High-Order Interpolation

As mentioned at various points in this book, high-order polynomial interpolation has a bad reputation. For equispaced points this is entirely appropriate, as shown in the last chapter, but for Chebyshev points it is entirely inappropriate. Here are some illustrative quotes from 50 years of numerical analysis textbooks, which we present anonymously.

We cannot rely on a polynomial to be a good approximation if exact matching at the sample points is the criterion used to select the polynomial. The explanation of this phenomenon is, of course, that the derivatives grow too rapidly. (1962)

However, for certain functions the approximate representation of $f ( x )$ by a single polynomial throughout the interval is not satisfactory. (1972)

But there are many functions which are not at all suited for approximation by a single polynomial in the entire interval which is of interest. (1974)

Polynomial interpolation has drawbacks in addition to those of global convergence. The determination and evaluation of interpolating polynomials of high degree can be too time-consuming for certain applications. Polynomials of high degree can also lead to difficult problems associated with roundoff error. (1977)

We end this section with two brief warnings, one against trusting the interpolating polynomial outside [the interval] and one against expecting too much of polynomial interpolation inside [the interval]. (1980)

Although Lagrangian interpolation is sometimes useful in theoretical investigations, it is rarely used in practical computations. (1985)

Polynomial interpolants rarely converge to a general continuous function. Polynomial interpolation is a bad idea. (1989)

While theoretically important, Lagrange’s formula is, in general, not as suitable for actual calculations as some other methods to be described below, particularly for large numbers $n$ of support points. (1993)

Unfortunately, there are functions for which interpolation at the Chebyshev points fails to converge. Moreover, better approximations of functions like $1 / ( 1 + x ^ { 2 } )$ can be obtained by other interpolants—e.g., cubic splines. (1996)

In this section we consider examples which warn us of the limitations of using interpolation polynomials as approximations to functions. (1996)

Increasing the number of interpolation points, i.e., increasing the degree of the polynomials, does not always lead to an improvement in the approximation. The spline interpolation that we will study in this section remedies this deficiency. (1998)

The surprising state of affairs is that for most continuous functions, the quantity $\| f - p _ { n } \| _ { \infty }$ will not converge to 0. (2002)

Because its derivative has $n - 1$ zeros, a polynomial of degree n has $n - 1$ extreme or inflection points. Thus, simply put, a high-degree polynomial necessarily has many “wiggles,” which may bear no relation to the data to be fit. (2002)

By their very nature, polynomials of a very high degree do not constitute reasonable models for real-life phenomena, from the approximation and from the handling pointof-view. (2004)

The oscillatory nature of high degree polynomials, and the property that a fluctuation over a small portion of the interval can induce large fluctuations over the entire range, restricts their use. (2005)

In addition to the inherent instability of Lagrange interpolation for large $_ { n }$ , there are also classes of functions that are not suitable for approximation by certain types of interpolation. There is a celebrated example of Runge. . . . (2011)

A great deal of confusion underlies remarks like these. Some of them are literally true, but they are all misleading. In fact, polynomial interpolants in Chebyshev points are problem-free when evaluated by the barycentric interpolation formula. They have the same behavior as discrete Fourier series for periodic functions, whose reliability nobody worries about. The introduction of splines is a red herring: the true advantage of splines is not that they converge where polynomials fail to do so, but that they are more easily adapted to irregular point distributions and more localized, giving errors that decay exponentially rather than just algebraically away from singularities (Exercise 9.8).

It is interesting to speculate as to how the distrust of high-degree polynomials became so firmly established. I think the crucial circumstance is that not one but several combined problems affect certain computations with polynomials, a situation complex enough to have obscured the truth from easy elucidation. If working with polynomials had been the central task of scientific computing, the truth would have been worked out nonetheless, but over the years there were always bigger problems pressing upon the attention of numerical analysts, like matrix computations and differential equations. Polynomial computations were always a sideline.

At the most fundamental level there are the two issues of conditioning and stability—both crucial, and not the same. See [Trefethen & Bau 1997] for a general

discussion of conditioning and stability.

(1) Conditioning of the problem. The interpolation points must be properly spaced (e.g., Chebyshev or Legendre) for the interpolation problem to be wellconditioned. This means that the interpolant should not depend too sensitively on the data. The Runge phenomenon for equally spaced points is the well-known consequence of extreme ill-conditioning, with sensitivities of order $2 ^ { n }$ . The next chapter makes such statements precise through the use of Lebesgue constants.

(2) Stability of the algorithm. The interpolation algorithm must be stable (e.g., the barycentric interpolation formula) for a computation to be accurate, even when the problem is well-conditioned. This means that in the presence of rounding errors, the computed solution should be close to an exact solution for some interpolation data close to the exact data. In particular, the best-known algorithm of all, namely the “polyval/polyfit” algorithm of solving a Vandermonde linear system of equations to find the coefficients of the interpolant expressed as a linear combination of monomials, is explosively unstable, relying on a matrix whose condition number grows exponentially with the dimension (Exercise 5.2).

These facts would be enough to explain a good deal of confusion, but another consideration has muddied the water further, namely crosstalk with the notoriously troublesome problem of finding roots of a polynomial from its coefficients (to be discussed in Chapter 18). The difficulties of polynomial rootfinding were widely publicized by Wilkinson beginning in the 1950s, who later wrote an article called “The perfidious polynomial” that won the Chauvenet Prize of the Mathematical Association of America [Wilkinson 1984]. Undoubtedly this negative publicity further discouraged people from the use of polynomials, even though interpolation and rootfinding are different problems. They are related, with related widespread misconceptions about accuracy: just as interpolation on an interval is trouble-free for a stable algorithm based on Chebyshev points, rootfinding on an interval is troublefree for a stable algorithm based on expansions in Chebyshev polynomials (Chapter 18). But very few textbooks tell readers these facts.

Summary of Chapter 14. Generations of numerical analysis textbooks have warned readers that polynomial interpolation is dangerous. In fact, if the interpolation points are clustered and a stable algorithm is used, it is bulletproof.

Exercise 14.1. Convergence as $n  \infty$ . The 1998 quote asserts that increasing $n$ “does not always lead to an improvement.” Based on the theorems of this book, for interpolation in Chebyshev points, for which functions $f$ do we know that increasing $n$ must lead to an improvement?

Exercise 14.2. Too many wiggles. Using the Chebfun roots(f,'all') option, plot all the roots in the complex plane of the derivative of the chebfun corresponding to $f ( x ) =$ $\exp ( x ) \operatorname { t a n h } ( 2 x - 1 )$ on $[ - 1 , 1 ]$ . What is the error in the argument in the second 2002 quote used to show that “a high-degree polynomial necessarily has many wiggles”? (We shall return to this phenomenon in the discussion of the theorems of Walsh and of Blatt and Saff at the end of Chapter 18.)

Exercise 14.3. Your own textbook. Find a textbook of numerical analysis and examine its treatment of polynomial interpolation. (a) What does it say about behavior for large $_ n$ ? If it asserts that this behavior is problematic, is this conclusion based on the assumption of equally spaced points, and does the text make this clear? (b) Does it mention interpolation in Chebyshev points? Does it state that such interpolants converge exponentially for analytic functions? (c) Does it mention the barycentric formula? (d) Does it claim that one should use a Newton rather than a Lagrange interpolation formula for numerical work? (This is a myth.)

Exercise 14.4. Spline interpolants. (a) Use the Chebfun spline command to interpolate $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ by a cubic spline in $n + 1$ equally spaced points on $[ - 1 , 1 ]$ . Compare the $\infty$ -norm error as $n \to \infty$ with that of polynomial interpolation in Chebyshev points. (b) Same problem for $f ( x ) = | x + 1 / \pi |$ . (c) Same problem for $f ( x ) = | x + 1 / \pi |$ , but measuring the error by the $\infty$ -norm over the interval [0, 1]. (Compare Exercise 9.8.)

# Chapter 15. Lebesgue Constants

There is a well-developed theory that quantifies the convergence or divergence of polynomial interpolants. A key notion is that of the Lebesgue constant, $\Lambda$ , for interpolation in a given set of points. The Lebesgue constant is the $\infty$ -norm of the linear mapping from data to interpolant:

$$
\Lambda = \operatorname* { s u p } _ { f } { \frac { \| p \| } { \| f \| } } ,
$$

where $\| \cdot \|$ denotes the $\infty$ -norm in $C ( [ - 1 , 1 ] )$ . In words, if you have data values on an $( n + 1 )$ -point grid, and the data come from sampling a function that is no greater than $^ { 1 }$ in absolute value, what is the largest possible value of the interpolant $p$ somewhere in $[ - 1 , 1 ]$ ?

In the plots of Chapter 13 for interpolation of Runge’s function, for example, we saw that the interpolants grew much bigger than the data. Thus the Lebesgue constants must be large for equispaced interpolation. For example, for $n = 5 0$ , the data are bounded by 1 for all $n$ , yet the interpolant is bigger than $1 0 ^ { 5 }$ . Thus the Lebesgue constant for interpolation in 50 equispaced points must be greater than $1 0 ^ { 5 }$ . (In fact, it is about $4 . 2 \times 1 0 ^ { 1 2 }$ .)

From the basic Lagrange formula (5.1) for polynomial interpolation,

$$
p ( x ) = \sum _ { j = 0 } ^ { n } f _ { j } \ell _ { j } ( x ) ,
$$

we can get a formula for $\Lambda$ in terms of the Lagrange polynomials $\{ \ell _ { j } \}$ . At any point $x \in [ - 1 , 1 ]$ , the maximum possible value of $| p ( x ) |$ for grid data bounded by $1$ in absolute value will be the number $\lambda ( x )$ obtained if each data value is $\pm 1$ , with signs

chosen to make all the signs at $x$ coincide:

$$
\lambda ( x ) = \sum _ { j = 0 } ^ { n } | \ell _ { j } ( x ) | .
$$

This sum of absolute values is known as the Lebesgue function for the given grid, and the Lebesgue constant is equal to its maximum value,

$$
\Lambda = \operatorname* { s u p } _ { x \in [ - 1 , 1 ] } \lambda ( x ) .
$$

The reason Lebesgue constants are interesting is that interpolants are guaranteed to be good if and only if the Lebesgue constants are small. We can make this statement precise as follows. Let $\Lambda$ be the Lebesgue constant for interpolation in a certain set of points. Without loss of generality (since the interpolation process is linear), suppose the largest absolute value of the samples is 1. If $p$ is the interpolant in these points to a function $f$ , we know that $\| p \|$ might be as great as $\Lambda$ ; yet $\| f \|$ might be as small as 1. Thus $\| f - p \|$ might be as great as $\Lambda - 1$ , showing that a large Lebesgue constant rigorously implies the possibility of a large interpolation error.

Conversely, let $p ^ { * }$ be the best degree $n$ polynomial approximation to $f$ in the $\infty$ -norm. If $p$ is the polynomial interpolant to $f$ in the given points, then $p - p ^ { * }$ is the polynomial interpolant to $f - p ^ { * }$ . By the definition of the Lebesgue constant, $\| p - p ^ { * } \|$ is no greater than $\Lambda \| f - p ^ { * } \|$ . Since $f - p = ( f - p ^ { * } ) - ( p - p ^ { * } )$ , this implies that $\| f - p \|$ is no greater than $( \Lambda + 1 ) \| f - p ^ { * } \|$ . Thus a small Lebesgue constant implies that interpolation will be close to best.

Actually, the discussion of the last two paragraphs is not limited to interpolation. What is really in play here is any approximation process that is a linear projection from $C ( [ - 1 , 1 ] )$ to $\mathcal { P } _ { n }$ , of which Chebyshev projection (truncation of the Chebyshev series) would be an example as well as interpolation. Suppose we let $L$ denote an operator that maps functions $f \in C ( [ - 1 , 1 ] )$ to approximations by polynomials $p \in \mathcal { P } _ { n }$ . For $L$ to be linear means that $L ( f _ { 1 } + f _ { 2 } ) = L f _ { 1 } + L f _ { 2 }$ for any $f _ { 1 } , f _ { 2 } \in$ $C ( [ - 1 , 1 ] )$ and $L ( \alpha f ) = \alpha L f$ for any scalar $\alpha$ , and for $L$ to be a projection means that if $p \in \mathcal { P } _ { n }$ , then $L p \ = \ p$ . By the argument above we have established the following result applicable to any linear projection.

Theorem 15.1. Near-best approximation and Lebesgue constants. Let $\Lambda$ (or $\Lambda _ { n }$ ) be the Lebesgue constant for a linear projection $L$ of $C ( [ - 1 , 1 ] )$ onto $\mathcal { P } _ { n }$ . Let $f$ be a function in $C ( [ - 1 , 1 ] )$ , $p = L f$ the corresponding polynomial approximant to $f$ , and $p ^ { * }$ the best approximation. Then

$$
\| f - p \| \leq ( \Lambda + 1 ) \| f - p ^ { * } \| .
$$

Proof. The proof is given in the paragraphs above.

So it all comes down to the question, How big is $\Lambda$ ? According to the theorem of Faber mentioned in Chapter 6 [Faber 1914], no sets of interpolation points can lead to convergence for all $f \in C ( [ - 1 , 1 ] )$ , so it follows from Theorems 6.1 and 15.1 that

$$
\operatorname* { l i m } _ { n \to \infty } \Lambda _ { n } = \infty
$$

for interpolation in any sets of points (Exercise 15.12). However, for well-chosen sets of points, the growth of $\Lambda _ { n }$ as $n  \infty$ may be exceedingly slow. Chebyshev points are nearly optimal, whereas equispaced points are very bad.

The following theorem summarizes a great deal of knowledge accumulated over the past century about interpolation processes. At the end of the chapter an analogous theorem is stated for Chebyshev projection. As always in this book, by “Chebyshev points” we mean Chebyshev points of the second kind, defined by (2.2).

Theorem 15.2. Lebesgue constants for polynomial interpolation. The Lebesgue constants $\Lambda _ { n }$ for degree $n \geq 0$ polynomial interpolation in any set of $n + 1$ distinct points in $[ - 1 , 1 ]$ satisfy

$$
\Lambda _ { n } \geq \frac { 2 } { \pi } \log ( n + 1 ) + 0 . 5 2 1 2 5 \ldots ;
$$

the number 0.52125 . . . is $( 2 / \pi ) ( \gamma + \log ( 4 / \pi ) )$ , where $\gamma \approx 0 . 5 7 7$ is Euler’s constant. For Chebyshev points, they satisfy

$$
\Lambda _ { n } \leq \frac { 2 } { \pi } \log ( n + 1 ) + 1 a n d \Lambda _ { n } \sim \frac { 2 } { \pi } \log n , n  \infty .
$$

For equispaced points they satisfy

$$
\Lambda _ { n } > \frac { 2 ^ { n - 2 } } { n ^ { 2 } } a n d \Lambda _ { n } \sim \frac { 2 ^ { n + 1 } } { e n \log n } , n  \infty ,
$$

with the inequality (15.9a) applying for $n \geq 1$ .

Proof. The fact that Lebesgue constants for polynomial interpolation always grow at least logarithmically goes back to Bernstein [1912b], Jackson [1913], and Faber [1914]. Bernstein knew that $( 2 / \pi ) \log n$ was the controlling asymptotic factor for interpolation in an interval, and the proof of (15.7) in this sharp form is due to Erd˝os [1961], who got a constant $C$ , and Brutman [1978], who improved the constant to 0.52125 . . . . Equation (15.8a) is a consequence of Theorem 4 of [Ehlich & Zeller 1966]; see also [Brutman 1997] and [McCabe & Phillips 1973]. Equation (15.8b) follows from this together with Erd˝os’s result. (Bernstein [1919] did the essential work, deriving this asymptotic result for Chebyshev points of the first kind, i.e., zeros of Chebyshev polynomials—see Exercise 15.2.) Equation (15.9b) is due to Turetskii [1940] and independently Sch¨onhage [1961], and for (15.9a) and a discussion of related work, see [Trefethen & Weideman 1991].

Equations (15.8) show that Lebesgue constants for Chebyshev points grow more slowly than any polynomial: for many practical purposes they might as well be 1. It is interesting to relate this bound to the interpolant through 100 random data points plotted on p. 10. The Lebesgue constant is the maximum amplitude this curve could possibly have attained, if the data had been as bad as possible. For 100 points this number is about 3.94. In the plot we see that random data have in fact come nowhere near even this modest limit.

On the other hand, equations (15.9) show that Lebesgue constants for equispaced points grow faster than any polynomial: for many practical purposes, unless $n$ is very small, they might as well be $\infty$ .

Taking advantage again of the interp1 command, as in Chapter 13, we can use Chebfun as a laboratory in which to see how such widely different Lebesgue constants emerge. Consider, for example, the case of four equally spaced points. Here are plots of the four Lagrange polynomials $\{ \ell _ { j } \}$ . In Chapter 9 we have already seen plots of Lagrange polynomials, but on a grid of 20 Chebyshev points instead of 4 equispaced points.

npts $\mathit { \Theta } = \mathit { \Theta } 4$ ; clear p, d = domain(-1,1); s = linspace(-1,1,4);   
for $\texttt { k } = \texttt { 1 }$ :npts subplot(2,2,k) $\textrm { y } =$ [zeros(1,k-1) 1 zeros(1,npts-k)]; p{k} $=$ interp1(s,y,d); plot(p{k}), hold on, plot(s,p{k}(s),'.') plot(s(k),p{k}(s(k)),'hr')   
end

![](images/c2485d98d1a80c2864b8a6cd8d05ec41a23975b5db921503a3b8ebf78d9f0312.jpg)

By taking the absolute values of these curves, we see the largest possible effect at each point in $[ - 1 , 1 ]$ of data that is nonzero at just one point of the grid:

for $\texttt { k } = \texttt { 1 }$ :npts subplot(2,2,k), absp $=$ abs(p{k}); plot(absp), hold on, plot(s,absp(s),'.') plot(s(k),absp(s(k)),'hr')   
end

![](images/f5113bb6133227a0e9fc82a6bf578a58b9ba4fd545535a2d67c1066c21f8186d.jpg)

Now let us add up these absolute values as in (15.3):

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); ${ \mathrm { ~ \cal ~ L ~ } } = { \mathrm { ~ 0 * x } }$ ; for k = 1:npts, $\mathrm { ~ L ~ } = \mathrm { ~ L ~ } +$ abs(p{k}); end plot(L), hold on, plot(s,L(s),'.')

![](images/d2748eece46b5b136215ab68be2ce0412085b849789dcfc188cf15a40251dcc0.jpg)

This is the Lebesgue function $\lambda ( x )$ , a piecewise polynomial, telling us the largest possible effect at each point $x \in [ - 1 , 1 ]$ of interpolating data of norm 1. The Lebesgue constant (15.4) is the height of the curve:

Lconst $=$ norm(L,inf)

Lconst $=$ 1.631130309440900

A code lebesgue for automating the above computation (actually based on a more efficient method) is included in Chebfun, and it optionally returns the Lebesgue constant as well as the Lebesgue function. Here are the results for 8 equispaced points:

s = linspace(-1,1,8); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 6.929739656126466

![](images/a708f71491e25c2aa7d3a3bffd7c7ba9f5579d6665b47c8495182bd2e9a4ba17.jpg)

And here they are for 12 points. Note that the Lebesgue constant has jumped from 7 to 51.

s = linspace(-1,1,12); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 51.214223185730020

![](images/1e48e6558849edde9bb798b139902543923504e308c74e4d2af78825dcfcc7a4.jpg)

The function takes large values near $\pm 1$ , as we expect from Chapter 13 since the Runge phenomenon is associated with interpolants becoming very large near the endpoints. In fact the Lebesgue function for interpolation in equispaced points is more naturally displayed on a log scale. Here it is for $n = 3 0$ :

s $=$ linspace(-1,1,30); [L,Lconst] $=$ lebesgue(s); semilogy(L), hold on, semilogy(s,L(s),'.'), Lconst

Lconst $=$ 3.447738672687561e+06

![](images/8a180e83159c55efa5e7b8158b8cc89d5676cd62f056c235516a2498b1683ef7.jpg)

For comparison, here are the corresponding results for 4, 8, and 12 Chebyshev points, now back again on a linear scale.

for npts $=$ 4:4:12 s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst   
end

Lconst $=$ 1.666666666666667   
Lconst $=$ 2.202214555205528   
Lconst $=$ 2.489430376881968

![](images/07d20a576c0d8356d0f243252221d479ad7b31319cffbf96a6449b16680fb8e7.jpg)

Here are 100 Chebyshev points, with a comparison of the actual Lebesgue constant with the bound from Theorem 15.2:

$\mathtt { n p t s } ~ = ~ 1 0 0$ ; s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), Lconst, Lbound $=$ 1 + (2/pi)\*log(npts)

Lconst $=$ 3.887871431579913   
Lbound $=$ 3.931742395517711

![](images/f4514cec933477f55fc1cf21c2cfc468af5d80ee5e0ff9c669eba4e15f452bfe.jpg)

The low height of this curve shows how stable Chebyshev interpolation is.

In Chapter 9 it was mentioned that combinations of Lagrange polynomials are the source of both the Gibbs phenomenon and the size of Lebesgue functions. Let us now explain this remark. To analyze the Gibbs oscillations near a step, we added up a succession of Lagrange polynomials with constant amplitude 1. Since a single Lagrange polynomial has an oscillatory inverse-linear tail, the sum corresponds to an alternating series that converges to a constant as $n \to \infty$ . Lebesgue functions, on the other hand, are defined by taking a maximum at each point on the grid. The maximum is achieved by adding up Lagrange polynomials with equal but alternating coefficients, so as to make the combined signs all equal. For example, on the 20- point Chebyshev grid, the maximum possible value of an interpolant is achieved at $x = 0$ by taking data with this pattern:

![](images/d3d42282ce745d2591889d8f130d63b6532a5d2a4437adc5c8f2bc84af934779.jpg)

Here is the Chebyshev interpolant:

p = chebfun(d); hold on, plot(p)

![](images/b6c51ce0a0064ec698268ec5fe3d212feaac408e92b60400fc14de94f8175ad9.jpg)

We readily confirm that the maximum of this interpolant is indeed the Lebesgue constant for this grid:

max(p), [L,Lconst] $=$ lebesgue(s); Lconst

ans $=$ 2.837131699740443   
Lconst $=$ 2.837131699740441

We can now summarize why Lebesgue constants for Chebyshev points, and indeed for any sets of interpolation points, must grow at least logarithmically with $n$ . The fastest a Lagrange polynomial can decay is inverse-linearly, and the Lebesgue function adds up those alternating tails with alternating coefficients, giving a harmonic series.

Our discussion in this chapter has focused on Chebyshev interpolation rather than projection. However, as usual, there are parallel results for projection, which historically were worked out earlier (for the Fourier case, not Chebyshev). We record here a theorem analogous to Theorem 15.2.

Theorem 15.3. Lebesgue constants for Chebyshev projection. The Lebesgue constants $\Lambda _ { n }$ for degree $n \geq 1$ Chebyshev projection in $[ - 1 , 1 ]$ are given by

$$
\Lambda _ { n } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left| \frac { \sin ( ( n + 1 / 2 ) t ) } { \sin ( t / 2 ) } \right| d t .
$$

They satisfy

$$
\Lambda _ { n } \leq { \frac { 4 } { \pi ^ { 2 } } } \log ( n + 1 ) + 3 a n d \Lambda _ { n } \sim { \frac { 4 } { \pi ^ { 2 } } } \log n , n  \infty .
$$

Proof. See [Rivlin 1981]. Equation (15.11b) is due to Fej´er [1910].

Related to Theorem 15.3 is another result concerning the norm of projection operators, proved by Landau [1913]. If $f$ is analytic in the unit disk and continuous on the boundary, and $p \in \mathcal { P } _ { n }$ is the Taylor projection of $f$ obtained by truncating its Taylor series, how much bigger can $p$ be than $f$ on the unit disk? Landau showed that these norms (now known as Landau constants) grow at a rate asymptotic to $( 1 / \pi ) \log n$ as $n \to \infty$ , a discovery that is perhaps the starting point of all results about logarithmic growth of norms of approximation operators.

For details about Lebesgue constants, an outstanding source is the survey article by Brutman [1997].

Though Lebesgue constants are a notion for linear approximation, the phenomenon of ill-conditioning that they quantify applies in nonlinear approximation too—see [Platte, Trefethen & Kuijlaars 2011].

Summary of Chapter 15. The Lebesgue constant for interpolation or any other linear projection is the $\infty$ -norm of the operator mapping the data to the approximant. For interpolation in $n + 1$ Chebyshev points, the Lebesgue constant is bounded by $1 + 2 \pi ^ { - 1 } \log ( n + 1 )$ , whereas for $n + 1$ equispaced points it is asymptotic to $2 ^ { n + 1 } / e n \log ( n )$ .

Exercise 15.1. Plots of Lebesgue functions. Plot the Lebesgue functions for the following distributions of interpolation points: (a) $- 0 . 9$ , $- 0 . 8$ , 0, 0.1, 0.2, 0.8; (b) same as in (a) but with additional points at a distance 0.01 to the right of the others.

Exercise 15.2. Chebyshev points of the first kind. The Lebesgue constant for interpolation in $n$ Chebyshev points is bounded by the Lebesgue constant for interpolation in $n { - } 1$ Chebyshev points of the first kind, introduced in Exercise 2.4 (see also help chebpts), with equality when $n$ is odd (Ehlich and Zeller [1966], McCabe and Phillips [1973]). Verify this numerically for $2 \leq n \leq 2 0$ .

Exercise 15.3. Reproducing a table by Brutman. Page 698 of [Brutman 1978] gives a table of various quantities associated with the Lebesgue function for interpolation in Chebyshev points of the first kind, mentioned in the last exercise. Track down this paper and write the shortest, most elegant Chebfun program you can to duplicate this table. Are all of Brutman’s digits correct?

Exercise 15.4. Omitting the endpoints. Suppose one performs polynomial interpolation in the usual Chebyshev points (2.2), but omitting the endpoints $x = \pm 1$ . Perform numerical experiments to determine what happens to the Lebesgue constants in this case. Does the growth appear to be of order $\log n$ , or $n ^ { \alpha }$ for some $\alpha$ , or what?

Exercise 15.5. Optimal interpolation points. Starting from the $n + 1$ Chebyshev points, one could attempt to use one of the MATLAB optimization codes to adjust the points to minimize the Lebesgue constant. Do this and give the Lebesgue constant and plot the Lebesgue function for (a) $n = 4$ , (b) $n = 5$ , (c) $n = 6$ , (d) $n = 7$ , and (e) $n = 8$ . How much improvement do you find in the Lebesgue constants as compared with Chebyshev points?

Exercise 15.6. Improving Turetskii’s estimate. For interpolation in equispaced points, Sch¨onhage [1961] derived a more accurate estimate than (15.9b): $\Lambda _ { n } ~ \sim$ $2 ^ { n + 1 } / e n ( \log n + \gamma )$ , where $\gamma = 0 . 5 7 7 \dots$ is again Euler’s constant. Perform a numerical study of $\Lambda _ { n }$ as a function of $n$ and see what difference this correction makes. For example, it might be helpful to make a table showing the percentage errors in both estimates as functions of $n$ .

Exercise 15.7. Interpolating data with a gap. (a) Consider polynomial interpolation in $n + 1$ points of a function $f$ defined on $[ - 1 , 1 ]$ , with half the points equally spaced from $^ { - 1 }$ to $- 1 / 4$ and the other half equally spaced from $1 / 4$ to 1. Determine the Lebesgue constants for this interpolation process numerically for the cases $n + 1 = 2 0$ and 40. (b) Suppose $f$ is analytic and bounded by 1 in the $\rho$ -ellipse $E _ { \rho }$ with $\rho = 2$ . Carefully quoting theorems from this book as appropriate, give upper bounds for the error $| f ( 0 ) - p ( 0 ) |$ for these two cases.

Exercise 15.8. Smallest local minimum of the Lebesgue function. Interpolation in equispaced points is much better near the middle of an interval than at the ends. In particular, the smallest local maximum of the Lebesgue function $\lambda$ is $\sim \log n / \pi$ as $n \to \infty$ [Tietze 1917]. Make a plot of these minima as a function of $n$ to verify this behavior numerically.

Exercise 15.9. Convergence for Weierstrass’s function. Exercise 7.3 promised that in Chapter 15 we would show that Chebyshev interpolants to Weierstrass’s nowheredifferentiable function of (6.1) converge as $n  \infty$ . Write down such a proof based on combining various theorems of this book.

Exercise 15.10. Random interpolation points. (a) Compute Lebesgue functions and constants numerically for degree $n$ interpolation in uniformly distributed random points in $[ - 1 , 1 ]$ . How does $\Lambda$ appear to grow with $n$ ? (b) The same question for points randomly distributed according to the Chebyshev density (11.18).

Exercise 15.11. A wiggly function. (a) Let $f$ be the function $T _ { m } ( x ) + T _ { m + 1 } ( x ) +$ $\cdots + T _ { n } ( x )$ with $m = 2 0$ and $n = 4 0$ , and let $p ^ { * }$ be the best approximation of $f$ of degree $m - 1$ . Plot $f$ and $f - p ^ { * }$ . What are their $\infty$ -norms and 2-norms? (b) The same questions with $m = 2 0 0$ and $n = 3 0 0$ .

Exercise 15.12. Divergence of Lebesgue constants. Spell out precisely the reasoning used to justify (15.6) in the text. In particular, make it clear why a “lim sup” rather than a “sup” appears in the formula.

Exercise 15.13. Confluent interpolation nodes. Let $\{ x _ { j } \}$ be a set of $n + 1$ distinct interpolation nodes in $[ - 1 , 1 ]$ . Now change $x _ { 0 }$ to $x _ { 1 } + \varepsilon$ , where $\varepsilon > 0$ is a parameter, and let $\Lambda ( \varepsilon )$ be the corresponding Lebesgue constant. Show that $\Lambda ( \varepsilon )$ diverges to $\infty$ as $\varepsilon  0$ . Can you quantify the rate of divergence?

# Chapter 16. Best and Near-Best

Traditionally, approximation theory has given a great deal of attention to best approximations in the $\infty$ -norm and rather less to alternatives such as Chebyshev interpolants. One might think that this is because best approximations are much better than the alternatives. However, this is not true.

In a moment we shall continue with Lebesgue constants to shed some light on this matter, but first, let us do some experiments. We start with the extreme case of a very smooth function, $\exp ( x )$ , and compare convergence of its Chebyshev interpolants $p$ and best approximants $p ^ { * }$ . (The difference between $n$ and $n { \mathrel { + { 1 } } }$ in this code is intentional, since chebfun takes as argument the number of interpolation points, whereas minimax takes the degree of the polynomial.)

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); nn = 0:15;   
errbest $=$ []; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\tt { n } { + } 1$ ),inf);   
end   
semilogy(nn,errcheb,'. $- \mathbf { r } ^ { \mathsf { \Pi } }$ ), hold on, semilogy(nn,errbest,'h-b')

![](images/dcbac3d9b6c7e7a7569f3845cfd830ce109c14ed6bb6c0ecfe1fd7215b78e87e.jpg)

Clearly the stars for $p ^ { * }$ aren’t much better than the dots for $p$ . The ratio of the two converges toward 2 until the rounding errors set in for larger degrees:

ratio $=$ errcheb./errbest; fprintf('%8d %12.5f\n',[nn; ratio])

<table><tr><td>n</td><td>ratio</td></tr><tr><td>0</td><td>1.46212</td></tr><tr><td>1</td><td>2.00000</td></tr><tr><td>2</td><td>1.74436</td></tr><tr><td>3</td><td>1.96807</td></tr><tr><td>4</td><td>1.94991</td></tr><tr><td>5</td><td>1.98188</td></tr><tr><td>6</td><td>1.98182</td></tr><tr><td>7</td><td>1.98861</td></tr><tr><td>8</td><td>1.99105</td></tr><tr><td>9</td><td>1.99222</td></tr><tr><td>10</td><td>1.99468</td></tr><tr><td>11</td><td>1.99259</td></tr><tr><td>12</td><td>1.97361</td></tr><tr><td>13</td><td>1.27028</td></tr><tr><td></td><td>0.25152</td></tr><tr><td>14</td><td></td></tr><tr><td>15</td><td>0.80000</td></tr></table>

At the other extreme of smoothness, consider $| x |$ :

f = abs(x); nn = [0 2 4 10 20 40 100 200];   
errbest $= ~ [ ]$ ; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\ n { + } 1 \cdot$ ),inf);   
end   
loglog( $\mathtt { n n } { + } 1$ ,errbest, $" \mathrm { h } - \mathrm { b } \cdot$ ) hold on, loglog( $\mathtt { n n } { + 1 }$ ,errcheb,'.-r')

![](images/4a49b5ad3fff42464dff32d93fc5afe678c9e3a9140d55230772055eaa3dd915.jpg)

Again the stars are only a little better than the dots, by a constant factor of about 2.1306:

ratio $=$ errcheb./errbest; fprintf('%8d %12.5f\n',[nn; ratio])

<table><tr><td>n</td><td>ratio</td></tr><tr><td>0</td><td>2.00000</td></tr><tr><td>2</td><td>2.00000</td></tr><tr><td>4</td><td>2.10234</td></tr><tr><td>10</td><td>2.12677</td></tr><tr><td>20</td><td>2.12968</td></tr><tr><td>40</td><td>2.13037</td></tr><tr><td>100</td><td>2.13056</td></tr><tr><td>200</td><td>2.13059</td></tr></table>

(For odd values of $n$ the ratio is somewhat larger, approaching a constant of about 3.57.)

So for these examples at least, you don’t buy much with best approximations. And the cost in computing time is considerable. Here is the time for computing a Chebyshev interpolant $p$ of degree 200 and evaluating it at 100 points:

xx = rand(100,1); tic, p = chebfun(f,201); p(xx); toc

Elapsed time is 0.019866 seconds.

Here is the time for finding the best approximation $p ^ { * }$ and evaluating it at the same points:

tic, p = minimax(f,200); p(xx); toc

Elapsed time is 0.284064 seconds.

The reason computing $p ^ { * }$ is more difficult is that the mapping from $f$ to $p ^ { * }$ is nonlinear, hence requiring iteration in a numerical implementation, whereas the mapping from $f$ to $p$ is linear (Exercise 10.6). It is perfectly feasible to compute $p$ for degrees in the millions, whereas for $p ^ { * }$ we would rarely attempt degrees higher than hundreds.

Why has $p ^ { * }$ received so much more attention than $p$ over the years? One reason is that in the days before fast computers, the degrees were low, so small differences in accuracy were more important. Another is that the theory of best approximations is so beautiful! Indeed, their very nonlinearity makes best approximations seemingly a richer field for research than the simpler Chebyshev interpolants. Everybody remembers Theorem 10.1, the equioscillation theorem, from the moment they first see it.

Yet in actual computation, true best approximations are not so often used, as we have mentioned earlier (Chapter 10). This is a clue that the world of practice may have its own wisdom, independent of the theorists.

Now let us see what theoretical results might tell us about the difference between $p$ and $p ^ { * }$ . The first such results pertain to Theorems 7.2 and 8.2 given earlier. Those theorems concerned convergence rates of $p _ { n }$ to $f$ , depending on the smoothness of $f$ . What about analogous theorems for $\boldsymbol { p } _ { n } ^ { * }$ ? Apart from constant factors, they turn out to be the same! For example, exactly the same bound (8.3) was published by de la Vall´ee Poussin [1919, pp. 123–124], except with the Chebyshev interpolant $p _ { n }$ replaced by the best approximation $\boldsymbol { p } _ { n } ^ { * }$ . So within the two classes of functions considered in Chapters 7 and 8— $f$ having a $k$ th derivative of bounded variation, or $f$ being analytic—there is no clear reason to expect $\boldsymbol { p } _ { n } ^ { * }$ to be much better than $p _ { n }$ .

An observation for arbitrary functions $f$ is the following consequence of Theorems 15.1–15.3.

Theorem 16.1. Chebyshev projections and interpolants are near-best. Let $f \in C ( [ - 1 , 1 ] )$ have degree $n$ Chebyshev projection $f _ { n }$ , Chebyshev interpolant $p _ { n }$ , and best approximant $\boldsymbol { p } _ { n } ^ { * }$ , $n \geq 1$ . Then

$$
\| f - f _ { n } \| \leq \left( 4 + { \frac { 4 } { \pi ^ { 2 } } } \log ( n + 1 ) \right) \| f - p _ { n } ^ { * } \|
$$

and

$$
\| f - p _ { n } \| \leq \left( 2 + { \frac { 2 } { \pi } } \log ( n + 1 ) \right) \| f - p _ { n } ^ { * } \| .
$$

Proof. The proof follows from Theorems 15.1, 15.2, and 15.3.

So the loss of accuracy in going from $\boldsymbol { p } _ { n } ^ { * }$ to $p _ { n }$ , say, can never be larger than a factor of $2 + ( 2 / \pi ) \log ( n + 1 )$ . It is interesting to examine the size of this quantity for various values of $n$ . For $n = 1 0 ^ { 5 }$ , for example,

ans = 9.3294

Since this number is less than 10, we see that in dealing with polynomials of degree up to $n = 1 0 0 0 0 0$ , the nonoptimality of Chebyshev interpolation can never cost us more than 1 digit of accuracy. Here is the computation for $n = 1 0 ^ { 6 6 }$ :

ans $=$ 98.7475

So we never lose more than 2 digits for degrees all the way up to $1 0 ^ { 6 6 }$ —which might as well be $\infty$ for practical purposes. (For British audiences, one can give a talk on these matters with the title “ $1 0 ^ { 6 6 }$ and All That.”)

In fact, one might question whether best approximations are really better than near-best ones at all. Of course they are better in a literal sense, as measured in the $\infty$ -norm. However, consider the following error curves, which are quite typical for high-degree approximation of a function that is smoother in some regions than others.

$\begin{array} { r l } { \mathbf { f } } & { { } = } \end{array}$ abs(x-0.8); tic, pbest $=$ minimax(f,100); toc, hold off, plot(f-pbest,'r') tic, pcheb $=$ chebfun(f,101); toc, hold on, plot(f-pcheb)

Elapsed time is 0.195897 seconds.   
Elapsed time is 0.005879 seconds.

![](images/6e6dc52df76454a7f7e350d0f95d05a8f379a23b984d35c5834e9ca9dfe04255.jpg)

We see that pbest is worse than pcheb for almost all values of $x$ , because the damage done by the singularity at $x = 0 . 8$ is global. By contrast, the effect of the singularity on pcheb decays with distance. Of course, pbest is better in the $\infty$ -norm:

errcheb $=$ norm(f-pcheb,inf), errbest $=$ norm(f-pbest,inf)

errcheb $=$ 0.0060 errbest $= \ 0 . 0 0 1 7 $

In the 2-norm, however, it is a good deal worse:

errcheb2 $=$ norm(f-pcheb,2), errbest2 $=$ norm(f-pbest,2)

errcheb2 $=$ 4.3337e-04   
errbest2 $=$ 0.0017

One might question how many applications there might be in which pbest was truly better than pcheb as an approximation to this function $f$ . To echo a title of Corless and Watt [2004], minimax approximations are optimal, but Chebyshev interpolants may sometimes be better!

Li [2004] takes another angle on the near-optimality of Chebyshev interpolants, pointing out that for applications to elementary functions, bounds on certain derivatives usually hold that imply that the error in interpolation in Chebyshev points of the first kind exceeds that of the best approximation by less than a factor of 2 or, as he calls it, “a fractional bit.”

From a more theoretical point of view, we return to a notion mentioned in Theorem 12.1. Given $f \in C ( [ - 1 , 1 ] )$ , let $\rho$ ( $1 \le \rho \le \infty$ ) be the parameter of the largest Bernstein ellipse $E _ { \rho }$ to which $f$ can be analytically continued, and let $\left\{ p _ { n } \right\}$ be any sequence of approximations to $f$ with $p _ { n } \in \mathcal { P } _ { n }$ . Then

$$
\operatorname* { l i m } _ { n \to \infty } \| f - p _ { n } \| ^ { 1 / n } \geq \rho ^ { - 1 } ,
$$

and if equality holds, $\left\{ p _ { n } \right\}$ is said to be maximally convergent. It follows from Theorems 8.2 and 15.1 that if $\{ p _ { n } \}$ comes from a linear projection with Lebesgue constants $\Lambda _ { n }$ that grow more slowly than exponentially as $\begin{array} { r l } { n \ \to \ \infty } \end{array}$ , i.e., with $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \Lambda _ { n } ^ { 1 / n } = 1 } \end{array}$ , then $\left\{ p _ { n } \right\}$ is maximally convergent for every $f \in C ( [ - 1 , 1 ] )$ . In particular, Chebyshev projections and interpolants are maximally convergent. This is a precise sense in which such approximations are “near-best.”

Finally, we mention another kind of optimality that has received attention in the approximation theory literature [Bernstein 1931, Erd˝os 1961, Kilgore 1978, de Boor & Pinkus 1978]: optimal interpolation points (Exercise 15.5). Chebyshev points are very good, but they do not quite minimize the Lebesgue constant. Optimal points minimize the Lebesgue constant (by definition), and they level out the peaks of the Lebesgue function exactly (it has been proved)—but the improvement is negligible. The first statement of Theorem 15.2 establishes that, like Chebyshev points, they lead to Lebesgue constants that are asymptotic to $( 2 / \pi ) \log n$ as $n  \infty$ , which means they do not improve upon Chebyshev points even by a constant factor.

Summary of Chapter 16. The $\infty$ -norm error in degree $n$ Chebyshev interpolation is never greater than $2 + ( 2 / \pi ) \log ( n + 1 )$ times the error in best approximation, and in practice, the ratio rarely exceeds even a factor of 2. In the 2-norm, the interpolant is often much better than the best approximation.

Exercise 16.1. Computing times for interpolation and best approximation. (a) Repeat the experiment of this chapter involving $\left| x - 0 . 8 \right|$ but for all the values $n = 1 0 0 , 2 0 0 , 3 0 0 , \ldots , 1 0 0 0$ . In each case measure the computing times for Chebyshev interpolation and best approximation as calculated by the Chebfun minimax command, the $L ^ { 2 }$ errors of both approximants, and the $L ^ { \infty }$ errors. Plot these results and comment on what you find. (b) In particular, produce a plot of error curves like that in the text.

Exercise 16.2. Approximation of a wiggly function. Define $f ( x ) = T _ { 2 0 0 } ( x ) +$ $T _ { 2 0 1 } ( x ) + \cdot \cdot \cdot + T _ { 2 2 0 } ( x )$ . Construct the Chebyshev interpolant $p$ and best approximation $p ^ { * }$ of degree 199. Plot the errors and measure the $\infty$ - and 2-norms.

Exercise 16.3. Rounding errors on a grid of $\mathbf { 1 0 ^ { 6 6 } }$ points. Suppose we had a computer with 16-digit precision capable of applying the barycentric formula (5.13) to evaluate a polynomial interpolant $p ( x )$ for data on a Chebyshev grid of $1 0 ^ { 6 6 }$ points. (For the sake of this thought experiment, imagine that the differences $\boldsymbol { x } - \boldsymbol { x _ { j } }$ can be evaluated correctly to 16-digit precision rather than coming out as 0 and thereby invoking the $x = x _ { j }$ clause of Theorem 5.2.) The evaluation would require adding up about $1 0 ^ { 6 6 }$ numbers, entailing about $1 0 ^ { 6 6 }$ rounding errors. Even if these errors accumulated only in the square root fashion of a random walk, it would still seem we must end up with errors on the order of $1 0 ^ { 3 3 }$ times $1 0 ^ { - 1 6 }$ , destroying all accuracy. Yet in fact, the computation would be highly accurate. What is the flaw in this $1 0 ^ { 3 3 }$ reasoning?

Exercise 16.4. Another wiggly function. Consider the function $f ( x ) = \sin ( x ^ { 2 } ) +$ $\ \sin ( x ) ^ { 2 }$ on the interval [0, 14]. Compute its degree 100 best polynomial approximation $p$ and make plots of $f$ and $p$ together and of $f - p$ . Discuss these curves in light of the developments of this chapter.

# Chapter 17. Orthogonal Polynomials

This book gives special attention to Chebyshev polynomials, since they are so useful in applications and the analogue on $[ - 1 , 1 ]$ of trigonometric polynomials on $[ - \pi , \pi ]$ . However, Chebyshev polynomials are just one example of a family of orthogonal polynomials defined on the interval $[ - 1 , 1 ]$ , and in this chapter we note some of the other possibilities, especially Legendre polynomials, which are the starting point for Gauss quadrature (Chapter 19). The study of orthogonal polynomials was initiated by Jacobi [1826] and already well developed by the end of the 19th century thanks to work by mathematicians including Chebyshev, Christoffel, Darboux, and Stieltjes. Landmark books on the subject include Szeg˝o [1985] and Gautschi [2004].

Let $w \in C ( - 1 , 1 )$ be a weight function with $w ( x ) > 0$ for all $x \in ( - 1 , 1 )$ and $\textstyle \int _ { - 1 } ^ { 1 } w ( x ) d x < \infty$ ; we allow $w ( x )$ to approach 0 or $\infty$ as $x  \pm 1$ . The function $w$ defines an inner product for functions defined on $[ - 1 , 1 ]$ :

$$
( f , g ) = \int _ { - 1 } ^ { 1 } w ( x ) { \overline { { f ( x ) } } } g ( x ) d x .
$$

(The bar over $f ( x )$ indicates the complex conjugate and can be ignored when working with real functions.) A family of orthogonal polynomials associated with $w$ is a family

$$
p _ { 0 } , p _ { 1 } , p _ { 2 } , \ldots ,
$$

where $p _ { n }$ has degree exactly $n$ for each $n$ and the polynomials satisfy the orthogonality condition

$$
( p _ { j } , p _ { k } ) = 0 , \quad k \neq j .
$$

Notice that this condition implies that each $p _ { n }$ is orthogonal to all polynomials of degree $k < n$ . The condition (17.2) determines the family uniquely except that each $p _ { n }$ can be multiplied by a constant factor. One common normalization is to

require that each $p _ { n }$ be monic, in which case we have a family of monic orthogonal polynomials. Another common normalization is $p _ { 0 } > 0$ together with the condition

$$
( p _ { j } , p _ { k } ) = \delta _ { j k } = { \left\{ \begin{array} { l l } { 1 , } & { k = j , } \\ { 0 , } & { k \neq j , } \end{array} \right. }
$$

in which case we have orthonormal polynomials. A third choice, the standard one for Chebyshev and Legendre polynomials, is to require $p _ { n } ( 1 ) = 1$ for each $n$ .

As we have seen in Chapter 3, the Chebyshev polynomials $\{ T _ { k } \}$ are orthogonal with respect to the weight function

$$
w ( x ) = { \frac { 2 } { \pi { \sqrt { 1 - x ^ { 2 } } } } }
$$

(Exercise 3.7). In fact, if $T _ { 0 }$ is replaced by $T _ { 0 } / \sqrt { 2 }$ , they are orthonormal. The first three Chebyshev polynomials are

$$
T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x , \quad T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 ,
$$

as we can confirm with the chebpoly command:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , disp(fliplr(poly(chebpoly(j)))), end

$$
\begin{array} { c c c c c c c c c c c c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

The Chebyshev weight function has an inverse–square root singularity at each end of $[ - 1 , 1 ]$ . Allowing arbitrary power singularities at each end gives the Jacobi weight function $w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta }$ , where $\alpha , \beta > - 1$ are parameters. The associated orthogonal polynomials are known as Jacobi polynomials and written as $\{ P _ { n } ^ { ( \alpha , \beta ) } \}$ . In the special case $\alpha = \beta$ we get the Gegenbauer or ultraspherical polynomials.

The most special case of all is $\alpha = \beta = 0$ , leading to Legendre polynomials, with the simplest of all weight functions, a constant:

$$
w ( x ) = 1 .
$$

If we normalize according to (17.3), the first three Legendre polynomials are

$$
p _ { 0 } ( x ) = \sqrt { 1 / 2 } , \quad p _ { 1 } ( x ) = \sqrt { 3 / 2 } x , \quad p _ { 2 } ( x ) = \sqrt { 4 5 / 8 } x ^ { 2 } - \sqrt { 5 / 8 } ,
$$

as we can confirm by using the flag 'norm' with the legpoly command:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , c = fliplr(poly(legpoly(j,'norm'))); disp(c), end

<table><tr><td>-0.7906</td><td>-0.0000</td><td>2.3717</td><td></td><td></td></tr><tr><td>0.0000</td><td>-2.8062</td><td>-0.0000</td><td>4.6771</td><td></td></tr><tr><td>0.7955</td><td>0.0000</td><td>-7.9550</td><td>-0.0000</td><td>9.2808</td></tr><tr><td>0.0000</td><td>4.3973</td><td>-0.0000</td><td>-20.5206</td><td>0.0000 18.4685</td></tr></table>

However, as mentioned above, it is more common to normalize Legendre polynomials by the condition $p _ { j } ( 1 ) = 1$ . Switching to an uppercase $P$ to follow the usual notation, the first three Legendre polynomials are

$$
\begin{array} { r } { P _ { 0 } ( x ) = 1 , \quad P _ { 1 } ( x ) = x , \quad P _ { 2 } ( x ) = \frac { 3 } { 2 } x ^ { 2 } - \frac { 1 } { 2 } . } \end{array}
$$

These are the polynomials returned by legpoly by default:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , c = fliplr(poly(legpoly(j))); disp(c), end

The rest of this chapter is devoted to comparing Legendre and Chebyshev polynomials. The comparison, and the consideration of orthogonal polynomials in general, will continue into the next two chapters on rootfinding (Chapter 18) and quadrature (Chapter 19). For example, Theorem 19.6 presents a fast method for calculating the barycentric interpolation weights for Legendre points, the zeros of Legendre polynomials. On the whole, different families of orthogonal polynomials have similar approximation properties, but Chebyshev points have the particular advantage that one can convert back and forth between interpolant and expansion by the FFT.

We begin with a visual comparison of the Chebyshev and Legendre polynomials of degrees 1–6 for $x \in [ - 1 , 1 ]$ . The shapes are similar, with the degree $n$ polynomial always having $n$ roots in the interval (Exercise 17.4).

for $\mathrm { ~ n ~ } = \mathrm { ~ 1 { : } ~ 6 ~ }$ $\mathrm { { T } \{ n \} \mathrm { { \Omega } = } }$ chebpoly(n); subplot(3,2,1), plot(T{n}) $\mathsf { P \{ n \} } = \mathsf { I e g p o l y ( n ) }$ ; subplot(3,2,2), plot(P{n},'m')   
end

![](images/1a20f25dd9da4716489b90fc593c2788273dd0907ffe4dcac8bc6f3f5409b30f.jpg)

For Legendre polynomials normalized by $P _ { j } ( 1 ) = 1$ , the orthogonality condition turns out to be

$$
\int _ { - 1 } ^ { 1 } P _ { j } ( x ) P _ { k } ( x ) d x = { \left\{ \begin{array} { l l } { 0 , } & { j \neq k , } \\ { { \cfrac { 2 } { 2 k + 1 } } , } & { j = k . } \end{array} \right. }
$$

We can verify this formula numerically by constructing what Chebfun calls a quasimatrix $X$ , that is, a “matrix” whose columns are chebfuns, and then taking inner products of each column with each other column via the quasimatrix product $X ^ { T } X$ . One way to construct $X$ is like this:

Another equivalent method is built into legpoly:

Here is the quasimatrix product:

X'\*X ans $=$

0.6667 0.0000 0.0000 -0.0000 -0.0000 -0.0000

<table><tr><td>0.0000</td><td>0.4000</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.0000</td></tr><tr><td>0.0000</td><td>-0.0000</td><td>0.2857</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td></tr><tr><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.2222</td><td>-0.0000</td><td>-0.0000</td></tr><tr><td>-0.0000</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.1818</td><td>0.0000</td></tr><tr><td>-0.0000</td><td>0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.0000</td><td>0.1538</td></tr></table>

This matrix of inner products looks diagonal, as it should, and we can confirm the diagonal structure by checking the norm of the off-diagonal terms:

norm(ans-diag(diag(ans)))

ans = 2.3066e-16

The entries on the diagonal are the numbers $2 / 3 , 2 / 5 , 2 / 7 , \ldots$ prescribed by (17.5). Legendre polynomials satisfy the 3-term recurrence relation

$$
( k + 1 ) P _ { k + 1 } ( x ) = ( 2 k + 1 ) x P _ { k } ( x ) - k P _ { k - 1 } ( x ) ,
$$

which may be compared with the recurrence relation (3.10) for Chebyshev polynomials. In general, orthogonal polynomials defined by (17.1)–(17.2) always satisfy a 3-term recurrence relation, and the reason is as follows. Supposing $\left\{ p _ { n } \right\}$ are monic for simplicity, one can determine $p _ { n + 1 }$ by the Gram–Schmidt orthogonalization procedure, subtracting off the projections of the monic degree $n + 1$ polynomial $x p _ { n }$ onto each of the polynomials $p _ { 0 } , \ldots , p _ { n }$ , with the coefficient of the projection onto $p _ { k }$ being given by the normalized inner product $( x p _ { n } , p _ { k } ) / ( p _ { k } , p _ { k } )$ :

$$
p _ { n + 1 } = x p _ { n } - { \frac { ( x p _ { n } , p _ { n } ) } { ( p _ { n } , p _ { n } ) } } p _ { n } - { \frac { ( x p _ { n } , p _ { n - 1 } ) } { ( p _ { n - 1 } , p _ { n - 1 } ) } } p _ { n - 1 } - \cdots - { \frac { ( x p _ { n } , p _ { 0 } ) } { ( p _ { 0 } , p _ { 0 } ) } } p _ { 0 } .
$$

For every $k < n { - } 1$ , however, the inner product is equal to $0$ because $p _ { n }$ is orthogonal to the lower-degree polynomial $x p _ { k }$ : 8

$$
\left( x p _ { n } , p _ { k } \right) = \left( p _ { n } , x p _ { k } \right) = 0 , \quad k < n - 1 .
$$

Thus the series above reduces to the 3-term recurrence [Darboux 1878]

$$
p _ { n + 1 } = x p _ { n } - { \frac { ( x p _ { n } , p _ { n } ) } { ( p _ { n } , p _ { n } ) } } p _ { n } - { \frac { ( x p _ { n } , p _ { n - 1 } ) } { ( p _ { n - 1 } , p _ { n - 1 } ) } } p _ { n - 1 } .
$$

When the weight function $w$ is even, the middle term drops out (Exercise 17.5), and the formula further simplifies to

$$
p _ { n + 1 } = x p _ { n } - { \frac { \left( x p _ { n } , p _ { n - 1 } \right) } { \left( p _ { n - 1 } , p _ { n - 1 } \right) } } p _ { n - 1 } \quad { \mathrm { f o r ~ } } w { \mathrm { ~ e v e n } } .
$$

Chebyshev polynomials are not orthogonal in the standard inner product:

ans =

Nevertheless, Legendre and Chebyshev polynomials have much in common, as is further suggested by plots of $T _ { 5 0 }$ and $P _ { 5 0 }$ :

$\mathrm { T 5 0 ~ = }$ chebpoly(50); P50 $=$ legpoly(50); subplot(2,1,1), plot(T50), subplot(2,1,2), plot(P50,'m')

![](images/e5d90fc270f7450248ea2b1c856e47fbef6043888b3234374787fb6bc4a6a7e9.jpg)

The zeros of the two families of polynomials are similar, as can be confirmed by comparing Chebyshev (dots) and Legendre (crosses) zeros for degrees 10, 20, and 50. (Instead of using the roots command here, one could achieve the same effect with chebpts(n,1) and legpts(n)—see Chapter 19.)

$\mathrm { T 1 0 ~ = }$ chebpoly(10); $\mathrm { { \Delta P 1 0 ~ } = }$ legpoly(10); Tr $=$ roots(T10); Pr = roots(P10); plot(Tr,.8,'.b'), hold on $\mathtt { p l o t } ( \mathtt { P r } , 0 . 9 , \mathbf { \Phi } ^ { \prime } \mathbf { x } \mathrm { m } ^ { \prime } )$ , ${ \mathrm { T } } 2 0 ~ =$ chebpoly(20); P20 = legpoly(20); Tr $=$ roots(T20); Pr $=$ roots(P20); plot(Tr,0.4,'.b') plot(Pr,0.5,'xm'), Tr $=$ roots(T50); Pr $=$ roots(P50); plot(Tr,0,'.b'), plot(Pr,0.1,'xm')

![](images/3740ddcf5c692d75db05d0c234a46138c6e6323c2609fbc88ed75e7ca3d25a0e.jpg)

Asymptotically as $n \to \infty$ , both sets of zeros cluster near $\pm 1$ with the same density distribution $n \mu ( x )$ , with $\mu$ given by (12.10). This behavior is made precise in

Theorem 12.1.4 of [Szeg˝o 1939] (Exercise 17.7), and exploitation of more detailed asymptotic properties of Jacobi polynomials is the crucial idea of [Hale & Townsend 2013].

Another comparison between Chebyshev and Legendre points concerns their Lebesgue functions and Lebesgue constants. Here we repeat a computation of Lebesgue functions from Chapter 15 for 8 Chebyshev points and compare it with the analogous computation for 8 Legendre points. Chebyshev and Legendre points as we have defined them so far differ not just in which polynomials they are connected with, but in that Chebyshev points come from extrema whereas Legendre points come from zeros.

$\qquad \mathtt { s } \ =$ chebpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst s $=$ legpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,2), plot(L), hold on, plot(s,L(s),'.'), Lconst

![](images/cdef487416dfbf74a75466ec8a6492f07456e9383e3368b077b9f7b47033309d.jpg)

The Lebesgue functions and constants for Legendre points are a little bigger than for Chebyshev points, having size $O ( n ^ { 1 / 2 } )$ rather than $O ( \log n )$ because of behavior near the endpoints [Szeg˝o 1939, p. 338]. This small difference is of little significance for most applications: the Lebesgue constants are still quite small, and either set of points will usually deliver excellent interpolants.

An alternative is to consider Legendre extreme points—the $n { \mathrel { + { 1 } } }$ points in $[ - 1 , 1 ]$ at which $| P _ { n } ( x ) |$ attains a local maximum. (The Legendre extreme points in $( - 1 , 1 )$ are also the roots of the Jacobi polynomial $P ^ { ( 1 , 1 ) } ( x )$ .) The Lebesgue function in this case looks even more satisfactory:

$\begin{array} { r } { \{ \begin{array} { r l } \end{array} \} = } & { { } \left[ - 1 \right. } \end{array}$ ; roots(diff(legpoly(7))); 1]; [L,Lconst] $=$ lebesgue(s); subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst $\mathbf { s } 1 5 ~ = ~ [ - 1$ ; roots(diff(legpoly(15))); 1]; [L,Lconst] $=$ lebesgue(s15); subplot(1,2,2), plot(L), hold on, plot(s15,L(s15),'.'), Lconst

Lconst $=$ 1.9724 Lconst $= \ 2 . 4 3 0 3$

![](images/f7c717a5dd83eb265b9678958aa24fb2c4a0c928fa0045020762ee3ff17e2ec0.jpg)

The Legendre extreme points have a memorable property: as shown by Stieltjes [1885], they are the Fekete or minimal-energy points in $[ - 1 , 1 ]$ , solving the equipotential problem on that interval for a finite number of equal charges (Exercise 12.1). Here, for example, is a repetition of a figure from Chapter 11 but now for 8 Legendre extreme points instead of 8 Chebyshev points. Again the behavior is excellent.

ell = poly(s,domain(-1,1)); plot(s,ell(s),'.k'), hold on xgrid $=$ -1.5:.02:1.5; ygrid $=$ -0.9:.02:0.9;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
ellzz $=$ ell(zz); levels $=$ 2.^(-6:0);   
contour(xx,yy,abs(ellzz),levels, $" \mathrm { \text k } "$ )

![](images/6b047fa41059702f7cc737862d2b7cf9a89af12b45f4fe02088e26526005d763.jpg)

Summary of Chapter 17. Chebyshev polynomials are just one example of a family of polynomials orthogonal with respect to a weight function $w ( x )$ on $[ - 1 , 1 ]$ . For $w ( x ) = c o n s t a n t$ , one gets the Legendre polynomials.

Exercise 17.1. Chebyshev and Legendre Lebesgue constants. Extend the experiments of the text to a table and a plot of Lebesgue constants of Chebyshev, Legendre, and Legendre extreme points for interpolation in $n + 1$ points with $n = 1 , 2 , 4 , \dotsc , 2 5 6$ . (To compute Legendre extreme points efficiently, you can use the observation about Jacobi polynomials mentioned in the text and the Chebfun command jacpoly.) What asymptotic behavior do you observe as $n \to \infty$ ?

Exercise 17.2. Chebyshev and Legendre interpolation points. Define $f ( x ) =$ $x \operatorname { t a n h } ( 2 \sin ( 2 0 x ) )$ , and let $p$ and $p _ { L }$ be the interpolants to $f$ in $n + 1$ Chebyshev or Legendre points on $[ - 1 , 1 ]$ , respectively. The latter can be computed with interp1 as in

Chapter 13. (a) For $n + 1 = 3 0$ , plot $f$ , $p$ , and $p _ { L }$ . What are the $\infty$ -norm errors $\| f - p \|$ and $\| f - p _ { L } \| ^ { . }$ ? (b) For $n + 1 = 3 0 0$ , plot $f - p$ and $f - p _ { L }$ . What are the errors now?

Exercise 17.3. Orthogonal polynomials via QR decomposition. (a) Construct a Chebfun quasimatrix A with columns corresponding to $1 , x , \ldots , x ^ { 5 }$ on $[ - 1 , 1 ]$ . Execute $\begin{array} { r } { [ { \mathsf Q } , { \mathsf R } ] { \mathsf \Pi } = { \mathsf Q } { \mathsf r } \left( { \mathsf A } \right) } \end{array}$ to find an equivalent set of orthonormal functions, the columns of $\mathsf { Q }$ , and plot these with plot(Q). How do the columns of $\mathsf { Q }$ compare with the Legendre polynomials normalized by (17.3)? (b) Write a for loop to normalize the columns of $\mathsf { Q }$ in a fashion corresponding to $P _ { j } ( 1 ) = 1$ and to adjust $R$ correspondingly so that the product $\scriptstyle { \mathsf { Q } } \ast { \mathsf { R } }$ continues to be equal to A, up to rounding errors, and plot the new quasimatrix with plot(Q). How do the columns of the new $\mathsf { Q }$ compare with the Legendre polynomials normalized by $P _ { j } ( 1 ) = 1 \Rsh$

Exercise 17.4. Zeros of orthogonal polynomials. Let $\left\{ p _ { n } \right\}$ be a family of orthogonal polynomials on $[ - 1 , 1 ]$ defined by (17.1)–(17.2). Show by using (17.2) that the zeros of $p _ { n }$ are distinct and lie in $( - 1 , 1 )$ .

Exercise 17.5. Even and odd orthogonal polynomials. Suppose the weight function $w$ of (17.1) is even. Prove by induction that $p _ { n }$ is even when $n$ is even and odd when $_ n$ is odd.

Exercise 17.6. Legendre and Chebyshev differential equations. (a) Show from the recurrence relation (17.6) that the Legendre polynomial $P _ { n }$ satisfies the differential equation $( 1 - x ^ { 2 } ) P ^ { \prime \prime } - 2 x P ^ { \prime } + n ( n + 1 ) P = 0$ . (b) Show from (3.10) that the Chebyshev polynomial $T _ { n }$ satisfies the differential equation $( 1 - x ^ { 2 } ) T ^ { \prime \prime } - x T ^ { \prime } + n ^ { 2 } T = 0$ .

Exercise 17.7. The envelope of an orthogonal polynomial. Theorem 12.1.4 of [Szeg˝o 1939] asserts that as $n \to \infty$ , the envelope of an orthonormal polynomial $p _ { n }$ defined by (17.1)–(17.3) approaches the curve $( w _ { \mathrm { C H E B } } ( x ) / w ( x ) ) ^ { 1 / 2 }$ , where $w _ { \mathrm { C H E B } }$ is the Chebyshev weight (17.4). Explore this prediction numerically with plots of Legendre polynomials for various $_ n$ .

Exercise 17.8. Minimality of orthogonal polynomials. Let $\left\{ p _ { n } \right\}$ be the family of monic orthogonal polynomials associated with the inner product (17.1). Show that if $q$ is any monic polynomial of degree $_ n$ , then $\left( q , q \right) \geq \left( p _ { n } , p _ { n } \right)$ .

# Chapter 18. Polynomial Roots and Colleague Matrices

It is well known that if $p$ is a polynomial expressed as a linear combination of monomials $x ^ { k }$ , then the roots of $p$ are equal to the eigenvalues of a certain companion matrix formed from its coefficients (Exercise 18.1). Indeed, from its beginning in the late 1970s, MATLAB has included a command roots that calculates roots of polynomials by using this identity. This method of zerofinding is effective and numerically stable, but only in a very narrow sense. It is a numerically stable algorithm for precisely the problem just posed: given the monomial coefficients, find the roots. The trouble is, this problem is an awful one! As Wilkinson made famous beginning in the 1960s, it is a highly ill-conditioned problem in general [Wilkinson 1984]. The roots tend to be so sensitive to perturbations in the coefficients that even though the algorithm is stable in the sense that it usually produces roots that are exactly correct for a polynomial whose coefficients match the specified ones to a coefficientwise relative error on the order of machine precision [Goedecker 1994, Toh & Trefethen 1994], this slight perturbation is enough to cause terrible inaccuracy.

There is an exception to this dire state of affairs. Finding roots from polynomial coefficients is a well-conditioned problem in the special case of polynomials with roots on or near the unit circle (see Exercise 18.7(a) and [Sitton et al. 2003]). The trouble is, most applications are not of this kind. More often, the roots of interest lie in or near a real interval, and in such cases one should avoid monomials, companion matrices, and the MATLAB roots command completely.

Fortunately, there is a well-conditioned alternative for such problems, and that is the subject of this chapter. By now we are experts in working with functions on $[ - 1 , 1 ]$ by means of Chebyshev interpolants and Chebyshev series. Within this class of tools, there is a natural way of computing the roots of a polynomial by solving an eigenvalue problem. Here is the crucial result, due independently to Specht [1960, p. 222] and Good [1961].9 The matrix $C$ of the theorem is called a colleague matrix.

Theorem 18.1. Polynomial roots and colleague matrix eigenvalues. The roots of the polynomial

$$
p ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } T _ { k } ( x ) , \quad a _ { n } \ne 0 ,
$$

are the eigenvalues of the matrix

$$
C = \left( \begin{array} { c c c c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { 1 } { 2 } } } & { { 0 } } & { { \frac { 1 } { 2 } } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \frac { 1 } { 2 } } } & { { 0 } } & { { \frac { 1 } { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { \frac { 1 } { 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { \frac { 1 } { 2 } } } & { { 0 } } & { { } } & { { a _ { 1 } } } & { { a _ { 2 } } } & { { \ldots } } & { { a _ { n - 1 } } } \end{array} \right) .
$$

(Entries not displayed are zero.) If there are multiple roots, these correspond to eigenvalues with the same multiplicities.

Proof. Let $x$ be any number, and consider the nonzero $n$ -vector

$$
v = ( T _ { 0 } ( x ) , T _ { 1 } ( x ) , \ldots , T _ { n - 1 } ( x ) ) ^ { T } .
$$

If we multiply $C$ by $v$ , then in every row but the first and last the result is

$$
\begin{array} { r } { T _ { k } ( x ) \mapsto \frac 1 2 T _ { k - 1 } ( x ) + \frac 1 2 T _ { k + 1 } ( x ) = x T _ { k } ( x ) , } \end{array}
$$

thanks to the 3-term recurrence relation (3.9) for Chebyshev polynomials. In the first row we likewise have

$$
T _ { 0 } ( x ) \mapsto T _ { 1 } ( x ) = x T _ { 0 } ( x )
$$

since $T _ { 0 } ( x ) = 1$ and $T _ { 1 } ( x ) = x$ . It remains to examine the bottom row. Here it is convenient to imagine that in the difference of matrices defining $C$ above, the “missing” entry $1 / 2$ is added in the $( n , n + 1 )$ position of the first matrix and subtracted again from the $( n , n + 1 )$ position of the second matrix. Then by considering the recurrence relation again we find

$$
T _ { n - 1 } ( x ) \mapsto x T _ { n - 1 } ( x ) - { \frac { 1 } { 2 a _ { n } } } ( a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + a _ { n } T _ { n } ( x ) ) .
$$

This equation holds for any $x$ , and if $x$ is a root of $p$ , then the term in parentheses on the right vanishes. In other words, if $x$ is a root of $p$ , then $C v$ is equal to $x v$ in every entry, making $v$ an eigenvector of $C$ with eigenvalue $x$ . If $p$ has $n$ distinct roots, this implies that they are precisely the eigenvalues of $C$ , and this completes the proof in the case where $p$ has distinct roots.

If $p$ has multiple roots, we must show that each one corresponds to an eigenvalue of $C$ with the same multiplicity. For this we can consider perturbations of the coefficients $a _ { 0 } , \ldots , a _ { n - 1 }$ of $p$ with the property that the roots become distinct. Each root must then correspond to an eigenvalue of the correspondingly perturbed matrix $C$ , and since both roots of polynomials and eigenvalues of matrices are continuous functions of the parameters, the multiplicities must be preserved in the limit as the amplitude of the perturbations goes to zero.

As mentioned above, the matrix $C$ of (18.1) is called a colleague matrix. Theorem 18.1 has been rediscovered several times, for example by Day & Romero [2005]. Since Specht [1957] there have also been generalizations to other families of orthogonal polynomials besides Chebyshev polynomials, and the associated generalized colleague matrices are called comrade matrices [Barnett 1975a & 1975b]. The generalization is immediate: one need only change the entries of rows 1 to $n - 1$ to correspond to the appropriate recurrence relation.

For an example to illustrate Theorem 18.1, consider the polynomial $p ( x ) =$ $x ( x - 1 / 4 ) ( x - 1 / 2 )$ .

![](images/4538c54c3096c0ab991b7ee3c1f9d20e8d5c95ed7b5c2307d5607307f3648368.jpg)

Obviously $p$ has roots $0$ , $1 / 4$ , and $1 / 2$ . The Chebyshev coefficients are $- 3 / 8 , 7 / 8$ , $- 3 / 8 , 1 / 4$ :

a = fliplr(chebpoly(p))   
a = -0.3750 0.8750 -0.3750 0.2500

As expected, the colleague matrix (18.1) for this polynomial,

C = [0 1 0; 1/2 0 1/2; 0 1/2 0] - (1/(2\*a(4)))\*[0 0 0; 0 0 0; a(1:3)] ${ \mathrm { ~ \small ~ C ~ } } =$

<table><tr><td>0</td><td>1.0000 0</td></tr><tr><td>0.5000</td><td>0 0.5000</td></tr><tr><td>0.7500</td><td>-1.2500 0.7500</td></tr></table>

has eigenvalues that match the roots of $p$ :

eig(C)

0.500000000000002   
0.249999999999999

In Chebfun, every function is represented by a polynomial or a piecewise polynomial. Theorem 18.1 provides Chebfun with its method of numerical rootfinding, implemented in the Chebfun roots command. For this polynomial $\mathrm { \Delta p }$ , we can call roots to add the roots to the plot, like this:

![](images/0f3a505ef380cf16e56ba97b6127b80e6ed487af6dbf61e4b795f24fa5999962.jpg)

In this example, $\mathrm { \Delta } _ { \mathrm { { P } } }$ was a polynomial from the start. The real power of Theorem 18.1, however, comes when it is applied to the problem of finding the roots on $[ - 1 , 1 ]$ of a general function $f$ . To do this, we first approximate $f$ by a polynomial and then find the roots of the polynomial. This idea was proposed in Good’s original 1961 paper [Good 1961]. In a more numerical era, it has been advocated in a number of papers by John Boyd, including [Boyd 2002], and it is exploited virtually every time Chebfun is used.

For example, here is the chebfun corresponding to $\cos ( 5 0 \pi x )$ on $[ - 1 , 1 ]$

It doesn’t take long to compute its roots, tic, r $=$ roots(f); toc

Elapsed time is 0.015067 seconds.

The exact roots of this function on $[ - 1 , 1 ]$ are $- 0 . 9 9 , - 0 . 9 7 , \hdots , 0 . 9 7 , 0 . 9 9$ . Inspecting a few of the computed results shows they are accurate to close to machine precision: