# Chapter 4. Interpolants, Projections, and Aliasing

Suppose $f ( x )$ is a Lipschitz continuous function on $[ - 1 , 1 ]$ with Chebyshev series coefficients $\{ a _ { k } \}$ as in Theorem 3.1,

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

One approximation to $f$ in $\mathcal { P } _ { n }$ is the polynomial obtained by interpolation in Chebyshev points:

$$
p _ { n } ( x ) = \sum _ { k = 0 } ^ { n } c _ { k } T _ { k } ( x ) .
$$

Another is the polynomial obtained by truncation or projection of the series to degree $n$ , whose coefficients through degree $n$ are the same as those of $f$ itself:

$$
f _ { n } ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } T _ { k } ( x ) .
$$

The relationship of the Chebyshev coefficients of $f _ { n }$ to those of $f$ is obvious, and in a moment we shall see that the Chebyshev coefficients of $p _ { n }$ have simple expressions too. In computational work generally, and in particular in Chebfun, the polynomials $\left\{ p _ { n } \right\}$ are usually almost as good approximations to $f$ as the polynomials $\left\{ f _ { n } \right\}$ and are easier to work with, since one does not need to evaluate the integral (3.12). The polynomials $\left\{ f _ { n } \right\}$ , on the other hand, are also interesting. In this book, most of our computations will make use of $\left\{ p _ { n } \right\}$ , but many of our theorems will treat both cases. A typical example is Theorem 8.2, which asserts that if $f$ is analytic on $[ - 1 , 1 ]$ , then both $\| f - f _ { n } \|$ and $\| f - p _ { n } \|$ decrease geometrically to $0$ as $n \to \infty$ .

The key to understanding $\left\{ c _ { k } \right\}$ is the phenomenon of aliasing, a term that originated with radio engineers early in the 20th century. On the $( n { + } 1 )$ -point Chebyshev grid, it is obvious that any function $f$ is indistinguishable from a polynomial of degree $n$ . But something more is true: any Chebyshev polynomial $T _ { N }$ , no matter how big $N$ is, is indistinguishable on the grid from a single Chebyshev polynomial $T _ { m }$ for some $m$ with $0 \leq m \leq n$ . We state this as a theorem.

Theorem 4.1. Aliasing of Chebyshev polynomials. For any $n \geq 1$ and $0 ~ \leq ~ m ~ \leq ~ n$ , the following Chebyshev polynomials take the same values on the $( n + 1 )$ -point Chebyshev grid:

$$
T _ { m } , T _ { 2 n - m } , T _ { 2 n + m } , T _ { 4 n - m } , T _ { 4 n + m } , T _ { 6 n - m } , . . . .
$$

Equivalently, for any $k \geq 0$ , $T _ { k }$ takes the same value on the grid as $T _ { m }$ with

$$
m = | ( k + n - 1 ) ( { \bmod { 2 n } } ) - ( n - 1 ) | ,
$$

a number in the range $0 \leq m \leq n$ .

Proof. Recall from (2.1) and (3.8) that Chebyshev polynomials on $[ - 1 , 1 ]$ are related to monomials on the unit circle by $T _ { m } ( x ) = ( z ^ { m } + z ^ { - m } ) / 2$ , and Chebyshev points are related to $( 2 n ) \mathrm { t h }$ roots of unity by $x _ { n } = ( z _ { n } + z _ { n } ^ { - 1 } ) / 2$ . It follows that the first assertion of the theorem is equivalent to the statement that the following functions take the same values at the $( 2 n ) \mathrm { t h }$ roots of unity:

$$
z ^ { m } + z ^ { - m } , \ z ^ { 2 n - m } + z ^ { m - 2 n } , \ z ^ { 2 n + m } + z ^ { - 2 n - m } , \cdot \cdot \cdot \cdot
$$

Inspection of the exponents shows that in every case, modulo $2 n$ , we have one exponent equal to $+ m$ and the other to $- m$ . The conclusion now follows from the elementary phenomenon of aliasing of monomials on the unit circle: at the $( 2 n ) \mathrm { t h }$ roots of unity, $z ^ { 2 \nu n } = 1$ for any integer $\nu$ .

For the second assertion (4.4), suppose first that $0 \leq k \left( { \bmod { 2 } } n \right) \leq n$ . Then $n - 1 \leq ( k + n - 1 ) ( { \bmod { 2 n } } ) \leq 2 n - 1$ , so (4.4) reduces to $m = k ( { \bmod { 2 } } n )$ , with $0 \leq m \leq n$ , and we have just shown that this implies that $T _ { k }$ and $T _ { m }$ take the same values on the grid. On the other hand, suppose that $n + 1 \leq k { \bigl ( } { \mathrm { m o d } } 2 n { \bigr ) } \leq 2 n - 1$ . Then $0 \leq ( k + n - 1 ) ( { \bmod { 2 n } } ) \leq n - 2$ , so the absolute value becomes a negation and (4.4) reduces to $m = ( - k ) ( { \bmod { 2 } } n )$ , with $1 \leq m \leq n - 1$ . Again we have just shown that this implies that $T _ { k }$ and $T _ { m }$ take the same values on the grid.

Here is a numerical illustration of Theorem 4.1. Taking $n = 4$ , let $\mathtt { X }$ be the Chebyshev grid with $n { \mathrel { + { 1 } } }$ points, and let $T \{ 1 \} , \ldots , T \{ 1 0 \}$ be the first 10 Chebyshev polynomials:

Then $T _ { 3 }$ and $T _ { 5 }$ are the same on the grid:

disp([T{3}(X) T{5}(X)])

T3 T5   
-1.000000000000000 -1.000000000000000   
0.707106781186548 0.707106781186547   
0 0   
-0.707106781186548 -0.707106781186547   
1.000000000000000 1.000000000000000

So are $T _ { 1 }$ , $T _ { 7 }$ , and $T _ { 9 }$ :

disp([T{1}(X) T{7}(X) T{9}(X)])

T1 T7 T9   
-1.000000000000000 -1.000000000000000 -1.000000000000000   
-0.707106781186547 -0.707106781186548 -0.707106781186547   
0 0 0   
0.707106781186547 0.707106781186548 0.707106781186547   
1.000000000000000 1.000000000000000 1.000000000000000

As a corollary of Theorem 4.1, we can now derive the connection between $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ . The following result can be found in [Clenshaw & Curtis 1960].

Theorem 4.2. Aliasing formula for Chebyshev coefficients. Let $f$ be Lipschitz continuous on $[ - 1 , 1 ]$ , and let $p _ { n }$ be its Chebyshev interpolant in $\mathcal { P } _ { n }$ , $n \geq 1$ . Let $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ be the Chebyshev coefficients of $f$ and $p _ { n }$ , respectively. Then

$$
\begin{array} { l } { { c _ { 0 } = a _ { 0 } + a _ { 2 n } + a _ { 4 n } + \cdots , } } \\ { { } } \\ { { c _ { n } = a _ { n } + a _ { 3 n } + a _ { 5 n } + \cdots , } } \end{array}
$$

and for $1 \leq k \leq n - 1$ ,

$$
c _ { k } = a _ { k } + ( a _ { k + 2 n } + a _ { k + 4 n } + \cdot \cdot \cdot ) + ( a _ { - k + 2 n } + a _ { - k + 4 n } + \cdot \cdot \cdot ) .
$$

Proof. By Theorem 3.1, $f$ has a unique Chebyshev series (3.11), and it converges absolutely. Thus we can rearrange the terms of the series without affecting convergence, and in particular, each of the three series expansions written above converges since they correspond to the Chebyshev series (3.11) evaluated at $x = 1$ . So the formulas (4.5)–(4.7) do indeed define certain numbers $c _ { 0 } , \ldots , c _ { n }$ . Taking these numbers as coefficients multiplied by the corresponding Chebyshev polynomials $T _ { 0 } , \ldots , T _ { n }$ gives us a polynomial of degree $n$ . By Theorem 4.1, this polynomial takes the same values as $f$ at each point of the Chebyshev grid. Thus it is the unique interpolant $p _ { n } \in \mathcal { P } _ { n }$ .

We can summarize Theorem 4.2 as follows. On the $( n + 1 )$ -point grid, any function $f$ is indistinguishable from a polynomial of degree $n$ . In particular, the Chebyshev series of the polynomial interpolant to $f$ is obtained by reassigning all the Chebyshev coefficients in the infinite series for $f$ to their aliases of degrees 0 through $n$ .

As a corollary, Theorems 4.1 and 4.2 give us absolutely convergent series for $f - f _ { n }$ and $f - p _ { n }$ , which we shall exploit in Chapters 7 and 8:

$$
f ( x ) - f _ { n } ( x ) = \sum _ { k = n + 1 } ^ { \infty } a _ { k } T _ { k } ( x ) ,
$$

$$
f ( x ) - p _ { n } ( x ) = \sum _ { k = n + 1 } ^ { \infty } a _ { k } ( T _ { k } ( x ) - T _ { m } ( x ) ) ,
$$

where $m = m ( k , n )$ is given by (4.4).

To illustrate Theorem 4.2, here is the function $f ( x ) = \operatorname { t a n h } ( 4 x - 1 )$ (solid) and its degree 4 Chebyshev interpolant $p _ { 4 } ( x )$ (dashed):

x = chebfun('x'); f = tanh( $4 * \mathbf { x } - 1 )$ ; $\mathrm { ~ n ~ } = \mathrm { ~ 4 ~ }$ ; pn $=$ chebfun(f, $\ n { + } 1 $ ); plot(f), hold on, plot(pn,'.--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/84418133a7618ae8edae1555741d0d56e9de746ebecdc608b0af410e69a41275.jpg)

The first 5 Chebyshev coefficients of $f$ , a $=$ chebpoly(f); a = a(end:-1:1)'; a(1:n+1)

ans $=$   
-0.166584582703135   
1.193005991160944   
0.278438064117869   
-0.239362401056012   
-0.176961398392888

are different from the Chebyshev coefficients of $p _ { n }$ ,

c $=$ chebpoly(pn); c $=$ c(end:-1:1)'   
c = -0.203351068209675 1.187719968517890 0.379583465333916 -0.190237989543227 -0.178659622412173

As asserted in (4.5) and (4.6), the coefficients $c _ { 0 }$ and $c _ { n }$ are given by sums of coefficients $a _ { k }$ with a stride of $2 n$ :

c0 = sum(a(1:2\*n:end)), cn = sum(a(n+1:2\*n:end))

$\mathsf { c 0 } \ = \ - 0 \ . 2 0 3 3 5 1 0 6 8 2 0 9 6 7 5$ $\mathtt { c n } \ = \ - 0 . 1 7 8 6 5 9 6 2 2 4 1 2 1 7 4$

And as asserted in (4.7), the coefficients $c _ { 1 }$ through $c _ { n - 1 }$ involve two sums of this kind:

for $\mathtt { k } \ = \ 1 { : } \mathtt { n - 1 }$ ck $=$ sum(a(1+k:2\*n:end)) + sum(a(1-k+2\*n:2\*n:end))   
end

ck = 1.187719968517889   
ck = 0.379583465333916   
ck = -0.190237989543227

Following up on the last figure, how does the truncated series $f _ { n }$ compare with the interpolant $p _ { n }$ as an approximation to $f$ ? Chebfun includes a 'trunc' option for computing $f _ { n }$ , which we now add to the plot as a dot-dash line:

fn $=$ chebfun(f,'trunc', $\tt { n } { + } 1$ ); plot(fn,'-.g')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/c3400146e9e81a4fe3f33873b958a85347149eefbc2cba3306720e9892245901.jpg)

Here are the errors $f - f _ { n }$ and $f - p _ { n }$ :

subplot(1,2,1), plot(f-fn, $" \mathtt { g } ^ { \prime }$ ), subplot(1,2,2), plot(f-pn,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/2b24a7bbb741c1e16f18e5ca8d1105d962920a71e53b9ba4b0aaed099e3195ee.jpg)

Here is the analogous plot with $n = 4$ increased to 24:

$\tt { n } = 2 4$ ; pn $=$ chebfun(f, $\mathtt { n } + 1 )$ ; fn $=$ chebfun(f,'trunc', $\ n { + } 1 \cdot$ ); subplot(1,2,1), plot(f-fn, $" \mathtt { g } " .$ ), subplot(1,2,2), plot(f-pn, $" \mathbf { r } \cdot \mathbf { \xi }$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/bced4887f07c445164e08746af701fc74e33ce0d61fe7e2a9ead14ee92130e4b.jpg)

On the basis of plots like these, one might speculate that $f _ { n }$ may often be a better approximation than $p _ { n }$ but that the difference is small. This is indeed the case, as we shall confirm in Theorems 7.2 and 8.2, both of which suggest a difference of a factor of 2, and Theorem 16.1, which suggests a factor of $\pi / 2$ .

Let us review where we stand. We have considered Chebyshev interpolants (Chapter 2) and Chebyshev expansions (Chapter 3) for a Lipschitz continuous function $f ( x )$ defined on $[ - 1 , 1 ]$ . Mathematically speaking, each coefficient of a Chebyshev expansion is equal to the value of the integral (3.12). This formula, however, is not needed for effective polynomial approximation, since Chebyshev interpolants are nearly as accurate as projections. Chebfun readily computes Chebyshev coefficients of polynomial interpolants, and this is done not by evaluating the integral but by taking the FFT of the sample values in Chebyshev points. If the degree of the interpolant is high enough that the polynomial matches $f$ to machine precision, then the Chebyshev coefficients will usually match too.

Summary of Chapter 4. Two excellent methods of approximating a function $f$ on $[ - 1 , 1 ]$ by a polynomial are truncation of its Chebyshev series, also known as projection, and interpolation in Chebyshev points. The Chebyshev interpolant is the polynomial obtained by reassigning contributions of degree $> n$ in the Chebyshev series to their aliases of degree $\leq n$ . The two approximations are typically within a factor of 2 of each other in accuracy.

Exercise 4.1. Node polynomial for Chebyshev points. Show using Theorem 4.1 that $p ( x ) = 2 ^ { - n } ( T _ { n + 1 } ( x ) - T _ { n - 1 } ( x ) )$ is the unique monic polynomial in $\mathcal { P } _ { n + 1 }$ with zeros at the $n + 1$ Chebyshev points (2.2).

Exercise 4.2. Examples of aliasing. (a) On the $( n + 1 )$ -point Chebyshev grid with $n = 2 0$ , which Chebyshev polynomials $T _ { k }$ take the same values as $T 5$ ? (b) Use Chebfun to draw plots illustrating some of these intersections.

Exercise 4.3. Aliasing in roots of unity. For each $n \geq 0$ , let $p _ { n } \in \mathcal { P } _ { n }$ be the degree $n$ polynomial interpolant to the function $f ( z ) = z ^ { - 1 }$ at the $( n + 1 ) \mathrm { s t }$ roots of unity on the unit circle in the $z$ -plane. Use the aliasing observation of the proof of Theorem 4.1 to prove that in the closed unit disk of complex numbers $z$ with $| z | \le 1$ , there is one and only one value $z$ for which $p _ { n }$ converges to $f$ as $n  \infty$ . (This example comes from [M´eray 1884].)

Exercise 4.4. Fooling the Chebfun constructor. (a) Construct the MATLAB anonymous function $\textbf { f } = \textsf { Q } ( \mathbb { M } )$ chebfu $\mathtt { n } ( \ @ ( \mathbf { x } ) 1 { + } \mathtt { e x p } ( - ( \mathtt { M } * ( \mathbf { x } { - } 0 . 4 ) ) \hat { - } 4 ) \mathtt { ) }$ ) and plot f(10) and $\mathtt { f } \left( 1 0 0 \right)$ . This function has a narrow spike of width proportional to $1 / M$ . Confirm this by comparing $\mathtt { s u m } ( \mathtt { f } \left( 1 0 \right) )$ and sum(f(100)). (b) Plot length(f(M)) as a function of $M$ for $M = 1 , 2 , 3 , \ldots$ , going into the region where the length becomes 1. What do you think is happening? (c) Let Mmax be the largest integer for which the constructor behaves normally and execute semilogy( $\texttt { f } ( \mathtt { M m a x } ) - 1 )$ . Superimpose on this plot information to show the locations of the points returned by chebpts(17), which is the default initial grid on which Chebfun samples a function. Explain how this result fits with (b). (d) Now for np taking values 33, 65, 129, execute chebfunpref.setDefaults('minSamples',np) and length( $\mathbf { f } \left( \mathtt { M m a x } { + } 1 \right) )$ , and plot the Chebyshev points on your semilog plot of (c). The minSamples flag forces Chebfun to sample the function at the indicated number of points. How do these results match your observations of (b) and (c)? When you’re done, be sure to return Chebfun to its default state with chebfunpref.setDefaults('factory').

Exercise 4.5. Relative precision. Try Exercise 4.4 again but without the “1+” in the definition of $\pm$ . The value of Mmax will be different, and the reason has to do with the Chebfun aim of constructing each function to about 15 digits of relative precision, not absolute. Can you figure out what is happening and explain it quantitatively?

Exercise 4.6. Chebfun computation of truncations. In the text we computed Chebyshev truncations of $f ( x ) = \mathrm { t a n h } ( 4 x - 1 )$ using the 'trunc' flag in the Chebfun constructor. Another method is to compute all the Chebyshev coefficients of $f$ down to machine precision by making a chebfun of $f$ , then truncate the series. Compute $f _ { 4 }$ by this method and verify that the results agree to machine precision.

Exercise 4.7. When projection equals interpolation. Sometimes the projection $f _ { n }$ and the interpolant $p _ { n }$ are identical, even though both differ from $f$ . Characterize exactly when this occurs, and give an example with $n = 3$ .
