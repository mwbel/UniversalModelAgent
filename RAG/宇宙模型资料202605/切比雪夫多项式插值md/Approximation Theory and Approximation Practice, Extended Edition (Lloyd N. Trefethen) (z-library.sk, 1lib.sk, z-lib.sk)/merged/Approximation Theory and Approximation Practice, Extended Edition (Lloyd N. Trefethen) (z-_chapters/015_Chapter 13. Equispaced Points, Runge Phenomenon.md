# Chapter 13. Equispaced Points, Runge Phenomenon

So far in this book, we have considered three good methods for approximating functions by polynomials: Chebyshev interpolation, Chebyshev projection, and best approximation. Now we shall look at a catastrophically bad method!—interpolation in equally spaced points. This procedure is so unreliable that, for generations, it has tainted people’s views of the whole subject of polynomial interpolation. The mathematical tools we will need to understand what is going on are the Hermite integral formula and potential theory, as discussed in the last two chapters.

As mentioned in Chapter 5, polynomial interpolation was an established tool by the 19th century. The question of whether polynomial interpolants would converge to an underlying function as $n  \infty$ was not given much attention. Presumably many mathematicians would have supposed that if the function was analytic, the answer would be yes. In 1884 and 1896, M´eray published a pair of papers in which he identified the fact that certain interpolation schemes do not converge [M´eray 1884 & 1896]. In the first paper he writes

It is rather astonishing that practical applications have not yet turned up any cases in which the interpolation is illusory.6

M´eray’s derivations had the key idea of using the Hermite integral formula. However, the examples he devised were rather contrived, and his idiosyncratically written papers had little impact. It was Runge in 1901 who made the possibility of divergence famous by showing that divergence of interpolants occurs in general even for equispaced points in a real interval and evaluation points in the interior of that interval [Runge 1901].

Runge illustrated his discovery with an example that has become known as the Runge function: $1 / ( 1 + x ^ { 2 } )$ on $[ - 5 , 5 ]$ or, equivalently, $1 / ( 1 + 2 5 x ^ { 2 } )$ on $[ - 1 , 1 ]$ :

We already know from Chapter 8 that there is nothing wrong with this function for polynomial interpolation in Chebyshev points: $f$ is analytic, and the polynomial interpolants converge geometrically. Now, however, let us follow Runge and look at interpolants in equally spaced points, which we can compute using the Chebfun overload of the MATLAB interp1 command.

Here is what we get with 8 points:

s = linspace(-1,1,8); $\mathrm { ~ p ~ } =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/220391880c7937795d2a9af13b48ce80b6fa12e0d2e8136eeb3914781a7ef305.jpg)

Here is the result for 16 points:

s = linspace(-1,1,16); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/272777894d27087f9e71a2990d29c2cf75494c5ceeda3cb53c0548f33b6447c4.jpg)

Is this going to converge as $n \to \infty$ ? Things look pretty good in the middle but not so good at the edges. Here is the result for 20 points:

s = linspace(-1,1,20); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/9c9ccb320d97d2b57b1ec070a2ef7573c0bc77d622225af921e473a48166ef48.jpg)

What is happening is exponential convergence in the middle of the interval but exponential divergence near the ends. The next figure shows the maximum error over $[ - 1 , 1 ]$ as a function of the number of points. We get a hint of convergence at first, but after $n = 1 0$ , things just get worse. Note the log scale.

f $\begin{array} { r l } & { \mathsf { e } ~ = ~ \left[ \mathsf { J } \right] ; ~ \mathrm { n n } ~ = ~ 2 { : 2 : 5 0 } ; } \\ & { \mathsf { o r } ~ \mathrm { n p } ~ = ~ \mathrm { n n } } \\ & { ~ \mathsf { s } ~ = ~ \mathrm { 1 i n s p a c e } ( - 1 , 1 , \mathrm { n p } ) ; ~ \mathsf { p } ~ = ~ \mathrm { c h e b f u n . i n t e r p 1 } ( \mathsf { s } , \mathsf { f } ) ; } \\ & { \mathsf { e e } ~ = ~ \left[ \mathsf { e e } ~ \mathrm { n o r m } ( \mathsf { f } \mathrm { - p } , \mathrm { i n f } ) \right] ; } \end{array}$   
end   
semilogy(nn,ee,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/7b0de94fd102b98c6ad7e5f80670335e81c7c370a08e420e707bdfb4f86efd8e.jpg)

By now the reader may have suspected that what is going wrong here can be understood by looking at potentials, as in the last two chapters. Here is an adaptation of a code segment from Chapter 11 to plot equipotential curves for $n + 1 = 8$ and 20.

d = domain([-1.5,1.5]);   
xgrid $=$ -1.5:.02:1.5; ygrid $=$ -1:.02:1;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
for np $=$ [8 20] xj $=$ linspace(-1,1,np); ell $=$ poly(xj,d); plot(xj,ell(xj),'.k') hold on, ellzz $=$ ell(zz); levels $=$ ((1.25:.25:3)/exp(1)).^np; contour(xx,yy,abs(ellzz),levels,'k')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3742bbf26473d69b848b293749f91a2c79ff984b9790bb0715ec8cfeb35e8ac7.jpg)  
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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d5b237d98f9f8c9cc5858e8678ca2e39b45fc99a482b8bada4b7addf7223900b.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1cd234b3c0d20801cabea992bcbeb832a43c65b31b0f5d428fad9289ebf4d9fb.jpg)

All of the above remarks about equispaced interpolation concern the ideal mathematics of the problem. On a computer in floating point arithmetic, however, a further complication arises: even if convergence ought to take place in theory, rounding errors will be amplified by $O ( 2 ^ { n } )$ , causing divergence in practice. Here, for example, are the errors in equispaced and Chebyshev interpolation of the entire function $\exp ( x )$ :

${ \textbf { f } } = \exp \left( \mathbf { x } \right)$ ; eequi $=$ []; echeb $=$ []; nn = 2:2:80;   
for $\texttt { n } = \texttt { n n }$ s $=$ linspace(-1,1,n+1); pequi $=$ chebfun.interp1(s,f); eequi $=$ [eequi norm(f-pequi,inf)]; pcheb $=$ chebfun(f, $\ n { + } 1 $ ); echeb $=$ [echeb norm(f-pcheb,inf)];   
end   
semilogy $\left( \operatorname { n n } , 2 . { \hat { \mathbf { \phi } } } ( \operatorname { n n - 5 0 } ) , \mathbf { \mu } ^ { * } - \mathbf { - r } \mathbf { \mu } ^ { * } \right)$ , hold on   
semilogy(nn,eequi, $\mathbf { \partial } ^ { \prime } \mathbf { x } \mathbf { - } \mathbf { r } ^ { \prime } \mathbf { \partial } .$ ), semilogy(nn,echeb,'.-b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4d86eea9a01b201af78e3728e92ab79faf74d1ad29b4d948372bcae93131ed96.jpg)

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
