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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/b74d126d2d240c6898ae1da52ce8737fe13528ace924ee8cb2a3c92a885336b7.jpg)

The speedup is clear. On the other hand, here is a repetition of the experiment with $\cos ( 2 0 x )$ .

f f $\begin{array} { l } { { \mathrm { \tiny ~ ( ~ \cos ~ ( 2 0 * x ) ~ ; ~ f g ~ = ~ f ~ ( g ) ~ ; ~ ~ n n ~ = ~ 0 : 2 : 6 0 ; ~ \ e e ~ = ~ 0 * n n ; ~ \ e e 2 ~ = ~ 0 : n n ; } } } \\ { { \mathrm { \tiny ~ ( ~ \partial ~ 1 : 1 \mathrm { { z } \it ~ { h } } ( n n ) ~ \partial ~ 1 ~ \partial ~ 2 ~ ) ~ } } } \\ { { \mathrm { \tiny ~ { n } ~ = ~ n n ( j ) ~ ; ~ f n ~ = ~ c h e b f u n ( f , n + 1 ) ~ ; ~ \ e e ( j ) ~ = ~ n o r m ( f - f n , i n f ) ~ ; } } } \\ { { \mathrm { \tiny ~ { f n 2 ~ = ~ c h e b f u n ( f g , n + 1 ) ~ ; ~ \ e e 2 ( j ) ~ = ~ n o r m ( f g - f n 2 , i n f ) ~ ; } } } } \end{array}$ end semilogy(nn,ee,'.'), hold on, semilogy(nn,ee2,'sm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/c5dde1ffdbd77482370e51a11163b26ba7a691d7e79e628ad60cc3913aa8b2c7.jpg)

Now the result is ambiguous: the transformed method starts out ahead, but the standard Chebyshev method wins eventually. The explanation can be found in the nested ellipses $E _ { \rho }$ and their images plotted earlier. The function cos(20 $x$ ) is entire, and for larger $n$ , the Chebyshev points take good advantage of its analyticity well away from $[ - 1 , 1 ]$ . The transformed points do not do as well. (The advantage of the transformation becomes decisive again if we change $\cos ( 2 0 x )$ to $\cos ( 1 0 0 x )$ .)

We can see similar effects if we look at best approximations. For a nonsmooth function like $| x |$ , transformed polynomials typically approximate better than true ones. The following figures should be compared with those of Chapter 10, and the variable ratio quantifies the degree of improvement.

$\begin{array} { r l } { \mathbf { f } } & { { } = } \end{array}$ abs(x); subplot(1,2,1), plot(f,'k')   
$\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ; [p,err] $=$ minimax(fg,4);   
hold on, plot(p(gi),'m') subplot(1,2,2), hold off   
1 $\mathrm { \Omega ) 1 0 t ( g , f { \mathrm { - p } } ( g i ) , \mathrm { ' m } ^ { \prime } ) }$ , hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,4); ratio $=$ err2/err

ratio $=$ 1.2847

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/1845e770388d2f91a6a63afd7d8a12eed41d56d5314988e5b12e59132018b3df.jpg)

On the other hand, for a gentle entire function like $\exp ( x )$ , pure polynomials converge very fast and transformed polynomials cannot compete. The following error curve is seven orders of magnitude larger than that of Chapter 10.

f = exp(x); $\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ;   
[p,err] $=$ minimax(fg,10); plot(g,fg-p,'m'), hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,10); ratio $=$ err2/err

ratio $=$ 2.9938e-07

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/9f0452bccff8c3ccc9940ad1366c0f614976292b5867844611b0c023be87b487.jpg)

Our final application of transformed polynomial approximants is the one that was the subject of [Hale & Trefethen 2008]: quadrature. As described in Chapter 19, standard quadrature formulas are based on the idea of integrating a function numerically by interpolating it by a polynomial and then integrating the interpolant. This is the basis of all the well-known quadrature formulas, including Gauss, Newton– Cotes, Simpson, and Clenshaw–Curtis. But why should quadrature formulas be based on polynomials? This is a question not often raised in the quadrature literature. Some of the explanation surely has to do with custom going back centuries, before the appearance of computers, when the algebraic simplicity of polynomials would have been a telling advantage. If one had to give a mathematical answer still with some validity today, it would probably be that a polynomial formula is optimal if the order is fixed while the grid size is decreased to zero. If the order increases to $\infty$ on a fixed interval of integration, however, polynomial formulas are in no sense optimal.

In particular, a “transformed Gauss” quadrature formula can be obtained by applying Gauss quadrature to the integral on the right in the formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) = \int _ { - 1 } ^ { 1 } f ( g ( s ) ) g ^ { \prime } ( s ) d s .
$$

To illustrate this transplanted quadrature idea we pick a wiggly function,

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/c2dcd2e35bcba46969634a33e170e23dc0c24f900efb28070c675e1eabe709fb.jpg)

Here is a code in which I represents Gauss quadrature and I2 is transformed Gauss quadrature—and we see that the dots decrease about $3 0 \%$ more slowly than the squares.

gp $=$ diff(g); Iexact $=$ sum(f); err $=$ []; err2 $=$ []; nn = 50:50:2000;   
for $\texttt { n } = \texttt { n n }$ $[ \bf s _ { \tau } , \bf w ] _ { \tau } = \mathrm { \sf ~ 1 e g p t s } \left( \ln \mathrm { \right) ; \mathrm { ~ \cal ~ I ~ } = \mathrm { \bf ~ w * f } \left( \bf s \right) }$ ; err $=$ [err abs(I-Iexact)]; $\begin{array} { r } { \texttt { I 2 } = \texttt { w * } ( \texttt { f } ( \texttt { g } ( \texttt { s } ) ) * \wp ( \texttt { s } ) ) } \end{array}$ ; err2 $=$ [err2 abs(I2-Iexact)];   
end   
semilogy(nn,err,'.-'), hold on, semilogy(nn,err2,'s-m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/44f69757e2b5552406911841849cb223729abd383099b2bb62db946daa1ca729.jpg)

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
