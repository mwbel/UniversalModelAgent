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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1a20f25dd9da4716489b90fc593c2788273dd0907ffe4dcac8bc6f3f5409b30f.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/e5d90fc270f7450248ea2b1c856e47fbef6043888b3234374787fb6bc4a6a7e9.jpg)

The zeros of the two families of polynomials are similar, as can be confirmed by comparing Chebyshev (dots) and Legendre (crosses) zeros for degrees 10, 20, and 50. (Instead of using the roots command here, one could achieve the same effect with chebpts(n,1) and legpts(n)—see Chapter 19.)

$\mathrm { T 1 0 ~ = }$ chebpoly(10); $\mathrm { { \Delta P 1 0 ~ } = }$ legpoly(10); Tr $=$ roots(T10); Pr = roots(P10); plot(Tr,.8,'.b'), hold on $\mathtt { p l o t } ( \mathtt { P r } , 0 . 9 , \mathbf { \Phi } ^ { \prime } \mathbf { x } \mathrm { m } ^ { \prime } )$ , ${ \mathrm { T } } 2 0 ~ =$ chebpoly(20); P20 = legpoly(20); Tr $=$ roots(T20); Pr $=$ roots(P20); plot(Tr,0.4,'.b') plot(Pr,0.5,'xm'), Tr $=$ roots(T50); Pr $=$ roots(P50); plot(Tr,0,'.b'), plot(Pr,0.1,'xm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3740ddcf5c692d75db05d0c234a46138c6e6323c2609fbc88ed75e7ca3d25a0e.jpg)

Asymptotically as $n \to \infty$ , both sets of zeros cluster near $\pm 1$ with the same density distribution $n \mu ( x )$ , with $\mu$ given by (12.10). This behavior is made precise in

Theorem 12.1.4 of [Szeg˝o 1939] (Exercise 17.7), and exploitation of more detailed asymptotic properties of Jacobi polynomials is the crucial idea of [Hale & Townsend 2013].

Another comparison between Chebyshev and Legendre points concerns their Lebesgue functions and Lebesgue constants. Here we repeat a computation of Lebesgue functions from Chapter 15 for 8 Chebyshev points and compare it with the analogous computation for 8 Legendre points. Chebyshev and Legendre points as we have defined them so far differ not just in which polynomials they are connected with, but in that Chebyshev points come from extrema whereas Legendre points come from zeros.

$\qquad \mathtt { s } \ =$ chebpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst s $=$ legpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,2), plot(L), hold on, plot(s,L(s),'.'), Lconst

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/cdef487416dfbf74a75466ec8a6492f07456e9383e3368b077b9f7b47033309d.jpg)

The Lebesgue functions and constants for Legendre points are a little bigger than for Chebyshev points, having size $O ( n ^ { 1 / 2 } )$ rather than $O ( \log n )$ because of behavior near the endpoints [Szeg˝o 1939, p. 338]. This small difference is of little significance for most applications: the Lebesgue constants are still quite small, and either set of points will usually deliver excellent interpolants.

An alternative is to consider Legendre extreme points—the $n { \mathrel { + { 1 } } }$ points in $[ - 1 , 1 ]$ at which $| P _ { n } ( x ) |$ attains a local maximum. (The Legendre extreme points in $( - 1 , 1 )$ are also the roots of the Jacobi polynomial $P ^ { ( 1 , 1 ) } ( x )$ .) The Lebesgue function in this case looks even more satisfactory:

$\begin{array} { r } { \{ \begin{array} { r l } \end{array} \} = } & { { } \left[ - 1 \right. } \end{array}$ ; roots(diff(legpoly(7))); 1]; [L,Lconst] $=$ lebesgue(s); subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst $\mathbf { s } 1 5 ~ = ~ [ - 1$ ; roots(diff(legpoly(15))); 1]; [L,Lconst] $=$ lebesgue(s15); subplot(1,2,2), plot(L), hold on, plot(s15,L(s15),'.'), Lconst

Lconst $=$ 1.9724 Lconst $= \ 2 . 4 3 0 3$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f7c717a5dd83eb265b9678958aa24fb2c4a0c928fa0045020762ee3ff17e2ec0.jpg)

The Legendre extreme points have a memorable property: as shown by Stieltjes [1885], they are the Fekete or minimal-energy points in $[ - 1 , 1 ]$ , solving the equipotential problem on that interval for a finite number of equal charges (Exercise 12.1). Here, for example, is a repetition of a figure from Chapter 11 but now for 8 Legendre extreme points instead of 8 Chebyshev points. Again the behavior is excellent.

ell = poly(s,domain(-1,1)); plot(s,ell(s),'.k'), hold on xgrid $=$ -1.5:.02:1.5; ygrid $=$ -0.9:.02:0.9;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
ellzz $=$ ell(zz); levels $=$ 2.^(-6:0);   
contour(xx,yy,abs(ellzz),levels, $" \mathrm { \text k } "$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/6b047fa41059702f7cc737862d2b7cf9a89af12b45f4fe02088e26526005d763.jpg)

Summary of Chapter 17. Chebyshev polynomials are just one example of a family of polynomials orthogonal with respect to a weight function $w ( x )$ on $[ - 1 , 1 ]$ . For $w ( x ) = c o n s t a n t$ , one gets the Legendre polynomials.

Exercise 17.1. Chebyshev and Legendre Lebesgue constants. Extend the experiments of the text to a table and a plot of Lebesgue constants of Chebyshev, Legendre, and Legendre extreme points for interpolation in $n + 1$ points with $n = 1 , 2 , 4 , \dotsc , 2 5 6$ . (To compute Legendre extreme points efficiently, you can use the observation about Jacobi polynomials mentioned in the text and the Chebfun command jacpoly.) What asymptotic behavior do you observe as $n \to \infty$ ?

Exercise 17.2. Chebyshev and Legendre interpolation points. Define $f ( x ) =$ $x \operatorname { t a n h } ( 2 \sin ( 2 0 x ) )$ , and let $p$ and $p _ { L }$ be the interpolants to $f$ in $n + 1$ Chebyshev or Legendre points on $[ - 1 , 1 ]$ , respectively. The latter can be computed with interp1 as in
