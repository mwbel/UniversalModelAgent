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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c2485d98d1a80c2864b8a6cd8d05ec41a23975b5db921503a3b8ebf78d9f0312.jpg)

By taking the absolute values of these curves, we see the largest possible effect at each point in $[ - 1 , 1 ]$ of data that is nonzero at just one point of the grid:

for $\texttt { k } = \texttt { 1 }$ :npts subplot(2,2,k), absp $=$ abs(p{k}); plot(absp), hold on, plot(s,absp(s),'.') plot(s(k),absp(s(k)),'hr')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f5113bb6133227a0e9fc82a6bf578a58b9ba4fd545535a2d67c1066c21f8186d.jpg)

Now let us add up these absolute values as in (15.3):

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); ${ \mathrm { ~ \cal ~ L ~ } } = { \mathrm { ~ 0 * x } }$ ; for k = 1:npts, $\mathrm { ~ L ~ } = \mathrm { ~ L ~ } +$ abs(p{k}); end plot(L), hold on, plot(s,L(s),'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d2748eece46b5b136215ab68be2ce0412085b849789dcfc188cf15a40251dcc0.jpg)

This is the Lebesgue function $\lambda ( x )$ , a piecewise polynomial, telling us the largest possible effect at each point $x \in [ - 1 , 1 ]$ of interpolating data of norm 1. The Lebesgue constant (15.4) is the height of the curve:

Lconst $=$ norm(L,inf)

Lconst $=$ 1.631130309440900

A code lebesgue for automating the above computation (actually based on a more efficient method) is included in Chebfun, and it optionally returns the Lebesgue constant as well as the Lebesgue function. Here are the results for 8 equispaced points:

s = linspace(-1,1,8); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 6.929739656126466

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/a708f71491e25c2aa7d3a3bffd7c7ba9f5579d6665b47c8495182bd2e9a4ba17.jpg)

And here they are for 12 points. Note that the Lebesgue constant has jumped from 7 to 51.

s = linspace(-1,1,12); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 51.214223185730020

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1e48e6558849edde9bb798b139902543923504e308c74e4d2af78825dcfcc7a4.jpg)

The function takes large values near $\pm 1$ , as we expect from Chapter 13 since the Runge phenomenon is associated with interpolants becoming very large near the endpoints. In fact the Lebesgue function for interpolation in equispaced points is more naturally displayed on a log scale. Here it is for $n = 3 0$ :

s $=$ linspace(-1,1,30); [L,Lconst] $=$ lebesgue(s); semilogy(L), hold on, semilogy(s,L(s),'.'), Lconst

Lconst $=$ 3.447738672687561e+06

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/8a180e83159c55efa5e7b8158b8cc89d5676cd62f056c235516a2498b1683ef7.jpg)

For comparison, here are the corresponding results for 4, 8, and 12 Chebyshev points, now back again on a linear scale.

for npts $=$ 4:4:12 s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst   
end

Lconst $=$ 1.666666666666667   
Lconst $=$ 2.202214555205528   
Lconst $=$ 2.489430376881968

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/07d20a576c0d8356d0f243252221d479ad7b31319cffbf96a6449b16680fb8e7.jpg)

Here are 100 Chebyshev points, with a comparison of the actual Lebesgue constant with the bound from Theorem 15.2:

$\mathtt { n p t s } ~ = ~ 1 0 0$ ; s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), Lconst, Lbound $=$ 1 + (2/pi)\*log(npts)

Lconst $=$ 3.887871431579913   
Lbound $=$ 3.931742395517711

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f4514cec933477f55fc1cf21c2cfc468af5d80ee5e0ff9c669eba4e15f452bfe.jpg)

The low height of this curve shows how stable Chebyshev interpolation is.

In Chapter 9 it was mentioned that combinations of Lagrange polynomials are the source of both the Gibbs phenomenon and the size of Lebesgue functions. Let us now explain this remark. To analyze the Gibbs oscillations near a step, we added up a succession of Lagrange polynomials with constant amplitude 1. Since a single Lagrange polynomial has an oscillatory inverse-linear tail, the sum corresponds to an alternating series that converges to a constant as $n \to \infty$ . Lebesgue functions, on the other hand, are defined by taking a maximum at each point on the grid. The maximum is achieved by adding up Lagrange polynomials with equal but alternating coefficients, so as to make the combined signs all equal. For example, on the 20- point Chebyshev grid, the maximum possible value of an interpolant is achieved at $x = 0$ by taking data with this pattern:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d3d42282ce745d2591889d8f130d63b6532a5d2a4437adc5c8f2bc84af934779.jpg)

Here is the Chebyshev interpolant:

p = chebfun(d); hold on, plot(p)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/b6c51ce0a0064ec698268ec5fe3d212feaac408e92b60400fc14de94f8175ad9.jpg)

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
