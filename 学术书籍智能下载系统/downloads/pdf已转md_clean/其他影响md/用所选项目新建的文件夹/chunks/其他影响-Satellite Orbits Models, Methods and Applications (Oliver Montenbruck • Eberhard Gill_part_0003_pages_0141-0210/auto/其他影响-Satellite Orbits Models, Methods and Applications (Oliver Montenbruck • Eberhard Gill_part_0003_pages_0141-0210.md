![](images/2010ccf0ad118d4d3e165ce3941ce71ce7c8a35a946effd7765db3fc98ba173d.jpg)  
Fig. 4.2. Performance diagram of several embedded Runge–Kutta–(Nyström) methods for test case D1 $\scriptstyle ( { \mathrm { e } } = 0 . 1 )$ of Hull et al. (1972). The number of function calls is plotted versus the accuracy in digits

to $2 0 / 2 \pi \approx 3 . 2$ revolutions. The analytical solution of the Kepler problem yields reference values

$$
\begin{array} { r c l l } { { y _ { 1 } ( t ) } } & { { = } } & { { \cos E - e } } & { { y _ { 2 } ( t ) = \ \sqrt { 1 - e ^ { 2 } } \sin E } } \\ { { } } & { { } } & { { } } \\ { { y _ { 3 } ( t ) } } & { { = } } & { { \displaystyle \frac { - \sin E } { 1 - e \cos E } } } & { { y _ { 4 } ( t ) = \ \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } \cos E } { 1 - e \cos E } } } \end{array}
$$

for calculating the total (global) integration error. The eccentric anomaly $E$ has to be obtained by an iterative solution of Kepler’s equation which takes the form

$$
E - e \sin { E } = t .
$$

Results for various Runge–Kutta and Runge–Kutta–Nyström methods are given in the performance diagram of Fig. 4.2. Here the total number of function evaluations is plotted against the final accuracy for an orbit of $e = 0 . 1$ (test case D1). For higher eccentricities one obtains similar results since the stepsize control of all methods is essentially the same. The following methods were used for the comparison:

DOPRI5 (RK5(4)7FM) is a 7-stage method of order 5 with an embedded method of order 4 developed by Dormand & Prince (1980). • DOPRI8 (RK8(7)13M) by Prince & Dormand (1981) requires 13 function evaluations for 8th-order approximation. The Fortran subroutines DOPRI5 and DOPRI8 used in the comparison are provided in Hairer et al. (1987). The authors recommend the lower-order method for relative accuracies of $1 0 ^ { - 4 }$ to $1 0 ^ { - 7 }$ , while DOPRI8 may be used for the adjacent range from $1 0 ^ { - 7 }$ to $1 0 ^ { - 1 3 }$ . The latter should not, however, be used for higher accuracies, since the coefficients are not given with a sufficient number of digits in this case.

RKF7 – a famous method developed by Fehlberg (1968) – is similar to DOPRI8 but uses the 7th-order method for integration, while the 8th-order method is only used for error estimation. A total of 13 function evaluations are required per step.   
DOPRIN (RKN7(6)9) is an embedded Runge–Kutta–Nyström method of order 7(6), which – in contrast to the aforementioned methods – is used for the direct integration of special second-order differential equations of type ${ \mathbf y } ^ { \prime \prime } = f ( t , { \mathbf y } )$ . The Fortran implementation is taken from Hairer et al. (1987).   
$\mathrm { R K N } ( \dot { x } ) 7 ( 8 )$ is a 13-stage Runge–Kutta–Nyström method of order 7 developed by Fehlberg (1975) which – in contrast to the other Nyström methods considered here – may also be used for second-order differential equations depending on $\dot { \boldsymbol { r } }$ . An implementation is described in Schastok et al. (1989).   
• FILG11 is based on the 11(10)th-order/17 stages RKN coefficient set K17M by Filippi & Gräf (1986) and has been implemented similar to DOPRIN.   
• RKN12(10)17M is a 12(10)th-order/17-stage Nyström method recently developed by Dormand et al. (1987). Implementations of this code are described in Brankin et al. (1987, 1989). The authors’ RKNINT program, which combines the RKN12(10) method with the RKN6(4) Runge–Kutta–Nyström triple (Dormand & Prince 1987), has been used for the present comparison. It allows the user to choose between a high-precision solution obtained with the 12th-order formulas and dense output at a somewhat lower precision. The code is also available under the name D02LAF in the well known NAG library.

The comparison of the various methods clearly shows that high-order methods are required to achieve accuracies of better than $1 0 ^ { - 8 }$ . Forcing a low-order code like DOPRI5 to produce a highly accurate solution by using small stepsizes results in excessive computing times. A comparison of RKF7 and DOPRI8 – both of which are embedded methods of order 7 and 8 – clearly shows the superiority of the approach of Dormand and Prince to optimize the higher-order method for calculating the solution and only use the low-order method for stepsize control. The excellent performance of the methods developed by Dormand and Prince is also seen in a comparison of DOPRI8 or DOPRIN with Fehlberg’s Nyström method $\mathrm { R K N } ( \dot { x } ) 7 ( 8 )$ . Methods like DOPRI8 or DOPRIN can be recommended for a wide range of accuracies, but high-order codes like FILG11 or RKN12(10) are certainly more efficient even for moderate accuracy requirements. Where applicable, the special Runge–Kutta–Nyström methods are preferable to standard Runge–Kutta methods of similar order.

The stepsize control of all codes performs well up to high eccentricities since all methods considered are embedded methods. Even though this is not essential for near-circular orbits, it facilitates the use of Runge–Kutta methods, since even a bad initial stepsize can easily be corrected to the optimum stepsize during the integration. All examples were calculated with a starting stepsize of $h { = } 0 . 1$ .

The discussion given here is intended to help the reader in a valuation of existing codes and a comparison with the entire range of Runge–Kutta and Runge–Kutta– Nyström methods available today. In Sect. 4.4 a subset of these methods is compared with multistep and extrapolation codes to provide a more general assessment of the performance of different types of integration methods.

# 4.2 Multistep Methods

The Runge–Kutta methods discussed so far may be characterized as single-step methods. No use is made of function values calculated in earlier steps, which means that all integration steps are completely independent of one another. This feature allows a compact implementation of single-step methods and makes them particularly easy to use. Since a new stepsize may be used in each step, single-step methods are well suited for differential equations with rapid changes in the function to be integrated.

One may, however, think of a completely different approach that tries to reduce the total number of function evaluations as much as possible by storing values from previous steps. This leads to the concept of multistep methods which are most efficient for differential equations defined by complicated functions with a lot of arithmetic operations.

The development of multistep integration methods in the 19th and early 20th centuries is closely linked with the work of astronomers who utilized them for an accurate description of solar system bodies. Among these are J. C. Adams, who is most famous for his contribution to the discovery of Neptune, F. R. Moulton, and Ph. H. Cowell, who accurately predicted the motion of Halley’s comet before its 1910 return.

# 4.2.1 Introduction

In order to illustrate the basic principles of multistep methods, it is assumed for the moment that one has already obtained approximate values $\eta _ { j }$ of the solution $\mathbf { \boldsymbol { y } } ( t _ { j } )$ at equidistant times $t _ { j } = t _ { 0 } + j h$ for $j = 0 , 1 , \ldots , i .$ Integrating both sides of the differential equation

$$
\dot { \mathbf { y } } = f ( t , \mathbf { y } )
$$

with respect to $t$ from $t _ { i }$ to $t _ { i + 1 }$ one obtains the equivalent expression

$$
\pmb { y } ( t _ { i + 1 } ) = \pmb { y } ( t _ { i } ) + \int _ { t _ { i } } ^ { t _ { i } + h } \pmb { f } ( t , \pmb { y } ( t ) ) d t \quad .
$$

The integral cannot, however, be evaluated as it is, since it depends itself on the unknown solution $\mathbf { \boldsymbol { y } } ( t )$ of the differential equation. To circumvent this difficulty, one replaces the integrand by a polynomial $\pmb { p } ( t )$ that interpolates some of the values

$$
\boldsymbol { f } _ { j } = f ( t _ { j } , \pmb { \eta } _ { j } )
$$

![](images/e6440b9b89163cf3e842dc518f689c591dd49b1306312dd4cc1546355798f65a.jpg)  
Fig. 4.3. Interpolation of four function values by a third-order polynomial

at previous times $t _ { j }$ that are already known according to the initial assumption. This results in

$$
\pmb { \eta } _ { i + 1 } = \pmb { \eta } _ { i } + \int _ { t _ { i } } ^ { t _ { i } + h } \pmb { p } ( t ) d t
$$

and the increment function of a multistep method is therefore given by

$$
\pmb { \phi } = \frac { 1 } { h } \int _ { t _ { i } } ^ { t _ { i } + h } \pmb { p } ( t ) d t \quad .
$$

As an example a third-order polynomial is considered (see Fig. 4.3), which is defined by the four function values $f _ { i - 3 } , f _ { i - 2 } , f _ { i - 1 }$ and $f _ { i }$ at times $t _ { i - 3 } , t _ { i - 2 }$ , $t _ { i - 1 }$ and $t _ { i }$ . This polynomial may be written as

$$
\pmb { p } ( t ) = \pmb { a } _ { 0 } + \pmb { a } _ { 1 } \sigma + \pmb { a } _ { 2 } \sigma ^ { 2 } + \pmb { a } _ { 3 } \sigma ^ { 3 }
$$

with $\sigma ( t ) = ( t - t _ { i } ) / h$ . This yields the simple expression

$$
\Phi = \int _ { 0 } ^ { 1 } ( a _ { 0 } + a _ { 1 } \sigma + a _ { 2 } \sigma ^ { 2 } + a _ { 3 } \sigma ^ { 3 } ) d \sigma = a _ { 0 } + a _ { 1 } / 2 + a _ { 2 } / 3 + a _ { 3 } / 4
$$

for the increment function. Substituting the coefficients

$$
\begin{array} { r } { \begin{array} { r l r } { \pmb { a } _ { 0 } } & { = ( } & { 6 { \pmb f } _ { i } ) / 6 } \\ { \pmb { a } _ { 1 } } & { = } & { ( - 2 { \pmb f } _ { i - 3 } \ + 9 { \pmb f } _ { i - 2 } - 1 8 { \pmb f } _ { i - 1 } + 1 1 { \pmb f } _ { i } ) / 6 } \\ { \pmb { a } _ { 2 } } & { = } & { ( - 3 { \pmb f } _ { i - 3 } + 1 2 { \pmb f } _ { i - 2 } - 1 5 { \pmb f } _ { i - 1 } \ + 6 { \pmb f } _ { i } ) / 6 } \\ { \pmb { a } _ { 3 } } & { = } & { ( - 1 { \pmb f } _ { i - 3 } \ + 3 { \pmb f } _ { i - 2 } \ - 3 { \pmb f } _ { i - 1 } \ + 1 { \pmb f } _ { i } ) / 6 } \end{array} } \end{array}
$$

finally leads to the 4th-order Adams–Bashforth formula

$$
\pmb { \phi } _ { \mathrm { A B } 4 } = \frac { 1 } { 2 4 } ( - 9 \pmb { f } _ { i - 3 } + 3 7 \pmb { f } _ { i - 2 } - 5 9 \pmb { f } _ { i - 1 } + 5 5 \pmb { f } _ { i } ) ~ ,
$$

which may be used to calculate the approximate solution

$$
\pmb { \eta } _ { i + 1 } = \pmb { \eta } _ { i } + h \pmb { \phi } _ { \mathrm { A B 4 } }
$$

of the differential equation at $t _ { i + 1 } = t _ { i } + h$ . Repeated application of the Adams– Bashforth formula then yields the solution of the differential equation for subsequent times $t _ { i } + j h$ .

In order to start the integration scheme the first four values $f _ { 0 }$ , $f _ { 1 }$ , $f _ { 2 }$ and $f _ { 3 }$ or, equivalently, $\pmb { \eta } _ { 0 }$ , $\pmb { \eta } _ { 1 }$ , $\pmb { \eta } _ { 2 }$ and $\pmb { \eta } _ { 3 }$ are required. They may, for example, be obtained from $t _ { 0 }$ and $\pmb { \eta } _ { 0 }$ using three steps of a fourth or higher-order Runge–Kutta method with sufficient accuracy.

# 4.2.2 Adams–Bashforth Methods

The simple procedure described in the introductory section may easily be extended to derive general multistep methods of arbitrary order.

For this purpose one makes use of Newton’s formula for a polynomial $\pmb { p } _ { m } ^ { i }$ of order $m - 1$ that interpolates $m$ points

$$
( t _ { i - m + 1 } , \ : f _ { i - m + 1 } ) \ : , \ : \ : \ : \dots \ : , \ : \ : \ : ( t _ { i } , \ : f _ { i } )
$$

with equidistant nodes $t _ { i }$ . This polynomial is given by the compact expression

$$
\pmb { p } _ { m } ^ { i } ( t ) = \pmb { p } _ { m } ^ { i } ( t _ { i } + \sigma h ) = \sum _ { j = 0 } ^ { m - 1 } ( - 1 ) ^ { j } \left( { - \sigma \atop j } \right) \nabla ^ { j } \pmb { f } _ { i } \quad ,
$$

where the binomial coefficient stands for

$$
\binom { - \sigma } { j } = \frac { ( - \sigma ) ( - \sigma - 1 ) \dots ( - \sigma - j + 1 ) } { j ! }
$$

if $j > 0$ and is equal to 1 for $j = 0$ . The backward differences of $f _ { i }$ are recursively defined by

$$
\begin{array} { l l l } { \nabla ^ { 0 } \pmb { f } _ { i } } & { = } & { \pmb { f } _ { i } } \\ { \nabla \pmb { f } _ { i } } & { = } & { \pmb { f } _ { i } - \pmb { f } _ { i - 1 } } \\ { \nabla ^ { n } \pmb { f } _ { i } } & { = } & { \nabla ^ { n - 1 } \pmb { f } _ { i } - \nabla ^ { n - 1 } \pmb { f } _ { i - 1 } } \end{array}
$$

and may be computed from the given function values as outlined in Fig. 4.4.

Using this notation the increment function of the mth-order Adams–Bashforth multistep method may now be written as

$$
\pmb { \phi } _ { \mathrm { A B } m } = \frac { 1 } { h } \int _ { t _ { i } } ^ { t _ { i } + h } \pmb { p } _ { m } ^ { i } ( t ) d t = \sum _ { j = 0 } ^ { m - 1 } \gamma _ { j } \nabla ^ { j } \pmb { f } _ { i }
$$

with stepsize independent coefficients

$$
\gamma _ { j } = ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } { \binom { - \sigma } { j } } d \sigma ~ .
$$

$$
\begin{array} { l c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } { f _ { i - 4 } } & { \cdots } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } &   \end{array}
$$

Fig. 4.4. Backward difference table for polynomial interpolation   
Table 4.4. Coefficients of Adams–Bashforth methods in backwards difference notation   

<table><tr><td></td><td>j012345</td><td></td><td></td><td></td><td></td><td></td><td>6</td><td>7</td><td>8</td></tr><tr><td></td><td></td><td>21</td><td>台</td><td>3</td><td>251 720</td><td>95 288</td><td>19087 60480</td><td>5257 17280</td><td>1070017 3628800</td></tr></table>

Numerical values of $\gamma _ { 0 } \ldots \gamma _ { 8 }$ are given in Table 4.4. They may be obtained from a simple recurrence relation (see e.g. Hairer et al. 1987):

$$
\gamma _ { j } = 1 - \sum _ { k = 0 } ^ { j - 1 } \frac { 1 } { j + 1 - k } \gamma _ { k } .
$$

The local truncation error of the Adams–Bashforth method decreases with the order $m$ and may be estimated by comparing two methods of order $m$ and $m + 1$ :

$$
\begin{array} { r } { e _ { \mathrm { A B } m } = | { \boldsymbol y } ( t _ { i } + h ) - \eta _ { \mathrm { A B } m } | \approx | \eta _ { \mathrm { A B } m + 1 } - \eta _ { \mathrm { A B } m } | = h | \gamma _ { m } \nabla ^ { m } { \boldsymbol f } _ { i } | ~ . } \end{array}
$$

Since $\nabla ^ { m } f / h ^ { m }$ is an approximation of the $m$ -th derivative of $f$ , the truncation error may also be expressed as

$$
e _ { \mathrm { A B } m } \approx h ^ { m + 1 } | \gamma _ { m } f _ { i } ^ { ( m ) } | = h ^ { m + 1 } | \gamma _ { m } y _ { i } ^ { ( m + 1 ) } |
$$

which shows that the order of the Adams–Bashforth method is equal to the number $( m )$ of nodes $( t _ { i - m + 1 } \ldots t _ { i } )$ .

Substituting the definition of backwards differences into (4.54), the increment function may also be written in terms of the function values $f _ { j }$ :

$$
\Phi _ { \mathrm { A B } m } = \beta _ { m 1 } f _ { i - m + 1 } + \ldots + \beta _ { m m } f _ { i } = \sum _ { j = 1 } ^ { m } \beta _ { m j } f _ { i - m + j } \quad .
$$

This formulation of the increment function, which has already been used in our introductory example, avoids the computation of the backwards differences and is therefore more convenient and efficient as long as methods of fixed order are considered. There are, however, several applications where (4.54) is preferable, since the use of backwards differences allows a straightforward estimation of the local truncation error and an easy change of the order from one step to the next.

Table 4.5. Coefficients of Adams–Bashforth methods up to order $m = 8$ .   

<table><tr><td>j</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td></td></tr><tr><td>所附晰附晰附防的</td><td>1 一云</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The new coefficients $\beta _ { m j }$ – which are no longer independent of the order $m -$ may be obtained from the $\gamma _ { j }$ ’s using the relation

$$
\beta _ { m j } = ( - 1 ) ^ { m - j } \sum _ { l = m - j } ^ { m - 1 } \gamma _ { l } \binom { l } { m - j }
$$

for $j = 1 , \ldots , m$ (Grigorieff 1977). Explicit values are given in Table 4.5.

# 4.2.3 Adams–Moulton and Predictor–Corrector Methods

In the mth-order Adams–Bashforth method the polynomial $\pmb { p } ( t )$ is defined by $m$ function values up to and including $f _ { i }$ at time $t _ { i }$ . The integration is, however, performed over the subsequent interval $t _ { i } \ldots t _ { i + 1 }$ where the approximation cannot be expected to be very good.

Another type of multistep method – known as the Adams–Moulton method – therefore uses the polynomial $p _ { m } ^ { i + 1 } ( t )$ which interpolates $m$ function values at time steps $t i - m + 2$ and $t _ { i + 1 }$ :

$$
p _ { m } ^ { i + 1 } ( t ) = { p } _ { m } ^ { i + 1 } ( t _ { i } + \sigma h ) = \sum _ { j = 0 } ^ { m - 1 } ( - 1 ) ^ { j } \left( { - \sigma + 1 \atop j } \nabla ^ { j } { f _ { i + 1 } } \right. \ .
$$

Upon integration this yields the Adams–Moulton formula

$$
\pmb { \phi } _ { \mathrm { A M } m } = \frac { 1 } { h } \int _ { t _ { i } } ^ { t _ { i } + h } \pmb { p } _ { m } ^ { i + 1 } ( t ) d t = \sum _ { j = 0 } ^ { m - 1 } \gamma _ { j } ^ { * } \nabla ^ { j } \pmb { f } _ { i + 1 }
$$

with coefficients

$$
\gamma _ { j } ^ { \ast } = ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } { \binom { - \sigma + 1 } { j } } d \sigma
$$

that are given in Table 4.6. Further values may be calculated from the recurrence relation

$$
\gamma _ { j } ^ { * } = - \sum _ { k = 0 } ^ { j - 1 } \frac { 1 } { j + 1 - k } \gamma _ { k } ^ { * } .
$$

Table 4.6. Coefficients of Adams–Moulton methods in backwards difference notation   

<table><tr><td>j</td><td></td><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>2</td><td></td><td>山</td><td>元</td><td>会</td><td>-19</td><td>=</td><td>-863</td><td>-275</td><td>-33953</td></tr><tr><td></td><td>1</td><td></td><td></td><td></td><td>720</td><td>160</td><td>60480</td><td>24192</td><td>3628800</td></tr></table>

The order of the Adams–Moulton method is equal to $m$ and is, therefore, the same as that of an Adams–Bashforth method involving $m$ grid points for the interpolating polynomial. The local truncation error of the Adams–Moulton method, which is given by

$$
e _ { \mathsf { A M } m } \approx h ^ { m + 1 } | \gamma _ { m } ^ { * } { \pmb { y } } _ { i } ^ { ( m + 1 ) } | \quad ,
$$

is smaller, however, than that of an Adams–Bashforth method of equal order, since the error constant $| \gamma _ { m } ^ { * } |$ is smaller than $| \gamma _ { m } |$ .

As with the Adams–Bashforth methods, the backwards differences may be substituted to yield a formulation that depends on $f _ { j }$ only:

$$
\Phi _ { \mathrm { A M } m } = \beta _ { m 1 } ^ { * } f _ { i - m + 2 } + \ldots + \beta _ { m m } ^ { * } f _ { i + 1 } = \sum _ { j = 1 } ^ { m } \beta _ { m j } ^ { * } f _ { i + 1 - m + j } .
$$

The coefficients $\beta _ { m j } ^ { * }$ (see Table 4.7) of the $m$ th-order method may be obtained from the $\gamma _ { j } ^ { * }$ using the relation

$$
\beta _ { m j } ^ { * } = ( - 1 ) ^ { m - j } \sum _ { l = m - j } ^ { m - 1 } \gamma _ { l } ^ { * } \binom { l } { m - j }
$$

for $j = 1 , \ldots , m$ (Grigorieff 1977).

Since the increment function of the Adams–Moulton method depends on

$$
\begin{array} { r } { \pmb { f } _ { i + 1 } = \pmb { f } ( t _ { i + 1 } , \pmb { \eta } _ { i + 1 } ) \quad , } \end{array}
$$

it is not possible to calculate an explicit solution at $t _ { i + 1 }$ from

$$
\pmb { \eta } _ { i + 1 } = \pmb { \eta } _ { i } + h \pmb { \Phi } _ { \mathrm { A M } m } \quad .
$$

Table 4.7. Coefficients of Adams–Moulton methods up to order $m = 8$ .   

<table><tr><td>j</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>阿附陶晰晰防附</td><td>1 云 -19 720</td><td>1 品 4 106</td><td>市 -264 720</td><td>4 646 720</td><td>2</td><td></td><td></td><td></td></tr></table>

The Adams–Moulton formula is therefore called an “implicit” method and some iterative procedure is required to solve for $\pmb { \eta } _ { i + 1 }$ .

To avoid this difficulty, an Adams–Bashforth method of order $m$ is usually combined with an Adams–Moulton method of order $m$ or $m + 1$ in a so-called predictor–corrector or PECE-algorithm which consists of four steps:

1. In the first step – the Predictor step – an initial estimate of the solution at $t _ { i + 1 }$ is calculated from the Adams–Bashforth formula

$$
\pmb { \eta } _ { i + 1 } ^ { \mathrm { p } } = \pmb { \eta } _ { i } + h \pmb { \Phi } _ { \mathrm { A B } } \quad .
$$

2. The result is used in the $E$ valuation step to find the corresponding function value

$$
\begin{array} { r } { \pmb { f } _ { i + 1 } ^ { \mathrm { p } } = \pmb { f } ( t _ { i + 1 } , \pmb { \eta } _ { i + 1 } ^ { \mathrm { p } } ) \ \mathrm { ~ . ~ } } \end{array}
$$

3. In the third step – called the $C$ orrector – the Adams–Moulton formula is applied to find an improved value

$$
\pmb { \eta } _ { i + 1 } = \pmb { \eta } _ { i } + h \pmb { \varPhi } _ { \mathrm { A M } } ( \pmb { f } _ { i + 1 } ^ { \mathrm { p } } ) \quad .
$$

4. The final $E$ valuation step yields the updated function value

$$
\pmb { f } _ { i + 1 } = \pmb { f } ( t _ { i + 1 } , \pmb { \eta } _ { i + 1 } )
$$

which may then be used for the start of the next integration step.

In principle the third and fourth step would have to be repeated until convergence is achieved to find the exact solution of the Adams–Moulton formula, but since each such iteration costs another function evaluation, this would not be worth the effort. A single corrector step is enough to assure that the order of the combined Adams–Bashforth–Moulton method is equal to that of the implicit method, even though the local truncation error is slightly larger (cf. Grigorieff 1977).

The justification for using the somewhat complicated predictor–corrector algorithm, lies in the stability of multistep methods at large stepsizes. Due to the truncation at a fixed order and a limited computing accuracy, the individual steps of the numerical integration are always affected by small local errors. An analysis of the way in which these errors are propagated from one step to the next shows that the errors may grow exponentially for large stepsizes. In order to avoid this unfavorable behavior and to guarantee stability, the stepsize may not exceed a certain limit that depends on the method and the differential equation to be solved.

Low-order methods are generally more stable even for large stepsizes. Due to their modest accuracy, small steps have to be used anyway and stability is often not a serious problem. When using high-order multistep methods, however, stability can pose stringent limits on the allowed stepsize. Even steps that yield a sufficiently small truncation error may then be too large since the propagation of local errors could result in an unbounded growth of the global integration error.

The implicit Adams–Moulton methods behave much better in this respect than the explicit Adams–Bashforth methods and even the approximate solution of the Adams–Moulton formula in the PECE algorithm improves the stability considerably. This is the main reason why it is generally recommended to use one additional function evaluation for the corrector step. Another advantage is that the local truncation error can be reduced by using the corrector. The doubled expense for a single integration step can at least partially be compensated for by larger stepsizes.

![](images/3eed788ec46f1f50728a0fd32e2d3f1ad71b2819bdf00135c06bd79ca8bf168f.jpg)  
Fig. 4.5. A plot of the global integration error versus time $t$ for an orbit of $e = 0 . 1$ reveals the effect of instability of high-order Adams–Bashforth methods

To illustrate the practical meaning of stability, the two-body problem (D1) has been integrated with both a 6th-order and an 8th-order Adams–Bashforth method (AB6, AB8) at a stepsize of $h = 0 . 0 4$ (see Fig. 4.5). Since the local truncation error decreases with higher order, one might expect more precise results for the

AB8 method, but the growth of the global integration error clearly shows the onset of instability. When combined with a corrector, the resulting Adams–Bashforth– Moulton method (ABM8) is stable, however, even at twice the stepsize.

As a compromise between a cheap predictor-only method and a more stable PECE method, a PECE∗ algorithm (cf. Long et al. 1989) may be useful for the treatment of perturbed satellite orbits. Here $\mathrm { E ^ { * } }$ stands for a pseudo-evaluate step, which means that some simplifications are made in the final evaluation step. According to (4.4) the evaluation of $f$ involves the computation of the acceleration

$$
{ \pmb a } ( t , { \pmb r } , \dot { \pmb r } ) = - \frac { G M _ { \oplus } } { r ^ { 3 } } { \pmb r } + { \pmb p } ( t , { \pmb r } , \dot { \pmb r } ) ,
$$

where the dominant first term arises from the central gravity field of the Earth and $\pmb { p }$ means the sum of all perturbations. Since the perturbations are much smaller than the central force, one makes a small error only if one does not recompute them after the corrector step. In a pseudo-evaluate step only the dominant term of the total acceleration is therefore updated with the coordinates obtained in the corrector step, while the perturbations are taken from the predictor step:

$$
{ \pmb a } ^ { * } ( t , r , { \dot { r } } ) = - \frac { G M _ { \oplus } } { r ^ { 3 } } { \pmb r } + { \pmb p } ( t , r ^ { \mathnormal ^ { \mathrm { p } } } , { \dot { r } } ^ { \mathnormal { \mathrm { p } } } ) \quad .
$$

Since the computation of the perturbations is much more time-consuming than that of the central acceleration term, the $\mathrm { P E C E ^ { * } }$ method increases the stability at almost no additional cost.

Irrespective of the use of a stabilizing corrector step one should not arbitrarily increase the order of a multistep method in an attempt to increase the stepsize and the accuracy. For the requirements of typical orbit computations orders in the range from 8 to 12 can usually be recommended.

# 4.2.4 Interpolation

The multistep methods of Adams’ type may be extended in a straightforward manner to provide a solution at intermediate output points. For this purpose it is assumed that a PECE step of size $h$ has been used to advance from $t _ { i }$ to $t _ { i + 1 }$ and that one is interested in the approximate solution at some time $t = t _ { i } + \sigma h$ , where $0 < \sigma < 1$ . From a total of $m + 1$ points

$$
( t _ { i - m + 1 } , \mathbf { { f } } _ { i - m + 1 } ) , \ldots , ( t _ { i } , \mathbf { { f } } _ { i } ) , ( t _ { i + 1 } , \mathbf { { f } } _ { i + 1 } ^ { \mathrm { p } } )
$$

one may construct the interpolating polynomial

$$
p _ { m + 1 } ^ { * , i + 1 } ( t ) = p _ { m + 1 } ^ { * , i + 1 } ( t _ { i } + \sigma h ) = \sum _ { j = 0 } ^ { m } ( - 1 ) ^ { j } \left( { - \sigma + 1 \atop j } \nabla ^ { j } f _ { i + 1 } ^ { * } \right.
$$

that was already used in the implicit Adams–Moulton formula of the corrector step. Here the $^ *$ denotes that $f _ { i + 1 } ^ { \mathrm { p } }$ is a predictor value while all other $f _ { j }$ result from the

final (corrector) values of previous steps. Inserting this polynomial into the integral form of the differential equation leads to

$$
\pmb { \eta } ( t _ { i } + \sigma h ) = \pmb { \eta } _ { i } + \int _ { t _ { i } } ^ { t _ { i } + \sigma h } \pmb { p } _ { m + 1 } ^ { * , i + 1 } ( t ) d t
$$

or

$$
\pmb { \eta } ( t _ { i } + \sigma h ) = \pmb { \eta } _ { i } + h \sum _ { j = 0 } ^ { m } \hat { \gamma } _ { j } ( \sigma ) \nabla ^ { j } \pmb { f } _ { i + 1 } ^ { * }
$$

with

$$
\hat { \gamma } _ { j } ( \sigma ) = \int _ { 0 } ^ { \sigma } ( - 1 ) ^ { j } \left( \begin{array} { c } { { - s + 1 } } \\ { { j } } \end{array} \right) d s ~ .
$$

The coefficients $\hat { \gamma } _ { j }$ depend on $\sigma$ and must therefore be calculated separately for each desired output value. Appropriate recurrence relations may be found e.g. in Shampine & Gordon (1975). Since the differential equations that are usually treated by multistep methods are characterized by complicated functions $f$ , the computational effort for the interpolation coefficients is negligible in most applications.

It should be noted that the interpolant given here is continuous at the grid points $t _ { i }$ , by definition, but that the same is not true for the first derivative. For a more detailed discussion of smooth interpolants we refer to Watts & Shampine (1986) and Higham (1989).

# 4.2.5 Variable Order and Stepsize Methods

In the derivation of the Adams–Bashforth and Adams–Moulton methods it has so far been assumed that the solution of the differential equation is calculated with a constant stepsize, i.e. on a series of equidistant time points. This concept has to be modified whenever the behavior of the solution requires changes of the stepsize during the integration.

The easiest way to realize a variable stepsize consists of stopping the integration and calculating new starting values for another stepsize (e.g. with a Runge–Kutta method) whenever the current stepsize has to be modified. Alternatively one may use interpolation formulas like those described above to find a new set of starting values. Both approaches are feasible when stepsize changes are rare events, i.e. when a constant stepsize can be used for most of the integration.

A more flexible solution is obtained by generalizing the Adams formulas of the previous sections. In the case of arbitrary stepsizes the mth-order predictor formula for the computation of the solution at $t _ { i + 1 }$ may be written as

$$
\eta _ { i + 1 } = \eta _ { i } + ( t _ { i + 1 } - t _ { i } ) \cdot \sum _ { j = 0 } ^ { m - 1 } g _ { j } ( i ) \phi _ { j } ( i ) ~ .
$$

Here the factors

$$
g _ { j } ( i ) = \frac { 1 } { t _ { i + 1 } - t _ { i } } \int _ { t _ { i } } ^ { t _ { i + 1 } } \prod _ { l = 0 } ^ { j - 1 } \frac { t - t _ { i - l } } { t _ { i + 1 } - t _ { i - l } } d t
$$

correspond to the coefficients $\gamma _ { j }$ of the fixed stepsize formula, while the

$$
\pmb { \phi } _ { j } ( i ) = \prod _ { l = 0 } ^ { j - 1 } ( t _ { i + 1 } - t _ { i - l } ) \cdot \pmb { f } [ t _ { i } , \dots , t _ { i - j } ]
$$

replace the backward differences $\nabla ^ { j } \boldsymbol { f } _ { i }$ (see e.g. Hairer et al. 1987). The expressions $f [ t _ { i } , \ldots , t _ { i - j } ]$ are known as divided differences and result from the use of Newton’s formula for a general interpolation polynomial. They are recursively defined by

$$
{ \begin{array} { l c l } { f [ t _ { i } ] } & { = } & { f _ { i } } \\ { f [ t _ { i } , t _ { i - 1 } ] } & { = } & { { \frac { f _ { i } - f _ { i - 1 } } { t _ { i } - t _ { i - 1 } } } } \\ { f [ t _ { i } , t _ { i - 1 } , t _ { i - 2 } ] } & { = } & { { \frac { f [ t _ { i } , t _ { i - 1 } ] - f [ t _ { i - 1 } , t _ { i - 2 } ] } { t _ { i } - t _ { i - 2 } } } } \\ { ~ } & { ~ } & { ~ } \end{array} }
$$

For constant stepsize $h$

$$
f [ t _ { i } , \dots , t _ { i - j } ] = { \frac { 1 } { h ^ { j } } } \nabla ^ { j } f _ { i } ~ .
$$

The coefficients $g _ { j } ( i )$ and $\phi _ { j } ( i )$ as well as those of a corresponding corrector formula may be calculated from recurrence relations which are essential for an efficient implementation of variable order methods (see e.g. Shampine & Gordon 1975).

For the selection of order and stepsize the error for the order currently in use is estimated as well as the expected error for adjacent orders. At the same time a new stepsize is calculated based on the current error estimate and the current order. Evaluating this information a new order or stepsize can be chosen. Since changes in the stepsize require an increased effort for the computation of the coefficients $g _ { j } ( i )$ the stepsize is changed only if the recommended stepsize is larger or smaller than the present one by a factor of at least two.

A great advantage of variable order and stepsize methods is the fact that they do not require a starting procedure. Starting from order one and a very small initial stepsize, both order and stepsize may be increased up to an optimum value within a few steps. This makes variable order and stepsize codes particularly easy to use. Among the various implementations the following are mentioned:

• DVDQ – developed at the Jet Propulsion Laboratory by Krogh (1969, 1974) – is one of the earliest variable order and stepsize multistep codes. DVDQ has, for example, been used for the numerical integration of the solar system ephemeris DE102 (Newhall et al., 1983).

DE/DEABM is one of the most popular methods of its kind. The code and its theoretical background are explained in detail in the textbook of Shampine & Gordon (1975). The original code DE has since been improved to meet the needs of program libraries (Shampine & Watts 1979) and is available under the name DEABM now. Further amendments of the interpolation routines are reported in Watts & Shampine (1986).

VOAS is a variable order and stepsize multistep code by Sedgwick (1973). Aside from a different implementation its characteristics and performance are similar to DE/DEABM.

The predictor–corrector method of Hall & Watts – implemented as D02CJF in the NAG Fortran library – provides interpolation for dense output similar to DE/DEABM.

# 4.2.6 Stoermer and Cowell Methods

In the discussion of Runge–Kutta methods, Nyström methods have been introduced that are especially designed for the direct integration of second-order differential equations. Corresponding multistep methods that are known as Stoermer and Cowell methods may be derived by an extension of the concept of Adams methods. For this purpose the differential equation

$$
\pmb { \ddot { r } } = \pmb { a } ( t , \pmb { r } )
$$

is integrated twice to form the equivalent integral equation

$$
r ( t _ { i } + h ) = r _ { i } + h \dot { r } _ { i } + \int _ { t _ { i } } ^ { t _ { i } + h } \int _ { t _ { i } } ^ { t } a ( \tau , r ( \tau ) ) d \tau d t .
$$

Using partial integration the double integral can be replaced by a single integral:

$$
\begin{array} { l l l } { \displaystyle { t _ { i } + h } } & { \displaystyle { t } } \\ { \displaystyle { \int _ { t _ { i } } { 1 \cdot \int _ { t _ { i } } ^ { \theta } ( \tau , { r ( \tau ) } ) d \tau d t } } } & { = } & { \displaystyle { \left( t \cdot \int _ { t _ { i } } ^ { t } a ( \tau , { r ( \tau ) } ) d \tau \right) \left| _ { t _ { i } } ^ { t _ { i } + h } - \int _ { t _ { i } } ^ { t _ { i } + h } a ( t , { r ( t ) } ) d t \right. } } \\ { \displaystyle } & { = } & { \displaystyle { \int _ { t _ { i } } ^ { t _ { i } + h } ( t _ { i } + h - t ) a ( t , { r ( t ) } ) d t } } \\ & { = } & { \displaystyle { \ I _ { t _ { i } } } } \\ & { = } & { \displaystyle { \left. \int _ { 0 } ^ { t } ( 1 - s ) a ( t _ { i } + s h , { r ( t _ { i } + s h ) } ) d s \right. } . } \end{array}
$$

Table 4.8. Coefficients of Stoermer and Cowell methods in backwards difference notation. See e.g. Schubart & Stumpff (1966) for higher-order coefficients.

$$
\begin{array} { c c c c c c c c c } { { \small j } } & { { | \begin{array} { c c c c c c c c c } { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } & { { 6 } } & { { 7 } } & { { 8 } } \\ { { \delta _ { j } | 1 } } & { { 0 } } & { { { \frac { 1 } { 1 2 } } } } & { { { \frac { 1 } { 1 2 } } } } & { { { \frac { 1 9 } { 2 4 0 } } } } & { { { \frac { 3 } { 4 0 } } } } & { { { \frac { 8 6 3 } { 1 2 0 9 6 } } } } & { { { \frac { 2 7 5 } { 4 0 3 2 } } } } & { { { \frac { 3 3 9 5 3 } { 5 1 8 4 0 0 } } } } \end{array}   } }  \\ { {   \begin{array} { c c c c c c c c c c } { { \delta _ { j } ^ { * } } } & { { - 1 } } & { { { \frac { 1 } { 1 2 } } } } & { { 0 } } & { { { \frac { - 1 } { 2 4 0 } } } } & { { { \frac { - 1 } { 2 4 0 } } } } & { { { \frac { - 2 2 1 } { 6 0 4 8 0 } } } } & { { { \frac { - 1 9 } { 6 0 4 8 } } } } & { { { \frac { - 9 8 2 9 } { 3 6 2 8 8 0 0 } } } } \end{array} | } }  \end{array}
$$

By adding $r ( t _ { i } + h )$ and $r ( t _ { i } - h )$ one can eliminate the velocity ${ \dot { \boldsymbol { r } } } _ { i }$ , which results in

$$
\begin{array} { r l } {  { r ( t _ { i } + h ) - 2 r ( t _ { i } ) + r ( t _ { i } - h ) } } \\ & { = h ^ { 2 } \int ( 1 - s ) [ a ( t _ { i } + s h , r ( t _ { i } + s h ) ) + a ( t _ { i } - s h , r ( t _ { i } - s h ) ) ] d s } \\ & { = \ 0 } \end{array} .
$$

As in the derivation of the Adams–Bashforth formulas one may now use a polynomial through $m$ points

$$
( t _ { i - m + 1 } , \pmb { a } _ { i - m + 1 } ) , \ldots , ( t _ { i } , \pmb { a } _ { i } )
$$

to approximate $\pmb { a }$ and to evaluate the integral. This yields the Stoermer formula

$$
\pmb { r } _ { i + 1 } = 2 \pmb { r } _ { i } - \pmb { r } _ { i - 1 } + h ^ { 2 } \sum _ { j = 0 } ^ { m - 1 } \delta _ { j } \nabla ^ { j } \pmb { a } _ { i }
$$

with coefficients given by

$$
\delta _ { j } = ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } ( 1 - s ) \left[ { \binom { - s } { j } } + { \binom { s } { j } } \right] d s ~ .
$$

They are easily obtained from the coefficients $\gamma _ { j } ^ { * }$ of the implicit Adams method (see Table 4.6) via the relation

$$
\delta _ { j } = ( 1 - j ) \gamma _ { j } ^ { \ast } ~ .
$$

Numerical values for $j \le 8$ are given in Table 4.8.

The use of the Stoermer formula requires the knowledge of two position vectors $r _ { i - 1 } , \ldots , r _ { i }$ and $m$ accelerations $\pmb { a } _ { i - m + 1 } , \ldots , \pmb { a } _ { i }$ . These initial values may be obtained from a special starting procedure (see e.g. Schubart & Stumpff 1966) or a Runge–Kutta method.

The explicit Stoermer method may be supplemented by the implicit Cowell method

$$
\pmb { r } _ { i + 1 } = 2 \pmb { r } _ { i } - \pmb { r } _ { i - 1 } + h ^ { 2 } \sum _ { j = 0 } ^ { m - 1 } \delta _ { j } ^ { * } \nabla ^ { j } \pmb { a } _ { i + 1 }
$$

as corrector. The coefficients $\delta _ { j } ^ { * }$ are given in Table 4.8 up to order 8. Further values follow from the simple relation

$$
\delta _ { j } ^ { * } = \delta _ { j } - \delta _ { j - 1 } \quad .
$$

# 4.2.7 Gauss–Jackson or Second Sum Methods

The Gauss–Jackson or second sum methods (Jackson 1924, Merson 1974) are slightly modified versions of the Stoermer–Cowell methods for second-order differential equations and probably the most recommendable fixed-stepsize multistep methods for orbit computations. The explicit Stoermer formula is replaced by the equation

$$
\pmb { r } _ { i + 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { m + 1 } \delta _ { j } \nabla ^ { j - 2 } \pmb { a } _ { i }
$$

and the modified Cowell formula is given by

$$
r _ { i + 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { m + 1 } \delta _ { j } ^ { * } \nabla ^ { j - 2 } { \pmb a } _ { i + 1 } \quad .
$$

Velocities at each step may be obtained from similar equations that follow from the Adams–Bashforth–Moulton formulas:

$$
{ \pmb v } _ { i + 1 } = h \sum _ { j = 0 } ^ { m } \gamma _ { j } \nabla ^ { j - 1 } { \pmb a } _ { i }
$$

and

$$
\pmb { v } _ { i + 1 } = h \sum _ { j = 0 } ^ { m } \gamma _ { j } ^ { * } \nabla ^ { j - 1 } \pmb { a } _ { i + 1 } \quad .
$$

The coefficients $\gamma _ { j } , \gamma _ { j } ^ { * } , \delta _ { j }$ and ${ \delta } _ { j } ^ { * }$ are listed in Tables 4.4, 4.6 and 4.8.

The expressions for $r _ { i + 1 }$ and $v _ { i + 1 }$ involve the use of first and second sums $( \nabla ^ { - 1 } , \nabla ^ { - 2 } )$ , which are generalizations of the backwards differences introduced earlier. They are implicitly defined by the recursions

$$
\begin{array} { r l r } { \pmb { a } _ { i } } & { = } & { \nabla ^ { - 1 } \pmb { a } _ { i } - \nabla ^ { - 1 } \pmb { a } _ { i - 1 } } \\ { \nabla ^ { - 1 } \pmb { a } _ { i } } & { = } & { \nabla ^ { - 2 } \pmb { a } _ { i } - \nabla ^ { - 2 } \pmb { a } _ { i - 1 } } \end{array}
$$

in close analogy with definition (4.53). By applying the backward difference operator $\nabla$ twice to the explicit second sum formula (4.93) for $r _ { i + 1 }$ , one obtains

$$
\pmb { r } _ { i + 1 } - 2 \pmb { r } _ { i } + \pmb { r } _ { i - 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { m - 1 } \delta _ { j } \nabla ^ { j } \pmb { a } _ { i }
$$

which is just equation (4.88) of the Stoermer method. In a similar manner one may prove the validity of the implict second sum formulas as well as the first sum formulas for the prediction of $\pmb { v }$ .

Despite the apparent equivalence of the Bashforth–Moulton and Stoermer-Cowell formulas and the first and second sum formulas, the latter are generally preferred in practical computations. According to Henrici (1962) and Herrick (1971,

1972) the sum formulas are less influenced by round-off errors that result from the finite computing accuracy. This is especially important in long-term integrations where round-off errors are the main source of error, since the local truncation error can always be limited by choosing a high-order method and/or a small stepsize.

In order to use the summed version of the Stoermer–Cowell formulas one has to determine initial values of the first and second sums in addition to the initial set of backward differences. For starting the calculation it is assumed that one knows the position and velocity $( r _ { j } , \pmb { v } _ { j } )$ of the satellite for a given set of $m$ equidistant times $t _ { j } = \mathrm { \Delta } t _ { 0 } + \mathrm { \Delta } j h$ $( j = - m + 1 , \ldots , 0 )$ . These data can always be obtained from the initial values $( t _ { 0 } , r _ { 0 } , v _ { 0 } )$ by a backwards integration with a high-order Runge– Kutta method or an extrapolation method. From position and velocity one is able to calculate the accelerations ${ \pmb { a } } _ { j }$ and the backward differences $\nabla \pmb { a } _ { 0 } \ldots \nabla ^ { m - 1 } \pmb { a } _ { 0 }$ . The desired values of the first and second sums can now be determined by solving the implicit Adams–Moulton and Cowell formulas for $\nabla ^ { - 1 } \pmb { a } _ { 0 }$ and $\nabla ^ { - 2 } \pmb { a } _ { 0 }$ :

$$
\nabla ^ { - 1 } a _ { 0 } = \frac { v _ { 0 } } { h } - \sum _ { j = 1 } ^ { m } \gamma _ { j } ^ { * } \nabla ^ { j - 1 } a _ { 0 } \qquad \nabla ^ { - 2 } a _ { 0 } = \frac { r _ { 0 } } { h ^ { 2 } } - \sum _ { j = 1 } ^ { m + 1 } \delta _ { j } ^ { * } \nabla ^ { j - 2 } a _ { 0 } \quad .
$$

As an alternative to using a single-step method for obtaining the initial set of accelerations and backward differences one may use a special starting calculation. It involves an iterative refinement of a crude approximation of the satellite’s coordinates and the corresponding difference table that may be based e.g. on the assumption of an unperturbed Keplerian orbit. For a detailed description of this method the reader is referred to Herrick (1971, 1972).

# 4.2.8 Comparison of Multistep Methods

The relative performance of some of the multistep methods described so far is compared in Fig. 4.6. The test set covers a 6th-order Adams–Bashforth method (AB6), two Adams–Bashforth–Moulton methods of order 8 and 12 (ABM8, ABM12) and the variable order, variable stepsize code DE (Shampine & Gordon 1975), all of which may be used for integrating general first-order differential equations. In addition two high-order Stoermer and Stoermer–Cowell methods (S14, SC14) for the integration of second-order differential equations are included.

When considering fixed-order multistep methods the user must be careful to select a method of appropriate order for a given accuracy requirement. While loworder methods may be inefficient for high accuracies, the higher-order methods are subject to instability at low accuracies (i.e. at large stepsizes). As an example, the ABM12 method can only be used to integrate problem D1 with accuracies of better than 9 digits, whereas the ABM8 method becomes inefficient at just the same accuracy. These problems may be avoided, however, by using a variable order and stepsize method like DE, since the automatic order selection avoids an unstable behavior and, simultaneously, guarantees a high efficiency.

![](images/d007f1f49b7144ccc4c31d0dc84ba7fc9a87f2c8659f6febc14658f463a4ec8d.jpg)  
Fig. 4.6. Performance diagram of several multistep methods for test case D1 $\textstyle ( { \mathrm { e } } = 0 . 1 )$ of Hull et al. (1972). The number of function calls is plotted versus the relative accuracy in digits.

While the use of a corrector is essential for all but the lowest-order Adams methods, the same is not true for the Stoermer(–Cowell) methods, which are considerably more stable. Predictor methods of the Stoermer type have therefore been preferred by several authors (see e.g. Schubart & Stumpff (1966), Herrick (1971, 1972)) for applications in celestial mechanics, especially for long-term integrations of the solar system. Due to their high stability, Stoermer(–Cowell) methods may be used up to very high orders which makes them the most efficient methods of the test set.

# 4.3 Extrapolation Methods

The extrapolation method is a powerful single-step method that extends the idea of Richardson extrapolation (i.e. extrapolation to zero stepsize) to the numerical solution of ordinary differential equations. It is often called Bulirsch–Stoer or Gragg–Bulirsch–Stoer method in honor of the pioneering work of Gragg (1965) and Bulirsch & Stoer (1966). A general review of extrapolation methods may be found in Deuflhard (1985).

# 4.3.1 The Mid-Point Rule

In order to find the solution of a first-order differential equation at some time $t _ { 0 } { + } H$ from given initial values $( t _ { 0 } , y _ { \mathbf { 0 } } )$ , the interval $[ t _ { 0 } , t _ { 0 } + H ]$ is first subdivided into $n$ (micro-)steps of size $h = H / n$ . A simple Euler step is then used to find an approximation $\pmb { u } _ { 1 }$ at $t _ { 0 } { + } h$ , while further values $\pmb { u } _ { i }$ are obtained from the so-called mid-point rule:

$$
\begin{array} { l l l l l } { { { \pmb u } _ { 1 } } } & { { = } } & { { { \pmb y } _ { 0 } + h f ( t _ { 0 } , { \pmb y } _ { 0 } ) } } & { { } } & { { } } \\ { { { \pmb u } _ { i + 1 } } } & { { = } } & { { { \pmb u } _ { i - 1 } + 2 h f ( t _ { 0 } + i h , { \pmb u } _ { i } ) } } & { { ( i = 1 , \dots , n - 1 ) } } \end{array} \ .
$$

This yields an approximate solution

$$
\pmb { \eta } ( h ) = \frac { 1 } { 4 } \pmb { u } _ { n - 2 } + \frac { 1 } { 2 } \pmb { u } _ { n - 1 } + \frac { 1 } { 4 } \pmb { u } _ { n } \approx \pmb { y } ( t _ { 0 } + H )
$$

at $t _ { 0 } { + } H$ which may be considered a function of the stepsize $h$ .

According to Gragg (1965) the difference between $\pmb { \eta } ( h )$ and the exact solution may be described by an asymptotic expansion

$$
\eta ( h ) - y ( t _ { 0 } + H ) = \varepsilon _ { 2 } h ^ { 2 } + \varepsilon _ { 4 } h ^ { 4 } + \varepsilon _ { 6 } h ^ { 6 } + \dots
$$

in $h ^ { 2 }$ for sufficiently smooth functions and even values of $n$ . The error coefficients $\varepsilon _ { j }$ depend on $t _ { 0 }$ and $H$ but are independent of $h$ .

# 4.3.2 Extrapolation

As may be expected from the simple formulas used for the micro-steps, the order of the approximation is quite low. However, one may improve it considerably after repeating the integration with a different stepsize $h ^ { \prime }$ . Forming

$$
\eta ^ { * } = { \frac { { h ^ { \prime } } ^ { 2 } \eta ( h ) - h ^ { 2 } \eta ( h ^ { \prime } ) } { { h ^ { \prime } } ^ { 2 } - { h } ^ { 2 } } } = y ( t _ { 0 } + H ) + \varepsilon _ { 4 } O ( { h ^ { 2 } { h ^ { \prime } } ^ { 2 } } ) \quad ,
$$

one can eliminate the leading error term $\varepsilon _ { 2 } h ^ { 2 }$ and thus reduce the error by two orders.

![](images/8611a33d90a05baff6834908b9a80f640ee8a3c3f0f19908bf50a7d5409f8b76.jpg)  
Fig. 4.7. Extrapolation of $\eta ( h )$ for $h \to 0$ .

Equation (4.103) describes a linear extrapolation of $\pmb { \eta }$ as a function of $h ^ { 2 }$ down to $h = 0$ and it is obvious that even better approximations may be obtained by using higher-order extrapolation formulas (see Fig. 4.7). This requires that the mid-point rule integration from $t _ { 0 }$ to $t _ { 0 } + H$ is repeated several times with different stepsizes $h _ { i } = H / n _ { i }$ , where the $n _ { i }$ are taken from a sequence like

$$
n = 2 , 4 , 6 , 8 , 1 2 , 1 6 , 2 4 , 3 2 , 4 8 \ldots \quad ( n _ { i } = 2 n _ { i - 2 } \mathrm { f o r } i \geq 4 )
$$

which is called the Bulirsch sequence. The extrapolation is then performed according to the following scheme:

$$
\begin{array} { c c c c c c c c c c c c c c c c c } { { \eta ( h _ { 1 } ) } } & { { = } } & { { \eta _ { 1 , 1 } } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \times } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \eta ( h _ { 2 } ) } } & { { = } } & { { \eta _ { 2 , 1 } } } & { {  } } & { { \eta _ { 2 , 2 } } } & { { \searrow } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \times } } & { { } } & { { \times } } & { { } } & { { } } & { { \times } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \eta ( h _ { 3 } ) } } & { { = } } & { { \eta _ { 3 , 1 } } } & { {  } } & { { \eta _ { 3 , 2 } } } & { {  } } & { { \eta _ { 3 , 3 } } } & { { \lnot } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \times } } & { { } } & { { \times } } & { { } } & { { \times } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \eta ( h _ { 4 } ) } } &  { = }  \end{array}
$$

When using polynomial extrapolation3 each entry of the table is a simple linear combination

$$
\eta _ { i , j + 1 } = \frac { h _ { i - j } ^ { 2 } \eta _ { i , j } - h _ { i } ^ { 2 } \eta _ { i - 1 , j } } { h _ { i - j } ^ { 2 } - h _ { i } ^ { 2 } } = \eta _ { i , j } + \frac { \eta _ { i , j } - \eta _ { i - 1 , j } } { ( n _ { i } / n _ { i - j } ) ^ { 2 } - 1 }
$$

of the entries to the left and upper left of it.

From the asymptotic expansion of the error and $\varepsilon _ { 2 j } = O ( H )$ one obtains the following estimate:

$$
e _ { i , j } = | { \bf y } ( t _ { 0 } { + } H ) { - } \eta _ { i , j } | = \varepsilon _ { 2 j } O ( h _ { i } ^ { 2 } { \cdot } h _ { i - 1 } ^ { 2 } { \cdot } . . . . h _ { i - j + 1 } ^ { 2 } ) = O ( H ^ { 2 j + 1 } ) ~ .
$$

This means that each value $\eta _ { i j }$ in column $j$ of the extrapolation table provides an approximation comparable to that of a Runge–Kutta method of order $2 j$ . Since the number of columns may be quite high (e.g. 7–10), the extrapolation method exceeds any known Runge–Kutta method with respect to the attainable order and is therefore often considered the best method for very high accuracy requirements.

The stepsize control of the extrapolation method may be based on the same consideration that led to (4.21) for embedded Runge–Kutta methods. For a given size of the extrapolation table one can estimate the truncation error from the difference of two neighboring values $\eta _ { j , j - 1 }$ and $\eta _ { j , j }$ and calculate a new stepsize from

$$
H ^ { * } = 0 . 9 H \cdot \sqrt [ 2 j - 1 ] { \frac { \varepsilon } { | \eta _ { j , j } - \eta _ { j , j - 1 } | } } ,
$$

where 0.9 is a safety factor that avoids an overoptimistic stepsize estimate and $\varepsilon$ is the required tolerance. Simultaneously one may check whether the order of the extrapolation table should be changed to decrease the total integration effort. For details of the stepsize control used in practical implementations of the extrapolation method the reader is referred to Hussels (1973), Deuflhard (1983) and Hairer et al. (1987).

![](images/879847bcc53511e43c2e858705aff17320f18ab60144bf1c3fe1061a93be6843.jpg)  
Fig. 4.8. Performance diagram of several extrapolation methods for test case D1 $\mathrm { ( e { = } 0 . 1 ) }$ of Hull et al. (1972). The number of function calls is plotted versus the relative accuracy in digits. Note the jump in the graph for DIFSY1 that is caused by the stepsize and order control

# 4.3.3 Comparison of Extrapolation Methods

Implementations of the extrapolation method have been published by various authors. They differ mainly in the choice of polynomial or rational extrapolation, the set of micro-stepsizes and the stepsize and order control:

• DIFSY1, DIFSY2: Extrapolation methods using rational instead of polynomial extrapolation (Bulirsch & Stoer 1966). The initial stepsize control has been improved by Hussels (1973). DIFSY2 has been developed by Hussels (1973) for special second-order differential equations $\ddot { \mathbf { y } } = f ( t , \mathbf { y } )$ that do not depend on first-order derivatives. For this purpose the mid-point rule is replaced by the lowest-order Stoermer formula $( \pmb { y } _ { i + 1 } = 2 \pmb { y } _ { i } - \pmb { y } _ { i - 1 } + h ^ { 2 } \pmb { f } _ { i } )$ . Compared to DIFSY1, computing times may be reduced considerably by using DIFSY2 whenever appropriate.   
• DIFEX1, DIFEX2: Extrapolation codes for first and second-order differential equations with a new kind of order and stepsize control developed by Deuflhard (1983). The Bulirsch sequence (4.104) is replaced by the harmonic sequence $( n = 2 , 4 , 6 , 8 , 1 0 , 1 2 , 1 4 , . . . )$ .

ODEX1, ODEX2: Implementations of the extrapolation method described in Hairer et al. (1987). ODEX2 – like DIFSY2 – is intended for use with second-order differential equations.

As with the Runge–Kutta methods (see Fig. 4.2), test problem D1 of Hull et. al. (1972) is used to compare the performance of some of these extrapolation codes (Fig. 4.8). The high order of the extrapolation methods is evident from the fact that even a small increase in the number of function evaluations leads to a considerable increase of the number of accurate digits. Within the set of first-order methods (DIFSY1, DIFEX1, ODEX1) performance differences of about $20 \%$ are observed in agreement with Hairer et al. (1987). The use of DIFEX2 and ODEX2 which have been developed for the direct integration of second-order differential equations increases the efficiency by about $3 0 { - } 5 0 \%$ . Concerning the order and stepsize control, the ODEX codes are notable for the smooth relation between function evaluations and accuracy in the performance diagram.

Since the effective order of extrapolation codes can be quite high, the integration is usually performed with large stepsizes. This may be pretty inefficient, if dense output is required. The situation is similar to that of high-order Runge–Kutta methods with the difference that an extrapolation method may be considered as a variable order method. If the maximum stepsize is limited by the requested output points, codes like DIFEX1 and ODEX therefore try to reduce the order as far as possible using only one column of the extrapolation table, if necessary. Even though the costs per integration step are reduced to a minimum in this way, the total integration effort may still be quite high. As a possible solution to this problem Shampine et al. (1982) have constructed a low-order interpolating Runge–Kutta formula based on the function evaluations that are required for the first entries of the extrapolation table. An interpolation algorithm that preserves the high order of extrapolation codes has only recently been developed by Hairer & Ostermann (1990) for first-order differential equations, but has not yet been tested for use in high-precision ephemeris calculations.

# 4.4 Comparison

In the preceding sections the basic concepts and features of Runge–Kutta, multistep, and extrapolation methods for the integration of ordinary differential equations have been discussed. Regarding the class of Runge–Kutta methods, it has been shown that only high-order methods are reasonable candidates for the accuracy requirements of orbit computations. FILG11 and RKN12(10) were identified as the most efficient methods, but if the acceleration involves velocity dependent terms, DOPRI8 will serve best. Among the extrapolation codes ODEX2 is most promising, being about $40 \%$ faster than the corresponding codes for first-order differential equations. As expected, an excellent performance is also found for all multistep methods.

The sample calculations presented so far have been restricted to near-circular orbits, however, and in order to extend the discussion to more general orbits, highly eccentric orbits $e = 0 . 9$ ; test case D5 of Hull et al. (1972)) have been considered, too. In addition to DOPRI8, FILG11, and ODEX2 the variable order, variable stepsize multistep code DE/DEABM is used for this comparison.

As before, the valuation of the different integration methods is based on a performance diagram showing the relation between the number of function evaluations and the achieved accuracy. This approach avoids the measurement of machinedependent computing times but some comments may be helpful to illustrate its validity.

The total computing effort of a numerical integration method depends not only on the number of function evaluations but also on the extent of additional arithmetic operations that are required inside the integration routine. In the case of the two-body problem the total computing time is, for example, about $30 \mathrm { - } 6 0 \%$ higher than expected from the number of function evaluations alone, if one uses a Runge–Kutta or Extrapolation method. For variable-order and stepsize multistep methods which require a lot of work to calculate new coefficients at each step, this computational overhead is even higher and may well be in the order of $200 \%$ . The situation changes, however, if one considers a realistic force model that is appropriate for the prediction of satellite orbits. While the additional perturbations do not affect the number of function evaluations, they increase the total computing time considerably and make the integration overhead more or less negligible. As an example we found values between $5 \%$ (single-step methods) and $20 \%$ (variableorder and stepsize multistep methods) for a satellite force model including a $3 \times 3$ geopotential, lunisolar gravitational attraction, and solar radiation pressure.

The number of function evaluations that are required to achieve a given accuracy is, therefore, an appropriate performance measure for our purposes and we may now turn to Fig. 4.9 which presents the results for the various integration methods under consideration. First of all it is evident that the total integration effort for a highly eccentric orbit is larger by a factor of about 3–4 than that for a near-circular orbit. Since this factor is almost the same for all methods, it can be concluded that the stepsize control of all codes works well even for orbits of high eccentricity. While the good performance of the multistep methods at low eccentricities is beyond doubt, it is noteworthy that DE is well suited for very high eccentricities, too. This clearly indicates the usefulness of variable-order and stepsize multistep methods for application to general types of orbits. A regularization of the equations of motion (see e.g. Long et al. 1989), which is essential for an efficient use of simple fixedstepsize multistep methods at high eccentricities, can thus be avoided completely.

![](images/edd2dfca2c91b40e0319f40fa42b32ca7b9ea9e9c4abad813cc0b94a455e0cf5.jpg)  
Fig. 4.9. Performance diagram of several single- and multistep methods for test cases D1 $e { = } 0 . 1$ , lower set of curves) and D5 $e { = } 0 . 9$ , upper set of curves) of Hull et al. (1972). The number of function calls is plotted versus the relative accuracy in digits.

A comparison of single-step methods with multistep methods indicates that both classes of integration methods have become almost competitive by now. While the 8th-order code DOPRI8 needs still 2–2.5 times the computing effort required by DE, one may note that the 11th-order Nyström method FILG11 is even more efficient than the multistep method for both low and high eccentricities. An excellent performance is also found for the ODEX2 code, which shows that all types of singlestep methods are well worth considering for applications in the field of orbital mechanics.

This result is somewhat in contrast to the common opinion that the use of a multistep method is an indispensable prerequisite for an efficient numerical integration of satellite orbits due to the small number of function evaluations required. While there is strong support for this point of view in earlier reviews (Moore 1974, Fox 1984) one should keep in mind that the technique of Runge–Kutta integration has been improved considerably within the past two decades and that new high-order methods like FILG11 are much more efficient than their predecessors. Fox (1984), for example, recommends the Gauss–Jackson method (without corrector step) for near-circular orbits, since he finds it superior to the 8th-order Runge–Kutta method DOPRI8 by a factor of about 3. This result is in close agreement with our comparison of DOPRI8 and the multistep method DE/DEABM and Fox’s conclusions can be supported as long as methods for general first or second-order differential equations are considered. If the equation of motion does not contain any velocity dependent term, however, then high-order Runge–Kutta–Nyström codes like FILG11 or RKN12(10) may be used which are even faster than multistep methods like DE or VOAS.

The good performance of Runge–Kutta and extrapolation methods exhibited in the sample calculations should not, however, obscure the fact that the efficiency of these method deteriorates considerably when the distance between subsequent output points becomes smaller than the natural stepsize. This situation might change with the development of interpolants for high-order Runge–Kutta methods, but up to now single-step methods can only be recommended, if less than 50 to 100 output points per revolution are required. Multistep methods are still, therefore, preferable for the generation of equidistant ephemerides at small time intervals. With the availability of variable-order and stepsize codes these methods are no longer restricted to near-circular orbits, but may also be used for high eccentricities without any precautions. Due to this increased flexibility, variable-order and stepsize multistep methods are ideal candidates for use in general satellite orbit prediction and determination systems. Nevertheless, fixed stepsize codes that have been favored in software packages like GTDS (Long et al. 1989), GEODYN (Martin et al. 1976), UTOPIA (Schutz & Tapley, 1980), and PEPSOC (Soop 1983) are useful for an efficient treatment of near-circular orbits like those of geodetic or geostationary satellites.

# Exercises

Exercise 4.1 (4th-Order Runge–Kutta Method) Apply the 4th-order Runge– Kutta method (cf. Sect. 4.1.1) to integrate the normalized two-body problem from $t _ { 0 } = 0$ to $t = 2 0$ for an eccentricity of $e = 0 . 1$ (test problem D1, cf. Sect. 4.1.6). Determine the resulting accuracy of the state vector at the end point using $n =$ {50, 100, 250, 500, 750, 1000, 1500, 2000} steps and count the corresponding number of function evaluations.

Solution: Reference values obtained with IEEE 8-byte floating point arithmetics (double precision) are given below:

<table><tr><td>nfnc 200</td><td>Accuracy 1.953-10-1</td><td>Digits 0.71</td></tr><tr><td>400</td><td>6.663.10-3</td><td>2.18</td></tr><tr><td>1000</td><td>9.051.10-5</td><td>4.04</td></tr><tr><td>2000</td><td>4.012.10-6</td><td>5.40</td></tr><tr><td>3000</td><td>6.847.10-7</td><td>6.16</td></tr><tr><td>4000</td><td>1.996.10-7</td><td>6.70</td></tr><tr><td>6000</td><td>3.608.10-8</td><td>7.44</td></tr><tr><td>8000</td><td>1.089.10-8</td><td>7.96</td></tr></table>

Exercise 4.2 (4th-Order Gauss–Jackson Method) Implement the 4th-order Gauss–Jackson method (cf. Sect. 4.2.7) and integrate the second-order differential equation $\ddot { r } = - r / r ^ { 3 }$ of the normalized two-body problem from $t _ { 0 } = 0$ to $t ~ = ~ 2 0$ for an eccentricity of $e \mathrm { ~ = ~ } 0 . 1$ (Test problem D1, cf. Sect. 4.1.6). Determine the resulting accuracy of the state vector at the end point using $n \_ =$ 100, 300, 600, 1000, 1500, 2000, 3000, 4000 steps and count the corresponding number of function evaluations.

Hint: Apply the 4th-order Runge–Kutta method to compute position and velocity at times $t _ { 0 } - h , t _ { 0 } - 2 h$ and $t _ { 0 } - 3 h$ from the intial values $r _ { 0 }$ and ${ \pmb v } _ { 0 }$ . The corresponding accelerations ${ \pmb a } _ { 0 } , \dots , { \pmb a } _ { - 3 }$ can then be used to form the backwards differences $\nabla ^ { 0 } { \pmb a } _ { 0 } , \dots , \nabla ^ { 3 } { \pmb a } _ { 0 }$ and to initialize the sums

$$
\begin{array} { l l l } { { \nabla ^ { - 1 } a _ { 0 } } } & { { = } } & { { \displaystyle \frac { v _ { 0 } } { h } - \left( - \frac { 1 } { 2 } \nabla ^ { 0 } a _ { 0 } - \frac { 1 } { 1 2 } \nabla ^ { 1 } a _ { 0 } - \frac { 1 } { 2 4 } \nabla ^ { 2 } a _ { 0 } - \frac { 1 9 } { 7 2 0 } \nabla ^ { 3 } a _ { 0 } \right) } } \\ { { \nabla ^ { - 2 } a _ { 0 } } } & { { = } } & { { \displaystyle \frac { r _ { 0 } } { h ^ { 2 } } - \left( - \nabla ^ { - 1 } a _ { 0 } + \frac { 1 } { 1 2 } \nabla ^ { 0 } a _ { 0 } - \frac { 1 } { 2 4 0 } \nabla ^ { 2 } a _ { 0 } - \frac { 1 } { 2 4 0 } \nabla ^ { 3 } a _ { 0 } \right) } } \end{array}
$$

at the starting point $t _ { 0 }$

Solution: Reference values obtained with IEEE 8-byte floating-point arithmetics (double precision) are given below:

<table><tr><td>nfnc</td><td>Accuracy 2.456.10-03</td><td>Digits</td></tr><tr><td>116</td><td></td><td rowspan="3">2.61 5.47</td></tr><tr><td>316</td><td>3.363.10-06</td></tr><tr><td>616</td><td>7.705:10-08</td></tr><tr><td>1016</td><td>4.539.10-09</td><td>7.11 8.34</td></tr><tr><td>1516</td><td>5.174-10-10</td><td>9.29</td></tr><tr><td>2016</td><td>1.166.10-10</td><td>9.93</td></tr><tr><td>3016</td><td>1.499.10-11</td><td>10.82</td></tr><tr><td>4016</td><td>3.577.10-12</td><td>11.45</td></tr></table>

Exercise 4.3 (Stepsize Control for Eccentric Orbits) Integrate the normalized two-body problem with eccentricity $e = 0 . 9$ from $t _ { 0 } = 0$ to $t = 2 0$ (test problem D5, cf. Sect. 4.1.6) using the DE multistep method of Shampine & Gordon (1975) and monitor the step size variation as a function of time and distance.

Solution: Using double-precision arithmetics and a value of $\varepsilon _ { \mathrm { a b s } } = 1 0 ^ { - 8 }$ for the error control parameter of the DE method, the results shown in Fig. 4.10 are obtained.

![](images/dbc4b1f4b268c391b8f39c54a217f182bc1fa621eba17778a130367d722faa2d.jpg)  
Fig. 4.10. Stepsize variation of DE multistep method during integration of normalized two-body problem with eccentricity $e = 0 . 9$ .

Following an infinitesimal initial step, the order and stepsize of the DE multistep method are continuously increased, until a typical order of ten is achieved. During the integration small steps are chosen close to pericenter, where the orbital position changes rapidly. Near apocenter, in contrast, the slow motion allows for much larger steps. It may be observed that the stepsize varies roughly as the square of the distance from the center, and is thus almost proportional to the inverse of the central acceleration. In total the stepsize varies by two orders of magnitude during one orbit.

# 5. Time and Reference Systems

The physical and numerical models presented so far have tacitly assumed the availability of a unique time and reference system for the equation of motion. In practice, however, one faces a multitude of historically grown concepts and definitions, which are employed along with each other. Whereas the definition of both time and the fundamental reference systems has traditionally been based on the rotational and translational motion of the Earth, one has now advanced to ideally uniform atomic time scales and an ideally non-rotating quasar-tied celestial reference frame. Nevertheless, a thorough understanding of the Earth’s motion and rotation remains essential for a rigorous description of satellite orbits and even more the accurate modeling of ground based measurements.

# 5.1 Time

Despite the apparent familiarity and its use in everyday life, time has remained an issue that requires careful attention in the description of astronomical, physical, and geodetic phemomena. In accordance with the advance of physical theories, observational methods, and measuring devices, the underlying concepts and definitions have undergone continued revisions and refinements up to the present date.

Time is traditionally measured in days of 86 400 seconds duration, where the length of the solar day is determined from subsequent meridian transits of the Sun. Because of the orbital motion of the Earth around the Sun, the Sun’s right ascension changes by approximately one degree per day and the solar day is thus about 4 minutes longer than the period of the Earth’s rotation. The latter time interval, which is also known as a sidereal day, amounts to $2 3 ^ { \mathrm { h } } 5 6 ^ { \mathrm { m } } 4 . 1$ (solar time) and is equal to time between successive meridian passages of the vernal equinox.

In view of the eccentricity of the Earth’s orbit and the resulting seasonal variations of the Sun’s apparent motion, the real Sun is not, however, well suited for time reckoning purposes. Instead it had to be replaced by the concept of a mean Sun, that moves uniformly in right ascension at a rate determined from observations and analytical ephemerides. Based on a conventional expression for the right ascension of the mean Sun that was derived from Newcomb’s Tables of the Motion of the Earth, the Greenwich Mean Time GMT or Universal Time UT was established in 1925 as an international time scale for astronomical and civil purposes.

When imperfections in the UT time scale became apparent that are due to irregularities and secular variations in the Earth’s rotation, it was decided to establish a new time scale in 1960 that was based exclusively on the orbital motion of solar system bodies. This time scale, known as Ephemeris Time ET, defined time as the independent argument of planetary and lunar ephemerides. Based on this definition ET could be determined by comparing observed positions of the Sun, the planets, or the Earth’s Moon with tabulated data predicted from analytical or numerical theories of motion. Ephemeris Time is thus the prototype of a dynamical time scale, which considers time as a continuously and uniformly passing physical quantity in the dynamical theories of motion.

With the advent of atomic clocks Atomic Time was introduced as a new timing system that was more easily accessible by laboratory standards and free from deficiencies of dynamical models. More recently a set of time scales has been defined that accounts for the effects of general relativity in the framework of a four-dimensional space-time.

Today the following time scales are of prime relevance in the precision modeling of Earth orbiting satellites:

Terrestrial Time $( T T )$ , a conceptually uniform time scale that would be measured by an ideal clock on the surface of the geoid. TT is measured in days of $8 6 4 0 0 \mathrm { S I } ^ { 1 }$ seconds and is used as the independent argument of geocentric ephemerides.   
International Atomic Time (TAI), which provides the practical realization of a uniform time scale based on atomic clocks and agrees with TT except for a constant offset of 32.184 s and the imperfections of existing clocks. GPS Time, which like TAI is an atomic time scale but differs in the chosen offset and the choice of atomic clocks used in its realization.   
Greenwich Mean Sidereal Time (GMST), the Greenwich hour angle of the vernal equinox.   
• Universal Time (UT1), today’s realization of a mean solar time, which is derived from GMST by a conventional relation.   
Coordinated Universal Time (UTC), which is tied to the International Atomic Time TAI by an offset of integer seconds that is regularly updated to keep UTC in close agreement with UT1.

For a description of planetary and lunar motion as well as solar system events within a general relativistic context, the above time scales are further supplemented by Geocentric and Barycentric Coordinate Time (TCG and TCB) as well as Dynamical Barycentric Time (TDB).

The mutual relation of the above time scales and their historical evolution is outlined in Fig. 5.1. Here distinction is made between dynamical time scales that serve as independent argument in the equations of motion, atomic time scales that provide the practical realization of a uniform clock, and the non-uniform solar time scales that are tied to the motion of the Sun and the rotation of the Earth.

![](images/47fd736bdc00b7570c676f6130ce865f5a8a05be5ff26de2541804147bbf5a04.jpg)  
Fig. 5.1. Evolution of conventional time scales

# 5.1.1 Ephemeris Time

Ephemeris Time was adopted in $1 9 6 0 ^ { 2 }$ to cope with irregularities in the Earth’s rotation that had been found to affect the flow of mean solar time. Even though its definition is based on Newtonian physics and has meanwhile been replaced by TT, TCG, and TCB within a relativistic framework, Ephemeris Time still represents the prototype of a dynamical time scale and provides a useful link to historical planetary observations.

The definition of Ephemeris Time is based on Newcomb’s analytical theory of the Earth’s motion around the Sun (Newcomb 1898). In his analytical solution of the equations of motion, Newcomb expressed the relative motion of the Earth-Moon barycenter and the Sun by a set of secularly perturbed Keplerian elements and superimposed periodic perturbations. Based on his theory and an adjustment to obervations, he derived the expression

$$
L _ { \odot } = 2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 ^ { \prime \prime } 0 4 + 1 2 9 6 0 2 7 6 8 ^ { \prime \prime } 1 3 \cdot T + 1 _ { \cdot } ^ { \prime \prime } 0 8 9 \cdot T ^ { 2 }
$$

for the geometric mean longitude of the Sun with respect to the Earth-Moon barycenter. Here $L _ { \odot }$ refers to the mean equinox of date while $T$ measures time from noon 1900 January 0 (JD 2 415 020.0) GMT in Julian centuries of 36525 days.

While a day was originally meant to represent a mean solar day in Newcomb’s computations, the above relation was later adopted as a conventional expression in the definition of Ephemeris Time. To this end, the instant at which the geometric mean longitude of the Sun had a value of $2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . ^ { \prime \prime } 0 4$ near the beginning of the calendar year AD 1900 was defined as 1900 January 0, $1 2 ^ { \mathrm { h } }$ Ephemeris Time (ET). The rate of change $d L _ { \odot } / d T$ at this epoch is given by the linear term in (5.1), which corresponds to an orbital period of

$$
P = { \frac { 3 6 0 \cdot 3 6 0 0 ^ { \prime \prime } } { 1 2 9 6 0 2 7 6 8 ^ { \prime \prime } 1 3 } } \cdot 3 6 5 2 5 \cdot 8 6 4 0 0 \thinspace \mathrm { s } = 3 1 ~ 5 5 6 9 2 5 . 9 7 4 7 \thinspace \mathrm { s } ~ .
$$

Accordingly, the ephemeris second was defined as the fraction 1/31556925.9747 of the tropical year at 1900 January $0 . 5 \mathrm { E T }$ , where a tropical year specifies the time during which the Sun’s mean longitude, as referred to the mean equinox of date, increases by $3 6 0 ^ { \circ }$ .

Even though Ephemeris Time provides a conceptually smooth and uniform time scale it is more difficult to measure than mean solar time that is closely related to the Earth’s rotation. In practice Ephemeris Time has to be determined by comparing observations of the Sun, Moon or planets with precomputed ephemerides. Among these bodies the Moon exhibits the fastest orbital motion and has therefore formed the basis for the actual implementation of Ephemeris Time. Soon, however, Ephemeris Time became superseded by the use of atomic time scales, which provided a much better short-term availability together with an excellent long-term stability.

# 5.1.2 Atomic Time

Atomic (or molecular) clocks are based on the periodic oscillation of a microwave signal that is in resonance with a low-energy state transition of a specific atom or molecule. While the first clock built at the National Bureau of Standards in 1948 used an ammonia $\mathrm { ( N H } _ { 3 } )$ absorption line to control the frequency generation (Forman 1985), today’s atomic clocks are generally based on cesium $\big ( { } ^ { 1 \bar { 3 } 3 } \mathrm { C s } \big )$ , hydrogen $( ^ { 1 } \mathrm { H } )$ , or rubidium $( ^ { 8 7 } \mathrm { R b } )$ (McCoubrey 1996). Among these types, cesium clocks provide the best long-term stability and are therefore used as primary standards in the practical realization of atomic time scales.

The principle of a cesium-beam atomic clock is illustrated in Fig. 5.2. A beam of cesium-133 atoms leaves an oven through a thin hole and enters the inhomogenous field of a Stern–Gerlach magnet. It then passes through a microwave resonator and a second magnet before it is finally collected by a detector (cf. Vessot 1974).

![](images/bd278de061638e17b3cc968f39cea9986401faad222ec7ee11fe5a44b8434c27.jpg)  
Fig. 5.2. Schematic view of a cesium-beam atomic clock

Depending on the nucleus and outer electron spins, the cesium atoms exhibit a total angular momentum of either $F = 3$ or $F = 4$ . Both states are separated by a small energy of about $0 . 0 4 \mathrm { m e V }$ and are almost equally populated in thermal equilibrium. Atoms in the $F = 3$ state experience an acceleration along the gradient of an external magnetic field, while atoms in the $F = 4$ state are deflected into the opposite direction. The first Stern–Gerlach magnet thus acts as a state selector, which allows only atoms in the $F = 3$ state to enter the subsequent microwave resonator. Here the beam passes through an electromagnetic field with a nominal frequency of $9 1 9 2 6 3 1 7 7 0 \mathrm { H z }$ , which corresponds to the energy difference between the two states. Accordingly, atoms in the $F = 3$ state may absorb a microwave photon and change the electron spin from anti-parallel to parallel orientation with respect to the spin of the nucleus. Upon leaving the resonator, the atoms pass a second Stern–Gerlach magnet (analyzer) that separates the $F = 3$ and $F = 4$ states and allows only the latter (i.e. those with modifed electron spin) to enter the detector. A maximum signal is thus obtained, if the microwave radiation frequency is properly centered to the hyperfine transition. The detector signal can, therefore, be used to adjust the resonator frequency to a fraction of the natural linewidth and obtain a highly stable frequency reference. Upon continued subdivision, lower frequencies of equal stability are obtained that ultimately provide the desired clock signal.

Due to the sharpness of the absorption line, the resonance frequency can be matched with great precision and is thus ideally suited as an accurate time reference.

Typical accuracies achieved with present cesium clocks range from $1 0 ^ { - 1 2 }$ to $1 0 ^ { - 1 4 }$ (Guinot 1989) with prospects for stabilities down to $1 0 ^ { - 1 6 }$ (Wolf & Petit 1995). This may be compared to a stability of the Earth’s rotation of about $1 0 ^ { - 8 }$ (0.3 s/year) and an accuracy of ephemeris time determination in the range of $1 0 ^ { - 1 0 }$ (0.05 s in 10 years).

In comparison with Ephemeris Time as derived from lunar observations, the cesium resonance frequency was determined as $9 1 9 2 6 3 1 7 7 0 \pm 2 0 \mathrm { H z }$ by Markowitz (1958). The numerical value was finally adopted in 1967 to independently define one second in the Système International (SI) as the duration of exactly 9 192 631 770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.

At the French Bureau International de l’Heure BIH atomic clocks were used as early as 1955 in addition to traditional astronomical time keeping procedures. In 1972, the BIH atomic time scale was adopted as a world-wide standard time under the name International Atomic Time TAI. The unit of time of TAI is defined as the SI second and the origin has arbitrarily been chosen such that TAI closely matches Universal Time on 1958 January 1.0, yielding the relation

$$
\mathrm { E T } = \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } ~ .
$$

Today TAI is established at the French Bureau International des Poids et Mesures BIPM using an elaborate stability algorithm and clock readings from a large number of atomic clocks (Guinot 1989).

In addition to TAI, the atomic time scale established by the Global Positioning Satellite (GPS) system has become of great significance in the past decade due to the common availability of GPS receivers. Besides serving the direct needs of geodetic and navigational measurements, GPS provides high-precision timing signals with a near-instantaneous and worldwide availability. GPS time is realized by an independent set of atomic clocks and is maintained to follow the United States Naval Observatory (USNO) atomic clock time with an accuracy of $1 \mu \mathrm { s }$ , which itself differs from TAI by less than $5 \mu \mathrm { s }$ . The origin of GPS time was arbitrarily chosen to coincide with UTC on 1980 January 6.0 UTC, i.e. GPS time differs from TAI by a constant offset of

$$
\mathrm { G P S } = \mathrm { T A I } - 1 9 \mathrm { s }
$$

aside from the aforementioned clock offsets on the micro-second level.

# 5.1.3 Relativistic Time Scales

While time is an absolute quantity in the context of Newtonian physics, which does not depend on the location and the motion of a clock, the same is no longer true in a general relativistic framework. Instead, different proper times apply for each clock, that are related to each other by a four-dimensional space-time transformation. This transformation requires knowledge of the space-time metric, which itself depends on the location and motion of the gravitating masses. Within the solar system, a first-order post-Newtonian approximation is generally adequate for a treatment of relativistic effects in view of moderate velocities and gravitational potentials (Soffel & Brumberg 1991).

In the vicinity of the Earth, it is possible to choose a rotation-free system of four-dimensional space-time coordinates $( x ^ { 0 } = c t , x = ( x ^ { 1 } , x ^ { 2 } , x ^ { 3 } ) )$ in such a way that the invariant space-time distance between two events is given by

$$
d s ^ { 2 } = - c ^ { 2 } d \tau ^ { 2 } = - \left( 1 - { \frac { 2 U } { c ^ { 2 } } } \right) ( d x ^ { 0 } ) ^ { 2 } + \left( 1 + { \frac { 2 U } { c ^ { 2 } } } \right) ( d x ) ^ { 2 }
$$

to lowest order. Here $c$ denotes the speed of light, $\tau$ is the proper time (as opposed to coordinate time $t$ ) and $U$ is the sum of the Earth’s gravitational potential and the tidal potential generated by external bodies. Eqn. (5.5) implies that the rate of a clock at rest on the surface of the Earth differs from the rate of coordinate time by a factor of

$$
\frac { d \tau } { d t } = \sqrt { 1 - \frac { 2 U } { c ^ { 2 } } - \frac { v ^ { 2 } } { c ^ { 2 } } } \approx 1 - \frac { G M _ { \oplus } } { R _ { \oplus } c ^ { 2 } } - \frac { v ^ { 2 } } { 2 c ^ { 2 } } \approx 1 - 7 . 1 0 ^ { - 1 0 } ,
$$

where $v \approx \omega _ { \oplus } R _ { \oplus } \cos \varphi$ is the clock’s speed in the non-rotating frame for a given latitude $\varphi$ . Likewise, clocks at different altitudes will have different proper times and experience a rate difference in long-term comparisons.

The conceptual difference between proper time and coordinate time has led the International Astronomical Union (IAU) to adopt two different time scales for use since 1992, which are named as Terrestrial Time $T T$ (formerly Terrestrial Dynamical Time TDT)3 and Geocentric Coordinate Time TCG. Terrestrial Time has as its unit the SI second as measured on the geoid and provides a smooth continuation of Ephemeris Time, i.e.

$$
\mathrm { T T } = \mathrm { T D T } = \mathrm { E T } = \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } \quad .
$$

Geocentric Coordinate Time TCG in contrast represents the time coordinate of a four-dimensional reference system and differs from TT by a constant scale factor $1 - L _ { \mathrm { G } }$ with

$$
L _ { \mathrm { G } } = 6 . 9 6 9 2 9 0 3 { \cdot } 1 0 ^ { - 1 0 }
$$

(Wolf & Petit 1995). By convention TCG agress with TT on 1977 January 1.0, yielding the relation

$$
\mathrm { T C G } = \mathrm { T T } + L _ { \mathrm { G } } \cdot ( \mathrm { J D } - 2 4 4 3 1 4 4 . 5 ) \cdot 8 6 4 0 0 \mathrm { s } \quad .
$$

Around the epoch J2000, the difference TCG–TT amount to roughly $0 . 5 \mathrm { s }$

Supplementary to TCG, the Barycentric Coordinate Time TCB has been introduced to describe the motion of solar-system objects in a non-rotating relativistic frame centered at the solar-system barycenter. Both time scales are defined to match each other on 1977 January 1.0 TAI but exhibit a rate difference

$$
\frac { d ( \mathrm { T C B } - \mathrm { T C G } ) } { d \mathrm { T C G } } \approx \frac { G M _ { \odot } } { a c ^ { 2 } } + \frac { v _ { \oplus } ^ { 2 } } { 2 c ^ { 2 } } \approx \frac { 3 } { 2 } \frac { G M _ { \odot } } { a c ^ { 2 } } \approx 1 . 5 { \cdot } 1 0 ^ { - 8 } ~ ,
$$

that depends on the gravitational potential of the Sun at the mean Earth-Sun distance $a = 1$ AU and the Earth’s orbital velocity $v _ { \oplus }$ . Due to the eccentricity of the Earth’s orbit and the associated variations of the heliocentric distance and velocity, the rigorous transformation involves additional periodic terms and is given by

$$
\mathrm { T C B } = \mathrm { T C G } + L _ { \mathrm { C } } \cdot ( \mathrm { J D } - 2 4 4 3 1 4 4 . 5 ) \cdot 8 6 4 0 0 \mathrm { s } + P
$$

with

$$
L _ { \mathrm { C } } = 1 . 4 8 0 8 2 6 8 4 5 7 cdot 1 0 ^ { - 8 }
$$

(McCarthy 1996) and

(Seidelmann & Fukushima 1992). The leading periodic term is of $1 . 7 \mathrm { m s }$ amplitude and varies with the sine of the Earth’s mean anomaly. All other terms are about two orders of magnitude smaller. In view of the significant rate difference between TCB and TCG/TT the accumulated TCB–TT time difference amounts to roughly 11 s around the epoch J2000 (cf. Fig. 5.3).

TCB supersedes a time scale known as Barycentric Dynamical Time TDB, which was introduced by the IAU in 1976 and defined to differ from TDT (now TT) by periodic terms, only. Accordingly TDB and TCB are related by

$$
\mathrm { T C B } = \mathrm { T D B } + L _ { \mathrm { B } } \cdot ( \mathrm { J D } - 2 4 4 3 1 4 4 . 5 ) \cdot 8 6 4 0 0 \mathrm { s } \quad ,
$$

where the scale difference

$$
L _ { \mathrm { B } } = L _ { \mathrm { C } } + L _ { \mathrm { G } } = 1 . 5 5 0 5 1 9 7 4 8 7 \cdot 1 0 ^ { - 8 }
$$

(McCarthy 1996) synchronizes the average rate of Barycentric Dynamical Time with that of Terrestrial (Dynamical) Time. While the definition of TDB appeared to be useful at first sight in view of the small amplitude of the TDB-TT time difference it has a subtle implication for models of solar system dynamics. While the post-Newtonian equations hold irrespective of the use of TCB or TDB time, the TDB second is longer than the TCB second by a factor $L _ { \mathrm { B } }$ . Furthermore, in order to maintain the adopted numerical value

![](images/711f58a1114622801f98b4fbf9f915aabd727e8e5e9835690bdbfa66ef7d36fe.jpg)  
Fig. 5.3. Difference of atomic, dynamical, and solar time scales between 1950 and 2020. Periodic terms in TCB and TDB have been exaggerated by a factor of 100 to make them discernible. (Adapted from Seidelmann & Fukushima 1992)

$$
c = 2 9 9 7 9 2 4 5 8 { \mathrm { m / s } }
$$

of the speed of light, the length of a meter is likewise different in the TCB and TDB system. In a similar manner derived quantities like the masses of the Sun, Earth, and planets are affected by the scaling difference (Hellings 1986). Considering, however, that all precise solar system ephemerides are so far based on a TDB time scale, the continued use of TDB is still accepted by the current IAU resolutions.

# 5.1.4 Sidereal Time and Universal Time

Greenwich Mean Sidereal Time GMST, also known as Greenwich Hour Angle, denotes the angle between the mean vernal equinox of date and the Greenwich meridian. It is a direct measure of the Earth’s rotation and may jointly be expressed in angular units or units of time with $3 6 0 ^ { \circ }$ $( 2 \pi )$ corresponding to $2 4 ^ { \mathrm { h } }$ . In terms of SI seconds, the length of a sidereal day (i.e the Earth’s spin period) amounts to $2 3 ^ { \mathrm { h } } 5 6 ^ { \mathrm { m } } 4 _ { \cdot } ^ { \mathrm { s } } 0 9 1 \pm 0 \mathrm { : } 0 0 5$ , making it about four minutes shorter than a $2 4 ^ { \mathrm { h } }$ solar day. Due to length-of-day variations with an amplitude of several milliseconds, sidereal time cannot be computed from other time scales with sufficient precision but must be derived from astronomical and geodetic observations.

<table><tr><td></td><td colspan="7">Contents described in the Explanatory Supplement，mailed with Bulletin B133</td></tr><tr><td></td><td colspan="7">1- EARTH ORIENTATION PARAMETERS（IERS eValuation）. The values in this section are samplings of section 2 given at five-day intervals.</td></tr><tr><td></td><td>Date 1999 （Oh UTC)</td><td>MJD</td><td>X Ⅱ</td><td>1</td><td>UT1R-UTC S</td><td>UT1R-TAI S</td><td>dPsi dEpsilon 0.001&quot;</td><td>0.001&quot;</td></tr><tr><td>Final Bulletin B values.</td><td colspan="8"></td></tr><tr><td>MAR</td><td>2</td><td>51239</td><td>.06888</td><td>.24160</td><td>.651265</td><td>-31.348735</td><td>-45.4</td><td>-5.7</td></tr><tr><td>MAR</td><td>7</td><td>51244</td><td>.06436</td><td>.24260</td><td>.646766</td><td>-31.353234</td><td>-46.6</td><td>-5.6</td></tr><tr><td>MAR</td><td>12</td><td>51249</td><td>.05871</td><td>.24135</td><td>.641753</td><td>-31.358247</td><td>-45.8</td><td>-5.9</td></tr><tr><td>MAR</td><td>17</td><td>51254</td><td>.05110</td><td>.23914</td><td>.636039</td><td>-31.363961</td><td>-44.7</td><td>-6.2</td></tr><tr><td>MAR</td><td>22</td><td>51259</td><td>.04643</td><td>.24049</td><td>.629993</td><td>-31.370007</td><td>-45.3</td><td>-6.4</td></tr><tr><td>MAR</td><td>27</td><td>51264</td><td>.03623</td><td>.24148</td><td>.623165</td><td>5-31.376835</td><td>-44.2</td><td>-7.0</td></tr><tr><td>APR</td><td>1</td><td>51269</td><td>.02603</td><td>.24102</td><td></td><td>.616594-31.383407</td><td>-44.1</td><td>-7.1</td></tr><tr><td colspan="7">Preliminary extension,to be updated weekly in Bulletin A and monthly in Bulletin B.</td><td></td><td></td></tr><tr><td>APR</td><td>6</td><td>51274</td><td>.01733</td><td>.23957</td><td>.609575</td><td>-31.390425</td><td>-45.1</td><td>-7.2</td></tr><tr><td>APR</td><td>11</td><td>51279</td><td>.01051</td><td>.24108</td><td>.602247</td><td>-31.397753</td><td>-43.6</td><td>-7.0</td></tr><tr><td>APR</td><td>16</td><td>51284</td><td>.00731</td><td>.24620</td><td>.595119</td><td>-31.404881</td><td>-44.6</td><td>-7.4</td></tr><tr><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JUN</td><td>10</td><td>51339</td><td>-.04182</td><td>.28130</td><td>.519993</td><td>-31.480007</td><td>-45.1</td><td>-7.3</td></tr><tr><td>JUN</td><td>15</td><td>51344</td><td>-.04460</td><td>.28498</td><td>.514725</td><td>-31.485275</td><td>-46.4</td><td>-8.1</td></tr><tr><td>JUN</td><td>20</td><td>51349</td><td>-.04711</td><td>.28882</td><td>.509953</td><td>-31.490048</td><td>-45.4</td><td>-7.4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JUN</td><td>25</td><td>51354</td><td>-.04935</td><td>.29281</td><td>.505676</td><td>-31.494324</td><td>-47.9</td><td>-7.4</td></tr><tr><td>JUN</td><td>30</td><td>51359</td><td>-.05133</td><td>.29693</td><td>.501881</td><td>-31.498119</td><td>-47.4</td><td>-7.7</td></tr></table>

Note.In UTiR,the effects of zonal tides with periods shorter than 35 days are removed;UT1-UT1R （ smaller than O.OO25s in absolute value ）should be added after quadratic interpolation of UTir.Section 2 of this Bulletin gives the daily interpolation of x,y, UT1,duration of day，dPsi,and dEpsilon.

![](images/4d84243d5ae713d00778c0b98a76b04fd8e5942e375ac999206a92e106cc7860.jpg)  
Fig. 5.4. Sample set of Earth Orientation Parameters as provided by the Bulletin B of the IERS International Earth Rotation Service

Universal Time UT1 is the presently adopted realization of a mean solar time scale with the purpose of achieving a constant average length of the solar day of 24 hours. As a result, the length of one second of Universal Time is not constant, because the actual mean length of a day depends on the rotation of the Earth and the apparent motion of the Sun (i.e. the length of the year). Similar to sidereal time, it is not possible to determine Universal Time by a direct conversion from e.g. atomic time, because the rotation of the Earth cannot be predicted accurately. Every change in the Earth’s rotation alters the length of the day, and must therefore be taken into account in UT1. Universal Time is therefore defined as a function of sidereal time, which directly reflects the rotation of the Earth. For any particular day, $0 ^ { \mathrm { h } }$ UT1 is defined as the instant at which Greenwich Mean Sidereal Time has the value

$$
\begin{array} { r l r } { \mathrm { G M S T } ( \mathrm { 0 } ^ { \mathrm { h } } \mathrm { U T } 1 ) } & { = } & { 2 4 1 1 0 ^ { \mathrm { s } } . 5 4 8 4 1 + 8 6 4 0 1 8 4 ^ { \mathrm { s } } . 8 1 2 8 6 6 \cdot T _ { 0 } } \\ & { } & { + 0 . 0 9 3 1 0 4 \cdot T _ { 0 } ^ { 2 } - 0 . 5 0 0 0 0 6 2 \cdot T _ { 0 } ^ { 3 } } \end{array}
$$

(Aoki et al. 1982). In this expression the time argument

$$
T _ { 0 } = \frac { \mathrm { J D } ( 0 ^ { \mathrm { h } } \mathrm { U T 1 } ) - 2 4 5 1 5 4 5 } { 3 6 5 2 5 }
$$

denotes the number of Julian centuries of Universal Time that have elapsed since 2000 Jan. 1.5 UT1 at the beginning of the day. For an arbitrary time of the day, the expression may be generalized to obtain the relation

$$
\begin{array} { r c l } { { \mathrm { G M S T } } } & { { = } } & { { 2 4 1 1 0 ^ { \mathrm { s } } 5 4 8 4 1 } } \\ { { } } & { { } } & { { + 8 6 4 0 1 8 4 \cdot 8 1 2 8 6 6 T _ { 0 } + 1 . 0 0 2 7 3 7 9 0 9 3 5 0 7 9 5 \mathrm { U T 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + 0 . 0 9 3 1 0 4 T ^ { 2 } - 0 . 0 0 0 0 0 6 2 T ^ { 3 } , } } \end{array}
$$

where the time argument

$$
T = { \frac { \mathrm { J D } ( \mathrm { U T 1 } ) - 2 4 5 1 5 4 5 } { 3 6 5 2 5 } }
$$

specifies the time in Julian centuries of Universal Time elapsed since 2000 Jan. 1.5 UT1.

The difference between Universal Time and Terrestrial Time or International Atomic Time can only be determined retrospectively. At the end of the 20th century $\Delta T = \mathrm { T T } - \mathrm { U T } 1$ amounts to roughly 65 s and increases by about 0.5 to 1.0 seconds per year (cf. Fig. 5.3). In addition to the secular variation, which is caused by tidal friction in the Earth-Moon system, UT1 is subject to periodic variations on the $1 \mathrm { m s }$ level that are caused by tidal perturbations of the polar moment of inertia (see McCarthy (1996) and references therein). By convention, zonal tide terms with periods between 5 and 35 days are removed from UT1 to obtain the regularized Universal Time UT1R. Values of the UT1R–TAI time difference are published on a monthly basis in Bulletin B of the International Earth Rotation Service (IERS) (cf. Fig. 5.4), while the adopted expression for UT1-UT1R is given in McCarthy (1996). Aside from reconstructed, post-facto values of the Earth orientation parameters, the bulletin provides approximate forecasts over a two month time frame at 5-day and 1-day intervals. Using quadratic interpolation of the tabulated data, UT1 may be obtained for arbitrary instants from given TAI (or TT), which then allows GMST to be computed as a function of TAI using the conventional relation (5.19).

Clock time, which is used for everyday purposes, is derived from Coordinated Universal Time (UTC). Since 1972, UTC is obtained from atomic clocks running at the same rate as International Atomic Time and Terrestrial Time. By the use of leap seconds, which may be inserted at the end of June and/or the end of December, care is taken to ensure that UTC never deviates by more than 0.9 seconds from Universal Time UT (cf. Fig. 5.3). Between 1972 and 1999, a total of 23 leap seconds have been introduced as summarized in Table 5.1. New leap seconds are announced in Bulletin C of the IERS (cf. Fig. 5.5) about half a year in advance of their implementation.

# INTERNATIONAL EARTH ROTATION SERVICE (IERS) SERVICE INTERNATIONAL DE LA ROTATION TERRESTRE

BUREAU CENTRAL DE L'IERS   
OBSERVATOIRE DE PARIS   
61,Av.de 1'Ubservatoire 75014 PARIS (France)   
Tei. ：33(0)14051 22 26   
FAX ：33(0)14051 22 91   
Internet:iers@obspm.fr

Paris,17 July 1998

Bulletin C 16

To authorities responsible for the measurement and distribution of time

# UTC TIME STEP

on the 1st of January 1999

A positive leap second will be introduced at the end of December 1998. The sequence of dates of the UTC second markers will be:

1998 December 31, 23h 59m 59s   
1998 December 31, 23h 59m 60s   
1999 January 1, OhOm0s

The difference between UTC and the International Atomic Time TAI is:

from 1997 July 1，Oh UTC,to 1999 January 1,Oh UTC :UTC-TAI $=$ -31s from 1999 January 1,Oh UTC,until further notice ：UTC-TAI $=$ - 32s

Leap seconds can be introduced in UTC at the end of the months of December or June，depending on the evolution of UT1-TAI. Bulletin C mailed every six months,either to announce a time step in UTC,or to confirm that there will be no time step at the next possible date.

Fig. 5.5. Announcement of new UTC leap seconds in Bulletin C of the IERS International Earth Rotation Service

Table 5.1. Leap seconds introduced in Coordinated Universal Time (UTC) since 1972.   

<table><tr><td>From UTC-TAI</td><td>From</td><td>UTC-TAI</td><td>From</td><td>UTC-TAI</td></tr><tr><td>1972 Jan. 1 -10s 1972 July 1 -11s 1973 Jan. 1 -12s 1974 Jan. 1 -13s 1975 Jan. 1 -14s 1976 Jan. 1 -15s</td><td>1981 July 1 1982 July 1 1983 July 1 1985 July 1 1988 Jan. 1 1990 Jan. 1 1991 Jan. 1 1992 July 1</td><td>-20s -21s -22s -23 s -24s -25 s -26s -27s -28s -29s</td><td>1996 Jan. 1 1997 July 1 1999 Jan. 1 2006 Jan. 1 2009 Jan.1 2012 July 1</td><td>-30s -31s -32s -33s -34s -35s</td></tr></table>

# 5.2 Celestial and Terrestrial Reference Systems

The equation of motion as derived in Chap. 3 describes the orbit of a satellite with respect to a quasi-inertial or Newtonian reference system, i.e. with respect to a coordinate system that moves with the center of the Earth but is free of rotation. Satellite observations on the other hand are commonly obtained from an observing site on the surface of the Earth, which is not at rest with respect to this reference system. In order to compare ground-based measurements with the computed satellite position, a concise definition of celestial and terrestrial reference systems is required and their mutual relation has to be established.

Traditionally, celestial reference frames have been tied to the Earth’s rotation and its annual revolution around the Sun. In view of the apparent constancy of both the orbital plane and the rotation axis of the Earth, two global coordinate systems can be defined in a straightforward manner. The first one gives the position of a point in space with respect to the ecliptic (the Earth’s orbital plane), while the other one refers to the Earth’s equatorial plane (the plane perpendicular to the rotation axis). These planes are inclined at an angle $\varepsilon \approx 2 3 . 5 ^ { \circ }$ and the line of intersection is a common axis of both coordinate systems (cf. Fig. 5.6). The $x / x ^ { \prime }$ -axis is defined as being the direction of the vernal equinox or First Point of Aries, designated by $\Upsilon$ . It is perpendicular to both the North Celestial Pole (the $z$ -axis) and the north pole of the ecliptic (the $z ^ { \prime }$ -axis). According to their definition the equatorial coordinates $r$ and the ecliptic coordinates $r ^ { \prime }$ of a given point are related by a rotation

![](images/001f353ade31a9832f3ac367ba043921dc62ae03e7aef8805fad9baf93ef2f25.jpg)  
Fig. 5.6. Ecliptic and equator

$$
r ^ { \prime } = R _ { x } ( \varepsilon ) r \quad ,
$$

where the precise value of the obliquity $\varepsilon$ is given in (5.42). The choice between ecliptic and equatorial coordinates is mainly a question of vividness and convenience. Planetary orbits, for example, are inclined at small angles to the Earth’s orbital plane and are therefore commonly described in ecliptic coordinates. Equatorial coordinates, on the other hand, are closely related to geographical coordinates and provide a natural link to an Earth-fixed reference system.

While the orbital plane of a body around a central mass is fixed in space as long as the attractive force is parallel to the radius vector, this condition does not hold for the Earth due to the presence of other solar system planets. This results in a small secular variation of the orbital plane which is known as planetary precession. At the same time the Earth’s axis of rotation is perturbed by the torque exerted on the equatorial bulge by the Sun and Moon. This torque tries to align the equator with the ecliptic and results in a gyroscopic motion of the Earth’s rotation axis around the pole of the ecliptic with a period of about 26 000 years. As a result of this lunisolar precession the vernal equinox recedes slowly on the ecliptic, whereas the obliquity of the ecliptic remains essentially constant. In addition to precession some minor periodic perturbations of the Earth’s rotation axis may be observed that are known as nutation and reflect variations of the solar and lunar torques on time scales larger than a month. In view of the time-dependent orientation of equator and ecliptic a standard reference frame is usually based on the mean equator, ecliptic, and equinox of some fixed epoch, which is currently selected as the beginning of the year 2000. Access to the Earth Mean Equator and Equinox of J2000 (EME2000) is provided by the FK5 star catalog (Fricke et al. 1988), which provides precise positions and proper motions of some 1 500 stars for the epoch J2000 as referred to the given reference frame.

In view of conceptual difficulties related to the dynamical definition of the ecliptic and equinox (see e.g. Kinoshita & Aoki 1983), it was decided by the IAU in 1991 to establish a new International Celestial Reference System $( I C R S ) ^ { 4 }$ and adopt it for use from 1998 onwards (Feissel & Mignard 1998). The origin of the ICRS is defined as the solar-system barycenter within a relativistic framework and its axes are fixed with respect to distant extragalactic radio objects. These are supposed to have no proper motion, thus ensuring that the ICRS exhibits no net rotation. For a smooth transition to the new system, the ICRS axes are chosen in such a way as to be consistent with the previous FK5 system to within the accuracy of the latter. The fundamental plane of the ICRS is closely aligned with the mean Earth equator at J2000 and the origin of right ascension is defined by an adopted right ascension of the quasar 3C273.

The practical realization of the ICRS is designated the International Celestial Reference Frame (ICRF) and is jointly maintained by the IERS and the IAU Working Group on Reference Frames (cf. Arias et al. 1995). It is mainly based on highprecision observations of extragalactic radio sources using Very Long Baseline Interferometry (VLBI) and may be accessed through a catalog providing source coordinates of 608 objects (cf. McCarthy 1996). Links to existing optical catalogs are provided by radio stars (Seidelmann 1998), while the ICRS and planetary frame tie is provided by VLBI observations of planetary spacecraft as well as lunar laser ranging (LLR) (Folkner et al. 1994, Standish 1998).

Complementary to the ICRS, the International Terrestrial Reference System (ITRS) provides the conceptual definition of an Earth-fixed reference system (Mc-Carthy 1996). Its origin is located at the Earth’s center of mass (including oceans and atmosphere) and its unit of length is the SI meter (consistent with the TCG time coordinate). The orientation of the IERS Reference Pole (IRP) and Meridian (IRM) are consistent with the previously adopted BIH system at epoch 1984.0 and the former Conventional International Origin (CIO) (cf. Sect. 5.4.3). The time evolution of the ITRS is such that it exhibits no net rotation with respect to the Earth’s crust. Realizations of the ITRS are given by the International Terrestrial Reference Frame (ITRF) that provides estimated coordinates and velocities of selected observing stations under authority of the IERS. Observational techniques used in their determination include satellite laser ranging (SLR), lunar laser ranging (LLR), Global Positioning System (GPS), and VLBI measurements. New versions of the ITRF are published annually and exhibit global differences at the centimeter level.

The transformation between the International Celestial Reference System and the International Terrestrial Reference System is accomplished by conventional models for

• precession (Lieske et al. 1977), describing the secular change in the orientation of the Earth’s rotation axis and the equinox,   
nutation (Seidelmann 1982), describing the periodic and short-term variation of the equator and the vernal equinox, and   
• Sidereal Time in relation to UT1 (Aoki et al. 1982), describing the Earth’s rotation about its axis.

These models are supplemented by the IERS Earth Observation Parameters (EOP), comprising

observations of the UT1-TAI difference and measured coordinates of the rotation axis relative to the IERS Reference Pole (IERS 1998). The resulting transformation may be expressed as

$$
r _ { \mathrm { I T R S } } = \pmb { \cal I } ( t ) \pmb { \theta } ( t ) \pmb { { \cal N } } ( t ) \pmb { { \cal P } } ( t ) r _ { \mathrm { I C R S } }
$$

where the rotation matrices $P , N , \Theta$ , and $\pi$ describe the coordinate changes due to precession, nutation, Earth rotation, and polar motion, respectively. A detailed account of the underlying concepts of these transformations and the adopted numerical expressions is presented in the subsequent sections.

# 5.3 Precession and Nutation

# 5.3.1 Lunisolar Torques and the Motion of the Earth’s Rotation Axis

In order to describe the precession of the Earth’s rotation axis, the Earth is considered as a rotationally symmetric gyroscope with an angular momentum $\imath$ that changes with time under the influence of an external torque $\pmb { D }$ according to

$$
{ \frac { d l } { d t } } = D \ .
$$

Even though the direction of the angular momentum may, in general, differ from the symmetry axis of a gyroscope and the instantaneous axis of rotation, one may neglect these differences in the discussion of precession and nutation and assume that $\iota$ is parallel to the unit vector $\boldsymbol { e } _ { z }$ that defines the Earth’s axis (cf. Fig. 5.7). Then

$$
\pmb { l } = C \omega _ { \oplus } \pmb { e } _ { z }
$$

where

$$
\omega _ { \oplus } \approx 7 . 2 9 { \cdot } 1 0 ^ { - 5 } \mathrm { r a d / s }
$$

is the angular velocity of the Earth’s rotation and $C$ is the moment of inertia. For a spherical body of homogeneous density with mass $M _ { \oplus }$ and radius $R _ { \oplus }$ the moment of inertia is given by

$$
I = \frac { 2 } { 5 } M _ { \oplus } R _ { \oplus } ^ { 2 }
$$

for an arbitrary axis of rotation. Due to the Earth’s flattening and its internal structure the actual moments of inertia are given by slightly differing values

$$
A = 0 . 3 2 9 M _ { \oplus } R _ { \oplus } ^ { 2 } \mathrm { a n d } C = 0 . 3 3 0 M _ { \oplus } R _ { \oplus } ^ { 2 }
$$

for a rotation around an axis in the equatorial plane and a rotation around the polar axis, respectively. It may be noted that these quantities are related to the $C _ { 2 0 }$ geopotential coefficient by

$$
C - A = - C _ { 2 0 } M _ { \oplus } R _ { \oplus } ^ { 2 } ~ .
$$

The torque $\pmb { D }$ due to a point mass $m$ (i.e. the Sun or Moon) at a geocentric position $r$ is given by

$$
\pmb { { \cal D } } = - m ( \pmb { r } \times \pmb { \ddot { r } } ) \quad ,
$$

![](images/944908ccd906cc3a6d247efa0a9dacf8886c01bea6108074d7a32211db22e492.jpg)  
Fig. 5.7. Motion of the Earth’s axis under the influence of solar and lunar torques

if $\ddot { r }$ designates the acceleration of $m$ by the gravitational force of the Earth. Neglecting higher-order zonal terms in the expansion of the geopotential, $\ddot { r }$ is obtained as

$$
\ddot { \pmb { r } } = - \frac { G M _ { \oplus } } { r ^ { 3 } } \pmb { r } - \frac { 3 } { 2 } \frac { G M _ { \oplus } R _ { \oplus } ^ { 2 } C _ { 2 0 } } { r ^ { 7 } } [ ( 5 z ^ { 2 } - r ^ { 2 } ) \pmb { r } - 2 ( z r ^ { 2 } ) \pmb { e } _ { z } ]
$$

for a rotationally symmetric Earth (cf. Sect. 3.2), where $z = r e _ { z }$ is the distance of $m$ from the equatorial plane. All terms of the acceleration that are parallel to the radius vector affect the Earth’s center of mass, only, and the resulting torque is given by the simple expression

$$
{ \pmb { { \cal D } } } = G m ( C - A ) \frac { 3 z ( \pmb { r } \times \pmb { e } _ { z } ) } { r ^ { 5 } } .
$$

The Sun moves around the Earth in a near-circular orbit that is inclined at an angle $\varepsilon$ with respect to the equator and the resulting torque vanishes whenever the Sun crosses the equator $( z = 0$ ). Introducing the unit vector $e _ { x }$ in the direction of the vernal equinox (cf. Fig. 5.7), the torque of the Sun at right angles to the line of

nodes is found to be

$$
D _ { \odot } = G M _ { \odot } ( C - A ) \frac { 3 \sin \varepsilon \cos \varepsilon } { r _ { \odot } ^ { 3 } } { e _ { x } } \quad ,
$$

irrespective of whether the Sun is above or below the equatorial plane. This results in a mean solar torque

$$
\overline { { { D } } } _ { \odot } = G M _ { \odot } ( C - A ) \frac { 3 \sin \varepsilon \cos \varepsilon } { 2 r _ { \odot } ^ { 3 } } e _ { x }
$$

in the direction of the vernal equinox during the course of a year, whereas the mean component in the direction perpendicular to $e _ { x }$ vanishes. Making use of Kepler’s third law, the last expression may further be written as

$$
\overline { { { D } } } _ { \odot } = \frac { 3 } { 2 } ( C - A ) \sin \varepsilon \cos \varepsilon n _ { \odot } ^ { 2 } { \pmb e } _ { x } \quad ,
$$

where $n _ { \odot }$ is the mean motion of the Sun in its orbit around the Earth.

Similar considerations hold for the Moon, with the exception that the inclination of the lunar orbit with respect to Earth’s equator is not fixed, but varies between $1 8 ^ { \circ }$ and $2 8 ^ { \circ }$ during a period of about 18 years. Since this period is small compared to the time scale of precession, one may, however, assume that the Moon moves in the ecliptic just like the Sun. This yields a total mean torque of

$$
\overline { { { \cal D } } } = \frac { 3 } { 2 } ( C - A ) \sin \varepsilon \cos \varepsilon \left( n _ { \odot } ^ { 2 } + \frac { M _ { \mathrm { M } } } { M _ { \oplus } } n _ { \mathrm { M } } ^ { 2 } \right) e _ { x } ,
$$

which changes neither the Earth’s total angular momentum nor the obliquity $\varepsilon$ but forces $\iota$ to move around the pole of the ecliptic at an angular velocity

$$
\varOmega _ { \mathrm { p r e c } } = \frac { | \overline { { D } } | } { \sin ( \varepsilon ) | l | } = \frac { 3 } { 2 } \frac { C - A } { C } \cos ( \varepsilon ) \frac { n _ { \odot } ^ { 2 } + n _ { \mathrm { M } } ^ { 2 } M _ { \mathrm { M } } / M _ { \oplus } } { \omega _ { \oplus } }
$$

of one revolution in 26 000 years.

# 5.3.2 Coordinate Changes due to Precession

The combined effects of precession on the orientation of the ecliptic and the equator are illustrated in Fig. 5.8, where the motion of both planes is described with respect to the mean equator and ecliptic of the reference epoch J2000 (2000 January 1.5).

Due to lunisolar precession the intersection of the mean equator of epoch $t$ and the mean ecliptic of J2000 lags behind the vernal equinox $\Upsilon _ { 2 0 0 0 }$ of J2000 by an angle

$$
\psi = 5 0 3 8 ! 8 \cdot T - 1 ! \cdot T ^ { 2 }
$$

that increases almost linearly with time, while the inclination of the mean equator with respect to the ecliptic of J2000 is nearly constant:

$$
\omega = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 ^ { \prime \prime } + 0 _ { \cdot } ^ { \prime \prime } 0 5 \cdot T ^ { 2 } ~ .
$$

![](images/cedec6b147b0467459bc2a41cc754ea02db40521b671033e2068288d0d607a2a.jpg)  
Fig. 5.8. The effects of precession on the ecliptic, equator, and vernal equinox

Here

$$
T = ( \mathrm { J D } - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 . 0
$$

is measured in Julian centuries Terrestrial Time5 since J2000 TT.

While the gravitational pull of the Sun and Moon changes the direction of the Earth’s axis and the equatorial plane, it does not affect the orientation of the ecliptic. Long-term changes of the mean orbit of the Earth around the Sun do, however, arise from the influence of the planets, which results in a corresponding motion of the ecliptic. With respect to the ecliptic of J2000 the ecliptic at another epoch is inclined at an angle of

$$
\pi = 4 7 . ^ { \prime \prime } 0 0 2 9 \cdot T - 0 . ^ { \prime \prime } 0 3 3 0 2 \cdot T ^ { 2 } + 0 . ^ { \prime \prime } 0 0 0 0 6 0 \cdot T ^ { 3 } ,
$$

where the line of intersection is described by the angle

$$
\pi = 1 7 4 . 8 7 6 3 8 3 8 8 9 - 8 6 9 ! ^ { \prime \prime } 8 0 8 9 \cdot T + 0 ! ^ { \prime \prime } 0 3 5 3 6 \cdot T ^ { 2 } .
$$

These values follow from a theory of the secular changes of the Earth’s orbital elements and have been derived by Lieske et al. (1977) following earlier calculations by Newcomb.

As a result of planetary precession the obliquity of the ecliptic is slightly decreasing and amounts to

$$
\varepsilon = 2 3 ^ { \circ } 4 3 9 2 9 1 1 1 - 4 6 ^ { \prime \prime } 8 1 5 0 T - 0 ^ { \prime \prime } 0 0 0 5 9 T ^ { 2 } + 0 ^ { \prime \prime } 0 0 1 8 1 3 T ^ { 3 } ~ .
$$

The combined precession in longitude

$$
p = A - \varPi = 5 0 2 9 ; \prime 0 9 6 6 \cdot T + 1 ; 1 1 1 1 3 \cdot T ^ { 2 } - 0 ; \prime 0 0 0 0 0 6 T ^ { 3 }
$$

is somewhat smaller, therefore, than the lunisolar precession $\psi$ alone.

The orientation of the mean equator and equinox of epoch $T$ with respect to the equator and equinox of J2000 is defined by the three angles

$$
\begin{array} { l l l } { { \zeta } } & { { = } } & { { 2 3 0 6 \mathrm { ! 2 } 2 1 8 1 T + 0 \mathrm { ! 2 } 3 0 1 8 8 T ^ { 2 } + 0 \mathrm { ! 7 0 1 7 9 9 8 } T ^ { 3 } } } \\ { { \vartheta } } & { { = } } & { { 2 0 0 4 \mathrm { ! 2 } 3 1 0 9 T - 0 \mathrm { ! 2 } 4 2 6 6 5 T ^ { 2 } - 0 \mathrm { ! 2 } 0 4 1 8 3 3 T ^ { 3 } } } \\ { { z } } & { { = } } & { { \zeta + 0 \mathrm { ! 7 7 9 2 8 0 } T ^ { 2 } + 0 \mathrm { ! 7 0 0 0 2 0 5 } T ^ { 3 } } } \end{array}
$$

that follow from the fundamental quantities $\pi , \pi$ , $p$ , and $\varepsilon$

According to Fig. 5.8 the transformation from coordinates $r _ { \mathrm { I C R F } }$ (referred to the mean equator and equinox of J2000) to coordinates referred to the mean equator and equinox of some other epoch (“mean-of-date”) may now be written as

$$
r _ { \mathrm { m o d } } = P r _ { \mathrm { I C R F } }
$$

where the matrix $P$ is the product of three consecutive rotations:

$$
\begin{array} { r c l } { { P } } & { { = } } & { { { \cal R } _ { z } ( - 9 0 ^ { \circ } - z ) { \cal R } _ { x } ( \vartheta ) { \cal R } _ { z } ( 9 0 ^ { \circ } - \zeta ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { { \cal R } _ { z } ( - z ) { \cal R } _ { y } ( \vartheta ) { \cal R } _ { z } ( - \zeta ) . } } \end{array}
$$

Evaluating the matrix product, one obtains the following expression for $P = ( p _ { i j } )$

$$
{ \begin{array} { r l } { p _ { 1 1 } } & { = \ - \sin z \sin \zeta + \cos z \cos { \vartheta } \cos \zeta } \\ { p _ { 2 1 } } & { = \ + \cos z \sin \zeta + \sin z \cos { \vartheta } \cos \zeta } \\ { p _ { 3 1 } } & { = \ + \sin { \vartheta } \cos \zeta } \\ { p _ { 1 2 } } & { = \ - \sin z \cos \zeta - \cos z \cos { \vartheta } \sin \zeta } \\ { p _ { 2 2 } } & { = \ + \cos z \cos \zeta - \sin z \cos { \vartheta } \sin \zeta } \\ { p _ { 3 2 } } & { = \ - \sin { \vartheta } \sin \zeta } \\ { p _ { 1 3 } } & { = \ - \cos z \sin { \vartheta } } \\ { p _ { 2 3 } } & { = \ - \sin z \sin { \vartheta } } \\ { p _ { 3 3 } } & { = \ + \cos { \vartheta } \ . } \end{array} }
$$

Since $P$ is a rotation matrix, its inverse ${ \pmb P } ^ { - 1 }$ is equal to the transpose $P ^ { T }$ :

$$
\pmb { P } ^ { - 1 } = \pmb { P } ^ { T } = \pmb { R } _ { z } ( + \zeta ) \pmb { R } _ { y } ( - \vartheta ) \pmb { R } _ { z } ( + z ) \quad .
$$

The precession transformation between arbitrary epochs $T _ { 1 }$ and $T _ { 2 }$ is thus obtained from

$$
r _ { 2 } = P ( T _ { 2 } ) P ^ { T } ( T _ { 1 } ) r _ { 1 } .
$$

Here $P ( T )$ denotes the rotation from the mean equator and equinox of J2000 to the mean equator and equinox of epoch $T$ .

Alternatively, the generalized expressions

$$
\begin{array} { r c l } { { \zeta ( T , t ) } } & { { = } } & { { ( + 2 3 0 6 { } ^ { \prime } 2 1 8 1 + 1 { } ^ { \prime } 3 9 6 5 6 T - 0 { } ^ { \prime } 0 0 0 1 3 9 T ^ { 2 } ) t } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + ( + 0 { } ^ { \prime \prime } 3 0 1 8 8 - 0 { } ^ { \prime \prime } 0 0 0 3 4 4 T ) t ^ { 2 } + 0 { } ^ { \prime \prime } 0 1 7 9 9 8 t ^ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { z ( T , t ) } } & { { = } } & { { ( + 2 3 0 6 { } ^ { \prime \prime } 2 1 8 1 + 1 { } ^ { \prime \prime } 3 9 6 5 6 T - 0 { } ^ { \prime \prime } 0 0 0 1 3 9 T ^ { 2 } ) t } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + ( + 1 { } ^ { \prime \prime } 0 9 4 6 8 + 0 { } ^ { \prime \prime } 0 0 0 0 6 6 T ) t ^ { 2 } + 0 { } ^ { \prime \prime } 0 1 8 2 0 3 t ^ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { \vartheta ( T , t ) } } & { { = } } & { { ( + 2 0 0 4 { } ^ { \prime \prime } 3 1 0 9 - 0 { } ^ { \prime \prime } 8 5 3 3 0 T - 0 { } ^ { \prime \prime } 0 0 0 2 1 7 T ^ { 2 } ) t } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + ( - 0 { } ^ { \prime \prime } 4 2 6 6 5 - 0 { } ^ { \prime \prime } 0 0 0 2 1 7 T ) t ^ { 2 } - 0 { } ^ { \prime \prime } 0 4 1 8 3 3 t ^ { 3 } } } \end{array}
$$

(Lieske et al.1977, Lieske 1979) with

$$
\begin{array} { l c l } { { T } } & { { = } } & { { T _ { 1 } \mathrm { ~  ~ { ~ \stackrel { ~ \textstyle ~ = ~ } { ~ \textstyle ~ ( ~ J D _ { 1 } ( T T ) ~ - ~ 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5 . 0 } ~ } } } } \\ { { t } } & { { = } } & { { T _ { 2 } - T _ { 1 } \mathrm { ~  ~ { ~ = ~ } } } } & { { ( \mathrm { J D _ { 2 } ( T T ) - J D _ { 1 } ( T T ) ) / 3 6 5 2 5 . 0 ~ } } } \end{array}
$$

can be used to compute the transformation matrix

$$
P ( T _ { 2 } , T _ { 1 } ) = R _ { z } ( - z ( T , t ) ) R _ { y } ( \vartheta ( T , t ) ) R _ { z } ( - \zeta ( T , t ) )
$$

directly from the mean equator and equinox of epoch $T _ { 1 }$ to the mean equator and equinox of epoch $T _ { 2 }$ .

The 3rd-order polynomials6 for the precession angles given in (5.50) obey the identities

$$
\begin{array} { l c l } { { z ( T + t , - t ) } } & { { = } } & { { - \zeta ( T , t ) } } \\ { { \zeta ( T + t , - t ) } } & { { = } } & { { - z ( T , t ) } } \\ { { \vartheta ( T + t , - t ) } } & { { = } } & { { - \vartheta ( T , t ) . } } \end{array}
$$

Accordingly,

$$
\begin{array} { l l l } { P ( T _ { 1 } , T _ { 2 } ) } & { = } & { \pmb { R _ { z } } ( - z ( T + t , - t ) ) \pmb { R _ { y } } ( + \vartheta ( T + t , - t ) ) \pmb { R _ { z } } ( - \zeta ( T + t , - t ) ) \pmb { \mathrm { \Omega } } } \\ & { = } & { \pmb { R _ { z } } ( \zeta ( T , t ) ) \pmb { R _ { y } } ( - \vartheta ( T , t ) ) \pmb { R _ { z } } ( z ( T , t ) ) } \\ & { = } & { \pmb { P ^ { T } } ( T _ { 2 } , T _ { 1 } ) } \end{array}
$$

yields the rigorous inverse of $P ( T _ { 2 } , T _ { 1 } )$ . On the other hand, the transitivity relation

$$
P ( T _ { 3 } , T _ { 1 } ) = P ( T _ { 3 } , T _ { 2 } ) P ( T _ { 2 } , T _ { 1 } )
$$

is not maintained exactly by the generalized precession angles. It is therefore better in practical applications of expression (5.50) to avoid the sequential use of precession matrices. Otherwise, errors typically of the order of $1 0 ^ { - 1 1 }$ rad, or $1 0 ^ { - \bar { 6 } \prime \prime }$ , will arise for epochs lying within one century from the reference epoch J2000.

# 5.3.3 Nutation

Aside from the secular precessional motion the orientation of the Earth’s rotation axis is affected by small periodic perturbations that are known as nutation. They are due to the monthly and annual variations of the lunar and solar torque that have been averaged in the treatment of precession. The main contribution to nutation arises from the varying orientation of the lunar orbit with respect to the Earth’s equator as expressed by the longitude of the Moon’s ascending node $\varOmega$ . It induces a periodic shift

$$
\varDelta \psi \approx - 1 7 \% 0 0 \cdot \sin ( \varOmega )
$$

of the vernal equinox and a change

$$
\varDelta \varepsilon \approx + 9 . ^ { \prime \prime } 2 0 3 \cdot \cos ( \varOmega )
$$

of the obliquity of the ecliptic during the 18.6-year nodal period of the Moon. As a result the true celestial pole performs an elliptic motion around the mean position as affected by the lunisolar precession.

The currently adopted IAU 1980 nutation series is based on theories of Kinoshita (1977) and Wahr (1981). It expresses the nutation angles

$$
\begin{array} { r c l } { { \Delta \psi } } & { { = } } & { { \displaystyle \sum _ { i = 1 } ^ { 1 0 6 } ( \Delta \psi ) _ { i } \cdot \mathrm { s i n } ( \phi _ { i } ) } } \\ { { \Delta \varepsilon } } & { { = } } & { { \displaystyle \sum _ { i = 1 } ^ { 1 0 6 } ( \Delta \varepsilon ) _ { i } \cdot \mathrm { c o s } ( \phi _ { i } ) } } \end{array}
$$

by a total of 106 terms, which are summarized in Table 5.2 (Seidelmann 1982). Each term describes a periodic function of the mean elements of the lunar and solar orbit with argument

$$
\phi _ { i } = p _ { l , i } l + p _ { l ^ { \prime } , i } l ^ { \prime } + p _ { F , i } F + p _ { D , i } D + p _ { \Omega , i } \Omega
$$

and integer coefficients $p _ { l , i } , p _ { l ^ { \prime } , i } , p _ { F , i } , p _ { D , i }$ , and $p _ { \varOmega , i } .$ The other parameters are the Moon’s mean anomaly $( l )$ , the Sun’s mean anomaly $( l ^ { \prime } )$ , the mean distance of the Moon from the ascending node $( F )$ , the difference between the mean longitudes of the Sun and the Moon $( D )$ , and the mean longitude of the ascending node of the lunar orbit $( \varOmega )$ . Numerical values for use with the IAU 1980 theory of nutation are originally given as

$$
{ \begin{array} { l } { l } { = 1 3 4 ^ { \circ } 5 7 4 6 { \mathrm { perth } } 7 3 3 + 4 7 7 1 9 8 ^ { \circ } 5 2 0 2 { \mathrm { 0 } } 2 { \mathrm { : } } 6 3 3 T + 3 1 { \mathrm { : } } 3 1 0 T ^ { 2 } + 0 { \mathrm { 0 } } 6 4 T ^ { 3 } } \\ { l { \mathrm { ' } } = 3 5 7 ^ { \circ } 3 1 ^ { \prime } 3 9 { \mathrm { 0 } } 4 + } \\ { 5 9 9 9 9 9 9 0 4 { \mathrm { + } } 3 5 9 9 9 9 0 3 { \mathrm { 0 } } 1 0 { \mathrm { ! } } 2 2 2 4 T - \ 0 { \mathrm { : } } 5 7 7 T ^ { 2 } - 0 { \mathrm { 0 } } 1 2 T ^ { 3 } } \\ { F = 9 3 9 9 1 6 1 8 { \mathrm { ? } } 8 7 7 + 4 8 3 2 0 2 0 9 0 1 0 { \mathrm { 3 : } } 1 3 7 T - 1 3 { \mathrm { : } } 3 7 2 5 7 T ^ { 2 } + 0 { \mathrm { : } } 0 1 1 T ^ { 3 } } \\ { D = 2 9 7 9 5 1 6 1 { \mathrm { 0 } } 1 { \mathrm { : } } 3 0 7 + 4 4 5 2 6 7 6 0 6 4 1 { \mathrm { : } } 3 2 8 8 T - \ 6 { \mathrm { : } } 8 9 8 1 T ^ { 2 } + 0 { \mathrm { 0 } } 8 9 T ^ { 3 } } \\ { \Omega = 1 2 5 { \mathrm { 0 } } 2 4 0 { \mathrm { 0 } } { \mathrm { : } } 3 0 0 - \ 1 9 3 4 9 0 8 ^ { \prime } 1 0 { \mathrm { : } } 5 3 9 T + \ 7 { \mathrm { : } } 4 5 5 5 T ^ { 2 } + 0 { \mathrm { 0 } } 8  T ^ { 3 } } \end{array} }
$$

Table 5.2. The IAU 1980 nutation theory   

<table><tr><td rowspan=1 colspan=1>Pl PV PF PD PΩ</td><td rowspan=1 colspan=2>△Ψ [0.0001&quot;]</td><td rowspan=1 colspan=2>△ε[0.0001&#x27;]</td><td rowspan=1 colspan=1>i</td><td rowspan=1 colspan=4>Pl Pv PF PD PΩ</td><td rowspan=1 colspan=1>△</td><td rowspan=1 colspan=1>4ε</td><td rowspan=1 colspan=1>i</td></tr><tr><td rowspan=1 colspan=1>0 0 0 0 1</td><td rowspan=1 colspan=2>-171996-174.2T</td><td rowspan=1 colspan=2>+92025+8.9T</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=4>1 0 22</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>54</td></tr><tr><td rowspan=1 colspan=1>0 0 0 0 2</td><td rowspan=1 colspan=2>2062+0.2T</td><td rowspan=1 colspan=2>-895+0.5 T</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=4>1 0 0 0</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>55</td></tr><tr><td rowspan=1 colspan=1>2 0 2 0 1</td><td rowspan=1 colspan=2>46</td><td rowspan=1 colspan=2>-24</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=4>20 2</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1>56</td></tr><tr><td rowspan=1 colspan=1>2 0    0 0</td><td rowspan=1 colspan=2>11</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=4>00 0 2</td><td rowspan=1 colspan=1>-6</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>57</td></tr><tr><td rowspan=1 colspan=1>2 0 2 0 2</td><td rowspan=1 colspan=2>-3</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=4>00 2 2</td><td rowspan=1 colspan=1>-7</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>58</td></tr><tr><td rowspan=1 colspan=1>0     0</td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=4>1 0 2-2 1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>59</td></tr><tr><td rowspan=1 colspan=1>0    2     1</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=4>0 0 0-2</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>60</td></tr><tr><td rowspan=1 colspan=1>2 0    0</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=3>0 0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>61</td></tr><tr><td rowspan=1 colspan=1>0 0 2</td><td rowspan=1 colspan=2>-13187 -1.6T</td><td rowspan=1 colspan=2>5736-3.1T</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>2 0</td><td rowspan=1 colspan=3>2 0</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>62</td></tr><tr><td rowspan=1 colspan=1>0 1 0 0</td><td rowspan=1 colspan=2>1426 -3.4T</td><td rowspan=1 colspan=2>54-0.1T</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0 1</td><td rowspan=1 colspan=3>0-2</td><td rowspan=1 colspan=1>-4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>63</td></tr><tr><td rowspan=1 colspan=1>0 1 2-2</td><td rowspan=1 colspan=2>-517 +1.2T</td><td rowspan=1 colspan=2>224-0.6T</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=4>1 0一-2 0</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>64</td></tr><tr><td rowspan=1 colspan=1>0-1 2-2</td><td rowspan=1 colspan=2>217 -0.5T</td><td rowspan=1 colspan=2>-95+0.3 T</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=4>0 00 1</td><td rowspan=1 colspan=1>-4</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>65</td></tr><tr><td rowspan=1 colspan=1>0 0 2-2</td><td rowspan=1 colspan=2>129 +0.1T</td><td rowspan=1 colspan=2>-70</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=4>1 1 0 0</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>66</td></tr><tr><td rowspan=1 colspan=1>2 00-2</td><td rowspan=1 colspan=2>48</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>67</td></tr><tr><td rowspan=1 colspan=1>0 0 2</td><td rowspan=1 colspan=2>-22</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=3>2 0</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>68</td></tr><tr><td rowspan=1 colspan=1>0 2 0 0</td><td rowspan=1 colspan=2>17 -0.1T</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1-1</td><td rowspan=1 colspan=3>2 2</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>69</td></tr><tr><td rowspan=1 colspan=1>0 1 0 0</td><td rowspan=1 colspan=2>-15</td><td rowspan=1 colspan=2>9</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>-2 0</td><td rowspan=1 colspan=3>001</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=1 colspan=1>0 2 2     2</td><td rowspan=1 colspan=2>16 +0.1T</td><td rowspan=1 colspan=2>7</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>3 0</td><td rowspan=1 colspan=3>202</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>71</td></tr><tr><td rowspan=1 colspan=1>0    0 0</td><td rowspan=1 colspan=2>12</td><td rowspan=1 colspan=2>6</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>2 2</td><td rowspan=1 colspan=1>-3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>72</td></tr><tr><td rowspan=1 colspan=1>2 0 0 2</td><td rowspan=1 colspan=2>-6</td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=3>2 0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>73</td></tr><tr><td rowspan=1 colspan=1>0-1 2-2</td><td rowspan=1 colspan=2>-5</td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=3>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>74</td></tr><tr><td rowspan=1 colspan=1>2 0 0-2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>2 0</td><td rowspan=1 colspan=3>0 0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>75</td></tr><tr><td rowspan=1 colspan=1>0 1 2-2  1</td><td rowspan=1 colspan=1>4X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>1 0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>76</td></tr><tr><td rowspan=1 colspan=1>00-1 0</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>3 0</td><td rowspan=1 colspan=2>0 0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1>2 10-2 0</td><td rowspan=1 colspan=1>X1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0 0</td><td rowspan=1 colspan=2>2 1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>78</td></tr><tr><td rowspan=1 colspan=1>00-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>-1 0</td><td rowspan=1 colspan=2>0 0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>79</td></tr><tr><td rowspan=1 colspan=1>0 1-2     0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>1 02</td><td rowspan=1 colspan=2>0-4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>80</td></tr><tr><td rowspan=1 colspan=1>0 1 0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>2  0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>81</td></tr><tr><td rowspan=1 colspan=1>0 0 1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>1 0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>82</td></tr><tr><td rowspan=1 colspan=1>0 1 2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>2 0</td><td rowspan=1 colspan=2>0-4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>83</td></tr><tr><td rowspan=1 colspan=1>0 0 2 0  2</td><td rowspan=1 colspan=1>-2274</td><td rowspan=1 colspan=1>-0.2T</td><td rowspan=1 colspan=2>977-0.5 T</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=2>2-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>84</td></tr><tr><td rowspan=1 colspan=1>0 0 0</td><td rowspan=1 colspan=1>712</td><td rowspan=1 colspan=1>+0.1T</td><td rowspan=1 colspan=2>-7</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>0 0 2 0</td><td rowspan=1 colspan=1>-386</td><td rowspan=1 colspan=1>-0.4T</td><td rowspan=1 colspan=2>200</td><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8哆</td></tr><tr><td rowspan=1 colspan=1>0 2 0</td><td rowspan=1 colspan=1>-301</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>129</td><td rowspan=1 colspan=1>129-0.1T</td><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>4 0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>8哆</td></tr><tr><td rowspan=1 colspan=1>0 0--2  0</td><td rowspan=1 colspan=1>-158</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>一-1</td><td rowspan=1 colspan=2>0-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>哆88</td></tr><tr><td rowspan=1 colspan=1>02 0  2</td><td rowspan=1 colspan=1>123</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-53</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>2 0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>89</td></tr><tr><td rowspan=1 colspan=1>0 0 0 2  0</td><td rowspan=1 colspan=1>63</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>2 0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>0 0 0  1</td><td rowspan=1 colspan=1>63</td><td rowspan=1 colspan=1>+0.1T</td><td rowspan=1 colspan=1>-33</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>1 0</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>91</td></tr><tr><td rowspan=1 colspan=1>0 0 0</td><td rowspan=1 colspan=1>-58</td><td rowspan=1 colspan=1>-0.1T</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>0 0</td><td rowspan=1 colspan=2>4-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>92</td></tr><tr><td rowspan=1 colspan=1>0 2 2</td><td rowspan=1 colspan=1>-59</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=2>2-2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>93</td></tr><tr><td rowspan=1 colspan=1>0 2 0</td><td rowspan=1 colspan=1>51</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>41</td><td rowspan=1 colspan=1>1 0</td><td rowspan=1 colspan=2>2-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>94</td></tr><tr><td rowspan=1 colspan=1>0 0 2 2</td><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>2 0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>95</td></tr><tr><td rowspan=1 colspan=1>0 0 0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=3>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>96</td></tr><tr><td rowspan=1 colspan=1>0 2 2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>12</td><td rowspan=1 colspan=1>44</td><td rowspan=1 colspan=1>0 0</td><td rowspan=1 colspan=2>-2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>97</td></tr><tr><td rowspan=1 colspan=1>2 0 2 0</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>13</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>0 0</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>98</td></tr><tr><td rowspan=1 colspan=1>0 2 0  0</td><td rowspan=1 colspan=2>26</td><td rowspan=1 colspan=2>-1</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>0 1</td><td rowspan=1 colspan=2>0 2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>99</td></tr><tr><td rowspan=1 colspan=1>0 2 0  1</td><td rowspan=1 colspan=2>21</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>110</td><td rowspan=1 colspan=2>-2-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>100</td></tr><tr><td rowspan=1 colspan=1>0 0 2</td><td rowspan=1 colspan=2>16</td><td rowspan=1 colspan=2>-8</td><td rowspan=1 colspan=1>48</td><td rowspan=1 colspan=1>0-1</td><td rowspan=1 colspan=2>2 0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>101</td></tr><tr><td rowspan=1 colspan=1>0 0</td><td rowspan=1 colspan=2>13</td><td rowspan=1 colspan=2>7</td><td rowspan=1 colspan=1>49</td><td rowspan=1 colspan=3>1 0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>102</td></tr><tr><td rowspan=1 colspan=1>0 2 2</td><td rowspan=1 colspan=2>-10</td><td rowspan=1 colspan=2>5</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=3>0-2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>103</td></tr><tr><td rowspan=1 colspan=1>0一2  0</td><td rowspan=1 colspan=2>-7</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>51</td><td rowspan=1 colspan=3>2 0 0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>104</td></tr><tr><td rowspan=1 colspan=1>0     2 0  2</td><td rowspan=1 colspan=2>7</td><td rowspan=1 colspan=2>-3</td><td rowspan=1 colspan=1>52</td><td rowspan=1 colspan=3>0 0 2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>105</td></tr><tr><td rowspan=1 colspan=1>2  0  2</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=1>53</td><td rowspan=1 colspan=4>0     0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>106</td></tr></table>

![](images/2901177959dde224e1d9ce129cee6d683390d1328d11b2a26a0964cabba78891.jpg)  
Fig. 5.9. The shift in the positions of the equator, the ecliptic and the vernal equinox, caused by nutation

in Seidelmann (1982), while slightly modified expressions recommended by the IERS are given in McCarthy (1996).

Following Fig. 5.9, the transformation from mean-of-date coordinates (referred to the mean equator and equinox) to true-of-date coordinates (referred to the true equator and equinox) may be written as

$$
r _ { \mathrm { t o d } } = N ( T ) r _ { \mathrm { m o d } } ,
$$

with

$$
N ( T ) = { \pmb R } _ { x } ( - \varepsilon - \varDelta \varepsilon ) { \pmb R } _ { z } ( - \varDelta \psi ) { \pmb R } _ { x } ( \varepsilon ) \quad .
$$

The elements of the transformation matrix $N = ( n _ { i j } )$ in equatorial coordinates are given by

$$
\begin{array} { r l } { n _ { 1 1 } } & { = } & { + \cos ( A y ) } \\ { n _ { 2 1 } } & { = } & { + \cos ( \varepsilon ^ { \prime } ) \cdot \sin ( A y ) } \\ { n _ { 3 1 } } & { = } & { + \sin ( \varepsilon ^ { \prime } ) \cdot \sin ( A y ) } \\ { n _ { 1 2 } } & { = } & { - \cos ( \varepsilon ) \cdot \sin ( A y ) } \\ { n _ { 2 2 } } & { = } & { + \cos ( \varepsilon ) \cdot \cos ( \varepsilon ^ { \prime } ) \cdot \cos ( A y ) + \sin ( \varepsilon ) \cdot \sin ( \varepsilon ^ { \prime } ) } \\ { n _ { 3 2 } } & { = } & { + \cos ( \varepsilon ) \cdot \sin ( \varepsilon ^ { \prime } ) \cdot \cos ( A y ) - \sin ( \varepsilon ) \cdot \cos ( \varepsilon ^ { \prime } ) } \\ { n _ { 1 3 } } & { = } & { - \sin ( \varepsilon ) \cdot \sin ( A y ) } \\ { n _ { 2 3 } } & { = } & { + \sin ( \varepsilon ) \cdot \cos ( \varepsilon ^ { \prime } ) \cdot \cos ( A y ) - \cos ( \varepsilon ) \cdot \sin ( \varepsilon ^ { \prime } ) } \\ { n _ { 3 3 } } & { = } & { + \sin ( \varepsilon ) \cdot \sin ( \varepsilon ^ { \prime } ) \cdot \cos ( A y ) + \cos ( \varepsilon ) \cdot \cos ( \varepsilon ^ { \prime } ) \enspace , } \end{array}
$$

where $\varepsilon$ and $\varepsilon ^ { \prime } = \varepsilon + \varDelta \varepsilon$ are the mean and true obliquity of the ecliptic at time $T = ( \mathrm { J D } ( \mathrm { T T } ) - 2 4 5 1 5 4 5 . 0 ) / 3 6 5 2 5$ .

From VLBI and LLR observations, the IAU 1980 theory of nutation is known to be in error on the level of several milli-arcseconds and an improved nutation theory (IERS 1996) due to T. Herring has been made available in McCarthy (1996). Nevertheless, the IAU 1980 series is retained as official standard in the IERS conventions and the existing deficiencies are compensated for by observed values of the celestial pole offsets $\delta \varDelta \psi$ and $\delta \varDelta \varepsilon$ . Improved nutation angles are obtained by adding these corrections to the IAU 1980 values:

$$
\begin{array} { r c l c l } { { \Delta \psi } } & { { = } } & { { \Delta \psi _ { \mathrm { I A U 1 9 8 0 } } } } & { { + } } & { { \delta \varDelta \psi } } \\ { { \Delta \varepsilon } } & { { = } } & { { \Delta \varepsilon _ { \mathrm { I A U 1 9 8 0 } } } } & { { + } } & { { \delta \varDelta \varepsilon . } } \end{array}
$$

The corresponding correction to the nutation matrix is obtained from

$$
N = \left( \begin{array} { c c c } { { 1 } } & { { - \delta \varDelta \psi \cos \varepsilon } } & { { - \delta \varDelta \psi \sin \varepsilon } } \\ { { + \delta \varDelta \psi \cos \varepsilon } } & { { 1 } } & { { - \delta \varDelta \varepsilon } } \\ { { + \delta \varDelta \psi \sin \varepsilon } } & { { + \delta \varDelta \varepsilon } } & { { 1 } } \end{array} \right) N _ { \mathrm { I A U l 9 8 0 } }
$$

(McCarthy 1996). Post-facto determinations and short-term predictions of the celestial pole offsets are published on a monthly basis in Bulletin B of the IERS (cf. Fig. 5.4).

# 5.4 Earth Rotation and Polar Motion

# 5.4.1 Rotation About the Celestial Ephemeris Pole

The IAU precession and nutation theories yield the instantaneous orientation of the Earth’s rotation axis, or, more precisely, the orientation of the Celestial Ephemeris Pole (CEP)7 with respect to the International Celestial Reference System. The rotation about the CEP axis itself is described by the Greenwich Mean Sidereal Time (GMST) that measures the angle between the mean vernal equinox and the Greenwich Meridian (cf. Sect. 5.1.4). Given the UT1–UTC or UT1–TAI time difference as monitored and published by the IERS, the Greenwich Mean Sidereal Time at any instant can be computed from the conventional relation (5.19).

Similar to GMST, the Greenwich Apparent Sidereal Time (GAST) measures the hour angle of the true equinox. Both values differ by the nutation in right ascension

$$
\mathrm { G A S T - G M S T } = \varDelta { \psi } \cos { \varepsilon } \quad ,
$$

which is also known as the equation of the equinoxes8. Given the apparent sidereal time, the matrix

$$
\pmb { \Theta } ( t ) = \pmb { R } _ { z } ( \mathrm { G A S T } )
$$

yields the transformation between the true-of-date coordinate system (as defined by the adopted precession–nutation theory) and a system aligned with the Earth equator and Greenwich meridian.

The common $z$ -axis of both systems points to the Celestial Ephemeris Pole, which is not, however, fixed with respect to the surface of the Earth, but performs a periodic motion around its mean position from which it differs by at most $1 0 \mathrm { m }$ . This motion is known as polar motion and can be understood by considering a rotationally symmetric gyroscope, in which the rotation axis moves around the axis of figure in the absence of external torques.

# 5.4.2 Free Eulerian Precession

In a body-fixed coordinate system $( e _ { 1 } , e _ { 2 } , e _ { 3 } )$ that is aligned with the principal axes of inertia the angular momentum $l ^ { \prime }$ of a symmetric gyroscope is given by

$$
l ^ { \prime } = \left( \begin{array} { c c c } { { A } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { A } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { C } } \end{array} \right) ~ \omega ~ ,
$$

where $\omega$ is the instantaneous rotation axis and where $A$ and $C$ are the moments of inertia for a rotation around the $e _ { 1 }$ - or $e _ { 2 }$ -axis and the $e _ { 3 }$ -axis, respectively. Without external torques the angular momentum $\imath$ is constant in an inertial reference system, but since $\scriptstyle { l ^ { \prime } }$ refers to a rotating system it obeys the relation

$$
\frac { d l } { d t } = \frac { d l ^ { \prime } } { d t } + \omega \times l ^ { \prime } = 0 .
$$

Upon insertion this yields Euler’s equations

$$
\begin{array} { l r } { \displaystyle { \cal A } \frac { d \omega _ { 1 } } { d t } + \left( C - { \cal A } \right) \omega _ { 2 } \omega _ { 3 } } & { = } & { 0 } \\ { \displaystyle { \cal A } \frac { d \omega _ { 2 } } { d t } - \left( C - { \cal A } \right) \omega _ { 1 } \omega _ { 3 } } & { = } & { 0 } \\ { \displaystyle C \frac { d \omega _ { 3 } } { d t } } & { = } & { 0 } \end{array}
$$

for the motion of $\omega$ with respect to the body-fixed coordinate system in the specialized case of a symmetric gyroscope. While the third equation implies a constant component of $\omega$ around the symmetry axis $e _ { 3 }$ , the solution of the first two equations is given by

$$
\begin{array} { r c l } { { \omega _ { 1 } } } & { { = } } & { { a \cos \left( { \displaystyle \frac { C - A } { A } } \omega _ { 3 } t + b \right) } } \\ { { } } & { { } } & { { } } \\ { { \omega _ { 2 } } } & { { = } } & { { a \sin \left( { \displaystyle \frac { C - A } { A } } \omega _ { 3 } t + b \right) ~ . } } \end{array}
$$

The instantaneous rotation vector therefore describes a circle around the $e _ { 3 }$ -axis, where the radius $a$ and phase $b$ are fixed by the initial conditions. The period

$$
P = { \frac { 2 \pi } { \omega _ { 3 } } } { \frac { A } { C - A } }
$$

depends on the angular velocity and the flattening of the gyroscope as expressed by the fraction of the moments of inertia. For the Earth, the dynamical flattening $C / ( C - A )$ as derived from the observed precession rate (cf. Sect. 5.3.1) amounts to 0.00326, which yields a period of 305 days.

# 5.4.3 Observation and Extrapolation of Polar Motion

Observations show that the Earth’s polar motion is actually a superposition of two components. One is the free precession with a period of about 435 days (the Chandler period) that is not, however, in accord with the expected 305 day period and can only be explained by a non-rigid Earth model. The second part is an annual motion that is induced by seasonal changes of the Earth’s mass distribution due to air and water flows.

In contrast to precession and nutation the motion of the rotation axis with respect to the surface of the Earth cannot, therefore, be predicted from theory but has to be monitored by continuous observations. For this purpose the mean position of the pole of rotation during the years 1900 to 1905 is usually chosen as the origin for polar motion measurements. Historically two slightly differing reference points have been employed by various institutions. The CIO (Conventional International Origin) is defined by the location of five stations of the International Latitude Service (ILS) that has been involved in polar motion measurements from the beginning of the century, whereas the BIH pole was later adopted by the Bureau International de l’Heure. The difference between the two definitions is estimated to be less than $1 \mathrm { m }$ (Groten 1984). Following the introduction of the International Terrestrial Reference System (ITRS) all polar motion data have consistently been referred to the IERS Reference Pole (IRP), which was initially aligned with the BIH pole in 1984.0.

![](images/6a30303247de7703e40e832814ede787216bf5c02d23bbba2058f6244c5bc626.jpg)  
Fig. 5.10. Due to polar motion the Celestial Ephemeris Pole (CEP) performs a periodic oscillation around the IERS Reference Pole (IRP). The superposition of the annual oscillation and the Chandlerian free precession results in a pronounced beat frequency of roughly 5–6 six years. In addition, the CEP exhibits a secular motion in the $y$ -direction

Examples of polar motion observations are given in Fig. 5.10 which shows the coordinates $x _ { \mathrm { p } }$ and $y _ { \mathrm { p } }$ of the Celestial Ephemeris Pole with respect to the IERS Reference Pole as a function of time. The $x$ and $y$ -axes are aligned with the IERS Reference Meridian (Greenwich meridian) and the $9 0 ^ { \circ }$ -West meridian. A displacement of $0 . 1$ corresponds to $3 \mathrm { m }$ on the surface of the Earth. Since 1900 the mean position of the pole has shifted by about $1 0 \mathrm { m }$ due to small changes in the Earth’s mass distribution (cf. Fig. 5.10). As a result of this motion, which is known as polar wander, the observed oscillation of the rotation axis is no longer symmetric with respect to the adopted CIO/BIH-pole. The superposition of the annual oscillation and the free precession is evident from the frequency spectrum of polar motion shown in Fig. 5.11. Both contributions are of near-equal magnitude and almost cancel each other with a beat period of 5 to 6 years (cf. Fig. 5.10). Current values of the pole coordinates are published on a monthly basis in Bulletin B (cf. Fig. 5.4) of the International Earth Rotation Service with a resolution of one and five days, respectively. From these data intermediate values for any time may be obtained by quadratic interpolation with sufficient accuracy.

![](images/4ee16cf0f6e7b225f2a23a17f98b1e2a50f5fe7c162f84596a6e603544a58708.jpg)  
Fig. 5.11. The polar motion frequency spectrum for the $x _ { \mathrm { p } }$ coordinate (continuous line) and the $y _ { \mathrm { p } }$ coordinate (dashed line) clearly shows the annual and the Chandlerian period

Even though polar motion cannot rigorously be predicted, an extrapolation over a certain interval is nevertheless possible from previous data. For this purpose the motion of the pole may be modeled as a superposition of a linear motion (polar wander), an oscillation with a period of 365.25 days (annual term), and an oscillation with a period of 435 days (Chandler term). Appropriate coefficients that provide an extrapolation of tabulated polar motion data with an accuracy of about $0 . 0 1$ over one month are published twice per week in IERS Bulletin A issued jointly by the IERS and US National Earth Orientation Service (NEOS). Similar predictions are also provided by the US National Imagery and Mapping Agency (NIMA) as part of the GPS precise ephemeris generation process (NIMA 1999).

For a prediction over longer time scales a more flexible model has been proposed by Chao (1985). The two components of polar motion are represented by time-

dependent functions

$$
\begin{array} { r c l } { x _ { \mathrm { p } } } & { = } & { a _ { x } + b _ { x } t + c _ { \mathrm { a x } } \cos ( 2 \pi t / P _ { \mathrm { a x } } + \phi _ { \mathrm { a x } } ) + c _ { \mathrm { c x } } \cos ( 2 \pi t / P _ { \mathrm { c x } } + \phi _ { \mathrm { c x } } ) } \\ { y _ { \mathrm { p } } } & { = } & { a _ { y } + b _ { y } t + c _ { \mathrm { a y } } \sin ( 2 \pi t / P _ { \mathrm { a y } } + \phi _ { \mathrm { a y } } ) + c _ { \mathrm { c y } } \sin ( 2 \pi t / P _ { \mathrm { c y } } + \phi _ { \mathrm { c y } } ) } \end{array}
$$

with a total of 16 free parameters $a _ { x } , \ldots , \phi _ { \mathrm { c y } }$ that are obtained from a least-squares fit to six years of past polar motion data. By allowing for different annual and Chandlerian periods $P _ { \mathrm { a } }$ and $P _ { \mathrm { c } }$ as well as different phases $\phi _ { \mathrm { a } }$ and $\phi _ { \mathrm { c } }$ in the $x$ - and $y$ -component of polar motion some additional degrees of freedom are introduced in this model that improve the prediction in times of notable period changes (e.g. starting in 1977). Within a one-year prediction interval an accuracy of $0 . ^ { \prime \prime } 0 2 5$ can thus be achieved.

# 5.4.4 Transformation to the International Reference Pole

Based on the previous discussion, the transformation from true-of-date coordinates (as defined by the theory of precession and nutation) to the International Terrestrial Reference System may be expressed as

$$
r _ { \mathrm { I T R F } } = \pmb { \cal I } ( t ) \pmb { \theta } ( t ) r _ { \mathrm { t o d } } .
$$

Here $\mathbf { \sigma } _ { \Theta }$ (cf. (5.67)) describes the Earth’s rotation about the CEP axis, while

$$
\begin{array} { r } { \pmb { \cal I } _ { \mathbf { \Lambda } } = \pmb { \cal R } _ { y } ( - x _ { \mathrm { p } } ) \pmb { \cal R } _ { x } ( - y _ { \mathrm { p } } ) \approx \left( \begin{array} { c c c } { 1 } & { 0 } & { + x _ { \mathrm { p } } } \\ { 0 } & { 1 } & { - y _ { \mathrm { p } } } \\ { - x _ { \mathrm { p } } + y _ { \mathrm { p } } } & { 1 } \end{array} \right) } \end{array}
$$

accounts for polar motion and describes the subsequent transition to the International Reference Pole and Meridian. In view of the small angles involved $\mathrm { 0 . } 3 \approx$ $1 . 5 \mu$ rad), second order terms can safely be neglected in the expansion of the trigonometric functions and the linearized form of $\pi$ is fully adequate for all applications.

# 5.5 Geodetic Datums

Besides the International Terrestrial Reference System and its annually updated realizations ITRFyy, a variety of other global geodetic datums are in widespread use. Common to all systems is the goal of establishing a global coordinate system that originates at the Earth’s center of mass and is closely aligned with the Greenwich meridian and the adopted pole.

The World Geodetic System 1972 (WGS72) and 1984 (WGS84) have been established by the United States Department of Defense (DoD) and the Defence Mapping Agency9 (DMA) for use with the TRANSIT and GPS satellite navigation systems. WGS84, in its initial realization, was itself based on reference station coordinates obtained by TRANSIT Doppler measurements and achieved a global accuracy of 1–2 meters. To improve its precision, two new realizations named WGS84 (G730) and WGS84 (G873) were established (Malys & Slater 1994, Malys et al. 1997) based on accurate GPS positioning techniques. The revised systems are considered to agree with the ITRF on the decimeter and centimeter level (cf. NIMA 1997). Similar to the use of WGS84 in GPS applications, the Russian GLONASS system employs a specific datum known as PZ-90 reference frame (ICD-GLONASS 1998).

Table 5.3. Helmert transformation parameters for global geodetic datums. References: (a) McCarthy 1992, (b) McCarthy 1996, (c) Cunningham & Curtis 1996, (d) Mitrikas et al. 1998   

<table><tr><td rowspan="2">From</td><td rowspan="2">To</td><td colspan="2">T1 T2</td><td rowspan="2">T</td><td rowspan="2">D 10-9</td><td rowspan="2">R1</td><td colspan="2">R2 0&#x27;001</td><td rowspan="2">Ref.</td></tr><tr><td>[cm]</td><td>[cm] [cm]</td><td>0&#x27;001</td><td>0&quot;001</td></tr><tr><td>ITRF90</td><td>WGS72</td><td>+6.0</td><td>-51.7</td><td>-472.3</td><td>-231</td><td>+18.3</td><td></td><td>-0.3 +547.0</td><td>(a)</td></tr><tr><td>ITRF90</td><td>WGS84</td><td>+6.0</td><td>-51.7</td><td>-22.3</td><td>-11</td><td>+18.3</td><td>-0.3</td><td>-7.0</td><td>(a)</td></tr><tr><td>ITRF90</td><td>ITRF88</td><td>+0.0</td><td>-1.2</td><td>-6.2</td><td>+6</td><td>+0.1</td><td>0.0</td><td>0.0</td><td>(a)</td></tr><tr><td>ITRF94</td><td>ITRF88</td><td>+1.8</td><td>0.0</td><td>-9.2</td><td>+7.4</td><td>+0.1</td><td>0.0</td><td>0.0</td><td>(b)</td></tr><tr><td>ITRF94</td><td>ITRF90</td><td>+1.8</td><td>1.2</td><td>-3.0</td><td>+0.9</td><td>0.0</td><td>0.0</td><td>0.0</td><td>(b)</td></tr><tr><td>ITRF94</td><td>ITRF92</td><td>+0.8</td><td>0.2</td><td>-0.8</td><td>-0.8</td><td>0.0</td><td>0.0</td><td>0.0</td><td>(b)</td></tr><tr><td></td><td>ITRF94 WGS84(G730)</td><td>-2</td><td>+2</td><td>-1</td><td>+0.2</td><td>+2.5</td><td>+1.9</td><td>-2.5</td><td>（c）</td></tr><tr><td></td><td>ITRF94 WGS84(G873)</td><td>+1</td><td>-1</td><td>-2</td><td>+0.3</td><td>+0.6</td><td>+1.2</td><td>+0.7</td><td>（c）</td></tr><tr><td>WGS84</td><td>PZ-90</td><td>+47</td><td>+51</td><td>+156</td><td>-22</td><td>+15.7</td><td>+3.5</td><td>-356</td><td>(d)</td></tr></table>

Except for statistical errors in the associated station coordinates, the relation between different datums may be expressed by an infinitesimal seven-parameter transformation. This is known as Helmert transformation and accounts for an offset in the adopted origin $( T _ { 1 , 2 , 3 } )$ , a scale difference $( D )$ and a misalignment of the coordinate axes $( R _ { 1 , 2 , 3 } )$ . Given the coordinates $r$ in the original system, the coordinates in another system may be expressed as

$$
\begin{array} { r } { \pmb { r } ^ { \prime } = \left( \begin{array} { l } { T _ { 1 } } \\ { T _ { 2 } } \\ { T _ { 3 } } \end{array} \right) + \left( \begin{array} { l l l } { 1 + D } & { - R _ { 3 } } & { + R _ { 2 } } \\ { + R _ { 3 } } & { 1 + D } & { - R _ { 1 } } \\ { - R _ { 2 } } & { + R _ { 1 } } & { 1 + D } \end{array} \right) \pmb { r } } \end{array} .
$$

Sample parameters for common transformations are provided in Table 5.3. In view of different conventions for the names and signs of the transformation parameters, care should be taken when applying the above equation with other parameter sets.

Supplementary to the Cartesian coordinates in the terrestrial reference system the location of points on or near the surface of the Earth is commonly expressed in terms of geodetic coordinates relative to a chosen reference ellipsoid. The geodetic longitude $\lambda$ is identical to the geocentric longitude and measures the angle between the Greenwich meridian (or the International Reference Meridian) and the meridian through the point. By convention $\lambda$ is counted positive towards the east of Greenwich. Unlike the geocentric latitude $\varphi ^ { \prime }$ that specifies the inclination of the position vector with respect to the equatorial plane, the geodetic latitude $\varphi$ gives the angle between the Earth’s equator and the normal to the reference ellipsoid. It thus equals the elevation of the north celestial pole above the local tangent plane.

![](images/e243bf1c423a220d6d1d7f7bcbebab92463f1cbc5582487c37668f7987c35aca.jpg)  
Fig. 5.12. Geocentric and geodetic latitude

The reference ellipsoid is rotationally symmetric and any plane through the symmetry axis intersects the ellipsoid in an ellipse of flattening $f$ which is defined by the relative difference of the equatorial radius and the polar radius:

$$
f = \frac { R _ { \oplus } - R _ { \mathrm { p o l e } } } { R _ { \oplus } } ~ .
$$

All points on the Greenwich meridian therefore obey the relation

$$
x ^ { 2 } + { \frac { z ^ { 2 } } { ( 1 - f ) ^ { 2 } } } = R _ { \oplus } ^ { 2 } ~ ,
$$

which may also be written in the differenced form as

$$
\frac { d z } { d x } = - ( 1 - f ) ^ { 2 } \frac { x } { z } .
$$

On the other hand

$$
{ \frac { d z } { d x } } = - { \frac { 1 } { \tan \varphi } }
$$

according to the definition of $\varphi$ , and by equating both expressions one obtains

$$
z = x \left( 1 - f \right) ^ { 2 } \tan \varphi .
$$

Inserting this relation into the equation of the ellipse and solving for $x$ finally leads to

$$
\begin{array} { l l l l } { x } & { = } & { \displaystyle { R _ { \oplus } \frac { 1 } { \sqrt { 1 + ( 1 - f ) ^ { 2 } \tan ^ { 2 } \varphi } } } } & { = } & { \displaystyle { R _ { \oplus } \frac { \cos \varphi } { \sqrt { 1 - f ( 2 - f ) \sin ^ { 2 } \varphi } } } } \\ { z } & { = } & { \displaystyle { R _ { \oplus } \frac { ( 1 - f ) ^ { 2 } \tan \varphi } { \sqrt { 1 + ( 1 - f ) ^ { 2 } \tan ^ { 2 } \varphi } } } } & { = } & { \displaystyle { R _ { \oplus } \frac { ( 1 - f ) ^ { 2 } \sin \varphi } { \sqrt { 1 - f ( 2 - f ) \sin ^ { 2 } \varphi } } } } \end{array} .
$$

This relation between Cartesian and geodetic coordinates may easily be generalized for arbitrary points yielding

$$
r ~ = ~ \left( \begin{array} { r } { { ( N + h ) \cos \varphi \cos \lambda } } \\ { { ( N + h ) \cos \varphi \sin \lambda } } \\ { { ( ( 1 - f ) ^ { 2 } N + h ) \sin \varphi } } \end{array} \right) \quad ,
$$

where

$$
N = { \frac { R _ { \oplus } } { \sqrt { 1 - f ( 2 - f ) \sin ^ { 2 } \varphi } } }
$$

is an auxiliary quantity that is illustrated in Fig. 5.12 and where $h$ is the height above the reference ellipsoid.

While the computation of Cartesian coordinates from given geodetic coordinates is fairly simple, the inverse transformation is slightly more involved. Besides direct methods that involve the solution of a quartic equation (Borkowski 1989, Bowring 1985) there are several iterative methods, which usually converge rapidly. The method described here utilizes the quantity

$$
\varDelta z = ( N + h ) \sin \varphi - z = N e ^ { 2 } \sin \varphi ,
$$

where

$$
e = { \sqrt { 1 - ( 1 - f ) ^ { 2 } } }
$$

stands for the eccentricity of the reference ellipsoid. Initially $\varDelta z$ is set to $e ^ { 2 } z$ , which is a good approximation for all points that are reasonably close to the surface of the Earth. Improved values are then calculated from

$$
\begin{array} { l c l } { \sin \varphi } & { = } & { \displaystyle \frac { z + \varDelta z } { \sqrt { x ^ { 2 } + y ^ { 2 } + ( z + \varDelta z ) ^ { 2 } } } } \\ { N } & { = } & { \displaystyle \frac { R _ { \oplus } } { \sqrt { 1 - e ^ { 2 } \sin ^ { 2 } \varphi } } } \\ { \varDelta z } & { = } & { N e ^ { 2 } \sin \varphi \quad , } \end{array}
$$

until the iteration converges. The geodetic longitude and latitude and the height above the reference ellipsoid may then be calculated from

$$
\begin{array} { l l l } { { \lambda } } & { { = } } & { { \arctan \left( \frac { y } { x } \right) } } \\ { { \varphi } } & { { = } } & { { \arctan \left( \frac { z + \varDelta z } { \sqrt { x ^ { 2 } + y ^ { 2 } } } \right) } } \\ { { h } } & { { = } } & { { \sqrt { x ^ { 2 } + y ^ { 2 } + ( z + \varDelta z ) ^ { 2 } } - N , } } \end{array}
$$

Table 5.4. Common reference ellipsoids   

<table><tr><td rowspan=1 colspan=2>Datum</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>1/f</td><td rowspan=1 colspan=2>Reference</td></tr><tr><td rowspan=1 colspan=2>GEM-10B</td><td rowspan=1 colspan=1>6378138m</td><td rowspan=1 colspan=1>298.257</td><td rowspan=5 colspan=2>McCarthy 1992McCarthy 1992McCarthy 1992NIMA 1997McCarthy1996,Moritz 1980ICD-GLONASS 1998</td></tr><tr><td rowspan=1 colspan=2>GEM-T3WGS72</td><td rowspan=1 colspan=1>6378137m6378135m</td><td rowspan=1 colspan=1>298.257298.26</td></tr><tr><td rowspan=1 colspan=2>WGS84</td><td rowspan=1 colspan=1>6378137m</td><td rowspan=3 colspan=1>298.257223563298.257222101298.257839303</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>NIMA 1997</td></tr><tr><td rowspan=1 colspan=1>ITRF (GRS-80)</td><td rowspan=1 colspan=1>-80）</td><td rowspan=1 colspan=1>6378137m</td></tr><tr><td rowspan=1 colspan=2>PZ-90</td><td rowspan=1 colspan=1>6378136m</td></tr></table>

which follows immediately from Fig. 5.12. It is noted that the above relations are singular for points on the $z$ -axis, which is likewise the case for many direct methods (see e.g. Seidelmann 1992).

Since the difference between the Earth’s equatorial and polar radii is less than $2 2 \mathrm { k m }$ , the flattening $f \approx 1 / 2 9 8 . 2 5 7$ is a very small quantity and the difference between geodetic and geocentric latitudes amounts to twelve arcminutes at most. To a first approximation

$$
\varphi = \varphi ^ { \prime } + f \sin ( 2 \varphi ^ { \prime } ) ~ ,
$$

which shows that the difference between $\varphi$ and $\varphi ^ { \prime }$ reaches its maximum for intermediate latitudes but vanishes at the poles and the equator. Numerical values of the inverse flattening for various datums and reference ellipsoid are presented in Table 5.4.

# Exercises

Exercise 5.1 (ICRS to ITRS Transformation) Compute the transformation from the International Celestial Reference System (or the mean equator and equinox of J2000) to the International Terrestrial Reference System (or the reference pole and Greenwich meridian) for the epoch 1999 March 4, $0 ^ { \mathrm { h } }$ UTC.

Hint: Obtain Terrestrial Time (TT) and Universal Time 1 (UT1) as well as pole coordinates at the time of interest from the respective IERS bulletins (cf. Figs. 5.4 and 5.5). Employ the IAU 1976 precession theory and the IAU 1980 nutation theory to compute the instantaneous orientation of the Celestial Ephemeris Pole (neglecting any corrections to the nutation angles). In computing the Earth rotation transformation account for the conventional relation between UT1 and GMST as well as the first-order term of the equation of the equinoxes.

Solution: The IERS Bulletins B (No. 135) and C (No. 16) provide the following Earth orientation parameters and derived quantities:

Using the above assumptions, the following step-by-step transformation matrices for precession $( P )$ , nutation $( N )$ , Earth rotation $( \pmb { \theta } )$ , and polar motion $( \pmb { I } )$ are obtained:

Multiplication then yields the matrix

$$
U _ { \mathrm { T R S } } ^ { \mathrm { I C R S } } = \pi \theta \ : N \ : P = \left( \begin{array} { l l l } { { - 0 . 9 4 7 3 7 8 0 3 } } & { { + 0 . 3 2 0 1 1 6 9 6 } } & { { - 0 . 0 0 0 0 8 4 3 1 } } \\ { { - 0 . 3 2 0 1 1 6 9 6 } } & { { - 0 . 9 4 7 3 7 8 0 3 } } & { { - 0 . 0 0 0 0 6 3 6 3 } } \\ { { - 0 . 0 0 0 1 0 0 2 4 } } & { { - 0 . 0 0 0 0 3 3 3 0 } } & { { + 0 . 9 9 9 9 9 9 9 9 } } \end{array} \right)
$$

that describes the full ICRS to ITRS transformation.

Exercise 5.2 (Velocity in the Earth-fixed Frame) The GPS precise ephemerides of the National Imagery and Mapping Agency (NIMA) provide the state vectors of the GPS satellites in an Earth-fixed reference system (presently WGS84 (G873)). This frame is considered as rotating, which implies that the rotation of the axes must be considered in the transformation of the velocity vector, i.e.

$$
\begin{array} { r c l } { { r _ { \mathrm { W G S } } } } & { { = } } & { { { \cal U } _ { \mathrm { W G S } } ^ { \mathrm { I C R S } } ( t ) r _ { \mathrm { I C R S } } } } \\ { { } } & { { } } & { { } } \\ { { { \displaystyle v _ { \mathrm { W G S } } } } } & { { = } } & { { { \cal U } _ { \mathrm { W G S } } ^ { \mathrm { I C R S } } ( t ) v _ { \mathrm { I C R S } } + \frac { d { \cal U } _ { \mathrm { W G S } } ^ { \mathrm { I C R S } } ( t ) } { d t } r _ { \mathrm { I C R S } } . } } \end{array}
$$

Given the state vector

$$
\begin{array} { r c l } { { r \mathrm { w g s } } } & { { = } } & { { ( \phantom { - } 1 9 4 4 0 . 9 5 3 8 0 5 , ~ 1 6 8 8 1 . 6 0 9 2 7 3 , ~ - 6 7 7 7 . 1 1 5 0 9 2 ) \mathrm { ~ k m } } } \\ { { } } & { { } } & { { } } \\ { { v \mathrm { w g s } } } & { { = } } & { { ( - 0 . 8 1 1 1 8 2 7 4 5 6 , - 0 . 2 5 7 3 7 9 9 1 3 7 , - 3 . 0 6 8 9 5 0 8 1 2 5 ) \mathrm { ~ k m / s } } } \end{array}
$$

of satellite PRN 15 at epoch 1999 March 4, $0 ^ { \mathrm { h } }$ GPS time, compute the position and velocity vector in the International Celestial Reference System (mean equator and equinox of J2000). Check your result by showing that the corresponding orbital elements describe a near-circular orbit with a twelve-hour period $( a \approx 2 6 5 6 0 \mathrm { k m } )$ ) and an inclination of about $5 6 ^ { \circ }$ .

Hint: The WGS84 (G873) frame is identical to the International Terrestrial Reference Frame within an accuracy of a few centimeters. In computing the derivative of the ICRS to ITRS transformation, the precession, nutation and polar motion matrix may be considered as constant, i.e.

$$
\frac { d { \cal U } _ { \mathrm { I T R S } } ^ { \mathrm { I C R S } } ( t ) } { d t } \approx \pi \frac { d \Theta } { d t } N { \cal P } .
$$

Furthermore, the time derivative of the Earth rotation matrix is given by

$$
\frac { d \pmb { \theta } ( t ) } { d t } = \omega _ { \oplus } \left( \begin{array} { l l l } { 0 } & { + 1 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) \pmb { \theta } ( t )
$$

where

$$
\omega _ { \oplus } = { \frac { d ( { \mathrm { G A S T } } ) } { d t } } \approx 1 . 0 0 2 7 3 7 9 0 9 3 5 0 7 9 5 { \frac { 2 \pi } { 8 6 4 0 0 { \mathrm { s } } } } = 7 . 2 9 2 1 1 5 8 5 5 3 \cdot 1 0 ^ { - 5 } { \mathrm { s } } ^ { - 1 }
$$

(cf. (5.19)) is the Earth’s angular velocity. IERS Earth orientation parameters for the date of interest are provided in the previous exercise.

Solution: The GPS–UTC time difference amounts to $1 3 \mathrm { s }$ , which results in the ICRS-ITRS transformation matrix

$$
U = \left( \begin{array} { l l l } { { - 0 . 9 4 7 0 7 4 1 4 } } & { { + 0 . 3 2 1 0 1 4 9 1 } } & { { - 0 . 0 0 0 0 8 4 2 5 } } \\ { { - 0 . 3 2 1 0 1 4 9 1 } } & { { - 0 . 9 4 7 0 7 4 1 4 } } & { { - 0 . 0 0 0 0 6 3 7 1 } } \\ { { - 0 . 0 0 0 1 0 0 2 4 } } & { { - 0 . 0 0 0 0 3 3 3 0 } } & { { + 0 . 9 9 9 9 9 9 9 9 } } \end{array} \right)
$$

and in its derivative

$$
\dot { U } = \left( \begin{array} { c c c } { { - 0 . 2 3 4 0 8 7 7 9 } } & { { - 0 . 6 9 0 6 1 7 4 4 } } & { { - 0 . 0 0 0 0 4 5 6 1 } } \\ { { + 0 . 6 9 0 6 1 7 4 3 } } & { { - 0 . 2 3 4 0 8 7 7 9 } } & { { + 0 . 0 0 0 0 6 1 6 7 } } \\ { { + 0 . 0 0 0 0 0 0 8 9 } } & { { - 0 . 0 0 0 0 0 0 0 5 } } & { { + 0 . 0 0 0 0 0 0 0 0 } } \end{array} \right) \cdot 1 0 ^ { - 4 } / \mathrm { s }
$$

Then

$$
\begin{array} { l c l } { { r _ { \mathrm { I C R S } } } } & { { = } } & { { U ^ { T } r _ { \mathrm { W G S } } } } \\ { { } } & { { = } } & { { ( - 2 3 8 3 0 . 5 9 3 , - 9 7 4 7 . 0 7 4 , - 6 7 7 9 . 8 2 9 ) \ \mathrm { k m } } } \\ { { } } & { { } } & { { } } \\ { { v _ { \mathrm { I C R S } } } } & { { = } } & { { U ^ { T } v _ { \mathrm { W G S } } + \dot { U } ^ { T } r _ { \mathrm { W G S } } } } \\ { { } } & { { } } & { { ( + 1 . 5 6 1 9 6 4 , - 1 . 7 5 4 3 4 6 , - 3 . 0 6 8 8 5 1 ) \ \mathrm { k m / s } } } \end{array}
$$

is the state vector in the inertial celestial reference system. The associated osculating orbital elements of the GPS satellite are obtained as

Semimajor axis a 26561.013 km Eccentricity $e$ 0.0070606 Inclination $i$ 56.338◦ RA ascend. node $\varOmega$ 12.146◦ Arg. of perigee ω 87.617◦ Mean anomaly M 109.435◦

which matches the specified orbital characteristics of the GPS space segment.

Exercise 5.3 (Geodetic coordinates) The Cartesian coordinates of the NIMA GPS receiver at Diego Garcia are given by

$$
r _ { \mathrm { W G S 8 4 ( G 8 7 3 ) } } = ( + 1 9 1 7 0 3 2 . 1 9 0 , + 6 0 2 9 7 8 2 . 3 4 9 , - 8 0 1 3 7 6 . 1 1 3 ) \mathrm { ~ m }
$$

at epoch 1997.0 (Cunningham & Curtis 1996). Compute the corresponding geodetic coordinates using the WGS84 reference ellipsoid.

Solution:

East longitude λ $+ 7 2 . 3 6 3 1 2 0 9 4 ^ { \circ }$ Latitude $\varphi$ $- 7 . 2 6 6 5 4 9 9 9 ^ { \circ }$ Height $h$ = $- 6 3 . 6 6 7 \mathrm { m }$ .

# 6. Satellite Tracking and Observation Models

# 6.1 Tracking Systems

Orbit determination of an artificial satellite requires as input measurements that are related to the satellite’s position or velocity. These data are collected by a satellite tracking system that measures the properties of electromagnetic wave propagation between the transmitter and the receiver. The transmitter as well as the receiver may either be a ground station or a satellite.

# 6.1.1 Radar Tracking

Since the early times of spaceflight radar techniques have been utilized to gather information on the position and velocity of artificial satellites. Restricting to a simple configuration with one ground station and one satellite:

1. the pointing angles in the topocentric system of the ground station are obtained by measuring the direction of the maximum signal amplitude of the spacecraft;   
2. the slant range or distance from the satellite to the station is computed from the round-trip light time of a radar signal emitted from the ground station antenna to the satellite and radiated back to the station;   
3. the range rate or line-of-sight velocity of the spacecraft relative to the ground station can be derived from the Doppler shift of a radar wave emitted from the ground station, transponded by the satellite, and received again at the ground station.

In many cases range and range rate measurements are two-way measurements with a ground station serving as transmitter and receiver. This is related to the fact that only few satellites are equipped with high-precision time and frequency standards to perform one-way range (high-precision transmit time required) or one-way Doppler (high-precision transmit frequency required) measurements. In case of ground-based two-way measurements the transmit time and frequency as well as the reception time and frequency are determined very accurately using the high-precision ground station equipment. In the sequel a variety of different radar tracking systems and principles is addressed in more detail.

# Angle Measurements

To determine the direction towards a radio signal emitted by the satellite, the ground antenna has to automatically follow the satellite beacon (autotrack mode). This may be achieved using the conical scan method, where the antenna feed performs a slight rotation in such a way that the cone always covers the direction to the satellite. The amplitude modulation of the received signal leads to an error signal that can be used to steer the antenna.

![](images/a4177fd6d2fb0a7fa9bb595a252e4816f9d61eb69875584bba483c72520bbb35.jpg)  
Fig. 6.1. Antenna beams of a monopulse autotrack system (left) and associated sum and difference signals (right)

The monopulse technique derives antenna-angle offsets by the extraction of two signals from the satellite beacon: the difference signal $\varDelta$ and the sum signal $\varSigma$ , which are illustrated in Fig. 6.1 (see Hartl 1977). There are two different methods to obtain these signals:

a feed network attached to the radiator system measures the incident direction of the satellite signals. By differencing and summation of the individual feed outputs the difference and sum signals are derived. This technique is hardware-intensive, since it requires several feed units. • a single feed such as a corrugated horn is applied. The incoming satellite signal generates low and high-oscillation modes. High modes are excited on the horn aperture by the asymmetry of the received wavefront caused by the antenna pointing error and extracted by a mode coupler. These error signals are similar to signals obtained with differencing techniques.

The sum signal is essentially applied as a reference for the error signal. The amplitude of the difference signal is proportional to the amplitude of the antenna-angle offset, while the phase of the difference signal corresponds to the direction of the offset. The error signal together with the sum signal is fed to a tracking unit to provide azimuth and elevation error outputs. The difference signal is, in contrast to the sum signal, extremely sensitive to the antenna angle offset (cf. Fig. 6.1) and may therefore be used to precisely measure the antenna angle offset and to control the antenna motion.

![](images/80b0f897970d811d519cea5007f996a2420fa2c43c2d482eced8bc6ee835ffcb.jpg)

![](images/9713a259939606fd6ba3b6f12db0784ef46daf44cfa0639fc8fe06077d0bcc6f.jpg)

![](images/424f7f4b603dafd9ea8dc64e43f394899f3c4322ab41b041775ccbfe3532dff2.jpg)  
Fig. 6.2. Methods of radar range and range rate tracking

The angle measurement errors depend essentially on the beamwidth of the ground station antenna. The beamwidth itself depends linearly on the carrier frequency of the satellite signal and the inverse of the antenna diameter. For an antenna of $1 5 \mathrm { ~ m ~ }$ diameter the $3 \mathrm { \ d B }$ beamwidth amounts to $0 . 6 ^ { \circ }$ at $2 0 0 0 ~ \mathrm { M H z }$ (Sband). Nevertheless, a resolution of about $5 0 ^ { \prime \prime }$ can be achieved in combination with a monopulse tracking system. At $\mathrm { K _ { u } }$ -band ( $1 4 0 0 0 \mathrm { M H z } )$ an accuracy of $1 0 ^ { \prime \prime }$ (0.05 mrad) may be obtained with an antenna of $1 0 \mathrm { m }$ diameter that is commonly used for the control of geostationary communications satellites. Depending on the altitude, the position of a spacecraft can be obtained with accuracies between $1 0 0 \mathrm { m }$ and $5 0 0 0 \mathrm { m }$ using typical angle tracking systems.

In general, angle measurements are severely affected by systematic errors that are due to calibration deficiencies, thermoelastic distortions, and wind or snow loads. Within an orbit determination the systematic angle errors may partially be absorbed by the estimation of angle measurement biases, although the error sources lead, in general, to varying angle errors.

# Ranging

The classical two-way radar ranging employs a ranging signal that is radiated from the ground station to the satellite. A satellite transponder is required to receive the signal and to transmit it back to the ground station (see Fig. 6.2a). The ground station receives the transponded ranging signal from the satellite and determines the signal travel time $\tau$ . This is expressed as an equivalent range value $\rho = 1 / 2 { \cdot } c \tau$ , which is equal to the average of the uplink and downlink distance.

![](images/afc69768fc5f5d39e7eae64ae014fde00b872eb529720ed985ada8910e559a1a.jpg)  
Fig. 6.3. Principle of distance measurements using tone ranging (left) and code ranging (right)

There are basically two different techniques to generate ranging signals. Common tone-ranging systems modulate the carrier signal with a sine wave of frequency $f _ { 0 } \approx 1 0 0 \mathrm { k H z }$ , which is known as major tone. Upon reception, the ranging demodulator locks onto the incoming tone and determines its phase with respect to the outgoing tone (Fig. 6.3). The phase shift $\varDelta \phi$ is directly proportional to the turnaround signal travel time

$$
\tau = { \frac { \varDelta \phi } { 2 \pi f _ { 0 } } }
$$

and can be measured with a resolution of about $\sigma _ { \phi } = 1 0 ^ { - 2 } \mathrm { c y c } = 2 \pi \cdot 1 0 ^ { - 2 }$ rad. As a result, the two-way range is obtained with a typical accuracy of $\sigma _ { \rho } = 1 0 ^ { - 2 } c / ( 2 f _ { 0 } ) =$ $1 5 \mathrm { m }$ . Because the phase shift can only be measured in the interval $[ 0 , 2 \pi ]$ , the range measurements suffer from an indetermination or ambiguity of

$$
\Delta \rho = { \frac { c } { 2 f _ { 0 } } } ~ ,
$$

which amounts to $1 5 0 0 \mathrm { m }$ in the given example. To overcome this difficulty, the ranging signal is supplemented by a series of sub-harmonic minor tones, which are derived from the major tone and coherently modulated on the carrier. A representative sequence of major and minor tones is given by the frequencies $f _ { 0 } = 1 0 0 \mathrm { k H z }$ , $f _ { 1 } = 2 0 \mathrm { k H z }$ , $f _ { 2 } = 4 \mathrm { k H z }$ , $f _ { 3 } = 8 0 0 \mathrm { H z }$ , $f _ { 4 } = 1 6 0 \mathrm { H z }$ , $f _ { 5 } = 3 2 \mathrm { H z }$ , and $f _ { 6 } = 8 \ : \mathrm { H z }$ (Zarrouati 1987). Here, the turn-around time can uniquely be measured up to a value of $1 / 8 \mathrm { s }$ as determined by the lowermost minor-tone frequency. This results in an overall range ambiguity of $a = c / ( 2 f _ { 6 } ) = 1 8 7 5 0 \mathrm { k m }$ that can readily be accepted in practice.

In contrast to harmonic signals, the code-ranging system applies a pseudonoise (PN) code that is continuously modulated onto the carrier (Fig. 6.3). The PN code consists of a random-like sequence of bits (or chips) that each take a value of zero or one. It is repeated again and again after a predefined number of bits, which is known as code length. Upon reception of the ranging signal the turnaround light time is obtained by correlating the incoming signal with a replica of the uplink code. The ranging accuracy is thus determined by the code rate (or, equivalently, the chip length), whereas the range ambiguity is given by the code length. The advantage of a code-ranging system lies in the simple acquisition of PN signals and the continuous frequency spectrum that allows sharing of the ranging signal with telecommand signals. On the other hand the acquisition time for weak signals is higher than that of tone-ranging systems and the achieved measurement accuracy may be worse, unless a pre-steering Doppler shift is used to reduce the loop bandwidth of the system (Gaudenzi et al. 1990).

# PRARE

PRARE (Precise Range and Range Rate Equipment) is a spaceborne tracking system that provides high-precision two-way range and range rate measurements (Hartl 1984). The PRARE system was developed by the Institut für Navigation (INS) of the University of Stuttgart and has been operated since 1995 aboard the European remote sensing satellite ERS-2.

The measurements are based on the signal travel time of an X-band ranging signal transmitted from the satellite, transponded by a PRARE ground-based user station, and received again by the satellite. Here the two-way signal travel time is measured, from which range data are derived (Fig. 6.2c). The Doppler shift of the X-band carrier frequency is, furthermore, measured to derive precise range rate data.

The space-based PRARE unit has dimensions $4 0 { \times } 2 1 { \times } 1 8 \ \mathrm { c m }$ and a power consumption of $3 0 \mathrm { ~ W ~ }$ in operational mode. Two crossed dipole antennas transmit continuous ranging signals to the ground segment in the S-band $( 2 2 4 8 ~ \mathrm { M H z } )$ and X-band $( 8 4 8 9 \mathrm { M H z } )$ ) as well as station-relevant information, such as visibility prediction. The ranging signals are pseudo-noise (PN) codes, modulated on the carriers with a rate of 10 MChips/s in X-band and 1 MChip/s in S-band. With a hardware resolution of 1/1000 an effective range resolution of $c 1 0 ^ { - 7 } \mathrm { s } 1 0 ^ { - 3 } \approx 3 \mathrm { c m }$ is given, while the Doppler hardware resolution is 1/1000 of the wavelength within one second, thus $c / ( 8 . 5 { \cdot } 1 0 ^ { 9 } \mathrm { H z } ) 1 0 ^ { - 3 } / \mathrm { s } \approx 0 . 0 4 \mathrm { m m / s }$ . The overall accuracy (r. m. s.) is about $6 \mathrm { c m }$ for range and $0 . 4 \mathrm { m m / s }$ for range rate at a 1 s integration time (Bedrich et al. 1997). Four independent correlators and four Doppler counters allow a simultaneous data collection from up to four stations in a code multiplexing mode.

The user-station network currently comprises a worldwide net of about 30 small transportable and automated ground stations, equipped with $6 0 \mathrm { c m }$ diameter antennas. Since the user stations measure the downlink signal travel time both in S-band and X-band, the ionospheric path delay (TEC) along the signal path may be derived and subsequently corrected within the orbit determination. The received X-band signal is then coherently transposed to $7 2 2 5 ~ \mathrm { M H z }$ , modulated with the regenerated PN code, and uplinked together with the dual frequency time delay, meteorological data at the ground site and housekeeping data.

The PRARE control segment comprises a command station, a master station, as well as a calibration station. While the command station performs the monitoring of the space system and commanding, the master station serves as central reception station, receiving the measured tracking data, time difference data from the user stations, and meteorological data from the global network. The data are processed, time-tagged to the UTC time scale, archived and disseminated to the users. The calibration station uses a laser tracking system to determine the hardware biases of the PRARE system.

# TDRSS

NASA’s Tracking and Data Relay Satellite System (TDRSS) is a constellation of six geosynchronous satellites and a ground system which provides tracking and communications support for low-Earth orbiting space vehicles. The first TDRS starting operated in 1983 and since then spacecraft like the Extreme Ultra-Violet Explorer (EUVE), the Compton Gamma Ray Observatory (CGRO), the Earth Radiation Budget Satellite (ERBS), Landsat-4, TOPEX/Poseidon, and the Space Shuttle have been tracked by TDRSS.

The space segment consists of geostationary satellites at longitudes of $4 1 ^ { \circ }$ West (TDE), $1 7 1 ^ { \circ }$ viz. $1 7 4 ^ { \circ }$ West (TDW) and, to close a gap in coverage over the Indian Ocean (zone of exclusion), $2 7 5 ^ { \circ }$ West (TDZ) (STDN 1998). Each TDRS can relay voice, television, and digital signals between a ground station and a user satellite. In the altitude regime from $1 2 0 0 ~ \mathrm { k m }$ to $3 0 0 0 ~ \mathrm { k m }$ the primary satellites TDE and TDW are sufficient to ensure continuous communication, while an $8 5 \%$ coverage can be achieved for altitudes of $2 0 0 \mathrm { k m }$ (STDN 1998). The TDRS provides links to the user spacecraft through two steerable single-access (SA) antennas with $4 . 9 \mathrm { m }$ diameter in the Ku-band and S-band. In addition a multiple-access (MA) S-band array may receive data from up to 20 satellites simultaneously and transmit to one satellite at a time. The communication to the ground is achieved using a $2 \textrm { m }$ Ku-band space-to-ground link (SGL) antenna.

The ground segment comprises the White Sands Ground Terminal (WSGT) in New Mexico, operating three $1 8 \mathrm { m }$ antennas for $\mathrm { K u }$ -band communication and one $6 \textrm { m } S$ -band antenna, as well as a second TDRSS ground terminal (STGT). The WSGT/STGT performs the tracking, telemetry, and telecommand operations for TDRSS and collects the user spacecraft data. Through the NASA ground terminal (GT) the communication with the Network Control Center (NCC) at the Goddard Space Flight Center (GSFC) is established, which manages the space network through system scheduling and TDRSS monitoring.

A TDRS allows relayed two-way range and range rate tracking of user satellites and, for user spacecraft equipped with an ultra-stable frequency reference, also precise relayed one-way range rate measurements. In case of two-way measurements, the signals are transmitted (14.6–15.25 GHz) (SN 1995) from the White Sands station to the TDRS, where they are coherently forwarded (2.1064 GHz MA, 2.0258–2.1179 GHz SA, 13.775 GHz SA) to the user spacecraft (Fig. 6.2e). The signals are transponded by the user satellite and transmitted (2.2875 GHz MA, 2.200–2.300 GHz SA, 15.0034 GHz SA) back to the TDRS, where they are relayed (13.4–14.05 GHz) to the receiving antenna at White Sands (Long et al. 1989). In the same way as the TDRS tracks a user satellite, each TDRS may also track groundbased TDRSS transponders, which are located at four different sites and are part of the Bilateration Ranging Transponder System (BRTS).

The overall quality of TDRS-relayed range and range rate data is similar to ground-based tracking. In the case of TOPEX/Poseidon the relayed two-way range and range rate residuals show a standard deviation of $2 \mathrm { m }$ and $0 . 5 \mathrm { m m } / \mathrm { s }$ (Marshall et al. 1996). The operational TDRSS orbit determination is based on relayed two-way range data from the BRTS. Due to a limited observation geometry, unmodeled ionospheric perturbations, and measurement biases, the operational TDRS trajectories are limited to $3 0 { - } 4 0 \mathrm { ~ m ~ } ( 1 \sigma )$ total position accuracies (Cox & Oza 1994). When TDRS tracking of TOPEX/Poseidon is applied together with a highly precise a priori ephemeris of TOPEX/Poseidon, the TDRS ephemerides may be determined with a total position accuracy of $1 { - } 3 \mathrm { m } ( 1 \sigma )$ (Rowlands et al. 1997).

# Doppler Tracking

The Doppler tracking of satellites is based on the frequency shift

$$
\frac { f _ { r } } { f _ { t } } = \frac { 1 - \pmb { v } _ { r } \cdot \pmb { e } / c + U _ { r } / c ^ { 2 } + \pmb { v } _ { r } ^ { 2 } / ( 2 c ^ { 2 } ) } { 1 - \pmb { v } _ { t } \cdot \pmb { e } / c + U _ { t } / c ^ { 2 } + \pmb { v } _ { t } ^ { 2 } / ( 2 c ^ { 2 } ) }
$$

of radio waves (Soffel 1989), which depends on the relative motion between the transmitter and receiver. Here $f _ { t }$ and $f _ { r }$ are the transmitted and received signal