# Chapter 22. Linear Approximation: Beyond Polynomials

Several times in the previous chapters, we have hinted that polynomials are not optimal functions for linear approximation on $[ - 1 , 1 ]$ . (Nonlinear approximations are another matter and will make their appearance in the next chapter.) It is now time to explain these hints and introduce alternative approximations that may be up to $\pi / 2$ times more efficient. One reason the alternatives are valuable is that they have practical advantages in some applications, especially for spectral methods in more than one space dimension. An equally important reason is that they push us to think more deeply about what it means to approximate a function and what may or may not be special about polynomials. The ideas of this chapter originate in [Bakhvalov 1967] and [Hale & Trefethen 2008]. Related ideas are the basis of work on sinc function numerical methods [Stenger 1993 & 2010, Richardson & Trefethen 2011], tanh and double exponential or tanh-sinh quadrature [Sag $\&$ Szekeres 1964, Takahasi & Mori 1974, Mori & Sugihara 2001], and the transformed-grid spectral methods introduced by Kosloff and Tal-Ezer [1993].

Recall from Chapter 8 that if $f$ is analytic on $[ - 1 , 1 ]$ , then to investigate its polynomial approximations, we ask how large a Bernstein ellipse $E _ { \rho }$ it can be analytically continued to. Here, for example, is the ellipse $E _ { \rho }$ with $\rho = 1 . 1 5$ . The words “Bernstein ellipse” written inside will help in a moment to visualize a conformal map. (Mathematically, these words are a piecewise linear complex function of a real variable constructed by the Chebfun scribble command.)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/bc5a67f9aa3e39cc7f814658724b47882a7a98247079adb5358b03bca5467d2b.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/3f5788a0d11dfe8aa24b7abdd438d78d7743c54f2e36502da7e05663aa506fc8.jpg)

Following [Hale & Trefethen 2008], we call $g$ a sausage map and $g ( E _ { 1 . 1 5 } )$ a sausage region. The crucial property is that for most of its length, the sausage is narrower than the ellipse, as the distorted “Bernstein ellipse” label makes clear. The ellipse has half-width approximately $\rho - 1$ , which is about $3 2 \%$ more than the half-width $0 . 7 6 ( \rho - 1 )$ of the sausage:

ellipse_width $=$ max(imag(z(1.15))) sausage_width $=$ max(imag(g(z(1.15)))) ratio $=$ ellipse_width/sausage_width ellipse_width = 0.1402 sausage_width $= ~ 0 . 1 0 6 1$ ratio $=$ 1.3210

We can learn more by looking at a family of ellipses. Following Chapter 8, here is a plot of $E _ { \rho }$ for $\rho = 1 , 1 . 2 , . . . , 2 . 2$ :

$\mathtt { w } = \mathtt { e x p } ( 2 \mathtt { i } \ast \mathtt { p i } \ast \mathtt { x } )$ ; for rho $=$ 1.1:0.2:2.2, plot( $( \mathtt { r h o } * _ { \mathsf { W } } + ( \mathtt { r h o } * _ { \mathsf { W } } ) \hat { \mathbf { \xi } } ( - 1 ) ) / 2 )$ , hold on, end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/e1cc3591d2061a32ed6003802c81f39d5c3810e6b7d48c452cb83c744bc29253.jpg)

Here is the corresponding figure for the images $g ( E _ { \rho } )$ :

for rho $= \ 1 . 1 : 0 . 2 : 2 . 2$ plot $( { \ g ( { ( { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } } ) } } } + { ( { { { \bf { \bar { \Phi } } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) } \hat { \bf { \Lambda } } } } ) } \cdot \mathrm { { \Lambda } } } ) } + ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) \cdot \mathrm { { \Lambda } }  )$ , hold on   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/70cb75854628d4586637894b834e8e541309db27a659f401d7dad8644d9e2bab.jpg)

It is clear that near $[ - 1 , 1 ]$ , the transformed ellipses are narrower and more uniform in shape than the ellipses, but further away, their behavior is more irregular. We shall see some of the implications of these shapes as we explore the uses of this map.
