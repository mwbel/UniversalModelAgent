# Chapter V. Multistep Methods for Stiff Problems

Multistep methods (BDF) were the first numerical methods to be proposed for stiff differential equations (Curtiss & Hirschfelder 1952) and since Gear's book (1971) computer codes based on these methods have been the most prominent and most widely used for all stiff computations.

This chapter introduces the linear stability theory for multistep methods in Sect.V.1,and arrives at the famous theorem of Dahlquist which says that $A$ -stable multistep methods cannot have high order. Attempts to circumvent this barrier proceed mainly in two directions: either study methods with slightly weaker stability requirements (Sect. V.2) or introduce new classes of methods (Sect. V.3). Order star theory on Riemann surfaces (Sect. V.4) then helps to extend Dahlquist's barrier to generalized methods and to explain various properties of stability domains. Sec-tion V.5 presents numerical experiments with several codes based on the methods introduced.

Since allthe foregoing stability theory is based uniquely on linear autonomous problems $y ^ { \prime } = A y$ , the question arises of their validity for general nonlinear problems. This leads to the concepts of $G$ -stability for multistep methods (Sect. V.6) and algebraic stability for general linear methods (Sect. V.9).

Another important subject is convergence estimates for $h  0$ which are independent of the stiffness (the analogue of $B$ -convergence in Sect.IV.15). We describe various techniques for obtaining such estimates in Sections V.7 (for linear problems) as well as V.6 and V.8 (for nonlinear problems). These techniques are: use of $G$ -stability, the Kreiss matrix theorem,the multiplier technique and, last but not least, a discrete variation of constants formula.

# V.1 Stability of Multistep Methods

A general $k$ -step multistep method is of the form

$$
\alpha _ { k } y _ { m + k } + \alpha _ { k - 1 } y _ { m + k - 1 } + \ldots + \alpha _ { 0 } y _ { m } = h ( \beta _ { k } f _ { m + k } + \ldots + \beta _ { 0 } f _ { m } ) .
$$

For this method, we can do the same stability analysis as in Sect.IV.2 for Euler's method. This means that we apply it to the linearized and autonomous system

$$
y ^ { \prime } = J y
$$

(see (IV.2.2')); this gives

$$
\alpha _ { k } y _ { m + k } + . . . + \alpha _ { 0 } y _ { m } = h J ( \beta _ { k } y _ { m + k } + . . . + \beta _ { 0 } y _ { m } ) .
$$

We again introduce a new basis for the vectors $y _ { m + \imath }$ consisting of the eigenvectors of $J$ . Then for the coefficients of $y _ { m + \imath }$ ， with respect to an eigenvector $v$ f $J$ ， we obtain exactly the same reccurrence equation as (1.3), with $J$ replaced by the corresponding eigenvalue $\lambda$ . This gives 1

$$
( \alpha _ { k } - \mu \beta _ { k } ) y _ { m + k } + \hdots + ( \alpha _ { 0 } - \mu \beta _ { 0 } ) y _ { m } = 0 , \qquad \mu = h \lambda
$$

and is the same as Method (1.1) applied to Dahlquist's test equation

$$
y ^ { \prime } = \lambda y .
$$

# The Stability Region

The difference equation (1.4) is solved using Lagrange's method (see Volume I, Sect. II1.3): we set $y _ { \jmath } = \zeta ^ { \jmath }$ , divide by $\zeta ^ { m }$ and obtain the characteristic equation

$$
( \alpha _ { k } - \mu \beta _ { k } ) \zeta ^ { k } + . . . + ( \alpha _ { 0 } - \mu \beta _ { 0 } ) = \varrho ( \zeta ) - \mu \sigma ( \zeta ) = 0
$$

which depends on the complex parameter $\mu$ . The polynomials $\varrho ( \zeta )$ and $\sigma ( \zeta )$ are our old friends from (III.2.4). The difference equation (1.4) has stable solutions (for arbitrary starting values) iff all roots of (1.6) are $\leq 1$ in modulus. In addition, multiple roots must be strictly smaller than 1 (see Volume I, Sect.III.3,Exercise 1).

# Definition 1.1. The set

$$
S = \{ \mu \in \mathbb { C } \ ; \ \operatorname { a l l } \ \mathrm { r o o t s } \ \zeta _ { \ j } ( \mu ) \ \mathrm { o f } \ ( 1 . 6 ) \ \mathrm { s a t i s f y } \ | \zeta _ { \ j } ( \mu ) | \le 1 , \} \}
$$

is called the stability domain or stability region or region of absolute stability of Method (1.1). We have $A$ -stability if $S \supset \mathbb { C } ^ { - }$

It is sometimes desirable to consider $S$ as a subset of the compactified complex plane $\overrightarrow { \mathbb { C } }$ . In this case, for $\mu  \infty$ , the roots of Eq.(l.6) tend to those of $\sigma ( \zeta ) = 0$

For $\mu = 0$ ,Eq. (1.6) becomes $\varrho \big ( \zeta \big ) = 0$ . Thus the usual stability (in the sense of Definition III.3.2) is equivalent to $0 \in S$

Theorem 1.2. All numerical solutions of Method (1.1) are bounded for the linearized equation (1.2) with a diagonalizable matrix $J$ 讲 $h \lambda \in S$ for all eigenvalues $\lambda$ of $J$ □

We explain the computation of the stability domain at a particular example, the explicit Adams method of order 4 (see Sect. II.1, Eq.(1.5)),

$$
y _ { m + 4 } = y _ { m + 3 } + h \Bigl ( { \frac { 5 5 } { 2 4 } } f _ { m + 3 } - { \frac { 5 9 } { 2 4 } } f _ { m + 2 } + { \frac { 3 7 } { 2 4 } } f _ { m + 1 } - { \frac { 9 } { 2 4 } } f _ { m } \Bigr ) ,
$$

for which Eq.(1.6) becomes

$$
\zeta ^ { 4 } - \Bigl ( 1 + { \frac { 5 5 } { 2 4 } } \mu \Bigr ) \zeta ^ { 3 } + { \frac { 5 9 } { 2 4 } } \mu \zeta ^ { 2 } - { \frac { 3 7 } { 2 4 } } \mu \zeta + { \frac { 9 } { 2 4 } } \mu = 0 .
$$

In Fig.1.1 we display the complicated behavior of the roots of this equation. We choose the $1 6$ values as the dots surrounding the white horse,and plot the corresponding 4 roots $\zeta _ { 1 } , \zeta _ { 2 } , \zeta _ { 3 } , \zeta _ { 4 }$ in the $\zeta$ -plane,which can be obscrved to emerge from the roots $1 , 0 , 0 , 0$ of the $\varrho$ -polynomial.

Complex mappings are conformal, i.e., preserve angles and orientation. The angle of rotation and the magnification of a complex map is (locally) determined by its derivative. Differentiating(1.8) with respect to $\mu$ and putting $\mu = 0 , \zeta = 1$ gives

$$
\varrho ^ { \prime } ( 1 ) \cdot \zeta _ { 1 } ^ { \prime } ( 0 ) - \sigma ( 1 ) = 0 ,
$$

hence $\zeta _ { 1 } ^ { \prime } ( 0 ) = 1$ (because of the consistency conditions $\varrho ^ { \prime } ( 1 ) \neq 0$ ， $\sigma ( 1 ) \stackrel { \triangledown } { = } \varrho ^ { \prime } ( 1 )$ ， see Volume I, Eq. (III.2.6)). This explains the fact that the map $\mu (  ) \zeta _ { 1 }$ is close to $1 + \mu$ in the neighbourhood of $\mu = 0$ ,and $\zeta _ { 1 } ( \mu )$ moves inside the unit disc when $\mu$ moves inside $\mathbb { C } ^ { - }$

The Root Locus Curve. The key for computing $S$ is the fact that the inverse map $\zeta \mapsto \mu$ ,since(1.8) is linear in $\mu$ , can easily be computed and is one-valued

$$
\mu = \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } = \frac { \zeta ^ { 4 } - \zeta ^ { 3 } } { \frac { 5 5 } { 2 4 } \zeta ^ { 3 } - \frac { 5 9 } { 2 4 } \zeta ^ { 2 } + \frac { 3 7 } { 2 4 } \zeta - \frac { 9 } { 2 4 } } .
$$

The outside of the unit circle in the $\zeta$ -plane mapped back into the $\mu$ -plane by this formula (see the zodiac of gray horses in Fig.1.1) produces the forbidden $\mu$ -values, for which at least one root $\zeta _ { \imath } ( \mu )$ generates instability. The image of the boundary curve of the unit circle $\zeta = e ^ { \imath \theta }$ ， $0 \leq \theta \leq 2 \pi$ ， is called the root locus curve. It must be considered as an oriented curve and the stability region, whenever it is not empty, must lie to the left of it.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/3c848d6ae2d9fd06db1368e423fd4cb07efb70c99aa82fb5fdd0362a3df622ea.jpg)  
Fig.1.1. Plot of the stability function (1.8) with root locus curve

We conclude that the stability domain of Adams4 is precisely the small diamond shaped region surrounded by the root locus curve in the positive direction located between the origin and the point $\mu = 2 \cdot 2 4 / ( - 5 5 - 5 9 - 3 7 - 9 ) = - 0 . 3$

# Adams Methods

The explicit Adams methods (III.1.5) applied to $y ^ { \prime } = \lambda y$ give

$$
y _ { n + 1 } = y _ { n } + \mu \sum _ { \jmath = 0 } ^ { k - 1 } \gamma _ { \jmath } \nabla ^ { j } y _ { n } , \qquad \gamma _ { 0 } = 1 , \ \gamma _ { 1 } = \frac { 1 } { 2 } , \ \gamma _ { 2 } = \frac { 5 } { 1 2 } , \ \gamma _ { 3 } = \frac { 3 } { 8 } , \ \cdot \ \cdot \ .
$$

or, after putting $y _ { n } = \zeta ^ { n }$ and dividing by $\zeta ^ { n }$ ，

$$
\zeta - 1 = \mu \Big ( \gamma _ { 0 } + \gamma _ { 1 } \Big ( 1 - \frac { 1 } { \zeta } \Big ) + \gamma _ { 2 } \Big ( 1 - \frac { 2 } { \zeta } + \frac { 1 } { \zeta ^ { 2 } } \Big ) + \dots \Big ) .
$$

Hence the root locus curve becomes

$$
\mu = { \frac { \zeta - 1 } { \sum _ { \jmath = 0 } ^ { k - 1 } \gamma _ { \jmath } ( 1 - 1 / \zeta ) ^ { j } } } , \qquad \zeta = e ^ { i \theta } .
$$

For $k \approx 1$ we again obtain the circle of Euler's method, centred at $- 1$ .These curves are plotted in Fig.1.2 for $k = 2 , 3 , \ldots , 6$ and show stability domains of rapidly decreasing sizes. These methods are thus surely not appropriate for stiff problems.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/809de5caa87a11046cdf49feda2e3f2e102da9e2ed850e93acf35b3f107c74e0.jpg)  
Fig.1.2. Stability domains for explicit Adams methods

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/2c71023b15a7e81415189ad2a2a0967e8d72ffa81fa0ca6d37489d1c54993206.jpg)  
Fig.1.3. Stability domains of implicit Adams methods, compared to those of the explicit ones

The implicit Adams methods (II.1.8) lead to

$$
y _ { n + 1 } = y _ { n } + \mu \sum _ { \jmath = 0 } ^ { k } \gamma _ { \jmath } ^ { \ast } \nabla ^ { \jmath } y _ { n + 1 } , \qquad \gamma _ { 0 } ^ { \ast } = 1 , \ \gamma _ { \mathbf { I } } ^ { \ast } = - \frac { 1 } { 2 } , \ \gamma _ { 2 } ^ { \ast } = - \frac { 1 } { 1 2 } , \dots
$$

Here we put $y _ { n } = \zeta ^ { n }$ and divide by $\zeta ^ { n + 1 }$ . This gives

$$
\mu = \frac { 1 - 1 / \zeta } { \sum _ { \jmath = 0 } ^ { k } \gamma _ { j } ^ { * } \big ( 1 - 1 / \zeta \big ) ^ { \jmath } } , \qquad \zeta = e ^ { \imath \theta } .
$$

For $k = 1$ this is the implicit trapezoidal rule and is $A$ -stable. For $k = 2 , 3 , \ldots , 6$ the stability domains, though much larger than those of the explicit methods, do not cover $\mathbb { C } ^ { - }$ (see Fig.1.3). Hence these methods are not $A$ -stable.

# Predictor-Corrector Schemes

The inadequacy of the theory incorporating the effect of the corrector equation only for predictor-corrector methods was first discovered through experimental computations on the prototype linear equation

$$
y ^ { \prime } = f ( x , y ) = - 1 0 0 y + 1 0 0 , \quad y ( 0 ) = 0 ,
$$

(...）Very poor correlation of actual errors with the errors expected on the basis of the properties of the corrector equation alone was obtained. This motivated the development of the theory (P.E. Chase 1962)

As we have seen in Sect.II.1, the classical way of computing $y _ { n + 1 }$ from the implicit equations (III.1.8) is to use the result $y _ { n + 1 } ^ { * }$ of the explicit Adams method as a predictor in $\beta _ { k } f ( x _ { n + 1 } , y _ { n + 1 } )$ . This destroys a good deal of the stability properties of the method (Chase 1962). The stability analysis changes as follows: the predictor formula

$$
y _ { n + 1 } ^ { * } = y _ { n } + \mu \bigl ( \gamma _ { 0 } y _ { n } + \gamma _ { 1 } ( y _ { n } - y _ { n - 1 } ) + \gamma _ { 2 } ( y _ { n } - 2 y _ { n - 1 } + y _ { n - 2 } ) + . . . \bigr )
$$

must be inserted into the corrector formula

$$
\begin{array} { r l } & { y _ { n + 1 } = y _ { n } + \mu \Bigl ( \gamma _ { 0 } ^ { * } y _ { n + 1 } ^ { * } + } \\ & { \qquad \gamma _ { 1 } ^ { * } ( y _ { n + 1 } ^ { * } - y _ { n } ) + } \\ & { \qquad \gamma _ { 2 } ^ { * } ( y _ { n + 1 } ^ { * } - 2 y _ { n } + y _ { n - 1 } ) + } \\ & { \qquad \gamma _ { 3 } ^ { * } ( y _ { n + 1 } ^ { * } - 3 y _ { n } + 3 y _ { n - 1 } - y _ { n - 2 } ) + . . . \Bigr ) . } \end{array}
$$

Since there is a $\mu$ in (1.12) and in (1.13), we obtain this time,by putting $y _ { n } = \zeta ^ { n }$ and dividing by $\zeta ^ { n }$ , a quadratic equation for $\mu$ ，

$$
\begin{array} { c } { { A \mu ^ { 2 } + B \mu + C = 0 , } } \\ { { A = \Big ( \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \Big ) \Big ( \displaystyle \sum _ { p = 0 } ^ { k - 1 } \gamma _ { j } \big ( 1 - \frac { 1 } { \zeta } \big ) ^ { p } \Big ) , } } \\ { { B = \big ( 1 - \zeta \big ) \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } + \zeta \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \big ( 1 - \frac { 1 } { \zeta } \big ) ^ { p } , } } \\ { { C = 1 - \zeta . } } \end{array}
$$

For each $\zeta = e ^ { \imath \theta }$ ,Eq.(1.14) has two roots. These give rise to two root locus curves which determine the stability domain. These curves are represented in Fig.1.4 and compared to those of the original implicit methods. It can be seen that we loose a lot of stability. In particular, for $k \approx 1$ the trapezoidal rule becomes an explicit second order Runge Kutta method and the $A$ -stability is destroyed.

While Chase (1962) studied real eigenvalues only, the general complex case has been stated by Crane & Klopfenstein (1965) and, with beautiful figures, by

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/bc87e9f1668cd23900e224c5e32bd4bc47f2fd3a218ec9d5cf5efd2a7a852a29.jpg)  
Fig.1.4. Stability domains for PECE compared to original implicit methods

Krogh (1966). All three papers also searched for procedures with increased stabil-ity domains. This research was brought to perfection by Stetter (1968).

# Nystrim Methods

Thus we see that Milne's method will not handle so simple an equation as $y ^ { \prime } = - y$ ， $y ( 0 ) = 1$ (R.W. Hamming 1959)

... Milne's method has a number of virtues not possessed by its principal rival, the Runge-Kutta method,which are especially important when the order of the system of equations is fairly high $( \mathrm { N } { = } 1 0$ to 30 or more）... (R.W. Hamming 1959)

The explicit Nystrom method (II.1.13) for $k \approx 1$ and 2 is the “explicit midpoint rule”

$$
y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n }
$$

and leads to the root locus curve

$$
\mu = { \frac { e ^ { i \theta } - e ^ { - i \theta } } { 2 } } = i \sin \theta .
$$

This curve moves up and down the imaginary axis between $\pm i$ and leaves as stability domain just the interval $( - i , + i )$ (see Fig.1.5). All eigenvalues in the interior of the negative half plane lead to instabilities. This is caused by the second root $- 1$ of $\varrho \{ \zeta \}$ which moves out of the unit circle when $\mu$ goes West. This famous phenomenon is called the“weak instability” of the midpoint rule and was the “entry point” of Dahlquist's stability-career (Dahlquist 1951). The graphs of Fig.II.9.2 nicely show the (weak) instability of the numerical solution.

The implicit Milne-Simpson method (III.1.15) for $k \approx 2$ and 3 is

$$
y _ { n + 1 } = y _ { n - 1 } + h \Big ( \frac { 1 } { 3 } f _ { n + 1 } + \frac { 4 } { 3 } f _ { n } + \frac { 1 } { 3 } f _ { n - 1 } \Big )
$$

and has the root locus curve

$$
\mu = { \frac { e ^ { i \theta } - e ^ { - i \theta } } { { \frac { 1 } { 3 } } e ^ { i \theta } + { \frac { 4 } { 3 } } + { \frac { 1 } { 3 } } e ^ { - i \theta } } } = 3 i ~ { \frac { \sin \theta } { \cos \theta + 2 } } ,
$$

which moves up and down the imaginary axis between $\pm i \sqrt { 3 }$ . Thus its behaviour is similar to the explicit Nystrom method with a slightly larger stability interval.

The higher order Nystrom and Milne-Simpson methods have root locus curves which are oriented the wrong way round (see Fig.1.5). Their stability domains therefore reduce to the smallest possible set (for stable methods): just the origin.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/a1346895f7d9be2820a61877cbc06e369193149d27d2d15c603a404b5d25d9ca.jpg)  
Fig.1.5. Root locus curves for Nystrom and Milne methods

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/6e76881778dc8923fdc8151af5b3d3b5a48d857112d3215739facf11d346fa05.jpg)  
Fig.1.6. Root locus curves and stability domains of BDF methods

# BDF

The backward differentiation formulas $\begin{array} { r } { \sum _ { j = 1 } ^ { k } \frac { 1 } { j } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 } } \end{array}$ (see Equation (III.1.22')) have the root locus curves given by

$$
\mu = \sum _ { j = 1 } ^ { k } { \frac { 1 } { j } } \left( 1 - { \frac { 1 } { \zeta } } \right) ^ { j } = \sum _ { j = 1 } ^ { k } { \frac { 1 } { j } } \left( 1 - e ^ { - i \theta } \right) ^ { j } .
$$

For $k = 1$ we have the implicit Euler method with stability domain $S = \{ \mu ; | \mu -$ $1 | \geq 1 \}$ .For $k = 2$ the root locus curve (see Fig.1.6) has $\operatorname { R e } \left( \mu \right) = { \textstyle { \frac { 3 } { 2 } } } - 2 \cos \theta +$ ${ \frac { 1 } { 2 } } \cos 2 \theta$ $\geq 0$ $\theta$ $A$   
$k = 3 , 4 , 5$   
stability on a part of the imaginary axis. For $k \geq 7$ , as we know, the formulas are unstable anyway, even at the origin.

# The Second Dahlquist Barrier

I searched for a long time, finally Professor Lax showed me the Riesz-Herglotz theorem and I knew that I had my theorem.

(G. Dahlquist 1979)

Theorem 1.3. If the multistep method (1.1) is $A$ -stable, then

$$
\mathrm { R e } \left( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \qquad f o r \qquad | \zeta | > 1 .
$$

For irreducible methods the converse is also true: (1.18) implies $A$ -stability.

Proof. If the method is $A$ -stable then all roots of (1.6) must satisfy $\vert \zeta \vert \le 1$ whenever $\operatorname { R e } \mu \leq 0$ . The logically equivalent statement ( $\mathrm { \ R e } \mu > 0$ whenever $| \zeta | > 1 )$ yields (1.18) since by (1.6) $\mu = \varrho ( \zeta ) / \sigma ( \zeta )$

Suppose now that (1.18) holds and that the method is irreducible. Fix a $\mu _ { 0 }$ with $\mathrm { R e } \mu _ { 0 } \leq 0$ and let $\zeta _ { 0 }$ be a root of (1.6). We then have $\sigma ( \zeta _ { 0 } ) \neq 0$ (otherwise the method would be reducible). Hence $\mu _ { 0 } = \varrho ( \zeta _ { 0 } ) / \sigma ( \zeta _ { 0 } )$ and it follows from (1.18) that $| \zeta _ { 0 } | \le 1$ . We still have to show that $\zeta _ { 0 }$ is a simple root if $| \zeta _ { 0 } | = 1$ By a continuity argument it follows from (1.18） that $| \zeta _ { 0 } | = 1$ and $\mathrm { R e } \mu _ { 0 } < 0$ are contradictory. Therefore, it remains to prove that for $\mathrm { R e } \mu _ { 0 } = 0$ a root satisfying $| \zeta _ { 0 } | = 1$ must be simple. In a neighbourbood of such a root we have

$$
\frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } - \mu _ { 0 } = C _ { 1 } ( \zeta - \zeta _ { 0 } ) + C _ { 2 } ( \zeta - \zeta _ { 0 } ) ^ { 2 } + . . .
$$

and (1.18) implies that $C _ { 1 } \neq 0$ . This,however, is only possible if $\zeta _ { 0 }$ is a simple root of (1.6). □

In all the above examples we have not yet seen an $A$ -stable multistep formula of order $p \geq 3$ . The following famous theorem explains this observation.

Theorem 1.4 (Dahlquist 1963). An $A$ -stable multistep method must be of order $p \leq 2$ . If the order is 2, then the error constant satisfies

$$
C \leq - { \frac { 1 } { 1 2 } } .
$$

The trapezoidal rule is the only $A$ -stable method of order 2 with $C = - 1 / 1 2$

Proof. Dahlquist's first proof of this theorem is difficult. More elementary versions emerged in Widlund (1967),in lecture notes of W. Liniger (Univ. of Neuchatel 1971) and in the book of Grigorieff (1977, vol.2, p. 218).

We start by recalling some formulas from Volume I: Eq. (ii) of Theorem III.2.4 and Eq. (III.2.7) yield

$$
\varrho \big ( e ^ { h } \big ) - h \sigma \big ( e ^ { h } \big ) = C _ { p + 1 } h ^ { p + 1 } + \ldots \qquad \mathrm { f o r } \quad h  0 .
$$

From the consistency conditions (III.2.6) we have

$$
\varrho \big ( e ^ { h } \big ) = \varrho \big ( 1 + h + \ldots \big ) = \varrho ( 1 ) + \varrho ^ { \prime } ( 1 ) h + \ldots = \sigma ( 1 ) h + \ldots .
$$

We divide (1.20) by $h \varrho ( e ^ { h } )$ and obtain

$$
{ \frac { 1 } { h } } - { \frac { \sigma ( e ^ { h } ) } { \varrho ( e ^ { h } ) } } = C h ^ { p - 1 } + \ldots \qquad { \mathrm { f o r } } \quad h \to 0
$$

where $C$ is the error constant (III.2.13). With $\zeta = e ^ { h }$ this becomes

$$
{ \frac { 1 } { \log \zeta } } - { \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } = C ( \zeta - 1 ) ^ { p - 1 } + . . . \qquad { \mathrm { f o r } } \quad \zeta \to 1 .
$$

In this formula we put $p = 2$ . Whenever the method is of higher order,we have $C = 0$ . When the order of the method is one,we have nothing to prove. The same formula for the trapezoidal rule for which $\varrho _ { \mathcal { T } } ( \zeta ) = \zeta - 1$ ， $\sigma _ { \mathscr { T } } ( \zeta ) \overset { = } { = } \frac { 1 } { 2 } \big ( \zeta + 1 \big )$ ， becomes by series expansion (or by using Table III.2.1)

$$
\frac { 1 } { \log \zeta } - \frac { \sigma _ { T } ( \zeta ) } { \varrho _ { T } ( \zeta ) } = - \frac { 1 } { 1 2 } ( \zeta - 1 ) + \dots . \qquad \mathrm { f o r } \quad \zeta \to 1 .
$$

The idea is now to subtract the two formulas and obtain

$$
d ( \zeta ) : = \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } - \frac { \sigma _ { T } ( \zeta ) } { \varrho _ { T } ( \zeta ) } = \left( - C - \frac { 1 } { 1 2 } \right) ( \zeta - 1 ) + \ldots \quad \quad \mathrm { f o r } \quad \zeta \to 1 .
$$

From(1.18) we have that

$$
\operatorname { R e } \left( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \quad \mathrm { ~ o r ~ e q u i v a l e n t l y } \quad \operatorname { R e } \left( \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right) > 0 \quad \mathrm { f o r ~ } | \zeta | > 1 .
$$

The point here is that for the trapezoidal rule this $\operatorname { R e } \left( \dots \right)$ is zero for $| \zeta | = 1$ since this method has precisely $\mathbb { C } ^ { - }$ as stability domain. Hence from (1.24) we obtain

$$
\operatorname* { l i m } _ { | \zeta | > 1 } \mathrm { R e } d ( \zeta ) \geq 0 \qquad \mathrm { f o r } \quad | \zeta _ { 0 } | = 1 .
$$

The poles of $d ( \zeta )$ are the roots of $\varrho ( \zeta )$ , which,by stability,are not allowed outside the unit circle. Thus,by the maximum principle,(1.26) remains true everywhere outside the unit circle. Choosing then $\zeta = 1 + \varepsilon$ with $\mathrm { R e } \varepsilon > 0$ and $| \varepsilon |$ small, we see from (1.24) that either $- C - { \textstyle { \frac { 1 } { 1 2 } } } > 0$ or $d ( \zeta ) \equiv 0$ . This concludes the proof.□

# Exercises

1. The Milne-Simpson methods for $k = 4$ and 5 satisfy $\mathrm { R e } \left( \varrho ( \zeta ) / \sigma ( \zeta ) \right) \geq 0$ for $| \zeta | = 1$ ． Since their order is higher than 2,this seems to be in contradiction with the above proof of Theorem 1.4. Explain.

2.For the explicit midpoint rule (1.15),do the endpoints $\pm i$ of the stability region belong to $S : ?$ Study the (possible) stability of this method applied with $h = 1$ to $u ^ { \prime } = v$ ， $v ^ { \prime } = - u$ .

3. Compute for the explicit and implicit Adams methods the largest $\lambda _ { 0 } \in \mathbb { R }$ such that the real interval $[ - \lambda _ { 0 } , 0 ]$ lies in $S$ . Show that for the $k$ -step explicit Adamsmthods we hae $\lambda _ { 0 } = 2 / u _ { k }$ with $\begin{array} { r } { \mathcal { U } _ { k } = \sum _ { \jmath = 0 } ^ { k - 1 } 2 ^ { \jmath } \gamma _ { \jmath } } \end{array}$ $u _ { 1 } = 1$ $u _ { 2 } = 2$ $u _ { 3 } = 1 1 / 3$ ， $u _ { 4 } = 2 0 / 3$ ， $u _ { 5 } = 5 5 1 / 4 5 , \ldots )$ . The use of generating functions (see Sect.III.1) allow us to show that

$$
\sum _ { j = 1 } ^ { \infty } u _ { k } t ^ { k } = \left( - 1 + { \frac { 2 } { 1 - t } } - { \frac { 1 } { 1 - 2 t } } \right) \log ( 1 - 2 t ) ,
$$

a series with convergence radius $1 / 2$ . This explains why these stability domains decrease so rapidly.

Hint. Just set $\theta = \pi$ in the root locus curve.

4.Prove that the stability region of the $k$ -step,implicit Adams methods is of finite size for every $k \geq 2$ Hint. Show that $( - 1 ) ^ { k } \sigma ( - 1 ) < 0$ , so that $\sigma$ has a real negative root, smaller than $- 1$ .

5. a) Show that all 2-step methods of order 2 are given by

$$
\begin{array} { l } { \varrho ( \zeta ) = ( \zeta - 1 ) ( \alpha \zeta + 1 - \alpha ) \qquad } \\ { \sigma ( \zeta ) = ( \zeta - 1 ) ^ { 2 } \beta + ( \zeta - 1 ) \alpha + ( \zeta + 1 ) / 2 } \end{array}
$$

(which are irreducible for $\alpha \neq 2 \beta$ ).

b) The method is stable at O iff $\alpha \ge 1 / 2$

c) The method is stable at $\infty$ iff

$$
\alpha \geq 1 / 2 \qquad \mathrm { a n d } \qquad \beta > \alpha / 2 .
$$

Apply the Schur-Cohn criterion (Sect.II.3, Exercise 4).

d) The method is $A$ -stable iff (1.27) holds.

Hint.

$$
{ \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } = { \frac { 1 } { 2 } } \cdot { \frac { \zeta + 1 } { \zeta - 1 } } + \bigl ( \beta - { \frac { \alpha } { 2 } } \bigr ) \cdot { \frac { \zeta - 1 } { \alpha \zeta + 1 - \alpha } } .
$$

# V.2“Nearly” A-Stable Multistep Methods

We are not atempting to disprove Dahlquist's theorems but are trying to get round the conditions they impose ...

(J. Cash 1979)

Dahlquist's condition $p \leq 2$ for the order of an $A$ -stable linear multistep method is a severe restriction for efficient practical calculations of high precision. There are only two ways of "breaking” this barrier:

either weaken the condition;   
$\bullet$ or strengthen the method.

These two points will occupy our attention in this and in the following section.

# $A ( \alpha )$ -Stability and Stiff Stability

It is the purpose of this note to show that a slightly different stability requirement permits methods of higher accuracy.

(O. Widlund 1967)

The angle $\alpha$ is only one of a number of parameters which have been proposed for measuring the extent of the stability region. But it is probably the best such measure ...

(Skeel& Kong 1977)

Many important classes of practical problems do not require stability on the entire left half-plane $\mathbb { C } ^ { - }$ . Further,for eigenvalues on the imaginary axis, the solutions are often highly oscillatory and one is then forced anyhow to restrict the step size “to the highest frequency present in order to represent the signal" (Gear 1971, p. 214).

Definition 2.1 (Widlund 1967). A convergent linear multistep method is $A ( \alpha ) -$ stable, $0 < \alpha < \pi / 2$ ,if

$$
S \supset S _ { \alpha } = \{ \mu ; | \arg ( - \mu ) | < \alpha , \mu \neq 0 \} .
$$

A method is $A ( 0 )$ -stable if it is $A ( \alpha )$ -stable for some (sufficiently small) $\alpha > 0$ ·

Similarly, Gear (1971) required in his famous concept of“stiff stability”that

$$
S \supset \{ \mu ; \mathrm { R e } \mu < - D \}
$$

for some $D > 0$ and that the method be “accurate” in a rectangle $- D \leq \operatorname { R e } \mu \leq$ $a , \ - \theta \leq \operatorname { I m } \mu \leq \theta$ for some $a > 0$ and $\theta$ about $\pi / 5$ . Many subsequent writers

didn't like the inaccurate meaning of “accurate” in this definition and replaced it by something else. For example Jeltsch (1976) required that in addition to (2.2),

$$
| \zeta _ { 1 } ( \mu ) | > | \zeta _ { \iota } ( \mu ) | , \quad i = 2 , \ldots , k \qquad \mathrm { i n } \quad | \mathrm { R e } \mu | \leq a , | \mathrm { I m } \mu | \leq \theta ,
$$

where $\zeta _ { 1 } ( \mu )$ is the analytic continuation of the principal root $\zeta _ { 1 } ( 0 ) = 1$ of (1.6). Also, the rectangle given by

$$
| \mathrm { I m } \mu | \leq \theta , \qquad - D \leq \mathrm { R e } \mu \leq - a
$$

should belong to $S$

Other concepts are $A _ { 0 }$ -stable (Cryer 1973) if

$$
| \zeta _ { \ i } ( x ) | < 1 , \quad i = 1 , \ldots , k \qquad \mathrm { f o r } \quad - \infty < x < 0
$$

and $\mathring { A }$ -stable (a joke of O. Nevanlinna 1979) if

$$
( - \infty , 0 ] \subset S .
$$

Of course, we have

$$
A ( 0 ) { \mathrm { - s t a b l e } } \ \Longrightarrow \ A _ { 0 } { \mathrm { - s t a b l e } } \ \Longrightarrow \ \mathring { A } { \mathrm { - s t a b l e } }
$$

but neither implication is reversible (Exercise 3; see also “Theorem $1 ^ { \circ }$ of Jeltsch 1976).

The BDF methods (1.18) satisfy (2.1） for $A ( \alpha )$ -stability and (2.2) for stiff stability with the values

<table><tr><td>k</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>α</td><td>90°</td><td>90°</td><td>86.030</td><td>73.350</td><td>51.84°</td><td>17.84°</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0.083</td><td>0.667</td><td>2.327</td><td>6.075</td></tr></table>

# High Order $A ( \alpha )$ -Stable Methods

Dill and Gear ... and Jain and Srivastava ... have used computers to construct stiffly stable methods of orders eight and eleven, respectively, but were unable to construct higher order stiffly stable methods. Even though we have shown here that $A _ { 0 }$ -stable methods of arbitrarily high order exist,we conjecture that $A ( 0 ) \cdot$ stable linear multistep methods of higher order, of order greater than 20 say,do not exist. (Cryer 1973)

Widlund (1967) showed that for every $\alpha < \pi / 2$ ， $\alpha$ arbitrarily close to $\pi / 2$ , there exist $A ( \alpha )$ -stable multistep methods of order $p = k$ for $p = 3$ and $p = 4$ . It is now an interesting question whether such methods also exist for higher orders. Well, the answer consists of good news and bad news.

First the good news. The conjecture of Cryer (see quotation) was quickly dis-proved by combining Cryer's $A _ { 0 }$ -stable methods with the result of Jeltsch (1976)

which says that certain $A _ { 0 }$ -stable methods are also $A ( \alpha )$ -stable. The following theorem shows that $\alpha$ can even be chosen arbitrarily close to $\pi / 2$ ：

Theorem 2.2 (Grigorieff & Schroll 1978). Let $\alpha < \pi / 2$ be given. Then for every $k \in \mathbb { N }$ there exists an $A ( \alpha )$ -stable linear $k$ -step method of order $p = k$

Proof. For $p = k = 2$ the two-step BDF method which is $A$ -stable,and hence $A ( \alpha _ { 2 } )$ -stable for every $\alpha _ { 2 } \leq \pi / 2$ ， does the job. For $k$ arbitrary,we intercalate $k - 2$ values between $\alpha$ and $\pi / 2$ ，

$$
\alpha < \alpha _ { k - 1 } < \alpha _ { k - 2 } < \ldots < \alpha _ { 3 } < \alpha _ { 2 } \leq { \frac { \pi } { 2 } } ,
$$

and extend the method step by step with the help of Lemma 2.3.

Lemma 2.3. Suppose an $A ( \alpha )$ -stable $k$ -step method of order $p$ is given with

$$
\begin{array} { r l } { \varrho ( \zeta ) \neq 0 \quad } & { { } i f | \zeta | = 1 , \zeta \neq 1 } \\ { \sigma ( \zeta ) \neq 0 \quad } & { { } i f | \zeta | = 1 . } \end{array}
$$

Then for every $\widetilde { \alpha } < \alpha$ there exists an $A ( \widetilde { \alpha } )$ -stable $\left( k + 1 \right)$ -step method of order $p + 1$ which also satisfies (2.9).

The proof follows very closely the ideas of Jeltsch & Nevanlinna (1982): Let $\varrho ( \zeta )$ and $\sigma ( \zeta )$ represent the given $k$ -step method with order condition

$$
\frac { \varrho ( \zeta ) } { \log \zeta } - \sigma ( \zeta ) = C _ { p + 1 } ( \zeta - 1 ) ^ { p } + \mathcal { O } \big ( ( \zeta - 1 ) ^ { p + 1 } \big ) .
$$

If we multiply $\varrho$ and $\sigma$ by $( \zeta - 1 )$ we formally increase the order by 1 and at the same time leave the root locus curve unchanged. Everything seems to be proved. However, the new $\varrho$ -polynomial would have a double root at $\zeta = 1$ and would thus lead to an unstable method. We therefore choose $\varepsilon > 0$ and multiply (2.10） by $\left( \zeta - 1 + \varepsilon \right)$ ，which moves the root slightly inside the unit circle. We then obtain a new method of order $p + 1$ if we put

$$
\begin{array} { r l } & { \widetilde { \varrho } ( \zeta ) = \varrho ( \zeta ) \left( \zeta - 1 + \varepsilon \right) } \\ & { \widetilde { \sigma } ( \zeta ) = \sigma ( \zeta ) \left( \zeta - 1 + \varepsilon \right) + \varepsilon C _ { p + 1 } ( \zeta - 1 ) ^ { p } . } \end{array}
$$

Since $p = k + 2$ is excluded (by Theorem III.3.9 methods with $p = k + 2$ are symmetric and violate Hypothesis (2.9a)),both polynomials $\widetilde { \varrho }$ and $\widetilde { \sigma }$ are of degree $\leq k + 1$ . Now the formula

$$
\frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } = \frac { \varepsilon C _ { p + 1 } ( \zeta - 1 ) ^ { p } } { \varrho ( \zeta ) ( \zeta - 1 + \varepsilon ) }
$$

allows us to compare, for $\varepsilon$ small, the root-locus curves of the two methods. The fact that we are working with $\sigma ( e ^ { i \theta } ) / \varrho ( e ^ { \imath \theta } ) = 1 / \mu$ instead of $\mu = \varrho \big ( e ^ { \imath \theta } \big ) / \sigma \big ( e ^ { \imath \theta } \big )$

does not matter, because the transformation $\mu \mapsto 1 / \mu$ maps the sector of Definition 2.1 onto itself. Because of Hypothesis (2.9a),1 is the only (simple) root of $\varrho ( \zeta )$ on the unit circle, therefore

$$
\left| { \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } } - { \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } \right| \leq C \cdot \varepsilon { \frac { | \zeta - 1 | ^ { p - 1 } } { | \zeta - 1 + \varepsilon | } } \qquad { \mathrm { f o r } } \quad \zeta = e ^ { \imath \theta } .
$$

A small obstacle still separates us from “endless pleasure,endless love,Semele enjoys above": the denominator $| \zeta - 1 + \varepsilon |$ ，which becomes small for $\varepsilon \to 0$ and $\theta  0$ .For $p > 1$ ,this “small’ denominator is simply balanced by one of the factors $| \zeta - 1 |$ from the numerator and we have

$$
\left| \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right| \leq \widehat { C } \cdot \varepsilon
$$

which means uniform pointwise convergence of ${ \widetilde \sigma } ( \zeta ) / { \widetilde \varrho ( \zeta ) }$ to $\sigma ( \zeta ) / \varrho ( \zeta )$ if $\varepsilon \to 0$ Since $\sigma ( \zeta ) / \varrho ( \zeta )$ is bounded away from the origin (Hypothesis (2.9b)), this also means uniform convergence of the angles.

This is already sufficient to prove Theorem 2.2, where we always have $p \geq 2$ . However,Lemma 2.3 remains valid for $p = 1$ too: the critical region is when $\theta  0$ ， in which case $\left| \sigma ( e ^ { \imath \theta } ) / \varrho ( e ^ { \imath \theta } ) \right|$ and $| \widetilde { \sigma } ( e ^ { \imath \theta } ) / \widetilde { \varrho } ( e ^ { \imath \theta } ) |$ tend to infinity like $C o n s t / \theta$ ， Instead of (2.14) we have for $p = 1$

$$
\left| \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right| \leq \frac { C \varepsilon } { | \zeta - 1 + \varepsilon | } = \mathcal { O } \Big ( \frac { \varepsilon } { \theta } \Big ) .
$$

Thus the angle (seen from the origin) between $\widetilde { \sigma } ( \zeta ) / \widetilde { \varrho } ( \zeta )$ and $\sigma ( \zeta ) / \varrho ( \zeta )$ is $\mathcal { O } ( \varepsilon )$

# Approximating Low Order Methods with High Order Ones

The above proof of Lemma 2.3 actually shows more than angle-boundedness of the root locus curve, namely uniform convergence of the root locus curve of a high order method to that of a lower order one. This leads to the following theorem of Jeltsch & Nevanlinna (1982):

Theorem 2.4. Let a linear stable $k$ -step method of order $p$ and stability domain $S$ be given which satisfies $( 2 . 9 a )$ Then to any closed set $\Omega \subset \operatorname { I n t } S \subset { \overline { { \mathbb { C } } } }$ and any $K \in \mathbb { N }$ there exists a linear $k + K$ -step method of order $p + K$ whose stability domain $\widetilde { S }$ satisfies

$$
\widetilde { S } \supset \Omega .
$$

Moreover if the first method is explicit, the higher-order method is also explicit.

Proof. The proof is similar to that of Lemma 2.3. Instead of the sequence (.8) we use a sequence of embedded closed and open subsets between $\Omega$ and $S$ (Urysohn's Lemma). Hypothesis (2.9b) is ruled out by passing to the compactified topology of $\overline { { \mathbb { C } } } = \mathbb { C } \cup \{ \infty \}$ □

Remark. No method with non-empty Int $S$ of practical interest violates Hypothesis (2.9a). Nevertheless, Theorem 2.4 remains valid without this hypothesis, but the proof becomes more complicated (see “Lemma $3 . 6 ^ { \mathfrak { s } }$ of Jeltsch & Nevanlinna 1982).

# A Disc Theorem

Another weakening of $A$ -stability is to require stability for

$$
D _ { r } = \{ \mu \ ; \ | \mu + r | \leq r \} ,
$$

which is a disc of radius $\mathscr { r }$ in $\mathbb { C } ^ { - }$ tangent to the imaginary axis at the origin. Theorems about stability in $D _ { r }$ are stronger than theorems about $A ( \alpha )$ -stability for eigenvalues close to the origin. The following result is,again,due to Jeltsch & Nevanlinna (1982):

Theorem 2.5. Let a linear $k$ -step method of order $p$ be given with $S \supset D _ { r }$ . Then for any $\widetilde r < r$ and any $K \in \mathbb { N }$ there exists_ a linear $k + { \bar { k } } ^ { \prime }$ -step method of order $p + K$ whose stability domain $\widetilde { S }$ satisfies $ { \widetilde { S } } \supset D _ {  { \widetilde { r } } }$ ·

Proof. The map $\mu \mapsto 1 / \mu$ used in the proof of Lemma 2.3 maps the exterior of $D _ { r }$ onto the half-plane

$$
\left\{ \mu \in \mathbb { C } \mathrm { ~ ; ~ } \operatorname { R e } \mu > - \frac { 1 } { 2 r } \right\} .
$$

Therefore the uniform convergence established in (2.14) also covers the new situation if $p > 1$ . The case $p = 1$ , however, needs a more careful study and we refer to the original paper of Jeltsch & Nevanlinna (1982, pp. 277-279). □

# Accuracy Barriers for Linear Multistep Methods

Now here is the “bad news": high order $A ( \alpha )$ -stable methods, for $\alpha$ close to $\pi / 2$ , cannot be of practical use,or in other words: “the second Dahlquist barrier cannot be broken". The reason is simply that high order alone is not sufficient for high accuracy,because the methods then have enormous error constants. Jeltsch & Nevanlinna (1982) give an impressive staccato (from“Theorem $4 . 1 ^ { \circ }$ to “Lemma 4.15"） of lower bounds for error constants and Peano kernels of methods having large stability domains. The Peano kernels, the most serious measures for the error, are defined by the formulas (see (III.2.15) and (III.2.3) of Volume I)

$$
\begin{array} { r l r } & { } & { L ( x ) = h ^ { q + 1 } \displaystyle \int _ { - \infty } ^ { \infty } \check { K } _ { q } ( - s ) y ^ { ( q + 1 ) } ( x + s h ) d s } \\ & { } & { \quad = \displaystyle \sum _ { j = 0 } ^ { k } \bigl ( \alpha _ { j } y ( x + \jmath h ) - h \beta _ { j } y ^ { \prime } ( x + j h ) \bigr ) . } \end{array}
$$

The kernels $\check { K } _ { q } ( - s ) = K _ { q } ( s )$ are zero outside the interval $0 \le s \le k$ and are piecewise polynomials given by complicated formulas (see (II.2.16)) which appear not very attractive to work with.

However, the formulas simplify if we use the Fourier transform which, for a function $f ( x )$ , is defined by

$$
{ \widehat { f } } ( \xi ) = \int _ { - \infty } ^ { \infty } e ^ { - \imath x \xi } f ( x ) d x .
$$

We obtain $\widehat { L }$ from (2.17) by insertion of the definitions,several integrations by parts and transformations of double integrals:

$$
\begin{array} { c } { { \widehat { L } ( \xi ) = h ^ { q + 1 } \widehat { K _ { q } } ( h \xi ) \cdot y ^ { ( q + 1 ) } ( \xi ) } } \\ { { = \widehat { K _ { q } } ( h \xi ) ( i h \xi ) ^ { q + 1 } \widehat { y } ( \xi ) , } } \end{array}
$$

and from (2.18)

$$
\widehat { L } ( \xi ) = \big ( \varrho \big ( e ^ { \imath h \xi } \big ) - i h \xi \sigma \big ( e ^ { \imath h \xi } \big ) \big ) \cdot \widehat { y } \big ( \xi \big ) .
$$

Thus (2.20) and (2.22) give

$$
\widehat { K _ { q } } ( - \xi ) = \widehat { K _ { q } } ( \xi ) = \big ( \varrho \big ( e ^ { \imath \xi } \big ) - i \xi \sigma \big ( e ^ { \imath \xi } \big ) \big ) \big ( i \xi \big ) ^ { - ( q + 1 ) } ,
$$

a nice formula, involving the polynomials $\varrho$ and $\sigma$ ， with which we are better acquainted.

What about the usefulness of $\widehat { \bar { K _ { q } } }$ for error estimates? Well, it is the Parseval identity (Exercise 4)

$$
\| f \| _ { L ^ { 2 } ( - \infty , \infty ) } = \frac { 1 } { \sqrt { 2 \pi } } \| \widehat { f } \| _ { L ^ { 2 } ( - \infty , \infty ) }
$$

which allows us to obtain the $L ^ { 2 }$ -estimate for the error

$$
\begin{array} { r } { \| L \| _ { L ^ { 2 } ( - \infty , \infty ) } \leq h ^ { q + 1 } \| \widehat { K _ { q } } \| _ { L ^ { \infty } } \cdot \| y ^ { ( q + 1 ) } \| _ { L ^ { 2 } } , } \end{array}
$$

as follows:

$$
\begin{array} { l } { \displaystyle | | L | | _ { L ^ { 2 } ( - \infty , \infty ) } ^ { 2 } = \frac { 1 } { 2 \pi } | | \widehat { L } | | _ { L ^ { 2 } ( - \infty , \infty ) } ^ { 2 } } \\ { \displaystyle = \frac { h ^ { 2 q + 2 } } { 2 \pi } \int _ { - \infty } ^ { \infty } \left| \widehat { K } _ { q } ( \xi ) \right| ^ { 2 } | y ^ { ( q + 1 ) } ( \xi ) | ^ { 2 } d \xi } \\ { \displaystyle \leq \frac { h ^ { 2 q + 2 } } { 2 \pi } \operatorname* { m a x } | \widehat { K } _ { q } ( \xi ) | ^ { 2 } \cdot \int _ { - \infty } ^ { \infty } \left| y ^ { ( q + 1 ) } ( \xi ) \right| ^ { 2 } d \xi } \\ { \displaystyle = \frac { h ^ { 2 q + 2 } } { 2 \pi } | | \widehat { K } _ { q } | | _ { L ^ { \infty } } ^ { 2 } \cdot | | y ^ { ( q + 1 ) } | | _ { L ^ { 2 } } ^ { 2 } } \\ { \displaystyle = h ^ { 2 q + 2 } | | \widehat { K } _ { q } | | _ { L ^ { \infty } } ^ { 2 } \cdot | | y ^ { ( q + 1 ) } | | _ { L ^ { 2 } } ^ { 2 } . } \end{array}
$$

In order that the obtained estimates (2.25) for $L$ express the actual errors of the numerical solution, we adopt throughout this section the normalization $\sigma ( 1 ) = 1$ (cf. Eq. (III.2.13)).

And here is the theorem which tells us that linear multistep methods of order $p > 2$ and“large” stability domain cannot be precise:

Theorem 2.6 (Jeltsch & Nevanlinna 1982). Consider $k$ -step methods of order $p >$ 2, normalized by $\sigma ( 1 ) = 1$ ,for which the disc $D _ { r }$ of(2.15) is in the stability domain $S$ . Then there exists a constant $C > 0$ (depending on $k , p , q$ ; but independent of $\mathscr { r }$ )such that the Fourier transform of the Peano kernel $K _ { q } ^ { \prime } ~ ( \it q \leq p ) ~ s a t i s f i e s$

$$
\| \widehat { K _ { q } } \| _ { \infty } \geq C \Big ( \frac { r } { 3 } \Big ) ^ { p - 2 } .
$$

The proof of Jeltsch & Nevanlinna is in two steps:

a) The stability requirement forces some coefficients $a _ { \scriptscriptstyle 3 }$ of $R ( z )$ to be large (Lemma 2.7 below), where as in (I.3.17)

$$
\begin{array} { l } { { \displaystyle R ( z ) = \left( \frac { z - 1 } 2 \right) ^ { k } \varrho \left( \frac { z + 1 } { z - 1 } \right) = \sum _ { j = 0 } ^ { k } a _ { j } z ^ { j } } } \\ { { \displaystyle S ( z ) = \left( \frac { z - 1 } 2 \right) ^ { k } \sigma \left( \frac { z + 1 } { z - 1 } \right) = \sum _ { j = 0 } ^ { k } b _ { j } z ^ { j } } . }  \end{array}
$$

b） $\| \widehat { \bar { K _ { q } } } \| _ { L ^ { \infty } }$ can be bounded from below by $\operatorname* { m a x } _ { \boldsymbol { \jmath } } a _ { \boldsymbol { \jmath } }$ (Lemma 2.8).

Lemma 2.7. If $D _ { r } \subset S$ and $p > 2$ then

$$
a _ { k - \jmath } \geq \left( { \frac { r } { 3 } } \right) ^ { \jmath - 1 } \cdot a _ { k - 1 } = \left( { \frac { r } { 3 } } \right) ^ { \jmath - 1 } \cdot 2 ^ { 1 - k } \qquad f o r \quad j = 2 , \ldots , p - 1 .
$$

Proof. Stability in $D _ { r }$ means that for $\mu \in D _ { r }$ all roots of $\varrho \big ( \zeta \big ) - \mu \sigma \big ( \zeta \big ) = 0$ lie in $| \zeta | \le 1$ . Hence

$$
\varrho ( \zeta ) / \sigma ( \zeta ) \notin D _ { r } \qquad \mathrm { f o r } \quad | \zeta | > 1 .
$$

Applying the Graeco-Roman transformation $\zeta = ( z + 1 ) / ( z - 1 )$ and using (2.16) this means that

$$
\mathrm { R e } \frac { S ( z ) } { R ( z ) } > - \frac { 1 } { 2 r } \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0
$$

or

$$
\mathrm { R e } \ \frac { 2 r S ( z ) + R ( z ) } { R ( z ) } > 0 \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0 .
$$

Next, we must consider the order conditions (Lemma III.3.7 and Exercise $9$ of Sect. III.3)

$$
R ( z ) \Big ( \frac { z } { 2 } - \frac { 1 } { 6 z } - \frac { 2 } { 4 5 z ^ { 3 } } - \ldots \Big ) - S ( z ) = { \mathcal O } \Big ( \Big ( \frac { 1 } { z } \Big ) ^ { p - k } \Big ) , \quad z \to \infty .
$$

This shows that $R ( z ) = \mathcal { O } ( z ^ { k - 1 } )$ ， $S ( z ) = \mathcal { O } ( z ^ { k } )$ ,but $2 S ( z ) - z R ( z ) = \mathcal { O } \left( z ^ { k - 1 } \right) .$ Thus we subtract $\mathscr { r } z$ from (2.32) in order to lower the degree of the numerator. The

resulting function again satisfies

$$
\mathrm { R e } \ \frac { r ( 2 S ( z ) - z R ( z ) ) + R ( z ) } { R ( z ) } > 0 \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0
$$

because of $\mathrm { R e } \left( r z \right) = 0$ on $z = i y$ and the maximum principle (an idea similar to that of Lemma IV.5.21). The function (2.34) can therefore have no zeros in $\mathbb { C } ^ { + }$ (since by Taylor expansion all arguments of a function appear in a complex neighbourhood of a zero). Therefore the numerator of (2.34) must have non-negative coefficients (cf. the proof of Lemma II.3.6). Multiplying out (2.33) and (2.34) we obtain for the coeficient of $z ^ { k - 1 } \ ( j \leq p - 1 )$ ：

$$
0 \leq r \left( - \frac 1 3 a _ { k - \jmath + 1 } - \frac { 4 } { 4 5 } a _ { k - \jmath + 3 } - . . . \right) + a _ { k - \jmath }
$$

or by simplifying (cf. Lemmas III.3.8 and III.3.6)

$$
\frac { r } { 3 } a _ { k - \jmath + 1 } \leq a _ { k - \jmath } .
$$

Using $a _ { k - 1 } = 2 ^ { 1 - k } ~ \varrho ^ { \prime } ( 1 ) = 2 ^ { 1 - k }$ (see Lemma II.3.6), this leads to (2.29).

Lemma 2.8. There exists $C > 0$ (depending on $k , p$ and $q$ with $q = 0 , 1 , \ldots , p )$ with the following property: if $0 \in S$ ,then

$$
\| \widehat { K _ { q } } \| _ { L ^ { \infty } } \geq C \cdot \operatorname* { m a x } _ { \jmath } a _ { \jmath } .
$$

Proof. We set $e ^ { \imath \xi } = \zeta , \xi = - \imath \log \zeta$ in Eq.(2.23) so that the maximum must be taken over the set $| \zeta | = 1$ . Then we introduce $\zeta = ( z + 1 ) / ( z - 1 )$ and take the maximum over the imaginary axis. This gives with (2.27) and (2.28)

$$
\big \| \widehat { K _ { q } } \big \| _ { L ^ { \infty } } = \operatorname* { s u p } _ { t } \underbrace { \bigg | \frac { 1 } { ( i t ) ^ { k } } \left( \frac { R ( i t ) } { \log \frac { i t + 1 } { t t - 1 } } - S ( i t ) \right) \bigg | } _ { \Phi ( t ) } \cdot \underbrace { \bigg | \left( \frac { 2 i t } { i t - 1 } \right) ^ { k } \bigg | \cdot \bigg | \log \left( \frac { i t + 1 } { i t - 1 } \right) \bigg | ^ { - q } } _ { \Psi ( t ) } .
$$

We now insert, for $| t | > 1$ ,Eqs. (III.3.19),(III.3.21) and (III.3.22) to obtain

$$
\left| \Phi ( t ) \right| = \left| P _ { k } { \Big ( } { \frac { 1 } { i t } } { \Big ) } + { \frac { d _ { 1 } } { ( i t ) ^ { k + 1 } } } + { \frac { d _ { 2 } } { ( i t ) ^ { k + 2 } } } + \dots \right|
$$

where $P _ { k }$ is a polynomial of degree $k$ and subdegree $p$ (see Lemma III.3.7), determined by the method. Since we want our estimates to be true for $a l l$ methods, we treat $P _ { k }$ as an arbitrary polynomial. Separating real and imaginary parts and substituting $1 / t = s$ gives

$$
\begin{array} { c } { { | \Phi ( t ) | ^ { 2 } = \left| Q _ { k - 1 } ( s ) + d _ { 1 } s ^ { k + 1 } - d _ { 3 } s ^ { k + 3 } + \mathrm {  ~ \Gamma ~ } \right| ^ { 2 } } } \\ { { { } } } \\ { { + \left| Q _ { k } ( s ) + d _ { 2 } s ^ { k + 2 } - d _ { 4 } s ^ { k + 4 } + \mathrm {  ~ \Gamma ~ } \right| ^ { 2 } = | \Phi _ { 1 } ( t ) | ^ { 2 } + | \Phi _ { 2 } ( t ) | ^ { 2 } } } \end{array}
$$

where $Q _ { k - 1 } ( s )$ and $Q _ { k } ( s )$ are arbitrary (even or odd) polynomials of subdegree $p$ and degree $k - 1$ and $k$ ,respectively. Both terms are minorized separately, e.g. for the first we write

$$
| \Phi _ { 1 } ( t ) | \geq | Q _ { k - 1 } ( s ) + d _ { 1 } s ^ { k + 1 } | - | d _ { 3 } s ^ { k + 3 } - d _ { 5 } s ^ { k + 5 } + - \dots | .
$$

Since $\mu _ { 1 } < \mu _ { 3 } < \mu _ { 5 } < . ~ . . < 0$ (Exercise 6 below) and $a _ { \imath } \geq 0$ we have from (II1.3.22)

$$
d _ { 1 } \leq d _ { 3 } \leq d _ { 5 } \leq \ldots \leq 0 \quad { \mathrm { a n d } } \quad d _ { 2 } \leq d _ { 4 } \leq d _ { 6 } \leq \ldots \leq 0 .
$$

Therefore,the second term in (2.39) is majorized by the alternating series argument for $0 < s < 1$ as

$$
| d _ { 3 } s ^ { k + 3 } - d _ { 5 } s ^ { k + 5 } + - \ldots | \leq | d _ { 3 } | s ^ { k + 3 } \leq | d _ { 1 } | s ^ { k + 3 } .
$$

Since $Q _ { k - 1 } ( s )$ is an arbitrary polynomial, we can replace it by $| d _ { 1 } | Q _ { k - 1 } ( s )$ s0 that $\left| d _ { 1 } \right|$ becomes a common factor of the whole expression

$$
\begin{array} { r } { \left| \Phi _ { 1 } ( t ) \right| \geq \left| d _ { 1 } \right| \left( \left| Q _ { k - 1 } ( s ) + s ^ { k + 1 } \right| - s ^ { k + 3 } \right) . } \end{array}
$$

This suggests that we define the constants

$$
\begin{array} { l } { { D _ { \mathrm { I } } = \displaystyle \operatorname* { i n f } _ { Q _ { k - 1 } } \left\{ \operatorname* { s u p } _ { 0 < s < 1 } \left[ \left( \left| Q _ { k - 1 } ( s ) + s ^ { k + 1 } \right| - s ^ { k + 3 } \right) \left( \frac 2 { \sqrt { 1 + s ^ { 2 } } } \right) ^ { k } \left( \frac 1 { 2 \arctan s } \right) ^ { q } \right] \right\} } } \\ { { D _ { \mathrm { 2 } } = \displaystyle \operatorname* { i n f } _ { Q _ { k } } \left\{ \operatorname* { s u p } _ { 0 < s < 1 } \left[ \left( \left| Q _ { k } ( s ) + s ^ { k + 2 } \right| - s ^ { k + 4 } \right) \left( \frac 2 { \sqrt { 1 + s ^ { 2 } } } \right) ^ { k } \left( \frac 1 { 2 \arctan s } \right) ^ { q } \right] \right\} _ { \mathrm { - ~ c ~ o ~ c ~ t ~ a ~ n ~ } } } } \end{array}
$$

where the inf is taken over all polynomials $Q _ { k - 1 } ( s ) = c _ { k - 1 } s ^ { k - 1 } + c _ { k - 3 } s ^ { k - 3 } +$ $c _ { k - 5 } s ^ { k - 5 } + \ldots$ respectively $Q _ { k } ( s ) = c _ { k } s ^ { k } + c _ { k - 2 } s ^ { k - 2 } + c _ { k - 4 } s ^ { k - 4 } + . . .$ of subdegree $p$ . The last two factors represent $\Psi ( t )$ of (2.36). Since $s ^ { k + 1 }$ dominates $s ^ { k + 3 }$ for small $s , D _ { 1 }$ and $D _ { 2 }$ are positive constants (see Exercise 8). We then have from (2.38) and (2.36)

$$
\| \widehat { K } _ { q } \| _ { L ^ { \infty } } \geq \sqrt { d _ { 1 } ^ { 2 } D _ { 1 } ^ { 2 } + d _ { 2 } ^ { 2 } D _ { 2 } ^ { 2 } }
$$

Since both $d _ { 1 }$ and $d _ { 2 }$ are sums of $a _ { \scriptscriptstyle 3 }$ with negative coefficients (see (I.3.22) and Lemma II.3.8), $\| \widehat { K } _ { q } \| _ { \infty }$ must be large if one of the coefficient $a _ { \scriptscriptstyle \mathscr { I } }$ is large.

This concludes the proof of Theorem 2.6 which, by the way, also proves Theorem 1.4 again. □

# Exercises

1. Show that no explicit method can be $A ( 0 )$ -stable.

2. Show that $\beta _ { k } / \alpha _ { k } > 0$ is a necessary condition for an $A ( \alpha )$ -stable linear $k$ -step method.

3.a) Show that the method

$$
y _ { n + 2 } - y _ { n + 1 } = { \frac { h } { 4 } } ( f _ { n + 2 } + 2 f _ { n + 1 } + f _ { n } )
$$

has a stability domain bounded by a parabola. It is therefore $A _ { 0 }$ -stable, but not $A ( 0 )$ -stable (Cryer 1973).

b) Find a“deformation”of the 5th order BDF scheme

$$
\sum _ { \jmath = 1 } ^ { 5 } \frac { 1 } { j } \nabla ^ { \jmath } y _ { n + 1 } + \beta \nabla ^ { 6 } y _ { n + 1 } = h f _ { n + 1 }
$$

with $\beta \approx 0 . 2 3 2 \ldots$ . which is $\mathring { A }$ -stable, but not $A _ { 0 }$ -stable.

c) Find a method which is $A _ { 0 }$ -stable, but not stable at infinity.

Hint for $( c )$ . If you “lift up your heads, o ye gates” (just a few lines, not to heaven), the answer is easy to find.

4.(Parseval 1799). Prove the identity (2.24).

Hint. Insert the definitions into

$$
\| \widehat { f } \| _ { L ^ { 2 } } ^ { 2 } = \int _ { - \infty } ^ { \infty } \widehat { f } ( \xi ) \overline { { { \widehat { f } } } } ( \xi ) d \xi
$$

to get a triple integral. Two of these integrals then disappear with the Fourier inversion formula.

Remark. You may be astonished to see that Parseval's identity is older than Fourier series and Fourier transforms. Well, Parseval's identity was originally a formula between an infinite sum and an integral, which was later re-interpreted and generalized to become what it is today.

5. Substitute $\xi = \pi$ in Formula (2.23) to obtain an easy minorization for $\| \widehat { K _ { q } } \| _ { L ^ { \infty } }$ Then compute for the methods defined in the proof of Lemma 2.3 (normalized by $\sigma ( 1 ) = 1 \dot { } .$ ）the value $\sigma ( - 1 )$ for $\varepsilon$ small. This then shows that $\widehat { K _ { q } }$ becomes very large.

6. Use the formula (see the proof of Lemma III.3.8)

$$
\mu _ { 2 \jmath + 1 } = \int _ { - 1 } ^ { + 1 } x ^ { 2 \jmath } \left( \left( \log \frac { 1 + x } { 1 - x } \right) ^ { 2 } + \pi ^ { 2 } \right) ^ { - 1 } d x
$$

to show that $\mu _ { 1 } > \mu _ { 3 } > \mu _ { 5 } > . . . > 0$ ·

7. Show that for $q \simeq p$ Eq.(2.23) becomes, by substituting $i \xi = h$ and letting $h  0$ in Eq. (1.20), $\widehat { K _ { p } } ( 0 ) = C _ { p + 1 }$ ， where $C _ { p + 1 }$ is, for $\sigma ( 1 ) = 1$ , the error constant.

Formula (2.36) then provides, for $p = k$ and $t \to \infty$ ,lower bounds for the error constant (see “Theorem $4 . 5 ^ { \prime \prime }$ of Jeltsch & Nevanlinna 1982).

8.For $p = k + 1$ ， the polynomials $Q _ { k - 1 }$ and $Q _ { k }$ in (2.42） vanish identically, because the subdegree must be $p$ . Compute in this case the constants $D _ { \imath }$ and $D _ { 2 }$ . It is also easy to compute them for $p = k - 1$ . In the general case the optimal solution satisfies a sort of “Tchebysheff alternative".

Results.

Case $p = k + 1 ~ ( Q = 0 )$   

<table><tr><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=2>p=3 p=4 p=5 p=6         D2k=2 k=3k=4k=5</td><td rowspan=1 colspan=1>p=3 p=4 p=5 p=6k=2 k=3 k=4 k=5</td></tr><tr><td rowspan=2 colspan=1>q=0q=1q=2q=3q=4q=5q=6</td><td rowspan=2 colspan=2>0.47420.56950.7020 0.8813       q=00.3876 0.4435 0.52980.6505       q=10.3524 0.3659 0.41520.4933       q=20.5000 0.3381 0.34590.3891       q=30.5000 0.32510.3275       q=40.5000 0.3131       q=50.5000       q=6</td><td rowspan=2 colspan=1>0.36070.45010.57060.73190.27540.33470.41630.52630.22050.25700.310880.38520.1935 0.2075 0.2400 0.28880.1849 0.1956 0.22440.1770 0.18450.1698</td></tr><tr><td rowspan=1 colspan=1>0.5000 0.3131       q=5</td></tr></table>

Case $p = k - 1$ (one free constant in $Q$ ）：

<table><tr><td>D1</td><td>p=3 p=4 p=5 p=6 k=4 k=5 k=6 k=7</td><td></td><td>D2</td><td>p=3 p=4 p=5 p=6 k=4 k=5 k=6 k=7</td></tr><tr><td>q=0</td><td>0.0511</td><td>0.0362 0.0262 0.0193</td><td>q=0</td><td>0.0195 0.0142 0.01040.0077 0.0191 0.0138 0.0101</td></tr><tr><td></td><td>0.0727 0.0499 0.0353</td><td>0.0256</td><td>q=1 0.0269</td></tr><tr><td>q=1</td><td></td><td></td></tr><tr><td>q=2</td><td>0.1100 0.0709 0.0486 0.0344</td><td>0.0384 0.0263 0.0186 0.0135 q=2</td></tr><tr><td>0.2031 0.1070 0.0691 0.0474 q=3</td><td>q=3</td></tr><tr><td>q=4</td><td>0.0583 0.0374 0.0256 0.0181</td></tr><tr><td>q=5</td><td>q=4</td></tr><tr><td>0.1962 0.1041 0.0673 0.1894 0.1012 0.1828 q=6</td><td>0.0567 0.0365 0.0250 0.0552 0.0356</td></tr><tr><td>q=6</td><td>q=5</td></tr></table>

Case $p = k - 3$ (two free constants in $Q$ ）：

<table><tr><td>D1</td><td>p=3 p=4 p=5 p=6 k=6k=7k=8k=9</td><td></td><td>D2</td><td></td><td>p=3 p=4 p=5 p=6 k=6k=7 k=8 k=9</td><td></td></tr><tr><td>q=0</td><td></td><td>0.00300.00140.0007 0.0003</td><td></td><td>q=0</td><td>0.0007 0.00040.0002 0.0001</td><td></td></tr><tr><td>q=1</td><td></td><td>0.0066 0.0029 0.0014 0.0007</td><td>q=1</td><td></td><td>0.0015 0.0007 0.0003</td><td>0.0002</td></tr><tr><td>q=2</td><td></td><td>0.0160 0.0066 0.0029 0.0014</td><td></td><td>q=2</td><td>0.0034 0.0015 0.0007 0.0003</td><td></td></tr><tr><td>q=3</td><td>0.0457 0.0158 0.0065 0.0029</td><td></td><td></td><td>q=3</td><td>0.0082 0.0034 0.0015 0.0007</td><td></td></tr><tr><td>q=4</td><td></td><td>0.0448 0.0156 0.0064</td><td></td><td>q=4</td><td>0.0081 0.0033 0.0015</td><td></td></tr><tr><td>q=5</td><td></td><td>0.0439 0.0154</td><td></td><td>q=5</td><td></td><td>0.0080 0.0033</td></tr><tr><td>q=6</td><td></td><td></td><td>0.0431</td><td>q=6</td><td></td><td>0.0079</td></tr></table>

# V.3 Generalized Multistep Methods

The Dahlquist bound of two on the order of $A$ -stable multistep methods was the imperative to propound ... weaker stability properties，... An alternative approach for circumventing Dahlquist's bound is to modify the class of methods,rather than the property.

(T.A. Bickart & W.B.Rubin 1974)

The search for higher order $A$ -stable multistep methods is carried out in two main directions:

Use higher derivatives of the solutions; Throw in additional stages, off-step points, super-future points and the like, which leads into the large field of general linear methods.

# Second Derivative Multistep Methods of Enright

Hermite's formulas are rediscovered and republished every four years. (P.J. Davis 1963)

Differentiation of a differential equation

$$
y ^ { \prime } = f ( x , y )
$$

with respect to $x$ gives the second derivative of the solution

$$
y ^ { \prime \prime } { = } f _ { x } + f _ { y } \cdot f = : g ( x , y ) ,
$$

which we shall denote by $g$ . Now a straightforward generalization of both multistep formulas (1.1) and, say, the Taylor series method (see I.8.13)

$$
y _ { n + 1 } = y _ { n } + h f _ { n } + { \frac { h ^ { 2 } } { 2 ! } } g _ { n }
$$

can be written in the form

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { n + \ i } = \hbar \sum _ { i = 0 } ^ { k } \beta _ { \ i } f _ { n + i } + \hbar ^ { 2 } \sum _ { \ i = 0 } ^ { k } \gamma _ { i } g _ { n + i }
$$

where the $\alpha _ { \ i } , \beta _ { \ i } , \gamma _ { \ i }$ are parameters which must be chosen appropriately. Most of the theory of linear multistep methods (Sect.III.2） generalizes without difficulty. Taylor expansion similar to (II.2.5) shows that method (3.3) is of order $p$ if and only if

$$
\sum _ { i = 0 } ^ { k } \alpha _ { \ i } i ^ { q } = q \sum _ { i = 0 } ^ { k } \beta _ { \ i } i ^ { q - 1 } + q ( q - 1 ) \sum _ { i = 0 } ^ { k } \gamma _ { \ o { i } } i ^ { q - 2 }
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_18, $©$ Springer-Verlag Berlin Heidelberg 2010

for $0 \leq q \leq p$ . The first two of these formulas are identical to (I1.2.6),ie., to

$$
\varrho ( 1 ) = 0 , \qquad \varrho ^ { \prime } ( 1 ) = \sigma ( 1 ) .
$$

The error constant (seeEq. (II.2.13) and Exercise2 of Sect. I.4) is given by

$$
C = { \frac { 1 } { \sigma ( 1 ) ( p + 1 ) ! } } \left( \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { p + 1 } - ( p + 1 ) \sum _ { \iota = 0 } ^ { k } \beta _ { i } i ^ { p } - ( p + 1 ) p \sum _ { \iota = 0 } ^ { k } \gamma _ { \iota } i ^ { p - 1 } \right) .
$$

A search for a good choice of the free parameters $\alpha _ { \imath } , \beta _ { \imath } , \gamma _ { \imath }$ was undertaken by Enright (1974) with the following ideas:

(i) Set $\alpha _ { k } = 1$ ， $\alpha _ { k - 1 } = - 1$ ， $\alpha _ { k - 2 } = . . . = \alpha _ { 0 } = 0$ to ensure reasonable stability in a neighbourhood of the origin as in the standard Adams formulas;   
(ii) Set $\gamma _ { k } \neq 0$ ， $\gamma _ { k - 1 } = . . . = \gamma _ { 0 } = 0$ to ensure stability at infinity as in the BDF formulas;   
(iii) Determine the remaining $k + 2$ coefficients $\gamma _ { k } , \beta _ { k } , \beta _ { k - 1 } , . . . , \beta _ { 0 }$ from Equations (3.4) for $q = 1 , 2 , \ldots , k + 2$ （ $q = 0$ is satisfied with (i)) to ensure a reasonably high order.

The result is a class of $k$ -step formulas of order $k + 2$ , which are of the form

$$
y _ { n + 1 } = y _ { n } + h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f _ { n + \imath - k + 1 } + h ^ { 2 } \gamma _ { k } g _ { n + 1 } .
$$

The first few of these methods are

$$
\begin{array} { r l } & { k = 1 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 2 } { 3 } \int _ { n + 1 } + \frac { 1 } { 3 } \int _ { n } \biggr ) - \frac { 1 } { 6 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 2 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 2 9 } { 4 8 } \int _ { n + 1 } + \frac { 5 } { 1 2 2 } f _ { n } - \frac { 1 } { 4 8 } f _ { n - 1 } \biggr ) - \frac { 1 } { 8 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 3 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 3 0 7 } { 5 4 0 } f _ { n + 1 } + \frac { 1 9 } { 4 0 } f _ { n } - \frac { 1 } { 2 0 } f _ { n - 1 } + \frac { 7 } { 1 0 8 0 } f _ { n - 2 } \biggr ) } \\ & { \qquad - \frac { 1 9 } { 1 8 0 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 4 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 3 1 3 3 } { 5 7 6 0 } f _ { n + 1 } + \frac { 4 7 7 } { 9 0 } f _ { n } - \frac { 4 1 } { 4 8 0 } f _ { n - 1 } + \frac { 1 } { 4 5 } f _ { n - 2 } } \\ & { \qquad \quad - \frac { 1 7 } { 5 7 6 0 } f _ { n - 3 } \biggr ) - \frac { 3 } { 3 2 5 } \hbar ^ { 2 } g _ { n + 1 } } \end{array}
$$

For a general expression, see Eq.(3.12) below and Exercise 1.

The stability analysis for second derivative methods is again done by linearizing and leads to

$$
y ^ { \prime } = \lambda y \qquad \mathrm { f o r ~ w h i c h } \qquad y ^ { \prime \prime } = \lambda ^ { 2 } y .
$$

This, inserted into (3.3), gives as the characteristic equation

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - \mu \beta _ { \imath } - \mu ^ { 2 } \gamma _ { \imath } ) \zeta ^ { \imath } = 0 , \qquad \mu = h \lambda
$$

instead of (1.6). Equation (3.9) is, for $\zeta = e ^ { \imath \theta }$ , a quadratic equation which gives rise to two root locus curves which, together, describe the stability domain. The Enright methods (3.7) turn out to be $A$ -stable for $k \approx 1$ and 2 (hence for $p = 3$ and 4) and are stiffly stable for $k \approx 3$ , 4, 5,6 and 7. The corresponding values $\alpha$ (for $A ( \alpha )$ -stability), $D$ and the error constants $C$ are given in Table 3.1. Pictures are shown in Fig.3.1.

Table 3.1. Stability characteristics and error constants for Enright methods   

<table><tr><td>k</td><td>1 2 3 4 5 6 7</td></tr><tr><td>3 P</td><td>8 9</td></tr><tr><td>4 5 6 7</td><td></td></tr><tr><td>90° 90° 87.88° 82.03° Q D 0. 0. 0.103</td><td>73.10° 59.95° 37.61° 0.526 1.339 2.728 5.182</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/d5d811e41c4f2d48a0c176b805bbe487d23e5731eceadf0e4fbf40cb51796ed9.jpg)  
Fig.3.1. Stability domains of Enright methods

Dense Output for Enright Methods. We have seen in Sect.II.1 that Newton's interpolation formula,basedonthedata $x _ { n + 1 } , x _ { n } , \ldots , x _ { n - k + 1 } ,$

· when integrated from $x _ { n }$ t0 $x _ { n + 1 }$ , leads to the implicit Adams methods;   
$\bullet$ when differentiated at $x _ { n + 1 }$ ,leads to the BDF methods.

It is natural to apply the same idea to Hermite interpolation (Addison 1979): guided by much previous experience (see above) we choose the data points

$$
x _ { n + 1 } ( { \mathrm { d o u b l e ~ n o d e } } ) , x _ { n } , x _ { n - 1 } , \cdot \cdot \cdot , x _ { n - k + 1 } ( { \mathrm { s i m p l e ~ n o d e s } } ) .
$$


<!-- chunk 0005: pages 281-350 -->
This gives the following scheme of divided differences

$$
\begin{array} { r l } { s = 1 \quad } & { f _ { 1 } } \\ { s = 1 \quad } & { f _ { 1 } } \\ { s = 0 \quad } & { f _ { 0 } \quad } & { \nabla f _ { 1 } ^ { \prime } - \nabla f _ { 1 } \quad } \\ { s = 0 \quad } & { f _ { 0 } } \\ { s = - 1 \quad f _ { - 1 } \quad } & { \nabla f _ { 0 } } \end{array} \quad \begin{array} { r l } { \frac { \nabla ^ { 2 } f _ { 1 } } { 2 ! } } & { \frac { h f _ { 1 } ^ { \prime } - \nabla f _ { 1 } - \frac { 1 } { 2 } \nabla ^ { 2 } f _ { 1 } } { 2 ! } } \\ { \frac { \nabla ^ { 2 } f _ { 1 } } { 2 ! } } & { \frac { h f _ { 1 } ^ { \prime } - \nabla f _ { 1 } - \frac { 1 } { 2 } \nabla ^ { 2 } f _ { 1 } } { 2 ! } } \end{array}
$$

where $x = x _ { n } + s h$ . For these “confluent” data, Newton's interpolation formula becomes

$$
\begin{array} { r l r } { f ( x _ { n } + s h ) = f _ { 1 } + ( s - 1 ) h f _ { 1 } ^ { \prime } + ( s - 1 ) ^ { 2 } ( h f _ { 1 } ^ { \prime } - \nabla f _ { 1 } ) } & { } & \\ { + ( s - 1 ) ^ { 2 } s \frac { h f _ { 1 } ^ { \prime } - \nabla f _ { 1 } - \frac { 1 } { 2 } \nabla ^ { 2 } f _ { 1 } } { 2 ! } } & { ( 3 ) } & \\ { + ( s - 1 ) ^ { 2 } s ( s + 1 ) \frac { h f _ { 1 } ^ { \prime } - \nabla f _ { 1 } - \frac { 1 } { 2 } \nabla ^ { 2 } f _ { 1 } - \frac { 1 } { 3 } \nabla ^ { 3 } f _ { 1 } } { 3 ! } + . . . } & { } & \end{array}
$$

We now interpret $f$ as the derivative $f ( x , y ( x ) )$ of the solution,so that $f ^ { \prime }$ becomes the second derivative. Integrating Formula (3.11) from $x _ { n }$ to $x _ { n + 1 }$ we obtain

$$
y _ { n + 1 } = y _ { n } + h f _ { n + 1 } - h \sum _ { j = 1 } ^ { k } { \frac { \nabla ^ { j } f _ { n + 1 } } { j } } \left( \sum _ { \iota = j } ^ { k } \nu _ { \iota } \right) + h ^ { 2 } g _ { n + 1 } \cdot \left( \sum _ { \iota = 0 } ^ { k } \nu _ { \iota } \right)
$$

where

$$
\nu _ { \ i } = \int _ { 0 } ^ { 1 } { \frac { ( s - 1 ) ^ { 2 } s ( s + 1 ) \ldots ( s + i - 2 ) } { i ! } } d s = ( - 1 ) ^ { \prime } \int _ { 0 } ^ { 1 } ( s - 1 ) { \binom { 1 - s } { i } } d s .
$$

Table 3.2. Coefficients for Enright methods   

<table><tr><td>1</td><td>0</td><td>1</td><td>2 3</td><td></td><td>4</td><td>5</td><td>6 7</td></tr><tr><td rowspan="2">Vj</td><td>1</td><td>1 1</td><td>7</td><td>17</td><td>41</td><td>731</td><td>8563</td></tr><tr><td>2</td><td>3</td><td>24 360</td><td>1440</td><td>5040</td><td>120960</td><td>1814400</td></tr></table>

The first few values of $\nu _ { i }$ are given in Table 3.2 and Eq.(3.12) is seen to be identical with (3.7). Dense output, of course, is obtained by integrating (3.11) from $x _ { n }$ to $x _ { n } + \theta h$ ：

$$
y ( x _ { n } + \theta h ) \approx y _ { n } + \theta h f _ { n + 1 } - h \sum _ { j = 1 } ^ { k } { \frac { \nabla ^ { j } f _ { n + 1 } } { j } } \left( \sum _ { \iota = j } ^ { k } \nu _ { \iota } ( \theta ) \right) + h ^ { 2 } g _ { n + 1 } \cdot \left( \sum _ { \iota = 0 } ^ { k } \nu _ { \iota } ( \theta ) \right)
$$

where

$$
\nu _ { i } ( \theta ) = ( - 1 ) ^ { \imath } \int _ { 0 } ^ { \theta } ( s - 1 ) \binom { 1 - s } { i } d s .
$$

# Second Derivative BDF Methods

If we are interested in a“second derivative” analogue of the BDF methods, we replace all $f ^ { \prime } { \bf s }$ by $\boldsymbol { y } ^ { \prime } \mathbf { s }$ in (3.11) and differentiate twice at $x _ { n + 1 }$ . This, on setting $y ^ { \prime \prime } ( x _ { n + 1 } ) = g _ { n + 1 }$ , results in the methods

$$
{ \frac { h ^ { 2 } } { 2 } } g _ { n + 1 } = \bigg ( \sum _ { i = 1 } ^ { k } { \frac { 1 } { i } } \bigg ) h f _ { n + 1 } - \sum _ { j = 1 } ^ { k } \bigg ( \sum _ { \ i = 2 } ^ { k } { \frac { 1 } { i } } \bigg ) { \frac { \nabla ^ { j } y _ { n + 1 } } { j } }
$$

which we call “Second derivative BDF methods"(SDBDF, the reader is cautioned against confusion: Cash (1981) uses this expression for the class of "Enright methods"). Analyzing the stability of these methods leads to the parameters of Table 3.3. The root locus curves are drawn in Fig.3.2.

In complete analogy to the behaviour of implicit Adams compared to BDF methods, the second derivative BDF methods have larger error constants than the Enright methods, but allow stiffly stable methods of higher order.

Table 3.3. Stability characteristics and error constants for SDBDF methods   

<table><tr><td>k</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>p</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>α</td><td>90°</td><td>90°</td><td>90°</td><td>89.36°</td><td>86.35°</td><td>80.82°</td><td>72.53°</td><td>60.71°</td><td>43.39°</td><td>12.34°</td></tr><tr><td>D</td><td>0.</td><td>0.</td><td>0.</td><td>0.015</td><td>0.128</td><td>0.401</td><td>0.886</td><td>1.646</td><td>2.770</td><td>4.373</td></tr><tr><td>C</td><td>.1667</td><td>.0556</td><td>.0273</td><td>.0160</td><td>.0104</td><td>.0073</td><td>.0054</td><td>.0041</td><td>.0032</td><td>.0026</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/5de77cd29428ce48cde8b732715402da96692757bb9901384b41cea6a5a2f05f.jpg)  
Fig. 3.2. Root locus curves of SDBDF methods

# Blended Multistep Methods

The original motivation for blended methods goes as follows (Skeel & Kong 1977): We know that Adams methods

$$
- y _ { n + 1 } + y _ { n } + h \bigl ( \beta _ { k } f _ { n + 1 } + \beta _ { k - 1 } f _ { n } + \ldots + \beta _ { 0 } f _ { n - k + 1 } \bigr ) = 0 \qquad ( A M F ^ { ( k + 1 ) } )
$$

are a very good choice for nonstiff problems, and that BDF methods

$$
- \bigl ( \alpha _ { k } y _ { n + 1 } + \alpha _ { k - 1 } y _ { n } + . . . + \alpha _ { 0 } y _ { n - k + 1 } \bigr ) + h f _ { n + 1 } = 0
$$

are a very good choice for stiff problems. Nonstiff problems are characterized by the fact that $- h \partial f / \partial y$ is small, while stiff problems are characterized by large $- h \partial f / \partial y$ (at first this makes sense only for scalar equations; but it works as well for systems of equations if we descend into the eigenspaces of the Jacobian matrix $\partial f / \partial y = J )$ . The idea is now to use a weighted mean ("blend", a term suggested by C.W. Gear) of the two methods such as

$$
\{ A M F ^ { ( k + 1 ) } \} - \gamma ^ { ( k ) } h J \{ B D F ^ { ( k ) } \} = 0
$$

where $\gamma ^ { ( k ) }$ is a free parameter. The factor $- h J$ , when small or large, just puts the weight at the right place,as required by the above motivation. Taylor expansion shows that Eq.(3.15) is for all $\gamma ^ { ( k ) }$ of order $p = k + 1$ (the factor $\because h ^ { , }$ in the second term saves one order), even if $J$ differs from $\partial f / \partial y$ . This method is thus a multistep analogue to the W -methods discussed in Sect.IV.7.

Example. We put $k \approx 2$ in (3.15) and insert the values from Sect.III.1, Formulas $\left( \mathrm { I I I } . 1 . 8 ^ { \circ } \right)$ and (III.1.22"):

$$
\begin{array} { l } { { y _ { n + 1 } = y _ { n } + h \Big ( \displaystyle \frac { 5 } { 1 2 } f _ { n + 1 } + \displaystyle \frac { 8 } { 1 2 } f _ { n } - \displaystyle \frac { 1 } { 1 2 } f _ { n - 1 } \Big ) } } \\ { { \qquad - \gamma ^ { ( 2 ) } h J \Big ( - \displaystyle \frac { 3 } { 2 } y _ { n + 1 } + 2 y _ { n } - \displaystyle \frac { 1 } { 2 } y _ { n - 1 } + h f _ { n + 1 } \Big ) . } } \end{array}
$$

If we now suppose that our differential equation is linear and autonomous $y ^ { \prime } = J y$ then $J y _ { n + i } = f _ { n + i }$ and the equation simplifies. Two special choices for $\gamma ^ { ( 2 ) }$ are then interesting:

a) $\gamma ^ { ( 2 ) } = 1 / 6 : \mathrm { I n }$ this case the $f _ { n - 1 }$ cancels with $J y _ { n - 1 }$ and Eq.(3.16) becomes the $\left( k - 1 \right)$ -step Enright formula of order $k + 1$ ；   
b） $\gamma ^ { ( 2 ) } = 1 / 8$ : This is a “superconvergence point’ for linear equations and we obtain the $k$ -step Enright formula of order $k + 2$

Both properties generalize to arbitrary $k$ ; in the first case we have to put $\gamma ^ { ( k ) } =$ $- k \gamma _ { k } ^ { \ast }$ $\begin{array} { r } { \gamma ^ { ( k ) } = - \sum _ { i = 0 } ^ { k } \nu _ { _ { i } } } \end{array}$ ，where the $\gamma _ { k } ^ { * }$ are the values of Table II.1.2, and in the second case we implement. A third possibility is to choose $\gamma ^ { ( k ) }$ in order to maximize the angle $\alpha$ for $A ( \alpha )$ -stability. The root-locus-curve equation for general $\gamma ^ { ( k ) }$ becomes

Table 3.4. Values for $\gamma ^ { ( k ) }$ and corresponding angles for blended methods   

<table><tr><td>k</td><td>-kY p</td><td>α for 2(k）=-kY</td><td>(k） Yopt</td><td>α for (k） 2(k） 二 Yopt</td></tr><tr><td>1</td><td>2 .5</td><td></td><td>90° [0,+00)</td><td>90°</td></tr><tr><td>2</td><td>3</td><td>.1666667 90°</td><td>[.125,+00)</td><td>90°</td></tr><tr><td>3</td><td>4 .125</td><td>90°</td><td>[.12189,.68379]</td><td>90°</td></tr><tr><td>4</td><td>5</td><td>.1055556 87.88°</td><td>.1284997</td><td>89.42°</td></tr><tr><td>5</td><td>6 .09375</td><td>82.03°</td><td>.1087264</td><td>86.97°</td></tr><tr><td>6</td><td>7</td><td>.08561508 73.10°</td><td>.0962596</td><td>82.94°</td></tr><tr><td>7</td><td>8</td><td>.07957176 59.95°</td><td>.08754864</td><td>77.43°</td></tr><tr><td>8</td><td>9</td><td>.07485229 37.61°</td><td>.08105624</td><td>70.22°</td></tr><tr><td>9</td><td>10</td><td>.07103299 11</td><td>.07599875</td><td>60.68°</td></tr><tr><td>10</td><td>11</td><td>.06785850</td><td>.07192937</td><td>47.63°</td></tr><tr><td>11</td><td>12</td><td>.06516462 11</td><td>.06857226</td><td>28.68°</td></tr></table>

$$
\mu ^ { 2 } \cdot \gamma ^ { ( k ) } + \mu \Big ( - \sum _ { \jmath = 0 } ^ { k } \gamma _ { \jmath } ^ { * } \big ( 1 - e ^ { - \imath \theta } \big ) ^ { \jmath } - \gamma ^ { ( k ) } \sum _ { \jmath = 1 } ^ { k } \frac { 1 } { j } \big ( 1 - e ^ { - i \theta } \big ) ^ { \jmath } \Big ) + \big ( 1 - e ^ { - \imath \theta } \big ) = 0 .
$$

Skeel & Kong(1977) have carefully computed the optimal $\gamma ^ { ( k ) }$ (see Table 3.4, the imprecise values for the “Enright column” have been corrected) and arrived thereby at stiffly stable methods up to order 12.

# Extended Multistep Methods of Cash

The second possibility for circumventing Dahlquist's barrier, instead of adding higher derivatives,is to add further stages,additional nodes,or off-step points. This leads into the huge desert ("A fable of K. Burrage") of general linear methods which have been discussed in Sect.III.8. Pioneering results for stiff differential equations are the “composite multistep methods”of Sloate & Bickart (1973), Bickart & Rubin (1974), the “hybrid” methods of England (1982),and the “extended’BDF methods of Cash (198O). We shall present the basic ideas for the latter in some detail. In order to increase stability of the BDF methods,we extend them by ading a “super-future" point at $x _ { n + k + 1 }$

$$
\sum _ { \jmath = 0 } ^ { k } \alpha _ { j } y _ { n + \jmath } = h \beta _ { k } f _ { n + k } + h \beta _ { k + 1 } f _ { n + k + 1 } ,
$$

where the coefficients are obtained by solving $\textstyle \sum _ { \ j } \alpha _ { \ j } j ^ { q } = q \sum _ { \ j } \beta _ { \ j } j ^ { q - 1 }$ for $q =$ $0 , 1 , \ldots , k + 1$ with the normalization $\alpha _ { k } = 1$ .Formula (3.17) is then used as follows (see Fig.3.3):

(i) Suppose that the solution values $y _ { n } , y _ { n + 1 } , \ldots , y _ { n + k - 1 }$ are available. Compute ${ \overline { { y } } } _ { n + k }$ as the solution of the conventional BDF formula

$$
\sum _ { \jmath = 0 } ^ { k } \widehat { \alpha } _ { \jmath } y _ { n + \jmath } = h \widehat { \beta } _ { k } f _ { n + k } , \qquad \widehat { \alpha } _ { k } = 1 ;
$$

(ii) Compute $\overline { { y } } _ { n + k + 1 }$ as the solution of the same BDF formula advanced by one step (using ${ \overline { { y } } } _ { n + k }$ for $y _ { n + k } )$

$$
\sum _ { \jmath = 0 } ^ { k } { \widehat { \alpha } } _ { \jmath } y _ { n + \jmath + 1 } = h \widehat { \beta } _ { k } f _ { n + k + 1 } \qquad ( y _ { n + k } : = { \overline { { y } } } _ { n + k } )
$$

and set ${ \overline { { f } } } _ { n + k + 1 } = f ( x _ { n + k + 1 } , { \overline { { y } } } _ { n + k + 1 } ) ;$

(ii) Discard ${ \overline { { y } } } _ { n + k }$ , insert ${ \overline { { f } } } _ { n + k + 1 }$ into (3.17)andsolve for a new $y _ { n + k }$ which serves as the final numerical solution of the method.

The advance of the numerical solution by one step thus requires the solution of three nonlinear systems of dimension $n$ . In stage (i) and stage (ii) we have excel-lent initial approximations: the super future point of the previous step and the value ${ \overline { { y } } } _ { n + k }$ , respectively.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/155dd54635f6d33da7c0e9923f666d7a4bba20a49aa55ac9bb944ba881d6a4f4.jpg)  
Fig.3.3. Errors of Cash's algorithm

Lemma 3.1 (Cash 1980). If Formula (3.17) is of order $k + 1$ and the BDF methods used in $( 3 . 1 7 i )$ and $( 3 . 1 7 i i )$ are of order $k$ ， then the whole predictor-corrector algorithm $( i ) - ( i i i )$ is of order $k + 1$

Proof. Suppose that $y _ { n } , \ldots , y _ { n + k - 1 }$ are on the exact solution (Fig.3.3). Then a simple calculation (as in the proof of Lemma III.2.2, see also Eq.(III.2.7)) shows that

$$
\begin{array} { c } { { y ( x _ { n + k } ) - \overline { { { y } } } _ { n + k } = C _ { 1 } h ^ { k + 1 } y ^ { ( k + 1 ) } ( x _ { n + k } ) + { \mathcal O } ( h ^ { k + 2 } ) } } \\ { { y ( x _ { n + k + 1 } ) - \overline { { { y } } } _ { n + k + 1 } = C _ { 1 } \Big ( 1 - \displaystyle \frac { \widehat { \alpha } _ { k - 1 } } { \widehat { \alpha } _ { k } } \Big ) h ^ { k + 1 } y ^ { ( k + 1 ) } ( x _ { n + k } ) + { \mathcal O } ( h ^ { k + 2 } ) } } \end{array}
$$

where $C _ { 1 }$ depends on the BDF method used. If now $C _ { 2 } h ^ { k + 2 } y ^ { ( k + 2 ) } ( \xi )$ is the defect ofEq. (3.17) (for the exact solution),replacing $h f ( x _ { n + k + 1 } , y ( x _ { n + k + 1 } ) )$ by

$h f ( x _ { n + k + 1 } , \overline { { y } } _ { n + k + 1 } )$ adds the expression obtained in (3.19) to this error and we obtain

$$
\begin{array} { c } { { y ( x _ { n + k } ) - y _ { n + k } = h ^ { k + 2 } \Big ( C _ { 2 } y ^ { ( k + 2 ) } + \beta _ { k + 1 } C _ { 1 } \big ( 1 - \frac { \widehat \alpha _ { k - 1 } } { \alpha _ { k } } \big ) \frac { \partial f } { \partial y } \cdot y ^ { ( k + 1 ) } \Big ) ( x _ { n + k } ) } } \\ { { + \mathcal { O } ( h ^ { k + 3 } ) . } } \end{array}
$$

The method is thus of order $k + 1$ . Like Runge-Kutta methods, but unlike linear multistep methods, the principal error term is composed of several “elementary differentials". □

Modified EBDF Methods. A disadvantage of the above algorithm is that stages (i) and (ii) represent nonlinear systems with the same Jacobian $I - \hbar \widehat { \beta } _ { k } J$ ,but stage (iii)has a different Jacobian $I - h \beta _ { k } J$ . This requires an extra LU-decomposition. The idea is to modify Eq. (3.17) for stage (iii) as follows (Cash 1983):

$$
\sum _ { \jmath = 0 } ^ { k } \alpha _ { \jmath } y _ { n + \jmath } = h \widehat { \beta } _ { k } f _ { n + k } + h ( \beta _ { k } - \widehat { \beta } _ { k } ) \overline { { f } } _ { n + k } + h \beta _ { k + \downarrow } \overline { { f } } _ { n + k + \downarrow } .
$$

This just adds an extra $h ^ { k + 2 }$ -term to the above proof and does not alter the order of the method. It allows the same Jacobian to be used in the Newton iteration for all three stages,and, possibly, to preserve it over several steps as well.

Stability Analysis. We insert ${ \bar { \hbar } } f _ { \jmath } = \mu y _ { \jmath }$ in (3.17.mod), (3.17i) and (3.17ii),set $y _ { n } = 1$ ， $y _ { n + 1 } = \zeta , \ldots , y _ { n + k - 1 } = \zeta ^ { k - 1 }$ and compute, following the algorithm (i), (i), (ii),the solution $y _ { n + k } = : \zeta ^ { k }$ . This gives the characteristic equation

$$
A \mu ^ { 3 } + B \mu ^ { 2 } + C \mu + D = 0
$$

where

$$
\begin{array} { l } { { A = \widehat { \beta } _ { k } ^ { 3 } \zeta ^ { k } } } \\ { { B = - 2 \widehat { \beta } _ { k } ^ { 2 } \zeta ^ { k } + \widehat { \beta } _ { k } ( \beta _ { k } - \widehat { \beta } _ { k } ) R + \widehat { \beta } _ { k } \beta _ { k + 1 } S - \widehat { \beta } _ { k } ^ { 2 } T } } \\ { { C = \widehat { \beta } _ { k } \zeta ^ { k } + ( \widehat { \alpha } _ { k - 1 } \beta _ { k + 1 } - \beta _ { k } + \widehat { \beta } _ { k } ) R - \beta _ { k + 1 } S + 2 \widehat { \beta } _ { k } T } } \\ { { D = - T } } \\ { { R = \displaystyle \sum _ { j = 0 } ^ { k - 1 } \widehat { \alpha } _ { j } \zeta ^ { j } , \quad S = \displaystyle \sum _ { j = 0 } ^ { k - 2 } \widehat { \alpha } _ { j } \zeta ^ { j + 1 } , \quad T = \displaystyle \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta ^ { j } . } } \end{array}
$$

Inserting $\zeta = e ^ { \tau \theta }$ ,Equation (3.21) gives us three roots $\mu _ { \ i } ( \theta ) \ i = 1 , 2 , 3$ ,which describe the stability domain. These,computed by Cardano's formula, are displayed in Fig.3.4. The corresponding stability characteristics are given in Table 3.5. The methods are $A$ -stable for $p \leq 4$ and are stiffly stable for orders up to 9.

Table 3.5. Stability measures for Cash's modified EBDF methods   

<table><tr><td>k</td><td>1</td><td>2 3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>p</td><td>2</td><td>3</td><td>4 5</td><td></td><td>6</td><td>7 8</td><td>9</td></tr><tr><td>α</td><td>90°</td><td>90° 90°</td><td>88.36°</td><td>83.07°</td><td>74.48°</td><td>61.98°</td><td>42.87°</td></tr><tr><td>D</td><td>0.</td><td>0. 0.</td><td>0.040</td><td>0.246</td><td>0.684</td><td>1.402</td><td>2.432</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/e7055502086e9e1968a9f479e49c4d2de0d658a9d2ea55b55a9eefc9499b5c12.jpg)  
Fig.3.4. Stability domains for Cash's MEBDF methods

# Multistep Collocation Methods

... a theorem of great antiquity ... the simple theorem of polynomial interpolation upon which much practical numerical analysis rests ...

(P.J. Davis,Interp.and Approx., Chapter II,1963)

There are essentially two possibilities to extend the idea of collocation, which is so successful in the Runge-Kutta case (see Sect. II.7, Formulas (II.7.16)), into the multistep scene:

a) In a Nordsieck type manner with given $y _ { n } , h y _ { n } ^ { \prime } , h ^ { 2 } y _ { n } ^ { \prime \prime } / 2 , . .$ . compute $y _ { n + 1 }$ ， $h y _ { n + 1 } ^ { \prime } , h ^ { 2 } y _ { n + 1 } ^ { \prime \prime } / 2 , . . .$ The result is a spline function which approximates the solution globally. Butcher's generalized singly-implicit methods (Butcher 1981) are of this type. Extensive studies of these methods are due to Multhei (1982).

b) In a multistep manner with given $y _ { n } , \ y _ { n - 1 } , \ldots , y _ { n - k + 1 }$ compute $y _ { n + 1 }$ then discard, as usual, the last point $y _ { n - k + 1 }$ and continue. This possibility was first proposed and analysed by Guillou & Soulé (1969). It is also the subject of a paper by Lie & Ngrsett (1989) and will retain our attention here in more detail. In evident generalization of Definition II.7.6, the method is defined as follows:

Definition 3.2. Let $s$ real numbers $c _ { 1 } , \ldots , c _ { s }$ (typically between O and 1) be given and $k$ solution values $\mathcal { Y } _ { n } , \mathcal { Y } _ { n - 1 } , \ldots , \mathcal { Y } _ { n - k + 1 }$ . Then define the corresponding $c o l .$ location polynomial $u ( x )$ of degree $s + k - 1$ by (see Fig.3.5)

$$
u ( x _ { \ j } ) = y _ { \ j } \qquad j = n - k + 1 , \ldots . n
$$

$$
u ^ { \prime } ( x _ { n } + c _ { \imath } h ) = f ( x _ { n } + c _ { \imath } h , u ( x _ { n } + c _ { i } h ) ) \quad i = 1 , \ldots , s .
$$

The numerical solution is then

$$
y _ { n + 1 } : = u ( x _ { n + 1 } ) .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/9a6d1cb3504cf3b16c39821caa203df14eda41d374c11517a197ec308ebb938b.jpg)  
Fig. 3.5. The collocation polynomial

If we suppose the derivatives ${ \mathfrak { U } } ^ { \prime } { \bigl ( } x _ { n } + c _ { i } h { \bigr ) }$ are known,Eqs. (3.23a) and (3.23b) constitute a Hermite interpolation problem with incomplete data: the function values at $x _ { n } + c _ { \imath } h$ are missing. We therefore have no nice formulas and reduce the problem to a linear algebraic equation. We introduce the dimensionless coordinate $t = ( x - x _ { n } ) / h$ ， $x = x _ { n } + t h $ ，nodes $t _ { 1 } = - k + 1 , \ldots , t _ { k - 1 } = - 1$ ， $t _ { k } = 0$ and define polynomials ${ \varphi _ { \iota } ( t ) \ ( i = 1 , \ldots , k ) }$ of degree $s + k - 1$ by

$$
\begin{array} { r l } & { \varphi _ { \imath } ( t _ { j } ) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { i f } i \neq j } \\ { 1 } & { \mathrm { i f } i = j } \end{array} \right. \qquad j = 1 , \dots k } \\ & { \varphi _ { \imath } ^ { \prime } ( c _ { \jmath } ) = 0 \qquad j = 1 , \dots , s } \end{array}
$$

and polynomials ${ \psi _ { \iota } ( t ) } \ ( \iota = 1 , \ldots , s )$ by

$$
\begin{array} { r l } & { \psi _ { \imath } ( t _ { j } ) = 0 \qquad \jmath = 1 , \ldots , k } \\ & { \psi _ { \imath } ^ { \prime } ( c _ { \jmath } ) = \left\{ \begin{array} { l l } { 1 } & { \mathrm { i f } i = j } \\ { 0 } & { \mathrm { i f } i \neq j } \end{array} \right. \qquad j = 1 , \ldots , s . } \end{array}
$$

This makes these polynomials a (generalized) Lagrange basis and the polynomial $u ( x )$ is readily written as

$$
u ( x _ { n } + t h ) = \sum _ { j = 1 } ^ { k } \varphi _ { j } ( t ) y _ { n - k + j } + h \sum _ { j = 1 } ^ { s } \psi _ { j } ( t ) u ^ { \prime } ( x _ { n } + c _ { j } h ) .
$$

Formulas (3.24) and (3.25) do not always have a solution (Exercise 4 below). A convenient way of computing them is indicated in Exercise 5. Putting $t = c _ { i }$ in (3.26)，writing $u ( x _ { n } + c _ { \ i } h ) = v _ { i }$ and inserting the collocation condition (3.23b) we obtain

$$
\begin{array} { r } { v _ { \imath } = \displaystyle \sum _ { \jmath = 1 } ^ { k } \varphi _ { \jmath } ( c _ { \imath } ) y _ { n - k + j } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } \psi _ { \jmath } ( c _ { \imath } ) f ( x _ { n } + c _ { j } h , v _ { j } ) } \\ { i = 1 , \ldots , s } \\ { \displaystyle \qquad \quad \cdot _ { n + 1 } = \displaystyle \sum _ { \jmath = 1 } ^ { k } \varphi _ { \jmath } ( 1 ) y _ { n - k + j } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } \psi _ { \jmath } ( 1 ) f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ) , } \end{array}
$$

a general linear method as defined in (III.8.7).

Theorem 3.3. The collocation method (3.23) is equivalent to the general linear method

$$
\begin{array} { l } { { v _ { \imath } = \displaystyle \sum _ { \jmath = 1 } ^ { k } a _ { \imath \jmath } y _ { n - k + \jmath } + h \sum _ { \jmath = 1 } ^ { s } b _ { \imath \jmath } f ( x _ { n } + c _ { j } h , v _ { j } ) \qquad i = 1 , \dots , s } } \\ { { y _ { n + 1 } = \displaystyle \sum _ { \jmath = 1 } ^ { k } a _ { k + 1 , \jmath } y _ { n - k + \jmath } + h \sum _ { \jmath = 1 } ^ { s } b _ { k + 1 , \jmath } f ( x _ { n } + c _ { j } h , v _ { j } ) } } \end{array}
$$

where

$$
a _ { \iota _ { 3 } } = \varphi _ { \jmath } ( c _ { \iota } ) , b _ { \iota _ { 3 } } = \psi _ { \jmath } ( c _ { \iota } ) , a _ { k + 1 , \jmath } = \varphi _ { \jmath } ( 1 ) , b _ { k + 1 , \jmath } = \psi _ { \jmath } ( 1 )
$$

and ${ \varphi } _ { \jmath } ( t ) , \ \psi _ { \jmath } ( t )$ are polynomials defined by (3.24) and (3.25). Formula (3.26) provides $a$ continuous output.

A straightforward extension of the proof of Theorem I.7.9, again using the Grobner & Alekseev formula (I.14.18),yields

Theorem 3.4 (Guillou & Soulé 1969). If the quadrature formula (3.27b) is exact for polynomials $g ( t )$ of $d e g r e e \le s + k + r$ ,i., $\begin{array} { r } { \sum _ { \jmath = 1 } ^ { k } \varphi _ { \jmath } ( 1 ) = 1 } \end{array}$ and

$$
\sum _ { \jmath = 1 } ^ { k } \varphi _ { \jmath } ( 1 ) \int _ { \jmath - k } ^ { 1 } g ( t ) d t = \sum _ { \imath = 1 } ^ { s } \psi _ { \imath } ( 1 ) g ( c _ { \imath } ) ,
$$

then the multistep collocation method (3.28) also has order $s + k + r$

# Methods of “Radau” Type

Nous allons maintenant étudier une classe de formules qui géné- ralise les formules ordinaires de Gauss,Radau et Lobatto.

(Guillou & Soulé 1969)

An interesting question is now how to choose the nodes $c _ { \imath }$ in order to obtain the highest possible order. Using an elegant idea of Krylov (1959) (see the last chapter of his book on integration), Guillou & Soulé (1969) and Lie & Ngrsett (1989) constructed such methods of maximal order $p { = } 2 s { + } k { - } 1$ . Unfortunately, these methods are not stify stable and therefore of no use for stiff problems. Consequently, we fix $c _ { s } = 1$ to achieve stability at infinity and try to determine $c _ { 1 } , \ldots , c _ { s - 1 }$ s0 that the order becomes $p = 2 s + k - 2$ . Because of Theorem 3.4, it is sufficient to consider quadrature problems.

And now to Krylov's idea for integrals, adapted to our situation. We fill in the gaps in the data for Hermite interpolation,i.e., we suppose that the function values $\boldsymbol { v } _ { \iota } = \boldsymbol { u } ( \boldsymbol { x } _ { n } + \boldsymbol { c } _ { \iota } \boldsymbol { h } )$ $( \iota = 1 , \ldots , s - 1 )$ are known and we extend our Lagrange basis accordingly: firstly, we add polynomials $\chi _ { 1 } ( t ) , \ldots , \chi _ { s - 1 } ( t )$ of degree $2 s + k - 2$ which must satisfy

$$
\begin{array} { l l } { { \chi _ { \iota } ( t _ { \jmath } ) = 0 } } & { { j = 1 , \ldots , k } } \\ { { \chi _ { \iota } ^ { \prime } ( c _ { \jmath } ) = 0 } } & { { j = 1 , \ldots , s } } \\ { { \chi _ { \iota } ( c _ { \jmath } ) = \left\{ \begin{array} { l l } { { 1 } } & { { \quad i = j } } \\ { { 0 } } & { { \quad i \neq j } } \end{array} \right. } } & { { j = 1 , \ldots , s - 1 } } \end{array}
$$

(Caution: the last condition is not for $j = s$ , because $c _ { s }$ is not a free node). Secondly, the polynomials $\varphi _ { \imath } ( t )$ and $\psi _ { \imath } ( t )$ are replaced by $\widetilde { \varphi } _ { \ i } ( t ) , ~ \widetilde { \psi } _ { \ i } ( t )$ of degree $2 s + k - 2$ which,in addition to (3.24)and (3.25), must satisfy

$$
\widetilde { \varphi } _ { \iota } ( c _ { \jmath } ) = 0 \quad \mathrm { ~ a n d ~ } \quad \widetilde { \psi } _ { \iota } ( c _ { \jmath } ) = 0 \qquad j = 1 , \dots , s - 1 .
$$

Then Eq. (3.26) is replaced by

$$
\widetilde { u } ( x _ { n } + t h ) = \displaystyle \sum _ { j = 1 } ^ { k } \widetilde { \varphi } _ { j } ( t ) y _ { n - k + j } + \displaystyle \sum _ { j = 1 } ^ { s - 1 } \chi _ { j } ( t ) v _ { j } + h \sum _ { j = 1 } ^ { s } \widetilde { \psi } _ { j } ( t ) u ^ { \prime } ( x _ { n } + c _ { j } h ) ,
$$

and (3.27b) becomes the integration formula

$$
y _ { n + 1 } = \sum _ { \jmath = 1 } ^ { k } \widetilde { \varphi } _ { \jmath } ( 1 ) y _ { n - k + \jmath } + \sum _ { \jmath = 1 } ^ { s - 1 } \chi _ { \jmath } ( 1 ) v _ { j } + h \sum _ { \jmath = 1 } ^ { s } \widetilde { \psi } _ { \jmath } ( 1 ) u ^ { \prime } ( x _ { n } + c _ { \jmath } h )
$$

which is of order $2 s + k - 2$ . If now, by a miracle, all coefficients

$$
\chi _ { \ j } ( 1 ) = 0 \qquad ( \ j = 1 , \ldots , s - 1 )
$$

were zero, then the quadrature Formula (3.27b) would become equal to (3.33), since by uniqueness the remaining coeficients $\widetilde { \varphi } _ { \jmath } ( 1 )$ and $\widetilde { \psi } _ { \jmath } ( 1 )$ must also be equal to $\varphi _ { j } ( 1 )$ and $\psi _ { \jmath } ( 1 )$

Theorem 3.5. If the collocation points $c _ { 1 } , \ldots , c _ { s - 1 }$ (with $c _ { s } = 1$ ) are chosen such that the polynomials $\varphi _ { \ i } ( t ) , \psi _ { \ i } ( t )$ of(3.24), (3.25) exist uniquely and that (3.34) is true, then the collocation method (3.28) is of highest possible order $2 s + k - 2$ .□

Computation of the Nodes. Equation (3.34) together with the conditions (3.30) allow us to write the polynomials ${ \boldsymbol { \chi } } _ { \boldsymbol { \imath } } ( t )$ in the simple form

$$
\chi _ { \iota } ( t ) = C \prod _ { \substack { j = 1 } } ^ { k } ( t - t _ { \jmath } ) \prod _ { \substack { \jmath = 1 } \atop \jmath \neq \imath } ^ { s } ( t - c _ { \jmath } ) ^ { 2 } .
$$

where $C$ is determined by $\chi _ { \iota } { \left( c _ { \iota } \right) } = 1$ . This then satisfies all derivative requirements (3.30b)， except at $c _ { \imath } . \chi _ { \imath } ^ { \prime } ( c _ { \imath } )$ is readily computed from (3.35) by taking logarithms and the conditions $\chi _ { \imath } ^ { \prime } { \left( c _ { \imath } \right) } = 0$ give

$$
\sum _ { \jmath = 1 } ^ { k } \frac { 1 } { c _ { \imath } - t _ { \jmath } } + \sum _ { \jmath = 1 \atop \jmath \neq \imath } ^ { s } \frac { 2 } { c _ { \imath } - c _ { \jmath } } = 0 , \qquad i = 1 , \dots , s - 1 .
$$

Example. For the case $s \simeq 3$ ,Eqs. (3.36) become $\left( c _ { 3 } = 1 \right)$

$$
\begin{array} { r l r } {  { \frac { 2 } { c _ { 2 } - c _ { 1 } } = \frac { 2 } { c _ { 1 } - 1 } + \sum _ { j = 1 } ^ { k } \frac { 1 } { c _ { 1 } - t _ { j } } , } } \\ & { } & { \frac { 2 } { c _ { 1 } - c _ { 2 } } = \frac { 2 } { c _ { 2 } - 1 } + \sum _ { j = 1 } ^ { k } \frac { 1 } { c _ { 2 } - t _ { j } } . } \end{array}
$$

These two equations can easily be solved for $c _ { 2 }$ and $c _ { 1 }$ respectively, and lead to $k \approx 3$ $k \approx 4$ $\binom { s + k - 1 } { k - 1 }$   
particles in equilibrium to prove their existence), but most of these lead to totally   
unstable and therefore useless methods (in the sense of Sect.II.3). Thus the only   
choice which we retain are the rightmost solutions $c _ { \imath }$ with $0 < c _ { 1 } , c _ { 2 } < 1$ , shown   
in Table 3.6 below. In addition, as Krylov has shown (see Krylov (1959), English   
translation 1962, p.329) this choice leads to the smallest error constant (for once,   
stability and small error are not in conflict!)

Stability of the Radau-Type Methods. The stability analysis of the Radau methods is done by inserting $y ^ { \prime } = \lambda y$ into (3.28). Since $c _ { s } = 1$ we have $y _ { n + 1 } = v _ { s }$ and thus obtain (for $s \simeq 3$ ） the characteristic equation

$$
\left( \begin{array} { c c c } { 1 - \mu b _ { 1 1 } } & { - \mu b _ { 1 2 } } & { - \mu b _ { 1 3 } } \\ { - \mu b _ { 2 1 } } & { 1 - \mu b _ { 2 2 } } & { - \mu b _ { 2 3 } } \\ { - \mu b _ { 3 1 } } & { - \mu b _ { 3 2 } } & { 1 - \mu b _ { 3 3 } } \end{array} \right) \left( \begin{array} { c } { v _ { 1 } } \\ { v _ { 2 } } \\ { \zeta ^ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right) \left( \begin{array} { c } { 1 } \\ { \zeta } \\ { \zeta ^ { 2 } } \end{array} \right) ,
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/7318b91f4cebfa39ca0df9b4a7d067f334882d827307d3cfdcc53db7f876f564.jpg)  
Fig.3.6. Solutions of (3.37). $\times$ unstable,口 stable

or

$$
\zeta ^ { 3 } = ( 0 , 0 , 1 ) \left( \begin{array} { c c c } { { 1 - \mu b _ { 1 1 } } } & { { - \mu b _ { 1 2 } } } & { { - \mu b _ { 1 3 } } } \\ { { - \mu b _ { 2 1 } } } & { { 1 - \mu b _ { 2 2 } } } & { { - \mu b _ { 2 3 } } } \\ { { - \mu b _ { 3 1 } } } & { { - \mu b _ { 3 2 } } } & { { 1 - \mu b _ { 3 3 } } } \end{array} \right) ^ { - 1 } \left( \begin{array} { c c c } { { a _ { 1 1 } } } & { { a _ { 1 2 } } } & { { a _ { 1 3 } } } \\ { { a _ { 2 1 } } } & { { a _ { 2 2 } } } & { { a _ { 2 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { a _ { 3 3 } } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { \zeta } } \\ { { \zeta ^ { 2 } } } \end{array} \right)
$$

which, when multiplied by $\operatorname* { d e t } ( I - \mu B )$ , becomes a polynomial of degree 3 in $\mu$ For a general multistep collocation method (3.28) we obtain in this way

$$
q _ { k } ( \mu ) \zeta ^ { k } + q _ { k - 1 } ( \mu ) \zeta ^ { k - 1 } + \ldots + q _ { 0 } ( \mu ) = 0
$$

where $q _ { k } ( \mu ) = \operatorname* { d e t } ( I - \mu B )$ and all $q _ { \imath } ( \mu )$ are polynomials of degree at most $s$

The root locus curves of Fig.3.7 were again obtained by Cardano's formula. Coefficients and stability measures are given in Table 3.6. The methods for $k = 1 , 2$ (orders $p = 5$ and 6) are $A$ -stable. The subsequent methods have surprisingly large $\alpha$ -values for very high orders (up to $p \approx 2 0$ )，which makes this class very promising.

# Exercises

1. Show that the coefficients $\nu _ { j }$ in (3.13) for the Enright methods can be com-puted recursively by

$$
\nu _ { j } = - \frac { 1 } { ( j + 1 ) ( \jmath + 2 ) } - \sum _ { k = 0 } ^ { j - 1 } \nu _ { k } S _ { j + 1 - k } \quad \mathrm { ~ w h e r e ~ } \quad S _ { l } = \sum _ { k = 1 } ^ { l } \frac { 1 } { k ( l + 1 - k ) } .
$$

Hint SeeteproEq.(7e $\textstyle G ( t ) = \sum _ { j = 0 } ^ { \infty } \nu _ { j } t ^ { j }$ becomes here $\begin{array} { r } { \int _ { 0 } ^ { 1 } ( s - 1 ) ( 1 - t ) ^ { 1 - s } d s } \end{array}$

Table 3.6. Coefficients and stability measuresfor multistep Radau methods $( s \approx 3$ ）  

<table><tr><td>k</td><td>p C1</td><td>C2</td><td>C3</td><td>8</td><td>D</td></tr><tr><td>1 2</td><td>5</td><td>0.1550510257216820.644948974278318</td><td>1.</td><td>90° 90°</td><td>0.000</td></tr><tr><td>6 3 7</td><td>0.177891722985607 0.192169638937766</td><td>0.673235257220651 0.689317969824851</td><td>1. 1.</td><td>89.73°</td><td>0.000 0.016</td></tr><tr><td>4</td><td>8 0.202814874040288</td><td>0.700407719104611</td><td>1.</td><td>89.13°</td><td>0.084</td></tr><tr><td>5</td><td>9 0.211395456069620</td><td>0.708798418188500</td><td>1.</td><td></td><td></td></tr><tr><td>6</td><td>0.218626151232186</td><td>0.715507419158199</td><td>1.</td><td>88.61°</td><td>0.178</td></tr><tr><td>7</td><td>10 11</td><td>0.721072684914921</td><td>1.</td><td>88.14°</td><td>0.278</td></tr><tr><td>8</td><td>0.224897548200883 12</td><td>0.725812172023161</td><td>1.</td><td>87.70°</td><td>0.376</td></tr><tr><td></td><td>0.230448266933707</td><td></td><td>1.</td><td>87.28°</td><td>0.467</td></tr><tr><td>9</td><td>13 0.235435607740434</td><td>0.729928926504599</td><td>1.</td><td>86.89°</td><td>0.555</td></tr><tr><td>10</td><td>14 0.239969169367303</td><td>0.733560240031675</td><td></td><td>86.51°</td><td>0.649</td></tr><tr><td>11</td><td>15 0.244128606044551</td><td>0.736803122952198</td><td>1.</td><td>86.14°</td><td>0.763</td></tr><tr><td>12</td><td>16 0.247973766491964</td><td>0.739728565298052</td><td>1.</td><td>85.79°</td><td>0.917</td></tr><tr><td>13</td><td>17 0.251550844436705</td><td>0.742390019356757</td><td>1.</td><td>85.44°</td><td>1.135</td></tr><tr><td>14</td><td>18 0.254896295040291</td><td>0.744828697795402</td><td>1.</td><td>85.07°</td><td>1.462</td></tr><tr><td>15</td><td>19 0.258039429919700</td><td>0.747077018862741</td><td>1.</td><td>84.68°</td><td>1.995</td></tr><tr><td>16</td><td>20 0.261004194709515（</td><td>0.749160923778290</td><td>1.</td><td>84.23°</td><td>3.037</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/1cb944dcbee95776780a2f2afb9871011fa220c63d6c69cca482f08f024f9696.jpg)  
Fig.3.7. Root locus curves for multistep Radau methods $( s \simeq 3 )$

2. The Enright Formulas are stiffly stable for $k \leq 7$ and are not stiffly stable, as one can easily inspect, e.g.by a computer plot, for $k = 8$ ， $k = 9 , \ldots$ and so on. Hence, everybody agrees that they are not stiffly stable for any $k > 7$ · However, no rigorous proof has been found for this,as for instance the proof of Theorem III.3.4. Why don't you try to find one?

3.Prove that the second derivative BDF methods (3.14) are unstable (in the sense of Sect. II.3) for $k > 1 1$ .

4. a) Show that for $k = 2$ ， $t _ { 1 } = - 1$ ， $t _ { 2 } = 0$ ， $s \approx 1$ ， $c _ { 1 } = - 1 / 2$ neither equations (3.24) nor equations (3.25) possess a solution.

b) Show that (3.24) and (3.25) always admit unique solutions if al $c _ { \iota }$ are distinct and satisfy $c _ { \imath } \geq 0$

Hint for $( b )$ .f $\varphi _ { \imath }$ (or $\psi _ { \imath } )$ are written as $\sum _ { l = 1 } ^ { s + k } a _ { l } t ^ { l - 1 }$ , then (3.24) and (3.25) become linear systems with the same matrix and different right-hand sides. The corresponding homogeneous system then possesses a non-zero solution iff the interpolation problem

$$
\begin{array} { r l } { p ( t _ { \jmath } ) = 0 } & { { } \quad \jmath = 1 , \dots , k } \\ { p ^ { \prime } ( c _ { \jmath } ) = 0 } & { { } \quad \jmath = 1 , \dots , s } \end{array}
$$

has a non-zero solution. Since $p ^ { \prime } ( t )$ has at most $k + s - 2$ real zeros and since (Rolle's theorem) each interval $( t _ { l } , t _ { l + 1 } )$ must contain at least one of these, there can be at most $s - 1$ zeros beyond $t _ { k } = 0$

5．A convenient way of computing the polynomials (3.24), (3.25) (written here for the case $s \approx 3$ ） is to put

$$
\varphi _ { \imath } ( t ) = ( a _ { 1 } + a _ { 2 } t + a _ { 3 } t ^ { 2 } + a _ { 4 } t ^ { 3 } ) \prod _ { l = 1 , \ l \neq \imath } ^ { k } ( t - t _ { l } ) .
$$

Show that Eqs.(3.24) (for $i = j$ ） and (3.25) then become the following linear system

$$
\begin{array} { r } { a _ { 1 } + t _ { \ i } a _ { 2 } + t _ { \ i } ^ { 2 } a _ { 3 } + t _ { \ i } ^ { 3 } a _ { 4 } = 1 / r _ { \ i } , \qquad ( 3 . 4 1 ) \times ( 3 . 4 1 ) } \\ { s _ { \ j } a _ { 1 } + ( s _ { \ j } c _ { \ j } + 1 ) a _ { 2 } + ( s _ { \ j } c _ { \ j } ^ { 2 } + 2 c _ { \ j } ) a _ { 3 } + ( s _ { \ j } c _ { \ j } ^ { 3 } + 3 c _ { \ j } ^ { 2 } ) a _ { 4 } = 0 , \qquad j = 1 , 2 , 3 } \end{array}
$$

$$
r _ { \imath } = \prod _ { l = 1 , \ l \neq \imath } ^ { k } ( t _ { \imath } - t _ { l } ) , \quad s _ { \jmath } = \sum _ { l = 1 , \ l \neq \imath } ^ { k } \frac { 1 } { c _ { \jmath } - t _ { l } } .
$$

$$
\psi _ { \imath } ( t ) = ( a _ { 1 } + a _ { 2 } t + a _ { 3 } t ^ { 2 } ) \prod _ { l = 1 } ^ { k } ( t - t _ { l } )
$$

Eq.(3.25) becomes

$$
s _ { j } a _ { 1 } + ( s _ { j } c _ { j } + 1 ) a _ { 2 } + ( s _ { j } c _ { j } ^ { 2 } + 2 c _ { j } ) a _ { 3 } = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } j \neq i } \\ { 1 / r _ { i } } & { { \mathrm { i f ~ } } j = i } \end{array} \right. } \qquad j = 1 , 2 , 3
$$

where $r _ { \imath } = \prod _ { l = 1 } ^ { k } ( c _ { \imath } - t _ { l } ) , \quad s _ { \jmath } = \sum _ { l = 1 } ^ { k } \frac { 1 } { c _ { \jmath } - t _ { l } } .$

6. Generalize the proof and the result of Theorem IV.3.10 to multistep collocation methods.

Hint. Instead of $K M ( x )$ in (IV.3.26) we have to insert a linear combination $\textstyle \sum _ { \ell = 1 } ^ { k } \alpha _ { \ell } M _ { \ell } ( x )$ where $M _ { \ell } ( x ) = M ( x ) \cdot x ^ { \ell - 1 }$ ， $\begin{array} { r } { M ( x ) = \frac { 1 } { s ! } \prod _ { i = 1 } ^ { s } ( x - c _ { * } ) } \end{array}$ and $\alpha _ { 1 } , \ldots , \alpha _ { k }$ are arbitrary. Instead of (IV.3.27) we then obtain

$$
u ( x ) = \sum _ { \ell = 1 } ^ { k } \alpha _ { \ell } \sum _ { j = 0 } ^ { s } \frac { M _ { \ell } ^ { ( j ) } ( x ) } { \mu ^ { j } } .
$$

Putting $x = t _ { 1 } , t _ { 2 } , \ldots , t _ { k } , t _ { k + 1 }$ and $u ( t _ { i } ) = y _ { i }$ gives an overdetermined system for $\alpha _ { 1 } , \ldots , \alpha _ { k }$ which has a solution only if a certain determinant is zero. Seting $y _ { 1 } = 1$ ， $y _ { 2 } = \zeta$ ， $y _ { 3 } = \zeta ^ { 2 } , \ldots$ ，there leads to the characteristic equation

$$
\begin{array} { r l } & { \operatorname* { d e t } \left( \begin{array} { c c c c c } { \sum _ { j = 0 } ^ { s } M _ { 1 } ^ { ( j ) } ( t _ { 1 } ) \mu ^ { s - j } } & { \dots } & { \sum _ { j = 0 } ^ { s } M _ { k } ^ { ( j ) } ( t _ { 1 } ) \mu ^ { s - j } } & { 1 } \\ { \sum _ { j = 0 } ^ { s } M _ { 1 } ^ { ( j ) } ( t _ { 2 } ) \mu ^ { s - j } } & { \dots } & { \sum _ { j = 0 } ^ { s } M _ { k } ^ { ( j ) } ( t _ { 2 } ) \mu ^ { s - j } } & { \zeta } \\ { \vdots } & { } & { } & { \vdots } & { \vdots } \\ { \sum _ { j = 0 } ^ { s } M _ { 1 } ^ { ( j ) } ( t _ { k + 1 } ) \mu ^ { s - j } } & { \dots } & { \sum _ { j = 0 } ^ { s } M _ { k } ^ { ( j ) } ( t _ { k + 1 } ) \mu ^ { s - j } } & { \zeta ^ { k } } \end{array} \right) } \end{array}
$$

as a generalization of (IV.3.22,23). Tedious expansions of this determinant into powers of $\zeta$ and $\mu$ (with many coefficients equal to zero) then leads to an explicit expression (see Theorem 7 of Lie 1990).

7. Prove that the 2-step 2-stage collocation method with $c _ { 2 } = 1$ is $A$ -stable iff

$$
c _ { 1 } \geq ( { \sqrt { 1 7 } } - 1 ) / 8 .
$$

Hint. a) Show that the characteristic equation is $q _ { 2 } ( \mu ) \zeta ^ { 2 } + q _ { 1 } ( \mu ) \zeta + q _ { 0 } ( \mu ) = 0$ ， where

$$
\begin{array} { r l } & { q _ { 2 } ( \mu ) = - ( 9 c _ { 1 } + 5 ) + \mu ( 3 c _ { 1 } ^ { 2 } + 7 c _ { 1 } + 2 ) - \mu ^ { 2 } 2 c _ { 1 } ( c _ { 1 } + 1 ) } \\ & { q _ { 1 } ( \mu ) = 1 2 c _ { 1 } + 4 - \mu 4 ( c _ { 1 } ^ { 2 } - 1 ) } \\ & { q _ { 0 } ( \mu ) = - 3 c _ { 1 } + 1 + \mu c _ { 1 } ( c _ { 1 } - 1 ) . } \end{array}
$$

b)Apply Schur's criterion (1918) to the polynomial (3.44) with $\mu = i t , t \in \mathbb { R }$

Schur's criterion. Let $a ( \zeta ) = a _ { k } \zeta ^ { k } + a _ { k - 1 } \zeta ^ { k - 1 } + . ~ . . + a _ { 0 }$ $\left( a _ { k } \neq 0 \right)$ be a polynomial with complex coefficients and set

$$
a ^ { * } ( \zeta ) = \overline { { a } } _ { 0 } \zeta ^ { k } + \overline { { a } } _ { 1 } \zeta ^ { k - 1 } + . . . + \overline { { a } } _ { k } .
$$

Then, all zeros of $a ( \zeta )$ lie inside the unit circle,iff

i) $| a _ { 0 } | < | a _ { k } |$   
ii) the zeros of $\zeta ^ { - 1 } ( a ^ { * } ( 0 ) a ( \zeta ) - a ( 0 ) a ^ { * } ( \zeta ) )$ , a polynomial of degree $k - 1$ ， are all inside the unit circle.

8. Prove that $c _ { 1 } = ( \sqrt { 1 7 } - 1 ) / 8$ is a super-convergence point for the 2-step 2-stage collocation methods with $c _ { 2 } = 1$

# V.4 Order Stars on Riemann Surfaces

Riemann ist der Mann der glänzenden Intuition. Durch seine umfassende Genialitat überragt er alle seine Zeitgenossen ... Im Auftreten schiuchtern, ja ungeschickt, musste sich der junge Dozent, zu dem wir Nachgeborenen wie zu einem Heiligen aufblicken,mancherlei Neckereien von seinen Kollegen gefallen lassen.

(F. Klein,Entwicklung der Mathematik im 19. Jhd., p.246,247)

We have seen in the foregoing sections that the highest possible order of $A$ -stable linear multistep methods is two; furthermore, the second derivative Enright methods as well as the SDBDF methods were seen to be $A$ -stable for $p \leq 4$ ; the three-stage Radau multistep methods were $A$ -stable for $p \leq 6$ . In this section we shall see that these observations are special cases of a general principle, the so-called “Daniel-Moore conjecture”which says that the order of an $A$ -stable multistep method involving either s derivatives or $s$ implicit stages satisfies $p \leq 2 s$ . Before proceeding to its proof, we should become familiar with Riemann surfaces.

# Riemann Surfaces

Fir manche Untersuchungen, namentlich fir die Untersuchung algebraischer und Abel'scher Functionen ist es vortheilhaft，die Verzweigungsart einer mehrwerthigen Function in folgender Weise geometrisch darzustellen. Man denke sich in der $( x , y )$ -Ebene eine andere mit ihr zusammenfallende Fläche (oder auf der Ebene einen unendlich dinen Körper) ausgebreitet,welche sich so weit und nur so weit erstreckt, als die Function gegeben ist. Bei Fortsetzung dieser Function wird also diese Fläche ebenfalls weiter ausgedehnt werden. In einem Theile der Ebene,fiir welchen zwei oder mehrere Fortsetzungen der Function vorhanden sind,wird die Fläche doppelt oder mehrfach sein; sie wird dort aus zwei oder mehreren Blättern bestehen, deren jedes einen Zweig der Function vertritt. Um einen Verzweigungspunkt der Function herum wird sich ein Blatt der Fläche in ein anderes fortsetzen, so dass in der Umgebung eines solchen Punktes die Fläche als eine Schraubenfläche mit einer in diesem Punkte auf der $( x , y )$ Ebene senkrechten Axe und unendlich kleiner Hohe des Schraubenganges betrachtet werden kann. Wenn die Function nach mehreren Umläufen des $z$ um den Verzweigungswerth ihren vorigen Werth wieder erhalt (wie z.B. $( z - a ) ^ { m / n }$ ，wenn $m , n$ relative Primzahlen sind, nach $\pmb { n }$ Umlaufen von $z$ ${ \mathrm { u m ~ } } a { \mathrm { ~ } }$ ),muss man dann freilich annehmen,dass sich das oberste Blatt der Fläche durch die üibrigen hindurch in das unterste fortsetzt.

Die mehrwerthige Function hat fuir jeden Punkt einer solchen ihre Verzwei-gungsart darstellenden Fläche nur einen bestimmten Werth und kann daher als eine vollig bestimmte Function des Orts in dieser Flache angesehen werden. (B.Riemann 1857)

We take as example the BDF method $( \mathrm { I I I } . 1 . 2 2 ^ { 9 } )$ for $k = 2$ which has the characteristic equation

$$
{ \Big ( } { \frac { 3 } { 2 } } - \mu { \Big ) } \zeta ^ { 2 } - 2 \zeta + { \frac { 1 } { 2 } } = 0 .
$$

This quadratic equation expresses $\zeta$ as a function of $\mu$ , both are complex variables. It is immediately solved to yield

$$
\zeta _ { 1 , 2 } = \frac { 2 \pm \sqrt { 1 + 2 \mu } } { 3 - 2 \mu }
$$

which defines a two-valued function,i.e., to each $\mu \in \mathbb { C }$ we have two solutions $\zeta$ These two solutions are displayed in Fig.4.1 (we have plotted the level curves of $| \zeta _ { 1 , 2 } ( \mu ) |$ ; the region with $\left| \zeta _ { 1 } ( \mu ) \right| > 1$ is in white).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/164bf061b371f0121a7dfc34e2a6057cf6e6811cbb6f682c3708ba1d2bc3d4e6.jpg)  
Fig. 4.1. The two solutions of the BDF2 characteristic equation

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/163f2ed757612ce3cd26430e832f81d5be6678404ca171474fd2450a76df3c16.jpg)  
Fig. 4.2. Three dimensional view of the map (4.4)

We observe two essential facts. First, there is a pole of $\zeta _ { 1 }$ , but not of $\zeta _ { 2 }$ ,at the point $\mu = 3 / 2$ . This is due to the factor $( 3 / 2 - \mu )$ in (4.1） which represents the implicit stage of the method. Second,we observe a curious discontinuity on the negative real axis left of the point $- 1 / 2$ , a phenomenon first observed in a famous paper of Puiseux (185O)("... a encore cet inconvénient, que $u$ devient alors une fonction discontinue ..."). It has its reason in the complex square root $\sqrt { 1 + 2 \mu }$ which,while $1 + 2 \mu$ performs a revolution around the origin,only does half a revolution and exchanges the two roots. We cannot therefore speak in a natural way of the two complex functions $\zeta _ { 1 } ( \mu )$ and $\zeta _ { 2 } ( \mu )$ . And here comes the great idea of Riemann (1857): Instead of varying $\mu$ in the complex plane $\mathbb { C }$ ， we imagine it varying in a double sheet of (in Riemann's words: infinitely close) complex planes $\mathbb { C } \cup \mathbb { C }$ . The $\mu ^ { \prime } s$ in the upper sheet are mapped to $\zeta _ { 1 }$ ，the $\mu ^ { \prime } s$ in the lower sheet are mapped to $\zeta _ { 2 }$ . The double-valued function then becomes single-valued. At the "cut",left of the point $- 1 / 2$ , the two roots $\zeta _ { 1 }$ and $\zeta _ { 2 }$ are interchanged, so we must imagine that the upper sheet for $\zeta _ { 1 }$ continues into the lower sheet for $\zeta _ { 2 }$ (shaded in Fig.4.1) and vice-versa. If we denote the manifold obtained in this way by $M$ ， then the map

$$
\left\{ \begin{array} { l l } { M \longrightarrow \mathbb { C } } \\ { \mu \longmapsto \zeta } \end{array} \right.
$$

becomes an everywhere continuous and holomorphic map (with the exception of the pole). $M$ is then called the Riemann surface of the algebraic function $\mu \mapsto \zeta$

A three-dimensional view of the map

$$
\left\{ \begin{array} { l l } { M \longrightarrow \mathbb { R } } \\ { \mu \longmapsto | \zeta | } \end{array} \right.
$$

is represented in Fig.4.2.

More General Methods. Most methods of Sect. V.3 are so-called multistep Runge-Kutta methods defined by the formulas

$$
\begin{array} { l } { { \displaystyle y _ { n + k } = \sum _ { j = 1 } ^ { k } a _ { j } y _ { n + j - 1 } + h \sum _ { j = 1 } ^ { s } b _ { j } f ( x _ { n } + c _ { j } h , v _ { j } ^ { ( n ) } ) } } \\ { { \displaystyle v _ { \imath } ^ { ( n ) } = \sum _ { j = 1 } ^ { k } \widetilde a _ { \imath _ { j } } y _ { n + j - 1 } + h \sum _ { j = 1 } ^ { s } \widetilde b _ { \imath _ { j } } f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ^ { ( n ) } ) } . } \end{array}
$$

This is the subclass of general linear methods (Example III.8.5) for which the external stages represent the solution $y ( x )$ on an equidistant grid. The bulk of numerical work for applying the above method are the implicit stages (4.5b).

For the stability analysis we set as now usual $f ( x , y ) = \lambda y$ ， $h \lambda = \mu$ and $( y _ { n } , y _ { n + 1 } , \dots , y _ { n + k } ) = ( 1 , \zeta , \dots , \zeta ^ { k } )$ . Equation (4.5b) then becomes in vector notation (using $\vec { \zeta } = ( 1 , \zeta , \dots , \zeta ^ { k - 1 } ) ^ { T } )$

$$
\begin{array} { r } { \vec { v } = \left( I - \mu \widetilde { B } \right) ^ { - 1 } \widetilde { A } \vec { \zeta } , } \end{array}
$$

which is rational in $\mu$ with denominator $\operatorname* { d e t } ( I - \mu { \tilde { B } } )$ . Inserting this into (4.5a) and multiplying with this denominator we obtain a characteristic equation of the form

$$
Q ( \mu , \zeta ) \equiv q _ { k } ( \mu ) \zeta ^ { k } + q _ { k - 1 } ( \mu ) \zeta ^ { k - 1 } + . . . + q _ { 0 } ( \mu ) = 0
$$

where $q _ { k } ( \mu ) = \operatorname* { d e t } ( I - \mu \widetilde { B } )$ and all $q _ { j } \{ \mu \}$ are polynomials in $\mu$ of degree $\leq s$

Multiderivative multistep methods, on the other hand, may be written as (M. Reimer 1967,R. Jeltsch 1976)

$$
\sum _ { j = 0 } ^ { s } h ^ { j } \sum _ { i = 0 } ^ { k } \alpha _ { i j } D ^ { j } y _ { n + i } = 0
$$

where the computation of higher derivatives $D ^ { j } y$ is done by Eq.(II.12.3). For the equation $y ^ { \prime } = \lambda y$ we have $D ^ { j } y = \lambda ^ { j } y$ and inserting this into (4.8) together with $( y _ { n } , y _ { n + 1 } , . . . , y _ { n + k } ) = ( 1 , \zeta , . . . , \zeta ^ { k } )$ we obtain at once a characteristic equation of the form (4.7). Here,the degree s of the polynomials $\varphi _ { j } \mathopen { } \mathclose \bgroup \left( \mu \aftergroup \egroup \right)$ is equal to the order of the highest derivative taken. The bulk of numerical work for evaluating (4.8) is the determination of $y _ { n + k }$ from an implicit equation containing $y _ { n + k }$ ， $D y _ { n + k } , \ldots , D ^ { s } y _ { n + k }$ . If the last of these derivatives is present (i.e., if $\alpha _ { k s } \neq 0$ then the degree of $q _ { k } \mathopen { } \mathclose \bgroup \left( \mu \aftergroup \egroup \right)$ in (4.7) will be s .

The Riemann surface $M$ of (4.7) will consist of $k$ sheets, one for each of the $k$ roots $\zeta _ { j }$ . The branch points are values of $\mu$ for which two or several roots of (4.7) coalesce to an $m$ -fold root. These are the roots of a certain “discriminant” (see any classical book on Algebra, e.g., the famous“Weber", Vol. I, $\ S$ 50); hence for irreducible $Q ( \mu , \zeta )$ there are only a finite number of such points. The movement of the coalescing roots $\zeta _ { j }$ ，when $\mu$ surrounds such a branch point, has been carefully studied by Puiseux: They usually form what Puiseux calls a “systeme circulaire”, i.e., they are cyclically permuted at each revolution like the values of the complex function $\sqrt [ m ] { z }$ near the origin. The Riemann surface must then follow these “monodromies” and must be cut along certain lines and rejoined appropriately. The location of these cuts is not unique.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/5d8582ed278b17bfdc6a1d7fd71d873c9dafbd0e3d7a872310de7200bb7abebc.jpg)  
Fig.4.3. Different cuts for (4.9) (Hurwitz & Courant 1925)

Different possibilities for cuting the Riemann surface of,say, the function

$$
\zeta ^ { 2 } - \left( 1 - \mu ^ { 4 } \right) = 0
$$

with branch points at $\pm 1$ and $\pm i$ , are shown in a classical figure reproduced from the book of Hurwitz & Courant, second edition 1925, p. 360 (Fig. 4.3).

# Poles Representing Numerical Work

Only 85 miles (geog.） from the Pole, but it's going to be a stiff pull both ways apparently; still we do make progress,which is something. (R.F. Scott, January 10,1912; first mention of interrelation between poles and stiffness in the literature)

We have just seen that the degree $s$ of $q _ { k } ( \mu )$ in (4.7) expresses the numerical work (either the number of implicit stages or the number of derivatives for the implicit solution). Now $q _ { k } ( \mu )$ will possess $s$ zeros $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { s }$ . What happens if $\mu$ approaches one of these zeros? The polynomial (4.7) of degree $k$ （with $k$ roots $\zeta _ { 1 } ( \mu ) , \ldots , \zeta _ { k } ( \mu ) )$ suddenly becomes a polynomial of degree $k - 1$ with only $k \sim 1$ roots.Where does the last one go? Well, by Vieta's Theorem, it must go to infinity. In order to compute its asymptotic behaviour, suppose $q _ { k } ( \mu _ { 0 } ) = 0$ ， $q _ { k } ^ { \prime } ( \mu _ { 0 } ) \neq 0$ ， $q _ { k - 1 } ( \mu _ { 0 } ) \neq 0$ and that $\zeta$ is large. Then all terms $q _ { k - 2 } ( \mu ) \zeta ^ { k - 2 } , \dots ,$ $q _ { 0 } ( \mu )$ are dominated by $q _ { k - 1 } ( \mu ) \zeta ^ { k - 1 }$ and may be neglected. It results that

$$
\zeta \sim - \frac { q _ { k - 1 } ( \mu _ { 0 } ) } { q _ { k } ^ { \prime } ( \mu _ { 0 } ) } \frac { 1 } { \mu - \mu _ { 0 } } \quad \mathrm { ~ a s ~ } \quad \mu \to \mu _ { 0 } ,
$$

hence the algebraic function $\zeta ( \mu )$ possesses a pole on one of its sheets. If $q _ { k } ( \mu _ { 0 } ) =$ O is a multiple root, the corresponding pole willbe multiple too.

It is also possible that the pole in question coincides with a branch point. This happens when in addition to $q _ { k } ( \mu _ { 0 } ) = 0$ also $q _ { k - 1 } ( \mu _ { 0 } ) = 0$ . In this case two roots $\zeta _ { \jmath } ( \mu )$ tend to infinity,but more slowly, like $\pm C ( \mu - \mu _ { 0 } ) ^ { - 1 / 2 }$ (Exercise 1). We therefore count both “half-poles” together as one pole again. If $c$ is a boundary curve of a neighbourhood $V$ of $\mu _ { 0 }$ (which around this branch point surrounds $\mu _ { 0 }$ twice before closing up), the argument of $\zeta ( \mu )$ makes just one clockwise revolution on this path. Fig. 4.4 illustrates this fact with an example.

Recapitulating we may state:

Lemma 4.1. The Riemann surface for the characteristic equation of a multistep Runge-Kuta method with $s$ implicit stages per step (or a multiderivative multistep method with s implicit derivative evaluations) includes at most s poles of the algebraic function $\zeta ( \mu )$ □

We shall see below that Lemma 4.1 remains true for the whole class of general linear methods,but for the moment we are “impatient et joyeux d'aller au combat”

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/fd47a350eee6cc54f45cd8eef80dbb954730d35f568f64f1cbd2bfc2b2ad71b8.jpg)  
Fig. 4.4. Behaviour of roots of $\mu \zeta ^ { 2 } + 2 \mu \zeta + 2 - \mu = 0$ near the origin $\mu = 0$

(Astérix Legionnaire, pp. 29 and 30). The argument principle also remains valid on Riemann surfaces and we state it as follows:

“On the left,isn't it ?”-“Right.” “On the right ?”-“Left, leeeft!"” (John Cleese in “Clockwise")

Lemma 4.2. Suppose that a domain $F \subset M$ contains no zeros of $\zeta ( \mu )$ and that its boundary consists of closed loops $\gamma _ { 1 } , \ldots , \gamma _ { \ell }$ . Then the number of poles of $\zeta ( \mu )$ contained in $F$ is equal to the total number of clockwise revolutions of $\mathsf { a r g } ( \zeta ( \mu ) )$ along $\gamma _ { 1 } , \ldots , \gamma _ { \ell }$ , each passed through in that direction which leaves $\boldsymbol { F }$ to the left of $\gamma _ { \jmath }$

The proof is by cutting $\boldsymbol { F }$ into thousand pieces, each of which is homeomorphic to a disc in $\mathbb { C }$ , and by adding up all revolution numbers which cancel along the cuts, because the adjacent edges are traversed in opposite directions. □

# Order and Order Stars

... denn das Klare und leicht Falliche zieht uns an, das Verwickelte schreckt uns ab. (D. Hilbert, Paris 1900)

Guided by the ideas of Sect.IV.4, we now compare the absolute values of the characteristic roots $| \zeta _ { 1 } |$ and $| \zeta _ { 2 } |$ for the BDF2 scheme (4.2) with the exponential function $\vert e ^ { \mu } \vert = e ^ { \mathrm { R e } \mu }$ ,hence we define (Wanner, Hairer & Ngrsett 1978)

$$
A _ { \ j } = \left\{ \mu \in \mathbb { C } \ ; \ | \zeta _ { \ j } ( \mu ) | > | e ^ { \mu } | \right\} \qquad j = 1 , 2 .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/6c9fe4ef3bb0060a98be57cc3cbe5f309914ffe2122eef77dad6ce65aaa8d0f4.jpg)  
Fig.4.5. The order star (4.14) for BDF2

These sets, on precisely the same scale as in Fig.4.1,are represented in Fig.4.5.

The sets $A _ { \ j }$ continue across the cuts in the same way as do the roots, it is therefore natural to embed them into the Riemann surface $M$ and define

$$
A = \left\{ \mu \in M ; | \zeta ( \mu ) | > | e ^ { \pi ( \mu ) } | \right\}
$$

where $\pi : \mathcal { M }  \mathbb { C }$ is the natural projection.

Fig.4.5 shows clearly an order star with three sectors for $\zeta _ { 1 } ( \mu )$ ,but none for $\zeta _ { 2 } ( \mu )$ , and we guess that this has to do with the order of the method, which is two. Lemma 4.3 below will extend Lemma IV.4.3 to multistep methods.

By putting $h \approx 0$ in (4.5) (hence $\mu = 0$ in (4.7)), and

$$
( y _ { n } , y _ { n + 1 } , \dots , y _ { n + k - 1 } ) = ( 1 , 1 , \dots , 1 )
$$

(hence $\zeta = 1$ in (4.7)), we must have by consistency that $y _ { n + k } = 1$ too,i.e., that $Q ( 0 , 1 ) = 0$ . This corresponds to the formula $\varrho ( 1 ) = 0$ in the multistep case (see (II.2.6)). But for $h \approx 0$ the difference equation (4.5a) is stable only if $\zeta = 1$ is a simple root of the polynomial equation $Q ( 0 , \zeta ) = 0$ . Hence we must have

$$
Q ( 0 , 1 ) = 0 , \qquad { \frac { \partial Q } { \partial \zeta } } \left( 0 , 1 \right) \neq 0 .
$$

The analytic continuation $\zeta _ { 1 } ( \mu )$ of this root in the neighbourhood of the origin (as far as it is not embarassed with branch points) will be called the principal root, the corresponding surface the principal sheet of $M$

Lemma 4.3. For stable multistep Runge-Kutta (or multiderivative) methods of order $p$ the set $A$ possesses a star of $p + 1$ sectors on the principal sheet in the neighbourhood of the origin.

Proof. We fix $\lambda \in \mathbb { C }$ ,set $y ^ { \prime } = \lambda y$ and take for $y _ { 0 } , \ldots , y _ { k - 1 }$ exact initial values $1 , e ^ { \mu } , \ldots , e ^ { ( k - 1 ) \mu }$ . The order of the method then tells us that the local error (see Fig. II.2.1),i.e., the difference between $e ^ { k \mu }$ and the numerical solution $y _ { k }$ com-puted from (4.5a), must be $\widetilde { C } \cdot h ^ { p + 1 }$ for $h  0$ , hence $\widetilde { C } \lambda ^ { - p - 1 } \mu ^ { p + 1 }$ for $\mu \to 0$

Thus, Formula (4.5) with all $y _ { \jmath }$ replaced by $e ^ { \ j \mu }$ will lead to

$$
Q ( \mu , e ^ { \mu } ) = \overline { { { C } } } \mu ^ { p + 1 } + \mathcal { O } ( \mu ^ { p + 2 } ) .
$$

We subtract (4.14) from (4.7), choose for $\zeta ( \mu )$ the principal root $\zeta _ { 1 } ( \mu )$ (for which $e ^ { \mu } - \zeta _ { 1 } ( \mu )$ is small for $| \mu |$ small) and linearize. This gives

$$
\frac { \partial Q } { \partial \zeta } \left( 0 , 1 \right) \cdot \left( e ^ { \mu } - \zeta _ { 1 } ( \mu ) \right) = \overline { { { C } } } \mu ^ { p + 1 } + \ldots .
$$

and by dividing through by the non-zero constant (4.13)

$$
e ^ { \mu } - \zeta _ { 1 } ( \mu ) = C \cdot \mu ^ { p + 1 } + { \mathcal O } ( \mu ^ { p + 2 } ) \qquad { \mathrm { f o r } } \qquad \mu \to 0 .
$$

The rest of the proof now goes exactly analogously to that of Lemma IV.4.3. There is also not much difference in the case of multiderivative methods. □

The constant $C$ of (4.15） is called the error constant of the method. This is consistent with Formula (II.2.6) and (II.2.13) for multistep methods and with (IV.3.5) for Runge-Kutta methods.

The stability domain of multistep Runge-Kutta methods as well as their $A$ stability is defined in the same way as for multistep methods (see Definition 1.1). One has only to interpret $\zeta _ { 1 } ( \mu ) , \ldots , \zeta _ { k } ( \mu )$ as the roots of (4.7).

# The “Daniel and Moore Conjecture'

It is conjectured here that no $A$ -stable method of the form of Eq. 5-6 can be of order greater than $2 J + 2$ and that, of those $A$ -stable methods of order $2 J + 2$ , the smallest error constant is exhibited by the Hermite method ...

(Daniel& M00re 1970, p. 80)

At the time when no simple proof for Dahlquist's second barrier was known, a proof of its generalization, the Daniel & Moore conjecture, seemed quite hopeless. Y. Genin (1974) constructed $A$ -stable multistep multiderivative methods with astonishingly high “order” contradicting the conjecture. R. Jeltsch (1976) later cleared up the mystery by showing that Genin's methods had 1 as multiple root of $\varrho ( \zeta )$ and hence the “effective” order was lower. The conjecture was finally proved in 1978 with the help of order stars:

Theorem 4.4. The highest order of an $A$ -stable s-stage Runge-Kutta (or s - derivative) multistep method is 2s. For the $A$ -stable methods of order $2 s$ the error constant satisfies

$$
( - 1 ) ^ { s } C \geq { \frac { s ! s ! } { ( 2 s ) ! ( 2 s + 1 ) ! } } .
$$

Proof.By $A$ -stability, we have for all roots $| \zeta _ { j } ( i y ) | \le 1$ along the imaginary axis; hence the order star $A$ is nowhere allowed to cross the imaginary axis. We consider $A ^ { + } = A \cap \pi ^ { - 1 } ( \mathbb { C } ^ { + } )$ , the part of the order star which lies above $\mathbb { C } ^ { + }$ . As in Lemma IV.4.4, $A ^ { + }$ must be finite on all sheets of $M$ . The boundary of $A ^ { + }$ may consist of several closed curves. As in Lemma IV.4.5, the argument of $\zeta ( \mu ) / e ^ { \mu }$ is steadily increasing along $\partial A ^ { + }$ . Since at the origin we have a star with $p + 1$ sectors (Lemma 4.3), of which at least $[ { \frac { p + 1 } { 2 } } ]$ lie in $\mathbb { C } ^ { + }$ ， the boundary curves of $A ^ { + }$ must visit the origin at least $\textstyle { \left[ { \frac { p + 1 } { 2 } } \right] }$ times. Hence the total rotation number is at least $[ { \frac { p + 1 } { 2 } } ]$ and from Lemmas 4.1 and 4.2 we conclude that

$$
\Big [ \frac { p + 1 } { 2 } \Big ] \leq s .
$$

This implies that $p \leq 2 s$ and the first assertion is proved.

We now need a new idea for the part concerning the error constant. The following reasoning will help: the star $A$ ex-presses the fact that the surface $| \zeta ( \mu ) / e ^ { \mu } \}$ goes up and down around the origin like Montaigne's ruff. There, the error con-stant has to do with the height of these waves. So if we want to compare different error constants we must compare $| \zeta ( \mu ) / e ^ { \mu } \}$ to $| R ( \mu ) / e ^ { \mu } |$ ，where $R ( \mu )$ is the characteristic function of a second method. By dividing the two expressions, $e ^ { \mu }$ cancels and we define

$$
B = \bigg \{ \mu \in M ; \bigg \vert { \frac { \zeta ( \mu ) } { R ( \pi ( \mu ) ) } } \bigg \vert > 1 \bigg \} ,
$$

called the relative order star. For $R ( z )$ we choose the diagonal Padé approximation $R _ { s s } ( z )$ with $s$ zeros and $s$ poles (see (IV.3.30)). By subtracting (IV.3.31) (with $j = k = s$ ） from (4.15) (where it is now supposed that $p = 2 s$ ） we obtain

$$
R _ { s s } ( \mu ) - \zeta _ { 1 } ( \mu ) = \underbrace { \left( C - ( - 1 ) ^ { s } \frac { s ! s ! } { ( 2 s ) ! ( 2 s + 1 ) ! } \right) } _ { \widetilde { C } } \mu ^ { 2 s + 1 } + \cdot \cdot \cdot
$$

It is known that $| R _ { s s } ( i y ) | = 1$ for all $y \in \mathbb { R }$ and that all zeros of $R _ { s s } ( z )$ lie in $\mathbb { C } ^ { - }$ (Theorem IV.4.12). Therefore the set $B$ in (4.18) cannot cross the imaginary axis (as before) and the quotient $\vert \zeta ( \mu ) / R ( \pi ( \mu ) ) \vert$ has no other poles above $\mathbb { C } ^ { + }$ than those of $\zeta ( \mu )$ , of which, we know, there are at most $s$ . Therefore the sectors of the relative order star $B$ must exhibit the same colours as those of the classical order star $A$ for diagonal Padé (see Fig.IV.4.2). Otherwise an extra pole would be needed. We conclude that the error constants must have the same sign (see Lemma IV.4.3), hence (see IV.3.31) $( - 1 ) ^ { s } \widetilde { C } > 0$ , which leads to (4.16).

Equality $\widetilde { C } = 0$ would produce an order star $B$ of even higher order which is impossible with $s$ poles,unless the two methods are identical. □

Remarks. a) The first half is in fact superfluous, since the inequality (4.16) implies that the $2 s$ -th order error constant $C \neq 0$ , hence necessarily $p \leq 2 s$ . It has been retained for its beauty and simplicity,and for readers who do not want to study the second half.

b) The proof never uses the full hypothesis of $A$ -stability; the only property used is stability on the imaginary axis ( $I$ -stability, see (IV.3.6)). Thus Theorem 4.4 allows the following sharpening, which then extends Theorem IV.4.7 to multistep methods:

Theorem 4.5. Suppose that an $I$ -stable $s$ -stage Runge-Kutta (or $s$ -derivative) multistep method possesses a characteristic function $\zeta ( \mu )$ with $s _ { 1 }$ poles in $\mathbb { C } ^ { + }$ Then

$$
p \leq 2 s _ { 1 }
$$

and the error constant for all such $I$ -stable methods of order $p = 2 s _ { 1 }$ satisfies

$$
( - 1 ) ^ { s _ { 1 } } C \geq { \frac { s _ { 1 } ! s _ { 1 } ! } { ( 2 s _ { 1 } ) ! ( 2 s _ { 1 } + 1 ) ! } } .
$$

Another interpretation of this theorem is the following result (compare with Theorem IV.4.8), which in the case $s \approx 1$ is due to R. Jeltsch (1978).

Thorem 4.6. Suppose that an $I$ -stable method with $s$ poles satisfies $p \geq 2 s - 1$ Then it is $A$ -stable.

Proof. If only $s - 1$ poles were in $\mathbb { C } ^ { + }$ ,we would have $p \leq 2 s - 2$ , a contradiction. Hence all poles of $\zeta ( \mu )$ are in $\mathbb { C } ^ { + }$ and $A$ -stability follows from the maximum principle. □

# Methods with Property $C$

It is now tempting to extend the proof of Theorem 4.4 to any method other than the diagonal Padé method. But this meets with an essential difculty in defining (4.18) if $R ( \mu )$ is a multistep method defined on another Riemann surface, since then the definition of $B$ makes no sense. The following observation will help: The second part of the proof of Theorem 4.4 only took place in $\mathbb { C } ^ { + }$ ，which was the instability domain of the “comparison method". This leads to

Definition 4.7 (Jeltsch & Nevanlinna 1982). Let a method be given with characteristic polynomial (4.7) satisfying (4.13) and denote its stability domain by $S _ { R }$ · We say that this method has Property $C$ if the principal sheet includes no branch points outside of $\pi ^ { - 1 } ( S _ { R } )$ (with $\infty$ included if $S _ { R }$ is bounded),and the principal root $R _ { 1 } ( \mu )$ produces the whole instability of the method,i.e.,

$$
\Delta _ { R } : = \partial S _ { R } = \big \{ \mu \in \mathbb { C } \mathrm { ; ~ } | R _ { 1 } ( \mu ) | = 1 \big \} \mathrm { . }
$$

Examples. All one-step methods have Property $C$ , of course. Linear multistep methods whose root locus curve is simply closed have Property $C$ too. In this situation all roots except $R _ { 1 } ( \mu )$ have modulus smaller than one for all $\mu \not \in \pi ^ { - 1 } ( S _ { R } )$ Thus the principal sheet cannot have a branch point there. The explicit 4th order Adams method analyzed in Fig. 1.1 does not have Property $C$ .The implicit Adams methods (see Fig.1.3) have Property $C$ for $k \leq 5$ ． Also,the 4th order implicit Milne-Simpson method (1.16) has property $C$

Definition 4.7 allows us to replace $R _ { s s } ( \mu )$ in the proof of Theorem 4.4 by $R _ { 1 } ( \mu )$ ， $\mathbb { C } ^ { + }$ by the exterior of $S _ { R }$ ， the imaginary axis by $\Delta _ { R }$ and to obtain the following theorem (Jeltsch and Nevanlinna the 5th of April, 1979 at 5 a.m. in Champaign; G.W. the 5th of April, 1979 at 4.30 a.m.in Urbana. How was this coincidence possible? $\mathbf { E }$ -mail was not yet in general use at that time; was it Psimail?)

Theorem 4.8. Let a method with characteristic function $R ( \mu )$ ， stability domain $S _ { R }$ and order $p _ { R }$ possess Property $C$ . If another method with characteristic function $\zeta ( \mu )$ ， stability domain $S _ { \zeta }$ and order $p _ { \zeta }$ is more stable than $R$ ,i.e.,if

$$
S _ { \zeta } \supset S _ { R } ,
$$

then

$$
p \leq 2 s
$$

where

$$
p = \operatorname* { m i n } ( p _ { R } , p _ { \zeta } )
$$

and s is the number of poles of $\zeta ( \mu )$ , each counted with its multiplicity, which are not poles of the principal root $R _ { 1 } ( \mu )$ of $R ( \mu )$ □ ... and tried to optimize the stability boundary. Despite many efforts we were not able to exceed $\sqrt { 3 }$ , the stability boundary of the Milne-Simpson method ... (K.Dekker 1981)

As an illustration of Theorem 4.8 we ask for the largest stability interval on the imaginary axis $I _ { r } = [ - i r , i r ] \subset \mathbb { C }$ of a 3rd order multistep method (for hyperbolic equations). Since we have $s = 1$ for linear multistep methods, $p = 3$ contradicts (4.24) and we obtain from Theorem 4.8 by using for $R ( \mu )$ the Milne-Simpson method (1.16):

Theorem 4.9 (Dekker 1981, Jeltsch & Nevanlinna 1982)．If $a$ linear multistep method of order $p \geq 3$ is stable on $I _ { r }$ , then $r \leq \sqrt { 3 }$ □

The second part of Theorem 4.4 also allows an extension, the essential ingredient for its proof has been the sign of the error constant for the diagonal Padé approximation.

Theorem 4.10. Consider a method with characteristic equation (4.7) satisfying (4.13) and let $p$ denote its order and $C$ its error constant. Suppose

a) the method possesses Property $C$ ，   
$b ,$ ）the principal root $R _ { 1 } ( \mu )$ possesses s poles,   
$c _ { , }$ ） $\ \mathrm { s i g n } \left( C \right) = ( - 1 ) ^ { s }$   
d） $p \geq 2 s - 1$

Then this method is “optimal" in the sense that every other method with s poles which is stable on $\Delta _ { R }$ of (4.22) has either lower order or, for the same order, a larger (in absolute value) error constant. □

Examples. The diagonal and first sub-diagonal Padé approximations satisfy the above hypotheses (see Eq. (IV.3.30)). Also $I$ -stable linear multistep methods with Property $C$ can be applied.

Remark 4.11. Property $C$ allows the extension of Theorem IV.4.17 of Jeltsch & Nevanlinna to explicit multistep methods. Thus explicit methods with comparable numerical work cannot have including stability domains. Exercise 4 below shows that Property $C$ is a necessary condition. Remember that explicit methods have all their poles at infinity.

# General Linear Methods

The large class of general linear methods (Example III.8.5) written in obvious matrix notation

$$
\begin{array} { r } { v _ { n } = \widetilde A u _ { n } + h \widetilde B f ( v _ { n } ) } \\ { u _ { n + 1 } = A u _ { n } + h B f ( v _ { n } ) } \end{array}
$$

seems to allow much more freedom to break the Daniel & Moore conjecture. This is not the case as we shall see in the sequel.

The bulk of numerical work for solving (4.26) is represented by the implicit stages (4.26a) and hence depends on the structure of the matrix $\widetilde { B }$ . Inserting $y ^ { \prime } =$ $\lambda y$ leads to

$$
\mathfrak { u } _ { n + 1 } = S ( \mu ) \mathfrak { u } _ { n }
$$

where

$$
S ( \mu ) = A + \mu B ( I - \mu \widetilde { B } ) ^ { - 1 } \widetilde { A } .
$$

The stability of the numerical method (4.27) is thus governed by the eigenvalues of the matrix $S ( \mu )$ . The elements of this matrix are seen to be rational functions in $\mu$ ·

Lemma 4.12. If the characteristic polynomial of $S ( \mu )$ is multiplied by $\mathrm { d e t } ( I -$ $\mu \widetilde { B } )$ then it becomes polynomial in $\mu$ ：

$$
\begin{array} { r } { \begin{array} { r } { \operatorname* { d e t } ( \zeta I - S ( \mu ) ) \cdot \operatorname* { d e t } ( I - \mu \widetilde { B } ) = q _ { k } ( \mu ) \zeta ^ { k } + q _ { k - 1 } ( \mu ) \zeta ^ { k - 1 } + . . . + q _ { 0 } ( \mu ) } \\ { = : Q ( \mu , \zeta ) \qquad ( a , b , 0 ) } \end{array} } \end{array}
$$

where $q _ { 0 } , \ldots , q _ { k }$ are polynomials of degree $\leq s$ and $q _ { k } ( \mu ) = \operatorname* { d e t } ( I - \mu \tilde { B } )$

Proof. Suppose first that $\tilde { B }$ is diagonalizable as

$$
T ^ { - 1 } \hat { B } T = \mathrm { d i a g } \left( \beta _ { \mathrm { t } } , . . . , \beta _ { \mathrm { s } } \right)
$$

so that from (4.28)

$$
S ( \mu ) = A + B T \mathrm { d i a g } \left( w _ { 1 } , \ldots , w _ { s } \right) T ^ { - 1 } \widetilde A = A + \sum _ { \imath = 1 } ^ { s } w _ { \imath } \vec { d } _ { \imath } \vec { c } _ { \imath } ^ { T }
$$

where

$$
\left. \begin{array} { l } { { w _ { \imath } = \displaystyle \frac { \mu } { 1 - \mu \beta _ { \imath } } } } \\ { { \vec { d } _ { \imath } = i \mathrm { t h } \mathrm { c o l u m n o f } B T } } \\ { { \vec { c } _ { \imath } ^ { T } = i \mathrm { \ - t h } \mathrm { r o w } \mathrm { o f } T ^ { - 1 } \widetilde { A } . } } \end{array} \right. = 1 , \ldots s
$$

We write the matrix $\zeta I - S ( \mu )$ in terms of its column vectors

$$
\Bigl ( \zeta \vec { e } _ { 1 } - \vec { a } _ { 1 } - w _ { 1 } c _ { 1 1 } \vec { d } _ { 1 } - w _ { 2 } c _ { 1 2 } \vec { d } _ { 2 } - \dots , \zeta \vec { e } _ { 2 } - \vec { a } _ { 2 } - w _ { 1 } c _ { 2 1 } \vec { d } _ { 1 } - w _ { 2 } c _ { 2 2 } \vec { d } _ { 2 } ^ { \ } - \dots , \dots \dots \Bigr ) .
$$

Its determinant, the characteristic polynomial of $S ( \mu )$ ,is computed using the multilinearity of det and considering $\zeta , w _ { \iota } , \iota _ { i j }$ as scalars. All terms containing one of the $w _ { j }$ to any power higher than 1 cancel, because the corresponding factor is a determinant with two or more identical columns. Thus,if $\operatorname* { d e t } ( \zeta I - S ( \mu ) )$ is multiplied by $\begin{array} { r } { \prod _ { \tau = 1 } ^ { s } ( 1 - \mu \beta _ { \iota } ) = \operatorname* { d e t } ( I - \mu \widetilde { B } ) } \end{array}$ it becomes a polynomial of the form (4.29).

A non-diagonalizable matrix $\tilde { B }$ is considered as the limit of diagonalizable matrices. The coeficients of the polynomial $Q ( \mu , \zeta )$ depend continuously on $\widetilde { B }$

We conclude that Lemma 4.1 again remains valid for general linear methods. The $s$ poles on the Riemann surface for the algebraic function ${ \cal Q } ( \mu , \zeta ) = 0$ are located at the positions $\mu = 1 / \beta _ { 1 } , \dots , \mu = 1 / \beta _ { s }$ where $\beta _ { i }$ are thc eigcnvalues of the matrix $\widetilde { B }$ .

We next have to investigate the order conditions, i.e., the analogue of Lemma 4.3. Recall that general linear methods must be equipped with a starting procedure (see Eq.(II.8.4a)) which for the differential cquation $y ^ { \prime } = \lambda y$ will be of the form $u _ { 0 } = \psi ( \mu ) \cdot y _ { 0 }$ with $\psi ( 0 ) \neq 0$ . Here $\mu = h \lambda$ and $\psi ( \mu )$ isa $k _ { i }$ -vector of polynomials or rational functions of $\mu$ . Then the diagram of Fig.III.8.1 becomes the one sketched in Fig.4.6.

The order condition (see Formula (II.8.16) of Lemma II.8.11) then gives:

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/4d106e2c4c5474502d825dcb694560554ba0fca12d1cb6512924a18131c1b13b.jpg)  
Fig. 4.6. General linear method for $y ^ { \prime } = \lambda y$

Lemma 4.13. If the general linear method (4.26) is of order $p$ then

$$
\left( e ^ { \mu } I - S ( \mu ) \right) \psi ( \mu ) = \mathcal { O } ( \mu ^ { p } ) \qquad f o r \mu \to 0
$$

$$
E \left( e ^ { \mu } I - S ( \mu ) \right) \psi ( \mu ) = \mathcal { O } ( \mu ^ { p + 1 } ) \quad f o r \mu \to 0
$$

where $E$ is defined in (III.8.12) and $S ( \mu )$ is given in (4.28).

Formula (4.33) tells us,roughly, that $\psi ( \mu )$ is an approximate eigenvector of $S ( \mu )$ with eigenvalue $e ^ { \mu }$ . We shall now see how this information can be turned into order conditions for the correct eigenvalues of $S ( \mu )$ ·

Definition 4.14. Let $\ell$ be the number of principal sheets of (4.29),i.e., the multiplicity of 1 as eigenvalue of $S ( 0 )$ (which,by stability, must then be a simple root of the minimal polynomial). $\ell$ is also the dimension of $I$ in (III.8.12) and the rank of $E$

Theorem 4.15. Suppose that there exists $\psi ( \mu )$ with $\psi ( 0 ) \neq 0$ such that the general linear method satisfies the conditions (4.33) for order $p \geq 1$ . Then the $\ell$ -fold eigenvalue 1 of $S$ continues into $\ell$ eigenvalues $\zeta _ { \jmath } ( \mu )$ of $S ( \mu )$ which satisfy

$$
e ^ { \mu } - \zeta _ { j } ( \mu ) = \mathcal { O } ( \mu ^ { p _ { \jmath } + 1 } ) \qquad \mu \to 0
$$

with

$$
p _ { \jmath } \geq 0 , \qquad \sum _ { \jmath = 1 } ^ { \ell } p _ { \jmath } \geq p .
$$

Examples. a) The matrix

$$
S ( \mu ) = \binom { 1 + \mu } { 3 \mu + \frac { 1 1 } { 8 0 } \mu ^ { 2 } } \quad 1 - \frac { 2 0 } { 3 } \mu ^ { 2 } \nonumber
$$

has $\ell = 2$ so that $E = I$ in (4.33b). There is a vector $\psi ( \mu )$ (non-vanishing for $\mu = 0$ ） such that

$$
( e ^ { \mu } I - S ( \mu ) ) \psi ( \mu ) = \mathcal { O } ( \mu ^ { 6 } ) ,
$$

i.e., $p = 5$ . The eigenvalues

$$
\zeta _ { 1 , 2 } ( \mu ) = \left( 1 - \frac { 1 7 \mu } { 3 } + \frac { 1 3 \mu ^ { 2 } } { 6 } \right) \pm \frac { 2 0 \mu } { 3 } \sqrt { 1 - \frac { \mu } { 2 } + \frac { 9 \mu ^ { 2 } } { 8 0 } }
$$

satisfy $e ^ { \mu } - \zeta _ { 1 } ( \mu ) = \mathcal { O } ( \mu ^ { 6 } )$ $e ^ { \mu } - \zeta _ { 2 } ( \mu ) = \mathcal { O } ( \mu )$ ， which is (4.34) with $p _ { 1 } = 5$ ， $p _ { 2 } = 0$

b) The matrix

$$
S ( \mu ) = \left( \begin{array} { c c } { { 1 + 2 \mu + \frac { \mu ^ { 2 } } { 2 } } } & { { - \mu } } \\ { { \mu } } & { { 1 + \frac { \mu ^ { 2 } } { 2 } } } \end{array} \right)
$$

satisfies (4.33) with $\ell = 2 , p = 4$ . Its eigenvalues $\zeta _ { 1 , 2 } ( \mu ) = 1 + \mu + \mu ^ { 2 } / 2$ fulfil (4.34) with $p _ { 1 } = p _ { 2 } = 2$

c) The example

$$
S ( \mu ) = \binom { 1 + 2 \mu } { \mu } - \mu + \mu ^ { 2 } { } 
$$

has $\ell = 2$ ， $p = 1$ in (4.33). Its eigenvalues $\zeta _ { 1 , 2 } ( \mu ) = 1 + \mu \pm \sqrt { \mu ^ { 3 } }$ satisfy (4.34) with $p _ { 1 } = p _ { 2 } = 1 / 2$ . This example shows that the $p _ { \jmath }$ in (4.34) need not be integers.

Proof of Theorem 4.15. We introduce the matrix

$$
\widetilde { S } ( \mu ) = c ^ { \mu } I - S ( \mu )
$$

which has the same eigenvectors as $S ( \mu )$ and the corresponding eigenvalues

$$
\widetilde { \zeta } _ { \jmath } ( \mu ) = e ^ { \mu } - \zeta _ { \jmath } ( \mu ) .
$$

Formulas (4.34) and (4.35) now say simply that

$$
\prod _ { \jmath = 1 } ^ { \ell } \widetilde { \zeta } _ { \jmath } ( \mu ) = \mathcal { O } ( \mu ^ { p + \ell } ) \qquad \mu \to 0 .
$$

Since the product of the eigenvalues is,as we know, the determinant of the matrix, we look for information about $\operatorname* { d e t } \widetilde { S } ( \mu )$

After a suitable change of coordinates (via the transformation matrix $T$ of (III.8.12)) we suppose the matrix $S = S ( 0 )$ in Jordan canonical form. We then separate blocks of dimensions $\ell$ and $k - \ell$ so that

$$
E = \left( \begin{array} { l l } { I } & { 0 } \\ { 0 } & { 0 } \end{array} \right) , \quad S ( \mu ) = \left( \begin{array} { l l } { I + \mathcal { O } ( \mu ) } & { \mathcal { O } ( \mu ) } \\ { \mathcal { O } ( \mu ) } & { \mathcal { O } ( 1 ) } \end{array} \right) , \quad \psi ( \mu ) = \left( \begin{array} { l } { \psi _ { 1 } ( \mu ) } \\ { \psi _ { 2 } ( \mu ) } \end{array} \right)
$$

$$
\widetilde { S } ( \mu ) = \left( \begin{array} { l l } { { \widetilde { S } _ { 1 1 } ( \mu ) } } & { { \widetilde { S } _ { 1 2 } ( \mu ) } } \\ { { \widetilde { S } _ { 2 1 } ( \mu ) } } & { { \widetilde { S } _ { 2 2 } ( \mu ) } } \end{array} \right) = \left( \begin{array} { l l } { { \mathcal O } ( \mu ) } & { { \mathcal O } ( \mu ) } \\ { { \mathcal O } ( \mu ) } & { { \mathcal O } ( 1 ) } \end{array} \right)
$$

where it is important to notice that $\widetilde { S } _ { 2 2 } ( 0 )$ is invertible; this is because $E$ collects all eigenvalues equal to 1, thus $S _ { 2 2 } ( 0 )$ has no eigenvalues equal to 1 and $\widetilde { S } _ { 2 2 } ( 0 )$ has none equal to zero. Conditions (4.33) now read

$$
\left( \begin{array} { c c } { \widetilde { S } _ { 1 1 } ( \mu ) } & { \widetilde { S } _ { 1 2 } ( \mu ) } \\ { \widetilde { S } _ { 2 1 } ( \mu ) } & { \widetilde { S } _ { 2 2 } ( \mu ) } \end{array} \right) \left( \begin{array} { c } { \psi _ { 1 } ( \mu ) } \\ { \psi _ { 2 } ( \mu ) } \end{array} \right) = \left( \begin{array} { c } { \mathcal { O } ( \mu ^ { p + 1 } ) } \\ { \mathcal { O } ( \mu ^ { p } ) } \end{array} \right) .
$$

Puting $\mu = 0$ in (4.44) we get $\psi _ { 2 } ( 0 ) = 0$ . The assumption $\psi ( 0 ) \neq 0$ thus implies that at least one component of $\psi _ { 1 } ( 0 )$ ， say the $j$ -th component $\psi _ { 1 } { } _ { 2 } ( 0 )$ , does not vanish. Cramer's rule then yields

$$
\operatorname* { d e t } \widetilde { S } ( \mu ) \cdot \psi _ { 1 \jmath } ( \mu ) = \operatorname* { d e t } T ( \mu ) ,
$$

where $T ( \mu )$ is obtained from $\widetilde { S } ( \mu )$ by replacing its $j$ -th column by the right-hand side of (4.44). One easily sees that $\operatorname* { d e t } T ( \mu ) = \mathcal { O } \left( \mu ^ { p + \ell } \right)$ (take out a factor $\mu$ from each of the first $\ell$ lines_and a factor $\mu ^ { p }$ from the $j$ -th column). Because of $\psi _ { 1 } { } _ { 2 } ( 0 ) \neq 0$ this implies $\operatorname* { d e t } \widetilde { S } ( \mu ) = \mathcal { O } ( \mu ^ { p + \ell } )$ . We have thus proved (4.41) (hence (4.34) and(4.35)),because $\widetilde { \zeta } _ { \ell + 1 } , \ldots , \widetilde { \zeta } _ { k }$ do not converge to zero for $\mu \to 0$ ：□

The next lemma excludes fractional orders for $A$ -stable methods:

Lemma 4.16. For $I$ -stable general linear methods the orders $p _ { \jmath }$ in (4.34) must be integers.

Proof.Divide (4.34) by $e ^ { \mu }$ ,let

$$
\frac { \zeta _ { \jmath } ( \mu ) } { e ^ { \mu } } = 1 - C \mu ^ { m / r } + . . .
$$

where $p _ { \ i } + 1 = m / r$ , and suppose that $r > 1$ and $m , r$ are relatively prime. Since $e ^ { \mu } - \zeta _ { \jmath } ( \dot { \mu } )$ are the eigenvalues of the matrix (4.39), hence the roots of an ana-lytic equation, the presence of a root $\mu ^ { m / r }$ involves the occurrence of all branches $\mu ^ { m / r } \cdot e ^ { 2 \imath \pi \jmath / r } ~ ( \jmath = 0 , 1 , . . . , r - 1 )$ .For $\mu { = } \pm i y { = } e ^ { \pm \imath \pi / 2 } y$ （ $y \in \mathbb { R }$ small), inserted into (4.46), we thus obtain $2 r$ different values

$$
1 - C y ^ { m / r } e ^ { \pm \imath m \pi / 2 r } e ^ { 2 \imath \pi \jmath / r } + \ldots \qquad j = 0 , 1 , \ldots r - 1
$$

which form a regular $2 r$ -Mercedes star; hence whatever the argument of $C$ is, there are values of $C ( \pm i y ) ^ { m / r } e ^ { 2 \imath \pi \jmath / r }$ (for some $0 \leq j \leq r - 1 )$ with negative real part, such that from (4.46) $| \zeta _ { , } ( \pm i y ) | > 1$ . This is a contradiction to $I$ -stability.□

And here is the “Daniel-Moore conjecture" for general linear methods:

Theorem 4.17. Let the characteristic function $Q ( \mu , \zeta )$ of an $I$ -stable general linear method possess $s$ poles in $\mathbb { C } ^ { + }$ . Then

$$
p \leq 2 s .
$$

Proof. Again we denote by $A ^ { + } = A \cap \pi ^ { - 1 } ( \mathbb { C } ^ { + } )$ , the part of the order star lying above $\mathbb { C } ^ { + }$ . By $I$ -stability $A ^ { + }$ does not intersect the imaginary axis $\pi ^ { - 1 } ( i \mathbb { R } )$ on any sheet.

By Theorem 4.15 the boundary curves $\gamma _ { m }$ of $A ^ { + }$ visit the origin on the different principal sheets at least $[ \frac { p _ { \jmath } + 1 } { 2 } ]$ times $( j = 1 , \ldots , \ell )$ (see (4.17)), where the $p _ { j }$ are integers by Lemma 4.16. Thus by Lemma 4.2

$$
\sum _ { \jmath = 1 } ^ { \ell } \Big [ \frac { p _ { \jmath } + 1 } { 2 } \Big ] \leq s .
$$

Multiplying this by 2, using $p _ { \jmath } \leq 2 [ { \frac { p _ { \jmath } + 1 } { 2 } } ]$ and (4.35), we get $p \leq 2 s$

# Dual Order Stars

Why not interchange the role of the two variables $\zeta$ and $\mu \cdots ?$ (J. Butcher, June 27,1989, in West Park Hall, Dundee,at midsummernight)

$A$ -stability implies that for all solutions $\zeta _ { j } ( \mu )$ of $Q ( \mu , \zeta ) = 0$ we have

$$
\operatorname { R e } \mu \leq 0 \qquad \Longrightarrow \qquad | \zeta _ { j } ( \mu ) | \leq 1 .
$$

This is logically equivalent to: For all solutions $\mu _ { \ j } ( \zeta )$ of $Q ( \mu , \zeta ) = 0$ we have

$$
| \zeta | \geq 1 \qquad \Longrightarrow \qquad \operatorname { R e } \mu _ { \ j } ( \zeta ) \geq 0
$$

(in fact, pure logic gives us $" > "$ on both sides; the $" \geq "$ then follow by continuity). Further the order condition (4.15) becomes,by passing to inverse functions for the principal root,

$$
\begin{array} { r } { \log \zeta - \mu _ { 1 } ( \zeta ) = - C ( \zeta - 1 ) ^ { p + 1 } + \dots . } \end{array}
$$

Thus order star theory can be very much dualized by the replacements

$$
{ \begin{array} { r c l } { \mu } & { \longleftrightarrow } & { \zeta } \\ { 0 } & { \longleftrightarrow } & { 1 } \\ { { \mathrm { I m a g . ~ a x i s } } } & { \longleftrightarrow } & { { \mathrm { U n i t ~ c i r c l e } } } \\ { { \mathrm { R e } } } & { \longleftrightarrow } & { | \cdot | } \\ { { \mathrm { I m } } } & { \longleftrightarrow } & { { \mathrm { A r g } } } \\ { \exp } & { \longleftrightarrow } & { { \log } } \end{array} }
$$

The analogue of the star defined in (4.12) becomes

$$
A = \left\{ \zeta ; \mathrm { R e } \mu ( \zeta ) \leq \mathrm { R e } ( \log \zeta ) \right\} = \left\{ \zeta ; \mathrm { R e } \mu ( \zeta ) \leq \log | \zeta | \right\}
$$

and the analogue of the relative order star (4.18) becomes

$$
B = \left\{ \zeta ; \mathrm { R e } \mu ( \zeta ) \leq \mathrm { R e } \mu _ { R } ( \zeta ) \right\} .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/ba09a13e62ee9d74a5390722bc5275632ebbf5991b5b1ef341d6dd8ae5e0628f.jpg)  
Fig.4.7. Dual order stars (4.53) for BDF methods

For the special case of the trapezoidal rule this is

$$
B = \left\{ \zeta \ ; \ \mathrm { R e } \mu ( \zeta ) \leq \mathrm { R e } \left( 2 \frac { \zeta - 1 } { \zeta + 1 } \right) \right\} .
$$

The set $A$ is displayed in Fig.4.7 for the BDF2 and BDF3 methods. It explains once again why $A$ -stable methods of order $> 2 s$ are not possible (see Exercise 5).

Still another possibility is to replace (4.5O) by the obviously equivalent condition

$$
| \zeta | \geq 1 \qquad \Longrightarrow \qquad \mathrm { R e } \frac { 1 } { \mu _ { j } ( \zeta ) } \geq 0
$$

in which case order condition (4.51) becomes

$$
{ \frac { 1 } { \log \zeta } } - { \frac { 1 } { \mu _ { 1 } ( \zeta ) } } = C ( \zeta - 1 ) ^ { p - 1 } + . . .
$$

since $\log \zeta$ as well as $\mu _ { \mathrm { 1 } } ( \zeta )$ are $( \zeta - 1 ) + \mathcal { O } \bigl ( ( \zeta - 1 ) ^ { 2 } \bigr )$ . The order stars now become analogously

$$
A = \left\{ \zeta \ ; \ \operatorname { R e } { \frac { 1 } { \mu ( \zeta ) } } \ \geq \ \operatorname { R e } { \frac { 1 } { \log \zeta } } \right\}
$$

and

$$
B = \left\{ \zeta \ ; \ \mathrm { R e } \frac { 1 } { \mu ( \zeta ) } \ \geq \ \mathrm { R e } \frac { 1 } { \mu _ { R } ( \zeta ) } \right\} .
$$

A special advantage of these last definitions is that for linear multistep methods $1 / \mu = \sigma ( \zeta ) / \varrho ( \zeta )$ , hence the poles of the functions involved are the zeros of $\varrho ( \zeta )$ ， which play a role in the definition of ordinary stability (Sect.III.3). This can be used to obtain a geometric proof of the first Dahlquist barrier (Theorem III.3.5), inspired by the paper Iserles & Ngrsett (1984) (see Exercise 6).

Also, the proof for Dahlquist's second barrier of Sect. V.1 (Theorem 1.4) can be seen to be nothing else but a study of $B$ of (4.59) where $r _ { R } ( \zeta )$ represents the trapezoidal rule.

# Exercises

1. Analyze the behaviour of the characteristic roots of (4.7) in the neighbourhood of a pole which coincides with a branch point, i.e., solve (4.7) asymptotically for $\zeta$ large in the case

$$
\varphi _ { k } ( \mu _ { 0 } ) = 0 , \quad \varphi _ { k } ^ { \prime } ( \mu _ { 0 } ) \neq 0 , \quad \varphi _ { k - 1 } ( \mu _ { 0 } ) = 0 , \quad \varphi _ { k - 2 } ( \mu _ { 0 } ) \neq 0 .
$$

Show that these roots behave like 士 $C ( \mu - \mu _ { 0 } ) ^ { - 1 / 2 }$ ·

2. Compute the approximate eigenvectors $\psi ( \mu )$ such that

$$
( e ^ { \mu } I - S ( \mu ) ) \psi ( \mu ) = \mathcal { O } ( \mu ^ { p + 1 } )
$$

for the matrices $S ( \mu )$ given in (4.36), (4.37)， (4.38). Show that the stated orders are optimal.

3. Explain with the help of order stars,why the 2-step 2-stage collocation method with $c _ { 2 } = 1$ (see Exercise 7 of Sect.V.3) looses $A$ -stability exactly when $c _ { \textup { 1 } }$ crosses the superconvergence point (Exercise 8 of Sect. V.3).

4.Modify the coefficient $\beta$ in the method

$$
y _ { n + 1 } = y _ { n } + h \Big ( f _ { n } + \frac { 1 } { 2 } \nabla f _ { n } + \frac { 5 } { 1 2 } \nabla ^ { 2 } f _ { n } + \beta \nabla ^ { 3 } f _ { n } \Big ) ,
$$

which for $\beta = 3 / 8$ is the Adams method of order 4, in such a way that the stability domain becomes strictly larger. This cxample shows that the multistep version of Theorem IV.4.17 of Jeltsch & Nevanlinna requires the hypothesis of "Property $C ^ { \overrightarrow { \mathbf { \alpha } } , \overrightarrow { \mathbf { \Lambda } } }$

5. Prove the Daniel & Moore conjecture with the help of the order star $A$ from (4.53).

Hint. The set $A$ is not allowed to cross the unit circle and along the borderlines of $A$ the imaginary part of $\log { \zeta } - \mu ( \zeta )$ must steadily decrease (consult (4.52) and the proof of Lemma IV.4.5). Hence a borderline starting and ending at the origin must either pass through a pole (which is not outside the unit circle) or cross the negative real axis in the upward direction (where $\operatorname { I m } \left( \log \zeta \right)$ increases by $2 \pi$ ). Since then the set $A$ must be to the left, this is only possible once on each sheet.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/2cabe652384dc3c0056f549d6e0020ea4c08307e5809e4826af2cd3a546307d3.jpg)  
Fig.4.8. Dual order stars (4.58) and (4.59) for

$$
\varrho _ { R } ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 ) ^ { 5 } , \quad \varrho ( \zeta ) = \zeta ^ { 6 } - 1 ,
$$

$$
\sigma _ { R } ( \zeta ) = ( 2 5 1 \zeta ^ { 6 } + 2 7 3 6 \zeta ^ { 5 } + 6 9 5 7 \zeta ^ { 4 } + 1 0 3 5 2 \zeta ^ { 3 } + 6 9 5 7 \zeta ^ { 2 } + 2 7 3 6 \zeta + 2 5 1 ) / 9 4 5
$$

$$
\sigma ( \zeta ) = ( 4 1 \zeta ^ { 6 } + 2 1 6 \zeta ^ { 5 } + 2 7 \zeta ^ { 4 } + 2 7 2 \zeta ^ { 3 } + 2 7 \zeta ^ { 2 } + 2 1 6 \zeta + 4 1 ) / 1 4 0
$$

6.Prove the first Dahlquist barrier by order stars,i.e.，prove that stable linear multistep methods satisfy $p \lesssim k + 2$ （ $k$ even) and $p \leq k + 1$ （ $k$ odd). Prove also that for methods with optimal order the smallest error constant is assumed by the method with

$$
\varrho _ { R } ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 ) ^ { \widetilde { k } - 1 } .
$$

where $\widetilde { k } = k$ (if $k$ is even) and $\stackrel { \sim } { k } = k - 1$ (if $k$ is odd).

Hint. Study theorder stars (4.58) (with $\mu = \mu _ { R } ,$ and (4.59) where $\mu _ { R } = \sigma _ { R } / \varrho _ { R }$ with $\varrho _ { R }$ from (4.60) (see Fig.4.8 for the case $k = 6$ ， $p = 8$ ， $\varrho \big ( \zeta \big ) = \zeta ^ { 6 } - 1 )$ You must show that the two order stars in the vicinity of $\zeta = 1$ have the same colours. The following observations will help:

i) The stars in the vicinity of $\zeta = - 1$ (produced by the pole $1 / ( \zeta + 1 ) ^ { \widetilde { k } - 1 } )$ have opposite colours;

ii) By stability all poles of

$$
d _ { A } ( \zeta ) = \operatorname { R e } \left( \frac { 1 } { \mu _ { R } ( \zeta ) } - \frac { 1 } { \log \zeta } \right) , \quad d _ { B } ( \zeta ) = \operatorname { R e } \left( \frac { 1 } { \mu _ { R } ( \zeta ) } - \frac { 1 } { \mu ( \zeta ) } \right)
$$

lie on or inside the unit circle;

iii） The boundary curves of $A$ and $B$ cannot cross the unit circle arbitrarily often, since $d _ { A } ( e ^ { \imath \varphi } )$ and $d _ { B } { \big ( } e ^ { \imath \varphi } { \big ) }$ are trigonometric polynomials.

iv) Study the behaviour of $A$ and $B$ at infinity.

7. Prove the second Dahlquist barrier for linear multistep methods with the help of the order star (4.55).

8. Compute on a computer for an implicit multistep method of order 3 the order star $B$ of (4.18), where $R ( \mu )$ is the maximal root of the Milne-Simpson method (1.17). Understand at once the validity of Theorem 4.9.

# V.5 Experiments with Multistep Codes

... we know that theory is unable to predict much of what hap-pens in practice at present and software writers need to discover the way ahead by numerical experiment ...

(J.R. Cash, in Aiken 1985)

A comparison of different codes is a notoriously difficult and inexact area ... but there are some clear conclusions that can ...

(J.R. Cash 1983)

This section presents numerical results of multistep codes on precisely the same problems as in Sect.IV.10. These are,in increasing dimension, VDPOL (the van der Pol equation (IV.10.1)), ROBER (the famous Robertson problem(IV.10.2), OREGO (the Oregonator (IV.10.3)),HIREs (the physiological problem (IV.10.4)),E5 (the badly scaled chemical reaction (IV.10.5)), PLATE ((IV.10.6), a car moving on a plate,the only linear and non autonomous problem), BEAM (the nonlinear elastic beam equation (IV.1.10'） with $n = 4 0$ ),CUSP (the cusp catastrophe (IV.10.8)), BRUSS (the brusselator (IV.1.6'）with one-dimensional diffusion $\alpha = 1 / 5 0$ and $n = 5 0 0 \AA$ ),and Ks (the one-dimensional Kuramoto-Sivashinsky equation (IV.10.11) with $n = 1 0 2 2 .$ ). We have not included here the problems BECKDO and BRUSS-2D, since they require a special treatment of the linear algebra routines.

As in Sect.IV.10, the codes have been applied with tolerances

$$
R t o l = 1 0 ^ { - 2 - m / 4 } \qquad m = 0 , 1 , 2 , . . .
$$

and $A t o l = R t o l$ (with the exceptions $A t o l = 1 0 ^ { - 6 } \cdot R t o l$ for OREGO and ROBER, $A t o l = 1 0 ^ { - 4 } \cdot R t o l$ for HIRES, $A t o l = 1 0 ^ { - 3 }$ · Rtol for PLATE, and $A t o l = 1 . 7 \cdot 1 0 ^ { - 2 4 }$ for E5). The numerical precisions obtained compared to the CPU times (where all codes are compiled with the same optimization options) are then displayed in Figs. 5.1 and 5.2, again with the symbols representing the required precision $R t o l =$ $1 0 ^ { - 5 }$ displayed in grey tone.

# The Codes Used

LSODE — is the“Livermore Solver”of Hindmarsh (1980,1983). Since we are dealing with stiff equations,we use “stiff” method flags $\mathrm { M F } = 2 1$ ,22,24 or 25, so that the code is based on the Nordsieck representation of the fixed step size BDF methods (see Sections III.6 and II.7). This code emerged from a long development starting with Gear's DIFSUB in 1971. Its exemplary user interface and ease of application has been a model for much subsequent ODE Software (includ-ing ours). Most problems were computed with analytical Jacobian and full linear algebra ( $\mathbf { M F } = 2 1$ ), with the exception of BRUsS and KS (analytical banded Jacobian, $\mathbf { M F } = 2 4$ ),BEAM (numerical full Jacobian, $\mathbf { M F } = 2 2$ ), and CUSP (numerical banded Jacobian, $\mathrm { M F } = 2 5$ ).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/9a8d3f21c731e09537553506e74a3ec914de455d725dda30b051930fcf46f73f.jpg)  
Fig.5.1. Work-precision diagrams for problems of dimension 2 to 80

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/138797eccef2a3b66331018e66b274c7ccd1aaf68ca70efd9559fbeb5ae72ef9.jpg)  
Fig.5.2. Work-precision diagrams for problems of dimension 80 to 1022

For E5,the code worked correctly only for $T o l \le 1 0 ^ { - 5 }$ , for PLATE it was necessary to have $T o l \le 1 0 ^ { - 7 }$ . For the BEAM problem,which has eigenvalues on the imaginary axis, it was necessary to restrict the maximal order to 2 because of the lack of $A$ -stability of the higher order BDF methods. The disastrous effect of the allowance of orders higher than 2 can be seen in Fig.5.3.

DEBDF — this is Shampine & Watts's driver for a modification of the code LSODE and is included in the“DEPAC” family (Shampine & Watts 1979). As is to be expected, it behaves nearly identically to LsODE (see Figs.5.l and 5.2). It also requires a restriction of the order for the BEAM problem (see Fig.5.3).

VODE - is the“Variable-coefficient Ordinary Differential Equation solver” of Brown, Byrne & Hindmarsh (1989). It is based on the EPISODE and EPISODEB packages (see Sect.II.7) which use BDF methods on a non uniform grid (Byrne & Hindmarsh 1975). The user interface is very similar to that of LSODE; the code again allows selection between full or banded linear algebra and between analytical or numerical Jacobian. The numerical results of VODE (see Figs.5.1 and 5.2) are very similar for the large problems to those of LSODE and DEBDF,the code is, however, considerably slower on the small problems. For problem E5 this code required a tolerance requirement ( $( R t o l \le 1 0 ^ { - 5 }$ ). On the PLATE problem, this code was by far the best. On the BEAM problem,one has to restrict the maximal order to two (Fig. 5.3).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/10a706b2afea68fd807c0ad9b1f0605e78ca515344a8a8d245b4a090e0614b38.jpg)  
Fig. 5.3. Performance of LSODE,DEBDF and VODE on the BEAM problem with restricted maximal order

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/7064f4a70c28ebadefcb40b498c79fdca615325c399ed00a6a73b81d0a5a09f4.jpg)  
Fig. 5.4. Performance of SECDER, compared to LSODE and VODE

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/7da8ccc9079320ecf5bf219d4d59b2132363f507afefc919e777e6282baf3229.jpg)  
Fig. 5.5.Performance of MEBDF, compared to LSODE and VODE (for the BEAM problem with restricted maximal order)

SPRINT- this package,written by M. Berzins (see Berzins & Furzeland 1985), which has been incorporated into the NAG library ("subchapter DO2N"), contains several modules for the step integrator, one of which is SBLEND. This allows us to study the effect of the blended multistep methods (3.15) of Skeel & Kong (1977). It can be seen from Table 3.4 that these methods are $A$ -stable for orders up to 4. We therefore expect them to be much better on the oscillatory BEAM problem. As can be observed in Fig. 5.2 (as well as in Fig.IV.10.8), this code gives excellent results for this problem. An observation of the grey points for $T o l = 1 0 ^ { - 5 }$ (Figs.5.1 and 5.2） shows that the code gives better values than the other multistep codes for a same given tolerance. From time to time, it is fairly slow (e.g.,in the PLATE and KS problems).

SECDER - this code,written in 1979 by C.A. Addison (see Addison 1979), implements the SECond DERivative multistep methods (3.7) of Enright. The high order of the methods accompanied with good stability leads us to expect good performance at high tolerances. This has shown to be true (see Fig.5.4) for OREGO, HIRES and PLATE; however, for the latter it is very slow. We have not used it on the large problems since it has no built-in banded algebra and requires an analytic Jacobian.

MEBDF - this code by Cash & Considine (1992) implements the modified extended BDF methods (see Eq. (3.17.mod) and Table 3.5). Its good performance is shown on selected examples in Fig.5.5. For the BEAM problem, the code works well if the maximal order is limited to 4.

LADAMS - this is the “Livermore Adams” code, i.e., LSODE with method flag $\mathbf { M F } { = } 1 0$ , included to demonstrate the performance of an explicit multistep method on large and/or mildly stiff problems. One can see that it has its chance on several large problems (PLATE, BEAM). It is, when compared to DOPRI5 in Fig.IV.10.8, a good deal slower when $f$ -evaluations are cheap (CUSP), but not on BEAM.

The codes LSODE,DEBDF, VODE and MEBDF can be obtained by sending an electronic mail (e.g.,"send lsode.f from odepack") to “netlib $@$ research.att.com".

# Exercises

1. Do your own experiments and draw your own conclusions for the above problems. The authors will be happy to provide you with drivers and function subroutines.

# V.6One-Leg Methods and G-Stability

... the error analysis is simpler to formulate for one-leg methods than for linear multistep methods. (G.Dahlquist 1975)

The first stability results for nonlinear differential equations and multistep methods are fairly old (Liniger 1956,Dahlquist 1963),older than similar studies for Runge-Kutta methods. The great break-through occured in 1975 (at the Dundee conference) when Dahlquist proposed considering nonlinear problems

$$
y ^ { \prime } = f ( x , y )
$$

which satisfy a one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 }
$$

or, if the functions are complex-valued,

$$
{ \mathrm { R e } } \left. f ( x , y ) - f ( x , z ) , y - z \right. \leq \nu \| y - z \| ^ { 2 }
$$

(see Sect.IV.12). He also found that the study of nonlinear stability for general multistep methods is simplified, if a related class of methods - the so-called oneleg (multistep) methods -is considered.

# One-Leg (Multistep) Methods

... the somewhat crazy name one-leg methods ...

(G. Dahlquist 1983)

Je ne suis absolument pas capable de traduire “one-leg” en francais ...uni-jambiste? (M. Crouzeix,in 1987)

Signor mio, le gru non hanno se non una coscia ed una gamba (Boccaccio, Decameron 1353; quotation suggested by M. Crouzeix)

Suppose that a linear $k$ -step method

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { m + i } = h \sum _ { i = 0 } ^ { k } \beta _ { i } f ( x _ { m + i } , y _ { m + i } )
$$

is given, and that the generating polynomials

$$
\varrho ( \zeta ) = \sum _ { i = 0 } ^ { k } \alpha _ { i } \zeta ^ { i } , \qquad \sigma ( \zeta ) = \sum _ { i = 0 } ^ { k } \beta _ { i } \zeta ^ { i }
$$

E.Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_21, $©$ Springer-Verlag Berlin Heidelberg 2010

have real coefficients and no common divisor (see Sect.II.2). We also assume throughout the normalization

$$
\sigma ( 1 ) = 1 .
$$

Then the associated one-leg method is defined by

$$
\sum _ { i = 0 } ^ { k } \alpha _ { \ i } y _ { m + i } = h f \biggl ( \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } x _ { m + i } , \sum _ { i = 0 } ^ { k } \beta _ { \ i } y _ { m + i } \biggl ) .
$$

In this new method, the derivative $f$ is evaluated at one point only, which makes it easier to analyze.

It is,of course, interesting to know how the solutions of the one-leg method (6.6) are related to those of its “multistep twin” (6.3). If the differential equation is linear and autonomous, $y ^ { \prime } = A y$ ,then both formulas— (6.3) and (6.6) - are identical. For the BDF schemes (1.18) there is in any case only one $f$ -value in the multistep-version, hence the equations (6.3) and (6.6) are the same. For general methods and general nonlinear equations, however, the formulas are not identical, but the solutions are related by certain transformations (see Exercise 3). We con-sider, as an example, the trapezoidal rule, which is a two-leg method,

$$
y _ { m + 1 } - y _ { m } = { \frac { h } { 2 } } \Bigl ( f ( x _ { m } , y _ { m } ) + f ( x _ { m + 1 } , y _ { m + 1 } ) \Bigr ) .
$$

The corresponding one-leg method is the implicit midpoint rule,

$$
y _ { m + 1 } - y _ { m } = h f \Big ( \frac { x _ { m } + x _ { m + 1 } } { 2 } , \frac { y _ { m } + y _ { m + 1 } } { 2 } \Big ) .
$$

If $\{ y _ { m } \}$ is a solution of the one-leg formula (6.8), then

$$
\widehat { y } _ { m } = \frac { 1 } { 2 } \big ( y _ { m } + y _ { m + 1 } \big ) , \qquad \widehat { x } _ { m } = \frac { 1 } { 2 } \big ( x _ { m } + x _ { m + 1 } \big )
$$

satisfies (6.7). On the other hand, if $\{ \widehat { y } _ { m } , \widehat { x } _ { m } \}$ satisfy (6.7), then

$$
y _ { m } = \widehat { y } _ { m } - \frac { h } { 2 } f ( \widehat { x } _ { m } , \widehat { y } _ { m } ) , \qquad x _ { m } = \widehat { x } _ { m } - \frac { h } { 2 }
$$

is a solution of (6.8). This relationship has already been extensively exploited in the proof of Theorem IV.15.8.

# Existence and Uniqueness

We suppose $\alpha _ { k } \neq 0$ (as always) and $\beta _ { k } \neq 0$ (otherwise the method is explicit). In the case of multistep methods, we write (6.3) in the form

$$
y - \eta - h \frac { \beta _ { k } } { \alpha _ { k } } f ( x , y ) = 0 ,
$$

where $\boldsymbol { x }$ is given, $\eta$ is a vector composed of known quantities, and $y = y _ { m + k }$ is the unknown vector. The one-leg Formula (6.6) can also be brought to the form (6.9)

by the transformation $y = \beta _ { k } y _ { m + k } + \ldots + \beta _ { 0 } y _ { m }$ ， so that all subsequent results on existence and uniqueness will be valid for multistep and one-leg methods. To obtain existence results for Eq.(6.9), we replace $h \beta _ { k } / \alpha _ { k }$ by a new “step size” $\widetilde { h }$ and obtain nothing else but implicit Euler. All theorems for implicit Runge-Kutta methods (Theorems 14.2, 14.3,and 14.4 of Sect.IV.14) are immediately applicable and give

Theorem 6.1 (Dahlquist 1975). Let $f$ be continuously differentiable and satisfy (6.2). If

$$
h \nu < \frac { \alpha _ { k } } { \beta _ { k } }
$$

then the nonlinear equation (6.9) has $a$ unique solution $y$

Theorem 6.2. Let y be given by (6.9) and consider $a$ perturbed value $\widehat { y }$ satisfying

$$
{ \widehat { y } } - \eta - h { \frac { \beta _ { k } } { \alpha _ { k } } } f ( x , { \widehat { y } } ) = \delta .
$$

Under the assumption (6.10) we then have

$$
\| \widehat { y } - y \| \leq \frac { 1 } { 1 - ( \beta _ { k } / \alpha _ { k } ) h \nu } \| \delta \| .
$$

Remark. Theorems IV.14.2, IV.14.3 and IV.14.4 are for much more general methods than just the implicit Euler needed here. The reader who is not interested in the more general case can rewrite the proofs of Sect.IV.14 nearly word for word. Since there is now only one implicit stage, all tensor products disappear and the formulas, but not the ideas of the proof, simplify considerably.

# $\pmb { G }$ -Stability

If the differential equation satisfies the one-sided Lipschitz condition (6.2) (or (6.2')) with $\nu = 0$ , then the exact solutions are contractive (Lemma IV.12.1). We shall investigate here,which one-leg (multistep) methods then also have contractive solutions. Since the numerical value $y _ { m + k }$ depends on all $y _ { m + k - 1 } , \ldots , y _ { m } ,$ it makes no sense to require $\| y _ { m + k } - \widehat { y } _ { m + k } \| \leq \| y _ { m + k - 1 } - \widehat { y } _ { m + k - 1 } \|$ as in the one-step case (Definition IV.12.2). We have to consider the method as a mapping $\mathbb { R } ^ { n \cdot k } \to \mathbb { R } ^ { n \cdot k }$ . For this we introduce the notation

$$
Y _ { m } = ( y _ { m + k - 1 } , \dots , y _ { m } ) ^ { T }
$$

and consider inner product norms on $\mathbb { R } ^ { n \cdot k }$

$$
\left\| Y _ { m } \right\| _ { G } ^ { 2 } = \sum _ { \iota = 1 } ^ { k } \sum _ { \jmath = 1 } ^ { k } g _ { \iota \jmath } \left. y _ { m + \iota - 1 } , y _ { m + \jmath - 1 } \right. ,
$$

where $\langle \cdot , \cdot \rangle$ is the inner product on $\mathbb { R } ^ { n }$ used in (6.2) and the $k$ -dimensional matrix

$$
G = ( g _ { i j } ) _ { i , \jmath = 1 , \dots , k }
$$

is assumed to be real, symmetric and positive definite.

Definition 6.3 (Dahlquist 1975). The one-leg method (6.6) is called $G$ -stable, if there exists a real, symmetric and positive definite matrix $G$ ， such that for two numerical solutions $\{ y _ { m } \}$ and $\{ \widehat { y } _ { m } \}$ we have

$$
\| Y _ { m + 1 } - \widehat { Y } _ { m + 1 } \| _ { G } \leq \| Y _ { m } - \widehat { Y } _ { m } \| _ { G }
$$

for all step sizes $h > 0$ and for alldifferential equations satisfying (6.2) or (6.2') with $\nu \simeq 0$ .

Since $y ^ { \prime } = \lambda y , \mathrm { R e } \lambda \leq 0$ satisfies (6.2') with $\nu \simeq 0$ , we immediately get

Theorem 6.4. $G$ -stability implies $A$ -stability.

Example 6.5. Consider the 2-step BDF method

$$
\frac { 3 } { 2 } y _ { m + 2 } - 2 y _ { m + 1 } + \frac { 1 } { 2 } y _ { m } = h f ( x _ { m + 2 } , y _ { m + 2 } ) .
$$

We take a second numerical solution $\{ \widehat { y } _ { m } \}$ and denote its difference to $\{ y _ { m } \}$ by $\Delta y _ { m } = y _ { m } - \widehat { y } _ { m }$ . If we insert (6.16) into our assumption (6.2')

$$
\mathrm { R e } \left. f ( x _ { m + 2 } , y _ { m + 2 } ) - f ( x _ { m + 2 } , \widehat { y } _ { m + 2 } ) , y _ { m + 2 } - \widehat { y } _ { m + 2 } \right. \leq 0
$$

we obtain

$$
E = \mathrm { R e } \left. \frac { 3 } { 2 } \Delta y _ { m + 2 } - 2 \Delta y _ { m + 1 } + \frac { 1 } { 2 } \Delta y _ { m } , \Delta y _ { m + 2 } \right. \leq 0 .
$$

The main idea is now to subtract from this inequality a well-chosen quadratic term $\| a _ { 2 } \Delta y _ { m + 2 } + a _ { 1 } \Delta y _ { m + 1 } + a _ { 0 } \Delta y _ { m } \| ^ { 2 }$ in order to bring it to the form required by (6.15). With $\Delta Y _ { m } = ( \Delta y _ { m + 1 } , \Delta y _ { m } ) ^ { T }$ this means that

$$
E = \| \Delta Y _ { m + 1 } \| _ { G } ^ { 2 } - \| \Delta Y _ { m } \| _ { G } ^ { 2 } + \| a _ { 2 } \Delta y _ { m + 2 } + a _ { 1 } \Delta y _ { m + 1 } + a _ { 0 } \Delta y _ { m } \| ^ { 2 }
$$

with a positive definite matrix

$$
G = \left( \begin{array} { l l } { { g _ { 2 2 } } } & { { g _ { 2 1 } } } \\ { { g _ { 2 1 } } } & { { g _ { 1 1 } } } \end{array} \right) .
$$

Multiplying out and comparing the coefficients of $\mathrm { R e } \left. \Delta y _ { \imath } , \Delta y _ { \jmath } \right.$ in (6.17) and (6.18) gives the six relations

$$
\begin{array} { c c c } { { \displaystyle \frac { 3 } { 2 } = g _ { 2 2 } + a _ { 2 } ^ { 2 } , \qquad 0 = g _ { 1 1 } - g _ { 2 2 } + a _ { 1 } ^ { 2 } , \qquad 0 = - g _ { 1 1 } + a _ { 0 } ^ { 2 } , } } & { { } } & { { } } \\ { { - 2 = 2 g _ { 2 1 } + 2 a _ { 2 } a _ { 1 } , \qquad \displaystyle \frac { 1 } { 2 } = 2 a _ { 2 } a _ { 0 } , \qquad 0 = - 2 g _ { 2 1 } + 2 a _ { 1 } a _ { 0 } . } } & { { } } & { { } } \end{array}
$$

Adding all six equations gives $0 = ( a _ { 0 } + a _ { 1 } + a _ { 2 } ) ^ { 2 }$ , so that $a _ { 0 } + a _ { 1 } + a _ { 2 } = 0$ .This relation together with (6.19b) determines the $a _ { i }$ as $a _ { 0 } = \pm 1 / 2$ ， $a _ { \mathrm { 1 } } = \mp 1$ ， $a _ { 2 } =$ $\pm 1 / 2$ . Inserting this into (6.19) yields the positive definite matrix

$$
G = \frac { 1 } { 4 } \left( \begin{array} { r r } { { 5 } } & { { - 2 } } \\ { { - 2 } } & { { 1 } } \end{array} \right) .
$$

Since $E \le 0$ by (6.17), it follows from (6.18) that the 2-step BDF method is $G$ - stable.

# An Algebraic Criterion

The algebraic structures of the foregoing computations become much more visible, if we replace formally in (6.17) and (6.18) all

$$
\langle \Delta y _ { m + i } , \Delta y _ { m + j } \rangle \longmapsto \zeta ^ { i } \omega ^ { j }
$$

and use

$$
2 \mathrm { R e } \left. \Delta y _ { m + \ i } , \Delta y _ { m + \ j } \right. = \langle \Delta y _ { m + \ i } , \Delta y _ { m + \ j } \rangle + \langle \Delta y _ { m + \ j } , \Delta y _ { m + \ i } \rangle .
$$

This yields

$$
\begin{array} { r l } & { E = \displaystyle \frac { 1 } { 2 } \big ( \varrho ( \zeta ) \sigma ( \omega ) + \varrho ( \omega ) \sigma ( \zeta ) \big ) } \\ & { E = ( \zeta \omega - 1 ) \displaystyle \sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { \imath - 1 } \omega ^ { j - 1 } + \left( \sum _ { i = 0 } ^ { k } a _ { i } \zeta ^ { \imath } \right) \left( \sum _ { j = 0 } ^ { k } a _ { j } \omega ^ { \jmath } \right) . } \end{array}
$$

We can now formulate an algebraic criterion which, in a different notation, already appears in Dahlquist (1975).

Theorem 6.6 (Baiocchi & Crouzeix 1989). Consider a method $( \varrho , \sigma )$ . If there exists a real, smmetric and positive definite matrix $G$ and real numbers $a _ { 0 } , \dots , a _ { k } ,$ such that

$$
\begin{array} { r l r } {  { \frac { 1 } { 2 } \big ( \varrho ( \zeta ) \sigma ( \omega ) + \varrho ( \omega ) \sigma ( \zeta ) \big ) } } \\ & { } & { = ( \zeta \omega - 1 ) \sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { \imath - 1 } \omega ^ { \jmath - 1 } + \Big ( \sum _ { \imath = 0 } ^ { k } a _ { \imath } \zeta ^ { i } \Big ) \Big ( \sum _ { j = 0 } ^ { k } a _ { j } \omega ^ { \jmath } \Big ) , } \end{array}
$$

then the corresponding one-leg method is $G$ -stable.

Remark. The factor $1 / 2$ on the left-hand side of (G) is of no significance and can be replaced by any other positive constant, leading to another scaling of the coeficients $g _ { i j }$ and $a _ { i }$

Proof. We just replace $\zeta ^ { i } \omega ^ { j }$ by $\langle \Delta y _ { m + i } , \Delta y _ { m + j } \rangle$ in Eq (G) and obtain

$$
\begin{array} { l } { { \displaystyle { \mathrm { R e } } \big \langle \sum _ { i = 0 } ^ { k } \alpha _ { i } \Delta y _ { m + i } , \sum _ { j = 0 } ^ { k } \beta _ { j } \Delta y _ { m + j } \big \rangle = } } \\ { { \displaystyle \qquad \| \Delta Y _ { m + 1 } \| _ { G } ^ { 2 } - \| \Delta Y _ { m } \| _ { G } ^ { 2 } + \| \sum _ { i = 0 } ^ { k } a _ { i } \Delta y _ { m + i } \| ^ { 2 } } . } \end{array}
$$

We then insert (6.6) and use (6.2'） with $\nu \simeq 0$ and obtain the desired estimate $\| \Delta Y _ { m + 1 } \| _ { G } \leq \| \Delta Y _ { m } \| _ { G } .$ □

An interesting question is now, for which methods $( \varrho , \sigma )$ Condition (6.21） is satisfied. By Theorem 6.4 the method is necessarily $A$ -stable. Is this also sufficient?

# The Equivalence of $\mathbf { A }$ -Stability and $G$ -Stability

Dahlquist struggled for three years to get the answer, which is

Theorem 6.7 (Dahlquist 1978). If $\varrho$ and $\sigma$ have no common divisor, then the method $( \varrho , \sigma )$ is $A$ -stable if and only if the corresponding one-leg method is $G$ - stable.

Proof. We follow here the presentation of Baiocchi & Crouzeix (1989). Recall first that $A$ -stability of the method $( \varrho , \sigma )$ implies

$$
\operatorname { R e } \varrho ( \zeta ) \overline { { \sigma ( \zeta ) } } \geq 0 \qquad \mathrm { f o r } | \zeta | \geq 1
$$

(see Sect. V.1). Because of Theorems 6.4 and 6.6 it is suficient to prove that condition (A) implies the existence of a real, symmetric and positive definite matrix $G$ and real numbers $a _ { 0 } , \ldots , a _ { k }$ such that Property (G) holds. The proof is in three steps:

a) computation of $a _ { 0 } , \ldots , a _ { k }$ b) computation of $G$ ； c) show that $G$ is positive definite.

a) The term containing the $g _ { i _ { \mathcal { I } } } ^ { \mathrm { ~ ~ } } \mathrm { ~ s ~ }$ in (G) disappears if we put $\omega = 1 / \zeta$ .We therefore consider the function

$$
E ( \zeta ) = \frac { 1 } { 2 } \big ( \varrho ( \zeta ) \sigma ( 1 / \zeta ) + \varrho ( 1 / \zeta ) \sigma ( \zeta ) \big ) ,
$$

which is of the form

$$
\begin{array} { l } { { \displaystyle { E ( \zeta ) = c _ { r } \left( \zeta ^ { r } + \frac { 1 } { \zeta ^ { r } } \right) + c _ { r - 1 } \left( \zeta ^ { r - 1 } + \frac { 1 } { \zeta ^ { r - 1 } } \right) + . . . + c _ { 1 } \left( \zeta + \frac { 1 } { \zeta } \right) + c _ { 0 } } } } \\ { { \displaystyle { = \frac { c _ { r } } { \zeta ^ { r } } \prod _ { j = 1 } ^ { 2 r } ( \zeta - \zeta _ { j } ) } } } \end{array}
$$

with some $r \leq k$ .Since $E ( \zeta ) = E ( 1 / \zeta )$ ，for each root $\zeta _ { j }$ of the polynomial $\zeta ^ { r } E ( \zeta )$ the inverse $1 / \zeta _ { j }$ is also a root with the same multiplicity. Therefore there are as many roots inside the unit circle as there are outside. As to the roots on the unit circle, Condition (A) tells us that $E ( \zeta ) = \mathrm { R e } \varrho ( \zeta ) \sigma ( \overline { { \zeta } } ) \geq 0$ on the unit circle. Therefore, all roots on the unit circle must have even multiplicity, half of them we declare “inside”and half of them we declare “outside". The clever idea is now to collect all roots “outside” the unit circle into a product, so that

$$
\begin{array} { r } { E ( \zeta ) = \cfrac { c _ { r } } { \zeta r } \coth ( \zeta - \zeta _ { j } ) \displaystyle \prod _ { \zeta _ { j } \mathrm { ~ o u t s i d e } } ( \zeta - \zeta _ { j } ) } \\ { = \cfrac { c _ { r } } { \zeta r } \displaystyle \prod _ { \zeta _ { j } \mathrm { ~ o u t s i d e } } ( \zeta - \zeta _ { j } ) \displaystyle \prod _ { \zeta _ { j } \mathrm { ~ o u t s i d e } } ( \zeta - \frac { 1 } { \zeta _ { j } } ) } \\ { = K \displaystyle \prod _ { \zeta _ { j } \mathrm { ~ o u t s i d e } } ( \zeta - \zeta _ { j } ) \displaystyle \prod _ { \zeta _ { j } \mathrm { ~ o u t s i d e } } ( \frac { 1 } { \zeta } - \zeta _ { j } ) } \end{array}
$$

where $\bar { \kappa }$ is a constant. But this constant must be non-negative,as can be seen thus: by Condition (A), $E ( \zeta )$ is non-negative on the unit circle. The same is true for the function divided by $\bar { k }$ ， since each factor $( e ^ { i \theta } - \zeta _ { j } )$ from the first product has a complex conjugate brother $\left( e ^ { - i \theta } - \overline { { \zeta } } _ { \jmath } \right)$ in the second. Therefore $E ( \zeta )$ in (6.24) can be factored as

$$
E ( \zeta ) = a ( \zeta ) \cdot a ( 1 / \zeta )
$$

where

$$
a ( \zeta ) = \sqrt { K } \prod _ { \zeta _ { j } \mathrm { o u t s i d e } } ( \zeta - \zeta _ { j } ) = : \sum _ { i = 0 } ^ { k } a _ { i } \zeta ^ { i } .
$$

and step (a) is done.

b) It follows from (6.22)and (6.25) that the polynomial

$$
P ( \zeta , \omega ) = \frac { 1 } { 2 } \Big ( \varrho ( \zeta ) \sigma ( \omega ) + \varrho ( \omega ) \sigma ( \zeta ) \Big ) - a ( \zeta ) a ( \omega )
$$

vanishes when $\zeta \omega - 1 = 0$ . It can therefore be written as

$$
P ( \zeta , \omega ) = ( \zeta \omega - 1 ) \sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { i - 1 } \omega ^ { j - 1 } .
$$

The coefficients $g _ { i j }$ are real and satisfy $g _ { i j } = g _ { j i }$ , because $P ( \zeta , \omega ) = P ( \omega , \zeta )$

c) Looking at (6.28), it appears at first sight a difficult task to prove positive definiteness for the matrix $G = ( g _ { i j } )$ defined there. The crucial idea is the following: choose $k$ (at first arbitrary) complex numbers $\zeta _ { 1 } , \ldots , \zeta _ { k }$ and replace in (6.28) $\zeta \mapsto \overline { { \zeta } } _ { q } , \omega \mapsto \zeta _ { r }$ , which gives together with (6.27)

$$
\begin{array} { l } { { \displaystyle b _ { q r } = \sum _ { i , j = 1 } ^ { k } \overline { { { \zeta } } } _ { q } ^ { i - 1 } g _ { i j } \zeta _ { r } ^ { j - 1 } } } \\ { { \displaystyle \ = \frac { 1 } { 1 - \overline { { { \zeta } } } _ { q } \zeta _ { r } } \Big \{ - \frac { 1 } { 2 } \Big ( \varrho ( \overline { { { \zeta } } } _ { q } ) \sigma ( \zeta _ { r } ) + \varrho ( \zeta _ { r } ) \sigma ( \overline { { { \zeta } } } _ { q } ) \Big ) + a ( \overline { { { \zeta } } } _ { q } ) a ( \zeta _ { r } ) \Big \} } . }  \end{array}
$$

Here the $b _ { q r }$ are the elements of the matrix

$$
B = V ^ { * } G V
$$

where $V = \big ( \zeta _ { \jmath } ^ { \imath - 1 } \big )$ is a Vandermonde matrix. Thus, we now have to prove that $B$ is positive definite, which appears much easier. First, we develop

$$
\frac { 1 } { 1 - \overline { { \zeta } } _ { q } \zeta _ { r } } = 1 + \overline { { \zeta } } _ { q } \zeta _ { r } + \overline { { \zeta } } _ { q } ^ { 2 } \zeta _ { r } ^ { 2 } + \overline { { \zeta } } _ { q } ^ { 3 } \zeta _ { r } ^ { 3 } + \dots .
$$

which converges if

$$
| \zeta _ { q } | < 1 \qquad q = 1 , 2 , \ldots , k .
$$

Next, we require that for all $q$

$$
\varrho ( \zeta _ { q } ) + \lambda \sigma ( \zeta _ { q } ) = 0 \qquad \mathrm { f o r ~ s o m e } ~ \lambda > 0 .
$$

With the exception of a finite number of $\lambda ^ { \prime } s$ ，the $k$ roots of Eq.(6.31) are all different. $A$ -stability (assumption (A)） implies (6.30b), because $- \lambda$ lies in the interior of the stability domain. Inserting (6.31) and (6.30a) into (6.29) gives, for an arbitrary non-zero vector $\vec { v } = ( v _ { 1 } , \ldots , v _ { k } )$ ，

$$
\vec { v } ^ { * } B \vec { v } = \sum _ { q , r = 1 } ^ { k } \overline { { v } } _ { q } b _ { q r } v _ { r } = \sum _ { m = 0 } ^ { \infty } \Big \{ \big | \sum _ { q = 1 } ^ { k } v _ { q } \zeta _ { q } ^ { m } a ( \zeta _ { q } ) \big | ^ { 2 } + \lambda \big | \sum _ { q = 1 } ^ { k } v _ { q } \zeta _ { q } ^ { m } \sigma ( \zeta _ { q } ) \big | ^ { 2 } \Big \} ,
$$

which looks rather positive. This expression cannot be zero for $\vec { v } \neq 0$ , because it follows from (6.31) that $\sigma ( \zeta _ { q } ) \neq 0$ for all $q$ ,otherwise $\varrho$ and $\sigma$ would have a common factor. Therefore $\vec { v } ^ { * } \dot { B } \vec { v } > 0$ ， thus the matrix $B$ ， and consequently the matrix $G$ , is positive definite. □

It is worth noting that the above proof provides constructive formulas for the matrix $G$ . As an illustration, we again consider the 2-step BDF method (6.16) with generating polynomials

$$
\varrho ( \zeta ) = \frac { 3 } { 2 } \zeta ^ { 2 } - 2 \zeta + \frac { 1 } { 2 } , \qquad \sigma ( \zeta ) = \zeta ^ { 2 } .
$$

The function $E ( \zeta )$ (Formula (6.22) becomes

$$
E ( \zeta ) = \frac { 1 } { 4 } \big ( \zeta ^ { 2 } + \frac { 1 } { \zeta ^ { 2 } } \big ) - \big ( \zeta + \frac { 1 } { \zeta } \big ) + \frac { 3 } { 2 } = \frac { 1 } { 4 } \big ( \zeta - 1 \big ) ^ { 2 } \big ( \frac { 1 } { \zeta } - 1 \big ) ^ { 2 }
$$

so that $\begin{array} { r } { a ( \zeta ) = \frac { 1 } { 2 } ( \zeta - 1 ) ^ { 2 } } \end{array}$ . Inserting this into (6.27) gives

$$
P ( \zeta , \omega ) = ( \zeta \omega - 1 ) \big ( \frac { 5 } { 4 } \zeta \omega - \frac { 1 } { 2 } \zeta - \frac { 1 } { 2 } \omega + \frac { 1 } { 4 } \big ) ,
$$

so that $g _ { 2 2 } = 5 / 4$ ， $g _ { 1 2 } = g _ { 2 1 } = - 1 / 2$ ， $g _ { 1 1 } = 1 / 4$ is the same as (6.20).

# A Criterion for Positive Functions

In the proof of Lemma IV.13.19 we have used the following criterion for positive functions, which is an immediate consequence of the above equivalence result.

Lemma 6.8. Let $\chi ( z ) = \alpha ( z ) / \beta ( z )$ be an irreducible rational function with real polynomials $\alpha ( z )$ ofdegree $\le k - 1$ and $\beta ( z )$ ofdegree $k$ . Then $\chi ( z )$ is a positive function, i.e.,

$$
\mathrm { R e } \chi ( z ) > 0 \qquad f o r \qquad \mathrm { R e } z > 0 ,
$$

if and only if there exist a real, symmetric and positive definite matrix $A$ and $a$ real, symmetric and non-negative definite matrix $B$ ， such that

$$
\alpha ( z ) \beta ( w ) + \alpha ( w ) \beta ( z ) = ( z + w ) \sum _ { \imath , \jmath = 1 } ^ { k } a _ { \imath g } z ^ { i - 1 } w ^ { \jmath - 1 } + \sum _ { \imath , \jmath = 1 } ^ { k } b _ { \imath g } z ^ { \imath - 1 } w ^ { \jmath - 1 } .
$$

Proof. The “if"-part follows immediately by putting $w = { \overline { { z } } }$ in (6.33). For the “only if"-part we consider the transformations

$$
\zeta = \frac { z + 1 } { z - 1 } , \quad z = \frac { \zeta + 1 } { \zeta - 1 } \qquad \mathrm { a n d } \qquad \omega = \frac { w + 1 } { w - 1 } , \quad w = \frac { \omega + 1 } { \omega - 1 }
$$

and introduce the polynomials

$$
\varrho ( \zeta ) = \Big ( { \frac { \zeta - 1 } { 2 } } \Big ) ^ { k } \alpha \Big ( { \frac { \zeta + 1 } { \zeta - 1 } } \Big ) , \qquad \sigma ( \zeta ) = \Big ( { \frac { \zeta - 1 } { 2 } } \Big ) ^ { k } \beta \Big ( { \frac { \zeta + 1 } { \zeta - 1 } } \Big ) .
$$

As the transformation (6.34) maps $| \zeta | > 1$ onto the half plane $\mathtt { R e } z > 0$ , Condition (6.32) is equivalent to Assumption (A). Therefore, Theorem 6.7 implies the existence of a real, symmetric and positive definite matrix $G$ and of real numbers ao,...,ak such that

$$
\frac 1 2 \big ( \varrho ( \zeta ) \sigma ( \omega ) + \varrho ( \omega ) \sigma ( \zeta ) \big ) = ( \zeta \omega - 1 ) \sum _ { \iota , \jmath = 1 } ^ { k } g _ { \iota \jmath } \zeta ^ { \iota - 1 } \omega ^ { \jmath - 1 } + \Big ( \sum _ { \iota = 0 } ^ { k } a _ { \iota } \zeta ^ { \iota } \Big ) \Big ( \sum _ { \jmath = 0 } ^ { k } a _ { \jmath } \omega ^ { \jmath } \Big ) .
$$

Backsubstitution of the old variables yields

$$
\begin{array} { l } { \displaystyle \frac 1 2 ( \alpha ( z ) \beta ( w ) + \alpha ( w ) \beta ( z ) ) \qquad \qquad \quad ( 6 . 3 } \\ { \displaystyle \qquad = 2 ( z + w ) \sum _ { \imath , \jmath = 1 } ^ { k } g _ { \imath \jmath } ( z + 1 ) ^ { \imath - 1 } ( z - 1 ) ^ { k - \imath } ( w + 1 ) ^ { \jmath - 1 } ( w - 1 ) ^ { k - \jmath } } \\ { \displaystyle \qquad + \left( \sum _ { \imath = 0 } ^ { k } a _ { \imath } ( z + 1 ) ^ { \imath } ( z - 1 ) ^ { k - \imath } \right) \left( \sum _ { \jmath = 0 } ^ { k } a _ { \jmath } ( w + 1 ) ^ { \jmath } ( w - 1 ) ^ { k - \jmath } \right) . } \end{array}
$$

Rearranging into powers of $z$ and $w$ gives Eq.(6.33). Since the polynomials $( z +$ $1 ) ^ { \iota - 1 } \left( z - 1 \right) ^ { k - \iota }$ for $i = 1 , \ldots , k$ are linearly independent, the resulting matrix $A$ is positive definite. The coefficient of $z ^ { k } w ^ { k }$ in the second term of the right-hand side of (6.35) must vanish, because the degree of $\alpha ( z )$ is at most $k - 1$ . We remark that the matrix $B$ of this construction is only of rank 1. □

# Error Bounds for One-Leg Methods

We shall apply the stability results of this section to derive bounds for the global error of one-leg methods. For a differential equation (6.1） with exact (smooth) solution $y ( x )$ it is natural to define the discretization error of (6.6) as

$$
\delta _ { O L } ( x ) = \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y ( x + i h ) - h f \biggl ( x + \beta h , \sum _ { i = 0 } ^ { k } \beta _ { \imath } y ( x + i h ) \biggr )
$$

with $\beta = \sigma ^ { \prime } ( 1 ) = \sum i \beta _ { \ i }$ . For the BDF methods we have $\begin{array} { r } { \sum _ { \ i } \beta _ { i } y ( x + i h ) = y ( x + } \end{array}$ $\beta h )$ , so that (6.36) equals

$$
\delta _ { D } ( x ) = \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y ( x + i h ) - h y ^ { \prime } ( x + \beta h ) ,
$$

the so-called differentiation error of the method. For methods which do not satisfy $\begin{array} { r } { \sum _ { \imath } \beta _ { \imath } y ( x + i h ) = y ( x + \beta h ) } \end{array}$ , the right hand side of (6.36) may become very large for stiff problems,even if the derivatives of the solution are bounded by a constant of moderate size. In this case,the expression (6.36) is not a suitable quantity for error estimates. Dahlquist (1983) proposed considering in addition to $\delta _ { D } ( x )$ also the interpolation error

$$
\delta _ { I } ( x ) = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } y ( x + i h ) - y ( x + \beta h ) .
$$

For nonstiff problems (with bounded derivatives of $f$ ) these two error expressions are related to $\delta _ { O L } ( x )$ by

$$
\delta _ { O L } ( x ) = \delta _ { D } ( x ) - h \frac { \partial f } { \partial y } \left( x , y ( x ) \right) \delta _ { I } ( x ) + \mathcal { O } ( h \| \delta _ { I } ( x ) \| ^ { 2 } ) .
$$

Taylor expansion of (6.37) and (6.38) shows that

$$
\delta _ { D } ( x ) = \mathcal { O } \bigl ( h ^ { p _ { D } + 1 } \bigr ) , \qquad \delta _ { I } ( x ) = \mathcal { O } \bigl ( h ^ { p _ { I } + 1 } \bigr ) ,
$$

where the optimal orders $p _ { D }$ and $p _ { I }$ are determined by certain algebraic conditions (see Exercise 1a). From $\beta = \sigma ^ { \prime } { ( 1 ) }$ we always have $p _ { I } \geq 1$ and from the consistency conditions it follows that $p _ { D } \geq 1$ . However, the orders $p _ { D }$ and $p _ { I }$ may be significantly smaller than the order of the corresponding multistep method (Exercise 1). The constants in the $\mathcal { O } ( \dots )$ -terms of (6.39) depend only on bounds for a certain derivative of the solution, but not on the stiffness of the problem.

Using $\delta _ { D } ( x )$ and $\delta _ { I } ( x )$ it is possible to interpret the exact solution of (6.1) as the solution of the following perturbed one-leg formula

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y ( x + i h ) - \delta _ { D } ( x ) = h f \Big ( x + \beta h , \sum _ { i = 0 } ^ { k } \beta _ { , } y ( x + i h ) - \delta _ { I } ( x ) \Big ) .
$$

The next lemma, which extends results of Dahlquist (1975) and of Nevanlinna (1976), investigates the influence of perturbations to the solution of a one-leg method.

Lemma 6.9. Consider, in addition to the one-leg method (6.6), the perturbed formula

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } \widehat { y } _ { m + \ i } - \delta _ { m } = h f \Bigg ( x _ { m } + \beta h , \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \widehat { y } _ { m + \ i } - \varepsilon _ { m } \Bigg ) .
$$

Suppose that the condition (6.2') holds for the differential equation (6.1) and that the method is $G$ -stable. Then the differences

$$
\Delta y _ { \jmath } = \widehat { y } _ { \jmath } - y _ { \jmath } , \qquad \Delta Y _ { m } = \left( \Delta y _ { m + k - 1 } , \ldots , \Delta y _ { m } \right) ^ { T }
$$

satisfy in the norm (6.14)

$$
\| \Delta Y _ { m + 1 } \| _ { G } \leq ( 1 + c h \nu ) \| \Delta Y _ { m } \| _ { G } + C \bigl ( \| \delta _ { m } \| + \| \varepsilon _ { m } \| \bigr ) \qquad f o r \ 0 < h \nu \leq C o n s t .
$$

The constants $c , C$ ， and Const depend only on the method, not on the differential equation. If $\nu \leq 0$ we have

$$
\begin{array} { r } { \| \Delta Y _ { m + 1 } \| _ { G } \leq \| \Delta Y _ { m } \| _ { G } + C \big ( \| \delta _ { m } \| + \| \varepsilon _ { m } \| \big ) \qquad f o r \ a l l \ h > 0 . } \end{array}
$$

Proof. We shall make the additional assumption that $f$ is continuously differentiable.A direct proof without this assumption is possible, but leads to a quadratic inequality for $\| \Delta Y _ { m + 1 } \| _ { G }$

The idea is to subtract (6.6) from (6.41) and to use

$$
\begin{array} { c } { f \big ( x _ { m } + \beta h , \displaystyle \sum \beta _ { \imath } \widehat { y } _ { m + \imath } - \varepsilon _ { m } \big ) - f \big ( x _ { m } + \beta h , \displaystyle \sum \beta _ { \imath } y _ { m + \imath } \big ) } \\ { = J _ { m } \big ( \displaystyle \sum \beta _ { \imath } \Delta y _ { m + \imath } - \varepsilon _ { m } \big ) } \end{array}
$$

where

$$
J _ { m } = \int _ { 0 } ^ { 1 } \frac { \partial f } { \partial y } \Big ( x _ { m } + \beta h , t \sum \beta _ { i } y _ { m + \ i } + ( 1 - t ) \big ( \sum \beta _ { i } \widehat { y } _ { m + \ i } - \varepsilon _ { m } \big ) \Big ) d t .
$$

This yields

$$
\sum _ { i = 0 } ^ { k } \alpha _ { \ i } \Delta y _ { m + \ i } = h J _ { m } \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \Delta y _ { m + \ i } + \delta _ { m } - h J _ { m } \varepsilon _ { m } .
$$

Computing $\Delta y _ { m + k }$ from this relation gives

$$
\Delta y _ { m + k } = \Delta z _ { m + k } + ( \alpha _ { k } - \beta _ { k } h J _ { m } ) ^ { - 1 } ( \delta _ { m } - h J _ { m } \varepsilon _ { m } )
$$

where $\Delta z _ { m + k }$ is defined by

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } \Delta z _ { m + 1 } = h J _ { m } \sum _ { i = 0 } ^ { k } \beta _ { 1 } \Delta z _ { m + 1 }
$$

and $\Delta z _ { \jmath } = \Delta y _ { j }$ for $j < m + k$ . By our assumption (6.2'） the matrix $J _ { m }$ satisfies the one-sided Lipschitz condition $\mathrm { R e } \left. J _ { m } u , u \right. \leq \nu \| u \| ^ { 2 }$ (see Exercise 6 of Sect. I.10). Taking the scalar product of (6.43) with $\sum \beta _ { \imath } \Delta z _ { m + i }$ and using (6.21) we thus obtain in the notation of (6.13)

$$
\begin{array} { r l r } {  { \| \Delta Z _ { m + 1 } \| _ { G } ^ { 2 } - \| \Delta Z _ { m } \| _ { G } ^ { 2 } \leq c _ { 0 } h \nu \| \sum \beta _ { \lambda } \Delta z _ { m + i } \| ^ { 2 } } } \\ & { } & { \leq c _ { 1 } h \nu ( \| \Delta Z _ { m + 1 } \| _ { G } + \| \Delta Z _ { m } \| _ { G } ) ^ { 2 } } \end{array}
$$

(the second inequality is only valid for $\nu \geq 0$ ; for negative values of $\nu$ we replace $\nu$ by 0 in (6.2'). A division by $\| \Delta Z _ { m + 1 } \| _ { G } + \| \Delta Z _ { m } \| _ { G }$ then leads to the estimate

$$
\| \Delta Z _ { m + 1 } \| _ { G } \leq ( 1 + c h \nu ) \| \Delta Z _ { m } \| _ { G } .
$$

With the help of von Neumann's theorem (Sect.IV.11) the second term of (6.42) can be bounded by $C o n s t ( \| \delta _ { m } \| + \| \varepsilon _ { m } \| )$ ． Inserting this and (6.44) into (6.42) yields the desired estimate. □

The above lemma allows us to derive a convergence result for one-leg methods, which is related to $B$ -convergence for Runge-Kutta methods.

Theorem 6.10. Consider a $G$ -stable one-leg method with differentiation order $p _ { D } \geq p$ and interpolation order $p _ { I } \geq p - 1$ . Suppose that the differential equation satisfies the one-sided Lipschitz condition (6.2'). Then there exists $C _ { 0 } > 0$ such that for $h \nu \leq C _ { 0 }$

$$
\left. \left. y _ { m } - y ( x _ { m } ) \right. \right. \leq C \operatorname* { m a x } _ { 0 \leq j < k } \left. \left. y _ { j } - y ( x _ { j } ) \right. \right. + M h ^ { p } .
$$

The constant $C$ depends on the method and, for $\nu > 0$ ， on the length ${ x _ { m } } - { x _ { 0 } }$ of the integration interval; the constant $M$ depends in addition on bounds for the $p$ -th and $( p + 1 )$ -th derivative of the exact solution.

Proof. A direct application of Lemma 6.9 to Eq.(6.40) yields the desired error bounds only for $p _ { I } \geq p$ . Following Hundsdorfer & Steininger (1991) we therefore introduce ${ \widehat { y } } ( x ) = y ( x ) - \delta _ { I } ( x )$ , so that (6.40) becomes

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } { \widehat { y } } ( x + i h ) - { \widehat { \delta } } ( x ) = h f { \big ( } x + \beta h , \sum _ { \iota = 0 } ^ { k } \beta _ { i } { \widehat { y } } ( x + i h ) - { \widehat { \varepsilon } } ( x ) { \big ) } ,
$$

where

$$
\widehat { \delta } ( x ) = \delta _ { D } ( x ) - \sum _ { i = 0 } ^ { k } \alpha _ { i } \delta _ { I } ( x + i h ) , \quad \widehat { \varepsilon } ( x ) = \delta _ { I } ( x ) - \sum _ { i = 0 } ^ { k } \beta _ { \ i } \delta _ { I } ( x + i h ) .
$$

Using $\varrho ( 1 ) = 0$ and $\sigma ( 1 ) = 1$ , Taylor expansion of these functions yields

$$
\| \widehat { \delta } ( x ) \| + \| \widehat { \varepsilon } ( x ) \| \leq C _ { 1 } h ^ { p } \int _ { x } ^ { x + k h } \| y ^ { ( p + 1 ) } ( \zeta ) \| d \zeta .
$$

We thus can apply Lemma 6.9 to (6.46) and obtain

$$
\| \Delta Y _ { m + 1 } \| _ { G } \leq ( 1 + c h \nu ) \| \Delta Y _ { m } \| _ { G } + M _ { 1 } h ^ { p + 1 }
$$

where $\Delta y _ { j } = \widehat { y } ( x _ { j } ) - y _ { j }$ . Using $( 1 + c h \nu ) ^ { j } \leq \exp ( c \nu ( x _ { j } - x _ { 0 } ) )$ , a simple induction argument gives

$$
\| \Delta Y _ { m + 1 } \| _ { G } \leq C \| \Delta Y _ { 0 } \| _ { G } + M h ^ { p } .
$$

The statement now follows from the equivalence of norms

$$
d _ { 0 } \| \Delta Y _ { 0 } \| _ { G } \leq \operatorname* { m a x } _ { 0 \leq \jmath < k } \| \Delta y _ { \jmath } \| \leq d _ { 1 } \| \Delta Y _ { 0 } \| _ { G } ,
$$

from the estimate $| | y _ { m } - y ( x _ { m } ) | | \leq | | y _ { m } - \widehat { y } ( x _ { m } ) | | + | | \delta _ { I } ( x _ { m } ) | |$ , and from the fact that $\| \delta _ { I } ( x _ { m } ) \| = \mathcal { O } ( h ^ { p } )$ □

# Convergence of $\mathbf { A }$ -Stable Multistep Methods

An interesting equivalence relation between one-leg and linear multistep methods is presented in Dahlquist (1975) (see Exercise 3). This allows us to translate the above convergence result into a corresponding one for multistep methods (Hundsdorfer & Steininger 1991). A different and more direct approach will be presented in Sect. V.8 (Theorem 8.2).

We consider the linear multistep method

$$
\sum _ { i = 0 } ^ { k } \alpha _ { \ i } { \widehat { y } } _ { m + i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } f ( { \widehat { x } } _ { m + \ i } , { \widehat { y } } _ { m + \ i } ) .
$$

We let $x _ { m } =  { \widehat { x } } _ { m } - \beta h$ , so that $et { } { _ { k } ^ { k } } \sum _ { \iota = 0 } \beta _ { \iota } x _ { m + \iota } = \widehat { x } _ { m }$ and,i (6),w define $\left\{ y _ { 0 } , y _ { 1 } , \dotsc , y _ { 2 k - 1 } \right\}$ as the solution of the linear system

$$
\sum _ { \ i = 0 } ^ { k } \beta _ { i } y _ { \jmath + \imath } = \widehat { y } _ { \jmath } , \qquad \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y _ { \jmath + \imath } = h f ( \widehat { x } _ { \jmath } , \widehat { y } _ { \jmath } ) , \qquad j = 0 , \ldots , k - 1 .
$$

This system is uniquely solvable, because the polynomials $\varrho ( \zeta )$ and $\sigma ( \zeta )$ are rela-tively prime. With these starting values we define $\{ y _ { m } \}$ as solution of the one-leg relation (for $m \geq k$ ）

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { i } y _ { m + i } = h f \Big ( \sum _ { i = 0 } ^ { k } \beta _ { \ i } x _ { m + \ i } , \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } y _ { m + \ i } \Big ) .
$$

By the second relation of (6.49),Eq.(6.50) holds for all $m \geq 0$ . Consequently (Extrise 3a)thexpreson $\scriptstyle \sum _ { i = 0 } ^ { k } \beta _ { \imath } y _ { m + \imath }$ isasout (6.48). Because of (6.49) and the uniqueness of the numerical solution this gives

$$
\sum _ { i = 0 } ^ { k } \beta _ { \ i } y _ { m + i } = \widehat { y } _ { m } \qquad \mathrm { f o r ~ a l l } \quad m \geq 0 .
$$

This relation leads to a proof of the following result.

Theorem 6.11. Consider an $A$ -stable linear multistep method of order $p$ . Suppose the differential equation satisfies (6.2'). Then there exists $C _ { 0 } > 0$ such that for $h \nu \leq C _ { 0 }$ ，

$$
\| \widehat { y } _ { m } - y \big ( \widehat { x } _ { m } \big ) \| \leq C \big ( \operatorname* { m a x } _ { 0 \leq j < k } \| \widehat { y } _ { j } - y \big ( \widehat { x } _ { j } \big ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( \widehat { x } _ { j } , \widehat { y } _ { j } ) - y ^ { \prime } ( \widehat { x } _ { j } ) \| \big ) + M h ^ { p } .
$$

The constants $C$ and $M$ are as in Theorem 6.10.

Proof. By Theorem 6.7, $A$ -stability implies $G$ -stability of the corresponding one-leg method. Further, Taylor expansion of (6.37) and (6.38) shows that $p _ { D } \ge$ $\operatorname* { m i n } ( p , 2 )$ and $p _ { I } \geq 1$ . Since $p \leq 2$ by Dahlquist's second barrier,all assumptions of Theorem 6.10 are verified. The one-leg solution $\{ y _ { m } \}$ thus satisfies (6.45). In order to estimate $\| y _ { j } - y ( x _ { j } ) \|$ for $j < k$ we subtract the definitions of $\delta _ { D } ( x )$ and $\delta _ { I } ( x )$ from (6.48) and obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \beta _ { i } \big ( y _ { \jmath + \imath } - y ( x _ { \jmath + \imath } ) \big ) = { \widehat { y } } _ { j } - y ( { \widehat { x } } _ { \jmath } ) - \delta _ { I } ( x _ { \jmath } ) } } \\ { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { \imath } \big ( y _ { j + \imath } - y ( x _ { j + \imath } ) \big ) = h f ( { \widehat x } _ { \jmath } , { \widehat { y } } _ { \jmath } ) - h y ^ { \prime } ( { \widehat x } _ { \jmath } ) - \delta _ { D } ( x _ { j } ) . } } \end{array}
$$

Solving these relations for $y _ { \jmath } - y ( x _ { j } )$ yields

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - y ( x _ { j } ) \| } } \\ & { \leq } & { C _ { 0 } \Big ( \operatorname* { m a x } _ { 0 \leq j < k } \| \widehat { y } _ { j } - y ( \widehat { x } _ { j } ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( \widehat { x } _ { j } , \widehat { y } _ { j } ) - y ^ { \prime } ( \widehat { x } _ { j } ) \| \Big ) + M _ { 0 } h ^ { p } . } \end{array}
$$

This proves the statement, because by (6.51)

$$
\| \widehat { y } _ { m } - y ( \widehat { x } _ { m } ) \| \leq \sum _ { \iota = 0 } ^ { k } | \beta _ { i } | \| y _ { m + \iota } - y ( x _ { m + \iota } ) \| + \| \delta _ { I } ( x _ { m } ) \| .
$$

# Exercises

1. a) Prove that the one-leg method (6.6) satisfies (6.39) iff

$$
\begin{array} { l } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { i } \imath ^ { q } = q \beta ^ { q - 1 } \qquad \quad \mathrm { f o r } q = 0 , 1 , \ldots , p _ { D } } } \\ { { \displaystyle \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \imath ^ { q } = \beta ^ { q } \qquad \quad \mathrm { f o r } q = 0 , \ldots , p _ { I } . } } \end{array}
$$

Compare this result with Theorem II1.2.4.

b) Compute the orders $p _ { D }$ and $p _ { I }$ for the Adams methods.

2. a) Show that the one-leg method (6.6) can be written in the form of a general linear method (Sect. III.8).

b)Prove that the order of convergence $p$ of this method is given by

$$
p = \operatorname* { m i n } ( p _ { D } , p _ { I } + 1 )
$$

with $p _ { D } , p _ { I }$ defined in (6.39).

c) The order of a one-leg method is never larger than the order of the corre-sponding multistep method.

3. (Dahlquist 1975).

a) Let $\{ y _ { m } \}$ and $\{ x _ { m } = x _ { 0 } + m h \}$ satisfy the (one-leg) difference relation (6.6); then

$$
\widehat { y } _ { m } = \sum _ { j = 0 } ^ { k } \beta _ { \jmath } y _ { m + j } , \qquad \widehat { x } _ { m } = \sum _ { \jmath = 0 } ^ { k } \beta _ { \jmath } x _ { m + \jmath }
$$

satisfy the (linear multistep) difference relation (6.3).

b) Conversely, let

$$
P ( \zeta ) = \sum _ { j = 0 } ^ { k - 1 } a _ { j } \zeta ^ { j } , \qquad Q ( \zeta ) = \sum _ { j = 0 } ^ { k - 1 } b _ { _ { j } } \zeta ^ { j }
$$

be such that $P ( \zeta ) \sigma ( \zeta ) - Q ( \zeta ) \varrho ( \zeta ) = \zeta ^ { l }$ for some integer $l$ $( 0 \leq l \leq k )$ , then

$$
\begin{array} { l } { \displaystyle { y _ { m + l } = \sum _ { j = 0 } ^ { k - 1 } a _ { j } \widehat { y } _ { m + { _ j } } - h \sum _ { j = 0 } ^ { k - 1 } b _ { j } f \big ( \widehat { x } _ { m + { _ j } } , \widehat { y } _ { m + { _ j } } \big ) } } \\ { \displaystyle { x _ { m + l } = \sum _ { j = 0 } ^ { k - 1 } a _ { j } \widehat { x } _ { m + { _ j } } - h \sum _ { j = 0 } ^ { k - 1 } b _ { j } } } \end{array}
$$

satisfy (6.6), whenever $\{ \widehat { y } _ { m } \}$ and $\{ \widehat { x } _ { m } \}$ are a solution of (6.3).

Hint for $a$ ). Multiply (6.6) by $\beta _ { j }$ ,replace $_ m$ by $m + j$ , sum from $j = 0$ to $j = k$ ,and interchange the summations.

4. One-leg collocation methods (Dahlquist 1983).

a) For a given $\beta$ there exists a unique $k$ -step one-leg method with $p _ { D } = k$ and $p _ { I } = k$

b) This one-leg method is of order $p = k + 1$ iff

$$
\sum _ { \ i = 0 } ^ { k } { \frac { 1 } { ( \beta - i ) } } = 0 .
$$

c) Discuss numerically the zero-stability of these methods.

5. (proposed by M. Crouzeix). a) Let $R ( z ) = P ( z ) / Q ( z )$ be an irreducible rational function where deg $P \leq k$ ，deg $Q \leq k$ . Show that $R ( z )$ is $A$ -stable, if and only if there exist polynomials $\alpha _ { \ i } ( z ) , \beta ( z )$ with real coefficients and with deg $\alpha _ { i } \leq k - 1$ ， $\deg \beta \leq k$ ,such that

$$
Q ( z ) Q ( w ) - P ( z ) P ( w ) = - ( z + w ) \sum _ { i = 1 } ^ { k } \alpha _ { i } ( z ) \alpha _ { i } ( w ) + \beta ( z ) \beta ( w ) .
$$

b) Use this characterization to give a new proof of von Neumann's theorem (Corollary IV.11.3).

Hint. Part (a) can be proved along the lines of the proofs of Theorem 6.7 and Lemma 6.8. Remark that (6.55) reduces to the $E$ -polynomial (IV.3.8) if $z = i y$ and $w = - i y$ . For the proof of (b), deduce from (6.55) the identity

$$
\| Q ( A ) u \| ^ { 2 } - \| P ( A ) u \| ^ { 2 } = - \sum _ { i = 1 } ^ { k } \mathrm { { R e } } \left. \alpha _ { \ i } ( A ) u , A \alpha _ { \ i } ( A ) u \right. + \| \beta ( A ) u \| ^ { 2 } .
$$

# V.7 Convergence for Linear Problems

Theorems 6.10 and 6.11 give satisfactory convergence results for $G$ -stable one-leg methods and $A$ -stable multistep methods. But there are only few such methods and their highest order is two (Theorem 1.4). It is therefore interesting to relax the requirement of $A$ -stability and to investigate higher-order multistep and one-leg methods. This section is devoted to linear stiff problems,while Sect. V.8 will treat non-linear problems.

We shall describe two different approaches for convergence results. One is with the help of the discrete variation of constants formula and shall be given at the end of this section (see Lemma 7.9 and Theorem 7.10 below). The other possibility is based on a formulation as a one-step method and on the use of the Kreiss matrix theorem.

# Difference Equations for the Global Error

Most of the difculties can already be seen by studying the one-dimensional problem of Prothero and Robinson

$$
y ^ { \prime } = \lambda y + g ( x ) , \qquad y ( x _ { 0 } ) = y _ { 0 } .
$$

We assume $\operatorname { R e } \lambda \leq 0$ and the solution $y ( x )$ to be smooth in the sense that sufficiently many derivatives are bounded independently of the stiffness parameter $\lambda$ .

Applying a linear multistep method to (7.1) yields

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { m + \imath } = h \lambda \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { m + i } + h \sum _ { i = 0 } ^ { k } \beta _ { i } g ( x _ { m + i } ) .
$$

The global error

$$
e _ { m } = y _ { m } - y \big ( x _ { m } \big )
$$

is seen to satisfy the difference relation

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { i } - h \lambda \beta _ { i } ) e _ { m + i } = - \delta _ { L M } ( x _ { m } )
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $\mathit { I I }$ ， Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_22, $©$ Springer-Verlag Berlin Heidelberg 2010

with

$$
\delta _ { L M } ( x ) = \sum _ { i = 0 } ^ { k } \alpha _ { , } y ( x + i h ) - h \sum _ { i = 0 } ^ { k } \beta _ { , } y ^ { \prime } ( x + i h )
$$

(to be compared with Formula II.2.3).We observe that the right-hand side of (7.4) is independent of the stiffness (i.e., of $\lambda$ ). Further, if the classical order of the method is $p$ ,then $\delta _ { L M } ( x ) = \mathcal { O } ( h ^ { p + 1 } )$

If we apply the method in its one-leg version, we obtain

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { i } y _ { m + \imath } = h \lambda \sum _ { i = 0 } ^ { k } \beta _ { \imath } y _ { m + \imath } + h g ( x _ { m } + \beta h ) ,
$$

where $\sum \beta _ { \imath } = 1$ and $\sum \beta _ { i } i = \beta$ . In this case the global error $e _ { m } = y _ { m } - y \big ( x _ { m } \big )$ satisfies

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { i } - h \lambda \beta _ { i } ) e _ { m + i } = h \lambda \delta _ { I } ( x _ { m } ) - \delta _ { D } ( x _ { m } )
$$

with $\delta _ { D } ( x )$ and $\delta _ { I } ( x )$ defined in (6.37) and (6.38),respectively. Unless $\delta _ { \bar { \cal I } } ( x ) = 0$ (which is the case for the BDF methods), Eq.(7.7) is disappointing,because its right-hand side becomes large in the stiff case $( h \lambda  \infty )$

In order to overcome this difficulty, Dahlquist (1983) proposes that one con-sider instead of $e _ { m } = y _ { m } - y \big ( x _ { m } \big )$ the quantities

$$
e _ { m } ^ { * } = \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { m + \imath } - y ( x _ { m } + \beta h )
$$

("... a more adequate measure of the global error than the customary one ...", Dahlquist 1983). Replacing $m$ by $m + j$ in (7.6), multiplying by $\beta _ { \jmath }$ and summing up gives the error formula

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { i } - h \lambda \beta _ { i } ) e _ { m + i } ^ { * } = - \delta _ { L M } ( x _ { m } + \beta h )
$$

with $\delta _ { L M } ( x )$ of (7.5). This difference relation now has the same strength as (7.4).

It has been pointed out by Hundsdorfer & Steininger (1991) that we usually get beter error estimates for one-leg methods by considering $\widehat { e } _ { m } = e _ { m } + \delta _ { I } ( x _ { m } )$ We then have

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { \iota } - h \lambda \beta _ { i } ) \widehat { e } _ { m + \iota } = h \lambda \widehat { \varepsilon } ( x _ { m } ) - \widehat { \delta } ( x _ { m } )
$$

with ${ \widehat { \varepsilon } } ( x )$ and $\widehat { \delta } ( x )$ given by (6.47). Observe that ${ \widehat { \varepsilon } } ( x ) = { \mathcal { O } } ( h ^ { p _ { I } + 2 } )$ and $\widehat { \delta } ( x ) =$ $\mathcal { O } \big ( h ^ { \operatorname* { m i n } ( p _ { D } + 1 , p _ { I } + 2 } \big )$ .

Formulation as a One-Step Method. The error relations (7.4). (7.7), (7.9), and (7.10) are all of the form

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - h \lambda \beta _ { i } ) c _ { m + \imath } = \delta _ { h } ( \boldsymbol { \cdot } \boldsymbol { \tau _ { m } } ) .
$$

In order to estimate $e _ { m }$ it is convenient to introduce, as in Sect. II.4,the vector

$$
E _ { m } = ( e _ { m + k - 1 } , \cdot \cdot \cdot , e _ { m + 1 } , \epsilon _ { m } ) ^ { T } ,
$$

the companion matrix

$$
C ( \mu ) = \left( \begin{array} { c c c c } { { c _ { k - 1 } ( \mu ) } } & { { \dots } } & { { c _ { 1 } ( \mu ) } } & { { c _ { 0 } ( \mu ) } } \\ { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { 0 } } \end{array} \right) , \quad c _ { j } ( \mu ) = - \frac { \alpha _ { j } - \mu \beta _ { j } } { \alpha _ { k } - \mu \beta _ { k } }
$$

and

$$
\Delta _ { m } = \big ( \delta _ { h } ( x _ { m } ) / ( \alpha _ { k } - \mu \beta _ { k } ) , 0 , \dots , 0 \big ) ^ { T } , \qquad \mu = h \lambda .
$$

Then,Eq.(7.11) becomes

$$
\begin{array} { r } { E _ { m + 1 } = C ( h \lambda ) E _ { m } + \Delta _ { m } , } \end{array}
$$

which leads to

$$
E _ { m + 1 } = C ( h \lambda ) ^ { m + 1 } E _ { 0 } + \sum _ { \jmath = 0 } ^ { m } C ( h \lambda ) ^ { m - \jmath } \Delta _ { \jmath } .
$$

To estimate $E _ { m + 1 }$ we have to bound the powers of $C ( h \lambda )$ uniformly in $h \lambda$ . This is the subject of the next subsection.

# The Kreiss Matrix Theorem

Als Fakultatsopponent fiuir meine Stockholmer Dissertation brachte Dr. G.Dahlquist die Frage der Stabilitatsdefinition zur Sprache.

(H.-O. Krciss 1962)

The following Theorem of Kreiss (1962) is a powerful tool for proving uniform power boundedness of an arbitrary family of matrices.

Theorem 7.1 (Kreiss 1962). Let $\mathcal { F }$ be $a$ family of $k \times k$ matrices $\mathcal { A }$ .Then the "power condition"

$$
\| A ^ { n } \| \leq M \qquad f o r \quad n = 0 , 1 , 2 , \dots \quad a n d \quad A \in { \mathcal { F } }
$$

is equivalent to the “resolvent condition”

$$
\| ( A - z I ) ^ { - 1 } \| \leq { \frac { C } { | z | - 1 } } \qquad f o r \quad | z | > 1 \quad a n d \quad A \in { \mathcal { F } } .
$$

Remark. The difficult step is to prove that $( R )$ implies $( P )$ . Several mathematicians contributed to a better understanding of this result (Richtmyer & Mrton 1967,Tadmor 1981). LeVeque & Trefethen (1984) have given a marvellous ver-sion of the proof; the best we can do is to copy it nearly word for word:

Proof. Necessity. If $( P )$ is true, the eigenvalues of $A$ lie within the closed unit disk and therefore $\left( A - z I \right) ^ { - 1 }$ exists for $| z | > 1$ . Moreover,

$$
\lVert ( A - z I ) ^ { - 1 } \rVert = \lVert \sum _ { n = 0 } ^ { \infty } A ^ { n } z ^ { - n - 1 } \rVert \leq M \sum _ { n = 0 } ^ { \infty } | z | ^ { - n - 1 } = { \frac { M } { | z | - 1 } } ,
$$

so that $( R )$ holds with $C = M$

Sufficiency. Assume condition $( R )$ ，so that all eigenvalues of $A$ lie inside the closed unit disk. The matrix $A ^ { n }$ can then be writen in terms of the resolvent by means of a Cauchy integral (see Exercise 1)

$$
A ^ { n } = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } z ^ { n } ( z I - A ) ^ { - 1 } d z ,
$$

where the contour of integration is, for example, a circle of radius $\varrho > 1$ centred at the origin. Let $u$ and $v$ be arbitrary unit vectors, i.e., $\left\| u \right\| = \left\| v \right\| = 1$ . Then,

$$
v ^ { * } A ^ { n } u = \frac { 1 } { 2 \pi i } \int _ { \Gamma } z ^ { n } q ( z ) d z \qquad \mathrm { w i t h } \qquad e ( z ) = v ^ { * } ( z I - A ) ^ { - 1 } u .
$$

Integration by parts gives

$$
v ^ { * } A ^ { n } u = \frac { - 1 } { 2 \pi i ( n + 1 ) } \int _ { \Gamma } z ^ { n + 1 } q ^ { \prime } ( z ) d z .
$$

Now fix as contour of integration the circle of radius $\varrho = 1 + 1 / ( n + 1 )$ . On this path one has $| z ^ { n + 1 } | \leq e$ , and therefore

$$
\left| v ^ { \ast } A ^ { n } u \right| \leq \frac { e } { 2 \pi ( n + 1 ) } \int _ { \Gamma } | q ^ { \prime } ( z ) | \left| d z \right| .
$$

By Cramer's rule, $q ( z )$ is a rational function of degree $k$ . Applying Lemma 7.2 below, the integral in (7.19) is bounded by $4 \pi k$ times the supremum of $| q ( z ) |$ on $\Gamma$ , and by $( R )$ this supremum is at most $( n + 1 ) C$ . Hence

$$
\left| v ^ { * } A ^ { n } u \right| \leq 2 e k C .
$$

Since $\| A ^ { n } \|$ is the supremum of $\{ v ^ { * } A ^ { n } u \}$ over all unit vectors $u$ and $v$ , this proves the estimate $( P )$ with $M = 2 e k C$ □

The above proof used the following lemma, which relates the arc length of a rational function on a circle to its maximum value. For the case of a polynomial of degree $k$ the result is a corollary of Bernstein's inequality $\begin{array} { r } { \operatorname* { s u p } _ { | z | = 1 } | q ^ { \prime } ( z ) | \leq } \end{array}$ $k \operatorname* { s u p } _ { | z | = 1 } | q ( z ) |$ (see e.g., Marden 1966).

Lemma 7.2. Let $q ( z ) = p ( z ) / r ( z )$ be a rational function with deg $p \leq k$ ， $\mathrm { d e g } \ r \le k$ and suppose that no poles lie on the circle $\Gamma : | z | = \varrho$ . Then

$$
\int _ { \Gamma } | q ^ { \prime } ( z ) | | d z | \leq 4 \pi k \operatorname * { s u p } _ { | z | = \varrho } | q ( z ) | .
$$

Proof. Replacing $q ( z )$ by $q ( \varrho z )$ we may assume without loss of generality that $\varrho \approx 1$ . With the parametrization $e ^ { \imath t }$ of $\Gamma$ we introduce

$$
\begin{array} { r } { \gamma ( t ) = q ( e ^ { \imath t } ) , \qquad \gamma ^ { \prime } ( t ) = i e ^ { \imath t } q ^ { \prime } ( e ^ { \imath t } ) } \end{array}
$$

so that

$$
\gamma ^ { \prime } ( t ) = | q ^ { \prime } ( e ^ { \imath t } ) | \cdot e ^ { \imath g ( t ) } \qquad \mathrm { w i t h } \quad g ( t ) = \arg ( \gamma ^ { \prime } ( t ) ) .
$$

Integration by parts now yields

$$
\begin{array} { r l } & { \displaystyle \int _ { \Gamma } | q ^ { \prime } ( z ) | | d z | = \int _ { 0 } ^ { 2 \pi } | q ^ { \prime } ( c ^ { \prime } { } ^ { t } ) | d t = \int _ { 0 } ^ { 2 \pi } \gamma ^ { \prime } ( t ) e ^ { - \imath g ( t ) } d t } \\ & { \quad \quad \quad = \imath \displaystyle \int _ { 0 } ^ { 2 \pi } \gamma ( t ) g ^ { \prime } ( t ) e ^ { - \imath g ( t ) } d t \le \exp | \gamma ( t ) | \cdot \displaystyle \int _ { 0 } ^ { 2 \pi } | g ^ { \prime } ( t ) | d t . } \end{array}
$$

It remains to prove that the total variation of $g$ ,i.e., $\begin{array} { r } { \mathrm { T V } [ g ] = \int _ { 0 } ^ { 2 \pi } | g ^ { \prime } ( t ) | d t } \end{array}$ , can be bounded by $4 \pi k$ . To prove this, note that $z q ^ { \prime } ( z )$ is a rational function of degree $( 2 k , 2 k )$ and can be written as a product

$$
z q ^ { \prime } ( z ) = \prod _ { \jmath = 1 } ^ { 2 k } \frac { a _ { \jmath } z + b _ { \jmath } } { c _ { \jmath } z + d _ { \jmath } } .
$$

This implies for $z = e ^ { \imath t }$

$$
g ( t ) = \arg ( \imath z q ^ { \prime } ( z ) ) = \frac { \pi } { 2 } + \sum _ { \jmath = 1 } ^ { 2 k } \arg \Big ( \frac { a _ { \jmath } z + b _ { \jmath } } { c _ { \jmath } z + d _ { \jmath } } \Big ) .
$$

Since the Mobius transformation $( a z + b ) / ( c z + d )$ maps the unit circle to some other circle, the total variation of $\arg ( ( a \Im + b ) / ( c z + d ) )$ is at most $2 \pi$ . Consequently,

$$
\mathbf { T V } [ g ] \leq \sum _ { j = 1 } ^ { 2 k } \mathbf { T V } \left[ \operatorname { a r g } \Big ( \frac { a _ { j } z + b _ { j } } { c _ { j } z + d _ { j } } \Big ) \right] \leq 4 \pi k .
$$

Remark. It has been conjectured by LeVeque & Trefethen (1984) that the bound (7.20) is valid with a factor $2 \pi$ instead of $4 \pi$ . This conjecture has been proved to be true by Spijker (1991).

# Some Applications of the Kreiss Matrix Theorem

Following Dahlquist, Mingyou & Le Veque (1983) we now obtain some results on the uniform power boundedness of the matrix $C ( \mu )$ ,defined in (7.13), with the help of the Kreiss matrix theorem. Similar results were found independently by Crouzeix & Raviart (1980) and Gekeler (1979,1984).

Lemma 7.3. Let $S \subset { \overline { { \mathbb { C } } } }$ denote the stability region of a method $( \varrho , \sigma )$ .1f $S$ is closed in $\overrightarrow { \mathbb { C } }$ , then there exists a constant $M$ such that

$$
\| C ( \mu ) ^ { n } \| \leq M \qquad f o r \quad \mu \in S \qquad a n d \quad n = 0 , 1 , 2 , \ldots .
$$

Proof. Because of Theorem 7.1 it is sufficient to prove that

$$
\| ( C ( \mu ) - z I ) ^ { - 1 } \| \leq { \frac { C } { | z | - 1 } } \qquad { \mathrm { f o r } } \quad \mu \in S \quad { \mathrm { a n d } } \quad | z | > 1 .
$$

To show this, we make use of the inequality (Kato (1960),see Exercise 2)

$$
\| ( C ( \mu ) - z I ) ^ { - 1 } \| \leq { \frac { ( \| C ( \mu ) \| + | z | ) ^ { k - 1 } } { | \ * \mathrm { d e t } ( C ( \mu ) - z I ) | } } .
$$

$\vert \vert C ( \mu ) \vert \vert$ is uniformly bounded for $\mu \in S$ . Therefore it suffices to show that

$$
\varphi ( \mu ) = \operatorname* { i n f } _ { | z | > 1 } \frac { | \operatorname* { d e t } ( C ( \mu ) - z I ) | } { | z | ^ { k - 1 } ( | z | - 1 ) }
$$

is bounded away from zero for all $\mu \in S$ .For $| z |  \infty$ the expression in (7.21) tends to 1 and so poses no problem. Further, observe that

$$
{ \big | } \operatorname* { d e t } ( C ( \mu ) - z I ) { \big | } = { \Big | } \prod _ { \jmath = 1 } ^ { k } ( z - \zeta _ { \jmath } ( \mu ) ) { \Big | } ,
$$

where $\zeta _ { \jmath } ( \mu )$ are the eigenvalues of $C ( \mu )$ ,i.e., the roots of

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - \mu \beta _ { \imath } ) \zeta ^ { \imath } = 0 .
$$

By definition of the stability region $S$ ， the values $\zeta _ { \jmath } ( \mu )$ lie,for $\mu \in S$ , inside the closed unit disc and those on the unit circle are well separated. Therefore, for fixed $\mu _ { 0 } \in S$ , only one of the $\zeta _ { \jmath } ( \mu _ { 0 } )$ can be close to a $z$ with $| z | > 1$ . The corresponding factor in (7.22) will be minorized by $| z | - 1$ , the other factors are bounded away from zero. By continuity of the $\zeta _ { \jmath } ( \mu )$ , the same holds for all $\mu \in S$ in a sufficiently small neighbourhood $V ( \mu _ { 0 } )$ of $\mu _ { 0 }$ .Hence $\varphi ( \mu ) \geq a > 0$ for $\mu \in V ( \mu _ { 0 } ) \cap S$ . Since $S$ is closed (compact in $\mathbf { \overline { { C } } }$ ) it is covered by a finite number of $V ( \mu _ { 0 } )$ . Consequently $\varphi ( \mu ) \geq a > 0$ for all $\mu \in S$ , which completes the proof of the theorem. □

Remark. The hypothesis $^ { \cdot } S$ is closed in $\overline { { \mathbb { C } } } ^ { \mathrm { , , } }$ is usually satisfied. For methods which do not satisfy this hypothesis (see e.g.,Exercise 2 of Sect. V.1 or Dahlquist, Mingyou & LeVeque (1981)） the above lemma remains valid on closed subsets $D \subset { \overline { { S } } } \subset { \overline { { \mathbb { C } } } }$

The estimate of this lemma can be improved, if we consider closed sets $D$ lying in the interior of $S$ .

Lemma 7.4. Let $S$ be the stability region of a method $( \varrho , \sigma )$ .If $D \subset \operatorname { I n t } S$ is closed in $\overline { { \mathbb { C } } }$ ， then there exist constants $M$ and $\kappa \left( 0 < \kappa < 1 \right)$ ）such that

$$
\| C ( \mu ) ^ { n } \| \leq M \kappa ^ { n } \qquad f o r \quad \mu \in D \quad a n d \quad n = 0 , 1 , 2 , \ldots .
$$

Proof. If $\mu$ lies in the interior of $S$ ,all roots of (7.23) satisfy $\vert \zeta _ { \jmath } ( \mu ) \vert < 1$ (maximum principle). Since $D$ is closed, this implies the existence of $\varepsilon > 0$ Such that

$$
D \subset S _ { \varepsilon } = \{ \mu \in { \overline { { \mathbb { C } } } } ; | \zeta _ { j } ( \mu ) | \leq 1 - 2 \varepsilon , j = 1 , \ldots , k \} .
$$

We now consider $R ( \mu ) = \kappa ^ { - 1 } C ( \mu )$ with $\kappa = 1 - \varepsilon$ . The eigenvalues of $R ( \mu )$ satisfy $| \kappa ^ { - 1 } \zeta _ { \ j } ( \mu ) | \leq ( 1 - 2 \varepsilon ) / ( 1 - \varepsilon ) < 1 - \varepsilon$ for $\mu \in S _ { \varepsilon }$ . As in the proof of Lemma 7.3 (more easily, because $R ( \mu )$ has no eigenvalues of modulus 1） we conclude that $R ( \mu )$ is uniformly power bounded for $\mu \in S _ { \varepsilon }$ . This implies the statement.□

Since the origin is never in the interior of $S$ , we add the following estimate for its neighbourhood:

Lemma 7.5. Suppose that the method $( \varrho , \sigma )$ is consistent and strictly stable (see Sect. II.9, Assumption A1). Then there exists $a$ neighbourhood $V$ of O and constants $M$ and $a$ such that

$$
\| C ( \mu ) ^ { n } \| \leq M e ^ { n ( \operatorname { R e } \mu + a | \mu | ^ { 2 } ) } \qquad \quad f o r \quad \mu \in V \quad a n d \quad n = 0 , 1 , 2 , \ldots .
$$

Proof. Since the method is strictly stable there exists a compact neighbourhood $V$ of $0$ , in which $\vert \zeta _ { 1 } ( \mu ) \vert < \vert \zeta _ { 1 } ( \mu ) \vert$ for $j = 2 , \ldots , k \ ( \zeta _ { \jmath } ( \mu )$ are the roots of (7.23)). The matrix $R ( \mu ) { } = \zeta _ { 1 } ( \mu ) ^ { - 1 } C ( \mu )$ then has a simple eigenvalue 1 and all other eigenvalues are strictly smaller than 1. As in the proof of Lemma 7.3 we obtain $\| R ( \mu ) ^ { n } \| \leq M$ and consequently $\| C ( \mu ) ^ { n } \| \leq M | \zeta _ { 1 } ( \mu ) | ^ { n }$ for $\mu \in V$ . The stated estimate now follows from $\zeta _ { 1 } ( \mu ) = e ^ { \mu } + \mathcal { O } ( \mu ^ { 2 } )$ □

# Global Error for Prothero and Robinson Problem

The above lemmas permit us to continue our analysis of Eq.(7.16). Whenever we consider $\lambda$ and $h$ such that their product $\lambda h$ varies in a closed subset of $S$ ，it follows that

$$
\| E _ { m + 1 } \| \leq M \Big ( \| E _ { 0 } \| + \sum _ { \jmath = 0 } ^ { m } \| \Delta _ { \jmath } \| \Big )
$$

(Lemma 7.3). If $h \lambda$ varies in a closed subset of the interior of $S$ ，we have the better estimate

$$
\| E _ { m + 1 } \| \leq M \Bigl ( \kappa ^ { m + 1 } \| E _ { 0 } \| + \sum _ { \jmath = 0 } ^ { m } \kappa ^ { m - \jmath } \| \Delta _ { \jmath } \| \Bigr ) \qquad \mathrm { w i t h ~ s o m e } \kappa < 1
$$

(Lemma 7.4). The resulting asymptotic estimates for the global errors $e _ { m } = y _ { m } -$ $y ( x _ { m } )$ for $m h \le C o n s t$ are presented in Table 7.1 ( $p$ denotes the classical order, $p _ { D }$ the differentiation order and $p _ { I }$ the interpolation order of Sect. V.6). We as-sume that the initial values are exact and that simultaneously $h \lambda  \infty$ and $h  0$ This is the most interesting situation because any reasonable method for stiff problems should integrate the equation with step sizes $h$ such that $h \lambda$ is large. We distinguish two cases:

(A） the half-ray $\{ h \lambda ; h > 0 , | h \lambda | \ge c \} \cup \{ \infty \}$ lies in $S$ (Lemma 7.3 is applicable, i.e.,Eq. (7.24)).   
(B) $\infty$ is an interior point of $S$ (estimate (7.25) is applicable; the global error $\{ \{ E _ { m } \} \}$ is essentially equal to the last term in the sum of (7.25)).

Table 7.1. Error for(7.1） when $h \lambda  \infty$ and $h  0$   

<table><tr><td>Method</td><td>error</td><td>（A)</td><td>(B)</td></tr><tr><td>multistep</td><td>em</td><td>O(x1-1hP-1）</td><td>O(x1-1hp)</td></tr><tr><td>one-leg</td><td>em</td><td>O(hP1+1+1x1-1hPD-1)</td><td>O(hp1+1 +1λ1-1hPD)</td></tr></table>

We remark that the global error of the multistep method contains a factor $| \lambda | ^ { - 1 }$ ， so that the error decreases if $| \lambda |$ increases ("the stiffer the better"). The estimate in case (A) for one-leg methods is obtained by the use of Recursion (7.10).

# Convergence for Linear Systems with Constant Coeficients

The extension of the above results to linear systems

$$
y ^ { \prime } = A y + g ( x ) , \qquad y ( x _ { 0 } ) = y _ { 0 }
$$

is straightforward,if we assume that the matrix $A$ is diagonalizable. The following results have been derived by Crouzeix & Raviart (1980).

Theorem 7.6. Suppose that the multistep method $( \varrho , \sigma )$ is of order $\boldsymbol { \underline p }$ ， $A { \big ( } \epsilon \varepsilon { \big ) }$ -stable and stable at infinity. If the matrix $A$ of (7.26) is diagonalizable ( $i . e . , \ T ^ { - 1 } A T =$ diag $\left( \lambda _ { 1 } , \ldots , \lambda _ { n } \right) ,$ )with eigenvalues satisfying

$$
| \arg ( - \lambda _ { \iota } ) | \leq \alpha \qquad f o r \quad \iota = 1 , \ldots , n ,
$$

then there exists a constant $\mathcal { M }$ (depending only on the method) such that for all $h > 0$ the global error satisfies

$$
\| y ( x _ { m } ) - y _ { m } \| \leq M \cdot \| T \| \cdot \| T ^ { - 1 } \| \left( \operatorname* { m a x } _ { 0 \leq j < k } \| y ( x _ { j } ) - y _ { j } \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \right) .
$$

Proof. The transformation $y = T z$ decouples the system (7.26) into $n$ scalar equations

$$
z _ { \imath } ^ { \prime } = \lambda _ { \imath } z _ { \imath } + ( T ^ { - 1 } g ) _ { \imath } ( x ) .
$$

Since this transformation leaves the numerical solution invariant, it suffices to consider Eq.(7.27). Lemma 7.3 yields the power boundedness

$$
| | C ( h \lambda _ { \ i } ) ^ { m } | | \leq M _ { 0 } \qquad { \mathrm { f o r } } \quad h > 0 , \quad i = 1 , \ldots , n \quad { \mathrm { a n d } } \quad m \geq 0 .
$$

The discretization error $\delta _ { L M } ( x )$ (Eq.(7.5)) can be writen as

$$
\delta _ { L M } ( x ) = h ^ { p + 1 } \int _ { 0 } ^ { k } K _ { p } ( s ) z _ { i } ^ { ( p + 1 ) } ( x + s h ) d s ,
$$

where $K _ { p } ( s )$ is the Peano-kernel of the multistep method (Thcorem II.2.8). By $A ( \alpha )$ -stability we have $\alpha _ { k } \cdot \beta _ { k } > 0$ ，so that $| \alpha _ { k } - / { \lambda } _ { 2 } / { \beta } _ { k } | ^ { - 1 } \leq | \alpha _ { k } | ^ { - 1 }$ . This together with (7.29) implies that

$$
\| \Delta _ { \jmath } \| \leq C h ^ { p } \int _ { x _ { \jmath } } ^ { x _ { \jmath + k } } | z _ { \imath } ^ { ( p + 1 ) } ( \xi ) | d \xi ,
$$

where $C$ depends only on the method. The estimates (7.28） and (7.30) inserted into (7.16) yield a bound for the global error of (7.27).which,by backsubstitution into the original variables, proves the statement. □

Because of its exponentially decaying terin, the following estimate is especially useful in the case when large time intervals are considered (or when the starting values do not lie on the exact solution).

Theorem 7.7. Let the multistep method $( \varrho , \sigma )$ be of order $p \geq 1$ ， $A ( \alpha )$ -stable and strictly stable at zero and at infinity $( i . e . , \ \sigma ( \zeta ) = 0$ implies $| \zeta | < 1 )$ . If the matrix $A$ of (7.26) is diagonalizable $^ { \prime } T ^ { - 1 } A T = \mathrm { d i a g } \left( \lambda _ { 1 } , \ldots , \lambda _ { n } \right) ,$ ) with eigenvalues $\lambda _ { \iota }$ satisfying

$$
| \arg ( - \lambda _ { \iota } ) | \leq \gamma < \alpha , \qquad \mathrm { R e } \lambda _ { \iota } \leq - \widehat { \lambda } < 0
$$

then, for given $h _ { 0 } > 0$ , there exist constants $M$ and $\nu > 0$ such that for $0 < h \leq h _ { 0 }$

$$
\begin{array} { r l } & { \displaystyle \| y ( x _ { m } ) - y _ { m } \| \leq M \cdot \| T \| \cdot \| T ^ { - 1 } \| \cdot \Big ( e ^ { - \nu ( x _ { m } - x _ { 0 } ) } \cdot \operatorname* { m a x } _ { 0 \leq j < k } \| y ( x _ { j } ) - y _ { j } \| } \\ & { \qquad \quad + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } e ^ { - \nu ( x _ { m } - \xi ) } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \Big ) . } \end{array}
$$

Remark. The constants $M$ and $\nu$ may depend on $\gamma , \widehat { \lambda } , h _ { 0 }$ and on the method, but they are independent of the eigenvalues $\lambda _ { \iota }$ and of the length ${ x _ { m } } - { x _ { 0 } }$ of the integration interval.

Proof. By Lemma 7.5 there exists an $r > 0$ such that

$$
\begin{array} { r } { \| C ( h \lambda _ { \iota } ) ^ { m } \| \leq M _ { 0 } e ^ { - m h \widehat { \lambda } / 2 } \qquad \mathrm { ~ f o r ~ } \quad | h \lambda _ { \iota } | \leq r } \end{array}
$$

(observe that $\mu | \leq C o n s t \cdot | { \mathrm { R e } } \mu | , { \mathrm { i f ~ } } | \arg ( - \mu ) | \leq \gamma < \pi / 2 ) .$ Since

$$
D = \left\{ \mu \ ; \ \left| \ \arg ( - \mu ) \right| \leq \gamma , \ \left| \mu \right| \geq r \right\} \cup \left\{ \infty \right\}
$$

lies in the interior of the stability region $S$ , it follows from Lemma 7.4 that

$$
\begin{array} { r } { \| C ( h \lambda _ { \iota } ) ^ { m } \| \leq M _ { 1 } \varrho ^ { m } \qquad \mathrm { ~ f o r ~ } \quad | h \lambda _ { \iota } | \geq r } \end{array}
$$

with some $\varrho < 1$ . Combining the estimates (7.31) and (7.32) we get

$$
\| C ( h \lambda _ { \iota } ) ^ { m } \| \leq M e ^ { - m h \nu } \qquad \mathrm { ~ f o r ~ } \quad 0 < h \leq h _ { 0 } ,
$$

where $M = \operatorname* { m a x } ( M _ { 0 } , M _ { 1 } )$ and $\nu = \operatorname* { m i n } ( \widehat { \lambda } / 2 , - \ln \varrho / h _ { 0 } )$ .Using（7.33） instead of (7.28) and $m h = x _ { m } - x _ { 0 }$ , the statement now follows as in the proof of Theorem 7.6. □

# Matrix Valued Theorem of von Neumann

An interesting contractivity result is obtained by the following matrix valued ver-sion of a theorem of von Neumann (Theorem IV.11.2).

We consider the Euclidean scalar product $\langle \cdot , \cdot \rangle$ on $\mathbb { R } ^ { n }$ ,the norm $\| \cdot \| _ { G }$ on $\mathbb { R } ^ { k }$ which is defined by a symmetric, positiv definite matrix $G$ ,and

$$
\| u \| _ { G } = \sqrt { \sum _ { i , \ j = 1 } ^ { k } g _ { \iota _ { \ j } } \langle u _ { \iota } , u _ { \ j } \rangle } \qquad \mathrm { ~ f o r ~ } u = ( u _ { 1 } , \ j \cdot \cdot \cdot , u _ { k } ) ^ { T } \in \mathbb { R } ^ { n k } .
$$

The corresponding operator norms are denoted by the same symbols.

Theorem 7.8 (O. Nevanlinna 1985). Let $C ( \mu ) = ( c _ { \iota j } ( \mu ) ) _ { \iota , \jmath = 1 } ^ { k }$ be a matrix whose elements are rational functions of $\mu . \textit { I f }$

$$
\| C ( \mu ) \| _ { G } \leq 1 \qquad f o r \quad \operatorname { R e } \mu \leq 0 ,
$$

then

$$
\| C ( A ) \| _ { G } \leq 1
$$

for all matrices $A$ such that

$$
\operatorname { R e } { \langle y , A y \rangle } \leq 0 \qquad f o r \quad y \in \mathbb { C } ^ { n } .
$$

Remark. If $C ( \mu )$ is the companion matrix of a $G$ -stable method $( \varrho , \sigma )$ , the result follows from Theorem 6.7 and Exercise 3 below ("It would be interesting to have a more operator-theoretical proof of this.” Dahlquist & Soderlind 1982).

Proof. This is a straight-forward extension of Crouzeix's proof of Theorem IV.11.2. We first suppose that $A$ is normal, so that $A = Q D Q ^ { * }$ with a unitary matrix $Q$ and a diagonal matrix $D = \operatorname { d i a g } \left( \lambda _ { 1 } , . . . , \lambda _ { n } \right)$ . In this case we have

$$
\| C ( A ) \| _ { G } = \| ( I \otimes Q ) C ( D ) ( I \otimes Q ^ { \ast } ) \| _ { G } = \| C ( D ) \| _ { G } .
$$

With the permutation matrix $P = ( I \otimes e _ { 1 } , \ldots , I \otimes e _ { n } )$ (where $I$ is the $k$ -dimensional identity and $e _ { j }$ is the $\mathscr { n }$ -dimensional $j$ -th unit vector) the matrix $C ( D )$ is transformed to block-diagonal form according to

$$
P ^ { * } C ( D ) P = \mathrm { b l o c k d i a g } ( C ( \lambda _ { 1 } ) , \ldots , C ( \lambda _ { n } ) ) .
$$

We further have $P ^ { * } ( G \otimes I ) P = I \otimes G$ . This implies that

$$
P ^ { * } C ( D ) ^ { * } ( G \otimes I ) C ( D ) P = \mathrm { b l o c k d i a g } \left( C ( \lambda _ { 1 } ) ^ { * } G C ( \lambda _ { 1 } ) , \ldots \right)
$$

and hence also

$$
\| C ( D ) \| _ { G } = \operatorname* { m a x } _ { \iota = 1 , \ldots , n } \| C ( \lambda _ { \iota } ) \| _ { G } .
$$

The statement now follows from (7.38) and (7.39), because $\mathrm { R e } \lambda _ { \iota } \leq 0$ by (7.37).

For a general $A$ we consider $\begin{array} { r } { A ( \omega ) = \frac { \omega } { 2 } ( A + A ^ { * } ) + \frac { 1 } { 2 } ( A - A ^ { * } ) } \end{array}$ and define the rational function

$$
\varphi ( \omega ) = \langle u , C ( A ( \omega ) ) v \rangle _ { G } = u ^ { * } ( G \otimes I ) C ( A ( \omega ) ) v .
$$

The statement of the theorem can then be deduced exactly as in the proof of Theorem IV.11.2. □

This theorem can be used to derive convergence results for differential equations (7.26) with $A$ satisfying (7.37). Indeed, if the method $( \varrho , \sigma )$ is $A$ -stable, the companion matrix (7.13) satisfies $\| C ( \mu ) \| _ { G } \leq 1$ for $\mathrm { R e } \mu \leq 0$ in some suitable

norm (Exercise 3). The above theorem then implies $\| | C ( h A ) \| | _ { G } \leq 1$ and Formula (7.16) with $\lambda$ replaced by $A$ yields the estimate

$$
\| E _ { m + 1 } \| _ { G } \leq \| E _ { 0 } \| _ { G } + \sum _ { \jmath = 0 } ^ { m } \| \| \Delta _ { \jmath } \| _ { G } .
$$

This proves convergence, because $\Delta _ { _ { \jmath } }$ can be bounded as in (7.30).

# Discrete Variation of Constants Formula

A second approach to convergence results of linear multistep methods is by the use of a discrete variation of constants formula. This is an extension of the classical proofs for nonstiff problems (Dahlquist 1956,Henrici 1962) to the case $\mu \neq 0$ .It has been developed by Crouzeix & Raviart (1976),and more recently by Lubich (1988,1991).

We consider the error equation (cf. (7.13))

$$
\sum _ { \ i = 0 } ^ { k } ( \alpha _ { \ i } - \mu \beta _ { \ i } ) e _ { m + \ i } = d _ { m + k } \qquad { \mathrm { f o r } } \quad m \geq 0 ,
$$

and extend this relation to negative $r \gamma _ { \ell }$ by putting ${ \mathfrak { e } } _ { \mathfrak { g } } = 0$ (for $j < 0$ )and by defining $d _ { 0 } , \ldots , d _ { k - 1 }$ according to (7.41). The main idea is now to introduce the generating power series

$$
e \mathopen { } \mathclose \bgroup \left( \zeta \aftergroup \egroup \right) = \sum _ { \jmath \geq 0 } e _ { \jmath } \zeta ^ { \jmath } , \qquad d ( \zeta ) = \sum _ { \jmath \geq 0 } d _ { \jmath } \zeta ^ { \jmath }
$$

so that (7.41) becomes the $m$ -th coefficient of the identity

$$
\begin{array} { r } { \big ( \varrho ( \zeta ^ { - 1 } ) - \mu \sigma ( \zeta ^ { - 1 } ) \big ) e ( \zeta ) = \zeta ^ { - k } d ( \zeta ) . } \end{array}
$$

This gives

$$
\begin{array} { r } { e ( \zeta ) = \big ( \varrho ( \zeta ^ { - 1 } ) - \mu \sigma ( \zeta ^ { - 1 } ) \big ) ^ { - 1 } \zeta ^ { - k } d ( \zeta ) = r ( \zeta , \mu ) d ( \zeta ) } \end{array}
$$

and allows to compute casily $e _ { m }$ in terms of $d _ { j }$ as

$$
{ \mathfrak { e } } _ { m } = \sum _ { j = 0 } ^ { m } r _ { m - j } \left( \mu \right) d _ { j } .
$$

Here $r _ { j } \left( \mu \right)$ are the coefficients of the discrete resolvent

where

$$
r ( \zeta , \mu ) = \big ( \delta ( \zeta ) - \mu \big ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \sum _ { \jmath \geq 0 } r _ { \jmath } ( \mu ) \zeta ^ { \jmath } ,
$$

$$
\delta ( \zeta ) = \frac { \varrho ( \zeta ^ { - 1 } ) } { \sigma ( \zeta ^ { - 1 } ) } = \frac { \alpha _ { 0 } \zeta ^ { k } + . . . + \alpha _ { k - 1 } \zeta + \alpha _ { k } } { \beta _ { 0 } \zeta ^ { k } + . . . + \beta _ { k - 1 } \zeta + \beta _ { k } } .
$$

Since $( \varrho ( \zeta ^ { - 1 } ) - \mu \sigma ( \zeta ^ { - 1 } ) ) r ( \zeta , \mu ) = \zeta ^ { - k }$ , the coefficients ${ \bar { \boldsymbol { r } } } _ { j } \left( { \boldsymbol { \mu } } \right)$ can be interpreted as the numerical solution $y _ { j }$ of the multistep method applied to the homogeneous equation $y ^ { \prime } = \mu y$ with step size $\hslash = 1$ , and with starting valucs $y _ { - k + 1 } = \ldots =$ $y _ { - 1 } = 0$ ， $y _ { 0 } = ( \alpha _ { k } - \mu \beta _ { k } ) ^ { - 1 }$ ·

Formula (7.43'） can be used to estimate $\mathcal { C } _ { \mathfrak { M } }$ ，if appropriate bounds for the coeficients $r _ { \it _ { ? } } ( \mu )$ of the discrete resolvent are known. Such bounds are given in the following lemma.

Lemma 7.9. Let $S \subset \overline { { \mathbb { C } } }$ denote the stability region of the multistep method. $a )$ If $S$ is closed in $\overrightarrow { \mathbb { C } }$ then

$$
| r _ { \jmath } ( \mu ) | \leq { \frac { \mathcal { M } } { 1 + | \mu | } } \qquad f o r \quad \mu \in S \quad a n d \quad j = 0 , 1 , 2 , . . .
$$

$b$ ）if $D \subset \operatorname { I n t } S$ is closed in $\overrightarrow { \mathbb { C } }$ then there exists a constant $\kappa$ $( 0 < \kappa < 1 )$ such that

$$
\left| r _ { \jmath } ( \mu ) \right| \leq { \frac { M \kappa ^ { \jmath } } { 1 + | \mu | } } \qquad f o r \quad \mu \in D \quad a n d \quad j = 0 , 1 . 2 , . . .
$$

c) If the method is strictly stable then there exists a neighbourhood $\gamma$ of O such that

$$
\vert r _ { \ j } ( \mu ) \vert \leq M e ^ { \jmath ( \mathrm { R e } \mu + a \vert \mu \vert ^ { 2 } ) } \qquad \quad f o r \quad \mu \in V \quad a n d \quad \jmath = 0 , 1 , 2 , . . . .
$$

The constants $M , \kappa$ ,and $a$ are independent of $\jmath$ and $\mu$ ·

Proof. The estimates for $| r _ { j } ( \mu ) |$ in (a), (b),and (c) can easily be deduced from Lemmas 7.3, 7.4, and 7.5 because $r _ { j } \left( \mu \right)$ is the numerical solution for the problem $y ^ { \prime } = \mu y$ with step size $h \approx 1$ and starting values $y _ { - k + 1 } = \ l _ { \cdot } \ l _ { \cdot } = y _ { - 1 } = 0$ ， $y _ { 0 } =$ $( \alpha _ { k } - \mu \beta _ { k } ) ^ { - 1 }$ .

As noted by Crouzeix & Raviart (1976) and Lubich (1988) the estimates of Lemma 7.9 can be proved directly, without any use of the Kreiss matrix thcorem. We illustrate these ideas by proving statement (b) (for a proof of statement (a) see Exercise 4).

By definition of the stability region the function ${ \zeta ^ { k } ( \varrho ( \zeta ^ { - 1 } ) \cdots \mu \sigma ( \zeta ^ { - 1 } ) ) }$ does not vanish for $| \zeta | \le 1$ if $\mu \in \operatorname { I n t } S$ . Therefore there exists a $\kappa \left( 0 < \kappa , < 1 \right)$ such that $\zeta ^ { k } \big ( \varrho \big ( \zeta ^ { - 1 } \big ) - \mu \sigma \big ( \zeta ^ { - 1 } \big ) \big )$ has no zeros in the disk $| \zeta | \le 1 / \kappa$ . Hence, for $\mu \in D$

$$
\operatorname* { s u p } _ { | \zeta | \leq 1 / \kappa } | \big ( \varrho ( \zeta ^ { - 1 } ) - \mu \sigma ( \zeta ^ { - 1 } ) \big ) ^ { - 1 } \zeta ^ { - k } | \leq \frac { M } { 1 + | \mu | } ,
$$

and Cauchy's integral formula

$$
r _ { j } \left( \mu \right) = \frac { 1 } { 2 \pi \imath } \int _ { | \zeta | = \imath / \kappa } \left( \varrho ( \zeta ^ { - 1 } ) - \mu \sigma ( \zeta ^ { - 1 } ) \right) ^ { - 1 } \zeta ^ { - k } \zeta ^ { - \jmath - 1 } d \zeta
$$

yields the desired estimate.


<!-- chunk 0006: pages 351-420 -->
The use of the discrete resolvent allows elegant convergence proofs for linear multistep methods. We shall demonstrate this for the linear problem (7.26) where the matrix $A$ satisfies

$$
\| ( s I - A ) ^ { - 1 } \| \leq { \frac { M } { 1 + | s | } } \qquad { \mathrm { f o r } } \quad | \arg ( s - c ) | \leq \pi - \alpha ^ { \prime }
$$

with some $c \in \mathbb { R }$ ． This is a common assumption in the theory of holomorphic semigroups for parabolic problems (see e.g., Kato (1966) or Pazy (1983)). If all eigenvalues $\lambda _ { \iota }$ of $A$ satisfy $| \arg ( \lambda _ { \iota } - c ) - \pi | < \alpha ^ { \prime }$ then Condition (7.47) is satisfied with a constant $M$ depending on the matrix $A$ (Exercise 2). The following theorem,which was communicated to us by Ch. Lubich, is an improvement of results of Crouzeix & Raviart (1976).

Theorem 7.10. Let the multistep method be of order $p \geq 1$ ， $A ( \alpha )$ -stable and strictly stable at zero and at infinity. If the matrix $A$ of (7.26) satisfies (7.47) with $\alpha ^ { \prime } < \alpha$ , then there exist constants $C$ ， $h _ { 0 }$ ，and $\gamma \left\{ \gamma \right\}$ of the same sign as c in (7.47)), which depend only on $M , c , \alpha ^ { \prime }$ and the method, such that for $h \leq h _ { 0 }$ the global error satisfies

$$
\begin{array} { r l r } {  { \| y ( x _ { m } ) - y _ { m } \| } } \\ & { } & { \leq C \big ( e ^ { \gamma x _ { m } } \displaystyle \operatorname* { m a x } _ { 0 \leq \jmath < k } \| y ( x _ { \jmath } ) - y _ { \jmath } \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } e ^ { \gamma ( x _ { m } - \xi ) } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \big ) . } \end{array}
$$

Moreover, if $c \leq 0$ ,then $h _ { 0 }$ can be chosen arbitrarily.

Proof. The global error $e _ { m } = y ( x _ { m } ) - y _ { m }$ satisfies

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - h A \beta _ { i } ) e _ { m + \imath } = d _ { m + k }
$$

where

$$
\| d _ { m + k } \| \leq C h ^ { p } \int _ { x _ { m } } ^ { x _ { m + k } } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi , \qquad m \geq 0
$$

and $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the $e _ { \mathfrak { g } }$ and $h A e _ { j }$ with $j < k$ We split these expressions into

$$
d _ { \ell } = d _ { \ell } ^ { \prime } + h A d _ { \ell } ^ { \prime \prime } \qquad { \mathrm { f o r } } \quad \ell < k ,
$$

so that $d _ { \ell } ^ { \prime }$ and $d _ { \ell } ^ { \prime \prime }$ are linear combinations of the $e _ { \mathscr { j } } ^ { \mathrm { ~ ~ } } \left( \ j < k \right)$ only. We also put $d _ { \ell } ^ { \prime } = d _ { \ell }$ and $d _ { \ell } ^ { \prime \prime } = 0$ for $\ell \geq k$ . The analysis at the' beginning of this subsection (Eq.(7.43)) then shows that

$$
e \mathopen { } \mathclose \bgroup \left( \zeta \aftergroup \egroup \right) = r \mathopen { } \mathclose \bgroup \left( \zeta , h A \aftergroup \egroup \right) d ^ { \prime } ( \zeta ) + r \mathopen { } \mathclose \bgroup \left( \zeta , h A \aftergroup \egroup \right) h A d ^ { \prime \prime } ( \zeta ) ,
$$

where as in the scalar case

$$
r ( \zeta , h A ) = ( \delta ( \zeta ) I - h A ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \sum _ { \jmath \geq 0 } r _ { \jmath } ( h A ) \zeta ^ { \jmath } .
$$

We now apply Lemma 7.11 below with $\Phi ( s ) = ( s I - A ) ^ { - 1 }$ .By assumption the estimate(7.57) holds with $\beta = 1$ so that

$$
\| r _ { \jmath } ( h A ) \| \leq C e ^ { \gamma j h } .
$$

The second term in (7.49) can be written as

$$
r ( \zeta , h A ) h A ( \delta ( \zeta ) ) ^ { - 1 } \delta ( \zeta ) d ^ { \prime \prime } ( \zeta ) = r ^ { \prime } ( \zeta , h A ) \widehat { d } ( \zeta )
$$

where

$$
\begin{array} { r l r } {  { r ^ { \prime } ( \zeta , h A ) = ( \delta ( \zeta ) I - h A ) ^ { - 1 } h A ( \delta ( \zeta ) ) ^ { - 1 } \displaystyle \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \sum _ { \jmath \geq 0 } r _ { \jmath } ^ { \prime } ( h A ) \zeta ^ { \jmath } } } \\ & { } & { \widehat { d } ( \zeta ) = \delta ( \zeta ) d ^ { \eta } ( \zeta ) = \displaystyle \sum _ { \jmath \geq 0 } \widehat { d } _ { \jmath } \zeta ^ { \jmath } . } \end{array}
$$

We apply Lemma 7.11 again, this time to

$$
\Phi ( s ) = ( s I - A ) ^ { - 1 } A s ^ { - 1 } = ( s I - A ) ^ { - 1 } - s ^ { - 1 } I .
$$

Condition (7.57) is satisfied with $\beta = 1$ so that

$$
\| r _ { \jmath } ^ { \prime } ( / { a } A ) \| \leq C ^ { \prime } e ^ { \gamma \jmath h } .
$$

The coefficients $\delta _ { \jmath }$ of $\delta ( \zeta )$ are exponentially decaying because all zeros of $\sigma ( \zeta )$ lie in $\vert \zeta \vert < 1$ . Consequently, we have

$$
\| \widehat { d } _ { \boldsymbol { \jmath } } \| \leq \kappa ^ { \boldsymbol { \jmath } } \widehat { C } \operatorname* { m a x } _ { 0 \leq \ell < k } \| e _ { \ell } \|
$$

with some $\kappa _ { \mathrm { { s } } } < 1$ . The coeficient of $\zeta ^ { m }$ in (7.49) gives

$$
e _ { m } = \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ( h A ) d _ { \jmath } ^ { \prime } + \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ^ { \prime } ( h A ) \widehat { d } _ { \jmath } .
$$

Inserting the estimates (7.48), (7.51), (7.54),and (7.55) proves the statement.

We still have to prove the estimates for $r _ { \mathrm { \lambda _ { 1 } } } ( h A )$ and $r _ { j } ^ { \prime } ( h . A )$ . For this we let $\Phi ( s )$ be some analytic (scalar-, vector-, or matrix-valued function and consider the coefficients of

$$
\Phi \big ( \delta \big ( \zeta \big ) / h \big ) \cdot \frac { \zeta ^ { - k } } { \sigma \big ( \zeta ^ { - 1 } \big ) } = h \sum _ { \jmath \geq 0 } \varphi _ { \jmath } \big ( h \big ) \zeta ^ { \jmath } .
$$

We then have the following result.

Lemma 7.11 (Lubich 1991). Assume that the multistep method is $A ( \alpha )$ -stable and strictly stable at zero and at infinity. Further suppose that $\Phi ( s )$ is analytic in a sector $| \arg ( s - c ) | < \pi - \alpha ^ { \prime }$ with ${ \mathfrak { x } } ^ { \prime } < \alpha$ ， $c \in \mathbb { R }$ and there satisfies

$$
| | \Phi ( s ) | | \leq M \cdot | s | ^ { - \beta } \qquad f o r s o m e \quad \beta > 0 .
$$

Then the coefficients $\varphi _ { \jmath } ( h )$ of (7.56) are bounded for $h \leq h _ { 0 }$ (sufficiently small) by

$$
\| \varphi _ { \ j } ( h ) \| \leq C \cdot ( j h ) ^ { \beta - 1 } e ^ { \gamma \ j h } \qquad f o r \quad j \geq 1 ,
$$

and for $j = 0$ the same bound holds as for $j = 1$ . The constants $C , \gamma$ ,and $h _ { 0 }$ depend only on $\alpha ^ { \prime } , c , M , \beta$ ， and the multistep method. Moreover, if $c < 0$ , then also $\gamma < 0$ ， and the result holds for arbitrary $h _ { 0 }$

Proof.By $A ( \alpha )$ -stability we have $\beta _ { k } / \alpha _ { k } > 0$ ,so that $\delta ( 0 ) / h$ lies in the region of analyticity of $\Phi$ for $h \leq h _ { 0 }$ . Cauchy's integral formula thus gives

$$
\Phi ( \delta ( \zeta ) / h ) = \frac { 1 } { 2 \pi i } \int _ { \Gamma } ( \delta ( \zeta ) / h - \lambda ) ^ { - 1 } \Phi ( \lambda ) d \lambda
$$

where $\Gamma$ is a suitable contour from $^ { * * } \infty \cdot e ^ { -- i ( \pi - \alpha ^ { \prime } } ) ^ { " }$ to $^ { 6 6 } \infty \cdot e ^ { \imath ( \pi - \alpha ^ { \prime } ) ^ { 3 9 } }$ within the sector of analyticity of $\Phi$ and does not meet the origin (see Fig.7.1; observe that $\Phi ( s )$ decays suficiently rapidly at infinity). Multiplying (7.59) by $\zeta ^ { - k } / \sigma ( \zeta ^ { - 1 } )$ and comparing coefficients of equal powers of $\zeta$ yields the representation

$$
\varphi _ { j } ( h ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } r _ { \jmath } ( h \lambda ) \Phi ( \lambda ) d \lambda , \qquad j \geq 0 ,
$$

which is a discrete analogue of the Laplace inversion formula. We next substitute $\omega = j h \lambda$ (for $j = 0$ we put $\omega = h \lambda$ ) so that with $\Gamma _ { j } = j \boldsymbol { h } \cdot \boldsymbol { \Gamma }$ Eq.(7.60) becomes

$$
\varphi _ { \ j } ( h ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { \ j } } r _ { \ j } \left( { \frac { \omega } { j } } \right) \Phi \Big ( { \frac { \omega } { j h } } \Big ) { \frac { d \omega } { j h } } , \qquad j \geq 1 ,
$$

and the use of (7.57) yields

$$
\Vert \varphi _ { \ j } ( h ) \Vert \leq \frac { M } { 2 \pi } ( j h ) ^ { \beta - 1 } \int _ { \Gamma _ { \ j } } \left. r _ { j } \Big ( \frac { \omega } { j } \Big ) \right. \cdot \vert \omega \vert ^ { - \beta } \cdot \vert d \omega \vert .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/9cbb6ebcef9b8091f7d666dda28f44cb2c558a78278945216ff59fb0fe598f3f.jpg)  
Fig. 7.1. Contour $\Gamma$ in Formula (7.59)

We still have to show that the integral in (7.62) is bounded by $C \cdot e ^ { \gamma \ j h }$ .For this we split it into two parts: the first one corresponds to those $\omega$ such that $\omega / j$ lies in a closed subset of the interior of the stability domain of the method. There we can use Lemma $7 . 9 \mathrm { b }$ so that the corresponding part of the integral in (7.62) is bounded by

$$
j \cdot \kappa ^ { \jmath } \int | \omega | ^ { - \beta - 1 } | d \omega | \leq C e ^ { \gamma \jmath h } \qquad \mathrm { f o r } \quad h \leq h _ { 0 } .
$$

For the remaining part, the argument $\omega / j = h \lambda$ of $r _ { \jmath }$ in (7.62) lies,for sufficiently small $h _ { 0 }$ ，in a neighbourhood $V$ of the origin, where the estimate of Lemma $7 . 9 \mathrm { c }$ holds. For $j h \ge 1$ we thus obtain the bound

$$
\int e ^ { \operatorname { R e } \omega + a | \omega | ^ { 2 } / \jmath } | \omega | ^ { - \beta } | d \omega | \leq C e ^ { \gamma \jmath h } ,
$$

because $\operatorname { R e } \omega = j h \operatorname { R e } \lambda$ ， $| \omega | ^ { 2 } / j \le j h \cdot C o n s t$ and $| \omega | \ge | \lambda |$ is bounded away from the origin. For small $j h$ the contour $\Gamma _ { j }$ comes arbitrarily close to the origin so that a more refined estimate is required." The idea is to replace the corresponding part of $\Gamma _ { \jmath }$ (in (7.61) and hence also in (7.62)) by an equivalent contour which is independent of $j h \in \{ h , 1 \}$ , has a positive distance to the origin and remains in the neighbourhood $V$ . The corresponding integral is thus bounded by some constant.

Remark 7.12. In Lemma 7.11 it is sufficient to require the analyticity of $\Phi ( s )$ and the estimate(7.57) in a sector $| \arg ( s - c ) | < \pi - \alpha ^ { \prime }$ ， where some compact neighbourhood of the origin is removed. We just have to take the contour $\Gamma$ in (7.59) so that it lies outside this compact neighbourhood of O. In this situation, the constant $\gamma$ may be positive also if $c < 0$

# Exercises

1. Prove the Cauchy integral formula (7.18) in the case where all eigenvalues $\lambda$ of $A$ satisfy $| \lambda | \leq 1$ and the contour of integration is the circle $| z | = \varrho$ with $\varrho > 1$

Hint. Integrate the identity

$$
z ^ { n } ( z I - A ) ^ { - 1 } = \sum _ { \jmath = 0 } ^ { \infty } A ^ { \jmath } z ^ { n - j - 1 } .
$$

2. (Kato 1960). For a non-singular $k \times k$ -matrix $B$ show that in the Euclidean norm

$$
\| B ^ { - 1 } \| \leq { \frac { \| B \| ^ { k - 1 } } { | \operatorname* { d e t } B | } } .
$$

Hint. Use the singular value decomposition of $B$ ,i.e., $B = U ^ { T } \Lambda V$ ,where $U$ and $V$ are orthogonal and $\boldsymbol { \Lambda } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { k } \right)$ with $\sigma _ { 1 } \geq \sigma _ { 2 } \geq . . . > \sigma _ { k } > 0$

3.A method $( \varrho , \sigma )$ is called $A$ -contractive in the norm $\| \cdot \| _ { G }$ (Nevanlinna & Liniger 1978-79,Dahlquist & Soderlind 1982),if

$$
\| C ( \mu ) \| _ { G } \leq 1 \qquad \mathrm { ~ f o r ~ } \quad \operatorname { R e } \mu \leq 0
$$

where $C ( \mu )$ is the companion matrix (7.13).

a) Prove that a method $\left( \varrho , \sigma \right)$ is $A$ -contractive for some positive definite matrix $G$ , if and only if it is $A$ -stable.

b) Compute the contractivity region

$$
\left\{ \mu \in \mathbb { C } \mathrm { : } \ \| C ( \mu ) \| _ { G } \leq 1 \right\}
$$

for the 2-step BDF method with $G$ given in (6.20). Observe that it is strictly smaller than the stability domain.

Result. The contractivity region is $\{ \mu \in \mathbb { C } \mathrm { : \mathrm { ~ } R e } \mu \leq 0 \}$

4. Give a direct proof for the statement of Lemma $7 . 9 \mathrm { a }$

Hint. Observe that

$$
r ( \zeta , \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \prod _ { \ i = 1 } ^ { k } \frac { 1 } { ( 1 - \zeta \cdot \zeta _ { \ i } ( \mu ) ) } ,
$$

where $\zeta _ { 1 } ( \mu ) , \ldots , \zeta _ { k } ( \mu )$ are the $k$ zeros of $\varrho ( \zeta ) - \mu \sigma ( \zeta )$ .If $\mu _ { 0 } \in \operatorname { I n t } S$ then there exists a neighbourhood $\mathcal { U }$ of $\mu _ { 0 }$ such that $| \zeta _ { \imath } ( \mu ) | \leq a < 1$ for all $i$ and $\mu \in \mathcal { U }$ ． Hence the coefficients $r _ { \jmath } ( \mu )$ are bounded. For $\mu _ { 0 } \in \partial S$ we have $\left| \zeta _ { \imath } ( \mu _ { 0 } ) \right| = 1$ for, say, $i = 1 , \ldots , \ell$ with $1 \leq \ell \leq k$ . These $\ell$ zeros are simple for all $\mu$ in a sufficiently small neighbourhood $\mathcal { U }$ of $\mu _ { 0 }$ and the other zeros satisfy $| \zeta _ { i } ( \mu ) | \leq a < 1$ for $\mu \in \mathcal { U } \cap S$ . A partial fraction decomposition

$$
r ( \zeta , \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \left( \sum _ { \iota = 1 } ^ { \ell } \frac { c _ { i } ( \mu ) } { 1 - \zeta \cdot \zeta _ { \iota } ( \mu ) ) } + s ( \zeta , \mu ) \right)
$$

shows that

$$
r _ { \jmath } ( \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \biggl ( \sum _ { \imath = 1 } ^ { \ell } c _ { \imath } ( \mu ) ( \zeta _ { i } ( \mu ) ) ^ { j } + s _ { \jmath } ( \mu ) \biggr ) ,
$$

where $s _ { \jmath } \left( \mu \right)$ are the coefficients of $s ( \zeta , \mu )$ . Since the function $s ( \zeta , \mu )$ is uniformly bounded for $| \zeta | \le 1$ and $\mu \in \mathcal { U } \cap S$ , it follows from Cauchy's integral formula with integration along $| \zeta | = 1$ that $s _ { \jmath } ( \mu )$ is bounded. The statement thus follows from(7.64)and thefactthatafinitesetof thefamily $\{ \mathcal { U } \} _ { \mu _ { 0 } \in S }$ covers $S$ (Heine-Borel).

# V.8 Convergence for Nonlinear Problems

In Sect. V.6 we have seen a convergence result for one-leg methods (Theorem 6.10) applied to nonlinear problems satisfying a one-sided Lipschitz condition. An extension to linear multistep methods has been given in Theorem 6.11. A different and direct proof of this result will be the first goal of this section. Unfortunately, such a result is valid only for $A$ -stable methods (whose order cannot exceed two). The subsequent parts of this section are then devoted to convergence results for nonlinear problems,where the assumptions on the method are relaxed (e.g., $A ( \alpha )$ \~ stability), but the class of problems considered is restricted. We shall present two different theories: the multiplier technique of Nevanlinna & Odeh (1981) and Lubich's perturbation approach via the discrete variation of constants formula (Lubich 1991).

# Problems Satisfying a One-Sided Lipschitz Condition

Suppose that the differential equation $y ^ { \prime } = f ( x , y )$ satisfies

$$
{ \mathrm { R e } } \left. f ( x , y ) - f ( x , z ) , y - z \right. \leq \nu \Vert y - z \Vert ^ { 2 }
$$

for some inner product. We consider the linear multistep method

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y _ { m + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f ( x _ { m + \imath } , y _ { m + \imath } )
$$

together with its perturbed formula

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } \widehat { y } _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } f ( x _ { m + \ i } , \widehat { y } _ { m + \ i } ) + d _ { m + k } .
$$

The perturbations $d _ { m + k }$ can be interpreted as the influence of round-off, as the error due to the iterative solution of the nonlinear equation, or as the local discretization error (compare Eq.(7.5)). Taking the difference of (8.3) and (8.2) we obtain (for $m \geq 0$ ）

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } \Delta y _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \Delta f _ { m + \ i } + d _ { m + k } ,
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $\mathit { I I }$ Springer Series in Computat1onal Mathematics 14, DOI 10.1007/978-3-642-05221-7_23, $©$ Springer-Verlag Berlin Heidelberg 2010

where we have introduced the notation

$$
\Delta y _ { \jmath } = \widehat { y } _ { \jmath } - y _ { \jmath } , \qquad \Delta f _ { \jmath } = f ( x _ { \jmath } , \widehat { y } _ { \jmath } ) - f ( x _ { \jmath } , y _ { \jmath } ) .
$$

The one-sided Lipschitz condition cannot be used directly, because several $\Delta f _ { \jmath }$ appear in (8.4) (in contrast to one-leg methods). In order to express one $\Delta f _ { m }$ in terms of $\Delta y _ { \jmath }$ only we introduce the formal power series

$$
\Delta y ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta y _ { \jmath } \zeta ^ { \jmath } , \quad \Delta f ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta f _ { \jmath } \zeta ^ { j } , \quad d ( \zeta ) = \sum _ { \jmath \geq 0 } d _ { \jmath } \zeta ^ { \jmath } .
$$

It is convenient to assume that $\Delta y _ { \jmath } = 0 , \Delta f _ { \jmath } = 0 , d _ { \jmath } = 0$ for negative indices and that $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined by Eq. (8.4) with $m \in \{ - k , \ldots , - 1 \}$ . Then Eq. (8.4) just compares the coeficient of $\zeta ^ { m }$ in the identity

$$
\varrho \big ( \zeta ^ { - 1 } \big ) \Delta y ( \zeta ) = h \sigma ( \zeta ^ { - 1 } ) \Delta f ( \zeta ) + \zeta ^ { - k } d ( \zeta ) .
$$

Dividing (8.4') by $\sigma ( \zeta ^ { - 1 } )$ and comparing the coefficients of $\zeta ^ { m }$ yields

$$
\sum _ { \jmath = 0 } ^ { m } \delta _ { m - j } \Delta y _ { j } = h \Delta f _ { m } + \widetilde { d } _ { m } ,
$$

where

$$
\frac { \varrho \big ( \zeta ^ { - 1 } \big ) } { \sigma \big ( \zeta ^ { - 1 } \big ) } = \delta ( \zeta ) = \sum _ { j \geq 0 } \delta _ { j } \zeta ^ { j }
$$

as in (7.45) and

$$
\frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } d ( \zeta ) = \widetilde { d } ( \zeta ) = \sum _ { \jmath \geq 0 } \widetilde { d } _ { \jmath } \zeta ^ { \jmath } .
$$

In (8.6) $\Delta f _ { m }$ is now isolated as desired and we can take the scalar product of (8.6) with $\Delta y _ { m }$ . We then exploit the assumption (8.1) and obtain

$$
\sum _ { \jmath = 0 } ^ { m } \delta _ { m - \jmath } \mathrm { R e } \langle \Delta y _ { \jmath } , \Delta y _ { m } \rangle \leq h \nu \| \Delta y _ { m } \| ^ { 2 } + \mathrm { R e } \langle \widetilde { d } _ { m } , \Delta y _ { m } \rangle .
$$

This allows us to prove the following estimate.

Lemma 8.1. Let $\{ \Delta y _ { \jmath } \}$ and $\{ \Delta f _ { \jmath } \}$ satisfy (8.6) with $\delta _ { \jmath }$ given by (8.7). If

$$
\begin{array} { r } { \mathrm { R e } \left. \Delta f _ { m } , \Delta y _ { m } \right. \leq \nu \| \Delta y _ { m } \| ^ { 2 } , \qquad m \geq 0 , } \end{array}
$$

and the method is $A$ -stable,then there exist constants $C$ and $C _ { 0 } > 0$ such that for $m h \leq x _ { \mathrm { e n d } } - x _ { 0 }$ and $h \nu \leq C _ { 0 }$ ，

$$
\| \Delta y _ { m } \| \leq C \sum _ { \jmath = 0 } ^ { m } \| \widetilde { d } _ { \jmath } \| .
$$

Proof. We firstreformulate theleft-handsideof(8.9).For this weintroduce $\{ \Delta z _ { _ { \jmath } } \}$ by the relation

$$
\sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \Delta z _ { m + \ i } = \Delta y _ { m } , \qquad m \ge 0
$$

and assume that $\Delta z _ { _ { \jmath } } = 0$ for $j < k$ .With $\begin{array} { r } { \Delta z ( \zeta ) = \sum _ { j } \Delta z _ { j } \zeta ^ { j } } \end{array}$ this means that $\sigma ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) = \Delta y \bar { ( \zeta ) }$ . Consequently we also have

$$
\begin{array} { r } { \delta ( \zeta ) \Delta y ( \zeta ) = \varrho ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) , } \end{array}
$$

which is equivalent to

$$
\sum _ { j = 0 } ^ { m } \delta _ { m - j } \Delta y _ { \jmath } = \sum _ { i = 0 } ^ { k } \alpha _ { i } \Delta z _ { m + i } .
$$

Inserting (8.11) and (8.10) into (8.9) yields

$$
\begin{array} { r l r } {  { \mathrm { R e } \Big \langle \sum _ { i = 0 } ^ { k } \alpha _ { \iota } \Delta z _ { m + i } , \sum _ { i = 0 } ^ { k } \beta _ { \iota } \Delta z _ { m + i } \Big \rangle } } \\ & { } & { \leq \displaystyle h \nu \bigg \| \sum _ { i = 0 } ^ { k } \beta _ { \iota } \Delta z _ { m + \iota } \bigg \| ^ { 2 } + \mathrm { R e } \Big \langle \widetilde { d } _ { m } , \sum _ { i = 0 } ^ { k } \beta _ { i } \Delta z _ { m + i } \Big \rangle . } \end{array}
$$

By Theorem 6.7 the method $( \varrho , \sigma )$ is $G$ -stable,so that Eq.(6.21) can be applied. As in the proof of Lemma 6.9 this yields for $\Delta Z _ { m } = ( \Delta z _ { m + k - 1 } , . . . , \Delta z _ { m } ) ^ { T }$ and $\nu \geq 0$

$$
\| \Delta Z _ { m + 1 } \| _ { G } \leq \big ( 1 + C _ { 1 } h \nu \big ) \| \Delta Z _ { m } \| _ { G } + C _ { 2 } \| \widetilde { d } _ { m } \| ,
$$

(if $\nu < 0$ replace $\nu$ by $\nu = 0$ ). But this implies

$$
\lVert \Delta Z _ { m + 1 } \rVert _ { G } \leq C _ { 3 } \Big ( \lVert \Delta Z _ { 0 } \rVert _ { G } + \sum _ { j = 0 } ^ { m } \lVert \widetilde { d } _ { j } \rVert \Big ) .
$$

By definition of $\Delta z _ { j }$ we have $\Delta Z _ { 0 } = 0$ . The statement now follows from the fact that $\begin{array} { r } { \| \Delta y _ { m } \| \leq C _ { 4 } \left( \| \Delta Z _ { m + 1 } \| _ { G } + \| \Delta Z _ { m } \| _ { G } \right) } \end{array}$ □

This lemma allows a direct proof for the convergence of $A$ -stable multistep methods which are strictly stable at infinity (compare Theorem 6.11).

Theorem 8.2. Consider an $A$ -stable multistep method of order $p$ which is strictly stable at infinity. Suppose that the differential equation satisfies (8.1). Then there exists $C _ { 0 } > 0$ such that for $h \nu \leq C _ { 0 }$

$$
\| y _ { m } - y ( x _ { m } ) \| \leq C { \big ( } \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - y ( x _ { j } ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \| { \big ) } + M h ^ { p } .
$$

The constant $C$ depends on the method and, for $\nu > 0$ ，on the length ${ x _ { m } } - { x _ { 0 } }$ of the integration interval; the constant $M$ depends in addition on bounds for the $( p + 1 )$ -th derivative of the exact solution.

Proof. We put ${ \widehat { y } } _ { m } = y ( x _ { m } )$ in (8.3). The perturbations thus become the local truncation errors $d _ { m + k } = \delta _ { L M } ( x _ { m } )$ ， where

$$
\delta _ { L M } ( x ) = \sum _ { i = 0 } ^ { k } \alpha _ { \ i } y ( x + i h ) - h \sum _ { \ i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x + i h ) .
$$

If the zeros of $\sigma ( \zeta )$ all lie in the open unit disk,the coefficients of $\zeta ^ { - k } / \sigma ( \zeta ^ { - 1 } )$ are absolutely summable and by (8.8) we have

$$
\sum _ { j = 0 } ^ { m } \| \widetilde { d } _ { j } \| \leq C _ { 1 } \sum _ { \jmath = 0 } ^ { m } \| d _ { j } \| .
$$

The statement then follows from Lemma 8.1, from $\| \delta _ { L M } ( x ) \| \le M h ^ { p + 1 }$ ，and from the fact that $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the $y _ { j } - y ( x _ { j } )$ and ${ } h \left( f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \right)$ for $j < k$ · □

# Multiplier Technique

... the best of all multipliers would be $\{ 1 , - \eta \}$ with a very small $\eta > 0$ ；. (Nevanlinna & Odeh 1981)

The above convergence proof is based on Eq.(8.6) and on the $A$ -stability of the multistep method. How can we modify this proof in order to get convergence results also for methods which are not $A$ -stable? This can be done by the so-called “multiplier technique",introduced by Nevanlinna & Odeh (1981） and based on previous ideas of Nevanlinna (1977) and Odeh & Liniger (1977).

The main idea is the following: instead of multiplying scalarly the identity (8.6) by $\Delta y _ { m }$ , we multiply it by

$$
\sum _ { \jmath = 0 } ^ { m } \mu _ { m - j } \Delta y _ { \jmath }
$$

where $\{ { \mu } _ { \jmath } \}$ are the coefficients of a rational function (the multiplier)

$$
\mu ( \zeta ) = \sum _ { j \geq 0 } \mu _ { j } \zeta ^ { j } = \frac { \eta ( \zeta ^ { - 1 } ) } { \tau ( \zeta ^ { - 1 } ) }
$$

（ $\eta$ and $\tau$ are polynomials).We obtain

$$
\begin{array} { r } { \mathrm { R e } \Big \langle \displaystyle \sum _ { j = 0 } ^ { m } \delta _ { m - , \ j } \Delta y _ { j } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle = h \mathrm { R e } \Big \langle \Delta f _ { m } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle } \\ { + \Big \langle \widetilde { d } _ { m } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle . } \end{array}
$$

Our next aim is to introduce new variables $\Delta z _ { j }$ such that the left-hand side of (8.14) becomes

$$
\Big \langle \sum _ { j = 0 } ^ { m } \delta _ { m - j } \Delta y _ { \ j } , \sum _ { \ j = 0 } ^ { m } \mu _ { m - j } \Delta y _ { j } \Big \rangle = \Big \langle \sum _ { i = 0 } ^ { \ell } \widetilde { \alpha } _ { i } \Delta z _ { m + i } , \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { i } \Delta z _ { m + i } \Big \rangle .
$$

Denoting

$$
\widetilde { \varrho } ( \zeta ) = \sum _ { i = 0 } ^ { \ell } \widetilde { \alpha } _ { i } \zeta ^ { i } , \qquad \widetilde { \sigma } ( \zeta ) = \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { \iota } \zeta ^ { i } ,
$$

the identity (8.15) certainly holds,if

$$
\begin{array} { r l } & { \varrho ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \sigma ( \zeta ^ { - 1 } ) \widetilde { \varrho } ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) } \\ & { \eta ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \tau ( \zeta ^ { - 1 } ) \widetilde { \sigma } ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) . } \end{array}
$$

Dividing these two relations motivates the following definition of the new generating polynomials

$$
\begin{array} { r } { \widetilde { \varrho } ( \zeta ) = \varrho ( \zeta ) \tau ( \zeta ) / \chi ( \zeta ) , \qquad \widetilde { \sigma } ( \zeta ) = \sigma ( \zeta ) \eta ( \zeta ) / \chi ( \zeta ) . } \end{array}
$$

Here $\chi ( \zeta )$ denotes the greatest common divisor of $\varrho ( \zeta ) \tau ( \zeta )$ and $\sigma ( \zeta ) \eta ( \zeta )$ . If we define $\Delta z _ { _ { \jmath } } = 0$ for $j < 0$ and the remaining $\Delta z _ { j }$ by

$$
\chi ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \sigma ( \zeta ^ { - 1 } ) \tau ( \zeta ^ { - 1 } ) \Delta z ( \zeta )
$$

the identity (8.15) holds for all $m$ . Suppose now that the multistep method $( \widetilde { \varrho } , \widetilde { \sigma } )$ is $A$ -stable, then the left hand side of (8.14) can be minorized by the $G$ -stability estimate (6.21) and we shall be able to derive convergence results. This motivates the following

Definition 8.3. The rational function $\mu ( \zeta )$ of (8.13) is called amultiplier for $( \varrho , \sigma )$ if $\mu ( \zeta ) \not \equiv \varrho ( \zeta ^ { - 1 } ) / \sigma ( \zeta ^ { - 1 } )$ and if the method $( \widetilde { \varrho } , \widetilde { \sigma } )$ ， given by (8.18) is $A$ -stable, i.e.,if

$$
\operatorname { R e } \left( \frac { 1 } { \mu ( \zeta ^ { - 1 } ) } \cdot \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \qquad \mathrm { f o r } \quad | \zeta | > 1 .
$$

A continuation of the above analysis yields the following convergence result.

Lemma 8.4. Let $\{ \Delta y _ { j } \}$ and $\{ \Delta f _ { j } \}$ satisfy (8.6) with $\delta _ { j }$ given by (8.7). If

$$
\sum _ { m = 0 } ^ { N } \sum _ { j = 0 } ^ { m } \mu _ { m - j } \mathrm { R e } \left. \Delta f _ { m } , \Delta y _ { j } \right. \leq 0 \qquad f o r a l l \quad N \geq 0
$$

and if $\mu ( \zeta )$ is $a$ multiplier for the method, then there exists a constant $C$ such that for $m h \leq x _ { \mathrm { e n d } } - x _ { 0 }$

$$
\lVert \Delta y _ { m } \rVert \leq C \sum _ { j = 0 } ^ { m } \lVert \widetilde { d } _ { j } \rVert .
$$

Proof. Inserting (8.15) into (8.14) and using the estimate (6.21) for the $A$ -stable method $( \widetilde { \varrho } , \widetilde { \sigma } )$ yields for $\Delta Z _ { m } = ( \Delta z _ { m + \ell - 1 } , . . . , \Delta z _ { m } ) ^ { T }$

$$
\begin{array} { r } { \| \Delta Z _ { m + 1 } \| _ { G } ^ { 2 } - \| \Delta Z _ { m } \| _ { G } ^ { 2 } \leq h \mathrm { R e } \left. \Delta f _ { m } , \displaystyle \sum _ { \jmath = 0 } ^ { m } \mu _ { m - \jmath } \Delta y _ { \jmath } \right. } \\ { + \| \widetilde { d } _ { m } \| \cdot \Big \| \displaystyle \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { i } \Delta z _ { m + i } \Big \| . } \end{array}
$$

Summing up this inequality from $m \simeq 0$ to $m \simeq N$ gives

$$
\| \Delta \boldsymbol { Z } _ { N + 1 } \| _ { G } ^ { 2 } \leq C _ { 1 } \sum _ { m = 0 } ^ { N } \| \widetilde { d } _ { m } \| \cdot \big ( \| \Delta \boldsymbol { Z } _ { m + 1 } \| _ { G } + \| \Delta \boldsymbol { Z } _ { m } \| _ { G } \big ) ,
$$

because $\Delta Z _ { 0 } = 0$ by (8.19). This also implies

$$
\operatorname* { m a x } _ { N \leq M } \| \Delta Z _ { N + 1 } \| _ { G } ^ { 2 } \leq 2 C _ { 1 } \sum _ { m = 0 } ^ { M } \| \widetilde { d } _ { m } \| \cdot \operatorname* { m a x } _ { m \leq M } \| \Delta Z _ { m + 1 } \| _ { G } .
$$

A division by $\mathrm { m a x } _ { N \leq M } \| \Delta Z _ { N + 1 } \| _ { G }$ yields the desired estimate, because $\Delta y _ { M }$ is alinearcombinationoftheelementsof $\Delta Z _ { M + 1 }$ □

The proof of Theorem 8.2 applied to the $A$ -stable method $( \widetilde { \varrho } , \widetilde { \sigma } )$ now yields:

Theorem 8.5 (Nevanlinna & Odeh 1981). Consider $a$ linear multistep method (8.2) of order $p$ ， which is strictly stable at infinity and has a multiplier $\mu ( \zeta )$ . Suppose that the differential equation satisfies

$$
\sum _ { m = 0 } ^ { N } \sum _ { \substack { j = 0 } } ^ { m } \mu _ { m - j } \mathrm { R e } \left. f ( x _ { m } , u _ { m } ) - f ( x _ { m } , v _ { m } ) , u _ { j } - v _ { j } \right. \leq 0
$$

for all $N \geq 0$ and for all sequences $\{ u _ { j } \}$ and $\{ v _ { \jmath } \}$ . Then we have

$$
\| y _ { m } - y ( x _ { m } ) \| \leq C { \Big ( } \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - y ( x _ { j } ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \| { \Big ) } + M h ^ { p } ,
$$

In the next two subsections we shall study the existence and construction of multipliers,and try to better understand the condition (8.22).

Construction of Multipliers. Obviously $\mu ( \zeta ) = 1$ is a multiplier iff the method itself is $A$ -stable. Moreover, the limit $| \zeta |  \infty$ in (8.20) shows that $\mu ( 0 )$ must have the same sign as $\alpha _ { k } / \beta _ { k }$ (which we always assume to be positive). Therefore, the simplest (and most important) nontrivial multiplier has the form

$$
\mu ( \zeta ) = 1 - \eta \zeta .
$$

Suppose now that the method $( \varrho , \sigma )$ is stable at infinity. The maximum principle for harmonic functions then implies that (8.23) is a multiplier for $( \varrho , \sigma )$ iff $| \eta | \leq 1$ and

$$
\operatorname { R e } \left( \left( 1 - \eta e ^ { \iota t } \right) { \frac { \varrho { \big ( } e ^ { \iota t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) \geq 0 \qquad { \mathrm { f o r ~ a l l } } \quad t \in \mathbb { R } .
$$

This condition motivates the study of

$$
\gamma ( t ) = { \Bigg ( } \mathrm { R e } \left( { \frac { \varrho { \big ( } e ^ { i t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) , - \mathrm { R e } \left( e ^ { i t } { \frac { \varrho { \big ( } e ^ { i t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) { \Bigg ) } ,
$$

which is called the modified root-locus curve by Nevanlinna & Odeh (1981). We then have:

Criterion 8.6. Consider a method which is stable at infinity. The function (8.23) is a multiplier for $( \varrho , \sigma )$ iff $| \eta | \leq 1$ and the modified root-locus curve lies to the right of the straight line through the origin with slope $- 1 / \eta$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/1a4bc43bcef68c3a617bbb54baddd37ec68c8f1a33cdb7c0941fb49f278aac4c.jpg)  
Fig.8.1. Modified root-locus curve for BDF schemes

Fig.8.1 shows the modified root-locus curves for the BDF schemes for $2 \le k \le$ }. The optimal values for $\eta$ are given in Table 8.1.

Table 8.1. Multiplier for BDF schemes   

<table><tr><td>k</td><td>m</td><td>A(α)-stable arccos n</td></tr><tr><td>2</td><td>0 π/2</td><td>π/2</td></tr><tr><td>3</td><td>0.0836</td><td>85.20° 86.03°</td></tr><tr><td>4</td><td>0.2878 73.27°</td><td>73.35°</td></tr><tr><td>5</td><td>0.8160</td><td>35.32° 51.84°</td></tr><tr><td>6</td><td>5.0130</td><td>17.84° 一</td></tr></table>

Proposition 8.7. If $\mu ( \zeta )$ is $a$ multiplier for $( \varrho , \sigma )$ and we have

$$
| \arg \mu ( \zeta ) | \leq { \frac { \pi } { 2 } } - \alpha \qquad f o r \quad | \zeta | \leq 1
$$

then the method is $A ( \alpha )$ -stable.

Proof. Condition (8.20) together with (8.25) implies that

$$
\bigg | \arg \bigg ( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \bigg ) - \pi \bigg | \geq \alpha \qquad \mathrm { f o r } \quad | \zeta | \geq 1 .
$$

But this condition implies $A ( \alpha )$ -stability.

A simple calculation shows that the multiplier(8.23) satisfies (8.25) with $\alpha =$ arccos $\eta$ . For the BDF schemes we have included these values in Table 8.1 together with the $\alpha$ -values for linear stability.

# Multipliers and Nonlinearities

We still have to investigate the problem under what conditions on the multiplier $\mu ( \zeta )$ and on the function $f ( x , y )$ one has (8.22) for all sequences $\{ u _ { \mathfrak { j } } \}$ and $\{ v _ { \jmath } \}$ To get an idea of the nature of (8.22) we first look, following Nevanlinna & Odeh (1981),at the linear problem $y ^ { \prime } = A y$

Proposition 8.8. If the multiplier $\mu ( \zeta )$ satisfies (8.25) and if the range of the matrix $A$ lies in the sector $| \arg \langle A u , u \rangle - \pi | \leq \alpha$ for all $u \in \mathbb { C } ^ { n }$ , then we have

$$
\sum _ { m = 0 } ^ { N } \sum _ { \jmath = 0 } ^ { m } \mu _ { m - j } \operatorname { R e } \left. A u _ { m } , u _ { \jmath } \right. \leq 0
$$

for all $N \geq 0$ and all sequences $\{ u _ { \mathfrak { z } } \}$

Proof. A direct computation shows that the expression in (8.26) equals

$$
\operatorname { R e } \left( \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mu ( e ^ { i t } ) \langle A \widehat { u } _ { N } ( t ) , \widehat { u } _ { N } ( t ) \rangle d t \right)
$$

where

$$
\widehat { u } _ { N } ( t ) = \sum _ { \jmath = 0 } ^ { N } e ^ { - \imath j t } u _ { j }
$$

denotes the Fourier transform of $( u _ { 0 } , u _ { 1 } , \ldots , u _ { N } )$ . The assumptions on $\mu ( \zeta )$ and on $A$ imply that the integrand in (8.27) has non-positive real part. This proves (8.26). □

Problems which satisfy (8.22) for some multiplier $\mu ( \zeta )$ must also satisfy the one-sided Lipschitz condition (8.1） with $\nu \simeq 0$ (this is seen by putting $N \approx 0$ in (8.22)).A class of nonlinear problems,for which (8.22) holds,is given by the following perturbation result.

Proposition 8.9． Let $f ( x , y ) = - A y + A g ( x , y )$ where $A$ is $a$ symmetric and positive semi-definite matrix. With $\| u \| _ { A } ^ { 2 } = u ^ { T } A u$ suppose that

$$
\| g ( x , y ) - g ( x , z ) \| _ { A } \leq L \| y - z \| _ { A } .
$$

Then Condition (8.22) holds if

$$
L \cdot \operatorname* { m a x } _ { | \zeta | = 1 } | \mu ( \zeta ) | \leq \operatorname* { m i n } _ { | \zeta | = 1 } \mathrm { R e } \mu ( \zeta ) .
$$

Remark. For the multiplier (8.23) Condition (8.29) is equivalent to $L \cdot ( 1 + \eta ) \leq ( 1 - \eta )$

Proof. As in the proof of Proposition8.8 we get for w,=uj-Uj

$$
\begin{array} { r l r } {  { - \sum _ { m = 0 } ^ { N } \sum _ { \jmath = 0 } ^ { m } \mu _ { m - \jmath } \operatorname { R e }  A w _ { m } , w _ { \jmath }  = - \operatorname { R e } ( \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mu ( e ^ { \imath t } ) \big \langle A \widehat { w } _ { N } ( t ) , \widehat { w } _ { N } ( t ) \big \rangle d t ) } } \\ & { } & { \leq - m _ { 0 } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \langle A \widehat { w } _ { N } ( t ) , \widehat { w } _ { N } ( t ) \rangle d t = - m _ { 0 } \sum _ { \jmath = 0 } ^ { N } \langle A w _ { j } , w _ { \jmath } \rangle \qquad ( 8 . 3 0 } \end{array}
$$

where $m _ { 0 } = \operatorname* { m i n } \mathrm { R e } \mu ( e ^ { \ i t } )$ . On the other hand, the inequality of Cauchy-Schwarz gives

$$
\begin{array} { r l r } {  { \sum _ { m = 0 } ^ { N } \mathrm { R e } \Big \langle A \big ( g ( x _ { m } , u _ { m } ) - g ( x _ { m } , v _ { m } ) \big ) , \sum _ { p = 0 } ^ { m } \mu _ { m - , \ j } ( u _ { \ j } - v _ { j } ) \Big \rangle } } \\ & { } & { \leq \bigg ( \displaystyle \sum _ { m = 0 } ^ { N } \| g ( x _ { m } , u _ { m } ) - g ( x _ { m } , v _ { m } ) \| _ { A } ^ { 2 } \bigg ) ^ { 1 / 2 } \cdot \bigg ( \displaystyle \sum _ { m = 0 } ^ { N } \Big \| \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - j } ( u _ { j } - v _ { j } ) \Big \| _ { A } ^ { 2 } \bigg ) ^ { 1 / 2 } . } \end{array}
$$

The last term in (8.31) can be estimated as (for the moment put $w _ { j } = 0$ for $j > N )$

$$
\begin{array} { r } { \displaystyle \sum _ { m = 0 } ^ { N } \Big \| \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - j } w _ { j } \Big \| _ { A } ^ { 2 } \leq \frac { 1 } { 2 \pi } \displaystyle \int _ { 0 } ^ { 2 \pi } \Big \| \displaystyle \sum _ { m \geq 0 } e ^ { - \imath m t } \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - \jmath } w _ { \jmath } \Big \| _ { A } ^ { 2 } d t } \\ { = \displaystyle \frac { 1 } { 2 \pi } \displaystyle \int _ { 0 } ^ { 2 \pi } | \mu ( e ^ { - i t } ) | ^ { 2 } \cdot \Big \| \displaystyle \sum _ { j \geq 0 } e ^ { - i j t } w _ { j } \Big \| _ { A } ^ { 2 } d t \leq M ^ { 2 } \displaystyle \sum _ { j = 0 } ^ { N } \| w _ { j } \| _ { A } ^ { 2 } } \end{array}
$$

where $M = \operatorname* { m a x } \left| \mu ( e ^ { - i t } ) \right|$ . These estimates together with (8.28) show that the expression in (8.22) is majorized by

$$
( L \cdot M - m _ { 0 } ) \sum _ { j = 0 } ^ { N } \| u _ { j } - v _ { j } \| _ { A } ^ { 2 } .
$$

This is non-positive if (8.29) holds.

# Discrete Variation of Constants and Perturbations

We now turn our attention to the perturbation approach of Lubich (1991), which extends the ideas of Sect. V.7 (discrete variation of constants) to nonlinear problems. For this we consider nonlinear differential equations written in the form

$$
y ^ { \prime } = A y + g ( t , y ) .
$$

Inserting this equation into Formulas (8.2), (8.3),and (8.4) we get

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { i } I - h A \beta _ { i } ) \Delta y _ { m + i } = h \Delta g _ { m + k } + d _ { m + k } ,
$$

where

$$
\Delta g _ { m + k } = \sum _ { i = 0 } ^ { k } \beta _ { i } \Bigl ( g ( x _ { m + i } , \widehat { y } _ { m + i } ) - g ( x _ { m + \imath } , y _ { m + i } ) \Bigr )
$$

for $m \geq 0$ . We further put $\Delta g _ { \jmath } = 0$ for $j < k$ . Recall that $d _ { \jmath }$ (for $j \geq k )$ are usually the local truncation errors and $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined by (8.33) with $m \in \{ - 1 , \ldots , - k \}$ . The differences $\Delta y _ { j }$ are then the global errors of the method. If we introduce the formal power series

$$
\Delta y ( \zeta ) = \sum _ { j \geq 0 } \Delta y _ { j } \zeta ^ { j } , \quad \Delta g ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta g _ { \jmath } \zeta ^ { j } , \quad d ( \zeta ) = \sum _ { j \geq 0 } d _ { \jmath } \zeta ^ { j }
$$

then the recursion (8.33) can be written as

$$
\Delta y ( \zeta ) = r ( \zeta , h A ) { \big ( } h \Delta g ( \zeta ) + d ( \zeta ) { \big ) } .
$$

The resolvent $r ( \zeta , h A )$ was introduced in (7.44) and (7.50). The coefficient of $\zeta ^ { m }$ in (8.35) then yields

$$
\Delta y _ { m } = h \sum _ { j = 0 } ^ { m } r _ { m - j } ( h A ) \Delta g _ { \jmath } + \sum _ { j = 0 } ^ { m } r _ { m - j } ( h A ) d _ { j } .
$$

The second sum on the right-hand side of (8.36) can be estimated as in Sect.V.7. In order to estimate the first term we have to combine estimates for $r _ { \jmath } ( h A )$ with a Lipschitz condition for $g ( x , y )$ . This will lead to a Gronwall-type inequality, whose resolution gives the desired estimates for $\Delta y _ { m }$ . Let us illustrate this procedure in a simple situation.

Theorem 8.10. Let the multistep method and the matrix $A$ satisfy the assumptions of Theorem 7.10. If the nonlinearity $g ( x , y )$ satisfies

$$
\| g ( x , y ) - g ( x , z ) \| \leq L \| y - z \|
$$

then there exist constants $C , \ h _ { 0 }$ and $\gamma$ as in Theorem 7.10, and A ( $h _ { 0 }$ and $\Lambda$

depend on $L$ )such that

$$
\begin{array} { r l r } {  { \| y ( x _ { m } ) - y _ { m } \| } } \\ & { } & { \quad \le C e ^ { \Lambda x _ { m } } \Big ( \operatorname* { m a x } _ { 0 \le j < k } \| y ( x _ { j } ) - y _ { j } \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } e ^ { \gamma ( x _ { m } - \xi ) } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \Big ) . } \end{array}
$$

Proof. It follows from the proof of Theorem 7.10 and from (8.36) that

$$
\| \Delta y _ { m } \| \leq h L C _ { 1 } \sum _ { j = 0 } ^ { m } e ^ { \gamma ( m - j ) h } \| \Delta y _ { j } \| + C _ { 2 } \sum _ { j = 0 } ^ { m } e ^ { \gamma ( m - j ) h } \varepsilon _ { j } ,
$$

where (with $0 \leq \kappa < 1$ ）

$$
\varepsilon _ { m } = C _ { 0 } \Biggl ( \kappa _ { \quad 0 \leq j < k } ^ { m } \| \Delta y _ { j } \| + h ^ { p } \int _ { x _ { m - k } } ^ { x _ { m } } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \Biggr ) .
$$

Application of Exercise 1 to the sequence $\left\{ e ^ { - \gamma m h } \| \Delta y _ { m } \| \right\}$ yields the statement of the theorem. □

Lubich (1991) has shown how the above estimates can be improved to obtain convergence results for singularly perturbed problems (see Sect. VI.2) and for discretized nonlinear parabolic equations,as we shall see in the sequel.

# Convergence for Nonlinear Parabolic Problems

We consider the initial value problem

$$
y ^ { \prime } + A y = g ( t , y ) , \qquad y ( 0 ) = y _ { 0 }
$$

obtained by space discretization of a parabolic differential equation. The matrix $A$ is assumed to satisfy for some $\alpha ^ { \prime } \in ( 0 , \pi / 2 )$

$$
\| ( s I + A ) ^ { - 1 } \| \leq { \frac { M } { 1 + | s | } } \qquad { \mathrm { ~ f o r ~ } } \qquad | \arg s | \leq \pi - \alpha ^ { \prime }
$$

(compare (7.47)). In order to motivate our assumptions on $g ( t , y )$ we begin with two examples.

Burgers' Equation. For this problem (Burgers 1948)

$$
u _ { t } + u u _ { x } = \mu u _ { x x } \qquad \mathrm { o r } \qquad u _ { t } + \left( \frac { u ^ { 2 } } { 2 } \right) _ { x } = \mu u _ { x x } , \qquad \mu > 0 ,
$$

we consider the discretization

$$
\dot { u } _ { i } = - \frac { u _ { \iota + 1 } ^ { 2 } - u _ { \iota - 1 } ^ { 2 } } { 4 \Delta x } + \mu \frac { u _ { i + 1 } - 2 u _ { \iota } + u _ { i - 1 } } { ( \Delta x ) ^ { 2 } } \ .
$$

It is of the form (8.39) with

$$
A = \frac { \mu } { \Delta x ^ { 2 } } \left( \begin{array} { c c c c c } { 2 } & { - 1 } & & & \\ { - 1 } & { 2 } & { - 1 } & & \\ & { - 1 } & { 2 } & { \ddots } & \\ & & & { \ddots } & { \ddots } & { - 1 } \\ & & & & { - 1 } & { 2 } \end{array} \right) , \qquad g ( t , y ) = \frac { 1 } { 4 \Delta x } \left( \begin{array} { c } { y _ { 2 } ^ { 2 } - y _ { 0 } ^ { 2 } } \\ { y _ { 3 } ^ { 2 } - y _ { 1 } ^ { 2 } } \\ { \vdots } \\ { y _ { n + 1 } ^ { 2 } - y _ { n - 1 } ^ { 2 } } \end{array} \right) ,
$$

where $\mu > 0$ is a given constant, $\Delta x = 1 / ( n + 1 )$ and, due to homogeneous boundary conditions, $y _ { 0 } = y _ { n + 1 } = 0$ . In this situation we work with the scaled norm (on $\mathbb { R } ^ { n } )$

$$
\begin{array} { r } { \| u \| = \sqrt { \Delta x \sum _ { i = 1 } ^ { n } | u _ { i } | ^ { 2 } } , } \end{array}
$$

which tends to that of $L ^ { 2 } ( 0 , 1 )$ for $n \to \infty$ . As the eigenvalues of the symmetric matrix $A$ are real and positive,condition (8.4O) is verified for every $\alpha ^ { \prime } > 0$ ， uniformly in $\Delta x$

The presence of the denominator $\Delta x$ in $g ( t , y )$ of (8.41) does not allow a Lipschitz condition (8.37) uniformly in $\Delta x > 0$ (not even in a neighbourhood of the exact solution). However, using the energy norm $\| A ^ { 1 / 2 } u \|$ ，which already contains the factor $1 / \Delta x$ , we show that

$$
| | g ( t , y ) - g ( t , z ) | | \leq \mu ^ { - 1 } r \cdot | | A ^ { 1 / 2 } ( y - z ) | | \qquad \mathrm { f o r } \quad | | A ^ { 1 / 2 } y | | + | | A ^ { 1 / 2 } z | | \leq r .
$$

For the proof of this relation we consider the bilinear map $b : \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ whose $\iota$ th component is defined by

$$
b _ { i } ( u , v ) = ( 4 \Delta x ) ^ { - 1 } ( u _ { i + 1 } + u _ { \ i - 1 } ) ( v _ { \ i + 1 } - v _ { i - 1 } )
$$

(again we put $u _ { 0 } = v _ { 0 } = u _ { n + 1 } = v _ { n + 1 } = 0 \mathrm { { ; } }$ ). Then

$$
g ( t , y ) - g ( t , z ) = b ( y , y ) - b ( z , z ) = b ( y , y - z ) + b ( y - z , z ) ,
$$

and we need an estimate for $\left| \left| b ( u , v ) \right| \right|$ . Using

$$
\begin{array} { r } { | ( u _ { i + 1 } + u _ { \iota - 1 } ) ( v _ { i + 1 } - v _ { \iota - 1 } ) | \leq 2 \cdot | v _ { \iota + 1 } - v _ { \iota - 1 } | \cdot \operatorname* { m a x } _ { j } | u _ { j } | , } \end{array}
$$

and the estimates of Exercise 3 we obtain

$$
\| b ( u , v ) \| \leq \| u \| _ { \infty } \cdot \| D v \| \leq \mu ^ { - 1 } \cdot \| A ^ { 1 / 2 } u \| \cdot \| A ^ { 1 / 2 } v \| .
$$

where

$$
D = \frac { 1 } { 2 \Delta x } \left( \begin{array} { c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 0 } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { 0 } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } & { { 0 } } \end{array} \right)
$$

represents the first central difference operator. The estimate (8.45) applied to (8.44) proves (8.43).

Incompressible Navier-Stokes Equation. The motion of a viscous incompressible fluid in a domain $\Omega \subset \mathbb { R } ^ { d }$ is governed by the equations of Navier(1823)and Stokes (1845)

$$
\frac { \partial \mathbf { u } } { \partial t } + \sum _ { \ i = 1 } ^ { d } u _ { \ i } \frac { \partial \mathbf { u } } { \partial x _ { \ i } } = \Delta \mathbf { u } - \mathbf { g r a d } p , \qquad \mathrm { d i v } \ \mathbf { u } = 0
$$

where $\mathbf { u } = ( u _ { 1 } , \ldots , u _ { d } ) ^ { T }$ . We denote by $P$ the orthogonal projection from $L ^ { 2 } ( \Omega ) ^ { d }$ onto $X$ ，where $X$ is the subspace of functions with div ${ \bf u } \simeq 0$ (more precisely: the closure of the set of smooth functions with vanishing divergence and support contained in $\Omega$ ). If we apply $P$ to Eq. (8.47), grad $p$ is eliminated and we obtain

$$
\frac { \partial \mathbf { u } } { \partial t } - P \Delta \mathbf { u } = - P \Big ( \sum _ { \ i = 1 } ^ { d } u _ { \ i } \frac { \partial \mathbf { u } } { \partial x _ { i } } \Big ) .
$$

These equations are now precisely of the form (8.39), where $A = - P \Delta$ (or some discretization of it） and $g ( t , y )$ is the right-hand side of (8.48). Lipschitz estimations for this nonlinear term have been obtained by Sobolevskii (1959) and Fujita & Kato (1964). They are of the form

$$
\| g ( t , u ) - g ( t , v ) \| _ { \beta - \gamma } \leq \ell ( r ) \cdot \| u - v \| _ { \beta } \qquad \mathrm { f o r } \quad \| u \| _ { \beta } + \| v \| _ { \beta } \leq r
$$

where $\| \cdot \| _ { \beta }$ denotes the norm

$$
\| u \| _ { \beta } = \| A ^ { \beta } u \| .
$$

In particular, for $d \approx 3$ , condition (8.49) is true for $\beta = 1 / 2 , \gamma \geq 3 / 4$ as well as for $\beta = \gamma > 3 / 4$ (Fujita & Kato 1964, pp.272-273).

Motivated by these examples we consider the initial value problem (8.39) on $\mathbb { R } ^ { n }$ ，where $A$ is supposed to satisfy (8.40) for some $\alpha ^ { \prime } \in ( 0 , \pi / 2 )$ and the nonlinearity $g ( t , y )$ is assumed to satisfy the Lipschitz condition (8.49).

Application of a linear multistep method to (8.39) yields

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { m + \ i } + h A \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } y _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } g ( t _ { m + \ i } , y _ { m + \ i } ) .
$$

Instead of comparing the numerical solution $\{ y _ { m } \}$ with the analytic solution $y ( t )$ of (8.39), it is more interesting to compare it with the exact solution of the original partial differential equation. We therefore denote by $\eta ( t )$ a projection of the solution of the PDE into the finite-dimensional space under consideration. In this way we obtain

$$
\eta ^ { \prime } + A \eta = g ( t , \eta ) + s ( t )
$$

where $s ( t )$ is the spatial discretization error.

Theorem 8.11 (Lubich 1991). Consider the problem (8.39) with $A$ and $g ( t , y )$ satisfying (8.40) and (8.49) with $\gamma < 1$ ， respectively. Assume that the multistep method is of order $p$ ， $A ( \alpha )$ -stable for some $\alpha > \alpha ^ { \prime }$ ， and strictly stable at infinity. Then,the full discretization error is bounded by

$$
\begin{array} { r l r } {  { \| y _ { m } - \eta ( t _ { m } ) \| _ { \beta } \leq C \cdot \bigg ( \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - \eta ( t _ { j } ) \| _ { \beta } + h ^ { p } \int _ { 0 } ^ { t _ { m } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t } } \\ & { } & { + \| A ^ { - 1 } s ( 0 ) \| _ { \beta } + \int _ { 0 } ^ { t _ { m } } \| A ^ { - 1 } s ^ { \prime } ( t ) \| _ { \beta } d t \bigg ) . \quad \quad ( \mathrm { ~ } } \end{array}
$$

The estimate holds for $t _ { m } = m h \leq T$ provided that $h \leq h _ { 0 }$ and the expression in brackets on the right-hand side is bounded by $\varepsilon$ ，where $h _ { 0 }$ and $\varepsilon$ are sufficiently small. The constants $C , \ h _ { 0 }$ and $\varepsilon$ depend on $\operatorname* { m a x } _ { 0 \leq t \leq T } \| \eta ( t ) \| _ { \beta }$ and $M$ of (8.40), but are otherwise independent of $A$ and the dimension of the system, and independent of m and $h$ .

Proof. a) The projected solution $\eta ( t )$ of the PDE,inserted into (8.51), gives

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } \eta ( t _ { m + i } ) = h \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } \Bigl ( - A \eta ( t _ { m + \iota } ) + g \bigl ( t _ { m + \iota } , \eta ( t _ { m + \iota } ) \bigr ) + s ( t _ { m + \iota } ) \Bigr ) + d _ { m + k }
$$

where

$$
\| d _ { m + k } \| _ { \beta } \leq C _ { 0 } h ^ { p } \int _ { t _ { m } } ^ { t _ { m + k } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t , \qquad m \geq 0 .
$$

The same analysis which was necessary for (8.36) now gives for the error $\Delta y _ { m } =$ $\eta ( t _ { m } ) - y _ { m }$ the relation

$$
\Delta y _ { m } = h \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) \Delta g _ { \jmath } + h \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) \Delta s _ { \jmath } + h \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ( - h A ) d _ { \jmath } .
$$

As in (8.34) the quantities $\Delta g _ { \jmath }$ and $\Delta s _ { _ { \jmath } }$ are defined by

$$
\begin{array} { l } { \displaystyle \Delta g _ { m + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Big ( g \big ( t _ { m + \imath } , \eta \big ( t _ { m + \imath } \big ) \big ) - g \big ( t _ { m + \imath } , y _ { m + \imath } \big ) \Big ) } \\ { \displaystyle \Delta s _ { m + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } s \big ( t _ { m + \imath } \big ) } \end{array}
$$

for $m \geq 0$ ,and $\Delta g _ { \jmath } = 0 , \Delta s _ { \jmath } = 0$ for $j < k$ . The values $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined as usual (see their definition before (8.4')). The following three parts of the proof treat the three terms in the right-hand side of (8.54) separately.

b) The Lipschitz condition (8.49) can be written as

$$
\begin{array} { r } { \big \| \boldsymbol A ^ { - \gamma } \big ( \boldsymbol g ( t , \boldsymbol y ) - \boldsymbol g ( t , \boldsymbol z ) \big ) \big \| _ { \beta } \leq \ell ( r ) \cdot \| \boldsymbol y - \boldsymbol z \| _ { \beta } \qquad \mathrm { f o r } \qquad \| \boldsymbol y \| _ { \beta } + \| \boldsymbol z \| _ { \beta } \leq r . } \end{array}
$$

We put $\varrho = \operatorname* { m a x } _ { 0 \leq t \leq T } \| \eta ( t ) \| _ { \beta }$ and assume that for $h m \leq T$ the numerical solution $y _ { m }$ exists and is bounded by $\| y _ { m } \| \leq \varrho + 1$ (this will be verified recursively in part

(f) of the proof) so that

$$
\| A ^ { - \gamma } \Delta g _ { m + k } \| _ { \beta } \leq \ell ( 2 \varrho + 1 ) \cdot \sum _ { i = 0 } ^ { k } | \beta _ { i } | \cdot \| \Delta y _ { m + i } \| _ { \beta } .
$$

Consequently we have to find an estimate for $\| r _ { m - j } ( - h A ) A ^ { \gamma } \| _ { \beta }$ (for the matrix norm corresponding to the vector norm ${ \big \{ } \cdot { \big \} } { \big \{ } _ { \beta } \cdot$ ； see Sect.I.9). We note that $\| r _ { m - j } ( - h A ) A ^ { \gamma } \| _ { \beta } = \| A ^ { \gamma } r _ { m - j } ( - h A ) \|$ and recall that $A ^ { \gamma } r _ { j } ( - h A )$ is the coefficient of $\zeta ^ { j }$ in the series for

$$
A ^ { \gamma } r ( \zeta , - h A ) = A ^ { \gamma } \left( \delta ( \zeta ) I + h A \right) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } .
$$

In order to apply Lemma 7.11 we have to estimate $\Phi ( s ) = A ^ { \gamma } ( s I + A ) ^ { - 1 }$ .If $A$ can be transformed to diagonal form with an orthogonal matrix (as it is the case for (8.41)), we have for $| \arg s | \leq \pi - \alpha ^ { \prime }$ $( 0 < \alpha ^ { \prime } < \alpha )$

$$
\| A ^ { \gamma } ( s I + A ) ^ { - 1 } \| \leq \operatorname* { s u p } _ { a \geq 0 } { \frac { a ^ { \gamma } } { | s + a | } } \leq M _ { 1 } \cdot | s | ^ { \gamma - 1 } .
$$

For the general case we refer the reader to Henry (1981, pp. 26-28). Application of Lemma 7.11 (see also Remark 7.12) yields

$$
\| r _ { \jmath } ( - h A ) A ^ { \gamma } \| _ { \beta } \leq C _ { 1 } { \big ( } ( j + 1 ) h { \big ) } ^ { - \gamma } \qquad { \mathrm { f o r ~ } } \jmath \geq 0 .
$$

Together with the Lipschitz condition (8.55) this gives with $L = C _ { 1 } \cdot \ell ( 2 \varrho + 1 )$

$$
h \Big | \Big | \sum _ { j = 0 } ^ { m } r _ { m - j } ( - h A ) \Delta g _ { j } \Big | \Big | _ { \beta } \leq h ^ { 1 - \gamma } L \sum _ { j = 0 } ^ { m } ( m - j + 1 ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } .
$$

c) The second term in (8.54) is the coefficient of $\zeta ^ { m }$ in

$$
h r ( \zeta , - h A ) \Delta s ( \zeta ) = \widetilde { r } ( \zeta ) \widetilde { \Delta s } ( \zeta )
$$

where we have introduced

$$
\begin{array} { r l } & { \widetilde { r } ( \zeta ) = \left( \delta ( \zeta ) I + h A \right) ^ { - 1 } h A \delta ( \zeta ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \displaystyle \sum _ { j \geq 0 } \widetilde { r } _ { j } \zeta ^ { j } } \\ & { \widetilde { \Delta } s ( \zeta ) = \displaystyle \delta ( \zeta ) A ^ { - 1 } \Delta s ( \zeta ) = \displaystyle \sum _ { j \geq 0 } \widetilde { \Delta } s _ { j } \zeta ^ { j } . } \end{array}
$$

In order to estimate $\| \widetilde { \boldsymbol { r } } _ { j } \| _ { \beta }$ (matrix norm) we note that $\vert \vert \widetilde { r } _ { j } \vert \vert _ { \beta } = \vert \vert \widetilde { r } _ { j } \vert \vert$ .In view of an application of Lemma 7.11 we have to consider $\Phi ( s ) { \overset { } { = } } ( s I + { \bar { A } } ) ^ { - 1 } A s ^ { - 1 } =$ $s ^ { - 1 } I - ( s I + A ) ^ { - 1 }$ which, because of (8.4O), is bounded by $( M + 1 ) / \vert s \vert$ . Lemma 7.11 thus yields $\| \widetilde { r } _ { j } \| _ { \beta } \le C _ { 2 }$ . Further we have

$$
\widetilde { \Delta s } ( \zeta ) = \frac { \delta ( \zeta ) } { 1 - \zeta } \cdot \Big ( A ^ { - 1 } \Delta s _ { k } \zeta ^ { k } + \sum _ { j \geq k + 1 } A ^ { - 1 } \big ( \Delta s _ { j } - \Delta s _ { j - 1 } \big ) \zeta ^ { j } \Big )
$$

where the coefficients of $\delta ( \zeta ) / ( 1 - \zeta )$ are absolutely summable, because the zeros of $\sigma ( \zeta )$ lie all inside $| \zeta | < 1$ . Combining all these estimates we get

$$
\begin{array} { r l } {  { \Big \| \sum _ { j = 0 } r _ { m - j } ( - h A ) \Delta s _ { j } \Big \| _ { \beta } = \Big \| \sum _ { j = 0 } \widetilde { r } _ { m - j } \widetilde { \Delta s } _ { j } \Big \| _ { \beta } } } \\ & { \leq C _ { 3 } \Big ( \| A ^ { - 1 } \Delta s _ { k } \| _ { \beta } + \displaystyle \sum _ { j = k + 1 } ^ { m } \big \| A ^ { - 1 } \big ( \Delta s _ { j } - \Delta s _ { j - 1 } \big ) \big \| _ { \beta } \Big ) } \\ & { \leq C _ { 4 } \Big ( \| A ^ { - 1 } s ( 0 ) \| _ { \beta } + \int _ { 0 } ^ { t _ { m } } \| A ^ { - 1 } s ^ { \prime } ( t ) \| _ { \beta } d t \Big ) . } \end{array}
$$

d) The last term in (8.54) can be estimated in the same way as the correspond-ing term in the proof of Theorem 7.10. We just have to take the norm (8.50) and get

$$
h \Big \| \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) d _ { j } \Big \| _ { \beta } \leq C _ { 5 } \bigg ( \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - \eta ( t _ { j } ) \| _ { \beta } + h ^ { p } \int _ { 0 } ^ { t _ { m } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t \bigg ) .
$$

e) Inserting (8.56), (8.57),and (8.58) into (8.54) gives

$$
\| \Delta y _ { m } \| _ { \beta } \leq h ^ { 1 - \gamma } L \sum _ { j = 0 } ^ { m } ( m - j + 1 ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } + C _ { 6 } \varepsilon _ { m }
$$

where $C _ { 6 } = \operatorname* { m a x } ( C _ { 4 } , C _ { 5 } )$ and $\varepsilon _ { m }$ denotes the expresson in brackets on the righthand side of (8.52). For $h \leq h _ { 0 }$ and $h _ { 0 } ^ { 1 - \gamma } L < 1$ this Gronwall-type inequality can be solved (Exercise 2) and gives $\| \Delta y _ { m } \| \le C _ { 7 } \varepsilon _ { m }$ , the desired result.

f) We now justify recurively our assumption $\| y _ { m } \| _ { \beta } \leq \varrho + 1$ used in (b). Sup-pose that $\| y _ { j } \| _ { \beta } \leq \varrho + 1$ for $j = 0 , 1 , \ldots , m - 1$ ,then it follows from $h ^ { 1 - \gamma } L < 1$ and the contraction mapping theorem that a unique solution $y _ { m }$ of (8.54) exists. This solution verifies $\| y _ { m } \| _ { \beta } \leq \| \eta ( t _ { m } ) \| _ { \beta } + \| \Delta y _ { m } \| _ { \beta } \leq \varrho + 1$ if $\varepsilon$ is small enough, more precisely, if $C _ { 7 } \varepsilon < 1$ □

Remark. A different approach to convergence results of multistep methods for nonlinear parabolic equations is given by Le Roux (198O). A corresponding theorem for Runge-Kutta methods is proved in Lubich & Ostermann (1993).

# Exercises

1. Let $L \geq 0$ and consider two sequences $\{ u _ { \ j } \}$ and $\{ \varepsilon _ { j } \}$ of nonnegative numbers which satisfy

$$
u _ { m } \leq h L \sum _ { j = 0 } ^ { m } u _ { j } + \sum _ { j = 0 } ^ { m } \varepsilon _ { j } \mathrm { f o r } m \geq 0 .
$$

Prove that for $h L \leq 1 - C ^ { - 1 }$

$$
u _ { m } \leq C e ^ { L C m h } \sum _ { j = 0 } ^ { m } \varepsilon _ { j } .
$$

Hint.Showby induction hat $\begin{array} { r } { v _ { m } \leq h \Lambda \sum _ { j = 0 } ^ { m - 1 } v _ { j } + M } \end{array}$ implies Um ≤M(1+hA)m ≤MeAmh .

2.Consider the inequality (8.59) with $\gamma < 1 , L \geq 0 , \varepsilon _ { m } \geq 0$ and $h > 0$ . Under the assumptions $h \leq h _ { 0 }$ and $h _ { 0 } ^ { 1 - \gamma } L < 1$ prove that there exists a constant $C$ such that $\| \Delta y _ { m } \| _ { \beta } \le C \varepsilon _ { m }$ for $m h \le T$

Hint. Move the term $h ^ { 1 - \gamma } L \| \Delta y _ { m } \| _ { \beta }$ to the left and divide the inequality by $\left( 1 - h ^ { 1 - \gamma } L \right)$ . This yields

$$
\| \Delta y _ { m } \| _ { \beta } \leq h ^ { 1 - \gamma } \hat { L } \sum _ { j = 0 } ^ { m - 1 } ( m - j ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } + \hat { \varepsilon } \quad \mathrm { f o r } \quad m \geq 0 .
$$

Show that $\| \Delta y _ { m } \| _ { \beta } \leq \widehat { \varepsilon } u ( m h )$ , where $u ( x )$ is the solution of

$$
u ( x ) = 1 + \widehat { L } \int _ { 0 } ^ { x } ( x - t ) ^ { - \gamma } u ( t ) d t .
$$

Estimate the solution of (8.60) (see Henry 1981, pp.188-190).

3. Let $A$ and $D$ be the matrices of (8.41) (suppose $\mu = 1$ ) and (8.46). Prove that for all $u \in \mathbb { R } ^ { n }$

$$
\begin{array} { r } { \| u \| _ { \infty } \leq \| A ^ { 1 / 2 } u \| , \qquad \mathsf { b } ) \quad \| D u \| \leq \| A ^ { 1 / 2 } u \| , } \end{array}
$$

where $\left\| u \right\| _ { \infty } = \operatorname* { m a x } _ { i } \left| u _ { i } \right|$ and $\| \cdot \|$ is the norm of (8.42).

H $u _ { 0 } = 0$ $\begin{array} { r } { \boldsymbol { u } _ { \iota } = \sum _ { j = 1 } ^ { i } ( \boldsymbol { u } _ { j } - \boldsymbol { u } _ { j - 1 } ) } \end{array}$

$$
\| u \| _ { \infty } ^ { 2 } \leq \sum _ { j = 1 } ^ { n } \Bigl ( \frac { u _ { j } - u _ { j - 1 } } { \Delta x } \Bigr ) ^ { 2 } = u ^ { T } A u .
$$

b） The inequality $u ^ { T } A u \geq \| D u \| ^ { 2 }$ is a consequence of the algebraic identity$( u _ { 0 } = u _ { n + 1 } = 0 )$ ）

$$
\begin{array} { c } { 4 \displaystyle \sum _ { \imath = 1 } ^ { n } ( 2 u _ { i } ^ { 2 } - u _ { \imath } u _ { i + 1 } - u _ { i } u _ { i - 1 } ) - \displaystyle \sum _ { i = 1 } ^ { n } ( u _ { i + 1 } - u _ { \imath - 1 } ) ^ { 2 } } \\ { = \displaystyle \sum _ { i = 1 } ^ { n } ( u _ { \imath + 1 } - 2 u _ { i } + u _ { \imath - 1 } ) ^ { 2 } + 2 u _ { 1 } ^ { 2 } + 2 u _ { n } ^ { 2 } . } \end{array}
$$

# V.9Algebraic Stability of General Linear Methods

General linear methods were originally introduced as a means of unifying and generalizing existing theories for traditional methods. (J.C.Butcher 1987)

In Sections IV.12 and V.6 we have studied the nonlinear stability of Runge-Kutta methods ( $B$ -stability) and of one-leg methods ( $G$ -stability). It is natural to ask whether these theories can be combined within the class of general linear methods. This work was initiated by Burrage & Butcher (1980).

We consider the differential equation ${ \boldsymbol { y } } ^ { \prime } { = } f ( { \boldsymbol { x } } , { \boldsymbol { y } } )$ where $y$ and $f$ are complexvalued vectors and we assume the one-sided Lipschitz condition

$$
\operatorname { R e } { \big \langle } f ( x , y ) - f ( x , z ) , y - z { \big \rangle } \leq \nu \| y - z \| ^ { 2 } .
$$

General linear methods are defined by (see Example 8.5 of Sect. II.8)

$$
\begin{array} { r l r } { \displaystyle } & { { } \displaystyle u _ { i } ^ { ( n + 1 ) } = \sum _ { j = 1 } ^ { k } a _ { i j } u _ { j } ^ { ( n ) } + h \sum _ { j = 1 } ^ { s } b _ { i j } f ( x _ { n } + c _ { j } h , v _ { j } ^ { ( n ) } ) , } & { i = 1 , \ldots , k } \\ { \displaystyle v _ { i } ^ { ( n ) } = \sum _ { j = 1 } ^ { k } \widetilde a _ { i j } u _ { j } ^ { ( n ) } + h \sum _ { j = 1 } ^ { s } \widetilde b _ { i j } f ( x _ { n } + c _ { j } h , v _ { j } ^ { ( n ) } ) , } & { i = 1 , \ldots , s . } \end{array}
$$

Here,un= (u（m)， $u _ { n } = ( u _ { 1 } ^ { ( n ) } , \ldots , u _ { k } ^ { ( n ) } ) ^ { T }$ cot vious step. The intermal stages $( v _ { 1 } ^ { ( n ) } , \ldots , v _ { s } ^ { ( n ) } )$ )，edyb)e computation of $u _ { n + 1 }$ in (9.2a).

# $\pmb { G }$ -Stability

As in Sect. V.6, we consider inner product norms

$$
\| u _ { n } \| _ { G } ^ { 2 } = \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { k } g _ { i j } \big \langle u _ { i } ^ { ( n ) } , u _ { j } ^ { ( n ) } \big \rangle ,
$$

where $G = ( g _ { i j } )$ is a real, symmetric and positive definite matrix.

Definition 9.1. The general linear method (9.2) is called $G$ -stable, if there exists a real, symmetric and positive definite matrix $G$ , such that for two numerical solutions $\{ u _ { n } \}$ and $\{ \widehat { u } _ { n } \}$ ，

$$
\lVert u _ { n + 1 } - \widehat { u } _ { n + 1 } \rVert _ { G } \leq \lVert u _ { n } - \widehat { u } _ { n } \rVert _ { G }
$$

for all step sizes $h > 0$ and for all differential equations satisfying (9.1) with $\nu = 0$ ·

For Runge-Kutta methods (where $k \approx 1$ and apart from a scaling factor $G =$ (1)）this definition reduces to $B$ -stability as introduced in Definition IV.12.2.For one-leg methods (where $s \simeq 1$ and $\boldsymbol { u } _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T } )$ it is equivalent to Definition 6.3.

Many methods can be written in different ways as general linear methods and the above definition of $G$ -stability may depend on the particular formulation. For example, the trapezoidal rule

$$
y _ { n + 1 } = y _ { n } + { \frac { h } { 2 } } { \bigl ( } f ( x _ { n } , y _ { n } ) + f ( x _ { n + 1 } , y _ { n + 1 } ) { \bigr ) }
$$

can be considered as a Runge-Kutta method (with $u _ { n } = y _ { n }$ ). In this case it is not $G$ -stable (because it is not $B$ -stable, see Theorem IV.12.12). However, if we let $u _ { n } = ( y _ { n } , h y _ { n } ^ { \prime } )$ where $y _ { n } ^ { \prime } = f ( x _ { n } , y _ { n } )$ , then the trapezoidal rule satisfies (9.4) with

$$
G = \left( \begin{array} { c c } { { 1 } } & { { 1 / 2 } } \\ { { 1 / 2 } } & { { 1 / 4 } } \end{array} \right) .
$$

This follows from the fact that whenever $\left\{ y _ { n } \right\}$ is the solution obtained by the trapezoidal rule, then $\begin{array} { r } { z _ { n } = y _ { n } + \frac { \displaystyle h } { \displaystyle 2 } y _ { n } ^ { \prime } } \end{array}$ is a solution of the implicit midpoint rule, which is known to be $B$ -stable (see Example IV.12.3 or Theorem IV.12.9). Therefore

$$
\| y _ { n + 1 } + { \frac { h } { 2 } } y _ { n + 1 } ^ { \prime } \| \leq \| y _ { n } + { \frac { h } { 2 } } y _ { n } ^ { \prime } \|
$$

which proves the statement. The matrix $G$ in (9.5) is singular and thus not strictly positive definite. Burrage & Butcher (198O), however, admit non-zero non-negative definite matrices $G$ in their definition of $G$ -stability (which they call monotonicity). Therefore the trapezoidal rule is $G$ -stable in their definition.

# Algebraic Stability

In addition to (9.2） we consider a second numerical solution (marked with hats) produced by the same method using different starting values. We denote the differences by

$$
\begin{array} { r l r l } & { \Delta u _ { \imath } ^ { ( n ) } = u _ { \imath } ^ { ( n ) } - \widehat { u } _ { \imath } ^ { ( n ) } , } & & { \Delta u _ { n } = u _ { n } - \widehat { u } _ { n } } \\ & { \Delta v _ { \imath } ^ { ( n ) } = v _ { \imath } ^ { ( n ) } - \widehat { v } _ { \imath } ^ { ( n ) } , } & & { \Delta f _ { \imath } ^ { ( n ) } = h \big ( f ( x _ { n } + c _ { \imath } h , v _ { \imath } ^ { ( n ) } ) - f ( x _ { n } + c _ { \imath } h , \widehat { v } _ { \imath } ^ { ( n ) } ) \big ) . } \end{array}
$$

The following lemma states an identity which will be essential in the study of $G$ - stability.

Lemma 9.2 (Burrage & Butcher 1980). Let $G$ be a real, symmetric matrix and $D = \mathrm { d i a g } \left( d _ { 1 } , \dots , d _ { s } \right)$ be a real diagonal matrix. The difference of two solutions of(9.2) then satisfies

$$
\| \Delta u _ { n + 1 } \| _ { G } ^ { 2 } - \| \Delta u _ { n } \| _ { G } ^ { 2 } = 2 \sum _ { \iota = 1 } ^ { s } d _ { i } \operatorname { R e } \left. \Delta f _ { i } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \right. - \sum _ { \iota , j = 1 } ^ { s + k } m _ { i j } \langle w _ { i } , w _ { \jmath } \rangle
$$

where $( w _ { 1 } , \dots , w _ { s + k } ) = \big ( \Delta u _ { 1 } ^ { ( n ) } , \dots , \Delta u _ { k } ^ { ( n ) } , \Delta f _ { 1 } ^ { ( n ) } , \dots , \Delta f _ { s } ^ { ( n ) } \big )$ and the matrix $M = ( m _ { \imath \jmath } )$ is given by

$$
M = \left( \begin{array} { c c } { { G - A ^ { T } G A } } & { { \widetilde { A } ^ { T } D - A ^ { T } G B } } \\ { { D \widetilde { A } - B ^ { T } G A } } & { { D \widetilde { B } + \widetilde { B } ^ { T } D - B ^ { T } G B } } \end{array} \right) .
$$

Proof. We consider the identity

$$
\begin{array} { r l } & { \displaystyle \| \Delta u _ { n + 1 } \| _ { G } ^ { 2 } - \| \Delta u _ { n } \| _ { G } ^ { 2 } - 2 \sum _ { \iota = 1 } ^ { s } d _ { \iota } \mathrm { R e } \left. \Delta f _ { \iota } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \right. } \\ & { \qquad = \displaystyle \sum _ { \iota , \eta = 1 } ^ { k } g _ { \iota j } \big \langle \Delta u _ { \iota } ^ { ( n + 1 ) } , \Delta u _ { \jmath } ^ { ( n + 1 ) } \big \rangle - \sum _ { \iota , \eta = 1 } ^ { k } g _ { \iota \jmath } \big \langle \Delta u _ { \iota } ^ { ( n ) } , \Delta u _ { \jmath } ^ { ( n ) } \big \rangle } \\ & { \qquad - \displaystyle \sum _ { \iota = 1 } ^ { s } d _ { \iota } \big \langle \Delta f _ { \iota } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \big \rangle - \sum _ { \iota = 1 } ^ { s } d _ { \iota } \big \langle \Delta v _ { \iota } ^ { ( n ) } , \Delta f _ { \iota } ^ { ( n ) } \big \rangle } \end{array}
$$

and insert the formulas (9.2). This gives

$$
\ldots = \sum _ { i , j = 1 } ^ { k } g _ { i j } \Bigl \langle \sum _ { \ell = 1 } ^ { k } a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } , \sum _ { \ell = 1 } ^ { k } a _ { j \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } b _ { j \ell } \Delta f _ { \ell } ^ { ( n ) } \Bigr \rangle
$$

$$
\begin{array} { c } { { \displaystyle \phantom { \displaystyle \sum _ { i , j = 1 } ^ { k } \sum _ { \ell = 1 } ^ { \ell = 1 } } \varepsilon _ { \ell = 1 } } } \\ { { \displaystyle - \sum _ { \imath , \jmath = 1 } ^ { k } g _ { i j } \bigl \langle \Delta u _ { i } ^ { ( n ) } , \Delta u _ { j } ^ { ( n ) } \bigr \rangle - \sum _ { i = 1 } ^ { s } d _ { i } \Bigl \langle \Delta f _ { \imath } ^ { ( n ) } , \sum _ { \ell = 1 } ^ { k } \widetilde a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } \widetilde b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } \Bigr \rangle } } \\ { { \displaystyle - \sum _ { i = 1 } ^ { s } d _ { i } \Bigl \langle \sum _ { \ell = 1 } ^ { k } \widetilde a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } \widetilde b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } , \Delta f _ { i } ^ { ( n ) } \Bigr \rangle . } } \end{array}
$$

Multiplying out and collecting suitable terms proves the statement.

Definition 9.3. The general linear method (9.2) is called algebraically stable, if there exist a real, symmetric and positive definite matrix $G$ and a real non-negative definite diagonal matrix $D$ , such that the matrix $M$ of (9.6) is non-negative definite.

An immediate consequence of our assumption (9.1） with $\nu = 0$ and of Lem-$\mathrm { \ m a } 9 . 2$ is the following result.

Theorem 9.4. Algebraic stability implies $G$ -stability.

For a given method it may be difficult to find matrices $D$ and $G$ such that $M$ of (9.6) is non-negative definite. The following lemma shows some useful relations, which hold if the method is assumed to be preconsistent, i.e.,if there exists a vector $\xi _ { 0 } \in \mathbb { R } ^ { k }$ such that

$$
A \xi _ { 0 } = \xi _ { 0 } , \qquad \widetilde A \xi _ { 0 } = 1 1
$$

(cf. Eq. (8.25) of Sect.II.8).

Lemma 9.5. If $a$ general linear method is preconsistent and algebraically stable, then the matrices $D$ and $G$ satisfy

i） $( d _ { 1 } , \ldots , d _ { s } ) ^ { T } = D \mathbb { 1 } = B ^ { T } G \xi _ { 0 } ,$   
$i i )$ $( I - A ^ { T } ) G \xi _ { 0 } = 0$ ,i.e.， $G \xi _ { 0 }$ is $a$ left-eigenvector of $A$ corresponding to the eigenvalue $l$

Proof. i) Let $\eta \in \mathbb { R } ^ { s }$ and $\varepsilon \in \mathbb { R }$ be arbitrary. The non-negativity of $M$ ， given by (9.6), implies

$$
( \xi _ { 0 } ^ { T } , \varepsilon \eta ^ { T } ) M \left( \xi _ { 0 } \atop \varepsilon \eta \right) \geq 0
$$

so that

$$
\begin{array} { r } { \xi _ { 0 } ^ { T } ( G - A ^ { T } G A ) \xi _ { 0 } + 2 \varepsilon \eta ^ { T } ( D \widetilde { A } - B ^ { T } G A ) \xi _ { 0 } + \varepsilon ^ { 2 } \eta ^ { T } ( D \widetilde { B } + \widetilde { B } ^ { T } D - B ^ { T } G B ) \eta \ge 0 . } \end{array}
$$

Since the $\varepsilon$ -independent term vanishes (due to $A \xi _ { 0 } = \xi _ { 0 } )$ , the coefficient of $\varepsilon$ must be zero and since this holds for all $\eta$ , the result follows.

ii) A similar argument applied to

$$
( \xi _ { 0 } + \varepsilon \xi _ { 1 } ) ^ { T } ( G - A ^ { T } G A ) ( \xi _ { 0 } + \varepsilon \xi _ { 1 } ) \geq 0 \quad \mathrm { ~ f o r ~ a l l ~ } \quad \xi _ { 1 } \in \mathbb { R } ^ { k } , \ \varepsilon \in \mathbb { R }
$$

implies the second statement.

# $\mathbf { \nabla } A \mathcal { N }$ -Stability and Equivalence Results

It is interesting to study in which situation algebraic stability is also necessary for $G$ -stability. For this we consider the differential equation

$$
y ^ { \prime } = \lambda ( x ) y \qquad { \mathrm { w i t h } } \qquad { \mathrm { R e } } \lambda ( x ) \leq 0 .
$$

If we apply the general linear method (9.2) to this problem, we obtain

$$
u _ { n + 1 } = S ( Z ) u _ { n }
$$

where $Z = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right) , z _ { j } = h \lambda ( x _ { n } + c _ { j } h )$ and

$$
S ( Z ) = A + B Z ( I - \widetilde { B } Z ) ^ { - 1 } \widetilde { A } .
$$

In the sequel we assume that the abscissae $c _ { \ j }$ are related to the other coefficients of the method by (see also Remark III.8.17)

$$
\begin{array} { r } { \left( c _ { 1 } , \dots , c _ { s } \right) ^ { T } = c = \widetilde { A } \xi _ { 1 } + \widetilde { B } \mathbb { 1 } , } \end{array}
$$

where $\xi _ { 1 } \in \mathbb { R } ^ { k }$ is the second coeficient vector of the exact value function

$$
z ( x , h ) = y ( x ) \xi _ { 0 } + h y ^ { \prime } ( x ) \xi _ { 1 } + \mathcal { O } ( h ^ { 2 } ) .
$$

This means that the internal stages approximate the exact solution as $v _ { \jmath } ^ { ( n ) } = y ( x _ { n } + c _ { j } h ) + { \mathcal O } ( h ^ { 2 } ) .$

Definition 9.6. A general linear method is called $A N$ -stable,if there exists a real, symmetric and positive definite matrix $G$ such that

$$
\begin{array} { r l r l } & { \| S ( Z ) u \| _ { G } \le \| u \| _ { G } } & & { \mathrm { f o r ~ a l l ~ } Z = \mathrm { d i a g } \left( z _ { 1 } , \ldots , z _ { s } \right) \mathrm { ~ s a t i s f y i } } \\ & { } & & { ( j = 1 , \ldots , s ) \mathrm { a n d ~ } z _ { j } = z _ { k } \mathrm { ~ w h e n e v e } } \end{array}
$$

Other possible definitions of $A N$ -stability are given in Butcher (1987).For example,if the condition $\| S ( Z ) u \| _ { G } \leq \| u \| _ { G }$ is replaced by the powerboundedness of the matrix $S ( Z )$ , the method is called weakly $A N$ -stable. This definition, however, does not allow the values $z _ { \jmath } = h \lambda ( x _ { n } + c _ { j } h )$ to change at each step. Another modification is to consider arbitrary norms (instead of inner product norms only) in the definition of $A N$ -stability. Butcher (1987) has shown that this does not lead to a larger class of $A N$ -stable methods,but makes the analysis much more difficult.

We are now interested in the relations between the various stability definitions: the implications

are either trivial or follow from Theorem 9.4. We also know that $A$ -stability does not, in general, imply $A N$ -stability (see e.g.,Theorem IV.12.12). The following result shows that the other two implications are (nearly always) reversible.

Theorem 9.7 (Butcher 1987). For preconsistent and non-confluent general linear methods (i.e., methods with distinct $c _ { j }$ ) we have

Proof. It is sufficient to prove that $A N$ -stability implies algebraic stability. For this we take the matrix $G$ ，whose existence is known by the definition of $A N \mathrm { ~ - ~ }$ stability, and show that the matrices $D$ and $M$ ， given by Lemma 9.5i and (9.6), are non-negative definite.

In order to prove $d _ { \jmath } \geq 0$ we put $z _ { \jmath } = - \varepsilon \ ( \varepsilon > 0 )$ and $z _ { k } = 0$ for $k \neq j$ .We further let $\Delta u _ { n } = \xi _ { 0 }$ (eecoss) $\Delta f _ { \ell } ^ { ( n ) } = z _ { \ell } \Delta v _ { \ell } ^ { ( n ) }$ so hat $\Delta u _ { n + 1 } = S ( Z ) \xi _ { 0 }$ and $\Delta v _ { \ell } ^ { ( n ) } = 1 + \mathcal { O } ( \varepsilon )$ . Using

$$
M \binom { \xi _ { 0 } } { 0 } = 0 ,
$$

which is a consequence of Lemma 9.5, the identity of Lemma 9.2 yields

$$
\lVert S ( Z ) \xi _ { 0 } \rVert _ { G } ^ { 2 } - \lVert \xi _ { 0 } \rVert _ { G } ^ { 2 } = - 2 \varepsilon d _ { \jmath } + \mathcal { O } ( \varepsilon ^ { 2 } ) .
$$

Since the left-hand side of this equation is non-positive by $A N$ -stability, we obtain $d _ { \jmath } \geq 0$

We next put $z _ { \ell } = i \varepsilon \eta _ { \ell }$ where $\eta = ( \eta _ { 1 } , \ldots , \eta _ { s } ) ^ { T } \in \mathbb { R } ^ { s }$ is arbitrary and $\mathcal { E }$ isa small real parameter. We further put $\Delta u _ { n } = \xi _ { 0 } + \imath \varepsilon _ { k }$ with $\mu \in \mathbb { R } ^ { k }$ and $\Delta f _ { \ell } ^ { ( n ) } =$ ${ \boldsymbol { z } } _ { \ell } \Delta { \boldsymbol { v } } _ { \ell } ^ { ( n ) }$ This aganimplies $\Delta v _ { \ell } ^ { ( n ) } = 1 + \mathcal { O } ( \varepsilon )$ The identyofLema9.2t10- gether with (9.11) gives

$$
\begin{array} { c } { { \| S ( Z ) \xi _ { 0 } \| _ { G } ^ { 2 } - \| \xi _ { 0 } \| _ { G } ^ { 2 } = - \big ( \xi _ { 0 } - i \varepsilon \mu , \iota \varepsilon \eta + { \mathcal O } ( \varepsilon ^ { 2 } ) \big ) M \biggl ( \begin{array} { c } { { \xi _ { 0 } + i \varepsilon \mu } } \\ { { i \varepsilon \eta + { \mathcal O } ( \varepsilon ^ { 2 } ) } } \end{array} \biggr ) = } } \\ { { = - \varepsilon ^ { 2 } ( \mu , \eta ) ^ { T } M \biggl ( \begin{array} { c } { { \mu } } \\ { { \eta } } \end{array} \biggr ) + { \mathcal O } ( \varepsilon ^ { 3 } ) . } } \end{array}
$$

Since this relation holds for all $\mu$ and $\eta$ ， the matrix $\mathcal { M }$ has to be non-negative definite. □

Example 9.8. Let us investigate the $G$ -stability of multistep collocation methods as introduced in Sect. V.3. We consider here the case $k = 2$ and $s  2$ ,and fix one collocation point at $c _ { 2 } \simeq 1$ . The method is then given by

$$
\begin{array} { r l } & { ( \begin{array} { c } { \varepsilon _ { ( g _ { n + 1 } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \end{array} ) = \overbrace { ( \begin{array} { c c } { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } & { \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } \\ { 1 } & { 0 } \end{array} ) } ^ { \mathcal { A } } \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n } ) } } \\ { g _ { n - 1 } } \end{array} \bigg ) } ^ { \mathcal { B } }  \\ & { \qquad + \hbar \overbrace { ( \begin{array} { c c } { \varphi _ { ( 1 ) } ^ { \varepsilon } ( 1 ) } & { \varphi _ { ( 2 ) } ^ { \varepsilon } ( 1 ) } \\ { 0 } & { \varphi _ { ( 2 ) } ^ { \varepsilon } ( 1 ) } \end{array} ) } ^ { g _ { n } } \bigg ( \overbrace { f ( \varepsilon _ { ( g _ { n } ) } + \varepsilon _ { ( h , \varphi _ { ( 1 ) } ) } } ^ { \mathcal { B } } \bigg ) } \\ & { \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \end{array} ) = \underbrace { ( \begin{array} { c c } { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon } } & { \varphi _ { ( 1 ) } ^ { \varepsilon } } \\ { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } & { \varphi _ { ( 1 ) } ^ { \varepsilon } } \end{array} ) } _ { \mathcal { A } } \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n - 1 } ) } } \\ { g _ { n - 1 } } \end{array} \bigg ) } \\ &  \qquad + \hbar \underbrace  \bigg ( \begin{array} { c c } { \Phi _ { 1 } ( \varepsilon _ { ( 1 ) } ^ { \varepsilon } } & { \psi _ { ( 1 ) } ^ { \varepsilon } ( \varepsilon _ { ( g _ { n } ) } ^ { \varepsilon } ) } \\  \Phi _ { 1 } ( \underset { \varepsilon _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } { \varepsilon _ { ( g _ { n } ) } ^ { \varepsilon _ { ( 1 ) } } } &  \psi _ \end{array} \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle \varphi ( x ) = - \frac { 6 } { 5 + 9 c _ { 1 } } \left( \frac { x ^ { 3 } } { 3 } - \frac { x ^ { 2 } } { 2 } ( 1 + c _ { 1 } ) + x c _ { \mathrm { t } } \right) } \\ { \displaystyle \psi _ { \mathrm { I } } ( x ) = \frac { x ( x + 1 ) } { ( 1 - c _ { 1 } ) ( 5 + 9 c _ { 1 } ) } \left( 5 - 3 x \right) } \\ { \displaystyle \psi _ { \mathrm { 2 } } ( x ) = \frac { x ( x + 1 ) } { ( 1 - c _ { 1 } ) ( 5 + 9 c _ { 1 } ) } \left( ( 2 c _ { \mathrm { t } } + 1 ) x - c _ { \mathrm { t } } ( 3 c _ { 1 } + 2 ) \right) . } \end{array}
$$

Wc know from Exercise V.3.7 that the method is $A$ -stable if and only if $c _ { 1 } \geq$ $( \sqrt { 1 7 } - 1 ) / 8$ . For the study of its $G$ -stability we assume that after an appropriate

scaling of $G$ ， $g _ { 1 1 } = 1$ . By Lemma 9.5ii the matrix $G$ must then be of the form (recall that $\xi _ { 0 } = ( 1 , 1 ) ^ { T } .$ ）

$$
G = \left( \begin{array} { c c } { { 1 } } & { { \gamma - 1 } } \\ { { \gamma - 1 } } & { { ( \varphi ( 1 ) - 1 ) \gamma + 1 } } \end{array} \right) .
$$

A necessary condition for $G$ to be positive definite is that det $G > 0$ .For $c _ { 1 } \geq 0$ this is equivalent to

$$
0 < \gamma < \frac { 6 ( 1 + c _ { 1 } ) } { 5 + 9 c _ { 1 } } .
$$

Next we use Lemma 9.5i which implies that

$$
d _ { 1 } = \gamma \psi _ { 1 } ( 1 ) , \qquad d _ { 2 } = \gamma \psi _ { 2 } ( 1 ) .
$$

Inserting (9.13) and (9.15) into the matrix $M$ of (9.6) yields for its lower right block

$$
\left( \begin{array} { c c } { { \psi _ { 1 } ( 1 ) } } & { { 0 } } \\ { { 0 } } & { { \psi _ { 2 } ( 1 ) } } \end{array} \right) \left( \begin{array} { c c } { { 2 \gamma \chi _ { 1 } - 1 } } & { { ( \chi _ { 2 } + 1 ) \gamma - 1 } } \\ { { ( \chi _ { 2 } + 1 ) \gamma - 1 } } & { { . } } \end{array} \right) \left( \begin{array} { c c } { { \psi _ { 1 } ( 1 ) } } & { { 0 } } \\ { { 0 } } & { { \psi _ { 2 } ( 1 ) } } \end{array} \right) \nonumber
$$

where

$$
\chi _ { 1 } = \frac { \psi _ { 1 } ( c _ { 1 } ) } { \psi _ { 1 } ( 1 ) } = \frac { 1 } { 4 } c _ { 1 } ( c _ { 1 } + 1 ) ( 5 - 3 c _ { 1 } ) , \qquad \chi _ { 2 } = \frac { \psi _ { 2 } ( c _ { 1 } ) } { \psi _ { 2 } ( 1 ) } = \frac { c _ { 1 } ^ { 2 } ( c _ { 1 } + 1 ) ^ { 2 } } { 2 ( 3 c _ { 1 } ^ { 2 } - 1 ) } .
$$

A direct computation (see Exercise 2) shows that this $2 \times 2$ matrix can not be non-negative definite for $c _ { 1 } \geq ( \sqrt { 1 7 } - 1 ) / 8$ and $\gamma$ satisfying (9.14). Consequently the considered methods are never $G$ -stable.

In the next subsections we shall show how high-order algebraically stable general linear methods can be constructed.

# Multistep Runge-Kutta Methods

An interesting extension of multistep collocation methods are the so-called multi-step Runge-Kutta methods. They are defined by the formulas

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } y _ { n + 1 - \jmath } + h \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ^ { ( n ) } ) } } \\ { { \displaystyle v _ { \imath } ^ { ( n ) } = \sum _ { \jmath = 1 } ^ { k } \widetilde a _ { \imath \jmath } y _ { n + 1 - \jmath } + h \sum _ { \jmath = 1 } ^ { s } \widetilde b _ { \imath \jmath } f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ^ { ( n ) } ) . } } \end{array}
$$

They obviously form a subclass of the general linear methods (9.2). This is seen by putting $u _ { n } = ( y _ { n } , y _ { n - 1 } , \ldots , y _ { { n - k + 1 } } ) ^ { T }$ so that the exact value function is

$$
z ( x , h ) = \bigl ( y ( x ) , y ( x - h ) , \ldots , y ( x - ( k - 1 ) h ) \bigr ) ^ { T } .
$$

Further, the matrices $A$ and $B$ have the special form

$$
A = \left( \begin{array} { c c c c } { { \alpha _ { 1 } } } & { { \cdot \cdot \cdot } } & { { \cdot \cdot \cdot } } & { { \alpha _ { k } } } \\ { { 1 } } & { { } } & { { } } & { { 0 } } \\ { { } } & { { \cdot \cdot } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { 1 } } & { { 0 } } \end{array} \right) , \qquad B = \left( \begin{array} { c c c } { { b _ { 1 } } } & { { \cdot \cdot \cdot } } & { { b _ { s } } } \\ { { 0 } } & { { \cdot \cdot } } & { { 0 } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { 0 } } & { { \ldots } } & { { 0 } } \end{array} \right) .
$$

The order conditions for such methods were derived in Theorem III.8.14. It follows from this theorem that the method (9.17) is of order $p$ ,iff

$$
1 = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } { \left( 1 - j \right) } ^ { \varrho { \left( t \right) } } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } { \mathbf { v } _ { \jmath } ^ { \prime } } { \left( t \right) } \quad { \mathrm { ~ f o r ~ } } \quad t \in T , \varrho { \left( t \right) } \leq p .
$$

The values $\mathbf { v } _ { \ j } ^ { \prime } ( t )$ are given recursively by

$$
\mathbf { v } _ { \ i } ( t ) = \sum _ { \jmath = 1 } ^ { k } \widetilde { a } _ { \imath \jmath } ( 1 - \jmath ) ^ { \varrho ( t ) } + \sum _ { \jmath = 1 } ^ { s } \widetilde { b } _ { \imath \jmath } \mathbf { v } _ { \jmath } ^ { \prime } ( t ) .
$$

Recall from Corollary II.12.7 that

$$
\begin{array} { r l r } & { \mathbf v _ { \ j } ^ { \prime } ( \emptyset ) = 0 , \qquad \mathbf v _ { \ j } ^ { \prime } ( \tau ) = 1 } \\ & { \mathbf v _ { \ j } ^ { \prime } ( t ) = \varrho ( t ) \mathbf v _ { \ j } ( t _ { 1 } ) \cdot \dots \cdot \mathbf v _ { \ j } ( t _ { m } ) } & { \mathrm { ~ i f ~ } \quad t = [ t _ { 1 } , \dots , t _ { m } ] . } \end{array}
$$

The order conditions (9.19) constitute a system of nonlinear equations in the coefficients of the method. Without any preparation, solving them may be difficult. We therefore introduce additional assumptions which simplify the construction of multistep Runge-Kutta methods.

# Simplifying Assumptions

The conditions $B ( p ) , C ( \eta )$ and $D ( \xi )$ of Sect.IV.5 were useful for the construction of high-order implicit Runge-Kutta methods. Burrage （1988） showed how these simplifying assumptions can be extended to general linear methods. In the sequel we specialize his approach to multistep Runge-Kutta methods. We consider the assumptions

$$
\begin{array} { l l l l l } { { } } & { { } } & { { \displaystyle { B ( p ) : \frac { q \overset { A } { \sum } b _ { j } c _ { j } ^ { q - 1 } + \sum _ { j = 1 } ^ { k } \alpha _ { j } ( 1 - j ) ^ { q } = 1 } } } } & { { \quad \mathrm { ~ } } } & { { \mathrm { ~ } q = 1 , \ldots , p ; } } \\ { { } } & { { } } & { { \displaystyle { C ( \eta ) : \frac { s } { \eta = 1 } \widetilde b _ { j } c _ { j } ^ { q - 1 } + \sum _ { j = 1 } ^ { k } \widetilde a _ { j } ( 1 - j ) ^ { q } = c _ { i } ^ { q } } } } & { { \quad \mathrm { ~ } q = 1 , \ldots , \eta , \mathrm { ~ a l l ~ i ; } } } \\ { { } } & { { } } &   \displaystyle { \begin{array} { l } { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { ~ } { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle { \mathcal { ~ } { D } _ { \mathrm { { a } } } ( \xi ) : \frac { s } { \mathcal { } } \sum _ { j = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } \widetilde a _ { i j } = \alpha _ { j } \left( 1 - ( 1 - j ) ^ { q } \right) } } } & { { \quad \mathrm { ~ } } } & { { \mathrm { ~ } q = 1 , \ldots , \xi , \mathrm { ~ a l l ~ } j ; } } \\ { { } } & { { } } &   \displaystyle  \begin{array} { l } { { \mathrm { ~ } } } \\  { \mathrm { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal    \end{array} \end{array} \end{array}
$$

Condition $B ( p )$ is equivalent to the order conditions (9.19) for bushy trees.Condition $C ( \eta )$ means that $\mathbf { v } _ { \jmath } ( t )$ ,defined by (9.20),satisfies

$$
\mathbf { v } _ { \boldsymbol { \jmath } } ( t ) = c _ { \boldsymbol { j } } ^ { \varrho ( t ) } \quad \mathrm { ~ f o r ~ } \quad \varrho ( t ) \leq \boldsymbol { \eta } .
$$

We remark that the preconsistency condition (9.7) with $\xi _ { 0 } = ( 1 , \ldots , 1 ) ^ { T }$ ，

$$
\sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } = 1 , \qquad \sum _ { \jmath = 1 } ^ { k } { \widetilde a } _ { \imath \jmath } = 1 \quad \mathrm { f o r } \quad i = 1 , \dots , s ,
$$

is obtained by putting $q = 0$ in $B ( p )$ and $C ( \eta )$ . The condition $D ( \xi )$ for Runge-Kutta methods splits into $D _ { A } ( \boldsymbol { \xi } )$ and $D _ { B } ( \boldsymbol { \xi } )$ . However, under certain assumptions one of these conditions is automatically satisfied.

Lemma 9.9. Suppose that the coefficients $c _ { 1 } , \ldots , c _ { s }$ of a multistep Runge-Kutta method are distinct and $\boldsymbol { b } _ { \imath } \neq 0$ . Then,

$$
\begin{array} { r l } & { B ( \xi + k - 1 ) , C ( k - 1 ) , D _ { B } ( \xi ) \Longrightarrow D _ { A } ( \xi ) , } \\ & { B ( \xi + s ) , C ( s ) , D _ { A } ( \xi ) \Longrightarrow D _ { B } ( \xi ) , } \\ & { B ( \eta + s ) , D _ { A } ( s ) , D _ { B } ( s ) \Longrightarrow C ( \eta ) . } \end{array}
$$

Proof. The first two implications are aconsequence of the identity

$$
\begin{array} { c } { { \displaystyle \sum _ { \jmath = 1 } ^ { k } \biggl ( q \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \widetilde a _ { \imath \jmath } - \alpha _ { \jmath } \bigl ( 1 - ( 1 - j ) ^ { q } \bigr ) \biggr ) ( 1 - j ) ^ { \ell } } } \\ { { = - \ell \displaystyle \sum _ { \jmath = 1 } ^ { s } \biggl ( q \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \widetilde b _ { \imath \jmath } - b _ { \jmath } \bigl ( 1 - c _ { \jmath } ^ { q } \bigr ) \biggr ) c _ { \jmath } ^ { \ell - 1 } } } \end{array}
$$

which holds under the assumptions $C ( \ell )$ and $B ( q + \ell )$ . The last implication can be proved similarly. □

The fundamental theorem, which generalizes Theorem IV.5.1, is

Theorem 9.10 (Burrage 1988). If the coefficients of $a$ multistep Runge-Kutta method (9.17) satisfy the simplifying assumptions $B ( p )$ ， $C ( \eta )$ ， $D _ { A } ( \boldsymbol { \xi } )$ ， $D _ { B } ( \boldsymbol { \xi } )$ with $p \leq \eta + \xi + 1$ and $p \leq 2 \eta + 2$ ,then the method is of order $p$

Proof. The conditions $C ( \eta )$ and $D _ { A } ( \xi ) , D _ { B } ( \xi )$ allow the reduction of order conditions of trees as sketched in Fig.7.1 and Fig.7.2 of Sect.I.7,respectively. Under the restrictions $p \leq \eta + \xi + 1$ and $p \leq 2 \eta + 2$ all order conditions reduce to those for bushy trees which are satisfied by $B ( p )$ □

Remember that we are searching for high-order algebraically stable methods. Due to the Daniel-Moore conjecture (Theorem V.4.4) the order is restricted by $p \leq 2 s$ . It is therefore natural to look for methods satisfying $B ( 2 s )$ ， $C ( s )$ and

$D _ { A } ( s ) , D _ { B } ( s )$ . They will be of order $2 . 5$ by Theorem 9.10 and are an extension of the Runge-Kuta methods based on Gauss quadrature. Let us begin by studying the condition $B ( 2 s )$

# Quadrature Formulas

Because of (9.23) condition $B ( p )$ of the preceding subsection is equivalent to

$$
\sum _ { j = 1 } ^ { s } b _ { \ u _ { j } } f ( c _ { \ u _ { j } } ) = \sum _ { j = 1 } ^ { k } \alpha _ { \ u _ { j } } \int _ { 1 - j } ^ { 1 } f ( x ) d x , \qquad \deg f \le p - 1 ,
$$

where $f$ stands for a polynomial of degree at most $p - 1$ . For the construction of such quadrature formulas it is useful to consider the bilinear form

$$
\langle f , g \rangle = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } f ( x ) g ( x ) d x = \int _ { 1 - k } ^ { 1 } \omega ( x ) f ( x ) g ( x ) d x ,
$$

where $\omega ( x )$ is the step-function sketched in Fig.9.1. Under the assumption

$$
\alpha _ { k } \geq 0 , \quad \alpha _ { k } + \alpha _ { k - 1 } \geq 0 , \ldots , \quad \alpha _ { k } + \ldots + \alpha _ { 2 } \geq 0 , \quad \alpha _ { k } + \ldots + \alpha _ { 1 } = 1 ,
$$

$\omega ( x )$ is non-negative and (9.25) becomes an inner product on the space of real polynomials. We call the quadrature formula (9.24) interpolatory if $B ( s )$ holds. This implies that

$$
b _ { \imath } = \int _ { 1 - k } ^ { 1 } \omega ( x ) \ell _ { i } ( x ) d x . \qquad \ell _ { \imath } ( x ) = \prod _ { \imath = 1 } ^ { s } \frac { ( x - c _ { \imath } ) } { ( c _ { \imath } - c _ { \imath } ) } .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/95bb9af32ca7f9a90f861f13d645fbd650a2e406a493de09a933000aaa87e583.jpg)  
Fig.9.1. Weight function for the inner product (9.25)

The following results on Gaussian quadrature and orthogonal polynomials are classical.

Lemma 9.11. Let $M ( x ) = ( x - c _ { 1 } ) \cdot . . . \cdot ( x - c _ { s } )$ . An interpolatory quadrature formula satisfies $B ( s + m )$ if and only if

$$
\sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } M ( x ) x ^ { q - 1 } d x = 0 \quad f o r \quad q = 1 , \ldots , m .
$$

Let $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ be the polynomial of degree s which is orthogonal with respect to (9.25) to all polynomials of degree $s \sim 1$ . Lemma 9.11 then states that a quadrature formula (9.24) is of order 2s iff $M ( x )$ is a scalar multiple of $p _ { s } ( x )$ .The polynomials $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ which depend on $\alpha _ { 1 } , \ldots , \alpha _ { k }$ via the bilinear form (9.25) can be computed from a standard three term recursion

$$
p _ { 0 } ( x ) = 1 , \qquad p _ { 1 } ( x ) = x - \beta _ { 0 }
$$

$$
p _ { s + 1 } ( x ) = ( x - \beta _ { s } ) p _ { s } ( x ) - \gamma _ { s } p _ { s - 1 } ( x )
$$

where

$$
\beta _ { s } = \frac { \langle x p _ { s } , p _ { s } \rangle } { \langle p _ { s } , p _ { s } \rangle } , \qquad \gamma _ { s } = \frac { \langle p _ { s } , p _ { s } \rangle } { \langle p _ { s - 1 } , p _ { s - 1 } \rangle } .
$$

Obviously this is only possible if $\langle p _ { \jmath } , p _ { \jmath } \rangle \neq 0$ for $j = 1 , \dots , s$ . This is certainly the case under the assumption (9.26).

Lemma 9.12. If $\alpha _ { 1 } , \ldots , \alpha _ { k }$ satisfy (9.26) then all zeros of $p _ { s } ( x )$ are real, simple and lie in the open interval $( 1 - k , 1 )$ □

For the construction of algebraically stable methods, quadrature formulas with positive weights willbe of particular interest. Suficient conditions for this property are given in the following theorem.

Theorem 9.13. If the quadrature formula (9.24) is of order $p \geq 2 s - 1$ and if $\alpha _ { 1 } , \ldots , \alpha _ { k }$ satisfy (9.26), then

$$
b _ { \imath } > 0 \qquad f o r \qquad i = 1 , \ldots , s .
$$

# Algebraically Stable Methods of Order $\pmb { 2 s }$

... the analysis of the algebraic stability properties of multivalue methods... is not as dificult as was generally thought ...

(Burrage 1987)

Following Burrage (1987） we consider the following class of multistep Runge-Kutta methods.

Definition 9.14. Let $\alpha _ { 1 } , \ldots , \alpha _ { k }$ with $\sum \alpha _ { \ j } = 1$ and $\alpha _ { k } \neq 0$ be given such that the zeros $c _ { 1 } , \ldots , c _ { s }$ of $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ (Formula(9.28))are real and simple. We then denote

by $E ( \alpha _ { 1 } , \dots , \alpha _ { k } )$ the multistep Runge-Kutta method (9.17) whose coeficients are given by

$$
\begin{array} { r l } & { \displaystyle b _ { \imath } = \sum _ { j = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s , } \\ & { \displaystyle \widetilde a _ { \imath \jmath } = \frac { \alpha _ { \jmath } } { b _ { \jmath } } \int _ { 1 - \jmath } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s ; \ \jmath = 1 , \ldots { / k } } \\ & { \displaystyle \widetilde b _ { \imath } = \frac { b _ { \jmath } } { b _ { \jmath } } \int _ { c _ { \jmath } } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s ; \ j = 1 , \ldots s } \end{array}
$$

where $\boldsymbol { \ell } _ { \boldsymbol { \imath } } ( \boldsymbol { x } )$ is the function of (9.27).

The definitions of $c _ { \iota }$ and $b _ { \imath }$ imply $B ( 2 s )$ by Lemma 9.11. The formulas for a and $\widetilde { \boldsymbol { b } } _ { \iota \boldsymbol { j } }$ are equivalent to $D _ { A } ( s )$ and $D _ { B } ( s )$ , respectively. Lcmma 9.9ii thus implies $\check { C } ( s )$ and Theorem 9.1O finally proves that the considered methods are of order $2 \mathit { s }$ . The following theorem gives sufficient conditions for the algebraic stability of these methods.

Theorem 9.15 (Burrage 1987).If $\alpha _ { _ { \mathscr { I } } } \geq 0$ for $j = 1 , \dots , k ^ { \prime }$ ， then the method $E ( \alpha _ { 1 } , \dots , \alpha _ { k } )$ is $G$ -stable with

$$
G = \mathrm { d i a g } ( 1 , \alpha _ { 2 } + \ldots + \alpha _ { k } , \ldots , \alpha _ { k - 1 } + \alpha _ { k } , \alpha _ { k } ) .
$$

Proof. For multistep Runge-Kutta methods the preconsistency vector is given by $\xi _ { 0 } = ( 1 , 1 , \dots , 1 ) ^ { T }$ . With the matrix $G$ of (9.30) it therefore follows from Lemma 9.5 that

$$
d _ { \ i } = b _ { \ i } \qquad \mathrm { f o r } \qquad i = 1 , \ldots , s .
$$

By Theorem 9.13 this implies $d _ { i } > 0$ so that the first condition for algebraic stability is satisfied. In order to verify that the matrix $M$ of (9.6) is non-negative definite, we transform it by a suitable matrix. We put

$$
V = \left( c _ { \iota } ^ { \jmath - 1 } \right) _ { \iota , \jmath = 1 , \ . , s } \quad \mathrm { ~ a n d ~ } \quad \alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { k } ) ^ { T } .
$$

A straightforward calculation using the simplifying assumptions $D _ { \Lambda } ( s ) , D _ { \cal B } ( s )$ and $B ( 2 s )$ shows that

$$
\left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { V ^ { T } } } \end{array} \right) M \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} \right) = \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W ^ { T } } } \end{array} \right) \widehat { M } \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W } } \end{array} \right)
$$

where

$$
W = \left( \frac { 1 } { \jmath } ( 1 - i ) ^ { \jmath } \right) _ { \imath = 1 , \ldots , k }
$$

and the $2 k \times 2 k$ matrix $\widehat { M }$ is given by

$$
{ \widehat { M } } = \left( { \begin{array} { l l } { Z } & { Z } \\ { Z } & { Z } \end{array} } \right) , \qquad Z = \mathrm { d i a g } \left( \alpha _ { 1 } , \ldots , \alpha _ { k } \right) - \alpha \alpha ^ { T } .
$$

Since $\alpha _ { \ j } \geq 0$ and $\sum \alpha _ { j } = 1$ it follows from the Cauchy-Schwarz inequality that

$$
x ^ { T } Z x = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } x _ { \jmath } ^ { 2 } - \left( \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } x _ { \jmath } \right) ^ { 2 } \geq 0
$$

Therefore the matrix $Z$ ， and hence also $\widehat { M }$ ， are non-negative definite matrices.   
This completes the proof of the theorem.

One can ask what are the advantages of the methods $E ( \alpha _ { 1 } , \ldots , \alpha _ { k } )$ with $k > 1$ over the $s$ -stage Gauss Runge-Kutta methods of order $2 s$ . All these methods have the same order and are algebraically stable for $\alpha _ { _ { \mathscr { I } } } \geq 0$ ·

· The Gauss methods have a stability function whose value at infinity satisfies $| R ( \infty ) | = 1$ . In contrast, the new methods allow the spectral radius $\varrho ( S ( \infty ) )$ to be smaller than 1, which improves stability at infinity. For example, numerical investigations of the case $s \simeq 2$ ， $k = 2$ show that $\varrho ( S ( \infty ) )$ has the minimal value $\sqrt { 2 } - 1 \approx 0 . 4 1 4 2 1$ for $\alpha _ { 1 } = 1 2 \sqrt { 2 } - 1 6$ and $\alpha _ { 2 } = 1 - \alpha _ { 1 }$ (see Exercise 7). There are some indications that $L$ -stable methods do not exist: if we could find methods with an internal stage, say $v _ { s } ^ { ( n ) }$ ,equal to $y _ { n + 1 }$ , then the method would be $I$ -stable. Unfortunately, this would imply $c _ { s } = 1$ , which is in contradiction to Lemma 9.12 and to $\alpha _ { _ { \mathscr { I } } } \geq 0$

· The eigenvalues of the Runge-Kutta matrix of the Gauss methods are com-plex (with the exception of one real eigenvalue,if $s$ is odd). Can we hope that, for a suitable choice of $\alpha _ { _ { \mathscr { I } } } \geq 0$ ， all eigenvalues of $\widetilde { B }$ become real? Numerical computations for $s \simeq 2$ and $k = 2$ indicate that this is not possible.

# $B$ -Convergence

Many results of Sections IV.14 and IV.15 have a straightforward extension to general linear methods. The following theorem corresponds to Theorems IV.14.2, IV.14.3,and IV.14.4 and is proved in the same way:

Theorem 9.16. Let $f$ be continuously differentiable and satisfy (9.1). If the matrix $\widetilde { B }$ of method (9.2) is invertible and if

$$
h \nu < \alpha _ { 0 } \big ( \widetilde { B } ^ { - 1 } \big ) ,
$$

then the nonlinear system $( 9 . 2 b )$ has a unique solution.

The next results give estimates of the local and global errors. We formulate these results only for multistep Runge-Kutta methods,because in this case the definitions of $C ( \eta )$ and $B ( p )$ are already available. In analogy to Runge-Kutta

methods we say that method (9.17) has stage order $q$ ,if $C ( q )$ and $B ( q )$ are satisfied. Recall that for the definition of the local error

$$
\delta _ { h } ( x ) = y _ { 1 } - y ( x + h )
$$

one assumes that $y _ { \ i } = y ( x + i h )$ for $i = 1 - k , \dots , 0$ lie on the exact solution.

Theorem 9.17. Suppose that the differential equation satisfies (9.1). If the matrix $\widetilde { B }$ is invertible,if $\overset { \bullet } { \alpha } _ { 0 } \mathopen { } \mathclose \bgroup \left( \widetilde { B } ^ { - 1 } \aftergroup \egroup \right) > 0$ and if the stage order is $q$ , then the local error of method (9.17) satisfies

$$
\| \delta _ { h } ( x ) \| \leq C h ^ { q + 1 } \operatorname* { m a x } _ { \xi \in [ x - ( k - 1 ) h , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| \quad f o r \quad h \nu \leq \alpha < \alpha _ { 0 } ( \widetilde { B } ^ { - 1 } )
$$

where $C$ depends only on the coefficients of the method and on $\alpha$ ·

This result, which corresponds to Proposition IV.15.1, is of particular interest for multistep collocation methods,for which the stage order $\ : q = s + k - 1 \ :$ is maximal. The global error allows the following estimate,which extends Theorem IV.15.3.

Theorem 9.18. Suppose, in addition to the assumptions of Theorem 9.17, that the method (9.17) is algebraically stable.

a)If $\nu > 0$ then the global error satisfies for $h \nu \leq \alpha < \alpha _ { 0 } ( \widetilde { B } ^ { - 1 } )$

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } \frac { e ^ { C _ { 1 } \nu ( x _ { n } - x _ { 0 } ) } - 1 } { C _ { 1 } \nu } C _ { 2 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

b)If $\nu \leq 0$ then (for all $h > 0$ ）

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } ( x _ { n } - x _ { 0 } ) C _ { 2 } \max _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

The constants $C _ { 1 }$ and $C _ { 2 }$ depend only on the coefficients of the method and (for case a) on $\alpha$ □

In contrast to the results of Sect.IV.15 the above theorem holds only for a constant step size implementation.

# Exercises

1. Show that for Runge-Kutta methods, where $A = ( 1 )$ ， $\stackrel { \sim } { A } = \mathbb { 1 }$ , both definitions of algebraic stability (IV.12.5 and V.9.3) are the same.

2. Prove in detail the statement of Example 9.8, that the 2-step 2-stage collocation methods with $c _ { 2 } = 1$ (and $c _ { 1 } \neq 1$ ) are not $G$ -stable.

Hint. The non-negativity of the matrix (9.16) implies $\gamma \geq 1 / 2$ and by considering its determinant,

$$
\gamma \bigl ( 4 \chi _ { 1 } - ( 1 + \chi _ { 2 } ) ^ { 2 } \bigr ) \geq 2 ( \chi _ { 1 } - \chi _ { 2 } ) .
$$

This inequality contradicts (9.14).

3. If a multistep Runge-Kutta method with distinct $c _ { \iota }$ and $c _ { \iota } \geq 0$ satisfies the assumptions $B ( s + k + \xi )$ and $C ( s + k - 1 )$ , then it also satisfies $D _ { B } ( \boldsymbol { \xi } )$

Hint. Show that

$$
\sum _ { j = 1 } ^ { k } \biggl ( q \sum _ { \iota = 1 } ^ { s } b _ { \iota } c _ { \iota } ^ { q - 1 } \widetilde a _ { \iota _ { j } } - \alpha _ { \jmath } ( 1 - ( 1 - j ) ^ { q } ) \biggr ) \bigl ( r ( 1 ) - r ( 1 - j ) \bigr ) = 0
$$

for all polynomials $r ( x )$ of degree $\leq s + k - 1$ which satisfy $r ( c _ { 1 } ) = \ldots =$ $r ( c _ { s } ) = 0$ . For given $j$ , construct such a polynomial which also satisfies

$$
r ( 1 - j ) = 1 , \quad r ( 1 - i ) = 0 \quad \mathrm { f o r } \quad i = 1 , \dots , k \quad \mathrm { a n d } \quad i \neq j .
$$

4.Disprove the conjecture of Burrage (1988) that for every $k$ and $s$ there exist zero-stable multistep Runge-Kutta methods of order $2 s + k - 1$

Hint. Consider the case $s \approx 1$ so that these methods are equivalent to one-leg methods and consult a result of Dahlquist (1983).

5. (Burrage 1988). Show that there exists a zero-stable multistep Runge-Kutta method with $s \simeq 2$ and $k = 2$ which is of order 5.

Result. $c _ { 1 , 2 } = ( \sqrt { 7 } \pm \sqrt { 2 } ) / 5$

6. (Stability at infinity). If a multistep Runge-Kutta method satisfies $D _ { A } ( s )$ and $D _ { B } ( s )$ then we have, e.g., for $s \simeq 2$ and $k = 2$ ，

$$
S ( \infty ) = \left( \begin{array} { c c } { { \alpha _ { 1 } } } & { { \alpha _ { 2 } } } \\ { { 1 } } & { { 0 } } \end{array} \right) - \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c c } { { 1 - c _ { 1 } } } & { { 1 - c _ { 2 } } } \\ { { 1 - c _ { 1 } ^ { 2 } } } & { { 1 - c _ { 2 } ^ { 2 } } } \end{array} \right) ^ { - 1 } \left( \begin{array} { c c } { { \alpha _ { 1 } } } & { { 2 \alpha _ { 2 } } } \\ { { \alpha _ { 1 } } } & { { 0 } } \end{array} \right) .
$$

Formulate this result also for general $s$ and $k$ .

7. Verify that for the method $E ( \alpha _ { 1 } , \alpha _ { 2 } )$ with $0 \leq \alpha _ { 1 } \leq 1$ ， $\alpha _ { 2 } = 1 - \alpha _ { 1 }$ , the spectral radius $\varrho ( S ( \infty ) )$ is minimal for $\alpha _ { 1 } = 1 2 \sqrt { 2 } - 1 6$ .
