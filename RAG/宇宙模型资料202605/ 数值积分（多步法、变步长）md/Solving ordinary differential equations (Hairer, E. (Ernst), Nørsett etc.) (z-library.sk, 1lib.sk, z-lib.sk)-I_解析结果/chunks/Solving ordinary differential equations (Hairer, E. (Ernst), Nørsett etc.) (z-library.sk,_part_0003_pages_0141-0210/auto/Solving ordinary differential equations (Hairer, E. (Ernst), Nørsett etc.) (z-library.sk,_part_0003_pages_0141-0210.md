is a universal constant, the Feigenbaum number. The repeated doublings of the periods at $b _ { 1 } , b _ { 2 } , b _ { 3 } , \ldots$ are called Feigenbaum cascades.

# Exercises

1. The Van der Pol equation (16.2) with e ${ \bf \Phi } = 1 { \bf \Phi }$ possesses a limit cycle of period T =6.6632868593231301896996820305 passing through ${ } y _ { 2 } { = } 0 , { } y _ { 1 } { = } A$ where A = 2.00861986087484313650940188. Replace now (16.2) by

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = y _ { 2 } ( A - y _ { 1 } ) } } \\ { { \nonumber } } \\ { { y _ { 2 } ^ { \prime } = ( ( 1 - y _ { 1 } ^ { \ 2 } ) y _ { 2 } - y _ { 1 } ) ( A - y _ { 1 } ) } } \end{array}
$$

so that the limit cycle receives a stationnary point. Study the behaviour of a solution starting in the interior, e.g.at ${ y _ { 1 0 } } ^ { = 1 }$ ， y20=0.

2. (Frommer (1934)). Consider the system

$$
y _ { 1 } ^ { \prime } = y _ { 2 } + 2 y _ { 1 } y _ { 2 } - y _ { 2 } ^ { 2 } , \quad y _ { 2 } ^ { \prime } = y _ { 1 } + ( 1 + \epsilon ) y _ { 1 } ^ { 2 } + 2 y _ { 1 } y _ { 2 } - y _ { 2 } ^ { 2 } .
$$

Show, either by a stability analysis similar to Exercise 5 of Section 1.13 or by numerical computations, that for $\epsilon > 0$ (16.17) possesses a limit cycle of asymptotic radius $r = \sqrt { 6 } \in / 7$ (See also Wanner (1983), p.15 and I.13, Exercise 5).

3. Solve Hilbert's 16th Problem: what is the highest possible number of limit cycles that a quadratic system

$$
\begin{array} { r } { y _ { 1 } ^ { \prime } = \alpha _ { 0 } + \alpha _ { 1 } y _ { 1 } + \alpha _ { 2 } y _ { 2 } + \alpha _ { 3 } y _ { 1 } ^ { 2 } + \alpha _ { 4 } y _ { 1 } y _ { 2 } + \alpha _ { 5 } y _ { 2 } ^ { 2 } } \\ { y _ { 2 } ^ { \prime } = \beta _ { 0 } + \beta _ { 1 } y _ { 1 } + \beta _ { 2 } y _ { 2 } + \beta _ { 3 } y _ { 1 } ^ { 2 } + \beta _ { 4 } y _ { 1 } y _ { 2 } + \beta _ { 5 } y _ { 2 } ^ { 2 } } \end{array}
$$

can have? The mathematical community is waiting for you: nobody has been able to solve this problem for more than 80 years. At the moment, the highest known number is 4, as for ex ample in the system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = \mathsf { \lambda } \mathsf { { k } } y _ { 1 } - y _ { 2 } - 1 0 y _ { 1 } ^ { ~ 2 } + ( 5 + 8 ) y _ { 1 } y _ { 2 } + y _ { 2 } ^ { ~ 2 } } } \\ { { \qquad y _ { 2 } ^ { \prime } = y _ { 1 } + y _ { 1 } ^ { ~ 2 } + ( - 2 5 + 8 \epsilon - 9 \delta ) y _ { 1 } y _ { 2 } ~ , } } \\ { { \qquad \ S = - 1 0 ^ { - 1 3 } ~ , ~ \mathsf { \epsilon } = - 1 0 ^ { - 5 2 } ~ , ~ \mathsf { \lambda } \lambda = - 1 0 ^ { - 2 0 0 } } } \end{array}
$$

(see Shi Songling (1980), Wanner (1983), Perko (1984)).

4. Find a change of coordinates such that the equation

$$
m y ^ { \prime \prime } + { \left( - A \ + B \left( y \right) ^ { 2 } \right) } y ^ { \prime } + k y \ = 0
$$

becomes the Van der Pol equation (16.2) (see Kryloff-Bogoliuboff (1947), p.5).

5. Treat the pendulum equation

$$
y ^ { \prime \prime } + \sin y = y ^ { \prime \prime } + y - { \frac { y ^ { 3 } } { 6 } } + { \frac { y ^ { 5 } } { 1 2 0 } } \pm \cdots = 0 \ ,
$$

$$
y \left( 0 \right) = \epsilon , y ^ { \prime } ( 0 ) = 0 ,
$$

by the method of asymptotic expansions (16.6) and (16.7) and study the period as a function of ε.

R esult. The period is $2 \pi ( 1 + \epsilon ^ { 2 } / 1 6 + \cdot \cdot \cdot ) .$

6. Compute the limit cycle (Hopf bifurcation) for

$$
y ^ { \prime \prime } + y ~ = \epsilon ^ { 2 } y ^ { \prime } - \left( y ~ \right) ^ { 3 } ~ , ~ y ^ { \prime } ( 0 ) = 0 ~ ,
$$

for $\epsilon$ small by the method of Poincare (16.6), (16.7) with $z _ { 0 } ( t ) { = } 0$

7. Treat in a similar way as in Exercise 6 the Brusselator (6.11') with $A = 1$ and $B = 2 + \epsilon ^ { 2 }$

Hint. In order to simplify the computations, first make a shift of the critical point (1, 2) into the origin and then choose new coordinates using the eigenvectors of the linearized equation (see (12.22) and (12.23)). This leads to the equation

$$
y ^ { \prime \prime } + y ~ = - \epsilon ^ { 2 } ( y ^ { \prime } { - } 1 ) - { ( y ^ { \prime } ) } ^ { 2 } ( y + y ^ { \prime } ) + 2 y y ^ { \prime } ~ .
$$

Result. $z \left( t \right) = \in ( 2 / \sqrt { 3 } ) \mathrm { c o s } t + \cdot \cdot \cdot _ { \mathrm { ~ 2 ~ } } t = x \left( 1 - e ^ { 2 } / 1 8 + \cdot \cdot \cdot \right)$ ，so that the period is asymptotically $2 \pi ( 1 + \epsilon ^ { 2 } / 1 8 + \cdot \cdot \cdot )$

8. (Lienard (1928)). Prove that the limit cycle of the Van der Pol equation (16.1) for every $\epsilon > 0$ is unique.

Hint. The identity

$$
y ^ { \prime \prime } + \epsilon ( 1 { - } y ^ { 2 } ) y ^ { \prime } = \frac { d } { d x } ( y ^ { \prime } + \epsilon ( y - \frac { y ^ { 3 } } { 3 } ) )
$$

suggests， using the coordinate system $y _ { 1 } ( x ) = y ( x ) , y _ { 2 } ( x ) = y ^ { \prime }$ $+ \epsilon \left( y - y ^ { 3 } / 3 \right)$ . Write the resulting first order system, study the signs of $y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime }$ and the increase of the "energy" function $V \ ( x ) { = } ( y \ _ { 1 } ^ { 2 } + y \ _ { 2 } ^ { 2 } ) / 2$

Also generalize the result to equations of the form $y ^ { \prime \prime } { + } f \left( y \right) y ^ { \prime } { + } g \left( y \right) { = } 0$ For more details see e.g. Simmons (1972), p.349.

9. (Rayleigh (1883)). Compute the periodic solution of

$$
y ^ { \prime \prime } + \kappa y ^ { \prime } + \lambda { \left( y ^ { \prime } \right) } ^ { 3 } + n ^ { 2 } y = 0
$$

for $\kappa$ and 入 small.

Result. y=A sin(nx)+(λnA³/32)cos(3nx) where A is given by $\kappa + \left( 3 / 4 \right) \bar { \lambda } n ^ { 2 } A ^ { 2 } { = } \stackrel { . } { 0 }$

10.(Bendixson (1901)). If in a certain region $\Omega$ of the plane the expression

$$
{ \frac { \partial f _ { 1 } } { \partial y _ { 1 } } } + { \frac { \partial f _ { 2 } } { \partial y _ { 2 } } }
$$

is always negative or always positive, then the system (16.4) cannot have closed solutions in $\Omega$

Hint. Apply Green's formula

$$
\int \int \bigg ( \frac { \partial f _ { 1 } } { \partial y _ { 1 } } + \frac { \partial f _ { 2 } } { \partial y _ { 2 } } \bigg ) d y _ { 1 } d y _ { 2 } = \int \big ( f _ { 1 } d y _ { 2 } - f _ { 2 } d y _ { 1 } \big ) \ .
$$

Numerical methods for ordinary differential equations fall natur-ally into two classes: those which use one starting value at each step ("one-step methods") and those which are based on several values of the solution ("multistep methods" or "multi-value methods"). The present chapter is devoted to the study of one-step methods, while multistep methods are the subject of Chapter III. Both chapters can, to a large extent, be read at least in their beginning independently of each other.

We start with the theory of Runge-Kutta methods: the derivation of order conditions with the help of labelled trees, error estimates, convergence proofs, implementation， methods of higher order. Section II.7 introduces implicit Runge-Kutta methods. More attention will be devoted to these methods in Volume II on stiff differential equations. Some sections are then devoted to the elegant idea of extrapolation (Richardson， Romberg, etc..)） and its use for obtaining high order codes. We then turn our attention to an algebraic theory of the composition of methods. This will be the basis for the study of order properties for many general classes of methods in the following chapters. The chapter ends with special methods for second order differential equations $y \prime \prime = f \left( x , y \right)$ and delay differential equations.

We illustrate the methods of this chapter with an example from Astronomy， the restricted three body problem. One considers two bodies of masses $1 - \mu$ and $\mu$ in circular rotation in a plane and a third body of negligible mass moving around in the same plane. The equations are

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime \prime } = y _ { 1 } + 2 y _ { 2 } ^ { \prime } - \mu ^ { \prime } \frac { y _ { 1 } + \mu } { D _ { 1 } } - \mu \frac { y _ { 1 } - \mu ^ { \prime } } { D _ { 2 } } , } \\ & { } \\ & { y _ { 2 } ^ { \prime \prime } = y _ { 2 } - 2 y _ { 1 } ^ { \prime } - \mu ^ { \prime } \frac { y _ { 2 } } { D _ { 1 } } - \mu \frac { y _ { 2 } } { D _ { 2 } } , } \\ & { D _ { 1 } = \left( ( y _ { 1 } + \mu ) ^ { 2 } + y _ { 2 } ^ { 2 } \right) ^ { 3 / 2 } , ~ D _ { 2 } = ( ( y _ { 1 } - \mu ^ { \prime } ) ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } , } \\ & { ~ \mu = 0 . 0 1 2 2 7 7 4 7 1 ~ , ~ \mu ^ { \prime } = 1 - \mu ~ . } \end{array}
$$

We have carefuily determined the initial values so that the solution becomes periodic with period $X _ { e n d }$ Such periodic solutions have fascinated astronomers and mathematicians for many decades (Poincare) and are now often called "Arenstorf orbits" (see Arenstorf (1963) who also did many numerical computations "on high speed clectronic computers").The problem is $C ^ { \infty }$ with the exception of the two singular points $y _ { 1 } = - \mu$ and $y _ { 1 } = 1 - \mu , y _ { 2 } = 0$ therefore the Euler polygons of Section I.7 are known to converge to the solution. But are they really numerically useful here? We have chosen 24000 steps of step length $h = X _ { e n d } / 2 4 0 0 0$ and plotted the result in Figure 0.1. The result is not very striking.

The performance of the Runge-Kutta method (left tableau of Table 1.2) is already much better and converges faster to the solution. We have used 6000 steps of step size $X _ { e n d } / 6 0 0 0$ , so that the numerical work becomes equivalent. Clearly， most accuracy is lost in those parts of the orbit which are close to a singularity. Therefore, codes with automatic step size selection， described in Section II.4, perform much better and the code DOPRI5 (Table 4.6) computes the orbit with a precision of $1 0 ^ { - 3 }$ in 75 steps. The step size becomes very large in some regions and the graphical representation as polygons connecting the solution points becomes unsatisfactory. The solid line is the interpolatory solution (5.7), which is also precise for all intermediate values and useful for many other questions such as delay differential equations, dense output or implicit output.

![](images/cadaed81570ab0f178b02c133088c121406b09025abce8adbe76eeb48e9ca540.jpg)  
Figure 0.1. An Arenstorf orbit computed by equidistant Euler， equidistant Runge-Kutta and variable step size Dormand and Prince

For still higher precision one needs methods of higher order. For example, the code DOPRI8 (Table 6.4) computes the orbit faster than DOPRl5 for more stringent tolerances, say smaller than about $1 0 ^ { - 6 }$ The highest possible order isobtained by extrapolation methods (Section I.9)and thecodeODEX (with $K _ { \mathrm { m a x } } = 1 5$ obtains the orbit with a precision of $1 0 ^ { - 3 0 }$ with about 2500o function evaluations, precisely the same amount of work as the above Euler solution.

# II.1. The first Runge-Kutta methods

"Die numerische Berechnung irgend einer Losung einer gegebenen Differentialgleichung， deren analytische Losung man nicht kennt, hat, wie es scheint, die Aufmerksamkeit der Mathematiker bisher wenig in Anspruch genommen.."   
(C. Runge, 1895)

The Euler method for solving the initial value problem

$$
y ^ { \prime } = f \left( x , y \right) , \quad y \left( x _ { 0 } \right) = y _ { 0 }
$$

was described by Euler (1768) in his "Institutiones Calculi Integralis" (Sectio Secunda, Caput VI). The method is easy to understand and to implement. We have studied its convergence ex tensively in Section I.7 and have seen that the global error behaves like $C h$ ,where $C$ is a constant depending on the problem and $h$ is the maximal step size. If one wants a precision of, say, 6 decimals, one would thus need about a million steps, which is not very satisfactory. On the other hand, one knows since the time of Newton that much more accurate methods can be found, if $f$ in (1.1） is independent of $y$ , i.e. if we have a quadrature problem

$$
y ^ { \prime } = f \left( x \right) , \quad y \left( x _ { 0 } \right) = y _ { 0 }
$$

with solution

$$
y \left( X \right) = y _ { 0 } + \intop _ { x _ { 0 } } ^ { X } f \left( x \right) d x .
$$

As an example consider the midpoint rule (or first Gauss formula)

$$
\begin{array} { c } { { y ( x _ { 0 } { + } h _ { 0 } ) \approx y _ { 1 } { = } y _ { 0 } { + } h _ { 0 } f ( x _ { 0 } { + } \displaystyle \frac { h _ { 0 } } { 2 } ) } } \\ { { { } } } \\ { { y ( x _ { 1 } { + } h _ { 1 } ) \approx y _ { 2 } { = } y _ { 1 } { + } h _ { 1 } f ( x _ { 1 } { + } \displaystyle \frac { h _ { 1 } } { 2 } ) } } \\ { { { } } } \\ { { \cdots } } \\ { { y ( X ) \approx Y = y _ { n - 1 } { + } h _ { n - 1 } f ( x _ { n - 1 } { + } \displaystyle \frac { h _ { n - 1 } } { 2 } ) ~ , } } \end{array}
$$

where $h _ { i } = x _ { i + 1 } - x _ { i }$ avd $x _ { 0 } , x _ { 1 } , . . . , x _ { n - 1 } , x _ { n } = X$ a sbdivision of ${ \overset { \underset { \mathrm { \tiny ~ 1 } } { } } { y } } ( X ) - Y$ bounded by $C h ^ { 2 }$ Thus for a desired precision of 6 decimals, a thousand steps will usually do, i.e. the method here is a thousand times faster. Therefore Runge (1895) asked whether it would be possible to extend Method $( 1 . 3 ^ { \prime } )$ also to Problem (1.1). The first step

with $h = h _ { \mathrm { ~ 0 ~ } }$ would read

$$
y \left( x _ { 0 } { + } h \right) \approx y _ { 0 } + h f \left( x _ { 0 } + { \frac { h } { 2 } } , y \left( x _ { 0 } + { \frac { h } { 2 } } \right) \right) ,
$$

but which value should we take for $y \left( x _ { 0 } + h / 2 \right) \cdot$ In the absence of something better, it is natural to use one smali Euler step with step size h/2 and obtain from (1.3)

$$
\begin{array} { r c l } { { } } & { { } } & { { k _ { 1 } = f \left( x _ { 0 } , y _ { 0 } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { k _ { 2 } = f \left( x _ { 0 } + { \frac { h } { 2 } } , y _ { 0 } + { \frac { h } { 2 } } k _ { 1 } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { y _ { 1 } = y _ { 0 } + h k _ { 2 } . } } \end{array}
$$

One might of course be surprised that we propose an Euler step for the computation of $\boldsymbol { k } _ { 2 } ,$ just half a page after preaching its inefficiency. The crucial point is, however, that $k _ { 2 }$ is m ultiplied by $h$ in the third expression and therefore its error becomes less important. To be more precise, we compute the Taylor expansion of $y _ { 1 }$ in (1.4) as a function of $^ h$ ，

$$
{ \begin{array} { r l } & { y _ { 1 } = y _ { 0 } + h f \left( x _ { 0 } + { \frac { h } { 2 } } , y _ { 0 } + { \frac { h } { 2 } } f _ { 0 } \right) } \\ & { \qquad = y _ { 0 } + h f \left( x _ { 0 } , y _ { 0 } \right) + { \frac { h ^ { 2 } } { 2 } } ( f _ { x } + f _ { y } f ) ( x _ { 0 } , y _ { 0 } ) } \\ & { \qquad + \left. { \frac { h ^ { 3 } } { 8 } } \left( f _ { x x } + 2 f _ { x y } f + f _ { y y } f ^ { 2 } \right) ( x _ { 0 } , y _ { 0 } ) + \cdots \right. . } \end{array} }
$$

This can be compared with the Taylor series of the exact solution， which is obtained from (1.1) by repeated differentiation and replacing $y ^ { \prime }$ by $f$ every time it appears (Euler (1768), Problema 86, par. 656, see also (8.12) of Chapter I)

$$
\begin{array} { l } { { \displaystyle y \left( x _ { 0 } { + } h \right) = y _ { 0 } { + } h f \left( x _ { 0 } , y _ { 0 } \right) { + } \ \frac { h ^ { 2 } } { 2 } ( f _ { x } { + } f _ { y } f ) ( x _ { 0 } , y _ { 0 } ) } } \\ { { \displaystyle ~ + \ \frac { h ^ { 3 } } { 6 } \left( f _ { x x } { + } 2 f _ { x y } f { + } f _ { y y } f ^ { 2 } { + } f _ { y } f _ { x } { + } f _ { y } ^ { 2 } f \right) ( x _ { 0 } , y _ { 0 } ) { + } \ { . . . } . } } \end{array} \nonumber
$$

Subtracting these two equations, we obtain for the error of the first step

$$
\begin{array} { l } { { \tiny \begin{array} { l } { { ( x _ { 0 } { + } h ) - y _ { 1 } } } \\ { { ~ } } \\ { { ~ = ~ \frac { h ^ { 3 } } { 2 4 } \left( f _ { x x } + 2 f _ { x y } f + f _ { y y } f ^ { 2 } + 4 ( f _ { y } f _ { x } + f _ { y } ^ { 2 } f ) \right) ( x _ { 0 } , y _ { 0 } ) + ~ . ~ . } } \end{array} } } \end{array}
$$

When all second partial derivatives of $f$ are bounded, we thus obtain $\mid \mid y ( x _ { 0 } { + } h ) { - } y _ { 1 } \mid \mid \ \leq K h ^ { 3 }$

In order to obtain an approximation of the solution of (1.1) at the endpoint $X$ ， we apply Formula (1.4) successively to the intervals $( x _ { 0 } , x _ { 1 } )$ ， $( x _ { 1 } , x _ { 2 } ) , . . . , ( x _ { n - 1 } , X )$ ， very similarly to the application of Euler's method in Section I.7. Again similarly to the convergence proof of Section I.7, it will be shown in Section I1.3 that, as in the case (1.1'), the error of the numerical solution is bounded by $C h ^ { 2 }$ (h the maximal step size). Method (1.4) is thus an improvement on the Euler method. For high precision computing we need to find still better methods; this will be the main task of the next sections.

# General Formulation of Runge-Kutta methods

Runge (1895) and Heun (1900) constructed methods by including one or two additional Euler steps in (1.4). It was Kutta (1901) who then formulated the general scheme of what is now called a Runge-Kutta method:

Definition 1.1. Let s be an integer (the "number of stages") and $a _ { 2 1 }$ ， $a _ { 3 1 }$ ， $a _ { 3 2 } , \ldots , a _ { s 1 } , \ a _ { s 2 } , \ldots , a _ { s , s - 1 } , \ b _ { 1 } , \ldots , b _ { s } , \ c _ { 2 } , \ldots , c _ { s }$ be real coefficients. Then the method

$$
\begin{array} { r l } & { k _ { 1 } = f ( x _ { 0 } , y _ { 0 } ) } \\ & { k _ { 2 } = f ( x _ { 0 } + c _ { 2 } h , y _ { 0 } + h a _ { 2 1 } k _ { 1 } ) } \\ & { k _ { 3 } = f ( x _ { 0 } + c _ { 3 } h , y _ { 0 } + h ( a _ { 3 1 } k _ { 1 } + a _ { 3 2 } k _ { 2 } ) ) } \\ & { \quad \cdot \ \cdot \ } \\ & { k _ { s } = f ( x _ { 0 } + c _ { s } h , y _ { 0 } + h ( a _ { s 1 } k _ { 1 } + \cdot \cdot \cdot + a _ { s , s - 1 } k _ { s - 1 } ) ) } \\ & { y _ { 1 } = y _ { 0 } + h ( b _ { 1 } k _ { 1 } + \cdot \cdot \cdot + b _ { s } k _ { s } ) } \end{array}
$$

is called an s -stage explicit Runge-K utta method (ERK) for (1.1).

Usually, the $c _ { i }$ satisfy the conditions

$$
c _ { 2 } = a _ { 2 1 } , \quad c _ { 3 } = a _ { 3 1 } + a _ { 3 2 } , \quad . . . , \quad c _ { s } = a _ { s 1 } + \cdot \cdot \cdot + a _ { s , s - 1 }
$$

or briefly,

$$
c _ { i } ^ { \phantom { } } = \sum _ { j } a _ { i j } ^ { \phantom { } } \mathrm { ~ . ~ }
$$

These conditions were assumed by Kutta without any comment and express that all points where $f$ is evaluated are first order approximations to the solution. They greatly simplify the derivation of order

conditions for high order methods. For low orders, however, these assum ptions are not necessary (see Exercise 6).

Definition 1.2. A Runge-Kutta method (1.8) has order $p$ if for sufficiently smooth problems (1.1)

$$
\begin{array} { r } { \left| \left| ~ y \left( x _ { 0 } + h \right) - y _ { 1 } \right| \right| ~ \leq ~ K h ^ { p + 1 } \ , } \end{array}
$$

i.e.,if the Taylor series for theexact solution $y \left( x _ { 0 } \mathrm { + } h \right)$ and for $y _ { 1 }$ coincide up to (and including) the term $h ^ { p }$

With the paper of Butcher (1964b) it became customary to symbolize Method (1.8) by the tableau (1.8').

Examples. The above method of Runge as well as methods of Runge and Heun of order 3 are given in Table 1.1.

Table 1.1. Low order Runge-Kutta methods   

<table><tr><td>Runge, order 2</td><td></td><td colspan="5">Runge, order 3</td><td colspan="3">Heun, order 3</td></tr><tr><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td></td></tr><tr><td>0</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td>0</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td></td><td></td><td>0</td><td>2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>0</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4</td><td></td></tr></table>

# Discussion of methods of order 4

"Von den neueren Verfahren halte ich das folgende von Herrn Kutta angegebene fur das beste". (C. Runge, 1905)

Our task is now to determine the coeficients of 4-stage Runge-Kutta methods (1.8) in order that they be of order 4. We have seen above what we must do: compute the derivatives of $v _ { 1 } { = } y _ { 1 } ( h )$ for $\scriptstyle h = 0$ and compare them with those of the true solution for orders

1,2,3,and 4. In theory, with the known rules of differential calculus, this is a completely trivial task and,by the use of (1.9),results in the following conditions:

$$
\begin{array} { c } { { \sum _ { b _ { i } } = b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 } } \\ { { { } } } \\ { { \sum _ { b _ { i } c _ { i } } = b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac 1 2 } } \end{array}
$$

$$
{ \underset { i } { \mathop { \sum } } } b _ { i } { c _ { i } } ^ { 2 } = { b _ { 2 } } { c _ { 2 } ^ { 2 } } + { b _ { 3 } } { c _ { 3 } ^ { 2 } } + { b _ { 4 } } { c _ { 4 } ^ { 2 } } = { \frac { 1 } { 3 } }
$$

$$
{ \underset { i , j } { \mathop { \sum } b _ { i } a _ { i j } c _ { j } } } = b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } ( a _ { 4 2 } c _ { 2 } + a _ { 4 3 } c _ { 3 } ) = { \frac { 1 } { 6 } }
$$

$$
{ \underset { i } { \mathop { \sum } } } b _ { i } { \ { c } _ { i } } ^ { 3 } = b _ { 2 } { c } _ { 2 } ^ { 3 } + b _ { 3 } { c } _ { 3 } ^ { 3 } + b _ { 4 } { c } _ { 4 } ^ { 3 } = { \frac { 1 } { 4 } }
$$

$$
\begin{array} { l } { { \sum b _ { i } c _ { i } a _ { i j } c _ { j } = b _ { 3 } c _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } c _ { 4 } ( a _ { 4 2 } c _ { 2 } + a _ { 4 3 } c _ { 3 } ) = \frac { 1 } { 8 } } }  \\ { { \phantom { \sum b _ { i } c _ { i } a _ { i j } c _ { j } ^ { 2 } = b _ { 3 } a _ { 3 2 } c _ { 2 } ^ { 2 } + b _ { 4 } ( a _ { 4 2 } c _ { 2 } ^ { 2 } + a _ { 4 3 } c _ { 3 } ^ { 2 } ) = \frac { 1 } { 1 2 } } } } \\ { { \phantom { \sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } = b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } . } } } \end{array}
$$

These computations, which are not reproduced in Kutta's paper (they are, however, in Heun (19o0))， are very tedious. And they grow enormously with higher orders. We shall see in Section II.2 that by using an appropriate notation, they can become very elegant.

Kutta gave the general solution of (1.11) without comment. A clear derivation of the solutions is given in Runge-Konig (1924), p.291. We shal follow here the ideas of J.C. Butcher, which make clear the role of the so called simplifying assumptions， and will also apply to higher order cases.

# Lemma 1

$$
\begin{array} { r l } { \cdot ^ { 3 , } } & { { } I f } \\ { \sum _ { b _ { i } a _ { i j } } = b _ { j } \big ( 1 - c _ { j } \big ) } & { { } j = 1 , \ldots , 4 , } \\ { \phantom { \sum _ { i } ^ { j } } } & { { } } \end{array}
$$

then the equations d), g), and h) in (1.11) follow from the others.

Proof: We demonstrate this for g):

$$
\sum { b _ { i } a _ { i j } c _ { j } ^ { 2 } } = \sum { b _ { j } c _ { j } ^ { 2 } } - \sum { b _ { j } c _ { j } ^ { 3 } } = \frac { 1 } { 3 } - \frac { 1 } { 4 } = \frac { 1 } { 1 2 }
$$

by c) and e). The equations d) and h) are seen similarly. QED.

We shall now show that (1.12) is also necessary in our case:

Lemma 1.4. For $s = 4$ ,the equations (1.11) and (1.9) impty (1.12).

The proof of this lemma will be based on the following:

Lemma 1.5. Let $U$ and $V$ be $3 \times 3$ matrices such that

$$
U V = \left( \begin{array} { c c c } { { a } } & { { b } } & { { 0 } } \\ { { c } } & { { d } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) , \quad \operatorname* { d e t } \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) \ \ne \ 0 \ ,
$$

then either $V e _ { 3 } { ^ { = 0 } }$ or $U ^ { T _ { e } } { } _ { 3 } = 0 \ w h e r e \ e \ e \ _ { 3 } = ( 0 , 0 , 1 ) ^ { T } .$

Proof of Lemma 1.5. If $\operatorname* { d e t } U \neq 0$ ,then $U V e _ { 3 } { = } 0$ implies $V e _ { 3 } { = } 0$ If $\tt d e t { } U = 0$ ，there exists ${ \boldsymbol x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { T } \neq { \boldsymbol 0 }$ such that $U ^ { T } x = 0$ ，and therefore $V ^ { T } U ^ { T } x = 0$ . But (1.13) implies that $x$ must be a multiple of $e _ { 3 }$ QED.

Proof of Lemma 1.4. Define

$$
d _ { j } = \sum _ { i } b _ { i } a _ { i j } - b _ { j } ( 1 - c _ { j } ) \quad \mathrm { f o r ~ } \ j = 1 , \ldots , 4 \ ,
$$

so that we have to prove $d _ { j } = 0$ . We now introduce the matrices

$$
U = \left( \begin{array} { c c c } { { b _ { 2 } } } & { { b _ { 3 } } } & { { b _ { 4 } } } \\ { { b _ { 2 } c _ { 2 } b _ { 3 } c _ { 3 } b _ { 4 } c _ { 4 } } } \\ { { d _ { 2 } } } & { { d _ { 3 } } } & { { d _ { 4 } } } \end{array} \right) , V = \left( \begin{array} { c c c } { { c _ { 2 } } } & { { c _ { 2 } ^ { 2 } } } & { { \sum _ { j } a _ { 2 j } c _ { j } - c _ { 2 } ^ { 2 } / 2 } } \\ { { } } & { { } } & { { j } } \\ { { c _ { 3 } } } & { { c _ { 3 } ^ { 2 } } } & { { \sum _ { j } a _ { 3 j } c _ { j } - c _ { 3 } ^ { 2 } / 2 } } \\ { { } } & { { } } & { { j } } \\ { { c _ { 4 } } } & { { c _ { 4 } ^ { 2 } } } & { { \sum _ { j } a _ { 4 j } c _ { j } - c _ { 4 } ^ { 2 } / 2 } } \end{array} \right) ,
$$

Multiplication of these two matrices, using the conditions of (1.11), gives

$$
U V = { \left| \begin{array} { l l l } { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 3 } } } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { { \frac { 1 } { 3 } } } } & { { { \frac { 1 } { 4 } } } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right| } \quad \mathrm { w i t h } \quad \operatorname* { d e t } { \left| \begin{array} { l l } { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 3 } } } } \\ { { } } & { { } } \\ { { { \frac { 1 } { 3 } } } } & { { { \frac { 1 } { 4 } } } } \\ { { } } & { { } } \end{array} \right| } \quad \neq \ 0 .
$$

Now the last column of $V$ cannot be zero, since ${ { c } _ { 1 } } ^ { = } 0$ im plies

$$
\sum _ { j } a _ { 2 j } c _ { j } - c _ { 2 } ^ { 2 } / 2 = - c _ { 2 } ^ { 2 } / 2 \neq 0
$$

by Condition h). Thus $d _ { 2 } = d _ { 3 } = d _ { 4 } = 0$ follows from Lemma 1.5. The last identity $d _ { 1 } { = } 0$ follows from $d _ { 1 } + d _ { 2 } + d _ { 3 } + d _ { 4 } = 0$ ， which is a consequence of (1.11a,b) and (1.9). QED.

From Lemmas 1.3 and 1.4 we obtain

Theorem 1.6. Under the assumption (1.9) the equations (1.1l) are equivalent to

$$
\begin{array} { c } { { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 } } \\ { { { } } } \\ { { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \displaystyle \frac { 1 } { 2 } } } \\ { { { } } } \\ { { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } = \displaystyle \frac { 1 } { 3 } } } \\ { { { } } } \\ { { b _ { 2 } c _ { 2 } ^ { 3 } + b _ { 3 } c _ { 3 } ^ { 3 } + b _ { 4 } c _ { 4 } ^ { 3 } = \displaystyle \frac { 1 } { 4 } } } \end{array}
$$

$$
b _ { 3 } c _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } c _ { 4 } ( a _ { 4 2 } c _ { 2 } + a _ { 4 3 } c _ { 3 } ) = { \frac { 1 } { 8 } }
$$

$$
b _ { 3 } a _ { 3 2 } + b _ { 4 } a _ { 4 2 } = b _ { 2 } \big ( 1 - c _ { 2 } \big )
$$

$$
b _ { 4 } a _ { 4 3 } = b _ { 3 } ( 1 - c _ { 3 } )
$$

$$
0 = b _ { 4 } ( 1 - c _ { 4 } ) .
$$

NED.

It follows from (1.15j) and (1.11h) that

$$
b _ { 3 } b _ { 4 } c _ { 2 } ( 1 - c _ { 3 } ) \neq 0 .
$$

In particular this implies ${ c _ { 4 } } ^ { = 1 }$ by (1.15k).

Solution of Equations (1.15): Equations a)-e) and k) just state that $b _ { i }$ and $c _ { i }$ are the coeficients of a fourth order quadrature formula with ${ { c } _ { 1 } } ^ { = 0 }$ and ${ c _ { 4 } } ^ { = 1 }$ . Because of (1.16) there are four cases for this:

$$
1 ) \quad c _ { 2 } = u , c _ { 3 } = \nu \quad \mathrm { w i t h } \quad u \neq \nu , u \neq \frac { 1 } { 2 } , u \mathrm { a n d } \nu \neq 0 , \neq 1 ; ( u \neq 1 ) 
$$

then a)-e) form a regular linear system for $b _ { 1 } , b _ { 2 } , b _ { 3 } , b _ { 4 }$ . This sys-tem has the solution

$$
\begin{array} { r l } & { b _ { 2 } = \frac { 2 \nu - 1 } { 1 2 u ( 1 - u ) ( \nu - u ) } , \quad b _ { 3 } = \frac { 1 - 2 u } { 1 2 \nu ( 1 - \nu ) ( \nu - u ) } , } \\ & { b _ { 4 } = \frac { 6 u \nu + 3 - 4 u - 4 \nu } { 1 2 ( 1 - u ) ( 1 - \nu ) } , \quad b _ { 1 } = 1 - b _ { 2 } - b _ { 3 } - b _ { 4 } . } \end{array}
$$

The three other cases with double nodes are built upon the Simpson rule:

3) 2) $c _ { 3 } = 0 , c _ { 2 } = \frac { 1 } { 2 } , b _ { 3 } = u \neq 0 , b _ { 1 } = \frac { 1 } { 6 } - u , b _ { 2 } = \frac { 4 } { 6 } , b _ { 4 } = \frac { 1 } { 6 } ;$ $\begin{array} { l } { { c _ { 3 } = 0 , c _ { 2 } = \displaystyle \frac 1 2 , b _ { 3 } = u \neq 0 , b _ { 1 } = \displaystyle \frac 1 6 - u , b _ { 2 } = \displaystyle \frac 1 6 , b _ { 4 } = \displaystyle \frac 1 6 } } \\ { { c _ { 2 } = c _ { 3 } = \displaystyle \frac 1 2 , b _ { 1 } = \displaystyle \frac 1 6 , b _ { 3 } = u \neq 0 , b _ { 2 } = \displaystyle \frac 4 6 - u , b _ { 4 } = \displaystyle \frac 1 6 ; } } \\ { { } } \\ { { c _ { \textmd a 1 . c . } = \displaystyle \frac 1 6 , b _ { \textmd a } = u \neq 0 , b _ { \textmd a } = \displaystyle \frac 1 - u , b _ { \textmd a } = \displaystyle \frac 1 6 , b _ { \textmd a } = \displaystyle \frac 4 6 } } \end{array}$   
4) $c _ { 2 } = 1 , c _ { 3 } = \frac { 1 } { 2 } , b _ { 4 } = u \neq 0 , b _ { 2 } = \frac { 1 } { 6 } - u , b _ { 1 } = \frac { 1 } { 6 } , b _ { 3 } = \frac { 4 } { 6 } .$

Once $b _ { i }$ and $c _ { i }$ are chosen, we obtain $a _ { 4 3 }$ from j), and then f) and i) form a linear system of two equations for $a _ { 3 2 }$ and $a _ { 4 2 }$ . The deter-minant of this system is

$$
\begin{array} { r l } { \operatorname* { d e t } \left( \begin{array} { c c } { b _ { 3 } } & { b _ { 4 } } \\ { b _ { 3 } c _ { 3 } c _ { 2 } } & { b _ { 4 } c _ { 4 } c _ { 2 } } \end{array} \right) } & { { } = \ b _ { 3 } b _ { 4 } c _ { 2 } ( c _ { 4 } - c _ { 3 } ) } \end{array}
$$

which is $\neq 0$ by (1.16). Finally we obtain $a _ { 2 1 } , \ a _ { 3 1 }$ ，and $\alpha _ { 4 1 }$ from (1.9).

Two particular choices of Kutta (1901) have become particularly popular: Case 3) with $u = 2 / 6$ and Case 1） with $u = 1 / 3$ ， $\nu = 2 / 3$ . They are given in Table 1.2. Both methods generalize classical quadrature rules in keeping the same order. The first is more popular, the second is more precise ("Wir werden diese Naherung als im allgemeinen beste betrachten...", Kutta).

Table 1.2. Kutta's methods   
"Optimal" form ulas   

<table><tr><td colspan="6">The&quot; Runge-Kutta method</td><td colspan="4">3/8-Rule</td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td>0</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td>3</td><td>13</td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>1</td><td></td><td></td><td>2</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td></td><td>1</td><td>1</td><td>-1</td><td>1</td><td></td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>2</td><td>1</td><td></td><td>1</td><td>38</td><td>3</td><td>1</td></tr></table>

Much research has been undertaken, in order to choose the "best” possibilities from the variety of possible 4th order RKformulas.

The first attempt in this direction was the very popular method of Gill (1951), with the aim of reducing the need for computer storage ("registers") as much as possible. The first computers in the fifties used largely this method which is therefore of historical interest. Gill observed that most computer storage is needed for the computation of $k _ { 3 } ,$ where "registers are required to store in some form"

$$
\begin{array} { c } { { y _ { 0 } + a _ { 3 1 } h k _ { 1 } + a _ { 3 2 } h k _ { 2 } \ , \quad y _ { 0 } + a _ { 4 1 } h k _ { 1 } + a _ { 4 2 } h k _ { 2 } \ , \ } } \\ { { { } } } \\ { { y _ { 0 } + b _ { 1 } h k _ { 1 } + b _ { 2 } h k _ { 2 } \ , \quad h k _ { 3 } } } \end{array}
$$

"Clearly, three registers will suffice for the third stage if the quantitie: to be stored are linearly dependent, i.e. if"

$$
\begin{array} { r } { { \operatorname* { d e t } } \left( \begin{array} { l l l } { 1 } & { a _ { 3 1 } } & { a _ { 3 2 } } \\ { } & { } & { } \\ { 1 } & { a _ { 4 1 } } & { a _ { 4 2 } } \\ { } & { } & { } \\ { 1 } & { b _ { 1 } } & { b _ { 2 } } \end{array} \right) ~ = 0 ~ . } \end{array}
$$

Gill observed that this condition is satisfied for the methods of type 3)if $u = ( 1 + \sqrt { 0 . 5 } ) / 3$ . The resulting method can then be reformulated as follows ("As each quantity is calculated it is stored in the register formerly holding the corresponding quantity of the previous stage, which is no longer required"):

$$
\begin{array} { r l r } & { y : = i n i t i a l \nu a l u e , \ k : = h f ( y ) , \ y : = y + 0 . 5 k , \quad , q : = k } \\ & { k : = h f ( y ) , \quad y : = y + ( 1 - \sqrt { 0 . 5 } ) ( k - q ) \ , } \\ & { q : = ( 2 - \sqrt { 2 } ) k + ( - 2 + 3 \sqrt { 0 . 5 } ) q \ , } \\ & { k : = h f ( y ) , \quad y : = y + ( 1 + \sqrt { 0 . 5 } ) ( k - q ) \ , } \\ & { q : = ( 2 + \sqrt { 2 } ) k + ( - 2 - 3 \sqrt { 0 . 5 } ) q \ , } \\ & { k : = h f ( y ) \ , \quad y : = y + \frac { k } { 6 } - \frac { q } { 3 } \ , \quad (  \ c o m p u t e \ n e x t s t e p ) \ . } \end{array}
$$

Today, in large high-speed computers, this method is no longer used, but could still be of interest for very high dimensional equations.

Other attempts have been made to choose u and $\nu$ in (1.17), Case 1), such that the error terms (terms in $h ^ { 5 }$ ， see Section II.3) become as small as possible. We shall discuss this question in Section 11.3.

# Numerical Example

"Zu grosses Gewicht darf man naturlich solchen   
Beispielen nicht beilegen..."   
(W. Kutta, 1901)

Let us compare five different choices of methods on two test equations. We choose the solutions

$$
y _ { 1 } = \exp ( \sin ( x ^ { 2 } ) ) , y _ { 2 } = \exp ( 5 \sin ( x ^ { 2 } ) ) , y _ { 3 } = \sin ( x ^ { 2 } ) + 1 , y _ { 4 } = \cos ( x ^ { 2 } )
$$

which all satisfy the initial conditions $y _ { i } ( 0 ) { = } 1$ . There are several differential equations which can be built upon these solutions, such as

$$
\begin{array} { l } { { y _ { 1 } ^ { ~ \prime } = 2 x y _ { 4 } y _ { 1 } ~ , ~ y _ { 2 } ^ { ~ \prime } = 1 0 x y _ { 4 } y _ { 1 } ^ { ~ 5 } ~ , } } \\ { { { } } } \\ { { y _ { 3 } ^ { ~ \prime } = 2 x y _ { 4 } ~ , ~ y _ { 4 } ^ { ~ \prime } = - 2 x \left( y _ { 3 } - 1 \right) ~ , } } \end{array}
$$

or, more complicated,

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = 2 x y _ { 2 } ^ { 1 / 5 } y _ { 4 } , } & & { y _ { 2 } ^ { \prime } = 1 0 x \exp ( 5 ( y _ { 3 } - 1 ) ) { \cdot } y _ { 4 } , } \\ & { y _ { 3 } ^ { \prime } = 2 x y _ { 4 } , } & & { y _ { 4 } ^ { \prime } = - 2 x \log ( y _ { 1 } ) . } \end{array}
$$

We have applied five codes with several fixed step sizes. The maximal errors and the number of function calls (which is 4 times the number of steps here) are displayed in logarithmic scales in Figures 1.1. The scales are chosen such that the theoretical slope of the lines, which is 1/4 by Theorem 3.4, appears to be $4 5 ^ { \circ }$ .These tests usually show up a slight inferiority of the classical RK-scheme com-pared to the others, but the differences appear to be very tiny. The

![](images/206ec651af6365d2e3f6de7a991142b03c64097809ad3c87e55da05d02052a81.jpg)  
Figure 1.1. Maximal global errors versus number of function calls

methods com pared are:

classical RK (left tableau of Table 1.2) Kutta's 3/8 rule (right tableau of Table 1.2) optimal formula, Ex. 3a, II.3, $\scriptstyle u = 0 . 3 5 8 7$ ， $\nu = 0 . 6 3 4 6$ Ralston (1962), Hull (1967), $u = 0 . 4$ ， $\nu = 0 . 4 5$ \*_\* Gill's Formula (1.18)

# Exercises

1. Show that every s-stage explicit RK method of order $s$ ,when applied to the problem $y ^ { \prime } = \lambda y$ （ $\lambda$ a complex constant)， gives

$$
y _ { 1 } = \left\{ \begin{array} { c c } { { s } } & { { z ^ { j } } } \\ { { \sum } } & { { \frac { z ^ { j } } { j ! } } } \end{array} \right\} y _ { 0 } , \quad z = h \lambda
$$

Hint. Show first that $y _ { 1 } / y _ { 0 }$ must be a polynomial in $z$ of degree s and then determine its coefficients by com paring the derivatives of $y _ { 1 }$ ， with respect to $^ h$ , to those of the true solution.

2. (Runge (1895), p.175; see also the introduction to Adams methods in Chapter II.1.). The theoretical form of drops of fluids is determined by the differential equation of Laplace (1805)

$$
- z \ = \mathbf { a } ^ { 2 } \frac { ( K _ { 1 } + K _ { 2 } ) } { 2 }
$$

where $\propto$ is a constant, $( K _ { 1 } { + } K _ { 2 } ) / 2$ the mean curvature, and z the height (see Figure 1.2). If we insert $1 / K _ { \mathrm { ~ 1 } } { = } r / \sin \Phi$ and $\kappa _ { 2 } = d \phi / d s$ ， the curvature of the meridian curve, we obtain

![](images/85cf33a64b69b4bb75708cce3cb971e309be136562ee2773c824a56811748f74.jpg)  
Figure 1.2. Drops

$$
- 2 z = { \alpha } ^ { 2 } \left( \frac { \sin \Phi } { r } + \frac { d \Phi } { d s } \right) ,
$$

where we put $\alpha = 1$ . Add

$$
\frac { d r } { d s } = \cos \Phi \ , \quad \frac { d z } { d s } = - \sin \Phi \ ,
$$

to obtain a system of three differential equations for $\phi ( s ) , r ( s ) _ { : }$ $z \left( s \right) , s$ being the arc length. Compute and plot different solution curves by the method of Runge (1.4) with initial values $\Phi ( 0 ) { = } 0$ ， $r ( 0 ) { = } 0$ and $z \left( 0 \right) { = } z _ { 0 }$ $\dot { z } _ { 0 } < 0$ for lying drops; compute also hanging drops with appropriate sign changes in (1.22)). Use different step sizes and compare the results.

Hint. Be careful at the singularity in the beginning: from (1.22) and (1.22） we have for small $s$ that $r = s$ $\Phi { = } A s$ with $\scriptstyle A = z _ { 0 }$ hence (sin Φ)/r→ Z0

3. Find the conditions for a 2-stage explicit RK-method to be of order two and determine all such methods ("... wozu eine weitere Erorterung nicht mehr notig ist" (Kutta)).

4. Find all methods of order three with three stages (i.e., solve (1.11;a-d) with $b _ { \mathbf { \Phi } _ { 4 } } { = } 0 _ { \mathbf { \Phi } _ { \cdot } }$

R esult. ${ \mathfrak { c } } _ { 2 } { = } { \mathfrak { u } }$ ， ${ { c } _ { 3 } } \mathrm { { = } } { \nu }$ ， $a _ { 3 2 } = \nu \left( \nu - u \right) / \left( u \left( 2 - 3 u \right) \right) ,$ $b _ { 2 } { = } ( 2 { - } 3 \nu ) / \big ( 6 u \big ( u - \nu \big ) \big )$ ， $b _ { 3 } { = } ( 2 { - } 3 u ) / ( 6 \nu \left( \nu - u \right) )$ $\boldsymbol { b } _ { 1 } { = } 1 { - } \boldsymbol { b } _ { 2 } { - } \boldsymbol { b } _ { 3 }$ ， $a _ { 3 1 } = c _ { 3 } - a _ { 3 2 }$ ， $\boldsymbol { a } _ { 2 1 } = \boldsymbol { c } _ { 2 }$ (Kutta (1901), p.438).

5. Construct all methods of order 2 of the form

$$
\begin{array} { c c } { { 0 } } & { { } } \\ { { c _ { 2 } } } & { { } } \\ { { \frac { c _ { 3 } } { 3 } } } & { { \left\{ \begin{array} { c c c } { { c _ { 2 } } } & { { } } & { { } } \\ { { 0 } } & { { c _ { 3 } } } & { { } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right. } } \end{array}
$$

Such methods "have the property that the corresponding Runge-Kutta process requires relatively less storage in a computer" (Van der Houwen (1977), \$2.7.2). Apply them to $y ^ { \prime } { = } { \lambda } y$ and compare with Exercise 1.

6. Determine the conditions for order two of the RK methods with two stages which do not satisfy the conditions (1.9):

$$
\begin{array} { r c l } { { } } & { { } } & { { k _ { 1 } = f \left( x _ { 0 } + c _ { 1 } h , y _ { 0 } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { k _ { 2 } = f \left( x _ { 0 } + c _ { 2 } h , y _ { 0 } + a _ { 2 1 } h k _ { 1 } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { y _ { 1 } = y _ { 0 } + h \left( b _ { 1 } k _ { 1 } + b _ { 2 } k _ { 2 } \right) . } } \end{array}
$$

Discuss the use of this extra freedom for $c _ { 1 }$ and $c _ { 2 }$ (Olive1 (1975)).

# I1.2. Order conditions for RK methods

"... I have heard a conference of Merson (J. Butcher's first contact with RK methods)

In this section we shall derive the general structure of the order conditions (Merson (1957), Butcher (1963)). The proof has evolved very much in the meantime, mainly under the influence of Butcher's later work， many personal discussions with him， the proof of "Theorem $6 "$ in Hairer-Wanner (1974), and our teaching experience. We shall see in Section II.11 that exactly the same ideas of proof lead to a general theorem of composition of methods $\mathrm { ~ ( = ~ B ~ }$ -series)，which gives access to order conditions for a much larger class of methods.

A big advantage is obtained by transforming (1.1) to autonomous form by adding $x$ to the dependent variables as

$$
{ \binom { x } { y } } ^ { \prime } = \left( { 1 \atop f ( x , y ) } \right) .
$$

The main difficulty in the derivation of the order conditions is to understand the correspondence of the formulas to certain rooted labelled trees; this comes out most naturally if we use well-chosen indices and tensor notation (as in Gill(1951), Henrici (1962), p.118, Gear (1971), p.32). As is usual in tensor notation, we denote (in this section) the components of vectors by superscript indices which， in order to avoid confusion, we choose as capitals. Then (2.1) can be written as

$$
( y ^ { J } ) ^ { \prime } = f ^ { J } ( y ^ { 1 } , \dots , y ^ { n } ) ~ , ~ J ~ = 1 , \dots , n ~ .
$$

We next rewrite the method (1.8) for the autonomous differential equation (2.2). In order to get a better symmetry in all formulas of (1.8)， we replace $k _ { i }$ by the argument $g _ { i }$ such that $k _ { i } ~ = f \left( g _ { i } \right)$ Then (1.8) becomes

$$
\begin{array} { l l } { { g _ { i } ^ { J } = y _ { 0 } ^ { J } + \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } h f ^ { J } ( g _ { j } ^ { 1 } , \ldots , g _ { j } ^ { n } ) } } & { { i = 1 , \ldots , s } } \\ { { { } } } & { { { } } } \\ { { y _ { 1 } ^ { J } = y _ { 0 } ^ { J } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } h f ^ { J } ( g _ { j } ^ { 1 } , \ldots , g _ { j } ^ { n } ) ~ . } } \end{array}
$$

If the system (2.2) originates from (2.1), then, for $J ~ = ~ 1$

$$
{ g _ { i } } ^ { 1 } = { y } _ { 0 } ^ { 1 } \ + \ \sum _ { j = 1 } ^ { i - 1 } a _ { i j } h \ = x _ { 0 } + c _ { i } h
$$

by (1.9). We see that (1.9) becomes a natural condition. If it is satisfied, then for the derivation of order conditions only the autonomous equation (2.2) has to be considered.

As indicated in Section II.1 we have to compare the Taylor series of $y _ { 1 } ^ { J }$ with that of the exact solution. Therefore we compute the derivatives of $y _ { 1 } ^ { J } .$ and $g _ { i } ^ { J }$ with respect to $h$ for $h = 0$ . Due to the similarity of the two formulas, it is suficient to do this for ${ { g } _ { i } ^ { J } }$ $\mathrm { O n }$ the right hand side of (2.3) there appear expressions of the form $h \phi ( h )$ ， so we make use of Leibniz' formula

$$
\left( h \phi ( h ) \right) ^ { ( q ) } \mid _ { h = 0 } = q \cdot \left( \phi ( h ) \right) ^ { ( q - 1 ) } \mid _ { h = 0 } .
$$

The reader is now askcd to take a dcep breath, take five shcets of reversed computer paper, remem ber the basic rules of differential calculus, and begin the following computations:

$q \ = 0$ : from (2.3)

$$
( g _ { i } ^ { J } ) ^ { ( 0 ) } \vert _ { \ h = 0 } = y _ { 0 } ^ { J } .
$$

q = 1 : from (2.3) and (2.4)

$$
( g _ { i } ^ { J } ) ^ { ( 1 ) } \vert _ { \phantom { } h = 0 } = \sum _ { j } a _ { i j } f ^ { J } \vert _ { \phantom { } y = y _ { 0 } } .
$$

$q \ = 2$ : because of (2.4) we shall need the first derivative of $f ^ { J } ( g _ { j } )$

$$
{ ( f ^ { J } ( g _ { j } ^ { \phantom { J } } ) ) } ^ { ( 1 ) } = \sum _ { K } f _ { K } ^ { J } ( g _ { j } ^ { K } ) { \cdot ( g _ { j } ^ { K } ) } ^ { ( 1 ) } ~ ,
$$

where, as usual, $f _ { K } ^ { J }$ denotes $\partial { f } ^ { J } / \partial y ^ { K }$ Inserting Formula (2.5;1) (with $i , j , J$ replaced by $j , k , K$ ) into (2.6;1) we obtain with (2.4)

$$
( g _ { i } ^ { J } ) ^ { ( 2 ) } \vert _ { \phantom { h } h = 0 } = 2 \sum _ { j , k } a _ { i j } a _ { j k } \sum _ { K } f _ { K } ^ { J } f ^ { K } \vert _ { \phantom { h } y - y _ { 0 } } .
$$

$q \ = 3$ : we differentiate (2.6;1) to obtain

$$
( f ^ { J } ( g _ { j } ) ) ^ { ( 2 ) } = \sum _ { K , \ L } f _ { K L } ^ { J } ( g _ { j } ) \cdot ( g _ { j } ^ { K } ) ^ { ( 1 ) } ( g _ { j } ^ { L } ) ^ { ( 1 ) } + \sum _ { K } f _ { K } ^ { J } ( g _ { j } ) ( g _ { j } ^ { K } ) ^ { ( 2 ) } \ _ { ( 2 , 0 ) } .
$$

The derivatives $( g _ { j } ^ { K } ) ^ { ( 1 ) }$ and $( g _ { j _ { \sigma } } ^ { K } ) ^ { ( 2 ) }$ at $h = 0$ are already available in (2.5;1) and (2.5;2). So we have from (2.3) and (2.4)

$$
\begin{array} { c } { { ( g _ { i } ^ { J } ) ^ { ( 3 ) } { } _ { \mid \ } { } _ { h = 0 } = 3 \displaystyle \sum _ { j , k , l } a _ { i j } a _ { j k } a _ { j l } \sum _ { K , L } f _ { K L } ^ { J } f ^ { K } f ^ { L } { } _ { \mid \ } { } _ { y - y _ { 0 } } } } \\ { { + 3 \cdot 2 \displaystyle \sum _ { j , k , l } a _ { i j } a _ { j k } a _ { k l } \sum _ { K , L } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } { } _ { \mid \ } { } _ { y - y _ { 0 } } . } } \end{array}
$$

The same formula holds for $( y _ { 1 } ^ { J } ) ^ { ( 3 ) } \vert _ { h = 0 }$ with $a _ { i j }$ replaced by $b _ { j }$

# The derivatives of the true solution

The derivatives of the correct solution are obtained much more easily just by differentiating Equation (2.2): first

$$
( y ^ { J } ) ^ { ( 1 ) } = f ^ { J } ( y ) ~ .
$$

Differentiating (2.2) and inserting (2.2) again for the derivatives we get

$$
{ ( y ^ { J } ) } ^ { ( 2 ) } = \sum _ { K } f _ { K } ^ { J } ( y ) \cdot { ( y ^ { K } ) } ^ { ( 1 ) } = \sum _ { K } f _ { K } ^ { J } ( y ) f ^ { K } ( y ) ~ .
$$

Differentiating (2.7;2) again we obtain

$$
( y ^ { J } ) ^ { ( 3 ) } = \sum _ { K , L } f _ { K L } ^ { J } ( y ) f ^ { K } ( y ) f ^ { L } ( y ) + \sum _ { K , L } f _ { K } ^ { J } ( y ) f _ { L } ^ { K } ( y ) f ^ { L } ( y ) .
$$

# Conditions for order 3

For order 3, the derivatives (2.5;1-3), (with $a _ { i j }$ replaced by $b _ { j }$ must be equal to the derivatives (2.7;1-3)， and this for every differential equation. Thus, comparing the corresponding expressions, we obtain:

Theorem 2.1. The RK method (2.3) (and thus $\left(  { I } . 8 \right)$ ) is of order 3 iff

$$
\begin{array} { c } { { \sum _ { b _ { j } } = 1 , } } \\ { { { } } } \\ { { 2 \sum _ { j , k } b _ { j } a _ { j k } = 1 , } } \\ { { { } } } \\ { { 3 \sum _ { b , l } b _ { j } a _ { j k } a _ { j l } = 1 , } } \\ { { { } } } \\ { { 6 \sum _ { j , k , l } b _ { j } a _ { j k } a _ { k l } = 1 . } } \end{array}
$$

QED.

Inserting $\sum _ { k } \mathrm { ~ \bf ~ \it ~ a ~ } _ { j k } = \mathrm { ~ \boldsymbol ~ c ~ } _ { j }$ from (1.9)， we can simplify these expres-sions stillfurther and obtain Formulas a)-d) of (1.11).

# Trees and elementary differentials

The continuation of this_ process， although theoretically clear, soon leads to very complicated formulas. It is therefore advantageous to use a graphical representation: indeed, the indices $j , k , l$ and $J \mathcal { K } \mathcal { \Lambda } , L$ in the terms of (2.5;3) are linked together as pairs of indices in @jk $a _ { j l } , \ldots .$ in exactly the same way as upper and lower indices in the

expressions $f _ { K L } ^ { J } , f _ { K } ^ { J }$ ,namely

$$
\begin{array} { c c c } { { \dot { [ \begin{array} { c c c c c c } { { \dot { [ { L } } } ^ { ~ , ~ J } { K } ^ { ~ , ~ \mathrm { B a m m e t y } } } & { { } } & { { } } & { { } } & { { l } } \\ { { \dot { l } } } & { { k } } & { { } } & { { } } & { { } } & { { } } \\ { { \dot { [ 3 ] } } } & { { = } } \end{array} ] } } } & { { \mathrm { a n d } } } & { { \dot { [ \begin{array} { c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \dot { [ 3 2 ] } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \dot { [ { j } } } } & { { } } & { { } } & { { } } \end{array} ] } } } \end{array}
$$

for the first and second term respectively. We call these objects labelled trees， because they are connected graphs (trees) whose vertices are labeled with summation indices. They can also be represented as mappings, e.g.

$$
l \to ~ j , ~ k \to ~ j \qquad \mathrm { a n d } \qquad l \to ~ k ~ , ~ k \to ~ j
$$

for the above trees. This mapping indicates to which lower letter the corresponding vertices are attached.

Definition 2.2. Let A be an ordered chain of indices $A = \{ j < k < l < m < . . . \}$ and denote by ${ ^ A } { _ q }$ the subset consisting of the first $q$ indices. A (rooted) labelled tree Oof order $q$ （ $q \geq 1$ ） is a mapping (the son-father mapping)

$$
t \colon A _ { q } - \{ j \} \to \ A _ { q }
$$

such that $t \left( z \right) < z$ for all $z \in A _ { q } - \{ j \}$ . The set of all labeled trees of order $q$ is denoted by $\boldsymbol { L } \boldsymbol { T } _ { g }$ . We call $z$ the son of $t ( z )$ and $t ( z )$ thc father of $z$ .The vertex $j ,$ the forefather of the whole dynasty, is called the rool of t. The order $q$ of a labelled tree is equal to the number of its vertices and is usually denoted by $q \ = \ \mathbf { \rho } ( t )$

Definition 2.3. For a labelled tree $\iota \in L T _ { q }$ we call

$$
F ^ { J } ( t ) ( y ) = \sum _ { K , L , . . } f _ { K , . . } ^ { J } ( y ) f _ { . . } ^ { K } ( y ) f _ { . . } ^ { L } ( y ) \cdot \cdot \cdot \cdot
$$

the corresponding elementary differential. Here the summation is over $q - 1$ indices $K \_ L$ .,.. ( which correspond to $A _ { q } - \{ j \} )$ and the summand is a product of $q$ $f$ 's, where the upper index runs through all vertices of $t$ and the lower indices are the corresponding sons.

If the set $A _ { q }$ is written as

$$
A _ { q } = \{ j _ { 1 } < j _ { 2 } < \cdots < j _ { q } \} \ ,
$$

then we can write the definition of $F \left( t \right)$ as follows:

$$
F ^ { J _ { 1 } } ( t ) = \sum _ { J _ { 2 } , . . . J _ { q } } \prod _ { i = 1 } ^ { q } f _ { t ^ { - 1 } ( J _ { i } ) } ^ { J _ { i } } ,
$$

since the sons of an index are its inverse images under the map t.

Examples of elementary differentials are

$$
\begin{array} { r l } { \sum _ { f } f _ { K L } ^ { J } f ^ { K } f ^ { L } } & { { } \mathrm { ~ a n d ~ } \sum _ { f } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } } \\ { K , L } \end{array}
$$

for the labelled trees $t _ { 3 1 }$ and $t _ { 3 2 }$ above. Thesc expressions appear in Formulas (2.5;3) and (2.7;3).

The three labelled trees

![](images/8977853e1648e7a976d5427547d8041cd2465c8c21aeb2c907a7b3d92f74c398.jpg)

all look topologically alike, moreover their elementary differentials

$$
\sum _ { K , L , M } f _ { K M } ^ { J } f _ { L } ^ { M } f _ { L } ^ { K } f ^ { L } ~ , ~ \sum _ { K , L , M } f _ { K L } ^ { J } f _ { M } ^ { L } f _ { ~ } ^ { K } f _ { M } ^ { M } ~ , ~ \sum _ { K , L , M } f _ { L K } ^ { J } f _ { M } ^ { K } f _ { ~ } ^ { L } f _ { M } ^ { M } f _ { L } ^ { L } ~ ,
$$

are the same, because they just differ by an exchange of the summa-tion indices. Thus we define

Definition 2.4. Two labeled trees t and u are equivalent, if they have the same order, say $q$ ， and if there exists a permutation $\sigma : A _ { q }  A _ { q } ,$ such that $\sigma ( j ) = j$ and $t \propto \ d = \sigma u$ on $A _ { q } - \{ j \}$

This clearly defines an equivalence relation.

Definition 2.5. An equivalence class of $q - t h$ order labelled trees is called a (rooted) tree of order $q$ . The set of all trees of order $q$ is denoted by T.. The order of a tree is defincd as the order of a representative and is again denoted by $\boldsymbol \rho ( t )$ . Furthermore we denote by $\alpha ( t )$ (for t E T,) the number of elements in the equivalence class t; i.e. the number of possible different monotonic labellings of t .

Geometrically，, a tree is distinguished from a labelled tree by omitting the labels. Often it is advantageous to include $\mathcal { D }$ ,the em pty tree,as the only tree of order O. The only tree of order 1 is denoted by $\tau$ . Representatives of all trees of order $\le 5$ are shown in Table 2.1. The number of trees of orders $1 , 2 , \ldots , 1 0$ are given in Table 2.2.

# The Taylor expansion of the true solution

We can now state the general result for the $q$ -th derivative of the true solution:

Theorem 2.6. The exact solution of (2.2) satisfies

$$
( y ^ { J } ) ^ { ( q ) } \vert _ { \ x - x _ { 0 } } = \sum _ { t \in L T _ { q } } F ^ { J } ( t ) ( y _ { 0 } ) = \sum _ { t \in T _ { q } } \propto ( t ) F ^ { J } ( t ) ( y _ { 0 } ) \ .
$$

Table 2.1. Trees and elementary differentials up to order 5   

<table><tr><td rowspan=1 colspan=1>q</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>Y（）</td><td rowspan=1 colspan=1>α（1）</td><td rowspan=1 colspan=1>F(1)()）</td><td rowspan=1 colspan=1>中(1）</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>y&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>·</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>广</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>j</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2SksKK</td><td rowspan=1 colspan=1>£ajkk</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>31132</td><td rowspan=1 colspan=1>k&gt;k</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>∑skLsksLKL2sEsKL</td><td rowspan=1 colspan=1>£aajk，∑akalk，</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>41424344</td><td rowspan=1 colspan=1>m1 kmmkmj&gt;k&lt;</td><td rowspan=1 colspan=1>481224</td><td rowspan=1 colspan=1>1311</td><td rowspan=1 colspan=1>∑SLMSMKLMKL,MESkfLMsLMKL,MKfLfMLMJKLM</td><td rowspan=1 colspan=1>∑akajamk,,m∑akaklamk,,m∑axaklakmk,l,m∑ajkaklabmk，m</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5152£53F54$ 55£ 565715859</td><td rowspan=1 colspan=1>m k尺mmKP  &gt;kpm kPmm   kP  mpk</td><td rowspan=1 colspan=1>510153020204060120</td><td rowspan=1 colspan=1>164431311</td><td rowspan=1 colspan=1>∑fkLMpSksMPP∑fKmpfLsSMfPESkpfKKfL fM fpfMLfEskpfEsK∑SkMSLsKL PESRSEMpSsMPESSEpSMsPEfkfESMpfMpPESsEssMsP</td><td rowspan=1 colspan=1>∑ajkajamaip∑ajkakla maip∑ajkaklakmapΣajkaklama P∑aikaklajmamp∑ajkaklakmakpΣajkaklamakp∑ajkaklabmaΣajkaklamamp</td></tr></table>

Table 2.2. Number of trees up to order 10   

<table><tr><td>q</td><td></td><td>1234567</td><td></td><td></td><td></td><td></td><td>8</td><td>9</td><td>10</td></tr><tr><td>card (Tq)</td><td></td><td>112492048</td><td></td><td></td><td></td><td></td><td>115</td><td>286</td><td>719</td></tr></table>

Proof: The theorem is true for $q = 1 , 2 , 3$ (see (2.7;1-3) above). For the computation of, say, the 4-th derivative, we have to differentiate (2.7;3). This consists of two terms (corresponding to the two trees of (2.9)),each of which contains three factors $f _ { . . } ^ { \ \cdot \cdot }$ (corresponding to the three nodes of these trees). The differentiation of these by Leibniz' rule and insertion of (2.2) for the derivatives is geometrically just the addition of a new branch with a new summation letter to each vertex (Figure 2.1).

![](images/9043e637b7a5625346ad597758ac3d1bcc86db122f5d3aa011216593bd5bb934.jpg)  
Figure 2.1. Derivatives of exact solution

It is clear that by this process all labelled trees of order $q$ appear for the $q$ -th derivative and each of them exactly once.

If we group together the terms with identical elementary differentials, we obtain the second expression of $( 2 . 7 ; { \mathfrak { q } } )$ . QED.

# Faa di Bruno's formula

Our next goal will be the computation of the $q$ -th derivative of the numerical solution $y _ { 1 }$ and of the ${ { \mathbf { } } ^ { g } } _ { j }$ . For this, we have first to generalize the formulas (2.6;1) (the chain rule) and (2.6;2) for the $q$ -th derivative of the composition of two functions. We represent these two formulas graphically in Figure 2.2.

Formula (2.6;2) consists of two terms, the first term contains three factors, the second contains only two. Here the node $" l "$ is a "dummy" node, not really present in the formula, and just indicates that we have to take the second derivative. The derivation of (2.6;2) will thus lead to five terms which we write down for the convenience of the reader (but not for the convenience of the printer...)

![](images/61813c1ab037ce1664687854d8023a10065e88e0f8bad9edd2b3e9675d3f82ba.jpg)  
Figure 2.2. Derivatives of f' (g)

$$
\begin{array} { l } { { ( f ^ { J } ( g ) ) ^ { ( 3 ) } = \displaystyle \sum _ { K , L , M } f _ { K L M } ^ { J } ( g ) \cdot ( g ^ { K } ) ^ { ( 1 ) } ( g ^ { L } ) ^ { ( 1 ) } ( g ^ { M } ) ^ { ( 1 ) } } } \\ { { \ ~ + \displaystyle \sum _ { K , L } f _ { K L } ^ { J } ( g ) \cdot ( g ^ { K } ) ^ { ( 2 ) } ( g ^ { L } ) ^ { ( 1 ) } + \displaystyle \sum _ { K , L } f _ { K L } ^ { J } ( g ) \cdot ( g ^ { K } ) ^ { ( 1 ) } ( g ^ { L } ) ^ { ( 2 ) } } } \\ { { \ ~ + \displaystyle \sum _ { K , M } f _ { K M } ^ { J } ( g ) \cdot ( g ^ { K } ) ^ { ( 2 ) } ( g ^ { M } ) ^ { ( 1 ) } + \displaystyle \sum _ { K } f _ { K } ^ { J } ( g ) \cdot ( g ^ { K } ) ^ { ( 3 ) } ~ . ~ ( 1 ) } } \end{array}
$$

The corresponding trees are represented in the third line of Figure 2.2. Each time we differentiate, we have to

i) differentiate the first factor $f _ { K , \cdot } ^ { J } ;$ i.e. we add a new branch to the root $j$ ； ii) increase the derivative numbers of each of the $g \mathrm { ~ \bar { ~ s ~ } ~ }$ by 1; we represent this by lengtheniug the corresponding branch.

Each time we add a new label. All trees which are obtained in this way are those "special" trees which have no ramifications except at the root.

Definition 2.7. We denote by $L S _ { q }$ the set of special labelled trees of order $q$ which have no ramifications except at the root.

Lemma 2.8. (Faa di Bruno's formula). For q≥ 1 we have

Here. for utLSg， m is the number of branches leaving tne root ans S1\*. ..8m are the numbers of nodes in each of these branches. such that q=1+81+... +8m. NED.

Remark : The usual mulunomial cocffeients arc absent here. as wc use labelled trees .

The derivatives of the numerical solution

'Tt is diffxcult to keep a cool head when discussing the various derivatives...   
(S. Gill, 1956)

In order to generalize (2.5:1-3). we need the following definitions:

Definition 2.9. Let t be a labelled tree With root /: we denote by

$$
\Phi _ { j } ( \varepsilon ) = \sum _ { k , l , . . } a _ { j k } a _ { . . . } . .
$$

the sum over the $q - 1$ remaining indices k .!... (as in Definition 2.3). The summand is a product of $q - 1$ a's. where all fathers stand two by two with their sons as indices. If the set $\cdot ^ { 4 } { } _ { \checkmark }$ is Written as in (2 10). we have

$$
\Phi _ { j _ { 1 } } ( t ) = \sum _ { j _ { 2 } , . . , j _ { q } } a _ { t ( j _ { 2 } ) , j _ { 2 } } \cdot \cdot \cdot a _ { t ( j _ { q } ) , j _ { q } } .
$$

Definition 2.10. For $\textit { \texttt { i } } \in \mathcal { L } \textit { \texttt { l } } _ { q }$ let y(t) be the produet of p(r) and all orders of the trees which appear. if thc roots. one after 3nothcr. are removed from t. (See Figure 2.3 or Formula (2.17)).

The above expressions are of course independent of the labellings, so $\Phi _ { j } ( t )$ as well as $\gamma ( \textit { t } )$ also make sense in Exam ples are given in Table 2.1.

![](images/8a067d70c72e9aab4748eae1e14733fb0ef1c8c96e2002708ca753295946d389.jpg)  
${ \mathrm { F i g u r e ~ } } 2 . 3 .$ Example for the definition of $\gamma ( \boldsymbol { \mathbf { \rho } } _ { i } )$

Theorem 2.11. The derivatives of ${ \boldsymbol g } _ { i } ^ { J }$ satisfy

$$
( g _ { i } ^ { J } ) ^ { ( q ) } \vert _ { \ h \ = 0 } = \sum _ { t \in L T _ { q } } \gamma ( t ) \sum _ { j } a _ { i j } \Phi _ { j } ( t ) F ^ { J } ( t ) ( y _ { 0 } ) \ .
$$

The numerical solution $y _ { 1 } ^ { J }$ of (2.3) satisfies

$$
\begin{array} { l } { { ( y _ { 1 } ^ { J } ) ^ { ( q ) } \big | _ { \begin{array} { l } { { h = 0 } } \end{array} } } } \\ { { { \stackrel { } { } } _ { t \in L { \cal T } _ { q } } \gamma ( t ) \sum _ { j } b _ { j } \Phi _ { j } ( t ) { \cal F } ^ { J } ( t ) ( y _ { 0 } ) } } \\ { { { } } } \\ { { { } = \displaystyle \sum _ { t \in { \cal T } _ { q } } \alpha ( t ) \gamma ( t ) \sum _ { j } b _ { j } \Phi _ { j } ( t ) { \cal F } ^ { J } ( t ) ( y _ { 0 } ) \ . } } \end{array}
$$

Proof: Because of the similarity of $y _ { 1 }$ and $\boldsymbol { g } _ { i }$ (see (2.3)) we only have to provc the first equation. We do this by induction on ，in exactly the same way as we obtained (2.5;1-3): first we apply Leibniz's formula (2.4) to obtain

$$
( g _ { i } ^ { J } ) ^ { ( q ) } \vert _ { \ h = 0 } = q \ \sum _ { j } \ a _ { i j } ( f ^ { J } ( g _ { j } ) ) ^ { ( q - 1 ) } \vert _ { \ y = y _ { 0 } } .
$$

Ncxt we use Faa di Bruno’s formula (Lemma 2.8). Finally we insert for the derivatives $( g _ { j } ^ { K , \bullet } ) ^ { ( 8 _ { s } ) }$ K,(8,), ， which appear in (2.6;q-1) with $\delta _ { s } < q$ ， the induction hypothesis (2.5;1) - (2.5;q-1) and rearrange the sums. This gives

$$
\begin{array} { l } { { ( g _ { i } ^ { J } ) ^ { ( q ) } \vert _ { \tiny { \ h = 0 } } = q \sum _ { \tiny { \ u \in L S _ { q } } } \sum _ { t _ { 1 } \in L T _ { \mathfrak { F } _ { 1 } } } \because \sum _ { \tiny { \mathfrak { t } _ { m } \in L T _ { \mathfrak { F } _ { m } } } } \gamma ( t _ { 1 } ) \cdot \cdot \cdot \gamma ( t _ { m } ) \cdot } } \\ { { \sum _ { \tiny { \ j } } a _ { i j } \sum _ { { \mathfrak { k } _ { 1 } } } a _ { j k _ { 1 } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \sum _ { \mathfrak { k } _ { m } } a _ { j k _ { m } } \Phi _ { k _ { m } } ( t _ { m } ) \cdot } } \\ { { \sum _ { \tiny { \mathfrak { t } _ { 1 } } , \ldots , { \mathfrak { t } _ { m } } } f _ { K _ { 1 } , \ldots , { \mathfrak { K } _ { m } } } ^ { J } ( y _ { 0 } ) F ^ { K _ { 1 } } ( t _ { 1 } ) ( y _ { 0 } ) \cdot \cdot \cdot F ^ { K _ { m } } ( t _ { m } ) ( y _ { 0 } ) \ . } } \end{array}
$$

The main difficulty is now to understand that to each tuple

$$
( u , t _ { 1 } , \ldots , t _ { m } ) \mathrm { w i t h } u \in L S _ { q } , t _ { s } \in L T _ { \mathfrak { F } _ { s } }
$$

there corresponds a labelled tree $t \in L T _ { q }$ such that

$$
\begin{array} { c } { { \gamma ( t ) = q \cdot \gamma ( t _ { 1 } ) \cdot \cdot \cdot \gamma ( t _ { m } ) } } \\ { { F ^ { J } ( t ) ( y ) = \displaystyle \sum _ { K _ { 1 } , \ldots , K _ { m } } f _ { K _ { 1 } , \ldots , K _ { m } } ^ { J } ( y ) F ^ { K _ { 1 } } ( t _ { 1 } ) ( y ) \cdot \cdot \cdot \cdot F ^ { K _ { m } } ( t _ { m } ) ( y ) } } \\ { { \Phi _ { j } ( t ) = \displaystyle \sum _ { k _ { 1 } , \ldots , k _ { m } } a _ { j k _ { 1 } } \cdot \cdot \cdot a _ { j k _ { m } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \Phi _ { k _ { m } } ( t _ { m } ) ~ . } } \end{array}
$$

This labelled tree $\ell$ is obtained if the branches of u are replaced by the trees $t _ { 1 } , \ldots , t _ { m }$ and the corresponding labels are taken over in a natural way, i.e. in the same order (see Figure 2.4 for some examples).

In this way, all trees $t \in L T _ { q }$ appear exactly once. Thus (2.16) becomes (2.5;q) after inserting (2.17),(2.18) and (2.19). QED.

The above construction of t can also be used for a recursive definition of trees. We first observe that the equivalence class of $t$ (in Figure 2.4) depends only on the equivalence classes of $t _ { 1 } , \ldots , t _ { m }$

![](images/4c661fe8e08f8a2862797dc01f26b18e663dd8c75b9069eb4c166303c9c9bf97.jpg)  
Figure 2.4. Example for the bijection $( u , t _ { 1 } , \ldots , t _ { m } ) \longleftrightarrow t$

Definition 2.12. We denote by

$$
t ~ = [ t _ { 1 } , \dots , t _ { m } ]
$$

the tree, which leaves over the trees $\tau _ { 1 } , \dots , \tau _ { m }$ when its root and the adjacent branches are chopped of (Figure 2.5).

![](images/364ef719ad384aff549c2274a86745c4e1ce2fe40efead9c08aa7f7772272390.jpg)  
Figure 2.5. Recursive definition of trees

With (2.20) alltrees_canbe expressed in terms of t; e.g. $\iota _ { 2 1 } = [ \tau ] , t _ { 3 1 } = [ \tau , \tau ] , t _ { 3 2 } = [ [ \tau ] ]$ ...et.

# The order conditions

Comparing Theorems 2.6 and 2.11 we now obtain:

Theorem 2.13. A Runge-K uta method (1.8) is of order p iff

$$
\sum _ { j } b _ { j } \Phi _ { j } ( t ) = \frac { 1 } { \gamma ( t ) }
$$

for all trees of order $\leq p$

Proof: While the "if" part is clear from the preceding discussion, the "only if" part needs the fact that the elementary differentials for different trees are actually independent. See Exercises 3 and 4 below. QED.

From Table 2.2 we then obtain the following number of order conditions (see Table 2.3). One can thus understand that the construction of higher order RK formulas is not an easy task.

Table 2.3. Number of order conditions   

<table><tr><td>order p</td><td>12345</td><td></td><td></td><td></td><td>7</td><td>8 9</td><td>10</td></tr><tr><td>no. of conditions</td><td></td><td></td><td>17</td><td>37</td><td>85</td><td>200 486</td><td>1205</td></tr></table>

Example. For the tree $t _ { 4 2 }$ of Table 2.1 we have (using (1.9) for the second expression)

$$
\sum _ { j , k , l , m } b _ { j } a _ { j k } a _ { j l } a _ { k m } = \sum _ { j , k } b _ { j } a _ { j k } c _ { j } c _ { k } = \frac { 1 } { 8 } ,
$$

which is (1.11;f). All remaining conditions of (1.11) correspond to the other trees of order $\leq 4$ 。

# Exercises

1. Find all trees of order 6 and order 7.

Hint. Search for all representations of $p - 1$ as a sum of positive integers, and then insert all known trees of lower order for each term in the sum. You may also use a computer for general $p$ ·

2. Denote the num ber of trees of order $q$ by $a _ { q }$ . Prove that

$$
a _ { 1 } + a _ { 2 } x + a _ { 3 } x ^ { 2 } + a _ { 4 } x ^ { 3 } + \cdot \cdot \cdot = { ( 1 - x ) } ^ { - a _ { 1 } } { ( 1 - x ^ { 2 } ) } ^ { - a _ { 2 } } { ( 1 - x ^ { 3 } ) } ^ { - a _ { 3 } } \cdot \cdot \cdot
$$

Compare the result with Table 2.2.

3. Compute the elementary differentials of Table 2.1 for the case of the scalar non-autonomous first-order equation (2.1), i.e. $f ^ { 1 } = \mathbb { 1 }$ ， $f ^ { 2 } { = } f \left( x , y \right)$ . One imagines the complications met by the first authors (Kutta, Nystrom, Huta) in looking for higher order conditions. Observe also that in this case the expressions for ${ } ^ { t } 5 4$ and $t _ { 5 7 }$ are the same, so that here Theorem 2.13 is sufficient, but not necessary for order 5.

Hint. For, say, ${ ^ t } _ { 5 4 }$ we have non-zero derivatives only if $K = L = 2$ Letting $M$ and $P$ run from 1 to 2 we then obtain

$$
{ F ^ { 2 } } ( t ) = { \left( { { f _ { x } } \ + \ f { f _ { y } } } \right) } { \left( { { f _ { y x } } \ + \ f { f _ { y y } } } \right) } { f _ { y } } .
$$

(See also Butcher (1963a)).

4. Show that for every $t \in T _ { o }$ there is a differential system such that $F ^ { 1 } ( t ) ( y _ { 0 } ) { = } 1$ and $F ^ { 1 } ( u ) ( y _ { 0 } ^ { \prime } ) { = } 0$ for all other trees $\boldsymbol { \mu }$

Hint. For $t _ { 5 4 }$ this system would be

$$
y _ { 1 } ^ { ~ \prime } = y _ { 2 } y _ { 5 } ~ , ~ y _ { 2 } ^ { ~ \prime } = y _ { 3 } ~ , ~ y _ { 3 } ^ { ~ \prime } = y _ { 4 } ~ , ~ y _ { 4 } ^ { ~ \prime } = 1 ~ , ~ y _ { 5 } ^ { ~ \prime } = 1
$$

with all initial values $= 0$ . Understand this and the general formula

$$
y _ { f a t h e r } ^ { \prime } = \prod y _ { s o n s } .
$$

5. Kutta (1901) claimed that the scheme given in Table 2.4 is of order 5. Was he correct in his statement? Try to correct these values.

Result. The values for $a _ { 6 j } ( j = 1 , \ldots , 5 )$ should read (6, 36, 10, 8, 0)/75; the correct values for b, are (23,0, 125,0, -81, 125)/192 (Nystr0m (1925)).

6. Verify

$$
\sum _ { \rho ( t ) = p } \alpha ( t ) = ( p - 1 ) !
$$

7. Prove that the local error $y \left( x _ { 0 } { + } h \right) - y _ { 1 }$ of a RK method, when applied to a linear system

$$
y ^ { \prime } = A \left( x \right) y + g \left( x \right) ,
$$

is $\mathbb { O } ( h ^ { p + 1 } )$ iff

$$
\begin{array} { c } { { \sum _ { j } b _ { j } c _ { j } ^ { q - 1 } = \frac 1 q \quad \mathrm { ~ f o r } \quad q \leq p } } \\ { { \sum _ { j , k } b _ { j } c _ { j } ^ { q - 1 } a _ { j k } c _ { k } ^ { r - 1 } = \displaystyle \frac 1 { ( q + r ) r } \quad \mathrm { ~ f o r } \quad q + r \leq p } } \\ { { \sum _ { j , k , l } b _ { j } c _ { j } ^ { q - 1 } a _ { j k } c _ { k } ^ { r - 1 } a _ { k l } c _ { l } ^ { s - 1 } = \displaystyle \frac 1 { ( q + r + s ) ( r + s ) s } \quad \mathrm { ~ f o r } \quad q + r + s \leq p } } \end{array}
$$

Hint. Write (2.22) in autonomous form and investigate which elementary differentials vanish identically. (See also Crouzeix (1975)).

# II.3. Error estimation and convergence for RK methods

'Es fehlt indessen noch der Beweis dass diese Naherungs-Verfahren convergent sind oder, was practisch wichtiger ist, es fehlt ein Kriterium, um zu ermitteln, wie klein die Schritte gemacht werden mussen, um eine vorgeschriebene Genauigkeit zu erreichen." (Runge, 1905)

Since the work of Lagrange (1797) and, above all, of Cauchy,a numerically established result should be accompanied by a reliable error estim ation (".. 'erreur commise sera inferieure a .."). Lagrange gave the well-known error bounds for the Taylor polynomials and Cauchy derived bounds for the error of the Euler polygons (see Section I.7). A couple of years after the first success of the Runge-Kutta methods, Runge (1905) also found a need for error estimates for these methods.

# Rigorous error bounds

Runge's device for obtaining bounds for the error in one step ("local error") can be described in a few lines (free translation):

"For a method of order $\boldsymbol { p }$ consider the local error

$$
e ( h ) = y ( x _ { 0 } { + } h ) - y _ { 1 }
$$

and use its Taylor expansion

$$
e \left( h \right) = e \left( 0 \right) + h e ^ { \prime } ( 0 ) + \cdot \cdot \cdot + \frac { h ^ { p } } { p ! } e ^ { \left( p \right) } ( \Theta h )
$$

with $0 < \theta < 1$ and $e ( 0 ) = e ^ { \mathbf { \varphi } } ( 0 ) = \cdots = e ^ { ( p ) } ( 0 ) = 0$ Now compute explicitly $e ^ { ( p ) } ( h )$ , which will be of the form

$$
e ^ { ( p ) } ( h ) = E _ { 1 } ( h ) + h E _ { 2 } ( h ) \ ,
$$

where $E _ { 1 } ( h )$ and $E _ { 2 } ( h )$ contain partial derivatives of $f$ up to order $p - 1$ and $p$ respectively. Further, because of $e ^ { ( p ) } ( 0 ) = 0$ ， we have $E _ { 1 } ( 0 ) = 0$ .Thus, if all partial derivatives of $f$ up to order $p$ are bounded, we have $E _ { 1 } ( h ) = \mathbf { O } ( h )$ and $E _ { 2 } ( h ) = \mathbf { 0 } ( 1 )$ . So there is a constant $C$ such that ${ \hat { | e } } ^ { ( p ) } ( h ) \mid \leq C h$ and

$$
\left| e \left( h \right) \right| \le C \frac { h ^ { p + 1 } } { p ! } , \prime \prime
$$

A slightly different approach is adopted by Bieberbach (1923, 1.Abschn., Kap.II, \$7), explained in more detail in Bieberbach (1951):

we write

$$
e \left( h \right) = y \left( x _ { 0 } + h \right) - y _ { 1 } = y \left( x _ { 0 } + h \right) - y _ { 0 } - h \sum _ { i = 1 } ^ { s } { b _ { i } k _ { i } }
$$

and use the Taylor expansions

$$
\begin{array} { c } { { \cdot h ) = y _ { 0 } + y ^ { \prime } ( x _ { 0 } ) h + y ^ { \prime \prime } ( x _ { 0 } ) { \frac { h ^ { 2 } } { 2 ! } } + \cdot \cdot \cdot + y ^ { ( p + 1 ) } ( \emptyset h ) { \frac { h ^ { p + 1 } } { ( p + 1 ) ! } } } } \\ { { k _ { i } ( h ) = k _ { i } ( 0 ) + k _ { i } ^ { \prime } ( 0 ) h + \cdot \cdot \cdot + k _ { i } ^ { ( p ) } ( \emptyset _ { i } h ) { \frac { h ^ { p } } { p ! } } \ , } } \end{array}
$$

where, for vector valued functions, the formula is valid componentwise with possibly different $\theta$ 's. The first terms in the h expansion of (3.5) vanish because of the order conditions. Thus we obtain

Theorem 3.1. If the Runge-Kutta method (1.8) is of order p and if all partial derivatives of $f \left( x \mathrm { ~ , ~ } y \mathrm { ~ } \right)$ up to order $p$ exist (and are continuous), then the local error of (1.8) admits the following rigorous bound

$$
\begin{array} { r l } { \| ~ y ( x _ { 0 } { + } h ) - y _ { 1 } \| } & { \le h ^ { p + 1 } \bigg ( \displaystyle \frac { 1 } { ( p + 1 ) ! } \operatorname* { m a x } _ { t \in [ 0 , 1 ] } \| y ^ { ( p + 1 ) } ( x _ { 0 } { + } t h ) \| } \\ & { + \displaystyle \frac { 1 } { p ! } \sum _ { i = 1 } ^ { s } | b _ { i } | \operatorname* { m a x } _ { t \in [ 0 , 1 ] } \| \big | \big | k _ { i } ^ { ( p ) } ( t h ) \| \bigg | \bigg ) } \end{array}
$$

and hence also

$$
\begin{array} { r } { \left\| ~ y \left( x _ { 0 } \mathrm { + } h \right) - y _ { 1 } \right\| \le C h ^ { p + 1 } \ . } \end{array}
$$

NED.

Let us demonstrate this result on Runge's first method (1.4), which is of order $p = 2$ ，applied to a scalar differential equation. Differentiating (1.1) we obtain

$$
y ^ { ( 3 ) } ( x ) = \biggl ( f _ { x x } + 2 f _ { x y } f + f _ { y y } f + f _ { y } ( f _ { x } + f _ { y } f ) \biggr ) ( x , y ( x ) )
$$

while the second derivative of $~ k ~ _ { 2 } ( h ) ~ = ~ f \left( x ~ _ { 0 } { + } { \frac { h } { 2 } } , y _ { 0 } { + } { \frac { h } { 2 } } f _ { 0 } \right)$ is given

$$
k _ { 2 } ^ { ( 2 ) } ( h ) = \frac 1 4 \left( f _ { x x } ( x _ { 0 } { + } \frac h 2 , y _ { 0 } { + } \frac h 2 f _ { 0 } ) + 2 f _ { x y } ( . . . ) f _ { 0 } + f _ { y y } ( . . . ) f _ { 0 } ^ { 2 } \right)
$$

$( f _ { \mathrm { ~ 0 ~ } }$ stands for $f ( x _ { 0 } , y _ { 0 } ) )$ . Under the assumptions of Theorem 3.1 we see that the expressions (3.9) and (3.10) are bounded by a constant independent of $h$ , which gives (3.8).

# The principal error term

For higher order methods rigorous error bounds, like (3.7), become very unpractical. It is therefore much more realistic to consider the first non-zero term in the Taylor expansion of the error. For autonomous systems of equations (2.2)， the error term is best obtained by subtracting the Taylor series and using (2.14) and (2.7;q).

Theorem 3.2. If the Runge-Kutta method is of order $p$ and if $f$ is $( p + 1 )$ -times continuously differentiable， we have

$$
\boldsymbol { y } ^ { J } ( \boldsymbol { x } _ { 0 } { + } h ) - \boldsymbol { y } _ { 1 } ^ { J } = \frac { h ^ { p + 1 } } { \left( p + 1 \right) ! } \sum _ { t \in T _ { p + 1 } } \boldsymbol { \alpha } ( t ) \boldsymbol { e } \left( t \right) \boldsymbol { F } ^ { J } ( t ) ( \boldsymbol { y } _ { 0 } ) + \boldsymbol { \mathrm { O } } ( h ^ { p + 2 } )
$$

where

$$
e ( t ) = 1 - \mathbb { Y } ( t ) \sum _ { j } b _ { j } \Phi _ { j } ( t ) \ .
$$

NED.

$\gamma ( t )$ and $\Phi _ { j } ( t )$ are given in Definitions 2.9 and 2.10; see also Formulas (2.17) and (2.19). The expressions $e \left( t \right)$ are called the error coeffi cients.

Example 3.3. For the two-parameter family of 4-th order RKmethods (1.17) the error coeficients for the 9 trees of Table 2.1 are$( c _ { 2 } ^ { \phantom { } } { ^ { = } } u \ , \ c _ { 3 } ^ { \phantom { } } { ^ { = } } \nu$ ）：

$$
\begin{array} { l l } { { e \left( t _ { 5 1 } \right) = - \displaystyle \frac { 1 } { 4 } + \frac { 5 } { 1 2 } ( u + \nu ) - \frac { 5 } { 6 } u \nu , } } & { { e \left( t _ { 5 2 } \right) = \frac { 5 } { 1 2 } \nu - \frac { 1 } { 4 } , } } \\ { { e \left( t _ { 5 3 } \right) = \frac { 5 } { 8 } u - \frac { 1 } { 4 } , } } & { { e \left( t _ { 5 4 } \right) = - \frac { 1 } { 4 } , } } \\ { { e \left( t _ { 5 5 } \right) = 1 - \displaystyle \frac { 5 \left( b _ { 4 } + b _ { 3 } \left( 3 - 4 \nu \right) ^ { 2 } \right) } { 1 4 4 b _ { 3 } b _ { 4 } \left( 1 - \nu \right) ^ { 2 } } , } } & { { } } \\ { { e \left( t _ { 5 6 } \right) = - 4 e \left( t _ { 5 1 } \right) , } } & { { e \left( t _ { 5 7 } \right) = - 4 e \left( t _ { 5 2 } \right) , } } \\ { { e \left( t _ { 5 8 } \right) = - 4 e \left( t _ { 5 3 } \right) , } } & { { e \left( t _ { 5 0 } \right) = - 4 e \left( t _ { 5 4 } \right) . } } \end{array}
$$

Proof: The last four formulas follow from (1.12). $e \left( t _ { 5 9 } \right)$ is trivial, $e \left( t _ { 5 8 } \right)$ and $e \left( t _ { 5 7 } \right)$ follow from (1.11.h). Further

$$
e \left( t _ { 5 1 } \right) = 5 \begin{array} { c } { { 1 } } \\ { { \int t \left( t - 1 \right) \left( t - u \right) \left( t - \nu \right) d t } } \\ { { 0 } } \end{array}
$$

expresses the quadrature error. For $e \left( t _ { 5 5 } \right)$ one best introduces $\begin{array} { r } { c _ { i } ^ { \prime } = \sum _ { j } a _ { i j } c _ { j } } \end{array}$ such that $\begin{array} { r } { e \left( \iota _ { 5 5 } \right) = 1 - 2 0 \sum _ { i } b _ { i } c _ { i } ^ { ^ { \prime } } c _ { i } ^ { ^ { \prime } } . } \end{array}$ Then from (1.11d,f)

one obtains

$$
c _ { 1 } ^ { \prime } = c _ { 2 } ^ { \prime } = 0 \ , b _ { 3 } c _ { 3 } ^ { \prime } = \frac { 1 } { 2 4 ( 1 - \nu ) } \ , b _ { 4 } c _ { 4 } ^ { \prime } = \frac { 3 - 4 \nu } { 2 4 ( 1 - \nu ) } \ .
$$

QED.

For the classical 4-th order method (Table 1.2a) these error coefficients are given by Kutta (1901), p.448 (scc also Lotkin (1951)) as follows

$$
\left( - { \frac { 1 } { 2 4 } } , - { \frac { 1 } { 2 4 } } , { \frac { 1 } { 1 6 } } , - { \frac { 1 } { 4 } } , - { \frac { 2 } { 3 } } , { \frac { 1 } { 6 } } , { \frac { 1 } { 6 } } , - { \frac { 1 } { 4 } } , 1 \right)
$$

Kutta remarked that for the second method (Table 1.2b) ("Als besser noch erweist sich ...") the error coefficients become

$$
\left( - { \frac { 1 } { 5 4 } } , { \frac { 1 } { 3 6 } } , - { \frac { 1 } { 2 4 } } , - { \frac { 1 } { 4 } } , - { \frac { 1 } { 9 } } , { \frac { 2 } { 2 7 } } , - { \frac { 1 } { 9 } } , { \frac { 1 } { 6 } } , 1 \right)
$$

which,with the exception of the 4-th and 9-th term,are all smaller than for the above method. A tedious calculation was undertaken by Ralston (1962) (and by many others) to determine optimal coefficients of (1.17). For solutions which minimize the constants (3.20), see Exercise 3 below.

# Estimation of the global error

"Das war auch eine aufregende Zet.." (P. Henrici, 1983)

The global error is the error of the computed solution after several steps. Suppose that we have a one-step method which, given an initial value $( x _ { 0 } , y _ { 0 } )$ and a step size $h$ , computes a numerical solution $y _ { 1 }$ approximating $y \left( x _ { 0 } \mathrm { + } h \right)$ . We shall denote this process by Henrici's notation

$$
y _ { 1 } = y _ { 0 } + h \Phi ( x _ { 0 } , y _ { 0 } , h ) 
$$

and call $\Phi$ the increment function of the method.

The numerical solution for a point $X > x _ { 0 }$ is then obtained by a step-by-step procedure

$$
y _ { i + 1 } = y _ { i } + h _ { i } \Phi ( x _ { i } , y _ { i } , h _ { i } ) ~ , ~ h _ { i } = x _ { i + 1 } - x _ { i } ~ , ~ x _ { N } = X
$$

and our task is to estimate the global error

$$
E \ = y ( X ) - y _ { N } .
$$

This estimate is found in a simple way, very similar to Cauchy's convergence proof for Theorem 7.3 of Chapter I: the local errors are transported to the final point $x _ { N }$ and then added up. This "error transport' can be done in two different ways:

a) either along the exact solution curves (see Figure 3.1); this method can yield sharp results when sharp estimates of error propagation for the exact solutions are known, e.g. from Theorem 10.6 of Chapter I based on the logarithmic norm $\mu ( \partial f / \partial y )$ ·

b) or along $N - i$ steps of the numerical method (see Figure 3.2); this is the method used in the proofs of Cauchy (1824) and Runge (1905), it generalizes easily to multistep methods (see Chapter III) and will be an important tool for the existence of asymptotic expansions (see I1.8).

![](images/3b79fdcff7cdd52d73a42683360624950ab8d6f60def9d06b3174b0ffc9a1fc7.jpg)  
Figure 3.1. Global error estimation, method a)

![](images/c7e9d86a15102f4e7ad43b02e4885cb0b54bd5fe12eb2454c0129fd29555aa2f.jpg)  
Figure 3.2. Global error estimation, method b)

In both cases we first estimate the local errors $\boldsymbol { e } _ { i }$ with the help of Theorem 3.1 to obtain

$$
\| e _ { i } \| \le C \cdot h _ { i - 1 } ^ { p + 1 } .
$$

Warning: The $e _ { i }$ of Figure 3.1 and Figure 3.2, for $i \neq 1$ , are not the same, but they allow similar estim ates.

We then estimate the transported errors $E _ { i }$ ：

a) For method a) we use the known results from Chapter I, especially Theorem I.10.6, Theorem I.10.2, or Formula (1.7.17). The result is

Theorem 3.4. Let $U$ be a neighbourhood of $\{ ( x ~ , y ( x ) ) | x _ { 0 } \leq x \leq X \}$ where y(x) is the exact solution of (2.2 Suppose that in U

$$
\begin{array} { r } { \mathrm { ~  ~ { ~ \psi ~ } ~ } \parallel \frac { \partial f } { \partial y } \parallel \leq L \quad o r \quad { \mit \mu } ( \frac { \partial f } { \partial y } ) \leq L , } \end{array}
$$

and that the local error estimates (3.24) are valid in $U$ . Then the global error (3.23) can be estimated by

$$
\left\| \begin{array} { l } { E } \end{array} \right\| \leq h ^ { p } \ \frac { C ^ { \prime } } { L } ( \exp ( L \ ( x _ { N } - x _ { 0 } ) ) - 1 )
$$

where h = max h;,

$$
C ^ { \prime } = \left\{ \begin{array} { l l } { { C } } & { { L \ge 0 } } \\ { { C \exp ( - L h ) } } & { { L < 0 , } } \end{array} \right.
$$

and h is small enough for the numerical solution to remain in $U$

Remark . For $L \to 0$ the estimate (3.26) tends to $h ^ { P } C ~ ( x _ { N } - x _ { 0 } )$

Proof: From Theorem I.10.2 (with $\epsilon = 0$ ） or Theorem I.10.6 (with $\mathfrak { F } = \mathrm { 0 }$ we obtain

$$
\left| ~ \left| ~ E _ { i } \right| \right| ~ \leq ~ \exp ( L ~ ( x _ { N } - x _ { i } ) ) \left| \right| ~ e _ { i } \right| \left| ~ .
$$

We then insert this together with (3.24) into

$$
\left\| \mathbf { \nabla } E \right\| \ \leq \ \sum _ { i = 1 } ^ { N } \ \left\| \mathbf { \nabla } E _ { i } \right\| \ .
$$

Using $h _ { i } ^ { p + 1 } \leq h ^ { p } \cdot h _ { i }$ this leads to

$$
\begin{array} { r } { \textup { \mid \mid E \mid \mid } \ \leq \ h ^ { p } C \left[ h _ { 1 } \mathrm { e x p } ( L \left( x _ { N } - x _ { 1 } \right) ) + h _ { 2 } \mathrm { e x p } ( L \left( x _ { N } - x _ { 2 } \right) ) + \cdots \right] \ . } \end{array}
$$

The expression in square brackets can be bounded by

$$
\begin{array} { l } { { \displaystyle \int _ { \scriptstyle x _ { 0 } } ^ { \scriptstyle x _ { N } } \exp ( L ( x _ { N } - x ) ) d x ~ f o r ~ L \ \geq \ 0 ~ } } \\ { { \displaystyle \int _ { \scriptstyle x _ { 0 } } ^ { \scriptstyle x _ { 0 } } \exp ( L ( x _ { N } - x ) ) d x ~ f o r ~ L \ < \ 0 ~ } } \\ { { \displaystyle \int _ { \scriptstyle x _ { 0 } } ^ { \scriptstyle x _ { N } } \exp ( L ( x _ { N } - h - x ) ) d x ~ f o r ~ L \ < \ 0 ~ } } \end{array}
$$

(see Figure 3.3). This gives (3.26). QED.

b) For the second method we need an estimate for $\{ \mid z _ { i + 1 } - y _ { i + 1 } \mid \mid$ in terms of $\{ | z _ { i } \ - \ y _ { i } \ \} .$ ， where, besides (3.22),

$$
z _ { i + 1 } = z _ { i } + h _ { i } \Phi ( x _ { i } , z _ { i } , h _ { i } )
$$

is a second pair of numerical solutions.

![](images/cbfbc2be4ea7cba03bbb6d324f497b17454c59b2259a2f894530a794a039e36e.jpg)  
Figure 3.3. Estimation of Riemann sums.

For RK-methods $z _ { i + 1 }$ is defined by

$$
\begin{array} { l } { { l _ { 1 } = f \left( x _ { i } , z _ { i } \right) ~ , } } \\ { { { } } } \\ { { l _ { 2 } = f \left( x _ { i } { + } c _ { 2 } h _ { i } , z _ { i } { + } h _ { i } a _ { 2 1 } l _ { 1 } \right) ~ , ~ e t c . } } \end{array}
$$

We now subtract Formuias (1.8) from this and obtain

$$
\begin{array} { r l } & { \left\| \textbf { \textit { k } } _ { 1 } - \boldsymbol { l } _ { 1 } \right\| \leq L \left\| \textbf { \textit { y } } _ { i } - \boldsymbol { z } _ { i } \right\| , } \\ & { \left\| \textbf { \textit { k } } _ { 2 } - \boldsymbol { l } _ { 2 } \right\| \leq L \left( 1 + \left| a _ { 2 1 } \right| h L \right) \left\| \textbf { \textit { y } } _ { i } - \boldsymbol { z } _ { i } \right\| , e t c . } \end{array}
$$

This leads to the following

Lemma 3.5. Let $\textit { L }$ be a Lipschitz constant for $f$ and let $\boldsymbol { h } _ { i } \ \le \ \boldsymbol { h }$ Then the increment function $\Phi$ of M ethod (1.8) satisfies

$$
\begin{array} { r } { \vert \vert \Phi ( x _ { i } , z _ { i } , h _ { i } ) - \Phi ( x _ { i } , y _ { i } , h _ { i } ) \vert \vert \ \le \ \Lambda \vert \vert z _ { i } - y _ { i } \vert \vert } \end{array}
$$

where

$$
\Lambda = L \ : ( \sum _ { i } \ : | b _ { i } | \ : + \ : h L \sum _ { i , j } \ : | b _ { i } a _ { i j } | \ : + \ : h ^ { 2 } L ^ { 2 } \sum _ { i , j , k } \ : | b _ { i } a _ { i j } a _ { j k } | \ : + \ : \cdot \cdot ) .
$$

NED.

From (3.30) we obtain

$$
\begin{array} { r } { \vert \vert \ z _ { i + 1 } - y _ { i + 1 } \vert \vert \ \le \ ( 1 + h _ { i } \Lambda ) \vert \vert \ z _ { i } - y _ { i } \vert \vert \ \le \ \exp ( h _ { i } \Lambda ) \vert \vert \ z _ { i } - y _ { i } \vert \vert } \end{array}
$$

and for the errors in Figure 3.2

$$
\mid \mid E _ { i } \mid \mid \ \leq \ \exp ( \Lambda ( x _ { N } - x _ { i } ) ) \mid \mid e _ { i } \mid \mid
$$

instead of (3.27).

The same proof as for Theorem 3.4 now gives us

Theorem 3.6. Suppose that the local error satisfies, for initial values on the exact solution,

$$
\left| \left| \begin{array} { l } { y \left( x + h \right) - y \left( x \right) - h \Phi \left( x , y \left( x \right) , h \right) } \end{array} \right| \right| \ \leq C h ^ { p + 1 } ,
$$

and suppose that in a neighbourhood of the solution the increment function $\Phi$ satisfies

$$
\begin{array} { r } { \left\| ~ \Phi ( x , z , h ) - \Phi ( x , y , h ) \right\| ~ \le ~ \Lambda \left\| ~ z ~ - ~ y ~ \right\| ~ . } \end{array}
$$

Then the global error (3.23) can be estimated by

$$
\parallel { \cal E } \parallel \le h ^ { p } \frac { C } { \Lambda } ( \exp ( \Lambda ( x _ { N } - x _ { 0 } ) ) - 1 )
$$

where h = max h,.

NED.

# Exercises

1. (Runge (1905)). Show that for explicit Runge Kutta methods with $b _ { \iota } ~ \geq ~ 0$ ,a ≥ 0 (all $i , j$ ) of order s the Lipschitz constant $\Lambda$ for $\Phi$ satisfies

$$
1 + h \Lambda < \exp ( h L )
$$

and that (3.36) is valid with $\Lambda$ replaced by L .

2. Show that $e \left( t _ { 5 5 } \right)$ of (3.20) becomes

$$
e ( \iota _ { 5 5 } ) = 1 - 5 \frac { ( 4 \nu ^ { 2 } - 1 5 \nu + 9 ) - u ( 6 \nu ^ { 2 } - 4 2 \nu + 2 7 ) - u ^ { 2 } ( 2 6 \nu - 1 8 ) } { 1 2 ( 1 - 2 u ) ( 6 u \nu - 4 ( u + \nu ) + 3 ) }
$$

after inserting (1.17.1).

3. Determine $\boldsymbol { \mu }$ and $\nu$ in (1.17) such that in (3.20)

$$
\begin{array} { r l r } { \mathrm { a ) } \ \underset { i = 5 , 6 , 7 , 8 } { \operatorname* { m a x } } | e ( t _ { 5 i } ) | = \operatorname* { m i n } } & { \ \mathrm { b } ) \underset { i = 1 } { \overset { \mathrm { 9 } } { \sum } } \ | e ( t _ { 5 i } ) | = \operatorname* { m i n } } & \\ { \mathrm { c } ) \ \underset { i = 5 , 6 , 7 , 8 } { \operatorname* { m a x } } ( t ) | e ( t _ { 5 i } ) | = \operatorname* { m i n } } & { \ \mathrm { d } ) \underset { i = 1 } { \overset { \mathrm { 9 } } { \sum } } \alpha ( t ) | e ( t _ { 5 i } ) | = \operatorname* { m i n } } & \end{array}
$$

Results:

4. Apply an explicit Runge-Kutta method to the problem $y ^ { \prime } { = } f \left( x , y \right) , y \left( 0 \right) { = } 0$ ,where

$$
f \left( x , y \right) = \left\{ \begin{array} { l l } { { \displaystyle \frac { \lambda } { x } y ~ + g \left( x \right) } } & { { ~ \mathrm { i f } ~ x > 0 } } \\ { { } } & { { } } \\ { { \displaystyle \left( 1 - \lambda \right) ^ { - 1 } g \left( 0 \right) } } & { { ~ \mathrm { i f } ~ x = 0 ~ , } } \end{array} \right.
$$

$\lambda \le 0$ and $g \left( x \right)$ are sufficientiy differentiable (see Exercise 10 of Section I.5).

a) Show that the error after the first step is given by

$$
y ( h ) - y _ { 1 } = C _ { 2 } h ^ { 2 } g ^ { \prime } ( 0 ) + \mathbf { O } ( h ^ { 3 } )
$$

where $c _ { 2 }$ is a constant depending on the coefficients of the method. Also for high order methods we have in general $C _ { 2 } \neq 0$ b) Com pute $c _ { 2 }$ for the classical 4-th order method (Table 1.2).

# I1.4. Practical error estimation and step size selection

"Ich glaube indessen, dass ein practischer Rechner sich meistens mit der geringeren Sicherheit begnugen wird, die er aus der Uebereinstimmung seiner Resultate for grossere und kleinere Schritte gewinnt."   
(C. Runge,1895)

Even the sim plified error estimates of Section I1.3, which are content with the leading error term，are of little practical interest, because they require the computation and majorization of several partial derivatives of high orders. But the main advantage of Runge-Kutta methods，compared with Taylor series, is precisely that the computations of derivatives should be no longer necessary. However, since practical error estimates are necessary (on the one hand to ensure that the step sizes $h _ { i }$ are chosen sufficiently small to have the required precision of the computed results,and on the other hand to ensure that the step sizes are sufficiently large to avoid unnecessary computational work)， we shall now discuss alternative methods for error estimates.

The oldest device, used by Runge in his numerical examples, is to repeat the computations with halved step sizes and to compare the results: those digits which haven't changed are assumed to be correct ("..woraus ich schliessen zu durfen glaube..").

# Richardson extrapolation

"..its usefulness for practical computations can hardly   
be overestimated."   
(G. Birkhoff- G.C. Rota)

The idea of Richardson, announced in his classical paper Richardson (1910) which treats mainly partial differential equations, and explained in full detail in Richardson (1927), is to use in a more careful way the known behaviour of the error as a function of $h$ ，

Suppose that, with a given initial value $( x _ { 0 } , y _ { 0 } )$ and step size $h$ ， we compute two steps, using a fixed Runge-Kutta method of order $p$ ， and obtain the numerical results $y _ { 1 }$ and $y _ { 2 }$ . We then compute, starting from $( x _ { 0 } , y _ { 0 } )$ , one big step with step size $_ { 2 h }$ to obtain the solution $w$ . The error of $y _ { 1 }$ is known to be (Thcorem 3.2)

$$
e _ { 1 } = y ( x _ { 0 } + h ) - y _ { 1 } = C \cdot h ^ { p + 1 } + \mathbf { O } ( h ^ { p + 2 } )
$$

where $C$ contains the error coefficients of the method and the elementary differentials $F ^ { J } ( t ) ( y _ { 0 } )$ of order $p + 1$ . The error of $y _ { 2 }$ is com-

posed of two parts: the transported error of the first step, which is

$$
\begin{array} { r } { ( I \ + h \frac { \partial f } { \partial y } + \mathbf { O } ( h ^ { 2 } ) ) e _ { 1 } \ , } \end{array}
$$

and the local error of the second step, which is the same as (4.1), but with the elementary differentials evaluated at $y _ { 1 } = y _ { 0 } + \mathbf { O } ( h ) .$ Thus we obtain

$$
{ \mathrm {  ~ \xi ~ } } _ { 2 } = y \left( x _ { 0 } + 2 h \right) - y _ { 2 } = \left( I + { \mit { \mathrm O } } ( h ) \right) C h ^ { p + 1 } + \left( C + { \mit { \mathrm O } } ( h ) \right) h ^ { p + 1 } + { \mit { \mathrm O } } ( h ) - z _ { 0 } = - { \mit { \mathrm O } } ( h ) ,
$$

hence

$$
e _ { 2 } = 2 C h ^ { p + 1 } + { \bf O } ( h ^ { p + 2 } ) .
$$

Similarly to (4.1), we have for the big step

$$
y \left( x _ { 0 } + 2 h \right) - w = C \left( 2 h \right) ^ { p + 1 } + \mathbf { O } \left( h ^ { p + 2 } \right) .
$$

Neglecting the terms $\mathbf { O } ( h ^ { p + 2 } )$ ,Formulas (4.2) and (4.3) allow us to eliminate the unknown constant $c$ and to "extrapolate" a better value $\vartheta _ { 2 }$ for $y \left( x _ { 0 } + 2 h \right)$ , for which we obtain:

Theorem 4.1. Suppose that $y _ { 2 }$ is the numerical result of two steps with step size h of a RK method of order $\boldsymbol { p }$ ,and $w$ is the result of one big step with step size $_ { 2 h }$ . Then the error of $y _ { 2 }$ can be extrapolated as

$$
\begin{array} { c c } { { y \left( x _ { 0 } { + } 2 h \right) - y _ { 2 } = \displaystyle \frac { y _ { 2 } { - } w } { 2 ^ { p } - 1 } + \mathbf { O } ( h ^ { p + 2 } ) } } & { { a n d } } \\ { { } } & { { } } \\ { { \hat { y } _ { 2 } = y _ { 2 } + \displaystyle \frac { y _ { 2 } { - } w } { 2 ^ { p } - 1 } } } \end{array}
$$

is an approximation of order $p + 1$ to $y \left( x _ { 0 } + 2 h \right)$ . QED.

Formula (4.4) is a very simple device to estimate the error and Formula (4.5) allows one to increase the precision by one additional order ("...The better theory of the following sections is complicated, and tends thereby to suggest that the practice may also be complicated; whereas it is really simple." (Richardson)).

# Automatic step size control

"D'ordinaire, on se contente de multiplier ou de divi  
ser par 2 la valeur du pas."   
(Ceschino, 1961)

We now want to write a code which automatically adjusts the step size in order to achieve a prescribed tolerance of the local error.

Whenever a starting step size h has been chosen, the program computes two steps of size h and one step of size 2h as described

above. Then the error is obtained from (4.4) as

$$
e r r = \frac { 1 } { 2 ^ { p } - 1 } \operatorname* { m a x } _ { i = 1 , \ldots , n } \frac { | y _ { 2 , i } - w _ { i } | } { d _ { i } } .
$$

Other norms, such as the Euclidean norm, are also of frequent use. In (4.6), $d _ { i }$ is a scaling factor: $d _ { i } ~ = ~ 1$ for absolute errors and $d _ { i } \ = \ | \hat { y } _ { 2 , i } |$ for relative errors. Often one also uses mixed scaling such as

$$
d _ { i } = \operatorname * { m a x } \ ( | \hat { y } _ { 2 , i } | , | y _ { 0 , i } | , 1 ) \ \mathrm { o r } \ \operatorname * { m a x } \ ( | \hat { y } _ { 2 , i } | , | y _ { 0 , i } | , 1 0 ^ { - 6 } )
$$

or the like. Then $e r r$ is compared to the desired tolerance tol which allows one to obtain an optimal step size from the error behaviour $C \cdot h ^ { p + 1 }$ as follows ("...le procede connu",Ceschino(1961))

$$
h \cdot \left( t o l / e r r \right) ^ { 1 / \left( p + 1 \right) } .
$$

Some care is now necessary for a good code: we multiply (4.7) by a safety factor $f a c$ ,usually $f a c = 0 . 8$ ,0.9, $( 0 . 2 5 ) ^ { 1 / ( p + 1 ) }$ ,or $( 0 . 3 8 ) ^ { 1 / ( p + 1 ) }$ ， so that the error will be acceptable the next time with high probability. Further, $h$ is not allowed to increase too fast nor to decrease too fast. For example, we may put

$$
h _ { n e w } \ = h \cdot \operatorname* { m i n } ( f a c m a x , \operatorname* { m a x } \ ( f a c m i n \ , f a c \cdot ( t o l / e r r ) ^ { 1 / ( p + 1 ) } ) )
$$

for the new step size. Then, if $e r r \ \leq \ t o l$ ， the two computed steps are accepted and the solution is advanced with either $y _ { 2 }$ or $\hat { y } _ { 2 }$ (this latter method is called "local extrapolation") and a new step is tried with $h _ { n e w }$ as step size. Else, both steps are rejected and the computations are repeated with the new step size $h _ { n e w }$ . The maximal step size increase facmax ，usually chosen between 1.5 and 5， prevents the code from too large step increases and contributes to its safety. It is clear that, when chosen too small, it may also unnecessarily increase the computational work. It is also advisable to put $f a c m a x \ = \ 1$ in the steps right after a step-rejection (Shampine-Watts, 1979).

# Embedded RK formulas

'It took me a long time to see this but the explanation is hard to put in writing".

(Merson, 1957)

"Scraton is right in his criticism of Merson's process, although Merson did not claim as much for his process as some people expect".   
(R. England, 1969)

The idea is, rather than using Richardson extrapolation, to construct RK formulas which themselves contain, besides the numerical approximation $y _ { 1 } ,$ an expression $\hat { y } _ { 1 }$ of higher order (or in some other fashion more precise than $y _ { 1 }$ ). This can then serve for error and step size control at every step and in particular makes step rejections less expensive.

So we have to find a scheme of coefficients (see (1.8)),

such that

$$
y _ { 1 } = y _ { 0 } + h \left( b _ { 1 } k _ { 1 } + \cdot \cdot \cdot + b _ { s } k _ { s } \right)
$$

is of order $p$ ,and

$$
\hat { y } _ { 1 } = y _ { 0 } + h ( \hat { b } _ { 1 } k _ { 1 } + \cdot \cdot \cdot + \hat { b } _ { s } k _ { s } )
$$

is of order $q$ (usually $\scriptstyle q = p - 1$ or $q = p + 1$

From Theorem 2.13, we have to satisfy the conditions

$$
\begin{array} { r l } { \underset { j } { \sum } b _ { j } \Phi _ { j } ( t ) = \frac { 1 } { \gamma ( t ) } } & { f o r \ a l l \ t r e e s \ o f o r d e r \leq p , } \\ { \underset { j } { \sum } \hat { b _ { j } } \Phi _ { j } ( t ) = \displaystyle \frac { 1 } { \gamma ( t ) } } & { f o r \ a l l \ t r e e s \ o f o r d e r \leq q . } \end{array}
$$

The first methods of this type were proposed by Merson (1957), Ceschino (1962), and Zonneveld (1963). They are given in Tables 4.1,4.2 and 4.3. Here,"name $p \left( q \right) "$ means that the order of $y _ { 1 }$ is $p$ and the order of the error estimator $\hat { y } _ { 1 }$ is $q$

Table 4.1. Ceschino 2(4)   

<table><tr><td>0 1</td><td></td></tr><tr><td>4</td><td>4</td></tr><tr><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td></tr><tr><td></td><td>1</td></tr><tr><td></td><td>2 0</td></tr><tr><td>1</td><td>4 6</td></tr></table>

Table 4.2. Merson 4("5")  

<table><tr><td>0 1-3 1-3 1-2</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>1 0</td><td>38</td></tr><tr><td>1</td><td></td><td>0</td><td>3 2 2</td></tr><tr><td></td><td></td><td>3</td><td>2</td></tr><tr><td></td><td>1</td><td>0 2 0</td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>2</td></tr></table>

Table 4.3. Zonneveld 4(3)   

<table><tr><td>0 1 2</td><td>1</td></tr><tr><td>1 0 2</td><td>1</td></tr><tr><td>1</td><td>2 0 0</td></tr><tr><td>44</td><td>1</td></tr><tr><td>5 7</td><td>13</td></tr><tr><td>32 32</td><td>1 32 32</td></tr><tr><td>1</td><td>1 1</td></tr><tr><td></td><td>1 3 3 6</td></tr><tr><td>1 7 2</td><td>13 16</td></tr></table>

These methods, however, do not yet completely satisfy our above requirements: Merson's $\hat { y } _ { 1 }$ is only of order 5 for linear equations with constant coefficients. This method thus overestimates the error for small $h$ , but works quite well and has been used very much, especially by NAG users ('The Team that gets results"). Similarly, Zonneveld's $\hat { y } _ { 1 }$ does not estimate the truncation error, but "the last term taken into account". Ceschino's method is uneconomic, because it estimates the error too precisely (see Exercises 1-3 below).

Formulas which satisfy Conditions (4.10) and $\left( 4 . 1 0 ^ { \circ } \right)$ were then derived by Sarafyan (1966)， England (1969)，and Fehlberg (1968, 1969). Let us demonstrate the derivation of a second order Fehlberg formula

$$
\begin{array} { r l } & { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { \frac { c _ { 3 } } { b _ { 1 } } } \end{array} \right| \begin{array} { c } { a _ { 2 1 } } \\ { a _ { 3 2 } } \end{array} \quad a _ { 3 2 } } \\ & { \left. \begin{array} { c c c c } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { \hat { b } _ { 1 } } & { \hat { b } _ { 2 } } & { \hat { b } _ { 3 } } \end{array} \right. } \end{array}
$$

The equations to be satisfied are by (4.10) and (4.10')

$$
\begin{array} { c c } { { b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 ~ } } & { { \hat { b } _ { 1 } + \hat { b } _ { 2 } + \hat { b } _ { 3 } = 1 } } \\ { { } } & { { } } \\ { { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \frac { 1 } { 2 } ~ } } & { { \hat { b } _ { 2 } c _ { 2 } + \hat { b } _ { 3 } c _ { 3 } = \frac { 1 } { 2 } } } \\ { { } } & { { } } \\ { { } } & { { \hat { b } _ { 2 } c _ { 2 } ^ { 2 } ~ + \hat { b } _ { 3 } c _ { 3 } ^ { 2 } = \frac { 1 } { 3 } } } \\ { { } } & { { } } \\ { { } } & { { \hat { b } _ { 3 } a _ { 3 2 } c _ { 2 } = \frac { 1 } { 6 } ~ . } } \end{array}
$$

Table 4.4. Embedded Runge-Kutta methods   

<table><tr><td></td><td>RKF 2(3)</td><td></td><td colspan="5">RKF 2(3)B</td></tr><tr><td>0</td><td></td><td></td><td>0 1</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>4</td><td>4</td><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td>27</td><td>189</td><td>729</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>40</td><td>800</td><td>800</td><td></td><td></td></tr><tr><td>1 2</td><td>1 4</td><td>1 4</td><td></td><td>214</td><td>1 33</td><td>650 891</td><td></td></tr><tr><td></td><td>1</td><td>1</td><td></td><td>891 214</td><td>1</td><td>650</td><td></td></tr><tr><td>y1</td><td>2</td><td>2</td><td>y1</td><td>891</td><td>33</td><td>891</td><td>0</td></tr><tr><td>91</td><td>1</td><td>1 6</td><td>4 6</td><td>91 533 2106</td><td>0</td><td>800 1053</td><td>1 78</td></tr></table>

We choose $c _ { 2 } = 1$ and $b _ { 3 } = 0$ to obtain $b _ { 2 } = b _ { 1 } = 1 / 2$ from the first two equations. There remain 4 equations for 5 unknowns. So we put $c _ { 3 } = 1 / 2$ so that $\hat { b } _ { 1 } ^ { \phantom { \dagger } } = { 1 } / { 6 } , \ \hat { b } _ { 2 } ^ { \phantom { \dagger } } = { \mathrm { \bar { 1 } } / { 6 } } , \ \hat { b } _ { 3 } ^ { \phantom { \dagger } } = { 4 } / { 6 }$ constitute Simpson's rule and finally obtain $a _ { 3 2 } = 1 / 4$ . The resulting method is given in Table 4.4. The second method of Table 4.4, also given by Fehiberg (1969), possesses one additional stage, but the coefficients are chosen such that $a _ { 4 i } = b _ { i }$ for all $i$ , therefore the last evaluation of $f$ in a current step can be re-used for the first evaluation in the following step. Since the error coefficients for $y _ { 1 }$ of RKF2(3)B are more than 100 times smaller, this method is claimed to be an improvement of RKF2(3) (this is not completely true, of course; see below).

Fehlberg derived many other formulas of different orders. One of the presently most used is the 4-th order method with 6 stages, given in Table 4.5.

Table 4.5. Fehlberg 4(5)   

<table><tr><td>1 4 3</td><td>4 3</td><td>9 32</td><td></td><td></td><td></td><td></td></tr><tr><td>8 12 13</td><td>32 1932 2197</td><td>7296 2197</td><td></td><td>845</td><td></td><td></td></tr><tr><td>1</td><td>439</td><td>18</td><td>3680 513</td><td>4104</td><td></td><td></td></tr><tr><td>1</td><td>216 8</td><td>2</td><td>3544</td><td>1859</td><td>11</td><td></td></tr><tr><td>2</td><td>27</td><td></td><td>2565</td><td>4104 2197</td><td>40 1</td><td>0</td></tr><tr><td>y1</td><td>25 216</td><td>0</td><td>1408 2565</td><td>4104</td><td>5</td><td></td></tr><tr><td>91</td><td>16 135</td><td>0</td><td>6656 12825</td><td>28561 56430</td><td>9 50</td><td>2 55</td></tr></table>

# The formula of Dormand and Prince

A natural question is: why should we not use the best possible result, i.e. the higher order expression $\hat { y } _ { 1 }$ , as numerical answer and as initial value for the following step? A natural answer to this question is: well, then our "error cstimation" $\hat { y } _ { 1 } - y _ { 1 }$ is no longer an error estimation, and we want to make error estimations, don't we? There are, however, two natural objections to this answer:

a) Due to generally unknown stability or instability properties of the differential system, the local errors generally have very litle in common with the global errors;

b) Fehlberg, in order to make his methods optimal, tried to minimize the error coeffcients for the lower order result $y _ { 1 }$ As a consequence, there is some danger that the difference $y _ { 1 } - \hat { y } _ { 1 }$ ，which consists mainly of the minimized error coefficients, underestimates the local error.

It is thus intercsting to derive methods for which the error terms of the higher order result are minimized and the lower order result is computed just for the step size control mechanism. Such a method, which also satisfies $a _ { s i } = b _ { i }$ , so that the last derivative evaluation can be re-used in the following step, has been constructed by Dormand and Prince (198O)， and gives excellent results. Its coefficients are given in Table 4.6.

Table 4.6. Dormand-Prince 5(4) (DOPRI5)   

<table><tr><td>0 1 5</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 10</td><td>3 40</td><td>9 40</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>44</td><td>_56</td><td></td><td>32</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>45</td><td></td><td>15</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>19372</td><td>25360</td><td></td><td>64448</td><td>212</td><td></td><td></td><td></td></tr><tr><td>9</td><td>6561</td><td>2187</td><td></td><td>6561</td><td>729</td><td></td><td></td><td></td></tr><tr><td>1</td><td>9017</td><td>355</td><td></td><td>46732</td><td>49</td><td>5103</td><td></td><td></td></tr><tr><td></td><td>3168</td><td>33</td><td></td><td>5247</td><td>176</td><td>18656</td><td></td><td></td></tr><tr><td>1</td><td>35</td><td>0</td><td></td><td>500</td><td>125</td><td>2187</td><td>11</td><td></td></tr><tr><td></td><td>384</td><td></td><td></td><td>1113</td><td>192</td><td>6784</td><td>84</td><td></td></tr><tr><td>y1</td><td>35</td><td></td><td>0</td><td>500</td><td>125</td><td>2187</td><td>11</td><td>0</td></tr><tr><td></td><td>384</td><td></td><td></td><td>1113</td><td>192</td><td>6784</td><td>84</td><td></td></tr><tr><td>y1</td><td>5179 57600</td><td></td><td>0</td><td>7571 16695</td><td>393 640</td><td>92097 339200</td><td>187 2100</td><td>1 40</td></tr></table>

![](images/b74df45bedbddf209871689befc6363a963db04080a2bf02af9b10ee253f4351.jpg)  
Figure 4.1. Step-control method RKF2(3) $t o l ~ = ~ 5 { \times } 1 0 ^ { - 4 }$ ，178 steps + 5 rejected

# Numerical study of the step-control mechanism

Figures 4.1 and 4.2 present the results of the above described step-control mechanism (4.7'). As example we choose the Brusselator (see Section I.16).

$$
\begin{array} { l } { { { y _ { 1 } } ^ { \prime } = 1 + y _ { 1 } ^ { 2 } y _ { 2 } - 4 y _ { 1 } } } \\ { { \ } } \\ { { { y _ { 2 } } ^ { \prime } = 3 y _ { 1 } - y _ { 1 } ^ { 2 } y _ { 2 } } } \end{array}
$$

with initial values $y _ { 1 } ( 0 ) = 1 . 0 1$ ， $y _ { 2 } ( 0 ) = 3$ very close to the critical point, and the integration interval $0 \leq x \leq 2 0$

The following results are plotted in the these pictures:

i) Below, the solutions $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ with all accepted integration steps;

![](images/04f1454bc3addab431475d0b0aedeb2a2366dc8b2a1b785794ac63968cdf346c.jpg)  
Figure 4.2. Step-control method RKF2(3)B $t o l ~ = ~ 3 { \times } 1 0 ^ { - 5 }$ ， 101 steps $^ +$ 12 rejected

ii) above this all step sizes used; the accepted as weli as the rejected ones;

iii) in the third graph from below the local estimated error $- \mathrm { l o g } _ { 1 0 } ( e r r )$ ; the desired tolerance is indicated by a broken horizontal line;

iv) and on top of the picture the global errors of the two numerical solutions. It can be seen that, due to the instabilities of the solu-tions with respect to the initial values, quite large global errors occur with small local tolerances everywhere.

We have compared the two Fehlberg formulas RKF2(3) and RKF2(3)B of Table 4.4. It can be observed that the second formula requires much smaller local tolerances in order to produce comparable actual global errors. This method, with its small error coefficients for $y _ { 1 } ,$ underestimates the actual errors.

It can be observed that the step size safety factor in (4.7'), which has been chosen as $f a c = 0 . 8$ here, usually kceps the local error nicely below the desired level.

# Numerical Comparison of 4th-order methods

We are now curious to see the behaviour of different 4-th order methods with step size control. We pick the following example from Fehlberg (1968):

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = 2 x y _ { 1 } \mathrm { l o g } ( \mathrm { m a x } ( y _ { 2 } , 1 0 ^ { - 3 } ) ) ~ , ~ y _ { 1 } ( 0 ) = 1 } } \\ { { } } \\ { { y _ { 2 } ^ { \prime } = - 2 x y _ { 2 } \mathrm { l o g } ( \mathrm { m a x } ( y _ { 1 } , 1 0 ^ { - 3 } ) ) ~ , ~ y _ { 2 } ( 0 ) = e ~ , } } \end{array}
$$

with correct solution $y _ { 1 } = \exp ( \sin ( x ^ { 2 } ) ) , y _ { 2 } = \exp ( \cos ( x ^ { 2 } ) )$ . The tolerances are chosen between $1 0 ^ { - 3 }$ and $1 0 ^ { - 7 }$ with ratio $\sqrt { 1 0 }$ and the integrations are performed on the interval $0 \leq x \leq 5$ . All results are then plotted in Figures 4.3: thus, the abscissae are $- \mathrm { l o g } _ { 1 0 } ( m a x i m a l$ global error) (the "precision")，and the ordinates are $\log _ { 1 0 } ( n u m b e r$ of function calls) (the "work"). The methods used are the same as in Figure 1.1 with the same line-style. To these we have added Fehlberg's method (Table 4.5), the method of Dorm and and Prince (Table 4.6), and the sixth order method of Butcher (Table 6.1). It appears that the method of Fehlberg RKF4(5) is better than the classical formulas without local extrapolation. However, the numerical results claimed in Fehlberg (1968) ("... save $40 \%$ to $60 \%$ computer time ...") can hardly be correct. We again see that the method underestimates the local error. Further, with the use of local extrapolation, the advantage of RKF4(5) melts away to a large extent.

The best method of all these is without doubt the coefficient set of Dormand and Prince.

# Ex ercises

1. Show that Runge's method (1.4) can be interpreted as two Euler steps (with step size h/2), followed by a Richardson extrapolation.   
2. Construct embedded formulas RK1(2) with two and three stages satisfying $\boldsymbol { a } _ { 2 i } = \boldsymbol { b } _ { i }$ . (Fehlberg: "Der Vollständigkeit halber sei noch erwahnt ."). Examples are given in Table 4.7. The second method is, of course, not uniquely determined.

![](images/53d68405f279d029de76f401c6b4dc137824a05a101c6939987978108be0f633.jpg)  
Figure 4.3. Precision-Work diagram

Table 4.7. Low order embedded methods   

<table><tr><td colspan="2">RKF 1(2)</td><td colspan="4">RKF 1(2)B</td></tr><tr><td>0</td><td></td><td>01 2</td><td>1</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td>255</td><td></td></tr><tr><td></td><td>0</td><td></td><td>256 1</td><td>256 255</td><td></td></tr><tr><td>y1</td><td>1</td><td>y1</td><td>256</td><td>256</td><td></td></tr><tr><td>91</td><td>1 1</td><td>91</td><td>1 512</td><td>255 256</td><td>1 512</td></tr></table>

I1.5. Further questions of practical computation

# Dense output

In the step control mechanism of Section I1.4 the computed points of the solution are chosen in accordance with the local error requirement. However, the solution is often required at prescribed output points which,in addition,can be dense. One possibility for obtaining the solution at such output points is to reduce the step size whenever necessary. Such a repeated reduction of the step size from a neariy optimal value disturbs the step size control and can result in a tremendous increase of computing time and rounding errors (Shampine, Watts and Davenport (1976)). It is therefore of interest to derive RK methods which are able to produce solution values at all intermediate points ${ \boldsymbol { x } } ^ { * } { = } { \boldsymbol { x } } _ { 0 } { + } { \boldsymbol { \theta } } h$ with $0 < \theta \leq 1$ (so-called continuous RK methods). Such continuous methods are of course particularly interesting if the $a _ { i j }$ are independent of 0; this allows the computation of hundreds of solution points in each integration step without much additional cost.

Example 5.1. The order conditions for a third order three-stage continuous RK method become (from Theorem 2.1 with $y \left( x _ { 0 } \mathrm { + } h \right)$ replaced by $y \left( x _ { 0 } + \theta h \right)$ ）

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } + b _ { 3 } = 0 } \\ { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \frac { \Theta ^ { 2 } } { 2 } } \\ { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \frac { \Theta ^ { 3 } } { 3 } } \\ { b _ { 3 } a _ { 3 2 } c _ { 2 } = \frac { \Theta ^ { 3 } } { 6 } \ . } \end{array}
$$

A simple calculation shows that this is impossible with c2, C3 and d32 independent of $\theta$ . We therefore reduce our requirement: since the continuous formula is used only once for each output value， we require that its precision correspond to the global error of a third order formula, which is ${ \bf O } ( h ^ { 3 } )$ . So we require second order for all θ and third order for $\theta = 1$ . Choosing $c _ { 2 } = 1 / 2 , c _ { 3 } { = } 1$ and solving the first three equations for 0 arbitrary and the last equation for $\theta = 1$ we obtain the scheme (Table 5.1) which extends a method of Kutta (1901).

Table 5.1. Continuous Runge-Kutta method   

<table><tr><td>0 1 2 1</td><td>1 -1 2 0</td></tr><tr><td></td><td>+0）） 3 0²(2 20) 0(1+0( 022 2 3 3 3</td></tr></table>

Example 5.2. There is, however, a simple and elegant device of third order interpolation， if we add the function evaluation ${ f _ { \mathit { \Pi } } } _ { 1 } { = } f \left( { x _ { \mathit { \Pi } } } _ { 0 } { + } h \mathrm { ~ } , y _ { \mathit { \Pi } } \right)$ which wil be necessary anyhow in the next step. We then have two function values $y _ { 0 } , y _ { 1 } ,$ and two derivatives ${ \boldsymbol { f } } _ { 0 } = { \boldsymbol { k } } _ { 1 } , { \boldsymbol { f } } _ { 1 } ,$ and can thus do a cubic polynomial interpolation: the scheme of divided differences becomes in this case

$$
\begin{array} { c c c c c c c } { { x _ { 0 } } } & { { \mid } } & { { y _ { 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { f _ { 0 } } } & { { } } & { { } } & { { } } \\ { { x _ { 0 } } } & { { \mid } } & { { y _ { 0 } } } & { { } } & { { ( d - f _ { 0 } ) / h } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { d } } & { { } } & { { ( f _ { 1 } - 2 d + f _ { 0 } ) / h ^ { 2 } } } \\ { { x _ { 1 } } } & { { \mid } } & { { y _ { 1 } } } & { { } } & { { } } & { { ( f _ { 1 } - d ) / h } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { f _ { 1 } } } & { { } } & { { } } \\ { { x _ { 1 } } } & { { \mid } } & { { y _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

where

$$
d ~ = ~ ( y ~ _ { 1 } - y ~ _ { 0 } ) / h ~ = ~ \sum _ { i } ~ b _ { i } k _ { i }
$$

and Newton's interpolation formula yields

$$
y \left( x _ { 0 } + \Theta h \right) = y _ { 0 } + h \Theta [ f _ { 0 } + \Theta ( d - f _ { 0 } ) + \Theta ( \Theta - 1 ) ( f _ { 1 } - 2 d + f _ { 0 } ) ]
$$

(see also Abramowitz-Stegun (1964), Formula 25.2.26).

Example 5.3. An elegant extension of the foregoing idea is possible if we do Richardson extrapolation over two steps as described in Theorem 4.1. For greater precision, we use the extrapolated value $y _ { 2 } { : = } \hat { y } _ { 2 }$ and make a derivative evaluation ${ f _ { 2 } } ^ { = } f \left( { x _ { 0 } } ^ { + } 2 h \mathrm { ~ , ~ } { y _ { 2 } } \right)$ (to be used in the next step). Further, since the constant $C$ in (4.1) is known from (4.3) and (4.4), we can also extrapolate a better value for $y _ { 1 }$

$$
y _ { 1 } : = y _ { 1 } + { \frac { y _ { 2 } - w } { ( 2 ^ { p } - 1 ) 2 } } \ .
$$

However, we do not have the derivative at the new $y _ { 1 }$ at our disposal without extra work. There are two possibilities for increasing precision:

A) Use a fourth degree interpolation polynomial based on the information $y _ { 0 , } { f } _ { 0 } , y _ { 1 } , y _ { 2 } , f _ { 2 } ;$   
B) Use for $f _ { \mathrm { ~ 1 ~ } }$ the derivative at $y _ { 1 }$ before extrapolation and compute fifth degree interpolation based on $y _ { 0 } , f _ { 0 } , y _ { 1 } , f _ { 1 } , y _ { 2 } , f _ { 2 }$ (numerical tests have shown that an additional functional evaluation at the new $y _ { 1 }$ is a useless waste of energy).

Newton's interpolation formula, similar to (5.3)， gives in these cases, if we write $d _ { \mathrm { \scriptsize ~ 1 } } = ( y _ { \mathrm { \scriptsize ~ 1 } } - y _ { \mathrm { \scriptsize ~ 0 } } ) / h$ ， $d _ { 2 } { = } ( y _ { 2 } { - } y _ { 1 } ) / h$ ，

$$
\begin{array} { r l } & { y \left( x _ { 0 } { + } \emptyset h \right) = y _ { 0 } + h \thinspace \Theta [ f _ { 0 } + \emptyset ( d _ { 1 } { - } f _ { 0 } + ( \theta { - } 1 ) ( ( d _ { 2 } { - } 3 d _ { 1 } { + } 2 f _ { 0 } ) / 4 } \\ & { \qquad + \thinspace ( \theta { - } 2 ) ( f _ { 2 } { - } 2 d _ { 2 } { + } 2 d _ { 1 } { - } f _ { 0 } ) / 4 ) ) ] } \end{array}
$$

for Case A), and

$$
\begin{array} { l } { { y \left( x _ { 0 } { + } \Theta h \right) = y _ { 0 } + h \theta [ f _ { 0 } + \Theta ( d _ { 1 } { - } f _ { 0 } + ( \theta { - } 1 ) ( f _ { 1 } { - } 2 d _ { 1 } { + } f _ { 0 } ) } } \\ { { \qquad + ~ ( \Theta { - } 1 ) ( ( d _ { 2 } { - } ^ { { 4 } f _ { 1 } { + } 5 d _ { 1 } { - } 2 f _ { 0 } } ) / 4 } } \\ { { \qquad + ~ ( \theta { - } 2 ) ( 2 f _ { 2 } { - } 6 d _ { 2 } { + } 8 f _ { 1 } { - } 6 d _ { 1 } { + } 2 f _ { 0 } ) / 8 ) ) ] } } \end{array}
$$

for Case B).

Numerical example. We compare the errors of the two forego-ing methods on Example (4.16) with initial values $y _ { 1 } ( 3 ) = \exp ( \sin ( 9 ) ) .$ $y _ { 2 } ( 3 ) { = } \mathrm { e x p } ( \cos ( 9 ) )$ . We compute 10 double steps with $h = 0 . 0 5$ using classical Runge-Kutta and interpolate at 10 intermediate values for each double step. The occurring errors are plotted in Figures 5.1. and 5.2. It can be seen that Formula (5.6) is clearly preferable. (5.5) is sufficient only for methods of order 3.

![](images/8db6688b2d6966c231e2f83afd79fc2d63732353dd5f28a37562d337257e924f.jpg)  
Figure 5.1. Interpolation error of Formula (5.5) over 10 double steps of the 4-th order RK method at Equation (4.16) (the big symbols are the computed RK points)

![](images/91f25b278b130cc2fdee4c344802154929bc6f2b178afeffbe57d0c8e64b0529.jpg)  
Figure 5.2. Interpolation error of Formula (5.6) combined with classical 4-th Drder RK on Example (4.16)

# Continuous embedded formulas

Continuous extensions of Runge-Kutta methods have been computed by Horn (1983) and Enright, Jackson, Nbrsett and Thomsen (1985). Horn has found that Fehlberg's Formula (Table 4.5) can be provided with a 4-th order global solution, if an additional function evaluation is added.

For the (preferable) method of Dormand and Prince (Table 4.6) a 4-th order continuous extension is possible even without an extra function evaluation. The solution, which for $\theta = 1$ becomes the fifthorder solution $\hat { y } _ { 1 }$ , is given by the following formulas:

$$
\begin{array} { l } { b _ { 1 } ( { \boldsymbol { \theta } } ) \ = \ \theta \big ( 1 + \theta \big ( - 1 3 3 7 / 4 8 0 + \theta \big ( 1 0 3 9 7 3 6 0 + \theta \big ( - 1 1 6 3 / 1 1 5 2 \big ) \big ) \big ) \big ) } \\ { b _ { 2 } ( { \boldsymbol { \theta } } ) \ = 0 } \\ { b _ { 3 } ( { \boldsymbol { \theta } } ) = 1 0 0 0 ^ { 2 } \big ( 1 0 5 4 / 9 2 7 5 + \theta \big ( - 4 6 8 2 / 2 7 8 2 5 + \theta \big ( 3 7 9 / 5 5 6 5 \big ) \big ) \big ) / 3 } \\ { b _ { 4 } ( { \boldsymbol { \theta } } ) = - 5 9 ^ { 2 } \big ( 2 7 / 4 0 + \theta \big ( - 9 / 5 + 9 6 \big ( 8 3 9 9 6 \big ) \big ) \big ) / 2 } \\ { b _ { 5 } ( { \boldsymbol { \theta } } ) \ = 1 8 2 2 5 6 ^ { 2 } \big ( - 3 / 2 5 0 + \theta \big ( 2 2 / 3 7 5 + \theta \big ( - 3 7 / 6 0 0 \big ) \big ) \big ) / 8 4 8 } \\ { b _ { 6 } ( { \boldsymbol { \theta } } ) \ = - 2 2 9 ^ { 2 } \big ( - 3 / 1 0 + \theta \big ( 2 9 / 3 0 + \theta \big ( - 1 7 / 2 4 \big ) \big ) \big ) / 7 } \\ { b _ { 6 } ( { \boldsymbol { \theta } } ) \ = - 9 2 9 ^ { 2 } \big ( - 3 / 1 0 + \theta \big ( 2 6 \big ) \big ) \ . } \\ { \qquad y \big ( x _ { 0 } + \Theta h \big ) \ \approx y _ { 0 } + \ h \underset { j = 1 } { \overset { \mathrm { G } } { \sum } } b _ { j } ( { \boldsymbol { \theta } } ) k _ { j } \ . } \end{array}
$$

These formulas together with the coefficients of Table 4.6 constitute an excellent tool for dense output， graphical representation of the solution, treatment of retarded equations (see Section I.15), implicit output, etc.

# Implicit Output

Often, the output value Xend for which the solutions are wanted are not known in advance, but depend implicitly on the computed solutions. Such situations occur very often; an example is the search for periodic solutions and limit cycles discussed in Section I.16, where we wanted to know when the solution reaches the Poincare-section for the first time.

Such problems are very easily treated by Newton's method; the derivatives of the solutions with respect to $x$ are known from thc differential equation. Let us suppose that we want to determine $x$ such that

$$
F \left( x , y \left( x \right) \right) = 0 .
$$

Algorithm 5.4. Compute the solution step-by-step until a sign change appears between $F \left( x _ { i } , y _ { i } \right)$ and $F \left( x _ { i + 1 } , y _ { i + 1 } \right)$ (this is, however, not completely safe since $F$ may change sign twice in an integration interval; use Formulas (5.3), (5.5),or (5.6) if more safety is needed). Then do Newton-iterations to search for the solution of (5.8):

$$
x _ { i } : = x _ { i } - { \frac { F ( x _ { i } , y _ { i } ) } { F ^ { \prime } ( x _ { i } , y _ { i } ) } }
$$

where

$$
' ( x , y ) = \frac { \partial F } { \partial x } ( x , y ) + \frac { \partial F } { \partial y ^ { 1 } } ( x , y ) \cdot f ^ { 1 } ( x , y ) + \cdot \cdot \cdot + \frac { \partial F } { \partial y ^ { n } } ( x , y ) \cdot f ^ { n } ( x , y ) .
$$

The new $y _ { 1 }$ is then obtained by a RK step with positive or negative $h$ .All the numerical examples of Section I.16 were computed with this method.

One can also compute the solution of (5.8) with the help of a continuous RK-method. In the case of the 5-th order Dormand-Prince method, this would be given by (5.7).

# Discontinuous equations

If you write some software which is half-way useful, sooner or later someone will use it on discontinuities. You have to scope about ...   
(A.R. Curtis, 1986)

Often, the functions defining the differential equations are not analytic or sufficiently differentiable everywhere, but the $f _ { i } ( x , y )$ or their derivatives have discontinuities along certain surfaces. If $f$ itself is discontinuous, the initial value problem may have no solution at all, as for example

$$
y ^ { \prime } = \left\{ \begin{array} { l l } { { - 1 } } & { { y \geq 0 } } \\ { { \quad 1 } } & { { y < 0 } } \end{array} \right. \qquad y \left( 0 \right) = 0 ~ ,
$$

Here, the solutions do not exist after having reached the $x$ -axis.

Usually， however, there exist solutions which satisfy the differential equations at all points of continuity of $f$ . Possible treat-ments for such problems are:

Method 1: Stop the computation at the surface of discontinuity (if necessary using Algorithm 5.4) and restart from there with the new $f$ 's.

Method 2: Ignore the discontinuity and apply an automatic stepcontrolling algorithm with local error control. Needless to say， this can waste computing time and does not give very reliable results.

Numerical Example: We have applied Method 2 with the algo-rithm DOPRI5 of Section I1.4 to the example $( y ~ ( 0 ) = 1$ ， $y \left( 5 \right) = ?$ ）

$$
y ~ ^ { \prime } = \left\{ \begin{array} { l } { { 1 / ( 1 + y ) } } \\ { { } } \\ { { a ~ ) ~ 1 } } \\ { { b ~ ) ~ 1 / 3 } } \\ { { } } \\ { { c ~ ) ~ ( 5 - y ) / 9 } } \end{array} \right\} ~ \mathrm { i f } ~ 2 < y ~ \leq ~ 2 
$$

We have chosen 81 tolerances between $1 0 ^ { - 3 }$ and $1 0 ^ { - 7 }$ .Figure 5.3 shows the errors of the 81 results in logarithmic scale compared to $\log _ { 1 0 } ($ (number of furction calls). The correct values are: a) 4.5,b) 17/6, c) 5-3exp(-5/18).

![](images/33b3a133015e2577cb7d579734a712ab740801fbd84e9f924fa39fdc777a5a7a.jpg)  
Figure 5.3. Numerical errors obtained for (5.10) by ignoring the discontinuity

It will be observed that the results are quite chaotic. In general one looses one or two digits of precision and the number of steps is very large. Another example of this kind will be studied in Sections I1.9 and I1.10.

# Starting step size

"If anything has been made foolproof, a better fool will   
be developed."   
(Heard from Dr. Pirkl, Baden)

For many years, the starting step size had to be supplied to a code. Users were considered to have a rough idea of a good step size from mathematical knowledge or previous experience. Anyhow,a bad starting choice for h was quickly repaired by the step size control. Nevertheless, when this happens too often and when the choices are too bad, much computing time can be wasted. Therefore, several peoplc (e.g. Watts (1983), Hindmarsh (1980)) developed ideas to let the computer do this choice. These ideas are usually guided by the hypothesis that， as for linear differential equations with constant coeficientsemetarydiferetialsfothtales" $t _ { 2 1 } , \ t _ { 3 2 }$ $t _ { 4 4 } , \ t _ { 5 9 }$ etc (see Table 2.1) behave like $\big \{ \big \} \ f \ \big \| \begin{array} { l } { q } \end{array}$ . Thus we may just compute $f \left( x , y \right)$ at the given initial point in order to get an idea of the order of magnitude of $\mid \mid f \mid \mid$ . The following formula is slightly more refined :

a) Do one function evaluation $f \left( x , y \right)$ at the initial point.

b) Let

$$
d e n ~ = ~ \biggl ( \frac { 1 } { \textsf { m a x } ( ~ | x _ { 0 } | , | x _ { e n d } | ) } \biggr ) ^ { p + 1 } + \parallel f _ { \mathbf { \theta } } | | \mathbf { \theta } ^ { p + 1 }
$$

where $p$ is the order of the method.

c) Let

$$
h ~ = ~ \left( \frac { t o l } { d e n } \right) ^ { 1 / \left( p + 1 \right) } .
$$

Very often， however, the initial value is in a special position where most of the $f _ { i }$ may be zero. Thus, we add to our algorithm:

d) Do one Euler step with the step size h proposed in c). e) Repeat a)-c) with the new initial value and choose the smaller of the two proposed step sizes.

An aigorithm like the one above, or a similar one, usually gives a good guess for the initial step size (or at least avoids a very bad choice). Sometimes, more information about h is known, e.g. from previous experience or computations of similar problems.

# Numerical computation of derivatives with respect to initial values and parameters

For the efficient computation of boundary value problems by a shooting technique as explained in Section I.15, we need to compute the derivatives of the solutions with respect to (the missing) initial values Also, if we want to adjust unknown parameters from given data, say by a nonlinear least square procedure, we have to compute the derivatives of the solutions with respect to parameters in the differential equation.

However, due to the error control mechanism with its $\mathrm { I F } ^ { \circ } \mathbf { s }$ and THEN's and step rejections, the numerical result is by no means a smooth function of the initial values or of the parameters.

Example. We have computed the numerical solutions of the Brusselator

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = 1 + y _ { 1 } ^ { 2 } y _ { 2 } - ( B + 1 ) y _ { 1 } } & & { y _ { 1 } ( 0 ) = 1 . 3 } \\ & { y _ { 2 } ^ { \prime } = B y _ { 1 } - y _ { 1 } ^ { 2 } y _ { 2 } } & & { y _ { 2 } ( 0 ) = B } \end{array}
$$

for $x = 2 0$ as a function of B ranging from $B = 2 . 9$ to $B = 3 . 1$ with $\Delta B = 0 . 0 0 0 1$ . The method used was that of Dormand and Prince with local tolerance $\scriptstyle { t o l = 3 \times 1 0 ^ { - 4 } }$ The divided differences for $\partial { y _ { \uparrow } } / \partial { B }$ and $\partial y _ { \boldsymbol { 2 } } / \partial B$ at $x = 2 0$ are plotted in Figure 5.4a and clearly show the lack of smoothness.

![](images/f1f105f5ea1001dc34c192b5c83f1976f339dab2ab9d3e9e056d66268c29ee19.jpg)  
Figure 5.4. Divided differences for numerical solutions of (5.11) a) without step size freeze, b) with step size freeze

A simple device for overcoming this difficulty is to freeze the step size sequence: in the first computation with parameter $B$ ， the selected step sizes are memorized and re-used in the second run with $B + \Delta B$ The divided differences of the two numerical results will then be a much better approximation to $\partial y / \partial B$ . This procedure, for $\Delta B$ very small, is identical to what is called "internal differentiation", obtained, however， with much less programming effort. The corresponding numerical results with step size freeze for Problem (5.11) are shown in Figure 5.4b.

# Exercises

1. (Butcher). Try your favorite code on the example

$$
\begin{array} { r l r l } & { \boldsymbol { y } _ { 1 } ^ { \prime } = f _ { 1 } ( \boldsymbol { y } _ { 1 } , \boldsymbol { y } _ { 2 } ) \ , } & & { \boldsymbol { y } _ { 1 } ( 0 ) = 1 } \\ & { } & & { \boldsymbol { y } _ { 2 } ^ { \prime } = f _ { 2 } ( \boldsymbol { y } _ { 1 } , \boldsymbol { y } _ { 2 } ) \ , } & & { \boldsymbol { y } _ { 2 } ( 0 ) = 0 } \end{array}
$$

where $f$ is defined as follows.

If $\left( { { y } _ { 1 } } | < \left| { { y } _ { 2 } } \right| \right)$ then

Else

$$
\begin{array} { c c } { { f _ { 1 } = 0 , } } & { { f _ { 2 } = \mathrm { s i g n } ( y _ { 1 } ) } } \\ { { { } } } & { { { } } } \\ { { f _ { 2 } = 0 , } } & { { f _ { 1 } = - \mathrm { s i g n } ( y _ { 2 } ) } } \end{array}
$$

End if.

Compu te $y _ { 1 } ( 8 ) , y _ { 2 } ( 8 )$ . Show that the exact solution is periodic.

2. Do numerical computations for the problem $y ^ { \prime } { = } f \left( y \right) , y \left( 0 \right) { = } 1 ,$ $y \left( 3 \right) = ?$ where

$$
f ( y ) = \{ \begin{array} { l l } { y ^ { 2 } } & { \mathrm { i f ~ } 0 \leq y \leq 2 } \\ { } & { } \\ { a ) } & { 1 } \\ { b ) } & { 4 } \\ { } & { } \\ { c ) } & { - 4 + 4 y } \end{array} \} \begin{array} { l } { \mathrm { ~ i f ~ } 0 \leq y \leq 2 } \\ { } \\ { } \\ { } \\ { \mathrm { ~ i f ~ } 2 < y } \\ { } \end{array} 
$$

Remark. The correct answer would be a) 4.5, b) 12, c) $\exp ( 1 0 ) + 1$

3. Consider an s-stage Runge-Kutta method and denote by $s ^ { * }$ the extension is number of distinct $\leq s ^ { * }$ $c _ { i }$ . Prove that the order of any continuous

Hint. Let $q \left( x \right)$ be a polynomial of degree $s ^ { * }$ satisfying $q \left( c _ { i } \right) = 0$ (for $i = 1 , \ldots , s$ ） and investigate the expression $\textstyle { \sum _ { i } b _ { i } ( \theta ) q ( c _ { i } ) }$ ·

# 11.6. Explicit RK-methods of higher order

"We now construct a 10th order RK formula .." (J. Butcher, 1969)

# The Butcher barriers

For methods of order 5 there are 17 order conditions to be satisfied (see Table 2.1). If we choose $s = 5$ we have 15 free parame-ters. Already Kutta raised the question whether there might nevertheless exist a solution, but he had no hope for this and turned straight away to the case $s = 6$ (see II.2, Exercise 5). Kutta's question then remained open for more than 60 years and was answered around 1963 by three authors independently (Ceschino-Kuntzmann (1963), p.89,Shanks (1966), Butcher (1964b,1965b)). Butcher's work is the farthest reaching and we shall mainly follow his ideas in the following:

Theorem 6.1. For $p \geq 5$ no explicit RK-method exists of order p with $s = p$ stages.

Proof: We first treat the case $s = p = 5$ : define the (3,3)-matrices $\boldsymbol { U }$ and $V$ by

$$
U = \left( \begin{array} { c c c c } { \sum _ { b _ { i } } a _ { i 2 } } & { \sum _ { b _ { i } } a _ { i 3 } } & { \sum _ { b _ { i } } a _ { i 4 } } \\ { i } & { i } & { \vdots } \\ { \sum _ { b _ { i } } a _ { i 2 } c _ { 2 } } & { \sum _ { b _ { i } } a _ { i 3 } c _ { 3 } } & { \sum _ { b _ { i } } a _ { i 4 } c _ { 4 } } \\ { i } & { i } & { i } & { g _ { 4 } } \\ { g _ { 2 } } & { g _ { 3 } } & { g _ { 4 } } \end{array} \right) , \quad V = \left( \begin{array} { c c c c } { c _ { 2 } } & { c _ { 2 } ^ { 2 } } & { \sum _ { a _ { 2 j } c _ { j } - c _ { 2 } ^ { 2 } / 2 } } \\ & & { j } & { a _ { 3 j } c _ { j } - c _ { 3 } ^ { 2 } / 2 } \\ { c _ { 3 } } & { c _ { 3 } ^ { 2 } } & { \sum _ { j } a _ { 3 j } c _ { j } - c _ { 3 } ^ { 2 } / 2 } \\ & & { j } & { a _ { 3 j } c _ { j } } \end{array} \right) .
$$

where

$$
g _ { k } = \sum _ { i , j } b _ { i } a _ { i j } a _ { j k } - { \frac { 1 } { 2 } } \sum _ { i } b _ { i } a _ { i k } ( 1 { - } c _ { k } ) .
$$

Then the order conditions for order 5 imply

$$
U V = \left( \begin{array} { c c c } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 1 2 } } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { \frac { 1 } { 1 2 } } } & { { \frac { 1 } { 2 0 } } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

Lemma 1.5 gives ${ { g } _ { 4 } } \mathrm { { = } 0 }$ and consequently ${ c _ { 4 } } \mathrm { { = } } 1$ as in Lemma 1.4. Next we put in (6.1)

$$
g _ { j } = \biggl ( \sum _ { i } b _ { i } a _ { i j } - b _ { j } ( 1 { - } c _ { j } ) \biggr ) ( c _ { j } - c _ { 5 } ) .
$$

Again it can be verified by trivial computations that $U V$ is the same as above. This time it follows that $c _ { 4 } = c _ { 5 }$ hence $c _ { \varsigma } { = } 1$ . Consequently, the expression

$$
\sum _ { i , j , k } b _ { i } ( 1 - c _ { i } ) a _ { i j } a _ { j k } c _ { k }
$$

must be zero (because of $2 \leq k < j < i$ ). However, by multiplying out and using two fifth order conditions, the expression in (6.5) should be 1/120, a contradiction.

The case $p = s = 6$ is treated by considering all "one-leg trees", i.e. the trees which consist of one leg above the root and the fifth-order trees grafted on. The corresponding order conditions have the form

$$
\sum _ { i , j , . . . } b _ { i } a _ { i j } ( a _ { j . . . } \cdot \cdot \mathrm { e x p r e s s i o n s ~ f o r ~ o r d e r } ~ 5 ) = \frac { 1 } { \gamma ( t ) } ~ .
$$

If we let $\begin{array} { r } { \boldsymbol { b } _ { j } ^ { \prime } = \sum _ { i } \boldsymbol { b } _ { i } \boldsymbol { a } _ { i j } } \\ { . } \end{array}$ we are back in the 5-th order 5 stage business and can follow the abovc ideas again. However, the $\gamma ( t )$ values are not the same as before; as a consequence, the product $U V$ in (6.3) now becomes

$$
U V = \left( \begin{array} { c c c } { { \displaystyle { \frac { 1 ! } { ( s - 2 ) ! } } } } & { { \displaystyle { \frac { 2 ! } { ( s - 1 ) ! } } } } & { { 0 } } \\ { { \displaystyle { \frac { 2 ! } { ( s - 1 ) ! } } } } & { { \displaystyle { \frac { 3 ! } { s ! } } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \qquad ( s = 6 )
$$

Further, for $p = s = 7$ we use the "stork-trees" with order conditions

$$
\sum _ { i , j , . . . } b _ { i } a _ { i j } a _ { j k } \left( a _ { k . . . } \cdot \cdot \cdot \mathrm { e x p r e s s i o n s ~ f o r ~ o r d e r ~ } 5 \right) = \frac { 1 } { \gamma \left( t \right) }
$$

and let $\begin{array} { r } { \boldsymbol { b _ { k } } ^ { \prime \prime } = \sum _ { i , j } \boldsymbol { b _ { i } } a _ { i j } a _ { j k } } \end{array}$ and so on. The general case $p = s \geq 5$ is now clear. QED.

# 6-stage, 5-th order processes

We now demonstrate the construction of such processes in full detail following the ideas which allowed Butcher (1964b) to construct 7-stage, 6-th order formulas. The same assumptions, more and more

complicated, were then used in all subsequent constructions of high order ERK's.

"In searching for such processes we are guided by the analysis of the previous section to make the following assumptions:"

$$
\begin{array} { l l } { { \displaystyle { \sum _ { i = 1 } ^ { 6 } b _ { i } a _ { i j } = b _ { j } ( 1 - c _ { j } ) } \qquad } } & { { j = 1 \mathrm { ~ , ~ \dots ~ , 6 ~ } , } } \\ { { \displaystyle { \sum _ { j = 1 } ^ { 6 } a _ { i j } c _ { j } = \frac { c _ { i } ^ { 2 } } { 2 } } \qquad } } & { { i = 3 \mathrm { ~ , ~ \dots ~ , 6 ~ } , } } \\ { { \qquad b _ { 2 } = 0 \mathrm { ~ . ~ } } } & { { } } \end{array}
$$

The advantage of Condition (6.6) is known to us already from Section I.1 (see Lemma 1.3): we can disregard all one-leg trees other than t21

The condition (6.7) together with (6.8) has a similar effect, e.g.

$$
\begin{array} { c } { { \displaystyle \sum _ { i , j , k } b _ { i } a _ { i j } c _ { j } a _ { i k } c _ { k } = \frac 1 { 5 \cdot 2 \cdot 2 } } } \\ { { \displaystyle \sum _ { i , j } b _ { i } c _ { i } ^ { 2 } a _ { i j } c _ { j } = \frac 1 { 5 \cdot 2 } } } \\ { { \displaystyle \sum _ { i } b _ { i } c _ { i } ^ { 4 } = \frac 1 { 5 } } } \end{array}
$$

become equivalent. All branches attached to the root with two vertices reduce to two branches with one vertex. Condition (6.7) cannot be true for $a u \textit { i }$ , because for $i = 2$ it reads $a _ { 2 1 } c _ { 1 } { = } c _ { 2 } ^ { 2 } / 2$ which im plies ${ c _ { 2 } } ^ { = 0 }$ , then all other $c _ { i }$ become zero.

The only trees which are left after the above reduction are the quadrature conditions

$$
\sum _ { i } b _ { i } c _ { i } ^ { q - 1 } = \frac { 1 } { q } \qquad q = 1 , 2 , 3 , 4 , 5
$$

and the two equations

$$
\begin{array} { l } { { \displaystyle \sum _ { i , j , k } b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } = \frac { 1 } { 5 \cdot 3 \cdot 2 } \ , } } \\ { { \displaystyle } } \\ { { \sum _ { i , j } b _ { i } c _ { i } a _ { i j } c _ { j } ^ { 2 } = \frac { 1 } { 5 \cdot 3 } \ . } } \end{array}
$$

We subtract these equations to obtain

$$
\sum _ { i , j } b _ { i } c _ { i } a _ { i j } \left( \sum _ { k } a _ { j k } c _ { k } - \frac { c _ { j } ^ { 2 } } { 2 } \right) = 0 .
$$

From (6.7) the parenthesis is zero except when $j = 2$ , and therefore

$$
\sum _ { i } b _ { i } c _ { i } a _ { i 2 } = 0 .
$$

Wc can simplify still further: from (6.6) we have ${ c _ { 6 } } ^ { = 1 }$ . We now do the same derivations for the order conditions similar to (6.10) and (6.11), but with $c _ { i }$ missing, and finally subtract from (6.12) to obtain

$$
\sum _ { i } b _ { i } ( 1 { - } c _ { i } ) a _ { i 2 } = 0 \ ,
$$

which contains only three terms. Our last simplification is to subtract other order conditions from (6.11) to obtain

$$
\sum _ { i , j } b _ { i } ( 1 { - } c _ { i } ) a _ { i j } c _ { j } ( c _ { j } { - } c _ { 3 } ) = { \frac { 1 } { 6 0 } } - { \frac { c _ { 3 } } { 2 4 } } ,
$$

which again has fewer terms than before. The result of these considerations is the following:

Theorem 6.2. The following algorithm gives 6-stage 5-th order ER K methods with 5 free parameters:

1 $c _ { 2 }$ ， $c _ { 3 }$ ， $c _ { 4 }$ ， $c _ { 5 }$ can be chosen as free parameters， subjecl onty to some trivial exceptions;

2. ${ c _ { 6 } } \mathrm { { = } } 1$ from (6.6) with $j = 6$ ：   
3. $b _ { \mathrm { ~ 1 ~ } }$ ， $b _ { 3 }$ ， $b _ { 4 } ,$ b 5, $b _ { 6 }$ from (6.9) (linear system), $b _ { 2 } { = } 0$ ；   
4 $a _ { 3 2 }$ from (6.7), $i = 3$ $\alpha _ { 4 2 } = \lambda$ arbitrary; $a _ { 4 3 }$ from (6.7), $i = 4$   
5 $a _ { 5 2 }$ from (6.12'), $a _ { 5 4 }$ from (6.13);   
6 $a _ { 5 3 }$ from (6.7), $i = 5$   
7 $\alpha _ { 6 3 }$ ， $a _ { 6 4 } =$ $a _ { 6 5 }$ from (6.6), j=3,4,5 (linear system);   
8. $a _ { 6 2 }$ from (6.7), $i = 6$ 6   
9. ai1 (i=2,..,6) from (1.9). QED.

Examples of such processes are the method of Kutta-Nystrom (Section II.2, Exercise 5) and the formula of Fehlberg (Table 4.5). For a good choice of free parameters see Exercise 1.

# 7-stage, 6-th order processes

Such processes were derived by Butcher (1964b) along the same lines as above. This time there are six additional equations to be treated in addition to (6.6)-(6.11)，so the computations are more complicated. Butcher arrived at an algorithm where $c _ { 2 } , c _ { 3 } , c _ { 5 } , c _ { 6 }$ are free parameters. Among the many possible choices we select the method of Table 6.1 since it possesses positive weights b1， $b _ { 3 } , \ldots , b _ { 7 }$

Table 6.1. Butcher's 6-th order method   

<table><tr><td>0 1 2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td>2-9</td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>35</td><td>55</td><td>35</td><td></td><td>15</td><td></td><td></td><td></td></tr><tr><td>6</td><td>144</td><td>36</td><td>48</td><td></td><td>8</td><td></td><td></td><td></td></tr><tr><td>1 6</td><td>1</td><td>11</td><td>1</td><td></td><td>1</td><td>10</td><td></td><td></td></tr><tr><td></td><td>360</td><td>36</td><td>8</td><td></td><td></td><td>32</td><td>80</td><td></td></tr><tr><td>1</td><td>41</td><td>22</td><td>43</td><td></td><td>118</td><td>195</td><td>39</td><td></td></tr><tr><td></td><td>260</td><td>13</td><td>156</td><td></td><td>39</td><td></td><td></td><td>13</td></tr><tr><td></td><td>13</td><td>0</td><td>11</td><td></td><td>11</td><td>4</td><td>4</td><td></td></tr><tr><td></td><td>200</td><td></td><td>40</td><td></td><td>40</td><td>25</td><td>25</td><td>200</td></tr></table>

# Further Butcher barriers

If we turn our attention to 7-th order methods, the existence of such a method with 8 stages is impossible by the following barrier:

Theorem 6.3. (Butcher (1965b)). For $p \geq 7$ no explicit R K-method exists of order $p$ with $s = p + 1$ stages.

Since the proof of this theorem is much more complicated than that of Theorem 6.1, we do not reproduce it here.

As to methods of order 8, Curtis (1970) and Cooper-Verner (1972) have constructed such processes with $s = 1 1$ . It was for a long time an open question whether there exist methods with 10 stages. John Butcher's dream of setling this difficult question before his 50th birthday did not become true. But he finally succeeded in proving the non-existence for Dahlquist's 6Oth birthday:

Theorem 6.4. (Butcher (1985b)). Fo $r p \geq 8$ no explicit R K-method exists of order p with $s = p + 2$ stages.

For the proof, which is still more complicated, we again refer to Butcher's original paper.

# A 10-th order form ula

The highest order actually obtained for explicitly constructed ERK is ten (Guiness Book of Records, page 333). Curtis (1975) constructed an 18-stage method of order 10. His construction was based solely on simplifying assumptions of the type (6.7), (6.8) and their extensions. Hairer (1978) then constructed a 17-stage method by using the complete arsenal of simplifying ideas. The coeficients are not rational because they are built on the 1O-th order Lobatto quadrature formula. As we shall see below, this formula is of use mainly for precisions higher than,say, $1 0 ^ { - 1 5 }$ . We therefore do not reproduce the coefficients of the method as decimal fractions (they are given with 21D in Hairer (1978)， p.57-58)， but as solutions of a sequence of linear equations, so that they can be obtained with any desired precision (f.p. = free parameter):

$$
c _ { 1 } = 0 , c _ { 2 } = c _ { 1 6 } = 1 / 2 ( \mathrm { f . p . } ) , c _ { 1 7 } = 1 , c _ { 6 } = c _ { 1 3 } = 0 . 7 6 6 6 5 4 ( \mathrm { f . p . } ) ,
$$

$$
c _ { 9 } = \textstyle { \frac { 1 } { 2 } } \left( 1 - \left( \textstyle { \frac { 7 - 2 \sqrt { 7 } } { 2 1 } } \right) ^ { 1 / 2 } \right) , c _ { 1 2 } = \textstyle { \frac { 1 } { 2 } } \left( 1 - \left( \textstyle { \frac { 7 + 2 \sqrt { 7 } } { 2 1 } } \right) ^ { 1 / 2 } \right) ,
$$

$c _ { 1 1 } = 1 - c _ { 9 } , ~ c _ { 1 0 } = 1 - c _ { 1 2 }$ (the 4 Lobatto points),

$$
( 1 { - } c _ { 1 4 } ) = \frac { 4 ( 1 { - } c _ { 1 3 } ) - 3 ( 1 { - } c _ { 1 2 } ) } { 6 ( 1 { - } c _ { 1 3 } ) - 4 ( 1 { - } c _ { 1 2 } ) } ( 1 { - } c _ { 1 2 } ) ,
$$

$$
c _ { 7 } = c _ { 1 4 } , ( 1 - c _ { 1 5 } ) = \frac { 2 } { 3 } ( 1 - c _ { 1 4 } ) , c _ { 3 } = c _ { 1 5 } , c _ { 4 } = \frac { 3 } { 2 } c _ { 3 } ,
$$

$$
c _ { 5 } = \frac { 4 c _ { 4 } - 3 c _ { 6 } } { 6 c _ { 4 } - 4 c _ { 6 } } c _ { 6 } , ~ c _ { 8 } = \frac { 2 0 c _ { 6 } c _ { 7 } - 1 5 c _ { 9 } ( c _ { 6 } + c _ { 7 } ) + 1 2 c _ { 9 } ^ { 2 } } { 3 0 c _ { 6 } c _ { 7 } - 2 0 c _ { 9 } ( c _ { 6 } + c _ { 7 } ) + 1 5 c _ { 9 } ^ { 2 } } c _ { 9 } ,
$$

$$
b _ { 1 3 } = 0 . 1 3 ~ ( \mathrm { f . p . } ) , b _ { 1 4 } = 0 . 1 8 ~ ( \mathrm { f . p . } ) , b _ { 1 5 } = 0 . 1 2 ~ ( \mathrm { f . p . } ) , b _ { 1 6 } = \frac { 1 } { 3 0 } ~ ( \mathrm { f . p . } ) ,
$$

$$
 { b } _ { 4 } = 0 ,  { b } _ { 5 } = 0 ,  { b } _ { 8 } = 0 ,  { b } _ { 2 } + b \_ { 1 6 } = 0 ,  { b } _ { 3 } + b \_ { 1 5 } = 0 ,  { b } _ { 6 } + b \_ { 1 3 } = 0 ,  { b } _ { 7 } + b \_ { 1 4 }
$$

$$
b _ { \ 1 0 } = b _ { \ 1 2 } = \frac { 1 } { 6 0 } ( 1 4 - \sqrt { 7 } ) , \quad b _ { 9 } = b _ { \ 1 1 } = \frac { 1 } { 6 0 } ( 1 4 + \sqrt { 7 } ) , \quad b _ { \ 1 } = b _ { \ 1 7 } = \frac { 1 } { 3 0 }
$$

(the Lobatto weights).

The computation of the non zero a., is then done in four steps as indicated in Table 6.2.

![](images/66f5c3d7c7182553225ad07f548db60450c81249aff0a1bd1f00ba09cbe1d3da.jpg)  
Table 6.2.

Step 1: Use the equations

$$
\begin{array} { r l } { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } - c _ { i } } & { \quad i = 2 , \ldots , 1 7 , } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } c _ { j } + \frac { c _ { i } ^ { 2 } } { 2 } } & { \quad i = 3 , \ldots , 1 4 , 1 7 , } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } c _ { j } ^ { 2 } + \frac { c _ { i } ^ { 3 } } { 3 } } & { \quad i = 4 , \ldots , 1 4 , 1 7 , } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } c _ { j } ^ { 2 } + \frac { c _ { i } ^ { 3 } } { 3 } } & { \quad i = 4 , \ldots , 1 4 , 1 7 , } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } c _ { j } ^ { 3 } + \frac { c _ { i } ^ { 4 } } { 4 } } & { \quad i = 6 , \ldots , 1 4 , 1 7 , } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { j } c _ { j } ^ { 4 } + \frac { c _ { i } ^ { 5 } } { 5 } } & { \quad i = 9 , 1 0 , 1 1 , 1 2 , 1 7 } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { 1 3 , j } c _ { j } ^ { 4 } - \frac { c _ { i } ^ { 5 } } { 2 } } & { \quad i = 9 , 1 0 , 1 2 , 1 7 } \\ { \underset { j = 1 } { \overset { \ldots } { \longrightarrow } } a _ { 1 3 , j } c _ { j } ^ { 4 } - \frac { c _ { i } ^ { 5 } } { 2 } } & { \quad i = 1 , \ldots , 1 4 , 1 6 , j ^ { 4 } - \frac { c _ { i } ^ { 5 } } { 2 } \alpha _ { j } c _ { j } ^ { 4 } . } \end{array}
$$

for $i \le 1 0$ . The only condition for $i = 2$ is ${ a _ { 2 , 1 } } ^ { a } { = } { c _ { 2 } }$ . There are two conditions for $i \ = 3$ ：

$$
\begin{array} { c } { { a _ { 3 , 1 } + a _ { 3 , 2 } = c _ { 3 } } } \\ { { { } } } \\ { { a _ { 3 , 1 } c _ { 1 } + a _ { 3 , 2 } c _ { 2 } = \displaystyle \frac { c _ { 3 } ^ { 2 } } { 2 } \ . } } \end{array}
$$

This linear system determines ${ a } _ { 3 , 1 }$ and ${ a } _ { 3 , 2 }$ . In a similar way one gets all the non-zero $a _ { i j }$ for $i \le 1 0$ by solving linear systems of Vandermonde type.

Step 2: Here we use the conditions

$$
\begin{array} { r l } { \displaystyle \sum _ { i = j + 1 } ^ { 1 7 } b _ { i } \alpha _ { i j } = b _ { j } ( 1 - c _ { j } ) \quad } & { j = 1 1 , 1 2 , 1 3 , 1 4 , 1 5 , 1 6 \mathrm { ~ , } } \\ { \displaystyle \sum _ { i = j + 1 } ^ { 1 7 } b _ { i } c _ { i } \alpha _ { i j } = \frac { 1 } { 2 } b _ { j } ( 1 - c _ { j } ^ { 2 } ) \quad } & { j = 1 1 , 1 2 , 1 3 , 1 4 , 1 5 \mathrm { ~ , } } \\ { \displaystyle \sum _ { i = j + 1 } ^ { 1 7 } b _ { i } c _ { i } ^ { 2 } \alpha _ { i j } = \frac { 1 } { 3 } b _ { j } ( 1 - c _ { j } ^ { 3 } ) \quad } & { j = 1 1 , 1 2 , 1 3 , 1 4 \mathrm { ~ , } } \\ { \displaystyle \sum _ { i = j + 1 } ^ { 1 7 } b _ { i } c _ { i } ^ { 3 } \alpha _ { i j } = \frac { 1 } { 4 } b _ { j } ( 1 - c _ { j } ^ { 4 } ) \quad } & { j = 1 1 , 1 2 , 1 3 , 1 4 \mathrm { ~ , } } \end{array}
$$

The only condition for $j = 1 6$ yields

$$
a _ { 1 7 , 1 6 } = \frac { b _ { 1 6 } } { b _ { 1 7 } } ( 1 { - } c _ { 1 6 } ) \ ;
$$

two conditions for j=15 give the coefficients a16,15 and a17,15, etc. Again, one has to solve linear systems of Vandermonde type.

Step 3:

$$
\begin{array} { r l } & { a _ { 1 5 , 6 } = - a _ { 1 5 , 1 3 } , a _ { 1 5 , 7 } = - a _ { 1 5 , 1 4 } , a _ { 1 6 , 3 } = - a _ { 1 6 , 1 5 } , a _ { 1 7 , 2 } = - a _ { 1 7 , 1 6 } , } \\ & { a _ { 1 7 , 3 } = - a _ { 1 7 , 1 5 } , a _ { 1 3 , 4 } = a _ { 6 , 4 } , a _ { 1 3 , 5 } = a _ { 6 , 5 } , a _ { 1 4 , 4 } = a _ { 7 , 4 } , a _ { 1 4 , 5 } = a _ { 7 , 5 } , } \\ & { a _ { 1 5 , 2 } = a _ { 3 , 2 } ; } \end{array}
$$

compute $a _ { 1 5 , 1 }$ and $^ a 1 6 , 1$ from the first equation of (6.14) for $i = 1 5$ and 16 respectively.

Step 4: Define

$$
w _ { i } = \sum _ { j = 1 } ^ { i - 1 } a _ { i j } c _ { j } ^ { 5 } \qquad i = 1 1 , 1 2 , 1 3 , 1 4 , 1 7
$$

and solve the five equations $\scriptstyle { k = 0 , 1 , 2 , 3 , 4 , k = 4 }$ is added arbitrarily)