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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4538c54c3096c0ab991b7ee3c1f9d20e8d5c95ed7b5c2307d5607307f3648368.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/0f3a505ef380cf16e56ba97b6127b80e6ed487af6dbf61e4b795f24fa5999962.jpg)

In this example, $\mathrm { \Delta } _ { \mathrm { { P } } }$ was a polynomial from the start. The real power of Theorem 18.1, however, comes when it is applied to the problem of finding the roots on $[ - 1 , 1 ]$ of a general function $f$ . To do this, we first approximate $f$ by a polynomial and then find the roots of the polynomial. This idea was proposed in Good’s original 1961 paper [Good 1961]. In a more numerical era, it has been advocated in a number of papers by John Boyd, including [Boyd 2002], and it is exploited virtually every time Chebfun is used.

For example, here is the chebfun corresponding to $\cos ( 5 0 \pi x )$ on $[ - 1 , 1 ]$

It doesn’t take long to compute its roots, tic, r $=$ roots(f); toc

Elapsed time is 0.015067 seconds.

The exact roots of this function on $[ - 1 , 1 ]$ are $- 0 . 9 9 , - 0 . 9 7 , \hdots , 0 . 9 7 , 0 . 9 9$ . Inspecting a few of the computed results shows they are accurate to close to machine precision:


<!-- chunk 0003: pages 141-210 -->
ans $=$   
-0.990000000000000   
-0.970000000000000   
-0.950000000000000   
-0.930000000000000   
-0.910000000000000

Changing the function to $\cos ( 5 0 0 \pi x )$ makes the chebfun 10 times longer,

f = cos(500\*pi\*x); length(f)

ans $=$ 1685

One might think this would increase the rootfinding time greatly, since the number of operations for an eigenvalue computation grows with the cube of the matrix dimension. (The colleague matrix has a special structure that can be used to bring the operation count down to $O ( n ^ { 2 } )$ , but this is not done in a straightforward MATLAB call to eig.) However, an experiment shows that the timing is still quite good,

tic, r = roots(f); toc

Elapsed time is 0.151371 seconds.

and the accuracy is still outstanding:

r(1:5)

ans $=$   
-0.999000000000000   
-0.997000000000000   
-0.995000000000000   
-0.993000000000000   
-0.991000000000000

We can make sure all 1000 roots are equally accurate by computing a norm:

exact = [-0.999:0.002:0.999]'; norm(r-exact,inf)

ans $=$ 4.440892098500626e-16

The explanation of this great speed in finding the roots of a polynomial of degree in the thousands is that the complexity of the algorithm has been improved from $O ( n ^ { 3 } )$ to $O ( n ^ { 2 } )$ by recursion. If a chebfun has length greater than 50, the interval is divided recursively into subintervals, with a chebfun constructed on each subinterval of appropriately lower degree. Thus no eigenvalue problem is ever solved of dimension greater than 50. This idea of rootfinding based on recursive subdivision of intervals and Chebyshev eigenvalue problems was developed by John Boyd in the 1980s and 1990s and published by him in 2002 [Boyd 2002]. Details of the original

Chebfun implementation of roots were presented in [Battles 2005], and in 2012 the Chebfun algorithm was speeded up substantially by Pedro Gonnet (unpublished).

These techniques are remarkably powerful for practical computations. For example, how many zeros does the Bessel function $J _ { 0 }$ have in the interval $\lfloor 0 , 5 0 0 0 \rfloor$ ? Chebfun finds the answer in a fraction of a second:

tic, f $=$ chebfun(@(x) besselj(0,x),[0,5000]); r $=$ roots(f); toc, length(r)

Elapsed time is 0.320189 seconds. ans $=$ 1591

What is the 1000th zero?

r(1000)

ans $=$ 3.140807295225079e+03

We readily verify that this zero is an accurate one:

besselj(0,ans)

ans $=$ 6.531871585675192e-15

This example, like a few others scattered around the book, makes use of a chebfun defined on an interval other than the default $[ - 1 , 1 ]$ . The mathematics is straightforward; $[ 0 , 5 0 0 0 ]$ is reduced to $[ - 1 , 1 ]$ by a linear transformation.

Here is another illustration of recursive colleague matrix rootfinding for a highorder polynomial. The function

$$
f ( x ) = e ^ { x } [ { \mathrm { s e c h } } ( 4 \sin ( 4 0 x ) ) ] ^ { \exp ( x ) }
$$

features a row of narrower and narrower spikes. Where in $[ - 1 , 1 ]$ does it take the value 1? We can find the answer by using roots to find the zeros of the equation $f ( x ) - 1 = 0$ :

$\mathbf { f } \mathbf { f } \ = \ \mathcal { Q } \left( \mathbf { x } \right)$ exp(x).\*sech(4\*sin(40\*x)).^exp(x); tic, f $=$ ff(x); r = roots(f-1); toc plot(f), hold on, plot(r,f(r),'or')

Elapsed time is 0.195736 seconds.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/0b48e90ad038745cf2dc85330b880ea1dcc37fcf6e690f490ae7c13f326b03e9.jpg)

Notice that we have found the roots here of a polynomial of quite high degree:

length(f)

ans $=$ 3541

A numerical check confirms that the roots are accurate, max(abs(ff(r)-1))

ans $=$ 2.042810365310288e-13 and zooming in gives perhaps a more convincing plot:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/d7aeb998b15c2f7cfe5cf15561b54b1dcb51e22b29d7fd495ec943544f9d6f13.jpg)

Computations like this are examples of global rootfinding, a special case of global optimization. They are made possible by the combination of fast methods of polynomial approximation with the extraordinarily fast and accurate methods for matrix eigenvalue problems that have been developed in the time since Francis invented the QR algorithm in the very same year as Good proposed his colleague matrices [Francis 1961]. (A crucial algorithmic feature that makes these eigenvalue calculations so accurate is known as “balancing,” introduced in [Parlett & Reinsch 1969]—see [Toh & Trefethen 1994] and Exercise 18.3.)

Global rootfinding is a step in many other practical computations. It is used by Chebfun, for example, in computing minima, maxima, $\infty$ -norms, 1-norms, and absolute values.

It is worth mentioning that as an alternative to eigenvalue problems based on Chebyshev expansion coefficients, it is possible to relate roots of polynomials to eigenvalue problems (or generalized eigenvalue problems) constructed from function values themselves at Chebyshev or other points. Mathematical processes along these lines are described in [Fortune 2001], [Amiraslani et al. 2004], and [Amiraslani 2006]. So far there has not been much numerical exploitation of these ideas, but preliminary experiments suggest that in the long run they may be competitive.

We close this chapter by clarifying a point that may have puzzled the reader, and which has fascinating theoretical connections. In plots like the last two, we see only real roots of a function. Yet if the function is a chebfun based on a polynomial representation, won’t there be complex roots too? This is indeed the case, but the Chebfun roots command by default returns only those roots in the interval where the function is defined. As mentioned in Exercise 14.2, this default behavior can be overridden by the use of the flags 'all' or 'complex'. For example, suppose we make a chebfun corresponding to the function $f ( x ) = ( x - 0 . 5 ) / ( 1 + 1 0 x ^ { 2 } )$ , which has just one root in the complex plane, at $x = 0 . 5$ :

$\textbf { f } = \textbf { ( x - 0 . 5 ) } / ( 1 + 1 0 * \mathbf x \hat { \textbf { \ i } } 2 ) ; \ \mathrm { 1 e n g t h } ( \mathbf f )$

Typing roots alone gives just the root at $x = 0 . 5$ :

roots(f)

ans $=$ 0.500000000000006

With roots(f,’all’), however, we get 106 roots:

r = roots(f,'all'); length(r)

ans $=$ 106

The complex roots are meaningless from the point of view of the underlying function $f$ ; they are an epiphenomenon that arises in the process of approximating $f$ on $[ - 1 , 1 ]$ . A plot reveals that they have a familiar distribution, lying almost exactly on the Chebfun ellipse for this function:

chebellipseplot(f,'r'), hold on, plot(r,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/57ac6591ccdeeaeab82ef8458c6ddb46314a600434aa53bfd66d02cc6c4594cf.jpg)

The fact that roots of best and near-best approximations cluster along the maximum Bernstein ellipse of analyticity is a special case of a theorem due to Walsh [1959]. Blatt and Saff [1986] extended Walsh’s result to the situation in which the function being approximated has no ellipse of analyticity but is merely continuous on $[ - 1 , 1 ]$ . They showed that in this case, the zeros of the best approximants cluster at every point of the interval as $n  \infty$ . This phenomenon applies not only to the best approximations but to all near-best approximations that are maximally convergent as defined in Chapter 12, and hence in particular to Chebyshev interpolants. Here, for example, are the roots of the degree 100 Chebyshev interpolant to $| x |$ :

f = chebfun('abs(x)',101); length(f), r = roots(f,'all'); plot([-1,1],[0,0],'r'), hold on, plot(r,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/622668859309b51b0eb9398fbe20d615d1c1f022a582f796b0282e89cfaa2e20.jpg)

The Walsh and Blatt–Saff theorems are extensions of Jentzsch’s theorem, which asserts that the partial sums of a Taylor series have roots clustering along every point of the circle of convergence [Jentzsch 1914].

Summary of Chapter 18. The roots of a polynomial are equal to the eigenvalues of a colleague matrix formed from its coefficients in a Chebyshev series, tridiagonal except in the final row. This identity, combined with recursive subdivision, leads to a stable and efficient numerical method for computing roots of a polynomial in an interval. For orthogonal polynomials other than Chebyshev, the colleague matrix generalizes to a comrade matrix with the same almost-tridiagonal structure.

Exercise 18.1. Companion matrix. Prove that the roots of the polynomial $p ( x ) = a _ { 0 } +$ $a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ , $a _ { n } \neq 0$ , are the eigenvalues of the $n \times n$ matrix with zero entries everywhere except for the value 1 in the first superdiagonal and the values $- a _ { 0 } / a _ { n } , \ldots , - a _ { n - 1 } / a _ { n }$ in the last row.

Exercise 18.2. Four forms of colleague matrix. A matrix $C$ has the same eigenvalues and eigenvalue multiplicities as $C ^ { T }$ and also as $S C S ^ { - 1 }$ , where $S$ is any nonsingular matrix. Use these properties to derive three alternative forms of the colleague matrix in which the Chebyshev coefficients appear in (a) the first row, (b) the first column, and (c) the last column.

Exercise 18.3. Some forms more stable than others. Mathematically, all the matrices described in the last exercise have the same eigenvalues. Numerically, however, some may suffer more than others from rounding errors, and in fact Chebfun works with the first-column option for just this reason. (a) Determine the $1 1 \times 1 1$ colleague matrix corresponding to roots $- 1 , - 0 . 8 , - 0 . 6 , \dots , 1$ . Get the entries of the matrix exactly, either analytically or by intelligent guesswork based on the MATLAB rat command. (b) How does the accuracy of the eigenvalues of the four matrix variants compare? Which one is best? Is the difference significant? (c) What happens if you solve the four eigenvalue problems again using the MATLAB 'nobalance' option in the eig command?

Exercise 18.4. Legendre polynomials. The Legendre polynomials satisfy $P _ { 0 } ( x ) = 1$ , $P _ { 1 } ( x ) = x$ , and, for $k \geq 1$ , the recurrence relation (17.6). (a) Derive a “comrade matrix” analogue of Theorem 18.1 for the roots of a polynomial expanded as a linear combination of Legendre polynomials. (b) Verify numerically that the roots of the particular polynomial $P _ { 0 } + P _ { 1 } + \cdots + P _ { 5 }$ match the prediction of your theorem. (Try sum(legpoly(0:5),2) to construct this polynomial elegantly in Chebfun and don’t forget to use roots(...,'all').) Exercise 18.5. Complex roots. For each of the following functions defined on $[ - 1 , 1 ]$ , construct corresponding chebfuns and plot all their roots in the complex plane with plot(roots(f,'all')). Comment on the patterns you observe. (Your comments are not expected to go very deep.) (a) $x ^ { 2 0 } - 1$ , (b) $\exp ( x ) ( x ^ { 2 0 } - 1 )$ , (c) $1 / ( 1 + 2 5 x ^ { 2 } )$ , (d $x \exp ( 3 0 i x )$ , (e) $\sin ( 1 0 \pi x )$ , (f) $\sqrt { 1 . 1 - x }$ , (g) an example of your own choosing.

Exercise 18.6. The Szeg˝o curve. If $f$ is entire, then it has no maximal Bernstein ellipse of analyticity. Plot the roots in the complex $_ x$ -plane of the Chebfun polynomial approximation to $e ^ { x }$ on $[ - 1 , 1 ]$ and, for comparison, the “Szeg˝o curve” defined by $| x e ^ { 1 - x } | =$ 1 and $| x | \le 1$ [Szeg˝o 1924, Saff & Varga 1978b, Pritsker & Varga 1997]. More precisely, for the comparison, rescale the Szeg˝o curve by multiplying it by the polynomial degree.

Exercise 18.7. Roots of random polynomials. (a) Use the MATLAB roots command to plot the roots of a polynomial $p ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { 2 0 0 } z ^ { 2 0 0 }$ with coefficients selected from the standard normal distribution. (b) Use chebfun('randn(201,1)','coeffs') and plot(roots(p,'all')) to plot the roots of a polynomial $p ( x ) = a _ { 0 } T _ { 0 } + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot +$ $a _ { 2 0 0 } T _ { 2 0 0 } ( x )$ with the same kind of random coefficients. (Effects like these are analyzed rigorously in [Shiffman & Zelditch 2003].)
