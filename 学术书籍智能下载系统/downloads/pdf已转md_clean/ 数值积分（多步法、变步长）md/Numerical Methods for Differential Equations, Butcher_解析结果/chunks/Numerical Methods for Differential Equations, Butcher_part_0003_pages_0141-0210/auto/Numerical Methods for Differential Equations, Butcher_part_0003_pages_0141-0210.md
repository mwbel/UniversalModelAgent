$$
\begin{array} { c } { \exp ( z ) - ( 1 + \alpha _ { 1 } z + \alpha _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \alpha _ { m } z ^ { m } ) } \\ { - \left( \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { m } z ^ { m } \right) \exp ( - z ) = O ( z ^ { 2 m + 1 } ) } \end{array}
$$

and

$$
\begin{array} { c } { { \exp ( z ) ( 1 - \gamma _ { 1 } z - \gamma _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \gamma _ { m } z ^ { m } ) } } \\ { { - \ ( 1 + \delta _ { 1 } z + \delta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \delta _ { m } z ^ { m } ) = O ( z ^ { 2 m + 1 } ) . } } \end{array}
$$

Note that the rational function

$$
\frac { N ( z ) } { D ( z ) } = \frac { 1 + \delta _ { 1 } z + \delta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \delta _ { m } z ^ { m } } { 1 - \gamma _ { 1 } z - \gamma _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \gamma _ { m } z ^ { m } } ,
$$

is known as a Pad´e approximation to the exponential function. It is the unique rational function with degree $m$ in both numerator and denominator, which maximizes the order of approximation of $N ( z ) / D ( Z )$ to $\exp ( z )$ .

For easy reference, the coefficients $\alpha _ { i }$ , $\beta _ { i }$ , $\gamma _ { i }$ and $\delta _ { i }$ are shown in Tables 253(I) and 253(II) up to $m = 4$ .

An example of the use of the methods discussed here, in a predictor– corrector mode, will be presented in Subsection 255.

# 254 The use of $f$ derivatives

In this subsection, we consider an autonomous differential equation system $y ^ { \prime } ( x ) = f ( y ( x ) )$ . As we remarked in Subsection 224, the use of derivatives of $f$ is more general than the use of higher derivatives of $y$ . Methods that use $f ^ { \prime }$ directly have mainly been proposed for the solution of stiff problems by onestep methods. If an implicit Runge–Kutta method is used, the implementation requires the solution of non-linear equations, typically by a Newton-type method. It was proposed by Rosenbrock (1963) that the Newton iterations could be replaced by a single iteration involving the inverse of a matrix such as $I - h \gamma f ^ { \prime } ( y ( x _ { n - 1 } ) )$ . Methods formed in this way use this linear operation as an intrinsic part of the order requirement for the method. We give a single example in which modified derivatives $F _ { 1 }$ and $F _ { 2 }$ , and the final result at the end of a step, are computed by the formulae

$$
\begin{array} { r l } & { \left( I - h \big ( 1 - \frac { \sqrt { 2 } } { 2 } \big ) f ^ { \prime } ( y _ { n - 1 } ) \right) F _ { 1 } = f ( y _ { n - 1 } ) , } \\ & { \left( I - h \big ( 1 - \frac { \sqrt { 2 } } { 2 } \big ) f ^ { \prime } ( y _ { n - 1 } ) \right) F _ { 2 } = f \Big ( y _ { n - 1 } + h \big ( \frac { \sqrt { 2 } } { 2 } - \frac { 1 } { 2 } \big ) F _ { 1 } \Big ) , } \\ & { \qquad y _ { n } = y _ { n - 1 } + h F _ { 2 } . } \end{array}
$$

Methods of various orders have been derived by Rosenbrock and others. These are known collectively as Rosenbrock methods, although the ambiguous name ‘implicit Runge–Kutta methods’ is sometimes applied to them.

![](images/f497cd364d3071fb5ed754c21de6505f2a4bd04e1331e08fb9557c9ef3f9f68e.jpg)  
Predictor–corrector multiderivative methods

![](images/8922fc1e84669bce4d380397aae166d9f2674a29b0b22cf687525c3d0e5cf123.jpg)  
Rosenbrock method given by (254a)–(254c)

# 255 Further numerical examples

We consider the solution of the same problem discussed in Subsection 252, but using the methods of Subsection 253. The two methods discussed there, for various values of $m$ , implying orders $2 m$ , attached to the curves, are used together in predictor–corrector mode in Figure 255(i). A comparison with Figure 252(i) shows the new methods to be slightly more accurate for the same stepsizes.

The final numerical result in this subsection is based on the mildly stiff problem (203a), written in the form

$$
\begin{array} { l l l } { \displaystyle { \frac { d y _ { 1 } } { d x } = - 1 6 y _ { 1 } + 1 2 y _ { 2 } + 1 6 \cos ( y _ { 3 } ) - 1 3 \sin ( y _ { 3 } ) , \quad } } & { \mathrm { ~ } y _ { 1 } ( 0 ) = 1 , } \\ { \displaystyle { \frac { d y _ { 2 } } { d x } = 1 2 y _ { 1 } - 9 y _ { 2 } - 1 1 \cos ( y _ { 3 } ) + 9 \sin ( y _ { 3 } ) , \quad } } & { \mathrm { ~ } y _ { 2 } ( 0 ) = 0 , } \\ { \displaystyle { \frac { d y _ { 3 } } { d x } = 1 , \quad } } & { \mathrm { ~ } y _ { 3 } ( 0 ) = 0 . } \end{array}
$$

The norm errors for the approximate solution at $x = \pi$ are given for various $h$ in Figure 255(ii).

# Exercises 25

25.1 Consider the function $f ( x , y ) = x ^ { 2 } + y ^ { 2 }$ and the differential equation $y ^ { \prime } ( x ) \ = \ f ( x , y ( x ) )$ . Derive formulae for the second, third and fourth derivatives.

25.2 Solve the initial value problem $y ^ { \prime } ( x ) = x ^ { 2 } + y ( x ) ^ { 2 }$ , $y ( 0 ) = 1$ by the fourth order Taylor series method using $n$ steps with constant stepsize $h = 1 / n$ to yield approximations to the solution at $x = 1$ . Use $n = 1 , 2 , 4 , \dots , 2 ^ { \mathrm { 1 0 } }$ . Are the results consistent with the order 4 nature of the method?

25.3 Use the eighth order predictor–corrector method discussed in Subsection 253 to solve this problem.

25.4 Show that the Rosenbrock method given by (254a), (254b) and (254c) has order 2.

# 26 Hybrid Methods

# 260 Historical introduction

The idea of combining the ideas behind Runge–Kutta methods with those behind linear multistep methods dates from the period 1960–1970. One approach is to make use of stage derivatives computed in one or more previous steps in the computation of the approximation at the end of a current step. Methods based on this idea are referred to as pseudo Runge–Kutta methods. The earliest work on these methods is that of Byrne and Lambert (1966).

Another type of generalization of existing methods was proposed in three independent publications (Gragg and Stetter, 1964; Butcher, 1965; Gear, 1965). The most commonly used name for these is that introduced by Gear, ‘hybrid methods’, although we use here the name ‘modified multistep methods’ introduced by Butcher. A consideration of these various generalizations has led to the construction of comprehensive theories. We consider one of the earliest of these formulations in this section, and refer to the wide class of multivalue–multistage methods as ‘general linear methods’.

# 261 Pseudo Runge–Kutta methods

The paper by Byrne and Lambert suggests a generalization of Runge– Kutta methods in which stage derivatives computed in earlier steps are used alongside stage derivatives found in the current step, to compute the output value in the step. The stages themselves are evaluated in exactly the same way as for a Runge–Kutta method. We consider the case where the derivatives found only in the immediately previous step are used. Denote these by $F _ { i } ^ { [ n - 1 ] }$ , $i = 1 , 2 , \dots , s$ , so that the derivatives evaluated in the current step, $n$ , are $F _ { i } ^ { \left[ n \right] }$ , $i = 1 , 2 , \dots , s$ .

The defining equations for a single step of the method will now be

$$
\begin{array} { c } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } ^ { [ n ] } , } } \\ { { \displaystyle F _ { i } ^ { [ n ] } = f ( x _ { n - 1 } + h c _ { i } , Y _ { i } ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \left( \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } ^ { [ n ] } + \sum _ { i = 1 } ^ { s } \overline { { { b } } } _ { i } F _ { i } ^ { [ n - 1 ] } \right) . } } \end{array}
$$

We consider a single example of a pseudo Runge–Kutta method in which there are $s = 3$ stages and the order is $p = 4$ . The coefficients are given by the tableau

<table><tr><td rowspan=1 colspan=1>011</td><td rowspan=1 colspan=1>1      4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>11      112</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1      1       1124</td></tr></table>

where the additional vector contains the $\overline { { b ^ { \intercal } } }$ components.

Characteristic handicaps with this sort of method are starting and changing stepsize. Starting in this case can be accomplished by taking the first step with the classical Runge–Kutta method but inserting an additional stage $Y _ { 5 }$ , with the role of Y (1)3 , to provide, along with $Y _ { 2 } ^ { ( 2 ) } = Y _ { 2 }$ , the derivatives in step 1 required to complete step 2. Thus the starting step is based on the Runge– Kutta method

<table><tr><td rowspan=1 colspan=1>1</td><td></td></tr><tr><td rowspan=1 colspan=1>1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1    1  1  1  0</td></tr></table>

These methods, known also as hybrid methods or modified linear multistep methods, generalize linear multistep methods, interpreted as predictor– corrector pairs, by inserting one or more additional predictors, typically at offstep points. Although many examples of these a single example for which the off-step point is $\frac { 8 } { 1 5 }$ thods are known, we give justof the way through the step. That is, the first predictor computes an approximation to $\begin{array} { r l } { y ( x _ { n - 1 } + \frac { 8 } { 1 5 } h ) = } \end{array}$ $\textstyle y ( x _ { n } - { \frac { 7 } { 1 5 } } h )$ . We denote this first predicted value by the symbol $\scriptstyle { \mathcal { Y } } _ { n - 7 / 1 5 }$ and the corresponding derivative by $\begin{array} { r } { \dddot { f } _ { n - 7 / 1 5 } = f ( x _ { n } - \frac { 7 } { 1 5 } h , \widetilde { y } _ { n - 7 / 1 5 } ) } \end{array}$ . Similarly, the second predictor, which gives an initial approximation to $y ( x _ { n } )$ , will be denoted by $\widetilde { y } _ { n }$ and the corresponding derivative by $\widetilde { f } _ { n } ~ = ~ f ( x _ { n } , \widetilde { y } _ { n } )$ . This notation is in contrast to $y _ { n }$ and $f _ { n }$ , which denote the corrected step approximation to $y ( x _ { n } )$ and the corresponding derivative $f ( x _ { n } , y _ { n } )$ , respectively. The relationships between these quantities are

$$
\begin{array} { r l r } {  { \widetilde { y } _ { n - 7 / 1 5 } = - \frac { 5 2 9 } { 3 3 7 5 } y _ { n - 1 } + \frac { 3 9 0 4 } { 3 3 7 5 } y _ { n - 2 } + h ( \frac { 4 2 3 2 } { 3 3 7 5 } f _ { n - 1 } + \frac { 1 4 7 2 } { 3 3 7 5 } f _ { n - 2 } ) , } } \\ & { } & \\ & { } & { \widetilde { y } _ { n } = \frac { 1 5 2 } { 2 5 } y _ { n - 1 } - \frac { 1 2 7 } { 2 5 } y _ { n - 2 } + h ( \frac { 1 8 9 } { 9 2 } \widetilde { f } _ { n - 7 / 1 5 } - \frac { 4 1 9 } { 1 0 0 } f _ { n - 1 } - \frac { 1 1 1 8 } { 5 7 5 } f _ { n - 2 } ) , } \\ & { } & \\ & { } & { y _ { n } = y _ { n - 1 } + h ( \frac { 2 5 } { 1 6 8 } \widetilde { f } _ { n } + \frac { 3 3 7 5 } { 5 1 5 2 } \widetilde { f } _ { n - 7 / 1 5 } + \frac { 1 9 } { 9 6 } f _ { n - 1 } - \frac { 1 } { 5 5 2 } f _ { n - 2 } ) . \qquad } \end{array}
$$

# 263 General linear methods

To obtain a general formulation of methods that possess the multivalue attributes of linear multistep methods, as well as the multistage attributes of Runge–Kutta methods, general linear methods were introduced by the present author (Butcher, 1966). However, the formulation we present, while formally different, is equivalent in terms of the range of methods it can represent, and was introduced in Burrage and Butcher (1980).

Suppose that $r$ quantities are passed from step to step. At the start of step $n$ , these will be denoted by $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { [ n - 1 ] }$ , . , y[n−1] r , and after the step is completed, thstep will be $y _ { 1 } ^ { [ n ] }$ or, $y _ { 2 } ^ { [ n ] }$ onding, . . . , $y _ { r } ^ { \lfloor n \rfloor }$ antities available for use in the subsequen. During the computation of the step, $s$ stage values $Y _ { 1 }$ , $Y _ { 2 }$ , $\cdot \cdot \cdot$ , $Y _ { s }$ are computed, along with the corresponding stage derivatives $F _ { 1 }$ , $F _ { 2 }$ , $\cdot \cdot \cdot$ , $F _ { s }$ . For convenience of notation, we can create supervectors containing either $r$ or $s$ subvectors as follows:

$$
\begin{array} { r } { y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n - 1 ] } } \\ { y _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n - 1 ] } } \end{array} \right] , \quad y ^ { [ n ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n ] } } \\ { y _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n ] } } \end{array} \right] , \quad Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad F = \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { \vdots } \\ { F _ { s } } \end{array} \right] . } \end{array}
$$

Just as for Runge–Kutta methods, the stages are computed making use of linear combinations of the stage derivatives but, since there are now a collection of input approximations, further linear combinations are needed to express the dependence on this input information. Similarly, the output quantities depend linearly on both the stage derivatives and the input quantities. All in all, four matrices are required to express all the details of these computations, and we denote these by $A = [ a _ { i j } ] _ { s , s }$ , $U = \left[ u _ { i j } \right] _ { s , r }$ , $B = [ b _ { i j } ] _ { r , s }$ and $V = [ v _ { i j } ] _ { r , r }$ .

The formulae for the stage values and the output values are

$$
\begin{array} { r } { Y _ { i } = \displaystyle \sum _ { j = 1 } ^ { s } h a _ { i j } F _ { j } + \sum _ { j = 1 } ^ { r } u _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , s , } \\ { y _ { i } ^ { [ n ] } = \displaystyle \sum _ { j = 1 } ^ { s } h b _ { i j } F _ { j } + \sum _ { j = 1 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , r , } \end{array}
$$

or, using Kronecker product notation for an $N$ -dimensional problem,

$$
\begin{array} { r } { Y = h ( A \otimes I _ { N } ) F + ( U \otimes I _ { N } ) y ^ { [ n - 1 ] } , } \\ { y ^ { [ n ] } = h ( B \otimes I _ { N } ) F + ( V \otimes I _ { N } ) y ^ { [ n - 1 ] } . } \end{array}
$$

We devote Chapter 5 to a detailed study of general linear methods but, for the present, we illustrate the all-encompassing nature of the methods included in this family by presenting a number of sample methods written in this terminology.

In each case, the coefficients of the general linear formulation are presented in the $( s + r ) \times ( s + r )$ partitioned matrix

$$
\textstyle \left[ { \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} } \right] .
$$

The Euler method and implicit Euler methods are, respectively,

$$
\left[ { \frac { 0 \left| 1 \right| } { 1 \left| 1 \right] } } \right] \quad { \mathrm { a n d } } \quad \left[ { \frac { 1 \left| 1 \right| } { 1 \left| 1 \right| } } \right] .
$$

The Runge–Kutta methods (232a) and (233f) and (235i) are, respectively,

$$
 { \begin{array} { c c } { \mathrm { ~ - } } & { 0 } & { 0 } \\ { \mathrm { ~ 1 } } & { 0 } & { 1 } \\ { \mathrm { ~ - } { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { | \begin{array} { c } { 1 } \\ { 1 } \\ { 1 } \end{array} ] } } \end{array} } \quad { \mathrm { a n d } } \quad [ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { \mathrm { ~ - } 1 } & { 2 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } |  \quad { \mathrm { a n d } } \quad [ { \begin{array} { c c c c } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } ] .
$$

The second order Adams–Bashforth and Adams–Moulton and PECE methods based on these are, respectively,

$$
[ \begin{array} { l l l } { 0 | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { 0 | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { 1 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} ] \quad \mathrm { a n d } \quad [ \frac { 1 } { \frac { 1 } { 2 } } | 1  1 ] \quad \mathrm { a n d } \quad [ \frac { 1 } { \frac { 1 } { 2 } } \begin{array} { l l l l } { 0 } & { 0 } & { | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } & { 0 } & { | 1 } & { \frac { 1 } { 2 } } & { 0 } \\ { \frac { 1 } { 2 } } & { 0 } & { 1 } & { \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { 1 } & { | 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } \end{array}  ] ,
$$

where for each of the Adams–Bashforth and PECE methods, the output quantities are approximations to $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ and $h y ^ { \prime } ( x _ { n - 1 } )$ , respectively.

Finally, we re-present two methods derived in this section. The first is the pseudo Runge–Kutta method (261a), for which the general linear representation is

<table><tr><td rowspan=2 colspan=1>0    0  00  0</td><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1> 0</td><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1>12   1  4</td><td rowspan=1 colspan=1>1  1    1      412</td></tr><tr><td rowspan=1 colspan=1>1    0  0</td><td rowspan=1 colspan=1>0  0    0      0</td></tr><tr><td rowspan=1 colspan=1>0    1  0</td><td rowspan=1 colspan=1>0  0    0      0</td></tr><tr><td rowspan=1 colspan=1>0    0 1</td><td rowspan=1 colspan=1>0  0    0      0</td></tr></table>

The four output quantities for this method are the approximate solution found at the end of the step, together with $h$ multiplied by each of the three stage derivatives. The second of the two general linear methods, that do not fit into any of the classical families, is the method introduced in Subsection 262. Its general linear method coefficient matrix is

<table><tr><td>0 189 92 3375 5152</td><td>0 0 25</td><td>0 529 3375 0 152 25 0 1</td><td>3904 3375 127 25 0</td><td>4232 3375 419 100 19</td><td>1472 3375 1118 575 1</td></tr><tr><td>3375</td><td>168 25 0 168</td><td>1</td><td>0</td><td>96 19</td><td>552 1</td></tr><tr><td>5152 0</td><td>0 0</td><td>1</td><td>0</td><td>96 0</td><td>552</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td></td><td></td><td></td><td>0</td></tr><tr><td>0</td><td>0 0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

For this method, the output quantities are given by $y _ { 1 } ^ { [ n ] } \approx y ( x _ { n } )$ , $y _ { 2 } ^ { [ n ] } \approx$ $y ( x _ { n - 1 } )$ , $y _ { 3 } ^ { [ n ] } \approx h y ^ { \prime } ( x _ { n } )$ and $y _ { 4 } ^ { \lfloor n \rfloor } \approx h y ^ { \prime } ( x _ { n - 1 } )$ .

![](images/8dff35cc11da4683e9c04024e751ac373f6803b26e372076b8e911de65602628.jpg)  
Comparison of Runge–Kutta with pseudo Runge–Kutta method

# 264 Numerical examples

The limited numerical testing performed here does not give a great deal of support to the use of pseudo Runge–Kutta or hybrid methods. Using the Kepler problem with eccentricity $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ over a half period, the pseudo Runge– Kutta method (261a) was compared with the classical Runge–Kutta method and the results are summarized in Figure 264(i). To make the comparison as fair as possible, the axis denoted by $\overline { { h } }$ shows the stepsize per function evaluation. That is, for the Runge–Kutta method, $h = 4 \overline { { h } }$ , and for the pseudo Runge–Kutta method, $h \ : = \ : 3 \overline { { h } }$ . The classical Runge–Kutta is significantly more accurate for this problem.

A similar comparison has been made between the hybrid method discussed in Subsection 262 and a fifth order Runge–Kutta method, but the results, which are not presented here, show almost identical performance for the two methods.

# Exercises 26

26.1 Find the error computed in a single step using the method (261a) for the problem

$$
y ^ { \prime } ( x ) = x ^ { 4 }
$$

and show that this is 16 times the error for the classical Runge–Kutta method.

26.2 Find a fifth order method similar to the one discussed in Subsection   
262, but with first predictor giving an approximation to $\textstyle y ( x _ { n } - { \frac { 1 } { 2 } } h )$ .

26.3 Show how to represent the PEC method based on the second order Adams–Bashforth predictor and the third order Adams–Moulton corrector as a general linear method.

26.4 Show how to represent the PECEC method based on second order Adams–Bashforth and Adams–Moulton methods as a general linear method.

# 27 Introduction to Implementation

# 270 Choice of method

Many differential equation solvers have been constructed, based on a variety of computational schemes, from Runge–Kutta and linear multistep methods, to Taylor series and extrapolation methods. In this introduction to implementation of initial value solvers, we will use an ‘Almost Runge– Kutta’ (ARK) method. We will equip this method with local error estimation, variable stepsize and interpolation. It is intended for non-stiff problems but can be used also for delay problems, because of its reliable and accurate builtin interpolation.

Many methods are designed for variable order, but this is a level of complexity which we will avoid in this introduction. The method to be presented has order 3 and, because it is a multivalue method, it might be expected to require an elaborate starting sequence. However, it is a characteristic property of ARK methods that starting will present a negligible overhead on the overall costs and will involve negligible complication in the design of the solver.

Recall from Subsection 263 the notation used for formulating a general linear method. In the case of the new experimental method, the coefficient matrix is

$$
[ A \ U ] = [ { \begin{array} { c c c c } { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 3 - 3 } & { 2 } \end{array} } [ { \begin{array} { c c c } { 1 } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 1 8 } } } \\ { 1 } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 1 8 } } } \\ { 1 } & { { \frac { 1 } { 4 } } } & { 0 } \\ { 1 } & { { \frac { 1 } { 4 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { - 2 } & { 0 } \end{array} } ] .
$$

Because general linear methods have no specific interpretation, we need to state the meaning of the various quantities which play a role in the formulation of the method. Approximate values of these are as follows:

α A single step using an ARK method   

<table><tr><td>function [xout，yout] = ARKstep(x,y,f,h) Uy = y*[1,1,1;1/3,1/6,1/4;1/18,1/18,0] ;</td></tr><tr><td>hF = h*f(x+(1/3)*h,Uy(:,1));</td></tr><tr><td></td></tr><tr><td>hF = [hF,h*f(x+(2/3)*h,Uy(:,2)+(1/2)*hF)];</td></tr><tr><td>xout = x+h;</td></tr><tr><td>y1out = Uy(:,3)+hF*[0;3/4]; hF = [hF,h*f(xout,y1out)];</td></tr></table>

$$
\begin{array} { r l } & { y _ { 0 } ^ {[ n - 1 ] } = y ( x _ { n - 1 } ) , } \\ & { y _ { 2 } ^ { [ n - 1 ] } = h y ^ { \prime } ( x _ { n - 1 } ) , } \\ & { y _ { 3 } ^ { [ n - 1 ] } = h ^ { 2 } y ^ { ( \prime \prime ) } ( x _ { n - 1 } ) , } \\ & { Y _ { 1 } = y ( x _ { n - 1 } + \frac { 1 } { 3 } h ) , } \\ & { Y _ { 2 } = y ( x _ { n - 1 } + \frac { 2 } { 3 } h ) , } \\ & { Y _ { 3 } = y ( x _ { n - 1 } + h ) , } \\ & { y _ { 1 } ^ { [ n ] } = y ( x _ { n } ) , } \\ & { y _ { 2 } ^ { [ n ] } = h y ^ { \prime } ( x _ { n } ) , } \\ & { y _ { 3 } ^ { [ n ] } = h ^ { 2 } y ^ { ( \prime \prime ) } ( x _ { n } ) . } \end{array}
$$

The method is third order and we would expect that, with precise input values, the output after a single step would be correct to within $O ( h ^ { 4 } )$ . With the interpretation we have introduced, this is not quite correct because the third output value is in error by $O ( h ^ { 3 } )$ from its target value. We can correct this by writing down a more precise formula for $y _ { 3 } ^ { [ n - 1 ] }$ , and correspondingly for $y _ { 3 } ^ { [ n ] }$ . However, we can avoid having to do this, by remarking that the method satisfies what are called ‘annihilation conditions’ which cause errors and $O ( h ^ { 3 } )$ $y _ { 2 } ^ { [ n ] }$ in the input 3 1. For this method, the stages are all computed correctly to within $y _ { 3 } ^ { [ n - 1 ] }$ to be cancelled out in the values computed for $y _ { 1 } ^ { \lfloor n \rfloor }$ $O ( h ^ { 3 } )$ , rather than only to first order accuracy as in an explicit Runge–Kutta method. The computations constituting a single step of the method in the solution of a differential equation $y ^ { \prime } = f ( x , y )$ are shown in Algorithm $2 7 0 \alpha$ . The array y as a parameter for the function ARKstep consists of three columns with the values of $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { [ n - 1 ] }$ , $y _ { 3 } ^ { \lfloor n - 1 \rfloor }$ , respectively. The updated values of these quantities, at the end of step $n$ , are embedded in a similar way in the output result yout.

Variation in the stepsize as the integration proceeds, is needed to deal with changes in behaviour in the apparent accuracy of individual steps. If, in addition to computing the output results, an approximation is computed to the error committed in each step, a suitable strategy is to adjust $h$ to maintain the error estimates close to a fixed value, specified by a user-imposed tolerance.

In the case of the ARK method introduced in Subsection 270, we propose to compute an alternative approximation to $y$ at the end of the step and to regard their difference as an error estimate. This alternative approximation will be defined as

$$
\begin{array} { r } { \widehat { y } _ { n } = y _ { 1 } ^ { [ n - 1 ] } + \frac { 1 } { 8 } y _ { 2 } ^ { [ n - 1 ] } + \frac { 3 } { 8 } ( h F _ { 1 } + h F _ { 2 } ) + \frac { 1 } { 8 } h F _ { 3 } , } \end{array}
$$

based on the three-eighths rule quadrature formula. It is known that the difference between ${ \widehat { y } } _ { n }$ and $y _ { 1 } ^ { [ n ] }$ is $O ( h ^ { 4 } )$ , and this fact will be used in stepsize adjustments.

Because of the asymptotic behaviour of the error estimate, we can increase or decrease the error predicted in the following step, by multiplying $h$ by

$$
r = \bigg ( \frac { T } { \lVert \widehat { y } - y _ { 1 } ^ { [ n ] } \rVert } \bigg ) ^ { 1 / 4 } .
$$

This assumes that the error, or at least the quantity we are estimating, is changing slowly from step to step. If $\lVert \widehat { y } - y _ { 1 } ^ { [ n ] } \rVert \leq T$ is used as a criterion for accepting the current step, then the use of (271b) to predict the next stepsize allows the possibility of obtaining an unwanted rejection in the new step. Hence it is customary to insert a safety factor, equal to 0.9 for example, in (271a). Furthermore, to avoid violent swings of $h$ in exceptional circumstances, the stepsize ratio is usually forced to lie between two bounds, such as 0.5 and 2.0. Thus we should refine (271b) by multiplying $h$ not by $r$ , but by $\operatorname* { m i n } ( \operatorname* { m a x } ( 0 . 5 , 0 . 9 r ) , 2 . 0 )$ . For robust program design, the division in (271b) must be avoided when the denominator becomes accidentally small.

In modern solvers, a more sophisticated stepsize adjustment is used, based on PI control (Gustafsson, Lundh and S¨oderlind, 1988; Gustafsson, 1991). In the terminology of control theory, P control refers to ‘proportional control’, whereas PI or ‘proportional integral control’ uses an accumulation of values of the controller, in this case a controller based on error estimates, over recent time steps.

To illustrate the ideas of error estimation and stepsize control, a modified version of Algorithm $2 7 0 \alpha$ is presented as Algorithm $2 7 1 \alpha$ . The additional parameter T denotes the tolerance; the additional outputs hout and reject are, respectively, the proposed stepsize in the succeeding step and an indicator as to whether the current step apparently achieved sufficient accuracy. In the case $\mathtt { r e j e c t } = 1$ , signifying failure, the variables xout and yout retain the corresponding input values x and y.

α An ARK method step with stepsize control   

<table><tr><td>function [xout,yout,hout,reject] = ARKstep(x,y,f,h,T) Uy = y*[1,1,1;1/3,1/6,1/4;1/18,1/18,0]; hF = h*f(x+(1/3)*h,Uy(:,1)); hF = [hF,h*f(x+(2/3)*h,Uy(:,2)+(1/2)*hF)];</td></tr><tr><td>xout = x+h; y1out = Uy(:,3)+hF*[0;3/4];</td></tr><tr><td>hF = [hF,h*f(xout,y1out)];</td></tr><tr><td>y3out = hF*[3;-3;2]-2*y(:,2);</td></tr><tr><td>yout = [y1out,hF(:,3),y3out];</td></tr><tr><td>err = norm(hF*[3/8;-3/8;1/8]-y(:,2)/8);</td></tr><tr><td>reject = err &gt; T;</td></tr><tr><td>if err &lt; 0.04*T</td></tr><tr><td>r=2;</td></tr><tr><td>else</td></tr><tr><td>r = (T/err)^0.25; r = min(max(0.5，0.9*r),2.0); end</td></tr></table>

# 272 Interpolation

To obtain an approximation solution for a specific value of $x$ , it is possible to shorten the final step, if necessary, to complete the step exactly at the right place. However, it is usually more convenient to rely on a stepsize control mechanism that is independent of output requirements, and to produce required output results by interpolation, as the opportunity arises. The use of interpolation makes it also possible to produce output at multiple and arbitrary points. For the third order method introduced in Subsection 270, a suitable interpolation scheme is based on the third order Hermite interpolation formula using both solution and derivative data at the beginning and end of each step. It is usually considered to be an advantage for the interpolated solution to have a reasonably high order of continuity at the step points and the use of third order Hermite will give first order continuity. We will write the interpolation formula in the form

$$
\begin{array} { r l } & { y ( x _ { n - 1 } + h t ) \approx ( 1 + 2 t ) ( 1 - t ) ^ { 2 } y ( x _ { n - 1 } ) + ( 3 - 2 t ) t ^ { 2 } y ( x _ { n } ) } \\ & { \qquad + t ( 1 - t ) ^ { 2 } h y ^ { \prime } ( x _ { n - 1 } ) - t ^ { 2 } ( 1 - t ) h y ^ { \prime } ( x _ { n } ) . } \end{array}
$$

![](images/35d8434cd222a65ca98f3c3abbb7739a1d14f2e0a351854bec22534ee0b981fd.jpg)  
Third order ARK method computations for the Kepler problem

To see how well the numerical method discussed in this section works in practice, it has been applied to the Kepler problem introduced in Subsection 101. For each of the eccentricity values chosen, denoted by $e$ , the problem has been scaled to an initial value

$$
\begin{array} { r } { y ( 0 ) = \Big [ 1 - e \quad 0 \quad 0 \quad \sqrt { ( 1 + e ) / ( 1 - e ) } \Big ] ^ { \top } , } \end{array}
$$

so that the period will be $2 \pi$ . The aim is to approximate the solution at $x = \pi$ for which the exact result is

$$
y ( \pi ) = { \Bigl [ } - 1 - e \quad 0 \quad 0 \quad - { \sqrt { ( 1 - e ) / ( 1 + e ) } } { \Bigr ] } ^ { \intercal } .
$$

In the first experiment, the problem was solved for a range of eccentricities $e = 0 , { \frac { 1 } { 2 } } , { \frac { 3 } { 4 } } , { \frac { 7 } { 8 } }$ with a tolerance of $T = 1 0 ^ { - 4 }$ . The results are shown in Figure 273(i) with all step points marked. The computed result for $x = \pi$ cannot be found from the variable stepsize schemes unless interpolation is carried out or the final step is forced to arrive exactly at the right value of $x$ . There was no discernible difference between these two half-period approximations, and their common values are indicated on the results.

The second experiment performed with this problem is to investigate the dependence on the accuracy actually achieved, as the tolerance is varied. The results achieved are almost identical for each of the eccentricities considered and the results will be reported only for $\textstyle e = { \frac { 7 } { 8 } }$ . Before reporting the outcome of this experiment, we might ask what might be expected. If we really were controlling locally committed errors, the stepsize would, approximately, be proportional to $T ^ { 1 / ( p + 1 ) }$ ; however, the contribution to global error, of errors committed within each small time interval, is proportional to $h ^ { p }$ . Hence we should expect that, for very small tolerances, the total error will be proportional to $T ^ { p / ( p + 1 ) }$ . But the controller we are using for the ARK method is not based on an asymptotically correct error estimate, and this will alter the outcome.

Global error and numbers of steps for varying tolerance with the Kepler problem   

<table><tr><td>T</td><td>|Error|l</td><td>Ratio</td><td>Steps</td></tr><tr><td>80</td><td>4.84285</td><td>3.94773</td><td>7</td></tr><tr><td>8-1</td><td>1.22674</td><td>3.71289</td><td>8</td></tr><tr><td>8-2</td><td>3.30401 1×10-1</td><td>3.98876</td><td>8</td></tr><tr><td>8-3</td><td>8.28328× 10-2</td><td>3.54007</td><td>10</td></tr><tr><td>8</td><td>2.33986 × 10-2</td><td>4.72504</td><td>13</td></tr><tr><td>8 -5</td><td>4.95205 × 10-3</td><td>4.73180</td><td>19</td></tr><tr><td>8-6</td><td>1.04655 × 10-3</td><td>4.65786</td><td>30</td></tr><tr><td>8-7</td><td>2.24684 × 10-4</td><td>4.58854</td><td>50</td></tr><tr><td>8-8</td><td>4.89663 × 10-5</td><td>4.78350</td><td>82</td></tr><tr><td>8-9</td><td>1.02365 × 10-5</td><td>4.75845</td><td>137</td></tr><tr><td>8-10</td><td>2.15123 × 10-6</td><td>4.74429</td><td>228</td></tr><tr><td>8-11</td><td>4.53436 × 10-7</td><td>4.73529</td><td>382</td></tr><tr><td>8-12</td><td>9.57567 × 10-8</td><td>4.76011</td><td>642</td></tr><tr><td>8-13</td><td>2.01165 × 10-8</td><td>4.75737</td><td>1078</td></tr><tr><td>8-14</td><td>4.22848 × 10-9</td><td></td><td>1810</td></tr></table>

In fact the results given in Table 273(I), for this third order method, do show an approximately two-thirds power behaviour. We see this by looking at the ratios of successive norm errors as $T$ is reduced by a factor of 8. Also included in the table is the number of steps. As $T$ becomes small, the number of steps should approximately double each time $T$ is decreased by a factor $\frac { 1 } { 8 }$ .

# 274 Experiments with a discontinuous problem

The stepsize control mechanism, coded into Algorithm $2 7 1 \alpha$ , contains upper and lower bounds on the stepsize ratios. The choice of these bounds acquires crucial importance when low order discontinuities arise in the solution. When a step straddles a point at which there is a sudden change in one of the low order derivatives, this will be recognized by the solver as a massive error estimate, unless the stepsize is abnormally short. Consider, for example, the two-dimensional problem

![](images/981ce10db140f26c18dfa65271bcb20a8d0328e89cfe766ec637b5a0664d3732.jpg)  
Errors and number of rejections for (274a)

$$
\begin{array} { r } { y ^ { \prime } ( x ) = \left\{ \begin{array} { l l } { \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] , } & { y _ { 1 } > y _ { 2 } , } \\ { \left[ \begin{array} { l } { - 1 } \\ { 0 } \end{array} \right] , } & { y ( 0 ) = \left[ \begin{array} { l } { 1 } \\ { \pi / 6 } \end{array} \right] . } \end{array} \right. } \end{array}
$$

The solution to this problem is very simple: $y ( x ) = [ 1 , x + \pi / 6 ] ^ { 1 }$ for $x < 1 - \pi / 6$ and $y ( x ) = [ 2 - \pi / 6 - x , 1 ] ^ { \mathfrak { l } }$ for $x > 1 - \pi / 6$ . Because we are interested in how well the method deals with discontinuous behaviour, we will not take into account our knowledge of where this point is located. What should we expect to happen? We would expect the first step, which jumps over $x = 1 - \pi / 6$ , to fail and for the stepsize to be reduced as much as the stepsize controller permits. There will then be a sequence of successes (followed by step increases), or failures (followed by step decreases). This sequence will terminate only when the stepsize is small enough for the quantity used as the error estimate to be less than $T$ . Numerical results for this problem using Algorithm $2 7 1 \alpha$ are presented in Figure $2 7 4 ( \mathrm { i } )$ .

These show the dependence on the accuracy achieved, measured in terms of the error in the component of $y _ { 2 }$ after the trajectory has turned the corner at $y = [ 1 , 1 ] ^ { \scriptscriptstyle 1 }$ , together with the number of steps rejected in the whole process of locating the discontinuity in $y ^ { \prime }$ and getting past it.

The results will be sensitive to the initial stepsize and, to guarantee we have represented typical and representative behaviour, a large number of initial stepsizes were used with each tolerance. For both the error calculations and the rejected step totals, the results indicate mean values over this range of initial $h$ with shading showing the mean values plus or minus the standard deviation and plus or minus twice the standard deviations. The results suggest that, for this and similar problems, we should expect the error to have a similar magnitude to the tolerance and the number of rejections to be proportional to the logarithm of the tolerance.

# Exercises 27

27.1 By computing the scaled derivative of the output from the classical fourth order Runge–Kutta method RK41 (235i), within the current step, rather than from the first stage of the following step, show that the method becomes the general linear method

$$
\begin{array}{c} [ { \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } \end{array} } ] { \mathrm { ~ 1 ~ } } { \mathrm { ~ \frac { 1 } { 2 } ~ } }  \\ { { [ { \begin{array} { l l l l l } { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { { | { \begin{array} { l l } { 1 } & { { \frac { 1 } { 6 } } } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } | } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } ] } } \end{array} ] ~ .
$$

27.2 Write a fourth order method, with stepsize control, based on the method in Exercise 27.1 which is equivalent to two steps of RK41, each with stepsize $h$ , combined with a single step from the same input, with stepsize $2 h$ . Use the difference between the two-step result and the double-step result as an error estimator.

27.3 Denote the starting point in Exercise 27.2 as $x _ { - 1 }$ so that the results are computed at $x _ { 0 } = x _ { - 1 } + h$ and $x _ { 1 } = x _ { 0 } + h$ . Find a suitable interpolator for this method based on approximations to $y ( x _ { - 1 } )$ , $h y ^ { \prime } ( x _ { - 1 } )$ , $y ( x _ { 0 } )$ , $y ( x _ { 1 } )$ , $h y ^ { \prime } ( x _ { 1 } )$ to yield an approximation to $y ( x _ { 0 } + h t )$ , for $t \in [ - 1 , 1 ]$ . Add this interpolator to the variable step method discussed in Exercise 27.2.

# Chapter 3

# Runge–Kutta Methods

# 30 Preliminaries

# 300 Rooted trees

We saw in Section 23 that the graphs known as ‘rooted trees’ play a central role in the analysis of the accuracy of Runge–Kutta methods. We regard a rooted tree as a pair $( V , E )$ , where $V$ is a finite set of ‘vertices’ and $E$ a set of ‘edges’. The edges consist of ordered pairs of members of $V$ , subject to certain conditions. The first condition is that every member of $V$ , except one element known as the ‘root’, occurs exactly once amongst the second member in each pair in $E$ . The special root vertex does not occur as the second member of any pair. For the final condition, for $( V , E )$ to be a rooted tree, there are two alternatives, which are known to be equivalent: the first is that the graph defined by $( V , E )$ is connected; and the second is that $( V , E )$ defines a partial ordering.

It will be convenient, throughout this discussion, to refer to members of $V$ which do not occur as the first member of any pair in $V$ . For a given edge $[ x , y ] \in E$ , $x$ will be referred to as the ‘parent’ of $y$ and $y$ will be referred to as a ‘child’ of $x$ . Thus, a vertex may have one or more children but, if it has none, it is a leaf. Similarly every vertex, except the root, has exactly one parent, whereas the root has no parent.

We do not pursue the formal properties of graphs, and of rooted trees in particular, because they are formulated in specialist books on this subject and are easily appreciated through examples and diagrams. In diagrammatic depictions of a directed graph, the vertices are represented as points and the edges by arrowed line segments joining pairs of points, with the arrow pointing from the first to second member of the pair. We illustrate these ideas in Figure 300(i), where a number of rooted trees are shown. In contrast, Figure 300(ii) shows some graphs which are not rooted trees. In these figures, the members of $V$ are chosen to be positive integers. Wherever possible, the diagrams are arranged so that the root, if it exists, is at the bottom of the picture and so that all arrows are pointing in a direction with an upwards component.

Even though we are representing rooted trees using points, labelled by members of a vertex set, we are interested in the abstract structure behind this definition. That is, if $( V , E )$ and $( V ^ { \prime } , E ^ { \prime } )$ are rooted trees and there exists a bijection $\varphi : V \to V ^ { \prime }$ such that $[ x , y ] \in E$ if and only if $[ \varphi ( x ) , \varphi ( y ) ] \in E ^ { \prime }$ , then the two rooted trees are identical, when represented as diagrams, except for the labels attached to the points. We can thus regard an ‘abstract rooted tree’ as an equivalence class under this type of isomorphism. We use each interpretation from time to time, according to our convenience; where it is not clear from the context which is intended, we add some words of clarification. For a labelled tree $\mathbf { t }$ , the corresponding abstract tree will be denoted by |t|.

![](images/cd9df731d918dc43d7de8d1f6ec505a63837bff0e398c0f965c9b70531d816fe.jpg)  
Some directed graphs which are rooted trees

![](images/56ef01b02ac5a1b850d36907458b3785c59fdf9682f70c488c287e3e8e7979fc.jpg)  
Some directed graphs which are not rooted trees

To conclude this introduction to rooted trees, we present two alternative notations for trees. In each notation, we denote the single tree, with only one vertex, by the symbol $\tau$ . In the first notation, we consider a tree $t$ such that, when the root is removed, there remain a number of disconnected trees, say $t _ { 1 }$ , $t _ { 2 } , \ldots , t _ { m }$ , where $m$ is the number of ‘children’ of the root of $t$ . We then write $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ . This gives a recursion for constructing a symbolic denotation for any particular tree. When some of $t _ { 1 }$ , $t _ { 2 }$ , $\cdot \cdot \cdot$ , $t _ { m }$ are equal to each other, it will be convenient to represent these repetitions using a power notation. For example, $\left[ t _ { 1 } t _ { 1 } t _ { 2 } t _ { 2 } t _ { 2 } t _ { 3 } \right]$ will also be written as $[ t _ { 1 } ^ { 2 } t _ { 2 } ^ { 3 } t _ { 3 } ]$ .

The second notation builds up a symbolic representation of all trees by using a non-associative product of rooted trees, such that $t _ { 1 } t _ { 2 }$ is formed by joining them at the roots, with an additional edge from the root $v _ { 1 }$ of $t _ { 1 }$ to the root $v _ { 2 }$ of $t _ { 2 }$ . Thus if $t _ { 1 } = | ( V _ { 1 } , E _ { 1 } ) |$ and $t _ { 2 } = | ( V _ { 2 } , E _ { 2 } ) |$ , and $V _ { 1 }$ and $V _ { 2 }$ are disjoint sets, then $t _ { 1 } t _ { 2 }$ is the tree $| ( V _ { 1 } \cup V _ { 2 } , E _ { 1 } \cup E _ { 2 } \cup | v _ { 1 } , v _ { 2 } | ) |$ . Because the product is not associative, we need to distinguish between $( t _ { 1 } t _ { 2 } ) t _ { 3 }$ and $t _ { 1 } ( t _ { 2 } t _ { 3 } )$ without introducing more parentheses than necessary. Hence, we sometimes write $( t _ { 1 } t _ { 2 } ) t _ { 3 } = t _ { 1 } t _ { 2 } . t _ { 3 }$ and $t _ { 1 } ( t _ { 2 } t _ { 3 } ) = t _ { 1 } . t _ { 2 } t _ { 3 }$ .

Trees, notations for trees and various functions on trees   

<table><tr><td>r(t)</td><td>t</td><td></td><td></td><td>σ(t）γ(t)</td><td></td></tr><tr><td>1</td><td>·</td><td>T</td><td>T</td><td>1</td><td>1</td></tr><tr><td>2</td><td>：</td><td>[7]</td><td>TT</td><td>1</td><td>2</td></tr><tr><td>3</td><td>?</td><td>[r2]</td><td>TT.T</td><td>2</td><td>3</td></tr><tr><td>3</td><td></td><td>[]]</td><td>T.TT</td><td>1</td><td>6</td></tr><tr><td>4</td><td>：</td><td>[73]</td><td>(TT.T)T</td><td>6</td><td>4</td></tr><tr><td>4</td><td>山</td><td>[[]]</td><td>TT.TT = (T.TT)T</td><td>1</td><td>8</td></tr><tr><td>4</td><td></td><td>[r2]]</td><td>T(TT.T)</td><td>2</td><td>12</td></tr><tr><td>4</td><td>：</td><td>[[]]</td><td>T(T.TT)</td><td>1</td><td>24</td></tr><tr><td>5</td><td>V</td><td>[r4]</td><td>(TT.T)T.T</td><td>24</td><td>5</td></tr><tr><td>5</td><td>2</td><td>[r2[7]]</td><td>(T.TT)T.T = (TT.TT)T = (TT.T).TT</td><td>2</td><td>10</td></tr><tr><td>5</td><td></td><td>[[r2]]</td><td>TT.(TT.T) = T(TT.T).T</td><td>2</td><td>15</td></tr><tr><td>5</td><td></td><td>[7[[]]</td><td>T(T.TT).T = TT.(T.TT)</td><td>1</td><td>30</td></tr><tr><td>5</td><td></td><td>[[r]2]</td><td>(T.TT).TT</td><td>2</td><td>20</td></tr><tr><td>5</td><td></td><td>[[73]]</td><td>T.(TT.T)T</td><td>6</td><td>20</td></tr><tr><td>5</td><td></td><td>[7[7]]</td><td>T(TT.TT) = T.(T.TT)T</td><td>1</td><td>40</td></tr><tr><td>5</td><td></td><td>[[t2]]</td><td>T.T(TT.T)</td><td>2</td><td>60</td></tr><tr><td>5</td><td></td><td>[[7]]]</td><td>T.T(T.TT)</td><td>1</td><td>120</td></tr></table>

We illustrate these notations in Table $3 0 0 ( \mathrm { I } )$ , where all trees with up to five vertices are shown. Also shown are the functions $r ( t )$ , $\sigma ( t )$ and $\gamma ( t )$ to be introduced in the next subsection.

# 301 Functions on trees

For a rooted tree $t$ , define $r ( t )$ , the ‘order’ of $t$ , as the number of vertices in $t$ . That is, if $t$ is labelled as $( V , E )$ , then $r ( t ) = \# V$ , the cardinality of the set $V$ . Let $A ( t )$ denote the group of automorphisms on a particular labelling of $t$ . That is, $A ( t )$ is the set of mappings $\varphi : V \to V$ such that $[ x , y ] \in E$ if and only if $[ \varphi ( x ) , \varphi ( y ) ] \in E$ . The group $A ( t )$ will be known as the ‘symmetry group’ of $t$ ; its order will be known as the ‘symmetry’, and denoted by $\sigma ( t )$ . The ‘density’ of $t$ , $\gamma ( t )$ , is defined as the product over all vertices of the order of the subtree rooted at that vertex. We illustrate these definitions using a specific tree $( V , E )$ with nine vertices given by

$$
\begin{array} { l } { V = \{ a , b , c , d , e , f , g , h , i \} , } \\ { E = \{ [ a , b ] , [ a , c ] , [ b , d ] , [ b , e ] , [ b , f ] , [ c , g ] , [ c , h ] , [ c , i ] \} . } \end{array}
$$

The diagram representing this tree, with the vertex labels attached, is

![](images/aaf9e43c403d3660ad34a43fc74b050dd3c840c16d0ef3da920dffb45c36fb80.jpg)

The value of $r ( t )$ is, of course, 9. The symmetry group is the set of permutations generated by all members of the symmetric group on $\{ d , e , f \}$ , by all members of the symmetric group on $\{ g , h , i \}$ , and the group $S _ { 2 }$ generated by the single permutation, in which $b$ and $c$ are interchanged, $d$ and $g$ are interchanged, $e$ and $h$ are interchanged, and $f$ and $i$ are interchanged. Thus the order of the symmetry group is $\sigma ( t ) = 3 ! 3 ! 2 ! = 7 2$ . To calculate $\gamma ( t )$ , attach integers to the vertices as follows:

![](images/448ab88329382b747dfbf9dfbf70889cd0decda08d950502a305747f8eee3640.jpg)

leading to $\gamma ( t ) = 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 4 \cdot 4 \cdot 9 \ = 1 4 4$

We complete this subsection with a formal statement of recursions for the computation of $r ( t )$ , $\sigma ( t )$ and $\gamma ( t )$ .

Theorem 301A Let $t = [ t _ { 1 } ^ { \prime \prime \imath 1 } t _ { 2 } ^ { \prime \prime \imath 2 } \cdot \cdot \cdot t _ { k } ^ { \prime \prime \imath k } ]$ , where $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { k }$ are distinct trees. Then

$$
\begin{array} { l } { \displaystyle r ( t ) = 1 + \sum _ { i = 1 } ^ { k } m _ { i } r ( t _ { i } ) , } \\ { \displaystyle \sigma ( t ) = \prod _ { i = 1 } ^ { k } m _ { i } ! \sigma ( t _ { i } ) ^ { m _ { i } } , } \\ { \displaystyle \gamma ( t ) = r ( t ) \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) ^ { m _ { i } } . } \end{array}
$$

Furthermore,

$$
r ( \tau ) = \sigma ( \tau ) = \gamma ( \tau ) = 1 .
$$

Proof. To verify (301d), calculate $r$ , $\sigma$ and $\gamma$ for the single tree with one vertex. To prove (301a), add the numbers of vertices in the $m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { k }$ trees attached to the new root, and add one extra for the new root. In the calculation of $\gamma ( t )$ , the integers attached to the vertices in the $m _ { 1 } + m _ { 2 } +$ $\cdots + m _ { k }$ trees joined to the new root are the same as in the constituent trees themselves. The product of these integers, and the integer $r ( t )$ , gives the result (301c). Finally, (301b) follows by noting that the permutations which leave the vertex pairs, making up the list of edges, are just as in the individual attached trees, together with the additional permutations of the label sets amongst identical subtrees. 

# 302 Some combinatorial questions

We consider the question of labelling a tree $t$ with $r ( t )$ vertices, using the symbols $\{ 1 , 2 , \ldots , r ( t ) \}$ , under the following conditions:

(i) Each vertex receives one and only one label.   
(ii) Labellings that are equivalent under the symmetry group are counted only once.   
(iii) If $( i , j )$ is a labelled edge then $i < j$ .

The number of distinct ways of labelling the given tree $t$ will be denoted by $\alpha ( t )$ . A similar question, in which conditions (i) and (ii) apply, but (iii) does not, leads to a function $\beta ( t )$ . We have:

Theorem 302A

$$
\begin{array} { l } { \displaystyle \alpha ( t ) = \frac { r ( t ) ! } { \sigma ( t ) \gamma ( t ) } , } \\ { \displaystyle \beta ( t ) = \frac { r ( t ) ! } { \sigma ( t ) } . } \end{array}
$$

Proof. The value of $\beta ( t )$ is found by labelling the vertices of $t$ with all permutations and then dividing by $\sigma ( t )$ so as to count, only once, sets of labellings which are equivalent under symmetry. In the case of $\alpha ( t )$ , we are restricted by the requirement that, of the labels assigned to any vertex $\boldsymbol { v }$ and to its descendants, only the lowest may be assigned to $v$ . The product of the factors that must be divided out to satisfy this constraint is $\gamma ( t )$ . $\boxed { \begin{array} { r l } \end{array} }$

We now look at the enumeration question of the number of rooted trees of various orders.

Theorem 302B Let $\theta _ { k }$ , $k = 1 , 2 , 3 , \dots$ . denote the number of rooted trees with exactly $k$ vertices. Then,

$$
\theta _ { 1 } + \theta _ { 2 } x + \theta _ { 3 } x ^ { 2 } + \cdot \cdot \cdot = ( 1 - x ) ^ { - \theta _ { 1 } } ( 1 - x ^ { 2 } ) ^ { - \theta _ { 2 } } ( 1 - x ^ { 3 } ) ^ { - \theta _ { 3 } } \cdot \cdot \cdot \cdot .
$$

Before proving this result, we consider how (302c) is to be interpreted. The right-hand side can be formally expanded as a power series, and it can be seen that the coefficient of $x ^ { k }$ depends only on $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots , \theta _ { k }$ (and is independent of any of $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ if $k = 0$ ). Equate this to the coefficient of $x ^ { k }$ on the left-hand side and the result is a formula for $\theta _ { k + 1 }$ in terms of previous members of the $\theta$ sequence. In particular, $k = 0$ gives $\theta _ { 1 } = 1$ . We now turn to the justification of the result.

Proof. Let $\Theta _ { k } ( U )$ denote the number of trees of order $k$ that can be formed using the operation $( t _ { 1 } , t _ { 2 } , \ldots , t _ { n } ) \mapsto [ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } ]$ , where $t _ { 1 }$ , $t _ { 2 }$ , $\cdot \cdot \cdot$ , $t _ { n }$ are all members of $U$ which is assumed to be a subset of $T$ . In particular, $\Theta _ { k } ( T )$ is identical to $\theta _ { k }$ . Let $V$ denote the set $U \cup \{ \hat { t } \}$ , where ${ \hat { t } } \notin U$ . Every tree of the form $[ \hat { t } ^ { m } , \dots ]$ , with order $k$ , is included in a set with $\Theta _ { k } ( V ) - \Theta _ { k } ( U )$ members. However, there are the same number of members of this set as there are trees of order $k - r ( \hat { t } )$ of the form $[ \hat { t } ^ { m - 1 } , \dots ]$ . Thus, $\Theta _ { k } ( V ) - \Theta _ { k } ( U ) = \Theta _ { k - r ( \hat { t } ) } ( V )$ , which is equivalent to

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = ( 1 - x ^ { r ( \hat { t } ) } ) ( \Theta _ { 1 } ( V ) + \Theta _ { 2 } ( V ) x + \cdots ) .
$$

Since

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdot \cdot \cdot = 1 ,
$$

when $U$ is the empty set, we can successively compute the value of this expression when $U = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } \}$ using (302d) as

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = \prod _ { k = 1 } ^ { n } ( 1 - x ^ { r ( t _ { k } ) } ) ^ { - 1 } .
$$

Now assume that $t _ { 1 }$ , $t _ { 2 } , \ldots$ consist of all trees of orders up to some integer $p$ , and we can write (302e) as

$$
\Theta _ { 1 } ( U ) + \Theta _ { 2 } ( U ) x + \cdots = \prod _ { k = 1 } ^ { p } ( 1 - x ^ { k } ) ^ { - \theta _ { k } } .
$$

Since $\textstyle \prod _ { k = 1 } ^ { \infty }$ . $\Theta _ { i } ( U ) = \theta _ { i }$ if $i \le p + 1$ , we obtain the result by replacing $\textstyle \prod _ { k = 1 } ^ { p }$ by $\boxed { \begin{array} { r l } \end{array} }$

The values of $\theta _ { k }$ , computed using Theorem 302B, are shown in Table $3 0 2 ( \mathrm { I } )$ up to order 10. Also shown are the total numbers of trees up to a given order, and two further functions equal to the totals of the $\alpha ( t )$ and $\beta ( t )$ values for each order.

Various enumerations of rooted trees up to order 10   

<table><tr><td>n</td><td>0n</td><td>∑i=10i ∑r(t)=n a(t) ∑r(t)=n β(t)</td></tr><tr><td>1 1</td><td></td><td>1 1</td></tr><tr><td>2</td><td>1 2</td><td>1</td></tr><tr><td>3</td><td>2 4</td><td>2 9</td></tr><tr><td>4</td><td>4 8</td><td>6</td></tr><tr><td>5</td><td>9 17</td><td>24 625</td></tr><tr><td>6</td><td>20 37</td><td>120 7776</td></tr><tr><td>7</td><td>48 85</td><td>720 117649</td></tr><tr><td>8</td><td>115 200</td><td>5040 2097152</td></tr><tr><td>9 286</td><td>486</td><td>40320 43046721</td></tr><tr><td>10 719</td><td>1205</td><td>362880 1000000000</td></tr></table>

The entries in last two columns of Table 302(I) are important in classical combinatorics, although their roles in our work is only incidental. The sum of the $\beta ( t )$ for $r ( t ) = n$ is the number of fully labelled rooted trees with $n$ vertices, whereas the corresponding sum for $\alpha ( t )$ is the number of monotonically labelled rooted trees. It is easy to guess a formula for each of these totals, and we now verify these.

Theorem 302C Let $\begin{array} { r } { A _ { n } = \sum _ { r ( t ) = n } \alpha ( t ) , B _ { n } = \sum _ { r ( t ) = n } \beta ( t ) } \end{array}$ . Then

$$
A _ { n } = ( n - 1 ) ! , \quad B _ { n } = n ^ { n - 1 } .
$$

Proof. Let $X _ { n }$ denote the set of vectors of the form $[ x _ { 1 } , x _ { 2 } , \dotsc , x _ { n - 1 } ]$ and $Y _ { n }$ the set of vectors of the form $\left[ y _ { 1 } , y _ { 2 } , \dotsc , y _ { n - 1 } \right]$ , where $x _ { i } \in \{ 1 , 2 , \ldots , i \}$ and $y _ { i } \in \{ 1 , 2 , . . . , n \}$ , for $i = 1 , 2 , \ldots , n$ . It is easy to see that the cardinalities of these sets are $\# X _ { n } = ( n - 1 ) !$ , $\# Y _ { n } = n ^ { n - 1 }$ . We conclude the proof by showing how to define bijections between the monotonically labelled rooted trees of order $n$ and $X _ { n }$ and between the fully labelled rooted trees of order $n$ and $Y _ { n } .$ In each case, given a labelled rooted tree, let $v$ denote the leaf with greatest label and assign, as the value of $x _ { n - 1 }$ or $y _ { n - 1 }$ , respectively, the label attached to the parent of $v$ . Delete the leaf $v$ and continue the process until only the root remains. That is, in step $i = 1 , 2 , \ldots , n - 1$ , we work with a tree with $n + 1 - i$ vertices. We assign to $x _ { n - i }$ (or to $y _ { n - i }$ , respectively) the label attached to the parent of the leaf with the highest remaining label, and then delete this leaf to yield a tree with $n - i$ vertices. 

Although we have not included details of the bijections involved in this summarized proof, we illustrate these in the cases $n = 4$ , for monotonically labelled trees in Table 302(II), and $n = 3$ , for fully labelled trees in Table 302(III).

The bijection relating a monotonically labelled fourth order tree $t$ and $x \in X _ { 4 }$   

<table><tr><td>x</td><td>t</td><td>x t</td><td>x t</td></tr><tr><td>[1,1,1] 2</td><td>[1,1,2] 3</td><td>4 [1,1,3]</td><td>.4 3</td></tr><tr><td>[1,2,1] 4</td><td>3 [1,2,2]</td><td></td><td>E [1,2,3]</td></tr></table>

The bijection relating a fully labelled third order tree $t$ and $y \in Y _ { 3 }$

<table><tr><td>y t</td><td>y</td><td>t y</td><td>t</td></tr><tr><td>[1,1] 2 3</td><td>F [1,2]</td><td>[1,3]</td><td>5</td></tr><tr><td>[2,1] 1</td><td>[2,2]1</td><td>[2,3]</td><td>E</td></tr><tr><td>L [3,1]</td><td>E [3,2]</td><td></td><td></td></tr></table>

# 303 The use of labelled trees

We have seen that $\alpha ( t )$ , introduced in Subsection 302, is the number of distinct ways of labelling the vertices of $t$ with the integers $\{ 1 , 2 , \ldots , r ( t ) \}$ , on condition that for each edge $( i , j )$ , $i < j .$ It is convenient to generalize this by writing $S$ for an finite ordered set such that the cardinality is $\# S = r ( t )$ , and counting trees labelled with members of $S$ such that $i < j$ for each edge $( i , j )$ . Let $T _ { S } ^ { * }$ denote the set of trees labelled in this way and let $| \mathbf t |$ denote the member of $T$ corresponding to $\mathbf { t } \in T _ { S } ^ { * }$ , but with the vertex labels removed. This means that $\alpha ( t )$ can be interpreted as the number of members of $T _ { S } ^ { * }$ such that $| \cdot |$ maps them to $t \in T$ . Similarly, we write $T _ { S }$ for the set of trees labelled by a set with cardinality $r ( t )$ , where no assumption is made about order. In this case $\beta ( t )$ is the number of $\mathbf { t } \in T _ { S }$ , such that $| \mathbf { t } | = t$ .

# 304 Enumerating non-rooted trees

Recall the generating function for the numbers of rooted trees of various orders

$$
\theta ( x ) = \theta _ { 1 } + \theta _ { 2 } x + \theta _ { 3 } x ^ { 2 } + \cdot \cdot \cdot ,
$$

![](images/00dff3eda7dd4af2044d9dda13be2eec775a97d03ed67464fab4d9661e03a211.jpg)  
Trees with up to six vertices

where $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ are given in (302c). Also write

$$
\begin{array} { l } { { \phi ( x ) = \phi _ { 1 } + \phi _ { 2 } x + \phi _ { 3 } x ^ { 2 } + \cdots , } } \\ { { \psi ( x ) = \psi _ { 1 } + \psi _ { 2 } x + \psi _ { 3 } x ^ { 2 } + \cdots , } } \end{array}
$$

as the generating functions for the numbers of trees $\phi _ { i }$ of orders $i = 1 , 2 , \dots$ and the numbers of non-superfluous trees $\psi _ { i }$ . The meaning of ‘superfluous tree’ will become clear from the discussion which follows.

Given a tree, we can form a family of rooted trees by designating one of its vertices to be the root. We will refer to two such rooted trees as adjacent if the two roots are at the ends of the same edge in the underlying tree. For any particular vertex $\boldsymbol { v }$ , let $t = \left\lfloor t _ { 1 } , t _ { 2 } , \ldots , t _ { m } \right\rfloor$ and write $\phi ( v ) = \mathrm { m a x } _ { i = 1 } ^ { m } r ( t _ { i } )$ . There will be at most one vertex adjacent to $\boldsymbol { v }$ for which the value of $\phi$ is lower. However, for some trees with even order there will be two adjacent vertices for which the values of $\phi$ are each equal to $r ( t ) / 2$ . The 14 trees with up to six vertices are shown in Figure $\mathrm { 3 0 4 ( i ) }$ . The value of $\phi$ is attached to each vertex, with arrows showing the direction of decreasing $\phi$ . In the cases of two adjacent vertices $\boldsymbol { v }$ and $w$ with $\phi ( v ) = \phi ( w )$ , two arrows are shown meeting midway through the edge.

For a rooted tree formed from a tree by selecting a vertex as the root, we can move along an arrow to obtain a vertex with a lower value of $\phi$ . Thus we should subtract from the total number of rooted trees of a given order $n$ , the number of pairs or trees with unequal orders. This means subtracting the number of rooted trees of the form $t u$ , where $r ( t ) < r ( u )$ . In the case of trees where $n = 2 m$ is even, and for two adjacent vertices, the rooted trees $t u$ and ut occur, where $r ( t ) = r ( u )$ , we need to subtract half the number of such trees unless $t = u$ , in which case no subtraction is performed.

For a tree of order $\textit { n } = \ 2 m + 1$ , the number of trees will thus be $\begin{array} { r } { \theta _ { n } - \sum _ { i = 1 } ^ { m } \theta _ { i } \theta _ { n - i } } \end{array}$ , which is the coefficient of $x ^ { n - 1 }$ in

$$
\theta ( x ) - \frac { x } { 2 } \Bigl ( \theta ( x ) ^ { 2 } \mp \theta ( x ^ { 2 } ) \Bigr ) ,
$$

where the term involving $\theta ( x ^ { 2 } )$ does not actually contribute to this case of odd $n$ . In the case of even $n = 2 m$ , the number of trees will be

$$
\theta _ { n } - \sum _ { i = 1 } ^ { m - 1 } \theta _ { i } \theta _ { n - i } - \frac 1 2 \theta _ { m } ( \theta _ { m } \mp 1 ) ,
$$

where $\mp$ is interpreted as $^ -$ , and this is again equal to the coefficient of $x ^ { n - 1 }$ in (304a).

Counting non-superfluous trees is the same except that we need to subtract from the totals the number of trees of the form $t t$ , and this gives the same result as (304a) but with $\mp$ replaced by $^ +$ . Putting these results together we formally state:

Theorem 304A The generating functions for trees and non-superfluous trees are

$$
\begin{array} { c } { { \phi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } - \theta ( x ^ { 2 } ) \Big ) , } } \\ { { \psi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } + \theta ( x ^ { 2 } ) \Big ) . } } \end{array}
$$

# 305 Differentiation

We need to develop fairly intricate formulae involving derivatives of vectorvalued functions of vector arguments. Hence, in this subsection and the next, we review basic calculus ideas in a vector setting. We start with the elementary notions of the derivative of a real-valued function of a single real variable, and the partial derivatives of a real-valued function of several real variables. A real-valued function $f$ , whose domain contains an open interval around the real number $a$ , is differentiable at $a$ if there exists a number $f ^ { \prime } ( a )$ , referred to as the derivative of $f$ at $a$ , such that $| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta | / | \delta | \to 0$ a s $| \delta | \to 0$ . This definition is extended in two ways. First, $f$ can take values in $\mathbb { R } ^ { N }$ , in which case $f$ is differentiable if each of its components is differentiable. Furthermore, $f ^ { \prime } ( a ) \in \mathbb { R } ^ { N }$ is equal to the vector made up from the derivatives of the components of $f$ . Another way of writing this is

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { | \delta | } } \to 0 \quad { \mathrm { a s ~ } } | \delta | \to 0 .
$$

When the domain of $f$ is generalized to $X \subset \mathbb { R } ^ { M }$ , such that $a \in O \subset X$ , where $O$ is an open set, such as a product of open intervals, then $f ^ { \prime } ( a )$ , if it

exists, is a linear operator, $f ^ { \prime } ( a ) : \mathbb { R } ^ { M } \longrightarrow \mathbb { R } ^ { N }$ , such that

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { \| \delta \| } } \to 0 \quad { \mathrm { a s ~ } } \| \delta \| \to 0 .
$$

If the components of $a$ and $f$ are written as

$$
a = \left[ \begin{array} { c } { { a ^ { 1 } } } \\ { { a ^ { 2 } } } \\ { { \vdots } } \\ { { a ^ { M } } } \end{array} \right] , \qquad f = \left[ \begin{array} { c } { { f ^ { 1 } } } \\ { { f ^ { 2 } } } \\ { { \vdots } } \\ { { f ^ { N } } } \end{array} \right] ,
$$

then the linear operator $f ^ { \prime } ( a )$ is represented by the matrix of partial derivatives

$$
{ \bf \\xi } ^ { \prime } ( a ) = \left[ { \begin{array} { c c c c } { f _ { 1 } ^ { 1 } ( a ) } & { f _ { 2 } ^ { 1 } ( a ) } & { \cdots } & { f _ { M } ^ { 1 } ( a ) } \\ { f _ { 1 } ^ { 2 } ( a ) } & { f _ { 2 } ^ { 2 } ( a ) } & { \cdots } & { f _ { M } ^ { 2 } ( a ) } \\ { \vdots } & { \vdots } & & { \vdots } \\ { f _ { 1 } ^ { N } ( a ) } & { f _ { 2 } ^ { N } ( a ) } & { \cdots } & { f _ { M } ^ { N } ( a ) } \end{array} } \right] = \left[ { \begin{array} { c c c c } { { \frac { \partial f ^ { 1 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { M } } } } \\ { { \frac { \partial f ^ { 2 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { M } } } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { { \frac { \partial f ^ { N } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { N } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { N } } { \partial a ^ { M } } } } \end{array} } \right] .
$$

Second and higher derivatives are bilinear and multilinear operators. In the tensor representation

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } ( a ) = { \frac { \partial ^ { k } f ^ { i } } { \partial a _ { j _ { 1 } } \partial a _ { j _ { 2 } } \cdot \cdot \cdot \partial a _ { j _ { k } } } } ,
$$

the argument ( $a$ ) is omitted, for convenience, if its value is understood.

Finally, inoperating wicollection of this subsech the order arguments $k$ $f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i }$ at eva, as a gives $k$ uation of the result of-linear operator, on thehe expression $k$ $v _ { 1 } , v _ { 2 } , \ldots , v _ { k } \in \mathbb { R } ^ { M }$

$$
\sum _ { j _ { 1 } = 1 } ^ { M } \sum _ { j _ { 2 } = 1 } ^ { M } \cdot \cdot \cdot \sum _ { j _ { k } = 1 } ^ { M } f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

The complicated appearance of (305a) can be alleviated by omitting all the summation symbols and regarding them as implied. This is the wellknown ‘summation convention’, and we use this notational simplification freely throughout this book. Thus we write, instead of (305a),

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

Members of $\mathcal { I } _ { 2 }$ and their symmetries

$$
\sigma ( I ) | \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { I } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } &  { } \end{array}
$$

# 306 Taylor’s theorem

We start from the identity,

$$
\begin{array} { r } { f ( a + \delta ) = f ( a ) + f ^ { \prime } ( a ) ( \delta ) + \frac { 1 } { 2 ! } f ^ { \prime \prime } ( a ) ( \delta , \delta ) \qquad } \\ { + \dots + \displaystyle \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } , } \end{array}
$$

where the ‘remainder’ $R _ { n }$ is given by

$$
R _ { n } = \frac { 1 } { n ! } \int _ { 0 } ^ { 1 } f ^ { ( n + 1 ) } ( a + \xi \delta ) ( \delta , \delta , \ldots , \delta ) ( 1 - \xi ) ^ { n } d \xi .
$$

This is proved by induction, with the key step being

$$
R _ { n - 1 } = \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } ,
$$

which is verified by integration by parts. With Taylor’s theorem written in the form (306a), the result is quite versatile and applies if $f : X \subset \mathbb { R } ^ { M } \to \mathbb { R } ^ { N }$ , where $a + \xi \delta \in O \subset X$ , for all $\xi \in [ 0 , 1 ]$ . Assuming that $\| f ^ { ( n + 1 ) } ( x ) \|$ exists and is bounded for $x \in O$ , then

$$
\| R _ { n } \| = O ( \| \delta \| ^ { n + 1 } ) .
$$

We consider a slight variation of the theorem, in which $\delta$ is replaced by the sum of a finite number of vectors, $\delta _ { i }$ , $i = 1 , 2 , \dots , m$ . We assume that $f$ is analytic in a neighbourhood of $a$ and that each of the $\delta _ { i }$ is small. The formal result we present can be interpreted as a finite series, together with remainder, with the details dependent on the relative magnitudes of the $\delta _ { i }$ . Let $I$ denote a sequence of integers from the set $\{ 1 , 2 , \ldots , m \}$ and $\mathcal { L } _ { m }$ the set of all such sequences. Two sequences $I$ and $I ^ { \prime }$ will be regarded as identical if the members of $I ^ { \prime }$ are a permutation of the members of $I$ . The ‘symmetry’ of $I$ is the order of the group of permutations of the elements of $\{ 1 , 2 , \ldots , \# I \}$ , which maps the ordered members of $I$ to themselves. That is, if $I$ contains $k _ { i }$ occurrences of $i$ , for each $i = 1 , 2 , \dots , m$ , then

$$
\sigma ( I ) = k _ { 1 } ! k _ { 2 } ! \cdot \cdot \cdot k _ { m } ! .
$$

For $m = 2$ , the first few $I \in \mathcal { I } _ { m }$ , together with the corresponding symmetries, are given in Table 306(I).

For $I = ( i _ { 1 } , i _ { 2 } , \ldots , i _ { k } ) \in { \mathcal { T } } _ { m }$ , we denote by $\delta _ { I }$ the quantity

$$
( \delta _ { i _ { 1 } } , \delta _ { i _ { 2 } } , \ldots , \delta _ { i _ { m } } ) \in ( \mathbb { R } ^ { N } ) ^ { m } .
$$

These will be used as operands for multilinear operators, such as $f ^ { ( m ) } ( a )$ , and, in the case $I = ( )$ , we interpret $f ( a ) ( )$ as being simply $f ( a )$ . We are now in a position to state the form of the Taylor expansion (306a), when $\delta$ is replaced by $\textstyle \sum _ { i = 1 } ^ { \cdot { m } } \delta _ { i }$ .

Theorem 306A

$$
f \biggl ( a + \sum _ { i = 1 } ^ { m } \delta _ { i } \biggr ) = \sum _ { I \in \mathcal { T } _ { m } } \frac { 1 } { \sigma ( I ) } f ^ { ( \# I ) } ( a ) \delta _ { I } .
$$

Proof. Continue to write $k _ { i }$ for the number of occurrences of $i$ in $I$ , so that $\sigma ( I )$ is given by (306b). The coefficient of $f ^ { ( \# I ) } ( a ) \delta _ { I }$ is equal to the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in $\textstyle \exp \left( \sum _ { i = 1 } ^ { m } x _ { i } \right)$ . This equals the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in

$$
\begin{array} { r } { \left( 1 + x _ { 1 } + \frac { 1 } { 2 ! } x _ { 1 } ^ { 2 } + \cdot \cdot \cdot \right) \left( 1 + x _ { 2 } + \frac { 1 } { 2 ! } x _ { 2 } ^ { 2 } + \cdot \cdot \cdot \right) \cdot \cdot \left( 1 + x _ { m } + \frac { 1 } { 2 ! } x _ { m } ^ { 2 } + \cdot \cdot \cdot \right) } \end{array}
$$

and is equal to $1 / \sigma ( I )$ .

We illustrate this result by applying (306A) to the case $m = 2$ , using Table 306(I):

$$
\begin{array} { r l } & { f ( a + \delta _ { 1 } + \delta _ { 2 } ) = f ( a ) + f ^ { \prime } ( a ) \delta _ { 1 } + f ^ { \prime } ( a ) \delta _ { 2 } + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } , \delta _ { 2 } ) + \cdots \ . } \end{array}
$$

# Exercises 30

30.1 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = | \mathbf { t } |$ , where $| \mathbf { t } | = ( V , E )$ , with

$$
V = \{ a , b , c , d , e , f , g \} \mathrm { ~ a n d ~ } E = \{ ( a , b ) , ( b , c ) , ( b , d ) , ( a , e ) , ( e , f ) , ( e , g ) \} .
$$

30.2 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = [ [ \tau ] ^ { 2 } \tau ^ { 3 } ]$ .

30.3 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = \tau \tau \cdot ( \tau \tau \cdot \tau ) \tau$ .

30.4 Define $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ by

$$
f ( y ^ { 1 } , y ^ { 2 } , y ^ { 3 } ) = \left[ \begin{array} { c } { { y ^ { 1 } + y ^ { 2 } y ^ { 3 } } } \\ { { ( y ^ { 1 } ) ^ { 2 } + 2 y ^ { 1 } y ^ { 2 } } } \\ { { 1 + ( y ^ { 2 } + y ^ { 3 } ) ^ { 2 } } } \end{array} \right] .
$$

Find formulae for $f _ { j } ^ { i }$ , $f _ { j k } ^ { i }$ and $f _ { j k l } ^ { \imath }$ , for $i , j , k , l = 1 , 2 , 3$ .

30.5 Expand $f ( a + \delta _ { 1 } \xi + \delta _ { 2 } \xi ^ { 2 } + \delta _ { 3 } \xi ^ { 3 } )$ up to terms in $\xi ^ { 3 }$ using Theorem 306A.

# 31 Order Conditions

# 310 Elementary differentials

To investigate the error in carrying out a single step of a Runge–Kutta method, we need to compare successive terms in the Taylor expansions of the exact and the computed solutions. These involve expressions whose structures are related to rooted trees. In the case of the exact solution, it is possible to evaluate the Taylor coefficients by repeated differentiation. We start with a differential equation, assumed for convenience to be autonomous,

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) .
$$

We also write (310a) in component-by-component form, with arguments omitted for brevity, as

$$
( y ^ { i } ) ^ { \prime } = f ^ { i } .
$$

To obtain the second derivative, use the chain rule

$$
y ^ { \prime \prime } ( x ) = { \frac { d } { d x } } f ( y ( x ) ) = f ^ { \prime } ( y ( x ) ) y ^ { \prime } ( x ) = f ^ { \prime } ( y ( x ) ) f ( y ( x ) )
$$

or, using (310b) as the starting point,

$$
{ \frac { d } { d x } } ( y ^ { i } ) ^ { \prime } = { \frac { d } { d x } } f ^ { i } = f _ { j } ^ { i } f ^ { j } .
$$

Note that in (310d) we have used the summation convention. We continue to use this convention without further comment. The third derivative can be found in a similar manner, but is complicated by the fact that $y ( x )$ is present in both factors in $f ^ { \prime } ( y ( x ) ) f ( y ( x ) )$ . Even though we are omitting arguments, $y ( x )$ is also implicitly present in the tensor form $f _ { j } ^ { i } f ^ { j }$ . The two forms of the third derivative are

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 3 } } { d x ^ { 3 } } y ( x ) = f ^ { \prime \prime } ( y ( x ) ) \big ( f ( y ( x ) ) , f ( y ( x ) ) \big ) + f ^ { \prime } ( y ( x ) ) ( f ^ { \prime } ( y ( x ) ) f ( y ( x ) ) ) , } } \\ { { \displaystyle \quad \frac { d ^ { 3 } } { d x ^ { 3 } } y ^ { i } = f _ { j k } ^ { i } f ^ { j } f ^ { k } + f _ { j } ^ { i } f _ { k } ^ { j } f ^ { k } . } } \end{array}
$$

We can find a pattern in the terms occurring in the first, second and third derivatives, using rooted trees. In the total derivative form, (310a), (310c), (310e), we relate $f ( \boldsymbol { y } ( \boldsymbol { x } ) )$ to a leaf in a tree, we relate $f ^ { \prime } ( y ( x ) )$ to a vertex with a single outwardly directed edge, and we relate $f ^ { \prime \prime } ( y ( x ) )$ to a vertex with two outward edges. In the case of $f ^ { \prime }$ and $f ^ { \prime \prime }$ , the outward edges are joined to subtrees, as representatives of the operands of these linear and bilinear operators, respectively.

For the tensor representations of the terms in the first three derivatives of $y ^ { i }$ , we treat the superscripts in $f ^ { i }$ , $f ^ { j }$ , $f ^ { k }$ as members of the vertex set $V$ , and we define the edge set $E$ in terms of the pairs, such as $( i , j )$ that occur in $f _ { j } ^ { i }$ , $f _ { j k } ^ { i }$ .

Relation between terms in $_ y$ derivatives and rooted trees   

<table><tr><td>Tree</td><td>Operator diagram</td><td>Term</td><td>Labelled tree</td><td>Tensor term</td></tr><tr><td>. ！</td><td>·f</td><td>f(y(x))</td><td>·i</td><td>fi</td></tr><tr><td></td><td>1</td><td>f&#x27;(y(x))f(y(x))</td><td>I</td><td>ffj</td></tr><tr><td>V</td><td>V f</td><td>f&quot;(y(x))(f(y(x)),f(y(x)))</td><td>V</td><td>fikfi fk</td></tr><tr><td>！</td><td>I</td><td>f&#x27;(y(x))(f&#x27;(y(x)f(y(x)))</td><td>[L</td><td>ffk</td></tr></table>

Thus, we can identify four trees as representatives of the terms that occur in the first, second and third derivatives of $y$ . In Table 310(I) we illustrate this correspondence using both formulations. Note that we write f, $\mathbf { f ^ { \prime } }$ and $\mathbf { f } ^ { \prime \prime }$ as abbreviations for $f ( \boldsymbol { y } ( \boldsymbol { x } ) )$ , $f ^ { \prime } ( y ( x ) )$ and $f ^ { \prime \prime } ( y ( x ) )$ , respectively.

We can expect this pattern to continue, because the operation of differentiating adds an additional vertex to an existing tree, in a number of different ways, and each of these corresponds to a further tree.

Definition 310A Given a tree $t$ and a function $f : \mathbb { R } ^ { N } \to \mathbb { R } ^ { N }$ , analytic in a neighbourhood of $y$ , the ‘elementary differential’ $F ( t ) ( y )$ is defined by

$$
\begin{array} { c } { F ( \tau ) ( y ) = f ( y ) , } \\ { F ( [ t _ { 1 } , t _ { 2 } , \dotsc , t _ { m } ] ) = f ^ { ( m ) } ( y ) ( F ( t _ { 1 } ) ( y ) , F ( t _ { 2 } ) ( y ) , \dotsc , F ( t _ { m } ) ( y ) ) . } \end{array}
$$

Note that the tensor interpretation of (310h) is written as

$$
F ^ { i } ( [ t _ { 1 } , t _ { 2 } , \ldots , t _ { m } ] ) = f _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { m } } ^ { i } F ^ { j _ { 1 } } ( t _ { 1 } ) F ^ { j _ { 2 } } ( t _ { 2 } ) \cdot \cdot \cdot F ^ { j _ { m } } ( t _ { m } ) .
$$

The elementary differentials up to order 5 are shown in Table 310(II). Note that we use the same abbreviation as in Table 310(I), in which f, $\mathbf { f ^ { \prime } } , \ldots$ denote $f ( y ( x ) ) , f ( y ( x ) ) ^ { \prime } , \ldots .$ The values of $\alpha ( t )$ are also shown; their significance will be explained in the next subsection.

As part of the equipment we need to manipulate expressions involving elementary differentials we consider the value of

$$
h f \Big ( y _ { 0 } + \sum _ { t \in T } \theta ( t ) \frac { h ^ { r ( t ) } } { \sigma ( t ) } F ( t ) ( y _ { 0 } ) \Big ) .
$$

Elementary differentials for orders 1 to 5   

<table><tr><td>r(t）</td><td>t</td><td>a（t）</td><td>F(t）(y)</td><td>F(t)(y）)</td></tr><tr><td>1</td><td>·</td><td>1</td><td>f</td><td>fr</td></tr><tr><td>2</td><td>：</td><td>1</td><td>ff</td><td>ffj</td></tr><tr><td>3</td><td>?</td><td>1</td><td>f&quot;(f,f)</td><td>fikfj fk</td></tr><tr><td>3</td><td>·</td><td>1</td><td>fff</td><td>ffk</td></tr><tr><td>4</td><td>Y</td><td>1</td><td>f&quot;(f,f,f)</td><td>fikfi fk fl</td></tr><tr><td>4</td><td></td><td>3</td><td>f&quot;(f,ff)</td><td>fkfiffl</td></tr><tr><td>4</td><td>小</td><td>1</td><td>f&#x27;f&quot;(f,f)</td><td>fffkfl</td></tr><tr><td>4</td><td>：</td><td>1</td><td>ffff</td><td>ffffl</td></tr><tr><td>5</td><td>￥ 4</td><td>1</td><td>f(4)(f,f,f,f)</td><td>fjklmfj fk fl fm</td></tr><tr><td>5</td><td></td><td>6</td><td>f(3)(f,f,ff)</td><td>fikifjfkfmfm</td></tr><tr><td>5</td><td></td><td>4</td><td>f&quot;(f,f&quot;(f,f))</td><td>fkfjfimflfm</td></tr><tr><td>5</td><td></td><td>4</td><td>f&quot;(f,fff)</td><td>fikfifrfmfm</td></tr><tr><td>5</td><td></td><td>3</td><td>f&quot;(f&#x27;f,ff)</td><td>fikfiflffm</td></tr><tr><td>5</td><td>Y</td><td>1</td><td>ff&quot;(f,f,f)</td><td>ffklmfk flfm</td></tr><tr><td>5</td><td>广</td><td>3</td><td>f&#x27;f&quot;(f,ff)</td><td>fffkfmfm</td></tr><tr><td>5</td><td></td><td>1</td><td>f&#x27;ff&quot;(f,f)</td><td>ff fimfl fm</td></tr><tr><td>5</td><td>！</td><td>1</td><td>f&#x27;fff&#x27;f</td><td>ffffm</td></tr></table>

As a formal series, this can be evaluated using the following result:

Lemma 310B The value of (310i) is

$$
\sum _ { t \in T } \widetilde { \theta } ( t ) \frac { h ^ { r ( t ) } } { \sigma ( t ) } F ( t ) ( y _ { 0 } ) ,
$$

where $ { \widetilde { \theta } }$ is defined by

$$
\widetilde { \theta } ( t ) = \left\{ \begin{array} { l l } { 1 , } & { t = \tau , } \\ { \displaystyle \prod _ { i = 1 } ^ { k } \theta ( t _ { i } ) , } & { t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } ] . } \end{array} \right.
$$

Proof. Use Theorem 306A. The case $t = \tau$ is obvious. For $t = [ t _ { 1 } ^ { m _ { 1 } } t _ { 2 } ^ { m _ { 2 } } \cdot \cdot \cdot t _ { j } ^ { m _ { j } } ]$ $t _ { 1 }$ $t _ { 2 }$ $t _ { j }$ are distinct, the factor

$$
\Big ( \sigma ( I ) \prod _ { i = 1 } ^ { j } \sigma ( t _ { j } ) ^ { m _ { j } } \Big ) ^ { - 1 } ,
$$

where $I$ is the index set consisting of $m _ { 1 }$ copies of $^ { 1 }$ , $m _ { 2 }$ copies of 2, $\cdot \cdot \cdot$ and copies of $j$ , is equal to $\sigma ( t ) ^ { - 1 }$ . $\sqcup$ $m _ { j }$

# 311 The Taylor expansion of the exact solution

We approach the question of the Taylor series of the exact solution from two points of view. In the first, we evaluate the Taylor coefficients by repeated differentiation, as we have illustrated in Subsection 310. In the second, we successively find Taylor series for the Picard iterates.

The central result in the first approach is an expression for the derivatives written in terms of labelled trees. Throughout the discussion it will be assumed, without further comment, that $y$ is a solution to $y ^ { \prime } ( x ) = f ( y ( x ) )$ and that $y$ is differentiable arbitrarily often. First, we need a formula for the derivative of a single elementary differential.

Lemma 311A Let $S = S _ { 0 } \cup \{ s \}$ be an ordered set, where every member of $S _ { 0 }$ is less than $s$ . Let $\mathbf { t }$ be a member of $T _ { S _ { 0 } } ^ { * }$ . Then

$$
{ \frac { d } { d x } } F ( | \mathbf { t } | ) ( y ( x ) )
$$

is the sum of $F ( | \mathbf { u } | ) ( y ( x ) )$ over all $\mathbf { u } \in T _ { S } ^ { * }$ such that the subtree formed by removing $s$ from the set of vertices is $\mathbf { t }$ .

Proof. If $S = \{ s _ { 0 } , s \}$ , then the result is equivalent to

$$
{ \frac { d } { d x } } f ( y ( x ) ) = f ^ { \prime } ( y ( x ) ) f ( y ( x ) ) .
$$

We now complete the proof by induction in the case $S = \{ s _ { 0 } \} \cup S _ { 1 } \cup S _ { 2 } \cup \cdot \cdot \cdot \cup$ $S _ { k } \cup \{ s \}$ , where $\left\{ s _ { 0 } \right\}$ , $S _ { 1 }$ , $S _ { 2 }$ , . . . , $S _ { k }$ , $\{ s \}$ are disjoint subsets of the ordered set $S$ . By the induction hypothesis, assume that the result of the lemma is true, when $S$ is replaced by $S _ { i }$ , $i = 1 , 2 , \ldots , k$ . If $\mathbf { t } \in T _ { S _ { 0 } } ^ { * }$ , then

$$
| \mathbf { t } | = [ \left| \mathbf { t } _ { 1 } \right| \left| \mathbf { t } _ { 2 } \right| \cdot \cdot \cdot \left| \mathbf { t } _ { k } \right| ] ,
$$

where $\mathbf { t } _ { i } \in T _ { S _ { i } } ^ { * }$ , $i = 1 , 2 , \ldots , k$ . Differentiate

$$
\begin{array} { r l } & { F ( | \mathbf { t } | ) ( y ( x ) ) } \\ & { \qquad = f ^ { ( k ) } ( y ( x ) ) \bigl ( F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \dots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) \bigr ) , } \end{array}
$$

to obtain

$$
Q _ { 0 } + Q _ { 1 } + Q _ { 2 } + \cdot \cdot \cdot + Q _ { k } ,
$$

where

$$
Q _ { 0 } = f ^ { ( k + 1 ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) , f ( y ( x ) ) { \big ) }
$$

and, for $i = 1 , 2 , \ldots , k$ ,

$$
Q _ { i } = f ^ { ( k ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , \ldots , { \frac { d } { d x } } F ( | \mathbf { t } _ { i } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) { \big ) } .
$$

The value of $Q _ { 0 }$ is

$$
F ( \left[ \left. \mathbf { t } _ { 1 } \right. \left. \mathbf { t } _ { 2 } \right. \cdot \cdot \cdot \left. \mathbf { t } _ { k } \right. \left. \mathbf { t } _ { 0 } \right. \right] ) ( y ( x ) ) ,
$$

where $| \mathbf { t } _ { 0 } |$ is $\tau$ labelled with the single label $s$ . For $i = 1 , 2 , \ldots , k$ , the value of $Q _ { i }$ is the sum of all terms of the form (311a), with $F ( | \mathbf { t } _ { i } | ) ( y ( x ) )$ replaced by terms of the form $F ( | \mathbf { u } _ { i } | ) ( y ( x ) )$ , where $\mathbf { u } _ { i }$ is formed from $\mathbf { t } _ { i }$ by adding an additional leaf labelled by $s$ . The result of the lemma follows by combining all terms contributing to the derivative of (311a).

Theorem 311B Let $S$ denote a finite ordered set. Then

$$
y ^ { ( \# S ) } ( y _ { 0 } ) = \sum _ { \mathbf { t } \in T _ { S } } F ( | \mathbf { t } | ) ( y _ { 0 } ) .
$$

Proof. In the case $| \mathbf { t } | = \tau$ , the result is obvious. For the case $\# S > 1$ , apply Lemma 311A repeatedly by adding additional (and increasing) members to $S$ . 

We rewrite this result in terms of unlabelled trees, by noting that the number of times that a tree $t$ with order $\# S$ occurs as the unlabelled counterpart of a member of $T _ { S } ^ { * }$ , is exactly $\alpha ( t )$ .

# Theorem 311C

$$
y ^ { ( n ) } ( y ( x ) ) = \sum _ { t \in T _ { n } } \alpha ( t ) F ( t ) ( y ( x ) ) .
$$

The alternative approach to finding the Taylor coefficients is based on the Picard integral equation

$$
y ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y ( x _ { 0 } + h \xi ) ) d \xi ,
$$

which, written in terms of Picard iterations, becomes

$$
y _ { n } ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y _ { n - 1 } ( x _ { 0 } + h \xi ) ) d \xi ,
$$

where the initial iterate is given by

$$
y _ { 0 } ( x + h \xi ) = y ( x _ { 0 } ) .
$$

For $n = 1 , 2 , \ldots$ , we expand $y _ { n } ( x _ { 0 } + h \xi )$ for $\xi \in [ 0 , 1 ]$ , omitting terms that are $O ( h ^ { n + 1 } )$ .

Theorem 311D The Taylor expansion of $y _ { n }$ given by (311b) and (311c) is equal to

$$
y _ { n } = y ( x _ { 0 } ) + \sum _ { i = 1 } ^ { n } h ^ { i } \xi ^ { i } \sum _ { t \in T _ { i } } \frac { 1 } { \sigma ( t ) \gamma ( t ) } F ( t ) ( y ( x _ { 0 } ) ) + O ( h ^ { n + 1 } ) .
$$

Proof. The case $n = 0$ is obvious. We now use induction and suppose that (311d) is true with $n$ replaced by $n - 1$ . By Lemma 310B, with

$$
\theta ( t ) = \frac { 1 } { \gamma ( t ) } ,
$$

we have as the coefficient of $F ( t ) ( y ( x _ { 0 } ) ) h ^ { r ( t ) }$ , the expression

$$
\int _ { 0 } ^ { \xi } \frac { 1 } { \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) - 1 } { d \xi } = \frac { 1 } { r ( t ) \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) } = \frac { 1 } { \gamma ( t ) } \xi ^ { r ( t ) } ,
$$

where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ .

# 312 Elementary weights

Having found the Taylor expansion of the exact solution to an initial value problem, we now find the corresponding expansion for the approximation computed by a Runge–Kutta method. A term-by-term comparison of these will provide criteria for the error generated in a single step to be zero, except for terms that can be estimated in terms of high powers of the stepsize $h$ .

As a prelude, we consider a three-stage explicit Runge–Kutta method. We find the Taylor expansion in this simple case up to terms in $h ^ { 3 }$ . As the standard problem that we use for studying Runge–Kutta methods, we consider the autonomous initial value system

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { N } \to \mathbb { R } ^ { N }$ . The method has the tableau

$$
\left. \begin{array} { c } { { 0 } } \\ { { c _ { 2 } } } \\ { { c _ { 3 } } } \\ { { b _ { 1 } } } \end{array} \right| _ { { c _ { 3 } } } - a _ { 3 2 } \quad a _ { 3 2 } \qquad \mathrm { ~ . ~ }
$$

Denote by $Y _ { 1 }$ , $Y _ { 2 }$ and $Y _ { 3 }$ the results computed at the stages and $y _ { 1 }$ for the result computed at the end of the step.

We can in turn find truncated Taylor expansions for the stages and the output result. We also use Theorem 306A to evaluate the Taylor expansions of $h F _ { i } = h f ( Y _ { i } )$ , for $i = 1 , 2 , 3 .$ . Note that the stage values need only terms up to $h ^ { 2 }$ , because the extra $h$ in $h F _ { i }$ takes away the need to find $h ^ { 3 }$ terms except for the $h F _ { i }$ terms and the final result:

$$
\begin{array} { r l } & { Y _ { 1 } = y _ { 0 } , } \\ & { h F _ { 1 } = h _ { 0 } / ( y _ { 0 } ) , } \\ & { Y _ { 2 } = y _ { 0 } + c _ { 2 } h / ( y _ { 0 } ) , } \\ & { h F _ { 2 } = h _ { 0 } + c _ { 2 } h / ( y _ { 0 } ) , } \\ & { Y _ { 3 } = h _ { 0 } + ( c _ { 3 } - a _ { 5 } ) h / ( y _ { 0 } ) + a _ { 5 } 2 c _ { 2 } ^ { 3 } h / ^ { \prime \prime } ( y _ { 0 } ) ( f ( y _ { 0 } ) , f ( y _ { 0 } ) ) + O ( h ^ { 3 } ) , } \\ & { \qquad \quad \gamma _ { 3 } = y _ { 0 } + ( c _ { 3 } - a _ { 5 } ) h f ( y _ { 0 } ) + a _ { 5 } 2 ( h f ( y _ { 0 } ) + c _ { 2 } h ^ { 2 } / ( y _ { 0 } ) f ( y _ { 0 } ) ) + O ( h ^ { 3 } ) , } \\ & { \qquad \quad = y _ { 0 } + c _ { 3 } h f ( y _ { 0 } ) + a _ { 3 } 2 c _ { 2 } ^ { 3 } h ^ { \prime } f ( y _ { 0 } ) f ( y _ { 0 } ) + O ( h ^ { 3 } ) , } \\ & { h F _ { 3 } = h f ( y _ { 0 } ) + c _ { 3 } h ^ { 2 } f ^ { \prime } ( y _ { 0 } ) f ( y _ { 0 } ) + a _ { 5 } 2 c _ { 2 } h ^ { 2 } f ^ { \prime } ( y _ { 0 } ) f ( y _ { 0 } ) f ( y _ { 0 } ) } \\ & { \qquad \quad + \frac { 1 } { 2 } c _ { 2 } ^ { 3 } h ^ { 3 } f ^ { \prime \prime } ( y _ { 0 } ) ( f ( y _ { 0 } ) , f ( y _ { 0 } ) ) + O ( h ^ { 4 } ) , } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \qquad \quad \quad \quad \end{array}
$$

We recognize elementary differentials, evaluated at $y _ { 0 }$ , appearing in these expansions and we rewrite $y _ { 1 }$ as

$$
\begin{array} { r l } & { y _ { 1 } = y _ { 0 } + h \Phi ( \bullet ) F ( \bullet ) ( y _ { 0 } ) + h ^ { 2 } \Phi ( \mathfrak { T } ) F ( \mathfrak { T } ) ( y _ { 0 } ) } \\ & { \qquad + \frac { 1 } { 2 } h ^ { 3 } \Phi ( \pmb { \mathbb { Y } } ) F ( \pmb { \mathbb { Y } } ) ( y _ { 0 } ) + h ^ { 3 } \Phi \left( \mathfrak { T } \right) F \left( \mathfrak { T } \right) ( y _ { 0 } ) + O ( h ^ { 4 } ) , } \end{array}
$$

where the coefficients associated with the four trees of orders up to 3 are given by

$$
\begin{array} { r l } & { \Phi ( \bullet ) = b _ { 1 } + b _ { 2 } + b _ { 3 } , } \\ & { \Phi ( \mathbf { \widehat { t } } ) = b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } , } \\ & { \Phi ( \mathbf { \widehat { V } } ) = b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } , } \\ & { \Phi \left( \mathbf { \widehat { f } } \right) = b _ { 3 } a _ { 3 2 } c _ { 2 } . } \end{array}
$$

It is obvious that these expressions, which we have already introduced in Section 234, are of vital importance in understanding the accuracy of Runge– Kutta methods. We name them ‘elementary weights’ and define them formally, along with similar expressions associated with the individual stages, in the next definition. At the same time we define ‘derivative weights’ associated with the stages.

Relation between elementary weights and rooted trees   

<table><tr><td>labelled tree t</td><td>Elementary weight Φ(t) S</td></tr><tr><td>·i</td><td>M bi i=1</td></tr><tr><td>1</td><td>S S M biaij= &gt; biCi i,j=1 i=1</td></tr><tr><td>k I</td><td>S S bic² £ biaijaik = ? i,j,k=1 i=1 s S M M</td></tr></table>

Definition 312A Let

$$
\frac { c \mid A } { b ^ { \textsf { T } } }
$$

denote the tableau for an $s$ -stage Runge–Kutta method. Then the ‘elementary weights’ $\Phi ( t )$ , the ‘internal weights’ $\Phi _ { i } ( t )$ and the ‘derivative weights $\mathbf { \nabla } ^ { \prime } ( \Phi _ { i } D ) ( t )$ for $t \in T$ and $i = 1 , 2 , \dots , s$ are defined by

$$
\begin{array} { c } { { ( \Phi _ { i } D ) ( \tau ) = 1 , } } \\ { { \displaystyle \Phi _ { i } ( t ) = \sum _ { j = 1 } ^ { s } a _ { i j } ( \Phi _ { j } D ) ( t ) , } } \\ { { \displaystyle ( \Phi _ { i } D ) ( [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot { t _ { k } } ] ) = \prod _ { j = 1 } ^ { k } \Phi _ { i } ( t _ { j } ) , } } \\ { { \displaystyle \Phi ( t ) = \sum _ { i = 1 } ^ { s } b _ { i } ( \Phi _ { i } D ) ( t ) . } } \end{array}
$$

This definition is used recursively. First $\Phi _ { i } D$ is found for $t = \tau$ , using (312a), then $\Phi _ { i }$ is evaluated for this single vertex tree, using (312b). This enables $( \Phi _ { i } D ) ( [ \tau ] )$ , using (312c), and then $\Phi _ { i } ( [ \tau ] )$ to be found for each stage. The order is built up in this way until $( \Phi _ { i } D ) ( t )$ is known for any required tree. Finally, (312d) is used to evaluate $\Phi ( t )$ .

The notation $\Phi _ { i } D$ is part of a more general scheme, which we introduce in Subsection 387. In the meantime, $D$ should be thought of as an operator to be applied to $\Phi _ { i }$ , which replaces the sequence of Taylor coefficient weights in a stage value by the set of coefficient weights for the stage derivatives.

Elementary weights for orders 1 to 5   

<table><tr><td>r(t)</td><td>t</td><td>（t）</td><td></td></tr><tr><td>1</td><td></td><td></td><td>∑i-1bi</td></tr><tr><td>2</td><td></td><td>：</td><td>∑i=1bici</td></tr><tr><td></td><td>?</td><td></td><td>∑i=1bic²</td></tr><tr><td>3</td><td></td><td>·</td><td></td></tr><tr><td>3</td><td></td><td></td><td>∑ij=1biaijj</td></tr><tr><td>4</td><td>Y</td><td></td><td>∑i=1bic</td></tr><tr><td>4</td><td>丫</td><td></td><td>∑ij=1biqaigGj</td></tr><tr><td>4</td><td></td><td></td><td>ij=1bai</td></tr><tr><td>4</td><td></td><td>！</td><td>∑ij=1iaijajC</td></tr><tr><td>5</td><td>Y</td><td></td><td>∑i-1bic</td></tr><tr><td>5</td><td></td><td>Y</td><td>∑ij=1bic2aijC</td></tr><tr><td>5</td><td>?</td><td></td><td>∑ij=1biciaije²</td></tr><tr><td>5</td><td></td><td>?</td><td>∑ij=1ijjk</td></tr><tr><td>5</td><td>Y</td><td></td><td>∑i-1bi(∑j=1aijc)）²</td></tr><tr><td>5</td><td></td><td>Y</td><td>Eij=1baig</td></tr><tr><td>5</td><td>丫</td><td></td><td>∑ijk=1biaijjajkCk</td></tr><tr><td></td><td></td><td>丫</td><td></td></tr><tr><td></td><td></td><td></td><td>ij=1biaijaj</td></tr><tr><td></td><td></td><td></td><td>ij=1biaigajac</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

An alternative formula for $\Phi ( t )$ , which uses the vertex and edge characterization of each tree $t$ , is given in the following lemma, which we state without proof.

Lemma 312B Denote the vertex set $V$ of the tree $t$ by the set of index symbols $V = \{ j , k , l , \dots \}$ , where $j$ is the root of $t$ . Let the corresponding edge set be $E$ . Form the expression

$$
b _ { j } \prod _ { ( k , l ) \in E } a _ { k l }
$$

and sum this over each member of $V$ ranging over the index set $\{ 1 , 2 , \ldots , s \}$ .

The resulting sum is the value of $\Phi ( t )$ . A similar formula for $\Phi _ { i } ( t )$ , where $i$ is not a member of $V$ , is found by replacing (312e) by

$$
a _ { i j } \prod _ { ( k , l ) \in E } a _ { k l }
$$

and summing this as for $\Phi ( t )$

Note that, although $c$ does explicitly appear in Definition 312A or Lemma 312B, it is usually convenient to carry out the summations $\textstyle \sum _ { l = 1 } ^ { s } a _ { k l }$ to yield a result $c _ { k }$ if $\it l$ denotes a leaf (terminal vertex) of $V$ . This is possible because $\it l$ occurs only once in (312e) and (312f).

We illustrate the relationship between the trees and the corresponding elementary weights in Table 312(I). For each of the four trees, we write $\Phi ( t )$ in the form given directly by Lemma 312B, and also with the summation over leaves explicitly carried out. Finally, we present in Table 312(II) the elementary weights up to order 5.

# 313 The Taylor expansion of the approximate solution

We show that the result output by a Runge–Kutta methods is exactly the same as (311d), except that the factor $\gamma ( t ) ^ { - 1 }$ is replaced by $\Phi ( t )$ . We first establish a preliminary result.

Lemma 313A Let $k = 1 , 2 , \ldots ,$ . If

$$
Y _ { i } = y _ { 0 } + \sum _ { r ( t ) \leq k - 1 } { \frac { 1 } { \sigma ( t ) } } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k } ) ,
$$

then

$$
h f ( Y _ { i } ) = \sum _ { r ( t ) \leq k } \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k + 1 } ) .
$$

Proof. Use Lemma 310B. The coefficient of $\sigma ( t ) ^ { - 1 } F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in $h f ( Y _ { i } )$ is $\textstyle \prod _ { j = 1 } ^ { n } \Phi _ { i } ( t _ { j } )$ , where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ . $\boxed { \begin{array} { r l } \end{array} }$

We are now in a position to derive the formal Taylor expansion for the computed solution. The proof we give for this result is for a general Runge– Kutta method that may be implicit. In the case of an explicit method, the iterations used in the proof can be replaced by a sequence of expansions for $Y _ { 1 }$ , for $h f ( Y _ { 1 } )$ , for $Y _ { 2 }$ , for $h f ( Y _ { 2 } )$ , and so on until we reach $Y _ { s }$ , $h f ( Y _ { s } )$ and finally $y _ { 1 }$ .

Theorem 313B The Taylor expansions for the stages, stage derivatives and output result for a Runge–Kutta method are

$$
\begin{array} { c } { { Y _ { i } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle h f ( Y _ { i } ) = \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) . } } \end{array}
$$

Proof. In a preliminary part of the proof, we consider the sequence of approximations to $Y _ { i }$ given by

$$
\begin{array} { l l } { { { \displaystyle Y _ { i } ^ { [ 0 ] } = y _ { 0 } } , } } & { { i = 1 , 2 , \ldots , s , } } \\ { { { \displaystyle Y _ { i } ^ { [ k ] } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f \left( Y _ { j } ^ { [ k - 1 ] } \right) , \ } } } & { { i = 1 , 2 , \ldots , s . } } \end{array}
$$

We prove by induction that Y [n]i agrees with the expression given for $Y _ { i }$ to within $O ( h ^ { n + 1 } ) .$ For $n = 0$ this is clear. For $n > 0$ , suppose it has been proved for $n$ replaced by $n - 1$ . From Lemma 313A with $k = n - 1$ and $Y _ { i }$ replaced by $Y _ { i } ^ { \lfloor n - 1 \rfloor }$ , we see that

$$
k f ( Y _ { i } ^ { [ n - 1 ] } ) = \sum _ { r ( t ) \leq n } { \frac { 1 } { \sigma ( t ) } } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { n + 1 } ) , \quad i = 1 , 2 , \ldots , s .
$$

Calculate Y [n]i using (313c) and the preliminary result follows. Assume $h$ tly to mall to guarantee convergence of the sequenceand (313c) follows. Finally, (313d) follows from $( Y _ { i } ^ { [ 0 ] } , Y _ { i } ^ { [ 1 ] } , Y _ { i } ^ { [ 2 ] } , \dots )$ $Y _ { i }$ Lemma 313A and (313e) from (312d). 

# 314 Independence of the elementary differentials

Our aim of comparing the Taylor expansions of the exact and computed solutions to an initial value problem will give an inconclusive answer unless the terms involving the various elementary differentials can be regarded as independent. We introduce a special type of differential equation for which any finite number of elementary differentials evaluate to independent vectors.

Let $U$ denote any finite subset of $T$ , such that if

$$
t _ { i } = [ t _ { 1 } ^ { m _ { 1 } } , t _ { 2 } ^ { m _ { 2 } } , \ldots , t _ { k } ^ { m _ { k } } ] \in U ,
$$

Trees to order 4 with corresponding differential equations   

<table><tr><td>i</td><td colspan="2">ti</td><td>yi</td><td>=fi</td></tr><tr><td>1</td><td>.</td><td></td><td>[]</td><td>y=1,</td></tr><tr><td>2</td><td></td><td>：</td><td>[t1]</td><td>y= y1,</td></tr><tr><td>3</td><td>?</td><td></td><td>[t]</td><td>y=y²，</td></tr><tr><td>4</td><td></td><td></td><td>[t2]</td><td>y4=y2,</td></tr><tr><td>5</td><td>?</td><td></td><td>[t]</td><td>y5=y，</td></tr><tr><td>6</td><td></td><td></td><td>[t1t2]</td><td>y = y1y2,</td></tr><tr><td>7</td><td>丫</td><td>：</td><td>[t3]</td><td>y= y3,</td></tr><tr><td>8</td><td></td><td></td><td>[t4]</td><td>y&#x27;s= y4.</td></tr></table>

then each of $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { k }$ is also a member of $U$ . For example, $U$ might consist of all trees with orders up to some specified integer. Assume that when we write a tree in this way, the $t _ { i }$ , $i = 1 , 2 , \ldots , k$ , are all distinct. Suppose that $N$ is the number of members of $U$ , and consider the $m$ -dimensional differential equation system in which

$$
y _ { i } ^ { \prime } = \prod _ { j = 1 } ^ { k } \frac { y _ { j } ^ { m _ { j } } } { m _ { j } ! } ,
$$

corresponding to tree number $i$ defined in (314a). The initial values are supposed to be $y _ { i } ( 0 ) ~ = ~ y _ { i } ( x _ { 0 } ) ~ = ~ 0$ , for $i = 1 , 2 , \ldots , N$ . The interesting property of this initial value problem is encapsulated in the following result:

Theorem 314A The values of the elementary differentials for the differential equation (314b), evaluated at the initial value, are given by

$$
F ( t _ { i } ) ( y ( x _ { 0 } ) ) = e _ { i } , \qquad i = 1 , 2 , \ldots , N .
$$

Because the natural basis vectors $e _ { 1 } , e _ { 2 } , \ldots , e _ { N }$ are independent, there cannot be any linear relation between the elementary differentials for an arbitrary differential equation system.

We illustrate this theorem in the case where $U$ consists of the eight trees with up to four vertices. Table 314(I) shows the trees numbered from $i = 1$ to $i = 8$ , together with their recursive definitions in the form (314a) and the corresponding differential equations. Note that the construction given here is given as an exercise in Hairer, Nørsett and Wanner (1993) .

# 315 Conditions for order

Now that we have expressions for the Taylor expansions of the exact solution, and also of the computed solution, we have all we need to find conditions for order. If the exact solution has Taylor series given by (311d) and the approximate solution has Taylor series given by (313e), then we need only compare these term by term to arrive at the principal result on the order of Runge–Kutta methods.

Theorem 315A A Runge–Kutta method with elementary weights

$$
\Phi : T  \mathbb { R } ,
$$

has order $p$ if and only if

$$
\Phi ( t ) = { \frac { 1 } { \gamma ( t ) } } , { \mathrm { ~ } } f o r { \mathrm { ~ } } a l l \ t \in T { \mathrm { ~ } } s u c h { \mathrm { ~ } } t h a t r ( t ) \leq p .
$$

Proof. The coefficient of $F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in (313e) is $\begin{array} { r } { \frac { 1 } { \sigma ( t ) } \Phi ( t ) } \end{array}$ , compared with the coefficient in (311d), which is $\frac { 1 } { \sigma ( t ) \gamma ( t ) }$ . Equate these coefficients and we obtain (315a). $\boxed { \begin{array} { r l } \end{array} }$

# 316 Order conditions for scalar problems

Early studies of Runge–Kutta methods were built around the single scalar equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) .
$$

Even though it was always intended that methods derived for (316a) should be interpreted, where appropriate, in a vector setting, a subtle difficulty arises for orders greater than 4.

We adopt the notation $f _ { x }$ , $f _ { y }$ for partial derivatives of $f$ with respect to the first and second arguments, with similar notations for higher derivatives. Also, for simplicity, we omit the arguments in expressions like $f _ { x } ( x , y )$ . By straightforward differentiation of (316a), we have

$$
y ^ { \prime \prime } = f _ { x } + f _ { y } y ^ { \prime } = f _ { x } + f _ { y } f ,
$$

where the two terms together correspond to the elementary differential associated with $t = \mathbb { I }$ Similarly, for the third derivative we have

$$
y ^ { \prime \prime \prime } = { \left( { { f _ { x x } } + 2 { f _ { x y } } f + { f _ { y y } } { f ^ { 2 } } } \right) + \left( { { f _ { y } } ( { f _ { x } } + { f _ { y } } { f } ) } \right) } ,
$$

where the grouped terms correspond to $t = \mathsf { Y }$ and $t = { \mathfrak { f } }$ respectively.

The expressions that arise here, and for the fourth derivative, are more complicated, because of the presence of derivatives with respect to $x$ . However, the terms can be grouped together according to the elementary differentials to which they correspond. Furthermore, the order conditions are identical to those found in the general vector case. When similar expressions are worked out for the 17 elementary differentials of order 5, we find a confusion between the results for two particular trees. In fact for each of $t _ { 1 } = { \sqrt [ { \object Object] { \operatorname { \rho } } } } \mathrm { a n d } t _ { 2 } = { \sqrt [ { \math { \rho } } } , F$ $F ( t )$ reduces to

$$
F ( t ) = f _ { y } ( f _ { y y } f + f _ { x y } ) ( f _ { y } f + f _ { x } ) ,
$$

and instead of two order conditions

$$
\Phi ( t _ { 1 } ) = \sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } = { \frac { 1 } { \gamma ( t _ { 1 } ) } } = { \frac { 1 } { 3 0 } }
$$

and

$$
\Phi ( t _ { 2 } ) = \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac 1 { \gamma ( t _ { 2 } ) } = \frac 1 { 4 0 } ,
$$

we have the single condition

$$
\sum b _ { i } c _ { i } a _ { i j } a _ { j k } c _ { k } + \sum b _ { i } a _ { i j } c _ { j } a _ { j k } c _ { k } = \frac { 7 } { 1 2 0 } .
$$

We discuss in Subsection 325 the construction of fifth order methods. These usually satisfy the so-called $D ( 1 )$ condition, which we introduce in Subsection 321. This simplifying assumption has, as one of its consequences, the dependence of (316b) on other conditions, for which there is no confusion. Hence, for methods satisfying $D ( 1 )$ , scalar and vector order 5 conditions are equivalent.

For orders 6 and higher, the confusion between the order conditions for the scalar case becomes more pronounced. The first published methods of this order(Huˇta, 1956, 1957) were derived for scalar problems but, nevertheless, have order 6 for the general vector case (Butcher, 1963a).

# 317 Independence of elementary weights

We show in Subsection 324 that, given a positive integer $p$ , there exists an integer $s$ such that there is a Runge–Kutta method with $s$ stages with order $p$ . We now present a more general result on the independence of the elementary weights but without a specific value of $s$ given.

Theorem 317A Given a finite subset $T _ { 0 }$ , of $T$ and a mapping $\phi : T _ { 0 }  \mathbb { R }$ , there exists a Runge–Kutta method such that the elementary weights satisfy

$$
\Phi ( t ) = \phi ( t ) , \qquad f o r \ a l l \ t \in T _ { 0 } .
$$

Proof. Let $\# T _ { 0 } = n$ . The set of possible values that can be taken by the vector of $\Phi ( t )$ values, for all $t \in T _ { 0 }$ , is a vector space. To see why this is the case, consider Runge–Kutta methods given by the tableaux

$$
{ \frac { c \left| \ A \right. } { \left| \ b ^ { \mathsf { T } } \right. } } \qquad { \mathrm { a n d } } \qquad { \frac { \overline { { c } } } { \overline { { b } } ^ { \mathsf { T } } } } \qquad { \frac { \overline { { A } } } { \overline { { b } } ^ { \mathsf { T } } } }
$$

with $s$ and $\overline { { s } }$ stages, respectively. If the elementary weight functions for these two Runge–Kutta methods are $\Phi$ and $\overline { { \Phi } }$ , then the method given by the tableau

$$
\frac { c } { c } \left| \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { \overline { { { A } } } } } \\ { { \theta b ^ { \intercal } } } & { { \overline { { { \theta } } } \overline { { { b } } } ^ { \intercal } } } \end{array} \right.
$$

has elementary weight function $\theta \Phi + { \overline { { \theta \Phi } } }$ . Let $V \subset \mathbb { R } ^ { n }$ denote this vector space. We complete the proof by showing that $V = \mathbb { R } ^ { n } .$ If this were not the case, there would exist a non-zero function $\psi : T _ { 0 } \to \mathbb { R }$ such that $\begin{array} { r } { \sum _ { t \in T _ { 0 } } \psi ( t ) \Phi ( t ) = 0 } \end{array}$ , for all Runge–Kutta methods. Because every coefficient in a Runge–Kutta tableau can be multiplied by an arbitrary scalar $\theta$ to give a new method for which $\Phi ( t )$ is replaced by $\theta ^ { r ( t ) } \Phi ( t )$ , we may assume that every non-zero value of $\psi$ corresponds to trees with the same order $k$ . This is impossible for $k = 1$ , because in this case there is only a single tree $\tau$ . Suppose the impossibility of this has been proved for all orders less than $k$ , but that there exist trees Kutta methods with $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { m }$ , each of order $\psi ( t _ { i } ) \neq 0$ $k$ , such that , for $i = 1 , 2 , \dots , m$ $\textstyle \sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \Phi ( t _ { i } ) = 0$ . Write $t _ { i } = [ t _ { i 1 } ^ { l _ { i 1 } } t _ { i 2 } ^ { l _ { i 2 } } \cdot \cdot \cdot ]$ , for all Runge– , for $i = 1 , 2 , \dots , m$ . Let $\hat { t }$ denote a tree appearing amongst the $t _ { i j }$ which does not occur with the same exponent in each of the $t _ { i }$ . Construct an $s$ -stage Runge–Kutta method

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

for which each of $\Phi ( t _ { i j } ) = 1$ , except for $\Phi ( \hat { t } ) = \theta$ . Define second Runge–Kutta tableau with $s + 1$ stages of the form

$$
{ \frac { c \ \boxed { A } \ 0 } { 1 \ \boxed { b ^ { \intercal } } \ 0 } } \ .
$$

If $q _ { i }$ is the exponent of $\hat { t }$ in $t _ { i }$ , then it follows that

$$
\sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \theta ^ { q _ { i } } = 0 .
$$

Since $\theta$ can take any value and since $q _ { i }$ is not constant, it is not possible that $\psi$ is never zero. 

# 318 Local truncation error

The conditions for order give guarantees that the Taylor expansions of the exact and computed solutions agree up to terms in $h ^ { p }$ . Obtaining an understanding of the respective terms in $h ^ { p + 1 }$ is regarded as a key to deriving methods that not only have a specific order, but also have a small truncation error. Because the number of terms of this order rises rapidly as $p$ increases, it is extremely difficult to know how this sort of optimality should be arrived at. Picking out just the terms of order $p + 1$ , we can write the local truncation error in a single step as

$$
h ^ { p + 1 } \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left( \frac { 1 } { \gamma ( t ) } - \Phi ( t ) \right) F ( t ) ( y _ { 0 } ) + O ( h ^ { p + 2 } ) .
$$

Since we are interested in asymptotic behaviour, that is, limiting behaviour for $h$ small, we do not devote much attention to the term $O ( h ^ { p + 2 } )$ . The coefficient of $h ^ { p + 1 }$ in (318a) is bounded in magnitude by

$$
\sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| ,
$$

and this should somehow be made small. There is simply no general rule interrelating the magnitudes of the various elementary differentials, and some assumptions need to be made.

expression fo The first approach that can be considered is to compare, term by term, the r 1(p+1)! y(p+1)(x0), which is proportional to the local truncation error coefficient for linear multistep methods or for implicit Runge–Kutta methods of collocation type. The coefficient in this expression, corresponding to $t$ , is

$$
{ \frac { 1 } { \sigma ( t ) \gamma ( t ) } } ,
$$

so that the corresponding multiplier to yield the corresponding term in (318b) is

$$
| \gamma ( t ) \Phi ( t ) - 1 | .
$$

Hence, we can bound (318b) by

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 | \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) \gamma ( t ) } \cdot \| F ( t ) ( y _ { 0 } ) \|
$$

and hence, it might be desirable to minimize

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 |
$$

in seeking an efficient method.

Another approach would be to assume a bound $M$ on $\| f \|$ , a bound $L$ on the linear operator $\| f ^ { \prime } \|$ , and further bounds to make up the sequence

$$
\begin{array} { r l } & { \| f \| \leq M , } \\ & { \| f ^ { \prime \prime } \| \leq L , } \\ & { \| f ^ { \prime \prime } \| \leq \frac { L ^ { 2 } } { M } , } \\ & { \| f ^ { \prime \prime \prime } \| \leq \frac { L ^ { 3 } } { M ^ { 2 } } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad  \end{array}
$$

This will mean that for any tree of order $p + 1$ , $\| F ( t ) ( y _ { 0 } ) \| \le L ^ { p } M$ and that

$$
\sum _ { \substack { \cdot ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| \leq \sum _ { \substack { r ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot L ^ { p } M .
$$

In studying the behaviour of a particular method of order $p$ when used to solve a particular initial value problem, we wish to assume that the local truncation error is bounded asymptotically by some constant multiplied by $h ^ { p + 1 }$ . This assumption will hinge on smoothness of the solution and the differentiability, sufficiently many times, of $f$ .

# 319 Global truncation error

We consider the cumulative effect of errors in many steps leading to an error in a final output point. Suppose that $n$ steps are performed to carry the solution from an initial point $x _ { 0 }$ to a final point $\scriptstyle { \overline { { x } } }$ . If a constant stepsize is used, this would need to be equal to $( { \overline { { x } } } - x _ { 0 } ) / n$ to exactly reach the final point. Denote the approximations computed by a Runge–Kutta method by $y _ { 1 }$ , $y _ { 2 }$ , $\cdot \cdot \cdot$ , $y _ { n }$ , with $y _ { 0 } = y ( x _ { 0 } )$ . If the error committed in each of the $n$ steps is bounded by $C h ^ { p + 1 }$ then the total contribution to the error would seem to be

$$
n C h ^ { p + 1 } = C ( \overline { { x } } - x _ { 0 } ) h ^ { p } .
$$

We attempt to make this argument more precise by noting that an error in the initial value input to a step will lead to an error in the output value consisting of two terms. The first of these is the perturbation to the output due to the error in the input, and the second is the truncation error due to the method itself.

In the statement of a preliminary lemma that we need, $| A |$ and $\left| b ^ { \dagger } \right|$ will denote the matrix $A$ and the vector $b ^ { \intercal }$ , respectively, with every term replaced by its magnitude.

![](images/7069dad99fe8cba6df92d3df7742e7e316a06d11c2a6f005b98913010ef5fb82.jpg)  
Growth of global errors from local errors referred to the computed solution

Lemma 319A Let $f$ denote a function $\mathbb { R } ^ { m } \to \mathbb { R } ^ { m }$ , assumed to satisfy a Lipschitz condition with constant $L$ . Let $y _ { 0 } \in \mathbb { R } ^ { m }$ and $z _ { 0 } \in \mathbb { R } ^ { m }$ be two input values to a step with the Runge–Kutta method $( A , b ^ { \intercal } , c )$ , using stepsize $h \leq h _ { 0 }$ , where $h _ { 0 } L \rho ( | A | ) < 1$ , and let $y _ { 1 }$ and $z _ { 1 }$ be the corresponding output values. Then

$$
\begin{array} { r } { \| y _ { 1 } - z _ { 1 } \| \leq ( 1 + h L ^ { \star } ) \| y _ { 0 } - z _ { 0 } \| , } \end{array}
$$

where

$$
L ^ { \star } = { L } | b ^ { \mathsf { T } } | ( I - h _ { 0 } L | A | ) ^ { - 1 } \mathbf { 1 } .
$$

Proof. Denote the stage values by $Y _ { i }$ and $Z _ { i }$ , $i = 1 , 2 , \dots , s$ , respectively. From the equation $\begin{array} { r } { Y _ { i } - Z _ { i } = ( y _ { 0 } - z _ { 0 } ) + h \sum _ { j = 1 } ^ { s } a _ { i j } ( f ( Y _ { j } ) - f ( Z _ { j } ) ) } \end{array}$ , we deduce that

$$
\| Y _ { i } - Z _ { i } \| \leq \| y _ { 0 } - z _ { 0 } \| + h _ { 0 } L \sum _ { j = 1 } ^ { s } | a _ { i j } | \| Y _ { j } - Z _ { j } \| ,
$$

so that, substituting into

$$
\| y _ { 1 } - z _ { 1 } \| \leq \| y _ { 0 } - z _ { 0 } \| + h L \sum _ { j = 1 } ^ { s } | b _ { j } | \| Y _ { j } - Z _ { j } \| ,
$$

we obtain the result.

![](images/26e12816636dcf5118b0aa79a0107d61337f85fe29f11b6c2cebf01bc1842577.jpg)  
Growth of global errors from local errors referred to the exact solution

To see how to use this result, consider Figures 319(i) and 319(ii). Each of these shows the development of global errors generated by local truncation errors in individual steps. In Figure 319(i), the local truncation errors are referred to the computed solution. That is, in this figure, $\delta _ { k }$ is the difference between the exact solution defined by an initial value at the start of step $k$ and the numerical solution computed in this step. Furthermore, $\Delta _ { k }$ is the contribution to the global error resulting from the error $\delta _ { k }$ in step $k$ . An alternative view of the growth of errors is seen from Figure 319(ii), where $\delta _ { k }$ is now the difference between the exact solution at $x _ { k }$ and the computed solution found by using an input value $y _ { k - 1 }$ at the start of this step exactly equal to $y ( x _ { k - 1 } )$ . As in the previous figure, $\Delta _ { k }$ is the contribution to the global error resulting from the local error $\delta _ { k }$ . To obtain a bound on the global truncation error we first need an estimate on $\delta _ { 1 }$ , $\delta _ { 2 } , \ldots , \delta _ { n }$ using these bounds. We then estimate by how much $\delta _ { k }$ can grow to $\Delta _ { k }$ , $k = 1 , 2 , \ldots , n$ . The global error is then bounded in norm by $\scriptstyle \sum _ { k = 1 } ^ { \pi } \Delta _ { k }$ . We have a bound already from (110c) on how much a perturbation in the exact solution can grow. If we were basing our global error bound on Figure $3 1 9 ( \mathrm { i } )$ then this would be exactly what we need. However, we use Figure 319(ii), and in this case we obtain the same growth factor but with $L$ replaced by $L ^ { \star }$ . The advantage of using an argument based on this figure, rather than on Figure 319(i), is that we can then use local truncation error defined in the standard way, by comparing the exact solution at step value $x _ { n }$ with the numerically computed result over a single step with initial value $y ( x _ { n - 1 } )$ .

Theorem 319B Let $h _ { 0 }$ and $L ^ { \star }$ be such that the local truncation error at step $k = 1 , 2 , \ldots , n$ is bounded by

$$
\delta _ { k } \leq C h ^ { p + 1 } , \qquad h \leq h _ { 0 } .
$$

Then the global truncation error is bounded by

$$
\| y ( x _ { n } ) - y _ { n } \| \leq \left\{ \begin{array} { l l } { \frac { \exp ( L ^ { \star } ( \overline { { x } } - x _ { 0 } ) ) - 1 } { L ^ { \star } } C h ^ { p } , } & { L ^ { \star } > 0 , } \\ { ( \overline { { x } } - x _ { 0 } ) C h ^ { p } , } & { L ^ { \star } = 0 . } \end{array} \right.
$$

Proof. Use Figure 319(ii) and obtain the estimate

$$
\| y ( x _ { n } ) - y _ { n } \| \leq C h ^ { p + 1 } \sum _ { k = 1 } ^ { n } ( 1 + h L ^ { \star } ) ^ { k } .
$$

The case $L ^ { \star } = 0$ is obvious. For the case $L ^ { \star } > 0$ , calculate the sum and use the bound

$$
( 1 + h L ^ { \star } ) ^ { n } \leq \exp ( L ^ { \star } h n ) = \exp ( L ^ { \star } ( \overline { { x } } - x _ { 0 } ) ) .
$$

# Exercises 31

31.1 Define $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ by

$$
f ( y ^ { 1 } , y ^ { 2 } , y ^ { 3 } ) = \left[ \begin{array} { c } { { y ^ { 1 } + y ^ { 2 } y ^ { 3 } } } \\ { { ( y ^ { 1 } ) ^ { 2 } + 2 y ^ { 1 } y ^ { 2 } } } \\ { { 1 + ( y ^ { 2 } + y ^ { 3 } ) ^ { 2 } } } \end{array} \right] .
$$

Find formulae for the elementary differentials $F ( t )$ , for $t = [ \tau ]$ , $\left[ \tau ^ { 2 } \right]$ and $[ \tau [ \tau ] ]$ .

31.2 For the Runge–Kutta method

$$
\frac { 1 } { 3 } \neq \frac { \frac { 5 } { 1 2 } } { 4 } \frac { \frac { 1 } { 4 } } { 4 }
$$

find the elementary weights for the eight trees up to order 4. What is the order of this method?

31.3 For an arbitrary Runge–Kutta method, find the order condition corresponding to the tree

# 32 Low Order Explicit Methods

# 320 Methods of orders less than 4

It will be shown in Subsection 324 that, for an explicit method to have order $p$ , at least $s = p$ stages are necessary. We derive methods up to $p = 3$ , with exactly $p$ stages, and then discuss briefly the advantages of using $s = p + 1$ .

For $s = p = 1$ there is no choice beyond the Euler method with tableau

![](images/9618c77e2502a58024623115b20e87f83cfa797f034b711167351b780177be93.jpg)

For $s = p = 2$ , we have a one-parameter family of methods of the form

$$
\frac { 0 } { \frac { c _ { 2 } } { 1 - \frac { 1 } { 2 c _ { 2 } } ~ \frac { 1 } { 2 c _ { 2 } } } }
$$

which satisfies the conditions $b _ { 1 } + b _ { 2 } = 1$ and $\begin{array} { r } { b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , corresponding to the trees and .

For $s = p = 3$ , we must satisfy four conditions, which are shown together with the corresponding trees as follows:

$$
\begin{array} { c c c } { \cdot } & { b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 , } \\ { \vdots } & { } & { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \displaystyle { \frac { 1 } { 2 } } , } \\ { \big \nvee } & { } & { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \displaystyle { \frac { 1 } { 3 } } , } \\ { \vdots } & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } = \displaystyle { \frac { 1 } { 6 } } . } \end{array}
$$

To solve these equations in the most straightforward manner, it is convenient to treat $c _ { 2 }$ and $c _ { 3 }$ as free parameters and to carry out three steps. First, solve for $b _ { 2 }$ and $b _ { 3 }$ from the linear system given by (320b) and (320c). Secondly, evaluate $b _ { 1 }$ from (320a). Finally, solve for $a _ { 3 2 }$ from (320d). This plan will run into difficulties if the matrix of coefficients in (320b) and (320c) is singular; that is, if $c _ { 2 } c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = 0$ . Assuming this does not occur, we have a further difficulty if the solution to (320b) and (320c) results in $b _ { 3 } = 0$ . This anomaly, which occurs if $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , makes it impossible to solve (320d). A more careful analysis is necessary to resolve these difficulties, and it is possible to identify three cases where a solution can be found. These are

$$
\begin{array} { l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \neq 0 \neq c _ { 3 } \neq c _ { 2 } \neq \frac { 2 } { 3 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { c _ { 2 } = c _ { 3 } = \frac { 2 } { 3 } , b _ { 3 } \neq 0 , } } \\ { { \mathrm { ~ I I I ~ } } } & { { c _ { 2 } = \frac { 2 } { 3 } , c _ { 3 } = 0 , b _ { 3 } \neq 0 . } } \end{array}
$$

The coefficient tableaux for the three cases are summarized as follows, with the general form of the tableau given in each case: for case I we have

for case II,

$$
{ \frac { \displaystyle { \frac { 2 } { 3 } } } { \displaystyle { \frac { 2 } { 3 } } - { \frac { 1 } { 4 b _ { 3 } } } } } { \frac { \frac { 2 } { 3 } } { \frac { 2 } { 4 } } } { \frac { \frac { 2 } { 3 } } { \frac { 1 } { 4 } - b _ { 3 } } } { \frac { \frac { 1 } { 6 } } { b _ { 3 } } }  ; 
$$

and for case III,

# 321 Simplifying assumptions

As the order being sought increases, the number of conditions rises rapidly and soon becomes unmanageable. For this reason, it is necessary to examine the relationships between the conditions corresponding to various trees. At the same time, we identify certain collections of order conditions which have some sort of central role. Since these special conditions will be of varying complexity, depending on the orders to which we apply them, they will be parameterized by one or more positive integers. For example, $E ( \eta , \zeta )$ is a set of assumptions about a method that hold for all positive integers $k \leq \eta$ and $l \leq \zeta$ .

that the cond The first of these conditions will be denoted by ions $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = k ^ { - 1 }$ old for $k = 1 , 2 , \ldots , \eta$ $B ( \eta )$ , and simply states . For a method $p$ $B ( p )$   
restates the order condition for the trees

Order conditions corresponding to some pairs of related trees   

<table><tr><td>t1</td><td>1 Φ(t1)= (t1）</td><td>t2</td><td>（t2）=27（t2)</td><td>1</td></tr><tr><td>：</td><td></td><td>?</td><td></td><td></td></tr><tr><td></td><td>∑baijC=</td><td></td><td>∑bic²=</td><td></td></tr><tr><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1∑bic=</td><td></td></tr><tr><td></td><td>∑biciaijCj=</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑bxakiaijCj =24</td><td></td><td>1∑bkakic²=4</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>丫</td><td></td><td></td></tr><tr><td>:iv:iI!</td><td></td><td></td><td></td><td></td></tr></table>

To motivate condition $C ( \eta )$ , consider pairs of trees $t _ { 1 }$ and $t _ { 2 }$ , with the same order, that differ in only one small respect. Suppose they are labelled with identical vertex sets and that the edge sets, say $E _ { 1 }$ and $E _ { 2 }$ , respectively, differ only in that $E _ { 1 }$ contains the edges $[ i , j ]$ and $[ j , k ]$ , and that $j$ and $k$ do not occur in any of the other ordered pairs in $E _ { 1 }$ , whereas $E _ { 2 }$ contains the edge $[ i , k ]$ instead of $[ j , k ]$ . This will mean that the elementary weight corresponding to $t _ { 1 }$ will have a factor $a _ { i j } c _ { j }$ , whereas $t _ { 2 }$ will have a corresponding factor $c _ { i } ^ { 2 }$ . Furthermore, the densities are also closely related in that $\gamma ( t _ { 1 } ) ~ = ~ 2 \gamma ( t _ { 2 } )$ . Hence, the equations

$$
\Phi ( t _ { 1 } ) = { \frac { 1 } { \gamma ( t _ { 1 } ) } } \qquad { \mathrm { a n d } } \qquad \Phi ( t _ { 2 } ) = { \frac { 1 } { \gamma ( t _ { 2 } ) } }
$$

will be equivalent if

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } = { \frac { 1 } { 2 } } c _ { i } ^ { 2 } , { \mathrm { ~ f o r ~ a l l ~ } } i = 1 , 2 , \ldots , s .
$$

We illustrate this by looking at some pairs of trees and noting the form of the equations

$$
\Phi ( t _ { 1 } ) = { \frac { 1 } { \gamma ( t _ { 1 } ) } } \mathrm { a n d } \frac { 1 } { 2 } \Phi ( t _ { 2 } ) = { \frac { 1 } { 2 \gamma ( t _ { 2 } ) } } .
$$

These are displayed in Table 321(I).

It is clear that, if it were possible for (321a) to hold for all $i \in \{ 1 , 2 , \ldots , s \}$ , then we could simply remove the order equations associated with the $t _ { 1 }$ trees from consideration, because they will automatically be satisfied if the conditions $\Phi ( t ) = 1 / \gamma ( t )$ are satisfied for the $t _ { 2 }$ trees. However, it is not possible in the case $i \ = \ 2$ because this gives the equation $\textstyle { \frac { 1 } { 2 } } c _ { 2 } ^ { 2 } \ = \ 0$ which implies $c _ { 2 } = 0$ . It will then follow in turn that $c _ { 3 } = 0$ , $c _ { 4 } = 0$ , . . . and all $c$ components equal to zero will not be consistent even with the order condition $\textstyle \sum b _ { i } c _ { i } \ = \ { \frac { 1 } { 2 } }$ . While we cannot make use of the simplification of assuming (321a) in the case of explicit methods, we make extensive use of this and closely related conditions in the case of implicit methods. Furthermore, we can still use this sort of simplification applied to just some of the stages.

![](images/fb84986ce75b33490495146aad335c44a6458ed7536f47415bf8920a02f3dc08.jpg)  
The $C ( k )$ condition relating $\textstyle \sum _ { j } a _ { i j } c _ { j } ^ { k - 1 }$ (left-hand tree) to $c _ { i } ^ { k }$ (right-hand tree). The underlying tree is a pohutukawa (Metrosideros excelsa), also known as the ‘New Zealand Christmas tree’ because its bright red flowers bloom at Christmas-time.

In addition to (321a), we can consider the possibility that conditions like

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \quad i = 1 , 2 , \ldots , s ,
$$

hold for $k = 1 , 2 , \ldots .$ Assuming that these hold for $1 \leq k \leq \xi$ , we denote this collection of conditions by $C ( \xi )$ . The consequences of $C ( \xi )$ are that, for any pair of trees $t _ { 1 }$ and $t _ { 2 }$ for which $\Phi ( t _ { 1 } )$ contains a factor $a _ { i j } c _ { j } ^ { k - 1 }$ , $\Phi ( t _ { 2 } )$ contains a factor $\scriptstyle { \frac { 1 } { k } } c _ { i } ^ { k }$ and the remaining factors are identical in the two expressions, then $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ implies $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ . We illustrate this in Figure 321(i).

The $D ( k )$ conditions interrelate three trees $t _ { 1 }$ , $t _ { 2 }$ and $t _ { 3 }$ for which the corresponding elementary weights differ only in that $\Phi ( t _ { 1 } )$ has a factor $b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ , $\Phi ( t _ { 2 } )$ has a factor $b _ { j }$ and $\Phi ( t _ { 3 } )$ has a factor $b _ { j } c _ { j } ^ { k }$ . This means that these trees have forms like those shown in Figure 321(ii).

We illustrate this further, for the case $k = 1$ , in Table 321(II). Note that if $D ( 1 )$ holds, then the truth of $\Phi ( t _ { 1 } ) = 1 / \gamma ( t _ { 1 } )$ follows from $\Phi ( t _ { 2 } ) = 1 / \gamma ( t _ { 2 } )$ and $\Phi ( t _ { 3 } ) = 1 / \gamma ( t _ { 3 } )$ . For explicit methods, $D ( 2 )$ cannot hold, for similar reasons to the impossibility of $C ( 2 )$ . For implicit methods $D ( s )$ is possible, as we shall see in Section 342.

![](images/ff9c9de1b79338b1593c984ed36a7e9e8e2f72cce9e35ce52ef10fe65ea4fc75.jpg)  
Figure 321(ii) The $D ( k )$ condition relating $\sum _ { i } b _ { i } c _ { i } ^ { k - 1 } a _ { i j }$ (left-hand tree) to $b _ { j }$ (middle tree) and $b _ { j } c _ { j } ^ { k }$ (right-hand tree). The underlying tree is a kauri (Agathis australis). Although the immature tree shown is only a few metres tall, the most famous kauri tree, Tane Mahuta (Lord of the Forest), has a height of $4 0 \textrm { m }$ and a diameter, 1.5 m above ground level, of 5.21 m.

Sets of three related trees illustrating $D ( 1 )$   

<table><tr><td rowspan="3">t1</td><td rowspan="3">(t1)=</td><td>1</td><td rowspan="3">t2</td><td rowspan="3">Φ(t2) =</td><td>1</td><td rowspan="3">t3</td><td rowspan="3">（(t3)=</td><td>1</td></tr><tr><td>(t1)</td><td>(t2）</td><td>（t3)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijcj=</td><td></td><td></td><td>∑bcj=</td><td></td><td>Y</td><td>∑bj²=</td><td></td></tr><tr><td></td><td></td><td></td><td>：</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>？</td><td></td><td></td><td>V</td><td></td><td></td></tr><tr><td></td><td>∑biaijc²=12</td><td></td><td></td><td>∑b=</td><td></td><td></td><td>∑bjc=1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>∑biaijajkck =</td><td></td><td></td><td></td><td></td><td>∑bjCjajkCk=</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>∑bjajkck=</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Finally, the condition $E ( \eta , \zeta )$ states that

$$
\sum b _ { i } c _ { i } ^ { k - 1 } a _ { i j } c _ { j } ^ { l - 1 } = \frac { 1 } { l ( k + l ) } , \qquad k = 1 , 2 , \ldots , \eta , \quad l = 1 , 2 , \ldots , \zeta .
$$

This simply expresses the fact that the order condition $\Phi ( t ) = 1 / \gamma ( t )$ is satisfied for trees $t = [ \tau ^ { k - 1 } [ \tau ^ { l - 1 } ] ]$ for $k \leq \eta$ and $l \leq \zeta$ . This is a necessary condition for orders at least $\eta + \zeta$ .

# 322 Methods of order 4

It is an interesting consequence of the fourth order conditions for a method with $s \ = \ 4$ stages, that $c _ { 4 } ~ = ~ 1$ and that $D ( 1 )$ holds. This fact reduces significantly the number of conditions that remain to be solved; furthermore, it is possible to segment the derivation into two phases: the solution of the remaining order conditions and the evaluation of the elements in the final row of $A$ to ensure that $D ( 1 )$ is actually satisfied. Assuming that the method

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { c _ { 4 } } \\ { b _ { 1 } } \end{array} \right| a _ { 2 1 } \qquad \eqno { 3 } 2 } \end{array}
$$

satisfies the fourth order conditions, then we can compute the values of

$$
\begin{array} { r l } & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 2 } ) c _ { i } = \frac { 1 } { 4 } - \frac { c _ { 2 } + c _ { 4 } } { 3 } + \frac { c _ { 2 } c _ { 4 } } { 2 } , } \\ & { b _ { 4 } a _ { 4 3 } ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } a _ { i j } ( c _ { j } - c _ { 2 } ) c _ { j } \qquad = \frac { 1 } { 1 2 } - \frac { c _ { 2 } } { 6 } , } \\ & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) a _ { i j } c _ { j } \qquad = \frac { 1 } { 8 } - \frac { c _ { 4 } } { 6 } , } \\ & { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } a _ { i j } a _ { j k } c _ { k } \qquad = \frac { 1 } { 2 4 } . } \end{array}
$$

In each of these calculations, the first column is the only non-zero term in the middle column, while the final column is found by expanding the middle column into a linear combination of elementary weights and equating each of these to the right-hand sides of the corresponding order conditions. For example, (322a) is evaluated from the trees $\blacktriangledown$ , $\blacktriangledown$ and $\natural$ and uses the combination of order conditions

$$
\Phi ( { \pmb { \Psi } } ) - ( c _ { 2 } + c _ { 4 } ) \Phi ( { \pmb { \Psi } } ) + c _ { 2 } c _ { 4 } \Phi ( { \pmb { \updownarrow } } ) = \frac { 1 } { \gamma ( { \pmb { \Psi } } ) } - \frac { c _ { 2 } + c _ { 4 } } { \gamma ( { \pmb { \ Y } } ) } + \frac { c _ { 2 } c _ { 4 } } { \gamma ( { \pmb { \updownarrow } } ) } .
$$

From the first columns of (322a)–(322d), we observe that $\mathrm { { ( 3 2 2 a ) } } \times \mathrm { { ( 3 2 2 d ) } } =$ (322b) $\times$ (322c) so that, from the last columns, we find

$$
\left( { \frac { 1 } { 4 } } - { \frac { c _ { 2 } + c _ { 4 } } { 3 } } + { \frac { c _ { 2 } c _ { 4 } } { 2 } } \right) \left( { \frac { 1 } { 2 4 } } \right) - \left( { \frac { 1 } { 1 2 } } - { \frac { c _ { 2 } } { 6 } } \right) \left( { \frac { 1 } { 8 } } - { \frac { c _ { 4 } } { 6 } } \right) = 0 .
$$

This relation simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$ which, because $c _ { 2 } = 0$ is incompatible with (322d), implies $c _ { 4 } = 1$ .

An alternative proof of this result, is found by using the following:

Lemma 322A If $P$ and $Q$ are each $3 \times 3$ matrices such that their product has the form

$$
P Q = \left[ \begin{array} { c c c } { r _ { 1 1 } } & { r _ { 1 2 } } & { 0 } \\ { r _ { 2 1 } } & { r _ { 2 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

where

$$
\operatorname* { d e t } \left( { \left[ \begin{array} { l l } { r _ { 1 1 } } & { r _ { 1 2 } } \\ { r _ { 2 1 } } & { r _ { 2 2 } } \end{array} \right] } \right) \neq 0 ,
$$

then either the last row of $P$ is zero or the last column of $Q$ is zero.

Proof. Because $P Q$ is singular, either $P$ is singular or $Q$ is singular. In the first case, let $u ^ { \prime } \ne 0$ be such that $u ^ { \prime } P = 0$ , and therefore $u ^ { \intercal } P Q = 0$ ; in the second case, let $v \neq 0$ be such that $Q v = 0$ , and therefore $P Q v = 0$ . Because of the form of $P Q$ , this implies that the first two components of $u ^ { \intercal }$ (or, respectively, the first two components of $v$ ) are zero. $\boxed { \begin{array} { r l } \end{array} }$

To obtain the result that $D ( 1 )$ necessarily holds if $s = p = 4$ , we apply Lemma 322A with

$$
\begin{array}{c} \mathbf { \Phi } ^ { \mathcal { P } } = \left[ \begin{array} { c c c } { b _ { 2 } } & { b _ { 3 } } & { b _ { 4 } } \\ { b _ { 2 } c _ { 2 } } & { b _ { 3 } c _ { 3 } } & { b _ { 4 } c _ { 4 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { i = 1 } & { i } & { i = 1 } \end{array} \right] \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 3 } - b _ { 3 } ( 1 - c _ { 3 } ) \quad \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } )  \end{array}
$$

and

$$
\begin{array} { r } { Q = \left[ \begin{array} { c c c c c } { c _ { 2 } } & { c _ { 2 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } } \\ { c _ { 3 } } & { c _ { 3 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 3 j } c _ { j } - \frac { 1 } { 2 } c _ { 3 } ^ { 2 } } \\ { c _ { 4 } } & { c _ { 4 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 4 j } c _ { j } - \frac { 1 } { 2 } c _ { 4 } ^ { 2 } } \end{array} \right] . } \end{array}
$$

The value of the matrix $P Q$ can be calculated from the order conditions. For example, the $( 2 , 2 )$ element is equal to

$$
\left[ b _ { 2 } c _ { 2 } b _ { 3 } c _ { 3 } b _ { 4 } c _ { 4 } \right] \left[ c _ { 2 } ^ { 2 } c _ { 3 } ^ { 2 } c _ { 4 } ^ { 2 } \right] ^ { \intercal } = \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 3 } = { \frac { 1 } { 4 } } .
$$

The elements in the last row and last column are a little more complicated to evaluate because they depend on linear combinations of elementary weights, but the relation of these elements in the product to the $C ( 2 )$ and $D ( 1 )$ conditions simplifies each of these elements to a zero value. In summary, the product of $P$ and $Q$ is

$$
P Q = \left[ \begin{array} { l l l } { \frac 1 2 } & { \frac 1 3 } & { 0 } \\ { \frac 1 3 } & { \frac 1 4 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

so that the conditions of Lemma 322A are satisfied. The conclusion is that the last roeither $P$ of  or $Q$ r, this means that. These simplify to $\begin{array} { r } { \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } ) = 0 } \end{array}$ $\begin{array} { r } { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ $b _ { 4 } ( 1 - c _ { 4 } ) = 0$ or to $\begin{array} { r } { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ , respectively. It is impossible that $c _ { 2 } = 0$ or that $b _ { 4 } = 1$ , and hence $c _ { 4 } = 1$ and the $D ( 1 )$ condition holds.

Since $D ( 1 )$ holds, the set of additional equations we need to satisfy reduce to those associated with the trees , , $\curlyvee$ and $\blacktriangledown$ as well as with the $\operatorname { t r e e } \sqrt { \frac { \pi } { 2 } }$ . The order condition associated with the last of these is $\begin{array} { r } { \sum b _ { i } c _ { i } a _ { i j } c _ { j } = \frac { 1 } { 8 } } \end{array}$ . It turns out to be more convenient to use, instead of this condition, the difference between this and with the condition associated with $\nmid$ , that is, $\begin{array} { r } { \sum b _ { i } a _ { i j } c _ { j } = \frac { 1 } { 6 } } \end{array}$ , which is a consequence of other assumptions and of the $D ( 1 )$ condition. Hence we assume $\begin{array} { r } { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } = \frac { 1 } { 2 4 } } \end{array}$ .

The steps we need to carry out to derive one of these methods are as follows:

(a) Choose $c _ { 2 }$ and $c _ { 3 }$ , noting that $c _ { 1 } = 0$ and $c _ { 4 } = 1$ . (b) Choose $b _ { 1 }$ , $b _ { 2 }$ , $b _ { 3 }$ , $b _ { 4 }$ to satisfy $\sum b _ { i } c _ { i } ^ { k - 1 } = 1 / k$ for $k = 1 , 2 , 3 , 4$ . (c) Choose $a _ { 3 2 }$ so that $\begin{array} { r } { b _ { 3 } ( 1 - c _ { 3 } ) a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } } \end{array}$ . (d) Choose $a _ { 4 1 }$ , $a _ { 4 2 }$ , $a _ { 4 3 }$ , so that $\begin{array} { r } { \sum _ { i } b _ { i } a _ { i j } = b _ { j } \bigl ( 1 - c _ { j } \bigr ) } \end{array}$ for $j = 1 , 2 , 3$

Carrying out this programme might present some difficulties. For example, if in step (a) the $c _ { i }$ are not distinct, then there might not exist a solution in step (b). It might also happen that the value of $b _ { 4 }$ , found in step (b), is zero, and this will make it impossible to carry out either step (c) or step (d). Even if a solution exists for the sub-problem that arises in each step, the solution might not be unique, and there could turn out to be a family of solutions. The general solution, which is valid except in these exceptional cases, is given by the following coefficients:

$$
\begin{array} { r l } & { a _ { 2 1 } = c _ { 2 1 } , } \\ & { a _ { 3 1 } = \frac { c _ { 3 } \left( c _ { 3 } + 4 c _ { 2 } ^ { 2 } - 3 c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 3 2 } = - \frac { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 4 1 } = \frac { - 1 2 c _ { 3 } c _ { 2 } ^ { 2 } + 1 2 c _ { 3 } ^ { 2 } c _ { 2 } ^ { 2 } + 4 c _ { 2 } ^ { 2 } - 6 c _ { 2 } + 1 5 c _ { 2 } c _ { 3 } - 1 2 c _ { 3 } ^ { 2 } c _ { 2 } + 2 + 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } } { 2 c _ { 2 } c _ { 3 } \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 2 } = \frac { \left( c _ { 2 } - 1 \right) \left( 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } + 2 - c _ { 2 } \right) } { 2 c _ { 2 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 3 } = - \frac { \left( 2 c _ { 2 } - 1 \right) \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - 1 \right) \left( c _ { 3 } - 1 \right) } { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \end{array}
$$

$$
\begin{array} { l } { b _ { 1 } = \cfrac { 6 c _ { 3 } c _ { 2 } - 2 c _ { 3 } - 2 c _ { 2 } + 1 } { 1 2 c _ { 3 } c _ { 2 } } , } \\ { b _ { 2 } = - \cfrac { \left( 2 c _ { 3 } - 1 \right) } { 1 2 c _ { 2 } \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - c _ { 2 } \right) } , } \\ { b _ { 3 } = \cfrac { \left( 2 c _ { 2 } - 1 \right) } { 1 2 c _ { 3 } \left( c _ { 2 } - c _ { 3 } c _ { 2 } + c _ { 3 } ^ { 2 } - c _ { 3 } \right) } , } \\ { b _ { 4 } = \cfrac { - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } } { 1 2 \left( c _ { 3 } - 1 \right) \left( c _ { 2 } - 1 \right) } . } \end{array}
$$

Kutta identified five special cases where a solution is certain to exist:

$$
\begin{array} { l l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \notin \{ 0 , \frac { 1 } { 2 } , \frac { 1 } { 2 } \pm \frac { \sqrt { 3 } } { 6 } , 1 \} , } } & { { c _ { 3 } = 1 - c _ { 2 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { b _ { 2 } = 0 , } } & { { c _ { 2 } \neq 0 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ I I I ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = \frac { 1 } { 2 } , \quad c _ { 3 } = 0 , } } \\ { { \mathrm { ~ I V ~ } } } & { { b _ { 4 } \neq 0 , } } & { { c _ { 2 } = 1 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ V ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = c _ { 3 } = \frac { 1 } { 2 } . } } \end{array}
$$

The coefficient tableaux are for case I,

<table><tr><td>0</td><td colspan="3"></td></tr><tr><td>1-C3</td><td colspan="3">1-C3</td></tr><tr><td>C3</td><td>C3(1-2c3)</td><td>C3 2(1-c3）</td><td></td></tr><tr><td rowspan="2">1</td><td colspan="3">2(1-c3）</td></tr><tr><td>12c-24c+17c3-4</td><td>C3(1-2c3)</td><td>1-C3</td></tr><tr><td colspan="3"></td><td></td></tr><tr><td rowspan="2"></td><td>2(1-c3)(6c3-1-6c) 6c3-1-6c</td><td>2(1-c3）(6c3-1-6c2）</td><td>6cg-1-6c2</td></tr><tr><td>1 12c3(1-c3) 12c3(1-c3)</td><td>1 12c3(1-c3)</td><td>6cg-1-6c 12c3(1-c3)</td></tr></table>

for case II,

$$
{ \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { { \frac { 1 } { 2 } } } \\ { 1 } \\ { { \frac { 1 } { 2 c _ { 2 } } } - 1 \quad - { \frac { 1 } { 2 c _ { 2 } } } \quad { \mathrm { ~ 2 ~ } } } \\ { { \frac { 1 } { 6 } } } \end{array} } ;
$$

for case III,

for case IV,

$$
\begin{array} { r }   \begin{array} { c } { 0 } \\ { 1 } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} | _ { \begin{array} { c c c c c c } { \frac { 3 } { 8 } } & { \frac { 1 } { 8 } } & { } & { } & { } \\ { 1 - \frac { 1 } { 4 b _ { 4 } } } & { - \frac { 1 } { 1 2 b _ { 4 } } } & { \frac { 1 } { 3 b _ { 4 } } } & { } & { } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 6 } - b _ { 4 } } & { \frac { 2 } { 3 } } & { b _ { 4 } } \end{array} \} } \end{array}
$$

and for case V,

$$
\begin{array} { r l } & { \left. \begin{array} { c } { 0 } \\ { \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} \right| \frac { 1 } { 2 } - \frac { 1 } { 6 b _ { 3 } } \qquad \frac { 1 } { 6 b _ { 3 } } } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad 1 - 3 b _ { 3 } \quad 3 b _ { 3 } \quad \right. } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad \frac { 2 } { 3 } - b _ { 3 } \quad b _ { 3 } \quad \frac { 1 } { 6 } \qquad \right. } \end{array} .
$$

Some interesting special choices within these cases are $\begin{array} { r } { c _ { 3 } = \frac { 2 } { 3 } } \end{array}$

and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ in case II,

$$
\begin{array} { r } { { \frac { 1 } { 4 } } { \left| \begin{array} { l l l l } { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { { \frac { 1 } { 2 } } } \end{array} \right| } ~ 0 \quad { { \frac { 1 } { 2 } } } } \\ { { \frac { 1 } { 6 } } { \frac { 1 } { 6 } } { \frac { - 2 } { 0 } } { \frac { 2 } { 3 } } { \begin{array} { l } { { \frac { 1 } { 6 } } } \end{array} } . } \end{array}
$$

A further, and somewhat eccentric, special choice in case II, is $c _ { 2 } = - \frac { 1 } { 2 }$

<table><tr><td>0 中</td><td></td></tr><tr><td></td><td>1 1</td><td>2</td><td></td></tr><tr><td></td><td>#</td><td>2</td><td></td></tr><tr><td></td><td>1</td><td></td><td>1</td></tr></table>

The interest in this method, as for a similar method with $c _ { 2 } = - 1$ , is that it is possible to eliminate one stage of computation, by replacing $F _ { 2 }$ by a quantity found in the previous step. The method contrived in this way is no longer a Runge–Kutta method, and has poorer stability, but it is more efficient in terms of order achieved per stages computed.

We also present the choices $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 1 2 } } \end{array}$ in case III,

$$
\begin{array} { r } { { \left. \begin{array} { c } { { 0 } } \\ { { \frac { 1 } { 2 } } } \\ { { 0 } } \\ { { 1 } } \end{array} \right| } \quad \frac { 1 } { 2 } \quad { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { 1 } } \end{array} \right. } } \\ { { \left. \begin{array} { l l l l l l } { { \frac { 1 } { 1 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 1 2 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 1 2 } } } & { { \frac { 1 } { 6 } } } \end{array} \right. } } \end{array} \right. , } } \end{array}
$$

and $\begin{array} { r } { b _ { 4 } = \frac { 1 } { 6 } } \end{array}$ in case IV,

Amongst the methods in case V, the ‘classical Runge–Kutta method’ is especially notable. The tableau is

$$
\begin{array} { r } { \frac { 0 } { 2 } \left| \begin{array} { l l l l l } { ~ } & { ~ } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ 0 } & { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 0 } } & { 0 } & { 1 } & { ~ } & { ~ } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 6 } } & { . ~ } \end{array} \right. } \end{array}
$$

Also in case V is a special method derived by Gill (1951), for the special purpose of reducing memory requirements for large problems. Gill found that by using a value $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 3 } + \frac { \sqrt { 2 } } { 6 } } \end{array}$ , or the conjugate of this which was rejected as having larger errors, it was possible to solve an $N$ -dimensional system using only $3 N$ stored numbers. For a general method with $s = p = 4$ , the corresponding memory needs are $4 N$ . The tableau for Gill’s method is

$$
{ \begin{array} { c } { { \mathrm { ~ 0 ~ } } } \\ { { \frac { 1 } { 2 } } } \\ { { \mathrm { ~ 1 ~ } } } \\ { { \mathrm { ~ 1 ~ } } } \end{array} } { \frac { 1 } { 2 } } { \left| \begin{array} { l l l l l } { { \underline { { { \mathrm { ~ 1 ~ } } } } } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { \mathrm { ~ 2 ~ } } { 2 } } } & { { \underline { { { 2 \mathrm { - } } } } } { \sqrt { \underline { { { 2 } } } } } } & { { } } & { { } } \\ { { 0 } } & { { - { \frac { { \sqrt { 2 } } } { 2 } } } } & { { { \underline { { { 2 \mathrm { + } { \sqrt { 2 } } } } } } } } & { { } } \\ { { { \frac { 1 } { 6 } } } } & { { { \frac { { 2 \mathrm { - } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { { 2 \mathrm { + } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { 1 } { 6 } } } } \end{array} \right. }
$$

and is characterized by the condition

$$
\operatorname * { d e t } \left( { \left[ \begin{array} { l l l } { 1 } & { a _ { 3 1 } } & { a _ { 3 2 } } \\ { 1 } & { a _ { 4 1 } } & { a _ { 4 2 } } \\ { 1 } & { b _ { 1 } } & { b _ { 2 } } \end{array} \right] } \right) = 0
$$

which, for a method in case V, imposes the constraint

$$
1 8 b _ { 3 } ^ { 2 } - 1 2 b _ { 3 } + 1 = 0 ,
$$

with solutions

$$
b _ { 3 } = { \frac { 2 \pm { \sqrt { 2 } } } { 6 } } .
$$

# 323 New methods from old

As we seek explicit Runge–Kutta methods of higher and higher order, we observe relationships between methods of two adjacent orders. For example, fourth order methods are connected in a special way with certain methods with only three stages, but with a modified type of third order condition. Denote the fourth order method by

$$
\begin{array} { r } { \frac { c } { \left| \begin{array} { l } { A } \\ { A } \\ { b ^ { \intercal } } \end{array} \right| } = \begin{array} { l } { c _ { 2 } } \\ { c _ { 3 } } \\ { 1 } \end{array} \left| \begin{array} { l l l l } { a _ { 2 1 } } & & & \\ { a _ { 3 1 } } & { a _ { 3 2 } } & & \\ { a _ { 4 1 } } & { a _ { 4 2 } } & { a _ { 4 3 } } & \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { b _ { 4 } } \end{array} \right| } \end{array}
$$

and consider the three-stage tableau

$$
\frac  \stackrel { \displaystyle \widetilde { c } } { \longrightarrow } \bigg | \stackrel { \widetilde { A } } { \widetilde { b } ^ { \top } } = \begin{array} { l } { 0 } \\ { c _ { 2 } } \\ { \frac { c _ { 3 } } { b _ { 1 } } \bigg | \stackrel { a _ { 2 1 } } { b _ { 2 } } \big ( 1 - c _ { 2 } \big ) \quad b _ { 3 } \big ( 1 - c _ { 3 } \big ) } \end{array} .
$$

If we denote the elementary weights for the new method (323b) by $\widetilde { \Phi }$ , we find for the trees with order up to 3,

$$
\begin{array} { l } { \displaystyle \widetilde { \Phi } ( \bullet ) = \frac 1 2 = \frac 1 { \left( r ( \bullet ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } ( \bullet ) = \frac 1 6 = \frac 1 { \left( r ( \bullet ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } ( \bullet \bullet ) = \frac 1 { 1 2 } = \frac 1 { \left( r ( \bullet \vee ) + 1 \right) \gamma ( \bullet ) } , } \\ { \displaystyle \widetilde { \Phi } \left( \ddag \right) = \frac 1 { 2 4 } = \frac 1 { \left( r \left( \bullet \right) + 1 \right) \gamma \left( \bullet \right) } . } \end{array}
$$

The conclusion that $\widetilde { \Phi } ( t ) = 1 / \big ( ( r ( t ) + 1 ) \gamma ( t ) \big )$ is not in the least remarkable. In fact, such a conclusion will always hold if $ { \tilde { b } } ^ { \intercal } = b ^ { \intercal } A$ , with obvious working in the opposi adjustments made to $c$ and   direction, from order 3 to order 4. If to form and $\widetilde { A }$ , but our interest here is in $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } = 1$ is satisfied for the four-stage method (323a), then the remainder of the order conditions are satisfied as a consequence of (323c)–(323f) and of the $D ( 1 )$ assumption. We check these as follows, where the relevant trees are also shown:

$$
\begin{array} { r l } & { \cdot \frac { \sum \hat { b } _ { i } } { 2 } b _ { i } = 1 , } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } = \frac { 3 } { \sqrt { 2 } } b _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) e _ { i } ^ { 4 } = \frac { 1 } { 2 } - \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } } \\ { 1 } & { \qquad \quad \le - \frac { 1 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 1 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } } \\ { 1 } & { \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } - \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } ( 1 - e _ { i } ) e _ { i } ^ { 2 } = \frac { 1 } { 5 } - \frac { 3 } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } = \frac { 1 } { 4 } , } \\ { 1 } &  \qquad \frac { \sum \hat { b } _ { i } } { \sqrt { 2 } } b _ { i } e _ { i } ^ { 2 } e _ { i } ^ { 2 }  \end{array}
$$

It is not possible to extend the principle illustrated in this result to higher orders without making some additional assumptions. We introduce the idea we need as follows:

Definition 323A Consider a Runge–Kutta method given by the tableau

$$
\frac { c \dag A } { \ d b ^ { \intercal } } _ { \mathbf { \Pi } . }
$$

For a tree t and stage $i$ , let $\Phi _ { i } ( t )$ denote the elementary weight associated with t for the tableau

$$
\frac { c \left| \begin{array} { l } { \boldsymbol { A } } \\ { e _ { i } ^ { \top } \boldsymbol { A } } \end{array} \right| } { \left| \begin{array} { l } { e _ { i } ^ { \top } \boldsymbol { A } } \end{array} \right| } .
$$

Stage i has ‘internal order $q$ ’, if for all trees such that $r ( t ) \leq q$

$$
\Phi _ { i } ( t ) = \frac { c _ { i } ^ { r ( t ) } } { \gamma ( t ) } .
$$

The significance of this definition is that if stage $i$ has internal order $q$ , then, in any step with initial value $y _ { n - 1 } = y ( x _ { n - 1 } )$ , the value computed in stage $i$ satisfies $Y _ { i } = y ( x _ { n - 1 } + h c _ { i } ) + O ( h ^ { q + 1 } )$ . Note that the $C ( q )$ condition is

necessary and sufficient for every stage to have internal order $q$ , and this is possible only for implicit methods.

We are now in a position to generalize the remarks we have made about third and fourth order methods.

Theorem 323B Let

$$
\frac { \boldsymbol { \widetilde { c } } \mathbin { \vrule h \vrule h \vrule h \vrule h 0 . 6 1 \widetilde { \boldsymbol { A } } } } { \textup { \vrule h } ^ { \boldsymbol { \widetilde { b } } \intercal } }
$$

denote a Runge–Kutta method with $s - 1$ stages and generalized order $p - 1$ , satisfying $\widetilde { c } _ { s - 1 } \neq 1$ . Let $q$ be an integer such that $2 q + 2 \geq p$ and suppose that for any $i \in S \subset \{ 1 , 2 , \dotsc , s - 1 \}$ , the method has internal order $q$ . If there exists $b \in \mathbb { R } ^ { s }$ , with $b _ { s } \neq 0$ such that

$$
\sum _ { i = 1 } ^ { s } b _ { i } = 1 ,
$$

and such that $b _ { i } \neq 0$ implies $i \in S$ , $c _ { i } \neq 1$ and $b _ { i } ( 1 - c _ { i } ) = \widetilde { b } _ { i }$ , then the s-stage method

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

has order $p$ , where $\boldsymbol { c } ^ { \intercal } = \left[ \begin{array} { l l } { \widetilde { \boldsymbol { c } } ^ { \intercal } } & { 1 } \end{array} \right]$ and the $s \times s$ matrix $A$ is formed from $\widetilde { A }$ by adding an additional row with component $j \in \{ 1 , 2 , \ldots , s - 1 \}$ equal to $\begin{array} { r } { \left( \tilde { b } _ { j } - \sum _ { i = 1 } ^ { s - 1 } b _ { i } a _ { i j } \right) / { b _ { s } } } \end{array}$ and then adding an additional column of s zeros.

Proof. The case $p = 1$ follows from (323g), so we consider instead the case $p \geq 2$ . Also, without loss of generality we assume that $1 \leq q \leq p - 1$ , because internal order $^ { 1 }$ is equivalent to $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } } \end{array}$ and because $q \geq p$ implies internal order $p - 1$ . We first prove that

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \qquad k = 1 , 2 , \ldots , p .
$$

For $k = 1$ the result is equivalent to (323g). If the result has been proved for $k - 1 < p$ , we verify it for $k$ , thus completing an induction argument. We have

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } - \sum _ { i = 1 } ^ { s } \widetilde { b } _ { i } c _ { i } ^ { k - 2 } = \frac { 1 } { k - 1 } - \frac { 1 } { k ( k - 1 ) } = \frac { 1 } { k } .
$$

The next step is to extend the internal order property to stage $s$ . Write the

value of $\Phi _ { i } ( t )$ as $\textstyle \sum _ { j = 1 } ^ { s } a _ { i j } \chi _ { j }$ . We then have

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { \gamma ( t ) ( r ( t ) + 1 ) } = \sum _ { j = 1 } ^ { s } \tilde { b } _ { j } \chi _ { j } } & { } \\ { = \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { j } \chi _ { j } } & { } \\ { = b _ { s } \left( \displaystyle \sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } - \frac { 1 } { \gamma ( t ) } \right) + \sum _ { i = 1 } ^ { s } b _ { i } \frac { c _ { i } ^ { r ( t ) } } { \gamma ( t ) } } & { } \\ { = b _ { s } \left( \displaystyle \sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } - \frac { 1 } { \gamma ( t ) } \right) + \frac { 1 } { \gamma ( t ) ( r ( l ) + 1 ) } , } & { } \end{array}
$$

implying that

$$
\sum _ { j = 1 } ^ { s } a _ { s j } \chi _ { j } = \frac { 1 } { \gamma ( t ) } .
$$

Next we prove the order condition for a tree of the form $[ \tau ^ { k - 1 } t _ { 1 } ]$ where $k + r ( t _ { 1 } ) \leq p$ . We write $\begin{array} { r } { \Phi ( t _ { 1 } ) = \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } } \end{array}$ . For $k = 1$ we have

$$
\Phi ( t ) = \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { i j } \chi _ { j } = \sum _ { j = 1 } ^ { s } \widetilde { b } _ { j } \chi _ { j } = \frac { 1 } { \gamma ( t _ { 1 } ) ( r ( t _ { 1 } ) + 1 ) } = \frac { 1 } { \gamma ( t ) } .
$$

Now assume that $k > 1$ and that the result has been proved when $k$ is replaced by $k - 1$ . For the rest of this proof, we write $\begin{array} { r } { \Phi ( [ t _ { 1 } ] ) = \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } } \end{array}$ . We have $b _ { i } c _ { i } ^ { k - 1 } = b _ { i } c _ { i } ^ { k - 2 } - \widetilde { b } _ { i } c _ { i } ^ { k - 2 }$ and hence

$$
\begin{array} { l } { \Phi ( t ) = \Phi ( [ \pi ^ { k - 1 } l _ { 1 } ] ) } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } \chi _ { i } } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 2 } \chi _ { i } - \displaystyle \sum _ { i = 1 } ^ { s } \tilde { b } _ { i } c _ { i } ^ { k - 2 } \chi _ { i } } \\ { = \displaystyle \frac { 1 } { \gamma ( l _ { 1 } ) ( r ( t ) - 1 ) } - \frac { 1 } { \gamma ( l _ { 1 } ) r ( t ) ( r ( t ) - 1 ) } } \\ { = \displaystyle \frac { 1 } { \gamma ( l _ { 1 } ) r ( t ) } } \\ { = \displaystyle \frac { 1 } { \gamma ( l ) } . } \end{array}
$$

Finally, we consider a tree of the form $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ , where $r ( t _ { 1 } ) \geq r ( t _ { 2 } ) \geq$ $\cdots \geq r ( t _ { m } )$ . Because $2 q + 2 \geq p$ , $r ( t _ { k } ) \leq q$ for $k = 2 , 3 , \ldots , m$ . We now have

$$
\begin{array} { r l } { \Phi ( t ) } & { = \Phi ( [ i _ { 1 } L _ { 2 } , \cdot . . . , i _ { m } ] ) } \\ & { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \chi _ { i } ^ { \prime } \prod _ { k = 2 } ^ { t ( t _ { k } ) } c _ { i } ^ { \prime } ( t _ { k } ) } \\ & { = \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \chi c _ { i } ^ { \prime } c _ { i } ^ { \prime } ( s ) - \overline { { 1 } } \prod _ { k = 2 } ^ { s } \gamma ( t _ { k } ) } \\ & { = \displaystyle \frac { 1 } { \prod _ { k = 2 } ^ { m } \gamma ( t _ { k } ) } \Phi ( [ r ^ { \prime ( t ) - r ( t _ { k } ) - 1 } t _ { 1 } ] ) } \\ & { = \displaystyle \frac { 1 } { r ( t ) \gamma ( t _ { k } ) \prod _ { k = 2 } ^ { m } \gamma ( t _ { k } ) } } \\ & { = \displaystyle \frac { 1 } { \gamma ( t ) } . } \end{array}
$$

Before we consider how to extend the benefits of Theorem 323B beyond the gain of a single order, we look again at the generalized order conditions

$$
\widetilde { \Phi } ( t ) = \frac { 1 } { ( r ( t ) + 1 ) \gamma ( t ) } .
$$

Because the series

$$
y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { \xi ^ { r ( t ) } h ^ { r ( t ) } } { \gamma ( t ) \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) )
$$

represents the solution of

$$
y ^ { \prime } ( x ) = f ( y ( x ) )
$$

at $x = x _ { 0 } + \xi h$ , we find by integrating term by term, from $\xi = 0$ to $\xi = 1$ , that h−1  x0+h y $\begin{array} { r } { h ^ { - 1 } \int _ { x _ { 0 } } ^ { x _ { 0 } + h } y ( x ) d x } \end{array}$ has Taylor expansion

$$
y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { h ^ { r ( t ) } } { ( r ( t ) + 1 ) \gamma ( t ) \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) ) .
$$

Hence a method satisfying (323h) for $r ( t ) \leq p$ agrees with (323i) to within $O ( h ^ { p + 1 } )$ .

We can generalize the meaning of order further by replacing the single integral by the double integral

$$
\int _ { 0 } ^ { 1 } \int _ { 0 } ^ { \overline { { \xi } } } y ( x _ { 0 } + \xi h ) d \xi d \overline { { \xi } } ,
$$

and we now find

$$
h ^ { - 2 } \int _ { x _ { 0 } } ^ { x _ { 0 } + h } \int _ { x _ { 0 } } ^ { \overline { { x } } } y ( x ) d x d \overline { { x } } = \frac { 1 } { 2 } y ( x _ { 0 } ) + \sum _ { t \in T } \frac { h ^ { r ( t ) } } { ( r ( t ) + 1 ) ( r ( t ) + 2 ) \gamma ( t ) \sigma ( t ) } F ( t ) ( y ( x _ { 0 } ) + y _ { 0 } ) ,
$$

For a method with generalized order conditions, it might seem possible to carry out the process of reducing to one less stage and the second generalization of the order conditions, but this is of little value. When we have recovered the method with the first generalization, the last abscissa will have value 1, and it will not be possible to go further to recover a method satisfying the standard order conditions.

However, this difficulty can be overcome, to some extent, by setting the last component of the abscissa vector of the first generalized method to 0 rather than to 1, with appropriate modifications made to the method of recovery. To see how this works, consider the method with first level of generalized order equal to 3 whose tableau is

$$
\begin{array} { r } { \frac { 1 } { 4 } \left| \begin{array} { l l l l } { \frac { 1 } { 4 } } & { } & { } & { } \\ { \frac { 1 } { 2 } } & { 0 } & { } & { } \\ { 0 } & { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } & { } \\ { 0 } & { \frac { 1 } { 2 } } & { - \frac { 1 } { 6 } } & { \frac { 1 } { 6 } } \end{array} \right. . } \end{array}
$$

Note that this method was constructed to satisfy not only the four generalized order conditions

$$
b ^ { \mathsf { T } } \mathbf { 1 } = { \frac { 1 } { 2 } } , \quad b ^ { \mathsf { T } } c = { \frac { 1 } { 6 } } , \quad b ^ { \mathsf { T } } c ^ { 2 } = { \frac { 1 } { 1 2 } } , \quad b ^ { \mathsf { T } } A c = { \frac { 1 } { 2 4 } } ,
$$

but also the condition

$$
\sum _ { i = 1 } ^ { 4 } { \frac { b _ { i } } { 1 - c _ { i } } } = 1 ,
$$

which is imposed in anticipation of our intention to construct a fourth order method by adding an additional stage. The new method is

$$
{ \begin{array} { r l } & { 0 } \\ & { { \frac { 1 } { 4 } } } \\ & { { \frac { 1 } { 2 } } } \\ & { { \frac { 3 } { 4 } } } \\ & { 0 } \\ & { 0 } \end{array} } { \left\{ \begin{array} { r r r r r r } { 1 } & { } & { } & { } & { } & { } \\ { } & { { \frac { 1 } { 4 } } } & { } & { } & { } & { } \\ { } & { { \frac { 1 } { 2 } } } & { 0 } & { } & { } & { } \\ { } & { 0 } & { { \frac { 1 } { 2 } } } & { } & { { \frac { 1 } { 4 } } } & { } \\ { } & { } & { } & { } & { } & { { \frac { 1 } { 4 } } } \end{array} \right. }  \\ &  { \begin{array} { r r r r r r r } { \left[ { \begin{array} { r r r r r r r } { 1 } & { } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } \\ { } & { } & { { \frac { 1 } { 6 \beta } } } & { - { \frac { 1 } { 3 \beta } } } & { { \frac { 1 } { 6 \beta } } } & { } \\ { } & { - \beta } & { { \frac { 2 } { 3 } } } & { - { \frac { 1 } { 3 } } } & { { \frac { 2 } { 3 } } } & { { \beta } } \end{array} } \right] } \end{array} }
$$

and it is an easy matter to check that all the fourth order conditions are satisfied for any choice of the non-zero parameter $\beta$ .

# 324 Order barriers

It is possible, as we have seen, to derive explicit methods with $s ~ = ~ p$ for $p = 1 , 2 , 3 , 4$ . These methods are optimal in the sense that $s ~ < ~ p$ is never possible and $p = 4$ is as high as it is possible to go with $s ~ = ~ p$ . We now formalize these remarks.

Theorem 324A If an explicit $s$ -stage Runge–Kutta method has order $p$ , then $s \geq p$ .

Proof. Let $t = [ [ \cdots [ t ] \cdot \cdot \cdot ] ]$ such that $r ( t ) = p > s$ . The order condition associated with this tree is $\Phi ( t ) = 1 / \gamma ( t )$ , where $\gamma ( t ) = p !$ and $\Phi ( t ) = b ^ { \mathsf { T } } A ^ { p - 1 } \mathbf { 1 }$ . Because $A$ is strictly lower triangular, $A ^ { p } = 0$ . Hence, the order condition becomes $0 = 1 / p !$ , which has no solution. 

Theorem 324B If an explicit $s$ -stage Runge–Kutta method has order $p \geq 5$ , then $s > p$ .

Proof. Assume $s = p$ . Evaluate the values of the following four expressions:

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) ( C - c _ { 2 } I ) c = \displaystyle { \frac { 6 } { p ! } } - \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) A c = \displaystyle { \frac { 3 } { p ! } } - \frac { c _ { 4 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ( C - c _ { 2 } I ) c = \displaystyle { \frac { 2 } { p ! } } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ^ { 2 } c = \displaystyle { \frac { 1 } { p ! } } . } } \end{array}
$$

From the left-hand sides of these expressions we observe that (324a) $\times$ (324d) = (324b) $\times$ (324c). Evaluate the right-hand sides, and we find that

$$
\left( { \frac { 6 } { p ! } } - { \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 3 } { p ! } } - { \frac { c _ { 4 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

which simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$

Now consider the four expressions

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ( C - c _ { 2 } I ) c = \displaystyle \frac { 8 } { p ! } - \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ^ { 2 } c = \displaystyle \frac { 4 } { p ! } - \frac { c _ { 5 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 2 } ( C - c _ { 2 } I ) c = \displaystyle \frac { 2 } { p ! } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 3 } c = \displaystyle \frac { 1 } { p ! } . } } \end{array}
$$

Again we see that (324e) $\times$ (324h) = (324f) $\times$ (324g), so that evaluating the right-hand sides, we find

$$
\left( { \frac { 8 } { p ! } } - { \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 4 } { p ! } } - { \frac { c _ { 5 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

leading to $c _ { 2 } ( c _ { 5 } - 1 ) = 0$ . Since we cannot have $c _ { 2 } = 0$ , it follows that $c _ { 4 } =$ $c _ { 5 } = 1$ . Now evaluate $b ^ { 1 } A ^ { p - 5 } ( C - e ) A ^ { 2 } c$ . This equals $( 4 - p ) / p !$ by the order conditions but, in contradiction to this, it equals zero because component number $i$ of $b ^ { 1 } A ^ { p - 5 }$ vanishes unless $i ~ \leq ~ 5$ . However, these components of $( C - e ) A ^ { 2 } c$ vanish. $\boxed { \begin{array} { r l } \end{array} }$

The bound $s - p \ge 1$ , which applies for $p \geq 5$ , is superseded for $p \geq 7$ by $s \mathrm { ~ - ~ } p \mathrm { ~ \geq ~ 2 ~ }$ . This is proved in Butcher (1965a). For $p \geq 8$ we have the stronger bound $s - p \ge 3$ (Butcher, 1985). It seems likely that the minimum value of $s - p$ rises steadily as $p$ increases further, but there are no published results dealing with higher orders. On the other hand, it is known, because of the construction of a specific method (Hairer, 1978), that $p = 1 0$ , $s = 1 7$ is possible.

That a sufficiently high $s$ can be found to achieve order $p$ follows immediately from Theorem 317A. We now derive an upper bound on the minimum value of such an $s$ . This is done by constructing methods with odd orders, or methods satisfying the generalization of odd orders introduced in Subsection 323. In the latter case, we then use the results of that subsection to extend the result to the next even order higher.

Theorem 324C For any positive integer $p$ , an explicit Runge–Kutta method exists with order $p$ and $s$ stages, where

$$
s = \left\{ \begin{array} { l l } { \frac { 3 p ^ { 2 } - 1 0 p + 2 4 } { 8 } , \qquad } & { p \ e v e n , } \\ { \frac { 3 p ^ { 2 } - 4 p + 9 } { 8 } , \qquad } & { p \ o d d . } \end{array} \right.
$$

Proof. We consider the case of $p$ odd, but allow for generalized order conditions. If $p = 1 + 2 m$ , we construct first an implicit Runge–Kutta method with $1 + m$ stages, using (case I) standard order conditions and (case II) generalized order conditions. For case I, the order condition associated with the tree $t$ is, as usual,

$$
\Phi ( t ) = \frac { 1 } { \gamma ( t ) } .
$$

In case II, this condition is replaced by

$$
\Phi ( t ) = \frac { 1 } { ( r ( t ) + 1 ) \gamma ( t ) } .
$$

For the implicit method, the abscissae are at the zeros of the polynomial

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m } , \mathrm { i n c a s e I , } } } \\ { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m + 1 } , \mathrm { i n c a s e I I , } } } \end{array}
$$

with the zero $x = 1$ omitted in case II. It is clear that $x = 0$ is a zero in both cases and that the remaining zeros are distinct and lie in the interval $\lfloor 0 , 1 \rfloor$ . Denote the positive zeros by $\xi _ { i }$ , $i = 1 , 2 , \dots , m$ . We now construct methods with abscissae chosen from the successive rows of the following table:

$$
\begin{array} { l l l l l l } { \mathrm { r o w ~ 0 } } & { 0 } & { 0 } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 1 } } & { } & { \xi _ { 1 } } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 2 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { } & { } & { } \\ { \mathrm { r o w ~ 3 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { } & { } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } & { } \\ { \mathrm { r o w ~ m ~ } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ { \mathrm { r o w ~ m + 1 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { } \\ { \mathrm { r o w ~ 2 } m } & { } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } \end{array}
$$

where there are exactly $m + 1$ repetitions of the rows with $m$ members. The total number of stages will then be

$$
s = 1 + { \big ( } 1 + 2 + \cdot \cdot \cdot + ( m - 1 ) { \big ) } + ( m + 1 ) m = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) .
$$

Having chosen $c = \left( \begin{array} { l l l l l l } { 0 } & { \xi _ { 1 } } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \dots } & { \xi _ { m } } \end{array} \right) ^ { 1 }$ , we construct $b ^ { \scriptscriptstyle 1 }$ with all components zero except the first component and the final $m$ components. The non-zero components are chosen so that

$$
\begin{array} { l } { { b _ { 1 } + \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } = \left\{ \begin{array} { l l } { { 1 , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { 2 } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right. } } \\ { { \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } \xi _ { i } ^ { k - 1 } = \left\{ \begin{array} { l l } { { \frac { 1 } { k } , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { k ( k + 1 ) } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right\} , \quad k = 1 , 2 , \ldots , 2 m + 1 . } } \end{array}
$$

The possibility that the non-zero $b$ components can be found to satisfy these conditions follows from the theory of Gaussian quadrature. The final step in the construction of the method is choosing the elements of the matrix $A$ . For $i$ corresponding to a member of row $k$ for $k = 1 , 2 , \ldots , m$ , the only non-zero