# Exercises

1. Solve the system

$$
\begin{array} { c c } { { y _ { 1 } ^ { \prime } = - y _ { 2 } , } } & { { \qquad y _ { 1 } ( 0 ) = 1 } } \\ { { { } } } & { { { } } } \\ { { y _ { 2 } ^ { \prime } = + y _ { 1 } , } } & { { \qquad y _ { 2 } ( 0 ) = 0 } } \end{array}
$$

by the methods of Euler and Picard, establish rigorous error estimates for all three norms mentioned. Verify the results using the correct solution $y _ { 1 } ( x ) { = } \mathrm { c o s } x$ ， $y _ { 2 } ( x ) { = } \mathrm { s i n } x$

2. Consider the differential equations

$$
\begin{array} { r l } & { y _ { 1 \ } ^ { \prime } = - 1 0 0 y _ { 1 \ } + y _ { 2 \ } , \qquad y _ { 1 } ( 0 ) = 1 \ , \qquad y _ { 1 } ( 1 ) = ? } \\ & { y _ { 2 \ } ^ { \prime } = y _ { 1 \ } - 1 0 0 y _ { 2 \ } , \qquad y _ { 2 } ( 0 ) = 0 \ , \qquad y _ { 2 } ( 1 ) = ? } \end{array}
$$

a) Compute the exact solution $y \left( x \right)$ by the method explained in Section I.6.

b) Compute the error bound for $| \begin{array} { l l l l } \end{array} | z ( x \begin{array} { r l } \end{array} ) - y ( x \begin{array} { r l } \end{array} ) | | \begin{array} { r l } \end{array} $ ,where $z \left( x \right) { = } 0$ ， obtained from (7.10).

c) Apply the method of Euler to this equation with $h = 1 / 1 0$ d) Apply Picard's iteration method.

3. Compute the Taylor series solution of the system with constant coefficients $y ^ { \prime } { = } A y$ ， ${ \boldsymbol { y } } \left( 0 \right) = { \boldsymbol { y } } _ { 0 }$ .Prove that this series converges for all $x$ . Apply this series to the equation of Exercise 1. R esult:

$$
y ( x ) = \sum _ { i = 0 } ^ { \infty } \frac { x ^ { i } } { i ! } { A ^ { i } y _ { 0 } } = : e ^ { A x } y _ { 0 } .
$$

# 1.10. Differential inequalities

An elegant instrument for a better understanding of Equations (7.10),(7.17) and much new insight is that of differential inequalities. This subject was inaugurated in the paper, once again, Peano (1890) and further developed by Perron (1915)，Muller (1926)， Kamke (1930). A classical treatise on the subject is the book of Walter (1970).

# Introduction

The basic idea is the following: let $\nu \left( x \right)$ denote the Euler polygon defined in (7.3) or (9.2), so that

$$
\nu ^ { \prime } ( x ) = f ( x _ { i } , y _ { i } ) \quad \mathrm { f o r } x _ { i } < x < x _ { i + 1 } .
$$

For any chosen norm， we investigate the error

$$
m \left( x \right) = \left. \nu \left( x \right) - y \left( x \right) \right.
$$

as a function of $x$ and we naturally try to estimate its growth.

Unfortunately, $m \left( x \right)$ is not necessarily differentiable, due firstly to the corners in the Euler polygons and secondly， to corners originating from the norms, especially the norms (9.6') and (9.6"). Therefore we consider the so-called $D$ ini derivates defined as

$$
\begin{array} { l } { { D ^ { + } m \left( x \right) = \displaystyle \operatorname* { l i m s u p } _ { h > 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D ^ { - } m \left( x \right) = \displaystyle \operatorname* { l i m s u p } _ { h < 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D _ { + } m \left( x \right) = \displaystyle \operatorname* { l i m i n f } _ { h > 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \\ { { D _ { - } m \left( x \right) = \displaystyle \operatorname* { l i m i n f } _ { h < 0 } \frac { m \left( x + h \right) - m \left( x \right) } { h } \ : , } } \end{array}
$$

(see e.g. Scheeffer (1884), Hobson (1921), Chap.V, \$260, \$280). The properties

$$
\begin{array} { r l r } { \left\| ~ w \left( x + h \right) \right\| ~ - \left\| ~ w \left( x \right) \right\| } & { \leq } & { \left\| ~ w \left( x + h \right) - w \left( x \right) \right\| } \\ { \left\| ~ w \left( x \right) \right\| ~ - \left\| ~ w \left( x + h \right) \right\| } & { \leq } & { \left\| ~ w \left( x + h \right) - w \left( x \right) \right\| } \end{array}
$$

are simple consequences of the triangle inequality (9.7). If we divide (10.3) by $h > 0$ , we obtain the estimates

$$
D _ { + } | | ~ w ( x ) ~ | | ~ \leq ~ | | ~ w ^ { \prime } ( x ) ~ | | ~ , ~ D ^ { + } | | ~ w ( x ) ~ | | ~ \leq ~ | | ~ w ^ { \prime } ( x ) ~ | | ~ ,
$$

where $w ^ { \prime } ( x )$ is the right derivative of the vector function $w \left( x \right)$ If we apply this to $m \left( x \right)$ of (10.2), we obtain

$$
\begin{array} { r l } {  { D _ { + } m ( x ) \ \leq \  \ \nu ^ { \prime } ( x ) - y ^ { \prime } ( x )   } } \\ & { =  \ \nu ^ { \prime } ( x ) - f ( x , \nu ( x ) ) + f ( x , \nu ( x ) ) - f ( x , y ( x ) )  } \end{array}
$$

and, using the triangle inequality and the Lipschitz condition (9.9),

$$
D _ { + } m \left( x \right) \leq 8 ( x ) + L m \left( x \right) .
$$

Here, we have introduced

$$
\delta ( x ) = \parallel \nu ^ { \prime } ( x ) - f \left( x , \nu ( x ) \right) \parallel
$$

which is called the defect of the approximate solution $\nu \left( x \right)$ This fundamental quantity measures the extent to which the function $\nu \left( x \right)$ does not satisfy the imposed differential equation. (7.11) tels us together with (10.1） that $\mathfrak { F } ( x ) \le \epsilon$ ， so that (10.5) can be further estimated to become

$$
D _ { + } m \left( x \right) \leq L m \left( x \right) + \epsilon , m \left( x _ { 0 } \right) = 0 .
$$

(10.7) (or (10.5)) is what one calls a differential inequality. The question is: are we allowed to replace "≤" by "=", i.e. to solve instead of (10.7) the equation

$$
u ^ { \prime } = L u + \epsilon , \qquad u ( x _ { 0 } ) = 0
$$

and to conclude that $m ( x ) \leq u ( x ) \}$ This would mean, by the formu-las of Section I.3 or I.5,

$$
m \left( x \right) \ { \le \ } \ \frac { \epsilon } { L } \bigg ( e ^ { L \left( x - x _ { 0 } \right) } - 1 \bigg ) \ .
$$

We would thus have obtained (7.17) in a natural way and furthermore discovered an elegant and powerful tool for many kinds of new estimates.

# The fundamental theorems

A general theorem of the type

$$
\begin{array} { r l } & { D _ { + } m \left( x \right) \leq \varrho \left( x , m \left( x \right) \right) } \\ & { D _ { + } u \left( x \right) \geq \varrho \left( x , u \left( x \right) \right) } \\ & { m \left( x _ { 0 } \right) \leq u \left( x _ { 0 } \right) } \end{array} \Bigg \} \begin{array} { r l } & { \mathrm { i m p l i e s } \quad m \left( x \right) \leq u \left( x \right) } \\ { \mathrm { f o r } x _ { 0 } \leq x } \end{array}
$$

cannot be true. Counter-examples are provided by any differential equation with non-unique solutions, such as

$$
g \left( x , y \right) = \sqrt { y } , m \left( x \right) = \frac { x ^ { 2 } } { 4 } , u \left( x \right) = 0 .
$$

The important observation, due to Peano and Perron， which allows us to overcome this difficulty, is that one of the first two inequalities must be replaced by a strict inequality (see Peano (1890), \$3, Lemme 1):

Theorem 10.1. Suppose that the functions $m \left( x \right)$ and $u \left( x \right)$ are continuous and satisfy $f o r \ x _ { 0 } { \le } x < X$

$$
\begin{array} { r l } { \mathrm { a } ) } & { { } D _ { + } m \left( x \right) \leq \ g \left( x , m \left( x \right) \right) } \\ { \mathrm { b } ) } & { { } D _ { + } u \left( x \right) > \ g \left( x , u \left( x \right) \right) } \\ { \mathrm { c } ) } & { { } m \left( x _ { 0 } \right) \leq \ u \left( x _ { 0 } \right) \ . } \end{array}
$$

Then

$$
m \left( x \right) \leq u \left( x \right) \qquad f o r \ x _ { \ 0 } \leq \ x \ \leq \ X \ .
$$

The same conclusion is true if both $D _ { + }$ are replaced by $D ^ { + }$

Proof: In order to be able to compare the derivatives $D _ { + } m$ and $D _ { + } \mu$ in (10.12),we consider points at which $m \left( x \right) = u \left( x \right) .$ This is the main idea.

If (10.13) were not true, we could choose a point $x _ { 2 }$ with $m \left( { x _ { 2 } } \right) > u \left( { x _ { 2 } } \right)$ and look for the first point $x _ { 1 }$ to the left of $x _ { 2 }$ with $m \left( x _ { 1 } \right) { = } u \left( x _ { 1 } \right) .$ Then for sm all $h > 0$ we would have

$$
\frac { m \left( x _ { 1 } + h \right) - m \left( x _ { 1 } \right) } { h } > \frac { u \left( x _ { 1 } + h \right) - u \left( x _ { 1 } \right) } { h }
$$

and, by taking limits, $D _ { + } m \left( x _ { 1 } \right) \geq D _ { + } u \left( x _ { 1 } \right) .$ This, however, contradicts a) and b), which give

$$
D _ { + } m \left( x _ { 1 } \right) \leq g \left( x _ { 1 } , m \left( x _ { 1 } \right) \right) = g \left( x _ { 1 } , u \left( x _ { 1 } \right) \right) < D _ { + } u \left( x _ { 1 } \right) .
$$

QED.

Many variant forms of this theorem are possible, for example by using left Dini derivates (Walter (1970), Chap.II, \$8, Theorem V). The developments of the introduction now lead to

Theorem 10.2. (The "fundamental lemma"). Suppose that $\nu \left( x \right)$ is an approximate solution of the system of diferential equations $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 } .$ satisfying

$$
\begin{array} { r l } { \mathrm { a } ) } & { \parallel \nu \left( x _ { 0 } \right) - y \left( x _ { 0 } \right) \parallel \leq \mathsf { p } } \\ { \mathrm { b } ) } & { \parallel \nu ^ { \prime } ( x ) - f \left( x , \nu \left( x \right) \right) \parallel \leq \mathsf { \epsilon } } \\ { \mathrm { c } ) } & { \parallel f \left( x , \nu \right) - f \left( x , y \right) \parallel \leq L \parallel \nu - y \parallel . } \\ { T h e n , f o r x \geq x _ { 0 } \mathrm { , } \mathrm { ~ } \mathsf { n } a \nu e \mathrm { ~ } t h e \mathrm { ~ } e r r o r e s t i m a t e } \\ { \parallel y \left( x \right) - \nu \left( x \right) \parallel \leq \mathsf { p } e ^ { L \left( x - x _ { 0 } \right) } + \frac { \mathsf { \epsilon } } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) . } \end{array}
$$

Remark: The two terms in (10.14) express, respectively, the influence of the error p in the initial values and the influence of the defect ∈ to the error of the approximate solution. It implies that the error depends continuously on both, and that for $\rho = \epsilon = 0$ we have $y \left( x \right) = y \left( x \right) ,$ i.e. uniqueness of the solution.

Proof: We put $m \left( x \right) = \left| \right| y \left( x \right) - \nu \left( x \right) \right| \left|$ and obtain, as in (10.7),

$$
D _ { + } m \left( x \right) \leq L m \left( x \right) + \epsilon , \qquad m \left( x _ { 0 } \right) \leq \textsf { \textsf { p } } ,
$$

We shall try to compare this with the differential equation

$$
u ^ { \prime } = L u + \epsilon , \qquad u ( x _ { 0 } ) = \rho .
$$

Theorem 10.1 is not directly applicable. We therefore replace in (10.15) $\epsilon$ by $\epsilon + \eta$ ， $\eta > 0$ and solve instead

$$
u ^ { \prime } = L u + \tt { \epsilon } + \tt { \eta } \eta > L u + \tt { \epsilon } \ , \qquad u \left( x \leq \alpha _ { 0 } \right) = \alpha _ { 0 } \ .
$$

Now Theorem 10.1 gives the estimate (10.14) with ∈ replaced by $\epsilon + \eta$ . Since this estimate is true for $a l l \ \eta > 0$ , it is also true for $\eta = 0$ QED.

Variant form of Theorem 10.2. The conditions

imply for x≥ x0

$$
\begin{array} { r }  | \begin{array} { l } { y ( x ) - \nu ( x ) | \displaystyle | \begin{array} { l } { \leq e ^ { L ( x ) } \Biggl [ \displaystyle \rho + \int _ { x _ { 0 } } ^ { x } e ^ { - L ( s ) } \mathfrak { f } ( s ) d s \Biggr ] , L ( x ) = \int _ { x _ { 0 } } ^ { x } l ( s ) d s } \end{array}  } \end{array} \end{array}
$$

Proof: This is nothing but Formula (3.3). QED.

Theorem 10.3. If the function $g \left( x , y \right)$ is continuous and satisfies a Lipschiz condition, then the implication (1O.1O) is true for continuous fonctions $m \left( x \right)$ and u $\left( x \right)$ ·

Proof: Define functions $w _ { n } ( x ) , \nu _ { n } ( x )$ by

$$
\begin{array} { r l r } { { w _ { n } ^ { \prime } ( x ) = g \left( x , w _ { n } ( x ) \right) + \frac { 1 } { n } \ , } } & { { } { w _ { n } ( x _ { 0 } ) = m \left( x _ { 0 } \right) \ , } } & { { } } \\ { { \nu _ { n } ^ { \prime } ( x ) = g \left( x , \nu _ { n } ( x ) \right) - \frac { 1 } { n } \ , } } & { { \nu _ { n } ( x _ { 0 } ) = u \left( x _ { 0 } \right) \ , } } \end{array}
$$

so that from Theorem 10.1

$$
m \left( x \right) \leq w _ { n } \left( x \right) , \quad \nu _ { n } \left( x \right) \leq u \left( x \right) \quad \mathrm { ~ f o r ~ } \quad x _ { 0 } \leq x \leq X ,
$$

It follows from Theorem 10.2 that the functions $w _ { n } \left( x \right)$ and $\nu _ { n } ( x )$ converge for $n  \infty$ to the solutions of

$$
\begin{array} { c c } { { w ^ { \prime } ( x ) = g \left( x , w \left( x \right) \right) , } } & { { w \left( x _ { 0 } \right) = m \left( x _ { 0 } \right) , } } \\ { { { } } } & { { { } } } \\ { { \nu ^ { \prime } ( x ) = g \left( x , \nu \left( x \right) \right) , } } & { { { } } } \\ { { { } } } & { { { } } } \end{array}
$$

since the defect is $\pm ~ 1 / n$ . Finally， because of $m \left( x _ { 0 } \right) \leq u \left( x _ { 0 } \right)$ and uniqueness we have $w \left( x \right) \leq \nu \left( x \right)$ .Passing to the limit $n  \infty$ in (10.16) thus gives $m \left( x \right) \leq u \left( x \right) .$ QED.

A further generalization of Theorem 10.2 is possible if the Lipschitz condition c) is replaced by something nonlinear such as

$$
\left| \left| \begin{array} { l } { f \left( x , \nu \right) - f \left( x , y \right) } \end{array} \right| \right| \ \leq \ \omega ( x , \left\| \nu - y \right\| ) \ .
$$

Then the differential inequality for the error $m \left( x \right)$ is to be compared with the solution of

$$
u ^ { \prime } = \omega ( x , u ) + \delta ( x ) + \eta , \qquad u ( x _ { 0 } ) = \rho , \qquad \eta > 0 .
$$

See Walter (1970), Chap. II, δ11 for more details.

# Estimates using one-sided Lipschitz conditions

As we already observed in Exercice 2 of I.9, and as was known for a long time, much information about the errors can be lost by the use of positive Lipschitz constants $L$ (e.g (9.10), (9.10'), 0r (9.10")) in the estimates (7.16), (7.17), or (7.18). The estimates all grow exponentially with $x$ , even if the solutions and errors decay. Therefore many efforts have been made to obtain better error estimates, as for example the papers Eltermann (1955)， Uhlmann (1957), Dahlquist (1959), and the references therein. We follow with great pleasure the particularly clear presentation of Dahlquist.

Let us estimate the derivative of $m ( x ) = | \downarrow \ \nu ( x ) - y ( x )  |$ with more care than we did in (10.5): for $h > 0$ we have

$$
\begin{array} { r l r } {  { m ( x + h ) = \| \begin{array} { l l } { \nu ( x + h ) - y ( x + h ) \| } & { ( 1 0 . 1 ) } \\ { * ( x ) - y ( x ) + h ( \nu ^ { \prime } ( x ) - y ^ { \prime } ( x ) ) \| } & { + \mathbf { O } ( h ^ { 2 } ) } \end{array}  } } \\ & { \leq } & { \| \begin{array} { l } { \nu ( x ) - y ( x ) + h [ f ( x , \nu ( x ) ) - f ( x , y ( x ) ) ] \| } \\ { * h \ S ( x ) + \mathbf { O } ( h ^ { 2 } ) } \end{array}  } \\ & { } & { + h \delta ( x ) + \mathbf { O } ( h ^ { 2 } ) } \end{array}
$$

by the use of (10.6) and (9.7). Here, we apply the mean value theorem to the function $\boldsymbol { y } + h \boldsymbol { f } \left( \boldsymbol { x } \mathrm { ~ , ~ } \boldsymbol { y } \right)$ and obtain

$$
n \left( x + h \right) \leq \ \left( \operatorname* { m a x } _ { \eta \in \left[ y \left( x \right) , \nu \left( x \right) \right] } \| \ I + h \frac { \partial f } { \partial y } ( x \cdot \eta ) \| \ \right) m \left( x \right) + h \vartheta ( x ) + \mathbf { O } ( h ^ { 2 } )
$$

and finally for $h > 0$

$$
\frac { m \left( x + h \right) - m \left( x \right) } { h } \leq \operatorname* { m a x } _ { \mathfrak { N } ^ { \mathfrak { c } } \left[ y \left( x \right) , \nu \left( x \right) \right] } \frac { \parallel I + h \frac { \partial f } { \partial y } ( x , \mathfrak { N } ) \parallel - 1 } { h } m \left( x \right)
$$

The expression on the right hand side of (10.18) leads us to the following definition:

Definition 10.4. Let $Q$ be a square matrix, then we call

$$
\mu ( Q ) = \operatorname* { l i m } _ { h  0 , h > 0 } { \frac { \parallel I + h Q \parallel - 1 } { h } }
$$

the logarithmic norm of $Q$ ·

Following are formulas for its computation (Dahlquist (1959), p.11, Eltermann (1955), p.498,499):

Theorem 10.5. The logarithmic norm (10.19) is obtained by the fol-lowing formulas: for the Euclidean norm (9.6),

$$
\begin{array} { c l } { { \displaystyle \mu ( Q ) = \lambda _ { \mathrm { m a x } } = } } & { { { \displaystyle l a r g e s t ~ e i g e n \nu a l u e ~ o f ~ { \displaystyle \frac { 1 } { 2 } } ( Q ^ { T } + Q ) ~ } . } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { o r } ~ t h e ~ m a x - n o r m ~ ( 9 . \delta ^ { \prime } ) , } } \\ { { \displaystyle \mu ( Q ) = \operatorname* { m a x } _ { k } \left( q _ { k k } ~ + \sum _ { i \neq k } | q _ { k i } | \right) ~ . } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \displaystyle o r ~ t h e ~ n o r m ~ ( 9 . \delta ^ { \prime \prime } ) , } } \\ { { \displaystyle \mu ( Q ) = \operatorname* { m a x } _ { i } \left( q _ { i i } ~ + \sum _ { k \neq i } | q _ { k i } | \right) ~ . } } \end{array}
$$

Proofs: (10.20') and $( 1 0 . 2 0 ^ { \circ } )$ ） follow quite trivially from (9.11') and (9.11") and the definition (10.19). The point is that the presence of $_ { I }$ suppresses, for $h$ sufficiently small, the absolute values for the

diagonal elements. (10.20) is seen from the fact that the eigenvalues of

$$
\left( I + h Q \right) ^ { T } \left( I + h Q \right) = I + h \left( \boldsymbol { Q } ^ { T } + \boldsymbol { Q } \right) + h ^ { 2 } \boldsymbol { Q } ^ { T } \boldsymbol { Q } \mathrm { ~ , ~ }
$$

for $h  ~ 0$ ， converge to $1 + h \wedge _ { i }$ ，where $\lambda _ { i }$ are the eigenvalues of $Q ^ { T } + Q$ . QED.

Remark: For complex-valued matrices the above formulas become

$$
\begin{array} { r l } & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \quad \underset { i } { \mathrm { l a r g e s t ~ e i g e n v a l u e ~ o f } } \quad \frac { 1 } { 2 } ( \boldsymbol { \mathcal { Q } } ^ { * } + \boldsymbol { \mathcal { Q } } ) \ , } \\ & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \underset { k } { \mathrm { m a x } } \left( \mathrm { R e } q _ { k k } + \underset { i \neq k } { \sum } \vert q _ { k i } \vert \right) \ , } \\ & { \boldsymbol { \mu } ( \boldsymbol { \mathcal { Q } } ) = \underset { i } { \mathrm { m a x } } \left( \mathrm { R e } q _ { i i } + \underset { k \neq i } { \sum } \vert q _ { k i } \vert \right) \ . } \end{array}
$$

We now obtain from (10.18) the following improvement of Theorem 10.3.

Theorem 10.6. Suppose that we have the estimates

$$
\begin{array} { r l } { \mathbb { i } \left\lfloor \frac { \mathcal { I } _ { f } } { \partial y } ( x , \eta ) \right\rfloor } & { \leq \ l ( x ) \quad f o r \quad \eta \in \left[ \mathrm { y } \left( x \right) , \nu \left( x \right) \right] \quad \mathrm { a n d } \quad } & { \mathrm { ( f ) } } \\ { \Big \| \nu ^ { \prime } ( x ) - f \left( x , \nu \left( x \right) \right) \Big \| } & { \leq 8 \left( x \right) , \ \Big \| \ \nu \left( x _ { 0 } \right) - y \left( x _ { 0 } \right) \Big \| } & { \leq \mathrm { p } \ . } \\ { T h e n f o r x > x _ { 0 } \ w e \ h a v e } \\ { \Big \| \ y \left( x \right) - \nu \left( x \right) \Big \| } & { \leq \ e ^ { L \left( x \right) } \bigg ( \mathrm { p } + \displaystyle \int _ { x _ { 0 } } ^ { x } e ^ { - L \left( s \right) } \delta ( s ) d s \bigg ) \ , \qquad \mathrm { ( f ) } } \\ { \quad \times \Big \| \ h \ \mathscr { L } \left( x \right) - \displaystyle \int _ { x _ { 0 } } ^ { x } \Big \vert \left( s \right) d s \ . } \end{array}
$$

Proof: Since, for a fixed $x$ , the interval $[ \nu \left( x \right) , y \left( x \right) ]$ is compact,

$$
K \ = \mathrm { m } \underset { i } { \mathrm { a x } } \ \underset { [ v ( x ) , y ( x ) ] } { \mathrm { m a x } } \ | \ \frac { \partial f _ { i } } { \partial y _ { i } } |
$$

is finite. Then (see the proof of Theorem 10.5)

$$
{ \frac { \parallel I + h { \frac { \partial f } { \partial y } } ( x , \cdot \mathsf { \bar { n } } ) \parallel - 1 } { h } } = \mu { \frac { \partial f } { \partial y } } ( x , \cdot \mathsf { \bar { n } } ) ) + \mathbf { O } ( h )
$$

where the $\mathbb { O } ( h )$ -term is uniformly bounded in $\eta$ (For the norms $\left( 9 . 6 ^ { \prime } \right)$ and $\left( 9 . 6 ^ { \circ \mathfrak { V } } \right)$ this term is in fact zero for $h < 1 / K$ ). Thus the condition (10.21) inserted into (10.18) gives

$$
D _ { + } m \left( x \right) \leq l ( x ) m \left( x \right) + \ S ( x ) .
$$

Now the estimate (10.22) follows in the same way as that of Theorem 10.3. QED.

# Exercises

1. Apply Theorem 10.5 to the example of Exercise 2 of I.9. Observe the substantial improvement of the estim ates.

2. Prove the following (a variant form of the famous "Gronwall lemma", Gronwall(1919)): suppose that a positive function $m \left( x \right)$ satisfies

$$
m \left( x \right) \leq \textsf { p } + \epsilon ( x - x _ { 0 } ) + L \intop _ { x _ { 0 } } ^ { x } m \left( s \right) d s \ = : w \left( x \right)
$$

then

$$
m \left( x \right) \leq \mathsf { p } e ^ { L \left( x - x _ { 0 } \right) } + \frac { \epsilon } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) ;
$$

a) directly, by subtracting from (10.23)

$$
u \left( x \right) = \rho + \epsilon ( x - x _ { 0 } ) + L \intop _ { x _ { 0 } } ^ { x } u \left( s \right) d s \ ;
$$

b) by differentiating $w \left( x \right)$ in (10.23) and using Theorem 10.1.

c) Prove Theorem 10.2 with the help of the above lemma of Gronwall. The same interrelations are, of course, also valid in more general situations.

3. Observe, using an example of the form

$$
y _ { 1 } ^ { \prime } = y _ { 2 } ~ , ~ y _ { 2 } ^ { \prime } = - y _ { 1 } ~ ,
$$

that a generalization of Theorem 10.1 to systems of first order differential equations, with inequalities interpreted componentwise, is not true in general (Muller (1926)).

However, it is possible to prove such a generalization of Theorem 10.1under the additional hypothesis that the functions $g _ { i } ( x , y _ { 1 } , \ldots , y _ { n } )$ are quasimonotone, i.e. that

$$
\begin{array} { r l } & { g _ { i } ( x , y _ { 1 } , \dotsc , y _ { j } , \dotsc , y _ { n } ) \leq g _ { i } ( x , y _ { 1 } , \dotsc , z _ { j } , \dotsc , y _ { n } ) } \\ & { \qquad \mathrm { i f } \quad y _ { j } < z _ { j } \qquad \mathrm { f o r ~ a l l } \quad j \neq i \ . } \end{array}
$$

Try to prove this.

An important fact is that many systems from parabolic differential equations, such as Equation (6.10)， are quasimonotone. This

allows many interesting applications of the ideas of this section (see Walter (1970), Chapter IV).

4. Prove the following properties of the logarithmic norm

$$
\begin{array} { r l } & { \mathrm { a ) } \quad \mu ( \alpha Q ) = \alpha \mu ( Q ) \ \mathrm { f o r ~ \alpha ~ \geq ~ 0 ~ } } \\ & { \mathrm { b ) } \quad - \parallel \mathcal { Q } \parallel \leq \ \mu ( Q ) \leq \parallel \mathcal { Q } \parallel } \\ & { \mathrm { c ) } \quad \mu ( Q + P ) \leq \hslash ( Q ) + \mu ( P ) \ , \quad \mu ( \int Q \left( t \right) d t ) \leq \int \mu ( Q \left( t \right) ) d t } \\ & { \mathrm { d ) } \quad \left| \mu ( Q ) - \mu ( P ) \right| \leq \parallel Q - P \parallel } \end{array}
$$

5. For the Euclidean norm (10.20), $\mu ( Q )$ is the smallest number satisfying

$$
< \nu , Q \nu > \leq \mu ( Q ) \parallel \nu \parallel ^ { 2 } .
$$

This property is valid for all norms associated with a scalar product. Prove this.

6. Show that for the Euclidean norm the condition (10.21） is equivalent to

$$
< y - z \mathrm { , ~ } f ( x \mathrm { , ~ } y ) - f ( x \mathrm { , ~ } z ) > \leq l ( x \mathrm { ) | | ~ } y - z \mathrm { ~ | | ~ } ^ { 2 } \mathrm { ~ . ~ }
$$

# 1.11. Systems of linear differential equations

With more knowledge about existence and uniqueness, and with more ability in linear algebra, we shall now, as did the mathematicians of the 19th century, better understand many points which had been left a litte mysterious in Sections I.4 and I.6 about linear differential equations of higher order.

Equation (4.9) divided by $\boldsymbol { a } _ { 0 } ( \boldsymbol { x } )$ (which is $\neq 0$ away from singular points) becomes

$$
y ^ { ( n ) } + a _ { 1 } ( x ) y ^ { ( n - 1 ) } + \cdot \cdot \cdot + a _ { n } ( x ) y = f \left( x \right) .
$$

Introducing $y = y _ { 1 } , y ^ { \prime } = y _ { 2 } , . . . , y ^ { ( n - 1 ) } = y _ { n }$ we ariveat

$$
( \begin{array} { c } { { y _ { 1 } ^ { \prime } } } \\ { { y _ { 2 } ^ { \prime } } } \\ { { \vdots } } \\ { { y _ { n } ^ { \prime } } } \end{array} ) = ( \begin{array} { c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { 0 } } & { { } } & { { } } & { { } } \\ { { } } & { { \vdots } } & { { \ddots } } & { { \vdots } } & { { } } \\ { { - a _ { n } ( x ) } } & { { - a _ { n - 1 } ( x ) } } & { { \cdots } } & { { - a _ { 1 } ( x ) } } \end{array} ) ( \begin{array} { c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \\ { { \vdots } } \\ { { y _ { n } } } \end{array} ) + ( \begin{array} { c } { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \\ { { f ( x ) } } \end{array} ) \begin{array} { c } { { x _ { 1 } } } \\ { { y _ { 2 } } } \\ { { f _ { 1 } } } \end{array} ) .
$$

We again denote by y the vector $( y _ { 1 } , \dots , y _ { n } ) ^ { I }$ and by $f \left( x \right)$ the inhomogeneity,sothat (11.1)becomesaspecial caseof thefollowing sy tem of linear differential equations

$$
y ^ { \prime } = A \left( x \right) y + f \left( x \right) ,
$$

$$
A \left( x \right) = ( a _ { i j } ( x ) ) , f \left( x \right) = ( f _ { i } ( x ) ) , i , j = 1 , \ldots , n .
$$

Here, the theorems of Section I.9 and I.10 apply without difficulty. Since the partial derivatives of the right hand side of (11.2) with respect to $y _ { i }$ are given by $a _ { k i } ( x )$ , we have the Lipschitz estimate (see Condition c) of the variant form of Theorem 10.2)， where $l ( x ) = \parallel A \left( x \right) \parallel$ in any subordinate matrix norm (9.11, $1 1 ^ { \circ }$ , 11"). We apply Theorem 7.4， and the variant form of Theorem 10.2 with $\nu \left( x \right) = 0$ as "approximate solution". We may also take $l ( x ) = \mu ( A \left( x \right) )$ (see $( 1 0 . 2 2 , 2 2 ^ { \prime } , 2 2 ^ { \prime \prime } )$ ） and apply Theorem 10.6.

Theorem 11.1. Suppose that A $( x$ ) is continuous on an interval $[ x _ { 0 } , X ]$ Then for any initial values $y _ { 0 } = ( y _ { 1 0 } , \ldots , y _ { n 0 } ) ^ { T }$ there exists for au $x _ { 0 } \leq x \leq X$ a unique solution of (11.2) satisfying

$$
\begin{array} { r } { \|  { y } ( x ) \| \ \le \ e ^ { L \left( x \right) } \bigg [ \|  { y } _ { 0 } \| + \displaystyle \int _ { x _ { 0 } } ^ { x } e ^ { - L \left( s \right) } \|  { f } ( s ) \| \ d s \bigg ] } \end{array}
$$

$$
L \left( x \right) = \int _ { x _ { 0 } } ^ { x } l ( s ) d s , l ( x ) = \mid \mid A \left( x \right) \mid \mid \quad o r l ( x ) = \mu ( A \left( x \right) ) .
$$

For $f \left( x \right) { \equiv } 0$ ， $y \left( x \right)$ depends linearly on the initial values, i.e. there is a matrix $R$ $( x , x _ { 0 } )$ (the "resolvent"), such that

$$
y ( x ) = R ( x , x _ { 0 } ) y _ { 0 } .
$$

Proof: Since $l ( x )$ is continuous and therefore bounded on any compact interval $[ x _ { 0 } , X ]$ , the estimate (11.3) shows that the solutions can be continued until the end. The linear dependence follows from the fact that, for $f \equiv 0$ ， linear combinations of solutions are again solutions, and from uniqueness. QED.

Also from uniqueness we have that the solutions with initial values $y _ { 0 }$ at $ { { \varepsilon } } _ { 0 }$ and ${ \boldsymbol { y } } _ { 1 } = { \boldsymbol { R } }$ $( x _ { \mathit { \mathrm { ~ 1 ~ } } } , x _ { \mathit { \mathrm { ~ 0 ~ } } } ) y _ { \mathit { \mathrm { ~ 0 ~ } } }$ at $x _ { 1 }$ must be the same. Hence we have

$$
\begin{array} { r } { R \left( x _ { 2 } , x _ { 0 } \right) = R \left( x _ { 2 } , x _ { 1 } \right) R \left( x _ { 1 } , x _ { 0 } \right) } \end{array}
$$

for $x _ { 0 } { \le } x _ { 1 } { \le } x _ { 2 }$ . Finally by integrating backward from $x _ { 1 } , y _ { 1 } ,$ i.e. by the coordinate transformation ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 1 } - t$ ， $0 \leq t \leq x _ { 1 } - x _ { 0 } ,$ we must arrive, again by uniqueness, at the starting values. Hence

$$
\textit { R } ( x _ { 0 } , x _ { 1 } ) = \left( \boldsymbol { R } \left( x _ { 1 } , x _ { 0 } \right) \right) ^ { - 1 }
$$

and (11.5) is true in general.

# The Wronskian

Let $y _ { i } ( x ) = ( y _ { 1 i } ( x ) , \ldots , y _ { n i } ( x ) ) ^ { t } ( i = 1 , \ldots , n )$ be a set of n solu-tions of the homogeneous differential equation

$$
y ^ { \prime } = A \left( x \right) y
$$

which are linearly independent at $\boldsymbol { x } - \boldsymbol { x } _ { \textup { \scriptsize 0 } }$ (i.e., they form a fundamental system). We form the W ronskian matrix (Wronski (1810))

$$
W \left( x \right) = \left( \begin{array} { c c } { { y _ { 1 1 } ( x ) } } & { { \ldots } } & { { y _ { 1 n } ( x ) } } \\ { { } } & { { } } \\ { { \vdots } } & { { } } \\ { { y _ { n 1 } ( x ) } } & { { \ldots } } & { { y _ { n n } ( x ) } } \end{array} \right) ,
$$

so that

$$
W ^ { \prime } ( x ) = A \left( x \right) W \left( x \right)
$$

and all solutions can be written as

$$
c _ { 1 } y _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } y _ { n } ( x ) = W \left( x \right) \cdot c \mathrm { ~ w h e r e ~ } c = \left( c _ { 1 } ^ { } , \cdot \cdot \cdot , c _ { n } ^ { } \right) ^ { T } .
$$

If this solution must satisfy the initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ , we obtain $c = W ^ { - 1 } ( x _ { 0 } ) y _ { 0 }$ and we have the formula

$$
R \left( x , x _ { 0 } \right) = W \left( x \right) W ^ { - 1 } ( x _ { 0 } ) \ .
$$

Therefore all solutions are known if one has found n linearly independent solutions. For their construction, however, nearly nothing is known for general non-constant A $( x )$ ·

# The Abel-Liouville-Jacobi-Ostrograds kii identity

We already know from (11.6) that $W \left( x \right)$ remains regular for all $x$ . We now show that the determinant of $W \left( x \right)$ can be given explicitly as follows (Abel (1827), Liouville (1838), Jacobi (1845), \$17):

$$
\operatorname* { d e t } ( W \left( x \right) ) = \operatorname* { d e t } ( W \left( x _ { 0 } \right) ) \cdot \exp \left( \int _ { x _ { 0 } } ^ { x } { T r \left( A \left( s \right) \right) d s } \right) \mathrm { ~ , ~ }
$$

$$
T r ( A { \bf \Psi } ( x ) ) = a _ { 1 1 } ( x ) + a _ { 2 2 } ( x ) + \cdot \cdot \cdot + a _ { n n } ( x )
$$

which connects the determinant of $W \left( x \right)$ to the trace of A .

${ \frac { d } { d x } } \operatorname* { d e t } ( W \left( x \right) )$ $\operatorname* { d e t } ( W \left( x \right) )$ the Leibniz rule) is a sum of $n$ terms, whose first is

$$
T _ { 1 } = \operatorname* { d e t } { \left( \begin{array} { l l l l } { y _ { 1 1 } ^ { \prime } } & { y _ { 1 2 } ^ { \prime } } & { \cdots } & { y _ { 1 n } ^ { \prime } } \\ { y _ { 2 1 } } & { y _ { 2 2 } } & { y _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { y _ { n 1 } } & { y _ { n 2 } } & { \cdots } & { y _ { n n } } \end{array} \right) } ~ .
$$

We insert $y _ { 1 i } ^ { \prime } { = } a _ { 1 1 } y _ { 1 i } { + } \cdot \cdot \cdot { + } a _ { 1 n } y _ { n i }$ from (117). All terms ${ a _ { 1 2 } y _ { 2 i } }$ ， $\dots , a _ { 1 n } y _ { n i }$ disappear by subtracting multiples of lines 2 to $n$ , so that $\boldsymbol { T } _ { 1 } { ^ { = } } \boldsymbol { a } _ { 1 1 } \mathrm { d e t } ( \boldsymbol { W } \left( \boldsymbol { x } \right) )$ . Summing all these terms we obtain finally

$$
{ \frac { d } { d x } } \mathrm { d e t } ( W ( x ) ) = ( a _ { 1 1 } ( x ) + \cdot \cdot \cdot + a _ { n n } ( x ) ) \cdot \mathrm { d e t } ( W ( x ) )
$$

and (11.10) follows by integration. QED.

# Inhomogeneous linear equations

Extending the idea of Joh. Bernoulli for (3.2) and Lagrange for (4.9),we now compute the solutions of the inhomogeneous equation (11.2) by leting c be "variable" in the "general solution" (11.8): ${ \boldsymbol { y } } \left( { \boldsymbol { x } } \right) = { \boldsymbol { W } } \left( { \boldsymbol { x } } \right) { \boldsymbol { c } } \left( { \boldsymbol { x } } \right)$ (Liouville (1838)). Exactly as in Section I.3 for (3.2) we obtain from (11.2) and (11.7) by differentiation

$$
y ^ { \prime } = W ^ { \prime } c + W c ^ { \prime } = A W c + W c ^ { \prime } = A W c + f . 
$$

Hence $c ^ { \prime } { = } W ^ { - 1 } f$ . If we integrate this with integration constants $c$ ，we obtain

$$
y \left( x \right) = W \left( x \right) \intop _ { x _ { 0 } } ^ { x } { W \left( { s } \right) f \left( { s } \right) d s + W \left( x \right) \cdot c } .
$$

The initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ imply $c = W ^ { - 1 } ( x _ { 0 } ) y _ { 0 }$ and we obtain:

Theorem 11.2. ("Variation of constants formula"). Let A $\mathbf { \Psi } ( x \mathbf { \Psi } )$ and $f \left( x \right)$ be continuous. Then the solution of the inhomogeneous equation $y ^ { \prime } { = } A \left( x \right) y + f \left( x \right)$ satisfying the initial conditions $y \left( x _ { 0 } \right) { = } y _ { 0 }$ is given by

$$
\begin{array} { l } { { \displaystyle y \left( x \right) = W \left( x \right) \left[ W ^ { - 1 } ( x _ { 0 } ) y _ { 0 } + \displaystyle \int W ^ { - 1 } ( s ) f \left( s \right) d s \right] } } \\ { { \displaystyle x _ { 0 } } } \\ { { \displaystyle = R \left( x , x _ { 0 } \right) y _ { 0 } + \int R \left( x , s \right) f \left( s \right) d s } } \\ { { \displaystyle x _ { 0 } } } \end{array} .
$$

# Exercises

1. Compute the resolvent matrix R $( x \mathrm { ~ , ~ } x _ { \mathrm { ~ 0 ~ } } )$ for the systems

$$
\begin{array} { c c c } { { \mathrm { a ) } } } & { { { \begin{array} { l } { y _ { 1 } ^ { \prime } = y _ { 1 } } \\ { y _ { 2 } ^ { \prime } = 3 y _ { 2 } } \end{array} } } } & { { \begin{array} { l } { { \mathrm { b ) } } } \end{array} } } & { { { \begin{array} { l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } \\ { { y _ { 2 } ^ { \prime } = - y _ { 1 } } } \end{array} } } } \end{array}
$$

and check the validity of (11.5), (11.6) as well as (11.10).

2. Reconstruct Abel's original proof for (11.10), which was for the case

$$
y _ { 1 } ^ { \prime \prime } + p y _ { ~ 1 } ^ { \prime } + q y _ { 1 } = 0 ~ , ~ y _ { 2 } ^ { \prime \prime } + p y _ { ~ 2 } ^ { \prime } + q y _ { 2 } = 0 ~ ;
$$

multiply the equations by $y _ { 2 }$ and $y _ { 1 }$ respectively and subtract to

eliminate $q$ . Then integrate. Use the result to obtain an identity for the two integrals

$$
y _ { 1 } ( a ) = \int _ { 0 } ^ { \infty } e ^ { a x - x ^ { 2 } } x ^ { \alpha - 1 } d x , { } ~ y _ { 2 } ( a ) = \intop e ^ { - a x - x ^ { 2 } } x ^ { \alpha - 1 } d x ,
$$

which both satisfy

$$
\frac { d ^ { 2 } y _ { i } } { d a ^ { 2 } } - \frac { a } { 2 } \frac { d y _ { i } } { d a } - \frac { { \bf a } } { 2 } y _ { i } = 0 { . }
$$

Hint: To verify (11.13), integrate from 0 to infinity the expression for ${ \frac { d } { d x } } ( \exp ( a x - x ^ { 2 } ) x ^ { \alpha } )$ (Abel (1827), case IV).

3. (Kummer (1839)). Show that the general solution of the equation

$$
{ \bf \chi } _ { y } ^ { ( n ) } ( x ) = x ^ { m } y ( x )
$$

can be obtained by quadrature.

Hint: Differentiate (11.14) to obtain

$$
y ^ { \left( n + 1 \right) } = x ^ { m } y ^ { \prime } + m x ^ { m - 1 } y .
$$

Suppose by recursion that the general solution of

$$
\Psi ^ { ( n + 1 ) } = x ^ { m - 1 } \Psi ~ , ~ \mathrm { i . e . } ~ \frac { d ^ { n + 1 } } { d x ^ { n + 1 } } \Psi ( x u ) = x ^ { m - 1 } u ^ { m + n } \Psi ( x u )
$$

is already known. Show that then

$$
y \left( x \right) = \intop _ { 0 } ^ { \infty } u ^ { m - 1 } \mathrm { e x p } \biggl ( - \begin{array} { c } { { u ^ { m + n } } } \\ { { m + n } } \end{array} \biggr ) \psi ( x u ) d x
$$

is the general solution of (11.15), and, under some conditions on the parameters,also of (11.14). To simplify the computations, consider the function

$$
g ( u ) = u ^ { m } \exp \bigg ( - \frac { u ^ { m + n } } { m + n } \bigg ) \Psi ( x u ) \ ,
$$

compute its derivative with respect to $\boldsymbol { \mu }$ ，multiply by $x ^ { m - 1 }$ ,and integrate from O to infinity.

4. (Weak singularities for systems). Show that the linear system

$$
y ^ { \prime } = { \frac { 1 } { x } } \biggl ( A _ { \ 0 } + A _ { \ 1 } x + A _ { \ 2 } x ^ { 2 } + \cdots \biggr ) y
$$

possesses solutions of the form

$$
y ( x ) = x ^ { \mathsf { p } } \biggl ( \nu _ { 0 } + \nu _ { 1 } x + \nu _ { 2 } x ^ { 2 } + \cdot \cdot \cdot \biggr )
$$

where $\nu _ { 0 }$ ， $\nu _ { \textrm { 1 } } , .$ . are vectors. Determine first p and ${ \boldsymbol \nu } _ { 0 }$ ,then recursively $\nu _ { 1 } , \nu _ { 2 }$ ， etc. Observe that there exist $n$ independent solutions of the form (11.18) if the eigenvalues of $\textit { A } _ { 0 }$ satisfy $\lambda _ { i } \neq \lambda _ { j }$ mod(Z) (Fuchs (1866)).

5. Find the general solution of thc weakly singular systems

$$
y ^ { \prime } = { \frac { 1 } { x } } \left( { \frac { 3 } { 4 } } \quad 1 \right) \quad \quad \mathrm { a n d } \quad \quad y ^ { \prime } = { \frac { 1 } { x } } \left( { \begin{array} { l l } { { { \frac { 3 } { 4 } } } } & { { 1 } } \\ { { } } & { { } } \\ { { { \frac { 1 } { 4 } } } } & { { - { \frac { 1 } { 4 } } } } \end{array} } \right) \quad y \quad \quad \mathrm { a n d } \quad \quad y ^ { \prime } = { \frac { 1 } { x } } \left( { \begin{array} { l l } { { { \frac { 3 } { 4 } } } } & { { 1 } } \\ { { } } & { { } } \\ { { - { \frac { 1 } { 4 } } } } & { { - { \frac { 1 } { 4 } } } } \end{array} } \right) \quad y \enspace .
$$

Hint: While the first is easy from Exercise 4, the second needs an additional idea (see Formula (5.6)). A second possibility is to use the transformation $x = e ^ { t } , y \left( x \right) = z \left( t \right)$ ， and apply the methods of Section I.12.

# 1.12. Systems with constant coefficients

"Die Technik der Integration der linearen Differentialgleichungen mit constanten Coeffzienten wird hier auf das Hochste entwickelt."   
(F. Klein in Routh (1898))

# Linearization

Systems of linear differential equations with constant coefficients form a class of equations for which the resolvent $R$ $( x , x _ { 0 } )$ can be computed explicitly. They generally occur by linearization of timeindependent (i.e. autonomous or permanent) nonlinear differential equations

$$
y _ { i } ^ { \prime } = f _ { i } ( y _ { 1 } , . . . , y _ { n } ) \quad { \mathrm { ~ o r ~ } } \quad y _ { i } ^ { \prime \prime } = f _ { i } ( y _ { 1 } , . . . , y _ { n } )
$$

in the neighbourhood of a stationary point (Lagrange (1788), see also Routh (1860), Chap.IX, Thomson and Tait (1879)). We choose the coordinates so that the stationary point under consideration is the origin, i.e. ${ f _ { i } } ( 0 , \dots , 0 ) { = } 0$ . We then expand $f _ { i }$ in its Taylor series and neglect all nonlinear terms:

$$
y _ { i } ^ { \prime } = \sum _ { k } { \frac { \partial f _ { i } } { \partial y _ { k } } } ( 0 ) y _ { k } \qquad { \mathrm { o r } } \quad y _ { i } ^ { \prime \prime } = \sum _ { k } { \frac { \partial f _ { i } } { \partial y _ { k } } } ( 0 ) y _ { k } ~ .
$$

This is a system of equations with constant coefficients, as introduced in Section I.6 (see (6.3), (6.11)),

$$
y ^ { \prime } = A y \qquad { \mathrm { o r } } \quad y ^ { \prime \prime } = A y .
$$

Autonomous systems are invariant under a shift $x \to x + C$ . We may therefore always assume that ${ { x } _ { 0 } } \mathrm { { = } } 0$ . For arbitrary $\boldsymbol { \mathscr { x } } _ { \mathrm { ~ 0 ~ } }$ the resolvent is given by

$$
R \left( x , x _ { 0 } \right) = R \left( x - x _ { 0 } , 0 \right) .
$$

# Diagonalization

We have seen in Section I.6 that the assumption $y \left( x \right) = y \cdot e ^ { \lambda x }$ leads to

$$
A \nu = \lambda \nu \qquad \mathrm { o r } \quad A \nu = \lambda ^ { 2 } \nu ,
$$

hence $\nu \neq 0$ must be an eigenvector of A and λ the corresponding eigenvalue (in the first case; a square root of the eigenvalue in the

second case, which we do not consider any longer). From (12.3) we obtain by subtraction that there exists such a $\nu \neq 0$ if and only if the determinant

$$
\chi _ { A } \left( \lambda \right) : = { \mathrm { d e t } } ( \lambda I - A { \bf \Gamma } ) = \left( \lambda - \lambda _ { 1 } \right) \left( \lambda - \lambda _ { 2 } \right) \cdot \cdot \cdot \left( \lambda - \lambda _ { n } \right) = 0 ~ .
$$

This determinant is called the characteristic polynomial of A .

Suppose now that for the n eigenvalues $\lambda _ { i }$ the n eigenvectors $\nu _ { i }$ can be chosen linearly independent. We then have from (12.3)

$$
A \left( \nu _ { 1 } \nu _ { 2 } \cdots \nu _ { n } \right) = \left( \nu _ { 1 } \nu _ { 2 } \cdots \nu _ { n } \right) \mathrm { d i a g } \left( \mathsf { \boldsymbol { k } } _ { 1 } , \mathsf { \boldsymbol { k } } _ { 2 } , \ldots , \mathsf { \boldsymbol { k } } _ { n } \right) ,
$$

or,if $T$ is the matrix whose columns are the eigenvectors of A ，

$$
\begin{array} { r } { T ^ { - 1 } A T \ = \ \mathrm { d i a g } \biggl ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { n } \biggr ) \ . } \end{array}
$$

On com paring (12.5） with $( 1 2 . 1 ^ { , 3 9 } )$ ， we see that the differential equation sim plifies considerably if we use the coordinate transformation

$$
y \left( x \right) = T z \left( x \right) , \qquad y ^ { \prime } ( x ) = T z ^ { \prime } ( x )
$$

which leads to

$$
z ^ { \prime } ( x ) = \mathrm { d i a g } \left( \mathbb { \lambda } _ { 1 } , \lambda _ { 2 } , \ldots , \mathbb { \lambda } _ { n } \right) z \left( x \right) \ .
$$

Thus the original system of differential equations decomposes into n single equations which are readily integrated to give

$$
z ( x ) = \mathrm { d i a g } \Big ( \exp ( \mathsf { \boldsymbol { \lambda } } _ { 1 } x ) , \exp ( \mathsf { \boldsymbol { \lambda } } _ { 2 } x ) , \ldots , \exp ( \mathsf { \boldsymbol { \lambda } } _ { n } x ) \Big ) \ z _ { 0 } \ ,
$$

from which (12.6), yields

$$
y \left( x \right) = T \mathrm { d i a g } \biggl ( \exp ( \mathsf { \mathsf { A } } _ { 1 } x ) , \exp ( \mathsf { \mathsf { A } } _ { 2 } x ) , \ldots , \exp ( \mathsf { \mathsf { A } } _ { n } x ) \biggr ) T ^ { - 1 } y _ { 0 } .
$$

# The Schur decomposition

"Der Beweis ist leicht zu erbringen". (Schur, 1909)

The foregoing theory， beautiful as it may appear， has several drawbacks:

a) Not all $n \times n$ matrices have a set of n linearly independent eigenvectors;

b) Even if it is invertible, the matrix T can behave very badly (see Exercise 1).

However， for symmetric matrices a classical theory tells that A can always be diagonalized by orthogonal transformations. Let us therefore, with Schur (1909), extend this classical theory to non-symmetric matrices. A real matrix $\boldsymbol { Q }$ is called orthogonal if its column vectors are pair-wise orthogonal and of norm 1, i.e. if $Q ^ { T } Q = I$ or $Q ^ { T } = Q ^ { - 1 }$ A complex matrix $Q$ is called unitary if $Q ^ { \ast } Q = I$ or ${ Q } ^ { * } { = } { Q } ^ { - 1 }$ ,where $Q ^ { * }$ is the adjoint matrix of $Q$ , i.e. transposed and complex conjugate.

# Theorem 12.1.

a) (Schur). For each complex matrix A there exists a unitary matrix $Q$ such that

$$
\varrho ^ { * } A Q \ = \left( \begin{array} { c c c } { { \star _ { 1 } \times \hfill } } & { { \times \hfill } } & { { \times \hfill } } \\ { { } } & { { } } & { { \ddots \hfill } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \ddots \hfill } } & { { \hfill } } \\ { { } } & { { } } & { { \ddots \hfill } } \\ { { } } & { { } } & { { } } \end{array} \right) \ ;
$$

b) (Wintner-Murnaghan (1931)). For a real matrix A the matrix $Q$ can be chosen real and orthogonal, if for each pair of conjugate eigenvalues λ, $\stackrel { \_ } { \lambda } = \alpha \pm \textit { i } \beta$ one allows the block

$$
\left( \begin{array} { c c } { { \lambda } } & { { \times } } \\ { { } } & { { \overline { { { \lambda } } } } } \end{array} \right) \qquad t o \ b e \ r e p l a c e { d \ b y } \qquad \left( \begin{array} { c c } { { \times } } & { { \times } } \\ { { \times } } & { { \times } } \end{array} \right) \ .
$$

Proof: a) The matrix A has at least one eigenvector with eigenvalue $\lambda _ { 1 }$ . We use this (normalized) vector as the first column of a matrix $Q _ { 1 }$ . Its other columns are then chosen by arbitrarily completing the first one to an orthonormal basis. Then

$$
A Q _ { 1 } = Q _ { 1 } \left( { \brace { - - { \frac { 1 } { \imath } } \dots { - } \dots } ^ { \vdots \ddots \cdot x _ { n } } } \right) \ .
$$

We then apply the same argument to the $( n - 1 )$ -dimensional matrix A . This leads to

$$
\tilde { A } \tilde { \mathcal { Q } } _ { 2 } = \tilde { \mathcal { Q } } _ { 2 } \left( \left. \begin{array} { l l l l } { \lambda _ { 2 } | \times } & { \cdot \cdot \cdot } & { \times } \\ { - \frac { 1 } { 2 } | } & { \cdot \cdot \cdot } & { - \cdot } \\ { \phantom { - } | \times } & { \cdot \cdot \cdot } & { \times } \\ { 0 } & { | } & { \vdots } & { } \\ { \phantom { - } | } & { \cdot \cdot } & { \times } \end{array} \right| \right) \enspace .
$$

With the unitary matrix

$$
\boldsymbol { Q } _ { 2 } = \left( \begin{array} { l } { 1 \mathrm { ~ i ~ } 0 } \\ { - \mathrm { - + -- } } \\ { 0 \mathrm { ~ i ~ } \tilde { \mathcal { Q } } _ { 2 } } \end{array} \right)
$$

we obtain

$$
\mathcal { Q } _ { 1 } ^ { * } A \mathcal { Q } _ { 1 } \mathcal { Q } _ { 2 } = \mathcal { Q } _ { 2 } \left( \frac { \lambda _ { 1 } } { 1 } \begin{array} { l l l l } { * } & { \times \frac { 1 } { 1 } } & { \times } & { \dots } & { \times } \\ & { \lambda _ { 2 } \stackrel { 1 } { \mapsto } 1 \times } & { \dots } & { \times } \\ & { - } & { - } & { \dots } \\ & & { \mid \times } & { \dots } & { \times } \\ { 0 } & { \overset { 1 } { \downarrow } : } & { \vdots } \\ & { \vdots } & & { \ddots } \end{array} \right) .
$$

A continuation of this process leads finally to a triangular matrix as in (12.9) with Q =Q122' @n-1

b) Suppose A to be a real matrix. If $\lambda _ { 1 }$ is real, $\boldsymbol { Q } _ { 1 }$ can be chosen real and orthogonal. Now let $\lambda _ { 1 } = \alpha + i \beta$ （ $\beta \neq 0$ ） be a non-real eigenvalue with a corresponding eigenvector $\mu + i \nu$ ,i.e.

$$
A \left( u \pm i \nu \right) = ( \alpha \pm i \beta ) ( u \pm i \nu )
$$

or

$$
A u \ = \alpha u - \beta \nu , A \nu \ = \ \beta u \ + \alpha \nu ,
$$

Since $\beta \neq 0$ ,u and $\nu$ are linearly independent. We choose an orthogonal basis $\hat { u } ~ , ~ \hat { \nu }$ of the subspace spanned by $\pmb { \mu }$ and $\nu$ and take $\hat { \mu }$ ， $\hat { \nu }$ as the first two columns of the orthogonal matrix $Q _ { 1 }$ .We then have from (12.11')

$$
A Q _ { 1 } = Q _ { 1 } ( | \begin{array} { c c c c } { { \times } } & { { \times \mid \times } } & { { \cdots } } & { { \times } } \\ { { } } & { { \mid } } & { { } } & { { } } \\ { { \times } } & { { \times \mid \times } } & { { \cdots } } & { { \times } } \\ { { - - - \mathrm { 1 } - -- } } & { { - - - - } } & { { - } } \\ { { } } & { { \mid } } & { { \tilde { A } } } & { { } } \end{array} | \quad ,
$$

QED.

Schur himself was not very proud of "his" decomposition, he just derived it as a tool for proving interesting properties of eigenvalues (see e.g. Exercise 2).

Clearly, if A is real and symmetric, $Q ^ { T } A Q$ will also be symmetric, and therefore diagonal (see also Exercise 3).

# N umerical computations

The above theoretical proof is still not of much practical use. It requires that one know the eigenvalues, but the computation of eigenvalues from the characteristic polynomial is one of the bestknown stupidities of numerical analysis. Good numerical analysis turns it the other way round: the real matrix A is directly reduced, first to Hessenberg form， and then by a sequence of orthogonal transformations to the real Schur form of Wintner-Murnaghan ("QRalgorithm" of Francis, coded by Martin-Peters-Wilkinson, contribution Ii/14 in Wilkinson-Reinsch (1970)). The eigenvalues then drop out. However, the produced code, called "HQR2", does not give the Schur form of A ， since it continues for the eigenvectors of A . Some manipulations have therefore to be done to interrupt the code at the right moment (in the FORTRAN translation HQR2 of Eispack (1974), for example, the $" 3 4 0 "$ of statement labelled $" 6 0 "$ has to be replaced by "1001"). Happy "Matlab"-users just call "SCHUR".

Whenever the Schur form has been obtained, the transformation $y \left( x \right) = Q z \left( x \right) ,$ y $\prime ( x ) { = } Q z ^ { \prime } ( x )$ (see (12.6)) leads to

$$
\begin{array} { r } { \left( \begin{array} { c } { z _ { 1 } ^ { \prime } } \\ { \vdots } \\ { z _ { n - 1 } ^ { \prime } } \\ { z _ { n - 1 } ^ { \prime } } \\ { z _ { n } ^ { \prime } } \end{array} \right) = \left( \begin{array} { c c c c } { \mathsf { A } _ { 1 } } & { b _ { 1 2 } } & { \cdots } & { b _ { 1 , n - 1 } } & { b _ { 1 n } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { b _ { n - 1 , n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } \end{array} \right) \left( \begin{array} { c } { z _ { 1 } } \\ { \vdots } \\ { z _ { n - 1 } } \\ { z _ { n } } \end{array} \right) . } \end{array}
$$

The last equation here is $z _ { n } ^ { \prime } = \lambda _ { n } z _ { n }$ and can be integrated to give $z _ { n } = \exp ( \lambda _ { n } x ) z _ { n 0 } .$ Next, the equation for $z _ { n - 1 }$ is

$$
z _ { n - 1 } ^ { \prime } = \lambda _ { n - 1 } z _ { n - 1 } + b _ { n - 1 , n } z _ { n }
$$

with $z _ { n }$ known. This is a linear equation (inhomogeneous, if $b _ { n - 1 , n } \neq 0 )$ which can be solved by Euler's method explained in Sec-tion 1.4. Two different cases arise:

$\lambda _ { n - 1 } \neq \lambda _ { n }$ wa put $z _ { n - 1 } { = } E \exp ( \operatorname { \lambda } _ { n - 1 } x ) + F \exp ( \operatorname { \lambda } _ { n } x )$ $F = b _ { n - 1 , n } z _ { n 0 } / ( \lambda _ { n } - \lambda _ { n - 1 } )$ and $\scriptstyle { E = z _ { n - 1 , 0 } - F }$

b）If $\lambda _ { n - 1 } = \lambda _ { n }$ we set $z _ { n - 1 } { = } ( E + F x ) \exp ( \lambda _ { n } x )$ and obtain $F = b _ { n - 1 , n } z _ { n 0 }$ and $E = _ { z _ { n - 1 , 0 } }$

The next stage, following the same ideas， gives $z _ { n - 2 }$ , etc. Simple recursive formulas for the elements of the resolvent, which work in the case $\lambda _ { i } \neq \lambda _ { j } ,$ are obtained as follows (Parlett (1976)): we assume

$$
z _ { i } ( x ) = \sum _ { j = i } ^ { n } E _ { i j } \mathrm { e x p } ( \lambda _ { j } x )
$$

and insert this into (12.12). After comparing coefficients, we obtain for $i = n , n - 1 , n - 2 ,$ etc.

$$
\begin{array} { l l } { { E _ { i k } = \displaystyle \frac { 1 } { \mathsf { k } _ { k } - \mathsf { k } _ { i } } \Biggl ( \sum _ { j = i + 1 } ^ { k } b _ { i j } E _ { j k } \Biggr ) \quad } } & { { k = i + 1 , i + 2 , \cdot \cdot \cdot } } \\ { { E _ { i i } = z _ { i , 0 } - \displaystyle \sum _ { j = i + 1 } ^ { n } E _ { i j } ~ . } } & { { } } \end{array}
$$

The Jordan canonical form "Simpler Than You Thought" (Amer. Math. Monthly 1980)

Whenever one is not afraid of badly conditioned matrices (see Exercise 1),and many mathematicians are not, the Schur form obtained above can be further transformed into the famous Jordan canonical form :

Theorem 12.2. (Jordan (1870), Livre deuxieme, $\ S \ S$ and 6). For every matrix A there exists a non-singular matrix $T$ such that

$$
T ^ { - 1 } { \cal A } T = \mathrm { d i a g } \left\{ \left[ \begin{array} { l l l } { { \lambda _ { 1 } } } & { { 1 } } & { { } } \\ { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { \ddots } } \end{array} \right] , \left[ \begin{array} { l l l } { { \lambda _ { 2 } } } & { { 1 } } & { { } } \\ { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { \ddots } } \\ { { } } & { { } } & { { \lambda _ { 2 } } } \end{array} \right] , \cdots \right\} .
$$

(The dimension of the blocks may vary and the $\lambda _ { i }$ are not necessarily distinct).

Proof (Fletcher-Sorensen (1983)): We may suppose that the matrix is already in the Schur form. This is of course possible in such a way that identical eigenvalues are grouped together on the principal diagonal.

The next step is to remove all nonzero elements outside the upper-triangular blocks containing identical eigenvalues. We demon-strate this on the following example: $\lambda _ { 1 } \neq \lambda _ { 2 }$ and

$$
\begin{array} { r } { A = \left( \begin{array} { c c c } { \lambda _ { 1 } } & { a } & { b } & { c } \\ & { \lambda _ { 1 } } & { d } & { e } \\ & & { \lambda _ { 2 } } & { f } \\ & & & { \lambda _ { 2 } } \end{array} \right) \ . } \end{array}
$$

Our task is to find a transformation matrix such that $b , c , d$ and $e$ disappear; we search for it in the form

$$
\left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { a \stackrel { \mid } { \mid } b } } & { { c } } \\ { { } } & { { \lambda _ { 1 } \stackrel { \mid } { \mid } d } } & { { e } } \\ { { -- -- - \ -- \ \displaystyle \frac { 1 } { 1 } -- \ -- \int } } \\ { { \mid \lambda _ { 2 } } } & { { f } } \\ { { \mid } } & { { \lambda _ { 2 } } } \end{array} \right) \left( \begin{array} { c c c } { { \mid p } } & { { q } } \\ { { I \mid } } & { { r } } \\ { { -- - \ \displaystyle \frac { 1 } { 0 } - \ -- \ } } \\ { { 0 \stackrel { \mid } { \mid } \ - \ \displaystyle \frac { 1 } { I } } I } \end{array} \right) = \left( \begin{array} { c c c } { { \mid p \ q } } \\ { { I \mid } } & { { r \ q } } \\ { { - - \ -- \ \mid r } } & { { s } } \\ { { 0 \mid \stackrel { \mid } { \mid } I } } & { { I } } \end{array} \right) \left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { a \stackrel { \mid } { \mid } 0 } } & { { 0 } } \\ { { } } & { { \mid \mid } } & { { 0 } } \\ { { - \lambda _ { 1 } \stackrel { \mid } { \mid } 0 } } & { { 0 } } \\ { { - -- \ \ \mid \ -- \ } } & { { \mid \lambda _ { 2 } } } & { { f } } \\ { { \mid \lambda _ { 1 } \mid } } & { { \lambda _ { 2 } } } \end{array} \right) .
$$

All elem ents $c _ { i j }$ of these matrices already coincide, with the exception of the right upper $2 \times 2$ submatrix ( $i = 1 , 2$ and $j = 3$ , 4). Multiplying out we obtain $\lambda _ { 1 } p + a r + b = \lambda _ { 2 } p , \lambda _ { 1 } r + d = \lambda _ { 2 } r$ (and a similar set of equations for $q$ and $s$ ). These are of triangular structure and since $\lambda _ { 1 } \neq \lambda _ { 2 }$ they can easily be solved for $r$ and $p$ , then for $s$ and $q$ . More general situations are now obvious (try an example!).

In the following steps we treat each of the remaining blocks separately: we thus assume that all diagonal elements are equal and transform the block recursively to the form stated in the theorem.

We suppose the matrix A is of form

$$
\begin{array} { r l r } { A } & { { } = } & { \left( \frac { \mathsf { A } _ { \mathsf { \Pi } } ^ { \dagger } a ^ { T } } { \mathsf { I } - \mathsf { I } - \mathsf { \Pi } _ { \mathsf { 1 } } ^ { - } - \mathsf { \Pi } _ { \mathsf { 1 } } } \right) } \\ { } & { { } } & { \left( \mathsf { I } _ { \mathsf { \Pi } _ { \mathsf { 1 } } } ^ { \dagger } A _ { \mathsf { 1 } } ^ { T } \right) } \end{array}
$$

and assume, by the induction hypothesis, that $\boldsymbol { A } _ { \textup { 1 } }$ can be transformed to Jordan form by a matrix $T _ { 1 ^ { \cdot } }$ Then

$$
\begin{array} { r } { ( \underbrace { \lambda _ { \quad 1 } ^ { \mid } a ^ { T } } _ { \begin{array} { l } { 0 } \\ { \dots \dots \dots } \\ { 0 _ { \mid } ^ { \mid } A _ { 1 } } \end{array} } ) ( \underbrace { 1 } _ { \begin{array} { l } { 0 } \\ { 0 } \\ { \mid T _ { 1 } } \end{array} } ^ { \mid } - \underbrace { ( \begin{array} { l } { 1 } \\ { 0 } \\ { \dots } \\ { 0 } \end{array} ) } _ { \begin{array} { l } { 1 } \\ { 1 } \end{array} } = ( \underbrace { 1 } _ { \begin{array} { l } { ( \begin{array} { l } { 1 } \\ { 0 } \\ { \dots } \\ { 0 } \end{array} } ) } _ { \begin{array} { l } { 1 } \\ { 0 } \end{array} } ) ( \begin{array} { l l l l } { \lambda _ { \quad 1 } ^ { \mid } b _ { \lambda } } & { b _ { \lambda } } & { b _ { 3 } } & { \dots } \\ { - \dots } & { - \dots } & { - \dots } & { - } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { 1 } & { } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { } & { } \\ { 0 _ { \mid } ^ { \mid } } & { \lambda } & { } & { } \\ { 1 } & { } & { \lambda } & { \dots } \end{array} ) } \end{array} \end{array}
$$

where the vector $^ b$ is given by $b = T _ { 1 } ^ { T } a$ . Next, the matrix on the right can be sim plified as

$$
\begin{array} { r } { \left( \begin{array} { l l l l l } { \wedge \ \ \vert b _ { 1 } } & { b _ { 2 } \vert b _ { 3 } } & { \dotsc } \\ { \neg \neg \dots - \dots \dots \dots } \\ { 0 \vert \wedge \ \mathbf { \Lambda } \vert } & { \vert } \\ { 0 \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \neg \vert } & { \mathbf { \Lambda } \vert } \\ { \neg \vert } & { \dots - \dots - \dots \vert } \\ { \vdots } & { \vert \mathbf { \Lambda } \vert } & { \dotsc } \\ { \neg \vert } & { \vert \mathbf { \Lambda } \vert } \end{array} \right) \left( \begin{array} { l l l l } { 1 \ \vert b _ { 2 } } & { 0 \vert \mathbf { \Lambda } \vert } \\ { - - \frac { 1 } { 1 } - 2 - \frac { 1 } { 1 } - } \\ { \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { - \vert } & { - - \dots - \vert } \\ { \vert } & { \vert } & { \vert } \end{array} \right) = \left( \begin{array} { l } { 1 \vert b _ { 2 } } & { 0 \vert \mathbf { \Lambda } \vert } \\ { - - \frac { 1 } { 1 } - 2 - - \frac { 1 } { 1 } - } \\ { \vert \mathbf { \Lambda } \vert } & { \vert } \\ { \vert } & { 1 } \\ { \vert } & { \vert } \\ { - \vert } & { 1 \vert } \\ { \vert } & { \vert } \end{array} \right) \left( \begin{array} { l l l l } { \underset { 1 } { } ^ { 1 } } & { 0 \vert \ b _ { 1 } } & { 0 \vert \ b _ { 3 } } & { \dotsc } \\ { \vdots - \vert } & { \vert } & { \vert \mathbf { \Lambda } \vert } \\ { 0 \vert \mathbf { \Lambda } \vert } & { 1 } & { \vert } \\ { 0 \vert } & { 1 } & { \vert } \\ { \vert } & { \vert } & { \vert } \\ { \dotsc - \vert } & { - \vert } & { \vert } \\ { \vdots } & { \vert } & { \vert } \end{array} \right) } \end{array}
$$

Here we distinguish two cases:

a） $b _ { 1 } = 0$ : in this case we exchange the first two (block-)lines and columns and are again back at the induction hypothesis.

b） $b _ { 1 } \neq 0$ : here we use a diagonal scaling matrix to replace $b _ { 1 }$ by 1 (Exercise 4). Our last task is to remove $b _ { 3 } , b _ { 4 } , . .$ . These terms are pushed down to the right as follows:

$$
{ \left| \begin{array} { l l l } { 1 } & { { \left| \begin{array} { l l } { b _ { 3 } } & { b _ { 4 } } \\ { | } & { | } \end{array} \right| } } \\ { \lambda } & { 1 } \\ { | } & { | } \\ { - -- } & { - } & { - } \\ { - } & { - } & { - } \\ { | } & { \lambda } & { 1 } \\ { | } & { | } & { | } \end{array} \right| } \left( { \left| \begin{array} { l l l } { ~ } & { | } & { 0 } & { 0 } \\ { ~ } & { | } & { - | } & { - b _ { 3 } } & { - b _ { 4 } } \\ { ~ } & { | } & { - } & { - } & { 0 } \\ { ~ } & { | } & { 0 } & { 0 } \\ { -- } & { - } & { - } & { - } & { 0 } \\ { | } & { 1 } & { 0 } & { 0 } \\ { | } & { | } & { 0 } & { 1 } \end{array} \right| } \right) = \left( { \begin{array} { l l l } { ~ } & { | } & { 0 } & { 0 } \\ { ~ } & { | } & { 1 } & { 0 } \\ { ~ } & { | } & { - b _ { 3 } } & { - b _ { 4 } } \\ { ~ } & { | } & { | } & { 0 } \\ { -- } & { - } & { - } & { 0 } \\ { | } & { 1 } & { 0 } \\ { | } & { | } & { 1 } \end{array} } \right) \left( { \begin{array} { l l l } { \lambda } & { 1 } & { | } & { | } & { | } \\ { ~ \lambda } & { 1 } & { | } & { b _ { 3 } } \\ { ~ } & { ~ } & { 1 } & { - } & { - } \\ { ~ } & { \lambda } & { 1 } & { - } & { - } \\ { - } & { - } & { - } & { - } & { - } \\ { 1 } & { 1 } & { 0 } \\ { | } & { | } & { 1 } & { - } & { - } \end{array} } \right) ,
$$

and so on. In order that by this procedure all $b _ { i }$ finally die out, we have to assume that the first block is not smaller than the following ones. This has to be arranged in the beginning by permutations.

The product of all these transformation matrices is then the m atrix $T$ in (12.14). QED.

Corollary 12.3. For every matrix A and for every number E≠ O there exists a non-singular matrix $T$ (depending on e ) such that

$$
T ^ { - 1 } { \cal A } T = \mathrm { d i a g } \left\{ \left( \begin{array} { c c c } { { \lambda _ { 1 } } } & { { \epsilon } } & { { } } \\ { { } } & { { \ddots } } & { { \epsilon } } \\ { { } } & { { } } & { { \lambda _ { 1 } } } \end{array} \right) , \left( \begin{array} { c c c } { { \lambda _ { 2 } } } & { { \epsilon } } & { { } } \\ { { } } & { { \ddots } } & { { \epsilon } } \\ { { } } & { { } } & { { \lambda _ { 2 } } } \end{array} \right) , \cdots \right\} ,
$$

Proof: Multiply Equation (12.14) from the right by $D = \mathrm { d i a g \bar { ( } 1 , \epsilon , \epsilon ^ { 2 } , \epsilon ^ { 3 } , \dots ) }$ and from the left by $D ^ { - 1 }$ QED.

Numerical difficulties in determining the Jordan canonical form are described in Golub-Wilkinson (1976). There exist also several computer programs, for example the one described in Kaogstrom-Ruhe (1980).

When the matrix A has been transformed to Jordan canonical form (12.14), the solutions of the differential equation $y ^ { \prime } { = } A y$ can be calculated by the method explained in (12.12'), case b):

$$
y \left( x \right) = T D T ^ { - 1 } y _ { 0 }
$$

where $D$ is a block-diagonal matrix with blocks of the form

$$
\begin{array} { r } { \left( \begin{array} { l l l l l } { e ^ { \lambda _ { 1 } x } } & { x e ^ { \lambda _ { 1 } x } } & { \dots } & { \displaystyle \frac { x ^ { k } } { k ! } e ^ { \lambda _ { 1 } x } } \\ & & & { \ddots } \\ & & & & { e ^ { \lambda _ { 1 } x } } \end{array} \right) } \end{array}
$$

This is an extension of Formula (12.8).

# Geometric representation

The geometric shapes of the solution curves of $y ^ { \prime } { = } A y$ are presented in Figure 12.1 for dimension $n = 2$ They are plotted as paths in the phase-space $( y _ { 1 } , y _ { 2 } )$ . The cases a), b),c) and e) are the linearized equations of (12.16) at the four critical points (see Figure 12.2).

![](images/43a4e9328f6af560885f78d1b8bde92ba3da66af1506af55afc98aad5608e4f2.jpg)

Figure 12.1. Solutions of linear two dimensional systems

Much of this structure remains valid also for nonlinear systems (12.1) in the neighbourhood of equilibrium points. Exceptions may be "structurally unstable" cases such as complex eigenvalues with $\scriptstyle \alpha = \operatorname { R e } ( \lambda ) = 0$ . This has been the subject of many papers discussing "critical points" or "singularities" (see e.g. the famous treatise of Poincare (1881,82,85)).

In Figure 12.2 we show solutions of the quadratic system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = \displaystyle \frac { 1 } { 3 } ( y _ { 1 } - y _ { 2 } ) ( 1 - y _ { 1 } - y _ { 2 } ) } } \\ { { { } } } \\ { { y _ { 2 } ^ { \prime } = y _ { 1 } ( 2 - y _ { 2 } ) } } \end{array}
$$

which possesses four critical points of all four possible structurally stable types (Exercise 4).

![](images/2daa316fb039c030610dd29a52434b167abe86ff36e3bc472b8be91561e82867.jpg)  
Figure 12.2. Solution flow of System (12.16)

# Exercises

1. a) Compute the eigenvectors of the matrix

$$
\begin{array} { r } { A } \\ { A } \end{array} = \left( \begin{array} { l l l l l l } { - 1 } & { 2 0 } & & & & \\ & { - 2 } & { 2 0 } & & & \\ & & { - 3 } & { 2 0 } & & \\ & & & { \ddots } & { \ddots } & \\ & & & & { - 1 9 } & { 2 0 } \\ & & & & & { - 2 0 } \end{array} \right)
$$

by solving $( A - \lambda _ { i } I ) _ { \underline { { \nu } } _ { i } } { = } 0$   
Result. $\boldsymbol { \nu } _ { 1 } { = } ( 1 , 0 , \ldots ) ^ { T } ,$ $\nu _ { 2 } { = } ( 1 , - 1 / 2 0 , 0 , . . . ) ^ { T } ,$ $\nu _ { 3 } = ( 1 , - \bar { 2 } / 2 0 , 2 / 4 0 0 , 0 _ { \bar { , } \bar { \dots } } ) ^ { T }$ ，   
$\nu _ { 4 } \mathrm { = } ( 1 , - 3 / 2 0 , 6 / 4 0 0 , - 6 / 8 0 0 0 , 0 , . . . ) ^ { T } ,$ etc.

b) Compute, numerically the inverse of $T = ( \nu _ { 1 } , \nu _ { 2 } , \ldots , \nu _ { n } )$ and determine its largest element (answer: $4 . 5 \times 1 0 ^ { 1 2 }$ ). The matrix $T$ is thus very badly conditioned.

c) Compute numerically or analytically from (12.13) the solutions of

$$
y ^ { \prime } = A y , \qquad y _ { i } ( 0 ) = 1 , \qquad i = 1 , \ldots , 2 0 .
$$

Observe the "hump" (Moler and Van Loan (1978)): although all eigenvalues of A are negative, the solutions first grow enormously before decaying to zero. This is typical of non-symmetric matrices and is connected with the bad condition of $^ T \cdot$ (See Figure 12.3, which shows the solutions in logarithmic scale ()). Result

![](images/b22a38445b32b718026d5286304730615eb24f7063b4ff9342626cb1954d4222.jpg)  
Figure 12.3. Solutions of Equation (12.18) with Matrix (12.17)

2. (Schur). Prove that the eigenvalues of a matrix A satisfy the esti-

$$
\sum _ { i = 1 } ^ { n } { | \lambda _ { i } | } ^ { 2 } \leq \sum _ { i , j = 1 } ^ { n } { | a _ { i j } | } ^ { 2 }
$$

and that equality holds iff $A$ is orthogonally diagonizabie (see also Exercise 3).

Hint. $\textstyle \sum _ { i , j } | a _ { i j } | ^ { 2 }$ is the trace of $A ^ { * } A$ and thus invariant under uni-tary transformations ${ \boldsymbol { Q } } ^ { * } { \boldsymbol { A } } { \boldsymbol { Q } }$

3. Show that the Schur decomposition ${ \boldsymbol { S } } = { \boldsymbol { Q } } ^ { * } { \boldsymbol { A } } { \boldsymbol { Q } }$ is diagonal iff $A ^ { * } A = A A ^ { * }$ Such matrices are called normal. Hint. The condition is equivalent to ${ \boldsymbol { S } } ^ { * } { \boldsymbol { S } } = { \boldsymbol { S } } { \boldsymbol { S } } ^ { * }$ Show that skew-symmetric matrices are normal.

4. Let $b \neq 0$ be given. Determine α such that

$$
\begin{array} { r } { \left( \begin{array} { l l } { \lambda } & { b } \\ & { \lambda } \end{array} \right) \left( \begin{array} { l l } { 1 } & { 0 } \\ & { \alpha } \end{array} \right) = \left( \begin{array} { l l } { 1 } & { 0 } \\ & { \alpha } \end{array} \right) \left( \begin{array} { l l } { \lambda } & { 1 } \\ & { \lambda } \end{array} \right) \textrm { . } } \end{array}
$$

5. Compute the four critical points of System (12.16), and for each of these points the eigenvalues and eigenvectors of the matrix $\partial f / \partial y$ . Compare the results with Figures 12.2 and 12.1.

6. Compute a Schur decomposition and the Jordan canonical form of the matrix

$$
A \ = \frac 1 9 \left( \begin{array} { l l l } { { 1 4 } } & { { 4 } } & { { 2 } } \\ { { - 2 } } & { { 2 0 } } & { { 1 } } \\ { { - 4 } } & { { 4 } } & { { 2 0 } } \end{array} \right) \ .
$$

R esult. The Jordan canonical form is

$$
\left( \begin{array} { c c c } { { 2 } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { } } \\ { { 2 } } & { { } } & { { } } \\ { { } } & { { } } & { { 2 } } \end{array} \right) ~ ,
$$

7. Reduce the matrices

$$
\begin{array} { r } { A = \left( \begin{array} { c c c } { \mathrm {  ~ \lambda ~ } _ { 1 } } & { b } & { c } \\ & { \mathrm {  ~ \lambda ~ } _ { 1 } } & { d } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } } \end{array} \right) , \quad A = \left( \begin{array} { c c c } { \mathrm {  ~ \lambda ~ } _ { 1 } } & { b } & { c } \\ & { \mathrm {  ~ \lambda ~ } _ { 0 } } & { d } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & { \mathrm {  ~ \lambda ~ } _ { 1 } } \\ & & & { \mathrm {  ~ \lambda ~ } _ { \mathrm {  ~ \lambda ~ } } } \end{array} \right) } \end{array}
$$

to Jordan canonical form. In the second case distinguish the possibilities $b + d = 0$ and $b + d \neq 0$

# I.13. Stability

The Examiners give notice that the following is the subject of the Prize to be adjudged in 1877: The Criterion of Dynamical Stability.   
(S.G. Phear (Vice-Chancellor), J. Challis, G.G. Stokes, J. Clerk Max well)

# Introduction

"To illustrate the meaning of the question imagine a particle to slide down inside a smooth inclined cylinder along the lowest generating line, or to slide down outside along the highest generating line. In the former case a slight derangement of the motion would merely cause the particle to oscillate about the generating line, while in the latter case the particle would depart from the generating line altogether. The motion in the former case would be, in the sense of the question， stable, in the latter unstable .. what is desired is,a corresponding condition enabling us to decide when a dynamically possible motion of a system is such, that if slightly deranged the motion shall continue to be only slighty departed from." ('The Examiners" in Routh (1877)).

Whenever no analytical solution of a problem is known, numerical solutions can only be obtained for specified initial values. But often one needs information about the stability behaviour of the solutions for all initial values in the neighbourhood of a certain equilibrium point. We again transfer the equilibrium point to the origin and define:

Definition 13.1. Let

$$
y _ { i } ^ { \prime } = f _ { i } ( y _ { 1 } , \dotsc , y _ { n } ) \qquad i = 1 , \dotsc , n
$$

be a system with ${ f _ { i } } ( 0 , \ldots , 0 ) { = } 0$ ， $i = 1 , \ldots , n$ . Then the origin is called stable in the sense of $\scriptstyle L$ iapunov if for any $\epsilon > 0$ there is a $\delta > 0$ such that for the solutions $\mid \mid y ( x _ { 0 } ) \mid \mid < 8$ implies $\left| \left| \begin{array} { l } { y \left( x \right) } \end{array} \right| \right| < \epsilon$ for all $x > x _ { 0 } .$

The first step, undertaken by Routh in his famous Adams Prize essay (Routh (1877)), was to study the linearized equation

$$
y _ { i } ^ { \prime } = \sum _ { j } a _ { i j } y _ { j } , \qquad a _ { i j } ^ { } = \frac { \partial f _ { i } } { \partial y _ { j } } ( 0 ) .
$$

("The quantities $x \ , y \ , z \ , \ \ldots .$ etc are said to be small when their squares can be neglected.") From the general solution of (13.2) obtained in Section I.12, we have immediately

Theorem 13.1. The linearized equation (13.2) is stable (in the sense of Liapunov) iff all roots of the characteristic equation

$$
\operatorname* { d e t } ( \lambda I - A \ ) = a _ { 0 } \mathsf { \lambda } ^ { n } + \alpha _ { 1 } \mathsf { \lambda } ^ { n - 1 } + \cdot \cdot \cdot + a _ { n - 1 } \mathsf { \lambda } + a _ { n } \ = 0
$$

satisfy $\mathrm { R e } ( \lambda ) \leq 0$ ， and the multiple roots, which give rise to Jordan chains, satisfy the strict inequality $\mathrm { R e } ( \lambda ) < 0$

Proof: See (12.12) and (12.15). For Jordan chains the "secular" term (e.g. $E + F x$ in the solution of (12.12), case b)） which tends to infinity for increasing $x$ ， must be "killed" by an exponential with strictly negative exponent. QED.

# The Routh-Hurwitz criterion

The next task, which leads to the famous Routh-Hurwitz criterion， was the verification of the conditions $\mathrm { R e } ( \lambda ) < 0$ directty from the coefficients of (13.3)， without computing the roots. To solve this problem， Routh combined two known ideas: the first was Cauchy's argument principle, saying that the number of roots of a polynomial $p \left( z \right) = u \left( z \right) + i \nu \left( z \right)$ inside a closed contour is equal to the number of (positive) rotations of the vector $\left( u \left( z \right) , \nu \left( z \right) \right)$ ，as $z$ travels along the boundary in the positive sense (cf. e.g. Henrici (1974)， p.276). An example is presented in Figure 13.1 for the polynomial

![](images/7813648712d1d9f19576fd908ef14df36689c6b33c8c76c2324e3e359ff9b54a.jpg)  
Figure 13.1. Vector field of arg $( p \left( z \right)$ ) for the polynomial $p \left( z \right)$ of (13.4)

$$
\begin{array} { c } { { z ^ { 6 } + 6 z ^ { 5 } + 1 6 z ^ { 4 } + 2 5 z ^ { 3 } + 2 4 z ^ { 2 } + 1 4 z + 4 } } \\ { { { } } } \\ { { = ( z + 1 ) ( z + 2 ) ( z ^ { 2 } + z + 1 ) ( z ^ { 2 } + 2 z + 2 ) \ . } } \end{array}
$$

On the half-circle $z = \mathbf { R e } ^ { i \mathbf { \theta } }$ $\pi / 2 \le \Theta \le 3 \pi / 2$ ， $R$ very large) the argument of $p \left( z \right)$ , due to the dominant term $z ^ { n }$ , makes $n / 2$ positive rotations. In order 'to have all zeros of $p$ in the negative half plane, we therefore need an additional n/2 positive rotations along the ima-ginary axis:

Lemma 13.2. Let $p \left( z \right)$ be a polynomial of degree n and suppose that $p ( i y ) \neq 0$ for $y \in \mathbb { R }$ . Then all roots of $p \left( z \right)$ are in the negative halfplane $i f ,$ along the imaginary axis, $a r g ( p \left( i \right) )$ )makes n/2 positive rotations for y from $- \infty$ to $+ \infty$ .NED.

The second idea was the use of Sturm's theorem (Sturm (1829)) which had its origin in Euclid's algorithm for polynomials. Sturm made the discovery that in the division of the polynomial $p _ { i - 1 } ( y )$ by $p _ { i } ( y )$ it is better to take the remainder $p _ { i + 1 } ( y )$ with negative sign

$$
p _ { i - 1 } ( y ) = p _ { i } ( y ) q _ { i } ( y ) - p _ { i + 1 } ( y ) ~ .
$$

Then, due to the "Sturm sequence property"

$$
s i g n ( p _ { i + 1 } ( y ) ) \ne s i g n ( p _ { i - 1 } ( y ) ) \mathrm { i f } p _ { i } ( y ) = 0 ,
$$

the number of sign changes

$$
w \left( y \right) = \mathrm { ~ N o . ~ o f ~ s i g n ~ c h a n g e s ~ o f } \left( p _ { 0 } ( y ) , p _ { 1 } ( y ) , . . . , p _ { m } ( y ) \right)
$$

does not vary at the zeros of $p _ { 1 } ( y ) , . . . , p _ { m - 1 } ( y )$ . A consequence is the following

Lemma 13.3. Suppose that a sequence $\boldsymbol { p } _ { 0 } ( y ) , \boldsymbol { p } _ { 1 } ( y ) , \dots , \boldsymbol { p } _ { m } ( y )$ of real polynomials satisfies

i） $\deg ( p _ { 0 } ) > \deg ( p _ { 1 } )$ not simutaneosty zer,. $\boldsymbol { p } _ { 0 } ( y )$ $p _ { 1 } ( y )$   
ii) $p _ { m } \left( y \right) \neq 0$ for all y ∈R,   
iv) and the Sturm sequence property (13.6).

Then

$$
\frac { w ( \infty ) - w ( - \infty ) } { 2 }
$$

is equal to the number of rotations， measured in the positive direction， of the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ as y tends from $- \infty \ t o \ + \infty$ ·

Proof: Due to the Sturm sequence property， $w \left( y \right)$ does not change at zeros of $p _ { 1 } ( y ) , \ldots , p _ { m - 1 } ( y )$ By assumption i) also $p _ { m } ( y )$ has no influence. Therefore $w \left( y \right)$ can change only at zeros of $p _ { 0 } ( y )$ · If $w \left( y \right)$ increases by one at $\hat { y }$ , either $p _ { 0 } ( y )$ changes from $^ +$ to - and $p _ { 1 } ( \hat { y } ) > 0$ or it changes from $^ -$ to $^ +$ and $p _ { 1 } ( \hat { y } ) < 0$ $( p _ { 1 } ( \hat { y } ) = 0$ is impossible by i)). In both situations the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ crosses the imaginary axis in the positive direction (see Figure 13.2). If $w \left( y \right)$ decreases by one, $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ ） crosses the imaginary axis in the negative direction. The result now foliows from i)， since the vector $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ is horizontal for $y  - \infty$ and for $y  + \infty$ . QED.

![](images/e3fd2d5ef08a18f5a87cbeee6526f87e4f8ddde5f618a56e628d73e3d9f56dae.jpg)  
Figure 13.2. Rotations of $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ ） compared to $w \left( y \right)$

The two preceding lem mas together give us the desired criterion for stability: let the characteristic polynomial (13.3)

$$
p ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } = 0 \ , \qquad a _ { 0 } > 0
$$

be given. We divide $p \left( i y \right)$ by $i ^ { n }$ and separate real and imaginary parts,

$$
\begin{array} { l } { { p _ { 0 } ( y ) = \displaystyle { \mathrm { R e } } \frac { p \left( i y \right) } { i ^ { n } } = a _ { 0 } y ^ { n } - a _ { 2 } y ^ { n - 2 } + a _ { 4 } y ^ { n - 4 } \pm \cdot \cdot \cdot \quad ( \mathrm { ( } } } \\ { { \mathrm { } } } \\ { { p _ { 1 } ( y ) = - \mathrm { I m } \frac { p \left( i y \right) } { i ^ { n } } = a _ { 1 } y ^ { n - 1 } - a _ { 3 } y ^ { n - 3 } + a _ { 5 } y ^ { n - 5 } \pm \cdot \cdot \cdot \mathrm { . } } } \end{array}
$$

Due to the special structure of these polynomials, the Euclidean algorithm (13.5) is here particularly simple: we write

$$
p _ { i } ( y ) = c _ { i 0 } y ^ { n - i } + c _ { i 1 } y ^ { n - i - 2 } + c _ { i 2 } y ^ { n - i - 4 } + \cdot \cdot \cdot \ ,
$$

and have for the quotient in (13.5) $q _ { i } ( y ) = ( c _ { i - 1 , 0 } / c _ { i 0 } ) y$ , provided that $c _ { i 0 } \neq 0$ Now (13.10) inserted into (13.5) gives the following recursive forulafortemputationftecicits $c _ { i j }$ ：

$$
c _ { i + 1 , j } = c _ { i , j + 1 } \cdot \frac { c _ { i - 1 , 0 } } { c _ { i 0 } } - c _ { i - 1 , j + 1 } = \frac { 1 } { c _ { i 0 } } \operatorname* { d e t } \left( \begin{array} { c c } { { c _ { i - 1 , 0 } } } & { { c _ { i - 1 , j + 1 } } } \\ { { c _ { i , 0 } } } & { { c _ { i , j + 1 } } } \end{array} \right)
$$

If $c _ { i 0 } { = } 0$ for some $i$ , the quotient $q _ { i } ( y )$ is a higher degree polynomial and the Euclidean algorithm stops at $p _ { m } ( y )$ with $m < n$

The sequence $( \boldsymbol { p } _ { i } ( y )$ ） obtained in this way obviously satisfies Conditions i) and iv) of Lemma 13.3. Condition ii) is equivalent to $p \left( i y \right) \neq 0$ for $y \in \mathbb { R } .$ ，and ii) is a consequence of ii since $p _ { m } ( y )$ is the greatest common divisor of $\boldsymbol { p } _ { 0 } ( y$ ) and $p _ { 1 } ( y )$

Theorem 13.4. (Routh (1877)). All roots of the real polynomial (13.3）with $a _ { 0 } > 0$ lie in the negative half plane $\mathrm { R e } \lambda < 0$ if and only if

$$
c _ { i 0 } > 0 \qquad f o r \quad i = 0 , 1 , 2 , \ldots , n \quad ,
$$

Remark: Due to the condition $c _ { i 0 } > 0$ , the division by $c _ { i 0 }$ in Formula (13.11) can be omitted (common positive factor of $p _ { i + 1 } ( y ) ,$ ）， which leads to the same theorem (Routh (1877), p. 27: ". so that by remembering this simple cross-muitiplication we may write down..."). This, however， is not advisable for n large because of possible overflow.

Proof: The coordinate systems $( p _ { 0 } , p _ { 1 } )$ and $( \operatorname { R e } ( p ) , \operatorname { I m } ( p ) )$ are of opposite orientation. Therefore, n/2 positive rotations of $p \left( i y \right)$ correspond to n /2 negative rotations of $( p _ { 0 } ( y ) , p _ { 1 } ( y ) )$ . If all roots of $p \left( \lambda \right)$ lie in the negative half plane $\mathrm { R e } \lambda < 0$ , it follows from Lemmas 13.2 and 13.3 that $w \left( \infty \right) - w \left( - \infty \right) = - n$ ,which is only possible if $w \left( \infty \right) = 0$ ， $w \left( - \infty \right) = n$ .This implies the positivity of all leading coefficients of $p _ { i } ( y )$

On the other hand,if (3.12)issatifd,westhat $p _ { n } \left( y \right) \equiv c _ { n } 0$ Hence the polynomials $\boldsymbol { p } _ { 0 } ( \boldsymbol { y }$ ）and $p _ { 1 } ( y )$ cannot have a common factor and $p \left( \lambda \right) \neq 0$ on the imaginary axis. We can now apply Lem mas 13.2 and 13.3 again to obtain the result. QED.

A second proof of this Theorem is possible using "positive func-tions" (see Volume II).

Example 1: The Routh tableau (13.11) for Equation (13.4) is given in Table 13.1. It clearly satisfies the conditions for stability.

Example 2: (Routh (1877), p. 27). Express the stability conditions for the biquadratic

$$
z ^ { 4 } + p z ^ { 3 } + q z ^ { 2 } + r z + s = 0 .
$$

The $c _ { i j }$ values (without division) are given in Table 13.2.

Table 13.1. Routh tableau for (13.4)   

<table><tr><td></td><td>j=0</td><td>j=1</td><td>j=2</td><td>j=3</td></tr><tr><td>i=0</td><td>1</td><td>-16</td><td>24</td><td>-4</td></tr><tr><td>i=1</td><td>6</td><td>-25</td><td>14</td><td></td></tr><tr><td>i=2</td><td>11.83</td><td>-21.67</td><td>4</td><td></td></tr><tr><td>i=3</td><td>14.01</td><td>-11.97</td><td></td><td></td></tr><tr><td>i=4</td><td>11.56</td><td>-4</td><td></td><td></td></tr><tr><td>i=5</td><td>7.12</td><td></td><td></td><td></td></tr><tr><td>i=6</td><td>4</td><td></td><td></td><td></td></tr></table>

Table 13.2. Routh tableau for (13.13)   

<table><tr><td></td><td>j=0</td><td>j=1</td><td>j=2</td></tr><tr><td>i=0</td><td>1</td><td>-q</td><td>S</td></tr><tr><td>i=1</td><td>p</td><td>-r</td><td></td></tr><tr><td>i=2</td><td>pq-r</td><td>-ps</td><td></td></tr><tr><td>i=3</td><td>(pq -r)r-p²s</td><td></td><td></td></tr><tr><td>i=4</td><td>((pq-r)r-p²s)ps</td><td></td><td></td></tr></table>

We have stability iff

$$
p > 0 \ , \quad p q - r > 0 \ , \quad ( p q - r ) r - p ^ { 2 } s > 0 \ , s > 0 \ .
$$

# Computational considerations

The actual computational use of Routh's criterion, in spite of its high historical importance and mathematical elegance, has two drawbacks for higher dimensions:

1) It is not easy to compute the characteristic polynomial for higher order matrices;

2) The use of the characteristic polynomial is very dangerous in the presence of rounding errors.

So, whenever one is not working with exact algebra or high precision,it is advisable to avoid the characteristic polynomial and use numerically stable algorithms for the eigenvalue problem (e.g. Eispack (1974)).

Numerical Experiments: 1. The matrix

$$
\begin{array} { r l } { A } & { = \left( \begin{array} { l l l l l } { - . 0 5 } & & { 1 } & { - 1 } & & \\ & { . } & { 1 } & & \\ & { . } & { 1 } & { . } & \\ & & { . } & { 1 } & \\ & & { - . 0 5 } & & { - n } \\ { - . -- } & { - . -- } & { - . -- } & { - n } \\ { 1 } & & { 1 } & { - . 0 5 } & \\ & { . } & { 1 } & & \\ & { . } & { 1 } & { . } & \\ & & { n } & { 1 } & { - . 0 5 } \end{array} \right) } \end{array}
$$

has the characteristic polynomial

$$
p ( z ) = \prod _ { j = 1 } ^ { n } \left( z ^ { 2 } + 0 . 1 z + j ^ { 2 } + 0 . 0 0 2 5 \right) .
$$

We computed the coefficients of $p$ using double precision, and then applied the Routh algorithm in single precision (machine precision ${ \dot { = 1 } } . 5 \times 1 0 ^ { - 8 }$ ).Theresults indicated stability for $n \leq 1 5$ , but not for $n \geq 1 6$ ， although the matrix always has its eigenvalues $- 0 . 0 5 \pm k i$ in the negative half plane. On the other hand, a direct computation of the eigenvalues of A with the use of Eispack subroutines gave no problem for any $n$ ·

2. We also tested the Routh algorithm at the (scaled) numerators of the diagonal Pade approximations to exp(z)

$$
\begin{array} { c } { { 1 + \displaystyle \frac { n } { 2 n } ( n z ) + \displaystyle \frac { n ( n - 1 ) } { ( 2 n ) ( 2 n - 1 ) } \displaystyle \frac { ( n z ) ^ { 2 } } { 2 ! } } } \\ { { + \displaystyle \frac { n ( n - 1 ) ( n - 2 ) } { ( 2 n ) ( 2 n - 1 ) ( 2 n - 2 ) } \displaystyle \frac { ( n z ) ^ { 3 } } { 3 ! } + \cdots ~ , } } \end{array}
$$

which are also known to possess all eigenvalues in $\mathbf { C } ^ { - }$ . Here, the results were correct only for $n \leq 2 1$ ， and wrong for larger $n$ due to rounding errors.

# Liapunov functions

We now consider the question whether the stability of the nonlinear system (13.1) "can really be determined by examination of the terms of the first order only" (Routh (1877), Chapt.VII). This theory, initiated by Routh and Poincaré, was brought to perfection in the famous work cf Liapunov (1892). As a general reference to the enormous theory that has devcloped in the meantime we mention Rouche-Habets-Laloy (1977) and W. Hahn (1967).

Liapunov's (and Routh's) main tools are the so-called Liapunov functions $V \left( y _ { 1 } , \ldots , y _ { n } \right)$ , which should satisfy

$$
\begin{array} { c } { { V \left( y _ { 1 } , \ldots , y _ { n } \right) \geq 0 \ , } } \\ { { { } } } \\ { { V \left( y _ { 1 } , \ldots , y _ { n } \right) = 0 \ \mathrm { i f f } y _ { 1 } = \cdot \ \cdot \ = y _ { n } = 0 } } \end{array}
$$

and along the solutions of (13.1)

$$
{ \frac { d } { d x } } V \left( y _ { 1 } ( x ) , \ldots , y _ { n } ( x ) \right) \leq 0 \ .
$$

Usually $V \left( y \right)$ behaves quadratically for sm all y and Condition (13.15) means that

$$
c \parallel y \parallel ^ { 2 } \leq V ( y ) \leq C \parallel y \parallel ^ { 2 } , \quad \quad C \geq c > 0 .
$$

The existence of such a Liapunov function is then a sufficient condition for stability of the origin.

We start with the construction of a Liapunov function for the linear case

$$
y ^ { \prime } = A y .
$$

This is best done in the basis which is naturally given by the eigenvectors (or Jordan chains) of $A$ . Wc therefore introduce $y = T z$ ， $z = T ^ { - 1 } y$ so that A is transformed to Jordan canonical form (12.14') ${ \boldsymbol { J } } = { \boldsymbol { T } } ^ { - 1 } { \boldsymbol { A } } { \boldsymbol { T } }$ and (13.18) becomes

$$
z ^ { \prime } = J z .
$$

If we put

$$
V _ { 0 } ( z ) = | | z | | ^ { 2 } \quad \mathrm { a n d } \quad V ( y ) = V _ { 0 } ( T ^ { - 1 } y ) = V _ { 0 } ( z ) ,
$$

the derivative of $V \left( y \left( x \right) \right)$ )becomes

$$
\begin{array} { l } { \displaystyle \frac { d } { d x } V \left( y \left( x \right) \right) = \frac { d } { d x } V _ { 0 } ( z \left( x \right) ) = 2 \mathrm { R e } < z \left( x \right) \mathrm { , ~ } z ^ { \prime } ( x ) > \quad \mathrm { ( ~ } \partial _ { x } \mathrm { ~ ) ~ } } \\ { \displaystyle = 2 \mathrm { R e } < z \left( x \right) \mathrm { , ~ } J { z } \left( x \right) > \ \le \ 2 \mu ( J ) V \left( y \left( x \right) \right) \mathrm { . ~ } } \end{array}
$$

By (10.20) the logarithmic norm is given by

$$
2 \mu ( J ) = \mathrm { l a r g e s t ~ e i g e n v a l u e ~ o f } J + J ^ { * } .
$$

The matrix $J + J ^ { * }$ is block-diagonal with tridiagonal blocks

$$
\left( \begin{array} { c c c c c } { { 2 \mathrm { R e } \lambda _ { i } } } & { { \epsilon } } & { { } } & { { } } & { { } } \\ { { \epsilon } } & { { 2 \mathrm { R e } \lambda _ { i } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \varepsilon } } \\ { { } } & { { } } & { { \epsilon } } & { { 2 \mathrm { R e } \lambda _ { i } } } \end{array} \right) ~ .
$$

Subtracting the diagonal and using Formula (6.7a), we see that the eigenvalues of the $m$ -dimensional matrix (13.22) are given by

$$
2 \left( { \tt R e A } _ { i } + \tt { e c o s } \frac { \pi k } { m + 1 } \right) \qquad k = 1 , \ldots , m .
$$

As a consequence of this formula or by the use of Exercise 4 we have:

Lemma 13.5. If all eigenvalues of A satisfy $\mathsf { R e } \lambda _ { i } < - \mathsf { p } < 0$ ，then there exists a (quadratic) Liapunov function for Equation (l3.18) which satisfies

$$
\frac { d } { d x } V \left( y \left( x \right) \right) \leq - \rho V \left( y \left( x \right) \right) .
$$

NED.

This last differential inequality implies that (Theorem 10.1)

$$
V \left( y \left( x \right) \right) \leq \ V \left( y _ { 0 } \right) \cdot \exp ( - \rho \left( x - x _ { 0 } \right) )
$$

and ensures that lim $| | \begin{array} { l } { y } \end{array} ( x \begin{array} { r } \end{array} ) | = 0$ , i.e. asymptotic stability.

# Stability of nonlinear systems

It is now easy to extend the same ideas to nonlinear equations. The following theorem is an example of such a result:

Theorem 13.6. Let the nonlinear system

$$
y ^ { \prime } = A y + g \left( x , y \right)
$$

be given with $\mathsf { R e } \lambda _ { i } < - \mathsf { \rho } < 0$ for all eigenvalues of A . Furher suppose that for each $\epsilon > 0$ there is a $\delta > 0$ such that

$$
\begin{array} { r } { | | \begin{array} { l } { g ( x , y ) } \end{array} | | \ \leq \ \epsilon | | \begin{array} { l } { y } \end{array} | \qquad \mathrm { f o r } \quad | | \begin{array} { l } { y | | < \delta } \end{array}  , \quad x \geq x _ { 0 } \ . } \end{array}
$$

Then the origin is (asymptotically) stable in the sense of Liapunov.

Proof: We use the Liapunov function $V \left( y \right)$ constructed for Lemma 13.5 and obtain from (13.25)

$$
\begin{array} { r } { \displaystyle \frac { d } { d x } V ( y ( x ) ) \leq - \mathsf { p } V ( y ( x ) ) \ ~ } \\ { +  2 \mathrm { R e } < T ^ { - 1 } y ( x ) , T ^ { - 1 } g ( x , y ( x ) ) > \ . } \end{array}
$$

Cauchy's inequality together with (13.26) yields

$$
{ \frac { d } { d x } } V \left( y \left( x \right) \right) \leq \mathbf { \alpha } ( { \mathbf { \bar { \alpha } } } _ { \mathsf { P } } + \parallel T \left. { \mathbf { \beta } } \cdot \right. T ^ { - 1 } \left. { \mathbf { \beta } } \epsilon \right) V \left( y \left( x \right) \right) ~ .
$$

For sufficiently small ε the right hand side is negative and we obtain asymptotic stability. QED.

We see that, for nonlinear systems, stability is onty ensured in a neighbourhood of the origin. This can also be observed in Figure 12.3. Another difference is that the stability for eigenvalues on the imaginary axis can be destroyed. An example for this (Routh (1877), p. 95) is the system

$$
y _ { 1 } ^ { \prime } = - y _ { 2 } + { y ^ { 3 } } _ { 1 } , \qquad y _ { 2 } ^ { \prime } = y _ { 1 } .
$$

Here, with the Liapunov function $V = ( y _ { 1 } ^ { ~ 2 } + y _ { 2 } ^ { ~ 2 } ) / 2$ ，we obtain $V \ ^ { \prime } { = } y \mathbf { \Sigma } _ { 1 } ^ { 4 }$ which is $> 0$ for $y _ { 1 } \neq 0$ . Therefore all solutions with initial value $\neq 0$ increase. A survey of this question ("the centre problem") together with its connection to limit cycles is given in Wanner (1983).

# Stability of non-autonomous systems

When the coefficients are not constant,

$$
y ^ { \prime } = A \left( x \right) y ,
$$

it is not a sufficient test of stability that the eigenvalues of A satisfy the conditions of stability for each instantaneous value of $x$ ·

Examples: 1. (Routh (1877), p. 96)

$$
y _ { 1 } ^ { \prime } = y _ { 2 } , \quad y _ { 2 } ^ { \prime } = - \frac { 1 } { 4 x ^ { 2 } } y _ { 1 }
$$

which is satisfied by $y _ { 1 } ( x ) { = } a { \sqrt { x } }$

2. An example with eigenvalues strictly negative: we start with

$$
B ~ = ~ \left( \begin{array} { c c } { { - 1 } } & { { 0 } } \\ { { 4 } } & { { - 1 } } \end{array} \right) ~ , ~ y ^ { \prime } = B y .
$$

An inspection of the derivative of $V = ( y _ { 1 } ^ { ~ 2 } + y _ { 2 } ^ { ~ 2 } ) / 2$ shows that V increases in the sector

$$
\frac { 1 } { 2 + \sqrt { 3 } } < \frac { y _ { 2 } } { y _ { 1 } } < 2 + \sqrt { 3 } .
$$

The idea is to take the initial value in this region and, for $x$ increasing, to rotate the coordinate system with the same speed as the solution rotates:

$$
y ^ { \prime } = T \left( x \right) B T \left( - x \right) y = A \left( x \right) y , T \left( x \right) = \left( \begin{array} { c c } { \cos a x } & { - \sin a x } \\ { \sin a x } & { \cos a x } \end{array} \right) .
$$

For $y \left( 0 \right) = \left( 1 , 1 \right) ^ { T }$ , the good choice for $a$ is $a = 2$ and (13.32） possesses the solution

$$
y \left( x \right) = \left( \left( \cos 2 x - \sin 2 x \right) e ^ { x } , \left( \cos 2 x + \sin 2 x \right) e ^ { x } \right) ^ { T } .
$$

This solution is clearly unstable, while $- 1$ remains for all $x$ the double eigenvalue of A $( x )$

For a third exam ple see Exercise 6 below.

We observe that stability theory for non autonomous systems is more complicated. Among the cases in which stability can be shown are the following:

1. $a _ { i i } ( x ) < 0$ and A $( x$ ) is diagonally dominant; then $\mu ( A \left( x \right) ) = 0$ and stability follows from Theorem 10.5.

2.A $( x ) = B + C \left( x \right)$ ，with $B$ constant and satisfying $\mathrm { R e } \lambda _ { i } < - \rho < 0$ for its eigenvalues, and $\displaystyle { \left| \mid C \left( x \right) \mid \right| < \epsilon }$ with $\epsilon$ so small that the proof of Theorem 13.6 can be applied.

# Exercices

1. Express the stability conditions for the polynomials $\scriptstyle z ^ { 2 } + p z + q = 0$ and $z ^ { 3 } + p z ^ { 2 } + q z + r = 0$

Result: a) $p > 0$ and $q > 0$ ; b) $p > 0$ ， $r > 0$ and $p q - r > 0$

2. (Hurwitz (1895)). Verify that Condition (13.12) is equivalent to the positivity of the principal minors of the matrix

$$
H = \left( \begin{array} { c c c c c } { a _ { 1 } } & { a _ { 3 } } & { a _ { 5 } } & { \cdots } \\ { a _ { 0 } } & { a _ { 2 } } & { a _ { 4 } } & { \cdots } \\ { } & { a _ { 1 } } & { a _ { 3 } } & { \cdots } \\ { } & { a _ { 0 } } & { a _ { 2 } } & { \cdots } \\ { } & { } & { \cdots } & { \cdots } \end{array} \right) = \left( a _ { 2 j - i } \right) _ { i , j = 1 } ^ { n }
$$

（ $a _ { k } = 0$ for $k < 0$ and $k > n$ ). Understand that Routh's algorithm (13.11) is identical to a sort of Gaussian elimination transforming $H$ to triangular form.

# 3. The polynomial

$$
\frac { 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 } { 1 0 \cdot 9 \cdot 8 \cdot 7 \cdot 6 } \frac { z ^ { 5 } } { 5 ! } + \frac { 5 \cdot 4 \cdot 3 \cdot 2 } { 1 0 \cdot 9 \cdot 8 \cdot 7 } \frac { z ^ { 4 } } { 4 ! } + \frac { 5 \cdot 4 \cdot 3 } { 1 0 \cdot 9 \cdot 8 } \frac { z ^ { 3 } } { 3 ! } + \frac { 5 \cdot 4 } { 1 0 \cdot 9 } \frac { z ^ { 2 } } { 2 ! } + \frac { 5 } { 1 0 } z + 1
$$

is the numerator of the $5 - 5$ Pade approximation to $\exp ( z )$ . Verify that all its roots satisfy $\mathrm { R e } z < 0$ . Try to establish the result for general $n$ (see e.g. Birkhoff and Varga (1965), Lemma 7).

4. (Gerschgorin). Prove that the eigenvalues of a matrix $A = ( a _ { i j } )$ lie in the union of the discs

$$
\left\{ z \mid \big | z - a _ { i i } \big | \le \sum _ { j \neq i } \big | a _ { i j } \big | \right\} .
$$

Hint: write the formula $A x = \lambda x$ in coordinates

$$
\sum _ { J } a _ { i j } x _ { j } = \lambda x _ { i } ,
$$

put the diagonal elements on the right hand side and choose i such that $| x _ { i } |$ is maximal.

5. Determine the stability of the origin for the system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = - y _ { 2 } - y _ { 1 } ^ { 2 } - y _ { 1 } y _ { 2 } ~ , } } \\ { { y _ { 2 } ^ { \prime } = y _ { 1 } + 2 y _ { 1 } y _ { 2 } ~ . } } \end{array}
$$

Hint: find a Liapunov function of degree 4 starting with $V = ( y _ { 1 } ^ { ~ 2 } + y _ { 2 } ^ { ~ 2 } ) / 2 + \cdot \cdot \cdot$ such that $V \ ^ { \prime } { = } K \ ( y \ _ { 1 } ^ { \ 2 } + y \ : _ { 2 } ^ { \ 2 } ) ^ { 2 } + \cdot \cdot \cdot$ and determine the sign of $K$ ·

6. (J. Lambert, 1986). Consider the system

$$
y ^ { \prime } = A \left( x \right) \cdot y \quad { \mathrm { ~ w h e r e ~ } } \quad A \left( x \right) = { \left( \begin{array} { l l } { - { \frac { 1 } { 4 x } } } & { { \frac { 1 } { x ^ { 2 } } } } \\ { - { \frac { 1 } { 4 } } } & { - { \frac { 1 } { 4 x } } } \end{array} \right) } \quad .
$$

a) Show that both eigenvalues of $A \ ( x )$ satisfy $\mathrm { R e } \lambda < 0$ for all $x > 0$ ，

b) Compute $\mu ( A )$ (from (10.20)) and show that

$$
\mu ( A ) \ \leq \ 0 \quad \quad \mathrm { i f f } \quad \ \sqrt { 5 } { - 1 } \leq x \ \leq \ \sqrt { 5 } { + 1 } \ .
$$

c) Compute the general solution of (13.34).

Hint: introduce the new functions

$$
z _ { 2 } ( x ) = y _ { 2 } ( x ) , \qquad z _ { 1 } ( x ) = x y _ { 1 } ( x )
$$

which leads to the second equation of (11.19) (Exercise 5 of Section I.11).

Solution:

$$
\begin{array} { l } { { y _ { 1 } ( x ) = x ^ { - 3 / 4 } \biggl ( a + b \log x \biggr ) } } \\ { { y _ { 2 } ( x ) = x ^ { 1 / 4 } \biggl ( - \frac { a } { 2 } + b ( 1 - \frac { 1 } { 2 } \mathrm { l o g } x ) \biggr ) \ . } } \end{array}
$$

d) Determine α and $^ b$ such that $| | \begin{array} { l } { y ( x ) } \end{array} | | \begin{array} { l } { 2 } \\ { 2 } \end{array} $ is increasing for $0 < x < \sqrt { 5 } - 1$   
e)_Determine α and $^ b$ such that $\left| \left| \begin{array} { l } { } \\ { y } \end{array} \right( x \begin{array} { l } { } \\ { } \end{array} \right) \left| \begin{array} { l } { 2 } \\ { 2 } \end{array} \right.$ is increasing for $\sqrt { 5 } + 1 < x < \infty$   
Results: $b = 1 . 8 1 1 6 0 3 5 a$ for d) and $b = 0 . 2 4 6 2 0 1 5 a$ for e).

7. Help James Watt (see original drawing from 1788 in Figure 13.3) to solve the stability problem for his steam engine governor: if ω is the rotation speed of the engine, its acceleration is influenced by the steam supply and exterior work as follows:

$$
{ \mathfrak { w } } ^ { \prime } = ( k \cos ( \Phi + { \mathfrak { a } } ) - F ) ~ , \qquad k ~ , F > 0 ~ .
$$

![](images/2a256b806c99a27c8787ecadafc9adc707c6d70f1138ca4c8df367bf184c378b.jpg)  
Figure 13.3. James Watt's steam engine governor

Here $\Phi$ and $\propto$ are the angles shown in Figure 13.3. The acceleration of $\phi$ is determined bycentrifugal force, weight,and friction as

$$
\phi ^ { \prime \prime } = \omega ^ { 2 } \mathrm { s i n } \phi \mathrm { c o s } \phi - g \mathrm { s i n } \phi - b \phi ^ { \prime } \qquad g , b > 0 .
$$

Compute the equilibrium point $\phi ^ { \prime \prime } { = } \phi ^ { \prime } { = } { \mathfrak { o } } ^ { \prime } { = } 0$ and determine under which conditions it is stable (the solution is easier for $\mathbf { \alpha } _ { \mathbf { \alpha } } \mathbf { \alpha } _ { \mathbf { \alpha } } \mathbf { \alpha } _ { \mathbf { \beta } }$ ).

Correct solutions should be sent to: James Watt, famous inventor of the steam engine, Westminster Abbey, 6HQ 1FX London.

Remark: Hurwitz’ paper (1895) was motivated by a similar practical problem,namely".. die Regulirung von Turbinen des Badeortes Davos".

# 1.14. Derivatives with respect to parameters and initial values

'For a single equation, Dr. Ritt has solved the problem indicated in the title by a very simple and direct method. Dr. Ritt's proof cannot be ex tended immedi-ately to a system of equations".   
(T.H. Gronwall, 1919)

In this section we consider the question whether the solutions of differential equations are differentiable

a) with respect to the initial values; b) with respect to constant parameters in the equation; and how these derivatives can be computed. Both questions are, of course, of extreme importance: once a solution has been computed (numerically) for given initial values, one often wants to know how small changes of these initial values affect the solutions. This question arises e.g. if some initial values are not known exactly and must be determined from other conditions, such as prescribed boundary values. Also, the initial values may contain errors, and the effect of these errors has to be studied. The same problems arise for un-known or wrong constant parameters in the defining equations.

Problems a) and b) are equivalent: let

$$
y ^ { \prime } = f \left( x , y , p \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

be a system of differential equations containing a parameter $p$ (or several parameters). We can add this parameter to the solutions

$$
\begin{array} { r l r } { ( { y ^ { \prime } } _ { p ^ { \prime } } ) } & { { } = } & { ( { f ( x , y , p ) } ) , \qquad { y ( x _ { 0 } ) } = y _ { 0 } } \\ { p ^ { \prime } ) } & { { } = } & { ( { f ( x , y , p ) } ) , \qquad p ( x _ { 0 } ) = p ^ { } , } \end{array}
$$

so that the parameter becomes an initial value for $p ^ { \prime } { = } 0$ . Conversely, for a differential system

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

we can write $y \left( x \right) { = } z \left( x \right) { + } y _ { 0 }$ and obtain

$$
z ^ { \prime } = f \left( x , z + y _ { 0 } \right) = F \left( x , z , y _ { 0 } \right) , z \left( x _ { 0 } \right) = 0 ,
$$

so that the initial value has become a parameter. Therefore, of the two problems a) and b)， we start with b) (as did Gronwall), because it seems simpler to us.

# The derivative with respect to a parameter

Usually, a given problem contains several parameters. But since we are interested in partial derivatives, we can treat one parameter after another while keeping the remaining ones fixed. It is therefore sufficient in the following theory to suppose that $f \left( x \ , \ y \ , \ p \right)$ ）depends only on one scalar parameter $p$ ·

When we replace the parameter $p$ in (14.1） by $q$ we obtain another solution, which we denote by $z ( x )$ ：

$$
z ^ { \prime } = f \left( x , z , q \right) , \qquad z \left( x _ { 0 } \right) = y _ { 0 } .
$$

It is then natural to subtract (14.1) from (14.3) and to linearize

$$
\begin{array} { l } { { z ^ { \prime } - y ^ { \prime } = f \left( x , z , q \right) - f \left( x , y , p \right) } } \\ { { { } } } \\ { { { } = \displaystyle \frac { \partial f } { \partial y } ( x , y , p ) ( z - y ) + { \sf p } _ { 1 } { \cdot } ( z - y ) } } \\ { { { } ~ } } \\ { { { } ~ + ~ \displaystyle \frac { \partial f } { \partial p } ( x , y , p ) ( q - p ) + { \sf p } _ { 2 } { \cdot } ( q - p ) . } } \end{array}
$$

If we put $\left( z \left( x \right) - y \left( x \right) \right) / \left( q - p \right) = \psi \left( x \right)$ and drop the error terms, we obtain

$$
\Psi ^ { \prime } = \frac { \partial f } { \partial y } \big ( x , y \big ( x \big ) , p \big ) \Psi + \frac { \partial f } { \partial p } \big ( x , y \big ( x \big ) , p \big ) , \psi ( x _ { 0 } ) = 0 .
$$

This equation is the key to the problem. In order that it make sense, we need hypotheses about the existence of the derivatives that occur:

Theorem 14.1. (Gronwall (1919)). Suppose that for $x _ { 0 } \leq x \leq x$ ， the partial derivatives

$$
\frac { \partial f } { \partial y } a n d \frac { \partial f } { \partial p }
$$

exist and are continuous in the neighbourhood of the solution $y \left( x \right)$ . Then the partial derivatives

$$
{ \frac { \partial y \left( x \right) } { \partial p } } = \Psi ( x )
$$

exist, are continuous, and satisfy the differential equation (14.5).

Proof: This theorem was the origin of the famous Gronwall lemma (see I.10., Exercice 2). We prove it here by the equivalent Theorem 10.2. Set

$$
L ~ = \operatorname* { m a x } \parallel \frac { \partial f } { \partial y } \parallel ~ , ~ A ~ = \operatorname* { m a x } \parallel \frac { \partial f } { \partial p } \parallel
$$

where the max is taken over the domain under considcration. When we consider $z ( x )$ as an approximate solution for (14.1) and use

Theorem 10.2 a first time, we have for the defect

$$
\begin{array} { r l } { \left| \left| \mathbf { \sigma } _ { z } ^ { \prime } ( x \mathbf { \theta } ) - f \left( x , z , \left( x \right) , p \right) \right| \right| } & { = \left| \left| f \left( x , z \left( x \right) , q \right) - f \left( x , z \left( x \right) , p \right) \right| \right| } \\ & { \leq \mathbf { \sigma } _ { A } \left| q - p \right| , } \end{array}
$$

therefore

$$
| | z ( x ) - y ( x ) | | \ \leq \ { \frac { A } { L } } | q - p \ | { \bigl ( } e ^ { L ( x - x _ { 0 } ) } - 1 { \bigr ) } \ .
$$

So for $| q - p$ |sufficiently small and $x _ { 0 } { \leq } x \leq X$ ， we can have $\left| \begin{array} { l l l } { z \left( x \right) - y \left( x \right) } \end{array} \right|$ arbitrarily small. By definition of differentiability and by (14.7)， for each $\epsilon > 0$ there is a δ such that the error terms in (14.4) satisfy

$$
\| { \bf \rho } _ { \mathsf { p } _ { 1 } } ( z - y ) + { \mathsf { p } _ { 2 } } ( q - p ) \| \ \leq \ \epsilon \left| q - p \right| \ \quad \mathrm { i f } \quad | q - p \ | \ \leq \ \delta \ .
$$

(The situation is, in fact, a little more complicated: the δ for the bounds i ${ \boldsymbol { \rho } } _ { 1 } \parallel < \epsilon$ and $\| \mathsf { \Omega } \mathsf { \rho } _ { 2 } \| < \epsilon$ may depend on $x$ . But due to compactness and continuity, it can then be replaced by an uniform bound. Another possibility to overcome this little obstacle would be a bound on the second derivatives. But why should wc worry about this detail? Gronwall himself did not mention it).

We now consider $( z \left( x \right) - y \left( x \right) ) / ( q - p )$ as an approximate solution for (14.5) and apply Theorem 10.2 a second time. Its defect is by (14.8) and (14.4) bounded by $\epsilon$ and the linear differential equation (14.5) also has $\mathcal { L }$ as a Lipschitz constant (see (11.2)). Therefore from (10.14) we obtain

$$
| | \frac { z \left( x \right) - y \left( x \right) } { q - p } - \Psi ( x ) | | \ \leq \ \frac { \epsilon } { L } \big ( e ^ { L \left( x - x _ { 0 } \right) } - 1 \big )
$$

which becomes arbitrarily small; this proves that $\psi ( x )$ is the derivative of $y \left( x \right)$ with respect to $\boldsymbol { p }$

Continuity: The partial derivatives $\partial y / \partial p = \Psi ( x )$ are solutions of the differential equation (14.5), which we write as

$$
\Psi ^ { \prime } = g \left( x , \Psi , p \right) ,
$$

where by hypothesis $g$ depends continuously on $p$ . Therefore the continuous dependence of $\psi$ on $\boldsymbol { p }$ follows again from Theorem 10.2. QED.

Theorem 14.2. Let $y \left( x \right)$ be the solution of Equation (l4.1) and consider the Jacobian

$$
\begin{array} { r } { A \left( x \right) = \frac { \partial f } { \partial y } ( x , y \left( x \right) , p ) . } \end{array}
$$

Let $R \ ( { \boldsymbol { x } } \ , \ { \boldsymbol { x } } \ _ { 0 } )$ be the resolvent of the equation $y ^ { \prime } { = } A \ ( x \ ) y$ (see (11.4)).

Then the solution $z \left( x \right)$ of (14.3) with a slightly perturbed parameter $q$ is given by

$$
z \left( x \right) = y \left( x \right) + ( q - p ) \int _ { x _ { 0 } } ^ { x } { R \left( x , s \right) \frac { \partial f } { \partial p } ( s , y \left( s \right) , p ) d s } + { \bf o } ( \left| q - p \right| )
$$

Proof: This is the variation of constants formula (11.12) applied to (14.5). QED.

It can be seen that the sensitivity of the solutions to changes of parameters is influenced firstly by the partial derivatives $\partial f / \partial p$ (which is natural), and secondly by the size of $\textit { R } ( x , s )$ , i.e. by the stability of the differential equation with matrix (14.9).

# Derivatives with respect to initial values

Notation. We denote by $y ( x , x _ { 0 } , y _ { 0 } )$ the solution $y \left( x \right)$ at the point $x$ satisfying the initial values $y \left( x _ { 0 } \right) { = } y _ { 0 }$ , and hope that no confusion arises from the use of the same letter y for two different functions.

The following identities are trivial by definition or follow from uniqueness arguments as for (11.6):

$$
\begin{array} { c } { { \displaystyle { \frac { \partial y ( x , x _ { 0 } , y _ { 0 } ) } { \partial x } = f ( x , y ( x , x _ { 0 } , y _ { 0 } ) ) } } } \\ { { y ( x _ { 0 } , x _ { 0 } , y _ { 0 } ) = y _ { 0 } } } \\ { { y ( ( x _ { 2 } , x _ { 1 } , y ( x _ { 1 } , x _ { 0 } , y _ { 0 } ) )  = y ( x _ { 2 } , x _ { 0 } , y _ { 0 } )  } } \end{array}
$$

Theorem 14.3. Suppose that the partial derivative of $f$ with respect to y exists and is continuous. Then the solutions $y \left( x \mathrm { ~ , ~ } x _ { 0 } , y _ { 0 } \right)$ are differentiable with respect to $y _ { 0 }$ and the derivative is given by the matrix

$$
\frac { \partial y \left( x , x _ { 0 } , y _ { 0 } \right) } { \partial y _ { 0 } } = R \left( x , x _ { 0 } \right)
$$

where $R$ is the solution of the so-called "variational equation"

$$
\begin{array} { l } { \displaystyle { \frac { \partial R \left( x , x _ { 0 } \right) } { \partial x } = \frac { \partial f } { \partial y } ( x , y \left( x , x _ { 0 } , y _ { 0 } \right) ) \cdot R \left( x , x _ { 0 } \right) , } } \\ { \displaystyle { R \left( x _ { 0 } , x _ { 0 } \right) = I } . } \end{array}
$$

Proof: We know from (14.2) and $( 1 4 . 2 ^ { \circ } )$ that $\partial F / \partial z$ and $\partial F / \partial y _ { 0 }$ are both equal to $\partial f / \partial y$ ， so the derivatives are known to exist by

Theorem 14.1. In order to obtain Formula (14.15)， we just have to differentiate (14.11) and (14.12) with respect to $y _ { 0 }$ QED.

We finally compute the derivative of $y \left( x , x _ { 0 } , y _ { 0 } \right)$ with respect to $x _ { 0 }$

Theorem 14.4. Under the same hypothesis as in Theorem 14.3， the solutions are also differentiable with respect to $x _ { \textup { 0 } }$ and the derivative is given by

$$
\frac { \partial y \left( x , x _ { 0 } , y _ { 0 } \right) } { \partial x _ { 0 } } = - R \left( x , x _ { 0 } \right) \cdot f \left( x _ { 0 } , y _ { 0 } \right) .
$$

Proof: Differentiate the identity

$$
y \left( x _ { 1 } , x _ { 0 } , y \left( x _ { 0 } , x _ { 1 } , y _ { 1 } \right) \right) = y _ { 1 } ,
$$

which follows from (14.13)， with respect to $x _ { 0 }$ and apply (14.14） and (14.11) (see Exercise 3). QED.

# The nonlinear variation-of-constants formula

We close this section with an extension of Theorem 11.2 to sys-tems of non-linear differential equations.

Theorem 14.5.(Alekseev (1961)，,Grobner (1960).Denote byy and z the solutions of

$$
\begin{array} { r l r } & { \boldsymbol { y } ^ { \prime } = f \left( x , y \right) , } & { \quad \boldsymbol { y } \left( x _ { 0 } \right) = \boldsymbol { y } _ { 0 } , } \\ & { \boldsymbol { z } ^ { \prime } = f \left( x , z \right) + g \left( x , z \right) , } & { \quad \boldsymbol { z } \left( x _ { 0 } \right) = \boldsymbol { y } _ { 0 } , } \end{array}
$$

respectively and suppose that df/dy exists and is continuous. Then the solutions of (14.17a) and of the "perurbed" equation (14.17b) are connected by

$$
z ( x ) = y ( x ) + \intop _ { x _ { 0 } } ^ { x } \frac { \partial y } { \partial z } ( x , s , z ( s ) ) \ g \left( s , z \left( s \right) \right) d s ,
$$

Proof: We choose a subdivision $x _ { 0 } = s _ { 0 } < s _ { 1 } < s _ { 2 } < . . . < s _ { N } = x$ (see Figure 14.1). The descending curves represent the solutions of the unperturbed equation (14.17a) with initial values $s _ { i } , z \left( s _ { i } \right)$ The differences $d _ { i }$ are, due to the different slopes of $z \left( s \right)$ and $y \left( s \right)$ ((14.17b) minus (14.17a)), equal to $d _ { i } = g \left( s _ { i } , z \left( s _ { i } \right) \right) \cdot \Delta s _ { i } + \mathbf { o } ( \Delta s _ { i } ) .$ This "error" at $s _ { i }$ is then "transported" to the final value $x$ by the amount given in Theorem 14.3, to give

$$
\begin{array} { r } { D _ { i } ^ { \phantom { } } = \frac { \partial y } { \partial z } ( x ^ { \phantom { } } , s _ { i } ^ { \phantom { } } , z ( s _ { i } ^ { \phantom { } } ) ) { \cdot } g ( s _ { i } ^ { \phantom { } } , z ( s _ { i } ^ { \phantom { } } ) ) { \cdot } \Delta s _ { i } ^ { \phantom { } } \phantom { } + \mathbf { o } ( \Delta s _ { i } ^ { \phantom { } } ) \phantom { \cdot } , } \end{array}
$$

![](images/e4f3fc4bd687d42917a9a36745c03903b279419f7dce94df5567510dff0ac03b.jpg)  
Figure 14.1. Lady Windermere's fan, Act 2

Since

$$
z \left( x \right) - y \left( x \right) = \sum _ { i = 1 } ^ { N } D _ { i } ,
$$

we obtain the integral in (14.18) after insertion of (14.19) and passing to the limit $\Delta s _ { i } \to 0$ . QED.

If we also want to take into account a possible difference in the initial values, we may formulate:

Corollary 14.6. Let $y \left( x \right)$ and $z \left( x \right)$ be the solutions of

$$
\begin{array} { l r } { { y ~ ^ { \prime } = f \left( x , y \right) ~ , } } & { { y \left( x _ { 0 } \right) = y _ { 0 } ~ , } } \\ { { } } & { { } } \\ { { z ^ { \prime } = f \left( x , z \right) + g \left( x , z \right) ~ , } } & { { z \left( x _ { 0 } \right) = z _ { 0 } ~ , } } \end{array}
$$

then

$$
\begin{array} { c } { { z \left( x \right) = y \left( x \right) + \displaystyle \int _ { 0 } ^ { 1 } \frac { \partial y } { \partial z } ( x , x _ { 0 } , y _ { 0 } + s \left( z _ { 0 } - y _ { 0 } \right) ) \cdot ( z _ { 0 } - y _ { 0 } ) d s } } \\ { { \displaystyle \phantom { x x } _ { 0 } ^ { x } } } \\ { { + \displaystyle \int _ { x _ { 0 } } ^ { x } \frac { \partial y } { \partial z } ( x , s , z \left( s \right) ) \cdot g \left( s , z \left( s \right) \right) d s . } } \end{array}
$$

NED.

These two theorems allow many estimates of the stability of general nonlinear systems. For linear systems, $\frac { \partial y } { \partial z } ( x , s , z )$ is independent of $z$ ，and Formulas (14.20) and (14.17) become the variationof-constants Formula (11.12). Also, by majorizing the integrals in (14.20) in a trivial way, one obtains thc fundamental lemma (10.14) and also the variant form of Theorem 10.2.

# Exercices

1. Study the dependence on the initial values of

$$
y ^ { \prime } = { y ^ { 2 } } , \quad x _ { 0 } = 0 \ , \quad y _ { 0 } = 1 \ , \quad X = 0 . 9 9 9 \ .
$$

2. Solve Equation (14.21) numerically by using 999 steps of Euler's method (7.3） with ${ x _ { i + 1 } } - { x _ { i } } = . 0 0 1$ Estimate the influence of the errors in the first step (which is $1 0 ^ { - 6 }$ ） on the final result， and ex plain the low precision.

3. Prove the following lemma from elementary calculus which is used in the proof of Theorem 14.4:

If for a function $F \left( x , y \right)$ , əF/dy exists and $y \left( x \right)$ is differentiable and such that

$$
F ( x , y ( x ) ) = c o n s t ,
$$

then F exists at $\left( x , y \left( x \right) \right)$ and is equal to

$$
{ \frac { \partial F } { \partial x } } ( x , y ( x ) ) = - { \frac { \partial F } { \partial y } } ( x , y ( x ) ) { \cdot } y ^ { \prime } ( x ) .
$$

Hint: Derive from (14.22) the identity

$$
F ( x \mathbin { \lrcorner } y ( x \mathbin { \lrcorner } ) ) - F ( x \mathbin { \lrcorner } y ( x \mathbin { \lrcorner } ) ) = F ( x \mathbin { \lrcorner } y ( x \mathbin { \lrcorner } ) ) - F ( x \mathbin { \lrcorner } y ( x \mathbin { \lrcorner } ) ) \ .
$$

I.15. Boundary value and eigenvalue problems

Although our book is mainly concerned with initial value problems, we want to include in this first chapter some properties of boundary and eigenvalue problems.

# Boundary value problems

They arise in systems of differential equations, say

$$
\begin{array} { r } { { y _ { 1 } ^ { \prime } = f _ { 1 } ( x , y _ { 1 } , y _ { 2 } ) \ , } } \\ { { { } } } \\ { { y _ { 2 } ^ { \prime } = f _ { 2 } ( x , y _ { 1 } , y _ { 2 } ) \ , } } \end{array}
$$

when there is no initial point $x _ { 0 }$ at which $y _ { 1 } ( x _ { 0 } )$ and $y _ { 2 } ( x _ { 0 } )$ are known simultaneously. Questions of existence and uniqueness then become much more complicated.

Example 1 : Consider the differential equation

$$
y ^ { \prime \prime } = \exp ( y ) \quad \mathrm { o r } \qquad y _ { 1 } ^ { \prime } = y _ { 2 } , y _ { 2 } ^ { \prime } = \exp ( y _ { 2 } )
$$

with the boundary conditions

$$
y _ { 1 } ( 0 ) = a , y _ { 1 } ( 1 ) = b .
$$

In order to apply our existence theorems or to do numerical computations (say by Euler's method (7.3)), we can proceed as follows: guess the missing initial value $y _ { 2 0 }$ We can then compute the solution and check whether the computed value for $y _ { 1 } ( 1 )$ is equal to $^ b$ or not. So our problem is,whether thefunctionof thesinglevrble $y _ { 2 0 }$

$$
F ( y _ { 2 0 } ) : = y _ { 1 } ( 1 ) - b
$$

possesses a zero or not.

Equation (15.2a) is quasimonotone, which implies that $F \left( y _ { 2 0 } \right)$ depends monotonically on $y _ { 2 0 }$ (Figure 15.1a, see Exercise 3 of I.10). Also, for $y _ { 2 0 }$ very small or very large, $y _ { 1 } ( 1 )$ is arbitrarily small or large, or even infinite. Therefore, (15.2) possesses for all $^ a$ ， $^ b$ a unique solution (see Figure 15.1b).

The root of $F \left( y _ { 2 0 } \right) { = } 0$ can be computed by an iterative method, (bisctio $y _ { 1 } ( 1 )$ with respect to $y _ { 2 0 }$ is used from Theorem 14.3 or numerically from finite differences,

![](images/615fd776434a39d632759ef20f924abf65e4c0690fe596fb2e82f9caa887750f.jpg)  
Figure 15.1. a) Solutions of (15.2a) for diferent initial values $y _ { 2 0 } { = } { - } 1 . 7 , . . . , { - 0 . 4 }$

b) Unique solution of (15.2a) for $a = 1$ ， $b = 2$ ， $y _ { 2 0 } = - 0 . 4 7 6 9 8 4 6 5 6$   
c) Solutions of (15.4a) for $y \left( 0 \right) { = } 1$ and $y _ { 2 0 } = 1 , 2 , \ldots , 8$   
d） The two solutions of (15.4a)， $y \left( 0 \right) = 1$ ， $y \left( 1 \right) { = } 0 . 5$ $y _ { 2 0 } { = } 7 . 9 3 7 1 9$ ，   
y 20=0.97084

also by Newton's method). The initial value problem is then computed several times. Small problems, such as the above example, can be done by a simple dialogue with the computer. Harder problems with more unknown initial values need more programmational sophistication. This method is one of the most commonly used and is called the shooting method.

Example 2: For the differential equation

$$
y ^ { \prime \prime } = - \exp ( y ) \quad \mathrm { ~ o r ~ } \qquad y _ { 1 } ^ { \prime } = y _ { 2 } , y _ { 2 } ^ { \prime } = - \exp ( y _ { 2 } )
$$

with the boundary conditions

$$
y _ { 1 } ( 0 ) = a ~ , ~ y _ { 1 } ( 1 ) = b
$$

the monotonicity of $F \left( y _ { 2 0 } \right)$ is lost and things become more complicated: solutions for different initial values $y _ { 2 0 }$ are sketched for $a = 1$ in Figure 15.1c. It can be seen that for $^ b$ above a certain value (which is 1.499719998) there exists no solution of the problem at all, and for $^ b$ below this value there exist two solutions (Figure 15.1d).

Example 3:

$$
y _ { 1 } ^ { \prime } = y _ { 2 } , y _ { 2 } ^ { \prime } = y _ { 1 } ^ { 3 } , y _ { 1 } ( 0 ) = 1 , y _ { 1 } ( 1 0 0 ) = 2 .
$$

This equation is similar to (15.2) and the same statement of existence and uniqueness holds as above. However, if one tries to compute the solutions by the shooting method, one gets into trouble because of the length of the interval: the solution nearly never exists on the whole interval; in fact， the correct solution is $y _ { 2 0 } = - 0 . 7 0 7 1 0 6 1 6 6 5 5$ But already for $y _ { 2 0 } { = } { - } 0 . 7 0 7 1 0 6 1$ ， $y _ { 1 } ( x )$ tends to $+ \infty$ for $x \to 9 8 . 2$ . On the other side, for ${ \therefore } { 2 0 } ^ { = - 0 . 7 0 7 1 1 }$ ,we have $y _ { 1 } ( 9 4 . 1 ) = - \infty$ So the dom ain where $F \left( y _ { 2 0 } \right)$ of (15.3) exists is of length less than $4 \times 1 0 ^ { - 6 }$

In a case like this, one uses the multiple shooting technique: the interval is split up into several subintervals, on each of which the solution is solved with well-chosen initial values. At the endpoints of the subintervals, the solutions are then matched together. Equation (15.3) thereby becomes a system of higher dimension to be solved. There exists an extensive literature on multiple shooting. As a general reference we give Deuflhard (1980).

# Sturm-Liouville eigenvalue problems

This subject originated with a remarkable paper of Sturm (Sturm (1836)) in Liouville's newly founded Journal. This paper was followed by a series of papers by Liouville and Sturm published in the following volumes. It is today considered as the starting point of the "geometric theory", where the main effort is not to try to integrate the equation， but merely to obtain geometric properties of the solution, such as its form, oscillations, sign changes, zeros, existence of maxima or minima and so on, directty from the differential equation ("Or on peut arriver a ce but par la seule consideration des equations differentielles en elles-memes， sans qu'on ait besoin de leur integration".)

The physical origin was, as in Section I.6, the study of heat and small oscillations of elastic media. Let us consider the heat equation with non-constant conductivity

$$
\frac { \partial u } { \partial t } = \frac { \partial } { \partial x } \left( k \left( x \right) \frac { \partial u } { \partial x } \right) - l \left( x \right) u , k \left( x \right) > 0 ,
$$

which was studied extensively in Poisson's "Theorie de la chaleur". Poisson assumes $u \left( x , t \right) = y \left( x \right) e ^ { - \mathsf { A } t }$ , so that (15.6) becomes

$$
{ \frac { d } { d x } } \left( k \left( x \right) { \frac { d y } { d x } } \right) - l ( x ) y \ = - \lambda y .
$$

We write (15.7) in the form

$$
( k ( x ) y \prime ) ^ { \prime } + G ( x ) y = 0
$$

and state the following comparison theorem of Sturm:

Theorem 15.1. Consider, with (15.8), the differential equation

$$
( \hat { k } ( x ) \hat { y } ^ { \prime } ) ^ { \prime } + \hat { G } ( x ) \hat { y } \ = 0 \ ,
$$

and assume k , $\hat { k }$ differentiable, $G$ ， $\hat { G }$ continuous,

$$
0 < \hat { k } \left( x \right) \le { k } \left( x \right) , \hat { G } \left( x \right) \ge G \left( x \right)
$$

for all $x$ and let $y \left( x \right)$ ， $\hat { y } \left( x \right)$ be linearly independent solutions of (15.8) and (15.9)， respectively. Then, between any two zeros of $y \left( x \right)$ there is at least one zero of ${ \hat { y } } \left( x \right)$ ,i.e. if $y \left( x  { 1 } \right) = y \left( x  { 2 } \right) = 0$ with $x _ { 1 } < x _ { 2 }$ then there exists $x _ { 3 }$ in the open interval $( x _ { 1 } , x _ { 2 } )$ such that $\hat { y } \left( x _ { 3 } \right) = 0$

Proof: The original proof of Sturm is based on the quotient

$$
q \left( x \right) = \frac { y \left( x \right) } { k \left( x \right) y ^ { \prime } ( x ) }
$$

which is the slope of the line connecting the origin with the solution point in the $\left( k y ^ { \prime } , y \right)$ -plane and satisfies a first-order differential equation. In order to avoid the singularities caused by the zeros of $y ^ { \prime } ( x )$ ， we prefer the use of polar coordinates (Prufer (1926))

$$
k \left( x \right) y ^ { \prime } ( x ) = \rho ( x ) \mathrm { c o s } \phi ( x ) , \qquad y \left( x \right) = \rho ( x ) \mathrm { s i n } \phi ( x ) .
$$

Differentiation of (15.11) yields the following differential equation for $\Phi$ ：

$$
\phi ^ { \prime } = \frac { 1 } { k \left( x \right) } { \cos } ^ { 2 } \phi + G \left( x \right) { \sin } ^ { 2 } \phi .
$$

In the same way we also introduce functions $\widehat { \boldsymbol { \rho } } \left( \boldsymbol { x } \right)$ and $\hat { \phi } ( x )$ for the second differential equation (15.9) and obtain

$$
\hat { \phi } ^ { \prime } = \frac { 1 } { \hat { k } \left( x \right) } { \cos } ^ { 2 } \hat { \Phi } + \hat { G } \left( x \right) { \sin } ^ { 2 } \hat { \Phi } .
$$

Suppose now that $x _ { 1 } , x _ { 2 }$ are two consecutive zeros of $y \left( x \right)$ . Then $\boldsymbol { \Phi } ( \boldsymbol { x } _ { 1 } )$ and $\Phi ( x _ { 2 } )$ must be multiples of $\pi$ ， since $\rho ( x )$ is always different from zero (uniqueness of the initial value problem). By (15.12) $\Phi ^ { \prime } ( x )$ is positive at $x _ { 1 }$ and at $x _ { 2 }$ . Therefore we may assume

$$
\phi ( x _ { 1 } ) = 0 , \phi ( x _ { 2 } ) = \pi , \hat { \phi } ( x _ { 1 } ) \in [ 0 , \pi ) .
$$

The fact that Equations (15.12) and (15.13) are first-order and the inequalities (15.10) allow the application of Theorem 10.3 to give

$$
\hat { \Phi } ( x ) \geq \phi ( x ) \quad \quad \mathrm { f o r } \quad x _ { 1 } \leq x \leq x _ { 2 } .
$$

It is impossible that $\hat { \phi } ( x ) { = } \Phi ( x )$ everywhere, since this would imply $k \left( x \right) { = } \hat { k } \left( x \right)$ ， $G \left( x \right) { = } \hat { G } \left( x \right)$ by (15.12) and (15.13) and the solutions $y \left( x \right) , \hat { y } \left( x \right)$ would be linearly dependent. Therefore, there exists

$x _ { 0 } \in ( x _ { 1 } , x _ { 2 } )$ such that $\hat { \phi } ( x _ { 0 } ) > \phi ( x _ { 0 } ) .$ In this situation $\hat { \phi } ( x ) > \phi ( x )$ for all $x \geq x _ { 0 }$ and the existence of $x  { 3 } ^ { \prime } ( \boldsymbol { x }  { 1 } , \boldsymbol { x }  { 2 } )$ with $\hat { \phi } ( x _ { 3 } ) = \pi$ is ensured. QED.

The next theorem shows that our eigenvalue problem possesses an infinity of solutions. We add to (15.7) the boundary conditions

$$
y ( x _ { 0 } ) = y ( x _ { 1 } ) = 0 .
$$

Theorem 15.2. The eigenvalue problem (15.7), $( \ I { \boldsymbol { \ S } } \ J { \boldsymbol { \ S } } )$ possesses an infinite sequence of eigenvalues $\lambda _ { 1 } < \lambda _ { 2 } < \lambda _ { 3 } < . . .$ whose corresponding solutions $y _ { i } ( x \ )$ ("eigenfunctions") possess respectively 0,1,2,.. zeros inside the interval $( x _ { 0 } , x _ { 1 } )$ . The zeros of $y _ { j + 1 } ( x )$ separate those of $y _ { j } ( x )$ .If $0 < K _ { 1 } \leq k \left( x \right) \leq K _ { 2 }$ and $L _ { 1 } { \le } l ( x ) { \le } L _ { 2 } ,$ then

$$
L _ { 1 } + K _ { 1 } \frac { { j ^ { 2 } \pi } ^ { 2 } } { \left( x _ { 1 } - x _ { 0 } \right) ^ { 2 } } \le \mathtt { A } _ { j } \le L _ { 2 } + K _ { 2 } \frac { { j ^ { 2 } \pi } ^ { 2 } } { \left( x _ { 1 } - x _ { 0 } \right) ^ { 2 } } \ .
$$

Proof: Let $y \left( x , \lambda \right)$ be the solution of (15.7) with initial values $y \left( x _ { 0 } \right) = 0 , y ^ { \prime } ( x _ { 0 } ) = 1$ .Theorem 15.1 (with $k \left( x \right) { = } k \left( x \right)$ ， ${ \hat { G } } \left( x \right) { = } G \left( x \right)$ $+ \Delta \lambda )$ implies that for increasing 入 the zeros of $y \left( x , \lambda \right)$ move towards $x _ { 0 }$ ， so that the number of zeros in $( x _ { 0 } , x _ { 1 } )$ is a non-decreasing function of $\lambda$

Comparing next (15.7) with the solution $( \lambda > L _ { 1 } )$

$$
\sin ( \sqrt { ( \lambda - L _ { 1 } ) / K _ { 1 } } ( x - x _ { 0 } ) )
$$

of $K _ { 1 } y ~ ^ { \prime \prime } { + } ( \lambda { - } L _ { 1 } ) y { = } 0$ 。wesee that $y \left( x , \lambda \right)$ possessesfor $\lambda { < } L _ { 1 } { + } K _ { 1 } j ^ { 2 } \pi ^ { 2 } / \left( x _ { 1 } { - } x _ { 0 } \right) ^ { 2 }$ at most $j - 1$ zeros in $( x _ { 0 , } x _ { 1 } ]$ .Similarly, a comparison with

$$
\sin ( \sqrt { ( \lambda - L _ { 2 } ) / K _ { 2 } } ( x - x _ { 0 } ) )
$$

which is a solution of $K _ { 2 } y \ ^ { \prime \prime } + ( \lambda - L _ { 2 } ) y = 0$ ， shows that for $\lambda > L _ { 2 }$ $+ K _ { 2 } j ^ { 2 } \pi ^ { 2 } / ( x _ { 1 } - x _ { 0 } ) ^ { 2 }$ the function $y \left( x , \lambda \right)$ possesses at least $j$ zeros in $( x _ { 0 } , x _ { 1 } ) .$ The statements of the theorem are now simple consequences of these three properties. QED.

Example: Figure 15.2 shows the first 5 solutions of the problem

$$
( ( 1 - 0 . 8 \sin ^ { 2 } x ) y ^ { \prime } ) ^ { \prime } - ( x - \mathtt { \mathtt { A } } ) y \ = \ 0 \ , y ( 0 ) \ = y \left( \pi \right) = 0 \ .
$$

The first eigenvalues are 2.1224， 3.6078， 6.0016, 9.3773， 13.7298,19.053,25.347,32.609,40.841, 50.041, etc.

For more details about this theory, which is a very important page of history, we refer to the book of Reid (1980).

![](images/30314fa6c289f5135454d7c8a50fdccfcaa8d2f6b56dd4727528fb8498edf22f.jpg)  
Figure 15.2. Solutions of the Sturm-Liouville eigenvalue problem (15.17)

# Exercises

1. Consider the equation

$$
L ( x ) y ^ { \prime \prime } + M ( x ) y ^ { \prime } + N ( x ) y = 0 .
$$

Multiply it with a suitable function $\Phi ( x )$ ， so that the ensuing equation is of the form (15.7) (Sturm (1836), p. 108).

2. Prove that two solutions of (15.7), (15.15) satisfy the orthogonal-ity relations

$$
\begin{array} { l } { { x _ { 1 } } } \\ { { \int y _ { j } ( x ) y _ { k } ( x ) d x = 0 \ ~ \mathrm { f o r } ~ \lambda _ { j } \ne \lambda _ { k } } } \\ { { x _ { 0 } } } \end{array} .
$$

Hint. Multiply this by $\lambda _ { j }$ ,replace $\lambda _ { j } y _ { j } ( \boldsymbol { x } )$ from (15.7) and do partial integration (Liouville (1836), p. 257).

3. Solve the problem (15.5) by elementary functions. Explain why the given value for $y _ { 2 0 }$ is so close to $- \sqrt { 2 } / 2$ ·

4. (Collatz). Show that the boundary value problem

$$
y ^ { \prime \prime } = y ^ { 3 } , \quad y ( 0 ) { = } 0 , \quad y ( A ) = B
$$

possesses infinitely many solutions for each pair $^ { ( A \mathrm { ~ } , B }$ ）with $A \neq 0$ Hint. Draw the solution $y \left( x \right)$ of (15.18) with $y \left( 0 \right) = 0$ ， $y \ ^ { \prime } ( 0 ) { = } 1$ Show that for each constant $a$ ， $z \left( x \right) { = } a y \left( a x \right)$ is also a solution.

1.16. Periodic solutions, limit cycles, strange attractors

The phenomenon of limit cycles was first described theoretically by Poincare (1882) and Bendixson (1901), and has since then found many applications in Physics, Chemistry and Biology.

# Van der Pol's equation

I have a theory that whenever you want to get in trouble with a method, look for the Van der Pol equation. (P.E. Zadunaisky 1982)

The first practical examples were studied by Rayleigh (1883) and later by Van der Pol (1920-1926) in a series of papers on nonlinear oscillations: the solutions of

$$
y \prime \prime + \alpha y \prime + y \prime = 0
$$

are damped for $\alpha > 0$ , and unstable for $\alpha < 0$ . The idea is to change α (with the help of a triode, for example) so that $\alpha < 0$ for small y and $\alpha > 0$ for large y. The simplest expression,which describes the physical situation in a somewhat idealised form, would be ${ \alpha } = \epsilon ( y ^ { 2 } - 1 )$ ， $\epsilon > 0 .$ . Then the above equation becomes

$$
y ^ { \prime \prime } + \epsilon ( y ^ { 2 } - 1 ) y ^ { \prime } + y ~ = 0 ~ ,
$$

or, written as a system,

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } \\ { { { } } } \\ { { y _ { 2 } ^ { \prime } = \epsilon ( 1 { - } y _ { 1 } ^ { 2 } ) y _ { 2 } { - } y _ { 1 } ~ , ~ { \epsilon > } 0 ~ . } } \end{array}
$$

In this equation, sm all oscillations are amplified and large oscillations are damped. We therefore expect the existence of a stable periodic solution to which all other solutions converge. We call this a limit cycle. The original illustrations of the paper of Van der Pol are reproduced in Figure 16.1.

# Existence Proof

The existence of limit cycles is studied by the method of Poincaré sections. The idea is to cut the solutions transversally by a hyperplane $P$ and, for an initial value $\boldsymbol { y } _ { 0 } \in \boldsymbol { P }$ , to study the first point $\Phi (  { \boldsymbol { y } } _ { 0 } )$ where the solution again crosses the plane $P$ in the same direction.

![](images/367afdadc8a5224464576fe116588c6972b44b2b403eaa39af1ae42e13eeee14.jpg)  
Figure 16.1. Ilustrations from Van der Pol (1926) (with permission)

For our example (16.2)， we choose for $P$ the half line $y _ { 2 } { = } 0$ ， ${ \boldsymbol { y } } _ { 1 } > 0$ . We then examine the signs of $y _ { 1 } ^ { \prime }$ and $y _ { 2 } ^ { \prime }$ in (16.2). The sign of $y _ { 2 } ^ { \prime }$ changes at the curve

$$
y _ { 2 } = { \frac { y _ { 1 } } { \epsilon ( 1 { - } y _ { 1 } ^ { 2 } ) } } \ ,
$$

which is drawn as a broken line in Figure 16.2. It follows (see Figure 16.2） that $\Phi ( \boldsymbol { y } _ { 0 } )$ exists for all $\boldsymbol { y } _ { 0 } \in P$ . Since two different solutions cannot intersect (due to uniqueness), the map $\Phi$ is monotone. Further, $\Phi$ is bounded (e.g. by every solution starting on the curve (16.3)), so $\Phi ( y _ { 0 } ) < y _ { 0 }$ for $y _ { 0 }$ large. Finally， since the origin is unstable, $\Phi ( y _ { 0 } ) > y _ { 0 }$ for $y _ { 0 }$ small. Hence there must be a fixed point of $\Phi ( \boldsymbol { y } _ { 0 } )$ ， i.e., a limit cycle. QED.

![](images/1173ad76826893c74314ffee78218eed9d5b19e11dac833a00e09d77770eb839.jpg)  
Figure 16.2. The Poincare map for Van der Pol's equation, $\epsilon = 1$

R emark: The limit cycle is, in fact, unique. The proof for this is more complicated and is indicated in Exercise 8 below (Lienard (1928)).

With similar ideas one proves the following general result:

Theorem 16.1. (Poincaré (1882)， Bendixson (1901)). Each bounded solution of a two-dimensional system

$$
y _ { 1 } ^ { \prime } = f _ { 1 } ( y _ { 1 } , y _ { 2 } ) ~ , ~ y _ { 2 } ^ { \prime } = f _ { 2 } ( y _ { 1 } , y _ { 2 } )
$$

must

i) tend to a critical point ${ f _ { 1 } } ^ { = } { f _ { 2 } } ^ { = 0 }$ for an infinity of points $x _ { i } \to \infty$ ;or ii) be periodic; or   
i) tend to a limit cycle. NED.

Remark: Exercise 1 below explains why the possibility i) is writ-ten in a form somewhat more complicated than seems necessary.

# Steady-state approximations for $\epsilon$ large

An important tool for simplifying complicated nonlinear systems is that of steady-state approximations. Consider (16.2) with e very large. Then, in the neighbourhood of ${ f } _ { 2 } ( y _ { 1 } , y _ { 2 } ) { = } 0$ , the derivative of $y _ { 2 } ^ { \prime } { = } f _ { 2 }$ with respect to $y _ { 2 }$ is very large negative. Therefore the solution will very rapidly approach an equilibrium state in the neighbourhood of $y _ { 2 } ^ { \prime } { = } f _ { 2 } ( y _ { 1 } , y _ { 2 } ) { = } 0$ , i.e., in our example, $y _ { 2 } { = } y _ { 1 } / ( \in ( \overset { - } { 1 - } y _ { 1 } ^ { 2 } ) )$ This can be inserted into (16.2) and leads to

$$
y _ { 1 } ^ { \prime } = { \frac { y _ { 1 } } { \epsilon ( 1 { - } y _ { 1 } ^ { 2 } ) } } \ ,
$$

an equation of lower dimension. Using the formulas of Section I.3, (16.5) is easily solved to give

$$
\log ( y _ { 1 } ) - \frac { y _ { 1 } ^ { ~ 2 } } { 2 } = \frac { x - x _ { 0 } } { \epsilon } + c o n s t .
$$

These curves are dotted in Van der Pol's Figure l6.3 for E ${ \it \Omega } = 1 0$ and show the good approximation of this solution.

![](images/c2c04284783e66961eac8093805136ce7f325c779fa0c7bdaea6e64eec8acf70.jpg)  
Figure 16.3. Solution of Van der Pol's equation for $\epsilon = 1 0$ compared with steady state approximations

# Asymptotic solutions for ∈ small

The computation of periodic solutions for small parameters was initiated by astronomers such as Newcomb and Lindstedt and brought to perfection by Poincare (1893). We demonstrate the method for the Van der Pol equation (16.1). The idea is to develop the solution as a series in powers of $\in$ . Since the period will change too, we also introduce a coordinate change

$$
t = x \left( 1 + \gamma _ { 1 } \varepsilon + \gamma _ { 2 } \varepsilon ^ { 2 } + \cdots \right)
$$

and put

$$
y ( x ) = z ( t ) = z _ { 0 } ( t ) + \in z _ { 1 } ( t ) + \mathfrak { e } ^ { 2 } z _ { 2 } ( t ) + \cdot \cdot \cdot .
$$

Inserting now $y ^ { \prime } ( x ) = z ^ { \prime } ( t ) ( 1 + \gamma _ { 1 } \epsilon + \cdot \cdot \cdot ) , y ^ { \prime \prime } ( x ) = z ^ { \prime \prime } ( t ) ( 1 + \gamma _ { 1 } \epsilon + \cdot \gamma _ { 1 } \epsilon + \cdot \cdot \cdot ) ,$ ）² into (16.1) we obtain

$$
\begin{array} { r l } & { ( z _ { 0 } ^ { \prime \prime } + \in z _ { 1 } ^ { \prime \prime } + \mathfrak { e } ^ { 2 } z _ { 2 } ^ { \prime \prime } + \cdot \cdot \cdot ) ( 1 + 2 \gamma _ { 1 } \mathfrak { e } + ( 2 \gamma _ { 2 } + \gamma _ { 1 } ^ { 2 } ) \mathfrak { e } ^ { 2 } + \cdot \cdot \cdot ) } \\ & { \ + \mathfrak { e } \big ( ( z _ { 0 } { + } \mathfrak { e } z _ { 1 } + \cdot \cdot \cdot ) ^ { 2 } - 1 \big ) ( z _ { \ 0 } ^ { \prime } + \mathfrak { e } z _ { \ 1 } ^ { \prime } + \cdot \cdot \cdot ) ( 1 + \gamma _ { 1 } \mathfrak { e } + \cdot \cdot \cdot ) } \\ & { \qquad + ( z _ { 0 } { + } \mathfrak { e } z _ { 1 } { + } \mathfrak { e } ^ { 2 } z _ { 2 } { + } \cdot \cdot \cdot ) = 0 \ . } \end{array}
$$

We first com pare the coefficients of $\epsilon ^ { 0 }$ and obtain

$$
z _ { 0 } ^ { \prime \prime } + z _ { 0 } = 0 \ .
$$

We arbitrarily fix the initial value $z \ ^ { \prime } ( 0 ) { = } 0$ ， so that $z _ { 0 } = A$ cost . Next, the coefficients of $\epsilon$ yield

$$
\begin{array} { r } { z _ { 1 } ^ { \prime \prime } + z _ { 1 } = - 2 \gamma _ { 1 } z _ { 0 } ^ { \prime \prime } - ( z _ { 0 } ^ { \ 2 } - 1 ) z _ { 0 } ^ { \prime } \qquad } \\ { \qquad = 2 \gamma _ { 1 } A \cos t + ( \frac { A ^ { \ 3 } } { 4 } - A ) \mathrm { s i n } t + \frac { A ^ { \ 3 } } { 4 } \mathrm { s i n } 3 t \ . } \end{array}
$$

Here, the crucial idea is that we are looking for periodic solutions, hence the terms in cost and sint on the righthand side of (16.8;1) must disappear, in order to avoid that $z _ { 1 } ( t )$ contain terms of the form t ·cost and t-sint (".. et de faire disparaitre ainsi les termes dits séculaires."). We thus obtain $\gamma _ { 1 } = 0$ and $A = 2$ . Then (16.8;1) can be solved and gives together with $z _ { 1 } ^ { \prime } ( 0 ) { = } 0$ ，

$$
z _ { 1 } = B \cos t + { \frac { 3 } { 4 } } \mathrm { s i n } t - { \frac { 1 } { 4 } } \mathrm { s i n } 3 t .
$$

The continuation of this process is now clear: the terms in $\epsilon ^ { 2 }$ in (16.8) give, after insertion of (16.9) and simplification,

$$
{ \begin{array} { r l } & { z { \prime } _ { 2 } ^ { \prime \prime } + z _ { 2 } = \left( 2 \gamma _ { 2 } + { \frac { 1 } { 4 } } \right) \cos t + 2 B \sin t + 3 B \sin 3 t } \\ & { \qquad - { \frac { 3 } { 2 } } \cos 3 t + { \frac { 5 } { 4 } } \cos 5 t . } \end{array} }
$$

In order to avoid the secular terms we have to set $B = 0$ and $\gamma _ { 2 } = - 1 / 8$ and obtain

$$
z _ { 2 } = C \cos t + { \frac { 3 } { 1 6 } } \mathrm { c o s } 3 t - { \frac { 5 } { 9 6 } } \mathrm { c o s } 5 t .
$$

The next round will give $C = - 1 / 8$ and $\gamma _ { 3 } { = } 0$ ， so that we have: the periodic orbit of the Van der Pol equation (l6.1) for e smal is given by

$$
\begin{array} { l } { { y \left( x \right) = z \left( t \right) , \qquad t = x \left( 1 - \epsilon ^ { 2 } / 8 + \cdot \cdot \cdot \right) , } } \\ { { z \left( t \right) = 2 { \cos t } + \epsilon \left( \frac 3 4 { \sin t } - \frac 1 4 { \sin } 3 t \right) } } \\ { { \qquad + \epsilon ^ { 2 } \bigg ( - \frac 1 8 { \cos t } + \frac 3 { 1 6 } { \cos } 3 t - \frac 5 { 9 6 } { \cos } 5 t \bigg ) + \cdot \cdot \cdot } } \end{array}
$$

and is of period $2 \pi ( 1 + \epsilon ^ { 2 } / 8 + \cdot \cdot \cdot ) .$

# Chemical reactions

The laws of chemical kinetics give rise to differential equations which, for multi-molecular reactions, become nonlinear and have interesting properties. Some of them possess periodic solutions (e.g. the Zhabotinski-Belousov reaction） and have important applications to the interpretation of biological phenomena (e.g. Prigogine, Lefever (1969)).

Let us examine in detail the model of Lefever and Nicolis (1971)， the so-called "Brusselator": suppose that six substances $A \ , \ B \ , \ D \ , \ E \ , \ X \ , \ Y$ undergo the following reactions:

$$
\begin{array} { r l r l } & { A \xrightarrow { k _ { 1 } } - X } & & { ( 1 6 ) } \\ & { B + X \xrightarrow { k _ { 2 } } - Y + D } & & { ( \mathrm { b i m o l e c u l a r ~ r e a c t i o n } ) } \\ & { 2 X + Y \xrightarrow { k _ { 3 } } - 3 X } & & { ( \mathrm { a u t o c a t a l y t i c ~ t r i m o l e c u l a r ~ r e a c t i o n } ) } \\ & { X \xrightarrow { k _ { 4 } } - E } \end{array}
$$

If we denote by A $( x )$ ， $B \left( x \right) , \ldots$ etc. the concentrations of A , $B$ .... etc. as functions of the time $\boldsymbol { \mathscr { X } }$ , the reactions (16.11) become by the mass action law, the following differential equations

$$
\begin{array} { l } { A ^ { \prime } = - k _ { 1 } A } \\ { B ^ { \prime } = - k _ { 2 } B X } \\ { D ^ { \prime } = k _ { 2 } B X } \\ { E ^ { \prime } = k _ { 4 } X } \\ { X ^ { \prime } = k _ { 1 } A - k _ { 2 } B X + k _ { 3 } X ^ { 2 } Y - k _ { 4 } X } \\ { Y ^ { \prime } = k _ { 2 } B X - k _ { 3 } X ^ { 2 } Y ~ . } \end{array}
$$

This system is now simplified as follows: the equations for $D$ and $E$ are left out, because they do not influence the others; A and $B$ are supposed to be maintained constant (positive) and all reaction rates $k _ { i }$ are set equal to 1. We further set $X ( x ) = : y _ { 1 } ( x )$ ， $Y \left( x \right) = : y _ { 2 } ( x )$ and obtain

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = A + y _ { 1 } ^ { 2 } y _ { 2 } - ( B + 1 ) y _ { 1 } } } \\ { { \nonumber } } \\ { { y _ { 2 } ^ { \prime } = B y _ { 1 } - y _ { 1 } ^ { 2 } y _ { 2 } . } } \end{array}
$$

The resuiting system has one critical point ${ y _ { 1 } ^ { \prime } } { = } { y _ { 2 } ^ { \prime } } { = } 0$ at ${ \boldsymbol { y } } _ { 1 } = { \boldsymbol { A } }$ ， ${ \boldsymbol { y } } _ { 2 } = { \boldsymbol { B } } / A$ . The linearized equation in the neighbourhood of this point is unstable iff $B > A ^ { 2 } + 1$ . Further, a study of the domains where $y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } ,$ or $( y _ { 1 } + y _ { 2 } ) ^ { \prime }$ is positive or negative leads to the result that all solutions remain bounded. Thus, for $B > A ^ { 2 } + 1$ there must be a limit cycle which, by numerical calculations, is seen to be unique (Figure 16.4).

An interesting phenomenon (Hopf bifurcation) occurs, when B approaches $A ^ { 2 } + 1$ .Then the limit cycle becomes smaller and smaller and finally disappears in the critical point. Another example of this type is given in Exercise 2.

![](images/9deb8d70e2cedfaac4bce222e7a6d7069e51bfbbf50202fa9589052462a18e1a.jpg)  
Figure 16.4. Solutions of the Brusselator, $A = 1 , B = 3$

# Limit cycles in higher dimensions, Hopf bifurcation

The Theorem of Poincaré-Bendixson is apparently true only in two dimensions. Higher dimensional counterexamples are given by nearly every mechanical movement without friction, as for example the spherical pendulum (Figure 16.5)，which has been extensively studied in history, e.g. in Lagrange (1788) (Seconde partie, Section VIII, Chap. II, &I). Its equations of motion become in spherical coordinates

$$
\begin{array} { l } { { \displaystyle \phi ^ { \prime \prime } = - 2 \frac { \cos \psi } { \sin \psi } \cdot \phi ^ { \prime } \cdot \psi ^ { \prime } } } \\ { { \displaystyle \psi ^ { \prime \prime } = \sin \psi \cos \psi \left( \phi ^ { \prime } \right) ^ { 2 } - \sin \psi } } \end{array}
$$

and a solution curve is plotted in Figure 16.5. Whenever the increase of $\Phi / ( 2 \pi )$ for one oscillation is irrational, the solution is not periodic, nor does it tend to a periodic or stationary solution.

![](images/fa992be55ce694b20ec056dc06f5b67987ded5a7f7424605fb722a6983ea3642.jpg)  
Figure 16.5. A solution of the spherical pendulum,a) $0 \leq x \leq 2 0$ ,b) $0 \leq x \leq 1 0 0$

Therefore, in higher dimensions limit cycles are usually found by numerical studies of the Poincare section map $\Phi$ defined above. A periodic solution (i.e. a fixed point of $\Phi$ ) is called an attractor， if all eigenvalues of $\Phi ^ { \prime } ( y _ { 0 } )$ are smaller than 1 in modulus. All solutions starting in a neighbourhood will tend to this attractor.

There is, however, one situation where limit cycles occur quite naturally (Hopf (1942)): namely when at a critical point of $y ^ { \prime } { = } f \left( y \right)$ ， y， $f \in \mathbb { R } ^ { n }$ ， all eigenvalues of $f ^ { \prime } ( y _ { 0 } )$ have strictly negative real part with the exception of one pair which crosses the im aginary axis. The eigenspace of the stable eigenvalues then continues into an analytic two dimensional manifold, inside which a limit cycle appears. This phenomenon is called "Hopf bifurcation". The proof of this fact is similar to Poincare's parameter expansion method (16.7) (see Exercises 6 and 7 below), so that Hopf even hesitated to publish it (". ich glaube kaum， dass an dem obigen Satz etwas wesentlich Neues ist .").

Let us consider for example the "full Brusselator" (16.11): we no longer suppose that $B$ is kept constant, but that $B$ is constantly added to the mixture with rate α. When we set $B \left( x \right) = : y _ { 3 } ( x )$ ， we obtain instead of (16.11') (with $A = 1$ ）

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = 1 + y _ { 1 } ^ { 2 } y _ { 2 } - ( y _ { 3 } + 1 ) y _ { 1 } } } \\ { { \ } } \\ { { y _ { 2 } ^ { \prime } = y _ { 1 } y _ { 3 } - y _ { 1 } ^ { 2 } y _ { 2 } } } \\ { { \ } } \\ { { y _ { 3 } ^ { \prime } = - y _ { 1 } y _ { 3 } + \alpha \mathrm { ~ . ~ } } } \end{array}
$$

This system possesses a critical point at $y _ { 1 } { = } 1$ ， ${ \boldsymbol { y } } _ { 2 } = { \boldsymbol { y } } _ { 3 } = \alpha$ with derivative

$$
\begin{array} { r } { \frac { \partial f } { \partial y } = \left[ \begin{array} { c c c } { \alpha - 1 } & { 1 } & { - 1 } \\ { - \alpha } & { - 1 } & { 1 } \\ { - \alpha } & { 0 } & { - 1 } \end{array} \right] \mathrm { ~ , ~ } } \end{array}
$$

This matrix has the characteristic polynominal $\lambda ^ { 3 } + ( 3 - \alpha ) \lambda ^ { 2 }$ $+ ( 3 - 2 \alpha ) \lambda + 1 = 0$ and satisfies the condition for stability (see I.13, Exercise 1) iff $\alpha < ( 9 - \sqrt { 1 7 } ) / 4 = 1 . 2 1 9 2 2$ . Thus when α increases beyond this value, there arises a limit cycle which exists for all values of α up to approximately 1.5 (See Figure 16.6).

When α continues to grow, the limit cycle "explodes" and $y _ { 1 } \circ \boldsymbol { \mathrm { ~ 0 ~ } }$ while $y _ { 2 }$ and $y _ { 3 } + \infty$ . So the system (16.13) has a completely different behavior from the simplified model (16.11').

A famous chemical reaction with a limit cycle in three dimensions is the "Oregonator" reaction between $H B r O _ { 2 } , B r ^ { - }$ and $C e ( I V )$ (Field and Noyes (1974))

![](images/3321e7622e220a7d2f8e2a9550fa28e545f4fb030fa9aa8203777197c5aa0803.jpg)  
Figure 16.6. Hopf bifurcation for the "full" Brusselator (16.13) $\alpha = 1 . 2 2$ , 1.24, 1.26, 1.28, 1.30 (broken line), 1.34, 1.38, 1.42, 1.46,1.50 (broken line)

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = 7 7 . 2 7 \bigg ( y _ { 2 } + y _ { 1 } ( 1 - 8 . 3 7 5 \times 1 0 ^ { - 6 } y _ { 1 } - y _ { 2 } ) \bigg ) } \\ { y _ { 2 } ^ { \prime } = \frac { 1 } { 7 7 . 2 7 } ( y _ { 3 } - ( 1 + y _ { 1 } ) y _ { 2 } ) } \\ { y _ { 3 } ^ { \prime } = 0 . 1 6 1 ( y _ { 1 } - y _ { 3 } ) } \end{array}
$$

whose solutions are plotted in Figure 16.7. This is an example of a "stif differential equation whose solutions change rapidly over many orders of magnitude. It is thus a challenging example for numerical codes and we shall meet it again in Volume II of our book.

Our next example is taken from the theory of superconducting Josephson junctions, coupled together by a mutual capacitance. The resulting equations are of the form (see e.g. Giovannini-Weiss-Ulrich (1978))

![](images/9796c0fc1d8f23dcd4416492e60916b930dfce41ab7ada7b294cbf4af393cf74.jpg)  
Figure 16.7. Limit cycle of the Oregonator

$$
\begin{array} { l } { { c \left( y _ { 1 } ^ { \prime \prime } - \alpha y _ { 2 } ^ { \prime \prime } \right) = i _ { 1 } - \sin ( y _ { 1 } ) - y _ { 1 } ^ { \prime } } } \\ { { \phantom { c } } } \\ { { c \left( y _ { 2 } ^ { \prime \prime } - \alpha y _ { 1 } ^ { \prime \prime } \right) = i _ { 2 } - \sin ( y _ { 2 } ) - y _ { 2 } ^ { \prime } . } } \end{array}
$$

Here, $y _ { 1 } ,$ and $y _ { 2 }$ are angles (the "quantum phase difference across the junction") which are thus identified modulo $2 \pi$ . Equation (16.16) is thus a system on the torus $T ^ { 2 }$ for $( y _ { 1 } , y _ { 2 } )$ ,and on $\mathbb { R } ^ { 2 }$ for the voltages $( y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } )$ . It is seen by numerical computations that the system (16.16) possesses an attracting limit cycle, which describes the phenomenon of "phase locking" (see Figure 16.8.).

![](images/0fb63afce0441a8f252efe6faddcfe04631e8099ce48c83a8e54147fdff1e85c.jpg)  
Figure 16.8. Josephson junctions (16.16) for $c = 2$ ， $\alpha = 0 . 5$ ， $i _ { 1 } { = } 1 . 1 1$ ， $i _ { 2 } { = } 1 . 0 8$

# Strange attractors

"Mr. Dahlquist, when is the spring coming?" "Tomorrow, at two o'clock." (Weather forecast, Stockholm 1955) "We were so nalve..." (H.O. Kreiss, Stockholm 1985).

Concerning the discovery of the famous "Lorenz model", we best quote from Lorenz (1979):

"By the middle $1 9 5 0 ^ { \circ } { \bf s }$ "numerical weather prediction", i.e., forecasting by numerically integrating such approximations to the atmospheric equations as could feasibly be handled, was very much in vogue, despite the rather mediocre results which it was then yielding. A smaller but determined group favored statistical prediction (...) apparently because of a misinterpretation of a paper by Wiener (..). I was skeptical, and decided to test the idea by applying the statistical method to a set of artificial data, generated by solving a system of equations numerically (..). The first task was to find a suitable system of equations to solve (..). The system would have to be simple enough (... and) the general solution would have to be aperiodic, since the statistical prediction of a periodic series would be a trivial matter, once the periodicity had been detected. It was not obvious that these conditions could be met. (..) The break came when I was visiting Dr. Barry Saltzman, now at Yale University. In the course of our talks he showed me some work on thermal convection, in which he used a system of seven ordinary differential equations. Most of his numerical solutions soon acquired periodic behavior, but one solution refused to settle down. Moreover, in this solution four of the variables appeared to approach zero. Presumably the equations governing the remaining three variables, with the terms containing the four variables eliminated, would also possess aperiodic solutions. Upon my return I put the three equations on our computer, and confirmed the aperiodicity which Saltzman had noted. We were finally in business."

In a changed notation， the three equations with aperiodic solu-tions are

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = - \sigma y _ { 1 } + \sigma y _ { 2 } } } \\ { { \ } } \\ { { y _ { 2 } ^ { \prime } = - y _ { 1 } y _ { 3 } + { p _ { 1 } } - y _ { 2 } } } \\ { { \ } } \\ { { y _ { 3 } ^ { \prime } = y _ { 1 } y _ { 2 } - b y _ { 3 } } } \end{array}
$$

where $\sigma , r$ and $b$ are positive constants. Denote by $\boldsymbol \Phi _ { x } : \mathbb { R } ^ { 3 } \to \ \mathbb { R } ^ { 3 }$ the map

$$
\phi _ { x } ( y _ { 0 } ) = y ( x , 0 , y _ { 0 } ) ~ ,
$$

the flow of the diffrential equation. Since (16.17) is autonomous, there is no restriction in choosing $x _ { 0 } { = } 0$ and (14.13) becomes

$$
\begin{array} { r } { \Phi _ { x _ { 1 } + x _ { 2 } } = \Phi _ { x _ { 1 } } \circ \Phi _ { x _ { 2 } } . } \end{array}
$$

It follows from (16.17) that

$$
\begin{array} { r l r } {  { \frac { 1 } { 2 } \frac { d } { d x } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + ( y _ { 3 } - \sigma - r ) ^ { 2 } ) } } & { { \mathrm { ( 1 6 ~ } } } \\ & { } & { \quad \quad \quad = - ( \sigma y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + b ( y _ { 3 } - \frac { \sigma } { 2 } - \frac { r } { 2 } ) ^ { 2 } ) + b ( \frac { \sigma } { 2 } + \frac { r } { 2 } ) ^ { 2 } . } \end{array}
$$

Therefore the ball

$$
R _ { 0 } = \left\{ ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) \mid y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + \left( y _ { 3 } - \sigma - r \right) ^ { 2 } \leq \ c ^ { 2 } \right\}
$$

is mapped by the flow $\Phi _ { 1 }$ into itself, provided that $c$ is sufficiently large so that $\boldsymbol { R } _ { 0 }$ wholly contains the ellipsoid defined by equating the right side of (16.20) to zero. Hence, if $x$ assumes the increasing values 1,2, $3 , \ldots , R _ { 0 }$ is carried into regions ${ R _ { 1 } } ^ { = } \Phi _ { 1 } ( { R _ { 0 } } )$ ， $\scriptstyle R _ { 2 } = \Phi _ { 2 } ( R _ { 0 } )$ $\mathbf { \Phi } = \Phi _ { 1 } ( R _ { 1 } )$ (by (16.19)) etc., which satisfy $R _ { 0 } { \supset } R _ { 1 } { \supset } R _ { 2 } { \supset } R _ { 3 } { \supset } R _ { 4 }$

The volume $V _ { k }$ of $\kappa _ { k }$

$$
\begin{array} { r } { V _ { k } ^ { } ~ = \int ^ { } ~ | ^ { } ~ \operatorname* { d e t } \left( \frac { \partial y } { \partial y _ { 0 } } ( k { } ~ , 0 { } , y _ { 0 } ^ { } ) \right) ~ | ^ { } ~ d y _ { 0 } ^ { } ~ , } \\ { R _ { 0 } ^ { } ~ } \end{array}
$$

tends to zero exponentially for $k  \infty$ . This is seen by applying the Abel-Jacobi identity (11.10) to the variational equation (14.15). The

trace of $\partial f / \partial y$ for the system (16.17) is the constant $- ( \sigma + b + 1 )$ and we have

$$
V _ { k } \ = \ e ^ { - k ( \sigma + b + 1 ) } V _ { 0 } \ .
$$

Every orbit is thus ultimately trapped in a set $R _ { \infty } = R _ { 0 } \cap R _ { 1 } \cap R _ { 2 } \cdot \cdot \cdot$ of zero volume.

System (16.17) possesses an obvious critical point ${ y _ { 1 } } ^ { = } { y _ { 2 } } ^ { = } { y _ { 3 } } ^ { = } { 0 }$ ； this becomes unstable when $r > 1$ . In this case there are two additional critical points $c$ and $C ^ { \prime }$ respectively given by

$$
y _ { 1 } = y _ { 2 } = \pm { \sqrt { b \left( r - 1 \right) } } , y _ { 3 } = r - 1 .
$$

These become unstable (e.g. by the Routh criterion, Exercise 1 of Section I.13) when $\sigma > b + 1$ and

$$
r \ge r _ { c } = \frac { \sigma \left( \sigma + b + 3 \right) } { \sigma - b - 1 } \ .
$$

In the first example we shall use Saltzman's values $b = 8 / 3$ ， $\sigma = 1 0$ , and $r = 2 8$ . (Here we note another lucky break: Saltzman used $\sigma = 1 0$ as a crude approximation to the Prandtl number (about 6) for water. Had he chosen to study air, he would probably have let $\sigma = \updownarrow$ , and the aperiodicity would not have been discovered", Lorenz (1979)). In Figure 16.9 we have plotted the solution curve of (16.17) with the initial value ${ y _ { 1 } } ^ { = - 8 }$ ， $y _ { 2 } = 8$ ， $y _ { 3 } { = } r { - } 1$ ，which， indeed， looks pretty chaotic.

![](images/f830fa39d5d29110a4e87619cff284c4fb6decf16d80cbd17383e18acafad442.jpg)  
Figure 16.9. Two views of a solution of (16.17)

In order to understand more clearly what’s going on, we observe that every solution which starts in the plane ${ { y } _ { 3 } } ^ { = { r - 1 } }$ between the two critical points, surrounds one of these two points and comes back from behind. We therefore choose this plane $\Pi$ as Poincare section $P : \Pi  \Pi$ . A numerical study of this map shows that there is a critical line, above which the solutions go right, and below which they go left. Therefore the image $P$ (II) consists of two sets as shown in Figure 16.10. It follows that the image of $P ^ { 2 }$ is formed by 4 slices, that of $P ^ { 3 }$ by 8 slices closer and closer together, and so on. The attractor set is thus formed of an infinity of sheets arranged like the points of the Cantor set. Such attractors are now called strange attractors ("An attractor of the type just described can therefore not be thrown away as non-generic pathology", Ruelle-Takens (1971)).

![](images/b52ef991f894c0f44ba41c15fdf62b614d384052fa10762065445063d4867a93.jpg)  
Figure 16.10. Poincare map for (16.17)

# Feigenbaum Cascades

As nicely as the paper of Lorenz (1979) is written in its beginning, the affirmations of his last section are only partly true. As Lorenz did, we now vary the parameter $^ b$ in (16.17), letting at the same time $r = r _ { c }$ (see (16.21)) and

$$
\sigma = b + 1 + \sqrt { 2 ( b + 1 ) ( b + 2 ) } .
$$

This is the value of $\sigma$ for which $r _ { c }$ is minimized. Numerical integration shows that for $^ { b }$ very small (say $b \le 0 . 1 3 9$ )， the solutions of (16.17) evidently converge to a stable limit cycle, which cuts the Poincare section $y _ { 3 } { = } r { - } 1$ twice at two different locations and surrounds both of the critical points $C$ and $C ^ { \prime } .$ Further, for $^ b$ large (for example $b = 8 / 3$ ） the coefficients are not far from those studied above and we have a strange attractor. But what happens in between? We have computed the solutions of the Lorenz model (16.17) for $^ b$ varying from 0.138 to 0.148 with 687 intermediate values. For each of these values, we have computed 80o Poincaré cuts and represented in Figure 16.11 the $y _ { 1 }$ -values of the intersections with the Poincare plane $y _ { 3 } { = } r { - } 1$ . Thereby, after each change of $^ b$ , the first 40 iterations were not drawn so that only the attractor becomes visible.

![](images/57bf5ec1ce014d05d00b44afca14f998c7331ec814f21a3d78604f34f88e3632.jpg)  
Figure 16.11. Poincare cuts $y _ { 1 }$ for (16.17) as function of $^ b$

For $^ b$ small, there is one periodic orbit; then, at $b = \boldsymbol { b } _ { 1 } = 0 . 1 3 9 7$ it suddenly splits into an orbit of period two, this then splits for $b = b _ { 2 } = 0 . 1 4 3 3$ into an orbit of period four, then eight, etc. There is a point $b _ { \infty }$ after which the movement becomes chaotic. Beyond this value, however, there are again and again intervals of stable attractors of periods 5, 3,.. etc. The whole picture resembles what is obtained by the recursion

$$
x _ { n + 1 } = a ( x _ { n } - x _ { n } ^ { 2 } )
$$

which is discussed in many papers (e.g. May (1976)， Feigenbaum (1978), Collet-Eckmann (1980)).

But where does this resemblance come from? We study in Figure 16.12 the Poincare map for the system (16.17) with $^ b$ chosen as 0.146 and choose the ellipse

$$
\begin{array} { c } { { y _ { 1 } = - 0 . 0 8 4 + ( u - \nu ) { \cdot } 0 . 7 0 7 1 \ , } } \\ { { { } } } \\ { { y _ { 2 } = - 0 . 0 7 7 + ( u + \nu ) { \cdot } 0 . 7 0 7 1 } } \end{array}
$$

u =0.012 cosΦ, $\nu = 0 . 0 0 1 5$ sinΦ, $0 \leq \phi \leq 2 \pi$ . What happens to this ellipse after one iteration? It is compressed to a thin line, bent to Ushape and mapped into itself.

![](images/efb16416110fe52c8ea5e42e3be16c5932543c459722d8b687f0120bc682fe13.jpg)  
Figure 16.12. Poincare map of the ellipse (16.24)

Therefore, the Poincare map is essentially a map of the interval [0,1] to itself similar to (16.23). It is a great discovery of Feigenbaum that for all maps of a similar shape, the phenomena are always the same, in particular that

$$
\operatorname * { l i m } _ { i \to \infty } { \frac { b _ { i } - b _ { i - 1 } } { b _ { i + 1 } - b _ { i } } } = 4 . 6 6 9 2 0 1 6 0 9 1 0 2 9 9 0 6 7 1 5 . . .
$$