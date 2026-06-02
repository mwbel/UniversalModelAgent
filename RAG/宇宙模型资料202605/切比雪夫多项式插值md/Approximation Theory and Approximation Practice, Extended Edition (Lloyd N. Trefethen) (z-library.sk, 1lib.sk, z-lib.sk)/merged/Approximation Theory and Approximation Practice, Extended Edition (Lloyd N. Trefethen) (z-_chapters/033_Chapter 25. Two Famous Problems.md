# Chapter 25. Two Famous Problems

In this chapter we discuss two problems of rational approximation that have been the focus of special attention over the years: approximation of $| x |$ on $[ - 1 , 1 ]$ , a prototype of approximation of nonsmooth functions, and approximation of $e ^ { x }$ on $( - \infty , 0 ]$ , a prototype of approximation on unbounded domains. Both stories go back many decades and feature initial theorems, later conjectures based on numerical experiments, and eventual proofs of the conjectures based on mathematical methods related to potential theory. We shall not present the proofs of the sharpest results, but we shall show that the essential rates of approximation can be achieved by using the trick that appears several times in this book: if a function $f ( x )$ can be written as an integral with respect to a variable $s$ , then an approximation $r ( x )$ in partial fractions form is obtained by applying a quadrature formula (19.3) to the integral.

The problem of approximation of $| x |$ on $[ - 1 , 1 ]$ originates at the beginning of the 20th century, when polynomial approximations of this function were of interest to Lebesgue, de la Vall´ee Poussin, Jackson, and Bernstein (Exercise 6.5). This was an era when the fundamental results of approximability were being developed, and $| x |$ served as a function from which many other results could be derived. Bernstein’s prize-winning article on the subject ran for 104 pages [1912b] and was followed by another of 57 pages [1914b]. Among other things, Bernstein proved that in best polynomial approximation of $| x |$ as $n  \infty$ , the errors decrease linearly but no faster, that is, at the rate $O ( n ^ { - 1 } )$ but not $o ( n ^ { - 1 } )$ .

Why linearly? This is an example of the fundamental principle mentioned first in Chapter 7: the close connection between the smoothness of a function and its rate of approximation. The function $f ( x ) = | x |$ has a derivative of bounded variation $V = 2$ on $[ - 1 , 1 ]$ , so by Theorem 7.2, its Chebyshev projections $\{ f _ { n } \}$ satisfy

$$
\| f - f _ { n } \| \leq { \frac { 4 } { \pi ( n - 1 ) } }
$$

for $n \geq 2$ , and its Chebyshev interpolants $\left\{ p _ { n } \right\}$ satisfy the same bound with 4 replaced by 8. Thus approximations to $| x |$ converge at least at the rate $O ( n ^ { - 1 } )$ . What Bernstein showed is that the rate is in fact no better than this: no approximations to $| x |$ can beat Chebyshev projection or interpolation by more than a constant factor. Or to put it another way, convergence of polynomial approximants to a function $f$ at a rate faster than $O ( n ^ { - 1 } )$ implies that $f$ is in some sense smoother than $| x |$ . Such results in the direction approximability $\Longrightarrow$ smoothness go by the general name of Bernstein theorems. In this book we have presented one result of this kind, Theorem 8.3, asserting that geometric convergence implies analyticity.

It is hard not to be curious about the constants. Bernstein in fact proved in [Bernstein 1914b] that there exists a number $\beta$ such that the best approximation errors satisfy

$$
E _ { n } ( | x | ) \sim { \frac { \beta } { n } }
$$

as $n \to \infty$ , and he obtained the bound

$$
0 . 2 7 8 < \beta < 0 . 2 8 6 .
$$

(Theorem 7.2 gives $\beta \leq 4 / \pi \approx 1 . 2 7 .$ .) He noted as a “curious coincidence” that $1 / 2 \sqrt { \pi } \approx 0 . 2 8 2 0 9 \ldots$ falls in this range, and the idea that $\beta$ might take exactly this value became known as Bernstein’s conjecture. Seventy years later, Varga and Carpenter [1985] investigated the problem numerically to great accuracy and found that in fact

$$
\beta \approx 0 . 2 8 0 1 6 9 4 9 9 0 2 3 8 6 9 1 3 3 0 3 6 4 3 6 4 9 \ldots
$$

(Of course the difference between 0.282 and 0.280 would not have the slightest practical importance.) Along with this numerical result, which was based on Richardson extrapolation, Varga and Carpenter established the rigorous bounds

$$
0 . 2 8 0 1 6 8 5 < \beta < 0 . 2 8 0 1 7 3 4 .
$$

For example, here are the values of $n E _ { n } ( | x | )$ for $n = 1 , 2 , 4 , \dots , 6 4$ , showing quadratic convergence to the limit value. A comparison with the much more accurate Table 2.1 of [Varga & Carpenter 1985] indicates that the Chebfun results are accurate in all but the last digit or two.

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); f = abs(x); limit $=$ 0.280169499023869133;   
for n = 2.^(0:6) [p,err] $=$ minimax(f,n); fprintf('%14d %16.8f %16.2e\n',n,n\*err,n\*err-limit)   
end

<table><tr><td>n</td><td>n*err</td><td>n*err - limit</td></tr><tr><td>1</td><td>0.50000000</td><td>2.20e-01</td></tr><tr><td>2</td><td>0.25000000</td><td>-3.02e-02</td></tr><tr><td>4</td><td>0.27048360</td><td>-9.69e-03</td></tr><tr><td>8</td><td>0.27751782</td><td>-2.65e-03</td></tr><tr><td>16</td><td>0.27948884</td><td>-6.81e-04</td></tr><tr><td>32</td><td>0.27999815</td><td>-1.71e-04</td></tr><tr><td>64</td><td>0.28012659</td><td>-4.29e-05</td></tr></table>

Now all this is for polynomial approximation. What about rational functions? As mentioned in Chapter 23, the dramatic discovery here came from Donald Newman, 50 years after Bernstein: best rational approximants to $| x |$ converge “rootexponentially.” Newman’s bounds were these:

$$
\frac { 1 } { 2 } e ^ { - 9 \sqrt { n } } \leq E _ { n n } ( | x | ) \leq 3 e ^ { - \sqrt { n } } .
$$

We have already seen in the second plot of Chapter 23 what an improvement in convergence rate this is as compared with (25.1). For approximating nonsmooth functions, rational functions can be far more powerful than polynomials.

Again mathematicians could not resist trying to sharpen the constants. First, Vyacheslavov [1975] found that the exact exponent is midway between Newman’s bounds of 1 and 9: it is $\pi$ . Then Varga, Ruttan, and Carpenter [1993] performed computations with a version of the Remez algorithm to 200 decimal places, leading to numerical evidence for the conjecture

$$
E _ { n n } \sim 8 e ^ { - \pi { \sqrt { n } } }
$$

as $n  \infty$ . Soon afterward this result was proved by Stahl [1993]. Later Stahl generalized the result to approximation of $x ^ { \alpha }$ on $[ 0 , 1 ]$ for any $\alpha > 0$ [Stahl 2003].

The following theorem summarizes the results we have mentioned.

Theorem 25.1. Approximation of $| x |$ on $[ - 1 , \bf 1 ]$ . The errors in best polynomial and rational approximation of $| x |$ on $[ - 1 , 1 ]$ satisfy as $n \to \infty$

$$
E _ { n 0 } ( | x | ) \sim \frac { \beta } { n } , \quad \beta = 0 . 2 8 0 1 \ldots ,
$$

and

$$
E _ { n n } ( \vert x \vert ) \sim 8 e ^ { - \pi { \sqrt { n } } } .
$$

Proof. Equation (25.4) is due to Varga and Carpenter [1985], and (25.5) is due to Stahl [1993].

Why can rational approximations of $| x |$ achieve $O ( C ^ { - \sqrt { n } } )$ accuracy? The crucial fact is that the poles of $r$ can be chosen to cluster near the singular point $x = 0$ . In particular, a good choice is to make the poles approach 0 geometrically, for each fixed $n$ , with a geometric factor depending on $\sqrt { n }$ .

Here is a derivation of a rational approximation that achieves the right rootexponential convergence. (Arguments like this have been made by Stenger in various publications; see, for example, [Stenger 1986].) We start from the identity

$$
\frac { 1 } { | x | } = \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } \frac { d t } { t ^ { 2 } + x ^ { 2 } } ,
$$

which is derived in calculus courses. Multiplying by $x ^ { 2 }$ gives

$$
| x | = { \frac { 2 x ^ { 2 } } { \pi } } \int _ { 0 } ^ { \infty } { \frac { d t } { t ^ { 2 } + x ^ { 2 } } } .
$$


<!-- chunk 0004: pages 211-280 -->
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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/cb2cc26b80ce5a52caaed3b5c6470377411b761de70ff44511665e1fddcc7b45.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/becf66a58b9e5c05e1a7583a0cfa870af25b853b965c729413383fe622ae605f.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a53178e113481cdc5cff0f9fd61f90f98fd58b1541b27f4ec150fa914301216f.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/3e8d41548190afd51e3d6f0652968652ec9e34cbbd699d04204fe73f05ad89df.jpg)

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

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/51a7bceac042511ae0e9b7e05af9f6ac74389ce54a1ecede84ecbd6ca3ad4a6f.jpg)

This gives us yet another way to compute rational approximations to $e ^ { x }$ on $( - \infty , 0 ]$ : truncate this Chebyshev series in $s$ , and then transplant by (25.19) to get rational functions in $x$ .

Alternatively, we can get true best approximations from (25.19) by applying the Chebfun minimax command. Here, for example, is the error for the best approximation of type $( 8 , 8 )$ plotted in the $s$ variable, showing 18 points of equioscillation.

[P,Q,RH,err] $=$ minimax(F,8,8); $\mathtt { R } \ = \ \mathtt { P } / \mathtt { Q }$ ; plot(F-R), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/19010920f0ecc626278b032a01e08552bb2f555b4da4b13e4b32bce56754a27f.jpg)

If we plot the same curve in the $x$ variable, it’s hard to see much because of the varying scale:

${ \bf s } 1 ~ = ~ - . 9 9 9$ ; s2 = .999; s = chebfun('s',[s1 s2]); $\textbf { x } = ~ 9 * \left( \mathbf { s } \mathbf { - } 1 \right) / \left( \mathbf { s } + 1 \right)$ ; plot(x,F{s1,s2}-R{s1,s2}), hold on $\bf { x } \bf { x } ~ = ~ [ - 1 e 4 ~ - 1 e - 2 ]$ ; plot(xx,err\*[1,1],'--k') plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f15b47e1106e1e775122ce5d66eb94578ba89660daed32b24abb34e65c922e0c.jpg)

Putting the $x$ -axis on a log scale, however, makes the plot informative again:

semilogx(x,F{s1,s2}-R{s1,s2}), hold on semilogx(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/bb34a2dee411d4a350616e3d4bc53e5a10171dd4c0b7141577f260b91cea6342.jpg)

Here is the analogous plot for type (12, 12) approximation:

[P,Q,RH,err] $=$ minimax(F,12,12); $\mathtt { R } \ = \ \mathtt { P } . / \mathtt { Q }$ ;$\mathbf { s e m i l o g x } ( \mathbf { x } , \mathbf { F } \{ \mathbf { s } 1 , \mathbf { s } 2 \} - \mathbb { R } \{ \mathbf { s } 1 , \mathbf { s } 2 \} )$ , hold onplot(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f38b49fe9b0b8ca55739285215fc25a6be46e8ebb86ca2d216306184305efbf7.jpg)

These plots are modeled after [Trefethen, Weideman & Schmelzer 2006], where it is shown that Carath´eodory–Fej´er approximation is equally effective and even faster than the Remez algorithm at computing these approximations.

Summary of Chapter 25. Two problems involving rational functions have attracted special attention, highlighting the power of rational approximations near singularities and on unbounded domains. For approximating $| x |$ on $[ - 1 , 1 ]$ , best rational functions converge root-exponentially, whereas polynomials converge linearly. For approximating $e ^ { x }$ on $( - \infty , 0 ]$ , best rational functions converge geometrically, whereas polynomials do not converge at all. Both rates of approximation can be achieved by constructing partial fractions from trapezoidal rule approximations to certain integrals.

Exercise 25.1. Newton iteration for $| { \pmb x } |$ . (This problem has roots in [Roberts 1980].) (a) Let $_ x$ be a number, and suppose we want to solve the equation $r ^ { 2 } = x ^ { 2 }$ for the unknown $r$ using Newton iteration. Show that the iteration formula is $r ^ { ( k + 1 ) } = ( ( r ^ { ( k ) } ) ^ { 2 } +$ $x ^ { 2 } ) / 2 r ^ { ( k ) }$ . (b) If the initial guess is $r ^ { ( 0 ) } = 1$ , then for $k \geq 1$ , what is the smallest $_ n$ for which the rational function $r ^ { ( k ) } ( x )$ is of type $( n , n )$ ? (c) Use Chebfun to compute and plot the approximations $r ^ { ( 0 ) } ( x ) , \ldots , r ^ { ( 5 ) } ( x )$ on the interval $[ - 1 , 1 ]$ . What is the sup-norm error $\| | x | - r ^ { ( k ) } ( x ) \|$ , and where is it attained? (d) What rate of convergence does this correspond to for $\| | x | - r ^ { ( k ) } ( x ) \|$ as a function of $n$ ? How does this compare with the optimal rate given by Theorem 25.1? (e) Make a semilog plot of $| | x | - r ^ { ( 5 ) } ( x ) |$ as a function of $x \in [ - 1 , 1 ]$ and comment further on the nature of these rational approximations.

Exercise 25.2. An elementary approximant for $e ^ { \alpha }$ on $( - \infty , \mathbf { 0 } ]$ . (a) A degree $n$ polynomial $p ( s )$ on $[ - 1 , 1 ]$ can be transplanted to a type $( n , n )$ rational function $r ( x )$ on $( - \infty , 0 ]$ by the map (25.19). Combine this observation with Theorem 8.2 to show that type $( n , n )$ approximants to $e ^ { x }$ on $( - \infty , 0 ]$ exist with accuracy $O ( \exp ( - C n ^ { - 2 / 3 } ) )$ . (b) How does the $n ^ { - 2 / 3 }$ prediction match the data in the curve after (25.20)?

Exercise 25.3. Computing Halphen’s constant. Write a short Chebfun program that computes Halphen’s constant to 10 or more digits based on the condition (25.12).

Exercise 25.4. Best approximation errors for $e ^ { \alpha }$ . (a) Using minimax and the change of variables (25.20), compute best approximation errors in type $( n , n )$ approximation of $e ^ { x }$ on $( - \infty , 0 ]$ for $n = 0 , 1 , \ldots , 1 3$ . Plot the results on a log scale and compare them with estimates from the asymptotic formula (25.18). Also on a log scale, plot the difference between the estimates and the true errors, and comment on the results. (b) Repeat the computation with CF instead of minimax. This time, plot the difference between the CF and true errors on a log scale, and comment on the results.

Exercise 25.5. Behavior of approximants of $| { \pmb x } |$ in the complex plane. It is shown in [Blatt, Iserles & Saff 1987] that the type $( n , n )$ best approximants to $| x |$ on $[ - 1 , 1 ]$ have all their zeros and poles on the imaginary axis and converge to $_ x$ for $\operatorname { R e } ( x ) > 0$ and to $- x$ for $\mathrm { R e } ( x ) < 0$ as $n \to \infty$ . Verify this result numerically by plotting $| x - r _ { n n } ^ { * } ( x ) |$ against $\mathrm { R e } ( x )$ for $x \in [ - 1 + 0 . 5 i , 1 + 0 . 5 i ]$ for $n = 1 , 2 , 3 , 4$ .

Exercise 25.6. Behavior of approximants of $e ^ { \alpha }$ in the complex plane. It is stated in [Stahl & Schmelzer 2009] that the poles of best type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ move off to $\infty$ as $n \to \infty$ , and the convergence at $n$ th-root rate governed by $H \approx 1 / 9 . 2 8 9 0 3$ applies on any compact set in the complex plane. With this result in mind, produce contour plots in the complex $z$ -plane for the errors $\displaystyle | e ^ { z } - r _ { n n } ( z ) |$ for the approximations (25.14)–(25.15) with $n = 2 , 4 , 6 , 8 , 1 0$ . Does it appear likely that these approximations too converge on all compact sets in the plane?
