# CHAPTER II MULTISTEP METHODS AND GENERAL LINEAR METHODS

This chapter is devoted to the study of multistep and general multivalue methods. After retracing their historical developement (Adams, Nystrom, Milne, BDF) we study in the subsequent sections the order, stability and convergence properties of these methods. Convergence is most elegantly set in the framework of one-step methods in higher dimensions. Sections III.5 and Il.6 are devoted to variable step size and Nordsieck methods. We then discuss the various available codes and compare them on the numerical examples of Section II.10 as well as on some equations of high dimension. Before closing the chapter with a section on special methods for second order equations, we discuss two highly theoretical subjects: one on general linear methods, including Runge-Kutta methods as well as multistep methods and many generalizations, and the other on the asymptotic expansion of the global error of such methods.

# II.1. Classical linear multistep formulas

and my undertaking must have ended here, if I had depended upon my own resources. But at this point Professor J.C. Adams furnished me with a perfectly satisfactory method of calculating by quadratures the exact theoretical forms of drops of fluids from the Differential Equation of Laplace."   
(F. Bashforth,1883)

Another improvement of Euler's method was considered even earlier than Runge-Kutta methods - the methods of Adams. Thesc were devised by John Couch Adams in order to solve a problem of F. Bashforth, which occured in an investigation of capillary action. Both the problem and the numerical integration schemes are published in Bashforth (1883). The actual origin of these methods must date back to at least 1855, since in that year F. Bashforth made an application to the Royal Society for assistance from the Government grant. There he wrote: "., but I am indebted to Mr Adams for a method of treating the differential equation

$$
\frac { \frac { d d z } { d u ^ { 2 } } } { \big ( 1 + \frac { { d z } ^ { 2 } } { { d u } ^ { 2 } } \big ) ^ { 3 / 2 } } + \frac { \frac { 1 } { u } \frac { d z } { d u } } { \big ( 1 + \frac { { d z } ^ { 2 } } { { d u } ^ { 2 } } \big ) ^ { 1 / 2 } } - 2 \alpha z = \frac { 2 } { b } ~ ,
$$

when put under the form

$$
{ \frac { b } { \ p } } \ + \ { \frac { b } { x } } \sin \Phi = 2 + 2 \alpha b ^ { 2 } { \frac { z } { b } } = 2 + \beta { \frac { z } { b } } \ ,
$$

which gives the theoretical form of the drop with an accuracy exceeding that of the most refined measurements."

In contrast to one-step methods, where the numerical solution is obtained solely from the differential equation and the initial value, the algorithm of Adams consists of two parts: firstly, a starting procedure which provides $y _ { 1 } , . . . , y _ { k - 1 }$ (approximations to the exact solution at the points $x _ { 0 } { + } h \ , \ldots , x _ { 0 } { + } ( k - 1 ) h \ )$ and, secondly， a multistep formula to obtain an approximation to the exact solution $y \left( x _ { \mathit { 0 } } + k h \right)$ This is then applied recursively, based on the numerical approximations of $k$ successive steps, to compute $y \left( x _ { 0 } + ( k + 1 ) h \right) , \ldots$ etc.

There are several possibilities for obtaining the starting values. J.C. Adams actually computed them using the Taylor series expansion of the exact solution (as described in Section I.8, see also Exercise 2). Another possbility is the use of any one-step method, e.g. a Runge-

Kutta method (see Chapter II). It is also usual to start with low-order Adams methods and very small step sizes.

# Explicit Adams methods

We now derive, following Adams, the first explicit multistep formulas. We introduce the notation ${ x _ { i } = } x _ { 0 } { + } i h$ for the grid points and suppose we know the numerical appoximations $y _ { n } , y _ { n - 1 } , \ldots , y _ { n - k + 1 }$ to the exact solution $y \left( x _ { n } \right) , \ldots , y \left( x _ { n - k + 1 } \right)$ of the differential equation

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } .
$$

Adams considers (1.1) in integrated form,

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n } \right) + \intop _ { x _ { n } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ , ~ }
$$

On the right hand side of (1.2) there appears the unknown solution $y \left( x \right)$ But since the approximations $y _ { n - k + 1 } , \ldots , y _ { n }$ are known, the values

$$
f _ { i } = f \left( x _ { i } , y _ { i } \right) \qquad \mathrm { f o r } i = n - k + 1 , \ldots , n
$$

are also available and it is natural to replace the function $f \left( t , y \left( t \right) \right)$ in (1.2) by the interpolation polynomial through the points $\{ ( \boldsymbol { x } _ { i } , f _ { i } ) | i = n - k + 1 , \ldots , n \}$ This polynomial can be expressed in terms of backward differences

$$
\nabla ^ { 0 } f _ { n } = f _ { n } , \qquad \nabla ^ { j + 1 } f _ { n } = \nabla ^ { j } f _ { n } - \nabla ^ { j } f _ { n - 1 }
$$

as follows:

$$
p \left( t \right) = p \left( x _ { n } + s h \right) = \sum _ { j = 0 } ^ { k - 1 } ( - 1 ) ^ { j } \binom { - s } { j } \nabla ^ { j } f _ { n }
$$

(Newton's interpolation formula, see e.g. Henrici (1962), p.190). The numerical analogue to (1.2) is then given by

$$
y _ { n + 1 } = y _ { n } + \intop _ { x _ { n } } ^ { x _ { n + 1 } } p \left( t \right) d t
$$

or after insertion of (1.4) by

$$
y _ { n + 1 } = y _ { n } + h \sum _ { j = 0 } ^ { k - 1 } \gamma _ { j } \nabla ^ { j } f _ { n }
$$

where the coefficients Y ， satisfy

Table 1.1. Coefficients for the explicit Adams methods   

<table><tr><td>j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>γj</td><td>1</td><td>1</td><td>5</td><td>3</td><td>251</td><td>95</td><td>19087</td><td>5257</td><td>1070017</td></tr><tr><td></td><td></td><td>2</td><td>12</td><td>8</td><td>720</td><td>288</td><td>60480</td><td>17280</td><td>3628800</td></tr></table>

$$
\gamma _ { j } = { ( - 1 ) ^ { j } } \intop _ { 0 } ^ { 1 } { \binom { - s } { j } d s }
$$

(see Table 1.1 for their numerical values). A simple recurrence relation for these coefficients will be derived later (Formula (1.11)).

Special cases of (1.5). For $k = 1 , 2 , 3 , 4$ ， after expressing the backward differences in terms of $f _ { n - j }$ , one obtains the form ulas

$$
\begin{array} { l } { { k = 1 ; \quad y _ { n + 1 } = y _ { n } + h f _ { n } ~ , ~ ( 1 . 5 ^ { \prime } ) } } \\ { { k = 2 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 3 } { 2 } f _ { n } - \displaystyle \frac { 1 } { 2 } f _ { n - 1 } \right] ~ , } } \\ { { k = 3 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 2 3 } { 1 2 } f _ { n } - \displaystyle \frac { 1 6 } { 1 2 } f _ { n - 1 } + \displaystyle \frac { 5 } { 1 2 } f _ { n - 2 } \right] ~ , } } \\ { { k = 4 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 5 5 } { 2 4 } f _ { n } - \displaystyle \frac { 5 9 } { 2 4 } f _ { n - 1 } + \displaystyle \frac { 3 7 } { 2 4 } f _ { n - 2 } - \displaystyle \frac { 9 } { 2 4 } f _ { n - 3 } \right] ~ . } } \end{array}
$$

Remark. For $k = 1$ we have the explicit Euler method.

# Implicit Adams methods

The formulas (1.5) are obtained by integrating the interpolation polynomial (1.4) from $x _ { n }$ t0 $x _ { n + 1 }$ ,ieoutsidetheitpaite val $( x _ { n - k + 1 } , x _ { n } )$ . It is wel known that an interpolation polynomial is usually a rather poor approximation outside this interval. Thus the explicit Adams methods are not very accurate. Adams therefore also investigated methods where (1.4) is replaced by the interpolation polynomial which uses in addition the point $( x _ { n + 1 } , f _ { n + 1 } )$ ,i.e.

$$
p ^ { * } ( t ) = p ^ { * } ( x _ { n } + s h ) = \sum _ { j = 0 } ^ { k } ( - 1 ) ^ { j } \binom { - s + 1 } { j } \nabla ^ { j } f _ { n + 1 } .
$$

Inserting this into (1.2) we obtain the following im plicit method

$$
y _ { n + 1 } = y _ { n } + h \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 }
$$

where the coeficients $\gamma _ { j } ^ { \ast }$ satisfy

Table 1.2. Coefficients for the implicit Adams methods   

<table><tr><td>j</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>Y</td><td>1</td><td>2</td><td>二1 12</td><td>-1 24</td><td>-19 720</td><td>-3 160</td><td>-863 60480</td><td>-275 24192</td><td>-33953 3628800</td></tr></table>

$$
{ \gamma _ { j } ^ { * } } = { ( - 1 ) ^ { j } } \intop _ { 0 } ^ { 1 } { \binom { - s + 1 } { j } } d s
$$

and are given in Table 1.2 for $j \le 8$ . Again, a simple recurrence relation can be derived for these coefficients (Exercise 3).

The formulas thus obtained are generally of the form

$$
y _ { n + 1 } = y _ { n } + h \left[ \beta _ { k } f _ { n + 1 } + \cdot \cdot \cdot + \beta _ { 0 } f _ { n - k + 1 } \right] .
$$

The first examples are as follows

$$
\begin{array} { l } { { k = 0 ; \quad y _ { n + 1 } = y _ { n } + h f _ { n + 1 } \ , \ } } \\ { { k = 1 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 1 } { 2 } f _ { n + 1 } + \displaystyle \frac { 1 } { 2 } f _ { n } \ \right] \ , } } \\ { { k = 2 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 5 } { 1 2 } f _ { n + 1 } + \displaystyle \frac { 8 } { 1 2 } f _ { n } - \displaystyle \frac { 1 } { 1 2 } f _ { n - 1 } \ \right] \ , } } \\ { { k = 3 ; \quad y _ { n + 1 } = y _ { n } + h \left[ \displaystyle \frac { 9 } { 2 4 } f _ { n + 1 } + \displaystyle \frac { 1 9 } { 2 4 } f _ { n } - \displaystyle \frac { 5 } { 2 4 } f _ { n - 1 } + \displaystyle \frac { 1 } { 2 4 } f _ { n - 2 } \right] \ . } } \end{array}
$$

The special cases $\scriptstyle k = 0$ and $k = 1$ are the implicit Euler method and the trapezoidal rule, respectively. They are actually one-step methods and have already been considered in Chapter II.7.

The methods (1.8) give in general more accurate approximations to the exact solution than (1.5). This will be discussed in detail when the concepts of order and error constant are introduced (Section III.2). The price for this higher accuracy is that $y _ { n + 1 }$ is only defined implicitly by Formula (1.8). Therefore, in general a nonlinear equation has to be solved at each step. This can be done by fixed point iteration: let y ( be an approximation to $y _ { n + 1 }$ and define

$$
y _ { n + 1 } ^ { ( l ) } = y _ { n } + h \left[ \ B _ { k } f \left( x _ { n + 1 } , y _ { n + 1 } ^ { ( l - 1 ) } \right) + \ B _ { k - 1 } f _ { n } \ + \cdot \cdot \cdot + \mathsf { \beta } _ { 0 } f _ { n - k + 1 } \right] \ .
$$

Then,if thestepire $^ h$ is small enoug, $y _ { n + 1 } ^ { ( l ) }$ converges for $l  \infty$ t the numerical solution $y _ { n + 1 }$ of (1.8). In practice one uses for $y _ { n + 1 } ^ { ( 0 ) }$ the value obtained from the explicit formula (1.5) ("Predictor"), followed by one iteration of formula (1.10) ("Corrector"). This technique has been used by F.R. Moulton (1926) as well as by W.E. Milne (1926). J.C. Adams actually solved the implicit equation (1.8) by Newton's method, in the same way as is now usual for stiff equations (see Volume II).

Remark: Formula (1.5) is often attributed to Adams-Bashforth. Similarly, the multistep formula (1.8) is usually attributed to Adams-Moulton (F.R. Moulton (1926)). In fact, both formulas are due to Adams.

# Recurrence relations for the Y;

Using Euler's method of generating functions (see e.g. Henrici (1962)) we can deduce simple recurrence relations for $\boldsymbol { \gamma } _ { i }$ Denote by $G \left( t \right)$ the series

$$
G \left( t \right) = \sum _ { j = 0 } ^ { \infty } { \gamma _ { j } t ^ { j } } \mathrm { ~ . ~ }
$$

With the definition of $\gamma _ { j }$ and the binomial theorem one obtains

$$
\begin{array} { l } { G \left( t \right) = \displaystyle \sum _ { j = 0 } ^ { \infty } \left( - t \right) ^ { j } \int _ { 0 } ^ { 1 } \binom { - s } { j } d s = \displaystyle \int _ { 0 } ^ { 1 } \sum _ { j = 0 } ^ { \infty } \left( - t \right) ^ { j } \binom { - s } { j } d s } \\ { \displaystyle = \displaystyle \int _ { 0 } ^ { 1 } \left( 1 { - } t \right) ^ { - s } d s = - \frac { t } { \left( 1 - t \right) \log \left( 1 - t \right) } . } \end{array}
$$

This can be written as

$$
- \ { \frac { \log ( 1 - t ) } { t } } \ G \left( t \right) = { \frac { 1 } { 1 - t } }
$$

or as

$$
( 1 + \textstyle { \frac { 1 } { 2 } } t + \textstyle { \frac { 1 } { 3 } } t ^ { 2 } + \cdot \cdot \cdot ) ( \gamma _ { 0 } + \gamma _ { 1 } t + \gamma _ { 2 } t ^ { 2 } + \cdot \cdot \cdot ) = ( 1 + t + t ^ { 2 } + \cdot \cdot \cdot ) \ .
$$

Comparing the coefficients of $t ^ { m }$ we get the desired recurrence reiation

$$
\gamma _ { m } + \frac { 1 } { 2 } \gamma _ { m - 1 } + \frac { 1 } { 3 } \gamma _ { m - 2 } + \cdots + \frac { 1 } { m + 1 } \gamma _ { 0 } = 1 \ .
$$

The corresponding formula for implicit Adams methods is discussed in Exercise 3.

# Ex plicit Nystrδm methods

'Die angenaherte Integration hat, besonders in der letzten Zeit, ein ausgedehntes Anwendungsgebiet innerhalb der exakten Wissenschaften und der Technik gefunden."

(E.J. Nystrom, 1925)

In his review article on the numerical integration of differential equations (which we have already encountered in Section II.13), Nystrom (1925) also presents a new class of multistep methods. He considers instead of (1.2) the integral equation

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n - 1 } \right) + \intop _ { x _ { n - 1 } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ . ~ }
$$

Just as J.C. Adams did he replaces the unknown function $f \left( t , y \left( t \right) \right)$ by the polynomial $p \left( t \right)$ of (1.4) and so obtains the formula

$$
y _ { n + 1 } = y _ { n - 1 } + h \sum _ { j = 0 } ^ { k - 1 } \kappa _ { j } \nabla ^ { j } f _ { n }
$$

with the coefficients

$$
\kappa _ { j } = { ( - 1 ) ^ { j } } \intop _ { - 1 } ^ { 1 } { \binom { - s } { j } d s } .
$$

The first six of these coefficients are given in Table 1.3. E.J. Nystrom recommended the formulas (1.13)， since the coefficients $\kappa _ { j }$ were more convenient for his computations than the coefficients' $\gamma _ { j }$ of (1.5). This recommendation, surely reasonable for a computation by hand, is of little relevance for computations on a computer.

Table 1.3. Coefficients for the explicit Nystrom methods   

<table><tr><td>j</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Kj</td><td>2 0</td><td>1 1 3 3</td><td>29 90</td><td>14 45</td><td>1139 3780</td></tr></table>

Special cases: For $k = 1$ the formula

$$
y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n }
$$

is obtained. It is called the mid-point rule and is the simplest two-step method. Its symmetry was extremely useful in the extrapolation schemes of Section II.9. The case $k = 2$ yields nothing new, since $\kappa _ { 1 } { = } 0 .$ For $k = 3$ one gets

$$
y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 7 } { 3 } f _ { n } - \frac { 2 } { 3 } f _ { n - 1 } + \frac { 1 } { 3 } f _ { n - 2 } \right] .
$$

# Milne-Simpson methods

We consider again the integral equation (1.12). But this time we replace the integrand by the polynomial $\boldsymbol { p } ^ { * } ( t )$ of (1.7),which in addition to $f _ { n } ~ , ~ \dots , f _ { n - k + 1 }$ also interpolates the value $f _ { n + 1 }$ . Proceeding as usual, we now get the implicit formulas

$$
y _ { n + 1 } = y _ { n - 1 } + h \sum _ { j = 0 } ^ { k } \kappa _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 } ~ .
$$

The coefficients $\kappa _ { j } ^ { \ast }$ are defined by

$$
\kappa _ { j } ^ { \ast } = ( - 1 ) ^ { j } \int _ { - 1 } ^ { 1 } \binom { - s + 1 } { j } d s ,
$$

and the first of these are given in Table 1.4.

Table 1.4. Coefficients for the Milne-Simpson methods   

<table><tr><td>j</td><td>0 1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>x</td><td>2 -2</td><td>1 3</td><td>0</td><td>-1 90</td><td>-1 90</td><td>-37 3780</td></tr></table>

If the backward differences in (1.15) are expressed in terms of $f _ { n - j } ,$ . one obtains the following methods for special values of $k$ ：

$$
\begin{array} { r l r } { \mathrm { ~ } } & { : = 0 ; } & { y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n + 1 } \ , \ } \\ { \mathrm { ~ } } & { : = 1 ; } & { y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n } \ , \ } \\ { \mathrm { ~ } } & { : = 2 ; } & { y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 1 } { 3 } f _ { n + 1 } + \frac { 4 } { 3 } f _ { n } + \frac { 1 } { 3 } f _ { n - 1 } \right] \ , \ } \\ { \mathrm { ~ } } & { : = 4 ; } & { y _ { n + 1 } = y _ { n - 1 } + h \left[ \frac { 2 9 } { 9 0 } f _ { n + 1 } + \frac { 4 4 } { 9 0 } f _ { n } + \frac { 4 } { 9 0 } f _ { n - 1 } + \frac { 4 } { 9 0 } f _ { n - 2 } - \frac { 1 } { 9 0 } f _ { n - 3 } \right] \ . } \end{array}
$$

The special case $k = 0$ is just Euler's implicit method applied with step size $2 h$ . For $k = 1$ one obtains the previously derived mid-point rule. The particular case $k = 2$ is an interesting method, known as the Milne method (see Milne (1926), (1970), p.66). It is a direct generalization of Simpson's rule.

Many other similar methods have been investigated. They are all based on an integral equation of the form

$$
y \left( x _ { n + 1 } \right) = y \left( x _ { n - l } \right) + \intop _ { x _ { n - l } } ^ { x _ { n + 1 } } f \left( t , y \left( t \right) \right) d t \mathrm { ~ , ~ }
$$

where $f \left( t , y \left( t \right) \right)$ is replaced either by the interpolating polynomial $p \left( t \right)$ (Formula (1.4)) or by $p ^ { * } ( t )$ (Formula (1.7). E.g. for $l = 3$ one obtains

$$
y _ { n + 1 } = y _ { n - 3 } + h \left[ { \frac { 8 } { 3 } } f _ { n } - { \frac { 4 } { 3 } } f _ { n - 1 } + { \frac { 8 } { 3 } } f _ { n - 2 } \right] .
$$

This particular method has been used by Milne (1926) as a "predictor" for his method: in order to solve the implicit equation (1.15'), Milne uses one or two fixed-point iterations with the numerical value of (1.18) as starting point.

Methods based on differentiation (BDF)

"My name is Gear." - - - "sorry? " "Gear, dshii, ii, ay, are." - . - “Jiea? (In a hotel in Paris)

The multistep formulas considered until now are all based on numerical integration, i.e. the integral in (1.17) is approximated numerically using some quadrature formula. The underlying idea of the following multistep formulas is totally different as they are based on the numerical differentiation of a given function.

Assume that the approximations $y _ { n - k + 1 } , \ldots , y _ { n }$ to the exact solution of (1.1) are known.In order to derive a formula for $y _ { n + 1 }$ we consider the polynomial $q \left( x \right)$ which interpolates the values $\{ ( x _ { i } , y _ { i } ) \mid i = n - k + 1 , . . . , n + 1 \}$ . As in (1.7) this polynomial can be expressed in terms of back ward differences, namely

$$
q \left( x \right) = q \left( x _ { n } + s h \right) = \sum _ { j = 0 } ^ { k } \left( - 1 \right) ^ { j } { \binom { - s + 1 } { j } } \nabla ^ { j } y _ { n + 1 } .
$$

The unknown value $y _ { n + 1 }$ will now be determined in such a way that the polynomial $q \left( x \right)$ satisfies the differential equation at at least one grid-point, i.e.

$$
q ^ { \prime } ( x _ { n + 1 - r } ) = f \left( x _ { n + 1 - r } , y _ { n + 1 - r } \right) ,
$$

For $r = 1$ we obtain explicit formulas. For $k = 1$ and $k = 2$ ,these are equivalent to the explicit Euler method and the mid-point rule, respectively. The case $k = 3$ yields

$$
\frac { 1 } { 3 } y _ { n + 1 } + \frac { 1 } { 2 } y _ { n } - y _ { n - 1 } + \frac { 1 } { 6 } y _ { n - 2 } = h f _ { n } .
$$

This formula, however, as well as those for $k > 3$ , is unstable (see Section I1.3) and therefore useless.

Much more interesting are the formulas one obtains when (1.20) is taken for $r = 0$ . In this case one gets the implicit formulas

$$
\sum _ { j = 0 } ^ { k } \ S _ { j } ^ { * } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 }
$$

with the coefficients

$$
\delta _ { j } ^ { * } = \left( - 1 \right) ^ { j } \frac { d } { d s } \left( { - s + 1 \atop j } \right) \mid _ { s = 1 } .
$$

Using the definition of the binomial coeficient

$$
( - 1 ) ^ { j } \binom { - s + 1 } { j } = \frac { 1 } { j ! } ( s - 1 ) s ( s + 1 ) \cdot \cdot \cdot ( s + j - 2 )
$$

the coefficients $\boldsymbol { \mathfrak { \delta } } _ { j } ^ { * }$ are obtained by direct differentiation:

$$
\mathfrak { d } _ { 0 } ^ { * } = 0 , \qquad \mathfrak { d } _ { j } ^ { * } = \frac { 1 } { j } \mathrm { f o r } j \ge 1 \ .
$$

Formula (1.22) therefore becomes

$$
\sum _ { j = 1 } ^ { k } \frac { 1 } { j } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 } .
$$

These multistep formulas, known as backward differentiation formulas (or BDF-methods) are widely used for the integration of stiff differentiai equations (see Volume II). They were introduced by Curtiss and Hirschfelder (1952)； Mitchell and Craggs (1953) call them "standard step-by-step methods".

For sake of completeness we give these formulas also in the form in which the backward differences are expressed in terms of the $y _ { n - j } .$

$$
\begin{array} { l l } { k = 1 ; } & { y _ { n + 1 } - y _ { n } = h f _ { n + 1 } \ , } \\ { k = 2 ; } & { \displaystyle \frac { 3 } { 2 } y _ { n + 1 } - 2 y _ { n } + \frac { 1 } { 2 } y _ { n - 1 } = h f _ { n + 1 } \ , } \\ { k = 3 ; } & { \displaystyle \frac { 1 1 } { 6 } y _ { n + 1 } - 3 y _ { n } + \frac { 3 } { 2 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } = h f _ { n + 1 } \ , } \\ { k = 4 ; } & { \displaystyle \frac { 2 5 } { 1 2 } y _ { n + 1 } - 4 y _ { n } + 3 y _ { n - 1 } - \frac { 4 } { 3 } y _ { n - 2 } + \frac { 1 } { 4 } y _ { n - 3 } = h f _ { n + 1 } \ , } \\ { k = 5 ; } & { \displaystyle \frac { 1 3 7 } { 6 0 } y _ { n + 1 } - 5 y _ { n } + 5 y _ { n - 1 } - \frac { 1 0 } { 3 } y _ { n - 2 } + \frac { 5 } { 4 } y _ { n - 3 } - \frac { 1 } { 5 } y _ { n - 4 } = h f _ { n + 1 } \ . } \\ { k = 6 ; } & { \displaystyle \frac { 1 4 7 } { 6 0 } y _ { n + 1 } - 6 y _ { n } + \frac { 1 5 } { 2 } y _ { n - 1 } - \frac { 2 0 } { 3 } y _ { n - 2 } + \frac { 1 5 } { 4 } y _ { n - 3 } - \frac { 6 } { 5 } y _ { n - 4 } + \frac { 1 } { 6 } y _ { n } \ . } \end{array}
$$

$$
= h f _ { n + 1 } ~ .
$$

For $k > 6$ the BDF-methods are unstable (see Section III.3).

# Exercises

1. Let the differential equation $y ^ { \prime } { = } y ^ { 2 }$ ， $y \left( 0 \right) = 1$ and the exact starting values ${ \boldsymbol y } _ { i } = 1 / \left( 1 - { \boldsymbol x } _ { i } \right)$ for $i = 0 , 1 , \ldots , k - 1$ be given. Apply the methods of Adams and study the expression $y \left( x _ { k } \right) - y _ { k }$ for small step sizes.

2. Consider the differential equation at the beginning of this section. It describes the form of a drop and can be written as (F. Bashforth 1883, page 26; the same problem as Exercise 2 of Section I1.1 in a different coordinate system)

$$
{ \frac { d x } { d \Phi } } = \rho \cos \Phi , \qquad { \frac { d z } { d \Phi } } = \rho \sin \Phi
$$

where

$$
\frac { 1 } { \rho } + \frac { \sin \Phi } { x } = 2 + \beta z \mathrm { ~ . ~ }
$$

p may be considered as a function of the coordinates $x$ and $z$ . It can be interpreted as the radius of curvature and $\Phi$ denotes the angle between the normal to the curve and the $z$ -axis (Figure 1.1). The initial values are given by $x \left( 0 \right) { = } 0$ $z \left( 0 \right) { = } 0$ ， $\rho ( 0 ) = 1$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/40357fa79624103240deb990ee246be867a305a1411628b1b00dc4dffbcd50cd.jpg)  
Figure 1.1. Solution of the differential equation (1.24) and an illustration from the book of Bashforth

Solve the above differential equation along the lines of J.C. Adams:

a) Assuming

$$
{ \mathrm { \scriptsize ~ p ~ } } = 1 + b _ { 2 } { \dot { \Phi } } ^ { 2 } + b _ { 4 } \Phi ^ { 4 } + \cdots
$$

and inserting this expression into (1.24) we obtain after integration the truncated Taylor series of $x \left( \Phi \right)$ and $z \left( \Phi \right)$ in terms of $b _ { 2 } , b _ { 4 } , \ldots$ These parameters can then be calculated from (1.25) by comparing the coefficients of $\phi ^ { m } .$ In this way one obtains the solution for small values of $\Phi$ (starting values).

b) Use one of the proposed multistep formulas and calculate the solution for fixed β (say $\beta = 3$ ） over the interval $[ 0 , \pi ]$

3. Prove that the coefficients $\gamma _ { j } ^ { * }$ , defined by (1.9), satisfy

$$
\gamma _ { 0 } ^ { * } = 1
$$

$$
\gamma _ { m } ^ { * } + \frac { 1 } { 2 } \gamma _ { m - 1 } ^ { * } + \frac { 1 } { 3 } \gamma _ { m - 2 } ^ { * } + \cdot \cdot \cdot + \frac { 1 } { m + 1 } \gamma _ { 0 } ^ { * } = 0 \quad \mathrm { f o r ~ } m \geq 1 .
$$

4. Let κj, K, $\boldsymbol { \gamma } _ { j } , \boldsymbol { \gamma } _ { j } ^ { * }$ be the coefcients defined by (1.14)， (1.16), (1.6), (1.9), respectively. Show that

$$
\kappa _ { j } ^ { } = 2 \gamma _ { j } ^ { } - \gamma _ { j - 1 } ^ { } , \kappa _ { j } ^ { * } { = } 2 \gamma _ { j } ^ { * } { - } \gamma _ { j - 1 } ^ { * } \mathrm { ~ f o r ~ } j { \ge } 0
$$

(with $\gamma _ { - 1 } { = } \gamma _ { - 1 } ^ { * } { = } 0 )$

Hint: By spliting the integral in (1.14) one gets $\kappa _ { j } { = } \gamma _ { j } { + } \gamma _ { j } ^ { * }$ The relation ${ \boldsymbol \gamma } _ { j } ^ { * } { = } { \boldsymbol \gamma } _ { j } { - } { \boldsymbol \gamma } _ { j - 1 }$ is obtained by using a well-known identity for binomial coefficients .

# I11.2. Local error and order conditions

"You know, I am a multistep-man...and don't tell anybody,but the first program I wrote for the first Swedish computer was a Runge-Kutta code..." (G. Dahlquist, 1982, after some glasses of wine; printed with permission)

A general theory of multistep methods was started by the work of Dahlquist (1956, 1959)，and became famous through the classical book of Henrici (1962). All multistep formulas considered in the last section have this in common that the numerical approximations $y _ { i }$ as well as the values $\boldsymbol { f } _ { i }$ appear linearly. We thus consider the general difference equation

$$
\alpha _ { k } y _ { n + k } + \alpha _ { k - 1 } y _ { n + k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } y _ { n } = h \left( \beta _ { k } f _ { n + k } + \cdot \cdot \cdot + \beta _ { 0 } f _ { n } \right) ,
$$

which includes all previously considered methods as special cases. In this formula the $\mathbf { a } _ { i }$ and $\beta _ { i }$ are real parameters, h denotes the step size and

$$
f _ { i } ^ { \phantom { \dagger } } = f \left( x _ { i } ^ { \phantom { \dagger } } , y _ { i } ^ { \phantom { \dagger } } \right) , \qquad x _ { i } ^ { \phantom { \dagger } } = x _ { 0 } ^ { \phantom { \dagger } } + i h ,
$$

Throughout this chapter we shall assume that

$$
\alpha _ { k } \neq 0 \ , \quad | \ \alpha _ { 0 } | \ + | \ \beta _ { 0 } | > 0 \ .
$$

The first assumption expresses the fact that the implicit equation (2.1) can be solved with respect to $y _ { n + k }$ at least for suficiently small $\hbar$ . The second relation in (2.2) can always be achieved by reducing the index k , if necessary.

Formula (2.1) will be called a linear multistep method or more precisely a linear $k$ -step method. We also distinguish between explicit $( \beta _ { k } = 0 )$ and implicit $( \beta _ { k } \neq 0$ ） multistep methods.

# Local error of a multistep method

As the numerical solution of a multistep method does not depend only on the initial value problem (1.1) but also on the choice of the starting values, the definition of the local error is not as straightforward as for one-step methods (compare Sections I1.2 and I1.3).

Definition 2.1. The local error of the multistep method (2.1) is defined by

$$
y \left( x _ { k } \right) \mathrm { ~ - ~ } y _ { k }
$$

where $y \left( x \right)$ is the exact solution of $y ^ { \prime } { = } f \left( x , y \right) , y \left( x _ { 0 } \right) { = } y _ { 0 } ,$ and $y _ { k }$ is the numerical solution obtained from (2.1) by using the exact starting values $\boldsymbol y _ { i } = \boldsymbol y \left( \boldsymbol x _ { i } \right)$ for $i = 0 , 1 , \ldots , k - 1 .$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/d27a939f44f97a8f45c062e394ce5eced82574e14b238b7c096a147bf5414727.jpg)  
Figure 2.1. Ilustration of the local error

In the case $k = 1$ this definition coincides with the definition of the local error for one-step methods. In order to show the connection with other possible definitions of the local error, we associate with (2.1) the linear difference operator $L$ defined by

$$
L \left( y , x , h \right) = \sum _ { i = 0 } ^ { k } \left[ \alpha _ { i } y \left( x + i h \right) - h \beta _ { i } y ^ { \prime } \left( x + i h \right) \right] .
$$

Here $y \left( x \right)$ is some differentiable function defined on an interval that contains the values $x + i h$ for $i = 0$ ,1,...,

Lemma 2.2. Consider the differential equation (1.1) with $f \left( x , y \right)$ continuousty differentiable and let $y \left( x \right)$ be its solution. For the local error one has

$$
y \left( x _ { k } \right) - y _ { k } \ = \ \left( \alpha _ { k } I - h \beta _ { k } { \frac { \partial f } { \partial y } } ( x _ { k } , \eta ) \right) ^ { - 1 } L \left( y , x _ { 0 } , h \right) \ .
$$

thec Here $\mathrm { \Delta \Psi ^ { \mathrm { T } } }$ is some value between e of a vetorvalued function $y \left( x _ { k } \right)$ $f$ and ， $\frac { \partial f } { \partial y } ( x _ { k } , \eta )$ $y _ { k }$ ，if $f$ is a scalar function. In is te Jacobin matrix,， whose rows are evaluated at possiby different values lying on the segment joining y(xk) and yk:

Proof: By Definition 2.1, $y _ { k }$ is determined implicitly by the equation

$$
\sum _ { i = 0 } ^ { k - 1 } \left[ \alpha _ { i } y \left( x _ { i } \right) - h \beta _ { i } f \left( x _ { i } , y \left( x _ { i } \right) \right) \right] + \alpha _ { k } y _ { k } - h \beta _ { k } f \left( x _ { k } , y _ { k } \right) = 0 \ .
$$

Inserting (2.3) we obtain

$$
L \left( y , x _ { 0 } , h \right) = \alpha _ { k } [ y \left( x _ { k } \right) - y _ { k } ] - h \beta _ { k } [ f \left( x _ { k } , y \left( x _ { k } \right) \right) - f \left( x _ { k } , y _ { k } \right) ]
$$

and the statement follows from the mean value theorem. QED.

This lemma shows that $\propto _ { k } ^ { - 1 } L \ ( y \ , x \ _ { 0 } , h )$ is essentially equal to the local error. Sometimes this term is also called the local crror (Dahlquist 1956, 1959).For explicit methods both expressions are equal.

# The order of a multistep method

Once the local error of a multistep method is defined, one can introduce the concept of order in the same way as for one-step methods.

Definition 2.3. The multistep method (2.1) is said to be of order $p$ , if one of the following two conditions is satisfied: i)forallsufficientlyregularfunctions $y \left( x \right)$ we have $L \left( y , x , h \right) = \mathbf { O } ( h ^ { p + 1 } )$ ； ii) the local error of (2.1) is $\mathbf { O } { ( h ^ { p + 1 } ) }$ for all sufficiently regular differential equations (1.1).

Observe that by Lemma 2.2 the above conditions i) and ii) are equivalent. Our next aim is to characterize the order of a multistep method in terms of the free parameters $\alpha _ { i }$ and $\beta _ { i }$ Dahlquist (1956) was the first to observe the fundamental role of the polynomials

$$
\begin{array} { l } { { \displaystyle { \mathsf { p } } \left( \zeta \right) = \alpha _ { k } \zeta ^ { k } + \alpha _ { k - 1 } \zeta ^ { k - 1 } + \cdots + \alpha _ { 0 } } } \\ { { \displaystyle { \sigma } \left( \zeta \right) = \beta _ { k } \zeta ^ { k } + \beta _ { k - 1 } \zeta ^ { k - 1 } + \cdots + \beta _ { 0 } } . } \end{array}
$$

They will be called the generating polynomials of the multistep method (2.1).

Theorem 2.4. The multistep method $( 2 . { \mathit { I } } )$ is of order $p$ , if and only if one of the following equivalent conditions is satisfied:

$$
\begin{array} { l } { { \mathrm { i } ) \quad \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } = 0 \quad a n d \quad \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } = q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \quad f o r \quad q = 1 , \dots , p \enspace ; } } \\ { { \mathrm { i i } ) \quad \displaystyle \mathsf { \rho } ( e ^ { h } ) - h \sigma ( e ^ { h } ) = 0 ( h ^ { p + 1 } ) \qquad f o r \quad h  0 \enspace ; } } \\ { { \mathrm { i i i } ) \quad \displaystyle \frac { \mathsf { \rho } ( \zeta ) } { \log \zeta } - \sigma ( \zeta ) = \mathsf { O } ( ( \zeta - 1 ) ^ { p } ) \qquad f o r \quad \zeta  1 \enspace . } } \end{array}
$$

Proof: Expanding $y \left( x + i h \right)$ and y $( x + i h )$ into a Taylor series and inserting these series (truncated if necessary) into (2.3) yields

$$
\begin{array} { c } { { \tiny { ? } \ ( y , x , h ) = \displaystyle \sum _ { i = 0 } ^ { k } \left[ \alpha _ { i } \sum _ { q \ge 0 } \frac { i ^ { q } } { q ! } h ^ { q } y ^ { ( q ) } ( x ) - h \beta _ { i } \sum _ { r \ge 0 } \frac { i ^ { r } } { r ! } h ^ { r } y ^ { ( r + 1 ) } ( x ) \right] } } \\ { { \tiny { \qquad k } } } \\ { { \tiny { = y \left( x \right) \sum _ { i = 0 } ^ { k } \alpha _ { i } + \displaystyle \sum _ { q \ge 1 } \frac { h ^ { q } } { q ! } y ^ { ( q ) } ( x ) \biggl [ \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \displaystyle \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \biggr ] \ . } } } \end{array}
$$

This implies the equivalence of Condition i) with $L \left( y , x , h \right)$ $= { \bf O } ( h ^ { p + 1 } )$ for all sufficiently regular functions $y \left( x \right)$

It remains to prove that the three conditions of Theorem 2.4 are equivalent. The identity

$$
L \left( \exp , 0 , h \right) = \rho \left( e ^ { h } \right) - h \sigma \left( e ^ { h } \right)
$$

where exp denotes the exponential function, together with

$$
L \left( \exp , 0 , h \right) = \sum _ { i = 0 } ^ { k } \alpha _ { i } + \sum _ { q \geq 1 } \frac { h ^ { q } } { q ! } \Bigg [ \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \Bigg ] \ ,
$$

which follows from (2.5)， shows the equivalence of the conditions i) and ii).

By use of the transformation $\zeta = e ^ { h }$ (or $h = \log \zeta )$ Condition ii） can be written in the form

$$
\begin{array} { r } { \mathsf { \rho } \mathsf { ( \xi ) } - \log \xi \sigma ( \boldsymbol \xi ) = \mathsf { O } ( ( \log \xi ) ^ { p + 1 } ) \qquad \mathrm { f o r ~ } \~ \xi \to \mathrm { ~ 1 ~ } . } \end{array}
$$

But this condition is equivalent to ii), since

$$
\begin{array} { r } { \log \  \zeta = ( \zeta - 1 ) + \mathbf { O } ( ( \zeta - 1 ) ^ { 2 } ) \ ~ \mathrm { f o r ~ } \ \zeta \to 1 \ . } \end{array}
$$

QED.

Remark : The conditions for a multistep method to be of order 1, which are usually called consistency conditions, can also be written in the form

$$
\mathsf { p } ( 1 ) = 0 \ , \qquad \mathsf { p ^ { \prime } ( 1 ) } = \sigma ( 1 ) \ .
$$

Once the proofs of the above order conditions have been understood, it is not difficult to treat the more general situation of non-equidistant grids (see Section I1.5 and the book of Stetter (1973), p.191).

Example 2.5. Order of the explicit Adams methods. Let us first investigate for which differential equations the explicit Adams methods give theoretically the exact solution. This is the case if the polynomial $p \left( t \right)$ of (1.4) is equal to $f \left( t , y \left( t \right) \right)$ . Suppose now that $f \left( t , y \right) { = } f \left( t \right)$ does not depend on y and is a polynomial of degree less than k . Then the explicit Adams methods integrate the differential equations

$$
y ^ { \prime } = q x ^ { q - 1 } , \qquad \mathrm { f o r } q = 0 , 1 , . . . , k
$$

exactly. This means that the local error is zero and hence, by Lemma 2.2,

$$
0 = L \left( { x ^ { q } } , 0 , h \right) = h ^ { q } \left[ \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } i ^ { q - 1 } \right] \quad \mathrm { f o r ~ } q = 0 , \dots , k \quad .
$$

This is just Condition i) of Theorem 2.4 with $p = k$ so that the order of the explicit Adams methods is at least $k$ . In fact it will be shown that the order of these methods is not greater than $k$ (Ex ample 2.7).

Example 2.6: For implicit Adams methods the polynomial $p ^ { * } ( t )$ of (1.7) is used instead of $p \left( t \right)$ . As the degree of $p ^ { * } ( t )$ is one higher than that of $p \left( t \right)$ ， the same considerations as in Example 2.5 show that the implicit Adams methods have order at least $k + 1$

All the methods of Section III.1 can be treated analogously (see Exercise 2 and Table 2.1).

# The error constant of a multistep method

The order of a multistep method indicates how fast the error tends to zero if $h  \mathrm { ~ 0 ~ }$ . Different methods of the same order, however, can have different errors; they are distinguished by the error constant. Formula (2.5) shows that the difference operator $L$ ， associated with a $p$ -th order multistep method, is such that for all sufficiently regular functions $y \left( x \right)$

$$
L \left( y , x , h \right) = C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x ) + \mathbf { O } ( h ^ { p + 2 } )
$$

where the constant $C _ { p + 1 }$ is given by

$$
C _ { p + 1 } = { \frac { 1 } { ( p + 1 ) ! } } \Bigg [ \sum _ { i = 0 } ^ { k } { \alpha _ { i } } ^ { p + 1 } - ( p + 1 ) \sum _ { i = 0 } ^ { k } { \beta _ { i } } i ^ { p } \Bigg ] ~ .
$$

This constant is not suitable as a measure of accuracy， since multipli-CationofForula(2.1bycostantcagiveauefo $C _ { p + 1 }$ whereas the numerical solution $\{ \boldsymbol { y } _ { n } \}$ remains unchanged. A better choice would be theconstant ${ \alpha } _ { k } ^ { - 1 } C _ { p + 1 } ^ { }$ ,since thelocalerrorofamul tistep method is given by (Lemma 2.2 and Formula (2.7))

$$
y ( x _ { k } ) - y _ { k } = \alpha _ { k } ^ { - 1 } C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { 0 } ) +  { \operatorname { O } ( h ^ { p + 2 } ) } \ .
$$

For several reasons, however, this is not yet a satisfactory definition, as we shall see from the following motivation: let

$$
e _ { n } \ = \ { \frac { y _ { n } - y \left( x _ { n } \right) } { h ^ { p } } }
$$

be the global error scaled by $h ^ { p }$ . Subtracting (2.1) from (2.3) and using (2.7) we have

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } e _ { \pi + i } ~ = ~ h \stackrel { 1 - p } { \sum _ { i = 0 } ^ { k } } \mathrm { \bf { \Sigma } } _ { i } ^ { k } \left( f \left( x _ { n + i } , y _ { n + i } \right) - f \left( x _ { n + i } , y \left( x _ { n + i } \right) \right) \right) } } \\ { { - C _ { p + 1 } h y ^ { ( p + 1 ) } ( x _ { n } ) ~ + { \bf O } ( h ^ { 2 } ) ~ . } } \end{array}
$$

The point is now to use

$$
y ^ { ( p + 1 ) } ( x _ { n } ) = { \frac { 1 } { \sigma ( 1 ) } } \sum _ { i  0 } ^ { k } \mathsf { \mathsf { \beta } } _ { i } y ^ { ( p + 1 ) } ( x _ { n + i } ) + \mathbf { O } ( h )
$$

which brings the error term in (2.10) inside the sum with the ${ \mathbf { } } | \beta _ { i }$ . We linearize

$$
^ { \ast } ( x _ { n + i } , y _ { n + i } ) - f ( x _ { n + i } , y ( x _ { n + i } ) ) = \frac { \partial f } { \partial y } ( x _ { n + i } , y ( x _ { n + i } ) ) h ^ { p } e _ { n + i } + 0 ( x _ { n + i } , y ( x _ { n + i } ) ) h ^ { p } e _ { n + i }
$$

and insert this together with (2.11) into (2.10). Neglecting the $\mathbf { O } ( h ^ { 2 } )$ and $\mathbb { O } \big ( h ^ { 2 p } \big )$ terms, we can interpret the obtained formula as the mul-tistep method applied to

$$
e ^ { \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) e ( x ) - C y ^ { ( p + 1 ) } ( x ) , e ( x _ { 0 } ) = 0 ,
$$

where

$$
C \ = \ { \frac { C _ { p + 1 } } { \sigma ( 1 ) } }
$$

is seen to be a natural measure for the global error and is therefore called the error constant.

Another derivation of Definition (2.13) will be given in the section on global convergence (see Exercise 2 of Section I1.4). Further, the solution of (2.12) gives just the first term of the asymptotic expansion of the global error (see Section II.9).

Example 2.7. Error constant of the explicit Adams methods. Consider the differential equation y'=f( ）with $f \left( x \right) = \left( k + 1 \right) x ^ { k }$ ，the exact solution of which is $y \left( x \right) = x ^ { k + 1 }$ As this differential equation is integrated exactly by the $\left( k + 1 \right)$ -step explicit Adams method (see Example 2.5), we have

$$
y \left( x _ { k } \right) - y \left( x _ { k - 1 } \right) = h \sum _ { j = 0 } ^ { k } { \gamma _ { j } \nabla ^ { j } f _ { k - 1 } } \mathrm { ~ . ~ }
$$

The local error of the $k$ -step explicit Adams method (1.5) is therefore given by

$$
y \left( x _ { k } \right) - y _ { k } \ = h \gamma _ { k } \nabla ^ { k } f _ { k - 1 } = h ^ { k + 1 } \gamma _ { k } f ^ { \left( k \right) } ( x _ { 0 } ) = h ^ { k + 1 } \gamma _ { k } y ^ { \left( k + 1 \right) } ( x _ { 0 } )
$$

As $\gamma _ { k } \neq 0$ , this formula shows that the order of the $k$ -step method is not greater than $k$ (compare Example 2.5). Furthermore, since $\alpha _ { k } = 1$ ， a comparison with Formula (2.9) yields $C _ { k + 1 } { = } { \boldsymbol { \gamma } } _ { k } .$ Finally, for Adams methods we have $p \left( \zeta \right) = \zeta ^ { k } - \zeta ^ { k - 1 }$ and $\rho ^ { \prime } ( 1 ) = 1$ , so that by the use of (2.6) the errocstatis given by $c = v _ { k }$

The error constants of all other previously considered multistep methods are summarized in Table 2.1 (observe that $\sigma ( 1 ) = 2$ for explicit Nystrom and Milne-Simpson methods).

Table 2.1. Order and error constant of multistep methods   

<table><tr><td>Method</td><td>Form ula</td><td>Order</td><td>Error Constant</td></tr><tr><td>Ex plicit Adam s</td><td>(1.5)</td><td>k</td><td>Yk</td></tr><tr><td>Im plicit Adam s</td><td>(1.8)</td><td>k+1</td><td>+1</td></tr><tr><td>Mid-point rule</td><td>(1.13&#x27;)</td><td>2</td><td>1 6</td></tr><tr><td>Nystrom,k &gt; 2</td><td>(1.13)</td><td>k</td><td>Kk 2</td></tr><tr><td>Milne, k =2</td><td>(1.15&#x27;)</td><td>4</td><td>1 180 *</td></tr><tr><td>Milne-Simpson, k &gt; 3</td><td>(1.15)</td><td>k+1</td><td>Kk+1 2</td></tr><tr><td>BDF</td><td>(1.22&#x27;)</td><td>k</td><td>1 k+1</td></tr></table>

# Irreducible methods

Let $\rho ( \zeta )$ and $\sigma ( \zeta )$ of Formula (2.4) be the generating polynomials of (2.1) and suppose that they have a common factor $\Phi ( \zeta )$ . Then define the polynomials

$$
{ \boldsymbol { \rho } } ^ { * } ( \zeta ) = \frac { \mathsf { \rho } ( \zeta ) } { \Phi ( \zeta ) } , \quad { \boldsymbol { \sigma } } ^ { * } ( \zeta ) = \frac { \sigma ( \zeta ) } { \Phi ( \zeta ) } ~ ,
$$

which are the generating polynomials of a new and simpler multistep method. Using the shift-operator $E$ , defined by

$$
E y _ { n } = y _ { n + 1 } \qquad \quad { \mathrm { o r } } \quad E y \left( x \right) = y \left( x + h \right)
$$

this multistep method can be written in compact form as

$$
\rho ^ { * } ( E ) y _ { n } \ = h \sigma ^ { * } ( E ) f _ { n } .
$$

Multiplication by $\phi ( E )$ shows that any solution $\{ y _ { n } \}$ of this method is

also a solution of $\operatorname { \rho } ( E { \bf \rho } ) y _ { n } = h \sigma ( E { \bf \rho } ) f _ { n }$ . The two methods are thus $L ^ { * }$ $\boldsymbol { C } _ { p + 1 } ^ { * }$

$$
\begin{array} { c } { { L \left( y , x , h \right) = \Phi ( E ) L ^ { * } ( y , x , h ) = C _ { p + 1 } ^ { * } h ^ { p + 1 } \Phi ( E ) y ^ { ( p + 1 ) } ( x ) + { \bf O } ( h ^ { p + 1 } ) , } } \\ { { { } } } \\ { { { } = C _ { p + 1 } ^ { * } \Phi ( 1 ) h ^ { p + 1 } y ^ { ( p + 1 ) } ( x ) + { \bf O } ( h ^ { p + 2 } ) } } \end{array}
$$

Cion one immeditely obtains $C _ { p + 1 } / \sigma ( 1 ) { = } C _ { p + 1 } ^ { * } / \sigma ^ { * } ( 1 )$ $C _ { p + 1 } { = } \Phi ( 1 ) C _ { p + 1 } ^ { * }$ and therefore also the rela hmethods thus hne thte same error constant.

The above analysis has shown that multistep methods whose generating polynomials have a common factor are not interesting. We therefore usually assume that

Multistep methods satisfying this property are called irreducible.

# The Peano kernel of a multistep method

The order and the error constant above do not yet give a com-$C _ { p + 1 }$ mula, to obtain a complete description of the error. The following discussion is an extension of the ideas of Peano (1913):

Theorem 2.8. Let the multistep method (2.1) be of order $\boldsymbol { p }$ and let $\eta \left( 1 \leq q \leq p \right)$ ） be an integer. For any $( q + 1 )$ times continuously differentiable function $y \left( x \right)$ we then have

where

$$
L \left( y , x , h \right) = h ^ { q + 1 } \int _ { 0 } ^ { k } K _ { q } ( s ) y ^ { \left( q + 1 \right) } ( x + s h ) d s ,
$$

$$
K _ { q } ( s ) = { \frac { 1 } { q ! } } \sum _ { i = 0 } ^ { k } \alpha _ { i } ( i - s ) _ { + } ^ { q } - { \frac { 1 } { ( q - 1 ) ! } } \sum _ { i = 0 } ^ { k } \mathfrak { p } _ { i } ( i - s ) _ { + } ^ { q - 1 }
$$

is called the $q$ -th Peano-kernel of the multistep method (3.1).

Remark. The notation

$$
( i - s ) _ { + } ^ { r } = \left\{ \begin{array} { c l l } { { \left( i - s \right) ^ { r } } } & { { \mathrm { f o r } } } & { { i - s > 0 } } \\ { { 0 } } & { { \mathrm { f o r } } } & { { i - s \leq 0 } } \end{array} \right.
$$

is used in the definition of the Peano-kernel. $\kappa _ { q } \left( s \right)$ is therefore

piece-wise a polynomial and satisfies

$$
K _ { q } ( s ) = { \frac { 1 } { q ! } } \sum _ { i = j } ^ { k } \alpha _ { i } ( i - s ) ^ { q } - { \frac { 1 } { ( q - 1 ) ! } } \sum _ { i = j } ^ { k } 8 _ { i } ( i - s ) ^ { q - 1 } \quad { \mathrm { f o r ~ } } s \in [ j - 1 , j ) ,
$$

Proof: Taylor's theorem with the integral representation of the rem ainder yields

$$
\begin{array} { l } { { \displaystyle ( x + i h ) = \sum _ { r = 0 } ^ { q } \frac { i ^ { r } } { r ! } h ^ { r } y ^ { ( r ) } ( x ) + h ^ { q + 1 } \int _ { 0 } ^ { \frac { i } { q } } \frac { ( i - s ) ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s , } } \\ { { \displaystyle + i h ) = \sum _ { r = 1 } ^ { q } \frac { i ^ { r - 1 } } { ( r - 1 ) ! } h ^ { r } y ^ { ( r ) } ( x ) + h ^ { q + 1 } \int _ { 0 } ^ { \frac { i } { ( q - 1 ) ! } } y ^ { ( q + 1 ) } ( x + s h ) d s } } \end{array}
$$

Inserting these two expressions into (2.3), the same considerations as in the proof of Theorem 2.4 show that for $q \leq p$ the polynomials before the integral are cancelled. The statement then follows from

$$
\int \limits _ { 0 } ^ { i } \frac { ( i - s ) ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s = \int \frac { k } { q ! } \frac { ( i - s ) _ { + } ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x + s h ) d s .
$$

QED.

Besides the representation (2.15)， the Peano-kernel $K _ { q } ( s )$ has the following properties:

$$
s \in ( - \infty \mathrm { ~ , 0 } ) \cup [ k \mathrm { ~ , } \infty \mathrm { ~ ) ~ a n d ~ } q = 1 \mathrm { ~ , ~ . ~ . ~ , } p \mathrm { ~ ; ~ }
$$

$K _ { q } \left( s \right)$ is $( q - 2 )$ -times continuously differentiable and $\overset { \vartriangle { 1 } } { \boldsymbol { \mathcal { K } } _ { q } ^ { \prime } } ( s ) = - \boldsymbol { K } _ { q - 1 } ( s )$ for $q = 2 , \ldots , p$ (for $q = 2$ in the sense of distributions);

$\boldsymbol { K } _ { \mathrm { ~ \scriptsize ~ 1 ~ } } ( \boldsymbol { s } )$ is a piece-wise linear function with discontinuities at $0 , 1 \ , \ \dots , k \ .$ It has a jump of size ${ \mathsf { \beta } } _ { j }$ at the point $j$ and its slope over the interval $( j - \dot { 1 } , j ^ { \cdot }$ ）is given by $- ( \alpha _ { j } + \alpha _ { j + 1 } + \cdot \cdot \cdot + \alpha _ { k } )$

For the constant $C _ { p + 1 }$ of (2.8) we have

$$
C _ { p + 1 } { = } \intop _ { 0 } ^ { k } K _ { p } ( s ) d s .
$$

The proofs of Statements (2.16) to (2.19) are as follows: it is an immediate consequence of the definition of the Peano-kernel that $K _ { q } \left( s \right) = 0$ for $s \geq k$ and $q \leq p$ . In order to prove $K _ { q } \left( s \right) = 0$ also for $s \dot { < } 0$ we consider the polynomial $y \left( x \right) = ( x - s ) ^ { q }$ with $s$ as a parameter. Theorem 2.8 then shows that

$$
L \left( y , 0 , 1 \right) = \sum _ { i = 0 } ^ { k } \alpha _ { i } ( i - s ) ^ { q } - q \sum _ { i = 0 } ^ { k } \beta _ { i } ( i - s ) ^ { q - 1 } \equiv 0 \qquad { \mathrm { f o r } } \quad q \leq p
$$

and hence $K _ { q . } \left( s \right) = 0$ for $s < 0$ . This gives (2.16). The relation (2.17) is seen by partial integration of (2.14). As an example, the Peanokernels for the 3-step Nystrom method $\left( 1 . 1 3 ^ { \circ } \right)$ ） are plotted in Figure 2.2.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/54633242988b50c4c609225b2d7ae878089c97c2847fdb5cdf155a675a6333a8.jpg)  
Figure 2.2. Peano-kernels of the 3-step Nystrom method

# Exercises

1. Construction of multistep methods.

a) To any $k$ -th degree polynomial $\rho ( \zeta )$ satisfying $\rho \left( 1 \right) { = } 0$ there corresponds exactly one polynomial $\sigma \left( \zeta \right)$ of degree $\le k$ , such that the order of the corresponding multistep method is at least $k + 1$ b) In situation a) there exists exactly one polynomial $\sigma \left( \zeta \right)$ of degree $< k$ , such that the corresponding multistep method, which is then explicit, has order at least $k$ 、   
Hint. Condition ii) of Theorem 2.4.

2. Find the multistep method of the form

$$
y _ { n + 2 } + \alpha _ { 1 } y _ { n + 1 } + \alpha _ { 0 } y _ { n } \ = h \left( \beta _ { 1 } f _ { n + 1 } + \beta _ { 0 } f _ { n } \right)
$$

of the highest possible order. Try this formula on the example $y ^ { \prime } { = } y , y ( 0 ) { = } 1 , h { = } 0 . 1 ,$

3. Verify that the order and the error constant of the BDF-formulas are those of Table 2.1.

4. Show that the Peano-kernel $K _ { p } ( s )$ does not change sign for the explicit and implicit Adams methods and for the BDF-formulas. Deduce from this property that

$$
L \left( y , x , h \right) = h ^ { p + 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( \zeta ) \quad \mathrm { w i t h } \quad \zeta \in \left( x , x + k h \right) .
$$

where the constant $C _ { p + 1 }$ is given by (2.8).

5. Let $y \left( x \right)$ be an exact solution of $y ^ { \prime } { = } f \left( x \ , y \right)$ and let $\boldsymbol { y } _ { i } = \boldsymbol { y } \left( \boldsymbol { x } _ { i } \right) ,$ $i = 0 , 1 , \ldots , k - 1$ . Assume that $f$ is continuous and satisfies a Lipschitz condition with respect to y $( f$ not necessarily differentiable). Prove that for consistent multistep methods (i.e. Formula (2.6) holds) the local error satisfies

$$
\| ~ y ( x _ { k } ) - y _ { k } \| ~ \leq ~ h \omega ( h )
$$

where ${ \mathfrak { o } } ( h ) \to 0$ for h- 0.

# I11.3. Stability and the first Dahlquist barrier

hat der Verfasser seither ofters Verfahren zur numerischen Integration von Differentialgleichungen beobachtet, die, obschon zwar mit bestechend kleinem Abbruchfehler behaftet, doch die grosse Gefahr der numerischen Instabilitat in sich bergen." (H. Rutishauser, 1952)

Rutishauser observed in his famous paper that high order and a small local error are not sufficient for a useful multistep method. The numerical solution can be "unstable", even though the step size h is taken very small. The same observation was made by Todd (1950), who applied certain difference methods to second order differential equations. Our presentation will mainly follow the lines of Dahlquist (1956),where this effect has been studied systematically. An interesting presentation of the historical development of numerical stability concepts can be found in Dahlquist (1985) "33 years of numerical instability, Part I".

Let us start with an example, taken from Dahlquist (1956)， see Exercise 2 of Section I1.2. Among all explicit 2-step methods we con-sider the formula with the highest order. A short calculation using Theorem 2.4 shows that this method of order 3 is given by

$$
y _ { n + 2 } + 4 y _ { n + 1 } - 5 y _ { n } = h \left( 4 f _ { n + 1 } + 2 f _ { n } \right) .
$$

Application to the differential equation

$$
y ^ { \prime } = y , \qquad y ( 0 ) = 1
$$

yields the linear difference relation

$$
y _ { n + 2 } + 4 ( 1 - h ) y _ { n + 1 } - ( 5 + 2 h ) y _ { n } ~ = 0 ~ ,
$$

As starting values we take $y _ { 0 } = 1$ and $\boldsymbol { y } _ { 1 } \mathrm { = e x p } ( h )$ , the values on the exact solution. The numerical solution together with the exact solution $\operatorname { e x p } ( x )$ is plotted in Figure 3.1 for the step sizes $h = 1 / 1 0$ ， $h = 1 / 2 0$ ， $h = 1 / 4 0$ , etc. In spite of the small local error, the results are very bad. One observes in Figure 3.1 that the results become worse as the step size decreased.

An explanation for this effect can easily be given. As usual for linear difference equations (Lagrange (1775))， we insert $y _ { j } = \zeta ^ { j }$ into (3.3). This leads to the characteristic equation

$$
\zeta ^ { 2 } + 4 ( 1 { - } h ) \zeta - ( 5 + 2 h ) = 0 .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/88f81fc81928f7b806ae17bd4ce86d40e89c6a24516343c3db836eb174eda10f.jpg)  
Figure 3.1. Numerical solution of the instable method (3.1)

The general solution of (3.3) is then given by

$$
y _ { n } = A \ \zeta _ { 1 } ^ { \ n } ( h ) + B \ \zeta _ { 2 } ^ { \ n } ( h )
$$

where

$$
\zeta _ { 1 } ( h ) = 1 + h + { \bf O } ( h ^ { 2 } ) , ~ \zeta _ { 2 } ( h ) = - 5 + { \bf O } ( h )
$$

are the roots of (3.4) and the coefficients A and $B$ are determined by the starting values $y _ { 0 }$ and $y _ { 1 }$ Since $\boldsymbol { \zeta } _ { 1 } ( h )$ approximates $\exp ( h )$ ,the first term in (3.5) approximates the exact solution $\operatorname { e x p } ( x )$ at the point $x = n h$ . The second term in (3.5)， often called a parasitic solution, is the one which causes trouble in our method: since for $h  \mathrm { ~ 0 ~ }$ the absolute value of $\zeta _ { 2 } ( h )$ is larger than one, this parasitic solution becomes very large and dominates the solution $y _ { n }$ for increasing $n$

We now turn to the stability discussion of the general method (2.1). The essential part is the behaviour of the solution as $n  \infty$ (or $h  ~ 0 ^ { \prime }$ ） with nh fixed. We see from (3.3) that for $h  ~ 0$ we obtain

$$
\alpha _ { k } y _ { n + k } + \alpha _ { k - 1 } y _ { n + k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } y _ { n } = 0 .
$$

This can be interpreted as the numerical solution of the method (2.1) for the differential equation

$$
y ^ { \prime } = 0 .
$$

We put $y _ { j } = \zeta ^ { j }$ in (3.6), divide by $\zeta ^ { n }$ , and find that $\zeta$ must be a root of

$$
\rho ( \zeta ) = \alpha _ { k } \zeta ^ { k } + \alpha _ { k - 1 } \zeta ^ { k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } = 0 \ .
$$

As in Section I.5, we again have some difficulty when (3.8) possesses cise 1 below) a root of multiplicity $y _ { n } = n ^ { J - 1 } \zeta ^ { n } ( j = 1 , . . . , m ) ,$ $m > 1$ . In this case (Lagrange (1792), see Exer- are solutions of (3.6)and we obtain by superposition:

Lemma 3.1. Let $\zeta _ { 1 } , \ldots , \zeta _ { l }$ be the roots of $\rho \left( \zeta \right)$ , of respective muliplicity $m _ { \textrm { 1 } } , \dots , m _ { l }$ Then the general solution of $\left( 3 . 6 \right)$ is given by

$$
y _ { n } = p _ { 1 } ( n ) \zeta _ { 1 } ^ { n } + \cdot \cdot \cdot + p _ { l } ( n ) \zeta _ { l } ^ { n }
$$

where the $p _ { j } ( n )$ are potynomials of degree $m _ { j } - 1$ . NED.

Formula (3.9) shows us that for boundedness of $y _ { n }$ ，as $n  \infty$ ,we need that the roots of (3.8) lie in the unit disc and that the roots on the unit circle be simple.

Definition 3.2. The multistep method (2.1) is called stable, if the generating polynomial $\rho \left( \zeta \right)$ (Formula (3.8)) satisfies the root condition; i.e.

i) The roots of $\rho \left( \zeta \right)$ lie on or within the unit circle;   
ii) The roots on the unit circle are simple.

Remark. In order to distinguish this stability concept from others, it is sometimes called zero-stability or, in honour of Dahlquist, also $D$ -stability.

Examples: For the explicit and implicit Adams methods, $\scriptstyle \mathsf { p } ( \zeta ) = \zeta ^ { k } - \zeta ^ { k - 1 }$ Besides the simple root 1, there is a $( k - 1 )$ -fold root at 0. The Adams methods are therefore stable.

The same is true for the explicit Nystrom and the Milne-Simpson methods, where $\scriptstyle \ p ( \zeta ) = \zeta ^ { k } - \zeta ^ { k - 2 }$ Note that here we have a simple root at $- 1$ . This root can be dangerous for certain differential equations (see Volume II).

# Stability of the BDF-formulas

The investigation of the stability of the BDF-formulas is more diffcuit.Asthecharacteristicpolyomialof $\nabla ^ { j } y _ { k + n } = 0$ is given by $\zeta ^ { k - j } ( \zeta - 1 ) ^ { j } = 0$ it follows from the representation (1.22') that the generating polynomial $\rho ( \zeta )$ of the BDF-formulas has the form

$$
{ \sf p } ( \xi ) = \sum _ { j = 1 } ^ { k } \frac { 1 } { j } \xi ^ { k - j } ( \xi - 1 ) ^ { j } \mathrm { ~ . ~ }
$$

In order to study the zeros of (3.10) it is more convenient to consider the polynom ial

$$
p ( z ) = ( 1 { - } z ) ^ { k } \rho ( { \frac { 1 } { 1 - z } } ) = \sum _ { j = 1 } ^ { k } { \frac { z ^ { j } } { j } }
$$

via the transform ation $\zeta = 1 / ( 1 - z )$ . This polynomial is just the $k$ -th partial sum of $- \mathrm { l o g } ( 1 - z )$ . As the roots of $p \left( z \right)$ and $\rho ( \zeta )$ are related by the above transformation, we have:

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/d0cd4fcf56f438bbe5dde3d5903e54b09f66037fc96fd8695521e93a31b079cf.jpg)  
Figure 3.2. Roots of the polynomial $p \left( z \right)$ of (3.11)

Lemma 3.3. The k -step $B D F$ -formula (1.22') is stable iff all roots of the potynomial (3.11) are outside the disc $\{ z \ ; | z - 1 | | \leq 1 \}$ , with simple roots allowed on the boundary.

NED.

The roots of (3.11) are displayed in Figure 3.2 for different values of k .

Theorem 3.4. The k -step BDF-formula (1.22') is stable for $k \leq 6$ ， and unstable for $k \geq 7$

Proof. The first assertion can be verified simply by a finite number of numerical calculations (see Figure 3.2. This was first observed by Mitchell and Craggs (1953)). The second statement, however, contains an infinity of cases and is more difficult. The first complete proof was given by Cryer (1971) in a technical report， a condensed version of which is published in Cryer (1972). A second proof is given in Creedon and Miller (1975) (see also Grigorieff (1977), p.135), based on the Schur-Cohn criterion. This proof is outlined in Exercise 4 below. The following proof, which is given in Hairer and Wanner (1983), is based on the representation

$$
p \left( z \right) = \int _ { 0 } ^ { z } \sum _ { j = 1 } ^ { k } \zeta ^ { j - 1 } d \zeta = \int _ { 0 } ^ { z } \frac { 1 - \zeta ^ { k } } { 1 - \zeta } d \zeta = \int _ { 0 } ^ { r } { { { \left( 1 - e ^ { i k \theta } s ^ { k } \right) } } } \Phi ( s ) d s
$$

with

$$
\zeta = s e ^ { i \theta } , \qquad z = r e ^ { i \theta } , \qquad \Phi ( s ) = \frac { e ^ { i \theta } } { 1 - s e ^ { i \theta } } .
$$

We cut the complex plane into $k$ sectors

$$
S _ { j } ~ = ~ \biggl \{ z ; ~ \frac { 2 \pi } { k } ( j - \frac { 1 } { 2 } ) < \arg ( z ) < \frac { 2 \pi } { k } ( j + \frac { 1 } { 2 } ) \biggr \} , ~ j = 0 , 1 ~ , \ldots , k - 1 ~ .
$$

On the rays bounding $S _ { j }$ we have $e ^ { i k \ \theta } = - 1$ , so that from (3.12)

$$
p ( z ) = \int _ { 0 } ^ { r } ( 1 + s ^ { k } ) \phi ( s ) d s
$$

always _lies in the angle spanned by with a positive weight function. Therefore the argument of $\phi ( s ) ,$ i.e. the angle between $\begin{array} { c } { { \left( z \atop e \right) } } \end{array}$ and $e ^ { i \pi } = - 1$ .So no revolution of $\arg ( p \left( z \right) )$ is possible on these rays, and due to the one revolution of $\arg ( z ^ { k } )$ at infinity between $\scriptstyle \theta = 2 \pi { \bigl ( } j - 1 / 2 { \bigr ) } / k$ and $\theta { = } 2 \pi ( j + 1 / 2 ) / k$ the principle of the argument (e.g. Henrici (1974), p.278) implies (see Figure 3.3) that in each sector $S _ { j }$ $, ( j = 1 , \ldots , k - 1$ ， with the exception of $j = 0$ ）there lies exactly one root of $p \left( z \right)$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0005_pages_0281-0350/auto/images/93cbad297a6ee76a971d0ad05c13444f01fe18773518679853e5b5dfb2be0bb4.jpg)  
Figure 3.3. Argument of p(z ) of (3.11)

In order to complete the proof, we still have to bound the zeros of $p \left( z \right)$ from above: we observe that in (3.12) the term $s ^ { k }$ becomes large for $s > 1$ .We therefore partition (3.12) into two integrals $p \left( z \right) { = } I _ { 1 } { - } I _ { 2 } ,$ where

$$
I _ { 1 } = \int \displaylimits _ { 0 } ^ { r } \Phi ( s ) d s - \int \displaylimits _ { 0 } ^ { 1 } e ^ { i k \theta } s ^ { k } \Phi ( s ) d s , I _ { 2 } = e ^ { i k \theta } \int \displaylimits _ { 1 } ^ { r } s ^ { k } \Phi ( s ) d s .
$$

Since $| \phi ( s ) | \leq B$ (0）where

$$
B \left( \boldsymbol { \Theta } \right) = \left\{ \begin{array} { c c c } { \displaystyle \frac { 1 } { \sin \theta } \quad } & { 0 < \boldsymbol { \Theta } \leq \displaystyle \frac { \pi } { 2 } } \\ { \displaystyle 1 \quad } & { \displaystyle \frac { \pi } { 2 } \leq \boldsymbol { \Theta } \leq \pi \ , } \end{array} \right.
$$

we obtain

$$
I _ { 1 ^ { ! } } ~ \le ~ ( r + \frac { 1 } { k + 1 } ) B \left( \theta \right) < ~ r B \left( \theta \right) \frac { k + 2 } { k + 1 } ~ , ~ ( r > 1 ) ~ .
$$

Secondly, since $s ^ { k }$ is positive,

$$
I _ { \ 2 } = e ^ { i k { \ \theta } } \Phi { \int _ { 1 } ^ { r } } s ^ { k } d s \ \quad \ \mathrm { ~ w i t h ~ } \quad \Phi \in \mathrm { c o n v e x ~ h u l l ~ o f ~ } \{ \Phi ( s ) ; \ 1 \leq s \leq r \} \ .
$$

Any element of the above convex hull can be written in the form

$$
\Phi = \alpha \phi ( s _ { 1 } ) + ( 1 { - } \alpha ) \phi ( s _ { 2 } ) = \frac { \phi ( s _ { 1 } ) \phi ( s _ { 2 } ) } { \phi ( \hat { s } ) }
$$

with $\hat { s } = \alpha s _ { 2 } + ( 1 - \alpha ) s _ { 1 } , 0 \leq \alpha \leq 1 , 1 \leq s _ { 1 } , s _ { 2 } \leq r .$ Since $\phi ( s )$ decreases monotonically for $s \geq 1$ ，we _have $\Phi \ge _ { ; \Phi } ( r )$ . Some elementary geometry then leads to $\left| \Phi \right| \geq \frac { 1 } { 2 r }$ and we get

$$
I _ { 2 } | \ \cong \ \frac { r ^ { k + 1 } - 1 } { 2 r ( k + 1 ) } > \ \frac { r ( r ^ { k - 1 } - 1 ) } { 2 k + 2 } \ , ( r > 1 ) \ .
$$

From (3.13) and (3.14) we see that

$$
r \geq R \ ( \theta ) \ = \ \left( ( 2 k + 4 ) B \left( \theta \right) + 1 \right) ^ { 1 / \left( k - 1 \right) }
$$

im plies $I _ { 2 } > I _ { 1 }$ ,so that $p \left( z \right)$ cannot be zero. The curve $R$ (0）is aiso plotted in Figure 3.2 and cuts from the sectors $S _ { j }$ what we call Madam Imhof's cheese pie,each slice of which (with $j \neq 0$ ）must contain a zero of $p \left( z \right)$ A simple analysis shows that for $k = 1 2$ the cheese pie, cut from $S  { 1 }$ , is small enough to ensure the presence of zeros of $p \left( z \right)$ inside the disc $\{ z \ ; \ z - 1 \ \leq 1 \}$ As $R$ (0), for fixed 0, as well as $R$ $\pi / k$ ） are monotonically decreasing in $k$ ，the same is true for all $k \geq 1 2$ .For $6 < k < 1 2$ numerical calculations show that the method is unstable (see Figure 3.2 or Exercise 4). QED.

# Highest attainable order of stable multistep methods

It is a natural task to investigate the stability of the multistep methods with highest possible order. This has been performed by Dahlquist (1956), resulting in the famous "first Dahlquist-barrier".

Counting the order conditions (Theorem 2.4) shows that for order $p$ the parameters of a linear multistep method have to satisfy $p + 1$ linear equations. As $2 k + 1$ free parameters are involved (without loss of generality one can assume ${ \alpha } _ { k } = 1$ ), this suggests that $2 k$ is the highest attainable order. Indeed, this can be verified (see Exercise 5). However, these methods are of no practical significance, because we shall prove

Theorem 3.5. (The first Dahlquist-barrier). The order p of a stable linear k -step method satisfies

$p \leq k + 2$ if k is even,   
$p \leq k + 1$ if k is odd,   
p≤k if βk/αk≤O (in particular if the method is explicut).

We postpone the verification of this theorem and give some notations and lemmas, which will be useful for the proof. First of all we introduce the "Greek-Rom an transform ation"

$$
 \zeta = \frac { z + 1 } { z - 1 } \qquad \mathrm { o r } \qquad z = \frac { \zeta + 1 } { \zeta - 1 } \ .
$$

This transformation maps the disk $| \zeta | < 1$ onto the half-plane $\mathrm { R e } z < 0$ ， the upper half-plane $\mathrm { I m } z > 0$ onto the lower half-plane, the circle $| \zeta | = 1$ to the imaginary axis, the point $\zeta = 1$ to $z = \infty$ and the point $\zeta = - 1$ to $z = 0$ . We then consider the polynomials

$$
\begin{array} { l } { { R \left( z \right) = \left( \displaystyle \frac { z - 1 } { 2 } \right) ^ { k } \rho ( \zeta ) = \sum _ { j = 0 } ^ { k } a _ { j } z ^ { j } \mathrm { ~ , ~ } } } \\ { { \displaystyle S \left( z \right) = \left( \displaystyle \frac { z - 1 } { 2 } \right) ^ { k } \sigma ( \zeta ) = \sum _ { j = 0 } ^ { k } b _ { j } z ^ { j } \mathrm { ~ . ~ } } } \end{array}
$$

Since the zeros of R (z) and of $\rho \left( \zeta \right)$ are connected via the transformation (3.16)， the stability condition of a multistep method can be formulated in terms of $R \ ( z )$ as follows: all zeros of $R \ ( z )$ lie in the negative half-plane Re $z \le 0$ and no multiple zero of $R$ （ $z$ ）lies on the im aginary axis.

Lemma 3.6. Suppose the multistep method to be stable and of order at least O. We then have

i） $a _ { k } = 0$ and $a _ { k - 1 } { = } 2 ^ { 1 - k } \rho ^ { \prime } ( 1 ) \neq 0 ;$

ii) All non-vanishing coefficients of $R$ (z) have the same sign.

Proof: Dividing Formula (3.17) by $z ^ { k }$ and putting $z = \infty$ ,one sees that $a _ { k } = 2 ^ { - k } \rho ( 1 )$ . This expression must vanish, because the method is of order O. In the same way one gets ${ a _ { k } } _ { - 1 } { = } 2 ^ { 1 - k } \rho ^ { \prime } ( 1 )$ ， which is different from zero, since by stability 1 cannot be a multiple root of


<!-- chunk 0006: pages 351-420 -->
$\rho \left( \zeta \right) .$ The second statement follows from the factorization

$$
\begin{array} { r } { R \left( z \right) = a _ { k - 1 } \prod \left( z + x _ { j } \right) \prod \left( \left( z + u _ { j } \right) ^ { 2 } + \nu _ { j } ^ { 2 } \right) . } \end{array}
$$

where $- x _ { j }$ are the real roots and $- \boldsymbol { u } _ { j } \pm \boldsymbol { i \nu } _ { j }$ are the conjugate pairs of complex roots. By stability $x _ { j } \geq 0$ and' $u _ { j } \geq 0$ ， implying that all coefficien ts of $R _ { , } ( z )$ have the same sign. QED.

We next express the order conditions of Theorem 2.4 in terms of the polynomials $R$ (z)and $S \left( z \right)$

Lemma 3.7. The multistep method is of order $p$ if and only if

$$
R \ ( z ) \biggl ( \log \frac { z + 1 } { z - 1 } \biggr ) ^ { - 1 } - S \ ( z ) \ = C _ { p + 1 } \biggl ( \frac { 2 } { z } \biggr ) ^ { p - k } \ + \mathbf { O } ( \biggl ( \frac { 2 } { z } \biggr ) ^ { p - k + 1 } )
$$

Proof: First, observe that the $\mathbf { O } ( ( \boldsymbol { \zeta } - 1 ) ^ { p } )$ term in Condition ii) of Theorem 2.4 is equal to $C _ { p + 1 } ( \zeta - 1 ) ^ { p } + \mathbf { O } ( ( \zeta - 1 ) ^ { p + 1 } )$ by Formula (2.7). Application of the transformation (3.16) then yields (3.18)， since $( \zeta - 1 ) = 2 / ( z - 1 ) = 2 / z +  { \mathbf { O } } ( ( 2 / z ) ^ { 2 } )$ for $z  \infty$ .QED.

Lemma 3.8. The coefficients of the Laurent series

$$
\left( \log \ { \frac { z + 1 } { z - 1 } } \right) ^ { - 1 } = { \frac { z } { 2 } } - \mu _ { 1 } z ^ { - 1 } - \mu _ { 3 } z ^ { - 3 } - \mu _ { 5 } z ^ { - 5 } - \cdot \cdot \cdot ,
$$

$s a t i s f y \ \mu _ { 2 j + 1 } > 0 \ f o r \ a l l \ j \ge 0 .$

Proof: We consider the branch of log§ which is analytic in the complex $\zeta$ -plane cut along the negative real axis and satisfies $\log 1 = 0$ The transformation (3.16) maps this cut onto the segment from $- 1$ to $+ 1$ on the real axis. The function $\log ( ( z + 1 ) / ( z - 1 ) )$ is thus analytic on the complex $z$ -plane cut along this segment (see Figure 3.4). From the formula

$$
\log \frac { z + 1 } { z - 1 } = \frac { 2 } { z } \left( 1 + \frac { z ^ { - 2 } } { 3 } + \frac { z ^ { - 4 } } { 5 } + \frac { z ^ { - 6 } } { 7 } + \cdot \cdot \cdot \right) ,
$$

e existence of (3.19) becomes clear. In order to prove the positiv the coefficients, we use Cauchy's formula for the coefficients e function

$$
\begin{array} { r } { f \left( z \right) = \displaystyle \sum _ { n \in \mathbb { Z } } a _ { n } \left( z - z _ { 0 } \right) ^ { n } , } \\ { a _ { n } = \displaystyle \frac { 1 } { 2 \pi i } \int \frac { f \left( z \right) } { \gamma } \frac { d z } { \left( z - z _ { 0 } \right) ^ { n + 1 } } d z \ , } \end{array}
$$

i.e. in our situation

$$
\mu _ { 2 j + 1 } = - \frac { 1 } { 2 \pi i } { \int _ { \gamma } z ^ { 2 j } \left( \log \frac { z + 1 } { z - 1 } \right) ^ { - 1 } } d z
$$

(Cauchy (1831); see also Behnke-Sommer (1962)). Here $\gamma$ is an arbitrary curve enclosing the segment $( - 1 , 1 )$ , e.g. the curve plotted in Figure 3.4.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/a573d82aa1d2efee0121d5b33913cc29aa598c111af1a0131607f69b3dfa1897.jpg)  
Figure 3.4. Cut z -plane with curve γ

Observing that $\log ( ( z + 1 ) / ( z - 1 ) ) = \log ( ( 1 + x ) / ( 1 - x ) ) - i \pi$ when z approaches the real value $x \in ( - 1 , 1 )$ from above, and that $\log ( ( z + 1 ) / ( z - 1 ) ) = \log ( ( 1 + x ) / ( 1 - x ) ) + i \pi$ when $z$ approaches $x$ from below, we obtain

$$
\begin{array} { l } { { \displaystyle \mu _ { 2 j + 1 } = - \frac { 1 } { 2 \pi i } \int _ { - 1 } ^ { 1 } { \displaystyle z ^ { 2 j } \left[ \left( \log \frac { 1 + x } { 1 - x } + i \pi \right) ^ { - 1 } - \left( \log \frac { 1 + x } { 1 - x } - i \pi \right) ^ { - 1 } \right] } d x } } \\ { { \mathrm { } ~ = \displaystyle \int _ { - 1 } ^ { 1 } { \displaystyle z ^ { 2 j } \left[ \left( \log \frac { 1 + x } { 1 - x } \right) ^ { 2 } + \pi ^ { 2 } \right] ^ { - 1 } } d x > 0 ~ . } } \\ { { \mathrm { } ~ } } \\ { { \displaystyle \neg \emptyset ~ } } \end{array}
$$

QED.

For another proof of this lemma, which avoids complex analysis, see Exercise 10.

Proof of Theorem 3.5. We insert the series (3.19) into (3.18) and obtain

where

$$
\begin{array} { r l r } { {  { R ( z ) ( \log \frac { z + 1 } { z - 1 } ) ^ { - 1 } - S ( z ) } } } & { { } } & { { ( 3 ) } } \\ { { } } & { { = { \mathrm { p o l y n o m i a l } } ( z ) + { d _ { 1 } } z ^ { - 1 } + { d _ { 2 } } { z ^ { - 2 } } + { 0 } ( z ^ { - 3 } ) } } \\ { { } } & { { } } & { { } } \\ { { d _ { 1 } = - \mu _ { 1 } a _ { 0 } - \mu _ { 3 } a _ { 2 } - \mu _ { 5 } a _ { 4 } - \dots } } & { { } } & { { ( 3 ) } } \\ { { } } & { { } } & { { d _ { 2 } = - \mu _ { 3 } a _ { 1 } - \mu _ { 5 } a _ { 3 } - \mu _ { 7 } a _ { 5 } - \dots . } } \end{array}
$$

Lemma 3.6 together with the positivity of the μ, (Lemma 3.8) implies that all summands in the above formulas for $d _ { 1 }$ and $d _ { 2 }$ have the same sign. Since $a _ { k - 1 } \neq 0$ we therefore have $d _ { 2 } \neq 0$ for $k$ even and $d _ { 1 } \neq 0$ for $k$ odd. The first two bounds of Theorem 3.5 are now an immediate consequence of Formula (3.18).

Finally, we prove that $p \leq k$ for $\beta _ { k } / \alpha _ { k } \leq 0$ : assume, by contradiction, that the order is greater than $k$ .Then by Formula (3.18), S (z) is equal to the principal part of $R ~ ( \boldsymbol { z } ~ ) ( \log ( ( \boldsymbol { z } + 1 ) / ( \boldsymbol { z } - 1 ) ) ) ^ { - 1 }$ , and we may write (putting $\mu _ { j } = 0$ for even $j$ ）

$$
S \left( z \right) = R \left( z \right) \left( \frac { z } { 2 } - \sum _ { j = 1 } ^ { k - 1 } { \mu _ { j } z ^ { - j } } \right) + \sum _ { j = 1 } ^ { k - 1 } { \left( \sum _ { s = j } ^ { k - 1 } { \mu _ { s } \alpha _ { s - j } } \right) z ^ { - j } } .
$$

Setting $z = 1$ we obtain

$$
\frac { S \left( 1 \right) } { R \left( 1 \right) } = \left( \frac { 1 } { 2 } - \sum _ { j = 1 } ^ { k - 1 } \mu _ { j } \right) + \sum _ { j = 1 } ^ { k - 1 } \left( \sum _ { s = j } ^ { k - 1 } \mu _ { s } a _ { s - j } \right) \frac { 1 } { R \left( 1 \right) } .
$$

Since by formula (3.17), $S \left( 1 \right) = \mathsf { \beta } _ { k }$ and $\boldsymbol { R } \ ( 1 ) = \boldsymbol { \alpha } _ { k }$ , it is sufficient to prove $S \left( 1 \right) / R \left( 1 \right) > 0$ Formula (3.19), for $z  1$ ， gives

$$
\sum _ { j = 1 } ^ { \infty } \mu _ { j } = \frac { 1 } { 2 } \mathrm { ~ , ~ }
$$

so that the first summand in (3.23) is strictly positive. The nonnegativity of the second summand is seen from the Lemmas 3.6 and 3.8. QED.

The stable multistep methods which attain the highest possible order $k + 2$ have a very special structure.

Theorem 3.9. Stable multistep methods of order k $+ 2$ are symmetric, i.e,

$$
\alpha _ { j } ^ { } \ = \ - \alpha _ { k - j } ^ { } \ , \qquad \beta _ { j } ^ { } \ = \ \beta _ { k - j } \qquad f o r \ a l l \quad j ^ { } \ .
$$

Remark: For symmetric multistep methods we have $\mathsf { p } \left( \boldsymbol { \zeta } \right) = - \boldsymbol { \zeta } ^ { k } \mathsf { p } \left( 1 / \zeta \right)$ by definition. Since with $\zeta _ { i }$ also $1 / \zeta _ { i }$ is a zero of $\rho ( \zeta )$ , all roots of stable sym metric multistep methods lie on the unit circle and are simple.

Proof: A comparison of the formulas (3.18) and (3.21) shows that $d _ { 1 } { = } 0$ is necessary for order $k + 2$ . Since the method is assumed to be stable, Lemma 3.6 implies that all even coefficients of $R \ ( z )$ vanish. Hence, $k$ is even and $R$ $( z$ ） satisfies the relation $R \ ( z ) = - R \ ( - z )$ By definition of $R \ ( z )$ this relation is equivalent to $p \left( \zeta \right) = - \zeta ^ { k } \rho \left( 1 / \zeta \right)$ ， which implies the first condition of (3.24). Using the above relation for R $\left( z \right)$ one obtains from Formula (3.18) that $S \left( z \right) - S \left( - z \right)$ ${ \bf \delta } = { \bf O } ( ( 2 / z ) ^ { 2 } )$ ， implying $S \left( z \right) = S \left( - z \right)$ . If this relation is transformed into an equivalent one for $\sigma ( \zeta )$ ， one gets the second condition of (3.24). QED.

# Exercises

1. Consider the linear difference equation (3.6) with

$$
\mathsf { \rho } ( \boldsymbol { \zeta } ) = \mathsf { \alpha } _ { k } \boldsymbol { \zeta } ^ { k } + \mathsf { \alpha } _ { k - 1 } \boldsymbol { \zeta } ^ { k - 1 } + \cdots + \mathsf { \alpha } _ { 0 }
$$

as characteristic polynomial. Let $\zeta _ { 1 } , \dots , \zeta _ { l }$ be the different roots of $\rho ( \zeta )$ and let $m _ { j } \geq 1$ be the multiplicity of the root $\zeta _ { j }$ . Show that the sequences

$$
\{ \left. { \binom { n } { i } } \zeta _ { j } ^ { n - i } \right\} _ { n \geq 0 }
$$

form for $1 \le j \le l$ and $0 \leq i \leq m _ { j } - 1$ a system of $k$ linearly independent solutions of (3.6).

2. Show that all roots of the polynomial $p \left( z \right)$ of Formula (3.11) except the simple root $0$ lie in the annulus

$$
{ \frac { k } { k - 1 } } \leq | z | \leq 2 .
$$

Hint. Use the following lemma, which can be found in Marden (1966)，p.137:ifallcoefficientsofthepolynomial $a _ { k } \ : z ^ { k } \ : + a _ { k - 1 } \ : z ^ { k - 1 } + \cdot \cdot \cdot + a _ { 0 }$ arerealandpositive,thenitsotsie in the annulus ${ \boldsymbol { \rho } } _ { 1 } \leq \left| z \right| \leq { \boldsymbol { \rho } } _ { 2 }$ with ${ \boldsymbol \rho } _ { 1 } = { \mathrm { m i n } }$ $( a _ { j } / a _ { j + 1 } )$ and ${ \rho } _ { 2 } = { \textrm { m a x } }$ $( a _ { j } / a _ { j + 1 } )$

3. Apply the lemma of the above example to $\rho ( \zeta ) / ( \zeta - 1 )$ and show that the BDF-formulas are stable for $k = 1 , 2 , 3 , 4$

4. Give a different proof of Theorem 3.4 by applying the Schur-Cohn criterion to the polynomial

$$
f \left( z \right) = z ^ { k } \rho ( \frac { 1 } { z } ) = \sum _ { j = 1 } ^ { k } \frac { 1 } { j } ( 1 { - } z ) ^ { j } .
$$

Schur-Cohn criterion (see e.g. Marden (1966), Chapter X). For a given polynomial with real coefficients

$$
f ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { k } z ^ { k }
$$

we consider the coefficients $a _ { i } ^ { ( j ) }$ where

$$
\begin{array} { r l r } { a _ { i } ^ { ( 0 ) } = a _ { i } } & { { } \quad i = 0 , 1 , \ldots , k } & { \qquad ( 3 } \\ { a _ { i } ^ { ( j + 1 ) } = a _ { 0 } ^ { ( j ) } a _ { i } ^ { ( j ) } - a _ { k - j } ^ { ( j ) } a _ { k - j - i } ^ { ( j ) } } & { { } \quad \mathrm { f o r } i = 0 , \ldots , k - j - 1 } \end{array}
$$

and also the products

$$
P _ { 1 } = \alpha _ { 0 } ^ { ( 1 ) } , \qquad P _ { j + 1 } = P _ { j } \alpha _ { 0 } ^ { ( j + 1 ) } \qquad \mathrm { f o r } j = 1 , , . . . , k - 1 \ ,
$$

We further denote by n the number of negative elements among $P _ { 1 } , \dots , P _ { k }$ and by $p$ 'the number of positive elements. Then $f \left( z \right)$ has at least n zeros inside the unit disk and at least $p$ zeros outside it.

a) Prove the following formulas for the coefficients of (3.25):

$$
a _ { 0 } = \sum _ { i = 1 } ^ { k } { \frac { 1 } { i } } \qquad a _ { 1 } = - k \qquad a _ { 2 } = { \frac { k ( k - 1 ) } { 4 } }
$$

Table 3.1 Signs of $a _ { 0 } ^ { \ ( j ) }$   

<table><tr><td>k</td><td>2345678910111213&gt;13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>j=1</td><td>十</td><td>+</td><td>十</td><td>+</td><td>+</td><td></td><td></td><td>冏十</td><td>十</td><td>+</td><td>+</td><td>十</td><td>+</td></tr><tr><td>j=2</td><td>0</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>十</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>j=3</td><td></td><td>0</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td></td><td></td></tr><tr><td>j=4</td><td></td><td></td><td>0</td><td>+</td><td>+</td><td>+</td><td>一</td><td>一</td><td>1</td><td>一</td><td></td><td></td><td></td></tr><tr><td>j=5</td><td></td><td>，</td><td></td><td>0</td><td>+</td><td>一</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

$$
\begin{array} { c c c } { { \displaystyle a _ { k - 2 } = \left( - 1 \right) ^ { k } \frac { k \left( k - 1 \right) } { 2 \left( k - 2 \right) } } } & { { } } & { { \displaystyle a _ { k - 1 } = \left( - 1 \right) ^ { k - 1 } \frac { k } { k - 1 } } } & { { \quad a _ { k } = \left( - 1 \right) ^ { k } \frac { 1 } { k } } } \end{array}
$$

b)Verifythat thecofficients $a _ { 0 } ^ { ( j ) }$ of (3.26) have the sign structure of Table 3.1. For $k < 1 3$ these tedious calculations can be performed on a computer - in order to avoid round-off errors - by $a _ { \ : 0 } ^ { \ : ( 1 ) } > 0$ afd $a _ { \cap } ^ { ( 2 ) } > 0$ isnipsy iorl $k > 2$ In The verieaion oi

$a _ { 0 } ^ { ( 3 ) } = ( a _ { 0 } ^ { ( 2 ) } ) ^ { 2 } - ( a _ { k - 2 } ^ { ( 2 ) } ) ^ { 2 } < 0$ for $k \geq 1 3$ consider the expression

$$
\begin{array} { r l } { { a _ { 0 } ^ { ( 2 ) } - \left( - 1 \right) ^ { k } a _ { k - 2 } ^ { ( 2 ) } } } & { { = a _ { 0 } ^ { ( 1 ) } [ a _ { 0 } ^ { 2 } - a _ { k } ^ { 2 } - a _ { 0 } | a _ { k - 2 } | + a _ { 2 } | a _ { k } | ] } } \\ { { } } & { { - \ | a _ { k - 1 } ^ { ( 1 ) } | \cdot ( a _ { 0 } + | a _ { k } | ) ( | a _ { k - 1 } | + a _ { 1 } ) } } \end{array}
$$

which can be written in the form $( a _ { 0 } + | a _ { k } | ) \phi ( k )$ with

$$
\begin{array} { r l } { \Phi ( k ) = ( a _ { 0 } - | a _ { k } | ) \biggl ( a _ { 0 } ^ { 2 } - a _ { k } ^ { 2 } - a _ { 0 } | a _ { k - 2 } | + a _ { 2 } | a _ { k } | \biggr ) - | a _ { k - 1 } ^ { ( 1 ) } | \cdot ( a _ { 1 } + | a _ { k } | ) } & { } \\ { = a _ { 0 } ^ { 3 } - a _ { 0 } ^ { 2 } \biggl ( \displaystyle \frac { k } { 2 } + \frac { 1 } { 2 } + \frac { 1 } { k - 2 } + \frac { 1 } { k } \biggr ) } & { } \\ { + a _ { 0 } \biggl ( \displaystyle \frac { 5 k } { 4 } + \frac { 1 } { 4 } + \frac { 1 } { 2 k - 4 } - \frac { 1 } { k - 1 } - \frac { 1 } { \left( k - 1 \right) ^ { 2 } } - \frac { 1 } { k ^ { 2 } } \biggr ) } & { } \\ { - \left( k - \displaystyle \frac { 3 } { 4 } - \frac { 1 } { k - 1 } - \frac { 1 } { 4 k } - \frac { 1 } { k ^ { 3 } } \right) . } & { } \end{array}
$$

Show that $\phi ( 1 3 ) < 0$ and that $\phi$ is monotonically decreasing for $k \geq 1 3$ (observe that $\boldsymbol { a } _ { 0 } = \boldsymbol { a } _ { 0 } ( \boldsymbol { k } )$ actually depends on $k$ and that （3.29） that $a _ { 0 } ( k + 1 ) = a _ { 0 } { \left( k \atop 0 \right) } + 1 / \left( k + 1 \right) )$ $a _ { 0 } ^ { ( 3 ) } < 0$ for $k \geq 1 3$ . Finally, deduce from the negativity of

c) Use Table 3.1 and the Schur-Cohn criterion for the verification of Theorem 3.4.

5. (Multistep methods of maximal order). Verify the following state-ments:

a) there is no $k$ -step method of order 2k +1,

b) there is a unique (implicit) k -step method of order $2 k$ ， c) thcrc is a unique explicit k -step method of order $2 k - 1$

6. Provc that symmctric multistep methods arc always of even order More prccisely, if a symmetric multistep method is of order $2 s - 1$ then it is also of order $2 s$

7. Show that all stable 4-step methods of order 6 are given by

$$
\rho ( \zeta ) = ( { \zeta } ^ { 2 } - 1 ) ( { \zeta } ^ { 2 } + 2 \mu \zeta + 1 ) , \quad \vert \mu \vert < 1 ,
$$

$$
\sigma ( \zeta ) = \frac { 1 } { 4 5 } \bigl ( 1 4 - \mu \bigr ) \bigl ( \zeta ^ { 4 } + 1 \bigr ) ^ { - } + \frac { 1 } { 4 5 } \bigl ( 6 4 + 3 4 \mu \bigr ) \zeta \bigl ( \zeta ^ { 2 } + 1 \bigr ) + \frac { 1 } { 1 5 } \bigl ( 8 + 3 8 \mu \bigr ) \zeta ^ { 2 }
$$

Compute the error constant and observe that it cannnot become arbitrarily small.

R esult. $C = - ( 1 6 - 5 \mu ) / \left( 7 5 6 0 ( 1 + \mu ) \right) .$

8. Prove the following bounds for the error constant:

a) For stable methods of order k $+ 2$ ，

$$
{ \cal C } \ \le \ - 2 ^ { - 1 - k } \mu _ { k + 1 } \ .
$$

b) For stable mcthods of order $k + 1$ with odd $k$ we have

$$
{ \cal C } \ \le \ - 2 ^ { - k } \mu _ { k } \ .
$$

c) For stable explicit methods of order $k$ we have ( ${ \boldsymbol { \mu } } _ { j } = 0$ for even $j )$

$$
C \ \geq \ 2 ^ { 1 - k } \left( \frac 1 2 - \sum _ { j = 1 } ^ { k - 1 } \mu _ { j } \right) \ .
$$

Show that all these bounds are optimal.

Hin $\mathrm { ~  ~ { ~ \sigma ~ } ~ } ( 1 ) { = } 2 ^ { k - 1 } a _ { k - 1 }$

9. The coefficients tion $\mu _ { j }$ of Formula (3.19) satisfy the recurrence rela-

$$
{ \mu } _ { 2 j + 1 } + \frac { 1 } { 3 } { \mu } _ { 2 j - 1 } + \cdot \cdot \cdot + \frac { 1 } { 2 j + 1 } { \mu } _ { 1 } = \frac { 1 } { 4 j + 6 } \mathrm { ~ . ~ }
$$

The first of these coefficients are given by

$$
\mu _ { 1 } = \frac { 1 } { 6 } , \mu _ { 3 } = \frac { 2 } { 4 5 } , \mu _ { 5 } = \frac { 2 2 } { 9 4 5 } , \mu _ { 7 } = \frac { 2 1 4 } { 1 4 1 7 5 } .
$$

10.Another proof of Lemma 3.8.

Multiplying (3.30) by $2 j + 3$ and subtracting from it the same for-mula with $j$ replaced by $j - 1$ yields

$$
( 2 j + 3 ) \mu _ { 2 j + 1 } + \sum _ { i = 0 } ^ { j - 1 } \mu _ { 2 i + 1 } \left( \frac { 2 j + 3 } { 2 j - 2 i + 1 } - \frac { 2 j + 1 } { 2 j - 2 i - 1 } \right) = 0 \mathrm { ~ . ~ }
$$

Show that the expression in brackets is negative and deduce the result of Lem ma 3.8 by a simple induction argument.

# I11.4. Convergence of multistep methods

ist das Adams'sche Verfahren jedem anderm bedeutend uberlegen. Wenn es gleichwohl nicht gendgend allgemein angewandt wird und, besonders in Deutschland, gegenuber den von Runge, Heun und Kutta entwickelten Methoden zurdcktritt, so mag dies daran liegen, dass bisher eine brauchbare Untersuchung der Genauigkeit der Adams'schen Integration gefehlt hat. Diese Lucke soll hier ausgefulit werden..." (R.v. Mises, 1930)

The convergence of Adams methods was investigated in the influential article of von Mises (1930)， which was followed by an avalanche of papers improving the error bounds and applying the ideas to other special multistep methods, e.g. Tollmien (1938), Fricke (1949)， Weissinger (1950)， Vietoris (1953). A general convergence proof for the method (2.1), however, was first given by Dahlquist (1956)， who gave necessary and suficient conditions for convergence. Great elegance was introduced in the proofs by the ideas of Butcher (1966)，where multistep form ulas are written as one-step formulas in a higher dimensional space. Furthermore, the resulting presentation can easily be extended to a more general class of integration methods (see Section II1.8).

Wc cannot expect reasonable convergence results of numerical methods, if the differential equation problem

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

does not possess a unique solution. We therefore make the following assumptions, which were seen in Sections I.7 and I.9 to be natural for our purpose:

$f$ is continuous on $D = \{ ( x \ , y ) ; x \in [ x \ _ { 0 } , \hat { x } \ ] , \ | | \ y ( x \ ) - y \ | | \leq b \ \}$ where $y \left( x \right)$ denotes the exact solution of (4.1) and $b$ is some positive number.

Furthermore $f$ satisfies the Lipschitz  condition $\| ~ f \left( x , y \right) - f \left( x , z \right) \| ~ \leq ~ L ~ \| ~ y - z ~ \|$ for (x,y), (x,z)∈D

If we apply the multistcp method (2.1) with step size h to the problem (4.1) we obtain a sequence $\left\{ y _ { i } \right\} .$ For given $x$ and h such that $( x - x _ { 0 } ) / h = n$ is an integer, we introduce the following notation for the numerical solution:

$$
y _ { h } ( x ) = y _ { n } \qquad { \mathrm { i f } } \quad x - x _ { 0 } = n h .
$$

A multistep method is expected to be "good" in the sense that the numerical solution $y _ { h } \left( x \right)$ converges to the exact solution $y \left( x \right)$ as $h  \mathrm { ~ 0 ~ }$ . In addition, we expect rapid convergence when $f$ , in addition to (4.2), is smoother.

Definition 4.1. (Convergence)

i) The linear muitistep method (2.1) is called convergent, if for all initial value problems (4.1) satisfying (4.2)

$$
y \left( x \right) - y _ { h } \left( x \right) \to 0 \qquad \mathrm { f o r } \ h \to 0 , \ x \in [ x _ { 0 } , \hat { x } ]
$$

whenever the starting values satisfy

$$
y \left( x _ { 0 } + i h \right) - y _ { h } \left( x _ { 0 } + i h \right) \prec 0 \qquad \mathrm { f o r } \quad h \prec 0 , i = 0 , 1 , \ldots , k - 1 \ .
$$

ii) Method (2.1) is convergent of order $p$ ,if to any problem (4.1) with $f$ sufficiently differentiable, there exists a positive ${ \mathfrak { h } } _ { 0 }$ such that

$$
| |  { y } ( x ) - y _ { h } ( x ) | | \le C h ^ { p } \qquad \mathrm { f o r } h \le h _ { 0 }
$$

whenever the starting values satisfy

$$
\mid y ( x _ { 0 } + i h ) - y _ { h } ( x _ { 0 } + i h ) \mid \mid \leq C _ { 0 } h ^ { p } \quad \mathrm { f o r } \quad h \leq h _ { 0 } , i = 0 , 1 , \ldots , k - 1 ~ .
$$

In this definition we clearly assume that a solution of (4.1) exists on $[ x _ { 0 } , \hat { x } ]$

The aim of this section is to prove that stability together with consistency are necessary and sufficient for the convergence of a multistep method. This is expressed in the famous slogan

$$
c o n \nu e r g e n c e \ = s t a b i l i t y \ + \ c o n s i s t e n c y
$$

(compare also Lax-Richtmyer (1956)). We begin with the study of necessary conditions for convergence.

Theorem 4.2. If the multistep method (2.1) is convergent, then it is necessarily

i) stable and ii) consistent (i.e. of order 1: ${ \mathsf p } ( 1 ) { = } 0 , { \mathsf p } ^ { \prime } ( 1 ) { = } { \sigma } ( 1 ) ) .$

Proof: Application of the multistep method (2.1) to the differential equation $y \prime { = } 0$ ， $y \left( 0 \right) { = } 0$ yields the difference equation (3.6). Suppose, by contradiction, that $\rho ( \zeta )$ has a root $\zeta _ { 1 }$ with $| \zeta _ { 1 } | > 1$ or a root $\boldsymbol { \zeta } _ { 2 }$ on the unit circle, whose multiplicity exceeds 1. $\zeta _ { 1 } ^ { n }$ and $n \zeta _ { 2 } ^ { n }$ are then divergent solutions of (3.6). Multiplying by Vh we achieve that the starting values converge to ${ { y } _ { 0 } } \mathrm { { = } } 0$ for $h  \mathrm { ~ 0 ~ }$ .Since $y _ { h } \left( x \right) = \sqrt { h } \ \zeta _ { 1 } ^ { x / h }$ and $y _ { h } ( x ) { = } ( x / \sqrt { h } ) \zeta _ { 2 } ^ { x / h }$ remain divergent for every fixed $x$ ， we have a contradiction to the assumption of convergence The method (2.1) must therefore be stable.

We next consider the initial value problem $y ^ { \prime } { = } 0$ ， $y \left( 0 \right) = 1$ with exact solution $y \left( x \right) = 1$ . The corresponding difference equation is again that of (3.6), which, in the new notation, can be written as

$$
\alpha _ { k } y _ { h } ( x + k h ) + \alpha _ { k - 1 } y _ { h } ( x + ( k - 1 ) h ) + \cdot \cdot \cdot + \alpha _ { 0 } y _ { h } ( x ) = 0 .
$$

Letting $h  ~ 0$ , convergence immediately implies $\rho ( 1 ) { = } 0$

Finally we apply Method (2.1) to the problem $y ^ { \prime } { = } 1$ ， $y \left( 0 \right) { = } 0$ The exact solution is $y \left( x \right) = x$ . Since we already know $\rho ( 1 ) = 0$ , it is easy to verify that a particular numerical solution is given by ${ y _ { n } } = n h K$ or $y _ { h } \left( x \right) = x K$ where $K = \scriptstyle \sigma ( 1 ) / \rho ^ { \prime } ( 1 )$ By convergence $K = 1$ is necessary. QED.

Although the statement of Theorem 4.2 was derived from a consideration of aimost trivial differential equations, it is remarkable that Conditions i) and ii) will turn out to be not only necessary but also sufficient for convergence.

# Formulation as one-step method

We are now at the point where it is useful to rewrite a multistep method as a one-step method in a higher dimensional space (see Butcher (1966),Skeel (1976)).Fo thislet $\ d _ { i } = \ d _ { \mathscr { W } } \left( \ d _ { x _ { i } } , \ d _ { y _ { i } } , . . . , \ d _ { y _ { i + k - 1 } } , \ d _ { h } \right)$ be defined implicitly by

$$
\Psi = \sum _ { j = 0 } ^ { k - 1 } \mathsf { \mathsf { B } } _ { j } ^ { \prime } f \left( x _ { i } + j h , y _ { i + j } \right) + \mathsf { \mathsf { B } } _ { k } ^ { \prime } f \left( x _ { i } + k h , h \bar { \Psi } - \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j } ^ { \prime } y _ { i + j } \right)
$$

where $\alpha _ { j } ^ { \prime } = \alpha _ { j } / \alpha _ { k }$ and $\beta _ { j } ^ { \prime } = \beta _ { j } / \alpha _ { k }$ . Multistep formula (2.1) can then be written as

$$
y _ { i + k } = - \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j } ^ { \prime } y _ { i + j } + h \psi .
$$

Introducing the $m \cdot k$ -dimensional vectors ( $_ m$ is the dimension of the differential equation)

$$
Y _ { i } = ( y _ { i + k - 1 } , y _ { i + k - 2 } , \dots , y _ { i } ) ^ { T } , \quad i \ge 0
$$

and

$$
\textbf {  { A } } = \left( \begin{array} { c c c c c c } { - \alpha _ { k - 1 } ^ { \prime } } & { - \alpha _ { k - 2 } ^ { \prime } } & { . . . } & { . } & { - \alpha _ { 0 } ^ { \prime } } \\ { 1 } & { 0 } & { . . . } & { . } & { 0 } \\ { 1 } & { 1 } & { . } & { 0 } \\ & & & { . } & { 0 } \\ & & & { \vdots } & { \vdots } \\ & & & { 1 } & { 0 } \end{array} \right) ~ , ~ e _ { 1 } = \left( \begin{array} { c } { 1 } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right)
$$

the multistep method (4.5) can be written - after adding some trivial identities - in compact form as

$$
Y _ { i + 1 } = ( A \otimes I ) Y _ { i } + h \Phi ( x _ { i } , Y _ { i } , h ) , \qquad i \geq 0
$$

with

$$
\Phi ( x _ { i } , Y _ { i } , h ) = ( e _ { 1 } \otimes I ) \Psi ( x _ { i } , Y _ { i } , h ) .
$$

Here, $A \otimes I$ denotes the Kronecker tensor product, i.e. the $m \cdot k \textrm { - }$ dimensional block matrix with $( m \textrm { , } m$ )-blocks $a _ { i j } I$ . Readers unfamiliar with the notation and properties of this product may assume for sim-plicity that (4.1) is a scalar equation ( $m = 1$ ) and A $\otimes I = A$ ·

The following lemmas express the concepts of order and stability in this new notation.

Lemma 4.3. Let $y \left( x \right)$ be the exact solution of (4.1). For $i = 0 , 1 , \ldots ,$ we define the vector $Y _ { i + 1 }$ as thenumericalsolutionofonestep

$$
\hat { Y } _ { i + 1 } = ( A \otimes I ) Y ( x _ { i } ) + h \Phi ( x _ { i } , Y ( x _ { i } ) , h )
$$

with correct starting values

$$
\boldsymbol { Y } \left( \boldsymbol { x } _ { i } \right) = \left( y \left( x _ { i + k - 1 } \right) , y \left( x _ { i + k - 2 } \right) , \ldots , y \left( x _ { i } \right) \right) ^ { T } .
$$

i) If the multistep method (2.1) is of order 1 and if $f$ satisfies (4.2) , then ar $~ h _ { 0 } > 0$ exists such that for $h \leq h _ { \mathrm { ~ 0 ~ } }$

$$
| | \textit { Y } ( x _ { i + 1 } ) - \hat { Y } _ { i + 1 } | | \leq h \omega ( h ) , \qquad 0 \leq i \leq \hat { x } / h - k
$$

where $w ( h ) \to 0 f o r h \to 0$

ii) If the multistep method (2.1) is of order $\boldsymbol { p }$ and if $f$ is sufficientty differentiable then a constant $M$ exists such that for h small enough

$$
| | \ : Y ( x _ { i + 1 } ) - \hat { Y } _ { i + 1 } | | \le M h ^ { p + 1 } , \qquad 0 \le i \le \hat { x } / h - k .
$$

Pro0f: The first component of $Y \left( x _ { i + 1 } \right) - { \hat { Y } } _ { i + 1 }$ is just the local error as given by Definition 2.1. Since the remaining components all vanish Exercise 5 of Section II.2 and Definition 2.3 yield the result. QED.

Lemma 4.4. Suppose that the multistep method (2.1) is stable. Then thereexiss aveorpo n $\mathbb { R } ^ { m k }$ )such thatexf (4.7) satisfies

$$
\left| \left| \begin{array} { l l l }  A \otimes I \ \right| \ \right| \ \leq 1 \end{array}
$$

in the subordinate matrix norm.

Proof: If λ is a root of $\rho ( \zeta )$ , then the vector $( \lambda ^ { k - 1 } , \ \lambda ^ { k - 2 } \ , \ \dots \ 1 )$ is an eigenvector of the matrix A with eigenvalue 入. Therefore the eigenvalues of A (which are the roots of $\rho ( \zeta )$ ) satisfy the root condi-

tion by Definition 3.2. A transformation to Jordan canonical form therefore yields (see Section I.12)

$$
\begin{array}{c} \boldsymbol { T } ^ { - 1 } \boldsymbol { A } _ { \textit { T } } = \boldsymbol { J } = [ \begin{array} { c c c c c } { \lambda _ { 1 } } & & & & & \\ & & & & \\ & & & & & \\ & { \cdots } & & & \\ & & & & & { 0 } \end{array} ] \boldsymbol { \epsilon } _ { \textit { T } } = \ldots \ldots \ldots \ldots \ldots \ldots  \\ { \boldsymbol { T } ^ { - 1 } \boldsymbol { A } _ { \textit { T } } = \boldsymbol { J } = [ \begin{array} { c c c c c } { \lambda _ { 1 } } & & & & \\ & & & & \\ & & { \ddots } & & \\ & & & & \\ & & & & { \ddots } & \\ & & & & & \end{array} ] \boldsymbol { \hat { \epsilon } } _ { \textit { T } } = \boldsymbol { \hat { \epsilon } } _ { \textit { T } } } \\ { 0 } & & & & { \ddots \ \boldsymbol { \epsilon } _ { \textit { T } - 1 } } \\ & & & & & { \boldsymbol { \hat { \epsilon } } _ { \textit { T } } = \boldsymbol { \hat { \epsilon } } _ { \textit { T } } } \end{array} ] \boldsymbol { \hat { \epsilon } } _ { \textit { T } }
$$

where $\lambda _ { 1 } , \dots , \lambda _ { l }$ are the eigcnvalues of modulus 1, which must be simple. We further find by a suitable multiplication of the columns of T that $\vert \epsilon _ { j } \vert < 1 - \vert \lambda _ { j } \vert$ for $j = l + 1 ~ , ~ \dots ~ , k - 1$ . Because of (9.11') of Chapter I we then have $\| J \otimes I \| _ { \infty } \leq 1$ . Using the transform ation $T$ of (4.9) we define the norm $\mid \mid x \mid \mid : = \mid \mid ( T ^ { - 1 } { \otimes } I ) x \mid \mid _ { \infty } .$ This yields

$$
\begin{array} { r } { \left| \mid ( A \otimes I ) x \mid \right| \ = \mid \mid ( T ^ { - 1 } \otimes I ) ( A \otimes I ) x \mid \mid _ { _ { \infty } } = \mid \mid ( J \otimes I ) ( T ^ { - 1 } \otimes I ) x \mid \mid _ { _ { \infty } } } \\ { \leq \mid \mid ( T ^ { - 1 } \otimes I ) x \mid \mid _ { _ { \infty } } = \mid \mid x \mid \mid } \end{array}
$$

and hence also $\| A \otimes I \| \leq 1 .$ QED.

# Proof of con vergence

The convergence theorem for multistep methods can now be established.

Theorem 4.5. If the multistep method $( 2 . I )$ is stable and of order 1 then it is convergent. If Method (2.1) is stable and of order p then it is convergent of order p.

Proof: As in the convergence theorem for one-step methods (Section I.3) we may assume without loss of generality that $f \left( x , y \right)$ is defined for all $y \in \mathbb { R } ^ { m }$ ， ${ \boldsymbol { x } } \in [ { \boldsymbol { x } } _ { 0 } , { \boldsymbol { \hat { x } } } ]$ and satisfies there a (global) Lipschitz condition. This implies that for suficiently small h the functions $\Psi ( x _ { i } , Y _ { i } , h )$ and $\Phi ( x _ { i } , Y _ { i } , h )$ satisfy a Lipschitz condition with respect to the second argument (with Lipschitz constant $L ^ { * }$ ). For the function $G$ defined by Formula (4.8) which maps the vector $Y _ { i }$ onto $Y _ { i + 1 }$ we thus obtain from Lemma 4.4

$$
\begin{array} { r }  | | \begin{array} { l l } { G ( Y _ { i } ) - G ( Z _ { i } ) | | \ \leq \ ( 1 + h L ^ { * } ) | | | \begin{array} { l l } { Y _ { i } - Z _ { i } } \end{array} | | \ . } \end{array} \end{array}
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/6d0070765f27c42354b5e5a0501e28c95c516d28dbb220aa2b9bd4a46f925a84.jpg)  
Figure 4.1. Lady Windermere's Fan for muitistep methods

The rest of the proof now proceeds in the same way as for one-step methods and is illustrated in Figure 4.1. The arrows in Figure 4.1 indicate the application of $G$ .From Lemma 4.3 we know that $| | \begin{array} { l } { Y ( x _ { i + 1 } ) } \end{array}  - G ( Y ( x _ { i } ) ) | | \leq h \omega ( h )$ . This together with (4.10) shows that the local error $Y \left( x _ { i + 1 } \right) \ - G \left( Y \left( x _ { i } \right) \right)$ at stage $i + 1$ causes an error at stage $m$ , Which is at most $h \ \omega ( h ) ( 1 + h L ^ { * } ) ^ { m - i + 1 } .$ Thus we have

$$
\begin{array} { r l r } {  { \|  { Y } ( x _ { m } ) - Y _ { m } \| \ \le \ \|  { Y } ( x _ { 0 } ) - Y _ { 0 } \| \ ( 1 + h L ^ { * } ) ^ { m } } } & { ( 4 . } & \\ & { + \ h \omega ( h ) [ ( 1 + h L ^ { * } ) ^ { m - 1 } + ( 1 + h L ^ { * } ) ^ { m - 2 } + \cdot \cdot \cdot + 1 ] } & \\ & { \le \ \|  { Y } ( x _ { 0 } ) - Y _ { 0 } \| \exp ( m h L ^ { * } ) + \frac { \omega ( h ) } { L ^ { * } } ( \exp ( m h L ^ { * } ) - 1 ) \ . } & \end{array}
$$

Convergence of Method (2.1) is now an immediate consequence of Formula (4.11). If the multistep method is of order $p$ ，the same proof with $\omega ( h )$ replaced by $M h ^ { p }$ yields convergence of order $p$ ， QED.

# Exercises

1. Consider the function (for $x \ge 0$ ）

$$
f \left( x , y \right) = \left\{ \begin{array} { l l } { 2 x , \qquad } & { y \leq 0 } \\ { 2 x - \frac { 4 y } { x } , \quad } & { 0 < y < x ^ { 2 } } \\ { - 2 x , \qquad } & { y \geq x ^ { 2 } . } \end{array} \right.
$$

a) Show that $y \left( x \right) = x ^ { 2 } / 3$ isthe unique solutionof $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( 0 \right) { = } 0$ ,although $f$ does not satisfy a Lipschitz condition near the origin.

b) Apply the mid-point rule (2.2') with starting values $y _ { 0 } { = } 0$ ， $y _ { 1 } = - h ^ { 2 }$ to the above problem and verify that the numerical solution at $x = n h$ is given by $y _ { h } \left( x \right) = \mathbf { \Psi } ( - 1 ) ^ { n } x ^ { 2 }$ (see Grigorieff (1977)).

2. Another motivation for the meaning of the error constant: sup-pose that 1 is the only eigenvalue of A in (4.7) of modulus one. Show that $( 1 , 1 , \ldots , 1 ) ^ { I }$ is the right 'eigenvector and $( 1 , 1 + \alpha ^ { \prime } { } _ { k - 1 } , 1 + \alpha ^ { \prime } { } _ { k - 1 } + \alpha ^ { \prime } { } _ { k - 2 } , \ldots )$ istheieft eigenvector tothis eigenvalue. The global contribution of the local error after many steps is then given by

$$
\begin{array} { r } { \boldsymbol { \mathsf { A } } ^ { \infty } \left( \begin{array} { l } { C _ { p + 1 } } \\ { 0 } \\ { : } \\ { 0 } \end{array} \right) = C \left( \begin{array} { l } { 1 } \\ { 1 } \\ { : } \\ { 1 } \end{array} \right) } \end{array} ,
$$

Multiply this equation from the left by the left eigenvector to show with (2.6) that $C$ is the error constant defined in (2.13).

Remark. For multistep methods with several eigenvalues of modulus 1, Formula (4.12) remains valid if $A ^ { \infty }$ is replaced by $E$ (see Section II1.8).

# III.5. Variable step size multistep methods

"Des war a harter Brockn, des..." (Tyrolean dialect)

It is clear from the considerations of Section I1.4 that an efficient integrator must be able to change the step size. However, changing the step size with multistep methods is difficult since the formulas of the preceding sections need the numerical approximations at equidistant points. There are in principle two possibilities for overcoming this difficulty:

i) use polynomial interpolation to reproduce the starting values at the new (equidistant) grid; ii) construct methods which are adjusted to variable gridpoints.

This section is devoted to the second approach. We investigate con-sistency, stability and convergence. The actual implementation (order and step size strategies) will be considered in Section IIl.7.

# Variable step size Adams methods

F. Ceschino (1961) was apparently the first person to propose a "smooth" transition from a step size $h$ to a new step size ωh . C.V.D. Forrington (1961) and later on F.T. Krogh (1969) extended his ideas: we consider an arbitrary grid $\left( x _ { n } \right)$ ）and denote the step sizes by ${ h _ { n } } = { x _ { n + 1 } } ^ { - x _ { n } }$ . We assume that approximations $y _ { j }$ to $y \left( x _ { j } \right)$ are known for $j = n - k + 1 ~ , ~ \ldots ~ , n$ and we put ${ f _ { j } } ^ { \mathrm { ~ } } { = } f _ { _ { \cdot } } ( x _ { _ { j } } , y _ { _ { j } } ) _ { _ { \cdot } }$ In the same way as in Section III.1 we denote by $p \left( t \right)$ the polynomial which interpolates the values $( x _ { j } , f _ { j } )$ for $j = n - k + 1 ~ , ~ \ldots ~ , ~ n$ . Using Newton's interpolation formula we have

$$
p \left( t \right) = \sum _ { j = 0 } ^ { k - 1 } \prod _ { i = 0 } ^ { j - 1 } \left( t - x _ { n - i } \right) f \left[ x _ { n } , x _ { n - 1 } , \ldots , x _ { n - j } \right]
$$

where the divided differences $f \left[ x _ { n } \ , \ \ldots , x _ { n - j } \right]$ are defined recursively by

$$
f [ x _ { n } ] = f _ { n } \qquad 
$$

For actual computations (see Krogh (1969)) it is practical to rewrite (5.1) as

$$
p ( t ) = \sum _ { j = 0 } ^ { k - 1 } \ \prod _ { i = 0 } ^ { j - 1 } \frac { t - x _ { n - i } } { x _ { n + 1 } - x _ { n - i } } \ \Phi _ { j } ^ { * } ( n )
$$

where

$$
\Phi _ { j } ^ { * } ( n ) = \prod _ { i = 0 } ^ { j - 1 } ( x _ { n + 1 } - x _ { n - i } ) \cdot f \left[ x _ { n } \ , \ \dots , x _ { n - j } \right] \ .
$$

We now define the approximation to $y \left( x _ { n + 1 } \right)$ by

$$
y _ { n + 1 } = y _ { n } + \intop _ { x _ { n } } ^ { x _ { n + 1 } } p \left( t \right) d t .
$$

Inserting Formula (5.1') into (5.4) we obtain

$$
y _ { n + 1 } = y _ { n } + h _ { n } \sum _ { j = 0 } ^ { k - 1 } g _ { j } ( n ) \Phi _ { j } ^ { * } ( n )
$$

with

$$
g _ { j } ( n ) = { \frac { 1 } { h _ { n } } } \int \prod _ { x _ { n } } ^ { x _ { n + 1 } } \prod _ { i = 0 } ^ { j - 1 } { \frac { t - x _ { n - i } } { x _ { n + 1 } - x _ { n - i } } } d t .
$$

Formula (5.5) is the extension of thc explicit Adams method (1.5) to variable step sizes. Observe that for constant step sizes the above expressions reduce to (Exercise 1)

$$
g _ { j } ( n ) = \gamma _ { j } , \qquad \Phi _ { j } ^ { * } ( n ) = \nabla ^ { j } f _ { n } \ .
$$

The variable step size implicit Adams methods can be deduced similarly. In analogy to Section III.1 we let $p ^ { * } ( t )$ be the polynomial of degree $k$ that interpolates $( x _ { j } , f _ { j } )$ for $j = n - k + 1 , \ldots , n , n + 1$ (The value ${ { f } _ { n + 1 } } \mathop { = } f \left( { { x } _ { n + 1 } } , { { y } _ { n + 1 } } \right)$ contains the unknown solution $y _ { n + 1 } )$ Again, using Newton's interpolation formula we obtain

$$
p ^ { * } ( t ) = p \left( t \right) + \prod _ { i = 0 } ^ { k - 1 } \left( t - x _ { n - i } \right) f \left[ x _ { n + 1 } , x _ { n } , \ldots , x _ { n - k + 1 } \right]
$$

The numerical solution, defined by

$$
y _ { n + 1 } = y _ { n } + \int _ { \mathbf { \Omega } } p ^ { * } ( t ) d t \mathrm { ~ , ~ }
$$

is now given by

$$
y _ { n + 1 } = p _ { n + 1 } + h _ { n } g _ { k } \left( n \right) \Phi _ { k } \left( n + 1 \right) ,
$$

where $p _ { n + 1 }$ is the numerical approximation obtained by the explici Adams method

$$
p _ { n + 1 } = y _ { n } + h _ { n } \sum _ { j \ { - } 0 } ^ { k - 1 } g _ { j } ( n ) \Phi _ { j } ^ { * } ( n )
$$

and where

$$
\Phi _ { k } \left( n + 1 \right) = \prod _ { i = 0 } ^ { k - 1 } ( x _ { n + 1 } - x _ { n - i } ) f \left[ x _ { n + 1 } , x _ { n } , \dots , x _ { n - k + 1 } \right] .
$$

Recurrence relations for ${ { g } _ { j } } ( n \mathrm { ~ ) }$ ， $\boldsymbol { \Phi } _ { j } ( \boldsymbol { n } )$ and $\boldsymbol { \Phi } _ { j } ^ { * } ( n )$

"The cost of computing integration coefficients is the biggest disadvantage to permitting arbitrary variations in the step size."

(F.T. Krogh, 1973)

The values $\Phi _ { j } ^ { * } ( n ) ( j = 0 , . . . , k - 1 )$ and $\Phi _ { k } \left( n + 1 \right)$ can be com-puted efficiently with the recurrence relations

$$
\begin{array} { l } { { \Phi _ { 0 } ( n ) = \Phi _ { 0 } ^ { * } ( n ) = f _ { n } } } \\ { { \Phi _ { j + 1 } ( n ) = \Phi _ { j } ( n ) - \Phi _ { j } ^ { * } ( n - 1 ) } } \\ { { \Phi _ { j } ^ { * } ( n ) = \beta _ { j } ( n ) \Phi _ { j } ( n ) } } \end{array}
$$

which are an immediate consequence of Definitions (5.3) and (5.8). The coefficient

$$
\beta _ { j } ( n ) = \prod _ { i = 0 } ^ { j - 1 } { \frac { x _ { n + 1 } - x _ { n - i } } { x _ { n } - x _ { n - i - 1 } } }
$$

can be calculated by

$$
\begin{array} { l } { { \beta _ { 0 } ( n ) = 1 } } \\ { { \beta _ { j } ( n ) = \beta _ { j - 1 } ( n ) \ \frac { x _ { n + 1 } - x _ { n - j + 1 } } { x _ { n } - x _ { n - j } } \ . } } \end{array}
$$

The calculation of the coefficients ${ { \mathbf { } } _ { g } } _ { j } ( n \mathbf { \Gamma } )$ is more tricky (F.T.Krogh (1974)). We introduce the $q$ -fold integral

$$
c _ { j q } ( x ) = { \frac { ( q - 1 ) ! } { h _ { n } ^ { q } } } { \overset { x } { \int } } \ \int ^ { \xi _ { q - 1 } } \cdots \int ^ { \xi _ { 1 } } \ \prod _ { i = 0 } ^ { j - 1 } { \frac { \xi _ { 0 } - x _ { n - i } } { x _ { n + 1 } - x _ { n - i } } } \ d \xi _ { 0 } \cdot \cdot \cdot d \xi _ { q - 1 }
$$

and observe that

$$
g _ { j } ( n ) = c _ { j 1 } ( x _ { n + 1 } ) .
$$

Lemma 5.1. We have

$$
\begin{array} { l } { { c _ { 0 q } ( x _ { n + 1 } ) = \frac { 1 } { q } \ , \quad \ c _ { 1 q } ( x _ { n + 1 } ) = \frac { 1 } { q \cdot ( q + 1 ) } \ } } \\ { { \ c _ { j q } ( x _ { n + 1 } ) = c _ { j - 1 , q } ( x _ { n + 1 } ) - c _ { j - 1 , q + 1 } ( x _ { n + 1 } ) \frac { h _ { n } } { x _ { n + 1 } - x _ { n - j + 1 } } \ . } } \end{array}
$$

Proof: The first two relations follow im mediately from (5.10). In order to prove the recurrence relation we denote by $d ( x )$ the difference

$$
= c _ { j q } ( x ) - c _ { j - 1 , q } ( x ) \frac { x - x _ { n - j + 1 } } { x _ { n + 1 } - x _ { n - j + 1 } } + c _ { j - 1 , q + 1 } ( x ) \ \frac { h _ { n } } { x _ { n + 1 } - x _ { n - j + 1 } } \ .
$$

Clearly, $d ^ { ( i ) } ( x _ { n } ) = 0$ for $i = 0$ ， $1 , \ldots , q - 1$ . Moreover, the $q$ -th derivative of $d ( x )$ vanishes, since by the Leibniz rule

$$
\begin{array} { r l } & { \quad \frac { d ^ { q } } { d x ^ { q } } \biggl [ c _ { j - 1 , q } ( x ) \cdot \frac { x - x _ { n - j + 1 } } { x _ { n + 1 } - x _ { n - j + 1 } } \biggr ] } \\ & { = c _ { j - 1 , q } ^ { ( q ) } ( x ) \frac { x - x _ { n - j + 1 } } { x _ { n + 1 } - x _ { n - j + 1 } } + q c _ { j - 1 , q } ^ { ( q - 1 ) } ( x ) \frac { 1 } { x _ { n + 1 } - x _ { n - j + 1 } } } \\ & { = c _ { j , q } ^ { ( q ) } ( x ) + c _ { j - 1 , q + 1 } ^ { ( q ) } ( x ) \frac { h _ { n } } { x _ { n + 1 } - x _ { n - j + 1 } } . } \end{array}
$$

Therefore we have $d \left( x \right) \equiv 0$ and the statement follows by putting $x = x _ { n + 1 } . \mathrm { O E D }$

Using the above recurrence relation one can successively compute $c _ { 2 q } ( x _ { n + 1 } )$ for $q = 1 , \ldots , k - 1$ 6 $c _ { 3 q } ( x _ { n + 1 } )$ for $q = 1 , \ldots , k - 2$ ;..; $c _ { k q } \left( x _ { n + 1 } \right)$ for $q = 1$ . This procedure yields in an efficient way the coefficien ts $g _ { j } ( n ) { = } c _ { j 1 } ( x _ { n + 1 } )$ of the Adams methods.

# Variable step size BDF-formulas

The BDF-formulas (1.22) can also be extended in a natural way to variable step size. Denote by $q \left( t \right)$ the polynomial of degree k that interpolates $( x _ { i } , y _ { i } )$ for $\scriptstyle i = n + 1 , n \ , \ , \ , \ n - k + 1$ . It can be expressed, using divided differences, by

$$
q \left( t \right) = \sum _ { j = 0 } ^ { k } \prod _ { i = 0 } ^ { j - 1 } \left( t - x _ { n + 1 - i } \right) y \left[ x _ { n + 1 } , x _ { n } , \ldots , x _ { n - j + 1 } \right] .
$$

The requirement

$$
q ^ { \prime } ( x _ { n + 1 } ) = f \left( x _ { n + 1 } , y _ { n + 1 } \right)
$$

immediately leads to the variable step size BDF-formulas

$$
\sum _ { j = 1 } ^ { k } h _ { n } \prod _ { i = 1 } ^ { j - 1 } ( x _ { n + 1 } - x _ { n + 1 - i } ) \ y [ x _ { n + 1 } , \ldots , x _ { n - j + 1 } ] \ = h _ { n } f \left( x _ { n + 1 } , y _ { n + 1 } \right) 
$$

The computation of the coefficients is much easier here than for the Adams methods.

# General variable step size multistep methods and their order of consis tency

For theoretical investigations it is convenient to write the methods in a form where the $y _ { j }$ and $f _ { j }$ values appear linearly. For example, the implicit Adams method (5.7) becomes ( $k = 2$ ）

$$
y _ { n + 1 } = y _ { n } \ + \ { \frac { \stackrel { \stackrel { \cdot } { h } } _ { n } } { 6 ( 1 + \omega _ { n } ) } } \left( ( 3 \ + \ 2 \omega _ { n } ) f _ { n + 1 } \ + \ ( 3 \ + \omega _ { n } ) ( 1 \ + \omega _ { n } ) f _ { n } \ - \ \omega _ { n } ^ { 2 } f _ { n - 1 } \right)
$$

where we have introduced the notation $\omega _ { n } { = } h _ { n } / h _ { n - 1 }$ for the step size ratio. $\mathrm { o r }$ , the 2-step BDF-formula (5.12) can be written as

$$
y _ { n + 1 } - \frac { \left( 1 + \omega _ { n } \right) ^ { 2 } } { 1 + 2 \omega _ { n } } y _ { n } + \frac { \omega _ { n } ^ { 2 } } { 1 + 2 \omega _ { n } } y _ { n - 1 } = h _ { n } \frac { 1 + \omega _ { n } } { 1 + 2 \omega _ { n } } f _ { n + 1 } \ .
$$

In order to give a unified theory for all these variable step size multistep methods we consider formulas of the form

$$
y _ { n + k } \ + \ \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j n } y _ { n + j } \ = h _ { n + k - 1 } \sum _ { j = 0 } ^ { k } \beta _ { j n } f _ { n + j } \ .
$$

The coeficients ${ \alpha } _ { j n }$ and $\beta _ { j n }$ actually depend on the ratios $\omega _ { i } = h _ { i } / h _ { i - 1 }$ for $i = n + 1 , , \ldots , n ^ { ' + k - 1 } ,$ In analogy to the constant step size case we give

Definition 5.2. Method (5.15) is consistent of order $\boldsymbol { p }$ ,if

$$
q \left( x _ { n + k } \right) ~ + ~ \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j n } q \left( x _ { n + j } \right) ~ = h _ { n + k - 1 } \sum _ { j = 0 } ^ { k } \beta _ { j n } q ^ { \prime } ( x _ { n + j } )
$$

holds for all polynomials $q \left( x \right)$ of degree $\leq p$ and for all grids $( x _ { j } )$

By definition, the explicit Adams method (5.5) is of order $k$ ,the implicit Adams method (5.7) is of order $k + 1$ , and the BDF-formula (5.12) is of order k .

The notion of consistency certainly has to be related to the local error. Indeed, if the method is of order $p$ , if the ratios $h _ { j } / h _ { n }$ are bounded for $j = n + 1 , . . . , n + k - 1$ and if the coefficients satisfy

$$
\alpha _ { j n } , \beta _ { j n } \mathrm { a r e b o u n d e d } ,
$$

then a Taylor expansion argument implies

$$
y ( x _ { n + k } ) ~ + ~ \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j n } y ( x _ { n + j } ) ~ - ~ h _ { n + k - 1 } \sum _ { j = 0 } ^ { k } \beta _ { j n } y ^ { \prime } ( x _ { n + j } ) ~ = ~ \mathsf { O } ( h _ { n } ^ { p + 1 } )
$$

for sufficiently smooth $y \left( x \right)$ . Interpreting $y \left( x \right)$ as the solution of the

differential equation, a trivial extension of Lemma 2.2 to variable step sizes shows that the local error at $x _ { n + k }$ (cf. Definition 2.1） is also $\mathbf { 0 } ( h _ { n } ^ { p + 1 } )$

This motivates the investigation of Condition (5.16). The methods (5.13) and (5.14) arc seen to satisfy (5.16) whenever the step size ratio $h _ { n } / h _ { n - 1 }$ is bounded from above.In general we have

$\propto _ { j n }$ $\beta _ { j n }$ ams mehodsaseas for some Ω

$$
h _ { n } / h _ { n - 1 } \leq \Omega .
$$

Proof: We prove the statement for the explicit Adams methods only. The proof for the other methods is similar and thus omitted. We see from Formula (5.5) that the coefficients $\propto _ { j n }$ do not depend on n and hence are bounded. The $\beta _ { { \mathbf { \Gamma } } _ { j n } }$ are composcd of products of ${ { g } _ { j } } ( n )$ with the coefficients of $\Phi _ { j } ^ { * } ( n )$ ，When written as a linear combination of $f _ { n } ~ , ~ \dots , f _ { n - j }$ FromFormula (5.6) wesee that $\vert g _ { j } ( n ) \vert \leq 1$ It follows from $( x _ { n + 1 } - x _ { n - j + 1 } ) \le \operatorname* { m a x } ( 1 , \Omega ^ { j } ) ( x _ { \eta } - x _ { n - j } )$ and an induction argument shows that the coeffcients of $\Phi _ { j } ^ { * } ( n )$ are also bounded. Hence the $\beta _ { j n }$ are bounded, which proves the lemma. QED.

The condition $h _ { n } / h _ { n - 1 } { \leq } \Omega$ is a reasonable assumption which can easily be satisfied by a code.

# Stability

"So geht das einfach ..." (R.D. Grigorieff, Halle 1983)

The study of stability for variable step size methods was begun in the articles of Gear-Tu (1974) and Gear-Watanabe (1974). Further investigations are due to Grigorieff (1983） and Crouzeix-Lisbona (1984).

We have seen in Section II1.3 that for equidistant grids stability is equivalent to the boundedness of the numerical solution, when applied to the scalar differential equation $y ^ { \prime } { = } 0$ . Let us do the same here for the general case. Method (5.15), applied to $y \prime { = } 0$ ， gives the difference equation with variable coefficients

$$
y _ { n + k } + \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j n } y _ { n + j } = 0 .
$$

Introducing the vector $Y _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ this difference equation is equivalent to

$$
Y _ { n + 1 } = A _ { n } Y _ { n }
$$

with

$$
A _ { n } \stackrel { \sim } { = } \left( \begin{array} { r r r r r } { - \alpha _ { k - 1 , n } } & { \cdots } & { \cdots } & { - \alpha _ { 1 , n } } & { - \alpha _ { 0 , n } } \\ { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { \cdots } & { 0 } & { \cdots } \\ { 1 } & { 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 1 } & { 1 } & { 0 } \end{array} \right) \ ,
$$

the com panion matrix.

Definition 5.4. Method (5.15) is called stable, if

$$
\| A _ { n + l } A _ { n + l - 1 } \cdot \cdot \cdot A _ { n + 1 } A _ { n } \| \leq M
$$

for all $n$ and $t \geq 0$

Observe that in general $A _ { n }$ depends on the step size ratios $\omega _ { n + 1 } , \ldots , \omega _ { n + k - 1 } .$ Therefore, Condition (5.19) will usually lead to a restriction on these values.

For theAdams methods(5.5)and (5.7)thecoeficents ${ \mathfrak { a } } _ { j n }$ do not depend on n and hence are stable for any step size sequence.

In the following three theorems we present stability results for general variable step size methods. The first one, taken from Crouzeix-Lisbona (1984), is a sort of perturbation result: the variable step size method is considered as a perturbation of a strongly stable fixed step size method.

Theorem 5.5. Let the method (5.15) satisfy the following properties: a) it is of order $p \geq 0$ ,i.e. $1 + \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j n } = 0 \ .$ b) the coefficients $\alpha _ { j n } = \alpha _ { j } ( \omega _ { n + 1 } , \cdot \cdot . , \omega _ { n + k - 1 } )$ are continuous in a neighbourhood of $( 1 , \ldots , 1 )$ ； c) the underlying constant step size formula is strongly stable,i.e. all roots of

$$
\zeta ^ { k } + \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j } ( 1 , \dots , 1 ) \zeta ^ { j } = 0
$$

lie in the open unit disc $| \zeta | < 1$ ， with the exception of $\zeta _ { 1 } = 1$

Then there exist real numbers w, $\Omega$ （ $\omega < 1 < \Omega$ ） such that the method is stable. if

$$
\omega \leq h _ { n } / h _ { n - 1 } \leq \Omega f o r \ a l l n .
$$

Proof: Let A be the companion matrix of the constant step size formula. As in the proof of Lemma 4.4 we transform A to Jordan canonical form and obtain

$$
\begin{array} { r l r } { \boldsymbol { T } ^ { - 1 } { } _ { A T } } & { = } & { \left( \begin{array} { c c c } & { \mathrm { ~ 1 ~ } } & { 0 } \\ & { \mathrm { ~ 1 ~ } } & { \mathrm { ~ : ~ } } \\ & { \hat { A } } & { \mathrm { ~ 1 ~ } } & { \mathrm { ~ 0 ~ } } \\ & & { \mathrm { ~ 1 ~ } } & { 0 } \\ & & { \mathrm { ~ 1 ~ } } & { 1 } \end{array} \right) } \end{array}
$$

where, by assumption c), $\| \hat { A } \| _ { 1 } < 1$ . Observe that the last column of $T$ ，the eigenvector of Acorresponding to1，is given by $t _ { k }$ $\mathbf { \Psi } = ( 1 , \dots , 1 ) ^ { T }$ .Assumption a) implies that this vector $t _ { k }$ is also an eigenvector for each $A _ { n } \cdot$ Therefore we have

$$
\begin{array} { r l r } { T ^ { - 1 } A _ { n } T } & { = } & { \left( \begin{array} { l l l } & { } & { 1 \ 0 } \\ { } & { } & { 1 \ \vdots } \\ { } & { \hat { A _ { n } } } & { \ 1 \ 0 } \\ { } & { } & { 1 \ 0 } \\ { } & { } & { 1 \ 1 } \end{array} \right) } \end{array}
$$

and, by continuity， $\Vert \hat { A } _ { n } \Vert _ { 1 } \leq 1$ if $\mathfrak { o } _ { n + 1 } , \dots , \mathfrak { w } _ { n + k - 1 }$ are sufficiently close to 1. Stability now follows from the fact that

$$
\parallel T ^ { - 1 } A _ { n } T \parallel _ { 1 } = \operatorname* { m a x } ( \parallel \hat { A } _ { n } \parallel _ { 1 } , 1 ) = 1
$$

which implies

$$
\begin{array} { r l r } { \parallel { \cal A } _ { n + l } \cdot \cdot \cdot { \cal A } _ { n + 1 } { \cal A } _ { n } \parallel } & { \leq } & { \parallel T \parallel \cdot \parallel T ^ { - 1 } \parallel \cdot \parallel \cdot \parallel } \end{array} .
$$

QED.

The next result (Grigorieff (1983)) is based on a reduction of the dimension of the matrices $A _ { n }$ by one. Thc idea is to use the transformation

$$
T = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { \ldots } } & { { 1 } } \\ { { } } & { { 1 } } & { { 1 } } & { { \ldots } } & { { 1 } } \\ { { } } & { { } } & { { 1 } } & { { \ldots } } & { { 1 } } \\ { { } } & { { 0 } } & { { \ddots } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { 1 } } \end{array} \right) , \quad T ^ { - 1 } = \left( \begin{array} { c c c c } { { 1 } } & { { - 1 } } & { { 0 } } & { { } } \\ { { } } & { { 1 } } & { { - 1 } } & { { } } \\ { { } } & { { 1 } } & { { \ldots } } & { { } } \\ { { } } & { { 0 } } & { { \ldots } } & { { - 1 } } \\ { { } } & { { } } & { { } } & { { 1 } } \end{array} \right) .
$$

Observe that the last column of $T$ is just $t _ { k }$ of the above proof. A sim ple calculation shows that

$$
\begin{array} { r l r } { T ^ { - 1 } A _ { n } T } & { = } & { \left( \begin{array} { c } { A _ { n } ^ { * } \ _ { 1 } ^ { 1 } 0 } \\ { - - - \frac { 1 } { 1 } -- } \\ { e _ { k - 1 } ^ { T } \ _ { 1 } ^ { 1 } 1 } \end{array} \right) } \end{array}
$$

where $e _ { k - 1 } ^ { T } = ( 0 , \dots , 0 , 1 )$ and

$$
\begin{array} { r } { A _ { n } ^ { * } \ = \ \left( \begin{array} { c c c c c } { - \alpha _ { k - 2 , n } ^ { * } \ - \alpha _ { k - 3 , n } ^ { * } \ - \ \hdots \ - \alpha _ { 1 n } ^ { * } \ - \alpha _ { 0 n } ^ { * } } \\ { 1 \ } & { 0 \ } & { \hdots } & { \hdots } & { 0 } \\ { 1 \ } & { 1 \ } & { \hdots } & { \hdots } & { 0 } \\ { 1 \ } & { \hdots } & { \hdots } & { \hdots } & { 0 } \\ { \hdots } & { \ddots } & { \vdots \ } & { \vdots } \\ { 1 \ } & { 1 \ } & { 0 \ } \end{array} \right) } \end{array}
$$

with

$$
\alpha _ { k - 2 , n } ^ { * } = 1 + \alpha _ { k - 1 , n } , \qquad \alpha _ { 0 n } ^ { * } = - \alpha _ { 0 n }
$$

$$
{ \mathfrak { a } } _ { k - j - 1 , n } ^ { * } - { \mathfrak { a } } _ { k - j , n } ^ { * } = \alpha _ { k - j , n } \qquad { \mathrm { f o r } } j = 2 , \ldots , k - 1 \ .
$$

We remarkthat thecoeffcients ${ \alpha } _ { j , n } ^ { * }$ are just thecoeficients f the

$$
\begin{array} { r l } & { ( \zeta ^ { k } + \alpha _ { k - 1 , n } \zeta ^ { k - 1 } + \cdot \cdot \cdot + \alpha _ { 1 , n } \zeta + \alpha _ { 0 , n } ) } \\ & { \qquad = ( \zeta - 1 ) ( \zeta ^ { k - 1 } + \alpha _ { k - 2 , n } ^ { * } \zeta ^ { k - 2 } + \cdot \cdot \cdot + \alpha _ { 1 , n } ^ { * } \zeta + \alpha _ { 0 , n } ^ { * } ) \ . } \end{array}
$$

Theorem 5.6. Let the method (5.15) be of order $p \geq 0$ . Then the method is stable if and only if for all n and $i \geq 0$

$$
\begin{array} { r l } { \mathrm { a } ) \quad } & { \| A _ { n + l } ^ { * } \cdot \cdot \cdot A _ { n + 1 } ^ { * } A _ { n } ^ { * } \| \leq M _ { 1 } } \\ { \mathrm { b } ) \quad } & { \| e _ { k - 1 } ^ { T } \displaystyle \sum _ { j = n } ^ { n + l } \prod _ { i = n } ^ { j - 1 } A _ { i } ^ { * } \| \leq M _ { 2 } . } \end{array}
$$

Proof: A simple induction argument shows that

with

$$
T ^ { - 1 } A _ { n + l } \cdot \cdot \cdot A _ { n } T ~ = ~ \left( { \cfrac { A _ { n + l } ^ { * } \cdot \cdot \cdot A _ { n } ^ { * } \stackrel { \dagger } { \mid } ~ 0 } { b _ { n , l } ^ { T } } } \right)
$$

$$
b _ { n , l } ^ { T } = e _ { k - 1 } ^ { T } \sum _ { j = n } ^ { n + l } \ \prod _ { i = n } ^ { j - 1 } A _ { i } ^ { * } .
$$

QED.

Since in this theorem the dimension of the matrices under consideration is reduced by one, it is especially useful for the stability investigation of two-step methods.

Example: Consider the two-step BDF-method (5.14). Here

$$
\alpha _ { 0 n } = \frac { \omega _ { n + 1 } ^ { 2 } } { 1 + 2 \omega _ { n + 1 } } \ , \qquad \alpha _ { 1 n } = - 1 - \alpha _ { 0 n } \ .
$$

The matrix (5.21) becomes in this case

$$
{ \cal A } _ { n } ^ { \ast } = \bigl ( - \alpha _ { 0 n } ^ { \ast } \bigr ) , \qquad - \alpha _ { 0 n } ^ { \ast } = \frac { \omega _ { n + 1 } ^ { 2 } } { 1 + 2 \omega _ { n + 1 } } \ .
$$

$| \alpha _ { 0 n } ^ { * } \ | \leq q < 1$ the conditions of Theorem 5.6 are satisfied and imply stability. This is the case, if

$$
0 < h _ { n + 1 } / h _ { n } \leq \Omega < 1 + \sqrt { 2 } \ .
$$

An interesting consequence of the theorem above is the instability of the two-step BDF-formulas if the step sizes increase at least like $h _ { n + 1 } / h _ { n } \geq \ \bar { 1 + \sqrt { 2 } }$

The investigation of stability for $k$ -step ( $k \geq 3$ ）methods becomes much more dificult,since several step sizeratios ${ \mathfrak { o } } _ { n + 1 } , \ { \mathfrak { o } } _ { n + 2 } , \ \cdot \ \cdot \ .$ are involved.

Grigorieff (1983) calculated the following bounds of the form (5.20) for the higher-order BDF-methods which ensure stability:

Table 5.1. Bounds (5.20) for the k -step BDF formulas   

<table><tr><td>k</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>W</td><td>0</td><td>0.836</td><td>0.979</td><td>0.997</td></tr><tr><td>Ω</td><td>2.414</td><td>1.127</td><td>1.019</td><td>1.003</td></tr></table>

These bounds are surely unrealistic, since all pathological step size variations are admitted.

A less pessimistic result is obtained if the step sizes are supposed to vary more smoothly (Gear-Tu (1974)): the local error is known to be of the form $d \big ( x _ { n } \big ) h _ { n } ^ { p + 1 } + \mathbf { O } \big ( h _ { n } ^ { p + 2 } \big )$ ,where $d ( x )$ is the principal error function. This local error is, by the step size control, kept equal to TOL. Hence, if $d ( x )$ is bounded away from zero we have

$$
h _ { n } \ = \ \vert T O L / d \left( x _ { n } \right) \vert ^ { 1 / \left( p + 1 \right) } + \mathbf { O } \left( h _ { n } \right)
$$

which implies (if $h _ { n + 1 } / n _ { n } \leq \Omega$ ）

$$
h _ { n + 1 } / h _ { n } = \left| d ( x _ { n } ) / d ( x _ { n + 1 } ) \right| ^ { 1 / ( p + 1 ) } + \mathbf { O } ( h _ { n } ) ~ .
$$

If $d ( x )$ is differentiable, we obtain

$$
\left| h _ { n + 1 } / h _ { n } - 1 \right| \leq C h _ { n } \ .
$$

Several stability results of Gear-Tu are based on this hypothesis ("Consequently, we can expect either method to be stable if the fixed step method is stable..."). Adding up (5.22) we obtain

$$
\begin{array} { r l } { \cdot \quad } & { { } \underset { j = n } { \overset { n + l } { \sum } } | h _ { j + 1 } / h _ { j } - 1 | \leq C \left( \hat { x } - x _ { 0 } \right) , } \end{array}
$$

a condition which contains only step size ratios. This motivates the following theorem:

ously difentiblefuctionsof Theorem 5.7. Let the coefcents $\mathfrak { w } _ { n + 1 } , \ldots , \mathfrak { w } _ { n + k - 1 }$ $\propto _ { j n }$ of method in a neighbourhood of $( 5 , I 5 )$ be continu-$\{ ( \omega _ { n + 1 } , \ldots , \omega _ { n + k - 1 } ) ; \omega \leq \omega _ { j } \leq \Omega \}$ and assume that the method is stable for constant step sizes (i.e. for $\omega _ { j } = 1$ ).Then the condition

$$
\sum _ { j = n } ^ { n + l } | h _ { j + 1 } / h _ { j } - 1 | \leq C \qquad f o r \ a l l \ n \ a n d \ l \geq 0 \ ,
$$

together with $\omega \leq h _ { j + 1 } / h _ { j } \leq \Omega$ , impty the stability condition (5.19).

Proof: As in the proof of Theorem 5.5 we denote by $A$ the com-panion matrix of the constant step size formula and by $T$ a suitable transformation such that $\parallel T ^ { - 1 } A T \parallel = 1$ . The mean value theorem, applied to $\alpha _ { j } ( \omega _ { n + 1 } , . . . , \omega _ { n + k - 1 } ) \ - \alpha _ { j } ( 1 , . . . , 1 )$ , implies that

$$
\Vert \textbf {  { T } } ^ { - 1 } A _ { n } T \ - \ T ^ { - 1 } A T \ \Vert \ \leq \ K \sum _ { j = n + 1 } ^ { n + k - 1 } | \omega _ { j } - 1 \ | \ .
$$

Hence

$$
\big \vert \bigtriangledown { T } ^ { - 1 } A _ { \pi } T \ \big \vert \ \big \vert \ \leq \ 1 + K \sum _ { j = \pi + 1 } ^ { n + k - 1 } \vert \omega _ { j } - 1 \vert \ \leq \ \exp ( K \sum _ { j = \pi + 1 } ^ { n + k - 1 } \vert \omega _ { j } - 1 \vert ) \ .
$$

From this inequality we deduce that

$$
\begin{array} { r } { \big \vert \big \vert \boldsymbol { A } _ { n + l } \cdot \cdot \cdot \boldsymbol { A } _ { n + 1 } \boldsymbol { A } _ { n } \big \vert \big \vert \ \leq \ \big \vert \big \vert \boldsymbol { T } \mathrm { ~ } \big \vert \big \vert \cdot \big \vert \big \vert \boldsymbol { T } ^ { - 1 } \big \vert \big \vert \cdot \exp \big ( \boldsymbol { K } \cdot ( \boldsymbol { k } - 1 ) \boldsymbol { C } \big ) \ . } \end{array}
$$

QED.

# Convergence

Convergence for variable step size Adams methods was first studied by Piotrowski (1969). In order to prove convergence for the general case we introduce the vector $Y _ { n } = ( y _ { n + k - 1 } , . . . , y _ { n + 1 } , y _ { n } ) ^ { T } .$ In analogy to (4.8) the method (5.15) then becomes equivalent to

$$
Y _ { n + 1 } = ( A _ { n } \otimes I ) Y _ { n } + h _ { n + k - 1 } \Phi _ { n } ( x _ { n } , Y _ { n } , h _ { n } )
$$

where $A _ { n }$ is given by (5.18) and

$$
\Phi _ { n } ( x _ { n } , Y _ { n } , h _ { n } ) = ( e _ { 1 } \otimes I ) \Psi _ { n } ( x _ { n } , Y _ { n } , h _ { n } ) \ .
$$

The value $\Psi { = } \Psi _ { n } \left( x _ { n } , Y _ { n } , h _ { n } \right)$ is im plicitly defined by

$$
\Psi = \sum _ { j = 0 } ^ { k - 1 } \mathsf { \mathsf { B } } _ { j n } f ( x _ { n + j } , y _ { n + j } ) \ + \mathsf { \mathsf { B } } _ { k n } f ( x _ { n + k } , h \Psi - \sum _ { j = 0 } ^ { k - 1 } \mathsf { \alpha } _ { j n } y _ { n + j } ) \mathrm { ~ . ~ }
$$

Let us further denote by

$$
{ \cal Y } \left( x _ { n } \right) = \left( y \left( x _ { n + k - 1 } \right) , \ldots , y \left( x _ { n + 1 } \right) , y \left( x _ { n } \right) \right) ^ { T }
$$

the exact values to be approximated by $Y _ { n } \ .$ The convergence theorem can now be formulated as follows:

Theorem 5.8. Assume that

a) the method (5.15) is stable, of order $p$ ， and has bounded coefficients $\alpha _ { j n }$ and $\beta _ { j n }$ ;

$^ b$ ) the staring values satisfy $\begin{array} { r l } { \Vert \textbf { \textit { Y } } ( \boldsymbol { x } _ { 0 } ) - \boldsymbol { Y } _ { 0 } \Vert } & { = \mathbf { 0 } ( h _ { 0 } ^ { p } ) ; } \end{array}$ c) the step size ratios are bounded $( h _ { n } / h _ { n - 1 } { \le \Omega }$ ）

Then the method is convergent of order $p$ ,i.e. for each differential equation $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 }$ with $f$ sufficiently differentiable the global error satisfies

$$
\| { \textbf { \it y } } ( x _ { n } ) - y _ { n } \| \leq C h ^ { p } { f o r } x _ { n } \leq \hat { x } ,
$$

where h = max h;.

Proof: Since the method is of order $p$ and the coefficients and step size ratios are bounded, Formula (5.17) shows that the local error

$$
\delta _ { n + 1 } = Y ( x _ { n + 1 } ) - ( A _ { n } \otimes I ) Y ( x _ { n } ) - h _ { n + k - 1 } \Phi _ { n } ( x _ { n } , Y ( x _ { n } ) , h _ { n } )
$$

satisfies

$$
\delta _ { n + 1 } = { \bf O } ( h _ { n } ^ { p + 1 } ) .
$$

Subtracting (5.24) from (5.25) we obtain

$$
\begin{array} { r l } & { Y \left( x _ { n + 1 } \right) - Y _ { n + 1 } = { \left( A _ { n } \otimes I \right) } { \left( Y \left( x _ { n } \right) - Y _ { n } \right) } } \\ & { \quad + h _ { n + k - 1 } \{ \Phi _ { n } ( x _ { n } , Y \left( x _ { n } \right) , h _ { n } ) - \Phi _ { n } ( x _ { n } , Y _ { n } , h _ { n } ) \} + \mathfrak { b } _ { n + 1 } } \end{array}
$$

and by induction it follows that

$$
Y ( x _ { n + 1 } ) - Y _ { n + 1 } = ( ( A _ { n } \cdot \cdot \cdot A _ { 0 } ) { \otimes } I ) ( Y ( x _ { 0 } ) - Y _ { 0 } )
$$

$$
+ \sum _ { j = 0 } ^ { n } h _ { j + k - 1 } ( ( A _ { n } \cdot \cdot \cdot A _ { j + 1 } ) \otimes I ) \{ \Phi _ { j } ( x _ { j } , Y ( x _ { j } ) , h _ { j } ) - \Phi _ { j } ( x _ { j } , Y _ { j } , h _ { j } ) \} \otimes
$$

$$
+ \sum _ { j = 0 } ^ { n } ( ( A _ { n } \cdot \cdot \cdot A _ { j + 1 } ) \otimes I ) \ S _ { j + 1 } .
$$

As in the proof of Theorem $4 . 5 \mathrm { \ w e }$ deduce that the $\Phi _ { n }$ satisfy a uniform Lipschitz condition with respect to $Y _ { n } \ .$ This, together with stability and (5.26),implies that

$$
\{ \mid Y ( x _ { n + 1 } ) - Y _ { n + 1 } \mid \mid \ \leq \ \sum _ { j = 0 } ^ { n } h _ { j + k - 1 } L \mid \mid Y ( x _ { j } ) - Y _ { j } \mid \mid \ + C _ { 1 } h ^ { p } .
$$

In order to solve this inequality we introduce the sequence {∈n defined bv

$$
\begin{array} { c } { { \displaystyle \epsilon _ { 0 } = \left\| { \cal Y } \left( x _ { 0 } \right) - { \cal Y } _ { 0 } \right\| , } } \\ { { } } \\ { { \epsilon _ { n + 1 } = \displaystyle \sum _ { j = 0 } ^ { n } h _ { j + k - 1 } L \epsilon _ { j } + C _ { 1 } h ^ { p } . } } \end{array}
$$

A simplc induction argument shows that

$$
\begin{array} { r } { \vert \vert  { Y } ( \boldsymbol { x } _ { n } ) - Y _ { n } \vert \vert \le \epsilon _ { n } \ . } \end{array}
$$

From (5.27) we obtain for $n \geq 1$

$$
\epsilon _ { n + 1 } = \epsilon _ { n } + h _ { n + k - 1 } L \epsilon _ { n } \leq \exp ( h _ { n + k - 1 } L ) \epsilon _ { n }
$$

so that also

$$
\begin{array} { r } { \epsilon _ { n } \leq \exp ( ( \hat { x } - x _ { 0 } ) L ) \epsilon _ { 1 } } \\ { = \exp ( ( \hat { x } - x _ { 0 } ) L ) \cdot \{ h _ { k - 1 } L \parallel Y ( x _ { 0 } ) - Y _ { 0 } \parallel + C _ { 1 } h ^ { p } \} \ . } \end{array}
$$

This inequality together with (5.28) completes the proof of Theorem 5.8. QED.

# Exercises

1. Prove that for constant step sizes the expressions $g _ { j } ( n )$ and $\Phi _ { j } ^ { * } ( n )$ (Formulas (5.3) and (5.6) reduce to

$$
g _ { j } ( n ) = \gamma _ { j } , \qquad \Phi _ { j } ^ { * } ( n ) = \nabla ^ { j } f _ { n } ,
$$

where $\gamma _ { j }$ is given by (1.6).

2. (Grigorieff (1983)). For the $k$ -step BDF-methods consider grids with constant mesh ratio $\boldsymbol { \omega }$ ,i.e. $h _ { n } = \omega h _ { n - 1 }$ for all $n$ . In this case the elements of ${ A } _ { n } ^ { * }$ (see (5.21)） are independent of $n$ . Show numerically that all eigenvalues of $\boldsymbol { A } _ { n } ^ { * }$ are of absolute value less than one for $0 < \omega < R _ { k }$ where

<table><tr><td>k</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Rk</td><td>2.414</td><td>1.618</td><td>1.280</td><td>1.127</td><td>1.044</td></tr></table>

In an important paper Nordsieck (1962) considered a class of methods for ordinary differential equations which allow a convenient way of changing the step size (see Section III.7). He already remarked that his methods are equivalent to the implicit Adams methods, in a certain sense. Let us begin with his derivation of these methods and then investigate their relation to linear multistep methods.

Nordsieck (1962) remarked ".. that all methods of numerical integration are equivalent to finding an approximating polynomial for $y \left( x \right) \ldots ^ { \prime \prime }$ His idea was to represent such a polynomial by the O-th to $k$ -th derivatives, i.e. by a vector ("the Nordsieck vector")

$$
z _ { n } = ( y _ { n } , h y _ { n } ^ { \prime } , \frac { h ^ { 2 } } { 2 ! } y _ { n } ^ { \prime \prime } , . . . , \frac { h ^ { k } } { k ! } y _ { n } ^ { ( k ) } ) ^ { T } .
$$

The ${ \bf \Phi } _ { y _ { n } } ( j )$ are meant to be approximations to $y ^ { ( j ) } ( x _ { n } )$ ，where $y \left( x \right)$ is the exact solution of the differential equation

$$
y ^ { \prime } = f \left( x , y \right) .
$$

In order to define the integration procedure we have to give a rule for determining $z _ { n + 1 }$ when $z _ { n }$ and the differential equation (6.2) are given. Such a rule is by Taylor's expansion (e.g. for $k = 3$ ）

$$
{ \begin{array} { r l r } { y _ { n + 1 } = } & { y _ { n } + ~ h y _ { n } ^ { \prime } + } & { { \frac { h ^ { 2 } } { 2 ! } } y _ { n } ^ { \prime \prime } + } & { { \frac { h ^ { 3 } } { 3 ! } } y _ { n } ^ { \prime \prime \prime } + } & { { \frac { h ^ { 4 } } { 4 ! } } e } \\ & { } & \\ { h y _ { n + 1 } ^ { \prime } = } & { h y _ { n } ^ { \prime } + 2 { \frac { h ^ { 2 } } { 2 ! } } y _ { n } ^ { \prime \prime } + } & { 3 { \frac { h ^ { 3 } } { 3 ! } } y _ { n } ^ { \prime \prime \prime } + } & { 4 { \frac { h ^ { 4 } } { 4 ! } } e } \\ & { } & \\ { { \frac { h ^ { 2 } } { 2 ! } } y _ { n + 1 } ^ { \prime \prime } = } & { { \frac { h ^ { 2 } } { 2 ! } } y _ { n } ^ { \prime \prime } + } & { 3 { \frac { h ^ { 3 } } { 3 ! } } y _ { n } ^ { \prime \prime \prime } + } & { 6 { \frac { h ^ { 4 } } { 4 ! } } e } \\ & { } & \\ { { \frac { h ^ { 3 } } { 3 ! } } y _ { n + 1 } ^ { \prime \prime } = } & { { \frac { h ^ { 3 } } { 3 ! } } y _ { n } ^ { \prime \prime \prime } + } & { 4 { \frac { h ^ { 4 } } { 4 ! } } e } \end{array} }
$$

where the value $e$ is determined in such a way that

$$
y _ { n + 1 } ^ { \prime } = f \left( x _ { n + 1 } , y _ { n + 1 } \right) .
$$

Inserting (6.4) into the second relation of (6.3) yields

$$
4 \frac { { h ^ { 4 } } } { 4 ! } e ~ = h \left( { f \left( { x _ { n + 1 } } , { y _ { n + 1 } } \right) - f _ { n } ^ { p } } \right)
$$

with

$$
h f _ { n } ^ { p } = h y _ { n } ^ { \prime } + 2 \frac { h ^ { 2 } } { 2 ! } y _ { n } ^ { \prime \prime } + 3 \frac { h ^ { 3 } } { 3 ! } y _ { n } ^ { \prime \prime \prime } .
$$

With this relation for $e$ the above method becomes

$$
\begin{array} { r l r } { y _ { n + 1 } = } & { y _ { n } \overset { \prime } { + } } & { h y _ { n } ^ { \prime } + } & { \frac { h ^ { 2 } } { 2 ! } y _ { n } ^ { \prime \prime } + } & { \frac { h ^ { 3 } } { 3 ! } y _ { n } ^ { \prime \prime \prime } + \frac { 1 } { 4 } h \left( f \left( x _ { n + 1 } , y _ { n + 1 } \right) - f _ { n } ^ { p } \right) } \\ & { } & \\ { h y _ { n + 1 } ^ { \prime } = } & { h y _ { n } ^ { \prime } + } & { 2 \frac { h ^ { 2 } } { 2 ! } y _ { n } ^ { \prime \prime } + } & { 3 \frac { h ^ { 3 } } { 3 ! } y _ { n } ^ { \prime \prime \prime } + \hphantom { \frac { h } { 2 } } h \left( f \left( x _ { n + 1 } , y _ { n + 1 } \right) - f _ { n } ^ { p } \right) } \\ & { } & \\ { \frac { h ^ { 2 } } { 2 ! } y _ { n + 1 } ^ { \prime \prime } = } & { \frac { h ^ { 2 } } { 2 ! } y _ { n } ^ { \prime \prime } + } & { 3 \frac { h ^ { 3 } } { 3 ! } y _ { n } ^ { \prime \prime \prime } + \frac { 3 } { 2 } h \left( f \left( x _ { n + 1 } , y _ { n + 1 } \right) - f _ { n } ^ { p } \right) } \\ & { } & \\ { \frac { h ^ { 3 } } { 3 ! } y _ { n + 1 } ^ { \prime \prime \prime } = } & { \frac { h ^ { 3 } } { 3 ! } y _ { n } ^ { \prime \prime \prime } + } & { h \left( f \left( x _ { n + 1 } , y _ { n + 1 } \right) - f _ { n } ^ { p } \right) } \end{array}
$$

The first equation constitutes an implicit formula for $y _ { n + 1 }$ ，the approximations remaining ones are explicit. Observe that for suficiently accurate $y _ { n } ^ { \mathbf { \alpha } ( j ) }$ t $\bar { y } ^ { ( j ) } ( x _ { n } )$ thrvauet(Formula(6.5)a approximation to ${ \overset { \cdot } { y } } ^ { ( 4 ) } ( x _ { n } ) .$ This seems to be a desirable property from the point of view of accuracy. Unfortunately, Method (6.6) is unstable. To see this, we put $f \left( x \ , y \right) { = } 0$ in (6.6). In this case the method becomes the linear transform ation

$$
z _ { n + 1 } = M z _ { n }
$$

where

$$
\begin{array} { r } { M = \left( \begin{array} { c c c c } { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { 3 } \\ { 0 } & { 0 } & { 1 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right) - \ \left( \begin{array} { c } { 1 / 4 } \\ { 1 } \\ { 3 / 2 } \\ { 1 } \end{array} \right) \ ( 0 \ 1 \ 2 \ 3 ) \ . } \end{array}
$$

The eigenvalues of $M$ are seen to be 1, 0, $- ( 2 + { \sqrt { 3 } } )$ and $- 1 / \left( 2 + { \sqrt { 3 } } \right)$ ， implying that (6.6) is unstable and therefore of no use. The phenomenon that highly accurate methods are often unstable has already been encountered in Section III.3.

To overcome this difficulty Nordsieck proposed to replace the constants $1 / 4 , 1 , 3 / 2 , 1$ which appear in front of the brackets in (6.6) by arbitrary values $( l _ { 0 } , l _ { 1 } , l _ { 2 } , l _ { 3 } )$ , and to use this extra freedom to achieve stability. In compact form this modification can be written as

$$
z _ { n + 1 } = ( P \otimes I ) z _ { n } + ( l \otimes I ) \left( h f \left( x _ { n + 1 } , y _ { n + 1 } \right) - ( e _ { 1 } ^ { T } P \otimes I ) z _ { n } \right) .
$$

Here $z _ { n }$ is given by (6.1), $P$ is the Pascal triangle matrix defined by

$$
P _ { i j } = \left\{ \begin{array} { l l } { { \binom { j } { i } } } & { { \quad \mathrm { f o r } 0 \leq i \leq j \leq k } } \\ { { 0 } } & { { \quad \mathrm { e l s e } , } } \end{array} \right.
$$

$\boldsymbol { l } = ( l _ { 0 } , l _ { 1 } , \dots , l _ { k } ) ^ { T }$ and $e _ { 1 } \substack { = } ( 0 , 1 , 0 , \ldots , 0 ) ^ { T }$ Observe that the indices of vectors and matrices start from zero.

For notational simplicity in the following theorems, we consider from now on scalar differential equations only, so that Method (6.8) becomes

$$
z _ { n + 1 } = P z _ { n } + l [ h f _ { n + 1 } - e _ { 1 } ^ { T } P z _ { n } ] \ .
$$

All results, of course, remain valid for systems of equations. Condition (6.4), which relates the method to the differential equation, fixes the value of $\boldsymbol { l } _ { 1 }$ as

$$
\begin{array} { r } { l _ { 1 } = 1 . } \end{array}
$$

The above stability analysis applied to the general method (6.8) leads to the difference equation (6.7) with

$$
M \ = P \ - \ l e _ { 1 } ^ { T } P ,
$$

For instance, for $k = 3$ this matrix is given by

$$
\begin{array} { r } { M \ = \ \left( \begin{array} { c c c c } { 1 } & { 1 - l _ { 0 } } & { 1 - 2 l _ { 0 } } & { 1 - 3 l _ { 0 } } \\ { } & { } & { } & { } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - l _ { 2 } } & { 1 - 2 l _ { 2 } } & { 3 - 3 l _ { 2 } } \\ { 0 } & { - l _ { 3 } } & { - 2 l _ { 3 } } & { 1 - 3 l _ { 3 } } \end{array} \right) \ . } \end{array}
$$

One observes that 1 and O are two eigenvalues of M and that its characteristic polynomial is independent of $l _ { 0 }$ . Nordsieck determined $\boldsymbol { l } _ { 2 } , \ldots , \boldsymbol { l } _ { k }$ in such a way that the remaining eigenvalues of $M$ are zero. For $k = 3$ this yields $\boldsymbol { l } _ { 2 } = 3 / 4$ and $l _ { 3 } { = } 1 / 6$ . The coefficient $l _ { 0 }$ can be chosen such that the error constant of the method (see Theorem 6.2 below) vanishes. In our situation one gets $\iota _ { 0 } { = } 3 / 8$ , so that the method is given by

$$
\boldsymbol { l } = \big ( \frac { 3 } { 8 } , 1 , \frac { 3 } { 4 } , \frac { 1 } { 6 } \big ) ^ { T } \mathrm { ~ . ~ }
$$

It is interesting to note that this method is equivalent to the implicit

3-stepAdaseoeediatiofetes $( h ^ { 3 } / 3 ! ) y _ { n } ^ { \prime \prime \prime }$ and $( h ^ { 2 } / 2 ! ) y _ { n } ^ { \prime \prime }$ by using Formula (6.8) with reduced indices leads to (cf. Formula $\left( 1 . 8 ^ { \circ 3 } \right)$ ）

$$
y _ { n + 1 } = y _ { n } + { \frac { h } { 2 4 } } \cdot [ 9 y _ { n + 1 } ^ { \prime } + 1 9 y _ { n } ^ { \prime } - 5 y _ { n - 1 } ^ { \prime } + y _ { n - 2 } ^ { \prime } ] ~ .
$$

# Equivalence with multistep methods

More insight into the connection between Nordsieck methods and multistep methods is due to Descloux (1963), Osborne (1966), and Skeel (1978). The following two theorems show that every Nordsieck method is equivalent to a multistep form ula and that the order of this method is at least $k$

Theorem 6.1. Consider the Nordsieck method (6.8) where $\boldsymbol { l } _ { 1 } { = } 1$ .The first two components of $z _ { n }$ then satisfy the linear multistep formula (for $n \geq 0$ ）

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } \ = h \sum _ { i = 0 } ^ { k } \beta _ { i } f _ { n + i }
$$

where the generating potynomials are given by

$$
\begin{array} { r } { \mathsf { p } ( \xi ) = \mathsf { d e t } ( \xi I - P ) e _ { 1 } ^ { T } \left( \xi I - P \right) ^ { - 1 } l } \\ { \mathsf { \sigma } ( \xi ) = \mathsf { d e t } ( \xi I - P ) e _ { 0 } ^ { T } \left( \xi I - P \right) ^ { - 1 } l \enspace . } \end{array}
$$

Proof: The proof of the original papers simplifies considerably, if we work with the generating functions (discrete Laplace transformation)

$$
Z \left( \zeta \right) = \sum _ { n \geq 0 } z _ { n } \zeta ^ { n } , Y \left( \zeta \right) = \sum _ { n \geq 0 } y _ { n } \zeta ^ { n } , F \left( \zeta \right) = \sum _ { n \geq 0 } f _ { n } \zeta ^ { n } , \cdots .
$$

Multiplying Formula (6.8') by $\zeta ^ { n + 1 }$ and adding up we obtain

$$
Z \left( \zeta \right) = \zeta P Z \left( \zeta \right) + l \left( h F \left( \zeta \right) - e _ { 1 } ^ { T _ { P } } \zeta Z \left( \zeta \right) \right) + \left( z _ { 0 } - l h f _ { 0 } \right) .
$$

Similarly, the linear multistep method (6.12) can be written as

$$
\hat { \rho } ( \zeta ) Y \left( \zeta \right) = h \hat { \sigma } ( \zeta ) F ( \zeta ) + p _ { k - 1 } ( \zeta ) \ ,
$$

where

$$
\hat { \mathsf { p } } \left( \boldsymbol { \zeta } \right) = \boldsymbol { \zeta } ^ { k } \mathsf { \mathsf { p } } \left( 1 / \zeta \right) , \qquad \hat { \mathsf { o } } \left( \boldsymbol { \zeta } \right) = \boldsymbol { \zeta } ^ { k } \sigma \left( 1 / \zeta \right)
$$

and $p _ { k - 1 }$ is a polynomial of degree $( k - 1 )$ depending on the starting values. In order to prove the theorem we have to show that the first two components of $Z \left( \zeta \right)$ satisfy a relation of the form (6.15). We first

rewrite Equation (6.14) in the form

$$
Z \left( \zeta \right) = \left( I - \zeta P \right) ^ { - 1 } l \left( h F ( \zeta ) - e _ { 1 } ^ { T } P \zeta Z \left( \zeta \right) \right) + \left( I - \zeta P \right) ^ { - 1 } ( z _ { 0 } - l h f _ { 0 } )
$$

so that its first two components become

$$
\begin{array} { r } { Y \left( \zeta \right) = e _ { 0 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } l \left( h F \left( \zeta \right) - e _ { 1 } ^ { T } P \zeta Z \left( \zeta \right) \right) + e _ { 0 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } \left( z _ { 0 } - l h f _ { 0 } \right) } \end{array}
$$

$$
h F ( \zeta ) = e _ { 1 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } l \left( h F ( \zeta ) - e _ { 1 } ^ { T } P \zeta Z \left( \zeta \right) \right) + e _ { 1 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } \left( z _ { 0 } - l h f ( \zeta ) \right)
$$

Eliminating the term in brackets and multiplying by de $\tau ( I - \zeta P$ ）we arrive at Formula (6.15) with

$$
\begin{array} { r } { \hat { \mathsf { \rho } } ( \zeta ) = \operatorname* { d e t } ( I - \zeta P ) e _ { 1 } ^ { T } ( I - \zeta P ) ^ { - 1 } l } \\ { \hat { \boldsymbol { \sigma } } ( \zeta ) = \operatorname* { d e t } ( I - \zeta P ) e _ { 0 } ^ { T } \left( { I - \zeta P } \right) ^ { - 1 } l } \\ { p _ { k - 1 } ( \zeta ) = \operatorname* { d e t } ( I - \zeta P ) \left( e _ { 1 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } l e _ { 0 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } \right. } \\ { \left. - e _ { 0 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } l e _ { 1 } ^ { T } \left( I - \zeta P \right) ^ { - 1 } \right) z _ { 0 } . } \end{array}
$$

With the help of (6.16) we immediately get Formulas (6.13). Therefore,it remains to show that $p _ { k - 1 }$ ,given by (6.17),isa polyomalof degree $( k - 1 )$ . Since the dimension of $P$ is $( k + 1 )$ ， $p _ { k - 1 }$ behaves like $\zeta ^ { k - 1 }$ for $| \zeta |  \infty .$ Finally,therelaion(6.15)impliestatthe Laurent series of $p _ { k - 1 }$ cannot contain negative powers. QED.

Puting $( \zeta I - P ) ^ { - 1 } l = u$ in (6.13) and applying Cramer's rule to the linear system $( \zeta I - P ) u = l$ we obtain from (6.13) the elegant expressions

$$
\begin{array} { r } { \mathsf { p } ( \xi ) = \operatorname* { d e t } \left( \begin{array} { l l l l l } { \xi - 1 } & { l _ { 0 } } & { - 1 } & { \hdots } & { - 1 } \\ { 0 } & { l _ { 1 } } & { - 2 } & { \hdots } & { - k } \\ { 0 } & { l _ { 2 } } & { \xi - 1 } & { \hdots } & { \cdot } \\ { : } & { : } & { : } & { : } \\ { 0 } & { l _ { k } } & { 0 } & { \hdots } & { \xi - 1 } \end{array} \right) } \end{array}
$$

$$
\begin{array} { r } { \sigma ( \xi ) = \operatorname* { d e t } \left( \begin{array} { l l l l l } { l _ { 0 } } & { - 1 } & { - 1 } & { \ldots } & { - 1 } \\ { l _ { 1 } } & { \xi - 1 } & { - 2 } & { \ldots } & { - k } \\ { l _ { 2 } } & { 0 } & { \xi - 1 } & { \ldots } & { , } \\ { : } & { : } & { : } & { : } \\ { l _ { k } } & { 0 } & { 0 } & { \ldots } & { \zeta - 1 } \end{array} \right) ~ . } \end{array}
$$

We observe that $\rho \left( \zeta \right)$ does not depend on $\iota _ { 0 }$ . Further, $\zeta _ { 0 } = 1$ is a sim-ple root of $\rho ( \zeta )$ if and only if $l _ { k } \neq 0$ . We have

$$
\rho ^ { \prime } ( 1 ) = \sigma ( 1 ) = k ! l _ { k } .
$$

Condition (6.9) is equivalent to ${ \alpha } _ { k } = 1$

Theorem 6.2. Assume that $\boldsymbol { l } _ { k } \neq 0$ . The multistep method defined by (6.13) is of order at least k and its error constant (see (2.13)) is given by

$$
C \ = \ - \ \frac { \boldsymbol { b } ^ { T } \boldsymbol { l } } { k ! l _ { k } } \ .
$$

Here the components of

$$
b ^ { T } = ( B _ { 0 } , B _ { 1 } , \ldots , B _ { k } ) = ( 1 , - \frac { 1 } { 2 } , \frac { 1 } { 6 } , 0 , - \frac { 1 } { 3 0 } , 0 , \frac { 1 } { 4 2 } , \cdots )
$$

are the Bernoulli numbers.

Proof: By Theorem 2.4 we have order $k$ ,iff

$$
\begin{array} { r } { \mathsf { \rho } \mathsf { ( \zeta ) } - \log \zeta \cdot \sigma \left( \zeta \right) = C _ { k + 1 } ( \zeta - 1 ) ^ { k + 1 } + \mathsf { O } ( ( \zeta - 1 ) ^ { k + 2 } ) \mathrm { ~ , ~ } } \end{array}
$$

Since $\operatorname* { d e t } ( \zeta I - P ) = ( \zeta - 1 ) ^ { k + 1 }$ this is equivalent to

$$
e _ { 1 } ^ { T } { \left( \zeta I - P \right) } ^ { - 1 } l - \log \zeta \cdot e _ { 0 } ^ { T } { \left( \zeta I - P \right) } ^ { - 1 } l = C _ { k + 1 } + \mathbf { O } ( ( \zeta - 1 ) )
$$

and, by (6.18), it suffices to show that

$$
\begin{array} { r } { \big ( \log \zeta \cdot e _ { 0 } ^ { T } - e _ { 1 } ^ { T } \big ) \big ( \zeta I - P \big ) ^ { - 1 } = b ^ { T } + \mathbf { O } \big ( \big ( \zeta - 1 \big ) \big ) \ . } \end{array}
$$

Denoting the left-hand side of (6.19) by $b ^ { T } ( \zeta )$ we obtain

$$
\left( \zeta I - P \right) ^ { T } b ( \zeta ) = \left( \log \zeta \cdot e _ { 0 } - e _ { 1 } \right) .
$$

The $q$ -th component ( $q \geq 2$ ） of this equation

$$
\zeta b _ { q } ( \zeta ) - \sum _ { j = 0 } ^ { q } { \binom { q } { j } } b _ { j } ( \zeta ) = 0
$$

is equivalent to

$$
\frac { \zeta b _ { q } ( \zeta ) } { q ! } - \sum _ { j = 0 } ^ { q } \frac { b _ { j } ( \zeta ) } { j ! } \frac { 1 } { ( q - j ) ! } = 0 ,
$$

which is seen to be a Cauchy product. Hence， Formula becomes

$$
\zeta \sum _ { q \ge 0 } \frac { t ^ { q } } { q ! } ~ b _ { q } ( \zeta ) - e ^ { t } \sum _ { q \ge 0 } \frac { t ^ { q } } { q ! } ~ b _ { q } ( \zeta ) = \log \zeta - t
$$

which yields

$$
\sum _ { q \ge 0 } \frac { \ i ^ { q } } { q ! } \ \not { b } _ { q } ( \zeta ) = \frac { \ i - \log { \zeta } } { e ^ { \ i } - \zeta } \ .
$$

If we set $\zeta = 1$ in this formula we obtain

$$
\sum _ { q \geq 0 } \frac { t ^ { q } } { q ! } ~ b _ { q } ( 1 ) = \frac { t } { e ^ { t } - 1 } ,
$$

therefore $b _ { q } \left( 1 \right) { = } B _ { q }$ ，the $q$ -th Bernoulli number (see Abramowitz-Stegun, Chapter 23). QED.

We have thus shown that to each Nordsieck method (6.8) there corresponds a linear multistep method of order at least k . Our next aim is to establish a correspondence in the opposite direction.

Theorem 6.3. Let $( \rho , \sigma )$ be the generating polynomials of a k-step method (6.12) of order at least k and assume $\alpha _ { k } = 1$ . Then we have:

a) There exists a unique vector l such that p and o are given by (6.13). b) If, in addition, the multistep method is irreducible, then there exists a non-singular transformation $\mathcal { T }$ such that the soiution of $( \delta . 8 ^ { \prime } )$ is related to that of (6.12) by

$$
z _ { n } = T ^ { - 1 } u _ { n }
$$

where the j-th component of $u _ { n }$ is given by

$$
u _ { j } ^ { ( n ) } = \left\{ \begin{array} { l l } { { \displaystyle \sum _ { i = 0 } ^ { j } \{ \alpha _ { { k - j + i } } y _ { n + i } - h \beta _ { { k - j + i } } f _ { n + i } \} } } & { { \quad f o r \quad 0 \leq j \leq k - 1 } } \\ { { \displaystyle h f _ { n } } } & { { \quad ( \mathrm { e r e } ) \quad \alpha = \alpha _ { \mathrm { - } } ( \mathrm { e r e } ) \quad } } \end{array} \right.
$$

Proof: a) For any $k$ -th order multistep method the polynomial $\rho ( \zeta )$ is uniquely determined by $\sigma \left( \zeta \right)$ (see Theorem 2.4). Expanding the determinant in (6.13b) with respect to the first column we see that

$$
\sigma \left( \zeta \right) = l _ { 0 } ( \zeta - 1 ) ^ { k } + l _ { 1 } ( \zeta - 1 ) ^ { k - 1 } r _ { 1 } ( \zeta ) + \dots + l _ { k } r _ { k } ( \zeta ) ,
$$

where $r _ { j } ( \zeta )$ is a polynomial of degree $j$ satisfying $r _ { j } ( 1 ) \not = 0$ . Hence, l can be computed from $\sigma \left( \zeta \right)$

b) Let $y _ { 0 } , \ldots , y _ { k - 1 }$ and $f _ { \mathrm { ~ 0 ~ } } , \hdots , f _ { k - 1 }$ be given. Then the polyno-mial $p _ { k - 1 } ( \zeta )$ in (6.15) satisfies

$$
p _ { k - 1 } ( \zeta ) = u _ { 0 } ^ { ( 0 ) } + u _ { 1 } ^ { ( 0 ) } \zeta + \cdot \cdot \cdot + u _ { k - 1 } ^ { ( 0 ) } \zeta ^ { k - 1 } .
$$

$\mathrm { o n }$ the other hand, if the starting vector for the Nordsieck method $^ z _ { 0 }$   
defined by i of a) is known, then $p _ { k - 1 } ( \zeta )$ is given by (6.17). Equating   
both expressions we obtain

$$
\sum _ { j = 0 } ^ { k - 1 } u _ { j } ^ { ( 0 ) } \zeta ^ { j } = \big ( \hat { \mathsf { p } } ( \zeta ) e _ { 0 } ^ { T } - \hat { \sigma } ( \zeta ) e _ { 1 } ^ { T } \big ) \big ( I - \zeta P \big ) ^ { - 1 } z _ { \phantom { ( } 0 } \ .
$$

We now denote by $t _ { j } ^ { T }$ $( j = 0 , \ldots , k - 1 )$ the coefficients of the vector polynomial

$$
\big ( \hat { \rho } ( \zeta ) e _ { 0 } ^ { T } - \hat { \sigma } ( \zeta ) e _ { 1 } ^ { T } \big ) \big ( I - \zeta P \big ) ^ { - 1 } = \sum _ { j = 0 } ^ { k - 1 } t _ { j } ^ { T } \zeta ^ { j }
$$

and set $\boldsymbol { t } _ { k } ^ { T } { = } \boldsymbol { e } _ { 1 } ^ { T } .$ Then let $T$ be the square matrix whose $j$ -th row is $t _ { j } ^ { T }$ so that ${ \boldsymbol { u } } _ { 0 } = T { \boldsymbol { z } } _ { 0 }$ is a consequence of (6.23) and $h f _ { n } = h y _ { n } ^ { \prime }$ . The same argument applied to $y _ { n } ~ , ~ \ldots ~ , y _ { n + k - 1 }$ and $f _ { n } ~ , ~ \dots , f _ { n + k - 1 }$ instead of $y _ { 0 } , \ldots , y _ { k - 1 }$ and $f _ { 0 } , \dots , f _ { k - 1 }$ yields $u _ { n } = T z _ { n }$ for al $_ \pi$

To complete the proof it remains to verify the non-singularity of $T$ .Let $\nu = ( \nu _ { 0 } , _ { _ { T } 1 } , \ldots , \nu _ { _ { k } } ) ^ { l }$ be a non-zero vector satisfying $T \nu = 0$ By definition of $t _ { k } ^ { T }$ we have $\nu _ { \uparrow } { = } 0$ and from (6.24) it follows (using the transformation (6.16)) that

$$
\begin{array} { r } { \mathsf { \rho } ( \xi ) \boldsymbol { \tau } _ { 0 } ( \xi ) = \sigma ( \xi ) \boldsymbol { \tau } _ { 1 } ( \xi ) \mathrm { ~ , ~ } } \end{array}
$$

where $\tau _ { i } ( \zeta ) { = } \operatorname* { d e t } ( \zeta I - P ) e _ { i } ^ { I } ( \zeta I - P ) ^ { - 1 } \nu$ are polynomials of degree at most $k$ . Moreover, Cramer's rule shows that the degree of $\tau _ { 1 } ( \zeta )$ is at most $k - 1$ , since $\nu _ { 1 } { = } 0$ . Hence from (6.25) at least one of the roots of $\rho ( \zeta )$ must be a root of $\sigma \left( \zeta \right) .$ This is in contradiction with the assumption that the method is irreducible. QED.

The vectors l which correspond to the implicit Adams methods and to the BDF-methods are given in Tables 6.1 and 6.2. For these two classes of methods we shall investigate the equivalence in some more detail.

Table 6.1. Coefficients $l _ { j }$ of the $k$ -step implicit Adams methods   

<table><tr><td></td><td>10</td><td>1</td><td>12</td><td>13</td><td>4</td><td>15</td><td>6</td></tr><tr><td>k=1</td><td>1/2</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>k =2</td><td>5/12</td><td>1</td><td>1/2</td><td></td><td></td><td></td><td></td></tr><tr><td>k =3</td><td>3/8</td><td>1</td><td>3/4</td><td>1/6</td><td></td><td></td><td></td></tr><tr><td>k =4</td><td>251/720</td><td>1</td><td>11/12</td><td>1/3</td><td>1/24</td><td></td><td></td></tr><tr><td>k =5</td><td>95/288</td><td>1</td><td>25/24</td><td>35/72</td><td>5/48</td><td>1/120</td><td></td></tr><tr><td>k =6</td><td>19087/60480</td><td>1</td><td>137/120</td><td>5/8</td><td>17/96</td><td>1/40</td><td>1/720</td></tr></table>

Table 6.2. Coefficients l, of the k -step BDF-methods   

<table><tr><td></td><td>10</td><td>11</td><td>12</td><td>13</td><td>A</td><td>15</td><td>16</td></tr><tr><td>k=1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>k =2</td><td>2/3</td><td>1</td><td>1/3</td><td></td><td></td><td></td><td></td></tr><tr><td>k=3</td><td>6/11</td><td>1</td><td>6/11</td><td>1/11</td><td></td><td></td><td></td></tr><tr><td>k =4</td><td>12/25</td><td>1</td><td>7/10</td><td>1/5</td><td>1/50</td><td></td><td></td></tr><tr><td>k =5</td><td>60/137</td><td>1</td><td>225/274</td><td>85/274</td><td>15/274</td><td>1/274</td><td></td></tr><tr><td>k=6</td><td>20/49</td><td>1</td><td>58/63</td><td>5/12</td><td>25/252</td><td>1/84</td><td>1/1764</td></tr></table>

# Implicit Adams methods

The following results are due to Byrne-Hindmarsh (1975). Since their "efficient package" EPISODE is based on the Nordsieck representation of variable step size methods, we extend our considerations to this case. The Adams methods define in a natural way a polynomial which approximates the unknown solution of (6.2). Namely, if $y _ { n }$ and $f _ { n } ~ , ~ \dots , f _ { n - k + 1 }$ are given, then the $k$ -step Adams method is equivalent to the construction of a polynomial $p _ { n + 1 } ( x )$ of degree $( k + 1 )$ which satisfies

$$
p _ { n + 1 } ( x _ { n } ) = y _ { n } , \qquad p _ { n + 1 } ( x _ { n + 1 } ) = y _ { n + 1 } ,
$$

$$
p _ { n + 1 } ^ { \prime } ( x _ { j } ) = f _ { j } \qquad \mathrm { f o r } \quad j = n - k + 1 , \ldots , n + 1 \ .
$$

Condition (6.26） defines $y _ { n + 1 }$ implicitly.Weobserve thatthe difference of two consecutive polynomials, $p _ { n + 1 } ( x ) { - } p _ { n } \left( x \right)$ ,vanishes at $x _ { n }$ and that its derivative is zero at $x _ { n - k + 1 } , \ldots , x _ { n }$ Therefore, if we let $e _ { n + 1 } { = } y _ { n + 1 } { - } p _ { n } ( x _ { n + 1 } )$ , this difference can be written as

$$
p _ { n + 1 } ( x ) - p _ { n } ( x ) = \Lambda \bigl ( \begin{array} { l } { { \frac { x - x _ { n + 1 } } { x _ { n + 1 } - x _ { n } } } } \end{array} \bigr ) e _ { n + 1 }
$$

where $\Lambda$ is the unique polynomial of degree $\left( k + 1 \right)$ defined by

$$
\Lambda ( 0 ) = 1 , \qquad \Lambda ( - 1 ) = 0
$$

$$
\Lambda ^ { \prime } ( \mathrm { ~ \frac { ~ } { ~ } } x _ { n + 1 } - x _ { n } + 1 { } ) = 0 \qquad \mathrm { f o r } \quad j = n - k + 1 , \ldots , n \ .
$$

The derivative of (6.27) taken at ${ x = x } _ { n + 1 }$ shows that with $h _ { n } = x _ { n + 1 } - x _ { n }$

$$
h _ { n } f _ { n + 1 } - h _ { n } p _ { n } ^ { \prime } ( x _ { n + 1 } ) = \Lambda ^ { \prime } ( 0 ) e _ { n + 1 } .
$$

If we introduce the Nordsieck vector

$$
\tilde { z } _ { n } = \left( p _ { n } ( x _ { n } ) , h _ { n } p _ { n } ^ { \prime } ( x _ { n } ) , \dots , \frac { h _ { n } ^ { k + 1 } } { ( k + 1 ) ! } p _ { n } ^ { ( k + 1 ) } ( x _ { n } ) \right) ^ { T }
$$

and the coefficients $\tilde { l } _ { j }$ by

$$
\Lambda ( t ) = \sum _ { j = 0 } ^ { k + 1 } \tilde { l } _ { j } t ^ { j } ,
$$

then (6.27) becomes equivalent to

$$
\begin{array} { r } { \tilde { z } _ { n + 1 } = P \tilde { z } _ { n } + \tilde { l } \tilde { l } _ { 1 } ^ { - 1 } [ h f _ { n + 1 } - e _ { 1 } ^ { T } P \tilde { z } _ { n } ] } \end{array}
$$

with $\bar { \boldsymbol { l } } \ = \big ( \bar { l } _ { 0 } , \bar { l } _ { 1 } , \dots , \bar { l } _ { k + 1 } \big ) ^ { T } .$ This method is of the form (6.8)). However, it is of dimension k $+ 2$ and not, as expected by Theorem 6.3, of dimension $k + 1$ . The reason is the following: let $\tilde { \rho } ( \zeta )$ and $\tilde { \sigma } \left( \zeta \right)$ be the generating polynomials of the multistep method which corresponds to (6.30). Then the conditions $\Lambda ( - 1 ) = 0$ and $\Lambda ^ { \prime } ( - 1 ) { = } 0$ imply that ${ \tilde { \sigma } } \left( 0 \right) { = } { \tilde { \rho } } \left( 0 \right) { = } 0$ ， so that this method is reducible. Nevertheless, Method (6.30) is useful, since the last component of $\tilde { z } _ { n }$ can be used for step size control.

Remark . For $k \geq 2$ the coefficients $\tilde { l } _ { j }$ , defined by (6.29), depend on the step size ratios $h _ { j } / h _ { j - 1 }$ for $j = n - k + 2 , \ldots , n$ . They can be computed from the formula

$$
\Lambda ( t ) = \frac { \displaystyle \int _ { - 1 } ^ { t } \prod _ { j = 1 } ^ { k } ( s - t _ { j } ) d s } { \displaystyle \int _ { - 1 } ^ { t } \prod _ { j = 1 } ^ { k } ( s - t _ { j } ) d s }
$$

where $t _ { j } = ( x _ { n - j + 1 } - x _ { n + 1 } ) / ( x _ { n + 1 } - x _ { n } )$ (see also Exercise 1).

# BDF-methods

One step of the $k$ -step BDF-method consists in constructing a polynomial $q _ { n + 1 } ( x )$ of degree $k$ which satisfies

$$
\begin{array} { r l r } { q _ { n + 1 } ( x _ { j } ) } & { { } = y _ { j } } & { \mathrm { f o r } j = n - k + 1 , \ldots , n + 1 } \\ { \quad } & { { } } & { \quad } \\ { q _ { n + 1 } ^ { \prime } ( x _ { n + 1 } ) } & { { } = f _ { n + 1 } } & { } \end{array}
$$

and in computing a value $y _ { n + 1 }$ which makes this possible. As for the Adams methods we have

$$
q _ { n + 1 } ( x ) - q _ { n } ( x ) = \Lambda ( \ \frac { x - x _ { n + 1 } } { x _ { n + 1 } - x _ { n } } \ ) \cdot ( y _ { n + 1 } - q _ { n } ( x _ { n + 1 } ) ) \ ,
$$

where $\Lambda \left( t \right)$ is the polynomial of degree $k$ defined by

$$
\Lambda ( \mathrm { ~ \frac { { { x _ { j } } - { x _ { n + 1 } } } } { { { x _ { n + 1 } } - { x _ { n } } } } ~ } ) = 0 \qquad \mathrm { { f o r } } j = n - k + 1 , \ldots , n
$$

$$
\Lambda ( 0 ) = 1 \ .
$$

With the vector

$$
\tilde { z } _ { n } = \bigg ( q _ { n } ( x _ { n } ) , h _ { n } q _ { n } ^ { \prime } ( x _ { n } ) , \dots , \frac { h _ { n } ^ { k } } { k ! } q _ { n } ^ { ( k ) } ( x _ { n } ) \bigg ) ^ { T }
$$

and the coefficients $\tilde { l } _ { j }$ given by

$$
\Lambda ( t ) = \sum _ { j = 0 } ^ { k } \tilde { l } _ { j } t ^ { j } ,
$$

Equation (6.33) becomes

$$
\tilde { z } _ { n + 1 } = P \tilde { z } _ { n } + \tilde { l } \tilde { l } _ { 1 } ^ { - 1 } [ h f _ { n + 1 } - e _ { 1 } ^ { T } P \tilde { z } _ { n } ] \ .
$$

The vector $\bar { \boldsymbol { l } } = ( \bar { l } _ { 0 } , \bar { l } _ { 1 } , \dots , \bar { l } _ { k } ) ^ { T }$ can be computed from the formula

$$
\Lambda ( t ) = \prod _ { j = 1 } ^ { k } ( 1 + \frac { t } { t _ { j } } )
$$

where $t _ { j } = ( x _ { n - j + 1 } - x _ { n + 1 } ) / ( x _ { n + 1 } - x _ { n } )$ For constant step sizes Formula (6.34) corresponds to that of Theorem 6.3 and the coefficients $l _ { j } = { l _ { j } } / { l _ { 1 } }$ coincide with those of Table 6.2.

# Exercises

1. Let $\mathcal { l } _ { j } ^ { ( k ) } \left( j = 0 , \ldots , k \right)$ be the Nordsieck coeffcients of the k -step implicit Adams methods (defined by Theorem 6.3 and given in Table 6.1). Further, denote by i(k） $( j = 0 , \ldots , k + 1 )$ the coefficients given by (6.29) and (6.31) for the case of constant step sizes. Show that

$$
\frac { \bar { l } _ { j } ^ { ( k ) } } { \bar { l } _ { 1 } ^ { ( k ) } } = \left\{ \begin{array} { l l } { { \displaystyle l _ { j } ^ { ( k ) } } } & { { \quad \mathrm { f o r } \quad j = 0 } } \\ { { \displaystyle l _ { j } ^ { ( k + 1 ) } } } & { { \quad \mathrm { f o r } \quad j = 1 , . . . , k + 1 . } } \end{array} \right.
$$

Use these relations to verify Table 6.1.

2. a) Calculate the matrix $T$ of Theorem 6.3 for the 3-step implicit Adams method. Result.

$$
\begin{array} { r } { T ^ { - 1 } = \left( \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 3 / 8 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 6 } & { 6 } & { 3 / 4 } \\ { 0 } & { 4 } & { 1 2 } & { 1 / 6 } \end{array} \right) \ . } \end{array}
$$

Show that the Nordsieck vector $z _ { n }$ is given by

$$
\begin{array} { r } { \underline { { \tau } } _ { n } ~ = ~ \biggl ( y _ { n } ~ , ~ h f _ { n } ~ , ~ ( 3 h f _ { n } - 4 h f _ { n - 1 } + h f _ { n - 2 } ) / 4 , ~ ( h f _ { n } - 2 h f _ { n - 1 } + h f _ { n - 2 } ) / 6 \biggr ) } \end{array}
$$

b) The vector ${ \tilde { z } } _ { n }$ for the 2-step implicit Adams method (6.30) (constant step sizes) also satisfies

$$
\begin{array} { r } { \mathrm { ~  ~ \lambda ~ } _ { \mathrm { ~ \mathfrak { n } ~ } } = \left( y _ { n } , \ h f _ { n } , \ ( 3 h f _ { n } - 4 h f _ { n - 1 } + h f _ { n - 2 } ) / 4 , \ ( h f _ { n } - 2 h f _ { n - 1 } + h f _ { n - 2 } ) / 6 \right) ^ { T } } \end{array}
$$

but this time $y _ { n }$ is a less accurate approximation to $y \left( x _ { n } \right)$

There is a great deal of freedom in the implementation of multistep methods (even if we restrict our considerations to the Adams methods) One can either directly use the variable step size methods of Section iI.5 or one can take a fixed step size method and determine the necessary offgrid values, which are needed for a change of step size，by interpolation. Further， it is possible to choose between the divided difference formulation (5.7) and the Nordsieck representation (6.30).

The historical approach was the use of Formula (1.8) together with interpolation (J.C. Adams (1883): "We may, of course, change the value of ω (the step size) whenever the more or less rapid rate of diminution of the successive differences shews that it is expedient to increase or diminish the interval. It is only necessary， by selection from or interpolation between the values already calculated, to find the coordinates for a few values of $\boldsymbol { \Phi }$ separated from each other by the newly chosen interval."). It is theoretically more satisfactory and more elegant to work with the variable step size method (5.7). For both of these approaches the change of step size is rather expensive whereas the change of order is very simple - one just has to add a further term to the expansion (1.8). If the Nordsieck representation (6.30) is implemented, the situation is the opposite.There, the change of order is not as direct as above, but the step size can simply be changed by a multiplication of the Nordsieck-vector (6.1) by the diagonal matrix $\mathrm { d i a g } ( 1 , \omega , \omega ^ { 2 } , \ldots )$ where $\omega = h _ { _ { n e w } } / h _ { o l d }$ is the step size ratio. Indeed, this was the main reason for introducing this representation.

# Step size and order selection

Much was made of the starting of multistep computations and the need for Runge-Kut methods in the literature Of the 60ies (see e.g. Ralston (1962)). Nowadays, codes for multistep methods sim ply start with order one and very small step sizes and are therefore selfstarting.

Suppose then that the numerical integration has proceeded successfully until $x _ { n }$ and that a further step with step size $h _ { n }$ and order $k + 1$ is taken，which yields theapproximation $y _ { n + 1 }$ to $y \left( x _ { n + 1 } \right)$ To decide whether $y _ { n + 1 }$ will be accepted or not, we need an estimate of the local truncation error. Such an estimate is e.g. given by

$$
l e _ { k + 1 } ( n + 1 ) = y _ { n + 1 } - y _ { n + 1 } ^ { * }
$$

where $y _ { n + 1 } ^ { * }$ is the result of the $( k + 2 )$ -nd order implicit Adams formula. Subtracting Formula (5.7) from the same formula with k replaced by $k + 1$ , we obtain

$$
l e _ { k + 1 } ( n + 1 ) = h _ { n } ( g _ { k + 1 } ( n ) - g _ { k } ( n ) ) \Phi _ { k + 1 } ( n + 1 ) \ ,
$$

Without changing the leading term in this expression we can replace $\Phi _ { k + 1 } ( n + 1 )$ by

$$
\Phi _ { k + 1 } ^ { p } ( n + 1 ) = \prod _ { i = 0 } ^ { k } ( x _ { n + 1 } - x _ { n - i } ) f ^ { p } [ x _ { n + 1 } , x _ { n } , . . . , x _ { k } ] \ ,
$$

The superscript $\boldsymbol { p }$ of $f$ indicates that ${ f _ { n + 1 } } ^ { = } ( x _ { n + 1 } , y _ { n + 1 } )$ is replaced by $f \left( x _ { n + 1 } , p _ { n + 1 } \right)$ when forming the divided differences. If the implicit equation (5.7) is solvcd iteratively with as predictor, then $\Phi _ { k + 1 } ^ { p } ( n + 1 )$ has to be calculated anyway. Therefore,the only cost for computing the estimate

$$
L E _ { k + 1 } ( n + 1 ) = h _ { n } ( g _ { k + 1 } ( n ) - g _ { k } ( n ) ) \Phi _ { k + 1 } ^ { p } ( n + 1 )
$$

is the computation of $g _ { k + 1 } ( n )$ . After the expression (7.3) has been calculated, we require (in some suitable norm)

$$
\left| \left\lfloor L E _ { k + 1 } ( n + 1 ) \right\rfloor \right| \leq T O L
$$

for the step to be successful.

If the Nordsieck representation (6.30) is considered instead of (5.7), then the estimate of the local error is not as simple, since the l-vectors in (6.30) are totally different for different orders. For a possible error-estimate we refer to the article of Byrne-Hindmarsh (1975).

Suppose now that $y _ { n + 1 }$ is accepted. We next have to choose a new step size and a new order. The idea of the step size selection is to find the largest $h _ { n + 1 }$ for which the predicted local error is acceptable, i.e. for which

$$
h _ { n + 1 } \cdot \vert g _ { k + 1 } ( n + 1 ) - g _ { k } ( n + 1 ) \vert \cdot \vert \vert \Phi _ { k + 1 } ^ { p } ( n + 2 ) \vert \vert \le T O L .
$$

However, this procedure is of no practical use, since the expressions $g _ { j } ( n + 1 )$ and $\Phi _ { k + 1 } ^ { p } ( n + 2 )$ dcpendinacomplicatcdmanrthc unknown step size $h _ { n + 1 }$ Also，the coeffcients $g _ { k + 1 } ( n + 1 )$ and $g _ { k } \left( n + 1 \right)$ are too expensive to calculate. To overcome this difficulty we assume the grid to be equidistant (this is a doubtful assumption, but leads to a simple formula for the new step size). In this case the local error (for the method of order $k + 1$ ）is of the form

$C \left( \boldsymbol { x } _ { n + 2 } \right) h ^ { k + 2 } + \mathbf { O } \left( h ^ { k + 3 } \right)$ with $C$ depending smoothly on $x$ . The local error at $x _ { n + 2 }$ can thus be approximated by that at $x _ { n + 1 }$ and in the same way as for one-step methods (cf. Section II.4 Formula (4.7)) we obtain

$$
h \left( k + 1 \right) = \left( \frac { T O L } { L E _ { k + 1 } ( n + 1 ) } \right) ^ { 1 / ( k + 2 ) }
$$

as optimal step size. The local error $L E _ { k + 1 } ( n + 1 )$ is given by (7.3) or, again under the assumption of an equidistant grid, by

$$
L E _ { k + 1 } ( n + 1 ) = h \gamma _ { k + 1 } ^ { * } \Phi _ { k + 1 } ^ { p } ( n + 1 )
$$

with $\gamma _ { k + 1 } ^ { * }$ from Table 1.2 (see Exercise 1 of Section I.5 and Exercise 4 of Section III.1).

We next describe how an optimal order can be determined. Since the number of necessary function evaluations is the same for all orders, there are essentially two strategies for selecting the new order. One can choose the order $k + 1$ either such that the local error estimate is minimal, or such that the new optimal step size is maximal. Because of the exponent $1 / \left( k + 2 \right)$ in Formula (7.5), the two strategies are not always equivalent. For more details see the description of the code DEABM below. It should be mentioned that each implementation of the Adams methods - and there are many - contains refinements of the above description and has in addition several adhocdevices.Eeepsthtepsiecotti $h _ { n e w } / h _ { o l d }$ is near to 1. In this way the computation of the coefficents $g _ { j } ( n )$ is sim plified.

# Some available codes

We have chosen the three codes DEABM, EPISODE and LSODE to demonstrate the order- and step size strategies for multistep methods.

DEABM is a modification of the code DE described in the book of Shampine-Gordon (1975). It dates from 1980 and is due to Shampine-Watts. Our numerical tests use the revised version from February 1984. For European users it is available from the 'Rechen-zentrum der RWTH Aachen, Seffenter Weg 23, D - 5100 Aachen, West-Germany".

This code implements the variable step size, divided difference representation (5.7) of the Adams formulas. In order to solve the nonlinear equation (5.7) for $y _ { n + 1 }$ the value $p _ { n + 1 }$ is taken as predictor $\left( P \right)$ ，then ${ { f } _ { n + 1 } ^ { p } } \mathrm { { = } } f \left( { { x } _ { n + 1 } } , { { p } _ { n + 1 } } \right)$ is calculated $[ E _ { }$ ） and one corrector iteration ( $C$ ）is performed, to obtain $y _ { n + 1 }$ Finally, if the step is successful, ${ { f } _ { n + 1 } } \mathop { = } f \left( { { x } _ { n + 1 } } , { { y } _ { n + 1 } } \right)$ is evaluated $[ E _ { }$ ) for the next step. This PECE implementation needs two function evaluations for each successful step. Let us also outline the order strategy of this code: after performing a step with order $k + 1$ ，one computes $L E _ { k - 1 } ( n + 1 ) _ { : }$ $L E _ { k } { \left( n + 1 \right) }$ and $L E _ { k + 1 } ( n + 1 )$ using a slight modification of (7.6). Then the order is reduced by one, if

$$
\operatorname* { m a x } \bigg ( \| \ L E _ { k - 1 } ( n + 1 ) \| ~ , \ \| \ L E _ { k } ( n + 1 ) \| ~ \bigg ) \leq \| \ L E _ { k + 1 } ( n + 1 ) \| ~ .
$$

An increase in the order is considered only if the step is successful, (7.7) is violated and a constant step size is used. In this case one computes the estimate

$$
L E _ { k + 2 } ( n + 1 ) = h \gamma _ { k + 2 } ^ { * } \Phi _ { k + 2 } ( n + 1 )
$$

using the new value ${ { f } _ { n + 1 } } \mathop { = } f \left( { { x } _ { n + 1 } } , { { y } _ { n + 1 } } \right)$ and increases the order by one if

$$
\| ~ L E _ { k + 2 } ( n + 1 ) \| ~ < ~ \| ~ L E _ { k + 1 } ( n + 1 ) \| ~ .
$$

In Figure 7.1 we demonstrate the variation of the step size and order on the example of Section II.4 (see Figure 4.1 and also Figure 9.5 of Section I1.9). We plot the solution, the step size and order for the tolerances $1 0 ^ { - 3 }$ $1 0 ^ { - 6 }$ and $1 0 ^ { - 9 }$ Compared to the extrapolation code ODEX (Section II.9) the behaviour of the selected order is totally different. Only the step size - and not the order - drops significantly at passages where the solution varies more rapidly. We also observe that constant step sizes are taken over long intervals and that the order is changed rather often (especially for $T { \bar { O } } L = 1 0 ^ { - 9 }$ ). This is in agreement with the observation of Shampine - Gordon (1975): ".. small reductions in the estimated error may cause the order to fluctuate, which in turn helps the code continue with constant step size."

EPISODE with parameter $M F = 1 0$ is an implementation of the variable order Nordsieck representation (6.30) of the Adams methods. It is due to Byrne-Hindmarsh (1975) and is available from the "National Energy Software Center, Building 21， Argonne National Laboratory, 9700 South Cass Avenue, Argonne IL 60439, USA" or from 'NEA Data Bank, B.P. No.9 (Bat. 45), F-91190 GIFsur-YVETTE, FRANCE". We used the version of April 5, 1977. This code differs in several respects from DEABM. The nonlinear equation (first component of (6.30)） is solved by fixed-point iteration until convergence. No final $f$ -evaluation is performed. This method can thus be interpreted as a $P \left( E C \right) ^ { M }$ -method, where M , the number of iterations, may be different from step to step. E.g. in the cxample of Figure 7.2 ( $T { \dot { O } } L = 1 0 ^ { - 6 }$ ） only 410 function evaluations are needed for 340 steps. This shows that for most steps one iteration is sufficient.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/c54753520ef54e4aacde21422db82a778a45980376b61bc7f2faf8b813d00f5d.jpg)  
Figure 7.1. Step size and order variation for the code DEABM

The order selection in EPISODE is based on maximizing the step size among $h _ { k } \left( n + 1 \right)$ ， $h _ { k + 1 } ( n + 1 )$ ， $h _ { k + 2 } ( n + 1 ) .$ Figure 7.2 presents the step size and order variation for EPIsODE for the same example as above: compared to DEABM we observe that much lower orders are taken. Further, the order is nearly constant over the whole interval. This is reasonable, since a change in the order is not natural for the Nordsieck representation.

LSODE (with parameter $M F = 1 0$ ） is another implementation of the Adams methods. This is a successor of the code GEAR (Hindmarsh, 1972)，which is itself a revised and improved code based on DIFSUB of Gear (1971). We used the version of June 17, 1980. It is available from the same addresses as EPISODE. LSODE is based on the Nordsieck representation of the fixed step size Adams formulas. The change of step size and order behaves similarly to that for EPISODE (see Figure 7.3).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/45c87cbb06b8ffc14b89d9753194a0d3171f7371e13cd4625748152b2e20b251.jpg)  
Figure 7.2. Step size and order variation for the code EPISODE

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/63170ac44e9bf8b6b1b488001ab1dfec88bc0490ee8224cc1f29c6b13656c27e.jpg)  
Figure 7.3. Step size and order variation for the code LSODE

# Numerical comparis ons

Of the three families of methods, the fixed order Runge-Kutta is the simplest, in several respects the best understood, and the least efficient." (Shampine-Gordon, 1975)

It is, of course, interesting to compare the different implementations of the same numerical method. Besides DEABM, EPISODE and LSODE we also consider the NAG-subroutine D02CAF (NAGlibrary， Mark 10)，which is a version of the GEAR-programm of Hindmarsh. We have also included the results of the fixed order Runge-Kutta code DOPRI8 (Section II.6) in order to see the different behaviours of one step- and multistep-methods.

Table 7.1. Codes used for comparison.   

<table><tr><td>Code</td><td>graphs in the figures</td><td> storage for large N</td></tr><tr><td>DEABM</td><td>11111</td><td>22·N</td></tr><tr><td>EPISODE</td><td>_&quot;_._&quot;_*</td><td>18N</td></tr><tr><td>LSODE</td><td>-&#x27;_.._·_</td><td>17:N</td></tr><tr><td>D02CAF</td><td></td><td>19·N</td></tr><tr><td>DOPRI8</td><td></td><td>9·N</td></tr></table>

With all these methods we have computed the numerical solution for the six problems JACB, TWOB, VDPL, BRUS, LAGR, PLEI of Section II.10 (using the five tolerances $1 0 ^ { - 3 }$ ， $1 0 ^ { - 6 }$ $1 0 ^ { - 9 }$ ， $1 0 ^ { - 1 2 }$ ， $1 0 ^ { - 1 5 } )$ . Figure 7.4 gives the number of function calls plotted against the achieved accuracy in double logarithmic scale. It seems that there is an advantage for the code DEABM (at least for $T O L \le 1 0 ^ { - 5 }$ ）、 DOPRI8 and EPIsODE necd the largest number of function evaluations. The authors of EPISODE recommend this code "for problems with highly varied levels of activity in the solution". The Runge-Kutta code DOPRI8 has much lower overhead (computer time for the operations outside the function subroutine) than the multistep methods. This can be seen in Figure 7.5 where we have plotted for the same six problems the CPU time (on the UNIVAC 1100/60 com - puter) against the achieved accuracy (in double logarithmic scale).

We observe that for problems with cheap function evaluations (this is the case for the first five cxamples) thc Runge-Kutta code needs much less CPU time than the multistep codes, although more function evaluations are neccssary in general. For the PLEI problem, where the right hand side is rathcr expensive to evaluate， the discrepancy is not as large.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/4526ff100184b2da7f6f5904804a034231209787c4865d15afc2b1274a16441f.jpg)  
Figure 7.4. Function calls of different codes for the six problems of Section [.10

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/e1d7f0962612be1b2504992a8218eb43a78f4716717581d1b7d7004f89b4887b.jpg)  
Figure 7.5. CPU time (in seconds) of different codes for the six problems of Section II.10

Our next aim is to study the case where the dimension of the problem is very high, but the individual components are not too complicated.

# A partial differential equation

We consider the reaction-diffusion equation (Brusselator with diffusion)

$$
\begin{array} { r l } & { \frac { \partial u } { \partial t } = 1 + u ^ { 2 } \nu - 4 . 4 u + \alpha ( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ) } \\ & { } \\ & { \frac { \partial \nu } { \partial t } = 3 . 4 u - u ^ { 2 } \nu + \alpha ( \frac { \partial ^ { 2 } \nu } { { \partial x ^ { 2 } } } + \frac { \partial ^ { 2 } \nu } { \partial y ^ { 2 } } ) } \end{array}
$$

for $0 \le x \le 1 , \ 0 \le y \le 1 , \ t \ge 0 , \ \alpha = 2 \cdot 1 0 ^ { - 3 }$ together with the Neumann boundary conditions

$$
\begin{array} { r } { \frac { \partial u } { \partial \mathbf { n } } = 0 , \qquad \frac { \partial \nu } { \partial \mathbf { n } } = 0 \ , } \end{array}
$$

and the initial conditions

$$
\begin{array} { l } { { \displaystyle { u \left( x , y , 0 \right) = 0 . 5 + y } } } \\ { { \mathrm { } } } \\ { { \nu \left( x , y , 0 \right) = 1 + 5 x } } \end{array} .
$$

By the method of lines (cf. Section I.6) this problem can be transformed into a system of ordinary differential equations. We put

$$
x _ { i } = \frac { i - 1 } { N - 1 } \qquad i = 1 , \dots , N \qquad y _ { j } = \frac { j - 1 } { N - 1 } \qquad j = 1 , \dots , N
$$

and define

$$
\begin{array} { r c l } { { U _ { i j } ( t ) = u \left( x _ { i } , y _ { j } , t \right) } } \\ { { } } & { { } } \\ { { V _ { i j } ( t ) = \nu \left( x _ { i } , y _ { j } , t \right) . } } \end{array}
$$

Discretizing the derivatives with respect to the space variables in (7.8 we obtain for i, j=1,...,N

$$
\begin{array} { r l } & { \textsf { v } \times \arctan \textsf { r o r } _ { i j } \ldots \textsf { z } _ { j } - \textsf { z } _ { i } \ldots \textsf { z } _ { i } ^ { \textsf { z } } } \\ &  \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \alpha } } } } } } } } } } \\ &  \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \beta } } } } } } } \\ & { \textsf { \textsf { \textsf { \textsf { \textsf { \beta } } } } } } \\ & { \textsf { \textsf { \textsf { \textsf { \beta } } } } = 3 . 4 \bar { U } _ { i j } - \bar { U } _ { i j } ^ { 2 } \bar { V } _ { i j } + \alpha \left( N - 1 \right) ^ { 2 } \biggl ( \bar { V } _ { i + 1 , j } + \bar { V } _ { i - 1 , j } + \bar { V } _ { i , j + 1 } + \bar { V } _ { i , j - 1 } - 4 \bar { V } _ { i j } \biggr ) \enspace , } \end{array}
$$

an ODE of dimension $2 N ^ { 2 }$ In (7.12) the values $U _ { 0 j }$ ， $U _ { N + 1 , j }$ ， $U _ { i 0 } , \ldots$ are not yet defined. Because of the boundary condition (7.9) they have to be chosen as follows:

$$
U _ { 0 j } = U _ { 2 j } ~ , ~ U _ { N + 1 , j } = U _ { N - 1 , j } ~ , ~ U _ { i 0 } = U _ { i 2 } ~ , ~ U _ { i , N + 1 } = U _ { i , N - 1 }
$$

and similarly for the $V _ { i j }$ quantities.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/6f82d5335b4b3d36e9b066f6f56bbebf439bcb078efe337188088017f44a6232.jpg)  
Figure 7.6. Solution $u \left( x , y , t \right)$ for t =0,0.5 , ... ,11.5

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/105d795cbcdd65ebda8c4be15c603e10e1dd17bcaef7571d9b7008655442ac54.jpg)  
Figure 7.7. Solution $\nu \left( x , y , t \right)$ for $\iota = 0 , 0 . 5 , \ldots , 1 1 . 5$

The solution of (7.12) as a function of $( x _ { i } , y _ { j } )$ (for $N = 2 1$ ）is represented in Figure 7.6 and Figure 7.7 for the equidistant time values $\iota = 0 , 0 . 5 , 1 , 1 . 5 , \ldots , 1 1 . 5$

Wc now apply the different codes to the problem (7.12) with $N = 2 1$ . Thc dimension of this problem is then 882. As in the preceding comparisons we present in Figure 7.8 the number of function calls and the CPU time against the achieved accuracy. We uscd the tolerances $1 0 ^ { - 2 }$ ， $1 0 ^ { - 4 }$ ， $1 0 ^ { - 6 }$ for all methods except DEABM, where $1 0 ^ { 0 }$ ， $1 0 ^ { - 2 }$ $1 0 ^ { - 4 }$ was used. This was necessary duc to the different norms used in the codes. Comparing thc two pictures of Figurc 7.8， we see that the extrapolation code ODEX (Section II.9) uses the most func-tion evaluations, but has the smallest overhead, so that its CPU time is nearly comparable to that of DOPRI8.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/82b69e52d9c783a553ac31ce17179bdc8f05026c24576d2c1e396fd7a7779912.jpg)  
Figure 7.8. Function calls and CPU time for Problem (7.12) with $N = 2 1$

# III.8. General linear methods

Pf methods sufficiently general as to inchude linear multistep and Runge-Kuta methods as special cases.." (K. Burrage and J.C. Butcher, 1980)

In a remarkably short period (1964-1966) many independent papers appeared which tried to generalize either Runge-Kutta methods in the direction of multistep or multistep methods in the direction of RK. The motivation was either to make the advantages of multistep accessible to RK or to "break the Dahlquist barrier" by modifying the multistep formulas. "Generalized multistep methods" were introduced by Gragg and Stetter in (1964), "modified multistep methods" by Butcher (1965a), and in the same year there appeared the work of Gear (1965) on "hybrid methods". A year later Byrne and Lambert (1966) published their work on "pseudo Runge-Kutta methods". All these methods fall into the class of "general linear methods" to be discussed in this section.

An example of such a method is the following (Butcher (1965a), order 5)

$$
\begin{array} { r l r } {  { \hat { y } _ { n + 1 / 2 } = y _ { n - 1 } + \frac { h } { 8 } ( 9 f _ { n } + 3 f _ { n - 1 } ) } } & { \quad { \scriptstyle ( 8 } } \\ & { \quad \hat { y } _ { n + 1 } = \frac { 1 } { 5 } ( 2 8 y _ { n } - 2 3 y _ { n - 1 } ) + \frac { h } { 5 } ( 3 2 \hat { f } _ { n + 1 / 2 } - 6 0 f _ { n } - 2 6 f _ { n - 1 } ) } & \\ & { \quad { \scriptstyle y _ { n + 1 } = \frac { 1 } { 3 1 } ( 3 2 y _ { n } - y _ { n - 1 } ) + \frac { h } { 9 3 } ( 6 4 \hat { f } _ { n + 1 / 2 } + 1 5 \hat { f } _ { n + 1 } + 1 2 f _ { n } - f _ { n - 1 } ) } , } & \end{array}
$$

We now have the choice of developing a theory of "generalized" multistep methods or of developing a theory of "generalized" RK methods. After having seen in Section II.4 that the convergence theory becomes much nicer when multistep methods are interpreted as one-step methods in higher dimension, we choose the second possibility: since Formula (8.1) uses tion, we introduce the vector $\begin{array} { c }  { \begin{array} { r l } { { \scriptstyle 1 \mathbf { s } \mathbf { c } \mathbf { s } } } & { { \boldsymbol { y } _ { n } \quad \mathbf { a } \mathbf { u } \mathbf { u } \ : \ : y _ { n } } \\ { { \boldsymbol { u } _ { n } } = { \bigl ( } y _ { n } \ : , \ : y _ { n - 1 } { \bigr ) } ^ { T } } \end{array} } } \end{array}$ and $y _ { n , - 1 }$ so that the last line of as previous informa-(8.1) becomes

$$
\mathbf { \Sigma } _ { n } ^ { ( + 1 ) } \mathbf { \Sigma } = \left( \begin{array} { c c } { \displaystyle \frac { 3 2 } { 3 1 } } & { \displaystyle - \frac { 1 } { 3 1 } } \\ { \displaystyle 1 } & { 0 } \end{array} \right) \ \left( \begin{array} { c } { \displaystyle y _ { n } } \\ { \displaystyle y _ { n - 1 } } \end{array} \right) \ + \ \left( \begin{array} { c c c c } { \displaystyle \frac { 6 4 } { 9 3 } } & { \displaystyle \frac { 1 5 } { 9 3 } } & { \displaystyle \frac { 1 2 } { 9 3 } } & { \displaystyle - \frac { 1 } { 9 3 } } \\ { \displaystyle 0 } & { 0 } & { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c } { \displaystyle h f \left( \hat { y } _ { n + 1 / 2 } \right) } \\ { \displaystyle h f \left( \hat { y } _ { n + 1 } \right) } \\ { \displaystyle f \left( y _ { n } \right) } \\ { \displaystyle f \left( y _ { n - 1 } \right) } \end{array} \right)
$$

which is of the form

$$
u _ { n + 1 } = S u _ { n } + h \Phi ( x _ { n } , u _ { n } , h ) .
$$

Properties of such general methods have been investigated by Butcher (1966), Hairer-Wanner (1973), Skeel (1976),Cooper (1978) and others. Clearly， nothing prevents us from letting S and $\Phi$ be arbitrary, or from allowing also other interpretations of $u _ { n }$

We consider the system

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

where $f$ satisfies the regularity condition (4.2). Let $m$ be the dimension of the differential equation (8.3), $q \geq m$ be the dimension of the difference equation (8.2) and ${ x _ { n } } ^ { = } { x _ { 0 } } ^ { + } { n h }$ be the subdivision points of an equidistant grid. The methods under consideration consist of three parts:

(I) a forward step procedure, i.e. a formula (8.2)， where the square matrix S is independent of (8.3).   
(I) a correct value function $z \left( x , h \right)$ ， which gives an interpretation of the values $u _ { n } ; z _ { n } = z \left( x _ { n } , h \right)$ is to be approximated by $u _ { n }$ , so that the global error is given by $u _ { n } - z _ { n }$ . It is assumed that the exact solution $y \left( x \right)$ of (8.3) can be recovered from $z \left( x , h \right)$   
(III)a starting procedure $\Phi ( h )$ ， which specifies the starting value ${ { u } _ { 0 } } ^ { = } \Phi ( h ) . \ \Phi ( h )$ approximates ${ \boldsymbol { z } } _ { 0 } = { \boldsymbol { z } } \left( { \boldsymbol { x } } _ { 0 } , h \right)$

The discrete problem corresponding to (8.3) is thus given by

$$
\begin{array} { c } { { u _ { 0 } = \phi ( h ) ~ , } } \\ { { { } } } \\ { { u _ { n + 1 } = S u _ { n } + h \Phi ( x _ { n } , u _ { n } , h ) ~ , \qquad n = 0 , 1 , 2 , \dots , } } \end{array}
$$

which yields the numerical solution $u _ { 0 } , u _ { 1 } , u _ { 2 } , . . . .$ We remark that the increment function $\Phi ( u , x , h )$ ， the starting procedure $\Phi ( h )$ and the correct value function $z \left( x , h \right)$ depend on the differential equation (8.3), although this is not stated explicitly.

# Examples of method (8.4)

Example 8.1. The most simple cases are one-step methods. A characteristic feature of these is that the dimensions of the differential and difference equation are equal (i.e. $m = q$ ) and that S is the identity matrix. Furthermore, $\Phi ( h ) = y _ { 0 }$ and $z \left( x , h \right) { \stackrel { } { = } } y \left( x \right)$ . They have been investigated in Chapter II.

Example 8.2. We have seen in Section II.4 that linear multistep methods also fall into the class (8.4). For $k$ -step methods the dimension of the difference equation is $\scriptstyle q = k m$ and the forward step procedure is given by Form ula (4.8). A starting procedure yields the vector $\Phi ( h ) = ( y _ { k - 1 } , . . . , y _ { 1 } , y _ { 0 } ) ^ { T }$ and, finallyt crect ue fuction is given by $z \left( x , h \right) = \left( y \left( x + ( k - 1 ) h \right) , \ldots , y \left( x + h \right) , y \left( x \right) \right) ^ { T } ,$

The most common way of implementing an implicit multistep method is a predictor-corrector process (compare (1.10) and Section I11.7): an approximation y(0k to $y _ { n + k }$ is "predicted" by an explicit multistep method, say

$$
\begin{array} { r }  \begin{array} { c } { \alpha _ { k } ^ { p } y _ { n + k } ^ { ( 0 ) } + \alpha _ { k - 1 } ^ { p } y _ { n + k - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } ^ { p } y _ { n } } \\ { = h ( \ B { \subsetneq [ [object Object] ] { ] { } } } \end{array} } \end{array}
$$

and is then "corrected" (usually once or twice) by

$$
f _ { n + k } \colon = f ( x _ { n + k } , y _ { n + k } ^ { ( l - 1 ) } )
$$

$$
\begin{array} { r l } & { \mathfrak { a } _ { \vec { k } } y _ { n + k } ^ { ( l ) } + \mathfrak { a } _ { k - 1 } y _ { n + k - 1 } + \cdot \cdot \cdot + \mathfrak { a } _ { 0 } y _ { n } } \\ & { \qquad = h \big ( \mathfrak { \beta } _ { k } f _ { n + k } + \mathfrak { \beta } _ { k - 1 } f _ { n + k - 1 } + \cdot \cdot \cdot + \mathfrak { \beta } _ { 0 } f _ { n } \big ) . } \end{array}
$$

If the iteration (8.5) is carried out until convergence, the process is identical to that of Example 8.2. In practice, however, only a fixed number, say M，of iterations are carried out and the method is theoretically no longer a "pure" multistep method. We distinguish two predictor-corrector (PC) methods, depending on whether it ends with a correction (8.5;C) or not. The first algorithm is symbolized as $P \left( E C \right) ^ { M }$ andthesecond possbilty，whee $f _ { n + k }$ is once more updated by (8.5;E) for further use in the subsequent steps， as $\bar { P ( E C ) } ^ { M } E$ .We shall now see how these two procedures can be interpreted as Methods (8.4):

Example 8.2a. $P \left( E C \right) ^ { M } E$ -methods. The starting procedure and the correct value function are the same as for multistep methods and also $\scriptstyle q = k m$ . Furthermore we have ${ \cal { S } } = { \cal { A } } \otimes I$ ， where A is given by (4.7) and $\boldsymbol { l }$ is the $m$ -dimensional identity matrix. Observe that S depends only on the corrector-formula and not on the predictorformula. Here, the increment function is given by

$$
\Phi ( x , u , h ) = ( e _ { 1 } \otimes I ) \Psi ( x , u , h )
$$

with $\boldsymbol { e } _ { 1 } { = } ( 1 , 0 , \dots , 0 ) ^ { T } .$ For $\boldsymbol { \mathfrak { u } } = \left( \boldsymbol { \mathfrak { u } } ^ { 1 } , \dots , \boldsymbol { \mathfrak { u } } ^ { k } \right) ^ { T }$ with $u ^ { j } \in \mathbb { R } ^ { m }$ the fuction $\psi ( x , u , h )$ is defined by

$$
\begin{array} { r } { \psi ( x , u , h ) = \mathfrak { a } _ { k } ^ { - 1 } \bigg ( \beta _ { k } f \left( x + k h , y ^ { ( M ) } \right) \bigg . } \\ { \bigg . + \beta _ { k - 1 } f \left( x + ( k - 1 ) h , u ^ { 1 } \right) + \cdot \cdot \cdot + \beta _ { 0 } f \left( x , u ^ { k } \right) \bigg ) } \end{array}
$$

where the value $y ^ { ( M ) }$ is calculated from

$$
\begin{array} { l } { { \mathfrak { a } _ { k } ^ { p } y ^ { ( 0 ) } + \mathfrak { a } _ { k - 1 } ^ { p } u ^ { 1 } + \cdot \cdot \cdot + \mathfrak { a } _ { 0 } ^ { p } u ^ { k } } } \\ { { \ \qquad = h \left( \mathfrak { \beta } _ { k - 1 } ^ { p } f \left( x + ( k - 1 ) h , u ^ { 1 } \right) + \cdot \cdot \cdot + \mathfrak { \beta } _ { 0 } ^ { p } f \left( x , u ^ { k } \right) \right) } } \\ { { \mathfrak { a } _ { k } y ^ { ( l ) } + \mathfrak { a } _ { k - 1 } u ^ { 1 } + \cdot \cdot \cdot + \mathfrak { a _ { 0 } } u ^ { k } \ = h \left( \mathfrak { \beta } _ { k } f \left( x + k h , y ^ { ( l - 1 ) } \right) \right. } } \\ { { \ \qquad + \left. \mathfrak { \beta } _ { k - 1 } f \left( x + ( k - 1 ) h , u ^ { 1 } \right) + \cdot \cdot \cdot + \mathfrak { \beta } _ { 0 } f \left( x , u ^ { k } \right) \right) } } \\ { { \ \qquad \mathrm { ~ } } } \\ { { \mathrm { ~ } = \mathrm { ~ } } \mathcal { M } , } \\ { { \ \qquad \mathfrak { a } _ { k } \mathrm { ~ } . \mathrm { ~ } , \qquad g , W \mathrm { ~ } } } \end{array}
$$

( for l=

Example 8.2b. For $P \left( E C \right) ^ { M }$ -methods, the formulation as a method of type (8.4) becomes more complicated, since the information to be carried over to the next step is determined not only by Where $y _ { n - k + 1 } , \ldots , y _ { n }$ $h f _ { n + j } = h f ( x _ { n + j } , y _ { n + j } ^ { ( M - 1 ) } )$ , but also depends on the values Thereforethedimensionofthe difference equation becomes $q = 2 k m$ . A usual starting procedure (as for multistep methods) yields

$$
\phi ( h ) = \left( y _ { k - 1 } , \ldots , y _ { 0 } , h f \left( x _ { k - 1 } , y _ { k - 1 } \right) , \ldots , h f \left( x _ { 0 } , y _ { 0 } \right) \right) ^ { T } .
$$

If we define the correct value function by

$$
, h ) = \bigg ( y ( x + ( k - 1 ) h ) , \dots , y ( x ) , h y ^ { \prime } ( x + ( k - 1 ) \hbar ) , \dots , h y ^ { \prime } ( x ) \bigg ) ^ { T }
$$

the forward step procedure is given by

$$
\begin{array} { r l } { S } & { = \left( \begin{array} { c c c c c c } { A } & { 1 } & & & & \\ & { 1 } & & & & \\ & { 1 } & { 0 } & { 0 } & { . . } & { 0 } & \\ & { 1 } & { 1 } & { 0 } & { . . } & { 0 } & \\ & { 0 } & { 1 } & { 0 } & { . } & { 0 } & \\ & { 1 } & { 1 } & { : } & { : } & { : } \\ & { 1 } & { 0 } & { 0 } & { . } & { 1 } & { 0 } \end{array} \right) , \quad \Phi ( x , u , h ) } & { = \left( \begin{array} { c } { \beta _ { k } ^ { \prime } } \\ { 0 } \\ { 0 } \\ { - \frac { \xi } { 1 } - } \\ { 1 } \\ { 0 } \\ { 1 } \end{array} \right) \Psi ( x , u , h ) \ . } \end{array}
$$

Here A is the matrix given by (4.7) and $B$ is the $k$ -dimensional rank-one-matrix

$$
( 1 , 0 , . . . , 0 ) ( \mathsf { { B } } _ { k - 1 } ^ { \prime } , . . . , \mathsf { { B } } _ { 0 } ^ { \prime } ) ^ { T } \ , \quad \mathsf { { B } } _ { j } ^ { \prime } = \mathsf { { B } } _ { j } / \mathsf { { a } } _ { k } \ .
$$

For $\boldsymbol { u } = ( u ^ { 1 } , \dots , u ^ { k } , h \nu ^ { 1 } , \dots , h \nu ^ { k } )$ the function $\Psi ( x \ : , \ : u \ : , \ : h \ : ) \in \mathbb { R } ^ { q }$ is defined by

$$
\psi ( x , u , h ) = f ( x + k h , y ^ { ( M - 1 ) } )
$$

where $y ^ { ( M - 1 ) }$ is given by

$$
\alpha _ { k } ^ { p } y ^ { ( 0 ) } + \alpha _ { k - 1 } ^ { p } u ^ { 1 } + \cdot \cdot \cdot + \alpha _ { 0 } ^ { p } u ^ { k } = h ( \beta _ { k - 1 } ^ { p } \nu ^ { 1 } + \cdot \cdot \cdot + \beta _ { 0 } ^ { p } \nu ^ { k } )
$$

$$
\begin{array} { r l } & { \mathfrak { a } _ { k } y ^ { ( l ) } + \mathfrak { a } _ { k - 1 } \mu ^ { 1 } + \cdot \cdot \cdot + \mathfrak { a } _ { 0 } \mu ^ { k } } \\ & { \quad \quad = h \left( \mathfrak { \beta } _ { k } f \left( x + k h , y ^ { ( l - 1 ) } \right) + \mathfrak { \beta } _ { k - 1 } \nu ^ { 1 } + \cdot \cdot \cdot + \mathfrak { \beta } _ { 0 } \nu ^ { k } \right) . } \end{array}
$$

Again we observe that S depends only on the corrector-formula.

Example 8.3. Nordsieck methods are also of the form (8.4). This follows immediately from the representation (6.8). In this case the correct value function

$$
z ( x , h ) = \bigg ( y ( x ) , h y \prime ( x ) , \frac { h ^ { 2 } } { 2 ! } y ^ { \prime \prime } ( x ) , \ldots , \frac { h ^ { k } } { k ! } y ^ { ( k ) } ( x ) \bigg ) ^ { T }
$$

is not only composed of values of the exact solution, but also con-tains their derivatives.

Example 8.4. Cyclic multistep methods. Donelson and Hansen (1971) have investigated the possibility of basing a discretization scheme on several different $k$ -step methods which are used cyclically. Let $S _ { j }$ and $\Phi _ { j }$ represent the forward step procedure of the $j$ -th multi-step method; then the numerical solution $u _ { 0 } , u _ { 1 } , \ldots$ is defined by

$$
\begin{array} { r } { \begin{array} { r l } { u _ { 0 } = \phi ( h ) } \\ { u _ { n + 1 } = S _ { j } u _ { n } \ + h \Phi _ { j } ( x _ { n } , u _ { n } , h ) } \end{array} \quad \mathrm { i f } n = ( j - 1 ) { \bmod { m } } . } \end{array}
$$

In order to get a method (8.4) with S independent of the step number, we consider one cycle of the method as one step of a new method

$$
\begin{array} { r c l } { { } } & { { } } & { { } } \\ { { } } & { { } } & { { u _ { 0 } ^ { * } = \phi ( \displaystyle \frac { h ^ { * } } { m } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { u _ { n + 1 } ^ { * } = S u _ { n } ^ { * } + h ^ { * } \Phi ( x _ { n } ^ { * } , u _ { n } ^ { * } , h ^ { * } ) } } \end{array}
$$

with step size $h ^ { * } { = } m h$ . Here ${ x ^ { * } } _ { n } = { x _ { 0 } } ^ { + n h ^ { * } }$ ， $S = S _ { m } \cdots S _ { 2 } S _ { 1 }$ and $\Phi$ has to be chosen suitably. E.g. in the case $m = 2$ we have

$$
\begin{array} { l } { { \Phi ( x ^ { * } , u ^ { * } , h ^ { * } ) = \displaystyle \frac { 1 } { 2 } S _ { 2 } \Phi _ { 1 } ( x ^ { * } , u ^ { * } , \frac { h ^ { * } } { 2 } ) } } \\ { { + \displaystyle \frac { 1 } { 2 } \Phi _ { 2 } \Big ( x ^ { * } + \frac { h ^ { * } } { 2 } , S _ { 1 } u ^ { * } + \frac { h ^ { * } } { 2 } \Phi _ { 1 } ( x ^ { * } , u ^ { * } , \frac { h ^ { * } } { 2 } ) , \frac { h ^ { * } } { 2 } \Big ) ~ . } } \end{array}
$$

It is interesting to note that cyclically used $k$ -step methods can lead to convergent methods of order $2 k - 1$ (or even 2k ). The "first Dahlquist barrier" (Theorem 3.5) can be broken in this way. For more details see Stetter (1973) and Exercise 2.

Example 8.5. General linear methods.

Following the advice of Aristotle..." (the original Greek can be found in Butcher's paper) "... we look for the greatest good as a mean between extremes" (J.C. Butcher, 1985a)

Introduced by Burrage-Butcher (1980), these methods are general enough to include all previous examples as special cases, but at the same time the increment function is given explicitly in terms of the differential equation and several free parameters. They are defined by

$$
\begin{array} { l l } { { u _ { i } ^ { \left( n + 1 \right) } = \displaystyle \sum _ { j = 1 } ^ { k } a _ { i j } u _ { j } ^ { \left( n \right) } + h \sum _ { j = 1 } ^ { s } b _ { i j } f \left( x _ { n } + c _ { j } h , \nu _ { j } ^ { \left( n \right) } \right) } } & { { i = 1 , \dots , k \ , } } \\ { { \nu _ { i } ^ { \left( n \right) } = \displaystyle \sum _ { j = 1 } ^ { k } \tilde { a } _ { i j } u _ { j } ^ { \left( n \right) } + h \sum _ { j = 1 } ^ { s } \tilde { b } _ { i j } f \left( x _ { n } + c _ { j } h , \nu _ { j } ^ { \left( n \right) } \right) } } & { { i = 1 , \dots , s \ . } } \end{array}
$$

The stages $( \boldsymbol { u } _ { i } ^ { ( n ) }$ ， $i = 1 , \ldots , k$ )are called te exteral stagessince they contain all the necessary information from the previous step used in carrying out the current step. The stages $( \nu _ { i } ^ { ( n ) ^ { \scriptstyle r } } , i = 1 , . . . , s ) $ are the internal stages and do not leave the "black box" of the current step. Very often, some internal stages are identical to external ones, as for example in Method (8.1), where

$$
\nu _ { _ { n } } = ( \hat { y } _ { n + 1 / 2 } , \hat { y } _ { n + 1 } , y _ { _ { n } } , y _ { _ { n - 1 } } ) \ .
$$

One-step Runge-Kutta methods are characterized by $k = 1$ . At the end of this section we shall discuss the algebraic conditions for general linear methods to be of order $p$

Example 8.6. In order to ilustrate the fact that the analysis of this section is not only applicable to numerical methods that discretize first order differential equations, we consider the second order initial value problem

$$
y ^ { \prime \prime } = g \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } 
$$

which clearly can also be written as a first order system (8.3). Replacingy $^ { \prime \prime } ( x )$ by a central difference yields

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } g ( x _ { n } , y _ { n } ) ~ ,
$$

and with the additional variables

$$
h y _ { n } ^ { \prime } = y _ { n + 1 } - y _ { n }
$$

this method can be written as

$$
\begin{array}{c} \begin{array} { r c l } { { \left( y _ { n + 1 } \right) } } & { { = } } & { { \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) } } & { { \left( y _ { n } \right) } } \\ { { \left( y _ { n + 1 } ^ { \prime } \right) } } & { { = } } & { { \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right) } } & { { \left( y _ { n } \right) } } \end{array} + h \left( \begin{array} { c c } { { y _ { n } ^ { \prime } } } & { { } } \\ { { } } & { { } } \\ { { g \left( x _ { n + 1 } , y _ { n } + h y _ { n } ^ { \prime } \right) } } \end{array} \right)   \end{array} ~ .
$$

It now has the form of a method (8.4) with the correct value function $z \left( x , h \right) = ( y \left( x \right) , ( y \left( x + h \right) - y \left( x \right) ) / h ) ^ { T }$ Here $y \left( x \right)$ denotes the exact solution of (8.8).

Clearly, all Nystrom methods (Section I.13) fit into this framework, as do multistep methods for second order differential equations. They will be investigated in more detail in Section I1.10.

Example 8.7. Multi-step multi-stage multi-derivative methods seem to be the most general class of explicitly given linear methods and generalize the methods of Section II.12. In the notation of that section, we can write

$$
\begin{array} { r l } & { \boldsymbol { \mathfrak { n } } ^ { ( n + 1 ) } = \displaystyle \sum _ { j = 1 } ^ { k } a _ { i j } \boldsymbol { u } _ { j } ^ { ( n ) } + \displaystyle \sum _ { r = 1 } ^ { q } \frac { h ^ { r } } { r ! } \sum _ { j = 1 } ^ { s } b _ { i j } ^ { ( r ) } \boldsymbol { D } ^ { r } \boldsymbol { y } ( x _ { n } + c _ { j } h , \nu _ { j } ^ { ( n ) } ) \quad i = 1 , \dots , t } \\ & { \nu _ { i } ^ { ( n ) } = \displaystyle \sum _ { j = 1 } ^ { k } \tilde { a } _ { i j } \boldsymbol { u } _ { j } ^ { ( n ) } + \displaystyle \sum _ { r = 1 } ^ { q } \frac { h ^ { r } } { r ! } \sum _ { j = 1 } ^ { s } \tilde { b } _ { i j } ^ { ( r ) } \boldsymbol { D } ^ { r } \boldsymbol { y } ( x _ { n } + c _ { j } h , \nu _ { j } ^ { ( n ) } ) \quad i = 1 , \dots , t } \end{array}
$$

Such methods have been studied in Hairer-Wanner (1973).

# Stability and Order

The following study of stability， order and convergence follows mainly the lines of Skeel (1976). Stability of a numerical scheme just requires that for $h \to 0$ the numerical solution remain bounded. This motivates the following definition:

Definition 8.8. Method (8.4) is called stable if $S ^ { n }$ is uniformly bounded for all $n \geq 0$

The local error of Method (8.4) is defined in exactly the same way as for one-step methods (Section I.3) and multistep methods (Section III.2):

Definition 8.9. Let $z \left( x , h \right)$ be the correct value function for the method (8.4) and let ${ z } _ { n } = z \left( \boldsymbol { x } _ { n } , h \right)$ The local error is then given by (see Figure 8.1)

$$
\begin{array} { c } { { d _ { 0 } = z _ { 0 } - \Phi ( h ) } } \\ { { { } } } \\ { { d _ { n + 1 } = z _ { n + 1 } - S z _ { n } - h \Phi ( x _ { n } , z _ { n } , h ) ~ , \qquad n = 0 , 1 , . . . } } \end{array}
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0006_pages_0351-0420/auto/images/fcfc4ad0fc50598e57105898837698cd060c44f9b368d546c513d6a382cab4ed.jpg)  
Figure 8.1. Illustration of the local error

The definition of order is not as straightforward. The requirement that the local error be $\mathbf { O } ( h ^ { p + 1 } )$ (cf. one-step and multistep methods) will turn out to be sufficient but in general not necessary for convergence of order $p$ . For an appropriate definition we need the spectral decomposition of the matrix S .

First observe that, whenever the local error (8.9) tends to zero for $h \to 0$ （ $n h = x - x _ { 0 }$ fixed), we get

$$
0 = z ( x , 0 ) - S z ( x , 0 ) ,
$$

so that 1 is an eigenvalue of S and $z \left( x , 0 \right)$ a corresponding eigenvector. Furthermore, by stability， no eigenvalue of S can lie outside the unit disc and the eigenvalues of modulus one can not give rise to Jordan chains. Denoting the eigenvalues of modulus one by $\boldsymbol { \zeta } _ { 1 } \left( = 1 \right)$ ， $\boldsymbol { \zeta } _ { 2 } \mathrm { ~ , ~ . ~ . ~ . ~ , ~ } \boldsymbol { \zeta } _ { l } \mathrm { ~ , ~ }$ the Jordan canonical form of S (see (I.12.14)) is therefore the block diagonal matrix

$$
S = T \operatorname { d i a g } \{ \begin{array} { l l } { ( \begin{array} { l l l } { 1 } & & \\ & { \ddots } & \\ & & { 1 } \end{array} ) , } \\ & & { \qquad 1 } \end{array}  , ( \begin{array} { l l l } { \begin{array} { l l l } { \boldsymbol { \zeta } _ { 2 } } & & \\ & { \ddots } & \\ & & { \ddots } & \\ & & { \boldsymbol { \zeta } _ { 2 } } \end{array} ) , \ \ldots , ( \begin{array} { l l l } { \boldsymbol { \zeta } _ { l } } & & \\ & { \ddots } & \\ & & { \ddots } & \\ & & & { \boldsymbol { \zeta } _ { l } } \end{array} ) , \boldsymbol { \bar { J } } } \end{array} \} T ^ { - 1 } .
$$

If we decompose this matrix into the terms which correspond to the single eigenvalues we obtain

where

$$
\begin{array} { r l r } {  { S = E + \zeta _ { 2 } E _ { 2 } + \cdots + \zeta _ { l } E _ { l } + \tilde { E } } } \\ & { } & \\ & { E = T \ \mathrm { d i a g } \{ I , 0 , 0 , \cdots \} T ^ { - 1 } , } \\ & { } & \\ & { E _ { 2 } = T \ \mathrm { d i a g } \{ 0 , I , 0 , \cdots \} T ^ { - 1 } , } \\ & { } & \\ & { } & { \quad \cdots , } \end{array}
$$

$$
\tilde { E } \ = T \ \mathrm { d i a g } \Big \{ 0 , 0 , 0 , \cdots , \tilde { J } \Big \} \ T ^ { - 1 } \ .
$$

We are now prepared to give

Definition 8.10. The method (8.4) is of order $p$ (consistent of order $p$ ), if for all problems (8.3) with $p$ times continuously differentiable $f$ , the local error satisfies

$$
\begin{array} { c c } { { d _ { 0 } { = } { \bf { O } } ( h ^ { p } ) } } &   ( 8 \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm   \end{array}
$$

Remark. This property is called quasi-consistency of order $p$ by Skeel (1976).

If the right-hand side of the differential equation (8.3) is $\boldsymbol { p }$ -times continuously differentiable then, in general, $\Phi ( h )$ ， $\Phi ( x , u , h )$ and $z \left( x , h \right)$ are also smooth, so that the local error (8.9) can be expanded into a Taylor series in $h$ ：

$$
\begin{array} { c } { { d _ { 0 } = \gamma _ { 0 } + \gamma _ { 1 } h + \cdot \cdot \cdot + \gamma _ { p - 1 } h ^ { p - 1 } + { \bf O } ( h ^ { p } ) } } \\ { { d _ { n + 1 } = d _ { 0 } ( x _ { n } ) + d _ { 1 } ( x _ { n } ) h + \cdot \cdot \cdot + d _ { p } ( x _ { n } ) h ^ { p } + { \bf O } ( h ^ { p + 1 } ) . } } \end{array}
$$

The function $d _ { j } ( \boldsymbol { x } )$ is then $( p - j + 1 )$ -times continuously differentiable. The following lem ma gives a more practical characterization of the order of the methods (8.4).

Lemma 8.11. Assume that the local eror of Method (8.4) satisfies (8.14） with continuous $d _ { j } ( \boldsymbol { x } )$ .The method is then of order $\boldsymbol { p }$ ,if and onty if

$$
d _ { n } \ = { \bf O } ( h ^ { p } ) f o r 0 { \le } n h { \le } c o n s t , a n d E d _ { p } ( x ) \ = 0 \ ,
$$

Proof: The condition (8.15) is equivalent to

$$
d _ { n } = { \bf O } ( h ^ { p } ) , { \cal E } d _ { n + 1 } = { \bf O } ( h ^ { p + 1 } ) { \mathrm { f o r } } 0 \leq n h \leq c o n s t ,
$$

which is clearly sufficient for order $p$ . We now show that (8.16) is also necessary. Since $E ^ { 2 } { = } E$ (see (8.12)) order $p$ im plies

$$
d _ { n } = \mathbf { O } { \left( h ^ { p } \right) } , E \left( d _ { 1 } + \cdot \cdot \cdot + d _ { n } \right) = \mathbf { O } { \left( h ^ { p } \right) } { \mathrm { f o r ~ } } 0 { \le } n h { \le } c o n s t .
$$

This is best seen by multiplying (8.13) by $E$ . Consider now pairs $( n , h )$ such that $n h = x - x _ { 0 }$ for some fixed $x$ . We insert (8.14) (observe that $d _ { n } = \mathbf { O } ( h ^ { p } ) )$ into $E \left( d _ { 1 } + \cdots + d _ { n } \right)$ and approximate the resulting sum by the corresponding Riemann integral

$$
\begin{array} { r } { E ( d _ { 1 } + \cdot \cdot \cdot + d _ { n } ) = h ^ { p } E \sum _ { j = 1 } ^ { n } d _ { p } ( x _ { j - 1 } ) + 0 ( h ^ { p } ) } \\ { = h ^ { p - 1 } E \int d _ { p } ( s ) d s + 0 ( h ^ { p } ) ~ . } \\ { x _ { 0 } } \end{array}
$$

It follows from (8.17) that $E \int d _ { p } { \big ( } s { \big ) } d s = 0$ and by differentiation that $E d _ { p } ( x ) = 0 .$ QED. x0

# Convergence

In addition to the numerical solution given by (8.4) we consider a perturbed numerical solution ( $a _ { n }$ ) defined by

$$
\begin{array} { r l } { \quad \hat { a } _ { 0 } = \phi ( h ) + r _ { 0 } } & { { } \quad ( \qquad \mathrm { ~ a ~ n ~ d ~ } ) = \qquad \quad } \\ { \hat { u } _ { n + 1 } = s \hat { u } _ { n } + h \Phi ( x _ { n } , \hat { u } _ { n } , h ) + r _ { n + 1 } , } & { { } \quad n = 0 , 1 , \dots , N - 1 } \end{array}
$$

for some perturbation $R = ( r _ { 0 } , r _ { 1 } , \ldots , r _ { N } )$ . For example, the "exact" solution ${ z _ { n } } = z \left( { { x } _ { n } } , h \right)$ can be interpreted as a perturbed solution, where the perturbation is just the local error. The following lemma gives the best possible qualitative bound on the difference ${ u _ { n } } - \hat { u } _ { n }$ in terms of the perturbation $R$ . We have to assume that the increment function $\Phi ( x , u , h )$ satisfies a Lipschitz condition with respect to u (on a com pact neighbourhood of the solution). This is the case for all reasonable methods.

Lemma 8.12. Lel the method (8.4) be stable and assume the sequences $\left( u _ { n } \right)$ and $\left( \hat { u } _ { \pi } \right)$ are given by (8.4) and (8.18), respectively. Then there exist positive constants $c$ and $C$ such that for any perturbation R and for $h N \leq C o n s t$

$$
\boldsymbol { c } \parallel \boldsymbol { R } \parallel _ { \mathcal { S } } \leq \operatorname* { m a x } _ { 0 \leq n \leq N } \parallel \boldsymbol { u } _ { n } - \boldsymbol { \hat { u } } _ { n } \parallel \leq \boldsymbol { C } \parallel \boldsymbol { R } \parallel _ { \mathcal { S } }
$$

wuh

$$
\parallel R \parallel _ { S } = \underset { 0 \leq n \leq N } { \operatorname* { m a x } } \parallel \sum _ { j = 0 } ^ { n } S ^ { n - j } r _ { j } \parallel .
$$

Remark. ${ \parallel } R { \parallel } _ { S }$ is a norm on $\mathbb { R } ^ { ( N + 1 ) q }$ . Its positivity is seen as follows: if $\parallel \boldsymbol { R } \parallel _ { \boldsymbol { S } } = 0$ then for $n = 0 , 1 , 2 , \ldots$ one obtains $r _ { 0 } { = } 0 , r _ { 1 } { = } 0$ ， etc. recursively.

Proof: Set $\delta _ { n } { = } \hat { u } _ { n } { - } u _ { n }$ Then

$$
\tilde { 8 } _ { n + 1 } = S \tilde { 8 } _ { n } + h \tilde { 8 } _ { n } + r _ { n + 1 }
$$

where

$$
\tilde { \tilde { \boldsymbol { \ v } } } _ { n } \ = \ \Phi ( \boldsymbol { x } _ { n } , \boldsymbol { \hat { u } } _ { n } , \boldsymbol { h } ) \ - \ \Phi ( \boldsymbol { x } _ { n } , \boldsymbol { u } _ { n } , \boldsymbol { h } ) \ ,
$$

Byassumptionthereexistsa constant $L$ such that $\lVert { \widetilde { \ \delta } } _ { n } \rVert \ \leq \ L { \widetilde { \ \parallel } } \ \delta _ { n } \parallel \ .$ Solving the difference equation (8.19) gives $\mathfrak { s } _ { 0 } = \mathfrak { r } _ { 0 }$ and

$$
\mathbb { S } _ { n + 1 } = \sum _ { j = 0 } ^ { n } \mathbb { S } ^ { n - j } h \tilde { \mathbb { S } } _ { j } + \sum _ { j = 0 } ^ { n + 1 } \mathbb { S } ^ { n + 1 - j } r _ { j } \mathrm { ~ . ~ }
$$

By stability there exists a constant $B$ such that

$$
\begin{array} { r } { \mathrm { ~  ~ { ~ \vert ~ \vert ~ } ~ } S ^ { ^ n } \mathrm { ~  ~ { \vert ~ \vert ~ } ~ } L \ \le \ B \qquad \mathrm { ~ f o r ~ ~ a l l ~ } n \ge 0 \ . } \end{array}
$$

Thus (8.20) becomes

$$
\Vert \ \delta _ { n + 1 } \Vert \ \leq \ h B \sum _ { j = 0 } ^ { n } \Vert \ \delta _ { j } \Vert \ + \ \Vert \ R \Vert _ { \textit { S } } \ .
$$

By induction on n it follows that

$$
\left| \left| ~ \mathfrak { d } _ { n } ~ \right| \right| ~ \leq ~ \left( 1 + h B ~ \right) ^ { n } \left\{ \left| ~ R ~ \right| \right| _ { S } ~ \leq ~ \exp ( C o n s t \cdot B ~ ) \left. \left| ~ R ~ \right| \right| _ { S } ~ , ~
$$

which proves the second inequality in the lemma. From (8.20) and (8.21)

$$
\big | \bigstar \sum _ { j = 0 } ^ { n } S ^ { n - j } r _ { j } \big | \bigstar \ \le \ \big ( 1 + n h B \big ) \operatorname* { m a x } _ { 0 \le n \le N } \big | \bigstar \vartheta _ { n } \big | \big | \quad ,
$$

and we thus obtain for Nh ≤ Const

$$
\begin{array} { r } { \left| \left| \begin{array} { l } { R } \end{array} \right| \right| _ { S } \leq \left( 1 + C o n s t { \cdot } B \right) \displaystyle \operatorname* { m a x } _ { 0 \leq n \leq N } \left| \left| \begin{array} { l } { a _ { n } - u _ { n } } \end{array} \right| \right| . } \end{array}
$$

QED.

Remark. A norm, such as $| | \mathbf { \nabla } \cdot | | _ { \mathbf { \nabla } S }$ , which permits an upper and a lower bound on $\operatorname* { m a x } { | | \textbf { \em u } _ { n } - \boldsymbol { \hat { u } } _ { n } \ | | }$ in terms of the perturbation, is said to be a minimal stability functional for the method. These ideas are discussed in more detail by Spijker (1971) and Stetter (1973, pp.81-84).

Using the lemma above we can prove

Theorem 8.13. Consider a stable method (8.4) and assume that the local error satisfies (8.14) with $d _ { p } ( x )$ continuousty differentiable. The method is then convergent of order p,i.e. the global error $u _ { n } - z _ { n }$ satisfies

$$
u _ { n } \ - z _ { n } \ = 0 ( h ^ { p } ) \qquad f o r 0 { \le } n h { \le } C o n s t ,
$$

if and onty if it is consistent of order p.

Proof: The identity

$$
E ( d _ { 0 } + \cdot \cdot \cdot + d _ { n } ) + d _ { n + 1 } = \sum _ { j = 0 } ^ { n + 1 } s ^ { n + 1 - j } d _ { j } - ( S - E ) \sum _ { j = 0 } ^ { n } s ^ { n - j } d _ { j } \ ,
$$

which is a consequence of $E S = E$ (see (8.11) and (8.12)), implies that for $n \leq N - 1$ and $D = ( d _ { 0 } , \ldots , d _ { N }$

$$
\begin{array} { r } { \left| \left| \begin{array} { l } { E \left( d _ { 0 } + \cdot \cdot \cdot + d _ { n } \right) + d _ { n + 1 } } \right| \right| \ \leq \ \left( 1 + \left| \right| \ S - E \left| \right| \ \right) \left| \left| \begin{array} { l } { D } \end{array} \right| \right| _ { S } \ . } \end{array} \end{array}
$$

The lower bound of Lemma 8.12, with $r _ { n }$ and ${ \hat { u } } _ { n }$ replaced by $d _ { n }$ and $z _ { n }$ respectively, yields the "only if"-part of the theorem.

For the "if"-part we use the upper bound of Lemma 8.12. We have to show that consistency of order $\boldsymbol { p }$ im plies

$$
\operatorname* { m a x } _ { 0 \leq n \leq N } \big | \big | \sum _ { j = 0 } ^ { n } S ^ { n - j } d _ { j } \big | \big | \ = { \bf O } \big ( h ^ { p } \big ) \ .
$$

By (8.11) and (8.12) we have

$$
S ^ { n - j } = E + \xi _ { 2 } ^ { n - j } E _ { 2 } + \cdot \cdot \cdot + \zeta _ { l } ^ { n - j } E _ { l } + \bar { E } ^ { n - j } \ .
$$

This identity together with Lem ma 8.11 im plies

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 0 } ^ { n } S ^ { n - j } d _ { j } = h ^ { p } E _ { 2 } \sum _ { j = 1 } ^ { n } \zeta _ { 2 } ^ { n - j } d _ { p } ( x _ { j - 1 } ) + \cdots } } \\ { { \qquad + h ^ { p } E _ { l } \sum _ { j = 1 } ^ { n } \zeta _ { l } ^ { n - j } d _ { p } ( x _ { j - 1 } ) + \sum _ { j = 0 } ^ { n } \tilde { E } ^ { n - j } d _ { j } + \mathbf { O } ( h ^ { p } ) } . } \end{array}
$$

The last term in this expression is $\mathbf { O } ( h ^ { P } )$ since in a suitable norm $\left| \left\{ \begin{array} { l l } { \mathcal { E } \ \right| \ < 1 } \end{array} \right.$ and therefore

$$
\big | \bigtriangledown \sum _ { j = 0 } ^ { n } \tilde { E } ^ { n - j } d _ { j } \bigm | \bigm | \ \leq \ \sum _ { j = 0 } ^ { n } \big \Vert \tilde { E } \bigm \Vert ^ { n - j } \bigm \Vert d _ { j } \bigm \Vert \ \leq \ \frac { 1 } { 1 - \big \Vert \tilde { E } \bigm \Vert } \cdot \operatorname* { m a x } _ { 0 \leq n \leq N } \bigm \Vert d _ { n } \bigm \Vert
$$

The rest follows from the fact that $\sum _ { j = 1 } ^ { n } \zeta ^ { n - j } d ( x _ { j - 1 } )$ is uniformly bounded in $n$ ,whenever $\mid \zeta \mid = 1 , \ \zeta \neq 1$ and $\dot { d }$ is of bounded variation. This can best be seen by partial summation (Abel (1826)):

$$
\sum _ { j = 1 } ^ { n } \zeta ^ { n - j } d ( x _ { j - 1 } ) = { \frac { 1 - \zeta ^ { n } } { 1 - \zeta } } \cdot d ( x _ { 0 } ) + \sum _ { j = 1 } ^ { n } { \frac { 1 - \zeta ^ { n - j } } { 1 - \zeta } } \cdot \left( d ( x _ { j } ) - d ( x _ { j - 1 } ) \right)
$$

QED.

# Order conditions for general linear methods

For the construction of a $\boldsymbol { p }$ -th order general linear method (8.7) the conditions (8.15) are still not very practical. One would like to have instead algebraic conditions in the free parameters, as is the case for Runge-Kutta methods. We shall demonstrate how this can be achieved using the theory of B-series of Section II.11 (see also Burrage-Moss, 1980). In order to avoid tensor products we assume in what follows that the differential equation under consideration is a scalar one. All results, however, are also valid for systems. We further assume the differential equation to be autonomous, so that the theory of Section I1.11 is directly applicable. This will be justified in Remark 8.17 below.

Suppose now that the components of the correct value function $z \left( x , h \right) = ( \boldsymbol { z } _ { 1 } ( x , h ) , . . . , \boldsymbol { z } _ { k } \left( x , h \right) ) ^ { T }$ possess an expansion as a B-series

$$
z _ { i } ( x , h ) = B \left( \tau _ { i } , y \left( x \right) \right)
$$

so that with ${ \boldsymbol { \pi } } ( t ) = \left( \mathbf { z } _ { 1 } ( t ) , \ldots , \mathbf { z } _ { k } ( t ) \right) ^ { T } ,$

$$
z ( x , h ) = \pmb { \mathrm { z } } ( \emptyset ) y ( x ) + h \pmb { \mathrm { z } } ( \tau ) f \left( y ( x ) \right) + \cdot \cdot \cdot .
$$

Before deriving the order conditions we observe that (8.7b) makes sense only if defined. Since $\bar { \nu } _ { j } ^ { ( n ) } { } _ {  } \ : y ( x _ { n } )$ $u _ { i } ^ { \phantom { \dagger } J }$ is an approximation of for $h  0$ Otherwise $z _ { j } ( x _ { n } , h )$ $f ( \nu _ { j } ^ { ( n ) } )$ ,this leads to the may not be condition $\Sigma \tilde { a } _ { i j } \tilde { \pmb { x } } _ { j } ( \mathcal { D } ) = 1$ . This together with (8.10) are the so-called preconsistency conditions:

$$
A \mathbf { z } ( \mathcal { D } ) = \mathbf { z } ( \mathcal { D } ) , \qquad \hat { A } \mathbf { z } \left( \mathcal { D } \right) = e \mathbf { \varepsilon } .
$$

A and A are the matrices with entries $\ e = \left( 1 \ , \ldots , 1 \right) ^ { T }$ Recall that thelocal error (8.9)for the general linear and $\hat { a } _ { i j }$ , respectively, and method (8.7) is given by

$$
d _ { i } ^ { ( n + 1 ) } = z _ { i } ( x _ { n } + h , h ) - \sum _ { j = 1 } ^ { k } a _ { i j } z _ { j } ( x _ { n } , h ) - \sum _ { j = 1 } ^ { s } b _ { i j } h f ( \nu _ { j } )
$$

where

$$
\nu _ { i } = \sum _ { j = 1 } ^ { k } \widetilde { a } _ { i j } z _ { j } ( x _ { n } , h ) + \sum _ { j = 1 } ^ { s } \widetilde { b } _ { i j } h f ( \nu _ { j } ) .
$$

For the derivation of the order conditions we write $\nu _ { i }$ and $d _ { i } ^ { ( n + 1 ) }$ as B-series

$$
\nu _ { i } = B ( { \bf v } _ { i } , y ( x _ { n } ) ) , d _ { i } ^ { ( n + 1 ) } = B ( { \bf d } _ { i } , y ( x _ { n } ) ) \ .
$$

By the composition theorem for B-series and by Formula (11.10) of Section II.11 we have

$$
\begin{array} { l } { { z _ { i } \left( x _ { n } + h , h \right) = B \left( { \bf z } _ { i } , y \left( x _ { n } + h \right) \right) = B \left( { \bf z } _ { i } , B \left( { \bf p } , y \left( x _ { n } \right) \right) \right) = } } \\ { { \qquad = B \left( { \bf p } { \bf z } _ { i } , y \left( x _ { n } \right) \right) . } } \end{array}
$$

Inserting all these series into (8.26) and comparing the coeficients we arrive at

$$
{ \bf d } _ { i } ( t ) = ( \mathtt { p } \mathtt { z } _ { i } ) ( t ) - \sum _ { j = 1 } ^ { k } a _ { i j } \mathtt { z } _ { j } ( t ) - \sum _ { j = 1 } ^ { s } b _ { i j } \mathtt { v } _ { j } ^ { \prime } ( t )
$$

$$
\mathbf { v } _ { i } ( t ) = \sum _ { j = 1 } ^ { k } \widetilde { a } _ { i j }  { \mathbf { z } } _ { j } ( t ) + \sum _ { j = 1 } ^ { s } \widetilde { b } _ { i j }  { \mathbf { v } } _ { j } ^ { \prime } ( t ) .
$$

An application of Lemma 8.11 now yields

Theorem 8.14. Let $\mathbf { d } ( t ) = ( \mathbf { d } _ { 1 } ( t ) , \dots , \mathbf { d } _ { r } ( t ) ) ^ { T }$ with ${ \bf d } _ { i } ( t )$ given by (8.27). The general linear method (8.7) is of order $\boldsymbol { p }$

$$
\begin{array} { r l } { \mathbf { d } ( t ) ~ = 0 } & { \qquad f o r \quad t \in T ~ , \mathsf { p } ( t ) { \le } p ^ { - 1 } } \\ { E \mathbf { d } ( t ) ~ = 0 } & { \qquad f o r \quad t \in T ~ , \mathsf { p } ( t ) { = } p ~ . } \end{array}
$$

(The matrix $\mathcal { E }$ is defined in (8.12)). NED.

Corollary 8.15. Sufficient conditions for the general linear method to be of order $p$ are

$$
{ \bf d } ( t ) = 0 \qquad f o r \quad t \in T , \ p ( t ) \le p .
$$

NED.

Remark 8.16. The expression $( \mathbb { P } \mathbb { Z } _ { i } ) ( t )$ in (8.27) can be computed using Formula (11.8) of Section I1.11. Since $\textstyle | ( t ) = 1$ for all trees t, we have

$$
( \mathbf { p z } _ { i } ) ( t ) = \sum _ { j = 1 } ^ { \mathsf { p } ( t ) } { \binom { \mathsf { p } ( t ) } { j } } \frac { 1 } { \alpha ( t ) } \sum _ { \mathrm { a l l ~ l a b e l l i n g s } } \mathbf { z } _ { i } ( s _ { j } ( t ) ) \ ,
$$

This rather complicated formula simplifies considerably if we assume that the coefficients $\boldsymbol { \mathscr { z } } _ { i } ( t )$ of the correct value function depend only on the order of t, i.e. that

$$
\begin{array} { r } { \mathrm { \bf ~ z } _ { i } ( t ) = \mathrm { \bf ~ z } _ { i } ( u ) \qquad \mathrm { w h e n e v e r } \quad \mathrm { \bf ~ \mathrm { \bf ~ \mathsf { p } } } ( t ) = \mathrm { \bf ~ \mathrm { \bf ~ \mathrm { p } } } ( u ) \ , } \end{array}
$$

In this case Formula (8.30) becomes

$$
( \mathbf { p } { \mathbf { z } _ { i } } ) ( t ) = \sum _ { j = 1 } ^ { \mathsf { p } ( t ) } { \binom { \mathsf { p } ( t ) } { j } } { \mathbf { z } _ { i } } ( \tau ^ { j } ) ~ .
$$

Here $\tau ^ { j }$ represents some tree of order j, e.g.

$$
\tau ^ { j } = [ \underbrace { \tau , \dots , \tau } _ { j - 1 } ] , \qquad \tau ^ { 1 } = \tau , \qquad \tau ^ { 0 } = \emptyset .
$$

Usually the components of $z \left( x , h \right)$ are com posed of $y \left( x \right)$ ， $y \left( x + j h \right)$ ， $h y \prime ( x ) , h ^ { 2 } y \prime \prime ( x ) , . . . ,$ in which case assumption (8.31) is satisfied.

Remark 8.17. Let us show how the $c _ { i }$ in (8.7) have to be defined in order that the above results, derived for autonomous systems,are also valid in the general case. For the differential equation $x \ ^ { \prime } { = } 1$ Formula (8.7b) becomes

$$
\nu _ { _ { R } } \ = \tilde { A } u _ { _ { R } } \ + h \tilde { B } e .
$$

Assuming that $x ^ { \prime } { = } 1$ is integrated exactly, i.e. $u _ { n } = z ( \ O ( \ O ) x _ { n } + h z ( \tau )$ we obtain $\nu _ { n } = x _ { n } e + h c$ ,where $c = ( c _ { 1 } , \ldots , c _ { s } ) ^ { T }$ is given by

$$
c = \tilde { A } z ( \tau ) + \tilde { B } e .
$$

This definition of the $c _ { i }$ implies that the numerical results for $y ^ { \prime } { = } f \left( x ~ , ~ y \right)$ and for the augmented, autonomous differential equation are the same.

We finally present in Table 8.1 the order conditions up to order 3 (under the assumption (8.31)). Remark that (8.25) is always assumed and that c is given by (8.34). Further $c ^ { j }$ denotes the vector $( c _ { 1 } ^ { j } , \ldots , c _ { s } ^ { j } ) ^ { T }$

Table 8.1. Order conditions for general linear methods   

<table><tr><td>0</td><td>p(1）</td><td>order condition</td></tr><tr><td>T</td><td>1</td><td>Az(t)+Be = z(t)+z(O)</td></tr><tr><td>。2 T</td><td>2</td><td>Az(τ²)+2Bc = z(τ²)+2z(τ)+z(O)</td></tr><tr><td></td><td>3</td><td>Az(t³)+3Bc² = z(t3)+3z(T²)+3z(T)+z(O)</td></tr><tr><td>[r2]</td><td>3</td><td>Az(T³)+3Bν(T²) = z(T³)+3z(T²)+3z(T)+z(O) with ν(τ²) = Az(T²)+2Be</td></tr></table>

# Construction of general linear methods

Let us demonstrate on an example how low order methods can be constructed: we set $k = s = 2$ and fix the correct value function as

$$
z \left( x , h \right) = \left( y \left( x \right) , y \left( x - h \right) \right) ^ { T } \ .
$$

This choice satisfies (8.24) and (8.31) with

$$
z ( \emptyset ) = { \binom { 1 } { 1 } } \ , \quad z ( \tau ) = { \binom { 0 } { - 1 } } \ , \quad z ( \tau ^ { 2 } ) = { \binom { 0 } { 1 } } \ , \cdot \cdot \cdot .
$$

Since the second component of $z \left( x + h , h \right)$ is equal to the first com-ponent of $z \left( x , h \right)$ , it is natural to look for methods with

$$
A \ = \ \left( \begin{array} { c c } { { a _ { 1 1 } } } & { { a _ { 1 2 } } } \\ { { } } & { { } } \\ { { 1 } } & { { 0 } } \end{array} \right) \ , \qquad B \ = \ \left( \begin{array} { c c } { { b _ { 1 1 } } } & { { b _ { 1 2 } } } \\ { { } } & { { } } \\ { { 0 } } & { { 0 } } \end{array} \right) \ .
$$

We further impose

$$
\begin{array} { r l r } { \tilde { B } } & { { } = } & { \left( \begin{array} { c c } { 0 } & { 0 } \\ { \tilde { b } _ { 2 1 } } & { 0 } \end{array} \right) } \end{array}
$$

so that the resulting method is explicit .

The preconsistency condition (8.25)， Formula (8.34) and the order conditions of Table 8.1 yield the following equations to be solved:

$$
\begin{array} { r l } & { a _ { 1 1 } + a _ { 1 2 } = 1 } \\ & { \quad a _ { 1 1 } + \bar { a } _ { 1 2 } = 1 , \quad \quad \bar { a } _ { 2 1 } + \bar { a } _ { 2 2 } = 1 } \\ & { \quad c _ { 1 } = - \bar { a } _ { 1 2 } , \quad \quad c _ { 2 } = \bar { b } _ { 2 1 } - \bar { a } _ { 2 2 } } \\ & { \quad - a _ { 1 2 } + b _ { 1 1 } + b _ { 1 2 } = 1 } \\ & { \quad a _ { 1 2 } + 2 ( b _ { 1 1 } c _ { 1 } + b _ { 1 2 } c _ { 2 } ) = 1 } \\ & { \quad - a _ { 1 2 } + 3 ( b _ { 1 1 } c _ { 1 } ^ { 2 } + b _ { 1 2 } c _ { 2 } ^ { 2 } ) = 1 } \\ & { \quad - a _ { 1 2 } + 3 \left( b _ { 1 1 } \bar { a } _ { 1 2 } + b _ { 1 2 } ( \bar { a } _ { 2 2 } + 2 \bar { b } _ { 2 1 } c _ { 1 } ) \right) = 1 . } \end{array}
$$

These are 9 equations in 11 unknowns. Letting $c _ { 1 }$ and $c _ { 2 }$ be free parameters, we obtain the solution in the following way: compute $a _ { 1 2 } , b _ { 1 1 }$ and $b _ { 1 2 }$ from the linear system (8.35d,e,f)，then ${ \tilde { a } } _ { 1 2 } , { \tilde { a } } _ { 2 2 }$ and $b _ { 2 1 }$ from (8.35c,g) and finally $a _ { 1 1 }$ $\tilde { a } _ { 1 1 }$ and $\tilde { a } _ { 2 1 }$ from (8.35a,b).

A particular solution for $c _ { 1 } { = } 1 / 2$ ， $c _ { 2 } = - 2 / 5$ is:

$$
\begin{array} { r c l } { { A } } & { { = } } & { { \left( \begin{array} { c c } { { 1 6 / 1 1 } } & { { - 5 / 1 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) ~ , ~ B } } & { { = } } & { { \left( \begin{array} { c c } { { 1 0 4 / 9 9 } } & { { - 5 0 / 9 9 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ~ , } } \\ { { \tilde { A } } } & { { = } } & { { \left( \begin{array} { c c } { { 3 / 2 } } & { { - 1 / 2 } } \\ { { 3 / 2 } } & { { - 1 / 2 } } \end{array} \right) ~ , ~ \tilde { B } } } & { { = } } & { { \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { - 9 / 1 0 } } & { { 0 } } \end{array} \right) ~ . } } \end{array}
$$

This method, which represents a stable explicit 2-step, 2-stage method of order 3, is due to Butcher (1984).

The construction of higher order methods soon becomes very complicated, and the use of simplifying assumptions will be very helpful:

Theorem 8.18. Assume that the correct value function satisfies (8.31). The simplifying assumptions

$$
\bar { A } \ : { \pi ( { \tau } ^ { j } ) } \ : + \ : j \ : \ : \tilde { B } c ^ { j - 1 } = c ^ { j } \ : \ : \qquad \ : j = 1 , \ldots , p - 1
$$

together with the preconsistency relations (8.25) and the order conditions for the "bushy trees"

$$
\mathbf { d } ( \tau ^ { j } ) = 0 \qquad j = 1 , \ldots , p
$$

imply that the method (8.7) is of order p.

Proof: An induction argument based on (8.27) implies that

$$
\mathbf { v } ( t ) = \mathbf { v } ( \tau ^ { j } ) \qquad \mathrm { f o r } \quad \mathsf { p } ( t ) = j , \quad j = 1 , \hdots , p - 1
$$

and consequently also

$$
{ \mathsf { d } } ( t ) = { \mathsf { d } } ( { \mathsf { \tau } } ^ { j } ) \qquad { \mathsf { f o r } } \quad { \mathsf { p } } ( t ) = j , \qquad j = 1 , \ldots , p \ .
$$

QED.

The simplifying assumptions (8.37) allow an interesting interpretation: they are equivalent to the fact that the internal stages $\nu _ { 1 } ^ { ( n ) }$ approximate the exact solution at $\boldsymbol { x } _ { n } + \boldsymbol { c } _ { i } h$ up to order $p - 1$ , i.e. that

$$
\nu _ { i } ^ { ( n ) } - y ( x _ { n } + c _ { i } h ) = \mathbf { O } ( h ^ { p } ) ~ .
$$

In the case of Runge-Kutta methods (8.37) reduces to the conditions (7.12) of Section II.7.

For further examples of general linear methods satisfying (8.37) we refer to Burrage-Moss (1980) and Butcher (1981). See also the more recent papers Burrage (1985) and Butcher (1985a).

# Exercises

1. Consider the composition of (cf. Example 8.5)

a) explicit and implicit Euler method;   
b) implicit and explicit Euler method.

To which methods are they equivalent? What is the order of the composite methods?

2. a) Suppose that each of the m multistep methods $( \boldsymbol \rho _ { i } , \boldsymbol \sigma _ { i } )$ $i = 1 , \ldots , m$ is of order $\boldsymbol { p }$ . Prove that the corresponding cyclic method is of order at least $p$ ·

b) Construct a stable, 2-cyclic, 3-steps linear multistep method of order $5 :$ find first a one-parameter family of linear 3-step methods of order 5 (which are necessarily unstable).

Result.

$$
\begin{array} { c } { { \displaystyle { \mathfrak { p } } _ { c } ( \zeta ) = c \zeta ^ { 3 } + ( { \frac { 1 9 } { 3 0 } } - c ) \zeta ^ { 2 } - ( { \frac { 8 } { 3 0 } } + c ) \zeta + ( c - { \frac { 1 1 } { 3 0 } } ) } } \\ { { \langle \zeta \rangle = ( { \frac { 1 } { 9 } } - { \frac { c } { 3 } } ) \zeta ^ { 3 } + ( c + { \frac { 8 } { 3 0 } } ) \zeta ^ { 2 } + ( { \frac { 1 9 } { 3 0 } } - c ) \zeta + ( { \frac { c } { 3 } } - { \frac { 1 } { 9 0 } } ) . } } \end{array}
$$

Then determine $c _ { 1 }$ and $c _ { 2 } { \mathrm { : } }$ ， such that the eigenvalues of the matrix S for the composite method become 1, 0, 0.

3. Prove that the composition of two different general linear methods (with the same correct value function) again gives a gen-eral linear method. As a consequence, the cyclic methods of Example 8.4 are general linear methods.

4. Suppose that all eigenvalues of S (except $\zeta _ { 1 } = 1$ ) lie inside the unit circle. Then

$$
\Vert R \parallel _ { E } = \underset { 0 \leq n \leq N } { \operatorname* { m a x } } \Vert r _ { n } + E \sum _ { j = 0 } ^ { n - 1 } r _ { j } \Vert
$$

is a minimal stability functional.

5. Verify for linear multistep methods that the consistency conditions (2.6) are equivalent to consistency of order 1 in the sense of Lemma 8.11.

6. Write Method (8.1) as general linear method (8.7) and determine its order (Answer: $p = 5$ ）


<!-- chunk 0007: pages 421-490 -->
# II1.9. Asymptotic expansion of the global error

The asymptotic expansion of the global error of multistep methods was studied in the famous thesis of Gragg (1963). His proof is very technical and can also be found in a modified version in the book of Stetter (1973)， pp.234-245. The existence of asymptotic expansions for general linear methods was conjectured by Skeel (1976). The proof given below (Hairer and Lubich (1984)) is based on the ideas of Section II.8.

# An instructive exam ple

Let us start with an example in order to understand which kind of asymptotic expansion may be expected. We consider the simple differential equation

$$
y ^ { \prime } = - y , \qquad y ( 0 ) = 1 ,
$$

take a constant step size $h$ and apply the 3-step BDF-formula (1. with one of the following three starting procedures:

$$
\begin{array} { r l r l } & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } \mathrm { e x p } ( - h ) } \\ & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } 1 { - } h + \displaystyle \frac { h ^ { 2 } } { 2 } - \displaystyle \frac { h ^ { 3 } } { 6 } } & & { y _ { 2 } { = } 1 { - } 2 h + 2 h ^ { 2 } - \displaystyle \frac { 8 h ^ { 3 } } { 6 } } \\ & { y _ { 0 } { = } 1 } & & { y _ { 1 } { = } 1 { - } h + \displaystyle \frac { h ^ { 2 } } { 2 } } & & { y _ { 2 } { = } 1 - 2 h + 2 h ^ { 2 } . } \end{array}
$$

The three pictures on the left of Figure 9.1 (they correspond to the three starting procedures in the same order) show the global error divided by $h ^ { 3 }$ for the five step sizes $h = 1 / 5$ ,1/10, 1/20, 1/40, 1/80.

For the first two starting procedures we observe uniform conver-gence to the function $e _ { 3 } ( x ) { = } x e ^ { - x } / 4$ (cf. Formula (2.12)), so that

$$
y _ { n } - y ( x _ { n } ) = e _ { 3 } ( x _ { n } ) h ^ { 3 } + \mathbf { O } ( h ^ { 4 } ) \ ,
$$

valid uniformly for $0 \leq n h \leq C o n s t$ . In the third case we have convergence to $e _ { 3 } ( x ) = ( 9 + x ) e ^ { - x } / 4$ (Exercise 2), but this time the convergence is no longer uniform. Therefore (9.2) only holds for $x _ { n }$ bounded away from $x _ { 0 }$ , i.e. for $0 < \alpha \leq n h \leq C o n s t$ . In the three pictures on the right of Figure 9.1 the functions

$$
( y _ { n } - y ( x _ { n } ) - e _ { 3 } ( x _ { n } ) h ^ { 3 } ) / { h ^ { 4 } }
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/f5f9264f23b35024421e522b37e06d839ab11b198efdad2094a03dcb57f87486.jpg)  
Figure 9.1. The values of $\frac { y _ { n } - y ( x _ { n } ) } { h ^ { 3 } }$ (left), $\frac { y _ { n } - y ( x _ { n } ) - e _ { 3 } ( x _ { n } ) h ^ { 3 } } { h ^ { 4 } }$ (right) for the 3-step BDF method and for three different starting procedures

are plotted. Convergence to functions $e _ { 4 } ( x )$ is observed in all cases. Clearly, since $e _ { 3 } ( x _ { 0 } ) \neq 0$ for the starting procedure (9.1c)， the sequence (9.3) diverges at $x _ { 0 }$ like $\mathbf { O } ( 1 / h )$ in this case.

We conclude from this example that for linear multistep methods there is in general no asymptotic expansion of the form

$$
y _ { n } - y ( x _ { n } ) = e _ { p } ( x _ { n } ) h ^ { p } + e _ { p + 1 } ( x _ { n } ) h ^ { p + 1 } + \cdot \cdot \cdot
$$

which holds uniformly for $0 \leq n h \leq C o n s t$ . It will be necessary to add perturbation terms

$$
y _ { n } - y ( x _ { n } ) = ( e _ { p } ( x _ { n } ) + \in _ { n } ^ { p } ) h ^ { p } + ( e _ { p + 1 } ( x _ { n } ) + \in _ { n } ^ { p + 1 } ) h ^ { p + 1 } + \cdot \cdot \cdot
$$

which compensate the irregularity near $x _ { 0 }$ . If the perturbations $\epsilon _ { n } ^ { j }$ decay exponentionally (for $n  \infty$ ), then they have no influence on the asymptotic expansion for $x _ { n }$ bounded away from $\boldsymbol { \mathscr { x } } _ { 0 }$

# Asymptotic expansion for strictly stable methods (8.4)

In order to extend the techniques of Section I1.8 to muitistep methods it is useful to write them as a "one-step" method in a higher dimensional space (cf. (4.8) and Example 8.2). This suggests we study at once the asymptotic expansion for the general method (8.4). Because of the presence of $\epsilon _ { n } ^ { j } h ^ { j }$ in (9.4), the iterative proof of Theorem 9.1 below will lead us to increment functions which also depend on $n$ , of the form

$$
\Phi _ { n } ( x , u , h ) = \Phi ( x , u + h \alpha _ { n } ( h ) , h ) + \beta _ { n } ( h ) \ .
$$

We therefore consider for an equidistant grid $( x _ { n } )$ the numerical procedure

$$
\begin{array} { c } { { u _ { 0 } = \phi ( h ) } } \\ { { { } } } \\ { { u _ { n + 1 } = S u _ { n } + h \Phi _ { n } ( x _ { n } , u _ { n } , h ) } } \end{array}
$$

where $\Phi _ { \pi }$ is given by (9.5) and the correct value function is again denoted by $z \left( x , h \right)$ . The following additional assumptions will simplify the discussion of an asymptotic expansion:

A1)Method (9.6) is stricty stable; i.e. it is stable (Definition 8.8) and 1 is the only eigenvalue of S with modulus one. In this case the spectral radius of $s - E$ (cf. Formula (8.11)) is smaller than 1 ;   
${ \bf A } 2 ) \alpha _ { n } ( h )$ and ${ \boldsymbol { \beta } } _ { n } \left( h \right)$ are polynomials， whose coeficients decay exponentially like $\mathbf { O } ( \rho _ { 0 } ^ { n } )$ for $n  \infty$ . Here ${ \boldsymbol \rho } _ { 0 }$ denotes some number lying between the spectral radius of $s - E$ and one; i.e. $\mathsf { p } ( \boldsymbol { S } - \boldsymbol { E } ) < \mathsf { p } _ { 0 } < 1$ ；

A3)the functions $\phi$ ， $z$ and $\Phi$ are sufficiently differentiable.

Assumption A3 allows us to expand the local error, defined by (8.9), into a Taylor series:

$$
\begin{array} { l } { { \displaystyle { \mathfrak { a } } + 1 = z ( x _ { n } + h , h ) - S z ( x _ { n } , h ) - h \Phi \big ( x _ { n } , z ( x _ { n } , h ) + h \mathfrak { a } _ { n } \big ( h ) , h \big ) - h \mathfrak { b } _ { n } } } \\ { { \displaystyle \qquad = d _ { 0 } ( x _ { n } ) + d _ { 1 } ( x _ { n } ) h + \cdot \cdot \cdot + d _ { N + 1 } ( x _ { n } ) h ^ { N + 1 } } } \\ { { \displaystyle \qquad - h ^ { 2 } \frac { \partial \Phi } { \partial u } ( x _ { n } , z ( x _ { n } , 0 ) , 0 ) \alpha _ { n } ( h ) - \cdot \cdot \cdot - h \mathfrak { b } _ { n } ( h ) + { \sf O } ( h ^ { N + 1 } ) \ , } } \end{array}
$$

The expressions involving $\alpha _ { n } \left( h \right)$ can be simplified further. Indeed, for a smooth function $G \left( x \right)$ we have

$$
\Im \left( x _ { n } \right) \alpha _ { n } ( h ) = G \left( x _ { 0 } \right) \alpha _ { n } ( h ) + h G ^ { \prime } ( x _ { 0 } ) n \alpha _ { n } ( h ) + \cdot \cdot \cdot + h ^ { N + 1 } R \left( n , \right)
$$

We observe that $n ^ { j } \alpha _ { _ n } ( h )$ is again a polynomial in $h$ and that its coefficients decay like" $\mathbf { 0 } ( \mathbf { \boldsymbol { \rho } } ^ { n } )$ where p satisfies $\boldsymbol { \rho } _ { 0 } < \boldsymbol { \rho } < 1$ . The same argument shows the boundedness of the remainder $R \ ( n \ , \ h )$ for $0 \leq n h \leq C o n s t$ .As a consequence we can write the local error in the form

$$
\begin{array} { r c l } { { } } & { { } } & { { d _ { 0 } = \gamma _ { 0 } + \gamma _ { 1 } h + \cdot \cdot \cdot + \gamma _ { N } h ^ { N } + 0 ( h ^ { N + 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { { } _ { n + 1 } = ( d _ { 0 } ( x _ { n } ) + \mathfrak { d } _ { n } ^ { 0 } ) + \cdot \cdot \cdot + ( d _ { N + 1 } ( x _ { n } ) + \mathfrak { d } _ { n } ^ { N + 1 } ) h ^ { N + 1 } + 0 ( h ^ { N + 2 } ) } } \end{array}
$$

The functions $d _ { j } ( \boldsymbol { x } )$ are smooth and the perturbations $8 { } _ { n } ^ { j }$ satisfy $\ S _ { n } ^ { j } { = } \mathbf { 0 } ( \boldsymbol { \rho } ^ { n } )$ . The expansion (9.7) is unique, because $\ S _ { \pi } ^ { j } \to$ 0 for $n  \infty$ ·

Method (9.6) is called consistent of order $\boldsymbol { p }$ , if the local error (9.7) satisfies (Lemma 8.11)

$$
d _ { n } = 0 ( h ^ { p } ) \qquad \mathrm { f o r } \quad 0 \leq n h \leq c o n s i , \quad \mathrm { a n d } \quad E d _ { p } ( x ) = 0 .
$$

Obs thisnth $8 { } _ { n } ^ { j }$ h ahe to vanish $j = 0 , \ldots , p - 1$ $\ S _ { n } ^ { p }$ tial decay of these terms implies that we still have

$$
d _ { n + 1 } + E ( d _ { n } + \cdot \cdot \cdot + d _ { 0 } ) = \mathrm { O } ( h ^ { P } ) \qquad \mathrm { f o r } 0 { \leq } n h { \leq } c o n s t ,
$$

in agreement with Definition 8.10. One can now easily verify that Lemma 8.12 ( $\Phi _ { \pi }$ satisfies a Lipschitz condition with the same constant as $\Phi$ ） and the Convergence Theorem 8.13 remain valid for Method (9.6). In the following theorem we use, as for one-step methods, the notation $\boldsymbol { u } _ { h _ { n } } ( \boldsymbol { x } ) = \boldsymbol { u } _ { n }$ when $x = x _ { n }$

Theorem 9.1. (Hairer-Lubich, 1984). Let the method (9.6) satisfy A $1 - A \ 3$ and be consistent of order $p \left( p \geq 1 \right)$ ).Then the global error has an asymptotic expansion of the form

$$
u _ { h } ( x ) - z ( x , h ) = e _ { p } ( x ) h ^ { p } + \cdot \cdot \cdot + e _ { N } ( x ) h ^ { N } + E ( x , h ) h ^ { N + 1 }
$$

where the $e _ { j } ( x )$ are given in the proof (cf. Formula $( 9 . I 8 )$ )and $E \left( x , h \right)$ is bounded uniformly in $h \in [ 0 , h _ { 0 } ]$ and for $x$ in compact intervals not containing $\boldsymbol { x } _ { \textup { 0 } }$ More precisely than (9.9), there is an expansion

$$
u _ { _ { R } } - z _ { _ { R } } = ( e _ { _ { p } } ( x _ { _ { R } } ) + \epsilon _ { _ { n } } ^ { p } ) h ^ { p } + \cdot \cdot \cdot + ( e _ { _ { N } } ( x _ { _ { R } } ) + \epsilon _ { _ { n } } ^ { N } ) h ^ { N } + \tilde { \cal E } ( n , h ) h _ { _ { \cal E } _ { \cal E } } ^ { I }
$$

where $\scriptstyle \epsilon _ { n } ^ { j } = 0 ( { \mathfrak { p } } ^ { n } )$ with $\mathsf { p } ( S - E ) < \mathsf { p } < 1$ and $\tilde { E } \left( n , h \right)$ is bounded for $0 \leq n h \leq c o n s t$

Remark: We obtain from (9.10) and (9.9)

$$
E ( x _ { n } , h ) = \tilde { E } ( n , h ) + h ^ { - 1 } \epsilon _ { n } ^ { N } + h ^ { - 2 } \epsilon _ { n } ^ { N - 1 } + \cdot \cdot \cdot + h ^ { p - N - 1 } \epsilon _ { n } ^ { p } ,
$$

so that the remainder term $E \left( x , h \right)$ is in general not uniformly bounded in $h$ for $x$ varying in an interval $[ x _ { 0 } , \bar { x } ]$ . However, if $x$ is bounded away from $\boldsymbol { \mathscr { x } } _ { \mathrm { ~ 0 ~ } }$ say ${ x \ge x _ { 0 } + 8 }$ ( $\delta > 0$ fixed), the sequence $\epsilon _ { n } ^ { j }$ goes to zero faster than any power of $8 / n \le h$ ·

Proof: a) As for one-step methods (cf. proof of Theorem 8.1, Chapter II) we construct a new method, which has as numerical solution

$$
\hat { a } _ { n } = u _ { n } - ( e ( x _ { n } ) + \epsilon _ { n } ) h ^ { p }
$$

for a given smooth function $e \left( x \right)$ and a given sequence $\epsilon _ { n }$ satisfying $\varepsilon _ { n } = \mathbf { O } ( \boldsymbol { \rho } ^ { n } ) .$ Such a method is given by

$$
\begin{array} { c } { { \hat { u } _ { 0 } = \hat { \phi } ( h ) } } \\ { { { } } } \\ { { \hat { u } _ { n + 1 } = S \hat { u } _ { n } + h \hat { \Phi } _ { n } ( x _ { n } , \hat { u } _ { n } , h ) } } \end{array}
$$

where $\hat { \boldsymbol { \Phi } } ( h ) { = } { \boldsymbol { \Phi } } ( h ) { - } ( \boldsymbol { e } ( \boldsymbol { x } _ { 0 } ) { + } \epsilon _ { 0 } ) h ^ { p }$ and

$$
\begin{array} { l } { { \hat { \Phi } _ { n } ( x , u , h ) = \Phi _ { n } ( x , u + ( e ( x ) + \epsilon _ { n } ) h ^ { p } , h ) } } \\ { { \mathrm { } - ( e ( x + h ) - S e ( x ) ) h ^ { p - 1 } - ( \epsilon _ { n + 1 } - S \epsilon _ { n } ) h ^ { p - 1 } . } } \end{array}
$$

Since $\Phi _ { n }$ is of the form (9.5), $\hat { \Phi } _ { n }$ is also of this form, so that its local error has an expansion (9.7). We shall now determine $e \left( x \right)$ and $\epsilon _ { n }$ in such a way that the method (9.12) is consistent of order $p + 1$ ·

b) The local error $\hat { d } _ { n }$ of (9.12) can be expanded as

$$
\begin{array} { r l } & { \quad \hat { d } _ { 0 } = z _ { 0 } - \hat { a } _ { 0 } = ( \gamma _ { p } + e ( x _ { 0 } ) + \epsilon _ { 0 } ) h ^ { p } + 0 ( h ^ { p + 1 } ) } \\ & { \quad \hat { d } _ { n + 1 } = z _ { n + 1 } - S z _ { n } - h \hat { \Phi } _ { n } ( x _ { n } , z _ { n } , h ) } \\ & { \quad \quad \quad = d _ { n + 1 } + \bigg ( ( I - S ) e ( x _ { n } ) + ( \epsilon _ { n + 1 } - S \epsilon _ { n } ) \bigg ) h ^ { p } } \\ & { \quad \quad \quad + \left( - G ( x _ { n } ) ( e ( x _ { n } ) + \epsilon _ { n } ) + e ^ { \prime } ( x _ { n } ) \right) h ^ { p + 1 } + 0 ( h ^ { p + 2 } ) \ . } \end{array}
$$

Here

$$
G ( x ) = \frac { \partial \Phi _ { n } } { \partial u } ( x , z ( x , 0 ) , 0 )
$$

which is independent of $n$ by (9.5). The method (9.12) is consistent of order $p + 1$ if (see (9.8))

$$
\begin{array} { r l } & { \epsilon _ { 0 } = - \gamma _ { 0 } - e ( x _ { 0 } ) } \\ & { d _ { p } ( x ) + ( I - S ) e ( x ) + \ S _ { n } ^ { p } + \epsilon _ { n + 1 } - S \epsilon _ { n } = 0 \quad \mathrm { f o r } x = x _ { n } } \\ & { E e ^ { \prime } ( x ) = E G \left( x \right) e ( x ) - E d _ { p + 1 } ( x ) \ . } \end{array}
$$

We assume for the moment that the system (i)-(ii) can be solved for $e \left( x \right)$ and $\epsilon _ { n }$ . This will actually be demonstrated in part d) of the proof. By the Convergence Theorem 8.13 the method (9.12) is convergent of order $p + 1 .$ Hence

$$
\begin{array} { r } { \widehat { a } _ { n } - z _ { n } = { \bf O } ( h ^ { p + 1 } ) \quad \mathrm { ~ u n i f o r m l y ~ f o r ~ } 0 \leq n h \leq c o n s t \enspace , } \end{array}
$$

which yields the statement (9.10) for $N = _ { P }$

c) The method (9.12) satisfies the assumptions of the theorem with $p$ replaced by $p + 1$ and ${ \mathfrak { p } } _ { 0 }$ by p. As in Theorem 8.1 (Section I.8) an induction argument yields the result.

d) It remains to find a solution of the system (i)-(ii). Condition (ii) is satisfied if

$$
\begin{array} { l } { { d _ { p } ( x ) = ( S - I ) ( e ( x ) + c ) \nonumber } } \\ { { \phantom { e } \epsilon _ { n + 1 } - c = S ( \epsilon _ { n } - c ) - 8 { } _ { n } ^ { p } } } \end{array}
$$

hold for some constant $c$ . Using $( I - S + E ) ^ { - 1 } ( I - S ) = ( I - E )$ , which is a consequence of $S E = E ^ { 2 } = E$ (see (8.11)), Formula (iia) is equivalent

to

$$
\bigl ( I - S + E \bigr ) ^ { - 1 } d _ { p } ^ { } \bigl ( x \bigr ) = - \bigl ( I - E \bigr ) \bigl ( e \bigl ( x \bigr ) + c \bigr ) .
$$

From (i) we obtain $\epsilon _ { 0 } - c = - \gamma _ { p } - ( e ( x _ { 0 } ) + c )$ , so that by (9.13)

$$
( I - E ) ( \epsilon _ { 0 } - c ) = - ( I - E ) \gamma _ { p } + \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) \ ,
$$

Since $E d _ { p } ( x _ { 0 } ) = 0$ , this relation is satisfied in particular if

$$
\epsilon _ { 0 } - c = - \left( I - E \right) \gamma _ { p } + \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) \ .
$$

The numbers $\epsilon _ { n } - c$ are now determined by the recurrencc relation (ib)

$$
\begin{array} { l } { { \displaystyle { \mathrm {  ~ \Sigma ~ } ^ { \prime } } \mathrm {  ~ \Sigma ~ } ^ { \epsilon } } _ { n } - c = S ^ { n } ( \epsilon _ { 0 } - c ) - \sum _ { j = 1 } ^ { n } S ^ { n - j } \mathfrak { d } _ { j - 1 } ^ { p } } \\ { \displaystyle { \mathrm {  ~ \Sigma ~ } } } \\ { { \displaystyle { \mathrm {  ~ \Sigma ~ } } ^ { \epsilon } \left( \epsilon _ { 0 } - c \right) + \left( S - E \right) ^ { n } \left( \epsilon _ { 0 } - c \right) - E \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p } + E \sum _ { j = n } ^ { \infty } \mathfrak { d } _ { j } ^ { p } - \sum _ { j = 1 } ^ { n } \left( S - E \right) ^ { n - j } \mathfrak { d } _ { j - 1 } ^ { p } } } \end{array}
$$

where we have used $S ^ { n } = E + ( S - E ) ^ { n }$ . If we put

$$
c = E \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p }
$$

the sequence $\{ \epsilon _ { n } \}$ defined above satisfies $\scriptstyle \epsilon _ { n } = 0 ( \rho ^ { n } )$ ,since $E \left( \epsilon _ { 0 } - c \right) = 0$ by (9.14) and since $\ S _ { n } ^ { p } { = } \mathbf { 0 } ( \boldsymbol { \rho } ^ { n } )$

In order to find $e \left( x \right)$ we define

$$
\nu ( x ) = E e ( x ) .
$$

With the help of Formulas (9.15) and (9.13) we can recover $e \left( x \right)$ from $\nu ( x )$ by

$$
e ( x ) = \nu ( x ) - ( I { - } S { + } E ) ^ { - 1 } d _ { p } ( x ) ~ .
$$

Equation (ii) can now be rewritten as the differential equation

$$
\nu ^ { \prime } ( x ) = E G \left( x \right) \left( \nu \left( x \right) - \left( I - S + E \right) ^ { - 1 } d _ { p } \left( x \right) \right) - E d _ { p + 1 } ( x ) \ ,
$$

and Condition (i) yields the starting value $\nu \left( x _ { 0 } \right) { = } { - } E \left( \gamma _ { p _ { . } } { + } \varepsilon _ { 0 } \right)$ . This initial value problem can be solved for $\nu \left( x \right)$ and we obtain $e \left( x \right)$ by (9.16). This function and the $\epsilon _ { n }$ defined above represent a solution of (i)-(ii). QED.

Remarks: a) It follows from (9.15)-(9.17) that the principal error term satisfies

$$
\begin{array} { l } { { e _ { p } ^ { \prime } ( x ) = E G ( x ) e _ { p } ( x ) - E d _ { p + 1 } ( x ) - \left( I - S + E \right) ^ { - 1 } d _ { p } ^ { \prime } ( x ) } } \\ { { e _ { p } ( x _ { 0 } ) = - E \gamma _ { p } - E \displaystyle \sum _ { j = 0 } ^ { \infty } \mathfrak { d } _ { j } ^ { p } - \left( I - S + E \right) ^ { - 1 } d _ { p } ( x _ { 0 } ) . } } \end{array}
$$

b） Since $e _ { p + 1 } ( x )$ is just the principal error term of Method (9.12), it satisfies the differential equation (9.18) with $d _ { j }$ replaced by $\hat { d } _ { j + 1 }$ By an induction argument we therefore have for $j \equiv p$

$$
e _ { j } ^ { \prime } ( x ) = E G ( x ) e _ { j } ( x ) + \mathrm { i n h o m o g e n e i t y } \ ( x ) .
$$

# Weakly stable methods

We next study the asymptotic expansion for stable methods, which are not strictly stable. E.g. the explicit mid-point rule (1.13'), treated in connection with the GBS-algorithm (Section II.9), is of this type. As at the beginning of this section, we apply the mid-point rule to the problem $y \prime { = } { - y }$ ， $y \left( 0 \right) { = } 1$ and consider the following three starting procedures

$$
\begin{array} { l c r c l } { { y _ { 0 } = 1 ~ , ~ } } & { { ~ } } & { { ~ y _ { 1 } = \exp ( - h ) } } \\ { { } } & { { } } & { { } } & { { } } \\ { { y _ { 0 } = 1 ~ , ~ } } & { { ~ y _ { 1 } = 1 - h + \frac { { h ^ { 2 } } } { 2 } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { y _ { 0 } = 1 ~ , ~ } } & { { ~ y _ { 1 } = 1 - h ~ . } } \end{array}
$$

The three pictures on the left of Figure 9.2 show the global error divided by $\hat { h } ^ { 2 }$ For the first two starting procedures we have conver-

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/70f37d930b08f2f3615448f281c85bb0eab8fa75c44ace4d2fbaeb16c0514353.jpg)  
Figure 9.2. Asymptotic expansion of the mid-point rule (three different starting procedures)

gence to the function $x e ^ { - x } / 6$ ，while for (9.19c) the divided error $\bar { ( y } _ { n } - y ( x _ { n } ) ) / h ^ { 2 }$ converges to

$$
\begin{array} { l l } { { e ^ { - x } \left( \displaystyle \frac { 2 x - 3 } { 1 2 } - \frac { e ^ { x } } { 4 } \right) \qquad \mathrm { f o r } n \mathrm { e v e n } \ , } } \\ { { e ^ { - x } \left( \displaystyle \frac { 2 x - 3 } { 1 2 } + \frac { e ^ { x } } { 4 } \right) \qquad \mathrm { f o r } n \mathrm { o d d } \ . } } \end{array}
$$

We then subtract the $h ^ { 2 }$ -term from the global error and divide by $h ^ { 3 }$ in the case (9.19a) and by $h ^ { 4 }$ for b) and c). The result is plotted in the pictures on the right of Figure 9.2.

This example nicely illustrates the fact that we no longer have an asymptotic expansion of the form (9.9) or (9.10) but that there exists an expansion if we consider $x _ { n }$ with $n$ even; there exists a different expansion at $x _ { n }$ with $n$ odd (see also Exercise 2 of Section II.9). Similar results for more general methods wil be obtained here.

We say that a method of the form (8.4) is weakly stable, if it is stable, but if the matrix S has, besides $\zeta _ { 1 } = 1$ ， further eigenvalues of modulus 1, say $\zeta _ { 2 } , \ldots , \zeta _ { i } .$ The matrix S therefore has the representation (cf. (8.11))

$$
S = \zeta _ { 1 } E _ { 1 } + \zeta _ { 2 } E _ { 2 } + \cdot \cdot \cdot + \zeta _ { l } E _ { l } + R
$$

where the $E _ { j }$ are the projectors (corresponding to $\zeta _ { j }$ ) and the spectral radius of $R$ satisfies $\rho ( R \ ) < 1$

In what follows we restrict ourselves to the case where all $\boldsymbol { \zeta } _ { j }$ $( j = 1 , \ldots , l )$ are roots of unity. This allows a simple proof for the existence of an asymptotic expansion and is at the same time by far the most important special case. For the general situation we refer to Hairer-Lubich (1984).

Theorem 9.2. Let the method (9.6) wih $\Phi _ { n }$ independent of n be stable, consistent of order $\boldsymbol { p }$ and satisfy A3. If all eigenvalues (of S ) of modulus 1 satisfy $\zeta _ { j } ^ { \ : q } = 1 \ : \ : ( j = 1 \ : , \ldots , l )$ for some positive integer $q$ , then we have an asymptotic expansion of the form ( $\scriptstyle ( 0 ) = e ^ { 2 \pi i / q }$ ）

$$
u _ { n } \ - z _ { n } \ = \ \sum _ { s = 0 } ^ { q - 1 } \mathfrak { u } ^ { n s } \left( e _ { p s } ( x _ { n } ) h ^ { p } \ + \ \cdot \ \cdot \ + e _ { N s } ( x _ { n } ) h ^ { N } \right) \ + E ( n , h ) h ^ { N + 1 }
$$

where the $e _ { j s } ( x )$ are smooth functions and $E \left( n \ , \ h \right)$ is uniformly bounded for $0 < 8 \leq n h \leq c o n s t$

Proof: The essential idea of the proof is to consider $q$ consecutive steps of Method (9.6) as one method over a large step. Puting $\tilde { u } _ { n } = u _ { n q + i } \quad ( 0 \leq i \leq q - 1$ fixed)， ${ \tilde { h } } = q h$ and $\boldsymbol { \tilde { x } } _ { n } = \boldsymbol { x } _ { i } + n \boldsymbol { \tilde { h } }$ ，thismethod becomes

$$
{ \tilde { u } } _ { n + 1 } = S ^ { q } { \tilde { u } } _ { n } + { \tilde { h } } { \tilde { \Phi } } ( { \tilde { x } } _ { n } , { \tilde { u } } _ { n } , { \tilde { h } } )
$$

with a suitably chosen $\tilde { \Phi }$ . E.g. for $q = 2$ we have

$$
\tilde { \Phi } ( \tilde { x } , \tilde { u } , \tilde { h } ) = \frac { 1 } { 2 } s \Phi ( \tilde { x } , \tilde { u } , \frac { \tilde { h } } { 2 } ) + \frac { 1 } { 2 } \Phi \left( \tilde { x } + \frac { \tilde { h } } { 2 } , { \cal S } \tilde { u } + \frac { \tilde { h } } { 2 } \Phi ( \tilde { x } , \tilde { u } , \frac { \tilde { h } } { 2 } ) , \frac { \tilde { h } } { 2 } \right)
$$

The assumption on the eigenvalues implies

$$
\boldsymbol { S } ^ { q } = \boldsymbol { E } _ { 1 } + \cdot \cdot \cdot + \boldsymbol { E } _ { l } + \boldsymbol { R } ^ { q }
$$

so that (9.21) is seen to be a strictly stable method. A straightforward calculation shows that the local error of (9.21) satisfies

$$
\begin{array} { r l } & { \qquad \tilde { d } _ { 0 } = { \bf O } ( h ^ { p } ) } \\ & { \qquad \tilde { d } _ { n + 1 } = ( I + S + \cdot \cdot \cdot + S ^ { q - 1 } ) d _ { p } ( \tilde { x } _ { n } ) h ^ { p } + { \bf O } ( h ^ { p + 1 } ) ~ . } \\ & { \qquad \mathrm { i n g ~ ( 9 . 1 9 ) ~ a n d ~ u s i n g ~ } \xi _ { j } ^ { q } = 1 \mathrm { ~ w e ~ o b t a i n , ~ w i t h ~ } \tilde { E } = E _ { 1 } + \cdot \cdot \cdot + E _ { l } , } \\ & { \qquad \tilde { E } \left( I + S + \cdot \cdot \cdot + S ^ { q - 1 } \right) d _ { p } ( x ) } \\ & { = \tilde { E } \left( I - \tilde { E } + q E _ { 1 } + \underset { j = 2 } { \overset { l } { \sum } } \frac { 1 - \xi _ { j } ^ { q } } { 1 - \xi _ { j } } E _ { j } + \underset { j = 1 } { \overset { q - 1 } { \sum } } R ^ { j } \right) d _ { p } ( x ) = q E _ { 1 } d _ { p } ( x ) ~ , } \end{array}
$$

which vanishes by (8.15). Hence, also Method (9.21) is consistent of order $p$ . All the assumptions of Theorem 9.1 are thus verified for Method (9.21). We therefore obtain

$$
\iota _ { n q + i } - z _ { n q + i } = \tilde { e } _ { p i } ( x _ { n q + i } ) h ^ { p } + \cdot \cdot \cdot + \tilde { e } _ { N i } ( x _ { n q + i } ) h ^ { N } + E _ { i } ( n , h ) h ^ { N + }
$$

where $E _ { i } ( n \ , \ h )$ has the desired boundedness properties. If we define $e _ { j s } ( x )$ as solution of the Vandermonde-type system

$$
\sum _ { s = 0 } ^ { q - 1 } \omega ^ { i s } e _ { j s } ( x ) = \widetilde { e } _ { j i } ( x )
$$

we obtain (9.20). QED.

# The adjoint method

For a method (8.4) the correct value function $z \left( x , h \right)$ , the starting procedure $\Phi ( h )$ and the increment function $\Phi ( x , u , h )$ are usu-ally also defined for negative h (see the examples of Section III.8). As for one-step methods (Section I.8) we shall give here a precise meaning to the numerical solution $\boldsymbol { u } _ { h } \left( \boldsymbol { x } \right)$ for negative h . This then leads in a natural way to the study of asymptotic expansions in even powers of h .

With the notation $\boldsymbol { u } _ { h } ( \boldsymbol { x } ) = \boldsymbol { u } _ { n }$ for $x = x _ { \mathrm { \ell _ { 0 } } } + n h \left( h > 0 \right)$ the method (8.4) becomes

$$
\begin{array} { r } { \begin{array} { r l r } { u _ { h } ( x _ { 0 } ) = \Phi ( h ) } & { { } \quad } & { ( \mathrm { i } \pi ^ { \prime } ) \leq \pi ^ { \prime } \frac { 1 } { h } , } \\ { u _ { h } ( x + h ) = S u _ { h } ( x ) + h \Phi ( x , u _ { h } ( x ) , h ) } & { { } \quad } & { \mathrm { f o r } x = x _ { 0 } + n h . } \end{array} } \end{array}
$$

We first replace $h$ by $- h$ in (9.22) to obtain

$$
\begin{array} { c } { { u _ { - h } ( x _ { 0 } ) = \phi ( - h ) } } \\ { { { } } } \\ { { u _ { - h } ( x - h ) = S u _ { - h } ( x ) - h \Phi ( x , u _ { - h } ( x ) , - h ) } } \end{array}
$$

and then $x$ by $x + h$ which gives

$$
\begin{array} { l } { { u _ { - h } ( x _ { 0 } ) = \phi ( - h ) \nonumber } } \\ { { u _ { - h } ( x ) = S u _ { - h } ( x + h ) - h \Phi ( x + h , u _ { - h } ( x + h ) , - h ) . } } \end{array}
$$

For sufficiently small $^ h$ this equation can be solved for $u _ { - h } ( x + h )$ (implicit function theorem) and we obtain

$$
\begin{array} { c } { { u _ { - h } ( x _ { 0 } ) = \Phi ( - h ) ~ , } } \\ { { u _ { - h } ( x + h ) = S ^ { - 1 } u _ { - h } ( x ) + h \Phi ^ { * } ( x , u _ { - h } ( x ) , h ) ~ . } } \end{array}
$$

The method (9.23),which is again of the form (8.4), is called the adjoint method of (9.22). Its correct value" function is $z ^ { * } ( x , h ) { = } z \left( x , - h \right)$ . Observe that for given S and $\Phi$ the new incre-ment function $\Phi ^ { * }$ is just defined by the pair of formulas

$$
\begin{array} { l } { { \nu = S u - h \Phi ( x + h , u , - h ) } } \\ { { } } \\ { { u = S ^ { - 1 } \nu + h \Phi ^ { * } ( x , \nu , h ) . } } \end{array}
$$

Example 9.3. Consider a linear multistep method with generating functions

$$
{ \displaystyle \rho ( \zeta ) = \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta ^ { j } } , ~ { \displaystyle \sigma \left( \zeta \right) = \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta ^ { j } } ~ .
$$

Then we have

$$
\left( \begin{array} { c c c c c } { { - \alpha _ { k - 1 } / \alpha _ { k } } } & { { - \alpha _ { k - 2 } / \alpha _ { k } } } & { { . . } } & { { . } } & { { - \alpha _ { 0 } / \alpha _ { k } } } \\ { { 1 } } & { { 0 } } & { { . . } } & { { . } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { . } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { . } } & { { 0 } } \\ { { } } & { { } } & { { \vdots } } & { { } } & { { : } } \\ { { } } & { { } } & { { 1 } } & { { 0 } } \end{array} \right) , \Phi ( x , u , h ) = \left( \begin{array} { c } { { 1 } } \\ { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right) \psi ( x , u , h ) .
$$

where $\psi = \psi ( x , u , h )$ is the solution of $( u = ( u _ { k - 1 } , \ldots , u _ { 0 } ) ^ { T } )$

$$
\alpha _ { k } \psi = \sum _ { j = 0 } ^ { k - 1 } 8 _ { j } f \left( x + j h , u _ { j } \right) + \beta _ { k } f \left( x + k h , h \psi - \sum _ { j = 0 } ^ { k - 1 } \frac { \alpha _ { j } } { \alpha _ { k } } u _ { j } \right) .
$$

A straightforward use of the formulas (9.24) shows that

$$
\begin{array} { r l r } { - 1 } & { { } } & { \left( \begin{array} { c c c c } { 0 } & { 1 } & { } & { } & { } \\ { 0 } & { 0 } & { } & { } & { } \\ { \vphantom { \int } 0 } & { \vphantom { \int } 0 } & { \dots } & { 1 } & { } \\ { \vphantom { \int } 0 } & { \dots } & { \dots } & { \dots } & { 1 } \\ { - \alpha _ { k } / \alpha _ { 0 } } & { - \alpha _ { k - 1 } / \alpha _ { 0 } } & { \dots } & { - \alpha _ { 1 } / \alpha _ { 0 } } \end{array} \right) , } & { \Phi ^ { * } ( x , \nu , h ) } & { { } = \left( \begin{array} { c } { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \end{array} \right) \Psi ^ { * } ( x , \nu , h ) } \end{array}
$$

where $\Psi ^ { * } { = } \Psi ^ { * } ( x \ , \nu \ , h )$ (with $\nu = ( \nu _ { 0 } , \ldots , \nu _ { k - 1 } ) ^ { T } )$ is given by

$$
- \alpha _ { 0 } \boldsymbol { \Psi } ^ { * } = \sum _ { j = 0 } ^ { k - 1 } \mathsf { B } _ { k - j } f \left( \boldsymbol { x } + \left( j - k + 1 \right) \boldsymbol { h } , \nu _ { j } \right) + \mathsf { B } _ { 0 } f \left( \boldsymbol { x } + \boldsymbol { h } , \boldsymbol { h } \boldsymbol { \Psi } ^ { * } - \sum _ { j = 0 } ^ { k - 1 } \frac { \alpha _ { k - j } } { \alpha _ { 0 } } \nu _ { j } \right)
$$

This shows that the adjoint method is again a linear multistep method. Its generating polynomials are

$$
\boldsymbol { \rho } ^ { * } ( \zeta ) = - \zeta ^ { k } \rho ( \frac { 1 } { \zeta } ) , \qquad \sigma ^ { * } ( \zeta ) = \zeta ^ { k } \sigma ( \frac { 1 } { \zeta } ) .
$$

Our next aim is to prove that the adjoint method has exactly the same asymptotic expansion as the original method, with h replaced by $- h$ .For this it is necessary that $S ^ { - 1 }$ also be a stable matrix. Therefore all eigenvalues of S must lie on the unit circle.

Theorem 9.4. Let the method (9.22) be stable, consistent of order p and assume that al eigenvalues of $s$ satisfy $\zeta _ { j } ^ { q } { = } 1$ for some positive integer $q$ Then the global error has an asymptotic expansion of the form $\scriptstyle { \hat { ( } } \omega = e ^ { 2 \pi i / q }$ ）

$$
\begin{array} { l } { { { \displaystyle { \stackrel { \prime } { } } } _ { \displaystyle { u _ { h } } } ( x _ { n } ) \stackrel { \prime } { } - z ( x _ { n } , h ) = \sum _ { s = 0 } ^ { q - 1 } \omega ^ { n s } \left( e _ { p s } ( x _ { n } ) h ^ { p } + \cdot \cdot \cdot \cdot + e _ { N s } ( x _ { n } ) h ^ { N } \right) } } \\ { { { } } } \\ { { { \qquad + \ E ( x _ { n } , h ) h ^ { N + 1 } , } } } \end{array}
$$

valid for positive and negative h. The remainder $E \left( x ~ , ~ h \right)$ is uniformly bounded for $\mid h \mid \leq h _ { 0 } a n d x _ { 0 } \leq x \leq { \hat { x } } .$

Proof: As in the proof of Theorem 9.2 we consider $q$ consecutive steps of Method (9.22) as one new method. The assumption on the eigenvalues implies that $S ^ { q } = I =$ identity. Therefore the new method is essentially a one-step method. The only difference is that here the starting procedure and the correct value function may depend on h . A straightforward extension of Theorem 8.5 of Chapter I1 (Exercise 3) implies the existence of an expansion

$$
\begin{array} { r } { u _ { h } ( x _ { n q + i } ) - z ( x _ { n q + i } , h ) = \tilde { e } _ { p i } ( x _ { n q + i } ) h ^ { p } + \cdot \cdot \cdot + \tilde { e } _ { N i } ( x _ { n q + i } ) h ^ { N } } \\ { + E _ { i } ( x _ { n q + i } , h ) h ^ { N + 1 } . \qquad } \end{array}
$$

This expansion is valid for positive and negative $h$ and the remainder $E _ { i } ( x \ , \ h \ )$ is bounded for $\left| h \right. \left| \leq h _ { 0 } \right.$ and $x _ { 0 } \leq x \leq \bar { x }$ . The same argument as in the proof of Theorem 9.2 now leads to the desired expansion. QED.

# Symmetric methods

The definition of symmetry for general linear methods is not as straightforward as for one-step methods. In Example 9.3 we saw that the components of the numerical solution of the adjoint method are in inverse order._Therefore, it is too restrictive to require $\Phi ( h ) { = } \Phi ( - h )$ ， $s = s ^ { - 1 }$ and $\bar { \Phi } { = } { \bar { \Phi } } ^ { * }$

However, for many methods of practical interest the correct value function satisfies a symmetry relation of the form

$$
z \left( x , h \right) = Q z \left( x + q h , - h \right)
$$

where $Q$ is a square matrix and $q$ an integer. This is for instance the case for linear multistep methods, where the correct value function is given by

$$
z \left( x , h \right) = \left( y \left( x + ( k - 1 ) h \right) , \ldots , y \left( x \right) \right) ^ { T } \ ;
$$

the relation (9.27) holds with

$$
{ \cal Q } \ = \ \left( \begin{array} { c c } { { } } & { { 1 } } \\ { { } } & { { . } } \\ { { 1 } } & { { } } \end{array} \right) \qquad \mathrm { a n d } \qquad q \ = k - 1 \ .
$$

Definition 9.5. Suppose that the correct value function satisfies (9.27). Method (9.22) is called symmetric (with respect to (9.27)), if the numerical solution satisfies its analogue

$$
u _ { h } ( x ) = Q u _ { - h } ( x + q h ) \ .
$$

Example 9.6. Consider a linear multistep method and suppose that the generating polynomials of the adjoint method (9.25) satisfy

$$
\begin{array} { r } { \rho ^ { \ast } ( \zeta ) = \rho ( \zeta ) , \qquad \sigma ^ { \ast } ( \zeta ) = \sigma ( \zeta ) . } \end{array}
$$

This is equivalent to the requirement (cf. (3.24))

$$
\alpha _ { k - j } = - \alpha _ { j } \ , \qquad \beta _ { k - j } = \beta _ { j } \ .
$$

A straightforward calculation (using the formulas of Example 9.3) then shows that the symmetry relation (9.29) holds for all ${ { x } \mathord {  } { } _ { \mathrm { { x } } } } _ { 0 } + { { n h } }$ whenever it holds for $x = x _ { 0 } .$ This imposes an additional condition on the starting procedure $\Phi ( h )$ ：

Let us finally demonstrate how Theorem 9.4 can be used to prove asymptotic expansions in even powers of $h$ . Denote by $u _ { h } ^ { j } ( x )$ the $j$ -th component of $u _ { h } ( x )$ . The symmetry relation (9.29) for multistep methods then implies

$$
\begin{array} { r } { \boldsymbol { \mu } _ { - h } ^ { k } ( \boldsymbol { x } ) = \boldsymbol { u } _ { h } ^ { 1 } ( \boldsymbol { x } - ( k - 1 ) h ) , } \end{array}
$$

Furthermore, for any multistep method we have

so that

$$
\begin{array} { c } { { u _ { h } ^ { k } ( x ) = u _ { h } ^ { 1 } ( x - ( k - 1 ) h ) } } \\ { { { } } } \\ { { u _ { h } ^ { k } ( x ) = u _ { - h } ^ { k } ( x ) } } \end{array}
$$

for symmetric methods. As a consequence of Theorem 9.4 the asymptotic expansion of the global error is in even powers of h, whenever the multistep method is symmetric in the sense of Definition 9.5.

# Exercises

1. Consider a strictly stable, $p$ -th order, linear multistep method written in the form (9.6) (see Example 9.3) and set

$$
G ( x ) = \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \ .
$$

a) Prove that

$$
E G \left( x \right) \mathbf { 1 } = \mathbf { 1 } \frac { \partial f } { \partial y } ( x \textrm { , } y ( x ) )
$$

where $\boldsymbol { E }$ is the matrix given by (8.11) and $\mathbf { 1 } = ( 1 , \ldots , 1 ) ^ { T }$

b) Show that the function $e _ { p } ( x )$ in the expansion (9.9) is given by $e _ { p } ( x ) = \mathbb { 1 } \hat { e } _ { p } ( x ) ,$ where

$$
\begin{array} { r } { \hat { e } _ { p } ^ { \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) \hat { e } _ { p } ( x ) - C y ^ { ( p + 1 ) } ( x ) } \end{array}
$$

and $c$ is the error constant (cf. (2.13)). Compute also ${ \partial _ { p } } ( x _ { 0 } )$

2. For the 3-step BDF-method, applied to $y ^ { \prime } { = } { - } y$ ， $y \left( 0 \right) { = } 1$ with start-ing procedure (9.1c), compute the function $e _ { 3 } ( x )$ and the perturbations $\bigl ( \epsilon _ { n } ^ { 3 } \bigr ) _ { n \geq 0 }$ in the expansion (9.4). Compare your result with Figure 9.1.

3. Consider the method

$$
\begin{array} { c } { { u _ { 0 } = \phi ( h ) } } \\ { { \ } } \\ { { u _ { n + 1 } = u _ { n } + h \Phi ( x _ { n } , z _ { n } , h ) } } \end{array}
$$

with correct,value function $z \left( x , h \right)$ ，

a) Prove that the global error has an asymptotic expansion of the form

$$
u _ { n } - z _ { n } = e _ { p } ( x _ { n } ) h ^ { p } + \cdot \cdot \cdot + e _ { N } ( x _ { n } ) h ^ { N } + E ( x _ { n } , h ) h ^ { N + 1 }
$$

where $E \left( x , h \right)$ is uniformly bounded for $0 \leq h \leq h _ { \mathrm { ~ 0 ~ } }$ and $x _ { 0 } \leq x \leq \hat { x }$ b) Show that Theorem 8.5 of Chapter II remains valid for Method (9.31).

4. Let $\rho ^ { * } ( \zeta )$ and $\sigma ^ { * } ( \zeta )$ be given by (9.25). Under the assumption

$$
\begin{array} { r } { \boldsymbol { \mathrm { p } } ^ { * } ( \boldsymbol { \xi } ) = \boldsymbol { C } \boldsymbol { \mathrm { p } } ( \boldsymbol { \xi } ) , \qquad \boldsymbol { \mathrm { \sigma } } ^ { * } ( \boldsymbol { \xi } ) = \boldsymbol { C } \boldsymbol { \mathrm { \sigma } } ( \boldsymbol { \xi } ) , } \end{array}
$$

the symmetry relation (9.29) is satisfied for all ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 } + n h$ whenever it is valid for ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 0 }$ . What was the reason for setting $C = 1$ in (9.30)?

# I11.10. Multistep methods for second order differential equations

"En 19o4 jeus besoin d'une pareille methode pour calculer les trajectoires des corpuscules electrises dans un champ magnetique, et en essayant diverses methodes deja connues, mais sans les trouver assez commodes pour mon but, je fus conduit moi-méme a elaborer une methode assez simple, dont je me suis servi ensuite."   
(C. Stormer, 1921)

Because of their importance, second order differential equations deserve some additional attention. We already saw in Section I1.13 that for special second order differential equations certain direct onestep methods are more efficient than the classical Runge-Kutta methods. We now investigate whether a similar situation also holds for multistep methods.

Consider the second order differential equation

$$
y \prime \prime = f \left( x , y , y \right)
$$

where y is allowed to be a vector. We rewrite (10.1) in the usual way as a first order system and apply a multistep method

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } = h \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } ^ { \prime } } } \\ { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } ^ { \prime } = h \sum _ { i = 0 } ^ { k } \beta _ { i } f \left( x _ { n + i } , y _ { n + i } , y _ { n + i } ^ { \prime } \right) . } } \end{array}
$$

If the right hand side of the differential equation does not depend on

$$
y \ ^ { \prime \prime } = f \left( x \ , \ y \right) \ ,
$$

it is natural to look for numerical methods which do not involve the first derivative y'. An elimination of $\{ \boldsymbol { y } _ { n } ^ { \prime } \}$ in the equations (10.2)

$$
\sum _ { i = 0 } ^ { 2 k } \hat { \mathbf { \alpha } } _ { i } y _ { n + i } = h ^ { 2 } \sum _ { i = 0 } ^ { 2 k } \hat { \mathbf { \beta } } _ { i } f \left( x _ { n + i } , y _ { n + i } \right)
$$

where the new coefficients &., $\hat { \mathsf { \beta } } _ { i }$ are given by

$$
\sum _ { i = 0 } ^ { 2 k } \hat { \alpha } _ { i } \zeta ^ { i } \ = \ \biggl ( \sum _ { i = 0 } ^ { k } \alpha _ { i } \zeta ^ { i } \biggr ) ^ { 2 } \ , \qquad \sum _ { i = 0 } ^ { 2 k } \hat { \beta } _ { i } \zeta ^ { i } \ = \ \biggl ( \sum _ { i = 0 } ^ { k } \beta _ { i } \zeta ^ { i } \biggr ) ^ { 2 } \ .
$$

In what follows we investigate (10.4) with coefficients that do not necessarily satisfy (10.5). It is hoped to achieve the same order with a smaller step num ber.

# The first methods

"nous avons calcule plus de 120 trajectoires differentes, travail immense qui a exige plus de 45oo heures.."

"Sein Vortrag ist ubrigens ziemlich trocken und langweilig.. (B. Riemann's opinion about Encke, 1847)

Since most differential equations of celestial mechanics are of the form (10.3) it is not surprising that the first atempts at developing special methods for these equations were made by astronomers.

In his treatise on the aurora borealis, C.Stormer (1907) derived a second order differential equation describing the movement of electrical particles in the earth's magnetic field. For his extensive numerical calculations of these trajectories (see the quotation above!) he developed an accurate and simple method as follows: by adding the Taylor series for $y \left( x _ { n } + h \right)$ and $y \left( x _ { n } - h \right)$ we obtain

$$
\prime ( x _ { n } + h ) - 2 y ( x _ { n } ) + y ( x _ { n } - h ) = h ^ { 2 } y \prime \prime ( x _ { n } ) + { \frac { h ^ { 4 } } { 1 2 } } y ^ { ( 4 ) } ( x _ { n } ) + { \frac { h ^ { 6 } } { 3 6 0 } } y ^ { ( 6 ) } ( x _ { n } ) + \cdots
$$

If we insert $y ^ { \prime \prime } ( x _ { n } )$ from the differential equation (10.3) and neglect higher terms, we get

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n }
$$

as a first simple and accurate method, which is sometimes called Stormer's or Encke's method. For greater precision, we replace the higher derivatives of y by central differences of $f$

$$
\begin{array} { l } { { { h ^ { 2 } y ^ { ( 4 ) } ( x _ { n } ) = \Delta ^ { 2 } f _ { n - 1 } - \frac { 1 } { 1 2 } \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot } } } \\ { { { } } } \\ { { { h ^ { 4 } y ^ { ( 6 ) } ( x _ { n } ) = \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot } } } \end{array}
$$

and obtain

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ f _ { n } + \frac { 1 } { 1 2 } \Delta ^ { 2 } f _ { n - 1 } - \frac { 1 } { 2 4 0 } \Delta ^ { 4 } f _ { n - 2 } + \cdot \cdot \cdot \biggr ] .
$$

This formula is not yet very practical, since the diferences of the $f _ { n + 1 }$ $f _ { n + 2 }$ $\Delta ^ { 2 } f _ { n - 1 } { = } \Delta ^ { 2 } f _ { n - 2 } { + } \Delta ^ { 3 } f _ { n - 3 } { + } \Delta ^ { 4 } f _ { n - 4 } )$ onegets foruequstfon damentale dans notre methode...", C.Stormer, 1907)

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } } } \\ { { \displaystyle \quad = h ^ { 2 } f _ { n } + \frac { h ^ { 2 } } { 1 2 } \biggl [ \Delta ^ { 2 } f _ { n - 2 } + \Delta ^ { 3 } f _ { n - 3 } + \Delta ^ { 4 } f _ { n - 4 } - \frac { 1 } { 2 0 } \Delta ^ { 4 } f _ { n - 4 } \biggr ] . } } \end{array}
$$

"Had the Ast. Ges. Essay been entirely free from numerical blunder.s.,.." (P.H. Cowell and A.C.D. Crommelin, 1910)

Some years later Cowell and Crommelin (1910) used the same ideas to investigate the motion of Halley's comet. They considered one additional term in the series (10.6), namely

$$
\frac { 3 1 } { 6 0 4 8 0 } { \Delta } ^ { 6 } f _ { n - 3 } { \approx } \frac { 1 } { 1 9 5 1 } { { \Delta } ^ { 6 } } f _ { n - 3 } \ .
$$

The direct use of (10.6) in its fourth order version

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \Big [ f _ { n } + \frac { 1 } { 1 2 } \Delta ^ { 2 } f _ { n - 1 } \Big ]
$$

was advocated by B. Numerov (1924, 1927): instead of replacing $\Delta ^ { 2 } f _ { n - 1 }$ bysomething explicit,Numerovtries tosolve thisimplicit nonlinear equation directly for yn +1

# Stormer's problem

"Quand on est suffisamment exerce, on calcule environ   
trois points $\left( R \ , z \right)$ par heure."   
(C. Stormer, 1907)

Suppose that an elementary magnet is situated at the origin and that its axis corresponds to the $z$ -axis. The trajectory $( x \left( s \right) , \ y \left( s \right)$ $z \left( s \right) )$ of an electrical particle in this magnetic field is then given as the solution of (Stormer, 1907)

$$
\begin{array} { l } { { \displaystyle x ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( 3 y z z ^ { \prime } - \big ( 3 z ^ { 2 } - r ^ { 2 } \big ) y \big ) } } \\ { { \displaystyle y ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( \big ( 3 z ^ { 2 } - r ^ { 2 } \big ) x ^ { \prime } - 3 x z z ^ { \prime } \big ) } } \\ { { \displaystyle z ^ { \prime \prime } = \frac { 1 } { r ^ { 5 } } \big ( 3 x z y ^ { \prime } - 3 y z x ^ { \prime } \big ) } } \end{array}
$$

where $r ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } .$ Introducing the polar coordinates

$$
x \ = R \cos \phi \qquad y \ = R \sin \phi
$$

the system (10.9) becomes equivalent to

$$
{ \begin{array} { l } { { \boldsymbol { R } } ^ { \prime \prime } = \left( { \frac { 2 \gamma } { R } } + { \frac { R } { r ^ { 3 } } } \right) \left( { \frac { 2 \gamma } { R ^ { 2 } } } + { \frac { 3 R ^ { 2 } } { r ^ { 5 } } } - { \frac { 1 } { r ^ { 3 } } } \right) } \\ { z ^ { \prime \prime } = \left( { \frac { 2 \gamma } { R } } + { \frac { R } { r ^ { 3 } } } \right) { \frac { 3 R z } { r ^ { 5 } } } } \end{array} }
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/cdaafdb2f0e9c44232b62ddaf6095e96a09f43676fe57f2745773f14f40cdf75.jpg)  
Figure 10.1. Solutions of (10.11a) in the $( R \ , \ z )$ -plane

$$
\phi ^ { \prime } = \left( \frac { 2 \gamma } { R } + \frac { R } { r ^ { 3 } } \right) \frac { 1 } { R }
$$

where $\gamma$ is some constant originating from the integration of $\phi ^ { \prime \prime } .$ The two equations (10.11a) constitute a second order differential equation of type (10.3) (observe that $r ^ { 2 } { = } R ^ { 2 } { + } z ^ { 2 }$ ),which can be solved numerically by the methods of this section. $\boldsymbol { \Phi }$ is then obtained by simple integration of (10.11b). Figure 10.1 shows two solutions of the subsystem (10.11a) with Stormer's original initial values R $\scriptstyle 0 ^ { = 0 . 2 5 7 4 5 3 }$ ， ${ z _ { 0 } } ^ { = 0 . 3 1 4 6 8 7 }$ ， $\gamma = - 0 . 5$ ${ r _ { 0 } } ^ { = \sqrt { R _ { \mathrm { ~ 0 ~ } } ^ { 2 } + z _ { 0 } ^ { 2 } } }$ ， $\scriptstyle Q _ { 0 } = 1 - ( 2 \gamma / R _ { \ 0 } + R _ { \ 0 } / r _ { 0 } ^ { \ 3 } ) ^ { 2 }$ $\stackrel { \scriptscriptstyle - } { R _ { \mathrm { \scriptsize ~ 0 } } ^ { \prime } } = \sqrt { \mathscr { Q } _ { \mathrm { \scriptsize ~ 0 } } } \cos u$ ， $z _ { 0 } ^ { \prime } { = } \sqrt { Q _ { 0 } } \sin \imath$ with $u \in \{ 0 , \pi / 4 , \pi , 5 \pi / 4 \}$ Figure 10.2 shows a three-dimensional view in $( x , y , z )$ of the solution with initial values $u = \pi / 4$ and $5 \pi / 4$

# Higher order methods

A generalization of St8rmer's formula can be derived as follows: integrating equation (10.3) twice we obtain

$$
y \left( x + h \right) = y \left( x \right) + h y ^ { \prime } ( x ) + h ^ { 2 } { \intop _ { 0 } ^ { 1 } { \left( 1 - s \right) } f \left( x + s h , y \left( x + s h \right) \right) } d s .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/fcf41424547f24f6378624e43744f0722921f3f2a41d9868297a89adcfc30664.jpg)  
Figure 10.2. Three dimensional view of the solution

In order to eliminate the first derivative of $y \left( x \right)$ we write the same formula with $h$ replaced by $- h$ and add the two expressions:

$$
\begin{array} { r l r } {  { y ( x + h ) - 2 y ( x ) + y ( x - h ) } } & { \mathrm { ( 1 0 . 1 3 ) } } \\ & { } & { = \displaystyle h ^ { 2 } \int ( 1 - s ) [ f ( x + s h , y ( x + s h ) ) + f ( x - s h , y ( x - s h ) ) ] d s . } \\ & { } & \end{array}
$$

As in the derivation of the Adams formulas (Section II.1) we replace the unknown function $f \left( t , y \left( t \right) \right)$ by the interpolation polynomial $p \left( t \right)$ of Formula (1.4). This yields the explicit method

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { k - 1 } \sigma _ { j } \nabla ^ { j } f _ { n }
$$

with coefficien ts $\mathrm { ~ \bf ~ \sigma ~ } _ { j }$ given by

$$
\sigma _ { j } \ = \ ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { } \big ( 1 { - } s \big ) \Bigg [ \left( { - } _ { j } ^ { s } \right) + \ \binom { s } { j } \Bigg ] d s .
$$

See Table 10.1 for their numerical values and Exercise 2 for their computation.

Table 10.1. Coefficients of the method (10.14)   

<table><tr><td>j</td><td>0 1 2</td><td>3 4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>oj</td><td>1 1 0</td><td>1 12 12</td><td>19 3 240 40</td><td>863 12096</td><td>275 4032</td></tr></table>

Special cases of (10.14) are

$$
\begin{array} { r l r } { \mathrm { ~ } } & { = 2 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n } \phantom { \frac { 1 } { 1 2 } } \qquad \mathrm { ~ } ( 1 0 . 1 \times n ) } \\ { \mathrm { ~ } } & { = 3 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 1 3 } { 1 2 } f _ { n } - \frac { 1 } { 6 } f _ { n - 1 } + \frac { 1 } { 1 2 } f _ { n - 2 } \biggr ] \phantom { \frac { 1 } { 1 2 } } } \\ { \mathrm { ~ } } & { = 4 ; } & { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 7 } { 6 } f _ { n } - \frac { 5 } { 1 2 } f _ { n - 1 } + \frac { 1 } { 3 } f _ { n - 2 } - \frac { 1 } { 1 2 } f _ { n - 1 } \biggr ] \phantom { \frac { 1 } { 1 2 } } } \end{array}
$$

Method (10.14) with $k = 5$ is equivalent to Formula (10.7), the method used by Stormer (1907, 1921),and for $k = 6$ one obtains the method used by Cowell and Crom melin (1910). The simplest of these methods ( $k = 1 \AA$ ） has been successfully applied as the basis of an ex trapolation method (Section II.13, Formula (13.32)).

To obtain higher accuracy one can also use the interpolation polynomial $p ^ { * } ( t )$ of (1.7)， which passes through the additional point $( x _ { n + 1 } , f _ { n + 1 } )$ Replacing $f \left( t , y \left( t \right) \right)$ by $\boldsymbol { p } ^ { * } ( t )$ in (10.13） yields the implicit method

$$
\begin{array} { l } { { \mathrm { { } } ^ { \mathrm { { 0 0 } } } } } \\ { { \displaystyle { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \sigma _ { j } ^ { * } \nabla ^ { j } f _ { n + 1 } } . } } \end{array}
$$

The coefficients $\sigma _ { j } ^ { * }$ are defined by

$$
\displaystyle \sigma _ { j } ^ { * } = ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } \left( 1 - s \right) \left[ \left( { - s + 1 \atop j } \right) + \left( { s + 1 \atop j } \right) \right] d s
$$

and are given in Tabie 10.2 for $j \le 6$ 。

For $k = 2$ (and also $k = 3$ ) one obtains the interesting method

$$
y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } \biggl [ \frac { 1 } { 1 2 } f _ { n + 1 } + \frac { 1 0 } { 1 2 } f _ { n } + \frac { 1 } { 1 2 } f _ { n - 1 } \biggr ] \ ,
$$

which is generally attributed to Numerov.

Further methods can be derived by using the ideas of Nyström and Milne for first order equations. With the substitutions $h  2 h$ ， $2 s  s$ and $x \to x - h$ Formula (10.13) becomes

Table 10.2. Coefficients of the implicit method (10.16)   

<table><tr><td>j</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>水） 9</td><td>1 -1</td><td>1 0 12</td><td>-1 240</td><td>-1 240</td><td>-221 60480</td><td>-19 6048</td></tr></table>

$$
\begin{array} { l } { { y \left( x + h \right) - 2 y \left( x - h \right) + y \left( x - 3 h \right) = h ^ { 2 } \displaystyle \int _ { 0 } ^ { 2 } \left( 2 - s \right) } } \\ { { \left[ f \left( x + \left( s - 1 \right) h , y \left( x + \left( s - 1 \right) h \right) \right) + f \left( x - \left( s + 1 \right) h , y \left( x - \left( s + 1 \right) h \right) \right) \right] d , } } \end{array}
$$

If one replaces $\textstyle f \left( t , y \left( t \right) \right)$ by the polynomial $p \left( t \right)$ (or $p ^ { * } ( t )$ ）one obtains new classes of explicit and implicit methods.

# General form ulation

Our next aim is to study stability, consistency and convergence of general linear multistep methods for (10.3). We write them in the form

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } y _ { n + i } \ = h ^ { 2 } \sum _ { i = 0 } ^ { k } \beta _ { i } f \left( x _ { n + i } , y _ { n + i } \right) \ .
$$

The generating polynomials of the coefficients $\alpha _ { i }$ and $\mathsf { \beta } _ { i }$ are again denoted by

$$
{ \sf \rho } ( \xi ) = \sum _ { i = 0 } ^ { k } { { { \bf \alpha } _ { i } } \xi ^ { i } } , \qquad { \bf { \sigma } } ( \xi ) = \sum _ { i = 0 } ^ { k } { { \bf \beta } _ { i } } \xi ^ { i } \mathrm { ~ . ~ }
$$

If we apply Method (10.19) to the initial value problem

$$
y ^ { \prime \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y ^ { \prime } \left( x _ { 0 } \right) = y _ { 0 } ^ { \prime }
$$

it is natural to require that the starting values be consistent with both initial values, i.e. that

$$
\frac { y _ { i } - y _ { 0 } - i h y _ { 0 } ^ { \prime } } { h } \preccurlyeq 0 \quad \mathrm { f o r } \ h  \ 0 , \ i = 0 , 1 , \dots , k - 1 .
$$

# The stability condition

In order to get a feeling for the stability condition which is necessary for convergence, we consider the simple problem

$$
y ^ { \prime \prime } = 0 ~ , ~ y _ { 0 } ^ { } = 0 ~ , ~ y _ { 0 } ^ { \prime } = 0 ~ .
$$

Its numerical solution satisfies a linear difference equation with $\rho \left( \zeta \right)$ as characteristic polynomial. The same considerations as in the proof of Theorem 4.2 show that the following condition is necessary for convergence.

Definition 10.1. Method (10.19) is called stable, if the generating polynomial p(&) satisfies:

i) The roots of $\rho \left( \zeta \right)$ lie on or within the unit circle;   
ii) The multiplicity of the roots on the unit circle is at most two.

# A one-step formulation of Method (10.19)

It is possible to develop a theory analguous to that of Sections III.2 - II.4. This is due to Dahlquist (1959) and can also be found in the book of Henrici (1962). We prefer to rewrite (10.19) in the form (8.4) and to apply directly the results of Section I1.8 and I1.9 (cf. Example 8.7). In order to achieve this goal, we could put $\boldsymbol { u } _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ , which seems to be a natural choice. But then the corresponding matrix S does not satisfy the stability condition of Definition 8.8 because of the double roots of modulus 1. To overcome this difficulty we separate these roots. We split the characteristic polynomial $\rho ( \zeta )$ into

$$
\mathsf { p } ( \boldsymbol { \zeta } ) = \mathsf { p } _ { 1 } ( \boldsymbol { \zeta } ) \cdot \mathsf { p } _ { 2 } ( \boldsymbol { \zeta } )
$$

such that both polynomials

$$
{ \mathsf { \rho } } _ { 1 } ( \zeta ) = \sum _ { i = 0 } ^ { l } { \gamma _ { i } \zeta } ^ { i } ~ , \qquad { \mathsf { \rho } } _ { 2 } ( \zeta ) = \sum _ { i = 0 } ^ { m } { \kappa _ { i } \zeta } ^ { i } \qquad ( l + m = k ~ )
$$

possess only simple roots of modulus 1. Without loss of generality we opume the ned ie (2.10 $m \geq \iota$ tand $\alpha _ { \boldsymbol { k } } = \gamma _ { \boldsymbol { l } } = \kappa _ { m } = 1$ WUtig the shift $\boldsymbol { \mathit { E } }$

$$
\rho ( E ) y _ { n } = h ^ { 2 } \sigma ( E ) f _ { n } .
$$

The main idea is to introduce ${ \rho } _ { 2 } ( E ) y _ { n }$ as a new variable, say $h \nu _ { n }$ ,s0 that the multistep formula becomes equivalent to the system

$$
\mathsf { \rho } _ { 1 } ( E ) \nu _ { n } = h \sigma ( E ) f _ { n } \qquad \mathsf { \rho } _ { 2 } ( E ) y _ { n } = h \nu _ { n } \ .
$$

Introducing the vector

$$
\boldsymbol { u } _ { n } = ( \nu _ { n + l - 1 } , , . . . , \nu _ { n } , y _ { n + m - 1 } , . . . , y _ { n } ) ^ { T }
$$

Formula (10.25) can be written as

$$
u _ { n + 1 } = S u _ { n } + h \Phi ( x _ { n } , u _ { n } , h ) 
$$

whe

$$
\begin{array} { r } { \boldsymbol { \mathsf { \Sigma } } \boldsymbol { \mathsf { \Sigma } } = \left( \begin{array} { c c } { G } & { 0 } \\ { 0 } & { K } \end{array} \right) \ , \quad \boldsymbol { \Phi } ( \boldsymbol { x } _ { n } , \boldsymbol { u } _ { n } , \boldsymbol { h } ) = \left( \begin{array} { c } { \boldsymbol { \Psi } ( \boldsymbol { x } _ { n } , \boldsymbol { u } _ { n } , \boldsymbol { h } ) } \\ { 0 } \\ { \boldsymbol { \Psi } ( \boldsymbol { x } _ { n } ) } \\ { 0 } \\ { \boldsymbol { \Psi } _ { n } } \\ { 0 } \end{array} \right) \ , } \end{array}
$$

The matrices $G$ and $K$ are the companion matrices

$$
\begin{array} { r l r } { \mathrm { ~  ~ \gamma ~ } } & { = \left( \begin{array} { c c c c c } { - \gamma _ { l - 1 } - \gamma _ { l - 2 } } & { \cdots } & { \cdots } & { - \gamma _ { 0 } } \\ { 1 } & { 0 } & { \cdots } & { \cdot } & { 0 } \\ { 1 } & { 1 } & { \cdot } & { \cdot } & { 0 } \\ & & { \cdot } & { \cdot } & { 0 } \\ & & & { \vdots } & { \vdots } \\ & & & { 1 } & { 0 } \end{array} \right) ~ , ~ { \cal K } } & { = \left( \begin{array} { c c c c c } { - \kappa _ { m - 1 } - \kappa _ { m - 2 } } & { \cdots } & { \cdot } & { - \gamma _ { 0 } } & { \cdots } & { 0 } \\ { 1 } & { 0 } & { \cdots } & { \cdot } & { 0 } \\ { 1 } & { 1 } & { \cdots } & { \cdot } & { 0 } \\ & & { \vdots } & & { \vdots } \\ & & & { \vdots } & { \vdots } \\ & & & & { \uparrow } & { 0 } \end{array} \right) } \end{array}
$$

and $\psi = \psi ( x _ { n } , u _ { n } , h )$ is implicitly defined by

$$
\Psi = \sum _ { j = 0 } ^ { k - 1 } { \mathsf { \beta } } _ { j } f ( x _ { n } + j h , y _ { n + j } ) + { \mathsf { \beta } } _ { k } f ( x _ { n } + k h , h ^ { 2 } \Psi - \sum _ { j = 0 } ^ { k - 1 } \alpha _ { j } y _ { n + j } ) .
$$

In this formula $\psi$ is written as a function of $x _ { n }$ ， $( y _ { n + k - 1 } , \dots , y _ { n } )$ and $h$ But the second relation of (10.25) shows that each value yn +k-1' \*\* , $y _ { n + m }$ can be expressd as alinear combination of the elements of $u _ { n }$ Therefore $\Psi$ is in fact a function of $( x _ { n } , u _ { n } , h )$ ·

Formula (10.26) defines our forward step procedure. The corresponding starting procedure is

$$
\boldsymbol { \Phi } ( h ) = \bigl ( \nu _ { l - 1 } , \ldots , \nu _ { 0 } , y _ { m - 1 } , \ldots , y _ { 0 } \bigr ) ^ { T }
$$

which,by (10.25)，is uniquely determined by $( y _ { k - 1 } , \dots , y _ { 0 } ) ^ { T }$ As correct value function we have

$$
\begin{array} { r } { z \left( x , h \right) = \left( \displaystyle \frac { 1 } { h } \mathsf { \rho } _ { 2 } ( E ) y \left( x + ( l - 1 ) h \right) , \ldots , \displaystyle \frac { 1 } { h } \mathsf { \rho } _ { 2 } ( E ) y \left( x \right) , \right) } \\ { y \left( x + ( m - 1 ) h , \ldots , y \left( x \right) \right) ^ { T } \ . } \end{array}
$$

By our choice of ${ \sf p } _ { 1 } ( \boldsymbol { \zeta } )$ and ${ \mathfrak { p } } _ { 2 } ( \zeta )$ (both have only simple roots of modulus 1） the matrices $G$ and $K$ are power bounded. Therefore S is also power bounded and Method (10.26) is stable in the sense of Definition 8.8.

# Consistency and con vergence

We search for conditions on the parameters $\alpha _ { i }$ and $\beta _ { i }$ , such that the method (10.26) is consistent of order $p$ (in the sense of Lemma 8.11). Let us start with the error in the initial values

$$
d _ { 0 } = z ( x _ { 0 } , h ) - \phi ( h ) .
$$

The first l components of this vector are

$$
\qquad \neg \circ _ { 2 } ( E ) y ( x _ { j } ) - \nu _ { j } = { \frac { 1 } { h } } \sum _ { i = 0 } ^ { m } \kappa _ { i } \left( y ( x _ { i + j } ) - y _ { i + j } \right) \qquad j = 0 , \dots , l - 1
$$

and the last m components are just

$$
y ( x _ { j } ) - y _ { j } \qquad j = 0 , . . . , m - 1 .
$$

We see that a sufficient condition for $d _ { 0 } { = } 0 ( h ^ { p } )$ to hold is

$$
y \left( x _ { j } \right) \sim y _ { j } = { \bf O } ( h ^ { p + 1 } ) \mathrm { f o r } j = 0 , 1 , \ldots , k - 1 .
$$

Consider next the local error at xn ,

$$
d _ { n + 1 } = z \big ( x _ { n } + h , h \big ) - S z \big ( x _ { n } , h \big ) - h \Phi \big ( x _ { n } , z \big ( x _ { n } , h \big ) , h \big ) .
$$

All com ponents of $d _ { n + 1 }$ vanish except the first, which equals

$$
d _ { n + 1 } ^ { ( 1 ) } = { \frac { 1 } { h } } \mathsf { p } ( E ) y ( x _ { n } ) - h \psi ( x _ { n } , z ( x _ { n } , h ) , h ) ~ .
$$

As in Section I1.2 we introduce the linear difference operator

$$
\begin{array} { l } { { L \left( y , x , h \right) = \rho ( E ) y \left( x \right) - h ^ { 2 } \sigma ( E ) y ^ { \prime \prime } ( x ) } } \\ { { \ } } \\ { { \displaystyle = \sum _ { i = 0 } ^ { k } \left( \alpha _ { i } y \left( x + i h \right) - h ^ { 2 } \beta _ { i } y ^ { \prime \prime } ( x + i h ) \right) . } } \end{array}
$$

Using Formula (10.28), an application of the mean value theorem yields

$$
d _ { n + 1 } ^ { ( 1 ) } = \frac { 1 } { h } L ( y , x _ { n } , h ) + h ^ { 2 } \mathsf { \& } f ^ { \prime } ( x _ { n + k } , \eta ) \cdot d _ { n + 1 } ^ { ( 1 ) }
$$

with $\mathbf { \boldsymbol { v } }$ as in Lemma 2.2. We therefore have

$$
d _ { n + 1 } = { \bf O } ( h ^ { p + 1 } ) \iff L \left( y , x _ { n } , h \right) = { \bf O } ( h ^ { p + 2 } ) \ .
$$

The Convergence Theorem 8.13 now yields

Theorem 10.2. Suppose that the method (10.19) is stable, that the starting values satisfy (10.29) and that

$$
L \left( y , x , h \right) = 0 ( h ^ { p + 2 } )
$$

for all sufficiently smooth functions $y \left( x \right)$ . Then the method (10.19) converges of order $p$ ,i.e.

$$
\| ~ y ( x _ { n } ) - y _ { n } ~ \| ~ \leq ~ C h ^ { p } ~ f o r ~ O \leq h n \leq C o n s t .
$$

NED.

A useful criterion for the verification of (10.31) is given by

Theorem 10.3. The multistep method (10.19) satisfies (10.31) if and only if the following equivalent conditions hold:

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } = 0 \ , \sum _ { i = 0 } ^ { k } i \alpha _ { i } = 0
$$

$$
\begin{array} { l c l } { { a n d } } & { { \displaystyle \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { q } = q ( q { - } 1 ) \sum _ { i = 0 } ^ { k } 8 _ { i } i ^ { q - 2 } } } & { { f o r } } & { { q = 2 , \ldots , p + 1 \ , } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { } } \\ { { \displaystyle \rho ( e ^ { h } ) - h ^ { 2 } \sigma ( e ^ { h } ) = 0 ( h ^ { p + 2 } ) } } & { { f o r } } & { { h  0 \ , } } \\ { { \displaystyle \frac { \rho ( \zeta ) } { ( \log \zeta ) ^ { 2 } } - \sigma ( \zeta ) = \mathbf { 0 } ( ( \zeta { - } 1 ) ^ { p } ) } } & { { f o r } } & { { \zeta {  } 1 \ . } } \end{array}
$$

The proof is the same as for Theorem 2.4 and hence omitted. NED.

Remarks. 1. $\zeta _ { 1 } = 1$ is necessarily a root of $\rho ( \zeta )$ of multiplicity two. Therefore the polynomials ${ \boldsymbol { \rho } } _ { 1 } , ~ { \boldsymbol { \rho } } _ { 2 }$ of (10.24) satisfy ${ \boldsymbol { \rho } } _ { 1 } ( 1 ) = 0$ and ${ \mathsf p } _ { 2 } ( 1 ) = 0$ . The correct value function $z \left( x , h \right)$ thus has a limit for $h  0$ ：

2. As for Adams methods one easily verifies that the method (10.14) is of order $k$ , and (10.16) of order $k + 1$

# Asym ptotic formula for the global error

Assume that the method (10.19) is stable and consistent of order $p \cdot$ The local truncation error of (10.26) is then given by

$$
d _ { n + 1 } = e _ { 1 } h ^ { p + 1 } C _ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } ) + \mathbf { O } ( h ^ { p + 2 } )
$$

with

$$
C _ { p + 2 } = { \frac { 1 } { ( p + 2 ) ! } } \sum _ { i = 0 } ^ { k } \left( { \alpha _ { i } } ^ { p + 2 } - ( p + 2 ) ( p + 1 ) { \beta _ { i } } ^ { p } \right) \ .
$$

Formula (10.32) can be verified by developing $L \left( y , x _ { n } , h \right)$ into a Taylor series in (10.30). An application of Theorem 9.1 (if 1 is the only root of modulus 1 of $\rho ( \zeta )$ ) or of Theorem 9.2 shows that the global error of Method (10.26) is of the form

$$
u _ { h } ( x ) - z ( x , h ) = e ( x ) h ^ { p } + \mathbf { O } ( h ^ { p + 1 } )
$$

where $e \left( x \right)$ is the solution of

$$
e ^ { \prime } ( x ) = E \frac { \partial \Phi } { \partial u } \big ( x , z ( x , 0 ) , 0 \big ) e ( x ) - E e _ { 1 } \cdot C _ { p + 2 } y ^ { ( p + 2 ) } ( x ) \ .
$$

Here $E$ is the matrix defined in (8.12). Since no $h ^ { p }$ -term is present in the local error (10.32),it follows from (9.16) that $e \left( x \right) { = } E e \left( x \right)$ Therefore (see Exercise 4a) this function can be written as

$$
e \left( x \right) = { \binom { \gamma ( x ) \mathbb { 1 } } { \kappa ( x ) \mathbb { 1 } } } .
$$

A straightforward calculation of $\frac { \partial \Phi } { \partial \boldsymbol { u } } ( \boldsymbol { x } , z \left( \boldsymbol { x } , 0 \right) , 0 )$ and $E e _ { 1 }$ (fo1

details see Exercise 4) shows that (10.33) becomes equivalent to the system

$$
\begin{array} { l } { { \gamma ^ { \prime } ( x ) = \displaystyle \frac { \sigma ( 1 ) } { \rho _ { 1 } ^ { \prime } ( 1 ) } \frac { \partial f } { \partial y } ( x , y ( x ) ) \kappa ( x ) - \displaystyle \frac { C _ { p + 2 } } { \rho _ { 1 } ^ { \prime } ( 1 ) } y ^ { ( p + 2 ) } ( x ) } } \\ { { \kappa ^ { \prime } ( x ) = \displaystyle \frac { 1 } { \rho _ { 2 } ^ { \prime } ( 1 ) } \gamma ( x ) . } } \end{array}
$$

Differentiating (10.34b) and inserting $\gamma ^ { \prime } ( x )$ from (10.34a), we finally obtain

$$
\begin{array} { r } { \kappa ^ { \prime \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) \ltimes ( x ) - C y ^ { ( p + 2 ) } ( x ) } \end{array}
$$

with

$$
C \ = \ { \frac { C _ { p + 2 } } { \sigma ( 1 ) } } \ ,
$$

Here we have used the relation $\sigma ( 1 ) { = } \rho _ { 1 } ^ { \prime } ( 1 ) { \cdot } \rho _ { 2 } ^ { \prime } ( 1 )$ which is an immediate consequence of (10.23) and the assumption that the order of the method is at least 1. The constant $c$ in (10.35) is called the error constant of Method (10.19). It plays the same role as (2.13) for first order equations.

Since the last component of the vector $u _ { n }$ is $y _ { n }$ we have the desired result

$$
y _ { n } - y ( x _ { n } ) = \kappa ( x _ { n } ) h ^ { p } +  { \mathbf { O } } ( h ^ { p + 1 } )
$$

with $\kappa ( x )$ satisfying (10.35). Further terms in the asymptotic expansion of the global error can also be obtained by specializing the results of II.9.

# An order barrier for stable methods (10.19)

It is a natural task to look for stable multistep methods (10.19) of highest possible order.

Theorem 10.4. The order p of a stable linear multistep method (10.19) satisfies

$p ~ \leq ~ k + 2$ if k is even, $p \ \leq \ k + 1$ if k is odd.

Theorem 10.5. Stable multistep methods (10.19) of order k +2 are symmetric, i.e.

$$
\alpha _ { j } = \alpha _ { k - j } , \qquad \beta _ { j } = \beta _ { k - j } f o r \ { a l l } j .
$$

The proofs of these two theorems are similar to those of Theorems 3.5 and 3.9. We omit them and refer the reader to the original article of Dahlquist (1959) or to Henrici (1962).

# Rounding errors

Let us briefly discuss a further advantage of the formulation (10.26). Among the many possibilities of implementing a multistep method, consider the following two:

i) Store the values $( y _ { n + k - 1 } , \dots , y _ { n } )$ ） and compute $y _ { n + k }$ directly with Formula (10.19).   
ii) Store $u _ { n }$ and make use of Formula (10.26). We call this a stabilization of (10.19).

Both processes are mathematically equivalent. However, from a computational point of view the two methods are different. For small h the recurrence relation (10.19) is unstable (due to the roots of multiplicity two on the unit circle), whereas the recursion (10.26) is stable (S is power bounded). For an illustration of this difference we apply Stormer's formula (10.14') with $k = 4$ to the problem $y \ ^ { \prime \prime } { = } { - } y$ with $y \left( x \right) = \sin x$ as exact solution. We take the starting values on the exact solution and choose the step size $h = 0 . 0 1$ to keep the truncation error smaller than the rounding errors (single precision with EPSMACH $= 1 . 5 \cdot E - 8 )$ . Figure 10.3 shows the absolute value of the global error for both implementations. The error of the stabilized version is seen to be smaller by a factor of 100. The downward peaks are due to sign-changes in the global error.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/f2418783d56bf70a1200b855c5d2ce821a52e88eeab7b99560e13b97f60eb9f0.jpg)  
Figure 10.3. Rounding errors for the two implementations of Stormer's formula (10.14') with $k = 4$

# Exercises

1. Compute the solution of St8rmer's problem (10.11a) with one ol the methods of this section.

2. a) Show that the generating functions of the coefficients $\boldsymbol { \sigma } _ { i }$ and $\sigma _ { j } ^ { * }$ (defined in (10.15) and (10.17))

$$
S \left( t \right) = \sum _ { j = 0 } ^ { \infty } { { \sigma _ { j } } t ^ { j } } \mathrm { ~ , ~ } \quad S ^ { * } ( t ) = \sum _ { j = 0 } ^ { \infty } { { \sigma _ { j } ^ { * } } t ^ { j } }
$$

satisfy

$$
S ( t ) = \sqrt { \frac { t } { \log ( 1 - t ) } } ) ^ { 2 } \frac { 1 } { 1 - t } S ^ { * } ( t ) = ( \frac { t } { \log ( 1 - t ) } ) ^ { 2 } ,
$$

b) Com pute the coefficients $d _ { j }$ of

$$
\sum _ { j = 0 } ^ { \infty } d _ { j } t ^ { j } = \left( { \frac { \log ( 1 - t ) } { t } } \right) ^ { 2 } = \left( 1 + { \frac { t } { 2 } } + { \frac { t ^ { 2 } } { 3 } } + { \frac { t ^ { 3 } } { 4 } } + \cdot \cdot \cdot \right) ^ { 2 }
$$

and derive a recurrence relation for the $\sigma _ { j }$ and $\sigma _ { j } ^ { * }$

c) Prove that

$$
{ \sigma } _ { j } ^ { * } = { \sigma } _ { j } - { \sigma } _ { j - 1 } .
$$

3. Let p(&) be a polynomial of degree k which has 1 as root of mul-tiplicity 2. Then there exists a unique $\sigma \left( \zeta \right)$ such that the corresponding method is of order $k + 1$

4. Consider the method (10.26) and, for simplicity， assume the differential equation to be a scalar one.

a) For any vector $w$ in $\mathbb { R } ^ { k }$ the im age vector $E w$ ,with $E$ given by (8.12), satisfies

$$
E w \ = \ { \binom { \gamma \mathbb { 1 } } { | \kappa \mathbb { 1 } } }
$$

where $\gamma , \kappa$ are real numbers and 1 is the vector with all elements equal to 1. The dimensions of $\gamma \mathbf { 1 }$ and κll are $l$ and $m$ ,respectively.

b) Verify that fo

$$
\begin{array} { r l } & { \textup { r } e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T } } \\ & { \boldsymbol { E } \left( { \boldsymbol { \alpha } \boldsymbol { e } _ { 1 } } \right) \ = \left( \begin{array} { l } { ( \boldsymbol { \alpha } / \rho _ { 1 } ^ { \prime } ( 1 ) ) \Im } \\ { ( \beta / \rho _ { 2 } ^ { \prime } ( 1 ) ) \Im } \end{array} \right) \ . } \end{array}
$$

c) Show that

$$
\begin{array} { r } { { \cal E } \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \left( { \gamma \bf 1 } \right) = \left( { \bf \Psi } \left( \frac { \sigma ( 1 ) } { \rho _ { 1 } ^ { \prime } ( 1 ) } \right) \bf { \Psi } \times { \bf \ I } \right) } \\ { { \cal E } \frac { \partial \Phi } { \partial u } ( x , z ( x , 0 ) , 0 ) \left( { \gamma \bf 1 } \right) = \left( { \bf \Psi } \left( \frac { 1 } { \rho _ { 2 } ^ { \prime } ( 1 ) } \right) \bf { \Psi } \times { \bf \Psi } \right) } \end{array} .
$$

Hint. With $Y _ { n } { = } ( y _ { n + k - 1 } , { \dots } , y _ { n } ) ^ { T }$ the formula (10.28) expresses $\psi$ as a function of $( x _ { n } , Y _ { n } , h )$ The vectors $Y _ { n }$ and $u _ { n }$ are related by

$$
{ K Y _ { n } } = L { \ * u _ { n } } + \mathbf { O } ( h )
$$

where

$$
\begin{array} { r l r } { K } & { = } & { \left( \begin{array} { l l l l l l } { \kappa _ { m } } & { \hdots } & { \hdots } & { \kappa _ { 0 } } & & & \\ & { \ddots } & & & { \ddots } & \\ & & & & { \ddots } & \\ & & { \kappa _ { m } } & { \hdots } & { \hdots } & { \kappa _ { 0 } } \\ & & & { 1 } & & \\ & & & { \ddots } & \\ & & & & { 1 } \end{array} \right) \qquad L = \left( \begin{array} { l l l l l l } { \hdots } & & { 0 } & & \\ & & { 0 } & \\ & & & & \\ & & & { 1 } & \\ & & & & { \ddots } \\ & & & & & { 1 } \end{array} \right) \qquad . } \end{array}
$$

Usethechain rulefor thecomputationof $\frac { \partial \Psi } { \partial u } ( x , z ( x , 0 ) , 0 ) ,$ See also Exercise 2 of Section III.4 and Exercise 1 of Section III.9.

5. Compute the error constant (10.36) for the methods (10.14) and (10.16).

$\sigma _ { k }$ and ${ \mathfrak {sigma } } _ { k + 1 } ^ { * } ,$

# APPENDIX. FORTRAN CODES

... but the software is in various states of development from experimental (a euphemism for badly written) to what we might cal...   
(W. Gear 1985)

The following Fortran codes have been developped for our numerical computations. They can be obtained from the Authors (Section de Mathematiques, Case Postale 240, CH-1211 Geneve 24, Switzerland) on an IBM diskette. Please send 15 Swiss Franks.

# 1. Dopri5

Explicit Runge-Kutta code based on the formulas of Dormand and Prince with step size control (see Table 4.6 of Section I.4). Best method for low tolerances $1 0 ^ { - 4 }$ to $1 0 ^ { - 7 }$ ）.

SUBROUTINE DOPRI5(N,FCN,X,Y,XEND,EPS,HMAX,H)   
C   
C NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDER   
C ORDINARY DIFFERENTIAL EQUATIONS $\mathbf { Y } ^ { \mathrm { ~ 5 ~ } } = \mathbb { F }$ (X,Y).   
C THIS IS AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER (4)5   
C DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.   
C C.F.SRCTION II.4   
C   
C INPUT PARAMETERS   
C   
C N DIMENSION OF THE SYSTEM （N.LE.51）   
C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THE   
C FIRST DERIVATIVE F(X,Y):   
C SUBROUTINE FCN(N,X,Y,F)   
C RBAL\*4 X,Y(N),F(N)   
C F(1)=.. BTC.   
C X INITIAL X-VALUE   
C XBND FINAL X-VALUE (XRND-X POSITIVE OR NEGATIVE)   
C Y(N) INITIAL VALUES FOR Y   
C BPS LOCAL TOLBRANCE   
C HMAX MAXIMAL STEPSIZE   
C H INITIAL STEPSIZE GUESS   
C   
C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
EXTERNAL SUBROUTINE (TO BR SUPPLIED BY THE USER) SOLOUS THIS SUBROUTINE IS CALLED AFTER EVERY SUCCESSFULLY COMPUTED STBP （AND THE INITIAL VALUE): SUBROUTINE SOLOUS (NR,X,Y,N) RBAL\*4 X,Y(N) FURNISHES THE SOLUTION Y AT THE NR-TH GRID-POINT X (THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTION IS NOT DESIRRD AT THE INTERMEDIATE POINTS. REAL\*4 K1(51),K2(51),K3(51),K4(51),K5(51),Y1(51),Y(N) LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CAN BE USED FOR STATISTICS   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STEPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NREJCT NUMBER OF REJECTED STEPS DATA NMAX/3000/,UROUND/5.E-8/   
C NMAX MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.+UROUND>1.   
C (TO BE ADAPTED BY THE USER) POSNEG=SIGN(1.,XEND-X)   
C INITIAL PRRPARATIONS HMAX=ABS(HMAX) H=AMIN1(AMAX1(1.E-4,ABS(H)),HMAX) H=SIGN(H,POSNEG) EPS=AMAX1(BPS,7.\*UROUND) REJECT=.FALSE. NACCPT=0 NRBJCT=0 NFCN=1 NSTEP=0 CALL SOLOUS(NACCPT+1,X,Y,N) CALl FCN(N,X,Y,K1）   
C BASIC INTEGRATION STEP 1 IF(NSTEP.GT.NMAX.OR.X+.1\*H.EQ.X)GOTO 79 IF（（X-XEND）\*POSNEG+UROUND.GT.O.） RETURN IF(（X+H-XEND)\*POSNEG.GT.O.)H=XEND-X NSTRP=NSTEP+1   
C THE FIRST 6 STAGES D0 22 I=1,N 22 Y1(I)=Y(I)+H\*.2\*K1(I) CALL FCN(N,X+.2\*H,Y1,K2) DO 23 I=1,N 23 Y1(I)=Y(I)+H\*((3./40.)\*K1(I)+(9./40.)\*K2(I)) CALL FCN(N,X+.3\*H,Y1,K3) DO 24 I=1,N 24 Y1(I)=Y(I)+H\*((44./45.)\*K1(I)-(56./15.)\*K2(I)+(32./9.)\*K3(I)) CALL FCN(N,X+.8\*H,Y1,K4) D0 25 I=1,N 25Y1(I)=Y(I)+H\*((19372./6561.)\*K1(I)-(25360./2187.)\*K2(I) &+(64448./6561.)\*K3(I)-(212./729.)\*K4（I)) CALL FCN(N,X+(8./9.)\*H,Y1,K5) D0 26 I=1,N 26Y1(I)=Y(I)+H\*((9017./3168.)\*K1(I)-(355./33.)\*K2(I) & +(46732./5247.)\*K3(I)+(49./176.)\*K4(I)-(5103./18656.)\*K5(I) XPH=X+H CALL FCN(N,XPH,Y1,K2) DO 27 I=1,N 27Y1(I)=Y(I)+H\*((35./384.)\*K1(I)+(500./1113.)\*K3(I) & +(125./192.)\*K4(I)-(2187./6784.)\*K5(I)+(11./84.)\*K2(I))   
C COMPUTE INTERMEDIATE SUM TO SAVE MEMORY D0 61 I=1,N 61K2(I)=(71./57600.)\*K1(I)-(71./16695.)\*K3(I) & +(71./1920.)\*K4(I)-(17253./339200.)\*K5(I)+(22./525.)\*K2(I)   
C THE LAST STAGE CALL FCN(N,XPH,Yl,K3) D0 28 I=1,N 28 $\mathrm { ~ K ~ 4 ~ ( ~ I ~ ) ~ } = ( \mathrm { ~ K ~ 2 ~ ( ~ I ~ ) ~ } - ( \mathrm { ~ 1 ~ } , / 4 0 ~ . ~ ) * \mathrm { ~ K ~ 3 ~ ( ~ I ~ ) ~ } ) * \mathrm { ~ H ~ }$ NFCN=NFCN+6   
C ERROR ESTIMATION ERR=0. D0 41 I=1,N DENOM=AMAX1(1.E-5,ABS(Y1(I)),ABS(Y(I)）,2.\*UROUND/EPS) 41 BRR=BRR+(K4(I)/DENOM)\*\*2 BRR=SQRT(ERR/FLOAT(N)) C COMPUTATION OF HNEW C WE REQUIRE .2<=HNEW/H<=10. FAC=AMAX1(.1,AMIN1(5.,(ERR/BPS)\*\*(1./5.)/.9)) HNBW=H/FAC IF(ERR.LE.RPS)THEN C 11i STEP IS ACCEPTED NACCPT=NACCPT+1 DO 44 I=1,N K1(I)=K3(I)   
44 Y(I)=Y1(I) X=XPH CALL SOLOUS(NACCPT+1,X,Y,N) IF（ABS(HNEW).GT.HMAX)HNEW=POSNEG\*HMAX IF(REJECT)HNEW=POSNEG\*AMINI(ABS(HNEW),ABS(H)) REJECT=.FALSE. ELSE C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1)NREJCT=NREJCT+1 END IF H=HNEW GOTO 1 C FAIL EXIT   
79 WRITE(6,979) X   
979 FORMAT(' EXIT OF DOPRI5 AT X=',E11.4) RETURN END C SUBROUTINE SOLOUS(NRPNTS,X,Y,N) REAL\*4 Y(N) RETURN END

# 2. Dopri8

Explicit Runge-Kutta code of high order based on the formulas of Prince and Dorm and with step size control (Table 6.4 of Section I1.6). It is written in double precision and preferable for tolerances between approximately $1 0 ^ { - 7 }$ and $1 0 ^ { - 1 3 }$ Do not use it below $1 0 ^ { - 1 6 }$

SUBROUTINE DOPRI8(N,FCN,X,Y,X&ND,EPS,HMAX,H)NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERORDINARY DIFFERENTIAL EQUATIONS Y'=F(X,Y).THIS IS AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER （7)8DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.C.F. SECTION II.6INPUT PARAMETERSN DIMENSION OF THE SYSTEM （N.LE.51)FCN NAME （EXTERNAL) OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*8 X,Y(N),F(N)F(1)=.. ETC.X INITIAL X-VALUEXEND FINAL X-VALUE (XEND-X POSITIVE OR NRGATIVE)Y(N) INITIAL VALUES FOR YBPS LOCAL TOLERANCEHMA X MAXIMAL STEPSIZEH INITIAL STEPSIZE GUESS

C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
C   
C EXTRRNAL SUBROUTINE (TO BR SUPPLIED BY THE USER)   
C   
C SOLOUT THIS SUBROUTINE IS CALLED AFTER EVERY   
C SUCCESSFULLY COMPUTED STEP (AND THB INITIAL VALUE): SUBROUTINE SOLOUT (NR,X,Y,N) REAL\*8 X,Y(N) FURNISHES THE SOLUTION Y AT THE NR-TH   
GRID-POINT X (THR INITIAL VALUB IS CON-SIDBRED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE，IF THR SOLUTION IS NOT DESIRED AT THE INTERMBDIATE POINTS.   
C IMPLICIT RRAL\*8 （A-H,O-Z) REAL\*8 Kl(51),K2(51),K3(51),K4(51),K5(51),K6(51),K7(51) \*,Y(N),Y1(51) LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CAN BE USED FOR STATISTICS   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STRPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NRBJCT NUMBER OF REJRCTED STEPS COMM0N/CoEF/C2,C3,C4,C5,c6,C7,c8,C9,C10,C11,C12,C13, &A21,A31,A32,A41,A43,A51,A53,A54,A61,A64,A65,A71,A74,A75,A76, &A81,A84,A85,A86,A87,A91,A94,A95,A96,A97,A98,A101,A104,A105,A106, &A107,A108,A109,A111,A114,A115,A116,A117,A118,A119,A1110,A121, &A124,A125,A126,A127,A128,A129,A1210,A1211,A131,A134,A135,A136, &A137,A138,A139,A1310,A1311,B1,B6,B7,B8,B9,B10,BI1,B12,B13, &BH1,BH6,BH7,BH8,BH9,BH1O,BH11,BH12 DATA NMAX/2000/,UROUND/1.73D-18/   
C NMAX MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.D0   
C (TO BE ADAPTED BY THE USER) CALL COEFST POSNEG=DSIGN(1.DO,XEND-X)   
C INITIAL PREPARATIONS HMAX=DABS(HMAX) H=DMIN1(DMAX1(1.D-1O,DABS(H)),HMAX) H=DSIGN(H,POSNEG) EPS=DMAX1(EPS,13.DO\*UROUND) REJECT=.FALSE. NACCPT=0 NREJCT=0 NFCN=0 NSTEP=0 CALL SOLOUT(NACCPT+1,X,Y,N)   
C BASIC INTEGRATION STEP 1 IF(NSTEP.GT.NMAX.OR.X+.03DO\*H.EQ.X)GOTO 79 IF((X-XEND)\*POSNEG+UROUND.GT.O.DO) RETURN IF((X+H-XEND)\*POSNBG.GT.O.DO)H=XEND-X CALL FCN(N,X,Y,K1) 2 CONTINUE NSTEP=NSTEP+1   
C THE FIRST 9 STAGES D0 22 I=1,N 22 Y1(I)=Y(I)+H\*A21\*K1(I) CALL FCN(N,X+C2\*H,Y1,K2) DO 23 I=1,N 23 Y1(I)=Y(I)+H\*(A31\*K1(I)+A32\*K2(I)) CALL FCN(N,X+C3\*H,Y1,K3) D0 24 I=1,N 24 Y1(I)=Y(I)+H\*(A41\*K1(I)+A43\*K3(I)) D0 25 I=1,N 25 Y1(I)=Y(I)+H\*(A51\*K1(I)+A53\*K3(I)+A54\*K4(I)) CALL FCN(N,X+C5\*H,Y1,K5) DO 26 I=1,N 26 Yl(I)=Y(I)+H\*(A61\*K1(I)+A64\*K4(I)+A65\*K5(I)) CALL FCN(N,X+C6\*H,Y1,K6) DO 27 I=1,N 27 Y1(I)=Y(I)+H\*(A71\*K1(I)+A74\*K4(I)+A75\*K5(I)+A76\*K6(I)) CALL FCN(N,X+C7\*H,Y1,K7) DO 28 I=1,N 28 Y1(I)=Y(I)+H\*(A81\*K1(I)+A84\*K4(I)+A85\*K5(I)+A86\*K6(I)+A87\*K7 CALL FCN(N,X+C8\*H,Y1,K2) DO 29 I=1,N 29 Y1(I)=Y(I)+H\*(A91\*K1(I)+A94\*K4(I)+A95\*K5(I)+A96\*K6(I)+A97\*K7. &+A98\*K2（I)) CALL FCN(N,X+C9\*H,Y1,K3) DO 30 I=1,N 30 Y1(I)=Y(I)+H\*(A101\*K1(I)+A104\*K4(I)+A105\*K5(I)+A106\*K6(I) &\~ +A107\*K7(I)+A108\*K2（I)+A109\*K3(I）)   
C COMPUTE INTERMEDIATE SUMS TO SAVE MEMORY DO 61 I=1,N Y11S=A111\*K1(I)+A114\*K4(I)+A115\*K5(I)+A116\*K6(I)+A117\*K7(I) & +A118\*K2（I)+A119\*K3（I） Y12S=A121\*K1(I)+A124\*K4(I)+A125\*K5(I)+A126\*K6(I)+A127\*K7(I) & +A128\*K2(I)+A129\*K3(I) K4(I)=A131\*K1(I)+A134\*K4(I)+A135\*K5(I)+A136\*K6(I)+A137\*K7(I） & +A138\*K2(I)+A139\*K3（I) K5(I)=B1\*K1(I)+B6\*K6(I)+B7\*K7(I)+B8\*K2(I)+B9\*K3(I) K6(I)=BH1\*K1(I)+BH6\*K6(I)+BH7\*K7(I)+BH8\*K2(I)+BH9\*K3（I) K2(I)=Y11S 61 K3(I)=Y12S   
C THE LAST 4 STAGES CALL FCN(N,X+C1O\*H,Yl,K7) D0 31 I=1,N 31 Y1(I)=Y(I)+H\*(K2(I)+A1110\*K7(I)) CALL FCN(N,X+C1I\*H,Yl,K2） XPH=X+H DO 32 I=1,N 32 Y1(I)=Y(I)+H\*(K3(I)+A1210\*K7(I)+A1211\*K2(I)) CALL FCN(N,XPH,Y1,K3) D0 33 I=1,N 33 Y1(I)=Y(I)+H\*(K4(I)+A1310\*K7(I)+A1311\*K2(I)) CALL FCN(N,XPH,Yl,K4) NFCN=NFCN+13 DO 35 I=1,N K5(I)=Y(I)+H\*(K5(I)+B10\*K7(I)+B11\*K2(I)+B12\*K3(I)+B13\*K4(I)) 35K6(I)=Y(I)+H\*(K6(I)+BH10\*K7(I)+BH11\*K2(I)+BH12\*K3(I))   
c BRROR ESTIMATION BRR=0.D0 D0 41 I=1,N DENOM=DMAX1(1.D-6,DABS(K5(I)),DABS(Y(I)),2.DO\*UROUND/BPS) 41 BRR=ERR+((K5(I)-K6(I))/DENOM)\*\*2 BRR=DSQRT(ERR/DFLOAT(N))   
C COMPUTATION OF HNEW   
C WE REQUIRE .333<=HNEW/W<=6. FAC=DMAX1((1.D0/6.DO),DMIN1(3.DO,(ERR/BPS)\*\*(1.D0/8.DO)/.9D0 HNEW=H/FAC IF(ERR.GT.EPS)GOTO 51   
C STEP IS ACCEPTED NACCPT=NACCPT+1 D0 44 I=1,N 44 Y(I)=K5(I) X=XPH CALL SOLOUT(NACCPT+1,X,Y,N) IF（DABS(HNEW) .GT.HMAX) HNEW=POSNEG\*HMAX IF(REJECT) HNEW=POSNEG\*DMINI(DABS(HNEW),DABS(H)) H=HNEW GOTO 1 STEP IS RRJECTED   
51 REJECT=.TRUE. H=HNEW IF(NACCPT.GE.1)NREJCT=NREJCT+1 NFCN=NFCN-1 GOTO 2 FAIL EXIT   
79 WRITE(6,979)X   
379 FORMAT(' EXIT OF DOPRI8 AT X=',D16. RETURN END SUBROUTINE COEFST THIS SUBROUTINE SETS THE COEFFICIEN' METHOD OF ORDER 8 WITH ERROR BSTIMA IMPLICIT REAL\*8 （A-H,O-Z) COMM0N/COBF/C2,C3,C4,C5,C6,C7,C8,c9 &A21,A31,A32,A41,A43,A51,A53,A54,A6 & A81,A84,A85,A86,A87,A91,A94,A95,A9 & A107,A108,A109,A111,A114,A115,A116 & A124,A125,A126,A127,A128,A129,A121( & A137,A138,A139,A1310,A1311,B1,B6,B‘ & BH1,BH6,BH7,BH8,BH9,BH1O,BH11,BH12 C2=1.D0/18.D0 C3=1.D0/12.D0 C4=1.D0/8.D0 C5=5.D0/16.D0 C6=3.D0/8.D0 C7=59.D0/400.D0 C8=93.D0/200.D0 C9=5490023248.D0/9719169821.D0 C10=13.D0/20.D0 C11=1201146811.D0/1299019798.D0 C12=1.D0 C13=1.D0 A21=C2 A31=1.D0/48.D0 A32=1.D0/16.D0 A41=1.D0/32.D0 A43=3.D0/32.D0 A51=5.D0/16.D0 A53=-75.D0/64.D0 A54=-A53 A61=3.D0/80.D0 A64=3.D0/16.D0 A65=3.D0/20.D0 A71=29443841.D0/614563906.D0 A74=77736538.D0/692538347.D0 A75=-28693883.D0/1125.D6 A76=23124283.D0/18.D8 A81=16016141.D0/946692911.D0 A84=61564180.D0/158732637.D0 A85=22789713.D0/633445777.D0 A86=545815736.D0/2771057229.D0 A87=-180193667.D0/1043307555.D0 A91=39632708.D0/573691083.D0 A94=-433636366.D0/683701615.D0 A95=-421739975.D0/2616292301.D0 A96=100302831.D0/723423059.D0 A97=790204164.D0/839813087.D0 A98=800635310.D0/3783071287.D0 A101=246121993.D0/1340847787.D0 A104=-37695042795.D0/15268766246.D0 A105=-309121744.D0/1061227803.D0

A106=-12992083.D0/490766935.D0  
A107=6005943493.D0/2108947869.D0  
A108=393006217.D0/1396673457.D0  
A109=123872331.D0/1001029789.D0  
A111=-1028468189.D0/846180014.D0  
A114=8478235783.D0/508512852.D0  
A115=1311729495.D0/1432422823.D0  
A116=-10304129995.D0/1701304382.D0  
A117=-48777925059.D0/3047939560.D0  
A118=15336726248.D0/1032824649.D0  
A119=-45442868181.D0/3398467696.D0  
A1110=3065993473.D0/597172653.D0  
A121=185892177.D0/718116043.D0  
A124=-3185094517.D0/667107341.D0  
A125=-477755414.D0/1098053517.D0  
A126=-703635378.D0/230739211.D0  
A127=5731566787.D0/1027545527.D0  
A128=5232866602.D0/850066563.D0  
A129=-4093664535.D0/808688257.D0  
A1210=3962137247.D0/1805957418.D0  
A1211=65686358.D0/487910083.D0  
A131=403863854.D0/491063109.D0  
A134=-5068492393.D0/434740067.D0  
A135=-411421997.D0/543043805.D0  
A136=652783627.D0/914296604.D0  
A137=11173962825.D0/925320556.D0  
A138=-13158990841.D0/6184727034.D0  
A139=3936647629.D0/1978049680.D0  
A1310=-160528059.D0/685178525.D0  
A1311=248638103.D0/1413531060.D0  
B1=14005451.D0/335480064.D0  
B6=-59238493.D0/1068277825.D0  
B7=181606767.D0/758867731.D0  
B8=561292985.D0/797845732.D0  
B9=-1041891430.D0/1371343529.D0  
B10=760417239.D0/1151165299.D0  
B11=118820643.00/751138087.D0  
B12=-528747749.D0/2220607170.D0  
B13=1.D0/4.D0  
BH1=13451932.D0/455176623.D0  
BH6=-808719846.D0/976000145.D0  
BH7=1757004468.D0/5645159321.D0  
BH8=656045339.D0/265891186.D0  
BH9=-3867574721.D0/1518517206.D0  
BH10=465885868.D0/322736535.D0  
BH11=53011238.D0/667516719.D0  
BH12=2.D0/45.D0  
RETURN  
BND

# 3. Odex

Extrapolation code (see Section I.9) with variable order and variable step size, Good for all tolerances, supreme for very high precision (e.g. $1 0 ^ { - 2 0 } \mathrm { o r } 1 0 ^ { - 3 0 } )$

SUBROUTINE ODEX (N,FCN,X,Y,XEND,EPS,HMAX,H)CNUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERORDINARY DIFFERENTIAL EQUATIONS Y'=F(X,Y).THIS IS AN EXTRAPOLATION-ALGORITHM，BASED ON THEEXPLICIT MIDPOINT RULE （WITH STEPSIZE CONTROLC AND ORDER SRLECTION).C C.F. SECTION II.9CC INPUT PARAMETERSCC N DIMENSION OF THE SYSTEM (N.LE.51)C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*8 X,Y(N),F(N)F(1)=... BTC.X INITIAL X-VALUEXEND FINAL X-VALUE （XRND.GT.X)C Y(N) INITIAL VALUES FOR YC EPS LOCAL TOLERANCEC HMAX MAXIMAL STEPSIZEC H INITIAL STEPSIZE GUESSCC OUTPUT PARAMETERSCC Y(N) SOLUTION AT XRNDCC EXTERNAL SUBROUTINE (TO BE SUPPLIED BY THE USER)CC SOLOUT THIS SUBROUTINE IS CALLED AFTER EVERYSUCCESSFULLY COMPUTED STEP (AND THEINITIAL VALUE）:SUBROUTINE SOLOUT (NR,X,Y,N)REAL\*8 X,Y(N)FURNISHES THE SOLUTION Y AT THE NR-THGRID-POINT X （THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT).SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTIONIS NOT DESIRED AT THE INTERMEDIATE POINTS.IMPLICIT REAL\*8 (A-H,O-Z)LOGICAL REJECT,LASTREAL\*8 Y(N)EXTERNAL FCNCOMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTC COMMON STAT CAN BE USED FOR STATISTICSNFCN NUMBER OF FUNCTION EVALUATIONSNSTEP NUMBER OF COMPUTED STEPSNACCPT NUMBER OF ACCEPTED STEPSC NREJCT NUMBER OF REJECTED STEPSCOMMON /EXTABL/ DZ(51),T(9,51),NJ(9),HH(9),W(9),ERR,FAI1 A(9),EPSD4,UROUND,FAC1,FAC2,SAFr2DATA NJ/2,4,6,8,10,12,14,16,18/DATA A/3.D0,7.D0,13.D0,21.D0,31.D0,43.D0,57.D0,73.D0,9DATA NMAX/800/,KM/9/,UROUND/1.73D-18/C NMAX MAXIMAL NUMBRR OF STEPSC UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.D0

(Iv DD AVAIIDU DI InD UUBn)DATA FAC1/2.D-2/,FAC2/4.D0/,FAC3/.9D0/,FAC4/.8D0/DATA SAFB1/.65D0/,SAFE2/.94D0/  
C INITIAL PRRPARATIONSRPSD4=EPS\*SAFE1NSTEP=0NREJCT=0NACCPT=0NFCN=0K=MAXO(3,MINO(8,INT(-DL0G10(BPS)\*.6D0+1.5D0)))H=DMINi(H,HMAX,(XEND-X)/2.D0)CALL SOLOUT (NACCPT+1,X,Y,N)BRR=0.D0W(1)=0.D0RrJECT=.FaLSE.LAST=.FALSE.  
C IS XEND REACHED IN THE NEXT STEP?10 H1=XEND-XIF （H1.LE.UROUND） GO TO 110H=DMINI(H,H1,HMAX)IF （H.GE.H1-UROUND) LAST=.TRUE.CALL FCN(N,X,Y,DZ)NFCN=NFCN+1  
C THE FIRST AND LAST STEPIF （NSTEP.EQ.O.OR.LAST) THENNSTEP=NSTEP+1D0 20 J=1,KKC=JCALL MIDEX(J,X,Y,H,HMAX,N,FCN)20 IF （J.GT.1.AND.ERR.LE.EPS) GO TO 60GO TO 55END IF  
C BASIC INTEGRATION STEP30 CONTINUENSTRP=NSTRP+1IF （NSTEP.GE.NMAX) GO TO 120KC=K-1DO 40 J=1,KC40 CALL MIDEX(J,X,Y,H,HMAX,N,FCN)  
C CONVERGENCE MONITORIF（K.EQ.2.OR.REJECT） GO TO 50IF (ERR.LE.EPS）GO TO 60IF (BRR/BPS.GT.(DFLOAT(NJ(K+1)\*NJ(K))/4.DO)\*\*2) GO TO 10050 CALL MIDRX(K,X,Y,H,HMAX,N,FCN)KC=KIF (ERR.LE.EPS) GO TO 60  
C HOPE FOR CONVERGENCE IN LINE K+155 IF (ERR/EPS.GT.(DFLOAT(NJ(K+1))/2.DO)\*\*2) GO TO 100KC=K+1CALL MIDEX(KC,X,Y,H,HMAX,N,FCN)IF （ERR.GT.EPS) GO TO 100  
C STEP IS ACCEPTED60 X=X+HDO 70 I=1,N70 Y(I)=T(1,I)NACCPT=NACCPT+1CALL SOLOUT (NACCPT+1,X,Y,N)  
C -. - COMPUTE OPTIMAL ORDERIF (KC.EQ.2） THENKOPT=3IF (REJECT) KOPT=2GO TO 80END IFIF (KC.LE.K) THENKOPT=KCIF (W(KC-1).LT.W(KC)\*FAC3) KOPT=KC-1IF (W(KC).LT.W(KC-1)\*FAC3) KOPT=MINO(KC+1,KM-1)BLDAKOPT=KC-1IF （KC.GT.3.AND.W(KC-2).LT.W(KC-1)\*FAC3) KOPT=KC-2IF (W(KC).LT.W(KOPT)\*FAC3) KOPT=MINO(KC,KM-1)END IF  
C AFTER A REJECTED STEP80 IF（REJECT）THENK=MINO(KOPT,KC）H=DMIN1(H,HH(K))REJECT=.FALSE.GO TO 10END IF  
C COMPUTE STEPSIZE FOR NEXT STEPIF （KOPT.LE.KC） THENH=HH(KOPT)ELSBIF （KC.LT.K.AND.W(KC).LT.W(KC-1)\*FAC4) THENH=HH(KC)\*A(KOPT+1)/A(KC)ELSEH=HH(KC)\*A(KOPT)/A(KC)ENDIFBND IFK=KOPTGO TO 10  
C STEP IS REJECTED100 K=MINO(K,KC）IF (K.GT.2.AND.W(K-1).LT.W(K)\*FAC3) K=K-1NREJCT=NREJCT+1H=HH(K)REJECT=.TRUE.GO TO 30  
C SOLUTION EXIT110 CONTINUERETURN  
C FAIL EXIT120 WRITE（6,\*)'MORE THAN ’,NmAx,' STEPS1RETURNEND  
CSUBROUTINE MIDEX(J,X,Y,H,HMAX,N,FCN)  
C THIS SUBROUTINE COMPUTES THE J-TH LINE OF THE  
C EXTRAPOLATION TABLE AND PROVIDES AN ESTIMATION  
C OF THE OPTIMAL STEPSIZEIMPLICIT REAL\*8 (A-H,O-Z）EXTERNAL FCNREAL\*8 Y(N),DY(51),YH1(51),YH2(51)COMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTCOMMON /EXTABL/ DZ(51),T(9,51),NJ(9),HH(9),W(9),ERR,FAC,1 A(9),EPSD4,UROUND,FAC1,FAC2,SAFE2HJ=H/DFLOAT(NJ(J))  
C EULER STARTING STEPDO 30 I=1,NYHI(I)=Y(I)30 YH2(I)=Y(I)+HJ\*DZ(I)  
C EXPLICIT MIDPOINT RULEM=NJ(J)-1D0 35 MM=1,MCALL FCN(N,X+HJ\*DFLOAT(MM),YH2,DY)D0 35 I=1,NYS=YH1(I)YH1(I) =YH2(I)35 YH2(I)=YS+2.DO\*HJ\*DY(I)  
C FINAL SMOOTHING STEPCALL FCN(N,X+H,YH2,DY)D0 40 $\mathbb { Z } = 1$ ,N40 T(J,I)=(YH1(I)+YH2(I)+HJ\*DY(I))/2.D0NFCN=NFCN+NJ(J）  
C --- POLYNOMIAL EXTRAPOLATIONIF （J.EQ.1) RETURNDO 60 L=J,2,-1FAC=(DFLOAT(NJ(J))/DFLOAT(NJ(L-1)))\*\*2-1.D0DO 60 I=1,NT(L-1,I)=T(L,I)+(T(L,I)-T(L-1,I))/FAC60 CONTINUEERR=0.D0D0 65 I=k,N  
C 一 SCALINGSCAL=DMAX1(DABS(Y(I)),DABS(T(1,I)),1.D-6,UROUND/EPSD4)65 BRR=BRR+((T(1,I)-T(2,I))/SCAL)\*\*2BRR=DSQRT(ERR/DFLOAT(N))  
C 一 COMPUTR OPTIMAL STEPSIZESBXPO=1.D0/DFLOAT(2\*J-1)FACMIN=FAC1\*\*EXPOFAC=DMINI(FAC2/FACMIN,DMAXI(FACMIN,(ERR/EPSD4)\*\*EXPO/SAFE2）)FAC=1.D0/FACHH(J)=DMINI（H\*FAC,HMAX)W(J)=A(J)/HH(J)RETURNBND  
CSUBROUTINE SOLOUT (NRPNTS,X,Y,N)IMPLICIT REAL\*8 (A-H,O-Z)REAL\*8 Y(N)RETURNEND

# 4. Odex2

Extrapolation code (see Section II.13) with variable order and variable step size for second order diferential systems of the form y $\prime \prime = f \left( x , y \right)$ Good for all tolerances.

SUBROUTINE ODEX2 (N,FCN,X,Y,YP,XEND,EPS,HMAX,H)CC NUMERICAL SOLUTION OF A SYSTEM OF SECOND ORDERC ORDINARY DIFFERENTIAL EQUATIONS Y"=F(X,Y).C THIS IS AN EXTRAPOLATION-ALGORITHM， BASED ON THEC EXPLICIT MIDPOINT RULE （WITH STEPSIZE CONTROLC AND ORDER SELECTION).C C.F. SECTION II.13CC INPUT PARAMETERSCC N DIMENSION OF THE SYSTEM （N.LE.51）C FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEC SECOND DERIVATIVE F(X,Y):C SUBROUTINE FCN(N,X,Y,F)C REAL\*8 X,Y(N),F(N)C F(1)=... ETC.C X INITIAL X-VALUEC X BND FINAL X-VALUE (XEND.GT.X)C Y(N) INITIAL VALUES FOR YC YP(N) INITIAL VALUES FOR Y'C EPS LOCAL TOLERANCEC HMAX MAXIMAL STEPSIZEC H INITIAL STRPSIZE GUESSCC OUTPUT PARAMETERSCC Y(N) SOLUTION AT XENDC YP(N) DERIVATIVE OF SOLUTION AT XENDC

SUCCESSFULLY COMPUTED STEP (AND THEINITIAL VALUE):SUBROUTINE SOLUT2 (NR,X,Y,YP,N)REAL\*8 X,Y(N),YP(N)FURNISHES THE SOLUTION (Y,YP) AT THE NR-THGRID-POINT X (THE INITIAL VALUE IS CON-SIDERED AS THE FIRST GRID-POINT).SUPPLY A DUMMY SUBROUTINE，IF THE SOLUTIONIS NOT DESIRED AT THE INTERMEDIATE POINTS.IMPLICIT REAL\*8 (A-H,O-Z)LOGICAL REJECT,LASTREAL\*8 Y(N),YP(N)EXTERNAL FCNCOMMON /STAT/NFCN,NSTEP,NACCPT,NREJCT  
C COMMON STAT CAN BE USED FOR STATISTICS  
C NFCN NUMBER OF FUNCTION EVALUATIONS  
C NSTBP NUMBER OF COMPUTED STEPS  
C NACCPT NUMBER OF ACCEPTED STEPS  
C NREJCT NUMBER OF REJECTED STEPSCOMMON /EXTABL/ DZ(51),T(9,51),TP(9,51),NJ(9),HH(9),W(9),BRR,F.A(9),rPSD4,UROUND,FACi,FAC2,SAFE2DATA NJ/2,4,6,8,10,12,14,16,18/DATA A/2.00,4.D0,7.00,11.00,16.D0,22.D0,29.D0,37.D0,46.D0/DATA NMAX/800/,KM/9/,UROUND/1.73D-18/  
C NMAX MAXIMAL NUMBER OF STEPS  
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.DO  
C (TO BE ADAPTED BY THE USER)DATA FAC1/2.D-2/,FAC2/4.D0/,FAC3/.9D0/,FAC4/.8D0/DATA SAFB1/.65D0/,SAFE2/.94D0/  
C INITIAL PRRPARATIONSBPSD4=EPS\*SAFE1NSTEP=0NREJCT=0NACCPT=0NFCN=0K=MAXO(3,MINO(8,INT(-DLOG10(EPS)\*.6D0+1.5D0)))H=DMINl(H,HMAX,(XBND-X)/2.D0)CALL SOLUT2 (NACCPT+1,X,Y,YP,N)ERR=0.D0W(1)=0.D0REJECT=.FALSE.LAST=.FALSE.  
C IS XEND REACHBD IN THE NEXT STEP?10 H1=XEND-XIF （HI.LE.UROUND） GO TO 110H=DMIN1(H,Hl,HMAX)IF（H.GR.HI-UROUND） LAST=.TRUE.CALL FCN(N,X,Y,DZ)NFCN=NFCN+1  
C THE FIRST AND LAST STEPIF （NSTEP.EQ.O.OR.LAST) THENNSTEP=NSTEP+1DO 20 J=1,KKC=JCALL STOERM(J,x,Y,YP,H,HMAX,N,FCN)20 IF（J.GT.1.AND.ERR.LR.EPS)GO TO 60GO T0 55BND IF  
C BASIC INTEGRATION STRP30 CONTINUENSTEP=NSTEP+1IF （NSTBP.GE.NMAX) GO TO 120KC=K-1D0 40 J=1,KC40 CALl STOERM(J,X,Y,YP,H,HMAX,N,FCN)  
C CONVERGENCE MONITORIF （K.EQ.2.OR.REJECT) GO TO 50IF (ERR.LE.EPS) GO TO 60IF (ERR/EPS.GT.(DFLOAT(NJ(K+1)\*NJ(K))/4.DO)\*\*2) GO TO50 CALL STOERM(K,X,Y,YP,H,HMAX,N,FCN)KC=KIF （ERR.LE.EPS) GO TO 60  
C HOPE FOR CONVERGBNCE IN LINE K+155 IF (BRR/BPS.GT.(DFLOAT(NJ(K+1))/2.DO)\*\*2) GO TO 100KC=K+1CALL STOERM(KC,X,Y,YP,H,HMAX,N,FCN)IF (ERR.GT.EPS) GO TO 100  
C STEP IS ACCEPTED60 X=X+HDO 70 I=1,NYP(I)=TP(1,I)70 Y(I)=T(1,I)NACCPT=NACCPT+1CALL SOLUT2 (NACCPT+1,X,Y,YP,N)  
C COMPUTE OPTIMAL ORDERIF (KC.EQ.2) THBNKOPT=3IF （REJECT） KOPT=2GO TO 80END IFIF (KC.LE.K) THENKOPT=KCIF(W(KC-1).LT.W(KC)\*FAC3) KOPT=KC-1IF (W(KC).LT.W(KC-1)\*FAC3) KOPT=MINO(KC+1,KM-1)ELSEKOPT=KC-1IF（KC.GT.3.AND.W(KC-2).LT.W(KC-1)\*FAC3) KOPT=KC-2IF(W(KC).LT.W(KOPT)\*FAC3)KOPT=MINO(KC,KM-1)END IF  
C AFTER A REJECTED STEP80 IF（REJECT） THENK=MINO(KOPT,KC)H=DMINi(H,HH(K))REJECT=.FALSR.GO TO 10BND IF  
C COMPUTR STEPSIZE FOR NEXT STEPIF（KOPT.LR.KC) THBNH=HH(KOPT)BLSEIF （KC.LT.K.AND.W(KC).LT.W(KC-1)\*FAC4) THENH=HH(KC)\*A(KOPT+1)/A(KC)ELSEH=HH(KC)\*A(KOPT)/A(KC)BNDIFBND IFK=KOPTGO TO 10  
C STRP IS REJECTrD  
100 K=MINO(K,KC)IF (K.GT.2.AND.W(K-1).LT.W(K)\*FAC3) K=K-1NRBJCT=NRBJCT+1H=HH(K)REJECT=.TRUE.GO TO 30  
C SOLUTION EXIT  
110 CONTINUERBTURN  
C FAIL EXIT  
120 WRITB(6,\*） MORE THAN',NMAX,’ STEPSRBTURNBNDSUBROUTINE STOERM(J,X,Y,YP,H,HMAX,N,FCN)  
C THIS SUBROUTINE COMPUTES THE J-TH LINE OF THE  
C EXTRAPOLATION TABLE AND PROVIDES AN ESTIMATION  
C OF THE OPTIMAL STEPSIZEIMPLICIT REAL\*8 (A-H,O-Z)EXTERNAL FCNREAL\*8 Y(N),YP(N),DY(5l),YHl(51),ZHl(51)COMMON /STAT/NFCN,NSTEP,NACCPT,NREJCTCOMMON /EXTABL/ DZ(51),T(9,51),TP(9,51),NJ(9),HH(9),W(9),ERR,FA1 A(9),BPSD4,UROUND,FACl,FAC2,SAFE2HJ=H/DFLOAT(NJ(J))HJ2=HJ\*2.D0  
C EULER STARTING STEPDO 30 I=1.NYH1(I)=Y(I)30 ZH1(I)=YP(I)+HJ\*DZ(I)  
C EXPLICIT MIDPOINT (STOBRMER) RULEM=NJ(J)/2-1IF (J.EQ.1) GO TO 37D0 35 MM=1,MDO 33 I-1,N33 YH1(I)=YHi(I)+HJ2\*ZHl（I)CALL FCN(N,X+HJ2\*DFLOAT(MM),YH1,DY)DO 35 I=1,N35 ZHl(I)=ZH1(I)+HJ2\*DY(I)  
C FINAL STEP37 CONTINUEDO 40 I=1,N40 YHl(I)=YH1(I)+HJ2\*ZH1(I)CALL FCN(N,X+H,YHl,DY)D0 43 I=1,NT(J,I)=YH1(I)43 TP(J,I)=ZHi(I)+HJ\*DY(I)NFCN=NFCN+M+1  
C POLYNOMIAL EXTRAPOLATIONIF (J.BQ.1）RRTURND0 60 L=J,2,-1FAC=(DFLOAT(NJ(J))/DFLOAT(NJ(L-1)))\*\*2-1.D0DO 60 I=1,NT(L-1,I)=T(L,I)+(T(L,I)-T(L-1,I))/FACTP(L-1,I)=TP(L,I)+(TP(L,I)-TP(L-1,I))/FAC60 CONTINUEERR=0.D0D0 65 I=1,N  
C SCALINGSCAL=DMAX1(DABS(Y(I)),DABS(T(1,I)),1.D-6,UROUND/BPSD4)SCALP=DMAXi(DABS(YP(I)),DABS(TP(1,I)),1.D-6,UROUND/BPSD4)65 BRR=ERR+((T(1,I)-T(2,I))/SCAL)\*\*2+((TP(1,I)-TP(2,I))/SCALP)\*\*2ERR=DSQRT(ERR/DFLOAT(N\*2))  
C COMPUTE OPTIMAL STEPSIZESRXPO=1.D0/DFLOAT(2\*J-1)FACMIN=FAC1\*\*EXPOFAC=DMINI(FAC2/FACMIN,DMAXI(FACMIN,(RRR/BPSD4)\*\*EXPO/SAFE2))FAC=1.D0/FACHH(J)=DMIN1(H\*FAC,HMAX)W(J)=A(J)/HH(J)RETURNEND  
CSUBROUTINE SOLUT2 (NRPNTS,X,Y,YP,N)IMPLICIT RBAL\*8 (A-H,O-Z）REAL\*8 Y(N),YP(N)RETURNBND

# 5. Doprin

Explicit Runge-Kutta-Nystrom code based on the formulas of Dormand and Prince with step size control (see Table 13.4 of Section 2.13) for second order differential systems of the form y $\mathbf { \Phi } ^ { \prime \prime } = f \left( { \boldsymbol { x } } , { \boldsymbol { y } } \right)$

SUBROUTINE dOPRIN(N,FCN,X,Y,YP,XEND,rPS,HMAX,H)   
NUMERICAL SOLUTION OF A SYSTEM OF SECOND ORDER ORDINARY DIFFERENTIAL EQUATIONS Y"=F(X,Y). THIS IS AN EMBEDDED NYSTROEM METHOD OF ORDER (6)7 DUE TO DORMAND & PRINCE (WITH STEPSIZE CONTROL） C.F. SECTION II.13 INPUT PARAMETERS N DIMENSION OF THE SYSTEM (N.LE.51) FCN NAME （EXTERNAL) OF SUBROUTINE COMPUTING THE SECOND DERIVATIVE F(X,Y): SUBROUTINE FCN(N,X,Y,F) REAL\*8 X,Y(N),F(N) F(1)=... ETC. X INITIAL X-VALUE XEND FINAL X-VALUE (XEND.GT.X) Y(N) INITIAL VALUES FOR Y YP(N) INITIAL VALUES FOR Y' BPS LOCAL TOLERANCE HMA X MAXIMAL STEPSIZE H INITIAL STEPSIZE GURSS OUTPUT PARAMETERS Y(N) SOLUTION AT XEND YP(N) DERIVATIVE OF SOLUTION AT XEND EXTERNAL SUBROUTINE (TO BE SUPPLIED BY THE USER) SOLUT2 THIS SUBROUTINE IS CALLED AFTER EVERY SUCCESSFULLY COMPUTED STEP (AND THE INITIAL VALUE): SUBROUTINE SOLUT2 (NR,X,Y,YP,N) RrAL\*8 X,Y(N),YP(N) FURNISHES THE SOLUTION (Y,YP) AT THE NR-TH GRID-POINT X （THE INITIAL VALUE IS CON-SIDRRED AS THE FIRST GRID-POINT). SUPPLY A DUMMY SUBROUTINE， IF THE SOLUTION IS NOT DESIRED AT THE INTERMEDIATE POINTS. IMPLICIT REAL\*8 (A-H,O-Z) REAL\*8 K0(51),K1(51),K2(51),K3(51),K4(51),Yl(51),Y(N),YP(N LOGICAL REJECT COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT COMMON STaT CAUMBBRUSED FuNcTITATIStIUATIONS NSTRP NUMBER OF COMPUTED STEPS NACCPT NUMBER OF ACCEPTED STEPS NRBJCT NUMBER OF REJECTED STEPS DATA NMAX/2000/,UROUND/1.73D-18/   
C NMA X MAXIMAL NUMBER OF STEPS   
C UROUND SMALLEST NUMBER SATISFYING 1.DO+UROUND>1.DO   
C (TO BE ADAPTED BY THE USER) ALPH1=.1D0 ALPH2=.2D0 ALrnJ-3.vv/o.vv ALPH4=.5D0 SQ21=DSQRT(21.D0) ALPH5=(7.D0-SQ21)/14.D0 ALPH6=(7.D0+SQ21)/14.D0 C0=.05D0 C4=16.D0/45.D0 C5=49.D0/180.D0 G10=1.D0/200.D0 G20=1.D0/150.D0 G21=1.D0/75.D0 G30=171.D0/8192.D0 G31=45.D0/4096.D0 G32=315.D0/8192.D0 G40=5.D0/288.D0 G41=25.D0/528.D0 G42=25.D0/672.D0 G43=16.D0/693.D0 G50=(1003.D0-205.D0\*SQ21)/12348.D0 G51=(-18775.D0+4325.D0\*SQ21)/90552.D0 G52=(15600.D0-3425.D0\*SQ21)/43218.D0 G53=(-46208.D0+10112.D0\*SQ21)/237699.D0 G54=(3411.D0-745.D0\*SQ21)/24696.D0 G60=(793.D0+187.D0\*SQ21)/12348.D0 G61=(-8275.D0-2825.D0\*SQ21)/90552.D0 G62=(26100.D0+6175.D0\*SQ21)/43218.D0 G63=-(1905280.D0+483712.D0\*SQ21)/9745659.D0 G64=(3327.D0+797.D0\*SQ21)/24696.D0 G65=-(581.D0+127.D0\*SQ21)/1722.D0 G70=(-157.D0+3.D0\*SQ21)/378.D0 G71=(3575.D0-250.D0\*SQ21)/2772.D0 G72=-(21900.D0+1375.D0\*SQ21)/3969.D0 G73=(1168640.D0+23040.D0\*SQ21)/596673.D0 G74=-(1353.D0+26.D0\*SQ21)/2268.D0 G75=(12439.D0+2639.D0\*SQ21)/4428.D0 G76=(35.D0-7.D0\*SQ21)/36.D0 G80=.05D0 G84=8.D0/45.D0 G85=(49.D0+7.D0\*SQ21)/360.D0 G86=(49.D0-7.D0\*SQ21)/360.D0 POSNEG=DSIGN(1.DO,XEND-X)   
C INITIAL PREPARATIONS HMAX=DABS(HMAX) H=DMIN1(DMAX1(1.D-8,DABS(H)),HMAX) H=DSIGN(H,POSNEG) EPS=DMAX1(RPS,9.DO\*UROUND) REJECT=.FALSE. NACCPT=0 NREJCT=0 NFCN=1 NSTEP=0 CALL SOLUT2(NACCPT+1,X,Y,YP,N) CALL FCN(N,X,Y,KO)   
C BASIC INTEGRATION STEP 1 IF(NSTRP.GT.NMAX.OR.X+.05DO\*H.EQ.X)GOTO 79 IF((X-XEND)\*POSNEG+UROUND.GT.O.DO) RETURN IF((X+H-XEND)\*POSNEG.GT.O.DO)H=XEND-X HP2=H\*H NSTEP=NSTEP+1   
C THE FIRST 5 STAGES D0 21 $\mathbb { I } = 1$ ,N 21 Y1(I)=Y(I)+ALPH1\*H\*YP(I)+HP2\*G10\*KO（I) CALL FCN(N,X+ALPHl\*H,Y1,K1) DO 22 I=1,N 22 Y1(I)=Y(I)+ALPH2\*H\*YP(I)+HP2\*(G20\*K0(I)+G21\*K1(I) CALL FCN(N,X+ALPH2\*H,Yl,K2) DO 23 I=1,N 23 Yl(I)=Y(I)+ALPH3\*H\*YP(I)+HP2\*(G30\*K0(I)+G31\*K1(I)+G32\*K2(I)) CALL FCN(N,X+ALPH3\*H,Y1,K3) DO 24 I=1,N 24 Y1(I)=Y(I)+ALPH4\*H\*YP(I)+HP2\*(G40\*K0(I)+G41\*K1(I)+G42\*K2(I)+ &G43\*K3(I)) CALL FCN(N,X+ALPH4\*H,Yl,K4) D0 25 I=1,N 25Y1(I)=Y(I)+ALPH5\*H\*YP(I)+HP2\*(G50\*K0(I)+G51\*K1(I)+G52\*K2(I)+ & G53\*K3（I)+G54\*K4（I))   
C --COMPUTE INTERMEDIATE SUM TO SAVE MEMORY DO 61 I=1,N Y1S=G60\*K0(I)+G61\*K1(I)+G62\*K2(I)+G63\*K3(I)+G64\*K4（I） K3(I)=G70\*K0(I)+G71\*K1(I)+G72\*K2(I)+G73\*K3(I)+G74\*K4（I) 61 K2(I)=Yls   
C THE LAST 4 STAGES CALL FCN(N,X+ALPH5\*H,Y1,Kl) D0 26 I=1,N 26 Y1(I)=Y(I)+ALPH6\*H\*YP(I)+HP2\*(K2(I)+G65\*K1(I)) CALL FCN(N,X+ALPH6\*H,Y1,K2) DO 27 I=1,N 27 Y1(I)=Y(I)+H\*YP(I)+HP2\*(K3(I)+G75\*K1(I)+G76\*K2(I)) XPH=X+H CALL FCN(N,XPH,Y1,K3) DO 28 I=1,N 28 Y1(I)=Y(I)+H\*YP(I)+HP2\*(G80\*K0(I)+G84\*K4(I)+G85\*K1(I)+G86\*K2（I) DO 30 I=1,N 30 K4(I)=YP(I)+H\*(C0\*(K0(I)+K3(I))+C4\*K4(I)+C5\*(K1(I)+K2(I))) CALL FCN(N,XPH,Y1,K1) DO 33 I=1,N 33 K2(I)=HP2\*(K1(I)-K3(I))/20.D0 NFCN=NFCN+8   
C ERROR ESTIMATION BRR=0.D0 D0 41 I=1,N DENOM=DMAXI(1.D-6,DABS(YI(I)),DABS(Y(I)),2.DO\*UROUND/RPS) 41 ERR=ERR+(K2(I)/DBNOM)\*\*2 ERR=DSQRT(ERR/DFLOAT(N))   
C COMPUTATION OF HNEW   
C WE REQUIRE .2<=HNBW/H<=10. FAC=DMAX1(.1DO,DMIN1(5.DO,(ERR/EPS)\*\*(1.DO/7.DO)/.9D0)) HNEW=H/FAC IF(ERR.LE.RPS)THEN   
C STEP IS ACCEPTED NACCPT=NACCPT+1 DO 44 I=1,N YP(I)=K4(I) KO(I)=K1(I) 44 Y(I)=Y1（I) X=XPH CALL SOLUT2(NACCPT+1,X,Y,YP,N) IF(DABS(HNEW).GT.HMAX) HNEW=POSNBG\*HMAX IF(REJECT)HNEW=POSNEG\*DMINI(DABS(HNEW),DABS(H)) REJECT=.FALSE. ELSE   
C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1) NRRJCT=NREJCT+1 END IF H=HNBW GOTO 1   
C FAIL EXIT 79 WRITE(6,979)X   
979 FORMAT(' EXIT OF DOPRIN AT X=',D16.7) RBTURN END   
SUBROUTINE SOLUT2 (NRPNTS,X,Y,YP,N)   
IMPLICIT REAL\*8 (A-H,O-Z)   
REAL\*8 Y(N),YP(N)   
RETURN   
END

# 6. Retard

Modification of the code DOPRI5 for delay differential equations (see Section I.15). A sample calling program is included. The subroutines STORE and YLAG are also useful for dense output and graphics.

C SAMPLE CALLING PROGRAM FOR RETARDC SOLVING PROBLEM （15.12） WITH SAME INITIAL CONDITIONSC AS FOR TABLE 15.1.DIMENSION Y（1)COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISCCOMMON/STAT/NFCN,NSTEP,NACCPT,NRBJCTEXTERNAL FCN$\mathtt { X 0 } = 0$ ，LAST=0H=0.5Y(1)=0.1Do i I=1,10X=FLOAT(I-1)XEND=FLOAT(I)EPS=1.E-6HMAX=1.CALL RETARD(1,FCN,X,Y,XEND,EPS,HMAX,H)WRITE(6,\*)X,Y(1)WRITE(6,\*) COMMON STAT:',NFCN,NSTEP,NACCPT,NREJC1 CONTINUESTOPENDSUBROUTINE FCN(N,X,Y,F)DIMBNSION Y(N),F(N)EXTERNAL PHIA=1.4F(1)=(A-YLAG(1,X-1.,PHI))\*Y(1)RETURNENDREAL FUNCTION PHI(I,X)IF(I.EQ.1)PHI=O.RETURNENDSUBROUTINE RETARD(N,FCN,X,Y,XEND,EPS,HMAX,H)NUMERICAL SOLUTION OF A SYSTEM OF FIRST ORDERRETARDED DIFFERENTIAL EQUATIONS Y'=F(X,Y(X),Y(X-TAU),..)。THIS IS BASED ON AN EMBEDDED RUNGE-KUTTA METHOD OF ORDER （4)5DUE TO DORMAND & PRINCE （WITH STEPSIZE CONTROL）.C.F. SECTIONS II.5 AND II.15INPUT PARAMRTERSN DIMENSION OF THE SYSTEM （N.LB.51)FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEFIRST DERIVATIVE F(X,Y):SUBROUTINE FCN(N,X,Y,F)REAL\*4 X,Y(N),F(N)EXTERNAL PHI

F(1)=-YLAG(1,X-1.,PHI)+... F(2)=... BTC.   
WHBRE "PHI" IS THE(BXTERNAL) NAME OF   
A REAL FUNCTION COMPUTING THE   
I-TH COMPONBNT OF THE INITIAL FUNCTION PHI（X)   
REAL FUNCTION PHI(I,X)   
IF（I.EQ.1) PHI=... BTC.   
X INITIAL X-VALUE   
C XBND FINAL X-VALUE (XEND>X)   
Y(N) INITIAL VALUES FOR Y   
BPS LOCAL TOLERANCE   
HMAX MAXIMAL STEP SIZE   
C H INITIAL STEP SIZE GUESS   
C   
C OUTPUT PARAMETERS   
C   
C Y(N) SOLUTION AT XEND   
C   
REAL\*4 K1(51),K2(51),K3(51),K4(51),K5(51),K6(51),K7(51)   
RBAL\*4 Y1(51),Y(N)   
LOGICAL REJECT,DISC   
COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC   
C MEANING OF THESE VARIABLES:   
C IFIRST LOWEST STEP NUMBER STILL IN MEMORY COEF;   
LAST ADDRESS OF LAST DATA WRITTEN BY STORE ON COMMON BLOCK COEF, MUST BE SET TO O IN THE CALLING PROGRAM   
BEFORE THE FIRST CALL.   
x0 INITIAL POINT， MUST BE SET IN THE CALLING PROGRAM   
C BEFORE THE FIRST CALL.   
C X LAST =X+H OF LAST WRITTEN STEP;   
C IPOS POSITION OF LAST SUCCESSFUL SEARCH IN FUNCTION YLAG; C DISC LOGICAL VARIABLE，NECESSARY FOR THE DISTINCTION   
C OF K7 AND KI OF THE FOLLOWING STEP IN THE CASE   
C WHBN Y(XO) IS DIFFERENT FROM PHI(XO).   
COMMON/STAT/NFCN,NSTEP,NACCPT,NREJCT   
C COMMON STAT CONTAINS STATISTICAL INFORMATION:   
C NFCN NUMBER OF FUNCTION EVALUATIONS   
C NSTEP NUMBER OF COMPUTED STEPS   
C NACCPT NUMBER OF ACCEPTED STEPS   
C NREJCT NUMBER OF REJECTED STEPS   
COMMON/UROUND/UROUND   
C UROUND SMALLEST NUMBER SATISFYING 1.+UROUND>1.   
C (TO BE ADAPTED BY THE USER)   
DATA UROUND/5.8-8/   
DATA NMAX/3000/   
C NMA X MAXIMAL NUMBER OF STEPS   
C INITIAL PREPARATIONS   
HMAX=ABS(HMAX)   
H=AMIN1(AMAXI(1.E-4,ABS(H)),HMAX)   
H=SIGN(H,1.)   
EPS=AMAX1(BPS,7.\*UROUND）   
RrJrCT=.faLse.   
NACCPT=0   
NRRJCT=0   
NFCN=1   
NSTEP=0   
DISC=.TRUE.   
CALL FCN(N,X,Y,K1)   
IF(.NOT.DISC) CALL FCN(N,X,Y,K1)   
BASIC INTEGRATION STEP   
1 DISC=.TRUE.   
IF(NSTBP.GT.NMAX.OR.X+.1\*H.EQ.X)GOTO 79   
IF((X-XEND)+UROUND.GT.O.）RETURN   
IF((X+H-XBND).GT.O.)H=XEND-X   
NSTEP=NSTRP+1   
C THB 7 RUNGE-KUTTA STAGES   
DO 22 I=1,N   
22 Yl(I)=Y(I)+H\*.2\*Kl(I)   
CALL FCN(N,X+.2\*H,Y1,K2）   
D0 23 I=1,N   
23 Y1(I)=Y(I)+H\*((3./40.)\*K1(I)+(9./40.)\*K2(I))   
CALL FCN(N,X+.3\*H,Y1,K3） 24 Y1(I)=Y(I)+H\*((44./45.)\*K1(I)-(56./15.)\*K2(I)+(32./9.)\*H CALL FCN(N,X+.8\*H,Y1,K4) DO 25 I=1,N 25 Y1(I)=Y(I)+H\*((19372./6561.)\*K1(I)-(25360./2187.)\*K2(I) &+(64448./6561.)\*K3(I)-(212./729.)\*K4(I)) CALL FCN(N,X+(8./9.)\*H,Y1,K5) DO 26 I=1,N" 26 Y1(I)=Y(I)+H\*((9017./3168.)\*K1(I)-(355./33.)\*K2(I) &+(46732./5247.)\*K3(I)+(49./176.)\*K4(I)-(5103./18656. XPH=X+H CALL FCN(N,XPH,Y1,K6) DO 27 I=1,N 27Y1(I)=Y(I)+H\*((35./384.)\*K1(I)+(500./1113.)\*K3(I) & +(125./192.)\*K4(I)-(2187./6784.)\*K5(I)+(11./84.)\*K6( DISC=.TRUE. CALL FCN(N,XPH,Y1,K7） D0 28 I=1,N 28 K2(I)=((71./57600.)\*K1(I)-(71./16695.)\*K3(I)+(71./1920. & -(17253./339200.)\*K5(I)+(22./525.)\*K6(I)-(1./40.)\*K7 NFCN=NFCN+6   
C ERROR ESTIMATION BRR=0. D0 41 I=1,N DENOM=AMAX1(1.R-5,ABS(YI(I)),ABS(Y(I)),2.\*UROUND/BPS） 41 ERR=ERR+(K2(I)/DBNOM)\*\*2 ERR=SQRT(ERR/FLOAT(N))   
C COMPUTATION OF HNEW   
C WE RBQUIRE .2<=HNEW/H<=10. FAC=AMAX1(.1,AMIN1(5.,(ERR/EPS)\*\*(1./6.)/.9)) HNEW=H/FAC IF(ERR.LE.EPS)THEN   
C STEP IS ACCEPTED NACCPT=NACCPT+1 CALL STORE(X,XPH,Y,N,K1,K3,K4,K5,K6） D0 44 I=1,N K1(I)=K7(I) 44 Y(I)=YI(I)   
C --- RECOMPUTE KI IN THE CASE OF DISCONTINUOUS INITIAL PHASE IF(.NOT.DISC) CALL FCN(N,XPH,Y,Kl) X=XPH IF(ABS(HNEW).GT.HMAX)HNEW=HMAX IF(REJECT) HNEW=AMINI(ABS(HNEW),ABS(H)) REJBCT=.FALSE. BLSE   
C STEP IS REJECTED REJECT=.TRUE. IF(NACCPT.GE.1) NREJCT=NRRJCT+1 BND IF H=HNBW G0T0 1   
C FAIL BXIT 79 WRITE(6,979)x   
979 FORMAT(' BXIT OF RETARD AT X=',E11.4) RETURN BND   
C SUBROUTINE STORE(X,XPH,Y,N,FG1,FG3,FG4,FG5,FG6) PARAMETER (NN=4,MXST=800） DIMENSION Y(N),FG1(N),FG3(N),FG4(N),FG5(N),FG6(N) COMMON/COEF/XSTOR(MXST),YSTOR(NN,MXST). &C1(NN,MXST).C2(NN,MXST),C3(NN.MXST),C4(NN,MXST)   
C --- COEFFICIENTS FOR GLOBAL SOLUTION ARE STORED IN COEF COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC LAST=LAST+1 IFIRST=MAXO(1,LAST-MXST+1) IADR=MOD(LAST-1,MXST)+1 XLAST= XPH XSTOR(IADR)=X DO 2 I=1,NN YSTOR(I,IADR)=Y(I) C1(I,IADR)=FG1(I) C2(I,IADR)=-(1337./480.)\*FG1(I)+(105400./27825.)\*FG & (135./80.)\*FG4(I)-(54675./212000.)\*FG5(I)+(66./7 C3(I,IADR)=(1039./360.)\*FG1(I)-(468200./83475.)\*FG3 & (9./2.)\*FG4(I)+(400950./318000.)\*FG5(I)-(638./21 C4(I,IADR)=-(1163./1152.)\*FG1(I)+(37900./16695.)\*FG & (415./192.)\*FG4(I)-(674325./508800.)\*FG5(I)+(374 2 CONTINUE RETURN BND p' REAL FUNCTION YLAG(I,X,PHI) PARAMETER (NN=4,MXST=800) LOGICAL DISC COMMON/COEF/XSTOR(MXST),YSTOR(NN,MXST), & C1(NN,MXST),C2(NN,MXST),C3(NN,MXST),C4(NN,X) COMMON/POSITS/IFIRST,LAST,XO,XLAST,IPOS,DISC COMMON/UROUND/UROUND   
C INITIAL PHASE IF（DISC） THEN IF(ABS(X-XO).LE.(3.\*UROUND\*ABS(X)))DISC=.FALSE. IF(X.LE.XO)THEN YLAG=PHI(I,X) RETURN END IF END IF   
C COMPUTE THK POSITION OF X IF(X.LT.XSTOR(IFIRST))THEN WRITE （6,\*) MEMORY FULL，MXST $=$ ',MXST STOP BND IF IPOS=MAXO(IFIRST,MINO(LAST,IPOS)) 1 IADR=MOD(IPOS-1,MXST)+1 IF（X.LT.XSTOR(IADR).AND.IPOS.GT.IFIRST) THEN IPOS=IPOS-1 GOTO 1 END IF 2 IADR=MOD(IPOS,MXST)+1 IF（IPOS.LT.LAST) THEN IF（X.GT.XSTOR(IADR)） THEN IPOS=IPOS+1 GOTO 2 END IF END IF   
C COMPUTE THE DESIRED APPROXIMATION IADR=MOD(IPOS-1,MXST)+1 IF（IPOS.BQ.LAST) THEN H=XLAST-XSTOR(IADR) ELSE H=XSTOR(MOD(IPOS,MXST)+1)-XSTOR(IADR) END IF S=(X-XSTOR(IADR))/H YLAG=YSTOR(I,IPOS)+H\*S\*(C1(I,IPOS)+S\*(C2(I,IPOS) & +S\*(C3(I,IPOS)+S\*C4(I,IPOS)))) RETURN END   
N.H. Abel (1826): Untersuchungen uber die R eihe: $1 + { \frac { m } { 1 } } x + { \frac { m ( m - 1 ) } { 1 \cdot 2 } } x ^ { 2 } + { \frac { m ( m - 1 ) ( m - 2 ) } { 1 \cdot 2 \cdot 3 } } x ^ { 3 } + \ldots \ldots \ldots u . s . w .$ Crelle J. f.d. r.u.angew. Math. (in zwanglosen Heften), vol.1, p.311- 339.   
N.H. Abel (1827): Ueber einige bestimmte Integrale, Crelle J. f. d. r. u. angew. Math., vol.2, p.22-30.   
M. Abramowitz and I.A.Stegun (1964): Handbook of mathematical functions, Dover, 1000 pages.   
J.C. Adams (1883): see FBashforth (1883).   
A.C. Aitken (1932): On interpolation by iteration of proportional parts， wihout the use of differences; Proc. Edinburgh Math. Soc. Second ser. Vol.3,p.56- 76.   
J. Albrecht (1955): Beitrage zum Runge-Kutt-Verfahren, ZAMM, vol.35, p.100- 110.   
V.M. Alekseev (1961): An estimate for the perturbations of the solution of ordinary differential equations (Russian). Vestn. Mosk. Univ.,Ser.I, Math. Meh, 2, p.28-36.   
JIe Rond d'Alembert (1748): Suite des recherches sur le calcul integral, quatrieme partie: Methodes pour integrer quelques equations différentielles， Hist. Acad. Berlin, Tom.IV, p.275-291.   
R.F. Arenstorf (1963): Periodic solutions of the restricted three body problem representing analytic continuations of Keplerian eliptic motions， Amer. J. Math., vol.LXxxV, p.27-35.   
C. Arzela (1895): Sulle funzioni di linee, Memorie dell. R. Accad. delle Sc. di Bo-logna, 5e serie, vol.V, p.225-244, see also: vol.V, p.257-270, vol.VI, (1896), p.131-140.   
N. Bakhvalov (1976): Methodes numeriques, Editions Mir, Moscou $6 0 0 \{ \mathbf { p } \mathbf { p } .$ , russian edition 1973.   
F. Bashforth (1883): An attempt to test the theories of capillary action by comparing the theoretical and measured forms of drops of fluid. Wuth an explanation of the method of integration employed in constructing the tables which give the theoretical form of such drops, by J.CAdams, Cambridge Univ. Press.   
R.H. Batin (1976): Resolution of Runge-Kutta-Nystrom condution equations through eighth order, AIAA J., vol.14, p.1012-1021.   
F.L. Bauer, H. Rutishauser and E. Stiefel (1963): New aspects in numerical quadrature. Proc. of Symposia in Appl. Math. vol.15, p.199-218, Am. Math. soc.   
PA. Beentjes and W.J. Gerritsen (1976): Higher order R unge-Kutta methods for the numerical solution of second order differential equations without first deriva-tives，Report NW 34/76,Math. Centrum, Amsterdam plexen Veranderlichen.'Zweite Auflage. Springer Verlag, Berlin-Gottingen-Heidelberg.   
A. Bellen (1984): One-step collcation for delay differential equatins， J. Comput. Appl. Math. Vol.10, p.275-283.   
R. Bellman and K.L. Cooke (1963): Diferential-Difference equations, Academic Press, 462pp.   
I. Bendixson (1893): Sur le calcul des integrales d'un systeme d'equations differenieles par des approximations successives, Stock. Akad. Forh., Vol.51, p.599-612.   
I. Bendixson (1901): Sur les courbes definies par des équations differentielles， Acta Mathematica, vol.24, p.1-88.   
Jac. Bernoulli (1695): Explicationes, Annotationes & Additiones ad ea, quae in Actis sup.anni de Curva Elastica, Isochrona Paracentrica, & Velaria, hinc inde memorata， & partim controversa legundur; ubi de Linea mediarum directio-num, alisque novis, Acta Erudit. Lipsiae, Anno MDCxCV, p. 537-553.   
Jac. Bernoulli (1697): Solutio Problematum Fratermorum, Peculiari Programmate Cal. Jan.I697 Groningae, nec non Actorum Lips. mense Jun. & Dec.1696， & Febr.1697 propositorum: una cum Propositione reciproca aliorum. Acta Erud. Lips. MDCXCVII, p.211-217.   
Joh. Bernoull (1696): Problema novum Mathematicis propositorum. Acta Erud. Lips. MDCXCVI, p.269, Opera Omnia vol.I, p.161 and 165, Lausannae & Genevae 1742.   
Joh. Bernouli (1697): De Conoidibus et Sphaeroidibus quaedam. Solutio anatytica Aequationis in Actis A. 1695， pag. 553 propositae, Acta Erud. Lips., MDCXCVII, p.113-118.   
Joh. Bernoulli (1697b): Solutioque Problematis a se in Actis 1696, p.269, proposit， de invenienda Linea Brachystochrona， Acta Erud.Lips. MDCXCVII, p.206, Opera Omnia vol.I, p.187-193.   
D. Bernoulli (176O): Essai d une nouvelle anatyse de la moralite causee par la petite verole,et des avantages de l'inoculation pour la prevenirHist.et Mem. de I'Acad. Roy. Sciences Paris, 1760, p.1-45; Werke Band 2,p.235-267.   
L. Bieberbach (1923): Theorie der Diferentialgleichungen， Grundlehren Bd.VI, Springer Verlag.   
L. Bieberbach (1951): On the remainder of the Runge-Kutta formula in the theory of ordinary differential equations， Zeitschr. angew. Math.Phys. (ZAMP), vol.2, p.233-248.   
G. Birkhoff and R.S. Varga (1965): Discretization errors for wel-set Cauchy problems I, Journal of Math. and Physics, volXLIV, p.1-23.   
C. de Boor and B. Swartz (1973): Collocation ai Gaussian points, SIAM J. Numer. Anal., vol.10, p.582-606.   
R. Bulirsch and J. Stoer (1964): Fehlerabschatzungen und Extrapolation mit rationalen Funktionen bei Verfahren vom Richardson-Typus, Num. Math. Vol.6, p.413-427.   
R. BulirschandJ.Stoer (1966): Numerical treatment ofordinary diferential equa tions by extrapolation methods, Num.Math.vol.8, p.1-13.   
K. Burrage (1985): Order and stability properties of explicit multivalue methods. Appl. Numer. Anal., vol.1, pp.363-379. (lyuvj. Aun-uicur suviuty Uj u gentrui usg Uj differential equation methods.B,vol.20,pp.5-20.   
K.Burrage and PMoss (1980):Simplifying assumptions for the order of paritioned multivalue eos..   
J.C.Butcher (1963): Coeficients for the study of Runge-Kuta integration processes, J. Austral. Math. Soc., vol.3, p.185-201.   
J.C. Butcher (1963a): On the integration processof A. Huta,J.Austral. MathSoc., vol.3, p.202-206.   
J.C.Butcher (1964a): Implicu Runge-Kuta Processes， Math. Comput. vol.18, p.50-64.   
J.C. Butcher (1964b): On Runge-Kuta processs of high order, J.Austral. Math. Soc. vol.IV, Part2, p.179-194.   
J.C. Butcher (1964c): Integration proceses based on Radau quadrature formulas, Math. Comput., Vol.18, p2-44.   
J.C. Butcher (1965a): A modified multistep method for the numerical integrution of ordinaryiffretaleios.J.C,vo2,5.   
J.C. Butcher (1965b): On the atainable order of Runge-Kutta methods， Math. of Comp. vol.19, p.408-417.   
J.C.Butcher (1966): On the convergence of numerical solutions to ordinary diferentil equations,th.omt.,ol,p.10   
J.C. Butcher (1967): A multistep generalization of Runge-Kutta methods with four or five stages. J. ACM, vol.14, p.84-99.   
J.C.Butcher (1969):The efective order of Runge-Kutta methods, in: Conference on the numerical solution of differential equations, Lecture notes in Math. Vol.109, p.133-139.   
J.C. Butcher (1972): An algebraic theory of integration methods, Math. Comput. Vol.26, p.79-106.   
J.C. Butcher (1975): An order bound for Runge-Kuta methods, SIAM JNum. Anal. vol.12, p.304-315.   
J.C. Butcher (1981): A eneralzationof singlymplicit methods，B,vol.21,p.15- 189.   
J.C. Butcher (1984): An application of the Runge-K utta space, BIT, vol.24, p.425- 440.   
J.C. Butcher (1985a): General linear method: a survey， Appl. Num. Math., vol.1, p.273-284.   
J.C. Butcher (1985b): The non-existence of ten stage eighth order explicit Runge-K utta methods, BIT, vol.25, p.521-540.   
G.D. Byrne and A.C. Hindmarsh (1975): A polyalgorithm for the numerical solution of ordinary differential equations, ACM Trans. on Math. Software, vol.1, No.1, p.71-96.   
G.D. Byrne and RJ. Lambert (1966): Pseudo-Runge-Kut methods involving two points, J. Assoc. Comput. Mach., vol.13, p.114-123.   
A.L. Cauchy (1824): Résume des Lecons donnees a l'Ecole Royale Polytechnique. Suite du Calcul Infinitesimal: published: Equations differentielles ordi-naires, ed. Chr. Gilain, Johnson 1981.   
A.L. Cauchy (1831): Sur la mecanique celeste et sur un nouveau calcul appelé calcul des timites, lu a l'acad. de Turin le 11 oct 1831; also: exerc. d'anal. et de pysique math, 2, Paris 1841; oeuvres (2), 12. de Parls. (Aug. 5, Nov. 21,183y, June 2y, Oct. 26,184U, etc).   
A. Cayley (1858): Amemoir on thetheory of matrices,Phil. Trans.of Royal Soc.of London,vol.CXLVIl, p.17-37, Mathematical Papers vol.2， Nr.152, p.475.   
F. Ceschino and J. Kuntzmann (1963): Problemes diférentiels de conditions initiales (methodes meriqes),d s   
F. Ceschino and J. Kuntzmann (1963): Problemes diferentiels de conditions initiales, Dunod Paris; english translation: Numerical solutions of initial value problems, Prentice Hall 1966   
F.Ceschino (1961): Modification de la longueur du pas dans Pintegration numerique par les méthodes a pas lies, Chiffres 2, p.101-106.   
F.Ceschino(962):Evaluationde lereurparpasdans lesproblemesdiferentels Chiffres vol.5, p.223-229.   
A.C. Clairaut (1734): Solution de plusieurs problemes ou il s'agit de trouver des courbes dont la propriete consiste dans une certaine relation entre leurs branches, exprimee par une Equation donnee, Memoires de Math.et de Phys. de l'Acad. Royale des Sciences, Paris, Annee MDCCXXXIV, p.196-215.   
L. Collatz (1951): Numerische Behandlung von Diferentialgleichungen, Grundlehren Band LX,Springer Verlag，458pp;second edition1955;third edition and english translation 1960.   
P. Collet and J.P. Eckmann (1980): Iterated maps on the interval as dynamical systems, Birkhuser,248pp.   
G.J. Cooper and J.H. Verner (1972): Some explicit Runge-Kuta methods of high order, SIAM J.Numer. Anal. vol.9, p.389-405.   
G.J. Cooper (1978): The order of convergence of general linear methods for ordinary differential equations. SAM, J. Numer. Anal., vol.15, pp.643-661.   
SA.Corey (1906):Amethod of approximationAmer.Math.MonthlyVl13, p.137-140.   
P.H. Cowell and A.C.D. Crommelin (1910): Investigation of the motion of Halley's comet from 1759 to 1910. Appendix to Greenwich Observations for 1909, Edinburgh, p.1-84.   
D.M. Creedon and JJ.H. Miller (1975): The stability properties of q-step backward difference schemes, BIT, vol.15, p.244-249.   
M. Crouzeix (1975): Sur Papproximation des equations différentielles operationnelles lineaires par des methodes de Runge-Kutt， These d'etat, Univ. Paris 6, 192pp.   
M. Crouzeix and F J. Lisbona (1984): The convergence of variable-stepsize, variable formula, multistep methods, SIAM J.Num.Anal. 21, p.512-534.   
C.W. Cryer (1971): A proof of the instability of backward-difference multistep methods for the numerical integration of ordinary differential equations, Tech. Rep. No.117, Comp. Sci. Dept., Univ. of Wisconsin, p.1-52.   
C.W. Cryer (1972): On the instability of high order backward-difference multistep methods, BIT, vol.12, p.17-25.   
W.J. Cunningham (1954): A nonlinear differential-difference equation of growth, Proc. Mat. Acad. Sci., USA, vol.40, p.708-713.   
A.R. Curtis (197O): An eighth order R unge-Kutta process with eleven function evalua-tions per step, Numer. Math. Vol.16, p.268-277.   
A.R. Cuius (1yiS): Hign-oraer expucu Kunge-K uua jormuiae, tneir uses, ana tmua-tions, J.Inst. Maths Applics, vol.16, p.35-55.   
C.F. Curtiss and J.O. Hirschfelder (1952): Integration of stiff equations. Proc. of the National Academy of Sciences of U.S., vol.38,p.235-243.   
G. Dahlquist and R. Jeltsch (1979): Generalized disks of contractivity for explici and implicit Ruge-uta eos.eort--796,, Inst. Techn. Stockholm.   
G.Dahlquist (1956): Convergenceand stability in the numerical integration of ordi-nary differential equations, Math. Scand., vol.4, p.33-53.   
G.Dahlquist (1959): Stability and errorbounds in the numerical integration of ordi nary differential equations， Trans. of the Royal Inst. of Techn., Stockholm,Sweden,Nr.30,p.   
G. Dahlquist (1985): 33 years of numerical instability，part.I, BIT, vol25,p.188- 204.   
J. Descloux (1963): A note on a paper by A. Nordsieck, Report No.131, Dept. of Comp. Sci., Univ. of Ilinois at Urbana-Champaign.   
P. Deuflhard and E. Hairer ed. (1983): Numerical treatment of inverse problems in differeniald inegral eioir,otoel $3 5 7 \mathrm { p p }$   
P. Deuflhard and G. Bader (1982): Multiple shooting techniques revisited, Preprint Nr.163, Univ.Heidelberg,Inst.Angew.Math.D-690 Heidelberg1. Summary published in: P. Deuflhard, E. Hairer, (1983) p.74-94.   
P. Deuflhard (1980): Recent advances in multiple shooting techniques; In: Computational techniques for ordinary differential equations (Gladwell-Sayers, ed.),Section 10,p.217272, Academics.   
P.Deufihard (1983): Order and stepsize control in extrapolation methods， Num. Math. vol.41, p.399-422.   
P. Deuflhard (1985): Recent progress in extrapolation methods for ordinary differential equations,Aev.,l275   
J. Donelson and E. Hansen (1971): Cyclic composite multistep predictor-corrector methods. SIAM, J. Numer. Anal., vol.8, pp.137-157.   
J.R. Dormand and PJ. Prince (1978): New Runge-Kutta algorithms for numerical simulation in dynamical astronomy， Celestial Mechanics， vol.18,p223- 232.   
J.R. Dormand and P.J. Prince (198O): A family of embedded Runge-Kutta formulae, J.Comp. Appl. Math. vol.6, p.19-26.   
R.D. Driver (1977): Ordinary and delay differential equations, Applied Math. Sciences 20, Springer Verlag,501pp.   
B.L. Ehle (1968): High order A-stable methods for the numerical solution of systems of D E's, BIT vol.8, p.276-278.   
N.F. Eispack (1974): B.T.Smuh， JM. Boyle, B.S.Garbow, Y Jkebe，V.C.Klema, CB Moler: Matrix Eigensytem Routines，(Fortran-translationsof algo rithms_ published in Reinsch and Wilkinson), Lecture Notes in Com-puter Science, vol.6, Springer Verlag.   
H. Eltermann (1955): Fehlerabschatzung bei naherungsweiser Losung von Systemen von Differentialgleichungen erster Ordnung, Math. Zeitschr. vol.62, p.469-501.   
R. England (1969): Error estimates for Runge-Kuta type solutions to systems of ordi-nary differential equations; The Computer J. vol.12, p.166-170.   
W.H. Enright, T.E. Hull and B. Lindberg (1975): Comparing numerical methods for stiff systems of $O \mathcal { D } \mathcal { E } _ { \mathcal { S } } ,$ BIT vol.15, p.10-48.   
W.H. Enright, K.R. Jackson, S.P. Nbrsett and P.G. Thomson (1985): Interpolants for Runge-Kutt formulas, Technical Report 180/85, Dept. Comput. Science, Toronto, Canada M5 1A5, $3 6 ~ \mathrm { p \bar { p } }$   
L. Euler (1728): Nova methodus innumerabiles aequationes diffrentiales secundi gradus reducendi ad aequationes differentiales primi gradus, Comm. acad. scient. Petrop.vol.3, p.124-137; Opera Omnia vol.XXII, p.1-14.   
L. Euler (1743): $D e$ integratione aequationum differentialium altiorum graduum,Miscellanea Berolinensia vol.7, p.193-242；Opera Omnia vol.XXII, p.108- 149. See also: Letter from Euler to Joh. Bernoulli, 15.Sept.1739.   
L. Euler (1744): Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes ., Lausannae & Genevae, Opera Omnia (intr. by Caratheodory) vol.XXIV, p.1-308.   
L. Euler (175O): Methodus aequationes differentiales altiorum graduum integrandi uterius promota， Novi Comment. acad. scient. Petrop. vol.3, p.3-35; Opera Omnia vol.XXII, p.181-213.   
L. Euler (1756): Elementa calculi variationum, presented September 16, 1756 at theAcad.of Science,Berlin;printed 1766,OperaOmnia vol.XXV,p.141-176.   
L. Euler (1768): Institutionum Calculi Integralis, Volumen Primum, Opera Omnia vol.XI.   
L. Euler (1769): Institutionum Calculi Integralis， Volumen Secundum， Opera Omnia vol.Xi.   
L. Euler (1778): Specimen transformationis singularis serienum， Nova acta. acad. Petrop., vol.12 (1794),p.58-70,Opera OmniavolVI, p.41-55.   
E. Fehlberg (1958): Eine Methode zur Fehlerverkleinerung beim Runge-Kuta-VerfahrenZAMvol.38, p.4226   
E. Fehlberg (1964): New high-order Runge-Kuta formulas with step size control for systems of first and second order differential equations, ZAMM, vol.44, Sonderheft T17-T19.   
E. Fehlberg (1968): Classical fifth-, sixth-， seventh-， and eighth order Runge-Kutta formuias with step size control; NASA Technical Report 287 (1968); extract published in Computing vol.4, p.93-106 (1969).   
E.Fehlberg (1969): Low-order classcal Runge-Kutta formulas with step size control and their application to some heat transfer problems，NASA Technical Report 315 (1969)，extract published in Computing vol.6，p.61-71 (1970).   
E. Fehlberg (1972): Classical eighth- and lower-order Runge-Kutt-Nystrom formulas with stepsize control for special second-order differential equations， NASA Technical Report R-381.   
M. Feigenbaum (1978): Quantitative universality for a class of nonlinear transformations,JStat.Phys.vol.19,p.25-52,vol.21 (1979),.669706.   
J.R. Field and R.M. Noyes (1974): Oscilations in chemical systems. IV. Limi cycle behavior in a model of a real chemical reaction, J. Chem. Physics, vol.60, p.1877-1884.   
S. Filippi and J. Graf (1986): New Runge-Kut-Nystrom formula-pairs of order 8(7),9(8). I0(9) and 11(10) for differential equations of the form $y \ ^ { \prime \prime } { = } f \left( x \ , y \right)$ , J.Comput. and Applied Math., vol.14, p.361-370.

R. Fletcher and D.C. Sorensen (1983): An algorithmic derivation of the Jordan canonical form, Amer. Math. Monthly, vol.90, No.1, p.12-16.

C.V.D. Forrington (1961-62): Extensions of the predictor-corrector method for the solution of systems of ordinary differential equations, Comput. J. 4, p.80 84.

J.BJ. Fourier (1807): Sur la propagation de la chaleur, unpublished manuscript; published: La theorie analytique de la chaleur, Paris 1822.

V. Franceschini (1980): Feigenbaum sequence of bifurcations in the Lorenz model, J.Stat, Phys. vol.22, p.397-406.

R.A. Frazer, W.P. Jones and S.W. Skan (1937): Approximations to functions and to the solutions of differential equations，Reports and Memoranda Nr.1799 (2913),Aeronautical Research Commiee. 3pp.

A.Fricke (1949): Ueber die Fehlerabschatzung des Adamsschen Verfahrens zur Inte gration gewohnlicher Diferentialgleichungen erster Ordnung， ZAMM, vol.29, p.165-178.

M.Frommer (1934): Ueber das Auftreten von Wirbeln und Strudeln (geschlossener und spiraliger Integralkurven) inder Umgebung rationaler Unbestimmtheits-stellen, Math. Ann., vol.109, p.395-424.

L.Fuchs (1866): Zur Theorie der linearen Differentialgleichungen mit verdnderlichen Coefficienten, Crelle J. f. d. r. u. angew. Math., vol.66, p.121-160 (prepublished in 'Programm der stadtischen Gewerbeschule zu Berlin, Ostern 1865").

P. Funk (1962): Variationsrechnung und ihre Anwendung in Physik und Technik, Springer Verlag, Grundlehren Bd. 94, 676 p.

C.F. Gauss (1812): Disquisitiones generales circa seriem infinitam

$$
\begin{array} { r l } & { 1 + \frac { \alpha \beta } { 1 \cdot \gamma } x + \frac { \alpha \left( \alpha + 1 \right) \beta \left( \beta + 1 \right) } { 1 \cdot 2 \cdot \gamma \left( \gamma + 1 \right) } x x } \\ & { \qquad + \frac { \alpha \left( \alpha + 1 \right) \left( \alpha + 2 \right) \beta \left( \beta + 1 \right) \left( \beta + 2 \right) } { 1 \cdot 2 \cdot 3 \cdot \gamma \left( \gamma + 1 \right) \left( \gamma + 2 \right) } x ^ { 3 } + e t c , } \end{array}
$$

Werke vol.3, p.123-162.

W. Gautschi (1962): On inverses of Vandermonde and confluent Vandermonde matri-ces, Numer. Math. vol.4, p.117-123.

C.W. Gear and D.S. Watanabe (1974): Stability and convergence of variable order multistep methods, SIAM J. Num. Anal. 11, p.1044-1058.

C.W. Gear and K.W. Tu (1974): The effect of variable mesh size on the stability of multistep methods, SIAM J. Num. Anal. 11, p.1025-1043.

C.W. Gear (1965): Hybrid methods for initial value problems in ordinary differentiai equations. SIAM J. Numer. Anal., ser.B, vol.2, p.69-86.

C.W. Gear (1971): Numerical initial value problems in ordinary differential equations, Prentice-Hall, 253pp.

A. Gibbons (1960): A program for the automatic integration of differential equations using the method of Taylor series, Computer J. vol.3, p.108-111.

S. Gill (1951): A process for the step-by-step integration of differential equations in an automatic digital computing machine， Proc. Cambridge Philos. Soc., vol.47, p.95-108.

B. Giovannini, L. Weiss-Parmeggiani and B.T. Ulrich (1978): Phase locking in coupled Josephson weak links, Helvet. Physica Acta, vol.51, p.69-74.

H.H. Goldstine (1980): A History of the Calculus of Variations, Springer Verlag, 410p.   
G.H. Golub and J.H. Wilkinson (1976): Iu-conditioned eigensystems and the computation of theJordan canonical form,AReview,vol.18,p.578-619.   
B.A. Gottwald (1985): Zur Modelierung zeiverzogerterbioogischer Prozesse,Infomatik Fachberichte,vol.109,p.350-354, Springer Verlag.   
W.B. Gragg and H.J. Stetter (1964):Generalized multistep predictor-corrector methods. J. ACM, vol.11, pp.188-209.   
W.B. Gragg (1964): Repeated extrapolation to the limit in the numerical solution of ordinary differential equations,Thesis， Univ. of California; see also SIAM J. Numer. Anal., vol.2, p.384-403 (1965).   
W.B.Gragg (1965):On extrapolationalgorithms for ordinary initial value problems， SIAMJ.Num. Anal.,ser.B,vol.2,p.384-43.   
R.D. Grigorieff (1977): Numerik gewohnlicher Differentialgleichungen 2. Teubner Studienbucher,Stt   
R.D. Grigorief (1983): Stability of multistep-methods on variable grids，Numer. Math. 42, p.359-377.   
W. Grobner (1960): Die Liereihen und ihre Anwendungen, D. Verl. d. Wis. Berlin, 2nd ed. 1967.   
T.H. Gronwal (1919): Note on the derivatives with respect to a parameter of the solu-tions of a system of differential equations, Ann. Math. vol.20, p.292-296.   
H. Hahn (1921): Theorie der reelen FunktionenSpringer Verlag Berlin, $6 0 0 \mathrm { p p }$   
W. Hahn (1967): Stability of motion, Springer Verlag, 446pp.   
E. Hairer and G. Wanner (1973): Mulistep-multistage-multiderivative methods for ordinary differential equations, Computing Vol.11, p.287-303.   
E. Hairer and G. Wanner (1974): On the Butcher group and general multi-value methods, Computing Vol.13, p.1-15.   
E. Hairer and G. Wanner (1976): A theory for Nystrom methods, Numer. Math., vol.25, p.383-400.   
E. Hairer and G. Wanner (1983): On the instability of the BDF formulas, SIAM J. Numer. Anal., vol.20, No.6, p.1206-1209.   
E. Hairer and Ch. Lubich (1984): Asymptotic expansions of the global error of fixed-stepsize methods, Numer. Math. vol.45, p.345-360.   
E.Hairer (197): Methodes de Nystrom pour l'equation diferentielle $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ Numer. Math., vol.27, p.283-300.   
E. Hairer (1978): A Runge-Kutta method of order 10, J.Inst. Maths Applics, vol.21, p.47-59.   
E. Hairer (1981): Order conditions for numerical methods for partitioned ordinary differential equations, Numer. Math., vol.36, p.431-445.   
E. Hairer (1982): A one-step method of order 10 for $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ , IMA J. Num. Anal. vol.2, p.83-94.   
P.C. Hammer and J.W. Hollngsworth (1955): Trapezoidal methods of approximating solutions of differential equations, MTAC vol.9, p.92-96.   
N.D. Hayes (1950): Roots of the transzendental equation associated with a certain difference-differential equation, J. of London Math. Soc., vol.25, p.226- 232. ytnwUjnungt-nwu mtnu Jui systems of n -th order diferential equations, J. Comput. Appl. Math., vol.8, p.3-14.   
P. Henrici (1962): Discrete variable methods in ordinary diferential equations. John Wiley & Sons,Inc.,New-York-London-Sydney.   
P.Henrici (1974):Applied andcomputational complexanalysis, Volume1,John Wiley &Sons,New York,68pp.   
Ch. Hermnite (1878): Extrait dune lettre de M. Ch. Hermite a M. Borchardt sur la formule dinterpolation de Lgrange,J.de Crelle,v84,p.；Os tome III, p.432-443.   
K. Heun (1900): Neue Methode zur approximativen Integration der Diferentialgleichungen einer unabhangigen Veranderlichen, Zeitschr. fur Math.u. Phys., vol.45, p238.   
A.C. Hindmarsh (1972): GEAR : ordinary differential equation system sotver, UCID-30001,Rev2,,imore,f.   
A.C. Hindmarsh (1980): LSoDE and LSODI, two new initial value ordinary diferential equation solvers, ACM Signum Newsletter 15,4.   
M.W. Hirsch and S. Smale (1974): Differential equations, dynamical systems and linear algebraAcad.es   
E.W. Hobson (1921): The theory offunctions of a real variable,vol.ICamridge, 670pp.   
G.'t Hooft (1974): Magnetic monopoles in unified gauge theories， Nucl. Phys. vol.B79, p.276-284.   
E. Hopf (1942): Abzweigung einer periodischen Losung von einer stationaren Losung eines Differenalsystems，Ber.math.physik.Kl. Akad.d.Wiss.Leipig, Bd.XCIV, p.-22.   
M.K. Horn (1983): Fourth and fifth-order scaled Runge-Kutt algorithms for treating dense output, SIAM JNumer. Anal. vol.20, p.558-568.   
PJ.van der Houwen (1977):Construction of integration formulas for initial vatue problems, North-Holland Amsterdam, $2 6 9 \mathrm { p p }$   
T.E. Hull W.H. Enright,B.M. Felln and A.E. Sedgwick (1972): Comparing numerical methods for ordinary differential equations, SIAM J. Numer. Anal., vol.9, p.603-637.   
T.E. Hull and R.L. Johnston (1964): Optimum Runge-Kutta methods, Math. Com-put., vol.18, p.306-310.   
T.E. Hull (1967): A search for optimum methods for the numerical integration of ordinary dierential equations,SAM Rev., vol.9, p.647-654.   
B.L. Hulme (1972): One-step piecewise potynomial Galerkin methods for initial value problems,ath. of Comput. vol.26, p.415-426.   
W.H. Hundsdorfer and M.N. Spijker (1981): A note on $B$ -stability of Runge-Kutta methods, Num. Math. Vol.36, p.319-331.   
A. Hurwitz (1895): Ueber die Bedingungen, unter welchen eine Gleichung nur Wurzebn mit negativen reellen Theilen besitzt, Math. Ann., vol.46, p273-284; Werke vol.2, p.533ff.   
E.L. Ince (1944): Ordinary differential equations， Dover Publications, New York, $5 5 8 \mathrm { p p }$   
G. Iooss and D.D. Joseph (1980): Elementary stability and bifurcation theory, Springer Verlag, 286 pp. (see chapter VII).   
C. Jordan (187o): Traite des Substitutions et des equations algebriques, Paris 667pp.   
C. Jordan (1928): Sur une formule d interpolation, Atti Congresso Bologna, vol 6, p.157-177   
B. Kaogstrom and A. Ruhe (1980): An algorithm for numerical computation of the Jordan normal form of a complex matrix; ACM Trans. Math. Software, vol.6, p.398-419. (Received May 1975, revised Aug.1977, accepted May 1979).   
S. Kakutani and L. Marcus (1958): On the non-linear difference-differential equation $\mathbf { \beta } _ { \prime } ^ { \prime } ( t ) = [ A - B y \left( t - \tau \right) ] y \left( t \right)$ ,in: Contributions to the theory of non-linear oscillations, Ed. by S.Lefschetz, Princeton, vol.IV, p.1-18.   
E. Kamke (193O): Ueber die eindeutige Bestimmtheut der Integrale von Diferential gleichugnen I1， Sitz. Ber. Heidelberg Akad. Wiss. Math. Naturw. Kl., 17. Abhandl., see also Math.Zeitschr., vol. 32, p.101-107.   
E. Kamke (1942): Diferentialgleichungen,Losungsmethoden und Losungen，Becker & Erler,Leipzig, 642pp.   
K.H. Kastlunger and G. Wanner (1972): Runge Kuuta processes with mutiple nodes, Computing vol.9, p.9-24.   
K.H. Kastlunger and G. Wanner (1972b): On Turan type implicit Runge-Kutta methods, Computing vol.9, p.317-325.   
H.B. Keller (1968): Numerical methods for two-point boundary-value problems, Blaisdell Publ. Comp., $1 8 4 \ \scriptstyle { \mathbb { p p } } .$ (see section 2.4).   
W.O. Kermack and A.G.Mc. Kendrick (1927): Contributions to the mathematical theory of epidemics (Par I), Proc. Roy. Soc., A, vol.115, p.700-721.   
R.King (1966):Runge-Kuta methods with constrained minimum eror bounds， Math. Comput., vol.20, p.386-391.   
H. Knapp and G. Wanner (1969): LIESE II A program for ordinary diferential equations using Lie-series, MRC Report No.10o8, Math. Research Center, Univ. Wisconsin,Madison,Wisc.53706.   
G. Kowalewski (1908): see Leibniz (1693).   
F.T. Krogh (1969): A variable step variable order mulistep method for the numerical solution of ordinary differential equations， Information Processing 68, North-Holland, Amsterdam, p.194-199.   
F.T. Krogh (1973): Algorithms for changing the step size, SIAM J. Num. Anal. 10, p.949-965.   
F.T. Krogh (1974): Changing step size in the integration of diferential equations using modified devided differences， Proceedings of the Conference on the Num. Sol. of ODE, Lecture Notes in Math. No.362, Springer Verlag New York, p.22-71.   
N. Kryloff and N. Bogoliuboff (1947): Introduction to non-linear Mechanics， free translation by S. Lefschetz, Princeton Univ. Press, $1 0 5 \mathrm { p p }$   
E.E.Kummer (839):Note sur integrationde lequation $d ^ { n } y / d x ^ { n } = x ^ { m } y$ par des integrales definies, Crelle J. f. d. r. u. angew. Math., vol.19, p286-288.   
J. Kuntzmann (1961): Neuere Entwickelungen der Methode von Runge-Kutta, ZAMM, vol.41,p28-31.   
J. Kuntzmann (1959): Deux formules optimales du type de Runge-Kutta, Chifres, vol.2, p.21-26. gleichungen, Zeitschr. fur Math. u. Phys., vol.46, p.435-453.   
J.L.de Lagrange (1759):Recherches sur la nature et la propagation duson, Miscell. Taurinensia t.I,Oeuvrest.1,914.   
J.LdeLagrange (762):olutiondediferensproblemsde CculItegalscel. Taurinensa,t.I,evres t.1,47668.   
J.L.de Lagrange (174): Sur les Integrales particulieres des Equations diférentielles, Oeuvres, tom.4, p.5-108.   
J.L.de Lagrange (1775): Recherche sur les Suites Recurrentes, Nouveaux Mem. de l'Acad. royale des Sciences et Belles-Lettres, Berlin. Oeuvres vol.4, p.159.   
J.L.de Lagrange (1788): Mecanique anatytique, Paris, Oeuvres t.11 et 12.   
J.L.de Lagrange (1792): Memoire sur texpression du terme general des series recurrentes, lorsque lequation generatrice a des racines egales， Nouv. Mem. de l'Acad. royale des Sciences de Berlin, Oeuvres t.5,p.627-641.   
J.L.de Lagrange (1797): Theorie des fonctions anatytiques, contenant les principes du calcul differentiel, degages de toute consideration d’infiniment petits, devanouissants，de limites et de fluxions，et reduis a Panalyse algebrique des quantites finies,Paris,1797,nouv.ed.1813,Oeuvres Tome9.   
P.S. Laplace (An $\mathbf { \Delta } \mathbf { X } \mathbf { I I I } \ = \ \mathbf { \Delta } 1 8 0 5$ ): Supplement au dixieme livre du Traite de mecanique celeste surl'ction capillaire,Paris chez Courcier, $6 5 + 7 8 \mathrm { p p }$   
P.D. Lax and R.D. Richtmyer (1956): Survey of the stabity of linear limite difference equations, Comm. Pure Appl. Math., vol.9, p.267-293.   
R. Lefever and G. Nicolis (1971): Chemical Instabilities and sustained oscillations, J. theor. Biol., vol.30, p.267-284.   
G.W. Leibniz (1691): Methodus， qua innummerarum linearum construction ex data proprietate tangentium seu aequatio inter abscissam et ordinatam ex dato valore subtangentialis, exhibetur. Letter to Huygens, in: C.I. Gerhardt, Leibnizens math. Schriften,1850, Band II, p.116-121.   
G.W. Leibniz (1693) (Gothofredi Guilielmi Leibnitzii): Supplementum Geometriae Dimensoriae seugeneralissima omnium tetra gonismorum effectio per motum: Similiterque multiplex constructio linea ex data tangentium conditione,Acta Eruditorum， Lipsiae,p.385-392；german translation:G. Kowalewski, Leibniz uber die Analysis des Unendlichen, Ostwalds Klassiker Nr.162 (1908), p.24-34.   
A.M. Liapunov (1892): Probleme general de la stabilite du mouvement, russ., trad. en francais 1907 (Annales de la Faculte des Sciences de Toulouse), reprinted 1947 Princeton Univ. Press, $4 7 4 \mathrm { p p }$   
A.M. Lienard (1928): Etude des oscillations entretenues, Revue generale de l'Elec-tricite, tome XXII, p. 901-912 et 946-954.   
E. Lindelof (1894): Sur tapplication des methodes d'approximation successives a letude des integrales reelles des equations diferentielles ordinaires, J. de Math., 4e serie, vol.10, p.117-128.   
J. Liouville (1836): Sur le developpement des fonctions ou parties de fonctions en series dont les divers termes sont assujetis a satisfaire a une meme equation différentielle du second ordre, contenant un parametre variable, Journ. de Math. pures et appl., vol.1, p.253-265.   
J. Liouville (1838): Sur la Theorie de la variation des constantes arbitraires, Liou-ville J. de Math. vol.3, p.342-349.   
J. Liouville (1841): Remarques nouveles sur l'equation de Riccati, J. des Math. pures et appl., vol.6, p.1-13.   
R. Lipschitz (1876): Sur la possibiliute d'integrer completement un systeme donne dequations differentielles, Bulletin des Sciences Math. et Astr.， Paris, vol.10, p.149-159.   
R. Lobatto (1852): Lessen over Differentiaal- en Integraal-Rekening， 2 vol., La Haye 1851-52.   
E.N. Lorenz (1979): On the prevalence of aperiodicity in simple systems, Global Analysis,Calgary 1978，ed.by M.Grmela and J.E.Marsden，Lecture Notes in Mathematics, vol.755, p.53-75.   
M. Lotkin (1951): On the accuracy of Runge-K utta methods, MTAC vol.5, p.128- 132.   
G.I. Marchuk (1975): Prostejshaya matematicheskaya model virusnogo zabolevaniya, Novosibirsk, VTS SO AN SSSR. Preprint.   
G.I. Marchuk (1983): Mathematical models in immunology. Translation series, Optimization oftwae,NewYork,Springer Verlag,5pp.   
M. Marden (1966): Geometry of polynomials， American Mathematical Society, Pro vidence, Rhode Island, 2nd edition.   
J.E. Marsden and M. McCracken (1976): The Hopf bifurcation and its applications, Springer,New York, 408pp.   
R.M. May (1976): Simple mathematical models with very complicated dynamics， Nature, vol.261, p.459-467   
R.H. Merson (1957): An operational method for the study of integration processes, Proc. Symp.Data Processing, Weapons Research Establishment, Salisbury,Australia, p.110-1 to11025.   
W.E. Milne (1926): Numerical integration of ordinary differential equations，Amer. Math. Monthly, vol.33,p.455-460.   
W.E. Milne (197o): Numerical solution of differential equations. Dover Publications, Inc.,New York, second edition.   
R.von Mises (1930):Zurnumerischen Integration von Dferentialgleichungen ZAMM, vol.10, p.81-92.   
A.R. Mitchell and J.W. Craggs (1953): Stability of difference relations in the solution of ordinary diferential equations， Math.Tables Aids Comput., vol.7, p.127-129.   
C. Moler and C. Van Loan (1978): Nineten dubious ways to compute the exponential of a matrix; AM Review,Vol20, p.801-836.   
R.E. Moore (1966): Interval Anatysis, Prentice-Hall Inc,145p.   
R.E. Moore (1979): Methods and applications of interval anatysis， SIAM studies in Appl. Math., 190pp.   
F.R. Moulton (1926): New methods in exterior balistics. Univ. Chicago Press.   
M. Muller (1926): Ueber das Fundamentalheorem in der Theorie der gewohnlichen Diferentialgleichungen，Math.Zeitschr.,vol.26,p619-645. (Kap).   
E.H. Neville (1934): Iterative interpolation, Ind. Math. Soc. J. Vol.20, p.87-120.   
I. Newton (1671): Methodus Fluxionum et Serierum Infinitarum， edita Londini 1736,Opuscula mathematica vol.I, Traduit en francais par M.de Buffon, Paris MDCCXL. (rou.). T uwsupnuc iuuruuw pruupu muuenuuu, Iipiunatui S. Pepys, Reg. Soc. Praeses, julii 5, 1686, Londini anno MDCLXXXVII.   
S.P. Nbrset and G. Wanner (1979): The real-pole sandwich for rational approximations and oscilation equations,BI vol.19, p.79-94.   
S.P. Nbrsett(1974a): One-step methods of Hermite type for numerical integration of stiff systems,,vl.14,p.6-77.   
S.P. Nbrsett (1974b): Semi explicit Runge-K uta methods， Report No.6/74, ISBN 82-7151-009-6,ept. ath.Univ.ondeim,oray, $6 8 + 7 \mathrm { p p }$   
A. Nordsieck (1962): On numerical integration of ordinary diferential equations, Math. Comp., vol.16, p.22-49.   
B. Numerov (B.VNoumerov) (1924): A method of extrapolation of perturbations. Monthly notices of the Royal Astronomical Society,vol84,p.59-601.   
B. Numerov (1927): Note on the numerical integration of $d ^ { 2 } x / d t ^ { 2 } { = } f \left( x \ , t \right)$ Astron. Nachrichten,vol230, p.359-364.   
E.J. Nystrom (1925): Ueber die numerische Integration von Diferentialgleichungen, Acta Soc. Sci. Fenn., vol.50, No.13, p.1-54.   
M. Okamoto and K. Hayashi (1984): Frequency conversion mechanism in enzymatic feedback systems,J.Theor.Biol., vol.108, p.529-537.   
J. Oliver (1975): Acuriosityof low-order expliit Runge-Kutta methods, Math. Comp., vol.29, p.1032-1036.   
M.R. Osborne (1966): On Nordsieck's method for the numerical solution of ordinary diffeential eil.,.   
B.N. Parlett (1976): A recurrence among the elements of functions of triangular matrices, Linear Algebra Appl., vol.14, p.117-121.   
G. Peano (1888): Integration par series des equations differentielles lineaires, Math. Annalen,2,.   
G. Peano (1890): Demonstration de l'integrabilite des equations differentieles ordi-naires, Math. Annalen vol.37, p.182-228; see also the german translation and commentation: G. Mie, Math. Annalen vol.43 (1893), p.553- 568.   
G.Peano (1913): Resto nelle formule di quadratura, espresso con un integrale definito，Atti Della Reale Accad. Dei Lincei, Rendiconti, vol.22,N.9, p.562-569, Roma.   
R. Pearl and LJ. Reed (1922): A further note on the mathematical theory of populationgrowth, Proceedings of the National Acad. of Sciences, vol.8, No.12, pp.365-368.   
L.M. Perko (1984): Limit cycles of quadratic systems in the plane, Rocky Mountain J. of Math., vol.14, p.619-645.   
O. Perron (1915): Ein neuer Existenzbeweis fur die Integrale der Diffrentialgleichung $y ^ { \prime } { = } f \left( x \operatorname { \lrcorner } y \right)$ , Math Annalen, vol.76, p.471-484.   
O. Perron (1918, zur Zeit im Felde): Ein neuer Existenzbeweis fur die Integrale eines_ Systems gewohnlicher Differentialgleichungen， Math. Annalen, vol.78, p.378-384.   
O. Perron (1929): Ueber Stabilitat und asymptotisches Verhalten der Integrale von Differentialgleichungssystemen, Math. Z., vol.29, p.129-160 (see par.3).   
E. Picard (189O): Memoire sur la theorie des equations aux derivees partieles et la methode des approximations successives, J. de Math. pures et appl., 4e serie, vol.6, p.145-210.   
P. Piotrowsky (1969): Stability， consistency and convergence of variable k -step methods for numerical integration of large systems of ordinary differential equations,Lecture Notes in Math., 109, Dundee 1969, p.221-227.   
H. Poincare (1881,82,85): Sur les courbes definies par les equations differentiells， J. de Math.,3e serie,t.7,p375-422,e serie,t.8,p25-296,4e srie,t., p.167-244.   
H. Poincare (1893): Les methodes nouveles de la mecanique celeste， Tome I, 480pp, Gauthier-Villars Paris.   
S.D. Poisson (1835): Theorie mathematique de la chaleur,Paris, Bachelier, 532pp., Supplement 1837, 72pp.   
B. Van der Pol (1926): On "R elaxation Oscillations", Phil. Mag., vol.2, p.978-992; reproduced in:B.vn derPol,elected Sientific Papers,vol.I,oth Holland Publ. Comp. Amsterdam (1960).   
P. Pouzet (1963): Etude en vue de leur traitement numerique des equations intégrales detype Volerra， Rev. Francais Traitement Information (Chiffes), vol.6, p.79-112.   
PJ. Prince and J.R. Dormand (1981): High order embedded Runge-Kutta formulae, J.Comp. Appl. Math. vol.7, p.67-75.   
H. Prufer (1926): Neue Herleitung der Sturm-Liouvillschen Reihenentwicklung stetiger Funktionen, Math. Annalen vol. 95, p.499-518.   
R. Radau (1880): Etude sur les formes d'appoximation qui servent a calculer la valeur numerique d'une integrale definie, Liouville J. de Mathem. pures et appl., 3eser., tome VI, p.283-336. (Voir p.307).   
A. Ralston (1962): Runge-Kutta methods with minimum error bounds， Math. Com-put., vol.16, p.431-437, corr. vol.17, p.488.   
Lord Rayleigh (1883): On maintained vibrations， Phil. Mag. Ser.5, vol.15, p.229- 235.   
W.T. Reid (1980): Sturmian theory for ordinary differential equations, Springer Verlag, Appl. Math., Serie31, 559pp.   
J. Riccati (1712): Soluzione generale del Problema inverso intomo a raggi osculatori,., determinar la curva, a cui convenga una tal'espressione, Gioale de'Letterati d'Italia, vol.11, p.204-220.   
J. Riccati (1723): Animadversiones in aequationes diferentiales secundi gradus, Acta Erud. Lips.,anno MDcCXxiII, p.502-510.   
L.F. Richardson (1910): The approximate arithmetical solution by finite differences of physical problems including differential equations, with an application to the stresses in a masonry dam, Phil. Trans., A, vol.210, p.307-357.   
L.F. Richardson (1927): The deferred approach to the limit, Phil. Trans. A, vol. 226, p.299-349.   
B. Riemann (1854): Ueber die Darstelbarkeit einer Function durch eine trigonometrische Reihe, von dem Verfasser behufs seiner Habilitation an der Universitat zu Gottingen der philosophischen Facultat eingereicht; collected works pp. 227-265.   
W. Romberg (1955): Vereinfachte numerische Integration， Norske Vid. Selsk. Forhdl, vol.28, p.30-36.   
E. Rothe (1930): Z weidimensionale parabolische Randwertaufgaben als Grenzfall eindimensionaler Randwertaufgaben,Math. Annalen,vol.102,p.650670 method, Appl. Math. Sci. 22, Springer Verlag,396pp.   
E.J. Routh (1877): A Treatise on the stabity of a given state of motions, being the essay to which the Adams prize was adjudged in 1877, in the University of Cambridge. London 108pp.   
F.J. Routh (1884): A Treatise on the dynamics of a system of rigid bodies，pan l and I1, 4th edition (st ed.860,6th ed.1897,german translation with remarks of F.Klein 1898).   
D. Ruelle and F. Takens (1971): On the nature of turbulence, Commun. Math. Physics, vol.20, p.167-192.   
C. Runge and H. Konig (1924): Vorlesungen liber numerisches Rechnen，Grund-lehren XI,Spriger Verlag,p.   
C. Runge (1895): Ueber die numerischeAuflosungvon Dferentialgleichungen,Math. Ann., vol.46, p.167-178.   
C.Runge (1905): Ueber dienumerische Auflosung totalerDiferentialgleichungen Gottinger Nachr., p.252-257.   
H. Rutishauser (1952): Ueber die Instabilitat von Methoden zur Integration gewohnlicher Differentialgleichungen, ZAMP, vol.3, p.65-74.   
D. Sarafyan (1966): Error estimation for Runge-Kutta methods through pseudoiterative formulas; Techn. Rep. Nol4, Lousiana State Univ., New Orle-ans, May 1966.   
L. Scheeffer (1884): Zur Theorie der stetigen Funktionen einer reellen Veranderlichen, Acta Mathematica, vol.5, p.183-194.   
I. Schur (19o9): Ueber die charakteristischen W urzeln einer linearen Substitution mit einer Anwendung auf die Theorie der Integralgleichungen, Math.Ann., vol.66, p.488-510.   
L.F. Shampine (1979): Storage reduction for Runge-K utta codes， ACM Trans. Math. Sofware, Vol.5,p.245-250.   
L.F. Shampine and L.S. Baca (1984): Fixed vs. variable order R unge-Kutta, Rept. SAND84-141ia Nat's.，queque, ic, $5 7 \mathrm { p p }$   
L.F. Shampine and M.K. Gordon (1975): Computer Solution of Ordinary Differential Equations, The Initial Value Problem， Freeman and Com-pany, San Francisco, 318pp.   
L.F. Shampine and H.A. Watts (1979): The art of writing a Runge-Kutta code. I1, Appl. Math. Comput., vol.5, p.93-121.   
L.F. Shampine, H.A. Wats and S.M. Davenport (1976): Sotving nonstiff ordinary differential equations - The state of the ar, SIAM Rev.vol.18,p.376-410.   
E.B. Shanks (1966): Solutions of differential equations by evaluations of functions, Math. of Comp. vol.20, p.21-38.   
D. Sommer (1965): Numerische Anwendung impliziter Runge_kutta-Formeln, ZAMM, vol. 45, Sonderheft, p. T77-79.   
Shi Songling (1980): A concrete example of the existence of four limit cycles for plane quadratic systems, Sci. Sinica, vol.23, p.153-158.   
G.F. Simmons (1972): Differential equations with applications and historical notes, MC Graw-Hill,465pp.   
R. Skeel (1976): Anatysis of fixed-stepsize methods， SIAM J. Numer. Anal., vol.13, p.664-685.   
N.D.Jkwi (1)ro). Lyuivuwn jorms Uj muusitp jurmuud, Repon N7o"yto, Depl. of Comp. Sci., Univ. of Ilinois at Urbana-Champaign.   
M.N. Spijker (1971): On the structure of error estimates forfinte diference methods. Numer. Math., vol.18, pp.73-100.   
JF. Steffensen (1956): On the restricted problem of three bodies， K.danske Vidensk.Selsk., Mat-fys. Medd. 30 Nr.18.   
H.J. Stettr (197O): Symmetric two-step algorihms for ordinary differential equations, Computing vol.5, p.267-280.   
H.J. Stetter (1973): Anatysis of discretization methods for ordinary differential equa-tions, Springer Verlag, Berlin-Heidelberg-New York .   
C. Stormer (1907): Sur les trajectoires des corpuscules electrises. Arch. sci. phys. nat., Geneve, vol.24, p.5-18, 113-158, 221-247.   
C. Stormer (1921): Methodes d'integration numerique des equations diferentielles ordinaires. C.R. congr. interm. math., Strasbourg, p.243-257.   
J.Stoer andR.Bulirsch(1973):Einfuhrung indie numerische Mathemaik，Springer Verlag,1st ed. 1973、English translation 1980 (see section 7.3.5).   
J. Stoer and R. Bulirsch (1980): Introduction to Numerical Analysis, Springer Verlag, $6 0 9 \mathrm { p p . , }$ german edition 1973.   
C. Stoermer (1907): Sur les trajectoires des corpuscules electrises， Arch. sci. phys. nat., Geneve, vol.24, p.5-18, 113-158, 221-247.   
C. Stoermer (1921): Methodes d'integration numerique des equations diferentieles ordinaires, C.R. congr. interm. math., Strasbourg, p.243-257.   
A.H. Stroud and D.D. Stancu (1965): Quadrature formulas with multiple Gaussian nodes, SIAM J. Numer. Anal., ser.B., vol.2, p.129-143.   
Ch. Sturm (1829): Buletin des Sciences de Ferussac, tome XI, p.419,see also: Algebre de Choquet et Mayer (1832).   
Ch. Sturm (1836): Sur les equations diferentieles lineaires du second ordre, Journal de Math. pures et appl. (Liouville)，vol.1, p.106-186 (see also p.253, p.269, p.373 of this volume).   
J. Todd (1950): Notes on modern numerical analysis， I， Math. Tables Aids Com-put., vol.4, p.39-44.   
W. Tollmien (1938): Ueber die Fehlerabschatzung beim Adamsschen Verfahren zur Integration gewohnlicher Differentialgleichungen, ZAMM, vol.18, p.83-90.   
W. Tomson (Lord Kelvin) and P.G.Tait (1879): Treatise on natural philosophy (Vol.I., Part I),Cambridge; New edition1890,508pp.   
W. Uhlmann (1957): Fehlerabschatzungen bei Anfangswenaufgaben gewohnlicher Differentialgleichungssysteme 1. Ordnung， ZAMM (Zeitschr. Angew. Math. Mech.) vol.37, p.88-99.   
P.F. Verhuist (1845): Recherches mathematiques sur la loi d'accroissment de la po-pulation, Nuov. Mem. Acad. Roy. Bruxelles, vol.18, p.3-38.   
J.H. Verner (1978): Explicit Runge-Kuta methods with estimates of the local trunca-tion error, SIAM J.Numer. Anal. vol.15, p.772-790.   
L. Vietoris (1953): Der Richtungsfehler einer durch das Adamssche Interpolationsverfahren gewonnenen Naherungslosung einer Gleichung $y ^ { \prime } =$ J $\textit { f } ( x , y )$ Oesterr.Akad. Wiss., Math.-naturw. Kl.， Abt. IIa, vol.162, p.157-167 and p.293-299.   
V. Volterra (1934): Remarques sur la Note de M. Regnier et Mue Lambin. C.R.Acad. Sc. t. CXClX, p.1682. See also: V.Volterra - U.d'Ancona , Les associations biologiques au point de vue mathematique, Paris 1935.   
W. Walter (97):Diffrenaland intgral inequaliesSpringer Verag 3p man edition 1964.   
W. Walter (1971): There is an elementary proofof Peano's existence theorem,Amer. Math.Monthly,vol.78,p.170-173.   
G.Wanner (1969): Integration gewohnlicher Diferentialgleichungen，Lie Reihen, Runge-Ku-etoeneiba.   
G. Wanner (1973): Runge-Kutta methods with expansions in even powers of h， Computing vol.11, p.81-85.   
G. Wanner (1983): On Shis counter example for the 16th Hilber problemInternal Rep.Sect. de Math.，Univ.Geneve 1982; in german in:Jahrbuch Ueberblicke Mathematik 1983, ed. Chattrji, Fenyo, Kulisch, Laugwitz,Liedl, BI Mannheim, p.9-24.   
H.A. Watts (1983): Starting stepsize for an ODE solver, J. Comp. Appl. Math. vol.9, p.177-191.   
K. Weierstrass (1858): Ueber ein die homogenen Functionen zweiten Grades betref. fendes Theorem, nebst Anwendung desselben auf die Theorie der kleinen Schwingungen， Monatsber. der Konigl. Akad. der Wiss, 4. Marz 1858, Werke Bd.I, p.233-246.   
J. Weissinger (1950): Eine verscharfte Fehlerabschatzung zum Extrapolationsverfahren von Adams, ZAMM, vol.30, p.356-363.   
O. Wilde (1892): Lady Windermere's Fan, Comedy in four acts.   
J.H. Wilkinson (1965): The algebraic eigenvalue problem， Monographs on numerical analysis, Oord,6pp.   
J.H. Wilkinson and C. Reinsch (1970): Linear Algebra, Grundlehren Band 186, Springer Verlag,439 pp.   
A. Wintner and F.D. Murnaghan (1931) : A canonical form for real matrices under orthogonal transformations,Proc. Nat. Acad. Sci. U.S.A., vol.17,p.417 420.   
E.M. Wright (1945): On a sequence defined by a non-linear recurrence formula, J. of London Math. Soc., vol.20, p.68-73.   
E.M. Wright (1946):The non-linear difference-differential equation, Quart. J. of Math., vol.17, p.245-252.   
E.M. Wright (1955): A non-linear difference-differential equation, Jf.d.r.u. angew. Math., vol.194, p.66-87.   
K. Wright (1970): Some relationships between implicut Runge-Kutta collocation and Lanczos T methods，and their sability properties，BI vol.10,p.217-227.   
H. Wronski (1810): Premier principe des methodes algorithmiques comme base de la technique algorithmique, publication refused by the Acad. de Paris (for more details see: S.Dickstein, Int. Math. Congress 1904, p.517).   
M. Zennaro (1986): Natural continuous extensions of Runge-K uta methods, Math. Comput. Vol.46, p.119-133.   
JA. Zonneveld (1963): Automatic integration of ordinary differential equations， Report R743,Mathematisch Centrum, Postbus 4079, 1009AB Amsterdam. Appeared in book form 1964.   
R. Zurmuhl (1948): Runge-Kutt-Verfahren zur numerischen Integration von Differ-entialgleichungen n-ter Ordnung, ZAMM, vol.28, p.173-182.   
R. Zurmuhl (1952): Runge-Kutta Verfahren unter Verwendung hoherer Ableitungen, Z angew. Math. Mech. vol.32, p.153-154.


<!-- chunk 0008: pages 491-504 -->
# Symbol Index

A81 tensor product 343   
a(1） B-series coefficients 243, 244   
$\boldsymbol { B } ^ { J } \left( \mathfrak { a } , \mathfrak { y } \right)$ B-series 244   
$B \left( p \right)$ quadrature order 204   
bj（0） continuous method 179   
$c _ { i } , a _ { i j }$ ， $b _ { j }$ RK coefficients 132f   
C error constant 320, 365,429   
$C _ { p + 1 }$ local error constant 319   
$C \left( \eta \right)$ simplifying assumptions 203   
D differential operator 250   
D(5） simplifying assumptions 203   
$D _ { \pm } ^ { \pm } m \left( x \right)$ Dini derivates 54   
d(t） difference set 244   
E principal part of S 392   
$e _ { p } ( x )$ global error coefficient 211, 212   
f[xn ,..,xπ-j] divided differences 347   
F(1)（()）) elementary differential 145,147, 264, 268, 279   
8j(n） variable step size coefficients 348   
h step size 128f   
Kq（s） Peano-kernel 322   
1=(1021) Nordsieck coefficients 361, 367   
L Lipschitz constant 33, 51   
L(y,x,h) difference operator 316, 427   
LNTa labelled N-trees 264   
LSq special labelled trees 149   
LTq,LT labelled trees 145,243   
LTPg, LTP labelled P-trees 278, 281   
NTa N-trees 264   
P(c,y） P-series 281   
P(EC）M predictor-corrector 388   
P(EC）M predictor-corrector 375, 387   
matrix norm 51,52   
R(x，x0） resolvent 64   
S matrix of general linear method 386   
sub-tree 244   
21313 trees 147   
[e,..,!m] com posite tree 152   
a[t1)stm] com posite tree 278   
Tq,T rooted trees 146,243   
TiTik extrapolation tableau 219, 273   
TPTp P-trees 278, 281   
V(y1...,yn) Liapunov function 87   
W(x） Wronskian 64   
Iyl vector norm 50   
y(x） Euler polygon 32   
y(x,x0,yo) solution 97   
n=z(xn,h) correct value function 386   
QjBj multistep coefficients 315, 351   
α（t） coefficient 146, 147, 264, 268, 278   
β;(n) variable step size coefficients 349   
y(t） order products 147, 150, 268   
ASR backward differences 305   
μ(@） logarithmic norm 59   
中（h） starting procedure 386   
（2） weights 150,266,268   
Φ;(n) divided differences 349   
（n） divided differences 348   
Φ(x0,y0,h） increment function 159, 211, 343,386, 405   
Φ（x，y,h） adjoint method 214   
order of a tree 145,147, 268, 278   
(5）,0(5） generating polynomial 317   
T,Ta one-node trees 146, 278

# Subject Index

Abel-Liouville-Jacobi-Ostrogradskii   
identity 65   
Adams methods 305f as Nordsieck methods 360, 363,367 error constant 320 variable step size 347   
Adjoint matrix 71   
Adjoint method 214 asymptotic expansion 216 general linear methods 412   
Aitken-Neville algorithm 221   
Arenstorf orbits 128, 197   
Asymptotic expansion 212 general linear methods 403f in $h ^ { 2 }$ 217,226, 416 second order equations 429   
Asymptotic solutions for small parame  
ters 110   
Asymptotic stability 89   
Autonomous systems 69   
B-series 242, 244   
Backward differences 305   
Backward differentiation formulas (see BDF)   
BDF 311, 312 as Nordsieck methods 368, 369 stability 328 variable step size 350, 356, 359   
Bernoulli equation 13   
Bernoulli numbers 365   
Bessel equation 23   
Boundary conditions 101   
Boundary value problems 101   
Brachystochrone problem 7, 12, 22   
BRUS 237,238   
Brusselator 112, 172, 237 full 114 with diffusion 381   
Bulirsch sequence 221   
Butcher barriers 189   
Butcher's 6-th order method 189   
Butcher's Lobatto formulas 205   
Butcher's methods of order 2s 203,   
204,205   
Ceschino's method 168   
Characteristic equation 16, 70 delay equations 290   
Characteristic polynomial 70   
Chemical reactions 111   
Clairaut differential equation 8, 13   
Collocation methods 206 equivalence to RK 206 order 207 with multiple nodes 251   
Collocation polynomial 206   
Composition of B-series 245   
Composition of RK methods 242   
Consistency conditions 318 general linear methods 393 second order equations 426   
Constant coefficients 69 geometric representation 77 numerical computations 72   
Continuous RK methods 176 for delay equations 289, 301 for DOPRI5 179   
Convergence Euler's method 31 general linear methods 394 multistep methods 340, 344 Nystrom methods 270 RK methods 156 second order equations 427 variable step size multistep 357   
Convergence monitor 230   
Correct value function 386   
Corrector 308

Cowell and Crommelin's method 423   
Critical points 77, 78   
Cyclic multistep methods 389   
D-stability 328   
D02CAF 378   
Dahlquist barrier (first) 326, 332   
DEABM 374   
Defect 55   
Delay differential equations 286   
stability 291   
Dense output 176   
Derivatives   
numerical 183   
with respect to initial values 97   
with respect to parameters 95   
Diagonal implicit RK-method 200   
Diagonalization 69   
DIFEX1 236   
Difference equation 27   
Differential equation of Laplace 140,   
304   
Differential inequalities 54   
for systems 61   
DIFSUB 376   
Dini derivatives 54   
DIRK-method 200   
Discontinuous equations (numerical   
study)180   
Discrete Laplace transformation 363   
Divided differences 347   
DOPRI5 171, 433   
DOPRI8 195, 435   
DOPRIN 273, 447   
Dormand and Prince method 171   
continuous extension 179   
second order equations 272   
Drops 140   
Effective order 247   
Ehle's methods 210   
Eigenfunctions 105   
Eigenvalue 69   
Eigenvector 69   
Elementary differential 145, 264, 268   
279,280

Embedded RK formulas 167 of high order 193   
Encke's method 419   
End-vertex 264   
Enzyme kinetics 295   
EPISODE 375   
Equiv alence of RK methods 249 labelled trees 146 N-trees 264 P-trees 278   
ERK 132, 200   
Error global 159, 211 local 160,315,391   
Error coefficients 158   
Error constant 319, 320 Nordsieck methods 365 second order equations 429   
Error estimate 57, 156 of Euler's method 36 practical 165   
Estimation of the global error 159   
Euler polygons 6, 32 convergence 31 error estimate 36 for systems 50   
Euler's method 6, 32, 306 implicit (backward) 199,307   
Euler-Maclaurin formula 213   
Existence theorem 31 for systems of equations 49 of Peano 37 using iteration methods 41 using Taylor series 43   
Explicit Adams methods 305, 306   
Explicit RK methods 132 arbitrary order 228 high order 185   
External stages 390   
Extrapolation methods 219 as Runge-Kutta methods 228 233 order 220 second order equations 271 with symmetric methods 223   
Faa di Bruno's formula 148

Father 145

Fehlberg's methods 170, 194 multiderivative 254,283   
Feigenbaum cascades 121 number 122   
FILGR9 273   
Forward step procedure 386   
Fourier 28   
Fundamental lemma 56   
GBS method 224, 271   
General linear methods 385, 390 convergence 394 order 393 order conditions 396 stability 391   
Generating functions for the $\gamma _ { i }$ 308   
Generating polynomials of multistep methods 317   
Gerschgorin's theorem 91   
Gill's method 138   
Global error 159, 211   
Gragg's method 224   
Greek-Roman transformation 332   
Gronwall lemma 61   
Hammer and Hollingsworth's method   
200,201,203   
Hanging string 26   
Harmonic sequence 221   
Heat conduction 28, 103   
Hermite interpolation 251   
Heun's methods 133   
Higher derivative methods 250   
Hiibert's 16th problem 123   
Hopf bifurcation 113   
Hybrid methods 385   
Hypergeometric functions 22   
Immunology 297   
Implementation of multistep methods   
372   
Implicit Adams methods 306, 307 as Nordsieck methods 360, 363, 367,368   
Implicit differential equation 8   
Implicit midpoint rule 199, 201   
Implicit output 180   
Implicit RK methods 199 as collocation methods 206 based on Gaussian formulas 203 based on Lobatto quadrature 204 existence of solution 201   
Increment function 159 general linear methods 386   
Index equation 21   
Infectious disease modelling 294   
Infinite series 4   
Inhomogeneous linear equation 10 systems 66   
Initial value 1   
Integro-differential equations 299   
Internal stages 390   
Inverse tangent problem 6   
IRK-method 200   
Irreducible methods 321   
JACB 236, 238   
Jacobian elliptic functions 236   
Jordan canonical form 74   
Josephson junctions 115, 116   
Kronecker tensor product 343   
Kuntzmann's methods of order 2s   
203,204,205   
Kutta's 3/8 rule 137   
Labelled N-tree 263   
Labelled P-tree 278   
Labelled tree 145   
Lady Windermere's Fan 35, 99, 160,   
345   
LAGR 237, 238   
Lagrange 25   
Large parameters 109   
Liapunov functions 87   
Limit cycle 107, 113 existence proof 107 unicity 124   
Linear differential equations 15 homogeneous 15 inhomogeneous 16,17, 66 systems 63 weak singularities 20 with constant coefficients 15, 69 general 315   
Lipschitz condition 33, 340 one-sided 58   
Local error 160, 211 general linear methods 391 multistep 315 numerical estimation 372   
Local extrapolation 196   
Logarithmic norm 59, 62   
Lorenz model 117, 118   
LSODE 376   
Madam Imhof's cheese pie 331   
Majorant method 44   
Matrix norms 51   
Merson's method 169   
Method of lines 3,381   
Midpoint rule 130, 309 implicit 199   
Milne-Simpson methods 310   
Multi-step multi-stage multi-derivative   
methods 391   
Multiderivative methods 250, 253,   
391 order conditions 256   
Multiple characteristic values 19   
Multistep formula as general linear method 387 characteristic equation 326 cyclic 389 generalized 385 irreducible 321 modified 385 parasitic solution 327 Peano kermel 322 stability 326,328 symmetric 335 variable step size 347   
N-tree of order q 264   
Newton's interpolation formula 305,   
347   
Nonlinear variation-of-constants formula 98   
Nordsieck methods 360f as general linear methods 389 equivalence with multistep 363   
Nordsieck vector 360, 369   
Norm 50 logarithmic 59 of a matrix 51   
Normal matrices 80   
Numerical ex amples comparisons of codes 236 extrapolation methods 222 4th order methods 139,174 high order methods 196 multistep codes 378 second order equations 273   
Numerov's method 423   
Nystrom methods construction 268 convergence 270 general linear methods 391 multistep 309 order conditions 267, 283   
Obreschkoff methods 253   
ODEX 236, 440   
ODEX2 273, 443   
One-sided Lipschitz condition 58   
One-step methods 127, 211   
Optimal formulas 137   
Optimal order extrapolation 229 multistep 374   
Order Adams methods 318, 319 extrapolation methods 220 general linear methods 393 labelled tree 145 multistep methods 317 RK methods 133 variable step size multistep 351   
Order barriers (Butcher) 185,189   
Order barriers (Dahlquist) 332, 429   
Order conditions general linear methods 396 multiderivative methods 256 multistep 315, 317 number of 153 Nystrom methods 267, 268 RK methods 142,144,153,247   
Order control extrapolation 228, 232 multistep 372

Oregonator 114, 115   
Orthogonal matrix 71   
P-series 281   
P-trees 277,278, 280   
Parasitic solution 327   
Partial differential equations 3, 381   
Partitioned systems 255, 276   
Peano kermel 322   
Pendulum equation 124   
Perimeter of the ellipse 23   
Periodic solution 107   
Phase-space 77   
Picard iteration 42   
for systems 52   
PLEI 237, 238,239   
Pleiades problem 237   
Poincare sections 107, 120   
computations 180   
Population dynamics 292   
Preconsistency conditions 397   
Predictor-corrector process 307, 387   
Prince and Dormand's method 195   
at high tolerances 197   
Principal error term 158   
Principle of the argument 330   
Propagation of sound 25   
Pseudo Runge-Kutta methods 385   
q-derivative RK method 250   
Quasimonotone 61   
Radau scheme 199   
Rational extrapolation 221   
Recurrence relations for the $\boldsymbol { \gamma } _ { i }$ 308   
Regular singular point 22   
Resolvent 64   
RETARD 289, 450   
Retarded arguments 286   
Riccati equation 41   
Richardson extrapolation 165, 177   
Rigorous error bounds 156   
Romberg sequence 221   
Root of a tree 145   
Root condition 328

Rothe's method 3, 381   
Rounding error reduction 430   
Routh tableau 85, 86 computation 86   
Routh-Hurwitz criterion 82   
Runge's methods 133   
Runge-Kutta methods delay 288 diagonal implicit 200 explicit 132f general formulation 132,142 implicit 199,200 of order four 133 singly diagonal implicit 200 "the" 137 violating (1.9) 282   
Schur decomposition 70   
Schur norm 52   
Schur-Cohn criterion 336   
SDIRK-method 200 order three 203   
Second order equations 11, extrapolation methods 271 multistep methods 418f Nystrom methods 261f Runge-Kutta methods 260   
Shooting method 102   
Simplifying assumptions 134, 203, 401   
Singularities 20   
SN-trees 267, 268   
Son 145   
Son-father mapping 145   
Special labelled trees 149   
Spherical pendulum 113   
Stability asymptotic 89 BDF 328 delay equations 291 general linear methods 391 multistep formula 326 non-autonomous systems 90 nonlinear systems 89 second order equations 424 variable step size multistep 352   
Stable in the sense of Liapunov 81   
Starting procedure 304, 386   
Starting step size 182   
Steady-state approximations 109   
Steam engine governor 92   
Step size control 166 extrapolation methods 228, 232 multistep methods 372 numerical study 172, 232   
Step size freeze 183   
Step size ratio 352, 372   
Stoermer's methods 273, 419, 423   
Strange attractors 117   
Strictly stable methods 405   
Sturm sequence 83   
Sturm's comparison theorem 103   
Sturm-Liouville eigenvalue problems 103   
Subordinate matrix norms 51   
Symmetric methods 216 asymptotic expansion 217 general linear methods 415 multistep 335   
Systems of equations 25 autonomous 69 linear 63 second order 260 with constant coefcients 69   
Taylor expansion of exact solutions 144, 146 of RK solutions 131, 143,150   
Taylor series 42 convergence proof 44 recursive computation 45   
Three body problem 127   
Three-eighth's rule 137   
Time lags 286   
Total differential equation 10   
Trapezoidal rule 199   
Tree 146 number of 147   
Two body problem 236   
TWOB 236, 238   
Unitary matrix 71   
Van der Pol's equation 107, 236   
Variable step size Adams 347 BDF 350 multistep methods 347f   
Variation of constants 17, 66 nonlinear 98   
Variational Calculus 7   
Variational equation 97   
VDPL 236, 238   
Vector notation 2, 50   
Vibrating string 25   
Weak singularities 20 for systems 67 RK methods applied to 164   
Weakly stable methods 411   
Work-precision diagrams 139, 175,   
181, 196,197,222,227,240,274, 379,380,384   
Wronskian 18, 64   
Zero-stability 328   
Zonneveld's method 169

# Springer Series in Computational Mathematics

Editorial Board: R.L.Graham, J.Stoer, R.Varga

Springer-Verlag Berlin Heidelberg New York London Paris Tokyo

Volume 7 D.Braess

# Nonlinear Approximation Theory

1986. 38 figures. XIV, 290 pages. ISBN 3-540-13625-8

Contents: Preliminaries. - Nonlinear Approxination: The Functional Analytic Approach. - Methods of Local Analysis. - Methods of Global Analysis. - Rational Approximation. - Approximation by Exponential Sums. - Chebyshev Approximation by y-Polynomials.-Approximation by Spline Functions with Free Nodes. - Appendix: The Conjectures of Bernstein and Erdos. -Bibliography.- Index.

Volume 6 F.Robert

# Discrete Iterations

A Metric Study Translated from the French by Jon Rokne 1986. 126 figures. XVI, 195 pages. ISBN 3-540-13623-1

Contents: Discrete Iterations and Automata Networks: Basic Concepts.- A Metric Tool. - The Boolean Perron-Frobenius and Stein-Rosenberg Theorems.- Boolean Contraction and Applications.- Comparison of Operating Modes.- The Discrete Derivative and Local Convergence. - A Discrete Newton Method.- General Conclusion. - Appendices 1-4. - Bibliography. -Index.

# Volume 5 V.Girault, P.-A. Raviart

# Finite Element Methods for Navier-Stokes Equations

Theory and Algorithms

1986.21 figures. X, 374 pages. ISBN 3-540-15796-1

Contents: Mathematical Foundation of the Stokes Problem. - Numerical Solution of the Stokes Problem in the Primitive Variables. - Incompressible Mixed Finite Element Methods for Solving the Stokes Problem. - Theory and Approximation of the Navier-Stokes Problem. - References. - Index of Mathematical Symbols.- Subject Index.

# Springer Series in Computational Mathematics

Editorial Board: R.L.Graham, J.Stoer, R. Varga

Volume 4 W.Hackbusch

# Multi-Grid Methods and Applications

1985. 43 figures, 48 tables. XIV, 377 pages. ISBN 3-540-12761-5

Contents: Preliminaries. - Introductorv Model Problem. - General Two-GridMethod.-General Mulu-Grid Iteration.-Nested Iteration Technique.- Convergence of the Two-Grid Iteration.- Convergence of the Multi-Grid Iteration. - Fourier Analysis.- Nonlinear Multl-Grid Methods.- Singular Perturbation Problems. - Eliptic Systems -Eigenvalue Problems and Singular Equations.- Continuation Techniques. - Extrapolation and Defect Correction Techniques.- Local Techniques. - The Multi-Grid Method of the Second Kind.- Bibliography. - Subject Indev

Volume 3 N.Z.Shor

# Minimization Methods for Non-Differentiable Functions

Translated from the Russian by K. C. Kiwiel, A. Ruszczy nski [985. VII, 162 pages. ISBN 3-540-12763-1

Contents: Introduction. - Special Classes of Nondifferentiable Functions and Generalizations of the Concept of the Gradient. - The Subgradient Method. - Gradient-type Methods with Space Dilation. - Applications of Methods for Nonsmooth Optinization to the Solution of Mathematicul Programming Problems.- Concluding Remarks. - References. - Subjcct Index.

Volume 2

J.R. Rice,R.F.Boisvert

# Solving Elliptic Problems Using ELLPACK

1985. 53 figures. X, 497 pages. ISBN 3-540-90910-9

Contents: The ELLPACK System. - The ELLPACK Modules. - Performance Evaluation. - Contributor's Guide. - System Programming Guide. - Appendices. - Index

Volume 1

# QUADPACK

A Subroutine Package for Automatic Integration

By R.Piessens. E.de Doncker-Kapenga, C.W.Uberhuber, D.K.Kahaner

1983. 26 figures. VIII,301 pages. ISBN 3-540-12553-1

Springer-Verlag Berlin Heidelberg New York London Paris Tokyo

Contents: Introduction. - Theoretical Background. - Algorithm Descriptions. - Guidelines for the Use of QUADPACK. - Special Applications of QUADPACK. - Implementation Notes and Routine Listings. - References.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0504/auto/images/7c37ed8aaab031a238e665459c6cabc70b97a9ec5358bedce1a66706c45ad533.jpg)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0504/auto/images/4ce921a295ea6febe793b2476377391b7ec165d202611561bf206ad307157d4b.jpg)

Hairer, Solving ordinary differential equations

DATE DUE

# Hairer· Norsett Wanner: Solving Ordinary Differential EquationsI

The subject of the book is the solution of nonstiff ordinary differential equations. The first chapter describes the historical development of the classical theory of differential equations from Newton and Leibniz to limit cycles and strange attractors. In a second chapter one-step methods are considered. A modern treatment of Runge-Kutta methods, continuous methods for dense output, graphics and delay differential equations is given. Also included are extrapolation methods and direct methods for second order differential equations. The third chapter begins with the classical theory of multistep methods, treats variable step size and Nordsieck methods and their numerical implementation, and concludes with the theory of general linear methods.

Many applications from physics, chemistry, biology and astronomytogetherwithcomputerprogramsandumerical comparisons are presented.
