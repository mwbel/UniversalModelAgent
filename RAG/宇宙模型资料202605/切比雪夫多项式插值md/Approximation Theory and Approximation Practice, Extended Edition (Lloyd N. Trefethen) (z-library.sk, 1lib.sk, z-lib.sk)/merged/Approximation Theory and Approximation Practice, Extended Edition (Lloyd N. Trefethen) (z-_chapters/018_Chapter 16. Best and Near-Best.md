# Chapter 16. Best and Near-Best

Traditionally, approximation theory has given a great deal of attention to best approximations in the $\infty$ -norm and rather less to alternatives such as Chebyshev interpolants. One might think that this is because best approximations are much better than the alternatives. However, this is not true.

In a moment we shall continue with Lebesgue constants to shed some light on this matter, but first, let us do some experiments. We start with the extreme case of a very smooth function, $\exp ( x )$ , and compare convergence of its Chebyshev interpolants $p$ and best approximants $p ^ { * }$ . (The difference between $n$ and $n { \mathrel { + { 1 } } }$ in this code is intentional, since chebfun takes as argument the number of interpolation points, whereas minimax takes the degree of the polynomial.)

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); nn = 0:15;   
errbest $=$ []; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\tt { n } { + } 1$ ),inf);   
end   
semilogy(nn,errcheb,'. $- \mathbf { r } ^ { \mathsf { \Pi } }$ ), hold on, semilogy(nn,errbest,'h-b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/dcbac3d9b6c7e7a7569f3845cfd830ce109c14ed6bb6c0ecfe1fd7215b78e87e.jpg)

Clearly the stars for $p ^ { * }$ aren’t much better than the dots for $p$ . The ratio of the two converges toward 2 until the rounding errors set in for larger degrees:

ratio $=$ errcheb./errbest; fprintf('%8d %12.5f\n',[nn; ratio])

<table><tr><td>n</td><td>ratio</td></tr><tr><td>0</td><td>1.46212</td></tr><tr><td>1</td><td>2.00000</td></tr><tr><td>2</td><td>1.74436</td></tr><tr><td>3</td><td>1.96807</td></tr><tr><td>4</td><td>1.94991</td></tr><tr><td>5</td><td>1.98188</td></tr><tr><td>6</td><td>1.98182</td></tr><tr><td>7</td><td>1.98861</td></tr><tr><td>8</td><td>1.99105</td></tr><tr><td>9</td><td>1.99222</td></tr><tr><td>10</td><td>1.99468</td></tr><tr><td>11</td><td>1.99259</td></tr><tr><td>12</td><td>1.97361</td></tr><tr><td>13</td><td>1.27028</td></tr><tr><td></td><td>0.25152</td></tr><tr><td>14</td><td></td></tr><tr><td>15</td><td>0.80000</td></tr></table>

At the other extreme of smoothness, consider $| x |$ :

f = abs(x); nn = [0 2 4 10 20 40 100 200];   
errbest $= ~ [ ]$ ; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\ n { + } 1 \cdot$ ),inf);   
end   
loglog( $\mathtt { n n } { + } 1$ ,errbest, $" \mathrm { h } - \mathrm { b } \cdot$ ) hold on, loglog( $\mathtt { n n } { + 1 }$ ,errcheb,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4a49b5ad3fff42464dff32d93fc5afe678c9e3a9140d55230772055eaa3dd915.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/6e6dc52df76454a7f7e350d0f95d05a8f379a23b984d35c5834e9ca9dfe04255.jpg)

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
