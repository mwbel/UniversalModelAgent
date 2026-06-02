# Chapter 20. Carath´eodory–Fej´er Approximation

We have seen that Chebyshev interpolants are near-best approximations in the sense that they come within a factor of at most $O ( \log n )$ of best approximations, usually even closer. For many applications, this is all one could ask for. But there is another kind of near-best approximations that are so close to best that for smooth functions, they are often indistinguishable from best approximations to machine precision on a computer. These are $\mathit { C F }$ (Carath´eodory–Fej´er) approximations, introduced by Gutknecht and Trefethen [1982]. Earlier related ideas were proposed in [Darlington 1970, Elliott 1973, Lam 1972, Talbot 1976], and the theoretical basis goes back to the early 20th century [Carath´eodory & Fej´er 1911, Schur 1918].10

Before explaining the mathematics of CF approximants, let us illustrate the remarkable degree of near-optimality they sometimes achieve. Here is the optimal $\infty$ -norm error in approximation of $f ( x ) = e ^ { x }$ on $[ - 1 , 1 ]$ by a polynomial of degree 2:

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); n = 2; pbest $=$ minimax(f,n); errbest $=$ norm(f-pbest,inf)

errbest $=$ 0.045017388402819

Here is the corresponding error for CF approximation computed by the Chebfun cf command:

pcf $=$ cf(f,n); errcf $=$ norm(f-pcf,inf)

errcf = 0.045017388414604

These two numbers agree to an extraordinary 9 significant digits. Comparing the best and CF polynomials directly to one another, we confirm that they are almost the same:

norm(pbest-pcf,inf)

# ans $=$ 1.178473985063988e-11

That was for degree $n = 2$ , and the near-optimality of the CF approximants grows stronger as $n$ increases. Let us explore the dependence on $n$ . On a semilog plot, the upper curve in the next figure shows the accuracy of the best polynomial as an approximation to $f ( x )$ , while the lower curve shows the accuracy of the CF polynomial as an approximation to the best polynomial. The two errors are of entirely different orders, and for $n > 3$ , the CF and best polynomials are indistinguishable in floating point arithmetic.

$\mathtt { n n } ~ = ~ 0 : 1 0$ ; err1 = []; err2 = [];   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/d76648981e8628108d5b09395f6a61f6be075bf549e534a3bc2852a9bae1cf7f.jpg)

Here is the same experiment repeated for $f ( x ) = \operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ .

f = tanh(4\*(x-.3)); ${ \tt n n } = 0 : 3 0$ ; err1 $=$ []; $\mathbf { e r r } 2 \ = \ \left[ \mathbf { } \mathbf { } \right]$ ;   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/4be6d2ec218d128b5ec2b6bae14ac23f7f20343d37b5af4b7c654d663efb5ad7.jpg)

Again we see that pbest−pcf is much smaller than f−pbest, implying that the CF approximant is for practical purposes essentially optimal. (Concerning the erratic oscillations, see Exercise 20.4.) Yet it is far easier to compute:

tic, minimax(f,20); tbest $=$ toc, tic, cf(f,20); tcf = toc

tbest $=$ 0.0389   
tcf $=$ 0.0098

Turning to a nonsmooth function, here again is the jagged example from Chapter 10 with its best approximation of degree 20:

f $=$ cumsum(sign(sin(20\*exp(x)))); plot(f,'k') tic, [pbest,err] $=$ minimax(f,20); tbest $=$ toc; hold on, plot(pbest)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/2355b5b8e5b6a93935c03f732071bf7d06024a4c20eb4cb53828d1a0facc24cd.jpg)

We saw the error curve before:

plot(f-pbest), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/609153f9f623bceea1209fd607f4b77668097bcd0d528f87550e6340eb16ec47.jpg)

In CF approximation, we must start from a polynomial, not a jagged function. As a rule of thumb, truncating the Chebyshev series at 5 times the degree of the desired approximation is usually pretty safe. Here is what we get:

$\yen 100 ~ =$ chebfun(f,100); tic, pcf $=$ cf(f100,20); tcf $=$ toc; plot(f-pcf), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/02fdd95c1b8a1523f0cf69d0f0ff4404ea19b9f4f87fce661df238205559118a.jpg)

Evidently the error falls short of optimality by just a few percent. Yet again the computation is much faster:

tbest, tcf

tbest $=$ 0.9996   
tcf $=$ 0.0105

Here for comparison is the error in Chebyshev interpolation.

pinterp $=$ chebfun(f,21); hold off, plot(f-pinterp), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/624b6a13cda812ad123b782025aa4cffc3ea886e50bd210045df8fe28faf4ce9.jpg)

The time has come to describe what CF approximation is all about. We shall see that the hallmark of this method is the use of eigenvalues and eigenvectors (or singular values and singular vectors) of a Hankel matrix of Chebyshev coefficients.

We start with a real function $f$ on $[ - 1 , 1 ]$ , which we want to approximate by a polynomial of degree $n \geq 0$ . Following Theorem 3.1, we assume that $f$ is Lipschitz continuous, so it has an absolutely convergent Chebyshev series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

Since our aim is polynomial approximation, there is no loss of generality if we suppose that $a _ { 0 } = a _ { 1 } = \cdot \cdot \cdot = a _ { n } = 0$ , so that the Chebyshev series of $f$ begins at the term $T _ { n + 1 }$ . For technical simplicity, let us further suppose that the series is a finite one, ending at the term $T _ { N }$ for some $N \geq n + 1$ . Then $f$ has the Chebyshev series

$$
f ( x ) = \sum _ { k = n + 1 } ^ { N } a _ { k } T _ { k } ( x ) .
$$

We now transplant $f$ to a function $F$ on the unit circle in the complex $z$ -plane by defining $F ( z ) = F ( z ^ { - 1 } ) = f ( x )$ for $| z | = 1$ , where $x = ( z + z ^ { - 1 } ) / 2$ . As in the proof of Theorem 3.1, this gives us a formula for $F$ as a Laurent polynomial,

$$
F ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } ( z ^ { k } + z ^ { - k } ) .
$$

We can divide $F ^ { \prime }$ into two parts, $F ( z ) = G ( z ) + G ( z ^ { - 1 } )$ , with

$$
G ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } z ^ { k } .
$$

The function $G$ is called the analytic part of $F$ , since it can be analytically continued to an analytic function in $| z | \le 1$ . Similarly $G ( z ^ { - 1 } )$ is the coanalytic part of $F ^ { \prime }$ , analytic for $1 \leq | z | \leq \infty$ .

Now we ask the following question: what is the best approximation $\ddot { P }$ to $G$ on the unit circle of the form

$$
\tilde { P } ( z ) = \frac { 1 } { 2 } \sum _ { k = - \infty } ^ { n } b _ { k } z ^ { k } ,
$$

where the series converges for all $z$ with $1 \leq | z | < \infty$ ? In other words, $\ddot { P }$ must be analytic in the exterior of the unit disk apart from a pole of order at most $n$ a t $z = \infty$ . This is the problem that Carath´eodory and Fej´er solved, and the solution is elegant. First of all, $\ddot { P }$ exists, and it is unique. Second, $G - \tilde { P }$ maps the unit circle onto a perfect circle that winds counterclockwise around the origin a number of times: the winding number is at least $n + 1$ . Third, as shown by Schur a few years after Carath´eodory and Fej´er [Schur 1918], $\ddot { P }$ can be constructed explicitly by solving a certain matrix singular value problem. Let $H$ denote the $( N - n ) \times ( N - n )$ real symmetric matrix of Chebyshev coefficients arranged like this,

$$
H = \left( \begin{array} { c c c c c } { a _ { n + 1 } } & { a _ { n + 2 } } & { a _ { n + 3 } } & { \ldots } & { a _ { N } } \\ { a _ { n + 2 } } & { a _ { n + 3 } } & { } & { } & { } \\ { a _ { n + 3 } } & { } & { } & { \ldots } & { } \\ { \vdots } & { } & { } & { } & { } \\ { a _ { N } } & { } & { } & { } & { } \end{array} \right) ,
$$

where the entries in the lower-right triangle are zero. A matrix with this structure, constant along diagonals so that $a _ { i j }$ depends only on $i + j$ , is called a Hankel matrix. Let $\lambda$ be the largest eigenvalue of $H$ in absolute value, let $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { N - n - 1 } ) ^ { T }$ be a corresponding real eigenvector, and define

$$
u ( z ) = u _ { 0 } + u _ { 1 } z + \cdot \cdot \cdot + u _ { N - n - 1 } z ^ { N - n - 1 } .
$$

Here is the theorem due to Carath´eodory and Fej´er and Schur.

Theorem 20.1. Carath´eodory–Fej´er–Schur theorem. The approximation problem described above has a unique solution $\ddot { P }$ , and it is given by the error formula

$$
( G - \tilde { P } ) ( z ) = \lambda z ^ { n + 1 } \frac { u ( z ) } { u ( z ) } .
$$

The function $G - \tilde { P }$ maps the unit circle to a circle of radius $| \lambda |$ and winding number $\geq n + 1$ , and if $| \lambda | > | \mu |$ for all other eigenvalues $\mu$ , the winding number is exactly $n + 1$ .

Proof. The result is due to Carath´eodory and Fej´er [1911] and Schur [1918]. See Theorem 1.1 of [Gutknecht & Trefethen 1982] and Theorem 4 of [Hayashi, Trefethen $\&$ Gutknecht 1990].

Theorem 20.1 is a mathematical assertion about the approximation of a function $G$ on the unit circle by an infinite series. We use this result to construct the polynomial CF approximant as follows. Since $G - \tilde { P }$ maps the unit circle to a circle of winding number $\geq n + 1$ , its real part (times 2)

$$
( G - { \tilde { P } } ) ( z ) + ( G - { \tilde { P } } ) ( z ^ { - 1 } )
$$

maps the unit circle to an equioscillating curve with at least $n + 2$ extreme points. Thus the function

$$
\tilde { p } ( x ) = \tilde { P } ( z ) + \tilde { P } ( z ^ { - 1 } )
$$

yields the equioscillatory behavior that characterizes a best approximation polynomial of degree $n$ to $f ( x )$ on $[ - 1 , 1 ]$ (Theorem 10.1). Unfortunately, $\tilde { p } ( x )$ is not a polynomial of degree $n$ . However, it will generally be very close to one. The function $\ddot { P }$ will normally have Laurent series coefficients $b _ { k }$ that decay as $k \to - \infty$ . We truncate these at degree $- n$ to define

$$
\mathcal { P } _ { _ \mathrm { C F } } ( z ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } b _ { k } z ^ { k } ,
$$

with real part (times 2)

$$
p _ { _ { \mathrm { C F } } } ( x ) = \mathcal { P } _ { _ { \mathrm { C F } } } ( z ) + \mathcal { P } _ { _ { \mathrm { C F } } } ( z ^ { - 1 } ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } ( b _ { k } + b _ { - k } ) z ^ { k } .
$$

If the truncated terms are small, $f - p _ { \mathrm { { C F } } }$ maps $[ - 1 , 1 ]$ to a curve that comes very close to equioscillation with $\geq n + 2$ extrema, and thus $p _ { \mathrm { C F } }$ is close to optimal.

For more details on real polynomial CF approximation, with numerical examples, see [Gutknecht $\&$ Trefethen 1982], [Trefethen 1983], and [Hayashi, Trefethen $\&$ Gutknecht 1990].

Our experiments in the opening pages of this chapter showed that CF approximants can be exceedingly close to best. The truncation described above gives an idea of how this happens. In the simplest case, suppose $f$ is an analytic function on $\lfloor - 1 , 1 \rfloor$ . Then by Theorem 8.1, its Chebyshev coefficients decrease geometrically, and let us suppose that this happens smoothly at a rate $a _ { k } = O ( \rho ^ { k } )$ . Then, roughly speaking, the dominant degree $n + 1$ term of $f$ is of order $\rho ^ { - n - 1 }$ , and the terms $b _ { n } , b _ { n - 1 } , \ldots , b _ { - n }$ are of orders $\rho ^ { - n - 2 } , \rho ^ { - n - 3 } , \cdot \cdot \cdot , \rho ^ { - 3 n - 2 }$ . This suggests that the truncation in going from $\tilde { p }$ to $p _ { \mathrm { C F } }$ will introduce an error of order $\rho ^ { - 3 n - 3 }$ . This is usually a very small number and, in particular, much smaller than the error $\| f - p ^ { * } \|$ of order $\rho ^ { - n - 1 }$ .

In fact, the actual order of accuracy for polynomial CF approximation is one order higher, $\rho ^ { - 3 n - 4 }$ rather than $\rho ^ { - 3 n - 3 }$ . (The reason is that the first truncated term is a multiple of $T _ { 3 n + 3 }$ , the same Chebyshev polynomial that dominates the error $f - p ^ { * }$ itself, and so it is not until the second truncated term, $T _ { 3 n + 4 }$ , that the equioscillation is broken.) On the other hand, to go from this rough argument to a precise theorem is not so easy, because in fact, Chebyshev series need not decay smoothly (Exericse 20.3). Here we quote without proof a theorem from [Gutknecht $\&$ Trefethen 1982].

Theorem 20.2. Accuracy of polynomial CF approximation. For any fixed $m \geq 0$ , let $f$ have a Lipschitz continuous $( 3 m + 3 ) r d$ derivative on $[ - 1 , 1 ]$ with a nonzero $( m + 1 ) s t$ derivative at $x = 0$ , and for each $s \in ( 0 , 1 ]$ , let $p ^ { * }$ and $p _ { { _ { C F } } }$ $b e$ the best and the $\mathit { C F }$ approximations of degree $_ { \mathbf { \nabla } ^ { \prime } \mathbf { \nabla } ^ { \prime } } \psi _ { \mathbf { \nabla } ^ { \prime } }$ to $f ( s x )$ on $[ - 1 , 1 ]$ , respectively. Then as $s \to 0$ ,

$$
\| f - p ^ { * } \| = O ( s ^ { m + 1 } )
$$

and

$$
\| f - p ^ { * } \| \neq O ( s ^ { m + 2 } )
$$

and

$$
\| p _ { { \scriptscriptstyle C F } } - p ^ { * } \| = O ( s ^ { 3 m + 4 } ) .
$$

Proof. See Theorem 3.4 of [Gutknecht $\&$ Trefethen 1982].

We can verify this result numerically. The two plots below display norms for $m = 1$ and $m = 2$ for the function $f ( x ) = e ^ { 5 x }$ .

${ \bf f } { \bf f } = \mathbb { Q } ( { \bf x } ) \exp ( { \sf5 * x } )$ ;   
for $\texttt { m } = \texttt { 1 : 2 }$ $\begin{array} { r } { \sin \mathtt { s s } = \mathtt { \Omega } . 8 . \hat { \mathbf { \Omega } } ^ { } ( 0 : 2 0 ) \mathrm { { ; ~ \ e r r f { p } ~ = ~ [ ] ~ ; ~ \ e r r p p ~ = ~ [ ] ~ ; ~ } } } \end{array}$ for $\mathrm { ~ \mathsf ~ { ~ s ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ s ~ s ~ } ~ }$ $\begin{array} { r l } { \underline { { \mathsf { f } } } } & { { } = } \end{array}$ chebfun(@(x) ff(s\*x)); pbest $=$ minimax(f,m); pcf $=$ cf(f,m); errfp $=$ [errfp norm(f-pbest,inf)]; errpp $=$ [errpp norm(pcf-pbest,inf)]; end loglog(ss,errfp,'.-') hold on, loglog(ss,errpp,'.-r'), loglog(ss,ss.^(m+1),'--'); $\textbf { s } = \ 0 . 0 2 5$ ; loglog(ss,ss.^( $3 * \mathtt { m } + 4 ,$ ,'--r')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/68087d695ebf3f3fdcfb8ad852a5d9a9b57f103c80be00428449070e4b348699.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/87d97e3db79daad033ecea33113cd8dd5bcd46a194ee686febc205072474fffe.jpg)

In this chapter we have considered CF approximation in its simplest context of approximation of one polynomial $f$ of degree $N$ by another polynomial $p _ { \mathrm { C F } }$ of degree $n$ . In fact, the method is much more general. So long as $f$ has an absolutely convergent Chebyshev series, which is implied, for example, if it is Lipschitz continuous, then Theorem 20.1 still applies [Hayashi, Trefethen $\&$ Gutknecht 1990]. Now $H$ is an infinite matrix which can be shown to represent a compact operator on $\ell ^ { 2 }$ or $\ell ^ { 1 }$ , its dominant eigenvector is an infinite vector, and $u ( z )$ is defined by an infinite series. The error curve is still a continuous function of winding number at least $n + 1$ .

Another generalization is to approximation by rational functions rather than polynomials. Everything goes through in close analogy to what has been written here, and now the other eigenvalues of the Hankel matrix come into play. The theoretical underpinnings of rational CF approximation can be found in papers of Takagi [1924], Adamjan, Arov, and Krein [1971], and Trefethen and Gutknecht [1983b], as well as the article by Hayashi, Trefethen, and Gutknecht cited above. Quite apart from theory, one can compute these approximations readily by the Chebfun cf command using capabilities introduced by Joris Van Deun. For details and examples see [Van Deun & Trefethen 2011].

Further generalizations of CF approximation concern approximation of vector or matrix functions rather than just scalars, and here, such techniques are associated with the name $H _ { \infty }$ approximation. An important early paper was Glover [1984], and there have been many extensions and generalizations since then [Antoulas 2005, Zhou, Doyle $\&$ Glover 1996].

We have emphasized the practical power of CF approximants as providing nearbest approximations at low computational cost. The conceptual and theoretical significance of the technique, however, goes beyond this. Indeed, the eigenvalue/singular value analysis of Carath´eodory–Fej´er approximation seems to be the principal known algebraic window into the detailed analysis of best approximations, and in most cases where best approximations of a function happen to be known exactly, these best approximations are CF approximations in which an approximant like $\tilde { P }$ or $\ddot { p }$ already has the required finite form, so that nothing needs to be truncated to get to $P$ or $p$ [Gutknecht 1983].

Summary of Chapter 20. Carath´eodory–Fej´er approximation constructs near-best approximations of a function $f \in C ( [ - 1 , 1 ] )$ from the singular values and vectors of a Hankel matrix of Chebyshev coefficients. If $f$ is smooth, CF approximants are often indistinguishable in machine precision from true best approximants.

Exercise 20.1. Approximating $\cos ( n x )$ . (a) For $n = \mathrm { 2 } , \mathrm { 4 } , \mathrm { 8 } , \mathrm { 1 6 } , \dots$ , compute the degree $_ { n }$ CF approximant to $f ( x ) = \cos ( n x )$ and plot the error curve. How high can you go in this sequence? (b) What happens if $\cos ( n x )$ is changed to $\cos ( 0 . 9 n x )$ ?

Exercise 20.2. Approximating the jagged function. Four of the figures of this chapter concerned approximations of degree 20 to a jagged function. (a) How do the $L ^ { 2 }$ norms of the best and CF approximations compare? (b) The CF approximation was based on truncation of the Chebyshev series at term $N = 1 0 0$ . How does the $\infty$ -norm of the error vary with $N$ ? (c) Draw a conclusion from this exploration: is the imperfect equioscillation of the error curve in the figure given in the text for this function mostly due to the fact that CF approximation is not best approximation, or to the fact that $N < \infty$ ?

Exercise 20.3. Complex approximation on the unit disk. (a) Suppose $f$ is an analytic function on the closed unit disk and $p$ is a polynomial of degree $_ n$ . Prove that $p$ is a best approximation to $f$ in the $\infty$ -norm on the disk $| z | \le 1$ if and only if it is a best approximation on the circle $| z | = 1$ . (b) Look up Rouch´e’s theorem and write down a careful statement, citing your source. (c) Suppose $f$ is an analytic function in the closed unit disk and $p$ is a polynomial of degree $_ n$ such that $f - p$ maps the unit circle to a circle of winding number at least $n + 1$ . Prove that $p$ is a best approximation to $f$ on the unit disk. (In fact it is unique, though this is not obvious.)

Exercise 20.4. Irregularity of CF approximation. The second figure of this chapter showed quite irregular dependence of $\| p _ { \mathrm { C F } } - p ^ { * } \|$ on the degree $n$ for the function $f ( x ) =$ $\operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ . In particular, $n = 1 5$ and $n = 1 6$ give very different results. Following the derivation of $p _ { \mathrm { { C F } } }$ in the text, investigate this difference numerically. (a) For $n = 1 5$ , how do the coefficients $\left| b _ { k } \right|$ depend on $k$ , and how big are the truncated terms in going from $\ddot { p }$ to $p _ { \mathrm { C F } }$ ? (b) Answer the same questions for $n = 1 6$ .
