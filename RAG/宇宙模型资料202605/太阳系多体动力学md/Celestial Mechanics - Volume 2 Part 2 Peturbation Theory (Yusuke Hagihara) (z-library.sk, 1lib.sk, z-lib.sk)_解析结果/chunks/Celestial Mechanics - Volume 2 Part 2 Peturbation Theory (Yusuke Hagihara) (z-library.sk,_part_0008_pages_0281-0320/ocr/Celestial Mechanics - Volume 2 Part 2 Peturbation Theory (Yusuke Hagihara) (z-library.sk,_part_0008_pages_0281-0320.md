where

$$
\phantom { } _ { \nu } D _ { 1 } = \sum _ { k = 1 } ^ { n } \phantom { } _ { \nu } \psi _ { k } ( t ) \frac { \partial } { \partial x _ { k } } + \frac { \partial } { \partial t } , \qquad \phantom { } _ { \nu } D _ { 2 } = D - \phantom { } _ { \nu } D _ { 1 } ,
$$

$$
{ } _ { v } x _ { i a } ( t ) = x _ { i } ^ { ( 0 ) } + \int _ { t _ { 0 } } ^ { t } v \psi _ { i } ( \tau ) \ d \tau .
$$

Then the next-order approximation is obtained from

$$
\begin{array} { l } { { \displaystyle { \mathrm { } _ { \nu + 1 } } x _ { i a } ( t ) = x _ { i } ^ { ( 0 ) } + \int _ { t _ { 0 } } ^ { t } \nu _ { + 1 } \psi _ { i } ( \tau ) d \tau } } \\ { { \displaystyle \quad = { } _ { \nu } x _ { i a } ( t ) + \sum _ { \alpha = 0 } ^ { m } \int _ { t _ { 0 } } ^ { t } \frac { ( t - \tau ) ^ { \alpha } } { \alpha ! } \left[ \nu D _ { 2 } D ^ { \alpha } x _ { i } \right] _ { \nu ^ { \alpha } ( \tau ) , \tau } d \tau } } \\ { { \displaystyle \qquad \quad \qquad \left( \begin{array} { l } { { \displaystyle i = 1 , 2 , . . . , n ; } } \\ { { \displaystyle \nu = 0 , 1 , 2 , . . . } } \end{array} \right) } . } \end{array}
$$

If single-valued functions

$$
X _ { i } ( x _ { 1 } , . . . , x _ { n } , t ) \qquad ( i = 1 , 2 , . . . , n )
$$

have partial derivatives of all orders up to the mth ( $\mathbf { \langle } m \mathbf { \rangle } \gtrapprox 0 \rangle$ in the closed interval

$$
\begin{array} { r } { [ ( { \boldsymbol x } _ { 1 } , . ~ . ~ . , { \boldsymbol x } _ { n } , t ) / | { \boldsymbol x } _ { i } - x _ { i } ^ { ( 0 ) } | \leq b ( i = 1 , 2 , . ~ . . , n ) , \quad | t - t _ { 0 } | \leq a \} , } \end{array}
$$

with the given constants $a , b ;$ ， and the derivatives $D ^ { m } X _ { i } \ ( i = 1 , . . . , n )$ ， continuous in all the arguments in $\pmb { B }$ ，where

$$
D = \sum _ { k = 1 } ^ { n } X _ { k } ( x _ { 1 } , . . . , x _ { n } , t ) { \frac { \partial } { \partial x _ { k } } } + { \frac { \partial } { \partial t } } ,
$$

satisfy the Lipschitz condition

$$
\left| [ D ^ { m } X _ { i } ] _ { x ^ { \prime } , t } - [ D ^ { m } X _ { i } ] _ { x ^ { \prime } , t } \right| \leq K \cdot \sum _ { k = 1 } ^ { n } | x _ { k } ^ { \prime \prime } - x _ { k } ^ { \prime } | \qquad ( i = 1 , . . . , n ) ,
$$

with a positive constant $\kappa ,$ then the sequence $\{ _ { \nu } x _ { i a } ( t ) \}$ defined by the iteration process in the interval $\left| t - t _ { 0 } \right| \le \beta \le a$ tends to the solution ${ \pmb x } _ { i } ( t )$ of the differential equations

$$
\frac { d x _ { i } } { d t } = X _ { i } ( x _ { 1 } ( t ) , . . . , x _ { n } ( t ) , t ) \qquad ( i = 1 , . . . , n )
$$

with the initial condition $x _ { i } ( t _ { 0 } ) = x _ { i } ^ { ( 0 ) } ( i = 1 , . . . , n )$

Stumpff (l968) studied the same problem on the Lie series as Grobner did, and applied it to Kepler's problem and perturbation theory.

Sconzo (1967),and Sconzo,LeSchack,and Tobey (1965) developed two algebraic methods for solving the three-body problem by convergent power series in terms of the independent variable which is either time $t$ or Levi-Civita's regularizing variable $\pmb { u }$ such that $d / d u = ( 1 / V ) ( d / d t ) .$ ， where $V$ is the negative potential energy (Section l7.12). Similarly to Steffensen's approach, Sconzo constructed the coefficients of high-order terms in power series by recursion formulas and accordingly obtained the series by using simple analytical tools for their manipulation.

The solution of

$$
\ddot { \mathfrak { c } } _ { i } = m _ { i } \mu _ { i j } ( { \boldsymbol { x } } _ { j } - { \boldsymbol { x } } _ { i } ) + m _ { k } \mu _ { i k } ( { \boldsymbol { x } } _ { k } - { \boldsymbol { x } } _ { i } ) , \qquad \mu _ { i j } = \frac { 1 } { r _ { i j } ^ { 3 } } ( \dot { \iota } , j = 0 , 1 ,
$$

where $\pmb { r } _ { i j }$ is the distance between the ith and jth bodies, is expanded in the MacLaurin series

$$
x _ { i } = \sum _ { v = 0 } ^ { \infty } x _ { i v } \tau ^ { v } , \qquad x _ { i v } = { \frac { 1 } { \nu ! } } \left| { \frac { d ^ { v } x _ { i } } { d \tau ^ { v } } } \right| _ { \tau = 0 } , \qquad \tau = K t ,
$$

where $\kappa$ is the Gaussian gravitational constant. If $\tau = 0$ is not a collision point, then the series is convergent,as proved by Sundman (Sections 22.1-22.8).By repeated differentiation of the equations of motion we obtain,by Leibnitz's rule,

$$
\begin{array} { l } { { \displaystyle { \mathrm {  ~ \Lambda ~ } ^ { + 2 ) } } ( x _ { i } ) = \sum _ { p = 0 } ^ { \nu } \binom { \nu } { \hat { p } } [ m _ { j } D ^ { ( \nu - p ) } ( \mu _ { i j } ) D ^ { ( \nu ) } ( x _ { j } - x _ { i } ) } } \\ { { \displaystyle ~ + m _ { k } D ^ { ( \nu - p ) } ( \mu _ { i k } ) D ^ { ( \nu ) } ( x _ { k } - x _ { i } ) } } \end{array}
$$

where $\pmb { D }$ stands for $d / d \tau$ Define

$$
\sigma _ { i j } = \frac { 1 } { r _ { i j } ^ { 2 } } \ : s _ { i j } , \ : \ : \ : \ : \ : \ : \ : \ : \epsilon _ { i j } = \frac { 1 } { r _ { i j } ^ { 2 } } \ : \dot { s } _ { i j } ,
$$

where, adding the expressions for $y , z$ as shown for $_ { x }$ ，

$$
r _ { i j } ^ { 2 } = \sum _ { ( y , z ) } [ ( x _ { j } - x _ { i } ) ^ { 2 } ] , \qquad s _ { i j } = \sum _ { ( y , z ) } [ ( x _ { j } - x _ { i } ) D ( x _ { j } - x _ { i } ) ] ,
$$

$$
\dot { s } _ { i j } = \sum _ { ( y , z ) } [ \{ D ( x _ { j } - x _ { i } ) \} ^ { 2 } + ( x _ { j } - x _ { i } ) D ^ { ( 2 ) } ( x _ { j } - x _ { i } ) ] .
$$

Observing that

$$
D \Big ( \frac { 1 } { r _ { i j } ^ { 2 } } \Big ) = - \frac { 2 } { r _ { i j } } \sigma _ { i j } , \qquad D ( \sigma _ { i j } ) = \epsilon _ { i j } - 2 \sigma _ { i j } ^ { 2 } , \qquad D ( \mu _ { i j } ) = - 3 \mu _ { i j } \sigma _ { i j } ,
$$

we obtain successively

$$
\begin{array} { l } { { \displaystyle D ^ { ( 2 ) } ( \mu ) = - 3 \mu ( \epsilon - 5 \sigma ^ { 2 } ) , } } \\ { { \displaystyle D ^ { ( 3 ) } ( \mu ) = - 3 \mu \biggl ( \frac 1 { r ^ { 2 } } D ^ { ( 2 ) } ( s ) - 1 5 \sigma \epsilon + 3 5 \sigma ^ { 3 } \biggr ) , } } \end{array}
$$

Sconzo computed $D ^ { ( \nu ) } ( \mu )$ up to $\nu = 1 3$ on a computer by using symbolic formula manipulation language (Sconzo, LeSchack, and Tobey, 1965; LeSchack and Sconzo, 1968).

$$
\begin{array} { c } { { \displaystyle { } ^ { \upsilon } ( s _ { i j } ) = \displaystyle \sum _ { ( y , z ) } \Biggl \{ \displaystyle \frac { 1 } { 2 } \int _ { \nu } ^ { 2 \nu } + 2 \Biggl \} [ D ^ { ( \nu + 1 ) } ( x _ { j } - x _ { i } ) ] ^ { 2 } } } \\ { { + \displaystyle \sum _ { l = 1 } ^ { \nu + 1 } \binom { 2 \nu + 1 } { \nu + 1 + l } D ^ { ( \nu + 1 - l ) } ( x _ { j } - x _ { i } ) D ^ { ( \nu + 1 + l ) } ( x _ { j } - x _ { i } ) } } \\ { { \qquad \quad ( \nu = 0 , 1 , 2 , . . . , \Biggr \} } } \end{array}
$$

In terms of $\pmb { u }$ the equations of motion are written

$$
\begin{array} { r } { \bar { V } x _ { i } ^ { \prime \prime } + \bar { V } ^ { \prime } x _ { i } ^ { \prime } = \bar { X } _ { i } , } \end{array}
$$

where a prime indicates differentiation with respect to $\pmb { u }$ and the barred quantities are expressed in terms of $\pmb { u }$ and

$$
= \frac { 1 } { m _ { i } } \frac { \partial \log \bar { V } } { \partial x _ { i } } = \frac { 1 } { \bar { V } } \{ m _ { j } \mu _ { i j } ( u ) [ x _ { j } ( u ) - x _ { i } ( u ) ] + m _ { k } \mu _ { i k } ( u ) [ x _ { k } ( u ) - x _ { i } ( u ) ] 
$$

Let

$$
\bar { x } _ { i } ( u ) = \bar { x } _ { i 0 } + \sum _ { v = 1 } ^ { \infty } \bar { x } _ { i v } u ^ { v }
$$

be the power series representing the solution of the above differential equation for $\boldsymbol { x } _ { i }$ .The coefficients $\bar { x } _ { i v }$ $( \nu \geq 2 )$ can be computed recursively, while $\bar { x } _ { i 0 } = x _ { i } ( 0 )$ and $\bar { x } _ { i 1 } = \dot { x } _ { i } ( 0 ) / V ( 0 )$ are known quantities depending on the initial condition for $x _ { i } ( 0 )$ and $\dot { x } _ { i } ( 0 )$ ,by

$$
\bar { x } _ { i \nu } = \frac { 1 } { ( \nu - 1 ) \nu \bar { V } _ { 0 } } \left[ \bar { X } _ { i , \nu - 2 } - ( \nu - 1 ) \sum _ { p = 1 } ^ { \nu - 1 } ( \nu - \rlap / p ) \bar { V } _ { p } \bar { x } _ { i , \nu - p } \right] \qquad ( \nu \equiv
$$

where

$$
\bar { X } _ { i } = \sum _ { \nu = 2 } ^ { \infty } \bar { X } _ { i , \nu - 2 } u ^ { \nu - 2 } , \qquad \bar { V } = \sum _ { p = 0 } ^ { \infty } \bar { V } _ { p } u ^ { p } .
$$

The coefficients $\bar { X } _ { i , \upsilon - 2 }$ and $\varPsi _ { p }$ can be computed by successive approximations, starting with $x _ { i } = x _ { i 0 } + x _ { i 1 } \tau$ ; that is,

$$
\tilde { x } _ { i 2 } = \frac { 1 } { 2 V _ { 0 } ^ { 2 } } \left[ \frac { 1 } { m _ { i } } \frac { \partial V } { \partial x _ { i } } \right] _ { \tau = 0 } - \frac { 1 } { 2 V _ { 0 } ^ { 3 } } V _ { 1 } x _ { 1 } , . . . .
$$

This is the kind of polynomial-series representation of the solution of the three-body problem by Painlevé (Section l0.45).

From the virial integral (Section 22.2)

$$
\frac { 1 } { 2 } \frac { d ^ { 2 } J } { d \tau ^ { 2 } } = V + 2 h , J = \frac { 1 } { m _ { 0 } + m _ { 1 } + m _ { 2 } } \sum _ { i , j } m _ { j } m _ { i } r _ { i j } ^ { 2 } ,
$$

with the energy constant $\pmb { h }$ ,we derive

$$
\frac { 1 } { 2 } \frac { d } { d u } \left( \bar { \cal V } { \cal J ^ { \prime } } \right) = 1 + \frac { 2 h } { \bar { \cal V } } ,
$$

or

$$
{ \scriptstyle \frac { 1 } { 2 } } [ \bar { V } J ^ { \prime } ( u ) - \bar { V } _ { 0 } J ^ { \prime } ( 0 ) ] = u + 2 h \tau ( u ) .
$$

Put

$$
\epsilon ( u ) = { \textstyle \frac { 1 } { 2 } } [ \bar { V } J ^ { \prime } ( u ) - \bar { V } _ { 0 } J ^ { \prime } ( 0 ) ] - [ u + 2 h \tau ( u ) ] .
$$

The successive approximation procedure can be regarded as terminated when for values of $\pmb { u }$ in $\boldsymbol { J }$ we have max $| \epsilon ( u ) | < H ,$ where $\boldsymbol { \mathsf { \Pi } } ^ { H }$ is a suitably chosen positive level of numerical tolerance.

Miachin and Sizova (197O) applied Steffensen's recurrent procedure to the Taylor expansion in the integration of the $\pmb { n }$ -body problem.

# 10.44 THE LIE TRANSFORM

Deprit (1968,1969),as suggested by Hori (1966, Section 9.29), wrote in formal series the canonical transformations:

$$
\begin{array} { l } { \displaystyle { : = y + \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } y ^ { ( n ) } ( y , Y ; t ) , \qquad X = Y + \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } Y ^ { ( n ) } ( y , Y ; t ) , } } \end{array}
$$

the Hamiltonian:

$$
H \equiv H ( x , X ; t ; \epsilon ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } H _ { n } ( x , X ; t ) ,
$$

and the generating function:

$$
W \equiv W ( { \pmb x } , Y ; { \epsilon } ) = { \pmb x } \cdot Y + \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } W _ { n } ( { \pmb x } , Y ) .
$$

Since the von Zeipel transformation

$$
X \equiv X ( x , Y ; \epsilon ) = W _ { x } , ~ y = y ( x , Y ; \epsilon ) = W _ { Y }
$$

presents various inconveniences, especially in the neighborhood of an equilibrium, Deprit constructed a straightforward recurrence formula by considering the transformation $x , y  X ,$ 、 $Y$ based on a Lie transform.

Let the Poisson operation on $W$ ：

$$
( f ; W ) \equiv \sum _ { j = 1 } ^ { m } { \frac { \partial f } { \partial y _ { j } } } { \frac { \partial W } { \partial Y _ { j } } } - { \frac { \partial f } { \partial Y _ { j } } } { \frac { \partial W } { \partial y _ { j } } } \equiv L _ { w }
$$

be called the Lie derivative $L _ { \mathbf { w } }$ generated by $W _ { ☉ }$ .Suppose that there exists the exponential operator

$$
\exp { ( \epsilon L _ { w } ) } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } L _ { w } ^ { n }
$$

at $( y , Y )$ of the phase space, analytic in $\epsilon$ for $\epsilon = 0 .$ .The transformation $( y , Y , \epsilon ) \to ( x , X )$ defined by an analytic mapping

$$
x = \exp { ( \epsilon L _ { w } ) ( y ) } , ~ X = \exp { ( \epsilon L _ { w } ) ( Y ) }
$$

is canonical. The so-called $\ L i e$ transform by this transformation of an analytic function

$$
f ( x , X ; \epsilon ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } f _ { n } ( x , X )
$$

is

$$
f [ x ( y , Y ; \epsilon ) ; X ( y , Y ; \epsilon ) ; \epsilon ] = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } \sum _ { m = 0 } ^ { n } { \binom { n } { m } } L _ { w } ^ { m } f _ { n - m } ( y , Y ) .
$$

If $W$ depends on $\epsilon$ such as $W ( y , Y ; \epsilon )$ ,then we define the transformation

$$
f  \Delta _ { \mathrm { w } } f = L _ { \mathrm { w } } f + \frac { \partial f } { \partial \epsilon } ,
$$

and consider the formal series

$$
E _ { w } ( f ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } f ^ { ( n ) } ( y , Y ; 0 ) .
$$

The mapping $E _ { \mathrm { w } } { : } f { \to } E _ { \mathrm { w } } ( f )$ is called the Lie transform generated by W. The formal power series

$$
x = E _ { \mathrm { { w } } } ( y ) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { n ! } } \epsilon ^ { n } y ^ { ( n ) } ( y , Y ; 0 ) ,
$$

$$
X = E _ { w } ( Y ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } Y ^ { ( n ) } ( y , Y ; 0 )
$$

define a completely canonical mapping $( y , Y , \epsilon ) \to ( x , X )$ . If $( x , X )$ is the solution with $( y , Y )$ at $\epsilon = 0$ of the canonical system

$$
\frac { d x } { d \epsilon } = \frac { \partial } { \partial X } W ( x , X ; \epsilon ) , \frac { d X } { d \epsilon } = - \frac { \partial } { \partial x } W ( x , X ; \epsilon ) ,
$$

then the expansion of the solution $( x , X )$ in power series of $\epsilon$ results in the above formal series.More generally along the solution $[ x ( y , Y ; \epsilon )$ ， $X ( y , Y ; \epsilon ) ]$ of the canonical equations we have

$$
f [ x ( y , Y ; \epsilon ) , X ( y , Y ; \epsilon ) ; \epsilon ] = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \epsilon ^ { n } ( \Delta _ { W } ^ { n } f ) _ { \epsilon = 0 } ,
$$

or symbolically

$$
f [ E _ { w } ( x ) , E _ { w } ( X ) ; \epsilon ] = [ E _ { w } ( f ) ] ( y , Y ; \epsilon ) .
$$

This is the rule for converting a function $f \circ \mathbf { f } \ x , X ,$ and $\epsilon$ into a function with arguments $y , \ Y ,$ and $\epsilon$ through the above canonical mapping. When both $W ( y , Y ; \epsilon )$ and $f$ are power series of $\epsilon$ then the coefficients $f ^ { ( n ) } ( y , Y ; 0 )$ of the series for ${ \pmb { E } } _ { \pmb { w } } ( f )$ can be constructed in a simple recurrence formula

$$
f _ { n } ^ { ( k ) } ( y , Y ; \epsilon ) = f _ { n + 1 } ^ { ( k - 1 ) } ( y , Y ; \epsilon ) + \sum _ { m = 0 } ^ { n } { \binom { n } { m } } L _ { m + 1 } f _ { n - m } ^ { ( k - 1 ) } ( y , Y ; \epsilon )
$$

(see Kamel, 1969).

Deprit and Rom (1969) applied this perturbation technique of Deprit, based on Lie transforms, for programming the analytical solution of the main problem in satellite theory. Short- and long-period displacement as well as the secular terms have been obtained up to the third order in $J _ { 2 }$ as power series of the eccentricity. In order to avoid the singularity due to the zero eccentricity they used $F = l + g $ $C = e \cos g $ ， $S = e \sin g ;$ $h , H ,$ and $L = { \sqrt { \mu a } }$ .They carried out two successive canonical transformations and obtained the constants of motion from the initial conditions.They applied the method to artifcial earth satellites Anna 1B and Relay II after about 3OoO revolutions.They say that Lie transforms supersede von Zeipel's method.

Shniad (197O) showed the equivalence of von Zeipel's mappings and Lie transforms.Curtis (1970) modified Brown's method (Section 9.14) such that the canonical transformations are performed by means of Lie series.The modified method produces a set of transformations in which not only the original variables are determined as explicit functions of the transformed variables but the transformed variables are also given as explicit functions of the original variables, thus enabling us to obtain the constants of integration as functions of the initial conditions.

Déprit,Henrard,and Rom (l970,1970a) applied the method of Lie transforms to obtain an analytical lunar ephemeris, that is,a general approximate solution applying to any single moon whose orbit satisfies certain a priori assumptions; the coordinates and velocity components come out as literal expressions in terms of the initial constants,and the dynamical parameters throughout the theory as mere symbols without being given any numerical value.

In the first stage,the barycenter of the pair (earth and moon） is supposed to move around the sun in a given Keplerian orbit. This initial stage is called the main problem and its solution constitutes the solar part of an analytical lunar ephemeris. In the second stage the secondary perturbations are studied by means of algebraic construction.The third stage is devoted to writing analytically the partial derivatives with respect to the astronomical constants to be determined from observations, evaluating the constants numerically,and substituting these numbers in the analytical expressions so as to obtain a numerical lunar ephemeris.

Déprit, Henrard,and Rom used, instead of Delaunay's variables $l , g ,$ $h , L , G , H ,$ the variables

$$
\begin{array} { l l } { { \lambda = l + g + h , ~ } } & { { ~ \displaystyle \rlap / { p } = - g - h , ~ } } \\ { { \Lambda = L , ~ } } & { { ~ \displaystyle P = L - G , ~ Q = G - H ; } } \end{array}
$$

the functions $E ( L , P ) > 0$ and $J ( L , Q ) > 0$ such that

$$
2 P = L E ^ { 2 } , \qquad 2 Q = L J ^ { 2 } ,
$$

or

$$
\begin{array} { r } { E = 2 \sin \frac { 1 } { 2 } \phi , ~ J = 2 ( 1 - \frac { 1 } { 2 } E ^ { 2 } ) ^ { 1 / 2 } \sin \frac { 1 } { 2 } I , } \end{array}
$$

where sin $\phi = e$ and $\boldsymbol { \mathit { I } }$ is the inclination; and

$$
F = l + g , ~ D = \lambda - \lambda ^ { \prime } = l + g + h - l ^ { \prime } - g ^ { \prime } ,
$$

which had been introduced by Delaunay as the mean elongation of the moon to its node and of the mean elongation of the moon to the sun respectively. They found that these variables are more convenient in constructing the partial derivatives in the development of the analytical lunar ephemeris.They(l97Oa）computed the series numerically for the mean motions of the node and perigee, and found agreement to within $1 ^ { \prime \prime }$ per Julian century with Brown's values as modified by Eckert (Section 11.7).

They compared the result of the analytical lunar ephemeris with Delaunay's analytical solutions. They found Brouwer's conjecture of using von Zeipel's algorithm (Section 9.20) to be troublesome. They showed that the difficulty raised by von Zeipel's method can be avoided by using Lie transforms.In the main problem the elimination of the monthly terms brings in divisors of the form $j + k m$ ,where $\pmb { m }$ is the ratio $n ^ { \prime } / n$ . Delaunay developed them systematically in powers of $m$ . Brouwer suggested the examination of whether these binomial expansions would be the primary cause of slow convergence in powers of $m$ .The answer is in the negative according to Déprit.

Kamel (l970） recently presented asymptotic recurrence formulas for treating nonlinear oscillation problems,on the basis of a Lie transform of Déprit for Hamiltonian systems.He extended the theory to non-Hamiltonian equations.Henrard (l970） presented a simpler algorithm by approaching the problem from an intrinsic viewpoint,and completed Kamel's theory by establishing the rules for inverting the transformation generated by the perturbation theory.

# 10.45EXPANSIONS IN POLYNOMIAL SERIES

As will be shown in Chapter 22,Painlevé (1896,1897,1897a） has proved that the solution ${ \pmb x } ( t )$ of the three-body problem can be expanded

in power series of $\pmb \theta$ within a circle of unit radius in the complex plane of $\theta _ { \mathrm { { i } } }$ ,such that (Sections 17.9-17.19)

$$
\theta = \frac { \exp { \left( \frac { \pi t } { 2 \Omega } \right) } - 1 } { \exp { \left( \frac { \pi t } { 2 \Omega } \right) } + 1 } ,
$$

if ${ \pmb x } ( t )$ is holomorphic in the strip with width $\mathbf { \boldsymbol { 2 } } \Omega$ bounded by two straight lines parallel to and on both sides of the real axis in the complex plane of $t$ ; and that the solution ${ \pmb x } ( t )$ can be expanded in polynomial series

$$
x ( t ) = P _ { 0 } ( t ) + P _ { 1 } ( t ) + \cdot \cdot \cdot + P _ { j } ( t ) + \cdot \cdot \cdot
$$

if ${ \pmb x } ( t )$ is holomorphic for real values of $t .$ ，The conditions are that all three mutual distances are inferiorly bounded,and that the smallest of the three mutual distances tends to zero or to a finite value as $\pmb { t }$ increases to infinity.The conditions for the exceptional cases,e.g., for collisions, will be discussed in Chapter 22.On the other hand,Weierstrass has shown that an arbitrary function with certain restrictions can be approximated by polynomial series -for example, the interpolatory series (Norlund, 1926;Walsh, l956)- in contrast to the trigonometric series frequently employed in the foregoing chapters.We propose to deal with such expansions in polynomial series, because these are convenient for manipulating on modern computers.

Mittag-Leffer (1900,1901,1902,1905,1920),Painlevé (1899,1902), Picard (1899),Montel (1910), Bernstein (1926), Borel (1928), Jackson (1930),and recently Boas and Buck (1958) and Meinardus (1964) dis-cussed the expansions of analytic functions in polynomial series. Let $f ( z )$ be an analytic holomorphic function at the origin $z = 0$ ，such that

$$
f ( z ) = f ( 0 ) + \frac { z } { 1 } f ^ { \prime } ( 0 ) + \cdot \cdot \cdot + \frac { z ^ { n } } { n ! } f ^ { \scriptscriptstyle ( n ) } ( 0 ) + \cdot \cdot \cdot
$$

in the Mittag-Leffer star region $\pmb { A }$ ，that is, the set of points attainable from the origin by semi-straight lines without meeting any of the singular points of $f ( z )$ . Put

$$
\begin{array} { l } { \dot { z } ) = \frac { z ^ { n } } { n ! } f ^ { ( n ) } ( 0 ) c _ { n } ^ { ( n ) } + \frac { z ^ { n - 1 } } { ( n - 1 ) ! } f ^ { ( n - 1 ) } ( 0 ) c _ { n - 1 } ^ { ( n ) } + \cdot \cdot \cdot } \\ { \qquad + \frac { z } { 1 } f ^ { \prime } ( 0 ) c _ { 1 } ^ { ( n ) } + f ( 0 ) c _ { 0 } ^ { ( } } \end{array}
$$

where $c _ { j } ^ { ( n ) }$ are numerical; then the polynomial series $\scriptstyle \sum _ { n } P _ { n } ( z )$ tends to $f ( z )$ in any star region $\pmb { A }$ ，and the polynomial series is divergent in

general on the exceptional semi-straight lines drawn from the origin beyond the singular points,i.e., outside $A$

Consider a differential equation

$$
\frac { d x } { d t } = f ( x , t ) ,
$$

for which $f , \partial f / \partial x , \partial ^ { 2 } f / \partial x ^ { 2 } , . . .$ are continuous functions of $_ x$ and $t .$ By Cauchy's existence theorem for the solutions of differential equations, the integral of this equation with the initial condition $\boldsymbol { x } = \boldsymbol { x } _ { 0 }$ at $t = t _ { 0 }$ is convergent ifit is continuous under this condition.Dividing the interval from $t _ { 0 }$ to $t$ into $\scriptstyle { \pmb { n } }$ parts at $t _ { 0 } , t _ { 1 } , . . . , t _ { n - 1 }$ we consider, following Cauchy and Lipschitz (Ince, 1927),

$$
\begin{array} { l } { { x _ { 1 } - x _ { 0 } = \displaystyle \frac { t } { n } f ( t _ { 0 } , x _ { 0 } ) , } } \\ { { { } } } \\ { { x _ { 2 } - x _ { 1 } = \displaystyle \frac { t } { n } f ( t _ { 1 } , x _ { 1 } ) , } } \end{array}
$$

$$
x _ { n } - x _ { n - 1 } = { \frac { t } { n } } f ( t _ { n - 1 } , x _ { n - 1 } ) ,
$$

and obtain $\phi _ { n } ( x _ { 0 } , t )$ for $x _ { n }$ ，which, for $t _ { 0 } , \ldots , \alpha ^ { \prime }$ ， $\alpha ^ { \prime } < \alpha$ ，represents the integral of the differential equation with the preassigned approximation $\epsilon$ for sufficiently large $_ { n }$ . The integral can be represented by a polynomial series

$$
P _ { 1 } ( x _ { 0 } , t ) + \cdot \cdot \cdot + P _ { j } ( x _ { 0 } , t ) + \cdot \cdot \cdot ,
$$

which is convergent in $t _ { 0 } , \ldots , \alpha$ and uniformly convergent in $t _ { 0 } , \ldots , \alpha ^ { \prime }$ This theorem of Picard (1899) can be generalized to a system of differential equations.

Goursat (1903） expanded $1 / ( 1 - x )$ of the solution of $d y / d x = y ^ { 2 }$ in polynomial series.Put

$$
U _ { 0 } ^ { ( n ) } = 1 , \qquad U _ { 1 } ^ { ( n ) } = 1 + \frac { x } { n } , \qquad U _ { 2 } ^ { ( n ) } = 1 + \frac { 2 x } { n } + \frac { 2 x ^ { 2 } } { n ^ { 2 } } + \frac { x ^ { 3 } } { n ^ { 3 } } ,
$$

$$
\ldots ; \qquad U _ { p + 1 } ^ { ( n ) } = U _ { p } ^ { ( n ) } + \frac { x } { n } ( U _ { p } ^ { ( n ) } ) ^ { 2 } \qquad ( \pmb { \hat { p } } \equiv n - 1 ) ,
$$

where $U _ { p } ^ { ( n ) }$ is a polynomial of degree $2 ^ { n } - 1$ .Let $_ { x }$ be nonreal and not larger than unity,and consider the sequence $u _ { p } ^ { ( n ) }$ such that

$$
\begin{array} { c c c } { { u _ { 0 } ^ { ( n ) } = 1 , \quad } } & { { u _ { 1 } ^ { ( n ) } = \displaystyle { \frac { 1 } { 1 - x / n } } , \quad } } & { { . . . , \quad u _ { p } ^ { ( u ) } = \displaystyle { \frac { 1 } { 1 - p x / n } } , } } \\ { { } } & { { } } & { { } } \\ { { . . . , \quad } } & { { u _ { n } ^ { ( n ) } = \displaystyle { \frac { 1 } { 1 - x } } . } } \end{array}
$$

We can see that $\begin{array} { r } { \left| u _ { p } ^ { ( n ) } \right| \le M , } \end{array}$ if $| 1 / ( 1 - z ) | < M$ as $z$ describes a straight line segment from $z = 0$ to $z = x$ Furthermore, we have

$$
u _ { p + 1 } ^ { ( n ) } = u _ { p } ^ { ( n ) } + \frac { x } { n } ( u _ { p } ^ { ( n ) } ) ^ { 2 } + \frac { x ^ { 2 } } { n ^ { 2 } } ( u _ { p } ^ { ( n ) } ) ^ { 2 } u _ { p + 1 } ^ { ( n ) } .
$$

Subtracting the sequence of $U _ { p } ^ { ( n ) }$ from that of $u _ { p } ^ { ( n ) }$ , we obtain

$$
\delta _ { p + 1 } ^ { ( n ) } = \delta _ { p } ^ { ( n ) } + \frac { x } { n } \delta _ { p } ^ { ( n ) } ( U _ { p } ^ { ( n ) } + u _ { p } ^ { ( n ) } ) - \frac { x ^ { 2 } } { n ^ { 2 } } ( u _ { p } ^ { ( n ) } ) ^ { 2 } u _ { p + 1 } ^ { ( n ) } .
$$

Here we have

$$
\begin{array} { r } { \big | \delta _ { p + 1 } ^ { \mathfrak { o } } \big | < \big | \delta _ { p } ^ { \mathfrak { o } } \big | \bigg [ 1 + \frac { \rho } { m } ( 2 M + \big | \delta _ { p } ^ { \mathfrak { o } } \big | ) \bigg ] + \frac { \rho ^ { 2 } M ^ { 3 } } { n ^ { 2 } } , \qquad \rho = | x | , } \end{array}
$$

since

$$
\big | U _ { p } ^ { ( n ) } + u _ { p } ^ { ( n ) } \big | < 2 M + \big | \delta _ { p } ^ { ( n ) } \big | .
$$

Consider also the sequence $\epsilon _ { p }$ such that

$$
\epsilon _ { p + 1 } = \epsilon _ { p } \biggl [ 1 + \frac { \rho } { n } ( 2 M + 1 ) + \frac { \rho ^ { 2 } M ^ { 3 } } { n ^ { 2 } } \biggr ] \qquad ( \rho \leq n - 1 ) ,
$$

or

$$
\epsilon _ { p + 1 } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } = \bigg [ 1 + \frac { \rho } { n } ( 2 M + 1 ) \bigg ] \bigg [ \epsilon _ { p } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } \overline { { { 1 } } } \bigg ] ;
$$

then,

$$
\begin{array} { r } { \begin{array} { c } { \bar { \mathbf { \Lambda } } _ { p + 1 } = \displaystyle { \bigg [ 1 + \frac { \rho } { n } ( 2 M + 1 ) \bigg ] ^ { p } \bigg [ \epsilon _ { 1 } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } \bigg ] - \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } } } \\ { \displaystyle { < e ^ { \rho ( 2 M + 1 ) } \bigg [ \epsilon _ { 1 } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } \bigg ] - \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } \quad ( \hat { \boldsymbol { \Lambda } } < \hat { \boldsymbol { \Lambda } } ) \bigg ] ^ { 3 } } } \end{array} } \end{array}
$$

Put $\epsilon _ { 1 } = \rho ^ { 2 } M / n ^ { 2 }$ . We see that, if

$$
\varrho ^ { \rho ( 2 M + 1 ) } \bigg [ \frac { \rho ^ { 2 } M } { n ^ { 2 } } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } \bigg ] - \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } < 1 ,
$$

then all quantities $\epsilon$ are less than unity.

Now we compare the sequences δ and $\epsilon$ Since

$$
\delta _ { 1 } ^ { ( n ) } = 1 + \frac { x } { n } - \frac { 1 } { 1 - x / n } = - \frac { x ^ { 2 } } { n ^ { 2 } } \frac { 1 } { 1 - x / n } ,
$$

it follows that

$$
\big | \delta _ { 1 } ^ { ( n ) } \big | < M \rho ^ { 2 } big / n ^ { 2 } ,
$$

or

$$
\big | \delta _ { 1 } ^ { ( n ) } \big | < \epsilon _ { 1 } < 1 .
$$

Similarly,

$$
\big | \delta _ { 2 } ^ { ( n ) } \big | \ < \ \epsilon _ { 2 } , \qquad \big | \delta _ { p + 1 } ^ { ( n ) } \big | \ < \ \epsilon _ { p + 1 } .
$$

Hence,

$$
\begin{array} { r l r } {  {  \begin{array} { c c } { \displaystyle { \boldsymbol { \tau } _ { n } ^ { ( n ) } - \frac { 1 } { 1 - x } | < R _ { n } } } \\ & { } \\ & { \displaystyle \equiv \exp { \{ \rho ( 2 M + 1 ) \} } \cdot [ \frac { \rho ^ { 2 } M } { n ^ { 2 } } + \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } ] - \frac { \rho M ^ { 3 } } { n ( 2 M + 1 ) } } \end{array} } } \end{array}
$$

where $R _ { n } \to 0$ as $n  \infty$ .Thus

$$
\operatorname * { l i m } _ { n \to \infty } U _ { n } ^ { ( n ) } = \frac { 1 } { 1 - x } ,
$$

subject to the above limitation on $_ { x }$

Lindelof (1903) applied Cauchy's residue theorem. Suppose that

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }
$$

is given with a finite nonzero radius of convergence,and define the domain $s$ in which $f ( { \pmb x } )$ is holomorphic inside the product domain $\boldsymbol { x } \times \boldsymbol { \bar { s } }$ where $\bar { s }$ denotes the domain obtained from the outer part of Sbyinversion with the origin as center.Let

$$
\sum _ { n = 0 } ^ { \infty } \phi ( n , x ) x ^ { n }
$$

be an entire function or integral function of $_ x$ that tends to $1 / ( 1 - x )$ inside the circle $| x | = 1$ as $\alpha \to 0$ This occurs if $\phi ( z , \alpha )$ is holomorphic and $\left| \phi ( z , \alpha ) \right| < e ^ { \kappa ( \alpha ) \rho }$ for $- \psi _ { 0 } ^ { \prime } \leq \psi \leq \psi _ { 0 }$ such that $z \equiv \rho e ^ { \sqrt { - 1 } \psi }$ ， $\rho < 1$ ， $0 < \psi _ { 0 } , \psi _ { 0 } ^ { \prime } < \pi ,$ where $K ( \alpha )$ tends to zero as $\alpha \to 0$ if $\phi ( z , \alpha )$ tends uniformly to unity as $\alpha \to 0$ ,and if

$$
\operatorname* { l i m } _ { n  \infty } | \phi ( n , \alpha ) | ^ { 1 / n } = 0 .
$$

Lindelof obtained, by Cauchy's residue theorem, the formula

$$
\sum _ { n = 0 } ^ { \infty } \phi ( n , \alpha ) x ^ { n } = \int _ { L } { \frac { e ^ { - \pi { \sqrt { - 1 } } z } } { 2 { \sqrt { - 1 } } \sin \pi z } } \phi ( z , \alpha ) x ^ { z } d z ,
$$

where the lengths of the radius vectors drawn in the directions $\psi , \psi ^ { \prime }$ from the origin are denoted by ${ \mathit { l } } , { \mathit { l } } ^ { \prime }$ ；; the intersections of these two vectors of length ${ \mathit { l } } , \ { \mathit { l } } ^ { \prime }$ with the circle $c$ of radius $| c | < 1$ and the circle $c$ of radius $c + { \frac { 1 } { 2 } }$ are denoted respectively by $A , a ,$ and $A ^ { \prime } , a ^ { \prime }$ ; and the contour $L$ consists of the arc $\acute { a } a ^ { \prime }$ on $c$ the arc $A A ^ { \prime }$ on $C _ { i }$ ,and the parts of the radi ${ \mathit { l } } , { \mathit { l } } ^ { \prime }$ between the two concentric circles.Subtracting this formula from

$$
\frac { 1 } { 1 - x } = \int _ { L } \frac { e ^ { - \pi ^ { \sqrt { - 1 } z } } } { 2 \sqrt { - 1 } \sin \pi z } x ^ { z } d z ,
$$

obtained by putting $\phi ( n , \alpha ) \equiv 1$ in the formula, he derived the limit of

$$
\sum _ { n = 0 } ^ { \infty } \phi ( n , \alpha ) x ^ { n } - { \frac { 1 } { 1 - x } }
$$

for $\propto = 0$ .Thus Lindelof proved that the entire function

$$
\sum _ { n = 0 } ^ { \infty } a _ { n } \phi ( n , \alpha ) x ^ { n }
$$

tends uniformly to the given function $f ( { \pmb x } )$ inside a finite area of $s$ as $\pmb { \alpha }$ tends to zero.

Brumberg (l963)applied this theory to the three-body problem.He considered

$$
\frac { d g } { d \omega } = g ^ { 2 } , ~ g ( 0 ) = 1 ,
$$

with

$$
\frac { d ^ { j } g } { d \omega ^ { j } } = j ! g ^ { j + 1 } ( j = 1 , 2 , . . . , \nu ) .
$$

# Define

$$
G _ { 0 } ( \omega ) = 1 , \qquad G _ { n + 1 } ( \omega ) = \sum _ { k = 0 } ^ { \nu } \omega ^ { k } [ G _ { n } ( \omega ) ] ^ { k + 1 } ,
$$

$$
G _ { n } ( \omega ) = \sum _ { k = 0 } ^ { m _ { n } } b _ { k } ^ { ( n ) } \omega ^ { k } , \qquad m _ { n } = ( \nu + 1 ) ^ { n } - 1 ;
$$

then we obtain the sequence

$$
\begin{array} { r l r } & { } & { g _ { n } ( \omega ) = c _ { 0 } ^ { ( n ) } + c _ { 1 } ^ { ( n ) } \omega + \cdot \cdot \cdot + c _ { m _ { n } } ^ { ( n ) } \omega ^ { m _ { n } } , } \\ & { } & \\ & { } & { c _ { k } ^ { ( n ) } = \cfrac { 1 } { n ^ { k } } b _ { k } ^ { ( n ) } , \qquad g _ { n } ( \omega ) = G _ { n } \Big ( \cfrac { \omega } { n } \Big ) , } \end{array}
$$

which tends uniformly to the solution of (199） as $n \to \infty$ .Brumberg obtained the recurrence formulas

$$
b _ { m } ^ { ( n + 1 ) } = \sum _ { k = k _ { 1 } } ^ { k _ { 2 } } d _ { m - 1 } ^ { ( k + 1 ) } b _ { k } ^ { ( n ) } \qquad ( m = 1 , 2 , . . . , m _ { n + 1 } ) ,
$$

$$
k _ { 1 } = \operatorname* { m a x } \Big \{ 0 , m - \Big [ \frac { \nu ( m + 1 ) } { \nu + 1 } \Big ] \Big \} , \qquad k _ { 2 } = \operatorname* { m i n } \big ( m , m _ { n } \big ) ,
$$

and

$$
d _ { k } ^ { ( m + 1 ) } = \sum _ { l = \operatorname* { m a x } \{ 0 , k - \nu \} } ^ { \operatorname* { m i n } \{ k , \nu m \} } d _ { l } ^ { ( m ) } \qquad ( k = 1 , 2 , . . . , \nu m + \nu ) .
$$

Thus

$$
d _ { k } ^ { ( m ) } = \sum _ { \lambda = 0 } ^ { [ k / ( \nu + 1 ) ] } ( - 1 ) ^ { \lambda } C _ { m } ^ { \lambda } C _ { k + m - 1 - \lambda ( \nu + 1 ) } ^ { m - 1 } \qquad ( k = 0 , 1 , . . . , m ) ,
$$

Consider a Taylor series

$$
\begin{array} { c } { { f ( \omega ) = a _ { 0 } + a _ { 1 } \omega + a _ { 2 } \omega ^ { 2 } + \cdot \cdot \cdot , } } \\ { { f _ { n } ( \omega ) = c _ { 0 } ^ { ( n ) } a _ { 0 } + c _ { 1 } ^ { ( n ) } a _ { 1 } \omega + \cdot \cdot \cdot + c _ { m _ { n } } ^ { ( n ) } a _ { m _ { n } } \omega ^ { m _ { n } } } } \end{array}
$$

with the coefficients just obtained. Then we find

$$
f ( x ) - f _ { n } ( x ) = { \frac { 1 } { 2 \pi { \sqrt { - 1 } } } } \int _ { \Gamma } \left[ { \frac { 1 } { 1 - { \frac { x } { \omega } } } } - g _ { n } { \bigg ( } { \frac { x } { \omega } } { \bigg ) } \right] { \frac { f ( \omega ) } { \omega } } d \omega ,
$$

and hence the estimate

$$
| f ( x ) - f _ { n } ( x ) | \leq \frac { \epsilon L } { 2 \pi } \operatorname* { m a x } _ { \Gamma } \bigg | \frac { f ( \omega ) } { \omega } \bigg | ,
$$

where $L$ is the length of the integration contour $\Gamma$ ; the expression in the bracket of the integrand is supposed to be smaller than $\epsilon$ in absolute value for $n > N ( \epsilon )$

For the two-body problem Brumberg (Section 5.14) put

$$
\begin{array} { c } { { M = 2 k \pi \pm \sqrt { - 1 } \Omega ( k = 0 , \pm 1 , \pm 2 , . . . ) , } } \\ { { { } } } \\ { { \Omega = - \sqrt { 1 - e ^ { 2 } } + \log \displaystyle \frac { 1 + \sqrt { 1 - e ^ { 2 } } } { e } , } } \end{array}
$$

$$
= \cos E - e = \sum _ { k = 0 } ^ { \infty } a _ { k } M ^ { 2 k } , \qquad Y = \sqrt { 1 - e ^ { 2 } } \sin E = \sum _ { k = 0 } ^ { \infty } b _ { k } M ^ { 2 k + 1 }
$$

and obtained

$$
X ^ { ( n ) } = \sum _ { k = 0 } ^ { [ m _ { n } / 2 ] } c _ { 2 k } ^ { ( n ) } \alpha _ { k } M ^ { 2 k } , \qquad Y ^ { ( n ) } = \sum _ { k = 0 } ^ { [ m _ { n - 1 } / 2 ] } c _ { 2 k + 1 } ^ { ( n ) } b _ { k } M ^ { 2 k + 1 } ,
$$

$$
a _ { k } = \frac { ( - 1 ) ^ { k } \bar { a } _ { k } } { ( 2 k ) ! ( 1 - e ) ^ { 3 k - 1 } } , \qquad b _ { k } = \frac { ( - 1 ) ^ { k } \sqrt { 1 - e ^ { 2 } } \bar { b } _ { k } } { ( 2 k + 1 ) ! ( 1 - e ) ^ { 3 k + 1 } } ,
$$

$$
{ \bar { a } } _ { k } = \sum _ { l = 0 } ^ { k - 1 } a _ { l } ^ { ( k ) } e ^ { l } , { \bar { b } } _ { k } = \sum _ { l = 0 } ^ { k - 1 } b _ { l } ^ { ( k ) } e ^ { l } ,
$$

$$
a _ { j } ^ { ( k + 1 ) } = \sum _ { \lambda = 0 } ^ { j } ( - 1 ) ^ { j - \lambda } ( \lambda + 1 ) 2 ^ { - \lambda } C _ { 3 k + 2 } ^ { j - \lambda } d _ { \lambda , k } ,
$$

$$
b _ { j } ^ { ( k ) } = \sum _ { \lambda = 0 } ^ { j } { \bigl ( } - 1 { \bigr ) } ^ { j - \lambda } 2 ^ { - \lambda } C _ { 3 k + 1 } ^ { j - \lambda } d _ { \lambda , k } ,
$$

$$
d _ { \lambda , k } = \sum _ { s = 0 } ^ { [ \lambda / 2 ] } { \frac { ( - 1 ) ^ { s } ( \lambda + 1 - 2 s ) ^ { \lambda + 2 k + 1 } } { s ! ( \lambda + 1 - s ) ! } } \cdotp
$$

For Sundman's variable defined by (l98),Brumberg computed the coefficients $A _ { s }$ for

$$
f ( \theta ) = a _ { 0 } + \sum _ { s = 1 } ^ { \infty } A _ { s } \theta ^ { s } , \qquad | \theta | < 1 ,
$$

in the form

$$
A _ { s } = \sum _ { k = 0 } ^ { [ ( s - 1 ) / 2 ] } a _ { s - 2 k } \dot { p } _ { s - 2 k } ^ { ( s ) } \bigg ( { \frac { 4 \Omega } { \pi } } \bigg ) ^ { s - 2 k } ,
$$

where

$$
\left( \theta + { \frac { \theta ^ { 3 } } { 3 } } + { \frac { \theta ^ { 5 } } { 5 } } + \cdot \cdot \cdot \right) ^ { q } = \sum _ { s = 0 } ^ { \infty } \beta _ { q } ^ { \left( q + 2 s \right) } \theta ^ { q + 2 s } ,
$$

$$
\begin{array} { r } { s { p } _ { s - 2 k } ^ { \scriptscriptstyle ( s ) } = ( s - 2 k ) p _ { s - 1 - 2 k } ^ { \scriptscriptstyle ( s - 1 ) } + ( s - 2 ) p _ { s - 2 k } ^ { \scriptscriptstyle ( s - 2 ) } } \end{array}
$$

$$
\Big ( s = 3 , 4 , . . . ; k = 0 , 1 , . . . , \Big [ \frac { s - 1 } { 2 } \Big ] \Big ) .
$$

For the three-body problem the regularizing variable $\pmb { \omega }$ (Sections 17.16 and 22.8), defined by

$$
d \omega = U d t , \qquad U = k ^ { 2 } \biggl ( \frac { m _ { 2 } m _ { 3 } } { r _ { 2 3 } } + \frac { m _ { 3 } m _ { 1 } } { r _ { 3 1 } } + \frac { m _ { 1 } m _ { 2 } } { r _ { 1 2 } } \biggr ) ,
$$

is used as the independent variable and all quantities are expanded in powers of $\pmb { \omega }$ with the above artifice of using the series $P _ { n } ( e )$ with coefficients $c _ { n } ^ { ( { \mathfrak { p } } ) }$ in the place of $f ( z )$

Cesco (l965)，on the other hand,by referring to Borel’s integral method of summability of divergent series (Borel, 19Ol),considered the series $\textstyle \sum _ { n } u _ { n }$ together with the series

$$
H ( x ) = \sum _ { n } u _ { n } h _ { n } ( x ) ,
$$

$$
h _ { n } ( x ) = \frac { 1 } { n ! } { \int _ { 0 } ^ { x } e ^ { - \theta } \theta ^ { n } d \theta } = h _ { n - 1 } ( x ) { } + \frac { x } { n } [ h _ { n - 2 } ( x ) - h _ { n - 1 } ( x ) ] ,
$$

which satisfies $\begin{array} { r } { \operatorname* { l i m } _ { x \to \infty } H ( x ) = u } \end{array}$ whenever $\textstyle \sum _ { n } u _ { n } = u$ converges. If $\textstyle \sum _ { n } u _ { n }$ is divergent, but if $H ( x )  u$ as $x \to \infty$ ，where $\boldsymbol { u }$ is finite, then we can take $\boldsymbol { u }$ as the sum of $\sum _ { n } u _ { n }$ and the values of $H ( x )$ for increasing values of $\pmb { x }$ as approximate values of the sum

$$
H ( x _ { \nu } ) = \sum _ { n = 0 } ^ { \infty } u _ { n } h _ { n } ( x _ { \nu } ) \sim \sum _ { n } u _ { n } , 0 < x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot ,
$$

where $h _ { n } ( x )$ are tabulated. The equations of motion of the three-body problem, in which $m _ { 0 } = 0 . 8$ ， $m _ { 1 } = m _ { 2 } = 0 . 1$ ,namely,

$$
{ \frac { d } { d \tau } } \left( { \frac { d x } { d t } } \right) = - { \frac { x y } { \rho ^ { 3 } } } , \qquad \rho ^ { 2 } = x ^ { 2 } + { \frac { y ^ { 2 } } { 4 } } ,
$$

$$
\frac { d ^ { 2 } y } { d \tau ^ { 2 } } = - 0 . 2 + \frac { ( d y / d t ) ^ { 2 } } { y } - 0 . 8 \Big ( \frac { y } { \rho } \Big ) ^ { 3 } , ~ y ~ d \tau = d t ,
$$

are transformed by

$$
X _ { 0 } = t , \qquad X _ { 1 } = { \frac { d x } { d t } } , \qquad X _ { 2 } = \biggl [ \biggl ( { \frac { d y } { d \tau } } \biggr ) ^ { 2 } \biggl / y - 0 . 4 \biggr ] \biggl / y ,
$$

$$
X _ { 3 } = y X _ { 6 } , \qquad X _ { 4 } = { \frac { d y } { d \omega } } X _ { 6 } , \qquad X _ { 5 } = x X _ { 6 } ,
$$

$$
X _ { 6 } = \frac { 1 } { \rho } = 0 . 5 X _ { 1 } ^ { 2 } + 0 . 1 5 6 2 5 X _ { 2 } - H , H = 4 0 . 3 4 4 7 \cdot \cdot \cdot ,
$$

to

$$
\begin{array} { l l l } { { \displaystyle { \frac { d X _ { 1 } } { d \tau } = - X _ { 3 } X _ { 5 } X _ { 6 } , \frac { d X _ { 2 } } { d \tau } = - 1 . 6 X _ { 3 } X _ { 4 } X _ { 6 } , \frac { d X _ { 3 } } { d \tau } = X _ { 4 } - X _ { 5 } } } } \\ { { \displaystyle { \frac { d X _ { 4 } } { d \tau } = X _ { 2 } X _ { 3 } - X _ { 4 } X _ { 8 } + 0 . 2 ( 1 - 4 X _ { 3 } ^ { 3 } ) X _ { 6 } , \frac { d X _ { 5 } } { d \tau } = X _ { 1 } X _ { 3 } - X _ { 4 } X _ { 6 } } } } \end{array}
$$

$$
X _ { 8 } = X _ { 3 } X _ { 7 } , ~ X _ { 7 } = X _ { 1 } X _ { 5 } + 0 . 2 5 X _ { 4 } .
$$

The equations are integrated numerically on computers with the initial conditions

$$
\begin{array} { r } { \dot { \mathrm { \iota _ { 0 } } } ( 0 ) = 0 , \qquad X _ { 1 } ( 0 ) = 1 , \qquad X _ { 2 } ( 0 ) = 2 5 5 . 8 , \qquad X _ { 3 } ( 0 ) = 2 / \sqrt { 6 5 } , } \\ { X _ { 4 } ( 0 ) = - 3 2 / \sqrt { 6 5 } , \qquad X _ { 5 } ( 0 ) = 8 / \sqrt { 6 5 } , \qquad X _ { 6 } ( 0 ) = 1 / \sqrt { 6 5 } , \qquad } \end{array}
$$

in the form

$$
X _ { i } ( \tau ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ^ { ( i ) } \tau ^ { n } \qquad ( i = 0 , 1 , . . . , 8 ) .
$$

Lopér Garcia (1966) extended the tables of Zumkley (l94l） for the three-body problem to higher-order approximations.

Zelmer (1967) improved Brumberg's procedure and applied it to the three-body problem with given initial values of the three mutual distances.

The Euler-Knopp sequence

$$
g _ { n } ( z ) = \sum _ { k } g _ { k } ^ { ( n ) } z ^ { k } = \frac { 1 - z [ ( 1 - r ) + r z ] ^ { n } } { 1 - z }
$$

is convergent to $1 / ( 1 - z )$ at all points inside the circular domain

$$
D = \left\{ z { \bigg / } \left. z - \left( 1 - { \frac { 1 } { r } } \right) \right. < { \frac { 1 } { \vert r \vert } } \right\} .
$$

If $G = \left( g _ { k } ^ { ( n ) } \right)$ is the given matrix, then the sequence

$$
g _ { n } ( z ) = \sum _ { k } g _ { k } ^ { ( n ) } z ^ { k } \qquad ( n = 0 , 1 , . . . )
$$

tends to $1 / ( 1 - z )$ as $\pmb { n }  \infty$ for each $z \in D$

Consider the sequence

$$
g _ { n } ( z ) = \sum _ { k } g _ { k } ^ { ( n ) } z ^ { k } = \frac { 1 - z f _ { n } ( z ) } { 1 - z } \cdot
$$

The sequence $g _ { n } ( z )$ tends to $1 / ( 1 - z )$ on $\pmb { D }$ if and only if $\Pr ( z )$ tends to zero as $n  \infty$ on $_ D$ . In order that the sequence $g _ { n } ( z )$ shall be convergent in some circular domain $| z | < R , R > 1 ,$ $R \supset D$ - that is,this function shall not possess a pole at $z = 1$ - we must have $f _ { n } ( 1 ) = 1$ for all $\pmb { n }$ The simplest way to obtain a sequence of functions $\{ f _ { \mathfrak { n } } ( z ) \}$ that satisfy this condition is to start from $\begin{array} { r } { f ( z ) = \sum _ { k } f _ { k } z ^ { k } } \end{array}$ (called the displacement function),such that $f ( 1 ) = 1$ ，where $f ( z )$ is analytic for $| z | < R , R > 1$ The sequence $\begin{array} { r } { f _ { n } ( z ) = \sum _ { k } f _ { k } ^ { ( n ) } z ^ { k } , } \end{array}$ where $f _ { 0 } ^ { ( 0 ) } = 1 , f _ { k } ^ { ( 0 ) } = 0$ for $k > 0$ and $f _ { k } ^ { \left( 1 \right) } = f _ { k } ,$ tends to zero on $D \colon D = \{ Z / | f ( z ) | < 1$ ， $| z | < R \}$ . The matrix $\boldsymbol { F } = \left( f _ { \boldsymbol { k } } ^ { ( n ) } \right)$ is called the Sonnenschein matrix. $f ( z ) = ( 1 - r ) + r z$ is one of the displacement functions.

It is remarked that the method with $f ( z ) = ( 1 - r ) + r z$ as the displacement function can be used for the interval $( - 2 \Omega , + 2 \Omega )$ ,and the method with $f ( z ) = ( 1 - r ) + r z ^ { 2 }$ for the interval

$$
( - 2 { \sqrt { 2 } } \Omega , + 2 { \sqrt { 2 } } \Omega ) ;
$$

but the transformation (198) can be used only for $( - \Omega , + \Omega )$ of the strip parallel to the real axis (see Sections 22.1i, 22.34).

Recently Saari (l969) presented a procedure for extending the convergence radius of a power series solution of a system of differential equations by a change of the independent variable in the form of a conformal mapping.

# REFERENCES

1922 J. Brit. Astron. Assoc., 32, 231.   
Andoyer, H. 1886 Contribution á la Theorie des Orbites Intermediaires,Thesis,Paris. 1887 Ann.Fac. Sci.Toulouse,1, E1. 1899 Ibid., 3, B1. 1901 Bull.Astron., 18, 177. 1902 Ibid., 19, 401. 1907 Ibid.,24, 395. 1926 Sur la Theorie Analytique du Mouvement de la Lune, Mem. présentée d l'Acad. Sci.,Institut de France, ser.2,58. 1926a La Théorie de la Lune,Collection Scientia, No. 17, Gauthier-Villars, Paris. 1926b Cours de Mécanique Celeste, II, Gauthier-Villars, Paris. 1928 Sur la Theorie Analytique du Mouvement de la Lune, Mem. présenteée ä l'Acad. Sci.,Institut de France, ser.2,59. 1928a J. de Math. pures appl.,ser. 2,7,61.   
Andrade,J. 1890°J. Ecole Polytech., Paris, cah.60, 1.   
Arenstorf, R. F., and Davidson, M. C. 1963 AIAAJ,1, 228.   
Backlund, O. 1882 Astron.Nachr.,101, 19. 1886 Mém. Acad. Sci. Saint. Petersbourg, ser.7, 34, no.8. 1886a Bull. Acad.Sci. Saint Petersbourg,30, 449. 1887 Bull.Astron.,4, 321. 1889 Astron. Nachr.,122, 273. 1892a Mem. Acad. Sci. Saint-Petersbourg,ser.7, 38, no. 8. 1892Ibid., ser.7,38, no. 11. 1897a Bull. Acad. Sci. Saint-Petersbourg,ser.5, 6,311. 1897b Astron. Nachr., 145,241. 1897c Bull. Astron., 14,321. 1898a Mém. Acad. Sci. Saint-Pétersbourg, ser.8,6, no. 10,1. 1898b Bull. Astron.,15,5. 1902 Bull. Astron., 19, 433. 1904 Bull.Astron., 21,289. 1912 Bull.Acad. Sci. Saint-Pétersbourg,16, no.3.   
Bailie, A.E.,and Bryant, R.W. 1960 Astron. J.,65,451.   
Bailie,A.E., and Fisher, D. 1963 NASA Technical Note, D-1468, National Aeronautics and Space Administration,Washington,D.C.   
Baillaud, B. 1876 Exposition de la Methode de M. Gylden pour le Développement des Perturbations des Cometes,Thesis, Paris.   
Baker,R.M.L., Westrom, G.B., Hilton, C.G., Gersten, R.H., Arsenault, J. L.,and Browne, E. J. 1960ARSJ,30,740. 1925 Cir. l'Obs. Cracovie, nos.16, 17,20. 1927 Ibid.,nos. 24,25. 1928 Monthly Notices Roy.Astron.Soc.,89,215.   
Barteneva, O. N. 1955Byull. Inst. Teor. Astron. (Akad.Nauk SSSR),6, 249.   
Barton, D. 1967 Computer J., 9, 340.   
Bauschinger, J. 1928 Die Bahnbestimmung der Himmelskorper, 2nd edition, Engel1 Leipzig.   
Behrens, J. G. 1929 Astron.Nachr.,234,49. 1935 Ibid.,255,245.   
Bernstein, S. N. 1026Lecons sur les Proprietes Extrémales et la Meilleure Approximati Fonctions Analytiques d'une Variable Relle, Gauthier-Villars,   
Biermann, L. 1951 Z. Astrophysik, 29, 274.   
Bilimovich, A. 1943 Astron. Nachr., 273, 161.   
Bilo, E.H.,and van de Hulst, H. C. 1960 Bull.Astron.Inst.Netherlands,15,119.   
Bilo, E. H., and van Houten-Groeneveld, I. 1960Bull.Astron.Inst.Netherlands,15,155.   
Block, H. G. 1907Astron. Iaktt.Unders. Stockholm Obs., 8, no.5.   
Boas,R.P.,and Buck, R.C. 1958 Polynomial Expansions of Analytic Functions, Springer, Berlin.   
Bobrovnikoff, N.T. 1929 Lick Obs. Bull,14, no. 408,28.   
Boda, K. 1928 Astron. Nachr., 233, 265. 1930 Ibid., 238, 1. 1930a Ibid., 243,17. 1933 Ibid., 249, 37.   
Boeva, N. T. 1933 Byull. Inst. Teor. Astron. (Akad. Nauk SSSR), no. 32, 152. 1936 Astron. Zh., 12, 476.   
Bohlin, K. 1896 Nova Acta Regiae Sci. Upsaliensis, ser.3,16. 1903 Astron. Iaktt.Unders. Stockholm Obs.,7, no.1. 1907 Ibid., 8, no. 7. 1908 Ibid., 9, no. 1. 1908a Ibid., 9, nos. 2,3. 1915 J. Math. pures appl., ser.7, 1, 367. 1916 Ibid., ser.7, 2, 173. 1921 Arkiv Mat. Astron.Fysik,16, no.4. 1922 Ibid., 16, no. 14. 19LJ ATKU Ivial.AslTon.rysin,Io,nO.ə5. 1931 Astron.Iaktt.Unders. Stockholm Obs., 11, no.7. 1933 Arkiu Mat. Astron.Fysik,24, no.11. 1933a Annali Mat. pura appl., ser.4,11, 241. 1933b Ibid.,12,135. 1934 Astron.Iakt.Unders.Stockholm Obs.,11,no.11. 1935 Arkiu Mat. Astron.Fysik,25, no.6.   
Bok, B. J. 1934 Haruard College Obs. Cir., no. 384.   
Borel, E. 1901 Lecons sur les Séries Divergentes, Gauthier-Villars, Paris. 1928 Lecons sur les Fonctions de Variables Reelles et les Approximations en Séries de Polynomes, Gauthier-Villars,Paris.   
Born, G. H. 1970 Celestial Mech., 2,103.   
Bosler, J. 1931 J. des Observateurs, 14, 177.   
Bower, E. 1932Lick Obs. Bull,10, no. 45,1.   
Brady, J. L. 1965 Astron. J., 70,279.   
Brady, J.L., and Carpenter, E. 1967Astron.J.,72,365. 1970 Ibid.,75,1052.   
Brandt, J. C. 1961Astrophys.J.,133,1091.   
Breakwell,J.V., and Perko,L.M. 1966"Methods in Astrodynamics and Celestial Mechanics， 159, R. L. Duncombe and V.G.Szebehely，eds.,Academic Press,New York.   
Brendel, M. 1887 Astron. Nachr., 116,161. 1889 Astron. Iaktt.Unders.Stockholm Obs.,4, no.3. 1890 Uber die Anwendung der Gylden'schen absoluten Storungstheorie auf die Breitenstorungen einer gewissen Klasse kleiner Planeten, nebst numerischem Beispiel fur den Planeten (46) Hestia,Dissertation, Gotingen. 1895 Astron.Nachr.,139,35. 1897 Ibid., 140, 145. 1898 Theorie der kleinen Planeten I, Abhandl.K. Gesell.Wiss.Gottingen, Math-Phys.Kl.,neue Folge,1,no.1. 1901 Math.Annalen, 55,248. 1905 Theorie der kleinen Planeten II, Abhandl. K.Gesell.Wiss.Gottingen, Math-Phys. Kl., neue Folge,3,no.4. 1909 Theorie der kleinen Planeten,III,ibid.,6, no.4. 1910 Theorie der kleinen Planeten,IV,ibid., 6, no.5. 1911 Theorie der kleinen Planeten, V,ibid., 8, no.1. 1925a Mitt. Univ. Sternwarte Frankfurt a.M.,Part 2. 1927 Mitt.Univ. Sternwarte Frankfurt a.M., Part 4. 1929 Ibid., Part 6. 1930 Astron. Nachr., 238, 197. 1933 Ibid., 250, 177. 1935 J.reine angew. Math., 172, 219.   
Breuer, F. D., and Riddell, W. C. 1964Celestial Mechanics and Astrodynamics,307,V.Szebehely,ed.,Academic Press, New York.   
Briggs, R.E. 1962 Astron. J., 67,710.   
Broucke, R. 1969Celestial Mech.,1, 110.   
Brouwer, D. 1933 Trans. Yale Univ. Obs., 6, no. 7. 1938 Astron. J., 46, 149. 1944 Astron. J., 51, 37,54. 1955 Monthly Notices Roy. Astron. Soc., 115, 221. 1959 Astron. J., 64, 378.   
Brouwer, D.,and Clemence, G.M. 1946 Astron. J., 52, 64.   
Brown, E. W. 1923 Trans.Yale Univ.Obs., 3, no.1. 1925 Ibid., 3, no. 3. 1929 Monthly Notices Roy. Astron. Soc., 90,3. 1930 Trans. Yale Univ. Obs., 6, no. 4.   
Brown,E.W.,and Brouwer, D. 1937 Trans. Yale Univ. Obs., 6, no.8.   
Brown, E. W., and Shook, C. A. 1933Planetary Theory,Cambridge University Press.   
Brumberg, V. 1961 Astron. Zh., 38, 738. 1963 Byull. Inst.Teor.Astron. (Akad. Nauk SSSR),9, 234.   
Brunnow, F. 1865Astron.Nachr.,62, 259.   
Buchholz, H. 1902 Denkschrift Math.-Naturw.Cl.,K.Akad. Wiss.Wien, 72, 309. 1903 Nova Acta,Abhandl.K.Leop.-Carol.Denkschrift Akad.Naturforscher, Halle, 81, no. 3. 1905 Denkschrift Math.-Naturw.Cl., K. Akad. Wiss. Wien, 77, 129.   
Burnside, W. S., and Panton, A.W. 1928The Theory of Equations,I1,7th ed.,Longmans,London.   
Callandreau, O. 1882 Ann. Obs.Paris, Mém., 16,A1. 1882a Compt.Rend.,93,779. 1890 Bull. Astron., 7, 471. 1892 Ann. Obs. Paris, Mém., 20, B1. 1894 Compt. Rend.,118, 751. 1912 Ann. Obs. Toulouse,6, 391. 1913Bull. Astron., 30, 315.   
Cesco, R. P. 1965Observ.Astron. Univ. Nac. La Plata, serie Astronomia, 31, n   
Chamberlain, J. W. 1960 Astrophys.J., 131,47. 1961 Ibid.,133,675.   
Chapront, J., and Mangeney, L. 1968 Astron. J.,73,214. 1969 Astron. and Astrophys., 2, 425.   
Charlier, C. V. L. 1887 Kongl. Suenska Vetenskaps-Akad.Handl., 22. 1892 Bihang Suenska Vetenskaps-Akad. Handl.,18, no. 6. 1893 Ibid.,19, no. 2. 1904 Medd. Lund Astr. Obs., no. 21.   
Charnow, M. L. 1966 NASA Technical Note, D-3378.National Aeronautics an Administration, Washington,D.C.   
Charnow, M., Musen, P.,and Maury,J.L. 1968 J.Astronaut.Sci.,15,303.   
Charnyi, V. I. 1963 Iskusstuvennye Sputniki Zemli,16, 226.   
Chazy, J. 1922 Ann. Ecole Norm. Sup., ser. 3, 39,29. 1924 Compt.Rend.,179, 1307. 1933 Ibid.,197, 1193. 1938 Bull. Astron., ser.2, 11,361.   
Chebotarev, G. A. 1963 Astron. Zh., 40, 812. 1964 Ibid., 41, 983. 1966 Ibid.,43, 435. 1968 Byull. Inst. Teor. Astron.(Akad. Nauk SSSR),11, 341.   
Chebotarev, G. A., and Bozhkova, A. I. 1960 Byull. Inst. Teor.Astron.(Akad. Nauk SSSR),7,581. 1962 Ibid., 8, 641. 1963 Ibid., 9, 169.   
Chebotarev, G. A., and Volkov, M. S. 1962 Byull. Inst. Teor. Astron. (Akad.Nauk SSSR),8, 99.   
Clemence, G. M. 1943 Astron. Papers Am. Eph. Naut. Alm.,11, no. 1,1. 1947 Astron. J., 52, 122. 1949 Astron.Papers Am. Eph. Naut.Alm.,11, no.2,229. 1953 Ibid., 13, 321. 1954 Ibid.,13, 365. 1960 Astron. J., 65, 21. 1961 Astron.Papers Am.Eph. Naut. Alm., 16,no. 2, 261.   
Cohen, C. J.,and Hubbard, E. C. 1962 Astron. J., 67,10. Differential Equations， J. P. LaSalle and S. Lefschetz, eds., Academic Press, New York.   
Collatz, L. 1951Numerische Behandlung von Differentialgleichungen, Springer, Berlin.   
Commendantov, N. V. 1931 Byull. Inst. Teor. Astron.(Akad. Nauk SSSR), no. 27. 1935 On the Determination of the General Perturbations of the Minor Planets of the Minerva Group,United Sci.Techn. Pub.,House of People's Commissariat of Heavy Industry of the USSR, Moscow. 1935a Byull. Inst. Teor. Astron. (Akad.Nauk SSSR), no. 35. 1935b Astron.Zh.,12,152. 1936 Astron.Nachr.,259, 17. 1936a Astron. Zh., 13,190.   
Cowell, P. N., and Crommelin, A. C. D. 1907 Monthly Notices Roy. Astron. Soc.,67,174, 386, 511. 1908 1bid.,68,111, 173,375,510,665. 1908a Ibid.,68,379,458. 1908b Ibid.,68,576. 1910Essay on the Return of Halley's Comet,Preisschrift,Pub．Astron. Gesell, 23,Engelmann,Leipzig.   
Cowell, P.H., Crommelin,A. C. D.,and Davidson, C. 1909Monthly Notices Roy. Astron. Soc., 69,421.   
Crommelin, A. C. D. 1908 Monthly Notices Roy.Astron. Soc.,68,457. 1910Ibid.,71,50.   
Curtis, J. D. 1970A Modification of the Brown-Shook Method based on Lie series, Dissertation, University of Maryland.   
Dallas, S. S. 1964 Celestial Mechanics_ and Astrodynamics， 391， V. Szebehely，ed., Academic Press,New York.   
Damoiseaux, M. C. T. 1827Mémoire sur la Théorie de la Lune,Mém.présentee á l'Acad. Sci., Institut de France,ser. 3,1, 313.   
Danby, J. M. A. 1962 Astron. J., 67, 287. 1965Ibid.,70,155.   
Darwin, G. H. 1897Acta Math.,21, 99.Reprinted in Darwin's Scientific Papers, IV, 1,Cambridge University Press,1911.   
Davis, M. S. 1951 Astron.J.,56,188. 1958 Ibid., 63, 418.   
Deprit, A. 1967 Boeing Sci.Res.Lab.Document D1-82-0663. 1968 Ibid.,D1-82-0755. 1969 Celestial Mech.,1, 12.

1970 Boeing Sci. Res. Lab. Document D1-82-0975.

Déprit, A., Henrard,J.,and Rom,A. 1970"Boeing Sci. Res.Lab.Document D1-82-0963, and Document D1-82-0990. 1970a Astron.J.,75,747; 76,269,273.   
Déprit, A.,and Rom,A. 1969Boeing Sci. Res. Lab. Dcument D1-82-088. Reprinted in Celestial Mech.,2, 1970,166.   
Donner, A. 1882 Eine Methode der Anvwendung der Gylden'schen Storungstheorie zur Berechnung der absoluten Storungen der kleinen Planeten,Dissertation, Dorpat, Frenckell,Helsingsfors.   
Dubiago, A. D. 1961The Determination of Orbits, transl. by R. D. Burke, G. Gordon, L.N.Rowell, and F.T. Smith, RAND,Macmillan, New York.   
Dukhnovski, P. G. 1958 Astron. Zh., 34,75.   
Duncombe, R. L., and Davis, M. S. 1950 Astron.J.,55,133. 1951Ibid.,56,199.   
Dziobek, O. 1888Die Mathematische Theorie der Planetenbewegung，Barth, Leipzig; also 1892:Mathematical Theory of Planetary Motions, Register Pub. Co., Ann Arbor, Mich.   
Eckert, W. J. 1933 Trans. Yale Univ. Obs., 6, no. 6. 1935Astron.J.,44,177.   
Eckert, W. J., and Brouwer, D. 1937 Astron.J., 46,125.   
Eckert, W. J., Brouwer, D., and Clemence, G. M. 1951 Astron.Papers Am. Eph. Naut. Alm.,12, no.2,31.   
Eckstein, M. C., Shi, Y. Y., and Kevorkian,J. 1966Astron. J., 71, 248,301. 1966a The Theory of Orbits in the Solar System and in Stellar Systems, 291, G. Contopoulos, ed., Academic Press, New York. 1966b Methods in Astrodynamics and Celestial Mechanics，183，R.L. Duncombe and V.G. Szebehely，eds.,Academic Press,New York.   
Encke, J. F. 1854Berliner Astron. Jahrbuch fur 1857.   
Everhart, E. 1967 Astron. J., 72, 716,1002. 1968 Ibid.,73,1029. 1969 Ibid., 74, 735.   
Filippi, S. 1966 Mathematische Methoden der Himmelsmechanik und Astronautik,309, Math.Forschungsinstitut, Oberwolfach.   
Fisher, D. 1963Astron. J.,68, 718.   
Foursenko, M. A. 1965 Byull. Inst.Teor. Astron. (Akad.Nauk SSSR),10, 272.   
Galibina, I. V. 1958 Byull. Inst.Teor. Astron. (Akad.Nauk SSSR),6,630. 1963 Ibid., 9, 46. 1964 Ibid.,9, 465. 1970 Ibid.,12, 470.   
Garfinkel, B. 1944Astron. J., 51,44. 1959Ibid.,64,353.   
Garofalo, A. M. 1960Astron. J., 65, 117.   
Gormally, J. M. 1966Methods in Astrodynamics and Celestial Mechanics,199, R. L. Duncombe and V.G. Szebehely, eds., Academic Press, New York.   
Goursat, E. 1903 Bull Sci. Math., ser. 2, 27, 226.   
Gravelius, H. 1889Bull. Astron.,6, 141.   
Grebenikov, E. A. 1960 Byull. Inst. Teor. Astron. (Akad. Nauk SSSR), 7, 811.   
Grobner, W. 1960 Die Lie Reihen und ihre Anwendung, Deutscher Verlag der Wissenschaften,Berlin.   
Grosch, J. 1948Astron. J.,53,180.   
Gylden, H. 1869 Bull.Acad. Sci. Saint-Pétersbourg,14, 195. 1871 Mém.Acad. Sci. Saint-Petersbourg,16, no. 10. 1874 Kongl. Suenska Vetenskaps-Akad. Handl.,11, no.9. 1876 J. de Math. pures appl., ser. 3, 2, 411. 1877 Astron. Iaktt. Unders. Stockholm Obs., 1, no.1. 1881 Bihang Suenska Vetenskaps-Akad.Handl.,6, nos.8,9, 16. 1881a Astron. Nachr.,100,97;Compt.Rend., 92,1262;93,127. 1881b Vierteljahrsschrift Astron.Gesell,16,296. 1882 Bihang Suenska Vetenskaps-Akad. Handl., 7, no. 2. 1882a Acta Math., 1, 77. 1884 Mém. Acad. Sci. Saint-Pétersbourg, ser.7,32, no. 11. 1885 Acta Math., 7,125. 1887 Ibid., 9, 185. 1892 Ibid., 15, 65. 1893 Traite Analytique des Orbites Absolues des Huit Planetes Principales,I, Beijers Bokforlags,Stockholm. 1893a Acta Math., 17, 1. 1896 Astron. Iaktt.Unders. Stockholm Obs.,5, no.4. 1909 Traité Analytique des Orbites Absolues des Huit Planetes Principales,II, Beijers Bokforlags,Stockholm.   
Hagihara, Y.   
lphen, G. H. 1886 Traité des Fonctions Elliptiques et de leurs Applications,I,Gauthier-Villars, Paris. 1891 Ibid., III, 33.   
mid, S. E. 1951Astron. J.,56,126.   
mid, S.E., and Whipple, F.L. 1953Astron.J.,58,100.   
nsen, P. A. 1831 Untersuchungen üiber die gegenseitigen Storungen des Jupiters und Saturns, eine von Konigl. Akad.Wiss.zu Berlin am 8 Juli 183O gekronte Preisschrift,Berlin. 1938 Fundamenta Nova Investigationis Orbitae Verae Quam Luna Perlustrat, Gotha, Schriften der Sternwarte Seeberg. 1843 Ermitelung der absoluten Storungen in Ellipsen von beliebiger Excentricitat und Neigung, Gotha, Schriften der Sternwarte Seeberg. 1855 Entwicklung des Products einer Potenz des Radius Vectors u.s.w. Abhandl. K. sachs. Gesell. Wiss, 2, no. 3. 1856 Auseinandersetzung einer zweckmassigen Methode zur Berechnung der absoluten Storungen der kleinen Planeten, Abhandl. K. sachs. Gesell. Wiss., 3, no. 2. 1856a Mémoire sur le calcul des Perturbations quéprouue des Cometes， Comp. Rend. Suppl.,1, 121-378. 1857 Auseinanderset zung II,Abhandl.K. sächs.Gesell.Wiss.,4, no.1. 1857a Tables de la Lune,construites d'apres le Principe Newtonien de la Gravitation Universelle, published for the British Government by G.E.Eyre and G. Spottiswoode, London. 1859 Auseinandersetzung II, Abhandl. K. sächs. Gesell. Wiss, 5, no. 2. 1862 Darlegung der theoretischen Berechnung der in der Mondtafeln angewandten Storungen, Abhandl.K. sachs. Gesell. Wiss., 6, no.2. 1864 Ibid., 7, no. 1. 1867 Auseinandersetzung IV, ibid.,8, no.4. 1874 Uber die Darstellung der graden Aufsteigung und Abweichung des Mondes in Funktion der Lange in der Bahn und der Knotenlange,ibid., 10, no. 8.   
:rtner, W. 1928Mit. Univ. Sternwarte Frankfurt a.M., Part 5.   
:rzer, P. 1886 Mém. Acad. Sci. Saint-Petersbourg,ser.7, 34, no. 12. 1886a Astron.Iaktt. Unders. Stockholm Obs., 3, no. 4. 1891 Astron.Nachr., 126,399. 1895 Ibid., 139,33.   
:inrich, W. W. 1912Astron. Nachr., 194,209.   
Henrard, J. 1970° Celestial Mech., 3,107.   
Herget, P. 1947 Astron. J., 52, 177. 1948 The Computation of Orbits, private publication. 1950 Astron. Papers Am. Eph.Naut. Alm.,11,527. 1952 Astron. J., 57, 13. 1962 Ibid., 67, 16.   
Herget, P., and Musen, P. 1959 Astron.J., 64,11.   
Herrick, S. 1948 Pub. Astron.Soc.Pacific,60,321. 1952 Astron. J., 56,186. 1953 Ibid.,58, 156.   
Hill, G. W. 1874Astron. Nachr., 83, 209. Reprinted in Colected Mathematical Works, I,151 (1905),Carnegie Institution,Washington, D.C. 1881 Am.J. Math.,4,256.Reprinted in Collected Mathematical Works,I, 348. 1890 Astron. Papers Am.Eph.Naut.Alm.,4. Reprinted in Collected Mathematical Works,III,1 (1906). 1896 Astron. J.,16, 57.Reprinted in Collected Mathematical Works,IV, 111 (1907). 1898 Astron. Papers Am. Eph.Naut. Alm., 7,nos. 1,2.   
Hintze, K. H. 1952 Astron. Nachr.,280, 263.   
Hoppe, J. 1937 Astron. Nachr., 264, 337.   
Hori, G. 1957 Proc.Japan Acad.,33,395. 1957a Pub.Astron. Soc.Japan, 9,51. 1958 Proc.Japan Acad.,34,263.   
Huang, Su-Shu 1961 Astron.J.,66,157. 1962Ibid.,67,304.   
Huang, Su-Shu, and Wade, C. 1963Astron. J.,68,388.   
Hunter, M. W. 1967Space Sci. Rev., 6, 601.   
Ince, E. L. 1927Ordinary Diffrential Equations, Longmans, London.   
Iwanow, A. 1899 Bull.Acad. Sci. Saint-Petersbourg,10, no.1. 1900 Ibid., 13, no. 3. 1901 Ibid.,14, no.1.   
Jackson, D. 1930The Theory of Approximation,Am.Math.Soc., New York.   
Jefferys, W. H. 1968 Astron. J., 73, 522.   
Johnson, F. J. 1964 Celestial Mechanics and Astrodynamics,475, V. Szebehely,ed.,Academic Press, New York.   
Jupp, A. H. 1969Astron. J.,74,35. 1970Monthly Notices Roy. Astron. Soc., 148,197.   
Kahrstedt, A. 1951Astron. Nachr., 280,24.   
Kamel, A. A. 1969 Celestial Mech., 1,190. 1970 Celestial Mech., 3,90.   
Kamienski, M. 1959Acta Astronomica,9, 53.   
Kaplun, S., and Lagerstrom, P. A. 1957J. Math. Mech.,6, 585.   
Kastel, G. R. 1965 Byull. Inst. Teor. Astron. (Akad. Nauk SSSR), 10,118.   
Kazimircak-Polonskaya, H.I. 1961 Trudi Inst. Teor. Astron. (Akad. Nauk SSSR), no. 7. 1962 Byull.Inst.Teor. Astron.(Akad. Nauk SSSR), 8, 459, 487. 1967Byull. Inst. Teor. Astron. (Akad. Nauk SSSR), 12, 3, 24,63.   
Kevorkian, J. 1962 Astron. J., 67, 204.   
Kevorkian, J., and Lancaster, J. E. 1968 Astron. J., 73, 791.   
Klauder, H. 1937 Astron. Nachr.,262, 233.   
Kline,J. E., and Herget, P. 1941 Astron. J.,49,121.   
Klinkerfues, W. 1863Abhandl. K. Gesell.Wiss. Gottingen, 11,3.   
Knapp, H. 1964 Monatshefte Math.,68,33. 1966 Mathematische Methoden der Himmelsmechanik und Astronautik 285,E.Stiefel,ed., Math.Forschungsinstitut, Oberwolfach.   
Koulikov, D. K. 1950Byull. Inst. Teor. Astron. (Akad. Nauk SSSR),4, 311.   
Kovalevsky, J. 1958 Astron. J., 63,452. 1959 Bull.Astron., 23, 1. 1959a Astron.J., 64,226. 1968 Astron. J., 73,203.   
Kozai, Y. 1959 Astron. J.，64, 367；Smithsonian Astrophys. Obs.，Spec. Rep. no. 22. 1902 Die genaherte absolute Bewegung des Planeten (108) Hecuba, Dissertation,Berlin. 1907Abhand. K. Gesell. Wiss. Gotingen, neue Folge,5, no. 3.   
Krassowski, J. 1916"Travaux Soc. Sci. Varsovie,II, Cl. Sci. Math. Natur., no.12.   
Kresak, L. 1965 Bull. Astron.Inst.Czech.,16,292.   
Kuhne, E.E. 1951 Astron. Nachr.,279,105.   
Kyner,W. T.,and Bennett, M.M. 1966 Astron. J., 71, 579.   
Lagerstrom, P. A., and Kevorkian, J. 1963Astron. J., 68,84. 1964 Celestial Mechanics and Astrodynamics,3,V.Szebehely,ed.,Academic Press, New York.   
Lancaster, J. E. 1970 Celestial Mech., 2, 481.   
Laplace, P. S. 1878 Oeuvres Completes de Laplace, I, Gauthier-Villars, Paris. 1878a Ibid., II.   
LeShack, A. B.,and Sconzo, P. 1968 Astron. J.,73,217.   
Lemekhova, E. N. 1961 Byull. Inst. Teor. Astron. (Akad.Nauk SSSR),8, 103.   
Lesser, O. 1861 Untersuchung über die allgemeinen Storungen der Metis,Dissertation, Dorpat.   
Leuschner, A. O. 1910Mem. Natl. Acad. Sci. Washington,10, no.7.   
Leuschner,A. O., Anderson, C. M., and Barndollar, E.J. 1937Pub. Astron. Soc.Pacific, 49, 190.   
Leuschner, A. O., Glancy, A. E., and Levy, S. H. 1922Mem.Natl. Acad. Sci.Washington,14.   
Le Veau, G. 1880 Ann. Obs. Paris, Mém., 15,A1. 1883 Ibid., 17,B1. 1892 Ibid., 20, C1.   
Le Verrier, D.J. J. 1857 Ann. Obs. Paris, Mém., 3, 203.   
Levi-Civita, T. 1903 Annali di Mat. pura appl., ser.3,9, 1. Reprinted in Opere Matematiche II, 279, Zanichelli,Bologna (1956). 1906 Acta Math., 30, 305. Reprinted in Opere Matematiche II, 419. 1919 Acta Math.,42,99.   
Lidov, M. P. 1961 Iskusstvennye Sputniki Zemli, no. 8, 5. 1966 Comm. Investig. Sci., Provincia Buenos Aires,La Plata.   
Lubbock, J. W. 1831 On the Theory of the Moon and on the Perturbations ofthe Planets,I, Phil.Trans.Roy. Soc.London,1831, 217. 1832 Ibid.II,Phil.Trans.Roy.Soc.London,1832,1,229,361,601. 1834 Ibid.III,Phil. Trans. Roy. Soc.London,1834, 123.   
Lubowe, A. G. 1970 Celestial Mech., 2,88.   
Ludendorff, H. 1897 DieJupiter-Storungen der Kleinen Planeten vom Hecuba-Typus,Dissertation, Berlin. 1899 Bull.Acad. Sci. Saint-Pétersbourg,10,no.1. 1900 Ibid., 13, no. 3. 1901 Ibid., 14, no. 1.   
Lyttleton, R. A. “1953'The Comets and their Origin, Cambridge University Press, London.   
Maitre, V. 1937J. des Observateurs, 20, 121.   
Makover, S.G. 1955Trudi Inst. Teor. Astron.(Akad. Nauk SSSR),no.4, 133. 1955a Byull. Inst. Teor. Astron. (Akad. Nauk SSSR),6, 214. 1964Ibid., 9,525.   
Makover, S.G., and Bokhan, N. A. 1961 Trudi Inst. Teor. Astron. (Akad. Nauk SSSR), no.8, 135.   
Marchal, Ch. 1966Bull. Astron.,ser. 3,1, 189.   
Marsden, B.G. 1968 Astron. J., 73,367. 1969Ibid., 74, 944. 1969a Ibid.,74,720. 1970Ibid.,75,206. 1970a Ibid., 75,75.   
Marsden, B.G., and Aksnes,K. 1967 Astron.J.,72,952.   
Masal, H. 1889 Kongl. Suenska Vetenskaps-Akad. Handl.,23, no. 7.   
Matukuma, T. 1917Proc.Phys.-Math. Soc. Japan, 9,2.   
McDonald, S. L., and Leuschner, A. O. 1952 Lick Obs.Publication, 20.   
Meinardus, G. 1964 Approximation von Funktionen und ihre numerische Behandlung,Springer, Berlin.   
Miachin, V.F. 1959 Byull. Inst. Teor. Astron.(Akad. Nauk SSSR),7, 257. 1961 Ibid., 8, 134. 1964 Ibid., 9,668.   
Milankovitch,M. 1939 Bull. Acad. Serbe Sci.,181,1. 1941Editions Speciales, Acad. Serbe Sci., Beograd.   
Mittag-Lefler, G. 1900 Acta Math., 23, 43. 1901 Ibid.,24,183,205. 1902 Ibid.,26,353. 1905 Ibid., 29,101. 1920 Ibid., 42,285.   
Montel, P. 1910 Lesons sur les Séries de Polynomes á une Variable Complexe,Gauthier-Villars, Paris.   
Morando, B. 1967Bull. Astron.,ser. 3, 1, 331.   
Morgan, H. R.,and Scott, F.P. 1939 Astron. J.,47, 193.   
Mulholland, J. D. 1967Astron. J., 72, 682.   
Musen, P. 1954 Astron. J., 59, 262. 1959 J. Geophys. Res., 64, 2271. 1961 J. Astronaut. Sci., 8, 48. 1961a J. Geophys.Res.,66,403. 1963 Ibid., 68,1439. 1964a NASA Technical Note D-230l and NASA Technical Note D-2152, National Aeronautics and Space Administration, Washington, D.C. 1964 J. des Observateurs,47, 73. 1965 Ibid., 48, 11. 1966 Ibid., 49, 54. 1966a J. Geophys. Res.,71, 5997. 1967 NASA Technical Note D-4169, National Aeronautics and Space Administration. Also in Bull. Astron., ser. 3, 3, 361. 1967a NASA Technical Note D-4002. National Aeronautics and Space Administration, Washington, D.C. 1968 NASA Technical Note D-4562.Also in J.Astronaut.Sci.,15,124.   
Musen, P., and Carpenter, L. 1963 J. Geophys.Res., 68,2727.   
Musen, P., and Maury, J. L., and Charnow, M.L. 1968NASA Technical Note D-4979, National Aeronautics and Space Administration, Washington, D.C.   
Nacozy, P. E. 1969Astron. J., 74, 544.   
Neubauer, F. J. 1938 Pub.Astron. Soc.Pacific, 50, 225.   
Newcomb, S. 1865Investigations of the Orbit of Neptune，Smithsonian Contribution to Knowledge,no. 199, Smithsonian Institution,Washington, D.C. 1UJ1Iviu., U, Hv. U, UJv. 1891a Ibid., 3, no. 1, 1. 1895a Ibid., 5, no.4, 297. 1895b Ibid.,5, no.2,49. 1895c Ibid., 5, no. 1, 1. 1898a Tables of the Four Inner Planets,Ibid.6;see also ibid.,1O (1940), 172; 11 (1943), 3. 1898b Tables of the Heliocentric Motion of Uranus,ibid.,7,no. 3,287. 1898c Tables of the Heliocentric Motion of Neptune,ibid.,7,no.4,417.   
Nicholson, S. B. 1944Astrophys. J., 100, 57.   
Norlund, N. E. 1926Differenzenrechnung, Springer, Berlin.   
Numerov, B. V. 1923 Pub. Obs.Astrophys. Central de Russie,2. 1924 Monthly Notices Roy.Astron. Soc.,84, 180, 592. 1926 Byull. Inst. Teor. Astron.(Akad. Nauk SSSR), nos.10,12. 1927 Astron.Nachr.,230,359. 1928 Ibid., 234, 1.   
Olsson, K. G. 1891 Bihang Svenska Vetenskaps-Akad.Handl.,17, no.4. 1893 Kongl. Suenska Vetenskaps-Akad.Handl., 25, no.8. 1896 Bihang Suenska Vetenskaps-Akad. Handl.,22, no. 1. 1896a Ibid.,22,no.2. 1896b Ofuersigt af Kongl. Vetenskaps-Akad.Forhandl., no.2, 55; no.3, 217. 1897 Bihang Suenska Vetenskaps-Akad.Handl.,22, no.5. 1900Ibid., 25, no.8.   
Oort, J. H. 1950Bull. Astron.Inst.Netherlands,11, 91, 259.   
Oort, J. H.,and Schmidt, M. 1951 Bull. Astron. Inst. Netherlands, 11, 419.   
Oppolzer, T. R. von 1880Lehrbuch zur Bahnbestimmung der Kometen und Planeten, II, Engelmann, Leipzig. 1886 Denkschriften Math.-Naturw.Cl., K. Akad. Wiss Wien, 51, 69. 1888 Ibid., 54, 49.   
Osten, H. 1920Astron.Iaktt.Unders. Stockholm Obs.,10, no.7.   
Ovenden, N. W., and Roy, A. E. 1961Monthly Notices Roy. Astron.Soc.,123,1.   
Painleve, P. 1896 Compt. Rend., 123,636,871. 1897 Lecons sur la Theorie Analytique des Equations Differentielles,professes a Stockholm,Hermann, Paris. 1897a Compt.Rend.,125,1078. 1899Ibid.,128,1505. 1902 Ibid.,135,11.   
Parker, E. N. 1958 Astrophys. J., 128, 664. 19601bid.,132,175.   
Payne, M. 1964 Celestial Mechanics and Astrodynamics, 53, V. Szebehely,ed.,Academic Press,New York.   
Pels, G. 1960 Bull.Astron. Inst. Netherlands,15,127.   
Pels-Kluyver, H. A. 1960 Bull.Astron.Inst. Netherlands,15,163.   
Penzo, P. A. 1964 Celestial Mechanics and Astrodynamics, 439, V. Szebehely， ed., Academic Press, New York.   
Perrotin, J. 1879Ann.Obs.Toulouse,1,B3.Also,Théorie de Vesta,Thesis,Paris.   
Picard, E. 1899 Compt.Rend., 128,1363.   
Picart, L. 1892 Ann. Obs. Bordeaux, 5.Also, Sur la Désagrégation des Essaims Meteoriques,Thesis, Paris.   
Pines, S. 1961 Astron. J., 66,5.   
Plana, G. A. A. 1832Theorie du Mouvement de la Lune (3 volumes), Torino.   
Poincare, H. 1889 Acta Math.,13,1. Reprinted in Oeuvres,VII,286,Gauthier-Villars,Paris (1952). 1902 Bull.Astron., 19, 177.Reprinted in Oeuures,VIII, 417 (1952). 1904 Bull.Astron., 21, 292.Reprinted in Oeures, VI1,619. 1904a Compt. Rend.,138,933. Reprinted in Oeuvres, VI, 583. 1905 Acta Math., 29, 235. Reprinted in Oeuvres, VII, 587. 1912 Calcul desProbabilites,2nd ed.，Chap.i6,Gauthier-Villars, Paris.   
Poisson, S. D. 1835 Mémoire sur le Mouvement de la Lune autour de la Terre, Mém. prés. ä l'Acad. Sci. Paris, ser. 3, 13,209.   
Pontecoulant, P.G. D.de 1846Theorie Analytique du Systeme du Monde, IV,Gauthier-Villars, Paris.   
Popovic, B. 1956 Bull. Soc. Math. Serbie,8,47. 1959 Ibid.,11, 151. 1961 Ann. Acad. Sci. Fennicae, ser. A, 3, 209. 1962 Bull.Soc.Math.Serbie, 14,169.   
Porter, V. G. 1952 Comets and Meteor Streams, Wiley, London. 1963 The Solar System, IV, B. M. Middlehurst and G. P. Kuiper, eds., University of Chicago Press, Chicago.   
Proskurine, V. F. 1949 Byull. Inst.Teor. Astron. (Akad. Nauk SSSR),4, 169. 1950 Ibid., 4, 355. 1952 Trudi Inst. Teor. Astron. (Akad. Nauk SSSR), no. 2, 1. 1955 Byull.Inst.Teor.Astron.(Akad.Nauk SSSR),9,25. 1962 Trudi Inst. Teor. Astron. (Akad.Nauk SSSR), no. 9, 1.   
Rabe, E. 1937 Sit zber.preuss. Akad.Wiss.Berlin,1937,209. 1942 Astron.Nachr.,272,208. 1943 Ibid., 273, 209.   
Radau, R. 1881 Bull.Sci.Math.,ser.2,5, 270. 1882 Compt. Rend.,95, 117. 1886 Bull.Astron.,3,433,475.   
Radyhski, M. A. 1935 Astron. Nachr., 257,33.   
Rasmusen, H. O. 1951" Pub.og mindre Meddelelser fra Kobenshauns Obs., no. 155.   
Reich, H. 1964 Celestial Mechanics and Astrodynamics, 34l,V.Szebehely,ed., Academic Press,New York.   
Robertson, H. R. 1937Monthly Notices Roy. Astron. Soc., 97,423.   
Roemer, E. 1961Astron. J., 66, 368. 1963 The Solar System, IV,chap.15, B. M. Middlehurst and G. P. Kuiper, eds., University of Chicago Press, Chicago.   
Rose, F. E. 1917 Astron. Papers Am. Eph. Naut. Alm., 9, part 2.   
Roure, H. 1939 J.des Obseruateurs,22,65,109,218. 1940 Ibid., 23,37, 55. 1946 Ibid.,29, 3. 1947a Ibid., 30, 31. 1947 Ibid.,30,49, 93. 1948 Ibid.,31,39. 1950 Bull.Astron.,ser.2,15,1,75.   
Runge, C., and Konig, H. 1924Vorlesungen über numerisches Rechnen, Springer, Berlin.   
Saari, D. G. 1969 Celestial Mech.,1, 331.   
Sampson, R. A. 1921 Mem. Roy. Astron. Soc., 63.   
Schmidt, A. 1888 Astron. Nachr., 119,321. 1889Ibid.,121,80.   
Scnuitz-Steinnell,C. A. 1898Die allgemeinen Jupiterstorungen des Planeten Alexandra,Dissertation, Lund.   
Schwarzschild, K. 1896Astron. Nachr.,141, 1.   
Sconzo, P. 1967Astron.Nachr., 290, 163.   
Sconzo,P., LeSchack,A.R., and Tobey, R. 1965Astron.J.,70,269.   
Sekanina, Z. 1966 Bull. Astron. Inst.Czech., 17,67. 1966a General Catalogue of Original and Future Comet Orbits, Pub. Astron. Inst.Charles Univ. Prague,no.48. 1967 Bull. Astron. Inst.Czech., 18,1. 1967a Bull. Astron. Inst.Czech.,18,15,19. 1969Astron.J.,74,944,1223.   
Sekanina, Z., and Vanysek, V. 1967Icarus, 7, 168.   
Sémirot, P. 1949 Bull. Astron., ser. 2, 14, 37.   
Serret, J. A. 1885 Cours d'Algebre Superieur, I,434.   
Shdanow, A. 1885Astron. Iaktt. Unders. Stockholm Obs., 3,1. 1885a Astron.Nachr.,111,113.   
Shen, Zee 1940 Jap. J. Astron. Geophys., 18, 1. 1941 Ibid., 19, 1, 217. 1957 Pub.Astron. Soc. Japan, 9,64.   
Shi, Y. Y., and Eckstein, M. C. 1967 Astron. J., 72, 685. 1968 Ibid., 73, 275. 1969 Ibid., 74, 551.   
Shniad, H. 1970 Celestial Mech., 2, 114.   
Shute, B. E. 1964 Celestial Mechanics and Astrodynamics, 377,V. Szebehely, ed., Academic Press,New York. 1966Astron. J.,71, 602.   
Sibuya, U. 1958Funkcionalaj Ekacioj,1,121.   
Skripnichenko, V.I. 1970 Byull. Inst. Teor. Astron. (Akad.Nauk SSSR),12, 16.   
Spencer Jones, H. 1939Monthly Notices Roy. Astron. Soc., 99, 541.   
Steffensen, J. F. 1955 Acta Math., 93, 169.   
Stellwacher-Amilhat, I. 1967 Bull. Astron., ser. 3, 1,215.   
Stracke, G. 1924Veroffentl. Astron.Recheninstitut, Berlin-Dahlem, no. 44. 1929 Bahnbestimmung der Planeten und Kometen, Springer, Berlin. 1929a Astron. Nachr., 236,97. 1930 Veroffentl.Astron.Recheninstitut,Berlin-Dahlem,48.   
Stromberg, G. 1916Astron. Iakt. Unders. Stockholm Obs.,10, no.3.   
Stromgren, B. 1929 Pub.og mindre Meddelelser fra Kobenshauns Obs., no. 65.   
Struble, R. A. 1960J. Math. Analys. Appl.,1,300. 1961a Archive Rat. Mech. Analysis,7,87. 1961 J.Math.Mech., 10, 691.   
Stumpff, K. 1943Astron. Nachr., 273,105. 1968 NASA Technical Note,D-4460,National Aeronautics and Space Administration,Washington, D.C.   
Subbotin, N. S. 1965 Byull.Inst. Teor. Astron.(Akad. Nauk SSSR),10, 143.   
Sundman, K. F. 1907 Acta Soc. Sci. Fennicae, 34, no.6. 1908 Ibid., 35, no. 9. 1913 Acta Math.,36,105.   
Takenouchi, T. 1954 Pub.Astron. Soc.Japan,6,113. 1954a Annals Tokyo Astron. Obs., ser. 2, 4, no. 3, 155.   
Thiele, T. N. 1882Astron.Nachr.,102,65.   
Tisserand, F. 1888Ann. Fac. Sci. Toulouse, 2, D1. 1889Bull. Astron., 6, 241,289.   
Tokmalayeva, S. S. 1956 Trudi Inst. Teor. Astron. (Akad. Nauk SSSR), no. 5,1.   
Trousset, J. 1913Etude Semi-Analytique du Mouvement du Huitieme Satelite de Jupiter, Thesis,Paris.Reprinted in Ann. Obs.Bordeaux,15,35. 1933 Ann. Obs. Bordeaux, 17, 3.   
Urabe, M. 1958Funkcionalaj Ekacioj,1,1.   
van der Corput, J. G. 1956 j.d'Analyse Math. (Jerusalem),4, 314.   
van Woerkom, A. J. J. 1948 Bull. Astron.Inst. Netherlands,10, 445.   
Villemarque, E. de la 1928J. des Obseruateurs,11, 37,65, 218. 1yzy J.aes Ubservateurs, 1Z,44, /Z, 1ZZ, 10z.   
von Haerdtl, E. F. 1891Abhandl. bayer. Akad. Wiss., II Kl., 17, no.3.   
von Zeipel, H. 1901"Mem. Acad. Sci. Saint-Petersbourg,12, no.8. 1901a Ibid.,12, no. 11. 1905 Bull.Astron.,22, 449.   
Voronov, N. M. 1935 Astron. Nachr.,254,329;256,157.   
Walsh, J. L. 1956Interpolation and Approximation by Rational Functions in the Complex Domain, Am. Math. Soc., Providence, R.I.   
Watson, J. C. 1900 Theoretical Astronomy,Lippincott, Philadelphia.   
Weiler, A. 1872 Pub.Astron. Gesell.,12. 1884 Astron. Nachr., 110, 49,145,241. 1889 Ibid.,120,97;122,49. 1891 Ibid., 127, 113. 1895 Ibid.,138,305,385.   
Whipple, F. L. 1938 Proc.Am. Phil. Soc., 79,499. 1940 Ibid., 83, 711. 1943 Revs.Mod.Phys.,15,246. 1947 Proc.Am.Phil.Soc.,91,189. 1950 Astrophys. J., 111, 375. 1951 Astron. J., 56, 51. 1952 Aduances in Geophys., 1, 119. 1954 Astron. J.,59,201,400. 1961 Ibid.,66, 375. 1962 Ibid., 67, 1. 1963 The Solar System, IV, chap. 19, B. M. Middlehurst and G. P. Kuiper, eds., University of Chicago Press, Chicago.   
Whipple, F.L., and Wright, F.W. 1954Monthly Notices Roy.Astron.Soc.,114, 229.   
Wilkens, A. 1932 Sitzber.bayer. Akad. Wiss., Math.-Naturw.Abt.,1932,1.   
Wilson, D. T. 1913 Astron.Iaktt. Unders. Stockholm Obs.,10, no.1.   
Wintner, A. 1930 Math. Z., 32, 668.   
Wittram, Th. 1885 Zur Berechnung der speziellen Storungen der kleinen Planeten, Dissertation, Dorpat.   
Wolf, M. 1891Astron.Iaktt Unders. Stockholm Obs.,4, no. 4.   
Yarov-Yarovoi, M. S. 1960 Astron. Zh., 37,908.   
Zelmer, G. K. 1967 Summation Methods in the Two- and Three-body Problem, Thesis, University of British Columbia,Vancouver.   
Zumkley, J. 1941 Astron. Nachr., 272,66.

# Hill's Lunar Theory

# HILL'S INTERMEDIARY ORBIT

# I1.1 HILL’S EQUATIONS OF MOTION

Newton in 1687, in his Principia Mathematica, could explain by semigeometrical theory only one-half of the observed motion of the lunar perigee. Clairaut in l747 presented a numerical theory by taking an ellipse with rotating perigee as a first approximation to the motion of the moon，and showed in his second approximation that Newton's law could satisfy the observed motion.D'Alembert worked out a similar analytical theory in 1751. Euler in his second theory of l772 referred to the moving rectangular coordinates for the first time,while his former theories, including his first theory of 1753,were based on the variation of elements. Euler initiated the representation of the coordinates by trigonometric series of time,and the approximation in powers of the eccentricities and inclinations,and also in powers of the disturbing force. T.Mayer published tables for the motion of the moon based on Euler's theory (Brown,1896).

Laplace's theory of 1770,which is included in the third volume of his Mécanique Celeste, published in l802,gave the general equations of motion; he developed a general method of solution by taking into account the figure of the earth and the planetary perturbation,and showed the meaning of the long-period and secular terms and the cause of the secular acceleration.In l802 Laplace used the true longitude as the independent variable instead of time,in order to attain a more rapid formal convergence of the series employed.Damoiseau numerically in 1827 and Plana analytically in 1832 worked out Laplace's method to