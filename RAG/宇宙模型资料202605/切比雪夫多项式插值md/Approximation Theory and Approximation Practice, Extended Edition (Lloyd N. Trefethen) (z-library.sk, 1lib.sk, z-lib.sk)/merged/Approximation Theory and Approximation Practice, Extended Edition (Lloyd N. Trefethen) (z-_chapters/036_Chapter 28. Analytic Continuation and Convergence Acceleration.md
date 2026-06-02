# Chapter 28. Analytic Continuation and Convergence Acceleration

We have considered techniques for rational approximation by best approximation on an interval (Chapter 24, minimax), interpolation or linearized least-squares fitting on an interval or disk (Chapter 26, ratinterp and ratdisk), and Pad´e approximation at a point or Chebyshev–Pad´e approximation on an interval (Chapter 27, padeapprox and chebpade). In this final chapter, we turn to the application of such approximations for extrapolating a function to real or complex values $z$ outside the region where it is initially known. Three of the applications listed in Chapter 23 fall into this category: those numbered 3 (convergence acceleration for sequences and series), 4 (determination of poles), and 5 (analytic continuation).

It will be a chapter more of examples than theory. For an example to begin the discussion, suppose we pretend that we can evaluate

$$
f ( z ) = \operatorname { t a n h } ( z )
$$

for real values of $z$ but know nothing about complex values, and we wish to estimate where $f$ has poles. How might we proceed? (Of course we really know the answer: there are poles at all the odd multiples of $\pm \pi i / 2$ .)

The first thing to try might be polynomials. For example, we could use Chebfun to construct a polynomial that approximates $f$ to 16 digits on $[ - 1 , 1 ]$ ,

f = @(z) tanh(z); p = chebfun(f); length(p)

ans $=$ 30

From here, however, it is hard to make much progress. As we know from Chapter 8, $p$ will be a good approximation to $f$ within a certain Bernstein ellipse, the Chebfun ellipse, which can be plotted by the command plotregion. We can expect this ellipse to reach approximately out to the first singularities at $\pm \pi i / 2$ . Once we hit the ellipse, however, everything will change. According to the theory of Walsh [1959] and Blatt and Saff [1986] mentioned in Chapter 18, zeros of $p$ will cluster all along the boundary, and a further result of Blatt and Saff states that outside the ellipse, there will be no convergence at all. The polynomial $p$ will simply grow rapidly, its behavior having nothing to do with that of $f$ . We can confirm this prediction with contour plots. Here are plots of $| f ( z ) |$ and $| p ( z ) |$ in the upper half-plane, with black contours at levels $0 . 2 5 , 0 . 5 , \ldots , 3$ and red contours at $1 0 ^ { 1 } , 1 0 ^ { 3 } , 1 0 ^ { 5 } , \dots , 1 0 ^ { 1 9 }$ . We see immediately that $p$ matches $f$ very well inside the Chebfun ellipse, which is marked in blue, but not at all outside.

$\textbf { x } = \mathbf { \delta } - 4 : . 0 5 : 4$ ; $\texttt { y } = \texttt { 0 } : . 0 5 : 8$ ; [xx yy] $=$ meshgrid(x,y); $\mathrm { z z \ = \ \mathrm { x } \mathrm { x } \ + \ 1 i \mathrm { * } \mathrm { y } \mathrm { y } }$ ; ff = f(zz); $\mathtt { p p } = \mathtt { p } ( \mathtt { z } \mathtt { z } )$ ;   
lev1 $=$ .25:.25:2; lev2 = 10.^(1:2:19);   
subplot(1,2,1), contour(x,y,abs(ff),lev1,'k'), hold on contour(x,y,abs(ff),lev2,'r')   
subplot(1,2,2), contour(x,y,abs(pp),lev1,'k'), hold on contour(x,y,abs(pp),lev2, $" \mathbf { r } \cdot \mathbf { \xi }$ ), plotregion(p,'b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/8629c7df03e133bbf2924e062e7042469204fdfb0197a09f837a86ed316cdefd.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a2ca5ea5f99c523e430da9d6a5a1f689c7f5c975ce95610d127b90a29b00806b.jpg)

To get better information, we turn to rational approximation. A practical approach is to use ratinterp to compute rational linearized least-squares approximations of $f$ in $[ - 1 , 1 ]$ . Specifically, suppose we take $r$ to be the type $( 7 , 8 )$ approximation to $f$ in 1000 Chebyshev points and draw the same contour plots as before. The picture changes completely, showing very impressive agreement over most of the range plotted. This is the power and the promise of rational approximation.

d = domain(-1,1);   
[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,7,8,1000); $\mathbf { r } \mathbf { r } ~ = ~ \mathbf { r } \left( { \bf z } { \bf z } \right)$ ; subplot(1,2,1), contour(x,y,abs(ff),lev1,'k'), hold on contour(x,y,abs(ff),lev2,'r')   
subplot(1,2,2), contour(x,y,abs(rr),lev1,'k'), hold on contour(x,y,abs(rr),lev2,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a2e22e6021bf581acff7c45ce58c23f10b19fa5be049f34363b77383d9206149.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f56962bce9da3e4c02fb137c3d8d7ab3aeb79d774a0995a3a226fe0db100b517.jpg)

For a direct measure of the accuracy of $r$ as an approximation to $f$ , we can look at $| f ( z ) - r ( z ) |$ . In the following plot the contours, from bottom to top, lie at $1 0 ^ { - 1 4 } , 1 0 ^ { - 1 2 } , \textrm { -- } , 1 0 ^ { - 2 }$ . Evidently the approximation is excellent over a wide region.

$\mathtt { l e v e l s \ = \ 1 0 \_ \hat { \ } ( - 1 4 : 2 : - 2 ) }$ ; contour(x,y,abs(ff-rr),levels,'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/4a72e9fc14d019edb8529a1a25f24d4fd6c07b57513344bee9a57ef31d516c6a.jpg)

Results like these become all the more remarkable when one recalls that the problem of analytic continuation is ill-posed: analytic continuations are unique, but they do not depend continuously on the data. For example, the following observation shows the ill-posedness of the problem of continuing a function analytically from the interval $( - 1 , 1 )$ to the unit disk. If $f$ is analytic in the disk, then for any $\varepsilon > 0$ , there is another function $g$ analytic in the disk such that $\| f - g \| \ge 1$ on the disk and yet $\| f - g \| \leq \varepsilon$ on the interval. (Proof: Perturb $f$ by $\varepsilon \sin ( M z )$ for a suitable value of $M$ .) Because of this ill-posedness, every successful example of numerical analytic continuation must entail some smoothness assumptions about $f$ , whether implicit or explicit. That is to say, numerical analytic continuation always involves some kind of regularization. (A standard reference on this subject is [Hansen 1998].) In the computations just shown, the regularization is introduced by the use of the SVD in ratinterp.

The question with which we opened the discussion was, Where are the poles of $\operatorname { t a n h } ( z )$ ? To experiment with this, let us now apply ratinterp to compute approximants of types $( 2 , 2 ) , ( 3 , 3 ) , \dots , ( 8 , 8 )$ , and examine the poles of these approximations. In the next output, following the convention of the past few chapters, $( m , n )$

represents the permitted type of each approximant and $( \mu , \nu )$ the exact type, with $\mu \leq m$ and $\nu \leq n$ . Note that $( \mu , \nu )$ always comes out in the form (odd, even), because $f$ is an odd function. Thus there are always an even number of poles, which come in complex conjugate pairs and are pure imaginary, and we print just their positive imaginary parts.

for $\texttt { n } = \texttt { 2 } : 8$ [p,q,r,mu,nu,poles] $=$ ratinterp(d,f,n,n,1000);fprintf $( \cdot \setminus \mathrm { n } \left( \mathrm { m } , \mathrm { n } \right) = \left( \% \mathrm { d } , \% \mathrm { d } \right)$ , (mu,nu) $=$ (%d,%d):\n',n,n,mu,nu)yi $=$ sort(imag(poles)); fprintf('%15.10fi',yi(yi>0))  
end  
$( { \mathfrak { m } } , { \mathfrak { n } } ) = ( 2 , 2 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 1 , 2 ) :$ 1.8048291471i  
$( \mathrm { m } , \mathrm { n } ) = ( 3 , 3 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 3 , 2 ) :$ 1.5884736641i  
$( \mathrm { m } , \mathrm { n } ) = ( 4 , 4 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 3 , 4 ) :$ 1.5716968677i 6.6346803797i  
$( \mathrm { m } , \mathrm { n } ) = ( 5 , 5 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 5 , 4 ) :$ 1.5708250772i 5.0809800411i  
$( \mathtt { m } , \mathtt { n } ) = ( 6 , 6 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 5 , 6 )$ :1.5707969475i 4.7823014265i 13.7250545528i  
$( \mathtt { m } , \mathtt { n } ) = ( 7 , 7 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 7 , 6 )$ :1.5707963365i 4.7228280448i 9.4123430302i  
$( \mathtt { m } , \mathtt { n } ) = ( 8 , 8 )$ , (mu,nu)=(7,8):1.5707963258i 4.7123498987i 8.2068730934i 22.4267991875i

The table shows that for larger values of $( m , n )$ , two of the poles lie near $1 . 5 7 0 7 9 6 3 i$ and $4 . 7 1 i$ . We compare these with the actual first three poles of $\operatorname { t a n h } ( z )$ in the upper half-plane:

fprintf('%15.10fi',(pi/2) $^ *$ [1 3 5])

Exact poles:

1.5707963268i 4.7123889804i 7.8539816340i

Evidently the type $( 7 , 8 )$ approximation has captured the first two poles to 9 and 3 digits of accuracy, respectively, numbers that are consistent with the contour levels near $z = 1 . 5 7 i$ and $4 . 7 1 i$ in the last contour plot.

To understand computations like this, it is important to recognize that the “goal” of $r$ is not to find the poles of $f$ , but simply to approximate $f$ over $[ - 1 , 1 ]$ . If $r$ turns out to have poles near those of $f$ , this is a by-product, a side effect that happened because placing poles there is an effective strategy for approximation.15

To illustrate this, suppose we compare the type $( 7 , 8 )$ approximation above to one of type (15, 8). One might expect that with more degrees of freedom, the new approximation would capture the first pole more accurately. In fact, the approximation returned has exact type $( 1 5 , 2 )$ , and the accuracy of the pole has deteriorated, because the denominator is less important to the quality of the least-squares approximation:

[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,15,8,1000); fprintf $\therefore \ln ( \ln , \mathbf { n } ) = ( 1 5 , 8 )$ , (mu,nu) $=$ (%d,%d):\n',mu,nu) yi $=$ sort(imag(poles)); fprintf('%15.10fi',yi(yi>0))

$( \mathtt { m } , \mathtt { n } ) = ( 1 5 , 8 )$ , (mu,nu) $=$ (15,2): 1.5707964024i

If we go further and ask for a type (35, 8) approximant, ratinterp returns an approximation with no poles at all. The numerator now provides so much flexibility for the least-squares problem that the degrees of freedom in the denominator are not needed in 16-digit arithmetic, putting us back in the situation of the Chebfun ellipse of the first plot of this chapter.

[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,35,8,1000); fprintf $\therefore \ln ( \ln , \mathbf { n } ) = ( 3 5 , 8 )$ , (mu,nu) $=$ (%d,%d):\n',mu,nu)

$$
\left( \mathrm { m } , \mathrm { n } \right) = \left( 3 5 , 8 \right) , \left( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } \right) = \left( 2 5 , 0 \right) :
$$

One must always bear this in mind when using rational approximations for extrapolation: increasing $m$ and/or $n$ does not always improve the accuracy of the quantities one cares about.

One way to get an idea of the dependence of an approximation on $m$ and $n$ is to print a table of digits of accuracy. The following table, for example, indicates the number of digits of accuracy in the computed first pole of $\operatorname { t a n h } ( z )$ for $m =$ $1 , 3 , 5 , \ldots , 1 9$ and $n = 2 , 4 , 6 , \dots , 2 0$ , all based on robust least-squares fits in 200 Chebyshev points in 16-digit arithmetic. The table shows again the effect that increasing $m$ beyond a certain small value—moving right in the table—diminishes the accuracy of the pole.

err $=$ zeros(1,10);   
for $\texttt { n } = \texttt { 2 : 2 : 2 0 }$ for $\texttt { m } = \texttt { 1 : 2 : 1 9 }$ [p,q,r,mu,nu,poles] $=$ ratinterp(d,f,m,n,200); $\mathtt { p 1 } \ =$ imag(poles(abs(poles-1.6i) $= =$ min(abs(poles-1.6i)))); err((m+1)/2) $=$ -round(log10(abs(p1-pi/2))); end fprintf('%3d',err)   
end

<table><tr><td>DIGITS</td><td>OF 3</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>ACCURACY:LEAST-SQUARES 7</td></tr><tr><td>1 1</td><td>2 3</td><td>5</td><td>6</td><td>7 8</td><td>8</td><td>7</td><td></td></tr><tr><td>2</td><td>4</td><td>6 8</td><td>9</td><td>8</td><td>8 7</td><td></td><td></td></tr><tr><td>2</td><td>5</td><td>8</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>3</td><td></td><td>9</td><td>9 9</td><td>8</td><td></td><td>7</td><td></td></tr><tr><td>4</td><td></td><td>9</td><td>9</td><td>9 8</td><td>8</td><td>7</td><td></td></tr><tr><td>4</td><td>87</td><td>9</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>5</td><td>7</td><td>9</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>5</td><td>7</td><td></td><td>9 9</td><td>8</td><td></td><td>7</td><td>7</td></tr><tr><td>5</td><td>7</td><td>9 9</td><td>9 9</td><td>8</td><td>8 8</td><td>8 7</td><td>7</td></tr></table>

The use of rational approximations for locating poles or other singularities has an honorable history. Many applications are mentioned in the monograph by Baker and Graves-Morris [1996], which is a standard reference on Pad´e approximation. One interesting kind of application is to locating singularities of solutions of ODEs or PDEs computed numerically, an idea explored by Weideman, among others [2003]. For Chebfun-based explorations, including the application of ratinterp to find complex singularities of solutions to the Lorenz and Lotka–Volterra equations, see [Pach´on 2010] and [Webb 2013].

Having just mentioned Pad´e approximation, which was the subject of the last chapter, let us now turn to this alternative method of constructing rational approximations. Here is a repetition of the last experiment, the table of digits of accuracy in the first pole of $\operatorname { t a n h } ( z )$ , but now based on Pad´e approximation instead of rational least-squares. The results are similar, but better. This is not a general conclusion: it depends on the problem.

for $\texttt { n } = \texttt { 2 : 2 : 2 0 }$ for $\texttt { m } = \texttt { 1 : 2 : 1 9 }$ [r,a,b,mu,nu,poles] $=$ padeapprox(f,m,n); $\mathtt { p 1 } \ =$ imag(poles(abs(poles-1.57i) $\mathbf { \partial } = = \mathbf { \partial }$ min(abs(poles-1.57i)))); err((m+1)/2) $=$ -round(log10(abs(p1-pi/2))); end fprintf('%3d',err)   
end

<table><tr><td colspan="2"></td><td>DIGITS</td><td>4</td><td colspan="2">OF ACCURACY:PADE</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5 6</td><td>7 8</td><td>9 10 13 13</td></tr><tr><td>2</td><td>3</td><td>5</td><td>6 8</td><td>9 11</td><td>12</td></tr><tr><td>2</td><td>5</td><td>7</td><td>9 10</td><td>12 15</td><td>11 12 13</td></tr><tr><td>3</td><td>6</td><td>8</td><td>11 13</td><td>14 12</td><td>15 11 12</td></tr><tr><td>3</td><td>7</td><td>10</td><td>12</td><td>14 13 14</td><td>12 15 11</td></tr><tr><td>4</td><td>8</td><td>12</td><td>14 12</td><td>14 13</td><td>14 12 15</td></tr><tr><td>5</td><td>9</td><td>13</td><td>12 14</td><td>12 14</td><td>13 14 12</td></tr><tr><td>5</td><td>11</td><td>11</td><td>13 12</td><td>14 12</td><td>14 13 14</td></tr><tr><td>6</td><td>12</td><td>11</td><td>11 13</td><td>12 14</td><td>12 14 13</td></tr><tr><td>612</td><td></td><td>12</td><td>11 11</td><td>13 12</td><td>14 12 14</td></tr></table>

In principle, least-squares fitting and Pad´e approximation are very different techniques, since the first uses function values only at many different points, whereas the second uses values of the function and its derivatives at a single point. (These are the extreme cases of the general notion of multipoint Pad´e approximation.) In our actual computation, however, the difference is diminished, because padeapprox begins by computing Taylor coefficients numerically by the FFT based on samples of the function at roots of unity, a standard technique. So in fact, in this comparison, ratinterp and padeapprox both work from function values: the first from samples on $[ - 1 , 1 ]$ , the second from samples on the unit circle. This raises the question, What is achieved by passing through the intermediate stage of Taylor coefficients? It is a fair point, and indeed, another effective approach would be to solve a rational least-squares problem on the circle directly as in Chapter 26. Explorations of this kind are presented in [Pach´on 2010].

We now turn to the topic of acceleration of convergence of sequences and series. The challenge here is as follows. Suppose we know some of the initial terms of a convergent sequence,

$$
s _ { 0 } , s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . \to S ,
$$

and we want to estimate the limit $S$ . Equivalently, suppose we wish to estimate the limit of an infinite sum,

$$
S = a _ { 0 } + a _ { 1 } + a _ { 2 } + \cdots .
$$

The two problems are equivalent since we may regard (28.1) as a sequence of partial sums,

$$
s _ { n } = \sum _ { k = 0 } ^ { n } a _ { k } , \quad a _ { k } = s _ { k + 1 } - s _ { k } .
$$

If the sequence or series converges slowly, how might we speed it up? For example, perhaps we can afford to compute 20 terms, but this gives just 2-digit accuracy. Can we process the data further somehow to improve the accuracy to 6 digits?

There is a long history to such questions, reaching from Stirling and Euler to the recent tour de force solution of nine of the ten “SIAM 100-Digit Challenge” problems to 10000 digits of accuracy [Bornemann et al. 2004]. It is probably fair to say that almost every method for accelerating convergence is based on the idea of embedding the sequence in an analytic function, though this may not be how the original authors conceived or described their method.

One way in which a sequence might be embedded in an analytic function is if the terms of the sequence can be regarded as values of a fixed function at different arguments. For example, suppose we define a function $f ( z )$ at the points $z =$ $1 , 2 ^ { - 1 } , 2 ^ { - 2 } , \ldots$ by the formula $f ( 2 ^ { - k } ) = s _ { k }$ . Then (28.1) becomes

$$
f ( 1 ) , f ( 2 ^ { - 1 } ) , f ( 2 ^ { - 2 } ) , . . . \to S .
$$

Does this point of view help us estimate $S$ ? The answer will probably be yes if there exists a function $f$ that is analytic in a neighborhood of $z = 0$ and takes the given values at $z = 2 ^ { - k }$ . In such a case, to estimate $S$ , it is enough to interpolate some of the data by a polynomial $p ( z )$ and then compute $p ( 0 )$ . This is the method known as Richardson extrapolation, which is of great practical importance in applications.16 In a typical application, $h$ might be the mesh size of a numerical discretization and $f ( h ) , f ( h / 2 ) , f ( h / 4 ) , \ldots$ the estimates obtained of a quantity of interest as the mesh is successively refined. Often only even powers of $h$ appear, indicating that $f$ is an even function, so one could take the view that the data are given at $\pm h , \pm h / 2 , \ldots$ and Richardson extrapolation is really Richardson interpolation. In the specific case in which $f ( h )$ is an estimate of an integral by the trapezoidal or rectangle rule with step length $h$ , this becomes the quadrature method known as Romberg quadrature. Nor is the idea of polynomial extrapolation from data such as (28.4) limited to cases in which the sample points are related by factors of 2. If they are $1 , 1 / 2 , 1 / 3 , \ldots$ , this is called Salzer extrapolation [Salzer 1955].

Often, however, the limit of a sequence or series is not in the interior of a region of analyticity of an analytic function. In such a case there may be less mileage in Richardson extrapolation, and one looks for formulations adapted to the edge of a region of analyticity. For such problems, there is a basic starting point: to insert a parameter $z$ in (28.2) so that it becomes the series

$$
S ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdots .
$$

Now we have the problem of evaluating $S ( 1 )$ for a function $S ( z )$ with known Taylor coefficients. If (28.2) converges, then $z = 1$ is a point of convergence of (28.5), and if (28.2) converges more slowly than geometrically, then $z = 1$ must be on the boundary of the disk of convergence of (28.5). So by introducing a parameter $z$ , we have converted the problem of the summation of a slowly convergent series to a problem of evaluating an analytic function at a point on the boundary of the disk of convergence of its Taylor series.

The simplest idea would be to evaluate $S ( z )$ for a succession of values of $z$ and use the identity

$$
S ( 1 ) = \operatorname* { l i m } _ { z \to 1 } S ( z ) ,
$$

where the limit is over real values of $z$ increasing to 1. This idea is known as Abel summation [Hardy 1991].

A more powerful and general approach is to use rational functions, specifically Pad´e approximants since the data are given as Taylor coefficients. Two variants of this idea have received special attention. We could construct a sequence of type $( m , 1 )$ Pad´e approximants, with one pole, and evaluate them at $z = 1$ :

$$
r _ { 0 1 } ( 1 ) , r _ { 1 1 } ( 1 ) , r _ { 2 1 } ( 1 ) , \ldots .
$$

This is called Aitken extrapolation or Aitken’s $\Delta ^ { 2 }$ method, used by Aitken [1926], though with origins further back. Or we could work with type $( n , n )$ Pad´e approximants,

$$
r _ { 0 0 } ( 1 ) , r _ { 1 1 } ( 1 ) , r _ { 2 2 } ( 1 ) , \ldots .
$$

This is called epsilon extrapolation (originally for sequences) [Shanks 1955, Wynn 1956] or eta extrapolation (originally for series) [Bauer 1959]. An earlier appearance of essentially the same idea is due to Schmidt [1941].

Here is an example showing how powerful eta extrapolation can be for some problems. What is the value of

$$
S = \sum _ { n = 2 } ^ { \infty } { \frac { \sin ( n ) } { \log ( n ) } } ?
$$

The series is extremely slow to converge, as we see by taking partial sums of as many as a million terms:

${ \sf S } = \mathbb { Q } \left( { \sf { n } } \right)$ sum(sin(2:n)./log(2:n));for $\texttt { n } = \texttt { 1 0 . \hat { } } [ 1 : 6 ]$ , fprintf('%6.1e %12.6f\n',n,S(n)), end

<table><tr><td>n</td><td>S(n)</td></tr><tr><td>1.0e+01</td><td>0.907319</td></tr><tr><td>1.0e+02</td><td>0.457822</td></tr><tr><td>1.0e+03</td><td>0.669234</td></tr><tr><td>1.0e+04</td><td>0.761940</td></tr><tr><td>1.0e+05</td><td>0.764913</td></tr><tr><td>1.0e+06</td><td>0.609190</td></tr></table>

To get 10-digit accuracy by summing the series in this fashion, we would need $1 0 ^ { 1 0 0 0 0 0 0 0 0 0 0 }$ terms! The actual answer (not known analytically) is

$$
S \approx 0 . 6 8 3 9 1 3 7 8 6 4 1 8 2 8 \ldots
$$

Here are the diagonal extrapolants, that is, the results of eta extrapolation. Now we just go from $2 ^ { 1 }$ to $2 ^ { 6 }$ instead of from $1 0 ^ { 1 }$ to $1 0 ^ { 6 }$ , yet we get 14 digits of accuracy instead of 1:

$\mathtt { \Delta 1 } ~ = ~ 2 { : } 1 5 0$ ; c = [0 0 sin(n)./log(n)];   
for $\textbf { n } = \ 2 . \hat { \ } ( 1 { : } 6 )$ [r,a,b,mu,nu] $=$ padeapprox(c,n,n,0); fprintf(' (%2.0d,%2.0d) (%2.0d,%2.0d) %19.15f\n',n,n,mu,nu,r(1))   
end

<table><tr><td>n,n) (mu,nu) （ 2，2) (2，2) (4，4) (4，4) （8,8) (8,8) (16,16) (16,16) (32,32) (32,32)</td><td>r_nn(1) 0.987966950435009 0.716844624573063 0.684142517808568 0.683915162212272 0.683913786418312</td></tr></table>

The convergence is excellent. Note that we have computed Pad´e approximants nonrobustly by specifying a tolerance of 0 to padeapprox. In typical applications, this use of nonrobust formulas seems advantageous in extrapolation applications, though it brings a risk of sensitivity to noise. For this example, calling padeapprox with its default tolerance $1 0 ^ { - 1 4 }$ leads to stagnation at type (15, 15) with just 7 digits of accuracy.

This simple method of eta extrapolation, at least as implemented by the Chebfun Pad´e approximation code, can be encapsulated in a single MATLAB command we may call extrap. Given a sequence $a _ { 0 } , a _ { 1 } , \dotsc , a _ { N }$ , we can round $N / 2$ to integers (say, round up for $m$ and down for $_ { n }$ ) and then use padeapprox to compute the type $( m , n )$ Pad´e approximation $r$ . The accelerated value is then $r ( 1 )$ . Here is the code.

$\begin{array} { l } { { \tt e v a l \_ a t \_ 1 } = \ { \tt o } \left( { \tt r } \right) { \tt r } \left( 1 \right) ; { \tt N } 2 = \ { \tt O } \left( { \tt c } \right) { \tt 1 } { \tt e n g t h } \left( { \tt c } \right) / 2 ; } \end{array}$ extrap $=$ @(c) eval_at_1(padeapprox(c,ceil(N2(c)),floor(N2(c)),0));

The $\sin ( n ) / \log ( n )$ example just treated is this:

extrap([0 0 sin(2:150)./log(2:150)])

ans $=$ 0.683913786418279

For another example, suppose we extrapolate the alternating series

$$
1 - { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } - \cdot \cdot \cdot = \log ( 2 ) .
$$

The result is accurate to machine precision:

$$
\mathtt { \cdot t r a p } ( ( - 1 ) \cdot \hat { \mathbf { \alpha } } ^ { \hat { } } ( 0 : 3 0 ) \cdot / ( 1 : 3 1 ) ) , \mathtt { \ e x a c t } \ = \ \log ( 2 )
$$

ans = 0.693147180559945   
exact = 0.693147180559945

Note that here, the function $f$ of (28.5) is $\log ( 1 + z )$ , so this example shows that eta extrapolation can be effective for functions with branch cuts as well as poles.

Another famous alternating series, which we can obtain by setting $t = 0$ in (9.3), is

$$
1 - { \frac { 1 } { 3 } } + { \frac { 1 } { 5 } } - \cdot \cdot \cdot = { \frac { \pi } { 4 } } .
$$

Again, extrapolation gives machine precision:

extrap((-1).^(0:30)./(1:2:61)), exact = pi/4

ans $=$ 0.785398163397447   
exact $=$ 0.785398163397448

These examples are very impressive, but it is not always so. For example, here is what happens if we attempt to extrapolate the series

$$
\zeta ( 2 ) = 1 + { \frac { 1 } { 2 ^ { 2 } } } + { \frac { 1 } { 3 ^ { 2 } } } + \cdots = { \frac { \pi ^ { 2 } } { 6 } } ,
$$

extrap(1./(1:30).^2), exact = pi^2/6

ans $=$ 1.640824460821040   
exact $=$ 1.644934066848226

The convergence is very poor because in this case the function $f ( z )$ of (28.5), known as the dilogarithm, has a branch point at $z = 1$ itself. As it happens, this is a case where Salzer extrapolation is effective (Exercise 28.3).

The discussion of convergence acceleration of the last five pages has little in common with the large literature of this subject, because our focus has been solely on the underlying approximations, particularly Pad´e approximants, and not at all on the mechanics. Our numerical illustrations have utilized the linear algebra of Chapter 27, based on the SVD and requiring $O ( n ^ { 3 } )$ floating point operations to compute a single estimate based on a type $( n , n )$ approximant. The literature of convergence acceleration is quite different, for it emphasizes recurrence relations and triangular or rhomboidal arrays related to continued fractions that can be used to generate a sequence of approximations at great speed without solving matrix problems. These approaches are certainly faster, though they come with a risk of sensitivity to noise and the possibility of breakdown if there is a division by 0.

A major reason why we have ignored the mechanical or implementational aspects of convergence acceleration is that these matters are complicated—and, one might say, distracting. The differences between various extrapolation algorithms in practice can be quite intricate, and in a discussion of such matters, one quickly loses sight of the underlying mathematics of approximation. For details of these aspects of convergence acceleration see surveys such as Chapter 3 of [Baker & Graves-Morris 1996], [Brezinski & Redivo Zaglia 1991], [Gragg 1972], [Joyce 1971], [Sidi 2003], [Weniger 1989], [Wimp 1981], or the appendix by Laurie in [Bornemann et al. 2004]. Such literature also points to many further acceleration methods beyond those we have mentioned, such as Levin’s sequence transformation and Brezinski’s theta method.

We finish with an observation that points to exciting further territories of interest to mathematicians at least since Euler. The series (28.5) consists just of Taylor coefficients, so it is meaningful even if the radius of convergence is less than 1. Therefore our methods based on analytic continuation can sum divergent series as well as convergent ones. For example, the Taylor series

$$
{ \frac { 1 } { 1 + z } } = 1 - z + z ^ { 2 } - z ^ { 3 } + \cdot \cdot \cdot
$$

suggests the result

$$
1 - 1 + 1 - 1 + \cdot \cdot = { \frac { 1 } { 2 } }
$$

if we set $z = 1$ . Similarly, setting $z = 2$ suggests

$$
1 - 2 + 4 - 8 + \cdot \cdot \cdot = { \frac { 1 } { 3 } } .
$$

Are these identities “correct”? As usual in mathematics, the answer depends on what definitions we choose. The formulas (28.9) and (28.10) are not too problematic since they correspond to Taylor series with positive radii of convergence. In more challenging cases, the series is only asymptotic. For example, what about this series with factorial coefficients considered by Euler [1760],

$$
0 ! - 1 ! + 2 ! - 3 ! + \cdot \cdot = ?
$$

The factorials grow too fast to be Taylor coefficients for any function analytic in a neighborhood of $z = 0$ . However, they are the asymptotic series coefficients at $z = 0$ for a function analytic in the right half-plane, namely

$$
f ( z ) = \int _ { 0 } ^ { \infty } { \frac { e ^ { - t } } { 1 + z t } } d t .
$$

So a plausible candidate for the sum of (28.11), as suggested by Euler, is

$$
0 ! - 1 ! + 2 ! - 3 ! + \dots = f ( 1 ) = 0 . 5 9 6 3 4 7 3 6 2 \dots . . .
$$

Our code extrap makes a creditable attempt at computing this number:

extrap((-1).^(0:10).\*factorial(0:10))

ans $=$ 0.593294558846647

Summary of Chapter 28. Rational approximations provide one of the basic technologies for analytic continuation and extrapolation. In particular, Pad´e approximants are the basis of standard methods of convergence acceleration for sequences and series including the Aitken $\Delta ^ { 2 }$ , Shanks, epsilon, and eta methods.

Exercise 28.1. Contour plot for Taylor polynomials. Draw a contour plot like the pair in this chapter for the Taylor polynomial approximants to $f ( z ) = \operatorname { t a n h } ( z )$ . Comment on the result.

Exercise 28.2. The divergent factorial series. Compute numerically the Pad´e approximants $r _ { 3 3 } , r _ { 4 4 } , \ldots , r _ { 7 7 }$ for the Taylor coefficients (28.11), and show that they match $f ( 1 )$ to better than $1 \%$ , where $f$ is defined by (28.12). What accuracy do these approximants give for $f ( 1 / 2 )$ ?

Exercise 28.3. Zeta function. It was noted in the text that eta extrapolation is ineffective for the series (28.8). Study the behavior of Richardson and Salzer extrapolation instead.

Exercise 28.4. Alternating square roots. (a) To 8 digits of accuracy, what do you think is the limit of $1 - 1 / \sqrt { 2 } + 1 / \sqrt { 3 } - \cdot \cdot \cdot ?$ (b) To the same accuracy, what number would you propose as a good choice for the sum of the divergent series $1 - { \sqrt { 2 } } + { \sqrt { 3 } } - \dots ?$

Exercise 28.5. Approximations to $e ^ { z }$ . Compute type $( 1 , 1 )$ approximations to $e ^ { z }$ on $[ - 1 , 1 ]$ by (a) Pad´e approximation, (b) best approximation, (c) Chebyshev–Pad´e approximation, (d) Carath´eodory–Fej´er approximation, (e) interpolation in 3 Chebyshev points, and (f) linearized least-squares approximation in a number of Chebyshev points large enough to be effectively infinite. In each case list the coefficients, measure the $L ^ { 2 }$ and $L ^ { \infty }$ errors, and plot the error curve.

Exercise 28.6. Nonlinear least-squares approximation. Find a way to compute the true type $( 1 , 1 )$ nonlinear least-squares approximation to $e ^ { z }$ on $[ - 1 , 1 ]$ , and report the same data for this function as for the approximations of Exercise 28.7.

Exercise 28.7. An alternating series. The following identity is known:

$$
1 + { \frac { 1 } { 2 } } - { \frac { 1 } { 3 } } - { \frac { 1 } { 4 } } + { \frac { 1 } { 5 } } + { \frac { 1 } { 6 } } - { \frac { 1 } { 7 } } - \cdots = { \frac { \pi } { 4 } } + { \frac { 1 } { 2 } } \log 2 .
$$

How many digits do you get by taking $1 0 ^ { 1 } , 1 0 ^ { 2 } , \dots , 1 0 ^ { 6 }$ terms of the series? Can you get more by extrapolation?

# Appendix A. Six Myths of Polynomial Interpolation and Quadrature

[This article was first published by the Institute of Mathematics and Its Applications (www.ima.org.uk): L. N. Trefethen (2012), Six myths of polynomial interpolation and quadrature, Mathematics Today 47, no. 4, 184–188.]

It is a pleasure to offer this essay for Mathematics Today as a record of my Summer Lecture on 29 June 2011 at the Royal Society.

Polynomials are as basic a topic as any in mathematics, and for numerical mathematicians like me, they are the starting point of numerical methods that in some cases go back centuries, like quadrature formulas for numerical integration and Newton iterations for finding roots. You would think that by now, the basic facts about computing with polynomials would be widely understood. In fact, the situation is almost the reverse. There are indeed widespread views about polynomials, but some of the important ones are wrong, founded on misconceptions entrenched by generations of textbooks.

Since 2006, my colleagues and I have been solving mathematical problems with polynomials using the Chebfun software system (www.chebfun.org). We have learned from daily experience how fast and reliable polynomials are. This entirely positive record has made me curious to try to pin down where these misconceptions come from, and this essay is an attempt to summarize some of my findings.

The essay is organised around “six myths.” Each myth has some truth in it— mathematicians rarely say things that are simply false! Yet each one misses something important.

Throughout the discussion, $f$ is a continuous function defined on the interval $[ - 1 , 1 ]$ , $n + 1$ distinct points $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ are given, and $p _ { n }$ is the unique polynomial of degree at most $n$ with $p _ { n } ( x _ { j } ) ~ = ~ f ( x _ { j } )$ for each $j$ . Two families of points will be of particular interest: equispaced points, $x _ { j } = - 1 + 2 j / n$ , and Chebyshev points, $x _ { j } = \cos ( j \pi / n )$ . I will also mention Legendre points, defined as the zeros of the degree $n + 1$ Legendre polynomial $P _ { n + 1 }$ .

The discussion of each myth begins with two or three representative quotations from leading textbooks, listed anonymously with the year of publication. Then I say a word about the mathematical truth underlying the myth, and after that, what that truth overlooks.

# Myth 1. Polynomial interpolants diverge as $n \to \infty$

Textbooks regularly warn students not to expect $p _ { n } \to f$ as $n \to \infty$ “Polynomial interpolants rarely converge to a general continuous function.” (1989)

“Unfortunately, there are functions for which interpolation at the Chebyshev points fails to converge.” (1996)

On the face of it, this caution is justified by two theorems. Weierstrass proved in 1885 that any continuous function can be approximated arbitrarily closely by polynomials. On the other hand, Faber proved in 1914 that no polynomial interpolation scheme, no matter how the points are distributed, will converge for all such functions.

So it sounds as if there is something wrong with polynomial interpolation. Yet the truth is, polynomial interpolants in Chebyshev points always converge if $f$ is $a$ little bit smooth. (We shall call them Chebyshev interpolants.) Lipschitz continuity is more than enough, that is, $| f ( x ) - f ( y ) | \leq L | x - y |$ for some constant $L$ and all $x , y \in [ - 1 , 1 ]$ . So long as $f$ is Lipschitz continuous, as it will be in almost any practical application, $p _ { n } \to f$ is guaranteed.

There is indeed a big problem with convergence of polynomial interpolants, but it pertains to interpolation in equispaced points. As Runge showed in 1901, equispaced interpolants may diverge exponentially, even if $f$ is so smooth as to be analytic (holomorphic). This genuinely important fact, known as the Runge phenomenon, has confused people. With Faber’s theorem seeming to provide justification, a real problem with equispaced polynomial interpolants has been overgeneralized so that people have suspected it of applying to polynomial interpolants in general.

The smoother $f$ is, the faster its Chebyshev interpolants converge. If $f$ has $\nu$ derivatives, with the $\nu$ th derivative being of bounded variation $V$ , then $\| f - p _ { n } \| =$ $O ( V n ^ { - \nu } )$ as $n  \infty$ . (By $\| f - p _ { n } \|$ I mean the maximum of $| f ( x ) - p _ { n } ( x ) |$ for $x \in [ - 1 , 1 ]$ .) If $f$ is analytic, the convergence is geometric, with $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ for some $\rho > 1$ . I will give details about the parameter $\rho$ under Myth 5.

For example, here is the degree 10000 Chebyshev interpolant $p _ { n }$ to the sawtooth function $f ( x )$ defined as the integral from $^ { - 1 }$ to $x$ of $\mathrm { s i g n } ( \sin ( 1 0 0 t / ( 2 - t ) )$ ). This curve may not look like a polynomial, but it is! With $\| f - p _ { n } \| \approx 0 . 0 0 0 1$ , the plot is indistinguishable from a plot of $f$ itself.

$$
\int M M M \min
$$

There is not much use in polynomial interpolants to functions with so little smoothness as this, but mathematically they are trouble free. For smoother functions like $e ^ { x }$ , $\cos ( 1 0 x )$ or $1 / ( 1 + 2 5 x ^ { 2 } )$ , we get convergence to 15 digits of accuracy for small values of $n$ (14, 34, and 182, respectively).

# Myth 2. Evaluating polynomial interpolants numerically is problematic

Interpolants in Chebyshev points may converge in theory, but aren’t there problems on a computer? Textbooks warn students about this.

“Polynomial interpolation has drawbacks in addition to those of global convergence. The determination and evaluation of interpolating polynomials of high degree can be too time-consuming and can also lead to difficulty problems associated with roundoff error.” (1977)

“Although Lagrangian interpolation is sometimes useful in theoretical investigations, it is rarely used in practical computations.” (1985)

“Interpolation is a notoriously tricky problem from the point of view of numerical stability.” (1990)

The origin of this view is the fact that some of the methods one might naturally try for evaluating polynomial interpolants are slow or numerically unstable or both. For example, if you write down the Lagrange interpolation formula in its most obvious form and implement it on a computer as written, you get an algorithm that requires $O ( n ^ { 2 } )$ work per evaluation point. (Partly because of this, books warn readers that they should use Newton interpolation formulas rather than Lagrange— another myth.) And if you compute interpolants “linear algebra style” by setting up a Vandermonde matrix whose columns contain samples of $1 , x , x ^ { 2 } , \ldots , x ^ { n }$ at the grid points, your numerical method is exponentially unstable. This is the “polyval/polyfit” algorithm of MATLAB, and I am guilty of propagating Myth 2 myself by using this algorithm in my textbook Spectral Methods in MATLAB. Rounding errors on a computer destroy all accuracy of this method even for $n = 6 0$ , let alone $n = 1 0 0 0 0$ as in the plot above.

Or how about $n = 1$ ,000,000? Here is a plot of the polynomial interpolant to $f ( x ) = \sin ( 1 0 / x )$ in a million Chebyshev points. The plot was obtained in about 30 seconds on my laptop by evaluating the interpolant at 2000 points clustered near zero.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/162d2e5dae70ccdf319789bcd980fe9124166566fef0af4445294e145a7058ec.jpg)

The fast and stable algorithm that makes these calculations possible comes from a representation of the Lagrange interpolant known as the barycentric formula, published by Salzer in 1972:

$$
p _ { n } ( x ) = { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } f _ { j } } { x - x _ { j } } } \Bigg / { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } } { x - x _ { j } } } ,
$$

with the special case $p _ { n } ( x ) = f _ { j }$ if $\boldsymbol { x } = \boldsymbol { x } _ { j }$ . The primes on the summation signs signify that the terms $j = 0$ and $j = n$ are multiplied by $1 / 2$ . The work required is $O ( n )$ per evaluation point, and though the divisions by $\boldsymbol { x } - \boldsymbol { x _ { j } }$ may look dangerous for $x \approx x _ { j }$ , the formula is numerically stable, as was proved by Nick Higham in 2004.

# Myth 3. Best approximations are optimal

This one sounds true by definition!

“Since the Remes algorithm, or indeed any other algorithm for producing genuine best approximations, requires rather extensive computations, some interest attaches to other more convenient procedures to give good, if not optimal, polynomial approximations.” (1968)

“Minimal polynomial approximations are clearly suitable for use in functions evaluation routines, where it is advantageous to use as few terms as possible in an approximation.” (1968)

“Ideally, we would want a best uniform approximation.” (1980)

Though the statement of this myth looks like a tautology, there is content in it. The “best approximation” is a common name for the unique polynomial $\boldsymbol { p } _ { n } ^ { * }$ that minimizes $\| f - p _ { n } ^ { * } \|$ . So a best approximant is optimal in the maximum norm, but is it really the best in practice?

As the first quotation suggests, computing $\boldsymbol { p } _ { n } ^ { * }$ is not a trivial matter, since the dependence on $f$ is nonlinear. By contrast, computing a Chebyshev interpolant with the barycentric formula is easy. Here our prejudices about value for money begin to intrude. If best approximations are hard to compute, they must be valuable!

Two considerations make the truth not so simple. First of all, the maximumnorm accuracy difference between Chebyshev interpolants and best approximations can never be large, for Ehlich and Zeller proved in 1966 that $\| f - p _ { n } \|$ cannot exceed $\| f - p _ { n } ^ { * } \|$ by more than the factor $2 + ( 2 / \pi ) \log ( n + 1 )$ . Usually the difference is less than that, and in fact the best known error bounds for functions that have $\nu$ derivatives or are analytic—the two smoothness classes mentioned under Myth 1— are just a factor of 2 larger for Chebyshev interpolants as for best approximations.

Secondly, according to the equioscillation theorem going back to Chebyshev in the 1850s, the maximum error of a best approximation is always attained at at least $n + 2$ points in $[ - 1 , 1 ]$ . For example, the black curve below is the error curve $f ( x ) - p _ { n } ^ { * } ( x )$ , $x \in [ - 1 , 1 ]$ , for the best approximant to $| x - 1 / 4 |$ of degree 100, equioscillating between 102 extreme values $\approx \pm 0 . 0 0 2 7$ . The red curve corresponds to the polynomial interpolant $p _ { n }$ in Chebyshev points. It is clear that for most values of $x$ , $| f ( x ) - p _ { n } ( x ) |$ is much smaller than $\left| f ( x ) - p _ { n } ^ { * } ( x ) \right|$ . Which approximation would be more useful in an application? I think the only reasonable answer is, it depends. Sometimes one really does need a guarantee about worst-case behavior. In other situations, it would be wasteful to sacrifice so much accuracy over 95% of the range just to gain one bit of accuracy in a small subinterval.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/8bc50a0f5e4b96ca11c50508e652aebb691db3daa1b3ff1dc5d0b9a0f06d297a.jpg)

# Myth 4. Gauss quadrature has twice the order of accuracy of Clenshaw–Curtis

Quadrature formulas are usually derived from polynomials. We approximate an integral by a finite sum,

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x \quad \approx \quad I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) ,
$$

and the weights $\{ w _ { k } \}$ are determined by the principle of interpolating $f$ by a polynomial at the points $\{ x _ { k } \}$ and integrating the interpolant. Newton–Cotes quadrature corresponds to equispaced points, Clenshaw–Curtis quadrature to Chebyshev points, and Gauss quadrature to Legendre points. Almost every textbook first describes Newton–Cotes, which achieves ${ \boldsymbol { I } } _ { n } = { \boldsymbol { I } }$ exactly if $f$ is a polynomial of degree $n$ , and then shows that Gauss has twice this order of exactness: ${ { I } _ { n } } \mathrm { ~ = ~ } I$ if $f$ is a polynomial of degree $2 n + 1$ . Clenshaw–Curtis is occasionally mentioned, but it only has order of exactness $n$ , no better than Newton–Cotes.

“However, the degree of accuracy for Clenshaw–Curtis quadrature is only $n - 1$ .” (1997)

“Clenshaw–Curtis rules are not optimal in that the degree of an n-point rule is only $n - 1$ , which is well below the maximum possible.” (2002)

This ubiquitous emphasis on order of exactness is misleading. Textbooks suggest that the reason Gauss quadrature gives better results than Newton–Cotes is its higher order of exactness, but this is not correct. The problem with Newton–Cotes is that the sample points are equally spaced: the Runge phenomenon. In fact, as P´olya proved in 1933, Newton–Cotes quadrature does not converge as $n  \infty$ , in general, even if $f$ is analytic.

Clenshaw–Curtis and Gauss quadratures behave entirely differently. Both schemes converge for all continuous integrands, and if the integrand is analytic, the convergence is geometric. Clenshaw–Curtis is easy to implement, using either the Fast Fourier Transform or by an algorithm of Waldvogel in 2006, and one reason it gets little attention may be that Gauss quadrature had a big head start, invented in 1814 instead of 1960. Both Clenshaw–Curtis and Gauss quadrature are practical even if $n$ is in the millions, in the latter case because nodes and weights can be calculated by an algorithm implemented in Chebfun due to Glaser, Liu and Rokhlin in 2007. (Indeed, since Glaser–Liu–Rokhlin, it is another myth to imagine that Gauss quadrature is only practicable for small values of $n$ .)

With twice the order of exactness, we would expect Gauss quadrature to converge twice as fast as Clenshaw–Curtis. Yet it does not. Unless $f$ is analytic in a large region surrounding $[ - 1 , 1 ]$ in the complex plane, one typically finds that Clenshaw–Curtis quadrature converges at about the same rate as Gauss, as illustrated by these curves for $f ( x ) = \exp ( - 1 / x ^ { 2 } )$ :

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6d9bb5af3a37051ca1ddc3ad6f6613f5ce3a4982085af7398e06ef38c270de3f.jpg)

A theorem of mine from 2008 makes this observation precise. If $f$ has a $\nu$ th derivative of bounded variation $V$ , Gauss quadrature can be shown to converge at the rate $O ( V ( 2 n ) ^ { - \nu } )$ , the factor of 2 reflecting its doubled order of exactness. The theorem asserts that the same rate $O ( V ( 2 n ) ^ { - \nu } )$ , with the same factor of 2, is also achieved by Clenshaw–Curtis. (Folkmar Bornemann (private communication) has pointed out that both of these rates can probably be improved by one further power of $n$ .)

The explanation for this surprising result goes back to O’Hara and Smith in 1968. It is true that $( n + 1 )$ -point Gauss quadrature integrates the Chebyshev polynomials $T _ { n + 1 } , T _ { n + 2 } , . . .$ exactly whereas Clenshaw–Curtis does not. However, the error that Clenshaw–Curtis makes consists of aliasing them to the Chebyshev polynomials $T _ { n - 1 } , T _ { n - 2 } , . . .$ and integrating these correctly. As it happens, the integrals of $T _ { n + k }$ and $T _ { n - k }$ differ by only $O ( n ^ { - 3 } )$ , and that is why Clenshaw–Curtis is more accurate than its order of exactness seems to suggest.

# Myth 5. Gauss quadrature is optimal

Gauss quadrature may not be much better than Clenshaw–Curtis, but at least it would appear to be as accurate as possible, the gold standard of quadrature formulas.

“The precision is maximised when the quadrature is Gaussian.” (1982)

“In fact, it can be shown that among all rules using n function evaluations, the $n$ -point Gaussian rule is likely to produce the most accurate estimate.” (1989)

There is another misconception here, quite different from the one just discussed as Myth 4. Gauss quadrature is optimal as measured by polynomial order of exactness, but that is a skewed measure.

The power of polynomials is nonuniform: they have greater resolution near the ends of an interval than in the middle. Suppose, for example, that $f ( x )$ is an analytic function on $[ - 1 , 1 ]$ , which means it can be analytically continued into a neighborhood of $[ - 1 , 1 ]$ in the complex $x$ -plane. Then polynomial approximants to $f$ , whether Chebyshev or Legendre interpolants or best approximants, will converge at a geometric rate $O ( \rho ^ { - n } )$ determined by how close any singularities of $f$ in the plane are to $[ - 1 , 1 ]$ . To be precise, $\rho$ is the sum of the semiminor and semimajor axis lengths of the largest ellipse with foci $\pm 1$ inside which $f$ is analytic and bounded. But ellipses are narrower near the ends than in the middle. If $f$ has a singularity at $x _ { 0 } = i \varepsilon$ for some small $\varepsilon$ , then we get $O ( \rho ^ { - n } )$ convergence with $\rho \approx 1 + \varepsilon$ . If √ $f$ has a singularity at $1 + \varepsilon$ , on the other hand, the parameter becomes $\rho \approx 1 + \sqrt { 2 \varepsilon }$ , corresponding to much faster convergence. A function with a singularity at 1.01 converges 14 times faster than one with a singularity at $0 . 0 1 i$ .

Quadrature rules generated by polynomials, including both Gauss and Clenshaw–Curtis, show the same nonuniformity. This might seem unavoidable, but in fact, there is no reason why a quadrature formula (A.1) needs to be derived from polynomials. By introducing a change of variables, one can generate alternative formulas based on interpolation by transplanted polynomials, which may converge up to $\pi / 2$ times faster than Gauss or Clenshaw–Curtis quadrature for many functions. This idea was developed in a paper of mine with Nick Hale in 2008 and is related to earlier work by Kosloff and Tal-Ezer in 1993.

The following theorem applies to one of the transformed methods Hale and I proposed. Let $f$ be a function that is analytic in an $\varepsilon$ -neighborhood of $\lfloor - 1 , 1 \rfloor$ for $\varepsilon \leq$ 0.05. Then whereas Gauss quadrature converges at the rate $I _ { n } - I = O ( ( 1 + \varepsilon ) ^ { - 2 n } )$ , transformed Gauss quadrature converges $5 0 \%$ faster, $I _ { n } - I = O ( ( 1 + \varepsilon ) ^ { - 3 n } )$ . Here is an illustration for $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ .

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/38f190837c274692b5cea20fae46462403b16b1e8502ef891a491d91f1f2f6b7.jpg)

The fact that some quadrature formulas converge up to $\pi / 2$ times faster than Gauss as $n \to \infty$ is probably not of much practical importance. The importance is conceptual.

# Myth 6. Polynomial root-finding is dangerous

Our final myth originates with Jim Wilkinson (1919–1986), a hero of mine who taught me two courses in graduate school at Stanford. Working with Alan Turing on the Pilot Ace computer in 1950, Wilkinson found that attempts to compute roots of even some low-degree polynomials failed dramatically. He publicized this discovery widely.

“Our main object in this chapter has been to focus attention on the severe inherent limitations of all numerical methods for finding the zeros of polynomials.” (1963)

“Beware: Some polynomials are ill-conditioned!” (1992)

The first of these quotations comes from Wilkinson’s book on rounding errors, and he also coined the memorable phrase “the perfidious polynomial” as the title of a 1984 article that won the Chauvenet Prize for outstanding mathematical exposition.

What Wilkinson discovered was the extreme ill-conditioning of roots of certain polynomials as functions of their coefficients. Specifically, suppose a polynomial $p _ { n }$ is specified by its coefficients in the form $a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ . If $p _ { n }$ has roots near the unit circle in the complex plane, these pose no difficulties: they are wellconditioned functions of the coefficients $a _ { k }$ and can be computed accurately by the MATLAB roots command, based on the calculation of eigenvalues of a companion matrix containing the coefficients. Roots far from the circle, however, such as roots on the interval $[ - 1 , 1 ]$ , can be so ill-conditioned as to be effectively uncomputable. The monomials $x ^ { k }$ form exponentially bad bases for polynomials on $[ - 1 , 1 ]$ .

The flaw in the argument is that it says nothing about the condition of roots of polynomials as functions of their values. For effective root-finding on $[ - 1 , 1 ]$ based on pointwise samples, all one must do is fix the basis: replace the monomials $x ^ { k }$ , which are orthogonal polynomials on the unit circle, by the Chebyshev polynomials $T _ { k } ( x )$ , which are orthogonal on the interval. Suppose a polynomial $p _ { n }$ is specified by its coefficients in the form $a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + a _ { n } T _ { n } ( x )$ . If $p _ { n }$ has roots near $[ - 1 , 1 ]$ , these are well-conditioned functions of the coefficients $a _ { k }$ , and they can be computed accurately by solving an eigenvalue problem involving a “colleague matrix.” The details were worked out by Specht in 1957 and Good in 1961.

Chebfun finds roots of a function $f$ on $[ - 1 , 1 ]$ by approximating it by a polynomial expressed in Chebyshev form and then solving a colleague-matrix eigenvalue problem, and if the degree is greater than 100, first subdividing the interval recursively to reduce it. These ideas originated with John Boyd in 2002 and are extraordinarily effective. Far from being exceptionally troublesome, polynomial root-finding when posed in this fashion begins to emerge as the most tractable of all root-finding problems, for we can solve the problem globally with just $O ( n ^ { 2 } )$ work to get all the roots in an interval to high accuracy.

For example, the function $f ( x ) = \sin ( 1 0 0 0 \pi x )$ on $[ - 1 , 1 ]$ is represented in Chebfun by a polynomial of degree 4091. It takes 2 seconds on my laptop to find all

2001 of its roots in $[ - 1 , 1 ]$ , and the maximum deviation from the exact values is $4 . 4 \times 1 0 ^ { - 1 6 }$ .

Here is another illustration of the robustness of polynomial root-finding on an interval. In Chebfun, we have plotted the function $f ( x ) = \exp ( x / 2 ) ( \sin ( 5 x )$ $+ \sin ( 1 0 1 x ) ,$ ) and then executed the commands $\mathbf { r } ~ = ~ \mathbf { r o o t s } \left( \mathbf { f - r o u n d } \left( \mathbf { f } \right) \right)$ , $\mathtt { p l o t } ( \mathtt { r } , \mathtt { f } \left( \mathtt { r } \right) , \mathtt { \xi } ^ { \prime } \cdot \mathtt { \xi } ^ { \prime } )$ . This sequence solves a collection of hundreds of polynomial root-finding problems to locate all the points where $f$ takes a value equal to an integer or a half-integer, and plots them as dots. The computation took $2 / 3$ of a second.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/aa94022df73a9a664b4cb4073759540e659b4caa33f59bc66b7ecbb3db693682.jpg)

# Conclusion

Perhaps I might close by mentioning another perspective on the misconceptions that have affected the study of computation with polynomials. By the change of variables $x = \cos \theta$ , one can show that interpolation by polynomials in Chebyshev points is equivalent to interpolation of periodic functions by series of sines and cosines in equispaced points. The latter is the subject of discrete Fourier analysis, and one cannot help noting that whereas there is widespread suspicion that it is not safe to compute with polynomials, nobody worries about the Fast Fourier Transform! In the end this may be the biggest difference between Fourier and polynomial interpolants, the difference in their reputations.

And here’s a bonus, free of charge.

# Myth 7. Lagrange discovered Lagrange interpolation

It was Waring in 1779. Euler used the formula in 1783, and Lagrange in 1795.

# Appendix B. “ATAP for Periodic Functions”

[This article was first published by the Society for Industrial and Applied Mathematics (www.siam.org): G. B. Wright, M. Javed, H. Montanelli, and L. N. Trefethen (2015), Extension of Chebfun to periodic functions, SIAM J. Sci. Statist. 37, no. 5, C554–C573.]

# B.1 Introduction

It is well known that trigonometric representations of periodic functions and Chebyshev polynomial representations of nonperiodic functions are closely related. Table B.1 lists some of the parallels between these two situations. Chebfun, a software system for computing with functions and solving ordinary differential equations (ODEs) [4, 12, 27], relied entirely on Chebyshev representations in its first decade. This paper describes its extension to periodic problems initiated by the first author and released with Chebfun Version 5.1 in December 2014.

Though Chebfun is a software product, the main focus of this paper is mathematics and algorithms rather than software per se. What makes this subject interesting is that the trigonometric/Chebyshev parallel, though close, is not an identity. The experience of building a software system based first on one kind of representation and then extending it to the other has given the Chebfun team a uniquely intimate view of the details of these relationships. We begin this paper by listing 10 differences between Chebyshev and trigonometric formulations that we have found important. This will set the stage for presentations of the problems of trigonometric series, polynomials, and projections (Section B.2), trigonometric interpolants, aliasing, and barycentric formulas (Section B.3), approximation theory and quadrature (Section B.4), and various aspects of our algorithms (Sections B.5–B.7).

Table B.1: Some parallels between trigonometric and Chebyshev settings. The row of contributors’ names is just a sample of some key figures.   

<table><tr><td>Trigonometric</td><td>Chebyshev</td></tr><tr><td>t ∈[0,2π]</td><td>x ∈[-1,1]</td></tr><tr><td>periodic</td><td>nonperiodic</td></tr><tr><td>exp(ikt)</td><td>T(x）</td></tr><tr><td>trigonometric polynomials</td><td>algebraic polynomials</td></tr><tr><td>equispaced points</td><td>Chebyshev points</td></tr><tr><td>trapezoidal rule</td><td>Clenshaw-Curtis quadrature</td></tr><tr><td>companion matrix</td><td>colleague matrix</td></tr><tr><td>Horner&#x27;srule</td><td>Clenshaw recurrence</td></tr><tr><td>fast Fourier transform</td><td>fast cosine transform</td></tr><tr><td>Gauss,Fourier, Zygmund,...</td><td>Bernstein,Lanczos,Clenshaw,..</td></tr></table>

1. One basis or two. For working with polynomials on $[ - 1 , 1 ]$ , the only basis functions one needs are the Chebyshev polynomials $T _ { k } ( x )$ . For trigonometric polynomials on $[ 0 , 2 \pi ]$ , on the other hand, there are two equally good equivalent choices: complex exponentials $\exp ( i k t )$ , or sines and cosines $\sin ( k t )$ and $\cos ( k t )$ . The former is mathematically simpler; the latter is mathematically more elementary and provides a framework for dealing with even and odd symmetries. A fully useful software system for periodic functions needs to offer both kinds of representation.

2. Complex coefficients. In the $\exp ( i k t )$ representation, the expansion coefficients of a real periodic function are complex. Mathematically, they satisfy certain symmetries, and a software system needs to enforce these symmetries to avoid imaginary rounding errors. Polynomial approximations of real nonperiodic functions, by contrast, do not lead to complex coefficients.

3. Even and odd numbers of parameters. A polynomial of degree $n$ is determined by $n + 1$ parameters, a number that may be odd or even. A trigonometric polynomial of degree $n$ , by contrast, is determined by $2 n + 1$ parameters, always an odd number, as a consequence of the $\exp ( \pm i n x )$ symmetry. For most purposes it is unnatural to speak of trigonometric polynomials with an even number of degrees of freedom. Even numbers make sense, on the other hand, in the special case of trigonometric polynomials defined by interpolation at equispaced points, if one imposes the symmetry condition that the interpolant of the $( - 1 ) ^ { j }$ sawtooth should be real, i.e., a cosine rather than a complex exponential. Here distinct formulas are needed for the even and odd cases.

4. The effect of differentiation. Differentiation lowers the degree of an algebraic polynomial, but it does not lower the degree of a trigonometric polynomial; indeed it enhances the weight of its highest-degree components.

5. Uniform resolution across the interval. Trigonometric representations have uniform properties across the interval of approximation, but polynomials are nonuniform, with much greater resolution power near the ends of $[ - 1 , 1 ]$ than near the

middle [28, Chap. 22].

6. Periodicity and translation invariance. The periodicity of trigonometric representations means that a periodic chebfun constructed on $[ 0 , 2 \pi ]$ , say, can be perfectly well evaluated at $1 0 \pi$ or $1 0 0 \pi$ ; nonperiodic chebfuns have no such global validity. Thus, whereas interpolation and extrapolation are utterly different for polynomials, they are not so different in the trigonometric case. A subtler consequence of translation invariance is explained in the footnote at the beginning of Section B.5.

7. Operations that break periodicity. A function that is smooth and periodic may lose these properties when restricted to a subinterval or subjected to operations like rounding or absolute value. This elementary fact has the consequence that a number of operations on periodic chebfuns require their conversion to nonperiodic form.

8. Good and bad bases. The functions $\exp ( i k t )$ or $\sin ( k t )$ and $\cos ( k t )$ are wellbehaved by any measure, and nobody would normally think of using any other basis functions for representing trigonometric functions. For polynomials, however, many people would reach for the basis of monomials $x ^ { k }$ before the Chebyshev polynomials $T _ { k } ( x )$ . Unfortunately, the monomials are exponentially ill-conditioned on $[ - 1 , 1 ]$ : a degree- $n$ polynomial of size $^ { 1 }$ on $[ - 1 , 1 ]$ will typically have coefficients of order $2 ^ { n }$ when expanded in the basis $1 , x , \ldots , x ^ { n }$ . Use of this basis will cause trouble in almost any numerical calculation unless $n$ is very small.

9. Good and bad interpolation points. For interpolation of periodic functions, nobody would normally think of using any interpolation points other than equispaced. For interpolation of nonperiodic functions by polynomials, however, equispaced points lead to exponentially ill-conditioned interpolation problems [23, 72]. The mathematically appropriate choice is not obvious until one learns it: Chebyshev points, quadratically clustered near $\pm 1$ .

10. Familiarity. All the world knows and trusts Fourier analysis. By contrast, experience with Chebyshev polynomials is often the domain of experts, and it is not as widely appreciated that numerical computations based on polynomials can be trusted. Historically, points 8 and 9 of this list have led to this mistrust.

The book Approximation Theory and Approximation Practice [28] summarizes the mathematics and algorithms of Chebyshev technology for nonperiodic functions. The present paper was written with the goal in mind of compiling analogous information in the trigonometric case. In particular, Section B.2 corresponds to Chapter 3 of [28], Section B.3 to Chapters 2, 4, and 5, and Section B.4 to Chapters 6, 7, 8, 10, and 19.

# B.2 Trigonometric series, polynomials, and projections

Throughout this paper, we assume $f$ is a Lipschitz continuous periodic function on $[ 0 , 2 \pi ]$ . Here and in all our statements about periodic functions, the interval $[ 0 , 2 \pi ]$ should be understood periodically: $t = 0$ and $t = 2 \pi$ are identified, and any smoothness assumptions apply across this point in the same way as for $t \in$ $( 0 , 2 \pi )$ [18, Chap. 1].

It is known that $f$ has a unique trigonometric series, absolutely and uniformly

convergent, of the form

$$
f ( t ) = \sum _ { k = - \infty } ^ { \infty } c _ { k } e ^ { i k t } ,
$$

with Fourier coefficients

$$
c _ { k } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) e ^ { - i k t } d t .
$$

(All coefficients in our discussions are in general complex, though in cases of certain symmetries they will be purely real or imaginary.) Equivalently, we have

$$
f ( t ) = \sum _ { k = 0 } ^ { \infty } a _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { \infty } b _ { k } \sin ( k t ) ,
$$

with $a _ { 0 } = c _ { 0 }$ and

$$
a _ { k } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \cos ( k t ) d t , \quad b _ { k } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \sin ( k t ) d t \qquad ( k \geq 1 ) .
$$

The formulas (B.4) can be derived by matching the $e ^ { i k t }$ and $e ^ { - i k t }$ terms of (B.3) with those of (B.1), which yields the identities

$$
c _ { k } = \frac { a _ { k } } { 2 } + \frac { b _ { k } } { 2 i } , \quad c _ { - k } = \frac { a _ { k } } { 2 } - \frac { b _ { k } } { 2 i } \qquad ( k \ge 1 )
$$

or, equivalently,

$$
a _ { k } = c _ { k } + c _ { - k } , \quad b _ { k } = i ( c _ { k } - c _ { - k } ) \quad \quad ( k \geq 1 ) .
$$

Note that if $f$ is real, then (B.4) implies that $a _ { k }$ and $b _ { k }$ are real. The coefficients $c _ { k }$ are generally complex, and (B.5) implies that they satisfy $c _ { - k } = \overline { { c } } _ { k }$ .

The degree n trigonometric projection of $f$ is the function

$$
f _ { n } ( t ) = \sum _ { k = - n } ^ { n } c _ { k } e ^ { i k t }
$$

or, equivalently,

$$
f _ { n } ( t ) = \sum _ { k = 0 } ^ { n } a _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { n } b _ { k } \sin ( k t ) .
$$

More generally, we say that a function of the form (B.7)–(B.8) is a trigonometric polynomial of degree $n$ , and we let $P _ { n }$ denote the $( 2 n + 1 )$ -dimensional vector space of all such polynomials. The trigonometric projection $f _ { n }$ is the least-squares approximant to $f$ in $P _ { n }$ , i.e., the unique best approximation to $f$ in the $L ^ { 2 }$ norm over $[ 0 , 2 \pi ]$ .

# B.3 Trigonometric interpolants, aliasing, and barycentric formulas

Mathematically, the simplest degree $n$ trigonometric approximation of a periodic function $f$ is its trigonometric projection (B.7)–(B.8). This approximation depends on the values of $f ( t )$ for all $t \in [ 0 , 2 \pi ]$ via (B.2) or (B.4). Computationally, a simpler approximation of $f$ is its degree $n$ trigonometric interpolant, which only depends on the values at certain interpolation points. In our basic configuration, we wish to interpolate $f$ in equispaced points by a function $p _ { n } \in P _ { n }$ . Since the dimension of $P _ { n }$ is $2 n + 1$ , there should be $2 n + 1$ interpolation points. We take these trigonometric points to be

$$
t _ { k } = { \frac { 2 \pi k } { N } } , \qquad 0 \leq k \leq N - 1 ,
$$

with $N = 2 n + 1$ . The trigonometric interpolation problem goes back at least to the young Gauss’s calculations of the orbit of the asteroid Ceres in 1801 [15].

It is known that there exists a unique interpolant $p _ { n } \in P _ { n }$ to any set of data values $f _ { k } = f ( t _ { k } )$ . Let us write $p _ { n }$ in the form

$$
p _ { n } ( t ) = \sum _ { k = - n } ^ { n } \tilde { c } _ { k } e ^ { i k t }
$$

or, equivalently,

$$
p _ { n } ( t ) = \sum _ { k = 0 } ^ { n } \widetilde { a } _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { n } \widetilde { b } _ { k } \sin ( k t )
$$

for some coefficients ${ \bar { c } } _ { - n } , \ldots , { \bar { c } } _ { n }$ or, equivalently, $\ddot { a } _ { 0 } , \dots , \ddot { a } _ { n }$ and $\ddot { b } _ { 1 } , \dotsc , \ddot { b } _ { n }$ . The coefficients $\bar { c } _ { k }$ and $c _ { k }$ are related by

$$
\tilde { c } _ { k } = \sum _ { j = - \infty } ^ { \infty } c _ { k + j N } \qquad ( | k | \le n )
$$

(the Poisson summation formula) and, similarly, $\begin{array} { r } { \tilde { a } _ { 0 } = \sum _ { j = 0 } ^ { \infty } a _ { j N } } \end{array}$ and $\tilde { a } _ { k } / \tilde { b } _ { k }$ and $a _ { k } / b _ { k }$ are related by

$$
\tilde { a } _ { k } = a _ { k } + \sum _ { j = 1 } ^ { \infty } ( a _ { k + j N } + a _ { - k + j N } ) , \quad \tilde { b } _ { k } = b _ { k } + \sum _ { j = 1 } ^ { \infty } ( b _ { k + j N } - b _ { - k + j N } )
$$

for $1 \leq k \leq n$ . We can derive these formulas by considering the phenomenon of aliasing. For all $j$ , the functions $\exp ( i [ k + j N ] t )$ take the same values at the trigonometric points (B.9). This implies that $f$ and the trigonometric polynomial (B.10) with coefficients defined by (B.12) take the same values at these points. In other words, (B.10) is the degree $n$ trigonometric interpolant to $f$ . A similar argument justifies (B.11)–(B.13).

Another interpretation of the coefficients $\tilde { c } _ { k } , \tilde { a } _ { k } , \tilde { b } _ { k }$ is that they are equal to the approximations to $c _ { k } , a _ { k } , b _ { k }$ one gets if the integrals (B.2) and (B.4) are approximated by the periodic trapezoidal quadrature rule with $N$ points [29]:

$$
\tilde { c } _ { k } = \frac { 1 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } e ^ { - i k t _ { j } } ,
$$

$$
\tilde { a } _ { k } = \frac { 2 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } \cos ( k t _ { j } ) , \quad \tilde { b } _ { k } = \frac { 2 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } \sin ( k t _ { j } ) \qquad ( k \ge 1 ) .
$$

To prove this, we note that the trapezoidal rule computes the same Fourier coefficients for $f$ as for $p _ { n }$ , since they take the same values at the grid points; but these must be equal to the true Fourier coefficients of $p _ { n }$ , since the $N = ( 2 n + 1 )$ -point trapezoidal rule is exactly correct for $e ^ { - 2 i n t } , \ldots , e ^ { 2 i n t }$ , hence for any trigonometric polynomial of degree $2 n$ , hence, in particular, for any trigonometric polynomial of degree $n$ times an exponential $\exp ( - i k t )$ with $| k | \le n$ . From (B.14)–(B.15) it is evident that the discrete Fourier coefficients $\bar { c } _ { k }$ , $\ddot { a } _ { k }$ , $\ddot { b } _ { k }$ can be computed by the Fast Fourier Transform (FFT), which, in fact, Gauss invented for this purpose.

Suppose one wishes to evaluate the interpolant $p _ { n } ( t )$ at certain points $t$ . One good algorithm is to compute the discrete Fourier coefficients and then apply them. Alternatively, another good approach is to perform interpolation directly by means of the barycentric formula for trigonometric interpolation, introduced by Salzer [26] and later simplified by Henrici [38]:

$$
p _ { n } ( t ) = \sum _ { k = 0 } ^ { N - 1 } ( - 1 ) ^ { k } f _ { k } \csc \left( \frac { t - t _ { k } } { 2 } \right) \bigg / \sum _ { k = 0 } ^ { N - 1 } ( - 1 ) ^ { k } \csc \left( \frac { t - t _ { k } } { 2 } \right) \quad ( N \ \mathrm { o d d } ) .
$$

(If $t$ happens to be exactly equal to a grid point $t _ { k }$ , one takes $p _ { n } ( t ) = f _ { k }$ .) The work involved in this formula is just $O ( N )$ operations per evaluation, and stability has been established (after a small modification) in [3]. In practice, we find the Fourier coefficients and barycentric formula methods equally effective.

In the above discussion, we have assumed that the number of interpolation points, $N$ , is odd. However, trigonometric interpolation, unlike trigonometric projection, makes sense for an even number of degrees of freedom too (see, e.g., [14, 19, 30]); it would be surprising if FFT codes refused to accept input vectors of even lengths! Suppose $n \geq 1$ is given and we wish to interpolate $f$ in $N = 2 n$ trigonometric points (B.9) rather than $N = 2 n + 1$ . This is one data value less than usual for a trigonometric polynomial of this degree, and we can lower the number of degrees of freedom in (B.10) by imposing the condition

$$
\widetilde c _ { - n } = \widetilde c _ { n }
$$

or, equivalently, in (B.11) by imposing the condition

$$
\tilde { b } _ { n } = 0 .
$$

This amounts to prescribing that the trigonometric interpolant through sawtoothed data of the form $f _ { k } = ( - 1 ) ^ { k }$ should be $\cos ( n t )$ rather than some other function such as $\exp ( i n t )$ —the only choice that ensures that real data will lead to a real interpolant. An equivalent prescription is that an arbitrary number $N$ of data values, even or odd, will be interpolated by a linear combination of the first $N$ terms of the sequence

$$
1 , \cos ( t ) , \sin ( t ) , \cos ( 2 t ) , \sin ( 2 t ) , \cos ( 3 t ) , \ldots .
$$

In this case of trigonometric interpolation with $N$ even, the formulas (B.9)– (B.15) still hold, except that (B.12) and (B.14) must be multiplied by $1 / 2$ for $k = \pm n$ . FFT codes, however, do not store the information that way. Instead, following (B.17), they compute ${ \ddot { c } } _ { - n }$ by (B.14) with $2 / N$ instead of $1 / N$ out front— thus effectively storing $\tilde { c } _ { - n } + \tilde { c } _ { n }$ in the place of ${ \ddot { c } } _ { - n }$ —and then apply (B.10) with the $k = n$ term omitted. This gives the right result for values of $t$ on the grid, but not at points in between.

Note that the conditions (B.17)–(B.19) are very much tied to the use of the sample points (B.9). If the grid were translated uniformly, then different relationships between $c _ { n }$ and $c _ { - n }$ or $a _ { n } / b _ { n }$ and $a _ { - n } / b _ { - n }$ would be appropriate in (B.17)–(B.18) and different basis functions in (B.19), and if the grid were not uniform, then it would be hard to justify any particular choices at all for even $N$ . For these reasons, even numbers of degrees of freedom make sense in equispaced interpolation but not in other trigonometric approximation contexts, in general. Henrici [38] provides a modification of the barycentric formula (B.16) for the equispaced case $N = 2 n$ .

# B.4 Approximation theory and quadrature

The basic question of approximation theory is, Will approximants to a function $f$ converge as the degree is increased, and how fast? The formulas of the last two sections enable us to derive theorems addressing this question for trigonometric projection and interpolation. (For finer points of trigonometric approximation theory, see [21].) The smoother $f$ is, the faster its Fourier coefficients decrease, and the faster the convergence of the approximants. (If $f$ were merely continuous rather than Lipschitz continuous, then the trigonometric version of the Weierstrass approximation theorem [18, Section I.2] would ensure that it could be approximated arbitrarily closely by trigonometric polynomials, but not necessarily by projection or interpolation.)

Our first theorem asserts that Fourier coefficients decay algebraically if $f$ has a finite number of derivatives, and geometrically if $f$ is analytic. Here and in Theorem B.2 below, we make use of the notion of the total variation, $V$ , of a periodic function $\varphi$ defined on $[ 0 , 2 \pi ]$ , which is defined in the usual way as the supremum of all sums $\textstyle \sum _ { i = 1 } ^ { n } | \varphi ( x _ { i } ) - \varphi ( x _ { i - 1 } ) |$ , where $\{ x _ { i } \}$ are ordered points in $[ 0 , 2 \pi ]$ with $x _ { 0 } = x _ { n }$ ; $V$ is equal to the the 1-norm of $f ^ { \prime }$ , interpreted if necessary as a Riemann–Stieltjes integral [18, Section I.4]. Thus $| \sin ( t ) |$ on $[ 0 , 2 \pi ]$ , for example, corresponds to $\nu = 1$ , and $| \sin ( t ) | ^ { 3 }$ to $\nu = 3$ . All our theorems continue to assume that $f$ is $2 \pi$ -periodic.

Theorem B.1. If $f$ is $\nu \geq 0$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then

$$
| c _ { k } | \leq { \frac { V } { 2 \pi | k | ^ { \nu + 1 } } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, then

$$
| c _ { k } | \leq M e ^ { - \alpha | k | } .
$$

Proof. The bound (B.20) can be derived by integrating (B.2) by parts $\nu + 1$ times. Equation (B.21) can be derived by shifting the interval of integration $[ 0 , 2 \pi ]$ of (B.2) downward in the complex plane for $k > 0$ , or upward for $k < 0$ , by a distance arbitrarily close to $\alpha$ ; see [29, Section 3].

To apply Theorem B.1 to trigonometric approximations, we note that the error in the degree $n$ trigonometric projection (B.7) is

$$
f ( t ) - f _ { n } ( t ) = \sum _ { | k | > n } c _ { k } e ^ { i k t } ,
$$

a series that converges absolutely and uniformly by the Lipschitz continuity assumption on $f$ . Similarly, (B.12) implies that the error in trigonometric interpolation is

$$
f ( t ) - p _ { n } ( t ) = \sum _ { | k | > n } c _ { k } ( e ^ { i k t } - e ^ { i k ^ { \prime } t } ) ,
$$

where $k ^ { \prime } = \mathrm { m o d } ( k + n , 2 n + 1 ) - n$ is the index that $k$ gets aliased to on the $( 2 n + 1 )$ -point grid, i.e., the integer of absolute value $\leq n$ congruent to $k$ modulo $2 n + 1$ . These formulas give us bounds on the error in trigonometric projection and interpolation.

Theorem B.2. If $f$ is $\nu \geq 1$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then its degree $n$ trigonometric projection and interpolant satisfy

$$
\| f - f _ { n } \| _ { \infty } \leq { \frac { V } { \pi \nu n ^ { \nu } } } , \qquad \| f - p _ { n } \| _ { \infty } \leq { \frac { 2 V } { \pi \nu n ^ { \nu } } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, they satisfy

$$
\| f - f _ { n } \| _ { \infty } \leq \frac { 2 M e ^ { - \alpha n } } { e ^ { \alpha } - 1 } , \qquad \| f - p _ { n } \| _ { \infty } \leq \frac { 4 M e ^ { - \alpha n } } { e ^ { \alpha } - 1 } .
$$

Proof. The estimates (B.24) follow by bounding the tails (B.22) and (B.23) with (B.20), and (B.25) likewise by bounding them with (B.21).

A slight variant of this argument gives an estimate for quadrature. If $I$ denotes the integral of a function $f$ over $[ 0 , 2 \pi ]$ and $I _ { N }$ its approximation by the $N$ -point periodic trapezoidal rule, then from (B.2) and (B.14), we have $I = 2 \pi c _ { 0 }$ and $I _ { N } =$ $2 \pi \tilde { c } _ { 0 }$ . By (B.12) this implies

$$
I _ { N } - I = 2 \pi \sum _ { j \neq 0 } c _ { j N } ,
$$

which gives the following result.

Theorem B.3. If $f$ is $\nu \geq 1$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then the $N$ -point periodic trapezoidal rule approximation to its integral over $[ 0 , 2 \pi ]$ satisfies

$$
| I _ { N } - I | \leq \frac { 4 V } { N ^ { \nu + 1 } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, it satisfies

$$
| I _ { N } - I | \leq \frac { 4 \pi M } { e ^ { \alpha N } - 1 } .
$$

Proof. These results follow by bounding (B.26) with (B.20) and (B.21) as in the proof of Theorem B.2. From (B.20), the bound one gets is $2 V \zeta ( \nu + 1 ) / N ^ { \nu + 1 }$ , where $\zeta$ is the Riemann zeta function, which we have simplified by the inequality $\zeta ( \nu + 1 ) \leq \zeta ( 2 ) < 2$ for $\nu \geq 1$ . The estimate (B.28) originates with Davis [17]; see also [19, 29].

Finally, in a section labeled “approximation theory” we must mention another famous candidate for periodic function approximation: best approximation in the $\infty$ -norm. Here the trigonometric version of the Chebyshev alternation theorem holds, assuming $f$ is real. This result is illustrated later in Figure B.11.

Theorem B.4. Let $f$ be real and continuous on the periodic interval $[ 0 , 2 \pi ]$ . For each $n \geq 0$ , $f$ has a unique best approximant $p _ { n } ^ { * } \in \boldsymbol { P } _ { n }$ with respect to the norm $\| \cdot \| _ { \infty }$ , and $\boldsymbol { p } _ { n } ^ { * }$ is characterized by the property that the error curve $( f - p _ { n } ^ { * } ) ( t )$ equioscillates on $[ 0 , 2 \pi )$ between at least $2 n + 2$ equal extrema $\pm \| f - p _ { n } ^ { * } \| _ { \infty }$ of alternating signs.

Proof. See [21, Section 5.2] for a proof.

# B.5 Trigfun computations

Building on the mathematics of the past three sections, Chebfun was extended in 2014 to incorporate trigonometric representations of periodic functions alongside its traditional Chebyshev representations. (Here and in the remainder of the paper, we assume the reader is familiar with Chebfun.) Our convention is that a trigfun is a representation via coefficients $c _ { k }$ as in (B.7) of a sufficiently smooth periodic function $f$ on an interval by a trigonometric polynomial of adaptively determined degree, the aim always being accuracy of 15 or 16 digits relative to the $\infty$ -norm of the function on the interval. This follows the same pattern as traditional Chebyshevbased chebfuns, which are representations of nonperiodic functions by polynomials, and a trigfun is not a distinct object from a chebfun but a particular type of chebfun. The default interval, as with ordinary chebfuns, is $[ - 1 , 1 ]$ , and other intervals are handled by the obvious linear transplantation.17

For example, here we construct and plot a trigfun for $\cos ( t ) + \sin ( 3 t ) / 2$ on $[ 0 , 2 \pi ]$ :

The plot appears in Figure B.1, and the following text output is produced, with the flag trig signaling the periodic representation.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/2edb0421aeed0cb35fec4b75249de3dd62ed45cd325e542f313647aa5c6af9fd.jpg)  
Figure B.1: The trigfun representing $f ( t ) = \cos ( t ) + \sin ( 3 t ) / 2$ on $[ 0 , 2 \pi ]$ . One can evaluate $f$ with $\pm \left( \ t \right)$ , compute its definite integral with sum(f) or its maximum with max(f), find its roots with roots(f), and so on.

f = chebfun column (1 smooth piece) interval length endpoint values trig   
[ 0, 6.3] 7 1 1

We see that Chebfun has determined that this function $f$ is of length $N = 7$ . This means that there are 7 degrees of freedom, i.e., $f$ is a trigonometric polynomial of degree $n = 3$ , whose coefficients we can extract with $\begin{array} { r l } { \mathtt { C } } & { { } = } \end{array}$ trigcoeffs(f), or in cosine/sine form with $[ { \mathsf { a } } , { \mathsf { b } } ] =$ trigcoeffs(f).

Note that the Chebfun constructor does not analyze its input symbolically but just evaluates the function at trigonometric points (B.9), and from this information the degree and the values of the coefficients are determined. The constructor also detects when a function is real. A trigfun constructed in the ordinary manner is always of odd length $N$ , corresponding to a trigonometric polynomial of degree $n = ( N - 1 ) / 2$ , though it is possible to make even-length trigfuns by explicitly specifying $N$ .

To construct a trigfun, Chebfun samples the function on grids of size $1 6 , 3 2 , 6 4 , \ldots$ and tests the resulting discrete Fourier coefficients for convergence down to relative machine precision. (Powers of 2 are used since these are particularly efficient for the FFT, even though the result will ultimately be trimmed to an odd number of points. As with nontrigonometric Chebfun, the engineering details are complicated and under ongoing development.) When convergence is achieved, the series is chopped at an appropriate point and the degree reduced accordingly.

Once a trigfun has been created, computations can be carried out in the usual Chebfun fashion via overloads of familiar MATLAB commands. For example,

>> sum(f^2) ans = 3.926990816987241

This number is computed by integrating the trigonometric representation of $f ^ { 2 }$ , i.e., by returning the number $2 \pi c _ { 0 }$ corresponding to the trapezoidal rule applied to $f ^ { 2 }$ as described around Theorem B.3. The default 2-norm is the square root of this result,

>> norm(f) ans = 1.981663648803005

Derivatives of functions are computed by the overloaded command diff. (In the unusual case where a trigfun has been constructed of even length, differentiation will increase its length by 1.) The zeros of $f$ are found with roots,

>> roots(f)   
ans = 1.263651122898791 4.405243776488583

and Chebfun determines maxima and minima by first computing the derivative, then checking all of its roots:

>> max(f) ans = 1.389383416980387

Concerning the algorithm used for periodic rootfinding, one approach would be to solve a companion matrix eigenvalue problem, and $O ( n ^ { 2 } )$ algorithms for this task have recently been developed [1]. When development of these methods settles down, they may be incorporated in Chebfun. For the moment, trigfun rootfinding is done by first converting the problem to nonperiodic Chebfun form using the standard Chebfun constructor, whereupon we take advantage of Chebfun’s $O ( n ^ { 2 } )$ recursive interval subdivision strategy [6]. This shifting to subintervals for rootfinding is an example of an operation that breaks periodicity as mentioned in item 7 of the introduction.

The main purpose of the periodic part of Chebfun is to enable machine precision computation with periodic functions that are not exactly trigonometric polynomials. For example, $\exp ( \sin t )$ on $[ 0 , 2 \pi ]$ is represented by a trigfun of length 27, i.e., a trigonometric polynomial of degree 13:

$$
\begin{array} { r l } & { \mathrm { ~ g ~ = ~ c h e b f u n } { ( \mathrm {  ~ \cdot ~ } \exp ( \mathrm { s i n } ( \mathrm { t } ) ) \mathrm {  ~ \cdot ~ } , ~ \mathrm { ~ } [ 0 ~ 2 * \mathrm { p i } ] ~ , ~ \mathrm {  ~ \cdot ~ } \mathrm { t r i g } ^ { \mathrm {  ~ \cdot ~ } } ) } } \\ & { \mathrm { ~ g ~ = ~ } } \\ & { \quad \mathrm { ~ c h e b f u n ~ c o l u m n ~ \Lambda ~ ( 1 ~ \ s m o o t h ~ \ p i e c e ) ~ } } \\ & { \quad \quad \quad \quad \mathrm { i n t e r v a l ~ } \quad \quad \quad \mathrm { l e n g t h } \quad \quad \quad \mathrm { e n d p o i n t ~ \ v a l u e s ~ \ t r i g } } \\ & { \mathrm { ~ [ ~ } \quad \quad 0 , \quad \quad \quad 6 . 3 \mathrm { ] } \quad \quad 2 7 \quad \quad \quad 1 } \end{array}
$$

The coefficients can be plotted on a log scale with the command plotcoeffs(f), and Figure B.2 reveals the faster-than-geometric decay of an entire function.

Figure B.3 shows trigfuns and coefficient plots for $f ( t ) = \operatorname { t a n h } ( 5 \cos ( 5 t ) )$ and $g ( t ) = \exp ( - 1 / \operatorname* { m a x } \{ 0 , 1 - t ^ { 2 } / 4 \} )$ on $[ - \pi , \pi ]$ . The latter is $C ^ { \infty }$ but not analytic. Figure B.4 shows a further pair of examples that we call an “AM signal” and an “FM signal.” These are among the preloaded functions available with cheb.gallerytrig, Chebfun’s trigonometric analogue of the MATLAB gallery command.

Computation with trigfuns, as with nonperiodic chebfuns, is carried out by a continuous analogue of floating point arithmetic [27]. To illustrate the “rounding” process involved, the degrees of the trigfuns above are 555 and 509, respectively. Mathematically, their product is of degree 1064. Numerically, however, Chebfun achieves 16-digit accuracy with degree 556.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/78599dc4b0da7ac0e6e0cf1af144dc909d16f33b3aa04fcd15add5ffb367a116.jpg)  
Figure B.2: Absolute values of the Fourier coefficients of the trigfun for $\exp ( \sin t )$ on $[ 0 , 2 \pi ]$ . This is an entire function (analytic throughout the complex $t$ -plane), and in accordance with Theorem B.1, the coefficients decrease faster than geometrically.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6a92bdc582656533fb1f8420b436a60477d4bb01b47a97f6c6cd1ca66dbff1f9.jpg)  
Figure B.3: Trigfuns of $\operatorname { t a n h } ( 5 \sin t )$ and $\exp ( - 1 0 0 ( t + . 3 ) ^ { 2 } )$ (upper row) and corresponding absolute values of Fourier coefficients (lower row).


<!-- chunk 0005: pages 281-350 -->
![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/9e97c24efa4c9cea2b8cb0df0ca54398aec8937acafb0793be69229914ab9cd9.jpg)  
Figure B.4: Trigfuns of the “AM signal” $\cos ( 5 0 t ) ( 1 + \cos ( 5 t ) / 5 )$ and of the “FM signal” $\cos ( 5 0 t + 4 \sin ( 5 t ) )$ (upper row) and corresponding absolute values of Fourier coefficients (lower row).

Here is a more complicated example of Chebfun rounding adapted from [27], where it is computed with nonperiodic representations:

$$
\begin{array} { r l } & { \mathbf { f _ { \lambda } } = \mathbf { \lambda } \mathrm { c h e b f u n } \left( \mathbb { Q } \left( \mathrm { t } \right) \ \mathrm { s i n } \left( \mathrm { p i } \ast \mathrm { t } \right) , \ \mathrm { \Lambda } ^ { \prime } \mathrm { t r i g } ^ { \prime } \right) } \\ & { \mathbf { s _ { \lambda } } = \mathbf { f _ { \lambda } } } \\ & { \mathbf { f o r } \ \mathbf { j _ { \lambda } } = \ 1 : 1 5 } \\ & { \mathbf { f _ { \lambda } } = \mathbf { \lambda } \left( 3 / 4 \right) \ast \left( 1 \ - \ 2 \ast \mathbf { f } ^ { \sim } 4 \right) , \ \mathbf { s _ { \lambda } } = \mathbf { \lambda } \mathbf { s _ { \lambda } } + \mathbf { \lambda } \mathbf { f _ { \lambda } } } \end{array}
$$

This program takes 15 steps of an iteration that in principle quadruples the degree at each step, giving a function $s$ at the end of degree $4 ^ { 1 5 } \ = \ 1$ ,073,741,824. In actuality, however, because of the rounding to 16 digits, the degree comes out one million times smaller as 1148. This function is plotted in Figure B.5. Following [27], we can compute the roots of $s - 8$ in half a second on a desktop machine:

>> roots(s-8)   
ans = -0.992932107411876 -0.816249934290177 -0.798886729723433 -0.201113270276572 -0.183750065709828 -0.007067892588112 0.346696120418255

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/468074f4004a911d43929a64de9a7c80bba191ec499f2330fc09ace0c0d5ae2a.jpg)  
Figure B.5: After 15 steps of an iteration, this periodic function has degree 1148 in its Chebfun representation rather than the mathematically exact figure 1,073,741,824.

0.401617073482111   
0.442269489632475   
0.557730510367530   
0.598382926517899   
0.653303879581760

The integral with sum(s) is 15.265483825826763, correct except in the last two digits.

If one tries to construct a trigfun by sampling a function that is not smoothly periodic, Chebfun will by default go up to length $2 ^ { 1 6 }$ and then issue a warning:

>> h = chebfun('exp(t)', [0 2\*pi], 'trig') Warning: Function not resolved using 65536 pts. Have you tried a non-trig representation?

On the other hand, computations that are known to break periodicity or smoothness will result in the representation being automatically cast from a trigfun to a chebfun. For example, here we define $g$ to be the absolute value of the function $f ( t ) =$ $\cos ( t ) + \sin ( 3 t ) / 2$ of Figure B.1. The system detects that $f$ has zeros, implying that $g$ will probably not be smooth, and accordingly constructs it not as a trigfun but as an ordinary chebfun with several pieces (Figure B.6):

>> f = chebfun('cos(t) + sin(3\*t)/2', [0 2\*pi], 'trig'), g = abs(f)   
g = chebfun column (3 smooth pieces) interval length endpoint values   
[ 0, 1.3] 17 1 3.8e-16   
[ 1.3, 4.4] 25 1.8e-15 7.3e-16   
[ 4.4, 6.3] 20 -6.6e-18 1   
Total length $\ c = ~ 6 2$ .

Similarly, if you add or multiply a trigfun and a chebfun, the result is a chebfun.

# B.6 Applications

Analysis of periodic functions and signals is one of the oldest topics of mathematics and engineering. Here we give six examples of how a system for automating such computations may be useful.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/1bd4928b83686d7df43439a7011057889ef08d727a819478e81b816b270a6333.jpg)  
Figure B.6: When the absolute value of the trigfun $f$ of Figure B.1 is computed, the result is a nonperiodic chebfun with three smooth pieces.

Complex contour integrals. Smooth periodic integrals arise ubiquitously in complex analysis. For example, suppose we wish to determine the number of zeros of $f ( z ) = \cos ( z ) - z$ in the complex unit disk. The answer is given by

$$
m = { \frac { 1 } { 2 \pi i } } \int { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = { \frac { 1 } { 2 \pi i } } \int { \frac { 1 } { f ( z ) } } { \frac { d f } { d t } } d t
$$

if $z = \exp ( i t )$ with $t \in [ 0 , 2 \pi ]$ . With periodic Chebfun, we can compute $m$ by

$$
\begin{array} { r l } & { \mathrm { \gamma > ~ z ~ = ~ c h e b f u n ( ~ ' \exp ( 1 i * t ) ~ ' , ~ [ 0 ~ 2 * p i ] ~ , ~ ' t r i g ' ) } ; } \\ & { \mathrm { \gamma > ~ f ~ = ~ c o s ( z ) ~ - ~ z ; } } \\ & { \mathrm { \gamma > ~ m ~ = ~ \mathrm { r e a l } ( s u m ( d i f f ( f ) / f ) / ( 2 i * p i ) ) } } \\ & { \mathrm { \gamma ~ m ~ = ~ 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } } \end{array}
$$

Changing the integrand from $f ^ { \prime } ( z ) / f ( z )$ to $z f ^ { \prime } ( z ) / f ( z )$ gives the location of the zero, correct to all digits displayed:

>> z0 = real(sum(z\*diff(f)/f)/(2i\*pi)) z0 = 0.739085133215161

(The real commands are included to remove imaginary rounding errors.) For wide-ranging extensions of calculations like these, including applications to matrix eigenvalue problems, see [2].

Linear algebra. Chebfun does not work from explicit formulas: to construct a function, it is only necessary to be able to evaluate it. This is an extremely useful feature for linear algebra calculations. For example, the matrix

$$
A = \frac { 1 } { 3 }
$$

has all its eigenvalues in the unit disk. A question with the flavor of control and stability theory is, What is the maximum resolvent norm $\lVert ( z I - A ) ^ { - 1 } \rVert$ for $z$ on the unit circle? We can calculate the answer with the code below, which constructs a periodic chebfun of degree $n = 5 6 9$ . The maximum is 27.68851, attained with $z = \exp ( 0 . 4 5 4 5 9 6 i )$ (Figure B.7).

$$
\begin{array} { r l } & { \mathrm { ~ \tt ~ A ~ = ~ [ 2 ~ - 2 i ~ 1 ~ 1 ~ 1 ; ~ 2 i ~ - 2 ~ 0 ~ 2 ; ~ - 2 ~ 0 ~ 1 ~ 2 ; ~ 0 ~ 1 { \tt } ~ 1 ~ 0 ~ 2 ] / 3 , ~ { \tt ~ I } ~ = ~ { \tt } e y e ( 4 ) } } \\ & { \mathrm { ~ \tt ~ f ~ f ~ = ~ { \tt ~ Q } ( t ) ~ \tt ~ 1 / m i n ( \ s v d ( e x p ( 1 1 * t ) * I - A ) ) } } \\ & { \mathrm { ~ \tt ~ f ~ = ~ \ c h e b f u n ( f f , ~ [ 0 ~ 2 * p i ] , ~ \theta ' { \tt ~ t r i g } ' , ~ \theta ' v e c t o r i z e ' ) } } \\ & { \mathrm { ~ [ m a x v a l , m a x p o s ] ~ \theta = \ m a x ( f ) ~ \theta ~ } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/263f3666c3798528417cf37c2000cb4bbe4c7506c31266b45dbb6336556487e4.jpg)  
Figure B.7: Resolvent norm $\| ( z I - A ) ^ { - 1 } \|$ for a $4 \times 4$ matrix $A$ with $z = e ^ { i t }$ on the unit circle.

Circular convolution and smoothing. The circular or periodic convolution of two functions $f$ and $g$ with period $T$ is defined by

$$
( f * g ) ( t ) : = \int _ { t _ { 0 } } ^ { t _ { 0 } + T } g ( s ) f ( t - s ) d s ,
$$

where $t _ { 0 }$ is aribtrary. Circular convolutions can be computed for trigfuns with the circconv function, whose algorithm consists of coefficientwise multiplication in Fourier space. For example, here is a trigonometric interpolant through 201 samples of a smooth function plus noise, shown in the upper-left panel of Figure B.8.

N = 201, tt = trigpts(N, [-pi pi]) ff = exp(sin(tt)) + 0.05\*randn(N,1) f = chebfun(ff, [-pi pi], 'trig')

The high wave numbers can be smoothed by convolving $f$ with a mollifier. Here we use a Gaussian of standard deviation $\sigma = 0 . 1$ (numerically periodic for $\sigma \leq 0 . 3 5$ ). The result is shown in the upper-right panel of the figure.

$$
\begin{array} { r l } & { \mathrm { g a u s s i a n ~ \ b = ~ \ b \emptyset ( \mathbf { t } , \mathbf { s i g m a } ) ~ \ b 1 / ( \mathbf { s i g m a * s q r t } ( \ b 2 * \mathbf { p i } ) ) * \mathbf { e x p } ( \ b - \ b 0 . 5 * ( \mathbf { t } / \mathbf { s i g m a } ) \cdot \ b \cdot \ b \cdot 2 ) } } \\ & { \mathrm { g ~ \ b = ~ \ b \emptyset ( \mathbf { s i g m a } ) ~ \ c h e b f u n ( \ b \emptyset ( \mathbf { t } ) ~ \mathbf { g a u s s i a n } ( \mathbf { t } , \mathbf { s i g m a } ) , ~ \{ \ b \cdot \_ p i ~ \mathbf \} ] ~ \ b , ~ \cdot \_ \mathbf { t r i g } \cdot ) ~ } } \\ & { \mathrm { h ~ \ b = ~ \ b c i r c c o n v ( \mathbf { f } , ~ \mathbf { g } ( \ b 0 . 1 ) ) ~ } } \end{array}
$$

Fourier coefficients of nonsmooth functions. A function $f$ that is not smoothly periodic will at best have a very slowly converging trigonometric series, but still, one may be interested in its Fourier coefficients. These can be computed by applying trigcoeffs to a chebfun representation of $f$ and specifying how many coefficients are required; the integrals (B.2) are then evaluated numerically by Chebfun’s standard method of Clenshaw–Curtis quadrature. For example, Figure B.9 shows a portrayal of the Gibbs phenomenon from Runge’s 1904 book together with its Chebfun equivalent computed in a few seconds with the commands

$$
\begin{array} { l } { { \mathrm {  ~ \ l ~ \ l ~ \bar { \ t } ~ \ l u ~ \bar { \ t } ~ u n ( \bar { \ t } ~ t ) ~ , ~ \bar { \ t } - p i ~ p i ] ~ , ~ \bar { \ t } ~ = ~ ( \bar { \ a b s } ( \bar { t } ) ~ \bar { \ } ~ \bar { \ t } ~ \mathrm {  ~ \ p i / } 2 ) } } } \\ { { \mathrm { \ o r ~ \mit \ N ~ = ~ 2 * \big [ ~ 1 ~ 3 ~ 5 ~ 7 ~ 2 1 ~ 7 9 \big ] ~ \bar { \ t } ~ 1 } } } \\ { { \mathrm {  ~ \ l ~ \bar { \ t } ~ \ l s o ~ \bar { \ t } { \mit \ c o e f f s } ( \bar { \sf \Phi } ( f , \bar { \ t } ) ~ \ l ) ~ } } } \\ { { \mathrm {  ~ \ f ~ \ l ~ \bar { \ t } ~ \ l e ~ \ b e b f u n ( c , \bar { \ t } ~ \bar { \ t } - p i ~ \bar { \ t } ] ~ , ~ \bar { \ t } ~ \mathrm { c o e f f s ^ { \prime } ~ , ~ \bar { \ t } r i g ^ { \prime } ) } } } } \\ { { \mathrm {  ~ \ p l o t ~ \ \bar { \ t } ~ \ i n t e r v a l ~ \bar { \ } ~ , ~ \bar { \ t } ~ \ l o ~ 4 * \ p i \big ] ~ } } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/65ac9ac4788532cc9248c8f85e8187915a990c3313f0c7a513532956c7cee921.jpg)  
Figure B.8: Circular convolution of a noisy function with a smooth mollifier.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ba29bcb64c1a21ac510e18069bfb8f10b5587ea7ec04aef9c25dd39d34c2b9b9.jpg)  
Figure B.9: On the left, a figure from Runge’s 1904 book Theorie und Praxis der Reihen [25]. On the right, the equivalent computed with periodic Chebfun. Among other things, this figure illustrates that a trigfun can be accurately evaluated outside its interval of definition.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/e232bbdf411f89c5d4b335957ee6abbe78ff8c6bb0f67f76d494a5c0a9c716d8.jpg)  
Figure B.10: Trigonometric interpolation of $| t |$ in unequally spaced points with the generalized barycentric formula implemented in chebfun/interp1.

Interpolation in unequally spaced points. Very little attention has been given to trigonometric interpolation in unequally spaced points, but the barycentric formula (B.16) for odd $N$ and Henrici’s generalization for even $N$ have been generalized to this case by Berrut [5]. Chebfun makes these formulas available through the command chebfun.interp1, just as has long been true for interpolation by algebraic polynomials. For example, the code

interpolates the function $| t |$ on $[ - \pi , \pi ]$ in the 9 points indicated by a trigonometric polynomial of degree $n = 4$ . The interpolant is shown in Figure B.10 together with the analogous curve for equispaced points.

Best approximation, Carath´eodory–Fej´er approximation, and rational functions. Chebfun has long had a dual role: it is a tool for computing with functions and also a tool for exploring principles of approximation theory, including advanced ones. The trigonometric side of Chebfun extends this second aspect to periodic problems. For example, Chebfun’s new trigremez command can compute best approximants with equioscillating error curves as described in Theorem B.3 [17]. Here is an example that generates the error curve displayed in Figure B.11, with error 12.1095909:

$$
\begin{array} { l } { \mathbf { f } ~ = ~ \mathrm { c h e b f u n } ( ^ { \prime } 1 / ( 1 . 0 1 \mathrm { - } \mathrm { s i n } ( \mathrm { t - } 2 ) ) ^ { \prime } , ~ [ 0 ~ 2 \mathrm { * p i } ] , ~ ^ { \prime } \mathrm { t r i g } ^ { \prime } ) } \\ { \mathbf { p } ~ = ~ \mathrm { t r i g r e m e z } ( \mathbf { f } , 1 0 ) , ~ \mathbf { p } \mathbf { l o t } ( \mathbf { f } - \mathbf { p } ) } \end{array}
$$

Chebfun is also acquiring other capabilities for trigonometric polynomial and rational approximation, including Carath´eodory–Fej´er near-best approximation via singular values of Hankel matrices, and these will be described elsewhere.

# B.7 Periodic ODEs, operator exponentials, and eigenvalue problems

A major capability of Chebfun is the solution of linear and nonlinear ODEs, as well as integral equations, by applying the backslash command to a “chebop” object. We have extended these capabilities to periodic problems, both scalars and systems. See [13] for the theory of existence and uniqueness of solutions to periodic ODEs, which goes back to Floquet in the 1880s, a key point being the avoidance of nongeneric configurations corresponding to eigenmodes.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/342345daaa48bc6dc3cdac2419f11f37bfddbd1ec780ceaa30645f34f4fae0cd.jpg)  
Figure B.11: Error curve in degree $n = 1 0$ best trigonometric approximation to $f ( t ) =$ $1 / ( 1 . 0 1 - \sin ( t - 2 ) )$ over $[ 0 , 2 \pi ]$ . The curve equioscillates between $2 n + 2 = 2 2$ alternating extrema.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/2e553a1bc621c1f29fdfddae4afeaad59a1d660045144020b4ff3fb88a49d8d0.jpg)  
Figure B.12: Solution of the linear periodic ODE (B.32) as a trigfun of degree 168, computed by an automatic Fourier spectral method.

Chebfun’s algorithm for linear ODEs amounts to an automatic spectral collocation method wrapped up so that the user need not be aware of the discretization. With standard Chebfun, these are Chebyshev spectral methods, and now with the periodic extension, they are Fourier spectral methods [9]. The problem is solved on grids of size 32, 64, and so on until the system judges that the Fourier coefficients have converged down to the level of noise, and the series is then truncated at an appropriate point.

For example, consider the problem

$$
0 . 0 0 1 ( u ^ { \prime \prime } + u ^ { \prime } ) - \cos ( t ) u = 1 , \qquad 0 \leq t \leq 6 \pi ,
$$

with periodic boundary conditions. The following Chebfun code produces the solution plotted in Figure B.12 in half a second on a laptop. Note that the trigonometric discretizations are invoked by the flag L.bc $=$ 'periodic':

$$
\begin{array} { l } { \mathrm { L ~ = ~ c h e b o p } ( 0 , 6 * \mathrm { p i } ) } \\ { \mathrm { L . o p ~ = ~ \Theta ^ { } ( x , u ) ~ 0 . 0 0 1 * d i f f ( u , 2 ) ~ + ~ 0 . 0 0 1 * d i f f ( u ) ~ - ~ \cos { ( x ) * u } ~ } } \\ { \mathrm { L . b c ~ = ~ \Omega ^ { * } ~ p e r i o d i c ^ { * } } } \\ { \mathrm { u ~ = ~ L \backslash { 1 } } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ad106ca66e2e4a4b0f5f9566a84a8d31b711a4d121ff59230565704c454fd76b.jpg)  
Figure B.13: Solution of the nonlinear periodic ODE (B.33) computed by iterating the Fourier spectral method within a continuous form of Newton iteration. Executing max(diff(u)) shows that the maximum of $u ^ { \prime }$ is 32.094.

This trigfun is of degree 168, and the residual reported by norm(L\*u-1) is $1 \times 1 0 ^ { - 1 2 }$ As always, $u$ is a chebfun; its maximum, for example, is $\mathtt { m a x } ( \mathtt { u } ) = 6 6 . 9 2 8$ .

For periodic nonlinear ODEs, Chebfun applies trigonometric analogues of the algorithms developed by Driscoll and Birkisson in the Chebyshev case [7, 8]. The whole solution is carried out by a Newton or damped Newton iteration formulated in a continuous mode (“solve then discretize” rather than “discretize then solve”), with Jacobian matrices replaced by Fr´echet derivative operators implemented by means of automatic differentiation and automatic spectral discretization. For example, suppose we seek a solution of the nonlinear problem

$$
0 . 0 0 4 u ^ { \prime \prime } + u u ^ { \prime } - u = \cos ( 2 \pi t ) , \qquad t \in [ - 1 , 1 ] ,
$$

with periodic boundary conditions. After seven Newton steps, the Chebfun commands below produce the result shown in Figure B.13, of degree $n = 3 6 2$ , and the residual norm norm(N(u)-rhs,'inf') is reported as $8 \times 1 0 ^ { - 9 }$ :

$$
\begin{array} { l } { { \mathrm { ~ N ~ = ~ c h e b o p ( - 1 , 1 ) ~ } } } \\ { { \mathrm { ~ N . o p ~ = ~ \mathbb { Q } ( x , u ) ~ \Lambda . ~ 0 0 4 * d i f f \left( u , 2 \right) ~ + ~ u * d i f f \left( u \right) ~ - ~ u } } } \\ { { \mathrm { ~ N . b c ~ = ~ \Lambda ^ \ast { p e r i o d i c } ^ { \ast } ~ } } } \\ { { \mathrm { ~ r h s ~ = ~ c h e b f u n ( \Lambda ^ \ast \cos { ( 2 * p i * t ) } ~ \Lambda ^ \ast { t r i g } ^ { \ast } ) ~ } } } \\ { { \mathrm { ~ u ~ = ~ \mathbb { N } \backslash r h s ~ } } } \end{array}
$$

Chebfun’s overload of the MATLAB eigs command solves linear ODE eigenvalue problems by, once again, automated spectral collocation discretizations [11]. This too has been extended to periodic problems, with Fourier discretizations replacing Chebyshev. For example, a famous periodic eigenvalue problem is the Mathieu equation

$$
- u ^ { \prime \prime } + 2 q \cos ( 2 t ) u = \lambda u , \qquad t \in [ 0 , 2 \pi ] ,
$$

where $q$ is a parameter. The commands below give the plot shown in Figure B.14:

$$
\begin{array} { l } { { \mathrm {  ~ q ~ = ~ 2 ~ \mit } } } \\ { { \mathrm {  ~ L ~ \mit = ~ \ c h e b o p { ( \mathfrak { O } ( x , u ) ~ \mathrm {  ~ \bar { \ c } d i f f ( u , 2 ) } + 2 \ast q \ast c o s ( 2 \ast x ) \ast u , ~ [ 0 ~ 2 \ast p i ] ~ , ~ \mathrm {  ~ \bar { \ p e r i o d i c } } } } } } \end{array}
$$

So far as we know, Chebfun is the only system offering such convenient solution of ODEs and related problems, now in the periodic as well as the nonperiodic case.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ee806050cd09a3647916dd824f938ce6cfc21503be16a5704e5985031e3b4ff8.jpg)  
Figure B.14: First five eigenfunctions of the Mathieu equation (B.34) with $q = 2$ , computed with eigs.

We have also implemented a periodic analogue of Chebfun’s expm command for computing exponentials of linear operators, which we omit from discussion here for reasons of space. All the capabilities mentioned in this section can be explored with Chebgui, the graphical user interface written by Birkisson, which now invokes trigonometric spectral discretizations when periodic boundary conditions are specified.

# B.8 Discussion

Chebfun is an open-source project written in MATLAB and hosted on GitHub; details and the user’s guide can be found at www.chebfun.org [12]. About 30 people have contributed to its development over the years and, at present, there are about 10 developers based mainly at the University of Oxford. During 2013–2014 the code was redesigned and rewritten as version 5 (first released June 2014) in the form of about 100,000 lines of code realizing about 40 classes. The aim of this redesign was to enhance Chebfun’s modularity, clarity, and extensibility, and the introduction of periodic capabilities, which had not been planned in advance, was the first big test of this extensibility. We were pleased to find that the modifications proceeded smoothly. The central new feature is a new class @trigtech in parallel to the existing @chebtech1 and @chebtech2, which work with polynomial interpolants in first- and second-kind Chebyshev points, respectively.

About half the classes of Chebfun are concerned with representing functions, and the remainder are mostly concerned with ODE discretization and automatic differentiation for solution of nonlinear problems, whether scalar or systems, possibly with nontrivial block structure. The incorporation of periodic problems into this second, more advanced part of Chebfun was achieved by introducing a new class @trigcolloc matching @chebcolloc1 and @chebcolloc2.

About a dozen software projects in various computer languages have been modeled on Chebfun, and a partial list can be found at www.chebfun.org. One of these, Fourfun, is a MATLAB system for periodic functions developed independently of the present work by K. McLeod [20], a student of former Chebfun developer R. Platte. Another that also has periodic and differential equations capabilities is ApproxFun, written in Julia by S. Olver and former Chebfun developer A. Townsend [22].18 We think the enterprise of numerical computing with functions is here to stay, but we cannot predict what systems or languages may be dominant, say, 20 years from now. For the moment, only Chebfun offers the breadth of capabilities entailed in the vision of MATLAB-like functionality for continuous functions and operators in analogy to the long-familiar methods for discrete vectors and matrices.

In this article we have not discussed Chebfun computations with twodimensional periodic functions, which are under development. For example, we are investigating capabilities for solution of time-dependent PDEs on a periodic spatial domain and for PDEs in two space dimensions, one or both of which are periodic. A particularly interesting prospect is to apply such representations to computation with functions on disks and spheres.

For computing with vectors and matrices, although MATLAB codes are rarely the fastest in execution, their convenience makes them nevertheless the best tool for many applications. We believe that Chebfun, including now its extension to periodic problems, plays the same role for numerical computing with functions.

# Acknowledgments

This work was carried out in collaboration with the rest of the Chebfun team, whose names are listed at www.chebfun.org. Particularly active in this phase of the project have been Anthony Austin, Asgeir Birkisson, Toby Driscoll, Nick Hale, ´ Hrothgar (an Oxford graduate student who has just a single name), Alex Townsend, and Kuan Xu. We are grateful to all of these people for their suggestions in preparing this paper. The first author would like to thank the Oxford University Mathematical Institute and, in particular, the Numerical Analysis Group, for hosting and supporting his sabbatical visit in 2014, during which this research was initiated.

# Bibliography

[1] J. L. Aurentz, T. Mach, R. Vandebril, and D. S. Watkins, Fast and backward stable computation of roots of polynomials, SIAM J. Matrix Anal. Appl., 36 (2005), pp. 942–973.   
[2] A. P. Austin, P. Kravanja and L. N. Trefethen, Numerical algorithms based on analytic function values at roots of unity, SIAM J. Numer. Anal., 52 (2014), pp. 1795–1821.   
[3] A. P. Austin and K. Xu, On the numerical stability of the second barycentric formula for trigonometric interpolation in shifted equispaced points, IMA J. Numer. Anal., 37 (2017), pp. 1355–1374.   
[4] Z. Battles and L. N. Trefethen, An extension of MATLAB to continuous functions and operators, SIAM J. Sci. Comput., 25 (2004), pp. 1743–1770.   
[5] J.-P. Berrut, Baryzentrische Formeln zur trigonometrischen Interpolation (I), J. Appl. Math. Phys., 35 (1984), pp. 91–105.   
[6] J.-P. Berrut and L. N. Trefethen, Barycentric Lagrange interpolation, SIAM Rev., 46 (2004), pp. 501–517.   
[7] A. Birkisson and T. A. Driscoll, Automatic Fr´echet differentiation for the numerical solution of boundary-value problems, ACM Trans. Math. Software, 38 (2012), 26.   
[8] A. Birkisson and T. A. Driscoll, Automatic Linearity Detection, preprint, http://eprints.maths.ox.ac.uk, 2013.   
[9] J. P. Boyd, Chebyshev and Fourier Spectral Methods, 2nd ed., Dover, Mineola, NY, 2001.   
[10] P. J. Davis, On the numerical integration of periodic analytic functions, in On Numerical Integration, R. E. Langer, ed., University of Wisconsin Press, Madison, WI, 1959, pp. 45–59.   
[11] T. A. Driscoll, Automatic spectral collocation for integral, integrodifferential, and integrally reformulated differential equations, J. Comput. Phys., 229 (2010), pp. 5980–5998.   
[12] T. A. Driscoll, N. Hale, and L. N. Trefethen, Chebfun Guide, Pafnuty Publications, Oxford, 2014; also available online at www.chebfun.org.   
[13] M. S. P. Eastham, The Spectral Theory of Periodic Differential Equations, Scottish Academic Press, Edinburgh, 1973.   
[14] G. Faber, Uber stetige Funktionen ¨ , Math. Ann., 69 (1910), pp. 372–443.   
[15] C. F. Gauss, Theoria interpolationis methodo nova tractata, in C. F. Gauss, Werke, Bd. 3, K¨oniglichen Gesellschaft der Wissenschaften, G¨ottingen, Germany, 1866, pp. 265–327.   
[16] P. Henrici, Barycentric formulas for interpolating trigonometric polynomials and their conjugates, Numer. Math., 33 (1979), pp. 225–234.   
[17] M. Javed and L. N. Trefethen, The Remez Algorithm for Trigonometric Approximation of Periodic Functions, unpublished preprint.   
[18] Y. Katznelson, An Introduction to Harmonic Analysis, Dover, New York, 1968.   
[19] R. Kress, Ein ableitungsfreies Restglied f¨ur die trigonometrische Interpolation periodischer analytischer Funktionen, Numer. Math., 16 (1971), pp. 389–396.   
[20] K. N. McLeod, Fourfun: A new system for automatic computations using Fourier expansions, SIAM Undergrad. Res. Online, 7 (2014), pp. 330–351.   
[21] G. Meinardus, Approximation of Functions: Theory and Numerical Methods, Springer, Berlin, 1967.   
[22] S. Olver and A. Townsend, A practical framework for infinite-dimensional linear algebra, in Proceedings of the First Workshop for High Performance Technical Computing in Dynamic Languages, IEEE Press, Piscataway, NJ, 2014, pp. 57–62.   
[23] R. B. Platte, L. N. Trefethen, and A. B. J. Kuijlaars, Impossibility of fast stable approximation of analytic functions from equispaced samples, SIAM Rev., 53 (2011), pp. 308–318.   
[24] C. Runge, Uber empirische Funktionen und die Interpolation zwischen ¨ ¨aquisitanten Ordinaten, Z. Math. Phys., 46 (1901), pp. 224–243.   
[25] C. D. T. Runge, Theorie und Praxis der Reihen, reprint, VKM Verlag, Saarbr¨ucken, 2007.   
[26] H. E. Salzer, Coefficients for facilitating trigonometric interpolation, J. Math. Phys., 27 (1948), pp. 274–278.   
[27] L. N. Trefethen, Computing numerically with functions instead of numbers, Commun. ACM, 28 (2015), pp. 91–97.   
[28] L. N. Trefethen, Approximation Theory and Approximation Practice, SIAM, Philadelphia, 2013.   
[29] L. N. Trefethen and J. A. C. Weideman, The exponentially convergent trapezoidal rule, SIAM Rev., 56 (2014), pp. 385–458.   
[30] A. Zygmund, Trigonometric Series, Cambridge University Press, Cambridge, UK, 1959.

# Appendix C. “ATAP for the Unit Disk”

[This article was first published by the Society for Industrial and Applied Mathematics (www.siam.org): A. P. Austin, P. Kravanja, and L. N. Trefethen (2014), Numerical algorithms based on analytic function values at roots of unity, SIAM J. Numer. Anal. 52, no. 4, 1795–1821.]

# C.1 Introduction and the unit disk filter function

The title of this paper suggests a narrow topic, but in fact our aim is a broad one: to present a set of ideas underlying certain numerical algorithms used across computational science. In each application, each geometry, it is easy to get lost in details particular to the problem at hand. But the common threads are remarkable, and concentrating our attention on analytic functions at roots of unity on the unit disk will help us to see them. Figure C.1 summarizes the problems and algorithms we shall discuss. From analytic functions on the unit disk one can reach out to generalizations including harmonic functions [16], matrix-valued functions [70], noncircular geometries [24], irregular sample points [41], nonsmooth functions [20], periodic functions with discontinuities [25], dimensions greater than 2 [78], Helmholtz problems [52], integral equations [37], radial basis functions (RBFs) [26], nonlinear partial differential equations [51], and linear operators [36]. (The references just given are a mix of mathematical classics and numerical state of the art.) We offer this list with the thought in mind that researchers may find it fruitful, in investigating some of these variants, to use the present paper as a template.

Throughout this paper, $n$ is a positive integer and $\left\{ \boldsymbol { z } _ { k } \right\}$ , $0 \leq k \leq n - 1$ , are the $n$ th roots of unity, $z _ { k } = \exp ( 2 \pi i k / n )$ . We let $S$ denote the unit circle, $D$ the open unit disk, and $D _ { R }$ the open disk $\{ z \in C : | z | < R \}$ . The function $f$ is assumed to be analytic in $D _ { R }$ but not $\overline { { D } } _ { R }$ for some $R > 1$ , and $\left\{ f _ { k } \right\}$ are its sampled values $f _ { k } = f ( z _ { k } )$ . The symbol $P _ { n - 1 }$ denotes the set of polynomials of degree at most $n - 1$ .

<table><tr><td></td><td>Polynomial interpolation Méray 1884</td><td>Discrete Cauchy integral Lyness-Delves 1967</td><td>Linearized rational interpolation</td></tr><tr><td rowspan="2">Derivatives or</td><td>Walsh 1935 Henrici 1982 Gutknecht 1986 Boyd 2013 [P],[P*]</td><td>[c]</td><td>Gonnet-Pachon-Tref. 2011 Pachón-Gonnet-V.Deun 2012 [ratdisk]</td></tr><tr><td>Ioakimidis-Pap.-Perd.1991</td><td>Lyness-Sande 1971 Henrici 1979 Fornberg 1981 Bornemann 2011 Ioakimidis-Pap.-Perd.1991</td><td></td></tr><tr><td>Zeros and poles</td><td>Corless 2004 Amiraslani 2006 Townsend 2012</td><td>McCune 1966 Delves-Lyness 1967 Burniston-Siewert 1973 Henrici 1979 Ioakimidis 1985 Anastasselou 1986 Kravanja-Sak.-V.Barel1999 Kravanja-Van Barel 1999 Kravanja-Van Barel 2000</td><td></td></tr><tr><td rowspan="2">Matrix eigenvalues</td><td>[Pz],[Pz*]</td><td>Luck-Stevens 2002 [Cz1],[Cz2],[Cp] Goedecker 1999 Sakurai-Sugiura 2003</td><td>[ratdisk_K],[ratdisk]</td></tr><tr><td></td><td>Sakurai-Tadano 2007 Polizzi 2009 Ikegami-Sakurai 2010 Asakura et al. 2009</td><td></td></tr><tr><td></td><td>[det]</td><td>Beyn 2012</td><td>[res],[ratdisk]</td></tr></table>

A certain simple function will have special importance in our discussion, which one might call the unit disk filter function:19

$$
b ( z ) = { \frac { 1 } { 1 - z ^ { n } } } = \prod _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } } { z _ { k } - z } } .
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/72153cde0d7fc6f256e90bc9820dd997ec8fd5c3e209f47f45cd52e5dc9e2bd5.jpg)  
Figure C.2: Absolute value of the unit disk filter function $b ( z )$ of $( C . 1 )$ for $n = 3 2$ . As $n  \infty$ , the function converges to $^ { 1 }$ for $| z | < 1$ and $_ 0$ for $| z | > 1$ , but there is always a ring of poles along the unit circle.

This is a rational function with $n$ poles and no zeros, apart from a zero of multiplicity $n$ at $z = \infty$ . Figure C.2 illustrates the shape of $b ( z )$ in the complex plane, with values $b ( z ) \approx 1$ inside $D$ and $b ( z ) \approx 0$ outside. The separation between the two regions is effected by a cage of poles along the unit circle. The pole at $z _ { k }$ has residue

$$
\mathrm { R e s } _ { k } = - \frac { z _ { k } } { n } ,
$$

and thus each individual pole gets weaker as $n  \infty$ . In the limit, pointwise for each $z$ with $| z | \neq 1$ , we have

$$
\operatorname* { l i m } _ { n \to \infty } b ( z ) = { \left\{ \begin{array} { l l } { 1 , } & { | z | < 1 , } \\ { 0 , } & { | z | > 1 . } \end{array} \right. }
$$

# C.2 Evaluating a function and its derivatives in the unit disk

# C.2.1 Two algorithms for evaluating a function

We begin with the most basic of all computational problems. Suppose $z \in D$ is given and we wish to evaluate $f ( z )$ approximately based on the values $\left\{ f _ { k } \right\}$ . Here are two good algorithms, whose interplay will resonate throughout this paper. A third approach, based on rational rather than polynomial interpolation, will be introduced in Sections C.4 and C.5 and considered more squarely in Section C.6.

Algorithm P. Polynomial interpolation. Approximate $f ( z )$ by $p ( z )$ , where $p \in P _ { n - 1 }$ is the unique polynomial interpolant to $f$ in the points $\left\{ z _ { k } \right\}$ .

Algorithm C. Discrete Cauchy integral. Approximate $f ( z )$ by the trapezoidal rule discretization in the points $\left\{ \boldsymbol { z } _ { k } \right\}$ of the integral $( 2 \pi i ) ^ { - 1 } \int _ { S } ( \zeta - z ) ^ { - 1 } f ( \zeta ) d \zeta$ .

Both algorithms make use of exactly the same data $\left\{ f _ { k } \right\}$ , and both, as we shall see in Section C.2.4, deliver results that converge geometrically to $f ( z )$ as $n \to \infty$ . Indeed, one’s first thought might be, Are these two different descriptions of the same method? But they are not the same. We shall see that Algorithm C approximates $f ( z )$ not by a polynomial but by the rational function

$$
r ( z ) = { \frac { p ( z ) } { 1 - z ^ { n } } } = b ( z ) p ( z ) .
$$

Thus the result of Algorithm C is the same as that of Algorithm P, but multiplied by the filter function (C.1), which introduces poles at all the roots of unity (except if a sample value $f _ { k }$ happens to be zero). In this paper we shall consider the significance of this relationship from several angles.

In the special case $z = 0$ , $b ( z )$ takes the value 1, and the results of Algorithms $\mathrm { P }$ and C are identical. This is the case that has gotten the most attention in the literature, beginning with work in the 1960s by Lyness and his coauthors, which may partly explain why, amid many publications that discuss algorithms of type C, it is hard to find many that discuss algorithms of type P (see, however, [12, Chapter 5]). Yet for $z \neq 0$ , not only are P and C different, but $\mathrm { P }$ is much more accurate for $| z | \approx 1$ (Theorem C.1). At the data points $\left\{ { z } _ { k } \right\}$ themselves, $\mathrm { P }$ returns exactly correct results, whereas C makes errors of infinite magnitude.

A practical situation where evaluation of a function $f$ from samples on a circle is useful is in problems where accurate direct computation of $f ( z )$ in floating-point arithmetic is impossible because of rounding errors. For an elementary example, consider the evaluation of a “phi function” like $( e ^ { z } - 1 - z ) / z ^ { 2 }$ , a problem of practical importance not only for scalars $z$ but also for matrices [51, 76].

# C.2.2 Barycentric formulas for the two algorithms

To derive formulas for the polynomial interpolant $p$ of algorithm P, one may first define the node polynomial

$$
\ell ( z ) = \prod _ { k = 0 } ^ { n - 1 } ( z - z _ { k } ) = z ^ { n } - 1
$$

and the barycentric weights

$$
\lambda _ { k } = { \frac { 1 } { \ell ^ { \prime } ( z _ { k } ) } } = { \frac { z _ { k } } { n } } .
$$

These give the degree $n - 1$ cardinal polynomial

$$
\ell _ { k } ( z ) = \ell ( z ) \frac { \lambda _ { k } } { z - z _ { k } } = \frac { 1 } { n } \ell ( z ) \frac { z _ { k } } { z - z _ { k } }
$$

for any $k$ , taking the values $^ { 1 }$ at $z = z _ { k }$ and $0$ at the other roots of unity. From (C.7) it follows that the interpolant $p$ can be written in Lagrange form as

$$
p ( z ) = { \frac { 1 } { n } } \ell ( z ) \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } f _ { k } } { z - z _ { k } } } ,
$$

and this is the barycentric formula of the first kind. Here it is to be understood that if $z = z _ { k }$ for some $k$ , then the use of the formula is replaced by the exact value $f _ { k }$ . A similar qualification applies to (C.7) and other formulas in this paper involving

divisions by $z - z _ { k }$ . The resulting polynomial evaluation algorithms are known to be numerically stable [40].

In particular, if $f \equiv 1$ , then its polynomial interpolant is the constant function $p \equiv 1$ , which we can write in the form (C.8) as

$$
1 = { \frac { 1 } { n } } \ell ( z ) \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } } { z - z _ { k } } } .
$$

If (C.8) is divided by (C.9), the factors $n ^ { - 1 } \ell ( z )$ in the numerator and denominator cancel, giving the elegant identity

$$
p ( z ) = \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } f _ { k } } { z - z _ { k } } \Bigg / \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } } { z - z _ { k } } ,
$$

the barycentric formula of the second kind, or in MATLAB,

$$
\mathtt { p z } = \mathtt { m e a n } ( \mathtt { z k . * f k . } / ( \mathtt { z - z k } ) ) / \mathtt { m e a n } ( \mathtt { z k . } / ( \mathtt { z - z k } ) ) .
$$

The work involved is $O ( n )$ operations. Here and in all the MATLAB formulas of this article, $_ { z \mathrm { k } }$ is a column vector containing the $n$ th roots of unity, $z _ { k } = \exp ( 2 \pi i k / n )$ , $0 \leq k \leq n - 1$ , and $\mathtt { f k }$ is the corresponding column vector of values $f _ { k }$ .

The use of the barycentric formula falls in the category of a calculation “by values.” It is equally possible to evaluate $p ( z )$ “by coefficients.” The Taylor coefficients can be computed by the Fast Fourier Transform (FFT), and the algorithm for evaluating $p ( z )$ becomes

$$
\mathsf { c } ~ = ~ \mathsf { f f t } \left( \mathsf { f k } \right) / \mathrm { n } , ~ \mathsf { p z } ~ = ~ \mathsf { p o l y v a l } \left( \mathsf { f l i p u d } \left( \mathsf { c } \right) , \mathsf { z } \right) ,
$$

requiring $O ( n \log n )$ operations, with $O ( n )$ additional operations for each point $z$ after the first one. The formulas behind [P\*] appear in the next section.

We now turn to Algorithm C. The trapezoidal rule formula is [63]

$$
r ( z ) = - { \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } f _ { k } } { z - z _ { k } } } ,
$$

or in MATLAB,

$$
\tt r z = - m e a n ( z k . * f k . / ( z - z k ) ) ,
$$

again with $O ( n )$ operations. Comparing (C) with (C.8), we see that the discrete Cauchy integral approximation to $f ( z )$ is

$$
r ( z ) = - { \frac { p ( z ) } { \ell ( z ) } } ,
$$

and since $- 1 / \ell ( z ) = b ( z )$ , this confirms (C.4). Note that $r$ is a rational function of type $( n - 1 , n )$ , meaning that it has at most $n - 1$ finite zeros (unless it is identically zero) and at most $n$ finite poles, counted with multiplicity, with a zero of order at least $^ { 1 }$ at $z = \infty$ .

# C.2.3 Taylor projections and polynomial interpolants

Suppose $f$ is analytic in $D _ { R }$ for some $R > 1$ . Then it has a Taylor series

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }
$$

with coefficients given by the Cauchy integrals

$$
a _ { k } = { \frac { 1 } { 2 \pi i } } \int _ { S } \zeta ^ { - k - 1 } f ( \zeta ) d \zeta .
$$

Since $f$ is bounded in $D _ { \rho }$ for any $\rho < R$ , Cauchy’s estimate gives

$$
\left| a _ { k } \right| = O ( \rho ^ { - k } ) , \quad k \to \infty .
$$

If we truncate the series to the degree $n - 1$ Taylor section

$$
f _ { n - 1 } ( z ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } z ^ { k } ,
$$

it follows that for any $z \in D _ { R }$ and $\rho$ with $| z | < \rho < R$ we have

$$
| f _ { n - 1 } ( z ) - f ( z ) | = O ( ( | z | / \rho ) ^ { n } ) , \quad n \to \infty ,
$$

uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

In this paper our interest is not Taylor sections $f _ { n - 1 }$ but polynomial interpolants $p _ { n - 1 }$ . (We use the labels $p$ and $p _ { n - 1 }$ interchangeably.) If we write $p _ { n - 1 }$ in the form

$$
p _ { n - 1 } ( z ) = \sum _ { k = 0 } ^ { n - 1 } c _ { k } z ^ { k } ,
$$

then the coefficients $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ are related by the aliasing identity

$$
c _ { k } = a _ { k } + a _ { k + n } + a _ { k + 2 n } + \cdots , \quad 0 \leq k \leq n - 1 .
$$

by its alias In words, $p _ { n - 1 }$ $a _ { k } z ^ { k ( \mathrm { m o d } \ n ) }$ is obtained from . By (C.13) this implies $f$ by replacing each term $a _ { k } z ^ { k }$ in the series (C.11)

$$
| p _ { n - 1 } ( z ) - f ( z ) | = O ( \rho ^ { - n } ) , \quad | z | \leq 1 ,
$$

as $n  \infty$ for any $\rho < R$ , since the leading term of the error is the first of the aliases, $a _ { n } z ^ { 0 }$ , and $a _ { n } = O ( \rho ^ { - n } )$ . For $1 < | z | < R$ , the leading term of the error becomes $- a _ { n } z ^ { n }$ , of order $O ( | z | ^ { n } \rho ^ { - n } )$ , so we get

$$
| p _ { n - 1 } ( z ) - f ( z ) | = O ( | z | ^ { n } \rho ^ { - n } ) , \quad 1 \leq | z | < \rho ,
$$

for any $\rho < R$ . Again these bounds hold uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

If the Taylor coefficients $\{ a _ { k } \}$ , $0 \leq k \leq n - 1$ , are approximated by applying the trapezoidal rule to (C.12), the same aliasing occurs, and so the resulting coefficients are $\left\{ c _ { k } \right\}$ . It is this property that led to the FFT-based algorithm [P\*], which utilizes the fact that the FFT computes all $n$ trapezoidal rule approximations at once.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/3dd94186b259e67a3008c6f265378d27073d72407fcc44ec7e42b9c8c9963e4a.jpg)  
Figure C.3: Error plot for approximations with $n = 3 2$ to $f ( z ) = \log ( 1 . 2 - z )$ by Algorithms P (left) and C (right), with the unit circle marked by a black curve and the branch point at $z = 1 . 2$ marked by a dot. The color bars represent base 10 logarithms. As established in Theorem $C . 1$ , Algorithm P converges throughout $D _ { 1 . 2 }$ as $n \to \infty$ , whereas Algorithm C converges only in $D$ . Faint white dots reflect exact interpolation at the $n = 3 2$ roots of unity on the left, and on the right, at $n + 1 = 3 3$ points close to a smaller circle (see Section C.2.9). At the roots of unity on the right, the errors are infinite because of the poles introduced by the trapezoidal rule.

# C.2.4 Accuracy of the two algorithms

The observations of the foregoing pages are summarized in the following theorem. For a general discussion of the geometric convergence of the trapezoidal rule for periodic analytic integrands, see [85].

Theorem C.1. Let $f$ be analytic in $D _ { R }$ for some $R > 1$ . Then as $n \to \infty$ , for any with $1 < \rho < R$ , the approximation of algorithm $\mathrm { P }$ has accuracy $\rho$

$$
| p ( z ) - f ( z ) | = { \left\{ \begin{array} { l l } { O ( \rho ^ { - n } ) , } & { | z | \leq 1 , } \\ { O ( | z | ^ { n } \rho ^ { - n } ) , } & { 1 \leq | z | < \rho , } \end{array} \right. }
$$

whereas algorithm $C$ gives

$$
| r ( z ) - f ( z ) | = \left\{ { O } ( \rho ^ { - n } ) , \quad | z | \leq R ^ { - 1 } , \right.
$$

These bounds hold uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

Proof. Equation (C.20) was already given as (C.18) and (C.19). Equation (C.21) follows from this together with (C.4), since $1 - ( 1 - z ^ { n } ) ^ { - 1 } = O ( | z | ^ { n } )$ as $n \to \infty$ for each $z$ with $| z | < 1$ .

Let us look at these conclusions in a numerical example. In Figure C.3, the function $f ( z ) = \log ( 1 . 2 - z )$ has been approximated by Algorithms $\mathrm { P }$ and C with $n = 3 2$ . The figure plots the error $| f ( z ) - p ( z ) |$ or $\left| f ( z ) - r ( z ) \right|$ in each approximation, revealing that $\mathrm { P }$ is accurate in a region considerably larger than the unit disk. This phenomenon, which is predicted by (C.20), is known as overconvergence. Method C, on the other hand, only converges in the unit disk, and near the unit circle it loses accuracy, as predicted in (C.21). To be precise, the estimates indicate that $\mathrm { P }$ is more accurate than C for $| z | > R ^ { - 1 }$ .

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/b259fe1dbaaf88ceaaa19fb7ac69741568933331cd7769c0e500ab5f8e87e230.jpg)  
Figure C.4: Phase portraits (see [88]) for the same two approximations as in Figure $C . 3$ . The image on the left shows $n { - } 2$ zeros of $p$ converging as $n \to \infty$ to $| z | = R = 1 . 2$ , the circle of analyticity for this function, in keeping with Jentzsch’s theorem and its generalization by Walsh (Section C.2.5). (The $( n - 1 ) \mathrm { s t }$ zero converges to the zero of $f$ at $z = 0 . 2$ .) The image on the right shows exactly the same zeros and in addition the $n$ poles at the $n$ th roots of unity of the approximation $r ( z ) = b ( z ) p ( z )$ .

Figure C.4 displays the approximations $p ( z )$ and $r ( z )$ themselves, rather than the associated errors. These images are phase portraits, depicting the phase but not the amplitude of each function: red for positive real, green for positive imaginary, cyan for negative real, and violet for negative imaginary [88]. Within the unit disk, it is apparent that both algorithms approximate the same function $f$ , whose zero at $z = 0 . 2$ shows up as a point where all the colors meet. The differences between the two figures near and outside the unit circle, on the other hand, are pronounced.

The theorems and figures of this section highlight an effect that was foreshadowed in Figure C.2: a Cauchy integral over a contour $\Gamma$ does not just approximate a function in the region enclosed by $\Gamma$ ; it acts to separate that region from the exterior. If such a separation is not part of one’s computational purpose, then the discrete Cauchy integral may not be the best algorithm.

# C.2.5 Zeros, poles, and the Jentzsch and Walsh theorems

A striking feature of Figure C.4 is the ring of colorful stripes in each image outside the unit disk. In both cases, these stripes end at $n - 2 = 3 0$ zeros lying approximately on the circle $| z | = 1 . 3$ , which will shrink to $| z | = 1 . 2$ as $n \to \infty$ . For the polynomial approximant $p ( z )$ on the left, the stripes extend outward to $z = \infty$ , where they meet at the pole of multiplicity $n - 1 = 3 1$ . For the rational approximant $r ( z )$ on the right, they point inward and terminate at the $n = 3 2$ poles on the unit circle.

The appearance of a ring of zeros near the circle of convergence of a Taylor series is a well-known phenomenon. According to Jentzsch’s theorem [49], if $f$ is analytic in $D _ { R }$ but not $\overline { { D } } _ { R }$ , the zeros of Taylor sections $f _ { n - 1 }$ cluster at every point on the circle $| z | = R$ as $n \to \infty$ . (This is a generalization of the phenomenon that the zeros of the partial sum $1 + z + \cdots + z ^ { n - 1 }$ of the Taylor series of $( 1 - z ) ^ { - 1 }$ are the $n$ th roots of unity except $z = 1$ .) In the present case Jentzsch’s theorem is inapplicable, because the polynomials $p _ { n - 1 }$ are interpolants in roots of unity rather than Taylor sections. However, a generalization due to Walsh asserts the same conclusion for any sequence of polynomials that is maximally convergent on $D$ , meaning $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \| p _ { n - 1 } - f \| _ { D } ^ { 1 / n } = R ^ { - 1 } } \end{array}$ , where $\| \cdot \| _ { D }$ is the supremum norm on $D$ [86]. By Theorem C.1, polynomial interpolants in roots of unity are maximally convergent, and thus Walsh’s theorem applies to Figure C.4. As $n \to \infty$ , zeros will cluster near every $z$ with $| z | = 1 . 2$ .

# C.2.6 Cauchy integrals of the second kind

The developments of Section C.2.2 suggest a curious observation. In analogy to our progression from (C.8) to (P), we could consider the “Cauchy integral of the second kind”

$$
f ( z ) = \int _ { S } \frac { f ( \zeta ) } { z - \zeta } d \zeta \int _ { S } \frac { 1 } { z - \zeta } d \zeta ,
$$

obtained by dividing the usual Cauchy integral formula for $f$ by the same formula for the case $f \equiv 1$ . Discretizing both the numerator and the denominator of this quotient by the trapezoidal rule then suggests a “discrete Cauchy integral of the second kind,”

$$
\tilde { r } ( z ) = \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } f _ { k } } { z - z _ { k } } \Bigg / \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } } { z - z _ { k } } .
$$

But this is exactly (P)! Thus the discrete Cauchy integral and the polynomial interpolation ideas give the same result after all, if one realizes the former by a nonstandard “second kind” discretization. As Helsing and Ojala put it in the context of an analogous formula for integral equations [37], “One could say that the denominator in this formula compensates for the error in the numerator.” This kind of compensation is familiar to devotees of barycentric formulas, which look numerically unstable at first sight because of their poles but are in fact stable [40].

This multiplicative derivation of (P) may appear rather magical, but a third and more straightforward additive realization of the Cauchy integral idea leads to the same formula. Note that unlike $f ( s ) / ( z - s )$ , the quotient $( f ( z ) - f ( s ) ) / ( z - s )$ has no pole at $s = z$ , so it is an analytic function of $s \in D _ { R }$ , whose Cauchy integral must be equal to zero. A trapezoidal rule discretization of that Cauchy integral accordingly gives

$$
- { \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } { \big ( } f ( z ) - f ( z _ { k } ) { \big ) } } { z - z _ { k } } } \approx 0 ,
$$

and now the summands do not diverge as $z  z _ { k }$ , so one can expect the trapezoidal rule to be more accurate than in (C). Solving for $f ( z )$ in (C.24) gives (C.23) again. This argument has been employed by various authors to derive improved discretizations of integrals near contours [37, 45]. Ioakimidis calls it “the use of the Cauchy theorem instead of the Cauchy formula” [44, 45].

# C.2.7 Derivatives of $f$ or Taylor coefficients

The ideas we have considered for the evaluation of $f ( z )$ extend readily to the evaluation of derivatives $f ^ { ( m ) } ( z )$ for any $m \geq 0$ or, equivalently, the computation of Taylor coefficients. Algorithms $\mathrm { P }$ and $\mathrm { C }$ have the following analogues.

Algorithm $\mathrm { P } ^ { ( m ) }$ . Approximate $f ^ { ( m ) } ( z )$ by $p ^ { ( m ) } ( z )$ , where $p \in \mathcal P _ { n - 1 }$ is the polynomial interpolant to $f$ in $\left\{ { z } _ { k } \right\}$ .

Algorithm $\mathrm { C } ^ { ( m ) }$ . Approximate $f ^ { ( m ) } ( z )$ by the trapezoidal rule discretization in $\left\{ { z } _ { k } \right\}$ of the integral $m ! ( 2 \pi i ) ^ { - 1 } \int _ { S } ( \zeta - z ) ^ { - m - 1 } f ( \zeta ) d \zeta$ .

The same convergence bounds hold as in Theorem C.1, with $\mathrm { P } ^ { ( m ) }$ more accurate than $\mathrm { C } ^ { ( m ) }$ and converging in a larger disk.

MATLAB generalizations of [P], $[ \mathsf { P } { * } ]$ , and [C] can be written as follows for the case $m = 1$ , the first derivative. Formula [P'] evaluates the derivative by a barycentric formula, a technique that originates with [77].

[P'\*]

$$
\begin{array} { r l } & { \mathrm { p z ~ = ~ \ p o n ( z k . * f k . / ( z { - } z k ) ) / m e a n ( z k . / ( z { - } z k ) ) } } \\ & { \mathrm { p p z ~ = ~ \ m e a n ( z k . * ( p z { - } f k ) . / ( z { - } z k ) . ^ { - } 2 ) / m e a n ( z k . / ( z { - } z k ) ) , } } \\ & { \mathrm { c ~ = ~ \ f f t ( t k ) / n , ~ \ c p ~ = ~ \ t ( \ t { - } 1 ) ' . * c ( 2 : e n d ) ~ } } \\ & { \mathrm { p p z ~ = ~ \ p o l y v a l ( f l i i p u d ( c p ) , \boldsymbol z ) , } } \\ & { \mathrm { r p z ~ = ~ \ m e a n ( z k . * f k . / ( z { - } z k ) . ^ { - } 2 ) . } } \end{array}
$$

We shall not discuss these methods at any length, since the mathematics is so close to the case $m = 0$ . However, it is worth noting that it is in the context of derivatives, not function values, that numerical methods based on complex samples are best known, since they eliminate the instabilities that afflict real finite differences. In the words of Lyness and Moler [64], “Once complex arguments are allowed, the principal difficulties encountered in numerical differentiation simply disappear.”

# C.2.8 Scaling of the radius

In this paper we work always with the unit disk and unit circle, but in practice, it is often desirable to vary the radius. According to (C.20), Algorithm P converges approximately at the rate $O ( R ^ { - n } )$ . It follows that if $z$ is rescaled by a factor $\tau < 1$ , so that $f$ is sampled on the circle $| z | = \tau$ , the convergence rate will improve to $O ( ( \tau / R ) ^ { n } )$ . On the other hand, as $\tau$ gets smaller, problems appear of ill-conditioning and rounding errors in floating-point arithmetic. The computation is particularly problematic when one wants to obtain higher Taylor coefficients of $f$ and do so with high relative as opposed to just absolute accuracy. These effects have been noted in this subject from the start, and in the 1980s Fornberg developed an algorithm for determining a good radius adaptively [27]. More recently Bornemann has published a theory showing that an optimal choice of $\tau$ can often eliminate ill-conditioning completely even for very high order derivatives [11].

An interesting extreme case in the matter of choice of radius arises in the method of “complex step differentiation” for computing the first derivative of a real function [80]. Here the grid size is $n = 2$ , using the midpoint rather than the trapezoidal rule, i.e., an imaginary rather than a real finite difference, and the radius $\tau$ is taken smaller than machine epsilon, which is possible since the real and imaginary parts of $z$ and $f ( z )$ are independent floating-point numbers that need not have the same scales.

# C.2.9 The method of fundamental solutions

Let us look again at the faint white spots in Figure C.3, showing points of interpolation. On the left, $f$ is approximated by a polynomial $p \in P _ { n - 1 }$ , which we can think of as a rational function with $n - 1$ poles at $z = \infty$ . The particular approximation in this class is determined by the condition of interpolation of $f$ at the $n$ th roots of unity. On the right, $f$ is approximated by a rational function with $n$ poles at the roots of unity, and the white spots show that it interpolates $f$ in a ring of $n + 1$ points lying approximately on a circle of radius 0.8.

These considerations suggest a unifying view of Algorithms $\mathrm { P }$ and C: choose a set of basis functions $\{ ( z - \zeta _ { k } ) ^ { - 1 } \}$ defined by a fixed set of poles $\left\{ \zeta _ { k } \right\}$ , and approximate $f$ by a linear combination of these basis functions determined by interpolation. To fit the framework of this paper, the interpolation points must be the roots of unity. The two algorithms now begin to look like extremes of a continuum, with poles at $\infty$ or on the unit circle. In-between choices could also be considered, such as poles distributed along a circle such as $| z | = 1 . 1$ . This is the method of fundamental solutions, also known as the charge simulation method [6] (and related to the Trefftz method). If one generalizes the idea to the Helmholtz equation, for example, then the appropriate fundamental solutions become Hankel functions rather than rational functions defined by simple poles.

The reason it may be advantageous to place poles near $S$ rather than at $z = \infty$ has to do with ill-conditioning. If one places poles on the circle $| z | = \tau$ for some $\tau$ , the interpolation problem becomes exponentially ill-conditioned as $\tau$ increases, making large finite values of $\tau$ unworkable. It happens that $\tau = \infty$ is well-behaved, because we can represent polynomials by means other than as linear combinations of simple poles, but such well-behaved representations are not always available in more general situations, such as problems on noncircular domains. And so the idea of placing singularities near the boundary of the problem domain is a powerful one. There is always a trade-off between wanting singularities well separated from the boundary, for accuracy, and close to the boundary, for conditioning.

Related issues of ill-conditioning arise in the use of RBFs for approximating functions $f$ or solving differential equations [26]. RBFs differ from fundamental solutions in that they do not exactly satisfy the differential equation under consideration; on the other hand they need not have singular points, and interpolation points can be distributed inside the problem domain as well as outside it. In analogy to the radius $\tau$ for the method of fundamental solutions, there is now a smoothness parameter $\varepsilon$ , and the limit $\varepsilon  0$ is associated with better approximations but worse conditioning.

# C.3 Zerofinding in the unit disk

# C.3.1 Two algorithms for zerofinding

We now turn to the second fundamental problem of this paper, the calculation of the zeros of $f$ within $D$ . This is an inverse of the former problem: instead of determining the value of $f$ at a given point, now we want to find points where $f$ takes a given value. For clarity we will use the letter $w$ to denote a zero. Once again, we begin with two basic ideas, polynomial interpolation and discretized Cauchy integrals.

We shall see that this time, the Cauchy integral has an advantage when $n$ is large. The first idea can be stated immediately. Curiously, there seems to be very little literature on the following simple algorithm; we know only of [12, Chapter 5].

Algorithm $\mathrm { P } ^ { Z }$ . Polynomial interpolation. Approximate $f$ by the polynomial interpolant $p ( z )$ in $\left\{ \boldsymbol { z } _ { k } \right\}$ and compute the zeros of p that lie in $D$ .

The zeros of $p$ can be calculated by computing its coefficients with the discrete Fourier transform, then finding its zeros by solving a companion matrix eigenvalue problem. In MATLAB, the eigenvalue computation is invoked by the roots command:

$$
\left[ \mathbb { P } \mathrm { z } ^ { * } \right] \qquad \textrm { \textsf { c } } = \textrm { f f t } \left( \mathrm { f k } \right) / \mathrm { n } , \textrm { \textsf { w } } = \textrm { r o o t s } \left( \mathrm { f l } \mathrm { i p u d } \left( \mathrm { c } \right) \right) , \textrm { \textsf { w } } = \textrm { w } \left( \mathrm { a b s } \left( \mathrm { w } \right) < 1 \right) .
$$

Alternatively, working from values rather than coefficients [29], one can compute zeros by solving an $( n + 1 ) \times ( n + 1 )$ generalized eigenvalue problem with arrowhead structure [2, 15]. (This approach produces two spurious eigenvalues at $\infty$ as well as the $n - 1$ eigenvalues corresponding to zeros of $p$ .) The following particularly elegant symmetric form has been suggested by Townsend [82]:

[Pz]

$$
\begin{array} { r l } { \mathrm { ~  ~ A ~ } = } & { \left[ 0 \mathrm { f i k . ~ } ^ { \prime } ; \mathrm { f i k ~ } \mathrm { d i a g } ( \mathrm { f k } ) \right] , \mathrm { ~  ~ B ~ } = \mathrm { d i a g } ( \left[ 0 ; \mathrm { f k . ~ } / z \mathrm { k } \right] ) } \\ { \mathrm { ~  ~ w ~ } = } & { \mathrm { e i g } ( \mathrm { A } , \mathrm { B } ) , \mathrm { ~  ~ w ~ } = \mathrm { w } ( \mathrm { a b s } \left( \mathrm { w } \right) < 1 ) . } \end{array}
$$

Both [Pz] and [Pz\*] require $O ( n ^ { 3 } )$ operations.

Like Algorithms $\mathrm { P }$ and $\mathrm { P } ^ { ( m ) }$ , Algorithm $\mathrm { P } ^ { Z }$ converges geometrically, at least when the zeros are simple.

Theorem C.2. Let $f$ be analytic in $D _ { R }$ for some $R > 1$ with exactly $K$ zeros in $D$ , all of them simple, and no zeros with $| z | = 1$ . Then for all sufficiently large $n$ , Algorithm $\mathrm { P } ^ { Z }$ produces exactly $K$ zeros in $D$ , which converge to the zeros of $f$ at the rate $O ( \rho ^ { - n } )$ as $n \to \infty$ for any $\rho < R$ .

Proof. This follows from (C.20) and the fact that simple zeros of analytic functions vary smoothly with analytic perturbations. ■

Another approach to zerofinding is to use a discretized contour integral. Many different integrals are suitable, and we begin with the one that has had the most attention in the literature, involving the logarithmic derivative $f ^ { \prime } / f$ . This approach has roots in the work of Delves and Lyness and was developed more fully by Kravanja and Van Barel, in collaboration with Sakurai [54], [56, Section 1.2]. The next subsection considers the alternative choice $1 / f$ , a derivative-free variant developed by Kravanja and Van Barel [55], [56, Section 1.6].

To simplify the discussion, we begin by assuming that $f$ has exactly one zero $w$ in $D$ and no zeros with $| w | = 1$ . In this case, $w$ is given by the integral

$$
w = { \frac { 1 } { 2 \pi i } } \int _ { S } { \frac { \zeta f ^ { \prime } ( \zeta ) } { f ( \zeta ) } } d \zeta ,
$$

as follows easily from the residue theorem. This formula goes back to the 19th century and was proposed in the computer era by Delves and Lyness [18] and McCune [66]. In analogy to (C) we get

$$
w \approx \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } ^ { 2 } f _ { k } ^ { \prime } } { f _ { k } } .
$$

For some problems, samples of $f _ { k } ^ { \prime }$ are available and this formula can be used as written. Our convention in this paper, however, is that just $\left\{ f _ { k } \right\}$ are known, in which case $\left\{ f _ { k } ^ { \prime } \right\}$ can be approximated by differentiating the polynomial interpolant as in [P'] or $[ \mathsf { P } ^ { \prime } * ]$ . This gives the following algorithm:

[McCune]

$$
\begin{array} { r l } & { \mathbf { c } ~ = ~ \mathbf { f f t } ( \mathbf { f k } ) / \mathbf { n } , ~ \mathbf { c p } ~ = ~ \left( 1 { : } \mathbf { n - 1 } \right) { : } ~ \mathbf { . } { * } { \mathbf { c } } \left( 2 : \mathbf { e n d } \right) } \\ & { \mathbf { p p } { \mathbf { z } } \mathbf { k } ~ = ~ \mathbf { n } { * } \mathbf { i f f t } ( \left[ \mathbf { c p } { ; } 0 \right] ) , ~ \mathbf { w } ~ = ~ \mathbf { m e a n } ( { \mathbf { z } } \mathbf { k . } { \mathbf { \sigma } } ^ { \sim } 2 . { \boldsymbol { * } } \mathbf { p p } { \mathbf { z } } \mathbf { k } . / \mathbf { f k } ) } \end{array}
$$

Algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ and [McCune] both work excellently in certain circumstances and converge geometrically, with $[ \mathsf { P } z ]$ , as in Sections C.2.4 and C.2.7, having the better convergence constant. A new feature arises now, however, that gives [McCune] an advantage. As mentioned above, $[ \mathsf { P } z ]$ and $[ \mathsf { P } z ^ { * } ]$ require $O ( n ^ { 3 } )$ operations when implemented by general-purpose solvers, whereas the operation count for [McCune] is just $O ( n \log n )$ . For modest values of $n$ like 32 or 64, this difference may not be very important, but when $n$ is in the hundreds, it becomes significant. For example, the function $f ( z ) = \log ( 1 . 1 - z )$ has a zero $w = 0 . 1$ . For 10-digit accuracy, algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ require $n = 1 9 0$ sample points and 0.5 sec on a 2012 desktop computer, whereas [McCune] requires $n = 2 4 0$ points but less than 0.001 sec.

This difference between algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ and [McCune] is rooted in the distinction mentioned in the introduction, Cauchy integrals’ property of separating the region inside the contour from the region outside. Algorithm [Pz] computes all the zeros of a polynomial interpolant, whereas algorithm [McCune] first projects the problem onto the unit disk and then computes only the zeros there. For a problem that is complicated in the large but relatively simple in the disk, this may be much more efficient.

It remains to generalize [McCune] to functions with more than one zero in $D$ . Following [56, Section 1.2], we begin with a generalization of (C.25). Suppose $f$ has $K$ zeros $w _ { 1 } , \ldots , w _ { K }$ in $D$ , which we assume to be simple, and no zeros on $S$ .20 Then for any integer $m \geq 0$ ,

$$
s _ { m } : = \frac { 1 } { 2 \pi i } \int _ { S } \frac { \zeta ^ { m } f ^ { \prime } ( \zeta ) } { f ( \zeta ) } d \zeta = \sum _ { j = 1 } ^ { K } w _ { j } ^ { m } .
$$

Taking $m = 2$ gives the sum of the squares of the zeros, $m = 3$ gives the sum of the cubes, and so on; also $m = 0$ recovers a familiar formula for counting the number of zeros. (These “moment integrals” are the starting point of a theory of formal orthogonal polynomials [19] with respect to the weight function $f ^ { \prime } ( \zeta ) / f ( \zeta )$ [54].) Now consider the $K \times K$ Hankel matrices

$$
H = \left( \begin{array} { c c c } { s _ { 0 } } & { \ldots } & { s _ { K - 1 } } \\ { \vdots } & { } & { \vdots } \\ { s _ { K - 1 } } & { \ldots } & { s _ { 2 K - 2 } } \end{array} \right) , \quad H ^ { < } = \left( \begin{array} { c c c } { s _ { 1 } } & { \ldots } & { s _ { K } } \\ { \vdots } & { } & { \vdots } \\ { s _ { K } } & { \ldots } & { s _ { 2 K - 1 } } \end{array} \right) .
$$

The roots $w _ { 1 } , \ldots , w _ { K }$ are precisely the eigenvalues $\lambda$ of the generalized eigenvalue problem

$$
H ^ { < } x = \lambda H x .
$$

To show this, note that the Hankel matrices can be factored as

$$
\boldsymbol { H } = V V ^ { T } , \quad \boldsymbol { H } ^ { < } = V \mathrm { d i a g } ( w _ { 1 } , \dots , w _ { K } ) V ^ { T } ,
$$

where $V$ is the Vandermonde matrix

$$
V = \left( \begin{array} { c c c } { { 1 } } & { { \dots } } & { { 1 } } \\ { { w _ { 1 } } } & { { \dots } } & { { w _ { K } } } \\ { { } } & { { } } & { { \vdots } } \\ { { w _ { 1 } ^ { K - 1 } } } & { { \dots } } & { { w _ { K } ^ { K - 1 } } } \end{array} \right) .
$$

It is readily verified that the $j$ th column of $V ^ { - T ^ { \prime } }$ is an eigenvector $x$ in (C.29) with eigenvalue $\lambda = w _ { j }$ . If the integrals are approximated by the trapezoidal rule in roots of unity, with $f _ { k } ^ { \prime }$ approximated by polynomial interpolation as in [McCune], this gives us an algorithm for approximating $K$ distinct roots of $f$ in $D$ . The following is a MATLAB realization. Because of the use of the FFT, this algorithm assumes $n \geq 2 K$ , which is not much of a restriction since we would normally expect to have $n \gg K$ when applying any of the algorithms of this article. The same condition arises in the error analysis of this algorithm published in [73].

[Cz1]

$$
\begin{array} { r l } & { \mathrm {  ~ c ~ } = \mathrm {  ~ f f t } ( \mathrm { f } \mathrm { k } ) / \mathrm { n } , \mathrm {  ~ c p ~ } = \mathrm {  ~ ( 1 } { \mathrm {  ~ \cdot n - 1 } } ) \mathrm {  ~ \cdot ~ } \mathrm {  ~ \ast c } ( \mathrm { 2 } : \mathrm { e n d } ) } \\ & { \mathrm { p p z } \mathrm { k } = \mathrm {  ~ n } { \mathrm { \ast } } \mathrm { i } \mathrm { f } \mathrm { f t } ( \mathrm { [ ~ c p ~ } ; 0 \mathrm { ] } ) , \mathrm {  ~ s ~ } = \mathrm { \ i f f t } ( \mathrm { p p z } \mathrm { k } \mathrm {  ~ \cdot ~ } \mathrm { \not { f } \mathrm { k } } ) } \\ & { \mathrm {  ~ H ~ } = \mathrm { \ h a n k e } 1 ( \mathrm { s } ( \mathrm { 2 } : \mathrm { K } { + } \mathrm { 1 } ) , \mathrm {  ~ s } ( \mathrm { K } { + } \mathrm { 1 } : \mathrm { 2 } { \ast } \mathrm { K } ) ) } \\ & { \mathrm {  ~ H 2 ~ } = \mathrm { \ h a n k e } 1 ( \mathrm { s } ( \mathrm { 3 } : \mathrm { K } { + } \mathrm { 2 } ) , \mathrm {  ~ s } ( \mathrm { K } { + } \mathrm { 2 } : \mathrm { 2 } { \ast } \mathrm { K } { + } \mathrm { 1 } ) ) } \\ & { \mathrm {  ~ w ~ } = \mathrm { \ e i g } ( \mathrm { H 2 } , \mathrm { H } ) } \end{array}
$$

Apart from its use of approximations to $f _ { k } ^ { \prime }$ rather than exact values, this algorithm is due to Kravanja and Van Barel in collaboration with Sakurai [54], based on earlier work by Delves and Lyness [18].

Although we have presented $[ \mathsf { C z 1 } ]$ as a generalization of [McCune] to multiple roots, in fact it is different in the case $K = 1$ , and more accurate. This is because its generalized eigenvalue problem gives it the “second kind” nature of a quotient of two trapezoidal approximations, as in (C.23), rather than a single trapezoidal approximant, as in (C.8). For $K = 1$ , the estimate of $w$ delivered by [Cz1] is equal to the estimate delivered by [McCune] divided by a constant close to 1, namely, the trapezoidal approximation to $s _ { 0 } = 1$ , the number of zeros inside the unit disk.

As we shall see in the numerical experiments of Section C.4.2, the assumption of distinct zeros used in deriving [Cz1] is an essential one. As explained in [56], nearly equal zeros cause instability for this algorithm, and additional formulas must be used to treat cases with confluent zeros.

# C.3.2 Cauchy integrals involving $1 / f$ instead of $f ^ { \prime } / f$

In the Cauchy integral method just described, values of the derivative $f ^ { \prime }$ were in principle required and approximated in practice by polynomial interpolation. Other contour integrals can be used for zerofinding, however, that do not involve $f ^ { \prime }$ . For the case where $f$ has just one zero in $D$ , an integral formulation analogous to (C.25) is

$$
w = \int _ { S } \frac { \zeta } { f ( \zeta ) } d \zeta \int _ { S } \frac { 1 } { f ( \zeta ) } d \zeta ,
$$

proposed by Luck and Stevens [61]. The trapezoidal discretization takes this form:

[LuckStevens]

$$
\ l _ { \sf U } = \ m e { \bf a } \ n \left( { \bf z } { \bf k . \hat { \mu } } \hat { \bf \phi } ^ { - } 2 . / { \bf f } { \bf k } \right) / \ m { \bf e } { \bf a } \mathrm { n } \left( { \bf z } { \bf k . \ / } \hat { \bf f } { \bf k } \right) .
$$

Note that unlike [McCune], [LuckStevens] contains a denominator sum, giving it the flavor of a “second kind” discretization. As a consequence, the generalization to the case of $K$ zeros will reduce exactly to [LuckStevens] in the case $K = 1$ .

That generalization is surprisingly easy: we just delete the $f ^ { \prime }$ terms from the algorithm of Section C.3.1! Following [56, Section 1.6], let us redefine the numbers $s _ { m }$ by replacing the integral (C.27) by

$$
s _ { m } : = \frac { 1 } { 2 \pi i } \int _ { S } \frac { \zeta ^ { m } } { f ( \zeta ) } d \zeta = \sum _ { j = 1 } ^ { K } \frac { w _ { j } ^ { m } } { f ^ { \prime } ( w _ { j } ) } ,
$$

assuming the roots are simple. From here the developments proceed as before. Again the zeros of $f$ are the eigenvalues of the generalized eigenvalue problem (C.29); the derivation is the same as before, except with the $j$ th column of $V$ divided by $( f ^ { \prime } ( w _ { j } ) ) ^ { 1 / 2 }$ . (Any choice of square roots will do. There is a much more general structure to these problems; see [7] and [56].) The trapezoidal rule in roots of unity gives accurate approximations and can be realized as follows in MATLAB:

[Cz2]

$$
\begin{array} { r l } & { \textbf { s } = \mathrm { ~ i f f t } ( 1 . / \mathrm { f k } ) } \\ & { \mathrm { ~ H ~ } = \mathrm { ~ h a n k e l } ( \mathbf { s } ( 2 : \mathrm { K } { + } 1 ) , \ \mathbf { s } ( \mathrm { K } { + } 1 : 2 { * } \mathrm { K } ) ) } \\ & { \mathrm { ~ H } 2 \ = \ \mathrm { h a n k e l } ( \mathbf { s } ( 3 : \mathrm { K } { + } 2 ) , \ \mathbf { s } ( \mathrm { K } { + } 2 : 2 { * } \mathrm { K } { + } 1 ) ) } \\ & { \mathbf { w } \ = \ \mathbf { e i g } ( \mathrm { H } 2 , \mathrm { H } ) } \end{array}
$$

Unlike [Cz1], algorithm [Cz2] is able to calculate nearly equal or multiple zeros, as we shall see in the numerical experiments of Section C.4.2. Both algorithms involve Hankel matrices that may be ill-conditioned, however, so they are not stable in all cases.

# C.4 Polefinding in the unit disk

To find zeros of an analytic function $f$ , algorithms [Cz1] and [Cz2] applied Cauchy integrals to the functions $f ^ { \prime } / f$ and $1 / f$ , respectively. However, one might say that at bottom, any algorithm utilizing Cauchy integrals is really a “polefinding” algorithm. Following this line of thinking, suppose we are given a function $g$ that is meromorphic in $D _ { R }$ for some $R > 1$ , having exactly $K$ poles there, which we assume are all in $D$ . We could then consider the problem of calculating these $K$ poles from samples of $g$ at roots of unity. Note that this problem is not quite equivalent to the problem of the last section with $g = 1 / f$ , since $g$ may have both poles and zeros, whereas $f$ was assumed to have no poles.

# C.4.1 Two algorithms for polefinding

Again we shall distinguish two approaches: interpolation and Cauchy integrals. The new feature that appears is that for polefinding, it is necessary to interpolate by rational functions rather than polynomials.

Algorithm $\mathrm { R } ^ { P }$ . Linearized rational interpolation. Assuming $_ { g }$ has $K$ poles in $D _ { R }$ , approximate it by $r ( z ) = p ( z ) / q ( z )$ , where $p \in { \cal P } _ { n - 1 - K }$ , $q \in P _ { K }$ is monic, and the equation $g ( z _ { k } ) q ( z _ { k } ) = p ( z _ { k } )$ holds at each of the nth roots of unity; then compute the zeros of $q$ in $D$ .

Generically, the linearized rational interpolant is a true rational interpolant, but interpolation may fail in cases where $q ( z _ { k } ) = 0$ . Algorithms for computing $r$ and a corresponding MATLAB code ratdisk are given in [33], based on a singular value decomposition (SVD) of a $K \times ( K { + } 1 )$ rectangular Toeplitz matrix of discrete Fourier coefficients of $g$ ; we shall say more in Section C.6. Using these tools, polefinding by linearized rational interpolation reduces to a single call to ratdisk:

$$
[ \bf { r } , \bf { a } , \bf { b } , \mathrm { m u } , \mathrm { n u } , \bf { w } ] ^ { \mathrm { ~ ~ } } = \ c a t d i s k ( \mathrm { g } { \bf } { \bf } { \bf } { \bf } , \ n - 1 - \mathrm { K } , \ \mathrm { K } )
$$

(The same effect is also available via ratinterp(gk,n-1-K,K,[],'unitroots') in Chebfun.) Here gk represents a column vector of samples of $g$ at the roots of unity. If our aim is to find zeros of an analytic function $f$ , we precede [ratdisk_K] by $\mathrm { g } \mathrm { k } \ = \ 1 . / \mathrm { f } \mathrm { k }$ .

Alternatively, we can compute poles by Cauchy integrals. The natural approach here is to use algorithm $[ \mathsf { C } z 2 ]$ with $1 / f$ relabeled as $g$ . For completeness we give this formulation of the algorithm the new name $[ \mathsf { C p } ]$ :

[Cp]

$$
\begin{array} { r l } & { \mathrm { { \bf ~ s } ~ = ~ \mathrm { i f f t } ( \mathrm { { \bf ~ g } k } ) } } \\ & { \mathrm { { \bf ~ H } ~ = ~ \mathrm { h a n k e l } ( \mathrm { { \bf ~ s } } ( 2 : \mathrm { K } { + } 1 ) , ~ \mathrm { { \bf ~ s } } ( \mathrm { { \bf ~ K } } { + } 1 : 2 * \mathrm { K } ) ) } } \\ & { \mathrm { { \bf ~ H } 2 ~ = ~ \mathrm { h a n k e l } ( \mathrm { { \bf ~ s } } ( 3 : \mathrm { K } { + } 2 ) , ~ \mathrm { { \bf ~ s } } ( \mathrm { { \bf ~ K } } { + } 2 : 2 * \mathrm { K } { + } 1 ) ) } } \\ & { \mathrm { { \bf ~ w } ~ = ~ \mathrm { e i g } ( \mathrm { { \bf ~ H } } 2 , \mathrm { { \bf { H } } } ) } } \end{array}
$$

# C.4.2 Numerical illustration of five algorithms for zerofinding

We have presented five algorithms that can be used for zerofinding, with MATLAB names $[ \mathsf { P } z ]$ and [Pz\*] (these two are equivalent), [Cz1], [Cz2] (or [Cp]), and [ratdisk_K]. To illustrate the behavior of these algorithms, we apply them with $n = 5 0$ to the function $f ( z ) = \sin ( z - 0 . 3 ) \log ( 1 . 2 - z )$ , which has two nearby zeros in $D$ at 0.2 and 0.3. The first four algorithms find zeros of $f$ directly, and [ratdisk_K] finds poles of $g = 1 / f$ . Here are the results:

Arrowhead matrix, Algorithm [Pz]: 0.20002100, 0.29997794   
Companion matrix, Algorithm [Pz\*]: 0.20002100, 0.29997794   
Cauchy integrals in f'/f, Algorithm [Cz1]: 0.20468368, 0.30432215   
Cauchy integrals in 1/f, Algorithm [Cz2]: 0.20000116, 0.29999865   
Rational interp. of 1/f, Algorithm [ratdisk_K]: 0.20000116, 0.29999865

These numbers reveal several interesting properties. First, [Pz] and $[ \mathsf { P } z * ]$ give the same results, since they are mathematically equivalent. Second, [Cz1] gives far worse results. This is a consequence of the nearly equal zeros; this algorithm must be modified in such cases, as explained in [56]. Third, [Cz2] and [ratdisk_K] also give the same results. This is a new observation (although it can be found between the lines in Section 2.3 of [56]), which we explain in the next subsection.

Fourth, this last pair of algorithms do not suffer from the nearly equal zeros, and indeed their results are slightly more accurate than those of $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ . As a rule, we believe that linearized rational interpolation is quite a good method for approximating zeros of analytic functions; we shall say more in Section C.6.

# C.4.3 Equivalence of linearized rational interpolation and a discretized contour integral algorithm

The two polefinding algorithms we have described, [ratdisk_K] and [Cz2] (or [Cp]), are mathematically equivalent. We now outline this connection.

let $n \geq 1$ $K < n$ , let  poly $g$ be a funomial in on defined, and let $_ { n }$ f unity,be the $\textstyle q ( z ) = \sum _ { k = 0 } ^ { K } b _ { k } z ^ { k }$ $P _ { K }$ $\textstyle p ( z ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } z ^ { k }$ polynomial in $P _ { n - 1 }$ that interpolates $g ( z ) q ( z )$ at the roots of unity. We know that $p / q$ corresponds to a linearized rational interpolant to $g$ if $p$ belongs to $P _ { n - 1 - K }$ .

Since $p \in P _ { n - 1 }$ , its coefficients $a _ { 0 } , \ldots , a _ { n - 1 }$ can be calculated by interpolation in the roots of unity: a discrete Fourier transform of the data $g ( z _ { k } ) q ( z _ { k } )$ . The condition for $p / q$ to be a linearized rational interpolant to $g$ is $\scriptstyle a _ { n - K } = a _ { n - K + 1 } =$ $\dots = a _ { n - 1 } = 0$ , that is, $K$ equations in the $K + 1$ unknowns $b _ { 0 } , \dots , b _ { K }$ . This rectangular linear system of equations always has a nontrivial solution, and ratdisk finds such a solution by computing an SVD.

Algorithm [Cp] is based on an alternative interpretation of the same conditions $a _ { n - K } = a _ { n - K + 1 } = \cdot \cdot \cdot = a _ { n - 1 } = 0$ . If $p$ has degree $< n - 1$ , its discrete contour integral in the $n$ th roots of unity must be zero:

$$
\sum _ { k = 0 } ^ { n - 1 } z _ { k } p ( z _ { k } ) = \sum _ { k = 0 } ^ { n - 1 } z _ { k } g ( z _ { k } ) q ( z _ { k } ) = 0 .
$$

But for any $j < K$ , $z ^ { j } p ( z )$ still has degree $< n - 1$ , so we actually have

$$
\sum _ { k = 0 } ^ { n - 1 } z _ { k } ^ { j + 1 } g ( z _ { k } ) q ( z _ { k } ) = 0 , \quad 0 \leq j \leq K - 1 .
$$

That is, $q$ is orthogonal to $1 , z , \dots , z ^ { K - 1 }$ , with respect to a discrete symmetric bilinear form supported at the roots of unity (not quite an inner product, since it lacks positive-definiteness and conjugate-symmetry). We say that $q$ is the degree $K$ discrete formal orthogonal polynomial defined by the weights $z _ { k } g ( z _ { k } )$ at the $n$ th roots of unity. From here, standard manipulations bring us to a generalized eigenvalue problem involving Hankel matrices of discrete moments, as described in (C.28)–(C.31) above, with the eigenvalues being the roots of $q$ .

In a word, [ratdisk_K] determines $q$ by its coefficients and [Cp] by its zeros.

# C.5 Computing the eigenvalues of a matrix in the unit disk

Let $A$ be a square matrix of dimension $N$ . How can we find its eigenvalues in the unit disk? This question is a natural extension of the topics addressed up to now in this paper, and it points toward major challenges of computational science, where $A$ will typically be an approximation with $N \gg 1$ to a partial differential or other linear operator. For simplicity we speak of the standard eigenvalue problem $A x = \lambda x$ , though most of the ideas carry over to the generalized eigenvalue problem $A x = \lambda B x$ .

One idea with a zerofinding flavor would be to compute zeros of the determinant, i.e., zeros of the function

$$
f ( z ) = \operatorname* { d e t } ( z I - A ) .
$$

To do this, we could evaluate $f ( z )$ at the $n$ th roots of unity and then apply any of the algorithms of Section C.3 or Section C.4 (with $g = 1 / f$ ). In MATLAB, one could write

[det]

$$
\mathbf { f o r } \ \mathrm {  ~ k ~ } = \ 1 : \mathrm { n } , \mathbf { f k } \left( \mathrm { k } \right) \ = \ \mathbf { d e t } \left( { z \mathrm { k } \left( \mathrm { k } \right) } * \mathrm { I } - \mathrm { A } \right) , \ \mathrm { e n d }
$$

followed by, say, $[ \mathsf { P } z ]$ . (The operation count could be improved from $O ( n N ^ { 3 } )$ to $O ( N ^ { 3 } + n N ^ { 2 } )$ by a preliminary factorization.) To illustrate, consider the $4 \times 4$ matrix

$$
A = \left( \begin{array} { r r r r } { { 3 . 2 } } & { { 1 . 5 } } & { { 0 . 5 } } & { { - 0 . 5 } } \\ { { - 1 . 6 } } & { { 0 . 0 } } & { { - 0 . 4 } } & { { 0 . 6 } } \\ { { - 2 . 1 } } & { { - 2 . 2 } } & { { 0 . 2 } } & { { - 0 . 1 } } \\ { { 2 0 . 7 } } & { { 9 . 3 } } & { { 3 . 9 } } & { { - 3 . 4 } } \end{array} \right)
$$

with eigenvalues $0 . 2 , 0 . 3 , 1 . 5 , - 1 . 9$ ; thus the eigenvalues in $D$ are 0.2 and 0.3. Here are the computed eigenvalue estimates with $n = 3 0$ :

Polynomial interpolation, Algorithm [Pz]/[Pz\*]: 0.20000000, 0.30000000   
Cauchy integrals in f'/f, Algorithm [Cz1]: 0.19901287, 0.29895203   
Cauchy integrals in 1/f, Alg. [Cz2]/[ratdisk_K]: 0.19994887, 0.30005345

In this case polynomial interpolation gives the exact result, since the determinant is a polynomial of degree $N \leq n$ . For dimensions $N \gg 1$ , of course, one would not be prepared to compute enough determinants for this property to hold. The other two algorithms give geometrically accurate results, with linearized rational interpolation performing particularly well.

Although this small-scale experiment was successful, we are not sure whether finding zeros of the determinant is likely to be an attractive option in many largescale computations. An algorithm of this nature has been proposed in [50].

The other approach for computing eigenvalues we will now consider is certainly an important one: computing poles of the resolvent. Strengthening the foundations of algorithms of this kind was a significant motivation for us to write this paper.

The eigenvalues of $A$ are the poles of the resolvent function, $( z I - A ) ^ { - 1 }$ . This function is matrix-valued, but suppose $u$ and $\boldsymbol { v }$ are fixed $N$ -vectors. Then the rational function

$$
g ( z ) = u ^ { * } ( z I - A ) ^ { - 1 } v
$$

is scalar-valued. If $u$ and $v$ are random vectors, then with probability $1$ , $g$ will have poles at all the eigenvalues of $A$ (though some of the residues may be very small). The same applies in the special case where $u$ and $v$ are taken to be equal.

This immediately gives us a first idea for approximating eigenvalues by polefinding: evaluate the scalarized resolvent function $g$ at roots of unity, then use [Cp] or

equivalently [ratdisk_K] to estimate its poles. Each point evaluation of $g$ requires the solution of a linear system of equations involving a shift of $A$ , which may be carried out in parallel:

[res]

$$
\mathrm { f o r ~ \ k ~ = ~ 1 : n , ~ \ g k ( k ) ~ \ b ~ = ~ u ^ { \prime } * ( \tau ( z k ( k ) * I - A ) \setminus \ v u ) , ~ \ e n d }
$$

As an example, consider the same $4 \times 4$ matrix as before. Here are the computed eigenvalue estimates with $n = 3 0$ and $u = v = ( 1 , 1 , 1 , 1 ) ^ { T }$ :

Rational interpolation, Alg. [Cz2]/[ratdisk_K]: 0.20021799, 0.29990926

In the past decade, algorithms of this kind have begun to be widely used. There are two main schools of research in this area: Sakurai and his collaborators in Japan [5, 42, 43, 74, 75], and Polizzi and his collaborators [30, 53, 57, 58, 71, 81], who have given their software package the name FEAST. The Sakurai school began with a trapezoidal discretization of Cauchy integrals, effectively [Cp] applied to the scalarized resolvent function $g$ [74]. Polizzi chose instead a Gauss quadrature discretization over semicircles. Both groups have applied their algorithms to largescale problems in physics, particularly the calculation of electronic structure, where earlier related algorithms were presented by Goedecker [32].

For these eigenvalue computations to be fully effective, one must move beyond scalar functions $g ( z )$ . To explain this we note that although algorithm [ratdisk_K] will find multiple poles, not every multiple eigenvalue of a matrix $A$ produces a multiple pole of the function $g$ ; this will happen only if the eigenvalues correspond to just a single Jordan block (i.e., the algebraic multiplicity is >1 but the geometric multiplicity is 1). The Hermitian matrices that often arise in physics are very far from this situation. To get around this problem, rather than using a single pair of vectors $u$ and $v$ , one can use a set of such vectors, so that $g$ effectively becomes a matrix function of dimension greater than 1 but much less than $N$ . Polizzi utilized this device from the start [71], and Sakurai (the “block Sakurai–Sugiura method”) from 2010 [42, 43]. A further important practical modification is that the sampling at roots of unity may be embedded in an outer loop, so that in the language of our introduction, the unit disk filter function is applied not just once but several times to improve the projection onto the unit disk, damping eigenvector components outside the disk relative to those inside. Many other practical variations have been considered, including use of regions other than a disk, and this is a rapidly moving area of research. Generalizations to nonlinear eigenvalue problems have been published by Asakura et al. [5] and Beyn [10].

# C.6 Rational approximations

Up to now, rational approximations have featured in this paper in two ways. First, there were rational approximations constructed implicitly by discretization of contour integrals, with poles fixed at the roots of unity. Second, there were rational interpolants with $K$ free poles, of type $( n - 1 - K , K )$ , constructed in Sections C.4 and C.5 for the purpose of locating $K$ poles in the unit disk. A rational function is of type $( J , K )$ if it can be written as a quotient $p ( z ) / q ( z )$ for some polynomials $p$ and $q$ of degrees no greater than $J$ and $K$ , respectively.

Here, we want to highlight the power of rational approximations with more free poles, for example, of type $( n - 1 - K , K )$ with $K \approx n / 2$ . (We are grateful to an anonymous referee for urging us to include these comments.) For another publication that showcases the power of rational approximations as compared with polynomials, see [20].

Suppose that samples $f _ { k } = f ( x _ { k } )$ of a function $f$ are available at the $_ { n }$ th roots of unity and we wish to construct a rational approximation $r$ to $f$ of type $( J , K )$ for some prescribed $J$ and $K$ . The most basic method for constructing such approximants is linearized interpolation, as utilized in the last two sections. Here we fix $K \leq n - 1$ and $J = n - 1 - K$ . The linearized equations $f ( z _ { k } ) q ( z _ { k } ) = p ( z _ { k } )$ , $0 \leq k \leq n - 1$ , can always be satisfied, and generically, such solutions will correspond to solutions of the nonlinear equations $f ( z _ { k } ) = p ( z _ { k } ) / q ( z _ { k } )$ too, so long as $q ( z _ { k } ) \neq 0$ . We use the ratdisk algorithm and code of [33] to compute these interpolants, and we shall say more about the significance of this choice in a moment.

Let us look again at some examples already considered in this paper, but now addressing them by linearized rational interpolation with $K = n / 2$ . First, following section C.2.4, suppose $f ( z ) = \log ( 1 . 2 - z ) / \log ( 1 . 2 - 0 . 8 )$ and we wish to evaluate $f ( 0 . 8 )$ based on samples at $n = 3 2$ roots of unity; the exact value is 1. Here are the results for polynomial interpolation as in Section C.2.2, discretized Cauchy integrals also as in Section C.2.2, and linearized rational interpolation with $K = n / 2$ :

[P] or [P\*] 1.00028 [C] 1.0011 [ratdisk] 1.000000000030

We see a dramatic improvement from 3 or 4 correct digits for the earlier methods to 10 correct digits for rational interpolation with $K = n / 2$ . Figure C.5 further reinforces this remarkable result, repeating the images of Figures C.3 and C.4 but now for the new rational approximation $r$ . We see immediately that this is strikingly more accurate than the previous approximations and not confined in the same way to the unit disk.

These happy results are not as straightforward as they may seem. If rational interpolants are computed by the obvious methods of numerical linear algebra, then unless $K$ is sufficiently small, there is a tendency for spurious pole-zero pairs to arise, known as Froissart doublets, in which a pole and a zero are present that are separated by only the order of machine epsilon. Equivalently, these are spurious poles with residues of order machine epsilon. Such difficulties have an august history in the field of rational approximation, both theoretical and numerical, and if the example just displayed is run as suggested with $n = 3 2$ , one such Froissart doublet appears. However, regularization based on an SVD of a Hankel matrix of Laurent coefficients can be used to largely eliminate such effects. Such a regularization algorithm is presented in [33], and the code ratdisk includes this procedure in its default mode of operation. In practice, we believe that this regularization is crucial for the reliability of numerical methods based on rational approximation. For more discussion, see the final chapters of [84].

For the next example, following Section C.4.2, suppose $f ( z ) ~ = ~ \sin ( z ~ -$ $0 . 3 ) \log ( 1 . 2 - z )$ and we seek the zeros of $f$ in the unit disk based on samples at $n = 5 0$ roots of unity; the exact zeros are 0.2 and 0.3. Here are the results for polynomial zerofinding as in Section C.3.1, a discretized contour integral as in

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/fcb6e1601a5e82a537f210ac7270cafcd5c90f6424ce9be7454def0b18c0f5ca.jpg)  
Figure C.5: Repetition of Figures $C . 3$ and $C . 4$ but for the type $( J , K )$ linearized rational interpolant $r$ with $K = n / 2$ as computed robustly with ratdisk. The approximation is now far more accurate. In fact, it remains more accurate even if $N$ is reduced from 32 to 10.

Section C.3.2 (which is the same as ratdisk with $K = 2$ as in Section C.4.1), and ratdisk with $K = n / 2$ . In the last case we simply interpolate the data by rational function, then compute the zeros of this interpolant.

[Pz] or [Pz\*] 0.200021 0.299978 [Cz2] or [ratdisk_K] 0.2000012 0.2999986 [ratdisk] 0.200000000000061 0.299999999999884

The accuracy has improved from 4 or 5 digits to 13. (Without regularization, this example would have five Froissart doublets and hence five spurious zeros.)

Now, consider the $4 \times 4$ matrix eigenvalue example of Section C.5, with eigenvalues 0.2 and 0.3 and $n = 3 0$ roots of unity. We obtain the following results:

[Cp] or [ratdisk_K] 0.20022 0.299909 [ratdisk] 0.200000000000032, 0.299999999999986

Once more there is a great increase in accuracy. (And once more, without regularization, there would be five Froissart doublets—spurious eigenvalues.)

These examples illustrate that over a range of problems, rational approximations with a significant number of free poles have the potential to achieve high accuracy. The results are not always as good as those shown, especially for functions $f$ with complicated behavior outside the unit disk, and they are more fragile than with purely polynomial methods. But it is safe to say that rational approximations are worthy of serious attention in many applications. In the business of FEAST-related algorithms for computing eigenvalues, such approximations are well-established, though not ordinarily presented in these terms. Sakurai and Polizzi speak of choosing larger than necessary parameters to enlarge the search subspace to accelerate convergence. In our language, this amounts to increasing the denominator degree $K$ in a rational approximation.

What we have called linearized rational interpolation is actually, in cases where Froissart doublets are removed, linearized rational least-squares fitting, in which the

sum of squares

$$
\sum _ { k = 0 } ^ { n - 1 } \left| f ( z _ { k } ) q ( z _ { k } ) - p ( z _ { k } ) \right| ^ { 2 }
$$

is minimized. The reason is that ratdisk reduces the denominator degree from $K$ to $K ^ { \prime }$ when certain singular values fall below a tolerance set by default to $1 0 ^ { - 1 4 }$ , so that now there are more constraints than free parameters. For details, see [33] and [84, Chapter 26].

Beyond linearized least-squares, another rational approximation idea is true nonlinear least-squares approximation, where one minimizes

$$
\sum _ { k = 0 } ^ { n - 1 } \left| f ( z _ { k } ) - { \frac { p ( z _ { k } ) } { q ( z _ { k } ) } } \right| ^ { 2 } .
$$

Here, best approximations need not even be unique, but in practice there may be advantages. A paper of Meier and Luenberger shows that a necessary condition for $r$ to be a rational least-squares approximation to an analytic function $f$ on the unit disk is that $r$ interpolates $f$ and also $r ^ { \prime }$ interpolates $f ^ { \prime }$ at the points in the disk that are the symmetric images with respect to the unit circle of the poles of $r$ [67]. This observation has been used as the basis of iterative algorithms in model reduction on the unit circle (“MIRIAm”) [13] and the imaginary axis (“IRKA”) [34]. When the unit circle is discretized by roots of unity, one can formulate an analogous necessary condition involving a polynomial interpolant of $f$ , as we shall report elsewhere.

Beyond these ideas, there are some powerful further methods for constructing rational approximations based on singular value analysis of Hankel matrices. These techniques stem from work of Adamjan, Arov, and Krein around 1970 [1], and different variants go by the names of Hankel norm approximation and CF approximation [4, 31, 83]. In many cases such methods provide approximations that are extremely close to optimal in the $L ^ { \infty }$ norm (where, as with the $L ^ { 2 }$ norm, optima need not always be unique), and an additional feature is that they may satisfy specified stability constraints on the number of poles within the unit disk. An article drawing these threads together, whether in the continuous setting or in the context of discrete data at the roots of unity, remains to be written.

# C.7 Further notes on the literature

In 2008, the third author started to write a book called Neoclassical Numerics, which was to begin with a chapter on the unit disk. Later he decided that the work should concentrate instead on $[ - 1 , 1 ]$ , and it evolved into Approximation Theory and Approximation Practice $/ A T A P$ ) [84]. The present paper now returns to that project of 2008, informed by the subsequent years’ experience with $A T A P$ and also the Chebfun software project: one may think of this paper as a kind of “ $A T A P$ for the unit disk,” or as the mathematical basis for a “Diskfun” project (not planned). There are close links between monomials, roots of unity, and the disk $D _ { R }$ as considered here and Chebyshev polynomials, Chebyshev points, and Bernstein ellipses as discussed in [84].

A feature of both that project and this one is that the mathematics involved is in good part classical, depending on results well distributed across the past century.

In particular, when it comes to approximation of functions in roots of unity, a great expert was Joseph Walsh (1895–1973), who served on the mathematics faculty at Harvard from 1921 to 1966. Walsh had little interest in numerical algorithms, but much of what we have done here would be familiar to him, and we wish he were here to comment on every line of this paper. His book [87] is an important resource, though difficult to read.

In the following we record some notes on individual sections and subsections.

Section C.2.1. Two algorithms for evaluating a function. Algorithm P is not discussed much in the numerical analysis literature, except in [12], but Algorithm C has received plenty of attention, beginning with the work of Lyness and his coauthors in the 1960s [18], [62, 63, 64, 65]. We do not know how often it has been noticed that Algorithms P and C are related by (C.4); this observation appears as equation (5.12) of [35].

Section C.2.2. Barycentric formulas for the two algorithms. For general point sets $\left\{ { z } _ { k } \right\}$ , the first barycentric formula (C.8) is due to Jacobi in 1825 [47] and the second to Dupuy in 1948 [21]. For the particular case of roots of unity, formula (P) was perhaps first written down by Henrici and can be found in print in [9, 35].

Section C.2.3. Taylor projections and polynomial interpolants. A parallel treatment of Chebyshev projections and interpolants can be found in Chapter 4 of [84].

Section C.2.4. Accuracy of the two algorithms. It was Runge in 1904 who first showed convergence in $D$ of polynomial interpolants in roots of unity [72, Section II.15, pp. 136–137], though M´eray had the necessary tools in hand two decades earlier [68]. Geometric convergence in the context of the trapezoidal rule for quadrature was analyzed by Davis in 1959 [17]. The better accuracy of polynomial interpolation as compared with discretized contour integrals for points near the boundary is emphasized in [12, Chapter 5].

Section C.2.5. Zeros, poles, and the Jentzsch and Walsh theorems. Beautiful phase portraits illustrating Jentzsch’s theorem and discretized contour integrals can be found in Figures 3.9–3.14 and 4.18 of [88].

Section C.2.6. Cauchy integrals of the second kind. In the integral equations literature, series-related reformulations of the standard Nystr¨om-type algorithms to achieve better accuracy near contours have been developed lately. An example in the context of the fast multipole method is the QBX method of Kl¨ockner et al. [52].

Section C.2.7. Derivatives of $f$ or Taylor series. The first proposal of numerical calculation of derivatives via the trapezoidal rule applied to Cauchy integrals may have been in [62, 63]. The FFT was introduced into the algorithm in [65], and barycentric formulas for derivatives were introduced in [77].

Section C.2.8. Scaling of the radius. The question of adjusting the radius $\tau$ goes back to [62], where the problem of numerical instability for small $\tau$ was noted.

Section C.2.9. The method of fundamental solutions. The trade-off between accuracy and conditioning in the smooth, high-accuracy regime is a central issue in the field of RBFs [23, 28].

Section C.3.1. Two algorithms for zerofinding. Equation (C.27) goes back to [46]. The classic paper on numerical zerofinding algorithms based on trapezoidal discretization of Cauchy integrals is [18], whose Section 6 proposes the use of the polynomial interpolant to approximate $\left\{ f _ { k } ^ { \prime } \right\}$ as in [Cz1] (i.e., Taylor polynomials with coefficients calculated by the trapezoidal rule). Delves and Lyness use Newton identities to find the roots; Kravanja, Sakurai, and Van Barel [54] use a generalized eigenvalue problem based on modified moments. The “discrete Cauchy integral of the second kind” idea is applied to zerofinding in [44]. The special case of (C.27) with $m = 0$ is the subject of [79].

Section C.4.1. Two algorithms for polefinding. There does not appear to be much literature explicitly on polefinding based on data at roots of unity, though such problems get some attention in [56, Chapter 3] and [33]. Perhaps the most interesting work we know in this connection is [28], where rational interpolants in roots of unity are utilized to evaluate a meromorphic function accurately in the unit disk despite the presence of poles there.

Section C.5. Computing the eigenvalues of a matrix in the unit disk. For more on the interplay of contour integrals, spectral projectors, and electronic structure, see [8, 60].

Section C.6. Rational approximations. A general discussion of the comparative features of rational and polynomial approximation can be found in [84, Chapters 23–28].

# C.8 Conclusions

The central theme of this article is that there are two kinds of algorithms for the problems at hand: those based on function approximations (polynomial or rational) and those based on discretized Cauchy integrals (which implicitly also construct rational approximations). The former have the advantage that they introduce no singularities on the boundary contour and may therefore be more accurate, while the latter have the advantage that they restrict the problem to the interior region and may therefore be faster. Sometimes the two concepts lead to the same result, as in [P] and (C.23), which are identical, or [Cp] and [ratdisk], which are mathematically equivalent but have different stability properties. It is rare in the literature for the two types of algorithms to be distinguished or compared. We believe such comparisons may reveal new computational possibilities, not just for analytic functions on the unit disk but in many other areas that may be regarded as variations on this theme. A list of such variations with references was given in the introduction.

The main algorithms we have discussed can be summarized as follows, listed with the names of their MATLAB realizations:

<table><tr><td>[P]</td><td>Evaluation of f(z） by polynomial interpolation (p. 301)</td></tr><tr><td>[P*]</td><td>Same,coefficient-based algorithm (p. 301)</td></tr><tr><td>[C]</td><td>Evaluation of f(z) by discretized Cauchy integral (p. 301)</td></tr><tr><td>[P&#x27;]</td><td>Evaluation of f&#x27;(z） by polynomial interpolation (p. 306)</td></tr><tr><td>[P&#x27;*]</td><td>Same,coefficient-based algorithm (p. 306)</td></tr><tr><td>[C&#x27;]</td><td>Evaluation of f&#x27;(z) by discretized Cauchy integral (p. 306)</td></tr><tr><td>[Pz]</td><td>Zerofinding for f via polynomial interpolation (p. 308)</td></tr></table>

<table><tr><td>[Pz*] Same,coefficient-based algorithm (p. 308)</td></tr><tr><td>[Cz1] Zerofinding for f via discretized Cauchy integral for f&#x27;/f (p. 310)</td></tr><tr><td>[Cz2] Zerofinding for f via discretized Cauchy integral for 1/f (p. 311)</td></tr><tr><td>[ratdisk_K] Polefinding for g via rational interpolation with K poles (p. 312)</td></tr><tr><td>[Cp] Polefinding for g via discretized Cauchy integral (p. 312)</td></tr><tr><td>[ratdisk] Evaluation/zerofinding/polefinding via rational interpolation</td></tr><tr><td>(p. 315)</td></tr></table>

We close by summarizing some of the main points of this paper:

• For evaluating $f ( z )$ , polynomial interpolants and discretized Cauchy integrals are equivalent for $z = 0$ and otherwise are distinct. The latter method approximates $f$ by a rational function equal to the polynomial interpolant divided by $1 - z ^ { n }$ , making it less accurate for $| z | \approx 1$ .   
• On the other hand, the barycentric formula for polynomial interpolation is identical to a “discretized Cauchy integral of the second kind,” or as Ioakimidis puts it [44, 45], a discretization of “the Cauchy theorem instead of the Cauchy formula.”   
• For zerofinding, the Cauchy integral approach has an $O ( n \log n )$ versus $O ( n ^ { 3 } )$ complexity advantage over polynomial interpolation, because the integral serves to project the problem onto the unit disk. It is not clear that zerofinding via polynomial interpolation has ever been proposed in the literature.   
• The polefinding method we have called [Cp], based on discretized Cauchy integrals, is mathematically equivalent to computing the poles of a linearized rational interpolant, the algorithm we have called [ratdisk_K]. However, the latter is numerically more stable.   
• The originators of algorithm [Cp], Kravanja and Van Barel, recognized its instability and proposed a more stable algorithm based on modified moments and formal orthogonal polynomials [55, 56]. A challenge for future research is to compare the stability of that algorithm and [ratdisk_K].   
• FEAST and related algorithms for finding eigenvalues of a matrix in a disk are derived from the idea of polefinding for the resolvent function. In the simplest case the resolvent is reduced to a scalar; more robust block algorithms reduce it to an intermediate dimension. In addition, an outer iteration may be applied to improve the projection onto the unit disk.   
• All the algorithms mentioned above are outperformed for some problems by rational approximations with more free poles, for example, rational interpolants of type approximately $( n / 2 , n / 2 )$ . Use of the SVD-regularized algorithm and code known as ratdisk from [33] for such calculations (or

equivalently the Chebfun code ratinterp with the 'unitroots' flag) prevents the appearance of spurious pole-zero Froissart doublets.

# Acknowledgments

We are grateful for corrections and suggestions from Alex Barnett, Jean-Paul Berrut, John Boyd, Bengt Fornberg, Martin Gutknecht, Georges Klein, Edward Saff, Alex Townsend, Elias Wegert, and Andr´e Weideman.

# Bibliography

[1] V. Adamjan, D. Arov, and M. Krein, Analytic properties of Schmidt pairs for a Hankel operator and the generalized Schur–Takagi problem, Math. USSR Sb., 15 (1971), pp. 31–73.

[2] A. Amiraslani, New Algorithms for Matrices, Polynomials, and Matrix Polynomials, Ph.D. dissertation, University of Western Ontario, 2006.

[3] E. G. Anastasselou, A formal comparison of the Delves–Lyness and Burniston–Siewert methods for locating the zeros of analytic functions, IMA J. Numer. Anal., 6 (1986), pp. 337–341.

[4] A. C. Antoulas, Approximation of Large-Scale Dynamical Systems, SIAM, Philadelphia, 2005.

[5] J. Asakura, T. Sakurai, H. Tadano, T. Ikegami, and K. Kimura, A numerical method for nonlinear eigenvalue problems using contour integrals, JSIAM Lett., 1 (2009), pp. 52–55.

[6] A. H. Barnett and T. Betcke, Stability and convergence of the method of fundamental solutions for Helmholtz problems on analytic domains, J. Comput. Phys., 227 (2008), pp. 7003–7026.

[7] B. Beckermann, G. H. Golub, and G. Labahn, On the numerical condition of a generalized Hankel eigenvalue problem, Numer. Math., 106 (2007), pp. 41–68.

[8] M. Benzi, P. Boito, and N. Razouk, Decay properties of spectral projectors with applications to electronic structure, SIAM Rev., 55 (2013), pp. 3–64.

[9] J.-P. Berrut and L. N. Trefethen, Barycentric Lagrange interpolation, SIAM Rev., 46 (2004), pp. 501–517.

[10] W.-J. Beyn, An integral method for solving nonlinear eigenvalue problems, Linear Algebra Appl., 436 (2012), 3839–3863.

[11] F. Bornemann, Accuracy and stability of computing high-order derivatives of analytic functions by Cauchy integrals, Found. Comput. Math., 11 (2011), pp. 1–63.

[12] J. P. Boyd, Solving Transcendental Equations: The Chebyshev Polynomial Proxy and Other Numerical Rootfinders, Perturbation Series, and Oracles, SIAM, Philadelphia, 2014.   
[13] A. Bunse-Gerstner, D. Kubalinska, G. Vossen, and D. Wilczek ´ , $h _ { 2 }$ - norm optimal model reduction for large scale discrete dynamical MIMO systems, J. Comput. Appl. Math., 233 (2010), pp. 1202–1216.   
[14] E. E. Burniston and C. E. Siewert, The use of Riemann problems in solving a class of transcendental equations, Proc. Cambridge Phil. Soc., 73 (1973), pp. 111–118.   
[15] R. Corless, Generalized companion matrices for the Lagrange basis, in Proceedings of EACA, 2004, pp. 317–322.   
[16] J. H. Curtiss, Interpolation by harmonic polynomials, J. SIAM, 10 (1962), pp. 709–736.   
[17] P. J. Davis, On the numerical integration of periodic analytic functions, in R. E. Langer, ed., On Numerical Integration: Proceedings of a Symposium, Madison, April 21–23, 1958, University of Wisconsin, 1959, pp. 45–59.   
[18] L. M. Delves and J. N. Lyness, A numerical method for locating the zeros of an analytic function, Math. Comput., 21 (1967), pp. 543–560.   
[19] A. Draux, Formal orthogonal polynomials revisited. Applications, Numer. Algorithms, 11 (1996), pp. 143–158.   
[20] T. A. Driscoll and B. Fornberg, A Pad´e-based algorithm for overcoming the Gibbs phenomenon, Numer. Algorithms, 26 (2001), pp. 77–92.   
[21] M. Dupuy, Le calcul num´erique des fonctions par l’interpolation barycentrique, C. R. Acad. Sci., 226 (1948), 158–159.   
[22] O. E ¨ gecio ˜ glu and C¸ . Koc¸ ˜ , A fast algorithm for rational interpolation via orthogonal polynomials, Math. Comp., 53 (1989), pp. 249–264.   
[23] G. E. Fasshauer, Meshfree Approximation Methods with Matlab, World Scientific, Singapore, 2007.   
[24] L. Fej´er, Interpolation und konforme Abbildung, G¨ottinger Nachrichten (1918), pp. 319–331.   
[25] M. S. Floater and K. Hormann, Barycentric rational interpolation with no poles and high rates of approximation, Numer. Math., 107 (2007), pp. 315–331.   
[26] B. Fornberg and N. Flyer, A Primer on Radial Basis Functions with Applications to the Geosciences, CBMS-NSF Regional Conf. Ser. in Appl. Math. 87, SIAM, Philadelphia, 2015.   
[27] B. Fornberg, Numerical differentiation of analytic functions, ACM Trans. Math. Software, 7 (1981), pp. 512–526.   
[28] B. Fornberg and G. Wright, Stable computation of multiquadric interpolants for all values of the shape parameter, Comput. Math. Appl., 48 (2004), pp. 853–867.   
[29] S. Fortune, Polynomial root finding using iterated eigenvalue computation, in Proceedings of the International Symposium on Symbolic and Algebrica Computation, ACM, 2001, pp. 121–128.   
[30] B. Gavin and E. Polizzi, Non-linear-eigensolver-based alternative to traditional SCF methods, J. Chem. Phys., 138 (2013), pp. 1–8.   
[31] K. Glover, All optimal Hankel-norm approximations of linear multivariable systems and their $L ^ { \infty }$ -error bounds, Internat. J. Control, 39 (1984), pp. 1115– 1193.   
[32] S. Goedecker, Linear scaling electronic structure methods, Rev. Modern Phys., 71 (1999), pp. 1085–1123.   
[33] P. Gonnet, R. Pachon, and L. N. Trefethen ´ , Robust rational interpolation and least-squares, Electron. Trans. Numer. Anal., 38 (2011), pp. 146–167.   
[34] S. Gugercin, A. C. Antoulas, and C. Beattie, $\mathcal { H } _ { 2 }$ model reduction for large-scale linear dynamical systems, SIAM J. Matrix Anal. Appl., 30 (2008), pp. 609–638.   
[35] M. H. Gutknecht, Numerical conformal mapping methods based on function conjugation, J. Comput. Appl. Math, 14 (1986), pp. 31–77.   
[36] N. Hale, N. J. Higham, and L. N. Trefethen, Computing $A ^ { \alpha }$ , $\log ( A )$ , and related matrix functions by contour integrals, SIAM J. Numer. Anal., 46 (2008), pp. 2505–2523.   
[37] J. Helsing and R. Ojala, On the evaluation of layer potentials close to their sources, J. Comput. Phys., 227 (2008), pp. 2899–2921.   
[38] P. Henrici, Fast Fourier methods in complex analysis, SIAM Rev., 21 (1979), pp. 481–527.   
[39] P. Henrici, Essentials of Numerical Analysis with Pocket Calculator Demonstrations, Wiley, New York, 1982.   
[40] N. J. Higham, The numerical stability of barycentric Lagrange interpolation, IMA J. Numer. Anal., 24 (2004), pp. 547–556.   
[41] E. Hlawka, Interpolation analytischer Funktionen auf dem Einheitskreis, in Number Theory and Analysis, P. Tur´an, ed., Plenum, New York, 1969, pp. 99– 118.   
[42] T. Ikegami and T. Sakurai, Contour integral eigensolver for non-Hermitian systems: A Rayleigh–Ritz-type approach, Taiwan J. Math., 14 (2010), pp. 825– 837.

[43] T. Ikegami, T. Sakurai, and U. Nagashima, A filter diagonalization for generalized eigenvalue problems based on the Sakurai–Sugiura projection method, J. Comput. Appl. Math., 223 (2010), pp. 1927–1936.

[44] N. I. Ioakimidis, A modification of the classical quadrature method for locating zeros of analytic functions, BIT, 25 (1985), pp. 681–686.   
[45] N. I. Ioakimidis, K. E. Papadakis, and E. A. Perdios, Numerical evaluation of analytic functions by Cauchy’s theorem, BIT, 31 (1991), pp. 276–285.   
[46] D. Jackson, Roots and singular points of semi-analytic functions, Ann. of Math., 19 (1917), pp. 142–151.   
[47] C. G. J. Jacobi, Disquisitiones Analyticae de Fractionibus Simplicibus, Dissertation, Berlin, 1825.   
[48] C. G. J. Jacobi, Uber die Darstellung einer Reihe gegebner Werthe durch eine ¨ gebrochne rationale Function, J. Reine Angew. Math., 30 (1846), pp. 127–156.   
[49] R. Jentzsch, Untersuchungen zur Theorie Analytischer Funktionen, Dissertation, Berlin, 1914.   
[50] E. Kamgnia and B. Philippe, Counting eignevalues in domains of the complex field, Electron. Trans. Numer. Anal., 40 (2013), pp. 1–16.   
[51] A.-K. Kassam and L. N. Trefethen, Fourth-order time-stepping for stiff PDEs, SIAM J. Sci. Comput., 26 (2005), pp. 1214–1233.   
[52] A. Klockner, A. Barnett, L. Greengard, and M. O’Neil ¨ , Quadrature by expansion: A new method for the evaluation of layer potentials, J. Comput. Phys., 252 (2013), pp. 332–349.   
[53] L. Kramer, E. Di Napoli, M. Galgon, B. Lang, and P. Bientinesi ¨ , Dissecting the FEAST algorithm for generalized eigenproblems, J. Comput. Appl. Math., 244 (2013), pp. 1–9.   
[54] P. Kravanja, T. Sakurai, and M. Van Barel, On locating clusters of zeros of analytic functions, BIT, 39 (1999), pp. 646–682.   
[55] P. Kravanja and M. Van Barel, A derivative-free algorithm for computing zeros of analytic functions, Computing, 63 (1999), pp. 69–91.   
[56] P. Kravanja and M. Van Barel, Computing the Zeros of Analytic Functions, Lecture Notes in Math. 1727, Springer, New York, 2000.   
[57] S. E. Laux, Solving complex band structure problems with the FEAST eigenvalue algorithm, Phys. Rev. B, 86 (2012), 075103.   
[58] A. R. Levin, D. Zhang, and E. Polizzi, FEAST fundamental framework for electronic structure calculations: Reformulation and solution of the muffintin problem, Comput. Phys. Comm., 183 (2012), pp. 2370–2375.

[59] T.-Y. Li, On locating all zeros of an analytic function within a bounded domain by a revised Delves/Lyness method, SIAM J. Numer. Anal., 20 (1983), pp. 865– 871.

[60] L. Lin, J. Lu, L. Ying, and W. E, Pole-based approximation of the Fermi– Dirac function, Chin. Ann. Math. Ser. B, 30 (2009), pp. 729–742.

[61] R. Luck and J. W. Stevens, Explicit solutions for transcendental equations, SIAM Rev., 44 (2002), pp. 227–233.

[62] J. N. Lyness, Numerical algorithms based on the theory of complex variable, in Proceedings of the 22nd National Conference, ACM, 1967, pp. 125–133.

[63] J. N. Lyness and L. M. Delves, On numerical contour integration round a closed contour, Math. Comp., 21 (1967), pp. 561–577.

[64] J. N. Lyness and C. B. Moler, Numerical differentiation of analytic functions, SIAM J. Numer. Anal., 4 (1967), pp. 202–210.

[65] J. N. Lyness and G. Sande, Algorithm 413: ENTCAF and ENTCRE: Evaluation of normalized Taylor coefficients of an analytic function, Commun. ACM, 14 (1971), pp. 669–675.

[66] J. E. McCune, Exact inversion of dispersion relations, Phys. Fluids, 9 (1966), pp. 2082–2084.

[67] L. Meier III and G. G. Luenberger, Approximation of linear constant systems, IEEE Trans. Automat. Control, 12 (1967), pp. 585–588.

[68] C. M´eray, Observations sur la l´egitimit´e de l’interpolation, Ann. Sci. Ec. ´ Norm. Sup´er., 3 (1884), pp. 165–176.

[69] R. Pachon, P. Gonnet, and J. Van Deun ´ , Fast and stable rational interpolation in roots of unity and Chebyshev points, SIAM J. Numer. Anal., 50 (2012), pp. 1713–1734.

[70] C. Pearcy, An elementary proof of the power inequality for the numerical radius, Michigan Math. J., 13 (1966), pp. 289–291.

[71] E. Polizzi, Density-matrix-based algorithm for solving eigenvalue problems, Phys. Rev. B, 79 (2009), pp. 1–6.

[72] C. Runge, Theorie und Praxis der Reihen, G. J. G¨oschen, Leipzig, 1904.

[73] T. Sakurai, P. Kravanja, H. Sugiura, and M. Van Barel, An error analysis of two related quadrature methods for computing zeros of analytic functions, J. Comput. Appl. Math., 152 (2003), pp. 467–480.

[74] T. Sakurai and H. Sugiura, A projection method for generalized eigenvalue problems using numerical integration, J. Comput. Appl. Math, 159 (2003), pp. 119–128.

[75] T. Sakurai and H. Tadano, CIRR: A Rayleigh–Ritz type method with contour integral for generalized eigenvalue problems, Hokkaido Math. J., 36 (2007), pp. 745–757.   
[76] T. Schmelzer and L. N. Trefethen, Evaluating matrix functions for exponential integrators via Carath´eodory–Fej´er approximation and contour integrals, Electron. Trans. Numer. Anal., 29 (2007), pp. 1–18.   
[77] C. Schneider and W. Werner, Some new aspects of rational interpolation, Math. Comp., 47 (1986), pp. 285–299.   
[78] I. H. Sloan and R. S. Womersley, Extremal systems of points and numerical integration on the sphere, Adv. Comput. Math., 21 (2004), pp. 107–125.   
[79] R. Spira, Zeros of approximate functional approximations, Math. Comp., 21 (1967), pp. 41–48.   
[80] W. Squire and G. Trapp, Using complex variables to estimate derivatives of real functions, SIAM Rev., 40 (1998), pp. 110–112.   
[81] P. T. P. Tang and E. Polizzi, Subspace iteration with approximate spectral projection, SIAM J. Matrix Anal. Appl., 35 (2014), pp. 354–390.   
[82] A. Townsend, private communication, 2012.   
[83] L. N. Trefethen, Rational approximation on the unit disk, Numer. Math., 37 (1981), pp. 297–320.   
[84] L. N. Trefethen, Approximation Theory and Approximation Practice, SIAM, Philadelphia, 2013.   
[85] L. N. Trefethen and J. A. C. Weideman, The exponentially convergent trapezoidal rule, SIAM Rev., 56 (2014), pp. 385–458.   
[86] J. L. Walsh, The analogue for maximally convergent polynomials of Jentzsch’s theorem, Duke Math. J., 26 (1959), pp. 605–616.   
[87] J. L. Walsh, Interpolation and Approximation by Rational Functions in the Complex Domain, 5th ed., AMS, Providence, RI, 1969.   
[88] E. Wegert, Visual Complex Functions, Springer, New York, 2012.

# References

Each reference is followed by a note highlighting a contribution of that publication that is relevant to this book. These notes are by no means comprehensive: in most cases the reference includes other significant contributions too. Papers listed by authors such as Cauchy, Chebyshev, Gauss, Jacobi, and Weierstrass can also be found in their collected works.

Among mathematicians of the 19th century, it is hard not to be struck by the remarkable creativity of Jacobi (1804–1851), who in his short life made key early contributions to barycentric interpolation [1825], orthogonal polynomials and Gauss quadrature [1826], and Pad´e approximation and rational interpolation [1846], as well as innumerable topics outside the scope of this book.

As of September 2019, the Mathematics Genealogy Project lists 13445 academic descendants of Pafnuty Lvovich Chebyshev. For example, one chain runs Chebyshev–Lyapunov– Steklov–Smirnov–Sobolev–Ladyzhenskaya–Faddeev–Its and another runs Chebyshev– Markov–Voronoy–Sierpinsky–Mazurkiewicz–Zygmund–Stein–Fefferman.

N. I. Achieser (1930), On extremal properties of certain rational functions (Russian), DAN 18, 495–499. [Equioscillation characterization for best rational approximations.]

N. I. Achieser (1992), Theory of Approximation, Dover. [Treatise by one of Chebyshev’s academic great-grandsons, first published in 1956.]

V. Adamjan, D. Arov and M. Krein (1971), Analytic properties of Schmidt pairs for a Hankel operator and the generalized Schur–Takagi problem, Math. USSR Sb. 15, 31–73. [Major work with a general extension of results of Carath´eodory, Fej´er, Schur, and Takagi to rational approximation on the unit circle.]

L. Ahlfors (1978), Complex Analysis, 3rd ed., McGraw-Hill. [A terse and beautiful complex analysis text by one of the masters, first published in 1953.]

N. Ahmed and P. S. Fisher (1970), Study of algorithmic properties of Chebyshev coefficients, Int. J. Comp. Math. 2, 307–317. [Possibly the first paper to point out that Chebyshev coefficients can be computed by the FFT.]

A. C. Aitken (1926), On Bernoulli’s numerical solution of algebraic equations, Proc. Roy. Soc. Edinb. 46, 289–305. [Discussion of Aitken extrapolation.]   
B. K. Alpert and V. Rokhlin (1991), A fast algorithm for the evaluation of Legendre expansions, SIAM J. Sci. Statist. Comput. 12, 158–179. [Algorithm for converting between Legendre and Chebyshev expansion coefficients.]   
A. Amiraslani (2006), New Algorithms for Matrices, Polynomials, and Matrix Polynomials, PhD diss., U. Western Ontario. [Algorithms related to rootfinding by values rather than Chebyshev coefficients.]   
A. Amiraslani, R. M. Corless, L. Gonzalez-Vega and A. Shakoori (2004), Polynomial algebra by values, TR-04-01, Ontario Research Center for Computer Algebra. [Outlines eigenvalue-based algorithms for finding roots of polynomials from their values at sample points rather than from coefficients in an expansion.]   
A. C. Antoulas (2005), Approximation of Large-Scale Dynamical Systems, SIAM. [Textbook about model reduction, a subject making much use of rational approximation.] A. I. Aptekarev (2002), Sharp constants for rational approximations of analytic functions, $S b$ . Math. 193, 1–72. [Extends the result of Gonchar & Rakhmanov 1989 on rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ to give the precise asymptotic form $E _ { n n } \sim 2 H ^ { n + 1 / 2 }$ first conjectured by Magnus, where $H$ is Halphen’s constant.]   
J. L. Aurentz and L. N. Trefethen (2017a), Block operators and spectral discretizations, SIAM Rev. 59, 423–446. [General presentation of rectangular discretization ideas springing from Driscoll and Hale 2015, the basis of Chebfun’s treatment of ODE BVPs.] J. L. Aurentz and L. N. Trefethen (2017b), Chopping a Chebyshev series, ACM Trans. Math. Softw. 43, 33. [Details of Chebfun’s algorithm for chopping a Chebyshev series at machine precision.]   
T. Bagby and N. Levenberg (1993), Bernstein theorems, New Zeal. J. Math. 22, 1–20. [Presentation of four proofs of Bernstein’s result that best polynomial approximants to a function $f \in C ( [ - 1 , 1 ] )$ converge geometrically if and only if $f$ is analytic, with discussion of extension to higher dimension.]   
G. A. Baker, Jr. and P. Graves-Morris (1996), Pad´e Approximants, 2nd ed., Cambridge U. Press. [The standard reference on many aspects of Pad´e approximations and their applications.]   
N. S. Bakhvalov (1967), On the optimal speed of integrating analytic functions, Comput. Math. Math. Phys. 7, 63–75. [A theoretical paper that introduces the idea of going beyond polynomials to speed up Gauss quadrature by means of a change of variables/conformal map, as in Hale & Trefethen 2008.]   
S. Barnett (1975a), A companion matrix analogue for orthogonal polynomials, Lin. Alg. Applics. 12, 197–208. [Generalization of Good’s colleague matrices to orthogonal polynomials other than Chebyshev. Barnett apparently did not know that Specht 1957 had covered the same ground.]   
S. Barnett (1975b), Some applications of the comrade matrix, Internat. J. Control 21, 849–855. [Further discussion of comrade matrices.]   
Z. Battles (2005), Numerical Linear Algebra for Continuous Functions, DPhil thesis, Oxford U. Computing Laboratory. [Presentation of Chebfun, including description of the Chebfun rootfinding algorithm based on recursion and eigenvalues of colleague matrices.] Z. Battles and L. N. Trefethen (2004), An extension of MATLAB to continuous functions and operators, SIAM J. Sci. Comput. 25, 1743–1770. [Chebfun was conceived on December 8, 2001, and this was the first publication about it.]

F. L. Bauer (1959), The quotient-difference and epsilon algorithms, in R. E. Langer, ed., On Numerical Approximation, U. Wisconsin Press, pp. 361–370. [Introduction of the eta extrapolation algorithm for series.]

R. Bellman, B. G. Kashef and J. Casti (1972), Differential quadrature: A technique for the rapid solution of nonlinear partial differential equations, J. Comput. Phys. 10, 40–52. [Perhaps the first publication to give a formula for the entries of a spectral differentiation matrix.]

S. N. Bernstein (1911), Sur l’approximation des fonctions continues par des polynˆomes, Compt. Rend. Acad. Sci. 152, 502–504. [Announcement of some results proved in Bernstein 1912b.]

S. N. Bernstein (1912a), Sur les recherches r´ecentes relatives \`a la meilleure approximation des fonctions continues par des polynˆomes, in Proc. 5th Intern. Math. Congress, v. 1, pp. 256–266. [Announcement of the results of Bernstein and Jackson on polynomial approximation, including a table summarizing theorems by Bernstein, Jackson, and Lebesgue linking smoothness to rate of convergence.]

S. N. Bernstein (1912b), Sur l’ordre de la meilleure approximation des fonctions continues par des polynˆomes de degr´e donn´e, M´em. Acad. Roy. Belg., 1–104. [Major work, which won a prize from the Belgian Academy of Sciences, establishing a number of the Jackson and Bernstein theorems on rate of convergence of best approximations for differentiable or analytic $f$ . Bernstein’s fundamental estimates for functions analytic in an ellipse appear in Sections 9 and 61.]

S. N. Bernstein (1912c), Sur la valeur asymptotique de la meilleure approximation des fonctions analytiques, Compt. Rend. Acad. Sci. 155, 1062–1065. [One of the first appearances of Bernstein ellipses, used here to analyze convergence of best approximations for a function with a single real singularity on the ellipse.]

S. N. Bernstein (1912d), D´emonstration du th´eor\`eme de Weierstrass fond´ee sur le calcul des probabilit´es, Proc. Math. Soc. Kharkov 13, 1–2. [Bernstein’s proof of the Weierstrass approximation theorem based on Bernstein polynomials.]

S. N. Bernstein (1914a), Sur la meilleure approximation des fonctions analytiques poss´edant des singularit´es complexes, Compt. Rend. Acad. Sci. 158, 467–469. [Generalization of Bernstein 1912c to functions with a conjugate pair of singularities.]

S. N. Bernstein (1914b), Sur la meilleure approximation de $| x |$ par des polynˆomes de degr´es donn´es, Acta Math. 37, 1–57. [Investigates polynomial best approximation of $| x |$ on $[ - 1 , 1 ]$ and mentions as a “curious coincidence” that $n E _ { n } \approx 1 / 2 \sqrt { \pi }$ , a value that became known as the “Bernstein conjecture,” later shown false by Varga and Carpenter.]

S. N. Bernstein (1919), Quelques remarques sur l’interpolation, Math. Annal. 79, 1–12. [Written in 1914 but delayed in publication by the war, this paper, like Faber 1914, pointed out that no array of nodes for interpolation could yield convergence for all continuous functions.]

S. N. Bernstein (1931), Sur la limitation des valeurs d’un polynˆomes $P ( x )$ de degr´e $_ n$ sur tout un segment par ses valeurs en $( n + 1 )$ points du segment, Izv. Akad. Nauk SSSR 7, 1025–1050. [Discussion of the problem of optimal interpolation nodes, defined by minimization of the Lebesgue constant.]

S. N. Bernstein (1938), On the inverse problem of the theory of the best approximation of continuous functions, Sochineya 2, 292–294. [Bernstein’s lethargy theorem.]

J.-P. Berrut (1988), Rational functions for guaranteed and experimentally wellconditioned global interpolation, Comput. Math. Appl. 15, 1–16. [Observes that if the barycentric formula is applied on an arbitrary grid with weights $1 , - 1 , 1 , - 1 , \ldots$ or ${ \scriptstyle { \frac { 1 } { 2 } } , - 1 , 1 , - 1 \ldots }$ , the resulting rational interpolants are pole-free and accurate.]

J.-P. Berrut, R. Baltensperger and H. D. Mittelmann (2005), Recent developments in barycentric rational interpolation, Intern. Ser. Numer. Math. 151, 27–51. [Combines conformal maps with the rational barycentric formula to get high-accuracy approximations of difficult functions.]

J.-P. Berrut, M. S. Floater and G. Klein (2011), Convergence rates of derivatives of a family of barycentric rational interpolants, Appl. Numer. Math. 61, 989–1000. [Establishes convergence rates for derivatives of Floater–Hormann barycentric rational interpolants.]

J.-P. Berrut and L. N. Trefethen (2004), Barycentric Lagrange interpolation, SIAM Rev. 46, 501–517. [Review of barycentric formulas for polynomial and trigonometric interpolation.]

A. Birkisson and T. A. Driscoll (2012), Automatic Fr´echet differentiation for the numerical solution of boundary-value problems. ACM Trans. Math. Softw. 38, 26. [Description of Chebfun’s method for solving nonlinear differential equations based on Newton or damped-Newton iteration and automatic differentiation.]

H.-P. Blatt, A. Iserles and E. B. Saff (1987), Remarks on the behaviour of zeros of best approximating polynomials and rational functions, in J. C. Mason and M. G. Cox, eds., Algorithms for Approximation, Clarendon Press, pp. 437–445. [Shows that the type $( n , n )$ best rational approximations to $| x |$ on $[ - 1 , 1 ]$ have all their zeros and poles on the imaginary axis and converge to $_ x$ in the right half-plane and to $- x$ in the left half-plane.]

H.-P. Blatt and E. B. Saff (1986), Behavior of zeros of polynomials of near best approximation, J. Approx. Th. 46, 323–344. [Shows that if $f \in C ( [ - 1 , 1 ] )$ is not analytic on $[ - 1 , 1 ]$ , then the roots of its best approximants $\{ p _ { n } ^ { * } \}$ cluster at every point of $[ - 1 , 1 ]$ as $n \to \infty$ .]

H. F. Blichfeldt (1901), Note on the functions of the form $f ( x ) \equiv \phi ( x ) + a _ { 1 } x ^ { n - 1 } +$ $a _ { 2 } x ^ { n - 2 } + \cdots + a _ { n }$ which in a given interval differ the least possible from zero, Trans. Amer. Math. Soc. 2, 100–102. [Blichfeldt proves a part of the equioscillation theorem: optimality implies equioscillation.]

M. Bocher ˆ (1906), Introduction to the theory of Fourier’s series, Ann. Math. 7, 81–152. [The paper that named the Gibbs phenomenon.]

I. Bogaert (2014), Iteration-free computation of Gauss–Legendre quadrature nodes and weights, SIAM J. Sci. Comput. 36, A1008–A1026. [Fastest known algorithm for computing nodes and weights even in millions of points, used by Chebfun.]

$\acute { \mathrm { E } }$ . Borel (1905), Le¸cons sur les fonctions de variables r´eelles et les d´eveloppements en s´eries de polynˆomes, Gauthier-Villars, Paris. [The first textbook essentially about approximation theory, including a proof of the equioscillation theorem, which Borel attributes to Kirchberger.]

F. Bornemann, D. Laurie, S. Wagon and J. Waldvogel (2004), The SIAM 100-Digit Challenge: A Study in High-Accuracy Numerical Computing, SIAM. [Detailed study of ten problems whose answers are each a single number, nine of which the authors manage to compute to 10000 digits of accuracy through the use of ingenious algorithms and acceleration methods.]

J. P. Boyd (2001), Chebyshev and Fourier Spectral Methods, 2nd ed., Dover. [A 668-page treatment of the subject with a great deal of practical information.]

J. P. Boyd (2002), Computing zeros on a real interval through Chebyshev expansion and polynomial rootfinding, SIAM J. Numer. Anal. 40, 1666–1682. [Proposes recursive Chebyshev expansions for finding roots of real functions, the idea that is the basis of the roots command in Chebfun.]

J. P. Boyd (2014), Solving Transcendental Equations: The Chebyshev Polynomial Proxy and Other Numerical Rootfinders, Perturbation Series, and Oracles, SIAM. [Presentation of a wide range of ideas related to the proxy rootfinding idea stemming from Good 1961 and used by Chebfun.]

D. Braess (1984), On the conjecture of Meinardus on rational approximation to $e ^ { x }$ . II, $J$ . Approx. Th. 40, 375–379. [Establishes an asymptotic formula conjectured by Meinardus for the best approximation error of $e ^ { x }$ on $[ - 1 , 1 ]$ .]

D. Braess (1986), Nonlinear Approximation Theory, Springer. [Advanced text on rational approximation and other topics, with emphasis on methods of functional analysis.]

C. Brezinski (1996), Extrapolation algorithms and Pad´e approximations: A historical survey, Appl. Numer. Math. 20, 299–318. [Historical survey.]

C. Brezinski and M. Redivo Zaglia (1991), Extrapolation Methods: Theory and Practice, North-Holland. [Extensive survey.]

L. Brutman (1978), On the Lebesgue function for polynomial interpolation, SIAM J. Numer. Anal. 15, 694–704. [Sharpening of a result of Erd˝os 1961 concerning Lebesgue constants.]

L. Brutman (1997), Lebesgue functions for polynomial interpolation—a survey, Ann. Numer. Math. 4, 111–127. [Exceptionally useful survey, including detailed results on interpolation in Chebyshev points.]

P. Butzer and F. Jongmans (1999), P. L. Chebyshev (1821–1894): A guide to his life and work, J. Approx. Th. 96, 111–138. [Discussion of the leading Russian mathematician of the 19th century.]

C. Canuto, M. Y. Hussaini, A. Quarteroni and T. A. Zang (2006), Spectral Methods: Fundamentals in Single Domains, Springer. [A major monograph on both collocation and Galerkin spectral methods.]

C. Carath´eodory and L. Fej´er (1911), Uber den Zusammenhang der Extremen von ¨ harmonischen Funktionen mit ihrer Koeffizienten und ¨uber den Picard-Landauschen Satz, Rend. Circ. Mat. Palermo 32, 218–239. [The paper that led, together with Schur 1918, to the connection of approximation problems with eigenvalues and singular values of Hankel matrices, later the basis of the Carath´eodory–Fej´er method for near-best approximation.]

A. J. Carpenter, A. Ruttan and R. S. Varga (1984), Extended numerical computations on the “1/9” conjecture in rational approximation theory, in P. Graves-Morris, E. B. Saff and R. S. Varga, eds., Rational Approximation and Interpolation, Lect. Notes Math. 1105, Springer. [Calculation to 40 significant digits of the best rational approximations to $e ^ { x }$ on $( - \infty , 0 ]$ of types $( 0 , 0 ) , ( 1 , 1 ) , \dots , ( 3 0 , 3 0 )$ .]

A. L. Cauchy (1821), Sur la formule de Lagrange relative \`a l’interpolation, Cours d’Analyse de l’Ecole Royale Polytechnique: Analyse alg´ebrique, ´ Imprimerie Royale, Paris. [First treatment of the “Cauchy interpolation problem” of interpolation by rational functions.]

A. L. Cauchy (1826), Sur un nouveau genre de calcul analogue au calcul infinit´esimal, Exerc. Math´ematiques 1, 11–24. [One of Cauchy’s foundational texts on residue calculus, including a derivation of what became known as the Hermite integral formula.]

P. L. Chebyshev (1854), Th´eorie des m´ecanismes connus sous le nom de parall´elogrammes, M´em. Acad. Sci. P´etersb., Series 7, 539–568. [Introduction of the idea of best approximation by polynomials in the supremum norm.]

P. L. Chebyshev (1859), Sur les questions de minima qui se rattachent \`a la repr´esentation approximative des fonctions, M´em. Acad. Sci. P´etersb. Series 7, 199–291. [Chebyshev’s principal work on best approximation.]

E. W. Cheney (1999), Introduction to Approximation Theory, Chelsea. [Classic approximation theory text first published in 1966.]

J. F. Claerbout (1985), Imaging the Earth’s Interior, Blackwell. [Text about the mathematics of migration for earth imaging by the man who developed many of these techniques, based on rational approximations of pseudodifferential operators.]

C. W. Clenshaw and A. R. Curtis (1960), A method for numerical integration on an automatic computer, Numer. Math. 2, 197–205. [Introduction of Clenshaw–Curtis quadrature.]

C. W. Clenshaw and K. Lord (1974), Rational approximations from Chebyshev series, in B. K. P. Scaife, ed., Studies in Numerical Analysis, Academic Press, pp. 95–113. [Analysis of Chebyshev–Pad´e approximations.]

W. J. Cody (1975), The FUNPACK package of special function subroutines, ACM Trans. Math. Softw. 1, 13–25. [Codes for evaluating special functions based on rational approximations.]

W. J. Cody (1993), Algorithm 715: SPECFUN—A portable FORTRAN package of special function routines and test drivers, ACM Trans. Math. Softw. 19, 22–32. [Descendant of FUNPACK with greater portability.]

W. J. Cody, W. Fraser and J. F. Hart (1968), Rational Chebyshev approximation using linear equations, Numer. Math. 12, 242–251. [Algol 60 code for best rational approximation by a variant of the Remez algorithm.]

W. J. Cody, G. Meinardus and R. S. Varga (1969), Chebyshev rational approximations to $e ^ { - x }$ in $[ 0 , + \infty )$ and applications to heat-conduction problems, J. Approx. Th. 2, 50–65. [Introduces the problem of approximation of $e ^ { - x }$ on $[ 0 , \infty )$ , or equivalently $e ^ { x }$ on $( - \infty , 0 ]$ , and shows that rational best approximants converge geometrically.]

R. M. Corless and S. M. Watt (2004), Bernstein bases are optimal, but, sometimes, Lagrange bases are better, in Proc. SYNASC (Symbolic and Numeric Algorithms for Scientific Computing), Timisoara, pp. 141–152. [A contribution to polynomial rootfinding with a marvelous title.]

G. Darboux (1878), M´emoire sur l’approximation des fonctions de tr\`es-grands nombres, et sur une classe ´etendue de d´eveloppements en s´erie, J. Math. Pures Appl. 4, 5–56. [3-term recurrence for orthogonal polynomials.]

S. Darlington (1970), Analytical approximations to approximations in the Chebyshev sense, Bell System Tech. J. 49, 1–32. [A precursor to the Carath´eodory–Fej´er method.]

P. J. Davis (1975), Interpolation and Approximation, Dover. [A leading text on the subject, first published in 1963.]

P. J. Davis and P. Rabinowitz (1984), Methods of Numerical Integration, 2nd ed., Academic Press. [The leading reference on numerical integration, with detailed information on many topics, first published in 1975.]

D. Day and L. Romero (2005), Roots of polynomials expressed in terms of orthogonal polynomials, SIAM J. Numer. Anal. 43, 1969–1987. [A rediscovery of the results of Specht, Good, Barnett, and others on colleague and comrade matrices.]

C. de Boor and A. Pinkus (1978), Proof of the conjectures of Bernstein and Erd˝os concerning the optimal nodes for polynomial interpolation, J. Approx. Th. 24, 289–303. [Together with Kilgore 1978, one of the papers solving the theoretical problem of optimal interpolation.]

R. A. DeVore and G. G. Lorentz (1993), Constructive Approximation, Springer. [A monograph emphasizing advanced topics.]

Z. Ditzian and V. Totik (1987), Moduli of Smoothness, Springer. [Careful analysis of smoothness and its effect on polynomial approximation on an interval, including the dependence on location in the interval.]

T. A. Driscoll, F. Bornemann and L. N. Trefethen (2008), The chebop system for automatic solution of differential equations, BIT Numer. Math. 48, 701–723. [Extension of Chebfun to solve differential and integral equations.]   
T. A. Driscoll and N. Hale (2015), Rectangular spectral collocation, IMA J. Numer. Anal. 36, 108–132. [Introduction of spectral collocation methods based on rectangular matrices. See also Aurentz & Trefethen 2017a.]   
M. Dupuy (1948), Le calcul num´erique des fonctions par l’interpolation barycentrique, Compt. Rend. Acad. Sci. 226, 158–159. [This paper is apparently the first to use the expression “barycentric interpolation” and also the first to generalize barycentric interpolation beyond the case of equidistant points considered by Taylor 1945.]   
A. Dutt, M. Gu and V. Rokhlin (1996), Fast algorithms for polynomial interpolation, integration, and differentiation, SIAM J. Numer. Anal. 33, 1689–1711. [Uses the Fast Multipole Method to derive fast algorithms for non-Chebyshev points.]   
H. Ehlich and K. Zeller (1966), Auswertung der Normen von Interpolationsoperatoren, Math. Ann. 164, 105–112. [Bound on Lebesgue constant for interpolation in Chebyshev points.]   
D. Elliott (1973), A direct method for “almost” best uniform approximation, in F. de Hoog and C. Jarvis, eds., Error, Approximation, and Accuracy, U. Queensland Press, pp. 129–143. [A precursor to the Carath´eodory–Fej´er method.]   
M. Embree and D. Sorensen (2013), An Introduction to Model Reduction for Linear and Nonlinear Differential Equations, to appear. [Long-awaited textbook.]   
B. Engquist and A. Majda (1977), Absorbing boundary conditions for the numerical simulation of waves, Math. Comp. 31, 629–651. [Highly influential paper on the use of Pad´e approximations to a pseudodifferential operator to develop numerical boundary conditions.]   
P. Erdos˝ (1961), Problems and results on the theory of interpolation. II, Acta Math. Acad. Sci. Hungar. 12, 235–244. [Shows that Lebesgue constants for optimal interpolation points are no better than for Chebyshev points asymptotically as $n \to \infty$ .]   
T. O. Espelid (2004), Extended doubly adaptive quadrature routines, Tech. Rep. 266, Dept. Informatics, U. Bergen. [Presentation of the exceptionally fast and accurate coteda and da2glob quadrature codes.]   
L. Euler (1760), De seriebus divergentibus, Novi Commentarii academiae scientiarum Petropolitanae 5, 205–237. [Early work on divergent series.]   
L. Euler (1783), De eximio usu methodi interpolationum in serierum doctrina, Opuscula Analytica 1, 157–210. [A work on various applications of interpolation, including equations related to the Newton and Lagrange formulas for polynomial interpolation.]   
L. C. Evans and R. F. Gariepy (1991), Measure Theory and Fine Properties of Functions, CRC Press. [Includes a definition of the total variation in the measure theoretic context.]   
G. Faber (1914), Uber die interpolatorische Darstellung stetiger Funktion ¨ en, Jahresber. Deutsch. Math. Verein. 23, 190–210. [Shows that no fixed system of nodes for polynomial interpolation will lead to convergence for all continuous $f$ .]   
L. Fej´er (1900), Sur les fonctions born´ees et int´egrables, Compt. Rend. Acad. Sci. 131, 984–987. [Fej´er, age 20, provides a new method of summing divergent Fourier series, with

a new proof of the Weierstrass approximation theorem as a corollary.]

L. Fej´er (1910), Lebesguesche Konstanten und divergente Fourierreihen, J. f. Math. 138, 22–53. [Shows that Lebesgue constants for Fourier projection are asymptotic to $( 4 / \pi ^ { 2 } ) \log n$ as $n \to \infty$ .]

L. Fej´er (1916), Ueber Interpolation, Nachr. Gesell. Wiss. G¨ottingen Math. Phys. Kl., 66–91. [Proves the Weierstrass approximation theorem by showing that Hermite–Fej´er interpolants in Chebyshev points of the first kind converge for any $f \in C ( [ - 1 , 1 ] )$ .]

S.-I. Filip, Y. Nakatsukasa, L. N. Trefethen and B. Beckermann (2018), Rational minimax approximation via adaptive barycentric representations, SIAM J. Sci. Comput. 40, A2427–A2455. [Chebfun implementation of Remez algorithm for computing polynomial and rational best approximations.]

A. M. Finkelshtein (2006), Equilibrium problems of potential theory in the complex plane, in Orthogonal Polynomials and Special Functions, Lect. Notes Math. 1883, Springer, pp. 79–117. [Survey article.]

M. S. Floater and K. Hormann (2007), Barycentric rational interpolation with no poles and high rates of approximation, Numer. Math. 107, 315–331. [Extension of results of Berrut 1988 to a family of barycentric rational interpolants of arbitrary order.]

G. B. Folland (1995), Introduction to Partial Differential Equations, 2nd ed., Princeton U. Press. [An elegant introduction to PDEs published first in 1976, including the Weierstrass approximation theorem proved via the heat equation in one or multiple dimensions.]

B. Fornberg (1988), Generation of finite difference formulas on arbitrarily spaced grids, Math. Comp. 51, 699–706. [Stable algorithm for generating finite difference formulas on arbitrary grids.]

B. Fornberg (1996), A Practical Guide to Pseudospectral Methods, Cambridge U. Press. [Practically oriented textbook of spectral collocation methods for solving ODEs and PDEs, based on Chebyshev interpolants.]

S. Fortune (2001), Polynomial root finding using iterated eigenvalue computation, in Proc. 2001 Intl. Symp. Symb. Alg. Comput., ACM, pp. 121–128. [An eigenvalue-based rootfinding algorithm that works directly from data samples rather than expansion coefficients.]

L. Fox and I. B. Parker (1968), Chebyshev Polynomials in Numerical Analysis, Oxford U. Press. [A precursor to the work of the 1970s and later on Chebyshev spectral methods.]

J. G. F. Francis (1961), The QR transformation: A unitary analogue to the LR transformation, parts I and II, Computer J. 4, 256–272 and 332–345. [Introduction of the QR algorithm for numerical computation of matrix eigenvalues.]

A. P. Frankel and W. B. Gragg (1973), Algorithmic almost best uniform rational approximation with error bounds (abstract), SIAM Rev. 15, 418–419. [Short note proposing a method of Chebyshev–Pad´e approximation for $m \geq n$ , based on transplantation to the unit circle.]

G. Freud (1955), Uber einseitige Approximation durch Polynome I, ¨ Acta Sci. Math. (Szeged) 6, 12–28. [Precursor to Xiang & Bornemann 2012.]

G. Frobenius (1881), Ueber Relationen zwischen den N¨aherungsbr¨uchen von Potenzreihen, J. Reine Angew. Math. 90, 1–17. [The first systematic treatment of Pad´e approximation.]

M. Froissart (1969), Approximation de Pad´e: application \`a la physique des particules ´el´ementaires, RCP, Programme No. 25, v. 9, CNRS, Strasbourg, pp. 1–13. [A rare publication by the mathematician and physicist after whom Froissart doublets were named (by Bessis).]

D. Gaier (1987), Lectures on Complex Approximation, Birkh¨auser. [A shorter book presenting some of the material considered at greater length in Smirnov & Lebedev 1968 and Walsh 1969.]

C. F. Gauss (1814), Methodus nova integralium valores per approximationem inveniendi, Comment. Soc. Reg. Scient. Gotting. Recent., pp. 39–76. [Introduction of Gauss quadrature—via continued fractions, not orthogonal polynomials.]

W. Gautschi (1981), A survey of Gauss–Christoffel quadrature formulae, in P. L. Butzer and F. Feh´er, eds., E. B. Christoffel: The Influence of His Work in Mathematics and the Physical Sciences, Birkh¨auser, pp. 72–147. [Outstanding survey of many aspects of Gauss quadrature.]

W. Gautschi (2004), Orthogonal Polynomials: Computation and Approximation, Oxford U. Press. [A monograph on orthogonal polynomials with emphasis on numerical aspects.]

K. O. Geddes (1978), Near-minimax polynomial approximation in an elliptical region, SIAM J. Numer. Anal. 15, 1225–1233. [Chebyshev expansions via the FFT for analytic functions on an interval.]

K. O. Geddes (1981), Block structure in the Chebyshev–Pad´e table, SIAM J. Numer. Anal. 18, 844–861. [Analysis of Chebyshev–Pad´e approximants, showing that previous formulations may break down in cases corresponding to a transplanted problem having poles inside the unit disk.]

W. M. Gentleman (1972a), Implementing Clenshaw–Curtis quadrature, I: Methodology and experience, Comm. ACM 15, 337–342. [A surprisingly modern paper that includes the aliasing formula for Chebyshev polynomials.]

W. M. Gentleman (1972b), Implementing Clenshaw–Curtis quadrature, II: Computing the cosine transformation, Comm. ACM 15, 343–346. [First connection of Clenshaw–Curtis quadrature with the FFT.]

A. Glaser, X. Liu and V. Rokhlin (2007), A fast algorithm for the calculation of the roots of special functions, SIAM J. Sci. Comput. 29, 1420–1438. [Introduction of an algorithm for computation of Gauss quadrature nodes and weights in $O ( n )$ operations rather than $O ( n ^ { 2 } )$ as in Golub & Welsch 1969.]

K. Glover (1984), All optimal Hankel-norm approximations of linear multivariable systems and their $L ^ { \infty }$ -error bounds, Internat. J. Control 39, 1115–1193. [Highly influential article on rational approximations in control theory.]

S. Goedecker (1994), Remark on algorithms to find roots of polynomials, SIAM J. Sci. Comput. 15, 1059–1063. [Emphasizes the stability of companion matrix eigenvalues as an algorithm for polynomial rootfinding, given a polynomial expressed by its coefficients in the monomial basis.]

G. H. Golub and J. H. Welsch (1969), Calculation of Gauss quadrature rules, Math. Comp. 23, 221–230. [Presentation of the famous $O ( n ^ { 2 } )$ algorithm for Gauss quadrature nodes and weights via a tridiagonal Jacobi matrix eigenvalue problem.]

A. A. Gonchar and E. A. Rakhmanov (1989), Equilibrium distributions and degree of rational approximation of analytic functions, Math. USSR-Sb. 62, 305–348. [A landmark paper, first published in Russian in 1987, that applies methods of potential theory to prove that the optimal rate of convergence for type $( n , n )$ rational minimax approximations of $e ^ { x }$ on $( - \infty , 0 ]$ is $O ( ( 9 . 2 8 9 0 3 \dots . . . ) ^ { - n } )$ as $n \to \infty$ .]

V. L. Goncharov (2000), The theory of best approximation of functions, J. Approx. Th. 106, 2–57. [English translation of a 1945 historical survey in Russian emphasizing contributions of Chebyshev and his successors.]

P. Gonnet, S. Guttel and L. N. Trefethen ¨ (2013), Robust Pad´e approximation via SVD, SIAM Rev. 55, 101–117. [Introduction of the robust SVD-based algorithm for computing Pad´e approximants presented in Chapter 27.]

P. Gonnet, R. Pachon and L. N. Trefethen ´ (2011), Robust rational interpolation and least-squares, Elect. Trans. Numer. Anal. 38, 146–167. [A robust algorithm based on the SVD for computing rational approximants without spurious poles.]

I. J. Good (1961), The colleague matrix, a Chebyshev analogue of the companion matrix, Quart. J. Math. 12, 61–68. [Together with Specht 1960, one of the two original independent discoveries that roots of polynomials in Chebyshev form can be computed as eigenvalues of colleague matrices, a term introduced here. Good recommends this approach to numerical rootfinding for functions other than polynomials too; see Boyd 2014.]

A. Gopal and L. N. Trefethen (2019a), New Laplace and Helmholtz solvers, Proc. Natl. Acad. Sci. USA 116, 10223–10225. [Announcement of new algorithms for solving PDEs on regions with corner singularities based on rational approximations with root-exponential convergence as in Newman 1964.]

A. Gopal and L. N. Trefethen (2019b), Solving Laplace problems with corner singularities via rational functions, SIAM J. Numer. Anal. 57, 2074–2094. [Details of the “lightning Laplace solver” announced in the paper above, including a proof of root-exponential convergence based on Hermite and Cauchy integrals.]

D. Gottlieb, M. Y. Hussaini and S. A. Orszag (1984), Theory and applications of spectral methods, in R. G. Voigt, D. Gottlieb, and M. Y. Hussaini, eds., Spectral Methods for Partial Differential Equations, SIAM, pp. 1–54. [Early survey article on spectral collocation methods, including the first publication of the formula for the entries of Chebyshev differentiation matrices.]

W. B. Gragg (1972), The Pad´e table and its relation to certain algorithms of numerical analysis, SIAM Rev. 14, 1–62. [A careful and extensive mathematical reference on the structure and algebra of the Pad´e table as presented in Chapter 27, though with an emphasis on determinants.]

A. Greenbaum and L. N. Trefethen (1994), GMRES/CR and Arnoldi/Lanczos as matrix approximation problems, SIAM J. Sci. Comput. 15, 359–368. [Shows that the GMRES/CR and Arnoldi/Lanczos matrix iterations are equivalent to certain polynomial approximation problems and generalizes this observation to matrix approximation problems such as “ideal GMRES.”]

T. H. Gronwall (1912), Uber die Gibbssche Erscheinung und die trigonometrischen ¨ Summen $\sin x + { \frac { 1 } { 2 } } \sin 2 x + \cdots + { \frac { 1 } { n } } \sin n x$ , Math. Ann. 72, 228–243. [Investigates detailed behavior of Fourier approximations near Gibbs discontinuities.]

M. H. Gutknecht (1983), Algebraically solvable Chebyshev approximation problems, in C. K. Chui, L. L. Schumaker, and J. D. Ward., eds., Approximation Theory IV, Academic Press. [Shows that many examples of $\infty$ -norm best approximations that can be written down explicitly correspond to Carath´eodory–Fej´er approximations.]

M. H. Gutknecht (1990), In what sense is the rational interpolation problem well posed?, Constr. Approx. 6, 437–450. [Generalization of Trefethen & Gutknecht 1985 from Pad´e to multipoint Pad´e approximation.]

M. H. Gutknecht and L. N. Trefethen (1982), Real polynomial Chebyshev approximation by the Carath´eodory–Fej´er method, SIAM J. Numer. Anal. 19, 358–371. [Introduction of CF approximation on an interval.]

S. Guttel ¨ (2010), Rational Krylov Methods for Operator Functions, PhD diss., TU Bergakademie Freiberg. [Survey and analysis of advanced methods of numerical linear algebra based on rational approximations.]

N. Hale, N. J. Higham and L. N. Trefethen (2008), Computing $A ^ { \alpha }$ , $\log ( A )$ , and related matrix functions by contour integrals, SIAM J. Numer. Math. 46, 2505–2523. [Derives efficient algorithms for computing matrix functions from trapezoidal rule approximations to contour integrals accelerated by contour maps. These are equivalent to rational approximations.]

N. Hale and T. W. Tee (2009), Conformal maps to multiply slit domains and applications, SIAM J. Sci. Comput. 31, 3195–3215. [Extension of Tee & Trefethen 2006 to new geometries and applications.]

N. Hale and A. Townsend (2013), Fast and accurate computation of Gauss–Legendre and Gauss–Jacobi quadrature nodes and weights, SIAM J. Sci. Comput. 35, A652–A674. [Proposes an $O ( n )$ algorithm based on asymptotic formulas for computing Gauss quadrature nodes and weights for large $_ n$ , faster than the Glaser–Liu–Rokhlin algorithm and also more accurate. See also Bogaert 2014.]

N. Hale and L. N. Trefethen (2008), New quadrature formulas from conformal maps, SIAM J. Numer. Anal. 46, 930–948. [Shows that conformal mapping can be used to derive quadrature formulas that converge faster than Gauss, as in Bakhvalov 1967.]

N. Hale and L. N. Trefethen (2012), Chebfun and numerical quadrature, Science China Math. 55, 1749–1760. [Review of quadrature algorithms in Chebfun, including fast Gauss and Gauss–Legendre quadrature by the Glaser–Liu–Rokhlin algorithm (but not yet the Hale–Townsend algorithm) with applications to computing with functions with singularities.]

L. Halpern and L. N. Trefethen (1988), Wide-angle one-way wave equations, $J$ . Acoust. Soc. Amer. 84, 1397–1404. [Review of rational approximations to $\sqrt { 1 - s ^ { 2 } }$ on $[ - 1 , 1 ]$ for application to one-way wave equations.]

G. H. Halphen (1886), Trait´e des fonctions elliptiques et de leurs applications, Gauthier-Villars, Paris. [A treatise on elliptic functions that contains a calculation to six digits of the number ${ \approx } 1 / 9 . 2 8 9 0 3$ that later became known as “Halphen’s constant” in connection with the rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

P. C. Hansen (1998), Rank-Deficient and Discrete Ill-Posed Problems: Numerical Aspects of Linear Inversion, SIAM. [A leading monograph on the treatment of rank-deficient or ill-posed matrix problems.]

G. H. Hardy (1991), Divergent Series, revised ed., Editions Jacques Gabay. [Hardy’s ´ marvelous posthumous volume on the mathematics of divergent series, first published in 1949.]

J. F. Hart et al. (1968), Computer Approximations, Wiley. [A classic compendium on computer evaluation of special functions, containing 150 pages of explicit coefficients of rational approximations.]

E. Hayashi, L. N. Trefethen and M. H. Gutknecht (1990), The CF table, Constr. Approx. 6, 195–223. [The most systematic and detailed treatment of the problem of rational CF approximation of a function $f$ on the unit disk, including cases where $f$ is just in the Wiener class or continuous on the unit circle.]

G. Heinig and K. Rost (1984), Algebraic Methods for Toeplitz-like Matrices and Operators, Birkh¨auser. [Analyzes rank properties of Toeplitz and Hankel matrices related to the robust Pad´e algorithms of Chapter 27.]

G. Helmberg and P. Wagner (1997), Manipulating Gibbs’ phenomenon for Fourier interpolation, J. Approx. Th. 89, 308–320. [Analyzes the overshoot in various versions of the Gibbs phenomenon for trigonometric interpolation.]

P. Henrici (1974), Applied and Computational Complex Analysis, Vol. 1, Wiley. [First of three extensive and highly readable volumes of applied complex analysis, full of details that are hard to find elsewhere.]

C. Hermite (1878), Sur la formule d’interpolation de Lagrange, J. Reine Angew. Math. 84, 70–79. [Application of what became known as the Hermite integral formula for polynomial interpolation, which had earlier been given by Cauchy, to problems of interpolation with confluent data points.]

J. S. Hestaven, S. Gottlieb and D. Gottlieb (2007), Spectral Methods for Time-Dependent Problems, Cambridge U. Press. [Well-known textbook on spectral methods.]

E. Hewitt and R. E. Hewitt (1979), The Gibbs–Wilbraham phenomenon: An episode in Fourier analysis, Arch. Hist. Exact Sci. 21, 129–160. [Discussion of the complex and not always pretty history of attempts to analyze the Gibbs phenomenon.]

N. J. Higham (2004), The numerical stability of barycentric Lagrange interpolation, IMA J. Numer. Anal. 24, 547–556. [Proves that barycentric interpolation in Chebyshev points is numerically stable, following earlier work of Rack & Reimer 1982.]

N. J. Higham (2008), Functions of Matrices: Theory and Computation, SIAM. [The definitive treatment of the problem of computing functions of matrices as of 2008. Many of the algorithms have connections with polynomial or rational approximation.]

N. J. Higham (2009), The scaling and squaring method for the matrix exponential revisited, SIAM Rev. 51, 747–764. [Careful analysis of the MATLAB method of evaluating $e ^ { A }$ leads to several improvements in the algorithm and the recommendation to use the Pad´e approximant of type (13, 13).]

N. J. Higham and A. H. Al-Mohy (2010), Computing matrix functions, Acta Numer. 19, 159–208. [Survey includes an appendix comparing Pad´e and Taylor approximants for computing the exponential of a matrix.]

E. Hille (1973), Analytic Function Theory, 2 vols., 2nd ed., Chelsea. [Major work first published in 1959 and 1962.]

M. Hochbruck and A. Ostermann (2010), Exponential integrators, Acta Numer. 19, 209–286. [Survey of exponential integrators for the fast numerical solution of stiff ODEs and PDEs.]

G. Hornecker (1956), D´etermination des meilleures approximations rationnelles (au sens de Tchebichef) de fonctions r´eelles d’une variable sur un segment fini et des bornes d’erreur correspondantes, Compt. Rend. Acad. Sci. 249, 2265–2267. [Possibly the first proposal of a kind of Chebyshev–Pad´e approximation for intervals.]

J. P. Imhof (1963), On the method for numerical integration of Clenshaw and Curtis, Numer. Math. 5, 138–141. [Shows that the Clenshaw–Curtis quadrature weights are positive.]

A. Iserles (2011), A fast and simple algorithm for the computation of Legendre coefficients, Numer. Math. 117, 529–553. [A fast algorithm based on a numerical contour integral over an ellipse in the complex plane.]

D. Jackson (1911), Uber die Genauigkeit der Ann¨aherung stetiger Funktionen d ¨ urch ganze rationale Funktionen gegebenen Grades und trigonometrische Summen gegebener Ordnung, dissertation, G¨ottingen. [Jackson’s PhD thesis under Landau in G¨ottingen, which together with Bernstein’s work at the same time (1912b) established many of the fundamental results of approximation theory. Despite the German, Jackson was an American from Massachusetts, like me—Harvard Class of 1908.]

D. Jackson (1913), On the accuracy of trigonometric interpolation, Trans. Amer. Math.

Soc. 14, 453–461. [In the final paragraph of this paper, polynomial interpolation in Chebyshev points (2.2) is considered, possibly for the first time in the literature.]

C. G. J. Jacobi (1825), Disquisitiones Analyticae de Fractionibus Simplicibus, dissertation, Berlin. [In his discussion of partial fractions Jacobi effectively states the “first form” of the barycentric interpolation formula.]

C. G. J. Jacobi (1826), Uber Gauss’ neue Methode, die Werthe der Integrale ¨ n¨aherungsweise zu finden, J. Reine Angew. Math. 1, 301–308. [This paper first invents the subject of orthogonal polynomials and then shows that Gauss quadrature can be derived in this framework.]

C. G. J. Jacobi (1846), Uber die Darstellung einer Reihe gegebener Werthe durch ein ¨ e gebrochene rationale Function, J. Reine Angew. Math. 30, 127–156. [Jacobi’s major work on rational interpolation.]

R. Jentzsch (1914), Untersuchungen zur Theorie der Folgen analytischer Funktionen, dissertation, Berlin. [Proves that every point on the circle of convergence of a power series is the limit of zeros of its partial sums. Jentzsch was also a noted poet and was killed at age 27 in World War I.]

D. C. Joyce (1971), Survey of extrapolation processes in numerical analysis, SIAM Rev. 13, 435–490. [Scholarly review of a wide range of material.]

A.-K. Kassam and L. N. Trefethen (2005), Fourth-order time-stepping for stiff PDEs, SIAM J. Sci. Comput. 26, 1214–1233. [Application of exponential integrator formulas to efficient numerical solution of stiff PDEs.]

T. A. Kilgore (1978), A characterization of the Lagrange interpolating projection with minimal Tchebycheff norm, J. Approx. Th. 24, 273–288. [Together with de Boor & Pinkus 1978, one of the papers solving the theoretical problem of optimal interpolation.]

P. Kirchberger (1902), Ueber Tchebychefsche Ann¨aherungsmethoden, PhD thesis, G¨ottingen. [Kirchberger’s PhD thesis under Hilbert contains apparently the first full statement and proof of the equioscillation theorem.]

P. Kirchberger (1903), Uber Tchebychefsche Ann¨aherungsmethoden, ¨ Math. Ann. 57, 509–540. [Extract from his PhD thesis the year before, focusing on multivariable extensions but without the equioscillation theorem.]

A. N. Kolmogorov (1948), A remark on the polynomials of P. L. Chebyshev deviating the least from a given function (Russian), Uspehi Mat. Nauk 3, 216–221. [Criterion for best complex approximations.]

D. Kosloff and H. Tal-Ezer (1993), A modified Chebyshev pseudospectral method with an $O ( N ^ { - 1 } )$ time step restriction, J. Comput. Phys. 104, 457–469. [Introduces a change of variables as a basis for nonpolynomial spectral methods.]

A. B. J. Kuijlaars (2006), Convergence analysis of Krylov subspace iterations with methods from potential theory, SIAM Rev. 48, 3–40. [Analyzes the connection between potential theory and the roots of polynomial approximants implicitly constructed by Krylov iterations such as the conjugate gradient and Lanczos iterations.]

J. L. Lagrange (1795), Le¸cons ´el´ementaires sur les Math´ematiques, Le¸con V., J. de l’Ecole polytechnique, ´ Tome II, Cahier 8, Paris, pp. 274–278. [Contains what became known as the Lagrange interpolation formula, published earlier by Waring 1779 and Euler 1783.]

B. Lam (1972), Some Exact and Asymptotic Results for Best Uniform Approximation, PhD thesis, U. of Tasmania. [A precursor to the Carath´eodory–Fej´er method.]

E. Landau (1913), Absch¨atzung der Koeffizientensumme einer Potenzreihe, Archiv Math.

Phys. 21, 42–50 and 250–255. [Investigates the norm of the degree $n$ Taylor projection for functions analytic in the unit disk, now known as the Landau constant, showing it is asymptotic to $\pi ^ { - 1 } \log n$ as $n \to \infty$ .]

H. Lebesgue (1898), Sur l’approximation des fonctions, Bull. Sci. Math. 22, 278–287. [In Lebesgue’s first published paper, he proves the Weierstrass approximation theorem by approximating $| x |$ by polynomials and noting that any continuous function can be approximated by piecewise linear functions.]

A. L. Levin and E. B. Saff (2006), Potential theoretic tools in polynomial and rational approximation, in J.-D. Fournier et al., eds., Harmonic Analysis and Rational Approximation, Lect. Notes Control Inf. Sci. 326, Springer, pp. 71–94. [Survey article by two of the experts.]

R.-C. Li (2004), Near optimality of Chebyshev interpolation for elementary function computations, IEEE Trans. Computers 53, 678–687. [Shows that although Lebesgue constants for Chebyshev points grow logarithmically as $n \to \infty$ , for many classes of functions of interest the interpolants come within a factor of 2 of optimality.]

E. L. Lindman (1975), “Free-space” boundary conditions for the time-dependent wave equation, J. Comput. Phys. 18, 66–78. [Absorbing boundary conditions based on Pad´e approximation of a square root function, later developed further by Engquist & Majda 1977].

G. G. Lorentz (1986), Approximation of Functions, 2nd ed., Chelsea. [A readable treatment including good summaries of the Jackson theorems for polynomial and trigonometric approximation, first published in 1966.]

K. N. Lungu (1971), Best approximations by rational functions, Math. Notes 10, 431– 433. [Shows that the best rational approximations to a real function on an interval may be complex and hence also nonunique, with examples as simple as type $( 1 , 1 )$ approximation of $| x |$ on $[ - 1 , 1 ]$ .]

H. J. Maehly (1963), Methods for fitting rational approximations, Parts II and III, $J$ . ACM 10, 257–277. [Posthumous completion by Ch. Witzgall of a 1957 publication by Maehly on practical numerical methods of rational approximation, including a linearized form of Chebyshev–Pad´e approximation.]

H. J. Maehly and Ch. Witzgall (1960), Tschebyscheff-Approximationen in kleinen Intervallen. II. Stetikeitss¨atze f¨ur gebrochen rationale Approximationen, Numer. Math. 2, 293–307. [Investigates well-posedness of the Cauchy interpolation problem and asymptotics of best approximations on small intervals.]

A. P. Magnus (1985), CFGT determination of Varga’s constant “1/9”, unpublished manuscript. [First identification of the exact value of Halphen’s constant $C = 9 . 2 8 9 0 3 \dots$ for the optimal rate of convergence $O ( C ^ { - n } )$ of best type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ , later proved correct by Gonchar $\&$ Rakhmanov 1989.]

A. P. Magnus (1994), Asymptotics and super asymptotics for best rational approximation error norms to the exponential function (the “1/9” problem) by the Carath´eodory–Fej´er method, in A. Cuyt et al., eds., Nonlinear Methods and Rational Approximation II, Kluwer, 1994, pp. 173–185. [Sharper conjectures on the “1/9 problem,” later proved valid by Aptekarev.]

A. P. Magnus and J. Meinguet (2000), The elliptic functions and integrals of the “1/9” problem, Numer. Alg. 24, 117–139. [Summary of work initiated by Magnus relating potential theory, elliptic functions, and the “1/9” problem.]

J. Marcinkiewicz (1936–37), Quelques remarques sur l’interpolation, Acta Sci. Math. (Szeged) 8, 127–30. [In contrast to the result of Faber 1914, shows that for any fixed continuous function $f$ there is an array of interpolation nodes that leads to convergence as $n \to \infty$ .]

A. I. Markushevich (1985), Theory of Functions of a Complex Variable, 2nd ed., 3 vols., Chelsea. [A highly readable treatise on complex variables first published in 1965, including chapters on Laurent series, polynomial interpolation, harmonic functions, and rational approximation.]   
J. C. Mason and D. C. Handscomb (2003), Chebyshev Polynomials, Chapman and Hall/CRC. [An extensive treatment of four varieties of Chebyshev polynomials and their applications.]   
G. Mastroianni and M. G. Russo (2010), Some new results on Lagrange interpolation for bounded variation functions, J. Approx. Th. 162, 1417–1428. [A collection of bounds in $L ^ { p }$ norms for both $p < \infty$ and $p = \infty$ .]   
G. Mastroianni and J. Szabados (1995), Jackson order of approximation by Lagrange interpolation. II, Acta Math. Acad. Sci. Hungar. 69, 73–82. [Corollary 2 bounds the rate of convergence of Chebyshev interpolants for functions whose $k { \mathrm { t h } }$ derivative has bounded variation.]   
J. H. McCabe and G. M. Phillips (1973), On a certain class of Lebesgue constants, BIT 13, 434–442. [Shows that the Lebesgue constant for polynomial interpolation in $n + 1$ Chebyshev points of the second kind is bounded by that of $_ n$ Chebyshev points of the first kind. The same result had been found earlier by Ehlich & Zeller 1966.]   
J. H. McClellan and T. W. Parks (2005), A personal history of the Parks–McClellan algorithm, IEEE Sign. Proc. Mag. 82, 82–86. [The story of the development of the celebrated filter design algorithm published in Parks & McClellan 1972.]   
G. Meinardus (1967), Approximation of Functions: Theory and Numerical Methods, Springer. [Classic approximation theory monograph.]   
C. M´eray (1884), Observations sur la l´egitimit´e de l’interpolation, Annal. Scient. de l’Ecole Normale Sup´erieure ´ 3, 165–176. [Discussion of the possibility of nonconvergence of polynomial interpolants 17 years before Runge, though without so striking an example or conclusion. M´eray uses just the right technique, the Hermite integral formula, which he correctly attributes to Cauchy.]   
C. M´eray (1896), Nouveaux exemples d’interpolations illusoires, Bull. Sci. Math. 20, 266–270. [Continuation of M´eray 1884 with more examples.]   
S. N. Mergelyan (1951), On the representation of functions by series of polynomials on closed sets (Russian), Dokl. Akad. Nauk SSSR (N. S.) 78, 405–408. Translation: Translations Amer. Math. Soc. 3 (1962), 287–293. [Famous theorem asserting that a function continuous on a compact set in the complex plane whose complement is connected, and analytic in the interior, can be uniformly approximated by polynomials.]   
H. N. Mhaskar and D. V. Pai (2000), Fundamentals of Approximation Theory, CRC/Narosa. [Extensive treatment of many topics, especially in linear approximation.] G. Mittag-Leffler (1900), Sur la repr´esentation analytique des fonctions d’une variable r´eelle, Rend. Circ. Mat. Palermo 14, 217–224. [Contains a long footnote by Phragm´en explaining how the Weierstrass approximation theorem follows from the work of Runge.] C. Moler and C. Van Loan (2003), Nineteen dubious ways to compute the exponential of a matrix, twenty-five years later, SIAM Rev. 45, 3–49. [Expanded reprinting of 1978 paper summarizing methods for computing $\exp ( A )$ , the best method being related to Pad´e approximation.]   
R. de Montessus de Ballore (1902), Sur les fractions continues alg´ebriques, Bull. Soc.

Math. France 30, 28–36. [Shows that type $( m , n )$ Pad´e approximants to meromorphic functions converge pointwise as $m \to \infty$ in a disk about $z = 0$ with exactly $_ n$ poles.]

M. Mori and M. Sugihara (2001), The double-exponential transformation in numerical analysis, J. Comput. Appl. Math. 127, 287–296. [Survey of the quadrature algorithm introduced by Takahasi & Mori 1974.]

J.-M. Muller (2006), Elementary Functions: Algorithms and Implementation, 2nd ed., Birkh¨auser. [A text on implementation of elementary functions on computers, including a chapter on the Remez algorithm.]

Y. Nakatsukasa, Z. Bai and F. Gygi (2010), Optimizing Halley’s iteration for computing the matrix polar decomposition, SIAM J. Matrix Anal. Appl. 31, 2700–2720. [Proposal of an algorithm based on a rational function of high degree generated by iteration of a simple equiripple approximation.]

Y. Nakatsukasa, O. S\`ete and L. N. Trefethen (2018), The AAA algorithm for rational approximation, SIAM J. Sci. Comput. 40, A1494–A1522. [Introduction of an adaptive method for rational approximation exploiting barycentric representations.]

I. P. Natanson (1965), Constructive Theory of Functions, 3 vols., Frederick Ungar. [This major work by a scholar in Leningrad gives equal emphasis to algebraic and trigonometric approximation.]

D. J. Newman (1964), Rational approximation to $| x |$ , Mich. Math. J. 11, 11–14. [Shows that whereas polynomial approximants to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $O ( n ^ { - 1 } )$ , for rational approximants the rate is $O ( \exp ( - C { \sqrt { n } } ) )$ ).]

D. J. Newman (1974), Rational approximation to $e ^ { - x }$ , $J$ . Approx. Th. 10, 301–303. [Shows by a lower bound $1 2 8 0 ^ { - n }$ that type $( n , n )$ rational approximants to $e ^ { x }$ on $( - \infty , 0 ]$ can converge no faster than geometrically as $n \to \infty$ in the supremum norm.]

J. Nuttall (1970), The convergence of Pad´e approximants of meromorphic functions, $J$ . Math. Anal. Appl. 31, 147–153. [Shows that type $( n , n )$ Pad´e approximants to meromorphic functions converge in measure as $n \to \infty$ , though not pointwise.]

H. O’Hara and F. J. Smith (1968), Error estimation in the Clenshaw–Curtis quadrature formula, Comput. J. 11, 213–219. [Early paper arguing that Clenshaw–Curtis and Gauss quadrature have comparable accuracy in practice.]

A. V. Oppenheim, R. W. Schafer and J. R. Buck (1999), Discrete-time Signal Processing, Prentice-Hall. [A standard textbook on the subject, which is tightly connected with polynomial and rational approximation.]

S. A. Orszag (1971a), Galerkin approximations to flows within slabs, spheres, and cylinders, Phys. Rev. Lett. 26, 1100–1103. [Orszag’s first publication on Chebyshev spectral methods.]

S. A. Orszag (1971b), Accurate solution of the Orr–Sommerfeld stability equation, J. Fluid Mech. 50, 689–703. [The most influential of Orszag’s early papers on Chebyshev spectral methods.]

R. Pachon´ (2010), Algorithms for Polynomial and Rational Approximation in the Complex Domain, DPhil thesis, U. of Oxford. [Includes chapters on rational best approximants, interpolants, and Chebyshev–Pad´e approximants and their application to exploration of functions in the complex plane.]

R. Pachon, P. Gonnet and J. Van Deun ´ (2012), Fast and stable rational interpolation in roots of unity and Chebyshev points, SIAM J. Numer. Anal. 50, 1713–1734. [Linear algebra formulation of the rational interpolation problem in a manner closely suited to computation.]

R. Pachon, R. B. Platte and L. N. Trefethen ´ (2010), Piecewise-smooth chebfuns, IMA J. Numer. Anal. 30, 898–916. [Generalization of Chebfun from single to multiple polynomial pieces, including edge detection algorithm to determine breakpoints.]

H. Pad´e (1892), Sur la repr´esentation approch´ee d’une fonction par des fractions rationelles, Annales Sci. de l’Ecole Norm. Sup. ´ 9 (suppl´ement), 3–93. [The first of many publications by Pad´e on the subject that became known as Pad´e approximation, with discussion of defect and block structure including a number of explicit examples.]

T. W. Parks and J. H. McClellan (1972), Chebyshev approximation for nonrecursive digital filters with linear phase, IEEE Trans. Circuit Theory CT-19, 189–194. [Proposes what became known as the Parks–McClellan algorithm for digital filter design, based on a barycentric formulation of the Remez algorithm for best approximation by trigonometric polynomials.]

B. N. Parlett and C. Reinsch (1969), Handbook series linear algebra: Balancing a matrix for calculation of eigenvalues and eigenvectors, Numer. Math. 13, 293–304. [Introduction of the technique of balancing a matrix by a diagonal similarity transformation that is crucial to the success of the QR algorithm.]

S. Paszkowski (1975), Numerical Applications of Chebyshev Polynomials and Series (Polish), PWN, Warsaw. [This monograph was later translated into Russian, but not English.]

K. Pearson (1920), On the Construction of Tables and on Interpolation I. Uni-variate Tables, Cambridge U. Press. [Contains as an appendix a fascinating annotated bibliography of 50 early contributions to interpolation. Pearson’s annotations are not always as polite as my own, with comments like “Not very adequate” and “A useful, but somewhat disappointing book.”]

O. Perron (1929), Die Lehre von den Kettenbr¨uchen, 2nd ed., Teubner. [This classic monograph on continued fractions, first published in 1913, was perhaps the first to identify the problem of spurious poles or Froissart doublets in Pad´e approximation. At the end of §78 a function is constructed whose type $( m , 1 )$ Pad´e approximants have poles appearing infinitely often on a dense set of points in the complex plane.]

R. Piessens (1974), Algorithm 473: Computation of Legendre series coefficients [C6], Comm. ACM 17, 25. $[ O ( n ^ { 2 } )$ algorithm for converting from Chebyshev to Legendre expansions.]

A. Pinkus (2000), Weierstrass and approximation theory, J. Approx. Th. 107, 1–66. [Detailed discussion of Weierstrass’s nowhere-differentiable function and of the Weierstrass approximation theorem and its many proofs and generalizations.]

R. B. Platte, L. N. Trefethen and A. B. J. Kuijlaars (2011), Impossibility of fast stable approximation of analytic functions from equispaced samples, SIAM Rev. 53, 308–318. [Shows that any exponentially convergent scheme for approximating analytic functions from equispaced samples in an interval must be exponentially ill-conditioned as $n \to \infty$ ; thus no approximation scheme can eliminate the Gibbs and Runge phenomena completely.]

G. Polya ´ (1933), Uber die Konvergenz von Quadraturverfahren, ¨ Math. Z. 37, 264–286. [Proves that a family of interpolating quadrature rules converges for all continuous integrands if and only if the sums of the absolute values of the weights are uniformly bounded; proves further that Newton–Cotes quadrature approximations do not always converge as $n \to \infty$ , even if the integrand is analytic.]

Ch. Pommerenke (1973), Pad´e approximants and convergence in capacity, J. Math. Anal. Appl., 41, 775–780. [Sharpens Nuttall’s result on convergence of Pad´e approximants in measure to convergence in capacity.]

J. V. Poncelet (1835), Sur la valeur approch´ee lin´eaire et rationelle des radicaux de la forme ${ \sqrt { a ^ { 2 } + b ^ { 2 } } } , { \sqrt { a ^ { 2 } - b ^ { 2 } } }$ etc., J. Reine Angew. Math. 13, 277–291. [Perhaps the very first discussion of minimax approximation.]

D. Potts, G. Steidl and M. Tasche (1998), Fast algorithms for discrete polynomial transforms, Math. Comp. 67, 1577–1590. [Algorithms for converting between Chebyshev and Legendre expansions.]

M. J. D. Powell (1981), Approximation Theory and Methods, Cambridge U. Press. [Approximation theory text with a computational emphasis, particularly strong on the Remez algorithm and on splines.]

H. A. Priestley (2003), Introduction to Complex Analysis, 2nd ed., Oxford U. Press. [Well-known introductory complex analysis textbook first published in 1985.]

I. E. Pritsker and R. S. Varga (1997), The Szeg˝o curve, zero distribution and weighted approximation, Trans. Amer. Math. Soc. 349, 4085–4105. [Analysis of the Szeg˝o curve using methods of potential theory.]

P. Rabinowitz (1969), Rough and ready error estimates in Gaussian integration of analytic functions, Comm. ACM 12, 268–270. [Derives tight bounds on accuracy of Gaussian quadrature by simple arguments.]

H.-J. Rack and M. Reimer (1982), The numerical stability of evaluation schemes for polynomials based on the Lagrange interpolation form, BIT 22, 101–107. [Proof of stability for barycentric polynomial interpolation in well-distributed point sets, later developed further by Higham 2004.]

T. Ransford (1995), Potential Theory in the Complex Plane, Cambridge U. Press. [Perhaps the only book fully devoted to this subject.]

T. Ransford (2010), Computation of logarithmic capacity, Comput. Meth. Funct. Th. 10, 555–578. [An algorithm for computing capacity of a set in the complex plane, with examples.]

E. Remes (1934a), Sur un proc´ed´e convergent d’approximations successives pour d´eterminer les polynˆomes d’approximation, Compt. Rend. Acad. Sci. 198, 2063–2065. [One of the original papers presenting the Remez algorithm.]

E. Remes (1934b), Sur le calcul effectif des polynˆomes d’approximation de Tchebichef, Compt. Rend. Acad. Sci. 199, 337–340. [The other original paper presenting the Remez algorithm.]

E. Ya. Remez (1951), On approximations in the complex domain (Russian), Dokl. Akad. Nauk SSSR 77, 965–968. [Characterizes best approximations on complex domains.]

E. Ya. Remez (1957), General computational methods of Tchebycheff approximation, Atomic Energy Commission Translation 4491, Kiev, pp. 1–85. [Remez’s summary of computational methods for best approximation.]

J. R. Rice (1969), The Approximation of Functions, Addison-Wesley. [Two volumes, the first linear and the second nonlinear.]

L. F. Richardson (1927), The deferred approach to the limit. I—single lattice. Phil. Trans. Roy. Soc. A 226, 299–349. [Systematic discussion of Richardson extrapolation, emphasizing discretizations with $O ( h ^ { 2 } )$ error behavior.]

M. Richardson and L. N. Trefethen (2011), A sinc function analogue of Chebfun, SIAM J. Sci. Comput. 33, 2519–2535. [Presents a “Sincfun” software analogue of Chebfun for dealing with functions with endpoint singularities via variable transformation and sinc function interpolants.]

F. Riesz (1918), Uber lineare Funktionalgleichungen, ¨ Acta Math. 41, 71–98. [First statement of the general existence result for best approximation from finite-dimensional linear spaces.]

M. Riesz (1916), Uber einen Satz des Herrn Serge Bernstein, ¨ Acta Math. 40, 43–47. [Gives a new proof of a Bernstein inequality based on the barycentric formula for Chebyshev points, in the process deriving the barycentric coefficients ${ \scriptstyle { \frac { 1 } { 2 } } } , - 1 , 1 , - 1 , \ldots$ half a century before Salzer 1972.]

T. J. Rivlin (1981), An Introduction to the Approximation of Functions, Dover. [Appealing short textbook originally published in 1969.]

T. J. Rivlin (1990), Chebyshev Polynomials: From Approximation Theory to Algebra and Number Theory, 2nd ed., Wiley. [Classic book on Chebyshev polynomials and applications, with first edition in 1974.]

J. D. Roberts (1980), Linear model reduction and solution of the algebraic Riccati equation by use of the sign function, Internat. J. Control 32, 677–687. [This article connecting rational functions with the sign function was written in 1971 as Technical Report CUED/B-Control/TR13 of the Cambridge University Engineering Dept.]

W. Rudin (1976), Principles of Mathematical Analysis, 3rd ed., McGraw-Hill. [Influential textbook first published in 1953.]

P. O. Runck (1962), Uber Konvergenzfragen bei Polynominterpolation mit ¨aqui ¨ distanten Knoten. II, J. Reine Angew. Math. 210, 175–204. [Analyzes the Gibbs overshoot for two varieties of polynomial interpolation of a step function.]

C. Runge (1885a), Zur Theorie der eindeutigen analytischen Functionen, Acta Math. 6, 229–244. [Publication of Runge’s theorem: a function analytic on a compact set in the complex plane whose complement is connected can be uniformly approximated by polynomials. This was later generalized by Mergelyan.]

C. Runge (1885b), Uber die Darstellung willk¨urlicher Functionen, ¨ Acta Math. 7, 387–392. [Shows that a continuous function on a finite interval can be uniformly approximated by rational functions. It was later noted by Phragm´en and Mittag-Leffler that this and the previous paper by Runge together imply the Weierstrass approximation theorem.]

C. Runge (1901), Uber empirische Funktionen und die Interpolation zwischen ¨ ¨aquidistanten Ordinaten, Z. Math. Phys. 46, 224–243. [M´eray had pointed out that polynomial interpolants might fail to converge, but it was this paper that focused on equispaced sample points, showed that divergence can take place even in the interval of interpolation, and identified the “Runge region” where analyticity is required for convergence.]

A. Ruttan (1981), The length of the alternation set as a factor in determining when a best real rational approximation is also a best complex rational approximation, J. Approx. Th. 31, 230–243. [Shows that complex best approximations are always better than real ones in the strict lower-right triangle of a square block of the Walsh table.]

A. Ruttan and R. S. Varga (1989), A unified theory for real vs. complex rational Chebyshev approximation on an interval, Trans. Amer. Math. Soc. 312, 681–697. [Shows that type $( m , m + 2 )$ complex rational approximants to real functions can be up to 3 times as accurate as real ones.]

E. B. Saff (1972), An extension of Montessus de Ballore’s theorem on the convergence of interpolating rational functions, J. Approx. Th. 6, 63–67. [Generalizes the de Montessus de Ballore theorem from Pad´e to multipoint Pad´e approximation.]

E. B. Saff and A. D. Snider (2003), Fundamentals of Complex Analysis with Applications to Engineering, Science, and Mathematics, 3rd ed., Prentice-Hall. [Widely used introductory complex analysis textbook.]

E. B. Saff and V. Totik (1997), Logarithmic Potentials with External Fields, Springer. [Presentation of connections between potential theory and rational approximation.] E. B. Saff and R. S. Varga (1978a), Nonuniqueness of best complex rational approximations to real functions on real intervals, J. Approx. Th. 23, 78–85. [Rediscovery of results of Lungu 1971.]   
E. B. Saff and R. S. Varga (1978b), On the zeros and poles of Pad´e approximants to $e ^ { z }$ . III, Numer. Math. 30, 241–266. [Analysis of the curves in the complex plane along which poles and zeros of these approximants cluster.]   
T. W. Sag and G. Szekeres (1964), Numerical evaluation of high-dimensional integrals, Math. Comp. 18, 245–253. [Introduction of changes of variables that can speed up Gauss and other quadrature formulas, even in one dimension.]   
H. E. Salzer (1955), A simple method for summing certain slowly convergent series, $J$ . Math. Phys. 33, 356–359. [“Salzer’s method” for acceleration of convergence, based on interpreting a sequence of values as samples of a function $f ( x )$ at $x _ { n } = n ^ { - 1 }$ .]   
H. E. Salzer (1972), Lagrangian interpolation at the Chebyshev points $x _ { n , \nu } = \cos ( \nu \pi / n )$ , $\nu = 0 ( 1 ) n$ ; some unnoted advantages, Computer J. 15, 156–159. [Barycentric formula for polynomial interpolation in Chebyshev points.]   
H. E. Salzer (1981), Rational interpolation using incomplete barycentric forms, $Z$ . Angew. Math. Mech. 61, 161–164. [One of the first publications to propose the use of rational interpolants defined by barycentric formulas.]   
T. Schmelzer and L. N. Trefethen (2007), Evaluating matrix functions for exponential integrators via Carath´eodory–Fej´er approximation and contour integrals, Elect. Trans. Numer. Anal. 29, 1–18. [Fast methods based on rational approximations for evaluating the $\varphi$ functions used by exponential integrators for solving stiff ODEs and PDEs.] J. R. Schmidt (1941), On the numerical solution of linear simultaneous equations by an iterative method, Philos. Mag. 32, 369–383. [Proposal of what became known as the epsilon or eta algorithm some years before Shanks 1955, Wynn 1956, and Bauer 1959.] C. Schneider and W. Werner (1986), Some new aspects of rational interpolation, Math. Comp. 47, 285–299. [Extension of barycentric formulas to rational interpolation.] A. Schonhage ¨ (1961), Fehlerfortpflanzung bei Interpolation, Numer. Math. 3, 62–71. [Independent rediscovery of results close to those of Turetskii 1940 concerning Lebesgue constants for equispaced points.]   
A. Schonhage ¨ (1971), Approximationstheorie, de Gruyter. [This monograph was unfortunately not translated into English.]   
A. Schonhage ¨ (1973), Zur rationalen Approximierbarkeit von $e ^ { - x }$ ¨uber $[ 0 , \infty )$ , J. Approx. Th. 7, 395–398. [Proves that in maximum-norm approximation of $e ^ { x }$ on $( - \infty , 0 ]$ by inversepolynomials $1 / p _ { n } ( x )$ , the optimal rate is $O ( 3 ^ { - n } )$ .]   
I. Schur (1918), Uber Potenzreihen, die im Innern des Einheitskreises besch ¨ r¨ankt sind, J. Reine Angew. Math. 148, 122–145. [Solution of the problem of Carath´eodory and Fej´er via the eigenvalue analysis of a Hankel matrix of Taylor coefficients.]   
D. Shanks (1955), Non-linear transformations of divergent and slowly convergent sequences, J. Math. Phys. 34, 1–42. [Introduction of Shanks’ method for convergence acceleration by Pad´e approximation, closely related to the epsilon algorithm of Wynn 1956.] J. Shen, T. Tang and L.-L. Wang (2011), Spectral Methods: Algorithms, Analysis and Applications, Springer. [Systematic presentation of spectral methods including convergence theory.]

B. Shiffman and S. Zelditch (2003), Equilibrium distribution of zeros of random polynomials, Int. Math. Res. Not., no. 1. [Shows that polynomials given by expansions in orthogonal polynomials with random coefficients have roots clustering near the support of the orthogonality measure.]

A. Sidi, Practical Extrapolation Methods (2003), Cambridge U. Press. [Extensive treatment of methods for acceleration of convergence.]

G. A. Sitton, C. S. Burrus, J. W. Fox and S. Treitel (2003), Factoring very-highdegree polynomials, IEEE Signal Proc. Mag. 20, 27–42. [Discussion of rootfinding for polynomials of degree up to one million by the Lindsey–Fox algorithm.]

V. I. Smirnov and N. A. Lebedev (1968), Functions of a Complex Variable: Constructive Theory, MIT Press. [Major survey of problems of polynomial and rational approximation in the complex plane.]

F. Smithies (1997), Cauchy and the Creation of Complex Function Theory, Cambridge U. Press. [Detailed account of Cauchy’s almost single-handed creation of this field from 1814 to 1831.]

M. A. Snyder (1966), Chebyshev Methods in Numerical Approximation, Prentice-Hall. [An appealing short book emphasizing rational as well as polynomial approximations.]

W. Specht (1957), Die Lage der Nullstellen eines Polynoms. III, Math. Nachr. 16, 369– 389. [Development of comrade matrices, whose eigenvalues are roots of polynomials expressed in bases of orthogonal polynomials.]

W. Specht (1960), Die Lage der Nullstellen eines Polynoms. IV, Math. Nachr. 21, 201– 222. [The final page considers colleague matrices, the special case of comrade matrices for Chebyshev polynomials. These ideas were developed independently by Good 1961.]

H. Stahl (1993), Best uniform rational approximation of $| x |$ on $[ - 1 , 1 ]$ , Russian Acad. Sci. Sb. Math. 76, 461–487. [Proof of the conjecture of Varga, Ruttan, and Carpenter that best rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $\sim 8 \exp ( - \pi { \sqrt { n } } )$ .]

H. Stahl (1997), The convergence of Pad´e approximants to functions with branch points, J. Approx. Th. 91, 139–204. [Generalizes the Nuttall–Pommerenke theorem on convergence of type $( n , n )$ Pad´e approximants to the case of functions $f$ with branch points.]

H. Stahl (1998), Spurious poles in Pad´e approximation, J. Comput. Appl. Math. 99, 511–527. [Defines and analyzes what it means for a pole of a Pad´e approximant to be spurious.]

H. R. Stahl (2003), Best uniform rational approximation of $x ^ { \alpha }$ on [0, 1], Acta Math. 190, 241–306. [Generalization of the results of the paper above to approximation of $x ^ { \alpha }$ on $[ 0 , 1 ]$ , completing earlier investigations of Ganelius and Vyacheslavov.]

H. Stahl and T. Schmelzer (2009), An extension of the “1/9”-problem, J. Comput. Appl. Math. 233, 821–834. [Announcement of numerous extensions of the “9.28903” result of Gonchar & Rakhmanov 1989 for type $( n , n )$ best approximation of $e ^ { x }$ on $( - \infty , 0 ]$ , showing that the same rate of approximation applies on compact sets in the complex plane and on Hankel contours, and that “9.28903” is also achieved on $( - \infty , 0 ]$ in type $( n , n + k )$ approximation of $e ^ { x }$ or of related functions such as $\varphi$ functions for exponential integrators.]

K.-G. Steffens (2006), The History of Approximation Theory: From Euler to Bernstein, Birkh¨auser. [Discussion of many people and results, especially of the St. Petersburg school, by a student of Natanson.]

E. M. Stein and R. Shakarchi (2005), Real Analysis: Measure Theory, Integration, and Hilbert Spaces, Princeton U. Press. [A leading textbook.]

F. Stenger (1986), Explicit nearly optimal linear rational approximation with preassigned poles, Math. Comp. 47, 225–252. [Construction of rational approximants by a method related to sinc expansions.]

F. Stenger (1993), Numerical Methods Based on Sinc and Analytic Functions, Springer. [Comprehensive treatise by the leader in sinc function algorithms.]

F. Stenger (2010), Sinc Numerical Methods, CRC Press. [A handbook of sinc methods and their implementation in the author’s software package Sinc-Pack.]

T. J. Stieltjes (1884), Quelques recherches sur la th´eorie des quadratures dites m´ecaniques, Ann. Sci. Ecole Norm. Sup. ´ 1, 409–426. [Proves that Gauss quadrature converges for any Riemann integrable integrand.]

T. J. Stieltjes (1885), Sur les polynˆomes de Jacobi, Compt. Rend. Acad. Sci. 199, 620– 622. [Shows that the roots of $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ are Fekete points (minimal-energy points) in $[ - 1 , 1 ]$ .]

J. Szabados (1970), Rational approximation to analytic functions on an inner part of the domain of analyticity, in A. Talbot, ed., Approximation Theory, Academic Press, pp. 165– 177. [Shows that for some functions analytic in a Bernstein $\rho$ -ellipse, type $( n , n )$ rational best approximations are essentially no better than degree $n$ polynomial best approximations.]

G. Szego˝ (1924), Uber eine Eigenschaft der Exponentialreihe, ¨ Sitzungsber. Berl. Math. Ges. 23, 50–64. [Shows that as $n \to \infty$ , the zeros of the normalized partial sums $s _ { n } ( n z )$ of the Taylor series of $e ^ { z }$ approach the Szeg˝o curve in the complex $z$ -plane defined by $| z e ^ { 1 - z } | = 1$ and $| z | \le 1$ .]

G. Szego˝ (1985), Orthogonal Polynomials, American Mathematical Society. [A classic monograph by the master, including chapters on polynomial interpolation and quadrature, first published in 1939.]

E. Tadmor (1986), The exponential accuracy of Fourier and Chebyshev differencing methods, SIAM J. Numer. Anal. 23, 1–10. [Presents theorems on exponential accuracy of Chebyshev interpolants of analytic functions and their derivatives.]

T. Takagi (1924), On an algebraic problem related to an analytic theorem of Carath´eodory and Fej´er and on an allied theorem of Landau, Japan J. Math. 1, 83–91 and ibid., 2 (1925), 13–17. [Beginnings of the generalization of Carath´eodory & Fej´er 1911 and Schur 1918 to rational approximation.]

H. Takahasi and M. Mori (1971), Estimation of errors in the numerical quadrature of analytic functions, Applicable Anal. 1, 201–229. [Relates the accuracy of a quadrature formula to the accuracy of an associated rational function as an approximation to $\log ( ( z + 1 ) / ( z - 1 ) )$ on a contour enclosing $[ - 1 , 1 ]$ .]

H. Takahasi and M. Mori (1974), Double exponential formulas for numerical integration, Publ. RIMS, Kyoto U. 9, 721–741. [Introduction of the double exponential or tanh-sinh quadrature rule, in which Gauss quadrature is transformed by a change of variables to another formula that can handle endpoint singularities.]

A. Talbot (1976), The uniform approximation of polynomials by polynomials of lower degree, J. Approx. Th. 17, 254–279. [A precursor to the Carath´eodory–Fej´er method.]

F. D. Tappert (1977), The parabolic approximation method, in J. B. Keller and J. S. Papadakis, eds., Wave Propagation and Underwater Acoustics, Springer, pp. 224–287. [Describes techniques for one-way acoustic wave simulation in the ocean, based on polynomial and rational approximations of a pseudodifferential operator.]

R. Taylor and V. Totik (2010), Lebesgue constants for Leja points, IMA J. Numer.

Anal. 30, 462–486. [Proves that for general sets in the complex plane, the Lebesgue constants associated with Leja points grow subexponentially.]

W. J. Taylor (1945), Method of Lagrangian curvilinear interpolation, J. Res. Nat. Bur. Stand. 35, 151–155. [The first use of the barycentric interpolation formula, for equidistant points only and without the term “barycentric,” which was introduced by Dupuy 1948.]

T. W. Tee and L. N. Trefethen (2006), A rational spectral collocation method with adaptively transformed Chebyshev grid points, SIAM J. Sci. Comput. 28, 1798– 1811. [Numerical solution of differential equations with highly nonuniform solutions using Chebyshev–Pad´e approximation, conformal maps, and spectral methods based on rational barycentric interpolants, as advocated by Berrut and coauthors.]

H. Tietze (1917), Eine Bemerkung zur Interpolation, Z. Angew. Math. Phys. 64, 74– 90. [Investigates the Lebesgue function for equidistant points, showing the local maxima decrease monotonically from the outside of the interval toward the middle.]

A. F. Timan (1951), A strengthening of Jackson’s theorem on the best approximation of continuous functions by polynomials on a finite interval of the real axis, Doklady Akad. Nauk SSSR 78, 17–20. [A theorem on polynomial approximation that recognizes the greater approximation power near the ends of the interval.]

A. F. Timan (1994), Theory of Approximation of Functions of a Real Variable, Dover. [First published in Russian in 1960.]

K.-C. Toh and L. N. Trefethen (1994), Pseudozeros of polynomials and pseudospectra of companion matrices, Numer. Math. 68, 403–425. [Analysis of stability of companion matrix eigenvalues as an algorithm for polynomial rootfinding, given a polynomial expressed by its coefficients in the monomial basis.]

L. Tonelli (1908), I polinomi d’approssimazione di Tschebychev, Annali di Mat. 15, 47–119. [Extension of results on real best approximation to the complex case.]

L. N. Trefethen (1983), Chebyshev approximation on the unit disk, in H. Werner et al., eds., Computational Aspects of Complex Analysis, D. Riedel, pp. 309–323. [An introduction to several varieties of CF approximation.]

L. N. Trefethen (1984), Square blocks and equioscillation in the Pad´e, Walsh, and CF tables, in P. R. Graves-Morris et al., eds., Rational Approximation and Interpolation, Lect. Notes in Math. 1105, Springer. [Shows that square block structure in all three tables of rational approximations arises from equioscillation-type characterizations involving the defect.]

L. N. Trefethen (2000), Spectral Methods in MATLAB, SIAM. [MATLAB-based textbook on spectral methods for ODEs and PDEs.]

L. N. Trefethen (2008), Is Gauss quadrature better than Clenshaw–Curtis?, SIAM Rev. 50, 67–87. [Shows by considering approximation properties in the complex plane that for most functions, the Clenshaw–Curtis and Gauss formulas have comparable accuracy.]

L. N. Trefethen (2010), Householder triangularization of a quasimatrix, IMA J. Numer. Anal. 30, 887–897. [Extends the Householder triangularization algorithm to quasimatrices, i.e., “matrices” whose columns are functions rather than vectors.]

L. N. Trefethen (2016), Inverse Yogiisms, Notices Amer. Math. Soc. 63, 1281–1285. [Discusses the phenomenon that mathematicians tend to say things that are literally true yet misleading, with Faber’s theorem of polynomial interpolation as an example.]

L. N. Trefethen and D. Bau, III (1997), Numerical Linear Algebra, SIAM. [A standard text, with a section “When vectors become continuous functions” at p. 52 that foreshadows Chebfun computation with quasimatrices.]

L. N. Trefethen, A. Birkisson and T. A. Driscoll ´ (2018), Exploring ODEs, SIAM. [Chebfun-based textbook.]

L. N. Trefethen and M. H. Gutknecht (1983a), Real vs. complex rational Chebyshev approximation on an interval, Trans. Amer. Math. Soc. 280, 555–561. [Shows that type $( m , n )$ complex rational approximations to a real function on an interval may be arbitrarily much better than real ones for $n \geq m + 3$ .]

L. N. Trefethen and M. H. Gutknecht (1983b), The Carath´eodory–Fej´er method for real rational approximation, SIAM J. Numer. Anal. 20, 420–436. [Introduction of real rational CF approximation, and first numerical computation of the constant 9.28903 . . . for minimax rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

L. N. Trefethen and M. H. Gutknecht (1985), On convergence and degeneracy in rational Pad´e and Chebyshev approximation, SIAM J. Math. Anal. 16, 198–210. [Proves theorems to the effect that the Pad´e approximation operator is continuous, and Pad´e approximants are limits of best approximants on regions shrinking to a point, provided that the defect is 0.]

L. N. Trefethen and M. H. Gutknecht (1987), Pad´e, stable Pad´e, and Chebyshev– Pad´e approximation, in J. C. Mason and M. G. Cox, eds., Algorithms for Approximation, Clarendon Press, pp. 227–264. [Reduces the problem of Chebyshev–Pad´e approximation to the problem of stable Pad´e approximation, that is, Pad´e approximation with a constraint on location of poles.]

L. N. Trefethen and L. Halpern (1986), Well-posedness of one-way wave equations and absorbing boundary conditions, Math. Comp. 47, 421–435. [Shows that approximations from two diagonals of the Pad´e table must be used in these applications; polynomial and other approximations are ill-posed.]

L. N. Trefethen and J. A. C. Weideman (1991), Two results concerning polynomial interpolation in equally spaced points, J. Approx. Th. 65, 247–260. [Discussion of the size of Lebesgue constants and “6 points per wavelength” for polynomial interpolation in equispaced points.]

L. N. Trefethen and J. A. C. Weideman (2014), The exponentially convergent trapezoidal rule, SIAM Rev. 56, 385–458. [Survey of uses of the periodic trapezoidal rule and its variants in numerical analysis.]

L. N. Trefethen, J. A. C. Weideman and T. Schmelzer (2006), Talbot quadratures and rational approximations, BIT Numer. Math. 46, 653–670. [Shows how integrals approximated by the trapezoidal rule correspond to rational approximations in the complex plane, with particular attention to the approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

A. H. Turetskii (1940), The bounding of polynomials prescribed at equally distributed points (Russian), Proc. Pedag. Inst. Vitebsk 3, 117–127. [Derivation of the $\sim 2 ^ { n } / e n \log n$ asymptotic size of Lebesgue constants for equispaced polynomial interpolation. This paper went largely unnoticed for fifty years and the main result was rediscovered by Sch¨onhage 1961.]

Ch.-J. de la Vall´ee Poussin (1908), Note sur l’approximation par un polynˆome d’une fonction dont la deriv´ee est \`a variation born´ee, Bull. Acad. Belg., 403–410. [Proof of the Weierstrass approximation theorem.]

Ch. de la Vall´ee Poussin (1910), Sur les polynˆomes d’approximation et la repr´esentation approch´ee d’un angle, Acad. Roy. de Belg., Bulletins de la Classe des Sci. 12. [Includes the de la Vall´ee Poussin lower bound on best approximation error.]

Ch. de la Vall´ee Poussin (1911), Sur la methode de l’approximation minimum, Annales Soc. Scient. Brux. 35, 1–16. [Rational best approximation.]

Ch. J. de la Vall´ee Poussin (1919), Le¸cons sur l’approximation des fonctions d’une variable r´eelle, Gauthier-Villars, Paris. [Monograph collecting de la Vall´ee Poussin’s results of the previous decade.]

J. Van Deun and L. N. Trefethen (2011), A robust implementation of the Carath´eodory–Fej´er method, BIT Numer. Math. 51, 1039–1050. [Twenty-five years after the original theoretical papers, a presentation of the practical details behind the Chebfun cf command.]

R. S. Varga and A. J. Carpenter (1985), On the Bernstein conjecture in approximation theory, Constr. Approx. 1, 333–348. [Shows that degree $n$ best polynomial approximants to $| x |$ have asymptotic accuracy $0 . 2 8 0 \dots n ^ { - 1 }$ rather than $0 . 2 8 2 \dots n ^ { - 1 }$ .]

R. S. Varga, A. Ruttan and A. J. Carpenter (1993), Numerical results on best uniform rational approximation of $| x |$ on $[ - 1 , 1 ]$ , Math. USSR-Sb. 74, 271–290. [Highprecision numerical calculations lead to the conjecture that best rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge asymptotically at the rate $\sim 8 \exp ( - \pi { \sqrt { n } } )$ , proved by Stahl 1993.]

N. S. Vyacheslavov (1975), On the uniform approximation of $| x |$ by rational functions, Sov. Math. Dokl. 16, 100–104. [Sharpens the result of Newman 1964 by showing that rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $O ( \exp ( - \pi { \sqrt { n } } ) )$ .]

J. Waldvogel (2006), Fast construction of the Fej´er and Clenshaw–Curtis quadrature rules, BIT Numer. Math. 46, 195–202. [Presentation of $O ( n \log n )$ algorithms for finding nodes and weights.]

H. Wallin (1972), On the convergence theory of Pad´e approximants, in Linear Operators and Approximation, Internat. Ser. Numer. Math. 20, Birkh¨auser, pp. 461–469. [Shows that there exists an entire function $f$ whose $( n , n )$ Pad´e approximants are unbounded for all $z \neq 0$ .]

J. L. Walsh (1931), The existence of rational functions of best approximation, Trans. Amer. Math. Soc. 33, 668–689. [Shows that there exists a best rational approximation of type $( m , n )$ to a given continuous function $f$ , not just on an interval such as $[ - 1 , 1 ]$ but also on more general sets in the complex plane.]

J. L. Walsh (1934), On approximation to an analytic function by rational functions of best approximation, Math. Z. 38, 163–176. [Perhaps the first discussion of what is now called the Walsh table, the table of best rational approximations to a given function $f$ for various types $( m , n )$ .]

J. L. Walsh (1959), The analogue for maximally convergent polynomials of Jentzsch’s theorem, Duke Math. J. 26, 605–616. [Shows that every point on the boundary of a region of convergence of a sequence of polynomial approximations is the limit of zeros of its partial sums.]

J. L. Walsh (1969), Interpolation and Approximation by Rational Functions in the Complex Domain, 5th ed., American Mathematical Society. [An encyclopedic but hard-to-read treatise on all kinds of material related to polynomial and rational approximation in the complex plane, originally published in 1935.]

H. Wang and S. Xiang (2012), On the convergence rates of Legendre approximation, Math. Comp. 81, 861–877. [Theorem 3.1 connects barycentric interpolation weights $\left\{ \lambda _ { k } \right\}$ and Gauss–Legendre quadrature weights $\{ w _ { k } \}$ .]

R. C. Ward (1977), Numerical computation of the matrix exponential with accuracy estimate, SIAM J. Numer. Anal. 14, 600–610. [Presentation of a scaling-and-squaring algorithm for computing the exponential of a matrix by Pad´e approximation, a form of which is used by the MATLAB expm command.]

E. Waring (1779), Problems concerning interpolations, Phil. Trans. R. Soc. 69, 59–67. [Presents the Lagrange interpolation formula 16 years before Lagrange.]

G. A. Watson (1980), Approximation Theory and Numerical Methods, Wiley. [Textbook with special attention to $L _ { 1 }$ and $L _ { p }$ norms.]

M. Webb (2013), Computing complex singularities of differential equations with Chebfun, SIAM Undergrad. Research Online 6, https://doi.org/10.1137/12S011520. [Exploration of rational approximation for locating complex singularities of numerical solutions to ODE problems including Lorenz and Lotka–Volterra equations.]

M. Webb, L. N. Trefethen and P. Gonnet (2012), Stability of barycentric interpolation formulas for extrapolation, SIAM J. Sci. Comput. 35, A3009–A3015. [Confirming the theory of Higham 2004, shows that the “type 2” barycentric interpolation formula can be dangerously unstable if used for extrapolation outside the data interval.]

J. A. C. Weideman (2003), Computing the dynamics of complex singularities of nonlinear PDEs, SIAM J. Appl. Dyn. Syst. 2, 171–186. [Applies Pad´e approximation to computed solutions of nonlinear time-dependent PDEs to estimate locations of moving poles and other singularities.]

J. A. C. Weideman and S. C. Reddy (2000), A MATLAB differentiation matrix suite, ACM Trans. Math. Softw. 26, 465–519. [A widely used collection of MATLAB programs for generating Chebyshev, Legendre, Laguerre, Hermite, Fourier, and sinc spectral differentiation matrices of arbitrary order.]

J. A. C. Weideman and L. N. Trefethen (2007a), The kink phenomenon in Fej´er and Clenshaw–Curtis quadrature, Numer. Math. 107, 707–727. [Analysis of the effect that as $n$ increases, Clenshaw–Curtis quadrature initially converges at the same rate as Gauss rather than half as fast, as commonly supposed.]

J. A. C. Weideman and L. N. Trefethen (2007b), Parabolic and hyperbolic contours for computing the Bromwich integral, Math. Comp. 76 (2007), 1341–1356. [Derivation of geometrically convergent “Talbot contour”–type rational approximations for problems related to $e ^ { x }$ on $( - \infty , 0 ]$ .]

K. Weierstrass (1872), Uber continuierliche Functionen eines reellen Arguments, ¨ die f¨ur keinen Werth des letzteren einen bestimmten Differentialquotienten besitzen, K¨onigliche Akademie der Wissenschaften, 18 July 1872. [Weierstrass’s publication of an example (which he had lectured on a decade earlier) of a continuous, nowhere-differentiable function.]

K. Weierstrass (1885), Uber die analytische Darstellbarkeit sogenannter willk¨u ¨ rlicher Functionen einer reellen Ver¨anderlichen, Sitzungsberichte der Akademie zu Berlin, 633–639 and 789–805. [Presentation of the Weierstrass approximation theorem.]

B. D. Welfert (1997), Generation of pseudospectral differentiation matrices I, SIAM J. Numer. Anal. 34, 1640–1657. [Derivation of stable recursive formulas for computation of derivatives of interpolants.]

E. J. Weniger (1989), Nonlinear sequence transformations for the acceleration of convergence and the summation of divergent series, Computer Phys. Rep. 10, 189–371 (also available as arXiv:math/0306302v1, 2003). [Extensive survey.]

H. Werner (1964), On the rational Tschebyscheff operator, Math. Z. 86, 317–326. [Shows that the operator mapping a real function $f \in C [ - 1 , 1 ]$ to its best real rational approximation of type $( m , n )$ is continuous if and only if $f$ is itself rational of type $( m , n )$ or its best approximation has defect 0 (“nondegenerate”).]

H. Wilbraham (1848), On a certain periodic function, Cambridge and Dublin Math. J. 3, 198–201. [Analyzes the Gibbs phenomenon fifty years before Gibbs.]

J. H. Wilkinson (1984), The perfidious polynomial, in G. H. Golub, ed., Studies in Numerical Analysis, Mathematical Association of America. [Wilkinson’s major work on polynomials was in the 1960s, but this entertaining review, which won the Chauvenet Prize of the Mathematical Association of America in 1987, remains noteworthy not least because of its memorable title.]   
J. Wimp (1981), Sequence Transformations and their Applications, Academic Press. [Monograph on many methods for acceleration of convergence.]   
C. Winston (1934), On mechanical quadratures formulae involving the classical orthogonal polynomials, Ann. Math. 35, 658–677. [States a general connection between Gauss– Jacobi quadrature weights and Lagrange polynomials.]   
P. Wynn (1956), On a device for computing the $e _ { m } ( S _ { n } )$ transformation, Math. Comp. 10, 91–96. [Wynn’s first of many papers about the epsilon algorithm for acceleration of convergence of sequences.]   
S. Xiang and F. Bornemann (2012), On the convergence rates of Gauss and Clenshaw– Curtis quadrature for functions of limited regularity, SIAM J. Numer. Anal. 50, 2581–2587. [Shows that Gauss and Clenshaw–Curtis quadrature formulas converge by one factor of $n$ faster than one might expect. See also Freud 1955.]   
K. Xu and N. Hale (2016) Explicit construction of rectangular differentiation matrices, IMA J. Numer. Anal. 36, 618–632. [Explicit formulas for the rectangular differentiation matrices of Driscoll & Hale 2015 and Aurentz & Trefethen 2017a.]   
K. Zhou, J. C. Doyle and K. Glover (1996), Robust and Optimal Control, Prentice-Hall. [A leading textbook on optimal control, with special attention to approximation issues.]   
W. P. Ziemer (1989), Weakly Differentiable Functions, Springer. [Includes a definition of total variation in the measure theoretic context.]


<!-- chunk 0006: pages 351-359 -->
# Index

0.28016949902. . . , 53, 210   
0.52552491457. . . , 99   
0.68391378641. . . , 259–260   
1.06578388826. . . , 65   
1.17897974447. . . , 68–69   
1.28228345577. . . , 65   
9.28902549192. . . , 214–216, 220

AAA algorithm, x–xi, 36   
absolute continuity, 51–52, 147   
absolute convergence, 17, 27, 158, 162, 181   
abs( $_ { x }$ ), 22, 47, 50–51, 53, 62, 73, 75, 78, 118, 122, 140, 182–184, 192, 209– 214   
Adamjan–Arov–Krein approximation, 162, 194   
Airy equation, 172, 192   
Aitken extrapolation, 193, 258, 262   
algorithm, 3, 197, 254   
aliasing, 25–31, 93, 150, 268   
aliasing formula, 27   
alternant, 74, 77, 200, 206   
analytic continuation, 3, 56, 59, 62, 83, 94, 121, 159, 177, 182, 193, 197, 251–262, 269   
analytic function, 3, 16–17, 25, 43, 46, 55–62, 82–87, 90–101, 106, 115– 116, 120, 146, 182–186, 191–195, 210, 212, 244, 247, 253, 257–258, 261, 264–269   
analytic part, 159   
approximation, multivariate, 3, 44   
approximation theory, 1–5, 14, 49, 63, 117, 143, 189–198, 215   
Arnoldi iteration, 127, 194   
asymptotic series, 261   
ATAPformats, 2   
backward stability, 39, see also stability   
balancing, 139, 141   
barycentric interpolation formula, 4, 33– 41, 70, 104, 187, 266 and ill-conditioning, 102 and Remez algorithm, 77 first, 77 for Chebyshev polynomials, 40 for Legendre points, 40, 125, 152 for rational functions, 40, 195, 224 for roots of unity, x, 40 in the literature, 106 stability, 38–39, 105, 122 weights, 102   
Battles, Zachary, 4, 9, 137   
Bernstein, Sergei, 2, 14, 44, 49, 53, 55–62, 109, 209 ellipse, 56, 62, 93, 94, 121, 140, 142, 177–179, 191, 193, 251, 269 inequality, 60–61 lethargy theorem, 78 polynomial, 44, 47, 62, 79, 153 theorem(s), 60, 62, 210   
Berrut, Jean-Paul, 4, 33, 36, 41, 195   
Bessel function, 23, 138, 192   
best approximation, 1, 49, 73–79, 117, 266 operator, continuity of, 78, 205 operator, nonlinearity of, 78, 119 strong uniqueness of, 78   
Birkisson, Asgeir, x, 4, 173, 174 ´   
Blatt–Saff theorem, x, 79, 105, 140–141, 219, 252   
Borel, Emile, 2, 74 ´   
Bornemann, Folkmar, x, 4, 35, 151, 174, 257, 261, 268   
bounded variation, see variation   
Boyd, John, 136, 137, 174, 197, 270   
branches and branch points, 59, 61, 92, 193, 195, 230, 247, 260   
capacity, 40, 92–94 convergence in, 247   
cardinal function, 232   
cardinal polynomial, 33, 63, 66, 70, 107, 114   
Cauchy, Augustin-Louis, 3–4, 34, 82–83, 221, 236 integral, 86, 165, 195 integral formula, 17–18 interpolation problem, 225   
central dogma of approximation theory, 49   
Ces\`aro means, 44, 47   
cf, 2, 155–163, 191   
CF (Carath´eodory–Fej´er) approximation, 4, 155–163, 215, 219, 262   
chebellipseplot, 2, 60–61, 140, 252   
Chebfun, x, 1–5, 9, 263 and chebfun, 15 constructor, 20 ellipse, 60 Guide, 5, 22, 86   
chebfunpref, 30   
chebop, 167–175   
chebpade, 2, 251   
chebpoly, 2, 14, 19, 135   
chebpts, 2, 8, 11, 115   
chebtest, 4   
Chebyshev, Pafnuty, 2, 14, 73, 74, 123, 329

approximation, 73 coefficients, 57, 158 expansion, see Chebyshev series extreme points, 8 grid, see Chebyshev points interpolant, 7–12, 25–31, 264 interpolation, 1, 133, 158 points, 7–12, 14, 109, 264 points of the first kind, 11, 115 points of the second kind, 8 polynomials, 13–23, 62, 105, 175, 268 projection, 25–31 series, ix, 13–23, 33, 93, 133, 139, 158, 217 technology, ix, 2 Chebyshev–Pad´e approximation, 193, 247 Clenshaw, Charles, 2, 145 Clenshaw’s algorithm, 23 Clenshaw–Curtis quadrature, 4, 143–153, 267–269 coanalytic part, 159 Cody, W. J., 77, 192–194, 214 colleague matrix, 4, 15, 133–142, 148, 197, 270 compact operator, 162 set, complex, 93, 220, 247 set, real, 2, 43, 46, 204 set of functions, 74, 78, 202–203 companion matrix, 133 complex approximation, 20, 46, 61, 93, 193–195, 199, 247, 251 existence and uniqueness, 74 of $| x |$ , 219 of $\exp ( x )$ , 142, 220 of real functions, 206 on the imaginary axis, 194 on the unit disk, 163, 193 complex variables, 2, 14, 81, 101 compressed sensing, 3 comrade matrix, 135, 141, 148 conditioning, 22, 39–40, 62, 101–102, 104–105, 115, 133, 175, 217, 270 confluent nodes, 82, 86, 116 conjugate gradient iteration, 62 continued fractions, 144, 195, 236, 248– 249, 261 contour integral, 2, 81, 215 conv, 2, 45 convergence acceleration, 3, 193, 257–262 convolution, 43–46

cos(x), 46, 56, 136–137, 163, 183–184,   
237, 244–246   
cosh(x), 23   
cumsum, 2, 47, 76, 157   
defect, 199–207, 228, 236–242, 248   
deficiency, 240–241   
degenerate rational approximation, 199,   
205, 232, 237   
diff, 2, 51, 65, 129, 166–173, 185   
differential equations, 3, 101, 104, 131,   
165–175   
differentiation matrix, x, 166–175   
diffusion equation, 43, 194   
digital filters, 77, 193, 197   
Dirac delta function, 91   
discontinuity, 3, 46, 69–71, 193, 233   
divergent series, 261–262   
downsampling, 20   
Driscoll, Toby, x, 4, 171   
Driscoll–Hale discretization, 171–175

edge detection, 174   
eigenvalue problem, 15, 133–141, 148, 153, 158–162, 174, 193, 197, 254, 270   
Elliott, David, 2, 155, 174   
entire function, 43, 46–47, 56, 60–61, 100   
epsilon algorithm, 193, 258, 262   
equilibrium measure, 91–94   
equioscillation, 74–79, 119, 160–163, 196, 199–207, 213, 217, 221, 236–237, 248, 267   
equiripple approximation, 73   
equispaced points, 40, 95–102, 106, 109, 187, 264   
error curve, 40, 73   
eta extrapolation, see epsilon algorithm   
Euler, Leonhard, 34, 67, 70, 257, 261–262, 271   
Euler’s constant, 109, 116   
even function, 22, 23, 75, 78, 127, 131, 201, 205, 206, 213, 237, 244, 258   
exp(x), 75, 78, 142, 169, 194, 197, 207, 214–220, 224, 248, 262   
exponential function, see exp(x) integral, 192 integrators, 195 of a matrix, 194   
extrap, 259–262   
extrapolation of sequences and series, see convergence acceleration   
Faber’s theorem, 46, 79, 108, 264   
Fej´er, Lip´ot, 44, 47 points, 93   
Fekete points, 93–94, 130   
FFT (Fast Fourier Transform), 14, 16, 20–21, 30, 125, 145–146, 174, 226, 244, 257, 271   
Floater–Hormann interpolation, 36, 41, 195   
floating point arithmetic, see rounding errors   
fluid mechanics, 174, 178   
formal power series, 235, 249   
forward stability, 39, see also stability   
Fourier, Joseph, 13, 69 analysis, 2, 11, 17, 49, 70, 271 coefficients, 226, 232 polynomials, see trigonometric polynomials projection, 67, 115 series, ix–x, 67–69, 104, 174 spectral methods, 174 transform, 195, see also FFT   
Fox, Leslie, 2, 174   
fractal, 46   
Fr´echet derivative, 173   
Fredholm alternative, 204   
Froissart doublets, 223, 244, 247   
FUNPACK, 192   
gamma function, 192, 198   
Gauss, Carl Friedrich, 143–144, 195, 236   
Gauss–Chebyshev points, 11   
Gauss quadrature, 1, 4, 123, 143–153, 185–187, 195, 236, 267–270 Glaser–Liu–Rokhlin algorithm, 148, 268 Golub–Welsch algorithm, 129, 148, 152–153 Hale–Townsend algorithm, 129, 148– 149   
Gaussian kernel, 43–47   
Gegenbauer polynomials, 91, 124   
geometric mean distance, 9, 11–12, 41, 90, 93, 99, 101   
Gibbs, Josiah Willard, 67, 69   
Gibbs phenomenon, 63–71, 114 for Fourier series, 70 for projection, 67 rational, 232   
global optimization, 139   
Golub, Gene, 214   
Gonchar and Rakhmanov, 195, 206, 215, 217   
Gonnet, Pedro, 4, 39, 77, 137, 221–233, 235, 241   
Good, Jack, 2, 136, 197   
Gragg, William, 248   
greedy algorithm, 40, 93   
Green’s function, 91–93   
Gutknecht, Martin, 4, 155–163, 206, 214– 215, 238, 241, 248   
G¨uttel, Stefan, 4, 194, 235, 242   
$H _ { \infty }$ approximation, 162, 194   
Haar condition, 74   
Hale, Nick, x, 4, 152, 171, 177–187, 195, 214, 269, see also Driscoll–Hale discretization and Gauss quadrature, Hale–Townsend algorithm   
Halphen’s constant, 215, 219   
Hankel matrix, 155–162   
hat function, 99   
heat equation, see diffusion equation   
Hermite, Charles, 236 integral formula, xi, 3–4, 35, 81–87, 90, 94–95, 165 interpolation problem, 86   
Hermite–Fej´er interpolation, 44, 47   
hermpts, 152   
Higham, Nicholas, 4, 35, 38–39, 194, 214, 266   
Hilbert, David, 49, 74, 196   
IEEE arithmetic, 39–40   
ill-posed problem, 196, 223, 253   
inner product, 22, 123, 144   
integral, 152   
interpolation, 3, 25, 103–106 rational, see rational interpolation   
interpolatory quadrature, 144, 153   
interp1, x, 2, 34, 36, 40, 47, 96, 110, 130, 187   
'interval', 64   
inverse iteration, 193–194   
Jackson, Dunham, 2, 8, 44, 49, 53–54, 109, 209   
Jackson theorems, 51   
Jacobi, Carl Gustav Jacob, 4, 33, 35, 83, 123, 144, 190, 195, 221, 224, 236, 329 matrix, 4, 148, 153 polynomials, 91, 94, 124, 129–130 weight function, 124   
Jacobian matrix, 173   
jacpts, 94, 152   
Jentzsch’s theorem, x, 141   
Joukowsky map, 56   
Kirchberger, Paul, 3, 74, 78, 196–197   
Kosloff and Tal-Ezer, 177, 186, 269   
Kronecker delta function, 63, 70, 232   
Krylov iteration, 194   
Lagrange, Joseph-Louis, 34, 236, 271 interpolation formula, 3, 33–35, 103, 107, 265, 271   
Lagrange polynomial, see cardinal polynomial   
Lanczos, Cornelius, 2, 174 iteration, 127, 254   
Landau, Edmund, 44, 49, 115 constants, 115   
Laplace equation, xi, 90, 92, 194   
Laplace transform, 194, 215   
LATEX, 2, 5   
Laurent coefficient, 17, 160, 226 polynomial, 13, 70, 159 series, ix, 17, 23   
lazy evaluation, 168, 173   
least-squares rational approximation linearized, 4, 193, 199, 221–233, 251– 262 nonlinear, 262   
lebesgue, 2, 111   
Lebesgue, Henri, 44, 47, 49, 53, 209 constant, 1, 63, 105, 107–122, 129– 130 function, 107–116, 129 integrable, 51   
Lebesgue–Stieltjes integral, 91   
Legendre extreme points, 129, 130 points, 9, 11, 21, 40, 125, 264 polynomials, 21, 91, 124, 141, 148   
legpoly, 2, 124–129, 141   
legpts, 2, 11, 40, 129, 148–152, 185   
Leja points, 93–94   
length, 19   
lethargy theorem, 78, 207   
linear programming, 77   
linop, 168   
Lipschitz continuous, 2, 16–18, 21, 25, 27, 47, 54, 67, 78, 158, 161, 181, 264   
$\log ( x )$ , 248   
logarithmic

capacity, see capacity

potential, see potential machine precision, 11, 19, 23, 30–31, 44, 54, 62, 100, 133, 155, 162, 170, 228, 224 see also IEEE arithmetic and rounding errors 'map', 186 Markov inequality, 22 MATLAB, x, 1–5, 133, 148, 265 matrix computations, 104, 127, 193 max, 64 maximally convergent, 94, 121, 140 maximum modulus principle, 61 M´eray, Charles, 95 Mergelyan’s theorem, 46 meromorphic function, 247 minandmax, 11 minimax, 2, 73, 76, 117–120, 122, 155– 161, 184, 191–192, 200–202, 210, 213, 217–218, 251 minimax approximation, 73, 121, 199, 214 see also best approximation 'minsamples', 30 model reduction, 194, 197 monomial basis, 15–16, 21–22, 26, 105, 133, 270 de Montessus de Ballore theorem, 247 near-best, 1, 108, 117–122, 155 Newman, Donald, xi, 192–193, 211, 215 Newton, Isaac, 33 interpolation formula, 33, 106, 265 iteration, 148–149, 172–173, 219, 263 Newton–Cotes quadrature, 101, 143, 267–268 node polynomial, 30, 34, 37, 81, 89, 94, 152 nonexistence, 221, 232 nonlinearity, 77–78, 115, 119, 172–175, 177, 189–198, 238, 262, 266 nonuniqueness, 175, 206 norm, 2, 139 norm, 2, 11 normal, 205, 248 odd function, 22–23, 75, 131, 147, 201, 205, 237, 254 one-way wave equation, 195, 197 optimal control, 194 optimal interpolation points, 2, 93, 109, 116, 122 order star, 248

orthogonal polynomials, 15, 22, 35, 91, 123–131, 135, 141, 144, 270   
orthonormal polynomials, 124, 131   
overflow, 36–40   
Pach´on, Ricardo, 4, 73, 77, 174, 201, 221– 233, 241, 256–257   
padeapprox, 2, 236, 243, 257, 259   
Pad´e approximation, 4, 193–195, 203, 235–249, 251–262 algorithm, 242–243 multipoint, 247, 257 operator, 238 table, 237, see also square blocks   
Painlev´e equation, 175   
Parks–McClellan algorithm, 77   
partial fractions, 83, 189–190, 198, 219   
PDEs (partial differential equations), 194, 197   
Phragm´en, Lars Edvard, 43   
Platte, Rodrigo, 4, 174   
Platte–Trefethen–Kuijlaars theorem, 115, 187   
plotcoeffs, x, 20   
Poincar´e, Henri, 70   
poles, x, 23, 87, 193, 197, 198, 251   
pole-zero pair, see Froissart doublet   
poly, 2   
P´olya, Georg, 101, 151, 153, 268   
polyfit and polyval, 2, 39, 105, 265   
polynomial part, 191   
Poncelet, Jean-Victor, 73, 214   
potential, 91 theory, xi, 4, 9, 81, 89–95, 201, 215   
power method, 193   
principal part, 191   
projection, 25, 31, 108, 115   
pseudodifferential operator, 195   
publish, 1, 2, 5   
QR algorithm, 139, 194   
QR decomposition, 131   
quadrature, 3, 101, 123, 143–153, 195, 197, 263–271 Clenshaw–Curtis, see Clenshaw– Curtis quadrature and rational approximation, 195, 209 Gauss, see Gauss quadrature interpolatory, 144 Newton–Cotes, see Newton–Cotes quadrature Romberg, 258

tanh-sinh, 177 transformed, 185–187 quasimatrix, 22, 126, 131

radial basis functions, 3   
random data, 10–11, 109 interpolation points, 84, 116 polynomials, 142 sample points, 229, 231 walk, 44, 47, 122   
rank, 229   
ratdisk, 226, 229, 251   
ratinterp, 2, 223–224, 231–233, 251–257   
rational approximation, x–xi, 150, 162, 189– 262 function, 36, 40, 91, 189–198 interpolation, 235   
recurrence relation, 15, 127, 131–135, 141, 153, 167, 236, 261   
recursion, 137   
regularization, 247, 253   
Remez algorithm, 1, 77, 192, 206, 211, 215, 266   
Richardson, Mark, 4, 177   
Richardson extrapolation, 78, 193, 210, 257–258, 262   
Riesz, Frigyes, 75   
Riesz, Marcel, 4, 33, 36   
Riesz Representation Theorem, 152   
Robin constant, 92–93   
Romberg quadrature, 258   
rootfinding, 3, 133–142, 139, 197   
roots, 2, 77, 101, 105, 128–129, 133, 136– 142, 224, 271   
roots of unity, 7, 14, 26, 30, 40, 224–227, 235, 257   
Rouch´e’s theorem, 163   
rounding errors, 8, 11, 20, 38, 55–56, 84, 86, 100–101, 103, 105, 118, 122, 131, 141, 151, 156, 167, 224–226, 228, 232, 241–243, 247, 265, 270   
Runge, Carl, x, xi, 3, 43, 95, 98, 101, 196– 197, 264 function, 11, 55, 58, 60, 79, 96, 104, 106–107, 142, 187, 265, 269 phenomenon, 95–102, 105, 112, 151, 187, 264, 268 region, 99 theorem, 46   
Ruttan, Arden, 206, 211, 215   
Saff, Edward, 17, 79, 89, 91, 142, 206, 215, 247   
Salzer, Herbert, 33, 36, 195, 266 extrapolation, 258, 260   
sausage region, 179   
scale-invariance, 36   
scribble, 177   
sech(x), 78, 138, 147   
self-adjoint, 127   
sequences and series, 193   
Shanks extrapolation, 258, 262, see also epsilon algorithm   
SIAM 100-Digit Challenge, 257   
$\mathrm { s i g n } ( x )$ , 22, 40, 53, 63   
Simpson’s rule, 151, 185   
$\sin ( x )$ , 166, 197   
$\sin ( 1 / x )$ , 45, 47   
$\sin ^ { - 1 } ( x )$ , 178   
sinc function, 101, 177   
sine integral, 68, 71   
singularities, x–xi, 189, 191   
$\sinh ( x )$ , 23   
SPECFUN, 192   
Specht, Wilhelm, 133, 135, 270   
special functions, 77, 192   
spectral methods, 165–175 adaptive, 195 collocation and Galerkin, 166 Fourier and Chebyshev, 174 naming of, 174   
spline, 2   
splines, 3, 54, 69, 71, 104, 106   
spurious pole, see Froissart doublet   
sqrt(x), 213   
square blocks in Pad´e table, 205, 237, 240, 242, 244– 248 in Walsh table, 205   
stability, 39, 105, 141   
Stahl, Herbert, 91, 211, 215, 220, 247   
Stenger, Frank, 177, 211   
stiff PDEs, 194–195, 197   
Stigler’s law, 3   
Stirling’s formula, 47   
strong uniqueness, 78   
sum, 30, 69, 141, 146, 148   
SVD (singular value decomposition), 4, 22, 158, 159, 221, 224–232, 241   
Szeg˝o curve, 142   
$\tan ( x )$ , 61   
tanh(x), 22, 27–31, 37, 58–61, 105, 198, 251–257, 262   
Taylor series, ix, 16, 46–47, 101, 141, 235, 238, 261   
Tee, Teik Wynn, 36, 186, 195   
Toeplitz matrix, 226, 232, 238–239   
total variation, see variation   
Townsend, Alex, 4, see also Gauss quadrature, Hale–Townsend algorithm   
transfinite diameter, 92–93   
trapezoidal rule, 212, 215, 219, 258   
trigonometric approximation, 70 functions, 197 identity, 198 interpolation, 50, 65, 70, 174 polynomials, 13–14, 70, 123 projection, 67 series, 69   
'trunc', 29, 31, 68   
truncation, see projection   
Turetskii, A. H., 109, 116   
Turing, Alan, 134, 270   
tv, 51   
type of a rational function, 189, 199, 235 exact, 190, 200

ultraspherical, see Gegenbauer   
unattainable point, 225   
unbounded domain, 189–198   
underflow, 36–40   
uniform convergence, 17, 21, 43–48, 247   
uniformly distributed, 94

unit circle, 7, 11, 13–21, 26, 52, 57, 70, 133, 159–163, 193, 224, 228–232, 257, 270   
de la Vall´ee Poussin, Charles, 2, 44, 49, 53, 54, 119, 200, 209 lower bound, 78, 207   
Vandermonde matrix, 39, 105, 265   
Varga, Richard, 53, 195, 206, 211, 215   
variation, 51, 52, 54   
Waldvogel algorithm, 145–146, 268   
Wallis, John, 33   
Walsh, Joseph, 89, 200, 203, 206, 238 table, 199, 205–206, 237 theorem, x, 105, 140–141, 252   
Waring, Edward, 3, 34, 271   
wavelets, 3   
Weideman, J. A. C., 4, 109, 150, 167, 215, 219, 256   
Weierstrass, Karl, 43, 46, 60 approximation theorem, 1, 43–48, 69, 79, 153, 264 M-test, 47, 60 nondifferentiable function, 46, 54, 78, 116   
weight function, 15, 22, 123–131, 143   
Wilbraham, Henry, 3, 67–70   
Wilkinson, James, 105, 133, 270   
zerofinding, see rootfinding   
zeta function, 260, 262   
Zolotarev, Yegor Ivanovich, 212

# Key Formulas for Polynomials

Waring (1779), Lagrange (1795) (1) ${ \mathrm { N o d e ~ p o l y n o m i a l : ~ } } \ell ( x ) = \prod _ { k = 0 } ^ { n } ( x - x _ { k } )$ (5.4) Jacobi (1825) From (1) (2) Barycentric weights: λj = 1ℓ′(x ) (5.7)   
M. Riesz (1916), Salzer (1972)From (1) and (2) (3) ${ \mathrm { C h e b y s h e v ~ c a s e } } \colon \lambda _ { j } = { \frac { 2 ^ { n - 1 } } { n } } ( - 1 ) ^ { j } .$ , halved for $j = 0 , n$ (5.14) Jacobi (1825)From (1) and (2) (5.8) (4) ${ \mathrm { L a g r a n g e ~ p o l y n o m i a l ~ a t ~ } } x _ { j } \colon \ell _ { j } ( x ) = \ell ( x ) { \frac { \lambda _ { j } } { x - x _ { j } } }$ From (4) (5) $\mathrm { 1 s t ~ b a r y c e n t r i c ~ f o r m u l a : } ~ p ( x ) = \ell ( x ) \sum _ { j = 0 } ^ { n } \frac { \lambda _ { j } } { x - x _ { j } } f _ { j }$ (5.9) Dupuy (1948)From (5) (6) ${ \mathrm { 2 n d ~ b a r y c e n t r i c ~ f o r m u l a : ~ } } p ( x ) = \sum _ { j = 0 } ^ { n } { \frac { \lambda _ { j } f _ { j } } { x - x _ { j } } } \left. \sum _ { j = 0 } ^ { n } { \frac { \lambda _ { j } } { x - x _ { j } } } \right.$ (5.11)   
Cauchy (1826), Hermite (1878) From (5) (7) ${ \mathrm { H e r m i t e ~ i n t e g r a l : ~ } } f ( x ) - p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) } { \ell ( t ) } } { \frac { f ( t ) } { ( t - x ) } } d t$   
Newton (1687), Cotes (1722)From (4) (8) ${ \mathrm { Q u a d r a t u r e : ~ } } I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) , \quad w _ { k } = \int _ { - 1 } ^ { 1 } \ell _ { k } ( x ) d x$ (19.3), (19.4) Winston (1934)p. 152 (9) Gauss–Jacobi quadrature weights: $w _ { k } = \frac { C } { ( 1 - x _ { k } ^ { 2 } ) [ \ell ^ { \prime } ( x _ { k } ) ] ^ { 2 } }$ Wang and Xiang (2012) From (2) and (9) (10) $\mathrm { L i n k ~ t o ~ b a r y c e n t r i c ~ w e i g h t s : ~ } \lambda _ { k } = C ( - 1 ) ^ { k } \sqrt { ( 1 - x _ { k } ^ { 2 } ) w _ { k } }$ (19.13)   
ellman, Kashef and Casti (1972) From (4) (11) ${ \mathrm { S p e c t r a l ~ d i f f } } ^ { \prime } { \mathrm { n } } \colon D _ { i j } = \ell _ { j } ^ { \prime } ( x _ { i } ) = { \frac { \lambda _ { j } } { \lambda _ { i } ( x _ { i } - x _ { j } ) } } ; \ { \frac { x _ { j } } { 1 - x _ { j } ^ { 2 } } } { \mathrm { i f } } \ i = j$

The Runge phenomenon follows from (7), as does exponential convergence of Chebyshev interpolants and Gauss or Clenshaw–Curtis quadrature for analytic functions.
