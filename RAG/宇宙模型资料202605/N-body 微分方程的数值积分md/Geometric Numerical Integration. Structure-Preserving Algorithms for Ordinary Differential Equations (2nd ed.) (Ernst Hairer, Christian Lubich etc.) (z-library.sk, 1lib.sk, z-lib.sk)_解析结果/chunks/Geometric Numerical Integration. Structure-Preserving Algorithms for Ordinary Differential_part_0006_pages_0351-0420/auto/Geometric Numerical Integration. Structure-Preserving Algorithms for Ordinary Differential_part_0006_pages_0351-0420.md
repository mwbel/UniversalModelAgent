Table6.2.Statistics of Gauss methods (total number of function evaluations,number of iterations per step) for computations of the Kepler problem over one period with $e = 0 . 6$   
Modified Newton iteration (general problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order4</td><td rowspan=1 colspan=1>3837.7</td><td rowspan=1 colspan=1>5115.1</td><td rowspan=1 colspan=1>7653.8</td><td rowspan=1 colspan=1>11252.8</td><td rowspan=1 colspan=1>16772.1</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>5975.5</td><td rowspan=1 colspan=1>8833.9</td><td rowspan=1 colspan=1>13873.0</td><td rowspan=1 colspan=1>23072.4</td><td rowspan=1 colspan=1>36671.8</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>7634.7</td><td rowspan=1 colspan=1>10953.3</td><td rowspan=1 colspan=1>17172.5</td><td rowspan=1 colspan=1>30032.2</td><td rowspan=1 colspan=1>56892.0</td></tr></table>

inHairer&Wanner (1996,Sect.IV.8),thecpu time is now considerably larger. Further improvements are possible,if the Jacobian of $f$ and hence also the $L R$ decomposition of $M$ isfrozen overa couple of steps.But all these efforts can hardly beat(in cpu time) the straightforward fixed-point iterations.In accordancewith the experience of Sanz-Serna &Calvo(1994,Sect.5.5）we recommendin general the use of fixed-point iterations.

Separable Systemsand Second Order Differential Equations.Many interesting differential equationsare of the form

$$
\dot { \eta } = f ( y ) , \qquad \dot { y } = g ( \eta ) .
$$

Forexample,the second orderdifferential equation $\ddot { y } = f ( y )$ is obtained by putting $g ( \eta ) = \eta$ .Also Hamiltonian systems with separable Hamiltonian ${ \cal H } ( p , q ) = T ( p ) +$ $U ( q )$ are of the form (6.19).

For this particular system the Runge-Kutta equations (6.1) become

$$
\zeta _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( y _ { n } + Z _ { j n } ) = 0 , \qquad Z _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } g ( \eta _ { n } + \zeta _ { j n } ) = 0 .
$$

In this case we can still do better:instead of the standard fixed-point iteration (6.16) weapplya Gauss-Seidel like iteration

$$
\zeta _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } f ( y _ { n } + Z _ { j n } ^ { k } ) , \qquad Z _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } g ( \eta _ { n } + \zeta _ { j n } ^ { k + 1 } ) ,
$$

whichis explicit for separable systems (6.19).Notice that the starting approximations have to be computed only for $\zeta _ { i n }$ .Those for $\boldsymbol { Z } _ { i n }$ are then obtained by(6.20) with $k + 1 = 0$ .

For second order differential equations $\ddot { y } = f ( y )$ ,where $g ( \eta ) = \eta$ ,thisiteration becomes

$$
Z _ { i n } ^ { k + 1 } = \hbar c _ { i } \eta _ { n } + h ^ { 2 } \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } f ( y _ { n } + Z _ { j n } ^ { k } ) ,
$$

Table 6.3.Statistics of iterations (6.2O) for Gauss methods (total numberof function evaluations,numberof iterationsperstep)forcomputations of the Kepler problem overone period with $e = 0 . 6$   
Fixed-point iteration (separable problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order 4</td><td rowspan=1 colspan=1>4378.7</td><td rowspan=1 colspan=1>6036.0</td><td rowspan=1 colspan=1>8574.3</td><td rowspan=1 colspan=1>12013.0</td><td rowspan=1 colspan=1>17172.1</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>6135.6</td><td rowspan=1 colspan=1>9234.1</td><td rowspan=1 colspan=1>14273.1</td><td rowspan=1 colspan=1>2.3392.4</td><td rowspan=1 colspan=1>36471.8</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>7814.9</td><td rowspan=1 colspan=1>11313.4</td><td rowspan=1 colspan=1>17412.6</td><td rowspan=1 colspan=1>30272.2</td><td rowspan=1 colspan=1>56772.0</td></tr></table>

where $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } } \end{array}$ and $\widehat { a } _ { i j }$ are te enres f hesquare $A ^ { 2 }$ of the Runge-Kutta matrix(any Nystrommethod could beapplied aswell).Due to the factor $h ^ { 2 }$ in(6.21) weexpect this iteration to converge about twice as fast as the standard fixed-point iteration.

TheKepler problem isasecond orderdifferential equation,so that the iteration (6.21）canbe applied.Inanalogy to theprevious tableswepresentin Table6.3the statistics of such an implementation of the Gauss methods.We observe that forrelatively large stepsizes thenumber of iterationsrequired per step in nearly halved (compared to Table6.1).For high accuracy requirements the number of necessary iterations is surprisingly small,and the question ariseswhether such an implementation can compete with high order explicit composition methods.

Comparison Between Implicit Runge-Kutta and Composition Methods.We consider second orderdifferential equations $\ddot { y } = f ( y )$ ,so that composition methods basedon the explicit Stormer-Verlet scheme can be applied.Weuse the coefficientsofmethod(V.3.14)which has turned out to beexcellentin the experiments of Sect.V.3.2.Itisamethod of order8and uses 17 functionevaluationsper integration step.

We compare it with the Gauss methods of order 8 and 12 (i.e., $s = 4$ and $s = 6$ ). Asa starting approximation for the solution of the nonlinear system (6.1） we use （6.7）with $m = 3$ , $\mu _ { 1 } = 0$ , $\mu _ { 2 } = 1$ , $\mu _ { 3 } = 1 . 7 5$ , $\mu _ { i j }$ chosen such that （6.11） holds for $k = 1 , \ldots , s + i - 1$ ,and $\beta _ { i j }$ , $\nu _ { i j }$ such that order $s + 2$ is obtained.Since we are concerned with second orderdifferential equations,we apply the iterations (6.20) until the norm of the difference of two successve approximations is below $1 0 ^ { - 1 7 }$

For both classes of methods we use compensated summation (Algorithm 5.1), which permits us to reduce rounding errors.For composition methodswe apply this technique forall updates of the basicintegrator.For Runge-Kutta methods,weuse itforaddingtheincremento $y _ { n }$ andalsoforcomputingthesum $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } k _ { i }$

The work-precision diagrams of the comparison are given inFig.6.2.Theupper pictures correspond to the Kepler problem with $e = 0 . 6$ and an integration over100 periods;the lower pictures correspond to the outer solar system with data given in Sect.I.2.4and an integrationover 5OoooO earthdays.The leftpictures show the

![](images/8a5ca4612c51c671466bbec8c71d1b4fbdc34561f4378e08f802f3b574132666.jpg)  
Fig.6.2.Work-precision diagrams for two problems (Keplerand outer solar system） and three numerical integrators(composition method with coefficients of method(V.3.14) based ontheexplicit Stormer-Verlet scheme and the Gauss methods of orders 8and12)

Euclidean norm of theerror at the end of the integration interval asa function of total numbers of function evaluations required for the integration;the pictures to the rightpresent the same error asa function of the cpu times (with optimizing compiler ona SunBlade 1Oo workstation).We can draw the following conclusions from this experiment:

·the implementation of composition methods based on the Stormer-Verlet scheme isextremely easy;that of implicit Runge-Kuttamethods is slightly more involved because it requires a stopping criterion for the fixed-point iterations;   
·the overhead (total cpu time minus that used for the function evaluations) is much higherfor the implicit Runge-Kutta methods;this is seen from the fact that implicit Runge-Kutta methods require less function evaluations fora given accuracy,but often more cpu time;   
among thetwo Gaussmethods,the higher ordermethod ismore efficient forall precisions of practical interest;   
·forvery accurate computations (say,in quadruple precision),high order Runge-Kuttamethods are more efficient than composition methods;   
much of the computation in the Runge-Kutta codecan be done in parallel (e.g., the $s$ function evaluations of a fixed-point iteration);composition methods do not have this potential;   
implicit Runge-Kutta methods can be applied to general (non-separable） differential equations,and thecost ofthe implementation is at most twice as large;if oneis obliged to use an implicit method as the basic method for composition, many advantages of composition methods are lost.

Bothclasses of methods (composition and implicit Runge-Kutta) are of interest inthe geometric integration ofdifferential equations.Each one has itsadvantages and disadvantages.

Fortran codes of these computations are available on the Internet under the homepage<http://www.unige.ch/math/folks/hairer>.AMatlabversion ofthese codesisdescribed inE.&M.Hairer(2003).

# VIII.7 Exercises

1.Considera one-step method applied toa Hamiltonian system.Givea probabilisticproof of the property that the error of the numerical Hamiltonian due to roundoff grows like $\mathcal { O } ( \sqrt { t } e p s )$

2.Prove that the collocation polynomial can be writtenas

$$
w _ { n } ( t ) = y _ { n } + h \sum _ { i = 1 } ^ { s } \beta _ { i } ( t ) f ( Y _ { i n } ) ,
$$

where the polynomials $\beta _ { i } ( t )$ are a solution of

$$
\sum _ { j = 1 } ^ { s } \beta _ { j } ( t ) c _ { j } ^ { k - 1 } = \frac { t ^ { k } } { k } .
$$

3.Applyyour favouritecode totheKepler problemand tothe outer solarsystem withdataasinFig.6.2.Plotawork-precision diagram.

Remark.Figure7.1 shows our resultsobtained with the 8th order Runge-Kutta codeDop853（Hairer,Ngrsett&Wanner1993)comparedtoan8thordercomposition method.Rounding errors are more pronounced for Dop853,because compensated summation is not applied.Computations on shorter time intervalsand comparisons ofrequired function evaluationswould bemorein favour forDop853.Itisalso of interest toconsider high order Runge-Kutta Nystrom methods.

4.Consider starting approximations

$$
Y _ { i n } ^ { 0 } = y _ { n - 2 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } ^ { ( 2 ) } f ( Y _ { j , n - 2 } ) + h \sum _ { j = 1 } ^ { s } \beta _ { i j } ^ { ( 1 ) } f ( Y _ { j , n - 1 } )
$$

![](images/8912cc4af13149dd0f571942c8812d2dbcc2875e6ece57637504e28d0d4b88a5.jpg)  
Fig.7.1.Work-precision diagrams for the explicit,variable step size Runge-Kutta code Dop853applied to two problems(Kepler and outer solar system).For a comparison,the resultsof Fig.6.2 for the composition method are included

which use the internal stages of two consecutive steps without any additional function evaluation.What are the conditions such that(7.1) is of order $s + 1$ ,of order $s + 2 ^ { \prime }$ ？

Compare the efficiency of these formulaswith the algorithms(A) and (B）of Sect.VIII.6.1.

5.Prove that fora second order differential equation $\ddot { y } = f ( y )$ (more precisely, for $\dot { y } = z , \dot { z } = f ( y ) )$ theapplication of the $s$ -stage Gauss method gives

$$
\begin{array} { l } { { y _ { n + 1 } ~ = ~ y _ { n } + h \dot { y } _ { n } + h ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ) f ( y _ { n } + Z _ { i n } ) } } \\ { { \dot { y } _ { n + 1 } ~ = ~ \ddot { y } _ { n } + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } f \big ( y _ { n } + Z _ { i n } \big ) , } } \end{array}
$$

where $Z _ { i n }$ is obtained from the iteration (6.21).

Hint.The coefficients of the Gauss methods satisfy $\begin{array} { r } { \sum _ { j } b _ { j } a _ { j i } = b _ { i } ( 1 - c _ { i } ) } \end{array}$ for all $i$

# Chapter IX. Backward Error Analysis and Structure Preservation

One of the greatest virtues of backward analysis...is that when it is theappropriateformofanalysis it tendstobe verymarkedlysuperior toforward analysis.Invariablyin such casesit hasremarkable formal simplicity and gives deepinsight into the stability (or lack of it）ofthe algorithm. (J.H.Wilkinson,IMA Bulletin 1986)

The origin of backward erroranalysisdates back to thework of Wilkinson(1960)in numerical linearalgebra.For the studyof integrationmethods for ordinarydifferential equations,its importance was seen much later.Thepresent chapteris devoted to this theory.Itis very useful,when the qualitative behaviour of numerical methods isof interest,and when statements over very long time intervals are needed.The formal analysis (construction of themodified equation,study of its properties)gives alreadyalot of insight into numerical methods.Forarigorous treatment,themodifiedequation,which isa formal series in powers of the stepsize,hasto be truncated. Theerror,induced by such a truncation,can be madeexponentially small,and the resultsremain valid on exponentially long time intervals.

# IX.1Modified Differential Equation-Examples

Consider an ordinary differential equation

$$
{ \dot { y } } = f ( y ) ,
$$

and a numerical method $\varPhi _ { h } ( y )$ which produces the approximations

![](images/1251b029870e43c9329b9330e7b35638ec7ac9de69fe553f7e1deababf369ad8.jpg)

Aforward error analysis consists of the study of the errors $y _ { 1 } - \varphi _ { h } ( y _ { 0 } )$ (local error) and $y _ { n } - \varphi _ { n h } ( y _ { 0 } )$ （global error） in the solution space.The idea of backward error analysisistosearch foramodifieddifferentialequation $\dot { \widetilde { y } } = f _ { h } ( \widetilde { y } )$ of the form

$$
\dot { \widetilde { y } } = f ( \widetilde { y } ) + h f _ { 2 } ( \widetilde { y } ) + h ^ { 2 } f _ { 3 } ( \widetilde { y } ) + \dots ,
$$

such that $y _ { n } = \widetilde { y } ( n h )$ ,and in studying thedifference of the vector fields $f ( y )$ and $f _ { h } ( y )$ .Thisthen givesmuch insight into the qualitative behaviour of the numerical solution and into the global error $y _ { n } - y ( n h ) = \widetilde { y } ( n h ) - y ( n h )$ Weremark that the series in（1.1） usually diverges and that one has to truncate it suitably.The effect ofsuch a truncation will be studiedin Sect.IX.7.For the moment we content ourselveswith a formal analysis without takingcare ofconvergence issues.The idea ofinterpreting the numerical solution as the exact solution of amodified equation iscommon to many numerical analysts("...Thisispossible since themap isthe solution of some physical Hamiltonian problem which,in some sense,is close to the original problem",Ruth(1983),or"...the symplectic integrator createsanumerical Hamiltonian system that isclose to the original...",Gladman,Duncan&Candy 1991).A systematic study started with thework ofGriffiths& Sanz-Serna(1986), Feng（1991）,Sanz-Serna（1992）,Yoshida（1993),Eirola（1993),Fiedler&Scheurle (1996),and many others.

For the computation of the modified equation(1.1)we put $y : = \widetilde { y } ( t )$ forafixedt, andweexpand the solution of(1.1) intoa Taylor series

$$
\begin{array} { l } { { \widetilde { y } ( t + h ) ~ = ~ y + h \big ( f ( y ) + h f _ { 2 } ( y ) + h ^ { 2 } f _ { 3 } ( y ) + . . . \big ) } } \\ { { { } } } \\ { { { } + ~ \frac { h ^ { 2 } } { 2 ! } \big ( f ^ { \prime } ( y ) + h f _ { 2 } ^ { \prime } ( y ) + . . . \big ) \big ( f ( y ) + h f _ { 2 } ( y ) + . . . \big ) + . . . ~ . } } \end{array}
$$

Weassume that the numerical method $\varPhi _ { h } ( y )$ can be expanded as

$$
\Phi _ { h } ( y ) = y + h f ( y ) + h ^ { 2 } d _ { 2 } ( y ) + h ^ { 3 } d _ { 3 } ( y ) + \ldots .
$$

(the coefficient of $h$ is $f ( y )$ forconsistent methods).The functions $d _ { j } ( y )$ areknown and are typicallycomposedof $f ( y )$ and itsderivatives.Forthe explicitEulermethod wesimplyhaved,（y）=O forall $j \geq 2$ In order to get $\widetilde { y } ( n h ) = y _ { n }$ forall $n$ ,we must have $\widetilde { y } ( t + h ) = \varPhi _ { h } ( y )$ .Comparing like powers of $h$ in the expressions（1.2） and(1.3)yields recurrencerelations for the functions $f _ { j } ( y )$ ,namely,

$$
\begin{array} { l } { { f _ { 2 } ( y ) ~ = ~ d _ { 2 } ( y ) - \frac { 1 } { 2 ! } f ^ { \prime } f ( y ) ~ } } \\ { { { } } } \\ { { f _ { 3 } ( y ) ~ = ~ d _ { 3 } ( y ) - \frac { 1 } { 3 ! } \Big ( f ^ { \prime \prime } ( f , \bar { f } ) ( y ) + f ^ { \prime } \bar { f } ^ { \prime } \bar { f } ( y ) \Big ) - \frac { 1 } { 2 ! } \Big ( \bar { f } ^ { \prime } f _ { 2 } ( y ) + \bar { f } _ { 2 } ^ { \prime } \bar { f } ( y ) \Big ) . } } \end{array}
$$

Example1.1.Consider the scalar differential equation

$$
\dot { y } = y ^ { 2 } , \qquad y ( 0 ) = 1
$$

with exact solution $y ( t ) = 1 / ( 1 - t )$ Ithas a singularityat $t = 1$ Weapply the explicit Eulermethod $y _ { n + 1 } = y _ { n } + h f ( y _ { n } )$ with step size $h = 0 . 0 2$ The picture in Fig.1.1 presents the exact solution (dashed curve) together with the numerical solution (bullets).The above procedure for the computation of the modified equation, implementedasaMapleprogram（seeHairer&Lubich 2Ooo）gives

![](images/af46e63ceecc65aa60cbe315e90687aa5e23802e50a50ecb7274073f845cd73f.jpg)  
Fig.1.1.Solutions of the modified equation for the problem (1.5)

>fcn $: = y - > y - 2$ ：  
$>$ nn:=6：  
$>$ fcoe[1] $: =$ fcn（y）:  
$>$ forn from2 by1 to nn do  
$>$ modeq $: =$ sum（hj\*fcoe[j+1]，j=0..n-2）：diffy[0]： $\begin{array} { r l } { \mathbf { \Psi } } & { { } = \mathbf { \Psi } \times \mathbf { \Psi } } \end{array}$ ：forifrom1by1tondodiffy[i]： $=$ diff(diffy[i-1],y)\*modeq:od:ytilde： $=$ sum(h^k\*diffy[k]/k！， $k = 0$ ..n）：  
$>$ res： $=$ ytilde-y-h\*fcn(y):  
$>$ tay： $=$ convert(series(res, $h = 0$ , $\nrightarrow \beth$ ),polynom）：fcoe[n]： $=$ -coeff(tay，h，n）：  
$>$ od:  
$>$ simplify(sum(h^j\*fcoe[j+1]，j=0..nn-1)）；

Its output is

$$
\dot { \widetilde { y } } = \widetilde { y } ^ { 2 } - h \widetilde { y } ^ { 3 } + h ^ { 2 } { \frac { 3 } { 2 } } \widetilde { y } ^ { 4 } - h ^ { 3 } { \frac { 8 } { 3 } } \widetilde { y } ^ { 5 } + h ^ { 4 } { \frac { 3 1 } { 6 } } \widetilde { y } ^ { 6 } - h ^ { 5 } { \frac { 1 5 7 } { 1 5 } } \widetilde { y } ^ { 7 } \pm \dots .
$$

Theabove picture also presents the solution of the modified equation,when truncatedafter1,2,3,and4terms.We observeanexcellentagreement of thenumerical solution with the exact solution of the modified equation.

Asimilar program for the implicit midpoint rule (I.1.7) computes the modified equation

$$
\dot { \widetilde { y } } = \widetilde { y } ^ { 2 } + h ^ { 2 } \frac { 1 } { 4 } \widetilde { y } ^ { 4 } + h ^ { 4 } \frac { 1 } { 8 } \widetilde { y } ^ { 6 } + h ^ { 6 } \frac { 1 1 } { 1 9 2 } \widetilde { y } ^ { 8 } + h ^ { 8 } \frac { 3 } { 1 2 8 } \widetilde { y } ^ { 1 0 } \pm \ldots ,
$$

and for theclassical Runge-Kutta method of order 4(left tableau of(II.1.8))

$$
\dot { \widetilde { y } } = \widetilde { y } ^ { 2 } - h ^ { 4 } { \frac { 1 } { 2 4 } } \widetilde { y } ^ { 6 } + h ^ { 6 } { \frac { 6 5 } { 5 7 6 } } \widetilde { y } ^ { 8 } - h ^ { 7 } { \frac { 1 7 } { 9 6 } } \widetilde { y } ^ { 9 } + h ^ { 8 } { \frac { 1 9 } { 1 4 4 } } \widetilde { y } ^ { 1 0 } \pm \dots .
$$

Weobserve that the perturbation terms in the modified equation are of size $\mathcal { O } ( h ^ { p } )$ ,where $p$ isthe order of themethod.This is truein general.

Theorem1.2. Suppose that themethod $y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )$ isoforder $p$ i.e.,

$$
\Phi _ { h } ( y ) = \varphi _ { h } ( y ) + h ^ { p + 1 } \delta _ { p + 1 } ( y ) + \mathcal { O } ( h ^ { p + 2 } ) ,
$$

where $\varphi _ { t } ( y )$ denotes the exact flow of $\dot { y } = f ( y )$ ,and $h ^ { p + 1 } \delta _ { p + 1 } ( y )$ the leading term ofthelocal truncation error.The modifiedequationthen satisfes

$$
\tilde { \tilde { y } } = f ( \widetilde { y } ) + h ^ { p } f _ { p + 1 } ( \widetilde { y } ) + h ^ { p + 1 } f _ { p + 2 } ( \widetilde { y } ) + \dots , \qquad \widetilde { y } ( 0 ) = y _ { 0 }
$$

with $f _ { p + 1 } ( y ) = \delta _ { p + 1 } ( y )$

Proof. The construction of the functions $f _ { j } ( y )$ (see the beginning of this section） shows that $f _ { j } ( y ) = 0$ for $2 \le j \le p$ ifand onlyif $\varPhi _ { h } ( y ) - \varphi _ { h } ( y ) = \mathcal { O } ( h ^ { p + 1 } )$ □

Afirstapplication of themodified equation (1.1) is the existence ofan asymptoticexpansionof theglobal error.Indeed,bythenonlinear variation ofconstants formula,the difference between its solution $\widetilde { y } ( t )$ and the solution $y ( t )$ of $\dot { y } = f ( y )$ satisfies

$$
\widetilde { y } ( t ) - y ( t ) = h ^ { p } e _ { p } ( t ) + h ^ { p + 1 } e _ { p + 1 } ( t ) + \dots .
$$

Since $y _ { n } = \widetilde { y } ( n h ) + \mathcal { O } ( h ^ { N } )$ for the solution of a truncated modified equation,this proves the existence of an asymptotic expansion in powers of $h$ for the global error $y _ { n } - y ( n h )$

Alarge part of this chapter studies properties of themodified differential equation,and the question of the extent to which structures (such as conservation of invariants,Hamiltonian structure） in the problem $\dot { y } = f ( y )$ can carry over to the modified equation.

Example1.3.We next consider theLotka-Volterra equations

$$
\dot { q } = q ( p - 1 ) , \qquad \dot { p } = p ( 2 - q ) ,
$$

and we apply(a) the explicit Euler method,and (b) the symplectic Eulermethod, both with constant step size $h = 0 . 1$ .The first terms of their modified equations are

$$
\begin{array} { l } { { \displaystyle { \dot { q } = q ( p - 1 ) - \frac { h } { 2 } q ( p ^ { 2 } - p q + 1 ) + \mathcal { O } ( h ^ { 2 } ) } , } } \\ { { \displaystyle { \dot { p } = - p ( q - 2 ) - \frac { h } { 2 } p ( q ^ { 2 } - p q - 3 q + 4 ) + \mathcal { O } ( h ^ { 2 } ) } , } } \\ { { \displaystyle { \ddot { q } = q ( p - 1 ) - \frac { h } { 2 } q ( p ^ { 2 } + p q - 4 p + 1 ) + \mathcal { O } ( h ^ { 2 } ) } , } } \\ { { \displaystyle { \dot { p } = - p ( q - 2 ) + \frac { h } { 2 } p ( q ^ { 2 } + p q - 5 q + 4 ) + \mathcal { O } ( h ^ { 2 } ) } . } } \end{array}
$$

Figure1.2 shows the numerical solutions for initial values indicated byathick dot. Inthepicturestothe left theyareembeddedin the exact flowof thedifferential equation,whereasin thoseto therighttheyareembedded in the flow of themodified differential equation,truncated after the $h ^ { 2 }$ terms.Asin the first example,we observe an excellent agreement of the numerical solution with the exact solution of themodified equation.For the symplectic Euler method,the solutions of the truncated modified equation are periodic,asisthe case for the unperturbed problem (Exercise 5).

![](images/8aed9f8d27f6c4365d8d80e3f27425ec0dc92e9357eecda5b8b8574777fe5f94.jpg)  
Fig.1.2.Numerical solutioncompared to the exact and modified flows

![](images/3d7a85bb874c6185cafa30e38865c264d70987ba061097eeae75cd603a4ed971.jpg)  
Fig.1.3.Study of the truncation in the modified equation

In Fig.1.3 we present the numerical solution and the exact solution of the modified equation,once truncated after the $h$ terms(dashed-dotted),and once truncated afterthe $h ^ { 2 }$ terms(dotted).The exact solution of theproblemis included asa solid curve.This shows that taking more terms in the modified equation usually improves theagreement of its solution with the numerical approximation of the method.

Example1.4.Fora linear differential equationwith constant coefficients

$$
{ \dot { y } } = A y , \qquad y ( 0 ) = y _ { 0 }
$$

we consider numerical methods which yield $y _ { n + 1 } = R ( h A ) y _ { n }$ ,where $R ( z )$ isthe stability function(VI.4.9) of themethod.In thiscasewe get $y _ { n } = R ( h A ) ^ { n } y _ { 0 }$ ,s0 that $y _ { n } = { \widetilde { y } } ( n h )$ ,where $\begin{array} { r } { \widetilde { y } ( t ) = R ( h . A ) ^ { t / h } y _ { 0 } = \exp \left( \frac { t } { h } \ln R ( h A ) \right) y _ { 0 } } \end{array}$ is the solution ofthemodified differential equation

$$
\dot { \widetilde { y } } = \frac { 1 } { h } \ln R ( h A ) \widetilde { y } = ( A + h b _ { 2 } A ^ { 2 } + h ^ { 2 } b _ { 3 } A ^ { 3 } + . . . ) \widetilde { y }
$$

with suitable constants $b _ { 2 } , b _ { 3 } , \dotsc$ .Since $R ( z ) = 1 + z + \mathcal { O } ( z ^ { 2 } )$ and $\ln ( 1 + x ) = x -$ $x ^ { 2 } / 2 + \mathcal { O } ( x ^ { 3 } )$ bothhaveapositive radius ofconvergence,the series(1.11） converges for $| h | < h _ { 0 }$ with some $h _ { 0 } ~ > ~ 0$ We shall see later that thisisan exceptional situation.In general,themodified equation isa formal divergent series.

# IX.2 Modified Equations of Symmetric Methods

Inthisand thefollowing sections we investigate how the structure of the differential equationand geometricproperties of themethod are reflected in the modified differential equation.Here we begin by studying thisquestion for symmetric/reversible methods.

Consider a numerical method $\phi _ { h }$ Recall that itsadjoint $y _ { n + 1 } ~ = ~ \varPhi _ { h } ^ { * } ( y _ { n } )$ is definedby the relation $y _ { n } = \varPhi _ { - h } ( y _ { n + 1 } )$ (see Definition II.1.4).

Theorem 2.1 (Adjoint Methods).Let $f _ { j } ( y )$ bethe coefficient functions ofthe modifiedequationforthemethod $\phi _ { h }$ Then,thecoefficient functions $f _ { j } ^ { * } ( y )$ ofthe modifiedequation fortheadjointmethod $\boldsymbol { \phi } _ { h } ^ { * }$ satisfy

$$
f _ { j } ^ { * } ( y ) = ( - 1 ) ^ { j + 1 } f _ { j } ( y ) .
$$

Proof.The solution $\widetilde { y } ( t )$ of the modified equation for $\boldsymbol { \varPhi } _ { h } ^ { * }$ has to satisfy $\widetilde { y } ( t ) =$ $\bar { \Phi } _ { - h } \big ( \widetilde { y } ( t + h ) \big )$ or,equivalently, $\mathcal { Y } ( t - h ) = \Phi _ { - h } ( y )$ with $y : = y ( t ) .$ Weget(2.1）if wereplace $h$ with $- h$ inthe formulas(1.1),(1.2)and(1.3). □

For symmetric methods we have $\phi _ { h } ^ { * } = \phi _ { h }$ ,implying $f _ { j } ^ { * } ( y ) = f _ { j } ( y )$ Wethereforeget the followingcorollary to Theorem 2.1.

Theorem2.2 (Symmetric Methods).The coefficient functions ofthe modified equation ofasymmetric method satisfy $f _ { j } ( y ) = 0$ whenever $j$ is even,so that(1.1） hasan expansion in even powers of $h$

This theorem explains the $h ^ { 2 }$ -expansion in themodified equation (1.7)of the midpoint rule.

Asaconsequence of Theorem2.2,the asymptotic expansion(1.1O) of the global error is also in even powers of $h$ .Thisproperty is responsible for the success of $h ^ { 2 }$ - extrapolation methods.

Consider now a numerical method applied to a $\rho$ -reversibledifferentialequation asstudiedin Sect.V.1.Recall from TheoremV.1.5 thatasymmetricmethod is $\rho$ reversible under the $\rho$ -compatibilitycondition(V.1.4),whichissatisfied formost numericalmethods.

Theorem2.3 (ReversibleMethods).Considera $\rho$ -reversibledifferentialequation ${ \dot { y } } = f ( y )$ anda $\rho$ -reversiblenumericalmethod $\varPhi _ { h } ( y )$ .Then,every truncationof the modifieddifferentialequationisagain $\rho$ -reversible.

ProofLet $f _ { j } ( y )$ be the $j$ th coefficient of the modified equation (1.1) for $\phi _ { h }$ The proof is by induction on $j$ So assume that for $\jmath = 1 , \ldots , r$ thevector field $f _ { j } ( y )$ is $\rho$ -reversible,i.e.,

$$
\rho \circ f _ { j } = - f _ { j } \circ \rho .
$$

We show that the same relation holds also for $j = r + 1$ Byassumption,the truncated modified equation

$$
\dot { \widetilde { y } } = f ( \widetilde { y } ) + h f _ { 2 } ( \widetilde { y } ) + \ldots + h ^ { r - 1 } f _ { r } ( \widetilde { y } )
$$

is $\rho$ -reversible,sohatby(V.1.2）,itha $\rho$ -reversibleflow $\varphi _ { r , t } ( y )$ ,that is, $\rho \circ \varphi _ { r , t } =$ $\varphi _ { r , t } ^ { - 1 } \circ \rho$ Byconstruction of the modified equation,we have

$$
\Phi _ { h } ( y ) = \varphi _ { r , h } ( y ) + h ^ { r + 1 } f _ { r + 1 } ( y ) + \mathcal { O } ( h ^ { r + 2 } ) .
$$

Since $\varphi _ { r , h } ( y ) = y + \mathcal { O } ( h )$ ,thisimplies

$$
\varPhi _ { h } ^ { - 1 } ( y ) = \varphi _ { r , h } ^ { - 1 } ( y ) = h ^ { r + 1 } f _ { r + 1 } ( y ) + O ( h ^ { r + 2 } ) .
$$

Since both $\phi _ { h }$ and $\varphi _ { r , h }$ are $\rho$ -reversiblemaps,these tworelations yield $\rho \circ f _ { r + 1 } =$ $- f _ { r + 1 } \circ \rho$ asdesired. □

# IX.3Modified Equations of Symplectic Methods

Wenow present one of the most important results of this chapter.We consider a Hamiltonian system $\dot { y } = J ^ { - 1 } \nabla H ( y )$ withan infinitelydifferentiable Hamiltonian $H ( y )$ ,and we show that the modified equation of symplectic methods is also Hamiltonian.

# IX.3.1 Existence of a Local Modified Hamiltonian

...if we neglect convergencequestions then one canalways finda formal integral... (J.Moser1968)

Theorem3.1.Ifasymplecticmethod $\varPhi _ { h } ( y )$ isapplied to $a$ Hamiltonian system witha smooth Hamiltonian $H : \mathbb { R } ^ { 2 d }  \mathbb { R }$ ,thenthemodifiedequation(1.1）is alsoHamiltonian.Moreprecisely,thereexist smooth functions $H _ { j } : \mathbb { R } ^ { 2 d }  \mathbb { R }$ for $j = 2 , 3 , . . . ,$ such that $f _ { j } ( y ) = J ^ { - 1 } \nabla H _ { j } ( y )$

Thefollowing proof by induction,whose ideas can be traced back to Moser (1968),was given by Benettin& Giorgilli（1994）and Tang（1994).Itcan beextended tomany other situations.We havealready encountered its reversibleversion in the proof of Theorem2.3.

Proof.Assume that $f _ { j } ( y ) = J ^ { - 1 } \nabla H _ { j } ( y )$ for $j = 1 , 2 , \ldots , r$ (this is satisfied for $r = 1$ ,because $f _ { 1 } ( y ) = f ( y ) = J ^ { - 1 } \nabla H ( y ) )$ We have to prove the existence of a Hamiltonian $H _ { r + 1 } ( y ) .$ Theidea is to consider the truncated modified equation

$$
\dot { \widetilde { y } } = f ( \widetilde { y } ) + h f _ { 2 } ( \widetilde { y } ) + \dots + h ^ { r - 1 } f _ { r } ( \widetilde { y } ) ,
$$

which isaHamiltoniansystemwith Hamiltonian $H ( y ) + h H _ { 2 } ( y ) + \ldots + h ^ { r - 1 } H _ { r } ( y ) .$ Itsfow $\varphi _ { r , t } ( y _ { 0 } )$ ,compared tothat of(1.1),satisfies

$$
\Phi _ { h } ( y _ { 0 } ) = \varphi _ { r , h } ( y _ { 0 } ) + h ^ { r + 1 } f _ { r + 1 } ( y _ { 0 } ) + \mathcal { O } ( h ^ { r + 2 } ) ,
$$

and also

$$
\begin{array} { r } { \Phi _ { h } ^ { \prime } ( y _ { 0 } ) = \varphi _ { r , h } ^ { \prime } ( y _ { 0 } ) + h ^ { r + 1 } f _ { r + 1 } ^ { \prime } ( y _ { 0 } ) + \mathcal { O } ( h ^ { r + 2 } ) . } \end{array}
$$

By our assumption on the method and by the induction hypothesis, $\phi _ { h }$ and $\varphi _ { r , h }$ aresymplectic transformations.This,together with $\varphi _ { r , h } ^ { \prime } ( y _ { 0 } ) = I + \mathcal { O } ( h )$ ,therefore implies

$$
J = \varPhi _ { h } ^ { \prime } ( y _ { 0 } ) ^ { T } J \varPhi _ { h } ^ { \prime } ( y _ { 0 } ) = J + h ^ { r + 1 } \Big ( f _ { r + 1 } ^ { \prime } ( y _ { 0 } ) ^ { T } J + J f _ { r + 1 } ^ { \prime } ( y _ { 0 } ) \Big ) + \mathcal { O } ( h ^ { r + 2 } ) .
$$

Consequently,the matrix $J f _ { r + 1 } ^ { \prime } ( y )$ is symmetric and the existence of $H _ { r + 1 } ( y )$ satisfying $f _ { r + 1 } ( y ) = J ^ { - 1 } \nabla H _ { r + 1 } ( y )$ follows from the Integrability Lemma VI.2.7. This part of theproof is similar to that of Theorem VI.2.6.

For Hamiltonians $H : D \to \mathbb { R }$ the statement of the above theorem remains valid with $H _ { j } : D \to \mathbb { R }$ on domains $D \subset \mathbb { R } ^ { 2 d }$ on which the Integrability Lemma VI.2.7 isapplicable.This is the case for simply connected domains $\mathcal { D }$ ,but not in general (see the discussion after the proof of Lemma VI.2.7).

# IX.3.2Existence ofa Global Modified Hamiltonian

ByLemma VI.5.3 every symplectic one-stepmethod $\phi _ { h } : ( p , q ) \mapsto ( P , Q )$ canbe locally expressed intermsofa generating function $S ( P , q , h )$ as

$$
p = P + { \frac { \partial S } { \partial q } } ( P , q , h ) , \qquad Q = q + { \frac { \partial S } { \partial P } } ( P , q , h ) .
$$

This property allows us to give an independent proof of Theorem 3.I and inaddition to show that the modified equation is Hamiltonian with $\bar { H } ( p , q )$ defined on the same domainas the generating function.The following result is mentioned in Benettin $\&$ Giorgilli(1994)andinthe thesisofMurua(1994）,p.100.

Theorem3.2.Assumethat the symplecticmethod $\phi _ { h }$ hasa generatingfunction

$$
S ( P , q , h ) = h S _ { 1 } ( P , q ) + h ^ { 2 } S _ { 2 } ( P , q ) + h ^ { 3 } S _ { 3 } ( P , q ) + \dots
$$

with smooth $S _ { j } ( P , q )$ defined on an openset $\mathcal { D }$ .Then,themodifieddifferentialequationisaHamiltonian systemwith

$$
\widetilde { H } ( p , q ) = H ( p , q ) + h H _ { 2 } ( p , q ) + h ^ { 2 } H _ { 3 } ( p , q ) + \dots ,
$$

where the functions $H _ { j } ( p , q )$ aredefinedand smooth on the whole of $\mathcal { D }$

Proof.By TheoremVI.5.7,the exact solution $( P , Q ) = \left( \widetilde { p } ( t ) , \widetilde { q } ( t ) \right)$ of the Hamiltonian system corresponding to $\breve { H } ( p , q )$ is given by

$$
p = P + \frac { \partial \widetilde { S } } { \partial q } ( P , q , t ) , \qquad Q = q + \frac { \partial \widetilde { S } } { \partial P } ( P , q , t ) ,
$$

where $\bar { S }$ is the solution of the Hamilton-Jacobi differential equation

$$
\frac { \partial \widetilde { S } } { \partial t } ( P , q , t ) = \widetilde { H } \Big ( P , \bar { q } + \frac { \partial \widetilde { S } } { \partial P } ( P , q , t ) \Big ) , \qquad \widetilde { S } ( P , \bar { q } , 0 ) = 0 .
$$

Since $\tilde { H }$ dependson the parameter $h$ ,thisisalso the case for $\widetilde { S }$ Ouraim is to determine the functions $H _ { j } ( p , q )$ such that the solution $\check { S } ( P , q , t )$ of(3.5） coincides for $t = h$ with (3.3).

We first express $\check { S } ( P , q , t )$ asaseries

$$
\widetilde { S } ( P , q , t ) = t \widetilde { S } _ { 1 } ( P , q , h ) + t ^ { 2 } \widetilde { S } _ { 2 } ( P , q , h ) + t ^ { 3 } \widetilde { S } _ { 3 } ( P , q , h ) + \dots ,
$$

insert it into(3.5）and compare powers of $t$ .This allows usto obtain the functions $\tilde { S } _ { j } ( p , q , h )$ recursivelyin terms of derivatives of $\bar { H }$ :

$$
\begin{array} { l } { { { \widetilde { S } } _ { 1 } ( p , q , h ) ~ = ~ { \widetilde { \cal H } } ( p , q ) } } \\ { { { 2 \widetilde { S } } _ { 2 } ( p , q , h ) ~ = ~ \displaystyle \biggl ( { \frac { \partial { \widetilde { \cal H } } } { \partial q } } \cdot { \frac { \partial { \widetilde { S } } _ { 1 } } { \partial P } } \biggr ) ( p , q , h ) } } \\  { { 3 \widetilde { S } } _ { 3 } ( p , q , h ) ~ = ~ \displaystyle \biggl ( { \frac { \partial { \widetilde { \cal H } } } { \partial q } } \cdot { \frac { \partial { \widetilde { S } } _ { 2 } } { \partial P } } \biggr ) ( p , q , h ) + { \displaystyle { \frac { 1 } { 2 } } \biggl ( { \frac { \partial ^ { 2 } { \widetilde { \cal H } } } { \partial q ^ { 2 } } } \Bigl ( { \frac { \partial { \widetilde { S } } _ { 1 } } { \partial P } } , { \frac { \partial { \widetilde { S } } _ { 1 } } { \partial P } } \Bigr ) \biggr ) ( p , q , h ) . } } \end{array} ~ \Longrightarrow ~ { \displaystyle ( { \widetilde { \cal B } } \cdot { \widetilde { \cal B } } _ { 1 } ) }
$$

We then write $\tilde { S } _ { j }$ asaseries

$$
\widetilde { S } _ { j } ( p , q , h ) = \widetilde { S } _ { j 1 } ( p , q ) + h \widetilde { S } _ { j 2 } ( p , q ) + h ^ { 2 } \widetilde { S } _ { j 3 } ( p , q ) + \dots ,
$$

insert it and the expansion (3.4） for $\bar { H }$ into (3.6),and compare powers of $h$ This yields $S _ { 1 k } ( p , q ) = H _ { k } ( p , q )$ andfor $j > 1$ wesee that $\tilde { S } _ { j k } ( p , q )$ isa function of derivativesof $H _ { l }$ with $l < k$

The requirement $S ( p , q , h ) = S ( p , q , h )$ finally shows $S _ { 1 } ( p , q ) = \tilde { S } _ { 1 1 } ( p , q )$ , $S _ { 2 } ( p , q ) = S _ { 1 2 } ( p , q ) + \bar { S } _ { 2 1 } ( p , q )$ ,etc.,sothat

$S _ { j } ( p , q ) = H _ { j } ( p , q ) +$ “functionofderivativesof $H _ { k } ( p , q )$ with $k < j "$

Fora given generating function $S ( P , q , h )$ ,thisrecurrence relation allowsus to determine successively the $H _ { j } ( p , q )$ We see from these explicit formulas that the functions $H _ { j }$ are defined on the same domain as the $S _ { j }$ □

AsaconsequenceofTheorem3.2andTheoremsVI.5.4andVI.5.5weobtain the following result.

Theorem3.3.Asymplectic(partitioned) Runge-Kutta methodappliedtoasystem with smooth Hamiltonian $H : D  \mathbb { R }$ (with $D \subset \mathbb { R } ^ { 2 d }$ an arbitrary open set) has a modified Hamiltonian(3.4)with smoothfunctions $H _ { j } : D \to \mathbb { R } .$ □

Example3.4 (Symplectic EulerMethod).Thesymplectic Eulermethod is nothing other than(3.2）with $S ( P , q , h ) = h H ( P , q ) .$ Wetherefore have(3.3）with $S _ { 1 } ( p , q ) = H ( p , q )$ and $S _ { j } ( p , q ) = 0$ for $j > 1$ .Following the constructive proof of Theorem 3.2weobtain

$$
\widetilde { \cal H } = { \cal H } - { \frac { h } { 2 } } H _ { p } H _ { q } + { \frac { h ^ { 2 } } { 1 2 } } \Bigl ( H _ { p p } H _ { q } ^ { 2 } + H _ { q q } H _ { p } ^ { 2 } + 4 H _ { p q } H _ { q } H _ { p } \Bigr ) + \ldots .
$$

as the modified Hamiltonian of the symplectic Euler method.For vector-valued $p$ and $q$ ,theexpression $H _ { p } H _ { q }$ is the scalar product of the vectors $H _ { p }$ and $H _ { q }$ ,and $H _ { p p } H _ { q } ^ { 2 } = H _ { p p } ( H _ { q } , H _ { q } )$ withthesecond derivativeinterpretedasabilinearmapping.

Asaparticular example consider the pendulum problem (I.1.13),whichis Hamiltonian with $H ( p , q ) = p ^ { 2 } / 2 - \cos q ,$ andapplythe symplectic Euler method. By(3.7),the modifiedHamiltonian is

$$
\widetilde { H } ( p , q ) = H ( p , q ) - { \frac { h } { 2 } } p \sin { q } + { \frac { h ^ { 2 } } { 1 2 } } \Bigl ( \sin ^ { 2 } { q } + p ^ { 2 } \cos { q } \Bigr ) + \ldots .
$$

This example illustrates that the modified equation corresponding to a separable Hamiltonian (i.e., $H ( p , q ) = T ( p ) + U ( q ) )$ isin general not separable.Moreover, itshows that the modified equation of a second order differential equation $\ddot { q } =$ $- \nabla U ( q )$ (or equivalently, $\dot { q } = p , \dot { p } = - \nabla U ( q ) ,$ isingeneral nota second order equation.

In principle,the constructiveproof of Theorem 3.2 allowsus to explicitly computethe modified equation of every symplectic (partitioned)Runge-Kutta method. InSect.IX.9.3 below we shallhowever,giveexplicit formulasfor themodified Hamiltonian in terms oftrees.This alsoyieldsan alternative proof of Theorem 3.3.

# IX.3.3Poisson Integrators

ConsideraPoissonsystem,i.e.,adifferential equation

$$
\dot { y } = B ( y ) \nabla H ( y ) ,
$$

where the structure matrix $B ( y )$ satisfies theconditions ofLemma VII.2.3,and applya Poisson integrator(Definition VII.4.6).

Theorem3.5.IfaPoissonintegrator $\varPhi _ { h } ( y )$ is applied to the Poisson system(3.8), thenthemodifiedequationislocallya Poissonsystem.Moreprecisely,forevery $y _ { 0 } \in \mathbb { R } ^ { n }$ thereexistaneighbourhood $U$ andsmooth functions $H _ { j } : U \to \mathbb { R }$ such thaton $U$ ,themodifiedequationisof theform

$$
\dot {  { \boldsymbol { \tilde { y } } } } = B (  { \boldsymbol { \tilde { y } } } ) \Big ( \nabla H (  { \boldsymbol { \tilde { y } } } ) + h \nabla H _ { 2 } (  { \boldsymbol { \tilde { y } } } ) + h ^ { 2 } \nabla H _ { 3 } (  { \boldsymbol { \tilde { y } } } ) + \dots \Big ) .
$$

Proof.Weuse the local change of coordinates $( u , c ) = \chi ( y )$ of the Darboux-Lie Theorem.ByCorollaryVI1.3.6,thistransforms(3.8) to

$$
\dot { \boldsymbol { u } } = J ^ { - 1 } \nabla _ { \boldsymbol { u } } K ( { \boldsymbol { u } } , { \boldsymbol { c } } ) , \qquad \dot { \boldsymbol { c } } = 0 ,
$$

where $K ( u , c ) = H ( y )$ and $\nabla _ { u }$ is the gradient with respect to $u$ .The same transformation takes $\varPhi _ { h } ( y )$ to $\chi \circ \varPhi _ { h } \circ \chi ^ { - 1 } ( u , c ) = ( \varPsi _ { h } ^ { 1 } ( u , c ) , c )$ ,wherebyLemmaVII.4.10 $u \mapsto \varPsi _ { h } ^ { \bot } ( u , c )$ isasymplectic transformation for every $c$ ByTheorem3.1,themodified equation in the $( u , c )$ variables is of the form

$$
\dot { \tilde { u } } = J ^ { - 1 } \nabla _ { u } \tilde { K } ( \tilde { u } , \tilde { c } ) , \qquad \dot { \tilde { c } } = 0
$$

with $K ( u , c ) = K ( u , c ) + h K _ { 2 } ( u , c ) + h ^ { 2 } K _ { 3 } ( u , c ) + \ldots$ Transforming back to the $y$ variables gives themodified equation(3.9)with $H _ { j } ( y ) = K _ { j } ( u , c ) .$ □

Theaboveresult is purely local in that itrelies on the local transformation of the Darboux-Lie Theorem.Itcanbemade more global under additional conditions on thedifferential equation.

Theorem 3.6.1f $H ( y )$ and $B ( y )$ aredefined and smooth ona simply connected domain $\mathcal { D }$ ,andif $B ( y )$ isinvertibleon $\boldsymbol { D }$ ，thena Poisson integrator $\varPhi _ { k } ( y )$ has $\boldsymbol { a }$ modifiedequation(3.9)with smooth functions $H _ { j } ( y )$ defined on allof $\mathcal { D }$ .

Proof.By the construction of Sect.IX.1,the coefficient functions $f _ { j } ( y )$ of themodified equation（1.1）aredefined and smooth on $D$ Since $B ( y )$ isassumed invertible, there exist unique smooth functions $g _ { j } ( y )$ suchthat $f _ { j } ( y ) = B ( y ) g _ { j } ( y )$ Itremains to show that $g _ { j } ( y ) = \nabla H _ { j } ( y )$ forafunction $H _ { j } ( y )$ defined on $\mathcal { D }$ .

Bythelocal result of Theorem 3.5,weknowthatfor every $y _ { 0 } \in \mathcal { D }$ thereexist functions $H _ { j } ^ { \mathrm { u } } ( y )$ such that $g _ { j } ( y ) = \nabla H _ { j } ^ { \cup } ( y )$ inaneighbourhood of $y _ { 0 }$ .This implies that the Jacobian of $g _ { j } ( y )$ issymmetric on $\mathcal { D }$ TheIntegrabilityLemmaVI.2.7thus proves the existence of functions $H _ { j } ( y )$ defined on all of $D$ such that $g _ { j } ( y ) =$ $\nabla H _ { j } ( y )$ □

# IX.4 Modified Equations of Splitting Methods

Forsplitting methodsapplied toa differential equation

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y ) ,
$$

themodified differential equation is obtained directlywith thecalculus ofLiederivativesand theBaker-Campbell-Hausdorffformula.Thisapproachisdueto Yoshida (1993)who considered the case of separable Hamiltonian systems.

First-Order Splitting.Consider the splitting method

$$
\varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } ,
$$

whereh is the time- $h$ flowof $\dot { y } = f ^ { [ i ] } ( y )$ IntermsoftheLiederivatives $D _ { i }$ definedby $D _ { i } g ( y ) = g ^ { \prime } ( y ) f ^ { [ i ] } ( y )$ ,thismethod becomes,usingLemma II.5.1,

$$
\begin{array} { r } { \varPhi _ { h } = \exp ( h D _ { 2 } ) \exp ( h D _ { 1 } ) \mathrm { I d } , } \end{array}
$$

andwith the BCH formula(III.4.11),(III.4.12) this reads

$$
\varPhi _ { h } = \exp ( h \widetilde { D } ) \mathrm { I d }
$$

with

$$
\tilde { D } = D _ { 1 } + D _ { 2 } + { \frac { h } { 2 } } \left[ D _ { 2 } , D _ { 1 } \right] + { \frac { h ^ { 2 } } { 1 2 } } \Big ( \left[ D _ { 2 } , \left[ D _ { 2 } , D _ { 1 } \right] \right] + \left[ D _ { 1 } , \left[ D _ { 1 } , D _ { 2 } \right] \right] \Big ) + \dots .
$$

It follows that $\phi _ { h }$ is formally the exact time- $h$ flow of the modified equation

$$
\dot { \tilde { y } } = \widetilde { f } ( \tilde { y } ) \qquad \mathrm { w i t h } \quad \widetilde { f } = \widetilde { D } \mathrm { I d } .
$$

This gives

$$
\widetilde { f } ( y ) = f ( y ) + h f _ { 2 } ( y ) + h ^ { 2 } f _ { 3 } ( y ) \lneq . . .
$$

with $f = f ^ { [ 1 ] } + f ^ { [ 2 ] }$ and

$$
\begin{array} { r l } & { : = \frac { 1 } { 2 } \Big ( f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] } - f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] } \Big ) } \\ & { = \frac { 1 } { 1 2 } \Big ( f ^ { [ 1 ] ^ { \prime \prime } } ( f ^ { [ 2 ] } , f ^ { [ 2 ] } ) + f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] ^ { \prime } } f ^ { [ 2 ] } - f ^ { [ 2 ] ^ { \prime \prime } } ( f ^ { [ 1 ] } , f ^ { [ 2 ] } ) - f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] } } \\ & { \qquad + f ^ { [ 2 ] ^ { \prime \prime } } ( f ^ { [ 1 ] } , f ^ { [ 1 ] } ) + f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] ^ { \prime } } f ^ { [ 1 ] } - f ^ { [ 1 ] ^ { \prime \prime } } ( f ^ { [ 2 ] } , f ^ { [ 1 ] } ) - f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] } \Big ) . } \end{array}
$$

Strang Splitting.For thesymmetric splitting

$$
\Phi _ { h } ^ { \mathrm { [ S ] } } = \varphi _ { h / 2 } ^ { \mathrm { [ 1 ] } } \circ \varphi _ { h } ^ { \mathrm { [ 2 ] } } \circ \varphi _ { h / 2 } ^ { \mathrm { [ 1 ] } }
$$

thesymmetricBCH formula (II.4.14),(III.4.15)yields

$$
\varPhi _ { h } ^ { [ \mathrm { S } ] } = \exp ( \frac { h } { 2 } D _ { 1 } ) \exp ( h D _ { 2 } ) \exp ( \frac { h } { 2 } D _ { 1 } ) \mathrm { I d } = \exp ( h \widetilde { D } ^ { [ \mathrm { S } ] } ) \mathrm { I d }
$$

with

$$
\widetilde D ^ { [ \mathrm { S l } ] } = D _ { 1 } + D _ { 2 } + h ^ { 2 } \Big ( { - \frac { 1 } { 2 4 } [ D _ { 1 \backslash } [ D _ { 1 \backslash } , D _ { 2 } ] ] + \frac { 1 } { 1 2 } [ D _ { 2 \backslash } [ D _ { 2 } , D _ { 1 } ] ] } \Big ) \mp \ldots \Big ) .
$$

Hence,s] is the formally exact flow of the modified equation

$$
\dot { \tilde { y } } =  { \widetilde { f } ^ { \mathrm { I S } } }  { \left( \tilde { y } \right) } \qquad \mathrm { w i t h } \quad  { \widetilde { f } ^ { \mathrm { I S } } }  { \left[ \ b { \mathrm { s } } \right] } =  { \widetilde { D } ^ { \mathrm { I S } } }  { \mathrm { I d } } .
$$

This gives

$$
\widetilde { f } ^ { \mathrm { [ S ] } } ( y ) = f ( y ) + h ^ { 2 } \ : f _ { 3 } ^ { \mathrm { [ S ] } } ( y ) + h ^ { 4 } \ : f _ { 5 } ^ { \mathrm { [ S ] } } ( y ) + \ldots
$$

with $f = f ^ { [ 1 ] } + f ^ { [ 2 ] }$ and

$$
\begin{array} { r } { f _ { 3 } ^ { [ 8 ] } = \Big ( \frac { 1 } { 1 2 } \big ( f ^ { [ 1 ] ^ { \prime \prime } } ( f ^ { [ 2 ] } , f ^ { [ 2 ] } ) \ast f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] ^ { \prime } } f ^ { [ 2 ] } - f ^ { [ 2 ] ^ { \prime \prime } } ( f ^ { [ 1 ] } , f ^ { [ 2 ] } ) - f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] ^ { \prime } } \Big ) } \\ { - \frac { 1 } { 2 4 } \big ( f ^ { [ 2 ] ^ { \prime \prime } } ( f ^ { [ 1 ] } , f ^ { [ 1 ] } ) + f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] ^ { \prime } } f ^ { [ 1 ] } - f ^ { [ 1 ] ^ { \prime \prime } } ( f ^ { [ 2 ] } , f ^ { [ 1 ] } ) - f ^ { [ 1 ] ^ { \prime } } f ^ { [ 2 ] ^ { \prime } } f ^ { [ 1 ] ^ { \prime } } \big ) } \end{array}
$$

Themodified equations for general splittingmethods(II.5.13)are obtained in the sameway,usingLemma III.5.5.

Hamiltonian Splittings.Considera differential equation (4.1）where the vector fields $f ^ { [ i ] } ( y ) = J ^ { - 1 } \nabla H ^ { [ i ] } ( y )$ areHamiltonian.Lemma VII.3.1 shows that the commutatorof theLiederivatives of two Hamiltonianvector fieldsis theLiederivative ofanother Hamiltonian vector field which correspondsto the Poisson bracket of the two Hamiltonians: $\left[ D _ { F } , D _ { G } \right] = D _ { \{ G , F \} } .$ This implies in particular that the modifieddifferential equations(4.3)and(4.5）areagain Hamiltonian.Forthefirst-order splitting,we thus get $f _ { j } ( y ) = J ^ { - 1 } \nabla H _ { j } ( y )$ ,whereby(4.2)and(4.3)，

$$
\begin{array} { r c l } { { } } & { { } } & { { { \cal H } _ { 2 } ~ = ~ \frac { 1 } { 2 } \{ { \cal H } ^ { [ 1 ] } , { \cal H } ^ { [ 2 ] } \} } } \\ { { } } & { { } } & { { { \cal H } _ { 3 } ~ = ~ \frac { 1 } { 1 2 } \Bigl ( \{ \{ { \cal H } ^ { [ 1 ] } , { \cal H } ^ { [ 2 ] } \} , { \cal H } ^ { [ 2 ] } \} + \{ \{ { \cal H } ^ { [ 2 ] } , { \cal H } ^ { [ 1 ] } \} , { \cal H } ^ { [ 1 ] } \} \Bigr ) , } } \end{array}
$$

andfor the Strang spliting,by (4.4)and (4.5)，

$$
H _ { 3 } ^ { [ \mathrm { S l } ] } = - \frac { 1 } { 2 4 } \{ \{ H ^ { [ 2 ] } , H ^ { [ 1 ] } \} , H ^ { [ 1 ] } \} \mp \frac { 1 } { 1 2 } \{ \{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} , H ^ { [ 2 ] } \} .
$$

Theexplicit expressions from the BCH-formula show that the modified Hamiltonian isdefined on the same open set as the smooth Hamiltonians $H ^ { [ i ] }$ ,

For the splitting $H ( p , q ) = T ( p ) + U ( q )$ ofa separable Hamiltonian,this approach givesanalternative derivation of the modified equation(3.7） of the symplectic Euler method,and a simple construction of the modified equation of the Stormer-Verletmethod(Yoshida1993).Here,the formula simplifiesto

$$
\widetilde { \cal H } ^ { [ \mathrm { S } ] } = { \cal H } + h ^ { 2 } \Bigl ( - \frac { 1 } { 2 4 } U _ { q q } ( T _ { p } , T _ { p } ) + \frac { 1 } { 1 2 } T _ { p p } ( U _ { q } , U _ { q } ) \Bigr ) + \ldots .
$$

# IX.5Modified Equations of Methods onManifolds

Weconsider the relationship between numerical methods fordifferential equations onmanifoldsand the associated modified differential equations.We give applicationsto the study of first integrals,constrained Hamiltonian systems,and Lie-Poisson integrators.

# IX.5.1Methods on ManifoldsandFirst Integrals

Consideradifferential equation ona smooth manifold $\mathcal { M }$ ,

$$
\begin{array} { r } { \dot { y } = f ( y ) \qquad \mathrm { w i t h } \quad f ( y ) \in T _ { y } \mathcal { M } , } \end{array}
$$

with a smooth vector field $f ( y )$ defined on $\mathcal { M }$

Theorem5.1. Let $\phi _ { h } : \mathcal { M } \to \mathcal { M }$ beanintegratoron themanifold $\mathcal { M }$ with $\varPhi _ { h } ( y )$ depending smoothly on $( y , h )$ Then,thereexistsamodifieddifferential equation on $\mathcal { M }$ ,

$$
\dot { \widetilde { y } } = f ( \widetilde { y } ) + h f _ { 2 } ( \widetilde { y } ) + h ^ { 2 } f _ { 3 } ( \widetilde { y } ) + \dots .
$$

with smooth $f _ { j } ( y ) \in T _ { y } \mathcal { M }$ suchthat $\varphi _ { r , h } ( y ) = \varPhi _ { h } ( y ) + \mathcal { O } ( h ^ { r + 1 } )$ where $\varphi _ { r , t } ( y )$ denotestheflow ofthe truncationof(5.2)after $_ { f }$ terms.

Forsymmetric methods,theexpansion(5.2)contains only even powers of $h$

Proof.We choosea local parametrization $y = \chi ( z )$ of themanifold $\mathcal { M }$ Inthe coordinates $z$ thedifferentialequation(5.1）reads

$$
\dot { z } = F ( z ) \quad \mathrm { w i t h } \ F ( z ) \operatorname { d e f i n e d } \mathrm { b y } \quad \chi ^ { \prime } ( z ) F ( z ) = f ( \chi ( z ) ) ,
$$

and the numerical integrator becomes

$$
\varPsi _ { h } ( z ) = \chi ^ { - 1 } \circ \varPhi _ { h } \circ \chi ( z ) .
$$

Since $F ( z )$ and $\varPsi _ { h } ( z )$ aresmooth,the standard backward error analysison $\mathbb { R } ^ { n }$ of Sect.IX.1 yieldsamodified equation for the integrator $\varPsi _ { h } ( z )$ ,

$$
{ \dot { \widetilde z } } = F ( { \widetilde z } ) + h F _ { 2 } ( { \widetilde z } ) + h ^ { 2 } F _ { 3 } ( { \widetilde z } ) + \dots .
$$

Defining

$$
f _ { j } ( y ) = \chi ^ { \prime } ( z ) F _ { j } ( z ) \qquad \mathrm { f o r } \quad y = \chi ( z )
$$

gives the desired vector fields $f _ { j } ( y )$ on $\mathcal { M }$ It follows from the uniqueness of the modified equation inthe parameter space that $f _ { j } ( y )$ is independent of the choice of the local parametrization.

Theadditional statement on symmetric methods follows from Theorem2.2,because $\psi _ { h }$ is symmetric if and onlyif $\phi _ { h }$ issymmetric. □

Underan analyticity assumption,the converse statement also holds.

Theorem5.2.Letthe integrator $\phi _ { h } : U \to \mathbb { R } ^ { n }$ (withopen $U \subset \mathbb { R } ^ { n }$ bereal analyticin $h$ ,andlet $\mathcal { M } = \{ y \in U ; g ( y ) = 0 \}$ with real analytic $g : U  \mathbb { R } ^ { m } .$ If thecoefficient functions $f _ { j } ( y )$ ofthemodifieddifferential equation(5.2) satisfy $g ^ { \prime } ( y ) f _ { j } ( y ) = 0$ forall $j$ andall $y \in \mathcal { M }$ ,thentherestriction of $\phi _ { h }$ to $\mathcal { M }$ definesan integratoron $\mathcal { M }$ ,i.e., $\phi _ { h } : { \mathcal { M } } \to { \mathcal { M } } .$

Proof.By the assumption on $f _ { j } ( y )$ ,the flow of the truncated modified equation satisfies $g \circ \varphi _ { r , h } ( y ) = 0$ forall $r \geq 1$ and all $y \in \mathcal { M }$ Since $\varphi _ { r , h } ( y ) = \phi _ { h } ( y ) +$ $\mathcal { O } ( h ^ { r + 1 } )$ wehave $g \circ \phi _ { h } ( y ) = \mathcal { O } ( h ^ { r + 1 } )$ forall $_ { r }$ Theanalyticity assumptions thereforeimply $g \circ \varPhi _ { h } ( y ) = 0$ . □

Theorems5.1and5.2 apply to many situations treated in Chap.IV.

First Integrals.The followingresult was obtained byGonzalez,Higham& Stuart （1999)and Reich(1999）with different arguments.

Corollary5.3.Consideradifferentialequation $\dot { y } = f ( y )$ withafrst integral $I ( y )$ , i.e., $I ^ { \prime } ( y ) f ( y ) = 0$ forally.If thenumericalmethodpreserves thisfirst integral, thenevery truncationof themodifiedequation has $I ( y )$ asafirst integral.

Proof.This follows from Theorem 5.1byconsidering $\dot { y } = f ( y )$ asadifferential equation on the manifold $\mathcal { M } = \{ y ; I ( y ) = C o n s t \}$ ,forwhich the tangent space is $T _ { y } \mathcal { M } = \{ v ; I ^ { \prime } ( y ) v = 0 \}$ □

The following converse ofCorollary 5.3 isa direct consequence of Theorem 5.2.

Corollary5.4.Consideradifferential equation $\dot { y } = f ( y )$ withareal-analytic first integral $I ( y )$ Ifthenumericalmethod $\varPhi _ { h } ( y )$ is real analytic in $h$ andifevery truncation of themodifiedequation has $I ( y )$ asafirst integral,then thenumerical methodpreserves $I ( y )$ exactly,i.e., $\begin{array} { r } { I ( \varPhi _ { h } ( y ) ) = I ( y ) f o r \ : a l l \ : y . } \end{array}$ □

ProjectionMethods.AlgorithmIV.4.2definesasmooth mapping on the manifold ifthedirection of projection depends smoothly on the position.This is satisfied byorthogonal projection,but is not fulfilled if switching coordinate projectionsare used(asin Example4.3).The symmetric orthogonal projectionmethod ofAlgorithmV.4.1 givesasymmetric method onthemanifoldtowhich Theorem5.1can beapplied.

Methods Based onLocal Coordinates.If the parametrization of the manifold employed inAlgorithmsIV.5.3andV.4.5depends smoothly ontheposition,thenagain Theorem5.1applies.This is thecase for the tangent space parametrization,but not forthe generalized coordinate partitioningconsidered in Sect.IV.5.3.

Corollary5.5(LieGroupMethods).Consideradifferentialequation onamatrix Lie groupG,

$$
{ \dot { Y } } = A ( Y ) Y ,
$$

where $A ( Y )$ is intheassociated Liealgebrag.ALie group integrator $\phi _ { h } : G \to G$ hasthemodifiedequation

$$
\dot { \tilde { Y } } = \big ( A ( \widetilde { Y } ) + h A _ { 2 } ( \widetilde { Y } ) + h ^ { 2 } A _ { 3 } ( \widetilde { Y } ) + . . . \big ) \widetilde { Y }
$$

with $A _ { j } ( Y ) \in { \mathfrak { g } }$ for $Y \in G .$

Proof.Thisisadirect consequenceof Theorem5.1and(IV.6.3),viz., $T _ { Y } G =$ $\{ A Y | A \in { \mathfrak { g } } \}$ □

# IX.5.2 Constrained Hamiltonian Systems

InSect.VI.1 we studied symplectic numerical integrators for constrained Hamiltoniansystems

$$
\begin{array} { l } { \dot { q } = H _ { p } ( p , q ) } \\ { \dot { p } = - H _ { q } ( p , q ) - G ( q ) ^ { T } \lambda } \\ { 0 = g ( q ) . } \end{array}
$$

Assuming theregularity condition(VII.1.13),theLagrange parameter $\lambda = \lambda ( p , q )$ isgivenby(VII.1.12).Thissystemcanbeinterpreted asadifferential equation on themanifold

$$
\mathcal { M } = \{ ( p , q ) | g ( q ) = 0 , G ( q ) H _ { p } ( p , q ) = 0 \} ,
$$

where $G ( q ) = g ^ { \prime } ( q ) .$ Thesymplectic Euler method(VII.1.19)-(VII.1.20),the RAT-TLEscheme(VII.1.26),and theLobattoIA-IIB pair(VII.1.27)-(VII.1.30)were found to be symplectic integrators $\phi _ { h }$ on the manifold $\mathcal { M }$ .

Theorem5.6.Asymplectic integrator $\phi _ { h } : { \mathcal { M } } \to { \mathcal { M } }$ for theconstrained Hamiltoniansystem(5.4) hasamodifiedequationwhich islocallyof theform

$$
\begin{array} { l } { \dot { \tilde { q } } ~ = ~ \tilde { H } _ { p } ( \tilde { p } , \tilde { q } ) } \\ { \dot { \tilde { p } } ~ = ~ - \tilde { H } _ { q } ( \tilde { p } , \tilde { q } ) - G ( \tilde { q } ) ^ { T } \tilde { \lambda } } \\ { 0 ~ = ~ g ( \tilde { q } ) , } \end{array}
$$

where $\bar { \lambda } = \bar { \lambda } ( \widetilde { p } , \widetilde { q } )$ isgivenby(VI.1.12)withHreplacedby $\bar { H }$ and

$$
\widetilde { H } ( p , q ) = H ( p , q ) + h H _ { 2 } ( p , q ) + h ^ { 2 } H _ { 3 } ( p , q ) + \dots .
$$

with $H _ { j } ( p , q )$ satisfying $G ( q ) \nabla _ { p } H _ { j } ( p , q ) = 0 f o r \left( p , q \right) \in \mathcal { M }$ and all j.

Proof.Asexplained in ExampleVII.2.7,a local parametrization $( p , q ) = \chi ( z )$ of themanifold $\mathcal { M }$ transforms(5.4) to the Poissonsystem

$$
\dot { z } = B ( z ) \nabla K ( z )
$$

with $B ( z ) = ( \chi ^ { \prime } ( z ) ^ { T } J \chi ^ { \prime } ( z ) ) ^ { - 1 }$ and $K ( z ) = H ( \chi ( z ) )$ LemmaVII.4.9implies that the numerical method $\Phi _ { h } ( p , q )$ on $\mathcal { M }$ becomes a Poisson integrator $\psi _ { h } ( z )$ for (5.8).By Theorem3.5, $\varPsi _ { h } ( z )$ has the modified equation

$$
\dot { \tilde { z } } = B ( \tilde { z } ) \Big ( \nabla K ( \tilde { z } ) + h _ { 1 } \nabla K _ { 2 } ( \tilde { z } ) + h ^ { 2 } \nabla K _ { 3 } ( \tilde { z } ) + \ldots \Big ) .
$$

Let $\pi$ bea smooth projection onto the manifold $\mathcal { M }$ ,defined ona neighbourhood of $\mathcal { M }$ in $\mathbb { R } ^ { 2 d }$ We then define

$$
H _ { j } ( p , q ) = K _ { j } \left( \chi ^ { - 1 } ( \pi ( p , q ) ) \right) + \mu ( p , q ) ^ { T } G ( q ) \nabla _ { p } H ( p , q )
$$

where we choose $\mu ( p , q )$ such that

$$
G ( q ) \nabla _ { p } H _ { \mathcal { I } } ( p , q ) = 0 \qquad \mathrm { f o r } \quad ( p , q ) \in \mathcal { M } .
$$

Thisis possible because of the regularity assumption (VI.1.13)，and because $G ( q ) \nabla _ { p } H ( p , q ) = 0$ on $\mathcal { M }$ .Thecondition（5.1O）implies that the system(5.6）can beviewed asa differential equation on the original manifold $\mathcal { M }$ Using the same parametrization $( p , q ) = \chi ( z )$ as before shows that (5.6) is equivalent to (5.9).□

Wenote that,due to the arbitrary choice of the projection $\boldsymbol { \mathscr { U } }$ ,the functions $H _ { j } ( p , q )$ of the modified equation are uniquely defined only on $\mathcal { M }$

Global Modified Hamiltonian.Ifwerestrict our considerations to partitioned Runge-Kutta methods,itispossible to find $H _ { j } ( p , q )$ in（5.7）that are globally defined on $\mathcal { M }$ SucharesultisprovedbyReich(1996a）andbyHairer&Wanner （1996)for theconstrained symplectic Euler method and the RATTLE algorithm,and byHairer(2Oo3) for general symplectic partitioned Runge-Kutta schemes.We followthe approach of the latter publication,but present the result only for the important special case of the RATTLE algorithm(VII.1.26).The construction of the $H _ { j } ( p , q )$ is done in the following three steps.

Step $I .$ Symplectic Extensionofthe MethodtoaNeighbourhood oftheManifold. The numerical solution $( p _ { 1 } , q _ { 1 } )$ of(VII.1.26)iswell-defined only forinitial values satisfying $( p _ { 0 } , q _ { 0 } ) \in \mathcal { M }$ However,ifwe replace the condition‘ $g ( q _ { 1 } ) = 0$ ”by

$$
g ( q _ { 1 } ) = g ( q _ { 0 } ) + h G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) ,
$$

and the condition $\ ^ { \cdot } G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) = 0$ ”by

$$
G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) = G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) ,
$$

then the numerical solution is well-defined forall $( p _ { 0 } , q _ { 0 } )$ inan $h$ -independent open neighbourhood of $\mathcal { M }$ (cf.the existence and uniqueness proof of Sect.VII.1.3).Unfortunately,the so-obtained extension of(VII.1.26) is not symplectic.

Inspired by the formula of Lasagni for the generating function of (unconstrained) symplectic Runge-Kutta methods(see Sect.VI.5.2）,we let

$$
\begin{array} { l } { { S ( p _ { \mathrm { 1 } } , q _ { 0 } , h ) ~ = ~ \displaystyle \frac { h } { 2 } \Big ( H ( p _ { \mathrm { 1 / 2 } } , q _ { 0 } ) + H ( p _ { \mathrm { 1 / 2 } } , q _ { \mathrm { 1 } } ) + g ( q _ { 0 } ) ^ { T } \lambda + g ( q _ { \mathrm { 1 } } ) ^ { T } \mu \Big ) ~ ( \frac { \lambda } { 2 } , \lambda ) ~ } } \\ { { ~ - ~ \displaystyle \frac { h ^ { 2 } } { 4 } \Big ( H _ { q } ( p _ { \mathrm { 1 / 2 } } , q _ { \mathrm { 1 } } ) + G ( q _ { \mathrm { 1 } } ) ^ { T } \mu \Big ) ^ { T } \Big ( H _ { p } ( p _ { \mathrm { 1 / 2 } } , q _ { 0 } ) + H _ { p } ( p _ { \mathrm { 1 / 2 } } , q _ { \mathrm { 1 } } ) \Big ) ~ , } } \end{array}
$$

where $p _ { 0 } , p _ { 1 / 2 } , p _ { 1 } , q _ { 0 } , q _ { 1 } , \lambda , \mu$ are the values of the above extension.In the definition(5.13）of the generating function weconsider $p _ { 0 } , p _ { 1 / 2 } , q _ { 1 } , \lambda , \mu$ as functions of

$( p _ { 1 } , q _ { 0 } )$ ,whatispossible because $p _ { 1 } = p _ { 0 } + O ( h )$ With thehelp of $S ( p , q , h )$ we defineanew numerical method onaneighbourhood of $\mathcal { M }$ by

$$
p _ { 0 } = p _ { 1 } + S _ { q } ( p _ { 1 } , q _ { 0 } , h ) , q _ { 1 } = q _ { 0 } + S _ { p } ( p _ { 1 } , q _ { 0 } , h ) .
$$

Thismethod is symplectic by definition,and it also coincideswith the RATTLE algorithm on the manifold $\mathcal { M }$ Usingthe fact that the last expression in(5.13)equals $( p _ { 1 } - p _ { 1 / 2 } ) ^ { I } ( q _ { 1 } - q _ { 0 } )$ ,thisis seen by the same computation asin the proof of Theorem VI.5.4.

Step2.ApplicationoftheResultsofSect.IX.3.2.Thefunction $S ( p _ { 1 } , q _ { 0 } , h )$ of(5.13) can be expanded into powers of $h$ with coefficients depending on $( p _ { 1 } , q _ { 0 } )$ .These coefficient functions are composed of derivatives of $H ( p , q )$ and $g ( q )$ and,consequently,they are globallydefined.For example,the $h$ -coefficient is

$$
S _ { 1 } ( p _ { 1 } , q _ { 0 } ) = H ( p _ { 1 } , q _ { 0 } ) + g ( q _ { 0 } ) ^ { T } \lambda ( p _ { 1 } , q _ { 0 } ) ,
$$

where $\lambda ( p , q )$ is the function defined in(VI.1.12).

Weare thus exactlyin the situation,where we can apply Theorem 3.2.This proves that the method (5.14） hasa modified differential equation with globally defined modified Hamiltonian

$$
\widetilde { H } _ { e x t } ( p , q ) = H _ { 1 } ( p , q ) + h H _ { 2 } ( p , q ) + \dots .
$$

Inparticular,theconstructiveproof of Theorem 3.2shows that $H _ { 1 } ( p , q ) = S _ { 1 } ( p , q )$ with $S _ { 1 } ( p , q )$ from(5.15）.

Step3.BackinterpretationfortheMethod onthe Manifold.SincetheRATTLEalgorithm definesa one-step method on $\mathcal { M }$ ,itfollowsfrom Theorem5.1thatevery truncation of themodified differential equation

$$
\dot { \widetilde { \boldsymbol { p } } } = - \nabla _ { \boldsymbol { q } } \widetilde { H } _ { e x t } ( \widetilde { \boldsymbol { p } } , \widetilde { \boldsymbol { q } } ) , \qquad \dot { \widetilde { \boldsymbol { q } } } = \nabla _ { \boldsymbol { p } } \widetilde { H } _ { e x t } ( \widetilde { \boldsymbol { p } } , \widetilde { \boldsymbol { q } } )
$$

isadifferential equation on the manifold $\mathcal { M }$ Terms of the form $g ( q ) ^ { T } \mu ( p , q )$ in $\bar { H } _ { e x t } ( p , q )$ ,which vanish on $\mathcal { M }$ ,giverise to $- g ( q ) ^ { T } \mu _ { q } ( p , q ) - G ( q ) ^ { T } \mu ( p , q )$ and $g ( q ) ^ { T } \mu _ { p } ( p , q )$ inthevector field of(5.17).On themanifold $\mathcal { M }$ ,where $g ( q ) =$ $_ 0$ ,only the expression $- G ( q ) ^ { T } \underline { { \mu } } ( p , q )$ remains.Consequently,we can arbitrarily remove terms of the form $g ( q ) ^ { T } \mu ( p , q )$ from the functions $H _ { j } ( p , q )$ in (5.16）,if weaddaterm $- G ( q ) ^ { T } \lambda$ in thedifferential equation for $p$ with $\lambda$ defined by the relation $g ( q ) = 0 .$ Thisthen givesaproblemof theform（5.6)with globallydefined $H _ { j } ( p , q )$

# IX.5.3Lie-Poisson Integrators

As inSect.VII.5.5weconsiderasymplectic integrator

$$
( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } ) \qquad \mathrm { o n } \ T ^ { * } G
$$

forthe left-invariant Hamiltoniansystem(VII.5.43)onamatrix Lie group $G$ witha Hamiltonian $H ( P , Q )$ that is quadratic in $P$ Wesuppose that the method preserves theleft-invariance(VII.5.54) so that it inducesa one-step map

$$
Y _ { 1 } = \varPsi _ { h } ( Y _ { 0 } ) \qquad { \mathrm { o n ~ } } \mathfrak { g } ^ { * }
$$

bysetting $Y _ { 1 } = Q _ { 1 } ^ { I } P _ { 1 }$ for $( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } )$ with $Q _ { 0 } ^ { I } P _ { 0 } = Y _ { 0 } .$ Thisisa numerical integrator for thedifferential equation (VII.5.37)on ${ \mathfrak { g } } ^ { * }$ ,and in the coordinates $y = ( y _ { j } )$ with respect to the basis（ $F _ { j }$ ）of ${ \mathfrak { g } } ^ { * }$ this givesamap

$$
y _ { 1 } = \psi _ { h } ( y _ { 0 } ) \qquad \mathrm { o n } ~ \mathbb { R } ^ { d } ,
$$

which isanumerical integrator for theLie-Poissonsystem $\dot { y } = B ( y ) \nabla H ( y )$ with $B ( y )$ given by(VII.5.35）.

Theorem5.7.1f $\varPhi _ { h } ( P , Q )$ isasymplecticandleft-invariant integratorfor(VI.5.43) whichisrealanalyticin $h$ ,thenitsreduction $\psi _ { h } ( y )$ isa Poisson integrator.Moreover, $\psi _ { h } ( Y )$ preserves thecoadjoint orbits,i.e., $\psi _ { h } ( Y ) \in \{ { \mathrm { A d } } _ { U - 1 } ^ { * } Y ; U \in G \} .$

Proof.(a)In the first step one shows,by the standard induction argument as in the proof of Theorem2.3,that themodified equation givenby Theorem5.6,

$$
\begin{array} { l l } { \displaystyle \dot { \tilde { P } } ~ = ~ - \nabla _ { Q } \widetilde { H } ( \widetilde { P } , \widetilde { Q } ) - \sum _ { i = 1 } ^ { m } \widetilde { \lambda } _ { i } \nabla _ { Q } g _ { i } ( \widetilde { Q } ) , \qquad \displaystyle \dot { \widetilde { Q } } = \nabla _ { P } \widetilde { H } ( \widetilde { P } , \widetilde { Q } ) } \\ { \displaystyle 0 ~ = ~ g _ { i } ( \widetilde { Q } ) , \quad i = 1 , \dots , m , } \end{array}
$$

with

$$
\widetilde { H } ( P , Q ) = H ( P , Q ) + h H _ { 2 } ( P , Q ) + h ^ { 2 } H _ { 3 } ( P , Q ) + \dots .
$$

is left-invariant,i.e.,

$$
H _ { j } ( U ^ { T } P , U ^ { - 1 } Q ) = H _ { j } ( P , Q ) \qquad { \mathrm { f o r ~ a l l ~ } } U \in G { \mathrm { ~ a n d ~ a l l ~ } } j .
$$

(b) TheLie-Poisson reduction of Theorem VII.5.8 yields thatif $\left( P ( t ) , Q ( t ) \right) \in$ ${ \bf \nabla } ^ { T } { \bf \Phi } ^ { * } G$ is a solution of the modified system (5.18),then $\boldsymbol { Y } ( t ) = \boldsymbol { Q } ( t ) ^ { T } \boldsymbol { P } ( t ) \in \mathfrak { g } ^ { * }$ solves the differential equation

$$
\langle \dot { \widetilde { Y } } , X \rangle = \langle \widetilde { Y } , [ \widetilde { H } ^ { \prime } ( \widetilde { Y } ) , X ] \rangle \qquad \mathrm { f o r ~ a l l ~ } X \in { \mathfrak { g } } .
$$

Theorem VII.5.6 shows that its solution lies onacoadjoint orbit.By Theorem VI.5.5, (5.20)is equivalent to the Poisson system

$$
\dot { \tilde { y } } = B ( \tilde { y } ) \nabla \tilde { H } ( \tilde { y } ) .
$$

(c)We knowalready from Theorem VII.5.11 that $\psi _ { h } ( y )$ isa Poisson map.Since all truncations of the modified equation (5.21） have the Casimirs as first integrals, their preservation by $\psi _ { h }$ follows fromCorollary5.4.Similarly,thepreservationof thecoadjoint orbits follows from Theorem5.2. □

Incontrast to Theorem 3.5,we here obtaina global modified Hamiltonian in themodified Poissonsystemif the method is obtained by thediscreteLie-Poisson reduction of the RATTLE algorithm;see thepreceding subsection.

# IX.6Modified Equations for Variable Step Sizes

Themodified differential equation of a numerical integrator depends on the step sizeemployed.Therefore,if thestepsizeischangedarbitrarily,adifferent modified equation occursat every step.Thisisthereason for thepoor longtime behaviour observed in Sect.VIII.1.On the other hand,asatisfactory backward erroranalysis ispossible for the variable-step approaches of Sects.VIII.2and VII.3.

Time Transformations.The adaptive approaches of Sect.VII.2 amount to applyinga fixed step sizemethod toa transformed differential equation.Hence,the backward error analysis considered so farapplies directly and yieldsmodified equations forthe transformed problem.These modified equations are Hamiltonian for AlgorithmVIII.2.1 and reversible for method(VII.2.12).

Proportional,Reversible Step Size Controllers.Asin Sect.VII.3.1 we let the step size be of the form

$$
h _ { n + 1 / 2 } = \varepsilon s ( y _ { n } , \varepsilon ) ,
$$

where $\boldsymbol { E }$ isasmall accuracy parameter.It isnot allowed to use information from previous steps.The idea is to work with expansions in powers of the fixed parameter $\succeq$ instead of the step sizes,and to consider the exact solution of the modified equation onavariable grid.The followingdevelopment is givenin Hairer&Stoffer(1997). Itextends the resultsof Sects.IX.1and IX.2 to variable step sizes.

Theorem 6.1.Let $\varPhi _ { h } ( y )$ beasmooth one-stepmethod.

a)Thevariable-stepmethod $y \mapsto \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ hasamodifieddifferential equation

$$
\dot { \widetilde { y } } = f ( \widetilde { y } ) + \varepsilon f _ { 2 } ( \widetilde { y } ) + \varepsilon ^ { 2 } f _ { 3 } ( \widetilde { y } ) + \dots ,
$$

with smooth vector fields $f _ { j } ( y )$ ,such that

$$
\varphi _ { r , \varepsilon s ( y , \varepsilon ) } ( y ) = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) + \mathcal { O } ( \varepsilon ^ { r + 1 } ) ,
$$

where $\varphi _ { r , t } ( y )$ denotestheflow of the truncation of(6.2)after $r$ terms.

b)If themethod is symmetric (i.e., $\varPhi _ { h } ( y ) = \varPhi _ { - h } ^ { - 1 } ( y ) )$ and $s ( \widehat { y } , - \varepsilon ) = s ( y , \varepsilon )$ holdswith $\widehat { y } = \phi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ ,thentheexpansion(6.2)isinevenpowersofe,i.e.,

$$
f _ { j } ( y ) = 0 \qquad f o r \ e v e n \ j .
$$

c)Ifthemethodis $\rho$ -reversible(i.e., $\rho \circ \varPhi _ { h } = \varPhi _ { h } ^ { - 1 } \circ \rho )$ and $s ( \rho ^ { - 1 } \widehat { y } , \varepsilon ) = s ( y , \varepsilon )$ holdswith $\hat { y } = \phi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ thenthemodifiedequation(.2)is $\rho$ -reversible,i.e.,

$$
\rho \circ f _ { j } = - f _ { j } \circ \rho \qquad f o r \mathop { a l l } ~ j .
$$

Proof.a) The modified equation (6.2) isconstructed by Taylor expansion of (6.3) in the same way as(1.1）,using $\varepsilon$ -expansions instead of $h$ -expansions.

For theproof of the statements(b) and(c)we denote,aswe didin Sect.VIII.3, $\varPsi _ { \varepsilon } ( y ) = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ We then compute the dominant errortermin(6.3）and obtain

$$
\psi _ { \varepsilon } ( y ) = \varphi _ { r , \varepsilon s ( y , \varepsilon ) } ( y ) + \varepsilon ^ { r + 1 } s ( y , \varepsilon ) f _ { r + 1 } ( y ) + \mathcal O ( \varepsilon ^ { r + 2 } ) .
$$

With the aim of geting an analogous formula for $\varPsi _ { \varepsilon } ^ { - 1 }$ ,we put $\widehat { y } = \varPsi _ { \varepsilon } ( y )$ and use $\varphi _ { r , t } ^ { - 1 } ( y ) = \varphi _ { r , - t } ( y )$ sothat

$$
y = \varphi _ { r , - \varepsilon s ( y , \bar { \varepsilon } ) } \big ( \widehat { y } - \varepsilon ^ { r + 1 } s ( y , \varepsilon ) f _ { r + 1 } ( y ) + \mathcal { O } ( \varepsilon ^ { r + 2 } ) \big ) .
$$

b)Inserting $s ( y , \varepsilon ) = s ( { \widehat { y } } , - \varepsilon )$ into(6.7）and using the facts that $y = { \hat { y } } + O ( \varepsilon )$ and that the derivative $\varphi _ { r , t } ^ { \prime } ( y )$ is $\mathcal { O } ( t )$ -closetotheidentity,weobtain

$$
\bar { \psi } _ { \varepsilon } ^ { - 1 } ( \widehat { y } ) = y = \varphi _ { r , - \varepsilon s ( \widehat { y } , - \varepsilon ) } ( \widehat { y } ) - \varepsilon ^ { r + 1 } s ( \widehat { y } , 0 ) f _ { r + 1 } ( \widehat { y } ) + { \cal O } ( \varepsilon ^ { r + 2 } ) .
$$

By（VIII.3.3） we have $\varPsi _ { \varepsilon } = \varPsi _ { - \varepsilon } ^ { - 1 } .$ Changing the sign of $\boldsymbol { \varepsilon }$ in(6.8）,acomparisonwith (6.6） proves that $f _ { r + 1 } ( y ) = ( - 1 ) ^ { r } f _ { r + 1 } ( y )$ implying(6.4）.

c）With $s ( y , \varepsilon ) = s ( \rho ^ { - 1 } \widehat { y } , \varepsilon )$ formula(6.7)yields

$$
\bar { \psi } _ { \varepsilon } ^ { - 1 } ( \widehat { y } ) = \varphi _ { \bar { r } , - \varepsilon s ( \bar { \rho } ^ { - 1 } \widehat { y } , \varepsilon ) } ( \widehat { y } ) - \varepsilon ^ { r + 1 } s ( \rho ^ { - 1 } \widehat { y } , 0 ) \widehat { f } _ { r + 1 } ( \widehat { y } ) + { \cal O } ( \varepsilon ^ { r + 2 } ) ,
$$

Byaninduction argument on $r$ we assume that $\rho \circ \varphi _ { r , t } \ = \ \varphi _ { r , - t } \circ \rho$ The $\rho$ reversibility of $\boldsymbol { \Psi } _ { \varepsilon }$ ,i.e., $\rho \circ \varPsi _ { \varepsilon } = \varPsi _ { \varepsilon } ^ { - 1 } \circ \rho$ ,thus implies the statement (6.5). $\sqcap$

Integrating,Reversible Step Size Controllers.We next studya backward error analysisforAlgorithm VII.3.4.Itispossibleto interpret thisalgorithmas the fixed step size method $\hat { \varPhi } _ { \varepsilon }$ of(VIII.3.19) applied to the augmented system(VIII.3.17）and toapply the construction of Sect.IX.1.Thisapproach hasbeen takenin Hairer& Soderlind(2oo4).Inview of anerroranalysis for reversibleintegrable systemsit seems to be more convenient to consider the solution of themodified equation on a variablegrid asitisdonein Theorem6.1.

Letusrecall Algorithm VIII.3.4.Fora given basic integrator $\varPhi _ { h } ( y )$ and a given time transformation $\sigma ( y )$ we denote $G ( y ) = - \big ( \sigma ( y ) \big ) ^ { - 1 } \nabla \sigma ( y ) ^ { T } f ( y )$ and we compute fora given initial value $y _ { 0 }$ andwith $z _ { 0 } = 1 / \sigma ( y _ { 0 } )$

$$
\begin{array} { r c l } { z _ { n + 1 / 2 } } & { = } & { z _ { n } + \varepsilon G ( y _ { n } ) / 2 } \\ { y _ { n + 1 } } & { = } & { \varPhi _ { \varepsilon / z _ { n + 1 / 2 } } ( y _ { n } ) } \\ { z _ { n + 1 } } & { = } & { z _ { n + 1 / 2 } + \varepsilon G ( y _ { n + 1 } ) / 2 . } \end{array}
$$

Thevalues $y _ { n }$ approximate $y ( t _ { n } )$ ,where $t _ { n + 1 } = t _ { n } + \varepsilon / z _ { n + 1 / 2 } .$ We further use the notation

$$
\psi _ { \varepsilon } : { \binom { y _ { n } } { z _ { n } } } \mapsto { \binom { y _ { n + 1 } } { z _ { n + 1 } } } \qquad { \mathrm { a n d } } \qquad { \widehat { \rho } } = { \left( \begin{array} { l l } { \rho } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } .
$$

The step size used in this algorithm is

$$
h _ { \bar { n } + 1 / 2 } = \frac { \varepsilon } { z _ { n + 1 / 2 } } = \varepsilon s ( y _ { n } , z _ { n } , \varepsilon ) ~ \mathrm { w i t h } ~ s ( y , z , \varepsilon ) = \frac { 1 } { z + \varepsilon G ( y ) / 2 } .
$$

Thesymmetricdefinitionof thealgorithm immediatelyyields

$$
\begin{array} { r } { s ( \widehat { y } , \widehat { z } , - \varepsilon ) = s ( y , z , \varepsilon ) \qquad \mathrm { f o r } \qquad ( \widehat { y } , \widehat { z } ) = \varPsi _ { \varepsilon } ( y , z ) . } \end{array}
$$

Fora $\rho$ -reversibledifferential equation $\dot { y } = f ( y )$ and for $\sigma ( y )$ satisfying $\sigma ( \rho ^ { - 1 } y ) =$ $\sigma ( y )$ we have $G ( \rho ^ { - 1 } y ) = - G ( y ) .$ Consequently,the step size function $s ( y , z , \varepsilon )$ of (6.11)also satisfies

$$
\begin{array} { r } {  { \boldsymbol { s } } ( \rho ^ { - 1 } \widehat { \boldsymbol { y } } , \widehat { z } , - \varepsilon ) =  { \boldsymbol { s } } (  { \boldsymbol { y } } , z , \varepsilon ) \qquad \mathrm { f o r } \qquad ( \widehat { \boldsymbol { y } } , \widehat { z } ) = \varPsi _ { \varepsilon } (  { \boldsymbol { y } } , z ) . } \end{array}
$$

With this preparation we are able to formulate the following result.

Theorem 6.2.Let $\varPhi _ { h } ( y )$ bea smooth one-step method, $\sigma ( y )$ a smooth time transformation,and $s ( y , z , \varepsilon )$ thestep sizefunction of(6.11).

a)For the method $\psi _ { \varepsilon }$ of(6.10)thereexistsamodifieddifferentialequation

$$
\begin{array} { r c l } { { \dot { \tilde { y } } } } & { { = } } & { { f ( \widetilde { y } ) + \varepsilon f _ { 2 } ( \widetilde { y } , \widetilde { z } ) + \varepsilon ^ { 2 } f _ { 3 } ( \widetilde { y } , \widetilde { z } ) + \ldots } } \\ { { \dot { \widetilde { z } } } } & { { = } } & { { \widetilde { z } G ( \widetilde { y } ) + \varepsilon G _ { 2 } ( \widetilde { y } , \widetilde { z } ) + \varepsilon ^ { 2 } G _ { 3 } ( \widetilde { y } , \widetilde { z } ) + \ldots , } } \end{array}
$$

with smooth vector felds $f _ { j } ( y , z ) , G _ { j } ( y , z )$ suchthat

$$
\varphi _ { r , \varepsilon s ( y , z , \varepsilon ) } ( y , z ) = \varPsi _ { \varepsilon } ( y , z ) + \mathcal { O } ( \varepsilon ^ { r + 1 } ) ,
$$

where $\varphi _ { r , t } ( y , z )$ denotes theflowofthe truncationofthesystem(6.14)after $r$ terms. b) Ifthe basicmethod issymmetric(i.e., $\varPhi _ { h } ( y ) = \varPhi _ { - h } ^ { - 1 } ( y ) )$ then

$$
f _ { j } ( y ) = 0 \qquad f o r e v e n j .
$$

c)Ifthebasic methodis $\rho$ -reversible(i.e., $\rho \circ \varPhi _ { h } = \varPhi _ { h } ^ { - 1 } \circ \rho ) a n d \sigma ( \rho ^ { - 1 } y ) = \sigma ( y )$ holds,then themodifiedequation(6.14)is $\hat { \rho }$ -reversiblewith $\hat { \rho }$ given by(6.10),i.e.,

$$
\begin{array} { r } { \rho f _ { j } ( y , z ) = - f _ { j } ( \rho y , z ) , \quad G _ { j } ( y , z ) = - G ( \rho y , z ) \qquad f o r \ a l l \ j . } \end{array}
$$

Proof. The proof is the same as for Theorem6.1 and therefore omitted.Notice that the step size function satisfies(6.12)and(6.13)whichare needed in that proof. $\sqsupset$

If the basicmethod is of order $p$ then the coefficient functions of (6.14) satisfy $f _ { j } ( y , z ) = 0$ for $j = 2 , \ldots , p$ Wealways have $G _ { 2 } ( y , z ) = 0$ due to the symmetric way of choosing $z _ { n + 1 / 2 }$ in(6.9).However, $G _ { 3 } ( y , z ) \neq 0$ in general,even if the method $\phi _ { h }$ has an order higher than two.

# IX.7 Rigorous Estimates-Local Error

Whereforeitishighlydesirablethat it beclearlyand rigorously shown whyseriesof thiskind,which at first convergevery rapidlyand then ever moreslowly,andat length divergemoreand more,neverthelessgivea sumclose to the true one if not too many terms are taken,and to what degree such a sum can safely be considered as exact.

(a footnote in Gauss'thesis,1799)

Up to nowwe have considered the modified equation(1.1）asa formal serieswithout taking care of convergence issues.Here,

·we show that already invery simple situations the modified differential equation does not converge;   
·we give bounds on the coefficient functions $f _ { j } ( y )$ of the modified equation (1.1), so that an optimal truncation index can be determined;   
·we estimate the difference between the numerical solution $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ and the exact solution $\widetilde { y } ( h )$ of the truncated modified equation.

Theseestimates will be the basis for rigorous statements concerning the long-time behaviour of numerical solutions.The rigorous estimates of the present section have beengiven inthearticlesBenettin&Giorgilli（1994),Hairer&Lubich（1997）and Reich(1999).Wemainly follow theapproach of Benettin&Giorgilli,but we also use ideas of the other two papers.

Example7.1.We consider the differential equationl $\dot { y } = f ( t )$ , $y ( 0 ) = 0$ ,andwe applythe trapezoidal rule $y _ { 1 } = h \big ( f ( 0 ) + f ( h ) \big ) / 2$ Inthiscase,the numerical solution has an expansion $\Phi _ { h } ( t , y ) = y + h \big ( f ( t ) + f ( t + h ) \big ) / 2 = y + h f ( t ) +$ $h ^ { 2 } f ^ { \prime } ( t ) / 2 + h ^ { 3 } f ^ { \prime \prime } ( t ) / 4 + . . . ,$ so that the modified equation is necessarily of the form

$$
{ \dot { \widetilde { y } } } = f ( t ) + h b _ { 1 } f ^ { \prime } ( t ) + h ^ { 2 } b _ { 2 } f ^ { \prime \prime } ( t ) + h ^ { 3 } b _ { 3 } f ^ { \prime \prime \prime } ( t ) + \dots .
$$

The real coefficients $b _ { k }$ can be computed by putting $f ( t ) ~ = ~ e ^ { t }$ Therelation $\begin{array} { r } { \Phi _ { h } ( t , y ) = \widetilde { y } ( t + h ) } \end{array}$ (with initial value $\widetilde { y } ( t ) = y$ )yieldsafterdivision by $e ^ { t }$

$$
\frac { h } { 2 } \Big ( e ^ { h } + 1 \Big ) = \Big ( 1 + b _ { 1 } h + b _ { 2 } h ^ { 2 } + b _ { 3 } h ^ { 3 } + . . . \Big ) \Big ( e ^ { h } - 1 \Big ) .
$$

This proves that $b _ { 1 } = 0$ ,and $\begin{array} { r } { b _ { k } = B _ { k } / k ! } \end{array}$ ,where $B _ { k }$ arethe Bernoulli numbers（see forexampleHairer&Wanner(1997),Sect.II.1O).Since thesenumbersbehavelike $B _ { k } / k ! \approx C o n s t \cdot ( 2 \pi ) ^ { - k }$ for $k  \infty$ ,theseries(7.1) diverges for all $h \neq 0$ ,as soonas the derivatives of $f ( t )$ grow like $f ^ { ( k ) } ( t ) \approx k ! M R ^ { - k } .$ This is typically the case for analytic functions $f ( t )$ with finite poles.

It is interesting to remark that the relation $\Phi _ { h } ( t , y ) = \widetilde { y } ( t + h )$ is nothing other thantheEuler-MacLaurin summation formula.

Asaparticular example we choose the function

$$
f ( t ) = { \frac { 5 } { 1 + 2 5 t ^ { 2 } } } .
$$

Figure 7.1 shows the numerical solution and the exact solution of the modified equationtruncated atdifferent values of $N$ .For $h = 0 . 2$ ,thereisanexcellentagreement for $N \leq 1 2$ ,whereas oscillations begin toappear from $N = 1 4$ onwards.For the halved step size $h = 0 . 1$ ,theoscillations become visible for $N$ twice as large.

![](images/7e3def14ca5d654289a64e7e8c106d24540f14589becb591f717d0b7383c9833.jpg)  
Fig.7.1.Numerical solution with the trapezoidal rulecompared tothe solution of the truncatedmodified equation for $h = 0 . 2$ (upperfour pictures),and for $h = 0 . 1$ (lowertwo pictures)

Themain ingredient of arigorous backward error analysis isan analyticityassumption on the differential equation $\dot { y } = f ( y )$ and on the method.Throughout this section we assume that $f ( y )$ isanalytic inacomplex neighbourhood of $y _ { 0 }$ and that

$$
\| f ( y ) \| \leq M \qquad { \mathrm { f o r } } \qquad \| y - y _ { 0 } \| \leq 2 R
$$

i.e.,for all $y$ of $B _ { 2 R } ( y _ { 0 } ) : = \{ y \in \mathbb { C } ^ { d } ; \| y - y _ { 0 } \| \le 2 R \}$ Our strategy isthe following:using(7.2) and Cauchy'sestimateswe derive bounds for the coefficient functions $d _ { j } ( y )$ of（1.3）on $B _ { R } ( y _ { 0 } )$ (Sect.IX.7.1), thenwe estimate the functions $f _ { j } ( y )$ of the modified differential equation on $B _ { R / 2 } ( y _ { 0 } )$ (Sect.IX.7.2),and finally wesearch fora suitable truncation for the formal series(1.1）and we prove the closeness of the numerical solution to the exact solution of the truncated modified equation (Sect.IX.7.3).

# IX.7.1Estimation of the Derivatives of the Numerical Solution

If we apply a numerical method to $\begin{array} { r } { \dot { y } = f ( y ) } \end{array}$ with analytic $f ( y )$ ,theexpression $\varPhi _ { h } ( y )$ will usuallybeanalyticinaneighbourhoodof $h = 0$ and $y ~ \in ~ B _ { R } ( y _ { 0 } )$ . Consequently,the coeficients $d _ { j } ( y )$ of the Taylor series expansion

$$
\Phi _ { h } ( y ) = y + h f ( y ) + h ^ { 2 } d _ { 2 } ( y ) + h ^ { 3 } d _ { 3 } ( y ) + \dots
$$

arealso analyticand the functions $d _ { j } ( y )$ can be estimated by theuse of Cauchy's inequalities.Let us demonstrate this forRunge-Kutta methods.

Theorem7.2.ForaRunge-Kutamethod(1.1.4)let

$$
\mu = \sum _ { i = 1 } ^ { s } | b _ { i } | , \qquad \kappa = \operatorname* { m a x } _ { i = 1 , \ldots , s } \sum _ { j = 1 } ^ { s } | a _ { i j } | ,
$$

1f $f ( y )$ is analytic inthe complexball $B _ { 2 R } ( y _ { 0 } )$ andsatisfies(7.2),thenthe coeffcient functions $d _ { j } ( y )$ of(7.3) are analytic in $B _ { R } ( y _ { 0 } )$ and satisfy

$$
\| d _ { j } ( y ) \| \leq \mu M \left( { \frac { 2 \kappa M } { R } } \right) ^ { j - 1 } ~ f o r ~ \| y - y _ { 0 } \| \leq R .
$$

ProofFor $y \in B _ { 3 R / 2 } ( y _ { 0 } )$ and $\| \varDelta y \| \leq 1$ the function $\alpha ( z ) = f ( y + z \Delta y )$ is analytic for $| z | \le R / 2$ and bounded by $M$ Cauchy'sestimate therefore yields

$$
\| f ^ { \prime } ( y ) \Delta y \| = \| \alpha ^ { \prime } ( 0 ) \| \le 2 M / R .
$$

Consequently, $\| f ^ { \prime } ( y ) \| \leq 2 M / R$ for $y \in B _ { 3 R / 2 } ( y _ { 0 } )$ in the operator norm.

nonline For $y \in B _ { R } ( y _ { 0 } )$ $\begin{array} { r } { g _ { i } = y + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( g _ { j } ) } \end{array}$ ,theRunge-Kutta method(II.1.4) requires the solution of the whichcanbesolvedbyfedoin iteration.If $| h | 2 \kappa M / R \le \gamma < 1$ ,itrepresents a contraction on the closed set $\{ ( g _ { 1 } , \dotsc , g _ { s } ) ; \| g _ { i } - y \| \leq R / 2 \}$ and possesses a unique solution.Consequently, themethod is analytic for $| h | \leq \gamma R / ( 2 \kappa M )$ and $y \in B _ { R } ( y _ { 0 } )$ Thisimplies that the functions $d _ { j } ( y )$ of(7.3)are also analytic.Furthermore, $\lVert \phi _ { h } ( y ) - y \rVert \leq | h | \mu M$ for $y \in B _ { R } ( y _ { 0 } )$ so that,again by Cauchy's estimate,

$$
\| d _ { j } ( y ) \| = \frac { 1 } { j ! } \| \frac { d ^ { j } } { d \bar { h } ^ { j } } \Big ( \varPhi _ { h } ( y ) - y \Big ) \| _ { h = 0 } \| \leq \mu M \Big ( \frac { 2 \kappa M } { \gamma R } \Big ) ^ { j - 1 }
$$

for $j \geq 1 ,$ The statement is then obtained by considering the limit $\gamma \to 1$

Due totheconsistencycondition $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } = 1$ ,methods withpositive weights $b _ { i }$ allsatisfy $\mu = 1$ Thevalues $\mu , \kappa$ ofsome classes of Runge-Kutta methodsare givenin Table7.1(those for theGaussmethodsand fortheLobatto IIIA methods have been checked for $s \leq 9$ and $s \leq 5$ ,respectively).

Estimates of the type(7.5),possiblywith a different interpretation of $M$ and $R$ , hold for allone-step methods which are analytic in $h$ and $y$ ,e.g.,partitioned Runge-Kutta methods,spliting and composition methods,projection methods,Lie group methods,....

Table 7.1. The constants $\mu$ and $\kappa$ of formula(7.4)   

<table><tr><td rowspan=1 colspan=1>method</td><td rowspan=1 colspan=1>μ</td><td rowspan=1 colspan=1>K</td><td rowspan=1 colspan=1>method</td><td rowspan=1 colspan=1>从</td><td rowspan=1 colspan=1>K</td></tr><tr><td rowspan=1 colspan=1>explicit Eulerimplicit midpointGauss methods</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>01/2Cs</td><td rowspan=1 colspan=1>implicit Eulertrapezoidal ruleLobatto IIIA</td><td rowspan=1 colspan=1>111</td><td rowspan=1 colspan=1>111</td></tr></table>

# IX.7.2 Estimation of the Coefficients of the Modified Equation

Atthe beginning of this chapter we gave an explicit formula for the first coefficient functions of the modified differential equation (see(1.4)).Using the Lie derivative

$$
( D _ { i } g ) ( y ) = g ^ { \prime } ( y ) f _ { i } ( y )
$$

(cf.(VI.5.2）） and $f _ { 1 } ( y ) : = f ( y )$ ,these formulascan bewritten as

$$
\begin{array} { l } { { f _ { 2 } ( y ) = d _ { 2 } ( y ) \displaystyle - \frac { 1 } { 2 ! } \big ( D _ { 1 } f _ { 1 } \big ) ( y ) } } \\ { { \displaystyle f _ { 3 } ( y ) = d _ { 3 } ( y ) \displaystyle - \frac { 1 } { 3 ! } ( D _ { 1 } ^ { 2 } f _ { 1 } ) ( y ) \displaystyle - \frac { 1 } { 2 ! } \big ( D _ { 2 } f _ { 1 } + D _ { 1 } f _ { 2 } \big ) ( y ) . } } \end{array}
$$

We have the following recurrence relation for the general case.

Lemma7.3.Ifthenumericalmethod hasanexpansionof theform(7.3),then the functions $f _ { j } ( y )$ ofthemodifieddifferentialequation(1.1)satisfy

$$
f _ { j } ( y ) = d _ { j } ( y ) - \sum _ { i = 2 } ^ { j } \frac { 1 } { i ! } \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \Bigl ( D _ { k _ { 1 } } \ldots D _ { k _ { i - 1 } } f _ { k _ { i } } \Bigr ) ( y ) ,
$$

where $k _ { m } \geq 1$ for all $m$ .Observethattheright-handexpressiononly involves $f _ { k } ( y )$ with $k < j$

Proof.The solution of themodified equation(1.1）withinitial value $y ( t ) = y$ can be formally written as (cf.(1.2))

$$
\widetilde { y } ( t + h ) = y + \sum _ { i \geq 1 } \frac { h ^ { i } } { i ! } D ^ { i - 1 } F ( y ) ,
$$

where $F ( y ) = f _ { 1 } ( y ) + h f _ { 2 } ( y ) + h ^ { 2 } f _ { 3 } ( y ) + \dots$ stands for the modified equation,and $h D = h D _ { 1 } + h ^ { 2 } D _ { 2 } + h ^ { 3 } D _ { 3 } + \ldots$ forthe corresponding Lie operator.We expand the formal sums and obtain

$$
\widetilde { y } ( t + h ) = y + \sum _ { i \geq 1 } { \frac { 1 } { i ! } } \sum _ { k _ { 1 } , \ldots , k _ { i } } h ^ { k _ { 1 } + \ldots + k _ { i } } \Big ( D _ { k _ { 1 } } \ldots D _ { k _ { i - 1 } } f _ { k _ { i } } \Big ) ( y ) ,
$$

where all $k _ { m } \geq 1$ .Comparing likepowers of $h$ in(7.3)and（7.7) yields the desired recurrence relations for the functions $f _ { j } \left( y \right)$ □

Toget bounds for $\parallel f _ { j } ( y ) \parallel$ ,we have to estimate repeatedly expressions like $\| ( D _ { i } g ) ( y ) \|$ The following variant ofCauchy's estimatewill be extremely useful.

Lemma7.4.Foranalytic functions $f _ { i } ( y )$ and $g ( y )$ we have for $0 \leq \sigma < \rho$ the estimate

$$
\| D _ { i } g \| _ { \sigma } \leq \frac { 1 } { \rho - \sigma } : \| f _ { i } \| _ { \sigma } \cdot \| g \| _ { \rho } .
$$

Here, $\Vert g \Vert _ { \rho } : = \operatorname* { m a x } \{ \Vert g ( y ) \Vert ; y \in B _ { \rho } ( y _ { 0 } ) \}$ and $\| f _ { i } \| _ { \sigma } , \| D _ { i } g \| _ { \sigma }$ aredefined similarly.

Proof.Forafixed $y \in B _ { \sigma } ( y _ { 0 } )$ the function $\alpha ( z ) = g ( y + z f _ { i } ( y ) )$ isanalytic for $\| z \| \leq \varepsilon : = ( \rho - \sigma ) / M$ with $M : = \| f _ { i } \| _ { \sigma } .$ Since $\alpha ^ { \prime } ( 0 ) = g ^ { \prime } ( y ) f _ { i } ( y ) = ( D _ { i } g ) ( y )$ , weget fromCauchy'sestimate that

$$
\| ( D _ { i } g ) ( y ) \| = \| \alpha ^ { \prime } ( 0 ) \| \leq \frac { 1 } { \varepsilon } \operatorname* { s u p } _ { | z | \leq \varepsilon } \| \alpha ( z ) \| \leq \frac { M } { \rho - \sigma } \cdot \| g \| _ { \rho } .
$$

This proves the statement.

Wearenow able to estimate the coefficients $f _ { j } \left( y \right)$ of the modified differential equation.

Theorem7.5.Let $f ( y )$ beanalytic in $B _ { 2 R } ( y _ { 0 } )$ ,lettheTaylorseriescoeffcientsof thenumericalmethod(7.3) beanalyticin $B _ { R } ( y _ { 0 } )$ andassume that(7.2) and(7.5) aresatisfied.Then,wehavefor thecoeffcientsofthemodifieddifferentialequation

$$
\begin{array} { r l r l } & { \displaystyle \left\| f _ { j } ( y ) \right\| \leq \ln 2 \eta M \bigg ( \frac { \eta M j } { R } \bigg ) ^ { j - 1 } } & & { f o r \qquad \| y - y _ { 0 } \| \leq R / 2 , } \\ & { \eta = 2 \operatorname* { m a x } \big ( \kappa , \mu / ( 2 \ln 2 - 1 ) \big ) . } \end{array}
$$

Proof.We fix anindex,say $J$ ,and we estimate (in the notation ofLemma7.4)

$$
\| f _ { j } \| _ { R - ( j - 1 ) \delta } \qquad \mathrm { ~ f o r ~ } \qquad j = 1 , 2 , \ldots , J ,
$$

where $\delta = R / ( 2 ( J - 1 ) ) .$ This willthenleadtothedesiredestimate for $\| f _ { J } \| _ { R / 2 }$

In the following weabbreviate $\| \cdot \| _ { R - ( j - 1 ) \delta }$ by $\| \cdot \| _ { j } .$ Usingrepeatedly Cauchy's estimate ofLemma7.4weget for $k _ { 1 } + \ldots + k _ { i } = j$ that

$$
\begin{array} { l c l } { \displaystyle \| D _ { k _ { 1 } } . . . D _ { k _ { i - 1 } } f _ { k _ { i } } \| _ { j } } & { \le } & { \displaystyle \frac { 1 } { \delta } \| f _ { k _ { 1 } } \| _ { j } \| D _ { k _ { 2 } } . . . , D _ { k _ { i - 1 } } f _ { k _ { i } } \| _ { j - 1 } } \\ & { \le } & { \displaystyle \operatorname* { s m a x } \le \frac { 1 } { \delta ^ { i - 1 } } \| f _ { k _ { 1 } } \| _ { j } \| f _ { k _ { 2 } } \| _ { j - 1 } . . . . . \cdot \| f _ { k _ { i } } \| _ { j - i + 1 } } \\ & { \le } & { \displaystyle \frac { 1 } { \delta ^ { i - 1 } } \| f _ { k _ { 1 } } \| _ { k _ { 1 } } \| f _ { k _ { 2 } } \| _ { k _ { 2 } } . . . . . \| f _ { k _ { i } } \| _ { k _ { i } } . } \end{array}
$$

The last inequality follows from $\| g \| _ { j } \leq \| g \| _ { l }$ for $l \leq j$ ,which isan immediate consequence of $B _ { R - ( j - 1 ) \delta } ( y _ { 0 } ) \subset B _ { R - ( l - 1 ) \delta } ( y _ { 0 } )$ It therefore follows fromLemma7.3 that

$$
\| f _ { j } \| _ { j } \leq \| d _ { j } \| _ { \bar { j } } + \sum _ { i = 2 } ^ { j } \frac { 1 } { i ! } \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \frac { 1 } { \delta ^ { i - 1 } } \| f _ { k _ { 1 } } \| _ { k _ { 1 } } \| f _ { k _ { 2 } } \| _ { k _ { 2 } } . . . . . . \cdot \| f _ { k _ { i } } \| _ { k _ { i } } .
$$

By induction on $j$ $1 \leq j \leq J$ ）we obtain that $\| f _ { j } \| _ { j } \leq \delta \beta _ { j }$ ,where $\beta _ { j }$ is defined by

$$
\beta _ { j } = \frac { \mu M } { \delta } { \left( \frac { 2 \kappa M } { R } \right) } ^ { j - 1 } + \sum _ { i = 2 } ^ { j } \frac { 1 } { i ! } \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \beta _ { k _ { 1 } } \beta _ { k _ { 2 } } \ldots \ldots \beta _ { k _ { i } } .
$$

![](images/f424a1f5a1052ee93d0623501e4f6f2b02afc9080a32357c0c2380fe4116de86.jpg)  
Fig.7.2.Complex functions of the proof of Theorem $. 5 \ : ( \gamma = q = 1 )$

Observe that $\beta _ { j }$ is defined for all $j \geq 1 .$ Welet $\begin{array} { r } { b ( \zeta ) = \sum _ { j \geq 1 } \beta _ { j } \zeta ^ { \mathcal { I } } } \end{array}$ be its generating functionand we obtain (by multiplying(7.9)with $\zeta ^ { \mathcal { I } }$ and summing over $j \geq 1$ )

$$
b ( \zeta ) = \frac { \gamma \zeta } { 1 - q \zeta } + \sum _ { j \geq 2 } \frac { 1 } { j ! } b ( \zeta ) ^ { j } = \frac { \gamma \zeta } { 1 - q \zeta } + e ^ { b ( \zeta ) } - 1 - b ( \zeta ) ,
$$

where we have used the abbreviations $\gamma : = \mu M / \delta$ and $q : = 2 \kappa M / R$

Whenever $e ^ { b ( \zeta ) } \neq 2$ (i.e., for $\zeta \neq ( 2 b - 1 ) / ( \gamma + q ( 2 b - 1 ) )$ with $b = \ln 2 + 2 k \pi i )$ theimplicit function theorem can be applied to(7,1O).Thisimplies that $b ( \zeta )$ is analytic inadiscwithradius $1 / \nu = ( 2 \ln 2 - 1 ) / ( \gamma + q ( 2 \ln 2 - 1 ) )$ and centre at the origin. On the disc $| \zeta | \le 1 / \nu$ ,the solution $b ( \zeta )$ of（7.10）with $b ( 0 ) = 0$ is bounded by $\ln { 2 }$ .This is seenas follows(Fig.7.2):with the function $w = - \gamma \zeta / ( 1 - q \zeta )$ thedisc $| \zeta | \le 1 / \nu$ ismapped into a disc which,for all possible choices of $\gamma \geq 0$ and $q \geq 0$ ,liesin $| w | \leq 2 \ln 2 - 1$ Theimage of this discunder themapping $b ( w )$ defined by $e ^ { b } - 1 - 2 b = w$ and $b ( 0 ) = 0$ is completely contained in the disc $| b | \leq \ln 2$ Cauchy'sinequalities therefore imply $| \beta _ { j } | \le \ln 2 \cdot \nu ^ { \jmath }$ ,andwe get

$$
\| f _ { J } \| _ { R / 2 } = \| f _ { J } \| _ { J } \leq \delta \beta _ { J } \leq \ln 2 \cdot \delta \cdot \nu ^ { J } .
$$

Since $\nu = q + \gamma / ( 2 \ln 2 - 1 ) \le \eta M J / R$ with $\eta$ given by $\eta = 2 \operatorname* { m a x } ( \kappa , \mu / ( 2 \ln 2 -$ 1))and $\delta \nu \leq \eta M$ ,this proves the statement for $J$ . □

# IX.7.3 Choice of $\mathcal { N }$ and the Estimation of the Local Error

To get rigorous estimates,we truncate the modified differential equation(1.1),and weconsider

$$
\dot { \widetilde { y } } = F _ { N } ( \widetilde { y } ) , \qquad F _ { N } ( \widetilde { y } ) = f ( \widetilde { y } ) + h f _ { 2 } ( \widetilde { y } ) + \ldots + h ^ { N - 1 } f _ { N } ( \widetilde { y } )
$$

![](images/fff567c1caff2c30b73f7b28d0f694196f1d077ece1bc2595ee33096b59968a1.jpg)

with initial value $\bar { y } ( 0 ) = y _ { 0 }$ It is common in the theory of asymptotic expansions to truncate theseries at the index where the corresponding termisminimal.Motivated by the bound(7.8) and by the fact that $( \varepsilon x ) ^ { x }$ admitsaminimum for $x = ( \varepsilon e ) ^ { - 1 }$ (see the picture to the left with $\varepsilon = 0 . 1 5$ ),we suppose that the truncation index $N$ satisfies

$$
h N \leq h _ { 0 } \qquad \mathrm { w i t h } \qquad hslash _ { 0 } = \frac { R } { e \eta M } .
$$

Under thelessrestrictive assumption $\hbar N \leq e h _ { 0 }$ ,theestimates(7.2)and(7.8)imply for $\| y - y _ { 0 } \| \le R / 2$ that

$$
\begin{array} { l } { \displaystyle \| F _ { N } ( y ) \| \le M \bigg ( 1 + \eta \ln 2 \sum _ { j = 2 } ^ { N } \bigg ( \frac { \eta M j h } { R } \bigg ) ^ { j - 1 } \bigg ) } \\ { \le M \bigg ( 1 + \eta \ln 2 \sum _ { j = 2 } ^ { N } \bigg ( \frac { j } { N } \bigg ) ^ { j - 1 } \bigg ) \le M \bigg ( 1 + 1 . 6 5 \eta \bigg ) . } \end{array}
$$

Onecan check that the sumin the lower formula of(7.13) ismaximal for $N = 7$ and bounded by 2.38.Fora pth order method we obtain under the sameassumptions

$$
\| F _ { N } ( y ) - f ( y ) \| \leq c M h ^ { p } ,
$$

where $c$ depends only on the method.

Theorem7.6. Let $f ( y )$ beanalytic in $B _ { 2 R } ( y _ { 0 } )$ ,let the coefficients $d _ { j } ( y )$ ofthe method(7.3）beanalyticin $B _ { R } ( y _ { 0 } )$ andassume that(7.2)and(7.5） hold.If $h \leq$ $h _ { 0 } / 4$ with $h _ { 0 } = R / ( e \eta M )$ then there exists $N = N ( h )$ (namely $N$ equal to the largest integer satisfying $h N \leq h _ { 0 }$ )suchthatthedifferencebetweenthe numerical solution $y _ { 1 } = \phi _ { h } ( y _ { 0 } )$ and the exact solution $\varphi _ { N , t } ( y _ { 0 } )$ of thetruncatedmodified equation(7.11） satisfes

$$
\lVert \Phi _ { h } ( y _ { 0 } ) - \tilde { \varphi } _ { N , h } ( y _ { 0 } ) \rVert \le h \gamma M e ^ { - h _ { 0 } / h } ,
$$

where $\gamma = e ( 2 + 1 . 6 5 \eta + \mu )$ depends only on themethod(we have $5 \leq \eta \leq 5 . 1 8$ and $\gamma \leq 3 1 . 4$ forthemethodsofTable7.1).

Thequotient $L = M / R$ isan upper bound of the first derivative $f ^ { \prime } ( y )$ and can beinterpreted asaLipschitz constant for $f ( y ) .$ The condition $h \leq h _ { 0 } / 4$ istherefore equivalent to $h L \leq C o n s t$ ,where Const depends only on themethod.Because of this condition,Theorem 7.6 requires unreasonably smallstep sizes for the numerical solution of stiff differential equations.

ProofofTheorem7.6.Wefollow here theelegantproof of Benetin $\&$ Giorgilli (1994).It is based on the fact that $\varPhi _ { h } ( y _ { 0 } )$ (asa convergent series(7.3)）and $\varphi _ { N , h } ( y _ { 0 } )$ (asthe solution of an analytic differential equation）are both analytic functions of $h$ . Hence,

$$
g ( h ) : = \varPhi _ { h } ( y _ { 0 } ) - \varphi _ { N , h } ( y _ { 0 } )
$$

is analytic in acomplex neighbourhood of $h = 0$ By definition of the functions $f _ { j } \left( y \right)$ of themodified equation(1.1),thecoeficients of the Taylor series for $\varPhi _ { h } ( y _ { 0 } )$ and $\varphi _ { N , h } ( y _ { 0 } )$ are the same up to the $h ^ { N }$ term,butnot further due to the truncation of the modified equation.Consequently,the function $g ( h )$ contains the factor $h ^ { N + 1 }$ , and the maximum principle for analytic functions,applied to $g ( h ) / h ^ { N + 1 }$ ,implies that

$$
\| g ( h ) \| \leq \left( \frac { h } { \varepsilon } \right) ^ { N + 1 } \operatorname* { m a x } _ { | z | \leq \varepsilon } \| g ( z ) \| \qquad \mathrm { f o r } 0 \leq h \leq \varepsilon ,
$$

if $g ( z )$ isanalytic for $| z | \leq \varepsilon$ We shall show that we can take $\varepsilon = e h _ { 0 } / N$ ,and we compute an upper bound for $\| g ( z ) \|$ by estimating separately $\| \varPhi _ { h } ( y _ { 0 } ) - y _ { 0 } \|$ and $\| \widetilde { \varphi } _ { N , h } ( y _ { 0 } ) - y _ { 0 } \|$

The function $\varPhi _ { z } ( y _ { 0 } )$ is given by the series(7.3） which,due to the bounds of Theorem7.2,converges certainly for $\lvert z \rvert \le R / ( 4 \kappa M )$ ,andthereforealso for $| z | \leq \varepsilon$ (because $2 \kappa \leq \eta$ and $N \geq 4$ ,which isa consequence of $h _ { 0 } / h \ge 4$ .Hence,itis analyticin $| z | \leq \varepsilon$ Moreover,we have from Theorem 7.2 that $\begin{array} { r } { \left\| \bar { \mathcal { P } } _ { z } ( y _ { 0 } ) - y _ { 0 } \right\| \leq } \end{array}$ $\lvert z \rvert M ( 1 + \mu )$ for $| z | \leq \varepsilon$ ：

Because of the bound (7.13） on $F _ { N } ( y )$ ,which isvalid for $y \in B _ { R / 2 } ( y _ { 0 } )$ and for $| h | \leq \varepsilon$ ,wehave $\| \tilde { \varphi } _ { N , z } ( y _ { 0 } ) - y _ { 0 } \| \leq | z | M ( 1 + 1 . 6 5 \eta )$ as longas the solution $\widetilde { \varphi } _ { N , z } ( y _ { 0 } )$ stays in the ball $B _ { R / 2 } ( y _ { 0 } ) .$ Because of $\varepsilon M ( 1 + 1 . 6 5 \eta ) \le R / 2$ ,which isa consequence of the definition of $\boldsymbol { \varepsilon }$ ,of $N \geq 4$ ,andof $( 1 + 1 . 6 5 \eta ) \leq 1 . 8 5 \eta$ (because for consistent methods $\mu \geq 1$ holds and therefore also $\eta \geq 2 / ( 2 \ln 2 - 1 ) \geq 5$ ,this is the case for all $| z | \leq \varepsilon .$ In particular,the solution $\widetilde { \varphi } _ { N , z } ( y _ { 0 } )$ isanalytic in $| z | \leq \varepsilon$ .

Inserting $\varepsilon = e h _ { 0 } / N$ and the bound on $\| g ( z ) \| \leq \| \varPhi _ { z } ( y _ { 0 } ) - y _ { 0 } \| + \| \widetilde { \varphi } _ { N , z } ( y _ { 0 } ) -$ $y _ { 0 } \|$ into （7.16)yields （with $C = 2 + 1 . 6 5 \eta + \mu )$

$$
\| g ( h ) \| \leq \varepsilon M C { \biggl ( } { \frac { h } { \varepsilon } } { \biggr ) } ^ { N + 1 } { \leq } h M C { \biggl ( } { \frac { h } { \varepsilon } } { \biggr ) } ^ { N } = h M C { \biggl ( } { \frac { h N } { e h _ { 0 } } } { \biggr ) } ^ { N } \leq h M C e ^ { - N }
$$

because $h N \leq h _ { 0 }$ .The statement now follows from the fact that $N \leq h _ { 0 } / h <$ $N + 1$ ,sothat ≤e.e-h/h □

Adifferent approach toa rigorous backward erroranalysis is developed by Moan (2005).There,the modified differential equation contains an exponentially small time-dependent perturbation,but its flow reproduces the numerical solution without error.

# IX.8 Long-Time Energy Conservation

In particular,one easily explainsin thisway why symplectic algorithms giverise toagood energy conservation,with essentially no accumulation of errors in time. （G.Benettin&A.Giorgilli1994）

Asafirst application of Theorem 7.6we study the long-time energy conservation of symplectic numerical schemesapplied to Hamiltonian systems $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) . } \end{array}$ It follows from Theorem 3.1 that the correspondingmodified differential equation is also Hamiltonian.After truncation we thus get a modified Hamiltonian

$$
\widetilde { H } ( y ) = H ( y ) + h ^ { p } H _ { p + 1 } ( y ) + \ldots + h ^ { N - 1 } H _ { N } ( y ) ,
$$

which we assume to be defined on the same open set as the original Hamiltonian $H$ seeTheorem3.2and Sect.IX.4.Wealsoassume that thenumericalmethod satisfies theanalyticitybounds (7.5),so that Theorem 7.6canbeapplied.The following result is given by Benettin&Giorgilli（1994).

Theorem8.1.Considera Hamiltoniansystemwithanalytic $H : D  \mathbb { R }$ (where $D \subset \mathbb { R } ^ { 2 d }$ )andapplya symplecticnumerical method $\varPhi _ { h } ( y )$ with step size $h .$ If thenumerical solution staysinthe compact set $K \subset D$ ,thenthereexist $h _ { 0 }$ and $N = N ( h )$ (asinTheorem7.6）such that

$$
\begin{array} { l } { { { \widetilde { \cal H } ( y _ { n } ) ~ = ~ { \widetilde { \cal H } ( y _ { 0 } ) + \mathcal O ( e ^ { - h _ { 0 } / 2 h } ) } ~ } } } \\ { { { \cal H } ( y _ { n } ) ~ = ~ { \cal H } ( y _ { 0 } ) + \mathcal { O } ( h ^ { p } ) } } \end{array}
$$

overexponentially long time intervalsnh≤eho/2h.

ProofWe let $\widetilde { \varphi } _ { N , t } ( y _ { 0 } )$ bethe flow of the truncated modified equation.Since this differential equation is Hamiltonian with $\tilde { H }$ of(8.1), $\widetilde { H } \big ( \widetilde { \varphi } _ { N , t } ( y _ { 0 } ) \big ) = \widetilde { H } \big ( y _ { 0 } \big )$ holds forall timest.FromTheorem7.6weknow that $\lVert y _ { n + 1 } - \widetilde { \varphi } _ { N , h } ( y _ { n } ) \rVert \leq h \gamma M e ^ { - h _ { 0 } / h }$ and,byusinga global $h$ -independent Lipschitz constant for $\tilde { H }$ (which exists by Theorem 7.5），we also get $\tilde { H } ( y _ { n + 1 } ) - \tilde { H } ( \tilde { \varphi } _ { N , h } ( y _ { n } ) ) = \mathcal { O } ( h e ^ { - h _ { 0 } / h } )$ From the identity

$$
\widetilde { H } ( y _ { n } ) - \widetilde { H } ( y _ { 0 } ) = \sum _ { j = 1 } ^ { n } \Bigl ( \widetilde { H } ( y _ { j } ) - \widetilde { H } ( y _ { j - 1 } ) \Bigr ) = \sum _ { j = 1 } ^ { n } \Bigl ( \widetilde { H } ( y _ { j } ) - \widetilde { H } \bigl ( \widetilde { \varphi } _ { N , h } ( y _ { j - 1 } ) \bigr ) \Bigr ) .
$$

we thus get $\widetilde { H } ( y _ { n } ) - \widetilde { H } ( y _ { 0 } ) = \mathcal { O } ( n h e ^ { - h _ { 0 } / h } )$ ,and the statement on the long-time conservation of $\bar { H }$ isanimmediate consequence.The statement fortheHamiltonian $H$ follows from (8.1),because $H _ { p + 1 } ( y ) + h H _ { p + 2 } ( y ) + \ldots + h ^ { N - p - 1 } H _ { N } ( y )$ is uniformly bounded on $K$ independently of $h$ and $N$ Thisfollows from the proofof Lemma VI.2.7and from the estimates of Theorem 7.5. □

Example 8.2.Let us check explicitly the assumptions of Theorem 8.1 for the pendulum problem ${ \dot { q } } = p$ ， $\dot { p } = - \sin q$ Thevector field $f ( p , q ) = ( p , - \sin q ) ^ { T }$ isalso well-defined forcomplex $p$ and $q$ ,and it isanalytic everywhere on $\mathbb { C } ^ { 2 }$ Welet $K$ be acompact subsetof{p,q）∈R²；|p|≤c}.Asaconsequenceof|sinq|≤elImql, we get the bound

$$
\| f ( p , q ) \| \leq \sqrt { c ^ { 2 } + 4 R ^ { 2 } + e ^ { 2 R } }
$$

for $\| ( p , q ) - ( p _ { 0 } , q _ { 0 } ) \| \leq 2 R$ and $( p _ { 0 } , q _ { 0 } ) \in K$ Ifwe choose $c \leq 2 , R = 1$ , and $M = 4$ ,thevalue $h _ { 0 }$ of Theorem 7.6is given by $h _ { 0 } = 1 / 4 e \eta \approx 0 . 0 1 8$ for the methods of Table 7.1.For step sizes that are smaller than $h _ { 0 } / 2 0$ ,Theorem8.1 guarantees that the numerical Hamiltonian iswell conserved on intervals $[ 0 , T ]$ with $T \approx e ^ { 1 0 } \approx 2 \cdot 1 0 ^ { 4 }$ .

Thenumerical experiment of Fig.8.1 shows that the estimates for $h _ { 0 }$ areoften too pessimistic.We have drawn 2Oo ooo steps of the numerical solution of the implicit midpoint rule for various step sizes $h$ and for initial values $( p _ { 0 } , q _ { 0 } ) =$ $( 0 , - 1 . 5 )$ , $( p _ { 0 } , q _ { 0 } ) = ( 0 , - 2 . 5 )$ , $( p _ { 0 } , q _ { 0 } ) = ( 1 . 5 , - \pi )$ ,and $( p _ { 0 } , q _ { 0 } ) = ( 2 . 5 , - \pi )$ Theyarecompared tothecontourlines of thetruncated modified Hamiltonian

![](images/b77e833418e3ee46a401d813fc71a8af839479222a2d293b6a1a371801dc4c05.jpg)  
Fig.8.1.Numerical solutions ofthe implicit midpoint rule with large step sizes

$$
\widetilde { H } ( p , q ) = \frac { p ^ { 2 } } { 2 } - \cos q + \frac { h ^ { 2 } } { 4 8 } \Big ( \cos ( 2 q ) - 2 p ^ { 2 } \cos q \Big ) .
$$

This shows that for step sizes as large as $h \leq 0 . 7$ theHamiltonian $\bar { H }$ isextremely well conserved.Beyond thisvalue,thedynamics of the numerical method soon turnsintochaoticbehaviour(see also Yoshida(1993)andHairer,Nprsett&Wanner (1993),page 336).

Theorem 8.1 explains the near conservation of the Hamiltonian with the symplectic Eulermethod,the implicit midpointruleand the Stormer-Verletmethod as observedin thenumerical experiments of Chap.I:in Fig.I.1.4 for thependulum problem,inFig.I.2.3for theKeplerproblem,andinFig.I.4.1forthefrozenargon crystal.

Thelinear drift of the numerical Hamiltonian for non-symplectic methods can beexplainedbyacomputation similarto thatof theproofofTheorem8.1.Froma Lipschitz condition of the Hamiltonian and from the standard local error estimate, we obtain $H ( y _ { n + 1 } ) - H ( \varphi _ { h } ( y _ { n } ) ) = \mathcal { O } ( h ^ { p + 1 } )$ Since $H ( \varphi _ { h } ( y _ { n } ) ) \ : = \ : H ( y _ { n } )$ ,a summation of these terms leads to

$$
H ( y _ { n } ) - H ( y _ { 0 } ) = \mathcal { O } ( t h ^ { p } ) \qquad { \mathrm { f o r ~ } } t = n h .
$$

This explains the linear growth in the error of the Hamiltonian observed in Fig.I.2.3 andinFig.I.4.1for theexplicitEulermethod.

# IX.9Modified Equation in Terms of Trees

By Theorem III.1.4 the numerical solution $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ ofaRunge-Kutta method can bewritten asaB-series

$$
\begin{array} { r } { \Phi _ { h } ( y ) = y + h f ( y ) + h ^ { 2 } a ( \hat { \mathcal { J } } ) ( f ^ { \prime } f ) ( y ) \ ~ } \\ { + \ h ^ { 3 } \Big ( \frac { 1 } { 2 } a ( \hat { \mathbb { V } } ) f ^ { \prime \prime } ( f , f ) ( y ) + a ( \hat { \mathcal { J } } ) f ^ { \prime } f ^ { \prime } f ( y ) \Big ) + \ldots \ . } \end{array}
$$

Forconsistent methods,i.e.,methods of orderat least1,we always have $a ( \bullet ) = 1$ , so that the coefficient of $h$ isequal to $f ( y )$ .In this section we exploit this special structure of $\varPhi _ { h } ( y )$ inorder to get practical formulas for the coeficient functions of themodified differential equation.Using(9.1） instead of(1.3),the equations(1.4) yield

$$
\begin{array} { l l l } { { f _ { 2 } ( y ) ~ = ~ \left( a ( \underline { { { f } } } ) - \frac { 1 } { 2 } \right) ( f ^ { \prime } f ) ( y ) } } \\ { { f _ { 3 } ( y ) ~ = ~ \frac { 1 } { 2 } \Big ( a ( \underline { { { \sf Y } } } ) - a ( \underline { { { f } } } ) + \frac { 1 } { 6 } \Big ) f ^ { \prime \prime } ( f _ { * } f ) ( y ) } } \\ { { ~ + ~ \left( a ( \underline { { { \sf Y } } } ) - a ( \underline { { { \sf Y } } } ) + \frac { 1 } { 3 } \right) f ^ { \prime } f ^ { \prime } f ( y ) . } } \end{array}
$$

Continuing thiscomputation,one is quicklyconvinced of the general formula

$$
f _ { j } ( y ) = \sum _ { | \tau | = j } { \frac { b ( \tau ) } { \sigma ( \tau ) } } F ( \tau ) ( y ) ,
$$

so that themodified equation（1.1） becomes

$$
\dot { \widetilde { y } } = \sum _ { \tau \in T } \frac { h ^ { | \tau | - 1 } } { \sigma ( \tau ) } b ( \tau ) F ( \tau ) ( \widetilde { y } )
$$

with $b ( \bullet ) = 1$ , $b ( \ b { \mathscr { f } } ) = a ( \ b { \mathscr { f } } ) - \frac { 1 } { 2 }$ ,etc.Since the coefficients $\sigma ( \tau )$ areknown from Definition II.1.7,all we have todois to find suitable recursion formulas for thereal coefficients $b ( \tau )$ .

# IX.9.1B-Series of the Modified Equation

Recurrence formulas for the coefficients $b ( \tau )$ in（9.4）were first given by Hairer （1994）andby Calvo,Murua& Sanz-Serna（1994).We follow here theapproach ofHairer (1999),which uses the Lie-derivative of B-series and thus simplifies the construction of the coefficients.

Wemakeuse of the notion of ordered trees introduced in Sect.III.1.3.Fora given tree $\tau$ wedefine the set of all splittingsas

$$
S P ( \tau ) = \big \{ \theta \in O S T ( \tau ) ; \tau \ \wedge \mathrm { \ t \ s o n s i s t s \ o f \ o n l y \ o n e \ e l e m e n t } \big \} .
$$

Here, $O S T ( \tau ) = O S T ( \omega ( \tau ) )$ is the set of ordered subtrees as defined in (III.1.33).

Lemma9.1 (Lie-Derivative ofB-series).Let $b ( \tau )$ (with $b ( \emptyset ) = 0$ )and $c ( \tau )$ be thecoefficients of two $B$ -series,and let $y ( t )$ beaformal solution ofthedifferentialequation $h \dot { y } ( t ) = B \big ( b , y ( t ) \big ) .$ TheLiederivative of thefunction $B ( c , y )$ with respecttothevectorfield $B ( b , y )$ isagain $\boldsymbol { a }$ $B$ -series

$$
h \frac { d } { d t } B \big ( c , y ( t ) \big ) = B \big ( \partial _ { b } c , y ( t ) \big ) .
$$

Its coefficients are given by $\partial _ { b } c ( \emptyset ) = 0$ and for $| \tau | \geq 1$ by

![](images/4d5387dcd1df94b3faeaf84caa4aeb30b3be37c18b782a0bb55c79a345ba03c3.jpg)  
Fig.9.1.Splitting ofan ordered tree $\omega$ intoasubtree $\theta$ and $\{ \delta \} = \omega \backslash \theta$

Proof.For theproof ofthis lemma itis convenient towork with ordered trees $\omega \in$ $O I .$ Since $\nu ( \tau )$ of(III.1.31） denotes the number of possible orderings ofa tree $\tau \in { \mathcal { I } }$ ,asum $\textstyle \sum _ { \tau \in T } \cdot / .$ becomes $\begin{array} { r } { \sum _ { \omega \in O T } \nu ( \omega ) ^ { - 1 } \cdot / \cdot } \end{array}$

For the computation of the Lie derivative of $B ( c , y )$ we have to differentiate theelementary differential $F ( \theta ) \left( y ( t ) \right)$ with respect to $t$ UsingLeibniz'rule,this yields $| \theta |$ terms,one for every vertex of $\theta$ Thenwe insert the series $B \left( b , y ( t ) \right)$ for $h \dot { y } ( t )$ Thismeans that allthe trees $\delta$ appearing in $B \left( b , y ( t ) \right)$ areattached witha newbranch to the distinguished vertex.Written out as formulas,this gives

$$
h \frac { d } { d t } { \cal B } ( c , y ( t ) ) = \sum _ { \theta \in O N \cup \{ \theta \} } \frac { h ^ { | \theta | } c ( \theta ) } { \nu ( \theta ) \sigma ( \theta ) } \sum _ { \gamma } \sum _ { \delta \in O T } \frac { h ^ { | \delta | } b ( \delta ) } { \nu ( \delta ) \sigma ( \delta ) } F ( \theta \circ _ { \gamma } \delta ) \bigl ( y ( t ) \bigr ) ,
$$

where $\sum \gamma$ isa sum over all vertices of $\theta$ ,and $\theta \circ _ { \gamma } \delta$ isthe ordered tree obtained whenattaching the root of $\delta$ witha new branch to $\gamma$ (seeFig.9.1).We choose one of the $n ( \gamma ) + 1$ possibilities of doing this,where $n ( \gamma )$ denotes the number of upwards leaving branches of $\theta$ at thevertex $\gamma$ Wenow collectthe termswith equal ordered tree $\omega = \theta \circ _ { \gamma } \delta$ ,and notice that $\nu ( \theta ) \sigma ( \theta ) = \kappa ( \theta )$ with $\kappa ( \theta )$ given by(III.1.32).This gives

$$
h \frac { d } { d t } B \big ( c , y ( t ) \big ) = \sum _ { \omega \in \mathcal { O } T } h ^ { | \omega | } \Big ( \sum _ { \theta \circ _ { \gamma } \delta = \omega } \frac { c ( \theta ) b ( \delta ) } { \big ( n ( \gamma ) + 1 \big ) \kappa ( \theta ) \kappa ( \delta ) } \Big ) F ( \omega ) \big ( y ( t ) \big ) ,
$$

where $\sum \theta \circ _ { \gamma } \delta = \omega$ is over all triplets $( \theta , \gamma , \delta )$ such that $\theta \circ _ { \gamma } \delta = \omega .$ Because of $\kappa ( \omega ) =$ $\kappa ( \theta ) \kappa ( \delta ) ( n ( \gamma ) + 1 )$ ,we obtain

![](images/b2bcecd2c7a78998654b60a36c459877b1e88124c914cdc09d2928e3f3655272.jpg)  
Fig.9.2.Illustration of the formula(9.6) foran ordered tree with5vertices

$$
\begin{array} { r l r } {  { h \frac { d } { d t } B \bigl ( c , y ( t ) \bigr ) \ = \ \sum _ { \omega \in O T } \frac { h ^ { | \omega | } } { \kappa ( \omega ) } \Bigl ( \sum _ { \theta \circ _ { \gamma } \delta = \omega } c ( \theta ) b ( \delta ) \Bigr ) F ( \omega ) \bigl ( y ( t ) \bigr ) } } \\ & { } & { \ = \ \sum _ { \tau \in T } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } \Bigl ( \sum _ { \theta \in S P ( \tau ) } c ( \theta ) b ( \tau \setminus \theta ) \Bigr ) F ( \tau ) \bigl ( y ( t ) \bigr ) , } \end{array}
$$

which proves the statement.

Letusillustrate this proof and the formula (9.6)with an ordered tree having5vertices.All possible splittings $\omega ~ = ~ \theta ~ \circ _ { \gamma } ~ \partial$ aregiven in Fig.9.2.Notice that $\theta$ maybe the emptytree $\emptyset$ ,and thatalways $| \delta | \geq 1$ We see that the tree $\boldsymbol { \omega }$ isobtained in several ways:(i） differentiation of $F ( \varnothing ) ( y ) \ = \ y$ andadding $F ( \omega ) ( y )$ asargument,(ii）differentiation of the factor corresponding to theroot in $F ( \theta ) ( y ) = f ^ { \prime \prime } ( f , f ) ( y )$ andadding $F ( \tilde { \mathcal { J } } ) ( y ) = ( f ^ { \prime } f ) ( y )$ ,(iii)differentiation ofall $f$ 'sin $F ( \theta ) ( y ) = f ^ { \prime \prime \prime } ( f , f , f ) ( y )$ andadding $F ( \bullet ) ( y ) = f ( y )$ ,andfinally, (iv)differentiation of the factor for the root in $F ( \theta ) ( y ) = f ^ { \prime \prime } ( f ^ { \prime } f , f ) ( y )$ andadding $F ( \bullet ) ( y ) = f ( y ) .$ This proves that

$$
\partial _ { b } c ( \dot { \pmb { \psi } } ) = c ( \emptyset ) b ( \dot { \pmb { \psi } } ) + c ( \pmb { \psi } ) b ( \pmb { \updownarrow } ) + c ( \pmb { \psi } ) b ( \bullet ) + 2 c ( \pmb { \updownarrow } ) b ( \bullet ) .
$$

Forthe trees up to order 3the formulas for $\partial _ { b } c$ are:

$$
\begin{array} { r c l } { { \partial _ { b } c ( \bullet ) } } & { { = } } & { { c ( \emptyset ) b ( \bullet ) } } \\ { { \partial _ { b } c ( \pmb { \mathring { \mathbf { \Psi } } } ) } } & { { = } } & { { c ( \emptyset ) b ( \pmb { \mathring { \mathbf { \Psi } } } ^ { \prime } ) + c ( \bullet ) b ( \bullet ) } } \\ { { \partial _ { b } c ( \pmb { \Psi } ) } } & { { = } } & { { c ( \emptyset ) b ( \pmb { \Psi } ) + 2 c ( \pmb { \mathring { \mathbf { \Psi } } } ^ { \prime } ) b ( \bullet ) } } \\ { { \partial _ { b } c ( \pmb { \mathring { \mathbf { \Psi } } } ) } } & { { = } } & { { c ( \emptyset ) b ( \pmb { \mathring { \mathbf { \Psi } } } ) + c ( \bullet ) b ( \pmb { \mathring { \mathbf { \Psi } } } ) + c ( \pmb { \mathring { \mathbf { \Psi } } } ) b ( \bullet ) . } } \end{array}
$$

Theabove lemma permitsus to get recursion formulas for the coefficients $b ( \tau )$ of themodified differential equation(9.4).

Theorem9.2.Ifthemethod $\varPhi _ { h } ( y )$ isgivenby(9.1),thefunctions $f _ { j } ( y )$ ofthemodifieddifferentialequation(1.1) satisfy(9.3),wherethereal coefficients $b ( \tau )$ arerecursively defined by $b ( \emptyset ) = 0$ ， $b ( \cdot ) = 1$ and

$$
b ( \tau ) = a ( \tau ) - \sum _ { j = 2 } ^ { | \tau | } \frac 1 { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) .
$$

Here, $\partial _ { b } ^ { \jmath - 1 }$ isthe $( j - 1 )$ -thiterateoftheLie-derivative $\partial _ { b }$ defined in Lemma 9.1.

Proof.Theright-hand side of the modified equation(9.4)is theB-series $B \left( b , \widetilde { y } ( t ) \right)$ dividedby $h .$ Itthereforefollows froman iterativeapplication ofLemma 9.1 that

$$
h ^ { j } \widetilde { y } ^ { ( j ) } ( t ) = B \big ( \partial _ { b } ^ { j - 1 } b , \widetilde { y } ( t ) \big ) ,
$$

so that by Taylor series expansion $\begin{array} { r } { \widetilde { y } ( t + h ) = y + B \left( \sum _ { j \geq 1 } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b , y \right) , } \end{array}$ where $y : = y ( t )$ Sincewehavetodetermine thecoeffcients $b ( \tau )$ insuchaway that $\tilde { y } ( t + h ) \ = \ \varPhi _ { h } ( y ) \ = \ B ( a , y ) ,$ acomparison of the two B-seriesgives $\begin{array} { r } { \sum _ { j \ge 1 } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) = a ( \tau ) \ } \end{array}$ Thisprovesthesatementecuse $\partial _ { b } ^ { 0 } b ( \tau ) ~ = ~ b ( \tau )$ for $\tau \in T$ ,and $\partial _ { b } ^ { \jmath - 1 } b ( \tau ) = 0$ for $j > | \tau |$ (asaconsequence of $b ( \emptyset ) = 0$ ).

We present in Table 9.1 the formula (9.7) for trees up to order 3.

Table9.1.Examples of formula (9.7)   

<table><tr><td>T=·</td><td>b(）=a（）</td></tr><tr><td>T=！</td><td>b（）=a（）-b（）²</td></tr><tr><td>T=Y</td><td>b（Y）=a（Y）-b（）6（）-b（）³</td></tr><tr><td>T=1</td><td>b(）=a(）-（）6(）-b(）</td></tr></table>

We next consider the case whena symplectic method is applied toa Hamiltonian system $\dot { y } = J ^ { - 1 } \nabla H ( y )$ ItfollowsfromTheorem3.1thatthemodifiedequation is againHamiltonian.What does this imply for the coefficientsof(9.4)?

Theorem9.3.Suppose thatforall Hamiltonians $H ( y )$ themodified vectorfeld (9.4),truncatedafter anarbitrarypowerof $h ,$ is(locally) Hamiltonian.Then,

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \qquad f o r a l l \quad u , v \in T .
$$

Proof.Let $\varphi _ { N , t } ( y _ { 0 } )$ bethe flow of the modified differential equation(9.4),truncated after the $h ^ { N - 1 }$ terms. It is symplectic for all $t$ ,and in particular for $t = \hbar$ . Asaconsequence of theproof of Theorem 9.2we obtain that $\varphi _ { N , h } ( y _ { 0 } )$ isasymplectic B-series $B \left( a _ { N } , y _ { 0 } \right) .$ The coefficients $a _ { N } ( \tau )$ aregiven by（9.7）,where $b ( \tau )$ isreplaced with O for $| \tau | > N .$ For $u , v \in T$ with $| u | + | v | = N$ we therefore have

$$
b ( u \circ v ) = a _ { N } ( u \circ v ) - a _ { N - 1 } ( u \circ v ) .
$$

Since $a _ { N } ( \tau ) = a _ { N - 1 } ( \tau )$ for $| \tau | < N$ ,formula (9.8) is an immediate consequence of Theorem VI.7.6. □

Remark 9.4.Let $G = \{ a : T \to \mathbb { R } \mid a ( \emptyset ) = 1 \}$ be the Butcher group (see Sect.I.1.5),and consider the mapping $S : G  \mathbb { R }$ defined by

$$
S ( a ) = a ( u \circ v ) + a ( v \circ u ) - a ( u ) \cdot a ( v ) .
$$

If we denote by $e \in G$ the element corresponding to the identity (i.e., $e ( \emptyset ) = 1$ and $e ( \tau ) = 0$ for $| \tau | \geq 1$ ),we have for itsderivative

$$
S ^ { \prime } ( e ) b = b ( u \circ v ) + b ( v \circ u ) .
$$

Hence,coefficient mappings $b ( \tau )$ satisfying（9.8）liein the tangent space at $e ( \tau )$ of thesymplectic subgroup of $G$ (i.e., $a \in G$ satisfying(VI.7.4)).Thisisin complete analogy tothe fact that Hamiltonian vector fields can be considered as elements of thetangent space at the identity of the group of symplectic diffeomorphisms (see also Exercises 15 and 16).

# IX.9.2 Elementary Hamiltonians

If the modified differential equation(9.4） isHamiltonian,canwe find explicit formulas for $\begin{array} { r } { H ( y ) ? } \end{array}$ Letus startwith an easy example,the implicit midpoint rule.Writtenasa B-series(9.1),its coefficients are $a ( \tau ) = 2 ^ { 1 - | \tau | }$ (cf.Exercise 8）so that the first coefficient functions (9.2) of the modified equation satisfy $f _ { 2 } ( y ) = 0$ and

$$
f _ { 3 } ( y ) = \frac { 1 } { 2 4 } \Big ( 2 ( f ^ { \prime } f ^ { \prime } f ) ( y ) = f ^ { \prime \prime } ( f , f ) ( y ) \Big ) .
$$

Since $f ( y ) = J ^ { - 1 } \nabla H ( y )$ ,differentiation of

$$
H _ { 3 } ( y ) = - \frac { 1 } { 2 4 } H ^ { \prime \prime } ( y ) \Bigl ( \bar { J } ^ { - 1 } \nabla H ( y ) , \bar { J } ^ { - 1 } \nabla H ( y ) \Bigr )
$$

shows that $f _ { 3 } ( y ) = J ^ { - 1 } \nabla H _ { 3 } ( y )$ ,and we have found an explicit expression of the Hamiltonian corresponding to the vector field $f _ { 3 } ( y )$ It isrecommended to compute also $f _ { 5 } ( y )$ and to try to find $H _ { 5 } ( y )$ such that $f _ { 5 } ( y ) = J ^ { - 1 } \nabla H _ { 5 } ( y )$ Such computations lead to expressions that have been introduced ina different context by Sanz-Serna&Abia(1991).Theycall themcanonical elementarydifferentials.

Definition 9.5 (Elementary Hamiltonians).For a given smooth function $H :$ $D  \mathbb { R }$ （with open $D \subset \mathbb { R } ^ { 2 d }$ ）and for $\tau \in T$ wedefine the elementary Hamiltonian $H ( \tau ) : D  \mathbb { R }$ by

$$
H ( \bullet ) ( y ) = H ( y ) , \qquad H ( \tau ) ( y ) = H ^ { ( m ) } ( y ) \bigl ( F ( \tau _ { 1 } ) ( y ) , \ldots , F ( \tau _ { m } ) ( y ) \bigr )
$$

for $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } ]$ Here, $F ( \tau _ { i } ) ( y )$ areelementary differentials corresponding to $f ( y ) = J ^ { - 1 } \nabla H ( y )$

The expression in(9.1O)is nothing else than the elementary Hamiltonian correspondingto the tree Y.Our aimistoprove that,forsymplectic methodsapplied toHamiltonian systems,the coefficient functions(9.3)of the modified differential equation satisfy $f _ { j } ( y ) = J ^ { - 1 } \nabla H _ { j } ( y )$ ,where $H _ { j } ( y )$ isa linear combination of elementary Hamiltonians.

Lemma9.6.Elementary Hamiltonians satisfy

$$
H ( u \circ v ) ( y ) + H ( v \circ u ) ( y ) = 0 \qquad f o r \ : a l l \ : \ : u , v \in T .
$$

In particular,we have $H ( u \circ u ) ( y ) = 0$ forall $u \in T$ .

Proof.This follows immediately fromthe fact thatfor $u = [ u _ { 1 } , \ldots , u _ { m } ] \in \textit { T }$ andfor $\smash { \upsilon \in  { \mathcal { T } } ^ { \prime } }$ wehave $H ( u \circ v ) \ = \ H ^ { ( m + 1 ) } { \bigl ( } F ( u _ { 1 } ) , \ldots , F ( u _ { m } ) , F ( v ) { \bigr ) } \ =$ $F ( v ) ^ { T } ( \nabla H ) ^ { ( m ) } \bigl ( F ( u _ { 1 } ) , \ldots , F ( u _ { m } ) \bigr ) = F ( v ) ^ { T } J F ( u )$ ,and from theskew-symmetryof $J$ . □

Thetrees $u \circ v$ and $v \circ u$ have the same graph and differ onlyin theposition oftheroot.The relation (9.12） thusmotivates the consideration of the(smallest) equivalence relation on $T$ satisfying

$$
u \circ v \sim v \circ u .
$$

Wewant to select from each equivalence class,not containinga tree of the form $u \odot u$ ,exactlyoneelement.Thiscanbedoneasfollows(cf.Chartier,Faou&Murua 2005）:we choose a total ordering on the set $T$ thatrespects the number of vertices, i.e., $u < v$ whenever $| u | < | v |$ andwedefine

$$
\begin{array} { r l r } { T ^ { * } = \{ \bullet \} \cup \{ \tau | \tau \mathrm { ~ c a n n o t ~ b e ~ w r i t t e n ~ a s ~ } \tau = u \circ v \mathrm { ~ w i t h ~ } u \leq v \} } & { } \\ { } & { = \{ \bullet \} \cup \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } \mathbb { V } . . . \} } \end{array}
$$

(for the second line we assume $[ \bullet , \bullet ] < ( | \bullet | | )$ .Every tree $\tau \in \mathcal { L }$ is eitherequivalent tosome $u \circ u$ ortoa tree in $T ^ { * }$ This isaconsequence of the fact that aslongas $\tau = u \circ v$ with $u < v$ ,it can be changed to $v \circ u$ (what happens onlyafinite number of times).Moreover,two trees of $\mathbf { \mathcal { L } ^ { \prime \ast } }$ can never be equivalent.

Lemma 9.7.For a tree $\tau \in \mathcal { T } ^ { * }$ wehave

$$
J ^ { - 1 } \nabla H ( \tau ) ( y ) = \sigma ( \tau ) \sum _ { \theta \sim \tau } \frac { ( - 1 ) ^ { \kappa ( \tau , \theta ) } } { \sigma ( \theta ) } F ( \theta ) ( y ) ,
$$

where $\kappa ( \tau , \theta )$ isthenumber of root changes that arenecessary to obtainθ from $\gamma$ .

Proof.We compute $J ^ { - 1 } \nabla H ( \tau ) ( y )$ Theexpression $H ( \tau ) ( y )$ consists of $| \tau |$ factors correspondingto the vertices of $\tau$ ,each of which has tobedifferentiatedbyLeibniz' rule.Differentiation of $H ^ { ( m ) } ( y )$ (cf.Definition 9.5）and pre-multiplication by the matrix $J ^ { - 1 }$ yields $F ( \tau ) ( y )$ Before differentiating the other factors,we bring the correspondingvertex down to theroot.In view of Lemma 9.6 this only multiplies $H ( \tau ) ( y )$ by $( - 1 ) ^ { \kappa ( \tau , \theta ) }$ ,and shows thatadifferentiation ofthecorrespondingfactor yields $F ( \theta ) ( y )$ Since $\tau \in \ b { I } ^ { * }$ ,thenumber of possibilities to obtain $\theta$ from $\tau$ by exchanging roots is equal to $\sigma ( \tau ) / \sigma ( \theta ) .$ This factor has to beincluded. □

# IX.9.3Modified Hamiltonian

Wearenow in theposition to givean explicit formula forthe Hamiltonian of the modified differential equation provided that thenumerical method,can bewrittenas aB-series.An extension to partitioned methodswill be given in Sect.IX.10.

Theorem 9.8.Consideranumericalmethod that can bewrittenasa $B$ series(9.1), andthat issymplectic forevery Hamiltoniansystem $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) . } \end{array}$ Itsmodified differentialequation isthen Hamiltonianwith

$$
\widetilde H ( y ) = H _ { 1 } ( y ) + h H _ { 2 } ( y ) + h ^ { 2 } H _ { 3 } ( y ) + \dots ,
$$

where

$$
H _ { j } ( y ) = \sum _ { \tau \in T ^ { * } , | \tau | = j } { \frac { b ( \tau ) } { \sigma ( \tau ) } } H ( \tau ) ( y ) ,
$$

and the coefficients $b ( \tau )$ arethose of Theorem 9.2.Notice that the sum in(9.16)is only over trees in $T ^ { * }$ asdefined in (9.14).

Proof.We apply themethod(9.1）to the Hamiltoniansystem,so that by Theorem3.1 themodifieddifferential equation is(locally) Hamiltonian.It therefore follows from Theorem 9.3 that the coefficients $b ( \tau )$ of(9.4)satisfy(9.8).This relation implies $b ( \theta ) = ( - 1 ) ^ { \kappa ( \tau , \theta ) } b ( \tau )$ whenever $\theta \sim \tau$ Insertedinto(9.3),anapplication ofLemma9.7 provesthe statement. □

Remark 9.9.This theorem givesan explicit formula forthemodified Hamiltonian (formethods expressed as B-series).Since the elementary Hamiltonians $H ( \tau ) ( y )$ depend only on derivatives of $H ( y )$ ,thismodifiedHamiltonianisgloballydefined. ForRunge-Kutta methods this providesan alternative approach to the statement of Theorem3.2.

Forthe sake of completeness we give in the following theoremacharacterization ofHamiltonian vector fields of the form(9.4).

Theorem9.10. Thedifferentialequation $h \dot { y } = B ( \boldsymbol { b } , \boldsymbol { y } )$ with $b ( \emptyset ) = 0$ isHamiltonian forall vectorfelds $f ( y ) = J ^ { - 1 } \nabla H ( y )$ ifand onlyif

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \qquad f o r a l l \quad u , v \in T .
$$

Proof.The“onlyifpartfollows fromTheorem9.3.The“if"partisaconsequence of the proof of Theorem9.8. □

# IX.9.4 First Integrals Close to the Hamiltonian

Wehaveseenin Sect.IX.9.3that for symplectic methodsthemodified differential equation （9.4) based on $f ( y ) = J ^ { - 1 } \nabla H ( y )$ is Hamiltonian with a function of the form

$$
H ( c , y ) = \sum _ { \tau \in T ^ { * } } { \frac { h ^ { | \tau | - 1 } } { \sigma ( \tau ) } } c ( \tau ) H ( \tau ) ( y )
$$

and coefficients $c ( \tau ) = b ( \tau )$ In this section we study whether for non-symplectic methodsa function oftheform(9.18) can bea first integral of(9.4).Thisquestion hasbeenaddressedby Faou,Hairer&Pham(2oO4),andweclosely follow their presentation.

Lemma 9.11.Let $y ( t )$ beasolution of the differential equation(9.4)whichcan be writen as $h \dot { y } ( t ) = B ( b , y ( t ) )$ .Wethenhave

$$
\frac { d } { d t } H \big ( c , y ( t ) \big ) = H \big ( \delta _ { b } c , y ( t ) \big )
$$

where $\delta _ { c } b ( \bullet ) = 0$ and,for $\tau \in T ^ { * } w i t h \ | \tau | > 1 ,$

$$
\delta _ { b } c ( \tau ) = \sum _ { \theta \sim \tau } ( - 1 ) ^ { \kappa ( \tau , \theta ) } \frac { \sigma ( \tau ) } { \sigma ( \theta ) } \sum _ { \omega \in T ^ { * } \cap S P ( \theta ) } c ( \omega ) b ( \theta \setminus \omega ) .
$$

Thefirst sum is over all trees $\theta$ thatareequivalent to $\gamma$ (see(9.13)）,and thesecond sum is over all splittings of $\theta$ asinLemma9.1 (see Table9.2).

Proof.The proof is nearly the sameas that ofLemma 9.1.The first sum in(9.19) appears,because $H ( \theta ) ( y ) = H ( \tau ) ( y )$ for $\theta \sim \tau$ and because the sum in(9.18)is only over trees in $T ^ { * }$ . □

Table9.2.Formulas for $\delta _ { b } c ( \tau )$ for trees $\tau \in T ^ { * }$ up to order 6

$$
\begin{array} { r l } { \varepsilon _ { \mathrm { e f f } } ( Y ) } & { = - 2 \varepsilon _ { \mathrm { e f f } } \cdot \mathbf { A } _ { \mathrm { B } } ( Z ) } \\ { \varepsilon _ { \mathrm { e f f } } ( Y ) } & { = 3 \varepsilon _ { \mathrm { V } } \nabla \left( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \right) \delta _ { \mathrm { B } } ( Y ) } \\ { \varepsilon _ { \mathrm { e f f } } ( Y ) } & { = 4 \varepsilon _ { \mathrm { e f f } } \nabla \left( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \right) \delta _ { \mathrm { B } } ( Y ) } \\ { \varepsilon _ { \mathrm { e f f } } ( Y ) } & { = \varepsilon _ { \mathrm { e f f } } \cdot \mathbf { B } _ { \mathrm { B } } ( Y ) } \\ { \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ) - 2 \varepsilon _ { \mathrm { e f f } } \big ) \big ) } \\ { \varepsilon _ { \mathrm { e f f } } ( \xi _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ) \big ) } & { = \varepsilon _ { \mathrm { e f f } } \cdot \big ( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ) } \\ { \varepsilon _ { \mathrm { e f f } } ( \xi _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ) \big ) } & { = \varepsilon _ { \mathrm { e f f } } \cdot \big ( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \xi _ { \mathrm { e f f } } \big ) } \\ { \varepsilon _ { \mathrm { e f f } } ( \xi _ { \mathrm { e f f } } ) } & { = - 2 \varepsilon _ { \mathrm { e f f } } \cdot \big ( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } } \big ( Y ) \big ) } \\ { \varepsilon _ { \mathrm { e f f } } ( \xi _ { \mathrm { e f f } } ) } &  = \varepsilon _ { \mathrm { e f f } } \cdot \big ( \varepsilon _ { \mathrm { e f f } } + \varepsilon _ { \mathrm { e f f } }  \end{array}
$$

Corollary9.12.Thefunction $H ( c , y )$ of(9.18)isafirst integralofthedifferential equation(9.4) forevery $H ( y )$ ifand onlyif

$$
\delta _ { b } c ( \tau ) = 0 f o r a l l \tau \in T ^ { * } .
$$

Proof.The sufficiency follows fromLemma9.11and the necessity isaconsequence oftheindependence of the elementary Hamiltonians.To prove their independence wehave to show that the series(9.18) vanishes forall smooth $H ( y )$ onlyif $c ( \tau ) = 0$ forall $\tau \in \mathcal { I } ^ { \ast }$ .Withthe techniques of theproof of Theorem VI.7.4one can show that for every tree $\tau \in \mathcal { I } ^ { * }$ thereexistsapolynomial Hamiltonian such that the first component of $F ( \tau ) ( 0 )$ vanishes forall trees except for $\tau$ Differentiating（9.18）and employingLemma9.7 proves that $c ( \tau ) = 0$ . □

Solving the System(9.20).We consider a consistent method,i.e., $b ( \bullet ) = 1$ ,and we search fora first integral $H ( c , y )$ close to the Hamiltonian,i.e., $c ( \bullet ) = 1$ .

$| \tau | = 3$ :The condition(9.20) for $\tau = \mathbb { V }$ implies $b ( \ b { \mathscr { I } } ) = 0$ ,which means that the method has to be of order two.

$| \tau | = 4$ :Thereis only one tree in $T ^ { * }$ with four vertices.The corresponding condition can be satisfied by putting $c ( V ) = b ( V )$ ,

$| \tau | = 5$ The third condition yields $b ( \left[ \left[ \cdot \right] \right] ) = 0 .$ Letting $c ( \bigtriangledown V )$ besuch that one of the other two conditions holds,we still have to satisfy

$$
b ( \backprime ) + b ( \div 2 ) = 2 6 ( \div 2 ) = 0 .
$$

This condition is satisfied for symplectic methods,for which $b ( u \circ v ) + b ( v \circ u ) = 0$ ， andalso forsymmetricmethods,forwhich $b ( \tau ) = 0$ for treeswith an even order.

$| \tau | = 6$ :Thereare four conditions for three $c ( \tau )$ coefficients.Assuming (9.20) fortrees with less than five vertices,these four conditions admita solution if and onlyif

$$
5 6 ( \dot { \Psi } ) + 5 6 ( \dot { Y } ) + 6 6 ( \dot { \zeta } ) + 6 6 ( \dot { \sqrt { 3 } } ) - 1 2 6 ( \dot { \sqrt { 3 } } + 3 6 ( \dot { \zeta } ) )
$$

Thisrelationis obviously satisfied by every symplectic method.However,as we shall see soon,there are symmetric methods that do not satisfy(9.22).

Forvarious symmetric methods of order4(i.e., $b ( \tau ) = 0$ for $1 < | \tau | < 5$ we compute the coefficients $b ( \tau )$ ofthe leading perturbation termin(9.4）and also the expression(9.22),see Table9.3.None of the considered methods is symplectic.

Surprisingly，the 3-stage collocation method Lobatto IIA (see Table II.1.2 for thecoefficients) satisfies the condition(9.22).This implies for every Hamiltonian system (reversible or not reversible) that thedominatingerror term in the numerical Hamiltonian does not have any drift.

The3-stageLobatto IIIB method(see Table II.1.4)does not satisfy the condition (9.22).We therefore expect a drift in the numerical Hamiltonian.

Table9.3.Coefficients $b ( \tau )$ and expression (9.22) for methods of order 4   

<table><tr><td>method</td><td>E</td><td>vYY{Y</td><td></td><td></td><td></td><td></td><td>(9.22)</td></tr><tr><td>Lobatto IIIA</td><td>1 120 240</td><td>1 480</td><td>1 120</td><td>1 240</td><td>1 720</td><td>1 360</td><td>0</td></tr><tr><td>Lobatto IIIB</td><td>1 120</td><td>1 720</td><td>1 120</td><td>1 360</td><td>1 720</td><td>1 240</td><td>1</td></tr></table>

Lemma9.13.For given $b ( \tau ) , \tau \in T$ satisfying $b ( \emptyset ) = 0$ , $b ( \bullet ) = 1$ andforfixed $c ( \bullet )$ ,thelinear system $( 9 . 2 0 ) f o r c ( \tau ) , \tau \in T ^ { * }$ hasat most one solution.

Proof. We prove by induction on $\tau \in \mathcal { I } ^ { * }$ that $c ( \tau )$ isuniquely determined by(9.20). For this we assume that the ordering on $T$ is such that,within trees of the same order,it is increasingwhen the numer of vertices connected to the root decreases, cf.(9.14).

Let $\tau = [ \tau _ { 1 } , \dots , \tau _ { m } , \bullet , \dots , \bullet ] \in T ^ { * } \setminus \{ \bullet \}$ with $| \tau _ { j } | > 1$ ,and denote by $k$ the numberof $^ { \circ }$ 'sin this representation.Since the tree $\tau \cup \mathbf { \Sigma } ^ { \bullet }$ is again in the set ${ \mathbf { \nabla } } ^ { T ^ { * } }$ , condition (9.20) yields

$$
0 = \delta _ { b } c ( \tau \circ \bullet ) = ( k + 1 ) c ( \tau ) b ( \bullet ) - ( k + 1 ) c ( \bullet ) b ( \tau ) + \dots .
$$

For $m = 0$ ,no further terms are present and $c ( \tau )$ isuniquely determined by this relation.For $m > 0$ ,thethree dots in (9.23）represent a linearcombination of $c ( \mu ) b ( \nu )$ with $| \mu | < | \tau |$ (which,by the induction hypothesis,are already known） andof $c ( \sigma ) b ( \cdot )$ ,where $\sigma \in \mathcal { I } ^ { \ast }$ is the representant in $T ^ { * }$ of the equivalence class for $\tau ^ { \prime }$ Weuse the notation $\tau ^ { \prime }$ for some tree which is obtained from $\tau$ byremoving one of the end vertices of $\tau _ { j }$ andby adding itto therootof $\tau$ .

In general we will have $\tau ^ { \prime } \in T ^ { * }$ （sothat $\sigma = \tau ^ { \prime }$ ）,and in thiscase its numberof end vertices connected to the root is larger than that for $\tau$ .Hence, $\sigma < \tau$ ,andthe coefficient $c ( \sigma )$ isknown bythe induction hypothesis.

If $\tau ^ { \prime } \notin T ^ { * }$ ,what is only possible if $\tau = u \circ v$ with $| u | = | v |$ and $u > v$ ,we have $\tau ^ { \prime } = u ^ { \prime } \circ v$ and $u ^ { \prime } < v$ (notice that $u ^ { \prime } = v$ is not permitted for trees in $T ^ { * }$ ). In this case we have $\sigma = v \circ u ^ { \prime } \in T ^ { * } .$ Consequently, $c ( \tau ) = c ( u \circ v )$ is expressed in terms of $c ( v \circ u ^ { \prime } )$ and known quantities.Applying the same reasoning to $v \circ u ^ { \prime }$ and observing that because of $u \ > \ v$ thetree $\boldsymbol { v }$ hasat least as many end vertices connected to the root as the tree $\boldsymbol { u }$ ,we see that $c ( v \circ u ^ { \prime } )$ is expressed in terms of alreadydetermined quantities. □

Theexpression (9.20) is bilinear in $b$ and $c$ Assuming that $h \dot { y } = B ( b , y )$ is Hamiltonian,the mapping $b$ hasthesame degree of freedom as $c$ Itis therefore not astonishing to have the followingdual variant ofLemma9.13.

Lemma9.14.Let $c ( \tau )$ , $\tau \in \mathcal { I } ^ { \ast }$ be given and assume $c ( \circ ) = 1$ and $b ( \emptyset ) = 0$ Then, forfixed $b ( \bullet )$ thelinearsystem(9.20)for $b ( \tau ) , \tau \in T$ hasat most one solution satisfying $b ( u \circ v ) + b ( v \circ u ) = 0$ forall $u , v \in T .$

Proof.By assumption on $b$ ,thecoefficients $b ( \tau )$ , $\tau \in T \setminus T ^ { * }$ areuniquely determined by those for $\tau \in \textit { T } ^ { * }$ Thestatement is thus obtained inthe samewayas that forLemma 9.13with the only difference that expressions $c ( \bullet ) b ( \sigma )$ and not $c ( \sigma ) b ( \bullet )$ have to be studied. □

Theorem9.15 (Chartier,Faou&Murua20o5).Theonly symplecticmethod(as $B$ -series)thatconservestheHamiltonianforarbitrary $H ( y )$ is the exact flow of the differentialequation.

Proof.If the method conserves exactly the Hamiltonian,we have (9.2O）with $c ( \circ ) = 1$ and $c ( \tau ) = 0$ forall other trees in $T ^ { * }$ Bythe uniqueness statement ofLemma 9.14and thesymplecticity of themethod(Theorem 9.10),we obtain $b ( \tau ) = 0$ for $| \tau | > 1$ .Consequently,no perturbation is permitted in the modified differential equation of the method. □

Aclosely relatedresult is giveninGe&Marsden（1988).There,general symplectic methodsare considered(not necessarilyB-seriesmethods)but aweakerresultisobtained (in fact,they assume that the system does not have other conserved quantities than $H ( y )$ ,andit is shown that the numerical flowcoincideswith the exactflowup toareparametrization of time).

# IX.9.5EnergyConservation:Examples and Counter-Examples

Itisgenerally believed that symmetric methods applied toreversibleHamiltonian systems (reversible in the sense that $H ( - p , q ) \ = \ H ( p , q ) )$ have the same longtimebehaviouras symplectic methods.Thisis true inmany situations of practical interest,and we shall prove thisrigorouslyin Sect.XI.3 for integrablereversible systems.There are,however,interesting counter-examples to this general belief. Theyare takenfromFaou,Hairer&Pham（2004).

Example9.16.Our first example is a modification of the pendulum equation

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { 2 } - \cos q + { \frac { 1 } { 5 } } \sin ( 2 q ) ,
$$

where the additional term $\sin ( 2 q )$ destroys the symmetry in $q$ TheHamiltonian still satisfies $H ( - p , q ) = H ( p , q )$ Weconsider initial values $p ( 0 ) = 2 . 5 $ , $q ( 0 ) = 0$ with sufficiently large initial velocity,such that $p ( t )$ stayspositive for all times and the symmetry $p  - p$ does not affect the numerical solution.The angle $q ( t )$ increases without limit,but thepotential is $2 \pi$ -periodic sothat thesolutionstaysonaclosed curve of the cylinder $\mathbb { R } \times S ^ { 1 }$ .

Weapply the3-stageLobatto IIIA and IIIB methodsto this problem.Figure9.3 shows the errorin the Hamiltonian along the numerical solutions.There isa visible energy drift of size $\mathcal { O } ( t h ^ { 4 } )$ for the Lobatto IIB method and no drift can be seen on thisscalefor theLobatto IIIA method.To get more insight into its long-time behaviour,we apply themethod with the same step sizetoamuch longer time interval, and we plot the error in $H ( p _ { n } , q _ { n } ) + h ^ { 4 } H _ { 5 } ( p _ { n } , q _ { n } )$ ,where the firstperturbation term iscomputed from(9.18) and the linear system (9.20)as

![](images/551539e51a8ef94bbab2e5abb75c94f723bd712f2fe0ff11cfe02e47a884b8d3.jpg)  
Fig.9.3.Numerical Hamiltonian of Lobattomethods of order4 for theperturbed pendulum (9.24)；step size $h = 0 . 2$ ,integration interval [0,500]

![](images/013e81fc15c526481af182d4d8422e3ec28420056321b69d170dd146fb59c442.jpg)  
Fig.9.4.Error in $H ( p , q ) + h ^ { 4 } H _ { 5 } ( p , q )$ along the numerical solution of the 3-stage Lobatto IIIA method for the perturbed pendulum(9.24);step size $h = 0 . 2$ ,integration interval $[ 0 , 5 0 0 0 0 0 ]$

$$
H _ { 5 } ( p , \bar { q } ) = \frac { 1 } { 9 6 0 } \Bigl ( 3 U ^ { ( 4 ) } ( q ) p ^ { 4 } - 2 U ^ { ( 3 ) } U ^ { \prime } ( q ) p ^ { 2 } - \bigl ( U ^ { \prime \prime } ( \bar { q } ) p \bigr ) ^ { 2 } + U ^ { \prime \prime } ( \bar { q } ) \bigl ( U ^ { \prime } ( \bar { q } ) \bigr ) ^ { 2 }
$$

with the potential $U ( q ) = - \cos q + 0 . 2 \sin ( 2 q )$ (seeFig.9.4).Repeating the same experiment with halved step size shows that there are oscillations with amplitude $\mathcal { O } ( h ^ { 6 } )$ and a drift with slope $\mathcal { O } ( h ^ { 8 } )$ .Consequently,the error in the Hamiltonian for theLobatto IIIA method behaves on this problem like $O ( h ^ { 4 } + t h ^ { 8 } )$ .

Without the term $\sin ( 2 q )$ in(9.24)allsymmetric one-step methods nearlyconserve the Hamiltonian.

Example9.17.Forpolynomial Hamiltonians $H ( y )$ of degree at most four,the elementary Hamiltonian corresponding tothe treevanishesidentically.Therefore,the condition(9.2O) need not be considered for this tree,and the remaining three conditions can always be satisfied by the three $c ( \tau )$ coefficients.This implies that,for example for the Henon-Heilesproblem

$$
H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = { \frac { 1 } { 2 } } { \big ( } p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } { \big ) } * { \frac { 1 } { 2 } } { \big ( } q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } { \big ) } * q _ { 1 } q _ { 2 } ^ { 2 } = { \frac { 1 } { 3 } } q _ { 1 } ^ { 3 } ,
$$

theleading error termin the numerical Hamiltonian remains boundedbyall methods of order four.Numerical experiments indicate that in this case also higher order error termsare bounded by symmetric methods suchasLobatto IIA and IIIB,even if the initialvalues are chosen so that the solution ischaotic.

Example9.18.A concrete mechanical system with two degrees of freedom is describedbytheHamiltonian

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } p + { \frac { \omega ^ { 2 } } { 2 } } { \bigl ( } \| q \| - 1 { \bigr ) } ^ { 2 } + q _ { 2 } - { \frac { 1 } { \| q - a \| } } .
$$

Itisamodel ofa planar spring pendulum with exterior forces.The spring has a harmonic potential with frequency $\omega$ (Hooke's law).The exterior forces are gravitationand attraction toa mass point situated at $a$ ,which has to be chosen so that no symmetry in the $q$ -variablesispresent.

Thenumerical experiments,reported by Faou,Hairer& Pham(2Oo4),use $\omega = 2$ , $a = ( - 3 , - 5 ) ^ { T }$ and initial values for theposition $q ( 0 ) = ( 0 , 1 ) ^ { T }$ （upright position),and for thevelocity $p ( 0 ) = ( - 1 , - 0 . 5 ) ^ { T } .$ The pendulum thus turns around the fixed end of the spring which is at the origin.

Asforthe problem of Example 9.16 one clearly observesadrift for the 3-stage Lobatto IIB method,and the error in the Hamiltonian behaves like $\mathcal { O } ( t h ^ { 4 } )$ As predicted by the theory of the preceding section,thedominant error term for the3- stageLobatto IIIA methodisbounded.Thereis,however,adriftalreadyinthenext term so that the error in the Hamiltonian behaves for thismethod as $\mathcal { O } ( h ^ { 4 } + t h ^ { 6 } )$

Removing one of the exterior forces（gravitation orattraction to $a$ ）,theerror in the Hamiltonian remains bounded of size $\mathcal { O } ( h ^ { 4 } )$ without any drift （even not in higher order terms) for bothLobatto methods.

# IX.10Extension to Partitioned Systems

Allresults of Sect.IX.9can be extended to partitioned methodswhosediscrete flow canbewritten as a P-series.This includes important geometric integrators such as thesymplectic Eulermethodandthe Stormer-Verletscheme.Interestingly,many of theresults have been originally presented and proved for this more general case(see Hairer(1994)).

# IX.10.1P-Series of the Modified Equation

We consider the partitioned system

$$
\dot { p } = f ( p , q ) , \qquad \dot { q } = g ( p , q ) ,
$$

where,inview of an application to Hamiltonian systems,we use $( p , q )$ instead of $( y , z )$ forthevariables.By Theorem III.2.4all consistent partitionedRunge-Kutta methods can be written as P-series (cf.Definition II.2.1)

$$
{ \binom { p _ { 1 } } { q _ { 1 } } } = { \binom { p _ { 0 } } { q _ { 0 } } } + h { \binom { f } { g } } _ { 0 } + h ^ { 2 } { \binom { a ( l ) ( f _ { p } f ) + a ( \tilde { \ell } ) ( f _ { q } g ) } { a ( \tilde { \ell } ) ( g _ { p } f ) + a ( \tilde { \ell } ) ( g _ { q } g ) } } _ { 0 } + \ldots ,
$$

wherethe subscript O indicates an evaluation at the initial value $( p _ { 0 } , q _ { 0 } )$ The first perturbation term of themodified equation(1.1) can therefore be written as

$$
{ \binom { f _ { 2 } ( p , q ) } { g _ { 2 } ( p , q ) } } = { \binom { ( a ( { \underline { { f } } } ) - { \frac { 1 } { 2 } } ) ( f _ { p } f ) ( p , q ) + ( a ( { \underline { { f } } } ) - { \frac { 1 } { 2 } } ) ( f _ { q } g ) ( p , q ) } { ( a ( { \underline { { f } } } ) - { \frac { 1 } { 2 } } ) ( g _ { p } f ) ( p , q ) + ( a ( { \underline { { f } } } ) - { \frac { 1 } { 2 } } ) ( g _ { q } g ) ( p , q ) } } ) 
$$

and,in general,one finds

$$
{ \binom { f _ { j } ( p , q ) } { g _ { j } ( p , q ) } } = { \binom { \sum _ { \tau \in T P _ { p } , \mid \tau \mid = j } { \frac { b ( \tau ) } { \sigma ( \tau ) } } F ( \tau ) ( p , q ) } { \sum _ { \tau \in T P _ { q } , \mid \tau \mid = j } { \frac { b ( \tau ) } { \sigma ( \tau ) } } F ( \tau ) ( p , q ) } } .
$$

Hence,the modified equation(1.1) is of the form

$$
\begin{array} { r } { \left( { \overbrace { \tilde { \eta } } } ^ { \dot { \tilde { p } } } \right) = \left( \sum _ { \tau \in T P _ { p } } { \frac { h ^ { \vert \tau \vert - 1 } } { \sigma ( \tau ) } } b ( \tau ) F ( \tau ) ( \widetilde { p } , \widetilde { q } ) \right) , } \\ { \left( { \overbrace { \tilde { q } } } ^ { \ddot { \tilde { q } } } \right) = \left( \sum _ { \tau \in T P _ { q } } { \frac { \dot { h } ^ { \vert \tau \vert - 1 } } { \sigma ( \tau ) } } b ( \tau ) \widetilde { F } ( \tau ) ( \widetilde { p } , \widetilde { q } ) \right) , } \end{array}
$$

where $b ( \tau ) = 1$ for $| \tau | = 1$ , $b ( \tau ) = a ( \tau ) - \textstyle { \frac { 1 } { 2 } }$ for $| \tau | = 2$ For $| \tau | > 2$ ,the coefficients $b ( \tau )$ canbe obtained recursively from Theorem 10.2below.The proofs of the following two results are straightforward extensions of those for Lemma 9.1 and Theorem 9.2,and are therefore omitted.

Lemma 10.1 (Lie-Derivative of P-series).Let $b ( \tau )$ (with $b ( \emptyset _ { p } ) = b ( \emptyset _ { q } ) = 0 .$ and $c ( \tau )$ bethe coefficients oftwo $P$ -series,and let $( p ( t ) , q ( t ) )$ beaformal solution of thedifferential equation $h ( \dot { p } ( t ) , \dot { q } ( t ) ) ^ { T } = P \big ( b , ( p ( t ) , q ( t ) ) \big )$ i.e.,(10.4).The Lie derivativeofthe function $P ( c , ( p , q ) )$ withrespect tothe vectorfeld $P ( b , ( p , q ) )$ is againa $P$ -series

$$
h \frac { d } { d t } P \big ( c , ( p ( t ) , q ( t ) ) \big ) = P \big ( \partial _ { b } c , ( p ( t ) , q ( t ) ) \big ) .
$$

Its coeffcientsare given by $\partial _ { b } c ( \emptyset _ { p } ) = \partial _ { b } c ( \emptyset _ { q } ) = 0$ ,andfor $| \tau | \geq 1$ by

$$
\partial _ { b } c ( \tau ) = \sum _ { \theta \in S P ( \tau ) } c ( \theta ) b ( \tau \setminus \theta ) ,
$$

where,analogously to(9.5), $S P ( \tau )$ denotes the setofsplittings of $\tau \in \mathit { T P }$ .

In formula (10.5), $\emptyset _ { p } ~ \in ~ S P ( \tau )$ definesaspliting only if $\tau \in \textit { T P } _ { p }$ and $\emptyset _ { q } \in S P ( \tau )$ onlyif $\tau \in \tau P _ { q }$ Wetherefore have $\partial _ { b } c ( \bullet ) = c ( \emptyset _ { p } ) b ( \bullet )$ ， $\partial _ { b } c ( \circ ) =$ $c ( \emptyset _ { q } ) b ( \circ )$ ,and asexamples for trees of order3

$$
\begin{array} { l l l } { { \partial _ { b } c ( { } ^ { \displaystyle \ P } ) } } & { { = } } & { { c ( { \emptyset } _ { p } ) b ( { } ^ { \displaystyle \ P } ) + 2 c ( { } ^ { \displaystyle \ P } ) b ( { } ^ { \displaystyle \circ } ) { } _ { \emptyset } } } \\ { { \partial _ { b } c ( { } ^ { \displaystyle \ P } ) } } & { { = } } & { { c ( { \emptyset } _ { p } ) b ( { } ^ { \displaystyle \ P } ) + c ( { } ^ { \displaystyle \ P } ) b ( { } ^ { \displaystyle \circ } ) + c ( { } ^ { \displaystyle \bar { \rho } } ) b ( { } ^ { \displaystyle \bullet } ) . } } \end{array}
$$

Theorem10.2.Ifthemethod $\left( p _ { 1 } , q _ { 1 } \right) = \varPhi _ { h } ( p _ { 0 } , q _ { 0 } )$ can be written as (10.2),the modifieddifferentialequationis givenby(1O.4),where therealcoefficients $b ( \tau )$ are recursively definedby $b ( \emptyset _ { p } ) = b ( \emptyset _ { q } ) = 0$ ， $b ( \tau ) = 1 f o r | \tau | = 1$ and

$$
b ( \tau ) = a ( \tau ) - \sum _ { j = 2 } ^ { | \tau | } \frac { 1 } { j ! } \partial _ { b } ^ { j - 1 } b ( \tau ) \qquad f o r \quad \tau \in T { \bar { T } } { \bar { P } } .
$$

Here, $\partial _ { b } ^ { j - 1 }$ denotestheiterateoftheLiederivative $\partial _ { b }$ defined in Lemma 10.1.[

Example10.3.The symplectic Euler method

$$
p _ { n + 1 } = p _ { n } + h f ( p _ { n + 1 } , q _ { n } ) , \qquad q _ { n + 1 } = q _ { n } + h g ( p _ { n + 1 } , q _ { n } )
$$

isapartitioned Runge-Kutta method $a _ { 1 1 } = 1$ , $\hat { a } _ { 1 1 } = 0$ ， $b _ { 1 } = \widehat { b } _ { 1 } = 1$ andcan therefore beexpressed asaP-series(10.2).From Theorem III.2.4we get itscoeffcients:

$$
a ( \tau ) = \left\{ \begin{array} { l l } { { 1 } } & { { \mathrm { i f ~ a l l ~ v e r t i c e s ~ ( d i f f e r e n t ~ f r o m ~ t h e ~ r o o t ) ~ a r e ~ b l a c k , } } } \\ { { 0 } } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right.
$$

From Theorem 10.2we can compute the coeficients $b ( \tau )$ of the modified equation (10.4).Theyare givenin Table10.1 for the treeswithablackroot.Since $a ( \tau )$ does not depend on the colour of the root of $\tau$ ,the same holds for the coefficients $b ( \tau )$ Hence,wedo not include the values of $b ( \tau )$ for trees with a white root.

Table10.1.Coefficients $b ( \tau )$ of the modified equation for symplectic Euler(10.7)   

<table><tr><td></td><td>~v}}}</td></tr><tr><td></td><td>6(T)11/2-1/21/6-1/31/61/3-1/6-1/61/3</td></tr></table>

Weknow from Theorem3.1 that themodifieddifferentialequation (10.4)ofa symplectic method applied toa Hamiltonian system

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q )
$$

is again Hamiltonian.

Theorem10.4.Supposethatforall separable Hamiltonians ${ \cal H } ( p , q ) = { \cal T } ( p ) +$ $U ( q )$ themodifiedvector feld(10.4),truncatedafteranarbitrarypowerof $h$ is (locally)Hamiltonian.Then,wehave

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \qquad \quad u \in T P _ { p } , v \in T P _ { q }
$$

fortrees,where neighbouring vertices have different colours.

If itis(locally)Hamiltonianforal $H ( p , q )$ then(10.9）holds forall $u \in \mathcal { I } P _ { p } ,$ $v \in \ I P _ { q } ,$ andadditionallywe have

$b ( \tau )$ is independent of thecolour of the rootof $\tau \in T P .$

Ifitis(locally) Hamiltonian forall $H ( p , q ) = { \textstyle \frac { 1 } { 2 } } p ^ { I } C p + c ^ { I } p + U ( q )$ (with symmetric matrix $C$ ),thenwehave

$$
b ( \circ \circ u ) + b ( u \circ \circ ) = 0 , \quad b ( u \circ \circ v ) - b ( v \circ \circ u ) = 0 \qquad u , v \in T N _ { p }
$$

(seeSect.VI.7.1for thedefinitionof $T N _ { p }$ and $u \circ \circ v$ )

Theproofis the sameas for Theorem9.3and thereforeomitted.

# IX.10.2 Elementary Hamiltonians

Wehavealready seenin Example 3.4that themodified Hamiltonian of the symplectic Euler method is composed of expressions such as $H _ { p } H _ { q }$ ， $H _ { p p } ( H _ { q } , H _ { q } )$ , $H _ { p q } ( H _ { q } , H _ { p } )$ ,etc.Thesewill play therole of elementary Hamiltonians forpartitionedmethods.In the followingdefinition,the elementary differentials $F ( \tau ) ( p , q )$ correspond to the partitioned system $f ( p , q ) = - H _ { q } ( p , q )$ , $g ( p , q ) = H _ { p } ( p , q )$

Definition 10.5. Fora given function $H : D  \mathbb { R }$ （with open $D \subset \mathbb { R } ^ { d } \times \mathbb { R } ^ { d } )$ and for $\tau \in \mathit { I P }$ wedefine the elementary Hamiltonian $H ( \tau ) : D  \mathbb { R }$ by

$$
\begin{array} { l } { { H ( \bullet ) ( p , q ) = H ( \circ ) ( p , q ) = H ( p , q ) } } \\ { { H ( \tau ) ( p , q ) = { \displaystyle { \frac { \partial ^ { m + l } H ( p , q ) } { \partial ^ { m } p \partial ^ { l } q } } } \Big ( F ( u _ { 1 } ) ( p , q ) , . . . , F ( v _ { 1 } ) ( p , q ) , . . . . \Big ) } } \end{array}
$$

where $\tau = [ u _ { 1 } , \dots , u _ { m } , v _ { 1 } , \dots , v _ { l } ] _ { p }$ or $\tau = [ u _ { 1 } , \dots , u _ { m } , v _ { 1 } , \dots , v _ { l } ] _ { q }$ with trees $u _ { i } \in T { \cal P } _ { p }$ and $v _ { i } \in \mathcal { I } P _ { q }$

Examples of elementary Hamiltoniansare

$$
\begin{array} { r } { H ( \bullet ) = H , H ( \mathring { \pmb { \ ? } } ) = H _ { q } H _ { p } , } \\ { H ( \mathring { \pmb { \gamma } } ) = H _ { p p } ( H _ { q } , H _ { q } ) , H ( \mathring { \pmb { \gamma } } ) = - H _ { p q } ( H _ { q } , H _ { p } ) , H ( \mathring { \pmb { \gamma } } ) = H _ { q q } ( H _ { p } , H _ { q } ) . } \end{array}
$$

We notice that,incontrast to Sect.IX.9.2,non-vanishing elementaryHamiltonians exist for trees with two vertices.

Lemma10.6.Elementary Hamiltonians satisfy

$$
H ( u \circ v ) ( p , q ) + H ( v \circ u ) ( p , q ) = 0 f o r \ u \in T P _ { p } \ a n d \ v \in T P _ { q } ,
$$

andtheydo not depend on thecolourofthe root.

Proof.The independence of the colour of theroot isby definition,and formula (10.12) is proved in the same way as the statement ofLemma 9.6. □

Theconditions(10.9)and (10.1O)define relations between the coefficients $b ( \tau )$ ofa Hamiltonian vector field (1O.4).The previous lemma shows analogous relations between elementary Hamiltonians.This motivates the consideration of the following equivalence relation on $T P$ (Hairer 1994).

Definition10.7.Wedenote by $\sim$ thesmallest equivalence relation on $T P$ which satisfies the two properties

$u \sim v$ if $u$ and $v$ are identical with the exception of the colour of the root;

$u \circ v \sim v \circ u$ for $u \in T P _ { p }$ and $v \in T P _ { q }$

Equivalent trees of ordersupto threeare grouped together in Fig.1O.1.We can change the colour of the root,andwe can move the root toa neighbouring vertex if it has the opposite colour.

Inthecase of separable Hamiltonians,one has to consider only trees forwhich neighbouring vertices havedifferent colours.This implies that the first condition of Definition 10.7 is empty.The second conditionmeans that theroot can be movedarbitrarily in the tree without changing the equivalence class.For this special situation, equivalenceclasses have beenconsideredalreadybyAbia&Sanz-Serna（1993)and arenamed“bicolour(unrooted) trees".

Similarto(9.l4) we select representatives from the equivalence classas follows: wefixa total ordering on the set $_ { T P }$ that（i）respects the number of vertices,and (ii)is such that no tree isbetween trees that differ only in the colour of the root.The orderingofFig.10.1issuchapossiblechoice.Wethendefine

$$
\begin{array} { r } { T P ^ { * } = \left\{ \bullet , \circ \right\} \cup \left\{ \tau \in T P \middle | \begin{array} { l } { \tau \mathrm { c a n n o t ~ b e ~ w r i t t e n ~ a s ~ } \tau = u \circ v \mathrm { ~ w i t h } } \\ { \mathrm { a l s o ~ n o t ~ i f ~ t h e ~ c o l o u r ~ o f ~ t h e ~ r o o t ~ i s ~ c h a ~ } } \end{array} \right. } \end{array}
$$

We further let $T P _ { p } ^ { * } = T P ^ { * } \cap T P _ { p }$ and $T P _ { q } ^ { * } = T P ^ { * } \cap T P _ { q }$

Lemma 10.8.Fora tree $\tau \in T P ^ { * }$ we have

$$
\begin{array} { r l r } { - \displaystyle \frac { \partial H ( \tau ) } { \partial q } ( p , q ) } & { = } & { \displaystyle \sigma ( \tau ) \sum _ { \theta \sim \tau , \theta \in T P _ { p } } \frac { ( - 1 ) ^ { \kappa ( \tau , \theta ) } } { \sigma ( \theta ) } F ( \theta ) ( p , q ) , } \\ { \displaystyle \frac { \partial H ( \tau ) } { \partial p } ( p , q ) } & { = } & { \displaystyle \sigma ( \tau ) \sum _ { \theta \sim \tau , \theta \in T P _ { q } } \frac { ( - 1 ) ^ { \kappa ( \tau , \theta ) } } { \sigma ( \theta ) } F ( \theta ) ( p , q ) , } \end{array}
$$

where $\kappa ( \tau , \theta )$ isthenumber of root changes that are necessaryto obtainθ from $^ { - 7 }$

Theproofisthe sameas forLemma9.7and therefore omitted.

Wearenow able to give themainresult of this section.

Theorem1o.9.Consider a numerical method that can be written asa $P$ -series (10.2),and that is symplectic for every Hamiltonian(1O.8).Itsmodifieddifferentialequation isthen Hamiltonianwith

$$
\widetilde { H } ( p , q ) = H _ { 1 } ( p , q ) + h H _ { 2 } ( p , q ) + h ^ { 2 } H _ { 3 } ( p , q ) + \dots ,
$$

where

$$
H _ { j } ( p , q ) = \sum _ { \tau \in T P _ { p } ^ { * } , \ | \tau | = j } { \frac { b ( \tau ) } { \sigma ( \tau ) } } H ( \tau ) ( p , q ) ,
$$

(10)det and the coefficients $b ( \tau )$ arethoseof Theorem 10.2.Notice that $T { \cal P } _ { p } ^ { * }$ or $T P _ { q } ^ { * }$ $H _ { j } ( p , q )$ from

Proof.Thisis the same as for Theorem 9.8.

If themethod(1O.2)is known to be symplectic for separable Hamiltonians only, and if it isapplied to $H ( p , q ) = T ( p ) + U ( q )$ ,the statement ofTheorem 10.9 is still valid.In this situation $H ( \tau ) ( p , q )$ vanishesifavertex of $\tau$ has sons with different colour(it then containsa factor $H _ { p q \dots } = 0$ ).

Example 10.10. Consider the 2-stage Lobatto IIA-IIB pair (cf. Table II.2.1), which is the natural extension of the Stormer-Verlet scheme to non-separable problems.We compute the coefficients $a ( \tau )$ from Theorem III.2.4,and $b ( \tau )$ from Theorem10.2.Theresultis givenin Table 1O.2.Notice that $a ( \tau )$ and $b ( \tau )$ areboth independent of the colour of the root.Theorem 10.9 then yields

$$
\widetilde { \cal H } = { \cal H } + { \frac { h ^ { 2 } } { 2 4 } } \Bigl ( 2 { \cal H } _ { p p } { \cal H } _ { q } ^ { 2 } - { \cal H } _ { q q } { \cal H } _ { p } ^ { 2 } + 2 { \cal H } _ { p q } { \cal H } _ { q } { \cal H } _ { p } \Bigr ) + \ldots ,
$$

for the modified Hamiltonian.Since the method is symmetric, $\breve { H }$ is in even powers of $h$ .The next non-vanishing term requires the consideration of trees up to order 5.

Table10.2. Coefficients $a ( \tau )$ and $b ( \tau )$ for the Stormer-Verlet scheme (Table II.2.1)   

<table><tr><td>T</td><td>vv} 1/4</td></tr><tr><td>a（T）</td><td>11/21/21/21/4</td></tr><tr><td></td><td>1/4</td></tr><tr><td>01/6-1/12-1/121/121/12-1/61/12</td><td>1/41/4</td></tr><tr><td>b(t) 1 0</td><td></td></tr></table>

Remark 9.9,thecharacterization of symplectic vector fields(1O.4),and theresultsof Sect.IX.9.4 can be extended to the case of (partitioned) P-series.We renounce of giving all the details here.

# IX.11 Exercises

1.Change the Maple program of Example 1.1in such away that themodified equations forthe implicit Eulermethod,the implicit midpoint rule,orthetrapezoidal ruleareobtained.Observe that for symmetricmethods one gets expansions in even powers of $h$ .   
2.Write a short Maple program which,for simple methods such as the symplectic Euler method,computes some terms of the modified equation for a twodimensional system $\dot { p } = f ( p , q )$ ， $\dot { q } = g ( p , q )$ .Check the modified equations of Example1.3.   
3.Prove that the modified equation of the Stormer-Verlet scheme(I.1.15)applied to $\ddot { y } = g ( y )$ isasecond order differential equation of the form $\ddot { \widetilde { y } } = g _ { h } ( \widetilde { y } , \dot { \widetilde { y } } )$ with initial values given by $\widetilde { y } ( 0 ) = y _ { 0 }$ and $\dot { \widetilde { y } } ( 0 )$ such that $\widetilde y ( h ) = y _ { 1 }$ holds.

Hint.Taylor expansion shows that for asmooth function $\widetilde { y } ( t )$ satisfying $\widetilde { y } ( t ) =$ $y _ { n }$ wehave

$$
\Big ( 1 + \frac { h ^ { 2 } } { 1 2 } D ^ { 2 } + \frac { h ^ { 4 } } { 3 6 0 } D ^ { 4 } + . . . \Big ) \tilde { \tilde { y } } ( t ) = g \big ( \widetilde { y } ( t ) \big ) ,
$$

where $D$ represents differentiation with respect to time.

Warning.Ingeneral,wedootetat $\widetilde { y } ( t _ { n } ) = \dot { y } _ { n }$

4.Prove that for $\rho$ -reversibledifferential equationstheelementarydifferentials satisfy

$$
F ( \tau ) ( \rho y ) = ( - 1 ) ^ { | \tau | } \rho F ( \tau ) ( y ) .
$$

Usethis to give an alternative proof of Theorem 2.3 for the case that the method issymmetric and can be expressed asa $B$ -series.

5.Findafirst integral of the truncated modified equation for the symplectic Euler method and theLotka-Volterra problem(Example1.3).

Hint.With thetransformation $p = \exp P$ , $q = \exp Q$ you will get a Hamiltoniansystem.

Result. $I ( p , q ) = I ( p , q ) - h \big ( ( p + q ) ^ { 2 } - 8 p - 1 0 q + 2 \ln p + 8 \ln q \big ) / 4$

6.(Field&Nijhoff2oo3).Apply the symplectic Euler method to the system with Hamiltonian $H ( p , q ) = \ln ( \alpha + p ) + \ln ( \beta + q ) ,$ Compute the modified Hamiltonianand prove that the series converges for sufficiently small step sizes.

Hint.The method conserves exactly $I ( p , q ) = ( \alpha + p ) ( \beta + q ) .$ Find linear twoterm recursions for $\left\{ p _ { n } \right\}$ and $\left\{ q _ { n } \right\}$ ,anduse the ideas ofExample1.4.Result.

$$
\widetilde { H } ( p , q ) = H ( p , q ) - \sum _ { k \geq 1 } { \frac { h ^ { k } I ( p , q ) ^ { - k } } { k ( k + 1 ) } } .
$$

7.Compute $\partial _ { b } c ( \tau )$ for the tree $\tau = [ [ \tau ] , \tau ]$ of order4.

8.For the implicit midpoint rule compute the coefficients $a ( \tau )$ of theexpansion (9.1),and alsoa few coefficients $b ( \tau )$ of the modified equation.

Result. $a ( \tau ) = 2 ^ { 1 - | \tau | } , \ b ( \bullet ) = 1 , \ b ( \pmb { \mathring { \tau } } ) = 0 , \ b ( \tau ) = a ( \tau ) - 1 / \gamma ( \tau )$ for $| \tau | = 3$ .

9.Check the formulas of Table 9.1.

10.Considera differential equation $\dot { y } = f ( y )$ withadivergence-free vector feld, andapplya volume-preserving integrator.Show that every truncation of the modified equation hasagain adivergence-freevectorfield. Hint.Adapt the proofby induction of Theorems 2.3and 3.1.

11.Consider explicit 2-stage Runge-Kutta methods of order2,applied to the pendulum problem $\dot { q } ~ = ~ p$ , $\dot { p } = - \sin q$ With the help of Exercise2compute $f _ { 3 } ( p , q )$ ofthe modified differential equation.Is thereachoice of the free parameter $c _ { 2 }$ ,suchthat $f _ { 3 } ( p , q )$ isaHamiltonian vector field?

12.Findatleast two linear transformations $\rho$ for which the Kepler problem (I.2.2) written asa first order system,is $\rho$ -reversible.

13.Consider the Kepler problem (I.2.2),writtenasa Hamiltonian system (I.1.10) Find constants $M$ and $R$ such that (7.2) holds for all $( p , q ) \in \mathbb { R } ^ { 4 }$ satisfying

$$
\| p \| \leq 2 \qquad \mathrm { a n d } \qquad 0 . 8 \leq \| q \| \leq 1 . 2 .
$$

14.(McLachlan& Zanna 2005).Consider the RATTLE method(Algorithm VII.5.1) applied to the Euler equations(VII.5.1O)of the freerigid body,writen as ${ \dot { y } } = f ( y )$ Provethat themodified differential equation isof theform

$$
\dot { y } = ( 1 + h ^ { 2 } s _ { 2 } ( y ) + h ^ { 4 } s _ { 4 } ( y ) + \ldots ) f ( y ) ,
$$

where the scalar functions $s _ { k } ( y )$ depend on $_ y$ onlyvia the Casimir function $C ( y ) = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ and the Hamiltonian $\begin{array} { r } { H ( y ) = \frac { 1 } { 2 } ( y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 } ) } \end{array}$ . Consequently,all $s _ { k } ( y )$ are constant along solutions of the Euler equations.

Hint. Since $C ( y )$ and $H ( y )$ areexactly conserved by the numerical method (see Sect.VI.5.3),themodified equation isa time transformation of the original system.The special form of the functions $s _ { k } ( y )$ follows from the fact that RATTLEisaPoisson integrator(TheoremVII.5.11）and fromatransformation to canonical form asin Theorem3.5.

15.(Murua 1999).Let $\varPhi _ { h } ( y ) = B ( a , y )$ be givenbya B-series and denote with i $b ( \tau )$ thecoefficients of the corresponding modified differential equation, cf. formula(9.4).Prove that thecoefficients of the $_ { n }$ thiterate $\begin{array} { r } { \begin{array} { r } { \varPhi _ { h } ^ { n } ( y ) = B ( a ^ { n } , y ) } \end{array} } \end{array}$ satisfy

$$
a ^ { n } ( \tau ) = n b ( \tau ) + n ^ { 2 } c ( \tau , n ) ~ , ~ \mathrm { f o r } ~ \tau \in T ,
$$

where $c ( \tau , n )$ isa polynomial of degree $\vert \tau \vert - 2$ in ${ \boldsymbol { n } }$ ,

Hint.This follows from the Taylor series $\begin{array} { r } { \widetilde { y } ( n h ) = \widetilde { y } ( 0 ) + n h \widetilde { y } ^ { \prime } ( 0 ) + \dots , } \end{array}$ for the solution of the modified differential equation.

16.With the help of Exercise 15,givean alternative proof of Theorem 9.3.

Hint.If $B ( \boldsymbol { a } , \boldsymbol { y } )$ is symplectic,also $B ( a ^ { n } , y )$ is symplectic and its coefficients thus satisfy(VI.7.4).

17.(Murua 1997).Find a one-to-one correspondence between the equivalence classes of $T P$ (corresponding to $\sim$ ofDefinition 10.7)and orientedfreetrees (i.e.,treeswithout a distinguished vertex (root),but with oriented edges),see Fig.11.1.

![](images/a68ad2c769ee05bae79af8558e9cfe704fe2848700d44dcdd6d912a7c3b03d1c.jpg)  
Fig.11.1.Oriented free trees up to order four

# Chapter X. Hamiltonian Perturbation Theory and Symplectic Integrators

Perturbation theoryisin fact an outgrowth of thenecessity todetermine the orbitswith ever greater accuracy.Thisproblem can besolved today, butinwhat is for the theoreticianarather disappointingway.With modern calculating machines,one is now ableto compute directlyresults even moreaccurately than those provided byperturbation theory.

(J.Moser 1978)

...allows computer prediction of planetary positions far more accurate (bybrute computation） than anything providedby classical perturbation theory.Inavery real sense,one of themost exhalted of human endeavors, goingback to the priests of Babylonand before,has been taken over by themachine. （S.Sternberg 1969)

In this chapter we study the long-time behaviour of symplectic integrators,combiningbackward error analysisand the perturbation theory of integrable Hamiltonian systems.

backward   
modified erroranal. numerical   
problem solution numerical method error？ original exact problem solution perturbation theory ierror？ 1   
approximate approximate problem solution

During the18th and 19th centuries,scientists struggled for the integration of complicated problems of dynamics,with the main aim of solving them analytically by "quadrature".But only fewproblems could be treated successfully in thisway.In cases where the original problem could not be solved,much effort was put into replacing itbyan integrableapproximateproblem,byusinganddevelopingperturbation theory.Thereby,aricharsenal ofvery ingenuous theorieshas beendiscovered since the 19th century.

In the1960s and 197Os,the enormousprogress of“calculating machines”and numerical software allowedmany of the original problems to be solved with extreme accuracy,so that for the first time numerical integration methods superseded analytical perturbation methods in the computations ofcelestial mechanics(see theabove citations).Since then,the further increasein computing speed has allowed problems tobetreated on larger and larger time scales,where huge amounts of errors areaccumulated and need to be understood and controlled.In the spirit of backward error analysis,thesenumerical errorsare interpretedas thoseofamodified problem,for the study of which perturbation theory is once again the appropriate tool.

# X.1 Completely Integrable Hamiltonian Systems

Integrable Hamiltonian systemswere originally of interest because their equations of motion can be solved analytically.Their interest in the present context lies in the fact that their flow is simply uniform motion on a Cartesian product of circles and straight lines insuitable coordinates,and that manyphysical systemscan be viewed as perturbations of integrable systems.

# X.1.1 Local Integration by Quadrature

M.Liouvillea fait voir qu’il fallait que toutes lescombinaisons $( \alpha , \beta )$ desintegrales trouvees fussent nulles. (E.Bour1855）

One of the great dreams of 18th and 19th century analytical mechanics was to solve theequations of motion of mechanical systems by“quadrature”,that is,using only evaluations and inversions of functions and calculating integrals ofknown functions. Inthis spirit,Newton's（1687)equations ofmotion of Kepler's two-body problem weresolved by Joh.Bernoulli(1710)and Newton(1713),see Sect.I.2.2.Euler's (1760) solution of the problem of the attraction of aparticle by two fixed centres, andLagrange's（1766) study of motion ofa particle ina field with one attracting centreand under an additional constant force were amongthe important achievementsof the 18th century.The three-bodyproblem,however,resistedall efforts aimingatan integration by quadrature,and though it continued todoso,thisproblemspurred thedevelopment of extremely useful mathematical theories ofamuch widerscope throughout the 19th century,from Poisson to Poincarévia Hamilton,Jacobi,Liouville,to name buta few of the most eminent mathematicians contributing to analytical mechanics.

Consider the Hamiltonian system

$$
\dot { p } = - \frac { \partial H } { \partial q } ( p , q ) , \quad \dot { q } = \frac { \partial H } { \partial p } ( p , q ) ,
$$

with $d$ degrees of freedom: $( p , q ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ We trytofindasymplectic transformation $( p , q ) \mapsto ( x , y )$ ,such that the system hasamore amenable formin thenew coordinates.In particular,thisis the case if the Hamiltonian expressed in the new variables,

$$
H ( p , q ) = K ( x ) ,
$$

does not depend on $_ y$ .Since $\begin{array} { l } { { \frac { \partial K } { \partial y } } \equiv 0 } \\ { . } \end{array}$ ,thetransformedsystemthen becomes (recall the conservation of the Hamiltonian form of the differential equations under symplectic transformations,Theorem VI.2.8)

$$
\dot { x } = 0 , \dot { y } = \omega ( x ) ,
$$

with $\begin{array} { r } { \omega ( x ) = \frac { \partial K } { \partial x } ( x ) . } \end{array}$ This is readilyintegated:

$$
x ( t ) = x _ { 0 } \ , \quad y ( t ) = y _ { 0 } + \omega ( x _ { 0 } ) t \ .
$$

Aswerecall from Sect.VI.5,a symplectic transformation $( p , q ) \mapsto ( x , y )$ canbe constructed viaageneratingfunction $S ( x , q )$ by the equations

$$
y = { \frac { \partial S } { \partial x } } ( x , q ) _ { \ast } \quad p = { \frac { \partial S } { \partial q } } ( x , q ) .
$$

If $( p _ { 0 } , q _ { 0 } )$ and $( x _ { 0 } , y _ { 0 } )$ arerelatedby(1.4),andif $\partial ^ { 2 } S / \partial x \partial q$ is invertible at $( x _ { 0 } , q _ { 0 } )$ ， then the equations(1.4)definea symplectic transformation between neighbourhoods of $( p _ { 0 } , q _ { 0 } )$ and $( x _ { 0 } , y _ { 0 } )$ .

The equation(1.2)together with the second equation of(1.4） giveapartial differential equation for $S$ ,theHamilton-Jacobiequation

$$
H \Bigl ( \frac { \partial S } { \partial q } ( x , q ) , q \Bigr ) = K ( x ) .
$$

If $S ( x , q )$ isa solution of such an equation (for some function $\boldsymbol { \kappa }$ ,then（1.3）shows that $x _ { i } = F _ { i } ( p , q )$ ( $i = 1 , \ldots , d )$ as given implicitly by the second equation of(1.4), arefirst integrals of the Hamiltonian system(1.1).Moreover,these functions $F _ { i }$ are ininvolution,which means that their Poisson brackets vanish pairwise:

$$
\{ F _ { i } , F _ { j } \} = 0 , \quad i , j = 1 , \ldots , d .
$$

This is an immediate consequence of the definition $\left\{ F , G \right\} = \nabla F ^ { T } J ^ { - 1 } \nabla G$ ofthe Poisson bracket and of the symplecticity of the transformation (the left upper block of $J ^ { - 1 }$ is $_ 0$ ).

Conversely,itwasrealized byBour(1855) andLiouville(1855)thataHamiltonian system having $d$ first integralsin involution can locally be transformed to the form(1.3）by“quadrature".This observationis based on the following completion resultand its proof.

Lemma 1.1 (Liouville Lemma). Let $F _ { 1 } , \ldots , F _ { d }$ be smooth real-valued functions, definedinaneighbourhoodof $( p _ { 0 } , q _ { 0 } ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ Suppose that these functions arein involution(i.e.,all Poisson brackets $\{ F _ { i } , F _ { j } \} = 0$ ),andthat their gradients are linearly independentat $( p _ { 0 } , q _ { 0 } )$ Then,thereexist smoothfunctions $G _ { 1 } , \ldots , G _ { d } ,$ defined on some neighbourhoodof $( p _ { 0 } , q _ { 0 } )$ ,suchthat

$$
( F _ { 1 } , . . . . , F _ { d } , G _ { 1 } , . . . , G _ { d } ) : ( p , q ) \mapsto ( x , y ) { \mathrm { \it ~ i s ~ a ~ s y m p l e c t i c ~ t r a n s f o r m a t i o n . } }
$$

Proof.Let $F = ( F _ { 1 } , \dots , F _ { d } ) ^ { T } .$ The linear independence of the gradients $\nabla F _ { i }$ implies that there are $d$ columns of the $d \times 2 d$ Jacobian $\partial { \cal F } / \partial ( p , q )$ that form an invertible $d { \times } d$ submatrix.After some suitable symplectic transformations (see Exercise1) wemay assumewithout loss of generality that $F _ { p } = \partial F / \partial p$ isinvertible.By the implicit function theorem,we can then locally solve $x = F ( p , q )$ for $p$ :

$$
p = P ( x , q ) \mathrm { w i t h \ p a r t i a l \ d e r i v a t i v e s } P _ { x } = F _ { p } ^ { - 1 } , P _ { q } = - F _ { p } ^ { - 1 } F _ { q } .
$$

The condition that the $F _ { i }$ areininvolution,reads in matrix notation

$$
F _ { p } F _ { q } ^ { T } - F _ { q } F _ { p } ^ { T } = 0 .
$$

Multiplyingthisequation with $F _ { p } ^ { - 1 }$ from the left and with $F _ { p } ^ { - T }$ from the right, we obtain

$$
- P _ { q } ^ { T } + P _ { q } = 0 ,
$$

so that $P _ { q } = \partial P / \partial q$ issymmetric.By the Integrability Lemma VI.2.7, $P ( x , q )$ is thus locally the gradient with respect to $q$ ofsome function $S ( x , q )$ （which is constructedbyquadrature).Moreover $\begin{array} { r } { \frac { \partial ^ { 2 } S } { \partial x \partial q } = P _ { x } = F _ { p } ^ { - 1 } } \end{array}$ is invertible.Theequations(1.4) define a symplectic transformation $( p , q ) \mapsto ( x , y )$ ,and by construction $x = F ( p , q )$ □

If,ina Hamiltonian system with $d$ degrees of freedom,we can find $d$ independent first integralsin involution $H \ = \ F _ { 1 } , F _ { 2 } , \ldots , F _ { d }$ ,thenLemma1.1yields asymplectic change of coordinates,constructed by quadrature,which transforms (1.1) locally to(1.2)with $K ( x _ { 1 } , \ldots , x _ { d } ) = x _ { 1 }$

Example1.2. Consider the Hamiltonian of motion in a central field,

$$
\begin{array} { r } { H = \frac { 1 } { 2 } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) + V ( r ) \quad \mathrm { ~ f o r ~ } r = \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } , } \end{array}
$$

with a potential $V ( r )$ thatisdefinedand smooth for $r > 0$ .TheKeplerproblem corresponds to the special case $V ( r ) = - 1 / r$ ,and the perturbed Kepler problem to $V ( r ) = - 1 / r - \mu / ( 3 r ^ { 3 } )$ Changing to polar coordinates (see Example VI.5.2）

$$
{ \binom { q _ { 1 } } { q _ { 2 } } } = { \binom { r \cos \varphi } { r \sin \varphi } } \ , \quad { \binom { p _ { r } } { p _ { \varphi } } } = { \binom { \cos \varphi } { - r \sin \varphi } } \ \sin \varphi \ { \binom { p _ { 1 } } { p _ { 2 } } } \ ,
$$

this becomes

$$
H ( p _ { r } , p _ { \varphi } , r , \varphi ) = \frac { 1 } { 2 } \Big ( p _ { r } ^ { 2 } + \frac { p _ { \varphi } ^ { 2 } } { r ^ { 2 } } \Big ) + V ( r ) .
$$

The system has the angular momentum $L = p _ { \varphi }$ asa first integral, since $H$ does not depend on $\varphi$ .Clearly, $\{ H , L \} = 0$ everywhere.The gradients of $H$ and $L$ are linearly independent unless both $p _ { r } = 0$ and $p _ { \varphi } ^ { 2 } = r ^ { 3 } V ^ { \prime } ( r )$ Byinserting $p _ { \varphi } ^ { 2 } =$ $2 r ^ { 2 } ( H - V ( r ) )$ andeliminating $r$ this becomes a condition of the form $\alpha ( H , L ) = 0$ , which for the Kepler problemreads explicitly $L ^ { 2 } ( 1 + 2 H L ^ { 2 } ) = 0 .$ The conditions ofLemma 1.1 are thus satisfied on thedomain

$$
M = \{ ( p _ { r } , p _ { \varphi } , r , \varphi ) \ ; \ r > 0 , \alpha ( H , L ) \neq 0 \} .
$$

The equations $\begin{array} { r } { x _ { 1 } = H = \frac { 1 } { 2 } ( p _ { r } ^ { 2 } + p _ { \varphi } ^ { 2 } / r ^ { 2 } ) + V ( r ) , x _ { 2 } = 1 } \end{array}$ $x _ { 2 } = L = p _ { \varphi }$ can be solved for

$$
p _ { r } = \pm \sqrt { 2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 } } , \quad p _ { \varphi } = L ,
$$

and $p _ { r } = \partial S / \partial r$ ， $p _ { \varphi } = \partial S / \partial \varphi$ with

$$
S ( H , L , r , \varphi ) = L \varphi \pm \int _ { r _ { 0 } } ^ { r } \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } d \rho .
$$

Theconjugate variables are

$$
\begin{array} { l } { { y _ { 1 } ~ = ~ { \displaystyle \frac { \partial S } { \partial H } } = \pm \int _ { r _ { 0 } } ^ { r } { \displaystyle \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } } d \rho } , } \\ { { y _ { 2 } ~ = ~ { \displaystyle \frac { \partial S } { \partial L } } = \varphi \mp \int _ { r _ { 0 } } ^ { r } { \displaystyle \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } } d \rho . } } \end{array}
$$

This defines (locally) the transformation $( p _ { r } , p _ { \varphi } , r , \varphi ) \mapsto ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) .$ In these variables,the equations of motion read $\dot { x } _ { 1 } = 0$ , $x _ { 2 } = 0$ , ${ \dot { y } } _ { 1 } = 1$ ， $y _ { 2 } = 0$ Overany time interval where $p _ { r } ( t )$ doesnot change sign,solutions therefore satisfy

$$
\begin{array} { r } { t _ { 1 } - t _ { 0 } = \pm \int _ { r ( t _ { 0 } ) } ^ { r ( t _ { 1 } ) } \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho , } \\ { \varphi ( t _ { 1 } ) - \varphi ( t _ { 0 } ) = \pm \int _ { r ( t _ { 0 } ) } ^ { r ( t _ { 1 } ) } \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho . } \end{array}
$$

# X.1.2 Completely Integrable Systems

Lemma 1.1 appears asapowerful tool foran explicit solution by quadrature.However,because of itspurely local nature this lemma does not tell usanythingabout thedynamicsof the system.Thiswasnot aconcern atLiouville's time,but the first rigorous non-integrability results by Poincaré（1892) put adefinite end to the hope of being eventually able to construct explicit analytic solutions of most equations of motion by quadrature,and shifted theinterest tounderstanding theglobal,qualitativebehaviour of dynamical systems.

Lemma 1.1can beglobalizedbyaprocedure similar toanalytic continuation if the conditions of the following definition are satisfied.

Definition1.3.A Hamiltonian systemwith Hamiltonian $H : M  \mathbb { R }$ $M$ anopen subset of $\mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ ）iscalled completely integrableif thereexistsmooth functions $F _ { 1 } = H , F _ { 2 } , \dots , F _ { d } : M \to \mathbb { R }$ with the following properties:

1） $F _ { 1 } , \ldots , F _ { d }$ arein involution (i.e.,all $\{ F _ { i } , F _ { j } \} = 0$ on $M$ . 2）The gradients of $F _ { 1 } , \ldots , F _ { d }$ arelinearlyindependentatevery pointof $M$ . 3）The solution trajectories of the Hamiltonian systems with Hamiltonian $F _ { i }$ $i =$ $1 , \ldots , d )$ exist forall timesand remain in $M$

Obviously,all the Hamiltonian systems with Hamiltonian $F _ { i }$ $i = 1 , \ldots , d )$ are thencompletely integrable,and so therewill benomathematical reasonto further distinguish $H = F _ { 1 }$ .Wenote thatcondition(1）ofDefinition1.3impliesthatall $F _ { j }$ arefirst integrals of the Hamiltonian systemwith Hamiltonian $F _ { i } ,$ and that theflows $\varphi _ { t } ^ { [ i ] }$ of theseHamiltoniansystemscommute: $\varphi _ { t } ^ { [ i ] } \circ \varphi _ { s } ^ { [ j ] } = \varphi _ { s } ^ { [ j ] } \circ \varphi _ { t } ^ { [ i ] }$ forall $i , j$ and all $t , s \in \mathbb { R }$ ;seeLemmaVII.3.2.

For $x = ( x _ { i } ) \in \mathbb { R } ^ { d }$ wedefine the level set

$$
M _ { x } = \{ ( p , q ) \in M ; \ F _ { i } ( p , q ) = x _ { i } \ { \mathrm { ~ f o r ~ } } i = 1 , \ldots , d \} .
$$

Theorem1.4. Suppose that $F _ { 1 } , \dots , F _ { d } : M \to \mathbb { R }$ satisfy the conditions of Definition1.3.Assume that $M _ { x }$ isconnected(andnon-empty)for al $x$ inaneighbourhood of $\boldsymbol { x } _ { 0 } \in \mathbb { R } ^ { d }$ .Then,onsome neighbourhood $B$ of $x _ { 0 }$ ,thereexistsasymplectic and surjective mapping

$$
e : B \times \mathbb { R } ^ { d } \to \bigcup _ { x \in B } M _ { x } : ( x , y ) \mapsto ( p , q ) \in M _ { x }
$$

that linearizes,forall $i = 1 , \ldots , d$ theflow $\varphi _ { t } ^ { [ i ] }$ ofthesystemwithHamiltonian $F _ { i }$

$$
\begin{array} { r } { { i f } ( p , q ) = e ( x , y ) , \quad t h e n \quad \varphi _ { t } ^ { [ i ] } ( p , q ) = e ( x , y + t e _ { i } ) , } \end{array}
$$

where $e _ { i } = ( 0 , \ldots , 1 , \ldots , 0 ) ^ { T }$ is the ith unit vector of $\mathbb { R } ^ { d }$ .

Since $e$ is symplectic, $e$ isalocal diffeomorphism.Itslocal inverse isa transformation as constructed inLemma 1.1.However, $( p , q )$ canhave countablymany discretely lying pre-images $( x , y )$ ,sothat $e ^ { - 1 }$ becomesa multi-valued function. The situation is analogous to that of the complex exponential and logarithm.The following example illustrates that thisanalogy is not incidental.

Example1.5.Considerthe harmonic oscillator,i.e., $d = 1$ and $\begin{array} { r } { H ( p , q ) = \frac 1 2 ( p ^ { 2 } + } \end{array}$ $q ^ { 2 }$ ).For $\begin{array} { r } { x = { \frac { 1 } { 2 } } r ^ { 2 } } \end{array}$ ,wehave $e ( x , y ) = ( r \cos y , r \sin y ) ,$

ProofofTheorem1.4.Wefix $( p _ { 0 } , q _ { 0 } ) \in M _ { x _ { 0 } }$ ,andinaneighbourhood $U$ of $( p _ { 0 } , q _ { 0 } )$ weconsiderasymplectic transformation

$$
\ell = ( F _ { 1 } , \dots , F _ { d } , G _ { 1 } , \dots , G _ { d } ) : ( p , q ) \mapsto ( x , y )
$$

as constructed in Lemma 1.1.We have $\ell ( p _ { 0 } , q _ { 0 } ) = ( x _ { 0 } , y _ { 0 } )$ where we may assume $y _ { 0 } = 0 .$ Toevery $v = ( v _ { i } ) \in \mathbb { R } ^ { d }$ we associate the Hamiltonian

$$
F _ { v } = v _ { 1 } F _ { 1 } + \ldots + v _ { d } F _ { d }
$$

andnotethat,becauseofthecommutativityofthefows $\varphi _ { t } ^ { [ i ] }$ ,theflow of the system with Hamiltonian $F _ { v }$ equals

$$
\varphi _ { t v } = \varphi _ { t v _ { 1 } } ^ { [ 1 ] } \circ \ldots \circ \varphi _ { t v _ { d } } ^ { [ d ] } .
$$

In the neighbourhood $U$ of $( p _ { 0 } , q _ { 0 } )$ ,the systemwith Hamiltonian $F _ { v }$ is transformed underthe symplectic mapping $\ell$ to

$$
\dot { x } = 0 , \quad \dot { y } = v .
$$

Hence,the following diagram commutes for $( p , q ) \in U$ and forsufficiently small $t v$

$$
\begin{array} { r l r } { ( p , q ) } & { { } \longrightarrow } & { \varphi _ { t v } ( p , q ) } \\ { \Big \downarrow \ell } & { { } } & { \Big \uparrow \ell ^ { - 1 } } \\ { ( x , y ) } & { { } \longrightarrow } & { ( x , y + t v ) } \end{array}
$$

Wenow construct $e$ byextending this diagram toarbitrary tu:

$$
\begin{array} { r l r } { ( p , q ) \quad } & { { } \longrightarrow } & { \varphi _ { y } ( p , q ) } \\ { { \hat { \Bigg \uparrow } } \ell ^ { - 1 } \quad } & { { } } & { } \\ { ( x , 0 ) \quad } & { { } \longleftarrow \quad } & { ( x , y ) } \end{array}
$$

That is,we define on $B \times \mathbb { R } ^ { d }$ (with $B$ aneighbourhood of $x _ { 0 }$ on which $\ell ^ { - 1 } ( x , 0 )$ is defined)

$$
e ( x , y ) = \varphi _ { y } \bigl ( \ell ^ { - 1 } ( x , 0 ) \bigr ) .
$$

For $( x , y )$ near some fixed $( \widehat { x } , \widehat { y } )$ ,we have by(1.10)with $y - \hat { y }$ and $\hat { y }$ instead of $y$ and $t v$ that

$$
e ( x , y ) = \varphi _ { \hat { y } } ( \ell ^ { - 1 } ( x , y - \widehat { y } ) ) \ ,
$$

which shows that $e$ issymplectic,being locally the composition of symplectic transformations.Theproperty(1.9)isobvious fromthedefinition of $e$ and from the comfows mutativity of the flows $\varphi _ { t } ^ { [ i ] }$ ,we have $e ( x , y ) \in M _ { x }$ $\varphi _ { t } ^ { [ i ] }$ Since foral $\ell ^ { - 1 } ( x , 0 ) \in M _ { x }$ $( x , y )$ and $M _ { x }$ is invariant under the

Itremains to show that $e : \{ x \} \times \mathbb { R } ^ { d } \to M _ { x }$ is surjective for every $x$ near $x _ { 0 }$ .Let $( \widehat { \boldsymbol { p } } , \widehat { \boldsymbol { q } } )$ beanarbitrary point on $M _ { x }$ Byassumption,there existsapath on $M _ { x }$ connecting $\ell ^ { - 1 } ( x , 0 )$ and $( \widehat { \boldsymbol { p } } , \widehat { \boldsymbol { q } } )$ .Moreover,by(1.10)andby the compactness of the path,there is a $\delta > 0$ such that,for every $( p , q )$ on this path,the mapping $y \mapsto \varphi _ { y } ( p , q )$ isadiffeomorphism between the ball $\| y \| < \delta$ andaneighbourhoodof $( p , q )$ on $M _ { x }$ .Therefore, $( \widehat { p } , \widehat { q } )$ can bereached from $\ell ^ { - 1 } ( x , 0 )$ byafinite composition of maps:

$$
( { \widehat { p } } , { \widehat { q } } ) = \varphi _ { y ^ { ( m ) } } \circ . . . \circ \varphi _ { y ^ { ( 1 ) } } ( \ell ^ { - 1 } ( x , 0 ) ) = \varphi _ { \widehat { y } } ( \ell ^ { - 1 } ( x , 0 ) ) = e ( x , { \widehat { y } } ) \ ,
$$

where $\widehat { y } = y ^ { ( 1 ) } + \ldots + y ^ { ( m ) }$ onceagainbythecommutativityoftheflows $\varphi _ { t } ^ { [ i ] }$ □

Illustration of the Liouville Transform.We illustrate the above construction at a simpleexample,thependulum(I.1.12）withHamiltonian $H = p ^ { 2 } / 2 - \cos q .$ The first coordinate is $x = H ( p , q )$ ,afirst integral.The secondcoordinate $y$ is,following (1.11),thetime $t$ whichis necessary to reach the point $( p , q )$ from an initial line, which we assume at $q = 0$ Thenwehave(Fig.1.1left) $d p d q = d H d t$ (because

$$
d p \frac { 1 ^ { p } } { \left[ \begin{array} { c c c c c } { d q } & { \cdots } & { \mathbf { \hat { ( A ) } } } & { \mathbf { \hat { ( A ) } } } & { \mathbf { \hat { ( C ) } } } & { \mathbf { \hat { ( B ) } } } & { \mathbf { \Huge \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge ( C ) } } \\ { d q ^ { \mathrm { ~ 2 ~ } } \cdots \cdots \sum _ { \mathbf { \hat { 2 } } } } & { \cdots } & { d H \frac { 1 ^ { \mathrm { ~ ~ 2 ~ } } } { \left[ \begin{array} { c c c c c } { d t } & { \cdots } & { \cdots } & { \mathbf { \Huge ( B ) } } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge ( C ) } } \\ { d t } & { \cdots } & { \mathbf { \Huge ( C ) } } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } \end{array} \right] } } \end{array} \right] }
$$

Fig.1.1.Liouvilleand action-angle coordinate transforms

of $d q \ = \ H _ { p } d t$ and $d H = H _ { p } d p )$ We see again that we have area preservation, because the symplecticity of theflow preserves thisproperty for all times.This symplectic change ofcoordinates $( p , q ) \mapsto ( x , y )$ isillustrated inFig.1.2,which transforms theproblem（A） toa much simpler form(B）withuniform horizontal movement.

![](images/ad67da2f38da5a41c0664e84dfc202b32541d72e9f9eab03881b248ffd7d287d.jpg)  
Fig.1.2.Liouvilleand action-angle coordinates illustratedat thependulumproblem

Weare not yet completely satisfied,however,because the orbits have periods $g = g ( H )$ whichare not all the same.We thereforeappenda second transform by putting $\begin{array} { r } { \theta = \frac { 2 \pi } { g } \cdot t } \end{array}$ (seepicture(C)inFig.1.1andFig.1.2),which forcesallperiods intoaProcrustean bed of length $2 \pi$ Areapreservation $d a d \theta = d H d$ tnowrequires that $2 \pi d a = g ( H ) d H$ ,which isadifferential equation between $a$ and $H .$ Thenew coordinates $( a , \theta )$ aretheaction-angle variablesand we see that they transform the phase space into $D \times \mathbb { T } ^ { 1 }$ where $D \subset \mathbb { R } ^ { 1 }$ Weagain have horizontal movement,but this time the speed depends on $\boldsymbol { a }$ Thegeneral existence forcompletely integrable systemswill be proved in Theorem 1.6below.

# X.1.3Action-Angle Variables

Weshow here that,under the hypotheses ofLiouville's theorem,we can findsymplectic coordinates $( \mathbb { I } , \varphi )$ such that the first integrals $\mathbf { F }$ depend onlyon I,and $\varphi$ are angular coordinates on the torus $M _ { \mathrm { f } }$ ,

(V.I.Amold1989,p.279)

Weare now in the position to prove the main result of this section,which establishes asymplecticchange ofcoordinates to the so-called action-angle variables,such that $d$ firstintegrals of acompletely integrable system depend only on the actions,and theanglesaredefined globally mod $2 \pi$ (provided the level sets of the frst integrals arecompact).This isknown as the Arnold-Liouville theorem;cf.Arnold（1963, 1989),Arnold,Kozlov&Neishtadt（1997;Ch.4,Sect.2.1),Jost(1968).Here and in the following,

$$
\mathbb { T } ^ { d } = \mathbb { R } ^ { d } / 2 \pi \mathbb { Z } ^ { d } = \{ ( \theta _ { 1 } \bmod { 2 \pi } , \ldots , \theta _ { d } \bmod { 2 \pi } ) ; \theta _ { i } \in \mathbb { R } \}
$$

denotes the standard $d$ -dimensional torus.

Theorem 1.6 (Arnold-Liouville Theorem).Let $F _ { 1 } , \dots , F _ { d } ~ ; ~ M \to \mathbb { R }$ befirst integralsofacompletely integrable systemasin Definition1.3.Suppose that the levelsets $M _ { x }$ (see(1.8)) are compact and connected for all $x$ inaneighbourhood of $x _ { 0 } \in \mathbb { R } ^ { d }$ .Then,thereareneighbourhoods $B$ of $x _ { 0 }$ and $\mathcal { D }$ of $_ 0$ in ${ \mathbb R } ^ { d }$ suchthat thefollowing holds:

(i）Forevery $x \in B$ ,thelevelset $M _ { x }$ isa $d$ -dimensionaltorusthatisinvariant undertheflowofthe systemwith Hamiltonian $F _ { i }$ $i = 1 , \ldots , d ,$ ).

(ii)Thereexistsabijective symplectic transformation

$$
\psi : D \times \mathbb { T } ^ { d } \longrightarrow \bigcup _ { x \in B } M _ { x } \subset \mathbb { R } ^ { d } \times \mathbb { R } ^ { d } : ( a , \theta ) \longmapsto ( p , q )
$$

suchthat $( F _ { i } \circ \psi ) ( a , \theta )$ depends only on a,i.e.,

$$
F _ { i } ( p , q ) = f _ { i } ( a ) \quad f o r \quad ( p , q ) = \psi ( a , \theta ) \qquad ( i = 1 , \dots , d )
$$

with functions $f _ { i } : D \to \mathbb { R }$ .

Thevariables $( a , \theta ) \ = \ ( a _ { 1 } , \ldots , a _ { d } , \theta _ { 1 }$ mod $2 \pi , \ldots , \theta _ { d }$ mod $2 \pi$ ）arecalled action-anglevariables.

Remark 1.7.If thelevel sets $M _ { x }$ arenot compact,then theproof of Theorem1.6 showsthat $M _ { x }$ isdiffeomorphic toa Cartesian product of circles and straight lines $\mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k }$ forsome $k < d$ ,andthereisa bijective symplectic transformation $( a , \theta ) \mapsto ( p , q )$ between $D \times ( \mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k } )$ andaneighbourhood $\bigcup \{ M _ { x } : x \in B \}$ of $M _ { x _ { 0 } }$ such that the first integrals again depend only on $a$

Remark 1.8.If the Hamiltonian is real-analytic,then the proof shows thatalso the transformationtoaction-anglevariablesisreal-analytic.

ProofofTheorem1.6.(a)WereturntoTheorem1.4.For $x \in B$ ,weconsider the set

$$
\begin{array} { r } { T _ { x } = \left\{ y \in \mathbb { R } ^ { d } ; e ( x , y ) = e ( x , 0 ) \right\} . } \end{array}
$$

Since $e$ is locallyadiffeomorphism,foreveryfixed $y _ { 0 } \invarGamma _ { x _ { 0 } }$ there exists a unique smooth function $\eta$ defined on aneighbourhoodof $\scriptstyle { \mathcal { X } } 0$ ,suchthat $\eta ( x _ { 0 } ) = y _ { 0 }$ and $\eta ( x ) \in T _ { x }$ for $_ { x }$ near $x _ { 0 }$ .Inparticular, $T _ { x }$ isadiscrete subset of $\mathbb { R } ^ { d }$ By（1.9）, for $y \in \mathcal { I } _ { x }$ wehave $e ( x , y + v ) = e ( x , v )$ forall $\boldsymbol { v } \in \mathbb { R } ^ { d }$ .Therefore, $T _ { x }$ isa subgroup of $\mathbb { R } ^ { d }$ ,i.e.,with $y , v \in I _ { x } ^ { \prime }$ also $y + v \in I _ { x }$ and $- y \in I _ { x } .$ It then follows (see Exercise 4） that $\varGamma _ { x }$ isagrid,generated by $k \leq d$ linearly independent vectors $g _ { 1 } ( x ) , \ldots , g _ { k } ( x ) \in \mathbb { R } ^ { d }$

$$
\Gamma _ { x } = \{ m _ { 1 } g _ { 1 } ( x ) + . . . . + m _ { k } g _ { k } ( x ) ; m _ { i } \in \mathbb { Z } \} .
$$

Weextend $g _ { 1 } ( x ) , \ldots , g _ { k } ( x )$ toabasis $g _ { 1 } ( x ) , \ldots , g _ { d } ( x )$ of $\mathbb { R } ^ { d }$ Then, $e$ inducesa diffeomorphism

$$
\begin{array} { r c l } { \mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k } } & { \to } & { M _ { x } } \\ { ( \theta _ { 1 } , \dots , \theta _ { k } , \tau _ { k + 1 } , \dots , \tau _ { d } ) } & { \mapsto } & { e \Big ( x , \displaystyle \sum _ { i = 1 } ^ { k } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x ) + \displaystyle \sum _ { j = k + 1 } ^ { d } \tau _ { j } g _ { j } ( x ) \Big ) . } \end{array}
$$

If $M _ { x }$ is compact,then necessarily $k = d$ and $M _ { x }$ isa torus.The above map then becomes the bijection

$$
\mathbb { T } ^ { d } \to M _ { x } : \theta \mapsto e \Big ( x , \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x ) \Big ) ~ .
$$

(b)Next we show that $g _ { i } ( x )$ is the gradient of some function $U _ { i } ( x )$ Fornotational convenience,we omit the subscript $i$ and consideradifferentiable function $g$ with

$$
e ( x , g ( x ) ) = e ( x , 0 ) , \qquad x \in B ,
$$

or equivalently,

$$
\ell \circ e ( x , g ( x ) ) = ( x , 0 ) , \qquad x \in B .
$$

Differentiating thisrelation gives （with $I$ the $d$ -dimensional identity)

$$
A \left( \begin{array} { c } { { I } } \\ { { g ^ { \prime } ( x ) } } \end{array} \right) = \left( \begin{array} { l } { { I } } \\ { { 0 } } \end{array} \right)
$$

where $A$ is the Jacobian matrix of $\ell \circ e$ at $( x , g ( x ) )$ Wethushave

$$
( I ~ g ^ { \prime } ( x ) ^ { T } ) A ^ { T } J A \left( ~ \begin{array} { c } { { I } } \\ { { g ^ { \prime } ( x ) } } \end{array} \right) = ( I ~ 0 ) J \left( ~ \begin{array} { c } { { I } } \\ { { 0 } } \end{array} \right) = 0 .
$$

Since $\ell \circ e$ isa symplectic transformation,we have $A ^ { T } J A = J$ ,and hence the above equation reduces to

$$
g ^ { \prime } ( x ) ^ { T } - g ^ { \prime } ( x ) = 0 .
$$

BytheIntegrabilityLemmaVI.2.7,thereisafunction $U$ such that $g ( x ) = \nabla U ( x ) .$ We may assume $U ( x _ { 0 } ) = 0$

(c)The resultof(b)allowsus to extend the bijection of (a） toa symplectic transformation.For this,we consider the generating function

$$
S ( x , \theta ) = \sum _ { i = 1 } ^ { d } { \frac { \theta _ { i } } { 2 \pi } } U _ { i } ( x ) .
$$

With $u ( x ) = \left( U _ { 1 } ( x ) , . . . , U _ { d } ( x ) \right)$ ,the mixed second derivative of $S$ is

$$
S _ { x \theta } ( x , \theta ) = \frac { 1 } { 2 \pi } u _ { x } ( x ) = \frac { 1 } { 2 \pi } \Big ( g _ { 1 } ( x ) , . . . , g _ { d } ( x ) \Big ) ,
$$

which is invertible because of the linear independence of the $g _ { i }$ Theequations

$$
a = \frac { \partial S } { \partial \theta } = \frac { 1 } { 2 \pi } u ( x ) , \quad y = \frac { \partial S } { \partial x } = \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x )
$$

definea bijective symplectic transformation (for some neighbourhood $D$ of $0$ ,and possiblywith areduced neighbourhood $B$ of $x _ { 0 }$ )

$$
\beta : D \times \mathbb { R } ^ { d } \to B \times \mathbb { R } ^ { d } : ( a , \theta ) \mapsto ( x , y ) = \left( f ( a ) , \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( f ( a ) ) \right)
$$

where $x = f ( a )$ is the inverse map of $\begin{array} { r } { a = \frac { 1 } { 2 \pi } u ( x ) . } \end{array}$ We now define

$$
\widehat { \psi } = e \circ \beta : D \times \mathbb { R } ^ { d } \to \bigcup _ { x \in B } M _ { x } .
$$

Byconstruction,this mapis smooth and symplectic,and such that $f _ { i } ( a ) = x _ { i } =$ $F _ { i } ( p , q )$ for $( p , q ) = \widehat { \psi } ( a , \theta )$ ItissurjectivebyTheorem1.4.By part (a) of this proof,it becomes injectivewhen the $\theta _ { i }$ aretaken mod $2 \pi$ ,thusyieldinga transformation $\psi$ defined on $D \times  { \mathbb { T } } ^ { d }$ with the stated properties. □

# X.1.4 Conditionally Periodic Flows

Animmediate and important consequence of Theorem 1.6 is the following.

Corollary 1.9.Inthe situationofTheorem1.6,consider thecompletely integrable systemwith Hamiltonian $H = F _ { 1 }$ Intheaction-anglevariables $( a , \theta )$ ,theHamiltonianequationsbecome

$$
\dot { a } _ { i } = 0 , \quad \dot { \theta } _ { i } = \omega _ { i } ( a ) \qquad ( i = 1 , \ldots , d )
$$

with $\omega _ { i } ( a ) = \partial K / \partial a _ { i } ( a )$ where $K ( a ) = H ( p , q ) f o r ( p , q ) = \psi ( a , \theta ) .$

Theflow ofadifferential system

$$
\begin{array} { r l r } { \Dot { \theta } = \omega , } & { { } } & { \omega = ( \omega _ { i } ) \in \mathbb { R } ^ { d } } \end{array}
$$

on the torus $\mathbb { T } ^ { d }$ is called conditionally periodic with frequencies $\omega _ { i }$ Theflow is periodic if there exist integers $k _ { i }$ such that for anytwo frequencies the relation $\omega _ { i } / \omega _ { j } =$ $k _ { i } / k _ { j }$ holds.Otherwise,theflowiscalled quasi-periodic.In particular,the latter occurs when the frequencies are rationally independent,or non-resonant:the only integers $k _ { i }$ with $k _ { 1 } \omega _ { 1 } + \ldots + k _ { d } \omega _ { d } = 0$ are $k _ { 1 } = \ldots = k _ { d } = 0$ Fornonresonant frequencies,itiswell known（seeArnold(1989),p.287）that everytrajectory $\{ \theta ( t ) : t \in \mathbb { R } \}$ is dense on the torus $\mathbb { T } ^ { d }$ anduniformly distributed.

![](images/b87f4113ee78594f9f1fb1dd23718137ac8c956c34b81aa67ac873cd05e912ff.jpg)

Example1.10.We takeupagain the example ofmotion inacentral field,Example1.2.For given $H$ and $\mathcal { L }$ ,wenow assume that

$$
\{ r > 0 ; 2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 } > 0 \} = [ r _ { 0 } , r _ { 1 } ]
$$

isanon-empty interval and thederivatives of $2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 }$ are nonvanishingat $r _ { 0 }$ , $r _ { 1 }$ .By(1.7）,themotion from $r _ { 0 }$ to $\tau _ { 1 }$ andback again takesa time $T$ and runs through anangle $\phi$ which are given by

$$
\begin{array} { r c l } { { T } } & { { = } } & { { 2 \displaystyle \int _ { r _ { 0 } } ^ { r _ { 1 } } \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho , } } \\ { { \Phi } } & { { = } } & { { 2 \displaystyle \int _ { r _ { 0 } } ^ { r _ { 1 } } \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho . } } \end{array}
$$

Note that $r _ { 0 }$ , $r _ { 1 }$ , $T$ ， $\boldsymbol { \Phi }$ are functions of $H$ and $\mathcal { L }$ .The solution is periodic if $\boldsymbol { \Phi }$ is arational multipleof $2 \pi$ Thisoccursfor theKeplerproblem,where $\phi = 2 \pi$ and where $T = 2 \pi / ( - 2 H ) ^ { 3 / 2 }$ (for $H < 0$ )depends onlyon $H$ ;see Exercise I.5.

Wenow construct action-angle variables and compute the frequencies of the system.We begin by constructing the mapping $e ( x , y )$ asdefined by（1.11）forthe variables $x = ( x _ { 1 } , x _ { 2 } ) = ( H , L )$ and $y \ = \ ( y _ { 1 } , y _ { 2 } )$ of(1.6）.Foragiven $( x , y )$ ， weconsider $( x , 0 )$ andwe fix $( p , q )$ with $p = ( p _ { r } , p _ { \varphi } )$ and $q = ( r , \varphi )$ such that $\ell ( p , q ) = ( x , 0 )$ ,e.g.,by choosing $r = r _ { 0 }$ , $\varphi = 0$ ， $p _ { r } = 0$ , $p _ { \varphi } = L .$ Themapping $e ( x , y )$ isdefinedby the flowat time $t = 1$ corresponding to the Hamiltonian

$$
F _ { y } = y _ { 1 } H + y _ { 2 } L = y _ { 1 } \Big ( { \textstyle \frac { 1 } { 2 } } ( p _ { r } ^ { 2 } + p _ { \varphi } ^ { 2 } / r ^ { 2 } ) + V ( r ) \Big ) + y _ { 2 } p _ { \varphi } ,
$$

i.e.,by the solution at $t = 1$ of

$$
\begin{array} { l } { { \displaystyle { \dot { p } } _ { r } = - y _ { 1 } \frac { p _ { \varphi } ^ { 2 } } { r ^ { 3 } } - y _ { 1 } V ^ { \prime } ( r ) ~ , \quad { \dot { p } } _ { \varphi } = 0 } } \\ { { \displaystyle { \dot { r } } = y _ { 1 } p _ { r } ~ , \quad { \dot { \varphi } } = y _ { 1 } \frac { p _ { \varphi } } { r ^ { 2 } } + y _ { 2 } . } } \end{array}
$$

If we denote the flow of the original system with Hamiltonian $H ( p _ { r } , p _ { \varphi } , r , \varphi )$ by $\varphi _ { t }$ ,thenwe have

$$
e ( x , y ) = \varphi _ { y _ { 1 } } ( 0 , L , r _ { 0 } , 0 ) + ( 0 , 0 , 0 , y _ { 2 } ) ^ { T }
$$

with the last component taken modulo $2 \pi$ Hence,the values of $y$ satisfying $e ( x , y ) = e ( x , 0 )$ are

$$
y = m _ { 1 } g _ { 1 } ( x ) + m _ { 2 } g _ { 2 } ( x )
$$

with integers $m _ { 1 } , m _ { 2 }$ and

$$
g _ { 1 } = \left( { \begin{array} { c } { T } \\ { - \varPhi } \end{array} } \right) , g _ { 2 } = \left( { \begin{array} { c } { 0 } \\ { 2 \pi } \end{array} } \right) .
$$

Weknow fromtheproof ofTheorem1.6that $g _ { 1 }$ and $g _ { 2 }$ are the gradients of functions $U _ { 1 } ( H , L )$ and $U _ { 2 } ( H , L )$ ,respectively.Clearly, $U _ { 2 } = 2 \pi L .$ The expression for $U _ { 1 }$ is lessexplicit.With theconstruction of the Integrability Lemma VI.2.7,this function isobtained byquadrature,inaneighbourhood of $( H _ { 0 } , L _ { 0 } )$ ,as

$$
\begin{array} { r } { U _ { 1 } ( H , L ) = \displaystyle \int _ { 0 } ^ { 1 } \Big ( \left( H - H _ { 0 } \right) T ( H _ { 0 } + s ( H - H _ { 0 } ) , L _ { 0 } + s ( L - L _ { 0 } ) ) = } \\ { ( L - L _ { 0 } ) \varPhi ( H _ { 0 } + s ( H - H _ { 0 } ) , L _ { 0 } + s ( L - L _ { 0 } ) ) \Big ) d s \ . } \end{array}
$$

(For the Kepler problem, $T = 2 \pi / ( - 2 H ) ^ { 3 / 2 }$ , $\phi = 0$ mod $2 \pi$ ,and hence $U _ { 1 } =$ $2 \pi / { \sqrt { - 2 H } } .$ )For the action variableswe thus obtain

$$
a _ { 1 } = \frac { 1 } { 2 \pi } U _ { 1 } ( H , L ) , \quad a _ { 2 } = L .
$$

Theangle variablesaregiven by $\begin{array} { r } { y = \frac { 1 } { 2 \pi } ( \theta _ { 1 } g _ { 1 } + \theta _ { 2 } g _ { 2 } ) } \end{array}$ ,i.e.,

$$
\theta _ { 1 } = y _ { 1 } \frac { 2 \pi } { T } , \theta _ { 2 } = y _ { 2 } + y _ { 1 } \frac { \Phi } { T } .
$$

Writing the total energy $H = K ( a _ { 1 } , L )$ if $a _ { 1 }$ isgiven bythe above formula,we obtain,bydifferentiation of the identity $2 \pi a _ { 1 } = U _ { 1 } ( K ( a _ { 1 } , L ) , L )$ ,

$$
2 \pi = \frac { \partial U _ { 1 } } { \partial H } \frac { \partial K } { \partial a _ { 1 } } , \quad 0 = \frac { \partial U _ { 1 } } { \partial H } \frac { \partial K } { \partial a _ { 2 } } + \frac { \partial U _ { 1 } } { \partial L }
$$

and hence the frequencies

$$
\omega _ { 1 } = \frac { \partial K } { \partial a _ { 1 } } = \frac { 2 \pi } { T } , \omega _ { 2 } = \frac { \partial K } { \partial a _ { 2 } } = \frac { \varPhi } { T } .
$$