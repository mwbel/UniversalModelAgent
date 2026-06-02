# Chapter 2

# Numerical Differential Equation Methods

# 20 The Euler Method

# 200 Introduction to the Euler methods

The famous method of Euler was published in his three-volume work Institutiones Calculi Integralis in the years 1768 to 1770, republished in his collected works (Euler, 1913). This fundamental idea is based on a very simple principle. Suppose that a particle is moving in such a way that, at time $x _ { 0 }$ , its position is equal to $y _ { 0 }$ and that, at this time, the velocity is known to be $v _ { 0 }$ . The simple principle is that, in a short period of time, so short that there has not been time for the velocity to change significantly from $v _ { 0 }$ , the change in position will be approximately equal to the change in time multiplied by $v _ { 0 }$ .

If the motion of the particle is governed by a differential equation, the value of $v _ { 0 }$ will be known as a function of $x _ { 0 }$ and $y _ { 0 }$ . Hence, given $x _ { 0 }$ and $y _ { 0 }$ , the solution at $x _ { 1 }$ , assumed to be close to $x _ { 0 }$ , can be calculated as

$$
y _ { 1 } = y _ { 0 } + ( x _ { 1 } - x _ { 0 } ) v _ { 0 } ,
$$

which can be found from known values only of $x _ { 0 }$ , $x _ { 1 }$ and $y _ { 0 }$ . Assuming that $v _ { 1 }$ , found using the differential equation from the values $x _ { 1 }$ and $y _ { 1 }$ , is sufficiently accurate, a second step can be taken to find $y _ { 2 }$ , an approximate solution at $x _ { 2 }$ , using the formula

$$
y _ { 2 } = y _ { 1 } + ( x _ { 2 } - x _ { 1 } ) v _ { 1 } .
$$

A sequence of approximations $y _ { 1 }$ , $y _ { 2 }$ , $y _ { 3 }$ , . . . to the solution of the differential equation at $x _ { 1 }$ , $x _ { 2 }$ , $x _ { 3 }$ , . . . is intended to lead eventually to acceptable approximations, at increasingly distant times from where the initial data was given.

Of course, the interpretation of the Euler method is much wider than in the description of the motion of a single particle, moving in time along a line. Even though the independent variable, which we denote by $x$ , will not always have the meaning of physical time, we will often refer to it as the ‘time variable’. The dependent variable $y$ need not have the meaning of distance and need not even be scalar. If $y$ is vector-valued, then it can be interpreted as a collection of scalar-valued components $y _ { 1 }$ , $y _ { 2 } , \ldots$ , $y _ { N }$ . Thus, we can write

$$
\begin{array} { r } { y ( x ) = \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { N } ( x ) } \end{array} \right] . } \end{array}
$$

The differential equation, and the initial information, which together determine the values of the $y$ components as the time variable varies, can be written in the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } .
$$

In the vector-valued case, the function $f$ is defined on $\mathbb { R } \times \mathbb { R } ^ { N }$ to $\mathbb { R } ^ { N }$ . However, it is often convenient to write the individual components of $f$ as scalar-valued functions of $x$ and the vector $y ( x )$ ; or, what is equivalent, of the individual components of $y ( x )$ . Similarly, the initial information can also be written in terms of individual components $y _ { 1 0 }$ , $y _ { 2 0 }$ , $\cdot \cdot \cdot$ , $y _ { N 0 }$ of $y _ { 0 }$ . There is a potential for confusion in the use of subscripts to denote either individual components of $y$ , or individual values of $x$ , at which $y$ is evaluated or approximated. This confusion will be avoided by using each notation only in a context which makes the meaning clear, or else, where it becomes necessary, by refining the notation.

With the freedom we have to write $y$ as a vector or as an ensemble of scalars, we see that (200a) can be written in one of several equivalent forms. We can write out the components of $y ( x )$ in $f ( x , y ( x ) )$ to emphasize the dependence of $y ^ { \prime } ( x )$ on each of these components:

$$
y ^ { \prime } ( x ) = f ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \ldots , y _ { N } ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

or we can take this a step further by writing out the individual components of $y ^ { \prime } ( x )$ :

$$
{ \left[ \begin{array} { l } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \\ { \vdots } \\ { y _ { N } ^ { \prime } ( x ) } \end{array} \right] } = f ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \ldots , y _ { N } ( x ) ) , \qquad y ( x _ { 0 } ) = { \left[ \begin{array} { l } { y _ { 1 0 } } \\ { y _ { 2 0 } } \\ { \vdots } \\ { y _ { N 0 } } \end{array} \right] } .
$$

Finally, we obtain a very detailed formulation by writing everything in terms of individual components:

![](images/9d041549e8ffb818f2fdca0ebe720318c79512fff55a7f8fe904e82eec4910d8.jpg)  
An example of the Euler method

$$
\begin{array} { r } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \\ { \vdots } \\ { y _ { N } ^ { \prime } ( x ) } \end{array} = \left[ \begin{array} { c } { f _ { 1 } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \\ { f _ { 2 } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \\ { \vdots } \\ { f _ { N } ( x , y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dotsc , y _ { N } ( x ) ) } \end{array} \right] , \left[ \begin{array} { c } { y _ { 1 } ( x _ { 0 } ) } \\ { y _ { 2 } ( x _ { 0 } ) } \\ { \vdots } \\ { y _ { N } ( x _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { c } { y _ { 1 0 } } \\ { y _ { 2 0 } } \\ { \vdots } \\ { y _ { N 0 } } \end{array} \right] .
$$

An important special case is that $f \mathrm { ~ - ~ } \mathrm { o r }$ , for vector problems, each of the functions $f _ { 1 }$ , $f _ { 2 }$ , . . . , $f _ { N } - \mathrm { d o e s }$ not depend on the time variable at all. In this case, we refer to the problem as being ‘autonomous’, and write it in the form

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

or in one of the expanded forms.

To conclude this subsection, we present a pictorial illustration of the use of the Euler method, for the scalar initial value problem

$$
\frac { d y } { d x } = \frac { y - 2 x y ^ { 2 } } { 1 + x } , \qquad y ( 0 ) = \frac { 2 } { 5 } .
$$

Five steps with the method, using equally sized time steps $\textstyle { \frac { 1 } { 5 } }$ , are taken and shown against a background of solutions with varying initial values. The general solution to this problem is given by

$$
y ( x ) = \frac { 1 + x } { C + x ^ { 2 } } ,
$$

for $C$ an arbitrary constant, and the exact and approximate solutions are shown in Figure 200(i).

# 201 Some numerical experiments

To see how the Euler method works in practice, consider the initial value problem

$$
{ \frac { d y } { d x } } = { \frac { y + x } { y - x } } , \quad y ( 0 ) = 1 ,
$$

for which the exact solution is

$$
y ( x ) = x + { \sqrt { 1 + 2 x ^ { 2 } } } .
$$

To calculate the solution at $x = 0 . 1$ using the Euler method, we need to use the approximation $y ( 0 . 1 ) \approx y ( 0 ) + 0 . 1 y ^ { \prime } ( 0 )$ . Since $y ( 0 ) = 1$ and $y ^ { \prime } ( 0 ) = 1$ , we find $y ( 0 . 1 ) \approx y ( 0 ) + 0 . 1 y ^ { \prime } ( 0 ) = 1 + 0 . 1 = 1 . 1$ .

We can now take the calculation a second step forward, to find an approximation at $x = 0 . 2$ using the formula $y ( 0 . 2 ) \approx y ( 0 . 1 ) + 0 . 1 y ^ { \prime } ( 0 . 1 )$ . For the value of $y ( 0 . 1 )$ , we can use the result of the first Euler step and for the value of $y ^ { \prime } ( 0 . 1 )$ , we can use (201a) with the approximate value of $y ( 0 . 1 )$ substituted. This gives $y ^ { \prime } ( 0 . 1 ) \approx ( 1 . 1 + 0 . 1 ) / ( 1 . 1 - 0 . 1 ) = 1 . 2$ . Hence, y(0.2)  y(0.1) + 0.1y- (0.1)  1.1 + 0.12 = 1.22.

In Table 201(I) these calculations are continued as far as $x = 0 . 5$ . Steps of size 0.1 are taken throughout but, for comparison, the same results are also given for steps of sizes 0.05 and 0.025, respectively. For the three columns of approximations, the headings $h = 0 . 1$ , $h = 0 . 0 5$ and $h = 0 . 0 2 5$ denote the sizes of the steps used to arrive at these approximations. The exact values of $y$ are also given in the table.

It is interesting to compare the errors generated in the very first step, for the three values of $h$ that we have used. For $h = 0 . 1$ , the exact solution minus the computed solution is $1 . 1 0 9 9 5 0 - 1 . 1 0 0 0 0 0 = 0 . 0 0 9 9 5 0$ ; for $h = 0 . 0 5$ , the corresponding difference is $1 . 0 5 2 4 9 7 - 1 . 0 5 0 0 0 0 = 0 . 0 0 2 4 9 7$ ; for $h = 0 . 0 2 5$ , the difference is $1 . 0 2 5 6 ^ { \cdot } 2 5 - 1 . 0 2 5 0 0 0 = 0 . 0 0 0 6 2 5$ . It is seen that, approximately, when $h$ is multiplied by a factor of $\textstyle { \frac { 1 } { 2 } }$ , the error in the first step is multiplied by a factor of $\textstyle { \frac { 1 } { 4 } }$ . This is to be expected because, according to Taylor’s theorem, the exact answer at $x = h$ is $y ( h ) \approx y ( 0 ) + h y ^ { \prime } ( 0 ) + ( h ^ { 2 } / 2 ) y ^ { \prime \prime } ( 0 )$ . The first two terms of this approximation are exactly what is calculated by the Euler method, so that the error should be close to $( h ^ { 2 } / 2 ) y ^ { \prime \prime } ( 0 )$ . We can check this more closely by evaluating $y ^ { \prime \prime } ( 0 ) = 2$ .

Of greater interest in understanding the quality of the numerical approximation is the error accumulated up to a particular $x$ value, by a sequence of Euler steps, with varying value of $h$ . In the case of $x \ : = \ : 0 . 5$ , we see that, for the three stepsizes we have used, the errors are respectively $1 . 7 2 4 7 4 5 - 1 . 6 8 7 5 5 5 = 0 . 0 3 7 1 9 0$ , $1 . 7 2 4 7 4 5 - 1 . 7 0 6 5 7 0 = 0 . 0 1 8 1 7 5$ and $1 . 7 2 4 7 4 5 - 1 . 7 1 5 7 6 0 = 0 . 0 0 8 9 8 5$ . These error values approximately drop by a factor $\textstyle { \frac { 1 } { 2 } }$ when $h$ is reduced by this same factor. The reason for this will be discussed more fully in Subsection 212, but it can be understood informally. Note that there is a comparable error produced in each of the steps, but there are more of these steps, if $h$ is small. In the case of the present calculation, the error is about $h ^ { 2 }$ in each step, but to get as far as $x = 0 . 5$ , $n = 1 / 2 h$ steps have to be carried out. This leads to a total error of about $n h ^ { 2 } = 0 . 5 h$ . A slight refinement of this argument would replace $y ^ { \prime \prime } ( 0 )$ by the mean of this quantity over the interval $\left\lfloor 0 , 0 . 5 \right\rfloor$ . The value of this mean is approximately 1.63299, so that the total error should be about $0 . 4 0 8 2 5 h$ . This very crude argument leads to a prediction that is incorrect by a factor of only about $1 0 \%$ . In the solution of practical problems using the Euler method, or indeed a different method, it is not really feasible to estimate the total accumulated error, but it is important to know the asymptotic form of the error in terms of $h$ . This will often make it possible to gauge the quality of approximations, by comparing the values for differing $h$ values. It will also often make it possible to make realistic decisions as to which of various alternative numerical methods should be used for a specific problem, or even for a large class of problems.

Euler method: problem (201a)   

<table><tr><td>x</td><td>h=0.1</td><td>h=0.05</td><td>h=0.025</td><td>y</td></tr><tr><td>0.000000</td><td>1.000000</td><td>1.000000</td><td>1.000000</td><td>1.000000</td></tr><tr><td>0.025000</td><td></td><td></td><td>1.025000</td><td>1.025625</td></tr><tr><td>0.050000</td><td></td><td>1.050000</td><td>1.051250</td><td>1.052497</td></tr><tr><td>0.075000</td><td></td><td></td><td>1.078747</td><td>1.080609</td></tr><tr><td>0.100000</td><td>1.100000</td><td>1.105000</td><td>1.107483</td><td>1.109950</td></tr><tr><td>0.125000</td><td></td><td></td><td>1.137446</td><td>1.140505</td></tr><tr><td>0.150000</td><td></td><td>1.164950</td><td>1.168619</td><td>1.172252</td></tr><tr><td>0.175000</td><td></td><td></td><td>1.200982</td><td>1.205170</td></tr><tr><td>0.200000</td><td>1.220000</td><td>1.229729</td><td>1.234510</td><td>1.239230</td></tr><tr><td>0.225000</td><td></td><td></td><td>1.269176</td><td>1.274405</td></tr><tr><td>0.250000</td><td></td><td>1.299152</td><td>1.304950</td><td>1.310660</td></tr><tr><td>0.275000</td><td></td><td></td><td>1.341799</td><td>1.347963</td></tr><tr><td>0.300000</td><td>1.359216</td><td>1.372981</td><td>1.379688</td><td>1.386278</td></tr><tr><td>0.325000</td><td></td><td></td><td>1.418581</td><td>1.425568</td></tr><tr><td>0.350000</td><td></td><td>1.450940</td><td>1.458440</td><td>1.465796</td></tr><tr><td>0.375000</td><td></td><td></td><td>1.499228</td><td>1.506923</td></tr><tr><td>0.400000</td><td>1.515862</td><td>1.532731</td><td>1.540906</td><td>1.548913</td></tr><tr><td>0.425000</td><td></td><td></td><td>1.583436</td><td>1.591726</td></tr><tr><td>0.450000</td><td></td><td>1.618044</td><td>1.626780</td><td>1.635327</td></tr><tr><td>0.475000</td><td></td><td></td><td>1.670900</td><td>1.679678</td></tr><tr><td>0.500000</td><td>1.687555</td><td>1.706570</td><td>1.715760</td><td>1.724745</td></tr></table>

Euler method: problem (201d) with $e = 0$   

<table><tr><td>h</td><td>Y1</td><td>y2</td><td>y3</td><td>Y4</td><td>|Errorll</td></tr><tr><td>π 200</td><td>-1.084562</td><td>0.133022</td><td>-0.159794</td><td>-0.944876</td><td>0.231124</td></tr><tr><td>π 400 T</td><td>-1.045566</td><td>0.067844</td><td>-0.085837</td><td>-0.973596</td><td>0.121426</td></tr><tr><td>800</td><td>-1.023694</td><td>0.034251</td><td>-0.044572</td><td>-0.987188</td><td>0.062333</td></tr><tr><td>π 1600</td><td>-1.012087</td><td>0.017207</td><td>-0.022723</td><td>-0.993707</td><td>0.031593</td></tr><tr><td>π 3200</td><td>-1.006106</td><td>0.008624</td><td>-0.011474</td><td>-0.996884</td><td>0.015906</td></tr><tr><td>π 6400</td><td>-1.003068</td><td>0.004317</td><td>-0.005766</td><td>-0.998450</td><td>0.007981</td></tr><tr><td>π 12800</td><td>-1.001538</td><td>0.002160</td><td>-0.002890</td><td>-0.999227</td><td>0.003998</td></tr><tr><td>π 25600</td><td>-1.000770</td><td>0.001080</td><td>-0.001447</td><td>-0.999614</td><td>0.002001</td></tr></table>

$\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$   

<table><tr><td>h</td><td>Y1</td><td>y2</td><td>Y3</td><td>Y4</td><td>|Error|l</td></tr><tr><td>π 200</td><td>-1.821037</td><td>0.351029</td><td>-0.288049</td><td>-0.454109</td><td>0.569602</td></tr><tr><td>T 400</td><td>-1.677516</td><td>0.181229</td><td>-0.163203</td><td>-0.517588</td><td>0.307510</td></tr><tr><td>π 800</td><td>-1.593867</td><td>0.091986</td><td>-0.087530</td><td>-0.548433</td><td>0.160531</td></tr><tr><td>π 1600</td><td>-1.548345</td><td>0.046319</td><td>-0.045430</td><td>-0.563227</td><td>0.082134</td></tr><tr><td>π 3200</td><td>-1.524544</td><td>0.023238</td><td>-0.023158</td><td>-0.570387</td><td>0.041559</td></tr><tr><td>π 6400</td><td>-1.512368</td><td>0.011638</td><td>-0.011693</td><td>-0.573895</td><td>0.020906</td></tr><tr><td>π 12800</td><td>-1.506208</td><td>0.005824</td><td>-0.005875</td><td>-0.575630</td><td>0.010485</td></tr><tr><td>π 25600</td><td>-1.503110</td><td>0.002913</td><td>-0.002945</td><td>-0.576491</td><td>0.005251</td></tr></table>

Table 201(IV) Euler method: problem (201d) with $\textstyle e = { \frac { 3 } { 4 } }$   

<table><tr><td>h</td><td>Y1</td><td>y2</td><td>Y3</td><td>Y4</td><td>|Error|l</td></tr><tr><td>π 200</td><td>-2.945389</td><td>1.155781</td><td>-0.739430</td><td>0.029212</td><td>1.864761</td></tr><tr><td>π 400</td><td>-2.476741</td><td>0.622367</td><td>-0.478329</td><td>-0.168796</td><td>1.089974</td></tr><tr><td>π 800</td><td>-2.162899</td><td>0.322011</td><td>-0.284524</td><td>-0.276187</td><td>0.604557</td></tr><tr><td>π 1600</td><td>-1.972584</td><td>0.163235</td><td>-0.158055</td><td>-0.329290</td><td>0.321776</td></tr><tr><td>π 3200</td><td>-1.865987</td><td>0.082042</td><td>-0.083829</td><td>-0.354536</td><td>0.166613</td></tr><tr><td>π 6400</td><td>-1.809268</td><td>0.041102</td><td>-0.043252</td><td>-0.366542</td><td>0.084872</td></tr><tr><td>元 12800</td><td>-1.779967</td><td>0.020567</td><td>-0.021980</td><td>-0.372336</td><td>0.042847</td></tr><tr><td>π 25600</td><td>-1.765068</td><td>0.010287</td><td>-0.011081</td><td>-0.375172</td><td>0.021528</td></tr></table>

It is equally straightforward to solve problems in more than one dependent variable using the Euler method. Given the problem of inverse-square law attraction in two dimensions

$$
Y ^ { \prime \prime } ( x ) = - { \frac { 1 } { \| Y ( x ) \| ^ { 3 / 2 } } } Y ( x ) ,
$$

where $\| Y \| = \sqrt { Y _ { 1 } ^ { 2 } + Y _ { 2 } ^ { 2 } }$ , it is necessary to first write the problem as a system of first order equations. This is done by writing $y _ { 1 }$ and $y _ { 2 }$ for the space coordinates $Y _ { 1 }$ and $Y _ { 2 }$ , and writing $y _ { 3 }$ and $y _ { 4 }$ for the velocity coordinates, given as the first derivatives of $Y _ { 1 }$ and $Y _ { 2 }$ . With this reformulation, the system of differential equations is written in the form

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = y _ { 4 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = - \frac { y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } , } \\ { \displaystyle \frac { d y _ { 4 } } { d x } = - \frac { y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } . } \end{array}
$$

The initial value, written as a vector $y ( 0 ) = [ 1 , 0 , 0 , 1 ] ^ { \scriptscriptstyle 1 }$ , defines the solution $y ( x ) = [ \cos ( x ) , \sin ( x ) , - \sin ( x ) , \cos ( x ) ] ^ { \mathrm { t } }$ . The first step of the Euler method gives a numerical result $y ( h ) \ \approx \ [ 1 , h , - h , 1 ] ^ { 1 }$ ; this differs from the exact result by approximately $[ - \textstyle { \frac { 1 } { 2 } } h ^ { 2 } , - \textstyle { \frac { 1 } { 6 } } h ^ { 3 } , \textstyle { \frac { 1 } { 6 } } h ^ { 3 } , - \textstyle { \frac { 1 } { 2 } } h ^ { 2 } ] ^ { \mathsf { T } } .$ . Rather than look at all the components of the error vector individually, it is often convenient to compute the norm of this vector and consider its behaviour as a function of $h$ .

It will be interesting to perform many steps, sufficient to complete, for example, half of one orbit and to compare the (Euclidean) norm of the error for differing values of $h$ . For various values of $h$ , decreasing in sequence by a factor $\textstyle { \frac { 1 } { 2 } }$ , some calculations are presented for this experiment in Table 201(II). The approximate halving of the error, when $h$ is halved, is easily observed in this table.

If the same problem is solved using initial values corresponding to an elliptic, rather than a circular, orbit, a similar dependence of the error on $h$ is observed, but with errors greater in magnitude. Table 201(III) is for an orbit with eccentricity $\begin{array} { l } { e \ = \ \frac { 1 } { 2 } } \end{array}$ . The starting value corresponds to the closest point on the orbit to the attracting force, and the exact value at the end of a half period is

$$
y ( 0 ) = \left[ \begin{array} { c } { { 1 - e } } \\ { { 0 } } \\ { { 0 } } \\ { { \sqrt { \frac { 1 + e } { 1 - e } } } } \end{array} \right] = \left[ \begin{array} { c } { { \frac { 1 } { 2 } } } \\ { { 0 } } \\ { { 0 } } \\ { { \sqrt { 3 } } } \end{array} \right] , \qquad y ( \pi ) = \left[ \begin{array} { c } { { - 1 - e } } \\ { { 0 } } \\ { { 0 } } \\ { { - \sqrt { \frac { 1 - e } { 1 + e } } } } \end{array} \right] = \left[ \begin{array} { c } { { - \frac { 3 } { 2 } } } \\ { { 0 } } \\ { { 0 } } \\ { { - \frac { 1 } { \sqrt { 3 } } } } \end{array} \right] .
$$

When the eccentricity is further increased to $\textstyle e = { \frac { 3 } { 4 } }$ , the loss of accuracy in carrying out the computation is even more pronounced. Results for $\begin{array} { l l l } { e } & { = } & { { \frac { 3 } { 4 } } } \end{array}$ are given in Table 201(IV), where we note that, in this case, $\begin{array} { r } { y ( \pi ) = [ - \frac { 7 } { 4 } , 0 , 0 , - 1 / \sqrt { 7 } ] ^ { \intercal } } \end{array}$ .

# 202 Calculations with stepsize control

The use of the Euler method, with constant stepsize, may not be efficient for some problems. For example, in the case of the eccentric orbits, discussed in the previous subsection, a small step should be taken for points on the orbit, close to the attracting force, and a larger step for points remote from the attracting force. In deciding how we might attempt to control the stepsize for a general problem, we need to consider how the error committed in each step can be estimated. First, however, we consider how the stepsize in a step should be chosen, to take account of this error estimate.

Because the total error is approximately the sum of the errors committed in the individual steps, at least for a limited number of steps, we look at a simple model in which the interval of integration is divided up into $m$ subintervals, with lengths ${ \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { m } }$ . We assume that the norms of the errors in steps carried out in these intervals are $C _ { 1 } h _ { 1 } ^ { 2 } , C _ { 2 } h _ { 2 } ^ { 2 } , \ldots , C _ { m } h _ { m } ^ { 2 }$ , respectively, where $h _ { 1 } , h _ { 2 } , \ldots , h _ { m }$ are the constant stepsizes in these subintervals. Assume that a total of $N$ steps of integration by the Euler method are carried out and that a fraction $t _ { i }$ of these are performed in subinterval $i = 1 , 2 , \dots , m$ . This means that $t _ { i } N$ steps are carried out in subinterval $i$ and that $h _ { i } = \delta _ { i } / t _ { i } N$ . The total error committed, which we assume, in the absence of further information, to be the sum of the individual errors, is approximately

$$
E = \sum _ { i = 1 } ^ { m } ( t _ { i } N ) C _ { i } \left( \frac { \delta _ { i } } { t _ { i } N } \right) ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { m } \delta _ { i } ^ { 2 } C _ { i } t _ { i } ^ { - 1 } ,
$$

where $\delta _ { i } / t _ { i } N$ is the stepsize used for every step in subinterval number $i$ . By the Cauchy–Schwarz inequality, the minimum value of (202a) is achieved by

$$
t _ { i } = \frac { \delta _ { i } \sqrt { C _ { i } } } { \sum _ { j = 1 } ^ { m } \delta _ { j } \sqrt { C _ { j } } }
$$

and it follows that optimality occurs when $C _ { i } h _ { i } ^ { 2 }$ is maintained constant over every subinterval. We interpret this result to mean that the estimated values of the error should be kept as close as possible to some pre-assigned value.

![](images/e91c8200d4af0f1ff8adae2902d909284f67d0b2726bbc386215fd366a6bea55.jpg)  
Constant (◦) and variable (•) step for orbit with eccentricities $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ $( - \cdot - )$ and $\textstyle e = { \frac { 3 } { 4 } }$ (· · · )

This pre-assigned value, which is under control of the user, will be regarded as the user-imposed tolerance.

To actually estimate the error committed in each step, we have a natural resource at our disposal; this is the availability of approximations to $h y ^ { \prime } ( x )$ at the beginning and end of every step. At the beginning of step $n$ , it is, of course, the value of $h f ( x _ { n - 1 } , y _ { n - 1 } )$ used in the computation of the Euler step itself. At the end of this step we can calculate $h f ( x _ { n } , y _ { n } )$ . This might seem to be an additional calculation of the function $f$ , but this computation needs to be done anyway, since it is needed when the following step is eventually carried out. From these approximations to $h y ^ { \prime } ( x _ { n - 1 } )$ and $h y ^ { \prime } ( x _ { n } )$ we can recalculate the step from $y _ { n - 1 }$ using the more accurate trapezoidal rule to yield the improved approximation to $y ( x _ { n } )$ , given by

$$
y ( x _ { n } ) \approx y ( x _ { n - 1 } ) + { \frac { 1 } { 2 } } { \big ( } h y ^ { \prime } ( x _ { n - 1 } ) + h y ^ { \prime } ( x _ { n } ) { \big ) } ,
$$

and we can use the difference between this approximation to $y ( x _ { n } )$ , and the result computed by the Euler step, as our local error estimate.

Hence we have, as an estimate of the norm of the error,

$$
\frac 1 2 \| h f ( x _ { n - 1 } , y ( x _ { n - 1 } ) ) - h f ( x _ { n } , y ( x _ { n } ) ) \| .
$$

As an illustration of how variable stepsize works in practice, the calculations of gravitational orbits with eccentricities 0.5 and 0.75 have been repeated using variable stepsize, but with the tolerances set at values that will give a total number of steps approximately the same as for the constant stepsize cases already investigated. A summary of the results is shown in Figure 202(i). To make the comparisons straightforward, only norms of errors are plotted against stepsize (or mean stepsize in the variable stepsize cases).

![](images/cb7e396e6d14461e335427110fe36a8bdc1059bd4be610ee21829d26ce48a5a8.jpg)  
Norm error against $n ^ { - 1 }$ for the ‘mildly stiff’ problem (203a)

203 Calculations with mildly stiff problems

Consider the initial value problem

$$
\begin{array} { l l l } { \displaystyle \frac { d y _ { 1 } } { d x } = - 1 6 y _ { 1 } + 1 2 y _ { 2 } + 1 6 \cos ( x ) - 1 3 \sin ( x ) , } & { y _ { 1 } ( 0 ) = 1 , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = 1 2 y _ { 1 } - 9 y _ { 2 } - 1 1 \cos ( x ) + 9 \sin ( x ) , } & { y _ { 2 } ( 0 ) = 0 , } \end{array}
$$

for which the exact solution is $y _ { 1 } ( x ) = \cos ( x )$ , $y _ { 2 } ( x ) = \sin ( x )$ . We attempt to solve this problem using the Euler method. First, we use constant stepsize. Specifically, we perform $n$ steps with $h = \pi / n$ and with $n$ taking on various integer values. This yields a sequence of approximations to $y ( \pi )$ , and results for the norm of the error are given in Figure 203(i).

The results shown here have a disturbing feature. Even though the asymptotic first order behaviour is clearly seen, this effect is recognizable only below a certain threshold, corresponding to $n = 3 8$ . For $h$ above the corresponding value of $\pi / 3 8$ , the errors grow sharply, until they dominate the solution itself. We consider what can be done to avoid this extreme behaviour and we turn to variable stepsize as a possible remedy. We need to be more precise than in Subsection 202, in deciding how we should apply this approach. After a step has been completed, we have to either accept or reject the step, and rejecting requires us to repeat the step, but with a scaled-down stepsize. In either case we need a policy for deciding on a stepsize to use in the new attempt at the failed step, or to use in the succeeding new step.

Because the local truncation error is asymptotically proportional to the square of $h$ , it makes sense to scale the stepsize in the ratio $\sqrt { T / \| E \| }$ , where $E$ is the error estimate and $T$ is the maximum permitted value of $\| E \|$ . However, it is essential to insert a ‘safety factor’ $S$ , less than $^ { 1 }$ , into the computation, to guard against a rejection in a new step, because of slight variations in the magnitude of the error estimate from step to step. It is also wise to use two further design parameters, $M$ and $m$ , representing the maximum and minimum stepsize ratios that will be permitted. Typically $M \ = \ 2$ , $m = \textstyle { \frac { 1 } { 2 } }$ and $S = 0 . 9$ , and we adopt these values. Fortunately, this experiment of using variable stepsize is successful, as is seen from Figure 203(ii).

![](images/fb9432b310ee636ef36e76450bcbb193c0afa071c2ab8b8bc782a7c64dfa4bcf.jpg)  
Norm error against tolerance $T$ for the ‘mildly stiff’ problem (203a) with variable stepsize

There is a loss of efficiency, in that unstable behaviour typically results in wide variations of stepsize, in sequences of adjacent steps. However, there are relatively few steps rejected, because of excessive error estimates. For the special choice of the tolerance $T = 0 . 0 2$ , 38 successful steps were taken, in addition to 11 failed steps. The value of the stepsize $h$ as a function of the value of $x$ , at the beginning of each of the steps, is shown in Figure 203(iii).

The phenomenon experienced with this example goes under the name of ‘stiffness’. To understand why this problem is stiff, and why there seems to be a value of $h$ such that, for values of the stepsize above this, it cannot be solved by the Euler method, write $v _ { 1 } ( x )$ and $v _ { 2 } ( x )$ for the deviations of $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ from the exact solution. That is, $y _ { 1 } ( x ) = \cos ( x ) + v _ { 1 } ( x )$ and $y _ { 2 } ( x ) = \sin ( x ) + v _ { 2 } ( x )$ . Because the system is linear, it reduces in a simple way to

$$
\left[ \begin{array} { r } { \frac { d v _ { 1 } } { d x } } \\ { \frac { d v _ { 2 } } { d x } } \end{array} \right] = \left[ \begin{array} { r r } { - 1 6 } & { 1 2 } \\ { 1 2 } & { - 9 } \end{array} \right] \left[ \begin{array} { r } { v _ { 1 } } \\ { v _ { 2 } } \end{array} \right] .
$$

To simplify the discussion further, find the eigenvalues, and corresponding eigenvectors, of the matrix $A$ occurring in (203b), where

$$
A = \left[ \begin{array} { r r } { { - 1 6 } } & { { 1 2 } } \\ { { 1 2 } } & { { - 9 } } \end{array} \right] .
$$

![](images/e5ec87d24fe6f6a58f63268602770b722684a1ae4cbdbad83f361e189ae8e4fa.jpg)  
Stepsize $h$ against $_ { x }$ for the ‘mildly stiff’ problem (203a) with variable stepsize for $T = 0 . 0 2$

The eigenvalues of $A$ are $\lambda _ { 1 } = 0$ and $\lambda _ { 2 } = - 2 5$ and the eigenvectors are the columns of the matrix

$$
T = \left[ \begin{array} { r r } { { 3 } } & { { 4 } } \\ { { 4 } } & { { - 3 } } \end{array} \right] .
$$

By substituting $v = T w$ , that is,

$$
\left[ \begin{array} { l } { v _ { 1 } } \\ { v _ { 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 3 } & { 4 } \\ { 4 } & { - 3 } \end{array} \right] \left[ \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right] ,
$$

we find that

$$
\left[ \begin{array} { r } { \left[ \frac { d w _ { 1 } } { d x } \right] } \\ { \frac { d w _ { 2 } } { d x } } \end{array} \right] = \left[ \begin{array} { r r } { 0 } & { 0 } \\ { 0 } & { - 2 5 } \end{array} \right] \left[ \begin{array} { r } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right] .
$$

The components of $w$ each have bounded solutions, and thus the original differential equation is stable. In particular, any perturbation in $w _ { 2 }$ will lead to very little change in the long term solution, because of the quickly decaying exponential behaviour of this component. On the other hand, when the equation for $w _ { 2 }$ is solved numerically, difficulties arise. In a single step of size $h$ , the exact solution for $w _ { 2 }$ should be multiplied by $\exp ( - 2 5 h )$ , but the numerical approximation is multiplied by $1 - 2 5 h$ . Even though $| \exp ( - 2 5 h ) |$ is always less than 1 for positive $h$ , $| 1 - 2 5 h |$ is greater than 1, so that its powers form an unbounded sequence, unless $h \leq \frac { 2 } { 2 5 }$ .

This, then, is the characteristic property of stiffness: components of the solution that should be stable become unstable when subjected to numerical approximations in methods like the Euler method.

Comparison of explicit and implicit Euler methods: problem (201a)   

<table><tr><td>n</td><td>Explicit error</td><td>Implicit error</td><td>Iterations</td></tr><tr><td>5</td><td>0.03719000</td><td>-0.03396724</td><td>28</td></tr><tr><td>10</td><td>0.01817489</td><td>-0.01737078</td><td>47</td></tr><tr><td>20</td><td>0.00898483</td><td>-0.00878393</td><td>80</td></tr><tr><td>40</td><td>0.00446704</td><td>-0.00441680</td><td>149</td></tr><tr><td>80</td><td>0.00222721</td><td>-0.00221462</td><td>240</td></tr><tr><td>160</td><td>0.00111203</td><td>-0.00110889</td><td>480</td></tr><tr><td>320</td><td>0.00055562</td><td>-0.00055484</td><td>960</td></tr><tr><td>640</td><td>0.00027771</td><td>-0.00027762</td><td>1621</td></tr></table>

# 204 Calculations with the implicit Euler method

As we have pointed out, the Euler method approximates the integral of $y ^ { \prime } ( x )$ , over each subinterval $[ x _ { n - 1 } , x _ { n } ]$ , in terms of the width of the interval, multiplied by an approximation to the height of the integrand at the left-hand end. We can consider also the consequences of using the width of this interval, multiplied by the height at the right-hand end.

This would mean that the approximation at $x _ { 1 }$ would be defined by $y ( x _ { 1 } ) \approx y _ { 1 }$ , where $y _ { 1 } = y _ { 0 } + h f ( x _ { 1 } , y _ { 1 } ) $ . This results in what is known as the ‘implicit Euler method’. The complication is, of course, that the solution approximation at the end of the step is defined not by an explicit formula, but as the solution to an algebraic equation.

For some problems, we can evaluate by simple (‘fixed point’) iteration. That is, we calculate a sequence of approximations $Y ^ { \left[ 0 \right] }$ , $Y ^ { \left[ 1 \right] }$ , $Y ^ { \left[ 2 \right] }$ , . . . using the formula

$$
Y ^ { [ k ] } = y _ { 0 } + h f ( x _ { 1 } , Y ^ { [ k - 1 ] } ) , \quad k = 1 , 2 , 3 , \dots x .
$$

Assuming that the sequence of approximations converges, to within a required tolerance, to a limiting value $Y$ , then we take this limit as the value of $y _ { 1 }$ . The starting value in the sequence may be taken, for simplicity and convenience, as $y _ { 0 }$ .

Some results for this method, as applied to the initial value problem (201a), are given in Table 204(I). In this table, all approximations are made for the solution at $x = 0 . 5$ and, for each number of steps $n$ , the calculation is carried out using both the Euler method and the implicit form of the Euler method. The total errors for the two methods are shown. In the case of the implicit method, the total number of iterations to achieve convergence, to within a tolerance of $1 0 ^ { - 6 }$ , is also given. If a tolerance as high as $1 0 ^ { - 4 }$ had been specified, there would have been only about two, rather than three, iterations per step, but the cost would still be approximately twice as great as for the explicit Euler method.

![](images/613b726b7fefffea7015667200c5194821c31402f8ff8d38599c49688745950f.jpg)  
Norm error against $n ^ { - 1 }$ for the ‘mildly stiff’ problem (203a) using the method (204a)

As we see from these results, there is no advantage in the implicit form of the Euler method, in the case of this problem. On the contrary, there is a serious disadvantage, because of the very much greater computing cost, as measured in terms of $f$ evaluations, for the implicit as compared with the explicit form of the method.

For stiff problems, such as that given by (203a), the implicit Euler method shows itself to advantage. Since this problem is linear, it is possible to write the answer for the approximation computed at the end of a step explicitly. In the step going from $x _ { 0 }$ to $x _ { 1 } = x _ { 0 } + h$ , with solution approximations going from $y _ { 0 } = [ ( y _ { 0 } ) _ { 1 } , ( y _ { 0 } ) _ { 2 } ] ^ { 1 }$ to $y _ { 1 } = [ ( y _ { 1 } ) _ { 1 } , ( y _ { 1 } ) _ { 2 } ] ^ { 1 }$ , we have the relations between these quantities given by

$$
\stackrel { \scriptscriptstyle ( y _ { 1 } ) _ { 1 } } { \scriptscriptstyle ( y _ { 1 } ) _ { 2 } } \stackrel { \scriptscriptstyle } { = } h \left[ \stackrel { \displaystyle - 1 6 } { \displaystyle 1 2 } \quad \stackrel { \mathrm { \scriptsize ~ 1 2 } } { \scriptscriptstyle - 9 } \right] \stackrel { \displaystyle } { \left[ ( y _ { 1 } ) _ { 2 } \right] } + \stackrel { \displaystyle \left[ ( y _ { 0 } ) _ { 1 } \right] } { \scriptscriptstyle ( y _ { 0 } ) _ { 2 } } + h \left[ \stackrel { \displaystyle 1 6 \cos ( x _ { 1 } ) - 1 3 \sin ( x _ { 1 } ) } { \displaystyle - 1 1 \cos ( x _ { 1 } ) + 9 \sin ( x _ { 1 } ) } \right] ,
$$

so that

$$
\left[ 1 + 1 6 h - 1 2 h \right] \left[ ( y _ { 1 } ) _ { 1 } \right] = \left[ ( y _ { 0 } ) _ { 1 } + 1 6 h \cos ( x _ { 1 } ) - 1 3 h \sin ( x _ { 1 } ) \right] ,
$$

and the new approximation is found using a linear equation solution.

The results for this calculation, presented in Figure 204(i), show that this method is completely satisfactory, for this problem. Note that the largest stepsize used is $\pi$ , so that only a single step is taken.

# Exercises 20

20.1 On a copy of Figure 200(i), plot the points corresponding to the solution computed by the Euler method with $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 4 } } \end{array}$ , $\textstyle h = { \frac { 1 } { 5 } }$ .

20.2 Write the initial value problem (200b) in the form

$$
\begin{array} { l l } { { \frac { d x } { d t } \ = \ 1 + x , \qquad } } & { { x ( 0 ) \ = \ 0 , } } \\ { { \frac { d y } { d t } \ = \ y - 2 x y ^ { 2 } , \qquad } } & { { y ( 0 ) \ = \ \frac 1 2 . } } \end{array}
$$

Using this alternative formulation, recalculate the solution, using five equal steps of the Euler method, from $t = 0$ to $t = \ln 2$ . Plot the solution points after each step on a graph in the $( x , y )$ plane.

20.3 Continue the calculations in Table 201(I) to the point $x = 1$ .

20.4 It is known that $E = \textstyle { \frac { 1 } { 2 } } ( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } ) - 1 / { \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } }$ , the total energy, and $A = y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 }$ , the angular momentum, are invariants of the system (201d); that is, for any value of $x$ the values of each of these will be equal respectively to the values they had at the initial time. The quality of a numerical method for solving this problem can be measured by calculating by how much these theoretical invariants actually change in the numerical computation. Repeat the calculations in Tables 201(II), 201(III) and 201(IV) but with the deviation in the values of each of these quantities used in place of the errors.

# 21 Analysis of the Euler Method

210 Formulation of the Euler method

Consider a differential equation system

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : [ a , b ] \times \mathbb { R } ^ { N }  \mathbb { R } ^ { N }$ is continuous and satisfies a Lipschitz condition $\| f ( x , y ) - f ( x , z ) \| \leq L \| y - z \|$ , for all $x$ in a neighbourhood of $x _ { 0 }$ and $y$ and $z$ in a neighbourhood of $y _ { 0 }$ . For simplicity, we assume that the Lipschitz condition holds everywhere; this is not a serious loss of generality because the existence and uniqueness of a solution to (210a) is known to hold in a suitable interval, containing $x _ { 0 }$ , and we can extend the region where a Lipschitz condition holds to the entire $N$ -dimensional vector space, secure in the knowledge that no practical difference will arise, because the solution will never extend beyond values in some compact set.

We assume that the solution to (210a) is required to be approximated at a point $\scriptstyle { \overline { { x } } }$ , and that a number of intermediate step points are selected. Denote these by $x _ { 1 }$ , $x _ { 2 }$ , . . . , $x _ { n } = { \overline { { x } } }$ . Define a function, $\widetilde { y }$ , on $[ x _ { 0 } , { \overline { { x } } } ]$ by the formula

$$
\begin{array} { r } { \widetilde { y } ( \boldsymbol { x } ) = \widetilde { y } ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , \widetilde { y } ( x _ { k - 1 } ) ) , \boldsymbol { x } \in ( x _ { k - 1 } , \boldsymbol { x } _ { k } ] , } \end{array}
$$

for $k = 1 , 2 , \ldots , n$ . If we assume that $\widetilde { y } ( x _ { 0 } ) = y ( x _ { 0 } ) = y _ { 0 }$ , then $\widetilde { y }$ exactly agrees with the function computed using the Euler method at the points $x = x _ { k }$ , $k = 1 , 2 , \ldots , n$ . The continuous function $\widetilde { y }$ , on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ , is a piecewise linear interpolant of this Euler approximation.

We are interested in the quality of $\widetilde { y }$ as an approximation to $y$ . This will clearly depend on the values of the step points $x _ { 1 }$ , $x _ { 2 }$ , $\cdot \cdot \cdot$ , and especially on the greatest of the distances between a point and the one preceding it. Denote the maximum of $x _ { 1 } - x _ { 0 }$ , $x _ { 2 } - x _ { 1 }$ , $\cdot \cdot \cdot$ , $x _ { n } - x _ { n - 1 }$ by $H$ .

We would like to know what happens to $\| \widetilde { y } ( \overline { { x } } ) - y ( \overline { { x } } ) \|$ as $H  0$ , given also that $\lVert \widetilde { \boldsymbol { y } } ( \boldsymbol { x } _ { 0 } ) - \boldsymbol { y } ( \boldsymbol { x } _ { 0 } ) \rVert  0 .$ . It is also interesting to know what happens to the uniform norm of $\| \widetilde { \boldsymbol { y } } ( \boldsymbol { x } ) - \boldsymbol { y } ( \boldsymbol { x } ) \|$ , for $x$ in $[ x _ { 0 } , { \overline { { x } } } ]$ . Under very general conditions, we show that $\widetilde { y }$ converges uniformly to $y$ , as the mesh is refined in this way.

# 211 Local truncation error

In a single step of the Euler method, the computed result, $y _ { 0 } + h f ( x _ { 0 } , y _ { 0 } )$ , differs from the exact answer by

$$
y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h f ( x _ { 0 } , y ( x _ { 0 } ) ) = y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h y ^ { \prime } ( x _ { 0 } ) .
$$

Assuming $y$ has continuous first and second derivatives, this can be written in the form

$$
h ^ { 2 } \int _ { 0 } ^ { 1 } ( 1 - s ) y ^ { \prime \prime } ( x _ { 0 } + h s ) d s .
$$

For $i ~ = ~ 1 , 2 , \ldots , N$ , component $i$ can be written, using the mean value theorem, as ${ \scriptstyle { \frac { 1 } { 2 } } } h ^ { 2 }$ times component $i$ of $y ^ { \prime \prime } ( x _ { 0 } + h s ^ { * } )$ , where $s ^ { * }$ is in the interval $( 0 , 1 )$ . Another way of writing the error, assuming that third derivatives also exist and are bounded, is

$$
{ \frac { 1 } { 2 } } h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) + { \cal O } ( h ^ { 3 } ) .
$$

This form of the error estimate is quite convenient for interpreting numerically produced results, because if $h$ is sufficiently small, the local error will appear to behave like a constant vector multiplied by $h ^ { 2 }$ . It is also useful for determining how stepsize control should be managed.

# 212 Global truncation error

After many steps of the Euler method, the errors generated in these steps will accumulate and reinforce each other in a complicated manner. It is important to understand how this happens. We assume a uniform bound $h ^ { 2 } m$ on the norm of the local truncation error committed in any step of length $h$ . We aim to find a global error bound using a difference inequality. We make the standard assumption that a Lipschitz condition holds, and we write $L$ as the Lipschitz constant.

Recall that $\widetilde y ( x )$ denotes the computed solution on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ . That is, at step values $x _ { 0 }$ , $x _ { 1 }$ , . . . , $x _ { n } ~ = ~ { \overline { { x } } }$ , $\widetilde { y }$ is computed using the equation $\widetilde { y } ( x _ { k } ) = y _ { k } = y _ { k - 1 } + ( x _ { k } - x _ { k - 1 } ) f ( x _ { k - 1 } , y _ { k - 1 } )$ . For ‘off-step’ points, $\widetilde y ( x )$ is defined by linear interpolation; or, what is equivalent, $\widetilde y ( x )$ is evaluated using a partial step from the most recently computed step value. That is, if $x \in ( x _ { k - 1 } , x _ { k } )$ , then

$$
\widetilde { y } ( x ) = y _ { k - 1 } + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , y _ { k - 1 } ) .
$$

Let $\alpha ( x )$ and $\beta ( x )$ denote the errors in $\widetilde y ( x )$ , as an approximation to $y ( x )$ , and in $f ( x , \widetilde { y } ( x ) )$ , as an approximation to $y ^ { \prime } ( x )$ , respectively. That is,

$$
\begin{array} { l } { \alpha ( x ) = y ( x ) - \widetilde { y } ( x ) , } \\ { \beta ( x ) = f ( x , y ( x ) ) - f ( x , \widetilde { y } ( x ) ) , } \end{array}
$$

so that, by the Lipschitz condition,

$$
\| \beta ( x ) \| \leq L \| \alpha ( x ) \| .
$$

Define $E ( x )$ so that the exact solution satisfies

$$
\begin{array} { r l r } & { } & { y ( x ) = y ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) f ( x _ { k - 1 } , y ( x _ { k - 1 } ) ) + ( x - x _ { k - 1 } ) ^ { 2 } { E } ( x ) , \quad } \\ & { } & { x \in ( x _ { k - 1 } , x _ { k } ] , } \end{array}
$$

and we assume that $\| E ( x ) \| \leq m$

Subtract (212a) from (212e), and use (212b) and (212c), so that

$$
\alpha ( x ) = \alpha ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) \beta ( x _ { k - 1 } ) + ( x - x _ { k - 1 } ) ^ { 2 } E ( x ) .
$$

Hence,

$$
\begin{array} { r l } & { \| \alpha ( x ) \| \leq \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) \| \beta ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) L \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq ( 1 + ( x - x _ { k - 1 } ) L ) \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) ^ { 2 } m } \\ & { \qquad \leq ( 1 + ( x - x _ { k - 1 } ) L ) \| \alpha ( x _ { k - 1 } ) \| + ( x - x _ { k - 1 } ) H m , } \end{array}
$$

where we have used (212d) and assumed that no step has a length greater than $H$ . We distinguish two cases. If $L = 0$ , then it follows that

$$
\| \alpha ( \boldsymbol { x } ) \| \le \| \alpha ( \boldsymbol { x } _ { 0 } ) \| + H m ( \boldsymbol { x } - \boldsymbol { x } _ { 0 } ) ;
$$

and if $L > 0$ , it follows that

$$
\begin{array} { r } { \displaystyle \left( \| \alpha ( x ) \| + \frac { H m } { L } \right) \leq ( 1 + ( x - x _ { k - 1 } ) L ) \left( \| \alpha ( x _ { k - 1 } ) \| + \frac { H m } { L } \right) } \\ { \leq \exp ( ( x - x _ { k - 1 } ) L ) \left( \| \alpha ( x _ { k - 1 } ) \| + \frac { H m } { L } \right) . } \end{array}
$$

Let $\phi ( x ) = \exp ( - ( x - x _ { 0 } ) L ) ( \| \alpha ( x ) \| + H m / L )$ , so that $\phi ( x )$ never increases. Hence,

$$
\| \alpha ( x ) \| \leq \exp ( ( x - x _ { 0 } ) L ) \| \alpha ( x _ { 0 } ) \| + \frac { \exp ( ( x - x _ { 0 } ) L ) - 1 } { L } H m .
$$

Combining the estimates found in the two cases and stating them formally, we have:

Theorem 212A Assuming that $f$ satisfies a Lipschitz condition, with constant $L$ , the global error satisfies the bound

$$
\| y ( x ) - \widetilde { y } ( x ) \| \leq \left\{ \begin{array} { l l } { \| y ( x _ { 0 } ) - \widetilde { y } ( x _ { 0 } ) \| + H m ( x - x _ { 0 } ) , \qquad L = 0 , } \\ { \exp ( ( x - x _ { 0 } ) L ) \| y ( x _ { 0 } ) - \widetilde { y } ( x _ { 0 } ) \| + ( \exp ( ( x - x _ { 0 } ) L ) - 1 ) \frac { H m } { L } , } \\ { \qquad L > 0 . } \end{array} \right.
$$

# 213 Convergence of the Euler method

We consider a sequence of approximations to $y ( { \overline { { x } } } )$ . In each of these approximations, a computation using the Euler method is performed, starting from an approximation to $y ( x _ { 0 } )$ , and taking a sequence of positive steps. Denote approximation number $n$ by $\widetilde { y } _ { n }$ .

The only assumption we will make about $\widetilde { y } _ { n }$ , for each specific value of $n$ , is that the initial error $y ( x _ { 0 } ) - \widetilde { y } _ { n } ( x _ { 0 } )$ is bounded in norm by $K _ { n }$ and that the greatest stepsize is bounded by $H _ { n }$ . It is assumed that, as $n \longrightarrow \infty$ , $H _ { n } \to 0$ and $K _ { n }  0$ . As always, we assume that $f$ satisfies a Lipschitz condition.

Denote by $D _ { n }$ the value of $\| y ( \overline { { x } } ) - \widetilde { y } _ { n } ( \overline { { x } } ) \|$ .

Theorem 213A Under the conditions stated in the above discussion, $D _ { n } \to 0$ as $n \longrightarrow \infty$ .

Proof. This result follows immediately from the bound on accumulated errors given by Theorem 212A. $\sqcup$

The property expressed in this theorem is known as ‘convergence’. In searching for other numerical methods that are suitable for solving initial value problems, attention is usually limited to convergent methods. The reason for this is clear: a non-convergent method is likely to give increasingly meaningless results as greater computational effort is expended through the use of smaller stepsizes.

Because the bound used in the proof of Theorem 213A holds not only for $x = { \overline { { x } } }$ , but also for all $x \in [ x _ { 0 } , { \overline { { x } } } ]$ , we can state a uniform version of this result.

Theorem 213B Under the conditions of Theorem 213A,

$$
\operatorname* { s u p } _ { x \in [ x _ { 0 } , { \overline { { x } } } ] } \| y ( x ) - { \widetilde { y } } _ { n } ( x ) \| \to 0
$$

as $n \longrightarrow \infty$ .

An example of enhanced order for problem (214a)   

<table><tr><td>n</td><td>[Error|</td><td>Ratio</td></tr><tr><td>20</td><td>1130400.0252×10-10</td><td>4.4125</td></tr><tr><td>40</td><td>256178.9889×10-10</td><td>4.1893</td></tr><tr><td>80</td><td>61150.2626×10-10</td><td>4.0904</td></tr><tr><td>160</td><td>14949.6176×10-10</td><td>4.0442</td></tr><tr><td>320</td><td>3696.5967×10-10</td><td>4.0218</td></tr><tr><td>640</td><td>919.1362 × 10-10</td><td>4.0108</td></tr><tr><td>1280</td><td>229.1629 × 10-10</td><td>4.0054</td></tr><tr><td>2560</td><td>57.2134× 10-10</td><td>4.0026</td></tr><tr><td>5120</td><td>14.2941×10-10</td><td>4.0003</td></tr><tr><td>10240</td><td>3.5733×10-10</td><td></td></tr></table>

# 214 Order of convergence

It is interesting to know not only that a numerical result is convergent, but also how quickly it converges. In the case of a constant stepsize $h$ , the bound on the global error given in Theorem 212A is proportional to $h$ . We describe this by saying that the order of the Euler method is (at least) 1.

That the order is exactly 1, and that it is not possible, for a general differential equation, to obtain error behaviour proportional to some higher power of $h$ , can be seen from a simple example. Consider the initial value problem

$$
y ^ { \prime } ( x ) = 2 x , \qquad y ( 0 ) = 0 ,
$$

with exact solution $y ( x ) = x ^ { 2 }$ . If $\overline { { x } } ~ = ~ 1$ , and $n$ steps are performed with stepsize $h = n ^ { - 1 }$ , the computed solution is

$$
h \sum _ { k = 0 } ^ { n - 1 } { \frac { 2 k } { n } } = { \frac { n - 1 } { n } } .
$$

This differs from the exact solution by $1 / n = h$ .

In spite of the fact that the order is only 1, it is possible to obtain higher order behaviour in special specific situations. Consider the initial value problem

$$
y ^ { \prime } ( x ) = - y ( x ) \tan ( x ) - { \frac { 1 } { \cos ( x ) } } , \qquad y ( 0 ) = 1 ,
$$

with solution $y ( x ) = \cos ( x ) - \sin ( x )$ . Because of an exact cancellation of the most significant terms in the error contributions, at different parts of the trajectory, the computed results for this problem are consistent with the order being 2 rather than 1, if the output value is taken as $\overline { { x } } \approx 1 . 2 9 2 6 9 5 7 1 9 3 7 3$ . Note that $\scriptstyle { \overline { { x } } }$ was chosen to be a zero of $\exp ( x ) \cos ( x ) = 1$ . As can be seen from Table 214(I), as the number of steps doubles, the error reduces by a factor approximately equal to $2 ^ { - 2 }$ . This is consistent with second order, rather than first order, behaviour. The errors are also plotted in Figure 214(i).

![](images/19b474494e72d9441d08b8d2cb6b7b913482f958c5221c79f2884158e4269233.jpg)  
Error versus stepsize for problem (214a) at two alternative output points

An analysis of the apparent cancellation of the most significant component of the global truncation error is easy to carry out if we are willing to do the estimation with terms, which decrease rapidly as $h  0$ , omitted from the calculation. A more refined analysis would take these additional terms into account, but would obtain bounds on their effect on the final result. In step $k$ , from a total of $n$ steps, the local truncation error is approximately $- { \textstyle { \frac { 1 } { 2 } } } h ^ { 2 } ( \cos ( x _ { k } ) - \sin ( x _ { k } ) )$ . To find the contribution this error makes to the accumulated error at $x _ { n } = { \overline { { x } } }$ , multiply by the product

$$
{ \big ( } 1 - h \tan ( x _ { n - 1 } ) { \big ) } { \big ( } 1 - h \tan ( x _ { n - 2 } ) { \big ) } \cdots { \big ( } 1 - h \tan ( x _ { k } ) { \big ) } .
$$

We have the approximation

$$
{ \frac { \cos ( x + h ) } { \cos ( x ) } } = \cos ( h ) - \sin ( h ) \tan ( x ) \approx 1 - h \tan ( x ) ,
$$

so that (214b) can be written approximately as

$$
{ \frac { \cos ( x _ { n } ) } { \cos ( x _ { n - 1 } ) } } { \frac { \cos ( x _ { n - 1 } ) } { \cos ( x _ { n - 2 } ) } } \cdot \cdot \cdot { \frac { \cos ( x _ { k + 1 } ) } { \cos ( x _ { k } ) } } = { \frac { \cos ( x _ { n } ) } { \cos ( x _ { k } ) } } .
$$

An example of reduced order for problem (214c)   

<table><tr><td>n</td><td>[Error]</td><td>Ratio</td></tr><tr><td>8</td><td>0.3012018700</td><td>1.4532</td></tr><tr><td>16</td><td>0.2072697687</td><td>1.4376</td></tr><tr><td>32</td><td>0.1441738248</td><td>1.4279</td></tr><tr><td>64</td><td>0.1009724646</td><td>1.4220</td></tr><tr><td>128</td><td>0.0710078789</td><td>1.4186</td></tr><tr><td>256</td><td>0.0500556444</td><td>1.4166</td></tr><tr><td>512</td><td>0.0353341890</td><td>1.4155</td></tr><tr><td>1024</td><td>0.0249615684</td><td>1.4149</td></tr><tr><td>2048</td><td>0.0176414532</td><td></td></tr><tr><td>4096</td><td>0.0124709320</td><td>1.4146</td></tr><tr><td></td><td></td><td>1.4144</td></tr><tr><td>8192</td><td>0.0088169646</td><td>1.4143</td></tr><tr><td>16384 32768</td><td>0.0062340372 0.0044079422</td><td>1.4143</td></tr></table>

Multiply this by the error in step $k$ and add over all steps. The result is

$$
- { \frac { 1 } { 2 } } h ^ { 2 } \cos ( \overline { { x } } ) \sum _ { k = 1 } ^ { n } { \frac { \cos ( x _ { k } ) - \sin ( x _ { k } ) } { \cos ( x _ { k } ) } } ,
$$

which is approximately equal to the integral

$$
- \frac { 1 } { 2 } h \cos ( \overline { x } ) \int _ { 0 } ^ { \overline { x } } \frac { \cos ( x ) - \sin ( x ) } { \cos ( x ) } d x = - \frac { 1 } { 2 } h \cos ( \overline { x } ) ( \overline { x } + \mathrm { l n } \cos ( \overline { x } ) ) .
$$

This vanishes when $\exp ( { \overline { { x } } } ) \cos ( { \overline { { x } } } ) = 1$ .

For comparison, results are also given in Figure 214(i) for a similar sequence of $h$ values, but at the output point $\overline { { x } } = \pi / 4$ . This case is unsurprising, in that it shows typical order 1 behaviour.

Finally, we present a problem for which an order, even as high as $1$ , is not observed. The initial value problem is

$$
y ^ { \prime } ( x ) = - { \frac { x y } { 1 - x ^ { 2 } } } , \qquad y ( 0 ) = 1 ,
$$

with exact solution $y = { \sqrt { 1 - x ^ { 2 } } }$ . The solution is sought at $\overline { { x } } = 1$ and the numerical results are shown in Table 214(II). It is seen that, as the number of steps doubles, the error reduces by a factor of approximately $2 ^ { - 1 / 2 }$ . Thus, the order seems to have been reduced from 1 to $\textstyle { \frac { 1 } { 2 } }$ . The reason for the loss of order for this problem is that the Lipschitz condition does not hold at the end of the trajectory (at $x = 1$ , $y = 0$ ). As for any initial value problem, the error in the approximate solution at this point develops from errors generated at every time step. However, in this case, the local truncation error in the very last step is enough to overwhelm the contributions to the error inherited from all previous steps. In fact the local truncation error for the final step is

![](images/0aa0245d3b7d862b6af9892fa01f524c3f766a68dbae33e01c32c0fb7ee25b16.jpg)  
Error versus stepsize for problem (214c) at two alternative output points

$$
\begin{array} { c } { y ( 1 ) - y ( 1 - h ) - h f ( 1 - h , y ( 1 - h ) ) } \\ { \displaystyle = - \sqrt { 1 - ( 1 - h ) ^ { 2 } } + h ( 1 - h ) \frac { \sqrt { 1 - ( 1 - h ) ^ { 2 } } } { 1 - ( 1 - h ) ^ { 2 } } , } \end{array}
$$

which simplifies to

$$
- { \frac { 1 } { \sqrt { 2 - h } } } h ^ { \frac { 1 } { 2 } } \approx - 2 ^ { - { \frac { 1 } { 2 } } } h ^ { \frac { 1 } { 2 } } .
$$

Thus, the order $\textstyle { \frac { 1 } { 2 } }$ behaviour can be explained just by the error contributed by the last step.

A second computation, for the solution at $\begin{array} { r } { \overline { { x } } = \frac { 1 } { 2 } } \end{array}$ , causes no difficulty and both results are shown in Figure 214(ii).

# 215 Asymptotic error formula

In a numerical approximation to the solution to a differential equation, using the Euler method, contributions to the total error are typically produced in every step. In addition to this, there may be errors introduced at the very start of the integration process, due to an inaccuracy in the numerical initial value. We attempt to model the development of this error using an asymptotic approach. That is, we assume that the magnitude of all contributions to the error are bounded in terms of some small parameter. We consider only the limiting case, as all stepsizes tend to zero. Consider a step which advances the approximate solution from $x$ to $x + h$ . Because the local truncation error in this step is approximately $\scriptstyle { \frac { 1 } { 2 } } y ^ { \prime \prime } ( x ) h ^ { 2 }$ , the rate at which errors are being generated, as $x$ increases, will be approximately $y ^ { \prime \prime } ( x ) h$ .

We suppose that for a step starting at $x$ , the stepsize is equal to $H s ( x )$ , where $0 ~ < ~ s ( x ) ~ \le ~ 1$ throughout the integration. We use $H$ as the small parameter, referred to above, and assume that the initial error is equal to a constant, which we denote by $v _ { 0 }$ , times $H$ . Using the integrated form of the differential equation,

$$
y ( x ) = y ( x _ { 0 } ) + \int _ { x _ { 0 } } ^ { x } f ( x , y ( x ) ) d x ,
$$

we write the perturbation to $y$ , defining the numerical approximation, as $y ( x ) + H v ( x )$ . Thus $y ( x ) + H v ( x )$ is approximately equal to

$$
y ( x ) + H v ( x ) = y ( x _ { 0 } ) + H v _ { 0 } + \int _ { x _ { 0 } } ^ { x } { \Big ( } f ( x , y ( x ) + H v ( x ) ) + { \frac { 1 } { 2 } } H s ( x ) y ^ { \prime \prime } ( x ) { \Big ) } d x
$$

Because $H$ is small, we approximate $f ( x , y ( x ) + H v ( x ) )$ by $f ( x , y ( x ) ) +$ $H ( \partial f / \partial y ) v ( x )$ :

$$
\begin{array} { l } { \displaystyle { y ( x ) + H v ( x ) = y ( x _ { 0 } ) + H v _ { 0 } } } \\ { \displaystyle { \qquad + \int _ { x _ { 0 } } ^ { x } \Big ( f ( x , y ( x ) ) + H \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } H s ( x ) y ^ { \prime \prime } ( x ) \Big ) d x . } } \end{array}
$$

Subtract (215a) from (215b), divide the difference by $H$ , and we find

$$
v ( x ) = v _ { 0 } + \int _ { x _ { 0 } } ^ { x } \left( \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } s ( x ) y ^ { \prime \prime } ( x ) \right) d x ,
$$

so that $v$ satisfies the initial value problem

$$
v ^ { \prime } ( x ) = \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } s ( x ) y ^ { \prime \prime } ( x ) , \quad v ( x _ { 0 } ) = v _ { 0 } .
$$

We use this result in an attempt to understand the contribution to the total error of local errors introduced at various points on the trajectory. This is done by writing $\Phi ( \xi , { \overline { { x } } } )$ for the solution at $\scriptstyle { \overline { { x } } }$ to the differential equation

$$
w ^ { \prime } ( x ) = \frac { \partial f } { \partial y } w ( x ) , \quad w ( \xi ) = I ,
$$

where $w$ takes values in the space of $N \times N$ matrices. In the special case where $\partial f / \partial y$ is a constant matrix $M$ , the solution is

$$
\Phi ( \xi , \overline { { { x } } } ) = \exp ( ( \overline { { { x } } } - \xi ) M ) .
$$

We can now write the solution at $x = { \overline { { x } } }$ of (215c) in the form

$$
v ( \overline { { { x } } } ) = \Phi ( x _ { 0 } , \overline { { { x } } } ) v _ { 0 } + \frac { 1 } { 2 } \int _ { x _ { 0 } } ^ { \overline { { { x } } } } \Phi ( x , \overline { { { x } } } ) s ( x ) y ^ { \prime \prime } ( x ) d x .
$$

This suggests that $s$ should be chosen, as closely as possible, to maintain a constant value of $\| \Phi ( x , \overline { { x } } ) s ( x ) y ^ { \prime \prime } ( x ) \|$ , if the norm of the total error is to be kept low for a given number of steps performed.

# 216 Stability characteristics

In addition to knowing that a numerical method converges to the true solution over a bounded interval, it is interesting to know how errors behave over an unbounded interval. Obtaining quantitative results is difficult, because we are no longer able to take limits, as stepsizes tend to zero. Hence, our attention will move towards qualitative questions, such as whether or not a computed result remains bounded. By comparing the answer to questions like this with the known behaviour of the exact solution, we obtain further insight into the appropriateness of the numerical approximation to model the differential equation.

A further reason for carrying out this type of qualitative analysis is that so-called ‘stiff problems’ frequently arise in practice. For such problems, qualitative or ‘stability’ analysis is vital in assessing the fitness of the method to be used in the numerical solution.

Because of the great complexity of this type of analysis, we need to restrict ourselves to purely linear problems with constant coefficients. Thus, we could consider a system of differential equations of the form

$$
y ^ { \prime } ( x ) = M y ( x ) ,
$$

with the matrix $M$ constant. Using fixed stepsize $h$ , the Euler method gives as the approximate solution at $x _ { n } = x _ { 0 } + n h$ ,

$$
y _ { n } = ( I + h M ) y _ { n - 1 } ,
$$

leading to the numerical solution

$$
y _ { n } = ( I + h M ) ^ { n } y _ { 0 } .
$$

For this problem, the exact solution is

$$
y ( x _ { n } ) = \exp ( n h M ) y ( x _ { 0 } ) .
$$

We wish to examine some features of the approximate solution (216b) by comparing these features with corresponding features of the exact solution (216c).

By making a change of basis, so that $y ( x ) = S { \widehat { y } } ( x )$ , and $y _ { n } = S { \widehat { y } } _ { n }$ , where $S$ is a constant non-singular matrix, we can rewrite the differential equation in the form

$$
{ \widehat { y } } ^ { \prime } ( x ) = { \widehat { M } } { \widehat { y } } ( x ) ,
$$

where $\widehat { M } = S ^ { - 1 } M S$ . The solution is

$$
\widehat { y } ( x _ { n } ) = \exp ( n h \widehat { M } ) \widehat { y } ( x _ { 0 } ) .
$$

The solution computed by the Euler method transforms to

$$
\widehat { y } _ { n } = ( I + h \widehat { M } ) ^ { n } \widehat { y } _ { 0 } .
$$

If the transformed matrix $\widehat { M }$ is chosen as the Jordan canonical form of $M$ , then the differential equation system (216d) and the numerical approximation become, to some extent, decoupled. This means that, for each distinct eigenvalue $q$ , one of the equations in the system (216d) has the simple form

$$
y ^ { \prime } ( x ) = q y ( x ) ,
$$

and other components that correspond to the same Jordan block will depend on this solution, but will not contribute to its behaviour.

Hence, to obtain acceptable behaviour, for the type of linear problem given by (216a), it is essential that we obtain acceptable behaviour for (216e). All this will mean is that $( 1 + h q ) ^ { n }$ will be an acceptable approximation to $\exp ( n h q )$ . At very least, we want bounded behaviour for $( 1 + h q ) ^ { n }$ , as $n \longrightarrow \infty$ , whenever $\exp ( n h q )$ is bounded. This, in turn, implies that $| 1 + h q |$ is bounded by $1$ , if $\mathrm { R e } q \le 0$ and $q$ is an eigenvalue of $M$ . Because any analysis of this type will involve the product of $h$ and $q$ , it is convenient to write this product as $z = h q$ . We allow the possibility that $z$ is complex, because there is no reason for $M$ to have only real eigenvalues.

The set of points in the complex plane, in which $z$ may lie for this stable behaviour, is known as the ‘stability region’. Because it is the set for which $| 1 + z | \le 1$ , this stability region is the disc with centre at $^ { - 1 }$ and radius $^ { 1 }$ . This is shown as the unshaded region in Figure 216(i). By contrast, we can find the stability region of the implicit Euler method by replacing $h f ( x _ { n } , y _ { n } )$ by $z y _ { n }$ in the formula defining this method. That is, $y _ { n } = y _ { n - 1 } + h f ( x _ { n } , y _ { n } )$ becomes

$$
y _ { n } = y _ { n - 1 } + z y _ { n } .
$$

Hence, $y _ { n } = ( 1 - z ) ^ { - 1 } y _ { n - 1 }$ , and the sequence formed by this relation is bounded if and only if $| 1 - z | \geq 1$ . This is the complement in the complex plane of the interior of the disc with centre $^ { 1 }$ and radius $^ { 1 }$ , shown as the unshaded region of Figure 216(ii).

![](images/30ca22b8a24076d1d50d7bddea3249bcb89b9fd057c8bc9588fbd88e8fe64493.jpg)  
Stability region: Euler method

![](images/b3e2a7e70023ec0a4266136d2ddd9db811ab52159672f24cbc5486d6002edd61.jpg)  
Stability region: implicit Euler method

Even if we cannot obtain accurate approximations to the solution to equations like (216e), we frequently wish to guarantee that the numerical approximation is bounded in cases when the exact solution is bounded. This means that we are especially interested in numerical methods, for which the stability region includes all of the left half-plane. This is the case for the implicit Euler method (Figure 216(ii)) but, as we clearly see from Figure 216(i), not for the Euler method itself. Methods with this desirable property are said to be ‘A-stable’. It is widely accepted that this property is close to being essential for stiff problems.

For these two one-step methods, the ratio $y _ { n } / y _ { n - 1 }$ is known as the ‘stability function’. Denote this by $R ( z )$ so that

$$
R ( z ) = \left\{ \begin{array} { l l } { 1 + z , \qquad } & { \mathrm { ( E u l e r ~ m e t h o d ) } } \\ { \displaystyle \frac { 1 } { 1 - z } . \qquad } & { \mathrm { ( i m p l i c i t ~ E u l e r ~ m e t h o d ) } } \end{array} \right.
$$

From a consideration of elementary complex analysis, the property of Astability can be expressed slightly differently. Obviously, for a method to be A-stable, the stability function must have no poles in the left half-plane. Also the magnitude $| R ( z ) |$ must be bounded by $1$ , for $z$ on the imaginary axis.

![](images/dd51a820ae8540723fe9dbc338733700eb600354cb7eea6d4c7ec804fb80a030.jpg)  
Order star: Euler method

![](images/1ccb7d15bc1123a7c3b02ba693c9b1482024f4fcee7eaa627bc14e901a61282c.jpg)  
Order star: implicit Euler method

The interesting thing is that these two conditions are also sufficient for Astability. If a method with these properties were not A-stable, then this would be contrary to the maximum modulus principle.

Multiplying $R ( z )$ by $\exp ( - z )$ should make no difference to these conclusions. That is, if the set in the complex plane for which $| R ( z ) \exp ( - z ) | \leq 1$ is plotted instead, A-stability can still be categorized by this set, including the imaginary axis, together with there being no poles in the left half-plane. The reason for this assertion is that the factor $\exp ( - z )$ does not add to, or take away from, the set of poles. Furthermore, its magnitude is precisely 1 when the real part of $z$ is zero.

The modified plots for the two methods are shown in Figures 216(iii) and 216(iv). These were named ‘order stars’ by their inventors, Wanner, Hairer and Nørsett (1978). The important new feature, introduced by the insertion of the exponential factor, is the pattern that has appeared near zero. Because, for each of these methods, $R ( z ) \exp ( - z ) = 1 + C z ^ { 2 } + O ( z ^ { 3 } )$ , the magnitude of this will be greater than, equal to, or less than $^ { 1 }$ for $| z |$ small, approximately when the real part of $C z ^ { 2 }$ is positive, zero or negative, respectively. The regions adjoining zero for which $\mathrm { R e } ( R ( z ) \exp ( - z ) ) > 0$ are known as ‘fingers’, and those for which $\mathrm { R e } ( R ( z ) \exp ( - z ) ) < 0$ , are ‘dual fingers’. The bounded fingers necessarily contain poles and the bounded dual fingers necessarily contain zeros. For both the Euler method and the implicit Euler method, there is an exact pairing between zeros and bounded dual fingers, and between poles and bounded fingers. Since this pairing also generalizes to other large classes of methods, specifically those methods for which the order is maximal, given the degrees of the numerator and denominator in the stability function, it is possible to relate the angles, at which fingers come out from zero, to the positions of the poles. It will be shown in Subsection 354 how this can be used to determine the possible A-stability of specific methods, and classes of methods.

![](images/62c1d0a3b94f88f68e17291e3390c6dbfd290e51f8fe959a34454802b5a36235.jpg)  
Order arrows: Euler method

![](images/8b5aa3e0a73b71ba05e95ebc19ea0e0d7283180d81aef66339f8db7a438e77a4.jpg)  
Order arrows: implicit Euler method

Although less well known, order arrows have a role similar to that of order stars, in the analysis of stability questions. For a given stability function $R ( z )$ , we plot the paths in the complex plane where $w ( z ) = \exp ( - z ) R ( z )$ is real and positive. Arrows are attached to the paths to show the direction of increasing $w$ . For the Euler and implicit Euler methods, order arrow diagrams are shown in Figures 216(v) and 216(vi) respectively.

# 217 Local truncation error estimation

We recall from Subsection 202 that stepsize control based on a local error estimate was useful in forcing the Euler method to devote computational effort to those parts of the trajectory where it is most needed. We discuss here the principles behind this idea.

Let $y _ { 1 }$ , $y _ { 2 }$ , . . . , $y _ { n - 1 }$ , $y _ { n }$ , . . . denote a sequence of approximations to the solution to an initial value problem, computed using the Euler method. For our present purposes, we can assume that the stepsize takes a constant value $h$ , since we are discussing the estimation of the local truncation error only over a single interval. Because we are considering the local error, we treat the incoming approximation for step $n$ as though it were exact. That is, we introduce a solution $\hat { y }$ to the initial value problem

$$
\widehat { y } ^ { \prime } ( x ) = f ( x , \widehat { y } ( x ) ) , \qquad \widehat { y } ( x _ { n - 1 } ) = y _ { n - 1 } .
$$

We can then interpret ${ \widehat { y } } ( x _ { n } ) - y _ { n }$ as the error introduced in step $n$ alone.

Although it is not feasible to obtain convenient and useful bounds on this quantity, it is possible to obtain asymptotically correct approximations without additional cost. These will often be useful for the purpose of controlling the stepsize, to produce efficient numerical algorithms, although they cannot be used to obtain rigorous error bounds.

An approximation for ${ \widehat { y } } ( x _ { n } )$ , to within $O ( h ^ { 3 } )$ , is found using a truncated Taylor series

$$
\widehat { y } ( x _ { n - 1 } + h ) \approx \widehat { y } ( x _ { n - 1 } ) + h \widehat { y } ^ { \prime } ( x _ { n - 1 } ) + \frac { h ^ { 2 } } { 2 ! } \widehat { y } ^ { \prime \prime } ( x _ { n - 1 } ) ,
$$

and the first two terms are

$$
{ \widehat { y } } ( x _ { n - 1 } ) + h { \widehat { y } } ^ { \prime } ( x _ { n - 1 } ) = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) = y _ { n } .
$$

Hence, we see that the truncation error is approximately

$$
\frac { h ^ { 2 } } { 2 ! } \widehat { y } ^ { \prime \prime } ( x _ { n - 1 } ) .
$$

An alternative interpretation of this quantity, at least asymptotically, with terms involving third and higher powers of $h$ ignored, is as the difference

between the result computed by the Euler method and a result computed, at least for the current step, using a method which has a higher order.

As we will see in Section 22, there are many ways in which such a higher order method can be found. One method is to evaluate $h f ( x _ { n } , y _ { n } )$ , and to recompute the step as

$$
y _ { n - 1 } + { \frac { 1 } { 2 } } { \Big ( } h f ( x _ { n } , y _ { n } ) + h f ( x _ { n - 1 } , y _ { n - 1 } ) { \Big ) } .
$$

If we were intending to actually use this more accurate approximation, then the second computation of the function $f$ in each step would approximately double the work that needs to be done to complete each step. However, all we intend to do is to estimate the error and, for this reason, the cost is unchanged, because we need the value of $h f ( x _ { n } , y _ { n } )$ to proceed to the next step in any case.

Thus, we see that a convenient, and essentially cost-free, method for estimating local truncation errors is as the difference of the result found by the Euler method itself, and the result found from (217a). This leads to the error estimate

$$
{ \frac { 1 } { 2 } } { \Big ( } h f ( x _ { n } , y _ { n } ) - h f ( x _ { n - 1 } , y _ { n - 1 } ) { \Big ) } .
$$

We already know this estimate can be used, quite satisfactorily, to control stepsize, because of its evident success in Subsection 202.

# 218 Rounding error

The mathematical analysis of the behaviour of a numerical method, such as the Euler method, is usually idealized to exact arithmetic. However, in practical computation, the nature of computer arithmetic can play a significant, and possibly overwhelming, part. Thus the discussion of error growth, given in Subsection 212, is deficient in this respect. Let $\alpha _ { n }$ denote the total error in the result, computed at step $n$ , and $\beta _ { n }$ the corresponding error in the derivative, computed at this step. Thus,

$$
\begin{array} { l } { \alpha _ { n } = y ( x _ { n } ) - y _ { n } , } \\ { \beta _ { n } = f ( x _ { n } , y ( x _ { n } ) ) - f ( x _ { n } , y _ { n } ) . } \end{array}
$$

The sequences of exact and approximate values are interrelated by

$$
\begin{array} { c } { { y _ { n } = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) - r _ { n } , } } \\ { { y ( x _ { n } ) = y ( x _ { n - 1 } ) + h f ( x _ { n - 1 } , y ( x _ { n - 1 } ) ) + l _ { n } , } } \end{array}
$$

where $r _ { n }$ is the rounding error, otherwise known as the round-off error, committed in this step, and $l _ { n }$ is the truncation error that we have already discussed.

![](images/52580f2b56f66bc5b51ce7203fa0b4edfacc83f9dee48f6b5e13c783af2c35a9.jpg)  
Schema showing effects of rounding error

These lead to the difference equation

$$
\alpha _ { n } = \alpha _ { n - 1 } + h \beta _ { n - 1 } + l _ { n } + r _ { n } .
$$

Even though we know something about $l _ { n }$ , in particular that it behaves asymptotically like a constant times $h ^ { 2 }$ , very little is known about $r _ { n }$ .

A somewhat pessimistic model of rounding error would bound its magnitude in terms of the magnitude of $y _ { n }$ . It would also assume that its sign (or direction, in the high-dimensional case) is always such as to reinforce errors already accumulated. Bounding the magnitude of the rounding error, in terms of the magnitude of $y _ { n }$ , is quite reasonable, because the greatest contribution to the total rounding error will usually arise from the final addition of $h f ( x _ { n - 1 } , y _ { n - 1 } )$ to $y _ { n - 1 }$ . Of these two terms, $y _ { n - 1 }$ is usually far the greater in magnitude. Thus, the rounding error will have a magnitude approximately equal to $\| y _ { n - 1 } \| \epsilon \approx | | y _ { n } | | \epsilon$ , where $\epsilon$ is the machine round-off constant defined as the smallest positive number which satisfies the inequality $1 + \epsilon > 1$ , in computer arithmetic.

The other aspect of this model, that rounding errors always conspire to produce the worst possible outcome, is, of course, too severe an assumption. An alternative is to treat the rounding errors arising in different steps as being independently and randomly distributed.

The pessimistic assumption adds an additional term to the accumulated error of $C h ^ { - 1 }$ , for $C$ a constant, because the local error will be more or less the same in each step and the number of steps is inversely proportional to $h$ . The randomness assumption will lead to the rounding error contribution being replaced by a term of the form $C h ^ { - 1 / 2 }$ . A detailed analysis of the probabilistic model of rounding error in initial value problem calculations is presented in Henrici (1962).

Under either the deterministic or the probabilistic model, it is clear that the conclusion of the convergence of computed solutions to the exact solution, as the stepsize tends to zero, will have to be reconsidered. If truncation error alone was significant, the error behaviour would be very much as shown by the dashed line in Figure 218(i). On the other hand, if there were no appreciable

# α Simple version of Euler

<table><tr><td>for i = 1:n</td></tr><tr><td></td></tr><tr><td>term = h*f(y);</td></tr><tr><td></td></tr><tr><td>y = y + term; end</td></tr></table>

β Sophisticated version of Euler using compensated summation truncation error, the accumulated rounding error would be very much like the dotted line. The solid line shows the combined effect of these two sources of error. Since a logarithmic scale is used for both stepsize and error, the two individual error components will be approximately straight lines whose slope will depend on the order of the method, one in the case of Euler, and whether the pessimistic or the probabilistic model of rounding error growth is assumed.

<table><tr><td>Z = zeros(size(y));</td><td></td></tr><tr><td>for i = 1:n</td><td></td></tr><tr><td>term = h*f(y)+ Z;</td><td></td></tr><tr><td>newy = y + term;</td><td></td></tr><tr><td>Z = term - (newy - y);</td><td></td></tr><tr><td>y = newy;</td><td></td></tr><tr><td>end</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

Rather than attempting to carry out this analysis, we remark that it is possible, to a large extent, to overcome the worst effects of the accumulation of rounding errors, as steps are computed in sequence. This is done by estimating the value of $r _ { n }$ in any particular step, and then adding this to the value of $h f ( x _ { n } , y _ { n } )$ , before this is added in the following step. This improved technique, which can be used for many situations involving the summation of a large number of small numbers, is sometimes known as the Gill–Møller algorithm (Gill, 1951; Møller, 1965, 1965a), but is now more often referred to as ‘compensated summation’. An analysis, in the context of floating point arithmetic, was carried out by Kahan (1965) and particular applications to initial value problems were considered in Vitasek (1969). A modern survey of compensated summation, with further references, is available in Higham (1993).

We show how this is done by presenting two fragments of MATLAB code, of which the first, referred to as Algorithm $2 1 8 \alpha$ , computes the solution naively, and the second, Algorithm $2 1 8 \beta$ , makes the improvement that we have referred to. In each case, the problem is assumed to be written in autonomous form; this is convenient because, if it were not the case, the updating of the $\mathbf { x }$ variable would need to be done in a similar way to the y variable. It is assumed that the statement f(y) yields the value of the derivative vector for given y.

![](images/6684464ee5f54006d07a9e530b3cd94d3d26d9b0bfd8ecdfdd314d70958c1298.jpg)  
Errors for naive (◦) and sophisticated ( $\bullet$ ) forms of the Euler method

Although each of these algorithms is coded to work in a vector setting, it will be adequate, for illustrative purposes, to confine ourselves to numerical experiments with a scalar problem. Specifically, we use the problem given by (201a), using a sequence of stepsizes, $h = 2 ^ { - 2 }$ , $h = 2 ^ { - 3 }$ , $\cdot \cdot \cdot$ , $h = 2 ^ { - 2 4 }$ . Each of the two algorithms was used, and the errors were plotted on the same graph, which is presented in Figure 218(ii). To avoid the necessity of using abnormally small stepsizes, before rounding error becomes significant, the calculations were performed in an arithmetic system in which it was possible to force an accuracy of only nine significant decimal digits. It is seen that the naive form of the method produces results that are increasingly infected by rounding for stepsizes less than $2 ^ { - 1 5 }$ . For the Gill–Møller (compensated summation) algorithm, on the other hand, there is no sign of accumulated rounding error at all. It can also be seen that the naive version of the method gives results much as was anticipated in Figure 218(i).

To give additional insight into how compensated summation works, a further calculation on the initial value problem (201a) was performed, using modified arithmetic in which the computations were consistently rounded to three significant decimal digits. Using the notation in Algorithm $2 1 8 \beta$ , these results are shown in Table 218(I) for the first ten steps, using stepsize 0.01. The crucial step in the calculation, the evaluation of $_ { \textrm { z } }$ , can be expected to be performed with little or no error. The reason for this is that each of the two subtractions, newy - y and term - (newy - y), has operands which are close to being equal, and these subtractions are usually performed without rounding error. Exceptions may occur when two operands are almost equal, but where the exponent parts of the floating point representations differ by one; but this situation will be relatively rare. If we also concede that the errors generated in the addition of two small quantities, in the statement term $=$ $\mathtt { h * f } \left( \mathtt { y } \right) ~ + ~ z$ , are not of great significance, then we see that, although y might not be accurate as an approximation to y at the end of a step, the value of y $+ \ z$ , if it could be evaluated accurately, would be a very good approximation, because the statement term - (newy - y) effectively increases the old value of $\texttt { y + z }$ by $\mathtt { h } * \mathtt { f } \left( \mathtt { y } \right)$ , to form the new value of $\texttt { y + z }$ .

Ten steps of sophisticated Euler to three significant decimals   

<table><tr><td>X</td><td>y</td><td>h*f(y)</td><td>term</td><td>newy</td><td>Z</td></tr><tr><td>0.00</td><td>1.00</td><td>0.0100</td><td>0.0100</td><td>1.01</td><td>0.0000</td></tr><tr><td>0.01</td><td>1.01</td><td>0.0102</td><td>0.0102</td><td>1.02</td><td>0.0002</td></tr><tr><td>0.02</td><td>1.02</td><td>0.0104</td><td>0.0106</td><td>1.03</td><td>0.0006</td></tr><tr><td>0.03</td><td>1.03</td><td>0.0106</td><td>0.0112</td><td>1.04</td><td>0.0012</td></tr><tr><td>0.04</td><td>1.04</td><td>0.0108</td><td>0.0120</td><td>1.05</td><td>0.0020</td></tr><tr><td>0.05</td><td>1.05</td><td>0.0110</td><td>0.0130</td><td>1.06</td><td>0.0030</td></tr><tr><td>0.06</td><td>1.06</td><td>0.0112</td><td>0.0142</td><td>1.07</td><td>0.0042</td></tr><tr><td>0.07</td><td>1.07</td><td>0.0114</td><td>0.0156</td><td>1.09</td><td>-0.0044</td></tr><tr><td>0.08</td><td>1.09</td><td>0.0116</td><td>0.0072</td><td>1.10</td><td>-0.0028</td></tr><tr><td>0.09</td><td>1.10</td><td>0.0118</td><td>0.0090</td><td>1.11</td><td>-0.0010</td></tr><tr><td>0.10</td><td>1.11</td><td></td><td></td><td></td><td></td></tr></table>

As further evidence in support of the use of compensated summation, we present the results of an extended calculation, with the same three decimal arithmetic system used to produce Table 218(I). In this calculation, 100 steps were taken, so that the numerical approximations are now extended to the interval $[ 0 , 1 ]$ . Shown in Figure 218(iii) are the computed values of y, found using each of Algorithms $2 1 8 \alpha$ and $2 1 8 \beta$ . In each case a rounding-free version of the same results was subtracted to isolate the error due to rounding alone. The sum of y and $_ { \textrm { z } }$ , for the sophisticated algorithm, is also given. Because the values of these quantities vary widely, a scale is used for which a value $\epsilon$ corresponds to a rounding error of $\epsilon \exp ( 1 0 ^ { 4 } | \epsilon | )$ . It is clear that, in this example, the sophisticated version of Euler performs overwhelmingly better than the crude version.

# Exercises 21

21.1 For the differential equation $y ^ { \prime } = y$ , $y ( 0 ) = 1$ , find the function $\widetilde { y }$ , given by (212a), where $n = 4$ and $[ x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ] = [ 0 , { \scriptstyle { \frac { 1 } { 4 } } } , { \scriptstyle { \frac { 1 } { 2 } } } , { \scriptstyle { \frac { 3 } { 4 } } } , 1 ]$  and $\widetilde y ( 0 ) = y ( 0 )$ .

21.2 For the same problem as in Exercise 21.1, but with $n$ an arbitrary positive integer and $x _ { k } ~ = ~ k / n$ , for $k = 0 , 1 , 2 , \ldots , n$ , find the value of $\widetilde { y } ( 1 ) - y ( 1 )$ and show that this converges to $0$ as $n \longrightarrow \infty$ .

![](images/2796455e5c95609983dd999621d1cbf3dc3267451a92806a518806cf91798f27.jpg)  
Accumulation of rounding errors in low accuracy calculations with sophisticated Euler, showing y (dashed line) and y $+ z$ (solid line); also, for comparison, crude Euler (dotted line)

21.3 Prove (211a), using integration by parts.

21.4 Assuming that $L = 0$ , prove (212f), using induction on $k$

21.5 Repeat the calculation in Subsection 218, but making the correction in the Gill–Møller algorithm only every second step.

# 22 Generalizations of the Euler Method

# 220 Introduction

As we have seen, in our discussion of the Euler method in Sections 20 and 21, this simplest of all numerical methods enjoys many desirable properties but, at the same time, suffers from some limitations. In the present section, we consider generalizations, which will yield improved numerical behaviour but will retain, as much as possible, its characteristic property of simplicity.

An important aim will be to obtain methods for which the asymptotic errors behave like high powers of the stepsize $h$ . For such methods, the gain in accuracy, resulting from a given reduction in stepsize, would be greater than for the Euler method, because for this method, the error behaves only like the first power of $h$ . We also examine the stability characteristics of these various more general methods. As we saw in Subsection 216, the Euler method does

Errors in the numerical solution of the orbital problem (201d) with zero eccentricity through a half period using (221a) and (221b)

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y1 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y2 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.014790210.003727810.000922330.000228520.000056820.00001416</td><td rowspan=1 colspan=1>3.96764.04174.03614.02194.0119</td><td rowspan=1 colspan=1>-0.04016858-0.01012098-0.00253020-0.00063190-0.00015785-0.00003945</td><td rowspan=1 colspan=1>3.96884.00014.00414.00314.0018</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y3 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y4 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.040386360.010225250.002547930.000634400.000158180.00003949</td><td rowspan=1 colspan=1>3.94974.01324.01634.01054.0059</td><td rowspan=1 colspan=1>-0.01548159-0.00372585-0.00091636-0.00022742-0.00005666-0.00001414</td><td rowspan=1 colspan=1>4.15524.06594.02944.01384.0067</td></tr></table>

not work well for stiff problems, because of stability considerations. We would like to find methods that have better stability.

The two major aims, greater accuracy and better stability, have to be balanced against the need to avoid additional computational costs, associated for example, with starting and stepsize-changing mechanisms. In the next few subsections, we explore some of the approaches used to achieve these aims.

# 221 More computations in a step

Instead of computing $f$ only once in each time step, as in the Euler method, we might look for methods which evaluate $f$ (with different arguments, of course) two or more times. We consider a single example of this idea in which $f$ is evaluated twice.

Since the Euler method is based on a left-hand quadrature rule, we might ask how it is possible to base a method on the trapezoidal rule. The difficulty with this is that the derivative at the beginning of the step is known, but at the end it is not known. To overcome this difficulty, one of the two $f$ evaluations can be used to approximate the solution value at the end of the step, using the same approximation that is used in the Euler method. From this first order approximation, an approximation to the derivative at the end of the step is computed. The quota of two $f$ evaluations has now been exhausted, but there is now data available to apply the trapezoidal rule formula.

Putting all these stages of the computation together, we write the algorithm for computing $y _ { n }$ in the form

$$
\begin{array} { l } { { \displaystyle y _ { n } ^ { * } = y _ { n - 1 } + h f \big ( x _ { n - 1 } , y _ { n - 1 } \big ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + \frac { h } { 2 } \big ( f \big ( x _ { n } , y _ { n } ^ { * } \big ) + f \big ( x _ { n - 1 } , y _ { n - 1 } \big ) \big ) . } } \end{array}
$$

This is an example of a Runge–Kutta method.

As an example of the use of this method, refer to Table 221(I), where the Kepler problem (201d), with zero eccentricity, is integrated through a half period. The number of steps, $n$ , takes on successive values $2 ^ { i }$ , $i = 5 , 6 , \ldots , 1 0$ , so that $h$ takes on values $\pi 2 ^ { - i }$ , $i = 5 , 6 , \ldots , 1 0$ , respectively. The second order nature of the approximations is suggested by the rate at which errors decrease in each of the four components, as $n$ is repeatedly doubled.

# 222 Greater dependence on previous values

After the first step of a numerical method has been completed, approximations are available, to be used in the computation of $y _ { n }$ , not only for $y ( x _ { n - 1 } )$ and $y ^ { \prime } ( x _ { n - 1 } )$ but also for $y ( x _ { n - 2 } )$ and $y ^ { \prime } ( x _ { n - 2 } )$ . After further steps, even more previous information is available. Instead of computing $y _ { n }$ in a complicated manner from just the value of $y _ { n - 1 }$ , we could consider making more use of the values computed in past steps, as they become available.

In the generalization of the Euler method, introduced in Subsection 221, we were, in effect, using an approximation to the derivative not at $x _ { n - 1 }$ , but at $x _ { n - \frac { 1 } { 2 } } ~ = ~ x _ { n - 1 } + \frac { 1 } { 2 } h$ . One way of doing a similar adjustment, but using past information, is to note that existing data indicates that the value of $y ^ { \prime } ( x )$ is changing by about $f ( x _ { n - 1 } , y _ { n - 1 } ) - f ( x _ { n - 2 } , y _ { n - 2 } )$ per step. It therefore seems reasonable to assume that, as $x$ advances from $x _ { n - 1 }$ to $\scriptstyle x _ { n - { \frac { 1 } { 2 } } }$ , the approximation to the derivative at $x _ { n - 1 }$ , given as $f ( x _ { n - 1 } , y _ { n - 1 } )$ , should be increased by ${ \begin{array} { l } { { \frac { 1 } { 2 } } \left( f ( x _ { n - 1 } , y _ { n - 1 } ) - f ( x _ { n - 2 } , y _ { n - 2 } ) \right) } \end{array} }$ to obtain a usable approximation to $y ^ { \prime } ( x _ { n - \frac { 1 } { 2 } } )$ . This means that we could approximate the derivative at $x _ { n - { \frac { 1 } { 2 } } }$ , the mid-point of the interval, by $\frac { 3 } { 2 } f ( x _ { n - 1 } , y _ { n - 1 } ) ~ -$ ${ \scriptstyle { \frac { 1 } { 2 } } } f ( x _ { n - 2 } , y _ { n - 2 } )$ , to yield the numerical method

$$
y _ { n } = y _ { n - 1 } + h \bigl ( { \frac { 3 } { 2 } } f ( x _ { n - 1 } , y _ { n - 1 } ) - { \frac { 1 } { 2 } } f ( x _ { n - 2 } , y _ { n - 2 } ) \bigr ) .
$$

This method is an example of a ‘linear multistep method’.

Before we can carry out numerical tests with this method, we first need some procedure for carrying out the first step of the computation. Once $y _ { 1 }$ is calculated, the information that is needed for the computation of $y _ { 2 }$ , and subsequently the solution at later steps, will be available as needed. In the

Errors in the numerical solution of the orbital problem (201d) 2(I)with zero eccentricity through a half period using (222a)

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y1error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y2 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.002959760.000374720.000046740.000005830.000000730.00000009</td><td rowspan=1 colspan=1>7.89878.01688.02178.01368.0074</td><td rowspan=1 colspan=1>0.005373470.002241140.000674650.000182940.000047510.00001210</td><td rowspan=1 colspan=1>2.39763.32193.68793.85033.9267</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y3 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y4 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>-0.00471581-0.00215339-0.00066358-0.00018155-0.00004734-0.00001208</td><td rowspan=1 colspan=1>2.18993.24513.65513.83513.9194</td><td rowspan=1 colspan=1>-0.00154957-0.00019419-0.00002391-0.00000295-0.00000037-0.00000005</td><td rowspan=1 colspan=1>7.97978.12218.10178.06208.0339</td></tr></table>

experiments we report here, the first step is taken using the Runge–Kutta method introduced in the previous subsection.

The errors are shown in Table 222(I) and we see that, for this problem at least, the results are just as good as for the Runge–Kutta method (221a) and (221b), even though only one derivative is computed in each step. In fact, for components 1 and 4, better than second order convergence is observed.

# 223 Use of higher derivatives

For many practical problems, it is possible to derive formulae for the second and higher derivatives of $y$ , making use of the formula for $y ^ { \prime }$ given by a differential equation. This opens up many computational options, which can be used to enhance the performance of multistage (Runge–Kutta) and multivalue (multistep) methods. If these higher derivatives are available, then the most popular option is to use them to evaluate a number of terms in Taylor’s theorem. Even though we consider this idea further in Section 25, we present a simple illustrative example here.

Consider the initial value problem

$$
y ^ { \prime } = y x + y ^ { 2 } , \qquad y ( 0 ) = \frac { 1 } { 2 } ,
$$

![](images/f7d820eb193caa421e353fdb5c7f7c233232d49b25904715a587ef41e7096fef.jpg)  
Errors in problem (223a) using Taylor series with orders $p = 1 , 2 , 3 , 4$

with solution

$$
y ( x ) = \frac { \exp ( \frac { 1 } { 2 } x ^ { 2 } ) } { 2 - \int _ { 0 } ^ { x } \exp ( \frac { 1 } { 2 } x ^ { 2 } ) d x } .
$$

By differentiating (223a) once, twice and a third time, it is found that

$$
\begin{array} { r l } & { y ^ { \prime \prime } = ( x + 2 y ) y ^ { \prime } + y , } \\ & { y ^ { \prime \prime \prime } = ( x + 2 y ) y ^ { \prime \prime } + ( 2 + 2 y ^ { \prime } ) y ^ { \prime } , } \\ & { y ^ { ( 4 ) } = ( x + 2 y ) y ^ { \prime \prime \prime } + ( 3 + 6 y ^ { \prime } ) y ^ { \prime \prime } . } \end{array}
$$

We illustrate the Taylor series method by solving (223a) with output point $\overline { { x } } = 1$ . Using $n$ steps and stepsize $h = 1 / n$ , for $n = 8$ , 16, 32, . . . , $2 ^ { 2 0 }$ , the method was used with orders $p = 1$ , $2$ , 3 and 4. For example, if $p = 4$ , then

$$
\begin{array} { r } { y _ { n } = y _ { n - 1 } + h y ^ { \prime } + \frac { h ^ { 2 } } { 2 } y ^ { \prime \prime } + \frac { h ^ { 3 } } { 6 } y ^ { \prime \prime \prime } + \frac { h ^ { 2 } } { 2 4 } y ^ { ( 4 ) } , } \end{array}
$$

where $y ^ { \prime }$ , $y ^ { \prime \prime }$ , $y ^ { \prime \prime \prime }$ and $y ^ { ( 4 ) }$ are given by (223a), (223b), (223c) and (223d) with $x _ { n - 1 }$ and $y _ { n - 1 }$ substituted for $x$ and $y$ , respectively.

The results for these experiments are shown in Figure 223(i). In each case the error is plotted, where we note that the exact result is

$$
\exp ( \frac { 1 } { 2 } ) / \big ( 2 - \int _ { 0 } ^ { 1 } \exp ( \frac { 1 } { 2 } x ^ { 2 } ) d x \big ) ,
$$

with numerical value 2.04799324543883.

![](images/9f0960271c22ed8239bfdcef9786c39cf73075f1b327da9430c10d9172d3836f.jpg)  
Classification of general method types

# 224 Multistep–multistage–multiderivative methods

While multistep methods, multistage methods and multiderivative methods all exist in their own right, many attempts have been made to combine their attributes so as to obtain new methods of greater power. By introducing higher $y$ derivatives into multistep methods, a new class of methods is found. These are known as Obreshkov methods, after their discoverer Obreshkov (1940).

The best-known combination of the use of higher derivatives with Runge– Kutta methods is in Rosenbrock methods (Rosenbrock, 1963). This is actually a greater generalization, in the sense that derivatives of $f$ are used. These must be regarded as more general, because $y ^ { \prime \prime }$ can be found in the case of an autonomous problem as $y ^ { \prime \prime } ( x ) = f ^ { \prime } ( y ( x ) ) ( f ( y ( x ) ) )$ . On the other hand, it is not possible to compute $f ^ { \prime } ( y ( x ) )$ from values of the various $y$ derivatives. Rosenbrock methods have a role in the solution of stiff problems.

Other potentially useful combinations certainly exist but, in this book, we mainly confine ourselves to combinations of multistage and multiderivative methods. These we refer to as ‘general linear methods’. The various methods that come under the classifications we have discussed here can be seen in a diagrammatic representation in Figure 224(i). The Euler method can be thought of as the infimum of all the method classes, and is shown at the lowest point of this diagram. On the other hand, the class of general linear methods is the supremum of all multistage and multivalue methods. The supremum of all methods, including also those with a multiderivative nature, is represented by the highest point in Figure 224(i).

We have already seen, in Subsection 204, that the implicit Euler method has a role in the solution of stiff problems. Implicitness also exists in the case of linear multistep and Runge–Kutta methods. For example, the second order backward difference formula (also known as BDF2),

$$
y _ { n } = \frac { 2 } { 3 } h f ( x _ { n } , y _ { n } ) + \frac { 4 } { 3 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } ,
$$

is also used for stiff problems. There are also implicit Runge–Kutta methods, suitable for the solution of stiff problems.

Another example of an implicit method is the ‘implicit trapezoidal rule’, given by

$$
y _ { n } = y _ { n - 1 } + { \frac { h } { 2 } } { \big ( } f ( x _ { n } , y _ { n } ) + f ( x _ { n - 1 } , y _ { n - 1 } ) { \big ) } .
$$

Like the Euler method itself, and its implicit variant, (225b) is, at the same time, a linear multistep method and a Runge–Kutta method. As a linear multistep method, it can be regarded as a member of the Adams–Moulton family of methods. As a Runge–Kutta method, it can be regarded as a member of the Lobatto IIIA family.

Implicit methods carry with them the need to solve the nonlinear equation on which the solution, at a new step value, depends. For non-stiff problems, this can be conveniently carried out by fixed-point iteration. For example, the solution of the implicit equation (225b) is usually found by evaluating a starting approximation $\eta ^ { [ 0 ] }$ , given as $y _ { n }$ in (222a). A sequence of approximations $\eta ^ { \left[ k \right] }$ , $k = 1 , 2 , \ldots$ , is then formed by inserting $\eta ^ { \left[ k \right] }$ in place of $y _ { n }$ on the left-hand side of (225b), and $\eta ^ { \lfloor k - 1 \rfloor }$ in place of $y _ { n }$ on the right-hand side. That is,

$$
\eta ^ { [ k ] } = y _ { n - 1 } + { \frac { h } { 2 } } \left( f \left( x _ { n } , \eta ^ { [ k - 1 ] } \right) + f ( x _ { n - 1 } , y _ { n - 1 } ) \right) , \quad k = 1 , 2 , \ldots .
$$

The value of $y _ { n }$ actually used for the solution is the numerically computed limit to this sequence.

For stiff problems, unless $h$ is chosen abnormally small, this sequence will not converge, and more elaborate schemes are needed to evaluate the solution to the implicit equations. These schemes are generally variants of the Newton– Raphson method, and will be discussed further in reference to the particular methods as they arise.

# 226 Local error estimates

It is usually regarded as necessary to have, as an accompaniment to any numerical method, a means of assessing its accuracy, in completing each step it takes. The main reason for this is that the work devoted to each step, and the accuracy that is achieved in the step, should be balanced for overall efficiency. If the cost of each step is approximately constant, this means that the error committed in the steps should be approximately equal.

A second reason for assessing the accuracy of a method, along with the computation of the solution itself, is that it may be more efficient to change to a higher, or lower, member of the family of methods being used. The only way that this can really be decided is for the accuracy of a current method to be assessed and, at the same time, for some sort of assessment to be made of the alternative method under consideration. We discuss here only the local error of the current method.

It is not known how much a computed answer differs from what would correspond to the exact answer, defined locally. What is often available, instead, is a second approximation to the solution at the end of each step. The difference of these two approximations can sometimes be used to give quantitative information on the error in one of the two solution approximations.

We illustrate this idea in a single case. Suppose the method given by (222a) is used to give a starting value for the iterative solution of (225b). It is possible to estimate local errors by using the difference of these two approximations. We discuss this in more detail in the context of predictor–corrector Adams methods.

# Exercises 22

22.1 Assuming the function $f$ satisfies a Lipschitz condition and that $y$ , $y ^ { \prime }$ , $y ^ { \prime \prime }$ and $y ^ { \prime \prime \prime }$ are continuous, explain why the method given by (221a) and (221b) has order 2.

22.2 Explain why the method given by (222a) has order 2.

22.3 Find a method similar to (221a) and (221b), except that it is based on the mid-point rule, rather than the trapezoidal rule.

22.4 For a ‘quadrature problem’, $f ( x , y ) \quad = \quad \phi ( x )$ , compare the likely accuracies of the methods given in Subsections 221 and 222.

22.5 Verify your conclusion in Exercise 22.4 using the problem $y ^ { \prime } ( x ) = \cos ( x )$ on the interval $[ 0 , \pi / 2 ]$ .

22.6 Show that the backward difference method (225a) has order 2.

22.7 Calculate the solution to (203a) using the backward difference method (225a). Use $_ { n }$ steps with constant stepsize $\begin{array} { l l l } { h } & { = } & { \pi / n } \end{array}$ for $n =$ $2 ^ { \mathrm { { 0 } } } , 2 ^ { \mathrm { { 1 } } } , 2 ^ { \mathrm { { 2 } } } , \ldots , 2 ^ { \mathrm { { 1 0 } } }$ . Verify that second order behaviour is observed.

# 23 Runge–Kutta Methods

# 230 Historical introduction

The idea of generalizing the Euler method, by allowing for a number of evaluations of the derivative to take place in a step, is generally attributed to Runge (1895). Further contributions were made by Heun (1900) and Kutta (1901). The latter completely characterized the set of Runge–Kutta methods of order 4, and proposed the first methods of order 5. Special methods for second order differential equations were proposed by Nystr¨om (1925), who also contributed to the development of methods for first order equations. It was not until the work of Huˇta (1956, 1957) that sixth order methods were introduced.

Since the advent of digital computers, fresh interest has been focused on Runge–Kutta methods, and a large number of research workers have contributed to recent extensions to the theory, and to the development of particular methods. Although early studies were devoted entirely to explicit Runge–Kutta methods, interest has now moved to include implicit methods, which have become recognized as appropriate for the solution of stiff differential equations.

A number of different approaches have been used in the analysis of Runge– Kutta methods, but the one used in this section, and in the more detailed analysis of Chapter 3, is that developed by the present author (Butcher, 1963), following on from the work of Gill (1951) and Merson (1957).

# 231 Second order methods

In Subsection 221, a method was introduced based on the trapezoidal rule quadrature formula. It turns out that for any non-zero choice of a parameter $\theta$ , it is possible to construct a method with two stages and this same order. All that is required is a first partial step to form an approximation a distance $\theta h$ into the step. Using the derivative at this point, together with the derivative at the beginning of the step, the solution at the end of the step is then found using the second order quadrature formula

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x \approx \left( 1 - \frac { 1 } { 2 \theta } \right) \phi ( 0 ) + \frac { 1 } { 2 \theta } \phi ( \theta ) .
$$

Thus, to advance the solution from $x _ { n - 1 }$ to $x _ { n } = x _ { n - 1 } + h$ , the result is found from

$$
\begin{array} { l } { { Y = y _ { n - 1 } + \theta h f ( x _ { n - 1 } , y _ { n - 1 } ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + \left( 1 - \frac { 1 } { 2 \theta } \right) h f ( x _ { n - 1 } , y _ { n - 1 } ) + \frac { 1 } { 2 \theta } h f ( x _ { n - 1 } + \theta h , Y ) . } } \end{array}
$$

Note that the intermediate stage value $Y$ is an approximation to the solution at the ‘off-step’ point $x _ { n - 1 } + \theta h$ , and is equal to $y _ { n } ^ { * }$ , in the special case we have already considered, given by (221a) and (221b), in which $\theta = 1$ . The other most commonly used value is $\begin{array} { r } { \theta = \frac { 1 } { 2 } } \end{array}$ , as in the ‘mid-point rule’.

# 232 The coefficient tableau

It is convenient to represent a Runge–Kutta method by a partitioned tableau, of the form

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

in which the vector $c$ indicates the positions, within the step, of the stage values, the matrix $A$ indicates the dependence of the stages on the derivatives found at other stages, and $b ^ { \intercal }$ is a vector of quadrature weights, showing how the final result depends on the derivatives, computed at the various stages.

In the case of explicit methods, such as those we have considered so far in this section, the upper triangular components of $A$ are left blank, because they have zero value.

The first two of the following examples of Runge–Kutta tableaux are, respectively, for the Euler method and the general second order method, parameterized by an arbitrary non-zero $\theta$ . The special cases, which are also given, are for the trapezoidal rule method, designated here as RK21 and the mid-point rule method, RK22, correspond to $\theta = 1$ and $\textstyle \theta = { \frac { 1 } { 2 } }$ , respectively:

![](images/57cf80dcaabe0f5f6d86baffcfb75220d62b2c10b4151be0032ca52563a610b2.jpg)

# 233 Third order methods

It is possible to construct methods with three stages, which have order 3 numerical behaviour. These have the form

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { b _ { 1 } \quad b _ { 2 } \quad b _ { 3 } } \end{array} \right. , } \end{array}
$$

where $a _ { 2 1 } = c _ { 2 }$ and $a _ { 3 1 } + a _ { 3 2 } = c _ { 3 }$ . The conditions for order 3, taken from results that will be summarized in Subsection 234, are

$$
\begin{array} { r } { { b _ { 1 } } + { b _ { 2 } } + { b _ { 3 } } = 1 , } \\ { \displaystyle } \\ { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \frac { 1 } { 2 } , } \\ { \displaystyle } \\ { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \frac { 1 } { 3 } , } \\ { b _ { 3 } a _ { 3 2 } c _ { 2 } = \frac { 1 } { 6 } . } \end{array}
$$

The following tableaux

$$
{ \mathrm { R K 3 1 : } } \quad { \begin{array} { l } { \quad 0 } \\ { \quad { \frac { 2 } { 3 } } } \\ { \quad { \frac { { \frac { 2 } { 3 } } } { \left\{ \begin{array} { l l l } { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \\ { { \frac { 1 } { 4 } } } & { { 0 } } & { { \frac { 3 } { 4 } } } \end{array} \right. } } } } \end{array} 
$$

and

give two possible solutions to (233a)–(233d).

# 234 Introduction to order conditions

As the order being sought increases, the algebraic conditions on the coefficients of the method become increasingly complicated. The pattern behind these conditions is known and, in this brief introduction to the order conditions, we state the results without any justification and show, by examples, how they are used.

![](images/87985150b311a58e0ff0506897b42884a8b4cbf36973f1d4d4839ba2baed0f24.jpg)  
Some illustrative rooted trees

Let $T$ denote the set of all ‘rooted trees’. These are simple combinatorial graphs, which have the properties of being connected, having no cycles, and having a specific vertex designated as the root. The ‘order’ of a tree is the number of vertices in this tree. If the order is greater than 1, then the ‘leaves’ of a tree are the vertices from which there are no outward-growing arcs; in other words, a leaf is a vertex, other than the root, which has exactly one other vertex joined to it.

An assortment of trees of various orders, with leaves and the root indicated in each case, is shown in Figure $2 3 4 ( \mathrm { i } ) .$ In pictorial representations of particular rooted trees, as in this figure, we use the convention of placing the root at the lowest point in the picture.

For each tree $t$ , a corresponding polynomial in the coefficients of the method can be written down. Denote this by $\Phi ( t )$ . Also associated with each tree $t$ is an integer $\gamma ( t )$ . We now explain how $\Phi ( t )$ and $\gamma ( t )$ are constructed.

In the case of $\Phi ( t )$ , associate with each vertex of the tree, except the leaves, a label $i$ , $j , \ldots ,$ and assume that $i$ is the label attached to the root. Write down a sequence of factors of which the first is $b _ { i }$ . For each arc of the tree, other than an arc that terminates in a leaf, write down a factor, say $a _ { j k }$ , where $j$ and $k$ are the beginning and end of the arc (assuming that all directions are in the sense of movement away from the root). Finally, for each arc terminating at a leaf, write down a factor, say $c _ { j }$ , where $j$ is the label attached to the beginning of this arc. Having written down this sequence of factors, sum their product for all possible choices of each of the labels, in the set $\{ 1 , 2 , \ldots , s \}$ .

To find the value of $\gamma ( t )$ , associate a factor with each vertex of the tree. For the leaves this factor is 1, and for all other vertices it is equal to the sum of the factors attached to all outward-growing neighbours, plus 1. The product of the factors, for all vertices of the tree, is the value of $\gamma ( t )$ .

The rooted trees up to order 4   

<table><tr><td>Tree</td><td>·</td><td>：</td><td>?</td><td>：</td></tr><tr><td>Order</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>重</td><td>∑ibi</td><td>∑ibiCi</td><td>∑ibic</td><td>∑ijbiaijCj</td></tr><tr><td>Y</td><td>1</td><td>2</td><td>3</td><td>6</td></tr></table>

<table><tr><td>Tree</td><td>? ?</td><td>丫</td><td>：</td></tr><tr><td>Order</td><td>4 4</td><td>4</td><td>4</td></tr><tr><td>重</td><td>∑ibic</td><td></td><td>∑ijbiciaijCj ∑ijbiaijc² ∑ijkbiaijajkCk</td></tr><tr><td>Y</td><td>4 8</td><td>12</td><td>24</td></tr></table>

The values of these quantities are shown in Table 234(I), for each of the eight trees with orders up to 4. A further illustrative example is given by the tree

$$
t = \alpha ^ { Y }
$$

for which $\begin{array} { r } { \Phi ( t ) = \sum _ { i j } b _ { i } c _ { i } ^ { 2 } a _ { i j } c _ { j } ^ { 2 } } \end{array}$ and $\gamma ( t ) ~ = ~ 1 8$ . Details of the calculation of these quantities are presented in Figure 234(ii). On the left-hand diagram labels $i$ and $j$ are attached to the non-terminal vertices, as used in the formula for $\Phi ( t )$ , using the factors shown in the middle diagram. On the right-hand diagram, the factors are shown whose product gives the value of $\gamma ( t )$ .

![](images/f186d3236766e589fa70ce8741ddc83be0bb3dc7bf22dad33fa708803aebd53c.jpg)  
Calculation details for $\Phi ( t )$ and $\gamma ( t )$ , where $t = \Phi$

# 235 Fourth order methods

Write the order conditions presented in the previous subsection, in the special case $s = 4$ , assuming, because the method will be explicit, that $a _ { i j } = 0$ unless $i > j$ . This yields the conditions

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 3 } c _ { 2 } + b _ { 4 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 3 } + b _ { 3 } c _ { 4 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } + b _ { 4 } c _ { 4 } \alpha _ { 3 } c _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 6 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } - \frac { 1 } { 4 } , } \\ { b _ { 6 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } + b _ { 6 } c _ { 4 } \alpha _ { 4 } c _ { 3 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 4 } c _ { 3 } = \frac { 1 } { 1 2 } } \\ { b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } = \frac { 1 } { 2 } . } \end{array}
$$

That $c _ { 4 } = 1$ can be shown, by solving for $b _ { 2 }$ , $b _ { 3 }$ and $b _ { 4 }$ , from equations (235b), (235c) and (235e); by then solving for $a _ { 3 2 }$ , $a _ { 4 2 }$ and $a _ { 4 3 }$ from (235d), (235f) and (235g); and then by substituting into (235h). Many solutions and families of solutions are known to these conditions; the following are two examples:

<table><tr><td rowspan="2">RK41 :</td><td>0 G</td><td>1 0 1 0 0</td><td>1</td><td rowspan="2">1</td></tr><tr><td></td><td>1</td><td>1 1</td></tr><tr><td rowspan="2">RK42 :</td><td>1</td><td>1 1 1 -2</td><td>2</td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>2 16</td></tr></table>

# 236 Higher orders

Because the number of rooted trees of various orders increases rapidly for orders greater than 4, the complexity of the order conditions also increases. Above order 4, it is no longer possible to obtain order $s$ with just $s$ stages. For order 5, six stages are required, and for order 6, seven stages are required. Above this order, there are even sharper increases in the required numbers of stages. We give a single example of a fifth order method:

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>G</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RK5 :</td><td></td><td></td><td>0</td><td></td><td>GR</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>16</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>32</td><td>GU</td><td></td><td></td><td></td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>7 90</td><td>0</td><td></td><td>32 90</td><td>1品</td><td>32</td><td>7 90</td></tr></table>

# 237 Implicit Runge–Kutta methods

Implicit methods have the potential advantage, compared with explicit methods, that there will be fewer stages for the same order. The disadvantage is in the implicit nature of at least some of the stages. This makes it impossible to avoid iterative methods of evaluation. For the purpose of experimental comparison with explicit methods, we present here just three methods:

<table><tr><td>1 1</td><td>1 1 3</td><td>0 0 4</td></tr><tr><td>3-2√2 1</td><td>5- -3√2 4 1+√2 4</td><td>7- -5√2 4 3-√2 4 3-√2</td></tr><tr><td></td><td>1+√2 4</td><td>4 1 √ 6</td></tr><tr><td>G A +</td><td>14+ 1 1</td><td>1 1</td></tr></table>

It can be verified that (237a) has order 3, (237b) has order only 2 and (237c) has order 4. In the implicit case, the cost of using a specific method depends not so much on the number of stages, as on the difficulty in evaluating the stages. From this point of view, (237a) is the easiest to use because only one of the stages is implicit; (237b) and (237c) each have two interconnected implicit stages but, as we will see in Subsection 363, the order 2 method (237b) can be implemented more cheaply than (237c).

# 238 Stability characteristics

In Subsection 216, we discussed the stability of the Euler method when solving a linear problem of the form

$$
y ^ { \prime } ( x ) = q y ( x ) .
$$

If $z = h q$ , then in a single step of length $h$ , the exact solution will be multiplied by the factor $\exp ( z )$ . In the same time interval the approximate solution computed using a Runge–Kutta method will be multiplied by a function of $z$ , specific to the particular Runge–Kutta method. As in Subsection 216, we denote this ‘stability function’ by $R ( z )$ . The ‘stability region’, defined as $\{ z \in \mathbb { C } : | R ( z ) | \leq 1 \}$ , is the set of points in the complex plane such that the computed solution remains bounded after many steps of computation. There is special interest in values of $z$ in the left half-plane, because in this case the exact solution is bounded and good modelling of the problem would require the computed solution to behave in a similar manner.

For an $s$ -stage Runge–Kutta method, defined by the tableau

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

the vector $Y$ , made up from the $s$ stage values, satisfies

$$
Y = \mathbf { 1 } y _ { 0 } + h A q Y = \mathbf { 1 } y _ { 0 } + z A Y ,
$$

where $y _ { 0 }$ is the incoming approximation. It follows that

$$
Y = ( I - z A ) ^ { - 1 } \mathbf { 1 } y _ { 0 } .
$$

Substitute this into the solution approximation found at the end of the step, and we find

$$
y _ { 1 } = y _ { 0 } + h b ^ { \intercal } q Y = y _ { 0 } + z b ^ { \intercal } ( I - z A ) ^ { - 1 } { \mathbf 1 } y _ { 0 } = R ( z ) y _ { 0 } ,
$$

where

$$
R ( z ) = 1 + z b ^ { \top } ( I - z A ) ^ { - 1 } \mathbf { 1 } .
$$

If (238a) represents an explicit Runge–Kutta method with order $p = s = 1 , 2 , 3$ or 4, then we can evaluate $R ( z )$ very simply as the exponential series truncated

![](images/18736941ee2bb85e725152cb0eaffe8d962a456eb25233ca806693eb885447ae.jpg)  
Stability regions for some explicit Runge–Kutta methods

at the $z ^ { s }$ term. To see why this should be the case, expand $( I - z A ) ^ { - 1 }$ by the geometric series and evaluate the terms using the order condition

$$
b ^ { \top } A ^ { k - 1 } \mathbf { 1 } = b ^ { \top } A ^ { k - 2 } c = { \frac { 1 } { k ! } } , \qquad k = 1 , 2 , \ldots , p .
$$

Hence, we have for the four cases for which $s = p$ is possible,

$$
R ( z ) = \left\{ \begin{array} { l l } { 1 + z , } & { p = 1 , } \\ { ] 1 + z + \frac { 1 } { 2 } z ^ { 2 } , } & { p = 2 , } \\ { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } , } & { p = 3 , } \\ { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } , } & { p = 4 . } \end{array} \right.
$$

The boundaries of the stability regions defined by these functions are shown in Figure 238(i). In each case the stability region is the bounded set enclosed by these curves.

For explicit methods with $s = 6$ and $p = 5$ , the stability function takes the form

$$
\begin{array} { r } { R ( z ) = 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } + \frac { 1 } { 1 2 0 } z ^ { 5 } + C z ^ { 6 } , } \end{array}
$$

where $C$ depends on the particular method. In the case of the method given by the tableau (236a), $\begin{array} { r } { C = \frac { 1 } { 1 2 8 0 } } \end{array}$ 11280 , and the stability region for this is also shown in Figure 238(i). In each case, the value of $p$ is attached to the curve.

![](images/5c68e9b1d738346ad122a7e308cc25c37692bda298eadd23b0fe70cad3e5df53.jpg)  
Stability regions for some implicit Runge–Kutta methods

It is never possible, even by the addition of extra stages, to devise explicit methods with order at least 1, which have unbounded stability regions, because $R ( z )$ is always a polynomial equal to $1 + z + O ( z ^ { 2 } )$ . However, as we saw in the case of the implicit Euler method, there is no such barrier for implicit Runge–Kutta methods.

For the three methods quoted in Subsection 237, the stability functions are found to be

$$
\begin{array} { r l r } & { } & { R ( z ) = \left\{ \begin{array} { l l } { \displaystyle 1 + \frac { 2 z } { 3 } + \frac { z ^ { 2 } } { 6 } , } & { \mathrm { m e t h o d ~ ( 2 3 7 a ) } , } \\ { \displaystyle 1 - \frac { z } { 3 } } & { \mathrm { m e t h o d ~ ( 2 3 7 a ) } , } \end{array} \right. } \\ & { } & { R ( z ) = \left\{ \begin{array} { l l } { \displaystyle 1 + ( \sqrt { 2 } - 1 ) z } & { \mathrm { m e t h o d ~ ( 2 3 7 b ) } , } \\ { \displaystyle \left( 1 - \left( 1 - \frac { 1 } { 2 } \sqrt { 2 } \right) z \right) ^ { 2 } , } & { \mathrm { m e t h o d ~ ( 2 3 7 b ) } , } \\ { \displaystyle \frac { 1 + \frac { z } { 2 } + \frac { z ^ { 2 } } { 1 2 } } { 1 - \frac { z ^ { 2 } } { 2 } + \frac { z ^ { 2 } } { 1 2 } } , } & { \mathrm { m e t h o d ~ ( 2 3 7 c ) } , } \end{array} \right. } \end{array}
$$

and the three stability regions are shown in Figure 238(ii). Note that for the fourth order method (237c), the stability region is exactly the closed left half-plane. The method (237a) shares the property of explicit Runge– Kutta methods of having a bounded stability region, whereas (237b) has an unbounded stability region which includes the left half-plane.

![](images/66dcd513a0cb28090850e59777de8eb64e9ca4d378f756739cf94f8a54478101.jpg)  
Orbital calculations for various Runge–Kutta methods

# 239 Numerical examples

High order methods generally perform better than low order methods if sufficiently small stepsizes are used. We illustrate this by attempting, with the methods introduced in this section, a solution to the gravitational problem (201d) with initial values corresponding to an eccentricity $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ . Although calculations were performed with each of the seven methods RK21, RK22, RK31, RK32, RK41, RK42, RK5, only results for the four methods RK22, RK31, RK42 and RK5 are actually presented in Figure 239(i). It was observed that for the two methods with each of the orders 2, 3 and 4, there was very little difference between the accuracy achieved and a representative of each order – in fact the slightly more accurate method was chosen in each case $^ -$ is sufficient to illustrate the phenomenon of $h ^ { p }$ dependence. In Figure 239(i), methods RK22, RK31, RK42 and RK5 are denoted by 2, 3, 4 and 5.

For this problem, high order methods are always more accurate than low order methods. However, the relative advantage is exaggerated in that no account is taken of the greater work in completing a step as the order increases. Assuming that the total computational work is proportional to the number of stages in the method, it is a simple matter to compensate for this; all that needs to be done is to multiply the number of steps by the number of stages in each method. The comparisons with this correction made are shown in Figure 239(ii). The general conclusion, that high order is more efficient than low order, still follows from these comparisons, but not to such a marked extent.

Numerical tests, not reported here, indicate similar behaviour for implicit methods. For the initial value problem (201a), with output computed at $x = 1$ , (237a) and (237b) gave slightly worse results than for corresponding explicit methods. However, for the fourth order method (237c), the results were approximately six decimal places better. This suggests that, even though the cost of evaluating the result in each step of an implicit method is significantly higher, the extra cost is sometimes worthwhile for this method.

![](images/220dfd13f2c84d938647042f8ebdc5aacb3eb0105a62709625692e8486650322.jpg)  
Runge–Kutta methods with cost corrections

# Exercises 23

23.1 Repeat the calculation that led to Table 221(I) but using the method given by (231a) and (231b) with $\begin{array} { r } { \theta = \frac { 1 } { 2 } } \end{array}$ .

23.2 Find a solution to the third order conditions (233a), (233b), (233c) and (233d) such that $b _ { 1 } = 0$ , $c _ { 3 } = 1$ .

23.3 Continue Table 234(I) to include trees of order 5.

23.4 Write down the formula for $\Phi ( t )$ and the value of $\gamma ( t )$ for $t$ the order 7 tree

$$
t = \ddagger \ddagger
$$

23.5 By noting that $b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } \cdot b _ { 3 } ( c _ { 4 } - c _ { 3 } ) ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = b _ { 4 } a _ { 4 3 } ( c _ { 3 } - c _ { 2 } ) c _ { 3 }$ · $b _ { 3 } ( c _ { 4 } - c _ { 3 } ) a _ { 3 2 } c _ { 2 }$ , prove that $c _ { 4 } = 1$ for any solution to the fourth order conditions (235a)–(235h).

23.6 Find the order of the implicit method given by the tableau (237a).

23.7 Solve the orbital problem with eccentricity $e ~ = ~ 0$ using the implicit method (237a).

# 24 Linear Multistep Methods

# 240 Historical introduction

The idea of extending the Euler method by allowing the approximate solution at a point to depend on the solution values and the derivative values at several previous step values was originally proposed by Bashforth and Adams (1883). Not only was this special type of method, now known as the Adams–Bashforth method, introduced, but a further idea was suggested. This further idea was developed in detail by Moulton (1926). Other special types of linear multistep methods were proposed by Nystr¨om (1925) and Milne (1926, 1953). The idea of predictor–corrector methods is associated with the name of Milne, especially because of a simple type of error estimate available with such methods. The ‘backward difference’ methods were introduced by Curtiss and Hirschfelder (1952), and these have a special role in the solution of stiff problems.

The modern theory of linear multistep methods was developed in large measure by Dahlquist (1956), and has become widely known through the exposition by Henrici (1962, 1963).

# 241 Adams methods

The most important linear multistep methods for non-stiff problems are of Adams type. That is, the solution approximation at $x _ { n }$ is defined either as

$$
\begin{array} { r } { y _ { n } = y _ { n - 1 } + h ( \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) \qquad } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) , } \end{array}
$$

or as

$$
\begin{array} { c } { y _ { n } = y _ { n - 1 } + h ( \beta _ { 0 } f ( x _ { n } , y _ { n } ) + \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) , } \end{array}
$$

where, in each case, the constants ( $\beta _ { 0 }$ ), $\beta _ { 1 }$ , $\beta _ { 2 }$ , . . . , $\beta _ { k }$ are chosen to give the highest possible order.

The meaning of order, and how it is achieved in particular cases, is straightforward in the case of methods of the form (241a), which are known as ‘Adams–Bashforth’ methods. Assuming that no errors have yet been introduced when the approximation at $x _ { n }$ is about to be calculated, we can replace the terms on the right-hand side by the quantities they are supposed to approximate, that is, by $y ( x _ { n - 1 } )$ , $y ^ { \prime } ( x _ { n - 1 } )$ , $y ^ { \prime } ( x _ { n - 2 } )$ , . . . , $y ^ { \prime } ( x _ { n - k } )$ , respectively. The amount by which the approximation, written in this form, differs from $y ( x _ { n } )$ is the error generated in this particular step. If this error can be estimated for a smooth problem as $O ( h ^ { p + 1 } )$ , then the method is regarded as having order $p$ .

For the methods given by (241b), which are known as ‘Adams–Moulton’ methods, the term involving $f ( x _ { n } , y _ { n } )$ is a complication in this understanding of order. However, the conclusion turns out to be exactly the same as for Adams–Bashforth methods: if every term in (241b) is replaced by the quantity it is supposed to be approximating and the two sides of this equation differ by an amount that can be estimated as $O ( h ^ { p + 1 } )$ , then the method has order $p$ .

To obtain a simple criterion for a given order, we can write all terms in

$$
\begin{array} { r l r } {  { y ( x _ { n } ) - y ( x _ { n - 1 } ) - h \big ( \beta _ { 0 } y ^ { \prime } ( x _ { n } ) + \beta _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + \beta _ { 2 } y ^ { \prime } ( x _ { n - 2 } ) } } \\ & { } & { \qquad + \cdot \cdot + \beta _ { k } y ^ { \prime } ( x _ { n - k } ) \big ) } \end{array}
$$

as Taylor series about, for example, $x _ { n }$ . This gives an expression of the form

$$
C _ { 1 } h y ^ { \prime } ( x _ { n } ) + C _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot + C _ { p } h ^ { p } y ^ { ( p ) } ( x _ { n } ) + O ( h ^ { p + 1 } ) ,
$$

and the conditions for order $p$ will be that $C _ { 1 } = C _ { 2 } = \cdot \cdot \cdot = C _ { p } = 0$ .

It can be shown that an equivalent criterion is that (241c) vanishes whenever $y$ is a polynomial of degree not exceeding $p$ .

We will use these criteria to derive Adams–Bashforth methods with $p = k$ for $k = 2 , 3 , 4$ , and Adams–Moulton methods with $p = k + 1$ for $k = 1 , 2 , 3$ .

For $k = 4$ , the Taylor expansion of (241c) takes the form

$$
\begin{array} { r l } & { h y ^ { \prime } ( x _ { n } ) ( 1 - \beta _ { 0 } - \beta _ { 1 } - \beta _ { 2 } - \beta _ { 3 } - \beta _ { 4 } ) } \\ & { \qquad + h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) \big ( - \frac 1 2 + \beta _ { 1 } + 2 \beta _ { 2 } + 3 \beta _ { 3 } + 4 \beta _ { 4 } \big ) } \\ & { \qquad + h ^ { 3 } y ^ { ( 3 ) } ( x _ { n } ) \big ( \frac 1 6 - \frac 1 2 ( \beta _ { 1 } + 4 \beta _ { 2 } + 9 \beta _ { 3 } + 1 6 \beta _ { 4 } ) \big ) } \\ & { \qquad + h ^ { 4 } y ^ { ( 4 ) } ( x _ { n } ) \big ( - \frac 1 { 2 4 } + \frac 1 6 ( \beta _ { 1 } + 8 \beta _ { 2 } + 2 7 \beta _ { 3 } + 6 4 \beta _ { 4 } ) \big ) + O ( h ^ { 5 } ) , } \end{array}
$$

so that

$$
\begin{array} { r l } & { C _ { 1 } = 1 - \beta _ { 0 } - \beta _ { 1 } - \beta _ { 2 } - \beta _ { 3 } - \beta _ { 4 } , } \\ & { C _ { 2 } = - \frac { 1 } { 2 } + \beta _ { 1 } + 2 \beta _ { 2 } + 3 \beta _ { 3 } + 4 \beta _ { 4 } , } \\ & { C _ { 3 } = \frac { 1 } { 6 } - \frac { 1 } { 2 } ( \beta _ { 1 } + 4 \beta _ { 2 } + 9 \beta _ { 3 } + 1 6 \beta _ { 4 } ) , } \\ & { C _ { 4 } = - \frac { 1 } { 2 4 } + \frac { 1 } { 6 } ( \beta _ { 1 } + 8 \beta _ { 2 } + 2 7 \beta _ { 3 } + 6 4 \beta _ { 4 } ) . } \end{array}
$$

For the Adams–Bashforth methods the value of $\beta _ { 0 }$ is zero; for $k = 2$ we also have $\beta _ { 3 } = \beta _ { 4 } = 0$ and we must solve the equations $C _ { 1 } = C _ { 2 } = 0$ . This gives $\beta _ { 1 } = \textstyle { \frac { 3 } { 2 } }$ and $\beta _ { 2 } = - \frac { 1 } { 2 }$ . For $k = 3$ we allow $\beta _ { 3 }$ to be non-zero and we require that $C _ { 1 } = C _ { 2 } = C _ { 3 } = 0$ $\beta _ { 3 } = \textstyle { \frac { 5 } { 1 2 } }$ $k = 4$ . The solutions of these equations is $C _ { 1 } = C _ { 2 } = C _ { 3 } = C _ { 4 } = 0$ $\beta _ { 1 } = \textstyle { \frac { 2 3 } { 1 2 } }$ , $\beta _ { 2 } = - \textstyle { \frac { 4 } { 3 } }$ $\beta _ { 1 } = \textstyle { \frac { 5 5 } { 2 4 } }$ 3 5 , $\beta _ { 2 } = - \frac { 5 9 } { 2 4 }$ $\textstyle \beta _ { 3 } = { \frac { 3 7 } { 2 4 } }$ $\beta _ { 4 } = - \textstyle { \frac { 3 } { 8 } }$

the Adam) we have milar man $\beta _ { 0 }$ $k = 1$ $p = 2$ $\beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } = 0$ $C _ { 1 } = C _ { 2 } = 0$ $\begin{array} { r } { \beta _ { 0 } = \beta _ { 1 } = \frac { 1 } { 2 } } \end{array}$ and for $k = 3$ ( $p = 4$ ) that $\begin{array} { r } { \beta _ { 0 } = \frac { 3 } { 8 } } \end{array}$ $k = 2$ , $\beta _ { 1 } = \textstyle { \frac { 1 9 } { 2 4 } }$ $p = 3$ ） $\beta _ { 2 } = - \frac { 5 } { 2 4 }$ $\beta _ { 0 } = \textstyle { \frac { 5 } { 1 2 } }$ , $\beta _ { 3 } = \textstyle { \frac { 1 } { 2 4 } }$ $\beta _ { 1 } = \textstyle { \frac { 2 } { 3 } }$ . $\beta _ { 2 } = - \frac { 1 } { 1 2 }$

# 242 General form of linear multistep methods

Even though Adams methods are amongst the most commonly used classes of linear multistep methods, they are very specialized in that the dependence of $y _ { n }$ on previously computed values ignores $y _ { n - 1 }$ , $y _ { n - 2 }$ , $\cdot \cdot \cdot$ , $y _ { n - k }$ . The general form of the method includes additional terms to take these into account. It thus has the form

$$
\begin{array} { c } { y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ { + h \big ( \beta _ { 0 } f ( x _ { n } , y _ { n } ) + \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) \big ) . } \end{array}
$$

It is customary to characterize this method by polynomials whose coefficients are the numbers $\alpha _ { 1 }$ , $\alpha _ { 2 }$ , . . . , $\alpha _ { k }$ , $\beta _ { 0 }$ , $\beta _ { 1 }$ , $\beta _ { 2 }$ , $\cdot \cdot \cdot$ , $\beta _ { k }$ . The standard terminology is to use polynomials $\rho ( z )$ and $\sigma ( z )$ defined by

$$
\begin{array} { l } { \rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } , } \\ { \sigma ( z ) = \beta _ { 0 } z ^ { k } + \beta _ { 1 } z ^ { k - 1 } + \beta _ { 2 } z ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } . } \end{array}
$$

The style we are adopting in this book makes it more convenient to use a slightly different pair of polynomials,

$$
\begin{array} { l } { \alpha ( z ) = 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } z ^ { k } , } \\ { \beta ( z ) = \beta _ { 0 } + \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { k } z ^ { k } . } \end{array}
$$

Of course, it really makes little difference whether we use $( \rho , \sigma )$ or $[ \alpha , \beta ]$ t o characterize a method because, once the value of $k$ is known, we can move between them by the relations

$$
\alpha ( z ) = z ^ { k } \rho \Big ( \frac { 1 } { z } \Big ) , \beta ( z ) = z ^ { k } \sigma \Big ( \frac { 1 } { z } \Big ) , \rho ( z ) = z ^ { k } \alpha \Big ( \frac { 1 } { z } \Big ) , \sigma ( z ) = z ^ { k } \beta \Big ( \frac { 1 } { z } \Big ) .
$$

For all eligible $\alpha$ polynomials, $\alpha ( 0 ) = 1$ , and for Adams methods, $\alpha ( z ) = 1 - z$ . Using the $[ \alpha , \beta ]$ representation, we can distinguish Adams–Bashforth from Adams–Moulton by the fact that $\beta ( 0 ) = 0$ for the Bashforth variety.

# 243 Consistency, stability and convergence

Suppose we attempt the numerical solution of the simple differential equation $y ^ { \prime } ( x ) = 0$ , with exact solution $y ( x ) = 1$ , using the linear multistep method characterized by the pair of polynomials $\lfloor \alpha , \beta \rfloor$ . If the exact answer has already been found for $k$ steps in a row, it seems to be a desirable property of the method that the exact value is also found in one further step. This computed value is equal to $\alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k }$ . For this expression to have the value $^ { 1 }$ is equivalent to the assumption that $\alpha ( 1 ) = 0$ or, what is equivalent, that $\rho ( 1 ) = 0$ . Because of its fundamental importance, this property will be given the name ‘preconsistency’.

Another interpretation of preconsistency can be found in terms of the covariance of the numerical method with respect to a translation. By a translation we mean the replacing of an autonomous initial value problem $y ^ { \prime } ( x ) \ = \ f { \big ( } y ( x ) { \big ) }$ , $y ( x _ { 0 } ) ~ = ~ y _ { 0 }$ , by a related problem $z ^ { \prime } ( x ) ~ = ~ f ( z ( x ) + v )$ , $z ( x _ { 0 } ) = y _ { 0 } - v$ . For the exact solutions to these problems, the value of $z$ will always equal the value of $y$ with the vector $v$ subtracted. In considering a numerical solution to each of these problems, we can do the calculation in terms of $y$ and then carry out the translation afterwards; or we can do the transformation first and carry out the numerical approximation using the $z$ values. By ‘covariance’ we mean that the two numerical results are exactly the same.

It is easy to verify that the only way this can be guaranteed to happen, if the calculations are carried out using a linear multistep method, is for the method to be preconsistent.

For a preconsistent method it is desirable that the exact solution can also be found for another simple differential initial value problem: the problem given by $y ^ { \prime } ( x ) = 1$ , $y ( 0 ) = 0$ . For every step, the value of $f ( y _ { n } )$ is precisely 1. Substitute these into (242a), and it is found that

$$
n h = \sum _ { i = 1 } ^ { k } \alpha _ { i } h ( n - i ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } ,
$$

implying that

$$
n \left( 1 - \sum _ { i = 1 } ^ { k } \alpha _ { i } \right) = \sum _ { i = 1 } ^ { k } \beta _ { i } - \sum _ { i = 1 } ^ { k } i \alpha _ { i } .
$$

The left-hand side vanishes for a preconsistent method, whereas the righthand side can be written in the form $\beta ( 1 ) + \alpha ^ { \prime } ( 1 )$ . A ‘consistent method’ is a method that satisfies the condition that $\beta ( 1 ) + \alpha ^ { \prime } ( 1 ) = 0$ , in addition to satisfying the preconsistency condition $\alpha ( 1 ) = 0$ .

No matter how precise numerical approximations to the solution to a differential equation might be, this precision has no ultimate benefit unless the effect on later step values of small errors is bounded. Later steps are effected by the introduction of a perturbation in step $m$ both through their dependence on $y _ { m }$ itself and through their dependence on $h f ( x _ { m } , y _ { m } )$ . To simplify the discussion we exclude the second cause of error dependence by restricting ourselves to a simple ‘quadrature’ type of problem in which $y ^ { \prime } ( x ) = f ( x )$ . This will mean that the difference between the unperturbed and perturbed problem will satisfy the even simpler equation $y ^ { \prime } ( x ) = 0$ . Consider the difference equation satisfied by the numerical solution just for the perturbation itself. This difference equation is

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } .
$$

A linear multistep method is said to be ‘stable’ if all solutions to the difference equation (243a) are bounded as $n \longrightarrow \infty$ .

From the theory of linear difference equations, we know exactly when this will be the case. It is necessary and sufficient that all zeros of the polynomial $\rho$ lie in the closed unit disc $\{ z : | z | \leq 1 \}$ and that all repeated zeros lie in the open unit disc $\{ z : | z | < 1 \}$ . Because the zeros of $\alpha$ are the reciprocals of those of $\rho$ we can equally state these conditions as (i) all zeros of $\alpha$ lie outside the open unit disc, and (ii) all repeated zeros of $\alpha$ lie outside the closed unit disc.

‘Convergence’ refers to the ability of a method to approximate the solution to a differential equation to any required accuracy, if sufficiently many small steps are taken. Of course, any numerical result computed by a linear multistep method will depend not only on the particular coefficients of the method and the differential equation, but also on the procedure used to obtain starting values. In the formal definition of this concept, we will not impose any conditions on how the starting values are approximated except to require that, as $h  0$ , the errors in the starting values tend to zero. Because the exact solution is continuous, this is equivalent to requiring that the starting values all converge to the initial value specified for the problem.

Divide the interval $[ x _ { 0 } , { \overline { { x } } } ]$ into $n$ steps each of size $h = ( \overline { { x } } - x _ { 0 } ) / n$ , for every positive integer $n$ . Solve a standard initial value problem using starting values $y _ { 0 }$ , $y _ { 1 }$ , $\cdot \cdot \cdot$ , $y _ { k - 1 }$ which depend on $h$ and converge to $y ( x _ { 0 } )$ as $h  0$ . Let the error in the approximation computed at $\scriptstyle { \overline { { x } } }$ be denoted by $\epsilon _ { n }$ . The method is convergent if necessarily $\epsilon _ { n } \to 0$ as $n \longrightarrow \infty$ .

We discuss this property, and its relationship to other concepts introduced in this subsection, in Chapter 4. In the meantime, we state without proof the important result expressed in the following.

Theorem 243A A linear multistep method is convergent if and only if it is stable and consistent.

# 244 Predictor–corrector Adams methods

Continuing the discussion of Adams–Bashforth and Adams–Moulton methods from Subsection 241, we present in tabular form the coefficients of these methods for orders as high as 8. In the Adams–Bashforth case this means presenting the methods as far as $k = 8$ and in the Moulton case as far as $k = 7$ .

Along with the coefficients of the methods, the value is given of the error constants. For example, in the case of the Adams–Bashforth method with order 2 we can write

$$
y ( x _ { n } ) = y ( x _ { n - 1 } ) + h \big ( { \textstyle \frac { 3 } { 2 } } y ^ { \prime } ( x _ { n - 1 } ) - { \textstyle \frac { 1 } { 2 } } y ^ { \prime } ( x _ { n - 2 } ) \big ) + C h ^ { 3 } y ^ { ( 3 ) } ( x _ { n } ) + O ( h ^ { 4 } ) ,
$$

Coefficients and error constants for Adams–Bashforth methods   

<table><tr><td>k</td><td>β1</td><td></td><td></td><td>ββββ5</td><td></td><td></td><td>βββ8</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>24</td><td>59 24</td><td>中</td><td>3</td><td></td><td></td><td></td><td></td><td>251 720</td></tr><tr><td>5</td><td>1901 720</td><td>1387 360</td><td>109 30</td><td>637 360</td><td>251 720</td><td></td><td></td><td></td><td>95 288</td></tr><tr><td>6</td><td>4277 1440</td><td>2641 480</td><td>4991 720</td><td>3649 720</td><td>959 480</td><td>95 288</td><td></td><td></td><td>19087 60480</td></tr><tr><td>7</td><td>198721 60480</td><td>18637 2520</td><td>235183 20160</td><td>10754 945</td><td>135713 20160</td><td>5603 2520</td><td>19087 60480</td><td></td><td>5257 17280</td></tr><tr><td>8</td><td>16083 4480</td><td>1152169 120960</td><td>242653 13440</td><td>296053 13440</td><td>2102243 120960</td><td>115747 13440</td><td>32863 13440</td><td>5257 17280</td><td>1070017 3628800</td></tr></table>

Coefficients and error constants for Adams–Moulton methods   

<table><tr><td>k</td><td>β</td><td>β1</td><td></td><td>ββ</td><td></td><td>β4β5</td><td></td><td>ββ</td><td>C</td></tr><tr><td>0</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>1</td><td></td><td>D</td><td></td><td></td><td></td><td></td><td></td><td></td><td>12</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>3</td><td>#</td><td></td><td>12524</td><td></td><td></td><td></td><td></td><td></td><td>24 19</td></tr><tr><td>4</td><td>251</td><td>24 323</td><td>11</td><td>五</td><td>19</td><td></td><td></td><td></td><td>720 3</td></tr><tr><td>5</td><td>720 95</td><td>360 1427</td><td>30 133</td><td>360 241</td><td>720 173</td><td>3</td><td></td><td></td><td>160 863</td></tr><tr><td>6</td><td>288 19087</td><td>1440 2713</td><td>240 15487</td><td>720 586</td><td>1440 6737</td><td>160 263</td><td>863</td><td></td><td>60480 275</td></tr><tr><td></td><td>60480</td><td>2520</td><td>20160</td><td>945</td><td>20160</td><td>2520</td><td>60480</td><td></td><td>24192</td></tr><tr><td>7</td><td>5257 17280</td><td>139849 120960</td><td>4511 4480</td><td>123133 120960</td><td>88547 120960</td><td>1537 4480</td><td>11351 120960</td><td>275 24192</td><td>33953 3628800</td></tr></table>

where the error constant is equal to $\begin{array} { r } { C = \frac { 5 } { 1 2 } } \end{array}$ . The values for the Adams– Bashforth methods are given in Table 244(I) and for the Adams–Moulton methods in Table 244(II).

The Adams methods are usually implemented in ‘predictor–corrector’ form. That is, a preliminary calculation is carried out using the Bashforth form of the method. The approximate solution at a new step value is then used to evaluate an approximation to the derivative value at the new point. This derivative approximation is then used in the Moulton formula in place of the derivative at the new point. There are many alternatives as to what is done next, and we will describe just one of them. Let $y _ { n } ^ { * }$ denote the approximation to $y ( x _ { n } )$ found during the Bashforth part of the step calculation and $y _ { n }$ the improved approximation found in the Moulton part of the step. Temporarily denote by $\beta _ { i } ^ { * }$ the value of $\beta _ { i }$ in the Bashforth formula so that $\beta _ { i }$ will denote only the Moulton coefficient. The value of $k$ corresponding to the Bashforth formula will be denoted here by $k ^ { * }$ . Usually $k$ and $k ^ { * }$ are related by $k ^ { * } = k + 1$ so that both formulae have the same order $p = k + 1$ .

In the Bashforth stage of the calculation we compute

$$
y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k ^ { * } } \beta _ { i } ^ { * } f ( x _ { n - i } , y _ { n - i } ) ,
$$

and in the Moulton stage

$$
y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f ( x _ { n } , y _ { n } ^ { * } ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ) .
$$

Methods of this type are referred to as ‘predictor–corrector’ methods because the overall computation in a step consists of a preliminary prediction of the answer followed by a correction of this first predicted value. The use of (244a) and (244b) requires two calculations of the function $f$ in each step of the computation. Such a scheme is referred to as being in ‘predict–evaluate– correct–evaluate’ or ‘PECE’ mode. An alternative scheme in which the second evaluation is never performed is said to be in ‘predict–evaluate–correct’ or ‘PEC’ mode. In this mode, every occurrence of $f ( x _ { n - i } , y _ { n - i } )$ would need to be replaced by $f ( x _ { n - i } , y _ { n - i } ^ { * } )$ , and would represent the value of a derivative evaluated in a previous step but based on the predicted approximation to $y ( x _ { n - i } )$ in that step. Thus, (244a) and (244b) would be replaced by

$$
y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k ^ { * } } \beta _ { i } ^ { * } f ( x _ { n - i } , y _ { n - i } ^ { * } )
$$

and

$$
y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f ( x _ { n } , y _ { n } ^ { * } ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ^ { * } ) .
$$

In addition to PEC and PECE modes it is also possible to have PECEC and PECECE and, more generally $\mathrm { P ( E C ) } ^ { k }$ and $\mathrm { P ( E C ) } ^ { k } \mathrm { E }$ , modes, in which corrections and evaluations are done repeatedly. Using this same type of terminology, $\mathrm { P ( E C ) ^ { \infty } }$ indicates iteration to convergence.

# 245 The Milne device

A feature of predictor–corrector methods is that two approximations to $y ( x _ { n } )$ are found in each step and each of these possesses different error constants, even though they might have the same order $p$ . Denote the error constant for the Adams–Bashforth $p$ -step method, as given in Table 244(I), by $C _ { p } ^ { * }$ , and the corresponding error constant for the $( p - 1 )$ -step Adams–Moulton method, as given in Table 244(II), by $C _ { p - 1 }$ . This means that the error in $y _ { n } ^ { * }$ , assuming that previous step values are exact, is equal to

$$
y _ { n } ^ { * } = y ( x _ { n } ) - h ^ { p + 1 } C _ { p } ^ { * } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

Of course, the previous values will not be exact, but we can interpret (245a) in the general case as the new error introduced into step $n$ . Similarly, we can interpret the corresponding formula for the error in the $( p - 1 )$ -step Adams– Moulton method as representing the error introduced into the corrected value of step $n$ . The formula for the Adams–Moulton method is

$$
y _ { n } = y ( x _ { n } ) - h ^ { p + 1 } C _ { p - 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

By calculating the difference of the predicted and corrected approximations and multiplying by an appropriate factor, we can estimate the error in the corrected value. That is,

$$
y ( x _ { n } ) - y _ { n } \approx \frac { C _ { p - 1 } } { C _ { p - 1 } - C _ { p } ^ { * } } ( y _ { n } ^ { * } - y _ { n } ) .
$$

This device, credited to Milne (1926), is used in practical algorithms to estimate local truncation errors for stepsize control. In some modern implementations, the order of the predictor is one lower than that of the corrector, and the Milne device loses the natural significance that we have described. However, it is still found to be a useful tool for adapting a numerical computation to the behaviour of the solution.

# 246 Starting methods

For a $k$ -step method, where $k > 1$ , something special has to be done in the first $k - 1$ steps. The method itself gives an algorithm for computing $y _ { k }$ in terms of $y _ { 0 }$ , $y _ { 1 }$ , $\cdot \cdot \cdot$ , $y _ { k - 1 }$ , and then $y _ { k + 1 }$ in terms of $y _ { 1 }$ , $y _ { 2 }$ , $\cdot \cdot \cdot$ , $y _ { k }$ , with all subsequent approximations found in a similar manner. However, it must be considered how $y _ { 1 }$ , $y _ { 2 }$ , . . . , $y _ { k - 1 }$ are to be found before the later steps can be evaluated.

It would be possible to evaluate the first $k - 1$ approximations using a sequence of low order methods. However, this would introduce serious errors which would nullify all the advantages of the later use of a method of high order. It would also be possible to use a Runge–Kutta method for the first $k - 1$ steps. As long as the Runge–Kutta method has the same order as the linear $k$ -step method to be used for the later steps, then there will be no overall order loss.

In the numerical experiments to be reported in the following subsection, a simple technique is used to retain the use of a single predictor–corrector method, and at the same time to maintain the long term order during the starting process. It is intended that the results should be straightforward and easy to understand, without the influence of alternative methods used in the early steps. What we do is to introduce, as unknowns to be computed, approximations to the values of $f ( x _ { i } , y _ { i } )$ , for $i = - ( k - 1 ) , - ( k - 2 ) , \ldots , - 1$ . Initial values for these quantities are chosen as $f ( x _ { i - 1 } , y _ { i - 1 } ) = f ( x _ { 0 } , y _ { 0 } )$ . With these values available, it is possible to carry out the computations in turn of $y _ { i }$ and of $f ( x _ { i } , y _ { i } )$ for $i = 1 , 2 , \ldots , k { - } 1$ . This then makes it possible to reverse the direction of integration, by changing the sign of $h$ used in the computations, and to recompute $y _ { i }$ and $f ( x _ { i } , y _ { i } )$ for $i = - 1 , - 2 , \ldots , - ( k - 1 )$ . This process of alternately integrating forwards and backwards can be repeated until convergence is achieved. Once this has happened, acceptable starting values will have been found to permit the step values numbered $i = k$ , $i = k + 1$ , . . . to be evaluated in turn.

![](images/1fc57f29f441978dd48f022d282239c7e271b43e00c33f0429c934f870f2f94c.jpg)  
Orbital calculations for various PEC methods

# 247 Numerical examples

Using the starting process described in Subsection 246, and a range of orders, the same test problem as was used in Subsection 239, that is, (201d) with $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ , was solved for PEC and PECE Adams methods. The errors generated for these methods are shown in Figures 247(i) (PEC methods) and 247(ii) (PECE methods). The orders are attached to the curves. Note that, at least for this problem, the two modes have almost identical errors. This means, perhaps, that the extra cost of PECE methods is not justified. However, for large stepsizes, there is an advantage in PECE methods because many types of unstable behaviour exhibit themselves more severely for PEC methods. For example, the iterative starting procedure that we have used, failed to converge for large stepsizes (not shown in the diagrams). This effect persisted for a larger range of stepsizes for PEC methods than was the case for PECE methods.

![](images/5494bcf92a7d4a8c5fbd9582959ba818cc37b03bd70df79100959d8ada89343b.jpg)  
Orbital calculations for various PECE methods

# Exercises 24

24.1 Find a linear multistep method of order 3 of the form

$$
y _ { n } = y _ { n - 2 } + \beta _ { 1 } h f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } h f ( x _ { n - 2 } , y _ { n - 2 } ) + \beta _ { 3 } h f ( x _ { n - 3 } , y _ { n - 2 } ) .
$$

24.2 Find a linear multistep method of order 3 of the form

$$
y _ { n } = y _ { n - 2 } + \beta _ { 0 } h f ( x _ { n } , y _ { n } ) + \beta _ { 1 } h f ( x _ { n - 1 , y _ { n - 1 } } ) + \beta _ { 2 } h f ( x _ { n - 2 } , y _ { n - 2 } ) .
$$

24.3 If the differential equation $y ^ { \prime } = y$ is solved using the implicit method $y _ { n } = y _ { n - 2 } + 2 h f ( x _ { n - 1 } , y _ { n - 1 } )$ , show that the resulting difference equation has a solution which grows in powers of $1 + h + \textstyle { \frac { 1 } { 2 } } h ^ { 2 } + O ( h ^ { 3 } )$ and a second solution that grows in powers of a quantity with smaller magnitude.

24.4 If the differential equation $y ^ { \prime } = - y$ is solved using the same method, show that the resulting difference equation has a solution which grows in powers of $\textstyle 1 - h + { \frac { 1 } { 2 } } h ^ { 2 } + O ( h ^ { 3 } )$ but has a second solution that grows in powers of a quantity with greater magnitude.

# 25 Taylor Series Methods

# 250 Introduction to Taylor series methods

A differential equation $y ^ { \prime } ( x ) = f ( x , y ( x ) )$ , characterized by the function $f$ , is presented to a computer in the form of a procedure, function or subroutine for computing values of $f ( u , v )$ for given arguments $u$ and $v$ . The program carries out the evaluation of this procedure in a manner that exactly corresponds to the occurrence of the function $f$ , in the mathematical formulation of the numerical method. In this brief introduction, we consider the use of procedures that evaluate, for given values of $x$ and $y ( x )$ , not only the value of $y ^ { \prime } ( x )$ , but also the value of $y ^ { \prime \prime } ( x )$ and possibly also $y ^ { \prime \prime \prime } ( x )$ and other higher derivatives.

With such facilities available, there is a wide range of possible methods, but the natural and straightforward choice of Taylor series is almost always followed. By repeated differentiation, we can find functions $f _ { 2 } ( x , y ( x ) )$ , $f _ { 3 } ( x , y ( x ) ) ,$ . . . , $f _ { m } ( x , y ( x ) )$ , which give values, respectively, of $y ^ { \prime \prime } ( x )$ , $y ^ { \prime \prime \prime } ( x )$ , . . . , $y ^ { ( m ) } ( x )$ .

The order $m$ formula for computing $y ( x _ { n } ) \ = \ y ( x _ { n - 1 } + h )$ using these functions, evaluated at $x = x _ { n - 1 }$ and $y = y _ { n - 1 }$ , is

$$
y _ { n } = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) + { \frac { h ^ { 2 } } { 2 ! } } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } )
$$

Most serious investigations of this method have been concerned, above all, with the automatic generation of procedures for generating the second, third, . . derivative functions $f _ { 2 }$ , $f _ { 3 }$ , . . . from a given first derivative function $f$ . While this aspect of the Taylor series method is more within the scope of algebraic manipulation than of numerical analysis, there are other important aspects which arise, just as for other methods. These include error estimation, order selection and stepsize control.

Although many individuals and teams have made important contributions to the use of Taylor series methods, we mention three in particular. The program of Gibbons (1960), using a computer with the limited memory available at that time, used a recursive technique to generate the Taylor coefficients automatically. A similar approach using greater sophistication and more powerful computational tools was used by Barton, Willers and Zahar (1971). The work of Moore (1964) is especially interesting, in that it uses interval arithmetic and supplies rigorous error bounds for the computed solution.

# 251 Manipulation of power series

We consider problems for which the components of the function $f$ are rational in $x$ and in the components of $y$ . This means that the terms occurring in (250a) can all be computed by the use of addition (and subtraction), multiplication and division.

We use power series with the $1 / i$ ! factor absorbed into the coefficient of $f _ { i } ( x _ { n - 1 } , y _ { n - 1 } )$ . Hence each component takes the form $a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot +$ $a _ { m } h ^ { m }$ . If a second such expansion, $b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m }$ , is added or subtracted, then we simply add or subtract corresponding coefficients. The product of two terms is found by expanding the formal product but truncating after the $h ^ { m }$ term. This means that the product of $a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + a _ { m } h ^ { m }$ and $b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m }$ would be $c _ { 0 } + c _ { 1 } h + c _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + c _ { m } h ^ { m }$ , where

$$
c _ { i } = \sum _ { j = 0 } ^ { i } a _ { i - j } b _ { j } , \qquad i = 0 , 1 , \ldots , m .
$$

The formula for the quotient

$$
a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + a _ { m } h ^ { m } \approx { \frac { c _ { 0 } + c _ { 1 } h + c _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + c _ { m } h ^ { m } } { b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m } } }
$$

is found by reinterpreting the relationship between the $a _ { i }$ , $b _ { i }$ and $c _ { i }$ coefficients in (251a) to give

$$
a _ { i } = \left\{ \begin{array} { l l } { \frac { c _ { 0 } } { b _ { 0 } } , ~ i = 0 , } \\ { \frac { c _ { i } - \sum _ { j = 1 } ^ { i } a _ { i - j } b _ { j } } { b _ { 0 } } , ~ i = 1 , 2 , . . . , m . } \end{array} \right.
$$

Given a system of differential equations with dependent variables $y ^ { 1 }$ , $y ^ { 2 }$ , $\ldots , \ y ^ { N }$ , write the truncated power series for $y ^ { k } ( x _ { n - 1 } + h )$ in the form $y _ { 0 } ^ { k } + h y _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { k }$ , $k = 1 , 2 , \ldots , N$ . Also denote the power series for component $k$ of $f ( x _ { n - 1 } , Y )$ by $f _ { 0 } ^ { k } + h f _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } f _ { m } ^ { k }$ , where the vector $Y$ has its components substituted by the series $y _ { 0 } ^ { l } + h y _ { 1 } ^ { l } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { l }$ , $l = 1 , 2 , \ldots , N$ .

We consider how to evaluate in turn the $y _ { i } ^ { k }$ coefficients for each $k \mathbf { \Sigma } =$ $1 , 2 , \ldots , N$ , with $i$ taking on values from $0$ to $m$ . For $i \ = \ 0$ , all the $y _ { i } ^ { k }$ are known from initial information at the start of the current step. For each value of $i > 0$ we already know the coefficients $y _ { j } ^ { k }$ for all $k$ and for all $j < i$ . It is thus possible to evaluate the $h ^ { i - 1 }$ terms in the components in the power series for $f ( x _ { n - 1 } + h , y _ { n - 1 } )$ . Writing the differential equation in the form

$$
\begin{array} { r } { \frac { d } { d h } ( y _ { 0 } ^ { k } + h y _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { k } ) = y _ { 1 } ^ { k } + 2 h y _ { 2 } ^ { k } + \cdot \cdot \cdot + m h ^ { m - 1 } y _ { m } ^ { k } } \\ { = f _ { 0 } ^ { k } + h f _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m - 1 } f _ { m - 1 } ^ { k } , } \end{array}
$$

where the last term on the right-hand side has been deleted, we see that $y _ { i } ^ { k } = f _ { i - 1 } ^ { k } / i$ .

When we have reached $i = m$ , all the required coefficients are known at $x = x _ { n - 1 }$ , and it is possible to take the step to $x = x _ { n }$ .

This method of solution will be illustrated in the next subsection.

# 252 An example of a Taylor series solution

We consider the example problem, already introduced in Subsection 201,

$$
y ^ { \prime } ( x ) = { \frac { y + x } { y - x } } , \qquad y ( 0 ) = 1 .
$$

Algorithm $\mathbf { 2 5 2 } \alpha$ A Taylor step for problem (252a)   

<table><tr><td>a(1)=y; b(1)= y + x; c(1)= y - x; for i=O:m- 1, temp = b(i+1); for j= 1:i, temp = temp - d(1+i-j)*c(1+j); end; d(i+1)= temp/c(1); a(i+2)= d(i+1)/(i+1); if i == 0, b(i+2)= a(i+2) + 1; c(i+2)= a(i+2) - 1; else b(i+2)= a(i+2); c(i+2)= a(i+2); end; end; x=x+h;</td></tr></table>

Let $a _ { 0 } , a _ { 1 } , \ldots , a _ { m }$ denote Taylor coefficients for $y ( x _ { n - 1 } + h )$ , $b _ { 0 } , b _ { 1 } , \ldots , b _ { m }$ be the corresponding coefficients for $y + x$ , and $c _ { 0 } , c _ { 1 } , \ldots , c _ { m }$ be the coefficients for $y - x$ . If $d _ { 0 } , d _ { 1 } , \ldots , d _ { m }$ are the coefficients for $( y + x ) / ( y - x )$ , then Algorithm $2 5 2 \alpha$ , written in MATLAB, can be used to update the value of $x \ = \ x _ { n - 1 }$ and $y = y _ { n - 1 }$ to the values at the end of a step, $x = x _ { n }$ , $y = y _ { n }$ . Note that $a _ { 0 } , a _ { 1 } , \ldots , a _ { m }$ are represented in this program by $\mathsf { a } ( 1 )$ , a(2), . . . , $\mathsf { a } \left( \mathtt { m } ^ { + 1 } \right)$ , because MATLAB subscripts start from 1 (and similarly for the $b _ { i }$ , etc.).

Numerical experiments based on this program have been made for a sequence of $m$ values from 1 to 10 and using stepsizes $h = 0 . 1 0 \times 2 ^ { - k }$ , with $k = 1 , 2 , \ldots .$ . The errors in the approximations to $y ( 0 . 5 )$ are presented in Figure 252(i). It can be seen that the rate of increase in accuracy, as smaller and smaller steps are taken, becomes more and more impressive as $m$ increases. The results found for $m = 9$ and $m = 1 0$ are not included because, even for 10 steps with $h = 0 . 0 5$ , the numerical results in these cases are accurate to approximately 15 decimal places.

![](images/8c5bea5252a96e8713163da748b07e949917b6e4235ee870fc261e0bd359d7fc.jpg)  
Taylor series calculations

![](images/257fdd7d955ce6611a3e81d089c5b55613a343c1d171d3cdeed690ecc5ecfbbd.jpg)  
Taylor series calculations with cost correction

Since high values of $m$ are more time-consuming, the favourable impression of their advantages shown in this figure is an exaggeration. Since the cost is approximately proportional to $m$ , a fairer comparison would be to plot the errors against $h / m$ . This weighted comparison is shown in Figure 252(ii).

The advantage of high order methods over low order methods is still evident from this more balanced comparison.

Coefficients defined by (253c)   

<table><tr><td>m</td><td>α1</td><td>α2</td><td>Q3</td><td>α4</td><td>β1</td><td>β2</td><td>β</td><td>β4</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>3-21-215265</td><td>花</td><td></td><td></td><td>中</td><td></td><td>49</td><td></td></tr><tr><td></td><td></td><td>10</td><td>3</td><td></td><td></td><td></td><td>120</td><td></td></tr><tr><td>4</td><td></td><td>515</td><td>107</td><td></td><td></td><td></td><td>239</td><td>117</td></tr><tr><td></td><td></td><td></td><td></td><td>769</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td>28</td><td>28</td><td>1680</td><td></td><td>28</td><td>84</td><td>560</td></tr></table>

Coefficients defined by (253d)   

<table><tr><td>m</td><td>1</td><td>72</td><td>73</td><td>4</td><td>81</td><td>82</td><td>83</td><td>84</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>中</td><td>1</td><td></td><td></td><td>立共</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td>面</td><td></td><td></td><td></td><td>路 1</td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>1680</td><td></td><td></td><td></td><td>1680</td></tr></table>

# 253 Other methods using higher derivatives

We consider the possibility of using higher derivative information at more than one step value. In particular, we consider two special schemes of the form

$$
\begin{array} { c } { { y _ { n } = y _ { n - 1 } + h \alpha _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + h ^ { 2 } \alpha _ { 2 } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot } } \\ { { + h ^ { m } \alpha _ { m } f _ { m } ( x _ { n - 1 } , y _ { n - 1 } ) + h \beta _ { 1 } f ( x _ { n - 2 } , y _ { n - 2 } ) } } \\ { { + h ^ { 2 } \beta _ { 2 } f _ { 2 } ( x _ { n - 2 } , y _ { n - 2 } ) + \cdot \cdot \cdot + h ^ { m } \beta _ { m } f _ { m } ( x _ { n - 2 } , y _ { n - 2 } ) } } \end{array}
$$

and

$$
\begin{array} { c } { y _ { n } = y _ { n - 1 } + h \gamma _ { 1 } f ( x _ { n } , y _ { n } ) + h ^ { 2 } \gamma _ { 2 } f _ { 2 } ( x _ { n } , y _ { n } ) + \cdot \cdot \cdot } \\ { \qquad + h ^ { m } \gamma _ { m } f _ { m } ( x _ { n } , y _ { n } ) + h \delta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) } \\ { \qquad + h ^ { 2 } \delta _ { 2 } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + h ^ { m } \delta _ { m } f _ { m } ( x _ { n - 1 } , y _ { n - 1 } ) . } \end{array}
$$

The scheme (253a) uses information already available before step $n$ is attempted. Thus it can be regarded as a generalization of an Adams–Bashforth method. In contrast, the scheme (253b) is fully implicit, and thus corresponds to an Adams–Moulton method. Using Taylor series analyses, conditions for order $2 m$ can readily be found. These are equivalent to the conditions