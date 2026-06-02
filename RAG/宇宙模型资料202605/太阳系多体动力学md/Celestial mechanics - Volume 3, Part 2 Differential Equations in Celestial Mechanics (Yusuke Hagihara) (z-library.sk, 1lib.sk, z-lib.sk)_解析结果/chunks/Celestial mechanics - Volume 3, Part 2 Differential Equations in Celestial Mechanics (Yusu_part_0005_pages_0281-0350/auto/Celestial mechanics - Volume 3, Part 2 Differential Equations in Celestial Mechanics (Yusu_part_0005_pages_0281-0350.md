$$
\left| \zeta _ { 0 } - \frac { P } { Q } \right| < \frac { 1 } { 2 Q ^ { 2 } } ,
$$

then $P / Q$ is equal to a reduced fraction of a regular continued fraction

$$
\zeta _ { \scriptscriptstyle 0 } = [ b _ { \scriptscriptstyle 0 } , b _ { \scriptscriptstyle 1 } , b _ { \scriptscriptstyle 2 } , . . . ] .
$$

A Liouville number should satisfy

$$
\left| \zeta _ { 0 } - \frac { A _ { n } } { B _ { n } } \right| < \frac { 1 } { B _ { n } ^ { \lambda - 2 } }
$$

for any large integer λ. A number $\zeta _ { 0 }$ defined by

$$
\zeta _ { 0 } = [ b _ { 0 } , b _ { 1 } , b _ { 2 } , \ldots , b _ { n } , b _ { n + 1 } ]
$$

satisfies

$$
\zeta _ { 0 } - \frac { A _ { n } } { B _ { n } } = \frac { ( - 1 ) ^ { n } } { B _ { n } ( B _ { n } \zeta _ { n + 1 } + B _ { n - 1 } ) } .
$$

Hence

$$
B _ { n } \zeta _ { n + 1 } + B _ { n - 1 } > B _ { n } ^ { \scriptscriptstyle \lambda + 1 } .
$$

Since

$$
b _ { n + 1 } < \zeta _ { n + 1 } < b _ { n + 1 } + 1 ,
$$

this inequality holds when and only when $\lambda$ satisfies $b _ { n + 1 } > B _ { n } ^ { \lambda }$ . Hence a regular continued fraction $[ b _ { 0 } , b _ { 1 } , b _ { 2 } , \dots ]$ with the reduced fraction $A _ { n } / B _ { n }$ represents a Liouville number when and only when there exists an index $_ n$ satisfying $b _ { n + 1 } > B _ { n } ^ { \ i }$ for any large integer λ (Perron, 1921). If $\xi$ is an algebraic number different from zero,then its reciprocal $\eta$ is also an algebraic number.If there is a relation

$$
\eta = r _ { 0 } + r _ { 1 } \xi + r _ { 2 } \xi ^ { 2 } + \cdot \cdot \cdot + r _ { m } \xi ^ { m }
$$

with rational coefficients $r _ { n }$ between two irrational numbers $\xi$ and $\eta$ ， then $\eta$ is an algebraic number different from zero in the same way as $\xi$ .A similar situation exists if $\eta$ is an irrational number defined by

$$
\eta = \frac { p _ { 0 } + p _ { 1 } \xi + \cdot \cdot \cdot + p _ { m } \xi ^ { m } } { q _ { 0 } + q _ { 1 } \xi + \cdot \cdot \cdot + q _ { m } \xi ^ { m } }
$$

with rational numbers $p _ { 0 } , p _ { 1 } , \ldots , p _ { m } ; q _ { 0 } , q _ { 1 } , \ldots , q _ { m }$

An important question to be referred to later is the distribution of the rational fractions $p / q$ defined by the Diophantine inequality

$$
\left| x - { \frac { p } { q } } \right| < { \frac { C } { q ^ { 2 } } } , \qquad C > 0 .
$$

The approximation of an irrational number by rational fractions is .called Diophantine approximation.It is shown that if the irrational .number $x$ is fixed then exists at least a rational number $p / q$ satisfying this inequality and that the Lebesgue measure of points $p / q$ satisfying this inequality is zero (Koksma,1936).A Liouville's number is a :special case of this.In particular,Thue-Siegel's theorem states that if $_ x$ is a root of an rth degree algebraic equation then there exist at most a finite number of rational fractions $p / q$ such that

$$
| q x - p | < \frac { C } { q ^ { r / 2 + k } } , \qquad C > 0 ,
$$

with a positive integer $k > 1$ (Skolem, 1938; Osgood,1972).

# BRUNS'S PROOF OF NONUNIFORM CONVERGENCE

# 15.4BRUNS's PROOF

We have seen that the expansions in perturbation theory are of the form

$$
F = \sum { A _ { i _ { 1 } i _ { 2 } \cdots i _ { r } } \cos { ( i _ { 1 } l _ { 1 } + i _ { 2 } l _ { 2 } + \cdots + i _ { r } l _ { r } ) } } ,
$$

$$
l _ { j } = n _ { j } t + \varepsilon _ { j } \qquad ( j = 1 , 2 , . . . , r ) .
$$

In the integration of the equations by the method of the variation of elements,divisors of the form $i _ { 1 } n _ { 1 } + i _ { 2 } n _ { 2 } + \cdots + i _ { r } n _ { r }$ appear，and, for certain sets of values of $n _ { 1 } , n _ { 2 } , \ldots , n _ { r }$ distributed densely in the domain of $n _ { j }$ ， the series obtained by term-by-term integration of the differential equations may become divergent. It was Bruns (1884) who discussed the divergence in a very ingenious manner. Bruns took a simpler case

$$
\sum _ { m , n } { \frac { p ^ { m } q ^ { n } } { m - n A } } \qquad ( m , n = 1 , 2 , \ldots , \infty ) ,
$$

where $p$ and $q$ are pure fractions and $\pmb { A }$ is a positive irrational number. Let $\pmb { A }$ be an algebraic number satisfying an irreducibe algebraic equation

$$
A ^ { s } + G _ { 1 } A ^ { s - 1 } + \cdot \cdot \cdot + G _ { s } = 0
$$

with integer coefficients $G _ { i }$ . Multiply the numerator and the denominator of this fraction (1) by the product

$$
( m - n A ^ { \prime } ) ( m - n A ^ { \prime \prime } ) \cdot \cdot \cdot ( m - n A ^ { ( s - 1 ) } )
$$

of linear factors formed of the remaining $s - 1$ roots of this algebraic equation. Then the denominator becomes a rational function of m and $\pmb { n }$ with integer coefficients. Since $\pmb { A }$ is irrational, the denominator is never equal to zero but at least equal to 1； while the numerator is a rational function of $m$ and $_ n$ of degree $s - 1$ .Hence the series is convergent.

In order to see if the series (1） is divergent for other irrational numbers,Bruns considered a representation of an irrational number. Take rositive pure fractions $\theta$ and $\eta$ such that

$$
0 \leq \theta < \frac { 1 } { 2 } , \qquad 0 \leq \eta \leq \frac { 1 } { 2 } ,
$$

and let $\varepsilon$ be $+ 1$ or $^ { - 1 }$ ，and $0 < A < \frac { 1 } { 2 }$ . Define a set of positive integers $h _ { \alpha }$ according to the algorithm

$$
\begin{array} { r l } & { A = \cfrac { 1 } { h _ { 1 } - \varepsilon _ { 1 } \eta _ { 1 } } , \quad \quad h _ { 1 } A - 1 = \cfrac { \varepsilon _ { 1 } \eta _ { 1 } } { h _ { 1 } - \varepsilon _ { 1 } \eta _ { 1 } } = \varepsilon _ { 1 } \theta _ { 2 } , } \\ & { } \\ & { \theta _ { 2 } = \cfrac { 1 } { h _ { 2 } - \varepsilon _ { 2 } \eta _ { 2 } } , \quad \quad h _ { 2 } A - 1 = \cfrac { \varepsilon _ { 2 } \eta _ { 2 } } { h _ { 2 } - \varepsilon _ { 2 } \eta _ { 2 } } = \varepsilon _ { 2 } \theta _ { 3 } , } \\ & { } \\ & { \theta _ { 3 } = \cfrac { 1 } { h _ { 3 } - \varepsilon _ { 3 } \eta _ { 3 } } , \quad \quad \cdot \cdot , } \\ & { \cdot \cdot . . } \end{array}
$$

Then the number $\pmb { A }$ can be represented by

$$
\begin{array} { r } { A = \frac { 1 } { h _ { 1 } } + \frac { \varepsilon _ { 1 } } { h _ { 1 } h _ { 2 } } + \frac { \varepsilon _ { 1 } \varepsilon _ { 2 } } { h _ { 1 } h _ { 2 } h _ { 3 } } + \cdots . } \end{array}
$$

This representation converges rapidly, since $h$ increases with its index according to the relation

$$
h _ { \alpha + 1 } \geq 2 h _ { \alpha } - 1 .
$$

If the series ends at a certain term, then $\pmb { A }$ is a rational number. If $\pmb { A }$ is rational, then the series does not extend to an infinite number of terms.Put

$$
\begin{array} { r } { h _ { 1 } h _ { 2 } \cdot \cdot \cdot \ h _ { \alpha } = H _ { \alpha } , \qquad \varepsilon _ { 1 } \varepsilon _ { 2 } \cdot \cdot \cdot \ \varepsilon _ { \alpha } = E _ { \alpha } ; } \end{array}
$$

then

$$
m = H _ { \alpha } \Big [ \frac { 1 } { H _ { 1 } } + \frac { E _ { 1 } } { H _ { 2 } } + \cdot \cdot \cdot + \frac { E _ { \alpha - 1 } } { H _ { \alpha } } \Big ] , \qquad n = H _ { \alpha } ,
$$

are two positive integers for which the divisor $m - n A$ takes the form

$$
- \frac { E _ { \alpha } } { h _ { \alpha + 1 } } - \frac { E _ { \alpha + 1 } } { h _ { \alpha + 1 } h _ { \alpha + 2 } } - \cdot \cdot \cdot .
$$

Hence the corresponding term of (1) is $h _ { \alpha + 1 } p ^ { m } q ^ { n }$ except for a numerical factor nearly equal to $\pm 1$ . This term increases indefinitely for fixed $p$ and $\pmb q$ with increasing values of $\alpha$ ，if the irrational number $\pmb { A }$ is taken in the following manner: Choose an integer $h$ arbitrarily up to a certain definite index $_ { \alpha }$ under the restriction (2),but choose the following $h _ { \alpha + 1 }$ so that

$$
\log h _ { \alpha + 1 } > \left( { \frac { H _ { \alpha } } { H _ { 1 } } } + { \frac { E _ { 1 } H _ { \alpha } } { H _ { 2 } } } + \cdots + E _ { \alpha - 1 } + 1 \right) \log \alpha .
$$

Thus there are arbitrarily many such irrational numbers, for which the series (1) is divergent, in any small interval of real numbers.

In a similar manner it can be shown that, in the general case of the $\pmb { n }$ of the diviser $i _ { 1 } n _ { 1 } + i _ { 2 } n _ { 2 } + \cdots + i _ { r } n _ { r }$ a set of values of $n _ { 1 } , n _ { 2 } , \ldots ,$ $n _ { r }$ can be found that are distributed everywhere densely in the domain of $_ n$ and for which the corresponding series is divergent.

In general perturbation theory, the constants $_ n$ are analytic functions of the integration constants.Even when these constants are not independent,we can assign to $_ n$ by choosing suitable integration constants such values that the corresponding divisor makes the corresponding series (1） divergent.Hence,in order that the trigonometric series in question may be useful in practice,we must restrict the domain of the integration constants. This is because the coordinates are analytic functions not only of time but also of the integration constants.

Charlier (1907) gave some examples.For $A = 1 / \sqrt { 5 }$ the series is convergent. If we expand $\pmb { A }$ in Bruns's algorithm we obtain $h _ { 1 } = 2$ ， $h _ { 2 } = 9 , h _ { 3 } = 2 0 , h _ { 4 } = 2 2 7 , h _ { 5 } = 8 3 3 , . . .$ . If we take, instead, $h _ { 5 } =$ $4 ^ { 4 5 1 7 4 }$ ， then the series is divergent.This irrational number differs from $1 / \sqrt { 5 }$ by a quantity less than $1 / 6 8 0 0 0 0 0 0 0 .$

# 15.5THE QUESTION OF GYLDEN'S PROBABILITY THEOREM

Gyldén (1888, 1888a) tried to prove that, although convergencepoints and divergence-points are densely distributed everywhere, the probability of divergence is infinitely small. The reasoning was based on a mathematical theorem on probability due to Gyldén himself.

Let $\nu$ be a given irrational number between O and 1,which can be represented uniquely by a regular continued fraction ${ \boldsymbol \nu } = [ a _ { 1 } , a _ { 2 } , a _ { 3 } , \ldots ] .$ where $a _ { 1 } , a _ { 2 } , a _ { 3 } , \ldots$ are positive. Since $\nu$ takes an arbitrary value between O and 1,all partial intervals of equal length contained between O and 1 can be considered to be equally likely； that is,if $\nu _ { 1 }$ and $\nu _ { 2 }$ have arbitrary values between O and 1, then the probability that $\pmb { \nu }$ lies between $\nu _ { 1 }$ and $\nu _ { 1 } + \delta \nu _ { 1 }$ is equal to the probability that $\nu$ lies between $\nu _ { 2 }$ and $\nu _ { 2 } + \delta \nu _ { 2 }$ ，where $\delta \nu _ { 1 } = \delta \nu _ { 2 }$ . If the numbers $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ of the continued fraction are given，what is the probability $\pmb { F } _ { \pmb { n } \mathscr { k } }$ that the number $a _ { n + 1 }$ immediately following takes the value $k$ ， and what is the probability $W _ { n k }$ that $a _ { n + 1 } \geq k ?$

We start with a simpler example.Let there be a relation

$$
y = { \frac { 1 } { 1 + ( 1 / x ) } }
$$

between $x$ and $y$ . Suppose that $_ x$ can take all real values between I and $\infty$ and that $y$ can take any value between $1 / 2$ and 1 with equaI probability.What is the probability that $x$ lies between 1 and 3? We know that $y$ increases continuously with $_ x$ .For $x = 0$ we have $y =$ 1/2. For $x = 3$ we have $y = 3 / 4$ . By our supposition,a value of $y$ between $1 / 2$ and $3 / 4$ is as equally probable as a value of $\mathfrak { y }$ between $3 / 4$ and 1.Hence the probability that $x$ lies between 1 and 3 is $1 / 2$

Now let us return to Gyldén's problem. Denote the reduced fraction of the continued fraction by

$$
[ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ] = { \frac { r _ { n } } { s _ { n } } } ,
$$

then we have the known relations

$$
\begin{array} { c } { { r _ { n + 1 } = a _ { n + 1 } r _ { n } + r _ { n - 1 } , \qquad s _ { n + 1 } = a _ { n + 1 } s _ { n } + s _ { n - 1 } , } } \\ { { \frac { r _ { n + 1 } } { s _ { n + 1 } } - \frac { r _ { n } } { s _ { n } } = \frac { ( - 1 ) ^ { n } } { s _ { n } s _ { n + 1 } } , } } \end{array}
$$

where $r _ { 1 } = 1 , \ r _ { 2 } = a _ { 2 } , \ s _ { 1 } = a _ { 1 } , \ s _ { 2 } = a _ { 1 } a _ { 2 } + 1$ ．The probability in question has been calculated by Brodén.

Let $\pmb { n }$ be a definite number, and assign definite values for the numbers $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ but not for the numbers $a _ { n + 1 } , a _ { n + 2 } , \ldots .$ Then the possible values of the continued fraction between $[ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ]$ and $[ a _ { 1 } , a _ { 2 } ,$ $\ldots , a _ { n } , 1 ]$ are obtained.The first or the second of these limiting numbers is the smaller according as $_ n$ is even or odd.Hence ${ \pmb \nu }$ is limited in an interval of length

$$
l _ { n 1 } = ( - 1 ) ^ { n } \{ [ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } , 1 ] - [ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ] \} .
$$

From the relations (4) we obtain

$$
l _ { n 1 } = { \frac { 1 } { s _ { n } s _ { n + 1 } } } = { \frac { 1 } { s _ { n } ( s _ { n } + s _ { n - 1 } ) } } .
$$

Let $k$ be an integer $\geq 1$ .If $a _ { n + 1 } \geq k$ and $a _ { n + 2 } , a _ { n + 3 } , \ldots$ take on arbitrary values ； then the corresponding value of $\pmb { \nu }$ falls in the interval

$$
l _ { n k } = ( - 1 ) ^ { n } \{ [ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } , k ] - [ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ] \} ,
$$

which according to (4) is of length

$$
l _ { n k } = \frac { 1 } { s _ { n } ( k s _ { n } + s _ { n - 1 } ) } .
$$

The probability that $a _ { n + 1 } \geq k$ for given values of $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ is expressed by the ratio of $l _ { n k }$ and $l _ { n 1 }$ . Put

$$
\begin{array} { r } { q _ { n } = \frac { S _ { n - 1 } } { S _ { n } } , } \end{array}
$$

then this probability $W ( q _ { n } , k )$ is equal to

$$
W ( q _ { n } , k ) = \frac { 1 + a _ { n } } { k + q _ { n } } .
$$

The greater $k$ is,the smaller is the probability that $a _ { n + 1 } \geq k$ This probability depends on $q _ { n }$ .But $q _ { n }$ is always less than unity because of (4).Hence $W$ must be limited to the interval

$$
{ \frac { 1 } { \bar { k } } } < W < { \frac { 2 } { \bar { k } + 1 } } .
$$

Hence the probability $\pmb { W }$ that an arbitrary partial denominator $a _ { n }$ of the continued fraction is larger than $\pmb { k }$ ， irrespective of the values of the other partial denominators,is always less than $2 / k$ Thisis Gyldén's theorem as was modified by Brodén (1900).

From the expression for $W ( q _ { n } , k )$ just obtained we can derive the probability $F ( q _ { n } , k )$ that $a _ { n + 1 }$ has exactly the value $\boldsymbol { k }$ for given values of $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ ：

$$
\begin{array} { c l c r } { { F ( q _ { n } , k ) = \displaystyle \frac { l _ { n , k } - l _ { n , k + 1 } } { l _ { n , 1 } } = W ( q _ { n } , k ) - W ( q _ { n } , k + 1 ) } } \\ { { } } \\ { { = \displaystyle \frac { 1 + q _ { n } } { ( k + q _ { n } ) ( k + 1 + q _ { n } ) } . } } \end{array}
$$

We see from this relation that for a sufficiently large value of $\pmb { k }$ the probability $\pmb { F }$ is always less than $2 / k ^ { 2 }$ for arbitrary values of $a _ { 1 } , a _ { 2 }$ $\ldots , a _ { n }$

Brodén (1900) denoted by $D _ { n k }$ the probability that $a _ { n + 1 } = k$ by $\pmb { S } _ { \pmb { \pi } \pmb { k } }$ the probability that $a _ { n + 1 } \geq k$ ，and by $\delta _ { n \kappa }$ the probability that one, say $a _ { i }$ ，of the $\pmb { n }$ numbers $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ is $a _ { i } = k$ ， an arbitrarily given number, and by ${ \pmb { \sigma } } _ { \pmb { \mathscr { n } } \pmb { k } }$ the probability that such an $a _ { i } \geq k$ .He obtained $D _ { n k }$ and $S _ { n k }$ approximately as follows.Let the value of the continued fraction with $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ be $\pmb { A } _ { n }$ .If $q _ { n }$ is given，then the possible values of $| \nu - A | \cdot s _ { n } ( s _ { n } + s _ { n - 1 } )$ are distributed uniformly in the interval between O and 1. Hence a possible value of this expression is $1 / 2$ . Since

$$
\begin{array} { r l } & { | \nu - A _ { n } | = \frac { 1 } { s _ { n } s _ { n + 1 } } - \frac { 1 } { s _ { n + 1 } s _ { n + 2 } } + \frac { 1 } { s _ { n + 2 } s _ { n + 3 } } - \cdot \cdot \cdot } \\ & { \qquad = \frac { 1 } { s _ { n } s _ { n + 1 } } ( 1 - q _ { n + 1 } q _ { n + 2 } + q _ { n + 1 } q _ { n + 2 } ^ { 2 } q _ { n + 3 } } \\ & { \qquad - q _ { n + 1 } q _ { n + 2 } ^ { 2 } q _ { n + 3 } ^ { 2 } q _ { n + 4 } + \cdot \cdot \cdot ) , } \end{array}
$$

the probable value of

$$
( 1 + q _ { n } ) ( q _ { n + 1 } - q _ { n + 1 } ^ { \ast } q _ { n + 2 } + q _ { n + 1 } ^ { \ast } q _ { n + 2 } ^ { \ast } q _ { n + 3 } - \cdot \cdot \cdot )
$$

for a given value of $q _ { n }$ is equal to $1 / 2$ .The probable value of (5) for a given value of $q _ { n }$ and for a given value of $_ n$ is equal to the probable value of (5) for a given value of $_ n$ . This probable value is not equal to the product of the probable values of the two factors in (5). This is because these factors are not mutually independent, i.e., the fixing of a definite value of $q _ { n }$ affects the probability ratio in $q _ { n + 1 }$ ,etc. Also, the probable value of the second factor of (5) is not equal to the series obtained by replacing $q _ { n + 1 } , q _ { n + 2 } , \ldots$ by the corresponding probable values. However,for large values of $_ n$ this mutual dependence of $q _ { n + i }$ is not so effective. Thus the probable value of $q _ { n + i } ^ { 2 }$ may differ very little from the square of the probable value of $q _ { n + i }$ This suggests a way to calculate the probable value approximately.

The exact determination of the probable value of $q _ { n + i }$ is very complicated.But the probable value of $q _ { i }$ can be seen to tend to a definite number $q$ as $_ i$ increases indefinitely.Hence the value $q$ may be used as an approximation. The probable value of $q _ { n + i }$ is equal to $q + \delta _ { n + i }$ where $\begin{array} { r } { \operatorname* { l i m } _ { i  \infty } \delta _ { n + i } = 0 } \end{array}$ independently of $_ n$ ，and where $| \delta _ { n + i } |$ may be taken to be arbitrarily small independently of $_ i$ for a sufficiently large value of $\pmb { n }$ . Substituting in the expression (5） the probable values of $q _ { n } , q _ { n + 1 } , \ldots$ ，which are all equal to $1 / 2$ ， we obtain

$$
( 1 - q ^ { 2 } + q ^ { 4 } - q ^ { 6 } + \cdots ) + \Delta _ { n } = { \frac { 1 } { 2 ( q + \delta _ { n + i } ) ( 1 + q + \delta _ { n } ) } } ,
$$

where

$$
\operatorname* { l i m } _ { n \to \infty } \Delta _ { n } = 0 .
$$

Since a similar situation occurs for $\delta _ { n }$ and $\delta _ { n + 1 }$ we have

$$
2 q ( 1 + q ) = 1 + q ^ { 2 } ,
$$

or

$$
q = { \sqrt { 2 } } - 1 .
$$

This is merely an approximation.

Since $S _ { n k }$ is the probable value of $W ( q _ { n } , k )$ for a given value of $_ n$ ,the probability $S _ { n k }$ is equal to the probable value of $( 1 + q _ { n } ) / ( k + q _ { n } )$ ，or

$$
\frac { 1 + q _ { n } } { k } \Big [ 1 - \frac { q _ { n } } { k } + \Big ( \frac { q _ { n } } { k } \Big ) ^ { 2 } - \Big ( \frac { q _ { n } } { k } \Big ) ^ { 3 } + \cdots \Big ] .
$$

Substituting the probable value of $q _ { n }$ we obtain an approximation to $S _ { n k }$ . Further,by taking the limiting value $q$ in place of $q _ { n }$ ， we find

$$
\operatorname* { l i m } _ { n  \infty } S _ { n k } = S _ { k } = \frac { 1 + q } { k + q } = \frac { \sqrt { 2 } } { k - 1 + \sqrt { 2 } } = \frac { 1 . 4 1 4 2 } { k + 0 . 4 1 4 2 } .
$$

We have

$$
D _ { n k } = S _ { n , k } - S _ { n , k + 1 } ,
$$

$$
\operatorname* { l i m } _ { n  \infty } D _ { n k } = D _ { k } = S _ { k } - D _ { k + 1 } .
$$

This is also an approximation. For example,

$$
\begin{array} { l } { { S _ { 0 k } = \displaystyle \frac { 1 } { k } , } } \\ { { S _ { 1 k } = \displaystyle \sum _ { i = 1 } ^ { \infty } \left( \displaystyle \frac { 1 } { i } - \displaystyle \frac { 1 } { i + ( 1 / k ) } \right) = \displaystyle \sum _ { i = 1 } ^ { \infty } \displaystyle \frac { 1 } { i ( k i + 1 ) } . } } \end{array}
$$

For a large value of $k$ we obtain approximately

$$
\frac { 1 . 6 4 4 9 3 4 } { k } - \frac { 1 . 2 0 2 0 4 6 } { k ^ { 2 } } + \frac { 1 . 0 8 2 3 2 } { k ^ { 3 } } - \frac { 1 . 0 3 6 9 3 } { k ^ { 4 } } + \frac { 1 . 0 1 7 1 } { k ^ { 5 } } - \cdot
$$

For a small value of $k$ we find

$$
{ \cal S } _ { 1 k } = 1 + \sum _ { n = 1 } ^ { ( k - 1 ) / 2 } \biggl [ 2 - 2 \sin ^ { 2 } \frac { n \pi } { k } \log \Big ( 4 \sin ^ { 2 } \frac { n \pi } { k } \Big ) - \pi \Big ( 1 - \frac { 2 n } { k } \Big ) \sin ^ { 2 } \frac { n \pi } { k } \biggr ] .
$$

(k odd),

$$
\begin{array} { r } { \mathsf { S } _ { \mathrm { 1 } k } = 1 - 2 \log 2 + \overset { \scriptscriptstyle { ( k - 2 ) / 2 } } { \underset { n = 1 } { \sum } } \left[ 2 - 2 \sin ^ { 2 } \frac { n \pi } { k } \log \left( 4 \sin ^ { 2 } \frac { n \pi } { k } \right) \right. } \\ { \left. - \pi \left( 1 - \frac { 2 n } { k } \right) \sin ^ { 2 } \frac { n \pi } { k } \right] } \end{array}
$$

Gyldén wrote

$$
\begin{array} { l } { \displaystyle \sigma _ { n k } = \frac { ( 1 + q ) \theta } { k + q } \qquad } \\ { \displaystyle = \frac { 1 } { 2 } \delta _ { n , k } + \delta _ { n , k + 1 } + \delta _ { n , k + 2 } + \cdots , } \end{array}
$$

while Brodén wrote

$$
\sigma _ { n k } = \frac { 1 + q } { k + q } = \delta _ { n , k } + \delta _ { n , k + 1 } + \delta _ { n , k + 2 } + \cdot \cdot \cdot .
$$

Since we are dealing merely with approximate values, this difference does not matter much. The probable value $A _ { n }$ of an arbitrarily chosen number $\dot { a } _ { i }$ in the system $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ is represented by

$$
A _ { n } = \sum _ { k = 1 } ^ { \infty } k \delta _ { n k } .
$$

If $\delta _ { n k }$ is replaced by $D _ { k }$ ， and $D _ { k }$ by $F ( q , k )$ ，then

$$
A _ { n } = \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k } \frac { 1 + q } { [ 1 + ( q / k ) ] [ 1 + ( ( 1 + q ) / k ) ] } .
$$

Thus we get $A _ { n } \to \infty$ independently of $_ n$

Gyldén obtained several interesting corollaries from this theorem. As an example,in the expansion of an arbitrarily chosen number in a continued fraction he proved that the probable value of a partial denominator $^ a$ is equal to 2.Hence 1 appears as a denominator in such an expansion equally often as numbers larger than 2.

Now we return to our equation (1) and consider

$$
\sum \frac { \kappa ^ { r } } { m - n A } , \qquad r = | m - n | , \qquad \kappa < 1 .
$$

We restrict ourselves to those values of $m$ and $_ n$ that correspond to the reduced fractions $r _ { \mathfrak { n } } / s _ { \mathfrak { n } }$ of the continued fraction representing $\pmb { A }$ The corresponding exponent is $s _ { n } - r _ { n }$ . Since $r _ { n }$ is approximately equal to $A s _ { n }$ ，we have, instead of (1),

$$
U = \sum _ { n = 1 } ^ { \infty } { \bigg | } { \frac { \varepsilon ^ { s _ { n } } } { r _ { n } - s _ { n } A } } { \bigg | } ,
$$

where e denotes a quantity approximately equal to $\varepsilon = \kappa ^ { 1 - \gamma } < 1$ . From a well-known theorem for continued fractions, we obtain

$$
A = \frac { r _ { n } } { s _ { n } } + ( - 1 ) ^ { n } \left\{ \frac { 1 } { s _ { n } s _ { n + 1 } } - \frac { 1 } { s _ { n + 1 } s _ { n + 2 } } + \cdot \cdot \cdot \right\} ,
$$

and approximately

$$
r _ { n } - s _ { n } A = { \frac { ( - 1 ) ^ { n + 1 } } { s _ { n + 1 } } } .
$$

Thus we must deal with a series of the form

$$
U = \sum _ { n = 1 } ^ { \infty } s _ { n + 2 } \varepsilon ^ { \mathcal { S } n } .
$$

Since we have $s _ { n + 1 } = a _ { n + 1 } s _ { n } + s _ { n - 1 }$ owing to the relation (4), the series $\pmb { U }$ is split into two series $U ^ { \prime }$ and $U ^ { \prime \prime }$ ， such that

$$
U ^ { \prime \prime } = \sum _ { n = 1 } ^ { \infty } s _ { n - 1 } \varepsilon ^ { s _ { n } } , \qquad U ^ { \prime } = \sum _ { n = 1 } ^ { \infty } a _ { n + 1 } s _ { n } \varepsilon ^ { s _ { n } } ,
$$

where $U ^ { \prime \prime }$ is always convergent and $U ^ { \prime }$ is the series whose convergence is under discussion.

In this form the proof of the everywhere dense distribution of the convergence-points and the divergence-points can be carried out directly. In fact, if the partial denominators $a _ { 1 } , a _ { 2 } , \ldots , a _ { m }$ are given, then $\pmb { A }$ must be limited to the interval $l _ { m 1 }$ .Let $a _ { m + 1 } , a _ { m + 2 } , \ldots$ . be so chosen that they are all less than an arbitrary finite number $k$ ; then the series $U ^ { \prime }$ is evidently convergent， and hence these convergencepoints are distributed everywhere densely in this interval. Similarly the divergence-points are everywhere dense in the interval if the number $a _ { m + 1 }$ is suitably chosen ; for example, if $a _ { m + 1 } \geq \varepsilon ^ { - s _ { m } }$

Gyldén proposed the theorem that the probability for the divergence of the series $U ^ { \prime }$ is infinitely small. This theorem was proved by Wiman (1900).Charlier (1907) has simplified the proof.

At first we see that the series $U ^ { \prime }$ is convergent or divergent at the same time as the series

$$
U ^ { \prime \prime \prime } = \sum _ { n = 1 } ^ { \infty } a _ { n + 1 } \varepsilon ^ { s _ { n } } .
$$

Let a power-series

$$
X = \sum _ { n = 0 } ^ { \infty } A _ { n } x ^ { n }
$$

be given. If for all integers $_ n$ greater than ${ \pmb n } _ { 1 }$ an inequality

$$
\textstyle | A _ { n } x _ { 1 } ^ { n } | \leq 1
$$

holds,then the series $\pmb { X }$ is convergent absolutely for all $| x | < | x _ { 1 } |$ . Conversely,if the series $\pmb { X }$ is not absolutely convergent, then such a value ${ \pmb n } _ { 1 }$ of the integer $_ n$ cannot be found. Applying this well-known theorem on power-series to the sum $U ^ { \prime \prime \prime }$ ， we see that this series is convergent for all $\varepsilon < \varepsilon _ { 1 }$ if an inequality

$$
a _ { n + 1 } \leqq { \frac { 1 } { \varepsilon _ { 1 } ^ { \ s _ { n } } } } .
$$

holds for $n \geq n _ { 1 }$ . Then what is the probability that this inequality is satisfied for all $n > n _ { \mathrm { 1 } } ?$ The probability that a certain of these inequalities is not satisfied is smaller than $2 \varepsilon _ { 1 } ^ { s _ { n } }$ according to the theorem proved above,which states that $W < 2 / k$ .Hence the probability that the inequality is satisfied for a certain value of $_ n$ is large than $1 - 2 \varepsilon _ { 1 } ^ { s _ { n } }$ . The probability that all the inequalities for all values of $_ n$ are satisfied is larger than the product

$$
\prod _ { n = n _ { 1 } } ^ { \infty } { \left( 1 - 2 \varepsilon _ { 1 } ^ { s _ { n } } \right) } .
$$

This product can be arbitrarily close to unity for a sufficiently large value of $n _ { 1 }$ .The probability for the convergence of the series $U ^ { \prime \prime \prime }$ differs from unity by an infinitely small amount. The probability for the divergence of the series $U ^ { \prime \prime \prime }$ ，and accordingly the probability for the divergence of the series $U$ ，is infinitely small.

There has been heated discussion between Brodén (1901,1901a) and Wiman (1900,1901） as to the meaning of Gyldén's theorem. Wiman considered Gyldén's theorem in its mathematically strict sense, while Brodén thought that the theorem could not be extended to the everywhere dense number-set which Gyldén dealt with.

In any case this study has made it clear that there exists point-set theoretical difference between the convergence-points and the diver-gence-points.Even though it may be true that the probability of diver-gence is infinitely small, the difficulty of Bruns's theorem has not been overcome.By the determination of the integration constants an infinite number of convergence-points and an infinite number of divergencepoits are met in the continuous variation of the initial values that the solution contains.Thus the determination of constants is mathematically meaningless,and the whole perturbation theory is lost in the confusion.Charlier (1889) tried to evade this difficulty by a method which will be discussed in Section 15.6.

Brodén considered Gyldén's series

$$
\sum _ { n = 1 } ^ { \infty } s _ { n } ^ { 2 } a _ { n + 1 } ^ { 2 } \varepsilon ^ { s _ { n } } , \qquad 0 < \varepsilon < 1 .
$$

The radius of convergence of this series is diffcult to estimate.Let $G$ denote the upper bound of

$$
\operatorname* { l i m } _ { n \to \infty } ( s _ { n } ^ { 2 } a _ { n + 1 } ^ { 2 } ) ^ { 1 / s _ { n } } .
$$

Then according to Cauchy's theorem on functions defined by their Taylor expansions, the series is convergent if $G < 1 / \varepsilon$ ， is divergent if $G > 1 / \varepsilon$ ，and is indeterminate if $G = 1 / \varepsilon$ (Hadamard,1892).Brodén proved that in any partial interval contained between O and 1 there exist points $\nu$ for which its expansion in a continued fraction is such that

$$
\left\{ a _ { n + 1 } \right\} ^ { 2 / s _ { n } } < \frac { 1 } { \varepsilon } - \delta , \qquad \delta < \frac { 1 } { 2 }
$$

for all values of $_ n$ beyond a certain bound；and also there exist points $\nu$ for which its expansion is such that

$$
\{ a _ { n + 1 } \} ^ { 2 / s _ { n } } > \frac { 1 } { \varepsilon } + \delta , \qquad \delta > 0
$$

for all values of $_ n$ beyond a certain bound. Hence the favorable and unfavorable points both lie everywhere condensed in any partial interval. Considered as a function of $\nu$ the series (6) constitutes an everywhere-dense set of infinity-points. Thus，according to Brodén, the corresponding function is totally discontinuous in Baire's sense (Sections 2.1,and 15.2).

The question may arise whether a series behaves in any assigned manner.For example,does it converge more strongly than a given geometrical series? For that purpose we assume that the terms of a series constantly decrease from the first to the nth term.Denote a term of the series by $u _ { i }$ ; then we have $u _ { i + 1 } < u _ { i }$ by the assumption. From the relation $s _ { 1 } = a _ { 1 }$ ， $s _ { 2 } = 1 + a _ { 1 } a _ { 2 }$ we obtain the inequality

$$
a _ { 3 } < \frac { a _ { 1 } a _ { 2 } } { 1 + a _ { 1 } a _ { 2 } } p ^ { a _ { 1 } a _ { 2 } - a _ { 1 } + 1 } , \qquad \sqrt { \frac { 1 } { \varepsilon } } = p .
$$

Since $a _ { 3 }$ is an integer, this is equivalent to

$$
a _ { 3 } < h ( a _ { 1 } , a _ { 2 } ) ,
$$

where $h ( a _ { 1 } , a _ { 2 } )$ is the smallest integer larger than the right-hand member of (7). The probability $w _ { 2 }$ that $u _ { 2 } < u _ { 1 }$ is

$$
w _ { 2 } = 1
$$

$$
- \sum _ { k = 1 } ^ { \infty } \sum _ { i = 1 } ^ { \infty } { \frac { 1 } { i ( i + 1 ) ( k i + 1 ) ^ { 2 } ( k i + i + 1 ) [ ( k i + 1 ) h ( r , k ) + i } }
$$

In fact, the probability that $a _ { 1 } = i$ and $a _ { 2 } = k$ is equal to

$$
\frac { 1 } { i ( i + 1 ) ( k i + 1 ) ( k i + i + 1 ) } ,
$$

as in the case of $S _ { \mathfrak { d } }$ and $S _ { \mathfrak { d } 2 }$ . With these values of $a _ { 1 }$ and $a _ { 2 }$ the probability for the non-validity of the inequality (7) is equal to

$$
\left[ i , k , h ( i , k ) \right] - \left[ i , { \frac { 1 } { k } } \right] = { \frac { 1 } { ( k i + 1 ) [ ( k i + 1 ) \cdot h ( i , k ) + i ] } } .
$$

Hence

$$
w _ { 2 } < 1 - \frac { 1 } { 2 4 ( p + 1 ) } ,
$$

where the terms with $i = k = 1$ are only taken into account in the sum. Thus the probability for the validity of $u _ { 1 } < u _ { 2 } < u _ { 3 }$ is smaller than $w _ { 2 }$ ，and successively we obtain $w _ { 2 } < w _ { 3 } < \cdots < w _ { n }$ . The higher the term of the series is,up to which the terms of the series remain constantly decreasing, the smaller is the corresponding probability.If we restrict matters further so that the terms of the series decrease as fast as a certain assigned rate, then the corresponding probability is much smaller.

If we suppose that the terms decrease,not from the first term, but from the term $u _ { \rho + 1 }$ to the term $u _ { \rho + n }$ ， while the behavior of the preceding terms is not taken into account, then the probability $w _ { \rho n }$ for this Occurrence is larger than ${ \boldsymbol w } _ { n } = { \boldsymbol w } _ { 0 n }$ . The probability $w _ { \rho n }$ increases with $\rho$ for a fixed value of $_ n$ ，while $\boldsymbol { w } _ { \boldsymbol { n } \rho }$ decreases with $_ n$ for a fixed value of $\rho$ .Let $\rho$ be a fixed number and let $_ n$ increase to infinity. Then what is the behavior of $\scriptstyle \operatorname* { l i m } _ { n \to \infty } w _ { \rho n }$ on the assumption that $u _ { \rho + n + 1 } < \theta u _ { \rho + n }$ $( 0 < \theta < 1 )$ for all values of $n ?$ What is the probability that the series (6) converges more rapidly than a geometrical series with quotient $\theta ?$ Any probability ${ { w } _ { \rho n } }$ may be equal to the ratio of the total favorable interval to the whole $\nu$ -interval from O to 1.If we make a transition to $w _ { \rho , n + 1 }$ ，then an unfavorable interval may remain as unfavorable but at the same time a new unfavorable interval may appear out of the former favorable interval. Thus an arbitrary interval for a sufficiently large $_ n$ contains an unfavorable partial interval. In the limit $n \to \infty$ the favorable points may not be condensed in any interval whatsoever. However there may be a set of these favorable points with nonzero content.At the same time there may be a set of these favorable points with zero content, then the probability is zero.Brodén (190O,1901) did not decide the question and maintained that Gyldén's theorem that the probability for an unfavorable case is infinitely small needed further discussion.

# 15.6CHARLIER’S COMMENT

As has been remarked, the convergence of the series found in celestial mechanics should be discussed in two different ways. One is the discussion of the series obtained at each stage of successive approximation.The other is the discussion of the final expression in the form of series,which,even though the series at each stage of successive approximation may be convergent,would be divergent, or which, even though the series at each stage of successive approximation may be divergent，would be convergent when those series obtained at each stage of successive approximation were superposed. The first aspect evidently bears on the convergence of the series at each approximation stage. The perturbation theory is,according to Laplace's original idea, expanded in powers of the disturbing masses.

In the first approximation we find the radius vector by solving a differential equation of the form (Gyldén, 1888 ； Section 10.19):

$$
\frac { d ^ { 2 } u } { d t ^ { 2 } } + \nu ^ { 2 } u = \sum _ { i , j } B _ { i j } \sin { [ ( i n - j n ^ { \prime } ) t + H _ { i j } ] } \equiv Q ,
$$

and the longitude from

$$
\frac { d ^ { 2 } Z } { d t ^ { 2 } } = \sum _ { i , j } A _ { i j } \sin { [ ( i n - j n ^ { \prime } ) t + G _ { i j } ] } \equiv R .
$$

The integrals are obtained in the form

$$
\begin{array} { l } { { \displaystyle { \boldsymbol { u } } = \frac { 1 } { \nu } \sin \nu t \int { \boldsymbol { Q } } \cos \nu t \cdot d t - \frac { 1 } { \nu } \cos \nu t \int { \boldsymbol { Q } } \sin \nu t \cdot d t } , } \\ { { \displaystyle { \boldsymbol { Z } } = \iint { \boldsymbol { R } } d t ^ { 2 } } . } \end{array}
$$

The series $\boldsymbol { Q }$ and $\pmb R$ are expanded in powers of the eccentricities and inclinations of the planetary orbits generally in convergent form, absolutely and uniformly. These expansions are substituted in (10) where the integration is carried out term by term. An integration constant may be added at each step. These constants are in general combined in one,and the integrals are considered to be indefinite integrals. In practice those two procedures are equivalent,but in discussing the convergence we should consider definite integrals in the interval $t _ { 0 }$ to $t$

Charlier (1889) wrote $\lambda _ { s }$ in place of $i n - j n ^ { \prime }$ ， and considered

$$
u = { \frac { 1 } { \nu } } \sin \upsilon \cdot \sum _ { s } B _ { s } \int _ { t _ { 0 } } ^ { t } \sin \left( \lambda _ { s } t + H _ { s } \right) \cos \upsilon t \cdot d t
$$

$$
\begin{array} { c } { { \displaystyle - \frac { 1 } { \nu } \cos \nu t \cdot \sum _ { s } B _ { s } \int _ { t _ { 0 } } ^ { t } \sin \left( \lambda _ { s } t + H _ { s } \right) \sin \nu t \cdot d t , } } \\ { { \displaystyle Z = \sum _ { s } A _ { s } \int _ { t _ { 0 } } ^ { t } d t \int _ { t _ { 0 } } ^ { t } \sin \left( \lambda _ { s } t + G _ { s } \right) d t . } } \end{array}
$$

From these he obtained

$$
\begin{array} { c } { \displaystyle \frac { u Z } { d t } = - \sum _ { s } \frac { A _ { s } } { \lambda _ { s } } [ \cos { ( \lambda _ { s } t + G _ { s } ) } - \cos { ( \lambda _ { s } t _ { 0 } + G _ { s } ) } ] , } \\ { \displaystyle Z = - \sum _ { s } \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } [ \sin { ( \lambda _ { s } t + G _ { s } ) } - \sin { ( \lambda _ { s } t _ { 0 } + G _ { s } ) } } \\ { \displaystyle - \lambda _ { s } \cos { ( \lambda _ { s } t _ { 0 } + G _ { s } ) } \cdot ( t - t _ { 0 } ) ] , } \\ { \displaystyle u = \sum _ { s } \frac { B _ { s } } { \nu ^ { 2 } - \lambda _ { s } ^ { 2 } } \Big [ \sin { ( \lambda _ { s } t + H _ { s } ) } - \sin { ( \lambda _ { s } t _ { 0 } + H _ { s } ) } \cos { ( \lambda _ { s } t _ { 0 } + H _ { s } ) } } \\ { \displaystyle - \frac { \lambda _ { s } } { \nu } \cos { ( \lambda _ { s } t + H _ { s } ) } \sin { \nu ( t - t _ { 0 } ) } \Big ] . } \end{array}
$$

If

$$
\sum _ { s } { \frac { A _ { s } } { \lambda _ { s } } } , \sum _ { s } { \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } } , \sum _ { s } { \frac { B _ { s } } { \nu ^ { 2 } - \lambda _ { s } ^ { 2 } } }
$$

are convergent, then, putting

$$
\begin{array} { r l } & { G _ { 0 } = \displaystyle \sum _ { s } \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } \sin { ( \lambda _ { s } t _ { 0 } + G _ { s } ) } , } \\ & { H _ { 1 } = \displaystyle - \sum _ { s } \frac { B _ { s } } { y ^ { 2 } - \lambda _ { s } ^ { 2 } } \sin { ( \lambda _ { s } t _ { 0 } + H _ { s } ) } , } \\ & { G _ { 1 } = \displaystyle \sum _ { s } \frac { A _ { s } } { \lambda _ { s } } \cos { ( \lambda _ { s } t _ { 0 } + G _ { s } ) } , } \\ & { H _ { 2 } = \displaystyle - \sum _ { s } \frac { y _ { s } } { y } \frac { B _ { s } } { y ^ { 2 } - \lambda _ { s } ^ { 2 } } \cos { ( \lambda _ { s } t _ { 0 } + H _ { s } ) } . } \end{array}
$$

we can write the integrals in the form of Laplace (Section 8.2):

$$
\frac { d Z } { d t } = G _ { 1 } - \sum _ { s } \frac { A _ { s } } { \lambda _ { s } } \cos { ( \lambda _ { s } t + G _ { s } ) } ,
$$

$$
\begin{array} { r l r } {  { Z = G _ { 0 } + G _ { 1 } ( t - t _ { 0 } ) - \sum _ { s } \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } \sin { ( \lambda _ { s } t + G _ { s } ) } , } } \\ & { } & { \quad \quad u = H _ { 1 } \cos { \nu ( t - t _ { 0 } ) } + H _ { 2 } \sin { \nu ( t - t _ { 0 } ) } } \\ & { } & { \quad \quad + \sum _ { s } \frac { B _ { s } } { \nu ^ { 2 } - \lambda _ { s } ^ { 2 } } \sin { ( \lambda _ { s } t + H _ { s } ) } . } \end{array}
$$

Here appear the small divisors $\lambda _ { s }$ and $\nu ^ { 2 } - \lambda _ { s } ^ { 2 }$ ，for which the series may become divergent, depending on the value of the mean motions. It can be shown that these series for any large value of $t$ are conver-gent absolutely but that the convergence is in general not uniform. In fact,the simplest series $d Z / d t$ can be written

$$
\frac { d Z } { d t } = 2 \cdot \sum _ { s } \frac { A _ { s } } { \lambda _ { s } } \sin \left[ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } \right] \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) .
$$

Assume that the series $\textstyle \sum _ { s } A _ { s }$ is convergent， i.e.，for any small number $\pmb { \sigma }$ we can choose a value of $s = p ^ { \prime }$ such that

$$
\sum _ { s = p ^ { \prime } } ^ { \infty } \left| A _ { s } \right| < \sigma
$$

for all $\pmb { p } ^ { \prime } \geq p$ . Put

$$
\frac { d Z } { d t } = 2 \cdot \sum _ { s = 0 } ^ { p ^ { \prime } - 1 } \frac { A _ { s } } { \lambda _ { s } } \sin \Big [ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } \Big ] \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) + R _ { p ^ { \prime } } ,
$$

then

$$
\begin{array} { r } { R _ { p ^ { \prime } } \equiv 2 \cdot \sum _ { s = p ^ { \prime } } ^ { \infty } \left| \frac { A _ { s } } { \lambda _ { s } } \sin \left[ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } \right] \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) \right| } \\ { < | t - t _ { 0 } | \cdot \sum _ { s = p ^ { \prime } } ^ { \infty } | A _ { s } | < | t - t _ { 0 } | \cdot \sigma . } \end{array}
$$

If we choose an arbitrarily large value $t ^ { \prime }$ of $t$ and an arbitrarily small positive number $\delta$ ，then we can find a number $q$ such that $R _ { q } , < \delta$ for all $\pmb q ^ { \prime } \geq q$ for all values of $t$ between $t _ { 0 }$ and $t ^ { \prime }$ ，that is,the series (11) is convergent, even absolutely convergent. But we see that the convergence is in general not uniform for an unlimited time interval, since $\pmb q$ depends on $t ^ { \prime }$ ，which can increase without limit.

Similarly， we can show that the series for $Z$ and $\pmb { u }$ are absolutely convergent.In fact,we have

$$
\begin{array} { r l r } { \left. { - 2 \cdot \sum _ { s } \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } \left\{ \cos \left[ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } \right] \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) \right. } }  \\ & { } & \\ & { } & { \quad - \cos \left( \lambda _ { s } t _ { 0 } + G _ { s } \right) \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) \right\} } \\ & { } & { \quad - 2 \cdot \sum _ { s } \frac { A _ { s } } { \lambda _ { s } ^ { 2 } } \left\{ \cos \left[ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } \right] \right. } \\ & { } & \\ & { } & { \quad \left. - \cos \left( \lambda _ { s } t _ { 0 } + G _ { s } \right) \right\} \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) } \end{array}
$$

$$
\begin{array} { r l r } {  { + 2 \cdot \sum _ { s } \frac { A _ { z } } { \lambda _ { s } ^ { 2 } } \cos [ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } ] } } \\ & { } & { \times [ \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) - \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) ] } \\ & { } & { = 4 \cdot \sum _ { s } \frac { A _ { z } } { \lambda _ { s } } \sin [ \frac { 1 } { 4 } \lambda _ { s } ( t + 3 t _ { 0 } ) + G _ { s } ] \cdot \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) \sin \frac { 1 } { 4 } \lambda _ { s } ( t - t _ { 0 } ) } \\ & { } & { +  2 \cdot \sum _ { s } \frac { A _ { z } } { \lambda _ { s } ^ { 2 } } \cos [ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + G _ { s } ]  } \\ & { } & { \times [ \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) - \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) ] . } \end{array}
$$

Since

$$
\begin{array} { r l } & { \sin \frac { 1 } { 4 } \lambda _ { s } ( t - t _ { 0 } ) < \frac { 1 } { 4 } \lambda _ { s } ( t - t _ { 0 } ) , } \\ & { \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) - \sin \frac { 1 } { 2 } \lambda _ { s } ( t - t _ { 0 } ) < \frac { 1 } { 4 8 } \lambda _ { s } ^ { 3 } ( t - t _ { 0 } ) ^ { 3 } , } \end{array}
$$

the inequality

$$
R _ { p } \leq ( t - t _ { 0 } ) ^ { 2 } \cdot \frac { 1 } { 2 } \cdot \sum _ { s = p } ^ { \infty } | A _ { s } | + ( t - t _ { 0 } ) ^ { 3 } \cdot \sum _ { s = p } ^ { \infty } \frac { 1 } { 2 4 } | \lambda _ { s } A _ { s } |
$$

is obtained for the remainder $\scriptstyle { R _ { p } }$ for the $p$ th term of this series.Hence the convergence is proved.

By a similar process we obtain

$$
\begin{array} { r } { u = \displaystyle \sum _ { s } \frac { 2 B _ { s } } { v ^ { 2 } - \lambda _ { s } ^ { 2 } } \cos \left[ \frac { 1 } { 2 } \lambda _ { s } ( t + t _ { 0 } ) + \frac { 1 } { 2 } \nu ( t - t _ { 0 } ) + H _ { s } \right] } \\ { \displaystyle \times \sin \frac { 1 } { 2 } ( \lambda _ { s } - \nu ) ( t - t _ { 0 } ) } \end{array}
$$

$$
+ \sum _ { s } \frac { B _ { s } } { \nu ( \lambda _ { s } + \nu ) } \cos { ( \lambda _ { s } t _ { 0 } + H _ { s } ) } \sin { \upsilon ( t - t _ { 0 } ) } .
$$

Hence the small divisor is eliminated by the argument of the sine function.

Thus the series obtained by the first approximation in Laplace's method are all convergent for any finite value of t. But the appearance of a small divisor makes the convergence nonuniform； that is,with increasing time we must consider more new terms to represent the function. This last property of the series, the nonuniform convergence, has little meaning for practical purposes.We can consider a sufficient number of terms of the series to make the sum of the remaining terms :smaller than we need for practice. But this defect in uniform conver-.gence is important from a theoretical standpoint. Until the uniform .convergence is proved，we cannot show that the represented function will remain bounded for all time.The stability character of the dynami-.cal system cannot be established by the representation in nonuniform .series.

The stability character must be judged on theoretical grounds not .only from the first approximate solution but from the final result of successive approximations.Even though the series may be divergent .or nonuniformly convergent at each stage of successive approximation, the final result may be represented by a uniformly convergent series. For example, define $s _ { 0 } , s _ { 1 } , \ldots$ by

$$
\begin{array} { l } { { \displaystyle s _ { 0 } = \sum _ { n = 1 } ^ { \infty } \sin \frac { t } { n ^ { n } } , \qquad s _ { 1 } = m \cdot \sum _ { n = 1 } ^ { \infty } \alpha ^ { n } \sin \frac { t } { n ^ { n } } , } } \\ { { \displaystyle s _ { 2 } = \frac { m ^ { 2 } } { 1 \cdot 2 } \cdot \sum _ { n = 1 } ^ { \infty } \alpha ^ { 2 n } \sin \frac { t } { n ^ { n } } , \ldots , S = \sum _ { r = 1 } ^ { \infty } s _ { r } } , } \end{array}
$$

where $\alpha$ is real and greater than 1. The series for each $\pmb { s }$ is convergent for finite values of $t$ ，although nonuniformly.However, for a negative $_ { m }$ the sum $s$ is uniformly convergent. Write

$$
S = \sum _ { n = 1 } ^ { \infty } C _ { n } \sin { \frac { t } { n ^ { n } } } ,
$$

then we have

$$
C _ { n } = 1 + m \alpha ^ { n } + \frac { m ^ { 2 } } { 1 \cdot 2 } \alpha ^ { 2 n } + \frac { m ^ { 3 } } { 1 \cdot 2 \cdot 3 } \alpha ^ { 3 n } + \cdot \cdot \cdot = \exp { \{ m \alpha ^ { n } \} } .
$$

If we'give to m any arbitrary negative value, then $\textstyle \sum _ { n } | C _ { n } |$ is very strongly convergent. Note that $s$ must be uniformly convergent. Similarly,it seems possible that

$$
\sum _ { i , i ^ { \prime } , j , j ^ { \prime } } A _ { i i ^ { \prime } j j ^ { \prime } } \sin { ( i \lambda _ { 1 } t + i ^ { \prime } \lambda _ { 2 } t + j \lambda _ { 3 } t + j ^ { \prime } \lambda _ { 4 } t + B _ { i i ^ { \prime } j j ^ { \prime } } ) }
$$

represents a uniformly convergent series if the correct values of the coefficients $A _ { i i ^ { \prime } j j ^ { \prime } }$ can be obtained by successive approximation, although the series obtained at each stage of successive approximation may not have this property.

Charlier (19O2) further discussed the convergence of the series in celestial mechanics,using Poincaré's extension of Cauchy's existence theorem on the solution of a differential equation,as will be shown in Sections 18.1-18.2. Charlier showed that the solution of the threebody problem in powers of the disturbing masses can be expressed in convergent series but that the convergence is not uniform, so that the radius of the convergence depends on the time interval in which the solution is valid.Popoff (1926) discussed a similar situation.

Bohlin (1889） considered the same question on the basis of the partial differential equation that he formulated in his theory (Section 12.6),but without coming to a definite conclusion.He could dispose of the small divisor, but the convergence of the resultant series is open to question (see Section 15.17).

# REFINEMENT BY PETERSSON AND WINTNER

# 15.7PETERSSON'S REFINEMENT

Petersson (1924) considered the convergence behavior of the series

$$
\begin{array} { c } { { \displaystyle \sum _ { \tau _ { 1 } , \tau _ { 2 } , \cdots , \tau _ { s } = - \infty } ^ { + \infty } \frac { A _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } } { \tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdots + \tau _ { s } \nu _ { s } } } } \\ { { \times \exp { \{ 2 \pi \sqrt { - 1 } ( \tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdots + \tau _ { s } \nu _ { s } ) t \} } , } } \end{array}
$$

where $A _ { \tt r _ { 1 } = \tt _ { 2 } \ldots \ldots }$ are given constant coefficients and the real numbers $\nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { s }$ are linearly independent, that is, $\tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdot \cdot \cdot + \tau _ { s } \nu _ { s }$ $\neq 0$ . The sum is taken so that $( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { s } ) \neq ( 0 , 0 , \dots , 0 )$ . Let $x _ { i } = x _ { i } ( t )$ $( i = 1 , 2 , \ldots , n )$ be the generalized coordinates of the nondisturbed motion，then 'the coordinates of the disturbed motion are defined by

$$
\frac { d x _ { i } } { d t } = \sum _ { \tau _ { 1 } , \dots , \tau _ { s } = - \infty } ^ { + \infty } A _ { \tau _ { 1 } \dots \tau _ { s } } \exp { \{ 2 \pi \sqrt { - 1 } ( \tau _ { 1 } \nu _ { 1 } + \dots + \tau _ { s } \nu _ { s } ) t \} } .
$$

An integration gives

$$
\begin{array} { l } { { \displaystyle x _ { i } = x _ { i } ( t ) = \frac { 1 } { 2 \pi \sqrt { - 1 } } \sum _ { \tau _ { 1 } , \dots , \tau _ { s } = - \infty } ^ { + \infty } \frac { A _ { \tau _ { 1 } \dots \tau _ { s } } } { \tau _ { 1 } \nu _ { 1 } + \dots \cdot + \tau _ { s } \nu _ { s } } } } \\ { { \displaystyle ~ \times \exp \left\{ 2 \pi \sqrt { - 1 } \left( \tau _ { 1 } \nu _ { 1 } + \dots \cdot + \tau _ { s } \nu _ { s } \right) t \right\} + A t + B , } } \end{array}
$$

with integration constants $\pmb { A }$ and $B$ , where the term with $\tau _ { 1 } \nu _ { 1 } + \dots +$ $\tau _ { s } \nu _ { s } = 0$ is excluded in the sum. The problem considered by Petersson is: what can be said,under certain restriction on the behavior of the coefficients $A _ { \pmb { \imath \imath \imath \imath \imath \imath \jmath } _ { s } }$ for large values of $| \tau _ { i } | \left( i = 1 , 2 , \dots , s \right)$ ，about the set of $( \nu _ { 1 } , \ldots , \nu _ { s } )$ for which the series (12) is convergent and for which the series (12) is divergent?

Theorem $\boldsymbol { \mathit { 1 } }$ :If

$$
\sum _ { \tau _ { 1 } , . . . , \tau _ { s } } | { \cal A } _ { \tau _ { 1 } \cdots \tau _ { s } } | ( | \tau _ { 1 } | + \cdot \cdot \cdot + | \tau _ { s } | ) ^ { s - 1 }
$$

is convergent, then the point-set $C ^ { \prime }$ of ${ \pmb S }$ -dimensional space $R _ { s }$ with rectangular coordinates $\nu _ { 1 } , \nu _ { 2 } , \ldots , \nu _ { s }$ ，for which

$$
\sum _ { \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } } \biggl | \frac { A _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } } { \tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdot \cdot \cdot + \tau _ { s } \nu _ { s } } \biggr |
$$

is convergent,is dense in the whole space $\pmb { R } _ { s }$ .We see from this theorem that the point-set $C$ of the $( s - 1 )$ -dimensional space $\scriptstyle R _ { s - 1 }$ with rectangular coordinates $\mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { s } .$ ，for which

$$
\sum _ { \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } } \mathopen { } \mathclose \bgroup \left| \frac { A _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } } { \tau _ { 1 } + \tau _ { 2 } \mu _ { 2 } + \cdot \cdot \cdot + \tau _ { s } \mu _ { s } } \aftergroup \egroup \right|
$$

is convergent, is dense in $R _ { s - 1 }$

Theorem 2: The point-set $D ^ { \prime } ( \mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { s } )$ ,for which the superior limit

$$
\overline { { \operatorname * { l i m } } } \left| \frac { A _ { \tau _ { 1 } z _ { 2 } \cdots \tau _ { s } } } { \tau _ { 1 } + \tau _ { 2 } \mu _ { 2 } + \ \cdots \ + \ \tau _ { s } \mu _ { s } } \right| > 0 ,
$$

is dense in $R _ { s - 1 }$ for arbitrary coefficients $A _ { \tt r _ { 1 } \tt r _ { 2 } \ldots \tt s }$ .The point-set $_ D$ of the divergence-points of (12) and (14) is also dense in $R _ { s - 1 }$ for arbitrary coefficients $A _ { \tt r { 1 } \tt r { 2 } } . . . . _ { \tt S }$

Theorem 3: If the series

$$
{ \sum } ^ { \prime \prime } | A _ { \tau _ { 1 } \tau _ { 2 } \dots \tau _ { s } } | \left( | \tau _ { 1 } | + | \tau _ { 2 } | + \dots \cdot + | \tau _ { s } | \right) ^ { 2 s - 1 }
$$

and

$$
\sum _ { \tau _ { 1 } = - \infty } ^ { + \infty } \left. \frac { A _ { \tau _ { 1 } 0 \cdots 0 } } { \tau _ { 1 } } \right.
$$

are both convergent, then the set $_ D$ is measurable with measure 0.

Theorems 1 and 2 were known from the work of Bruns (Section 15.4)，but Petersson has since simplified them，by using algebraic number theory and the theory of continued fractions (Section 15.3). Theorem 3 is new.Actually,if $s = 2$ ， the series

$$
\sum _ { \tau _ { 1 } , \tau _ { 2 } = 0 } ^ { \infty } \left| \frac { A _ { \tau _ { 1 } \tau _ { 2 } } } { \tau _ { 1 } - \tau _ { 2 } \nu } \right| , \qquad \nu > 0 ,
$$

is the series which Gyldén and Brodén discussed (Section 15.5). They concluded that the geometrical probability that $\pmb { \nu }$ is a divergencepoint is infinitely small.But it is impossible to extend this method of proof to the cases $s \geq 3$ . Petersson introduced the idea of Lebesgue's. measure in the proof (Section 15.2),by extending to the general values. of $\pmb { s }$

To prove Theorem 1, suppose that the numbers $\nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { s }$ are all algebraic. Then there exist integers $g _ { i }$ $\boldsymbol { \mathscr { I } } _ { i } ( i = 1 , 2 , \ldots , s )$ such that $\nu _ { i } g _ { \dot { \tau } }$ are all algebraic.Hence, by extending the fraction

$$
\frac { | A _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } | } { | \tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdots + \tau _ { s } \nu _ { s } | }
$$

with $g = g _ { 1 } g _ { 2 } \ldots g _ { s } ,$ ，we obtain algebraic numbers $\nu _ { i } ^ { \prime } = g _ { i } \nu _ { i }$ in the resulting fraction

$$
\frac { | A _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } ^ { \prime } | } { | \tau _ { 1 } \nu _ { 1 } ^ { \prime } + \tau _ { 2 } \nu _ { 2 } ^ { \prime } + \cdots + \tau _ { s } \nu _ { s } ^ { \prime } | } .
$$

Consider the algebraic number-field $R ( \nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { s } )$ of degree $\pmb { n }$ generated by the adjunction of algebraic numbers $\nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { s }$ to the rational number-field $\pmb R$ . In this algebraic number-field $R ( \nu _ { 1 } , \nu _ { 2 } , \dots \dots , \nu _ { s } )$ of degree $\pmb { n }$ with respect to $\pmb R$ the number $\tau _ { 1 } \nu _ { 1 } + \tau _ { 2 } \nu _ { 2 } + \cdot \cdot \cdot + \tau _ { s } \nu _ { s }$ is an algebraic number $\vartheta = \vartheta ^ { ( 1 ) } \neq 0$ belonging to this extended numberfield. In the extension of $| A _ { \tau _ { 1 } \tau _ { 2 } \dots \tau _ { s } } | / | \vartheta |$ with $\big | \vartheta ^ { ( 2 ) } \vartheta ^ { ( 3 ) } \cdots \vartheta ^ { ( n ) } \big | _ { ; }$ ，which is the absolute value of the product of the remaining $n - 1$ factors conjugate to $\vartheta ^ { ( 1 ) }$ ，an integer $| N ( \vartheta ) |$ appears in the denominator and an expression $| A _ { \tau _ { 1 } \tau _ { 2 } \dots \tau _ { s } } | \cdot O [ ( | \tau _ { 1 } | + | \tau _ { 2 } | + \dots + | \tau _ { s } | ) ^ { n - 1 } ]$ appears in the numerator, where $o$ denotes the limit to which the expression tends uniformly with increasing values of $| \tau _ { i } | \left( i = 1 , 2 , \dots , s \right)$ . We propose to show that, if

$$
\sum | A _ { \mathfrak { r } _ { 1 } \mathfrak { r } _ { 1 } \cdots \mathfrak { r } _ { s } } | ( | \tau _ { 1 } | + | \tau _ { 2 } | + \cdot \cdot \cdot + | \tau _ { s } | ) ^ { n - 1 }
$$

is convergent, then the points $( \nu _ { 1 } , \nu _ { 2 } , \dots , \nu _ { s } )$ belong to the point-set $C ^ { \prime }$ . It is sufficient to show that the point-set $Q$ of points $( \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s } )$ with linearly independent coordinates,which are real numbers of an algebraic number-field of degree $_ n$ ， is dense.Evidently we know such a system of numbers $\lambda _ { 1 } ^ { ( 0 ) } , \lambda _ { 2 } ^ { ( 0 ) } , \dots , \lambda _ { s } ^ { ( 0 ) }$ ，that is，the set of all points $( r _ { 1 } \lambda _ { 1 } ^ { ( 0 ) } , r _ { 2 } \lambda _ { 2 } ^ { ( 0 ) } , . . . , r _ { s } \lambda _ { s } ^ { ( 0 ) } )$ inwhich $r _ { 1 } , r _ { 2 } , \ldots , r _ { s }$ are arbitrary rational numbers is a subset of $Q$ and is dense. Put $\lambda _ { 1 } ^ { ( 0 ) } = 1 , \lambda _ { 2 } ^ { ( 0 ) } = \alpha , \ldots ,$ $\lambda _ { s } ^ { ( 0 ) } = \alpha ^ { s - 1 }$ ，where $\alpha$ is an algebraic number of degree s. This is one of the required system,and is dense in $Q$ . Under our assumption on $A _ { \tt r { 1 7 } 2 } . . . . . _ { \tt S }$ it is only necessary to have the convergence of $\sum | A _ { \substack { \scriptscriptstyle \tau _ { 1 } = \ldots \ldots ; \scriptscriptstyle \tau _ { s } } } |$ ， $( | \tau _ { 1 } | + | \tau _ { 2 } | + \cdot \cdot \cdot + | \tau _ { s } | ) ^ { s - 1 }$ ·

For the proof of Theorem 2 it is sufficient to consider the case $s = 2$ Because the partial sum of (14),obtained by taking the sum of (14) with respect to $\tau _ { 1 }$ only， puting the remaining $\tau _ { i }$ $( i \geq 0 )$ equal to zero, is of the form for $s = 2$ . After the case $s = 2$ is proved, it is clear that the points of the set $D ^ { * }$ of Theorem 2 fill the whole hyperplanes of $s - 1$ dimensions which are densely stratified along each coordinate axis.Thus it remains to prove that the number-set $N$ ，each individual $\pmb { \nu }$ of which has the property

$$
\left| \operatorname* { l i m } _ { | \tau _ { 1 } | + | \tau _ { 2 } | \to \infty } \right| \frac { A _ { \tau _ { 1 } = 2 } } { \tau _ { 1 } - \tau _ { 2 } \nu } \biggr | > 0 ,
$$

is dense. We show that there exists a number $\pmb { \nu }$ of $N$ with $| \kappa - \nu | < \varepsilon$ if $\pmb { \kappa }$ is rational and $\varepsilon > 0$ . For that purpose we expand $\pmb { \kappa }$ in a continued fraction

$$
\kappa = [ b _ { 0 } , b _ { 1 } , b _ { 2 } , \ldots , b _ { m } ] ,
$$

and also $\nu$ in the form

$$
 { \boldsymbol { \nu } } = [ b _ { 0 } , b _ { 1 } , b _ { 2 } , \ldots , b _ { m } , b _ { m + 1 } , b _ { m + 2 } , \ldots ] .
$$

Let

$$
\frac { p _ { i } } { q _ { i } } = [ b _ { 0 } , b _ { 1 } , b _ { 2 } , \ldots , b _ { i - 1 } , b _ { i } ]
$$

be the ith reduced fraction of $\pmb { \nu }$ ; then $\pmb { \kappa } = p _ { m } / q _ { m }$ and

$$
| \nu - \kappa | = \left| \nu - \frac { p _ { m } } { q _ { m } } \right| \leq \frac { 1 } { | q _ { m } q _ { m + 1 } | } .
$$

This expression is less than $\varepsilon$ ，if $q _ { m + 1 } = b _ { m + 1 } q _ { m } + q _ { m - 1 } > b _ { m + 1 }$ is made sufficiently large by a suitable choice of $b _ { m + 1 }$ .Then

$$
\left| \frac { p _ { m + 1 } } { q _ { m + 1 } } - \nu \right| \leq \frac { 1 } { q _ { m + 1 } q _ { m + 2 } } < \frac { 1 } { q _ { m + 1 } b _ { m + 2 } } ,
$$

$$
| p _ { m + 1 } - q _ { m + 1 } \nu | < \frac { 1 } { b _ { m + 2 } } , \qquad \frac { 1 } { | p _ { m + 1 } - q _ { m + 1 } \nu | } > b _ { m + 2 } .
$$

If we choose

$$
b _ { m + 2 } > \frac { 1 } { | A _ { p _ { m + 1 } q _ { m + 1 } } | } ,
$$

then we find

$$
\frac { | A _ { p _ { m + 1 } q _ { m + 1 } } | } { | p _ { m + 1 } - q _ { m + 1 } \nu | } > 1 .
$$

If $b _ { i }$ are known for $m + 1 \leqq i \leqq k$ in general, then we have

$$
{ \frac { 1 } { | p _ { k } - q _ { k } \nu | } } > b _ { k + 1 } .
$$

Hence, if $b _ { \kappa + 1 }$ is chosen sufficiently large,we obtain

$$
\frac { 1 } { | p _ { k } - q _ { k } \nu | } > \frac { 1 } { | A _ { p _ { k } q _ { k } } | } .
$$

In this way we see the existence of infinitely many numbers $\nu$ with the required property. For each of these numbers we have $| \nu - \kappa | < \varepsilon ,$ and there are infinitely many pairs $\{ p _ { i } , q _ { i } \}$ of mutually prime numbers such that $p _ { i + 1 } > p _ { i }$ ， $q _ { i + 1 } > q _ { i }$ ，and

$$
\left| { \frac { A _ { p _ { i } q _ { i } } } { p _ { i } - q _ { i } \nu } } \right| > 1 .
$$

Finally we prove Theorem 3 for $s = 2$ , that is, for the series

$$
\sum _ { \tau _ { 1 } \neq 0 , \tau _ { 2 } \neq 0 } \bigg | \frac { A _ { \tau _ { 1 } \tau _ { 2 } } } { \tau _ { 1 } - \tau _ { 2 } \nu } \bigg | .
$$

Let $\pmb { \nu }$ be irrational such that for each fraction $\tau _ { 1 } / \tau _ { 2 }$ we have

$$
\left| \frac { { \tau } _ { 1 } } { { \tau } _ { 2 } } - \nu \right| \geq \frac { \delta } { | { \tau } _ { 1 } | ^ { \alpha _ { 1 } } | { \tau } _ { 2 } | ^ { \alpha _ { 2 } } } ,
$$

where $\delta > 0$ is arbitrary and $\alpha _ { 1 } > 1$ ， $\alpha _ { 2 } > 1$ are fixed.Then

$$
\frac { 1 } { | \tau _ { 1 } - \tau _ { 2 } \nu | } \leq \frac { 1 } { \delta } | \tau _ { 1 } | ^ { \alpha _ { 1 } } | \tau _ { 2 } | ^ { \alpha _ { 2 } - 1 } .
$$

Consider a majorant series

$$
\sum { \frac { 1 } { \delta } } | A _ { \tau _ { 1 } \tau _ { 2 } } | | \tau _ { 1 } | ^ { \alpha _ { 1 } } | \tau _ { 2 } | ^ { \alpha _ { 2 } }
$$

of the series in question

$$
\sum _ { \tau _ { 1 } \neq 0 , \tau _ { 2 } \neq 0 } \bigg | \frac { A _ { \tau _ { 1 } \tau _ { 2 } } } { \tau _ { 1 } - \tau _ { 2 } \nu } \bigg | .
$$

The majorant series is convergent if $\sum \vert A _ { \tau _ { 1 } \tau _ { 2 } } \vert \vert \tau _ { 1 } \vert ^ { \alpha _ { 1 } } \vert \tau _ { 2 } \vert ^ { \alpha _ { 2 } }$ is convergent. We will show that if there exists an irrational number with the required property it corresponds to a convergence-point. Remove a segment of length $\delta / ( | \tau _ { 1 } | ^ { \alpha _ { 1 } } | \tau _ { 2 } | ^ { \alpha _ { 2 } } )$ from both sides of each fraction $\tau _ { 1 } / \tau _ { 2 } ,$ then the set of the divergence-points is covered by a denumerably infinite number of intervals. The sum of the lengths of these intervals is

$$
\leq 2 \delta \cdot \sum _ { \mathfrak { r } _ { 1 } \neq 0 , \mathfrak { r } _ { 2 } \neq 0 } \frac { 1 } { | \tau _ { 1 } | ^ { \alpha _ { 1 } } | \tau _ { 2 } | ^ { \alpha _ { 2 } } } .
$$

Hence the sum can be made arbitrarily small, because the series

$$
\sum _ { \tau _ { 1 } \neq 0 , \tau _ { 2 } \neq 0 } \frac { 1 } { | \tau _ { 1 } | ^ { \alpha _ { 1 } } | \tau _ { 2 } | ^ { \alpha _ { 2 } } }
$$

is convergent.

The discussion of the general case is rather complicated, because the divergence-points in $R _ { s - 1 }$ for $s \geq 3$ fill the whole hyperplanes, which themselves are densely stratified.The proof is based on the theorem that the external measure of the sum-set of denumerably infinite sets is at most equal to the sum of the external measure of each individual set (Section 15.2). It is sufficient to show that the external measure of the set of divergence-points,which are located in a sphere of an arbitrary radius $R > 0$ ，is zero.In fact，this theorem is then valid also for the set of divergence-points in any sphere of radius nR $( n = 1 , 2 , \ldots )$ ,hence for the sum-set of these sets,and hence for the set of all divergence-points.

Insofar as.the theorem refers to the divergence-points in a fixed sphere $\kappa$ of radius $\pmb R$ ， we prove the theorem in a more general manner than is necessary for the theorem.

Let $F ( \tau _ { 1 } , \tau _ { 2 } , \dots \dots , \tau _ { s } )$ be a positive function of integers $\tau _ { 1 } , \tau _ { 2 } , \ldots , \tau _ { s }$ for all systems $( \tau _ { 1 } , \tau _ { 2 } , \dots \dots \tau _ { s } )$ in the summation $\Sigma ^ { \prime \prime }$ such that

$$
{ \sum } ^ { \prime \prime } \frac { 1 } { F ( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { s } ) \sqrt { \tau _ { 2 } ^ { 2 } + \tau _ { 3 } ^ { 2 } + \dots + \tau _ { s } ^ { 2 } } }
$$

is convergent. By a suitable choice of the function $\pmb { F }$ the coefficients $A _ { \tt r a s e s }$ can be made to satisfy the condition that the series

$$
\sum ^ { \prime \prime } | A _ { \tau _ { 1 } : _ { 2 } \dots : \tau _ { \mathcal { S } } } | \cdot F ( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { \mathcal { S } } )
$$

and

$$
\sum _ { \tau _ { 1 } = - \infty } ^ { + \infty } \left. \frac { A _ { \tau _ { 1 } 0 \cdots 0 } } { \tau _ { 1 } } \right.
$$

are both convergent. Of course, if $A _ { \tt r _ { 1 } \tt s _ { 2 } \tt s } . . . . _ { \tt s }$ satisfy the condition in the statement of Theorem 3, then

$$
F ( \tau _ { 1 } , \tau _ { 2 } , \ldots , \tau _ { s } ) = ( | \tau _ { 1 } | + | \tau _ { 2 } | + \cdots + | \tau _ { s } | ) ^ { 2 s - 1 } .
$$

Also, in place of the series (14),we consider the series

$$
\sum ^ { \prime \prime } { \biggl | } { \frac { \mathcal { A } _ { \tau _ { 1 } \tau _ { 2 } \cdots \tau _ { s } } } { \tau _ { 1 } + \tau _ { 2 } \mu _ { 2 } + \cdots + \tau _ { s } \mu _ { s } } } { \biggr | } ,
$$

which is convergent or divergent at the same time as the series (14) is convergent or divergent.

Now take the points $( \mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { s } )$ such that for all possible systems $( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { s } )$ in $\Sigma ^ { \prime \prime }$ we have

$$
| \tau _ { 1 } + \tau _ { 2 } \mu _ { 2 } + \cdot \cdot \cdot + \tau _ { s } \mu _ { s } | > \frac { \delta } { F ( \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } ) } ,
$$

where $\delta > 0$ is arbitrary. Then we have

$$
\sum ^ { \prime \prime } < \frac { 1 } { \delta } \cdot et { } { ' } \sum ^ { \prime \prime } | A _ { \tau _ { 1 } \tau _ { 2 } \dots \tau _ { s } } | \cdot F ( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { s } ) .
$$

Hence the points $( \mu _ { 2 } , \mu _ { 3 } , \ldots , \mu _ { s } )$ are convergence-points. In order to construct the covering of the divergence-points by a denumerable number of space-segments we consider the geometrical meaning of the condition for a point to be a convergence-point. With $\tau _ { 1 } , \tau _ { 2 } , \ldots , \tau _ { s }$ fixed, the inequality

$$
| \tau _ { 1 } + \tau _ { 2 } \mu _ { 2 } + \cdots + \tau _ { s } \mu _ { s } | \leq \frac { \delta } { F ( \tau _ { 1 } , \tau _ { 2 } , \ldots , \tau _ { s } ) }
$$

means that the totality of points $( \mu _ { 2 } , \ldots , \mu _ { s } )$ is at a distance

$$
\leq { \frac { \delta } { F ( \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } ) } } \cdot { \frac { 1 } { \sqrt { \tau _ { 2 } ^ { 2 } + \dots + \tau _ { s } ^ { 2 } } } }
$$

from the plane $T \colon \tau _ { 1 } + \tau _ { 2 } \lambda _ { 2 } + \cdots + \tau _ { s } \lambda _ { s } = 0$ ,i.e.,within a domain limited by two planes parallel to $_ T$ . If a point is outside all planes obtained by all systems $( \tau _ { 1 } , \tau _ { 2 } , \dots , \tau _ { s } )$ ， then it is certainly a convergence-point. Then the covering of the set of divergence-points in the totality of all such planes is obtained；in particular, the set of divergence-points in $\kappa$ is covered by the totality of the partial segments of all planes that are cut by $\kappa$ from each individual plane. The geometrical content

$$
\int d x _ { \mathnormal { 2 } } \ldots d x _ { \mathnormal { s } }
$$

of such a partial segment is computed by integration over the domain defined by

$$
\begin{array} { c } { x _ { 2 } ^ { 2 } + \dots + x _ { s } ^ { 2 } \equiv R ^ { 2 } , } \\ { \mathrm { } } \\ { | \tau _ { 1 } + \tau _ { 2 } x _ { 2 } + \dots + \tau _ { s } x _ { s } | \equiv \frac { \delta } { F ( \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } ) } , } \end{array}
$$

which is denoted by $^ { a }$ . We transform the variables of integration by an orthogonal transformation such that a coordinate plane is rotated to the plane $\tau _ { 2 } \mu _ { 2 } + \dots + \tau _ { s } \mu _ { s } = 0$ parallel to $_ { T }$ . Denote the new variables by $z _ { 2 } , \ldots , z _ { s }$ ; then

$$
\tau _ { 2 } x _ { 2 } + \cdot \cdot \cdot + \tau _ { s } x _ { s } = c z _ { s } , ~ c = \sqrt { \tau _ { 2 } ^ { 2 } + \cdot \cdot \cdot + \tau _ { s } ^ { 2 } } ,
$$

and the integral becomes

$$
\int d z _ { 2 } \cdots d z _ { s } ,
$$

integrated over the domain

$$
z _ { 2 } ^ { 2 } + \cdots + z _ { s } ^ { 2 } \equiv R ^ { 2 } , \qquad \left| \frac { \tau _ { 1 } } { c } + z _ { s } \right| \equiv \frac { a } { c } .
$$

In an elementary manner, an estimate of the integral gives

$$
\int d x _ { 2 } \cdot \cdot \cdot d x _ { s } \leq C ( R , s ) \cdot { \frac { a } { c } } ,
$$

where $c$ depends only on $\pmb R$ and $s$ Hence

$$
\int d x _ { 2 } \cdot \cdot \cdot d x _ { s } \leq C \cdot \frac { \delta } { F ( \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } ) } \cdot \frac { 1 } { \sqrt { \tau _ { 2 } ^ { 2 } + \cdot \cdot \cdot + \tau _ { s } ^ { 2 } } } .
$$

Thus the sum of the geometrical contents of the covering is

$$
\leq \delta C \cdot \sum ^ { \prime \prime } \frac { 1 } { F ( \tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { s } ) \sqrt { \tau _ { 2 } ^ { 2 } + \dots + \tau _ { s } ^ { 2 } } } ,
$$

and is arbitrarily small. Hence Theorem 3 is proved.

# 15.8WINTNER'S DISCUSSION BASED ON THE THEORY OF ALMOST PERIODIC FUNCTIONS

Wintner (1929) pointed out that the proof of Gyldén and Bruns is not satisfactory and discussed the theorem on the basis of modern theory of functions of a real variable. Even Poincaré's proof (1884) based on majorant series,as will be shown shortly， is not mathematically strict. Wintner discussed the theorem directly, basing his investigation on the theory of almost periodic functions (Sections 2.11-2.14). According to Bohr (1925) the sum of amplitudes is absolutely conver-gent, if the exponents are linearly independent in the series representation in the form of an almost periodic function.

Wintner (1929) considered the differential equation

$$
\frac { d x } { d t } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \mu ^ { n + m } A _ { n m } ( \mu ) \cos { ( n - m \rho ) } t \qquad ( x ) _ { t = 0 } = 0 ,
$$

where $\rho$ is a real irrational number, $\pmb { A } _ { \pi m }$ is a function of a real parameter $\mu \ ( - 1 < \mu < \ + 1 )$ for which

$$
) < \mathrm { c o n s t a n t } < ( | A _ { \pi m } ( \mu ) | ) ^ { 1 / ( n + m ) } < \mathrm { c o n s t a n t } ( n , m = 1 , 2 , \ldots )
$$

The condition

$$
A _ { n m } ( \mu ) = 1 \qquad ( n , m = 1 , 2 , \ldots )
$$

does not impose any restriction on the problem. Put

$$
\phi = \phi ( t ; \mu ; \rho ) = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \mu ^ { n + m } \cos { ( n - m \rho ) } t ,
$$

then (15) becomes

$$
\frac { d x } { d t } = \phi ( t ; \mu ; \rho ) , ( x ) _ { t = 0 } = 0 .
$$

The parameter $\mu$ is not necessarily real. Time $t$ is real． The real irrational number $\rho$ is chosen fixed. In $| \mu | < 1$ ,then the series (16) is uniformly convergent on the whole $t \cdot$ -axis extending up to infinity, since it admits a convergent majorant series $\phi ( 0 ; | \mu | ; \cdot )$ . The series (16) is almost periodic because of the uniformly convergent expansion of the series (Section 2.11).Since the series is then uniformly conver-gent, term-by-term integration of the right-hand member of (17) gives

$$
x = \psi ( t ; \mu ; \rho ) ,
$$

where

$$
\psi ( t ; \mu ; \rho ) = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \frac { \mu ^ { n + m } } { n - m \rho } \sin { ( n - m \rho ) t }
$$

is uniformly convergent for any $\rho$ and for any $\mu$ such as $| \mu | < 1$ on any finite but fixed interval $- T < t < + T$ If $\rho$ is rational,then (16) gives a continuous periodic function,besides a linear additional term with respect to $t$ ,for and only for $| \mu | < 1$ . This trivial case is put outside our consideration. Then the problem at hand is to see when (18) is uniformly convergent also for all $t$ ,i.e.,on the whole $t \cdot$ -axis extend-ing to infinity. The original problem was to see for what values of $\mu$ and $\rho$ the value of the coordinate (17),which is uniquely defined by a convergent series (18) for any $\rho$ and for $| \mu | < 1 \ ( - \infty < t < + \infty )$ ， remains smaller than an upper bound independent of $t$ .This is the case when and only when the function (17) is almost periodic. In fact, for the almost periodicity of an indefinite integral of an almost periodic function the boundedness is not only necessary but suffcient (Section 2.12),and then the derivative (16) is likewise almost periodic.

For a further study we must first discuss the series

$$
\Psi ( \mu ; \rho ) = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } { \frac { | \mu | ^ { n + m } } { | n - m \rho | } } .
$$

Let a number $\mu _ { 0 } \neq 0$ for a fixed $\rho$ be such that the series $\Psi ( \mu _ { 0 } ; \rho )$ is convergent.Then (19） is also convergent for $| \mu | < | \mu _ { 0 } |$ The series (18）is uniformly convergent in this circle for all $t$ ，and hence is bounded, i.e.,almost periodic.If $\mu _ { 0 } \neq 0$ for a fixed $\rho$ is, on the contrary,such that the series $\psi ( t ; \mu _ { 0 } ; \rho )$ is uniformly convergent for all $t$ with a definite arrangement of the order of terms, then the function represented by the series is bounded.But,if the function is bounded, then the series

$$
M ( \mu _ { 0 } ; \rho ) = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \frac { | \mu _ { 0 } | ^ { 2 ( n + m ) } } { ( n - m \rho ) ^ { 2 } } ,
$$

i.e., the sum of the squares of the amplitudes is convergent. Hence it follows from (19) that the majorant series (19) is convergent for $\lvert \mu \rvert$ $< \mu _ { 0 }$ by Schwarz's inequality

$$
[ \Psi ( \mu ; \rho ) ] ^ { 2 } \leq M ( \mu _ { 0 } ; \rho ) \cdot \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } | \vartheta | ^ { 2 ( n + m ) } , \qquad | \vartheta | < 1 ,
$$

if $| \mu | < | \mu _ { 0 } |$ ,i.e.,if $\mu = \vartheta \mu _ { 0 } \left( | \vartheta | < 1 \right)$ . Hence (18) is almost periodic for $| \mu | < \mu _ { 0 }$ and is uniformly convergent for all $t$ Thus the upper bound $\Theta _ { \rho }$ of nonnegative numbers $\lvert \mu \rvert$ ，for which the majorant series $\Psi ( \mu ; \rho )$ is convergent， satisfies all our conditions.Namely，if an irrational number $\rho$ is such that $\Theta _ { \rho } \neq 0$ ，i.e.，for $\Theta _ { \rho } > 0$ ，then, insofar as the boundary $| \mu | = \Theta _ { \rho }$ is not taken into account, two cases are possible:either $| \mu | < \Theta _ { \rho }$ holds,in which case the series(19) is uniformly convergent and bounded for all $t$ ，i.e.，(19)is almost periodic ；or $| \mu | > \Theta _ { \rho }$ ,in which case the series (18) is neither bounded nor uniformly convergent for $- \infty < t < + \infty$ , but is convergent only for $- T < t < T$ .If $\Theta _ { \rho } = 0$ ,then (18) is neither bounded nor uniformly convergent for all $t$ ，but is convergent for any finite interval, for any $\mu \neq 0$ . It is implicitly assumed that $| \mu | < 1$ . Other values of $\mu$ do not appear. For all $\rho$ we have $\Theta _ { \rho } \lessgtr 1$ ，i.e.,(19) is always divergent for $| \mu | > 1$ . In fact, the inner sum of the positive double series (19) is convergent only for $| \mu | < 1$ . In the same way，the series (20) is divergent for $\vert \mu \vert \geq 1$ ； accordingly (18） is certainly not an almost periodic function.

Thus our original question concerning the trigonometric series (18) becomes the question of the radius of convergence $\Theta _ { \rho }$ of the majorant series (19) independent of $t$ ， as a function of the irrational number $\rho$ Here is where the Diophantine character of $\rho$ (Section 15.3) comes in. If the number $\rho$ is irregular, i.e.,if it admits strong approximation by rational numbers in the manner of the transcendental numbers constructed by Liouville (Section 15.3)，then the numerator of (9) decreases rapidly,i.e., the radius of convergence $\Theta _ { \rho }$ decreases and perhaps tends to zero. Otherwise the series (19) is expected to be well convergent by means of algebraic irrationality on the basis of Liouville's inequality (Section 15.3). Thus we have three cases: the irrationality $\pmb { \rho }$ is called regular if $\Theta _ { \rho } \gtrapprox 1$ ； irregular if $0 \leq \Theta _ { \rho } < 1$ ； and singular if $\Theta _ { \rho } = 0$ ，,which is included in the second case,of course.

It can be shown that any interval of the $\rho$ -axis contains singular numbers of the power of continuum but the singular and,more generally， the irregular numbers are distributed only with measure zero.From this circumstance we can see the meaning of this sensitive behavior of the function $\Theta = \Theta _ { \rho }$ for the trigonometric series (18). That is to say, however small we choose to fix the positive number $\mu$ ,there are everywhere densely and even of the power of continuum such values of $\pmb { \rho }$ that the coordinates $x$ are non-bounded, i.e.，not almost periodic. The appearance of such values of $\rho$ in the sense of measure theory is of zero probability in Gylden's terminology.

The proof of the first part of the theorem,which is related to the distribution and the power of the singular number-set, can be carried out according to the well-known theorems on Borel's series (Section 15.1；Hahn,1921) of the type (22) which implies immediately,that this point-set is of the second class of Baire (Section 12.5), that is, it cannot be represented by a sum-set of denumerably infinite number of nowhere-dense point-sets. It must contain a subset of the power of continuum in any interval.

The second part of the theorem, that $\Theta _ { \rho } = 1$ almost everywhere, follows from the consideration of the following Borel series. Let $\{ a _ { j } \}$ be a sequence of positive numbers whose sum $\textstyle \sum _ { j = 1 } ^ { \infty } { \sqrt { a _ { j } } }$ is bounded, and $\left\{ \omega _ { j } \right\}$ be a sequence of arbitrary numbers. Then the series

$$
F ( \rho ) = \sum _ { j = 1 } ^ { \infty } \frac { a _ { j } } { | \rho - \omega _ { j } | }
$$

is almost everywhere convergent (Hahn, 1921, $\mathfrak { p }$ .313).In fact，the series (19) can be written

$$
\Psi ( \mu _ { 0 } ; \rho ) = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \frac { | \mu _ { 0 } | ^ { n + m } / m } { | \rho - ( n / m ) | } .
$$

Both series (21） and (22) are identical to one arother for a fixed choice of $\pmb { \mu }$ ，and accordingly $\{ \omega _ { j } \}$ is identical to a double sequence $\lbrace \lbrace n / m \rbrace \rbrace$ arranged in some way. Hence the boundedness of the sequence $\{ \sqrt { a _ { j } } \}$ reduces to the boundedness of

$$
\sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \frac { | \sqrt { \mu _ { 0 } } | ^ { n + m } } { \sqrt { m } } .
$$

Since the boundedness of this double series is satisfied for $| \mu _ { 0 } | < 1$ ， accordingly for $\mu _ { \circ } = 1 - \left( 1 / k \right) \left( k > 1 \right)$ ，the numbers $\rho$ ，for which $\Theta _ { \rho } \cong 1 - ( 1 / k )$ does not hold, constitute a zero-set. Since a sum-set of a denumerably infinite number of zero-sets $( k = 2 , 3 , \ldots )$ is also a zero-set, the inequality $\Theta _ { \rho } \gtrapprox 1$ holds almost everywhere.Thus the theorem is proved.

Such regular numbers $\rho$ can be given effectively. In fact， any algebraic irrationality is regular.If $_ { \alpha }$ is the degree of $\rho$ ，then according to Liouville there exists a positive number $\beta$ only depending on $\rho$ such that

$$
\left| \rho - { \frac { n } { m } } \right| > { \frac { \beta } { | m | ^ { \alpha } } } \qquad ( n , m = \pm 1 , \pm 2 , . . . ) .
$$

Hence (22) must be convergent for $\vert \mu _ { 0 } \vert < 1$ . Whence it follows again that $\Theta _ { \rho } = 1$ almost everywhere.In fact,non-Liouville numbers, for which the condition (23) is not satisfied for any $\alpha > 0$ ， $\beta > 0$ ，constitute a zero-set.

The equation (17) with (19) is what Hill (1896) considered as typical example (see Section 14.2).We can derive from (17) the equation

$$
{ \frac { d x } { d t } } = \sum _ { n = - \infty } ^ { \infty } { \sum _ { m = - \infty } ^ { \infty } } ^ { \prime } \mu ^ { | n - m | } \cos { ( n - m \rho ) } t ,
$$

where the prime on the summation sign means exclusion of $m = n$ In the case of the equation for the mean longitude,the left-hand side contains the second derivative in place of the first (Section 8.3),so that (17) is transferred to

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \mu ^ { n + m } \cos { \mathrm { \Omega } } ( n - m \rho ) t .
$$

The general solution of this equation is

$$
x = - \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \frac { \mu ^ { n + m } } { ( n - m \rho ) ^ { 2 } } \cos { ( n - m \rho ) } t + C _ { 1 } t + C _ { 2 } .
$$

The difference $x - ( C _ { 1 } t + C _ { 2 } )$ can be disposed of if we take into account the majorant series

$$
\sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } { \frac { | \mu | ^ { n + m } } { ( n - m \rho ) ^ { 2 } } } ,
$$

in the same way as in the above.

It is remarkable that Sibahara (1952） derived the necessary and sufficient condition for the convergence of Bruns's series (1) in the form

$$
\sum _ { i , j } \bigg | \frac { K _ { i j } x ^ { | i - j | } } { i - j \nu } \bigg | .
$$

He divided the summation into the sum for $| i - j \nu | < \varepsilon$ and the sum for $| i - j \nu | \geq \varepsilon$ ， and considered the pair $( i , j )$ such that $| i - j \nu | < \varepsilon ,$ $i < j$ We have

$$
j C > j ( 1 - \nu ) + \varepsilon > j - i = | i - j | > j ( 1 - \nu ) - \varepsilon > j C _ { 1 } ,
$$

for such a pair,so that the first sum is smaller than

$$
\sum { | K _ { i j } x ^ { j C _ { 1 } } / ( i - j \nu ) | } ,
$$

where $C , C _ { 1 }$ are constants. Put, with integers $n \geq 1 , a \geq 1$ ，

$$
\omega = \omega ( \hat { \xi } ) = \operatorname* { l i m } _ { n \to \infty } \frac { \omega _ { n } } { n } , \qquad \omega _ { n } = \omega _ { n } ( \hat { \xi } ) = \operatorname* { l i m } _ { \alpha \to \infty } \frac { \log { ( 1 / \omega _ { n } ( a ) ) } } { \log { a } } ,
$$

$$
\omega _ { \pi } ( a ) = \omega ( a , \xi ) = \operatorname* { m i n } _  \substack { { \scriptscriptstyle 1 a } _ { 0 } \} , \ldots , { \scriptscriptstyle 1 a } _ { n } \ o 1 \geq a } \left( \left| \sum _ { \upsilon = 0 } ^ { \infty } a _ { \upsilon } \hat { \varsigma } ^ { \star } \right| \right) \quad \quad \left( \sum _ { \upsilon = 0 } ^ { n } a , \hat { \varsigma } ^ { \star } \neq 0 \right)
$$

which is at most equal to 1 and does not increase with $_ { a }$ and $\pmb { n }$ . Then $0 \leq \omega _ { n } \leqq \infty$ ， $0 \leq \omega \leq \infty$ . Also,there exists a single-valued definite index $\mu = \mu ( \xi )$ $( 1 \leq \mu \leq \infty )$ ，such that $\omega _ { n } < \infty$ for $n < \mu$ ，and $\omega _ { n } = \infty$ for $n \geq \mu$ . The two numbers $\omega$ and $\mu$ cannot be finite simultaneously.A number $\xi$ is called on $\pmb { A }$ -number if $\omega = 0$ ， $\mu = \infty$ ； an $s$ -number if $0 < \omega < \infty$ ， $\mu = \infty$ ；a $_ { T }$ -number if $\omega = \infty$ ， $\mu = \infty$ ； and a $\pmb { U }$ -number if $\omega = \infty$ ， $\mu < \infty$ ,according to Mahler (1930,1932; see also Koksma, 1936).

It is known that $\xi$ is transcendental if and only if for any large number $\Omega > 0$ there exists a number $n \geq 1$ such that the form $L \equiv$ $x _ { 0 } + x _ { 1 } \xi + \cdots + x _ { n } \xi ^ { n }$ with respect to $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ admits proper approximation $t ^ { - \Omega }$ ，where $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ，1 are linearly independent with respect to the field of rational numbers (Section 15.1). According to this theorem every algebraic number is an $\pmb { A }$ -number. If $\xi$ is real then $\omega \geq 1$ ；and if $\pmb { \xi }$ is not real then $\omega \geq 1 / 2$ ； accordingly, $\boldsymbol { \xi }$ cannot be an $\pmb { A }$ -number. The set of algebraic numbers is identical with the set of $\pmb { A }$ -numbers.Any transcendental number is an $S -$ ，ora $T \sb { - }$ ,or a $U$ -number. The Napier number $^ e$ is an $s { \mathrm { . } }$ -number and $\pi$ is either an Sor a $_ { T }$ -number.Liouville's numbers (Section 15.3） are ${ \pmb U }$ -numbers with $\mu = 1$ ；accordingly,both numbers are algebraically independent of $^ e$ and $\pi$ . According to Mahler (1932a) a number which is not an $s .$ number has the measure zero on the number-segment.

Thus there exists an $\omega$ such that

$$
\vert i - j \nu \vert > C _ { 2 } j ^ { - \omega C _ { 3 } } \qquad ( C _ { 2 } , C _ { 3 } = \mathrm { c o n s t a n t } ) ,
$$

for each $\pmb { \nu }$ other than a $\boldsymbol { \mathbf { \mathit { U } } }$ -number with $\mu = 1$ . Hence the first sum is smaller than

$$
C _ { 4 } \cdot \sum _ { j } | j ^ { \omega _ { 1 } C _ { 3 } } \chi ^ { j C _ { 1 } } | .
$$

This last series has the convergence radius unity as a power series in

$x ^ { C \tt _ { 1 } }$ ，so that it is convergent for $| x | < 1$ .If $\nu$ is a $\pmb { U }$ -number with $\mu = 1$ ， that is,a Liouville number, then there exists a pair $( i , j )$ such that for $\omega > \nu$ we have $0 < | i - j \nu | < j ^ { - \omega }$ . Hence the first sum is greater than

$$
\sum _ { j } | j ^ { \omega ^ { \prime } } \alpha ^ { j C } | .
$$

Put

$$
\omega ^ { \prime } = \lambda ( j ) , \qquad \operatorname * { l i m } _ { j  \infty } \frac { \lambda ( j ) } { j } = \infty ,
$$

then the last series is convergent. Consequently Bruns's series is convergent if $\pmb { \nu }$ is not a Liouville number (Siegel, 1956).

Since the Lebesgue measure of the set of all $s { \mathrm { . } }$ -numbers in the interval [O,1] is unity according to Mahler (1932a), the measure of the set of the convergence-points is unity. This is Gyldén's theorem (Section 15.5).

# TRIGONOMETRIC SERIES

# 15.9TRIGONOMETRIC SERIES

Trigonometric series or Fourier series (Section 2.2) are of the form

$$
T ( x ) = { \frac { 1 } { 2 } } a _ { 0 } + \sum _ { k = 1 } ^ { \infty } { \bigl ( } a _ { k } \cos k x + b _ { k } \sin k x { \bigr ) } .
$$

This is the real part of the power series

$$
{ \frac { 1 } { 2 } } a _ { 0 } + \sum _ { k = 1 } ^ { \infty } ( a _ { k } - { \sqrt { - 1 } } b _ { k } ) z ^ { k }
$$

on the unit circle $z = e ^ { \sqrt { - 1 } x }$ . The series obtained from the imaginary part of this power series

$$
\sum _ { k = 1 } ^ { \infty } \left( a _ { k } \sin k x - b _ { k } \cos k x \right)
$$

is called the conjugate to the series (24).

The summation of the series

$$
P _ { \tau } ( x ) = { \frac { 1 } { 2 } } + \sum _ { k = 1 } ^ { \infty } r ^ { k } \cos k x ,
$$

$$
Q _ { r } ( x ) = \sum _ { k = 1 } ^ { \infty } r ^ { k } \sin k x \qquad ( 0 \leq r < 1 ) ,
$$

can be found from the power series

$$
\frac { 1 } { 2 } + z + z ^ { 2 } + \cdots , \qquad z = r e ^ { \sqrt { - 1 } x }
$$

to be

$$
P _ { r } ( x ) = { \frac { 1 } { 2 } } { \frac { 1 - r ^ { 2 } } { 1 - 2 r \cos x + r ^ { 2 } } } , \ Q _ { r } ( x ) = { \frac { r \sin x } { 1 - 2 r \cos x + r ^ { 2 } } } .
$$

A sequence $v _ { 0 } , v _ { 1 } , v _ { 2 } , \ldots .$ is said to be of bounded variation if the series

$$
| v _ { 0 } - v _ { 1 } | + | v _ { 1 } - v _ { 2 } | + \cdot \cdot \cdot
$$

is convergent. If a sequence $\{ a _ { k } \}$ is of bounded variation, and $a _ { k } \to 0$ ， in particular if $a _ { k }$ decreases monotonically to zero, then the series

$$
\frac 1 2 a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k x , \qquad \sum _ { k = 1 } ^ { \infty } a _ { k } \sin k x
$$

converge uniformly in any interval $0 < \varepsilon \leq x \leq 2 \pi - \varepsilon$ If the series (24) is uniformly convergent, the coefficients are given by

$$
a _ { k } = { \frac { 1 } { \pi } } \int _ { 0 } ^ { 2 \pi } f ( t ) \cos k t d t , \qquad b _ { k } = { \frac { 1 } { \pi } } \int _ { 0 } ^ { 2 \pi } f ( t ) \sin k t d t .
$$

If $a _ { k } \equiv 0 ( k = 1 , 2 , \ldots )$ ， then the necessary and sufficient condition for the uniform convergence of the series

$$
{ \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { \infty } a _ { k } \cos k x
$$

is the convergence of the series $a _ { 0 } + a _ { 1 } + a _ { 2 } + \cdots$ .If $a _ { \kappa } \geq a _ { \kappa + 1 } \to 0$ ， then the necessary and sufficient condition for the uniform convergence of the series

$$
\sum _ { k = 1 } ^ { \infty } a _ { k } \sin { k x }
$$

is $k a _ { k }  0$

If $f ( x )$ and $g ( x )$ are continuous at $\xi$ and $f ( \xi ) \neq g ( \xi )$ ，then the Fourier series for $\ b { f } ( \ b { x } )$ and $g ( x )$ are different. If $\phi ( x )$ is absolutely integrable in $[ a , b ]$ ， then

$$
\int _ { a } ^ { b } \phi ( x ) \operatorname* { s i n } _ { \cos \mu x } d x \to 0 , \qquad \mu \to + \infty .
$$

If $\ b { f } ( \ b { x } )$ is continuous in $[ 0 , 2 \pi ]$ and $f ( 0 ) = f ( 2 \pi )$ ， then there exists a finite trigonometric sum

$$
T _ { m } ( x ) = { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { m } ( a _ { k } \cos k x + b _ { k } \sin k x )
$$

for every $\varepsilon > 0$ ， that satisfies

$$
| f ( x ) - T _ { m } ( x ) | \leq \varepsilon
$$

uniformly in $[ 0 , 2 \pi ]$ . This is called the Weierstrassian approximation theorem.For a quadrically integrable function $f ( x )$ we have

$$
{ \frac { a _ { 0 } ^ { 2 } } { 2 } } + \sum _ { k = 1 } ^ { \infty } { \bigl ( } a _ { k } ^ { 2 } + b _ { k } ^ { 2 } { \bigr ) } = { \frac { 1 } { \pi } } \int _ { 0 } ^ { 2 \pi } [ f ( x ) ] ^ { 2 } d x ,
$$

and

$$
\int _ { 0 } ^ { 2 \pi } [ f ( x ) - T ( x ) ] ^ { 2 } d x \to 0
$$

for $m \to \infty$ . This is called the Riesz-Fischer theorem.A truncated sum (Abschnitt) of the Fourier series for a quadrically integrable function tends to zero. This is the completeness theorem. If $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ and $g ( x )$ are quadrically integrable, then they are convergent and satisfy

$$
{ \frac { a _ { 0 } a _ { 0 } ^ { \prime } } { 2 } } + \sum _ { k = 1 } ^ { \infty } { \bigl ( } a _ { k } a _ { k } ^ { \prime } + b _ { k } b _ { k } ^ { \prime } { \bigr ) } = { \frac { 1 } { \pi } } \int _ { 0 } ^ { 2 \pi } f ( x ) g ( x ) d x ,
$$

where $a _ { 0 } , a _ { 1 } , b _ { 1 } , a _ { 2 } , b _ { 2 } , \dots$ and $a _ { 0 } ^ { \prime } , a _ { 1 } ^ { \prime } , b _ { 1 } ^ { \prime } , a _ { 2 } ^ { \prime } , b _ { 2 } ^ { \prime } , \ldots$ .are the Fourier coefficients for $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ and $g ( x )$ ，respectively.This is called Parseval $\pmb { s }$ formula (Section 2.2).

Let $f ( x )$ be a function defined for $[ a , b ]$ and $\omega ( \delta ) = \omega ( \delta ; f ) =$ max $| f ( x _ { 1 } ) - f ( x _ { 2 } ) |$ for all $x _ { 1 }$ and $x _ { 2 }$ in $( a , b )$ and such that $| x _ { 2 } - x _ { 1 } | \leqq$ $\pmb { \delta }$ . We call $\omega ( \delta )$ the modulus of continuity of $f$ .The function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is continuous if and only if $\omega ( \delta ) \to 0$ with $\pmb { \delta }$ If $\omega ( \delta ) < C \delta ^ { \alpha }$ $( 0 < \alpha \leq 1 )$ and $C$ is independent of $\pmb { \delta }$ ， then we say that $f$ satisfies the Lipschitz condition of order $_ { \alpha }$ in $( a , b )$ . Suppose that $( a , b )$ coincides with $( 0 , 2 \pi )$ and consider a periodic and integrable function $f _ { : }$ ，not necessarily continuous.Let

$$
\omega _ { 1 } ( \delta ) = \omega _ { 1 } ( \delta ; f ) = \operatorname* { m a x } \int _ { 0 } ^ { 2 \pi } | f ( x + h ) - f ( x ) | d x
$$

for all $0 < h \leq \delta$ We call ${ \omega } _ { 1 } ( \delta )$ the integral modulus of continuity of $f$ .For every integrable function $f$ we have $\omega _ { 1 } ( \delta ; f ) = 0$ as $\delta \to 0$ The Fourier coeficients of an integrable function tend to zero,according to Riemann and Lebesgue. If $f$ is of bounded variation,then $| a _ { k } |$ $\leq V / k$ $V / k , | b _ { k } | \leq V / k ( k = 1 , 2 , \ldots )$ where $V$ is the total variation of $f$ over $( 0 , 2 \pi )$ ，and the Fourier series for $f$ converges at every point $x$ to the value $[ f ( x + 0 ) - f ( x - 0 ) ] / 2$ If,in addition, $f$ is continuous at every point of $( a , b )$ ， then the Fourier sum $_ { T }$ is uniformly convergent in $( a , b )$ ，according to Dirichlet.

If $T ( x )$ converges absolutely in a set $\boldsymbol { \varepsilon }$ of positive measure, then the series $\sum { \left( \left. a _ { k } \right. + \left. b _ { k } \right. \right) }$ converges. If $f$ satisfies the Lipschitz condition with $\alpha > 1 / 2$ ，then the sum $T ( x )$ is absolutely convergent.For $\alpha = 1 / 2$ this is no longer true，according to Bernstein.If $f$ is of bounded variation and satisfies the Lipschitz condition with $\alpha > 0$ ， then the series converges absolutely.If two Fourier series $T ( x )$ and $\scriptstyle { T ^ { \prime } ( x ) }$ each converge to the same sum $s ( x )$ at all points $x$ ，then $T ( x )$ ${ \bf \chi } = { \bf T } ^ { \prime } ( x )$ ，i.e.，the two series are identical. This is called the Heine-Cantor uniqueness theorem. If $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is an absolutely integrable function with period $2 \pi$ in $[ 0 , 2 \pi ]$ ，and if its integral has at most a reducible set of singular points, then $\boldsymbol { T } ( \boldsymbol { x } )$ is the Fourier series for $\ b { f } ( \ b { x } )$ . This is the Du Bois-Reymond theorem. If $\begin{array} { r } { \frac { 1 } { 4 } a _ { 0 } ^ { 2 } + \sum _ { k = 1 } ^ { \infty } \left( a _ { k } ^ { 2 } + b _ { k } ^ { 2 } \right) } \end{array}$ converges, then almost all series

$$
\pm a _ { 0 } + \sum _ { k = 1 } ^ { \infty } \pm ( a _ { k } \cos k x + b _ { k } \sin k x )
$$

converge almost everywhere in $[ 0 , 2 \pi ]$

A series

$$
\sum _ { k = 1 } ^ { \infty } ( a _ { k } \cos n _ { k } x + b _ { k } \sin n _ { k } x ) ,
$$

in which $n _ { k + 1 } / n _ { k } > \lambda > 1$ increases at least as rapidly as a geometrical series with term-ratio larger than 1 is called a lacunary series.If this series converges in a set of positive measure， then the series $\scriptstyle \sum _ { k = 1 } ^ { \infty } ( a _ { k } ^ { 2 } + b _ { k } ^ { 2 } )$ converges (Lebesgue,1906; Toneli,1928;Rogosinski, 1930；Hardy and Rogosinski,1944；Zygmund,1935；Hardy,1949; Ford,1916；Knopp,1931；Bromwich,1926；Borel,1928a).

If $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ has at most a finite number of discontinuities $\xi$ ，it is called piecewise discontinuous and we write

$$
f ( \xi ) = \frac { f ( \xi + 0 ) - f ( \xi - 0 ) } { 2 }
$$

at the discontinuity-point $\xi$ Also, $f ( x )$ is piecewise differentiable. Put

$$
\phi ( t , \xi ) = \frac { f ( \xi + 2 t ) + f ( \xi - 2 t ) } { 2 }
$$

then Dini’s criterion for the convergence is that, if there exists a number $\pmb { A }$ such that

$$
\int _ { 0 } ^ { \pi / 2 } \left| \frac { \phi ( t , \xi ) - A } { t } \right| d t
$$

exists,then the Fourier series for $f ( x )$ converges to $\pmb { A }$ at $x = \xi$ .If $\ b { f } ( \ b { x } )$ satisfies the Lipschitz condition with $\pmb { \alpha }$ ，then,it fulfills Dini's criterion, i.e., if $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is continuous in $[ a , b ]$ and satisfies uniformly for $\pmb { \xi }$ in $[ a , b ]$ the inequality

$$
| f ( \xi + t ) - f ( \xi ) | \leq C | t | ^ { \alpha } , \qquad C > 0 , \qquad \alpha > 0 , \qquad | t | \leq T ,
$$

where $C , \alpha , T$ are independent of $\xi$ ，then the Fourier series for $f ( x )$ represents the function $f ( x )$ uniformly convergent in $[ a , b ]$ .The Dirichlet-Jordan criterion is that,if $\phi ( t , \xi )$ is of bounded variation at $t = 0$ ，then the Fourier series for $f ( x )$ converges to

$$
A = \operatorname* { l i m } _ { t \to 0 } { \frac { f ( \xi + t ) + f ( \xi - t ) } { 2 } }
$$

at $\xi$

Fejér has given an example of a continuous function with its Fourier series divergent at a point. Consider a series

$$
\sum _ { k = 1 } ^ { \infty } \alpha _ { k } Q ( x , \mu _ { k } , n _ { k } ) ,
$$

where

$$
Q ( x , \mu , n ) = \sin { ( \mu + n ) x } \cdot \sum _ { k = 1 } ^ { n } { \frac { \sin { k x } } { k } } .
$$

If $\alpha _ { k } = k ^ { - 2 }$ ， $\mu _ { k } = n _ { k } = \alpha ^ { k ^ { 3 } }$ ，then this series defines a continuous function, but the Fourier series is divergent.Also,a series

$$
\sum _ { k = 1 } ^ { \infty } \alpha _ { k } \overline { { Q } } ( x , \mu _ { k } , n _ { k } ) ,
$$

where

$$
\bar { Q } ( x , \mu , n ) = - \cos { ( \mu + n ) x } \cdot \sum _ { k = 1 } ^ { n } \frac { \sin { k x } } { k } ,
$$

defines a continuous function，and the Fourier series is convergent everywhere, but nonuniformly. Kolmogorov has shown that there ex-ists an integrable function for which the Fourier series diverges everywhere.

Riemann (1892) considered the two series

$$
\sum _ { k = 1 } ^ { \infty } { \frac { \psi [ k x + ( 1 / 2 ) ] } { k } } ,
$$

and

$$
\sum _ { n = 1 } ^ { \infty } { \frac { c ( n ) } { n } } \sin 2 \pi n x ,
$$

where

$$
\ast ( x ) = \left. { \begin{array} { l l } { x - [ x ] - { \frac { 1 } { 2 } } } & { \quad ( x \neq [ x ] ) , } \\ { 0 } & { \quad ( x = [ x ] ) , } \end{array} } \right.
$$

and

$$
c ( n ) = \sum _ { d / n } ( - 1 ) ^ { d } ,
$$

the summation in the last equation being extended over the number $d ( n )$ of the divisors $^ d$ of $_ n$ If $x$ is rational, then the two series are both convergent and represent the same value,while the function defined by these series on the set of rational numbers is a nonbounded function on the set of those rational numbers contained in any fixed interval. Chowla and Walfisz (1935) discussed the series for irrational values of $x$ ，and proved that the second Fourier series is almost everywhere convergent and represents almost everywhere the sum of the first Fourier series. Khintchine proved the almost-everywhere convergence by basing his argument on the metrical theory of Diophantine approximation (Titchmarsh,1930).Wintner (1937) discussed these series of Riemann from the standpoint of Lebesgue's measure. The second series is a Fourier series in Lebesgue's sense and belongs to the function defined by the first series,that is,an odd periodic function integrable in Lebesgue's sense and with the Fourier constants as given by the coefficients of the second series. Wintner showed that not only the function defined by the first series but also every positive power of it is integrable in Lebesgue's sense,although this function is non-bounded in every interval if sets of measure zero are excluded.

# 15.I0 NONUNIFORM CONVERGENCE

As has been discussed often in the previous chapters the series in celestial mechanics are of the form

$$
\sum A _ { p } \sin { ( \mu m _ { p } + \nu n _ { p } ) } t + \sum B _ { p } \cos { ( \mu m _ { p } + \nu n _ { p } ) } t ,
$$

where $\pmb { \mu }$ and $\nu$ are independent of $p$ ，and $m _ { p }$ and $n _ { p }$ are positive or negative integers.We consider a series of the form

$$
\sum _ { p = 0 } ^ { \infty } A _ { p } \sin \alpha _ { p } t + \sum _ { p = 0 } ^ { \infty } B _ { p } \cos \beta _ { p } t ,
$$

or particularly

$$
\phi ( t ) = \sum _ { p = 1 } ^ { \infty } A _ { p } \sin \alpha _ { p } t , \qquad A _ { p } > 0 , \qquad \alpha _ { p } > 0 ,
$$

where $1 / A _ { \mathfrak { p } }$ and $\alpha _ { p }$ tend to zero as $p \to \infty$ . The series is convergent if the series $\textstyle \sum _ { p } A _ { p } \alpha _ { p }$ is convergent.By hypothesis, $A _ { p }$ may increase beyond all limits,but it is not clear without proof that $| \phi ( t ) |$ becomes infinite.Poincaré (1882) proved that $| \phi ( t ) |$ becomes greater than $A _ { m } / 4 _ { ; }$ ， where $A _ { m }$ is one of the coefficients of the series.

In fact, if we suppose that we have always

$$
| \phi ( t ) | < \frac { A _ { m } } { 4 } ,
$$

then

$$
\left| \int _ { 0 } ^ { t } \phi ( t ) \sin \alpha _ { m } t d t \right| < \frac { A _ { m } t } { 4 } , \qquad | \phi ( t ) \cos \alpha _ { m } t | < \frac { A _ { m } } { 4 } ,
$$

or, from

$$
\int _ { 0 } ^ { t } \phi ( t ) \sin { \alpha _ { m } t } d t = - \frac { \phi ( t ) \cos { \alpha _ { m } t } } { \alpha _ { m } } + \int _ { 0 } ^ { t } \frac { d \phi } { d t } \frac { \cos { \alpha _ { m } t } } { \alpha _ { m } } d t ,
$$

we find

$$
\left| \int _ { 0 } ^ { t } \frac { d \phi } { d t } \cdot \frac { \cos \alpha _ { m } t } { \alpha _ { m } } d t \right| < \frac { A _ { m } } { 4 } \left( t + \frac { 1 } { \alpha _ { m } } \right) .
$$

Since

$$
\frac { d \phi } { d t } = \sum A _ { p } \alpha _ { p } \cos \alpha _ { p } t ,
$$

we obtain

$$
\begin{array} { r } { \displaystyle \int _ { 0 } ^ { t } \frac { d \phi } { d t } \cos { \alpha _ { m } t } d t = \frac { A _ { m } \alpha _ { m } t } { 2 } + \sum _ { p } \frac { A _ { p } \alpha _ { p } \sin { ( \alpha _ { m } - \alpha _ { p } ) t } } { 2 ( \alpha _ { m } - \alpha _ { p } ) } } \\ { + \sum _ { p } \frac { A _ { p } \alpha _ { p } \sin { ( \alpha _ { m } + \alpha _ { p } ) t } } { 2 ( \alpha _ { m } + \alpha _ { p } ) } . } \end{array}
$$

The two series

$$
\sum _ { p } \frac { A _ { p } \alpha _ { p } } { 2 ( \alpha _ { m } - \alpha _ { p } ) } , \qquad \sum _ { p } \frac { A _ { p } \alpha _ { p } } { 2 ( \alpha _ { m } + \alpha _ { p } ) }
$$

are convergent. Call the sums $\pmb { B }$ and $C$ ，respectively. Then

$$
\left| \int _ { 0 } ^ { t } \frac { d \phi } { d t } \cos \alpha _ { m } t d t - \frac { A _ { m } \alpha _ { m } t } { 2 } \right| < B + C .
$$

Hence

$$
\frac { A _ { m } t } { 2 } < \frac { A _ { m } } { 4 } \Big ( t + \frac { 1 } { \alpha _ { m } } \Big ) + \frac { B } { \alpha _ { m } } + \frac { C } { \alpha _ { m } } .
$$

This inequality cannot be valid for large values of t. Hence $\phi ( t )$ can become greater than $A _ { m } / 4$ Since $A _ { m }$ increases without limit, $\phi ( t )$ can become greater than any given number.

In celestial mechanics we have for the variation of the semimajor axis (Sections 8.7-8.1O) for example,an equation of the form

$$
\frac { d a } { d t } = \sum A _ { p } \sin \alpha _ { p } t + \sum B _ { p } \cos \beta _ { p } t ,
$$

where $\textstyle \sum | A _ { p } |$ and $\sum | B _ { p } |$ are convergent. Neglecting the squares of the disturbing masses,we obtain

$$
\delta a = \sum \frac { A _ { p } } { \alpha _ { p } } ( 1 - \cos \alpha _ { p } t ) + \sum \frac { B _ { p } } { \beta _ { p } } \sin \beta _ { p } t .
$$

If the mean motions are incommensurable, then $\delta \boldsymbol { a }$ may be contained between certain finite limits. However， there are equally incommensurable values for the mean motions for which the series can increase without limit, like the series discussed above.

In practice we know only approximately the ratio of the mean motions and cannot decide if the series remains finite or increases without limit.We cannot draw conclusions about the stability of a planetary system even with Lindstedt's series (Section 13.9).Poincaré (1883) showed that (i),if a series is convergent for a certain time interval， then the series is convergent always,(ii) it is not certain whether the constants are so chosen that the series is convergent,and (ii even if the series is not convergent the series may represent the solution of the problem by an indefinite approximation.

Poincaré (1884) further argued that it is not necessary that the series in celestial mechanics should be uniformly convergent in a strict mathematical sense.It is sufficient that the errors committed by truncating the series at a certain term should remain, for a certain time interval, smaller than a sufficiently small quantity.These are the conditions under which the series in celestial mechanics can represent the motion reasonably well, even though they are divergent (Section 14.3).

Consider a series

$$
\sum A _ { m } \sin { ( \alpha _ { m } t + \beta _ { m } ) } = \phi ( t ) ,
$$

which is supposed to be convergent for certain values of $t$ It may be either absolutely convergent or semiconvergent (Section 14.3). Con-sider the first case and suppose that the series is absolutely convergent for $- \tau < t < + \tau$ ， so that we can alter the order of arrangement of the terms without modifying the sum.Thus two series

$$
\begin{array} { l } { { \displaystyle \sum _ { m } A _ { m } \cos \beta _ { m } \sin \alpha _ { m } t } } \\ { { \displaystyle \quad = \frac { 1 } { 2 } \Big [ \sum _ { m } A _ { m } \sin { ( \alpha _ { m } t + \beta _ { m } ) } - \sum _ { m } A _ { m } \sin { ( - \alpha _ { m } t + \beta _ { m } } } } \end{array}
$$

$$
\begin{array} { l } { \displaystyle { \sum A _ { m } \sin \beta _ { m } \cos \alpha _ { m } t } } \\ { \displaystyle { \quad = \frac { 1 } { 2 } \Big [ \sum A _ { m } \sin ( \alpha _ { m } t + \beta _ { m } ) + \sum A _ { m } \sin ( - \alpha _ { m } t + \beta _ { m } ) \Big ] } } \end{array}
$$

are absolutely convergent, and we can write

$$
\begin{array} { l } { \displaystyle \sum _ { m } A _ { m } \sin { ( \alpha _ { m } t + \beta _ { m } ) } } \\ { = \displaystyle \sum _ { m } A _ { m } \cos { \beta _ { m } } \sin { \alpha _ { m } t } + \displaystyle \sum _ { m } A _ { m } \sin { \beta _ { m } } \cos { \alpha _ { m } t } . } \end{array}
$$

If we put $t = 0$ in the first series (25),then we see that the series $\sum A _ { m } \sin \beta _ { m }$ is absolutely convergent and the third series (27) is convergent for all values of t. Multiply the mth term of the second series (26) by 2 cos $\alpha _ { m } t$ ； then we obtain a convergent series

$$
2 \sum _ { \ l } A _ { m } \cos \beta _ { m } \sin \alpha _ { m } t \cos \alpha _ { m } t = \sum _ { \ l } A _ { m } \cos \beta _ { m } \sin 2 \alpha _ { m } t .
$$

Hence the third series (27) is convergent for $- 2 \tau < t < + 2 \tau$ .Thus, if the series (26) is convergent in a certain time interval, it is conver-gent in the double time interval. Repeating this procedure, we see that the series is convergent for all values of t.Hence the first series (25) is absolutely convergent for all values of $t$ if it is absolutely convergent for a certain time interval, however small.

The convergence may be uniform.A series $\textstyle \sum _ { m } f _ { m } ( x )$ is said to be uniformly convergent in an interval $\pmb { B }$ ， if for a given $\varepsilon$ there exists a number $N = N ( \varepsilon )$ independent of $x$ ，such that the inequality

$$
| f _ { n + 1 } ( x ) + f _ { n + 2 } ( x ) + \cdots + f _ { n + k } ( x ) | < \varepsilon
$$

is valid for $n > N$ and for $k \geq 1$ for all $x$ in $\pmb { B }$ (Knopp,1931; Rogosinski, 1930). If $\textstyle \sum f _ { n } ( x )$ is uniformly convergent and $g ( x )$ is bounded, then $\textstyle \sum g ( x ) f _ { n } ( x )$ is uniformly convergent. If $\textstyle \sum | f _ { n } ( x ) |$ is uniformly convergent and $g _ { n } ( x )$ is uniformly bounded, then $\sum g _ { n } ( x ) f _ { n } ( x )$ is uniformly convergent. Functions $g _ { n } ( x )$ are said to be uniformly bounded if $m$ and $G$ exist such that $| g _ { n } ( x ) | < G$ for $n > m$ and for all $x$ .If $\textstyle \sum f _ { n } ( x )$ is uniformly convergent and $f _ { n } ( x )$ is continuous at $x _ { 0 }$ ，then $\begin{array} { r } { F ( x ) = \sum f _ { n } ( x ) } \end{array}$ is continuous at $x _ { 0 }$ ，and there exists the term-by-term limit

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } \sum _ { n = 0 } ^ { \infty } f _ { n } ( x ) = \sum _ { n = 0 } ^ { \infty } \operatorname* { l i m } _ { x \to x _ { 0 } } f _ { n } ( x ) .
$$

If a series is uniformly convergent and each of its terms is integrable, then $F ( x )$ is also integrable and can be integrated term by term.If each term of $\Sigma f _ { n } ( x )$ is differentiable and $\textstyle \sum d f _ { n } ( x ) / d x$ is uniformly convergent,and if $\textstyle \sum f _ { n } ( x )$ is uniformly convergent at least at one point, then it is uniformly convergent everywhere,and the derivative of $\pmb { F } ( \pmb { x } )$ is $\begin{array} { r } { d F ( x ) / d x = \sum d f _ { n } ( x ) / d x . } \end{array}$ ，that is, the series can be differentiated term by term.

Now in the series of celestial mechanics, if the error committed by truncating the series at the mth term remains smaller than a certain value $\rho _ { m }$ for all $t _ { i }$ and $\rho _ { \pi }$ depends only on $_ m$ and tends to zero for $m \to \infty$ , then the convergence may be uniform.It may happen that a series is absolutely convergent but not uniformly convergent. If the series (27) is absolutely convergent, then the series $\sum A _ { m }$ sin $\beta _ { m }$ ，and consequently $\sum | A _ { m } \sin \beta _ { m } | ;$ ，isalso absolutely convergent. The remainder of the series (27) is smaller than the remainder $\rho _ { m }$ ，which tends to zero,of the series $\sum | A _ { m } \sin \beta _ { m } |$ .Hence the series (27) can be convergent only uniformly.

However, the series

$$
2 \sin { \frac { t } { 3 } } + 4 \sin { \frac { t } { 9 } } + \cdots + 2 ^ { n } \sin { \frac { t } { 3 ^ { n } } } + \cdots
$$

is convergent absolutely for all $t$ but not uniformly.Write the series (26) in the form

$$
\sum C _ { m } \sin \alpha _ { m } t = \sum C _ { p } \sin \alpha _ { p } t + \sum C _ { q } \sin \alpha _ { q } t ,
$$

$$
C _ { m } = A _ { m } \cos { \beta _ { m } } ,
$$

where the first member on the right-hand side of this equation contains all terms whose coefficients $\alpha _ { p }$ are greater than a given $\lambda$ and the second member contains all terms whose coefficients are smaller than . The necessary and sufficient condition for the convergence is that the two series $\sum | C _ { p } |$ and $\sum \vert C _ { q } \alpha _ { q } \vert$ be convergent. Thus the series (26) can be convergent,even though the series $\sum \vert C _ { q } \vert$ is divergent or even though the coefficients $C _ { q }$ can increase without limit. Take for example the differential equation for the variation of Keplerian elements

$$
\frac { d \alpha } { d t } = F ,
$$

where $\pmb { F }$ is a trigonometric series of $t$ whose coefficients depend on the Keplerian elements.As a first approximation, neglecting the squares of the disturbing masses,we have

$$
\delta \alpha = \int _ { 0 } ^ { t } F \ d t .
$$

The right-hand member consists of a secular term and a trigonometric series.For an incommensurable ratio of the mean motions the series is nonuniformly convergent. In any interval, however small, there are an infinite number of values of this ratio for which the series is nonuniformly convergent and an infinite number of values of the ratio for which the series is uniformly convergent (Section 15.4； see Birkhoff, 1921).

When a function $\phi ( t )$ can be represented by a uniformly convergent trigonometric series,its absolute value $| \phi ( t ) |$ remains finite for all $t .$ If the convergence is not uniform, the situation is not the same.We can only prove that $\phi ( t ) / t$ tends to zero as $t$ increases indefinitely. If $\phi ( t )$ is not uniformly convergent, but the series obtained by the term-by-term differentiation of $\phi ( t )$ is uniformly convergent, then the series represents the derivative $d \phi ( t ) / d t$ and the ratio $\phi ( t ) / t$ tends to zero as $t$ increases indefinitely.In fact, let $\sigma _ { q }$ be the sum of the first $q$ terms of the series $\phi ( t )$ ，then $\phi = \sigma _ { q } + \rho _ { q }$ ， $| \sigma _ { q } | < s _ { q }$ ， $| d \rho _ { q } / d t | < r _ { q }$ ，where $s _ { q }$ and $r _ { q }$ are constants depending only on $\pmb q$ By hypothesis, $q$ can be taken sufficiently large to make $r _ { q }$ as small as we please. Thus $| \phi ( t ) |$ $< s _ { q } + r _ { q } t$ .The limit of $| \phi ( t ) | / t$ is thus smaller than $r _ { q }$ for an infinite $t$ and hence is zero,since $r _ { q }$ can be taken as small as we please.

The same is true when $\phi ( t )$ is the sum of two series,of which one is uniformly convergent and the derivative of the other is uniformly convergent.Consider, for example, the first series (25) in the form

$$
\phi ( t ) = \sum B _ { n } \cos \alpha _ { n } t + \sum C _ { p } \sin \alpha _ { p } t + \sum C _ { q } \sin \alpha _ { q } t ,
$$

where the coefficients $\alpha _ { p }$ are all larger than $\gimel$ and the coefficients $\alpha _ { q }$ are all smaller than . The first two members on the right hand side are uniformly convergent and the derivative of the third member is uniformly convergent. For a second example,take the series

$$
\phi _ { 1 } ( t ) = \sum C _ { q } \sin ^ { 2 } \alpha _ { q } t ,
$$

where $\sum \vert C _ { q } \vert$ is divergent and $\sum \vert C _ { q } \alpha _ { q } \vert$ is convergent. The derivative

$$
\frac { d \phi _ { 1 } } { d t } = \sum C _ { q } \alpha _ { q } \sin 2 \alpha _ { q } t
$$

is uniformly convergent. In both these examples the ratios $\phi / t$ and $\phi _ { 1 } / t$ tend to zero for $t$ infinite. Put

$$
\psi ( t ) = \int _ { 0 } ^ { t } \phi ( t ) \sin \alpha _ { m } t \cdot d t , \qquad \theta ( t ) = \int _ { 0 } ^ { t } \phi ( t ) \cos \alpha _ { m } t \cdot d t ,
$$

and suppose that the series $\phi ( t )$ contains terms in sin $\alpha _ { m } t$ and cos $\alpha _ { m } t$ ， and that $\alpha _ { m }$ is larger than $\lambda$ ， so that its coefficient is included in those denoted by $\alpha _ { p }$ . Thus

$$
\begin{array} { c l } { { } } & { { 2 \psi ( t ) = 2 \cdot \displaystyle \sum _ { \alpha _ { n } } \frac { B _ { n } } { \alpha _ { n } \pm \alpha _ { m } } \sin ^ { 2 } \frac { \alpha _ { n } \pm \alpha _ { m } } { 2 } t } } \\ { { } } & { { ~ + \displaystyle \sum _ { \alpha _ { m } \pm \alpha _ { p } } \frac { \mp C _ { p } } { \alpha _ { m } \pm \alpha _ { p } } \sin { ( \alpha _ { m } \pm \alpha _ { p } ) } t + C _ { m } t } } \\ { { } } & { { ~ + \displaystyle \frac { \cos { \alpha _ { m } t } } { \alpha _ { m } } \sum _ { q } \sin { \alpha _ { q } t } } } \\ { { } } & { { ~ + \displaystyle \sum _ { \alpha _ { m } } \frac { \mp C _ { q } \alpha _ { q } } { \alpha _ { m } ( \alpha _ { q } \pm \alpha _ { m } ) } \sin { ( \alpha _ { m } \pm \alpha _ { q } ) } t . } } \end{array}
$$

The derivatives of the series on the right-hand side are all uniformly convergent. If we divide any of the terms, except the secular term,

by $t _ { i }$ ，then the limit of the quotient is zero for $t$ infinite. Hence

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { | \psi | } { t } } = { \frac { | C _ { m } | } { 2 } } .
$$

Similarly

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { | \theta | } { t } } = { \frac { | B _ { m } | } { 2 } } .
$$

Thus it is impossible for the absolute value $| \phi ( t ) |$ to remain constantly smaller than $| C _ { m } | / 2$ or $| B _ { m } | / 2$

From this result we can draw an important conclusion. Among the series of the form of the series (26) there are some,however conver-gent they may be, for which the coefficients become larger than any assigned number. The series $\sum | A _ { n } \sin \beta _ { n } | .$ ，whose nth coefficient is equal to $2 ^ { n }$ ， is an example. The sum can increase with time beyond all limits.Hence, in order to prove the stability of a dynamical system, it is not suffcient to prove that the mutual distances can be represented by convergent trigonometric series, but it is necessary that the convergence be uniform.

Another conclusion is that a trigonometric series can never be zero unless all coeffcients are zero, since the series cannot remain always smaller than $_ { 1 / 2 }$ of any one of the coefficients in absolute value. Furthermore a single function cannot be represented by two different trigonometric series，unless the difference of the two series is zero without all coefficients being equal to zero. It may happen that a trigonometric series representing a particular function in a given interval represents a totally different function in another interval. The Lindstedt series would represent the mutual distance for all values of $t$ if we admit that the series is absolutely convergent (Section 14.5), since the series satisfies the differential equation. This method of proof by Poincaré was later criticized by Wintner (1929 ； Section 15.8).

If the series is semiconvergent instead of uniformly convergent (Section 14.3), several circumstances may arise.Let

$$
s _ { 1 } + s _ { 2 } + \cdots + s _ { n } + \cdots
$$

be an absolutely convergent series,each of whose terms is itself an absolutely convergent trigonometric series. It may happen that we cannot alter the order of arrangement of the terms without changing the convergence,possibly into semiconvergence.Such a series is not met in the application of the method of successive approximation.Neglecting the squares of the disturbing masses， we obtain a trigonometric series $s _ { 1 }$ . In the second-order calculation, taking the squares of the disturbing masses into account but neglecting the cubes,we obtain another trigonometric term $s _ { 2 }$ ，and so on. The series obtained in this way $s _ { 1 } + s _ { 2 } + \cdots + s _ { n } + \cdots$ would be convergent if the method could give an indefinite approximation.This is how Lindstedt worked out his theory (Section 14.5). Such series can be convergent for a small time interval but cannot be convergent for all values of $t .$ For example, take the series

$$
2 \sin ^ { 2 } t - 4 \sin ^ { 4 } t + 8 \sin ^ { 6 } t + \cdot \cdot \cdot + ( - 1 ) ^ { n + 1 } 2 ^ { n } \sin ^ { 2 n } t + \cdot \cdot \cdot .
$$

Each term of this series can be writen in the form of a trigonometric series which is convergent only if

$$
t < \log { \frac { 1 + { \sqrt { 3 } } } { \sqrt { 2 } } } .
$$

The Lindstedt series is semiconvergent but not absolutely convergent (Section 15.15).Hence it represents the mutual distances only for a a limited time interval.

Thus the convergence of a trigonometric series may or may not be absolute,If it is absolute, then it is absolutely convergent for all values of t.If it is not absolutely convergent but only semiconvergent, then the semiconvergent character subsists only for a limited time interval.

If convergence is absolute, then it may be either uniform or nonuniform.If it is uniform,then the function represented by the series remains smaller than a certain limit. Otherwise,the function can increase without limit.Furthermore,a function can be represented uniquely by a single absolutely convergent trigonometric series (Section 15.9).

Denjoy (1921,1941, 1949,1954) presented a new concept of totalization for determining the coefficients of trigonometric series for nonintegrable functions.The problem is to derive the convergent trigonometric series whose sum is equal to .a given function $f ( \theta )$ ，finite and periodic in $\theta$ with period $2 \pi$ . Denjoy considered the second variation

$$
\begin{array} { l } { { V ( F , a , b , c ) = F ( a ) ( c - b ) + F ( b ) ( a - c ) + F ( c ) ( b - a ) , } } \\ { { \displaystyle { \omega ( F , x , h , k ) = V R ( F , x - k , x , x + h ) } } } \\ { { \displaystyle { \quad = \frac { 2 } { h + k } \Big [ \frac { F ( x + h ) - F ( x ) } { h } - \frac { F ( x ) - F ( x - k ) } { k } \Big ] . } } } \end{array}
$$

The superior and the inferior limits of $\omega ( F , x , h , k )$ are denoted by $\Delta ^ { \prime \prime } F ( x )$ ， $\delta ^ { \prime \prime } F ( x )$ ，respectively，where $h , k \to 0$ ，and are called the

superior and the inferior second mixed derivative, respectively，of $\pmb { F } ( \pmb { x } )$ at $x$ . When these two derivatives coincide they are called the second mixed derivative.

Let

$$
{ \frac { a _ { 0 } } { 2 } } + a _ { 1 } \cos \theta + b _ { 1 } \sin \theta + \cdot \cdot \cdot + a _ { n } \cos n \theta + b _ { n } \sin n \theta \ .
$$

$$
A _ { n } = a _ { n } \cos n \theta + b _ { n } \sin n \theta = \rho _ { n } \sin ( n \theta + \phi _ { n } ) _ { ; }
$$

$$
\frac { d B _ { n } } { d \theta } = n A _ { n } , \qquad \frac { d A _ { n } } { d \theta } = - n B _ { n } .
$$

Denjoy obtained the coefficients of this expansion，which, if it exists and if the convergence for each value of $\theta$ is known, represents as its sum the given function $f ( \theta )$ which is finite for all $\theta$ and periodic with period $2 \pi$ . It is known that the sum of the most general conver-gent trigonometric series is not always integrable in Lebesgues's sense.

A linear functional is a linear transformation whose range is in the coefficient field. A functional of $x ( t )$ in the interval $[ a , b ]$ is in general a quantity $z$ whose value is determined by the values of the function $x ( t )$ supposed known as $t$ varies between $_ { a }$ and $^ { b }$ ，this function being arbitrarily under the restriction which limits the functional field of definition or of the existence of $z$ ，such as in the variational problems and in the boundary value problems connected with integral equations (Volterra and Péres,1936； Kantorovich and Akimov, 1964; Yosida, 1966; Section 16.18).

The simple total $T ( \boldsymbol { f } , \alpha , \beta )$ is a linear functional with argument $f$ a function of a variable defined in the segment $\alpha , \beta$ . The functional $T ( \boldsymbol { f } , \alpha , \beta )$ does not always correspond to an arbitrary function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ defined in the interval $\alpha , \beta$ A function $f _ { : }$ ，for which the total $T ( f , \alpha , \beta )$ has a definite value and which is regarded as constituting the field of existence of a functional $T ( \boldsymbol { f } , \alpha , \beta )$ in the given interval $\alpha , \beta$ ,is said to be totalizable on the interval $\alpha , \beta$ If $f$ is totalizable on $\alpha , \beta$ then $f$ is simply totalizable in any interval $\alpha ^ { \prime } , \beta ^ { \prime }$ contained in $\alpha , \beta$ The functional $T ( f , \alpha , \beta )$ satisfies the same identity as the simple variation in the interval $\alpha , \beta$ For any $\alpha , \beta , \gamma$ in the interval on which $f$ is defined and totalizable we have the identity

$$
\begin{array} { c } { { \displaystyle { \dot { \left( f , \alpha , \alpha \right) } = 0 , \qquad T ( f , \alpha , \beta ) + T ( f , \beta , \alpha ) = 0 , } } } \\ { { \displaystyle { T ( f , \alpha , \beta ) + T ( f , \beta , \gamma ) + T ( f , \gamma , \alpha ) = 0 . } } } \end{array}
$$

If the simple total $T ( \boldsymbol { f } , \alpha , \beta )$ exists, then the total $T ( \boldsymbol { f } , \boldsymbol { x } , \boldsymbol { x } ^ { \prime } )$ is a con-

tinuous function of $x$ and $x ^ { \prime }$ varying on the interval $\alpha , \beta$ ·

# 15.IISOLUTION BY TRIGONOMETRIC SERIES

Cauchy proved that the integral of a differential equation without singularity with the independent variable $t$ can be expanded in convergent series in powers of $t - t _ { 0 }$ ，where $t _ { 0 }$ is the initial epoch.But the series remains convergent only for small values of $t - t _ { 0 }$ (Sections 10.42-1O.43).In celestial mechanics a trigonometric series is often employed instead of such a power series.Consider

$$
{ \frac { d x _ { 1 } } { X _ { 1 } } } = { \frac { d x _ { 2 } } { X _ { 2 } } } = \cdots = { \frac { d x _ { n } } { X _ { n } } } = { \frac { d s } { X _ { 1 } ^ { 2 } + X _ { 2 } ^ { 2 } + \cdots + X _ { n } ^ { 2 } + 1 } } ,
$$

where $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ are polynomials in $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ ，and $\pmb { s }$ is an auxiliary variable.Poincaré (1882a） proved that a number $_ { \alpha }$ can be found such that $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ are represented by series proceeding in powers of $( e ^ { \alpha s } - 1 ) / ( e ^ { \alpha s } + 1 )$ uniquely for all real values of $\pmb { s }$ We shall return to this in Sections 17.16 and 22.8. The coefficients are rational functions of $_ { \alpha }$ ， the coefficients of the polynomials $X _ { i }$ ，and the initial values of $x _ { i }$

Poincaré (1885) discussed whether the function defined by a trigonometric series

$$
\sum A \sin \alpha t
$$

tends to infinity or oscillates with increasing amplitude.In the latter case we can find a value of $t > t _ { 0 }$ ， such that the function defined by the series takes any value whatsoever, irrespective of $t _ { 0 }$ . Poincaré gave two examples of such a function.Let

$$
F ( t ) = \sin t + A \sin { \frac { t } { 2 } } + A ^ { 2 } \sin { \frac { t } { 2 ^ { 2 } } } + \cdots + A ^ { n } \sin { \frac { t } { 2 ^ { n } } } + \cdots .
$$

If $A < 2$ ，this series is convergent, but the convergence is not uniform if $A > 1$ . Then

$$
F ( 2 t ) = A F ( t ) + \sin 2 t .
$$

Hence

$$
F ( 2 t ) > A F ( t ) - 1 .
$$

Since

$$
\sin t > t - \frac { t ^ { 3 } } { 6 } , \qquad \sin \frac { t } { 2 ^ { n } } > \frac { t } { 2 ^ { n } } \left( 1 - \frac { t ^ { 2 } } { 6 } \right)
$$

for $t > 0$ ，we have

$$
{ \cal F } ( t ) > \Big ( t - { \frac { t ^ { 3 } } { 6 } } \Big ) { \frac { 1 } { 1 - ( A / 2 ) } } .
$$

Put $t _ { 0 } < \sqrt { 3 } / 2$ ; then

$$
t _ { 0 } - \frac { 8 t _ { 0 } ^ { 3 } } { 6 } = B > 0 .
$$

If $t _ { 0 } < . t < 2 t _ { 0 } ,$ ，then from the inequality (28a) we obtain

$$
F ( t ) > { \frac { B } { 1 - ( A / 2 ) } } .
$$

Take $\theta > 1 > 0$ and put

$$
A = \frac { 2 + ( 2 \theta / B ) } { 2 + ( \theta / B ) } , \qquad \frac { \theta } { A - 1 } = \frac { 1 } { A - 1 } + h \qquad ( h > 0 ) ;
$$

then

$$
1 < A < 2 .
$$

From the inequalities (28) and (28a) we obtain

$$
\begin{array} { r l } { F ( t ) > \displaystyle \frac { 1 } { A - 1 } + h } & { { } \quad ( t _ { 0 } < t < 2 t _ { 0 } ) , } \\ { F ( t ) > \displaystyle \frac { 1 } { A - 1 } + A h } & { { } \quad ( 2 t _ { 0 } < t < 4 t _ { 0 } ) , } \\ { F ( t ) > \displaystyle \frac { 1 } { A - 1 } + A ^ { 2 } h } & { { } \quad ( 4 t _ { 0 } < t < 8 t _ { 0 } ) , } \\ { . . . } \end{array}
$$

$$
F ( t ) > \frac { 1 } { A - 1 } + A ^ { n } h ( 2 ^ { n } t _ { 0 } < t < 2 ^ { n + 1 } t _ { 0 } ) ,
$$

Hence $\pmb { F } ( t )$ is always positive and tends to infinity.

Next take

$$
\begin{array} { l } { { F ( t ) = \displaystyle \sin t - { \cal A } \sin \frac { t } { 2 } + { \cal A } ^ { 2 } \sin \frac { t } { 4 } - \cdots } } \\ { { \mathrm { } } } \\ { { \mathrm { } + ( - { \cal A } ) ^ { n } \sin \frac { t } { 2 ^ { n } } \pm \cdots . } } \end{array}
$$

then we have

$$
F ( 2 t ) = - A F ( t ) + \sin { 2 t } .
$$

Hence we get

$$
- A F ( t ) - 1 < F ( 2 t ) < - A F ( t ) + 1 .
$$

If $1 < A < 2$ ， the series is convergent,but the convergence is not uniform.Hence we can find a value of $t$ such that $F ( t )$ is as large as we please in absolute value. Hence $F ( t )$ can become either positively or negatively infinite.

In the first example we have

$$
F ( t ) > { \frac { 1 } { A - 1 } } + h ,
$$

where $h$ is positive and infinite. Then, since

$$
F ( 2 t ) < - \frac { 1 } { A - 1 } - A h ,
$$

it follows that $F ( 2 t )$ becomes negative and infinite. In the second example, we have

$$
F ( t ) < - \frac { 1 } { A - 1 } - h ,
$$

and

$$
F ( 2 t ) > \frac { 1 } { A - 1 } + A h .
$$

Hence $F ( 2 t )$ is positively infinite.Thus $\pmb { F } ( t )$ becomes alternately positively and negatively infinite.The value of this function constantly oscillates and the amplitude of the oscillation increases to infinity；in other words, $\pmb { F } ( t )$ takes any assigned value an infinite number of times We call such a function oscillatory (Section 22.22).

# 15.12ELEVATION OF THE DEGREE OF FORMAL CONVERGENCE

If a series,although it may not be convergent in strict mathematical sense,has its terms decreasing in magnitude in proceeding to higherorder terms, then the series is said to be formally convergent. In order to compute the numerical value of such a series it is convenient if the successive terms decrease in magnitude as rapidly as we desire.The rapidity of decrease in magnitude of successive terms is expressed by the degree of formal convergence.We consider artifices for elevating the degree of formal convergence.

Gyldén (1867） represented the expansions of $\theta$ ，sin $\mu \theta$ and cos μ for an irrational $\theta$ ，by formally rapidly convergent series proceeding with multiples of $\theta$ ，where $\theta$ contains two arguments $g$ and $g ^ { \prime }$ .He transformed the two arguments by writing $g ^ { \prime } = \mu g$ . Consider

$$
\psi = \sum _ { i } \sum _ { j } \{ \alpha _ { i j } \cos { ( i g - j \mu g ) } + \beta _ { i j } \sin { ( i g - j \mu g ) } \} ,
$$

where $\pmb { \mu }$ is the ratio of the mean motions. If cos jμg and sin jμg are represented by series of the form

$$
\begin{array} { r l r } & { } & { p _ { 0 } + p _ { 1 } \cos g + p _ { 2 } \cos 2 g + \cdots } \\ & { } & { + q _ { 1 } \sin g + q _ { 2 } \sin 2 g + \cdots , } \end{array}
$$

then $\psi$ can be written

$$
\begin{array} { c } { { \psi = A _ { 0 } + A _ { 1 } \cos g + A _ { 2 } \cos 2 g + \cdot \cdot \cdot } } \\ { { + B _ { 1 } \sin g + B _ { 2 } \sin 2 g + \cdot \cdot \cdot . . } } \end{array}
$$

If $\pmb { g }$ varies within a certain limited interval $k \pi / 2$ and $( k + 2 ) \pi / 2$ ，then the coefficients $p , q , A , B$ may be approximately constant. In order that the expansion be valid for the values of $g$ outside this interval, the coefficients must be expressed as functions of $k$ ， which may be a positive or a negative integer.Then the coefficients of the expansion for $\psi$ may be functions of $k$ ，but may be considered as approximately constant during one half of the period of revolution of the disturbed planet.This possibility depends essentially on the degree of formal convergence of the series.

Let

$$
\begin{array} { c } { { \alpha _ { 2 n } ^ { \langle \rangle } = \displaystyle \frac { 1 } { n } \displaystyle \frac { ( i - n + 1 ) ( i - n + 2 ) \cdot \cdot \cdot \cdot \cdot i } { ( i + 1 ) ( i + 2 ) \cdot \cdot \cdot \cdot ( i + n ) } , } } \\ { { \beta _ { 2 n + 1 } ^ { \langle \rangle } = \displaystyle \frac { 4 } { \pi } \sin \frac { 2 n + 1 } { 2 } \pi \cdot 2 ^ { \varepsilon \cdot } } } \\ { { \times \displaystyle \frac { ( - 1 ) ^ { i } ( 1 \cdot 2 \cdot \cdot \cdot \cdot \cdot \cdot i ) ^ { 2 } } { ( 2 n + 2 i + 1 ) ( 2 n + 2 j - 1 ) \cdot \cdot \cdot \cdot ( 2 n + 3 ) ( 2 n + 1 ) ^ { 2 } ( 2 n - 2 k ) } , } } \\ { { \times \displaystyle \frac { 1 } { \dots \cdot ( 2 n - 2 i + 3 ) ( 2 n - 2 i + 1 ) ( 2 n - 2 i + 2 i - 3 ) ( 2 n - 2 i + 1 ) ^ { 2 } ( 2 n - 2 k ) } , } } \end{array}
$$

then we have

$$
\cos { \frac { 2 \lambda } { \pi } } \theta = \cos { \lambda \kappa ( i , \lambda ) }
$$

$$
\sin { \frac { 2 \lambda } { \pi } } \theta
$$

$$
\begin{array} { r l } { \displaystyle } & { = - \left( \frac { 2 \lambda } { \pi } \right) \cos \lambda \kappa ( i , \lambda ) \cdot \sum _ { n = 1 } ^ { i } \frac { \alpha _ { 2 n } ^ { ( i ) } } { 1 - [ 2 \lambda / ( 2 n \pi ) ] ^ { 2 } } \sin 2 n \theta } \\ & { + \left( \frac { 2 \lambda } { \pi } \right) \cos \lambda \kappa ( i , \kappa ) \cdot \sum _ { n = 0 } ^ { \infty } \frac { \beta _ { 2 n + 1 } ^ { ( i ) } } { 1 - [ 2 \lambda / ( ( 2 n + 1 ) \pi ) ] ^ { 2 } } \sin { ( 2 n + 1 ) } \theta . } \end{array}
$$

If we put $\lambda = 0$ ，then

$$
\theta = - \sum _ { n = 1 , } ^ { i } \alpha _ { 2 n } ^ { ( i ) } \sin 2 n \theta + \ \sum _ { n = 0 } ^ { \infty } \beta _ { 2 n + 1 } ^ { ( i ) } \sin { ( 2 n + 1 ) } \theta .
$$

These expressions hold only for $- \pi / 2 \leq \theta \leqq \pi / 2$ .Both $_ n$ and $_ i$ are positive integers, and $_ i$ can be taken arbitrarily. If $i = 0$ 01 $i = \infty$ ， then the series reduces to a known expansion which cannot be employed practically because of the slow formal convergence of the $\beta$ -coefficients.But, if we take $i = 1 , 2 , 3$ ，or 4,then the coeffcients decrease in magnitude so rapidly that these four terms are sufficient for practical purpose.

Put

$$
T _ { n } = \frac { \cos \lambda } { 1 - [ 2 \lambda / ( ( 2 n + 1 ) \pi ) ] ^ { 2 } } , \qquad U _ { n } = \frac { \kappa ( i , \lambda ) } { 1 - [ 2 \lambda / ( 2 n \pi ) ] ^ { 2 } } ,
$$

$$
c _ { 0 } = \cos { \lambda } \cdot \kappa ( i , \lambda ) ,
$$

$$
s _ { 2 \pi } = - \frac { 2 \lambda } { \pi } \cos \lambda \cdot \alpha _ { 2 n } ^ { ( i ) } U _ { n } , ~ c _ { 2 \pi } = \frac { 1 } { 2 n } \frac { 2 \lambda } { \pi } s _ { 2 \pi } ,
$$

$$
s _ { 2 n + 1 } = \frac { 2 \lambda } { \pi } \kappa ( i , \lambda ) \beta _ { 2 n + 1 } ^ { ( i ) } T _ { n } , \qquad c _ { 2 n + 1 } = \frac { 1 } { 2 n + 1 } \frac { 2 \lambda } { \pi } s _ { 2 n + 1 } ;
$$

then we get

$$
\cos { \frac { 2 \lambda } { \pi } } \theta = c _ { 0 } + c _ { 1 } \cos \theta + c _ { 2 } \cos 2 \theta + \cdot \cdot \cdot ,
$$

$$
\sin { \frac { 2 \lambda } { \pi } } \theta = s _ { 1 } \sin \theta + s _ { 2 } \sin 2 \theta + \cdot \cdot \cdot
$$

$$
\left( - { \frac { \pi } { 2 } } \leq \theta \leq { \frac { \pi } { 2 } } \right) .
$$

If we put $\theta = g - k \pi$ ，then

$$
- \sin 2 k \lambda [ s _ { 2 } \sin 2 g + s _ { 4 } \sin 4 g + \cdot \cdot \cdot
$$

$$
+ \cos k \pi ( s _ { 1 } \sin g + s _ { 3 } \sin 3 g + \cdot \cdot \cdot ) ] ,
$$

$$
\begin{array} { c } { { \pi } } \\ { { + \cos k \pi ( c _ { 1 } \cos g + c _ { 3 } \cos 3 g + \cdot \cdot \cdot ) ] } } \\ { { + \cos 2 k \lambda [ s _ { 2 } \sin 2 g + s _ { 4 } \sin 4 g + \cdot \cdot \cdot } } \\ { { + \cos k \pi ( s _ { 1 } \sin g + s _ { 3 } \sin 3 g + \cdot \cdot \cdot ) ] } } \\ { { \left( - \frac { \pi } { 2 } \le g - k \pi \le \frac { \pi } { 2 } \right) . } } \end{array}
$$

Callandreau (1882),in discussing the perturbation of an asteroid according to Gyldén's theory (Sections 10.18-10.20), considered simi-. lar expansions.He applied them to the asteroid 1O3 Hero.

In the interval $- \pi < x < \pi$ the series

$$
x = 2 ( \sin x - { \frac { 1 } { 2 } } \sin 2 x + { \frac { 1 } { 3 } } \sin 3 x - { \frac { 1 } { 4 } } \sin 4 x + \cdot \cdot \cdot )
$$

converges very slowly. But for the interval $- \pi / 2 < x < \pi / 2$ Gylden invented a representation by a more rapidly formally convergent series,and indeed not a unique representation. Put

$$
g = n t + c = \varepsilon - e \sin \varepsilon , \mu = \frac { n ^ { \prime } } { n } ,
$$

$$
g ^ { \prime } = n ^ { \prime } t + c ^ { \prime } = c ^ { \prime } - \mu c + \mu \varepsilon - \mu e \sin \varepsilon ,
$$

$$
\left( - \frac { \pi } { 2 } < \varepsilon < \frac { \pi } { 2 } \right) ,
$$

or

$$
\begin{array} { c } { { g ^ { \prime } = c ^ { \prime } - \mu c + \mu m \pi + \mu ( \varepsilon - m \pi ) - \mu e \sin \varepsilon } } \\ { { { } } } \\ { { ( ( m - \frac 1 2 ) \pi < \varepsilon < ( m + \frac 1 2 ) \pi ) . } } \end{array}
$$

Charlier (1886) modified Gyldén's formulas without dividing the interval. Gylden's method is based on the introduction of an auxiliary function $\cos ^ { 2 i } \theta$ .Let $\phi ( x )$ be the function to be expanded, such that

$$
\phi ( x ) = \sum _ { m = 0 } ^ { \infty } \alpha _ { m } \cos m x \qquad ( 0 \leq x \leq \pi ) ,
$$

where

$$
{ \frac { \pi } { 2 } } \alpha _ { m } = \int _ { 0 } ^ { \tau } \phi ( x ) \cos m x \cdot d x \qquad ( m = 1 , 2 , \ldots ) ,
$$

in which $\textstyle { \frac { 1 } { 2 } } \alpha _ { 0 }$ should be taken instead of $\alpha _ { 0 }$ for $m = 0$ . Consider an auxiliary function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ defined by

$$
f ( x ) = \phi ( x ) - \sum _ { n = 1 } ^ { 2 ^ { r } } 2 \beta _ { n } \sin n x ,
$$

where the coefficients $\beta _ { \pi }$ .and the integer $r$ should be chosen so that the series representing $f ( x )$ converges rapidly，although formally. Let

$$
\begin{array} { l l } { { f ( x ) = \displaystyle \sum _ { m = 0 } ^ { \infty } A _ { m } \cos m x } } & { { ( 0 \leq x \leq \pi ) , \hfill } } \\ { { \displaystyle \frac { \pi } { 2 } A _ { m } = \displaystyle \int _ { 0 } ^ { \pi } f ( x ) \cos m x \cdot d x . } } & { { } } \end{array}
$$

Substituting the series for $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ we obtain

$$
{ \frac { \pi } { 2 } } A _ { m } = { \frac { \pi } { 2 } } \alpha _ { m } + \int \sum _ { n = 1 } ^ { 2 r } \beta _ { n } \Bigl [ { \frac { \cos { ( n + m ) x } } { n + m } } + { \frac { \cos { ( n - m ) x } } { n - m } } \Bigr ] _ { 0 } ^ { \pi } ,
$$

where terms corresponding to even values of $n \pm m$ vanish．The remaining terms are

$$
\frac { \pi } { 2 } A _ { m } = \frac { \pi } { 2 } \alpha _ { m } + \sum _ { n = 1 } ^ { 2 r } \frac { 4 n \beta _ { n } } { m ^ { 2 } - n ^ { 2 } } .
$$

If $_ { m }$ is even， then $_ n$ takes odd values from 1 to $2 r - 1$ ， and viceversa.

By Fourier's theorem we have

$$
x = { \frac { \pi } { 2 } } - { \frac { 2 } { \pi } } \cdot \sum _ { m = 1 } ^ { \infty } { \frac { 2 } { m ^ { 2 } } } \cos m x \qquad ( m = 1 , 3 , 5 , \ldots ) .
$$

This series converges very slowly. In this case $( \pi / 2 ) \alpha _ { m } = - 2 / m ^ { 2 }$ .Put $\ 8 n \beta _ { 2 n } = \gamma _ { n }$ ; then

$$
{ \frac { \pi } { 2 } } A _ { m } = - { \frac { 2 } { m ^ { 2 } } } + { \frac { \gamma _ { 1 } } { m ^ { 2 } - 2 ^ { 2 } } } + { \frac { \gamma _ { 2 } } { m ^ { 2 } - 4 ^ { 2 } } } + \cdots + { \frac { \gamma _ { r } } { m ^ { 2 } - 4 r ^ { 2 } } }
$$

The coefficients $\gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { r }$ can be chosen arbitrarily.Equate all coefficients to zero except the pth ； then

$$
\frac { \pi } { 2 } A _ { m } = - \frac { 2 } { m ^ { 2 } } + \frac { \gamma _ { p } } { m ^ { 2 } - 4 p ^ { 2 } } = \frac { ( \gamma _ { p } - 2 ) m ^ { 2 } + 8 p ^ { 2 } } { m ^ { 2 } ( m ^ { 2 } - 4 p ^ { 2 } ) } .
$$

Assign to $\gamma _ { p }$ such a value that the coefficient of $m ^ { 2 }$ in the numerator vanishes, i.e.,

$$
\gamma _ { p } = 2 , \qquad \beta _ { 2 p } = \frac { 1 } { 4 p } ,
$$

then we have

$$
{ \frac { \pi } { 2 } } A _ { m } = { \frac { 8 p ^ { 2 } } { m ^ { 2 } ( m ^ { 2 } - 4 p ^ { 2 } ) } } .
$$

Hence

$$
x = \frac { \pi } { 2 } + \sum _ { m = 1 } ^ { \infty } \frac { 8 p ^ { 2 } } { m ^ { 2 } ( m ^ { 2 } - 4 p ^ { 2 } ) } \cos m x + \frac { 1 } { 2 p } \sin 2 p x .
$$

This series converges more rapidly,although formally, than the above series for $x$

If an arbitrary number of the coefficients are equated to zero and we choose the remaining coefficients so that the series,although formally,converges more rapidly, then we arrive at a much more interesting result. We have

$$
\begin{array} { l } { { \frac { \pi } { 2 } A _ { m } = \frac { - 2 \Pi ^ { \scriptscriptstyle ( 0 ) } + \gamma _ { 1 } \Pi ^ { \scriptscriptstyle ( 1 ) } + \cdot \cdot \cdot + \gamma _ { r } \Pi ^ { \scriptscriptstyle ( r ) } } { \prod _ { n = 0 } ^ { r } \left( m ^ { 2 } - 4 n ^ { 2 } \right) } , } } \\ { { \Pi ^ { \scriptscriptstyle ( p ) } = \frac { \prod _ { n = 0 } ^ { r } \left( m ^ { 2 } - 4 n ^ { 2 } \right) } { m ^ { 2 } - 4 p ^ { 2 } } . } } \end{array}
$$

Choose the coefficients $\gamma \ \mathsf { s o }$ that the numerator in the expression fol $\pmb { A } _ { m }$ is constant, and arrange the terms in decreasing powers of $_ m$ ：

$$
\Pi ^ { ( p ) } = m ^ { 2 r } + d _ { 1 } ^ { ( p ) } m ^ { 2 r - 2 } + \cdots + d _ { r - 1 } ^ { ( p ) } m ^ { 2 } + d _ { r } ^ { ( p ) } ,
$$

then the numerator takes the form

$$
\sum \limits _ { n = 0 } ^ { r } \delta _ { r - n } m ^ { 2 n } ,
$$

where

$$
\begin{array} { r l } & { \delta _ { 0 } = - 2 + \gamma _ { 1 } + \cdot \cdot \cdot + \gamma _ { r } , } \\ & { \delta _ { 1 } = - 2 d _ { 1 } ^ { ( 0 ) } + \gamma _ { 1 } d _ { 1 } ^ { ( 1 ) } + \cdot \cdot \cdot + \gamma _ { r } d _ { 1 } ^ { ( r ) } , } \\ & { \cdot \cdot \cdot } \\ & { \delta _ { r } = - 2 d _ { r } ^ { ( 0 ) } + \gamma _ { 1 } d _ { r } ^ { ( 1 ) } + \cdot \cdot \cdot + \gamma _ { r } d _ { r } ^ { ( r ) } . } \end{array}
$$

Thus $\gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { r }$ are defined by a system of $r$ linear equations with $\delta _ { 0 } = \delta _ { 1 } = \cdot \cdot \cdot = \delta _ { r - 1 } = 0$ .The solution is

$$
\gamma _ { p } = 2 ( - 1 ) ^ { p - 1 } \frac { D _ { p } } { D _ { 0 } } ,
$$

where

$$
D _ { p } = \left| \begin{array} { l l l l l } { 1 } & { 1 } & { \cdots \cdot 1 } & { 1 } & { \cdots \cdot 1 } \\ { d _ { 1 } ^ { ( 0 ) } } & { d _ { 1 } ^ { ( 1 ) } } & { \cdots \cdot d _ { 1 } ^ { ( p - 1 ) } } & { d _ { 1 } ^ { ( p + 1 ) } \cdot \cdot \cdot d _ { 1 } ^ { ( r ) } } \\ { \cdots \cdot } & { \qquad \cdot \cdot \cdot } \\ { d _ { r - 1 } ^ { ( 0 ) } } & { d _ { r - 1 } ^ { ( 1 ) } \cdot \cdot \cdot d _ { r - 1 } ^ { ( p - 1 ) } } & { d _ { r - 1 } ^ { ( p + 1 ) } \cdot \cdot \cdot d _ { r - 1 } ^ { ( r ) } } \end{array} \right| .
$$

Let $\alpha _ { 0 } , \alpha _ { 1 } , \ldots , \alpha _ { r }$ be $r + 1$ given numbers and denote by

$$
\Pi ^ { ( { p } ) } \left( x - \alpha _ { n } \right)
$$

the product of r factors x - αo,x - α,...,x - αp-1x - αp+1,., $x - \alpha _ { \tau }$ . Put

$$
\Pi ^ { ( p ) } ( x - \alpha _ { n } ) = x ^ { r } + k _ { 1 } ^ { ( p ) } x ^ { r - 1 } + \cdot \cdot \cdot + k _ { r } ^ { ( p ) } ;
$$

then

$$
\Delta _ { p } = \left| \begin{array} { l l l l l } { 1 } & { 1 } & { \cdots \cdot 1 } & { 1 } & { \cdots \cdot 1 } \\ { k _ { 1 } ^ { ( 0 ) } } & { k _ { 1 } ^ { ( 1 ) } } & { \cdots \cdot k _ { 1 } ^ { ( p - 1 ) } } & { k _ { 1 } ^ { ( p + 1 ) } \cdot \cdot \cdot \cdot k _ { 1 } ^ { ( r ) } } \\ { \cdot \cdot \cdot } & { } & { \cdot \cdot \cdot } \\ { k _ { r - 1 } ^ { ( 0 ) } } & { k _ { r - 1 } ^ { ( 1 ) } \cdot \cdot \cdot \cdot k _ { r - 1 } ^ { ( p - 1 ) } } & { k _ { r - 1 } ^ { ( p + 1 ) } \cdot \cdot \cdot \cdot k _ { r - 1 } ^ { ( r ) } } \end{array} \right|
$$

is equal to the product $P _ { p }$ of all differences between the roots $\alpha _ { 0 } , \alpha _ { 1 } ,$ $\dots , \alpha _ { p - 1 } , \alpha _ { p + 1 } , \dots , \alpha _ { r }$ of the algebraic equation (30) of degree $r$ multiplied by $( - 1 ) ^ { r ( r - 1 ) / 2 }$ ,i.e.,

$$
\begin{array} { r l r } {  { \Delta _ { p } = ( - 1 ) ^ { \tau ( \tau - 1 ) / 2 } P _ { p } , } } \\ { P _ { p } = ( \alpha _ { 0 } - \alpha _ { 1 } ) ( \alpha _ { 0 } - \alpha _ { 2 } ) \cdot \cdot \cdot ( \alpha _ { 0 } - \alpha _ { p - 1 } ) ( \alpha _ { 0 } - \alpha _ { p + 1 } ) \cdot \cdot \cdot ( \alpha _ { 0 } - \alpha _ { \tau } } \\ & { } & { \times ( \alpha _ { 1 } - \alpha _ { 2 } ) \cdot \cdot \cdot ( \alpha _ { 1 } - \alpha _ { p - 1 } ) ( \alpha _ { 1 } - \alpha _ { p + 1 } ) \cdot \cdot \cdot ( \alpha _ { 1 } - \alpha _ { \tau } } \\ & { } & { \times \cdot \cdot \cdot } \\ & { } & { \times \cdot \cdot \cdot } \end{array}
$$

Hence we obtain

$$
\frac { \Delta _ { p } } { \Delta _ { 0 } } = ( - ) ^ { p } \Bigg [ \prod _ { n = 1 } ^ { r } \left( \alpha _ { 0 } - \alpha _ { n } \right) \Bigg ] \Bigg / \Bigg [ \prod _ { n = 0 } ^ { r } { } ^ { ( p ) } \left( \alpha _ { p } - \alpha _ { n } \right) \Bigg ] .
$$

Put $\alpha _ { 0 } = 0$ ， $\alpha _ { 1 } = 2 ^ { 2 }$ ， $\alpha _ { 2 } = 4 ^ { 2 } , \ldots , \alpha _ { r } = 4 r ^ { 2 }$ ; then we get

$$
\gamma _ { p } = ( - 1 ) ^ { p - 1 } \frac { 4 ( r ! ) ^ { 2 } } { ( r - p ) ! ( r + p ) ! } .
$$

Hence

$$
\beta _ { 2 n } = \frac { ( - 1 ) ^ { n - 1 } ( r ! ) ^ { 2 } } { 2 n \cdot ( r - n ) ! ( r + n ) ! } ,
$$

and

$$
{ \frac { \pi } { 2 } } A _ { m } = ( - 1 ) ^ { r + 1 } { \frac { 2 ^ { 2 r + 1 } ( r ! ) ^ { 2 } } { m ^ { 2 } ( m ^ { 2 } - 2 ^ { 2 } ) \cdots ( m ^ { 2 } - 4 r ^ { 2 } ) } } .
$$

Finally, we find

$$
x = \frac { \pi } { 2 } + \sum _ { m = 1 } ^ { \infty } A _ { m } \cos m x + \sum _ { n = 1 } ^ { r } 2 \beta _ { 2 n } \sin 2 n x \eqno ( m = 1 , 3 , 5 , \ldots ) .
$$

The integer $r$ can be chosen arbitrarily. The formal convergence of this series can be made as rapid as we please. The greater the $r$ is, the more rapidly the coefficient of a higher term of the series decreases. If we substitute $\theta + ( \pi / 2 )$ in place of $_ x$ in this formula for $_ x$ ，the series becomes identical with Gyldén's. Gyldén's auxiliary function $\int _ { 0 } ^ { \theta } \cos ^ { 2 i } \theta \cdot d \theta$ is a special case of our auxiliary function $\mathbf { \nabla } ^ { f ( x ) }$ . Gyldén's function is the best for achieving our aim by the present method. The equation (29) gives the clue to the problem.Expand $\alpha _ { m }$ in the form

$$
\alpha _ { m } = \frac { \lambda _ { 1 } } { m } + \frac { \lambda _ { 2 } } { m ^ { 2 } } + \frac { \lambda _ { 3 } } { m ^ { 3 } } + \cdots .
$$

If this expansion contains only even powers of $^ { m }$

$$
\alpha _ { m } = \frac { \lambda _ { 2 } } { m ^ { 2 } } + \frac { \lambda _ { 4 } } { m ^ { 4 } } + \cdots ,
$$

then from (29) it follows that the coefficints $\beta _ { n }$ and the integer $r$ can be chosen so that the infinitesimal order attributed to $\pmb { A } _ { m }$ for $m = \infty$ becomes arbitrary. In particular, if

$$
\alpha _ { m } = \frac { \lambda } { m ^ { 2 } - \mu ^ { 2 } } ,
$$

then the expansion includes the expansion of sin $\mu x$ and cos $\mu x$ when $\pmb { \mu }$ is irrational.

Poincaré (1886) called the formal convergence of order $\pmb { p }$ if

$$
| m ^ { p } A _ { m } | \leq K , \qquad | m ^ { p } B _ { m } | \leq K
$$

in the expansion

$$
f ( x ) \sim \sum A _ { \mathit { m } } \sin m x + \sum B _ { \mathit { m } } \cos m x ,
$$

where $\kappa$ is independent of $_ m$ . Suppose that a function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ ，periodic with period $2 \pi$ ，is finite and continuous together with all its derivatives for all values of $x$ between O and $2 \pi$ ，except at a finite number of exceptional points. A function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is said to be discontinuous of order $p$ at a given value of $x$ ,if $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ and its first $p - 2$ derivatives are finite and continuous in the neighborhood of that value while its $( p - 1 ) \mathrm { t h }$ derivative is finite but discontinuous. Poincaré proved that, if $f ( x )$ is discontinuous of order $p$ ，then $f ( x )$ is represented by a trigonometric series whose formal convergence is of order $p$

At first Poincaré showed that the formal convergence is at least of order $p - 1$ . Suppose that $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ has discontinuities of order 2,that is, its first-order derivative is finite but discontinuous.Then the derivative is always less than $\kappa$ in absolute value. We have, for any $h$ ，

$$
| f ( x + h ) - f ( x ) | < | K h | .
$$

Now

$$
\begin{array} { l } { { f ( x + h ) - f ( x ) = \displaystyle \sum _ { - 2 } A _ { m } \sin m h \cos m x } } \\ { { \displaystyle ~ - 2 \sum _ { \alpha } A _ { m } \sin ^ { 2 } \frac { m h } { 2 } \sin m x } } \\ { { \displaystyle ~ - 2 \sum _ { \alpha } B _ { m } \sin ^ { 2 } \frac { m h } { 2 } \cos m x } } \\ { { \displaystyle ~ - \sum _ { \alpha } B _ { m } \sin m h \sin m x . } } \end{array}
$$

As has been seen, the coefficients have absolute values less than twice the maximum absolute value of the function that the series represents. Applying this theorem to $f ( x + h ) - f ( x )$ we have

$$
\begin{array} { l } { { \displaystyle \left| { \cal A } _ { m } \sin m h - 2 B _ { m } \sin ^ { 2 } \frac { m h } { 2 } \right| < | 2 K h | } , } \\ { { \displaystyle \left| 2 { \cal A } _ { m } \sin ^ { 2 } \frac { m h } { 2 } + B _ { m } \sin m h \right| < | K h | } , } \end{array}
$$

or

$$
\begin{array} { l } { { \displaystyle \left| A _ { \mathfrak { m } } \frac { \sin m h } { m h } - B _ { \mathfrak { m } } \frac { 2 \sin ^ { 2 } ( m h / 2 ) } { m h } \right| < \bigg | \frac { 2 K } { m } \bigg | } , } \\ { { \displaystyle \left| A _ { \mathfrak { m } } \frac { 2 \sin ^ { 2 } ( m h / 2 ) } { m h } + B _ { \mathfrak { m } } \frac { \sin m h } { m h } \right| < \bigg | \frac { 2 K } { m } \bigg | } . } \end{array}
$$

Let $h \to 0$ ； then the left-hand members tend to $A _ { m }$ and $\pmb { B } _ { m }$ , respectively,and we obtain

$$
| m A _ { m } | \leq | 2 K | , \qquad | m B _ { m } | \leq | 2 K | .
$$

Hence the formal convergence of $f ( x )$ is of order 1.

If $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is discontinuous of order $p$ ,then its derivative of order $p - 2$ is discontinuous of order 2.The derivative is

$$
\begin{array} { c } { { \displaystyle \sum m ^ { p - 2 } A _ { m } \sin \left[ m x + ( p - 2 ) \frac { \pi } { 2 } \right] } } \\ { { + \displaystyle \sum m ^ { p - 2 } B _ { m } \cos \left[ m x + ( p - 2 ) \frac { \pi } { 2 } \right] . } } \end{array}
$$

Since this derivative is discontinuous of order 2, its formal convergence is at least of order 1, i.e.,

$$
| m ^ { p - 1 } A _ { m } | \leq | 2 K | , \qquad | m ^ { p - 1 } B _ { m } | \leq | 2 K | .
$$

Hence the series representing $f ( x )$ is formally convergent of order $p - 1$ at least. We will now show that the formal convergence is of order $p$

For the proof, construct a periodic function which admits derivatives of a given order.

Suppose that the discontinuities_are of the first order. Let $\alpha _ { 1 } , \alpha _ { 2 } ,$ $\cdot \cdot , \alpha _ { n }$ be $\pmb { n }$ values of $x$ arranged in order of increasing magnitude between O and $2 \pi$ ，for which the function $\phi ( x )$ is discontinuous.Let $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { n }$ be the amounts by which $\phi ( x )$ jumps as $x$ passes through each of those values. Then we have

$$
\operatorname * { l i m } _ { \varepsilon  0 } [ \phi ( \alpha _ { i } + \varepsilon ) - \phi ( \alpha _ { i } - \varepsilon ) ] = \beta _ { i } \qquad ( \varepsilon > 0 ) .
$$

Further, let

$$
\operatorname* { l i m } _ { \varepsilon \to 0 } \left[ \phi ( \varepsilon ) - \phi ( - \varepsilon ) \right] = \beta _ { n + 1 } ,
$$

which may be zero when $\phi ( x )$ is continuous for $x = 0$ . To construct $\phi ( x + 2 \pi ) = \phi ( x )$ it is sufficient to take

$$
\begin{array} { l l } { \phi ( x ) = \lambda x + h } & { ( 0 < x < \alpha _ { 1 } ) , } \\ { \phi ( x ) = \lambda x + h + \beta _ { 1 } } & { ( \alpha _ { 1 } < x < \alpha _ { 2 } ) , } \\ { \phi ( x ) = \lambda x + h + \beta _ { 1 } + \beta _ { 2 } } & { ( \alpha _ { 2 } < x < \alpha _ { 3 } ) , } \\ { \cdot \cdot \cdot } \\ { \phi ( x ) = \lambda x + h + \beta _ { 1 } + \beta _ { 2 } + \cdot \cdot \cdot + \beta _ { n - 1 } } & { ( \alpha _ { n - 1 } < x < \alpha _ { \tau } } \\ { \phi ( x ) = \lambda x + h + \beta _ { 1 } + \beta _ { 2 } + \cdot \cdot \cdot + \beta _ { n - 1 } + \beta _ { n } } & { ( \alpha _ { n } < x < 2 \pi ) , } \end{array}
$$

where

$$
\lambda = - \frac { 1 } { 2 \pi } ( \beta _ { 1 } + \beta _ { 2 } + \cdots + \beta _ { n } + \beta _ { n + 1 } ) .
$$

Expand $\phi ( x )$ in the form

$$
\phi ( x ) = \sum A _ { m } \sin m x + \sum B _ { m } \cos m x ;
$$

then it is evident that the formal convergence of this series is of the first order. We choose the constant $h$ so that $\pmb { { \cal B } } _ { 0 }$ is zero.

Next,suppose that the derivatives are of order $p$ . We construct a function $\phi _ { p } ( x )$ that admits given discontinuities of order $\pmb { p }$ ，that is, whose $( p - 1 ) \mathrm { t h }$ derivative has the given discontinuities of order 1. From the above discussion we can construct a function

$$
\phi ( x ) = \sum A _ { m } \sin m x + \sum B _ { m } \cos m x ,
$$

such that it admits discontinuities of the first-order imposed on its $( p - 1 ) \operatorname { t h }$ derivative， that $B _ { \circ } = 0$ ，and that it is represented by a series whose formal convergence is of the first order. Then we put

$$
\begin{array} { c } { { \phi _ { p } ( x ) = \displaystyle et { } { ' } \sum _ { m ^ { p - 1 } } \sin \Big [ m x - ( p - 1 ) \frac { \pi } { 2 } \Big ] } } \\ { { + \displaystyle et { } { ' } \sum _ { m ^ { p - 1 } } \cos \Big [ m x - ( p - 1 ) \frac { \pi } { 2 } \Big ] . } } \end{array}
$$

The $( p - 1 ) \mathtt { t h }$ derivative of this function is $\phi ( x )$ . Thus $\phi _ { p } ( x )$ satisfies the condition of the problem and is represented by a series formally convergent of the pth but not the $( p + 1 ) \mathrm { t h }$ order.

Take our function $\boldsymbol { \mathscr { f } } ( \boldsymbol { x } )$ whose discontinuities are of order $\pmb { p }$ ，and consider its series representation. The formal convergence of this series is of order $\pmb { p }$ . In fact,a periodic function $\phi _ { \mathfrak { p } } ( x )$ can be constructed so that it has the same discontinuities of order $p$ as those of $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ and is represented by a series formally convergent of order $p$ but not of order $p + 1$ . Then $f ( x ) - \phi _ { p } ( x )$ has only discontinuities of order $p + 1$ and hence is represented by a series formally convergent at least of order $p$ . The same holds for $\phi _ { \mathfrak { p } } ( x )$ .Hence the same is true for $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$

Now the series representing $f ( x )$ cannot be formally convergent of order $p + 1$ . On the other hand, since $f ( x ) - \phi _ { p } ( x )$ has only discontinuities of order $p + 1$ , it is represented by a series formally convergent of order $p + 1$ . If the same were true for $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ , the same would be true for $\phi _ { p } ( x )$ . This is contradictory. Hence the formal convergence of the series representing $f ( x )$ is of the pth but not of the $( p + 1 ) \mathrm { t h }$ order.

We now apply this principle of Poincaré to Gyldén's problem. We must find a trigonometric series whose formal convergence is of order $\pmb { p }$ and which is represented by a function $f ( x )$ for all values of $_ x$ between O and $\pi$ . Suppose that the function $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is finite and continuous together with all its derivatives.Consider a new function $\phi ( x )$ which is finite and continuous together with all its derivatives but otherwise completely arbitrary.A trigonometric series exists

$$
\sum A _ { m } \sin m x + \sum B _ { m } \cos m x ,
$$

which represents $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ for $0 < x < \pi$ and $\phi ( x )$ for $- \pi < x < 0$ The coefficients of such a series are

$$
\begin{array} { l } { \displaystyle 2 \pi B _ { 0 } = \int _ { 0 } ^ { \pi } f ( x ) d x + \int _ { - \pi } ^ { 0 } \phi ( x ) d x , } \\ { \displaystyle \pi B _ { m } = \int _ { 0 } ^ { \pi } f ( x ) \cos m x \cdot d x + \int _ { - \pi } ^ { 0 } \phi ( x ) \cos m x \cdot d x , } \\ { \displaystyle \pi A _ { m } = \int _ { 0 } ^ { \pi } f ( x ) \sin m x \cdot d x + \int _ { - \pi } ^ { 0 } \phi ( x ) \sin m x \cdot d x . } \end{array}
$$

We must choose an arbitrary function $\phi ( x )$ so that the series is formally convergent of order $p$ .According to Poincaré's principle just described, it is necessary and sufficient that

$$
f ( 0 ) = \phi ( 0 ) , \qquad f ^ { \prime } ( 0 ) = \phi ^ { \prime } ( 0 ) , \qquad f ^ { \prime \prime } ( 0 ) = \phi ^ { \prime \prime } ( 0 ) ,
$$

$$
f ( \pi ) = \phi ( - \pi ) ~ f ^ { \prime } ( \pi ) = \phi ^ { \prime } ( - \pi ) , ~ f ^ { \prime \prime } ( \pi ) = \phi ^ { \prime \prime } ( - \pi ) ,
$$

$$
f ^ { ( p - 1 ) } ( \pi ) = \phi ^ { ( p - 1 ) } ( - \pi ) ,
$$

where $f ^ { \prime } , f ^ { \prime \prime } , \ldots , f ^ { \scriptscriptstyle ( p - 1 ) }$ denote the successive derivatives of $f$ ，while $\phi ^ { \prime }$ ， $\phi ^ { \prime \prime } , \ldots , \phi ^ { ( p - 1 ) }$ denote those of $\phi$ . This condition can be satisfied in an infinite number of ways. The function $\phi ( x )$ remains arbitrary in large measure ; $\phi ( x )$ and its first $p - 1$ derivatives are subject only to our taking the definite values for $x = 0$ and for $x = - \pi$

Let us apply this principle to Charlier's case $\textstyle f ( x ) = x$ .Expand the function $x$ in the form

$$
\sum _ { m = 0 } ^ { \infty } A _ { m } \cos m x + \sum _ { n = 1 } ^ { 2 r } 2 \beta _ { n } \sin n x .
$$

In this case, take

$$
\phi ( x ) = - x + \sum _ { n = 1 } ^ { 2 r } 4 \beta _ { n } \sin n x .
$$

The above conditions for the formal convergence of order $\pmb { p }$ are

$$
\begin{array} { l l l } { { 1 = - 1 + \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n \beta _ { n } , } } & { { \qquad 1 = - 1 + \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n \beta _ { n } ( - 1 ) ^ { n } , } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 3 } \beta _ { n } , } } & { { \qquad 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 3 } ( - 1 ) ^ { n } \beta _ { n } , } } \\ { { \mathrm { } 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 5 } \beta _ { n } , } } & { { \qquad 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 5 } ( - 1 ) ^ { n } \beta _ { n } , } } \\ { { \mathrm { } \ldots , } } & { { \qquad \ldots , } } \\ { { \mathrm { } 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 4 } \beta _ { n } , } } & { { \qquad 0 = \displaystyle \sum _ { \vphantom { \ d + 1 } } 4 n ^ { 4 } ( - 1 ) ^ { n } \beta _ { n } , } } \end{array}
$$

where $\pmb q$ is the largest odd integer not larger than $\pmb { p }$ . The number of the unknown coefficients $\beta _ { n }$ is $_ { 2 r }$ .In order that the number of the equations be equal to the number of the unknown coefficients it is sufficient to take $p = 2 r$ ， $q = 2 r - 1$ .Hence the conditions are

$$
\sum _ { n = 1 } ^ { r } 4 ( 2 n - 1 ) ^ { h } \beta _ { 2 h - 1 } = 0 \qquad ( h = 1 , 3 , 5 , \ldots , 2 r - 1 ) ,
$$

or

$$
\beta _ { 2 n - 1 } = 0 \qquad ( n = 1 , 2 , \ldots , r ) .
$$

Furthermore

$$
2 = \sum _ { n = 1 } ^ { r } 4 ( 2 n ) \beta _ { 2 n } , ~ 0 = \sum _ { n = 1 } ^ { r } 4 ( 2 n ) ^ { h } \beta _ { 2 n } ,
$$

$$
( h = 3 , 5 , \ldots , 2 r - 1 ) ,
$$

from which we obtain the values of the remaining $r$ coefficients $\beta _ { 2 } , \beta _ { 4 }$ $\cdots \cdot \cdot , \beta _ { 2 \tau }$ . These values coincide with those obtained by Gyldén and Charlier.

Finally we come to the general case. Let $f ( x )$ be an arbitrary function to be represented between O and $\pi$ by a series of the form

$$
\sum _ { m = 0 } ^ { \infty } A _ { m } \cos m x + \sum _ { n = 1 } ^ { 2 r } 2 \beta _ { n } \sin n x ,
$$

whose formal convergence is of order $p$ . Take $p = 2 r$ ; then we have

$$
\phi ( x ) = f ( - x ) + \sum _ { n = 1 } ^ { 2 r } 4 \beta _ { n } \sin n x .
$$

The conditions are now

$$
\begin{array} { c c } { { { \displaystyle f ^ { \prime } ( 0 ) = 2 \sum n \beta _ { n } , } } } & { { { ~ \displaystyle f ^ { \prime } ( \pi ) = 2 \sum n ( n - 1 ) ^ { n } \beta _ { n } , } } } \\ { { { \displaystyle - f ^ { \prime \prime \prime } ( 0 ) = 2 \sum n ^ { 3 } \beta _ { n } , } } } & { { { ~ \displaystyle - f ^ { \prime \prime \prime } ( \pi ) = 2 \sum n ^ { 3 } \beta ^ { \circ } ( - 1 ) ^ { n } \beta _ { n } , } } } \\ { { { \displaystyle f ^ { \mathrm { v } } ( 0 ) = 2 \sum n ^ { 5 } \beta _ { n } , } } } & { { { ~ \displaystyle f ^ { \mathrm { v } } ( \pi ) = 2 \sum n ^ { 5 } \bar { \imath } ^ { \mathrm { v } } ( - 1 ) ^ { n } \beta _ { n } , } } } \\ { { { \displaystyle \cdots , } } } & { { { ~ \displaystyle \cdots , } } } \\ { { { \displaystyle f ^ { \mathrm { ( p - 1 ) } } ( 0 ) = 2 \sum n ^ { 9 - 1 } \beta _ { n } , } } } & { { { ~ \displaystyle \pm f ^ { \mathrm { ( p - 1 ) } } ( \pi ) = 2 \sum n ^ { 9 - 1 } ( - 1 ) ^ { n } \beta _ { n } } } } \end{array}
$$

The $_ { 2 r }$ coefficients $\beta _ { 2 } , \beta _ { 4 } , \ldots , \beta _ { 2 r }$ are obtained from these equations as. linear functions of $2 r$ quantities

$$
\begin{array} { l } { { f ^ { \prime } ( 0 ) , f ^ { \prime \prime \prime } ( 0 ) , f ^ { \mathrm { v } } ( 0 ) , \ldots , f ^ { ( p - 1 ) } ( 0 ) , } } \\ { { f ^ { \prime } ( \pi ) , f ^ { \prime \prime \prime } ( \pi ) , f ^ { \mathrm { v } } ( \pi ) , \ldots , f ^ { ( p - 1 ) } ( \pi ) . } } \end{array}
$$

The preceding solution which contains Gyldén's can vary up to infinity， since $\phi ( x )$ remains almost completely arbitrary.

Following Callandreau we take the eccentric anomaly of the disturbed planet as the independent variable $x$ and express various quantities as functions of $x$ .Let $F ( x )$ be one of those quantities. It is finite and continuous together with allits derivatives. Represent $x$ by Gyldén's series

$$
x = \sum A _ { m } \cos m x + \sum B _ { m } \sin m x ,
$$

of which the formal convergence is of order $\pmb { p }$ . The sum of this series is a finite and continuous periodic function, together with its first $p - 1$ derivatives, and coincides with $_ x$ in the interval from O to $\pmb { \pi }$

Callandreau expanded $F [ f ( x ) ]$ in a trigonometric series whose sum is equal to $F ( x )$ in the interval between O and $\pi$ . The formal convergence of this series is of order $p$ . This is based on Poincaré's principle just discussed. If $f ( x )$ is finite and continuous together with its frst $p - 1$ derivatives,then clearly the same is true for $F [ f ( x ) ]$ (refer to Section 10.45).

# 15.13GROUPING OF TERMS

The series in celestial mechanics have been expanded in trigonometric series proceeding with sines and cosines of multiples of the angular variables (Section 14.7). Poincaré(1898) proposed a method for grouping the terms of such series in order to obtain the formal convergence as rapid as we please.He limited himself to the consideration of the restricted three-body problem.In the usual notation

$$
\begin{array} { c c } { { x _ { 1 } = \sqrt { a } - \sqrt { a ( 1 - e ^ { 2 } ) } , \qquad } } & { { x _ { 2 } = \sqrt { a } + \sqrt { a ( 1 - e ^ { 2 } ) } , } } \\ { { 2 y _ { 1 } = l - g + l ^ { \prime } , } } & { { 2 y _ { 2 } = l + g - l ^ { \prime } , } } \end{array}
$$

the equations of motion are

$$
\frac { d x _ { 1 } } { d t } = \frac { \partial F } { \partial y _ { 1 } } , \qquad \frac { d x _ { 2 } } { d t } = \frac { \partial F } { \partial y _ { 2 } } , \qquad \frac { d y _ { 1 } } { d t } = - \frac { \partial F } { \partial x _ { 1 } } , \qquad \frac { d y _ { 2 } } { d t } = - \frac { \partial F } { \partial x _ { 2 } } ,
$$

where $\pmb { F }$ is expanded in powers of $\mu$ and is periodic with respect to $y _ { 1 }$ and $y _ { 2 }$ .For $\mu = 0$ the Hamiltonian $\pmb { F }$ reduces to

$$
F _ { 0 } = \frac { 2 } { ( x _ { 1 } + x _ { 2 } ) ^ { 2 } } + \frac { x _ { 2 } - x _ { 1 } } { 2 } ,
$$

which is independent of $y _ { 1 }$ and $y _ { 2 }$

Let $z _ { 1 } , z _ { 2 } , \varpi _ { 1 } , \varpi _ { 2 }$ be the integration constants and let $n _ { 1 } , n _ { 2 }$ be the two new constants depending on $z _ { 1 } , z _ { 2 }$ ，and $\mu$ ，and write

$$
w _ { 1 } = n _ { 1 } t + \varpi _ { 1 } , \qquad w _ { 2 } = n _ { 2 } t + \varpi _ { 2 } .
$$

The variables $x$ and $y$ are expanded in powers of $\mu$

$$
\begin{array} { r } { x _ { i } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \mu ^ { 2 } x _ { i } ^ { ( 2 ) } + \cdots , } \\ { y _ { i } = y _ { i } ^ { ( 0 ) } + \mu y _ { i } ^ { ( 1 ) } + \mu ^ { 2 } y _ { i } ^ { ( 2 ) } + \cdots , } \end{array}
$$

where $x _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ ， except $y _ { 1 } ^ { ( 0 ) }$ and $y _ { 2 } ^ { ( 0 ) }$ which are equal to $w _ { 1 }$ and $w _ { 2 }$ ， respectively,are expanded in trigonometric series proceeding with sines and cosines of multiples of $w _ { 1 }$ and $w _ { 2 }$ ， the coefficients depending on $z _ { 1 }$ and $z _ { 2 }$ . Also, $n _ { 1 }$ and $\mathfrak { n } _ { 2 }$ are expanded in powers of $\pmb { \mu }$ ,each term being a function of $z _ { 1 }$ and $z _ { 2 }$ ：

$$
n _ { i } = n _ { i } ^ { ( 0 ) } + \mu n _ { i } ^ { ( 1 ) } + \mu ^ { 2 } n _ { i } ^ { ( 2 ) } + \cdots \quad \quad ( i = 1 , 2 ) .
$$

Suppose that $x _ { i } ^ { ( 0 ) } = z _ { i }$ ; then

$$
n _ { 1 } ^ { ( 0 ) } = \frac { 4 } { ( z _ { 1 } + z _ { 2 } ) ^ { 3 } } + \frac { 1 } { 2 } , \qquad n _ { 2 } ^ { ( 0 ) } = \frac { 4 } { ( z _ { 1 } + z _ { 2 } ) ^ { 3 } } - \frac { 1 } { 2 } .
$$

The constant $z _ { 1 } = x _ { 1 } ^ { ( 0 ) }$ is very small and of the order of the square of the eccentricity, and $\boldsymbol { x } _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ ，except $y _ { 1 } ^ { ( 0 ) }$ and $y _ { 2 } ^ { ( 0 ) }$ , can be expanded in powers of $\sqrt { z _ { 1 } } \cos w _ { 1 }$ and $\sqrt { z _ { 1 } } \sin w _ { 1 }$ ， each term depending on $w _ { 2 }$ and $z _ { 2 }$ and periodic with respect to $w _ { 2 }$

It is noted that an infinite number of other series of the same form can be derived from these series.In fact, replacing $z$ and $\varpi$ by the expansions

$$
\begin{array} { r l } & { z _ { i } = z _ { i } ^ { ( 0 ) } + \mu z _ { i } ^ { ( 1 ) } + \mu ^ { 2 } z _ { i } ^ { ( 2 ) } + \cdots , } \\ & { \varpi _ { i } = \varpi _ { i } ^ { ( 0 ) } + \mu \varpi _ { i } ^ { ( 1 ) } + \mu ^ { 2 } \varpi _ { i } ^ { ( 2 ) } + \cdots , } \end{array}
$$

gives $\boldsymbol { z } _ { i } ^ { ( k ) }$ and ${ \varpi _ { i } ^ { ( k ) } }$ as functions of four new constants $z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime } , \varpi _ { 1 } ^ { \prime } , \varpi _ { 2 } ^ { \prime } ;$ except for $z _ { i } ^ { ( 0 ) } = z _ { i } ^ { \prime }$ ， $\varpi _ { i } ^ { ( 0 ) } = \varpi _ { i } ^ { \prime }$ . If the constants $z _ { i }$ and $\varpi _ { i }$ are replaced by (34) and arranged with respect to $\mu$ ， then new expansions for $x _ { i }$ and $y _ { i }$ are obtained which are of the same form as (31) proceeding in powers of $\mu$ and in sines and cosines of multiples of $w _ { 1 } ^ { \prime } = n _ { 1 } t +$ $\varpi _ { 1 } ^ { \prime }$ ， $w _ { 2 } ^ { \prime } = n _ { 2 } t + \varpi _ { 2 } ^ { \prime }$ ， with coefficients depending on the new constants $z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime } , \varpi _ { 1 } ^ { \prime } , \varpi _ { 2 } ^ { \prime }$ . The most remarkable case is when these coefficients depend only on $z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime }$ ，and are independent of $\varpi _ { 1 } ^ { \prime } , \varpi _ { 2 } ^ { \prime }$ ，like the series (31) itself.

How can we choose in general the expansions (34) that define the constants $z _ { i } ^ { \prime }$ and $\varpi _ { i } ^ { \prime } ?$ First we arrange so that the ratio of the two mean motions $n _ { 1 }$ and $n _ { 2 }$ shall be independent of $\mu$ ：

$$
\frac { n _ { 1 } } { n _ { 2 } } = \frac { 8 + ( z _ { 1 } ^ { \prime } + z _ { 2 } ^ { \prime } ) ^ { 3 } } { 8 - ( z _ { 1 } ^ { \prime } + z _ { 2 } ^ { \prime } ) ^ { 3 } } .
$$

If there were no relation between ${ n } _ { 1 } ^ { ( 0 ) }$ and ${ n } _ { 2 } ^ { ( 0 ) }$ ，then we should be able to choose the expansions (34) so that the mean motions $n _ { 1 }$ and $n _ { 2 }$ are both independent of $\mu$ .But there is such a relation.The equation （33） gives $n _ { 1 } ^ { ( 0 ) } - n _ { 2 } ^ { ( 0 ) } = 1$ .Let $n _ { 1 } ^ { ( 1 ) } - n _ { 2 } ^ { ( 1 ) } = \phi ( z _ { 1 } , z _ { 2 } )$ ，and write

$$
\begin{array} { l } { { \Bigl [ \frac { 4 } { ( z _ { 1 } ^ { \prime } + z _ { 2 } ^ { \prime } ) ^ { 3 } } + \frac { 1 } { 2 } \Bigr ] [ 1 + \mu \phi ( z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime } ) ] } } \\ { { { } ~ = n _ { 1 } ^ { \scriptscriptstyle ( 0 ) } + \mu n _ { 1 } ^ { \scriptscriptstyle ( 1 ) } + \mu ^ { \prime } n _ { 1 } ^ { \scriptscriptstyle ( 2 ) } + \cdots , } } \\ { { { \Bigl [ \frac { 4 } { ( z _ { 1 } ^ { \prime } + z _ { 2 } ^ { \prime } ) ^ { 3 } } - \frac { 1 } { 2 } \Bigr ] [ 1 + \mu \phi ( z _ { 1 } ^ { \prime } , z _ { 2 } ^ { \prime } ) ] } } } \\ { { { } ~ = n _ { 2 } ^ { \scriptscriptstyle ( 0 ) } + \mu n _ { 2 } ^ { \scriptscriptstyle ( 1 ) } + \mu ^ { \prime } n _ { 2 } ^ { \scriptscriptstyle ( 2 ) } + \cdots . } } \end{array}
$$

Since ${ n } _ { i } ^ { ( k ) }$ are known functions of $z _ { 1 }$ and $z _ { 2 }$ ，the variables $z _ { 1 } ^ { \prime }$ and $z _ { 2 } ^ { \prime }$ can be obtained from (36) as functions of $z _ { 1 } , z _ { 2 }$ ，and $\mu$ ； thus the expansions of the form (34) are obtained,where ${ z _ { i } ^ { ( k ) } }$ and ${ \widetilde { \pmb { \varpi } } } _ { i } ^ { ( k ) }$ depend only on $z _ { i } ^ { \prime }$ and not on $\varpi _ { i } ^ { \prime }$ . Thus the equations (36) are related to the relation (35).

We can also choose for the constants $z _ { i } ^ { \prime }$ and $\widetilde { \varpi } _ { i } ^ { \prime }$ the initial values of $x _ { i }$ and $y _ { i }$ for $t = 0$ In fact, replace $\pmb { t }$ by O in (31), $x _ { i }$ and $y _ { i }$ by $z _ { i } ^ { \prime }$ and $\varpi _ { i } ^ { \prime }$ ，respectively； then we get

$$
\begin{array} { r } { z _ { i } ^ { \prime } = x _ { i } ^ { ( 0 ) } + \mu x _ { i } ^ { ( 1 ) } + \mu ^ { 2 } x _ { i } ^ { ( 2 ) } + \cdots , } \\ { \varpi _ { i } ^ { \prime } = y _ { i } ^ { ( 0 ) } + \mu y _ { i } ^ { ( 1 ) } + \mu ^ { 2 } y _ { i } ^ { ( 2 ) } + \cdots , } \end{array}
$$

where the arguments $w _ { 1 }$ and $w _ { 2 }$ in the expansions for $\boldsymbol { x } _ { i } ^ { ( k ) }$ and $y _ { i } ^ { ( k ) }$ should be replaced by $\varpi _ { 1 }$ and $\widetilde { \omega } _ { 2 }$ . The right-hand members of (37) are known functions of $z , \varpi$ ,and $\mu$ .For $\mu = 0$ they reduce to $x _ { i } ^ { \scriptscriptstyle ( 0 ) } = z _ { i } , y _ { i } ^ { \scriptscriptstyle ( 0 ) }$ $= \varpi _ { i }$ . Hence $z$ and $\varpi$ are obtained from (37) as functions of new variables $z ^ { \prime } , \varpi ^ { \prime }$ ，and $\mu$ in series proceeding in powers of $\mu$ . These expansions are nothing but the expansions (34) in question. The inconven-ience of such expansions arises from the dependence of $z$ and $\varpi - \varpi ^ { \prime }$ not only on $z _ { 1 } ^ { \prime }$ and $z _ { 2 } ^ { \prime }$ but also on $\smash { \widetilde { \omega } _ { 1 } ^ { \prime } }$ and $\widetilde { \varpi } _ { 2 } ^ { \prime }$ . This inconvenience disappears if we proceed by arranging the series in the form (36).Hence the series (31) are replaced by the series,which we call (31a),of the same form but with coefficients depending not only on $z _ { 1 } ^ { \prime }$ and $z _ { 2 } ^ { \prime }$ but also on $\varpi _ { 1 } ^ { \prime }$ and $\varpi _ { 2 } ^ { \prime }$ . If we proceed otherwise，we obtain the series in the same form, but the coefficients are independent of $\widetilde { \varpi } _ { 1 } ^ { \prime }$ and $\widetilde { \varpi } _ { 2 } ^ { \prime }$

Before proceeding to such new expansions we examine how to derive from the series (31) the expansions obtained in classical celestial mechanics.With the constants $z ^ { \prime }$ and $\varpi ^ { \prime }$ ，consider the series (31a) just defined. The equations (32） give $n _ { 1 }$ and $n _ { 2 }$ as functions of $z _ { 1 } , z _ { 2 } ,$ and $\pmb { \mu }$ . Combining these with (34)，we obtain $n _ { 1 }$ and $n _ { 2 }$ as functions of $z ^ { \prime } , \varpi ^ { \prime }$ ，and $\pmb { \mu }$ ，which we write as

$$
n _ { i } = n _ { i } ^ { \prime ( 0 ) } + \mu n _ { i } ^ { \prime ( 1 ) } + \mu ^ { 2 } n _ { i } ^ { \prime ( 2 ) } + \cdots .
$$

Also, the $n _ { i } ^ { \prime ( k ) }$ are given as functions of $z ^ { \prime }$ and $\varpi ^ { \prime }$ and

$$
n _ { i } ^ { \prime ( 0 ) } = \frac { 4 } { ( z _ { 1 } ^ { \prime } + z _ { 2 } ^ { \prime } ) ^ { 3 } } \pm \frac { 1 } { 2 } .
$$

Consider the series

$$
x _ { i } = \sum _ { k } \mu ^ { k } x _ { i } ^ { \prime ( k ) } , \qquad y _ { i } = \sum _ { k } \mu ^ { k } y _ { i } ^ { \prime ( k ) } .
$$

Denote a term of $x _ { i } ^ { \prime ( k ) }$ or of $y _ { i } ^ { \prime ( k ) }$ by ${ \cal A } \sin { ( m _ { 1 } w _ { 1 } ^ { \prime } + m _ { 2 } w _ { 2 } ^ { \prime } ) }$ ，where $\pmb { A }$

depends on $z ^ { \prime }$ and $\varpi ^ { \prime }$ ，while $m _ { 1 }$ and $m _ { 2 }$ are integers. This term, however,depends on $\mu$ indirectly,since

$$
m _ { 1 } w _ { 1 } ^ { \prime } + m _ { 2 } w _ { 2 } ^ { \prime } = ( m _ { 1 } n _ { 1 } + m _ { 2 } n _ { 2 } ) t + ( m _ { 1 } \varpi _ { 1 } ^ { \prime } + m _ { 2 } \varpi _ { 2 } ^ { \prime } ) ,
$$

with $n _ { 1 }$ and $n _ { 2 }$ depending on $\mu$ . If we expand this term in powers of $\mu$ ， it becomes

$$
\begin{array} { r l r } & { \boldsymbol { A } \sin { ( m _ { 1 } w _ { 1 } ^ { \prime } + m _ { 2 } w _ { 2 } ^ { \prime } ) } = \boldsymbol { A } \sin { \omega } } & \\ & { \qquad + \ \mu \boldsymbol { A } t ( m _ { 1 } n _ { 1 } ^ { \prime ( 1 ) } + m _ { 2 } n _ { 2 } ^ { \prime ( 1 ) } ) \cos { \omega } + \cdots , } & \\ & { \boldsymbol { \omega } = ( m _ { 1 } n _ { 1 } ^ { \prime ( 0 ) } + m _ { 2 } n _ { 2 } ^ { \prime ( 0 ) } ) t + ( m _ { 1 } \widetilde { \omega } _ { 1 } ^ { \prime } + m _ { 2 } \widetilde { \omega } _ { 2 } ^ { \prime } ) . } & { ( 3 8 ) } \end{array}
$$

Replace each term of (31a) by its expansion (38) and arrange the resulting series with respect to $\mu$ .Then we obtain the series

$$
\begin{array} { r } { x _ { i } = x _ { i } ^ { \prime \prime ( 0 ) } + \mu x _ { i } ^ { \prime \prime ( 1 ) } + \mu ^ { 2 } x _ { i } ^ { \prime \prime ( 2 ) } + \cdot \cdot \cdot , } \\ { y _ { i } = y _ { i } ^ { \prime \prime ( 0 ) } + \mu y _ { i } ^ { \prime \prime ( 1 ) } + \mu ^ { 2 } y _ { i } ^ { \prime \prime ( 2 ) } + \cdot \cdot \cdot , } \end{array}
$$

which consist of purely trigonometric terms and also terms with $t$ outside the trigonometric signs as factors,in the same way as in the expansion (38).Each term is entirely independent of $\mu$ .Thus the series (31b）are the same as those obtained by means of the classical procedure.

These series contain non-secular terms, that is, trigonometric terms with arguments $m _ { 1 } w _ { 1 } ^ { \prime \prime } + m _ { 2 } w _ { 2 } ^ { \prime \prime }$ ，where the $ { \boldsymbol { w } } _ { i } ^ { \prime \prime }$ are linear functions of time， i.e.，where $w _ { i } ^ { \prime \prime } = n _ { i } ^ { \prime ( 0 ) } t + \varpi _ { i } ^ { \prime }$ . They also contain such trigonometric terms multiplied by $t$ or integral powers of $t _ { i }$ ，that is,mixed secular terms (Section 8.2).We separate these two kinds of terms in the form.

$$
x _ { 1 } = \begin{array} { r } { \sum A \sin \omega + t \cdot \sum _ { \mod } B \cos \omega + t ^ { 2 } \cdot \sum C \sin \omega + \cdots , } \\ { \omega = m _ { 1 } w _ { 1 } ^ { \prime \prime } + m _ { 2 } w _ { 2 } ^ { \prime \prime } + h , } \end{array}
$$

where $h$ is a constant. We can derive the coefficients $B , C , \ldots$ from the cofficients $\pmb { A }$ by

$$
B = \frac { { \cal A } } { 1 } ( m _ { 1 } \alpha _ { 1 } + m _ { 2 } \alpha _ { 2 } ) , ~ { \cal C } = - \frac { { \cal A } } { 1 \cdot 2 } ( m _ { 1 } \alpha _ { 1 } + m _ { 2 } \alpha _ { 2 } ) ^ { 2 } , \ldots ,
$$

where $\alpha _ { 1 } , \alpha _ { 2 }$ denote the constants $n _ { 1 } - n _ { 1 } ^ { \prime ( 0 ) }$ ， $n _ { 2 } \mathrm { ~ - ~ } n _ { 2 } ^ { \prime ( 0 ) }$ ， respectively. Thus, if we know $\alpha _ { 1 }$ and $\alpha _ { 2 }$ and the non-secular terms,then we can obtain the secular terms immediately. We see also that the purely secular terms should always be cancelled as we proceed to a higher approximation.

If we compare the series (31b） given by classical procedure with the series (31） given by our new procedure, then we at first see that the series (31b) arranged in powers of $\mu$ are convergent, as long as t is sufficiently small. The convergence is destroyed if $t$ is larger than a certain bound.The first terms of the series (31） converge rapidly enough for practical purpose, but no rigorous mathematical proof of the convergence of the series has yet been discovered. However,as we have shown,the convergence,if any,is not uniform for all values of t,nor for all values of the integration constants in certain intervals. Hence the question is whether our new method, in which expansions in powers of $t$ are avoided, has any real advantage. The answer de-pends on whether we are dealing with the motion over a comparatively short time interval with high accuracy or over a long time interval with medium accuracy.

We now abandon the classical procedure and refer to the expansions (31). These expansions contain certain terms that may become very large; but it is often possible to compensate by an appropriate grouping of the terms.It occurs frequently that a group of terms contains very large terms but the sum of such terms in a group is nevertheless very small. In fact, the terms of (31) are obtained by a set of operations including integrations,additions,multiplications,and differentiations.For example,in integrating a term of the form $\pmb { A }$ cos αt we obtain a term $( A \sin \alpha t ) / \alpha$ .If $\alpha$ is very small, then this integrated term becomes very large.But this is not so for a finite value of $t$ ，since the term is smaller than $\boldsymbol { A } t$ . If we integrate a term $A \sin \alpha t$ ，we obtain $- ( A \cos \alpha t ) / \alpha$ or $( A / \alpha ) - ( A \sin \alpha t ) / \alpha$ .Each of these two terms is very large,but the set of these two terms is finite and smaller than $A \alpha t ^ { 2 } / 2$ .These examples show the advantage of grouping the terms.

Consider a term $A \cos \alpha t$ and its integrated result $( A \sin \alpha t ) / \alpha$ Multiply this term by sin $\beta t$ ； then we obtain

$$
\frac { A \sin { \alpha t } \sin { \beta t } } { \alpha } = \frac { A } { 2 \alpha } \cos { ( \beta - \alpha ) } t - \frac { A } { 2 \alpha } \cos { ( \beta + \alpha ) } t .
$$

Integration gives

$$
\frac { A \sin { ( \beta - \alpha ) t } } { 2 \alpha ( \beta - \alpha ) } - \frac { A \sin { ( \beta + \alpha ) t } } { 2 \alpha ( \beta + \alpha ) } .
$$

If $\beta$ is finite and $\alpha$ is very small,each term is very large. Since both terms are of nearly equal period,the two nearly cancel, both being of order $\boldsymbol { A } t / \beta$ . This circumstance often appears in the computation of the second-order perturbation.

Next, let us study_ the form of the expansions (31) by examining some of their terms.Let

$$
\mu ^ { p } A \operatorname * { s i n } _ { \mathrm { { c o s } } } ( m _ { 1 } w _ { 1 } + m _ { 2 } w _ { 2 } )
$$

be one of these terms, $\pmb { A }$ being a function of $z _ { 1 }$ and $z _ { 2 }$ . We see that the expansions (32) reduce to the first two terms

$$
n _ { 1 } = n _ { 1 } ^ { ( 0 ) } + \mu n _ { 1 } ^ { ( 1 ) } , ~ n _ { 2 } = n _ { 2 } ^ { ( 0 ) } + \mu n _ { 2 } ^ { ( 1 ) } ,
$$

such that

$$
\frac { n _ { 1 } } { n _ { 2 } } = \frac { n _ { 1 } ^ { ( 0 ) } } { n _ { 2 } ^ { ( 0 ) } } = \frac { 8 + ( z _ { 1 } + z _ { 2 } ) ^ { 3 } } { 8 - ( z _ { 1 } + z _ { 2 } ) ^ { 3 } }
$$

is independent of $\mu$ but depends only on $z _ { 1 } + z _ { 2 }$ . Otherwise we should be able to pass from the constants $z$ to the constants $z ^ { \prime }$ as defined by (34).The successive integration introduces in the function $\pmb { A }$ the divisors of the form $q _ { 1 } n _ { 1 } ^ { ( 0 ) } + q _ { 2 } n _ { 2 } ^ { ( 0 ) }$ with integers $q _ { 1 }$ and $q _ { 2 }$ ，which we call small divisors. Write $A = B / \Pi$ ，where $\Pi$ is the product of small divisors and $B$ is a function of $z _ { 1 }$ and $z _ { 2 }$ . Then $\pmb { B }$ remains finite for all values of $z _ { 1 }$ and $z _ { 2 }$ ，but $\pmb { A }$ may become infinite,since certain small divisors can vanish for a commensurable value of $n _ { 1 } ^ { ( 0 ) } / n _ { 2 } ^ { ( 0 ) }$ . Now consider $\pmb { B }$ as a function of $z _ { 1 }$ and $z _ { 1 } + z _ { 2 }$ ,orof $z _ { 1 }$ and ${ n } _ { 1 } ^ { ( 0 ) }$ . The product $\Pi$ is an integral polynomial of ${ n } _ { 1 } ^ { ( 0 ) }$ , because $q _ { 1 } n _ { 1 } ^ { ( 0 ) } + q _ { 2 } n _ { 2 } ^ { ( 0 ) } = ( q _ { 1 } + q _ { 2 } ) n _ { 1 } ^ { ( 0 ) }$ $- q _ { 2 } ( n _ { 1 } ^ { ( 0 ) } - n _ { 2 } ^ { ( 0 ) } )$ . For a moment, suppose that $z _ { 1 }$ is a constant； then $\pmb { A }$ will be equal to a function of ${ n } _ { 1 } ^ { ( 0 ) }$ , holomorphic in a certain domain, dividedbya polynomial in ${ n } _ { 1 } ^ { ( 0 ) }$ .Let $B = C \mathbb { 1 } + D$ ,where $C$ is another function holomorphic in ${ n } _ { 1 } ^ { ( 0 ) }$ and $D$ is a polynomial of degree lower than $\pi$ .Then $A = C + D / \Pi$ . If we decompose the rational fraction into a sum of simple fractions,we find

$$
\begin{array} { l } { { \mu ^ { p } C _ { \cos } ^ { \sin } \left( m _ { 1 } w _ { 1 } + m _ { 2 } w _ { 2 } \right) } } \\ { { \qquad + \displaystyle \sum ^ { p } \mu ^ { p } { \frac { E } { ( q _ { 1 } n _ { 1 } ^ { ( 0 ) } + q _ { 2 } n _ { 2 } ^ { ( 0 ) } ) ^ { h } } } \cos \left( m _ { 1 } w _ { 1 } + m _ { 2 } w _ { 2 } \right) } , } \end{array}
$$

where $C$ is a holomorphic function in $z _ { 1 }$ and ${ n } _ { 1 } ^ { ( 0 ) }$ ,and other terms contain in the numerator a function $\boldsymbol { \varepsilon }$ ，which is holomorphic in $z _ { 1 }$ only, and in the denominator an integral power $h$ of a single small divisor. By taking into account the way we have obtained the expansions (31), we see that the polynomial $\Pi$ is the product of at most $2 p - 1$ small divisors for the expansions of $x _ { 1 }$ and $x _ { 2 }$ ，and the product of at most $2 p$ small divisors for the expansions of $y _ { 1 }$ and $y _ { 2 }$ . Hence the polynomial is at most of degree $2 p - 1$ or $2 p$ , where $p$ is the exponent of $\mu$ of the term in question. In each term of (39) the exponent $h$ is at most equal to $2 p - 1$ or $2 p$ . If it attains its upper limit $2 p - 1$ or $2 p$ ， then we have $m _ { 1 } / q _ { 1 } = m _ { 2 } / q _ { 2 }$

Now we group the terms obtained by decomposing each term of the series into the form (39) in the following manner: the first group contains all terms without any small divisor such as the first term of (39), while each of the other groups consists of the terms containing a power of a small divisor in the denominator. Consider a group of terms containing a power of $\delta = q _ { 1 } n _ { 1 } ^ { ( 0 ) } + q _ { 2 } n _ { 2 } ^ { ( 0 ) }$ in the denominator and call it the group $( q _ { 1 } , q _ { 2 } )$ . Each term of the group $( q _ { 1 } , q _ { 2 } )$ contains $\mu / \delta ^ { \hbar }$ as a factor, where the difference $2 p - 1 - h$ is positive or zero for the variables $x _ { 1 }$ and $x _ { 2 }$ ,and $2 p - h$ is positive or zero for $y _ { 1 }$ and $y _ { 2 }$ . Arrange a sub-group of terms for which this difference has the same value； the principal sub-group is the one with a difference equal to zero. If $\delta$ is very small of order $\sqrt { \mu }$ ， then certain terms of a higher order with respect to $\mu$ may become of sensible magnitude due to the presence of a power of $\delta$ in the denominator.The importance of a term is measured by the difference $2 p - 1 - h$ . A term with $2 p - 1 - h = 0$ is the most important. The numbers $q _ { 1 }$ and $q _ { 2 }$ can be considered to be mutually prime,so that we can find two integers $r _ { 1 }$ and $r _ { 2 }$ such that $q _ { 1 } r _ { 2 } - q _ { 2 } r _ { 1 } = 1$ . Put $m _ { 1 } = \alpha q _ { 1 } + \beta r _ { 1 }$ and $m _ { 2 } = \alpha q _ { 2 } + \beta r _ { 2 }$ ，with two integers $_ \alpha$ and $\beta$ . Classify in one partial series those terms of a subgroup that correspond to the same value of $\beta$ . Since $\delta$ is very small, $q _ { 1 } n _ { 1 } + q _ { 2 } n _ { 2 }$ is also very small，so that all terms of one of the partial series have periods nearly equal to $2 \pi / [ \beta ( r _ { 1 } n _ { 1 } + r _ { 2 } n _ { 2 } ) ]$ . A principal sub-group contains only one partial series， since $m _ { 1 } / q _ { 1 } = m _ { 2 } / q _ { 2 }$ and accordingly $\beta = 0$ for such a sub-group. The terms of the first group are generally very small, since they do not contain any small divisor.

A singular situation may arise where each of the partial series is easily summable. The summation is carried out by a finite number of quadratures.Generally we need only sum a few isolated terms and a few partial series.Bohlin's theory is concerned with the classical procedure that leads to the series (31). If we limit ourselves to summing the partial series that correspond to the principal sub-group，then we come to Delaunay's theory (Section 9.1). If the mean motions are nearly commensurable, the partial series may diverge.Neverthless,an analytical expression obtained after this summation still has meaning. Thus the expression $1 / ( 1 - x )$ conserves its meaning for $x > 1$ ，even though the series $1 + x + x ^ { 2 } + \cdots$ is not convergent. Even when a partial series may diverge,we can replace it by such an analytical expression. This is why Bohlin's and Delaunay's theories are applicable to the case when the direct use of the series (31) becomes illusory,and even