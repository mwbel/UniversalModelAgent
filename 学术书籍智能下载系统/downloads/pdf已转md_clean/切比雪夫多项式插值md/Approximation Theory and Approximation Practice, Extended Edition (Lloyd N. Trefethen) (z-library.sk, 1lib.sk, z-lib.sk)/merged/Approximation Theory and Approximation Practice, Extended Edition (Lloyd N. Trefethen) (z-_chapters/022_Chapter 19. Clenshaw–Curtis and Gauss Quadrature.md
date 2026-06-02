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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/23226133b7fe630874e30104b8115d38e008ccede804b35a99658e2c5102e39a.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/639b448a0f07d31574bc929f9f98732f9f97b44ce42c761b34b656ee01eca676.jpg)

This behavior is typical: for smaller values of $n$ , Clenshaw–Curtis (dots) and Gauss quadrature (stars) have similar accuracy, not a difference of a factor of 2. This effect was pointed out by Clenshaw and Curtis in their original paper [1960]. Only at a sufficiently large value of $n$ , if the integrand is analytic, does a kink appear in the Clenshaw–Curtis convergence curve, whose further convergence is then about half as fast as before. An explanation of this effect based on ideas of rational approximation is given in Figures 4–6 of [Trefethen 2008], and another explanation based on aliasing can be derived from Theorems 4.2 and 19.2 and goes back to O’Hara and Smith [1968] (Exercise 19.4). For a full analysis, see [Weideman $\&$ Trefethen 2007a].

Here is a similar comparison for the harder integral (19.11):

I = sum(f); $\mathtt { n n } \ = \ 5 0 : 5 0 : 2 0 0 0$ ;   
errcc $= ~ [ ]$ ; errgauss $=$ [];   
for $\texttt { n } = \texttt { n n }$ Icc $=$ sum(chebfun(ff, $\tt { n } { + } 1 \tt {  }$ )); errcc $=$ [errcc abs(I-Icc)]; [s,w] = legpts $\left( \mathtt { n } + 1 \right)$ ; Igauss $=$ w\*ff(s); errgauss $=$ [errgauss abs(I-Igauss)];   
end   
semilogy(nn,errcc,'.-'), hold on, semilogy(nn,errgauss,'h-m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/ae74f1a813ebbd75928cab325bc2c247f387fd0a9f4ee4b4e3cfea080ba54d6c.jpg)

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
