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

![](images/0b48e90ad038745cf2dc85330b880ea1dcc37fcf6e690f490ae7c13f326b03e9.jpg)

Notice that we have found the roots here of a polynomial of quite high degree:

length(f)

ans $=$ 3541

A numerical check confirms that the roots are accurate, max(abs(ff(r)-1))

ans $=$ 2.042810365310288e-13 and zooming in gives perhaps a more convincing plot:

![](images/d7aeb998b15c2f7cfe5cf15561b54b1dcb51e22b29d7fd495ec943544f9d6f13.jpg)

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

![](images/57ac6591ccdeeaeab82ef8458c6ddb46314a600434aa53bfd66d02cc6c4594cf.jpg)

The fact that roots of best and near-best approximations cluster along the maximum Bernstein ellipse of analyticity is a special case of a theorem due to Walsh [1959]. Blatt and Saff [1986] extended Walsh’s result to the situation in which the function being approximated has no ellipse of analyticity but is merely continuous on $[ - 1 , 1 ]$ . They showed that in this case, the zeros of the best approximants cluster at every point of the interval as $n  \infty$ . This phenomenon applies not only to the best approximations but to all near-best approximations that are maximally convergent as defined in Chapter 12, and hence in particular to Chebyshev interpolants. Here, for example, are the roots of the degree 100 Chebyshev interpolant to $| x |$ :

f = chebfun('abs(x)',101); length(f), r = roots(f,'all'); plot([-1,1],[0,0],'r'), hold on, plot(r,'.')

![](images/622668859309b51b0eb9398fbe20d615d1c1f022a582f796b0282e89cfaa2e20.jpg)

The Walsh and Blatt–Saff theorems are extensions of Jentzsch’s theorem, which asserts that the partial sums of a Taylor series have roots clustering along every point of the circle of convergence [Jentzsch 1914].

Summary of Chapter 18. The roots of a polynomial are equal to the eigenvalues of a colleague matrix formed from its coefficients in a Chebyshev series, tridiagonal except in the final row. This identity, combined with recursive subdivision, leads to a stable and efficient numerical method for computing roots of a polynomial in an interval. For orthogonal polynomials other than Chebyshev, the colleague matrix generalizes to a comrade matrix with the same almost-tridiagonal structure.

Exercise 18.1. Companion matrix. Prove that the roots of the polynomial $p ( x ) = a _ { 0 } +$ $a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ , $a _ { n } \neq 0$ , are the eigenvalues of the $n \times n$ matrix with zero entries everywhere except for the value 1 in the first superdiagonal and the values $- a _ { 0 } / a _ { n } , \ldots , - a _ { n - 1 } / a _ { n }$ in the last row.

Exercise 18.2. Four forms of colleague matrix. A matrix $C$ has the same eigenvalues and eigenvalue multiplicities as $C ^ { T }$ and also as $S C S ^ { - 1 }$ , where $S$ is any nonsingular matrix. Use these properties to derive three alternative forms of the colleague matrix in which the Chebyshev coefficients appear in (a) the first row, (b) the first column, and (c) the last column.

Exercise 18.3. Some forms more stable than others. Mathematically, all the matrices described in the last exercise have the same eigenvalues. Numerically, however, some may suffer more than others from rounding errors, and in fact Chebfun works with the first-column option for just this reason. (a) Determine the $1 1 \times 1 1$ colleague matrix corresponding to roots $- 1 , - 0 . 8 , - 0 . 6 , \dots , 1$ . Get the entries of the matrix exactly, either analytically or by intelligent guesswork based on the MATLAB rat command. (b) How does the accuracy of the eigenvalues of the four matrix variants compare? Which one is best? Is the difference significant? (c) What happens if you solve the four eigenvalue problems again using the MATLAB 'nobalance' option in the eig command?

Exercise 18.4. Legendre polynomials. The Legendre polynomials satisfy $P _ { 0 } ( x ) = 1$ , $P _ { 1 } ( x ) = x$ , and, for $k \geq 1$ , the recurrence relation (17.6). (a) Derive a “comrade matrix” analogue of Theorem 18.1 for the roots of a polynomial expanded as a linear combination of Legendre polynomials. (b) Verify numerically that the roots of the particular polynomial $P _ { 0 } + P _ { 1 } + \cdots + P _ { 5 }$ match the prediction of your theorem. (Try sum(legpoly(0:5),2) to construct this polynomial elegantly in Chebfun and don’t forget to use roots(...,'all').) Exercise 18.5. Complex roots. For each of the following functions defined on $[ - 1 , 1 ]$ , construct corresponding chebfuns and plot all their roots in the complex plane with plot(roots(f,'all')). Comment on the patterns you observe. (Your comments are not expected to go very deep.) (a) $x ^ { 2 0 } - 1$ , (b) $\exp ( x ) ( x ^ { 2 0 } - 1 )$ , (c) $1 / ( 1 + 2 5 x ^ { 2 } )$ , (d $x \exp ( 3 0 i x )$ , (e) $\sin ( 1 0 \pi x )$ , (f) $\sqrt { 1 . 1 - x }$ , (g) an example of your own choosing.

Exercise 18.6. The Szeg˝o curve. If $f$ is entire, then it has no maximal Bernstein ellipse of analyticity. Plot the roots in the complex $_ x$ -plane of the Chebfun polynomial approximation to $e ^ { x }$ on $[ - 1 , 1 ]$ and, for comparison, the “Szeg˝o curve” defined by $| x e ^ { 1 - x } | =$ 1 and $| x | \le 1$ [Szeg˝o 1924, Saff & Varga 1978b, Pritsker & Varga 1997]. More precisely, for the comparison, rescale the Szeg˝o curve by multiplying it by the polynomial degree.

Exercise 18.7. Roots of random polynomials. (a) Use the MATLAB roots command to plot the roots of a polynomial $p ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { 2 0 0 } z ^ { 2 0 0 }$ with coefficients selected from the standard normal distribution. (b) Use chebfun('randn(201,1)','coeffs') and plot(roots(p,'all')) to plot the roots of a polynomial $p ( x ) = a _ { 0 } T _ { 0 } + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot +$ $a _ { 2 0 0 } T _ { 2 0 0 } ( x )$ with the same kind of random coefficients. (Effects like these are analyzed rigorously in [Shiffman & Zelditch 2003].)

# Chapter 19. Clenshaw–Curtis and Gauss Quadrature

One thing that is famous about Legendre points and polynomials is their connection with Gauss quadrature, invented by Gauss [1814]. Chebyshev points, similarly, are the basis of Clenshaw–Curtis quadrature [Clenshaw & Curtis 1960], and equispaced points are the basis of Newton–Cotes quadrature. Quadrature is the standard term for the numerical calculation of integrals. It is one of the areas where approximation theory has an immediate link to applications, as we shall see in Theorems 19.3–19.5.

In the basic quadrature problem, we are given a function $f \in C ( [ - 1 , 1 ] )$ and wish to calculate

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x .
$$

(More generally the integral may include a weight function $w ( x )$ as in (17.1).) There is a standard idea for doing this that is the basis of the Gauss, Clenshaw–Curtis, and Newton–Cotes formulas and many others besides. Given $n \geq 0$ , we sample $f$ at a certain set of $n + 1$ distinct nodes $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ . We then approximate $I$ by $I _ { n }$ , the exact integral of the degree $n$ polynomial interpolant $p _ { n }$ of $f$ in these nodes:

$$
I _ { n } = \int _ { - 1 } ^ { 1 } p _ { n } ( x ) d x .
$$

One might wonder, Why use a polynomial rather than some other interpolant? This is a very good question, and in Chapter 22 we shall see that other interpolants may in fact be up to $\pi / 2$ times more efficient. Nevertheless, polynomial interpolants have been the standard idea in numerical quadrature since the 18th century.

To integrate $p _ { n }$ , we do not construct it explicitly. Instead, $I _ { n }$ is computed from

the formula

$$
I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) ,
$$

where the numbers $w _ { 0 } , \ldots , w _ { n }$ are a set of $n + 1$ weights that have been predetermined so that the value of $I _ { n }$ will come out right. From (5.1) it is clear that the weights must be the integrals of the Lagrange polynomials,

$$
w _ { k } = \int _ { - 1 } ^ { 1 } \ell _ { k } ( x ) d x .
$$

Another way to write (19.3) is to say that $I _ { n }$ is given by an inner product,

$$
I _ { n } = w ^ { T } v ,
$$

where $w$ and $\boldsymbol { v }$ are column vectors of the weights $w _ { k }$ and function values $f ( x _ { k } )$ . Any linear process of computing an approximate integral from $n + 1$ sample points must be representable in this inner product form, and the integration of polynomial interpolants is a linear process. The mapping from $\{ f ( x _ { k } ) \}$ to $I _ { n }$ is a linear functional (Exercise 19.1).

When the weights $\{ w _ { k } \}$ of a quadrature formula (19.3) are determined by the principle of integrating the polynomial interpolant, i.e., by (19.4), the formula is said to be interpolatory. (Logically, the term should really be polynomial interpolatory.) For the following theorem, we say that a formula is exact when applied to $f$ if the result it gives is the exactly correct integral of $f$ .

Theorem 19.1. Polynomial degree of quadrature formulas. For any $n \geq 0$ , an $( n + 1 )$ -point interpolatory quadrature formula such as Clenshaw–Curtis, Gauss, or Newton–Cotes is exact for $f \in \mathcal { P } _ { n }$ . The $( n + 1 )$ -point Gauss formula is exact for $f \in \mathscr { P } _ { 2 n + 1 }$ .

Proof. Since an interpolatory formula is constructed by integration of a polynomial interpolant of degree $n$ , it is immediate that it is exact for $f \in \mathcal { P } _ { n }$ . The nontrivial property to be established is that Gauss quadrature achieves more than this, being exact for polynomials all the way up to degree $2 n + 1$ . The following standard argument, based on orthogonal polynomials, comes from [Jacobi 1826]. Gauss’s original work 12 years earlier made use of continued fractions rather than orthogonal polynomials.

Suppose that $f \in \mathcal { P } _ { 2 n + 1 }$ . Such a function can be written in the form $f ( x ) =$ $P _ { n + 1 } ( x ) q _ { n } ( x ) + r _ { n } ( x )$ , where $P _ { n + 1 }$ is the $( n + 1 ) \mathrm { s t }$ Legendre polynomial and $q _ { n } , r _ { n } \in$ $\mathcal { P } _ { n }$ . This implies

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x = \int _ { - 1 } ^ { 1 } P _ { n + 1 } ( x ) q _ { n } ( x ) d x + \int _ { - 1 } ^ { 1 } r _ { n } ( x ) d x .
$$

The first of the integrals on the right is zero because of the orthogonality property of Legendre polynomials, leaving us with

$$
I = \int _ { - 1 } ^ { 1 } r _ { n } ( x ) d x .
$$

Now consider $I _ { n }$ , the $( n + 1 )$ -point Gauss quadrature approximation to $I$ . The nodes of this formula are the zeros of $P _ { n + 1 } ( x )$ . Accordingly, at each node $x _ { k }$ we have $f ( x _ { k } ) = r _ { n } ( x _ { k } )$ . Thus the value $I _ { n }$ the Gauss formula gives for $f$ will be the same as the value it gives for $r _ { n }$ . But $\boldsymbol { r } _ { n } \in \mathcal { P } _ { n }$ , so this value is exactly the integral of $r _ { n }$ , that is, ${ \boldsymbol { I } } _ { n } = { \boldsymbol { I } }$ .

Theorem 19.1 is famous, but we shall see that it is misleading. It suggests that there is a significant gap between Clenshaw–Curtis and Newton–Cotes quadrature, with one rate of convergence, and Gauss quadrature, with a rate twice as high. In fact, the great gap is between Newton–Cotes, which does not converge at all in general, and both Clenshaw–Curtis and Gauss, which converge for every continuous $f$ and do so typically at similar rates. The crucial distinction is that the weights $w _ { k }$ for both the Clenshaw–Curtis and the Gauss formulas are positive [Imhof 1963], whereas for Newton–Cotes they oscillate in sign and diverge to $\infty$ (Exercise 19.9).

First, let us give some more details of the Clenshaw–Curtis and Gauss formulas. For Clenshaw–Curtis quadrature, one way to compute $I _ { n }$ is by constructing the weight vector $w$ explicitly. It can be shown that the weights are all positive and sum to 2 (the same properties also hold for Gauss quadrature weights, whose computation we discuss later in the chapter). From a practical point of view, this approach may be advantageous for integrating a collection of functions on a single Chebyshev grid. There is a classical formula for calculation of the weights with $O ( n ^ { 2 } )$ operations [Davis $\&$ Rabinowitz 1984, Trefethen 2000], and it is also possible to compute the weights faster, in $O ( n \log n )$ operations, using the FFT [Waldvogel 2006]. This fast algorithm is invoked by Chebfun when the command chebpts is called with two arguments, as we illustrate with $n + 1 = 3$ :

[nodes,weights] $=$ chebpts(3)

0.333333333333333 1.333333333333333 0.333333333333333

By increasing 3 to one million we see the speed of Waldvogel’s algorithm:

tic, [nodes,weights] $=$ chebpts(1000000); toc

Elapsed time is 0.108811 seconds.

The other way to carry out Clenshaw–Curtis quadrature, simplest when just one or a small number of integrands are involved, is to use the FFT to transform the problem to coefficient space (see Chapter 3) at a cost of $O ( n \log n )$ operations per integrand. (This idea was not proposed by Clenshaw and Curtis, who wrote before the rediscovery of the FFT in 1965, but by Morven Gentleman a few years later [Gentleman 1972a, 1972b].) To see how this works, we observe that the integral of the Chebyshev polynomial $T _ { k }$ from $^ { - 1 }$ to $1$ is zero if $k$ is odd and

$$
\int _ { - 1 } ^ { 1 } T _ { k } ( x ) d x = { \frac { 2 } { 1 - k ^ { 2 } } }
$$

if $k$ is even (Exercise 19.6). This gives us the following theorem, the basis of the FFT realization of Clenshaw–Curtis quadrature.

Theorem 19.2. Integral of a Chebyshev series. The integral of a degree $n$ polynomial expressed as a Chebyshev series is

$$
\int _ { - 1 } ^ { 1 } \sum _ { k = 0 } ^ { n } c _ { k } T _ { k } ( x ) d x \ = \quad \sum _ { k = 0 , k { \mathrm { e v e n } } } ^ { n } { \frac { 2 c _ { k } } { 1 - k ^ { 2 } } } .
$$

Proof. The proof follows from (19.6).

Chebfun applies Theorem 19.2 every time one types sum(f), and this theorem is also the basis of Waldvogel’s algorithm mentioned above.

By combining (19.6) with Theorems 8.1 and 19.1, we can now write down a theorem about the geometric convergence of Clenshaw–Curtis and Gauss quadrature for analytic integrands. For Gauss quadrature, this estimate is due to Rabinowitz [1969], and the extension to Clenshaw–Curtis can be found in [Trefethen 2008]. This result is fundamental and very important. For analytic integrands, the Gauss and Clenshaw–Curtis formulas converge geometrically. Every numerical analysis textbook should state this fact.

Theorem 19.3. Quadrature formulas for analytic integrands. Let a function $f$ be analytic in $[ - 1 , 1 ]$ and analytically continuable to the open Bernstein ellipse $E _ { \rho }$ , where it satisfies $| f ( z ) | \leq M$ for some $M$ . Then $( n + 1 )$ -point Clenshaw– Curtis quadrature with $n \geq 2$ applied to $f$ satisfies

$$
| I - I _ { n } | \leq { \frac { 6 4 } { 1 5 } } { \frac { M \rho ^ { 1 - n } } { \rho ^ { 2 } - 1 } }
$$

and $( n + 1 )$ -point Gauss quadrature with $n \geq 1$ satisfies

$$
\left. I - I _ { n } \right. \leq \frac { 6 4 } { 1 5 } \frac { M \rho ^ { - 2 n } } { \rho ^ { 2 } - 1 } .
$$

The factor $\rho ^ { 1 - n }$ in (19.7) can be improved to $\rho ^ { - n }$ if $n$ is even, and the factor 64/15 can be improved to 144/35 if $n \geq 4$ in (19.7) or $n \geq 2$ in (19.8).

Proof. If the constants 64/15 are increased to 8 and $\rho ^ { 2 } - 1$ is reduced to $\rho - 1$ , these conclusions can be obtained as corollaries of Theorem 8.2. The key is to note that the error in integrating $f$ will be the same as the error in integrating $f - f _ { n }$ . Applying the triangle inequality, this gives us

$$
| I - I _ { n } | \leq | I ( f - f _ { n } ) | + | I _ { n } ( f - f _ { n } ) | .
$$

By Theorem 8.2, $| ( f - f _ { n } ) ( x ) | \leq 2 M \rho ^ { - n } / ( \rho - 1 )$ for each $| x |$ . Since the interval $[ - 1 , 1 ]$ has length 2, this implies

$$
\vert I ( f - f _ { n } ) \vert \leq \frac { 4 M \rho ^ { - n } } { \rho - 1 } .
$$

In addition to this, there also holds the analogous property

$$
\left| I _ { n } ( f - f _ { n } ) \right| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

This follows from the fact that the weights are positive.

To get the sharper results stated, we use an additional fact: both Gauss and Clenshaw–Curtis formulas get the right answer, namely zero, when integrating an odd function. In particular the error is zero in integration of $T _ { k } ( x )$ for any odd $k$ . Now by Theorem 19.1, Gauss quadrature is exact through the term of degree $2 n + 1$ in the Chebyshev expansion of $f$ . Since odd terms do not contribute, we see that the error in integrating $f$ by $( n + 1 )$ -point Gauss quadrature will thus be the error in integrating

$$
a _ { 2 n + 2 } T _ { 2 n + 2 } ( x ) + a _ { 2 n + 4 } T _ { 2 n + 4 } ( x ) + \cdot \cdot \cdot ,
$$

a series in which the smallest index that appears is at least 4. Now by (19.6), the true integral of $T _ { k }$ for $k \geq 4$ is of magnitude at most 2/15. When $T _ { k }$ is integrated over $[ - 1 , 1 ]$ by the Gauss quadrature formula, the result will be of magnitude at most 2 since the weights are positive and add up to 2. Thus the error in integrating each $T _ { k }$ is at most $2 + 2 / 1 5 = 3 2 / 1 5$ . Combining this estimate with the bound $| a _ { k } | \leq 2 M \rho ^ { - k }$ of Theorem 8.1 gives (19.8). The argument for (19.7) is analogous. For the improvement from 64/15 to 144/35, see Exercise 19.5.

Just as Theorem 19.3 follows from the results of Chapter 8 for analytic integrands, there is an analogous result for differentiable integrands based on the results of Chapter 7.

Theorem 19.4. Quadrature formulas for differentiable integrands. For any $f \in C ( [ - 1 , 1 ] )$ , both the Clenshaw–Curtis and Gauss approximations $I _ { n }$ converge to the integral $I$ as $n  \infty$ . For an integer $\nu \geq 1$ , let $f$ and its derivatives through $f ^ { ( \nu - 1 ) }$ be absolutely continuous on $[ - 1 , 1 ]$ and suppose the νth derivative $f ^ { ( \nu ) }$ is of bounded variation $V$ . Then $( n + 1 )$ -point Clenshaw–Curtis quadrature applied to $f$ satisfies

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( n - \nu ) ^ { \nu } }
$$

for $n > \nu$ and $( n + 1 )$ -point Gauss quadrature satisfies

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( 2 n + 1 - \nu ) ^ { \nu } }
$$

for $n \geq \nu / 2$ .

Proof. The first assertion, for arbitrary continuous $f$ , is due to Stieltjes [1884]. As for (19.9) and (19.10), these can be derived as in the previous proof, but now using Theorem 7.2.

Here is a numerical example, the integration of the function (18.1) with a sequence of spikes:

$$
I = \int _ { - 1 } ^ { 1 } e ^ { x } [ { \mathrm { s e c h } } ( 4 \sin ( 4 0 x ) ) ] ^ { \mathrm { e x p } ( x ) } d x
$$

$\mathbf { f } \mathbf { f } \ = \ \mathcal { Q } \left( \mathbf { x } \right)$ exp(x).\*sech(4\*sin(40\*x)).^exp(x);$\mathrm { ~ x ~ } =$ chebfun $( \mathbf { \partial } ^ { \prime } \mathbf { x } ^ { \prime } )$ ; f $=$ ff(x); plot(f)

![](images/23226133b7fe630874e30104b8115d38e008ccede804b35a99658e2c5102e39a.jpg)

The corresponding chebfun is not exactly short:

length(f)

ans $=$ 3541

Nevertheless, Chebfun computes the integral in a fraction of a second:

sum(f)

ans = 0.543384000907901

Now let us look at Gauss quadrature. The nodes for the $( n + 1 )$ -point Gauss formula are the roots of the Legendre polynomial $P _ { n + 1 } ( x )$ . A good method for computing these numbers is implicit in Theorem 18.1 and the comment after it. According to that theorem, the roots of a polynomial expressed as a Chebyshev series are equal to the eigenvalues of a colleague matrix whose structure is tridiagonal apart from a nonzero final row. If the Chebyshev series reduces to the single polynomial $T _ { n + 1 }$ , the matrix reduces to tridiagonal without the extra row. Similarly the roots of a polynomial expressed as a series in Legendre polynomials are the eigenvalues of a comrade matrix, which is again tridiagonal except for a final row, and for the roots of $P _ { n + 1 }$ itself, the matrix reduces to tridiagonal. When symmetrized, this matrix is called a Jacobi matrix (Exercise 19.7). The classic numerical algorithm for implementing Gauss quadrature formulas comes from Golub and Welsch in 1969, who showed that the weights as well as the nodes can be obtained by solving the eigenvalue problem for this Jacobi matrix [Golub $\&$ Welsch 1969]. The Golub– Welsch algorithm can be coded in six lines of MATLAB (see gauss.m in [Trefethen 2000]), and the operation count is in principle $O ( n ^ { 2 } )$ , although it is $O ( n ^ { 3 } )$ in the simple implementation since MATLAB does not offer a command to exploit the tridiagonal structure of the eigenvalue problem.

For larger values of $n$ , a much faster alternative algorithm was introduced by Glaser, Liu, and Rokhlin [2007], based on numerical solution of certain linear ordinary differential equations by high-order Taylor series approximations combined with Newton iteration. This GLR algorithm shrank the operation count dramatically to $O ( n )$ and became the default algorithm invoked by Chebfun during 2009– 2012 when the legpts command was called with two output arguments. Most recently even faster algorithms have been introduced by Hale and Townsend [2013] and Bogaert [2014]. The key idea of the Hale–Townsend algorithm is to start from high-accuracy asymptotic approximations for nodes and then take one or two Newton steps, with $P _ { n }$ and $P _ { n } ^ { \prime }$ evaluated to machine precision by known asymptotic formulas. When $n$ is large enough, one may not even need any Newton steps at all. A crucial feature is that the method treats the nodes independently, so that it vectorizes readily, and this is a primary reason why it is approximately 20 times faster than the GLR algorithm in a MATLAB implementation.

Following the illustration of Clenshaw–Curtis quadrature earlier, here are nodes and weights for Gauss quadrature with $n + 1 = 3$ :

[nodes,weights] = legpts(3)   
nodes $=$ -0.774596669241483 0 0.774596669241483   
weights $=$ 0.555555555555556 0.888888888888889 0.555555555555556

And here is the time it takes to compute Gauss quadrature nodes and weights for one million points, about the same as for Clenshaw–Curtis:

tic, [nodes,weights] $=$ legpts(1000000); toc

Elapsed time is 0.089773 seconds.

For example, here is the integral (19.11) computed by $n$ -point Gauss quadrature for various values of $n$ . We write $\mathtt { w } { * } \mathtt { f f } \left( \mathtt { s } \right)$ rather than $\kappa ^ { \prime } { \ast } \mathbf { f } \mathbf { f } \left( \mathbf { s } \right)$ since $w$ as returned by legpts is a row vector, not a column vector.

for $\texttt { n } = \phantom { - } 5 0 0 : 5 0 0 : 1 5 0 0$ tic, $[ \mathbf { s } , \mathbf { w } ] ~ = ~ \mathrm { { 1 e g p t s } } \left( \mathrm { { n + 1 } } \right) ; ~ \mathrm { { 1 } } ~ = ~ \mathsf { w } { * } \mathbf { f } \mathsf { f } \left( \mathbf { s } \right) ; ~ \mathsf { t } ~ = ~ \mathsf { t o c } ;$ fprintf $\because n = \% 4 d$ , $\mathrm { ~ I ~ } = \ \% 1 6 . 1 4 \pounds$ , time $=$ %6.4f\n',n,I,t)   
end

$$
\begin{array} { r l r l } & { \mathtt { n } = } & { 5 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 9 2 7 5 8 1 0 6 2 2 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 1 8 } \\ & { \mathtt { n } = } & { 1 0 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 8 4 0 0 1 8 2 5 5 8 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 2 7 } \\ & { \mathtt { n } = } & { 1 5 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 8 4 0 0 0 9 0 7 8 4 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 3 7 } \end{array}
$$

Gauss quadrature has not often been employed for numbers of nodes in the thousands, because with traditional algorithms the computations are too expensive. It is clear from this experiment that the GLR and Hale–Townsend algorithms make such computations feasible after all.

So is Gauss quadrature the formula of choice? In particular, how does it compare with Clenshaw–Curtis quadrature as $n \to \infty$ ? As mentioned above, the traditional expectation, based on Theorem 19.1 and seemingly supported by Theorems 19.3 and 19.4, is that Gauss should converge twice as fast as Clenshaw–Curtis. However, numerical experiments show that the truth is not so simple. We begin with the easy integrand $f ( x ) = \exp ( - 1 0 0 x ^ { 2 } )$ .

er $\begin{array} { r l } { = } & { \Theta ( \mathbf { x } ) \ \exp \left( { - 1 0 0 * \mathbf { x } . \hat { \phantom { . } } \mathrm { \hat { \Phi } } ^ { 2 } } \right) ; \mathrm { ~ I ~ \ = ~ \mathbf { s u m } ( \mathrm { c h e b f u n } ( \mathrm { g g } ) ) } ; } \\ { \mathrm { r c c } = } & { [ ] ; \mathrm { ~ e r r g a u s s \ = ~ [ ] ~ ; ~ \boldsymbol { n } = ~ \boldsymbol { \Omega } [ \hat { \omega } , ~ \boldsymbol { n } = ~ \boldsymbol { \Omega } _ 2 : 2 : 8 0 } ; } \\ { \mathrm { ~ r ~ \hat { \omega } ~ \in ~ \boldsymbol { n } { \operatorname { m } } ~ \hat { \omega } ~ } } \\ { \mathrm { ~ I c c ~ = ~ \boldsymbol { s u m } ( \mathrm { c h e b f u n } ( \mathrm { g g } , \boldsymbol { n } + 1 ) ) ; ~ e r r c c } = } & { \left[ { \mathrm { e r r c c } \ \mathrm { \hat { \omega } a b s } \left( \mathrm { I - I c c } \right) } \right] ; } \\ { \mathrm { ~ \hat { \omega } , \tilde { \boldsymbol { u } } ] ~ = ~ \mathbf { 1 } e g p t s ( \boldsymbol { n } + 1 ) ; ~ \hat { \omega } ~ } } \\ { \mathrm { ~ I g a u s s \ = ~ \mathbf { w } * g g ( \hat { \omega } s ) } ; \mathrm { ~ e r r g a u s s \ = ~ \begin{array} { l } { \left[ \mathrm { e r r g a u s s } \ { a b s } \ { ( \mathrm { I - I g a u s s } ) } \right] ; } \\ { \mathrm { ~ e r r g a u s s } \ \mathrm { a b s } \ ( \mathrm { I - I g a u s s } ) } \end{array} } } \end{array}$ fo   
end   
semilogy(nn,errcc,'.-'), hold on, semilogy(nn,errgauss,'h-m')

![](images/639b448a0f07d31574bc929f9f98732f9f97b44ce42c761b34b656ee01eca676.jpg)

This behavior is typical: for smaller values of $n$ , Clenshaw–Curtis (dots) and Gauss quadrature (stars) have similar accuracy, not a difference of a factor of 2. This effect was pointed out by Clenshaw and Curtis in their original paper [1960]. Only at a sufficiently large value of $n$ , if the integrand is analytic, does a kink appear in the Clenshaw–Curtis convergence curve, whose further convergence is then about half as fast as before. An explanation of this effect based on ideas of rational approximation is given in Figures 4–6 of [Trefethen 2008], and another explanation based on aliasing can be derived from Theorems 4.2 and 19.2 and goes back to O’Hara and Smith [1968] (Exercise 19.4). For a full analysis, see [Weideman $\&$ Trefethen 2007a].

Here is a similar comparison for the harder integral (19.11):

I = sum(f); $\mathtt { n n } \ = \ 5 0 : 5 0 : 2 0 0 0$ ;   
errcc $= ~ [ ]$ ; errgauss $=$ [];   
for $\texttt { n } = \texttt { n n }$ Icc $=$ sum(chebfun(ff, $\tt { n } { + } 1 \tt {  }$ )); errcc $=$ [errcc abs(I-Icc)]; [s,w] = legpts $\left( \mathtt { n } + 1 \right)$ ; Igauss $=$ w\*ff(s); errgauss $=$ [errgauss abs(I-Igauss)];   
end   
semilogy(nn,errcc,'.-'), hold on, semilogy(nn,errgauss,'h-m')

![](images/ae74f1a813ebbd75928cab325bc2c247f387fd0a9f4ee4b4e3cfea080ba54d6c.jpg)

This time, for the values of $n$ under study, the kink does not appear at all. Clenshaw–Curtis has approximately the same accuracy as Gauss throughout, and in particular, it obtains the correct integral to machine precision by around $n = 1 8 0 0$ , which is about half the length of the chebfun, length(f), reported earlier! This is typical of Clenshaw–Curtis quadrature: just as with Gauss quadrature, the quadrature value converges about twice as fast as the underlying polynomial approximation, even though Theorems 19.1, 19.3, and 19.4 give no hint of such behavior.

There is a theorem that substantiates this effect. The following result, whose proof we shall not give, comes from [Trefethen 2008].

Theorem 19.5. Clenshaw–Curtis quadrature for differentiable integrands. Under the hypotheses of Theorem 19.4, the same conclusion (19.10) also holds for $( n + 1 )$ -point Clenshaw–Curtis quadrature:

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( 2 n + 1 - \nu ) ^ { \nu } } .
$$

The only difference is that this bound applies for all sufficiently large $n$ (depending on $\nu$ but not $f$ ) rather than for $n \geq \nu / 2$ .

Proof. See [Trefethen 2008]. Here, the definition of $V$ is somewhat different, but this does not affect the argument leading to (19.12).

Theorems 19.4–19.5 are not sharp: Xiang and Bornemann [2012] have shown that the actual convergence rates are one factor of $n$ better than these theorems indicate. I regret that there has not been time to include their results here.

In summary, though Gauss quadrature is more celebrated than Clenshaw–Curtis, its behavior in practice is not much different. For a survey of many aspects of Gauss quadrature, see [Gautschi 1981], and for general information about quadrature, see [Davis & Rabinowitz 1984]. In practice it is common to use adaptive formulas of low or moderate order rather than letting $n$ increase toward $\infty$ with a global grid, though Chebfun is an exception to this pattern.

As mentioned earlier, both Gauss and Clenshaw–Curtis quadrature grids can be improved by a factor approaching $\pi / 2$ by the introduction of a change of variables, taking us beyond the realm of polynomial approximations. These ideas are discussed in Chapter 22.

We have not said much about Newton–Cotes quadrature formulas, based on equispaced points. For smaller orders these are of practical interest: $n = 4$ gives Simpson’s rule, and Espelid has used Newton–Cotes rules of order up to 33 as the basis of excellent codes coted2a and da2glob for adaptive quadrature [Espelid 2004]. The weights $\{ w _ { j } \}$ of Newton–Cotes formulas, however, oscillate in sign between magnitudes on the order of $2 ^ { n }$ , a reflection of the Runge phenomenon, causing terrible numerical instability for large $n$ . Even in the absence of rounding errors, the results of Newton–Cotes formulas do not converge in general as $n \to \infty$ , even for analytic functions. It was clear upon publication of Runge’s paper in 1901 that such divergence was likely, and a theorem to this effect was proved by P´olya [1933].

We close this chapter with an elegant application of Gauss quadrature nodes and weights pointed out by Wang and Xiang [2012].

Theorem 19.6. Barycentric weights for Legendre points. The barycentric weights of Theorem 5.1 for polynomial interpolation in Legendre points can be written as

$$
\lambda _ { k } = C ( - 1 ) ^ { k } { \sqrt { ( 1 - x _ { k } ^ { 2 } ) w _ { k } } } ,
$$

where $x _ { k }$ and $w _ { k }$ are the nodes and weights for $( n + 1 )$ -point Gauss quadrature.

Proof. Both the barycentric weights $\left\{ \lambda _ { k } \right\}$ and the quadrature weights $\{ w _ { k } \}$ are related to the node polynomial $\ell$ . In particular, it is shown in [Winston 1934] that the weights can be written as $w _ { k } = C ( 1 - x _ { k } ^ { 2 } ) ^ { - 1 } [ \ell ^ { \prime } ( x _ { k } ) ] ^ { - 2 }$ .

This theorem implies that polynomial interpolants in Legendre points, just as with Chebyshev points, can be evaluated in $O ( n )$ operations. The formulas are implemented in Chebfun and accessed when one calls legpts, jacpts, hermpts, or lagpts with three output arguments [Hale & Trefethen 2012].

Summary of Chapter 19. Clenshaw–Curtis quadrature is derived by integrating a polynomial interpolant in Chebyshev points, and Gauss quadrature from Legendre points. The nodes and weights for both families can be computed quickly and accurately, even for millions of points. Though Gauss has twice the polynomial order of accuracy of Clenshaw–Curtis, their rates of convergence are approximately the same for nonanalytic integrands.

Exercise 19.1. Riesz Representation Theorem. (a) Look up the Riesz Representation Theorem and write down a careful mathematical statement of it. (b) Show that the computation of an approximate integral $I _ { n }$ from $n + 1$ samples of a function $f \in C ( [ - 1 , 1 ] )$ by integrating the degree $n$ polynomial interpolant through a fixed set of $n + 1$ nodes in $[ - 1 , 1 ]$ is an example of the kind of linear functional to which this theorem applies, provided we work in a finite-dimensional space rather than all of $C ( [ - 1 , 1 ] )$ . (c) In what sense is the Riesz Representation Theorem significantly more general than is needed for this particular application to quadrature?

Exercise 19.2.  -. Evaluate (19.11) with the MATLAB integral command. As a function of the specified precision, what is the actual accuracy obtained and how long does the computation take? How do these results compare with Chebfun sum?

Exercise 19.3. Quadrature weights. (a) Use Chebfun to illustrate the identity (19.4) for Clenshaw–Curtis quadrature in the case $n = 2 0$ , $k = 7$ . (b) Do the same for Gauss quadrature.

Exercise 19.4. Accuracy of Clenshaw–Curtis quadrature. Using theorems of Chapters 4 and 19, derive an exact expression for the error $I \mathrm { ~ - ~ } I _ { n }$ in Clenshaw–Curtis quadrature applied to the function $f ( x ) = T _ { k } ( x )$ for $k > n$ [Gentleman 1972a].

Exercise 19.5. Sharpening Theorem 19.3. Suppose we assume $n \geq 2$ instead of $n \geq 1$ in the Gauss quadrature bound of Theorem 19.3. Show why the constant 64/15 improves to 144/35. What is this actual “constant” as a function of $n$ ?

Exercise 19.6. Integral of a Chebyshev polynomial. Derive the formula (19.6) for the integral of $T _ { k } ( x )$ with $k$ even. (Hint: Following the proof of Theorem 3.1, replace $T _ { k } ( x ) d x$ by $( z ^ { k } + z ^ { - k } ) ( d x / d z ) d z$ .)

Exercise 19.7. Symmetrization in the Golub–Welsch algorithm. The nodes $\{ x _ { j } \}$ of the $( n + 1 )$ -point Gauss quadrature rule are the zeros of the Legendre polynomial $P _ { n + 1 }$ . From the recurrence relation (17.6), it follows as in Theorem 18.1 that they are the eigenvalues of a certain $( n + 1 ) \times ( n + 1 )$ tridiagonal matrix $A$ . (a) Give formulas for the entries of $A$ . (b) Find the unique diagonal matrix $D = \mathrm { d i a g } ( d _ { 0 } , \ldots , d _ { n } )$ with $d _ { 0 } = 1$ and $d _ { j } ~ > ~ 0$ for $j \geq 1$ such that $B = D A D ^ { - 1 }$ , which has the same eigenvalues as $A$ , is real symmetric. What are the entries of $B$ ? (This symmetrized matrix is the Jacobi matrix that is the basis of the Golub–Welsch algorithm.)

Exercise 19.8. Integrating the Bernstein polynomial. Given $f \in C ( [ - 1 , 1 ] )$ , let $B _ { n } ( x )$ be the Bernstein polynomial defined by (6.2) and let $I _ { n }$ be the approximation to $\textstyle \int _ { - 1 } ^ { 1 } f ( x ) d x$ defined by $\begin{array} { r } { I _ { n } = \int _ { - 1 } ^ { 1 } B _ { n } ( x ) d x } \end{array}$ . (a) Show that $I _ { n } = ( n + 1 ) ^ { - 1 } \textstyle \sum _ { k = 0 } ^ { n } f ( k / n )$ (b) Is this an interpolatory quadrature formula? (c) What is its order of accuracy $\alpha$ for smooth integrands as defined by the condition $I - I _ { n } = O ( n ^ { - \alpha } ) ^ { \cdot }$ ?

Exercise 19.9. Nonnegative weights and convergence. Suppose the weights $w _ { k }$ of an interpolatory quadrature formula (19.3) are all nonnegative. Show using the Weierstrass approximation theorem that $I _ { n } \to I$ for any continuous integrand $f$ . (P´olya [1933] showed that uniform boundedness of the sums of the absolute values of the weights is necessary and sufficient for convergence for all $f$ .)

# Chapter 20. Carath´eodory–Fej´er Approximation

We have seen that Chebyshev interpolants are near-best approximations in the sense that they come within a factor of at most $O ( \log n )$ of best approximations, usually even closer. For many applications, this is all one could ask for. But there is another kind of near-best approximations that are so close to best that for smooth functions, they are often indistinguishable from best approximations to machine precision on a computer. These are $\mathit { C F }$ (Carath´eodory–Fej´er) approximations, introduced by Gutknecht and Trefethen [1982]. Earlier related ideas were proposed in [Darlington 1970, Elliott 1973, Lam 1972, Talbot 1976], and the theoretical basis goes back to the early 20th century [Carath´eodory & Fej´er 1911, Schur 1918].10

Before explaining the mathematics of CF approximants, let us illustrate the remarkable degree of near-optimality they sometimes achieve. Here is the optimal $\infty$ -norm error in approximation of $f ( x ) = e ^ { x }$ on $[ - 1 , 1 ]$ by a polynomial of degree 2:

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); n = 2; pbest $=$ minimax(f,n); errbest $=$ norm(f-pbest,inf)

errbest $=$ 0.045017388402819

Here is the corresponding error for CF approximation computed by the Chebfun cf command:

pcf $=$ cf(f,n); errcf $=$ norm(f-pcf,inf)

errcf = 0.045017388414604

These two numbers agree to an extraordinary 9 significant digits. Comparing the best and CF polynomials directly to one another, we confirm that they are almost the same:

norm(pbest-pcf,inf)

# ans $=$ 1.178473985063988e-11

That was for degree $n = 2$ , and the near-optimality of the CF approximants grows stronger as $n$ increases. Let us explore the dependence on $n$ . On a semilog plot, the upper curve in the next figure shows the accuracy of the best polynomial as an approximation to $f ( x )$ , while the lower curve shows the accuracy of the CF polynomial as an approximation to the best polynomial. The two errors are of entirely different orders, and for $n > 3$ , the CF and best polynomials are indistinguishable in floating point arithmetic.

$\mathtt { n n } ~ = ~ 0 : 1 0$ ; err1 = []; err2 = [];   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](images/d76648981e8628108d5b09395f6a61f6be075bf549e534a3bc2852a9bae1cf7f.jpg)

Here is the same experiment repeated for $f ( x ) = \operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ .

f = tanh(4\*(x-.3)); ${ \tt n n } = 0 : 3 0$ ; err1 $=$ []; $\mathbf { e r r } 2 \ = \ \left[ \mathbf { } \mathbf { } \right]$ ;   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](images/4be6d2ec218d128b5ec2b6bae14ac23f7f20343d37b5af4b7c654d663efb5ad7.jpg)

Again we see that pbest−pcf is much smaller than f−pbest, implying that the CF approximant is for practical purposes essentially optimal. (Concerning the erratic oscillations, see Exercise 20.4.) Yet it is far easier to compute:

tic, minimax(f,20); tbest $=$ toc, tic, cf(f,20); tcf = toc

tbest $=$ 0.0389   
tcf $=$ 0.0098

Turning to a nonsmooth function, here again is the jagged example from Chapter 10 with its best approximation of degree 20:

f $=$ cumsum(sign(sin(20\*exp(x)))); plot(f,'k') tic, [pbest,err] $=$ minimax(f,20); tbest $=$ toc; hold on, plot(pbest)

![](images/2355b5b8e5b6a93935c03f732071bf7d06024a4c20eb4cb53828d1a0facc24cd.jpg)

We saw the error curve before:

plot(f-pbest), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](images/609153f9f623bceea1209fd607f4b77668097bcd0d528f87550e6340eb16ec47.jpg)

In CF approximation, we must start from a polynomial, not a jagged function. As a rule of thumb, truncating the Chebyshev series at 5 times the degree of the desired approximation is usually pretty safe. Here is what we get:

$\yen 100 ~ =$ chebfun(f,100); tic, pcf $=$ cf(f100,20); tcf $=$ toc; plot(f-pcf), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](images/02fdd95c1b8a1523f0cf69d0f0ff4404ea19b9f4f87fce661df238205559118a.jpg)

Evidently the error falls short of optimality by just a few percent. Yet again the computation is much faster:

tbest, tcf

tbest $=$ 0.9996   
tcf $=$ 0.0105

Here for comparison is the error in Chebyshev interpolation.

pinterp $=$ chebfun(f,21); hold off, plot(f-pinterp), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](images/624b6a13cda812ad123b782025aa4cffc3ea886e50bd210045df8fe28faf4ce9.jpg)

The time has come to describe what CF approximation is all about. We shall see that the hallmark of this method is the use of eigenvalues and eigenvectors (or singular values and singular vectors) of a Hankel matrix of Chebyshev coefficients.

We start with a real function $f$ on $[ - 1 , 1 ]$ , which we want to approximate by a polynomial of degree $n \geq 0$ . Following Theorem 3.1, we assume that $f$ is Lipschitz continuous, so it has an absolutely convergent Chebyshev series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

Since our aim is polynomial approximation, there is no loss of generality if we suppose that $a _ { 0 } = a _ { 1 } = \cdot \cdot \cdot = a _ { n } = 0$ , so that the Chebyshev series of $f$ begins at the term $T _ { n + 1 }$ . For technical simplicity, let us further suppose that the series is a finite one, ending at the term $T _ { N }$ for some $N \geq n + 1$ . Then $f$ has the Chebyshev series

$$
f ( x ) = \sum _ { k = n + 1 } ^ { N } a _ { k } T _ { k } ( x ) .
$$

We now transplant $f$ to a function $F$ on the unit circle in the complex $z$ -plane by defining $F ( z ) = F ( z ^ { - 1 } ) = f ( x )$ for $| z | = 1$ , where $x = ( z + z ^ { - 1 } ) / 2$ . As in the proof of Theorem 3.1, this gives us a formula for $F$ as a Laurent polynomial,

$$
F ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } ( z ^ { k } + z ^ { - k } ) .
$$

We can divide $F ^ { \prime }$ into two parts, $F ( z ) = G ( z ) + G ( z ^ { - 1 } )$ , with

$$
G ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } z ^ { k } .
$$

The function $G$ is called the analytic part of $F$ , since it can be analytically continued to an analytic function in $| z | \le 1$ . Similarly $G ( z ^ { - 1 } )$ is the coanalytic part of $F ^ { \prime }$ , analytic for $1 \leq | z | \leq \infty$ .

Now we ask the following question: what is the best approximation $\ddot { P }$ to $G$ on the unit circle of the form

$$
\tilde { P } ( z ) = \frac { 1 } { 2 } \sum _ { k = - \infty } ^ { n } b _ { k } z ^ { k } ,
$$

where the series converges for all $z$ with $1 \leq | z | < \infty$ ? In other words, $\ddot { P }$ must be analytic in the exterior of the unit disk apart from a pole of order at most $n$ a t $z = \infty$ . This is the problem that Carath´eodory and Fej´er solved, and the solution is elegant. First of all, $\ddot { P }$ exists, and it is unique. Second, $G - \tilde { P }$ maps the unit circle onto a perfect circle that winds counterclockwise around the origin a number of times: the winding number is at least $n + 1$ . Third, as shown by Schur a few years after Carath´eodory and Fej´er [Schur 1918], $\ddot { P }$ can be constructed explicitly by solving a certain matrix singular value problem. Let $H$ denote the $( N - n ) \times ( N - n )$ real symmetric matrix of Chebyshev coefficients arranged like this,

$$
H = \left( \begin{array} { c c c c c } { a _ { n + 1 } } & { a _ { n + 2 } } & { a _ { n + 3 } } & { \ldots } & { a _ { N } } \\ { a _ { n + 2 } } & { a _ { n + 3 } } & { } & { } & { } \\ { a _ { n + 3 } } & { } & { } & { \ldots } & { } \\ { \vdots } & { } & { } & { } & { } \\ { a _ { N } } & { } & { } & { } & { } \end{array} \right) ,
$$

where the entries in the lower-right triangle are zero. A matrix with this structure, constant along diagonals so that $a _ { i j }$ depends only on $i + j$ , is called a Hankel matrix. Let $\lambda$ be the largest eigenvalue of $H$ in absolute value, let $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { N - n - 1 } ) ^ { T }$ be a corresponding real eigenvector, and define

$$
u ( z ) = u _ { 0 } + u _ { 1 } z + \cdot \cdot \cdot + u _ { N - n - 1 } z ^ { N - n - 1 } .
$$

Here is the theorem due to Carath´eodory and Fej´er and Schur.

Theorem 20.1. Carath´eodory–Fej´er–Schur theorem. The approximation problem described above has a unique solution $\ddot { P }$ , and it is given by the error formula

$$
( G - \tilde { P } ) ( z ) = \lambda z ^ { n + 1 } \frac { u ( z ) } { u ( z ) } .
$$

The function $G - \tilde { P }$ maps the unit circle to a circle of radius $| \lambda |$ and winding number $\geq n + 1$ , and if $| \lambda | > | \mu |$ for all other eigenvalues $\mu$ , the winding number is exactly $n + 1$ .

Proof. The result is due to Carath´eodory and Fej´er [1911] and Schur [1918]. See Theorem 1.1 of [Gutknecht & Trefethen 1982] and Theorem 4 of [Hayashi, Trefethen $\&$ Gutknecht 1990].

Theorem 20.1 is a mathematical assertion about the approximation of a function $G$ on the unit circle by an infinite series. We use this result to construct the polynomial CF approximant as follows. Since $G - \tilde { P }$ maps the unit circle to a circle of winding number $\geq n + 1$ , its real part (times 2)

$$
( G - { \tilde { P } } ) ( z ) + ( G - { \tilde { P } } ) ( z ^ { - 1 } )
$$

maps the unit circle to an equioscillating curve with at least $n + 2$ extreme points. Thus the function

$$
\tilde { p } ( x ) = \tilde { P } ( z ) + \tilde { P } ( z ^ { - 1 } )
$$

yields the equioscillatory behavior that characterizes a best approximation polynomial of degree $n$ to $f ( x )$ on $[ - 1 , 1 ]$ (Theorem 10.1). Unfortunately, $\tilde { p } ( x )$ is not a polynomial of degree $n$ . However, it will generally be very close to one. The function $\ddot { P }$ will normally have Laurent series coefficients $b _ { k }$ that decay as $k \to - \infty$ . We truncate these at degree $- n$ to define

$$
\mathcal { P } _ { _ \mathrm { C F } } ( z ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } b _ { k } z ^ { k } ,
$$

with real part (times 2)

$$
p _ { _ { \mathrm { C F } } } ( x ) = \mathcal { P } _ { _ { \mathrm { C F } } } ( z ) + \mathcal { P } _ { _ { \mathrm { C F } } } ( z ^ { - 1 } ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } ( b _ { k } + b _ { - k } ) z ^ { k } .
$$

If the truncated terms are small, $f - p _ { \mathrm { { C F } } }$ maps $[ - 1 , 1 ]$ to a curve that comes very close to equioscillation with $\geq n + 2$ extrema, and thus $p _ { \mathrm { C F } }$ is close to optimal.

For more details on real polynomial CF approximation, with numerical examples, see [Gutknecht $\&$ Trefethen 1982], [Trefethen 1983], and [Hayashi, Trefethen $\&$ Gutknecht 1990].

Our experiments in the opening pages of this chapter showed that CF approximants can be exceedingly close to best. The truncation described above gives an idea of how this happens. In the simplest case, suppose $f$ is an analytic function on $\lfloor - 1 , 1 \rfloor$ . Then by Theorem 8.1, its Chebyshev coefficients decrease geometrically, and let us suppose that this happens smoothly at a rate $a _ { k } = O ( \rho ^ { k } )$ . Then, roughly speaking, the dominant degree $n + 1$ term of $f$ is of order $\rho ^ { - n - 1 }$ , and the terms $b _ { n } , b _ { n - 1 } , \ldots , b _ { - n }$ are of orders $\rho ^ { - n - 2 } , \rho ^ { - n - 3 } , \cdot \cdot \cdot , \rho ^ { - 3 n - 2 }$ . This suggests that the truncation in going from $\tilde { p }$ to $p _ { \mathrm { C F } }$ will introduce an error of order $\rho ^ { - 3 n - 3 }$ . This is usually a very small number and, in particular, much smaller than the error $\| f - p ^ { * } \|$ of order $\rho ^ { - n - 1 }$ .

In fact, the actual order of accuracy for polynomial CF approximation is one order higher, $\rho ^ { - 3 n - 4 }$ rather than $\rho ^ { - 3 n - 3 }$ . (The reason is that the first truncated term is a multiple of $T _ { 3 n + 3 }$ , the same Chebyshev polynomial that dominates the error $f - p ^ { * }$ itself, and so it is not until the second truncated term, $T _ { 3 n + 4 }$ , that the equioscillation is broken.) On the other hand, to go from this rough argument to a precise theorem is not so easy, because in fact, Chebyshev series need not decay smoothly (Exericse 20.3). Here we quote without proof a theorem from [Gutknecht $\&$ Trefethen 1982].

Theorem 20.2. Accuracy of polynomial CF approximation. For any fixed $m \geq 0$ , let $f$ have a Lipschitz continuous $( 3 m + 3 ) r d$ derivative on $[ - 1 , 1 ]$ with a nonzero $( m + 1 ) s t$ derivative at $x = 0$ , and for each $s \in ( 0 , 1 ]$ , let $p ^ { * }$ and $p _ { { _ { C F } } }$ $b e$ the best and the $\mathit { C F }$ approximations of degree $_ { \mathbf { \nabla } ^ { \prime } \mathbf { \nabla } ^ { \prime } } \psi _ { \mathbf { \nabla } ^ { \prime } }$ to $f ( s x )$ on $[ - 1 , 1 ]$ , respectively. Then as $s \to 0$ ,

$$
\| f - p ^ { * } \| = O ( s ^ { m + 1 } )
$$

and

$$
\| f - p ^ { * } \| \neq O ( s ^ { m + 2 } )
$$

and

$$
\| p _ { { \scriptscriptstyle C F } } - p ^ { * } \| = O ( s ^ { 3 m + 4 } ) .
$$

Proof. See Theorem 3.4 of [Gutknecht $\&$ Trefethen 1982].

We can verify this result numerically. The two plots below display norms for $m = 1$ and $m = 2$ for the function $f ( x ) = e ^ { 5 x }$ .

${ \bf f } { \bf f } = \mathbb { Q } ( { \bf x } ) \exp ( { \sf5 * x } )$ ;   
for $\texttt { m } = \texttt { 1 : 2 }$ $\begin{array} { r } { \sin \mathtt { s s } = \mathtt { \Omega } . 8 . \hat { \mathbf { \Omega } } ^ { } ( 0 : 2 0 ) \mathrm { { ; ~ \ e r r f { p } ~ = ~ [ ] ~ ; ~ \ e r r p p ~ = ~ [ ] ~ ; ~ } } } \end{array}$ for $\mathrm { ~ \mathsf ~ { ~ s ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ s ~ s ~ } ~ }$ $\begin{array} { r l } { \underline { { \mathsf { f } } } } & { { } = } \end{array}$ chebfun(@(x) ff(s\*x)); pbest $=$ minimax(f,m); pcf $=$ cf(f,m); errfp $=$ [errfp norm(f-pbest,inf)]; errpp $=$ [errpp norm(pcf-pbest,inf)]; end loglog(ss,errfp,'.-') hold on, loglog(ss,errpp,'.-r'), loglog(ss,ss.^(m+1),'--'); $\textbf { s } = \ 0 . 0 2 5$ ; loglog(ss,ss.^( $3 * \mathtt { m } + 4 ,$ ,'--r')   
end

![](images/68087d695ebf3f3fdcfb8ad852a5d9a9b57f103c80be00428449070e4b348699.jpg)

![](images/87d97e3db79daad033ecea33113cd8dd5bcd46a194ee686febc205072474fffe.jpg)

In this chapter we have considered CF approximation in its simplest context of approximation of one polynomial $f$ of degree $N$ by another polynomial $p _ { \mathrm { C F } }$ of degree $n$ . In fact, the method is much more general. So long as $f$ has an absolutely convergent Chebyshev series, which is implied, for example, if it is Lipschitz continuous, then Theorem 20.1 still applies [Hayashi, Trefethen $\&$ Gutknecht 1990]. Now $H$ is an infinite matrix which can be shown to represent a compact operator on $\ell ^ { 2 }$ or $\ell ^ { 1 }$ , its dominant eigenvector is an infinite vector, and $u ( z )$ is defined by an infinite series. The error curve is still a continuous function of winding number at least $n + 1$ .

Another generalization is to approximation by rational functions rather than polynomials. Everything goes through in close analogy to what has been written here, and now the other eigenvalues of the Hankel matrix come into play. The theoretical underpinnings of rational CF approximation can be found in papers of Takagi [1924], Adamjan, Arov, and Krein [1971], and Trefethen and Gutknecht [1983b], as well as the article by Hayashi, Trefethen, and Gutknecht cited above. Quite apart from theory, one can compute these approximations readily by the Chebfun cf command using capabilities introduced by Joris Van Deun. For details and examples see [Van Deun & Trefethen 2011].

Further generalizations of CF approximation concern approximation of vector or matrix functions rather than just scalars, and here, such techniques are associated with the name $H _ { \infty }$ approximation. An important early paper was Glover [1984], and there have been many extensions and generalizations since then [Antoulas 2005, Zhou, Doyle $\&$ Glover 1996].

We have emphasized the practical power of CF approximants as providing nearbest approximations at low computational cost. The conceptual and theoretical significance of the technique, however, goes beyond this. Indeed, the eigenvalue/singular value analysis of Carath´eodory–Fej´er approximation seems to be the principal known algebraic window into the detailed analysis of best approximations, and in most cases where best approximations of a function happen to be known exactly, these best approximations are CF approximations in which an approximant like $\tilde { P }$ or $\ddot { p }$ already has the required finite form, so that nothing needs to be truncated to get to $P$ or $p$ [Gutknecht 1983].

Summary of Chapter 20. Carath´eodory–Fej´er approximation constructs near-best approximations of a function $f \in C ( [ - 1 , 1 ] )$ from the singular values and vectors of a Hankel matrix of Chebyshev coefficients. If $f$ is smooth, CF approximants are often indistinguishable in machine precision from true best approximants.

Exercise 20.1. Approximating $\cos ( n x )$ . (a) For $n = \mathrm { 2 } , \mathrm { 4 } , \mathrm { 8 } , \mathrm { 1 6 } , \dots$ , compute the degree $_ { n }$ CF approximant to $f ( x ) = \cos ( n x )$ and plot the error curve. How high can you go in this sequence? (b) What happens if $\cos ( n x )$ is changed to $\cos ( 0 . 9 n x )$ ?

Exercise 20.2. Approximating the jagged function. Four of the figures of this chapter concerned approximations of degree 20 to a jagged function. (a) How do the $L ^ { 2 }$ norms of the best and CF approximations compare? (b) The CF approximation was based on truncation of the Chebyshev series at term $N = 1 0 0$ . How does the $\infty$ -norm of the error vary with $N$ ? (c) Draw a conclusion from this exploration: is the imperfect equioscillation of the error curve in the figure given in the text for this function mostly due to the fact that CF approximation is not best approximation, or to the fact that $N < \infty$ ?

Exercise 20.3. Complex approximation on the unit disk. (a) Suppose $f$ is an analytic function on the closed unit disk and $p$ is a polynomial of degree $_ n$ . Prove that $p$ is a best approximation to $f$ in the $\infty$ -norm on the disk $| z | \le 1$ if and only if it is a best approximation on the circle $| z | = 1$ . (b) Look up Rouch´e’s theorem and write down a careful statement, citing your source. (c) Suppose $f$ is an analytic function in the closed unit disk and $p$ is a polynomial of degree $_ n$ such that $f - p$ maps the unit circle to a circle of winding number at least $n + 1$ . Prove that $p$ is a best approximation to $f$ on the unit disk. (In fact it is unique, though this is not obvious.)

Exercise 20.4. Irregularity of CF approximation. The second figure of this chapter showed quite irregular dependence of $\| p _ { \mathrm { C F } } - p ^ { * } \|$ on the degree $n$ for the function $f ( x ) =$ $\operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ . In particular, $n = 1 5$ and $n = 1 6$ give very different results. Following the derivation of $p _ { \mathrm { { C F } } }$ in the text, investigate this difference numerically. (a) For $n = 1 5$ , how do the coefficients $\left| b _ { k } \right|$ depend on $k$ , and how big are the truncated terms in going from $\ddot { p }$ to $p _ { \mathrm { C F } }$ ? (b) Answer the same questions for $n = 1 6$ .

# Chapter 21. Spectral Methods

Theorem 8.2 described the geometric convergence of Chebyshev projections and interpolants for an analytic function $f$ defined on $[ - 1 , 1 ]$ . For such a function, it is not just the polynomials that converge geometrically, but also their derivatives. The following theorem makes this precise. An early publication with a result along these lines is [Tadmor 1986].

Theorem 21.1. Geometric convergence of derivatives. Let a function $f$ be analytic in $[ - 1 , 1 ]$ and analytically continuable to the closed Bernstein ellipse $\overline { { E } } _ { \rho }$ for some $\rho > 1$ . Then for each integer $\nu \geq 0$ , the νth derivatives of the Chebyshev projections $f _ { n }$ and interpolants $p _ { n }$ satisfy as $n \to \infty$

$$
\| f ^ { ( \nu ) } - f _ { n } ^ { ( \nu ) } \| = O ( \rho ^ { - n } ) , \quad \| f ^ { ( \nu ) } - p _ { n } ^ { ( \nu ) } \| = O ( \rho ^ { - n } ) .
$$

Proof. Here is an outline, to be filled in in Exercise 21.1. If $f$ is analytic in the closed region $\overline { { E } } _ { \rho }$ , it is also analytic and bounded in the open region $E _ { \tilde { \rho } }$ for some $\bar { \rho } > \rho$ . By Theorem 8.1 it follows that the Chebyshev coefficients satisfy $a _ { k } = O ( \tilde { \rho } ^ { - k } )$ . The bounds (21.1) follow by differentiating the Chebyshev series for $f ^ { ( \nu ) } - f _ { n } ^ { ( \nu ) }$ and $f ^ { ( \nu ) } - p _ { n } ^ { ( \nu ) }$ term by term. The differentiations introduce powers of $n$ , since $T _ { n } ^ { \prime }$ is of size $O ( n ^ { 2 } )$ on $[ - 1 , 1 ]$ , for example, but since $n ^ { \alpha } \tilde { \rho } ^ { - n } = O ( \rho ^ { - n } )$ as $n \to \infty$ for any fixed $\alpha$ , we still get $O ( \rho ^ { - n } )$ convergence for any fixed $\nu$ .

The phenomenon captured in Theorems 8.2 and 21.1 is a general one in complex analysis. When a property holds for an analytic function, there is a good chance that a similar property holds for its derivatives too. The ultimate reason is that both function and derivative can be related to Cauchy integrals, and indeed, an alternative proof of Theorem 21.1 can be based on the Hermite integral formula.

The present chapter is a practical one, devoted to outlining some of the wideranging consequences of Theorem 21.1 for scientific computing: the whole field of spectral methods for the numerical solution of differential equations. Spectral methods are noted for achieving spectral accuracy, which means accuracy that is limited not by the order of the numerical discretization, but only by the smoothness of the function being approximated. This is in contrast to a traditional finite difference or finite element method, which might achieve just $O ( ( \Delta x ) ^ { 2 } )$ or $O ( ( \Delta x ) ^ { 4 } )$ accuracy as $\Delta x  0$ , say, where $\Delta x$ is a grid spacing, even when the function being approximated is $C ^ { \infty }$ or analytic. For a leisurely introduction to spectral methods on Chebyshev grids, see [Trefethen 2000].

We now put aside $\left\{ f _ { n } \right\}$ and focus on spectral collocation methods, based on point values and polynomial interpolants, as opposed to spectral Galerkin methods, based on integrals.

The starting point of spectral collocation methods is the notion of a differentiation matrix. If $p$ is a polynomial of degree $n$ , it is determined by its values on an $( n + 1 )$ -point grid in $[ - 1 , 1 ]$ . The derivative $p ^ { \prime }$ , a polynomial of degree $n - 1$ , is determined by its values on the same grid. The classical spectral differentiation matrix is the $( n + 1 ) \times ( n + 1 )$ matrix that represents the linear map from the vector of values of $p$ on the grid to the vector of values of $p ^ { \prime }$ . (Later we shall mention rectangular alternatives to this classical square matrix formulation.) An explicit formula for this matrix in the case where $\pm 1$ are not among the grid points follows from (5.8) and was first published by Bellman, Kashef, and Casti [1972] (Exercise 21.9):

$$
D _ { i j } = \ell _ { j } ^ { \prime } ( x _ { i } ) = \left\{ \begin{array} { l l } { \displaystyle \frac { \lambda _ { j } } { \lambda _ { i } ( x _ { i } - x _ { j } ) } , } & { i \neq j , } \\ { \displaystyle \frac { x _ { j } } { 1 - x _ { j } ^ { 2 } } , } & { i = j . } \end{array} \right.
$$

The particularly important special case is that of a Chebyshev grid. For exam ple, the function $\sin ( x )$ can be represented to machine precision by a Chebyshev interpolant $p$ on a grid of 14 points:

ans = 14

Suppose we wish to calculate the values of $p ^ { \prime }$ on the same grid. In Chebfun we can write

pp $=$ diff(p); $\tt { x 1 4 } =$ chebpts(14); $\mathtt { p p 1 4 } \ = \ \mathtt { p p } ( \mathtt { x } 1 4 )$   
$\tt p p 1 4 =$ 0.540302305868155 0.564522388819886 0.632936510563863 0.732703188872980 0.842943722651218 0.937783753082982 0.992744245701781 0.992744245701782 0.937783753082982

0.842943722651218   
0.732703188872980   
0.632936510563863   
0.564522388819886   
0.540302305868155

But we can also get our hands on the differentiation matrix explicitly with these commands involving a chebfun object known as a “chebop”:

D = chebop(@(u) diff(u)); D14 = D(14);

If the matrix D14 is multiplied by the vector $\mathtt { p } ( \mathtt { x } 1 4 )$ , the result is the same vector pp14 of sampled derivatives, up to rounding errors:

ans = 3.253654380697663e-14

Above, we put a semicolon after D(14) to avoid printing a $1 4 \times 1 4$ matrix. To give the idea while using up a little less space, here are the $3 \times 3$ and $5 \times 5$ Chebyshev differentiation matrices on $[ - 1 , 1 ]$ :

ans = -1.5000 2.0000 -0.5000 -0.5000 0 0.5000 0.5000 -2.0000 1.5000

# D(5)

ans =

-5.5000 6.8284 -2.0000 1.1716 -0.5000   
-1.7071 0.7071 1.4142 -0.7071 0.2929   
0.5000 -1.4142 0 1.4142 -0.5000   
-0.2929 0.7071 -1.4142 -0.7071 1.7071   
0.5000 -1.1716 2.0000 -6.8284 5.5000

Formulas for the entries of Chebyshev differentiation matrices were first published by Gottlieb, Hussaini, and Orszag [1984], and recurrence relations for computing them fast and stably were given by Welfert [1997], based on earlier work by Fornberg [1988]. Welfert’s paper in turn led to the influential MATLAB Differentiation Matrix Suite by Weideman and Reddy [2000], and another MATLAB code cheb for generating these matrices can be found in [Trefethen 2000].

There is no need to stop at the first derivative. Here is the $5 \times 5$ Chebyshev matrix corresponding to the second derivative on $[ - 1 , 1 ]$ :

D2 $=$ chebop(@(u) diff(u,2)); D2(5)

ans $=$

17.0000 -28.4853 18.0000 -11.5147 5.0000   
9.2426 -14.0000 6.0000 -2.0000 0.7574   
-1.0000 4.0000 -6.0000 4.0000 -1.0000   
0.7574 -2.0000 6.0000 -14.0000 9.2426   
5.0000 -11.5147 18.0000 -28.4853 17.0000

Yes, D2(5) is the square of D(5):

norm(D2(5)-(D(5))^2)

ans = 5.5939e-15

The entries of this matrix can be interpreted as follows. The $j$ th column ( $0 \leq j \leq n$ ) contains the second derivatives of the Lagrange polynomial $\ell _ { j } ( x )$ evaluated at grid points $x _ { 0 } , \ldots , x _ { n }$ . That is, its $( i , j )$ entry (with indexing from 0 to $n$ ) is $\ell _ { j } ^ { \prime \prime } ( x _ { i } )$ . (We have seen Lagrange polynomials in Chapters 5, 9, 11, and 15.) For example, here is the Lagrange polynomial supported at $x _ { 3 }$ :

![](images/ecddf1bbac8ce66d50410f7c305e97fa5c3a94f8f5f48e184b6c58dd5b7ce342.jpg)

Its second derivatives at the grid points are the values in the fourth column of the matrix $D ( 5 )$ just shown:

ans $=$   
-11.5147   
-2.0000   
4.0000   
-14.0000   
-28.4853

In Chebfun, an object like D or D2 is called a linear chebop (and internally within the Chebfun system, a linop). A linear chebop is not a matrix, but rather a prescription for how to construct matrices of arbitrary order. (A computer science term for the process of filling such prescriptions is lazy evaluation.) If $D$ is applied to an integer argument, the matrix of that dimension is produced:

size(D(33)) ans $=$ 33 33

If $D$ is applied to a chebfun, it has the effect appropriate to the length of that chebfun:

$$
\textbf { f } = \mathbf { \Omega } _ { \mathbf { S } } \mathrm { i n } \left( 7 * \mathbf { x } \right) * \mathbf { e x p } \left( \mathbf { x } \right) * \mathrm { t a n } \left( \mathbf { x } \right) ; \mathbf { \Omega } \mathrm { n o r m } \left( \mathrm { d i f f \left( \mathbf { f } \right) - D * \mathbf { f } \Lambda } \right)
$$

ans = 0

More generally, a chebop can be defined for any differential (or integral) operator. For example, here is the chebop corresponding to the map $L : u \mapsto u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u$ on $[ - 1 , 1 ]$ :

$$
\mathrm { \small ~ L ~ = ~ c h e b o p ~ ( \mathfrak { Q } ~ ( u ) ~ \ d i f f ~ ( u , 2 ) ~ + ~ d i f f ~ ( u ) ~ + ~ 1 0 0 * u } ) ~ ;
$$

Here is the $5 \times 5$ realization of this operator:

ans $=$

111.5000 -21.6569 16.0000 -10.3431 4.5000   
7.5355 86.7071 7.4142 -2.7071 1.0503   
-0.5000 2.5858 94.0000 5.4142 -1.5000   
0.4645 -1.2929 4.5858 85.2929 10.9497   
5.5000 -12.6863 20.0000 -35.3137 122.5000

We can illustrate its use by applying it to the chebfun for $e ^ { x }$ :

ans $=$ 2.0967e-13

Now we come at last to spectral methods proper. If we just wanted to apply differential operators to functions, we would not need matrices. To solve a differential equation, however, we need to invert the process of applying a differential operator. We want to find a function $u$ satisfying certain boundary conditions such that $\boldsymbol { L u }$ is equal to a prescribed function $f$ . This is where the matrices come in, for matrices can be inverted.

Suppose, for example, we seek a function $u$ that satisfies the equation

$$
u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u = x , \quad u ( - 1 ) = u ( 1 ) = 0
$$

with $x \in [ - 1 , 1 ]$ . The matrix realization above had no boundary conditions. Now we need to impose them, and a standard way of doing this is to modify one or more initial or final rows of the matrix, one row for each boundary condition (see Chapters 7 and 13 of [Trefethen 2000]). For Dirichlet boundary conditions as in (21.3), we change the first and last rows to correspond to rows of the identity:

L.bc $=$ 'dirichlet'; feval(L,5,'oldschool')

ans =

(We shall explain the clumsy command feval(L,5,'oldschool') in a moment.) Thus, instead of imposing the differential equation at the boundary points $x _ { 0 }$ and $x _ { n }$ , we are imposing boundary conditions at those points. We can now use exactly this matrix to solve the ODE approximately with a $5 \times 5$ spectral discretization. The right-hand side of the matrix problem will be the vector of $x$ sampled at the Chebyshev points—except that the first and last components of the vector will be changed to the appropriate Dirichlet values at $x _ { 0 }$ and $x _ { n }$ , namely zero.

$\mathtt { x 5 } \ =$ chebpts(5); x5([1 end]) = 0; $\mathtt { u 5 } \ =$ feval(L,5,'oldschool') $\mathtt { \backslash x 5 }$ ; plot(chebfun(u5),'.-')

![](images/7760fc9b2bae4c1b1835bd989be3849791033173bf1111d11050c85d26428bc8.jpg)

We have just computed our first solution of a boundary value problem with a spectral method. From the picture it is not evident whether the result is close to correct or not. In fact it is not, as increasing the resolution reveals:

$\tt { x 1 2 } =$ chebpts(12); x12([1 end]) = 0; $\tt { u } 1 2 \ =$ feval(L,12,'oldschool')\x12; plot(chebfun(u12),'.-')

![](images/e0c5dd7f4a2b19f6bb209c73bac98c52b82ad8eecc6970bfeac64bf9fa54361c.jpg)

This curve is beginning to get close to the true solution. How fine a grid do we need to reach approximately machine precision? In Chebfun, the appropriate grid is determined automatically when one solves the problem without specifying dimensions, still with the backslash command:

u = L\x; plot(u,'.-')

![](images/3909a25866b98cfff9c8c5cceabf1359eb5722dfd798d95c6367a2bea7bec921.jpg)

To get this result, Chebfun has solved matrix problems of sizes 17, 33, and 65, at which point its convergence criteria were satisfied. The final length is

length(u)

and we can verify that the accuracy is good:

norm(L\*u-x)

ans = 1.1362e-12

This brings us to the clumsy expression feval(L,5,'oldschool') in the demonstration above. This notation instructs Chebfun to display a spectral differentiation matrix corresponding to boundary conditions imposed in the classical way that we have just described, in which certain rows of a square differentiation matrix are replaced by rows corresponding to boundary conditions [Trefethen 2000]. This method of applying boundary conditions relies on the assumption that for each boundary condition, there is a clear choice of which row of the ODE discretization matrix it should replace. In fact, this ceases to be clear in various situations involving systems of equations or more complicated boundary conditions, as well as more general side conditions such as $\textstyle \int u ( x ) d x = 0$ . Around 2010, Driscoll and Hale realized that more robust and flexible discretizations could be obtained by switching to a different approach based on rectangular differentiation matrices. For an order $d$ differential operator to be applied on an $( n + 1 )$ -point grid, the Driscoll–Hale discretization begins with a matrix of dimension $( n + 1 - d ) \times ( n + 1 )$ corresponding to a map from data on an $( n + 1 )$ -grid to data on an $( n + 1 - d )$ -grid, and then appends an additional $d$ rows for boundary conditions. No collocation equation gets replaced in this process. This is now the discretization strategy used routinely by Chebfun, and it is what Chebfun actually did in solving the problem $\texttt { u } = \texttt { L } \backslash \texttt { x }$ above. To see the matrices, one can type the more natural expression L(5) instead of feval(L,5,'oldschool'). We shall not go into details here; see [Driscoll & Hale 2015] and [Aurentz & Trefethen 2017a].

Homogeneous Dirichlet conditions at both ends are only the simplest of many possible boundary conditions for a boundary value problem. To solve (21.3) again except with Neumann conditions $u ^ { \prime } ( - 1 ) = u ^ { \prime } ( 1 ) = 0$ , the first and last rows of the discretization matrix would classically get replaced by the corresponding rows of the first derivative matrix:

L.bc $=$ 'neumann'; feval(L,5,'oldschool')

ans =   
-5.5000 6.8284 -2.0000 1.1716 -0.5000   
7.5355 86.7071 7.4142 -2.7071 1.0503   
-0.5000 2.5858 94.0000 5.4142 -1.5000   
0.4645 -1.2929 4.5858 85.2929 10.9497   
0.5000 -1.1716 2.0000 -6.8284 5.5000

Here is the Chebfun solution, again based on the Driscoll–Hale discretization, now plotted without dots:

$\texttt { u } = \texttt { L } \backslash \texttt { x }$ ; plot(u)

![](images/7128fd6ac5add7d725356a87dd567f4c6bdbe9f3ed4c681ddf772a409d20be94.jpg)

Spectral methods can also solve problems with variable coefficients. For example, suppose we wish to solve the Airy equation boundary value problem

$$
u ^ { \prime \prime } - x u = 0 , \quad u ( - 3 0 ) = 1 , \ u ( 3 0 ) = 0
$$

for $x \in [ - 3 0 , 3 0 ]$ . Here is the solution:

L = chebop(@(x,u) diff $( \mathtt { u } , 2 ) \mathtt { - x } . \mathtt { * u }$ ,[-30,30]); L.lbc $\ c = ~ 1$ ; $\mathtt { L . r b c } = \mathtt { 0 }$ ; $\tt { u } = \tt { L } \backslash 0$ ; plot(u)

![](images/fda62db12db0af10cd530c95478748b328a95c24c12c1d2756c92bc73a30cbbc.jpg)

For nonlinear problems, one would normally use a Newton iteration or some variant. Chebfun handles these cases too. For example, the equation

$$
\theta ^ { \prime \prime } + \mathrm { s i n } ( \theta ) = 0 , \quad \theta \in [ 0 , 6 ] ,
$$

describes the motion in time of a nonlinear pendulum situated at height $h ( t ) =$ $- \cos ( \theta ( t ) ) \in [ - 1 , 1 ]$ . If we prescribe boundary conditions

$$
u ( 0 ) = - \pi / 2 , \quad u ( 6 ) = \pi / 2 ,
$$

we can solve the system numerically with Chebfun as follows. Notice that the solution is still invoked by the backslash command, though we are very far now from the original MATLAB notion of backslash for solving a square system of linear equations.

N = chebop(0,6); N.op $=$ @(theta) diff(theta,2) $^ +$ sin(theta); N.lbc $=$ -pi/2; N.rbc $=$ pi/2; theta $=$ N\0; plot(-cos(theta))

![](images/51dd67a0f7e1b309c5c389dbbccca972d46ebad59c4ab4577d10135d5319940c.jpg)

This solution corresponds to the pendulum first going up above height 0 for a time, and then swinging over to the other side, where it again goes above height 0 before falling back down again. On the other hand, suppose we change the right-hand boundary condition to $5 \pi / 2$ . Then another solution appears, corresponding to the pendulum swinging once around the top:

![](images/77be7365c74c98dbe70a824f4e9a6ab97f0e8efa369498d55ee92dd2e920f079.jpg)

These two solutions do not exhaust the full set of possibilities for this nonlinear problem; see Exercise 21.7.

To compute solutions of nonlinear differential equations, Chebfun uses variants of Newton’s method implemented for continuous functions rather than discrete vectors. Where one might expect to encounter Jacobian matrices in the solution process, Chebfun actually utilizes their continuous analogues known as Fr´echet derivative operators, which are constructed by a process of automatic differentiation, again exploiting lazy evaluation. These capabilities are due to Birkisson and

Driscoll [2012]. Chebfun can also solve systems of equations, eigenvalue problems, and problems specified by coefficients that are just piecewise smooth.

This is a book about approximation theory, not differential equations, and we began this chapter with an approximation result, a theorem about the $O ( \rho ^ { - n } )$ accuracy of derivatives of approximations of analytic functions. It would be excellent if this theorem implied that spectral methods converge to analytic solutions at the rate $O ( \rho ^ { - n } )$ , but it does not. Theorem 21.1 ensures that if $u$ is an analytic solution to a boundary value problem $L u = f$ , then the Chebyshev interpolants to $\boldsymbol { L u }$ would converge geometrically to $f$ as $n  \infty$ . In spectral computations, however, we do not have the exact solution available to discretize but must approximate it by solving matrix problems. One can hope that the approximations will converge at the expected rate, and indeed they do so under many circumstances, but proving this requires further arguments, which we shall not attempt to discuss here. As a rule, in this business, the practice is ahead of the theory.

Some of the ideas behind spectral methods are as old as Fourier and Chebyshev expansions, and many people contributed in the early years of computers, including Lanczos, Elliott, Fox, and Clenshaw. But it was their application to the PDEs of fluid mechanics by Orszag and Gottlieb and others beginning around 1970 that made these methods famous, and it was Orszag who coined the term “spectral methods” [Orszag 1971a & 1971b]. Spectral methods divide into Fourier methods, for periodic problems, and Chebyshev and related methods, for nonperiodic problems. As always in this book, we have emphasized the nonperiodic case, which is less obvious, even though at bottom it is essentially the same. In applications, Fourier and Chebyshev discretizations are often found mixed together. For example, a three-dimensional cylindrical geometry may be discretized by a Chebyshev grid for the radial variable, a periodic Fourier grid for the circumferential variable, and another periodic grid serving as an approximation to an ideal infinite Fourier grid for the longitudinal variable. When the grids are fine, implementations are often based on the FFT rather than matrices.

For details of the spectral methods incorporated in Chebfun, see [Driscoll, Bornemann & Trefethen 2008] and [Driscoll & Hale 2015] for the linear case and [Birkisson & Driscoll 2012] for nonlinear aspects; more recent material can be found in [Aurentz & Trefethen 2017a] and Appendix A of [Trefethen, Birkisson & Driscoll 2018]. For information about spectral methods in general, see texts such as [Fornberg 1996], [Trefethen 2000], [Boyd 2001], [Canuto et al. 2006], [Hesthaven, Gottlieb & Gottlieb 2007], and [Shen, Tang & Wang 2011].

This chapter began by noting that if a function is smooth, the derivatives of its interpolants converge rapidly. A contrapositive of this observation is the phenomenon that if the discrete approximations to derivatives of a function blow up as the mesh is refined, it is not smooth. Chebfun exploits this principle as the basis of its edge detection algorithm for breaking piecewise smooth functions into subintervals, which was illustrated at the end of Chapter 9. This algorithm was developed by Rodrigo Platte and is described in [Pach´on, Platte & Trefethen 2010].

Summary of Chapter 21. Spectral collocation methods are numerical algorithms for solving differential equations based on polynomial or trigonometric interpolants. For problems whose solutions are analytic, they typically converge geometrically as the grid is refined.

Exercise 21.1. Proof of Theorem 21.1. Write down a careful proof of Theorem 21.1 as a corollary of Theorems 3.1 and 8.1. Be sure to state precisely what properties of the Chebyshev polynomials $\{ T _ { k } \}$ your proof depends on.

Exercise 21.2. Extension of Theorem 21.1. Theorem 21.1 quantifies the accuracy of the derivatives of Chebyshev interpolants based on an assumption of analyticity in a Bernstein ellipse. State and prove a different theorem about the convergence of the derivatives for any sequence of polynomials $p _ { n } \in \mathcal { P } _ { n }$ for which the errors satisfy $\| f - p _ { n } \| =$ $O ( \rho ^ { - n } )$ for some $\rho > 1$ .

Exercise 21.3. Differentiation matrices. (a) The text displayed the $3 \times 3$ matrix $D ( 3 )$ . Derive the entries of this matrix analytically. (b) Also displayed was the $5 \times 5$ matrix $D 2 ( 5 )$ . Derive the entries of the middle column of this matrix analytically.

Exercise 21.4. Linear boundary value problems. Solve the following linear ODE boundary value problems numerically with Chebfun. In each case plot the solution and report the value of $u$ at the midpoint of the interval and the length of the chebfun repre senting $_ u$ .

(a) $0 . 0 0 1 u ^ { \prime \prime } + x u ^ { \prime } - u = \exp ( - 1 0 x ^ { 2 } )$ , $x \in [ - 1 , 1 ]$ , $u ( - 1 ) = 2$ , $u ( 1 ) = 1$ .   
(b) $0 . 0 0 1 u ^ { \prime \prime } + ( 1 - x ^ { 2 } ) u = 1$ , $x \in [ - 5 , 5 ]$ , $u ( - 5 ) = 0$ , $u ( 5 ) = 0$ .   
(c) $0 . 0 0 1 u ^ { \prime \prime } + \sin ( x ) u = 1 ,$ $x \in [ - 1 0 , 1 0 ]$ , $u ( - 1 0 ) = 0$ , $u ^ { \prime } ( 1 0 ) = 0$ .

Exercise 21.5. Nonlinear boundary value problems. Find a solution numericall to each of the following nonlinear ODE boundary value problems. In each case plot th solution and report the value of $u$ at the midpoint of the interval.

(a) $0 . 0 5 u ^ { \prime \prime } + ( u ^ { \prime } ) ^ { 2 } - u = 1$ , $x \in [ 0 , 1 ]$ , $u ( 0 ) = 2$ , $u ( 1 ) = 1$ . (b) $0 . 0 1 u ^ { \prime \prime } - u u ^ { \prime } - u = 0$ , $x \in [ - 1 , 1 ]$ , $u ( - 1 ) = 1$ , $u ( 1 ) = 2$

Exercise 21.6. Convergence with $\mathbf { \nabla } ^ { \prime } \mathbf { \pmb { \nu } } ^ { \prime }$ . The text solved the boundary value problem $u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u = x$ on $[ - 1 , 1 ]$ with boundary conditions $u ( - 1 ) = u ( 1 ) = 0$ for grid parameters $n + 1 = 5$ , 12, and 35. Perform a numerical study of the $\infty$ -norm error of the solution as a function of $_ n$ , and comment on the results.

Exercise 21.7. Nonunique solutions. (a) For each of the two nonlinear pendulum problems solved at the end of the chapter, determine exactly how many solutions there must be. (You can use physical reasoning, or phase plane analysis.) (b) Find them all numerically with Chebfun by using sufficiently close initial guesses specified by a command of the form $\mathbb { N } . \mathrm { i n i t } \ = \ \mathbf { \ " } \mathbf { f } \left( \mathrm { t h e t a } \right)$ to start the iteration. Report the maximum heights $- \cos ( \theta )$ of the pendulum in all cases and the time(s) at which these heights are reached.

Exercise 21.8. Painlev´e equation. Solutions to the second Painlev´e equation, $u ^ { \prime \prime } = 2 u ^ { 3 } + x u$ , typically blow up at various locations on the $_ x$ -axis. There exist special solutions, however, that are smooth for all real $_ x$ . Characterized by the asymptotic boundary conditions $u \sim \pm \sqrt { - x / 2 }$ as $x  - \infty$ and $u  0$ as $x \to + \infty$ , these are the so-called Hastings–McLeod solutions. Truncate the problem to the interval $[ - L , L ]$ with boundary conditions $u ( - L ) = \sqrt { L / 2 }$ , $u ( L ) = 0$ and compute and plot solutions for $L = 1 , 2 , 4 , 8 , 1 6$ . Produce a table of $u ( 0 )$ and $u ^ { \prime } ( 0 )$ for each value of $L$ . To 10 digits, what do you think are the values of $u ( 0 )$ and $u ^ { \prime } ( 0 )$ in the limit $L \to \infty$ ?

Exercise 21.9. Formula for square differentiation matrix. Derive (21.2) from (5.8).

Exercise 21.10. Eigenvalues of differentiation matrices. Let $D _ { 1 }$ and $D _ { 2 }$ be the $2 0 \times 2 0$ matrices corresponding to spectral discretization of the second derivative operator on $[ - 1 , 1 ]$ with Dirichlet boundary conditions of the Driscoll–Hale and “old school” types, respectively. Are the eigenvalues real or complex? What are the condition numbers? How do the condition numbers grow with the dimension? (This is an important matter for accuracy of spectral methods.)

# Chapter 22. Linear Approximation: Beyond Polynomials

Several times in the previous chapters, we have hinted that polynomials are not optimal functions for linear approximation on $[ - 1 , 1 ]$ . (Nonlinear approximations are another matter and will make their appearance in the next chapter.) It is now time to explain these hints and introduce alternative approximations that may be up to $\pi / 2$ times more efficient. One reason the alternatives are valuable is that they have practical advantages in some applications, especially for spectral methods in more than one space dimension. An equally important reason is that they push us to think more deeply about what it means to approximate a function and what may or may not be special about polynomials. The ideas of this chapter originate in [Bakhvalov 1967] and [Hale & Trefethen 2008]. Related ideas are the basis of work on sinc function numerical methods [Stenger 1993 & 2010, Richardson & Trefethen 2011], tanh and double exponential or tanh-sinh quadrature [Sag $\&$ Szekeres 1964, Takahasi & Mori 1974, Mori & Sugihara 2001], and the transformed-grid spectral methods introduced by Kosloff and Tal-Ezer [1993].

Recall from Chapter 8 that if $f$ is analytic on $[ - 1 , 1 ]$ , then to investigate its polynomial approximations, we ask how large a Bernstein ellipse $E _ { \rho }$ it can be analytically continued to. Here, for example, is the ellipse $E _ { \rho }$ with $\rho = 1 . 1 5$ . The words “Bernstein ellipse” written inside will help in a moment to visualize a conformal map. (Mathematically, these words are a piecewise linear complex function of a real variable constructed by the Chebfun scribble command.)

![](images/bc5a67f9aa3e39cc7f814658724b47882a7a98247079adb5358b03bca5467d2b.jpg)

Bernstein ellipses are unavoidable if one works with polynomial interpolants, but from the user’s point of view, they have an unfortunate property: they are thicker in the middle than near the ends! For a function $f$ to be analytic in the region just shown, its Taylor series about a point $x \approx 0$ must have a radius of convergence 0.14 or more. For $x \approx \pm 1$ , on the other hand, a radius of convergence of 0.01 is sufficient. Thus the smoothness requirement on $f$ is highly nonuniform, and this is not an artifact of the analysis. Polynomials of a given degree really can resolve rougher behavior of a function $f$ near the endpoints than in the middle. This phenomenon turns up in one form of another whenever approximation theorists seek sharp results about polynomial approximations, whether $f$ is analytic or not. See, for example, [Timan 1951], [Lorentz 1986], [Ditzian $\&$ Totik 1987], and Chapter 8 of [DeVore and Lorentz 1993].

Of course, there are some functions that have most of their complexity near $\pm 1$ , and for these, the nonuniform approximation power of polynomials may be an advantage. For example, functions of this kind arise in fluid mechanics problems with boundary layers. More often, however, the nonuniform approximation power of polynomials is a disadvantage from a practical point of view, as well as being a conceptual complication. If only those ellipses had constant width for all $x \in [ - 1 , 1 ] !$

As soon as one frames the difficulty in this way, a possibility for a solution suggests itself. The idea is to change variables by means of a function that conformally maps ellipses, approximately at least, to straight-sided $\varepsilon$ -neighborhoods of $\lfloor - 1 , 1 \rfloor$ , while mapping $[ - 1 , 1 ]$ to itself. To explore this idea we shall use the variable $x$ for the domain where $f$ is defined and introduce a new variable $s$ for the parameter domain, where the Chebyshev points and ellipses live. Our conformal map will be $x = g ( s )$ , and we shall approximate a function $f ( x )$ on $[ - 1 , 1 ]$ by $p ( g ^ { - 1 } ( x ) ) = p ( s )$ , where $p$ is a polynomial. Equivalently, we shall approximate $f ( g ( s ) )$ on $[ - 1 , 1 ]$ by a polynomial. In the remainder of this chapter we explore the consequences of this idea, considering just one fixed example of a map $g$ ,

$$
g ( s ) = { \frac { 1 } { 5 3 0 8 9 } } ( 4 0 3 2 0 s + 6 7 2 0 s ^ { 3 } + 3 0 2 4 s ^ { 5 } + 1 8 0 0 s ^ { 7 } + 1 2 2 5 s ^ { 9 } ) ,
$$

or as a Chebfun command,

$$
\begin{array} { r }  \begin{array} { l } { \mathrm { g ~ = ~ c h e b f u n } { \left( \mathfrak { Q } \left( \mathbf { s } \right) \begin{array} { l l } { ( 4 0 3 2 0 \ast \mathbf { s } + 6 7 2 0 \ast \mathbf { s } \widehat { \textbf { \small s } } + 3 0 2 4 \ast \mathbf { s } \widehat { \textbf { \small s } } + \mathbf { \small ~ \cdot } \widehat { \textbf { \small { \xi } } } \cdot \mathbf { \xi } \cdot \mathbf { \xi } \cdot \mathbf { \xi } ) } \end{array} \right. } \\ { \quad \left. \begin{array} { l } { 1 8 0 0 \ast \mathbf { s } \widehat { \textbf { \small s } } ^ { - } 7 \ + \ 1 2 2 5 \ast \mathbf { s } \widehat { \textbf { \small s } } ^ { } 9 ) / 5 3 0 8 9 } \end{array} \right) ; } \end{array} } \end{array}
$$

This function $g$ is derived by truncating the Taylor series of $( 2 / \pi ) \sin ^ { - 1 } ( x )$ and then rescaling the result so that $g ( \pm 1 ) = \pm 1$ . See [Hale & Trefethen 2008] for a discussion of this and other possible choices of $g$ , some of which (notably a conformal map onto an infinite strip) come closer to realizing the maximum possible improvement by a factor of $\pi / 2$ . See also Exercises 22.2 and 22.3.

To begin the discussion, let us look at how $g$ transforms ellipses about $[ - 1 , 1 ]$ . Here is a plot of $g ( E _ { 1 . 1 5 } )$ , the transformed version of the ellipse shown earlier. Notice the much straighter sides.

plot(g(z(1.15)),'m'), hold on, plot(g(f),'k')

![](images/3f5788a0d11dfe8aa24b7abdd438d78d7743c54f2e36502da7e05663aa506fc8.jpg)

Following [Hale & Trefethen 2008], we call $g$ a sausage map and $g ( E _ { 1 . 1 5 } )$ a sausage region. The crucial property is that for most of its length, the sausage is narrower than the ellipse, as the distorted “Bernstein ellipse” label makes clear. The ellipse has half-width approximately $\rho - 1$ , which is about $3 2 \%$ more than the half-width $0 . 7 6 ( \rho - 1 )$ of the sausage:

ellipse_width $=$ max(imag(z(1.15))) sausage_width $=$ max(imag(g(z(1.15)))) ratio $=$ ellipse_width/sausage_width ellipse_width = 0.1402 sausage_width $= ~ 0 . 1 0 6 1$ ratio $=$ 1.3210

We can learn more by looking at a family of ellipses. Following Chapter 8, here is a plot of $E _ { \rho }$ for $\rho = 1 , 1 . 2 , . . . , 2 . 2$ :

$\mathtt { w } = \mathtt { e x p } ( 2 \mathtt { i } \ast \mathtt { p i } \ast \mathtt { x } )$ ; for rho $=$ 1.1:0.2:2.2, plot( $( \mathtt { r h o } * _ { \mathsf { W } } + ( \mathtt { r h o } * _ { \mathsf { W } } ) \hat { \mathbf { \xi } } ( - 1 ) ) / 2 )$ , hold on, end

![](images/e1cc3591d2061a32ed6003802c81f39d5c3810e6b7d48c452cb83c744bc29253.jpg)

Here is the corresponding figure for the images $g ( E _ { \rho } )$ :

for rho $= \ 1 . 1 : 0 . 2 : 2 . 2$ plot $( { \ g ( { ( { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } } ) } } } + { ( { { { \bf { \bar { \Phi } } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) } \hat { \bf { \Lambda } } } } ) } \cdot \mathrm { { \Lambda } } } ) } + ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) \cdot \mathrm { { \Lambda } }  )$ , hold on   
end

![](images/70cb75854628d4586637894b834e8e541309db27a659f401d7dad8644d9e2bab.jpg)

It is clear that near $[ - 1 , 1 ]$ , the transformed ellipses are narrower and more uniform in shape than the ellipses, but further away, their behavior is more irregular. We shall see some of the implications of these shapes as we explore the uses of this map.

Chapter 2 considered polynomial interpolants in Chebyshev points $\left\{ s _ { k } \right\}$ . With the transformation $g$ , $f$ is interpolated by transformed polynomials $p ( g ^ { - 1 } ( x ) )$ in the points $\{ g ( s _ { k } ) \}$ . We illustrate the difference between Chebyshev and transformed Chebyshev points by adapting a code segment from Chapter 17. The squares show the transformed points.

ss $=$ chebpts(10); plot(ss,.9,'.b'), hold on, plot(g(ss),.8,'sm') ss $=$ chebpts(20); plot(ss,.5,'.b'), plot(g(ss),.4,'sm') ss $=$ chebpts(50); plot(ss,.12,'.b'), plot(g(ss),0,'sm')

![](images/6189e1c158c916011fb303df42912e4cb1a9182a823869043c26f7e997bc8a1c.jpg)

Note that the squares are more evenly distributed than the dots, and in particular, they are denser in the middle, providing finer resolution.

Chapter 3 considered Chebyshev polynomials and series. We adapt another code segment from Chapter 17 to illustrate how a Chebyshev polynomial $T _ { n } ( x )$ compares to the corresponding transformed polynomial $T _ { n } ( g ^ { - 1 } ( x ) )$ . For this we need the inverse map $g ^ { - 1 }$ .

$\tt { g i } = \tt { i n v } ( \tt { g } )$ ; $\mathrm { T 5 0 ~ = }$ chebpoly(50); subplot(2,1,1), plot(T50), plot(T50(gi),'m')

![](images/092327442afbae877400180cee5b60fe4a6be53b3d8330b4fa60397ff6f8ac7d.jpg)

Notice that the lower curves are more like uniform sine waves than the upper ones.

Theorem 3.1 summarized some basic facts about Chebyshev series, and these carry over immediately to a theorem for transformed Chebyshev series. The theorem as stated assumes $g$ is analytic, though in fact, continuous differentiability would be enough.

Theorem 22.1. Transformed Chebyshev series. Let $g$ be an analytic function on $[ - 1 , 1 ]$ mapping $[ - 1 , 1 ]$ to itself with $g ^ { \prime } ( s ) > 0$ . Then if $f$ is Lipschitz continuous on $[ - 1 , 1 ]$ , it has a unique representation as an absolutely convergent series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } { \bigl ( } g ^ { - 1 } ( x ) { \bigr ) } ,
$$

and the coefficients are given for $k \geq 1$ by the formula

$$
a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( g ( s ) ) T _ { k } ( s ) } { \sqrt { 1 - s ^ { 2 } } } d s
$$

and for $k = 0$ by the same formula with the factor $2 / \pi$ changed to $1 / \pi$

Proof. This is a consequence of Theorem 3.1.

For many functions $f$ , the transformed series are $2 0 - 3 0 \%$ more efficient than the originals. For example, Chebyshev interpolation of $( 2 + \cos ( 2 0 x + 1 ) ) ^ { - 1 }$ requires about 520 terms for 15-digit accuracy:

![](images/3ee084befebde40f7769f1c49fbec04e681c07b84f3dd47adcbe9f25b88c3522.jpg)

For the transformed interpolants the number is closer to 400:

plotcoeffs(f(g),'m')

![](images/5990e9478385f1faccb15819b7e9b302f53d5ac8e689fd5c34b060a28adc0027.jpg)

Chapter 7 considered convergence for differentiable functions. Theorem 7.2 can readily be restated for the transformed context—see Exercise 22.1. For a numerical illustration, here is a repetition of the experiment from Chapter 7 involving $f ( x ) =$ $| x |$ . On the loglog scale, the transformed approximants run parallel to the same line as the Chebyshev interpolants, but lower.

$\begin{array} { r l } & { \mathrm { \bf ~ f ~ = ~ \ a b s ( x ) : ~ \ f g ~ = ~ \bf ~ f \left( g \right) : ~ \omega ~ } } \\ & { \mathrm { \bf ~ n n ~ = ~ \omega ~ 2 * r o u n d \left( 2 . \hat { \omega } ( 0 : \cdot 3 : 7 ) \right) - 1 ; ~ { \vec { \varphi } } ~ e ~ = ~ \omega ~ 0 * n n ; ~ { \vec { \varphi } } ~ e \in ~ \omega _ 0 \ * n n ; } } \\ & { \mathrm { \bf ~ f o r ~ \bf ~ j ~ = ~ \bf ~ 1 : 1 \cdot } \mathrm { \bf ~ e n g t h } \mathrm { \bf ~ ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ \omega ~ n n ( j ) : ~ \omega _ \mathrm { { f } ~ n ~ = ~ \ c h e b f u n ( f , n + 1 ) ; ~ \vec { \varphi } e e ( j ) ~ = ~ \ n o r m ( f - f n , i n f ) ~ ; } } } \\ & { \mathrm { \bf ~ f n 2 ~ = ~ \ c h e b f u n ( f g , n + 1 ) ; ~ \vec { \varphi } e e 2 ( j ) ~ = ~ \ n o r m ( f g - f n 2 , i n f ) ~ ; } } \end{array}$   
end   
$\log 1 0 \mathbf { g } \left( \mathtt { n n } , 1 . / \mathtt { n n } , ^ { \prime } \mathtt { r } ^ { \prime } \right)$   
hold on, loglog(nn,ee,'.'), loglog(nn,ee2,'sm')   
ratio $=$ ee(end-4:end)./ee2(end-4:end)

ratio $=$

1.3167 1.3167 1.3167 1.3167 1.3167

![](images/f7077a8ad74b49d1e12289efd32e01b45e17d95f749d1ed792a1e2fc23225126.jpg)

Chapter 8 considered convergence for analytic functions. Here is the transformed equivalent of Theorems 8.1 and 8.2.

Theorem 22.2. Transformed coefficients of analytic functions. For given $\rho > 1$ , let $_ { g }$ and $f$ be analytic functions on $[ - 1 , 1 ]$ that can be analytically continued to $E _ { \rho }$ and $g ( E _ { \rho } )$ , respectively, with $| f ( z ) | \leq M$ for $z \in g ( E _ { \rho } )$ . Then the transformed Chebyshev coefficients of Theorem 22.1 satisfy

$$
| a _ { k } | \leq 2 M \rho ^ { - n } ,
$$

the truncated transformed series satisfy

$$
\| f - f _ { n } ( g ^ { - 1 } ( x ) ) \| \leq \frac { 2 M \rho ^ { - n } } { \rho - 1 } ,
$$

and the transformed Chebyshev interpolants satisfy

$$
\| f - p _ { n } ( g ^ { - 1 } ( x ) ) \| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

Proof. These results follow from Theorems 8.2 and 22.1.

Here is a repetition of the Chapter 8 experiment for the Runge function, now with squares to show the transformed approximants.

$\begin{array} { r l } & { \mathrm { \bf ~ f ~ = ~ \bf ~ 1 / \left( 1 + 2 5 * x \mathrm { \bf ~ \dot { \bf ~ \underline { ~ } { ~ 2 ~ } } } \right) ; ~ \bf ~ f ~ g ~ = ~ \bf ~ f ~ ( g ) ~ } ; } \\ & { \mathrm { \bf ~ n n ~ = ~ \bf ~ 0 : 1 0 : 2 0 0 ; ~ { \bf ~ e ~ e ~ = ~ \bf ~ 0 * n n } ; ~ { \bf ~ e } e 2 ~ = ~ \bf ~ 0 * n n } ; } \\ & { \mathrm { \bf ~ f o r ~ \bf ~ j ~ = ~ \bf ~ 1 : 1 \mathrm { e n g t h } ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ \bf ~ n n ( j ) ; ~ \bf ~ f ~ n ~ = ~ \mathrm { c h e b f u n } ( f , n + 1 ) ; ~ { \bf ~ e } e ( j ) ~ = ~ \mathrm { n o r m } ( f - f n , i n f ) ~ } ; } \\ & { \mathrm { \bf ~ f n 2 ~ = ~ \mathrm { c h e b f u n } ( f g , n + 1 ) ; ~ { \bf ~ e } e 2 ( j ) ~ = ~ \mathrm { n o r m } ( f g - f n 2 , i n f ) ~ } ; } \end{array}$ end semilogy(nn,ee,'.'), hold on, semilogy(nn,ee2,'sm')

![](images/b74d126d2d240c6898ae1da52ce8737fe13528ace924ee8cb2a3c92a885336b7.jpg)

The speedup is clear. On the other hand, here is a repetition of the experiment with $\cos ( 2 0 x )$ .

f f $\begin{array} { l } { { \mathrm { \tiny ~ ( ~ \cos ~ ( 2 0 * x ) ~ ; ~ f g ~ = ~ f ~ ( g ) ~ ; ~ ~ n n ~ = ~ 0 : 2 : 6 0 ; ~ \ e e ~ = ~ 0 * n n ; ~ \ e e 2 ~ = ~ 0 : n n ; } } } \\ { { \mathrm { \tiny ~ ( ~ \partial ~ 1 : 1 \mathrm { { z } \it ~ { h } } ( n n ) ~ \partial ~ 1 ~ \partial ~ 2 ~ ) ~ } } } \\ { { \mathrm { \tiny ~ { n } ~ = ~ n n ( j ) ~ ; ~ f n ~ = ~ c h e b f u n ( f , n + 1 ) ~ ; ~ \ e e ( j ) ~ = ~ n o r m ( f - f n , i n f ) ~ ; } } } \\ { { \mathrm { \tiny ~ { f n 2 ~ = ~ c h e b f u n ( f g , n + 1 ) ~ ; ~ \ e e 2 ( j ) ~ = ~ n o r m ( f g - f n 2 , i n f ) ~ ; } } } } \end{array}$ end semilogy(nn,ee,'.'), hold on, semilogy(nn,ee2,'sm')

![](images/c5dde1ffdbd77482370e51a11163b26ba7a691d7e79e628ad60cc3913aa8b2c7.jpg)

Now the result is ambiguous: the transformed method starts out ahead, but the standard Chebyshev method wins eventually. The explanation can be found in the nested ellipses $E _ { \rho }$ and their images plotted earlier. The function cos(20 $x$ ) is entire, and for larger $n$ , the Chebyshev points take good advantage of its analyticity well away from $[ - 1 , 1 ]$ . The transformed points do not do as well. (The advantage of the transformation becomes decisive again if we change $\cos ( 2 0 x )$ to $\cos ( 1 0 0 x )$ .)

We can see similar effects if we look at best approximations. For a nonsmooth function like $| x |$ , transformed polynomials typically approximate better than true ones. The following figures should be compared with those of Chapter 10, and the variable ratio quantifies the degree of improvement.

$\begin{array} { r l } { \mathbf { f } } & { { } = } \end{array}$ abs(x); subplot(1,2,1), plot(f,'k')   
$\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ; [p,err] $=$ minimax(fg,4);   
hold on, plot(p(gi),'m') subplot(1,2,2), hold off   
1 $\mathrm { \Omega ) 1 0 t ( g , f { \mathrm { - p } } ( g i ) , \mathrm { ' m } ^ { \prime } ) }$ , hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,4); ratio $=$ err2/err

ratio $=$ 1.2847

![](images/1845e770388d2f91a6a63afd7d8a12eed41d56d5314988e5b12e59132018b3df.jpg)

On the other hand, for a gentle entire function like $\exp ( x )$ , pure polynomials converge very fast and transformed polynomials cannot compete. The following error curve is seven orders of magnitude larger than that of Chapter 10.

f = exp(x); $\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ;   
[p,err] $=$ minimax(fg,10); plot(g,fg-p,'m'), hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,10); ratio $=$ err2/err

ratio $=$ 2.9938e-07

![](images/9f0452bccff8c3ccc9940ad1366c0f614976292b5867844611b0c023be87b487.jpg)

Our final application of transformed polynomial approximants is the one that was the subject of [Hale & Trefethen 2008]: quadrature. As described in Chapter 19, standard quadrature formulas are based on the idea of integrating a function numerically by interpolating it by a polynomial and then integrating the interpolant. This is the basis of all the well-known quadrature formulas, including Gauss, Newton– Cotes, Simpson, and Clenshaw–Curtis. But why should quadrature formulas be based on polynomials? This is a question not often raised in the quadrature literature. Some of the explanation surely has to do with custom going back centuries, before the appearance of computers, when the algebraic simplicity of polynomials would have been a telling advantage. If one had to give a mathematical answer still with some validity today, it would probably be that a polynomial formula is optimal if the order is fixed while the grid size is decreased to zero. If the order increases to $\infty$ on a fixed interval of integration, however, polynomial formulas are in no sense optimal.

In particular, a “transformed Gauss” quadrature formula can be obtained by applying Gauss quadrature to the integral on the right in the formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) = \int _ { - 1 } ^ { 1 } f ( g ( s ) ) g ^ { \prime } ( s ) d s .
$$

To illustrate this transplanted quadrature idea we pick a wiggly function,

![](images/c2dcd2e35bcba46969634a33e170e23dc0c24f900efb28070c675e1eabe709fb.jpg)

Here is a code in which I represents Gauss quadrature and I2 is transformed Gauss quadrature—and we see that the dots decrease about $3 0 \%$ more slowly than the squares.

gp $=$ diff(g); Iexact $=$ sum(f); err $=$ []; err2 $=$ []; nn = 50:50:2000;   
for $\texttt { n } = \texttt { n n }$ $[ \bf s _ { \tau } , \bf w ] _ { \tau } = \mathrm { \sf ~ 1 e g p t s } \left( \ln \mathrm { \right) ; \mathrm { ~ \cal ~ I ~ } = \mathrm { \bf ~ w * f } \left( \bf s \right) }$ ; err $=$ [err abs(I-Iexact)]; $\begin{array} { r } { \texttt { I 2 } = \texttt { w * } ( \texttt { f } ( \texttt { g } ( \texttt { s } ) ) * \wp ( \texttt { s } ) ) } \end{array}$ ; err2 $=$ [err2 abs(I2-Iexact)];   
end   
semilogy(nn,err,'.-'), hold on, semilogy(nn,err2,'s-m')

![](images/44f69757e2b5552406911841849cb223729abd383099b2bb62db946daa1ca729.jpg)

We emphasize that in the end a quadrature formula is just a quadrature formula, as specified in (19.3):

$$
I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) .
$$

Gauss leads to one choice of nodes and weights, Clenshaw–Curtis leads to another, transplanted Gauss leads to a third, and transplanted Clenshaw–Curtis leads to a fourth. Regardless of what concepts may have been employed in the derivation, in the end the quadrature formula just takes a linear combination of function values, and the transformed formulas usually outperform the classical ones. For example, in [Hale & Trefethen 2008] it is proved that the transformed Gauss formulas based on mapping $E _ { 1 . 1 }$ to an infinite strip converge $5 0 \%$ faster than Gauss quadrature for the class of functions analytic in the $\varepsilon$ -neighborhood of $[ - 1 , 1 ]$ , for any $\varepsilon < 0 . 0 5$ .

This chapter has shown that polynomials are not the only effective general linear class of approximants for general functions $f$ on an interval and indeed are often suboptimal. There is much more that can be said on this subject. For example, there is the matter of how the mapping $g$ was derived and what other maps might be useful; an influential family of maps was introduced by Kosloff and Tal-Ezer [1993]. Another topic we have not discussed is the application to spectral methods, Kosloff and Tal-Ezer’s motivation, and it is here that transformations of variables are perhaps most important in practice. Finally, there is the idea of using the map $g$ for rational functions rather than polynomials. The last two ideas have been combined powerfully in Tee’s adaptive rational spectral collocation method based on adaptively determined conformal maps [Tee & Trefethen 2006, Hale & Tee 2009].

Summary of Chapter 22. Although many numerical methods are based on polynomial approximations of a function $f \in C ( [ - 1 , 1 ] )$ , such approximations are not optimal, for polynomials have higher resolution near the endpoints of the interval than near the middle. By a conformal transplantation one can derive approximations that are up to $\pi / 2$ times more efficient.

Exercise 22.1. A challenging integrand. Repeat the Gauss vs. transformed Gauss quadrature experiment for the “spiky integrand” (18.2). By approximately what percentage is Gauss slower than transformed Gauss for this function? How do you account for this behavior?

Exercise 22.2. Chebfun '	
'. [Unfortunately to carry out this exercise it is necessary to acquire the pre-2014 Chebfun version 4.] Chebfun contains a 'map' parameter that enables one to explore some of the ideas of this chapter in an automatic fashion (try help maps for information). To illustrate this, construct $\textbf { f } = \mathbf { \nabla } _ { 1 } / ( 1 { + } 2 5 { * } \mathbf { x } \hat { \mathbf { \nabla } } 2 )$ with both $\mathrm { ~ \tt ~ x ~ } =$ chebfun $( ^ { \prime } { \tt x } ^ { \prime } )$ as usual and also $\qquad \tt { x } =$ chebfun( $" \mathbf { x } \cdot \mathbf { \lambda }$ ,'map',{'sausage',9}). How do the plotcoeffs results compare? (b) What if the parameter 9 is varied to $1 , 3 , 5 , \ldots , 1 5 ?$ (This is the degree of the expansion in (22.1).)

Exercise 22.3. Transformed Clenshaw–Curtis quadrature. Generate the final plot of this chapter again, but now with two further curves added corresponding to Clenshaw– Curtis and transformed Clenshaw–Curtis quadrature. How do the results compare with those for Gauss and transformed Gauss?

Exercise 22.4. Gauss quadrature transformed by an infinite strip. Better than a sausage map for some applications is a map onto an infinite strip. Following the last two exercises, use $\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun( $" \mathbf { x } \cdot \mathbf { \xi }$ ,'map',{'strip',1.4}) to reproduce the final plot of this chapter again, now with one other curve added corresponding to Gauss quadrature transformed by the strip map of the Bernstein ellipse of parameter $\rho = 1 . 4$ . How do the results compare with those from the sausage transformation?

Exercise 22.5. Interpolation of equispaced data. Here is a scheme for interpolation of data at equispaced points on $[ - 1 , 1 ]$ : use a conformal map $g ^ { - 1 }$ to transform the equispaced grid to an approximate Chebyshev grid, and then compute a polynomial interpolant by means of the barycentric formulas (5.11)–(5.12). Explore this method in Chebfun for interpolation of the Runge function $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ where $g$ is the map (22.1), using interp1 to compute the interpolant. Do these approximants weaken the Runge phenomenon? (A theorem of [Platte, Trefethen $\&$ Kuijlaars 2011] asserts that no approximation scheme can eliminate the Runge phenomenon entirely.)

# Chapter 23. Nonlinear Approximation: Why Rational Functions?

Up to now, this book has been about polynomials or, in the last chapter, their transplants. The final six chapters of the book are about rational functions, which have been a mainstay of approximation theory from the beginning. Why do rational approximations occupy such a large place in the literature? Polynomials are familiar and comfortable, but rational functions seem complex and specialized. Is their position in approximation theory justified, or is it an artifact of history, perhaps a holdover from the precomputer era? In this chapter we attempt to answer these questions, and in doing so we shall find ourselves considering the broader question of what the uses are of the whole subject of approximation theory.

I think the answer is this. Although rational functions indeed became an established part of approximation theory long before computers and many of today’s practical applications, their place in the subject is deserved. Their importance stems from a conjunction of two facts. On the one hand, rational functions are more powerful than polynomials at approximating functions near singularities and on unbounded domains. On the other hand, for various reasons related, for example, to partial fraction decompositions, they are easier to work with than their nonlinearity might suggest—indeed, sometimes no more complicated than polynomials.

A rational function is the ratio of two polynomials, and in particular, given $m \geq 0$ and $n \geq 0$ , we say that $r$ is a rational function of type $( m , n )$ if it can be written as a quotient $p _ { m } / q _ { n }$ with $p _ { m } \in \mathcal { P } _ { m }$ and $q _ { n } \in \mathcal { P } _ { n }$ . The set of all rational functions of type $( m , n )$ is denoted by $\mathcal { R } _ { m n }$ , and any $r \in \mathcal { R } _ { m n }$ can be written in the form

$$
r ( x ) = \sum _ { k = 0 } ^ { m } a _ { k } x ^ { k } { \Bigg / } \sum _ { k = 0 } ^ { n } b _ { k } x ^ { k }
$$

for some real or complex coefficients $\{ a _ { k } \}$ and $\left\{ b _ { k } \right\}$ . The degrees need not be exact, i.e., there is no requirement that $a _ { m }$ or $b _ { n }$ must be nonzero. Nor do we require that the numerator and denominator be relatively prime, that is, that they have no common zeros.

Suppose, however, that for some nonzero $r \in \mathcal { R } _ { m n }$ , we choose a representation with relatively prime numerator and denominator. Define $\mu \leq m$ to be the index of the highest degree nonzero numerator coefficient and similarly $\nu \leq n$ for the denominator, and further normalize the coefficients by requiring $b _ { \nu } = 1$ . Then we can write

$$
r ( x ) = \sum _ { k = 0 } ^ { \mu } a _ { k } x ^ { k } \Biggl / \sum _ { k = 0 } ^ { \nu } b _ { k } x ^ { k } ~ , ~ a _ { \mu } \neq 0 , ~ b _ { \nu } = 1 .
$$

In this case $r$ has exactly $\mu$ finite zeros and $\nu$ finite poles, counted with multiplicity: we say that $r$ is of exact type $( \mu , \nu )$ . (The case in which $r$ is identically zero is a special one, with no nonzero coefficients in the numerator, and we say it has exact type $( - \infty , 0 )$ .) If $\mu > \nu$ , then $r$ has a pole at $x = \infty$ of order $\mu - \nu$ , and if $\nu > \mu$ , it has a zero at $x = \infty$ of order $\nu - \mu$ . Basic properties of rational functions are described in books of complex analysis such as [Ahlfors 1953, Henrici 1974, Markushevich 1985].

These representations highlight the nonlinearity of rational functions, but a different perspective is suggested when we represent them by partial fractions. (Partial fractions were the subject of Jacobi’s PhD thesis [1825], and an excellent general reference is Chapter 7 of [Henrici 1974].) In the simplest situation, consider

$$
r ( x ) = \sum _ { k = 1 } ^ { n } { \frac { c _ { k } } { x - \xi _ { k } } } ,
$$

where $\{ \xi _ { k } \}$ are distinct real or complex numbers. For any coefficients $\left\{ c _ { k } \right\}$ , this is a rational function of type $( n - 1 , n )$ . The number $c _ { k }$ is the residue of $r$ at $\xi _ { k }$ . This representation highlights the linear aspects of rational functions. For example, whereas computing the integral of $r$ written in the form $p / q$ looks daunting, in the representation (23.3) we have simply

$$
\int ^ { x } r ( s ) d s = C + \sum _ { k = 1 } ^ { n } c _ { k } \log ( x - \xi _ { k } ) .
$$

In applications, it is interesting how often a formula like this turns out to be instrumental in making a rational function useful.

The partial fraction form (23.3) does not apply to all rational functions. One limitation is that it always represents a rational function of exact type $( \mu , \nu )$ with $\mu \ < \nu$ . Another is that it does not represent all functions of this kind, since it cannot account for poles of multiplicity greater than 1. The following theorem gives a partial fraction representation for the general case.

Theorem 23.1. Partial fraction representation. Given $m , n \ \geq \ 0$ , let $r \in \mathcal { R } _ { m n }$ be arbitrary. Then $r$ has a unique representation in the form

$$
r ( x ) = p _ { 0 } ( x ) + \sum _ { k = 1 } ^ { \mu } p _ { k } ( ( x - \xi _ { k } ) ^ { - 1 } ) ,
$$

where $p _ { 0 }$ is a polynomial of exact degree $\nu _ { 0 }$ for some $\nu _ { 0 } \leq m$ (unless $p = 0$ ) and $\left\{ p _ { k } \right\}$ , $1 \leq k \leq \mu$ , are polynomials of exact degrees $\nu _ { k } ~ \geq ~ 1$ with $p _ { k } ( 0 ) = 0$ and $\scriptstyle \sum _ { k = 1 } ^ { \mu } \nu _ { k } \leq n$ .

Proof. See Theorem 4.4h of [Henrici 1974].

The function $p _ { 0 }$ is the polynomial part of $r$ , and $p _ { k } \big ( ( x - \xi _ { k } ) ^ { - 1 } \big )$ is its principal part at $\xi _ { k }$ .

This is all we shall say for the moment about the mathematics of rational functions. Let us now turn to the main subject of this chapter, the discussion of why these functions are useful in approximation theory and approximation practice.

The right place to start is with a cautionary observation. Rational functions are not always better than polynomials. Indeed, consider the most basic of all situations, in which a function $f$ is analytic in a $\rho$ -ellipse $E _ { \rho }$ for some $\rho > 1$ . For such a function, by Theorem 8.2, polynomial approximations will converge at the rate $O ( \rho ^ { - n } )$ . It turns out that a typical convergence rate for type $( n , n )$ rational functions is $O ( \rho ^ { - 2 n } )$ . So, doubling the number of parameters to be determined sometimes just approximately doubles the convergence rate. (In fact, sometimes it does not increase the convergence rate at all [Szabados 1970].) For applications of this kind, rational functions may outperform polynomials, but often it is by a rather modest factor.

For example, here are a pair of curves showing $\| f - p _ { 2 n } ^ { * } \|$ (dots) and $\| f - r _ { n n } ^ { * } \|$ (stars) as functions of $n$ for $f ( x ) = \exp ( - x ^ { 4 } )$ , where $p _ { 2 n } ^ { * }$ and $r _ { n n } ^ { * }$ are the best approximations to $f$ in $\mathcal { P } _ { 2 n }$ and $\mathcal { R } _ { n n }$ , respectively. (We shall discuss rational best approximation in the next chapter.) Both curves decrease slightly faster than geometrically, and there is not much difference between them. (The rational approximations here should in principle be computed with minimax, but Chebfun’s rational Remez algorithm is currently not robust enough, so cf is used instead.)

$\begin{array} { r } { \mathrm { ~ x ~ = ~ c h e b f u n ( ~ ` ~ x ' ~ ) ~ ; ~ f ~ = ~ e x p ( - x ' 4 ) ~ ; ~ n n ~ = ~ 0 : 2 0 ; ~ e x r p ~ = ~ [ ] ~ ; ~ e x r r ~ = ~ [ ] ~ ; } } \end{array}$   
for $\texttt { n } = \texttt { n n }$ p2n $=$ minimax(f,2\*n); errp $=$ [errp norm(f-p2n,inf)]; [p,q,foo] $=$ cf(f,n,n); $\mathtt { r n n } = \mathtt { p } / { \mathtt { q } }$ ; errr $=$ [errr norm(f-rnn,inf)];   
end   
semilogy(nn,errp,'.-'), hold on, semilogy(nn,errr,'h-r')

![](images/5348b9738a28172861973c7f703c95f71573f070eebf075b4b16c11224e9f365.jpg)

What makes rational functions important is that, in contrast to this example, there are many problems where one wants to operate near singularities, or on unbounded domains. For these problems, rational approximations may converge much faster than polynomials. For example, here is an experiment like the last one, but with $f ( x ) = \left| x \right|$ . For this function, a type $( n , n )$ rational approximant with $n = 1 5 0$ gives 16-digit accuracy, whereas polynomial approximants would need $n = 1 0 ^ { 1 5 }$ to do so well. (Again this code should in principle use minimax but cannot, so known best approximation errors are hardwired in.)

f = abs(x); xx = linspace(-1,1,1000); $\mathtt { n n } ~ = ~ 0 : 5 0$ ; errp = [];   
errr $=$ [.5 4.37e-2 8.50e-3 2.28e-3 7.37e-4 2.69e-4 1.07e-4 ... 4.60e-5 2.09e-5 9.89e-6 4.88e-6 2.49e-6 1.30e-6 ... 6.3\*exp(-pi\*sqrt(26:2:max(nn)))];   
errr $=$ kron(errr,[1 1]); errr(end) $=$ [];   
for $\texttt { n } = \texttt { n n }$ p2n $=$ minimax(f, $^ { 2 * \mathrm { n } }$ ); errp $=$ [errp norm(f(xx)-p2n(xx),inf)];   
end   
semilogy(nn,errp,'.-'), hold on, semilogy(nn,errr,'h-r')

![](images/8ef41d96a0d562740d0ad1f854d6a45a57a6609f840faa242b7ab614da97b403.jpg)

The approximation of $| x |$ by rational functions is one of the “two famous problems” to be considered in Chapter 25. Half a century ago Donald Newman proved that whereas polynomial approximants to $| x |$ converge just at the rate $O ( n ^ { - 1 } )$ , for rational approximants the rate is $\exp ( - C { \sqrt { n } } )$ with $C > 1$ [Newman 1964]. This result rigorously established the possibility of an exponential difference in effectiveness of the two types of approximations.

The rest of this chapter is devoted to an outline of 12 applications in which rational approximations are useful. In most of these examples, there is a singularity or unbounded domain in the picture. The exceptions are applications #1 and #8, where rational functions outperform polynomials less decisively.

1. Elementary and special functions. Classically, approximation theory brings to mind the problem of designing subroutines for computers to evaluate elementary functions, like $\sin ( x )$ , and special functions, like Airy or Bessel functions. For some of these applications, especially when the number of digits of accuracy required is known in advance, rational approximations prove to be the best choice. A classic project in this line is the SPECFUN software package [Cody 1993], descendant of the earlier FUNPACK [Cody 1975], which uses rational best approximations to evaluate Bessel functions, error functions, gamma functions, and exponential integrals to 18 digits of accuracy. For many years a driving force behind these software products and an expert on the matter of practical rational approximations was W. J. Cody at the Argonne National Laboratory; Cody’s version of the rational Remez algorithm is described in [Cody, Fraser & Hart 1968]. For a presentation of some of the state of the art early in the 21st century, see [Muller 2006].

2. Digital filters. In electrical engineering, the construction of low-pass, highpass, and other digital filters often involves approximation of functions with jumps. (For these problems the approximation domain is usually the unit circle in the complex plane.) Jumps amount to singularities on or near the domain of approximation, and Theorem 8.3 implies that polynomials have no chance of rapid convergence for such functions. As Newman’s theorem would lead us to expect, rational approximations sometimes do much better. Engineers use the term FIR (Finite Impulse Response) for polynomial filters and IIR (Infinite Impulse Response) in the rational case [Oppenheim, Schafer & Buck 1999].

3. Convergence acceleration for sequences and series. The mathematical sciences are full of problems of extrapolation. For example, one might be interested in $\scriptstyle \operatorname* { l i m } _ { h \to 0 } f ( h )$ , where $f ( h )$ is a quantity computed numerically on a grid of spacing $h$ . For such a problem, $f$ is often analytic at $h = 0$ , in which case Richardson extrapolation, based on interpolating the data by a polynomial, may be beautifully effective. On the other hand, suppose we want to evaluate $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a _ { n }$ for a sequence $\{ a _ { n } \}$ . We can regard this problem too as $\scriptstyle \operatorname* { l i m } _ { h \to 0 } f ( h )$ with the definition $f ( 1 / n ) =$ $a _ { n }$ , but now, in many applications, $f ( h )$ will not be analytic at $h = 0$ and Richardson extrapolation will be ineffective. The more powerful extrapolation methods that have been developed for such problems, such as Aitken extrapolation and the epsilon algorithm, are mostly based on rational approximations. See Chapter 28.

4. Determination of poles. Suppose a function $f$ is analytic on $[ a , b ]$ and has some real or complex poles nearby whose positions and residues are of interest. Classic examples of such problems arise in the study of phase transitions in condensed matter physics. If we approximate $f$ by polynomials on $[ a , b ]$ , then by Theorem 8.3, the convergence fails outside a $\rho$ -ellipse of analyticity, so not much information about poles can be obtained. If we approximate by rational functions, exponential convergence to some of the poles can often be achieved. Specifically, a good strategy is to consider the poles of $r _ { m n }$ for moderate values of $n$ , where $r _ { m n }$ is a rational approximant to $f$ obtained by Pad´e or Chebyshev–Pad´e approximation or rational interpolation or least-squares. See Chapters 26–28.

5. Analytic continuation. If $f$ is analytic on $[ a , b ]$ , then in many applications it can be analytically continued, in theory, to the rest of the complex plane, apart from exceptional points and curves in the form of poles, other singularities, and branch cuts. Computing such continuations numerically, however, is a difficult problem. One could try approximating $f$ by a polynomial, but this approach will be useless outside the largest Bernstein ellipse in which $f$ is analytic. Rational functions, by contrast, may be effective for continuation much further out. Again see Chapter 28.

6. Eigenvalues and eigenvectors of matrices. Suppose we want to compute an eigenvector of a matrix $A$ . One approach, the power method, is to pick a starting vector $x$ and compute $\scriptstyle \operatorname* { l i m } _ { n \to \infty } A ^ { n } x$ , but the convergence of this polynomial-based idea is very slow in general. A much faster method, inverse iteration, is based on rational approximations: find an approximation $\mu$ to some eigenvalue $\lambda$ and compute $\scriptstyle \operatorname* { l i m } _ { n \to \infty }$ $( A - \mu I ) ^ { - n } x$ . The convergence gets faster the closer $\mu$ is to the singularity $\lambda$ , and exploitation of this effect leads to the spectacularly effective QR algorithm for matrix eigenvalues and eigenvectors [Francis 1961]. Experts in numerical linear algebra do not usually think about rational approximations when discussing inverse iteration or the QR algorithm, but such approximations come explicitly to the fore in the analysis of extensions such as shift-and-invert Arnoldi or rational Krylov iteration [G¨uttel 2010].

7. Model reduction and optimal control. A major topic in numerical linear algebra and control theory is the approximation of complex input-output systems by simpler ones for more efficient computation. Via the Laplace transform, problems of this kind (in the case of continuous as opposed to discrete time) can in many cases be reduced to problems of approximation on the imaginary axis in the complex plane. The unbounded domain makes rational approximations a natural choice, and in fortunate cases, a system with hundreds of thousands of degrees of freedom may be reduced to a model with just dozens or hundreds. One set of methods for such problems goes by the name of $H _ { \infty }$ approximation, based on results by Adamjan, Arov, and Krein [1971] and Glover [1984] that are related to CF approximation (Chapter 20). For more information see [Antoulas 2005, Zhou, Doyle & Glover 1996, Embree & Sorensen 2013].

8. Exponential of a matrix. A famous paper in numerical analysis is “Nineteen Dubious Ways to Compute the Exponential of a Matrix,” by Moler and Van Loan in 1978, reprinted in expanded form 25 years later [Moler & Van Loan 2003]. These authors compared many algorithms for computing $e ^ { A }$ and reached the conclusion that the most effective was a scaling-and-squaring method based on Pad´e approximation [Ward 1977]. Here, first $A$ is scaled so that its norm is on the order of 1. Then $e ^ { A }$ is approximated by $r ( A )$ , where $r$ is a type $( n , n )$ Pad´e approximant to $e ^ { x }$ (Chapter 27). This is an example where rational approximations outperform polynomials not decisively but by a more or less constant factor. This approach is used by the matrix exponential program expm in MATLAB, which for many years was based on type $( 6 , 6 )$ Pad´e approximation. A more careful analysis of the scalingand-squaring algorithm was later provided by Higham [2009], who concluded that a better choice was type (13, 13), and the expm code was adjusted accordingly in MATLAB Version 8. In [Higham & Al-Mohy 2010, Appendix] the authors conclude that Pad´e approximants are up to $2 3 \%$ more efficient than Taylor polynomials in this application.

9. Numerical solution of stiff PDEs. A particularly important set of problems related to matrix exponentials are derived from PDEs. The starting point of such applications is the Laplace operator $\Delta$ on a spatial domain $\Omega$ with Dirichlet boundary conditions, which has an infinite set of negative real eigenvalues diverging to $- \infty$ . To solve the heat equation $\partial u / \partial t = \Delta u$ numerically on $\Omega$ with initial data $u ( x , 0 ) = u _ { 0 }$ , one would like to be able to compute the matrix exponential product $e ^ { t A } v _ { 0 }$ , where $A$ is a matrix discretization of $\Delta$ and $v _ { 0 }$ is a discretization of $u _ { 0 }$ . The wide range of eigenvalues makes such a problem “stiff,” posing challenges for numerical methods. One method for coping with stiffness is to find a rational function $r ( x )$ that approximates $e ^ { x }$ accurately on $( - \infty , 0 ]$ , hence in particular at all of the eigenvalues of $A$ , and then to compute $r ( t A ) v _ { 0 }$ . Polynomials cannot approximate a bounded function uniformly on an infinite interval, but rational functions can. This problem of rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ goes back to Cody,

Meinardus, and Varga [1969], whose “1/9 conjecture,” eventually settled by Gonchar and Rakhmanov [1989], is the other famous problem considered in Chapter 25. Generalizations have become important in scientific computing in recent years in the design of exponential integrators for the fast numerical solution of stiff nonlinear ODEs and PDEs [Hochbruck & Ostermann 2010, Kassam & Trefethen 2005, Schmelzer & Trefethen 2007].

10. Quadrature formulas. As we have seen in Chapter 19, a quadrature formula approximates an integral $\begin{array} { r } { I ~ = ~ \int _ { a } ^ { b } f ( x ) d x } \end{array}$ by a finite linear combination $\begin{array} { r } { I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) } \end{array}$ . If the weights $w _ { k }$ are interpreted as residues of a rational function $r ( x )$ with poles at the nodes $x _ { k }$ , then by estimation of a Cauchy integral over a contour $\Gamma$ enclosing $[ a , b ]$ in the complex plane, one can show that the error $I - I _ { n }$ is bounded in terms of the size of $f$ in the region enclosed by $\Gamma$ times the error in approximation of the analytic function $\log ( ( x + 1 ) / ( x - 1 ) )$ by $r$ over the same region [Takahasi $\&$ Mori 1971]. So every quadrature formula is connected with a rational approximation problem. In fact, Gauss’s original derivation of the $( n + 1 )$ -point Gauss quadrature formula on $[ - 1 , 1 ]$ was based on exactly this connection: via continued fractions, he considered type $( n , n + 1 )$ Pad´e approximation of $\log ( ( x + 1 ) / ( x - 1 ) )$ at $x = \infty$ [Gauss 1814].

11. Adaptive spectral methods for $P D E s$ . The barycentric interpolation formula has the form of a rational function that reduces to a polynomial for a special choice of weights (Chapter 5). Regardless of the choice of weights, however, one still gets an interpolant, so long as the weights are nonzero, and in some applications there is no compelling reason to force the interpolant to be a polynomial. This opens up the possibility of much more flexible rational interpolants, which have the particular advantage of not being so sensitive to the distribution of the interpolation points. These ideas originated with Salzer [1981] and Schneider and Werner [1986], building on earlier work going as far back as Jacobi [1846], and were later developed by Berrut [1988] and Floater and Hormann [2007]. For ODEs and PDEs, they form the basis of adaptive spectral methods for solving problems whose solutions have singularities close to the region of approximation [Berrut, Baltensperger & Mittelmann 2005, Tee & Trefethen 2006, Hale & Tee 2009].

12. One-way wave equations. Our final application became well known in the 1970s and 1980s [Halpern & Trefethen 1988]. The usual wave equation permits energy propagation in all directions, but there are applications where one would like to restrict to half the permitted angles, a $1 8 0 ^ { \circ }$ range. For example, this idea is useful in underwater acoustics [Tappert 1977], geophysical migration [Claerbout 1985], and the design of absorbing boundary conditions for numerical simulations [Lindman 1975, Engquist $\&$ Majda 1977]. How can we define a system that behaves like $u _ { t t } = u _ { x x } + u _ { y y }$ for leftgoing waves, say, with negative $x$ -component of velocity, while not propagating rightgoing waves? (The subscripts represent partial derivatives.) A Fourier transform shows that the dispersion relation of such a system should be $\xi = \omega \sqrt { 1 - s ^ { 2 } }$ , where $s = \eta / \omega$ and $\omega , \xi , \eta$ are the dual variables to $t , x , y$ . Only the positive branch of the square root should be present, making this system a pseudodifferential operator. However, a rational approximation ${ \sqrt { 1 - s ^ { 2 } } } \approx r ( s )$ simplifies this to a differential equation. For example, the type $( 2 , 2 )$ Pad´e approximation $r ( s ) = ( 1 - \textstyle { \frac { 3 } { 4 } } s ^ { 2 } ) / ( 1 - \textstyle { \frac { 1 } { 4 } } s ^ { 2 } )$ leads to the PDE $\begin{array} { r } { u _ { x t t } - \frac { 1 } { 4 } u _ { x y y } = u _ { t t t } - \frac { 3 } { 4 } u _ { t y y } } \end{array}$ , sometimes known as the “ $4 5 ^ { \circ }$ equation” because it has high accuracy approximately for angles up to $4 5 ^ { \circ }$ . In this application, rational functions are superior to polynomials both because of higher accuracy in view of the singularities at $s = \pm 1$ , and because polynomial approximations lead to PDEs that are ill-posed [Trefethen $\&$ Halpern 1986].

We have just seen a list of 12 applications. In concluding this chapter I would like to consider what light these may shed on the biggest question of all, namely, What is the use of approximation theory?

To see some possible views, let us go back to 1901. That was the year of Runge’s landmark paper (Chapter 13), whose title was $^ { 1 1 }$

“On Empirical Functions and Interpolation between Equidistant Ordinates.”

In reading this today, one is struck by the word “empirical.” The empirical theme is echoed in the opening sentence:

The relationship between two measurable quantities can, strictly speaking, not be found by observation.

Runge goes on to mention “observations” six times more in the opening paragraph. It would seem that his motivation is the processing of scientific data: interpolation in the traditional sense of evaluating a function at points lying between those at which it is listed in a table.

The next year, 1902, brought another landmark of approximation theory: Kirchberger’s PhD thesis under Hilbert in G¨ottingen, which included the first systematic statement and proof of the equioscillation theorem for polynomial approximation (Theorem 10.1). Here is the first paragraph of Kirchberger’s thesis, as reprinted in the first paragraph of his published paper a year later [1903], setting forth a clear motivation for approximation theory. We may imagine that this was probably also Hilbert’s view of the subject.12

The notion of a function entails the assumption that a numerical value of the function can be calculated for any value of the independent variable. But since the only operations that can really be carried out numerically are the four elementary operations of addition, subtraction, multiplication and division, or strictly speaking only the first three of these, it follows that we are really only masters of more general functions insofar as we can replace them by rational functions, that is, represent them approximately. This highlights the great significance of approximation problems for the whole of mathematics and the special role of approximation by polynomials and rational functions. Indeed, for numerical calculation at least, any use of other approximations such as trigonometric functions presupposes that these can in turn be approximated by rational functions.

Updated to the 21st century, we may say that Kirchberger’s justification of approximation theory is all about machine arithmetic. Approximation by polynomials and rational functions is important, he is saying, because ultimately computers can only carry out polynomial and rational operations.

Both Runge’s emphasis on data and Kirchberger’s emphasis on arithmetic capture aspects of approximation theory that remain valid today. In particular, Kirchberger’s paragraph seems a remarkably clear statement of a justification of approximation theory that in a certain philosophical sense seems almost unarguable (although the line between “primitive” operations like $^ +$ and “derived” ones like $\sin ( \cdot )$ is not always so clear on actual computers, with their multiple levels of hardware, software, and microcode). The same argument is often seen nowadays.

Nevertheless, I do not think data analysis and machine arithmetic get at the heart of why approximation theory is important and interesting. In fact I don’t think Runge’s words even capture the truth of why he was interested in the subject! (He becomes more of a mathematician in the second half of his paper.) What these observations miss is the importance of algorithms.

Let us look again at the list of applications. Kirchberger’s motivation could be said to be on target for #1 and #2 (evaluation of functions, digital filters), and Runge’s for #3, $\# 4$ , and #5 (extrapolation, determination of poles, analytic continuation). But the remaining seven items need to be accounted for in other ways. It is noteworthy that applications #6 to #9 all involve matrices, sometimes of very large dimension (eigenvalues and eigenvectors, model reduction, exponentials of matrices, stiff PDEs). Applications #9 to #12 all involve integrals and differential equations (stiff PDEs, quadrature, adaptive spectral methods, one-way wave equations). In most of these problems we seem a long way from scalars $x$ and $r ( x )$ : the polynomial and rational operations are applied to matrices and operators, not just numbers.

Chebfun provides another interesting data point (for polynomials rather than rational functions). Chebfun is built on a century of developments in polynomial interpolation and approximation, and it makes it possible to work with univariate functions numerically in almost unlimited ways. A particularly important Chebfun capability is finding roots of a function $f ( x )$ , which enables many further operations like computing extrema, absolute values, and 1-norms. Chebfun finds the roots by the algorithm proposed by Good [1961] and Boyd [2002] and described in Chapter 18: approximate $f$ by polynomial interpolants, and then find roots of the polynomials by computing eigenvalues of colleague matrices. This is as powerful an application of approximation theory as one could ask for, but it has little to do with data analysis or machine arithmetic.

Why are polynomial and rational approximations useful? Not because $r ( x )$ is easier to evaluate than $\exp ( x )$ , but because $r ( A )$ is easier to evaluate than $\exp ( A )$ , and $r ( \partial / \partial x )$ is easier to evaluate than $\exp ( \partial / \partial x )$ ! Not because we can evaluate $p ( x )$ , but because we can find its roots !

Summary of Chapter 23. Rational functions are more powerful than polynomials for approximating functions near singularities or on unbounded domains. This is the reason for their importance in approximation theory and approximation practice.

Exercise 23.1. Examples of partial fractions. Express the following functions in partial fraction form: (a) $x ^ { 3 } / ( 1 - x )$ , (b) $x / ( x ^ { 2 } - 4 )$ , (c) $x ^ { 2 } / ( x ^ { 2 } - 4 ) ^ { 2 }$ , (d) $( 1 - x ^ { 3 } ) / ( 1 + x ^ { 2 } )$ . Exercise 23.2. Uses of partial fractions. (a) Express the function $r ( x ) = ( x ( x +$ $1 ) ( x + 2 ) ) ^ { - 1 }$ in partial fraction form. (b) What is its integral from 1 to $t$ ? (c) What is the sum of the infinite series $r ( 1 ) + r ( 2 ) + r ( 3 ) + \cdot \cdot \cdot ?$

Exercise 23.3. Another infinite series. (a) Based on numerical experiments, conjecture a value of the infinite sum $1 / ( 1 \cdot 3 \cdot 5 ) + 2 / ( 3 \cdot 5 \cdot 7 ) + 3 / ( 5 \cdot 7 \cdot 9 ) + \cdot \cdot \cdot .$ (b) Verify your conjecture with partial fractions.

Exercise 23.4. A trigonometric identity. Verify the identity $1 / ( 1 \cdot 3 \cdot 5 ) - 1 / ( 7 \cdot 9 \cdot$ $1 1 ) + 1 / ( 1 3 \cdot 1 5 \cdot 1 7 ) - \cdot \cdot \cdot = \pi / 4 8$ .

Exercise 23.5. Polynomial vs. rational experiments. Produce plots comparing $E _ { 2 n , 0 } ( f )$ and $E _ { n , n } ( f )$ for the following functions $f$ defined on $[ - 1 , 1 ]$ : (a) $\log ( 1 + x ^ { 2 } )$ , (b) $\operatorname { t a n h } ( 5 x )$ , (c) $\exp ( x ) / ( 2 - x )$ .

Exercise 23.6. Approximation of a gamma function. Consider the function $f ( x ) =$ $\Gamma ( x + 2 )$ on $[ - 1 , 1 ]$ , which has simple poles at $x = - 2 , - 3 , \ldots .$ . Determine analytically the geometric convergence rates to be expected as $m \to \infty$ for rational approximants to $f$ of types (a) $( m , 0 )$ , (b) $( m , 1 )$ , (c) $( m , 2 )$ .

# Chapter 24. Rational Best Approximation

Chapter 10 considered best or “minimax” approximation by polynomials, that is, approximation in the $\infty$ -norm, where optimality is characterized by an equioscillating error curve. This chapter presents analogous results for approximation by rational functions. Much remains the same, but a crucial new feature is the appearance in the equioscillation condition of a number known as the defect, which leads to the phenomenon of square blocks of degenerate entries in the “Walsh table” of best approximations. This complication adds a fascinating new dimension to the theory, but it is a complication with destructive consequences in terms of the fragility of rational approximations and the difficulty of computing them numerically. An antidote to some such difficulties may be the use of algorithms based on linearized least-squares and the singular value decomposition, a theme we shall take up in Chapters 26 and 27.

Another new feature in rational approximation is that we must now be careful to distinguish real and complex situations, because of a curious phenomenon: best rational approximations to real functions are in general complex. This effect is intriguing, but it has little relevance to practical problems, so for the most part we shall restrict our attention to approximations in the space $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ consisting of functions in $\mathcal { R } _ { m n }$ with real coefficients.

We will first state the main theorem, then give some examples, and then present a proof. To begin the discussion, we must define the defect. Suppose $r \in \mathcal { R } _ { m n }$ , that is, $r$ is a rational function of type $( m , n )$ . As discussed in the last chapter, this means that $r$ can be written as a fraction $p / q$ in lowest terms with $p$ and $q$ having exact degrees $\mu \leq m$ and $\nu \leq n$ . The defect $d$ of $r$ in $\mathcal { R } _ { m n }$ is the number between $0$ and $n$ defined by

$$
d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0 .
$$

Note that $d$ is a measure of how far both the numerator and the denominator degrees fall short of their maximum allowed values. Thus $( 1 - x ^ { 2 } ) / ( 1 + x ^ { 2 } )$ , for example, has defect $0$ in $\mathcal { R } _ { 2 2 }$ or $\mathcal { R } _ { 2 3 }$ and defect 1 in $\mathcal { R } _ { 3 3 }$ .

A special case to be noted is the situation in which $r = 0$ , that is, $r$ is identically zero. Recall that in this case we defined $\mu = - \infty$ and $\nu = 0$ , so that $r$ is said to have exact type $( - \infty , 0 )$ . The definition (24.1) remains in force in this case, so if $r = 0$ , we say that $T$ has defect $d = n$ in $\mathcal { R } _ { m n }$ , regardless of $m$ .

The reason why defects matter has to do with the counting of zeros. Suppose $r = p / q \in \mathcal { R } _ { m n }$ has exact type $( \mu , \nu )$ and $\tilde { r } = \tilde { p } / \tilde { q }$ is another function in $\mathcal { R } _ { m n }$ . Then we have

$$
r - \tilde { r } = \frac { p } { q } - \frac { \tilde { p } } { \tilde { q } } = \frac { p \tilde { q } - \tilde { p } q } { q \tilde { q } } ,
$$

a rational function of type $( \operatorname* { m a x } \{ \mu + n , m + \nu \} , n + \nu )$ . By (24.1), this implies that $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus $r - \bar { r }$ can have at most $m + n - d$ zeros, and this zero count is a key to equioscillation and uniqueness results.

Here is our main theorem. The study of rational best approximations goes back to Chebyshev [1859], including the idea of equioscillation, though without a precise statement of what form an alternant must take. Existence was first proved by de la Vall´ee Poussin [1911] and Walsh [1931], and equioscillation is due to Achieser [1930].

Theorem 24.1. Equioscillation characterization of best approximants. $A$ real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and a function $r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ is equal to $r ^ { * }$ if and only if $f - r$ equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

“Equioscillation” here is defined just as in Chapter 10. For $f - r$ to equioscillate between $k$ extreme points means that there exists a set of numbers $- 1 \leq x _ { 1 } < \cdot \cdot \cdot <$ $x _ { k } \le 1$ such that

$$
f ( x _ { j } ) - r ( x _ { j } ) = ( - 1 ) ^ { j + i } \| f - r \| , \qquad 1 \leq j \leq k ,
$$

with $i = 0$ or 1. Here and throughout this chapter, $\| \cdot \|$ is the supremum norm.

We now give some examples. To begin with, here is a function with a spike at $x = 0$ :

Polynomial approximations of this function converge rather slowly. For example, it takes $n = 2 0$ to achieve 1 digit of accuracy:

[p,err] $=$ minimax(f,10); subplot(1,2,1), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,err] $=$ minimax(f,20); subplot(1,2,2), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/71364f9cd98091156bcd840d63950feea6cbb1351b11bd535434152b78f2c657.jpg)

Notice that the extreme points of these error curves are distributed all across $[ - 1 , 1 ]$ , even though the challenging part of the function would appear to be in the middle. As discussed in Chapter 16, this is typical of polynomial best approximations.

If we switch to rational approximations, which can also be computed by the Chebfun minimax command [Filip et al. 2018, Pach´on 2010], the accuracy improves. Here we see error curves for approximations of types $( 2 , 2 )$ and $( 4 , 4 )$ , with much smaller errors despite the degrees being low. Note that most of the extreme points are now localized in the middle.

[p,q,rh,err] $=$ minimax(f,2,2); subplot(1,2,1), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,q,rh,err] $=$ minimax(f,4,4); subplot(1,2,2), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/5a158a7a1c8b82ee4e508ef486ec2dd932c1de7544806d4b9e8c107d16725881.jpg)

The error curves just plotted provide good examples of the role of the defect in the characterization of best approximants. The function $f$ is even, and so are its best approximations (Exercise 24.1). Thus we expect that the type $( 2 , 2 )$ , $( 3 , 2 )$ , $( 2 , 3 )$ , and $( 3 , 3 )$ best approximations will all be the same function, a rational function of exact type $( 2 , 2 )$ whose error curve has 7 points of equioscillation. For $( m , n ) =$ $( 2 , 2 )$ , the defect is $0$ and there is one more equioscillation point than the minimum $m + n + 2 - d = 6$ . For $( m , n ) = ( 3 , 2 )$ or $( 2 , 3 )$ , the defect is $0$ and the number of equioscillation points is exactly the minimum $m + n + 2 - d$ . For $( m , n ) = ( 3 , 3 )$ , the defect is $1$ and the number of equioscillation points is again exactly the minimum $m + n + 2 - d$ .

Similarly, the error curve in the plot on the right, with 11 extrema, indicates that this rational function is a best approximation not only of type $( 4 , 4 )$ but also of types $( 5 , 4 )$ , $( 4 , 5 )$ , and $( 5 , 5 )$ .

Here is another example, an odd function:

f = x.\*exp(-5\*abs(abs(x)-.3)); plot(f)

![](images/dae37f7f8c0bd16c20f22e13a193c5feb32662b17dbeaebd0596fb863e222e99.jpg)

If we look for a best approximation of type $( 4 , 5 )$ , we find that the numerator has exact degree 3,

[p,q,rh,err] $=$ minimax(f,4,5); chebcoeffs(p)'

ans $=$

0.0000 0.0154 0.0000 0.0045 and the denominator has exact degree 4,

chebcoeffs(q)'

ans =

0.1468 0.0000 0.1987 0.0000 0.0574

The defect is 1, so there must be at least $4 + 5 + 2 - 1 = 1 0$ extreme points in the error curve. In fact, there are exactly 10:

plot(f-p/q), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/a4eb78e96c299be0b8944715e676a297b9a8a6e5ca0d38788e5458b962e9bf4c.jpg)

We conclude that $r$ is the best approximation of types $( 4 , 4 ) , ( 4 , 5 ) , ( 3 , 4 )$ , and $( 3 , 5 )$ . Let us now turn to the proof of Theorem 24.1. For polynomial approximations, our analogous theorem was Theorem 10.1, whose proof proceeded in four steps:

1. Existence proof via compactness,   
2. Equioscillation $\Rightarrow$ optimality,

3. Optimality equioscillation,

4. Uniqueness proof via equioscillation.

For rational functions, we shall follow the same sequence. The main novelty is in step 1, where compactness must be applied in a subtler way. We shall see an echo of this argument one more time in Chapter 27, in the proof of Theorem 27.1 for Pad´e approximants.

Part 1 of proof: Existence via compactness. For polynomial approximation, in Chapter 10, we noted that $\| f - p \|$ is a continuous function on $\mathcal { P } _ { n }$ , and since one candidate approximation was the zero polynomial, it was enough to look in the bounded subset $\{ p \in { \mathcal { P } } _ { n } : \| f - p \| \leq \| f \| \}$ . Since this set was compact, the minimum was attained.

For rational functions, $\| f - r \|$ is again a continuous function on $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and again it is enough to look in the bounded subset $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| f - r \| \leq \| f \| \}$ or, more simply, the larger bounded set $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| r \| \leq 2 \| f \| \}$ . The difficulty is that bounded sets of rational functions are not, in general, compact. To illustrate this fact, consider the family of functions

$$
r _ { \varepsilon } ( x ) = { \frac { x ^ { 3 } + \varepsilon } { x ^ { 2 } + \varepsilon } } ,
$$

where $\varepsilon > 0$ is a parameter. For each $\varepsilon$ , $r _ { \varepsilon } ( x )$ is a continuous function on $[ - 1 , 1 ]$ with $\| r _ { \varepsilon } \| = 1$ . As $\varepsilon  0$ , however, $r _ { \varepsilon }$ behaves discontinuously:

$$
\operatorname* { l i m } _ { \varepsilon \to 0 } r _ { \varepsilon } ( x ) = { \left\{ \begin{array} { l l } { 1 , } & { x = 0 , } \\ { x , } & { x \neq 0 . } \end{array} \right. }
$$

So we cannot find a limit function $r _ { 0 }$ by taking a limit as $\varepsilon \  \ 0$ . What saves us, however, is that the spaces of numerators and denominators are both compact, so we can argue that the numerators and denominators separately approach limits and , which in this example would be $x ^ { 3 }$ and $x ^ { 2 }$ . We then define a limiting $p _ { 0 }$ $q _ { 0 }$   
rational function by $r _ { 0 } = p _ { 0 } / q _ { 0 }$ and argue by continuity that it has the necessary properties. This kind of reasoning is spelled out in greater generality in [Walsh 1931].

Suppose then that $\{ r _ { k } \}$ is a sequence of functions in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with $\| r _ { k } \| \le 2 \| f \|$ and

$$
\operatorname* { l i m } _ { k \to \infty } \left\| f - r _ { k } \right\| = E = \operatorname* { i n f } _ { r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } } \left\| f - r \right\| .
$$

Write each $r _ { k }$ in the form $p _ { k } / q _ { k }$ with $p _ { k } \in \mathcal { P } _ { m }$ , $q _ { k } \in \mathcal { P } _ { n }$ , $q _ { k } ( x ) \neq 0$ for all $x \in [ - 1 , 1 ]$ , and $\| q _ { k } \| = 1$ ; hence $\| p _ { k } \| \leq \| q _ { k } \| \| r _ { k } \| \leq 2 \| f \|$ . Since $\left\{ p _ { k } \right\}$ and $\left\{ q _ { k } \right\}$ lie in compact sets, we may assume by passing to a subsequence if necessary that $p _ { k } \to p ^ { * }$ and $q _ { k } \to q ^ { * }$ for some $p ^ { * } \in \mathcal { P } _ { m }$ and $q ^ { * } \in \mathcal { P } _ { n }$ . Since $\| q _ { k } \| = 1$ for each $k$ , $\| q ^ { * } \| = 1$ too, and thus $q ^ { * }$ is not identically zero but has at most a finite set of zeros on $[ - 1 , 1 ]$ . Now define $r ^ { * } = p ^ { * } / q ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . For all $x \in [ - 1 , 1 ]$ except perhaps the zeros of $q ^ { * }$ , $| f ( x ) - r ^ { * } ( x ) | = \operatorname* { l i m } _ { k \to \infty } | f ( x ) - r _ { k } ( x ) | \leq E$ . By continuity, the same must hold for all $x \in [ - 1 , 1 ]$ , with $p ^ { * }$ having zeros in $[ - 1 , 1 ]$ wherever $q ^ { * }$ does. Thus $r ^ { * }$ is a best approximation to $f$ .

Part 2 of proof: Equioscillation $\Rightarrow$ optimality. Suppose $f { - } r$ takes equal extreme values with alternating signs at $m + n + 2 - d$ points $x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { m + n + 1 - d }$ , and suppose $\| f - \tilde { r } \| < \| f - r \|$ for some $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then $r - \bar { r }$ must take nonzero values with alternating signs at the equioscillation points, implying that it must take the value zero in at least $m + n + 1 - d$ points in between. However, as observed above, $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus it cannot have $m + n + 1 - d$ zeros unless it is identically zero, a contradiction.

Part 3 of proof: Optimality equioscillation. Suppose $f - r$ equioscillates at fewer than $m + n + 2 - d$ points, and set $E = \| f - r \|$ . Without loss of generality suppose the leftmost extremum is one where $f - r$ takes the value $- E$ . Then by a compactness argument, for all sufficiently small $\varepsilon > 0$ , there are numbers $- 1 < x _ { 1 } < \dots < x _ { k } < 1$ with $k \leq m + n - d$ such that $( f - r ) ( x ) < E - \varepsilon$ for x $ [ - 1 , x _ { 1 } + \varepsilon ] \cup [ x _ { 2 } - \varepsilon , x _ { 3 } + \varepsilon ] \cup [ x _ { 4 } - \varepsilon , x _ { 5 } + \varepsilon ] \cup$ · · · and $( f - r ) ( x ) > - E + \varepsilon$ for $x \in | x _ { 1 } - \varepsilon , x _ { 2 } + \varepsilon | \cup | x _ { 3 } - \varepsilon , x _ { 4 } + \varepsilon | \cup \cdot \cdot \cdot$ . Let $r$ be written in the form $p / q$ , where $p$ has degree $\mu \leq m - d$ and $q$ has degree $\nu \leq n - d$ , with $p$ and $q$ having no roots in common. The proof now consists of showing that $r$ can be perturbed to a function $\tilde { r } = ( p + \delta p ) / ( q + \delta q ) \in \mathcal { R } _ { m n }$ with the properties that $\| \tilde { r } - r \| < \varepsilon$ and $\bar { r } - r$ is strictly negative for $x \in [ - 1 , x _ { 1 } - \varepsilon ] \cup [ x _ { 2 } + \varepsilon , x _ { 3 } - \varepsilon ] \cup [ x _ { 4 } + \varepsilon , x _ { 5 } - \varepsilon ] \cup \cdot \cdot \cdot$ and strictly positive for $x \in | x _ { 1 } + \varepsilon , x _ { 2 } - \varepsilon | \cup | x _ { 3 } + \varepsilon , x _ { 4 } - \varepsilon | \cup \cdot \cdot \cdot$ . Such a function $\tilde { r }$ will have error less than $E$ throughout the whole interval $\lfloor - 1 , 1 \rfloor$ . We calculate

$$
\tilde { r } = \frac { p + \delta p } { q + \delta q } = \frac { ( p + \delta p ) ( q - \delta q ) } { q ^ { 2 } } + O ( \lVert \delta q \rVert ^ { 2 } )
$$

and therefore

$$
\tilde { r } - r = \frac { q \delta p - p \delta q } { q ^ { 2 } } + O ( \| \delta p \| \| \delta q \| + \| \delta q \| ^ { 2 } ) .
$$

We are done if we can show that $\delta p$ and $\delta \boldsymbol { q }$ can be chosen so that $q \delta p - p \delta q$ is a nonzero polynomial of degree exactly $k$ with roots $x _ { 1 } , \ldots , x _ { k }$ ; by scaling this $\delta p$ and $\delta \boldsymbol { q }$ sufficiently small, the quadratic terms above can be made arbitrarily small relative to the others, so that the required $\varepsilon$ conditions are satisfied. This can be shown by the Fredholm alternative of linear algebra. The map from the $( m + n + 2 )$ - dimensional set of choices of $\delta p$ and $\delta \boldsymbol { q }$ to the $( m + n + 1 - d )$ -dimensional space of polynomials $q \delta p - p \delta q$ is linear. To show the map is surjective, it is enough to show that its kernel has dimension $d + 1$ but no more. Suppose then that $q \delta p - p \delta q$ is zero, that is, $q \delta p = p \delta q$ . Then since $p$ and $q$ have no roots in common, all the roots of $p$ must be roots of $\delta p$ and all the roots of $q$ must be roots of $\delta \boldsymbol { q }$ . In other words we must have $\delta p = g p$ and $\delta q = g q$ for some polynomial $g$ . Since $\delta p$ has degree no greater than $m$ and $\delta \boldsymbol { q }$ has degree no greater than $n$ , $g$ can have degree no greater than $d$ . The set of polynomials of degree $d$ has dimension $d + 1$ , so we are done.

Part 4 of proof: Uniqueness via equioscillation. Finally, to prove uniqueness, suppose $r$ is a best approximation whose error curve equioscillates between extreme points at $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then (without loss of generality) $x _ { 0 } < x _ { 1 } < \dots < x _ { m + n + 1 - d }$ , and suppose $( r - \tilde { r } ) ( x )$ must be $\| f - \tilde { r } \| \leq \| f - r \|$ $\leq 0$ at $x _ { 0 } , x _ { 2 } , x _ { 4 } , \ldots$ for some and $\geq 0$ at $x _ { 1 } , x _ { 3 } , x _ { 5 } , \ldots$ . This implies that $r - \tilde { r }$ has roots in each of the $m + n +$ $1 - d$ closed intervals $[ x _ { 0 } , x _ { 1 } ] , \dotsc , [ x _ { m + n - d } , x _ { m + n + 1 - d } ]$ , and since $r - \tilde { r }$ is a rational function of type $( m + n - d , 2 n - d )$ , the same must hold for its numerator polynomial. We wish to conclude that its numerator polynomial has at least $m + n + 1 - d$ roots in total, counted with multiplicity, implying that $r = \tilde { r }$ . The argument for this is the same as given in the proof of Theorem 10.1.

We have now finished the substantial mathematics. It is time to look at some of the consequences.

One of the recurring themes in the subject of rational approximation is the phenomenon of square blocks in the Walsh table. Suppose that a real function $f \in$ $C ( [ - 1 , 1 ] )$ is given, and consider the set of all of its real rational best approximations of type $( m , n )$ for various $m , n \geq 0$ . We can imagine these laid out in an array, with $m$ along the horizontal and $n$ along the vertical. This array is called the Walsh table for $f$ [Walsh 1934].

Generically, all the entries in the Walsh table for a given $f$ will be distinct, and in this case we say that $f$ is normal. Sometimes, however, certain entries in the table may be repeated, and in fact this is a frequent occurrence because it happens whenever $f$ is even or odd. If $f$ is even, then for any nonnegative integers $j$ and $k$ , all of its rational approximations of types $( 2 j , 2 k )$ , $( 2 j + 1 , 2 k )$ , $( 2 j , 2 k + 1 )$ , and $( 2 j + 1 , 2 k + 1 )$ must be the same. Similarly, if $f$ is odd, then all of its approximations of types $( 2 j + 1 , 2 k )$ , $( 2 j + 2 , 2 k )$ , $( 2 j + 1 , 2 k + 1 )$ , and $( 2 j + 2 , 2 k + 1 )$ must be the same. We have already seen a number of examples.

More generally, repeated entries or “degeneracies” in the Walsh table may take complicated forms. Nevertheless the equioscillation condition imposes quite a bit of structure on the chaos. Degeneracies always appear precisely in a pattern of square blocks. The following statement of this result is taken from [Trefethen 1984], where a discussion of various aspects of this and related problems can be found. We shall return to the subject of square blocks in Chapter 27, on Pad´e approximation.

Theorem 24.2. Square blocks in the Walsh table. The Walsh table of best real rational approximants to a real function $f \in C ( [ - 1 , 1 ] )$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. Given a nonrational function $f$ , let $r \neq 0$ be a best approximation in $\mathcal { R } _ { \mu \nu } ^ { \mathrm { r e a . } }$ l of exact type $( \mu , \nu )$ . (The cases of rational $f$ or $r = 0$ can be handled separately.) By Theorem 24.1, the number of equioscillation points of $f - r$ is $\mu + \nu + 2 + k$ for some integer $k \geq 0$ . We note that $r$ is an approximation to $f$ in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ for any $m \geq \mu$ and $n \geq \nu$ , and the defect is $\operatorname* { m i n } \{ m - \mu , n - \nu \}$ . Thus by Theorem 24.1, $r$ is the best approximation to $f$ precisely for those values of $( m , n )$ satisfying $m \geq \mu$ , $n \geq \nu$ , and $\mu + \nu + 2 + k \geq m + n + 2 - \operatorname* { m i n } \{ m - \mu , n - \nu \}$ . The latter condition simplifies to $n \leq \nu + k$ and $m \leq \mu + k$ , showing that $r$ is the best approximation to $f$ precisely in the square block $\mu \leq m \leq \mu + k$ , $\nu \leq n \leq \nu + k$ .

Within a square block in the Walsh table, the defect $d$ is equal to zero precisely in the first column and the first row. An approximation with $d = 0$ is sometimes said to be nondegenerate. It can have more points of equioscillation than the generic number $m + n + 2$ , but never fewer.

As mentioned above, the theory of equioscillation and degeneracies is very appealing mathematically. As an example we note a result due to Werner [1964], in completion of earlier work of Maehly and Witzgall [1960]: the type $( m , n )$ best approximation operator, which maps functions $f$ to their best approximations $r _ { m n } ^ { * }$ , is continuous at $f$ with respect to the supremum norm if and only if $f \in \mathcal { R } _ { m n }$ or the corresponding function $r _ { m n } ^ { * }$ is nondegenerate. The essential reason for this effect is that if a function $r ^ { * }$ is the best approximation to $f$ in a nontrivial square block, then a small perturbation $f  { \ddot { f } }$ might fracture that block into smaller pieces [Trefethen 1984]. If $( m , n )$ corresponds to a degenerate position in the block, with $d > 0$ , then the best approximation $\tilde { r } ^ { * }$ for such an $\ddot { f }$ might need to have a higher equioscillation number than that of $r ^ { * }$ for $f$ , requiring $\tilde { r } ^ { * }$ to be far from $r ^ { * }$ if $\| f - r ^ { * } \|$ is positive.

These complications hint at some of the practical difficulties of rational approximation. For example, the Remez algorithm is based on explicit manipulation of alternant sets. If the number of extremal points is not known a priori, it is plausible that one may expect numerical difficulties in certain circumstances. Indeed, this is the case, and so far as I am aware, no implementation of the Remez algorithm for rational approximation, including that of Chebfun, can be called fully robust. Other kinds of algorithms may have better prospects.

We finish by returning to the matter of best complex approximations to real functions. Nonuniqueness of certain complex rational approximations was pointed out by Walsh in the 1930s. Later Lungu [1971] noticed, following a suggestion of Gonchar, that the nonuniqueness arises even for approximation of a real function $f$ on $[ - 1 , 1 ]$ , with examples as simple as type $( 1 , 1 )$ approximation of $| x |$ . (Exercise 24.3 gives another proof that there must exist such examples.) These observations were rediscovered independently by Saff and Varga [1978a]. Ruttan [1981] showed that complex best approximations are always better than real ones in the strict lower-right triangle of a square block, that is, when a type $( m , n )$ best approximation equioscillates in no more than $m + n + 1$ points. Trefethen and Gutknecht [1983a] showed that for every $( m , n )$ with $n \geq m + 3$ , examples exist where the ratio of the optimal complex and real errors is arbitrarily small. Levin, Ruttan, and Varga showed that the minimal ratio is exactly $1 / 3$ for $n = m + 2$ and exactly $1 / 2$ for $1 \leq n \leq m + 1$ [Ruttan & Varga 1989]. None of this has much to do with practical approximation, but it is fascinating.

Summary of Chapter 24. Any real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { \ast } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with respect to the $\infty$ -norm, and $r ^ { * }$ is characterized by having an error curve that equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . In the Walsh table of all best approximations to $f$ indexed by $m$ and $n$ , repeated entries, if any, lie in exactly square blocks.

Exercise 24.1. Approximating even functions. Prove that if a real function $f \in$ $C ( [ - 1 , 1 ] )$ is even, then its real best approximations of all types $( m , n )$ are even.

Exercise 24.2. Approximating the Gaussian. The first figures of this chapter considered lower degree polynomial and rational approximations of $\exp ( - 1 0 0 x ^ { 2 } )$ on $[ - 1 , 1 ]$ . Make a plot of the errors in approximations of types $( n , 0 )$ and $( n , n )$ , now taking $n$ as high as you can. (You may find that the cf command takes you farther than minimax.) How do the polynomial and rational approximations compare?

Exercise 24.3. Complex approximations and nonuniqueness. (a) Suppose a real function $f \in C ( [ - 1 , 1 ] )$ takes both the values 1 and $^ { - 1 }$ . Prove that no real rational function $r \in \mathcal { R } _ { 0 n } ^ { \mathrm { r e a l } }$ , for any $n$ , can have $\| f - r \| < 1$ . (b) On the other hand, show that for any $\varepsilon > 0$ , there is a complex rational function $r \in \mathcal { R } _ { 0 n }$ for some $n$ with $\| f - r \| < \varepsilon$ . (Hint: Perturb $f$ by an imaginary constant and consider its reciprocal.) (c) Conclude that type $( 0 , n )$ complex rational best approximations in $C ( [ - 1 , 1 ] )$ are nonunique in general for large enough $_ n$ .

Exercise 24.4. A function with a spike. Plot chebfuns of the function (24.2) for $\varepsilon = 1 , 0 . 1 , \dots , 1 0 ^ { - 6 }$ and determine the polynomial degree $n ( \varepsilon )$ of the chebfun in each case. What is the observed asymptotic behavior of $n ( \varepsilon )$ as $\varepsilon  0$ ? How accurately can you explain this observation based on the theory of Chapter 8?

Exercise 24.5. de la Vall´ee Poussin lower bound. Suppose an approximation $r \in$ $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } < s _ { 1 } < \cdot \cdot \cdot < s _ { m + n + 1 - d } \leq 1$ at which $f - r$ alternates in sign with $| f ( s _ { j } ) - r ( s _ { j } ) | \geq$ $\varepsilon$ for some $\varepsilon > 0$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . Show that the best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ satisfies $\| \boldsymbol { f } - \boldsymbol { r } ^ { * } \| \ge \varepsilon$ . (Compare Exercise 10.3.)

Exercise 24.6. A rational lethargy theorem. Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Adapt the proof of Exercise 10.7 to show that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - r _ { n n } ^ { * } \| \geq \varepsilon { n }$ for all $_ n$ .

Exercise 24.7. Approximation of $e ^ { z }$ . Equation (10.2) gave an asymptotic formula for the accuracy of polynomial best approximations to $e ^ { z }$ on $[ - 1 , 1 ]$ . The generalization to rational best approximations is

$$
E _ { m n } \sim \frac { m ! n ! } { 2 ^ { m + n } ( m + n ) ! ( m + n + 1 ) ! } , \quad m + n \to \infty
$$

(conjectured by Meinardus [1967], proved by Braess [1984]). Produce a table of numerically computed best approximation errors for $0 \leq m + n \leq 1 2$ . How well do these numbers match the asymptotic formula?

# Chapter 25. Two Famous Problems

In this chapter we discuss two problems of rational approximation that have been the focus of special attention over the years: approximation of $| x |$ on $[ - 1 , 1 ]$ , a prototype of approximation of nonsmooth functions, and approximation of $e ^ { x }$ on $( - \infty , 0 ]$ , a prototype of approximation on unbounded domains. Both stories go back many decades and feature initial theorems, later conjectures based on numerical experiments, and eventual proofs of the conjectures based on mathematical methods related to potential theory. We shall not present the proofs of the sharpest results, but we shall show that the essential rates of approximation can be achieved by using the trick that appears several times in this book: if a function $f ( x )$ can be written as an integral with respect to a variable $s$ , then an approximation $r ( x )$ in partial fractions form is obtained by applying a quadrature formula (19.3) to the integral.

The problem of approximation of $| x |$ on $[ - 1 , 1 ]$ originates at the beginning of the 20th century, when polynomial approximations of this function were of interest to Lebesgue, de la Vall´ee Poussin, Jackson, and Bernstein (Exercise 6.5). This was an era when the fundamental results of approximability were being developed, and $| x |$ served as a function from which many other results could be derived. Bernstein’s prize-winning article on the subject ran for 104 pages [1912b] and was followed by another of 57 pages [1914b]. Among other things, Bernstein proved that in best polynomial approximation of $| x |$ as $n  \infty$ , the errors decrease linearly but no faster, that is, at the rate $O ( n ^ { - 1 } )$ but not $o ( n ^ { - 1 } )$ .

Why linearly? This is an example of the fundamental principle mentioned first in Chapter 7: the close connection between the smoothness of a function and its rate of approximation. The function $f ( x ) = | x |$ has a derivative of bounded variation $V = 2$ on $[ - 1 , 1 ]$ , so by Theorem 7.2, its Chebyshev projections $\{ f _ { n } \}$ satisfy

$$
\| f - f _ { n } \| \leq { \frac { 4 } { \pi ( n - 1 ) } }
$$

for $n \geq 2$ , and its Chebyshev interpolants $\left\{ p _ { n } \right\}$ satisfy the same bound with 4 replaced by 8. Thus approximations to $| x |$ converge at least at the rate $O ( n ^ { - 1 } )$ . What Bernstein showed is that the rate is in fact no better than this: no approximations to $| x |$ can beat Chebyshev projection or interpolation by more than a constant factor. Or to put it another way, convergence of polynomial approximants to a function $f$ at a rate faster than $O ( n ^ { - 1 } )$ implies that $f$ is in some sense smoother than $| x |$ . Such results in the direction approximability $\Longrightarrow$ smoothness go by the general name of Bernstein theorems. In this book we have presented one result of this kind, Theorem 8.3, asserting that geometric convergence implies analyticity.

It is hard not to be curious about the constants. Bernstein in fact proved in [Bernstein 1914b] that there exists a number $\beta$ such that the best approximation errors satisfy

$$
E _ { n } ( | x | ) \sim { \frac { \beta } { n } }
$$

as $n \to \infty$ , and he obtained the bound

$$
0 . 2 7 8 < \beta < 0 . 2 8 6 .
$$

(Theorem 7.2 gives $\beta \leq 4 / \pi \approx 1 . 2 7 .$ .) He noted as a “curious coincidence” that $1 / 2 \sqrt { \pi } \approx 0 . 2 8 2 0 9 \ldots$ falls in this range, and the idea that $\beta$ might take exactly this value became known as Bernstein’s conjecture. Seventy years later, Varga and Carpenter [1985] investigated the problem numerically to great accuracy and found that in fact

$$
\beta \approx 0 . 2 8 0 1 6 9 4 9 9 0 2 3 8 6 9 1 3 3 0 3 6 4 3 6 4 9 \ldots
$$

(Of course the difference between 0.282 and 0.280 would not have the slightest practical importance.) Along with this numerical result, which was based on Richardson extrapolation, Varga and Carpenter established the rigorous bounds

$$
0 . 2 8 0 1 6 8 5 < \beta < 0 . 2 8 0 1 7 3 4 .
$$

For example, here are the values of $n E _ { n } ( | x | )$ for $n = 1 , 2 , 4 , \dots , 6 4$ , showing quadratic convergence to the limit value. A comparison with the much more accurate Table 2.1 of [Varga & Carpenter 1985] indicates that the Chebfun results are accurate in all but the last digit or two.

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); f = abs(x); limit $=$ 0.280169499023869133;   
for n = 2.^(0:6) [p,err] $=$ minimax(f,n); fprintf('%14d %16.8f %16.2e\n',n,n\*err,n\*err-limit)   
end

<table><tr><td>n</td><td>n*err</td><td>n*err - limit</td></tr><tr><td>1</td><td>0.50000000</td><td>2.20e-01</td></tr><tr><td>2</td><td>0.25000000</td><td>-3.02e-02</td></tr><tr><td>4</td><td>0.27048360</td><td>-9.69e-03</td></tr><tr><td>8</td><td>0.27751782</td><td>-2.65e-03</td></tr><tr><td>16</td><td>0.27948884</td><td>-6.81e-04</td></tr><tr><td>32</td><td>0.27999815</td><td>-1.71e-04</td></tr><tr><td>64</td><td>0.28012659</td><td>-4.29e-05</td></tr></table>

Now all this is for polynomial approximation. What about rational functions? As mentioned in Chapter 23, the dramatic discovery here came from Donald Newman, 50 years after Bernstein: best rational approximants to $| x |$ converge “rootexponentially.” Newman’s bounds were these:

$$
\frac { 1 } { 2 } e ^ { - 9 \sqrt { n } } \leq E _ { n n } ( | x | ) \leq 3 e ^ { - \sqrt { n } } .
$$

We have already seen in the second plot of Chapter 23 what an improvement in convergence rate this is as compared with (25.1). For approximating nonsmooth functions, rational functions can be far more powerful than polynomials.

Again mathematicians could not resist trying to sharpen the constants. First, Vyacheslavov [1975] found that the exact exponent is midway between Newman’s bounds of 1 and 9: it is $\pi$ . Then Varga, Ruttan, and Carpenter [1993] performed computations with a version of the Remez algorithm to 200 decimal places, leading to numerical evidence for the conjecture

$$
E _ { n n } \sim 8 e ^ { - \pi { \sqrt { n } } }
$$

as $n  \infty$ . Soon afterward this result was proved by Stahl [1993]. Later Stahl generalized the result to approximation of $x ^ { \alpha }$ on $[ 0 , 1 ]$ for any $\alpha > 0$ [Stahl 2003].

The following theorem summarizes the results we have mentioned.

Theorem 25.1. Approximation of $| x |$ on $[ - 1 , \bf 1 ]$ . The errors in best polynomial and rational approximation of $| x |$ on $[ - 1 , 1 ]$ satisfy as $n \to \infty$

$$
E _ { n 0 } ( | x | ) \sim \frac { \beta } { n } , \quad \beta = 0 . 2 8 0 1 \ldots ,
$$

and

$$
E _ { n n } ( \vert x \vert ) \sim 8 e ^ { - \pi { \sqrt { n } } } .
$$

Proof. Equation (25.4) is due to Varga and Carpenter [1985], and (25.5) is due to Stahl [1993].

Why can rational approximations of $| x |$ achieve $O ( C ^ { - \sqrt { n } } )$ accuracy? The crucial fact is that the poles of $r$ can be chosen to cluster near the singular point $x = 0$ . In particular, a good choice is to make the poles approach 0 geometrically, for each fixed $n$ , with a geometric factor depending on $\sqrt { n }$ .

Here is a derivation of a rational approximation that achieves the right rootexponential convergence. (Arguments like this have been made by Stenger in various publications; see, for example, [Stenger 1986].) We start from the identity

$$
\frac { 1 } { | x | } = \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } \frac { d t } { t ^ { 2 } + x ^ { 2 } } ,
$$

which is derived in calculus courses. Multiplying by $x ^ { 2 }$ gives

$$
| x | = { \frac { 2 x ^ { 2 } } { \pi } } \int _ { 0 } ^ { \infty } { \frac { d t } { t ^ { 2 } + x ^ { 2 } } } .
$$