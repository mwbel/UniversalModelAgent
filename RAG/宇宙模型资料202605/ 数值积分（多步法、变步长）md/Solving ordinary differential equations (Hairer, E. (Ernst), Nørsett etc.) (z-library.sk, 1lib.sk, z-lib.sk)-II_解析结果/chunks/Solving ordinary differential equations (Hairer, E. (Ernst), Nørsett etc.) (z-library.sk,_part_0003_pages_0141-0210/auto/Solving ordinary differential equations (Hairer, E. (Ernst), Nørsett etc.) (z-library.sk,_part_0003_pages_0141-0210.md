for step size prediction. This requires one additional function evaluation, but satisfies $\widetilde { e r r }  0$ for $h \lambda  \infty$ ,as does the error of the numerical solution.

Standard Step Size Controller. Since the expressions (8.19) and (8.2O) behave like $\mathcal { O } ( h ^ { 4 } )$ for $h  0$ , the standard step size prediction leads to

$$
h _ { \mathrm { n e w } } = f a c \cdot h _ { \mathrm { o l d } } \cdot \lvert \lvert e r r \rvert \rvert ^ { - 1 / 4 } .
$$

where

$$
\left| \left| e r r \right| \right| = \sqrt { \frac { 1 } { n } \sum _ { \ i = 1 } ^ { n } \Bigl ( \frac { e r r _ { i } } { s c _ { \ i } } \Bigr ) ^ { 2 } } ,
$$

and $s c _ { \ i } = A t o l _ { \ i } + \operatorname* { m a x } ( | y _ { 0 \ i } | , | y _ { 1 \ i } | ) \cdot R t o l _ { \ i }$ as in (4.11) of Sect.II.4. Here, the safety factor fac is proposed to depend on $N e w t$ , the number of Newton iterations of the current step and on the maximal number of Newton iterations $k _ { \mathrm { m a x } }$ ,say, as: $f a c = 0 . 9 \times ( 2 k _ { \operatorname* { m a x } } + 1 ) / ( 2 k _ { \operatorname* { m a x } } + N e w t ) .$

In order to save LU-decompositions of the matrix (8.14),we also include the following strategy: if no Jacobian is recomputed and if the step size $h _ { \mathrm { n e w } }$ , defined by (8.21), satisfies

$$
c _ { 1 } h _ { \mathrm { o l d } } \leq h _ { \mathrm { n e w } } \leq c _ { 2 } h _ { \mathrm { o l d } }
$$

with, say $c _ { 1 } = 1 . 0$ and $c _ { 2 } = 1 . 2$ , then we retain $h _ { \mathrm { o l d } }$ for the following step.

Predictive Controller The step size prediction by formula (8.21) has the disadvan-tage that step size reductions by more than the factor fac are not possible without step rejections (observe that $h _ { \mathrm { n e w } } < f a c \cdot h _ { \mathrm { o l d } }$ implies $\left\| e r r \right\| > 1 )$ . For stiff differential equations, however, a rapid decrease of the step size is often required (see for example the situation of Fig.8.1, where the step size drops from $1 0 ^ { - 2 }$ to $1 0 ^ { - 7 }$ within a very small time interval). Denoting by $e r r _ { n + 1 }$ the error expression (8.19) (or (8.20))，, computed in the $\mathscr { n }$ th step with step size $h _ { n }$ ， step size predictions are typically derived from the asymptotic formula

$$
\| e r r _ { n + 1 } \| = C _ { n } h _ { n } ^ { 4 } .
$$

The strategy (8.21) is based on the additional assumption $C _ { n + 1 } \approx C _ { n }$ ， which, as we have seen, is not always very realistic.

A careful control-theoretic study of step size strategies has been undertaken by Gustafsson (1994). He came to the conclusion that a better model is to assume that $\log C _ { n }$ is a linear function of $\mathscr { n }$ . This means that $\log C _ { n + 1 } - \log C _ { n }$ is constant or, equivalently,

$$
C _ { n + 1 } / C _ { n } \approx C _ { n } / C _ { n - 1 } .
$$

Inserting $C _ { n }$ and $C _ { n - 1 }$ from (8.23) and $C _ { n + 1 }$ from $1 = C _ { n + 1 } h _ { \mathrm { n e w } } ^ { 4 }$ into (8.24) yields

$$
h _ { \mathrm { n e w } } = f a c \cdot h _ { n } \bigg ( \frac { 1 } { \| e r r _ { n + 1 } \| } \bigg ) ^ { 1 / 4 } \cdot \frac { h _ { n } } { h _ { n - 1 } } \bigg ( \frac { \| e r r _ { n } \| } { \| e r r _ { n + 1 } \| } \bigg ) ^ { 1 / 4 } .
$$

![](images/a34acc3688c9c236807cdc429aaec0e6d70a277e063eab770d1be544ea4411b3.jpg)  
Fig.8.1. Solution, step sizes and Newton iterations for RADAU5

In our code RADAU5 we take the minimum of the two step sizes (8.21) and (8.25). For the problem considered in Fig.8.1, this new strategy reduces the number of rejected steps from 27 to 7.

Numerical Study of the Step-Control Mechanism. As a representative example we choose the van der Pol equation $( 1 . 5 )$ with $\varepsilon = 1 0 ^ { - 6 }$ , initial values $y _ { 1 } ( 0 ) = 2$ ， $y _ { 2 } ( 0 ) = - 0 . 6$ and integration interval $0 \leq x \leq 2$ . Fig.8.1 shows four pictures. The first one presents the solution $y _ { 1 } ( x )$ with all accepted integration steps for $A t o l = R t o l = 1 0 ^ { - 4 }$ . Below this, the step sizes obtained by RADAU5 are plotted as function of $_ x$ . The solid line represents the accepted steps. The rejected steps are indicated by $\times \mathit { \textbf { s } }$ . Observe the very small step sizes which are required in the rapid transients between the smooth parts of the solution. The lowest two pictures give the number of Newton iterations needed for solving the nonlinear system (8.2a), once as function of $_ x$ ，and once as function of the step-number. The last picture also indicates the steps where the Jacobian has been recomputed.

Another numerical experiment (Fig.8.2) illustrates the quality of the error es-timates. We applied the code RADAU5 with $A t o l = R t o l = 1 0 ^ { - 4 }$ and initial step size $h = 1 0 ^ { - 4 }$ to the above problem and plotted at several chosen points of the numerical solution

a） the exact local error (marked by small circles) b) the estimates (8.19) and (8.20) (marked by $\phi$ and X respectively)

![](images/c1288d1775b4a9653e848870d6ad471e07218049aae9f0e7cb2dc0c334c0e37d.jpg)  
Fig.8.2. Exact local error and the estimates (8.19) and (8.20)

as functions of $h$ . The large symbols indicate the position of the actually used step size. Newt is the number of required Newton iterations.

It is interesting to note that the local error behaves like $\mathcal { O } ( h ^ { 6 } )$ (straight line of slope 6) only for $h \leq \varepsilon$ and for large $h$ . Between these regions, the local error grows like $\mathcal { O } ( h ^ { - 1 } )$ with decreasing $h$ . This is the only region where the error estimate (8.20) is significantly better than (8.19). Therefore,we use the more expensive estimator (8.2O) only in the first and after each rejected step. In any way,both error estimators are always above the actual local error, so that the code usually produces very precise results.

# Implicit Differential Equations

Many applications (such as space discretizations of parabolic differential equations) often lead to systems of the form

$$
M y ^ { \prime } = f ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 }
$$

with a constant matrix $M$ . For such problems we formally replace all $f$ 's by $M ^ { - 1 } f$ and multiply the resulting equations by $M$ .Formulas (8.13) and (8.19) then have to be replaced by

$$
\left( h ^ { - 1 } \Lambda \otimes M - I \otimes J \right) \Delta W ^ { k } = - h ^ { - 1 } \left( \Lambda \otimes M \right) W ^ { k } + ( T ^ { - 1 } \otimes I ) F ( ( T \otimes I ) W ^ { k } )
$$

$$
e r r = \left( ( h \gamma _ { 0 } ) ^ { - 1 } M - J \right) ^ { - 1 } \left( f ( x _ { 0 } , y _ { 0 } ) + ( h \gamma _ { 0 } ) ^ { - 1 } M ( e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } ) \right) .
$$

Here the matrix $J$ is again an approximation to $\partial f / \partial y$ . These formulas may even be applied to certain problems (8.26) with singular $M$ (for more details see Chapters VI and VII).

Solving the linear system (8.13a) is done by a decomposition of the matrix (see (8.14), (8.14'))

$$
\left( \begin{array} { c c } { { \gamma M - J } } & { { 0 } } \\ { { 0 } } & { { ( \alpha + i \beta ) M - J } } \end{array} \right) .
$$

If $M$ and $J$ are banded or sparse, the matrices $\gamma M - J$ and $( \alpha + \imath \beta ) M - J$ remain banded or sparse, respectively. The code RADAU5 of the appendix has options for banded structures.

# An SDIRK-Code

We have also coded,using many of the above ideas,the SDIRK formula (6.16) together with the global solution (6.17). For this method also, it was again very important to replace the error estimator $y _ { 1 } - { \widehat { y } } _ { 1 }$ by (8.19).

Here, in contrast to fully implicit Runge-Kutta methods, one can treat the stages one after the other. Such a serial computation has the advantage that the information of the already computed stages can be used for a good choice of the starting values for the Newton iterations in the subsequent stages. For example, suppose that

$$
\begin{array} { l } { z _ { 1 } = \gamma h f ( x _ { 0 } + \gamma h , y _ { 0 } + z _ { 1 } ) } \\ { z _ { 2 } = \gamma h f ( x _ { 0 } + c _ { 2 } h , y _ { 0 } + z _ { 2 } ) + a _ { 2 1 } h f ( x _ { 0 } + \gamma h , y _ { 0 } + z _ { 1 } ) } \end{array}
$$

are already available. Since for all $i$

$$
z _ { i } = c _ { i } h f ( x _ { 0 } , y _ { 0 } ) + ( \sum _ { \jmath } a _ { i \jmath } c _ { j } ) h ^ { 2 } ( f _ { x } + f _ { y } f ) ( x _ { 0 } , y _ { 0 } ) + \mathcal { O } ( h ^ { 3 } ) ,
$$

by solving

$$
\left( { \begin{array} { c c } { c _ { 1 } } & { c _ { 2 } } \\ { \sum _ { j } a _ { 1 j } c _ { j } } & { \sum _ { j } a _ { 2 j } c _ { j } } \end{array} } \right) { \binom { \alpha _ { 1 } } { \alpha _ { 2 } } } = \left( { \begin{array} { c c } { c _ { 3 } } \\ { \sum _ { j } a _ { 3 j } c _ { j } } \end{array} } \right)
$$

one finds $\alpha _ { 1 } , \alpha _ { 2 }$ such that

$$
\alpha _ { 1 } z _ { 1 } + \alpha _ { 2 } z _ { 2 } = z _ { 3 } + \mathcal { O } ( h ^ { 3 } ) .
$$

The expression $z _ { 3 } ^ { ( 0 ) } = \alpha _ { 1 } z _ { 1 } + \alpha _ { 2 } z _ { 2 }$ then serves as starting value for the computation of $z _ { 3 }$ . In the last stage one can take $\widehat { y } _ { 1 }$ ，which is then available, for starting the Newton iterations for $g _ { s } = y _ { 1 }$ .The computation of $z _ { 3 } , z _ { 4 } , y _ { 1 }$ ，done in this way, needs few Newton iterations and a failure of convergence is usually already detected in the first stage.

However, when parallel processors are available, the exploitation of the triangular structure of the Runge-Kutta matrix may be less desirable. Whereas in the iteration (8.13） all $s$ function evaluations and much of the linear algebra can be done in parallel, this is no longer possible for DIRK-methods, when $z _ { 1 } , \dots , z _ { k }$ is used in the computations of $z _ { k + 1 }$

# SIRK-Methods

The fact that singly-implicit methods have a coeficient matrix with a one-point spectrum is the key to reducing the operation count for these methods to the level which prevails in linear multistep methods.

(J.C.Butcher, K. Burrage & FH. Chipman 1980)

In order to avoid the difficulties (in writing a Runge-Kutta code) caused by the com-plex eigenvalues of the Runge-Kutta matrix $A$ , one may look for methods with real eigenvalues, especially with a single $s$ -fold real eigenvalue. Such methods were introduced by Ngrsett (1976). Burrage (1978) provided them with error estimators, and codes in ALGOL and FORTRAN are presented in Butcher, Burrage & Chipman (1980). The basic methods for their code STRIDE are given by the following lemma.

Lemma 8.1. For collocation methods (i.e., for Runge-Kuta methods satisfying condition $C ( s )$ of Sect. IV.5), we have

$$
\operatorname* { d e t } ( I - z A ) = ( 1 - \gamma z ) ^ { s } ,
$$

if and only if

$$
c _ { \iota } = \gamma x _ { \iota } , \qquad i = 1 , \ldots , s ,
$$

where $x _ { 1 } , \dots , x _ { s }$ are the zeros of the Laguerre polynomial $L _ { s } ( x )$ $( c . f .$ Formula (6.11)).

Proof. The polynomial $\operatorname* { d e t } ( I - z A )$ is the denominator of the stability function (Formula (3.3)), so that by Theorem 3.10

$$
M ^ { ( s ) } ( 0 ) + M ^ { ( s - 1 ) } ( 0 ) z + \ldots + M ( 0 ) z ^ { s } = ( 1 - \gamma z ) ^ { s }
$$

with $M ( x )$ given by (3.25). Computing $M ^ { ( j ) } ( 0 )$ from (8.30) we obtain

$$
\frac { 1 } { s ! } \prod _ { i = 1 } ^ { s } ( x - c _ { i } ) = M ( x ) = \sum _ { \jmath = 0 } ^ { s } { \binom { s } { \jmath } } ( - \gamma ) ^ { s - \jmath } \frac { x ^ { \jmath } } { \jmath ! } = ( - \gamma ) ^ { s } L _ { s } ( \frac { x } { \gamma } )
$$

which leads to (8.29).

The stability function of the method of Lemma 8.1 has been studied in Sections IV.4 (multiple real-pole approximations) and IV.6. We have further seen (Proposition 3.8) that $R ( \infty ) = 0$ when $x _ { 0 } + h$ is a collocation point. This means that $c _ { q } = 1$ or $\gamma = 1 / x _ { q }$ for $q \in \{ 1 , \ldots , s \}$ where $0 < x _ { 1 } < . . . < x _ { s }$ are the zeros of $L _ { s } ( x ) ^ { \dagger }$ . However, if we want $A$ -stable methods, Theorem 4.25 restricts this point to be in the middle (more precisely: $q = s / 2$ or $s / 2 + 1$ for $s$ even, $q = ( s + 1 ) / 2$ for $s$ odd).An apparently undesirable consequence of this is that many of the collocation points lie outside the integration interval (for example, for $s \approx 5$ and $q = 3$ we have $c _ { 1 } = 0 . 0 7 3$ ， $c _ { 2 } = 0 . 3 9 3$ ， $c _ { 3 } = 1$ ， $c _ { 4 } = 1 . 9 7 0$ ， $c _ { 5 } = 3 . 5 1 5 )$ .

Since these methods with $\gamma = 1 / x _ { q }$ are of order $p {  } s$ only,it is easy to embed them into a method of higher order. Burrage (1978) added a further stage

$$
g _ { s + 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s + 1 } a _ { s + 1 , \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } )
$$

where $c _ { s + 1 }$ and $a _ { s + 1 , s + 1 }$ are arbitrary and the other $a _ { \mathfrak { s } + 1 , \ j }$ are determined so that the $( s + 1 )$ -stage method satisfies $C ( s )$ too. In order to avoid a new LUdecomposition we choose $a _ { s + 1 , s + 1 } = \gamma$ . The coefficient $c _ { s + 1 }$ is fixed arbitrarily

as $c _ { s + 1 } = 0$ . We then find a unique method

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s + 1 } \widehat { b } _ { \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } )
$$

of order $s + 1$ by computing the coefficients of the interpolatory quadrature rule. An explicit formula for the matrix $T$ which transforms the Runge-Kutta matrix $A$ to Jordan canonical form and $A ^ { - 1 }$ to a very simple lower triangular matrix $\Lambda$ is given in Exercise 1. It can be used for economically solving the linear system (8.13).

# Exercises

1. (Butcher 1979).For the collocation method with $c _ { 1 } , \ldots , c _ { s }$ given by (8.29) prove that (e.g. for $s = 4$ ）

$$
T ^ { - 1 } A T = \gamma \left( \begin{array} { c c c c } { { 1 } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { - 1 } } & { { 1 } } \end{array} \right) , T ^ { - 1 } A ^ { - 1 } T = \frac { 1 } { \gamma } \left( \begin{array} { c c c c } { { 1 } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 1 } } & { { } } & { { } } \\ { { 1 } } & { { 1 } } & { { 1 } } & { { } } \\ { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \end{array} \right)
$$

where the transformation $T$ satisfies

$$
T = \left( L _ { \jmath - 1 } ( x _ { \imath } ) \right) _ { \imath , \jmath = 1 } ^ { s } , \qquad T ^ { - 1 } = \left( \frac { x _ { \jmath } L _ { \imath - 1 } ( x _ { \jmath } ) } { s ^ { 2 } L _ { s - 1 } ( x _ { \jmath } ) ^ { 2 } } \right) _ { \imath , \jmath = 1 } ^ { s }
$$

and $L _ { \jmath - 1 } ( \boldsymbol { x } )$ are the Laguerre polynomials.

Hint. Use the identities

$$
L _ { n } ^ { \prime } ( x ) = L _ { n - 1 } ^ { \prime } ( x ) - L _ { n - 1 } ( x ) , \qquad L _ { n } ( x ) = L _ { n - 1 } ( x ) + { \frac { x } { n } } L _ { n } ^ { \prime } ( x )
$$

and the Christoffel-Darboux formula

$$
\sum _ { \jmath = 0 } ^ { n } L _ { \jmath } ( x ) L _ { \jmath } ( y ) = \frac { n + 1 } { y - x } \Big ( L _ { n + 1 } ( x ) L _ { n } ( y ) - L _ { n + 1 } ( y ) L _ { n } ( x ) \Big )
$$

which, in the limit $y  x$ ,becomes

$$
\sum _ { j = 0 } ^ { n } ( L _ { j } ( x ) ) ^ { 2 } = ( n + 1 ) { \Big ( } L _ { n + 1 } ( x ) L _ { n } ^ { \prime } ( x ) - L _ { n + 1 } ^ { \prime } ( x ) L _ { n } ( x ) { \Big ) } .
$$

# IV.9Extrapolation Methods

It seems that a suitable version of an IEM (implicit extrapolation method) which takes care of these dificulties may become a very strong competitor to any of the general discretization methods for stiff systems presently known.

(the very last sentence of Stetter's book,1973)

Extrapolation of explicit methods is an interesting approach to solving nonstiff differential equations (see Sect.I.9). Here we show to what extent the idea of extrapolation can also be used for stiff problems. We shall use the results of Sect. II.8 for the existence of asymptotic expansions and apply them to the study of those implicit and linearly implicit methods, which seem to be most suitable for the computation of stiff differential equations. Our theory here is restricted to classical $h  0$ order,the study of stability domains and $A$ -stability.

A big difficulty, however, is the fact that the coefficients and remainders of the asymptotic expansion can explode with increasing stiffness and the $h$ -interval, for which the expansion is meaningful,may tend to zero. Bounds on the remainder which hold uniformly for a class of arbitrarily stiff problems,will be discussed later in Sect. VI.5.

# Extrapolation of Symmetric Methods

It is most natural to look first for symmetric one-step methods as the basic integration scheme. Promising candidates are the trapezoidal rule

$$
y _ { \iota + 1 } = y _ { \iota } + { \frac { h } { 2 } } { \Bigl ( } f ( x _ { \iota } , y _ { \iota } ) + f ( x _ { \iota + 1 } , y _ { \iota + 1 } ) { \Bigr ) }
$$

and the implicit mid-point rule

$$
y _ { \imath + 1 } = y _ { \imath } + h f \Big ( x _ { \imath } + \frac { h } { 2 } , \frac { 1 } { 2 } \left( y _ { \imath + 1 } + y _ { \imath } \right) \Big ) .
$$

We take some step-number sequence $n _ { 1 } < n _ { 2 } < n _ { 3 } < \ldots$ set $\begin{array} { r } { h _ { \jmath } = H / n _ { \jmath } } \end{array}$ and define

$$
T _ { j 1 } = y _ { h _ { j } } ( x _ { 0 } + H ) ,
$$

the numerical solution obtained by performing $n _ { \jmath }$ steps with step size $h _ { \ j }$ As described in Sect.I.9 we extrapolate these values according to

$$
T _ { \jmath , k + 1 } = T _ { \jmath , k } + \frac { T _ { \jmath , k } - T _ { \jmath - 1 , k } } { ( n _ { \jmath } / n _ { \jmath - k } ) ^ { 2 } - 1 } .
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $I I _ { \perp }$ ， Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_9, $©$ Springer-Verlag Berlin Heidelberg 2010

![](images/83a23622c865d41304b2423d8011573c89576ab98f4a9bb9e6277ede2a662bbd.jpg)  
Fig.9.1. Stability domains for the extrapolated trapezoidal rule

This provides an extrapolation tableau

$$
\begin{array} { c c c c c } { { T _ { 1 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { T _ { 2 1 } } } & { { T _ { 2 2 } } } & { { } } & { { } } & { { } } \\ { { T _ { 3 1 } } } & { { T _ { 3 2 } } } & { { T _ { 3 3 } } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } \end{array}
$$

all entries of which represent diagonally implicit Runge-Kutta methods (see Ex-ercise 1). Due to the symmetry of the basic schemes (9.1) and (9.2), $T _ { \ j \boldsymbol { k } }$ is a DIRK-method of order $2 k$ . In order to study the stability properties of these methods, we apply them to the test equation $y ^ { \prime } = \lambda y$ . For both methods,(9.1) and (9.2), we obtain

$$
y _ { i + 1 } = { \frac { 1 + { \frac { h \lambda } { 2 } } } { 1 - { \frac { h \lambda } { 2 } } } } y _ { i }
$$

so that the stability function $R _ { j k } ( z )$ of the method $T _ { j k }$ is given recursively by $\left( z = H \lambda \right)$

$$
\begin{array} { c } { { R _ { j 1 } ( z ) = \displaystyle \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } } , } } \\ { { R _ { j , k + 1 } ( z ) = R _ { j , k } ( z ) + \displaystyle \frac { R _ { j , k } ( z ) - R _ { j - 1 , k } ( z ) } { ( n _ { j } / n _ { j - k } ) ^ { 2 } - 1 } . } } \end{array}
$$

Already Dahlquist (1963) noticed that for $n _ { 1 } = 1$ and $n _ { 2 } = 2$ we have

$$
R _ { 2 2 } ( z ) = \frac { 1 } { 3 } \left( 4 \left( \frac { 1 + \frac { z } { 4 } } { 1 - \frac { z } { 4 } } \right) ^ { 2 } - \left( \frac { 1 + \frac { z } { 2 } } { 1 - \frac { z } { 2 } } \right) \right) \to \frac { 5 } { 3 } > 1 \mathrm { f o r } z \to \infty ,
$$

an undesirable property when solving stiff problems. Stetter (1973) proposed taking only even or only odd numbers in the step-number sequence $\{ n _ { \jmath } \}$ .Then, all stability functions of the extrapolation tableau tend for $z  \infty$ to $1$ or $- 1$ ， respectively. But even in this situation extrapolation immediately destroys the $A$ - stability of the underlying scheme (Exercise 2). Fig.9.1 shows the stability domains $\{ z \ ; \ | R _ { k k } ( z ) | \le 1 \}$ for the sequence $\{ 1 , 3 , 5 , 7 , 9 , \ldots \}$

# Smoothing

Some numerical examples reveal the power of the smoothing combined with extrapolation. (B.Lindberg 1971)

Another possibility to overcome the difficulty encountered in (9.7) is smoothing (Lindberg 1971). The idea is to replace the definition (9.3)by Gragg's smoothing step

$$
\begin{array} { c } { { \displaystyle \widehat { T } _ { \jmath 1 } = S _ { h _ { \jmath } } ( x _ { 0 } + H ) , } } \\ { { \displaystyle S _ { h } ( x ) = \frac { 1 } { 4 } \big ( y _ { h } ( x - h ) + 2 y _ { h } ( x ) + y _ { h } ( x + h ) \big ) . } } \end{array}
$$

With $y _ { h } ( x ) , S _ { h } ( x )$ also possesses an asymptotic expansion in even powers of $h$ Therefore, extrapolation according to (9.4) is justified.For the stability function of T1 we now obtain

$$
\begin{array} { c c l } { { \widehat { R } _ { j 1 } ( z ) = \displaystyle \frac { 1 } { 4 } \left\{ \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } - 1 } + 2 \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } } + \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } + 1 } \right\} } } \\ { { = \displaystyle \frac { 1 } { \left( 1 - \frac { z } { 2 n _ { j } } \right) ^ { 2 } } \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } - 1 } } } & { { ( 9 } } \end{array}
$$

which is an $L$ -stable approximation to the exponential function. The stability functions $\widehat { R } _ { \jmath k } ( z )$ (obtained from (9.6b)) all satisfy $\widehat { R } _ { \jmath k } ( z ) = \mathcal { O } ( z ^ { - 2 } )$ for $z \to \infty$ .For the step-number sequence

$$
\{ n _ { \jmath } \} = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , . . . \}
$$

the stability domains of $\widehat { R } _ { k k } ( z )$ are plotted in Fig.9.2.

![](images/ea7f078e45a8f796ab5e18d8211cbe522f30832668548dbb517ea9cac702e000.jpg)  
Fig.9.2. Stability domains of Rkk(z)

# The Linearly Implicit Mid-Point Rule

Extrapolation codes based on fully implicit methods are difficult to implement efficiently. After extensive numerical computations, G.Bader and P.Deuflhard (1983) found that a linearly implicit (Rosenbrock-type) extension of the GBS method of Sect.II.9 gave promising results for stiff equations. This method is based on a two-step algorithm, since one-step Rosenbrock methods (7.4) cannot be symmetric for nonlinear differential equations.

The motivation for the Bader & Deuflhard method is based on Lawson's transformation (Lawson 1967)

$$
y ( x ) = e ^ { J x } \cdot c ( x ) ,
$$

where it is hoped that the matrix $J \approx f ^ { \prime } ( y )$ will neutralize the stiffness.Differentiation gives

$$
c ^ { \prime } = e ^ { - J x } \cdot g ( x , e ^ { J x } c ) \quad { \mathrm { ~ w i t h ~ } } \quad g ( x , y ) = f ( x , y ) - J y .
$$

We now solve (9.13) by the Gragg algorithm (I1.9.13b)

$$
c _ { i + 1 } = c _ { i - 1 } + 2 h e ^ { - J x _ { i } } \cdot g ( x _ { i } , e ^ { J x _ { i } } c _ { i } )
$$

and obtain by back-substitution of (9.12)

$$
e ^ { - h J } y _ { i + 1 } = e ^ { h J } y _ { i - 1 } + 2 h g ( x _ { i } , y _ { i } ) .
$$

For evident reasons of computational ease we now replace $e ^ { \pm h J }$ by the approximations $I \pm h J$ and obtain, adding an appropriate starting and final smoothing step,

$$
\begin{array} { r l r } & {  { ( I - h J ) y _ { 1 } = y _ { 0 } + h g ( x _ { 0 } , y _ { 0 } ) } } \\ & { } & { \displaystyle ( I - h J ) y _ { i + 1 } = ( I + h J ) y _ { i - 1 } + 2 h g ( x _ { i } , y _ { i } ) } \\ & { } & { \displaystyle S _ { h } ( x ) = \frac { 1 } { 2 } ( y _ { 2 m - 1 } + y _ { 2 m + 1 } ) \quad \mathrm { w h e r e } x = x _ { 0 } + 2 m h . } \end{array}
$$

Substituting finally $g$ from (9.13), we arrive at (with $x = x _ { 0 } + 2 m h$ ， $x _ { \ i } = x _ { 0 } + i h )$

$$
\begin{array} { c } { { ( I - h J ) ( y _ { 1 } - y _ { 0 } ) = h f ( x _ { 0 } , y _ { 0 } ) } } \\ { { ( I - h J ) ( y _ { i + 1 } - y _ { \imath } ) = \displaystyle - ( I + h J ) ( y _ { i } - y _ { \imath - 1 } ) + 2 h f ( x _ { \imath } , y _ { i } ) } } \\ { { S _ { h } ( x ) = \displaystyle \frac { 1 } { 2 } ( y _ { 2 m - 1 } + y _ { 2 m + 1 } ) } } \end{array}
$$

where $J$ stands for some approximation to the Jacobian $\frac { \partial f } { \partial y } \big ( x _ { 0 } , y _ { 0 } \big )$ . Putting $J { = } 0$ ， Formulas (9.16a) and (9.16b) become equivalent to those of the GBS method. The scheme (9.16b) is the linearly implicit (or semi-implicit) mid-point rule, Formula (9.16a) the linearly implicit Euler method.

Theorem 9.1 (Bader & Deuflhard 1983).Let $f ( x , y )$ be sufficiently often differentiable and let $J$ be an arbitrary matrix; then the numerical solution defined by $\left( 9 . l 6 a , b , c \right)$ possesses an asymptotic expansion of the form

$$
y ( x ) - S _ { h } ( x ) = \sum _ { \jmath = 1 } ^ { l } e _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } C ( x , h )
$$

where $C ( \boldsymbol { x } , h )$ is bounded for $x _ { 0 } \leq x \leq \overline { { x } }$ and $0 \leq h \leq h _ { 0 }$ .For $J \neq 0$ we have in general $e _ { j } ( x _ { 0 } ) \neq 0$

Proof. As in Stetter's proof for the GBS algorithm we introduce the variables

$$
\begin{array} { r l } & { h ^ { * } = 2 h , \quad x _ { k } ^ { * } = x _ { 0 } + k h ^ { * } , \quad u _ { 0 } = v _ { 0 } = y _ { 0 } , \quad u _ { k } = y _ { 2 k } , } \\ & { v _ { k } = ( I - h J ) y _ { 2 k + 1 } + h J y _ { 2 k } - h f ( x _ { 2 k } , y _ { 2 k } ) } \\ & { \quad = ( I + h J ) y _ { 2 k - 1 } - h J y _ { 2 k } + h f ( x _ { 2 k } , y _ { 2 k } ) . } \end{array}
$$

Method (9.16a,b) can then be rewritten as

$$
\begin{array} { r l } & { \left( \begin{array} { c } { u _ { k + 1 } } \\ { v _ { k + 1 } } \end{array} \right) = \left( \begin{array} { c } { u _ { k } } \\ { v _ { k } } \end{array} \right) \qquad ( } \\ & { + h \ast \left( \begin{array} { c c } { f \left( x _ { k } ^ { \ast } + \frac { h ^ { \ast } } { 2 } , y _ { 2 k + 1 } \right) - J y _ { 2 k + 1 } + J \left( \frac { u _ { k + 1 } + u _ { k } } { 2 } \right) } \end{array} \right) } \\ & { + h \ast \left( \begin{array} { c } { 1 \Big ( f \left( x _ { k } ^ { \ast } + h ^ { \ast } , u _ { k + 1 } \right) + f \left( x _ { k } ^ { \ast } , u _ { k } \right) \Big ) + J y _ { 2 k + 1 } - J \big ( \frac { u _ { k + 1 } + u _ { k } } { 2 } \big ) } \end{array} \right) } \end{array}
$$

where,from (9.18), we obtain the symmetric representation

$$
y _ { 2 k + 1 } = \frac { v _ { k + 1 } + v _ { k } } { 2 } + h ^ { \ast } J \Big ( \frac { u _ { k + 1 } - u _ { k } } { 4 } \Big ) - \frac { h ^ { \ast } } { 4 } \Big ( f \big ( x _ { k + 1 } ^ { \ast } , u _ { k + 1 } \big ) - f \big ( x _ { k } ^ { \ast } , u _ { k } \big ) \Big ) .
$$

The symmetry of (9.19) is illustrated in Fig.9.3 and can be checked analytically by exchanging $u _ { k + 1 }  u _ { k } , v _ { k + 1 }  v _ { k }$ ， $h ^ { \ast }  - h ^ { \ast }$ ,and $x _ { k } ^ { * }  x _ { k } ^ { * } + h ^ { * }$ . Method (9.19) is consistent with the differential equation

$$
\begin{array} { r l r } { u ^ { \prime } = f ( x , v ) - J ( v - u ) , } & { { } } & { u ( x _ { 0 } ) = y _ { 0 } } \\ { v ^ { \prime } = f ( x , u ) + J ( v - u ) , } & { { } } & { v ( x _ { 0 } ) = y _ { 0 } } \end{array}
$$

![](images/00ed4d016f38d7705ad45db8257986a28b5aec194fefa02ad697da8382c44f39.jpg)  
Fig.9.3. Symmetry of Method (9.19) (see (9.16b))

whose exact solution is $u ( x ) = v ( x ) = y ( x )$ ，where $y ( x )$ is the solution of the original equation $y ^ { \prime } = f ( x , y )$ . Applying Theorem II.8.10 we obtain

$$
\begin{array} { l } { { y ( x ) - u _ { h ^ { * } } ( x ) = \displaystyle \sum _ { \jmath = 1 } ^ { l } a _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } A ( x , h ) } } \\ { { \displaystyle y ( x ) - v _ { h ^ { * } } ( x ) = \sum _ { \jmath = 1 } ^ { l } b _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } B ( x , h ) } } \end{array}
$$

with $a _ { _ { \mathcal { I } } } ( x _ { 0 } ) = b _ { _ { \mathcal { I } } } ( x _ { 0 } ) = 0$ . With the help of Formulas (9.18) we can express the numerical solution (9.16c) in terms of $u _ { m }$ and $v _ { m }$ as follows:

$$
\frac { 1 } { 2 } ( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) = ( I - h ^ { 2 } J ^ { 2 } ) ^ { - 1 } \Big ( v _ { m } + h ^ { 2 } J \big ( f ( x _ { 2 m } , u _ { m } ) - J u _ { m } \big ) \Big ) ,
$$

and we obtain for $x = x _ { 0 } + 2 m h$ ，

$$
\begin{array} { c } { { y ( x ) - S _ { h } ( x ) = ( I - h ^ { 2 } J ^ { 2 } ) ^ { - 1 } \bigg ( y ( x ) - v _ { h ^ { * } } ( x ) } } \\ { { - h ^ { 2 } J \Big ( f ( x , u _ { h ^ { * } } ( x ) ) + J \big ( y ( x ) - u _ { h ^ { * } } ( x ) \big ) \Big ) \bigg ) . } } \end{array}
$$

Inserting the expansions (9.20) we find (9.17).

As an application of this theorem we obtain an interesting theoretical result on the existence of $W$ -methods (7.4) (with inexact Jacobian). We saw in Volume I (Exercise1ofSect IL9andTheoremIL9.4)thatthe $T _ { j , k }$ of the extrapolated GBS method represent explicit Runge-Kutta methods. By analogy, it is not difficult to guess that the $T _ { \ j , k }$ for the above linearly implicit midpoint rule represent W - methods (more details in Exercise 3) and we have the following existence result fol such methods.

Theorem 9.2. For $p$ even, there exists a W -method (7.4) of order $p$ with $s =$ $p ( p + 2 ) / 4$ stages.

Proof. It follows from(9.20) that for $x = x _ { 0 } + 2 m h$ the numerical solution $y _ { h } ( x ) =$ $y _ { 2 m }$ possesses an $h ^ { 2 }$ -expansion of the form (9.17) with $e _ { j } ( x _ { 0 } ) = 0$ . Therefore, extrapolation yields W -methods of order $2 k$ (in the $k$ -th column). The result follows by taking $\{ n _ { j } \} = \{ 2 , 4 , 6 , 8 , 1 0 , 1 2 , . . . \}$ and counting the number of necessary function evaluations. □

Table 9.1. $A ( \alpha )$ -stability of extrapolated linearly implicit mid-point rule   

<table><tr><td colspan="6">90°</td></tr><tr><td>90° 90°</td><td colspan="4"></td></tr><tr><td>90°</td><td>90°</td><td>90°</td><td></td><td></td></tr><tr><td>90°</td><td>89.34°</td><td>87.550</td><td>87.34°</td><td></td></tr><tr><td>90°</td><td>88.80°</td><td>86.87°</td><td>86.10°</td><td>86.02°</td></tr><tr><td>90°</td><td>88.490</td><td>87.30°</td><td>86.61°</td><td>86.36° 86.33°</td></tr><tr><td>90°</td><td>88.430</td><td>87.42°</td><td>87.00° 86.78°</td><td>86.70° 86.69°</td></tr></table>

For a stability analysis we apply the method (9.16) with $J = \lambda$ to the test equation $y ^ { \prime } = \lambda y$ . In this case Formula (9.16b) reduces to

$$
y _ { \imath + 1 } = { \frac { 1 + h \lambda } { 1 - h \lambda } } y _ { i - 1 }
$$

and the numerical result is given by

$$
S _ { h } ( x _ { 0 } + 2 m h ) = \frac { 1 } { ( 1 - h \lambda ) ^ { 2 } } \Big ( \frac { 1 + h \lambda } { 1 - h \lambda } \Big ) ^ { m - 1 } y _ { 0 } ,
$$

exactly the same as that obtained from the trapezoidal rule with smoothing (see Formula (9.10). We next have to choose a step-number sequence $\{ n _ { \jmath } \}$ . Clearly, $n _ { j } = 2 m _ { j }$ must be even.Bader & Deuflhard (1983） proposed taking only odd numbers $m _ { j }$ ， since then $S _ { h } ( x _ { 0 } + 2 m _ { \jmath } h )$ in (9.21) has the same sign as the exact solution $e ^ { \lambda \bar { 2 } m _ { j } h } y _ { 0 }$ for all real $h \lambda \leq 0$ . Consequently they were led to

$$
\{ n _ { j } \} = \{ 2 , 6 , 1 0 , 1 4 , 2 2 , 3 4 , 5 0 , . . . \} .
$$

Putting $T _ { j 1 } = S _ { h _ { j } } ( x _ { 0 } + H )$ with ${ h _ { j } = H / n _ { j } }$ and defining $T _ { j k }$ by (9.4) we obtain a tableau of $W$ -methods (7.4) (Exercise 3). By Theorem 9.1 the $k$ -th column of this tableau represents methods of order $2 k - 1$ independent of the choice of $J$ (the methods are not of order $2 k$ ,since $e _ { l } ( x _ { 0 } ) \neq 0$ in (9.17)). The stability function of $T _ { j 1 }$ is given by

$$
R _ { j 1 } ( z ) = \frac { 1 } { ( 1 - \frac { z } { n _ { j } } ) ^ { 2 } } \left( \frac { 1 + \frac { z } { n _ { j } } } { 1 - \frac { z } { n _ { j } } } \right) ^ { n _ { j } / 2 - 1 }
$$

and those of $T _ { \ j \boldsymbol { k } }$ can be computed with the recursion (9.6b). An investigation of the $E$ -polynomial (3.8) for these rational functions shows that not only $T _ { j 1 }$ ,but

![](images/500f1c6133a71c149d84c345e6cf79150b9e8732c8d63d60c50390a7e0c258ee.jpg)  
Fig. 9.4. Stability domains of extrapolated linearly implicit mid-point rule

also $T _ { 2 2 } , T _ { 3 2 }$ and $T _ { 3 3 }$ are $A$ -stable (Hairer,Bader & Lubich 1982). The angle of $A ( \alpha )$ -stability for some further elements in the extrapolation tableau are listed in Table 9.1. Stability domains of $T _ { k k }$ for $k = 2 , 3 , 4 , 5 , 6$ are plotted in Fig. 9.4.

# Implicit and Linearly Implicit Euler Method

Why not consider also non-symmetric methods as basic integration schemes? Deuflhard (1985) reports on experiments with extrapolation of the implicit Euler method

$$
y _ { i + 1 } = y _ { i } + h f ( x _ { i + 1 } , y _ { \imath + 1 } )
$$

and of the linearly implicit Euler method

$$
( I - h J ) ( y _ { i + 1 } - y _ { i } ) = h f ( x _ { i } , y _ { i } ) ,
$$

where, again, $J$ is an approximation to $\frac { \partial f } { \partial y } \big ( x _ { 0 } , y _ { 0 } \big )$ .These methods are not symmetric and have only a $h$ -expansion of their global error. We therefore have to extrapolate the numerical solutions at $x _ { 0 } + H$ according to

$$
T _ { j , k + 1 } = T _ { j , k } + \frac { T _ { j , k } - T _ { j - 1 , k } } { ( n _ { j } / n _ { j - k } ) - 1 } ,
$$

so that $T _ { j k }$ represents a method of order $k$

For both basic methods,(9.24) and (9.25), the stability function of $T _ { j k }$ is the same and defined recursively by

$$
\begin{array} { c } { { R _ { j 1 } ( z ) = \displaystyle \bigg ( 1 - \frac { z } { n _ { j } } \bigg ) ^ { - n _ { j } } } } \\ { { { } } } \\ { { R _ { j , k + 1 } ( z ) = R _ { j , k } ( z ) + \displaystyle \frac { R _ { j , k } ( z ) - R _ { j - 1 , k } ( z ) } { ( n _ { j } / n _ { j - k } ) - 1 } . } }  \end{array}
$$

Taking the step-number sequence

$$
\{ n _ { j } \} = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , . . . \}
$$

we have plotted in Fig.9.5 the stability domains of $R _ { k k } ( z )$ (left picture） and $R _ { k , k - 1 } ( z )$ (right picture). All these methods are seen to be $A ( \alpha )$ -stable with $\alpha$ close to $9 0 °$ . The values of $\alpha$ (computed numerically) for $R _ { j k } ( z )$ with $j \le 8$ are given in Table 9.2.

We shall see in the chapter on differential algebraic systems that it is preferable to use the first subdiagonal of the extrapolation tableau resulting from (9.28). This is equivalent to the use of the step number sequence $\{ n _ { i } \} = \{ 2 , 3 , 4 , 5 , . . . \}$ . Also an effective construction of a dense output can best be motivated in the seting of differential-algebraic equations (Sect. VI.5).

Table 9.2. $A ( \alpha )$ -stabiliy of extrapolated Euler   

<table><tr><td colspan="8"></td></tr><tr><td>90° 90° 90°</td><td colspan="5"></td><td rowspan="7">89.80°</td></tr><tr><td>90°</td><td>90°</td><td>89.850</td><td></td><td></td></tr><tr><td>90°</td><td>90°</td><td>89.90°</td><td>89.77°</td><td></td></tr><tr><td>90°</td><td>90°</td><td>89.930</td><td>89.84°</td><td>89.77°</td></tr><tr><td>90°</td><td>90°</td><td>89.95°</td><td>89.88°</td><td>89.82° 89.780</td></tr><tr><td>90°</td><td>90°</td><td>89.96°</td><td>89.91° 89.860</td><td>89.820 89.83°</td></tr><tr><td>90°</td><td>90°</td><td>89.970</td><td>89.93°</td><td>89.89° 89.85°</td></tr></table>

![](images/4ebadf70862a50d3aa59480b18587f4c0358f000ba7e3f709f65db63c878de45.jpg)  
Fig.9.5.Stability domains of extrapolated Euler

# Implementation

Extrapolation methods based on implicit discretizations are in general less efficient than those based on linearly implicit discretizations. The reason is that the arising nonlinear systems have to be solved very accurately, so that the asymptotic expansion of the error is not destroyed. The first successful extrapolation code for stiff differential equations is METAN1 of Bader & Deuflhard (1983),which implements the linearly implicit mid-point rule (9.16). In fact, Formula (9.16b) is replaced by the equivalent formulation

$$
\Delta y _ { \imath } = \Delta y _ { i - 1 } + 2 ( I - h J ) ^ { - 1 } \Big ( h f ( x _ { \imath } , y _ { \imath } ) - \Delta y _ { \imath - 1 } \Big ) , \quad \Delta y _ { \imath } = y _ { \imath + 1 } - y _ { \imath }
$$

which avoids a matrix-vector multiplication. The step size and order selection of this code is described in Deuflhard (1983). Modifications in the control of step size and order are proposed by Shampine (1987). We have implemented the following two extrapolation codes (see Appendix):

SODEX is based on the linearly implicit mid-point rule (9.16),uses the stepnumber sequence (9.22) and is mathematically equivalent to METAN1. The step size and order selection in SODEX is with some minor changes that of the non-stiff code ODEX of Sect. II.9. We just mention that in the formula for the work per unit step (II.9.26) the number $A _ { k }$ is augmented by the dimension of the differential equation in order to take into account the Jacobian evaluation.

SEULEX is an implementation of the linearly implicit Euler method (9.25) using the step-number sequence $\{ 2 , 3 , 4 , 5 , 6 , 7 , \ldots \}$ (other sequences can be chosen as internal options). The step size and order selection is that of SODEX. The original code (EULSIM, first discussed by Deuflhard 1985) uses the same numerical method,but a different implementation.

Neither code can solve the van der Pol equation problem in a straightforward way because of overflow ...

(L.F. Shampine 1987)

A big diffculty in the implementation of extrapolation methods is the use of “large” step sizes. During the computation of $T _ { \ j 1 }$ one may easily get into trouble with exponential overflow when evaluating the right-hand side of the differential equation. As a remedy we propose the following strategies:

a） In establishing the extrapolation tableau we compare the estimated error $e r r _ { \jmath } =$ $\| T _ { j , j - 1 } - T _ { j j } \|$ with the preceding one. Whenever $e r r _ { j } \geq e r r _ { j - 1 }$ for some $j \geq 3$ we restart the computation of the step with a smaller $H$ ,say, $H = 0 . 5 \cdot H$   
b) In order to be able to interrupt the computations already after the first $f$ evaluations,we require that the step sizes $h = H / n _ { i }$ (for $i = 1$ and $i \approx 2$ be small enough so that a simplified Newton iteration applied to the implicit Euler method $y = y _ { 0 } + h f ( x , y )$ ， $x = x _ { 0 } + h$ would converge ("stability check", an idea of Deuflhard). The first two iterations read

$$
\begin{array} { r l } & { ( I - h J ) \Delta _ { 0 } = h f ( x _ { 0 } , y _ { 0 } ) , \qquad y ^ { ( 1 ) } = y _ { 0 } + \Delta _ { 0 } } \\ & { ( I - h J ) \Delta _ { 1 } = h f ( x _ { 0 } + h , y ^ { ( 1 ) } ) - \Delta _ { 0 } . } \end{array}
$$

The computations for the step are restarted with a smaller $H$ ,if $\| \Delta _ { 1 } \| \ge \| \Delta _ { 0 } \|$ (divergence of the iteration). Observe that for both methods,(9.16) and (9.25), no additional function evaluations are necessary. For the linearly implicit midpoint rule we have the simple relations $\Delta _ { 0 } = \Delta y _ { 0 }$ ， $\begin{array} { r } { \Delta _ { 1 } = \frac { 1 } { 2 } ( \Delta y _ { 1 } - \Delta y _ { 0 } ) } \end{array}$ (see (9.29)).

Non-Autonomous Differential Equations. Given a non-autonomous differential equation $y ^ { \prime } { = } f ( x , y )$ , one has several possibilities to apply the above extrapolation algorithms:

i) apply the Formula (9.16) or (9.25)directly (this is justified, since allasymptotic expansions hold for general non-autonomous problems);   
ii） transform the differential equation into an autonomous system by adding $x ^ { \prime } = 1$ and then apply the algorithm. This yields

$$
( I - h J ) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( x _ { \iota } , y _ { \iota } ) + h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } )
$$

for the linearly implicit Euler method (the derivative $\frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } )$ can also be replaced by some approximation). For the linearly implicit mid-point rule, (9.16a) has to be replaced by (9.31) with $i \simeq 0$ , the remaining two formulas (9.16b) and (9.16c) are not changed.

iii） apply one simplified Newton iteration to the implicit Euler discretization (9.24). This gives

$$
( I - h J ) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( x _ { \iota + 1 } , y _ { \iota } ) .
$$

The use of this formula avoids the computation of the derivative $\partial f / \partial x$ ,but requires one additional function evaluation for each $T _ { , \mathfrak { l } }$ . In the case of the linearly implicit mid-point rule the replacement of (9.16a) by (9.32） would destroy symmetry and the expansions in $h ^ { 2 }$

A theoretical study of the three different approaches for the linearly implicit Euler method applied to the Prothero-Robinson equation (see Exercise 4 below) indicates that the third approach is preferable. More theoretical insight into this question will be obtained from the study of singular perturbation problems (Chapter VI).

Implicit Differential Equations. Our codes in the appendix are written for problems of the form

$$
M y ^ { \prime } = f ( x , y )
$$

where $M$ is a constant square matrix. The necessary modifications in the basic formulas are obtained,as usual, by replacing all $f ^ { \prime } s$ and $J ^ { \prime } s$ by $M ^ { - 1 } f$ and $M ^ { - 1 } J$ ， and premultiplying by $M$ . The linearly implicit Euler method then reads

$$
( M - h J ) ( y _ { i + 1 } - y _ { \imath } ) = h f ( x _ { \imath } , y _ { \imath } )
$$

andthe linearlyimplicit mid-pointrule becomes,with $\Delta y _ { i } = y _ { i + 1 } - y _ { i }$

$$
\Delta y _ { \imath } = \Delta y _ { \imath - 1 } + 2 ( M - h J ) ^ { - 1 } \Big ( h f ( x _ { \imath } , y _ { i } ) - M \Delta y _ { \imath - 1 } \Big ) .
$$

# Exercises

1. Consider the implicit mid-point rule (9.2) as basic integration scheme and define $T _ { \ j \boldsymbol { k } }$ by (9.3) and (9.4).

a) Prove that $T _ { \ j \boldsymbol { k } }$ represents a DIRK-method of order $p = 2 k$ with $s = n _ { \mathrm { 1 } } +$ $n _ { 2 } + \ldots + n _ { _ { J } }$ stages.

b） $\widehat { T } _ { \jmath k }$ ,definedy(9.8)d(9.4)svalettK-etdfder $p = \bar { 2 } k - 1$ only.

2.Let $R _ { \ j k } ( z )$ be given by (9.6) and assume that the step-number sequence consists of even numbers only. Prove that $R _ { \ j 2 } ( z )$ cannot be $A$ -stable. More precisely, show that at most a finite number of points of the imaginary axis can lie in the stability domain of $R _ { j 2 } ( z )$ (interpret Fig. 9.6).

![](images/39722dae46486d4bc0ba72671a329fd34bb3ea3bc5ee99cbf3263a4b62ca6b36.jpg)  
Fig.9.6. How extrapolation destroys $A$ -stability

3.Prove that $S _ { h } ( x )$ ,defined by (9.16),is the numerical result of the $( 2 n + 1 )$ stage $W$ -method (7.4) with the following coefficients $\left( n = 2 m \right)$ ：

$$
\begin{array} { r l } & { \alpha _ { i j } = \left\{ \begin{array} { l l } { 1 / n } & { \mathrm { i f ~ } j = 1 \mathrm { ~ a n d ~ } i \mathrm { ~ e v e n } , } \\ { 2 / n } & { \mathrm { i f ~ } 1 < j < i \mathrm { ~ a n d ~ } i - j \mathrm { ~ o d d } , } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right. } \\ & { \gamma _ { \imath j } = \left\{ \begin{array} { l l } { ( - 1 ) ^ { i - j } / n } & { \mathrm { i f ~ } j = 1 \mathrm { ~ o r ~ } j = i , } \\ { 2 ( - 1 ) ^ { i - \jmath } / n } & { \mathrm { i f ~ } 1 < j < i . } \end{array} \right. } \\ & { b _ { \imath } = \alpha _ { n + 1 , \imath } + \gamma _ { n + 1 , i } \qquad \mathrm { f o r ~ a l l ~ } i . } \end{array}
$$

4.Apply the three different versions of the linearly implicit Euler method (9.25), (9.31) and (9.32) to the problem $y ^ { \prime } = \lambda ( y - \varphi ( x ) ) + \varphi ^ { \prime } ( x )$ ．Prove that the errors $e _ { i } = y _ { i } - \varphi ( x _ { i } )$ satisfy $e _ { \imath + 1 } = ( 1 - h \lambda ) ^ { - 1 } e _ { \imath } + \delta _ { h } ( x _ { i } )$ , where for $h \to 0$ and $h \lambda  \infty$ ，

$$
\begin{array} { l } { { \delta _ { h } ( x ) = - h \varphi ^ { \prime } ( x ) + { \mathcal O } ( h ^ { 2 } ) + { \mathcal O } ( \lambda ^ { - 1 } ) , } } \\ { { \delta _ { h } ( x ) = - \displaystyle \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + ( 1 - h \lambda ) ^ { - 1 } h ^ { 2 } \lambda ( \varphi ^ { \prime } ( x ) - \varphi ^ { \prime } ( x _ { 0 } ) ) + { \mathcal O } ( h ^ { 3 } ) + { \mathcal O } ( h \lambda ^ { - 1 } ) , } } \\ { { \delta _ { h } ( x ) = ( 1 - h \lambda ) ^ { - 1 } \Big ( \displaystyle \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + { \mathcal O } ( h ^ { 3 } ) \Big ) , } } \end{array}
$$

respectively.

Theory without practice cannot survive and dies as quickly as it lives. (Leonardo da Vinci

1452-1519,cited from M. Kline,Math. Thought 1972, p. 224)

Sine experientia nihil sufficienter scrire potest (Without experience it is not possible to know anything adequately).

(Inscription overlooking Botanic Garden, Oxford; found in The Latin Citation Calendar, Oxford 1996)

After having seen so many diferent methods and ideas in the foregoing sections, it is legitimate to study how all these theoretical properties pay off in numerical efficiency.

# The Codes Used

We compared the following codes, some of which are described in the Appendix:

RADAU5 and SDIRK4 are implicit Runge-Kutta codes. The first one is based on the Radau IIA method with $s = 3$ of order 5 (Table 5.6), whereas the second one is based on the SDIRK method (6.16) of order 4. Both methods are $I$ stable. Details of their implementation are given in Sect.IV.8.

RODAS and ROS4 are Rosenbrock codes of order 4 with an embedded 3rd order error estimator. ROS4 implements the methods of Table 7.2. A switch allows one to choose between the different coefficient sets. The underlying method of RODAS satisfies additional order conditions for differential-algebraic equations (see Sect. VI.4 below), but requires a little more work per step. RODAS5 is an extension of RODAS to order 5. Its coefcients are constructed by Di Marzo (1992).

SEULEX and SODEX are extrapolation codes. They implement the (Stiff) linearly implicit EULer EXtrapolation method (9.32) and the extrapolation algorithm based on the linearly implicit mid-point rule (method (9.16) of Bader & Deuflhard 1983),respectively. Both methods are discussed in Sect.IV.9.

In the numerical experiments of this section we have also included the results of LSODE (a BDF code of Hindmarsh 1980)． It is a representative of the class of multistep methods to be described in Chapter V.

Many of the treated examples are very stiff and explicit methods would require hours to compute the solution. On some examples, however, it was also interesting to see their performance, especially for the methods with extended region of stabil-ity (e.g., the Runge-Kutta-Chebyshev code RKC of Sommeijer (1991), explained in Sect.IV.2),as well as for a standard explicit Runge-Kutta code, such as DOPRI5 of Volume I.

# Twelve Test Problems

Man huite sich,auf Grund einzelner Beispiele allgemeine Schluisse über den Wert oder Unwert einer Methode zu ziehen. Dazu gehort sehr viel Erfahrung. (L. Collatz 1950)

The first extensive numerical comparisons for stiff equations were made by Enright, Hull & Lindberg (1975). Their STIFF-DETEST set of problems has become a veritable “must” for generations of software writers (see also the critical remarks of Shampine 1981). Several additional test problems, usually from chemical kinetics,have been proposed by Enright & Hull (1976). An interesting review article containing also problems of large dimension is due to Byrne & Hindmarsh (1987).

The problems chosen here for our tests are the following:

VDPOL - the van der Pol oscillator (see (1.5") and Fig.8.1)

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = y _ { 2 } } \\ { \qquad y _ { 2 } ^ { \prime } = \big ( ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \big ) / \varepsilon , \qquad \varepsilon = 1 0 ^ { - 6 } } \\ { y _ { 1 } ( 0 ) = 2 , \quad y _ { 2 } ( 0 ) = 0 ; \quad x _ { \mathrm { o u t } } = 1 , 2 , 3 , 4 , \dots , 1 1 . } \end{array}
$$

ROBER - the reaction of Robertson (1966) (see (1.3) and (1.4))

$$
\begin{array} { r l r } { y _ { 1 } ^ { \prime } = - 0 . 0 4 y _ { 1 } + 1 0 ^ { 4 } y _ { 2 } y _ { 3 } \qquad } & { } & { y _ { 1 } ( 0 ) = 1 } \\ { y _ { 2 } ^ { \prime } = } & { { } 0 . 0 4 y _ { 1 } - 1 0 ^ { 4 } y _ { 2 } y _ { 3 } - 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & { y _ { 2 } ( 0 ) = 0 } \\ { y _ { 3 } ^ { \prime } = } & { { } \ 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & { y _ { 3 } ( 0 ) = 0 , } \end{array}
$$

one of the most prominent examples of the “stiff" literature. It was usually treated on the interval $0 \leq x \leq 4 0$ , until Hindmarsh discovered that many codes fail if $_ x$ becomes very large $( 1 0 ^ { 1 1 } \ \mathrm { s a y } )$ . The reason is that whenever the numerical solution of $y _ { 2 }$ accidentally becomes negative, it then tends to $- \infty$ and the run ends by overflow. We have therefore chosen $x _ { \mathrm { o u t } } = 1 , 1 0 , 1 0 ^ { 2 } , 1 0 ^ { 3 } , \dotsc , 1 0 ^ { 1 1 }$ ·

OREGO - the Oregonator, the famous model with a periodic solution describing the Belusov-Zhabotinskii reaction (Field & Noyes 1974,see also Enright & Hull 1976)

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = 7 7 . 2 7 \Big ( y _ { 2 } + y _ { 1 } \big ( 1 - 8 . 3 7 5 \cdot 1 0 ^ { - 6 } y _ { 1 } - y _ { 2 } \big ) \Big ) } \\ { y _ { 2 } ^ { \prime } = \cfrac { 1 } { 7 7 . 2 7 } \big ( y _ { 3 } - ( 1 + y _ { 1 } ) y _ { 2 } \big ) } \\ { y _ { 3 } ^ { \prime } = 0 . 1 6 1 \big ( y _ { 1 } - y _ { 3 } \big ) } \end{array}
$$

$$
y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = 2 , \quad y _ { 3 } ( 0 ) = 3 , \qquad x _ { 0 0 t } = 3 0 , 6 0 , 9 0 , \ldots , 3 6 0 .
$$

For pictures see Volume I, p. 119.

HIRES -this chemical reaction involving eight reactants was proposed by Schäfer (1975） to explain “the growth and differentiation of plant tissue independent of

photosynthesis at high levels of irradiance by light". It has been promoted as a test example by Gottwald (1977). The corresponding equations are

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = - 1 . 7 1 \cdot y _ { 1 } + 0 . 4 3 \cdot y _ { 2 } + 8 . 3 2 \cdot y _ { 3 } + 0 . 0 0 0 7 } \\ & { y _ { 2 } ^ { \prime } = 1 . 7 1 \cdot y _ { 1 } - 8 . 7 5 \cdot y _ { 2 } } \\ & { y _ { 3 } ^ { \prime } = - 1 0 . 0 3 \cdot y _ { 3 } + 0 . 4 3 \cdot y _ { 4 } + 0 . 0 3 5 \cdot y _ { 5 } } \\ & { y _ { 4 } ^ { \prime } = 8 . 3 2 \cdot y _ { 2 } + 1 . 7 1 \cdot y _ { 3 } - 1 . 1 2 \cdot y _ { 4 } } \\ & { y _ { 5 } ^ { \prime } \simeq - 1 . 7 4 5 \cdot y _ { 5 } + 0 . 4 3 \cdot y _ { 6 } + 0 . 4 3 \cdot y _ { 7 } } \\ & { y _ { 6 } ^ { \prime } = - 2 8 0 \cdot y _ { 6 } y _ { 8 } + 0 . 6 9 \cdot y _ { 4 } + 1 . 7 1 \cdot y _ { 5 } - 0 . 4 3 \cdot y _ { 6 } + 0 . 6 9 \cdot y _ { 7 } } \\ & { y _ { 7 } ^ { \prime } = 2 8 0 \cdot y _ { 6 } y _ { 8 } - 1 . 8 1 \cdot y _ { 7 } } \\ & { y _ { 8 } ^ { \prime } = - y _ { 7 } ^ { \prime } } \end{array}
$$

$$
y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = y _ { 3 } ( 0 ) = \ldots = y _ { 7 } ( 0 ) = 0 , \quad y _ { 8 } ( 0 ) = 0 . 0 0 5 7
$$

and chosen output values are $x _ { \mathrm { o u t } } = 3 2 1 . 8 1 2 2$ and 421.8122.

E5 — is another chemical recation problem, called $^ { 6 6 } \mathrm { E } 5 ^ { \circ }$ in the collection by Enright,Hull & Lindberg (1975). It is given by

$$
\begin{array} { r l r l } { y _ { 1 } ^ { \prime } = - A y _ { 1 } - B y _ { 1 } y _ { 3 } } & { } & & { y _ { 1 } ( 0 ) = 1 . 7 6 \cdot 1 0 ^ { - 3 } } \\ { y _ { 2 } ^ { \prime } = { } } & { { } A y _ { 1 } } & { - M C y _ { 2 } y _ { 3 } } & { } & { y _ { 2 } ( 0 ) = 0 } \\ { y _ { 3 } ^ { \prime } = { } } & { { } A y _ { 1 } - B y _ { 1 } y _ { 3 } - M C y _ { 2 } y _ { 3 } + C y _ { 4 } } & { } & { y _ { 3 } ( 0 ) = 0 } \\ { y _ { 4 } ^ { \prime } = { } } & { { } B y _ { 1 } y _ { 3 } } & { - C y _ { 4 } } & { } & { y _ { 4 } ( 0 ) = 0 , } \end{array}
$$

where $A = 7 . 8 9 \cdot 1 0 ^ { - 1 0 }$ ， $B = 1 . 1 \cdot 1 0 ^ { 7 }$ ， $C = 1 . 1 3 \cdot 1 0 ^ { 3 }$ ,and $M = 1 0 ^ { 6 }$ . As we can see from Fig.10.1 the variables are badly scaled $( y _ { 1 } \approx 1 0 ^ { - 3 }$ at the beginning,all other components do not exceed the value $1 . 4 6 \cdot 1 0 ^ { - 1 0 } )$ ,and “... a scalar absolute error tolerance is quite unsuitable” (Shampine 1981). The differential equation possesses the invariant $y _ { 2 } - y _ { 3 } - y _ { 4 } = 0$ , and it is recommended to use the relation $y _ { 3 } ^ { \prime } = y _ { 2 } ^ { \prime } - y _ { 4 } ^ { \prime }$ in the function subroutine (because of eventual cancellation of digits).

Originally the problem was posed on the interval $0 \leq x \leq 1 0 0 0$ , but Alexander (1997) discovered that the solutions possess interesting properties on a much longer interval.We folow this suggestion and consider output values at $x _ { \tt o u t } =$ $1 0 , 1 0 ^ { 3 } , 1 0 ^ { 5 } , 1 0 ^ { 7 } , \dotsc , 1 0 ^ { 1 3 }$

![](images/c815e9e9ee59e64b3193a46d67ff29f64d551f6a5229652c5c8d1792d3a94375.jpg)  
Fig.10.1. Solution of (10.5) in double logarithmic scale

PLATE - this is a linear and non-autonomous example of medium stiffness and medium size. It describes the movement of a rectangular plate under the load of a car passing across it:

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } + \omega \frac { \partial u } { \partial t } + \sigma \Delta \Delta u = f ( x , y , t ) .
$$

The plate $\Omega = \{ ( x , y ) ; 0 \leq x \leq 2 , 0 \leq y \leq 4 / 3 \}$ is discretized on a grid of $8 \times 5$ interior points $x _ { \imath } = i h$ ， $y _ { \jmath } = j h , h = 2 / 9$ with initial and boundary conditions

$$
u | _ { \partial \Omega } = 0 , \quad \Delta u | _ { \partial \Omega } = 0 , \quad u ( x , y , 0 ) = 0 , \quad \frac { \partial u } { \partial t } ( x , y , 0 ) = 0 .
$$

The integration interval is $0 \leq t \leq 7$ . The load $f ( x , y , t )$ is idealized by the sum of two Gaussian curves which move in the $x$ -direction and which reside on “four wheels"

$$
f ( x , y , t ) = \left\{ \begin{array} { c c } { { 2 0 0 \big ( e ^ { - 5 ( t - x - 2 ) ^ { 2 } } + e ^ { - 5 ( t - x - 5 ) ^ { 2 } } \big ) } } & { { \mathrm { i f ~ } y = y _ { 2 } \mathrm { ~ o r ~ } y _ { 4 } } } \\ { { 0 } } & { { \mathrm { f o r ~ a l l ~ o t h e r ~ } y . } } \end{array} \right.
$$

The plate operator $\Delta \Delta$ is discretized via the standard “computational molecule”

$$
\begin{array} { r l } { 1 } & { { } } \\ { 2 } & { { } { - } 8 \quad 2 } \\ { 1 } & { { } { - } 8 \quad 2 0 \quad { - } 8 \quad 1 } \\ { 2 } & { { } { - } 8 \quad 2 } \\ { 1 } & { { } \qquad 1 } \end{array}
$$

and the friction and stiffness parameters are chosen as $\omega = 1 0 0 0$ and $\sigma = 1 0 0$ The resulting system is then of dimension 80 with negative real as well as complex eigenvalues ranging between $- 5 0 0 \leq \mathrm { R e } \lambda < 0$ with maximal angle $\alpha \approx 7 1 ^ { \circ }$ (see Definition 3.9).

BEAM— the elastic beam (1.10) of Sect.IV.1. We choose $n = 4 0$ in (1.10'） so that the differential system is of dimension 80, and $0 \le t \le 5$ as integration interval. The eigenvalues of the Jacobian are purely imaginary and vary between $- 6 4 0 0 i$ and $+ 6 4 0 0 i$ (see Eq.(2.23)). The initial conditions (1.18) and (1.19) are chosen such that the solution nevertheless appears to be smooth. However, a detailed numerical study shows that the exact solution possesses high oscillations with period $\approx 2 \pi / 6 4 0 0$ and amplitude $\approx 1 0 ^ { - 6 }$ (see Fig.10.2).

![](images/3b059ee4cb0251e10b2f483d415a3d1664ed3518db57f7127a114afe064b0028.jpg)  
Fig.10.2. Third finite differences $\Delta ^ { 3 } y _ { 8 0 } / \Delta x ^ { 3 }$ of solutionsof the beam equation (1.10'） with $n = 4 0$ for $0 \leq x \leq 0 . 0 7$

![](images/164cb468cfd0531dc6b04f5d3db01189a5ee55dd546c64564dcf85ad9605b0e7.jpg)  
Fig.10.3. The cusp catastrophe with $N \approx 3 2$

CUSP — this is a combination of Zeeman's “cusp catastrophe”model ( $( - \varepsilon \dot { y } =$ $y ^ { 3 } + a y + b )$ for the nerve impulse mechanism (Zeeman 1972) combined with the van der Pol oscillator (see Fig.10.3)

$$
\begin{array} { l } { \displaystyle \frac { \partial y } { \partial t } = - \frac { 1 } { \varepsilon } ( y ^ { 3 } + a y + b ) + \sigma \frac { \partial ^ { 2 } y } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial a } { \partial t } = b + 0 . 0 7 v + \sigma \frac { \partial ^ { 2 } a } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial b } { \partial t } = ( 1 - a ^ { 2 } ) b - a - 0 . 4 y + 0 . 0 3 5 v + \sigma \frac { \partial ^ { 2 } b } { \partial x ^ { 2 } } } \end{array}
$$

where

$$
v = \frac { u } { u + 0 . 1 } , \quad u = ( y - 0 . 7 ) ( y - 1 . 3 ) .
$$

We put $\sigma = 1 / 1 4 4$ and make the problem stiff by choosing $\varepsilon = 1 0 ^ { - 4 }$ . We discretize the diffusion terms by the method of lines

$$
\begin{array} { r l } & { \dot { y } _ { \iota } = - 1 0 ^ { 4 } ( y _ { \iota } ^ { 3 } + a _ { \iota } y _ { \iota } + b _ { \iota } ) + D ( y _ { \iota - 1 } - 2 y _ { \iota } + y _ { \iota + 1 } ) } \\ & { \dot { a } _ { \iota } = b _ { \iota } + 0 . 0 7 v _ { \iota } + D ( a _ { \iota - 1 } - 2 a _ { \iota } + a _ { \iota + 1 } ) \qquad \quad \qquad i = 1 , \dots , N } \\ & { \dot { b } _ { \iota } = ( 1 - a _ { \iota } ^ { 2 } ) b _ { \iota } - a _ { \iota } - 0 . 4 y _ { \iota } + 0 . 0 3 5 v _ { \iota } + D ( b _ { \iota - 1 } - 2 b _ { \iota } + b _ { \iota + 1 } ) } \end{array}
$$

where

$$
N = 3 2 , \quad v _ { \ i } = \frac { u _ { \ i } } { u _ { \ i } + 0 . 1 } , \quad u _ { \ i } = ( y _ { \ i } - 0 . 7 ) ( y _ { \ i } - 1 . 3 ) , \quad D = \sigma N ^ { 2 } = \frac { N ^ { 2 } } { 1 4 4 } ,
$$

with periodic boundary conditions

$$
\begin{array} { r l r l r l } { y _ { 0 } : = y _ { N } , } & { \quad } & { a _ { 0 } : = a _ { N } , } & { \quad } & { b _ { 0 } : = b _ { N } , } & \\ { y _ { N + 1 } : = y _ { 1 } , } & { \quad } & { a _ { N + 1 } : = a _ { 1 } , } & { \quad } & { b _ { N + 1 } : = b _ { 1 } , } & \end{array}
$$

and obtain a system of dimension $3 \cdot N = 9 6$ . We take the initial values

$$
y _ { \tau } ( 0 ) = 0 , \quad a _ { \ i } ( 0 ) = - 2 \cos \Bigl ( { \frac { 2 i \pi } { N } } \Bigr ) , \quad b _ { \ i } ( 0 ) = 2 \sin \Bigl ( { \frac { 2 i \pi } { N } } \Bigr ) \qquad i = 1 , \ldots , N .
$$

and $t _ { \mathrm { o u t } } = 1 . 1$ ·

BRUSS — this is the equation(1.6') with $\alpha = 1 / 5 0$ ,the same initial conditions as in Sect.IV.1,and integration interval $0 \leq t \leq 1 0$ . But we now let $N = 5 0 0$ so that (1.6') becomes a system of 1ooo differential equations with largest eigenvalue close to $- 2 0 0 0 0$ . The equations therefore become considerably stiff. The Jacobian of this system is banded with upper and lower bandwidth 2 (if the solution components are ordered as $u _ { 1 } , v _ { 1 } , u _ { 2 } , v _ { 2 } , u _ { 3 } , v _ { 3 } , \quad$ etc.).

KS - is the one-dimensional Kuramoto-Sivashinsky equation

$$
{ \frac { \partial U } { \partial t } } = - { \frac { \partial ^ { 2 } U } { \partial x ^ { 2 } } } - { \frac { \partial ^ { 4 } U } { \partial x ^ { 4 } } } - { \frac { 1 } { 2 } } { \frac { \partial U ^ { 2 } } { \partial x } }
$$

with periodic boundary conditions $\boldsymbol { u } ( \boldsymbol { x } + \boldsymbol { L } , t ) = \boldsymbol { u } ( \boldsymbol { x } , t )$ , taken from Collet, Eckmann,Epstein & Stubbe (1993)．We choose $L = 2 \pi / q$ ， $q = 0 . 0 2 5$ , and take as initial condition

$$
\begin{array} { r l } & { \eta _ { 1 } = \operatorname* { m i n } ( x / L , 0 . 1 - x / L ) , } \\ & { \eta _ { 2 } = 2 0 ( x / L - 0 . 2 ) ( 0 . 3 - x / L ) , } \\ & { \eta _ { 3 } = \operatorname* { m i n } ( x / L - 0 . 6 , 0 . 7 - x / L ) , } \\ & { \eta _ { 4 } = \operatorname* { m i n } ( x / L - 0 . 9 , 1 - x / L ) , } \end{array}
$$

The inverse heat equation term $- \partial ^ { 2 } U / \partial x ^ { 2 }$ creates instability, which is stabilized for the higher oscillations by the beam equation term $- \partial ^ { 4 } U / \partial x ^ { 4 }$ . The nonlinear transport term $\partial U ^ { 2 } / \partial x$ couples the modes and ensures that the solution remains bounded. All this creates wonderful chaos (see Fig.10.4).

We solve Eq.(10.9) using the pseudo-spectral method, i.e.，we consider the Fourier coefficients

$$
\widehat { U } _ { \ j } ( t ) = \frac { 1 } { L } \int _ { 0 } ^ { L } U ( \boldsymbol { x } , t ) e ^ { - \imath q \boldsymbol { \jmath } x } d \boldsymbol { x } , \qquad U ( \boldsymbol { x } , t ) = \sum _ { \boldsymbol { \jmath } \in \mathbb { Z } } \widehat { U } _ { \ j } ( t ) e ^ { \imath q \boldsymbol { \jmath } x } ,
$$

so that (10.9) takes the form of an infinite dimensional ordinary differential equation

$$
\widehat { U } _ { \jmath } ^ { \prime } = \big ( ( q j ) ^ { 2 } - ( q j ) ^ { 4 } \big ) \widehat { U } _ { \jmath } - \frac { \imath q j } { 2 } ( \widehat { U \cdot U } ) _ { \jmath } .
$$

We truncate this system as follows: for a fixed $N$ ,say $N = 1 0 2 4$ , we consider the $N$ -periodic sequence $u ( t ) = \{ u _ { \ j } ( t ) \}$ solving the ordinary differential equation

$$
u ^ { \prime } = ( d ^ { 2 } - d ^ { 4 } ) u - \frac { i d } { 2 } \mathcal { F } _ { N } \big ( \mathcal { F } _ { N } ^ { - 1 } u \cdot \mathcal { F } _ { N } ^ { - 1 } u \big ) ,
$$

where $d$ denotes the $N$ -periodic sequence given by $d _ { j } = q j$ for $| j | < N / 2$ and $d _ { N / 2 } = 0$ ,and the product of sequences in (10.11) is componentwise. The discrete

![](images/d348a2fa54c6842f5b15655b14f6a30e9492d4a2ef64cafca1b8169fd3b878ce.jpg)  
Fig.10.4. Solution of Kuramoto-Sivashinsky equation

Fourier transform $\mathcal { F } _ { N }$ can be computed by FFT. From the fact that $U ( x , t )$ is real it follows that the sequence $u$ is hermitian, i.e., $u _ { - \jmath } = \overline { { u } } _ { \jmath }$ ．Hence, the routine REALFT from Press,Flannery, Teukolsky& Vetterling(1986,1989),Chapter 12,is best suited for computing the right-hand side of (10.11). Since $d _ { 0 } = d _ { N / 2 } = 0$ ,the components $u _ { 0 } ( t )$ and $u _ { N / 2 } ( t )$ are constant and need not be integrated. We thus are concerned with an ordinary differential equation of real dimension $N - 2 =$ 1022.As initial values we take the discrete Fourier transform of $\left\{ U ( j L / N , 0 ) \right\}$ with the $( N / 2 )$ th component put to zero. In our tests we solve the differential equation (10.11) on the interval $0 \leq t \leq 1 0 0$ (see Fig. 10.4).

It can be seen from Fig.10.5 that the Fourier modes tend to zero for $j  \infty$ ， behave chaotically, and, by computing their mean values over a long period, that the modes for $q j \approx \sqrt { 2 } / 2$ are dominant.

![](images/dbbf5fa2b0fa728b16997d9098de68a3f4c0372156f04b86381ea63bfe59df31.jpg)  
Fig.10.5. Fourier modes for Kuramoto-Sivashinsky equation

BECKDO - the Becker-Döring model describes the dynamics of a system with a large number of identical particles which can coagulate to form clusters. We let $y _ { k }$ denote the expected number of $k$ -particle clusters per unit volume. Assuming that clusters can gain or loose only single particles, we are led to the system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = - J _ { 1 } - \displaystyle \sum _ { k = 1 } ^ { N - 1 } J _ { k } , \qquad y _ { N } ^ { \prime } = J _ { N - 1 } } } \\ { { y _ { k } ^ { \prime } = J _ { k - 1 } - J _ { k } , \qquad k = 2 , 3 , \ldots , N - 1 , } } \end{array}
$$

where $J _ { k } = y _ { 1 } y _ { k } - b _ { k + 1 } y _ { k + 1 }$ and $b _ { k + 1 } = \exp \left( k ^ { 2 / 3 } - ( k - 1 ) ^ { 2 / 3 } \right)$ . For a detailed description of this system we refer to the article by Carr, Duncan & Walshaw (1995). This equation is especially interesting because of its metastability (extremely slow variations in the solution over very long time intervals; see Fig. 10.6).

![](images/e55d64b0a0471e1587715aacf370dfab2daa8de82579f8ab2c9c0307b1cdc642.jpg)  
Fig.10.6. Solutions of Becker-Doring equation (10.12)

As initial condition we take

$$
y _ { 1 } ( 0 ) = \varrho , \qquad y _ { k } ( 0 ) = 0 \qquad \mathrm { f o r } \quad k = 2 , \ldots , N
$$

(no clusters at the beginning). It can be seen by differentiation that the density (total number of particles per unit volume)

$$
\sum _ { k = 1 } ^ { N } k y _ { k } \quad ( = \varrho )
$$

is an invariant of the system (10.12). Most numerical schemes (in particular Runge-Kutta methods and multistep methods) preserve automatically such linear invariants in the absence of round-off errors. Whenever the relation (10.14) is not satisfactorily preserved, there is the possibility to re-establish it during the computations by projections (see “differential equations with invariants", Sect.VI1.2). This precautionary measure was not used in the subsequent numerical tests.

In order to be able to observe the metastable states of the system, the dimension $N$ has to be sufficiently large. Following the experiments of Carr, Duncan &

Walshaw (1995) we take $N = 5 0 0 0$ and $\varrho = 7 . 5$ , and consider the solution on the interval $0 \leq t \leq 1 0 ^ { 1 5 }$ . We compare the errors at $x _ { \mathrm { o u t } } = 1 , 1 0 , 1 0 ^ { 2 } , 1 0 ^ { 3 } , \dotsc , 1 0 ^ { 1 5 }$

The Jacobian of this system is tri-diagonal with an additional non-zero first row and a non-zero first column. A Gershgorin test reveals that its eigenvalues can not go,except for the initial phase,beyond $- 1 0$ . Stiffness, in this example,is therefore not created by large eigenvalues of $J$ , but by the extremely long integration interval.

![](images/54f99ff73ba613b31db1b279569aea337182776c9c6dd7452f70621a288b9298.jpg)  
Fig.10.7. Solution of Brusselator in 2 dimensions

BRUSS-2D-the two-dimensional Brusselator reaction-diffusion problem of Sect.

$$
\begin{array} { l } { \displaystyle \frac { \partial u } { \partial t } = 1 + u ^ { 2 } v - 4 . 4 u + \alpha \Big ( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } \Big ) + f ( x , y , t ) } \\ { \displaystyle \frac { \partial v } { \partial t } = 3 . 4 u - u ^ { 2 } v + \alpha \Big ( \frac { \partial ^ { 2 } v } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } v } { \partial y ^ { 2 } } \Big ) } \end{array}
$$

in its discretized form (II.10.14), but this time we make the problem stiff by increasing the coefficient $\alpha$ (which was 0.002） to $\alpha = 0 . 1$ and by increasing the number of grid points to $N = 1 2 8$ . This gives an ordinary differential equation of dimension $2 N ^ { 2 } = 3 2 7 6 8$ . The initial conditions, chosen here as

$$
u ( x , y , 0 ) = 2 2 \cdot y ( 1 - y ) ^ { 3 / 2 } , \qquad v ( x , y , 0 ) = 2 7 \cdot x ( 1 - x ) ^ { 3 / 2 } ,
$$

are quickly wiped out by the strong diffusion (see Fig.10.7 for $t = 1$ ), we therefore suppose that the inhomogeneity $f ( x , y , t )$ defined by

$$
f ( x , y , t ) = \left\{ \begin{array} { l l } { 5 } & { \mathrm { i f ~ } ( x - 0 . 3 ) ^ { 2 } + ( y - 0 . 6 ) ^ { 2 } \leq 0 . 1 ^ { 2 } \mathrm { ~ a n d ~ } t \geq 1 . 1 } \\ { 0 } & { \mathrm { e l s e } } \end{array} \right.
$$

models an extra addition of substance $u$ in a small disc. In order to be able to solve the linear algebra comfortably by a double FFT routine we replace the Neumann conditions of Sect.I.10 by periodic boundary conditions

$$
u ( x + 1 , y , t ) = u ( x , y , t ) , \qquad u ( x , y + 1 , t ) = u ( x , y , t ) .
$$

As output points we choose $x _ { \mathrm { o u t } } = 1 . 5$ and 11.5.

# Results and Discussion

For each of these examples we have computed very carefully the exact solution at the specified output points. Then, the above codes have been applied with many different tolerances

$$
T o l = 1 0 ^ { - 2 - m / 4 } , \qquad m = 0 , 1 , 2 , \ldots , 3 2 .
$$

More precisely, we set the relative error tolerance to be $R t o l = T o l$ and the absolute error tolerance $A t o l = 1 0 ^ { - 6 } \cdot T o$ l for the problems OREGO and ROBER, $A t o l =$ $1 0 ^ { - 4 } \cdot T o l$ for HIRES, $A t o l = 1 0 ^ { - 3 } \cdot T o l$ for PLATE and BECKDO, $A t o l = 1 . 7 \cdot 1 0 ^ { - 2 4 }$ for E5, and $A t o l = T o l$ for all other problems. Several codes returned numerical re-sults which were considerably less precise than the required precision, while other methods turned out to be more reliable. As a reasonable measure of efficiency we have therefore chosen to compare

- the actual error (a norm taken over all components and all output points) - the computing time (of a SUN Sparc 20 Workstation) in seconds.

The obtained data are then displayed as a polygonal line in a “precision-work diagram’ in double logarithmic scales. The integer-exponent tolerances $1 0 ^ { - 2 }$ ， $1 0 ^ { - 3 }$ ， $1 0 ^ { - 4 }$ ,... are displayed as enlarged symbols. The symbol for $T o l = 1 0 ^ { - 5 }$ is specially distinguished by its gray colour. The more this line is to the right, the higher was the obtained precision; the higher this line is to the top, the slower was the code. The“slope” of the curve expresses the (effective) order of the formula: lower order methods are steeper than higher order methods. The results of the above codes on the 12 test examples are displayed in Figs.10.8 and 10.9.

VDPOL,ROBER, OREGO — are very stiff problems of small dimension. We see from Fig.10.8 that the Rosenbrock code RODAS is best for low tolerances ( $1 0 ^ { - 2 }$ to $1 0 ^ { - 5 }$ ),whereas the extrapolation code SEULEX is superiour for stringent tolerances.Due to the cheapness of the function evaluations the multistep code LSODE requires in general slightly more computing time than the one-step codes. We also remark that for a given tolerance (the position of the gray symbol for $T o l = 1 0 ^ { - 5 }$ ） the code RADAU5 gives the precisest result, followed by RODAS, SEULEX，and LSODE.

HIRES -- this problem is less stiff and can also be solved by explicit methods. The computing times for the explicit code DOPRI5 are initially perfectly horizontal. This is, of course, no surprise, because the step size is restricted by stability. The (explicit, but stabilized) Runge-Kutta-Chebyshev code RKC shows a considerable improvement over DOPRI5 for low tolerances. The stiff codes are still more efficient.

E5 — is a stiff and badly scaled problem, which is integrated over a very long time. Codes cannot work correctly, if the absolute tolerance Atol is too large. The codes RODAS (for low tolerances） and RADAU5 (for $T o l \le 1 0 ^ { - 4 } $ ） give the best results. LSODE works safely only for $T o l \le 1 0 ^ { - 5 }$ ，whereas SEULEX has problems with round-off errors at high precision.

PLATE and BEAM—are both problems of the type $y ^ { \prime \prime } { = } f ( x , y , y ^ { \prime } )$ ,implemented as the first order system $y \prime = v$ ， $v ^ { \prime } = f ( x , y , v )$ . For stiff codes the linear systems to be solved have a matrix of the form

$$
\left( \begin{array} { c c } { { \alpha I } } & { { I } } \\ { { B } } & { { C } } \end{array} \right)
$$

(where $I$ is the identity matrix). Using the option IWORK $( 9 ) = 1 1 / 2$ (where $N$ is the dimension of the first order system) our codes do the first $N / 2$ elimination sweeps analytically and the dimension of the linear system is halved. Without this option, the computing times for the codes RADAU5, RODAS, and SEULEX would be larger by a factor of about 3.0, 1.7,and 2.6,respectively (these numbers are for the BEAM problem at $T o l = 1 0 ^ { - 5 }$ ). We did not include here the results of LSODE, for which we did not have an easy possibility for such a reduction. For the PLATE problem we also exploited the banded structure of $\partial f / \partial y$ and $\partial f / \partial v$ by puting ML $J \mathbb { A } \mathbb { C } { = } 1 6$ and MUJ $A C = 1 6$ .

For both problems the explicit code DOPRI5 was applicable too.A curious phenomenon arose for DOPRI5 at the PLATE problem: as expected, for low tolerance requirements $( T o l \ge 1 0 ^ { - 5 } )$ ， the code appeared to be restricted by stability， gave computing times independent of $T o l$ and issued the message “the problem seems to be stiff". But for more stringent tolerances the code was restricted by precision, with computing times unexpectedly high above those of the implicit code RADAU5. The analysis of Sect. IV.15 for the Prothero & Robinson problem (15.1） gives an explanation for this fact. We see that stiffproblems not only create loss of stability, but also loss of precision for explicit integrators.

![](images/f2d999e350d9c330cfd15705659adbb416e0b74b99f4ee984b84c8bce85e6fca.jpg)  
Fig.10.8. Work-precision diagrams for problems of dimension 2 to 80

![](images/e04af4214765435cd0dce3781292b98cb89d7410867f466504bcc057adc74322.jpg)  
Fig.10.9. Work-precision diagrams for problems of dimension 80 to 32768

Especially for the BEAM problem,a problem with expensive linear algebra, the efficiency of the codes can be considerably increased by tuning the parameters. If, for the integration with RADAU5, we put

$$
\begin{array} { l l } { { \sf W O R K ( 3 ) = 0 . 1 } } & { { \mathrm { ( J a c o b i a n ~ l e s s ~ o f t e n ~ r e c o m p u t e d ) } } } \\ { { \sf W O R K ( 4 ) = 0 . 3 } } & { { \mathrm { ( N e w t o n ~ i t e r a t i o n s ~ s t o p p e d ~ e a r l i e r ) } } } \\ { { \sf N U R K ( 5 ) = 0 . 9 9 } } & { { \mathrm { ( S t e p ~ s i z e ~ c h a n g e d ~ l e s s ~ o f t e n , } } } \\ { { \sf W O R K ( 6 ) = 2 . } } & { { \mathrm { d e c r e a s i n g ~ n u m b e r ~ o f ~ L U \mathrm { - } d e c o m p o s i t i o n s . } } } \end{array}
$$

then the computing time decreases by a factor between 2 and 5. Fig.10.9 shows the spectacular improvement of this “tuned" run.

CUSP — the Jacobian of this problem is of the form

$$
J = \left( \begin{array} { c c c c } { { A _ { 1 } } } & { { B _ { 1 } } } & { { } } & { { D _ { 1 } } } \\ { { C _ { 2 } } } & { { A _ { 2 } } } & { { \ddots } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { B _ { N - 1 } } } \\ { { D _ { N } } } & { { } } & { { C _ { N } } } & { { A _ { N } } } \end{array} \right)
$$

where $A _ { \ i _ { 2 } } , B _ { \ i } , C _ { \ i } , D _ { \ i }$ are $3 \times 3$ matrices,and an efficient solution of the linear system needs a special treatment (see Exercise 1). However the considered methods, with the exception of the Rosenbrock methods, do not require an exact Jacobian. Therefore,an easy possibility for a considerable reduction of computing time is simply to use the codes in the banded version by putting $M I = M U = 3$ The $D _ { 1 }$ and $D _ { N }$ are neglected and we obtain the computing times displayed in Fig.10.9. If the Jacobian were treated as a full matrix, the computing times would increase by a factor of 8.3, 6.6,and 4.8 for the codes RADAU5, SEULEX, and LSODE, respectively (these numbers are for $T o l = 1 0 ^ { - 5 }$ ). The explicit code RKC gives excellent results for low precision, whereas the results of DOPRI5 (more than 30 seconds) are outside of the picture.

BRUSS - for this one-dimensional reaction-diffusion problem the linear algebra is done in the “banded” version with “analytical Jacobian". The problem is very stiff (large diffusion constant and small $\Delta x )$ and an explicit method, such as DO-PRI5,would require close to 600o0 steps of integration. The code RKC works well, although less efficiently than the stiff integrators.

KS 一 the solution of this problem is sensitive with respect to changes in the initial values,a phenomenon already encountered in the LRNZ problem of Sect. I.10. Similarly as there, the precision increases only for $T o l$ beyond a certain threshold. The Jacobian of this problem is full. Numerical experiments revealed that the codes worked best when the Jacobian is replaced by a diagonal matrix with $( q j ) ^ { 2 } - ( q j ) ^ { 4 }$ in its $j$ th entry. Rosenbrock methods,which require an exact Jacobian,are not efficient here. The explicit codes RKC and DOPRI5 need too much computing time.

BECKDO- for this problem,the stiff codes (the only ones which work) require the solution of linear systems of the form

$$
\left( \begin{array} { c c } { { u } } & { { v ^ { T } } } \\ { { w } } & { { T } } \end{array} \right) \left( \begin{array} { l } { { x } } \\ { { y } } \end{array} \right) = \left( \begin{array} { l } { { a } } \\ { { b } } \end{array} \right) ,
$$

where $v , w , b$ are $( n - 1 )$ -dimensional vectors and $T$ is a tri-diagonal matrix. Since the linear algebra routines are completely separated from the codes RADAU5, RODAS and SEULEX, it is easy to replace these routines by a special program which solves (10.19) efficiently as follows

$$
\begin{array} { r l } & { x = \left( a - v ^ { T } T ^ { - 1 } b \right) / \left( u - v ^ { T } T ^ { - 1 } w \right) } \\ & { y = T ^ { - 1 } b - x T ^ { - 1 } w . } \end{array}
$$

It is not necessary to alter the stiff integrator itself.

Fig.10.9 shows that, as usual, RODAS is best for low tolerances and RADAU5 is preferable for high precision. Not as usual is the fact that RODAS performs very badly for stringent tolerances. We explain this by the fact that the linear system (10.19) is sensitive to round-off errors, or, as Wilkinson would turn it, delivers a solution for a wrong Jacobian. Thus, the order of the Rosenbrock method drops to 1.

BRUSS-2D — due to its large dimension ( $' n = 2 \cdot 1 2 8 ^ { 2 } = 3 2 7 6 8 \rangle$ ，this problem makes no sense in full or even banded linear algebra. We therefore solved the linear equations (in the codes with separated linear algebra, see the corresponding remarks in the BECKDO problem) by FFT methods, taking into account only the(stiff) diffusion terms and neglecting the (in this problem non-stiff) reaction terms. The FFT codes used were those of Press,Flannery, Teukolsky & Vetterling (1986,1989) in the chapter on partial differential equations. A special advantage of the Radau method is here that the complex algebra, which is anyway used in FFT, crunches the complex eigenvalues of the Runge-Kutta matrix without further harm.

For this problem, which is a typical parabolic partial differential equation with non-stiff nonlinearities, we have made a detailed comparison of the performances of the implicit code RADAU5, the “stabilized’ explicit code RKC,and the explicit code DOPRI5, in dependence of the discretization parameter $\Delta x = \Delta y = 1 / N$ and the diffusion parameter $\alpha$ (see Eqs.(10.15) and (II.10.14)). The results (number of function calls and computing times) are displayed in Table 10.1, where the best performances are displayed in boldface characters. We can see how the olympic fire goes over from DOPRI5, which is best for low stiffness $( \alpha N ^ { 2 } \le 1 )$ , by increasing the stiffness first to RKC,and then (for $\alpha N ^ { 2 } \geq 1 0 0 0 )$ to the implicit RADAU5 code. We also observe that the number of function evaluations is nearly independent of the stiffness for RADAU5, behaves like $C o n s t \cdot \sqrt { \alpha } \cdot N$ for RKC, and like Const · $\alpha \cdot N ^ { 2 }$ for DOPRI5.

Comparisons Between Codes of the Same Type. Figs.10.8 and 10.9, which are a sort of “Final Competition of Wimbledon”, contain only one code from each class of integration methods (Radau methods, Implicit Runge-Kutta, Rosenbrock, and extrapolation methods). Following are some comparisons within each of these classes.

Table 10.1. Function evaluations / computing times at $T o l = 1 0 ^ { - 5 }$   

<table><tr><td rowspan=1 colspan=1>RADAU5</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N = 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N = 128</td><td rowspan=1 colspan=1>N = 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α=10-2α = 10-1α=1</td><td rowspan=1 colspan=1>3372/19.81286/7.71150/6.81195/7.8</td><td rowspan=1 colspan=1>3233/84.91322/36.21131/30.91199/33.0</td><td rowspan=1 colspan=1>3271/413.51295/167.41227/172.31247/177.3</td><td rowspan=1 colspan=1>3290/2215.61381/868.81173/854.91242/945.9</td><td rowspan=1 colspan=1>3261/14902.11380/6459.31204/5664.91258/5961.2</td></tr><tr><td rowspan=1 colspan=1>RKC</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N= 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N= 128</td><td rowspan=1 colspan=1>N = 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α = 10-2α = 10-1α=1</td><td rowspan=1 colspan=1>2367/4.71661/3.21899/3.64013/7.2</td><td rowspan=1 colspan=1>2277/18.61674/13.82823/22.57565/58.9</td><td rowspan=1 colspan=1>2249/76.32078/70.45047/176.814631/503.4</td><td rowspan=1 colspan=1>2311/352.53379/511.59666/1446.229022/4328.8</td><td rowspan=1 colspan=1>2911/1912.06259/4086.918911/12312.2</td></tr><tr><td rowspan=1 colspan=1>DOPRI5</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N= 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N= 128</td><td rowspan=1 colspan=1>N= 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α =10-2α =10-1α=1</td><td rowspan=1 colspan=1>976/2.0784/1.64366/9.042832/90.6</td><td rowspan=1 colspan=1>1030/8.51894/15.417176/145.5171010/1505.8</td><td rowspan=1 colspan=1>1408/48.56976/240.668446/2419.7683836/24362.7</td><td rowspan=1 colspan=1>3286/509.427478/4369.6273568/43982.2</td><td rowspan=1 colspan=1>11464/7704.2</td></tr></table>

Radau Methods. For a comparison of Radau methods of various orders (see also the results of Reymond (1989) in the first edition), we have written a code RADAUP, which allows to choose with the help of a method flag IWORK $( 1 1 ) = 3$ ,5,7 to choose between $s = 3 , 5$ ， or 7 (i.e., between orders $p = 5 , 9$ ，or 13). The code is for $s = 3$ mathematically equivalent to RADAU5, but, due to a different coding, slightly slower. We can see in Fig.10.1O how the higher order pays off for higher precision,but for lower precision arise problems due to large step sizes and bad convergence of the Newton iterations.

Implicit Runge-Kutta Methods. It has for a long time been taken for granted that only DIRK and SDIRK methods could be implemented efficiently. Our experience shows that the diagonally implicit method SDIRK4, constructed in Section IV.6, gives rather disappointing results (see Fig. 10.11). An exception is the BEAM problem with its, microscopically, highly oscillatory solutions. Since the code SDIRK4 has not the option for “second order" linear algebra, we have also applied RADAU5 without this option. The computing times for RADAU5 are therefore not the same as in Fig. 10.9.

Rosenbrock Methods. There is usually not much difference between the performance of the different Rosenbrock methods (see Fig.10.12). In spite of their larger number of stages, the codes RODAs5 (order 5）and RODAS (order 4） give often the best results. Among the 4th order “classical” Rosenbrok methods of Table 7.2 the best is in general “method $2 ^ { \mathfrak { s } }$ with its small error constant; it fails completely, however,on the Beam problem due to lack of $A$ -stability."Method $6 ^ { \circ }$ corresponds to the choice of coefficients which give an $L$ -stable method.

![](images/00071c3ad6adbf6d7ceb2eb3e95c867f522a2d39ba25c2e7ab4b9ef3ecaa9819.jpg)  
Fig.10.10. Comparison between Radau codes

![](images/daea7d9e0c3af3b391e0bcc9bffc40c15ca246d94dc8c61da17be46c93f0432f.jpg)  
Fig.10.11. Comparison between implicit Runge-Kutta codes

![](images/15ec86b0617ac9571ee934b3d0048a3a2420e8a7b2d7d14f560bd3b8b9ddae53.jpg)  
Fig.10.12. Comparison between Rosenbrock codes

![](images/7ee35b4010c72ed892ebceb686a228335deb5718da721e6dd655db0e4a501aef.jpg)  
Fig.10.13. Comparison between extrapolation codes

Extrapolation Methods. The code SODEX,which is based on an $h ^ { 2 }$ -extrapolation of the semi-implicit midpoint rule, is clearly superiour to SEULEX for low precision (see Fig.10.13). The opposite situation appears for more stringent tolerances; here we observe an order reduction phenomenon, which is explained in Sect. VI.5 below. We have also included in these tests the results of the code EULSIM by Deuflhard, Novak&Poehle (poehle $@$ sc.zib-berlin.de) which is another implementation of the extrapolated semi-implicit Euler method, with a different stepsize sequence.

Chebyshev Methods. During the final realization of these experiments we have received a code DUMKA3 (written by A. Medovikov, nucrect $@$ inm.ras.ru) which implements an extension of the optimal Chebyshev methods of Lebedev (see Sect. IV.2) to third order. This code is still in a very experimental stage,but the results, presented in Fig. 10.14, are very promising.

![](images/6f23601cde27d38e3ee525461a4e83a22cba36ebb864dc456cef0ab8ce1dcc80.jpg)  
Fig.10.14. Comparison between Chebyshev codes and RADAU5

# Partitioning and Projection Methods

Most codes for solving stiff systems ... spend most of their time solving systems of linear equations ...

(Watkins & HansonSmith 1983)

Further spectacular reductions of the work for the linear algebra are often possible. One of the oldest ideas is to partition a stiff system into a (hopefully) small stiff system and a large nonstiff part,

$$
\begin{array} { l l } { { { y } _ { a } ^ { \prime } = f _ { a } \left( y _ { a } , y _ { b } \right) \quad \quad } } & { { ( \mathrm { s t i f f } ) } } \\ { { { y } _ { b } ^ { \prime } = f _ { b } \left( y _ { a } , y _ { b } \right) \quad \quad } } & { { ( \mathrm { n o n s t i f f } ) , } } \end{array}
$$

so that the two systems can be treated by two different methods, one implicit and the other explicit (e.g. Hofer 1976). The theory of $P$ -series in Sect.II.14 had its origin in the study of the order properties of such methods. A difficulty of this approach is,of course,to decide which equations should be the stiff ones. Further, stiffness may affect subspaces which are not parallel to the coordinate axes. We shall therefore turn our attention to procedures which do not adapt the underlying numerical method to the partitioning,but the linear algebra only. An excellent survey of the older literature on these methods is given by Soderlind (1981). The following definition describes an especially promising class of problems:

Definition10.1 (Bjorck 1983,1984). The system $y ^ { \prime } = f ( x , y )$ is called separably stiff at a position $x _ { 0 } , y _ { 0 }$ if the Jacobian $\begin{array} { r } { \dot { J _ { \mathrm { ~ } } } = \frac { \partial f } { \partial y } ( \bar { x } _ { 0 } , y _ { 0 } ) } \end{array}$ possesses $k < n$ eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ such that

$$
\operatorname* { m i n } _ { 1 \leq i \leq k } | \lambda _ { \iota } | > > \operatorname* { m a x } _ { k + 1 \leq i \leq n } | \lambda _ { i } | .
$$

The eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ are called the stiff eigenvalues and

$$
\mu = \operatorname* { m i n } _ { 1 \leq i \leq k } | \lambda _ { i } | { \bf \mu } / \operatorname* { m a x } _ { k + 1 \leq \imath \leq n } | \lambda _ { i } |
$$

the relative separation. The space $D$ spanned by the $^ { s t }$ iff eigenvectors is called the dominant invariant subspace.

For example, the Robertson problem (10.2) possesses only one stiff eigenvalue (close to -20oO),and is therefore separably stiff with $k = 1$ . The CUSP problem (10.8'）of dimension 96 has 32 large eigenvalues which range,except for transient phases,between $- 2 0 0 0 0$ and -6oooo.All other eigenvalues satisfy approximately $| \lambda | < 3 0$ ． This problem is,in fact,a singular perturbation problem (see Sect.VI.1),and such problems are all separably stiff. The other large problems of this section have eigenvalues scattered all around. A.R. Curtis' study (1983) points out that in practical problems separably stiff problems are rather seldom.

The Method of Gear and Saad. Implicit methods such as (transformed) Runge-Kutta or multistep formulas require the solution of a linear system (where we denote,as usual in linear algebra, the unknown vector by $x$ ）

$$
A x = b \qquad { \mathrm { w h e r e } } \qquad A = { \frac { 1 } { h \gamma } } I - J
$$

with residual $r = b - A x$ . We choose $k$ (usually) orthogonal vectors $q _ { 1 } , \ldots , q _ { k }$ in such a way that the span $\{ q _ { 1 } , \dots , q _ { k } \} = \widetilde { \cal D }$ is an approximation to the dominant subspace $D$ , and denote by $Q$ the $k \times n$ -matrix formed by the columns $q _ { j }$ ，

$$
Q = ( q _ { 1 } , \dots , q _ { k } ) .
$$

There are now several possibilities for replacing the solution $x$ of (10.23) by an approximate solution $\bar { \tilde { x } _ { \mathrm { \ell } } } \in \tilde { D }$ . One of the most natural is to require (Saad 1981, Gear & Saad 1983; in fact,Galerkin 1915) that the residual of $\widetilde { x }$ ，

$$
\widetilde { r } = b - A \widetilde { x } = A ( x - \widetilde { x } ) ,
$$

be orthogonal to $\widetilde { D }$ , i.e., that $Q ^ { T } ( b - A \widetilde { x } ) = 0$ . If we write $\widetilde { x }$ in the basis of (10.24) as $\widetilde { x } = Q \widetilde { y }$ , this yields

$$
\begin{array} { r } { H \widetilde { y } = Q ^ { T } b , } \end{array}
$$

where

$$
H = Q ^ { T } A Q \qquad \mathrm { o r } \qquad Q H = A Q ,
$$

which means that we have to solve a linear system of dimension $k$ with matrix $H$ . A particularly good choice for $\widetilde { D }$ is a Krylov subspace spanned by an arbitrary vector $r _ { 0 }$ (usually the residual of a well chosen initial approximation $x _ { 0 }$ ），

$$
{ \widetilde D } = \operatorname { s p a n } \{ r _ { 0 } , A r _ { 0 } , A ^ { 2 } r _ { 0 } , \ldots , A ^ { k - 1 } r _ { 0 } \} .
$$

The vectors (10.28) constitute the sequence created by the well-known power me-thod. Therefore, in the case of a separably stiff system, as analyzed by D.J. Higham (1989), the space $\widetilde { D }$ approaches the space $D$ extremely well as soon as its dimension is sufficiently high. In the Arnoldi process (Arnoldi 1951) the vectors of (10.28) are successively orthonormalized (Gram-Schmidt) as

$$
\begin{array} { r l r l } & { q _ { 1 } = r _ { 0 } / \Vert r _ { 0 } \Vert } \\ & { \widehat { q } _ { 2 } = A q _ { 1 } - h _ { 1 1 } q _ { 1 } , } & & { q _ { 2 } = \widehat { q } _ { 2 } / h _ { 2 1 } \quad \mathrm { w i t h } \quad h _ { 2 1 } = \Vert \widehat { q } _ { 2 } \Vert } \end{array}
$$

and so on,and we see that

$$
\begin{array} { l } { { A q _ { 1 } = h _ { 2 1 } q _ { 2 } + h _ { 1 1 } q _ { 1 } } } \\ { { A q _ { 2 } = h _ { 3 2 } q _ { 3 } + h _ { 2 2 } q _ { 2 } + h _ { 1 2 } q _ { 1 } } } \\ { { \ldots } } \end{array}
$$

which,compared to (10.28),shows that $H$ is Hessenberg. For $A$ symmetric, $H$ is also symmetric, hence tridiagonal, so that the method is equivalent to the conjugate gradient method.

Two features are important for this method: Firstly, the matrix $A$ need never be computed nor stored. All that is needed are the matrix-vector multiplications in (10.29),which can be obtained from the “directional derivative"

$$
J v \approx [ f ( x , y + \delta v ) - f ( x , y ) ] / \delta .
$$

Several people therefore call such methods “matrix-free". Secondly, the dimension $k$ does not have to be known: one simply computes one column of $H$ after the other and periodically estimates the residual. As soon as this estimate is small enough (or $k$ becomes too large) the algorithm stops. We also mention two variants of the method:

1. (Gear & Saad 1983, p. 595). Before starting the computation of the Krylov subspace, perform some initial iteration of the power method on the initial vector $r _ { 0 }$ ,using either the matrix $A$ or the matrix $J$ . Lopez & Trigiante （1989) report excellent numerical results for this procedure.

2. Incomplete Orthogonalization (Saad 1982). The new vector $A q _ { \jmath }$ is only orthogonalized against the previous $p$ vectors, where $p$ is some small integer. This makes $H$ a banded matrix and saves computing time and memory. For symmetric matrices, the ideal choice is of course $p = 2$ , for matrices more and more unsymmetric $p$ usually is increased to 10 or 15.

The EKBWH-Method (this tongue-twister stands for Enright, Kamel, Bjorck, Watkins and HansonSmith). Here, the matrices $A$ (and $J$ ) in (10.23)are replaced by approximations

$$
\stackrel { \sim } { A } = \frac { 1 } { h \gamma } I - \stackrel { \sim } { J }
$$

where $\widetilde { J }$ should approach $J$ suficiently well and the matrix $\widetilde { A }$ be relatively easy to invert. $\widetilde { J }$ is determined as follows: Complete (theoretically) the vectors (10.24) to an orthogonal basis $( Q , { \widehat { Q } } )$ of $\mathbb { R } ^ { n }$ . In the new basis $J$ becomes

$$
\left( { \begin{array} { l } { Q ^ { T } } \\ { { \widehat { Q } } ^ { T } } \end{array} } \right) J \left( Q , { \widehat { Q } } \right) = \left( { \begin{array} { l l } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { T _ { 2 1 } } & { T _ { 2 2 } } \end{array} } \right)
$$

and we have

$$
Q ^ { T } J Q = T _ { 1 1 } .
$$

If span $Q = \widetilde { D }$ approaches $D$ , then $T _ { 1 1 }$ will contain the stiff eigenvalues and $T _ { 2 1 }$ will tend to zero. If $\widetilde { D } = D$ exactly, then $T _ { 2 1 } = 0$ and (10.32) is a block-Schur decomposition of $J$ . For separably stiff systems $\| T _ { 2 2 } \|$ will become small compared to $( h \gamma ) ^ { - 1 }$ and we define

$$
\widetilde { J } = ( Q , \widehat { Q } ) \left( \begin{array} { c c } { { T _ { 1 1 } } } & { { T _ { 1 2 } } } \\ { { 0 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { Q ^ { T } } } \\ { { \widehat { Q } ^ { T } } } \end{array} \right) = Q ( T _ { 1 1 } Q ^ { T } + T _ { 1 2 } \widehat { Q } ^ { T } ) \stackrel { ( 1 0 . 3 2 ) } { = } Q Q ^ { T } J .
$$

This shows $\widetilde { J }$ to be the orthogonal projection of $J$ onto $\widetilde { D }$ . The inverse of $\widetilde { A }$ is computed by developing $( I - B ) ^ { - 1 } = I + B + B ^ { 2 } + \dots .$ as a geometric series

$$
\begin{array} { r l } & { \widetilde { A } ^ { - 1 } = h \gamma \big ( I - h \gamma Q Q ^ { T } J \big ) ^ { - 1 } } \\ & { \quad \quad = h \gamma \big ( I + h \gamma Q Q ^ { T } J + h ^ { 2 } \gamma ^ { 2 } Q \underbrace { Q ^ { T } J Q } _ { T _ { 1 1 } } Q ^ { T } J + \dots \big ) } \\ & { \quad \quad = h \gamma \big ( I + Q ( h \gamma I + h ^ { 2 } \gamma ^ { 2 } T _ { 1 1 } + h ^ { 3 } \gamma ^ { 3 } T _ { 1 1 } ^ { 2 } + \dots ) Q ^ { T } J \big ) } \\ & { \quad \quad = h \gamma \big ( I + Q \big ( \frac { 1 } { h \gamma } I - T _ { 1 1 } \big ) ^ { - 1 } Q ^ { T } J \big ) } \end{array}
$$

which only requires the solution of the “small” system with matrix $\left( I / h \gamma - T _ { 1 1 } \right)$ (the last expression is called the Sherman-Morrison-Woodbury formula).

Choice of $Q$ ：

-Björck(1983) computes the precise span of $D$ , by Householder transforms followed by block- $Q R$ iterations. For separably stiff systems the block $T _ { 2 1 }$ converges to zero linearly with ratio $\mu ^ { - 1 }$ so that usually 2 or 3 iterations are sufficient. A disadvantage of the method is that an estimate for the dimension $k$ of $D$ must be known in advance.

-Enright & Kamel（1979) transform $J$ to Hessenberg form and stop the transformations when $\| T _ { 2 1 } \| + \| T _ { 2 2 } \|$ become suficiently smal (remark that $T _ { 2 1 }$ is non zero in its last column only). Thus the dimension $k$ can be discovered dynamically. Enright & Kamel combine the Householder reflexions with a pivoting strategy and repeated row & column permutations in order to make $T _ { 2 2 }$ small as fast as possible. It was first observed numerically (by Carlsson) and then shown theoretically (Soderlind 1981) that this pivoting strategy “needs some comments": if we start from (10.32),by knowing that

$$
\left( \begin{array} { c c } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { T _ { 2 1 } } & { T _ { 2 2 } } \end{array} \right)
$$

is Hessenberg in its frst $k$ columns, (with $h _ { 2 1 } \neq 0 , h _ { 3 2 } \neq 0 , \ldots )$ and do the analysis of formulas (10.29) backwards,we see that the space $\widetilde { D }$ for the Enright & Kamel method is a Krylov subspace created by $q _ { 1 }$ (D.J. Higham 1989). Thus only the first permutation influences the result.

- Watkins & HansonSmith (1983) start from an arbitrary $Q ^ { ( 0 ) }$ followed by several steps of the block power method

$$
J Q ^ { ( \imath ) } = Q ^ { ( \imath + 1 ) } R ^ { ( \imath + 1 ) }
$$

where $R ^ { ( i + 1 ) }$ re-orthogonalizes the vectors of the product $J Q ^ { ( \imath ) }$ . A great advantage of this procedure is that no large matrix needs to be computed nor stored. The formulas (10.35) as well as (10.34) only contain matrix-vector products which are computed by (10.30). The disadvantage is that the dimension of the space must be known.

Stopping Criteria. The above methods need a criterion on the goodness of the approximation $\widetilde { J }$ to decide whether the dimension $k$ is sufficient. Suppose that we solve the linear equation (10.23) by a modified Newton correction which uses $\tilde { A }$ as “approximate Jacobian"

$$
\widetilde { x } = x _ { 0 } + \widetilde { A } ^ { - 1 } \big ( b - A x _ { 0 } \big ) ,
$$

then the convergence of this iteration is governed by the condition

$$
\varrho \big ( I - \widetilde { A } ^ { - 1 } A \big ) = \varrho \big ( \widetilde { A } ^ { - 1 } \big ( \widetilde { A } - A \big ) \big ) = \varrho \big ( \widetilde { A } ^ { - 1 } \big ( J - \widetilde { J } \big ) \big ) < 1 .
$$

A reasonable condition is therefore that the spectral radius $\varrho$ of $\widetilde { A } ^ { - 1 } ( J - \widetilde { J } )$ is plainly smaller than 1. Let us compute this value for the Bjork method ( $( T _ { 2 1 } = 0$ ： since the eigenvalues of a matrix $C$ are invariant under the similarity transforma-

tion $T ^ { - 1 } C T$ , we have

$$
\begin{array} { r l } & { \varrho \left( \widetilde { A } ^ { - 1 } ( J - \widetilde { J } ) \right) = \varrho \left( \left( \frac { 1 } { h \gamma } I - \left( \begin{array} { c c } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \right) ^ { - 1 } \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { T _ { 2 2 } } \end{array} \right) \right) } \\ & { \qquad = \varrho \left( \left( \begin{array} { c c } { \left( \frac { 1 } { h \gamma } I - T _ { 1 1 } \right) ^ { - 1 } } & { \times \times \times } \\ { 0 } & { h \gamma I } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { T _ { 2 2 } } \end{array} \right) \right) } \\ & { \qquad = \varrho \left( \left( \begin{array} { c c } { 0 } & { \times \times } \\ { 0 } & { h \gamma T _ { 2 2 } } \end{array} \right) \right) = \varrho ( h \gamma T _ { 2 2 } ) . } \end{array}
$$

In practice, a condition of the form

$$
\| h \gamma T _ { 2 2 } \| < 1 ,
$$

where $\| \cdot \|$ is usually the Frobenius norm $\sqrt { \sum _ { i , j } a _ { \iota j } ^ { 2 } }$ , ensures a reasoable rte f convergence. For an analogous condition in the Enright-Kamel case see Exercise 3 below.

# Exercises

1. (The red-black reduction). The Jacobian matrix of the (periodic) cusp catastrophe model (10.8’) is of the form

$$
\left( \begin{array} { c c c c c } { { A _ { 1 } } } & { { B _ { 1 } } } & { { } } & { { } } & { { C _ { 1 } } } \\ { { C _ { 2 } } } & { { A _ { 2 } } } & { { B _ { 2 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { C _ { 2 m - 1 } } } & { { A _ { 2 m - 1 } } } & { { B _ { 2 m - 1 } } } \\ { { B _ { 2 m } } } & { { } } & { { C _ { 2 m } } } & { { A _ { 2 m } } } \end{array} \right)
$$

where $A _ { \imath } , B _ { \imath } , C _ { \imath }$ are $( 3 \times 3 )$ -matrices. Write a solver which solves linear equations with matrix (10.38） using the “red-black ordering reduction". This means that $A _ { 1 } , A _ { 3 } , A _ { 5 } , \dotsc .$ are used as (matricial） pivots to eliminate $C _ { 2 } , C _ { 4 } , \ldots , B _ { 2 } , B _ { 4 } , \ldots$ aboveand belowbyGaussanblock-elimination.Then the resulting system is again of the same structure as (10.38) with halved dimension. If the original system's dimension contains $2 ^ { k }$ as prime factor, this process can be iterated $k$ times. Study the increase of performance which this algorithm allows for the RADAU5 and Rosenbrock codes on model (10.8'). The algorithm is also highly parallelizable.

2. Show by numerical experiments that the circular nerve (10.8') loses its limit cycle when the diffusion coefficient $D$ becomes either too smal (the message does not go across the water fall) or too large (the limit cycle then melts down across the origin).

3.(Stopping criterion for Enright & Kamel method; D.J. Higham 1989). Suppose that the matrix $J$ has been transformed to partial Hessenberg form (see

$$
\left( { \big { \underset { Q ^ { T } } { Q ^ { T } } } } \right) J ( Q , { \widehat { Q } } ) = { \overset { k } { _ { n - k } } } \left( { \begin{array} { l l } { k } & { n - k } \\ { H } & { T _ { 1 2 } } \\ { ( 0 ~ b ) } & { T _ { 2 2 } } \end{array} } \right)
$$

where $H$ is upper Hessenberg and $b$ a column vector. Show that the criterion (10.36) then becomes

$$
\varrho ( h \gamma B ) < 1
$$

where

$$
B = \begin{array} { l r } { { k } } & { { k - 1 } } & { { 1 + n - k } } \\ { { n - k } } & { { \left( \begin{array} { l r } { { 0 } } & { { - h \gamma \overline { { { H } } } ^ { - 1 } T _ { 1 2 } \bigl ( b T _ { 2 2 } \bigr ) } } \\ { { 0 } } & { { \left( b T _ { 2 2 } \right) } } \end{array} \right) } } \end{array}
$$

with $\overline { { H } } = \left( I - h \gamma H \right)$ . Since $\varrho ( B )$ is the same as the spectral radius of its lower $1 + n - k$ by $1 + n - k$ principal submatrix,a sufficient condition for convergence is

$$
 { | h \gamma | } \sqrt {  { | | T _ { 2 2 } | | ^ { 2 } } +  { | | b | | ^ { 2 } } +  { | | y | | ^ { 2 } } } < 1
$$

where $y ^ { T }$ is the $k$ -th row of the matrix $- h \gamma \overline { { H } } ^ { - 1 } T _ { 1 2 } ( b T _ { 2 2 } )$

# IV.11 Contractivity for Linear Problems

He who loves practice without theory is like the sailor who boards ship without a rudder and compass and never knows where he may be cast. (Leonardo da Vinci 1452-1519, cited from M. Kline,Mathematical Thought .. 1972,p. 224)

The stability analysis of the preceeding sections is based on the transformation of the Jacobian $J \approx \partial f / \partial y$ to diagonal form (see Formulas (2.5),(2.6) of Sect.IV.2). Especially for large-dimensional problems, however, the matrix which performs this transformation may be badly conditioned and destroy all the nice estimations which have been obtained.

Example 11.1. The discretization of the hyperbolic problem

$$
{ \frac { \partial u } { \partial t } } = { \frac { \partial u } { \partial x } }
$$

by the method of lines leads to

$$
y ^ { \prime } = A y , \qquad A = \lambda \left( \begin{array} { c c c c c } { { - 1 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } \end{array} \right) , \qquad \lambda = \frac { 1 } { \Delta x } > 0 .
$$

This matrix has all eigenvalues at $- \lambda$ and the above spectral stability analysis would indicate fast asymptotic convergence to zero. But neither the solution of (11.1)，which just represents a travelling wave, nor the solution of (11.2), if the dimension becomes large,have this property. So our interest in this section is to obtain rigorous bounds for the numerical solution (see (2.3))

$$
y _ { m + 1 } = R ( h A ) y _ { m }
$$

in different norms of $\mathbb { R } ^ { n }$ or $\mathbb { C } ^ { n }$ . Here $R ( z )$ represents the stability function of the method employed. We have from (11.3)

$$
\| y _ { m + 1 } \| \leq \| R ( h A ) \| \cdot \| y _ { m } \|
$$

(see Volume I, Sect.I.9,Formula (9.10)),and contractivity is assured if

$$
\| R ( h A ) \| \leq 1 .
$$

# Euclidean Norms (Theorem of von Neumann)

People in mathematics and science should be reminded that many of the things we take for granted today owe their birth to perhaps one of the most brilliant people of the twentieth century — John von Neumann.

(John Impagliazzo, quoted from SIAM News September 1988)

Let the considered norm be Euclidean with the corresponding scalar product denoted by $\langle \cdot , \cdot \rangle$ . Then, for the solution of $y ^ { \prime } = A y$ we have

$$
{ \frac { d } { d x } } \| y \| ^ { 2 } = { \frac { d } { d x } } \langle y , y \rangle = 2 \mathrm { R e } \langle y , y ^ { \prime } \rangle = 2 \mathrm { R e } \langle y , A y \rangle ,
$$

hence the solutions are decaying in this norm if

$$
\operatorname { R e } \left. y , A y \right. \leq 0 \quad { \mathrm { f o r ~ a l l } } \quad y \in \mathbb { C } ^ { n } .
$$

This result is related to Theorem 10.6 of Sect.I.10, because

$$
\mathrm { R e } \left. y , A y \right. \leq \mu _ { 2 } ( A ) \left\| y \right\| ^ { 2 } ,
$$

where $\mu _ { 2 } ( A )$ is the logarithmic norm of $A$ (Eq. (10.20) of Sect.I.10).

Theorem 11.2. Let the rational function $R ( z )$ be bounded for Re $z \le 0$ and assume that the matrix $A$ satisfies (11.6). Then, in the matrix norm corresponding to the scalar product we have

$$
\| R ( A ) \| \leq \operatorname* { s u p } _ { \operatorname { R e } z \leq 0 } | R ( z ) | .
$$

Remark. This is a finite-dimensional version of a result of J. von Neumann (1951). A short proof is given in Hairer,Bader & Lubich (1982). The idea of the following proof is due to M. Crouzeix (unpublished).

Proof. a) Normal matrices can be transformed to diagonal form by a unitary matrix $Q$ (see Exercise 3 of Section I.12). Hence, $A = Q D Q ^ { * }$ ，where $D =$ diag $\{ \lambda _ { 1 } , \ldots , \lambda _ { n } \}$ . In this case we have

$$
\| R ( A ) \| = \| Q R ( D ) Q ^ { * } \| = \| R ( D ) \| = \operatorname* { m a x } _ { \iota = 1 , \ldots , n } | R ( \lambda _ { \iota } ) | ,
$$

ind (11.8) follows from (11.6), because the eigenvalues of $A$ satisfy $\mathrm { R e } \lambda _ { \imath } \leq 0$

b) For a general $A$ we consider the matrix function

$$
A ( \omega ) = \frac { \omega } { 2 } ( A + A ^ { * } ) + \frac { 1 } { 2 } ( A - A ^ { * } ) .
$$

We see from the identity

$$
\langle v , A ( \omega ) v \rangle = \omega \mathrm { R e } \langle v , A v \rangle + i \operatorname { I m } \langle v , A v \rangle
$$

that $A ( \omega )$ satisfies (11.6) for all $\omega$ with $\mathrm { R e } \omega \geq 0$ , so that also the eigenvalues of $A ( \omega )$ satisfy $\operatorname { R e } \lambda ( \omega ) \leq 0$ for $\mathrm { R e } \omega \geq 0$ . Therefore, the rational function

$$
\varphi ( \omega ) = \langle u , R ( A ( \omega ) ) v \rangle
$$

$( u , v$ fixed) has no poles in $\operatorname { R e } \omega \geq 0$ . Using $A ( 1 ) = A$ we obtain from the maximum principle that

$$
\begin{array} { r l } { \langle u , R ( A ) v \rangle = \displaystyle \varphi ( 1 ) \le \operatorname* { s u p } _ { y \in \mathbb R } \varphi ( i y ) \le \operatorname* { s u p } _ { y \in \mathbb R } \| R ( A ( i y ) ) \| \| u \| \| v \| } & { } \\ { \le \displaystyle \operatorname* { s u p } _ { \tiny \mathrm { R e } ~ z \le 0 } | R ( z ) | \| u \| \| v \| . } & { } \end{array}
$$

The last inequality of (11.9) follows from part (a), because $A ( i y )$ is a normal matrix (i.e., $A ( i y ) A ( i y ) ^ { * } = A ( i y ) ^ { * } A ( i y ) )$ . Formula (11.8) is now an immediate consequence of (11.9) and of the fact that $\begin{array} { r } { \| C \| = \operatorname* { s u p } _ { \| u \| \leq 1 , \| v \| \leq 1 } \left. u , C v \right. } \end{array}$ □

Corollary 11.3. If the rational function $R ( z )$ is $A$ -stable, then the numerical solution $y _ { n + 1 } = R ( h A ) y _ { n }$ is contractive in the Euclidean norm $\left( i . e . , \ \left. y _ { n + 1 } \right. \leq \right.$ $| | y _ { n }  | $ ,whenever (1l.6) is satisfied.

Proof. $A$ -stability implies that $\operatorname* { m a x } _ { \mathrm { R e } z \leq 0 } | R ( z ) | \leq 1$

Corollary 11.4. If $a$ matrix $A$ satisfies $\operatorname { R e } \langle v , A v \rangle \leq \nu \| v \| ^ { 2 }$ for all $v \in \mathbb { C } ^ { n }$ ,then

$$
\| R ( A ) \| \leq \operatorname* { s u p } _ { \operatorname { R e } z \leq \nu } | R ( z ) | .
$$

Proof. Apply Theorem 11.2 to $\widetilde { R } ( z ) = R ( z + \nu )$ and $\widetilde { A } = A - \nu I$

# Error Growth Function for Linear Problems

Guided by the above estimate, we define

$$
\varphi _ { R } ( x ) : = \operatorname* { s u p } _ { \operatorname { R e } z \leq x } | R ( z ) | .
$$

This function is called error growth function (for linear problems). It is continuous and monotonically increasing. If $R ( z )$ is analytic in the half-plane $\operatorname { R e } z < x$ ,the maximum principle implies that

$$
\varphi _ { R } ( x ) = \operatorname* { s u p } _ { y \in \mathbb { R } } | R ( x + \imath y ) | .
$$

# Examples.

1. Implicit Euler method:

$$
R ( z ) = { \frac { 1 } { 1 - z } } \qquad \varphi _ { R } ( x ) = \left\{ { R ( x ) } \begin{array} { l l } { { \displaystyle R ( x ) } } & { { \mathrm { ~ i f ~ } } - \infty < x < 1 } \\ { { \displaystyle \infty } } & { { \mathrm { ~ i f ~ } } 1 \leq x . } \end{array} \right.
$$

2. The stability function of the $\theta$ -method (or of a one-stage Rosenbrock method):

$$
R ( z ) = \frac { 1 + ( 1 - \theta ) z } { 1 - \theta z } \qquad \varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { | R ( \infty ) | } & { \mathrm { ~ i f ~ } x \leq \xi _ { 0 } } \\ { R ( x ) } & { \mathrm { ~ i f ~ } \xi _ { 0 } \leq x < 1 / \theta } \\ { \infty } & { \mathrm { ~ i f ~ } 1 / \theta \leq x , } \end{array} \right.
$$

where $\xi _ { 0 } = ( 1 - 2 \theta ) / ( 2 \theta ( 1 - \theta ) )$ for $0 < \theta < 1$ and $\xi _ { 0 } = - \infty$ for $\theta \geq 1$

3. The (0,2)-Padé approximation:

$$
R ( z ) = { \frac { 1 } { 1 - z + z ^ { 2 } / 2 } } \varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { R ( x ) } & { \mathrm { ~ i f ~ } - \infty < x \leq 0 } \\ { \displaystyle { \frac { 1 } { 1 - x } } } & { \mathrm { ~ i f ~ } 0 \leq x < 1 } \\ { \infty } & { \mathrm { ~ i f ~ } 1 \leq x . } \end{array} \right.
$$

4. The (1,2)-PdoimaiRz)

$$
\varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { | R ( x ) | } & { \mathrm { i f ~ } - \infty < x \leq \xi } \\ { \frac { \sqrt { 3 \sqrt { 1 2 x ^ { 2 } + 1 2 x + 9 } + 1 0 x + 7 } } { 2 ( 2 - x ) } } & { \mathrm { i f ~ } \xi _ { 0 } \leq x < 2 } \\ { \infty } & { \mathrm { i f ~ } 2 \leq x , } \end{array} \right.
$$

where $\xi _ { 0 } = - 6 - 3 \sqrt { 1 0 }$

5. he (2,2)-Pad pfroxia $R ( z ) = \frac { 1 + z / 2 + z ^ { 2 } / 1 2 } { 1 - z / 2 + z ^ { 2 } / 1 2 }$

$$
\varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { 1 \quad } & { \mathrm { i f ~ } - \infty < x \leq 0 } \\ { \displaystyle \frac { 2 x + \sqrt { 9 + 3 x ^ { 2 } } } { 3 - x } \quad } & { \mathrm { i f ~ } 0 \leq x < 3 } \\ { \infty \quad } & { \mathrm { i f ~ } 3 \leq x . } \end{array} \right.
$$

The next two theorems give some general results on the shape of $\varphi _ { R } ( x )$

Theorem 11.5. Let $R ( z )$ be an $A$ -stable approximation to $e ^ { z }$ of exact order $p$ ， i.e.， $R ( z ) = e ^ { z } - C z ^ { p + 1 } + \mathcal { O } \left( z ^ { p + 2 } \right)$ with $C \neq 0$ . If additionally $| R ( i y ) | < 1$ for $y \neq 0$ and $| R ( \infty ) | < 1$ ， then we have

$a )$ f $p$ is odd

$$
\varphi _ { R } ( x ) = e ^ { x } + \mathcal { O } ( x ^ { p + 1 } ) \quad f o r \quad x \to 0 .
$$

$b _ { . }$ if $p$ is even we have (11.17) only for $( - 1 ) ^ { p / 2 } C x > 0$ , otherwise

$$
\varphi _ { R } ( x ) = e ^ { x } + \mathcal { O } ( x ^ { r + 1 } ) \ - \ fint { f o r \quad x \to 0 }
$$

for some positive rational number $r \leq p / 2$

Proof. The assumptions imply that for $x \to 0$ the maximum of $\{ | R ( x + i y ) | ; y \in \mathbb { R } \}$ must be located near the origin. We further observe that it must lie within the order star $A = \left\{ z \in \mathbb { C } ; | R ( z ) | > | e ^ { z } | \right\}$ .If $p$ is odd, the order star consists of $p + 1$ sectors near the origin (Lemma 4.3) and, asymptotically for $z  \infty$ ， all elements of $A$ satisfy $| z | \leq D | x |$ ， $D < \infty$ . Therefore

$$
| R ( z ) | = e ^ { x } + \mathcal { O } ( | z | ^ { p + 1 } ) = e ^ { x } + \mathcal { O } ( x ^ { p + 1 } ) \quad \mathrm { f o r } \quad x \to 0 .
$$

The same argument applies if $p$ is even and $( - 1 ) ^ { p / 2 } C x > 0$ . In the remaining case $p$ even and $( - 1 ) ^ { p / 2 } C x < 0 )$ the maximum of $\{ | R ( x + i y ) | ; y \in \mathbb { R } \}$ is attained near the imaginary axis and a more detailed analysis is necessary (Hairer, Bader & Lubich 1982). □

Theorem 11.6 (Hairer & Zennaro 1996). For an $A$ -stable approximation to $e ^ { z }$ the function $\varphi _ { R } ( x )$ is superexponential, i.e., it satisfies $\varphi _ { R } ( 0 ) = 1$ and

$$
\varphi _ { R } ( x _ { 1 } ) \varphi _ { R } ( x _ { 2 } ) \leq \varphi _ { R } ( x _ { 1 } + x _ { 2 } )
$$

for all $x _ { 1 } , x _ { 2 }$ having the same sign.

Proof. $A$ -stability is equivalent to $\varphi _ { R } ( 0 ) = 1$ ．It therefore remains to verify (11.19). Let $x _ { 1 }$ and $x _ { 2 }$ be fixed (both $\leq 0$ or both $\geq 0$ ) and assume $\varphi _ { R } ( x _ { 1 } + x _ { 2 } ) <$ $\infty$ . The idea is to consider the rational function

$$
S ( z ) = R ( a - z ) R ( z )
$$

where $a \in \mathbb { C }$ is a parameter satisfying $\mathrm { R e } a \leq x _ { 1 } + x _ { 2 }$ . Due to $A$ -stability and $\varphi _ { R } ( x _ { 1 } + x _ { 2 } ) < \infty , S ( z )$ is analytic on the stripe $0 \leq \mathrm { R e } z \leq x _ { 1 } + x _ { 2 }$ （ $\mathrm { ~ r ~ } x _ { 1 } + x _ { 2 } \leq$ $\mathrm { R e } z \le 0 ) ,$ ，and its modulus is bounded by $\varphi _ { R } ( x _ { 1 } + x _ { 2 } )$ on the border. By the maximum principle we therefore have for all $z$ in the considered stripe

$$
| R ( a - z ) R ( z ) | \leq \varphi _ { R } ( x _ { 1 } + x _ { 2 } ) .
$$

We now choose $z$ on the line $\mathrm { R e } z = x _ { 2 }$ in such a way that $| R ( z ) |$ becomes maximal; then, we choose $a$ on the line $\mathrm { R e } a = x _ { 1 } + x _ { 2 }$ (i.e., $\operatorname { R e } { \big ( } a - z { \big ) } = x _ { 1 } { \big . }$ ）such that $| R ( a - z ) |$ becomes maximal (eventually one has to consider limits). This proves (11.19). □

Property (11.19) has an interesting practical interpretation. Consider a numerical solution $y _ { n }$ obtained with variable step sizes.Repeated application of (11.4) and Corollary 11.4 implies

$$
\| y _ { m } \| \leq \Big ( \prod _ { k = 0 } ^ { m - 1 } \varphi _ { R } ( h _ { k } \mu ) \Big ) \cdot \| y _ { 0 } \| ,
$$

if the problem $y ^ { \prime } = A y$ satisfies (11.7) with $\mu = \mu _ { 2 } ( A )$ . For $\mu < 0$ and for an $A -$ stable method all factors $\varphi _ { R } ( h _ { k } \mu )$ are smaller than one. If in addition $| R ( \infty ) | < 1$ ，

these factors are close to one only for $h _ { k } \to 0$ . The inequality (11.19), written as

$$
\begin{array} { r } { \varphi _ { R } ( h _ { k } \mu ) \varphi _ { R } ( h _ { k + 1 } \mu ) \leq \varphi \big ( ( h _ { k } + h _ { k + 1 } ) \mu \big ) , } \end{array}
$$

means that replacing two consecutive steps by one large step of size $h _ { k } + h _ { k + 1 }$ increases the upper bound (11.2O). Therefore,after combining several consecutive steps (if necessary), we may assume $h _ { k } \geq h > 0$ for all $k$ . This implies that $\| y _ { m } \| \leq$ $\varrho ^ { m } \| y _ { 0 } \|$ with $\varrho = \varphi _ { R } ( h \mu ) < 1$ . Hence, for any mesh $x _ { 0 } , x _ { 1 } , \ldots$ with $x _ { m } \to \infty$ ，we have asymptotic stability,i.e., $\| y _ { m } \| \to 0$ for $m \to \infty$ . Under additional restrictions on the step size, sharper bounds on $\| y _ { m } \|$ can be obtained (Exercise 3).

# Small Nonlinear Perturbations

The above estimates,valid only for linear autonomous equations $y ^ { \prime } = J y$ ，can be extended to problems with small nonlinear perturbations, so-called semi-linear problems

$$
y ^ { \prime } = J y + g ( x , y )
$$

where

$$
\begin{array} { c } { { \langle y , J y \rangle \leq \mu \| y \| ^ { 2 } } } \\ { { } } \\ { { \| g ( x , y ) - g ( x , z ) \| \leq L \| y - z \| } } \end{array}
$$

with $L$ assumed to be small.

Here,in the presence of nonlinearities, stability properties are obtained by $\mathbf { e s - }$ timating the distance of two neighbouring solutions $y ( x )$ and ${ \widehat { y } } ( x )$ . Instead of (11.5) we therefore have

$$
\frac { d } { d x } \| y ( x ) - \widehat { y } ( x ) \| ^ { 2 } = 2 \langle y ^ { \prime } - \widehat { y } ^ { \prime } , y - \widehat { y } \rangle
$$

which gives,after inserting(11.21） for $y ^ { \prime }$ and ${ \widehat { y } } ^ { \prime }$ ,using the Cauchy-Schwarz inequality and the estimates (11.22)

$$
{ \frac { d } { d x } } \| y ( x ) - { \widehat { y } } ( x ) \| ^ { 2 } \leq 2 { \big ( } \mu + L { \big ) } \ \| y ( x ) - { \widehat { y } } ( x ) \| ^ { 2 } .
$$

We thus have contractivity whenever $\mu + L \leq 0$

We now want to establish the same property for the numerical solutions. In principle, these estimates can be carried out for all methods of this chapter; however, since the subsequent sections will deal with so many nice properties of implicit Runge-Kutta methods, we shall concentrate here on Rosenbrock methods.

Example 11.7. Consider the 1-stage Rosenbrock method

$$
\begin{array} { c } { { ( I - \gamma h J ) k _ { 1 } = h f ( x _ { 0 } , y _ { 0 } ) } } \\ { { y _ { 1 } = y _ { 0 } + k _ { 1 } } } \end{array}
$$

with $\gamma > 0$ as a free parameter. Its stability function is

$$
R ( z ) = \frac { 1 + ( 1 - \gamma ) z } { 1 - \gamma z }
$$

and we have $A$ -stability for $\gamma \geq 1 / 2$ . Application of (11.24) to (11.21) yields

$$
y _ { 1 } = R ( h J ) y _ { 0 } + ( I - \gamma h J ) ^ { - 1 } h g ( x _ { 0 } , y _ { 0 } ) .
$$

From von Neumann's theorem (Corollary 11.4) we obtain $\| ( I - \gamma h J ) ^ { - 1 } \| \leq ( 1 -$ $\gamma h \mu ) ^ { - 1 }$ and $\| R ( h J ) \| \leq \varphi _ { R } ( h \mu )$ with $\varphi _ { R }$ given in (11.13). If we take a second numerical solution $\widehat { y } _ { 1 }$ ,also defined by (11.25),its difference to $y _ { 1 }$ can be estimated by

$$
\| y _ { 1 } - \widehat { y } _ { 1 } \| \leq \Big ( R ( h \mu ) + \frac { h L } { 1 - \gamma h \mu } \Big ) \| y _ { 0 } - \widehat { y } _ { 0 } \| = \Big ( 1 + \frac { h ( \mu + L ) } { 1 - \gamma h \mu } \Big ) \| y _ { 0 } - \widehat { y } _ { 0 } \|
$$

whenever $\xi _ { 0 } < h \mu < 1 / \gamma$ with $\xi _ { 0 }$ given in (11.13). Therefore contractivity occurs for $\mu + L \leq 0$ , as desired.

For the general Rosenbrock method (7.4) applied to problem (11.21)

$$
\begin{array} { l } { { \displaystyle { k _ { \imath } = h g \big ( x _ { 0 } + c _ { \imath } h , u _ { \imath } \big ) + h J y _ { 0 } + h J \sum _ { \jmath = 1 } ^ { \imath } \big ( a _ { \imath \jmath } + \gamma _ { \imath \jmath } \big ) k _ { \jmath } } } } \\ { { \displaystyle { u _ { \imath } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \imath \jmath } k _ { \jmath } } , \quad { y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } k _ { \imath } } } } \end{array}
$$

we easily find the following analogue of the variation of constants formula.

Theorem 11.8. The numerical solution of a Rosenbrock method applied to (11.21) can be written as

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = R ( h J ) y _ { 0 } + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( h J ) g ( x _ { 0 } + c _ { \imath } h , u _ { \imath } ) } } \\ { \displaystyle { u _ { \imath } = R _ { \imath } ( h J ) y _ { 0 } + h \sum _ { j = 1 } ^ { \imath - 1 } a _ { \imath _ { \jmath } } ( h J ) g ( x _ { 0 } + c _ { \jmath } h , u _ { \jmath } ) , \quad i = 1 , \ldots , s . } } \end{array}
$$

Here $R ( z )$ is the stability function, $R _ { \ i } ( z )$ are the so-called internal stability functions and $b _ { i } ( z ) , \ a _ { \ i j } ( z )$ are rational functions whose only pole is $1 / \gamma$ and which satisfy $b _ { \imath } ( \infty ) = 0$ ， $\dot { a } _ { \iota \jmath } ( \infty ) = 0$ □

Remark. For many classes of linearly implicit methods (e.g., the methods of van der Houwen (1977),Friedli (1978), Strehmel & Weiner (1982),etc.), the numerical solution can be expressed by (11.26) with certain rational functions. Thus the following analysis can be applied to these methods as well.

We now take a second numerical solution $\widehat { y } _ { 0 } , \widehat { u } _ { \iota } , \widehat { y } _ { 1 }$ (again defined by (11.26)), take the difference to $y _ { 1 }$ and apply the triangle inequality. Using von Neumann's theorem (Corollary 11.4) the assumptions (11.22) then imply

$$
\begin{array} { r l } & { \| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \varphi _ { R } ( h \mu ) \| \widehat { y } _ { 0 } - y _ { 0 } \| + h L \displaystyle \sum _ { \imath = 1 } ^ { s } \varphi _ { b _ { \imath } } ( h \mu ) \| \widehat { u } _ { \imath } - u _ { \imath } \| } \\ & { \| \widehat { u } _ { \imath } - u _ { \imath } \| \leq \varphi _ { R _ { \imath } } ( h \mu ) \| \widehat { y } _ { 0 } - y _ { 0 } \| + h L \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \varphi _ { a _ { \imath , \jmath } } ( h \mu ) \| e \widehat { u } _ { \jmath } - u _ { \jmath } \| . } \end{array}
$$

Inserting the second inequality of(11.27) repeatedly into the first one yields

Theorem 11.9. Under the assumption (11.22) the difference of two numerical solutions of (7.4) can be estimated by

$$
\| { \widehat { y } } _ { 1 } - y _ { 1 } \| \leq { \big ( } \varphi _ { R } ( h \mu ) + c h L { \big ) } \| { \widehat { y } } _ { 0 } - y _ { 0 } \|
$$

where $\varphi _ { R } ( x )$ is given by (11.11) ( $R ( z )$ is the stability function of (7.4)) and c is a constant depending smoothly on $h L$ and $h \mu$ but not on $\| J \|$ (which represents the stiffness of the problem). □

This estimate shows numerical contractivity whenever $\varphi _ { R } ( h \mu ) + h L ^ { * } \leq 0$ .In Theorem 11.5 we have shown under certain assumptions that $\varphi _ { R } ( x ) = 1 + x +$ $o ( x )$ ，so contractivity holds essentially for $\mu + L ^ { * } \leq 0$ . In any case we have that $A$ -stability implies

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \left( 1 + h C ^ { * } \right) \| \widehat { y } _ { 0 } - y _ { 0 } \|
$$

for $h \mu \leq C o n s t$ . Here, $C ^ { * }$ is a constant independent of the stiffess of (11.21).

Remark. Since the rational functions $b _ { \imath }$ and $a _ { \scriptscriptstyle { \imath \jmath } }$ in (11.26) vanish at infinity,also $( 1 - \gamma h J ) b _ { \iota } ( h J )$ and $( 1 - \gamma h J ) a _ { \iota \boldsymbol { \jmath } } ( h J )$ are uniformly bounded for $J$ satisfying (11.22) and for $h \mu \leq C < \gamma ^ { - 1 }$ . Instead of the second condition of (11.22) we may therefore require that

$$
\begin{array} { r } { \| ( I - \gamma h J ) ^ { - 1 } h ( g ( x , y ) - g ( x , z ) ) \| \leq \ell \| y - z \| , } \end{array}
$$

and the statement of Theorem 11.9 holds with $h L$ replaced by $\ell$ . Observe that the assumption（11.22) implies （11.29） with $\ell = h L / ( 1 - \gamma h \mu )$ . However, in some special situations the number $\ell$ may be significantly smaller than $h L$ . Related techniques are used by Hundsdorfer(1985) and Strehmel & Weiner (1987) to prove contractivity and convergence for linearly implicit methods. Ostermann (1988) ap-plies these ideas to nonlinear singular perturbation problems, where $h L = \mathcal { O } ( h \varepsilon ^ { - 1 } )$ with some very small $\varepsilon$ $\left( \varepsilon \ll h \right)$ ,but $\ell$ can be bounded independently of $\varepsilon ^ { - 1 }$ ·

# Contractivity in $\| \cdot \| _ { \infty }$ and $\| \cdot \| _ { 1 }$

The study of contractivity in general norms has been carried out mainly by Spijker (1983,1985) and his collaborators. Similar techniques of proof can be found in Bolley & Crouzeix (1978),where a related problem (monotonicity) is treated.

The following theorem gives a condition which is necessary for contractivity just for the special equation (11.2) and for one of the two norms $\| \cdot \| _ { \infty } \ \mathrm { o r } \ \| \cdot \| _ { 1 } .$ Later,the same condition will also turn out to be sufficient for general problems and all norms.

Theorem 11.10. Let $A$ be the $\textit { n }$ -dimensional matrix of(11.2) with fixed $\lambda \geq 0$ For a rational function $R ( z )$ satisfying $R ( 0 ) = 1$ we have

$$
\| R ( h A ) \| _ { \infty } \leq 1 \quad i n a l l d i m e n s i o n s \quad n = 1 , 2 , \ldots .
$$

only if

$$
R ^ { ( j ) } ( x ) \geq 0 f o r x \in [ - \lambda h , 0 ] a n d j = 0 , 1 , 2 , . . .
$$

(The same statement is true,if Il:ll in (11.30) is replaced by $\| \cdot \| _ { 1 } )$

Proof. We put $h = 1$ and write $A = - \lambda I + \lambda N$ ,where $N$ is a nilpotent matrix. In a suitable norm, $\| N \|$ is arbitrarily small and therefore we have by Taylor expansion and $N ^ { n } = 0$

$$
R ( A ) = \sum _ { j = 0 } ^ { n - 1 } R ^ { ( j ) } ( - \lambda ) { \frac { ( \lambda N ) ^ { j } } { j ! } } .
$$

This means (e.g. for $n = 4$ ）

$$
R ( A ) = \left( \begin{array} { r r r r } { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 2 } } { 2 ! } R ^ { \prime \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 3 } } { 3 ! } R ^ { \prime \prime \prime } ( - \lambda ) } } \\ { { } } & { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 2 } } { 2 ! } R ^ { \prime \prime } ( - \lambda ) } } \\ { { } } & { { } } & { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } \\ { { } } & { { } } & { { R ( - \lambda ) } } & { { R ( - \lambda ) } } \end{array} \right) .
$$

Application of Formula (I.9.11'） shows that $\| R ( A ) \| _ { \infty } \leq 1 \ ( \mathrm { o r } \ \| R ( A ) \| _ { 1 } \leq 1 )$ isequivalent to

$$
\sum _ { j = 0 } ^ { n - 1 } \big | R ^ { ( j ) } ( - \lambda ) \big | \frac { \lambda ^ { j } } { j ! } \ \le 1 .
$$

If (11.32) is valid for all $n \geq 1$ , the series

$$
\sum _ { \jmath \geq 0 } R ^ { ( \jmath ) } ( - \lambda ) \frac { \lambda ^ { j } } { j ! }
$$

is absolutely convergent, and therefore we have

$$
1 = R ( 0 ) = \sum _ { j \geq 0 } R ^ { ( j ) } ( - \lambda ) { \frac { \lambda ^ { j } } { j ! } } \leq \sum _ { j \geq 0 } | R ^ { ( j ) } ( - \lambda ) | { \frac { \lambda ^ { j } } { j ! } } \leq 1
$$

implying $R ^ { ( j ) } ( - \lambda ) \geq 0$ for all $j \geq 0$ . Since the Taylor expansion

$$
R ^ { ( j ) } ( x ) = \sum _ { k \geq \jmath } R ^ { ( k ) } ( - \lambda ) \frac { ( x + \lambda ) ^ { k - j } } { ( k - j ) ! }
$$

consists for $x \geq - \lambda$ only of non-negative terms, we have (11.31).

The next theorem shows that condition (11.31） is sufficient for contractivity in arbitrary norms. It can readily be applied to the system (11.2),since its matrix satisfies $\| A + \lambda I \| _ { \infty } = \lambda$

Theorem 11.11. Consider an arbitrary norm and let $A$ be such that for some $\lambda \geq 0$ ，

$$
\| A + \lambda I \| \leq \lambda .
$$

If the stability function of $a$ method satisfies $R ( 0 ) = 1$ and

$$
R ^ { ( \jmath ) } ( x ) \geq 0 \quad f o r \quad x \in [ - \varrho , 0 ] \quad a n d \quad j = 0 , 1 , 2 , \ldots .
$$

then we have numerical contractivity $\| R ( h A ) \| \leq 1$ , whenever $h \lambda \leq \varrho$

Proof. We again put $h = 1$ . Since for $0 \leq \lambda \leq \varrho$ we have $R ^ { ( j ) } ( - \lambda ) \ge 0$ for all $j$ the function

$$
R ( z ) = \sum _ { j \geq 0 } R ^ { ( j ) } ( - \lambda ) { \frac { ( z + \lambda ) ^ { j } } { j ! } }
$$

satisfies $| R ( z ) | \leq R ( - \lambda + r )$ for all complex $z$ in the disk $| z + \lambda | \leq r$ . This property and (11.35) imply that no pole of $R ( z )$ can lie in $| z + \lambda | \leq \lambda$ ， so that the radius of convergence of (11.36) is strictly larger than $\lambda$ . Consequently we have from (11.34)

$$
R ( A ) = \sum _ { j \geq 0 } R ^ { ( \jmath ) } ( - \lambda ) { \frac { ( A + \lambda I ) ^ { \jmath } } { j ! } } .
$$

The triangle inequality applied to (11.37) yields the conclusion.

# Study of the Threshold Factor

Definition 11.12. The largest $\varrho$ satisfying (11.35) is called the threshold-factor of $R ( z )$

Example 11.13. The implicit Euler method, for which

$$
R ^ { ( j ) } ( x ) = { \frac { j ! } { ( 1 - x ) ^ { j + 1 } } } , \quad j = 0 , 1 , 2 , \ldots ,
$$

satisfies (11.35) for all $\varrho > 0$ . It possesses a threshold-factor $\varrho = \infty$

Example 11.14 (Threshold-factor for Padé-approximations). The derivatives of the polynomials

$$
R _ { k 0 } ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 ! } } + \ldots + { \frac { z ^ { k } } { k ! } }
$$

are easily calculated; the most dangerous one is $1 + z$ ,therefore $\varrho = 1$ for all $k$

The Padé approximations $R _ { k 1 } ( z )$ possess one simple pole only,so they can be written in the form

$$
R _ { k 1 } ( z ) = \frac { a } { 1 - b z } + \mathrm { p o l y n o m i a l i n } z ,
$$

which has only a finite number of derivatives which can change sign (see Example 11.13). The numerical values obtained are shown in Table 11.1.

The functions $R _ { k 2 } ( z )$ possess no real pole (see Sect.IV.4). But the property $| R ( z ) | \leq R ( - \varrho + r )$ for $| z + \varrho | \leq r$ (see proof of Theorem 11.10) means that the maximum of $| R ( z ) |$ on the circle with center $- \varrho$ and radius $\mathscr { r }$ is assumed to the right on the real axis. For increasing $\boldsymbol { \mathscr { r } }$ , the first pole met by this circle must therefore be real and to the right of $- \varrho$ ． This is not possible here and therefore the approximations $R _ { k 2 } ( z )$ never satisfy property (11.35). This is indicated by an asterisk $( * )$ in Table 11.1.

All further values of Table 11.1 were computed using the decomposition of $R ( z )$ into partial fractions and are cited from Kraaijevanger (1986) and van de Griend & Kraaijevanger (1986).

Table 11.1. Threshold-factors of Padé approximations   

<table><tr><td>k</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>J=0</td><td>1 1</td><td>1</td><td>1</td><td>1 1</td><td>1</td></tr><tr><td>J=1</td><td>8 2</td><td>2.196</td><td>2.350 2.477</td><td>2.586</td><td>2.682</td></tr><tr><td>j=2</td><td>* *</td><td>*</td><td>* *</td><td>*</td><td>*</td></tr><tr><td>j=3</td><td>0.584 1.195</td><td>1.703</td><td>2.208</td><td>2.710 3.212</td><td>3.713</td></tr><tr><td>j=4</td><td>* *</td><td>*</td><td>* *</td><td>*</td><td>*</td></tr><tr><td>j=5</td><td>0.353 0.770</td><td>1.081</td><td>1.424</td><td>1.794 2.185</td><td>2.590</td></tr></table>

It is curious to observe that in this table the methods with the largest thresholdfactors are precisely those which are not $A$ -stable. An exception is the implicit Euler method $\left( k = 0 , j = 1 \right)$ for which $\varrho = \infty$ .

# Absolutely Monotonic Functions

... on peut definir la fonction $e ^ { x }$ comme la seule fonction absolument monotone sur tout le demi-axe négatif qui prend al'origine, ainsi que sa dérivee premiere [sic] la valeur un.

(S. Bernstein 1928)

A thorough study of real functions satisfying (11.35) was begun by S.Bernstein (1914) and continued by F. Hausdorff(1921). Such functions are called absolutely monotonic in $[ - \varrho , 0 ]$ . Later, S. Bernstein (1928) gave the following characterization of functions which are absolutely monotonic in $( - \infty , 0 ]$ (see also D.V. Widder 1946).

Theorem 11.15 (Bernstein 1928). A necessary and sufficient condition that $R ( x )$ be absolutely monotonic in $( - \infty , 0 ]$ is that

$$
R ( x ) = \int _ { 0 } ^ { \infty } e ^ { x t } d \alpha ( t ) ,
$$

where $\alpha ( t )$ is bounded and non-decreasing and the integral converges for $- \infty <$ $x \le 0$

This is a hard result and the main key for the next two theorems. It does not seem to permit an elementary and easy proof. We therefore refer to the original literature, S. Bernstein (1928). For a more recent description see e.g. Widder (1946),p.160. From this result we immediately get the “limit case $\lambda  \infty ^ { \prime \prime }$ of Theorem 11.11, which also holds for an arbitrary norm.

Theorem 11.16. Let $R ( x )$ be absolutely monotonic in $( - \infty , 0 ] , R ( 0 ) = 1$ and A a matrix with non-positive logarithmic norm $\mu ( A ) \leq 0$ ， then

$$
\| R ( A ) \| \leq 1 .
$$

Proof. By Theorem I.10.6 we have for the solution $y ( x ) = e ^ { A x } y _ { 0 }$ of $y ^ { \prime } = A y$ that $\| y ( x ) \| \leq \| y _ { 0 } \|$ , hence also $\| e ^ { \ b { A } \ b { x } } \| \leq 1$ for $x \ge 0$ . The statement now follows from

$$
\| R ( A ) \| = \| \int _ { 0 } ^ { \infty } e ^ { A t } d \alpha ( t ) \| \le \int _ { 0 } ^ { \infty } \| e ^ { A t } \| d \alpha ( t ) \le \int _ { 0 } ^ { \infty } d \alpha ( t ) = R ( 0 ) = 1
$$

since $\alpha ( t )$ is non-decreasing.

The following result proves that no Runge-Kutta method of order $p > 1$ can have a stability function which is absolutely monotonic in $( - \infty , 0 ]$

Theorem 11.17. If $R ( x )$ is absolutely monotonic in $( - \infty , 0 ]$ and

$$
R ( x ) = 1 + x + x ^ { 2 } / 2 + \mathcal { O } ( x ^ { 3 } ) \qquad f o r \quad x \to 0 ,
$$

then $R ( x ) = e ^ { x }$

Proof (Bolley & Crouzeix 1978). It follows from (11.38) that

$$
R ^ { ( j ) } ( 0 ) = \int _ { 0 } ^ { \infty } t ^ { j } d \alpha ( t ) .
$$

Since $R ( 0 ) = R ^ { \prime } ( 0 ) = R ^ { \prime \prime } ( 0 ) = 1$ , this yields

$$
\int _ { 0 } ^ { \infty } ( 1 - t ) ^ { 2 } d \alpha ( t ) = 0 .
$$

Consequently, $\alpha ( t )$ must be the Heaviside function $( \alpha ( t ) = 0$ for $t \leq 1$ and $\alpha ( t ) =$ 1 for $t > 1$ ). Inserted into (11.38) this gives $R ( x ) = e ^ { x }$ □

# Exercises

1. Prove Formula (11.14). For given $\boldsymbol { x }$ ，study the set of $y$ -values for which $| R ( x + i y ) |$ attains its maximum.

2. Show that the error growth function (11.11） for an $A$ -stable $R ( z )$ of order $p \geq 1$ satisfies

$$
\varphi _ { R } ( x ) > e ^ { x } \quad { \mathrm { f o r ~ a l l } } \quad x \neq 0 .
$$

Hint. You can study the order star on parallel lines $\{ x + i y , y \in \mathbb { R } \}$ (Hairer, Bader & Lubich 1982),or you can use the fact that $\varphi _ { R } ( x )$ is superexponential.

3. (Hairer & Zennaro 1996). Let $| R ( \infty ) | < 1$ and consider a mesh $x _ { 0 } , x _ { 1 } , \ldots$ with step sizes $h _ { k } = x _ { k + 1 } - x _ { k }$ satisfying $h _ { k + 1 } \leq c h _ { k }$ $( c > 1 )$ .Prove the existence of constants $C > 0$ and $\alpha > 0$ such that

$$
\begin{array} { r } { \| y _ { m } \| \leq C ( x _ { m } - x _ { 0 } ) ^ { - \alpha } \| y _ { 0 } \| \qquad \mathrm { ~ f o r ~ } \quad m = 1 , 2 , \ldots . } \end{array}
$$

4. (Kraaijevanger 1986). Let $R ( z )$ be a polynomial of degree $s$ satisfying $R ( z ) =$ $e ^ { z } + \mathcal { O } \big ( z ^ { p + 1 } \big )$ . Then the threshold factor $\varrho$ (Definition 11.11) is restricted by

$$
\varrho \leq s - p + 1 .
$$

Hint. Justify the formula

$$
R ^ { ( p - 1 ) } ( z ) = \sum _ { \jmath = 0 } ^ { s - p + 1 } \alpha _ { \jmath } \Big ( 1 + \frac { z } { \varrho } \Big ) ^ { \jmath } , \quad \alpha _ { \jmath } \geq 0
$$

and deduce the result from $R ^ { ( p - 1 ) } ( 0 ) = R ^ { ( p ) } ( 0 ) = 1$

5. Let $\varrho$ be the threshold factor of the rational function $R ( z )$ . Show that its stability domain contains the disc $| z + \varrho | \le \varrho$

# IV.12 B-Stability and Contractivity

Next we need a generalization of the notion of $A$ -stability. The most natural generalization would be to consider the case that ${ \boldsymbol x } ( t )$ is a uniform-asymptotically stable solution ... in the sense of Liapunov theory ... but this case seems to be a little too wide.

(G. Dahlquist 1963)

The theoretical analysis of the application of numerical methods on stiff nonlinear problems is still fairly incomplete.

(G. Dahlquist 1975)

Here we enter a new era, the study of stability and convergence for general nonlinear systems. All the“crimes” and diverse omissions of which we have been guilty in earlier sections, especially in Sect. IV.2, shall now be repaired.

Large parts of Dahlquist's(1963) paper deal with a generalization of $A$ -stability to nonlinear problems. His search for a sufciently general class of nonlinear systems was finally successful 12 years later. In his talk at the Dundee conference of July 1975 he proposed to consider differential equations satisfying a one-sided Lipschitz condition,and he presented some first results for multistep methods. J.C.Butcher(1975） then extended (on the flight back from the conference） the ideas to implicit Runge-Kutta methods and the concept of $B$ -stability was born.

# One-Sided Lipschitz Condition

We consider the nonlinear differential equation

$$
y ^ { \prime } = f ( x , y )
$$

such that for the Euclidean norm the one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 }
$$

holds.The number $\nu$ is the one-sided Lipschitz constant of $f$ . This definition is motivated by the following result.

Lemma 12.1. Let $f ( x , y )$ be continuous and satisfy (12.2). Then, for any two solutions $y ( x )$ and $z ( x )$ of(12.1) we have

$$
\| y ( x ) - z ( x ) \| \leq \| y ( x _ { 0 } ) - z ( x _ { 0 } ) \| \cdot e ^ { \nu ( x - x _ { 0 } ) } \qquad f o r ~ x \geq x _ { 0 } .
$$

Proof. Differentiation of $m ( x ) = \| y ( x ) - z ( x ) \| ^ { 2 }$ yields

$$
m ^ { \prime } ( x ) = 2 { \bigl \langle } f ( x , y ( x ) ) - f ( x , z ( x ) ) , \ y ( x ) - z ( x ) { \bigr \rangle } \leq 2 \nu m ( x ) .
$$

This differential inequality can be solved to give (see Theorem I.10.3)

$$
m ( x ) \leq m ( x _ { 0 } ) e ^ { 2 \nu ( x - x _ { 0 } ) } \qquad { \mathrm { f o r } } \ x \geq x _ { 0 } ,
$$

which is equivalent to the statement.

EHairer and G Wanner, Solving Ordinary Differential Equations II, Springer Series in Computat1onal Mathematics 14, DOI 10 1007/978-3-642-05221-7_12, $©$ Springer-Verlag Berlin Heidelberg 2010

Remarksesoistt $\mu ( \frac { \partial f } { \partial y } ) \leq \nu$ (see Sect.I.10, Exercise 6), if $f$ is continuously differentiable. Lemma 12.1 then becomes a special case of Theorem I.10.6.

b) For complex-valued $y$ and $f$ condition (12.2) has to be replaced by

$$
\mathrm { R e } \left. f ( x , y ) - f ( x , z ) , y - z \right. \leq \nu \left. y - z \right. ^ { 2 } , \qquad y , z \in \mathbb { C } ^ { n } ,
$$

and Lemma 12.1 remains valid.

# $B$ -Stability and Algebraic Stability

Whenever $\nu \leq 0$ in (12.2） the distance between any two solutions of (12.1） is a non-increasing function of $x$ . The same property is then also desirable for the numerical solutions. We consider here implicit Runge-Kutta methods

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } f \big ( x _ { 0 } + c _ { i } h , g _ { i } \big ) , } } \\ { \displaystyle { g _ { \imath } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { \imath j } f \big ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } \big ) , \qquad i = 1 , \dots , s . } } \end{array}
$$

Definition 12.2 (Butcher 1975). A Runge-Kutta method is called $B$ -stable, if the contractivity condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq 0
$$

implies for all $h \geq 0$

$$
\lVert y _ { 1 } - { \widehat { y } } _ { 1 } \rVert \leq \lVert y _ { 0 } - { \widehat { y } } _ { 0 } \rVert .
$$

Here, $y _ { 1 }$ and $\widehat { y } _ { 1 }$ are the numerical approximations after one step starting with initial values $y _ { 0 }$ and $\widehat { y } _ { 0 }$ ,respectively.

Clearly, $B$ -stability implies $A$ -stability. This is seen by applying the above definition to $y ^ { \prime } = \lambda y , \lambda \in \mathbb { C }$ or, more precisely, to

$$
\left( \begin{array} { c } { { y _ { 1 } ^ { \prime } } } \\ { { y _ { 2 } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { c c } { { \alpha } } & { { - \beta } } \\ { { \beta } } & { { \alpha } } \end{array} \right) \left( \begin{array} { c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \end{array} \right) .
$$

Example 12.3. For the collocation methods based on Gaussian quadrature a simple proof of $B$ -stability is possible (Wanner 1976). We denote by $u ( x )$ and ${ \widehat { u } } ( x )$ the collocation polynomials (see Definition II.7.6) for the initial values $y _ { 0 }$ and $\widehat { y } _ { 0 }$ and differentiate the function $m ( x ) = \| u ( x ) - { \widehat { u } } ( x ) \| ^ { 2 }$ ． At the collocation points $\xi _ { \ i } = x _ { 0 } + c _ { \ i } h$ we obtain

$$
\begin{array} { r } { m ^ { \prime } ( \xi _ { \iota } ) = 2 \big \langle f ( \xi _ { \iota } , u ( \xi _ { \iota } ) ) - f ( \xi _ { \iota } , \widehat { u } ( \xi _ { \iota } ) ) , u ( \xi _ { \iota } ) - \widehat { u } ( \xi _ { \iota } ) \big \rangle \leq 0 . } \end{array}
$$

The result then follows from the fact that Gaussian quadrature integrates the polynomial $m ^ { \prime } ( x )$ (which is of degree $2 s - 1 )$ ） exactly and that the weights $b _ { \imath }$ are positive:

$$
\begin{array} { l } { \displaystyle \| y _ { 1 } - \widehat { y } _ { 1 } \| ^ { 2 } = m ( x _ { 0 } + h ) = m ( x _ { 0 } ) + \int _ { x _ { 0 } } ^ { x _ { 0 } + h } m ^ { \prime } ( x ) d x } \\ { \displaystyle = m ( x _ { 0 } ) + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } m ^ { \prime } ( x _ { 0 } + c _ { \imath } h ) \leq m ( x _ { 0 } ) = \| y _ { 0 } - \widehat { y } _ { 0 } \| ^ { 2 } . } \end{array}
$$

An algebraic criterion for $B$ -stability was found independently by Burrage & Butcher(1979) and Crouzeix (1979). The result is

Theorem 12.4. If the coeffcients of a Runge-Kutta method (12.3) satisfy

i） $b _ { \imath } \geq 0$ for $i = 1 , \dots , s ,$   
ii $M = ( m _ { i j } ) = ( b _ { \ i } a _ { \ i j } + b _ { \jmath } a _ { \jmath \imath } - b _ { i } b _ { \jmath } ) _ { i , j = 1 } ^ { \it s }$ is non-negative definite, then the method is $B$ -stable.

Definition 12.5.A Runge-Kutta method, satisfying (i) and (ii) of Theorem 12.4, is called algebraically stable.

Proof of Theorem 12.4. We introduce the differences

$$
\begin{array} { r l } & { \Delta y _ { 0 } = y _ { 0 } - \widehat { y } _ { 0 } , \qquad \Delta y _ { 1 } = y _ { 1 } - \widehat { y } _ { 1 } , \qquad \Delta g _ { \iota } = g _ { \iota } - \widehat { g } _ { \iota } , } \\ & { \Delta f _ { \iota } = h \big ( f ( x _ { 0 } + c _ { \iota } h , g _ { i } ) - f ( x _ { 0 } + c _ { i } h , \widehat { g } _ { \iota } ) \big ) , } \end{array}
$$

and subtract the Runge-Kutta formulas (12.3) for $y$ and $\widehat { y }$

$$
\begin{array} { l } { \displaystyle \Delta y _ { 1 } = \Delta y _ { 0 } + \sum _ { i = 1 } ^ { s } b _ { i } \Delta f _ { \imath } , } \\ { \displaystyle \Delta g _ { \imath } = \Delta y _ { 0 } + \sum _ { j = 1 } ^ { s } a _ { \imath j } \Delta f _ { \jmath } . } \end{array}
$$

Next we take the square of Formula (12.5a)

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { i = 1 } ^ { s } b _ { \imath } \langle \Delta f _ { \imath } , \Delta y _ { 0 } \rangle + \sum _ { \imath = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } b _ { \imath } b _ { \jmath } \langle \Delta f _ { \imath } , \Delta f _ { \jmath } \rangle .
$$

The main idea of the proof is now to compute $\Delta y _ { 0 }$ from (12.5b) and insert this into (12.6). This gives

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { \iota = 1 } ^ { s } b _ { \iota } \langle \Delta f _ { \iota } , \Delta g _ { i } \rangle - \sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { \iota \jmath } \langle \Delta f _ { \iota } , \Delta f _ { \jmath } \rangle .
$$

$\langle \Delta f _ { \imath } , \Delta g _ { i } \rangle \leq 0$ by $( 1 2 . 2 ^ { \circ } )$ and ta $\begin{array} { r } { \sum _ { \iota , \jmath = 1 } ^ { s } m _ { \iota \jmath } \langle \Delta f _ { i } , \Delta f _ { \jmath } \rangle \geq 0 } \end{array}$

Example 12.6. For the SDIRK method of Table 7.2 (Chapter II) the weights $b _ { i }$ are seen to be positive and the matrix $M$ becomes

$$
M = ( \gamma - 1 / 4 ) \cdot \left( \begin{array} { r r } { { 1 } } & { { - 1 } } \\ { { - 1 } } & { { 1 } } \end{array} \right) .
$$

For $\gamma \ge 1 / 4$ this matrix is non-negative definite and we have $B$ -stability. Exactly the same condition was obtained by studying its $A$ -stability (c.f. (3.10)).

# Some Algebraically Stable IRK Methods

La premiere de ces proprietes consiste en ce que tous les $A _ { k }$ sont positifs. (T.-J. Stieltjes 1884)

The general study of algebraic stability falls naturally into two steps: the positivity of the quadrature weights and the nonnegative-definitness of the matrix $M$

Theorem 12.7. Consider a quadrature formula $( c _ { \imath } , b _ { \imath } ) _ { \imath = 1 } ^ { s }$ of order $p$

$a _ { . }$ ）If $p \geq 2 s - 1$ then $b _ { \imath } > 0$ for all $i$ $b _ { \mathcal { S } }$ If $c _ { \imath }$ are the zeros of (5.3) (Lobatto quadrature) then $b _ { i } > 0$ for all $i$

Proof (Stieltjes 1884). The first statement follows from the fact that for $p \geq 2 s - 1$ polynomials of degree $2 s - 2$ are integrated exactly, hence

$$
b _ { \imath } = \int _ { 0 } ^ { 1 } \prod _ { \jmath \neq \imath } \Bigl ( { \frac { x - c _ { \jmath } } { c _ { \imath } - c _ { \jmath } } } \Bigr ) ^ { 2 } d x > 0 .
$$

In the case of the Lobatto quadrature $( c _ { 1 } = 0 , \ c _ { s } = 1$ and $p = 2 s - 2 )$ the factors for the indices $j = 1$ and $j = s$ are taken without squaring and the same argument applies. □

In order to verify condition (ii) of Theorem 12.4 we find it convenient to use the $W$ -transformation of Sect.IV.5 and to consider $W ^ { T } M W$ instead of $M$ In vector notation $( b = ( b _ { 1 } , \dots , b _ { s } ) ^ { T }$ ， $B = \mathrm { d i a g } ( b _ { 1 } , \dots , b _ { s } )$ ， $A = \left( a _ { \imath \jmath } \right) )$ we have

$$
M = B A + A ^ { T } B - b b ^ { T } .
$$

If we choose $W$ according to Lemma 5.12, then $W ^ { T } B W = I$ and, since $W ^ { T } b =$ $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T }$ ,condition (ii) becomes equivalent to

$$
W ^ { T } M W = X + X ^ { T } - e _ { 1 } e _ { 1 } ^ { T } { \mathrm { i s ~ n o n } } { \mathrm { - n e g a t i v e ~ d e f i n i t e } }
$$

where $X = W ^ { - 1 } A W = W ^ { T } B A W$ as in Theorem 5.11.

Theorem 12.8. Suppose that a Runge-Kutta method with distinct $c _ { \imath }$ and positive $b _ { i }$ satisfies the simplifying assumptions $B ( 2 s - 2 ) , C ( s - 1 ) , D ( s - 1 )$ (see beginning of Sect.IV.5). Then the method is algebraically stable if and only if $| R ( \infty ) | \leq 1$ (where $R ( z )$ denotes the stability function).

Proof. Since the order of the quadrature formula is $p \geq 2 s - 2$ , the matrix $W$ of Lemma 5.12 is

$$
W = W _ { G } D , \quad D = { \mathrm { d i a g } } ( 1 , \dots , 1 , \alpha ^ { - 1 } ) ,
$$

where $\boldsymbol { W } _ { G } = ( P _ { \jmath - 1 } ( c _ { \imath } ) ) _ { \imath , \jmath = 1 } ^ { s }$ is as in (5.21), and $\begin{array} { r } { \alpha ^ { 2 } = \sum _ { \iota = 1 } ^ { s } \bar { b } _ { i } P _ { s - 1 } ^ { 2 } ( c _ { \iota } ) \ne 0 } \end{array}$ .Us-ing the relation (observe that $W ^ { T } B W = I$ ）

$$
X = W ^ { - 1 } A W = D ^ { - 1 } W _ { G } ^ { - 1 } A W _ { G } D = D W _ { G } ^ { T } B A ( W _ { G } ^ { T } B ) ^ { - 1 } D ^ { - 1 }
$$

and applying Lemma 5.7 with $\eta = s - 1$ and Lemma 5.8 with $\xi = s - 1$ , we obtain

$$
X = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { \cdot \cdot } } & { { } } & { { } } & { { } } \\ { { } } & { { \cdot \cdot } } & { { \cdot \cdot } } & { { - \xi _ { s - 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { \xi _ { s - 2 } } } & { { 0 } } & { { - \alpha \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \alpha \xi _ { s - 1 } } } & { { \beta } } \end{array} \right) .
$$

If this matrix is inserted into (12.10) then, marvellous surprise, everything cancels with the exception of $\beta$ . Therefore, condition (ii) of Theorem 12.4 is equivalent to $\beta \geq 0$

Using the representation (5.31)of the stability function we obtain by develop-ing the determinants

$$
| R ( \infty ) | = \left| { \frac { \operatorname* { d e t } ( X - e _ { 1 } e _ { 1 } ^ { T } ) } { \operatorname* { d e t } X } } \right| = \left| { \frac { \beta d _ { s - 1 } - \alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } } { \beta d _ { s - 1 } + \alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } } } \right| ,
$$

where $d _ { k } = k ! / ( 2 k ) !$ is the determinant of the $k$ -dimensional matrix $X _ { G }$ of (5.13). Since $\alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } > 0$ ,the expression(12.12)isbounded by1iff $\beta \geq 0$ This proves the statement. □

Comparing these theorems with Table 5.13 yields

Theorem 12.9. The methods Gauss, Radau IA, Radau IIA and Lobatto IIIC are algebraically stable and therefore also $B$ -stable. □

# A N -Stability

$A$ -stability theory is based on the autonomous linear equation $y ^ { \prime } = \lambda y$ ，whereas $B$ -stability is based on general nonlinear systems $y ^ { \prime } { = } f ( x , y )$ . The question arises whether there is a reasonable stability theory between these two extremes. A natural approach would be to study the scalar, linear, nonautonomous equation

$$
y ^ { \prime } = \lambda ( x ) y , \qquad \operatorname { R e } \lambda ( x ) \leq 0 ,
$$

where $\lambda ( x )$ is an arbitrarily varying complex-valued function (Burrage & Butcher 1979,Scherer 1979). The somewhat surprising result of this subsection will be that stability for(12.13) will, for most RK-methods, be equivalent to $B$ -stability.

For the problem (12.13) the Runge-Kutta method (12.3) becomes (in vector notation $g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T }$ ， $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T } )$

$$
g = 1 1 y _ { 0 } + A Z g , \quad Z = \mathrm { d i a g } ( z _ { 1 } , \dots , z _ { s } ) , \quad z _ { \jmath } = h \lambda ( x _ { 0 } + c _ { \jmath } h ) .
$$

Computing $g$ from(12.14) and inserting into (12.3a) gives

$$
\begin{array} { r } { y _ { 1 } = K ( Z ) y _ { 0 } , \quad K ( Z ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 } . } \end{array}
$$

Definition 12.10. A Runge-Kutta method is called AN -stable, if

$$
| K ( Z ) | \leq 1 \quad \left\{ { \begin{array} { l } { { \mathrm { f o r ~ a l l ~ } } Z = \mathrm { d i a g } ( z _ { 1 } , \ldots , z _ { s } ) { \mathrm { ~ s a t i s f y i n g ~ R e ~ } } z _ { j } \leq 0 } \\ { { \mathrm { a n d ~ } } z _ { \jmath } = z _ { k } { \mathrm { ~ w h e n e v e r ~ } } c _ { \jmath } = c _ { k } \ ( j , k = 1 , \ldots , s ) . } \end{array} } \right.
$$

Comparing (12.15) with (3.2) we find that

$$
K \big ( \mathrm { d i a g } ( z , z , \ldots , z ) \big ) = R ( z ) ,
$$

the usual stability function. Further, arguing as with (12.4), $B$ -stability implies $A N$ -stability. Therefore we have:

Theorem 12.11. For Runge-Kutta methods it holds

$$
B \cdot s t a b l e \quad \Rightarrow \quad A N \cdot s t a b l e \quad \Rightarrow \quad A \cdot s t a b l e .
$$

For the trapezoidal rule $y _ { 1 } = y _ { 0 } + { \textstyle \frac { h } { 2 } } \big ( f ( x _ { 0 } , y _ { 0 } ) + f ( x _ { 1 } , y _ { 1 } ) \big )$ the function $\bar { \kappa } ( Z )$ of (12.15) is given by

$$
K ( Z ) = \frac { 1 + z _ { 1 } / 2 } { 1 - z _ { 2 } / 2 } .
$$

Putting $z _ { 2 } = 0$ and $z _ { 1 }  - \infty$ we see that this method is not $A N$ -stable. More generally we have the following result.

Theorem 12.12 (Scherer 1979). The Lobatto IIIA and Lobatto IIIB methods are not $A N$ -stable and therefore not $B$ -stable.

Proof. As in Proposition 3.2 we find that

$$
K ^ { ^ { \prime } } ( Z ) = { \frac { \operatorname * { d e t } ( I - ( A - 1 1 b ^ { T } ) Z ) } { \operatorname * { d e t } ( I - A Z ) } } .
$$

By definition, the first row of $A$ and the last row of $A - \mathbb { 1 } b ^ { T }$ vanish for the Lobatto IIIA methods (compare also the proof of Theorem 5.5). Therefore the denominator of $K ( Z )$ does not depend on $z _ { 1 }$ and the numerator not on $z _ { s }$ . If we put for example $z _ { 2 } = . . . = z _ { s } = 0$ , the function $K ( Z )$ is unbounded for $z _ { 1 }  - \infty$ · This contradicts $A N$ -stability.

For the Lobatto IIB methods, one uses in a similar way that the last column of $A$ and the first column of $A - \mathbb { 1 } b ^ { T }$ vanish. □

The following result shows,as mentioned above, that $A N$ -stability is much closer to $B$ -stability than to $A$ -stability.

Theorem 12.13 (Burrage & Butcher 1979). Suppose that

$$
| K ( Z ) | \leq 1 \left\{ \begin{array} { l l } { f o r a l l Z = \mathrm { d i a g } ( z _ { 1 } , \ldots , z _ { s } ) w i t h \mathrm { R e } z _ { \jmath } \leq 0 } \\ { a n d | z _ { \jmath } | \leq \varepsilon f o r s o m e \varepsilon > 0 , } \end{array} \right.
$$

then the method is algebraically stable (and hence also $B$ -stable).

Proof. For $\Delta f _ { \imath } : = z _ { \imath } \Delta g _ { \imath }$ and $\Delta y _ { 0 } = 1$ the result of (12.5) is $\Delta { y } _ { 1 } = K ( Z )$ . Taking care of the fact that $z _ { \imath }$ need not be real, the computation of the proof of Theorem 12.4 shows that

$$
| K ( Z ) | ^ { 2 } - 1 = 2 \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } \mathrm { R e } z _ { \imath } | g _ { \imath } | ^ { 2 } - \sum _ { \imath , \jmath = 1 } ^ { s } m _ { \imath \jmath } \bar { z } _ { \imath } \bar { g } _ { \imath } z _ { \jmath } g _ { \jmath } .
$$

Here $g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T }$ is a solution of (12.14) with $y _ { 0 } = 1$ ·

To prove that $b _ { \imath } \geq 0$ ,choose $z _ { \imath } = - \varepsilon < 0$ and $z _ { \jmath } = 0$ for $j \neq \imath$ . Assumption (12.19) together with (12.20) implies

$$
- 2 \varepsilon b _ { \iota } | g _ { \iota } | ^ { 2 } - m _ { \iota \iota } \varepsilon ^ { 2 } | g _ { \iota } | ^ { 2 } \leq 0 .
$$

For sufficiently small $\varepsilon , g _ { \imath }$ is close to 1 and the second term in(12.21) is negligible for $\boldsymbol { b } _ { \imath } \neq 0$ . Therefore, $b _ { \imath }$ must be non-negative.

To verify the second condition of algebraic stability we choose the purely imaginary numbers $z _ { \jmath } = i \varepsilon \xi _ { \jmath } \left( \xi _ { \jmath } \in \mathbb { R } \right)$ . Since again $g _ { \imath } = 1 + \mathcal { O } ( \varepsilon )$ for $\varepsilon \to 0$ , we have from (12.20) that

$$
- \varepsilon ^ { 2 } \sum _ { \ i , \jmath = 1 } ^ { s } m _ { \imath \jmath } \xi _ { \imath } \xi _ { \jmath } + \mathcal { O } ( \varepsilon ^ { 3 } ) \leq 0 .
$$

Therefore, $M = ( m _ { \imath \jmath } )$ has to be non-negative definite.

Combining this result with those of Theorems 12.4 and 12.11 we obtain

Corollary 12.14. For non-confluent Runge-Kutta methods (i.e., methods with all $c _ { \ j }$ distinct) the concepts of $A N$ -stability, $B$ -stability and algebraic stability are equivalent. □

An equivalence result (between $B$ - and algebraic stability) for confuent Runge-Kutta methods is much more difficult to prove (see Theorem 12.18 below) and will be our next goal. To this end we first have to discuss reducible methods.

# Reducible Runge-Kutta Methods

For an RK-method (12.3) it may happen that for alldiferential equations (12.1)

i） some stages don't influence the numerical solution;   
ii） several $g _ { \imath }$ are identical.

In both situations the Runge-Kuta method can be simplified to an “equivalent" one with fewer stages.

For an illustration of situation (i) consider the method of Table 12.1. Its numerical solution is independent of $g _ { 2 }$ and equivalent to the implicit Euler solution. For the method of Table 12.2 one easily verifies that $g _ { 1 } = g _ { 2 }$ , whenever the system (12.3b) possesses a unique solution. The method is thus equivalent to the implicit mid-point rule.

Table 12.2. $S$ -reducible method   

<table><tr><td>1/2 1/2</td><td>1/2 0 1/4 1/4</td></tr><tr><td></td><td>1/2 1/2</td></tr></table>

Table 12.1. $D J$ -reducible method   
Table 12.3. $D J$ -reducibility   

<table><tr><td>1 1/2</td><td>1 0 1/4 1/4</td></tr><tr><td></td><td>1 0</td></tr></table>

The situation (i) above can be made more precise as follows:

Definition 12.15 (Dahlquist & Jeltsch 1979). A Runge-Kutta method is called $D J$ -reducible, if for some non-empty index set $T \subset \{ 1 , \ldots , s \}$ ，

$$
b _ { _ { J } } = 0 \quad { \mathrm { f o r } } \quad { _ { \mathcal { J } } } \in T \qquad { \mathrm { a n d } } \qquad a _ { _ { \iota _ { \mathcal { J } } } } = 0 \quad { \mathrm { f o r } } \quad i \notin T , { \ i \in T } .
$$

Otherwise it is called $D J$ -irreducible.

Condition (12.22) implies that the stages $\jmath \in T$ don't influence the numerical solution. This is best seen by permuting the stages so that the elements of $T$ are the last ones (Cooper 1985). Then the Runge-Kutta tableau becomes that of Table 12.3.

$$
{ \frac { c _ { 1 } } { c _ { 2 } } } \quad \left| { \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { A _ { 2 1 } } & { A _ { 2 2 } } \\ { b _ { 1 } ^ { T } } & { 0 } \end{array} } \right| \qquad \Rightarrow \qquad { \frac { c _ { 1 } } { b _ { 1 } ^ { T } } } \quad \left| { \begin{array} { l } { A _ { 1 1 } } \\ { b _ { 1 } ^ { T } } \end{array} } \right|
$$

An interesting property of $D J$ -irreducible and algebraically stable Runge-Kuta methods was discovered by Dahlquist & Jeltsch (1979).

Theorem 12.16. A $D J$ -irreducible, algebraically stable Runge-Kutta method satisfies

$$
b _ { \ i } > 0 f o r i = 1 , \ldots , s .
$$

Proof. Suppose $b _ { \jmath } = 0$ for some index $j$ . Then $m _ { j j } = 0$ by definition of $M$ . Since $M$ is non-negative definite,all elements in the $j$ th column of $M$ must vanish (Exercise 11） so that $b _ { \imath } a _ { \imath \jmath } = 0$ for all $i$ ．This implies (12.22) for the set $T =$ $\{ j | b _ { j } = 0 \}$ , a contradiction to $D J$ -irreducibility. □

An algebraic criterion for the situation (ii) was given for the first time (but incompletely) by Stetter(1973,p.127) and finally by Hundsdorfer & Spijker(1981), see also Butcher(1987),p.319,and Dekker & Verwer (1984), p.108.

Definition 12.17. A Runge-Kutta method is $S$ -reducible,if for some partition $( S _ { 1 } , \ldots , S _ { r } )$ of $\{ 1 , \ldots , s \}$ with $r < s$ we have for all $l$ and $m$

$$
\sum _ { k \in S _ { m } } a _ { \iota k } = \sum _ { k \in S _ { m } } a _ { \jmath k } \quad \mathrm { i f } \quad \iota , \dot { \jmath } \in S _ { l } .
$$

Otherwise it is called $S$ -irreducible. Methods which are neither $D J$ -reducible nor $S$ -reducible are called irreducible.

In order to understand condition (12.23) we assume that, after a certain permutation of the stages, $l \in S _ { l }$ for $l = 1 , \ldots , r$ . We then consider the $\pmb { \gamma }$ -stage method with coefficients

$$
c _ { \iota } ^ { \ast } = c _ { \iota } , \qquad a _ { \iota \ j } ^ { \ast } = \sum _ { k \in S _ { \jmath } } a _ { \iota k } , \qquad b _ { \jmath } ^ { \ast } = \sum _ { k \in S _ { \jmath } } b _ { k } .
$$

Application of this new method to (12.1) yields $g _ { 1 } ^ { * } , \ldots , g _ { r } ^ { * } , y _ { 1 } ^ { * }$ and one easily verifies that $g _ { \imath }$ and $y _ { 1 }$ defined by

$$
g _ { \ i } = g _ { l } ^ { \ast } \quad \mathrm { i f } \quad i \in S _ { l } , \qquad y _ { 1 } = y _ { 1 } ^ { \ast } ,
$$

are a solution of the original method (12.3). For the method of Table 12.2 we have $S _ { 1 } = \{ 1 , 2 \}$ . A further example of an $S$ -reducible method is given in Table 12.4 of Sect.II.12 ( $\mathbfcal { S } _ { 1 } = \{ 1 , 2 , 3 \}$ and $S _ { 2 } = \{ 4 \}$ ）.

# The Equivalence Theorem for $S$ -Irreducible Methods

Theorem 12.18 (Hundsdorfer & Spijker 1981). For $S$ -irreducible Runge-Kuta methods,

Proof. Because of Corollary 12.14,which covers nearly all cases of practical importance - and which was much easier to prove - this theorem seems to be of little practical interest. However, it is an interesting result which had been con-jectured by many people for many years, so we reproduce its proof, which also includes the three Lemmas 12.19-12.21. The counter example of Exercise 6 below shows that $S$ -irreducibility is a necessary hypethesis.

By Theorem 12.4 it is sufficient to prove that $B$ -stability and $S$ -irreducibility imply algebraic stability. For this we take s complex numbers $z _ { 1 } , \dots , z _ { s }$ which satisfy $\mathrm { R e } z _ { _ { \jmath } } < 0$ and $| z _ { \jmath } | \leq \varepsilon$ for some sufficiently small $\varepsilon > 0$ . We show that there exists a continuous function $f : \mathbb { C } \to \mathbb { C }$ satisfying

$$
\operatorname { R e } { \big \langle } f ( u ) - f ( v ) , u - v { \big \rangle } \leq 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } u , v \in \mathbb { C } ~ ,
$$

such that the Runge-Kutta solutions $y _ { 1 } , g _ { \imath }$ and $\widehat { y } _ { 1 } , \widehat { g } _ { \iota }$ corresponding to $y _ { 0 } = 0$ ， $\widehat { y } _ { 0 } = 1$ ， $h \approx 1$ satisfy

$$
f ( { \widehat { g } } _ { \imath } ) - f ( g _ { \imath } ) = z _ { \imath } ( { \widehat { g } } _ { \imath } - g _ { \imath } ) .
$$

This yields $\widehat { y } _ { 1 } - y _ { 1 } = K ( Z )$ with $K ( Z )$ given by (12.15). $B$ -stability then implies $| K ( Z ) | \le 1$ . By continuity of $K ( Z )$ near the origin we then have $| \mathit { K } ( Z ) | \le 1$ for all $z _ { \jmath }$ which satisfy $\mathrm { R e } z _ { \jmath } \leq 0$ and $| z _ { \jmath } | \leq \varepsilon$ ， so that Theorem 12.13 proves the statement.

Construction of the function $f$ : we denote by $\Delta g _ { i }$ the solution of

$$
\Delta g _ { \imath } = 1 + \sum _ { \jmath = 1 } ^ { s } a _ { i j } z _ { \jmath } \Delta g _ { \jmath }
$$

(the solution exists uniquely if $| z _ { \jmath } | \leq \varepsilon$ and $\varepsilon$ is sufficiently small). With $\xi , \eta$ given by Lemma 12.19 (below) we define

$$
\begin{array} { l l } { { g _ { \iota } = t \eta _ { \iota } , } } & { { f ( g _ { \iota } ) = t \xi _ { \iota } } } \\ { { \widehat { g } _ { \iota } = g _ { \iota } + \Delta g _ { \iota } , } } & { { f ( \widehat { g } _ { i } ) = f ( g _ { \iota } ) + z _ { \iota } \Delta g _ { \iota } . } } \end{array}
$$

This is well-defined for sufficiently large $t$ (to be fixed later), because the $\eta _ { \imath }$ are distinct. Clearly, $g _ { \imath }$ and $\widehat { \boldsymbol { g } } _ { \imath }$ represent a Runge-Kutta solution for $y _ { 0 } = 0$ and $\widehat { y } _ { 0 } = 1$ ， and (12.26) is satisfied by definition.

We next show that

$$
\operatorname { R e } { \big \langle } f ( u ) - f ( v ) , u - v { \big \rangle } < 0 \qquad { \mathrm { i f } } \qquad u \neq v
$$

is satisfied for $u , v \in D = \{ g _ { 1 } , \dotsc , g _ { s } , \widehat { g } _ { 1 } , \dotsc , \widehat { g } _ { s } \}$ . This follows from the construction of $\xi , \eta$ ,if $u , v \in \{ g _ { 1 } , \dotsc , g _ { s } \}$ . If $u \simeq g _ { \tau }$ and $\boldsymbol { v } = \widehat { \boldsymbol { g } } _ { \iota }$ this is a consequence of (12.26). For the remaining case $u = \widehat { g } _ { \iota } , v \in D \setminus \{ g _ { \iota } , \widehat { g } _ { \iota } \}$ we have

$$
\langle f ( u ) - f ( v ) , u - v \rangle = t ^ { 2 } ( \xi _ { \imath } - \xi _ { \jmath } ) ( \eta _ { \imath } - \eta _ { \jmath } ) + \mathcal { O } ( t ) \quad \mathrm { f o r } \quad t \to \infty ,
$$

so that (12.28) is satisfied, if $t$ is sufficiently large. Applying Lemma 12.20 below we find a continuous function $f : \mathbb { C } \to \mathbb { C }$ that extends (12.27) and satisfies (12.25).

To complete the above proof we still need the following three lemmas:

Lemma 12.19. Let $A$ be the coeffcient matrix of an $S$ -irreducible Runge-Kutta method. Then there exist vectors $\xi \in \mathbb { R } ^ { s }$ and $\eta = A \xi$ such that

$$
( \xi _ { \iota } - \xi _ { \jmath } ) ( \eta _ { \iota } - \eta _ { \jmath } ) < 0 f o r i \neq j .
$$

Proof (see Butcher 1982). The first idea is to put

$$
\boldsymbol { \xi } = \mathbb { 1 } - \varepsilon A \mathbb { 1 } \quad \mathrm { w i t h } \quad \mathbb { 1 } \mathbb { = } ( 1 , 1 , \dots , 1 ) ^ { T } ,
$$

so that $\eta$ becomes

$$
\eta = A \xi = A \mathbb { 1 } - \varepsilon A ^ { 2 } \mathbb { 1 } .
$$

f $c _ { \imath } \neq c _ { \jmath }$ for all $i , j$ ,then $\xi _ { i } - \xi _ { { \scriptscriptstyle 3 } } \neq 0$ and for $\varepsilon$ sufficientlysmall we have $\eta _ { i } - \eta _ { j }$ of opposite sign, thus (12.29) is true.

For a proof of the remaining cases,we shall construct recursively vectors $v _ { 0 } , v _ { 1 } , v _ { 2 } , \ldots$ and denote by $P _ { k }$ the partition of $\{ 1 , \ldots , s \}$ defined by the equivalence relation

$$
i \sim j \quad \iff \quad ( \boldsymbol { v } _ { q } ) _ { \iota } = ( \boldsymbol { v } _ { q } ) _ { \jmath } \quad \mathrm { f o r } \quad q = 0 , 1 , \ldots , k .
$$

For a given partition $P$ of $\{ 1 , 2 , \ldots , s \}$ we introduce the space

$$
X ( P ) = \{ v \in \mathbb { R } ^ { s } ; ( v ) _ { \imath } = ( v ) _ { j } \quad { \mathrm { i f } } \quad i \sim j \quad { \mathrm { w i t h r e s p e c t t o ~ } } P \} .
$$

With this notation,the method is $S$ -irreducible if and only if

$$
A X ( P ) \not \subset X ( P )
$$

for every partition other than $\{ \{ 1 \} , \{ 2 \} , \dots , \{ s \} \}$

We start with $v _ { 0 } = \mathbb { 1 }$ and $P _ { 0 } = \{ \{ 1 , . . . , s \} \}$ and define

$$
v _ { k + 1 } = \left\{ \begin{array} { l l } { A v _ { k } \quad } & { \mathrm { i f } A v _ { k } \notin X ( P _ { k } ) } \\ { \omega } & { \mathrm { i f } A v _ { k } \in X ( P _ { k } ) } \end{array} \right.
$$

where $\omega$ is an arbitrary vector of $X ( P _ { k } )$ satisfying $A \omega \notin X ( P _ { k } )$ . Such a choice is possible by (12.31). After a finite number of steps, say $m$ ，we arrive at $P _ { m } =$ $\{ \{ 1 \} , \{ 2 \} , \dots , \{ s \} \}$ , because the number of components of $P _ { k }$ is increasing, and strictly increasing after every second step. Therefore all elements of the vector

$$
\xi = v _ { 0 } - \varepsilon v _ { 1 } + \varepsilon ^ { 2 } v _ { 2 } - . . . + ( - \varepsilon ) ^ { m } v _ { m }
$$

are distinct (for sufficiently small $\varepsilon > 0$ ) and (12.29) is satisfied.

Lemma 12.20 (Minty 1962). Let $\mathcal { U } _ { 1 } , \dots , \mathcal { U } _ { k }$ and $f ( u _ { 1 } ) , \ldots , f ( u _ { k } )$ be elements of $\mathbb { R } ^ { n }$ with

$$
\langle f ( u _ { \ i } ) - f ( u _ { \ j } ) , u _ { \ i } - u _ { \ j } \rangle < 0 \qquad f o r \quad i \neq \jmath .
$$

Then there exists a continuous extension $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ satisfying

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 \qquad f o r a l l \quad u , v \in \mathbb { R } ^ { n } .
$$

Proof (Wakker 1985).Define

$$
\gamma = \operatorname* { m a x } _ { \iota \neq j } \frac { \langle f ( u _ { \iota } ) - f ( u _ { \iota } ) , u _ { \iota } - u _ { \jmath } \rangle } { | | f ( u _ { \iota } ) - f ( u _ { \jmath } ) | | ^ { 2 } } < 0
$$

and put $g ( u _ { \iota } ) = 2 \gamma f ( u _ { \iota } ) - u _ { \iota }$ ,so that $\| g ( u _ { \ i } ) - g ( u _ { \ j } ) \| \leq \| u _ { \ i } - u _ { \ j } \|$ . An applica-tion of Lemma 12.21 shows that there exists a continuous extension $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ satisfying $\| g ( u ) - g ( v ) \| \leq \| u - v \|$ (i.e., $g$ is non-expansive). The function

$$
f ( u ) = \frac { 1 } { 2 \gamma } \big ( g ( u ) + u \big )
$$

then satisfies the requirements.

Lemma 12.21 (Kirszbraun 1934). Let $u _ { 1 } , \ldots , u _ { k }$ and $g ( u _ { 1 } ) , \dots , g ( u _ { k } ) \in \mathbb { R } ^ { n } b e$ such that

$$
| | g ( u _ { \ i } ) - g ( u _ { \ j } ) | | \leq | | u _ { \ i } - u _ { \ j } | | \qquad f o r \ i , j = 1 , \ldots , k .
$$

Then there exists a continuous extension $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ such that

$$
\left\| g ( u ) - g ( v ) \right\| \leq \left\| u - v \right\| \qquad f o r a l l \quad u , v \in \mathbb { R } ^ { n } .
$$

Proof. This was once a difficult result in set-theory. A particularly nice proof, of which we give here a “dynamic" version, has been found by I.J. Schoenberg(1953).

![](images/a4c3448ac40215ca50a7afd5804ce8597378870d6cfb00a3890e7237bfcef4f4.jpg)  
Fig.12.1. Construction of $g ( p )$

a) The main problem is to construct for one given point $p$ the extension $g ( p )$ such that (12.33) remains satisfied. We move the points $u _ { \imath }$ into their images $g ( u _ { \ i } )$ by an affine map

$$
u _ { \ i } ( \lambda ) = u _ { \ i } + \lambda ( g ( u _ { \ i } ) - u _ { \ i } ) , \qquad 0 \le \lambda \le 1 , \ i = 1 , \dots , k .
$$

We define $\boldsymbol { r } _ { \imath } = \| u _ { \imath } - p \|$ and shrink, for each $\lambda$ , the balls with center $u _ { \imath } ( \lambda )$ and radius $r _ { \ i } \mu$ until their intersection consists of one point only

$$
\mu ( \lambda ) : = \operatorname* { m i n } \Bigl \{ \mu ; \bigcap _ { i = 1 } ^ { k } \bigl \{ u ; \| u _ { \iota } ( \lambda ) - u \| \le r _ { \iota } \mu \bigr \} \neq \emptyset \Bigr \} .
$$

This intersection point, denoted by $p ( \lambda )$ (see Fig.12.1),depends continuously (except for a possible sudden decrease of $\mu$ if $\lambda = 0$ ） and piecewise differentiably on $\lambda$ . We shall show that $\mu ( \lambda )$ is non-increasing, which means that $g ( p ) : = p ( 1 )$ is a point satisfying (12.33).

We denote the vectors

$$
R _ { \iota } : = u _ { \iota } ( \lambda ) - p ( \lambda ) ,
$$

and have from the hypothesis (12.32) that $\| R _ { \imath } - R _ { \jmath } \| ^ { 2 }$ is non-increasing, hence that $\langle R _ { \iota } - R _ { j } , d R _ { \iota } - d R _ { j } \rangle \leq 0$ or

$$
\langle R _ { \imath } , d R _ { \jmath } \rangle + \langle R _ { \jmath } , d R _ { \imath } \rangle \geq \langle R _ { \imath } , d R _ { \imath } \rangle + \langle R _ { \jmath } , d R _ { \jmath } \rangle .
$$

As can be seen in Fig.12.1, not all points $u _ { \ i } ( \lambda )$ are always “active” in (12.35), i.e., $p ( \lambda )$ lies on the boundary of the shrinked ball centered in $u _ { \ i } ( \lambda )$ . While for $\lambda \simeq 0$ (for which $\| R _ { \imath } \| = r _ { \imath } \mu )$ all four are active,at $\lambda = 1 / 2$ the active points are $u _ { 1 } ( \lambda ) , u _ { 2 } ( \lambda ) , u _ { 3 } ( \lambda )$ ， and finally for $\lambda \simeq 1$ we only have $u _ { 1 } ( \lambda )$ and $u _ { 2 } ( \lambda )$ active. We suppose, for a given $\lambda$ ， that $u _ { 1 } ( \lambda ) , \ldots , u _ { m } ( \lambda ) \ ( m \leq \bar { k } )$ are the active points,which may sometimes require a proper renumbering. The crucial idea of Schoenberg is the fact that $p ( \lambda )$ lies in the convex hull of $u _ { 1 } ( \lambda ) , \dots , u _ { m } ( \lambda )$ ,i.e., there are positive values $c _ { 1 } ( \lambda ) , \ldots , c _ { m } ( \lambda )$ with $\scriptstyle \sum _ { \imath = 1 } ^ { m } c _ { \imath } R _ { \imath } = 0$ . This means that

$$
\begin{array} { r } { \langle \sum _ { \iota } c _ { \iota } R _ { \iota } , \sum _ { \jmath } c _ { \jmath } d R _ { \jmath } \rangle = 0 . } \end{array}
$$

We here apply (12.37) pairwise to $i , j$ and $j , i$ , and obtain

$$
\begin{array} { r } { 0 = \langle \sum _ { \iota } c _ { \iota } R _ { \iota } , \sum _ { \jmath } c _ { \jmath } d R _ { \jmath } \rangle \geq \sum _ { \iota } \langle R _ { \imath } , d R _ { \imath } \rangle \big ( c _ { \iota } \sum _ { \jmath } c _ { \jmath } \big ) . } \end{array}
$$

Since by construction (see (12.36)) all $\Vert R _ { \imath } \Vert$ decrease or increase simultaneously with $\mu$ , and since all $c _ { \scriptscriptstyle \imath } > 0$ , we see that $d \mu \leq 0$ ,i.e., $\mu$ is non-increasing.

b) The rest is now standard (Kirszbraun): we choose a countable dense sequence of points $p _ { 1 } , p _ { 2 } , p _ { 3 } , . . .$ in $\mathbb { R } ^ { n }$ and extend $g$ gradually to these points, so that (12.33) is always satisfied. By continuity (see (12.33)),our function is then defined everywhere. This completes the proof of Lemma 12.21 and with it the proof of Theorem 12.18. □

Nous ne connaissons pas d'exemples de méthodes qui soient $B$ - stables au sens de Butcher et qui ne soient pas $B$ -stables suivant notre definition. (M. Crouzeix 1979)

Remark. Burrage & Butcher (1979) distinguish between $B N$ -stability (based on non-autonomous systems) and $B$ -stability (based on autonomous systems). Since the differential equation constructed in the above proof (see (12.25)) is autonomous, both concepts are equivalent for irreducible methods.

# Error Growth Function

All the above theory deals only with contractivity when the one-sided Lipschitz constant $\nu$ in (12.2) is zero (see Definition 12.2). The question arises whether we can sharpen the estimate when it is known that $\nu < 0$ , and whether we can obtain estimates also in the case when (12.2) holds only for some $\nu > 0$

Definition 12.22 (Burrage & Butcher 1979). Let $\nu$ be given and set $x = h \nu$ ,where $h$ is the step size. We then denote by $\varphi _ { B } ( x )$ the smallest number for which the estimate

$$
\| y _ { 1 } - { \widehat { y } } _ { 1 } \| \leq \varphi _ { B } ( x ) \| y _ { 0 } - { \widehat { y } } _ { 0 } \|
$$

holds for all problems satisfying

$$
\operatorname { R e } { \big \langle } f ( x , y ) - f ( x , z ) , y - z { \big \rangle } \leq \nu \| y - z \| ^ { 2 } .
$$

We call $\varphi _ { B } ( x )$ the error growth function of the method.

We consider here complex-valued functions $f : \mathbb { R } \times \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ ．This is not more general (any such system can be written in real form by considering real and imaginary parts, see Eq.(12.4)), but it is more convenient when working with problems $y ^ { \prime } = \lambda ( x ) y$ ，where $\lambda ( x )$ is complex-valued.

In the case of a linear nonautonomous problem $y ^ { \prime } = A ( x ) y$ ,condition (12.39) becomes $\mu ( A ( x ) ) \leq \nu$ (where $\mu ( \cdot )$ denotes the logarithmic norm; see Sect.I.10). Putting $Z _ { \iota } : = h A ( x _ { 0 } + c _ { \iota } h )$ , the difference of two numerical solutions becomes

$$
y _ { 1 } - { \widehat { y } } _ { 1 } = K ( Z _ { 1 } , \ldots , Z _ { s } ) ( y _ { 0 } - { \widehat { y } } _ { 0 } ) ,
$$

where

$$
K ( Z _ { 1 } , \ldots , Z _ { s } ) = I + ( b ^ { T } \otimes I ) Z \bigl ( I \otimes I - ( A \otimes I ) Z \bigr ) ^ { - 1 } ( \mathbb { 1 } \otimes I ) ,
$$

and $Z$ is the block diagonal matrix with $Z _ { 1 } , \dots , Z _ { s }$ as entries in the diagonal.

Theorem 12.23. The error growth function of an implicit Runge-Kutta method satisfies

$$
\varphi _ { B } ( x ) = \operatorname* { s u p } _ { \mu ( Z _ { 1 } ) \leq x , \ldots , \mu ( Z _ { s } ) \leq x } | | K ( Z _ { 1 } , \ldots , Z _ { s } ) | | .
$$

Proof. Upper Bound. The difference $\Delta { y } _ { 1 } = { y } _ { 1 } - \widehat { y } _ { 1 }$ of two Runge-Kutta solutions satisfies (12.5). The assumption (12.39) implies that $\mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { i } \right. \leq x \| \Delta g _ { i } \| ^ { 2 }$ We shall prove that there exist matrices $Z _ { i }$ $( i = 1 , \ldots , s )$ with $\mu ( Z _ { \imath } ) \leq x$ such that $\Delta f _ { \imath } = Z _ { \imath } \Delta g _ { \imath }$ . This implies $\Delta y _ { 1 } = K ( Z _ { 1 } , \dots , Z _ { s } ) \Delta y _ { 0 }$ and,as a consequence, that the right-hand expression of Eq.(12.41) is an upper bound of $\varphi _ { B } ( x )$

f $\Delta g _ { \imath } = 0$ then $\Delta f _ { \imath } = 0$ and we can take an arbitrary matrix satisfying $\mu ( Z _ { \imath } ) \leq$ $x$ . Therefore,let us consider vectors $f , g$ (with $g \neq 0$ in $\mathbb { C } ^ { n }$ satisfying $\operatorname { R e } \left. f , g \right. \leq$ $x \| g \| ^ { 2 }$ . We put $u _ { 1 } : = g / \| g \|$ ,and complete it to an orthonormal basis $\boldsymbol { u } _ { 1 } , \ldots , \boldsymbol { u } _ { n }$