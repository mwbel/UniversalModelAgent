# Chapter 6. Weierstrass Approximation Theorem

Every continuous function on a bounded interval can be approximated to arbitrary accuracy by polynomials. This is the famous Weierstrass approximation theorem, proved by Karl Weierstrass when he was 70 years old [Weierstrass 1885]. The theorem was independently discovered at about the same time, in essence, by Carl Runge: as pointed out in 1886 by Phragm´en in remarks published as a footnote stretching over four pages in a paper by Mittag-Leffler [1900], it can be derived as a corollary of results Runge published in a pair of papers in 1885 [Runge 1885a & 1885b].

Here and throughout this book, unless indicated otherwise, $\| \cdot \|$ denotes the supremum norm on $[ - 1 , 1 ]$ .

Theorem 6.1. Weierstrass approximation theorem. Let $f$ be a continuous function on $[ - 1 , 1 ]$ , and let $\varepsilon > 0$ be arbitrary. Then there exists a polynomial $p$ such that

$$
\| f - p \| < \varepsilon .
$$

Outline of proof. We shall not spell out an argument in detail. However, here is an outline of the beautiful proof from Weierstrass’s original paper. First, extend $f ( x )$ to a continuous function $\tilde { f }$ with compact support on the whole real line. Now, take $\ddot { f }$ as initial data at $t ~ = ~ 0$ for the diffusion equation $\partial u / \partial t = \partial ^ { 2 } u / \partial x ^ { 2 }$ o n the real line. It is known that by convolving $\ddot { f }$ with the Gaussian kernel $\phi ( x ) = $ $e ^ { - x ^ { 2 } / 4 t } / \sqrt { 4 \pi t }$ , we get a solution to this PDE that converges uniformly to $f$ as $t  0$ and thus can be made arbitrarily close to $f$ on $[ - 1 , 1 ]$ by taking $t$ small enough. On the other hand, since $\tilde { f }$ has compact support, for each $t > 0$ this solution is an integral over a bounded interval of entire functions and is thus itself an entire function, that is, analytic throughout the complex plane. Therefore it has a uniformly convergent Taylor series on $[ - 1 , 1 ]$ , which can be truncated to give polynomial approximations of arbitrary accuracy.

For a fuller presentation of the argument just given as “one of the most amusing applications of the Gaussian kernel,” where the result is stated for the more general case of a function of several variables approximated by multivariate polynomials, see [Folland 1995].

Many other proofs of the Weierstrass theorem are also known, including these early ones:

Runge (1885)   
Picard (1891)   
Lerch (1892 and 1903)   
Volterra (1897)   
Lebesgue (1898)   
Mittag-Leffler (1900)   
Fej´er (1900 and 1916)   
Landau (1908)   
de la Vall´ee Poussin (1908)   
Jackson (1911)   
Sierpinski (1911)   
Bernstein (1912)   
Montel (1918)

For example, Bernstein’s proof is a discrete analogue of the argument just given: continuous diffusion is replaced by a random walk made precise by the notion of Bernstein polynomials (Exercise 6.4) [Bernstein 1912d]. Lebesgue’s proof, which appeared in his first paper published as a student at age 23, is based on reducing the approximation of general continuous functions to the approximation of $| x |$ (Exercise 6.5) [Lebesgue 1898]. Fej´er was an even younger student, age 20, when he published his proof based on Ces\`aro means (Exercise 6.6(a)) [Fej´er 1900], and he published a different proof years later based on Hermite–Fej´er interpolation (Exercise 6.6(b)) [Fej´er 1916]. This long list gives an idea of the great amount of mathematics stimulated by Weierstrass’s theorem and the significant role it played in the development of analysis in the early 20th century. For a fascinating presentation of this corner of mathematical history, see [Pinkus 2000].

Weierstrass’s theorem establishes that even extremely nonsmooth functions can be approximated by polynomials, functions like $x \sin ( x ^ { - 1 } )$ or even $\sin ( x ^ { - 1 } ) \sin ( 1 / \sin ( x ^ { - 1 } ) )$ . The latter function has an infinite number of points near which it oscillates infinitely often, as we begin to see from the plot below over the range [0.07, 0.4]. In this calculation Chebfun is called with a user-prescribed number of interpolation points, 30000, since the usual adaptive procedure has no chance of resolving the function to machine precision.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/756be56501e27c15923928c47a67e99435011337960d728fa84e898d2e29cf3a.jpg)

We can illustrate the idea of Weierstrass’s proof by showing the convolution of this complicated function with a Gaussian. First, here is the same function $f$ recomputed over a subinterval extending from one of its zeros to another:

a = 0.2885554757; b = 0.3549060246;   
$\boldsymbol { \tt { f } } 2 { \it { \Delta \phi } } =$ chebfun(@(x) sin(1/x)\*sin(1/sin(1/x)),[a,b],2000); plot(f2)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/3fbf3af31fbdfe1b929c7cdb3f715dd8626a285940e86e5fd70ea1db685ccd3f.jpg)

Here is a narrow Gaussian with integral 1:

$\scriptstyle { \mathrm { ~ t ~ } } = { \mathrm { ~ 1 } } \mathtt { e } - 7$ ;   
phi $=$ chebfun(@(x) exp(-x^2/(4\*t))/sqrt(4\*pi\*t),.003\*[-1 1]); plot(phi)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/3d9de49f557f2dd48979c8d49aa6ab15cfe8fd777d11b57b28e53c0340cadbc4.jpg)

Convolving the two gives a smoothed version of the close-up of $f$ . Notice how the short wavelengths vanish while the long ones are nearly undisturbed.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/7112b59880b548805bd95a1e245b4d6c774f2ccf38e34461aafa0e705afe4b29.jpg)

This is an entire function, which means it can be approximated by polynomials by truncating the Taylor series.

Weierstrass’s theorem has an important generalization to complex analytic functions. Suppose a function $f$ is defined on a compact set $K$ in the complex plane whose complement is connected (so $K$ cannot have any holes). Mergelyan’s theorem asserts that if $f$ is continuous on $K$ and analytic in the interior, then $f$ can be approximated on $K$ by polynomials [Mergelyan 1951, Gaier 1987]. The earlier Runge’s theorem is the weaker result in which $f$ is assumed to be analytic throughout $K$ , not just in the interior [Runge 1885a].

For all its beauty, power, and importance, the Weierstrass approximation theorem has in some respects served as an unfortunate distraction. Knowing that even troublesome functions can be approximated by polynomials, we naturally ask, How can we do it? A famous result of Faber and Bernstein asserts that there is no fixed array of grids of $1 , 2 , 3 , \ldots$ interpolation points, Chebyshev or otherwise, that achieves convergence as $n  \infty$ for all continuous $f$ [Faber 1914, Bernstein 1919]. So it becomes tempting to look at approximation methods that go beyond interpolation, and to warn people that interpolation is dangerous, and to try to characterize exactly what minimal properties of $f$ suffice to ensure that interpolation will work after all. A great deal is known about these subjects. The trouble with this line of research is that for almost all the functions encountered in practice, Chebyshev interpolation works beautifully! Weierstrass’s theorem has encouraged mathematicians over the years to give too much of their attention to pathological functions at the edge of discontinuity, leading to the bizarre and unfortunate situation where many books on numerical analysis caution their readers that interpolation may fail without mentioning that for functions with a little bit of smoothness, it succeeds outstandingly. For discussions of the history of such misrepresentations and misconceptions, see Chapter 14, Appendix A, and [Trefethen 2016].

Summary of Chapter 6. A continuous function on a bounded interval can be approximated arbitrarily closely by polynomials.

Exercise 6.1. A pathological function of Weierstrass. Weierstrass was one of the first to give an example of a function continuous but nowhere differentiable on $[ - 1 , 1 ]$ , and it is one of the early examples of a fractal [Weierstrass 1872]:

$$
w ( x ) = \sum _ { k = 0 } ^ { \infty } 2 ^ { - k } \cos ( 3 ^ { k } x ) .
$$

(a) Construct a chebfun w7 corresponding to this series truncated at $k = 7$ . Plot w7, its derivative (use diff), and its indefinite integral (cumsum). What is the degree of the polynomial defining this chebfun? (b) Prove that $w$ is continuous. (You can use the Weierstrass M-test.)

Exercise 6.2. Taylor series of an entire function. To illustrate the proof of the Weierstrass approximation theorem, we plotted a Gaussian kernel. The key point of the proof is that this kernel is entire, so its Taylor series converges for all $x$ . (a) For $x = 1$ at the given time $t = 1 0 ^ { - 7 }$ , how many terms of the Taylor series about $x = 0$ would you have to take before the terms fall below 1? Estimate the answer at least to within a factor of 2. You may find Stirling’s formula helpful. (b) Also for $x = 1$ and $t = 1 0 ^ { - 7 }$ , approximately how big is the biggest term in the Taylor series?

Exercise 6.3. Resolving a difficult function. Although the example function $f ( x ) = \sin ( 1 / x ) \sin ( 1 / \sin ( 1 / x ) )$ of this chapter is not Lipschitz continuous, its Chebyshev interpolants do in fact converge. Explore this phenomenon numerically by computing the degree $n$ Chebyshev interpolant to $f$ over the interval [0.07, 0.4] for $n + 1 = 4 , 8 , 1 6 , \dots , 2 ^ { 1 4 }$ and measuring the error in each case over a Chebyshev grid of $2 n$ points. Plot the results on a loglog scale. How do you think the error depends on $_ n$ as $n \to \infty$ ? Approximately how large would $_ n$ have to be to get 16-digit accuracy for this function over this interval?

Exercise 6.4. Bernstein’s proof. For $f \in C ( [ 0 , 1 ] )$ , the associated degree $_ n$ Bernstein polynomial is defined by

$$
B _ { n } ( x ) = \sum _ { k = 0 } ^ { n } f ( k / n ) { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } .
$$

Bernstein proved the Weierstrass approximation theorem by showing that $B _ { n } ( x )  f ( x )$ uniformly as $n \to \infty$ . (a) Give an interpretation of $B _ { n } ( x )$ involving a random walk driven by a coin which comes up heads with probability $_ x$ and tails with probability ${ \mathrm { ~ 1 ~ - ~ } } x$ . (b) Show that max $B _ { n } ( x ) \leq \operatorname* { m a x } f ( x )$ and $\operatorname* { m i n } B _ { n } ( x ) \geq \operatorname* { m i n } f ( x )$ for $x \in [ 0 , 1 ]$ .

Exercise 6.5. Lebesgue’s proof. (a) Show using uniform continuity that any $f \in$ $C ( [ - 1 , 1 ] )$ can be approximated uniformly by a polygonal curve, i.e., a function $g ( x )$ that is piecewise linear and continuous. (b) Show that such a function can be written in the form $\begin{array} { r } { g ( x ) = A + B x + \sum _ { k = 1 } ^ { m } C _ { k } | x - x _ { k } | } \end{array}$ . (c) Show that $| x |$ can be uniformly approximated by polynomials on $\lfloor - 1 , 1 \rfloor$ by truncating the binomial expansion

$$
| x | = [ 1 + ( x ^ { 2 } - 1 ) ] ^ { 1 / 2 } = \sum _ { n = 0 } ^ { \infty } { \binom { \frac { 1 } { 2 } } { n } } ( x ^ { 2 } - 1 ) ^ { n } .
$$

You may use without proof the fact that these binomial coefficients are of size $O ( n ^ { - 3 / 2 } )$ as $n \to \infty$ . (d) Explain how (a)–(c) combine to give a proof of the Weierstrass approximation theorem.

Exercise 6.6. Fej´er’s proofs. (a) In 1900 Fej´er proved the Weierstrass approximation theorem via Ces\`aro means. In the Chebyshev case, define $S _ { n }$ to be the mean of the partial sums of the Chebyshev series (3.11)–(3.12) of orders 0 through $n$ . Then it can be shown that $S _ { n } \ \to \ f$ uniformly as $n  \infty$ for any $f \in C ( [ - 1 , 1 ] )$ . Explore such approximations for $f ( x ) = e ^ { x }$ with various degrees $n$ . For this very smooth function $f$ , how does the accuracy compare with that of ordinary Chebyshev interpolants? (b) In 1916 Fej´er proved the theorem again by considering what are now known as Hermite–Fej´er interpolants: he showed that if $p _ { 2 n - 1 } \in \mathcal { P } _ { 2 n - 1 }$ is obtained by interpolating $f \in C ( [ - 1 , 1 ] )$ in the zeros of $T _ { n } ( x )$ and also setting $p ^ { \prime } ( x ) = 0$ at these points, then $p _ { 2 n - 1 } \to f$ uniformly as $n  \infty$ . Explore such interpolants numerically for various $n$ by using interp1 to construct polynomials $p 2 n - 1$ with $p _ { 2 n - 1 } ( x _ { j } ) = p _ { 2 n - 1 } ( x _ { j } + 1 0 ^ { - 6 } ) = \exp ( x _ { j } )$ . Again how does the accuracy compare with that of ordinary Chebyshev interpolants?

Exercise 6.7. Convergent series of polynomials. (a) Show that any $f \in C ( [ - 1 , 1 ] )$ ) can be written as a uniformly convergent series

$$
f ( \boldsymbol { x } ) = \sum _ { k = 0 } ^ { \infty } q _ { k } ( \boldsymbol { x } ) ,
$$

where each $q _ { k }$ is a polynomial of some degree. (b) Show that a series of this kind also exists for a function continuous on the whole real line, with pointwise convergence for all $_ x$ and uniform convergence on any bounded subset.
