# Chapter 26. Rational Interpolation and Linearized Least-Squares

For polynomials, we have emphasized that although best approximations with their equioscillating error curves are fascinating, Chebyshev interpolants or projections are just as good for most applications and simpler to compute since the problem is linear. To some degree at least, the same is true of rational functions. Best rational approximations are fascinating, but for practical purposes, it is often a better idea to use rational interpolants, and again an important part of the problem is linear since one can multiply through by the denominator.

But there is a big difference. Rational interpolation problems are not entirely linear, and unlike polynomial interpolation problems, they suffer from both nonexistence and discontinuous dependence on data in some settings. To use rational interpolants effectively, one must formulate the problem in a way that minimizes such effects. The method we shall recommend for this, here and in the next two chapters, makes use of the singular value decomposition (SVD) and the generalization of the linearized interpolation problem to one of least-squares fitting. This approach originates in [Pach´on, Gonnet & Van Deun 2012] and [Gonnet, Pach´on $\&$ Trefethen 2011]. The literature of rational interpolation goes back to Cauchy [1821] and Jacobi [1846], but much of it is rather far from computational practice.

Here is an example to illustrate the difficulties. Suppose we seek a rational function $r \in \mathcal { R } _ { 1 1 }$ satisfying the conditions

$$
r ( - 1 ) = 2 , \quad r ( 0 ) = 1 , \quad r ( 1 ) = 2 .
$$

Since a function in $\mathcal { R } _ { 1 1 }$ is determined by three parameters, the count appears right for this problem to be solvable. In fact, however, there is no solution, and one can prove this by showing that if a function in $\mathcal { R } _ { 1 1 }$ takes equal values at two points,

it must be a constant (Exercise 26.1). We conclude that solutions to seemingly sensible rational interpolation problems do not always exist.

Let us modify the problem and seek a function $r \in \mathcal { R } _ { 1 1 }$ satisfying the conditions

$$
r ( - 1 ) = 1 + \varepsilon , \quad r ( 0 ) = 1 , \quad r ( 1 ) = 1 + 2 \varepsilon ,
$$

where $\varepsilon$ is a parameter. Now there is a solution for any $\varepsilon$ , namely

$$
r ( x ) = 1 + \frac { \frac { 4 } { 3 } \varepsilon x } { x - \frac { 1 } { 3 } } .
$$

However, this is not quite the smooth interpolant one might have hoped for. Here is the picture for $\varepsilon = 0 . 1$ :

$$
\begin{array} { l } { \mathrm {  ~ x ~ = ~ c h e b f u n ( \bar { ~ } x ^ { \prime } ) ~ } ; \mathrm {  ~ r ~ = ~ } \emptyset \left( \mathrm { e p } \right) \mathrm {  ~ 1 ~ } + \mathrm {  ~ \left( 4 / 3 \right) } { * \mathrm { e p } ^ { * } \mathrm { x } } / \left( \mathrm { x } - \left( \mathrm { 1 / 3 } \right) \right) ; } \\ { \mathrm { e p } = \mathrm {  ~ 0 ~ } . 1 ; \mathrm {  ~ p l o t } \left( \mathrm { r \left( e p \right) } \right) , \mathrm { \ h o l d ~ o n ~ } } \\ { \mathrm { p l o t } \mathrm {  ~ ( } \mathrm { [ - 1 ~ } \mathrm {  ~ 0 ~ } \mathrm {  ~ 1 ] ~ } , \mathrm { \mathrm { [ 1 + e p ~ 1 ~ } ~ 1 + 2 * \mathrm { e p ] ~ } , \mathrm {  ~ \cdot ~ } } . \mathrm { k } ^ { \prime } \mathrm {  ~ ) } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a922a6a33d1513ea97ca77179498ae0ea8d3af9c3f468ab44336e55886904154.jpg)

And here it is for $\varepsilon = 0 . 0 0 1$ :

$\mathtt { e p } \ = \ 0 . 0 0 1$ ; plot(r(ep)), hold on plot([-1 0 1],[1+ep 1 1+2\*ep],'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/14fcd2d1f524126e58fc09f801506da302bdcb986693054316d462fa9f43d8ca.jpg)

Looking back at the formula (26.3), we see that for any nonzero value of $\varepsilon$ , this function has a pole at $x = 1 / 3$ . When $\varepsilon$ is small, the effect of the pole is quite localized, and we may confirm this by calculating that the residue is $( 4 / 9 ) \varepsilon$ . Another way to interpret the local effect of the pole is to note that $r$ has a zero at a distance just $O ( \varepsilon )$ from the pole:

$$
\begin{array} { r } { \mathrm { p o l e : ~ } x = \frac { 1 } { 3 } , \qquad \mathrm { z e r o : ~ } x = \frac { 1 } { 3 } / ( 1 + \frac { 4 } { 3 } \varepsilon ) . } \end{array}
$$

For $| x - { \textstyle \frac { 1 } { 3 } } | \gg \varepsilon$ , the pole and the zero will effectively cancel. This example shows that even when a rational interpolation problem has a unique solution, the problem may be ill-posed in the sense that the solution depends discontinuously on the data. For $\varepsilon = 0$ , (26.3) reduces to the constant $r = 1$ , whereas for any nonzero $\varepsilon$ there is a pole, though it seems to have little to do with approximating the data. Such poles are often called spurious poles. Since a spurious pole is typically associated with a nearby zero that approximately cancels its effect further away, another term is Froissart doublet, named after the physicist Marcel Froissart [Froissart 1969]. We may also say that the function has a spurious pole-zero pair.

Here is an example somewhat closer to practical approximation. Consider the function $f ( x ) = \cos ( e ^ { x } )$ ,

and suppose we want to construct rational interpolants of type $( n , n )$ to $f$ based on samples at $2 n + 1$ Chebyshev points in $[ - 1 , 1 ]$ . Chebfun has a command ratinterp that will do this, and here is a table of the maximum errors obtained by ratinterp for $n = 1 , 2 , \ldots , 6$ :

for $\mathrm { ~ n ~ } = \mathrm { ~ 1 { : } ~ 6 ~ }$

$\begin{array} { l } { { \mathrm { [ p , q ] ~ = ~ r a t i n t e r p ( f , n , n ) ; ~ e r r ~ = ~ n o r m ( f \mathrm { - } p / q , i n f ) ; } } } \\ { { \mathrm { f p r i n t f ( \mathrm { ' } \phantom { n } ( \% 1 { \mathrm { d } } , \% 1 d ) ~ \% 7 . 2 e \setminus n \mathrm { " } , n , n , e r r ) } } } \end{array}$ end

We seem to have very fast convergence, but what has gone wrong with the type $( 3 , 3 )$ approximant? A plot reveals that the problem is a spurious pole:

[p,q] = ratinterp(f,3,3); plot(p/q), hold on xx = chebpts(7); plot(xx,f(xx),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6106bef17cdb2ef9e4ddc7b1c1fa17ba59233a3d0c78594b0b722f14a9aa8059.jpg)

One might suspect that this artifact has something to do with rounding errors on the computer, but it is not so. The spurious pole is in the mathematics, with residue equal to about $- 0 . 0 0 1 3$ .

In other examples, on the other hand, spurious poles do indeed arise from rounding errors. In fact, they appear very commonly when one aims for approximations with accuracy close to machine precision. Here, for example, is a numerically computed interpolant of type $( 8 , 8 )$ to $e ^ { x }$ in 21 Chebyshev points:

[p,q] = ratinterp(exp(x),8,8,[],[],0); plot(p/q), hold on xx $=$ chebpts(21); plot(xx,exp(xx),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/1b9092b88f30bc9b2a7360d60f3bd92612fab5957831c18369de3f6d6c17311d.jpg)

The picture looks fine, but that is only because Chebfun has failed to detect that $p / q$ has a spurious pole-zero pair:

spurious_zero $=$ roots(p), spurious_pole $=$ roots(q)

spurious_zero $=$ 0.819870673405979   
spurious_pole $=$ 0.819870673405979

One could attempt to get around this particular pathology by computing in higher-precision arithmetic. However, quite apart from the practical difficulties of high-precision arithmetic, that approach would not really address the challenges of rational interpolation at a deeper level. The better response is to adjust the formulation of the rational interpolation problem so as to make it more robust. In this last example, it seems clear that a good algorithm should be sensible enough to reduce the number of computed poles. We now show how this can be done systematically with the SVD.

At this point, we shall change settings. Logically, we would now proceed to develop a robust rational interpolation strategy on $[ - 1 , 1 ]$ . However, that route would require us to combine new ideas related to robustness with the complexities of Chebyshev points, Chebyshev polynomials, and rational barycentric interpolation formulas. Instead, now and for most of the rest of the book, we shall move from the real interval $[ - 1 , 1 ]$ to the unit disk and switch variable names from $x$ to $z$ . This will make the presentation simpler, and it fits with the fact that many applications of rational interpolants and approximants involve complex variables.

Specifically, here is the problem addressed in the remainder of this chapter, following [Pach´on, Gonnet & Van Deun 2012] and [Gonnet, Pach´on & Trefethen 2011] but with origins as far back as Jacobi [1846]. Suppose $f$ is a function defined on the unit circle in the complex plane and we consider its values $f ( z _ { j } )$ at the $( N + 1 ) \mathrm { s t }$ roots of unity for some $N \geq 0$ ,

$$
z _ { j } = e ^ { 2 \pi i j / ( N + 1 ) } , \quad 0 \le j \le N .
$$

Using this information, how can we construct a good approximation $r \in \mathcal { R } _ { m n }$ ? We assume for the moment that $m$ , $n$ , and $N$ are related by $N = m + n$ . The parameter count is then right for an interpolant $r = p / q$ satisfying

$$
\frac { p ( z _ { j } ) } { q ( z _ { j } ) } = f ( z _ { j } ) , \quad 0 \leq j \leq N .
$$

The problem of finding such a function $r$ is known as the Cauchy interpolation problem. As we have seen, however, a solution does not always exist.

Our first step toward greater robustness will be to linearize the problem and seek polynomials $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ such that

$$
p ( z _ { j } ) = f ( z _ { j } ) q ( z _ { j } ) , \quad 0 \leq j \leq N .
$$

By itself, this set of equations isn’t very useful, because it has the trivial solution $p = q = 0$ . Some kind of normalization is needed, and for this we introduce the representations

$$
p ( z ) = \sum _ { k = 0 } ^ { m } a _ { k } z ^ { k } , \qquad q ( z ) = \sum _ { k = 0 } ^ { n } b _ { k } z ^ { k }
$$

with

$$
\mathbf { a } = ( a _ { 0 } , \ldots , a _ { m } ) ^ { T } , \qquad \mathbf { b } = ( b _ { 0 } , \ldots , b _ { n } ) ^ { T } .
$$

Our normalization will be the condition

$$
\| \mathbf { b } \| = 1 ,
$$

where $\| \cdot \|$ is the standard 2-norm on vectors,

$$
\| \mathbf { b } \| = \left( \sum _ { k = 0 } ^ { n } | b _ { k } | ^ { 2 } \right) ^ { 1 / 2 } ,
$$

and similarly for vectors of dimensions other than $n + 1$ . Our linearized rational interpolation problem consists of solving the two equations (26.5)–(26.6). A solution with $q ( z _ { j } ) \neq 0$ for all $j$ will also satisfy (26.4), but if $q ( z _ { j } ) = 0$ for some $j$ , then (26.4) may or may not be satisfied. A point where it is not attained is called an unattainable point.

We turn (26.5)–(26.6) into a matrix problem as follows. Given an arbitrary $( n { + } 1 )$ -vector $\mathbf { b }$ , there is a corresponding polynomial $q \in \mathcal { P } _ { n }$ , which we may evaluate at the $( N + 1 ) \mathrm { { ; } }$ st roots of unity $\{ z _ { j } \}$ . Multiplying by the values $f ( z _ { j } )$ gives a set of $N + 1$ numbers $f ( z _ { j } ) q ( z _ { j } )$ . There is a unique polynomial $\hat { p } \in \mathcal { P } _ { N }$ that interpolates these data,

$$
\begin{array} { r } { \hat { p } ( z _ { j } ) = f ( z _ { j } ) q ( z _ { j } ) , \quad 0 \leq j \leq N . } \end{array}
$$

Let $\hat { p }$ be written as

$$
\hat { p } ( z ) = \sum _ { k = 0 } ^ { N } \hat { a } _ { k } z ^ { k } , \quad \hat { \mathbf { a } } = ( \hat { a } _ { 0 } , \ldots , \hat { a } _ { N } ) ^ { T } .
$$

Then $\hat { \bf a }$ is a linear function of $\mathbf { b }$ , and we may accordingly express it as the product

$$
\hat { \mathbf { a } } = \hat { C } \mathbf { b } ,
$$

where $\hat { C }$ is a rectangular matrix of dimensions $( N + 1 ) \times ( n + 1 )$ depending on $f$ . It can be shown that $\hat { C }$ is a Toeplitz matrix with entries given by the discrete Laurent or Fourier coefficients

$$
c _ { j k } = \frac { 1 } { N + 1 } \sum _ { \ell = 0 } ^ { N } z _ { \ell } ^ { k - j } f ( z _ { \ell } ) .
$$

And now we can solve (26.5)–(26.6). Let $\bar { C }$ be the $n \times ( n + 1 )$ matrix consisting of the last $n$ rows of $\hat { C }$ . Since $\tilde { C }$ has more columns than rows, it has a nontrivial null vector, and for $\mathbf { b }$ we take any such null vector normalized to length 1:

$$
\tilde { C } { \bf b } = 0 , \quad \| { \bf b } \| = 1 .
$$

The corresponding vector $\hat { \mathbf { a } } = \hat { C } \mathbf { b }$ is equal to zero in positions $m + 1$ through $N$ , and we take $\mathbf { a }$ to be the remaining, initial portion of $\hat { \bf a }$ : $a _ { j } = { \hat { a } } _ { j }$ , $0 \leq j \leq m$ . In matrix form we can write this as

$$
\mathbf { a } = C \mathbf { b } ,
$$

where $C$ is the $( m + 1 ) \times ( n + 1 )$ matrix consisting of the first $m + 1$ rows of $\hat { C }$ .   
Equations (26.8)–(26.9) constitute a solution to (26.5)–(26.6).

In a numerical implementation of the algorithm just described, the operations should properly be combined into a MATLAB function, and a function like this called ratdisk is presented in [Gonnet, Pach´on & Trefethen 2011]. Here, however, for the sake of in-line presentation, we shall achieve the necessary effect with a string of anonymous functions.

The first step is to construct the Toeplitz matrix $\hat { C }$ using the MATLAB fft command. The real command below eliminates imaginary parts at the level of rounding errors and would need to be removed for a function $f$ that was not real on the real axis.

$$
\begin{array} { r l } & { \mathrm { \bf ~ f ~ j ~ = ~ \boldsymbol { \mathfrak { Q } } \left( \mathbf { \mathfrak { f } } , \boldsymbol { \mathbb { N } } \right) ~ \ f ~ ( e x p \left( 2 i \ast p \mathbf { i } \ast \left( 0 : \mathbb { N } \right) \cdot \big / \left( \mathbb { N } + 1 \right) \right) ) ~ ; } } \\ & { \mathrm { \bf ~ e x t r a c t ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { A } } , I , \mathbf { J } \right) ~ \ A \left( \mathbf { \bar { I } } , \mathbf { J } \right) ~ ; } } \\ & { \mathrm { \bf ~ c o l u m n ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \boldsymbol { \mathbb { N } } \right) ~ \ r e a l \left( \mathbf { \bar { f } } \mathbf { f } \left( \mathbf { f } \left( \mathbf { f } , \mathbb { N } \right) \right) \right) / \left( \mathbb { N } + 1 \right) ~ ; } } \\ & { \mathrm { \bf ~ r o w ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \mathbf { n } , \mathbb { N } \right) ~ \ e x t r a c t \left( c o l u m n \left( \mathbf { \bar { f } } , \mathbb { N } \right) ~ , \left[ \mathbf { \bar { \lambda } } \mathbb { N } + 1 : - 1 : \mathbb { N } + 2 - \mathbf { n } \right] ~ , 1 \right) ; } } \\ &  \mathrm { \bf ~ { \boldsymbol ~ C h a t ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \mathbf { n } , \mathbb { N } \right) ~ \ t o e p \mathbf { \bar { \lambda } } i \ t z \left( c o l u m n \left( \mathbf { \bar { f } } , \mathbb { N } \right) , \mathbf { r o w } \left( \mathbf { \bar { f } } , \mathbf { n } , \mathbb { N } \right) \right) ~ ; } } \end{array}
$$

Next we extract the submatrices $\tilde { C }$ and $C$ :

Ctilde $\mathbf { \delta } = \mathbf { \delta } \otimes ( \mathbf { f _ { \delta } } , \mathbf { m } , \mathbf { n } , \mathbf { N } )$ extract(Chat(f,n,N),m+2:N+1,:);   
$\bar { \mathrm { ~ C ~ } } = \mathrm { ~ \textcircled ~ { ~ 2 ~ } ~ } ( \mathrm { ~ f ~ } , \mathrm { ~ m ~ } , \mathrm { ~ n ~ } , \mathrm { ~ N ~ } )$ extract(Chat(f,n,N),1:m+1,:);

Finally we compute the vector $\mathbf { b }$ using the MATLAB null command, which makes use of the SVD, and multiply by $C$ to get a:

$$
\begin{array} { r l r } & { \mathbf { q } } & { = \ \odot \left( \mathbf { f } \ , \mathtt { m } , \mathbf { n } , \mathtt { N } \right) \ \mathrm { n u l 1 } \left( \mathbf { C t i } 1 \mathrm { d e } \left( \mathbf { f } \ , \mathtt { m } , \mathbf { n } , \mathtt { N } \right) \right) ; } \\ & { \mathbf { p } } & { = \ \odot \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) \ \mathbf { C } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) * \mathbf { q } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) ; } \end{array}
$$

For example, here are the coefficients of the type $( 2 , 2 )$ interpolant to $e ^ { z }$ in the 5th roots of unity:

$\textbf { f } = \mathbb { Q } \left( \boldsymbol { z } \right)$ exp(z); ${ \mathfrak { m } } = { \mathfrak { 2 } }$ ; $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ 2 ~ }$ ; N = m+n;   
pp = p(f,m,n,N), qq = q(f,m,n,N)   
pp = -0.893131422200046 -0.446418130422149 -0.074390723603151   
qq $=$ -0.891891822763679 0.446093473426966 -0.074361209330862

The zeros lie in the left half-plane and the poles in the right half-plane (cf. Exercise 18.5):

rzeros $=$ roots(flipud(pp)), rpoles $=$ roots(flipud(qq))   
rzeros $=$ -3.000495954331878 + 1.732909565613550i -3.000495954331878 - 1.732909565613550i   
rpoles $=$ $\mathrm { 2 . 9 9 9 5 0 3 8 9 0 8 1 3 0 2 2 \ + \ 1 . 7 3 1 1 9 1 2 6 0 7 6 7 6 8 4 i }$ 2.999503890813022 - 1.731191260767684i

Here are the values of the interpolant at $z = 0$ and $z = 2$ , which one can see are not too far from $e ^ { 0 }$ and $e ^ { 2 }$ :

$\textbf { r } = \~ \Theta ( z )$ polyval(flipud(pp),z)./polyval(flipud(qq),z);   
approximation $=$ r([0 2]), exact $=$ exp([0 2])   
approximation $=$ 1.001389854021227 7.011719966971134   
exact $=$ 1.000000000000000 7.389056098930650

Now let us take stock. We have derived an algorithm for computing rational interpolants based on the linearized formula (26.5), but we have not yet dealt with spurious poles. Indeed, the solution developed so far has neither uniqueness nor continuous dependence on data. It is time to take our second step toward greater robustness, again relying on the SVD.

An example will illustrate what needs to be done. Suppose that instead of a type $( 2 , 2 )$ interpolant to $e ^ { z }$ in 5 points, we want a type $( 8 , 8 )$ interpolant in 17 points. (This is like the type $( 8 , 8 )$ interpolant computed earlier, but now in roots of unity rather than Chebyshev points.) Here is what we find:

$\mathtt { m \_ s } \mathtt { n \_ n } = 8 ; \mathtt { n \_ w } = 8 ; \mathtt { N \_ m } = \mathtt { m \_ m } + \mathtt { n \_ p p } = \mathtt { p } ( \mathtt { f \_ m } , \mathtt { n } , \mathtt { n } ) , \mathtt { q } \mathtt { q } = \mathtt { q } ( \mathtt { f \_ m } , \mathtt { n } , \mathtt { n } , \mathtt { N } )$   
pp = -0.1447 -0.9818

-1.0170 -0.7967  
-0.4901 -0.2675  
-0.1118 -0.0517  
-0.0155 -0.0065  
-0.0014 -0.0006  
-0.0001 -0.0000  
-0.0000 -0.0000  
-0.0000 -0.0000  
qq =  
-0.1447 -0.9818  
-0.8723 0.1851  
0.4546 0.0383  
-0.1062 -0.0189  
0.0148 0.0033  
-0.0013 -0.0003  
0.0001 0.0000  
-0.0000 -0.0000  
0.0000 0.0000

Instead of the expected vectors a and $\mathbf { b }$ , we have matrices of dimension $9 \times 2$ , and the reason is that $\tilde { C }$ has a nullspace of dimension 2. This would not be true in exact arithmetic, but it is true in 16-digit floating point arithmetic. If we construct an interpolant from one of these vectors, it will have a spurious pole-zero pair. Here is an illustration, showing that the spurious pole (cross) and zero (circle) are near the unit circle, which is typical. The other seven nonspurious poles and zeros have moduli about 10 times larger.

rpoles $=$ roots(flipud(pp(:,1))); rzeros $=$ roots(flipud(qq(:,1))); plot(exp(2i\*pi\*x)), hold on, plot(rpoles,'xk'), plot(rzeros,'or')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/25663588c0e4aa5ac6fa3523a12e349e59e7f04b3d3313e5134364a4ae233645.jpg)

Having identified the problem, we can fix it as follows. If $\bar { C }$ has rank $n - d$ for some $d \geq 1$ , then it has a nullspace of dimension $d + 1$ . (We intentionally use the same letter $d$ as was used to denote the defect in Chapter 24.) There must exist a vector $\mathbf { b }$ in this nullspace whose final $d$ entries are zero. We could do some linear algebra to construct this vector, but a simpler approach is to reduce $m$ and $n$ by $d$ and $N$ by $2 d$ and compute the interpolant again. Here is a function for computing $d$ with the help of the MATLAB rank command, which is based on the SVD. The tolerance $1 0 ^ { - 1 2 }$ ensures that contributions close to machine precision are discarded.

$\mathsf { d } \ = \ \odot ( \mathtt { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } )$ n-rank(Ctilde(f,m,n,N),1e-12);

We redefine q and $\mathtt { p }$ to use this information:

$$
\begin{array} { r l } { \mathbf { q } } & { = \mathbf { \Phi } \odot ( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ) \mathrm { n u l l } \left( \mathbf { C } \mathbf { t } \mathrm { i } 1 \mathtt { d } \mathbf { e } \left( \mathbf { f } \ , \mathtt { m } \mathrm { - } \mathtt { d } , \mathtt { n } \mathrm { - } \mathtt { d } , \mathtt { N } \mathrm { - } 2 \ast \mathtt { d } \right) \right) ; } \\ { \mathbf { p } } & { = \mathbf { \Phi } \odot ( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ) \mathbf { C } ( \mathbf { f } \ , \mathtt { m } \mathrm { - } \mathtt { d } , \mathtt { n } \mathrm { - } \mathtt { d } , \mathtt { N } \mathrm { - } 2 \ast \mathtt { d } ) \ast \mathbf { q } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } \right) ; } \end{array}
$$

Our example now gives vectors instead of matrices, with no spurious poles.

$$
\begin{array} { r l } & { \mathrm { p p ~ = ~ \ p ( f , m , n , n , d ( f , m , n , n ) ) ~ , ~ } \ q \mathrm { q } = \ q ( \mathbf { f } , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ( \mathbf { f } , \mathtt { m } , \mathtt { n } , \mathtt { N } ) ) } \end{array}
$$

pp qq  
-0.889761508242969 -0.889761508242815  
-0.444881276259238 0.444880231983654  
-0.101109523962203 -0.101109001824429  
-0.013481293296385 0.013481177243356  
-0.001123443568826 -0.001123429053792  
-0.000056172338563 0.000056171300326  
-0.000001337441819 -0.000001337407096

This type $( 7 , 7 )$ rational function approximates $e ^ { z }$ to approximately machine precision in the unit disk. To verify this loosely, we write a function error that measures the maximum of $| f ( z ) - r ( z ) |$ over 1000 random points in the disk:

$\textbf { r } = \~ \Theta \left( z \right)$ polyval(flipud(pp),z)./polyval(flipud(qq),z); $_ z =$ sqrt(rand(1000,1)).\*exp(2i\*pi\*rand(1000,1)); error $=$ $\mathbf { \Sigma } ( \boldsymbol { \mathfrak { Q } } ( \mathbf { f } , \mathbf { r } )$ norm(f(z)-r(z),inf); error(f,r)

# ans $=$ 7.520010650629788e-13

Mathematically, in exact arithmetic, the trick of reducing $m$ and $n$ by $d$ restores uniqueness and continuous dependence on data, making the rational interpolation problem well-posed. On a computer, we do the same but rely on finite tolerances to remove contributions from singular values close to machine epsilon. A much more careful version of this algorithm can be found in the MATLAB code ratdisk from [Gonnet, Pach´on & Trefethen 2011], mentioned earlier.

We conclude this chapter by taking a third step toward robustness. So far, we have spoken only of interpolation, where the number of data values exactly matches the number of parameters in the fit. In some approximation problems, however, it may be better to have more data than parameters and perform a least-squares fit. This is one of those situations, and in particular, a least-squares formulation will reduce the likelihood of obtaining poles in the region near the unit circle where one is hoping for good approximation. This is why we have included the parameter $N$ throughout the derivation of the last six pages. We will now consider the situation $N > m + n$ . Typical choices for practical applications might be $N = 2 ( m + n )$ or $N = 4 ( m + n )$ .

Given an $( n + 1 )$ -vector $\mathbf { b }$ and corresponding function $q$ , we have already defined $\| \mathbf b \|$ as the usual 2-norm. For the function $q$ , let us now define

$$
\| q \| _ { N } = ( N + 1 ) ^ { - 1 / 2 } \Big ( \sum _ { j = 0 } ^ { N } | q ( z _ { j } ) | ^ { 2 } \Big ) ^ { 1 / 2 } ,
$$

a weighted 2-norm of the values of $q ( z )$ over the unit circle. So long as $N \geq n$ , the two norms are equal:

$$
\| q \| _ { N } = \| \mathbf { b } \| .
$$

The norm $\| \cdot \| _ { N }$ , however, applies to any function, not just a polynomial. In particular, our linearized least-squares rational approximation problem is this generalization of (26.5)–(26.6):

$$
\| p - f q \| _ { N } = \mathrm { { m i n i m u m } , \quad } \| q \| _ { N } = 1 .
$$

The algorithm we have derived for interpolation solves this problem too. What changes is that the matrix $\tilde { C }$ , of dimension $( N - m ) \times ( n + 1 )$ , may no longer have a null vector. If its singular values are $\sigma _ { 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n + 1 } \geq 0$ , then the minimum error will be

$$
\| p - f q \| _ { N } = \sigma _ { n + 1 } ,
$$

which may be positive or zero. If $\sigma _ { n } > \sigma _ { n + 1 }$ , $\mathbf { b }$ is obtained from the corresponding singular vector and that is all there is to it. If

$$
\sigma _ { n - d } > \sigma _ { n - d + 1 } = \cdot \cdot \cdot = \sigma _ { n + 1 }
$$

for some $d \geq 1$ , then the minimum singular space is of dimension $d + 1$ , and as before, we reduce $m$ and $n$ by $d$ . The parameter $N$ can be left unchanged, so $f$ does not need to be evaluated at any new points.

For example, let $f$ be the function $f ( z ) = \log ( 1 . 4 4 - z ^ { 2 } )$ ,

$$
\textbf { f } = \textsf { Q } ( \mathbf { z } ) \ \log \left( 1 . 4 4 \mathbf { - } \mathbf { z } \cdot \mathbf { \hat { \mu } } ^ { - } 2 \right) ;
$$

with branch points at $\pm 1 . 2$ , and suppose we want a type $( 4 0 , 4 0 )$ least-squares approximant with $N = 4 0 0$ . The approximation delivered by the SVD algorithm comes out with exact type (18, 18):

$$
\begin{array} { r l } & { \mathfrak { m } = 4 0 ; \ \mathfrak { n } = 4 0 ; \ \mathbb { N } = 4 0 0 ; } \\ & { \mathrm { p p } = \mathfrak { p } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathfrak { N } , \mathsf { d } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathbb { N } ) ) ; \ \mathbf { q } \mathbf { q } = \mathbf { q } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathbb { N } , \mathsf { d } ( \mathbf { f } , \mathfrak { m } , \mathbf { n } , \mathbb { N } ) ) ; } \\ & { \mathfrak { m } \equiv 1 \mathrm { e n g t h } ( \mathtt { p p } ) - 1 ; \ \mathtt { n u } = \mathbf { \lambda } \mathrm { e n g t h } ( \mathbf { q } \mathbf { q } ) - 1 ; } \\ & { \mathbf { f p r i n t f } ( \mathbf { \lambda } ^ { \prime } \qquad \mathfrak { m u } = \sqrt [ \gamma _ { 0 } ] { \mathsf { d } } \mathbf { \lambda } \qquad \mathtt { n u } = \sqrt [ \gamma _ { 0 } ] { \mathsf { d } } \mathsf { N } ^ { \prime } , \mathtt { m u } , \mathtt { n u } ) } \end{array}
$$

$$
\mathrm { \ m u } \ = \ 1 8 \qquad \mathrm { \ n u } \ = \ 1 8
$$

The accuracy in the unit disk is good (Exercise 26.4):

$\textbf { r } = \textsf { Q } ( \boldsymbol { z } )$ polyval(flipud(pp),z)./polyval(flipud(qq),z); error(f,r)

ans $=$ 6.884478705857767e-12

Here are the poles:

rpoles $=$ roots(flipud(qq)); plot(exp(2i\*pi\*x)), hold on, plot(rpoles+1e-10i,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/142436d8ae81686bec488fb2dbd84abd731ed2b398484f2e3c8c1f924e3a220a.jpg)

For comparison, suppose we revert to the original definitions of the anonymous functions $\mathrm { \Delta p }$ and q, with no removal of negligible singular values:

$\mathbf { q _ { \lambda } } = \mathbf { \lambda } \otimes ( \mathbf { f _ { \lambda } } , \mathbf { m _ { \lambda } } , \mathbf { n _ { \lambda } } , \mathbf { N } )$ null(Ctilde(f,m,n,N));   
p = @(f,m,n,N) C(f,m,n,N)\*q(f,m,n,N);

Now the computation comes out with exact type $( 4 0 , 4 0 )$ , and half the poles are spurious:

$\mathtt { m } ~ = ~ 4 0$ ; $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ 4 0 ~ }$ ; $\tt { N } = \tt { 4 0 0 }$ ;   
pp = p(f,m,n,N); pp = pp(:,end); qq = q(f,m,n,N); qq = qq(:,end); rpoles $=$ roots(flipud(qq)); hold off, plot(exp(2i\*pi\*x)), hold on plot(rpoles+1e-10i,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/76e29bad9d92b0d67373adc66181e0f71c55da1721c330fdb4b1cabebd163a94.jpg)

The error looks excellent,

$\mathbf { r } ~ = ~ \mathbb { Q } \left( \mathbf { z } \right)$ polyval(flipud(pp),z)./polyval(flipud(qq),z); error(f,r)

ans = 1.632044892792071e-14

but in fact it is not so good. Because of the spurious poles, the maximum error in the unit disk is actually infinite, but this has gone undetected at the 1000 random sample points used by the error command.

In closing this chapter we return for a moment to the variable $x$ on the interval $[ - 1 , 1 ]$ . Earlier we used the Chebfun command ratinterp to compute a type $( 8 , 8 )$ interpolant to $e ^ { x }$ in Chebyshev points and found that it had a spurious pole-zero pair introduced by rounding errors. This computation was one of pure interpolation, with no SVD-related safeguards of the kind described in the last few pages. However, ratinterp is actually designed to incorporate SVD robustness by default.

The earlier computation called ratinterp(exp(x),8,8,[],[],0) in order to force a certain SVD tolerance to be 0 instead of the default $1 0 ^ { - 1 4 }$ . If we repeat the computation with the default robustness turned on, we find that an approximation of exact type $( 8 , 4 )$ is returned and it has no spurious pole and zero:

[p,q,rh,mu,nu] $=$ ratinterp(exp(x),8,8); mu, nu spurious_zero $=$ roots(p), spurious_pole $=$ roots(q)

$\mathtt { m u } \ = \ 8$   
nu = 4   
spurious_zero $=$ Empty matrix: 0-by-1   
spurious_pole $=$ Empty matrix: 0-by-1

Summary of Chapter 26. Generically, there exists a unique type $( m , n )$ rational interpolant through $m + n + 1$ data points, but such interpolants do not always exist, depend discontinuously on the data, and exhibit spurious pole-zero pairs both in exact arithmetic and even more commonly in floating point arithmetic. They can be computed by solving a matrix problem involving a Toeplitz matrix of discrete Fourier coefficients. Uniqueness, continuous dependence, and avoidance of spurious poles can be achieved by reducing $m$ and $n$ when the minimal singular value of this matrix is multiple. It may also be helpful to oversample and solve a least-squares problem.

Exercise 26.1. Nonexistence of certain interpolants. Show that if a function in $\mathcal { R } _ { 1 1 }$ takes equal values at two points, it must be a constant.

Exercise 26.2. An invalid argument. We saw that the type $( 3 , 3 )$ interpolant to $\cos ( e ^ { x } )$ in 7 Chebyshev points has a pole near $x = 0 . 6$ . What is the flaw in the following argument? (Spell it out carefully; don’t just give a word or two.) The interpolant through these 7 data values can be regarded as a combination of cardinal functions, i.e., type $( 3 , 3 )$ rational interpolants through Kronecker delta functions supported at each of the data points. If the sum has a pole at $x _ { 0 }$ , then one of the cardinal interpolants must have a pole at $x _ { 0 }$ . So type $( 3 , 3 )$ rational interpolants to almost every set of data at these 7 points will have a pole at exactly the same place.

Exercise 26.3. Explicit example of degeneracy. Following the example (26.2)–(26.3), but now on the unit circle, let $r$ be the type $( 1 , 1 )$ rational function satisfying $r ( 1 ) = 1$ , $r ( \omega ) = 1 + i \varepsilon$ , $r ( \overline { { \omega } } ) = 1 - i \varepsilon$ , where $\omega$ is the cube root of 1 in the upper half-plane and $\varepsilon > 0$ is a parameter. (a) What is $r$ ? (b) What is the $2 \times 3$ matrix $\hat { C }$ of (26.7)? (c) How do the singular values of $\hat { C }$ behave as $\varepsilon  0$ ?

Exercise 26.4. Rational vs. polynomial approximation. The final computational example of this chapter considered type $( n , n )$ rational approximation of $f ( z ) = \log ( 1 . 4 4 -$ $z ^ { 2 }$ ) with $n = 4 0$ , which was reduced to $n = 1 8$ by the robust algorithm. For degree $2 n$ polynomial approximation, one would expect accuracy of order $O ( \rho ^ { - 2 n } )$ , where $\rho$ is the radius of convergence of the Taylor series of $f$ at $z = 0$ . How large would $n$ need to be for this figure to be comparable to the observed accuracy of $1 0 ^ { - 1 1 }$ ?

Exercise 26.5. Rational Gibbs phenomenon (from [Pach´on 2010, Sect. 5.1]). We saw in Chapter 9 that if $f ( x ) = \mathrm { s i g n } ( x )$ is interpolated by polynomials in Chebyshev points in $[ - 1 , 1 ]$ , the errors decay inverse-linearly with distance from the discontinuity. Use ratinterp to explore the analogous rates of decay for type $( m , 2 )$ and $( m , 4 )$ linearized rational interpolants to the same function, keeping $m$ odd for simplicity. What do the decay rates appear to be?

Exercise 26.6. A function with two rows of poles. After Theorem 22.1 we considered as an example the function $f ( x ) = ( 2 + \cos ( 2 0 x + 1 ) ) ^ { - 1 }$ . (a) Call ratinterp with $( m , n ) =$ (100, 20) to determine a rational approximation $r$ to $f$ on $[ - 1 , 1 ]$ with up to 20 poles. How many poles does $r$ in fact have, and what are they? (b) Determine analytically the full set of poles of $f$ and produce a plot of the approximations from (a) together with the nearby poles of $f$ . How accurate are these approximations?
