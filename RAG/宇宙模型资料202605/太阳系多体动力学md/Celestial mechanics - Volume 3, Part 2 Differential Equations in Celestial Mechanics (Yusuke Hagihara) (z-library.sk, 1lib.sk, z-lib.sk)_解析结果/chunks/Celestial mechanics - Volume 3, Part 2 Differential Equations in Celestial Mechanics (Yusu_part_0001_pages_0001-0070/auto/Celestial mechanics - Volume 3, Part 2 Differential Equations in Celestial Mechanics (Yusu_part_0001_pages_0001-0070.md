# CELESTIAL MECHANICS

VOLUME III, PRT 2

Yusuke Hagihara

As a sequel to previous two volumes on Transformation Theory and Perturbation Theory, published by the MIT Press, Volume Ill containing Chapters 12-16. treats the form of the solution in the three-body problem and perturbation theory, closely connected with the stability of a planetary system,and the question of its uniform convergence on the basis of the theory of differential equations.

In Chapter 12,after reducing the problem in celestial mechanics to simpl differential equations,such as Hill's, Lindstedt's and Mathieu's,the form of the solutions is discussed in detail. Theory of Saturn's rings is treated on such-grounds.Matrix integration method is applied to various problems. The Krylov-Bogoliubov method and Diliberto's periodic surface theory are. described in Chapter 13 with application to the motion of earth satellites. In Chapter 14 various forms of solution in planetary theory,such as Newcomb's,Lindstedts's,Bohlin's, Whittaker's are presented. The third integral recently discovered in galaxy dynamics is fully examined. Almost periodic differential equations are treated. The convergence problem is discussed in Chapter 15 on the viewpoint of point-set theory, Liouvilles numbers and diophantine approximations and it is proved that all solutions previously obtained are not uniformly convergent.Methods for elevating the degree of formal convergence are described. Littlewood's asymptotic integral of the three-body problem is presented. The last Chapter is on the Liapounoy stability and its modern development mainly in Soviet.Various new6nceptions, such as uniform

# CELESTIAL MECHANICS Volume III, Part 2 Differential Equations in Celestial Mechanics

# CELESTIAL MECHANICS

Yusuke Hagihara

Differential Equations in Celestial Mechanics

# Form of the Integrals of Planetary Theory

# ASYMPTOTIC REPRESENTATION

# I4.IPROBLEM OF THE FORM OF THE INTEGRALS

The question of the form of the integrals of differential equations is one which has for many years commanded attention in celestial mechanics in connection with the stability of the solar system.

Generally the problem of a dynamical system is based on the integration of a system of differential equations with time as the independent variable.The solution is possible in general in a form of a series proceeding with integral ascending powers of time， insofar as we are concerned with the solution in the domains free from any singularity or far from any of the singularities of the differential equations,by the well-known theorem on the existence of the solution (Painlevé,1897；Sections 10.42-10.43； 22.4-22.12). Consider a system of differential equations

$$
\frac { d x _ { i } } { d t } = \frac { \partial H } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial H } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

where $\pmb { H }$ does not contain time $t$ explicitly.The solution can be obtained in $_ { 2 n }$ equations of the type

$$
\begin{array} { l } { { \displaystyle x _ { i } = a _ { i } + ( t - t _ { 0 } ) ( a _ { i } , K ) + \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 ! } ( ( a _ { i } , K ) , K ) } } \\ { { \displaystyle ~ + \frac { ( t - t _ { 0 } ) ^ { 3 } } { 3 ! } ( ( ( a _ { i } , K ) , K ) , K ) + \cdots , } } \end{array}
$$

$$
y _ { i } = b _ { i } + ( t - t _ { 0 } ) ( b _ { i } , K ) + \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 ! } \left( ( b _ { i } , K ) , K \right)
$$

$$
+ \frac { ( t - t _ { 0 } ) ^ { 3 } } { 3 ! } ( ( ( b _ { i } , K ) , K ) , K ) + \cdots ,
$$

where $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ ， $b _ { 1 } , \ldots , b _ { n }$ are respectively the initial values of $x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , y _ { 1 } , \ldots , y _ { n }$ for $t = t _ { 0 }$ and $\kappa$ is a function of $a _ { 1 } , \ldots , a _ { n } ;$ $b _ { 1 } , \ldots , b _ { n }$ in the same form as $\pmb { H }$ is a function of $x _ { 1 } , \ldots , x _ { n } , y _ { 1 } , \ldots ,$ $y _ { n }$ ，and (Sections 1.9 and 4.3)

$$
\left( { f , \phi } \right) = \sum _ { i = 1 } ^ { n } { \left( { \frac { { \partial { f } } } { { \partial { a _ { i } } } } \frac { { \partial \phi } } { { \partial { b _ { i } } } } - \frac { { \partial { f } } } { { \partial { b _ { i } } } } \frac { { \partial \phi } } { { \partial { a _ { i } } } } } \right) } .
$$

The method can be easily extended to the case when $\pmb { H }$ contains $t$ explicitly. From a purely theoretical point of view the problem can be solved completely by the aggregate of such series.But these series are unsatisfactory. On one hand, they are convergent in a very limited interval of time and their analytical continuation is very difficult in most cases.On the other hand, the nature and the number of the distinct types of the possible motion are not known from such series. For example,in the three-body problem we want to classify all kinds of possible orbits and the period,if any,and to know various remarkable characteristics including the stability of the motion.The necessity of analytic continuation can be made by means of regularizing variables,such as those of Sundman,Levi-Civita,or Birkhoff in the case of a binary collision in the three-body problem (Sections 17.9-17.19). The solution is then obtained in series proceeding with ascending powers of the new variable,but the same difficulty still remains.

Thus the solution in trigonometric series has been considered, merely by formal expansion. The integrals of planetary theory are obtained in series form,disregarding the convergence,in powers of the disturbing masses and also in powers of small quantities such as the eccentricities and orbital inclinations,and indeed in trigonometric series with linear functions of time as the arguments.In order to avoid the appearance of secular terms in the solution, various methods of integration have been proposed,as has been treated in Chapter 8 on the secular variation and in Chapters 9-12.If the series in trigonometric form were uniformly convergent, then the coordinates and momenta would be bounded and recurrent in character,and the motion would be stable in a certain sense.As will be shown in the next chapter, the series are unfortunately divergent. If the motion be known to be quasi-periodic in the sense of Section 2.10,or to be almost periodic in the sense of Sections 2.11-2.14, then the solution would be expressed in convergent series for quasi-periodic or almost periodic functions.This is the case for a conditionally periodic motion discussed in Section 2.7.The solution is expressed rigorously in the fom of multiple Fourier series,and the characteristics of the motion can be judged from the form of the integrals.The integrals are represented by trigonometric series with linear functions of time as arguments and are uniformly convergent, i.e.， the motion is quasiperiodic when the mean motions-the coefficients of time in the arguments of the trigonometric functions--are not connected by any linear homogeneous relation with integer coefficients.

However,as has been shown by Poincaré (1889,1893), the series, although divergent, represents the motion in a limited interval of time within an assigned error in the observational technique. That is why the series solutions,despite its divergence in the rigorous mathematical sense，are utilized in practical dynamical astronomy.In the present section we shall deal with this kind of representation. Later in this chapter various theories for obtaining the integrals of planetary theory or the three-body problem will be treated.

# 14.2IRREGULAR INTEGRALS

It is well known that Stirling's series

$$
\begin{array} { c } { { \log \Gamma ( x + 1 ) = \displaystyle { \frac { 1 } { 2 } \log \left( 2 \pi \right) + \left( x + \frac { 1 } { 2 } \right) \log x - x } } } \\ { { + \displaystyle { \frac { B _ { 1 } } { 1 \cdot 2 } \frac { 1 } { x } - \frac { B _ { 2 } } { 3 \cdot 4 } \frac { 1 } { x ^ { 2 } } + \frac { B _ { 3 } } { 5 \cdot 6 } \frac { 1 } { x ^ { 3 } } - \cdot \cdot \cdot , } } } \end{array}
$$

where $B _ { 1 } , B _ { 2 } , \ldots$ are Bernoulli's numbers,is divergent, but this expression can be employed conveniently for computing $\Gamma ( x + 1 )$ for a large value of $x$ . In fact,the terms at first decrease very rapidly and then increase indefinitely. If we stop at the smallest term, the error will be very small. Stirling's series represents asymptotically the function log $\Gamma ( x + 1 )$ . Denote the sum of the first $n$ terms by $S _ { n }$ , by involving the term $( - 1 ) ^ { n - 1 } B _ { n } / [ 2 n ( 2 n - 1 ) x ^ { n } ]$ ，then we see that the expression $x ^ { n + 1 } \left[ \log { \Gamma ( x + 1 ) } - S _ { n } \right]$ tends to zero as $x$ increases indefinitely.We say that a divergent series

$$
A _ { 0 } + { \frac { A _ { 1 } } { x } } + { \frac { A _ { 2 } } { x ^ { 2 } } } + \cdots + { \frac { A _ { n } } { x ^ { n } } } + \cdots
$$

represents asymptotically a function $\pmb { J } ( \pmb { x } )$ ,if $x ^ { n } ( J - S _ { n } )$ tends to zero as $x$ increases indefinitely,where $S _ { n }$ denotes the sum of the first $n + 1$ terms.Indeed,if $x$ is sufficiently large, then we have $x ^ { n } ( J - S _ { n } ) < \varepsilon ,$ where $\varepsilon$ is very small,and the error $J - S _ { n } = \varepsilon / x ^ { n }$ in the computation of $\boldsymbol { \jmath }$ by taking the first $n + 1$ terms is extremely small.Moreover, the error is smaller than the error $J - S _ { n - 1 } = ( A _ { n } + \varepsilon ) / x ^ { n }$ that results when we stop at the first $_ n$ terms.Thus the series（1） behaves like Stirling's series and the terms at first decrease rapidly and then increase indefinitely. Such series are called asymptotic series (Section 12.17). The study of asymptotic series was initiated by Poincaré and Stieltjes. The uniqueness theorem for asymptotic series has heen proved by Poincaré, Nevanlinna, and Carleman (Hardy, 1949 ； Borel, 1928).

Take two asymptotic series (Poincaré, 1886)

$$
\begin{array} { l } { { J ( x ) = A _ { 0 } + \displaystyle \frac { A _ { 1 } } { x } + \frac { A _ { 2 } } { x ^ { 2 } } + \cdots + \frac { A _ { n } } { x ^ { n } } + \cdots , } } \\ { { \mathrm { } } } \\ { { J ^ { \prime } ( x ) = A _ { 0 } ^ { \prime } + \displaystyle \frac { A _ { 1 } ^ { \prime } } { x } + \frac { A _ { 2 } ^ { \prime } } { x ^ { 2 } } + \cdots + \frac { A _ { n } ^ { \prime } } { x _ { n } } + \cdots , } } \end{array}
$$

and define by $S _ { n }$ and $S _ { n } ^ { \prime }$ respectively the sums of the first $n + 1$ terms of these series.By definition

$$
\operatorname* { l i m } _ { n \to \infty } x ^ { n } ( J - S _ { n } ) = \operatorname* { l i m } _ { n \to \infty } x ^ { n } ( J ^ { \prime } - S _ { n } ^ { \prime } ) = 0 .
$$

Construct the product of the two series according to the rule for multiplication of two convergent series and let the product be

$$
\Sigma = B _ { 0 } + \frac { B _ { 1 } } { x } + \frac { B _ { 2 } } { x ^ { 2 } } + \cdots + \frac { B _ { n } } { x ^ { n } } + \cdots ,
$$

and let the sum of the first $n + 1$ terms be $\Sigma _ { n }$ . Since $S _ { n } , S _ { n } ^ { \prime } , \Sigma _ { n }$ are polynomials of $1 / x$ ，we have $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } x ^ { n } ( S _ { n } S _ { n } ^ { \prime } - \Sigma _ { n } ) = 0 } \end{array}$ and

$$
\operatorname* { l i m } _ { n \to \infty } \frac { J } { S _ { n } } = \operatorname* { l i m } _ { n \to \infty } \frac { J ^ { \prime } } { S _ { n } ^ { \prime } } = 1 , \qquad \operatorname* { l i m } \frac { J } { A _ { 0 } } = \operatorname* { l i m } \frac { J ^ { \prime } } { A _ { 0 } ^ { \prime } } = 1 .
$$

From

$$
\begin{array} { r } { J = S _ { n } + \frac { \varepsilon } { x ^ { n } } , \qquad J ^ { \prime } = S _ { n } ^ { \prime } + \frac { \varepsilon ^ { \prime } } { x ^ { n } } , \qquad \operatorname* { l i m } \varepsilon = \operatorname* { l i m } \varepsilon ^ { \prime } = 0 } \end{array}
$$

we obtain

$$
J J ^ { \prime } = S _ { n } S _ { n } ^ { \prime } + \frac { S _ { n } ^ { \prime } \varepsilon + S _ { n } \varepsilon ^ { \prime } + ( \varepsilon \varepsilon ^ { \prime } / x ^ { n } ) } { x ^ { n } } .
$$

Since lim $S _ { n } ^ { \prime } \varepsilon = 0$ ,lim $S _ { n } \varepsilon ^ { \prime } = 0$ ,lim $\varepsilon \varepsilon ^ { \prime } / x ^ { n } = 0$ ，we have

$$
\operatorname * { l i m } x ^ { n } ( J J ^ { \prime } - S _ { n } S _ { n } ^ { \prime } ) = 0 , \qquad \operatorname * { l i m } x ^ { n } ( J J ^ { \prime } - \Sigma _ { n } ) = 0 .
$$

Hence

$$
J J ^ { \prime } = B _ { 0 } + { \frac { B _ { 1 } } { x } } + { \frac { B _ { 2 } } { x ^ { 2 } } } + \cdots + { \frac { B _ { n } } { x ^ { n } } } + \cdots
$$

is an asymptotic series.

An asymptotic series is obtained if we raise an asymptotic series to any higher power. Let

$$
S = A _ { 0 } + \frac { A _ { 1 } } { x } + \frac { A _ { 2 } } { x ^ { 2 } } + \cdots
$$

be a divergent series representing asymptotically a function $\pmb { J }$ .We raise the series $S - A _ { 0 }$ to any power and obtain the series $( S - A _ { 0 } ) ^ { n }$ arranged in powers of $1 / x$ and representing asymptotically $( J - A _ { 0 } ) ^ { n }$ Let

$$
F ( z ) = B _ { 0 } + B _ { 1 } z + \cdot \cdot \cdot + B _ { n } z ^ { n }
$$

be a holomorphic function of $z$ in the neighborhood of $z = 0$ . The series is convergent. If we form a divergent series

$$
B _ { 0 } + B _ { 1 } ( S - A _ { 0 } ) + \cdots + B _ { n } ( S - A _ { 0 } ) ^ { n } + \cdots
$$

and arrange in powers of $1 / x$ ，then we get a divergent series

$$
\Sigma = C _ { 0 } + \frac { C _ { 1 } } { x } + \frac { C _ { 2 } } { x ^ { 2 } } + \cdots + \frac { C _ { n } } { x ^ { n } } + \cdots .
$$

It is seen that this series represents asymptotically the function $F ( J - A _ { 0 } )$ . In fact, if we define by $\Sigma _ { n }$ the sum of the first $n + 1$ terms of the series and by $\Sigma _ { n } ^ { \prime }$ the sum

$$
\Sigma _ { n } ^ { \prime } = B _ { 0 } + B _ { 1 } ( S _ { n } - A _ { 0 } ) + B _ { 2 } ( S _ { n } - A _ { 0 } ) ^ { 2 } + \cdot \cdot \cdot + B _ { n } ( S _ { n } - A _ { 0 } )
$$

and arrange the two sums in powers of $1 / x ,$ ，then we find

$$
\operatorname* { l i m } _ { n \to \infty } x ^ { n } ( \Sigma _ { n } - \Sigma _ { n } ^ { \prime } ) = 0 ,
$$

and further

$$
\operatorname* { l i m } _ { n \to \infty } x ^ { n } [ F ( J - A _ { 0 } ) - \Sigma _ { n } ^ { \prime } ] = 0 .
$$

Put

$$
T _ { n } = B _ { 0 } + B _ { 1 } ( J - A _ { 0 } ) + \cdots + B _ { n } ( J - A _ { 0 } ) ^ { n } ,
$$

then we have

$$
\operatorname* { l i m } _ { n \to \infty } x ^ { n } ( T _ { n } - \Sigma _ { n } ^ { \prime } ) = 0 , \qquad \operatorname* { l i m } _ { n \to \infty } x ^ { n } ( F - T _ { n } ) = 0 .
$$

Hence we can substitute an asymptotic series in the expansion of a holomorphic function as if it were a convergent series.

If we form

$$
1 + S + S ^ { 2 } + \cdots + S ^ { n } + \ldots .
$$

from the above series $s$ ， and arrange in powers of $1 / x$ ， then we get an asymptotic series asymptotically representing the function $1 / ( 1 - J )$ Thus we can divide two asymptotic series in the same way as two convergent series,provided that the divisor series is not zero.

We can likewise integrate an asymptotic series in the same way as a convergent series.However it is not always possible to differentiate an asymptotic series.An asymptotic series may represent several different functions with the same argument $x$

Consider the integrals for large values of $| x |$ of a linear differential equation

$$
P _ { n } { \frac { d ^ { n } y } { d x ^ { n } } } + P _ { n - 1 } { \frac { d ^ { n - 1 } y } { d x ^ { n - 1 } } } + \cdot \cdot \cdot + P _ { 1 } { \frac { d y } { d x } } + P _ { 0 } y = 0 ,
$$

in which the coefficients $\pmb { P }$ are integral polynomials in $x$ . If the degree of the polynomials $P _ { n } , P _ { n - 1 } , \cdots , P _ { 0 }$ is constantly decreasing，then $_ n$ series of the form

$$
x ^ { \alpha } \big ( A _ { 0 } + \frac { A _ { 1 } } { x } + \frac { A _ { 2 } } { x ^ { 2 } } + \cdot \cdot \cdot \big ) ,
$$

where $_ { \alpha }$ is determined by the determining fundamental equation or the indicial equation in Fuchs's theory of a linear differential equation (see Section 3.7),satisfy the differential equation；and the series are convergent if $| x |$ is sufficiently large,i.e.，if these are the regular integrals.There is an exception when the difference of two roots of the determinantal equation for $_ { \alpha }$ is an integer；then a term log $x$ appears in the series. If the degree of the polynomials $P$ is never increasing but not always decreasing and if the degree of $P _ { 0 }$ is lower than that of $P _ { \pi }$ ， then there are in certain cases $m ( m < n )$ series of the above form formally satisfying the differential equation but not necessarily convergent.

If we put aside certain exceptional cases, it can be shown that there are $_ n$ series of the form

$$
e ^ { \boldsymbol { Q } } \boldsymbol { x } ^ { \alpha } \Big ( \boldsymbol { A } _ { 0 } + \frac { \boldsymbol { A } _ { 1 } } { x } + \frac { \boldsymbol { A } _ { 2 } } { x ^ { 2 } } + \boldsymbol { \cdot \cdot \cdot } \Big )
$$

formally satisfying the differential equation,where $Q$ is a polynomial in $x$ . Such a series is calleda normal series,and its order is the degree $p$ of the polynomial $\boldsymbol { Q }$ (Section 12.17).A normal series is not always convergent. If one of these series converges, then the equation is said to admit a normal integral； but this occurs only in certain exceptional cases.

If the determinantal equation for $_ { \alpha }$ has its roots differing only by an integer, then we obtain a series of the form

$$
x ^ { \alpha } [ \psi _ { 0 } + \psi _ { 1 } \log { x } + \psi _ { 2 } \log { \log { x } } + \cdot \cdot \cdot + \psi _ { q } \underbrace { \log \log { \cdot \cdot \cdot \log { x } } } _ { q } ] ,
$$

where the $\psi$ are series in powers of $1 / x$ . Such a series is called a logarithmic normal series of order $p$

Let $^ { a }$ be the coefficient of $x ^ { p }$ in $Q$ and suppose that none of the normal series satisfying (2) is of order higher than $p$ ； then $^ a$ is given by a certain equation. If this equation has multiple roots, the process of constructing the normal series becomes illusory. Then the series is of the form $e ^ { Q } x ^ { \alpha } \psi$ ，where $Q$ is a polynomial of degree higher than $( p - 1 ) n$ and not higher than $_ { p n }$ in $x ^ { 1 / \pi }$ ，and $\psi$ is arranged in increasing powers of $x ^ { - 1 / \mathfrak { n } }$ . Such a series is generally divergent and is called an abnormal series of order $p$ . Denote the degree of $P _ { i }$ by $M _ { i }$ and write $N _ { i } = ( M _ { i } - M _ { n } ) / ( n - i )$ Let $h$ be the largest of the $_ n$ quantities $N _ { i }$ .If $p$ is the integer equal to or immediately superior to $h$ ，then it can be shown that the normal series or the abnormal series formally satisfying the equation (2) are at most of order $p$ . The number $h$ is called the rank of the equation.We can show that $h \leq p$

At first we limit ourselves to the consideration of the cases of the normal series of the first order,that is, the cases in which the degree of each polynomial $P$ in (2) is not higher than the degree $_ { m }$ of $P _ { n }$ Let $\boldsymbol { A } _ { i }$ be the coefficient of $x ^ { m }$ in $P _ { i }$ ，and form

$$
A _ { n } a ^ { n } + A _ { n - 1 } a ^ { n - 1 } + \cdot \cdot \cdot + A _ { 1 } a + A _ { 0 } = 0 .
$$

Suppose that the roots $a _ { 1 } , a _ { 2 } , \cdots , a _ { n }$ of this equation are all distinct; then the equation (2) is satisfied by $n$ normal series of the first order of the form

$$
e ^ { a _ { 1 } x } x ^ { \alpha _ { 1 } } \phi _ { 1 } , \qquad e ^ { a _ { 2 } x } x ^ { \alpha _ { 2 } } \phi _ { 2 } , . . . , e ^ { a _ { 7 } x ^ { \alpha _ { 7 } } } \phi _ { n } ,
$$

where $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n }$ are suitably chosen constants, and $\phi _ { 1 } , \phi _ { 2 } , \ldots , \phi _ { n }$ are series arranged in increasing powers of $1 / x$

Consider the Laplace transform (4b) (Ince,1927) of (2)

$$
Q _ { m } \frac { d ^ { m } v } { d z ^ { m } } + Q _ { m - 1 } \frac { d ^ { m - 1 } v } { d z ^ { m - 1 } } + \cdot \cdot \cdot + Q _ { 1 } \frac { d v } { d z } + Q _ { 0 } v = 0 ,
$$

where the $\boldsymbol { Q }$ are polynomials of degree at most $_ n$ in $z$ and

$$
\mathcal { Q } _ { m } = ( z - a _ { 1 } ) ( z - a _ { 2 } ) \cdot \cdot \cdot ( z - a _ { n } ) .
$$

Then (3) admits $_ n$ simple singular points

$$
z = a _ { 1 } , \qquad z = a _ { 2 } , \qquad \ldots , \qquad z = a _ { n } .
$$

Let the roots of the determinantal equation relative to the singular point $z = a _ { i }$ be $0 , 1 , 2 , \ldots , m - 2$ and $\beta _ { i }$ ， where the $\beta _ { i }$ are supposed to be neither positive nor negative integers.Then there exist $m - 1$ integrals of (3） holomorphic in the neighborhood of $z = a _ { i }$ ，and the mth integral, which we call $v _ { i }$ ，is

$$
v _ { i } = ( z - a _ { i } ) ^ { \beta _ { i } } + C _ { 1 } ( z - a _ { i } ) ^ { \beta _ { i } + 1 } + C _ { 2 } ( z - a _ { i } ) ^ { \beta _ { i } + 2 } + \cdot \cdot \cdot .
$$

Construct a small circle with very small radius around the point $a _ { i }$ ， and let it cut the straight line parallel to the real axis in the negative direction at $b _ { i }$ . Take a closed contour $k _ { i }$ starting from the negative infinity to $b _ { i }$ along the above straight line and describing the circumference of the small circle up to $b _ { i }$ and leaving to infinity along the straight line in the negative direction. It has been proved (Poincaré, 1885) that the integral

$$
J _ { i } = \int _ { \not { k } _ { i } } v _ { i } e ^ { z x } d z
$$

taken along the closed contour $k _ { i }$ is an integral of the equation (2), provided that the real part of $x$ is sufficiently large,and in particular if $x$ is positive and large. Thus a normal series of the first order,even when it is divergent， represents asymptotically an integral of the equation which it satisfies formally.This normal series is written

$$
\frac { e ^ { \alpha { i } x } } { x ^ { \beta _ { i } + 1 } } + C _ { 1 } ( \beta _ { i } + 1 ) \frac { e ^ { \alpha { i } x } } { x ^ { \beta _ { i } + 2 } } + C _ { 2 } ( \beta _ { i } + 1 ) ( \beta _ { i } + 2 ) \frac { e ^ { \alpha { i } x } } { x ^ { \beta _ { i } + 3 } } + \cdot \cdot \cdot .
$$

If the normal series is convergent, then it represents an integral of the equation (2) and is called a normal integral.

To each singular point $a _ { i }$ there corresponds an integral of (2), whatever the argument $x$ is,but,when the argument varies,the integral does not remain the same.For a certain value of the argument the integral may suddenly pass to another which is not the analytic continuation of the former (Section 12.17).

In order that the normal series (4) be convergent for sufficiently large values of $x$ ，it is necessary and sufficient that

$$
[ C _ { n } ( \beta _ { i } + 1 ) ( \beta _ { i } + 2 ) \cdot \cdot \cdot ( \beta _ { i } + n ) ] ^ { 1 / n }
$$

should tend to a finite limit for $_ n$ infinite,or that $v _ { i }$ should be of the form $( z - a _ { i } ) ^ { \beta : } \phi ( z )$ ,where $\phi ( z )$ is a holomorphic function on the whole plane.

Next suppose that the polynomial $P _ { n }$ in the coefficients of (2) is of degree $_ m$ ， $P _ { n - 1 }$ of degree $( m + 1 )$ at most, $P _ { n - 2 }$ of degree $( m + 2 )$ at most, $\cdots , P _ { 1 }$ of degree $( m + n - 1 )$ at most,and $P _ { 0 }$ of degree $( m + n )$ at most. Then it can be shown that the equation (2) admits $\pmb { n }$ normal series of the second order $\phi _ { 1 } ( x ) , \phi _ { 2 } ( x ) , \cdot \cdot \cdot , \phi _ { n } ( x )$ ，where

$$
\phi _ { i } ( x ) = e ^ { a _ { i } x ^ { 2 } + b _ { i } x } x ^ { \alpha _ { i } } \psi _ { i } \left( \frac { 1 } { x } \right) ,
$$

$\psi ( 1 / x )$ being a series arranged in ascending powers of $1 / x$ but generally divergent.Also it is proved that the integration of (2） is reduced to that of (3) which is of rank 1. Hence we form the Laplace transform (4) of (3) and obtain $\pmb { u }$ in the form of a definite integral.

Let $y = f ( x )$ be any integral of (2) and put $u = f ( x ) f ( - x )$ . Change $_ x$ to $- x$ in the solution $y$ and call it $y _ { 1 }$ ，where $u = y y _ { 1 }$ . Then we get $n ^ { 2 } + 1$ equations

$$
\frac { d ^ { \alpha } u } { d x ^ { \alpha } } = \sum _ { \beta } \sum _ { r } F _ { \alpha \beta r } \frac { d ^ { \beta } y } { d x ^ { \beta } } \frac { d ^ { r } y _ { 1 } } { d x ^ { r } } \qquad { \binom { \alpha = 0 , 1 , 2 , \dots , n - 1 } { \beta = 0 , 1 , 2 , \dots , n - 1 } } ,
$$

where the $F _ { \alpha \beta \gamma }$ are series of rational functions of $x$ .If we eliminate $n ^ { 2 }$ products $( d ^ { \beta } y / d x ^ { \beta } ) ( d ^ { \tau } y _ { 1 } / d x ^ { \tau } )$ from these $( n ^ { 2 } + 1 )$ equations, we obtain

$$
Q _ { n ^ { 2 } } { \frac { d ^ { n ^ { 2 } } u } { d x ^ { n ^ { 2 } } } } + Q _ { n ^ { 2 } - 1 } { \frac { d ^ { n ^ { 2 } - 1 } u } { d x ^ { n ^ { 2 } - 1 } } } + \dots + Q _ { 1 } { \frac { d u } { d x } } + Q _ { 0 } u = 0 ,
$$

where the $\boldsymbol { Q }$ are polynomials of $x$ From $\pmb { u }$ we can compute $\boldsymbol { y } \boldsymbol { y } _ { 1 }$ ， $y _ { 1 } ( d y / d x )$ ,... by simple quadratures.

Suppose in general that the integration of the equation (2) is reduced to that of (3) of rank $p$ . Put

$$
u = f ( x ) f ( \alpha x ) f ( \alpha ^ { 2 } x ) \cdot \cdot \cdot f ( \alpha ^ { p - 1 } x ) ,
$$

where $_ \alpha$ is one of the pth roots of unity. Then $u$ satisfies an equation of the form (5) of rank $p$ and of order $n ^ { p }$ ,whose coefficients are polynomials of $x$ . The equation remains the same when $x$ is changed to $_ { \alpha x }$ .Put $x ^ { p } = t$ ; then we have

$$
{ \frac { d ^ { p } u } { d x ^ { p } } } = \sum { \frac { p ! } { ( p - q ) ! ( 2 q - p ) ! } } ( 2 x ) ^ { 2 q - p } { \frac { d ^ { q } u } { d t ^ { q } } } \qquad ( q \leq p \leq 2 q )
$$

and (5) becomes

$$
\sum Q _ { p } \frac { d ^ { p } u } { d x ^ { p } } = 0 \qquad ( n ^ { 2 } \geq p \geq 0 ) ,
$$

or

$$
\begin{array} { r l r } { \displaystyle { \sum _ { \vphantom { \ d { \frac { 1 } { 2 } } } } R _ { q } \frac { d ^ { q } u } { d t ^ { q } } = 0 , } } & { } & \\ { R _ { q } = \displaystyle { \sum _ { \vphantom { \ d { \frac { 1 } { 2 } } } } Q _ { p } ( 2 x ) ^ { 2 q - p } \frac { p ! } { ( p - q ) ! ( 2 q - p ) ! } \frac { \binom { 2 q \geq p \geq q } { p \leq n ^ { 2 } } , } { p \leq n ^ { 2 } } } , } & { } & { \binom { 2 q \geq p \geq q } { p \leq n ^ { 2 } } , } \end{array}
$$

$R _ { p }$ being a polynomial in $t$ ，This equation is of rank 1.After $\pmb { u }$ is obtained, $y$ is computed by $n ^ { p } + 1$ equations

$$
\begin{array} { l } { \displaystyle \frac { d ^ { \alpha } u } { d x ^ { \alpha } } = \displaystyle \sum _ { \alpha } F _ { \alpha \beta \tau \cdots \alpha } \frac { d ^ { \beta } y } { d x ^ { \beta } } \frac { d ^ { \tau } y _ { 1 } } { d x ^ { \tau } } \cdot \cdot \cdot \frac { d ^ { \lambda } y _ { n - 1 } } { d x ^ { \lambda } } , } \\ { \displaystyle ( \alpha = 0 , 1 , 2 , \ldots , n ^ { p } ; \beta , \gamma , \ldots , \lambda = 0 , 1 , 2 , \ldots , n - 1 ) , } \end{array}
$$

where the $\pmb { F }$ are rational functions of $_ x$ and the $y _ { p }$ are the functions $f ( \alpha ^ { q } x )$ .From the first $n ^ { q }$ of these equations we get $n ^ { p }$ products $( d ^ { \beta } y / d x ^ { \beta } ) ( d ^ { \tau } y _ { 1 } / d x ^ { \tau } ) \cdot \cdot \cdot ( d ^ { 2 } y _ { p - 1 } / d x ^ { \lambda } )$ ，provided that the determinant of the coefficients is not zero. Thus,if $u$ is known,then $y$ is determined by a simple quadrature.It is shown that, in order for(5) to admit a normal integral, it is necessary and sufficient that the Laplace transform (4） should admit an integral of the form $v = ( z - a ) ^ { \alpha } G ( z )$ ， where $G ( z )$ is an entire function of $z$ .The function $y$ is represented asymptotically by a divergent series, in the case of rank 2 for example, of the form

$$
S = e ^ { a x ^ { 2 } + b x } x ^ { 2 } \phi ( x ) ,
$$

where $\phi ( x )$ is a series arranged in ascending powers of ${ 1 / x }$ .(Poincaré,1885，1886； Ince,1927；Schlesinger，1922；Poole,1936；van derCorput, 1956, 1957；Pittnauer, 1972).

Poincaré (1885,1886),Horn (1897,1897a,1898,1898a,1899, 1900,1900a,1908,1912,1924),Kneser (1896,1897,1897a,1899), Birkhoff (1908，1909，1912，1913，1913a，1913b)，Birkhoff and Langer (1923),Langer (1949),Murray (1923),Turrittin (1955),Bellmann (1943,1947,1953),Levinson (1948), Coddington and Levinson (1955),and Hukuhara (1937, 1937a) discussed an asymptotic representation of the solution of a differential equation (Ince,1927). While Poincaré and Kneser and later Horn (1914,1915,1916) treated the problem by transforming the dependent variable from $y ( x )$ to $v ( x )$ by means of the Laplace transformation (Widder, 1946)

$$
y = \int v e ^ { z x } d z ,
$$

Horn in earlier years referred to the method of successive approximation. Birkhoff studied the differential equation

$$
\frac { d ^ { n } y } { d x ^ { n } } + \rho a _ { n - 1 } ( x , \rho ) \frac { d ^ { n - 1 } y } { d x ^ { n - 1 } } + \cdot \cdot \cdot + \rho ^ { n } a _ { 0 } ( x , \rho ) y = 0
$$

for large values of the parameter $\rho$ , under the assumption that $a _ { i } ( x , \rho )$ are complex analytic functions of $\rho$ with derivatives of all orders with respect to $x$ (Schlesinger,-1895,1907) by associating it to the Sturm-Liouville boundary-value problem. Tamarkin and Besikowitsch (1924) discussed the differential equations

$$
{ \frac { d y _ { i } } { d x } } = \sum _ { k = 1 } ^ { n } \ a _ { i k } { ( x , \rho ) } \cdot y _ { k } \qquad ( i = 1 , 2 , \ldots , n )
$$

where $a = ( a _ { i k } )$ is of the form

$$
\imath \equiv \rho ^ { p } [ a ^ { ( p ) } ( x ) + \frac { 1 } { \rho } a ^ { ( p - 1 ) } ( x ) + \cdot \cdot \cdot + \frac { 1 } { \rho ^ { p - 1 } } a ^ { ( 1 ) } ( x ) + \frac { 1 } { \rho ^ { p } } \sum _ { \nu = 0 } ^ { \infty } \rho ^ { - \nu } a ^ { ( - \nu ) } (
$$

On the other hand, Horn considered a differential equation of the Sturm-Liouville type :

$$
{ \frac { d ( A ( d y / d x ) ) } { d x } } + ( k ^ { 2 } B + C ) y = 0 ,
$$

where $A , B , C$ are real functions of $x , a \leq x \leq b$ and $k$ is an arbitrary parameter. The integral $y$ ，together with its derivative $d y / d x ,$ is supposed to be independent of $k$ for $x = a$ .It is known that the integral $\boldsymbol { y }$ is an entire or integral transcendental function of $_ x$ if $A , B , C$ are integral rational functions of $x$ . The solution is expanded in the form

$$
y = \cos k \omega \Big ( \phi _ { 0 } + \frac { \phi _ { 2 } } { k ^ { 2 } } + \cdot \cdot \cdot \Big ) + \sin k \omega \Big ( \frac { \phi _ { 1 } } { k } + \frac { \phi _ { 3 } } { k ^ { 3 } } + \cdot \cdot \cdot \Big ) ,
$$

where $\omega , \phi _ { 0 } , \phi _ { 1 } , \ldots .$ are functions of $_ x$ ， only in formal aspect, in the neighborhood of the essential singularity $k = \infty$ . For the asymptotic representation of a Bessel function he obtained

$$
\begin{array} { c } { { J _ { n } \sim \exp \left\{ n \Big ( 1 + \log \frac { x } { 2 } \Big ) - \Big ( n + \frac 1 2 \Big ) \log n \right\} } } \\ { { \cdot \Big ( C _ { 0 } + \frac { C _ { 1 } } { n } + \cdot \cdot \cdot + \frac { C _ { \mu } } { n ^ { \mu } } + \frac { \Gamma _ { \mu } } { n ^ { \mu } } \Big ) , } } \end{array}
$$

where $\Gamma _ { \mu }$ tends to zero uniformly as $\pmb { n }$ goes to infnity with its argument between $- \pi + \delta$ and $\pi - \delta$ .Horn obtained for the hypergeometric functions of Gauss (Section 5.12)

$$
F ( \alpha , \beta , \gamma , x ) \sim 1 + \frac { c _ { 1 } } { \gamma } + \frac { c _ { 2 } } { \gamma ^ { 2 } } + \cdots ,
$$

when $\gamma$ goes to infinity with $- \pi < \arg \gamma < \pi$ ；

$$
\begin{array} { r } { F ( \alpha , \beta , \gamma , x ) \sim \exp { \left\{ ( \beta - \gamma ) \log { \alpha } - \alpha \log { ( 1 - x ) } \right\} } \cdot \mathfrak { P } _ { 1 } \Big ( \frac { 1 } { \alpha } \Big ) } \\ { + \exp { \{ - \beta \log { \alpha } \} } \cdot \mathfrak { P } _ { 2 } \Big ( \frac { 1 } { \alpha } \Big ) , } \end{array}
$$

when $\alpha$ goes to infinity with its argument between O and $\pi$ ; and

$$
\begin{array} { r } { F ( \alpha , \beta , \gamma , x ) \sim \exp { \{ ( \beta - \gamma ) \log { \alpha } - \alpha \log { ( 1 - x ) } \} } \cdot \mathfrak { P } _ { 1 } \Big ( \frac { 1 } { \alpha } \Big ) } \\ { + \exp { \{ - \beta \log { \alpha } \} } \cdot \exp { \{ - 2 \pi \sqrt { - 1 } \ \beta \} } \cdot \mathfrak { P } _ { 2 } \Big ( \frac { 1 } { \alpha } \Big ) , } \end{array}
$$

when $_ { \alpha }$ goes to infinity with $- \pi < \arg \alpha < 0$

Consider a linear differential equation (Section 12.7)

$$
\begin{array} { c } { { \frac { d ^ { m } y } { d x ^ { m } } + x ^ { k } P _ { 1 } \frac { d ^ { m - 1 } y } { d x ^ { m - 1 } } + x ^ { 2 k } P _ { 2 } \frac { d ^ { m - 2 } y } { d x ^ { m - 2 } } + \ O \cdot \cdot \cdot } } \\ { { \ } } \\ { { \qquad + \ x ^ { ( m - 1 ) k } P _ { m - 1 } \frac { d y } { d x } + x ^ { m k } P _ { m } y = 0 , } } \end{array}
$$

where $P _ { 1 } , P _ { 2 } , \ldots , P _ { n }$ are expanded in convergent power series of $1 / x$ Poincaré(1886) called $k + 1$ the rank of the differential equation at the singularity $x = \infty$ ．Suppose that the coefficients are rational functions of $x$ ，Horn considered the cases $k = 0$ (1897,1898) and $m = 2$ (1900a).In particular, the solution for the singularity $x = \infty$ of a differential equation

$$
\frac { d ^ { 2 } y } { d x ^ { 2 } } + P _ { 1 } \frac { d y } { d x } + P _ { 2 } y = 0 ,
$$

$$
P _ { i } = a _ { i } + { \frac { a _ { i } ^ { \prime } } { x } } + { \frac { a _ { i } ^ { \prime \prime } } { x ^ { 2 } } } + \cdots \qquad ( i = 1 , 2 ) ,
$$

is asymptotically represented by Thomé's normal series

$$
S _ { j } = e ^ { \alpha _ { j } x } x ^ { \rho _ { j } } \Big ( \Phi _ { j } + \frac { \gamma _ { j } } { x ^ { n + 1 } } \Big ) ,
$$

$$
\Phi _ { j } = 1 + { \frac { A _ { j 1 } } { x } } + { \frac { A _ { j 2 } } { x ^ { 2 } } } + \cdot \cdot \cdot + { \frac { A _ { j n } } { x ^ { n } } } \qquad ( j = 1 , 2 ) ,
$$

where the $\alpha _ { j }$ are the roots of $\alpha ^ { 2 } + a _ { 1 } \alpha + a _ { 2 } = 0$ and

$$
\rho _ { j } = - \frac { a _ { 1 } ^ { \prime } \alpha _ { j } + a _ { 2 } ^ { \prime } } { 2 \alpha _ { j } + a _ { 1 } }
$$

in the domain $- \pi \leqq \arg x \leqq \pi$ for $j = 1$ ，and in $0 \leq \arg x \leq 2 \pi$ for $j = 2$ ; or in the domain respectively $\pi \leq \arg x \leq { \frac { 3 } { 2 } } \pi - \delta$ and $- \textstyle { \frac { 3 } { 2 } } \pi \ +$ $\delta \leq \arg x \leq - \pi , 0 < \delta < { \frac { 1 } { 2 } } \pi$ . Horn gave the estimate of the magnitude of $\gamma _ { j }$ in these domains. Suppose that

$$
D ( y ) \equiv \frac { d ^ { m } y } { d x ^ { m } } + P _ { 1 } \frac { d ^ { m - 1 } y } { d x ^ { m - 1 } } + \cdot \cdot \cdot + P _ { m - 1 } \frac { d y } { d x } + P _ { m } y = 0 ,
$$

where

$$
P _ { j } = a _ { j } + \frac { a _ { j } ^ { \prime } } { x } + \frac { a _ { j } ^ { \prime \prime } } { x ^ { 2 } } + \ \cdot \cdot \cdot ( j = 1 , 2 , \ldots , n )
$$

are regular in the neighborhood of $x = \infty$ ．If the characteristic equation

$$
\alpha ^ { m } + a _ { 1 } \alpha ^ { m - 1 } + \cdot \cdot \cdot + a _ { m - 1 } \alpha + a _ { m } = 0
$$

has m distinct roots $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { m }$ ， then the differential equation is satisfied by Thomé's normal series

$$
\begin{array} { r l } & { S _ { j } = e ^ { \alpha _ { j } x } x ^ { \rho _ { j } } \cdot \Phi _ { j } , } \\ & { \Phi _ { j } = 1 + \cfrac { A _ { j 1 } } { x } + \cfrac { A _ { j 2 } } { x ^ { 2 } } + \dots \qquad ( j = 1 , 2 , \dots , m ) . } \end{array}
$$

Horn (1908) has shown for $m = 3$ that,if the roots of $\alpha ^ { 3 } + a _ { 1 } \alpha ^ { 2 } +$ $a _ { 2 } \alpha + a _ { 3 } = 0$ are distinct and lie on a straight line,then $\alpha _ { 2 } - \alpha _ { 1 }$ and $\alpha _ { 3 } - \alpha _ { 2 }$ are real and positive. The corresponding asymptotic solutions are

$$
\begin{array} { r l } { \eta _ { 1 } \sim S _ { 1 } \quad } & { \mathrm { f o r } \quad \pi / 2 < \arg x < 3 \pi / 2 , } \\ { \eta _ { 2 } \sim S _ { 2 } \quad } & { \mathrm { f o r } \quad - \pi / 2 < \arg x < 3 \pi / 2 , } \\ { \tilde { \eta } _ { 2 } \sim S _ { 2 } \quad } & { \mathrm { f o r } \quad \pi / 2 < \arg x < 5 \pi / 2 , } \\ { \eta _ { 3 } \sim S _ { 3 } \quad } & { \mathrm { f o r } \quad - \pi / 2 < \arg x < 5 \pi / 2 ; } \end{array}
$$

and that, if the roots $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ are not on a straight line, then the corresponding asymptotic solutions are

$$
\begin{array} { r l } { \eta _ { 1 } \sim S _ { 1 } } & { \quad \mathrm { f o r } \quad - 2 \pi + \vartheta _ { 1 } < \arg x < \pi , } \\ { \tilde { \eta } _ { 1 } \sim S _ { 1 } } & { \quad \mathrm { f o r } \quad 0 < \arg x < \pi + \vartheta _ { 1 } , } \\ { \eta _ { 2 } \sim S _ { 2 } } & { \quad \mathrm { f o r } \quad - \pi < \arg x < 2 \pi - \vartheta _ { 2 } , } \\ { \tilde { \eta } _ { 2 } \sim S _ { 2 } } & { \quad \mathrm { f o r } \quad - \pi - \vartheta _ { 2 } < \arg x < 0 , } \\ { \eta _ { 3 } \sim S _ { 3 } } & { \quad \mathrm { f o r } \quad - 2 \pi - \vartheta _ { 2 } < \arg x < \vartheta _ { 1 } , } \\ { \tilde { \eta } _ { 3 } \sim S _ { 3 } } & { \quad \mathrm { f o r } \quad - \pi + \vartheta _ { 1 } < \arg x < \pi - \vartheta _ { 2 } , } \end{array}
$$

where $\vartheta _ { 1 } , \vartheta _ { 2 } , \vartheta _ { 3 }$ are the interior angles of the triangle $\alpha _ { 1 } \alpha _ { 2 } \alpha _ { 3 }$

Next suppose that the rank at $\infty$ is $k + 1$ .For the differential equation

$$
\frac { d ^ { 2 } y } { d x ^ { 2 } } + x ^ { k } P _ { 1 } \frac { d y } { d x } + x ^ { 2 k } P _ { 2 } y = 0
$$

we put

$$
S _ { j } = e ^ { g _ { j } ( x ) } x ^ { \rho _ { j } } \Big ( 1 + \frac { A _ { j 1 } } { x } + \frac { A _ { j 2 } } { x ^ { 2 } } + \cdot \cdot \cdot \Big ) \qquad ( j = 1 , 2 ) ,
$$

where

$$
g _ { j } ( x ) = \alpha _ { j } { \frac { x ^ { k + 1 } } { k + 1 } } + \alpha _ { j 1 } { \frac { x ^ { k } } { k } } + \cdot \cdot \cdot + \alpha _ { j k } x
$$

are integral polynomials of $( k + 1 ) \mathrm { t h }$ degree in $x$ ， and where $\beta = \alpha _ { 2 }$ $- \alpha _ { 1 }$ is assumed to be real and positive.The asymptotic representation of the solution at $x = \infty$ is

$$
\eta _ { 1 } ^ { ( p ) } \sim S _ { 1 } \qquad ( p = 0 , 1 , 2 , \ldots , k ) ,
$$

$$
\frac { 2 p \pi } { k + 1 } - \frac { 3 \pi } { 2 ( k + 1 ) } < \arg x < \frac { 2 p \pi } { k + 1 } + \frac { 3 \pi } { 2 ( k + 1 ) } ,
$$

and

$$
\eta _ { 2 } ^ { ( p ) } \sim S _ { 2 } \qquad ( p = 0 , 1 , 2 , \ldots , k )
$$

for

$$
\frac { 2 p \pi } { k + 1 } - \frac { \pi } { 2 ( k + 1 ) } < \arg x < \frac { 2 p \pi } { k + 1 } + \frac { 5 \pi } { 2 ( k + 1 ) } .
$$

Horn further has shown that the rank of a differential equation is a generalization of the notion of genus (Geschlecht) of an entire function (Section 12.4;Horn,1924；Trjitzinsky,1935；Evans,1954).

Birkhoff (1909, 1913b) reduced the given system

$$
\frac { d y } { d x } = x ^ { k } A ( x ) y ,
$$

where $k$ is a non-negative integer and where $A ( x )$ isan $n \times n$ matrix whose components are convergent power series in $x ^ { - 1 }$ ，into a system

$$
{ \frac { d z } { d x } } = x ^ { k } B ( x ) z
$$

with at worst a regular singular point $x = 0$ (Section 3.7),where the components of $B ( x )$ are polynomials in $x ^ { - 1 }$ ，by the transformation $y = P ( x ) z$ ，where $P ( x )$ is an $n \times n$ matrix such that the components of $P ( x )$ are convergent power series in $x ^ { - 1 }$ and $\scriptstyle \operatorname* { l i m } _ { x \to \infty } P ( x )$ is nonsingular (Hukuhara,1937,1942；Malmquist,1940,1941；Turritin, 1955，1963；Wasow,1965；Lutz，1970).Saito (1963） studied the perturbation with a parameter $\varepsilon$ . Sibuya(1962,1968,1971) discussed the perturbation of asymptotic solutions by introducing an $r$ -dimensional parameter $\mu$ and a complex parameter $\varepsilon$ in the matrix $A ( x )$ such that $A ( x , \mu , \varepsilon )$ is expanded in powers of ε whose coefficients are also expanded in powers of $x ^ { - 1 }$

# 14.3SEMI-CONVERGENT SERIES

In the preceding chapters on the perturbation theory we have spoken of the convergence of series in the formal sense.When the terms of a series become smaller in general in absolute magnitude, we say that the series is formally convergent in the conventional terminology of celestial mechanics,although the series may not be mathematically convergent.A series is mathematically convergent even though the absolute values of the first finite number of terms may not decrease sufficiently rapidly. Such formally convergent series were called semi-convergent series by Poincaré (1889, 1893).

The series of Stirling is divergent mathematically. The terms of the series at first decrease in absolute value and then increase,and finally the series is divergent.But, if we truncate or cut off the series at the smallest term, then the series represents an approximation to the function represented.

The series

$$
\phi ( w , \mu ) = \sum _ { n } \frac { w ^ { n } } { 1 + n \mu }
$$

converges for all values of $w$ and $\mu$ such that

$$
| w | < w _ { 0 } , \qquad \mu \equiv 0 , \qquad 0 < w _ { 0 } < 1 ,
$$

and indeed absolutely and uniformly. But the series

$$
\sum _ { n } \ { \frac { w ^ { n } } { 1 + n \mu } } = \sum _ { n } \sum _ { p } \ w ^ { n } ( - 1 ) ^ { p } n ^ { p } \mu ^ { p }
$$

is not absolutely convergent. If we arrange it in the form

$$
A _ { 0 } - A _ { 1 } \mu + A _ { 2 } \mu ^ { 2 } - A _ { 3 } \mu ^ { 3 } + \cdot \cdot \cdot ,
$$

$$
A _ { 0 } = \sum _ { n } w ^ { n } , \qquad A _ { 1 } = \sum _ { n } n w ^ { n } , \qquad A _ { 2 } = \sum _ { n } n ^ { 2 } w ^ { n } ,
$$

$$
A _ { 3 } = \sum _ { n } n ^ { 3 } w ^ { n } , \ldots ,
$$

then the series in ascending powers of $\mu$ is divergent. In fact, we have

$$
k ^ { j } w ^ { j } < A _ { j } < \frac { j ! } { ( 1 - w ) ^ { j } }
$$

and $\textstyle \sum _ { j } ( - j w \mu ) ^ { j }$ is divergent and hence the series $\textstyle \sum _ { j } ( - 1 ) ^ { j } A _ { j } \mu ^ { j }$ is divergent.But the terms of the series

$$
\sum _ { j } { \frac { ( - \mu ) ^ { j } \cdot j ! } { ( 1 \ - \ w ) ^ { j } } }
$$

decrease very rapidly at first and then increase without limit,if $\mu / ( 1 - w )$ is very small.

$$
\phi _ { p } ( w , \mu ) = A _ { 0 } - A _ { 1 } \mu + A _ { 2 } \mu ^ { 2 } - A _ { 3 } \mu ^ { 3 } + \cdot \cdot \cdot + ( - 1 ) ^ { p } A _ { p } \mu ^ { p } ,
$$

then we have

$$
\frac { \phi - \phi _ { p } } { \mu ^ { p } } = ( - 1 ) ^ { p + 1 } \mu \cdot \sum _ { n } { \frac { n ^ { p + 1 } w ^ { n } } { 1 + n \mu } }
$$

and the series $\textstyle \sum _ { n } { \bigl \{ \bigl ( } n ^ { p + 1 } w ^ { n } \bigr ) / \bigl (  1 + n \mu ) \bigr \}$ converges uniformly. Hence we obtain, for $\mu = 0$ ，

$$
\operatorname* { l i m } _ { \pi \to \infty } \sum _ { n } { \frac { n ^ { p + 1 } w ^ { n } } { 1 + n \mu } } = \sum _ { n } n ^ { p + 1 } w ^ { n } = { \mathrm { f n i t e } } ,
$$

and hence

$$
\operatorname* { l i m } _ { p \to \infty } { \frac { \phi - \phi _ { p } } { \mu ^ { p } } } = 0 .
$$

Thus $\phi _ { p } ( w , \mu )$ represents approximately the function $\phi ( w , p )$

Consider a function $\phi ( x , \mu )$ and the corresponding divergent series arranged in powers of $\pmb { \mu }$

$$
f _ { 0 } + \mu f _ { 1 } + \mu ^ { 2 } f _ { 2 } + \cdots ,
$$

where the coefficients $f _ { 0 } , f _ { 1 } , \ldots$ are functions of $x$ .Put

$$
\phi _ { p } = f _ { 0 } + \mu f _ { 1 } + \cdot \cdot \cdot + \mu ^ { p } f _ { p } .
$$

If

$$
\operatorname* { l i m } _ { p \to \infty } \frac { \phi - \phi _ { p } } { \mu ^ { p } } = 0 ,
$$

then we say that the series represents the function $\phi$ asymptotically. If $\pmb { \mu }$ is sufficiently small, then $\phi - \phi _ { \mathfrak { p } }$ is very small although the series itself is divergent mathematically.We write

$$
\phi ( x , \mu ) \sim f _ { 0 } + \mu f _ { 1 } + \mu ^ { 2 } f _ { 2 } + \cdot \cdot \cdot .
$$

Consider next a system of differential equations

$$
\frac { d x _ { i } } { d t } = X _ { i } , \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

where the $X _ { i }$ are functions uniform in $t , x _ { 1 } , \ldots , x _ { n }$ and in a parameter $\pmb { \mu } _ { i }$ ，such that $X _ { i }$ are developable in ascending integral powers of $\pmb { \mu }$ Let $f _ { i , k }$ be known functions of $t , \mu$ and developable in convergent power series of $\pmb { \mu }$ ，and let

$$
S _ { k } = f _ { 0 k } + \mu f _ { 1 k } + \mu ^ { 2 } f _ { 2 k } + \cdot \cdot \cdot \quad \quad ( k = 1 , 2 , \ldots , n )
$$

be $_ n$ divergent series.Denote the sum of the first $p + 1$ terms of $S _ { k }$ by $\phi _ { p , k }$ . Suppose that, if we substitute $\phi _ { p 1 } , \phi _ { p 2 } , \ldots , \phi _ { p n }$ in place of $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ in the differential equations, then the differences $( d x _ { i } / d t ) - X _ { i }$ are divisible by $\mu ^ { p + 1 }$ . Then we say that the series $S _ { 1 { \mathrm { : } } }$ ， $S _ { 2 } , \ldots , S _ { n }$ formally satisfy the differential equations.Suppose further that $f _ { i k }$ vanish for $t = 0$ . Consider a particular solution of the differential equations which vanishes for $t = 0$ ，that is, $x _ { 1 } = x _ { 2 } = \cdots =$ $x _ { n } = 0$ for $t = 0$ ，and let

$$
x _ { 1 } = \theta _ { 1 } ( t , \mu ) , x _ { 2 } = \theta _ { 2 } ( t , \mu ) , \qquad \ldots , x _ { n } = \theta _ { n } ( t , \mu ) ,
$$

be such a solution. Then we have asymptotically

$$
\theta _ { 1 } ( t , \mu ) \sim S _ { 1 } , \qquad \theta _ { 2 } ( t , \mu ) \sim S _ { 2 } , \ldots , \qquad \theta _ { n } ( t , \mu ) \sim S _ { n } .
$$

In fact, put

$$
x _ { k } = \phi _ { p k } + \mu ^ { p + 1 } \hat { \xi } _ { k } \qquad ( k = 1 , 2 , \ldots , n ) ,
$$

and substitute these values of $x _ { k }$ in the differential equations；then we obtain

$$
\mu ^ { p + 1 } \frac { d \xi _ { k } } { d t } = X _ { k } - \frac { d \phi _ { p k } } { d t } ,
$$

where the $X _ { k }$ are developable in powers of $\mu , \mu ^ { p + 1 } \xi _ { 1 } , \ldots , \mu ^ { p + 1 } \xi _ { n }$ ，the coefficients being known functions of $t$ .Except when the particular solution $x _ { k } = \theta _ { k } ( t , 0 )$ ， $\mu = 0$ ，passes through one of the singular points of the differential equations for a certain value of $t$ ，we can find two positive numbers $M$ and $\alpha$ ，such that

$$
X _ { i } - \frac { d \phi _ { p i } } { d t } \ll \frac { M } { 1 - \alpha ( \mu + \mu ^ { p + 1 } \xi _ { 1 } + \cdot \cdot \cdot + \mu ^ { p + 1 } \xi _ { n } ) } \arg { ( \mu , \xi _ { k } ) } ,
$$

which means that the right-hand member is a majorant series of the left-hand member when expanded in powers of $\mu , \xi _ { 1 } , \xi _ { 2 } , \ldots , \xi _ { n }$ By our hypothesis the series $S _ { \kappa }$ satisfy formally the differential equations, that is, $X _ { i } - ( d \phi _ { p i } / d t )$ is divisible by $\mu ^ { p + 1 }$ if $\xi _ { 1 } = \xi _ { 2 } = { } \cdot \cdot \cdot = \xi _ { n } = 0$ ， 'that is, if $x _ { i } = \phi _ { p i }$ .Hence

$$
X _ { i } - \frac { d \phi _ { p i } } { d t } \leqslant \frac { M \mu ^ { p + 1 } \alpha ( \alpha ^ { p } + \mathfrak { f } _ { 1 } + \cdot \cdot \cdot + \mathfrak { f } _ { n } ) } { 1 - \alpha ( \mu + \mu ^ { p + 1 } \mathfrak { f } _ { 1 } + \cdot \cdot \cdot + \mu ^ { p + 1 } \mathfrak { f } _ { n } ) } .
$$

Denote the right-hand member by $\mu ^ { p + 1 } Z$ ， and put

$$
X _ { i } - \frac { d \phi _ { p i } } { d t } = \mu ^ { p + 1 } Y _ { i } ,
$$

then the differential equations become

$$
\frac { d \xi _ { i } } { d t } = Y _ { i } , \qquad Y _ { i } \ll Z _ { i } .
$$

Consider a particular solution of these differential equations such that $\xi _ { 1 } = \xi _ { 2 } = \cdot \cdot \cdot = \xi _ { n } = 0$ for $t = 0$ . Such a solution can be written

$$
\xi _ { i } = \frac { \theta _ { i } ( t , \mu ) - \phi _ { \mathscr { p } i } } { \mu ^ { p + 1 } } .
$$

The differential equations

$$
\begin{array} { r } { \frac { d \xi _ { i } } { d t } = Z } \end{array}
$$

can be integrated by writing $\xi _ { 1 } + \xi _ { 2 } + \cdot \cdot \cdot + \xi _ { n } = \sigma _ { : }$ ，that is, by considering $\xi _ { 1 } = \xi _ { 2 } = \cdot \cdot \cdot = \xi _ { n } = \sigma / n$ with

$$
\frac { d \sigma } { d t } = \frac { \mu \alpha ( \alpha ^ { p } + \sigma ) } { 1 - \alpha \mu - \sigma \mu ^ { p + 1 } } .
$$

The solution $\pmb { \sigma }$ is finite and tends to a finite limit for $\mu \to 0$ . Since $Y _ { i } \ll Z _ { i } ,$ ，we see that the solution $\boldsymbol { \xi } _ { i }$ of the differential equations $d \hat { \xi } _ { i } / d t = Y _ { i }$ is finite.Hence we have the asymptotic relation

$$
\theta _ { k } ( t , \mu ) \sim S _ { k } ^ { \mathrm { ~ \scriptsize ~ \cdot ~ } } ( k = 1 , 2 , \ldots , n ) .
$$

This theorem justifies the conventional methods in perturbation theory when $\mu$ is sufficiently small.

We can extend the result to the algebraic operations and differentiation and integration of semi-convergent series in a manner similar to the treatment of the asymptotic series of Section 14.2.

# THEORIES OF NEWCOMB AND LINDSTEDT

# 14.4NEWCOMB's THEORY

As has been shown in Chapter 12, the integral of a linear differential equation with periodic coefficients is formally expressed as trigonometric series with linear functions of time as arguments. The problem at hand is to study the form of the integrals arising in perturbation theory and in the three-body problem.It has been shown by Newcomb, Lindstedt,Bohlin，Gyldén,Poincaré,and Whittaker that these integrals can be expressed likewise in the form of trigonometric series with linear functions of time as arguments,with positive integral powers of the disturbing masses on one hand and of the small quantities such as the eccentricities and orbital inclinations on the other as coefficients. However,as we shall show in the next chapter, following Poincaré, the series are not uniformly convergent, although the formal aspect of the series representation is the same as for the quasi-periodic functions of Bohl and Esclangon (Sections 2.10 and 2.12). Because the series are not uniformly convergent they are not endowed with the properties of quasi-periodic functions and the characteristics of the solution cannot be predicted merely by a study of the formal appearance.

Newcomb (1874) has formally expressed the solution of perturbation theory in the requisite form by starting with the theory of secular variations incorporating the ordinary perturbations of short periods.

We have seen in Section 8.13 that the eccentricities and inclinations of planets are represented by

with $f _ { 1 } = 0$ . That this is true also for higher degrees has been shown in Section 12.30. We have proved in Sections 8.2 and 8.3 that the coordinates of planets are expressed in the form

$$
\begin{array} { c } { { m ^ { \prime } h _ { \mathrm { \tiny ~ s i n } } ^ { \mathrm { \tiny ~ c o s } } ( i l + i ^ { \prime } l ^ { \prime } + j \varpi + j ^ { \prime } \varpi ^ { \prime } + k \Omega + k ^ { \prime } \Omega ^ { \prime } ) } } \\ { { ( i + i ^ { \prime } + j + j ^ { \prime } + k + k ^ { \prime } = 0 ) , } } \end{array}
$$

where the coefficient $h$ is written

$$
h = \sum _ { } A e ^ { j } e ^ { \prime \prime ^ { \prime } } I ^ { k } I ^ { \prime k ^ { \prime } } ( 1 + A _ { 1 } e ^ { 2 } + A _ { 2 } e ^ { \prime 2 } + \cdot \cdot \cdot ) .
$$

Put

$$
\begin{array} { c } { { \lambda _ { j } = g _ { j } t + \beta _ { j } , \qquad \lambda _ { j } ^ { \prime } = f _ { j } t + \gamma _ { j } , \qquad \Lambda = \exp \{ \sqrt { - 1 } \lambda \} , } } \\ { { \Lambda ^ { \prime } = \exp \{ \sqrt { - 1 } \lambda ^ { \prime } \} , \qquad \Pi = \exp \{ \sqrt { - 1 } \varpi \} , } } \\ { { = \exp \{ \sqrt { - 1 } \varpi ^ { \prime } \} , \quad \Theta = \exp \{ \sqrt { - 1 } \Omega \} , \qquad \Theta ^ { \prime } = \exp \{ \sqrt { - 1 } \Omega ^ { \prime } } }  \end{array}
$$

then the formulas for the secular variations are transformed to

$$
\begin{array} { r l r } { \boldsymbol { e } \Pi = \displaystyle \sum _ { j } M _ { j } \Lambda _ { j } , } & { { } } & { \boldsymbol { e } \Pi ^ { - 1 } = \displaystyle \sum _ { j } M _ { j } \Lambda _ { j } ^ { - 1 } , } \\ { \boldsymbol { I } \Theta = \displaystyle \sum _ { j } { \cal Q } _ { j } \Lambda _ { j } ^ { \prime } , } & { { } } & { \boldsymbol { I } \Theta ^ { - 1 } = \displaystyle \sum _ { j } { \cal Q } _ { j } \Lambda _ { j } ^ { \prime - 1 } . } \end{array}
$$

Hence the coefficients

$$
{ } + A _ { 1 } e ^ { 2 } + A _ { 2 } e ^ { \prime 2 } + \cdot \cdot \cdot ) A e ^ { j } e ^ { \prime \prime } { } ^ { I } I ^ { \prime } { } ^ { k } I ^ { \prime } { } ^ { \cos } \sin { ( j \varpi + j ^ { \prime } \varpi ^ { \prime } + k \Omega + k ^ { \prime } \Omega }
$$

of $\sin ^ { \mathtt { c o s } } ( i l + i ^ { \prime } l ^ { \prime } )$ can be represented by

$$
{ \frac { 1 } { 2 } } \left( e \Pi \right) ^ { j } ( e ^ { \prime } \Pi ^ { \prime } ) ^ { j ^ { \prime } } ( I \Theta ) ^ { k } ( I ^ { \prime } \Theta ^ { \prime } ) ^ { k ^ { \prime } } + { \Bigl ( } { \frac { e } { \Pi } } { \Bigr ) } ^ { j } { \Bigl ( } { \frac { e ^ { \prime } } { \Pi ^ { \prime } } } { \Bigr ) } ^ { j ^ { \prime } } { \Bigl ( } { \frac { I } { \Theta } } { \Bigr ) } ^ { k } { \Bigl ( } { \frac { I ^ { \prime } } { \Theta ^ { \prime } } } { \Bigr ) } ^ { k ^ { \prime } } ,
$$

or,after substituting (6),by

$$
\begin{array} { c } { { \stackrel { \cos } { \sin } ( j _ { 1 } \lambda _ { 1 } + j _ { 2 } \lambda _ { 2 } + \cdot \cdot \cdot \cdot + j _ { N } \lambda _ { N } + j _ { 1 } ^ { \prime } \lambda _ { 1 } ^ { \prime } + \cdot \cdot \cdot + j _ { N } ^ { \prime } \lambda _ { N } ^ { \prime } ) } } \\ { { \nonumber } } \\ { { ( j _ { 1 } + j _ { 2 } + \cdot \cdot \cdot \cdot + j _ { N } = j + j ^ { \prime } ; j _ { 1 } ^ { \prime } + j _ { 2 } ^ { \prime } + \cdot \cdot \cdot + j _ { N } ^ { \prime } = k + N } } \end{array}
$$

Thus the terms in question in the expressions for the coordinates can be written, when there are $\mathbf { N }$ planets,

$$
\begin{array} { r } { m ^ { \prime } A ^ { \prime } \stackrel { \cos } { \sin } ( i _ { 1 } l _ { 1 } + i _ { 2 } l _ { 2 } + \cdot \cdot \cdot \cdot + i _ { N } l _ { N } + j _ { 1 } \lambda _ { 1 } + \cdot \cdot \cdot + j _ { N } \lambda _ { N } } \\ { + \dot { J } _ { 1 } ^ { \prime } \lambda _ { 1 } ^ { \prime } + \cdot \cdot \cdot + \dot { J } _ { N } ^ { \prime } \lambda _ { N } ^ { \prime } ) , } \end{array}
$$

with

$$
i _ { 1 } + i _ { 2 } + \cdot \cdot \cdot + i _ { N } + j _ { 1 } + \cdot \cdot \cdot + j _ { N } + j _ { 1 } ^ { \prime } + \cdot \cdot \cdot + j _ { N } ^ { \prime } = 0 ,
$$

where $\ b { A ^ { \prime } }$ is a function of the semimajor axes $a _ { 1 } , a _ { 2 } , \cdots , a _ { N }$ ，and the 2N quantities $M _ { j }$ and $Q _ { j } ( j = 1 , 2 , . . . , N )$ . Thus the $3 \mathbf { N }$ coordinates of $\mathbf { N }$ planets are represented by trigonometric series with $\mathsf { 3 N }$ arguments which are all linear functions of $t$ .Hence the coordinates are expressed by

$$
\begin{array} { l }   x = \displaystyle \sum _ { \begin{array} { l } { X _ { i _ { 1 } \cdots j _ { 1 } \cdots j _ { 1 } ^ { \prime } \cdots } \cos { ( i _ { 1 } \lambda _ { 1 } + \cdots + i _ { 3 N } \lambda _ { 3 N } ) } , } \\ { { y = \displaystyle \sum _ { \begin{array} { l } { Y _ { i _ { 1 } \cdots j _ { 1 } \cdots j _ { 1 } ^ { \prime } \cdots } \sin { ( i _ { 1 } \lambda _ { 1 } + \cdots + i _ { 3 N } \lambda _ { 3 N } ) } , } \\ { { z = \displaystyle \sum _ { \begin{array} { l } { Z _ { i _ { 1 } \cdots j _ { 1 } \cdots j _ { 1 } \cdots } \sin { ( j _ { 1 } \lambda _ { 1 } + \cdots + j _ { 3 N } \lambda _ { 3 N } ) } , } \end{array} } } \end{array} } } } \end{array} } } \\ { { y = \displaystyle \sum _ { \begin{array} { l } { Y _ { i _ { 1 } \cdots j _ { 1 } \cdots j _ { 1 } ^ { \prime } \cdots } \sin { ( i _ { 1 } \lambda _ { 1 } + \cdots + i _ { 3 N } \lambda _ { 3 N } ) } , } \end{array} } } } \end{array}
$$

with

$$
i _ { 1 } + i _ { 2 } + \cdot \cdot \cdot + i _ { 3 N } = 1 , \qquad i _ { 1 } + j _ { 2 } + \cdot \cdot \cdot + j _ { 3 N } = 0 .
$$

Following Newcomb,we shall prove that the solutions of similar form are obtained even when higher-order perturbations are taken into account， provided that the question of convergence of the infinite process is disregarded.

Consider a system of differential equations

$$
\begin{array} { r } { \frac { d \hat { \xi } _ { i } } { d t } = \frac { \partial \Omega } { \partial \xi _ { i } } , \qquad \frac { d \eta _ { i } } { d t } = \frac { \partial \Omega } { \partial \eta _ { i } } , \qquad \frac { d \zeta _ { i } } { d t } = \frac { \partial \Omega } { \partial \zeta _ { i } } \qquad ( i = 1 , 2 , \cdots , n ) } \end{array}
$$

and $_ { 3 n }$ equations of the form

$$
\hat { \xi } _ { i } = \sum K _ { i } \cos { ( i _ { 1 } \lambda _ { 1 } + \cdot \cdot \cdot + i _ { 3 n } \lambda _ { 3 n } ) } ,
$$

$$
\begin{array} { l } { \displaystyle \eta _ { i } = \sum { K _ { i } \sin { ( i _ { 1 } \lambda _ { 1 } + \cdots + i _ { 3 n } \lambda _ { 3 n } ) } } , } \\ { \displaystyle \zeta _ { i } = \sum { K _ { i } ^ { \prime } \sin { ( j _ { 1 } \lambda _ { 1 } + \cdots + j _ { 3 n } \lambda _ { 3 n } ) } } \qquad ( i = 1 , 2 , \ldots , n ) , } \end{array}
$$

where $\xi _ { i } , \eta _ { i } , \zeta _ { i }$ are functions of $6 n$ arbitrary constants and time,and $\lambda _ { i } = n _ { i } t + \gamma _ { i }$ with $3 n$ arbitrary constants $\gamma _ { i }$ ，and while the constants $n _ { i } , K _ { i }$ and $K _ { i } ^ { \prime }$ are functions of $_ { 3 n }$ arbitrary constants $c _ { 1 } , c _ { 2 } , \ldots , c _ { 3 n } .$ Let $a _ { 1 } , a _ { 2 } , \ldots , a _ { 6 n }$ represent $\gamma _ { i }$ and $c _ { i }$ $( i = 1 , 2 , \ldots , 3 n )$ . Since

$$
\sum _ { j } \frac { \partial \xi _ { i } } { \partial a _ { j } } \frac { d a _ { j } } { d t } = 0 , \qquad \sum _ { j } \frac { \partial \eta _ { i } } { \partial a _ { j } } \frac { d a _ { j } } { d t } = 0 , \qquad \sum _ { j } \frac { \partial \zeta _ { i } } { \partial a _ { j } } \frac { d a _ { j } } { d t } = 0 ,
$$

it follows that

$$
\frac { d \hat { \xi } _ { i } } { d t } = \frac { \partial \hat { \xi } _ { i } } { \partial t } = \xi _ { i } ^ { \prime } , \frac { d \eta _ { i } } { d t } = \frac { \partial \eta _ { i } } { \partial t } = \eta _ { i } ^ { \prime } , \frac { d \zeta _ { i } } { d t } = \frac { \partial \zeta _ { i } } { \partial t } = \zeta _ { i } ^ { \prime } ,
$$

and that

$$
\sum _ { j = 1 } ^ { 6 n } \frac { \partial \xi _ { i } ^ { \prime } } { \partial a _ { j } } \frac { d a _ { j } } { d t } = \frac { \partial \Omega } { \partial \xi _ { i } } - \frac { \partial ^ { 2 } \xi _ { i } } { \partial t ^ { 2 } } ,
$$

or

$$
\sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { 6 n } \frac { \partial \xi _ { i } } { \partial a _ { k } } \frac { \partial \xi _ { i } ^ { \prime } } { \partial a _ { j } } \frac { d a _ { j } } { d t } = \frac { \partial \Omega } { \partial a _ { k } } - \sum _ { i = 1 } ^ { n } \frac { \partial ^ { 2 } \xi _ { i } } { \partial t ^ { 2 } } \frac { \partial \xi _ { i } } { \partial a _ { k } } ,
$$

From the last equation we obtain

$$
\sum _ { j = 1 } ^ { 6 n } \left( a _ { k } , a _ { j } \right) \frac { d a _ { j } } { d t } = \frac { \partial \Omega } { \partial a _ { k } } - \sum _ { i = 1 } ^ { n } \frac { \partial ^ { 2 } \xi _ { i } } { \partial t ^ { 2 } } \frac { \partial \xi _ { i } } { \partial a _ { k } } ,
$$

where the parentheses on the left-hand side represent the Poisson brackets.Put

$$
\begin{array} { r l } & { i _ { 1 } n _ { 1 } + \cdots + i _ { 3 n } n _ { 3 n } = b , \qquad i _ { 1 } \lambda _ { 1 } + \cdots + i _ { 3 n } \lambda _ { 3 n } = N , } \\ & { j _ { 1 } n _ { 1 } + \cdots + j _ { 3 n } n _ { 3 n } = b ^ { \prime } , \qquad j _ { 1 } \lambda _ { 1 } + \cdots + j _ { 3 n } \lambda _ { 3 n } = N ^ { \prime } , } \end{array}
$$

then

$$
\begin{array} { c } { { \displaystyle { \xi _ { i } ^ { \prime } = - \sum _ { { } } b K \sin N , \qquad \eta _ { i } ^ { \prime } = \sum _ { { } } b K \cos N , } } } \\ { { \displaystyle { \zeta _ { i } ^ { \prime } = \sum _ { { } } b ^ { \prime } K ^ { \prime } \cos N ^ { \prime } } , } } \end{array}
$$

where $\scriptstyle \sum$ denotes the $_ { 3 n }$ -ple summation

$$
\sum = \sum _ { i _ { 1 } = - \infty } ^ { \infty } \sum _ { i _ { 2 } = - \infty } ^ { \infty } \cdot \cdot \cdot \sum _ { i _ { 3 n } = - \infty } ^ { \infty } .
$$

Denote a combination of $i _ { 1 } , i _ { 2 } , \ldots , i _ { 3 n }$ by $\nu$ or $\mu$ . Then, for example,

$$
\xi _ { i } = \sum _ { \mu } K _ { \mu } \cos N _ { \mu } , \qquad \xi _ { i } ^ { \prime } = - \sum _ { \nu } ( b K ) , \sin N _ { \nu } ,
$$

$$
\begin{array} { l } { \displaystyle \frac { \partial \xi _ { i } } { \partial a _ { k } } = \sum _ { \mu }  \{ \frac { \partial K _ { \mu } } { \partial a _ { k } } \cos N _ { \mu } - K _ { \mu } \frac { \partial b _ { \mu } } { \partial a _ { k } } t \sin N _ { \mu } \} , } \\ { \displaystyle \frac { \partial \xi _ { i } ^ { \prime } } { \partial a _ { j } } = \sum _ { \nu }  \{ - \frac { \partial ( b K ) _ { \nu } } { \partial a _ { j } } \sin N _ { \nu } - ( b K ) _ { \nu } \frac { \partial b _ { \nu } } { \partial a _ { j } } t \cos N _ { \nu } \} ,  } \end{array}
$$

and hence the Poisson brackets $( a _ { j } , a _ { k } )$ take the form

$$
\sum _ { i = 1 } ^ { n } \sum _ { \mu } \sum _ { \nu } \{ A _ { \mu , \nu } \sin { ( N _ { \mu } - N _ { \nu } ) } + A ^ { \prime } t + A ^ { \prime \prime } t ^ { 2 } \} .
$$

But in Section 1.9 it was shown that the Poisson brackets are inde-pendent of $t$ Hence $A ^ { \prime } = A ^ { \prime \prime } = 0$ ，and $A _ { \mu , \nu }$ do not depend on $N _ { \mu } -$ $N _ { \ast } =$ constant and are zero. Thus $i _ { 1 } + \cdots + i _ { 3 n } = 1$ ， $j _ { 1 } + \cdots + j _ { 3 n }$ $= 0$ are valid only if $i _ { 1 \mu } = i _ { 1 \nu } , \ i _ { 2 \mu } = i _ { 2 \nu }$ ，etc.Hence $( a _ { j } , a _ { k } )$ has no constant term and $( a _ { j } , a _ { k } ) = 0$ . Furthermore we can show that $( \gamma _ { j } , \gamma _ { k } )$ $= 0$ ， $( \gamma _ { j } , c _ { k } ) = 0$ ，and that

$$
\begin{array} { r l } & { \displaystyle \frac { d \gamma _ { i } } { d t } = - \Omega _ { i } ^ { \prime } , \qquad \Omega _ { i } ^ { \prime } = \frac { \partial \Omega } { \partial c _ { i } } - \sum _ { j = 1 } ^ { n } { \sqrt { \frac { \partial ^ { 2 } \xi _ { j } } { \partial t ^ { 2 } } } \frac { \partial \xi _ { j } } { \partial c _ { i } } + \frac { \partial ^ { 2 } \gamma _ { j } } { \partial t ^ { 2 } } \frac { \partial \eta _ { j } } { \partial c _ { i } } + \frac { \partial ^ { 2 } \zeta _ { j } } { \partial t ^ { 2 } } \frac { \partial \zeta } { \partial c } } } \\ & { \displaystyle \frac { d c _ { i } } { d t } = \Omega _ { i } , \qquad \Omega _ { i } = \frac { \partial c _ { i } } { \partial a _ { 1 } } \frac { d a _ { 1 } } { d t } + \dots + \frac { \partial c _ { i } } { \partial a _ { 3 n } } \frac { d a _ { 3 n } } { d t } . } \end{array}
$$

Now $\Omega$ can be written

$$
\Omega = \sum h \cos { ( i _ { 1 } \lambda _ { 1 } + \cdot \cdot \cdot + i _ { 3 \pi } \lambda _ { 3 \pi } ) }
$$

and we have also

$$
\begin{array} { r l r } {  { \frac { \partial \Omega } { \partial \gamma _ { j } } = - \sum _ { \mathrm { \ell } } h \sin N , } } \\ & { \frac { \partial \hat { \xi } } { \partial c _ { j } } = \sum _ { \mathrm { \ell } } \frac { \partial K } { \partial c _ { j } } \cos N + \mathrm { \ell } t \cdot \sum _ { \mathrm { \ell } } \frac { \partial b } { \partial c _ { j } } \sin N , } & \\ & { \frac { \partial \Omega } { \partial c _ { j } } = \sum _ { \mathrm { \ell } } ( \frac { \partial h } { \partial c _ { j } } \cos N - t h \frac { \partial b } { \partial c _ { j } } \sin N ) . } & \end{array}
$$

Hence

$$
\begin{array} { l } { { \displaystyle { \frac { d c _ { j } } { d t } = - \sum _ { i } h _ { j } ^ { \prime } \sin N , } } } \\ { { \displaystyle { \frac { d c _ { j } } { d t } = - \sum _ { i } h ^ { \prime \prime } \cos N + t \cdot \sum _ { j } h ^ { \prime \prime \prime } \sin N } , } } \end{array}
$$

where $h ^ { \prime \prime }$ and $h ^ { \prime \prime \prime }$ are obtained in a manner similar to $h ^ { \prime }$ . After integrating these equations we substitute the solution in the expressions for the coordinates $\xi _ { i } , \eta _ { i }$ and $\zeta _ { i }$ . Denote the perturbation by $\pmb { \delta }$ ,and let $\delta \lambda _ { i } = t \delta n _ { i } + \delta \gamma _ { i }$ .Then

$$
\delta \frac { d \lambda _ { i } } { d t } = \frac { d \gamma _ { i } } { d t } + t \frac { d n _ { i } } { d t } + \delta n _ { i } .
$$

Thus

$$
\begin{array} { r l } & { \frac { d c _ { j } } { d t } = \frac { \partial \Omega } { \partial \gamma _ { j } } - \displaystyle \sum _ { i = 1 } ^ { n } \left\{ \hat { \xi } _ { i } ^ { \prime \prime } \frac { \partial \hat { \xi } _ { i } } { \partial \gamma _ { j } } + \eta _ { i } ^ { \prime \prime } \frac { \partial \eta _ { i } } { \partial \gamma _ { j } } + \zeta _ { i } ^ { \prime \prime } \frac { \partial \zeta _ { i } } { \partial \gamma _ { j } } \right\} , } \\ & { \frac { d \gamma _ { j } } { d t } = - \frac { \partial \Omega } { \partial c _ { j } } + \displaystyle \sum _ { i = 1 } ^ { n } \left\{ \hat { \xi } _ { i } ^ { \prime \prime } \frac { \partial \hat { \xi } _ { i } } { \partial c _ { j } } + \eta _ { i } ^ { \prime \prime } \frac { \partial \eta _ { i } } { \partial c _ { j } } + \zeta _ { i } ^ { \prime \prime } \frac { \partial \zeta _ { i } } { \partial c _ { j } } \right\} . } \end{array}
$$

After making the necessary computation we can see that the terms with factor $t$ disappear from the right-hand sides because of the relations $\partial n _ { i } / \partial c _ { j } = \partial n _ { j } / \partial c _ { i }$ Hence

$$
\delta \frac { d \lambda _ { i } } { d t } = \left( \frac { d \gamma _ { i } } { d t } \right) + \delta n _ { i } ,
$$

where the parenthesis indicates that the terms with factor $\pmb { t }$ are omitted. From(7) we obtain

$$
\delta c _ { j } = \sum \frac { h _ { j } ^ { \prime } } { b } \cos N , \qquad ( \delta \gamma _ { j } ) = - \sum \frac { h _ { j } ^ { \prime \prime } } { b } \sin N ,
$$

and

$$
{ \mathfrak { I } } { \mathfrak { E } } = \sum { \frac { \partial { \boldsymbol { \xi } } } { \partial c _ { j } } } { \mathfrak { E } } { \mathfrak { c } } _ { j } + \sum { \frac { \partial { \boldsymbol { \xi } } } { \partial \gamma _ { j } } } { \mathfrak { d } } { \mathfrak { r } } _ { j } = \sum { \frac { \partial { \boldsymbol { \xi } } } { \partial c _ { j } } } { \mathfrak { d } } c _ { j } + \sum { \frac { \partial { \boldsymbol { \xi } } } { \partial \lambda _ { j } } } { \mathfrak { d } } { \mathfrak { z } } .
$$

Thus we have

$$
\delta n _ { i } = \sum \frac { \partial n _ { i } } { \partial c _ { j } } \delta c _ { j } = \sum \sum _ { j = 1 } ^ { 3 n } \frac { h _ { j } ^ { \prime } } { b } \frac { \partial n _ { i } } { \partial c _ { j } } \cos N .
$$

Further we find

$$
\delta \lambda _ { i } = ( \delta \gamma _ { i } ) + \int \delta n _ { i } d t = - \sum \left\{ \frac { h _ { i } ^ { \prime \prime } } { b } - \sum _ { j = 1 } ^ { 3 n } \frac { h _ { j } ^ { \prime } } { b ^ { 2 } } \frac { \partial n _ { i } } { \partial c _ { j } } \right\} \sin N ,
$$

or

$$
\begin{array} { r } { \delta \lambda _ { i } = \displaystyle \sum _ { \nu } L _ { i } \sin N , \qquad L _ { i } = - \frac { h _ { i } ^ { \prime \prime } } { b } - \displaystyle \sum _ { j = 1 } ^ { 3 n } \frac { h _ { j } ^ { \prime } } { b ^ { 2 } } \frac { \partial n _ { i } } { \partial c _ { j } } . } \end{array}
$$

The effect of $\delta c _ { i }$ in the expressions for $\xi _ { i } , \eta _ { i } , \zeta _ { i }$ is only to change $\kappa$ by an amount $\delta K$ ，so that

$$
\begin{array} { l } { { \displaystyle \partial \hat { \varepsilon } = \sum _ { \mu } \{ \delta K \cdot \cos N - K \sin N \cdot ( i _ { 1 } \partial \lambda _ { 1 } + \dots + i _ { \mathfrak { s n } } \partial \lambda _ { 3 n } ) \} , } } \\ { { \displaystyle \partial \eta = \sum _ { \mu } \{ \delta K \cdot \sin N + K \cos N \cdot ( i _ { 1 } \partial \lambda _ { 1 } + \dots + i _ { \mathfrak { s n } } \partial \lambda _ { 3 n } ) \} , } } \\ { { \displaystyle \partial \zeta = \sum _ { \mu } \{ \delta K ^ { \prime } \cdot \sin N ^ { \prime } + K ^ { \prime } \cos N ^ { \prime } \cdot ( j _ { 1 } \partial \lambda _ { 1 } + \dots + j _ { \mathfrak { s n } } \partial \lambda _ { 3 n } ) \} } } \end{array}
$$

Since we have

$$
\delta K = \sum \frac { \partial K } { \partial c _ { i } } \delta c _ { i } = \sum _ { \mu } \left( \sum \frac { h _ { i } ^ { \prime } } { b } \frac { \partial K ^ { \prime } } { \partial c _ { i } } \right) \cos N ,
$$

we obtain

$$
\delta \hat { \xi } = \frac { 1 } { 2 } \sum _ { \mu } \sum _ { \nu } \left\{ \sum _ { i } \left( \frac { h _ { i } ^ { \prime } } { b } \frac { \partial K } { \partial c _ { i } } \right) _ { \nu } + K _ { \mu } ( i _ { 1 } L _ { 1 } + \cdot \cdot \cdot + i _ { 3 n } L _ { 3 n } ) \right\}
$$

$$
\quad + { \frac { 1 } { 2 } } \sum _ { \mu } \sum _ { \nu } \left\{ \sum _ { i } \left. { \frac { h _ { i } ^ { \prime } } { b } } { \frac { \partial K } { \partial c _ { i } } } \right. _ { \nu } - K _ { \mu } ( i _ { 1 } L _ { 1 } + \cdots + i _ { 3 \pi } L _ { 3 \pi } ) \right\}
$$

·cos $( N _ { \mu } - N _ { \nu } )$

$$
\delta \eta = \frac { 1 } { 2 } \sum _ { \mu } \sum _ { \nu } \left\{ \sum _ { i } \left( \frac { h _ { i } ^ { \prime } } { b } \frac { \partial K } { \partial c _ { i } } \right) _ { \nu } + K _ { \mu } ( i _ { 1 } L _ { 1 } + \cdot \cdot \cdot + i _ { 3 n } L _ { 3 n } ) \right\}
$$

$$
\quad + { \frac { 1 } { 2 } } \sum _ { \mu } \sum _ { \nu } \left\{ \sum _ { i } \left. { \frac { h _ { i } ^ { \prime } } { b } } { \frac { \partial K } { \partial c _ { i } } } \right. _ { \nu } - K _ { \mu } ( i _ { 1 } L _ { 1 } + \cdots + i _ { 3 \pi } L _ { 3 \pi } ) \right\}
$$

$$
\delta \zeta = \frac { 1 } { 2 } \sum _ { \mu } \sum _ { \nu } \ \left\{ \sum _ { i } \ \left. \frac { h _ { i } ^ { \prime } } { b } \frac { \partial K ^ { \prime } } { \partial c _ { i } } \right. _ { \nu } + K _ { \mu } ^ { \prime } ( j _ { 1 } L _ { 1 } + \cdot \cdot \cdot + j _ { 3 \pi } L _ { 3 \pi } ) \right\}
$$

·sin (N" + N)

$$
  + \frac { 1 } { 2 } \sum _ { \mu } \sum _ { \nu } \{ \sum _ { i }  \sum _ { i } ( \frac { h _ { i } ^ { \prime } } { b } \frac { \partial K ^ { \prime } } { \partial c _ { i } } ) _ { \nu } - K _ { \mu } ^ { \prime } ( j _ { 1 } L _ { 1 } + \cdot \cdot \cdot + j _ { 3 n } L _ { 3 n } ) \}  
$$

These are of the same form as the original expressions for $\xi _ { i } , \eta _ { i } , \zeta _ { i }$ ·

One of the coefficients $^ { b }$ becomes O for some values of $N$ . In that case we replace

$$
\int K d t \cdot \cos N = { \frac { K } { b } } \sin N
$$

by

$$
\int K d t \cdot \cos N = K t .
$$

Such a term should be included in $\delta \gamma$ .Denote by $h _ { 0 } ^ { \prime \prime }$ the coefficient of a vanishing term in $d \gamma _ { i } / d t$ ； then the term in question is $\delta \gamma = - h _ { 0 } ^ { \prime \prime } t$ · This amounts to diminishing $n _ { i }$ by $h _ { 0 } ^ { \prime \prime }$ . Similar changes should be made in $\delta \xi , \delta \eta , \delta \zeta$ Thus $\xi + \delta \xi , \eta + \delta \eta , \zeta + \delta \zeta$ for the second approximation are now in the same form as the original expressions for $\xi , \eta ;$ ， $\zeta$ .Hence the expressions for $\xi , \eta , \zeta$ are of the same form even in any higher-order approximation.

Newcomb (1871) applied similar consideration to the form of the solution for the perturbation of the moon's motion due to the action of planets (Section 11.9).

By taking the secular variation in the eccentricities and inclinations of higher degrees into account, Hagihara (1928,1930) supplemented Newcomb's theory (Section 12.30).

# 14.5LINDSTEDT'S THEORY

Lindstedt (1883,1884,1887) extended his method (Section 12.5) of solving a linear differential equation with periodic coefficients to the representation of the three mutual distances in the three-body problem by means of purely trigonometric series with linear functions of $t$ as arguments.

Let the coordinates of the three bodies $m , m ^ { \prime }$ ，and $M$ be $x , y , z ;$ $x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ ; and 0,0,0; and let $r ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ ， $r ^ { \prime 2 } = x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 }$ ，

$$
\Delta ^ { 2 } = ( x - x ^ { \prime } ) ^ { 2 } + ( y - y ^ { \prime } ) ^ { 2 } + ( z - z ^ { \prime } ) ^ { 2 } .
$$

The equations of motion of $_ m$ and $m ^ { \prime }$ around $M$ are (we write the expressions for the $x \cdot$ -coordinates only)

$$
\begin{array} { l } { \displaystyle \frac { d ^ { 2 } x } { d t ^ { 2 } } + x \Big ( \frac { M + m } { r ^ { 3 } } + \frac { m ^ { \prime } } { \Delta ^ { 3 } } \Big ) = m ^ { \prime } x ^ { \prime } \Big ( \frac { 1 } { \Delta ^ { 3 } } - \frac { 1 } { r ^ { \prime 3 } } \Big ) , } \\ { \displaystyle \frac { d ^ { 2 } x ^ { \prime } } { d t ^ { 2 } } + x ^ { \prime } \Big ( \frac { M + m ^ { \prime } } { r ^ { \prime 3 } } + \frac { m } { \Delta ^ { 3 } } \Big ) = m x \Big ( \frac { 1 } { \Delta ^ { 3 } } - \frac { 1 } { r ^ { 3 } } \Big ) . } \end{array}
$$

In order to deduce the equations for $r , r ^ { \prime } , \Delta$ we define

$$
{ \frac { 1 } { 2 } } q = x { \frac { d x ^ { \prime } } { d t } } + y { \frac { d y ^ { \prime } } { d t } } + z { \frac { d z ^ { \prime } } { d t } } - x ^ { \prime } { \frac { d x } { d t } } - y ^ { \prime } { \frac { d y } { d t } } - z ^ { \prime } { \frac { d z } { d t } }
$$

according to Lagrange (Section 5.1). Then $q$ satisfies

$$
\begin{array} { l } { { \displaystyle \frac { d q } { d t } + M \Big \langle \frac { 1 } { r ^ { \prime 3 } } - \frac { 1 } { r ^ { 3 } } \Big \rangle ( r ^ { } + r ^ { \prime 2 } - \Delta ^ { 2 } ) } } \\ { { \displaystyle ~ + ~ m \Big \langle \frac { 1 } { r ^ { 3 } } - \frac { 1 } { \Delta ^ { 3 } } \Big \rangle ( r ^ { 2 } + \Delta ^ { 2 } - r ^ { \prime 2 } ) + m ^ { \prime } \Big \langle \frac { 1 } { \Delta ^ { 3 } } - \frac { 1 } { r ^ { \prime 3 } } \Big \rangle ( r ^ { \prime 2 } + \Delta ^ { 2 } - r ^ { 2 } ) } } \end{array}
$$

Further, put

$$
\begin{array} { l l l } { \displaystyle \frac { 1 } { \Delta ^ { 3 } } - \frac { 1 } { r ^ { \prime 3 } } = \phi , } & { \displaystyle \frac { 1 } { r ^ { 3 } } - \frac { 1 } { \Delta ^ { 3 } } = \psi , } & { \displaystyle \frac { 1 } { r ^ { \prime 3 } } - \frac { 1 } { r ^ { 3 } } = \theta , } \\ { \displaystyle \frac { 1 } { \Delta ^ { 3 } } + \frac { 1 } { r ^ { \prime 3 } } = \phi ^ { \prime } , } & { \displaystyle \frac { 1 } { r ^ { 3 } } + \frac { 1 } { \Delta ^ { 3 } } = \psi ^ { \prime } , } & { \displaystyle \frac { 1 } { r ^ { \prime 3 } } + \frac { 1 } { r ^ { 3 } } = \theta ^ { \prime } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \frac { r ^ { 2 } + \Delta ^ { 2 } - r ^ { \prime 2 } } { 2 r ^ { 5 } } = \Phi , \frac { r ^ { \prime 2 } + r ^ { 2 } - \Delta ^ { 2 } } { 2 r ^ { \prime 5 } } = \Psi , \frac { \Delta ^ { 2 } + r ^ { \prime 2 } - r ^ { 2 } } { 2 \Delta ^ { 5 } } = } \\ & { \frac { r ^ { 2 } + r ^ { \prime 2 } - \Delta ^ { 2 } } { 2 r ^ { 5 } } = \Phi ^ { \prime } , \frac { r ^ { \prime 2 } + \Delta ^ { 2 } - r ^ { 2 } } { 2 r ^ { \prime 5 } } = \Psi ^ { \prime } , \frac { \Delta ^ { 2 } + r ^ { 2 } - r ^ { \prime 2 } } { 2 \Delta ^ { 5 } } = } \end{array}
$$

then,by referring to the equations of motion, we obtain the equations for $r , r ^ { \prime }$ ，and $\Delta$ ，

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 3 } r ^ { 2 } } { d t ^ { 3 } } + \frac { d r ^ { 2 } } { d t } \left( \frac { M + m } { r ^ { 3 } } + 2 m ^ { \prime } \phi ^ { \prime } \right) + m ^ { \prime } \frac { d r ^ { \prime 2 } } { d t } ( - 2 \phi - 3 \Psi ) \nonumber } } \\ { { \mathrm { } } } \\ { { \displaystyle ~ + m ^ { \prime } \frac { d \Delta ^ { 2 } } { d t } ( 2 \phi - 3 \Theta ^ { \prime } ) + m ^ { \prime } q \phi = 0 , } } \\ { { \displaystyle ~ d ^ { 3 } r ^ { \prime 2 } ~ d r ^ { \prime 2 } ~ / M \perp m ^ { \prime } } } \end{array}
$$

$$
{ \frac { d ^ { 3 } r ^ { \prime 2 } } { d t ^ { 3 } } } + { \frac { d r ^ { \prime 2 } } { d t } } \left( { \frac { M + m ^ { \prime } } { r ^ { \prime 3 } } } + 2 m \psi ^ { \prime } \right) + m { \frac { d r ^ { 2 } } { d t } } \left( 2 \psi - 3 \Phi ^ { \prime } \right)
$$

$$
\begin{array} { c } { { \displaystyle { \frac { d ^ { 3 } \Delta ^ { 2 } } { d t ^ { 3 } } + \frac { d \Delta ^ { 2 } } { d t } \left( \frac { m + m ^ { \prime } } { \Delta ^ { 3 } } + 2 M \theta ^ { \prime } \right) + M \frac { d r ^ { 2 } } { d t } ( - 2 \theta - 3 \Phi ) } } } \\ { { \mathrm { } } } \\ { { \displaystyle { + \ M \frac { d r ^ { \prime 2 } } { d t } ( 2 \theta - 3 \Psi ^ { \prime } ) + M q \theta = 0 . } } } \end{array}
$$

From (9) we have

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } q } { d t ^ { 2 } } + \frac { d r ^ { 2 } } { d t } ( - m ^ { \prime } \phi + m \psi + M \theta - 3 M \Phi ^ { \prime } + 3 m \Phi ) } } } \\ { { \displaystyle ~ + \frac { d r ^ { \prime 2 } } { d t } ( m ^ { \prime } \phi - m \psi + M \theta - 3 m ^ { \prime } \Psi ^ { \prime } + 3 M \Psi ) } } \\ { { \displaystyle ~ + \frac { d \Delta ^ { 2 } } { d t } ( m ^ { \prime } \phi + m \psi - M \theta - 3 m \Theta ^ { \prime } + 3 m ^ { \prime } \Theta ) = 0 . } } \end{array}
$$

The equations (9) and (1O) are those used to determine $r , r ^ { \prime }$ ，and $\Delta$ This system of equations is of order 11 and has 11 arbitrary constants. But there are two relations among these 11 constants,and the number of independent constants is thus reduced to 9.

Lagrange disregarded the symmetry of the equations, having in mind practical applications to perturbation theory.Lindstedt,on the contrary, conserved the symmetrical character of the equations and, with the constants $a , a ^ { \prime } , d$ wrote

$$
r ^ { 2 } = a ^ { 2 } ( 1 + \rho ) , r ^ { 2 } = a ^ { \prime 2 } ( 1 + \rho ^ { \prime } ) , \Delta = d ^ { 2 } ( 1 + \partial ) ,
$$

by supposing (with the application to perturbation theory in view) that the eccentricities of the orbits are all small, so that $\rho , \rho ^ { \prime } , \delta < 1$ ，and that the ratio $r / r ^ { \prime }$ is either greater or less than 1 for finite values of $t$ After the substitution of these in the differential equations, the expressions in parentheses in (9) and (1O) are expanded in series proceeding in positive integral powers of $\rho , \rho ^ { \prime } , \delta$ . We separate the constant parts from these series expansions.Let, for example, the constant part of the first parenthesis in the first equation of (9) be $\alpha _ { 1 } - U _ { 1 }$ ，where

$$
\alpha _ { 1 } = \frac { M + m } { a ^ { 3 } } + 2 m ^ { \prime } \left( \frac { 1 } { a ^ { \prime 3 } } + \frac { 1 } { d ^ { 3 } } \right) ,
$$

$$
J _ { 1 } = \alpha _ { 1 } - \Bigl [ { \frac { M + m } { a ^ { 3 } } } ( 1 + \rho ) ^ { - 3 / 2 } + { \frac { 2 m ^ { \prime } } { a ^ { \prime 3 } } } ( 1 + \rho ^ { \prime } ) ^ { - 3 / 2 } + { \frac { 2 m ^ { \prime } } { d ^ { 3 } } } ( 1 + \tilde { \sigma } ) ^ { - 3 }
$$

Similarly we define $\alpha _ { 2 } - U _ { 2 }$ ， $\alpha _ { 3 } - U _ { 3 }$ ， $\beta _ { 1 } - U _ { 1 ; } ^ { \prime }$ $\beta _ { 2 } - U _ { 2 } ^ { \prime } ,$ ， $\beta _ { 3 } - U _ { 3 } ^ { \prime } ,$ Y- ${ \bf \gamma } _ { 1 } , ~ { \gamma } _ { 2 } - { \cal V } _ { 2 } , ~ { \gamma } _ { 3 } - { \cal V } _ { 3 } , ~ { \varepsilon } _ { 1 } - { \cal Q } _ { 1 } , ~ { \varepsilon } _ { 2 } - { \cal Q } _ { 2 } , ~ { \varepsilon } _ { 3 } - { \cal Q } _ { 3 } ; ~ \mathrm { a n d } ~ \alpha$ $\begin{array} { r } { \alpha _ { 0 } - U _ { \mathfrak { o } } , } \end{array}$ $\beta _ { 0 } - U _ { 0 } ^ { \prime } , \ \gamma _ { 0 } - V _ { 0 }$ respectively for the three equations (9) and for the equation (10).

Put

$$
\frac { d r ^ { 2 } } { d t } = u , \qquad \frac { d r ^ { \prime 2 } } { d t } = u ^ { \prime } , \qquad \frac { d \Delta ^ { 2 } } { d t } = v ;
$$

then,

$$
\mathrm {  ~ \xi ~ } ^ { 2 } = a ^ { 2 } + \int u d t , \quad \quad r ^ { \prime 2 } = a ^ { \prime 2 } + \int u ^ { \prime } d t , \quad \quad \Delta ^ { 2 } = d ^ { 2 } + \int v d t ,
$$

or

$$
\rho = { \frac { 1 } { a ^ { 2 } } } \int u d t , \qquad \rho ^ { \prime } = { \frac { 1 } { a ^ { \prime 2 } } } \int u ^ { \prime } d t , \qquad \hat { \boldsymbol { o } } = { \frac { 1 } { d ^ { 2 } } } \int v d t .
$$

With indeterminate constants $\lambda _ { 0 } , \mu _ { 0 } , \nu _ { 0 } , \tau _ { 0 } ; ~ \lambda _ { 1 } , \mu _ { 1 } , \nu _ { 1 } , \tau _ { 1 } ; ~ \lambda _ { 2 } , \mu _ { 2 } , \nu _ { 2 } , \tau _ { 2 } ; ~ \lambda _ { 3 } ,$ $\mu _ { 3 } , \nu _ { 3 } , \tau _ { 3 }$ we obtain from (9) and (10) the equations

$$
\begin{array} { r l } & { \frac { i } { 2 } + ( \alpha _ { 0 } - \lambda _ { 0 } ) u + ( \beta _ { 0 } - \mu _ { 0 } ) u ^ { \prime } + ( \gamma _ { 0 } - \nu _ { 0 } ) v - \tau _ { 0 } q } \\ & { \quad = ( U _ { 0 } - \lambda _ { 0 } ) u + ( U _ { 0 } ^ { \prime } - \mu _ { 0 } ) u ^ { \prime } + ( V _ { 0 } - \nu _ { 0 } ) v - \tau _ { 0 } q , } \\ & { \frac { i } { 2 } + ( \alpha _ { 1 } - \lambda _ { 1 } ) u + ( \beta _ { 1 } - \mu _ { 1 } ) u ^ { \prime } + ( \gamma _ { 1 } - \nu _ { 1 } ) v + ( \varepsilon _ { 1 } - \tau _ { 1 } ) q } \\ & { \quad = ( U _ { 1 } - \lambda _ { 1 } ) u + ( U _ { 1 } ^ { \prime } - \mu _ { 1 } ) u ^ { \prime } + ( V _ { 1 } - \nu _ { 1 } ) v + ( Q _ { 1 } - \tau _ { 1 } ) q , } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } u ^ { \prime } } { d t ^ { 2 } } + ( \alpha _ { 2 } - \lambda _ { 2 } ) u + ( \beta _ { 2 } - \mu _ { 2 } ) u ^ { \prime } + ( \gamma _ { 2 } - \nu _ { 2 } ) v + ( \varepsilon _ { 2 } - \tau _ { 2 } ) q } } } \\ { { \mathrm { ~ \ ~ \ ~ - ~ } ( T \bar { \bf { \Psi } } ) _ { \mathrm { ~ \tiny ~ 2 ~ \rangle ~ \alpha ~ , ~ \bar { ~ } ~ ( ~ T \bar { \bf { \Psi } } ~ ) ~ } , \mathrm { ~ \ ~ \ ~ - ~ } } \mathrm { ~ \ \ } _ { \mathrm { ~ \tiny ~ 2 ~ } } \mathrm { ~ \ ~ \ } _ { \mathrm { ~ \tiny ~ 1 ~ } } \mathrm { ~ \ ~ \ } _ { \mathrm { ~ \Omega ~ } } } } \end{array}
$$$$
= ( U _ { 2 } - \lambda _ { 2 } ) u + ( U _ { 2 } ^ { \prime } - \mu _ { 2 } ) u ^ { \prime } + ( V _ { 2 } - \nu _ { 2 } ) v + ( Q _ { 2 } - \tau _ { 2 } ) q ,
$$

$$
\frac { d ^ { 2 } v } { d t ^ { 2 } } + ( \alpha _ { 3 } - \lambda _ { 3 } ) u + ( \beta _ { 3 } - \mu _ { 3 } ) u ^ { \prime } + ( \gamma _ { 3 } - \nu _ { 3 } ) v + ( \varepsilon _ { 3 } - \tau _ { 3 } ) q
$$

$$
= ( U _ { 3 } - \lambda _ { 3 } ) u + ( U _ { 3 } ^ { \prime } - \mu _ { 3 } ) u ^ { \prime } + ( V _ { 3 } - \nu _ { 3 } ) v + ( Q _ { 3 } - \tau _ { 3 } ) q .
$$

We determine the functions $u , u ^ { \prime } , v , q ; \rho , \rho ^ { \prime } , \delta ; r ^ { 2 } , r ^ { \prime 2 } , \Delta ^ { 2 }$ in the form of trigonometric series with four distinct arguments

$$
\begin{array} { r l r } { w _ { 1 } = n t + \pi , } & { { } } & { w _ { 2 } = n ^ { \prime } t + \pi ^ { \prime } , } \\ { w _ { 3 } = \upsilon t + \omega , } & { { } } & { w _ { 4 } = \upsilon ^ { \prime } t + \omega ^ { \prime } , } \end{array}
$$

where $\pi , \pi ^ { \prime } , \omega , \omega ^ { \prime }$ are the integration constants.A term with the arguments $i w _ { 1 } \pm i ^ { \prime } w _ { 2 } \pm j w _ { 3 } \pm j ^ { \prime } w _ { 4 }$ contains the factor $\eta ^ { i } \eta ^ { \prime i ^ { \prime } } \kappa ^ { j } \kappa ^ { \prime j ^ { \prime } }$ ，where $i , i ^ { \prime } , j , j ^ { \prime }$ are positive integers. Such a term is of order $i + i ^ { \prime } + j + j ^ { \prime }$

We proceed to solve the equations (11） by successive approximations.The constants $n , n ^ { \prime } , \nu , \nu ^ { \prime }$ are the sums of constant terms of odd orders. The 11 integration constants are $a ^ { 2 } , a ^ { \prime 2 } , d ^ { 2 } ; \eta , \eta ^ { \prime } , \kappa , \kappa ^ { \prime } ; \pi ,$ $\pi ^ { \prime } , \omega , \omega ^ { \prime }$ . There should be two relations among these 11 constants.

The constants $n , n ^ { \prime } , \nu , \nu ^ { \prime }$ are determined by

$$
\left| \begin{array} { l l l l } { w - { \tau _ { 0 } } } & { \alpha _ { 0 } - \lambda _ { 0 } } & { \beta _ { 0 } - \mu _ { 0 } } & { \gamma _ { 0 } - \nu _ { 0 } } \\ { \varepsilon _ { 1 } - { \tau _ { 1 } } } & { w + \alpha _ { 1 } - \lambda _ { 1 } } & { \beta _ { 1 } - \mu _ { 1 } } & { \gamma _ { 1 } - \nu _ { 1 } } \\ { \varepsilon _ { 2 } - { \tau _ { 2 } } } & { \alpha _ { 2 } - \lambda _ { 2 } } & { w + \beta _ { 2 } - \mu _ { 2 } } & { { \tau _ { 2 } } - \nu _ { 2 } } \\ { \varepsilon _ { 3 } - { \tau _ { 3 } } } & { \alpha _ { 3 } - \lambda _ { 3 } } & { \beta _ { 3 } - \mu _ { 3 } } & { w + { \tau _ { 3 } } - \nu _ { 3 } } \end{array} \right| = 0 .
$$

The roots are real negative and denoted by $- n ^ { 2 } , - n ^ { \prime 2 } , - \nu ^ { 2 } , - \nu ^ { \prime 2 }$ The solution of the homogeneous equations of (11), (with their righthand members equated to zero) is the sum of four trigonometric terms with arguments $\mathcal { W } _ { 1 } , \mathcal { W } _ { 2 } , \mathcal { W } _ { 3 } , \mathcal { W } _ { 4 }$ .We consider this solution as the first approximation.

The left-hand members of (11） are linear equations with constant coefficients.The right-hand members are expanded in positive integral powers of $\rho , \rho ^ { \prime } , \delta$ .If we substitute the first approximate solution on the right-hand sides,then they are arranged in trigonometric series with arguments of the form $i w _ { 1 } \pm i ^ { \prime } w _ { 2 } \pm j w _ { 3 } \pm j ^ { \prime } w _ { 4 }$ . We so determine the indeterminate constants $\lambda _ { i } , \mu _ { i } , \nu _ { i } , \tau _ { i }$ as to avoid the appearance of any secular term in the integrals.In the first approximation they are all zero,and we obtain

$$
\begin{array} { r } { q = \eta _ { 0 } \sin w _ { 1 } + \eta _ { 0 } ^ { \prime } \sin w _ { 2 } + \kappa _ { 0 } \sin w _ { 3 } + \kappa _ { 0 } ^ { \prime } \sin w _ { 4 } , } \\ { u = \eta _ { 1 } \sin w _ { 1 } + \eta _ { 1 } ^ { \prime } \sin w _ { 2 } + \kappa _ { 1 } \sin w _ { 3 } + \kappa _ { 1 } ^ { \prime } \sin w _ { 4 } , } \\ { u ^ { \prime } = \eta _ { 2 } \sin w _ { 1 } + \eta _ { 2 } ^ { \prime } \sin w _ { 2 } + \kappa _ { 2 } \sin w _ { 3 } + \kappa _ { 2 } ^ { \prime } \sin w _ { 4 } , } \\ { v = \eta _ { 3 } \sin w _ { 1 } + \eta _ { 3 } ^ { \prime } \sin w _ { 2 } + \kappa _ { 3 } \sin w _ { 3 } + \kappa _ { 3 } ^ { \prime } \sin w _ { 4 } , } \end{array}
$$

where $\eta _ { i } , \eta _ { i } ^ { \prime } , \kappa _ { i } , \kappa _ { i } ^ { \prime } \left( i = 0 , 1 , 2 , 3 \right)$ contain the four integration constants $\eta , \eta ^ { \prime } , \kappa , \kappa ^ { \prime }$ ，respectively，as factors.The coefficients are the values of the minor determinants of (12) for $w = - n ^ { 2 }$ ， $w = - n ^ { \prime 2 }$ ， $w = - \nu ^ { 2 }$ and $w = - \nu ^ { \prime 2 }$ successively.

In the second approximation we obtain the expressions for $U , U ^ { \prime }$ ， $V , Q$ in the form $_ \alpha$ cos $w _ { 1 } + \beta \cos w _ { 2 } + \gamma \cos w _ { 3 } + \delta \cos w _ { 4 }$ ，and the right-hand members of (11） are composed of sine terms with arguments $2 w _ { \mathfrak { r } }$ ， $2 w _ { \mathfrak { z } }$ ， $2 w _ { 3 }$ ， $2 w _ { 4 }$ ， $w _ { 1 } + w _ { 2 }$ ， $w _ { 2 } + w _ { 3 }$ ， $w _ { 3 } + w _ { 1 }$ ， $w _ { 1 } - w _ { 2 }$ ， $w _ { 2 } - w _ { 3 }$ ， $w _ { 3 } - w _ { 1 }$ ,and with coefficients which are of the second order. Denote by $[ \eta ^ { 2 } ] , \ldots , [ \eta \eta ^ { \prime } ] , .$ .. the quantities of order $\eta ^ { 2 } , \ldots , \eta \eta ^ { \prime } , \ldots ,$ respectively. Then the second approximate solution is

$$
\eta = \eta _ { 0 } \sin w _ { 1 } + \eta _ { 0 } ^ { \prime } \sin w _ { 2 } + \kappa _ { 0 } \sin w _ { 3 } + \kappa _ { 0 } ^ { \prime } \sin w _ { 4 }
$$

The solution for $u , u ^ { \prime }$ ， $v$ contain only cosine terms.

In the third approximation we obtain on the right-hand sides of (11) terms of the form

$$
\begin{array} { r l } & { U _ { i } u + U _ { i } ^ { \prime } u ^ { \prime } + V _ { i } v + Q _ { i } q } \\ & { \qquad = l _ { i } \eta \sin w _ { 1 } + m _ { i } \eta ^ { \prime } \sin w _ { 2 } + n _ { i } \kappa \sin w _ { 3 } + t _ { i } \kappa ^ { \prime } \sin w _ { 4 } } \\ & { \qquad + \displaystyle \sum _ { \alpha , \beta } \left[ 2 \right] _ { \alpha \beta } \sin \big ( w _ { \alpha } \pm w _ { \beta } \big ) } \\ & { \qquad + \displaystyle \sum _ { \alpha , \beta , \gamma } \left[ 3 \right] _ { \alpha \beta \gamma } \sin \big ( w _ { \alpha } \pm w _ { \beta } \pm w _ { \tau } \big ) , } \end{array}
$$

where $[ 2 ] _ { \alpha \beta } , [ 3 ] _ { \alpha \beta \gamma }$ are respectively of the second and the third orders and $l _ { i } , m _ { i } , n _ { i } , t _ { i }$ are of the second order. Futhermore,we have

$$
\begin{array} { r l } & { \lambda _ { i } u + \mu _ { i } u ^ { \prime } + \nu _ { i } v + \tau _ { i } q } \\ & { \qquad = ( \lambda _ { i } \eta _ { 1 } + \mu _ { i } \eta _ { 2 } + \nu _ { i } \eta _ { 3 } + \tau _ { i } \eta _ { 0 } ) \sin { w _ { 1 } } } \\ & { \qquad + \left( \lambda _ { i } \eta _ { 1 } ^ { \prime } + \mu _ { i } \eta _ { 2 } ^ { \prime } + \nu _ { i } \eta _ { 3 } ^ { \prime } + \tau _ { i } \eta _ { 0 } ^ { \prime } \right) \sin { w _ { 2 } } } \\ & { \qquad + \left( \lambda _ { 1 } \kappa _ { 1 } + \mu _ { i } \kappa _ { 2 } + \nu _ { i } \kappa _ { 3 } + \tau _ { i } \kappa _ { 0 } \right) \sin { w _ { 3 } } } \\ & { \qquad + \left( \lambda _ { i } \kappa _ { 1 } ^ { \prime } + \mu _ { i } \kappa _ { 2 } ^ { \prime } + \nu _ { i } \kappa _ { 3 } ^ { \prime } + \tau _ { i } \kappa _ { 0 } ^ { \prime } \right) \sin { w _ { 4 } } } \\ & { \qquad + \ \displaystyle \sum _ { \alpha , \beta } \left[ 4 \right] _ { \alpha \beta } ^ { \prime } \sin { \left( w _ { \alpha } \pm \ w _ { \beta } \right) } , } \end{array}
$$

where $[ 4 ] _ { \alpha \beta }$ are of the second order. The constants $\lambda _ { i } , \mu _ { i } , \nu _ { i } , \tau _ { i }$ are determined so that there is no term containing sin $w _ { 1 }$ ，sin $w _ { 2 }$ ，sin $w _ { 3 }$ ， sin ${ \boldsymbol { w } } _ { 4 }$ in the expression

$$
( U _ { i } - \lambda _ { i } ) u + ( U _ { i } ^ { \prime } - \mu _ { i } ) u ^ { \prime } + ( V _ { i } - \nu _ { i } ) v + ( Q _ { i } - \tau _ { i } ) q ,
$$

that is, so that

$$
\begin{array} { l l } { { } } & { { \lambda _ { i } \eta _ { 1 } + \mu _ { i } \eta _ { 2 } + \nu _ { i } \eta _ { 3 } + \tau _ { i } \eta _ { 0 } = l _ { i } \eta , } } \\ { { } } & { { \lambda _ { i } \eta _ { 1 } ^ { \prime } + \mu _ { i } \eta _ { 2 } ^ { \prime } + \nu _ { i } \eta _ { 3 } ^ { \prime } + \tau _ { i } \eta _ { 0 } ^ { \prime } = m _ { i } \eta ^ { \prime } , } } \\ { { } } & { { \lambda _ { i } \kappa _ { 1 } + \mu _ { i } \kappa _ { 2 } + \nu _ { i } \kappa _ { 3 } + \tau _ { i } \kappa _ { 0 } = n _ { i } \kappa , } } \\ { { } } & { { \lambda _ { i } \kappa _ { 1 } ^ { \prime } + \mu _ { i } \kappa _ { 2 } ^ { \prime } + \nu _ { i } \kappa _ { 3 } ^ { \prime } + \tau _ { i } \kappa _ { 0 } ^ { \prime } = t _ { i } \kappa ^ { \prime } \qquad ( i = 0 , 1 , 2 , 3 ) . } } \end{array}
$$

This method fails if there are linear homogeneous relations with integer coefficients among $n , n ^ { \prime } , \nu , \nu ^ { \prime }$

The seven integration constants $a ^ { 2 } , a ^ { \prime 2 } , d ^ { 2 } ; \eta , \eta ^ { \prime } , \kappa , \kappa ^ { \prime }$ are connected by two relations.One of the relations is obtained from (8a). The other relation is Lagrange's and expresses $q$ defined by (8) in terms of $r , r ^ { \prime }$ ， $\Delta$ and their derivatives of the first and the second orders.

Tisserand (1884,1885,1888) adopted Jacobi's relative canonical coordinates (Section 5.6) for the three bodies and referred the motion to the invariable plane of the three bodies.He then took the Keplerian motion of the two bodies as the first approximation and considered the variation of elements according to Delaunay's theory (Section 9.1). We can reduce the order of the differential equations to eight by means of the elimination of the nodes according to Jacobi. The three mutual distances are expressed in trigonometric series with four arguments linear in $\pmb { t } .$ .Let one of the Delaunay variables $^ { h }$ be expressed in the form $h = h _ { 0 } + h _ { 1 } t + h _ { 2 } ( t )$ ，where $h _ { 2 } ( t )$ is a periodic function with the four arguments linear in $t$ .Rotate the coordinate axes by an angle $h _ { 0 } + h _ { 1 } t$ around the $z \cdot$ -axis，which is perpendicular to the invariable plane.Tisserand showed that, with reference to this rotating axes,the coordinates of the two bodies can be expressed in trigonometric functions with four arguments linear in $t$ .These four arguments are those which are obtained at the final stage of the Delaunay transformation for the angular variables ${ \mathit { l } } , { \mathit { l } } ^ { \prime } , { \mathit { g } }$ and $g ^ { \prime }$ ·

Andoyer (1887,1890) started with the equations of Laplace (Section 10.14) for planetary theory. Let $m _ { 0 }$ denote the Sun's mass and $m _ { 1 } , m _ { 2 }$ ， $\ldots , m _ { i }$ the masses of the planets.The equations of motion of the ith planets are

$$
\begin{array} { c }  { { \displaystyle { \frac { 1 } { 2 } \frac { d ^ { 2 } ( r _ { i } ^ { 0 } ) } { d t ^ { 2 } } - \frac { k ^ { 2 } ( m _ { 0 } + m _ { i } ) } { r _ { i } } - 2 \int ( d R _ { i } ) - r _ { i } \frac { \partial R _ { i } } { \partial r _ { i } } = 0 , } } } \\  { { \displaystyle { 1 - s _ { i } ^ { 2 } \frac { d ^ { 2 } v _ { i } } { d t ^ { 2 } } - \frac { 1 } { r _ { i } } \frac { d ^ { 2 } r _ { i } } { d t ^ { 2 } } - \frac { k ^ { 2 } ( m _ { 0 } + m _ { i } ) } { r _ { i } ^ { 3 } } + \frac { 1 } { 1 - s _ { i } ^ { 2 } } \Big ( \frac { d s _ { i } } { d t } \Big ) ^ { 2 } + \frac { 1 } { r _ { i } } \frac { \partial R _ { i } } { \partial { \bar { w } } _ { i } } = } } } \\  { { \displaystyle { \frac { 1 } { 1 - s _ { i } ^ { 2 } } \frac { d ^ { 2 } s _ { i } } { d t ^ { 2 } } + s _ { i } \Big ( \frac { d v _ { i } } { d t } \Big ) ^ { 2 } + \frac { 2 } { r _ { i } ( 1 - s _ { i } ^ { 2 } ) } \frac { d r _ { i } } { d t } \frac { d s _ { i } } { d t } } } } \\ { { { + \frac { s _ { i } } { ( 1 - s _ { i } ^ { 2 } ) ^ { 2 } } \Big ( \frac { d s _ { i } } { d t } \Big ) ^ { 2 } - \frac { 1 } { r _ { i } ^ { 2 } } \frac { \partial R _ { i } } { \partial s _ { i } } = } } } \end{array}
$$

where

$$
( d R _ { i } ) = \frac { \partial R _ { i } } { \partial r _ { i } } d r _ { i } + \frac { \partial R _ { i } } { \partial v _ { i } } d v _ { i } + \frac { \partial R } { \partial s _ { i } } d s _ { i } ,
$$

$$
\begin{array} { l } { { R _ { i } = \displaystyle \sum _ { j } R _ { i j } , \qquad z _ { i } = r _ { v } s _ { i } , } } \\ { { R _ { i j } = k ^ { 2 } m _ { j } \left\{ \displaystyle \frac { 1 } { [ ( x _ { i } - x _ { j } ) ^ { 2 } + ( y _ { i } - y _ { j } ) ^ { 2 } + ( z _ { i } - z _ { j } ) ^ { 2 } ] ^ { 1 / 2 } } \right. } } \\ { { \displaystyle \left. - \frac { x _ { i } x _ { j } + y _ { i } y _ { j } + z _ { i } z _ { j } } { r _ { j } ^ { 3 } } \right\} . } } \end{array}
$$

Put

$$
\begin{array} { c c } { { n _ { i } ^ { 2 } a _ { i } ^ { 3 } = k ^ { 2 } ( m _ { 0 } + m _ { i } ) , } } & { { \quad r _ { i } = a _ { i } ( 1 + \rho _ { i } ) , } } \\ { { v _ { i } = N _ { i } + \lambda _ { i } , } } & { { \quad N _ { i } = n _ { i } t + \varepsilon _ { i } , } } \end{array}
$$

then we have

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 2 } } { d t ^ { 2 } } \left( \rho _ { t } + \frac { 1 } { 2 } \rho _ { t } ^ { 2 } \right) - \frac { n _ { t } ^ { 2 } } { 1 + \rho _ { t } } - \frac { 2 } { a _ { t } ^ { 2 } } \int ( d R _ { \delta } ) - \frac { \tau _ { t } } { a _ { t } ^ { 2 } } \frac { \partial R _ { \delta } } { \partial \tau _ { t } } = 0 , } } \\ { { \displaystyle ( 1 - s _ { t } ^ { 3 } ) \Big ( n _ { t } + \frac { d \lambda _ { \bar { \lambda } } } { d t } \Big ) ^ { 2 } - \frac { 1 } { 1 + \rho _ { t } } \frac { d ^ { 2 } \rho _ { t } } { d t ^ { 2 } } - \frac { n _ { t } ^ { 2 } } { ( 1 + \rho _ { t } ) ^ { 3 } } } } \\ { { \displaystyle ~ + \frac { 1 } { 1 - s _ { t } ^ { 2 } } \Big ( \frac { d s _ { t } } { d t } \Big ) ^ { 2 } + \frac { 1 } { r _ { t } } \frac { \partial R _ { \bar { \lambda } } } { \partial s _ { t } } = 0 , } } \\ { { \displaystyle \frac { 1 } { 1 - s _ { t } ^ { 2 } } \frac { d ^ { 2 } s _ { t } } { d t ^ { 2 } } + s _ { t } \Big ( n _ { t } + \frac { d \lambda _ { \bar { \lambda } } } { d t } \Big ) ^ { 2 } + \frac { 2 } { ( 1 + \rho _ { t } ) ( 1 - s _ { t } ^ { 3 } ) } \frac { d \rho _ { t } } { d t } \frac { d s _ { \bar { \lambda } } } { d t } } } \\ { { \displaystyle ~ + \frac { s _ { t } } { ( 1 - s _ { t } ^ { 3 } ) ^ { 2 } } \Big ( \frac { d s _ { \bar { \lambda } } } { d t } \Big ) ^ { 2 } - \frac { 1 } { r _ { t } ^ { 2 } } \frac { \partial R _ { \bar { \lambda } } } { \partial s _ { t } } = 0 . } } \end{array}
$$

These equations are integrated in the form

$$
\begin{array} { l } { \rho _ { i } = \displaystyle \sum _ { i } \rho _ { i } ( p _ { 1 } , \ldots , q _ { 1 } , \ldots , r _ { 1 } , \ldots ) \cos V ^ { ( p ) } , } \\ { \lambda _ { i } = \displaystyle \sum _ { i } \lambda _ { i } ( p _ { 1 } , \ldots , q _ { 1 } , \ldots , r _ { 1 } , \ldots ) \sin V ^ { ( p ) } , } \\ { s _ { i } = \displaystyle \sum _ { i } s _ { i } ( p _ { 1 } , \ldots , q _ { 1 } , \ldots , r _ { 1 } , \ldots ) \sin V ^ { ( p ) } , } \end{array}
$$

where

$$
V ^ { ( p ) } = p _ { 1 } N _ { 1 } + \cdots + q _ { 1 } G _ { 1 } + \cdots + r _ { 1 } H _ { 1 } + \cdots ,
$$

$$
N _ { i } = n _ { i } t + \varepsilon _ { i } , \qquad G _ { i } = g _ { i } t + \varpi _ { i } , \qquad H _ { i } = h _ { i } t + \vartheta _ { i } ,
$$

$$
\sum p _ { i } + \sum q _ { i } + \sum r _ { i } = 0 ,
$$

and $\sum r _ { i }$ is even in the first two equations and is odd in the third. Also, $g _ { i }$ and $h _ { i }$ are of the first order,and $\varepsilon _ { i } , \varpi _ { i } , \vartheta _ { i }$ are the integration constants.As the arbitrary constants we take the coeffcients of

$$
{ \cos { ( N _ { 3 } - G _ { i } ) } }
$$

in $\rho _ { 3 }$ and the coefficients of

$$
\sin { ( N _ { 3 } - H _ { i } ) }
$$

in $s _ { 3 }$ ， and denote them respectively by $\varepsilon _ { 1 } , \varepsilon _ { 2 } , \ldots , \eta _ { 1 } , \eta _ { 2 } , \ldots .$ Then $\rho _ { i } ( p _ { 1 } , \dots , q _ { 1 } , \dots , r _ { 1 } , \dots )$ is written

$$
\begin{array} { r l r } {  { \varepsilon _ { 1 } ^ { ( q _ { 1 } ) } \varepsilon _ { 2 } ^ { ( q _ { 2 } ) } \mathrm { ~ \cdots ~ } \gamma _ { 1 } ^ { ( r _ { 1 } ) } \gamma _ { 2 } ^ { ( r _ { 2 } ) } \mathrm { ~ \cdots ~ } m _ { j } m _ { j } \mathrm { ~ \cdots ~ } } } \\ & { } & { \qquad \cdot \displaystyle \sum _ { i } \varepsilon _ { 1 } ^ { 2 q _ { 1 } ^ { \prime } } \mathrm { ~ \cdots ~ } \gamma _ { 1 } ^ { 2 r _ { 1 } ^ { \prime } } \mathrm { ~ \cdots ~ } \rho _ { i ( 2 q _ { 1 } ^ { \prime } , \cdots , 2 r _ { 1 } ^ { \prime } , \cdots ) } ^ { ( p _ { 1 } , \cdots , q _ { 1 } , \cdots , r _ { 1 } , \cdots ) } . } \end{array}
$$

The index $q _ { 1 } ^ { \prime } , q _ { 2 } ^ { \prime } , \cdots$ arepostiveintegesoreoe corresponding to the disturbing mass $m _ { j }$ yis is not zero. The arranged in powers of the disturbing masses, its principal part being of order zero. We have similar expressions for $\lambda _ { i } ( p _ { 1 } , \ldots , q _ { 1 } , \ldots ,$ $r _ { 1 } , \ldots . )$ and $s _ { i } ( p _ { 1 } , \dots , q _ { 1 } , \dots , r _ { 1 } , \dots )$ . Finally, $g _ { i }$ and $h _ { i }$ are of the form

$$
\sum _ { \mathrm { \scriptsize { \in } } 1 } \varepsilon _ { 1 } ^ { 2 q _ { 1 } ^ { \prime } } \varepsilon _ { 2 } ^ { 2 q _ { 2 } ^ { \prime } } \cdot \cdot \cdot \ \gamma _ { 1 } ^ { 2 \tau _ { 1 } ^ { \prime } } \gamma _ { 2 } ^ { 2 \tau _ { 2 } ^ { \prime } } \ \cdot \cdot \cdot \ g _ { i } ( 2 q _ { 1 } ^ { \prime } , 2 q _ { 2 } ^ { \prime } , \cdot \cdot \cdot , 2 r _ { 1 } ^ { \prime } , \cdot \cdot \cdot ) ,
$$

and their principal parts are of the first order.

The disturbing function $R _ { i }$ is expanded in powers of $\lambda _ { i } , \rho _ { i }$ and $s _ { i }$ ， and in trigonometric series with arguments $N _ { i } - N _ { j }$ and $V ^ { ( { p } ) }$ (see Callandreau,1891).

# 14.6VON ZEIPEL'S THEORY

Consider with von Zeipel (1898,1901) the three-body problem in which one of the masses is large compared with the other two.In the notation of Sections 5.16 to 5.17,put

$$
\beta _ { 1 } = \frac { m _ { 0 } } { m _ { 0 } + m _ { 1 } } , \qquad \beta _ { 2 } = \frac { m _ { 2 } } { m _ { 1 } } \frac { m _ { 0 } + m _ { 1 } } { m _ { 0 } + m _ { 1 } + m _ { 2 } } , \nonumber 
$$

$$
k _ { 1 } ^ { 2 } = k ^ { 2 } ( m _ { 0 } + m _ { 1 } ) , \qquad k _ { 2 } ^ { 2 } = k ^ { 2 } m _ { 0 } \frac { m _ { 0 } + m _ { 1 } + m _ { 2 } } { m _ { 0 } + m _ { 1 } } ,
$$

$$
k _ { \ast } \beta _ { \ast } \sqrt { a } _ { \ast } = \Lambda _ { \ast } \qquad k _ { \ast } \beta _ { \ast } G _ { \ast } = \Theta _ { \ast } \qquad ( \nu = 1 , 2 ) ,
$$

and take the canonical set

$$
\begin{array} { r l } & { \Lambda _ { \nu } , \qquad \quad \xi _ { \nu } = \sqrt { 2 ( \Lambda _ { \nu } - \Theta _ { \nu } ) } \cdot \cos { g _ { \nu } } , } \\ & { \lambda _ { \nu } = l _ { \nu } + g _ { \nu } , \qquad \eta _ { \nu } = - \sqrt { 2 ( \Lambda _ { \nu } - \Theta _ { \nu } ) } \cdot \sin { g _ { \nu } } \qquad ( \nu = 1 , 2 ) , } \end{array}
$$

and the equations

$$
\begin{array} { r l r l } & { \frac { d \Lambda _ { \nu } } { d t } = \frac { \partial F } { \partial \lambda _ { \nu } } , } & & { \frac { d \xi _ { \nu } } { d t } = \frac { \partial F } { \partial \eta _ { \nu } } , } \\ & { \frac { d \lambda _ { \nu } } { d t } = - \frac { \partial F } { \partial \Lambda _ { \nu } } , } & & { \frac { d \eta _ { \nu } } { d t } = - \frac { \partial F } { \partial \xi _ { \nu } } \quad \quad ( \nu = 1 , 2 ) , } \end{array}
$$

where

$$
F = F _ { \boldsymbol \circ } + \mu F _ { \boldsymbol \imath } , \qquad F _ { \boldsymbol \circ } = \frac { k _ { 1 } ^ { 4 } \beta _ { 1 } ^ { 3 } } { 2 \Lambda _ { 1 } ^ { 2 } } + \frac { k _ { 2 } ^ { 4 } \beta _ { 2 } ^ { 3 } } { 2 \Lambda _ { 2 } ^ { 2 } } ,
$$

$$
\mu { \cal F } _ { 1 } = \sum \Phi ( \Lambda _ { 1 } , \Lambda _ { 2 } , J ) \xi _ { 1 } ^ { k _ { 1 } } \xi _ { 2 } ^ { k _ { 2 } } \gamma _ { 1 } ^ { l _ { 1 } } \gamma _ { 2 } ^ { l _ { 2 } } \stackrel { \mathrm { C O S } } { \sin } ( i _ { 1 } \lambda _ { 1 } + i _ { 2 } \lambda _ { 2 } ) ,
$$

$$
\lambda _ { \nu } = n _ { \nu } t + \gamma _ { \nu } , ~ n _ { \nu } = - \frac { \partial F _ { 0 } } { \partial \Lambda _ { \nu } } ~ ( \nu = 1 , 2 ) .
$$

Von Zeipel wrote

$$
\Lambda _ { \nu } = \Lambda ^ { \left( \nu \right) } + \xi _ { \nu + 2 } , \qquad \lambda _ { \nu } = \lambda ^ { \left( \nu \right) } + \eta _ { \nu + 2 } \qquad ( \nu = 1 , 2 ) ,
$$

so that the equations are

$$
\frac { d \xi _ { \nu } } { d t } = \frac { \partial \Phi } { \partial \eta _ { \nu } } , \qquad \frac { d \eta _ { \nu } } { d t } = - \frac { \partial \Phi } { \partial \xi _ { , } } \qquad ( \nu = 1 , 2 , 3 , 4 ) ,
$$

$$
\Phi = F + n _ { 1 } \xi _ { 3 } + n _ { 2 } \xi _ { 4 } = \Phi _ { 0 } + \mu \Phi _ { 1 } + \mu ^ { 2 } \Phi _ { 2 } + \cdot \cdot \cdot ,
$$

$$
\Phi _ { 0 } = F _ { 0 } , \qquad \lambda ^ { \scriptscriptstyle ( \upsilon ) } = n , t + \gamma ^ { \scriptscriptstyle ( \upsilon ) } , \qquad n , = - \frac { \partial \Phi _ { 0 } } { \partial \Lambda ^ { \scriptscriptstyle ( \upsilon ) } } ,
$$

$$
\Phi _ { k } = \sum \overline { { { \Phi } } } _ { k } \xi _ { 1 } ^ { r _ { 1 } } \cdot \cdot \cdot \xi _ { 4 } ^ { r _ { 4 } } \gamma _ { 1 } ^ { s _ { 1 } } \cdot \cdot \cdot \gamma _ { 4 } ^ { s _ { 4 } } \sin { ( i _ { 1 } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } \lambda ^ { \scriptscriptstyle ( 2 ) } ) } ,
$$

where cosines are taken if $s _ { 1 } + s _ { 2 } + s _ { 3 } + s _ { 4 }$ is even,and sines otherwise. It is shown that this system (15) can be satisfied formally by

$$
\begin{array} { l } { { \hat { \xi } _ { \nu } = \tilde { \xi } _ { \nu } = \mu \hat { \xi } _ { \nu } ^ { ( 1 ) } + \mu ^ { 2 } \hat { \xi } _ { \nu } ^ { ( 2 ) } + \cdot \cdot \cdot , } } \\ { { \eta _ { \nu } = \tilde { \eta } _ { \nu } = \mu \eta _ { \nu } ^ { ( 1 ) } + \mu ^ { 2 } \eta _ { \nu } ^ { ( 2 ) } + \cdot \cdot \cdot } } \end{array} \quad ( \nu = 1 , 2 , 3 , 4 ) ,
$$

where

$$
\begin{array} { l } { { \displaystyle \hat { \xi } _ { \nu } ^ { ( k ) } = \sum _ { i _ { 1 } , i _ { 2 } } C _ { i _ { 1 } i _ { 2 } } \cos { ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } ) } , } } \\ { { \displaystyle \eta _ { \nu } ^ { ( k ) } = \sum _ { i _ { 1 } , i _ { 2 } } S _ { i _ { 1 } i _ { 2 } } \sin { ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } ) } . } } \end{array}
$$

Substitute these expressions in the differential equations (15) and equate the same power of $\pmb { \mu }$ on both sides；then

$$
\begin{array} { r l } & { \frac { d \hat { \xi } _ { i } ^ { ( 1 ) } } { d t } = \frac { \partial \Phi _ { 1 } } { \partial \gamma _ { i } ^ { ( 0 ) } } \quad \quad ( i = 1 , 2 , 3 , 4 ) , } \\ & { \frac { d \eta _ { j } ^ { ( 1 ) } } { d t } = - \frac { \partial \Phi _ { 1 } } { \partial \hat { \xi } _ { j } ^ { ( 0 ) } } , } \\ & { \frac { d \eta _ { j + 2 } ^ { ( 1 ) } } { d t } = - \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( j ) } \partial \Lambda ^ { ( 1 ) } } \xi _ { 3 } ^ { ( 1 ) } - \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( j ) } \partial \Lambda ^ { ( 2 ) } } \xi _ { 4 } ^ { ( 1 ) } - \frac { \partial \Phi _ { 1 } } { \partial \hat { \xi } _ { j + 2 } ^ { ( 0 ) } } } \end{array}
$$

Denote the mean value of $\Phi$ with respect to $\lambda ^ { ( 1 ) }$ and $\lambda ^ { ( 2 ) }$ by $[ \Phi ]$ ； then $\partial [ \Phi _ { 1 } ] / \partial \eta _ { i } ^ { \left( 0 \right) } = 0$ since $\partial \Phi _ { 1 } / \partial \eta _ { i } ^ { ( 0 ) }$ contains only sine terms.We have

$$
\xi _ { i } ^ { ( 1 ) } = [ \xi _ { i } ^ { ( 1 ) } ] + \int \frac { \partial \Phi _ { 1 } } { \partial \eta _ { i } ^ { ( 0 ) } } d t ,
$$

which consists of only cosine terms. We derive $\big [ \xi _ { i } ^ { ( 1 ) } \big ]$ in the next step. The derivatives $\partial \Phi _ { 1 } / \partial \xi _ { j } ^ { ( 0 ) } \ ( j = 1 , 2 )$ contain only cosine terms.The mean value $[ \Phi _ { \imath } ]$ is even with respect to $\xi _ { j }$ and $\eta _ { j } \ ( j = 1 , 2 )$ . Hence $\partial [ \Phi _ { 1 } ] / \partial \xi _ { j } ^ { \scriptscriptstyle ( 0 ) } = 0$ Put $[ \eta _ { j } ^ { ( 1 ) } ] = 0$ ; then $\eta _ { j } ^ { \scriptscriptstyle ( 1 ) } = - \int ( \partial \Phi _ { 1 } / \partial \xi _ { j } ^ { \scriptscriptstyle ( 0 ) } ) \ d t$ and $\eta _ { j } ^ { ( 1 ) }$ is of sine form.If we take the mean values of both sides of the equations (16） giving ${ d \eta _ { j + 2 } } / { d t } \ ( j = 1 , 2 )$ ， then we obtain

$$
\begin{array} { r l r } & { } & { \frac { \hat { \sigma } ^ { 2 } F _ { 0 } } { \hat { \sigma } \Lambda ^ { ( 1 ) 2 } } \left[ \hat { \xi } _ { 3 } ^ { ( 1 ) } \right] + \frac { \hat { \sigma } ^ { 2 } F _ { 0 } } { \hat { \sigma } \Lambda ^ { ( 1 ) } \hat { \partial } \Lambda ^ { ( 2 ) } } \left[ \hat { \xi } _ { 4 } ^ { ( 1 ) } \right] = - \frac { \hat { \sigma } [ \Phi _ { 1 } ] } { \hat { \sigma } \hat { \xi } _ { 3 } ^ { ( 0 ) } } = - \frac { \hat { \sigma } [ \Phi _ { 1 } ] } { \hat { \sigma } \Lambda ^ { ( 1 ) } } , } \\ & { } & { \frac { \hat { \sigma } ^ { 2 } F _ { 0 } } { \hat { \sigma } \Lambda ^ { ( 1 ) } \hat { \partial } \Lambda ^ { ( 2 ) } } \left[ \hat { \xi } _ { 3 } ^ { ( 1 ) } \right] + \frac { \hat { \sigma } ^ { 2 } F _ { 0 } } { \hat { \sigma } \Lambda ^ { ( 2 ) 2 } } \left[ \hat { \xi } _ { 4 } ^ { ( 1 ) } \right] = - \frac { \hat { \sigma } [ \Phi _ { 1 } ] } { \hat { \sigma } \hat { \xi } _ { 4 } ^ { ( 0 ) } } = - \frac { \hat { \sigma } [ \Phi _ { 1 } ] } { \hat { \sigma } \Lambda ^ { ( 2 ) } } . } \end{array}
$$

Since

$$
\left| \begin{array} { c c } { { { \frac { \partial ^ { 2 } F _ { \scriptscriptstyle 0 } } { \partial \Lambda ^ { { \scriptscriptstyle ( 1 ) } 2 } } } } } & { { { \frac { \partial ^ { 2 } F _ { \scriptscriptstyle 0 } } { \partial \Lambda ^ { { \scriptscriptstyle ( 1 ) } } \partial \Lambda ^ { { \scriptscriptstyle ( 2 ) } } } } } } \\ { { { } } } & { { { } } } \\ { { { \frac { \partial ^ { 2 } F _ { \scriptscriptstyle 0 } } { \partial \Lambda ^ { { \scriptscriptstyle ( 1 ) } } \partial \Lambda ^ { { \scriptscriptstyle ( 2 ) } } } } } } & { { { \frac { \partial ^ { 2 } F _ { \scriptscriptstyle 0 } } { \partial \Lambda ^ { { \scriptscriptstyle ( 2 ) } 2 } } } } } \end{array} \right| \ne 0 ,
$$

$\left[ \hat { \xi } _ { 3 } ^ { ( 1 ) } \right]$ and $\big [ \xi _ { 4 } ^ { ( 1 ) } \big ]$ can be determined from these equations. Substitute the result for $\hat { \xi } _ { 3 } ^ { ( 1 ) }$ and $\xi _ { 4 } ^ { ( 1 ) }$ in the right-hand members of the equations (16) for $d \eta _ { j + 2 } ^ { ( 1 ) } / d t$ ； then they are seen to be of cosine form and $[ \eta _ { j + 2 } ^ { ( 1 ) } ] = 0$ Thus we see that $\eta _ { j + 2 } ^ { ( 1 ) }$ is of sine form.

Suppose that we have in this way determined

$$
\begin{array} { r l r l r l r l r l r l } & { \xi _ { j } ^ { ( 1 ) } , } & & { } & & { \xi _ { j } ^ { ( 2 ) } , } & { \quad } & { \cdots , } & { } & { \xi _ { j } ^ { ( k - 2 ) } , } & { } & { \xi _ { j } ^ { ( k - 1 ) } - [ \xi _ { j } ^ { ( k - 1 ) } ] , } \\ & { \vdots } & { } & & { \xi _ { j + 2 } ^ { ( 2 ) } , } & { } & & { \cdots , } & { } & { \xi _ { j + 2 } ^ { ( k - 2 ) } , } & { } & { \xi _ { j + 2 } ^ { ( k - 1 ) } } & { } & { ( j = 1 , 2 ) , } \end{array}
$$

in cosine form,and

$$
\eta _ { i } ^ { ( 1 ) } , \qquad \eta _ { i } ^ { ( 2 ) } , \qquad \cdots , \qquad \eta _ { i } ^ { ( k - 2 ) } , \qquad \eta _ { i } ^ { ( k - 1 ) } \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

in sine form.The next step is to determine

$$
[ \xi _ { j } ^ { ( k - 1 ) } ] , \qquad \xi _ { j } ^ { ( k ) } - [ \xi _ { j } ^ { ( k ) } ] , \qquad \xi _ { j + 2 } ^ { ( k ) } \qquad ( j = 1 , 2 ) ,
$$

and

$$
\begin{array} { r } { \eta _ { i } ^ { ( k ) } \qquad ( i = 1 , 2 , 3 , 4 ) . } \end{array}
$$

The $\eta _ { j } ^ { ( k ) }$ are given by

$$
\begin{array} { r } { \frac { d \eta _ { j } ^ { ( k ) } } { d t } = - \frac { \partial ^ { 2 } \Phi _ { 1 } } { \partial \hat { \xi } _ { j } ^ { ( 0 ) } \partial \hat { \xi } _ { 1 } ^ { ( 0 ) } } \left[ \hat { \xi } _ { 1 } ^ { ( k - 1 ) } \right] - \frac { \partial ^ { 2 } \Phi _ { 1 } } { \partial \hat { \xi } _ { j } ^ { ( 0 ) } \partial \hat { \xi } _ { 2 } ^ { ( 0 ) } } \left[ \hat { \xi } _ { 2 } ^ { ( k - 1 ) } \right] + ( C _ { j } ) \qquad ( j = 1 , } \end{array}
$$

where $( C _ { j } )$ denotes a known function of cosine form. Since the mean values of the right-hand members should be zero, we have

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } [ \hat { \Phi } _ { 1 } ] } { \partial \hat { \xi } _ { 1 } ^ { ( 0 ) 2 } } \left[ \hat { \xi } _ { 1 } ^ { ( k - 1 ) } \right] + \frac { \partial ^ { 2 } [ \hat { \Phi } _ { 1 } ] } { \partial \hat { \xi } _ { 1 } ^ { ( 0 ) } \partial \hat { \xi } _ { 2 } ^ { ( 0 ) } } \left[ \hat { \xi } _ { 2 } ^ { ( k - 1 ) } \right] = K _ { 1 } , } \\ & { \frac { \partial ^ { 2 } [ \hat { \Phi } _ { 1 } ] } { \partial \xi _ { 1 } ^ { ( 0 ) } \partial \hat { \xi } _ { 2 } ^ { ( 0 ) } } \left[ \hat { \xi } _ { 1 } ^ { ( k - 1 ) } \right] + \frac { \partial ^ { 2 } [ \hat { \Phi } _ { 1 } ] } { \partial \hat { \xi } _ { 2 } ^ { ( 0 ) 2 } } \left[ \hat { \xi } _ { 2 } ^ { ( k - 1 ) } \right] = K _ { 2 } , } \end{array}
$$

where $K _ { 1 }$ and $K _ { 2 }$ are known functions. These equations determine $[ \xi _ { 1 } ^ { ( k - 1 ) } ]$ and $[ \xi _ { 2 } ^ { ( k - 1 ) } ]$ ， because it can be shown by referring to the expansion of the disturbing function $[ F _ { 1 } ]$ that

$$
\Delta = \left| \begin{array} { l l } { \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \hat { \xi } _ { 1 } ^ { ( 0 ) 2 } } } & { \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \hat { \xi } _ { 1 } ^ { ( 0 ) } \partial \hat { \xi } _ { 2 } ^ { ( 0 ) } } } \\ { \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \hat { \xi } _ { 1 } ^ { ( 0 ) } \partial \hat { \xi } _ { 2 } ^ { ( 0 ) } } } & { \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \hat { \xi } _ { 2 } ^ { ( 0 ) 2 } } } \end{array} \right| \neq 0 .
$$

Put $[ \eta _ { j } ^ { ( k ) } ] = 0 ~ ( j = 1 , 2 )$ ； then the $\eta _ { j } ^ { ( k ) }$ are obtained in sine form.The $\hat { \xi } _ { i } ^ { ( k ) }$ are determined by

$$
\frac { d \pmb { \xi } _ { i } ^ { ( k ) } } { d t } = ( S _ { i } ) \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

where the $( S _ { i } )$ are known functions of sine form.Then we have

$$
\xi _ { i } ^ { ( k ) } = [ \xi _ { i } ^ { ( k ) } ] + \int ( S _ { i } ) d t \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

where $[ \xi _ { i } ^ { ( k ) } ]$ will be determined at a later stage. The $\eta _ { j + 2 } ^ { ( k ) } \left( j = 1 , 2 \right)$ can be obtained, in a manner similar to that for $\eta _ { 1 } ^ { ( k ) }$ and $\eta _ { 2 } ^ { ( k ) }$ ，from

$$
\frac { d \eta _ { j + 2 } ^ { ( k ) } } { d t } = - \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( j ) } \partial \Lambda ^ { ( 1 ) } } \left[ \xi _ { 3 } ^ { ( k ) } \right] - \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( j ) } \partial \Lambda ^ { ( 2 ) } } \left[ \xi _ { 4 } ^ { ( k ) } \right] + ( C _ { j + 2 } ) .
$$

Since the mean values of the right-hand members should be zero, we should have, with known functions $K _ { 3 }$ and $K _ { 4 }$ ，

$$
\begin{array} { l } { { \displaystyle { \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( 1 ) 2 } } [ \xi _ { 3 } ^ { ( k ) } ] + \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( 1 ) } \partial \Lambda ^ { ( 2 ) } } [ \xi _ { 4 } ^ { ( k ) } ] = K _ { 3 } } , } } \\ { { \displaystyle { \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( 1 ) } \partial \Lambda ^ { ( 2 ) } } [ \xi _ { 3 } ^ { ( k ) } ] + \frac { \partial ^ { 2 } F _ { 0 } } { \partial \Lambda ^ { ( 2 ) 2 } } [ \xi _ { 4 } ^ { ( k ) } ] = K _ { 4 } } , } } \end{array}
$$

which determine $\big [ \xi _ { 3 } ^ { ( k ) } \big ]$ and $[ \xi _ { 4 } ^ { ( k ) } ]$ . Put furter $[ \eta _ { j + 2 } ^ { ( k ) } ] = 0$ ; then the $\eta _ { j + 2 } ^ { ( k ) }$ are obtained in sineform.The unknown functions $\xi _ { j } ^ { ( k ) } - [ \xi _ { j } ^ { ( k ) } ]$ ， $\xi _ { j + 2 } ^ { ( k ) }$ $( j = 1 , 2 )$ are determined in cosine form,and the $\eta _ { i } ^ { ( k ) } \left( i = 1 , 2 , 3 , 4 \right)$ are in sine form.

Writing in (14)

$$
\xi _ { i } = \tilde { \xi } _ { i } + u _ { i } , \qquad \eta _ { i } = \tilde { \eta } _ { i } + v _ { i } \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

and expanding in powers of $u _ { i }$ and $v _ { i }$ we have the equations for variations

$$
\begin{array} { l l } { \displaystyle \frac { d u _ { i } } { d t } = \sum _ { k = 1 } ^ { 4 } \left\{ \frac { \hat { \partial } ^ { 2 } \Phi } { \partial \tilde { \gamma } _ { i } \partial \tilde { \xi } _ { k } } u _ { k } + \frac { \hat { \partial } ^ { 2 } \Phi } { \partial \tilde { \gamma } _ { i } \partial \tilde { \gamma } _ { k } } v _ { k } \right\} , } \\ { \displaystyle \frac { d v _ { i } } { d t } = - \sum _ { k = 1 } ^ { 4 } \left\{ \frac { \hat { \partial } ^ { 2 } \Phi } { \partial \tilde { \xi } _ { i } \partial \tilde { \xi } _ { k } } u _ { k } + \frac { \hat { \partial } ^ { 2 } \Phi } { \partial \tilde { \xi } _ { i } \partial \tilde { \gamma } _ { k } } v _ { k } \right\} ~ } & { ( i = 1 , 2 , 3 , 4 ) . } \end{array}
$$

These equations can be satisfied if

$$
u _ { i } = e ^ { \alpha t } \cdot s _ { i } , \qquad v _ { i } = e ^ { \alpha t } \cdot t _ { i } \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

where $s _ { i }$ and $t _ { i }$ are periodic functions of $\lambda ^ { ( 1 ) }$ and $\lambda ^ { ( 2 ) }$ . Put

$$
\begin{array} { l } { { \alpha = \mu \alpha ^ { ( 1 ) } + \mu ^ { 2 } \alpha ^ { ( 2 ) } + \cdots , } } \\ { { s _ { i } = s _ { i } ^ { ( 0 ) } + \mu s _ { i } ^ { ( 1 ) } + \cdots , ~ t _ { i } = t _ { i } ^ { ( 0 ) } + \mu t _ { i } ^ { ( 1 ) } + \cdots , } } \end{array}
$$

then

$$
\begin{array} { r l } & { \displaystyle \frac { d s _ { i } } { d t } + \alpha s _ { i } = \sum _ { k = 1 } ^ { 4 } \left\{ \frac { \partial ^ { 2 } \Phi } { \partial \tilde { \gamma } _ { i } \partial \hat { \xi } _ { k } } s _ { k } + \frac { \partial ^ { 2 } \Phi } { \partial \tilde { \gamma } _ { i } \partial \tilde { \gamma } _ { k } } t _ { k } \right\} , } \\ & { \displaystyle \frac { d t _ { i } } { d t } + \alpha t _ { i } = - \sum _ { k = 1 } ^ { 4 } \left\{ \frac { \partial ^ { 2 } \Phi } { \partial \tilde { \xi } _ { i } \partial \tilde { \xi } _ { k } } s _ { k } + \frac { \partial ^ { 2 } \Phi } { \partial \tilde { \xi } _ { i } \partial \tilde { \gamma } _ { k } } t _ { k } \right\} \qquad ( i = 1 , 2 , 3 , 4 ) . } \end{array}
$$

The coefficients of $s _ { k }$ and $t _ { \kappa }$ on the right-hand sides are also expanded in powers of $\mu$ in the form

$$
\frac { \partial ^ { 2 } \Phi } { \partial \tilde { \eta } _ { i } \partial \tilde { \xi } _ { k } } = B _ { i k } = B _ { i k } ^ { ( 0 ) } + \mu B _ { i k } ^ { ( 1 ) } + \cdots ,
$$

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } \tilde { \Phi } } { \partial \tilde { \eta } _ { i } \partial \tilde { \eta } _ { k } } = C _ { i k } = C _ { i k } ^ { ( 0 ) } + \mu C _ { i k } ^ { ( 1 ) } + \cdots , } \\ & { } \\ & { \frac { \partial ^ { 2 } \tilde { \Phi } ^ { \cdot } } { \partial \tilde { \xi } _ { i } \partial \tilde { \eta } _ { k } } = A _ { i k } = A _ { i k } ^ { ( 0 ) } + \mu A _ { i k } ^ { ( 1 ) } + \cdots , } \end{array}
$$

where $B _ { i k } ^ { ( 0 ) } = C _ { i k } ^ { ( 0 ) } = 0$ ，and $A _ { i k } ^ { ( 0 ) } = 0$ ，except ${ \cal A } _ { 3 3 } ^ { ( 0 ) } = \partial ^ { 2 } { \cal F } _ { 0 } / \partial \Lambda ^ { ( 1 ) 2 }$ ${ \cal A } _ { 4 4 } = \partial ^ { 2 } { \cal F } _ { 0 } / \partial \Lambda ^ { ( 2 ) 2 }$ . First we obtain

$$
\begin{array} { r l r } { \frac { d s _ { i } ^ { ( 0 ) } } { d t } = 0 } & { { } } & { ( i = 1 , 2 , 3 , 4 ) , } \end{array}
$$

$$
\frac { d t _ { i } ^ { \scriptscriptstyle ( 0 ) } } { d t } = 0 , \quad \frac { d t _ { j + 2 } ^ { \scriptscriptstyle ( 0 ) } } { d t } = - A _ { j + 2 , j + 2 } ^ { \scriptscriptstyle ( 0 ) } s _ { j + 2 } ^ { \scriptscriptstyle ( 0 ) } \qquad ( j = 1 , 2 ) .
$$

From the terms in $\mu$ we get

$$
\begin{array} { l } { { \displaystyle { \frac { d S _ { i } ^ { ( 1 ) } } { d t } + \alpha ^ { ( 1 ) } s _ { i } ^ { ( 0 ) } = \sum _ { k } B _ { i k } ^ { ( 1 ) } s _ { k } ^ { ( 0 ) } + \sum _ { k } C _ { i k } ^ { ( 1 ) } t _ { k } ^ { ( 0 ) } } , } } \\ { { \displaystyle { \frac { d t _ { i } ^ { ( 0 ) } } { d t } + \alpha ^ { ( 1 ) } t _ { i } ^ { ( 0 ) } = - \sum _ { k } A _ { i k } ^ { ( 1 ) } s _ { k } ^ { ( 0 ) } - \sum _ { k } B _ { k i } ^ { ( 1 ) } t _ { k } ^ { ( 0 ) } } , } } \\ { { \displaystyle { \frac { d t _ { j + 2 } ^ { ( 0 ) } } { d t } + \alpha ^ { ( 1 ) } t _ { j + 2 } ^ { ( 0 ) } = - A _ { j + 2 , j + 2 } ^ { ( 0 ) } s _ { j + 2 } ^ { ( 1 ) } - \sum _ { k } A _ { j + 2 , k } ^ { ( 1 ) } s _ { k } ^ { ( 0 ) } - \sum _ { k } B _ { k , j + 1 } ^ { ( 1 ) } } } } \end{array}
$$

where $\pmb { A } _ { i k } ^ { ( \nu ) }$ and $C _ { i k } ^ { ( \nu ) }$ are trigonometric series in cosine form in $\lambda ^ { ( 1 ) }$ and $\lambda ^ { ( 2 ) }$ ，and $B _ { i k } ^ { ( \nu ) }$ are in sine form.Write

$$
[ A _ { i k } ^ { ( \nu ) } ] = a _ { i k } ^ { ( \nu ) } , \qquad [ B _ { i k } ^ { ( \nu ) } ] = b _ { i k } ^ { ( \nu ) } , \qquad [ C _ { i k } ^ { ( \nu ) } ] = c _ { i k } ^ { ( \nu ) } ;
$$

then we have

$$
a _ { j k } ^ { \scriptscriptstyle ( 1 ) } = \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \hat { \xi } _ { j } ^ { \scriptscriptstyle ( 0 ) } \partial \hat { \xi } _ { k } ^ { \scriptscriptstyle ( 0 ) } } , \qquad c _ { j k } ^ { \scriptscriptstyle ( 1 ) } = \frac { \partial ^ { 2 } [ \Phi _ { 1 } ] } { \partial \eta _ { j } ^ { \scriptscriptstyle ( 0 ) } \partial \eta _ { k } ^ { \scriptscriptstyle ( 0 ) } } \qquad ( j , k = 1 , 2 ) .
$$

In order that $s _ { i } ^ { ( 1 ) }$ and $t _ { i } ^ { ( 1 ) }$ be periodic in $\lambda ^ { ( 1 ) }$ and $\lambda ^ { ( 2 ) }$ , it is necessary and sufficient that

$$
\left[ { \frac { d s _ { i } ^ { ( 1 ) } } { d t } } \right] = 0 , \qquad \left[ { \frac { d t _ { i } ^ { ( 1 ) } } { d t } } \right] = 0 \qquad ( i = 1 , 2 , 3 , 4 ) .
$$

In order that $s _ { i } ^ { ( 1 ) }$ and $t _ { i } ^ { ( 1 ) }$ may be derived from these equations, it is necessary and sufficient that

$$
\begin{array} { r } { - \alpha ^ { ( 1 ) } s _ { 1 } ^ { ( 0 ) } + c _ { 1 1 } ^ { ( 1 ) } t _ { 1 } ^ { ( 0 ) } + c _ { 1 2 } ^ { ( 1 ) } t _ { 2 } ^ { ( 0 ) } = 0 , } \\ { - \alpha ^ { ( 1 ) } s _ { 2 } ^ { ( 0 ) } + c _ { 2 1 } ^ { ( 1 ) } t _ { 1 } ^ { ( 0 ) } + c _ { 2 2 } ^ { ( 1 ) } t _ { 2 } ^ { ( 0 ) } = 0 , } \end{array}
$$

$$
\begin{array} { r } { a _ { 1 1 } ^ { ( 1 ) } s _ { 1 } ^ { ( 0 ) } + a _ { 1 2 } ^ { ( 1 ) } s _ { 2 } ^ { ( 0 ) } + \alpha ^ { ( 1 ) } t _ { 1 } ^ { ( 0 ) } = 0 , } \\ { a _ { 2 1 } ^ { ( 1 ) } s _ { 1 } ^ { ( 0 ) } + a _ { 2 2 } ^ { ( 1 ) } s _ { 2 } ^ { ( 0 ) } + \alpha ^ { ( 1 ) } t _ { 2 } ^ { ( 0 ) } = 0 . } \end{array}
$$

The root $\alpha ^ { ( 1 ) }$ is determined from

$$
\mathrm { \Lambda } ^ { 4 } + \{ a _ { 1 1 } ^ { ( 1 ) } c _ { 1 1 } ^ { ( 1 ) } + 2 a _ { 1 2 } ^ { ( 1 ) } c _ { 2 1 } ^ { ( 1 ) } + a _ { 2 2 } ^ { ( 1 ) } c _ { 2 2 } ^ { ( 1 ) } \} \alpha ^ { ( 1 ) 2 } + | \begin{array} { l l } { { a _ { 1 1 } ^ { ( 1 ) } } } & { { a _ { 1 2 } ^ { ( 1 ) } } } \\ { { a _ { 2 1 } ^ { ( 1 ) } } } & { { a _ { 2 2 } ^ { ( 1 ) } | c _ { 2 1 } ^ { ( 1 ) }  } } \end{array}  \ c _ { 1 2 } ^ { ( 1 ) } | = 0
$$

If the inclination is sufficiently small the $c _ { i j } ^ { ( 1 ) }$ are nearly equal to $a _ { i j } ^ { \left( 1 \right) }$ and we have

$$
\alpha ^ { ( 1 ) 4 } + \big \{ a _ { 1 1 } ^ { ( 1 ) 2 } + 2 a _ { 1 2 } ^ { ( 1 ) 2 } + a _ { 2 2 } ^ { ( 1 ) 2 } \big \} \alpha ^ { ( 1 ) 2 } + \bigg | _ { a _ { 2 1 } ^ { ( 1 ) } } ^ { a _ { 1 1 } ^ { ( 1 ) } } - { a _ { 2 2 } ^ { ( 1 ) } } \bigg | ^ { 2 } = 0 .
$$

The roots $\alpha ^ { ( 1 ) 2 }$ are real and negative.In the general case, the roots may become positive through being both equal to zero,or become imaginary through being a pair of equal roots.In such a case the values of $\Lambda ^ { ( 1 ) }$ and $\Lambda ^ { ( 2 ) }$ are so chosen that the two roots are still real and negative.

Then to each root $\alpha ^ { ( 1 ) }$ there corresponds a set of values of $s _ { 1 } ^ { ( 0 ) } , s _ { 2 } ^ { ( 0 ) }$ $t _ { 1 } ^ { ( 0 ) } , t _ { 2 } ^ { ( 0 ) }$ ， one of which can be taken arbitrarily. The solution of (19) gives

$$
\begin{array} { l } { { s _ { i } ^ { ( 1 ) } = [ s _ { i } ^ { ( 1 ) } ] + S _ { i 3 } t _ { 3 } ^ { ( 0 ) } + S _ { i 4 } t _ { 4 } ^ { ( 0 ) } + S _ { i } ^ { ( 1 ) } , } } \\ { { t _ { i } ^ { ( 1 ) } = [ t _ { i } ^ { ( 1 ) } ] + T _ { i 3 } t _ { 3 } ^ { ( 0 ) } + T _ { i 4 } t _ { 4 } ^ { ( 0 ) } + T _ { i } ^ { ( 1 ) } ~ ( i = 1 , 2 , 3 , 4 ) , } } \end{array}
$$

where $S _ { i 3 } , S _ { i 4 } , T _ { i 3 } , T _ { i 4 }$ are known periodic functions of $\lambda ^ { ( 1 ) }$ and $\lambda ^ { ( 2 ) }$ with their mean values equal to zero. In order that $t _ { j + 2 } ^ { ( 1 ) }$ be periodic, it is necessary and sufficient to have

$$
\alpha ^ { ( 1 ) } t _ { j + 2 } ^ { ( 0 ) } + A _ { j + 2 , j + 2 } ^ { ( 1 ) } [ S _ { j + 2 } ^ { ( 1 ) } ] = k _ { j + 2 } ^ { ( 1 ) } ~ ( j = 1 , 2 ) ,
$$

with known constants $k _ { j + 2 } ^ { ( 1 ) }$ .From (17) we obtain further

$$
t _ { j + 2 } ^ { ( 1 ) } = [ t _ { j + 2 } ^ { ( 1 ) } ] + T _ { j + 2 , 3 } t _ { 3 } ^ { ( 0 ) } + T _ { j + 2 , 4 } t _ { 4 } ^ { ( 0 ) } + T _ { j + 2 } ^ { ( 1 ) } \qquad ( j = 1 , 2 ) ,
$$

where the mean values of $T _ { j + 2 , 3 } , T _ { j + 3 , 4 } , T _ { j + 2 } ^ { \scriptscriptstyle ( 1 ) }$ are zero.

We have two more relations among $t _ { 3 } ^ { ( 0 ) } , t _ { 4 } ^ { ( 0 ) } , [ S _ { 3 } ^ { ( 1 ) } ]$ ,and $\big [ s _ { 4 } ^ { ( 1 ) } \big ]$ . In fact, we have from (19)

$$
\begin{array} { r } { \frac { d S _ { j + 2 } ^ { ( 2 ) } } { d t } + \alpha ^ { ( 1 ) } s _ { j + 2 } ^ { ( 1 ) } = \displaystyle \sum _ { k = 1 } ^ { 4 } B _ { j + 2 , k } ^ { ( 1 ) } s _ { k } ^ { ( 1 ) } + \displaystyle \sum _ { k } C _ { j + 2 , k } ^ { ( 1 ) } t _ { k } ^ { ( 1 ) } } \\ { + \displaystyle \sum _ { k } B _ { j + 2 , k } ^ { ( 2 ) } s _ { k } ^ { ( 1 ) } + \displaystyle \sum _ { k } C _ { j + 2 , k } ^ { ( 2 ) } t _ { k } ^ { ( 1 ) } . } \end{array}
$$

Taking the mean values of both sides we derive one of the relations

$$
- \alpha ^ { ( 1 ) } [ s _ { j + 2 } ^ { ( 1 ) } ] + K _ { j + 2 , 3 } t _ { 3 } ^ { ( 0 ) } + K _ { j + 2 , 4 } t _ { 4 } ^ { ( 0 ) } = K _ { j + 2 } ^ { ( 1 ) } ~ ( j = 1 , 2 ) ,
$$

with known constants $K _ { j + 2 , 3 } , K _ { j + 2 , 4 } , K _ { j + 2 } ^ { ( 1 ) }$ where we can show that $K _ { j + 2 , 3 } = K _ { j + 2 , 4 } = 0$ .Hence we are left with

$$
- \alpha ^ { { \scriptscriptstyle ( 1 ) } } [ s _ { j + 2 } ^ { ( 1 ) } ] = K _ { j + 2 } ^ { { \scriptscriptstyle ( 1 ) } } \qquad ( j = 1 , 2 ) .
$$

These equations determine $\left[ S _ { 3 } ^ { ( 1 ) } \right]$ and $\left[ s _ { 4 } ^ { ( 1 ) } \right]$ . Then $\pmb { t } _ { 3 } ^ { ( 0 ) }$ and $\pmb { t } _ { 4 } ^ { ( 0 ) }$ are given by (20).Thus we have determined

$$
\begin{array} { r l } { ^ { 0 ) } , \quad } & { s _ { j } ^ { ( 1 ) } - [ s _ { j } ^ { ( 1 ) } ] , \quad \quad s _ { j + 2 } ^ { ( 0 ) } , \quad \quad s _ { j + 2 } ^ { ( 1 ) } \quad ( j = 1 , 2 ) , } \\ { t _ { i } ^ { ( 0 ) } , \quad } & { t _ { i } ^ { ( 1 ) } - [ t _ { i } ^ { ( 1 ) } ] \quad \quad ( i = 1 , 2 , 3 , 4 ) , } \end{array}
$$

and hence we can determine $s _ { j + 2 } ^ { ( 2 ) } ~ ( j = 1 , 2 )$ at the next step.

The process can be shown to hold for any number of steps. Thus the solution is obtained in the form (18).The roots $_ { \alpha }$ can be taken as pure imaginary, so that $\overline { { \alpha } } = - \alpha$ ，where $\bar { \alpha }$ is the conjugate imaginary root.In fact, we should have

$$
\sum _ { i = 1 } ^ { 4 } { ( u _ { i } \overline { { v } } _ { i } - \bar { u } _ { i } v _ { i } ) } = \mathrm { c o n s t a n t } ,
$$

or

$$
\exp \{ ( \alpha + \bar { \alpha } ) t \} \cdot \sum _ { i = 1 } ^ { 4 } \ ( s _ { i } \bar { t } _ { i } - \bar { s } _ { i } t _ { i } ) = \mathrm { c o n s t a n t } .
$$

Hence

$$
\alpha + \overline { { { \alpha } } } = 0 .
$$

Thus the solution is obtained in the form

$$
\begin{array} { l } { { \displaystyle { u _ { i \bar { \star } } } \Big \vert = \sum _ { i _ { 1 } , i _ { 2 } } C _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \cos \big ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } \big ) } } \\ { { \displaystyle ~ + \sum _ { i _ { 1 } , i _ { 2 } } S _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \sin \big ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } \big ) \qquad ( k = 1 , 2 ) , } } \end{array}
$$

where

$$
\bar { \lambda } ^ { ( k ) } = \bar { n } _ { k } t + \bar { c } ^ { ( k ) } , \qquad \bar { n } _ { k } = \frac { \alpha _ { k } } { \sqrt { - 1 } } ,
$$

and the $\bar { \pmb { c } } ^ { ( k ) }$ are arbitrary constants.

In the equations (17) the coefficients of $u _ { k }$ and ${ \boldsymbol { v } } _ { \kappa }$ in the first four equations are of sine and cosine form respectively. The coefficients in the last four equations are of cosine and sine form respectively. The solution of (17) is thus

$$
u _ { i k } = \sum _ { i _ { 1 } , i _ { 2 } } C _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \cos { ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } ) } ,
$$

$$
v _ { i k } = \sum _ { i _ { 1 } , i _ { 2 } } S _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \sin \left( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } \right)
$$

$$
( i = 1 , 2 , 3 , 4 ) .
$$

By replacing $\bar { c } ^ { ( k ) } - \pi / 2$ by $\bar { c } ^ { ( k ) }$ we obtain a new solution

$$
\bar { u } _ { i k } = \sum _ { i _ { 1 } , i _ { 2 } } C _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \sin { ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } ) } ,
$$

$$
\overline { { v } } _ { i k } = \sum _ { i _ { 1 } , i _ { 2 } } S _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \cos { ( i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + \bar { \lambda } ^ { ( k ) } ) } .
$$

Thus (18), (22) and (22a) constitute the fundamental system of solutions of the linear differential equations (17).Hence we conclude that, when the constants $\Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) }$ ，and $\pmb { J }$ are so chosen that the two roots $\alpha _ { 1 } ^ { ( 1 ) 2 }$ and $\alpha _ { 2 } ^ { ( 1 ) 2 }$ are unequal and negative and that $i _ { 1 } ^ { \prime } \alpha _ { 1 } ^ { ( 1 ) } + i _ { 2 } ^ { \prime } \alpha _ { 2 } ^ { ( 1 ) }$ is not zero,then the canonical system (16) can be solved formally by series of the form

$$
\begin{array} { r l } & { \xi _ { i } = \displaystyle \sum _ { \lambda } C ( \Lambda ^ { \scriptscriptstyle ( 1 ) } , \Lambda ^ { \scriptscriptstyle ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \cos A , } \\ & { \eta _ { i } = \displaystyle \sum _ { \lambda } S ( \Lambda ^ { \scriptscriptstyle ( 1 ) } , \Lambda ^ { \scriptscriptstyle ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \sin A , } \end{array}
$$

$$
A = i _ { 1 } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } \lambda ^ { \scriptscriptstyle ( 2 ) } + i _ { 1 } ^ { \prime } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } ^ { \prime } \lambda ^ { \scriptscriptstyle ( 2 ) } ,
$$

$$
\lambda ^ { \scriptscriptstyle ( p ) } = n , t + c ^ { \scriptscriptstyle ( p ) } , \qquad \lambda ^ { \scriptscriptstyle ( p ) } = n _ { \scriptscriptstyle \nu } ^ { \prime } t + c ^ { \scriptscriptstyle ( p ) } ,
$$

where $\varepsilon _ { 1 }$ and $\varepsilon _ { 2 }$ are arbitrary constants and

$$
k _ { \nu } = \vert i _ { \nu } ^ { \prime } \vert + \mathrm { a n ~ e v e n ~ i n t e g e r } ,
$$

$$
n _ { \nu } ^ { \prime } = n _ { \nu } ^ { \prime ( 0 ) } + n _ { \nu } ^ { \prime ( 2 ) } + \cdot \cdot \cdot + n _ { \nu } ^ { \prime ( 2 l ) } + \cdot \cdot \cdot ,
$$

where $n _ { s } ^ { \prime ( 2 l ) }$ are homogeneous polynomials of degree $ { l }$ in $\pmb { \varepsilon } _ { 1 } ^ { 2 }$ and $\pmb { \varepsilon _ { 2 } ^ { 2 } }$ whose coefficients are arranged in increasing powers of $\mu$ and divisible by $\mu$ · Furthermore, $\xi _ { 3 }$ and $\xi _ { 4 }$ are also divisible by $\mu$

The proof proceeds similarly to the foregoing by expanding the solution $\xi _ { i }$ and $\eta _ { i }$ and computing the solution in successive steps in series of the stated form.

We say that the right-hand members of (22) and (22a) are respectively of the forms $\{ C \}$ and $\{ S \}$ . When $| i _ { 1 } ^ { \prime } | + | i _ { 2 } ^ { \prime } | = r -$ an even integer and $k _ { 1 } + k _ { 2 } = r +$ an even integer, we write them as $\{ C \} _ { r }$ and $\{ S \} _ { r }$ ， respectively. When $k _ { 1 } + k _ { 2 } = r$ ，we write them $\{ C \} _ { r r }$ and $\{ S \} _ { r r }$ ， respectively.Expand $\xi _ { i }$ and $\eta _ { i }$ in the form

$$
\begin{array} { r } { \xi _ { i } = \delta _ { 0 } \xi _ { i } + \delta _ { 1 } \xi _ { i } + \cdot \cdot \cdot + \delta _ { \nu } \xi _ { i } + \cdot \cdot \cdot , } \\ { \eta _ { i } = \delta _ { 0 } \eta _ { i } + \delta _ { 1 } \eta _ { i } + \cdot \cdot \cdot + \delta _ { \nu } \eta _ { i } + \cdot \cdot \cdot , } \end{array}
$$

where $\delta _ { \nu } \xi _ { i }$ is of the form $\{ C \} _ { r }$ and $\delta _ { \nu \eta _ { i } }$ is of the form $\{ S \} _ { \tau }$

First put

$$
\begin{array} { l } { { \displaystyle \delta _ { 1 } \xi _ { i } = \sum _ { k = 1 } ^ { 2 } \varepsilon _ { k } \sum _ { i _ { 1 } , i _ { 2 } } C _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \cos \big ( i _ { 1 } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } \lambda ^ { \scriptscriptstyle ( 2 ) } + \lambda ^ { \scriptscriptstyle ( \iota ( k ) ) } , } } \\ { { \displaystyle \delta _ { 1 } \eta _ { i } = \sum _ { k = 1 } ^ { 2 } \varepsilon _ { k } \sum _ { i _ { 1 } , i _ { 2 } } S _ { i _ { 1 } i _ { 2 } } ^ { ( i , k ) } \sin \big ( i _ { 1 } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } \lambda ^ { \scriptscriptstyle ( 2 ) } + \lambda ^ { \scriptscriptstyle ( \iota ( k ) ) } } } \end{array}
$$

Then $\delta _ { 1 } \xi _ { i }$ and $\delta _ { 1 } \eta _ { i }$ are determined by

$$
\begin{array} { r l } & { \frac { d \hat { \theta } _ { 1 } \hat { \xi } _ { i } } { d t } - \displaystyle \sum _ { s = 1 } ^ { 2 } \left( n _ { s } ^ { \prime } - n _ { s } ^ { \prime ( 0 ) } \right) \frac { \partial } { \partial \lambda ^ { \prime ( s ) } } = \displaystyle \sum _ { k = 1 } ^ { 4 } \left\{ B _ { i k } \hat { \theta } _ { 1 } \hat { \xi } _ { k } + C _ { i k } \hat { \theta } _ { 1 } \eta _ { k } \right\} , } \\ & { \frac { d \hat { \theta } _ { 1 } \eta _ { i } } { d t } - \displaystyle \sum _ { s = 1 } ^ { 2 } \left( n _ { s } ^ { \prime } - n _ { s } ^ { \prime ( 0 ) } \right) \frac { \partial } { \partial \lambda ^ { \prime ( s ) } } = - \displaystyle \sum _ { k = 1 } ^ { 4 } \left\{ A _ { i k } \hat { \theta } _ { 1 } \hat { \xi } _ { k } + B _ { k i } \hat { \theta } _ { 1 } \eta _ { k } \right\} , } \end{array}
$$

for all values of $n _ { 1 } ^ { \prime } - n _ { 1 } ^ { \prime ( 0 ) }$ and $n _ { 2 } \mathrm { ~ - ~ } n _ { 2 } ^ { \prime ( 0 ) }$

Consider the equations

$$
\begin{array} { l } { \displaystyle \frac { d u _ { i } } { d t } = \sum _ { k = 1 } ^ { 4 } \left\{ B _ { i k } u _ { k } + C _ { i k } v _ { k } \right\} + \mu U _ { i } , } \\ { \displaystyle \frac { d v _ { i } } { d t } = - \sum _ { k = 1 } ^ { 4 } \left\{ A _ { i k } u _ { k } + B _ { k i } v _ { k } \right\} + \mu V _ { i } ~ ( i = 1 , 2 , 3 , 4 ) , } \end{array}
$$

where $U _ { i }$ and $V _ { i }$ are known functions of the form $\{ S \} _ { r r }$ and $\{ C \} _ { r r }$ ， respectively. If $U _ { i } = V _ { i } = 0$ ,then the equations reduce to (17).By the properties of the fundamental system of solutions we have a matrix with the fundamental system (22) and (22a):

$$
\begin{array} { l l l l l l l l } { { u _ { 1 } | ( S _ { 1 } ) } } & { { ( S _ { 2 } ) } } & { { t ( S _ { 1 } ) + ( C _ { 1 } ) } } & { { t ( S _ { 2 } ) + ( C _ { 2 } ) } } & { { u _ { 1 1 } } } & { { \bar { u } _ { 1 1 } } } & { { u _ { 1 2 } } } & { { \bar { u } _ { 1 2 } } } \\ { { u _ { 2 } | ( S _ { 1 } ) } } & { { ( S _ { 2 } ) } } & { { t ( S _ { 1 } ) + ( C _ { 1 } ) } } & { { t ( S _ { 2 } ) + ( C _ { 2 } ) } } & { { u _ { 2 1 } } } & { { \bar { u } _ { 2 1 } } } & { { u _ { 2 2 } } } & { { \bar { u } _ { 2 2 } } } \\ { { u _ { 3 } | ( S _ { 1 } ) } } & { { ( S _ { 2 } ) } } & { { t ( S _ { 3 } ) + ( C _ { 1 } ) } } & { { t ( S _ { 2 } ) + ( C _ { 2 } ) } } & { { u _ { 3 1 } } } & { { \bar { u } _ { 3 1 } } } & { { u _ { 3 2 } } } & { { \bar { u } _ { 3 2 } } } \\ { { u _ { 4 } | ( S _ { 1 } ) } } & { { ( S _ { 2 } ) } } & { { t ( S _ { 1 } ) + ( C _ { 1 } ) } } & { { t ( S _ { 2 } ) + ( C _ { 2 } ) } } & { { u _ { 4 1 } } } & { { \bar { u } _ { 4 1 } } } & { { u _ { 4 2 } } } & { { \bar { u } _ { 4 2 } } } \\ { { v _ { 1 } | ( \bar { C } _ { 1 } ) } } & { { ( \bar { C } _ { 2 } ) } } & { { t ( \bar { C } _ { 1 } ) + ( \bar { S } _ { 1 } ) } } & { { t ( \bar { C } _ { 2 } ) + ( \bar { S } _ { 2 } ) } } & { { v _ { 1 1 } } } & { { \bar { v } _ { 1 1 } } } & { { v _ { 1 2 } } } & { { \bar { v } _ { 1 2 } } } \\ { { v _ { 2 } | ( \bar { C } _ { 1 } ) } } & { { ( \bar { C } _ { 2 } )  } } &   t ( \bar { C } _ { 1 } ) + ( \bar \end{array}
$$

The first four columns are the same as those for the equations (17) and the last four columns are the fundamental system defined by (22) and (22a). Thus the eight systems represented by the columns of this matrix are the fundamental system of (24). Let the kth column be $u _ { 1 } ^ { ( k ) } , u _ { 2 } ^ { ( k ) } , \ldots , v _ { 1 } ^ { ( k ) } , v _ { 2 } ^ { ( k ) }$ ,;then the general solution of (17) is

$$
u _ { i } = \sum _ { k = 1 } ^ { 8 } c _ { k } u _ { i } ^ { ( k ) } , \qquad v _ { i } = \sum _ { k = 1 } ^ { 8 } c _ { k } v _ { i } ^ { ( k ) } \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

with arbitrary constants $c _ { 1 } , \ldots , c _ { 8 }$ . The general solution of (24) can be put in a similar form, where $c _ { 1 } , \ldots , c _ { 8 }$ are not arbitrary constants but are connected by

$$
\Delta \frac { d c _ { k } } { d t } = \mu \cdot \sum _ { i = 1 } ^ { 4 } \ : \left\{ U _ { i } \frac { \partial \Delta } { \partial u _ { i } ^ { ( k ) } } + V _ { i } \frac { \partial \Delta } { \partial v _ { i } ^ { ( k ) } } \right\} \qquad ( k = 1 , 2 , \ldots , 8 ) .
$$

Under certain conditions we can construct a solution expanded in increasing powers of $\mu , \varepsilon _ { 1 } , \varepsilon _ { 2 }$ without secular term,that is,

$$
\begin{array} { c } { { c _ { 1 } u _ { 1 } ^ { \left( 1 \right) } + c _ { 3 } u _ { 1 } ^ { \left( 3 \right) } = \left( S _ { 1 } \right) \displaystyle \int \displaystyle \frac { 1 } { \Delta } | \mu U _ { 1 } , \left( S _ { 2 } \right) , t ( S _ { 1 } ) + \left( C _ { 1 } \right) , \left( C _ { 2 } \right) , \ldots | d t } } \\ { { \displaystyle + \left. t ( S _ { 1 } ) + \left( C _ { 1 } \right) \right. \cdot \displaystyle \int \displaystyle \frac { 1 } { \Delta } | \left( S _ { 1 } \right) , \left( S _ { 2 } \right) , \mu U _ { 1 } , \left( C _ { 2 } \right) , \ldots | d t } } \end{array}
$$

The first integral on the right-hand side contains terms proportional to $t$ .Integrating by parts we obtain

$$
\begin{array} { l } { { \displaystyle c _ { 1 } u _ { 1 } ^ { \scriptscriptstyle ( 1 ) } + c _ { 3 } u _ { 1 } ^ { \scriptscriptstyle ( 3 ) } = ( S _ { 1 } ) \int \frac { 1 } { \Delta } | \mu U _ { 1 } , ( S _ { 2 } ) , ( C _ { 1 } ) , ( S _ { 2 } ) , \dots | d t } } \\ { ~ } \\ { { \displaystyle ~ + ~ ( S _ { 1 } ) \int \int \frac { 1 } { \Delta } | ( S _ { 1 } ) , ( S _ { 2 } ) , \mu U _ { 1 } , ( C _ { 2 } ) , \dots | d t ^ { 2 } } } \\ { { \displaystyle ~ + ~ ( C _ { 1 } ) \int \frac { 1 } { \Delta } | ( S _ { 1 } ) , ( S _ { 2 } ) , \mu U _ { 1 } , ( C _ { 2 } ) , \dots | d t . } } \end{array}
$$

The determinants in the integrands are trigonometric series with arguments $\lambda ^ { ( 1 ) } , \lambda ^ { ( 2 ) } , \lambda ^ { \prime ( 1 ) } , \lambda ^ { \prime ( 2 ) }$ . By the integration of a term of the form

$$
A \cos \left( i _ { 1 } \lambda ^ { \scriptscriptstyle ( 1 ) } + i _ { 2 } \lambda ^ { \scriptscriptstyle ( 2 ) } + i _ { 1 } ^ { \prime } \lambda ^ { \prime \scriptscriptstyle ( 1 ) } + i _ { 2 } ^ { \prime } \lambda ^ { \prime \scriptscriptstyle ( 2 ) } \right)
$$

there appears a divisor

$$
\frac { 1 } { i _ { 1 } n _ { 1 } + i _ { 2 } n _ { 2 } + i _ { 1 } ^ { \prime } n _ { 1 } ^ { \prime } + i _ { 2 } ^ { \prime } n _ { 2 } ^ { \prime } } .
$$

We expand this divisor in increasing powers of $\mu , \varepsilon _ { 1 } , \varepsilon _ { 2 }$ If one of $i _ { 1 }$ and $i _ { 2 }$ is not zero, only positive powers appear. If $i _ { 1 } = i _ { 2 } = 0$ ，then $\pmb { \mu }$ appears in the denominator.When integrated once, this factor is cancelled by the factor $\pmb { \mu }$ which multiplies $U _ { 1 } , \dots , U _ { 4 } , V _ { 1 } , \dots , V _ { 4 }$ When integrated twice,we get a divisor $\mu ^ { 2 }$ .In order that this term may vanish in the double integral, it is necessary and sufficient to have

$$
[ U _ { 3 } ^ { ( 0 ) } ] _ { \lambda ^ { ( 1 ) } \lambda ^ { ( 2 ) } } = 0 .
$$

In that case $c _ { 1 } u _ { 1 } ^ { ( 1 ) } + c _ { 3 } u _ { 1 } ^ { ( 3 ) }$ is of the form $\{ C \} _ { r }$ . Similarly $c _ { 2 } u _ { 1 } ^ { ( 2 ) } + c _ { 4 } u _ { 1 } ^ { ( 4 ) }$ is of the form $\{ C \} _ { r }$ if $[ U _ { 4 } ^ { \scriptscriptstyle ( 0 ) } ] _ { \lambda ^ { ( 1 ) } \lambda ^ { ( 2 ) } } = 0$ . Thus we get $\scriptstyle \sum _ { k = 1 } ^ { 4 } c _ { k } u _ { i } ^ { ( k ) }$ in the form $\{ C \} _ { r }$ ，and $\scriptstyle \sum _ { k = 1 } ^ { 4 } c _ { k } v _ { i } ^ { ( k ) }$ in the form $\{ S \} _ { \tau }$ .Hence we obtain the result :

The solution of the system of differential equations

$$
\begin{array} { r l } & { \displaystyle \frac { d u _ { i } } { d t } = \sum _ { k = 1 } ^ { 4 } \left\{ B _ { i k } u _ { k } + C _ { i k } v _ { k } \right\} + \mu U _ { i } + \sum _ { s = 1 } ^ { 2 } \kappa _ { s } \frac { \partial \partial _ { 1 } \hat { \xi } _ { i } } { \partial \lambda ^ { \prime ( s ) } } , } \\ & { \displaystyle \frac { d v _ { i } } { d t } = - \sum _ { k = 1 } ^ { 4 } \left\{ A _ { i k } u _ { k } + B _ { k i } v _ { k } \right\} + \mu V _ { i } + \sum _ { s = 1 } ^ { 2 } \kappa _ { s } \frac { \partial \hat { \partial } _ { 1 } \gamma _ { i } } { \partial \lambda ^ { \prime ( s ) } } } \end{array}
$$

where $U _ { i }$ and $V _ { i }$ are of the form $\{ S \} _ { 2 l + 1 , 2 l + 1 }$ and $\{ C \} _ { 2 l + 1 , 2 l + 1 }$ respectively,and where $[ U _ { 3 } ^ { ( 0 ) } ] = [ U _ { 4 } ^ { ( 0 ) } ] = 0$ ,is obtained so that the $u _ { i }$ are of the form $\{ C \} _ { 2 l + 1 }$ and the $v _ { i }$ are of the form $\{ S \} _ { 2 l + 1 } ,$ if $\kappa _ { 1 }$ and $\kappa _ { 2 }$ are homogeneous polynomials in $\pmb { \varepsilon _ { 1 } ^ { 2 } }$ and $\pmb { \varepsilon _ { 2 } ^ { 2 } }$ and divisible by $\mu$

Similarly we can proceed for the determinant of $\delta _ { 2 } \xi _ { i } , \delta _ { 2 } \eta _ { i } , \delta _ { 3 } \xi _ { i }$ ， $\delta _ { 3 } \eta _ { i } , \ldots$ . Thus

$$
\xi _ { i } = \delta _ { 0 } \hat { \xi } _ { i } + \delta _ { 1 } \hat { \xi } _ { i } + \delta _ { 2 } \hat { \xi } _ { 2 } + \cdots , \qquad \eta _ { i } = \delta _ { 0 } \eta _ { i } + \delta _ { 1 } \eta _ { i } + \delta _ { 2 } \eta _ { i } + \cdot \cdot \cdot
$$

satisfy the equations (16).

The final solution for the Keplerian elements is expressed, similarly to the theory of Lindstedt,in the forms

$$
\begin{array} { r l r } & { } & { a _ { i } = \displaystyle \sum _ { i } A _ { i } ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \cos A , } \\ & { } & \\ { e _ { i } \cos g _ { i } = \displaystyle \sum _ { i } E _ { i } ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \cos A , \ } \\ & { } & \\ { e _ { i } \sin g _ { i } = \displaystyle \sum _ { i } E _ { i } ^ { \prime } ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \sin A , \ } \\ & { } & \\ { \eta ^ { 2 } = \displaystyle \sum _ { i } K ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \cos A , \ } \end{array}
$$

$$
\begin{array} { r l } & { \lambda _ { i } = n _ { i } t + c ^ { ( i ) } + \displaystyle \sum _ { j } G _ { i } ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \sin { A } , } \\ & { \theta _ { 1 } = \theta _ { 2 } = \sigma t + k + \displaystyle \sum _ { j = 1 } C ( \Lambda ^ { ( 1 ) } , \Lambda ^ { ( 2 ) } , J ) \mu ^ { l } \varepsilon _ { 1 } ^ { k _ { 1 } } \varepsilon _ { 2 } ^ { k _ { 2 } } \sin { A } , } \\ & { A = i _ { 1 } \lambda ^ { ( 1 ) } + i _ { 2 } \lambda ^ { ( 2 ) } + i _ { 1 } ^ { \prime } \lambda ^ { ( 1 ) } + i _ { 2 } ^ { \prime } \lambda ^ { ( 2 ) } , } \\ & { \lambda ^ { ( s ) } = n _ { s } t + c ^ { ( s ) } , \qquad \lambda ^ { \prime ( s ) } = n _ { s } ^ { \prime } t + c ^ { \prime ( s ) } \qquad ( s = 1 , 2 ) , } \\ & { k _ { s } = | i _ { s } ^ { \prime } | + \mathrm { a n e v e n \ i n t e g e r } , } \\ & { n _ { s } ^ { \prime } = n _ { s } ^ { \prime ( 0 ) } + n _ { s } ^ { \prime ( 0 ) } + \cdots + n _ { s } ^ { \prime ( 2 l ) } + \cdots , } \end{array}
$$

where $\theta _ { 1 }$ and $\theta _ { 2 }$ are the longitudes of the nodes and $\eta ^ { 2 } = \sin ^ { 2 } \left( I / 2 \right)$ ， and where $\pmb { \sigma }$ is expanded in positive powers of $\mu$ and of small arbitrary constants $\pmb { \varepsilon _ { 1 } ^ { 2 } }$ and $\varepsilon _ { 2 } ^ { 2 }$ ,and is divisible by $\mu$ ，provided that $i _ { 1 } ^ { \prime } \alpha _ { 1 } ^ { ( 1 ) } + i _ { 2 } ^ { \prime } \alpha _ { 2 } ^ { ( 1 ) } \neq 0$ for any integers $i _ { 1 } ^ { \prime }$ and $i _ { 2 } ^ { \prime }$ . Thus the coordinates are expressed in trigonometric series of four arguments linear in $t$ 、In order that the above discussion may hold, it is sufficient that the roots of the equation

$$
x ^ { 4 } - ( a _ { 1 1 } c _ { 1 1 } + 2 a _ { 1 2 } c _ { 1 2 } + a _ { 2 2 } c _ { 2 2 } ) x ^ { 2 } + | \ O { \ l } { a _ { 1 1 } } \quad { a _ { 1 2 } } | \ l | { c _ { 1 1 } } \quad { c _ { 1 2 } } | = 0
$$

should be real and unequal. The discussion,and hence the theory of Lindstedt, fails if $[ ( \Lambda ^ { ( 1 ) } + \Lambda ^ { ( 2 ) } ) ^ { 2 } - J ^ { 2 } ] ^ { 1 / 2 }$ is not small enough for a small value of the ratio of the semimajor axes,that is,if the orbital mutual inclination $I$ is greater than $3 9 ^ { \circ } 1 4 ^ { \prime }$ for Jupiter and Saturn.If the inclination is large enough, there may appear secular terms which would endanger the stability of the system by the presence of terms linear in $t$ ，The condition has been further studied by von Zeipel (1901),and recently by Kozai (Section 9.25).

Hill (1905) tried to obtain integrals of planetary motion suitable for an indefinite length of time.He considered the system Sun, Jupiter and Saturn moving in the same plane and referred to Gyldén's fundamental conception (Sections 10.18,10.19,10.20).He took an ideal problem in which the coefficients of various inequalities of the coordinates of the two planets relative to the sun are functions of two protometers of Gyldén and two constants indicating the deviation of the orbits from circular， the so-called diastematic functions.The modification of this ideal problem to the actual is determined by the method of variation of constants. Since Gyldén's theory,as has been shown, is unsatisfactory,so is this theory of Hill's.

Brumberg (1966) discussed the theory of planetary motion represented in purely trigonometric form. Two methods by using rectangular coordinates are suggested for the practical elaboration of such theory with the aid of digital computers.The first method is based on the use of an intermediary orbit according to Hill's lunar theory (see Chapter 11).The second method consists in determining the formal trigonometric series for the coordinates and substituting in the differential equations of the planetary motion，thus it is reduced to solving an infinite nonlinear algebraic system.The disturbing function is expanded by Tisserand-Lebeuf polynomials (Section 7.8)，which，he says,is simpler and more suitable for closer lunar satellities than expansion by ordinary methods.

# POINCARE'S THEORY

# 14.7POINCARE'S TRANSFORMATION

Take the canonical variables (Section 5.17)

$$
\beta \sqrt { \bar { a } } = X _ { 1 } , \qquad \beta ^ { \prime } \sqrt { \bar { a ^ { \prime } } } = X _ { 2 } , \qquad l = Y _ { 1 } , \qquad l ^ { \prime } = Y _ { 2 } ,
$$

$$
- \sqrt { 2 \beta \sqrt { a } \left( 1 - \sqrt { 1 - e ^ { 2 } } \right) } \cdot \sin \varpi = y _ { 1 } ,
$$

$$
- \sqrt { 2 \beta ^ { \prime } \sqrt { a ^ { \prime } } \left( 1 - \sqrt { 1 - e ^ { \prime 2 } } \right) } \cdot \sin \varpi ^ { \prime } = y _ { 2 } ,
$$

$$
\begin{array} { r l } & { ~ ^ { \prime } \overline { { 2 \beta \sqrt { a ( 1 - e ^ { 2 } ) } } } \cdot ( 1 - \cos I ) } \\ & { ~ - \sqrt { 2 \beta \sqrt { a ( 1 - e ^ { 2 } ) } \cdot ( 1 - \cos I ) } \cdot \sin \Omega = y _ { 3 } , } \\ & { ~ / \overline { { 2 \beta ^ { \prime } \sqrt { a ^ { \prime } ( 1 - e ^ { \prime 2 } ) } \cdot ( 1 - \cos I ^ { \prime } ) } } \cdot \cos \Omega ^ { \prime } = x _ { 4 } , } \\ & { ~ - \sqrt { 2 \beta ^ { \prime } \sqrt { a ^ { \prime } ( 1 - e ^ { \prime 2 } ) } \cdot ( 1 - \cos I ^ { \prime } ) } \cdot \sin \Omega ^ { \prime } = y _ { 4 } . } \end{array}
$$

and consider the canonical equations for the three-body problem

$$
\begin{array} { r l } { \frac { d X _ { i } } { d t } = \frac { \partial F } { \partial Y _ { i } } , } & { { } \quad \frac { d Y _ { i } } { d t } = - \frac { \partial F } { \partial X _ { i } } , } \\ { \frac { d x _ { i } } { d t } = \frac { \partial F } { \partial y _ { i } } , } & { { } \quad \frac { d y _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } } , } \end{array}
$$

where

$$
{ \cal F } = { \cal F } _ { 0 } + \mu { \cal F } _ { 1 } + \mu ^ { 2 } { \cal F } _ { 2 } + \cdots ,
$$

$\scriptstyle { F _ { 0 } }$ being independent of $\boldsymbol { Y } , \boldsymbol { x }$ and $y$ . The functions $F _ { 1 } , F _ { 2 } , \ldots$ depend on all the variables $X , Y , x$ and $y$ . They are periodic in $\pmb { Y }$ and are developable in powers of $x$ and $y$ . Denote the mean value of $F _ { 1 }$ with

respect to $\boldsymbol { Y } _ { \imath }$ and $Y _ { 2 }$ by $[ F _ { 1 } ]$ and put $[ F _ { 1 } ] = R$ ， then $\pmb R$ is expanded in powers of $x$ and $y$ ，

$$
R = R _ { 0 } + R _ { 2 } + R _ { 4 } + \cdots ,
$$

where $R _ { p }$ denotes the aggregate of terms of degree $p$ in $x$ and $y$

We propose to express our variables in functions of six constants $z _ { 1 } , z _ { 2 } , \rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 } , \rho _ { 4 }$ and of six arguments $w _ { 1 } , w _ { 2 } , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } , \omega _ { 4 } ,$ ，which are all linear functions of $t$ (Poincaré,1897).We shall see that the $w _ { i }$ vary rapidly while the $\omega _ { i }$ vary very slowly and that $\omega _ { 4 }$ reduces to a constant. Now

$$
\begin{array} { l l } { { \displaystyle X _ { i } = \sum _ { p } \mu ^ { p } X _ { i } ^ { \left( p \right) } , \ ~ } } & { { ~ Y _ { i } = \displaystyle \sum _ { p } \mu ^ { p } Y _ { i } ^ { \left( p \right) } , } } \\ { { \displaystyle x _ { i } = \sum _ { p } \mu ^ { p } x _ { i } ^ { \left( p \right) } , \ ~ } } & { { ~ y _ { i } = \displaystyle \sum _ { p } \mu ^ { p } y _ { i } ^ { \left( p \right) } , } } \end{array}
$$

and $X _ { i } ^ { \left( p \right) } , Y _ { i } ^ { \left( p \right) } , x _ { i } ^ { \left( p \right) } , y _ { i } ^ { \left( p \right) } , p > 0$ ，are functions of $w _ { i }$ developable in powers of

$$
\rho _ { k } \exp \{ \sqrt { - 1 } \omega _ { k } \} , \qquad \rho _ { k } \exp \{ - \sqrt { - 1 } \omega _ { k } \} .
$$

They also depend on the constants $z _ { i }$ in such a way that $X _ { i } ^ { ( 0 ) } = z _ { i }$ The functions $Y _ { i } ^ { \left( 0 \right) } - w _ { i } , x _ { i } ^ { \left( 0 \right) }$ ，and $y _ { i } ^ { ( 0 ) }$ are independent of $w$ and developable in powers of $\rho _ { k } \exp { \{ \sqrt { - 1 } \omega _ { k } \} }$ and $\bar { \rho } _ { k } \exp \left\{ - \sqrt { - 1 } \omega _ { k } \right\}$ If $\rho _ { i } = 0$ ，then $Y _ { i } ^ { \left( 0 \right) }$ reduces to $w _ { i }$ ，and $x _ { i } ^ { ( 0 ) } , y _ { i } ^ { ( 0 ) }$ reduce to zero.And $X _ { i } ^ { ( p ) } , Y _ { i } ^ { ( p ) }$ are periodic functions of $w$ . Denote the mean values by brackets.

The differences $X _ { i } ^ { \left( p \right) } - [ X _ { i } ^ { \left( p \right) } ] , Y _ { i } ^ { \left( p \right) } - [ Y _ { i } ^ { \left( p \right) } ]$ represent the shortperiod perturbation of order $p$ with respect to the masses.The mean values $[ X _ { i } ^ { ( p ) } ]$ represent the secular perturbation of order $p$ ，because they are independent of $w _ { i }$ but dependent only on $\omega _ { k }$ ， and hence they vary very slowly. The quantities themselves are of order $p$ but their variations are of order $p + 1$ .We see further that the $\rho _ { i }$ are of the order of the eccentricities and inclinations.Write the first-degree terms with respect to $\rho _ { i }$ in the expansions of $\boldsymbol { x } _ { k } ^ { ( 0 ) }$ and $y _ { k } ^ { ( 0 ) }$ as $u _ { k }$ and ${ \boldsymbol { v } } _ { \kappa }$ ， respectively.

The problem can be replaced by the following, namely, to determine the series (25) such that (i) the function $\pmb { F }$ is reduced,when the series (25)are substituted,to a function $\phi$ depending only on the constants $z _ { i }$ and $\rho _ { i }$ ，and (ii) the expressions

$$
d S = \sum _ { i } \left[ ( X _ { i } - z _ { i } ) d y _ { i } ^ { _ { 0 } } + ( Y _ { i } ^ { _ { 0 } } - Y _ { i } ) d z _ { i } \right]
$$

$$
\begin{array} { c } { { + \displaystyle \sum _ { k } ~ [ ( x _ { k } - x _ { k } ^ { ( 0 ) } ) d y _ { k } + ( y _ { k } ^ { ( 0 ) } - y _ { k } ) d x _ { k } ^ { ( 0 ) }  } } \\ { {  d T = \displaystyle \sum _ { k } ~ [ ( x _ { k } ^ { ( 0 ) } - u _ { k } ) d y _ { k } ^ { ( 0 ) } + ( w _ { k } - y _ { k } ^ { ( 0 ) } ) d u _ { k } ] } } \\ { {  + \displaystyle \sum _ { i } ~ ( w _ { i } - y _ { i } ^ { ( 0 ) } ) d z _ { i } ,  } } \\ { {  d U = \displaystyle \sum _ { k } ~ u _ { k } d v _ { k } + \sqrt { - 1 } \displaystyle \sum _ { k } ~ \rho _ { k } ^ { 2 } d \omega _ { k } , } } \end{array}
$$

are exact differentials.

In fact,if the three differentials are exact, then

$$
\sum _ { i } \ X _ { i } d Y _ { i } + \sum _ { i } \ x _ { i } d y _ { i } - \sum _ { i } \ z _ { i } d w _ { i } + { \sqrt { - 1 } } \sum _ { k } \rho _ { k } ^ { 2 } d \omega _ { k }
$$

is also an exact differential. Hence, if we transform the variables $z _ { i }$ $w _ { i } , \rho _ { k } ^ { 2 }$ ,and $- \sqrt { - 1 } \omega _ { k }$ as the new variables, then the original canonical equations keep their canonical form and become

$$
\begin{array} { r l } & { \frac { d z _ { i } } { d t } = \frac { \partial F } { \partial w _ { i } } = \frac { \partial \phi } { \partial w _ { i } } = 0 , \qquad z _ { i } = \mathrm { c o n s t a n t } , } \\ & { \frac { d \rho _ { k } } { d t } = - \frac { \partial \phi } { \sqrt { - 1 } \ \partial \omega _ { k } } = 0 , \quad \rho _ { k } = \mathrm { c o n s t a n t } , } \\ & { \frac { d w _ { i } } { d t } = - \frac { \partial \phi } { \partial z _ { i } } = \mathrm { c o n s t a n t } , } \\ & { \frac { d \omega _ { k } } { d t } = \frac { \partial \phi } { \sqrt { - 1 } \ \partial ( \rho _ { k } ^ { 2 } ) } = \mathrm { c o n s t a n t } . } \end{array}
$$

Hence the variables $z _ { i }$ and $\rho _ { \mathscr { k } } ^ { 2 }$ are constant, and $w _ { i }$ and $\omega _ { k }$ are linear functions of time.

When the expansions (25） are substituted in $\pmb { F }$ and arranged in powers of $\mu$ ，then we obtain

$$
\boldsymbol { F } = \boldsymbol { \Theta } _ { 0 } + \boldsymbol { \mu } \boldsymbol { \Theta } _ { 1 } + \boldsymbol { \mu } ^ { 2 } \boldsymbol { \Theta } _ { 2 } + \cdots .
$$

When the function $\phi$ is expanded similarly in powers of $\pmb { \mu }$ such that $\begin{array} { r } { \phi = \sum \mu ^ { p } \phi _ { p } } \end{array}$ ，then the equation $F = \phi$ gives

$$
\Theta _ { 0 } = \phi _ { 0 } , \qquad \Theta _ { 1 } = \phi _ { 1 } , \qquad \Theta _ { 2 } = \phi _ { 2 } ,
$$

$\Theta _ { 0 }$ is the expression $F _ { \mathfrak { d } }$ in which the $X _ { i }$ are replaced by $z _ { i }$ .Hence $\Theta _ { 0 } = \phi _ { 0 }$ is satisfied by itself. Similarly the principal function $s$ is developed as

$$
{ \cal S } = \mu S _ { 1 } + \mu ^ { 2 } S _ { 2 } + \cdots .
$$

At first we have from the terms factored by the first power of $\mu$

$$
d S _ { 1 } = \sum \ ( X _ { i } ^ { ( 1 ) } d Y _ { i } ^ { ( 0 ) } - Y _ { i } ^ { ( 1 ) } d z _ { i } + x _ { k } ^ { ( 1 ) } d y _ { k } ^ { ( 0 ) } - y _ { k } ^ { ( 1 ) } d x _ { k } ^ { ( 0 ) } ) .
$$

By our hypothesis $Y _ { i } ^ { \scriptscriptstyle { ( 0 ) } } - w _ { i } , z _ { i } , y _ { \scriptscriptstyle { k } } ^ { \scriptscriptstyle { ( 0 ) } } , x _ { \scriptscriptstyle { k } } ^ { \scriptscriptstyle { ( 0 ) } }$ are independent of $w _ { i }$ . Hence

$$
\begin{array} { r l } & { \frac { \partial Y _ { i } ^ { ( 0 ) } } { \partial w _ { i } } = 1 , \quad \frac { \partial Y _ { k } ^ { ( 0 ) } } { \partial w _ { i } } = 0 , } \\ & { \frac { \partial y _ { k } ^ { ( 0 ) } } { \partial w _ { i } } = 0 , \quad \frac { \partial x _ { k } ^ { ( 0 ) } } { \partial w _ { i } } = 0 \quad \quad ( k \neq i ) . } \end{array}
$$

Thus we obtain

$$
{ \frac { \partial S _ { 1 } } { \partial w _ { i } } } = X _ { i } ^ { ( 1 ) } .
$$

But the mean value of ${ \partial S _ { 1 } } / { \partial w _ { i } }$ ，which is the derivative of a periodic function, is zero,i.e., $[ X _ { i } ^ { ( 1 ) } ] = 0$ . The expression $[ X _ { i } ^ { ( 1 ) } ]$ represents the secular perturbation of $X _ { i }$ ,i.e.,of the semimajor axes,and this is of the second order of the disturbing mass.Thus we get Poisson's theorem on the invariability of the major axis up to the second order (Sections 8.7-8.10).

Since the $z _ { i }$ are considered to be constant， the derivatives $\partial \Theta _ { 0 } / \partial z _ { i }$ are constants and we have

$$
\Theta _ { 1 } = - \sum a _ { i } X _ { i } ^ { \scriptscriptstyle ( 1 ) } + F _ { 1 } , \qquad a _ { i } = - \frac { \partial \Theta _ { \scriptscriptstyle 0 } } { \partial z _ { i } } ,
$$

where $X _ { i } , Y _ { i } , x _ { i } , y _ { i }$ are replaced in $F _ { 1 }$ by $X _ { i } ^ { \left( 0 \right) } , Y _ { i } ^ { \left( 0 \right) } , x _ { i } ^ { \left( 0 \right) } , y _ { i } ^ { \left( 0 \right) }$ ， respectively. Taking the mean values we get

$$
[ \Theta _ { 1 } ] = - \sum a _ { i } [ X _ { i } ^ { \scriptscriptstyle ( 1 ) } ] + [ F _ { 1 } ] = R .
$$

Thus the mean value of the equation $\Theta _ { 1 } = \phi _ { 1 }$ becomes $R = \phi _ { 1 }$ By supposing $z _ { i }$ to be constant we have

$$
\begin{array} { r l } & { d T = \displaystyle \sum _ { k } \left[ \left( x _ { k } ^ { \scriptscriptstyle ( 0 ) } - u _ { k } \right) d y _ { k } ^ { \scriptscriptstyle ( 0 ) } + \left( v _ { k } - y _ { k } ^ { \scriptscriptstyle ( 0 ) } \right) d y _ { k } \right] , } \\ & { d U = \displaystyle \sum _ { k } u _ { k } d v _ { k } + \sqrt { - 1 } \sum _ { k } \rho _ { k } ^ { \scriptscriptstyle ^ 2 } d \omega _ { k } . } \end{array}
$$

We are to determine $x _ { k } ^ { ( 0 ) }$ and $y _ { k } ^ { ( 0 ) }$ so that they satisfy the equation $R = \phi _ { 1 }$ and so that these expressions for $d T$ and $d U$ are exact differentials.

In fact, the system of linear equations with constant coefficients

$$
\begin{array} { r } { \frac { d x _ { i } } { d t } = \frac { \partial R _ { 2 } } { \partial y _ { i } } , \frac { \partial y _ { i } } { d t } = - \frac { \partial R _ { 2 } } { \partial x _ { i } } \qquad ( i = 1 , 2 , 3 , 4 ) , } \end{array}
$$

admits the solution

$$
x _ { i } = \alpha _ { i } ^ { ( k ) } \exp { \{ \lambda _ { k } t \} } , \qquad y _ { i } = \beta _ { i } ^ { ( k ) } \exp { \{ \lambda _ { k } t \} } \qquad ( i = 1 , 2 , 3 , 4 ) .
$$

We have then

$$
\lambda _ { k } \alpha _ { i } ^ { ( k ) } = \frac { \partial R _ { 2 } } { \partial \beta _ { i } ^ { ( k ) } } , \qquad - \lambda _ { k } \beta _ { i } ^ { ( k ) } = \frac { \partial R _ { 2 } } { \partial \alpha _ { i } ^ { ( k ) } } \qquad ( i = 1 , 2 , 3 , 4 ) ,
$$

where $x _ { i }$ and $y _ { i }$ in $R _ { 2 }$ are replaced by ${ \alpha _ { i } ^ { ( k ) } }$ and $\beta _ { i } ^ { ( k ) }$ respectively. By eliminating ${ \alpha _ { i } ^ { ( k ) } }$ and $\beta _ { i } ^ { ( k ) }$ from these equations we obtain an equation in $\lambda _ { k }$ of degree eight,whose roots are arranged in pairs,which are equal in absolute value but of opposite sign. If the quadratic form $R _ { 2 }$ is positive-definite, then the roots $\lambda _ { k }$ will be pure imaginary， and $\lambda _ { k }$ and $- \lambda _ { k }$ will be conjugate imaginary. Let $\mu _ { k }$ be another root of the algebraic equation for $\lambda _ { k }$ ; then

$$
x _ { i } = \gamma _ { i } ^ { ( k ) } \exp { \{ \mu _ { k } t \} } , \qquad y _ { i } = \delta _ { i } ^ { ( k ) } \exp { \{ \mu _ { k } t \} }
$$

are the solution.Put

$$
\begin{array} { r } { \xi _ { i } = \alpha _ { i } ^ { ( k ) } \exp { \{ \lambda _ { k } t \} } , \qquad \eta _ { i } = \beta _ { i } ^ { ( k ) } \exp { \{ \lambda _ { k } t \} } , } \\ { \xi _ { i } ^ { \prime } = \gamma _ { i } ^ { ( k ) } \exp { \{ \mu _ { k } t \} } , \qquad \eta _ { i } ^ { \prime } = \delta _ { i } ^ { ( k ) } \exp { \{ \mu _ { k } t \} } . } \end{array}
$$

Then $x _ { i } = \xi _ { i } , y _ { i } = \eta _ { i }$ and $x _ { i } = \xi _ { i } ^ { \prime } , y _ { i } = \eta _ { i } ^ { \prime }$ are both solutions. Hence

$$
\sum \left( \xi _ { i } \eta _ { i } ^ { \prime } - \xi _ { i } ^ { \prime } \eta _ { i } \right) = \mathrm { c o n s t a n t } .
$$

Since the left-hand side is divisible by exp $\{ ( \lambda _ { k } + \mu _ { k } ) t \}$ , the right-hand member should be zero, unless we have $\mu _ { k } = - \lambda _ { k }$ .If $\mu _ { k } = - \lambda _ { k }$ ，then we set the constant equal to $+ 1$ . Let $a _ { i } ^ { ( k ) } , b _ { i } ^ { ( k ) }$ be the corresponding values of $\gamma _ { i } ^ { ( k ) } , \delta _ { i } ^ { ( k ) }$ for $\mu _ { k } = - \lambda _ { k }$ .If $\pmb { R } _ { 2 }$ is positive-definite， then ${ \alpha _ { i } ^ { ( k ) } }$ ， $\sqrt { - 1 } a _ { i } ^ { ( k ) }$ ，and $\beta _ { i } ^ { ( k ) } , \sqrt { - 1 } \ b _ { i } ^ { ( k ) }$ are conjugate imaginary. Put

$$
\begin{array} { l } { { \displaystyle x _ { i } = \sum _ { k } \alpha _ { i } ^ { ( k ) } x _ { k } ^ { \prime } + \sum _ { k } a _ { i } ^ { ( k ) } y _ { k } ^ { \prime } } , } \\ { { \displaystyle y _ { i } = \sum _ { k } \beta _ { i } ^ { ( k ) } x _ { k } ^ { \prime } + \sum _ { k } b _ { i } ^ { ( k ) } y _ { k } ^ { \prime } } , } \end{array}
$$

then we have

$$
\sum \ ( x _ { i } d y _ { i } - y _ { i } d x _ { i } ) = \sum \ ( x _ { k } ^ { \prime } d y _ { k } ^ { \prime } - y _ { k } ^ { \prime } d x _ { k } ^ { \prime } ) .
$$

Thus $\sum x d y - \sum x ^ { \prime } d y ^ { \prime }$ is an exact differential and the canonical equations conserve their canonical form, i.e.,

$$
\frac { d x _ { k } ^ { \prime } } { d t } = \frac { \partial R _ { 2 } } { \partial y _ { k } ^ { \prime } } , \qquad \frac { d y _ { k } ^ { \prime } } { d t } = - \frac { \partial R _ { 2 } } { \partial x _ { k } ^ { \prime } } ,
$$

$$
R _ { 2 } = \sum _ { k } \lambda _ { k } x _ { k } ^ { \prime } y _ { k } ^ { \prime } ,
$$

and the solution is

$$
x _ { k } ^ { \prime } = \exp { \{ \lambda _ { k } t \} } , \qquad y _ { k } ^ { \prime } = \exp { \{ - \lambda _ { k } t \} } .
$$

Now we have

$$
R = \Theta _ { 2 } + \Theta _ { 3 } + \cdots ,
$$

and

$$
\begin{array} { r } { \Theta _ { 2 } = \phi _ { 2 } , \qquad \Theta _ { 3 } = \phi _ { 3 } , } \end{array}
$$

Put

$$
\begin{array} { l } { { \displaystyle { u _ { i } = \sum _ { k } \alpha _ { i } ^ { ( k ) } \rho _ { k } \exp \left\{ \sqrt { - 1 } \omega _ { k } \right\} } } } \\ { { \displaystyle { - \sqrt { - 1 } \sum _ { k } a _ { i } ^ { ( k ) } \rho _ { k } \exp \left\{ - \sqrt { - 1 } \omega _ { k } \right\} } , } } \end{array}
$$

$$
\begin{array} { l } { { v _ { i } = \displaystyle \sum _ { k } \beta _ { i } ^ { ( k ) } \rho _ { k } \exp \left\{ \sqrt { - 1 } \omega _ { k } \right\} } } \\ { { \displaystyle ~ - \sqrt { - 1 } \sum _ { k } b _ { i } ^ { ( k ) } \rho _ { k } \exp \left\{ - \sqrt { - 1 } \omega _ { k } \right\} } , }  \end{array}
$$

then $\begin{array} { r } { \sum u _ { i } d v _ { i } + \sqrt { - 1 } \sum \rho _ { k } ^ { 2 } d \omega _ { k } } \end{array}$ is an exact differential and $\Theta _ { 2 } = R _ { 2 }$ $( u _ { i } , v _ { i } )$ reduces to $- \sqrt { - 1 } \sum \lambda _ { k } \rho _ { k } ^ { 2 }$ ，since $\begin{array} { r } { R _ { 2 } = \sum _ { k } \lambda _ { k } x _ { k } y _ { k } } \end{array}$ . Hence $\Theta _ { 2 } = \phi _ { 2 }$ is satisfied.

In the expression

$$
{ \cal S } = { \cal S } _ { 0 } + \mu { \cal S } _ { 1 } + \mu ^ { 2 } { \cal S } _ { 2 } + \cdots ,
$$

we have $S _ { 0 } = S _ { 1 } = S _ { 2 } = 0$ and we obtain

$$
d S _ { 3 } = \sum x _ { i } ^ { ( 2 ) } d v _ { i } - \sum y _ { i } ^ { ( 2 ) } d u _ { i } .
$$

On the other hand, we have

$$
\Theta _ { 3 } = \sum \left( \frac { \partial \Theta _ { 2 } } { \partial u _ { i } } x _ { i } ^ { \scriptscriptstyle ( 2 ) } + \frac { \partial \Theta _ { 2 } } { \partial v _ { i } } y _ { i } ^ { \scriptscriptstyle ( 2 ) } \right) + \Phi ,
$$

where $\Phi$ is a known function. Since

$$
x _ { i } ^ { \scriptscriptstyle ( 2 ) } = \frac { \partial S _ { 3 } } { \partial v _ { i } } , \qquad y _ { i } ^ { \scriptscriptstyle ( 2 ) } = - \frac { \partial S _ { 3 } } { \partial u _ { i } } ,
$$

the equation $\Theta _ { 3 } = \phi _ { 3 }$ reduces to

$$
\sum \left( \frac { \partial \Theta _ { 2 } } { \partial u _ { i } } \frac { \partial S _ { 3 } } { \partial v _ { i } } - \frac { \partial \Theta _ { 2 } } { \partial v _ { i } } \frac { \partial S _ { 3 } } { \partial u _ { i } } \right) = - \Phi + \phi _ { 3 } .
$$

But, since $\phi _ { 3 }$ depends only on $\phi$ ，we have

$$
\sum \left( \frac { \partial \Theta _ { 2 } } { \partial u _ { i } } \frac { \partial \phi _ { 3 } } { \partial v _ { i } } - \frac { \partial \Theta _ { 2 } } { \partial v _ { i } } \frac { \partial \phi _ { 3 } } { \partial u _ { i } } \right) = 0 ,
$$

where $\Theta _ { 2 }$ is a homogeneous quadratic form in $u _ { i }$ and $v _ { i }$ ，where $\Phi$ is a known homogeneous polynomial, and $S _ { 3 }$ and $\phi$ are unknown homo-geneous polynomials of the same degree as $\Phi$

By the above change of variables from $x _ { i } , y _ { i }$ to $x _ { i } ^ { \prime } , y _ { i } ^ { \prime }$ these equations are transformed to

$$
\begin{array} { r l } & { \displaystyle \sum _ { k } \lambda _ { k } \Big ( y _ { k } ^ { \prime } \frac { \partial S _ { 3 } } { \partial y _ { k } ^ { \prime } } - x _ { k } ^ { \prime } \frac { \partial S _ { 3 } } { \partial x _ { k } ^ { \prime } } \Big ) = - \Phi + \phi _ { 3 } , } \\ & { \displaystyle \sum _ { k } \lambda _ { k } \Big ( y _ { k } ^ { \prime } \frac { \partial \phi _ { 3 } } { \partial y _ { k } ^ { \prime } } - x _ { k } ^ { \prime } \frac { \partial \phi _ { 3 } } { \partial x _ { k } ^ { \prime } } \Big ) = 0 , } \end{array}
$$

where $\phi _ { 3 }$ is a homogeneous polynomial in the products $( x _ { k } ^ { \prime } y _ { k } ^ { \prime } )$ . Let

$$
\begin{array} { l } { { \Phi = \displaystyle \sum _ { { \bf \alpha } } { \cal A } x _ { 1 } ^ { \alpha _ { 1 } } y _ { 1 } ^ { \beta _ { 1 } } x _ { 2 } ^ { \alpha _ { 2 } } y _ { 2 } ^ { \beta _ { 2 } } { \bf \alpha } \cdot { \bf \mu } \cdot { \bf \sigma } , } } \\ { { { \cal S } _ { 3 } = \displaystyle \sum _ { { \bf \alpha } } { \cal B } x _ { 1 } ^ { \alpha _ { 1 } } y _ { 1 } ^ { \beta _ { 1 } } x _ { 2 } ^ { \alpha _ { 2 } } y _ { 2 } ^ { \beta _ { 2 } } { \bf \alpha } \cdot { \bf \sigma } \cdot { \bf \sigma } , } } \\ { { { \cal \phi } _ { 3 } = \displaystyle \sum _ { { \bf \alpha } } { \cal C } ( x _ { 1 } y _ { 1 } ) ^ { \alpha _ { 1 } } ( x _ { 2 } y _ { 2 } ) ^ { \alpha _ { 2 } } { \bf \alpha } \cdot { \bf \sigma } \cdot { \bf \sigma } \cdot { \bf \sigma } ; } } \end{array}
$$

then these equations are satisfied if we put

$$
B = \frac { A } { \sum \lambda _ { k } ( \alpha _ { k } - \beta _ { k } ) } ,
$$

provided that we do not have simultaneously $\alpha _ { 1 } = \beta _ { 1 } , \alpha _ { 2 } = \beta _ { 2 } , \ldots .$ They are satisfied if we put $C = A$ in the case $\alpha _ { 1 } = \beta _ { 1 } , \alpha _ { 2 } = \beta _ { 2 } , \ldots ,$ simultaneously. The solution is possible provided that the $\lambda _ { k }$ are not connected by any linear equation with integer coefficients. Hence $\boldsymbol { \mathscr { S } } _ { 3 }$ is known. Thus $\boldsymbol { x } _ { k } ^ { ( 0 ) }$ and $y _ { k } ^ { ( 0 ) }$ are expanded in powers of $\rho _ { k } \exp \{ \pm \sqrt { - 1 } \omega _ { k } \}$

When $_ { T }$ is known, we obtain the secular perturbation of the epoch by

$$
Y _ { i } ^ { \left( 0 \right) } = w _ { i } - \frac { \partial T } { \partial z _ { i } } .
$$

Thus the secular perturbation of the first order is obtained.

Next we determine the periodic perturbation of the first order. The equation $\Theta _ { 1 } = \phi _ { 1 }$ is written

$$
\sum a _ { i } \frac { \partial S _ { 1 } } { \partial w _ { i } } = F _ { 1 } - \phi _ { 1 } .
$$

The right-hand member is a periodic function of $w$ , whose mean value is zero, $[ F _ { 1 } - \phi _ { 1 } ] = 0$ ，since $R = \phi _ { 1 }$ . Hence the equation is written

$$
\begin{array} { r l r } & { } & { F _ { 1 } - \phi _ { 1 } = \displaystyle \sum _ { \mathrm { \Lambda } } A \cos { ( i _ { 1 } w _ { 1 } + \cdot \cdot \cdot + i _ { q } w _ { q } + D ) } , } \\ & { } & { S _ { 1 } = \displaystyle \sum _ { \mathrm { \Lambda } } B \sin { ( i _ { 1 } w _ { 1 } + \cdot \cdot \cdot + i _ { q } w _ { q } + E ) } , } \end{array}
$$

where $\pmb { A }$ and $D$ are given quantities and $\pmb { B }$ and $\pmb { F }$ are to be determined. If $i _ { 1 } a _ { 1 } + i _ { 2 } a _ { 2 } + \dotsb + i _ { q } a _ { q }$ is not zero,then the relations

$$
E = D , \qquad B = { \frac { A } { i _ { 1 } a _ { 1 } + \dots + i _ { q } a _ { q } } }
$$

solve the problem. Thus $S _ { 1 } - [ S _ { 1 } ]$ is determined. We get

$$
\begin{array} { r l r } { \mathbf { \Phi } _ { i } ^ { \mathsf { ^ { * } ( 1 ) } } - [ X _ { i } ^ { \mathrm { ^ { ( 1 ) } } } ] = \frac { \partial ( S _ { 1 } - [ S _ { 1 } ] ) } { \partial Y _ { i } ^ { \mathrm { ^ { ( 0 ) } } } } , } & { \quad Y _ { i } ^ { \mathrm { ( 1 ) } } - [ Y _ { i } ^ { \mathrm { ^ { ( 1 ) } } } ] = - \frac { \partial ( S _ { 1 } - [ S _ { 1 } ] ) } { \partial z _ { i } } , } \\ { \mathbf { \Phi } _ { x _ { k } ^ { \mathrm { ( 1 ) } } } - [ x _ { k } ^ { \mathrm { ^ { ( 1 ) } } } ] = \frac { \partial ( S _ { 1 } - [ S _ { 1 } ] ) } { \partial y _ { k } ^ { \mathrm { ^ { ( 0 ) } } } } , } & { \quad y _ { k } ^ { \mathrm { ^ { ( 1 ) } } } - [ y _ { k } ^ { \mathrm { ^ { ( 1 ) } } } ] = - \frac { \partial ( S _ { 1 } - [ S _ { 1 } ] ) } { \partial x _ { k } ^ { \mathrm { ^ { ( 0 ) } } } } , } \end{array}
$$

where $S _ { 1 } - [ S _ { 1 } ]$ is expressed as a function of $z _ { i } , Y _ { i } ^ { \scriptscriptstyle ( 0 ) } , x _ { k } ^ { \scriptscriptstyle ( 0 ) } , y _ { k } ^ { \scriptscriptstyle ( 0 ) }$ , but not of $z _ { i } , \rho _ { i } , { w _ { i } } , \omega _ { k }$ Thus, $Y _ { i } ^ { \left( 0 \right) }$ being equal to $w _ { i }$ plus a quantity independent of $w$ ，we have

$$
\frac { \partial S _ { 1 } } { \partial w _ { i } } = \frac { \partial S _ { 1 } } { \partial Y _ { i } ^ { \left( 0 \right) } } .
$$

Hence our equation can be replaced by

$$
\sum a _ { i } \frac { \partial S _ { 1 } } { \partial Y _ { i } ^ { ( 0 ) } } = F _ { 1 } - \phi _ { 1 } .
$$

Since any function periodic in $w _ { i }$ is also periodic in $Y _ { i } ^ { ( 0 ) }$ ，its mean value with respect to $Y _ { i } ^ { ( 0 ) }$ is the same as that with respect to $w _ { i }$

The next problem is to determine the secular perturbation of the second order,i.e., to determine $[ X _ { i } ^ { ( 1 ) } ] , [ Y _ { i } ^ { ( 1 ) } ] , [ x _ { k } ^ { ( 1 ) } ] , [ y _ { k } ^ { ( 1 ) } ]$ . We have

$$
\begin{array} { c } { { d S _ { 2 } = \displaystyle et { } { ' } \sum _ { i } \left( X _ { i } ^ { ( 2 ) } d Y _ { i } ^ { ( 0 ) } + X _ { i } ^ { ( 1 ) } d Y _ { i } ^ { ( 1 ) } - Y _ { i } ^ { ( 2 ) } d z _ { i } \right. } } \\ { { \nonumber ~ + ~ x _ { k } ^ { ( 2 ) } d y _ { k } ^ { ( 0 ) } - y _ { k } ^ { ( 2 ) } d x _ { k } ^ { ( 0 ) } + x _ { k } ^ { ( 1 ) } d y _ { k } ^ { ( 1 ) } ) . } } \end{array}
$$

Whence we obtain

$$
{ \frac { \partial S _ { 2 } } { \partial w _ { i } } } = X _ { i } ^ { \left( 2 \right) } + \sum \left( x _ { k } ^ { \left( 1 \right) } { \frac { \partial y _ { i } ^ { \left( k \right) } } { \partial w _ { i } } } + X _ { k } ^ { \left( i \right) } { \frac { \partial Y _ { k } ^ { \left( 1 \right) } } { \partial w _ { i } } } \right) .
$$

The mean value of the left-hand member is zero. The second term of the right-hand member is known, because we have, for example,

$$
\bigg [ x _ { k } ^ { ( 1 ) } \frac { \partial y _ { k } ^ { ( 1 ) } } { \partial w _ { i } } \bigg ] = \bigg [ \big ( x _ { k } ^ { ( 1 ) } - [ x _ { k } ^ { ( 1 ) } ] \big ) \frac { \partial } { \partial w _ { i } } ( y _ { k } - [ y _ { k } ^ { ( 1 ) } ] ) \bigg ] + [ x _ { k } ^ { ( 1 ) } ] \bigg [ \frac { \partial y _ { k } ^ { ( 1 ) } } { \partial w _ { i } } \bigg ] ,
$$

in which the frst term is known and the second term is zero.Hence $[ X _ { i } ^ { ( 2 ) } ]$ is known.

Taking the mean value of the equation $\Theta _ { 2 } = \phi _ { 2 }$ we get

$$
\sum \frac { \partial R } { \partial x _ { k } ^ { \scriptscriptstyle ( 0 ) } } [ x _ { k } ^ { \scriptscriptstyle ( 1 ) } ] + \sum \frac { \partial R } { \partial y _ { k } ^ { \scriptscriptstyle ( 0 ) } } [ y _ { k } ^ { \scriptscriptstyle ( 1 ) } ] = \Phi + \phi _ { 2 } .
$$

On the other hand

$$
d [ S _ { 1 } ] = \sum \ ( [ - Y _ { i } ^ { ( 1 ) } ] d z _ { i } + [ x _ { k } ^ { ( 1 ) } ] d y _ { k } ^ { ( 0 ) } - [ y _ { k } ^ { ( 1 ) } ] d x _ { k } ^ { ( 0 ) } ) ,
$$

or, by considering $z _ { i }$ to be constant,

$$
d [ S _ { 1 } ] = \sum \left( \left[ x _ { k } ^ { \left( 1 \right) } \right] d y _ { k } ^ { \left( 0 \right) } - \left[ y _ { k } ^ { \left( 1 \right) } \right] d x _ { k } ^ { \left( 0 \right) } \right) .
$$

Take $u _ { \kappa }$ and ${ \boldsymbol { v } } _ { \kappa }$ as the new variables in place of $x _ { k } ^ { ( 0 ) }$ and $y _ { k } ^ { ( 0 ) }$ . Any function developable in powers of $\boldsymbol { x } _ { k } ^ { ( 0 ) }$ and $y _ { k } ^ { ( 0 ) }$ is equally developable in powers of $u _ { \kappa }$ and ${ \boldsymbol { v } } _ { \kappa }$ . Then we find

$$
x _ { k } ^ { \scriptscriptstyle ( 0 ) } = u _ { k } + D _ { k } , \qquad y _ { k } ^ { \scriptscriptstyle ( 0 ) } = v _ { k } + C _ { k } ,
$$

$$
{ \frac { \partial R } { \partial x _ { k } ^ { ( 0 ) } } } = { \frac { \partial R } { \partial u _ { k } } } + A _ { k } , \qquad { \frac { \partial R } { \partial y _ { k } ^ { ( 0 ) } } } = { \frac { \partial R } { \partial v _ { k } } } + B _ { k } ,
$$

where $A _ { k } , B _ { k } , C _ { k } , D _ { k }$ are known functions developable in powers of $\boldsymbol { u } _ { k }$ and ${ \boldsymbol { v } } _ { k }$ beginning with the second-degree terms.Whence we obtain

$$
\sum _ { k } \left( \frac { \partial R } { \partial u _ { k } } [ x _ { k } ^ { ( 1 ) } ] + \frac { \partial R } { \partial v _ { k } } [ y _ { k } ^ { ( 1 ) } ] + A _ { k } [ x _ { k } ^ { ( 1 ) } ] + B _ { k } [ y _ { k } ^ { ( 1 ) } ] \right) = \Phi + \phi _ { 2 } ,
$$

$$
d [ S _ { 1 } ] = \sum \{ [ x _ { k } ^ { ( 1 ) } ] ( d v _ { k } + d C _ { k } ) + [ y _ { k } ^ { ( 1 ) } ] ( d u _ { k } + d D _ { k } ) \} .
$$

On the other hand, $\phi _ { 2 }$ ,being a function only of $\rho$ ，satisfies

$$
\frac { \partial \phi _ { 2 } } { \partial u _ { k } } \frac { \partial R _ { 2 } } { \partial v _ { k } } - \frac { \partial R _ { 2 } } { \partial u _ { k } } \frac { \partial \phi _ { 2 } } { \partial v _ { k } } = 0 .
$$

Put

$$
\begin{array} { c } { { \displaystyle { [ x _ { k } ^ { ( 1 ) } ] = \sum _ { p } \xi _ { k } ^ { ( p ) } , \qquad [ y _ { k } ^ { ( 1 ) } ] = \sum _ { p } \eta _ { k } ^ { ( p ) } } , } } \\ { { \displaystyle { \Phi = \sum _ { p } P _ { p } , \qquad \phi _ { 2 } = \sum _ { p } Q _ { p } , \qquad S = \sum _ { p } S _ { p } } , } } \end{array}
$$

and equate the terms of the first degree; then we obtain

$$
\sum \left( \frac { \partial R _ { 2 } } { \partial u _ { i } } \xi _ { i } ^ { \left( 0 \right) } + \frac { \partial R _ { 2 } } { \partial v _ { i } } \eta _ { i } ^ { \left( 0 \right) } \right) = P _ { 1 } - Q _ { 1 } ,
$$

$$
\sum { \left( \frac { \partial R _ { 2 } } { \partial u _ { i } } \frac { \partial Q _ { 1 } } { \partial v _ { i } } - \frac { \partial R _ { 2 } } { \partial v _ { i } } \frac { \partial Q _ { 1 } } { \partial u _ { i } } \right) } = 0 ,
$$

$$
d S _ { 1 } = \sum \ ( \xi _ { i } ^ { ( 0 ) } \ d v _ { i } - \eta _ { i } ^ { ( 0 ) } \ d u _ { i } ) ,
$$

$$
\xi _ { i } ^ { ( 0 ) } = \frac { \partial S _ { 1 } } { \partial v _ { i } } , \qquad \eta _ { i } ^ { ( 0 ) } = - \frac { \partial S _ { 1 } } { \partial u _ { i } } ,
$$

$$
\sum { \bigg ( } { \frac { \partial R _ { 2 } } { \partial u _ { i } } } { \frac { \partial S _ { 1 } } { \partial v _ { i } } } - { \frac { \partial R _ { 2 } } { \partial v _ { i } } } { \frac { \partial S _ { 1 } } { \partial u _ { i } } } { \bigg ) } = P _ { 1 } - Q _ { 1 } .
$$

Equating the terms of the second degree we obtain

$$
\sum \left( \frac { \partial R _ { 2 } } { \partial u _ { i } } \xi _ { i } ^ { \left( 1 \right) } + \frac { \partial R _ { 2 } } { \partial v _ { i } } \eta _ { i } ^ { \left( 1 \right) } \right) = \Phi - Q _ { 2 } ,
$$

$$
\sum { \left( \frac { \partial R _ { 2 } } { \partial u _ { i } } \frac { \partial Q _ { 2 } } { \partial v _ { i } } - \frac { \partial R _ { 2 } } { \partial v _ { i } } \frac { \partial Q _ { 2 } } { \partial u _ { i } } \right) } = 0 ,
$$

$$
d S _ { 2 } = \sum \ ( \pounds _ { i } ^ { \scriptscriptstyle ( 1 ) } d v _ { i } - \eta _ { i } ^ { \scriptscriptstyle ( 1 ) } d u _ { i } ) ,
$$

$$
\sum { \bigg ( } { \frac { \partial R _ { 2 } } { \partial u _ { i } } } { \frac { \partial S _ { 2 } } { \partial v _ { i } } } - { \frac { \partial R _ { 2 } } { \partial v _ { i } } } { \frac { \partial S _ { 2 } } { \partial u _ { i } } } { \bigg ) } = \Phi - Q _ { 2 } .
$$

The equation for $d S _ { z }$ gives

$$
d S _ { 2 } = \sum _ { i } { ( \xi _ { i } ^ { \scriptscriptstyle ( 1 ) } d v _ { i } - \eta _ { i } ^ { \scriptscriptstyle ( 1 ) } d u _ { i } ) } + \sum _ { i } { ( \xi _ { i } ^ { \scriptscriptstyle ( 0 ) } d C _ { i } - \eta _ { i } ^ { \scriptscriptstyle ( 0 ) } d D _ { i } ) } ,
$$

and hence

$$
\frac { \partial S _ { 2 } } { \partial v _ { i } } = \xi _ { i } ^ { ( 1 ) } + \Phi , \frac { \partial S _ { 2 } } { \partial u _ { i } } = - \eta _ { i } ^ { ( 1 ) } + \Phi .
$$

By the transformation from $x _ { k } , y _ { k }$ to $x _ { k } ^ { \prime } , y _ { k } ^ { \prime }$ ，which was described formally by

$$
\begin{array} { r l } & { u _ { i } = \displaystyle \sum _ { \mathrm { \scriptsize ~ \sum ~ } } \alpha _ { i } ^ { ( k ) } u _ { k } ^ { \prime } + \displaystyle \sum _ { \mathrm { \scriptsize ~ \sum ~ } } a _ { i } ^ { ( k ) } v _ { k } ^ { \prime } , } \\ & { v _ { i } = \displaystyle \sum _ { \mathrm { \scriptsize ~ \sum ~ } } \beta _ { i } ^ { ( k ) } u _ { k } ^ { \prime } + \displaystyle \sum _ { \mathrm { \scriptsize ~ \sum ~ } } b _ { i } ^ { ( k ) } v _ { k } ^ { \prime } , } \end{array}
$$

these equations are transformed to

$$
\begin{array} { r l } &  \displaystyle \sum _ { \lambda _ { k } \Big ( \boldsymbol { v } _ { k } ^ { \prime } \frac { \partial S } { \partial \boldsymbol { v } _ { k } ^ { \prime } } - \boldsymbol { u } _ { k } ^ { \prime } \frac { \partial S } { \partial \boldsymbol { u } _ { k } ^ { \prime } } \Big ) = P - Q , } \\ &  \displaystyle \sum _ { \lambda _ { k } \Big ( \boldsymbol { v } _ { k } ^ { \prime } \frac { \partial Q } { \partial \boldsymbol { v } _ { k } ^ { \prime } } - \boldsymbol { u } _ { k } ^ { \prime } \frac { \partial Q } { \partial \boldsymbol { u } _ { k } ^ { \prime } } \Big ) = 0 . } \end{array}
$$

The second equation shows that $\boldsymbol { Q }$ is an integral polynomial in the products $( u _ { \bar { \kappa } } ^ { \prime } v _ { \bar { \kappa } } ^ { \prime } )$ . Hence the first equation can be solved by the process cited above,provided that the $\lambda _ { k }$ are not connected by any linear relation with integer coefficients.Here $Q$ is zero if $p$ is odd.

Thus we can derive $[ S _ { 1 } ] , [ x _ { k } ^ { ( 1 ) } ] , [ y _ { k } ^ { ( 1 ) } ]$ in powers of $u _ { \kappa }$ and ${ \boldsymbol { v } } _ { \kappa }$ ; in other words, in powers of $\beta _ { k } \exp { \{ \pm \sqrt { - 1 } \omega _ { k } \} }$ . Then the equation

$$
[ Y _ { i } ^ { \scriptscriptstyle ( 1 ) } ] = - \frac { \partial [ S _ { 1 } ] } { \partial z _ { i } }
$$

gives $[ Y _ { i } ^ { ( 1 ) } ]$ . Thus the secular perturbation of the second order is determined.

The periodic perturbation of the second order is derived by $\Theta _ { 2 } = \phi _ { 2 }$ ， in which $x _ { k } ^ { ( 1 ) } , y _ { k } ^ { ( 1 ) }$ are known. It is written as

$$
\sum a _ { i } X _ { i } ^ { ( 2 ) } = \Phi - \phi _ { 2 } .
$$

We have,on the other hand,

$$
\frac { \partial S _ { 2 } } { \partial w _ { i } } = \stackrel { . } { X } _ { i } ^ { ( 2 ) } + \Phi .
$$

Hence we obtain

$$
\sum a _ { i } \frac { \partial S _ { 2 } } { \partial w _ { i } } = \Phi - \phi _ { 2 } .
$$

The right-hand member is a known function of $\pmb { w }$ and its mean value is zero,since we have just determined the secular perturbation of the second order so that the mean value vanishes. Hence the function $S _ { 2 } - [ S _ { 2 } ]$ can be determined by expanding $\Phi$ and $s$ in the form

$$
\begin{array} { c } { \Phi = \displaystyle \sum _ { } A \cos { ( i _ { 1 } w _ { 1 } + \cdot \cdot \cdot + i _ { q } w _ { q } + D ) } , } \\ { s = \displaystyle \sum _ { } B \sin { ( i _ { 1 } w _ { 1 } + \cdot \cdot \cdot + i _ { q } w _ { q } + E ) } , } \end{array}
$$

that is, by taking

$$
E = D , \quad \quad B = { \frac { A } { i _ { 1 } a _ { 1 } + \dots + i _ { q } a _ { q } } } ,
$$

provided that $i _ { 1 } a _ { 1 } + \dotsb + i _ { q } a _ { q }$ is not zero. Similarly we can determine $X _ { i } ^ { ( 2 ) } , Y _ { i } ^ { ( 2 ) } - [ Y _ { i } ^ { ( 2 ) } ] , x _ { k } ^ { ( 2 ) } - [ x _ { k } ^ { ( 2 ) } ] , y _ { k } ^ { ( 2 ) } - [ y _ { k } ^ { ( 2 ) } ] ,$ ,and so forth.

In the above procedure it has been assumed throughout that there is no linear homogeneous relation with integer coeficients among the $\lambda _ { k }$ . In the problem of three bodies there is certainly one value of $\lambda _ { k }$ which is zero.This is due to the existence of the integral of the total angular momentum. Poincaré succeeded in avoiding this difficulty by taking $F ^ { \prime } = F + U ^ { 2 } + V ^ { 2 }$ in place of $F$ as the Hamiltonian function, where $U , V , W$ are the components of the total angular momentum. Then none of the $\lambda _ { k }$ is zero,and the diffculty disappears. $U + { \sqrt { - 1 } } V$ can be expressed as an exponential, of which the exponent is a linear function of time and developable in powers of $\rho$ exp $\{ \pm \sqrt { - 1 } \omega \}$ Hence it should be divisible by

$$
\begin{array} { r l r } {  { \prod \ \rho _ { k } ^ { \alpha _ { k } + \beta _ { k } } \cdot \exp { \{ ( \alpha _ { k } - \beta _ { k } ) \sqrt { - 1 } \ \omega _ { k } \} } \cdot \exp { \{ \sqrt { - 1 } \ ( i _ { 1 } w _ { 1 } + i _ { 2 } w _ { 2 } ) \} } , } } \end{array}
$$

where $\alpha _ { k } , \beta _ { k } , i _ { k }$ are integers.The first-degree terms in the expansion of $U + { \sqrt { - 1 } } V$ in powers of $\boldsymbol { u }$ and $v$ reduce to $\rho _ { 4 } \exp { \{ \sqrt { - 1 } \omega _ { 4 } \} }$ factored by a constant. Hence $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = \beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } =$ $i _ { 1 } = i _ { 2 } = 0$ ， $\alpha _ { 4 } = 1$ ，and $U + { \sqrt { - 1 } } V$ is divisible by $\rho _ { 4 } \exp { \{ \sqrt { - 1 } \omega _ { 4 } \} }$ · Similarly $U - { \sqrt { - 1 } } V$ is divisible by $\rho _ { 4 } \exp \{ - \sqrt { - 1 } \stackrel { . } { \omega } _ { 4 } \}$ .The original equations with the Hamiltonian $\pmb { F }$ are reduced from the equations with the Hamiltonian $F ^ { \prime }$ by putting $U = V = 0$ , that is, $u _ { 4 } = v _ { 4 } = 0$ ， or $\rho _ { 4 } = 0$ . Thus they do not depend on the argument ${ \boldsymbol { \omega } } _ { 4 }$ . Hence the original equations with the Hamiltonian $\pmb { F }$ depend,not on six linear arguments $w _ { 1 } , w _ { 2 } , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } , \omega _ { 4 }$ ，but on five linear arguments $\displaystyle w _ { 1 } , w _ { 2 } , \omega _ { 1 } ,$ $\omega _ { 2 } , \omega _ { 3 }$ . Thus the coordinates of the three bodies are functions of five arguments $w _ { 1 } , w _ { 2 } , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 }$ and the mutual distances depend on four arguments,which are the differences of these five.

The linear arguments are expressed in the form

$$
w _ { i } = n _ { i } t + \varpi _ { i } , \qquad \omega _ { k } = \nu _ { k } t + \varepsilon _ { k } ,
$$

where $\varpi _ { i }$ and $\varepsilon _ { k }$ are arbitrary integration constants,and $n _ { i }$ and $\nu _ { k }$ are

constants such that

$$
\frac { d w _ { i } } { d t } = n _ { i } , \qquad \frac { d \omega _ { k } } { d t } = \nu _ { k } ,
$$

that is,

$$
n _ { i } = - \frac { \partial \phi } { \partial z _ { i } } , \qquad \nu _ { k } = \frac { \partial \phi } { \sqrt { - 1 } \partial ( \rho _ { k } ^ { 2 } ) } .
$$

Since $\phi$ is expanded in powers of $\pmb { \mu }$ and $\rho _ { \mathscr { k } } ^ { 2 }$ ，the derivatives $n _ { i }$ and $\nu _ { k }$ are also expanded in powers of $\mu$ and $\rho _ { \kappa } ^ { 2 }$ ，and the coefficients depend on $z _ { i }$ . It can be seen that $n _ { i }$ and $\nu _ { k }$ are real,and that the expansion of $n _ { i }$ in powers of $\mu$ begins with the terms independent of $\pmb { \mu }$ and the expansion of $\nu _ { k }$ in powers of $\pmb { \mu }$ begins with the terms factored by the first power of $\mu$ .Hence the $w _ { i }$ vary rapidly and the $\omega _ { k }$ slowly.Thus the terms depending only on $\omega _ { k }$ are called secular. $n _ { 1 }$ and $n _ { 2 }$ are called the mean mean motions.The $\nu _ { k }$ are of the order of the mean motions of the perihelia and the nodes.The squares of the constants $z _ { i }$ are assimilated to the mean semimajor axes. The $\rho _ { k }$ play a role analogous to the eccentricities and inclinations,and $\omega _ { k }$ the longitudes of the perihelia and nodes.

# 14.8VESSIOT'S TRANSFORMATION

Vessiot (1917, 1918) considered a canonical system

$$
\frac { d x _ { i } } { d t } = \frac { \partial F } { \partial y _ { i } } , \frac { d y _ { i } } { d t } = - \frac { \partial F } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

$$
{ \cal F } = { \cal F } _ { 0 } + \mu { \cal F } _ { 1 } + \mu ^ { 2 } { \cal F } _ { 2 } + \cdots .
$$

The variables $x _ { 1 } , \ldots , x _ { p }$ are proportional to the square roots of the major axes; $y _ { 1 } , \ldots , y _ { p }$ are mean longitudes; and $x _ { p + 1 } , \ldots , x _ { n } ;$ $y _ { p + 1 } , \ldots , y _ { n }$ are the eccentric and oblique variables. The function $\pmb { F }$ depends only on $x _ { 1 } , \ldots , x _ { p } ; F _ { 1 } , F _ { 2 } , \ldots .$ are integral power series in exp $\{ \pm \sqrt { - 1 } \ : y _ { 1 } \}$ ,...,exp{±√-1yp}; $x _ { p + 1 } , \ldots , x _ { n }$ $y _ { p + 1 } , \dotsc , y _ { n } ;$ ， whose coefficients are functions of $x _ { 1 } , \ldots , x _ { p }$

The integral

$$
\begin{array} { r l } & { x _ { i } = \phi _ { i } ( a _ { 1 } , \ldots , a _ { n } ; b _ { 1 } , \ldots , b _ { n } ; t ) , } \\ & { y _ { i } = \psi _ { i } ( a _ { 1 } , \ldots , a _ { n } ; b _ { 1 } , \ldots , b _ { n } ; t ) } \end{array}
$$

developed in powers of $\mu$ can be obtained by integrating an auxiliary canonical system

$$
\frac { d x _ { i } } { d t } = \frac { \partial H } { \partial y _ { i } } , \frac { d y _ { i } } { d t } = - \frac { \partial H } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

$$
H = H _ { 0 } + \frac { \mu } { 1 } H _ { 1 } + \frac { \mu ^ { 2 } } { 1 \cdot 2 } H _ { 2 } + \cdot \cdot \cdot ,
$$

with the initial condition that gives an elliptic motion

$$
x _ { i } = x _ { i } ^ { ( 0 ) } , \qquad y _ { i } = - \frac { \partial F _ { 0 } } { \partial x _ { i } ^ { ( 0 ) } } t + y _ { i } ^ { ( 0 ) } , \qquad x _ { p + h } = x _ { p + h } ^ { ( 0 ) } ,
$$

$$
y _ { p + h } = y _ { p + h } ^ { ( 0 ) } \qquad ( i = 1 , 2 , \ldots , p ; h = 1 , 2 , \ldots , n - p ) .
$$

The function $\pmb { H }$ developed in powers of $\mu$ is an integral of an auxiliary equation (Section 4.3)

$$
\frac { \partial H } { \partial t } + ( F , H ) = \frac { \partial F } { \partial \mu } ,
$$

which vanishes for $t = 0$

Let a bar on a symbol indicate that the variables $y _ { i }$ contained in it are replaced by

$$
y _ { i } = z _ { i } - \frac { \partial F _ { 0 } } { \partial x _ { i } } t \qquad ( i = 1 , 2 , \cdot \cdot \cdot , p ) ,
$$

and consider

$$
\overline { { H } } _ { k } = \int _ { 0 } ^ { t } \overline { { G } } _ { k + 1 } d t ,
$$

where

$$
\begin{array} { r } { \tilde { \mathfrak { r } } _ { k } = F _ { k } + \displaystyle \frac { k - 1 } { 1 } ( H _ { 0 } , F _ { k - 1 } ) + \frac { ( k - 1 ) ( k - 2 ) } { 1 \cdot 2 } ( H _ { 1 } , F _ { k - 2 } ) + \cdots } \\ { + \frac { k - 1 } { 1 } ( H _ { k - 1 } , F _ { 1 } ) } \end{array}
$$

We then have explicitly

$$
\begin{array} { l } { \displaystyle \overline { { H } } _ { 0 } = \int _ { 0 } ^ { t } \bar { F } _ { 1 } ( \tau ) d \tau , \quad \quad \displaystyle \overline { { H } } _ { 1 } = \int _ { 0 } ^ { t } \bar { F } _ { 2 } ( \tau ) d \tau + \int _ { 0 } ^ { t } d \tau ^ { \prime } \int _ { 0 } ^ { \tau ^ { \prime } } \big ( \bar { F } _ { 1 } ( \tau ) , \bar { F } _ { 1 } ( \tau ^ { \prime } ) \big ) } \\ { \displaystyle \quad \cdot \cdot \cdot , } \end{array}
$$

where the Poisson bracket operations are taken with respect to $x _ { 1 } , \dotsc , x _ { p } , x _ { p + 1 } , \dotsc , x _ { \pi } ; z _ { 1 } , \dotsc , z _ { p } , y _ { p + 1 } , \dotsc , y _ { \pi } .$

In order to calculate $x _ { i } , y _ { i }$ $( i = 1 , 2 , \ldots , n )$ , up to the terms in $\mu ^ { k }$ inclusive,it issuffcient toobtain $\overline { { H } } _ { 0 } , \overline { { H } } _ { 1 } , \dots , \overline { { H } } _ { k - 1 }$ by simple differentiation. For a general function $f ( x _ { 1 } , \ldots , x _ { n } ; y _ { 1 } , \ldots , y _ { n } )$ we see that

$$
f = \bar { f } + \frac { \mu } { 1 } \int _ { 0 } ^ { t } ( \overline { { F } } _ { 1 } ( \tau ) , \bar { f } ( t ) ) \ d \tau
$$

$$
\begin{array} { l } { { + \displaystyle \frac { \mu ^ { 2 } } { 1 \cdot 2 } \left\{ \int _ { 0 } ^ { t } ( \bar { F } _ { 2 } ( \tau ) , \bar { f } ( t ) ) d \tau + 2 \int _ { 0 } ^ { t } d \tau ^ { \prime } \int _ { 0 } ^ { \tau } \left( \bar { F } _ { 1 } ( \tau ) , ( \bar { F } _ { 1 } ( \tau ^ { \prime } ) , \bar { f } ( t ) ) \right) \right. } }  \\ { { + \ \cdot \cdot \cdot , } } \end{array}
$$

where on the right-hand side we should make

$$
\begin{array} { r l } & { ( i = 1 , 2 , \ldots , n ) ; \qquad z _ { i } = y _ { i } ^ { \scriptscriptstyle ( 0 ) } \qquad ( i = 1 , 2 , \ldots , p ) ; } \\ & { y _ { p + h } = y _ { p + h } ^ { \scriptscriptstyle ( 0 ) } \qquad ( h = 1 , 2 , \ldots , n - p ) . } \end{array}
$$

This method is very simple if we stop at the terms in $\mu ^ { 2 }$ .The successive change of variables is not necessary. By referring only to the Poisson brackets the transformation is canonical. Poisson's theorem on the invariability of the semimajor axes comes out as an immediate consequence.

Put, after Poincaré,

$$
\begin{array} { r l } & { u _ { k } = \sqrt { x _ { p + h } } \cdot \exp { \{ \sqrt { - 1 } \ y _ { p + h } \} } , } \\ & { v _ { k } = \sqrt { - x _ { p + h } } \cdot \exp { \{ - \sqrt { - 1 } \ y _ { p + h } \} } } \\ & { \qquad ( h = 1 , 2 , \ldots , n - p ) ; } \end{array}
$$

then $F _ { 1 } , F _ { 2 } , \ldots$ are developable in integral power series with respect to exp ${ \ L } \{ \pm \sqrt { - 1 } \ y _ { l } \} \ ( l = 1 , 2 , \ldots , p ) ; \ u _ { h } , v _ { h } \ ( h = 1 , 2 , \ldots , n - p ) .$ Denote by $[ f ]$ the mean value of a periodic function $f$ with respect to the mean longitudes $y _ { 1 } , \ldots , y _ { p }$ We have after Poincaré (1897)

$$
[ F _ { 1 } ] = R _ { 0 } + R , ~ R = R _ { 2 } + R _ { 3 } + \cdots ,
$$

where $\scriptstyle { R _ { m } }$ is homogeneous of degree m with respect to $u _ { h } , v _ { h }$ ，and with functions of $x _ { 1 } , \ldots , x _ { p }$ as the coefficients. Then we find

$$
\mathfrak { L } _ { 2 } = \sqrt { - 1 } \cdot \sum _ { h = 1 } ^ { n - p } c _ { h } u _ { h } v _ { h } , \qquad C = \sum _ { i = 1 } ^ { p } x _ { i } + \sqrt { - 1 } \cdot \sum _ { h = 1 } ^ { n - p } u _ { h } v _ { h } ,
$$

where $c$ is the integral of the angular momentum.

Consider a new set of canonical elements $x _ { 1 } ^ { \prime } , \ldots , x _ { n } ^ { \prime } ; y _ { 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$

$$
\begin{array} { c } { { x _ { i } ^ { \prime } = x _ { i } ^ { \left( 0 \right) } + \displaystyle \frac { \mu } { 1 } x _ { i } ^ { \left( 1 \right) } + \displaystyle \frac { \mu ^ { 2 } } { 1 \cdot 2 } x _ { i } ^ { \left( 2 \right) } + \cdots , } } \\ { { { } } } \\ { { y _ { i } ^ { \prime } = y _ { i } ^ { \left( 0 \right) } + \displaystyle \frac { \mu } { 1 } y _ { i } ^ { \left( 1 \right) } + \displaystyle \frac { \mu ^ { 2 } } { 1 \cdot 2 } y _ { i } ^ { \left( 2 \right) } + \cdots } } \\ { { { } } } \\ { { { \left( i = 1 , 2 , \ldots , n \right) } , } } \end{array}
$$

where the coefficients are periodic in $y _ { 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$ ，such that the variables $y _ { i }$ disappear from $\pmb { F }$ . This gives the solution $y _ { i } ^ { \prime } = - ( \partial F / \partial x _ { i } ^ { \prime } ) t \ +$ constant when we put $x _ { i } ^ { \prime } =$ constant.

Suppose that (26) is the solution of the auxiliary canonical system

$$
\begin{array} { c } { { \displaystyle \frac { d x _ { i } } { d t } = \frac { \partial H } { \partial y _ { i } } , \qquad \frac { d y _ { i } } { d t } = - \frac { \partial H } { \partial x _ { i } } \qquad ( i = 1 , 2 , \ldots , n ) , } } \\ { { \nonumber } } \\ { { H = H _ { 0 } + \frac { \mu } { 1 } H _ { 1 } + \frac { \mu ^ { 2 } } { 1 \cdot 2 } H _ { 2 } + \cdots . } } \end{array}
$$

It is necessary to calculate the coefficients $H _ { 0 } , H _ { 1 } , H _ { 2 } ,$ ... and the functions $x _ { i } ^ { ( 0 ) }$ and $y _ { i } ^ { ( 0 ) }$ as functions of $x _ { 1 } ^ { \prime } , \ldots , x _ { n } ^ { \prime } ; y _ { 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$ Then the series (26) can be obtained by an ordinary Taylor expansion.

Consider a canonical transformation (26a), to which the canonical transformation (26) reduces for $\mu = 0$ . This transformation (26a） is obtained by the substitution

$$
\begin{array} { r l } & { u _ { h } ^ { \prime } = \sqrt { x _ { p + h } ^ { \prime } } \cdot \exp { \{ \sqrt { - 1 } ~ y _ { p + h } ^ { \prime } \} } , } \\ & { v _ { h } ^ { \prime } = \sqrt { - x _ { p + h } ^ { \prime } } \cdot \exp { \{ - \sqrt { - 1 } ~ y _ { p + h } ^ { \prime } \} } \qquad ( h = 1 , 2 , \dots , n - p ) , } \end{array}
$$

in a general transformation $\left( \Theta \right)$ defined by the symbol $e ^ { ( \Theta , f ) }$ of a one-parameter canonical group (Section 12.24). The unknown function is

$$
\Theta = \Theta _ { 3 } + \Theta _ { 4 } + \cdots ,
$$

in terms of the variables $x _ { 1 } , \dotsc , x _ { p } ; u _ { 1 } , \dotsc , u _ { n - p } ; v _ { 1 } , \dotsc , v _ { n - p } .$ expanded in the same form as $\pmb R$ . This function is defined so that the transformation $\left( \Theta \right)$ transforms $\pmb R$ into a function of $x _ { 1 } ^ { \prime } , \ldots , x _ { n } ^ { \prime }$ only, that is,by omitting the primes attached,

$$
\begin{array} { l } { { { \displaystyle R = \frac { 1 } { 1 } ( \Theta , R ) _ { u , v } + \frac { 1 } { 1 \cdot 2 } ( \Theta , ( \Theta , R ) ) _ { u , v } + \cdots } } } \\ { { { \displaystyle \quad \equiv R _ { 2 } + [ ( \Theta _ { 3 } , R _ { 2 } ) _ { u , v } + R _ { 3 } ] + \cdots + [ ( \Theta _ { m } , R _ { 2 } ) _ { u , v } + S _ { m } ] + \cdot \cdot \cdot } } } \end{array}
$$

where $S _ { m }$ is a function of $\scriptstyle { R _ { k } }$ and of $\Theta _ { 3 } , \ldots , \Theta _ { m - 1 }$ through Poisson's brackets. The terms of the right-hand member are grouped according to the degree with respect to $u _ { n }$ and $v _ { h }$ .Hence we obtain the conditions

$$
( \Theta _ { m } , R _ { 2 } ) _ { u , v } + S _ { m } = \bar { S } _ { m } , \qquad ( S _ { 3 } = R _ { 3 } ) ,
$$

where $\bar { S } _ { m }$ denotes the mean value of a periodic function $S _ { m }$ of $y _ { p + 1 } , \ldots , y _ { n }$ . These equations determine the unknown functions $\Theta _ { m }$ Further,by the condition $( C , \Theta ) = 0$ the transformation $\left( \Theta \right)$ leaves the integral $C$ invariant.

The result of the transformation (26) on $F$ is, by omitting the upper indices of $x _ { k } ^ { ( 0 ) } , y _ { k } ^ { ( 0 ) }$ and arranging in powers of $\mu$ ，

$$
F _ { 0 } + \frac { \mu } { 1 } \Phi _ { 1 } + \frac { \mu ^ { 2 } } { 1 \cdot 2 } \Phi _ { 2 } + \cdot \cdot \cdot .
$$

The coefficients are obtained by repeated applications of the operation $( \partial f / \partial \mu ) + ( H , f )$ on $\boldsymbol { F } _ { 1 }$ in place of $f$ .Thus we obtain

$$
\Phi _ { 1 } = ( H _ { 0 } , F _ { 0 } ) + F _ { 1 } , \qquad \Phi _ { k + 1 } = ( H _ { k } , F _ { 0 } ) + D _ { k + 1 } ,
$$

$$
\begin{array} { l } { { D _ { k + 1 } = ( k + 1 ) ( H _ { k - 1 } , F _ { 1 } ) + k ( H _ { 0 } , ( H _ { k - 1 } , F _ { 0 } ) ) } } \\ { { \mathrm { } + ( H _ { k - 1 } , ( H _ { 0 } , F _ { 0 } ) ) + G _ { k } , } } \end{array}
$$

where the $G _ { k }$ are expressed in terms of $F _ { \circ } , F _ { \scriptscriptstyle 1 } , F _ { \scriptscriptstyle 2 } , \ldots , F _ { k + 1 } ; H _ { \scriptscriptstyle 0 } , H _ { \scriptscriptstyle 1 } ,$ $\ldots , H _ { k - 2 }$ by means of the Poisson brackets.Hence these formulas are independent of the canonical variables employed. The functions $H _ { k }$ should satisfy the conditions that the $\Phi _ { \kappa }$ are independent of $y _ { 1 } , \ldots , y _ { p }$ as expressed in terms of $x , y$ ,i.e., the $\Phi _ { k }$ are equal to their respective mean values $[ \Phi _ { k } ]$ ，and that the $H _ { k }$ should be independent of $y _ { p + 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$ as expressed in terms of $x ^ { \prime } , y ^ { \prime }$ ,i.e., the $[ \Phi _ { k } ]$ are equal to their respective mean values $[ \overline { { \Phi } } _ { k } ]$ . Thus we obtain

$$
( H _ { 0 } , F _ { 0 } ) _ { x , y } + F _ { 1 } = [ F _ { 1 } ] , \qquad [ F _ { 1 } ] = [ \bar { F } _ { 1 } ]
$$

in terms of $x ^ { \prime } , y ^ { \prime }$ . The first equation gives $H _ { 0 } - [ H _ { 0 } ]$ . The second equation is an identity by the choice of the variables $x ^ { \prime } , y ^ { \prime }$ . In general we obtain

$$
( H _ { k } , F _ { 0 } ) _ { x , y } + D _ { k + 1 } = [ D _ { k + 1 } ] , \qquad [ D _ { k + 1 } ] = [ \bar { D } _ { k + 1 } ] ,
$$

in terms of $x ^ { \prime } , y ^ { \prime }$ . The first equation gives $H _ { k } \mathrm { ~ - ~ } [ H _ { k } ]$ when $H _ { 0 } , \ldots ,$ $H _ { k - 1 }$ are known. In the second equation the mean value $[ H _ { \kappa - 1 } ]$ enters only in the term $( k + 1 ) ( H _ { k - 1 } , F _ { 1 } )$ . We form

$$
( [ H _ { k - 1 } ] , R ) _ { u ^ { \prime } , v ^ { \prime } } + \Delta _ { k + 1 } = \overline { { \Delta } } _ { k + 1 } ,
$$

where $\Delta _ { k + 1 }$ depends only on $H _ { 0 } , H _ { 1 } , \dots , H _ { k - 2 }$ and $H _ { k - 1 } - [ H _ { k - 1 } ]$ When these functions are known, the second equation gives $[ H _ { k - 1 } ]$ developed in homogeneous powers of $u ^ { \prime } , v ^ { \prime }$ ，in a manner similar to the calculation of $\Theta$ . If further the condition $( C , H ) = 0$ is imposed, then the transformation (26) leaves the form of the integral $C$ invariant.

# BOHLIN'S THEORY

14.9POINCARE'S FORMULATION OF LINDSTEDT'S THEORY

Consider the equations for the three-body problem in Poincaré's form (Section 5.17)