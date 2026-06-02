(This formula is perhaps due to Roberts [1980], though the essence of the matter dates to Zolotarev in the 1870s.) The change of variables $t = e ^ { s }$ , $d t = e ^ { s } d s$ converts this to

$$
| x | = \frac { 2 x ^ { 2 } } { \pi } \int _ { - \infty } ^ { \infty } \frac { e ^ { s } d s } { e ^ { 2 s } + x ^ { 2 } } ,
$$

which is an attractive integral to work with because the integrand decays exponentially as $| s | \to \infty$ . We now get a rational approximation of $| x |$ by approximating this integral by the trapezoidal rule with node spacing $h > 0$ :

$$
r ( x ) = \frac { 2 h x ^ { 2 } } { \pi } \sum _ { k = - ( n - 2 ) / 4 } ^ { ( n - 2 ) / 4 } \frac { e ^ { k h } } { e ^ { 2 k h } + x ^ { 2 } } .
$$

Here $n$ is a positive even number, and there are $n / 2$ terms in the sum, so $r ( x )$ is a rational function of $x$ of type $( n , n )$ . There are two sources of error that make $r ( x )$ differ from $| x |$ . The fact that the sum has been terminated at a limit $n < \infty$ introduces an error on the order of $e ^ { - n h / 4 }$ , and the finite step size $h > 0$ introduces an error on the order of $e ^ { - \pi ^ { 2 } / h }$ . (The integrand is analytic in the strip around the real $s$ -axis of half-width $a = \pi / 2$ , corresponding to a convergence rate $e ^ { - 2 \pi a / h }$ .) Balancing these sources of error suggests the condition $e ^ { - n h / 4 } \approx e ^ { - \pi ^ { 2 } / h }$ , that is,

$$
h \approx 2 \pi / { \sqrt { n } } ,
$$

with error of order

$$
e ^ { - ( \pi / 2 ) { \sqrt { n } } } .
$$

We can see these approximations with an experiment.

$$
\mathrm { ~ \bf ~ r ~ } = \mathrm { ~ \bf ~ r ~ } + \mathrm { ~ \bf ~ e x p } ( \mathrm { k } * \mathrm { h } ) / ( \mathrm { e x p } ( 2 * \mathrm { k } * \mathrm { h } ) + \mathrm { \bf x } ^ { \sim } 2 ) ;
$$

![](images/cb2cc26b80ce5a52caaed3b5c6470377411b761de70ff44511665e1fddcc7b45.jpg)

![](images/becf66a58b9e5c05e1a7583a0cfa870af25b853b965c729413383fe622ae605f.jpg)

The poles of (25.7)–(25.8) in the $x$ -plane lie at

$$
\pm i e ^ { 2 \pi k / { \sqrt { n } } } .
$$

Here are these numbers (those in the upper half-plane) for the six approximations plotted above, showing the wide range of amplitudes associated with the exponential spacing.

for $\texttt { n } = \texttt { 2 } : 2 : 1 2$ $\mathrm { ~ h ~ = ~ 2 ^ { * } p i / s q r t { ( n ) } ; ~ k ~ = ~ - { ( n - 2 ) / 4 } : { ( n - 2 ) / 4 } ; ~ y ~ = ~ \exp { ( k * h ) } ~ ; }$ fprintf('%8.2ei ',y)   
end   
Poles of rational approximants to |x|:   
$1 . 0 0 \mathsf { e } ^ { + 0 0 \dot { 1 } }$   
2.08e-01i 4.81e+00i   
7.69e-02i 1.00e+00i 1.30e+01i   
3.57e-02i 3.29e-01i 3.04e+00i 2.80e+01i   
1.88e-02i 1.37e-01i 1.00e+00i 7.29e+00i 5.32e+01i   
1.07e-02i 6.58e-02i 4.04e-01i 2.48e+00i 1.52e+01i 9.32e+01i

The approximations aren’t optimal, but they are close. The convergence rate (25.10) as $n \to \infty$ is one-quarter of the optimal rate (25.5) in the sense that we need 4 times as large a value of $n$ to achieve a certain accuracy in (25.10) as in (25.5).

Above, we computed errors for best polynomial approximations to $| x |$ with the Chebfun command minimax. In the rational case, minimax does not succeed in computing best approximations beyond a certain low order. This difficulty is related to the exponential spacing of the oscillations of $f - r ^ { * }$ near $x = 0$ .

It is worth noting that the problem of approximating $| x |$ on $[ - 1 , 1 ]$ is equivalent to certain other approximation problems. If $r ( x )$ is a type $( m , n )$ approximation to $| x |$ on $[ - 1 , 1 ]$ , then normally $r$ will be an even function of $x$ and $m$ and $n$ can be taken to be even too. Thus $r ( x ) = \tilde { r } ( x ^ { 2 } )$ , where $\tilde { r }$ is a rational function of type $( m / 2 , n / 2 )$ . Since $\tilde { r } ( x ^ { 2 } )$ approximates $| x |$ for $x \in [ - 1 , 1 ]$ , $\tilde { r } ( x )$ approximates $\sqrt { x }$ for $x \in [ 0 , 1 ]$ . This reasoning holds for any approximations, and in particular, by counting equioscillations one finds that best type $( m , n )$ approximation of $| x |$ o n $[ - 1 , 1 ]$ is equivalent to best type $( m / 2 , n / 2 )$ approximation of $\sqrt { x }$ on $[ 0 , 1 ]$ . The following pair of plots illustrates this equivalence. Notice that the error curves are the same apart from the scaling of the $x$ -axis.

f = abs(x); [p,q,rh,err] = minimax(f,2,2);   
subplot(1,2,1), plot(f-p/q), hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') f $=$ chebfun('sqrt(x)',[0,1],'splitting','on');   
[p,q,rh,err] $=$ minimax(f,1,1);   
subplot(1,2,2), plot(f-p/q), hold on   
plot([-.03 1],err\*[1 1],'--k'), plot([0 1],-err\*[1 1],'--k')

![](images/a53178e113481cdc5cff0f9fd61f90f98fd58b1541b27f4ec150fa914301216f.jpg)

For applications in scientific computing, the approximation of $\sqrt { x }$ on an interval $[ a , b ]$ is particularly interesting because of the case in which $x$ is a matrix $A$ with eigenvalues in $[ a , b ]$ , which might come from discretizing a differential operator. Rational approximations of the square root lead to powerful algorithms for evaluating $A ^ { 1 / 2 } v$ for vectors $v$ , as described in [Hale, Higham & Trefethen 2008] and [Higham 2008]. At the other end of the historical spectrum, approximation of square roots was the problem addressed by Poncelet in the very first paper on minimax approximation [Poncelet 1835].

We now turn to the second of the famous problems of this chapter: approximation of $e ^ { x }$ on $( - \infty , 0 ]$ . This problem was introduced in a paper of Cody, Meinardus, and Varga [1969], which drew attention to the connection of such approximations with the numerical solution of PDEs, since a rational approximation can be used to compute the exponential of a matrix arising from a numerical discretization [Moler $\&$ Van Loan 2003].13 Curiously, despite that good motivation from applied mathematics, the influence of this paper was mainly in theoretical approximation theory for quite a few decades, until computers and numerical linear algebra had advanced to the point where it became more practical to take advantage of algorithms based on rational functions.

The first thing we may note about approximation of $e ^ { x }$ on $( - \infty , 0 ]$ is that polynomials cannot do the job at all. Since any nonconstant polynomial $p ( x )$ diverges to $\pm \infty$ as $x \to - \infty$ , the only polynomials that can approximate $e ^ { x }$ with finite error on $( - \infty , 0 ]$ are constants, so the minimax error can never be less than $1 / 2$ .

Inverse-polynomials of the form $1 / p _ { n } ( x )$ , however, can be chosen to converge geometrically. This makes sense when you consider that $e ^ { x }$ on $( - \infty , 0 ]$ is the same as $1 / e ^ { x }$ for $x \in [ 0 , \infty )$ . Cody, Meinardus, and Varga noted that to achieve geometric convergence, it is enough to consider $1 / p _ { n } ( x )$ , where $p _ { n }$ is the degree $n$ truncation of the Taylor series for $e ^ { x }$ . They showed that these approximations converge at a rate $O ( 2 ^ { - n } )$ , and then they improved this rate to $O ( 2 . 2 9 8 ^ { - n } )$ by a shift of origin. It was later proved by Sch¨onhage [1973] that the optimal rate for inverse-polynomials is $O ( 3 ^ { - n } )$ .

Since $1 / p _ { n } ( x )$ is a rational function of type $( n , n )$ , these observations tell us that best rational type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ converge at least geometrically. Newman [1974] proved that the convergence is no faster than geometric. What is the optimal rate? With twice as many parameters to work with as with inverse-polynomials, one might guess that it should be $O ( 9 ^ { - n } )$ , and this idea became known in the 1970s as the $1 / 9$ conjecture. In fact, the optimal convergence rate turned out to be $O ( H ^ { n } )$ with $H \approx 1 / 9 . 2 8 9 0 3$ , a number now known as Halphen’s constant, equal to the unique positive root of the equation

$$
h ( s ) = \sum _ { k = 1 } ^ { \infty } { \frac { k s ^ { n } } { 1 - ( - s ) ^ { n } } } = { \frac { 1 } { 8 } } .
$$

This number was conjectured numerically based on Carath´eodory–Fej´er singular values by Trefethen and Gutknecht [1983b], verified to many digits by high-precision Remez algorithms by Carpenter, Ruttan, and Varga [1984], conjectured to have the exact value associated with a certain problem of elliptic functions treated by Halphen [1886] by Magnus via the Carath´eodory–Fej´er method [Magnus 1985, Magnus & Meinguet 2000], and then proved using quite different methods of potential theory by Gonchar and Rakhmanov [1989]. This work represents a fascinating and important line of investigation in approximation theory, and for a summary of many of the ideas with wide generalizations to related problems, a good place to start is [Stahl & Schmelzer 2009]. A presentation of the potential theory underlying results in this area can be found in [Saff & Totik 1997].

Following the idea presented earlier for $| x |$ on $[ - 1 , 1 ]$ , it is interesting to see what can be achieved for this problem by the trapezoidal rule approximation of a contour integral. Here is a derivation of a rational approximation that achieves the rate $O ( ( 2 . 8 4 9 \dots . . . ) ^ { - n } )$ , adapted from [Weideman $\&$ Trefethen 2007b]; such approximations are discussed more generally in [Trefethen, Weideman $\&$ Schmelzer 2006]. We begin with a Laplace transform identity that is easily proved by residue calculus,

$$
e ^ { x } = \frac { 1 } { 2 \pi i } \int \frac { e ^ { t } d t } { t - x }
$$

for $x \in ( - \infty , 0 ]$ , where the integral is over any contour in the complex plane that starts at $- \infty$ below the $t$ -axis, circles around $t = 0$ , and finishes at $- \infty$ above the $t$ -axis. Choosing the contour to be a parabola, we convert this to an integral over the real $s$ -axis by the change of variables

$$
t = ( i s + a ) ^ { 2 } , \quad d t = 2 i ( i s + a ) d s
$$

for some constant $a > 0$ , which gives

$$
e ^ { x } = \frac { 1 } { \pi } \int _ { - \infty } ^ { \infty } \frac { e ^ { ( i s + a ) ^ { 2 } } ( i s + a ) d s } { ( i s + a ) ^ { 2 } - x } .
$$

As in (25.8), we now approximate this integral by the trapezoidal rule with node spacing $h > 0$ :

$$
r ( x ) = \frac { h } { \pi } \sum _ { k = - ( n - 1 ) / 2 } ^ { ( n - 1 ) / 2 } \frac { e ^ { ( i k h + a ) ^ { 2 } } ( i k h + a ) } { ( i k h + a ) ^ { 2 } - x } .
$$

Here $n$ is a positive even number, and since $x$ rather than $x ^ { 2 }$ appears in each term we now take $n$ terms in the sum rather than $n / 2$ as in (25.8) to make $r ( x )$ a rational function of $x$ of type $( n - 1 , n )$ .

This time, the integral has square-exponential rather than just exponential decay as $s  \infty$ , so choosing $h = O ( 1 / { \sqrt { n } } )$ is enough to make the errors from endpoint truncation exponentially small. We also have the parameter $a$ to play with. By taking $a = O ( { \sqrt { n } } )$ , we can make the errors due to grid spacing exponentially small too, and in this fashion we can achieve geometric convergence. More precisely, the choices

$$
a = { \sqrt { \frac { \pi n } { 2 4 } } } , \quad h = { \sqrt { \frac { 3 \pi } { 2 n } } }
$$

lead to the convergence rate

$$
\lVert f - r _ { n n } \rVert = O ( e ^ { - \pi n / 3 } ) \approx O ( ( 2 . 8 4 9 \cdot . . ) ^ { - n } ) .
$$

As before, we can see these approximations with an experiment, this time plotting $f - r$ rather than $r$ itself.

$\mathrm { ~ x ~ } =$ $\begin{array} { r l } & { = \mathrm { \ c h e b f u n } ( ^ { \prime } \mathrm { \ x } ^ { \prime } , [ - 2 , - . 0 1 ] ) ; \mathrm { ~ f ~ = ~ } \exp ( \mathrm { \ x } ) ; } \\ & { \mathrm { \texttt { r n } ~ = ~ } 2 ; 2 \colon 8 } \\ & { \mathrm { \texttt { r } ~ = ~ } 0 * \mathrm { \texttt { x } } ; \mathrm { \texttt { h } ~ = ~ s q r t } ( 3 * \mathrm { p i } / ( 2 * \mathrm { n } ) ) ; \mathrm { \texttt { a } ~ = ~ s q r t } ( \mathrm { p i } * \mathrm { n } / 2 4 ) ; } \\ & { \mathrm { \texttt { f o r ~ k } ~ = ~ } - ( \mathrm { n } - 1 ) / 2 ; ( \mathrm { n } - 1 ) / 2 } \\ & { \mathrm { \texttt { r } ~ = ~ } \mathrm { \texttt { r } ~ + ~ } \exp ( ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) \cdot 2 ) * ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) . / ( ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) \cdot 2 - \mathrm { x } ) ; } \end{array}$ fo   
end   
$\begin{array} { r } { \mathbf { r } ~ = ~ \left( \mathrm { h / p i } \right) { * } \mathrm { r e a l } \left( \mathrm { r } \right) } \end{array}$ ; subplot(2,2,n/2), plot(f-r)   
err $=$ norm(f-r,inf);   
ss $=$ sprintf('(%1d,%1d) error = %7.5f',n,n,err);   
end

![](images/3e8d41548190afd51e3d6f0652968652ec9e34cbbd699d04204fe73f05ad89df.jpg)

Let us summarize these results with a theorem, which goes further to include the precise leading-order asymptotic behavior of the best approximation errors as conjectured by Magnus [1994] and proved by Aptekarev [2002].

Theorem 25.2. Approximation of $e ^ { \mathbf { x } }$ on $( - \infty , \mathbf { 0 } ]$ . The errors in best type $( 0 , n )$ and $( n , n )$ rational approximation of $\exp ( x )$ on $( - \infty , 0 ]$ satisfy as $n \to \infty$

$$
\operatorname* { l i m } _ { n \to \infty } { E _ { 0 n } ^ { 1 / n } } = \frac { 1 } { 3 }
$$

and

$$
E _ { n n } \sim 2 H ^ { n + 1 / 2 } , ~ H = 1 / 9 . 2 8 9 0 2 5 4 9 1 9 2 0 8 \ldots _ { \cdot \cdot \cdot }
$$

Proof. Equation (25.17) is due to Sch¨onhage [1973] and (25.18) to Aptekarev [2002], extending the earlier result on $_ { n }$ th root asymptotics and the constant $H$ by Gonchar and Rakhmanov [1989].

We finish this chapter by showing that the numerical computation of these best approximants is surprisingly easy. The crucial matter is to note that the change of variables

$$
x = a \frac { s - 1 } { s + 1 } , \qquad s = \frac { a + x } { a - x } ,
$$

where $a$ is a positive parameter, maps the negative real axis $( - \infty , 0 ]$ in $x$ to the interval $( - 1 , 1 ]$ in $s$ . Since the mapping is a rational function of type $( 1 , 1 )$ , it transplants a rational function of type $( n , n )$ in $s$ or $x$ to a rational function of type $( n , n )$ in the other variable. In particular, for the approximation of $f ( x ) = e ^ { x }$ o n $( - \infty , 0 ]$ , let us define

$$
F ( s ) = e ^ { a ( s - 1 ) / ( s + 1 ) } , \quad s \in ( - 1 , 1 ] .
$$

A good choice of the parameter is $a ~ = ~ 9$ , which has a big effect for numerical computation in improving the conditioning of the approximation problem. We now find we have a function that can be approximated to machine precision by a Chebyshev interpolating polynomial $p ( s )$ of degree less than 50:

ans $=$ 47

The Chebyshev series of $F$ decreases at a good exponential rate:

plotcoeffs(F)

![](images/51a7bceac042511ae0e9b7e05af9f6ac74389ce54a1ecede84ecbd6ca3ad4a6f.jpg)

This gives us yet another way to compute rational approximations to $e ^ { x }$ on $( - \infty , 0 ]$ : truncate this Chebyshev series in $s$ , and then transplant by (25.19) to get rational functions in $x$ .

Alternatively, we can get true best approximations from (25.19) by applying the Chebfun minimax command. Here, for example, is the error for the best approximation of type $( 8 , 8 )$ plotted in the $s$ variable, showing 18 points of equioscillation.

[P,Q,RH,err] $=$ minimax(F,8,8); $\mathtt { R } \ = \ \mathtt { P } / \mathtt { Q }$ ; plot(F-R), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](images/19010920f0ecc626278b032a01e08552bb2f555b4da4b13e4b32bce56754a27f.jpg)

If we plot the same curve in the $x$ variable, it’s hard to see much because of the varying scale:

${ \bf s } 1 ~ = ~ - . 9 9 9$ ; s2 = .999; s = chebfun('s',[s1 s2]); $\textbf { x } = ~ 9 * \left( \mathbf { s } \mathbf { - } 1 \right) / \left( \mathbf { s } + 1 \right)$ ; plot(x,F{s1,s2}-R{s1,s2}), hold on $\bf { x } \bf { x } ~ = ~ [ - 1 e 4 ~ - 1 e - 2 ]$ ; plot(xx,err\*[1,1],'--k') plot(xx,-err\*[1,1],'--k')

![](images/f15b47e1106e1e775122ce5d66eb94578ba89660daed32b24abb34e65c922e0c.jpg)

Putting the $x$ -axis on a log scale, however, makes the plot informative again:

semilogx(x,F{s1,s2}-R{s1,s2}), hold on semilogx(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](images/bb34a2dee411d4a350616e3d4bc53e5a10171dd4c0b7141577f260b91cea6342.jpg)

Here is the analogous plot for type (12, 12) approximation:

[P,Q,RH,err] $=$ minimax(F,12,12); $\mathtt { R } \ = \ \mathtt { P } . / \mathtt { Q }$ ;$\mathbf { s e m i l o g x } ( \mathbf { x } , \mathbf { F } \{ \mathbf { s } 1 , \mathbf { s } 2 \} - \mathbb { R } \{ \mathbf { s } 1 , \mathbf { s } 2 \} )$ , hold onplot(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](images/f38b49fe9b0b8ca55739285215fc25a6be46e8ebb86ca2d216306184305efbf7.jpg)

These plots are modeled after [Trefethen, Weideman & Schmelzer 2006], where it is shown that Carath´eodory–Fej´er approximation is equally effective and even faster than the Remez algorithm at computing these approximations.

Summary of Chapter 25. Two problems involving rational functions have attracted special attention, highlighting the power of rational approximations near singularities and on unbounded domains. For approximating $| x |$ on $[ - 1 , 1 ]$ , best rational functions converge root-exponentially, whereas polynomials converge linearly. For approximating $e ^ { x }$ on $( - \infty , 0 ]$ , best rational functions converge geometrically, whereas polynomials do not converge at all. Both rates of approximation can be achieved by constructing partial fractions from trapezoidal rule approximations to certain integrals.

Exercise 25.1. Newton iteration for $| { \pmb x } |$ . (This problem has roots in [Roberts 1980].) (a) Let $_ x$ be a number, and suppose we want to solve the equation $r ^ { 2 } = x ^ { 2 }$ for the unknown $r$ using Newton iteration. Show that the iteration formula is $r ^ { ( k + 1 ) } = ( ( r ^ { ( k ) } ) ^ { 2 } +$ $x ^ { 2 } ) / 2 r ^ { ( k ) }$ . (b) If the initial guess is $r ^ { ( 0 ) } = 1$ , then for $k \geq 1$ , what is the smallest $_ n$ for which the rational function $r ^ { ( k ) } ( x )$ is of type $( n , n )$ ? (c) Use Chebfun to compute and plot the approximations $r ^ { ( 0 ) } ( x ) , \ldots , r ^ { ( 5 ) } ( x )$ on the interval $[ - 1 , 1 ]$ . What is the sup-norm error $\| | x | - r ^ { ( k ) } ( x ) \|$ , and where is it attained? (d) What rate of convergence does this correspond to for $\| | x | - r ^ { ( k ) } ( x ) \|$ as a function of $n$ ? How does this compare with the optimal rate given by Theorem 25.1? (e) Make a semilog plot of $| | x | - r ^ { ( 5 ) } ( x ) |$ as a function of $x \in [ - 1 , 1 ]$ and comment further on the nature of these rational approximations.

Exercise 25.2. An elementary approximant for $e ^ { \alpha }$ on $( - \infty , \mathbf { 0 } ]$ . (a) A degree $n$ polynomial $p ( s )$ on $[ - 1 , 1 ]$ can be transplanted to a type $( n , n )$ rational function $r ( x )$ on $( - \infty , 0 ]$ by the map (25.19). Combine this observation with Theorem 8.2 to show that type $( n , n )$ approximants to $e ^ { x }$ on $( - \infty , 0 ]$ exist with accuracy $O ( \exp ( - C n ^ { - 2 / 3 } ) )$ . (b) How does the $n ^ { - 2 / 3 }$ prediction match the data in the curve after (25.20)?

Exercise 25.3. Computing Halphen’s constant. Write a short Chebfun program that computes Halphen’s constant to 10 or more digits based on the condition (25.12).

Exercise 25.4. Best approximation errors for $e ^ { \alpha }$ . (a) Using minimax and the change of variables (25.20), compute best approximation errors in type $( n , n )$ approximation of $e ^ { x }$ on $( - \infty , 0 ]$ for $n = 0 , 1 , \ldots , 1 3$ . Plot the results on a log scale and compare them with estimates from the asymptotic formula (25.18). Also on a log scale, plot the difference between the estimates and the true errors, and comment on the results. (b) Repeat the computation with CF instead of minimax. This time, plot the difference between the CF and true errors on a log scale, and comment on the results.

Exercise 25.5. Behavior of approximants of $| { \pmb x } |$ in the complex plane. It is shown in [Blatt, Iserles & Saff 1987] that the type $( n , n )$ best approximants to $| x |$ on $[ - 1 , 1 ]$ have all their zeros and poles on the imaginary axis and converge to $_ x$ for $\operatorname { R e } ( x ) > 0$ and to $- x$ for $\mathrm { R e } ( x ) < 0$ as $n \to \infty$ . Verify this result numerically by plotting $| x - r _ { n n } ^ { * } ( x ) |$ against $\mathrm { R e } ( x )$ for $x \in [ - 1 + 0 . 5 i , 1 + 0 . 5 i ]$ for $n = 1 , 2 , 3 , 4$ .

Exercise 25.6. Behavior of approximants of $e ^ { \alpha }$ in the complex plane. It is stated in [Stahl & Schmelzer 2009] that the poles of best type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ move off to $\infty$ as $n \to \infty$ , and the convergence at $n$ th-root rate governed by $H \approx 1 / 9 . 2 8 9 0 3$ applies on any compact set in the complex plane. With this result in mind, produce contour plots in the complex $z$ -plane for the errors $\displaystyle | e ^ { z } - r _ { n n } ( z ) |$ for the approximations (25.14)–(25.15) with $n = 2 , 4 , 6 , 8 , 1 0$ . Does it appear likely that these approximations too converge on all compact sets in the plane?

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

![](images/a922a6a33d1513ea97ca77179498ae0ea8d3af9c3f468ab44336e55886904154.jpg)

And here it is for $\varepsilon = 0 . 0 0 1$ :

$\mathtt { e p } \ = \ 0 . 0 0 1$ ; plot(r(ep)), hold on plot([-1 0 1],[1+ep 1 1+2\*ep],'.k')

![](images/14fcd2d1f524126e58fc09f801506da302bdcb986693054316d462fa9f43d8ca.jpg)

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

![](images/6106bef17cdb2ef9e4ddc7b1c1fa17ba59233a3d0c78594b0b722f14a9aa8059.jpg)

One might suspect that this artifact has something to do with rounding errors on the computer, but it is not so. The spurious pole is in the mathematics, with residue equal to about $- 0 . 0 0 1 3$ .

In other examples, on the other hand, spurious poles do indeed arise from rounding errors. In fact, they appear very commonly when one aims for approximations with accuracy close to machine precision. Here, for example, is a numerically computed interpolant of type $( 8 , 8 )$ to $e ^ { x }$ in 21 Chebyshev points:

[p,q] = ratinterp(exp(x),8,8,[],[],0); plot(p/q), hold on xx $=$ chebpts(21); plot(xx,exp(xx),'.k')

![](images/1b9092b88f30bc9b2a7360d60f3bd92612fab5957831c18369de3f6d6c17311d.jpg)

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

![](images/25663588c0e4aa5ac6fa3523a12e349e59e7f04b3d3313e5134364a4ae233645.jpg)

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

![](images/142436d8ae81686bec488fb2dbd84abd731ed2b398484f2e3c8c1f924e3a220a.jpg)

For comparison, suppose we revert to the original definitions of the anonymous functions $\mathrm { \Delta p }$ and q, with no removal of negligible singular values:

$\mathbf { q _ { \lambda } } = \mathbf { \lambda } \otimes ( \mathbf { f _ { \lambda } } , \mathbf { m _ { \lambda } } , \mathbf { n _ { \lambda } } , \mathbf { N } )$ null(Ctilde(f,m,n,N));   
p = @(f,m,n,N) C(f,m,n,N)\*q(f,m,n,N);

Now the computation comes out with exact type $( 4 0 , 4 0 )$ , and half the poles are spurious:

$\mathtt { m } ~ = ~ 4 0$ ; $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ 4 0 ~ }$ ; $\tt { N } = \tt { 4 0 0 }$ ;   
pp = p(f,m,n,N); pp = pp(:,end); qq = q(f,m,n,N); qq = qq(:,end); rpoles $=$ roots(flipud(qq)); hold off, plot(exp(2i\*pi\*x)), hold on plot(rpoles+1e-10i,'.r')

![](images/76e29bad9d92b0d67373adc66181e0f71c55da1721c330fdb4b1cabebd163a94.jpg)

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

# Chapter 27. Pad´e Approximation

Suppose $f$ is a function with a Taylor series

$$
f ( z ) = c _ { 0 } + c _ { 1 } z + c _ { 2 } z ^ { 2 } + \cdot \cdot \cdot
$$

at $z = 0$ .14 Whether or not the series converges doesn’t matter in this chapter (it is enough for $f$ to be a formal power series). For any integer $m \geq 0$ , the degree $m$ Taylor approximant to $f$ is the unique polynomial $p _ { m } \in \mathcal { P } _ { m }$ that matches the series as far as possible, which will be at least through degree $m$ ,

$$
( f - p _ { m } ) ( z ) = O ( z ^ { m + 1 } ) .
$$

Pad´e approximation is the generalization of this idea to rational approximation. For any integers $m , n \geq 0$ , $r \in \mathcal { R } _ { m n }$ is the type $( m , n )$ Pad´e approximant to $f$ if their Taylor series at $z = 0$ agree as far as possible:

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { \mathrm { m a x i m u m } } ) .
$$

In these conditions the “big O” notation has its usual precise meaning. Equation (27.2) asserts, for example, that the first nonzero term in the Taylor series for $f - p _ { m }$ is of order $z ^ { k }$ for some $k \geq m + 1$ , but not necessarily $k = m + 1$ .

Pad´e approximation can be viewed as the special case of rational interpolation in which the interpolation points coalesce at a single point. Thus there is a close analogy between the mathematics of the last chapter and this one, thoughsome significant differences too that spring from the fact that the powers $z ^ { 0 } , z ^ { 1 } , \dots$ are ordered whereas the roots of unity are all equal in status. We shall see that a key property is that $r _ { m n }$ exists and is unique. Generically, it matches $f$ through term $m + n$ ,

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { m + n + 1 } ) ,
$$

but in some cases, the matching will be to lower or higher order.

For example, the type $( 1 , 1 )$ Pad´e approximant to $e ^ { z }$ is $( 1 + \textstyle { \frac { 1 } { 2 } } z ) / ( 1 - \textstyle { \frac { 1 } { 2 } } z )$ , as we can verify numerically with the Chebfun command padeapprox:

[r,a,b] $=$ padeapprox(@exp,1,1); fprintf(' Numerator coeffs: %19.15f %19.15f\n',a) fprintf(' Denominator coeffs: %19.15f %19.15f\n',b)

Numerator coeffs: 1.000000000000000 0.500000000000000   
Denominator coeffs: 1.000000000000000 -0.500000000000000

The algorithm used by padeapprox will be discussed in the second half of this chapter.

The early history of Pad´e approximation is hard to disentangle because every continued fraction can be regarded as a Pad´e approximant (Exercise 27.7), and continued fractions got a lot of attention in past centuries. For example, Gauss derived the idea of Gauss quadrature from a continued fraction that amounts to a Pad´e approximant to the function $\log ( ( z + 1 ) / ( z - 1 ) )$ at the point $z = \infty$ [Gauss 1814, Takahasi & Mori 1971, Trefethen 2008]. Ideas related to Pad´e approximation have been credited to Anderson (1740), Lambert (1758), and Lagrange (1776), and contributions were certainly made by Cauchy [1826] and Jacobi [1846]. The study of Pad´e approximants began to come closer to the current form with the papers of Frobenius [1881] and Pad´e himself [1892], who was a student of Hermite and published many articles after his initial thesis on the subject. Throughout the early literature, and also in the more recent era, much of the discussion of Pad´e approximation is connected with continued fractions, determinants, and recurrence relations, but here we shall follow a more robust matrix formulation.

We begin with a theorem about existence, uniqueness, and characterization, analogous to Theorem 24.1 for rational best approximation on an interval. There, the key idea was to count points of equioscillation of the error function $f - r$ . Here, we count how many initial terms of the Taylor series of $f - r$ are zero. The arguments are similar, and again, everything depends on the integer known as the defect. Recall that if $r \in \mathcal { R } _ { m n }$ is of exact type $( \mu , \nu )$ for some $\mu \leq m$ , $\nu \leq n$ , then the defect of $r$ with respect to $\mathcal { R } _ { m n }$ is $d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0$ , with $\mu = - \infty$ and $d = n$ in the special case $r = 0$ .

Theorem 27.1. Characterization of Pad´e approximants. For each $m , n \geq$ 0, a function $f$ has a unique Pad´e approximant $r _ { m n } \in \mathcal { R } _ { m n }$ as defined by the condition (27.3), and a function $r \in \mathcal { R } _ { m n }$ is equal to $r _ { m n }$ if and only if $( f - r ) ( z ) =$ $O ( z ^ { m + n + 1 - d } )$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

Proof. The first part of the argument is analogous to parts 2 and 4 of the proof of Theorem 24.1: we show that if $r$ satisfies $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , then $r$ is the unique type $( m , n )$ Pad´e approximant to $f$ as defined by the condition (27.3). Suppose then that $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ and that $( f - \tilde { r } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ also for some possibly different function $\tilde { r } \in \mathcal { R } _ { m n }$ . Then $( r - { \tilde { r } } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . However, $r - \tilde { r }$ is of type $( m + n - d , 2 n - d )$ , so it can only have $m + n - d$ zeros at $z = 0$ unless it is identically zero. This implies $\tilde { r } = r$ .

The other half of the proof is to show that there exists a function $r$ with $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . This part of the argument makes use of linear algebra and is given in the two paragraphs following (27.8).

Let us consider some examples to illustrate the characterization of Theorem 27.1. First, a generic case: We noted above that the type (1,1) Pad´e approximant to $e ^ { z }$ is $r _ { 1 1 } ( z ) = ( 1 + \textstyle \frac { 1 } { 2 } z ) / ( 1 - \textstyle \frac { 1 } { 2 } z )$ . The defect of $r _ { 1 1 }$ in $\mathcal { R } _ { 1 1 }$ is $d = 0$ , and we have

$$
r _ { 1 1 } ( z ) - e ^ { z } = \textstyle { \frac { 1 } { 1 2 } } z ^ { 3 } + \textstyle { \frac { 1 } { 1 2 } } z ^ { 4 } + \cdot \cdot \cdot = O ( z ^ { 3 } ) .
$$

Since $m + n + 1 - d = 3$ , this confirms that $r _ { 1 1 }$ is the Pad´e approximant.

On the other hand, if $f$ is even or odd, we soon find ourselves in the nongeneric case. Suppose we consider

$$
\begin{array} { r } { f ( z ) = \cos ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 2 4 } z ^ { 4 } - \cdot \cdot \cdot } \end{array}
$$

and the rational approximation

$$
\begin{array} { r } { r ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } } \end{array}
$$

of exact type $( 2 , 0 )$ . This gives

$$
( f - r ) ( z ) = O ( z ^ { 4 } ) , \ \ne O ( z ^ { 5 } ) .
$$

By Theorem 27.1, this implies that $r$ is the Pad´e approximation to $f$ for four different choices of $( m , n )$ : $( 2 , 0 )$ , $( 3 , 0 )$ , $( 2 , 1 )$ , and $( 3 , 1 )$ . With $( m , n ) = ( 2 , 0 )$ , for example, the defect is $d = 0$ and we need $( f - r ) ( z ) = O ( z ^ { 2 + 0 + 1 - 0 } ) = O ( z ^ { 3 } )$ , and with $( m , n ) = ( 3 , 1 )$ , the defect is $d = 1$ and we need $( f - r ) ( z ) = O ( z ^ { 3 + 1 + 1 - 1 } ) = O ( z ^ { 4 } )$ . Both matching conditions are satisfied, so $r$ is the Pad´e approximant of both types $( 2 , 0 )$ and $( 3 , 1 )$ . Similarly it is also the Pad´e approximant of types $( 3 , 0 )$ and $( 2 , 1 )$ , but for no other values of $( m , n )$ .

This example involving an even function suggests the general situation. In analogy to the Walsh table of Chapter 24, the Pad´e table of a function $f$ consists of the set of its Pad´e approximants for various $m , n \geq 0$ laid out in an array, with $m$ along the horizontal and $n$ along the vertical:

$$
\left( { \begin{array} { c c c c } { r _ { 0 0 } } & { r _ { 1 0 } } & { r _ { 2 0 } } & { . . . } \\ { r _ { 0 1 } } & { r _ { 1 1 } } & { r _ { 2 1 } } & { . . . } \\ { r _ { 0 2 } } & { r _ { 1 2 } } & { r _ { 2 2 } } & { . . . } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \end{array} } \right) .
$$

The idea of the Pad´e table was proposed by Pad´e [1892], who called it “a table of approximate rational fractions. . . analogous to the multiplication table, unbounded to the right and below.” Like the Walsh table for real rational approximation on an interval, the Pad´e table breaks into square blocks of degenerate entries, again as a consequence of the equioscillation-type characterization [Trefethen 1984].

Theorem 27.2. Square blocks in the Pad´e table. The Pad´e table for any function $f$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. The proof is essentially the same as the proof of Theorem 24.2.

As in the case of best real approximation on an interval discussed in Chapter 24, square blocks and defects have a variety of consequences for Pad´e approximants. In particular, the Pad´e approximation operator, which maps Taylor series $f$ to their Pad´e approximants $r _ { m n }$ , is continuous at $f$ with respect to a norm based on Taylor coefficients if and only if $r _ { m n }$ has defect $d = 0$ . Another related result is that best supremum-norm approximations on intervals $[ - \varepsilon , \varepsilon ]$ converge to the Pad´e approximant as $\varepsilon  0$ if $d = 0$ , but not, in general, if $d > 0$ . These results come from [Trefethen $\&$ Gutknecht 1985], with earlier partial results due to Walsh; Werner and Wuytak; and Chui, Shisha, and Smith.

At this point we have come a good way into the theory of Pad´e approximation without doing any algebra. To finish the job, and to lead into algorithms, it is time to introduce vectors and matrices, closely analogous to those of the last chapter.

Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , suppose we look for a representation of the Pad´e approximant $r _ { m n }$ as a quotient $r = p / q$ with $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ . Equation (27.4) is nonlinear, but multiplying through by the denominator suggests the linear condition

$$
p ( z ) = f ( z ) q ( z ) + O ( z ^ { m + n + 1 } ) ,
$$

just as (26.4) led to (26.5). To express this equation in matrix form, suppose that $p$ and $q$ are represented by coefficient vectors $\mathbf { a }$ and $\mathbf { b }$ :

$$
\mathbf { a } = \left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m } } \end{array} \right) , \qquad \mathbf { b } = \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) ,
$$

$$
p ( z ) = \sum _ { k = 0 } ^ { m } a _ { k } z ^ { k } , \qquad q ( z ) = \sum _ { k = 0 } ^ { n } b _ { k } z ^ { k } .
$$

Then (27.5) can be written as an equation involving a Toeplitz matrix of Taylor coefficients of $f$ , that is, a matrix with constant entries along each diagonal. For $m \geq n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \\ { \vdots } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { m + n } } \end{array} \right) = \left( \begin{array} { c c c c c } { c _ { 0 } } & & & & \\ { c _ { 1 } } & & { c _ { 0 } } & & \\ { \vdots } & { \vdots } & { \ddots } & & \\ { c _ { n } } & { c _ { m - 1 } } & { \ddots } & & { c _ { 0 } } \\ { \vdots } & { \vdots } & & & { \vdots } \\ { c _ { m } } & { c _ { m - 1 } } & { \hdots } & { c _ { m - n } } \\ { c _ { m + 1 } } & { c _ { m } } & { \hdots } & { c _ { m + 1 - n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \hdots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right)
$$

coupled with the condition

$$
a _ { m + 1 } = \cdots = a _ { m + n } = 0 .
$$

In other words, $\mathbf { b }$ must be a null vector of the $n \times ( n + 1 )$ matrix displayed below the horizontal line. If $m < n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { n } } \\ { a _ { m } } \end{array} \right) = \left( \begin{array} { c c c c c c c } { c _ { 0 } } \\ { c _ { 1 } } \\ { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { c _ { m } } & { c _ { m - 1 } } & { \ldots } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } \\ { c _ { n } } & { c _ { n - 1 } } & { \ddots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \ldots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) .
$$

For simplicity we shall use the label (27.6) to refer to both cases, writing the $n ~ \times$ $( n + 1 )$ matrix always as

$$
C = \left( \begin{array} { c c c c } { { c _ { m + 1 } } } & { { c _ { m } } } & { { \ldots } } & { { c _ { m + 1 - n } } } \\ { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { c _ { m + n } } } & { { c _ { m + n - 1 } } } & { { \ldots } } & { { c _ { m } } } \end{array} \right)
$$

with the convention that $c _ { k } = 0$ for $k < 0$ .

One solution to (27.6)–(27.7) would be $\mathbf { a } = \mathbf { 0 }$ and $\mathbf { b } = \mathbf { 0 }$ , corresponding to the useless candidate $r = 0 / 0$ . However, an $n \times ( n + 1 )$ matrix always has a nonzero null vector,

$$
C \mathbf { b } = \mathbf { 0 } , \quad \mathbf { b } \neq \mathbf { 0 } ,
$$

and once $\mathbf { b }$ is chosen, the coefficients $a _ { 0 } , \ldots , a _ { m }$ of $p$ can be obtained by multiplying out the matrix-vector product above the line. Thus there is always a solution to (27.5) with $q \neq 0$ .

If $b _ { 0 } \neq 0$ , then dividing (27.5) by $q$ shows that $p / q$ is a solution to (27.4). Some nonzero null vectors $\mathbf { b }$ , however, may begin with one or more zero components. Suppose that $\mathbf { b }$ is a nonzero null vector with $b _ { 0 } = b _ { 1 } = \cdot \cdot \cdot = b _ { \sigma - 1 } = 0$ and $b _ { \sigma } \neq 0$ for some $\sigma \geq 1$ . Then the corresponding vector $\mathbf { a }$ will also have $u _ { 0 } = u _ { 1 } = \cdot \cdot \cdot =$ $a _ { \sigma - 1 } = 0$ (and $a _ { \sigma }$ might be zero or nonzero). It follows from the Toeplitz structure of (27.6) that we can shift both $\mathbf { a }$ and $\mathbf { b }$ upward by $\sigma$ positions to obtain new vectors $\tilde { \mathbf { a } } = ( a _ { \sigma } , \ldots , a _ { m } , 0 , \ldots , 0 ) ^ { T }$ and $\bar { \mathbf { b } } = ( b _ { \sigma } , \ldots , b _ { n } , 0 , \ldots , 0 ) ^ { T }$ while preserving the quotient $r = \tilde { p } / \tilde { q } = p / q$ . Thus $r$ has defect $d \geq \sigma$ , and (27.6)–(27.7) are still satisfied except that $\tilde { a } _ { m + n - \sigma + 1 } , \dots , \tilde { a } _ { m + n }$ may no longer be zero, implying $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \sigma } )$ . Thus $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , and this completes the proof of Theorem 27.1.

We have just shown that any nonzero null vector of the matrix $C$ of (27.8) gives a function $r$ that satisfies the condition for a Pad´e approximation and hence must be the unique approximant provided by Theorem 27.1. So we have proved the following theorem.

Theorem 27.3. Linear algebra solution of Pad´e problem. Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , let b be any nonzero null vector of the matrix

$C$ of (27.8), let a be the corresponding vector obtained from (27.6), and let $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ be the corresponding polynomials. Then $r _ { m n } = p / q$ is the unique type $( m , n )$ Pad´e approximant to $f$ .

We emphasize that the vectors $\mathbf { a }$ and $\mathbf { b }$ are not unique in general: a function in $\mathcal { R } _ { m n }$ may have many representations $p / q$ . Nevertheless, all choices of $\mathbf { a }$ and $\mathbf { b }$ lead to the same rmn.

From Theorems 27.1–27.3 one can derive a precise characterization of the algebraic structure of the Pad´e approximants to a function $f$ , as follows. Let $\hat { r }$ b e a rational function of exact type $( \mu , \nu )$ that is the Pad´e approximant to $f$ in a $( k + 1 ) \times ( k + 1 )$ square block for some $k \geq 0$ :

$$
\left( \begin{array} { c c c } { { r _ { \mu \nu } } } & { { . . . } } & { { r _ { \mu + k , \nu } } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } \\ { { r _ { \mu , \nu + k } } } & { { . . . } } & { { r _ { \mu + k , \nu + k } } } \end{array} \right) .
$$

Write $\hat { r } = \hat { p } / \hat { q }$ with $\hat { p }$ and $\hat { q }$ of exact degrees $\mu$ and $\nu$ . From Theorem 27.1 we know that the defect $d$ must be distributed within the square block according to this pattern illustrated for $k = 5$ :

$$
\begin{array} { r l } { { \operatorname* { d e f e c t } \ d : } } & { { } \left( \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { 2 } & { 2 } & { 2 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 3 } & { 3 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 4 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 5 } \end{array} \right) \ . } \end{array}
$$

According to Theorem 27.3, the polynomials $p$ and $q$ that result from solving the matrix problem (27.6)–(27.7) must be related to $\hat { p }$ and $\hat { q }$ by

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some polynomial $\pi$ of degree at most $d$ . Now let us define the deficiency $\lambda$ of $r$ as the distance below the cross-diagonal in the square block, with the following pattern:

$$
\mathrm { d e f f c i e n c y ~ } \lambda : \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } \end{array} \right) ~ . \nonumber
$$

From Theorem 27.1, we know that in the positions of the block with $\lambda ~ > ~ 0$ , $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \lambda } ) , \neq O ( z ^ { m + n + 2 - \lambda } )$ , for otherwise, the block would be bigger. For this to happen, $\pi ( z )$ must be divisible by $z ^ { \lambda }$ , so that at least $\lambda$ powers of $z$ are lost when solutions $p$ and $q$ from (27.6) are normalized to $\hat { p }$ and $\hat { q }$ . Since may have degree up to $d$ , the number of degrees of freedom remaining in and $\pi$ $p$ $q$ is $d - \lambda$ , an integer we denote by $\chi$ , distributed within the block according to this

pattern:

$$
\mathrm { r a n k ~ d e f i c i e n c y ~ } \chi ; \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \ .
$$

Thus the dimensionality of the space of vectors $q$ is $\chi + 1$ , and the same for $p$ . We call $\chi$ the rank deficiency of $r$ because of a fact of linear algebra: the rank of the $n \times ( n + 1 )$ matrix $C$ of (27.8) must be equal to $n - \chi$ , so that its space of null vectors will have the required dimension $\chi + 1$ . Some ideas related to these developments can be found in [Heinig & Rost 1984].

We have just outlined a proof of the following theorem, which can be found in Section 3 of [Gragg 1972].

Theorem 27.4. Structure of a Pad´e approximant. Let $f$ and $m , n \geq 0$ be given, let the type $( m , n )$ Pad´e approximant $r _ { m n }$ of $f$ have exact type $( \mu , \nu )$ , and let $\hat { p }$ and $\hat { q } \neq 0$ be polynomials of exact degrees $\mu$ and $\nu$ with $r _ { m n } = \hat { p } / \hat { q }$ . Let the defect $d$ , deficiency $\lambda$ , and rank deficiency $\chi = d - \lambda$ be defined as above. Then the matrix $C$ of (27.8) has rank $n - \chi$ , and two polynomials $p \in P _ { m }$ and $q \in P _ { n }$ satisfy (27.5) if and only if

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some $\pi \in \mathcal { P } _ { d }$ divisible by $z ^ { \lambda }$ .

Although we did not state it in the last chapter, there is an analogue of this theorem for rational interpolation in distinct points, proved by Maehly and Witzgall [1960] and discussed also in [Gutknecht 1990] and [Pach´on, Gonnet & Van Deun 2012].

With the results of the past few pages to guide us, we are now prepared to talk about algorithms.

At one level, the computation of Pad´e approximants is trivial, just a matter of implementing the linear algebra of (27.6)–(27.7). In particular, in the generic case, the matrix $C$ of (27.8) will have full rank, and so will its $n \times n$ submatrix obtained by deleting the first column. One computational approach to Pad´e approximation is accordingly to normalize $\mathbf { b }$ by setting $b _ { 0 } = 1$ and then determine the rest of the entries of $\mathbf { b }$ by solving a system of equations involving this square matrix.

This approach will fail, however, when the square matrix is singular, and it is nonrobust with respect to rounding errors even when the matrix is nonsingular. To work with (27.8) robustly, it is a better idea to normalize by the condition

$$
\| \mathbf { b } \| = 1 ,
$$

where $\| \cdot \|$ is the vector 2-norm, as in (26.6) of the last chapter. We then again consider the SVD (singular value decomposition) of $C$ , a factorization

$$
\boldsymbol { C } = \boldsymbol { U \Sigma V } ^ { * } ,
$$

where $U$ is $n \times n$ and unitary, $V$ is $( n + 1 ) \times ( n + 1 )$ and unitary, and $\Sigma$ is an $n \times ( n + 1 )$ real diagonal matrix with diagonal entries $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq 0$ .

Suppose $\sigma _ { n } ~ > ~ 0$ . Then $C$ has rank $n$ , and the final column of $V$ provides a unique nonzero null vector $\mathbf { b }$ of $C$ up to a scale factor. This null vector defines a polynomial $q \in \mathcal { P } _ { n }$ . Moreover, from (27.11), we know that $( m , n )$ must lie on the outer boundary of its square block in the Pad´e table. If $q$ is divisible by $z ^ { \lambda }$ for some $\lambda \geq 1$ , then $( m , n )$ must lie in the bottom row or right column, and dividing $p$ and $q$ by $z ^ { \lambda }$ brings it to the left column or top row, respectively. A final trimming of any trailing zeros in $p$ or $q$ brings them to the minimal forms $\hat { p }$ and $\hat { q }$ with exact degrees $\mu$ and $\nu$ .

On the other hand, suppose $\sigma _ { n } = 0$ , so that the number of zero singular values of $C$ is $\chi \geq 1$ . In this case (27.11) tells us that $( m , n )$ must lie in the interior of its square block at a distance $\chi$ from the boundary. Both $m$ and $n$ can accordingly be reduced by $\chi$ and the process repeated with a new matrix and a new SVD, $\chi$ steps closer to the upper-left $( \mu , \nu )$ corner. After a small number of such steps (never more than $2 + \log _ { 2 } ( d + 1 )$ , where $d$ is the defect), convergence is guaranteed.

These observations suggest the following SVD-based algorithm, introduced in [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.1. Pure Pad´e approximation in exact arithmetic

Input: $m \geq 0$ , $n \geq 0$ , and a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of $a$ function $f$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of $f$ .

1. If $c _ { 0 } = \cdots = c _ { m } = 0$ , set $p = 0$ and $q = 1$ and stop.

2. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 8.

3. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of nonzero singular values.

4. If $\rho < n$ , reduce $n$ to $\rho$ and $m$ to $m - ( n - \rho )$ and return to Step 2.

5. Get $q$ from the null right singular vector b of $C$ and then $p$ from the upper part of (27.6).

6. If $b _ { 0 } = \cdot \cdot \cdot = b _ { \lambda - 1 } = 0$ for some $\lambda \geq 1$ , which also implies $a _ { 0 } = \cdot \cdot \cdot = a _ { \lambda - 1 } = 0$ , cancel the common factor of $z ^ { \lambda }$ in $p$ and $q$ .

7. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

8. Remove trailing zero coefficients, if any, from $p ( z )$ or $q ( z )$ .

In exact arithmetic, this algorithm produces the unique Pad´e approximant $r _ { m n }$ in a minimal-degree representation of type $( \mu , \nu )$ with $b _ { 0 } = 1$ . The greatest importance of Algorithm 27.1, however, is that it generalizes readily to numerical computation with rounding errors, or with noisy Taylor coefficients $\{ c _ { j } \}$ . All one needs to do is modify the tests for zero singular values or zero coefficients so as to incorporate a suitable tolerance, such as $1 0 ^ { - 1 4 }$ for computations in standard 16-digit arithmetic. The following modified algorithm also comes from [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.2. Robust Pad´e approximation for noisy data or floating point arithmetic

Input: $m \geq 0$ , $n \geq 0$ , a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of a function $f$ , and a relative tolerance $\mathbf { t o l } \geq 0$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of a function close to $f$ .

1. Rescale $f ( z )$ to $f ( z / \gamma )$ for some $\gamma > 0$ if desired to get a function whose Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ do not vary too widely.

2. Define $\tau = \pm \circ 1 \cdot \| \mathbf { c } \| _ { 2 }$ . If $| c _ { 0 } | = \cdot \cdot \cdot = | c _ { m } | \leq \tau$ , set $p = 0$ and $q = 1$ and stop.

3. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 7.

4. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of singular values of $C$ that are greater than $\gamma$ .

5. If $\rho < n$ , reduce n to $\rho$ and m to $m - ( n - \rho )$ and return to Step 3.

6. Get $q$ from the null right singular vector b of $C$ and then p from the upper part of (27.6).

7. If $| b _ { 0 } | , \ldots , | b _ { \lambda - 1 } | \leq \mathrm { t o l }$ for some $\lambda \geq 1$ , zero the first $\lambda$ coefficients of $p$ and $q$ and cancel the common factor $z ^ { \lambda }$ .

8. If $| b _ { n + 1 - \lambda } | , \ldots , | b _ { n } | \leq \mathtt { t o l }$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $q$ . If $| a _ { m + 1 - \lambda } | , \ldots , | a _ { m } | \leq \tau$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $p$ .

9. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

10. Undo the scaling of Step 1 by redefining $\gamma ^ { j } a _ { j }$ as $a _ { j }$ and $\gamma ^ { j } b _ { j }$ as $b _ { j }$ for each $j$

Algorithm 27.2 has been implemented in a MATLAB code called padeapprox that is included in the Chebfun distribution, though it does not involve chebfuns. In its basic usage, padeapprox takes as input a vector $\mathbf { c }$ of Taylor coefficients together with a specification of $m$ and $n$ , with $\mathtt { t o l } = 1 0 ^ { - 1 4 }$ by default. For example, following [Gragg 1972], suppose

$$
f ( z ) = { \frac { 1 - z + z ^ { 3 } } { 1 - 2 z + z ^ { 2 } } } = 1 + z + z ^ { 2 } + 2 z ^ { 3 } + 3 z ^ { 4 } + 4 z ^ { 5 } + \cdots .
$$

Then the type $( 2 , 5 )$ Pad´e approximation of $f$ comes out with the theoretically correct exact type $( 0 , 3 )$ :

c = [1 1 (1:50)]; [r,a,b] $=$ padeapprox(c,2,5); disp(a.'), disp(b.')

Coefficients of numerator: 1.0000 Coefficients of denominator:

1.0000 -1.0000 0.0000 -1.0000

To illustrate the vital role of the SVD in such a calculation, here is what happens if robustness is turned off by setting $\tt t o l = 0$ :

[r,a,b] $=$ padeapprox(c,2,5,0); disp(a.'), disp(b.')

Coefficients of numerator:

1.0e+15 \*  
0.0000 -0.0000 3.4166

Coefficients of denominator:

0.0000 -0.0000 3.4166 -3.4166 0.0000 -3.4166

We now see longer vectors with enormous entries, on the order of the inverse of machine precision. The type appears to be $( 2 , 5 )$ , but the zeros and poles reveal that this is spurious:

disp(roots(a(end:-1:1))), disp(roots(b(end:-1:1)))

Zeros:

1.44015621657119e-16 + 1.71080672699754e-08i1.44015621657119e-16 - 1.71080672699754e-08iPoles:-0.341163901914009 + 1.16154139999725i-0.341163901914009 - 1.16154139999725i0.6823278038280191.44015621642544e-16 + 1.71080672699754e-08i1.44015621642544e-16 - 1.71080672699754e-08i

We see that the two zeros are virtually canceled by two poles that differ from them by only about $1 0 ^ { - 2 4 }$ . Thus this approximant has two spurious pole-zero pairs, or Froissart doublets, introduced by rounding errors. Many Pad´e computations over the years have been contaminated by such effects, and in an attempt to combat them, many authors have asserted that it is necessary to compute Pad´e approximations in high-precision arithmetic.

If padeapprox is called with a MATLAB function handle $f$ rather than a vector as its first argument, then it assumes $f$ is a function analytic in a neighborhood of the closed unit disk and computes Taylor coefficients by the FFT. For example, here is the type $( 2 , 2 )$ Pad´e approximant of $f ( z ) = \cos ( z )$ :

[r,a,b] = padeapprox(@cos,2,2); disp(a.'), disp(b.')

Coefficients of numerator: 1.000000000000000 0 -0.416666666666667   
Coefficients of denominator: 1.000000000000000 0 0.083333333333333

One appealing application of padeapprox is the numerical computation of block structure in the Pad´e table for a given function $f$ . For example, here is a table of the computed pair $( \mu , \nu )$ for each $( m , n )$ in the upper-left portion of the Pad´e table of $\cos ( z )$ with $0 \leq m , n \leq 8$ . One sees the $2 \times 2$ block structure resulting from the evenness of $\cos ( z )$ .

nmax $= ~ 8$ ; for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$

for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); fprintf(' (%1d,%1d)',mu,nu) end fprintf $( " \setminus " )$ end

(0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,8) (0,8) (2,8) (2,8) (4,8) (4,8) (6,8) (6,8) (8,8)

We can also show the block structure with a color plot, like this:

d = zeros(nmax $^ { + 2 }$ );   
rand('state',7); h = tan(2\*rand(50)-1); h(8,1) = 1;   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for m = 0:nmax $[ \mathbf { r } , \mathbf { a } , \mathbf { b } , \mathtt { m u } , \mathtt { n u } ] \ = \ \mathtt { p a d e a p p r o x } ( \mathtt { q c o s } , \mathtt { m } , \mathtt { n } ) ; \ \mathtt { d } ( \mathtt { n } + 1 , \mathtt { m } + 1 ) \ = \ \mathtt { h } ( \mathtt { m u } + 1 , \mathtt { n u } + 1 )$ ;   
end, end, pcolor(d), axis ij square off

Pad´e table of cos(z)

![](images/d1bcc5e47359d73544afa6fe38d9c72ede3bff9a0a46350c613c3fd463d7de52.jpg)

The pattern of $2 \times 2$ blocks is broken if we compute a larger segment of the table, such as $0 \leq m , n \leq 1 6$ :

nmax $\textstyle { \begin{array} { r l } \end{array} } = { \begin{array} { r l } { 1 6 } \end{array} }$ ; d = zeros(nmax+2);   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); d( $\mathtt { n } { + } 1$ ,m+1) = h(mu+1,nu+1);   
end, end, pcolor(d), axis ij square off

![](images/1f5924d667f3826fa7628b5e5879ac29b445e6eb79057f4275c3ed0ef985e38b.jpg)

What is going on here is that for $m + n$ greater than about 16, $\cos ( z )$ is resolved to machine precision, and the diagonal stripes of the plot show that padeapprox has automatically cut $m$ and $n$ down to this level.

For an “arbitrary” function $f$ with gaps in its Taylor series, the block structure can be quite intriguing, as illustrated by this example with $f ( z ) = 1 + z + z ^ { 4 } + z ^ { 7 } +$ $z ^ { 1 0 } + z ^ { 1 3 } + z ^ { 1 6 } + z ^ { 1 7 }$ :

$$
\begin{array} { r l } & { \mathrm { ~ \beta = ~ \Theta ( z ) ~ \gamma _ 1 + z + z _ { \perp } \cdot \gamma _ 4 + z _ { \perp } \cdot \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \psi ~ } } \mathrm {  ~ \psi ~ } } } } } \\ & { \mathrm { ~ \beta r ~ \mathrm { ~ n ~ \beta ~ = ~ 0 : n m a x , ~ \hat { \mathrm { ~ f ~ o r ~ ~ m ~ \psi ~ } } = ~ 0 : n m a x } ~ } } \\ & { \mathrm { ~ [ \hat { \mathrm { ~  ~ r ~ } } , \mathrm { ~ a ~ } , \mathrm { b ~ } , m u , n u ] ~ \mathrm { ~ \beta ~ = ~ \ p a d e a p p r o x ( \mathrm { ~ f ~ , ~ m ~ } , n ) ~ ; ~ \mathrm { ~ d ~ } ( n + 1 , m + 1 ) ~ \mathrm { ~ \beta ~ = ~ h ~ ( m u + 1 , n u + 1 ) ~ ; ~ \hat { \mathrm { ~ o r ~ } ~ } \mathrm { ~ \hat { \delta ~ } ~ } } ~ } } } \end{array}
$$

end, end, pcolor(d), axis ij square off

![](images/08a9b6677bb826de065fa36fe7c1499a670bc0e4d892b4dd93100a577ea21ee7.jpg)

Apart from $z ^ { 1 7 }$ , these are the initial terms of the Taylor series of

$$
f ( z ) = { \frac { 1 + z - z ^ { 3 } } { 1 - z ^ { 3 } } } ,
$$

an example for which Pad´e worked out the block structure for $0 \leq m \leq 7$ , $0 \leq n \leq 5$ [Pad´e 1892], showing vividly a $2 \times 2$ block, two $3 \times 3$ blocks, and the beginning of the infinite block at position $( 3 , 3 )$ .

In this chapter we have discussed how to compute Pad´e approximants, but not what they are useful for. As outlined in Chapter 23, applications of these approximations typically involve situations where we know a function in one region of the $z$ -plane and wish to evaluate it in another region that lies near or beyond certain singularities. The next chapter is devoted to practical exploration of such problems.

From a theoretical perspective, a central question for more than a century has been, what sort of convergence of Pad´e approximants of a function $f$ can we expect as $m$ and/or $n$ increase to $\infty$ ? In the simplest case, suppose that $f$ is an entire function, that is, analytic for all $z$ . Then for any compact set $K$ in the complex plane, we know that the type $( m , 0 )$ Pad´e approximants converge uniformly on $K$ as $m \to \infty$ , since these are just the Taylor approximants. One might hope that the same would be true of type $( m , n _ { 0 } )$ approximants for fixed $n _ { 0 } \geq 1$ as $m \to \infty$ , or of type $( n , n )$ approximants as $n \to \infty$ , but in fact, pointwise convergence need not occur in either of these situations. The problem is that spurious pole-zero pairs, Froissart doublets, may appear at seemingly arbitrary locations in the plane. As $m$ and/or $n$ increases, the doublets get weaker and their effects more localized, but they can never be guaranteed to go away. (In fact, there exist functions $f$ whose Pad´e approximants have so many spurious poles that the sequence of $( n , n )$ approximants is unbounded for every $z \neq 0$ [Perron 1929, Wallin 1972].) The same applies if $f$ is meromorphic, i.e., analytic apart from poles, or if it has more complicated singularities such as branch points. All this is true in exact mathematics, and when there are rounding errors on a computer, the doublets become ubiquitous.

Despite these complexities, important theorems have been proved. The theorem of de Montessus de Ballore [1902] concerns the case of $m \to \infty$ with fixed $n$ , guaranteeing convergence in a disk about $z = 0$ if $f$ has exactly $n$ poles there. The Nuttall– Pommerenke theorem [Nuttall 1970, Pommerenke 1973] concerns $m = \pi \to \infty$ and ensures convergence for meromorphic $f$ not pointwise but in measure or in capacity, these being precise notions that require accuracy over most of a region as $m , n \to \infty$ while allowing for localized anomalies. This result was powerfully generalized for functions with branch points by Stahl [1997], who showed that as $n  \infty$ , almost all the poles of type $( n , n )$ Pad´e approximants line up along branch cuts that have a property of minimal capacity in the $z ^ { - 1 }$ -plane. For discussion of these results see [Baker & Graves-Morris 1996]. There are also analogous results for multipoint Pad´e approximation and other forms of rational interpolation. For example, an analogue of the de Montessus de Ballore theorem for interpolation as in the last chapter was proved by Saff [1972].

As a practical matter, these complexities of convergence are well combated by the SVD approach we have described, which can be regarded as a method of regularization of the Pad´e problem.

For reasons explained in the last chapter, the whole discussion of this chapter has been based on the behavior of a function $f ( z )$ at $z = 0$ rather than this book’s usual context of a function $f ( x )$ on an interval such as $[ - 1 , 1 ]$ . There is an analogue of Pad´e approximation for $[ - 1 , 1 ]$ called Chebyshev–Pad´e approximation, developed by Hornecker [1956], Maehly [1963], Frankel and Gragg [1973], Clenshaw and Lord [1974], and Geddes [1981]. The idea is to consider the analogue of (27.3) for Chebyshev series rather than Taylor series:

$$
( f - r _ { m n } ) ( x ) = O ( T _ { \mathrm { m a x i m u m } } ( x ) ) .
$$

(The Maehly version starts from the analogue of the linearized form (27.5).) In analogy to Theorem 27.1, it turns out that any $r \in \mathcal { R } _ { m n }$ satisfying $( f - r ) ( x ) =$ $O ( T _ { m + n + 1 - d } ( x ) )$ is the unique Chebyshev–Pad´e approximant according to this definition, but now, there is no guarantee that such a function $T$ exists. For theoretical details, see [Trefethen & Gutknecht 1987], and for computations in Chebfun, there is a code chebpade. As of today, there has not yet been a study of Chebyshev–Pad´e approximation employing the SVD-based robustness ideas described in this chapter for Pad´e approximation.

For extensive information about Pad´e approximation, see the book by Baker and Graves-Morris [1996]. However, that monograph uses an alternative definition according to which a Pad´e approximant exists only if (27.4) can be satisfied, and in fact the present treatment is mathematically closer to the landmark review of Gragg [1972], which uses the definition (27.3).

Summary of Chapter 27. Pad´e approximation is the generalization of Taylor polynomials to rational approximation, that is, rational interpolation at a single point. Pad´e approximants are characterized by a kind of equioscillation condition and can be computed robustly by an algorithm based on the SVD. The analogue on the interval $[ - 1 , 1 ]$ is known as Chebyshev–Pad´e approximation.

Exercise 27.1. Pad´e approximation of a logarithm. Show from Theorem 27.1 that the function $f ( z ) = \log ( 1 + z )$ has Pad´e approximants $r _ { 0 0 } = 0$ , $r _ { 1 , 0 } ( z ) = z$ , $r _ { 0 1 } ( z ) = 0$ , and $r _ { 1 1 } = z / ( 1 + \textstyle { \frac { 1 } { 2 } } z )$ .

Exercise 27.2. Reciprocals and exponentials. (a) Suppose $r _ { m n }$ is the type $( m , n )$ Pad´e approximant to a function $f$ with $f ( 0 ) \neq 0$ . Show that $1 / r _ { m n }$ is the type $( n , m )$ Pad´e approximant to $1 / f$ . (b) As a corollary, state a theorem relating the $( m , n )$ and $( n , m )$ Pad´e approximants of $e ^ { z }$ .

Exercise 27.3. Prescribed block structures. Devise functions $f$ with the following structures in their Pad´e tables, and verify your claims numerically by color plots for $0 \leq$ $m , n \leq 2 0$ . (a) $3 \times 3$ blocks everywhere. (b) $1 \times 1$ blocks everywhere, except that $r _ { 1 1 } =$ $r _ { 2 1 } = r _ { 1 2 } = r _ { 2 2 }$ . (c) $1 \times 1$ blocks everywhere, except that all $r _ { m n }$ with $n \leq 2$ are the same.

Exercise 27.4. Order stars. The order star of a function $f$ and its approximation $r$ is the set of points $z$ in the complex plane for which $| f ( z ) | = | r ( z ) |$ . Use the MATLAB contour command to plot the order stars of the Pad´e approximations $r _ { 1 1 }$ , $r _ { 2 2 }$ , $r _ { 3 2 }$ , and $r _ { 2 3 }$ to $e ^ { z }$ . Comment on the behavior near the origin.

Exercise 27.5. Nonsingularity and normality. Show that for a given $f$ and $( m , n )$ , the Pad´e approximation $r _ { m n }$ has defect $d = 0$ if and only if the square matrix obtained by deleting the first column of (27.8) is nonsingular. (If all such matrices are nonsingular, the Pad´e table of $f$ is accordingly normal, with all its entries distinct.)

Exercise 27.6. Arbitrary patterns of square blocks? Knowing that degeneracies in the Pad´e table always occupy square blocks, one might conjecture that, given any tiling of the quarter-plane $m \geq 0$ , $n \geq 0$ by square blocks, there exists a function $f$ with this pattern in its Pad´e table. Prove that this conjecture is false. (Hint: Consider the case where the first two rows of the table are filled with $2 \times 2$ blocks [Trefethen 1984].)

Exercise 27.7. Continued fractions and the Pad´e table. If $d _ { 0 } , d _ { 1 } , \ldots$ is a sequence of numbers, the continued fraction

$$
d _ { 0 } + \frac { d _ { 1 } z } { 1 + \displaystyle \frac { d _ { 2 } z } { 1 + \cdot \cdot \cdot } }
$$

is shorthand for the sequence of rational functions

$$
d _ { 0 } , \ d _ { 0 } + d _ { 1 } z , \ d _ { 0 } + { \frac { d _ { 1 } z } { 1 + d _ { 2 } z } } , \ldots ,
$$

known as convergents of the continued fraction. (a) Show that if $d \sb { 0 } , \ldots , d \sb { k - 1 } \neq 0$ and $d _ { k } = 0$ , then (27.15) defines a rational function $r ( z )$ , and determine its exact type. (b) Assuming $d _ { k } \neq 0$ for all $k$ , show that the convergents are the Pad´e approximants of types $( 0 , 0 ) , ( 1 , 0 ) , ( 1 , 1 ) , ( 2 , 1 ) , ( 2 , 2 ) , \ldots$ of a certain formal power series.

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

![](images/8629c7df03e133bbf2924e062e7042469204fdfb0197a09f837a86ed316cdefd.jpg)

![](images/a2ca5ea5f99c523e430da9d6a5a1f689c7f5c975ce95610d127b90a29b00806b.jpg)

To get better information, we turn to rational approximation. A practical approach is to use ratinterp to compute rational linearized least-squares approximations of $f$ in $[ - 1 , 1 ]$ . Specifically, suppose we take $r$ to be the type $( 7 , 8 )$ approximation to $f$ in 1000 Chebyshev points and draw the same contour plots as before. The picture changes completely, showing very impressive agreement over most of the range plotted. This is the power and the promise of rational approximation.

d = domain(-1,1);   
[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,7,8,1000); $\mathbf { r } \mathbf { r } ~ = ~ \mathbf { r } \left( { \bf z } { \bf z } \right)$ ; subplot(1,2,1), contour(x,y,abs(ff),lev1,'k'), hold on contour(x,y,abs(ff),lev2,'r')   
subplot(1,2,2), contour(x,y,abs(rr),lev1,'k'), hold on contour(x,y,abs(rr),lev2,'r')

![](images/a2e22e6021bf581acff7c45ce58c23f10b19fa5be049f34363b77383d9206149.jpg)

![](images/f56962bce9da3e4c02fb137c3d8d7ab3aeb79d774a0995a3a226fe0db100b517.jpg)

For a direct measure of the accuracy of $r$ as an approximation to $f$ , we can look at $| f ( z ) - r ( z ) |$ . In the following plot the contours, from bottom to top, lie at $1 0 ^ { - 1 4 } , 1 0 ^ { - 1 2 } , \textrm { -- } , 1 0 ^ { - 2 }$ . Evidently the approximation is excellent over a wide region.

$\mathtt { l e v e l s \ = \ 1 0 \_ \hat { \ } ( - 1 4 : 2 : - 2 ) }$ ; contour(x,y,abs(ff-rr),levels,'k')

![](images/4a72e9fc14d019edb8529a1a25f24d4fd6c07b57513344bee9a57ef31d516c6a.jpg)

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

![](images/162d2e5dae70ccdf319789bcd980fe9124166566fef0af4445294e145a7058ec.jpg)

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

![](images/8bc50a0f5e4b96ca11c50508e652aebb691db3daa1b3ff1dc5d0b9a0f06d297a.jpg)

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

![](images/6d9bb5af3a37051ca1ddc3ad6f6613f5ce3a4982085af7398e06ef38c270de3f.jpg)

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

![](images/38f190837c274692b5cea20fae46462403b16b1e8502ef891a491d91f1f2f6b7.jpg)

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

![](images/aa94022df73a9a664b4cb4073759540e659b4caa33f59bc66b7ecbb3db693682.jpg)

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

![](images/2edb0421aeed0cb35fec4b75249de3dd62ed45cd325e542f313647aa5c6af9fd.jpg)  
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

![](images/78599dc4b0da7ac0e6e0cf1af144dc909d16f33b3aa04fcd15add5ffb367a116.jpg)  
Figure B.2: Absolute values of the Fourier coefficients of the trigfun for $\exp ( \sin t )$ on $[ 0 , 2 \pi ]$ . This is an entire function (analytic throughout the complex $t$ -plane), and in accordance with Theorem B.1, the coefficients decrease faster than geometrically.

![](images/6a92bdc582656533fb1f8420b436a60477d4bb01b47a97f6c6cd1ca66dbff1f9.jpg)  
Figure B.3: Trigfuns of $\operatorname { t a n h } ( 5 \sin t )$ and $\exp ( - 1 0 0 ( t + . 3 ) ^ { 2 } )$ (upper row) and corresponding absolute values of Fourier coefficients (lower row).