c. Use Taylor's method of order four with $h = 0 . 1$ to approximate the solution, and compare it with the actual values of $y$   
d. Use the answers generated in part (c) and piecewise cubic Hermite interpolation to ap-proximate y at the following values,and compare them to the actual values of $y$ ·

iy(1.04) ii.y(1.55) ii.y(1.97)

6. Given the initial-value problem

$$
y ^ { \prime } = { \frac { 1 } { t ^ { 2 } } } - { \frac { y } { t } } - y ^ { 2 } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = - 1 ,
$$

with exact solution $y ( t ) = - 1 / t$ ：

a. Use Taylor's method of order two with $h = 0 . 0 5$ to approximate the solution, and com-pare it with the actual values of $\boldsymbol { y }$ ·   
b. Use the answers generated in part (a) and linear interpolation to approximate the following values of y,and compare them to the actual values. i.y(1.052) ii.y(1.555) iii.y(1.978)   
c. Use Taylor's method of order four with $h = 0 . 0 5$ to approximate the solution, and com-pare it with the actual values of $\boldsymbol { y }$ ·   
d. Use the answers generated in part (c) and piecewise cubic Hermite interpolation to ap-proximate the following values of y,and compare them to the actual values.

i $\mathbf { y } ( 1 . 0 5 2 )$ $\begin{array} { r l } { \mathbf { i i } . \quad } & { { } y ( 1 . 5 5 5 ) } \end{array}$ ii.y(1.978)

7.A projectile of mass m = 0.11 kg shot vertically upward with initial velocity v(O) = 8 m/s is slowed due to the force of gravity, $F _ { g } = - m g$ , and due to air resistance, $F _ { r } = - k \nu | \nu \vert$ ，where $g = 9 . 8 \mathrm { m } / \mathrm { s } ^ { 2 }$ and $k = 0 . 0 0 2 \mathrm { k g / m }$ .The differential equation for the velocity $v$ is given by

$$
m v ^ { \prime } = - m g - k v | v | .
$$

a. Find the velocity after 0.1, 0.2,...,1.0 s.

b. To the nearest tenth of a second, determine when the projectile reaches its maximum height and begins falling.

# 5.4 Runge-Kutta Methods

The Taylor methods outlined in the previous section have the desirable property of highorder local truncation error, but the disadvantage of requiring the computation and evaluation of the derivatives of $f ( t , y )$ . This is a complicated and time-consuming procedure for most problems, so the Taylor methods are seldom used in practice.

Runge-Kutta methods have the high-order local truncation error of the Taylor meth-ods while eliminating the need to compute and evaluate the derivatives of $f ( t , y )$ . Before presenting the ideas behind their derivation, we need to state Taylor's Theorem in two variables.The proof of this result can be found in any standard book on advanced calculus (see, for example, $[ \mathrm { F u } , \mathfrak { p } . 3 3 1 ] ,$ .

Suppose that $f ( t , y )$ and all its partial derivatives of order less than or equal to $n + 1$ are continuous on $D = \{ \ ( t , y ) \mid a \leq t \leq b , c \leq y \leq d \}$ ,and let $( t _ { 0 } , y _ { 0 } ) \in D$ . For every $( t , y ) \in D$ , there exists $\pmb { \xi }$ between $t$ and $t _ { 0 }$ and $\mu$ between $\textbf { y }$ and $y _ { 0 }$ with

$$
f ( t , y ) = P _ { n } ( t , y ) + R _ { n } ( t , y ) ,
$$

where

$$
\begin{array} { l } { { P _ { n } ( t , y ) = f ( t _ { 0 } , y _ { 0 } ) + \displaystyle \left[ ( t - t _ { 0 } ) \frac { \partial f } { \partial t } ( t _ { 0 } , y _ { 0 } ) + ( y - y _ { 0 } ) \frac { \partial f } { \partial y } ( t _ { 0 } , y _ { 0 } ) \right] } } \\ { { \displaystyle ~ + \left[ \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 } \frac { \partial ^ { 2 } f } { \partial t ^ { 2 } } ( t _ { 0 } , y _ { 0 } ) + ( t - t _ { 0 } ) ( y - y _ { 0 } ) \frac { \partial ^ { 2 } f } { \partial t \partial y } ( t _ { 0 } , y _ { 0 } ) \right. } } \\ { { \displaystyle ~ \left. + \frac { ( y - y _ { 0 } ) ^ { 2 } } { 2 } \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } ( t _ { 0 } , y _ { 0 } ) \right] + \cdots } } \\ { { \displaystyle ~ + \left[ \frac { 1 } { n ! } \sum _ { j = 0 } ^ { n } \binom { n } { j } ( t - t _ { 0 } ) ^ { n - j } ( y - y _ { 0 } ) ^ { j } \frac { \partial ^ { n } f } { \partial t ^ { n - j } \partial y ^ { j } } ( t _ { 0 } , y _ { 0 } ) \right] } } \end{array}
$$

and

$$
R _ { n } ( t , y ) = { \frac { 1 } { ( n + 1 ) ! } } \sum _ { j = 0 } ^ { n + 1 } { \binom { n + 1 } { j } } ( t - t _ { 0 } ) ^ { n + 1 - j } ( y - y _ { 0 } ) ^ { j } { \frac { \partial ^ { n + 1 } f } { \partial t ^ { n + 1 - j } \partial y ^ { j } } } ( \xi , \mu ) .
$$

The function $P _ { n } ( t , y )$ is called the nth Taylor polynomial in two variables for the function $f$ about $( t _ { 0 } , y _ { 0 } )$ , and $R _ { n } ( t , y )$ is the remainder term associated with $P _ { n } ( t , y )$

Figure 5.4 on page 274 shows the graph of the function

$$
f ( t , y ) = \exp \left[ - \frac { ( t - 2 ) ^ { 2 } } { 4 } - \frac { ( y - 3 ) ^ { 2 } } { 4 } \right] \cos ( 2 t + y - 7 )
$$

together with the second Taylor polynomial of $f$ about (2,3), the polynomial in two variables

$$
P _ { 2 } ( t , y ) = 1 - \frac { 9 } { 4 } ( t - 2 ) ^ { 2 } - 2 ( t - 2 ) ( y - 3 ) - \frac { 3 } { 4 } ( y - 3 ) ^ { 2 } .
$$

The differentiation required to determine this polynomial would be tedious to do by hand. Fortunately, there is a Maple procedure to do the work for us.First we need to initiate the multiple variable Taylor polynomial procedure by entering the command

>readlib(mtaylor);

which produces the response proc()... end proc

The Taylor polynomial we need in this example is found by issuing the command >mtaylor(exp(-(t-2)^2/4-(y-3)^2/4)\*cos(2\*t+y-7), $[ t = 2$ ， $y = 3 ]$ ,3)；

The final parameter in this command indicates that we want the second multivariate Taylor polynomial, that is, the quadratic polynomial.If this parameter is 2, we get the linear polynomial,and if it is 1, we get the constant polynomial. When this parameter is omitted, it defaults to 6and gives the fifth Taylor polynomial.

The response from this Maple command is the polynomial

$$
1 - \frac 9 4 ( t - 2 ) ^ { 2 } - 2 ( t - 2 ) ( y - 3 ) - \frac 3 4 ( y - 3 ) ^ { 2 } .
$$

![](images/6f10c77785afe2268fc0e11f5818856191ce4c39b7b4a596490119af8946db43.jpg)  
Figure 5.4

The first step in deriving a Runge-Kutta method is to determine values for $a _ { 1 } , \alpha _ { 1 }$ ,and $\beta _ { 1 }$ with the property that $a _ { 1 } f ( t + \alpha _ { 1 } , y + \beta _ { 1 } )$ approximates

$$
T ^ { ( 2 ) } ( t , y ) = f ( t , y ) + \frac { h } { 2 } f ^ { \prime } ( t , y ) ,
$$

with error no greater than $O ( h ^ { 2 } )$ , the local truncation error for the Taylor method of order two. Since

$$
f ^ { \prime } ( t , y ) = { \frac { d f } { d t } } ( t , y ) = { \frac { \partial f } { \partial t } } ( t , y ) + { \frac { \partial f } { \partial y } } ( t , y ) \cdot y ^ { \prime } ( t ) \quad { \mathrm { ~ a n d ~ } } \quad y ^ { \prime } ( t ) = f ( t , y ) ,
$$

this implies

$$
T ^ { ( 2 ) } ( t , y ) = f ( t , y ) + { \frac { h } { 2 } } { \frac { \partial f } { \partial t } } ( t , y ) + { \frac { h } { 2 } } { \frac { \partial f } { \partial y } } ( t , y ) \cdot f ( t , y ) .
$$

Expanding $f ( t + \pmb { \alpha } _ { 1 } , y + \pmb { \beta } _ { 1 } )$ in its Taylor polynomial of degree one about $( t , y )$ gives

$$
\begin{array} { l } { { \displaystyle a _ { 1 } f ( t + \alpha _ { 1 } , y + \beta _ { 1 } ) = a _ { 1 } f ( t , y ) + a _ { 1 } \alpha _ { 1 } \frac { \partial f } { \partial t } ( t , y ) } } \\ { { \displaystyle ~ + a _ { 1 } \beta _ { 1 } \frac { \partial f } { \partial y } ( t , y ) + a _ { 1 } \cdot R _ { 1 } ( t + \alpha _ { 1 } , y + \beta _ { 1 } ) , } } \end{array}
$$

where

$$
R _ { 1 } ( t + \alpha _ { 1 } , y + \beta _ { 1 } ) = \frac { \alpha _ { 1 } ^ { 2 } } { 2 } \frac { \partial ^ { 2 } f } { \partial t ^ { 2 } } ( \xi , \mu ) + \alpha _ { 1 } \beta _ { 1 } \frac { \partial ^ { 2 } f } { \partial t \partial y } ( \xi , \mu ) + \frac { \beta _ { 1 } ^ { 2 } } { 2 } \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } ( \xi , \mu ) ,
$$

for some $\pmb { \xi }$ between $t$ and $\pmb { t } + \pmb { \alpha } _ { 1 }$ and $\mu$ between $y$ and $y + \beta _ { 1 }$

Matching the coefficients of $f$ and its derivatives in Eqs. (5.18) and (5.19) gives the three equations

$$
f ( t , y ) : \quad a _ { 1 } = 1 ; \qquad { \frac { \partial f } { \partial t } } ( t , y ) : \quad a _ { 1 } \alpha _ { 1 } = { \frac { h } { 2 } } ;
$$

and

$$
\frac { \partial f } { \partial t } ( t , y ) : \quad a _ { 1 } \beta _ { 1 } = \frac { h } { 2 } f ( t , y ) .
$$

The parameters $a _ { 1 } , \alpha _ { 1 }$ ,and $\beta _ { 1 }$ are uniquely determined to be

$$
a _ { 1 } = 1 , \quad \alpha _ { 1 } = \frac h 2 , \quad \mathrm { a n d } \quad \beta _ { 1 } = \frac h 2 f ( t , y ) ;
$$

so

$$
T ^ { ( 2 ) } ( t , y ) = f \left( t + { \frac { h } { 2 } } , y + { \frac { h } { 2 } } f ( t , y ) \right) - R _ { 1 } \left( t + { \frac { h } { 2 } } , y + { \frac { h } { 2 } } f ( t , y ) \right) ,
$$

and from Eq.(5.20),

$$
\begin{array} { l } { { \displaystyle R _ { 1 } \left( t + \frac { h } { 2 } , y + \frac { h } { 2 } f ( t , y ) \right) = \frac { h ^ { 2 } } { 8 } \frac { \partial ^ { 2 } f } { \partial t ^ { 2 } } ( \xi , \mu ) + \frac { h ^ { 2 } } { 4 } f ( t , y ) \frac { \partial ^ { 2 } f } { \partial t \partial y } ( \xi , \mu ) } } \\ { { \displaystyle \qquad + \frac { h ^ { 2 } } { 8 } ( f ( t , y ) ) ^ { 2 } \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } ( \xi , \mu ) . } } \end{array}
$$

If all the second-order partial derivatives of $f$ are bounded, then

$$
R _ { 1 } \left( t + { \frac { h } { 2 } } , y + { \frac { h } { 2 } } f ( t , y ) \right)
$$

is $O ( h ^ { 2 } )$ , the order of the local truncation error of Taylor method of order two. As a consequence,using the new procedure in place of the Taylor method of order two might add error, but it does not increase the order of the error.

The difference-equation method resulting from replacing $T ^ { ( 2 ) } ( t , y )$ in Taylor's method of order two by $f ( t + ( h / 2 ) , y + ( h / 2 ) f ( t , y ) )$ is a specific Runge-Kutta method known as the Midpoint method.

# Midpoint Method:

wo = α,

$$
\begin{array} { r c l } { { } } & { { \sec = \infty , } } & { { , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { w _ { i + 1 } = w _ { i } + h f \left( t _ { i } + \displaystyle \frac { h } { 2 } , w _ { i } + \displaystyle \frac { h } { 2 } f ( t _ { i } , w _ { i } ) \right) , } } & { { \mathrm { f o r } \operatorname { e a c h } i = 0 , 1 , \ldots , N - 1 . } } \end{array}
$$

Since only three parameters are present in $a _ { 1 } f ( t + \alpha _ { 1 } , y + \beta _ { 1 } )$ and all are needed in the match of $\hat { T } ^ { ( 2 ) }$ , we need a more complicated form to satisfy the conditions required for any of the higher-order Taylor methods.

The most appropriate four-parameter form for approximating

$$
T ^ { ( 3 ) } ( t , y ) = f ( t , y ) + \frac { h } { 2 } f ^ { \prime } ( t , y ) + \frac { h ^ { 2 } } { 6 } f ^ { \prime \prime } ( t , y )
$$

is

$$
a _ { 1 } f ( t , y ) + a _ { 2 } f ( t + \alpha _ { 2 } , y + \delta _ { 2 } f ( t , y ) ) ;
$$

and even with this, there is insuficient flexibility to match the term

$$
\frac { h ^ { 2 } } { 6 } \left[ \frac { \partial f } { \partial y } ( t , y ) \right] ^ { 2 } f ( t , y ) ,
$$

resulting from the expansion of $( h ^ { 2 } / 6 ) f ^ { \prime \prime } ( t , y )$ . Consequently, the best that can be obtained from using (5.21) are methods with $O ( h ^ { 2 } )$ local truncation error. The fact that (5.21) has four parameters, however, gives a flexibility in their choice, so a number of $O ( h ^ { 2 } )$ methods can be derived. One of the most important is the Modifed Euler method, which corresponds to choosing $\begin{array} { r } { a _ { 1 } = a _ { 2 } = \frac { 1 } { 2 } } \end{array}$ and $\alpha _ { 2 } = \delta _ { 2 } = h$ and has the following difference-equation form.

# Modified Euler Method:

$$
\begin{array} { c } { { w _ { 0 } = \alpha , } } \\ { { \displaystyle } } \\ { { w _ { i + 1 } = w _ { i } + \frac { h } { 2 } [ f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i } + h f ( t _ { i } , w _ { i } ) ) ] , } } \end{array}
$$

$$
i = 0 , 1 , 2 , \ldots , N - 1 .
$$

The other important $O ( h ^ { 2 } )$ method is Heun's method, which corresponds to $\begin{array} { r } { a _ { 1 } = \frac { 1 } { 4 } , a _ { 2 } = } \end{array}$ $\frac { 3 } { 4 }$ ,and $\alpha _ { 2 } = \delta _ { 2 } = { \textstyle { \frac { 2 } { 3 } } } h$ , and has the following difference-equation form.

# Heun's Method:

$$
\begin{array} { c } { { w _ { 0 } = \alpha , } } \\ { { \displaystyle w _ { i + 1 } = w _ { i } + \frac { h } { 4 } [ f ( t _ { i } , w _ { i } ) + 3 f ( t _ { i } + \frac { 2 } { 3 } h , w _ { i } + \frac { 2 } { 3 } h f ( t _ { i } , w _ { i } ) ) ] , } } \end{array}
$$

$$
i = 0 , 1 , 2 , \dots , N - 1 .
$$

Both are classified as Runge-Kutta methods of order two, the order of their local truncation error.

# EXAMPLE 2

Suppose we apply the Runge-Kutta methods of order two to our usual example,

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

with $N = 1 0 , h = 0 . 2 , t _ { i } = 0 . 2 i$ ,and $w _ { 0 } = 0 . 5$ in each case. The difference equations produced from the various formulas are

$$
w _ { i + 1 } = 1 . 2 2 w _ { i } - 0 . 0 0 8 8 i ^ { 2 } - 0 . 0 0 8 i + 0 . 2 1 8 \mathrm { . }
$$

Modified Euler method: $w _ { i + 1 } = 1 . 2 2 w _ { i } - 0 . 0 0 8 8 i ^ { 2 } - 0 . 0 0 8 i + 0 . 2 1 6 ;$

$$
w _ { i + 1 } = 1 . 2 2 w _ { i } - 0 . 0 0 8 8 i ^ { 2 } - 0 . 0 0 8 i + 0 . 2 1 7 \overline { { 3 } } ,
$$

for each $i = 0 , 1 , \ldots , 9$ . Table 5.5 lists the results of these calculations.Forthis problem, the Midpoint method is superior, followed by Heun's method. ?

Table 5.5   

<table><tr><td></td><td>y(t)</td><td>Midpoint Method</td><td>Error</td><td>Modified Euler Method</td><td>Error</td><td>Heun&#x27;s Method</td><td>Error</td></tr><tr><td>0.0</td><td>0.5000000</td><td>0.5000000</td><td>0</td><td>0.5000000</td><td>0</td><td>0.5000000</td><td>0</td></tr><tr><td>0.2</td><td>0.8292986</td><td>0.8280000</td><td>0.0012986</td><td>0.8260000</td><td>0.0032986</td><td>0.8273333</td><td>0.0019653</td></tr><tr><td>0.4</td><td>1.2140877</td><td>1.2113600</td><td>0.0027277</td><td>1.2069200</td><td>0.0071677</td><td>1.2098800</td><td>0.0042077</td></tr><tr><td>0.6</td><td>1.6489406</td><td>1.6446592</td><td>0.0042814</td><td>1.6372424</td><td>0.0116982</td><td>1.6421869</td><td>0.0067537</td></tr><tr><td>0.8</td><td>2.1272295</td><td>2.1212842</td><td>0.0059453</td><td>2.1102357</td><td>0.0169938</td><td>2.1176014</td><td>0.0096281</td></tr><tr><td>1.0</td><td>2.6408591</td><td>2.6331668</td><td>0.0076923</td><td>2.6176876</td><td>0.0231715</td><td>2.6280070</td><td>0.0128521</td></tr><tr><td>1.2</td><td>3.1799415</td><td>3.1704634</td><td>0.0094781</td><td>3.1495789</td><td>0.0303627</td><td>3.1635019</td><td>0.0164396</td></tr><tr><td>1.4</td><td>3.7324000</td><td>3.7211654</td><td>0.0112346</td><td>3.6936862</td><td>0.0387138</td><td>3.7120057</td><td>0.0203944</td></tr><tr><td>1.6</td><td>4.2834838</td><td>4.2706218</td><td>0.0128620</td><td>4.2350972</td><td>0.0483866</td><td>4.2587802</td><td>0.0247035</td></tr><tr><td>1.8</td><td>4.8151763</td><td>4.8009586</td><td>0.0142177</td><td>4.7556185</td><td>0.0595577</td><td>4.7858452</td><td>0.0293310</td></tr><tr><td>2.0</td><td>5.3054720</td><td>5.2903695</td><td>0.0151025</td><td>5.2330546</td><td>0.0724173</td><td>5.2712645</td><td>0.0342074</td></tr></table>

Although $T ^ { ( 3 ) } ( t , \mathfrak { y } )$ can be approximated with error $O ( h ^ { 3 } )$ by an expression of the form

$$
f ( t + \alpha _ { 1 } , y + \delta _ { 1 } f ( t + \alpha _ { 2 } , y + \delta _ { 2 } f ( t , y ) ) ) ,
$$

involving four parameters,the algebra involved in the determination of ${ \alpha } _ { 1 } , { \delta } _ { 1 } , { \alpha } _ { 2 }$ , and $\delta _ { 2 }$ is quite involved and will not be presented. In fact, the Runge-Kutt method of order three re-sulting from this expression is not generally used. The most common Runge-Kutta method in use is of order four and,indifference-equation form, is given by the following.

# Runge-Kutta Order Four:

$$
\begin{array} { l } { { w _ { 0 } = \alpha , } } \\ { { { k _ { 1 } } = h f ( t _ { i } , w _ { i } ) , } } \\ { { { k _ { 2 } } = h f \left( t _ { i } + { \displaystyle \frac { h } { 2 } } , w _ { i } + { \displaystyle \frac { 1 } { 2 } } k _ { 1 } \right) , } } \end{array}
$$

$$
\begin{array} { r c l } { { } } & { { } } & { { k _ { 3 } = h f \left( t _ { i } + \displaystyle \frac { h } { 2 } , w _ { i } + \displaystyle \frac { 1 } { 2 } k _ { 2 } \right) , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { k _ { 4 } = h f ( t _ { i + 1 } , w _ { i } + k _ { 3 } ) , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 } + 2 k _ { 2 } + 2 k _ { 3 } + k _ { 4 } ) , } } \end{array}
$$

for each $i = 0 , 1 , \ldots , N - 1$ . This method has local truncation error $O ( h ^ { 4 } )$ ，provided the solution $y ( t )$ has five continuous derivatives. The reason for introducing the notation $k _ { 1 } , k _ { 2 } , k _ { 3 } , k _ { 4 }$ into the method is to eliminate the need for successive nesting in the second variable of $f ( t , y )$ (see Exercise 17). Algorithm 5.2 implements the Runge-Kutta method of order four.

# Runge-Kutta (Order Four)

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

at $( N + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ：

INPUT endpoints $a , b$ ; integer $N$ ; initial condition $\pmb { \alpha }$

OUTPUTapproximation $w$ to $y$ at the $( N + 1 )$ values of $t$

Step 1 Se $\begin{array} { r l } & { \mathrm {  ~ t ~ } h = ( b - a ) / N ; } \\ & { \mathrm {  ~ \omega ~ } t = a ; } \\ & { \mathrm {  ~ \omega ~ } w = \alpha ; } \\ & { \mathrm {  ~ \omega ~ } J { \mathrm { T P U T } } \left( t , w \right) . } \end{array}$ OU

Step 2 For $i = 1 , 2 , \dots , N$ do Steps 3-5.

Step3 Set $\begin{array} { r c l } { { } } & { { } } & { { : K _ { 1 } = h f ( t , w ) ; } } \\ { { } } & { { } } & { { K _ { 2 } = h f ( t + h / 2 , w + K _ { 1 } / 2 ) ; } } \\ { { } } & { { } } & { { K _ { 3 } = h f ( t + h / 2 , w + K _ { 2 } / 2 ) ; } } \\ { { } } & { { } } & { { K _ { 4 } = h f ( t + h , w + K _ { 3 } ) . } } \end{array}$

Step 4 Set $w = w + ( K _ { 1 } + 2 K _ { 2 } + 2 K _ { 3 } + K _ { 4 } ) / 6 ; ( C o m p u t e ~ w _ { i } . )$ $t = a + i h . \ : ( C o m p u t e \ : t _ { i } . )$

Step 5OUTPUT $( t , w )$

Step 6 STOP.

Using the Runge-Kutt method of order four to obtain approximations to the solution of the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

with $h = 0 . 2$ ， $N = 1 0$ ,and $t _ { i } = 0 . 2 i$ gives the results and errors listed in Table 5.6.

Table 5.6   

<table><tr><td></td><td>Exact y=y(t）</td><td>Runge-Kutta Order Four Wi</td><td>Error lyi-wil</td></tr><tr><td>t 0.0</td><td>0.5000000</td><td>0.5000000</td><td>0</td></tr><tr><td>0.2</td><td>0.8292986</td><td>0.8292933</td><td>0.0000053</td></tr><tr><td>0.4</td><td>1.2140877</td><td>1.2140762</td><td>0.0000114</td></tr><tr><td>0.6</td><td>1.6489406</td><td>1.6489220</td><td>0.0000186</td></tr><tr><td>0.8</td><td>2.1272295</td><td>2.1272027</td><td>0.0000269</td></tr><tr><td>1.0</td><td>2.6408591</td><td>2.6408227</td><td>0.0000364</td></tr><tr><td>1.2</td><td>3.1799415</td><td>3.1798942</td><td>0.0000474</td></tr><tr><td>1.4</td><td>3.7324000</td><td>3.7323401</td><td>0.0000599</td></tr><tr><td>1.6</td><td>4.2834838</td><td>4.2834095</td><td>0.0000743</td></tr><tr><td>1.8</td><td>4.8151763</td><td>4.8150857</td><td>0.0000906</td></tr><tr><td>2.0</td><td>5.3054720</td><td>5.3053630</td><td>0.0001089</td></tr></table>

The main computational effort in applying the Runge-Kutt methods is the evaluation of $f$ . In the second-order methods, the local truncation error is $O ( h ^ { 2 } )$ ,and the cost is two functional evaluations per step. The Runge-Kutta method of order four requires 4 evalua-tions per step, and the local truncation error is $O ( h ^ { 4 } )$ : Butcher (see [But] for a summary) has established the relationship between the number of evaluations per step and the order of the local truncation error shown in Table 5.7.This table indicates why the methods of order less than five with smaller step size are used in preference to the higher-order methods using a larger step size.

# Table 5.7

<table><tr><td>Evaluations per step</td><td>2 3</td><td>4</td><td>5≤n≤7</td><td>8≤n≤9</td><td>10≤n</td></tr><tr><td>Best possible local truncation error</td><td>0(h2） 0（h3）</td><td>0(h4）</td><td>0(h~-1）</td><td>0(h~-2)</td><td>O(hn-3）</td></tr></table>

One measure of comparing the lower-order Runge-Kutt methods is described as follows:

The Runge-Kutta method of order four requires four evaluations per step, so it should give more accurate answers than Euler's method with one-fourth the step size if it is to be superior. Similarly, if the Runge-Kutta method of order four is to be superior to the second-order Runge-Kutta methods, it should give more accuracy with step size $h$ than a second-order method with step size ${ \scriptstyle { \frac { 1 } { 2 } } } h$ , because the fourth-order method requires twice as many evaluations per step.

An ilustration of the superiorityof the Runge-Kuta fourth-order method by this measure is shown in the following example.

For the problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

Euler's method with $h \ : = \ : 0 . 0 2 5$ , the Midpoint method with $h \ : = \ : 0 . 0 5$ , and the Runge-Kutta fourth-order method with $h = 0 . 1$ are compared at the common mesh points of these methods 0.1, 0.2, 0.3, 0.4,and 0.5. Each of these techniques requires 20 functional evaluations to determine the values listed in Table 5.8 to approximate y(O.5). In this example, the fourth-order method is clearly superior.

Table 5.8   

<table><tr><td>Exact</td><td></td><td>Euler h = 0.025</td><td>Modified Euler h = 0.05</td><td>Runge-Kutta Order Four h = 0.1</td></tr><tr><td>i 0.0</td><td></td><td>0.5000000</td><td>0.5000000</td><td>0.5000000</td></tr><tr><td>0.1</td><td>0.5000000 0.6574145</td><td>0.6554982</td><td>0.6573085</td><td>0.6574144</td></tr><tr><td>0.2</td><td>0.8292986</td><td>0.8253385</td><td>0.8290778</td><td>0.8292983</td></tr><tr><td>0.3</td><td>1.0150706</td><td>1.0089334</td><td>1.0147254</td><td>1.0150701</td></tr><tr><td>0.4</td><td>1.2140877</td><td>1.2056345</td><td>1.2136079</td><td>1.2140869</td></tr><tr><td>0.5</td><td>1.4256394</td><td>1.4147264</td><td>1.4250141</td><td>1.4256384</td></tr></table>

# ExERCIsE SEt 5.4

1. Use the Modified Euler method to approximate the solutions to each of the following initialvalue problems,and compare the results to the actual values.

a. y = te³r - 2y, $0 \leq t \leq 1$ ， $y ( 0 ) = 0$ ，with $h = 0 . 5$ ；actual solution $y ( t ) =$ $\textstyle { \frac { 1 } { 5 } } t e ^ { 3 t } - { \frac { 1 } { 2 5 } } e ^ { 3 t } + { \frac { 1 } { 2 5 } } e ^ { - 2 t }$   
b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1$ ，with $h = 0 . 5$ ； actual solution $\begin{array} { r } { y ( t ) = t + \frac { 1 } { 1 - t } } \end{array}$ ·   
c. y' =1+y/t， 1 ≤t ≤2, y(1) = 2,with h =0.25;actual solution y(t)= t lnt+2t.   
d. $y ^ { \prime } = \cos 2 t + \sin 3 t$ $0 \leq t \leq 1$ 、 $y ( 0 ) = 1$ ，with $h \ = \ 0 . 2 5$ ；actual solution $y ( t ) = { \textstyle { \frac { 1 } { 2 } } } \sin 2 t - { \textstyle { \frac { 1 } { 3 } } } \cos 3 t + { \textstyle { \frac { 4 } { 3 } } }$

2.Repeat Exercise 1 using Heun's method.

3. Repeat Exercise 1 using the Midpoint method.

4. Use the Modified Euler method to approximate the solutions to each of the following initial-value problems, and compare the results to the actual values.

a. $\begin{array} { l l } { { y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , } } & { { 1 \leq t \leq 2 , \quad y ( 1 ) = 1 , } } \\ { { t / ( 1 + \ln t ) . } } & { { } } \end{array}$ with $h = 0 . 1$ ； actual solution $y ( t ) =$   
b. $y ^ { \prime } = 1 + y / t + ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = 0 ,$ with $h = 0 . 2$ ；actual solution$y ( t ) = t \tan ( \ln t )$ ，  
c. $y ^ { \prime } = - ( y + 1 ) ( y + 3 ) , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = - 2 ,$ with $h = 0 . 2$ ； actual solutiony(t)=-3+2(1+e-2)-1.  
d. y= -5y+5t²+2t， $0 \leq t \leq 1$ $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 3 } } \end{array}$ ，with $h = 0 . 1$ ；actual solutiony(t）=t²+e-5t.

5.Use the results of Exercise 4 and linear interpolation to approximate values of $y ( t )$ , and com-pare the results to the actual values.

a.y(1.25)and y(1.93) $\begin{array} { r l } { \mathbf { b } . \ } & { { } y ( 2 . 1 ) \mathrm { a n d } y ( 2 . 7 5 ) } \\ { \mathbf { d } . \ } & { { } y ( 0 . 5 4 ) \mathrm { a n d } y ( 0 . 9 4 ) } \end{array}$ c.y(1.3) and y(1.93)

6. Repeat Exercise 4 using Heun's method.

7.Repeat Exercise 5 using the results of Exercise 6.

8.Repeat Exercise 4 using the Midpoint method.

9.Repeat Exercise 5 using the results of Exercise 8.

10.Repeat Exercise 1 using the Runge-Kut method of order four.

11.Repeat Exercise 4 using the Runge-Kutta method of order four.

12.Use the results of Exercise 11 and Cubic Hermite interpolation to approximate values of $y ( t )$ ， and compare the approximations to the actual values.

a.y(1.25) and y(1.93) $\begin{array} { r l } { \mathbf { b } . \ } & { { } y ( 2 . 1 ) \ \mathrm { a n d } \ y ( 2 . 7 5 ) } \\ { \mathbf { d } . \ } & { { } y ( 0 . 5 4 ) \ \mathrm { a n d } \ y ( 0 . 9 4 ) } \end{array}$ c. y(1.3)andy(1.93)

13.Show that the Midpoint method,the Modified Euler method,and Heun's method give the same approximations to the initial-value problem

$$
y ^ { \prime } = - y + t + 1 , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 ,
$$

for any choice of h. Why is this true?

14.Water flows from an inverted conical tank with circular orifice at the rate

$$
\frac { d x } { d t } = - 0 . 6 \pi r ^ { 2 } \sqrt { 2 g } \frac { \sqrt { x } } { A ( x ) } ,
$$

where $\pmb { r }$ is the radius of the orifice, $\pmb { x }$ is the height of the liquid level from the vertex of the cone, and $A ( x )$ is the area of the cross section of the tank $\pmb { x }$ units above the orifice. Suppose $r = 0 . 1$ ft, $g = 3 2 . 1 \mathrm { f } \mathsf { t } / \mathsf { s } ^ { 2 }$ ,and the tank has an initial water level of 8 ft and initial volume of $5 1 2 ( \pi / 3 )$ ft.

a. Compute the water level after 10 min with $h = 2 0 ~ \mathsf { s }$ ${ \bf h } .$ Determine, to within 1 min, when the tank will be empty.

15. The irreversible chemical reaction in which two molecules of solid potassum dichromate $( \mathbb { K } _ { 2 } \mathbb { C } _ { \mathbb { I } _ { 2 } } 0 _ { 7 } )$ , two molecules of water $\left( \mathbf { H } _ { 2 } \mathbf { O } \right)$ ,and three atoms of solid sulfur (S) combine to yield three molecules of the gas sulfur dioxide $( S O _ { 2 } )$ ,four molecules of solid potassum hydroxide (KOH),and two molecules of solid chromic oxide $( \mathbf { C r } _ { 2 } \mathbf { O } _ { 3 } )$ can be represented symbolically by the stoichiometric equation:

$$
2 \mathrm { K } _ { 2 } \mathrm { C r } _ { 2 } \mathrm { O } _ { 7 } + 2 \mathrm { H } _ { 2 } \mathrm { O } + 3 \mathrm { S } \longrightarrow 4 \mathrm { K O H } + 2 \mathrm { C r } _ { 2 } \mathrm { O } _ { 3 } + 3 \mathrm { S O } _ { 2 } .
$$

If $n _ { 1 }$ molecules of ${ \bf K } _ { 2 } \mathbf { C r } _ { 2 } \mathbf { O } _ { 7 }$ ， $\pmb { n } _ { 2 }$ molecules of ${ \bf H } _ { 2 } \boldsymbol { 0 }$ ,and $\pmb { n _ { 3 } }$ molecules of S are originally available, the following differential equation describes the amount $x ( t )$ of KOH after time $t$ ：

$$
\frac { d x } { d t } = k \left( n _ { 1 } - \frac { x } { 2 } \right) ^ { 2 } \left( n _ { 2 } - \frac { x } { 2 } \right) ^ { 2 } \left( n _ { 3 } - \frac { 3 x } { 4 } \right) ^ { 3 } ,
$$

where $k$ is the velocity constant of the reaction. If ${ k = 6 . 2 2 \times 1 0 ^ { - 1 9 } }$ ， $n _ { 1 } = n _ { 2 } = 2 \times 1 0 ^ { 3 }$ ，and $n _ { 3 } = 3 \times 1 0 ^ { 3 }$ ,how many units of potassium hydroxide will have been formed after $0 . 2 \ { \mathsf { s ? } }$

16.Show that the difference method

$$
\begin{array} { r l } & { w _ { 0 } = \alpha , } \\ & { w _ { i + 1 } = w _ { i } + a _ { 1 } f ( t _ { i } , w _ { i } ) + a _ { 2 } f ( t _ { i } + \alpha _ { 2 } , w _ { \mathrm { I } } + \delta _ { 2 } f ( t _ { i } , w _ { i } ) ) , } \end{array}
$$

for each $i = 0 , 1 , \ldots , N - 1$ ， cannot have local truncation error $O ( h ^ { 3 } )$ for any choice of constants $a _ { 1 } , a _ { 2 } , \alpha _ { 2 }$ ,and $\delta _ { 2 }$ ·

17.The Runge-Kutta method of order four can be written in the form

$$
\begin{array} { l } { { \displaystyle w _ { i + 1 } = w _ { i } + \frac { h } { 6 } f ( t _ { i } , w _ { i } ) + \frac { h } { 3 } f ( t _ { i } + \alpha _ { 1 } h , w _ { i } + \delta _ { 1 } h f ( t _ { i } , w _ { i } ) ) } } \\ { ~ } \\ { { \displaystyle ~ + \frac { h } { 3 } f ( t _ { i } + \alpha _ { 2 } h , w _ { i } + \delta _ { 2 } h f ( t _ { i } + \gamma _ { 2 } h , w _ { i } + \gamma _ { 3 } h f ( t _ { i } , w _ { i } ) ) ) } } \\ { { \displaystyle ~ + \frac { h } { 6 } f ( t _ { i } + \alpha _ { 3 } h , w _ { i } + \delta _ { 3 } h f ( t _ { i } + \gamma _ { 4 } h , w _ { i } + \gamma _ { 5 } h f ( t _ { i } + \gamma _ { 6 } h , w _ { i } + \gamma _ { 7 } h f ( t _ { i } , w _ { i } ) ) ) ) . } } \end{array}
$$

Find the values of the constants

$$
\alpha _ { 1 } , ~ \alpha _ { 2 } , ~ \alpha _ { 3 } , ~ \delta _ { 1 } , ~ \delta _ { 2 } , ~ \delta _ { 3 } , ~ \gamma _ { 2 } , ~ \gamma _ { 3 } , ~ \gamma _ { 4 } , ~ \gamma _ { 5 } , ~ \gamma _ { 6 } , ~ \mathrm { a n d } ~ \gamma _ { 7 } .
$$

# 5.5 Error Control and the Runge-Kutta-Fehlberg Method

The appropriate use of varying step size was seen in Section 4.6 to produce computationally efficient integral approximating methods. In itself,this might not be sufficient to favor these methods due to the increased complication of applying them. However, they have another feature that makes them worthwhile. They incorporate in the step-size procedure an estimate of the truncation error that does not require the approximation of the higher derivatives of the function. These methods are called adaptive because they adapt the number and position of the nodes used in the approximation to ensure that the truncation error is kept within a specified bound.

There is a close connection between the problem of approximating the value of a definite integral and that of approximating the solution to an initial-value problem. It is not surprising,then, that there are adaptive methods for approximating the solutions to initial-value problems and that these methods are not only eficient, but also incorporate the control of error.

An ideal difference-equation method

$$
w _ { i + 1 } = w _ { i } + h _ { i } \phi ( t _ { i } , w _ { i } , h _ { i } ) , \quad i = 0 , 1 , \ldots , N - 1 ,
$$

for approximating the solution, $y ( t )$ , to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

would have the property that, given a tolerance $\varepsilon > 0$ , the minimal number of mesh points would be used to ensure that the global error, $| y ( t _ { i } ) - w _ { i } |$ , would not exceed $\varepsilon$ for any $i = 0$ ,1,..., $N$ . Having a minimal number of mesh points and also controlling the global error of a difference method is, not surprisingly, inconsistent with the points being equally spaced in the interval. In this section we examine techniques used to control the error of a difference-equation method in an efcient manner by the appropriate choice of mesh points.

Although we cannot generally determine the global error of a method, we wil see in Section 5.10 that there is a close connection between the local truncation error and the global error. By using methods of differing order we can predict the local truncation error and, using this prediction, choose a step size that willkeep it and the global error in check.

To illustrate the technique, suppose that we have two approximation techniques. The first is an $n$ th-order method obtained from an nth-order Taylor method of the form

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h \phi ( t _ { i } , y ( t _ { i } ) , h ) + O ( h ^ { n + 1 } ) ,
$$

producing approximations

$$
\begin{array} { r c l } { { } } & { { } } & { { w _ { 0 } = \alpha } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { w _ { i + 1 } = w _ { i } + h \phi ( t _ { i } , w _ { i } , h ) , \quad \mathrm { f o r } i > 0 , } } \end{array}
$$

with local truncation error $\tau _ { i + 1 } ( h ) = { \cal O } ( h ^ { n } )$ . In general, the method is generated by applying a Runge-Kutta modification to the Taylor method, but the specific derivation is unimportant.

The second method is similar but one order higher; it comes from an $( n + 1 )$ st-order Taylor method of the form

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h \tilde { \phi } ( t _ { i } , y ( t _ { i } ) , h ) + O ( h ^ { n + 2 } ) ,
$$

producing approximations

$$
\begin{array} { r } { \tilde { w } _ { 0 } = \alpha } \\ { \quad } \\ { \tilde { w } _ { i + 1 } = \tilde { w } _ { i } + h \tilde { \phi } ( t _ { i } , \tilde { w } _ { i } , h ) , \quad \mathrm { f o r } i > 0 , } \end{array}
$$

with local truncation error $\tilde { \tau } _ { i + 1 } ( h ) = O ( h ^ { n + 1 } )$

We first make the assumption that $w _ { i } \approx y ( t _ { i } ) \approx \tilde { w } _ { i }$ and choose a fixed step size $h$ to generate the approximations ${ \boldsymbol { w } } _ { i + 1 }$ and $\tilde { w } _ { i + 1 }$ to $y ( t _ { i + 1 } )$ . Then

$$
\begin{array} { r l } & { \tau _ { i + 1 } ( h ) = \frac { y ( t _ { i + 1 } ) - y ( t _ { i } ) } { h } - \phi ( t _ { i } , y ( t _ { i } ) , h ) } \\ & { \qquad = \frac { y ( t _ { i + 1 } ) - w _ { i } } { h } - \phi ( t _ { i } , w _ { i } , h ) } \\ & { \qquad = \frac { y ( t _ { i + 1 } ) - [ w _ { i } + h \phi ( t _ { i } , w _ { i } , h ) ] } { h } } \\ & { \qquad = \frac { 1 } { h } ( y ( t _ { i + 1 } ) - w _ { i + 1 } ) . } \end{array}
$$

In a similar manner,

$$
\tilde { \tau } _ { i + 1 } ( h ) = \frac { 1 } { h } ( y ( t _ { i + 1 } ) - \tilde { w } _ { i + 1 } ) ,
$$

and, as a consequence,

$$
\begin{array} { l } { \displaystyle \tau _ { i + 1 } ( h ) = \frac { 1 } { h } ( y ( t _ { i + 1 } ) - w _ { i + 1 } ) } \\ { \displaystyle \quad = \frac { 1 } { h } [ ( y ( t _ { i + 1 } ) - \tilde { w } _ { i + 1 } ) + ( \tilde { w } _ { i + 1 } - w _ { i + 1 } ) \} } \\ { \displaystyle \quad = \tilde { \tau } _ { i + 1 } ( h ) + \frac { 1 } { h } ( \tilde { w } _ { i + 1 } - w _ { i + 1 } ) . } \end{array}
$$

But $\tau _ { i + 1 } ( h )$ is $O ( h ^ { n } )$ and $\tilde { \tau } _ { i + 1 } ( h )$ is $O ( h ^ { n + 1 } )$ ， so the significant portion of $\tau _ { i + 1 } ( h )$ must come from

$$
\frac { 1 } { h } \left( \tilde { w } _ { i + 1 } - w _ { i + 1 } \right) .
$$

This gives us an easily computed approximation for the local truncation error of the $O ( h ^ { n } )$ method:

$$
\tau _ { i + 1 } ( h ) \approx \frac { 1 } { h } \left( \tilde { w } _ { i + 1 } - w _ { i + 1 } \right) .
$$

The object, however, is not simply to estimate the local truncation error but to adjust the step size to keep it within a specified bound. To do this we now assume that since $\tau _ { i + 1 } ( h )$ is $O ( h ^ { n } )$ ,a number $K$ , independent of $h$ ,exists with

$$
\tau _ { i + 1 } ( h ) \approx K h ^ { n } .
$$

Then the local truncation error produced by applying the nth-order method with a new step size $q h$ can be estimated using the original approximations $w _ { i + 1 }$ and $\tilde { w } _ { i + 1 }$ ：

$$
\tau _ { i + 1 } ( q h ) \approx K ( q h ) ^ { n } = q ^ { n } ( K h ^ { n } ) \approx q ^ { n } \tau _ { i + 1 } ( h ) \approx \frac { q ^ { n } } { h } ( \tilde { w } _ { i + 1 } - w _ { i + 1 } ) .
$$

To bound ${ \tau } _ { i + 1 } ( q h )$ by $\varepsilon$ , we choose $q$ so that

$$
\frac { q ^ { n } } { h } | \tilde { w } _ { i + 1 } - w _ { i + 1 } | \approx | \tau _ { i + 1 } ( q h ) | \leq \varepsilon ;
$$

that is, so that

$$
q \leq \left( \frac { \varepsilon h } { | \tilde { w } _ { i + 1 } - w _ { i + 1 } | } \right) ^ { 1 / n } .
$$

One popular technique that uses this inequality for error control is the Runge-Kutta-Fehlberg method. (See [Fe].) This technique uses a Runge-Kutta method with local truncation error of order five,

$$
\tilde { w } _ { i + 1 } = w _ { i } + \frac { 1 6 } { 1 3 5 } k _ { 1 } + \frac { 6 6 5 6 } { 1 2 8 2 5 } k _ { 3 } + \frac { 2 8 5 6 1 } { 5 6 4 3 0 } k _ { 4 } - \frac { 9 } { 5 0 } k _ { 5 } + \frac { 2 } { 5 5 } k _ { 6 } ,
$$

to estimate the local error in a Runge-Kutta method of order four given by

$$
w _ { i + 1 } = w _ { i } + { \frac { 2 5 } { 2 1 6 } } k _ { 1 } + { \frac { 1 4 0 8 } { 2 5 6 5 } } k _ { 3 } + { \frac { 2 1 9 7 } { 4 1 0 4 } } k _ { 4 } - { \frac { 1 } { 5 } } k _ { 5 } ,
$$

where

$$
\begin{array} { l } { { \displaystyle k _ { 1 } = h f ( t _ { i } , w _ { i } ) , } } \\ { { \displaystyle k _ { 2 } = h f \left( t _ { i } + \frac { h } { 4 } , w _ { i } + \frac { 1 } { 4 } k _ { 1 } \right) , } } \end{array}
$$

$$
\begin{array} { l } { \displaystyle { k _ { 3 } = h f \left( t _ { i } + \frac { 3 h } { 8 } , w _ { i } + \frac { 3 } { 3 2 } k _ { 1 } + \frac { 9 } { 3 2 } k _ { 2 } \right) , } } \\ { \displaystyle { k _ { 4 } = h f \left( t _ { i } + \frac { 1 2 h } { 1 3 } , w _ { i } + \frac { 1 9 3 2 } { 2 1 9 7 } k _ { 1 } - \frac { 7 2 0 0 } { 2 1 9 7 } k _ { 2 } + \frac { 7 2 9 6 } { 2 1 9 7 } k _ { 3 } \right) , } } \\ { \displaystyle { k _ { 5 } = h f \left( t _ { i } + h , w _ { i } + \frac { 4 3 9 } { 2 1 6 } k _ { 1 } - 8 k _ { 2 } + \frac { 3 6 8 0 } { 5 1 3 } k _ { 3 } - \frac { 8 4 5 } { 4 1 0 4 } k _ { 4 } \right) , } } \\ { \displaystyle { k _ { 6 } = h f \left( t _ { i } + \frac { h } { 2 } , w _ { i } - \frac { 8 } { 2 7 } k _ { 1 } + 2 k _ { 2 } - \frac { 3 5 4 4 } { 2 5 6 5 } k _ { 3 } + \frac { 1 8 5 9 } { 4 1 0 4 } k _ { 4 } - \frac { 1 1 } { 4 0 } k _ { 5 } \right) . } } \end{array}
$$

An advantage to this method is that only six evaluations of $f$ are required per step. Arbitrary Runge-Kutta methods of orders four and five used together require (see Table 5.7 in Section 5.4) at least four evaluations of $f$ for the fourth-order method and an additional six for the fifth-order method,for a total of at least ten functional evaluations.

In the error-control theory,an initial value of $h$ at the ith step was used to find the first values of $w _ { i + 1 }$ and $\tilde { w } _ { i + 1 }$ ，which Ied to the determination of $q$ for that step, and then the calculations were repeated. This procedure requires twice the number of functional evaluations per step as without the error control. In practice, the value of $\pmb q$ to be used is chosen somewhat differently in order to make the increased functional-evaluation cost worthwhile. The value of $q$ determined at the ith step is used for two purposes:

1.To reject, if necessary,the initial choice of $h$ at the ith step and repeat the calculations using $\pmb q h$ ; and 2.To predict an appropriate initial choice of $h$ for the $( i + 1 )$ st step.

Because of the penalty in terms of functional evaluations that must be paid if the steps are repeated, $q$ tends to be chosen conservatively. In fact, for the Runge-Kutta-Fehlberg method with $n = 4$ ,the usual choice is

$$
q = \left( \frac { \varepsilon h } { 2 | \tilde { w } _ { i + 1 } - w _ { i + 1 } | } \right) ^ { 1 / 4 } = 0 . 8 4 \left( \frac { \varepsilon h } { | \tilde { w } _ { i + 1 } - w _ { i + 1 } | } \right) ^ { 1 / 4 } .
$$

In Algorithm 5.3 for the Runge-Kutta-Fehlberg method, Step 9 is added to eliminate large modifications in step size. This is done to avoid spending too much time with small step sizes in regions with irregularities in the derivatives of $y$ and to avoid large step sizes, which can result in skipping sensitive regions between the steps. In some instances the step-size increase procedure is omited completely from the algorithm,and the step-size decrease procedure is modified to be incorporated only when needed to bring the error under control.

# Runge-Kutta-Fehlberg

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

with local truncation error within a given tolerance:

INPUTendpoints $a , b$ ; initial condition $\pmb { \alpha }$ ; tolerance TOL; maximum step size hmax;   
minimum step size hmin.

OUTPUTt, $w , h$ where $\pmb { w }$ approximates $y ( t )$ and the step size $h$ was used, or a message that the minimum step size was exceeded.

Step 1 Set $t = a$ ； w=α; $h = h m a x ;$ $F L A G = 1 ;$ OUTPUT $( t , w )$

Step2 While $( F L A G = 1 )$ do Steps 3-11.

Step 3 Set $K _ { 1 } = h f \left( t , w \right)$ ：

$$
\begin{array} { r l } & { K _ { 2 } = h f \left( t + \frac { 1 } { 4 } h , w + \frac { 1 } { 4 } K _ { 1 } \right) ; } \\ & { K _ { 3 } = h f \left( t + \frac { 3 } { 8 } h , w + \frac { 3 } { 3 2 } K _ { 1 } + \frac { 9 } { 3 2 } K _ { 2 } \right) ; } \\ & { K _ { 4 } = h f \left( t + \frac { 1 2 } { 1 3 } h , w + \frac { 1 9 3 2 } { 2 1 9 7 } K _ { 1 } - \frac { 7 2 0 0 } { 2 1 9 7 } K _ { 2 } + \frac { 7 2 9 6 } { 2 1 9 7 } K _ { 3 } \right) ; } \\ & { K _ { 5 } = h f \left( t + h , w + \frac { 4 3 9 } { 2 1 6 } K _ { 1 } - 8 K _ { 2 } + \frac { 3 6 8 0 } { 5 1 3 } K _ { 3 } - \frac { 8 4 5 } { 4 1 0 4 } K _ { 4 } \right) ; } \\ & { K _ { 6 } = h f \left( t + \frac { 1 } { 2 } h , w - \frac { 8 } { 2 7 } K _ { 1 } + 2 K _ { 2 } - \frac { 3 5 4 4 } { 2 5 6 5 } K _ { 3 } + \frac { 1 8 5 9 } { 4 1 0 4 } K _ { 4 } - \frac { 1 1 } { 4 0 } K _ { 5 } \right) . } \end{array}
$$

Step4 Set $\begin{array} { r } { R = \frac { 1 } { h } | \frac { 1 } { 3 6 0 } K _ { 1 } - \frac { 1 2 8 } { 4 2 7 5 } K _ { 3 } - \frac { 2 1 9 7 } { 7 5 2 4 0 } K _ { 4 } + \frac { 1 } { 5 0 } K _ { 5 } + \frac { 2 } { 5 5 } K _ { 6 } | . } \end{array}$

$$
\begin{array} { r } { ( N o t e ; R = \frac { 1 } { h } | \tilde { w } _ { i + 1 } - w _ { i + 1 } | . ) } \end{array}
$$

Step 5 If $R \leq T O L$ then do Steps 6 and 7.

Step $\sigma$ Set $t = t + h$ ；  (Approximation accepted.)

$$
\begin{array} { r } { w = w + \frac { 2 5 } { 2 1 6 } K _ { 1 } + \frac { 1 4 0 8 } { 2 5 6 5 } K _ { 3 } + \frac { 2 1 9 7 } { 4 1 0 4 } K _ { 4 } - \frac { 1 } { 5 } K _ { 5 } . } \end{array}
$$

Step 7OUTPUT $( t , w , h )$

Step 8 Set $\delta = 0 . 8 4 ( T O L / R ) ^ { 1 / 4 } .$

Step 9If $\delta \leq 0 . 1$ then set $h = 0 . 1 h$ else if $\delta \geq 4$ then set $h = 4 h$ else set $h = \delta h$ .(Calculate new h.)

Step 10 If $h >$ hmax then set $h = h m a x$

Step 11 If $t \geq b$ then set $F L A G = 0$ else if $t + h > b$ then set $h = b - t$ else if $h <$ hmin then set $F L A G = 0$ ； OUTPUT ('minimum h exceeded'). (Procedure completed unsuccessfuly.)

Step 12 (The procedure is complete.) STOP.

# EXAMPLE 1

Algorithm 5.3 will be used to approximate the solution to the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

which has solution $y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t }$ . The input consists of a tolerance $T O L = 1 0 ^ { - 5 }$ ， a maximum step size hmax = 0.25,and a minimum step size hmin = 0.O1. The results are shown in Table 5.9.The last two columns in Table 5.9 show the results of the fifth-order method. For small values of $\pmb { t }$ , the error is less than the error in the fourth-order method, but the error exceeds that of the fourth-order method when $t$ increases. ■

Table 5.9   

<table><tr><td></td><td></td><td>RKF-4</td><td></td><td></td><td></td><td>RKF-5</td><td></td></tr><tr><td>t</td><td>yi=y(ti）</td><td>Wi</td><td>h</td><td>R</td><td>lyi-wil</td><td>Wi</td><td>lyi-Wil</td></tr><tr><td>0</td><td>0.5</td><td>0.5</td><td></td><td></td><td>0.5</td><td></td><td></td></tr><tr><td>0.2500000</td><td>0.9204873</td><td>0.9204886</td><td>0.2500000</td><td>6.2 ×10-6</td><td>1.3 × 10-6</td><td>0.9204870</td><td>2.424 × 10-7</td></tr><tr><td>0.4865522</td><td>1.3964884</td><td>1.3964910</td><td>0.2365522</td><td>4.5×10-6</td><td>2.6× 10-6</td><td>1.3964900</td><td>1.510 × 10-6</td></tr><tr><td>0.7293332</td><td>1.9537446</td><td>1.9537488</td><td>0.2427810</td><td>4.3×10-6</td><td>4.2 ×10-6</td><td>1.9537477</td><td>3.136×10-6</td></tr><tr><td>0.9793332</td><td>2.5864198</td><td>2.5864260</td><td>0.2500000</td><td>3.8×10-6</td><td>6.2 × 10-6</td><td>2.5864251</td><td>5.242 × 10-6</td></tr><tr><td>1.2293332</td><td>3.2604520</td><td>3.2604605</td><td>0.2500000</td><td>2.4×10-6</td><td>8.5×10-6</td><td>3.2604599</td><td>7.895 × 10-6</td></tr><tr><td>1.4793332</td><td>3.9520844</td><td>3.9520955</td><td>0.2500000</td><td>7×10-7</td><td>1.11 × 10-5</td><td>3.9520954</td><td>1.096 × 10-5</td></tr><tr><td>1.7293332</td><td>4.6308127</td><td>4.6308268</td><td>0.2500000</td><td>1.5 × 10-6</td><td>1.41 × 10-5</td><td>4.6308272</td><td>1.446 × 10-5</td></tr><tr><td>1.9793332</td><td>5.2574687</td><td>5.2574861</td><td>0.2500000</td><td>4.3×10-6</td><td>1.73 ×10-5</td><td>5.2574871</td><td>1.839 × 10-5</td></tr><tr><td>2.0000000</td><td>5.3054720</td><td>5.3054896</td><td>0.0206668</td><td></td><td>1.77 × 10-5</td><td>5.3054896</td><td>1.768 ×10-5</td></tr></table>

An implementation of the Runge-Kutta-Fehlberg method is available in Maple using the dsolve command with the numeric option. Consider the initial-value problem of Ex. ample 1. The command

$$
> \mathtt { g } : = \mathtt { d s o l v e } \left( \left. \mathbb { D } \left( \mathbf { y } \right) \left( \mathtt { t } \right) = \mathtt { y } \left( \mathtt { t } \right) - \mathtt { t } \ast \mathtt { t } + 1 , \mathtt { y } \left( 0 \right) = 0 . 5 \right. , \mathtt { y } \left( \mathtt { t } \right) , \mathtt { n u m e r i c } \right) ;
$$

returns the procedure

$$
g : = \operatorname { p r o c } ( r k f 4 5 - x ) \ldots { \mathrm { e n d } }
$$

We can evaluate $y$ as shown by example, using

which gives

$$
[ t = 2 . 0 , y ( t ) = 5 . 3 0 5 4 7 1 9 5 8 4 0 0 1 9 4 ]
$$

# EXERCIsE SET 5.5

1.Use the Runge-Kutta-Fehlberg method with tolerance $T O L \ : = \ : 1 0 ^ { - 4 }$ ， $h m a x \ = \ 0 . 2 5$ ，and hmin $\mathbf { \sigma } = 0 . 0 5$ to approximate the solutions to the following initial-value problems. Compare the results to the actual values.

a. $y _ { , } ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ;$ actual solution $\begin{array} { r } { y ( t ) = \frac { 1 } { 5 } t e ^ { 3 t } - \frac { 1 } { 2 5 } e ^ { 3 t } + } \end{array}$ 2se-2i   
b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1$ ； actual solution $y ( t ) = t + 1 / ( 1 - t )$   
c. $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2$ ；actual solution $y ( t ) = t \ln t + 2 t$   
d. y= cos 2t + sin 3t， $0 \leq t \leq 1$ ， $y ( 0 ) = 1$ ；actual solution $y ( t ) = { \textstyle { \frac { 1 } { 2 } } } \sin 2 t -$ cos3t+

2. Use the Runge-Kutta Fehlberg Algorithm with tolerance $T O L = 1 0 ^ { - 4 }$ to approximate the solution to the following initial-value problems.

a. $y ^ { \prime } = ( y / t ) ^ { 2 } + y / t , \quad 1 \leq t \leq 1 . 2 , \quad y ( 1 ) = 1$ ，with $h m a x = 0 . 0 5$ and hmi $\pmb { \imath } = 0 . 0 2$ b. $y ^ { \prime } = \sin t + e ^ { - t } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ,$ with $h m a x = 0 . 2 5$ and hmin $\mathbf { \tau } = 0 . 0 2$ c. $y ^ { \prime } = 1 / t ( y ^ { 2 } + y )$ ， $1 \leq t \leq 3$ ， $y ( 1 ) = - 2$ with $h m a x = 0 . 5$ and h ${ m i n = 0 . 0 2 }$ d. $y ^ { \prime } = t ^ { 2 } , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 ,$ with $h m a x = 0 . 5$ and $h m i n = 0 . 0 2$

3. Use the Runge-Kutta-Fehlberg method with tolerance $T O L = 1 0 ^ { - 6 }$ ， $h m a x = 0 . 5$ , and hmin $\lneq$ 0.05 to approximate the solutions to the following initial-value problems. Compare the results to the actual values.

a. $y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 4 , \quad y ( 1 ) = 1 ;$ actual solution $y ( t ) = t / ( 1 + \ln t )$   
b. $y ^ { \prime } = 1 + y / t + ( y / t ) ^ { 2 } , \quad 1 \leq$ $1 \leq t \leq 3$ ， $y ( 1 ) = 0$ ；actual solution $y ( t ) = t \tan ( \ln t )$   
c. y'=-(y+1)(y+3)， $0 \leq t \leq 3$ ， $y ( 0 ) = - 2$ ； actual solution $y ( t ) = - 3 + 2 ( 1 +$ $e ^ { - 2 t } ) ^ { - 1 }$ ：   
d. y=(t+2t³)y³-ty，0≤t≤2， $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 3 } } \end{array}$ ； actual solution $y ( t ) = ( 3 + 2 t ^ { 2 } +$ 6e²2)-1/2.

4.The Runge-Kutta-Verner method is based on the formulas

$$
\begin{array} { r l } & { w _ { i + 1 } = w _ { i } + \displaystyle \frac { 1 3 } { 1 6 0 } k _ { 1 } + \frac { 2 3 7 5 } { 5 9 8 4 } k _ { 3 } + \frac { 5 } { 1 6 } k _ { 4 } + \frac { 1 2 } { 8 5 } k _ { 5 } + \frac { 3 } { 4 4 } k _ { 6 } \quad \mathrm { a n d } } \\ & { \tilde { w } _ { i + 1 } = w _ { i } + \displaystyle \frac { 3 } { 4 0 } k _ { 1 } + \frac { 8 7 5 } { 2 2 4 4 } k _ { 3 } + \frac { 2 3 } { 7 2 } k _ { 4 } + \frac { 2 6 4 } { 1 9 5 5 } k _ { 5 } + \frac { 1 2 5 } { 1 1 5 9 2 } k _ { 7 } + \frac { 4 3 } { 6 1 6 } k _ { 8 } , } \end{array}
$$

where

$$
\begin{array} { r l } & { k = b k ^ { \prime } ( \theta _ { 1 } , \theta _ { 2 } , \theta _ { 1 } ) } \\ & { \delta _ { t } - \lambda b ^ { \prime } \left( \boldsymbol { f } _ { 1 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 1 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 1 } \right) , } \\ & { \delta _ { t } = b k ^ { \prime } \left( \boldsymbol { f } _ { 1 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 2 } \right) , } \\ & { \delta _ { t } = \lambda b ^ { \prime } \left( \boldsymbol { f } _ { 2 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 2 } \right) , } \\ & { \mathrm { ~ k = } \lambda r \left( \delta + \frac { 2 \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 1 } \right) , } \\ & { \delta _ { t } = \lambda r \left( \boldsymbol { f } _ { 1 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } \right) , } \\ & { \delta _ { t } - \lambda r \left( \boldsymbol { f } _ { 1 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 2 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 2 } \right) , } \\ &  \delta _ { t } = b k ^ { \prime } \left( \boldsymbol { f } _ { 1 } + \frac { \delta _ { t } } { 2 } , \theta _ { 1 } , - \frac { 1 6 \delta _ { t } } { 2 } - \delta _ { t } \right) \delta _ { t } - \frac { \delta _ { t } \delta _ { t } } { 2 } - \frac { 1 6 \delta _ { t } } { 2 } - \frac { 1 6 \delta _ { t } } { 2 } - \frac { 3 6 \delta _ { t } } { 2 } - \frac { 3 6 \delta _ { t } } { 2 } - \frac { 3 6 \delta _ { t } } { 2 } - \end{array}
$$

The sixth-order method $\tilde { w } _ { i + 1 }$ is used to estimate the error in the fth-order method ${ \boldsymbol { w } } _ { i + 1 }$ Construct an algorithm similar to the Runge-Kutta-Fehlberg Algorithm, and repeat Exercise 3 using this new method.

5.In the theory of the spread of contagious disease (see [Bal] or [Ba2]), a relatively elementary differential equation can be used to predict the number of infective individuals in the population at any time, provided appropriate simplification assumptions are made. In particular, let us assume that all individuals in a fixed population have an equally likely chance of being infected and once infected remain in that state. Suppose $x ( t )$ denotes the number of susceptible individuals at time $t$ and $y ( t )$ denotes the number of infectives. It is reasonable to assume that the rate at which the number of infectives changes is proportional to the product of $x ( t )$ and $y ( t )$ since the rate depends on both the number of infectives and the number of susceptibles present at that time. If the population is large enough to assume that $x ( t )$ and $y ( t )$ are continuous variables, the problem can be expressed

$$
y ^ { \prime } ( t ) = k x ( t ) y ( t ) ,
$$

where $k$ is a constant and $x ( t ) + y ( t ) = m$ ,the total population.This equation can be rewritten involving only $y ( t )$ as

$$
y ^ { \prime } ( t ) = k ( m - y ( t ) ) y ( t ) .
$$

a. Assuming that $m = 1 0 0 , 0 0 0 , y ( 0 ) = 1 0 0 0 , k = 2 \times 1 0 ^ { - 6 }$ , and that time is measured in days,find an approximation to the number of infective individuals at the end of 3O days.   
b. The differential equation in part (a) is called a Bernoulli equation and it can be transformed into a linear differential equation in $u ( t ) = ( y ( t ) ) ^ { - 1 }$ . Use this technique to find the exact solution to the equation, under the same assumptions as in part (a), and compare the true value of $y ( t )$ to the approximation given there. What is $\scriptstyle \operatorname* { l i m } _ { t \to \infty } y ( t )$ ？ Does this agree with your intuition?

6. In the previous exercise,all infected individuals remained in the population to spread the disease.A more realistic proposal is to introduce a third variable $z ( t )$ to represent the number of individuals who are removed from the affected population at a given time $t$ by isolation, recovery and consequent immunity, or death. This quite naturally complicates the problem, but it can be shown (see [Ba2]) that an approximate solution can be given in the form

$$
x ( t ) = x ( 0 ) e ^ { - ( k _ { 1 } / k _ { 2 } ) z ( t ) } \quad { \mathrm { a n d } } \quad y ( t ) = m - x ( t ) - z ( t ) ,
$$

where $k _ { 1 }$ is the infective rate, $k _ { 2 }$ is the removal rate, and $z ( t )$ is determined from the differential equation

$$
z ^ { \prime } ( t ) = k _ { 2 } \left( m - z ( t ) - x ( 0 ) e ^ { - ( k _ { 1 } / k _ { 2 } ) z ( t ) } \right) .
$$

The authors are not aware of any technique for solving this problem directly, so a numerical procedure must be applied. Find an approximation to $z ( 3 0 ) , y ( 3 0 )$ ，and $x ( 3 0 )$ , assuming that $m = 1 0 0 , 0 0 0 , x ( 0 ) = 9 9 , 0 0 0 , k _ { \mathrm { t } } = 2 \times 1 0 ^ { - 6 }$ ,and $k _ { 2 } = 1 0 ^ { - 4 }$

# 5.6 Multistep Methods

The methods discussed to this point in the chapter are called one-step methods because the approximation for the mesh point $t _ { i + 1 }$ involves information from only one of the previous mesh points, $t _ { i }$ . Although these methods might use functional evaluation information at points between $t _ { i }$ and $t _ { i + 1 }$ ,they do not retain that information for direct use in future approximations. All the information used by these methods is obtained within the subinterval over which the solution is being approximated. /

Since the approximate solution is available at each of the mesh points $t _ { 0 } , t _ { 1 } , \ldots , t _ { i }$ before the approximation at $t _ { i + 1 }$ is obtained,and because the error $ { \vert w _ { j } - y ( t _ { j } ) \vert }$ tends to increase with $j$ , it seems reasonable to develop methods that use these more accurate previous data when approximating the solution at $t _ { i + 1 }$

Methods using the approximation at more than one previous mesh point to determine the approximation at the next point are called multistep methods. The precise definition of these methods follows,together with the definition of the two types of multistep methods.

# Definition 5.14

An m-step multistep method for solving the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

has adifference equation for finding the aproximation ${ \pmb w } _ { i + 1 }$ at the mesh point $t _ { i + 1 }$ repre-sented by the following equation, where m is an integer greater than 1:

$$
\begin{array} { r } { w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } \quad } \\ { \quad \quad + h [ b _ { m } f ( t _ { i + 1 } , w _ { i + 1 } ) + b _ { m - 1 } f ( t _ { i } , w _ { i } ) \quad } \\ { \quad \quad + \cdot \cdot \cdot + b _ { 0 } f ( t _ { i + 1 - m } , w _ { i + 1 - m } ) ] , } \end{array}
$$

for $i \ = \ m - \ 1 , m , \dots , N - 1$ ， where $\hbar ~ = ~ ( b - a ) / N$ ，the $a _ { 0 } , a _ { 1 } , \ldots , a _ { m - 1 }$ and $b _ { 0 } , b _ { 1 } , \ldots , b _ { m }$ are constants, and the starting values

$$
w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , \quad \ldots , \quad w _ { m - 1 } = \alpha _ { m - 1 }
$$

are specified.

When $b _ { m } = 0$ the method iscalled expicit,or open,sinceEq. (5.23)tn gives $w _ { i + 1 }$ explicitly in terms of previously determined values.When $b _ { m } \neq 0$ the method is called implicit, or closed, since $w _ { i + 1 }$ occurs on both sides of Eq. (5.23) and is specified only implicitly.

# EXAMPLE 1 The equations

$$
\begin{array} { l r } { { w _ { 0 } = \alpha , } } & { { w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , \quad w _ { 3 } = \alpha _ { 3 } , } } & { { ( 5 . 2 ) } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { } i _ { i + 1 } = w _ { i } + { \cfrac { h } { 2 4 } } [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 3 } ) ] } } \end{array}
$$

for each $i = 3 , 4 , \dots , N - 1$ ,define an explicit four-step method known as the fourthorder Adams-Bashforth technique. The equations

$$
\begin{array} { c c } { { w _ { 0 } = \alpha , } } & { { w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , } } \\ { { } } & { { } } \\ { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 2 4 } [ 9 f ( t _ { i + 1 } , w _ { i + 1 } ) + 1 9 f ( t _ { i } , w _ { i } ) - 5 f ( t _ { i - 1 } , w _ { i - 1 } ) + f ( t _ { i - 2 } , w _ { i - 2 } ) ] , } } \end{array}
$$

for each $i = 2 , 3 , \dots , N - 1$ , define an implicit three-step method known as the fourthorder Adams-Moulton technique.

The starting values in either (5.24)or (5.25) must be specified, generally by assuming $w _ { 0 } = \alpha$ and generating the remaining values by either a Runge-Kutta method or some other one-step technique.

To apply an implicit method such as (5.25) directly, we must solve the implicit equation for $w _ { i + 1 }$ . It is not clear that this can be done in general or that a unique solution for $w _ { i + 1 }$ will always be obtained.

To begin the derivation of a multistep method, note that the solution to the initial-value problem (5.22),if integrated over the interval $[ t _ { i } , t _ { i + 1 } ]$ ,has the property that

$$
y ( t _ { i + 1 } ) - y ( t _ { i } ) = \int _ { t _ { i } } ^ { t _ { i + 1 } } y ^ { \prime } ( t ) d t = \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t .
$$

Consequently,

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t .
$$

Since we cannot integrate $f ( t , y ( t ) )$ without knowing $y ( t )$ , the solution to the problem, we instead integrate an interpolating polynomial $P ( t )$ to $f ( t , y ( t ) )$ that is determined by some of the previously obtained data points $( t _ { 0 } , w _ { 0 } ) , ( t _ { 1 } , w _ { 1 } )$ ，·， $( t _ { i } , w _ { i } )$ . When we assume,in addition, that $y ( t _ { i } ) \approx w _ { i }$ ,Eq. (5.26) becomes

$$
y ( t _ { i + 1 } ) \approx w _ { i } + \int _ { t _ { i } } ^ { t _ { i + 1 } } P ( t ) d t .
$$

Although any form of the interpolating polynomial can be used for the derivation, it is most convenient to use the Newton backward-difference formula.

To derive an Adams-Bashforth explicit $m$ -step technique,we form the backwarddifference polynomial $P _ { m - 1 } ( t )$ through $( t _ { i } , f ( t _ { i } , y ( t _ { i } ) ) )$ ， $( t _ { i - 1 } , f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) ) , \ldots ,$ $( t _ { i + 1 - m } , f ( t _ { i + 1 - m } , y ( t _ { i + 1 - m } ) ) )$ . Since $P _ { m - 1 } ( t )$ is an interpolatory polynomial of degree $m - 1$ , some number $\xi _ { i }$ in $( t _ { i + 1 - m } , t _ { i } )$ exists with

$$
f ( t , y ( t ) ) = P _ { m - 1 } ( t ) + \frac { f ^ { ( m ) } ( \xi _ { i } , y ( \xi _ { i } ) ) } { m ! } ( t - t _ { i } ) ( t - t _ { i - 1 } ) \cdot \cdot \cdot ( t - t _ { i + 1 \cdots m } ) .
$$

Introducing the variable substitution $t = t _ { i } + s h$ , with $d t = h d s$ into $P _ { m - 1 } ( t )$ and the error term implies that

$$
\begin{array} { l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t = \int _ { t _ { i } } ^ { t _ { i + 1 } } \sum _ { k = 0 } ^ { m - 1 } ( - 1 ) ^ { k } \binom { - s } { k } \nabla ^ { k } f ( t _ { i } , y ( t _ { i } ) ) d t } \\ { + \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } \frac { f ^ { ( m ) } ( \xi _ { i } , y ( \xi _ { i } ) ) } { m ! } ( t - t _ { i } ) ( t - t _ { i - 1 } ) \cdot \cdot ( t - t _ { i + 1 - m } ) d t } \end{array}
$$

$$
\begin{array} { l } { \displaystyle = \sum _ { k = 0 } ^ { m - 1 } \nabla ^ { k } f ( t _ { i } , y ( t _ { i } ) ) h ( - 1 ) ^ { k } \int _ { 0 } ^ { 1 } \left( { \binom { - s } { k } } d s \right. } \\ { \displaystyle \left. + \frac { h ^ { m + 1 } } { m ! } \int _ { 0 } ^ { 1 } s ( s + 1 ) \cdots ( s + m - 1 ) f ^ { ( m ) } ( \xi _ { i } , y ( \xi _ { i } ) ) d s . \right. } \end{array}
$$

The integrals $\begin{array} { r } { ( - 1 ) ^ { k } \int _ { 0 } ^ { 1 } \binom { - s } { k } d s } \end{array}$ for various values of $k$ are easily evaluated and are listed in Table 5.10. For example, when $k = 3$ ，

$$
\begin{array} { c } { { ( - 1 ) ^ { 3 } \displaystyle \int _ { 0 . } ^ { 1 } \left( _ { 3 } ^ { - s } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } \frac { ( - s ) ( - s - 1 ) ( - s - 2 ) } { 1 \cdot 2 \cdot 3 } d s } } \\ { { = \displaystyle \frac { 1 } { 6 } \displaystyle \int _ { 0 } ^ { 1 } ( s ^ { 3 } + 3 s ^ { 2 } + 2 s ) d s } } \\ { { = \displaystyle \frac { 1 } { 6 } \left[ \frac { s ^ { 4 } } { 4 } + s ^ { 3 } + s ^ { 2 } \right] _ { 0 } ^ { 1 } = \displaystyle \frac { 1 } { 6 } \left( \displaystyle \frac { 9 } { 4 } \right) = \displaystyle \frac { 3 } { 8 } . } } \end{array}
$$

# Table 5.10

<table><tr><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>(-1) S()ds</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>i</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>28</td></tr></table>

As a consequence,

$$
\begin{array} { r } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t = h \left[ f ( t _ { i } , y ( t _ { i } ) ) + \frac { 1 } { 2 } \nabla f ( t _ { i } , y ( t _ { i } ) ) + \frac { 5 } { 1 2 } \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) + \cdots \right] } \\ { + \displaystyle \frac { h ^ { m + 1 } } { m ! } \int _ { 0 } ^ { 1 } s ( s + 1 ) \cdot \cdot \cdot ( s + m - 1 ) f ^ { ( m ) } ( \xi _ { i } , y ( \xi _ { i } ) ) d s . \quad \mathrm { ~ ( ~ s ~ o ~ n ~ o ~ d ~ \xi ~ ) ~ } } \end{array}
$$

Since $s ( s + 1 ) \cdots ( s + m - 1 )$ does not change sign on [0,1],the Weighted Mean Value Theorem for Integrals can be used to deduce that for some number $\mu _ { i }$ ，where $t _ { i + 1 - m } <$ $\mu _ { i } < t _ { i + 1 }$ , the error term in Eq. (5.28) becomes

$$
{ \begin{array} { r l } & { { \frac { \hbar ^ { m + 1 } } { m ! } } \displaystyle \int _ { 0 } ^ { 1 } s ( s + 1 ) \cdot \cdot \cdot ( s + m - 1 ) f ^ { ( m ) } ( \xi _ { i } , y ( \xi _ { i } ) ) \ d s } \\ & { \quad \quad \quad = { \frac { h ^ { m + 1 } f ^ { ( m ) } ( \mu _ { i } , y ( \mu _ { i } ) ) } { m ! } } \displaystyle \int _ { 0 } ^ { 1 } s ( s + 1 ) \cdot \cdot \cdot ( s + m - 1 ) \ d s } \end{array} }
$$

or

$$
h ^ { m + 1 } f ^ { ( m ) } ( \mu _ { i } , y ( \mu _ { i } ) ) ( - 1 ) ^ { m } \int _ { 0 } ^ { 1 } \left( { - s \atop m } \right) d s .
$$

Since $\begin{array} { r } { y ( t _ { i + 1 } ) - y ( t _ { i } ) = \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t , } \end{array}$ ,Eq. (5.26) can be written as

$$
\begin{array} { l } { \displaystyle { y ( t _ { i + 1 } ) = y ( t _ { i } ) + h \left[ f ( t _ { i } , y ( t _ { i } ) ) + \frac { 1 } { 2 } \nabla f ( t _ { i } , y ( t _ { i } ) ) + \frac { 5 } { 1 2 } \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) + \cdot \cdot \cdot \cdot \right] } } \\ { \displaystyle { \quad \qquad + h ^ { m + 1 } f ^ { ( m ) } ( \mu _ { i } , y ( \mu _ { i } ) ) ( - 1 ) ^ { m } \int _ { 0 } ^ { 1 } \left( \binom { - s } { m } \ d s . \right. \qquad } } \end{array}
$$

# EXAMPLE 2

To derive the three-step Adams-Bashforth technique, consider Eq. (5.30) with $m = 3$ ：

$$
\begin{array} { c } { { y ( t _ { i + 1 } ) \approx y ( t _ { i } ) + h [ f ( t _ { i } , y ( t _ { i } ) ) + { \displaystyle \frac { 1 } { 2 } } \nabla f ( t _ { i } , y ( t _ { i } ) ) + { \displaystyle \frac { 5 } { 1 2 } } \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) ] } } \\ { { { } } } \\ { { { } = y ( t _ { i } ) + h \{ f ( t _ { i } , y ( t _ { i } ) ) + { \displaystyle \frac { 1 } { 2 } } [ f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) ]  } } \\ { { { } } } \\ { { { } ~ + { \displaystyle \frac { 5 } { 1 2 } } [ f ( t _ { i } , y ( t _ { i } ) ) - 2 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) ] \} } } \\ { { { } } } \\ { { { } { } = y ( t _ { i } ) + { \displaystyle \frac { h } { 1 2 } } [ 2 3 f ( t _ { i } , y ( t _ { i } ) ) - 1 6 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 5 f ( t _ { i - 2 } , y ( t _ { i - 1 } ) ) ] } } \end{array}
$$

The three-step Adams-Bashforth method is,consequently,

$$
\begin{array} { c } { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , } } \\ { { \displaystyle } } \\ { { w _ { i + 1 } = w _ { i } + \frac { h } { 1 2 } [ 2 3 f ( t _ { i } , w _ { i } ) - 1 6 f ( t _ { i - 1 } , w _ { i - 1 } ) ] + 5 f ( t _ { i - 2 } , w _ { i - 2 } ) ] , } } \end{array}
$$

for $i = 2 , 3 , \dots , N - 1$

Multistep methods can also be derived by using Taylor series. An example of the procedure nvolved is considered in Exercise 10. A derivation using a Lagrange interpolating polynomial is discussed in Exercise 9.

The local truncation error for multistep methods is defined analogously to that of onestep methods.As in the case of one-step methods, the local truncation error provides a measure of how the solution to the differential equation fails to solve the difference equation.

# Definition 5.15

If $y ( t )$ is the solution to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

and

$$
\begin{array} { c } { { w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } } } \\ { { \nonumber } } \\ { { + h [ b _ { m } f ( t _ { i + 1 } , w _ { i + 1 } ) + b _ { m - 1 } f ( t _ { i } , w _ { i } ) + \cdot \cdot \cdot + b _ { 0 } f ( t _ { i + 1 - m } , w _ { i + 1 - m } ) ] } } \end{array}
$$

is the $( i + 1 )$ st step in a multistep method, the local truncation error at this step is

$$
\begin{array} { l } { \displaystyle \tau _ { i + 1 } ( h ) = \frac { y ( t _ { i + 1 } ) - a _ { m - 1 } y ( t _ { i } ) - \cdot \cdot \cdot - a _ { 0 } y ( t _ { i + 1 - m } ) } { h } } \\ { \displaystyle - [ b _ { m } f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) + \cdot \cdot \cdot + b _ { 0 } f ( t _ { i + 1 - m } , y ( t _ { i + 1 - m } ) ) ] , } \end{array}
$$

for each $i = m - 1 , m , \dots , N - 1$ ：

To determine the local truncation error for the three-step Adams-Bashforth method derived in Example 2,consider the formof the error given in Eq. (5.29)andthe appropriate entry in Table 5.10:

$$
h ^ { 4 } f ^ { ( 3 ) } ( \mu _ { i } , y ( \mu _ { i } ) ) ( - 1 ) ^ { 3 } \int _ { 0 } ^ { 1 } \left( { - s \atop 3 } \right) d s = \frac { 3 h ^ { 4 } } { 8 } f ^ { ( 3 ) } ( \mu _ { i } , y ( \mu _ { i } ) ) .
$$

Using the fact that $f ^ { ( 3 ) } ( \mu _ { i } , y ( \mu _ { i } ) ) = y ^ { ( 4 ) } ( \mu _ { i } )$ and the diference equation derived in Example 2, we have

$$
\begin{array} { r l r } & { } & { \tau _ { i + 1 } ( h ) = \frac { y ( t _ { i + 1 } ) - y ( t _ { i } ) } { h } - \frac { 1 } { 1 2 } [ 2 3 f ( t _ { i } , y ( t _ { i } ) ) - 1 6 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 5 f ( t _ { i - 2 } , y ( t _ { i - 1 } ) ) } \\ & { } & { \quad \quad = \frac { 1 } { h } \left[ \frac { 3 h ^ { 4 } } { 8 } f ^ { ( 3 ) } ( \mu _ { i } , y ( \mu _ { i } ) ) \right] = \frac { 3 h ^ { 3 } } { 8 } y ^ { ( 4 ) } ( \mu _ { i } ) , \quad \mathrm { f o r ~ s o m e } \ \mu _ { i } \in ( t _ { i - 2 } , t _ { i + 1 } ) . } \end{array}
$$

Some of the explicit multistep methods together with theirrequired starting values and local truncation errors are as follows. The derivation of these techniques is similar to the procedure in Examples 2 and 3.

# Adams-Bashforth Two-Step Explicit Method:

$$
\begin{array} { c } { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , } } \\ { { } } \\ { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 2 } [ 3 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) ] , } } \end{array}
$$

where $i = 1 , 2 , \dots , N - 1$ .The local truncation error is $\textstyle \tau _ { i + 1 } ( h ) = { \frac { 5 } { 1 2 } } y ^ { \prime \prime \prime } ( \mu _ { i } ) h ^ { 2 }$ ,for some $\mu _ { i } \in ( t _ { i - 1 } , t _ { i + 1 } )$ ·

# Adams-Bashforth Three-Step Explicit Method:

$$
\begin{array} { c } { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , } } \\ { { \mathrm { } } } \\ { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 1 2 } [ 2 3 f ( t _ { i } , w _ { i } ) - 1 6 f ( t _ { i - 1 } , w _ { i - 1 } ) + 5 f ( t _ { i - 2 } , w _ { i - 2 } ) ] , } } \end{array}
$$

where $i = 2 , 3 , \dots , N - 1$ .The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = \frac { 3 } { 8 } y ^ { ( 4 ) } ( \mu _ { i } ) h ^ { 3 } } \end{array}$ ,for some $\mu _ { i } \in ( t _ { i - 2 } , t _ { i + 1 } )$ ·

# Adams-Bashforth Four-Step Explicit Method:

$$
\begin{array} { c c } { { w _ { 0 } = \alpha , } } & { { w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , \quad w _ { 3 } = \alpha _ { 3 } , } } \\ { { } } & { { } } \\ { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 2 4 } [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 3 } ) + 3 7 f ( t _ { i - 1 } , w _ { i - 1 } ) ] . } } \end{array}
$$

where $i = 3 , 4 , \dots , N - 1$ . The local truncation err is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = \frac { 2 5 1 } { 7 2 0 } y ^ { ( 5 ) } ( \mu _ { i } ) h ^ { 4 } } \end{array}$ ,for some $\mu _ { i } \in ( t _ { i - 3 } , t _ { i + 1 } )$ ·

# Adams-Bashforth Five-Step Explicit Method:

$$
\begin{array} { c } { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , \quad w _ { 3 } = \alpha _ { 3 } , \quad w _ { 4 } = \alpha _ { 4 } , } } \\ { { \displaystyle } } \\ { { w _ { i + 1 } = w _ { i } + \frac { h } { 7 2 0 } [ 1 9 0 1 f ( t _ { i } , w _ { i } ) - 2 7 7 4 f ( t _ { i - 1 } , w _ { i - 1 } ) } } \\ { { \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle } } \end{array}
$$

where $i = 4 , 5 , \dots , N - 1$ . The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = \frac { 9 5 } { 2 8 8 } y ^ { ( 6 ) } ( \mu _ { i } ) h ^ { 5 } } \end{array}$ , for some $\mu _ { i } \in ( t _ { i - 4 } , t _ { i + 1 } )$ ，

Implicit methods are derived by using $( t _ { i + 1 } , f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) )$ as an additional interpolation node in the approximation of the integral

$$
\int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t .
$$

Some of the more common implicit methods are as follows.

# Adams-Moulton Two-Step Implicit Method:

$$
\begin{array} { r c l } { { } } & { { } } & { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , } } \\ { { } } & { { } } & { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 1 2 } \{ 5 f ( t _ { i + 1 } , w _ { i + 1 } ) + 8 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) \} , } } \end{array}
$$

where $i = 1 , 2 , \dots , N - 1$ . The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = - \frac { 1 } { 2 4 } y ^ { ( 4 ) } ( \mu _ { i } ) h ^ { 3 } } \end{array}$ ,for some $\mu _ { i } \in ( t _ { i - 1 } , t _ { i + 1 } )$

# Adams-Moulton Three-Step Implicit Method:

$$
\begin{array} { c c } { { w _ { 0 } = \alpha , } } & { { w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , } } \\ { { } } & { { } } \\ { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 2 4 } [ 9 f ( t _ { i + 1 } , w _ { i + 1 } ) + 1 9 f ( t _ { i } , w _ { i } ) - 5 f ( t _ { i - 1 } , w _ { i - 1 } ) + f ( t _ { i - 2 } , w _ { i - 2 } ) ] , } } \end{array}
$$

where $i = 2 , 3 , \dots , N - 1$ . The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = - \frac { 1 9 } { 7 2 0 } y ^ { ( 5 ) } ( \mu _ { i } ) h ^ { 4 } } \end{array}$ ,for some $\mu _ { i } \in ( t _ { i - 2 } , t _ { i + 1 } )$

# Adams-Moulton Four-Step Implicit Method:

$$
\begin{array} { r c l } { { } } & { { } } & { { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad w _ { 2 } = \alpha _ { 2 } , \quad w _ { 3 } = \alpha _ { 3 } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { h } { 7 2 0 } [ 2 5 1 f ( t _ { i + 1 } , w _ { i + 1 } ) + 6 4 6 f ( t _ { i } , w _ { i } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - 2 6 4 f ( t _ { i - 1 } , w _ { i - 1 } ) + 1 0 6 f ( t _ { i - 2 } , w _ { i - 2 } ) - 1 9 f ( t _ { i - 3 } , w _ { i - 3 } ) ] , } } \end{array}
$$

where $i = 3 , 4 , \dots , N - 1$ . The local truncation rror is $\begin{array} { r } { \tau _ { i + 1 } ( h ) = - \frac { 3 } { 1 6 0 } y ^ { ( 6 ) } ( \mu _ { i } ) h ^ { 5 } } \end{array}$ ,for some $\mu _ { i } \in ( t _ { i - 3 } , t _ { i + 1 } )$ 、

It is interesting to compare an $m$ -step Adams-Bashforth explicit method to an $( m - 1 )$ - step Adams-Moulton implicit method. Both involve m evaluations of $f$ per step, and both have the terms $y ^ { ( m + 1 ) } ( \mu _ { i } ) h ^ { m }$ in their local truncation errors. In general, the coeficients of the terms involving $f$ in the local truncation error are smaller for the implicit methods than for the explicit methods. This leads to greater stability and smaller roundoff errors for the implicit methods.

EXAMPLE 4 Consider the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

and the approximations given by the explicit Adams-Bashforth four-step method and the implicit Adams-Moulton three-step method, both using $h = 0 . 2$

The Adams-Bashforth method has the difference equation

$$
w _ { i + 1 } = w _ { i } + { \frac { h } { 2 4 } } [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 3 } ) + 3 7 f ( t _ { i - 1 } , w _ { i - 1 } ) ] .
$$

for $i = 3 , 4 , \dots , 9$ .When simplified using $f ( t , y ) = y - t ^ { 2 } + 1 , h = 0 . 2$ ,and $t _ { i } = 0 . 2 i$ ， it becomes

$$
w _ { i + 1 } = \frac { 1 } { 2 4 } [ 3 5 w _ { i } - 1 1 . 8 w _ { i - 1 } + 7 . 4 w _ { i - 2 } - 1 . 8 w _ { i - 3 } - 0 . 1 9 2 i ^ { 2 } - 0 . 1 9 2 i + 4 . 7 3 6 ] .
$$

The Adams-Moulton method has the difference equation

$$
\upsilon _ { i + 1 } = \upsilon _ { i } + \frac { h } { 2 4 } [ 9 f ( t _ { i + 1 } , \upsilon _ { i + 1 } ) + 1 9 f ( t _ { i } , \upsilon _ { i } ) - 5 f ( t _ { i - 1 } , \upsilon _ { i - 1 } ) + f ( t _ { i - 2 } , \upsilon _ { i - 2 } ) ] ,
$$

for $i = 2 , 3 , \dots , 9$ . This reduces to

$$
w _ { i + 1 } = \frac { 1 } { 2 4 } [ 1 . 8 w _ { i + 1 } + 2 7 . 8 w _ { i } - w _ { i - 1 } + 0 . 2 w _ { i - 2 } - 0 . 1 9 2 i ^ { 2 } - 0 . 1 9 2 i + 4 . 7 3 6 ] .
$$

To use this method explicitly, we solve for $w _ { i + 1 }$ ,which gives

$$
w _ { i + 1 } = { \frac { 1 } { 2 2 . 2 } } [ 2 7 . 8 w _ { i } - w _ { i - 1 } + 0 . 2 w _ { i - 2 } - 0 . 1 9 2 i ^ { 2 } - 0 . 1 9 2 i + 4 . 7 3 6 ] ,
$$

for $i = 2 , 3 , \dots , 9$

The results in Table 5.11 were obtained using the exact values from $y ( t ) = ( t + 1 ) ^ { 2 } -$ $0 . 5 e ^ { t }$ for ${ \pmb { \alpha } } , { \pmb { \alpha } } _ { 1 } , { \pmb { \alpha } } _ { 2 }$ , and $\alpha _ { 3 }$ in the explicit Adams-Bashforth case and for $\alpha , \alpha _ { 1 }$ ，and $\alpha _ { 2 }$ in the implicit Adams-Moulton case.

In Example 4 the implicit Adams-Moulton method gave better results than the explicit Adams-Bashforth method of the same order.Although this is generally the case, the implicit methods have the inherent weakness of first having to convert the method algebraically to an explicit representation for $w _ { i + 1 }$ . This procedure is not always possible,as can be seen by considering the elementary initial-value problem

$$
y ^ { \prime } = e ^ { y } , \quad 0 \leq t \leq 0 . 2 5 , \quad y ( 0 ) = 1 .
$$

Table 5.11   

<table><tr><td>t</td><td>Exact</td><td>Adams- Bashforth Wi</td><td>Error</td><td>Adams- Moulton Wi</td><td>Error</td></tr><tr><td>0.0</td><td>0.5000000</td><td></td><td></td><td></td><td></td></tr><tr><td>0.2</td><td>0.8292986</td><td></td><td></td><td></td><td></td></tr><tr><td>0.4</td><td>1.2140877</td><td></td><td></td><td></td><td></td></tr><tr><td>0.6</td><td>1.6489406</td><td></td><td></td><td>1.6489341</td><td>0.0000065</td></tr><tr><td>0.8</td><td>2.1272295</td><td>2.1273124</td><td>0.0000828</td><td>2.1272136</td><td>0.0000160</td></tr><tr><td>1.0</td><td>2.6408591</td><td>2.6410810</td><td>0.0002219</td><td>2.6408298</td><td>0.0000293</td></tr><tr><td>1.2</td><td>3.1799415</td><td>3.1803480</td><td>0.0004065</td><td>3.1798937</td><td>0.0000478</td></tr><tr><td>1.4</td><td>3.7324000</td><td>3.7330601</td><td>0.0006601</td><td>3.7323270</td><td>0.0000731</td></tr><tr><td>1.6</td><td>4.2834838</td><td>4.2844931</td><td>0.0010093</td><td>4.2833767</td><td>0.0001071</td></tr><tr><td>1.8</td><td>4.8151763</td><td>4.8166575</td><td>0.0014812</td><td>4.8150236</td><td>0.0001527</td></tr><tr><td>2.0</td><td>5.3054720</td><td>5.3075838</td><td>0.0021119</td><td>5.3052587</td><td>0.0002132</td></tr></table>

Since $f ( t , y ) = e ^ { y }$ , the three-step Adams-Moulton method has

$$
w _ { i + 1 } = w _ { i } + \frac { h } { 2 4 } [ 9 e ^ { w _ { i + 1 } } + 1 9 e ^ { w _ { i } } - 5 e ^ { w _ { i - 1 } } + e ^ { w _ { i - 2 } } ]
$$

as its difference equation,and thisequation cannotbe solved explicitly for $w _ { i + 1 }$

We could use Newton's method or the secant method to aproximate Wi+1, but this complicates the procedure considerably. In practice, implicit multistep methods are not used as described above. Rather, they are used to improve approximations obtained by explicit methods.The combination of an explicit and implicit technique is called a predictor-corrector method. The explicit method predicts an approximation, and the implicit method corrects this prediction.

Consider the following fourth-order method for solving an initial-value problem. The first step is to calculate the starting values $w _ { 0 } , w _ { 1 } , w _ { 2 }$ ,and $w _ { 3 }$ for the four-step explicit Adams-Bashforth method. To do this,we use a fourth-order one-step method,the Runge-Kuta method of order four. The next step is to calculate an approximation, ${ w _ { 4 } ^ { ( 0 ) } }$ ,to $y ( t _ { 4 } )$ using the explicit Adams-Bashforth method as predictor:

$$
w _ { 4 } ^ { ( 0 ) } = w _ { 3 } + \frac { h } { 2 4 } [ 5 5 f ( t _ { 3 } , w _ { 3 } ) - 5 9 f ( t _ { 2 } , w _ { 2 } ) + 3 7 f ( t _ { 1 } , w _ { 1 } ) - 9 f ( t _ { 0 } , w _ { 0 } ) ] .
$$

Tiso ${ w _ { 4 } ^ { ( 0 ) } }$ i Adams-Moulton method and using that method as a corrector. This gives

$$
w _ { 4 } ^ { ( 1 ) } = w _ { 3 } + \frac { h } { 2 4 } [ 9 f ( t _ { 4 } , w _ { 4 } ^ { ( 0 ) } ) + 1 9 f ( t _ { 3 } , w _ { 3 } ) - 5 f ( t _ { 2 } , w _ { 2 } ) + f ( t _ { 1 } , w _ { 1 } ) ] .
$$

Tly $f ( t _ { 4 } , w _ { 4 } ^ { ( 0 ) } )$ in the corretcor equation; all the other values of $f$ have been calculated for earlier approximations.

The value $\boldsymbol { w _ { 4 } ^ { ( 1 ) } }$ is then used as theapproximation to $y ( t _ { 4 } )$ , and the technique of using the Adams-Bashforth method as a predictor.and the Adams-Moulton method as a corrector is repeated to find ${ w _ { 5 } ^ { ( 0 ) } }$ and ${ w _ { 5 } ^ { ( 1 ) } }$ ,teiialaot $y ( t _ { 5 } )$ ,etc.

Improved approximations to $y ( t _ { i + 1 } )$ could be obtained by iterating the Adams-Moulton formula

$$
\upsilon _ { i + 1 } ^ { ( k + 1 ) } = w _ { i } + \frac { h } { 2 4 } [ 9 f ( t _ { i + 1 } , w _ { i + 1 } ^ { ( k ) } ) + 1 9 f ( t _ { i } , w _ { i } ) - 5 f ( t _ { i - 1 } , w _ { i - 1 } ) + f ( t _ { i - 2 } , w _ { i - 2 } ) ] .
$$

However, {wi+1 converges to the approximation given by the implicit formula rather than to the solution $y ( t _ { i + 1 } )$ , and it is usually more efficient to use a reduction in the step size if improved accuracy is needed.

Algorithm 5.4 is based on the fourth-order Adams-Bashforth method as predictor and one iteration of the Adams-Moulton method as corrector, with the starting values obtained from the fourth-order Runge-Kutta method.

# Adams Fourth-Order Predictor-Corrector

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

at $( N + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ：

INPUT endpoints $a , b$ ; integer $N$ ; initial condition $\pmb { \alpha }$

OUTPUTapproximation $w$ t0 $y$ at the $( N + 1 )$ values of $t$

Step1 Set $\begin{array} { r l } & { \mathrm { : } h = ( b - a ) / N ; } \\ & { \mathrm { ~ } t _ { 0 } = a ; } \\ & { \mathrm { ~ } w _ { 0 } = \alpha ; } \\ & { \mathrm { ~ } \mathrm { ) T P U T } \mathrm { ~ } ( t _ { 0 } , w _ { 0 } ) . } \end{array}$ OU

Step 2 For $i = 1 , 2 , 3$ ,do Steps 3-5. (Compute starting values using Runge-Kutta method.)

Step 3Set $\begin{array} { r l } & { { \cal K } _ { 1 } = h f ( t _ { i - 1 } , w _ { i - 1 } ) ; } \\ & { { \cal K } _ { 2 } = h f ( t _ { i - 1 } + h / 2 , w _ { i - 1 } + { \cal K } _ { 1 } / 2 ) ; } \\ & { { \cal K } _ { 3 } = h f ( t _ { i - 1 } + h / 2 , w _ { i - 1 } + { \cal K } _ { 2 } / 2 ) ; } \\ & { { \cal K } _ { 4 } = h f ( t _ { i - 1 } + h , w _ { i - 1 } + { \cal K } _ { 3 } ) . } \end{array}$

Step 4 Set $w _ { i } = w _ { i - 1 } + ( K _ { 1 } + 2 K _ { 2 } + 2 K _ { 3 } + K _ { 4 } ) / 6 ;$ $t _ { i } = a + i h$ ，

Step 5OUTPUT $( t _ { i } , w _ { i } )$ ·

Step $6$ For $i = 4 , \dots , N$ do Steps 7--10.

Step7 Set $t = a + i h$

$$
\begin{array} { r l } & { \imath = a + \imath n ; } \\ & { w = w _ { 3 } + h [ 5 5 f ( t _ { 3 } , w _ { 3 } ) - 5 9 f ( t _ { 2 } , w _ { 2 } ) + 3 7 f ( t _ { 1 } , w _ { 1 } ) } \\ & { \quad \quad - 9 f ( t _ { 0 } , w _ { 0 } ) ] / 2 4 ; \quad \quad ( P r e d i c t \quad w _ { i \cdot } ) } \\ & { w = w _ { 3 } + h [ 9 f ( t , w ) + 1 9 f ( t _ { 3 } , w _ { 3 } ) - 5 f ( t _ { 2 } , w _ { 2 } ) } \\ & { \quad \quad + f ( t _ { 1 } , w _ { 1 } ) ] / 2 4 . \quad \quad ( C o r r e c t \quad w _ { i \cdot } ) } \end{array}
$$

Step 8 OUTPUT $( t , w )$

Step 9For $j = 0 , 1 , 2$ set $t _ { j } = t _ { j + 1 }$ ;(Prepare for next iteration.) $w _ { j } = w _ { j + 1 } .$

![](images/8b759f19d7b01250ee286b4e617eee5cd9dd83e9826f7cba2915b2035746d8de.jpg)

Step 10 Set $t _ { 3 } = t$ ；$w _ { 3 } = w .$

Step 11 STOP.

# EXAMPLE 5

Table 5.12 lists the results obtained by using Algorithm 5.4 for the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

with $N = 1 0$ . The results here are more accurate than those in Example 4, which used only the corrector (that is, the implicit Adams-Moulton method), but this is not always the case.

Table 5.12   

<table><tr><td colspan="2"></td><td colspan="2">Error</td></tr><tr><td>ti</td><td>yi=y(ti）</td><td>Wi</td><td>lyi-wil</td></tr><tr><td>0.0</td><td>0.5000000</td><td>0.5000000</td><td>0</td></tr><tr><td>0.2</td><td>0.8292986</td><td>0.8292933</td><td>0.0000053</td></tr><tr><td>0.4</td><td>1.2140877</td><td>1.2140762</td><td>0.0000114</td></tr><tr><td>0.6</td><td>1.6489406</td><td>1.6489220</td><td>0.0000186</td></tr><tr><td>0.8</td><td>2.1272295</td><td>2.1272056</td><td>0.0000239</td></tr><tr><td>1.0</td><td>2.6408591</td><td>2.6408286</td><td>0.0000305</td></tr><tr><td>1.2</td><td>3.1799415</td><td>3.1799026</td><td>0.0000389</td></tr><tr><td>1.4</td><td>3.7324000</td><td>3.7323505</td><td>0.0000495</td></tr><tr><td>1.6</td><td>4.2834838</td><td>4.2834208</td><td>0.0000630</td></tr><tr><td>1.8</td><td>4.8151763</td><td>4.8150964</td><td>0.0000799</td></tr><tr><td>2.0</td><td>5.3054720</td><td>5.3053707</td><td>0.0001013</td></tr></table>

Other multistep methods can be derived using integration of interpolating polynomials over intervals of the form $[ t _ { j } , t _ { i + 1 } ]$ ,for $j \le i - 1$ , to obtain an approximation to $y \left( t _ { i + 1 } \right)$ · When an interpolating polynomial is integrated over $[ t _ { i - 3 } , t _ { i + 1 } ]$ ,the result is the explicit Milne's method:

$$
w _ { i + 1 } = w _ { i - 3 } + { \frac { 4 h } { 3 } } [ 2 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) + 2 f ( t _ { i - 2 } , w _ { i - 2 } ) ] ,
$$

which has local truncation error $\textstyle { \frac { 1 4 } { 4 5 } } h ^ { 4 } y ^ { ( 5 ) } ( \xi _ { i } )$ , for some $\xi _ { i } \in ( t _ { i - 3 } , t _ { i + 1 } )$ ·

This method is occasionally used as a predictor for the implicit Simpson's method,

$$
w _ { i + 1 } = w _ { i - 1 } + { \frac { h } { 3 } } [ f ( t _ { i + 1 } , w _ { i + 1 } ) + 4 f ( t _ { i } , w _ { i } ) + f ( t _ { i - 1 } , w _ { i - 1 } ) ] ,
$$

which has local truncation error $- ( h ^ { 4 } / 9 0 ) y ^ { ( 5 ) } ( \xi _ { i } )$ ,for some $\xi _ { i } \in ( t _ { i - 1 } , t _ { i + 1 } )$ ,and is obtained by integrating an interpolating polynomial over $[ t _ { i - 1 } , t _ { i + 1 } ]$

The local truncation error involved with a predictor-corrector method of the Milne-Simpson type is generally smaller than that of the Adams-Bashforth-Moulton method. But the technique has limited use because of roundoff error problems,which do not occur with the Adams procedure.Elaboration on this difficulty is given in Section 5.10.

# ExERcIsE SEt 5.6

1.Use allthe Adams-Bashforth methods to approximate the solutions to the folowing initialvalue problems. In each case use exact starting values,and compare the results to the actual values.

a. y= te -2y， $0 \leq t \leq 1$ ， $y ( 0 ) = 0$ ，with $h = 0 . 2$ ；actual solution $y ( t ) =$ $\frac { 1 } { 5 } t e ^ { 3 t } - \frac { 1 } { 2 5 } e ^ { 3 t } + \frac { 1 } { 2 5 } e ^ { - 2 t }$   
b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1$ with $h = 0 . 2$ ; actual solution $\begin{array} { r } { y ( t ) = t + \frac { 1 } { 1 - t } } \end{array}$   
$\pmb { \mathrm { c } } _ { \bullet }$ $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2 ,$ with $h = 0 . 2$ ； actual solution $y ( t ) = t \ln t + 2 t$   
d. $y ^ { \prime } = \cos 2 t + \sin 3 t$ ， $0 ~ \leq ~ t ~ \leq ~ 1$ $y ( 0 ) = 1$ ，with $h \ = \ 0 . 2$ ；actual solution $y ( t ) = { \textstyle { \frac { 1 } { 2 } } } \sin 2 t - { \textstyle { \frac { 1 } { 3 } } } \cos 3 t + { \textstyle { \frac { 4 } { 3 } } }$

2.Use all the Adams-Moulton methods to approximate the solutions to the Exercises 1(a), 1(c), and l(d). In each case use exact starting values,and explicitly solve for $w _ { i + 1 }$ . Compare the results to the actual values.

3. Use each of the Adams-Bashforth methods to approximate the solutions to the following initial-value problems.In each case use starting values obtained from the Runge-Kutta method of order four. Compare the results to the actual values.

a $y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 1$ ，with $h = 0 . 1$ ; actual solution $\begin{array} { r } { y ( t ) = \frac { t } { 1 + \ln t } } \end{array}$   
b. $y ^ { \prime } \equiv 1 + y / t + ( y / t ) ^ { 2 }$ ， $1 \leq t \leq 3$ $y ( 1 ) = 0$ ，with $h = 0 . 2$ ；actual solution $y ( t ) = t \tan ( \ln t )$   
c. $y ^ { \prime } = - ( y + 1 ) ( y + 3 ) , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = - 2 , \mathrm { w i t h ~ } h$ $h = 0 . 1$ ； actual solution $y ( t ) = - 3 + 2 / ( 1 + e ^ { - 2 t } )$ ·   
d. y= -5y+5t²+2t， $0 \leq t \leq 1$ ， $y ( 0 ) = 1 / 3$ ，with $h = 0 . 1$ ； actual solution $y ( t ) = t ^ { 2 } + { \frac { 1 } { 3 } } e ^ { - 5 t }$

4.Use Algorithm 5.4 to approximate the solutions to the initial-value problems in Exercise 1.

5.Use Algorithm 5.4 to approximate the solutions to the initial-value problems in Exercise 3.

6. Change Algorithm $5 . 4 ~ \mathsf { s o }$ that the corrector can be iterated for a given number $p$ iterations. Repeat Exercise 5 with $p = 2 , 3$ ,and 4 iterations.Which choice of $p$ gives the best answer for each initial-value problem?

7. The initial-value problem

$$
y ^ { \prime } = e ^ { y } , \quad 0 \leq t \leq 0 . 2 0 , \quad y ( 0 ) = 1
$$

has solution

$$
y ( t ) = 1 - \ln ( 1 - e t ) .
$$

Applying the three-step Adams-Moulton method to this problem is equivalent to finding the fixed point ${ w _ { i + 1 } }$ of

$$
g ( w ) = w _ { i } + { \frac { h } { 2 4 } } [ 9 e ^ { w } + 1 9 e ^ { w _ { i } } - 5 e ^ { w _ { i - 1 } } + e ^ { w _ { i - 2 } } ] .
$$

a. With $h = 0 . 0 1$ ,obtain $w _ { i + 1 }$ by functional iteration for $i = 2 , \ldots , 1 9$ using exact starting values $w _ { 0 } , w _ { 1 }$ ,and $w _ { 2 }$ . At each step use $w _ { i }$ to initially approximate $w _ { i + 1 }$ · b. Will Newton's method speed the convergence over functional iteration?

8. Use the Milne-Simpson Predictor-Corrector method to approximate the solutions to the initialvalue problems in Exercise 3.

9.a.Derive Eq. (5.32) by using the Lagrange form of the interpolating polynomial. b.Derive Eq.(5.34)by using Newton's backward-difference form ofthe interpolating polynomial.

10．Derive Eq. (5.33) by the following method. Set

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + a h f ( t _ { i } , y ( t _ { i } ) ) + b h f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + c h f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) .
$$

Expand $y ( t _ { i + 1 } ) , f ( t _ { i - 2 } , y ( t _ { i - 2 } ) )$ ，and $f ( t _ { i - 1 } , y ( t _ { i - 1 } ) )$ in Taylor series about $( t _ { i } , y ( t _ { i } ) )$ ，and equate the coefficients of $h$ ， $h ^ { 2 }$ and $h ^ { 3 }$ to obtain $a , b$ ,and $\pmb { c }$

11.Derive Eq. (5.36)and its local truncation error by using an appropriate form of an interpolating polynomial.

12.Derive Simpson's method by applying Simpson's rule to the integral

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 1 } ) = \int _ { t _ { i - 1 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t .
$$

13.Derive Milne's method by applying the open Newton-Cotes formula (4.29) to the integral

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \int _ { t _ { i - 3 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t .
$$

14.Verify the entries in Table 5.10.

# 5.7 Variable Step-Size Multistep Methods

The Runge-Kutta-Fehlberg method is used for error control because at each step it provides,at little additional cost, two approximations that can be compared and related to the local error. Predictor-corrector techniques always generate two approximations at each step, so they are natural candidates for error-control adaptation.

To demonstrate the error-control procedure, we will construct a variable step-size predictor-corrector method using the four-step explicit Adams-Bashforth method as predictor and the three-step implicit Adams-Moulton method as corrector.

The Adams-Bashforth four-step method comes from the relation

$$
\begin{array} { l } { \displaystyle y ( t _ { i + 1 } ) = y ( t _ { i } ) + \frac { h } { 2 4 } [ 5 5 f ( t _ { i } , y ( t _ { i } ) ) - 5 9 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } \\ { \displaystyle \qquad + 3 7 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) - 9 f ( t _ { i - 3 } , y ( t _ { i - 3 } ) ) ] + \frac { 2 5 1 } { 7 2 0 } y ^ { ( 5 ) } ( \hat { \mu } _ { i } ) h ^ { 5 } , } \end{array}
$$

for some $\hat { \mu } _ { i } \in ( t _ { i - 3 } , t _ { i + 1 } )$ . The assumption that the approximations $w _ { 0 } , w _ { 1 } , \ldots , w _ { i }$ are all exact implies that the Adams-Bashforth truncation error is

$$
\frac { y ( t _ { i + 1 } ) - w _ { i + 1 } ^ { ( 0 ) } } { h } = \frac { 2 5 1 } { 7 2 0 } y ^ { ( 5 ) } ( \hat { \mu } _ { i } ) h ^ { 4 } .
$$

A similar analysis of the Adams-Moulton three-step method, which comes from

$$
\begin{array} { l } { { \displaystyle y ( t _ { i + 1 } ) = y ( t _ { i } ) + \frac { h } { 2 4 } [ 9 f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) + 1 9 f ( t _ { i } , y ( t _ { i } ) ) - 5 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } } \\ { { \displaystyle \qquad + f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) ] - \frac { 1 9 } { 7 2 0 } y ^ { ( 5 ) } ( \tilde { \mu } _ { i } ) h ^ { 4 } , } } \end{array}
$$

for some $\tilde { \mu } _ { i } \in ( t _ { i - 2 } , t _ { i + 1 } )$ ,leads to the local truncation error

$$
\frac { y ( t _ { i + 1 } ) - w _ { i + 1 } } { h } = - \frac { 1 9 } { 7 2 0 } y ^ { ( 5 ) } ( \tilde { \mu _ { i } } ) h ^ { 4 } .
$$

To proceed further, we must make the assumption that for small values of $h$ ，

$$
y ^ { ( 5 ) } ( \hat { \mu } _ { i } ) \approx y ^ { ( 5 ) } ( \tilde { \mu } _ { i } ) .
$$

"he effectiveness of the error-control technique depends directly on this assumption. If we subtract Eq. (5.40) from Eq. (5.39), we have

$$
\frac { w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } } { h } = \frac { h ^ { 4 } } { 7 2 0 } [ 2 5 1 y ^ { ( 5 ) } ( \hat { \mu _ { i } } ) + 1 9 y ^ { ( 5 ) } ( \tilde { \mu _ { i } } ) ] \approx \frac { 3 } { 8 } h ^ { 4 } y ^ { ( 5 ) } ( \tilde { \mu _ { i } } ) ,
$$

so

$$
y ^ { ( 5 ) } ( \tilde { \mu _ { i } } ) \approx \frac { 8 } { 3 h ^ { 5 } } ( w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } ) .
$$

Using this result to eliminate the term involving $h ^ { 4 } y ^ { ( 5 ) } ( \tilde { \mu } _ { i } )$ from (5.40) gives the ap-proximation to the Adams-Moulton local truncation error

$$
| \tau _ { i + 1 } ( h ) | = \frac { | y ( t _ { i + 1 } ) - w _ { i + 1 } | } { h } \approx \frac { 1 9 h ^ { 4 } } { 7 2 0 } \cdot \frac { 8 } { 3 h ^ { 5 } } | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | = \frac { 1 9 | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } { 2 7 0 h } .
$$

Suppose we now reconsider (5.40) with a new step size $q h$ generating new approximations $\mathbf { \hat { \boldsymbol { w } } } _ { i + 1 } ^ { ( 0 ) }$ and $\hat { w } _ { i + 1 }$ . The object isto choose $q$ sothatthelocaratioeg (5.40) is bounded by a prescribed tolerance $\pmb { \mathcal { E } }$ . If we assume that the value $y ^ { ( 5 ) } ( \mu )$ in (5.40) associated with $q h$ is also approximated using (5.41), then

$$
\frac { | y ( t _ { i } + q h ) - \hat { w } _ { i + 1 } | } { q h } = \frac { 1 9 q ^ { 4 } h ^ { 4 } } { 7 2 0 } | y ^ { ( 5 ) } ( \mu ) | \approx \frac { 1 9 q ^ { 4 } h ^ { 4 } } { 7 2 0 } \left[ \frac { 8 } { 3 h ^ { 5 } } | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | \right] ,
$$

and we need to choose $q$ so that

$$
\frac { | y ( t _ { i } + q h ) - \hat { w } _ { i + 1 } | } { q h } \approx \frac { 1 9 q ^ { 4 } } { 2 7 0 } \frac { | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } { h } < \varepsilon .
$$

That is, we choose $q$ so that

$$
q < \left( \frac { 2 7 0 } { 1 9 } \frac { h \varepsilon } { | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } \right) ^ { 1 / 4 } \approx 2 \left( \frac { h \varepsilon } { | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } \right) ^ { 1 / 4 } .
$$

A number of approximation assumptions have been made in this development, so in practice $q$ is chosen conservatively,usually as

$$
q = 1 . 5 \left( \frac { h \varepsilon } { | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } \right) ^ { 1 / 4 } .
$$

A change in step size for a multistep method is more costly in terms of function evaluations than for a one-step method, since new, equally-spaced starting values must be com-puted. As a consequence, it is common practice to ignore the step-size change whenever the local truncation error is between $\varepsilon / 1 0$ and $\pmb { \varepsilon }$ ,that is, when

$$
\frac { \varepsilon } { 1 0 } < | \tau _ { i + 1 } ( h ) | = \frac { | y ( t _ { i + 1 } ) - w _ { i + 1 } | } { h } \approx \frac { 1 9 | w _ { i + 1 } - w _ { i + 1 } ^ { ( 0 ) } | } { 2 7 0 h } < \varepsilon .
$$

In addition, $q$ is given an upper bound to ensure that a single unusually accurate approximation does not result in too large a step size. Algorithm 5.5 incorporates this safeguard with an upper bound of 4.

Remember that since the multistep methods require equal step sizes for the starting values,any change in step size necessitates recalculating new starting values at that point. In Algorithm 5.5 this is done by calling a Runge-Kutta subalgorithm (Algorithm 5.2).

# Adams Variable Step-Size Predictor-Corrector

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha
$$

with local truncation error within a given tolerance:

INPUTendpoints $a , b$ ； initial condition $\pmb { \alpha }$ ; tolerance TOL; maximum step size hmax;  
minimum step size hmin.

OUTPUT $i , t _ { i } , w _ { i } , h$ where at the ith step $w _ { i }$ approximates $y ( t _ { i } )$ and the step size $h$ was used, or a message that the minimum step size was exceeded.

Step 1Set up a subalgorithm for the Runge-Kutta fourth-order method to be called $R K 4 ( h , v _ { 0 } , x _ { 0 } , v _ { 1 } , x _ { 1 } , v _ { 2 } , x _ { 2 } , v _ { 3 } , x _ { 3 } )$ that accepts as input a step size $h$ and starting values $v _ { 0 } \approx y ( x _ { 0 } )$ and returns $\{ ( x _ { j } , v _ { j } ) \mid j = 1 , 2 , 3 \}$ defined by the following:

$$
\begin{array} { r l } & { \cdots 1 - { n f } \left( { { x } _ { j - 1 } } , { { v } _ { j - 1 } } / { 2 } \right) , } \\ & { \begin{array} { r l } { K _ { 2 } = h f ( { { x } _ { j - 1 } } + { { h } } / { 2 } , { { v } _ { j - 1 } } + K _ { 1 } / 2 ) } \\ { K _ { 3 } = h f ( { { x } _ { j - 1 } } + { { h } } / 2 , { { v } _ { j - 1 } } + K _ { 2 } / 2 ) } \\ { K _ { 4 } = h f ( { { x } _ { j - 1 } } + { { h } } , { { v } _ { j - 1 } } + K _ { 3 } ) } \\ { { v _ { j } } = v _ { j - 1 } + ( K _ { 1 } + 2 K _ { 2 } + 2 K _ { 3 } + K _ { 4 } ) / 6 ; } \\ { { { x } _ { j } } = { { x } _ { 0 } } + j h . } \end{array} } \end{array}
$$

Step 2 Set $t _ { 0 } = a$ ；$w _ { 0 } = \alpha ;$

$h = h m a x$ ； $F L A G = 1$ ； (FLAG will be used to exit the loop in Step 4.) $L A S T = 0$ (LAST will indicate when the last value is calculated.) OUTPUT $( t _ { 0 } , w _ { 0 } )$

Step 3 Call $R K 4 ( h , w _ { 0 } , t _ { 0 } , w _ { 1 } , t _ { 1 } , w _ { 2 } , t _ { 2 } , w _ { 3 } , t _ { 3 } ) ;$ Set $N F L A G = 1$ ；  (Indicates computation from RK4.) $\begin{array} { l } { i = 4 ; } \\ { t = t _ { 3 } + h . } \end{array}$

Step 4 While $( F L A G = 1 )$ do Steps 5-20.

$$
\begin{array} { l } { \displaystyle { \textrm { t } W P = w _ { i - 1 } + \frac { h } { 2 4 } [ 5 5 f ( t _ { i - 1 } , w _ { i - 1 } ) - 5 9 f ( t _ { i - 2 } , w _ { i - 2 } ) } } \\ { \displaystyle { \qquad + 3 7 f ( t _ { i - 3 } , w _ { i - 3 } ) - 9 f ( t _ { i - 4 } , w _ { i - 4 } ) ] ; \quad ( P r e d i c t w _ { i } , ) } } \\ { \displaystyle { W C = w _ { i - 1 } + \frac { h } { 2 4 } [ 9 f ( t , W P ) + 1 9 f ( t _ { i - 1 } , w _ { i - 1 } ) } } \\ { \displaystyle { \qquad - 5 f ( t _ { i - 2 } , w _ { i - 2 } ) + f ( t _ { i - 3 } , w _ { i - 3 } ) ] ; \quad ( C o r r e c t w _ { i } . ) } } \\ { \displaystyle { \sigma = 1 9 | W C - W P | / ( 2 7 0 h ) . } } \end{array}
$$

Step $\sigma$ If $\sigma \le \mathit { T O L }$ then do Steps 7-16 (Result accepted.) else do Steps 17-19. (Result rejected.)

Step 7Set $w _ { i } = W C$ ; (Result accepted.) $t _ { i } = t .$

Step 8If $N F L A G = 1$ then for $j = i - 3 , i - 2 , i - 1 , i$ OUTPUT $( j , t _ { j } , w _ { j } , h )$ ； (Previous results also accepted.) else OUTPUT $( i , t _ { i } , w _ { i } , h )$ (Previous results already accepted.)

Step 9If $L A S T = 1$ then set $F L A G = 0$ (Next step is 20.) else do Steps 10-16.

![](images/00f941fb0a5878dcdcf61a75cc76e0cee9d1ecafd6cba12c12b8770cfc6415ff.jpg)

Step 10 Set $i = i + 1$ ；$N F L A G = 0$

Step 11 If $\sigma \le 0 . 1 T O L$ or $t _ { i - 1 } + h > b$ then do Steps 12-16. (Increase $h$ if it is more accurate than required or decrease h to include $b$ as a mesh point.)

Step 12 Set $q = ( T O L / ( 2 \sigma ) ) ^ { 1 / 4 } .$

Step 13 If $q > 4$ then set $h = 4 h$ else set $h = q h$ ，

Step 14 If $h > h m a x$ then set $h = h m a x$

Step 15 If $t _ { i - 1 } + 4 h > b$ then set $h = ( b - t _ { i - 1 } ) / 4 ;$ $L A S T = 1$

Step 16 Call $R K 4 ( h , w _ { i - 1 } , t _ { i - 1 } , w _ { i } , t _ { i } , w _ { i + 1 } , t _ { i + 1 } , w _ { i + 2 } , t _ { i + 2 } ) ;$ Set $N F L A G = 1$ ； $i = i + 3$ . (True branch completed. Next step is 20.)

Step 17 Set $q = ( T O L / ( 2 \sigma ) ) ^ { 1 / 4 }$ . (False branch from Step 6: Result rejected.)

Step 18 If $q < 0 . 1$ then set $h = 0 . 1 h$ else set $h = q h$

Step 19 If $h < h m i n$ then set $F L A G = 0$ ； OUTPUT('hmin exceeded') else if $N F L A G = 1$ then set $i = i - 3$ ； (Previous results also rejected.) Call $R K 4 ( h , w _ { i - 1 } , t _ { i - 1 } , w _ { i } , t _ { i } , w _ { i + 1 } , t _ { i + 1 } , w _ { i + 2 } , t _ { i + 2 } ) ;$ set $i = i + 3$ ； $N F L A G = 1$ .

![](images/e46f1e9a7ba9f8cf7a65d81c5495554c4ac716dd630afc80b38b3a65ff6555b9.jpg)

Step 20 Set $t = t _ { i - 1 } + h$

Step 21 STOP.

# Table 5.13 lists the results obtained using Algorithm 5.5 to find approximations to the solution of the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

# Table 5.13

<table><tr><td>i</td><td>y(ti）</td><td>Wi</td><td>hi</td><td>0i</td><td>ly(ti）-wil</td></tr><tr><td>0</td><td colspan="5">0.5 0.5</td></tr><tr><td>0.1257017</td><td>0.7002323</td><td>0.7002318</td><td>0.1257017</td><td>4.051 × 10-6</td><td>0.0000005</td></tr><tr><td>0.2514033</td><td>0.9230960</td><td>0.9230949</td><td>0.1257017</td><td>4.051 ×10-6</td><td>0.0000011</td></tr><tr><td>0.3771050</td><td>1.1673894</td><td>1.1673877</td><td>0.1257017</td><td>4.051 × 10-6</td><td>0.0000017</td></tr><tr><td>0.5028066</td><td>1.4317502</td><td>1.4317480</td><td>0.1257017</td><td>4.051 × 10-6</td><td>0.0000022</td></tr><tr><td>0.6285083</td><td>1.7146334</td><td>1.7146306</td><td>0.1257017</td><td>4.610 × 10-6</td><td>0.0000028</td></tr><tr><td>0.7542100</td><td>2.0142869</td><td>2.0142834</td><td>0.1257017</td><td>5.210 ×10-6</td><td>0.0000035</td></tr><tr><td>0.8799116</td><td>2.3287244</td><td>2.3287200</td><td>0.1257017</td><td>5.913 ×10-6</td><td>0.0000043</td></tr><tr><td>1.0056133</td><td>2.6556930</td><td>2.6556877</td><td>0.1257017</td><td>6.706 × 10-6</td><td>0.0000054</td></tr><tr><td>1.1313149</td><td>2.9926385</td><td>2.9926319</td><td>0.1257017</td><td>7.604 × 10-6</td><td>0.0000066</td></tr><tr><td>1.2570166</td><td>3.3366642</td><td>3.3366562</td><td>0.1257017</td><td>8.622 ×10-6</td><td>0.0000080</td></tr><tr><td>1.3827183</td><td>3.6844857</td><td>3.6844761</td><td>0.1257017</td><td>9.777 ×10-6</td><td>0.0000097</td></tr><tr><td>1.4857283</td><td>3.9697541</td><td>3.9697433</td><td>0.1030100</td><td>7.029 ×10-6</td><td>0.0000108</td></tr><tr><td>1.5887383</td><td>4.2527830</td><td>4.2527711</td><td>0.1030100</td><td>7.029 × 10-6</td><td>0.0000120</td></tr><tr><td>1.6917483</td><td>4.5310269</td><td>4.5310137</td><td>0.1030100</td><td>7.029 ×10-6</td><td>0.0000133</td></tr><tr><td>1.7947583</td><td>4.8016639</td><td>4.8016488</td><td>0.1030100</td><td>7.029 ×10-6</td><td>0.0000151</td></tr><tr><td>1.8977683</td><td>5.0615660</td><td>5.0615488</td><td>0.1030100</td><td>7.760 × 10-6</td><td>0.0000172</td></tr><tr><td>1.9233262</td><td>5.1239941</td><td>5.1239764</td><td>0.0255579</td><td>3.918× 10-8</td><td>0.0000177</td></tr><tr><td>1.9488841</td><td>5.1854932</td><td>5.1854751</td><td>0.0255579</td><td>3.918×10-8</td><td>0.0000181</td></tr><tr><td>1.9744421</td><td>5.2460056</td><td>5.2459870</td><td>0.0255579</td><td>3.918×10-8</td><td>0.0000186</td></tr><tr><td>2.0000000</td><td>5.3054720</td><td>5.3054529</td><td>0.0255579</td><td>3.918×10-8</td><td>0.0000191</td></tr></table>

which has solution $y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t }$ . Included in the input is the tolerance $T O L =$ $1 0 ^ { - 5 }$ , maximum step size hm ${ \bf \sigma } _ { a x } = 0 . 2 5$ ,and minimum step size hmin $= 0 . 0 1$ ·

# Exercise Set 5.7

1.Use the Adams Variable Step-Size Predictor-Corrector Algorithm with tolerance $T O L = 1 0 ^ { - 4 }$ ， $h m a x \ = \ 0 . 2 5$ ， and hmin $= \ 0 . 0 2 5$ to approximate the solutions to the given initial-value problems. Compare the results to the actual values.

$y ^ { \prime } = t e ^ { 3 t } - 2 y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ;$ actual solution $\begin{array} { r } { y ( t ) = \frac { 1 } { 5 } t e ^ { 3 t } - \frac { 1 } { 2 5 } e ^ { 3 t } + \frac { 1 } { 2 5 } e ^ { - 2 t } } \end{array}$ b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1 ;$ actual solution $y ( t ) = t + 1 / ( 1 - t )$ c. $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2 ;$ actual solution $y ( t ) = t \ln t + 2 t$ d. $\begin{array} { l l } { { y ^ { \prime } = \cos 2 t + \sin 3 t , } } & { { 0 \leq t \leq 1 , \quad y ( 0 ) = 1 ; } } \\ { { \frac { 1 } { 3 } \cos 3 t + \frac { 4 } { 3 } . } } & { { } } \end{array}$ actual solution $\begin{array} { r } { y ( t ) = \frac { 1 } { 2 } \sin 2 t - } \end{array}$

2. Use the Adams Variable Step-Size Predictor-Corrector Algorithm with $T O L = 1 0 ^ { - 4 }$ to approximate the solutions to the following initial-value problems:

a. $y ^ { \prime } = ( y / t ) ^ { 2 } + y / t , \quad 1 \leq t \leq 1 . 2 , \quad y ( 1 ) = 1$ with h $m a x = 0 . 0 5$ and $h m i n = 0 . 0 1$ b. $y ^ { \prime } = \sin t + e ^ { - t } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ,$ with $h m a x = 0 . 2$ and $h m i n = 0 . 0 1$ c. $y ^ { \prime } = ( 1 / t ) ( y ^ { 2 } + y ) , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = -$ ，with $h m a x = 0 . 4$ and hmi $\iota = 0 . 0 1$ d. $y ^ { \prime } = - t y + 4 t / y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1$ ，with $h m a x = 0 . 2$ and hm $i n = 0 . 0 1$ ，

3.Use the Adams Variable Step-Size Predictor-Corrector Algorithm with tolerance $T O L = 1 0 ^ { - 6 }$ ， $h m a x = 0 . 5$ ,and $h m i n = 0 . 0 2$ to approximate the solutions to the given initial-value problems. Compare the results to the actual values.

a. $y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 4 , \quad y ( 1 ) = 1 ;$ actual solution $y ( t ) = t / ( 1 + \ln t )$   
b. $y ^ { \prime } = 1 + y / t + ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = 0 ;$ actual solution $y ( t ) = t \tan ( \ln t )$ ·   
c. $y ^ { \prime } = - ( y + 1 ) ( y + 3 ) , \quad 0 \leq t \leq 3 , \quad y ( 0 ) = - 2$ ；actual solution $y ( t ) = - 3 + 2 ( 1 +$ $e ^ { - 2 t } ) ^ { - 1 }$   
d. $y ^ { \prime } = ( t + 2 t ^ { 3 } ) y ^ { 3 } - t y , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = { \frac { 1 } { 3 } } ;$ actual solution $y ( t ) = ( 3 + 2 t ^ { 2 } +$ 6et2)-1/2.

4. Construct an Adams Variable Step-Size Predictor-Corrector Algorithm based on the Adams-Bashforth five-step method and the Adams-Moulton four-step method. Repeat Exercise 3 using this new method.

5.An electrical circuit consists of a capacitor of constant capacitance $C \simeq 1 . 1$ farads in series with a resistor of constant resistance $R _ { 0 } = 2 . 1$ ohms. A voltage $\mathcal { E } ( t ) = 1 1 0 \mathrm { s i r }$ nt is applied at time $t = 0$ . When the resistor heats up, the resistance becomes a function of the current $i$ ，

$$
R ( t ) = R _ { 0 } + k i , \quad \mathrm { w h e r e \ } k = 0 . 9 ,
$$

and the differential equation for $i ( t )$ becomes

$$
\left( 1 + \frac { 2 k } { R _ { 0 } } i \right) \frac { d i } { d t } + \frac { 1 } { R _ { 0 } C } i = \frac { 1 } { R _ { 0 } C } \frac { d \mathcal { E } } { d t } .
$$

Find i(2),assuming that $i ( 0 ) = 0$

# 5.8 Extrapolation Methods

Extrapolation was used in Section 4.5 for the approximation of definite integrals,where we found that by correctly averaging relatively inaccurate trapezoidal approximations we could produce new approximations that are exceedingly accurate. In this section we will apply extrapolation to increase the accuracy of approximations to the solution of initialvalue problems.As we have previously seen, the original approximations must have an error expansion of a specific form for the procedure to be successful.

To apply extrapolation to solve initial-value problems,we use a technique based on the Midpoint method:

$$
w _ { i + 1 } = w _ { i - 1 } + 2 h f ( t _ { i } , w _ { i } ) , \quad { \mathrm { f o r ~ } } i \geq 1 .
$$

This technique requires two starting values since both $w _ { 0 }$ and $w _ { 1 }$ are needed before the first midpoint approximation, $w _ { 2 }$ , can be determined. As usual, one is the initial condition for $w _ { 0 } = y ( a ) = \alpha$ . To determine the second starting value, $w _ { 1 }$ ,we apply Euler's method. Subsequent approximations are obtained from (5.42).After a series of approximations of this type are generated ending at a value $t$ ,an endpoint correction is performed that involves the final two midpoint approximations. This produces an approximation $w ( t , h )$ to $y ( t )$ that has the form

$$
y ( t ) = w ( t , h ) + \sum _ { k = 1 } ^ { \infty } \delta _ { k } h ^ { 2 k } ,
$$

where the $\delta _ { k }$ are constants related to the derivatives of the solution $y ( t )$ . The important point is that the $\delta _ { k }$ do not depend on the step size $h$ . The details of this procedure can be found in the paper by Gragg $[ G r ]$

To illustrate the extrapolation technique for solving

$$
y ^ { \prime } ( t ) = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

let us assume that we have a fixed step size $h$ and that we wish to approximate $y ( t _ { 1 } ) =$ $y ( a + h )$

For the first extrapolation step we let $h _ { 0 } = h / 2$ and use Euler's method with $w _ { 0 } = \alpha$ to approximate $y ( a + h _ { 0 } ) = y ( a + h / 2 )$ as

$$
\begin{array} { r } { w _ { 1 } = w _ { 0 } + h _ { 0 } f ( a , w _ { 0 } ) . } \end{array}
$$

We then apply the Midpoint method with $t _ { i - 1 } = a$ and $t _ { i } = a + h _ { 0 } = a + h / 2$ to produce a first approximation to $y ( a + h ) = y ( a + 2 h _ { 0 } )$ ，

$$
w _ { 2 } = w _ { 0 } + 2 h _ { 0 } f ( a + h _ { 0 } , w _ { 1 } ) .
$$

The endpoint correction is applied to obtain the final approximation to $y ( a + h )$ for the step size $h _ { 0 }$ . This results in the $O ( h _ { 0 } ^ { 2 } )$ approximation to $y ( t _ { 1 } )$

$$
y _ { 1 , 1 } = \frac { 1 } { 2 } [ w _ { 2 } + w _ { 1 } + h _ { 0 } f ( a + 2 h _ { 0 } , w _ { 2 } ) ] .
$$

We save the approximation $y _ { 1 , 1 }$ and discard the intermediate results $w _ { 1 }$ and $w _ { 2 }$

To obtain the next approximation, $y _ { 2 , 1 }$ ，to $y ( t _ { 1 } )$ ，we let $h _ { 1 } = h / 4$ and use Euler's method with $w _ { 0 } = \alpha$ to obtain an approximation to $y ( a + h _ { 1 } ) = y ( a + h / 4 )$ that we will call $w _ { 1 }$ ：

$$
\begin{array} { r } { w _ { 1 } = w _ { 0 } + h _ { 1 } f ( a , w _ { 0 } ) . } \end{array}
$$

Next we produce approximations $w _ { 2 }$ to $y ( a + 2 h _ { 1 } ) = y ( a + h / 2 )$ and $w _ { 3 }$ to $y ( a +$ $3 h _ { 1 } ) = y ( a + 3 h / 4 )$ given by

$$
w _ { 2 } = w _ { 0 } + 2 h _ { 1 } f ( a + h _ { 1 } , w _ { 1 } ) \quad { \mathrm { a n d } } \quad w _ { 3 } = w _ { 1 } + 2 h _ { 1 } f ( a + 2 h _ { 1 } , w _ { 2 } ) .
$$

Then we produce the approximation $w _ { 4 }$ to $y ( a + 4 h _ { 1 } ) = y ( t _ { 1 } )$ given by

$$
w _ { 4 } = w _ { 2 } + 2 h _ { 1 } f ( a + 3 h _ { 1 } , w _ { 3 } ) .
$$

The endpoint correction is now applied to $w _ { 3 }$ and $w _ { 4 }$ to produce the improved $O ( h _ { 1 } ^ { 2 } )$ approximation to $y ( t _ { 1 } )$ ，

$$
y _ { 2 , 1 } = \frac { 1 } { 2 } [ w _ { 4 } + w _ { 3 } + h _ { 1 } f ( a + 4 h _ { 1 } , w _ { 4 } ) ] .
$$

Because of the form of the error given in (5.43), the two approximations to $y ( a + h )$ have the property that

$$
y ( a + h ) = y _ { 1 , 1 } + \delta _ { 1 } \left( { \frac { h } { 2 } } \right) ^ { 2 } + \delta _ { 2 } \left( { \frac { h } { 2 } } \right) ^ { 4 } + \cdots = y _ { 1 , 1 } + \delta _ { 1 } { \frac { h ^ { 2 } } { 4 } } + \delta _ { 2 } { \frac { h ^ { 4 } } { 1 6 } } + \cdots ,
$$

and

$$
y ( a + h ) = y _ { 2 , 1 } + \delta _ { 1 } \left( { \frac { h } { 4 } } \right) ^ { 2 } + \delta _ { 2 } \left( { \frac { h } { 4 } } \right) ^ { 4 } + \cdots = y _ { 2 , 1 } + \delta _ { 1 } { \frac { h ^ { 2 } } { 1 6 } } + \delta _ { 2 } { \frac { h ^ { 4 } } { 2 5 6 } } + \cdots .
$$

We can eliminate the $O ( h ^ { 2 } )$ portion of this truncation error by averaging these two formulas appropriately. Specifically, if we subtract the first formula from 4 times the second and divide the result by 3, we have

$$
y ( a + h ) = y _ { 2 , 1 } + \frac { 1 } { 3 } ( y _ { 2 , 1 } - y _ { 1 , 1 } ) - \delta _ { 2 } \frac { h ^ { 4 } } { 6 4 } + \cdot \cdot \cdot .
$$

So the approximation

$$
y _ { 2 , 2 } = y _ { 2 , 1 } + \frac { 1 } { 3 } ( y _ { 2 , 1 } - y _ { 1 , 1 } )
$$

has error of order $O ( h ^ { 4 } )$

Continuing in this manner, we next let $h _ { 2 } ~ = ~ h / 6$ and apply Euler's method once followed by the Midpoint method five times. Then we use the endpoint correction to determine the $h ^ { 2 }$ approximation, $y _ { 3 , 1 }$ ,to $y ( a + h )$ . This approximation can be averaged with $y _ { 2 , 1 }$ to produce a second ${ \cal O } ( h ^ { 4 } )$ approximation that we denote $y _ { 3 , 2 }$ . Then y3.2 and $y _ { 2 , 2 }$ are averaged to eliminate the ${ \cal O } ( h ^ { 4 } )$ error.terms and produce an approximation with error of order $O ( h ^ { 6 } )$ . Higher-order formulas are generated by continuing the process.

The only significant difference between the extrapolation performed here and that used for Romberg integration in Section 4.5 results from the way the subdivisions are chosen. In

Romberg integration there is a convenient formula for representing the Composite Trape-Zoidal rule approximations that uses consecutive divisions of the step size by the integers 1,2,4,8,16,32, 64,... This procedure permits the averaging process to proceed in an easily followed manner.

We do not have a means for easily producing refined approximations for initial-value problems, so the divisions for the extrapolation technique are chosen to minimize the number of required function evaluations. The averaging procedure arising from this choice of subdivision,shown in Table 5.14,is not as elementary, but,other than that,the process is the same as that used for Romberg integration.

# Table 5.14

<table><tr><td colspan="4">y1.1= w(t,ho)</td></tr><tr><td colspan="4">h y2.1= w(t,h1) y2,2 = y2,1 + (y2.1- y1.1)</td></tr><tr><td></td><td>-h H</td><td>H</td><td>(y3,2-y2.2)</td></tr><tr><td>y3.1 = w(t,h2)</td><td>y3,2 = y3,1 + (y3,1-y2.1) -</td><td>3.3=y3.2 + H-H</td><td></td></tr></table>

Algorithm 5.6 uses the extrapolation technique with the sequence of integers

$$
q _ { 0 } = 2 , ~ q _ { 1 } = 4 , ~ q _ { 2 } = 6 , ~ q _ { 3 } = 8 , ~ q _ { 4 } = 1 2 , ~ q _ { 5 } = 1 6 , ~ q _ { 6 } = 2 4 , ~ \mathrm { a n d } ~ q _ { 7 } = 3 2 .
$$

A basic step size $h$ is selected,and the method progresses by using $h _ { i } ~ = h / q _ { i }$ , for each $i = 0 , \ldots , 7$ , to approximate $y ( t + h )$ . The error is controlled by requiring that the approximations $y _ { 1 , 1 } , y _ { 2 , 2 } , \ldots$ ，be computed until $\{ y _ { i , i } - y _ { i - 1 , i - 1 } \}$ is less than a given tolerance. If the tolerance is not achieved by $i = 8$ ,then $h$ is reduced,and the process is reapplied. Minimum and maximum values of $h$ , hmin,and hmax, respectively, are specified to ensure control of the method. If $y _ { i , i }$ is found to be acceptable, then $w _ { 1 }$ is set to $y _ { i , i }$ and computations begin again to determine $w _ { 2 }$ ,which will approximate $y ( t _ { 2 } ) = y ( a + 2 h )$ . The process is repeated until the approximation $w _ { N }$ to $y ( b )$ is determined.

# Extrapolation

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

with local truncation error within a given tolerance:

INPUTendpoints $a , b$ ； initial condition $\alpha$ ; tolerance TOL; maximum step size hmax;  
minimum step size hmin.

OUTPUT $T$ ,W, $h$ where $W$ approximates $y ( t )$ and step size $h$ was used, or a message that minimum step size was exceeded.

Step1 Initialize the array $N K = ( 2 , 4 , 6 , 8 , 1 2 , 1 6 , 2 4 , 3 2 ) .$

Step 2 Set $T O = a$ ； $W O = \alpha$ ； $h = h m a x ;$ $F L A G = 1$ .(FLAG is used to exit the loop in Step 4.)

Step 3 Fori= 1,2,..,7 for $j = 1 , \dots , i$ set $Q _ { i , j } = ( N K _ { i + 1 } / N K _ { j } ) ^ { 2 } . ( N o t e { : } \quad Q _ { i , j } = h _ { j } ^ { 2 } / h _ { i + 1 } ^ { 2 } . )$

Step 4 While $F L A G = 1$ do Steps 5-20.

Step 5Set $k = 1$ ；

$N F L A G = 0$ (When desired accuracy is achieved, NFLAG is set to 1.)

Step 6 While( $( k \leq 8$ and ${ \cal N F L A G } = 0 $ do Steps 7-14.

$$
\begin{array} { r l } & { \mathfrak { s t } H K = h / N K _ { k } ; } \\ & { \begin{array} { r l } { T = T O ; } \\ { W 2 = W O ; } \\ { W 3 = W 2 + H K \cdot f ( T , W 2 ) ; } \end{array} } & { ( E u l e r ^ { \prime } s f r s t s t e p . ) } \\ & { \begin{array} { r l } { T = T O + H K . } \end{array} } \end{array}
$$

$$
T = T O + ( j + 1 ) \cdot H K
$$

Step 9 Set $y _ { k } = [ W 3 + W 2 + H K \cdot f ( T , W 3 ) ] / 2 .$ (End-point correction to compute yk,1.)

Step 10 If $k \geq 2$ then do Steps 11-13.   
(Note: $y _ { k - 1 } \equiv y _ { k - 1 , 1 } , y _ { k - 2 } \equiv y _ { k - 2 , 2 } , . . . , y _ { 1 } \equiv y _ { k - 1 , k - 1 }$ since only the previous row of the table is saved.)

Step 11 Set $\begin{array} { l } { { j = k ; } } \\ { { v = y _ { 1 } . ( S a v e y _ { k - 1 , k - 1 } . ) } } \end{array}$

Step 12 While $( j \geq 2 )$ do

$$
\mathsf { s e t } y _ { j - 1 } = y _ { j } + \frac { y _ { j } - y _ { j - 1 } } { Q _ { k - 1 , j - 1 } - 1 } ;
$$

(Extrapolation to compute $y _ { j - 1 } \equiv y _ { k , k - j + 2 } . )$

$$
\bigg ( N o t e   \cdot \mathrmtriangledown \ y _ { j - 1 } = \frac { h _ { j - 1 } ^ { 2 } y _ { j } - h _ { k } ^ { 2 } y _ { j - 1 } } { h _ { j - 1 } ^ { 2 } - h _ { k } ^ { 2 } } . \bigg )
$$

$$
j = j - 1 .
$$

Step 13 If $| y _ { 1 } - v | \leq T O L$ then set $N F L A G = 1$

$( y _ { 1 }$ is accepted as the new $w$ .）

Step 14 Set $k = k + 1$

Step 15 Set $k = k - 1$

Step 16 If $N F L A G = 0$ then do Steps 17 and 18(Result rejected.) else do Steps 19 and 20. (Result accepted.)

Step 17Set $h = h / 2$ . (New value for w rejected, decrease h.)

Step 18 If $h < h m i n$ then (True branch completed, next step is back to Step 4.)

Step 19 Set $W O = y _ { 1 }$ ； (New value for w accepted.)$T O = T O + h$ ；OUTPUT $( T O , W O , h )$

Step 20 If $T O \geq b$ then set $F L A G = 0$ (Procedure completed successfully.) else if $T O + h > b$ then set $h = b - T O$ (Terminate at $t = b$ ） else if $( k \leq 3$ and $h < 0 . 5 ( h m a x )$ then set $h = 2 h$ ， (Increase step size if possible.)

Step 21 STOP.

Consider the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

which has the solution $y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t }$ .The Extrapolation Algorithm will be applied to this problem with $h = 0 . 2 5$ ， $T O L = 1 0 ^ { - 1 0 }$ ， $h m a x = 0 . 2 5$ ,and hmin $= 0 . 0 1$ . Table 5.15 is obtained in the computation of $w _ { 1 }$

The computations stopped with $w _ { 1 } = y _ { 5 , 5 }$ because $| y _ { 5 , 5 } - y _ { 4 , 4 } | \le 1 0 ^ { - 1 0 }$ and $y _ { 5 , 5 }$ is accepted as the approximation to $y ( t _ { 1 } ) ~ = ~ y ( 0 . 2 5 )$ . The complete set of approximations accurate to the places listed is given in Table 5.16.

Table 5.15   

<table><tr><td>y1.1 = 0.9187011719</td><td></td><td></td><td></td></tr><tr><td>y2.1 = 0.9200379848</td><td>y2.2 = 0.9204835892</td><td></td><td></td></tr><tr><td>y3.1 = 0.9202873689</td><td>Y3.2 = 0.9204868761</td><td>3,3= 0.9204872870</td><td></td></tr><tr><td>：0.9203747896 y4.1 =</td><td>y4,2 = 0.9204871876</td><td>Y4.3 = 0.9204872914</td><td>Y4,4= 0.9204872917</td></tr><tr><td>ys. = 0.9204372763</td><td>Y5.2 = 0.9204872656</td><td>Y5.3 = 0.9204872916</td><td>y5,4 = 0.9204872917</td></tr></table>

Table 5.16   

<table><tr><td>t</td><td>yi=y(ti）</td><td>wi</td><td>hi</td><td>k</td></tr><tr><td>0.25</td><td>0.9204872917</td><td>0.9204872917</td><td>0.25</td><td>5</td></tr><tr><td>0.50</td><td>1.4256393646</td><td>1.4256393646</td><td>0.25</td><td>5</td></tr><tr><td>0.75</td><td>2.0039999917</td><td>2.0039999917</td><td>0.25</td><td>5</td></tr><tr><td>1.00</td><td>2.6408590858</td><td>2.6408590858</td><td>0.25</td><td>5</td></tr><tr><td>1.25</td><td>3.3173285213</td><td>3.3173285212</td><td>0.25</td><td>4</td></tr><tr><td>1.50</td><td>4.0091554648</td><td>4.0091554648</td><td>0.25</td><td>3</td></tr><tr><td>1.75</td><td>4.6851986620</td><td>4.6851986619</td><td>0.25</td><td>3</td></tr><tr><td>2.00</td><td>5.3054719505</td><td>5.3054719505</td><td>0.25</td><td>3</td></tr></table>