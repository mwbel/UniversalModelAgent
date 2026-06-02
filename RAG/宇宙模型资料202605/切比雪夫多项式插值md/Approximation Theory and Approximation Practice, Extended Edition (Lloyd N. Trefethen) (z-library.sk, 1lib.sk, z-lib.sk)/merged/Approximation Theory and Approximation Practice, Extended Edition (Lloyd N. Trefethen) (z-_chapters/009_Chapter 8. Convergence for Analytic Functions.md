# Chapter 8. Convergence for Analytic Functions

Suppose $f$ is not just $k$ times differentiable but infinitely differentiable and in fact analytic on $[ - 1 , 1 ]$ . (Recall that this means that for any $s \in [ - 1 , 1 ]$ , $f$ has a Taylor series about $s$ that converges to $f$ in a neighborhood of $s$ .) Then without any further assumptions we may conclude that the Chebyshev projections and interpolants converge geometrically, that is, at the rate $O ( C ^ { - n } )$ for some constant $C > 1$ . This means the errors will look like straight lines (or better) on a semilog scale rather than a loglog scale. This kind of connection was first announced in 1911 by Bernstein, who showed that the best approximations to a function $f$ on $[ - 1 , 1 ]$ converge geometrically as $n \to \infty$ if and only if $f$ is analytic [Bernstein 1911 & 1912b].

For example, for Chebyshev interpolants of the function $( 1 + 2 5 x ^ { 2 } ) ^ { - 1 }$ , known as the Runge function (Chapter 13), we get steady geometric convergence down to the level of rounding errors:

$\begin{array} { r l } & { \mathtt { x \_ } { c h e b f u n } ( \mathrm { \iota _ { X } ^ { \prime } ~ } \mathtt { x ^ { \prime } } ) \mathrm { ; ~ } \mathtt { f \_ } = \mathrm { \mathtt { 1 / ( 1 + 2 5 * x ^ { \circ } 2 ) } } \mathrm { ; ~ } \mathtt { n n \_ } = \mathrm { \mathtt { 0 : 1 0 : 2 0 0 } } \mathrm { ; ~ } \mathtt { e e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \mathtt { e } \_ \mathtt { \mathtt { i } } } } } } } } } } \mathtt { o } } = \mathrm { \mathtt { 0 : } } \mathtt { n } \mathrm { n } \mathrm { ; ~ } } \\ & { \mathtt { f o r \_ j } = \mathrm { \mathtt { 1 : 1 \mathtt { e n g t h } ( n n \mathtt { n } ) } } } \\ & { \mathtt { n \_ } = \mathtt { n \_ { e \_ \mathtt { e \_ { e \_ \mathtt { e \_ { e \_ \mathtt { e \_ { e } } } } } } } } \mathtt { n \_ } \mathtt { f n \_ } = \mathtt { c h e b f u n } ( \mathtt { f \_ { \mathtt { e } , n + 1 } } ) \mathrm { ; ~ } \mathtt { e e ( j ) \ } = \mathtt { n o r m } ( \mathtt { f \mathrm { - } f n , i n f } ) \mathrm { ; ~ } } \end{array}$   
end   
semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/72ea8df1c59a1d8b6e0c461a1caeb2c66610e22ed3ff60ccca6f136bb88ef4e0.jpg)

If $f$ is analytic not just on $[ - 1 , 1 ]$ but in the whole complex plane—such a function is said to be entire—then the convergence is even faster than geometric. Here, for the function $\cos ( 2 0 x )$ , the dots are approaching not a fixed straight line but a curve that gets steeper as $n$ increases, until rounding errors cut off the progress.

f $\begin{array} { r l } { = } & { \cos \left( 2 0 { * \mathbf { x } } \right) ; ~ \mathrm { n n ~ = ~ } 0 : 2 : 6 0 ; ~ \mathrm { e e ~ = ~ } 0 { * \mathbf { n } } \mathrm { n } ; } \\ { \mathrm { 3 r ~ j ~ = ~ } 1 : \mathrm { 1 e n g t h } \left( \mathrm { n n } \right) } \\ { \mathrm { ~ n ~ = ~ } \mathrm { n n ( j ) } ; ~ \mathrm { f n ~ = ~ c h e b f u n } \left( \mathrm { f , n + 1 } \right) ; ~ \mathrm { e e ( j ) ~ = ~ } \mathrm { n o r m } \left( \mathrm { f - f n , i n f } \right) ; } \end{array}$   
end   
semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/63bd3fd8967484fb149e6ea5504922c367fdc556e220582d4c3baf49c78fa183.jpg)

There are elegant theorems that explain these effects. If $f$ is analytic on $[ - 1 , 1 ]$ , then it can be analytically continued to a neighborhood of $[ - 1 , 1 ]$ in the complex plane. (The idea of analytic continuation is explained in complex variables textbooks; see also Chapter 28.) The bigger the neighborhood, the faster the convergence. In particular, for polynomial approximations, the neighborhoods that matter are the regions in the complex plane bounded by ellipses with foci at $^ { - 1 }$ and 1, known as Bernstein ellipses [Bernstein 1912b, 1912c & 1914a]. It is easy to plot these curves: pick a number $\rho > 1$ and plot the image in the complex $x$ -plane of the circle of radius $\rho$ in the $z$ -plane under the Joukowsky map $x = ( z + z ^ { - 1 } ) / 2$ . We let $E _ { \rho }$ denote the open region bounded by this ellipse. Here, for example, are the Bernstein ellipses corresponding to the parameters $\rho = 1 . 1 , 1 . 2 , . . . , 2$ :

z = exp(2i\*pi\*x);   
f $\mathrm { \Lambda } _ { 0 \Sigma } \ \mathrm { \bf ~ r h o } = 1 . 1 : 0 . 1 : 2$ e = (rho\*z+(rho\*z)^(-1))/2; plot(e), hold on   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/69575e4e795ac7ee11b111ff42e27f587cba42c34c5d6960fc5662c715aa98a0.jpg)

It is not hard to verify that the length of the semimajor axis of $E _ { \rho }$ plus the length of the semiminor axis is equal to $\rho$ (Exercise 8.1).

Here is the basic bound on Chebyshev coefficients of analytic functions from which many other things follow. It first appeared in Section 61 of [Bernstein 1912b].

Theorem 8.1. Chebyshev coefficients of analytic functions. Let a function $f$ analytic in $[ - 1 , 1 ]$ be analytically continuable to the open Bernstein ellipse $E _ { \rho }$ , where it satisfies $| f ( x ) | \leq M$ for some $M$ . Then its Chebyshev coefficients satisfy $| a _ { 0 } | \le M$ and

$$
\begin{array} { r } { | a _ { k } | \leq 2 M \rho ^ { - k } , \quad k \geq 1 . } \end{array}
$$

Proof. As in the proofs of Theorems 3.1, 4.1, and 7.1, we make use of the transplantation from $f ( x )$ and $T _ { k } ( x )$ on $[ - 1 , 1 ]$ in the $x$ -plane to $F ( z )$ and $( z ^ { k } +$ $z ^ { - k } ) / 2$ on the unit circle in the $z$ -plane, with $x = ( z + z ^ { - 1 } ) / 2$ and $F ( z ) = F ( z ^ { - 1 } ) =$ $f ( x )$ . The ellipse $E _ { \rho }$ in the $x$ -plane corresponds under this formula in a 1-to-2 fashion to the annulus $\rho ^ { - 1 } < | z | < \rho$ in the $z$ -plane. By this we mean that for each $x$ in $E _ { \rho } \backslash [ - 1 , 1 ]$ there are two corresponding values of $z$ that are inverses of one another, and both the circles $| z | = \rho$ and $| z | = \rho ^ { - 1 }$ map onto the ellipse itself. The first thing to note is that if $f$ is analytic in the ellipse, then $F ^ { \prime }$ is analytic in the annulus since it is the composition of the two analytic functions $z \mapsto ( z + z ^ { - 1 } ) / 2$ and $x \mapsto f ( x )$ . Now we make use of the contour integral formula (3.13),

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } z ^ { - 1 - k } F ( z ) d z ,
$$

with $\pi i$ replaced by $2 \pi i$ for $k = 0$ . Suppose for a moment that $F$ is analytic not just in the annulus but in its closure $\rho ^ { - 1 } \leq | z | \leq \rho$ . Then we can expand the contour to $| z | = \rho$ without changing the value of the integral, giving

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = \rho } z ^ { - 1 - k } F ( z ) d z ,
$$

again with $\pi i$ replaced by $2 \pi i$ for $k ~ = ~ 0$ . Since the circumference is $2 \pi \rho$ and $| F ( z ) | \le M$ , the required bound now follows from an elementary estimate. If $F$ is analytic only in the open annulus, we can move the contour to $| z | = s$ for any $s < \rho$ , leading to the same bound for any $s < \rho$ and hence also for $s = \rho$ .

Here are two of the consequences of Theorem 8.1. Equation (8.2) first appeared in [Bernstein 1912b, Sect. 61]. I do not know where (8.3) may have appeared, though similar slightly weaker bounds can be found in (4.13) and (4.16) of [Tadmor 1986]. For a generalization of (8.3) to interpolation in other point sets with the same asymptotic distribution as Chebyshev points, see Theorem 12.1.

Theorem 8.2. Convergence for analytic functions. If $f$ has the properties of Theorem 8.1, then for each $n \geq 0$ its Chebyshev projections satisfy

$$
\| f - f _ { n } \| \leq { \frac { 2 M \rho ^ { - n } } { \rho - 1 } }
$$

and its Chebyshev interpolants satisfy

$$
\| f - p _ { n } \| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

Proof. Equation (8.2) follows from Theorem 8.1 and (4.8), and (8.3) follows from Theorem 8.1 and (4.9).

We can apply Theorem 8.2 directly if $f$ is analytic and bounded in $E _ { \rho }$ . If it is analytic but unbounded in $E _ { \rho }$ , then it will be analytic and bounded in $E _ { s }$ for any $s < \rho$ , so we still get convergence at the rate $O ( s ^ { - n } )$ for any $s < \rho$ . If it is unbounded in $E _ { \rho }$ but the only singularities on the ellipse are simple poles, then we get convergence at the rate $O ( \rho ^ { - n } )$ after all (Exercise 8.15).

Before applying Theorem 8.2 to a couple of examples, it will be convenient to note formulas for $\rho$ in two common special cases. Suppose $f$ has its dominant singularity at a real value $x _ { 0 } = \pm \alpha$ for some $\alpha > 1$ . Then the corresponding ellipse parameter is

$$
\rho = \alpha + \sqrt { \alpha ^ { 2 } - 1 } \quad ( \mathrm { r e a l \ s i n g u l a r i t y \ a t \ } x = \pm \alpha ) .
$$

Or suppose that the dominant singularity is at the pure imaginary value $x _ { 0 } = \pm i \beta$ for some $\beta > 0$ . Then we have

$$
\rho = \beta + { \sqrt { \beta ^ { 2 } + 1 } } \quad ( { \mathrm { i m a g i n a r y ~ s i n g u l a r i t y ~ a t ~ } } x = \pm i \beta ) .
$$

For example, the Runge function $( 1 + 2 5 x ^ { 2 } ) ^ { - 1 }$ considered above has poles at√ $\pm i / 5$ . By (8.5), the corresponding value of $\rho$ is $( 1 + \sqrt { 2 6 } ) / 5 \approx 1 . 2 2 0$ , and the errors in Chebyshev interpolation match this rate beautifully:

$\begin{array} { r l } { \mathbf { f } } & { = \mathbf { \Phi } _ { 1 } / ( 1 + 2 5 * \mathbf { x } \cdot 2 ) ; \mathbf { \Phi } \mathrm { n n } \ = \ 0 : 1 0 : 2 0 0 ; \mathbf { \Phi } \mathrm { e e ~ = \ 0 * \mathrm { n n } } ; } \\ { \mathbf { f o r } \ \mathbf { j } } & { = \mathbf { \Phi } _ { 1 } : \mathbf { { l } \mathrm { e n g t h } } ( \mathrm { n n } ) } \\ { \mathbf { n } } & { = \mathbf { \Phi } \mathrm { n n } ( \mathbf { j } ) ; \mathbf { \Phi } \mathrm { f n } \ = \ { \mathrm { c h e b f u n } } ( \mathbf { f } , \mathbf { n } + 1 ) ; \mathbf { \Phi } \mathrm { e e ( \mathbf { j } ) } \ = \ \mathbf { \mathrm { n o r m } } ( \mathbf { f } \mathrm { - } \mathbf { f n } , \mathbf { i } \mathrm { n f } ) ; } \end{array}$ end   
rho $=$ ( $1 +$ sqrt(26))/5;   
semilogy(nn,rho.^-nn, $\ " - \mathbf { r } \cdot \mathbf { \sigma }$ ), hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/d326a4b3ef702de624286acfd195a476bf5444dd6766a320c981a3ea782d1461.jpg)

Here is a more extreme but entirely analogous example: $\operatorname { t a n h } ( 5 0 \pi x )$ , with poles at $\pm 0 . 0 1 i$ . These poles are so close to $[ - 1 , 1 ]$ that the convergence is much slower, but it is still robust. The only difference in this code segment is that $\mathtt { n o r m } ( \mathtt { f } \mathtt { - f } \mathtt { n } , \mathtt { i n f } )$ , a relatively slow Chebfun operation that depends on finding zeros of the derivative of $\tt f - f n$ , has been replaced by the default 2-norm norm(f-fn), which is quick. This makes little difference to the figure, as the exponential decay rates are the same. (In the $\infty$ -norm, the dots in the figure would appear just above the red line instead of just below it.)

$\begin{array} { r l } & { \mathrm { ~ f ~ \omega = \ t a n h ( 5 0 * p i * x ) ~ ; ~ n n ~ \omega = ~ 0 : 2 0 0 : 4 0 0 0 ; ~ \eta \in \varphi = \varphi 0 * n n ; } } \\ & { \mathrm { ~ f o r ~ j ~ \omega = ~ 1 : 1 \mathrm { e n g t h } ( n n ) } } \\ & { \mathrm { ~ n ~ = ~ n n ( j ) ~ ; ~ f { n ~ = ~ c h e b f u n ( f , n + 1 ) } ~ ; ~ \eta \in e ( j ) ~ \omega = \varphi _ { n o r m } ( f - f { n } ) ~ ; } } \end{array}$ end   
rho $=$ ( $1 +$ sqrt(10001))/100;   
semilogy(nn,rho.^-nn,'-r'), hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/ae6d627aab68f93b8b6605848098e28f3faec1735413b2d13dce5c7b784f660a.jpg)

For an example with a real singularity, the function √ $\sqrt { 2 - x }$ has a branch point at $x = 2$ , corresponding by (8.4) to $\rho = 2 + \sqrt { 3 }$ . Again we see a good match, with the curve gradually bending over to the expected slope as $n \to \infty$ .

f $\begin{array} { r l } { = } & { \mathbf { s q r t } ( 2 \mathbf { - x } ) ; ~ \mathrm { n n ~ = ~ } 0 : 3 0 ; ~ \mathbf { e e ~ = ~ } 0 * \mathrm { n n } ; } \\ { \mathrm { ~ \mathrm { ~  ~ \lambda ~ } ~ } ] ~ \mathrm { ~  ~ \lambda ~ } = ~ 1 : \mathrm { { l e n g t h } } ( \mathrm { n n } ) } \\ { ~ \mathrm { ~  ~ \lambda ~ } = } & { \mathrm { { n n } ( j ) ~ ; ~ \mathrm { ~ \mathrm { ~ f n ~ = ~ c h e b f u n } ( f , n + 1 ) ~ } ; ~ \mathbf { e e } ( j ) ~ = ~ \mathrm { n o r m } ( f \mathrm { - } f n , \mathrm { i n f } ) ~ } ; } \end{array}$   
f   
end   
rho $=$ 2+sqrt(3); semilogy(nn,rho.^-nn,'-r')   
hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/124f5ab1686affef3bb200a80fa21247e2ca85304b6e3063b758f75f778428c9.jpg)

We now derive an elegant converse of Theorem 8.2, also due to Bernstein [1912b, Sect. 9]. The converse is not quite exact: Theorem 8.2 assumes analyticity and boundedness in $E _ { \rho }$ , whereas the conclusion of Theorem 8.3 is analyticity but not necessarily boundedness (Exercise 8.15).

Theorem 8.3. Converse of Theorem 8.2. Suppose $f$ is a function on $[ - 1 , 1 ]$ for which there exist polynomial approximations $q _ { n } \in P _ { n }$ satisfying

$$
\left\| f - q _ { n } \right\| \leq C \rho ^ { - n } , \quad n \geq 0 ,
$$

for some constants $\rho > 1$ and $C > 0$ . Then $f$ can be analytically continued to an analytic function in the open Bernstein ellipse $E _ { \rho }$ .

Proof. The assumption implies that the polynomials $\left\{ q _ { n } \right\}$ satisfy $\| q _ { n } - q _ { n - 1 } \| \leq$ $2 C \rho ^ { 1 - n }$ on $[ - 1 , 1 ]$ . Since $q _ { n } \mathrm { ~ - ~ } q _ { n - 1 } \in \mathcal { P } _ { n }$ , it can be shown that this implies $\| q _ { n } - q _ { n - 1 } \| _ { E _ { s } } \leq 2 C s ^ { n } \rho ^ { 1 - n }$ for any $s > 1$ , where $\| \cdot \| _ { E _ { s } }$ is the supremum norm on the $s$ -ellipse $E _ { s }$ . (This estimate is one of Bernstein’s inequalities, from Section 9 of [Bernstein 1912b]; see Exercise 8.6.) For $s < \rho$ , this gives us a representation for $f$ in $E _ { s }$ as a series of analytic functions,

$$
f = q _ { 0 } + ( q _ { 1 } - q _ { 0 } ) + ( q _ { 2 } - q _ { 1 } ) + \cdots ,
$$

which is uniformly convergent according to the Weierstrass M-test. According to another well-known theorem of Weierstrass, this implies that the limit is a bounded analytic function [Ahlfors 1953, Markushevich 1985]. Since this is true for any $s < \rho$ , the analyticity applies throughout $E _ { \rho }$ .

Note that Theorems 8.2 and 8.3 together establish a simple fact, sometimes known as Bernstein’s theorem: a function defined on $[ - 1 , 1 ]$ can be approximated by polynomials with geometric accuracy if and only if it is analytic. (See also Exercise 8.11 and [Bagby & Levenberg 1993].)

The term “Bernstein ellipse” refers to any ellipse in the complex plane with foci $\{ - 1 , 1 \}$ , and if $f$ is a function analytic on $[ - 1 , 1 ]$ , the bounds of Theorems 8.1 and 8.2 apply for any Bernstein ellipse inside which $f$ is analytic and bounded. If there is a largest ellipse inside which $f$ is analytic, then one might choose to say that this was “the” Bernstein ellipse for $f$ , but this might not always be the ellipse that gives the most useful bound, and if $f$ is entire, then there is no largest ellipse at all (Exercise 8.3).

Chebfun computations, however, suggest a practical way to single out a special Bernstein ellipse associated with a given function $f$ . The Chebfun ellipse for $f$ is the Bernstein ellipse whose parameter $\rho$ satisfies the condition

$$
\rho ^ { - n } = \varepsilon ,
$$

where $\varepsilon$ is the tolerance used by the Chebfun constructor (normally $2 ^ { - 5 2 }$ ) and $n$ is the degree of the polynomial chosen by Chebfun to resolve $f$ . The command plotregion plots these Chebfun ellipses. Thus for $f ( x ) = 1 / ( 1 { + } 2 5 x ^ { 2 } )$ , for example, the Chebfun ellipse comes very close to passing through the poles at $\pm 0 . 2 i$ :

$\begin{array} { r l } { \hat { \mathbf { f } } } & { { } = } \end{array}$ chebfun('1/(1+25\*x^2)'); plotregion(f), hold on, plot([.2i -.2i],'xr')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/be6fa3870d4c5327066d466f249064457bbd940e1ceea9eaf2e1a41cedcad210.jpg)

For the entire function $f ( x ) = \exp ( - 2 0 0 x ^ { 2 } )$ , the Chebfun ellipse has much the same shape, although now $f$ has no singularities:

f = chebfun('exp(-200\*x^2)'); plotregion(f)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/e24a609c87bb2d15d9eceae1984aaa1a388f8766374a10cd91b9d1cb0a5966b7.jpg)

Summary of Chapter 8. If $f$ is analytic, its Chebyshev coefficients $\{ a _ { k } \}$ decrease geometrically. In particular, if $f$ is analytic with $| f ( x ) | \leq M$ in the Bernstein $\rho$ -ellipse about $[ - 1 , 1 ]$ , then $| a _ { k } | \le 2 M \rho ^ { - k }$ . It follows that the degree $n$ Chebyshev projection and interpolant of $f$ have accuracy $O ( M \rho ^ { - n } )$ .

Exercise 8.1. Bernstein ellipses. Verify that for any $\rho > 1$ , the length of the semiminor axis plus the length of the semimajor axis of the Bernstein ellipse $E _ { \rho }$ is equal to $\rho$ .

Exercise 8.2. A Chebyshev series. With $\textbf { x } = \mathtt { c h e b f u n } ( \mathbf { \Omega } ^ { \prime } \mathbf { x } ^ { \prime } )$ , execute the command plotcoeffs $( \sin { ( 1 0 0 * ( \mathbf { x } - 1 ) ) } + . 0 1 * \operatorname { t a n h } { ( 2 0 * \mathbf { x } ) } )$ . Explain the various features of the resulting plot as quantitatively as you can.

Exercise 8.3. Interpolation of an entire function. The function $f ( x ) = \exp ( - x ^ { 2 } )$ is analytic throughout the complex $_ x$ -plane, so Theorem 8.2 can be applied for any value of the parameter $\rho > 1$ . Produce a semilog plot of $\| f - p _ { n } \|$ as a function of $n$ together with lines corresponding to the upper bound of the theorem for $\rho = 1 . 1 , 1 . 2 , 1 . 4 , 2 , 3 , 5 , 8$ . Be sure to use the right value of $M$ in each case. How well do your bounds fit the data?

Exercise 8.4. Convergence rates for different functions. Based on the theorems of this chapter, what can you say about the convergence as $n  \infty$ of the Chebyshev interpolants to (a) $\tan ( x )$ , (b) $\operatorname { t a n h } ( x )$ , (c) $\log ( ( x + 3 ) / 4 ) / ( x - 1 )$ , (d) $\int _ { - 1 } ^ { \cdot x } \cos ( t ^ { 2 } ) d t$ , (e) $\tan ( { \tan ( x ) } )$ , and (f) $( 1 + x ) \log ( 1 + x ) { \stackrel { . } { . } }$ ? In each case compare theoretical bounds with numerically computed results. Which is the case that converges much faster than the theorems predict? Can you speculate as to why?

Exercise 8.5. Accuracy of approximations in the complex plane. Let $_ p$ be the chebfun for $f ( x ) = \exp ( - 2 0 0 x ^ { 2 } )$ and plot contour lines in the complex $_ x$ -plane corresponding to $| f ( x ) - p ( x ) | = 1 0 ^ { - 2 } , 1 0 ^ { - 4 } , \cdot \cdot \cdot , 1 0 ^ { - 1 4 }$ . How do these curves compare to the Bernstein ellipses corresponding to parameters $\rho$ satisfying $\rho ^ { - n } = \varepsilon \times \{ 1 0 ^ { 2 } , 1 0 ^ { 4 } , \cdot \cdot \cdot , 1 0 ^ { 1 4 } \}$ , where $\varepsilon$ is the Chebfun constructor tolerance $2 ^ { - 5 2 }$ ?

Exercise 8.6. Proof of Bernstein inequality. Prove Bernstein’s inequality used in the proof of Theorem 8.3: if $p$ is a polynomial of degree $d$ , then $\| p \| _ { E _ { \rho } } \leq \rho ^ { d } \| p \|$ , where $\| \cdot \| _ { E _ { \rho } }$ is the $\infty$ -norm over the $\rho$ -ellipse and $\| \cdot \|$ is the $\infty$ -norm over $[ - 1 , 1 ]$ . (Hint: Show that if the branch cut is taken to be the unit interval $[ - 1 , 1 ]$ , the function $q ( z ) = p ( z ) / ( z + ( z ^ { 2 } - 1 ) ^ { 1 / 2 } ) ^ { d }$ is analytic throughout the region consisting of the complex plane plus the point $z = \infty$ minus $[ - 1 , 1 ]$ . Apply the maximum modulus principle.)

Exercise 8.7. Absolute value function. The function $| x - i |$ is analytic for $x \in [ - 1 , 1 ]$ . This means it can be analytically continued to an analytic function $f ( x )$ in a neighborhood of $[ - 1 , 1 ]$ in the complex $_ x$ -plane. The formula $| x - i |$ itself does not define an analytic function in any complex neighborhood. Find another formula for $f$ that does, and use it to explain what singularities $f$ has in the complex plane.

Exercise 8.8. Chebyshev polynomials on the Bernstein ellipse. Show that for any $\rho > 1$ and any $z$ on the boundary of the ellipse $E _ { \rho }$ in the complex $_ x$ -plane, $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } | T _ { n } ( x ) | ^ { 1 / n } = \rho } \end{array}$ .

Exercise 8.9. You can’t judge smoothness by eye. Define $f ( x ) = 2 + \sin ( 5 0 x )$ and $g ( x ) = f ( x ) ^ { 1 . 0 0 0 1 }$ and construct chebfuns for these functions on $[ - 1 , 1 ]$ . What are their lengths? Explain this effect quantitatively using the theorems of this chapter.

Exercise 8.10. Convergence of conjugate gradient iteration. Suppose we wish to approximate $f ( x ) = x ^ { - 1 }$ on the interval $[ m , M ]$ with $0 < m < M$ . Show that for any $\kappa > M / m$ , there exist polynomials $p _ { n } \in \mathcal { P } _ { n }$ such that $\| f - p _ { n } \| = O ( ( 1 + 2 / { \sqrt { \kappa } } ) ^ { - n } )$ as $n \to \infty$ , where $\| \cdot \|$ is the $\infty$ -norm on $[ m , M ]$ . This result is famous in numerical linear algebra as providing an upper bound for the convergence of the conjugate gradient iteration applied to a symmetric positive definite system of equations $A x = b$ with condition number $\kappa$ . See Theorem 38.5 of [Trefethen & Bau 1997].

Exercise 8.11. Bernstein’s theorem. Show that the conclusion of Theorem 8.3 also holds if the hypothesis is weakened to $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \| f - q _ { n } \| ^ { 1 / n } \leq \rho ^ { - 1 } } \end{array}$ .

Exercise 8.12. Resolution power of Chebyshev interpolants. The function $f _ { M } ( x ) = \exp ( - M ^ { 2 } x ^ { 2 } / 2 )$ has a spike of width $O ( 1 / M )$ at $x \ = \ 0$ . Let $n ( M )$ be the degree of a chebfun for $f _ { M }$ . (a) Determine the asymptotic behavior of $n ( M )$ as $M \to \infty$ by numerical experiments. (b) Explain this result based on the theorems of this chapter.

Exercise 8.13. Resolution power of Bernstein polynomials. Continuing the last exercise, now let $n ( M )$ be the degree of a Bernstein polynomial (6.2) needed to approximate $f _ { M }$ to machine precision. (For this discussion rescale (6.2) from $[ 0 , 1 ]$ to $[ - 1 , 1 ]$ .) (a) Determine the asymptotic behavior of $n ( M )$ as $M  \infty$ by numerical experiments. (b) Explain this result, not necessarily rigorously.

Exercise 8.14. Formulas for ellipse parameter. Derive (8.4) and (8.5).

Exercise 8.15. Simple poles on the Bernstein ellipse. (a) Explain how (3.16) illustrates that Theorem 8.3 is not an exact converse of Theorem 8.2. (b) Let $f$ be analytic in the open Bernstein ellipse region $E _ { \rho }$ for some $\rho > 1$ with the only singularities on the ellipse itself being simple poles. Show that $\| f - f _ { n } \|$ and $\| f - p _ { n } \|$ are of size $O ( \rho ^ { - n } )$ as $n \to \infty$ .


<!-- chunk 0002: pages 71-140 -->
