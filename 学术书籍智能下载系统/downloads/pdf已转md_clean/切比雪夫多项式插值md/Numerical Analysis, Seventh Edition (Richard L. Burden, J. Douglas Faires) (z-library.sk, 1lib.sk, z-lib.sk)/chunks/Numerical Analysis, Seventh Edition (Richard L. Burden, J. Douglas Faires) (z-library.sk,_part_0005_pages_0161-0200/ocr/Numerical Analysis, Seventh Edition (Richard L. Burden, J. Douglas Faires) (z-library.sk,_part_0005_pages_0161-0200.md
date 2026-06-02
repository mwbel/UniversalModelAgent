To use a clamped spline to approximate this curve we would need derivative approximations for the endpoints. Even if these approximations were available, we could expect litle improvement because of the close agreement of the free cubic spline to the curve of the top profile.

Constructing a cubic spline to approximate the lower profile of the ruddy duck would be more difficult since the curve for this portion cannot be expressed as a function of $x$ , and at certain points the curve does not appear to be smooth. These problems can be resolved by using separate splines to represent various portions of the curve, but a more effective approach to curves of this type is considered in the next section.

The clamped boundary conditions are generally preferred when approximating func-tions by cubic splines, so the derivative of the function must be estimated at the endpoints of the interval. When the nodes are equally spaced near both endpoints, approximations can be obtained by using Eq. (4.7) or any of the other appropriate formulas given in Sec-tions 4.1 and 4.2. When the nodes are unequally spaced,the problem is considerably more difficult.

To conclude this section, we list an error-bound formula for the cubic spline with clamped boundary conditions. The proof of this result can be found in [Schul, pp. 57-58].

Let $f \in C ^ { 4 } [ a , b ]$ with $\textstyle \operatorname* { m a x } _ { a \leq x \leq b } | f ^ { ( 4 ) } ( x ) | = M$ If $s$ is the unique clamped cubic spline interpolant to $f$ with respect to the nodes $a = x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } = b$ ,then

$$
\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - S ( x ) | \leq { \frac { 5 M } { 3 8 4 } } \operatorname* { m a x } _ { 0 \leq j \leq n - 1 } ( x _ { j + 1 } - x _ { j } ) ^ { 4 } .
$$

A fourth-order error-bound result also holds in the case offreeboundary conditions, butit is more diffcult to express. (See [BD,pp.827-835].)

The free boundary conditions will generally give less accurate results tan the clamped conditions near the ends of the interval $[ x _ { 0 } , x _ { n } ]$ unless the function $f$ happens to nearly satisfy $f ^ { \prime \prime } ( x _ { 0 } ) = f ^ { \prime \prime } ( x _ { n } ) = 0$ . An alternative to the free boundary condition that does not require knowledge of the derivative of $f$ is the not-a-knot condition,(see [Deb, pp.55-56]). This condition requires that $S ^ { \prime \prime \prime } ( x )$ be continuous at $x _ { 1 }$ and at $x _ { n - 1 }$

# Exercise Set 3.4

1.Determine the free cubic spline $s$ that interpolates the data $f ( 0 ) = 0$ ， $f ( 1 ) = 1$ , and $f ( 2 ) = 2$

2.Determine the clamped cubic spline $\pmb { \mathscr { s } }$ that interpolates the data $f ( 0 ) = 0 , f ( 1 ) = 1 , f ( 2 ) = 2$ and satisfies $s ^ { \prime } ( 0 ) = s ^ { \prime } ( 2 ) = 1$

3.Construct the free cubic spline for the following data.

<table><tr><td>a.</td><td>X</td><td>f(x)</td></tr><tr><td></td><td>8.3</td><td>17.56492</td></tr><tr><td></td><td>8.6</td><td>18.50515</td></tr></table>

<table><tr><td>b.</td><td>x</td><td>f(x)</td></tr><tr><td>1.0</td><td>0.8</td><td>0.22363362 0.65809197</td></tr></table>

<table><tr><td>c.</td><td>X -0.5</td><td>f(x)</td></tr><tr><td>-0.25</td><td>-0.0247500</td></tr><tr><td></td><td>0.3349375</td></tr></table>

<table><tr><td>d.</td><td>x</td><td>f(x)</td></tr><tr><td></td><td>0.1</td><td>-0.62049958</td></tr><tr><td></td><td>0.2</td><td>-0.28398668</td></tr><tr><td></td><td>0.3</td><td>0.00660095</td></tr><tr><td></td><td>0.4</td><td>0.24842440</td></tr></table>

4. The data in Exercise 3 were generated using the following functions. Use the cubic splines constructed in Exercise 3 for the given value of $x$ to approximate $f ( x )$ and $f ^ { \prime } ( x )$ , and calculate the actual error.

a. $f ( x ) = x \ln x ;$ approximate $f ( 8 . 4 )$ and $f ^ { \prime } ( 8 . 4 )$ .   
$\mathbf { b } .$ $f ( x ) = \sin ( e ^ { x } - 2 )$ ；approximate $f ( 0 . 9 )$ and $f ^ { \prime } ( 0 . 9 )$   
c. $f ( x ) = x ^ { 3 } + 4 . 0 0 1 x ^ { 2 } + 4 . 0 0 2 x + 1 . 1 0 1$ ；approximate $f ( - { \frac { 1 } { 3 } } )$ and $f ^ { \prime } ( - \frac { 1 } { 3 } )$ d. $f ( x ) = x \cos x - 2 x ^ { 2 } + 3 x - 1$ ；approximate $f ( 0 . 2 5 )$ and $f ^ { \prime } ( 0 . 2 5 )$

5.Construct the clamped cubic spline using the data of Exercise 3 and the fact that a. $f ^ { \prime } ( 8 . 3 ) = 1 . 1 1 6 2 5 6$ and $f ^ { \prime } ( 8 . 6 ) = 1 . 1 5 1 7 6 2$ b. $f ^ { \prime } ( 0 . 8 ) = 2 . 1 6 9 1 7 5 3$ and $f ^ { \prime } ( 1 . 0 ) = 2 . 0 4 6 6 9 6 5$ c. $f ^ { \prime } ( - 0 . 5 ) = 0 . 7 5 1 0 0 0 0$ and $f ^ { \prime } ( 0 ) = 4 . 0 0 2 0 0 0 0$ d. $f ^ { \prime } ( 0 . 1 ) = 3 . 5 8 5 0 2 0 8 2$ and $f ^ { \prime } ( 0 . 4 ) = 2 . 1 6 5 2 9 3 6 6$

6.Repeat Exercise 4 using the cubic splines constructed in Exercise 5.

7.A natural cubic spline $s$ on [0, 2] is defined by

$$
S ( x ) = \left\{ \begin{array} { l l } { S _ { 0 } ( x ) = 1 + 2 x - x ^ { 3 } , } & { \mathrm { i f ~ } 0 \leq x < 1 , } \\ { S _ { 1 } ( x ) = 2 + b ( x - 1 ) + c ( x - 1 ) ^ { 2 } + d ( x - 1 ) ^ { 3 } , } & { \mathrm { i f ~ } 1 \leq x \leq 2 . } \end{array} \right.
$$

Find $b , c ,$ and $d$

8.A clamped cubic spline $\pmb { \mathscr { s } }$ for a function $f$ is defined on [1,3] by

$$
s ( x ) = { \left\{ \begin{array} { l l } { s _ { 0 } ( x ) = 3 ( x - 1 ) + 2 ( x - 1 ) ^ { 2 } - ( x - 1 ) ^ { 3 } , } & { { \mathrm { i f ~ } } 1 \leq x < 2 , } \\ { s _ { 1 } ( x ) = a + b ( x - 2 ) + c ( x - 2 ) ^ { 2 } + d ( x - 2 ) ^ { 3 } , } & { { \mathrm { i f ~ } } 2 \leq x \leq 3 . } \end{array} \right. }
$$

Given $f ^ { \prime } ( 1 ) = f ^ { \prime } ( 3 )$ , find $a , b , c ,$ and $d$

9.A natural cubic spline $s$ is defined by

$$
S ( x ) = \left\{ \begin{array} { l l } { S _ { 0 } ( x ) = 1 + B ( x - 1 ) - D ( x - 1 ) ^ { 3 } , } & { \mathrm { i f ~ } 1 \leq x < 2 , } \\ { S _ { 1 } ( x ) = 1 + b ( x - 2 ) - \frac 3 4 ( x - 2 ) ^ { 2 } + d ( x - 2 ) ^ { 3 } , } & { \mathrm { i f ~ } 2 \leq x \leq 3 . } \end{array} \right.
$$

If $s$ interpolates the data (1,1), (2,1),and $( 3 , 0 )$ ,find $B , D , b$ ,and $d$

10．A clamped cubic spline $\pmb { \mathscr { s } }$ for a function $f$ is defined by

$$
s ( x ) = { \left\{ \begin{array} { l l } { s _ { 0 } ( x ) = 1 + B x + 2 x ^ { 2 } - 2 x ^ { 3 } , } & { { \mathrm { i f ~ } } 0 \leq x < 1 , } \\ { s _ { 1 } ( x ) = 1 + b ( x - 1 ) - 4 ( x - 1 ) ^ { 2 } + 7 ( x - 1 ) ^ { 3 } , } & { { \mathrm { i f ~ } } 1 \leq x \leq 2 . } \end{array} \right. }
$$

Find $f ^ { \prime } ( 0 )$ and $f ^ { \prime } ( 2 )$

11. Construct a free cubic spline to approximate $f ( x ) = \cos \pi x$ by using the values given by $f ( x )$ at $x = 0$ ,0.25,0.5, 0.75,and 1.0. Integrate the spline over [0,1],and compare the result to $\begin{array} { r } { \int _ { 0 } ^ { 1 } \cos \pi x \ d x \ = 0 } \end{array}$ Use the derivatives of the spline to approximate $f ^ { \prime } ( 0 . 5 )$ and $f ^ { \prime \prime } ( 0 . 5 )$ Compare these approximations to the actual values.

12.Construct a free cubic spline to appoximate $f ( x ) = e ^ { - x }$ by using the values given by $f ( x )$ at $x ~ \bumpeq 0$ ,0.25,0.75,and1.0. Integrate the spline over [O,1],and compare theresult to $\begin{array} { r } { \int _ { 0 } ^ { 1 } e ^ { - x } ~ d x = 1 - 1 / e } \end{array}$ . Use the derivatives of the spline to approximate $f ^ { \prime } ( 0 . 5 )$ and $f ^ { \prime \prime } ( 0 . 5 )$ Compare the approximations to the actual values.

13.Repeat Exercise 11, constructing instead the clamped cubic spline with $f ^ { \prime } ( 0 ) = f ^ { \prime } ( 1 ) = 0$

14.Repeat Exercise 12, constructing instead the clamped cubic spline with $f ^ { \prime } ( 0 ) = - 1$ ， $f ^ { \prime } ( 1 ) =$ $- e ^ { - 1 }$

15. Suppose that $f ( x )$ is a polynomial of degree 3. Show that $f ( x )$ is its own clamped cubic spline,but that it cannot be its own free cubic spline.

16.Suppose the data $\{ x _ { i } , f ( x _ { i } ) \} _ { i = 1 } ^ { n }$ lie on a straight line.What can be said about the free and clamped cubic splines for the function $f 2$ [Hint: Take a cue from the results of Exercises 1 and 2.]

17. Given the partition $x _ { 0 } = 0$ ， ${ \boldsymbol { x } } _ { 1 } ~ = ~ 0 . 0 5$ ， and $x _ { 2 } = 0 . 1$ of [0,0.1], find the piecewise linear interpolating function $F$ for $f ( x ) \ = \ e ^ { 2 x }$ . Approximate $\int _ { 0 } ^ { 0 . 1 } e ^ { 2 x } \ d x$ with $\begin{array} { r } { \int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x } \end{array}$ and compare the results to the actual value.

18.Let $f \in C ^ { 2 } [ a , b ]$ , and let the nodes $a = x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } = b$ be given. Derive an error estimate similar to that in Theorem 3.13 for the piecewise linear interpolating function $F$ . Use this estimate to derive error bounds for Exercise 17.

19.Extend Algorithms 3.4 and 3.5 to include as output the first and second derivatives of the spline at the nodes.

20.Extend Algorithms 3.4 and 3.5 to include as output the integral of the spline over the interval $[ x _ { 0 } , x _ { n } ]$

21．Given the partition $x _ { 0 } = 0 , x _ { 1 } = 0 . 0 5 , x _ { 2 } = 0 . 1$ of [0, 0.1] and $f ( x ) = e ^ { 2 x }$ ：

a. Find the cubic spline $\pmb { S }$ with clamped boundary conditions that interpolates $f$ $\mathbf { b } .$ Find an approximation for $\int _ { 0 } ^ { 0 . 1 } e ^ { 2 x } d x$ by evaluating $\textstyle { \int _ { 0 } ^ { 0 . 1 } s ( x ) d x }$ c. Use Theorem 3.13 to estimate $\mathrm { m a x } _ { 0 \leq x \leq 0 . 1 } | f ( x ) - s ( x ) |$ and

$$
\left| \int _ { 0 } ^ { 0 . 1 } f ( x ) d x - \int _ { 0 } ^ { 0 . 1 } s ( x ) d x \right| .
$$

d. Determine the cubic spline $s$ with free boundary conditions, and compare $S ( 0 . 0 2 )$ $s ( \mathbf { 0 . 0 2 } )$ , and $e ^ { 0 . 0 4 } = 1 . 0 4 0 8 1 0 7 7$

22.Let $f$ be defined on $\left[ a , b \right]$ , and let the nodes $a = x _ { 0 } < x _ { 1 } < x _ { 2 } = b$ be given. A quadratic spline interpolating function $s$ consists of the quadratic polynomial

$$
S _ { 0 } ( x ) = a _ { 0 } + b _ { 0 } ( x - x _ { 0 } ) + c _ { 0 } ( x - x _ { 0 } ) ^ { 2 } \quad \mathrm { ~ o n ~ } [ x _ { 0 } , x _ { \mathrm { ~ I ~ } } ]
$$

and the quadratic polynomial

$$
S _ { 1 } ( x ) = a _ { 1 } + b _ { 1 } ( x - x _ { 1 } ) + c _ { 1 } ( x - x _ { 1 } ) ^ { 2 } \quad \mathrm { o n } [ x _ { 1 } , x _ { 2 } ] ,
$$

such that

i $S ( x _ { 0 } ) = f ( x _ { 0 } ) , S ( x _ { 1 } ) = f ( x _ { 1 } ) , { \mathrm { a n d ~ } } S ( x _ { 2 } ) = f ( x _ { 2 } ) ,$ i. $S \in C ^ { 1 } [ x _ { 0 } , x _ { 2 } ]$

Show that conditions (i) and (ii) lead to five equations in the six unknowns $a _ { 0 } , b _ { 0 } , c _ { 0 } , a _ { 1 } , b _ { 1 }$ and $c _ { 1 }$ . The problem is to decide what additional condition to impose to make the solution unique. Does the condition $S \in C ^ { 2 } [ x _ { 0 } , x _ { 2 } ]$ lead to a meaningful solution?

23.Determine a quadratic spline $\pmb { \mathscr { s } }$ that interpolates the data $f ( 0 ) = 0$ ， $f ( 1 ) \simeq 1$ ， $f ( 2 ) = 2$ and satisfies ${ \pmb s } ^ { \prime } ( \mathbf { 0 } ) = 2$

24.a.The introduction to this chapter included atable listing the population of the United States from 1940 to 1990. Use free cubic spline interpolation to approximate the population in the years 1930,1965,and 2010. b. The population in 1930 was approximately 123,203,000. How accurate do you think your 1965 and 2010 figures are?

25.A car traveling along a straight road is clocked at a number of points.The data from the observations are given in the following table,where the time is in seconds, the distance is in feet, and the speed is in feet per second.

<table><tr><td rowspan=2 colspan=1>Time</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>Distance</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>383</td><td rowspan=1 colspan=1>623</td><td rowspan=1 colspan=1>993</td></tr><tr><td rowspan=1 colspan=1>Speed</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>74</td><td rowspan=1 colspan=1>72</td></tr></table>

a. Use a clamped cubic spline to predict the position of the car and its speed when $t \simeq 1 0 ~ \mathrm { s }$ b. Use the derivative of the spline to determine whether the car ever exceeds a 55-mi/h speed limit on the road; if so,what is the first time the car exceeds this speed? c. What is the predicted maximum speed for the car?

26.The 1995 Kentucky Derby was won by a horse named Thunder Gulch in a time of $2 { : } 0 1 \ \frac { 1 } { 5 }$ min and ${ \scriptstyle { \frac { 1 } { 5 } } } \ s )$ for the $1 \frac { 1 } { 4 }$ -mirceiaeld $\dot { 2 } 2 \frac { 2 } { 5 }$ $4 5 \frac { 4 } { 5 }$ ,and $1 : 3 5 \frac { 3 } { 5 }$

a. Use these values together with the starting time to construct a free cubic spline for Thunder Gulch's race.   
b. Use the spline to predict the time at the three-quarter-mile pole,and compare this to the actual time of $1 { : } 1 0 \frac { 1 } { 5 }$   
c. Use the spline to approximate Thunder Gulch's starting speed and speed at the finish line.   
27.It is suspected that the high amounts of tannin in mature oak leaves inhibit the growth of the winter moth (Operophtera bromata $L$ , Geometridae) larvae that extensively damage these trees in certain years. The following table lists the average weight of two samples of larvae at   
+ times in the first 28 days after birth. The first sample was reared on young oak leaves. whereas the second sample was reared on mature leaves from the same tree.

a.Use a free cubic spline to approximate the average weight curve for each sample.

b. Find an approximate maximum average weight for each sample by determining the maximum of the spline.

<table><tr><td rowspan=1 colspan=1>Day</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>28</td></tr><tr><td rowspan=1 colspan=1>Sample l average weight (mg)</td><td rowspan=1 colspan=1>6.67</td><td rowspan=1 colspan=1>17.33</td><td rowspan=1 colspan=1>42.67</td><td rowspan=1 colspan=1>37.33</td><td rowspan=1 colspan=1>30.10</td><td rowspan=1 colspan=1>29.31</td><td rowspan=1 colspan=1>28.74</td></tr><tr><td rowspan=1 colspan=1>Sample 2 average weight (mg)</td><td rowspan=1 colspan=1>6.67</td><td rowspan=1 colspan=1>16.11</td><td rowspan=1 colspan=1>18.89</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>10.56</td><td rowspan=1 colspan=1>9.44</td><td rowspan=1 colspan=1>8.89</td></tr></table>

28.The upper portion of this noble beast is to be approximated using clamped cubic spline interpolants. The curve is drawn on a grid from which the table is constructed. Use Algorithm 3.5 to construct the three clamped cubic splines.

![](images/c50e192e7810d18fd82a96acf54121dd2ce2555ce639fa7e0c2166d77ae8341d.jpg)

Curve 1   
Curve 2   
Curve 3   

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>f&#x27;(xi)</td><td>i</td><td>Xi</td><td>f(x）</td><td>f&#x27;(xi)</td><td>i</td><td>X</td><td>f(xi）</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>1.0</td><td>0</td><td>17</td><td>4.5</td><td>3.0</td><td>0</td><td>27.7</td><td>4.1</td><td>0.33</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td></td><td>1</td><td>20</td><td>7.0</td><td></td><td>1</td><td>28</td><td>4.3</td><td></td></tr><tr><td>2</td><td>5</td><td>3.9</td><td></td><td>2</td><td>23</td><td>6.1</td><td></td><td>2</td><td>29</td><td>4.1</td><td></td></tr><tr><td>3</td><td>6</td><td>4.2</td><td></td><td>3</td><td>24</td><td>5.6</td><td></td><td>3</td><td>30</td><td>3.0</td><td>-1.5</td></tr><tr><td>4</td><td>7</td><td>5.7</td><td></td><td>4</td><td>25</td><td>5.8</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>8</td><td>6.6</td><td></td><td>5</td><td>27</td><td>5.2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>10</td><td>7.1</td><td></td><td>6</td><td>27.7</td><td>4.1</td><td>14.0</td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>13</td><td>6.7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>17</td><td>4.5</td><td>-0.67</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

29.Repeat Exercise 28, constructing three natural splines using Algorithm 3.4.

# 3.5 Parametric Curves

None of the techniques developed in this chapter can be used to generate curves of the form shown in Figure 3.13 since this curve cannot be expressed as a function of one coordinate variable in terms of the other. In this section we will see how to represent general curves by using a parameter to express both the $x -$ and $y$ -coordinate variables. This technique can be extended to represent general curves and surfaces in space.

![](images/a9c14f44516214b4b8039e13d2f37d74999cd53e4336c682671bc79ea664de4b.jpg)  
Figure 3.13

A straightforward parametric technique for determining a polynomial or piecewise polynomial to connect the points $( x _ { 0 } , y _ { 0 } ) , ( x _ { 1 } , y _ { 1 } ) , \dots , ( x _ { n } , y _ { n } )$ in the order given is to use a parameter $t$ on an interval $[ t _ { 0 } , t _ { n } ]$ ，with $t _ { 0 } < t _ { 1 } < \cdots < t _ { n }$ , and construct approximation functions with

$$
x _ { i } = x ( t _ { i } ) \quad { \mathrm { a n d } } \quad y _ { i } = y ( t _ { i } ) , \quad { \mathrm { f o r e a c h } } i = 0 , 1 , \dots , n .
$$

The following example demonstrates the technique in the case where both approximating functions are Lagrange interpolating polynomials.

# EXAMPLE 1

Construct a pair of Lagrange polynomials to approximate the curve shown in Figure 3.13.   
using the data points shown on the curve.

There is fexibilityin choosing the parameter,and we willchoose the points{t equally spaced in [O,1], which gives the data in Table 3.17.

Table 3.17   

<table><tr><td>i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>ti</td><td>0</td><td>0.25</td><td>0.5</td><td>0.75</td><td>1</td></tr><tr><td>Xi</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>yi</td><td>0</td><td>1</td><td>0.5</td><td>0</td><td>-1</td></tr></table>

This produces the interpolating polynomials

$$
x ( t ) = \left( \left( \left( 6 4 t - { \frac { 3 5 2 } { 3 } } \right) t + 6 0 \right) t - { \frac { 1 4 } { 3 } } \right) t - 1
$$

and

$$
y ( t ) = \left( \left( \left( - \frac { 6 4 } { 3 } t + 4 8 \right) t - \frac { 1 1 6 } { 3 } \right) t + 1 1 \right) t .
$$

Ploting this parametric system produces the graph shown in blue in Figure 3.14. Although it passes through the required points and has the same basic shape,it is quite a crude approximation to the original curve. A more accurate approximation would require additional nodes,with the accompanying increase in computation. □

![](images/18a3ebb2ae4a66f107b42e93510bb490f8c4deafce2f19fb4371df23cea62479.jpg)  
Figure 3.14

Hermite and spline curves can be generated in a similar manner, but these also require extensive computational effort.

Applications in computer graphics require the rapid generation of smooth curves that can be easily and quickly modified.For both aesthetic and computational reasons,changing one portion of these curves should have litle or no effect on other portions of the curves. This eliminates the use of interpolating polynomials and splines since changing one portion of these curves affects the whole curve.

The choice of curve for use in computer graphics is generally a form of the piecewise cubic Hermite polynomial. Each portion of a cubic Hermite polynomial is completely determined by specifying its endpoints and the derivatives at these endpoints.As a consequence, one portion of the curve can be changed while leaving most of the curve the same. Only the adjacent portions need to be modified to ensure smoothness at the endpoints. The computations can be performed quickly, and the curve can be modified a section at a time.

The problem with Hermite interpolation is the need to specify the derivatives at the endpoints of each section of the curve. Suppose the curve has $n + 1$ data points $( x ( t _ { 0 } ) , y ( t _ { 0 } ) )$ $( x ( t _ { n } ) , y ( t _ { n } ) )$ , and we wish to parameterize the cubic to allow complex features. Then we must specify $x ^ { \prime } ( t _ { i } )$ and $y ^ { \prime } ( t _ { i } )$ , for each $i = 0 , 1 , \ldots , n$ .This is not as dificult as it would first appear, since each portion is generated independently. We must ensure only that the derivatives at the endpoints of each portion match those in the adjacent portion. Essentially, then, we can simplify the process to one of determining a pair of cubic Hermite polynomials in the parameter $t$ ，where $t _ { 0 } = 0$ and $t _ { 1 } = 1$ ， given the endpoint data $( x ( 0 ) , y ( 0 ) )$ and $( x ( 1 ) , y ( 1 ) )$ and the derivatives $d y / d x$ (at $t = 0$ and $d y / d x$ (at $t = 1 )$ .

Notice, however, that we are specifying only six conditions,and the cubic polynomials in $x ( t )$ and $y ( t )$ each have four parameters, for a total of eight. This provides flexibility in choosing the pair of cubic Hermite polynomials to satisfy the conditions, because the natural form for determining $x ( t )$ and $y ( t )$ requires that we specify $x ^ { \prime } ( 0 ) , x ^ { \prime } ( 1 ) , y ^ { \prime } ( 0 )$ ,and $y ^ { \prime } ( 1 )$ . The explicit Hermite curve in $x$ and $y$ requires specifying only the quotients

$$
{ \frac { d y } { d x } } ( t = 0 ) = { \frac { y ^ { \prime } ( 0 ) } { x ^ { \prime } ( 0 ) } } \quad { \mathrm { a n d } } \quad { \frac { d y } { d x } } ( t = 1 ) = { \frac { y ^ { \prime } ( 1 ) } { x ^ { \prime } ( 1 ) } } .
$$

By multiplying $x ^ { \prime } ( 0 )$ and $y ^ { \prime } ( 0 )$ by a common scaling factor, the tangent line to the curve at $( x ( 0 ) , y ( 0 ) )$ remains the same, but the shape of the curve varies. The larger the scaling factor, the closer the curve comes to approximating the tangent line near $( x ( 0 ) , y ( 0 ) )$ .A similar situation exists at the other endpoint $( x ( 1 ) , y ( 1 ) )$

To further simplify the process in interactive computer graphics, the derivative at an endpoint is specified by using a second point, called a guidepoint, on the desired tangent line.The farther the guidepoint is from the node,the more closely the curve approximates the tangent line near the node.

In Figure 3.15, the nodes occur at $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ , the guidepoint for $( x _ { 0 } , y _ { 0 } )$ is $( x _ { 0 } + \alpha _ { 0 } , y _ { 0 } + \beta _ { 0 } )$ , and the guidepoint for $( x _ { 1 } , y _ { 1 } )$ is $( x _ { 1 } - \alpha _ { 1 } , y _ { 1 } - \beta _ { 1 } )$ . The cubic Hermite polynomial $x ( t )$ on [0,1] satisfies

$$
x ( 0 ) = x _ { 0 } , \quad x ( 1 ) = x _ { 1 } , \quad x ^ { \prime } ( 0 ) = \alpha _ { 0 } , \quad \mathrm { a n d } \quad x ^ { \prime } ( 1 ) = \alpha _ { 1 } .
$$

![](images/d26c2d50950558cc76f39766e898198ef330d4a7842b6ecf72149e4a2980d99a.jpg)  
Figure 3.15

The unique cubic polynomial satisfying these conditions is

$$
x ( t ) = [ 2 ( x _ { 0 } - x _ { 1 } ) + ( \alpha _ { 0 } + \alpha _ { 1 } ) ] t ^ { 3 } + [ 3 ( x _ { 1 } - x _ { 0 } ) - ( \alpha _ { 1 } + 2 \alpha _ { 0 } ) ] t ^ { 2 } + \alpha _ { 0 } t + x _ { 0 } .
$$

In a similar manner, the unique cubic polynomial satisfying

$$
y ( 0 ) = y _ { 0 } , \quad y ( 1 ) = y _ { 1 } , \quad y ^ { \prime } ( 0 ) = \beta _ { 0 } , \quad \mathrm { a n d } \quad y ^ { \prime } ( 1 ) = \beta _ { 1 }
$$

is

$$
y ( t ) = [ 2 ( y _ { 0 } - y _ { 1 } ) + ( \beta _ { 0 } + \beta _ { 1 } ) ] t ^ { 3 } + [ 3 ( y _ { 1 } - y _ { 0 } ) - ( \beta _ { 1 } + 2 \beta _ { 0 } ) ] t ^ { 2 } + \beta _ { 0 } t + y _ { 0 } .
$$

![](images/467e96041a9b26fa3cb366a41e10f6d44ff22af9bc432d685945a8937987ab40.jpg)  
Figure 3.16

The graphs in Figure 3.16 show some possibilities of the curves produced by Eqs. (3.22) and (3.23) when the nodes are (O, O) and (1,O) and the slopes at these nodes are 1 and -1, respectively. The specification of the slope at the endpoints requires only that $\alpha _ { 0 } = \beta _ { 0 }$ and $\alpha _ { 1 } = - \beta _ { 1 }$ , since the ratios $\alpha _ { 0 } / \beta _ { 0 }$ and $\alpha _ { 1 } / \beta _ { 1 }$ give the slopes at the left and right endpoints, respectively. ■

The standard procedure for determining curves in an interactive graphics mode is to first use a mouse or trackballto set the nodes and guidepoints to generate a first approximation to the curve. These can be set manually, but most graphics systems permit you to use your input device to draw the curve on the screen freehand and will select appropriate nodes and guidepoints for your freehand curve.

The nodes and guidepoints can then be manipulated into a position that produces an aesthetically pleasing curve. Since the computation is minimal, the curve can be determined so quickly that the resulting change is seen immediately. Moreover, all the data needed to compute the curves are imbedded in the coordinates of the nodes and guidepoints,so no analytical knowledge is required of the user of the system.

Popular graphics programs use this type of system for their freehand graphic representations in a slightly modified form. The Hermite cubics are described as Bézier polynomials,which incorporate a scaling factor of 3 when computing the derivatives at the endpoints. This modifies the parametric equations to

$$
x ( t ) = [ 2 ( x _ { 0 } - x _ { 1 } ) + 3 ( \alpha _ { 0 } + \alpha _ { 1 } ) ] t ^ { 3 } + [ 3 ( x _ { 1 } - x _ { 0 } ) - 3 ( \alpha _ { 1 } + 2 \alpha _ { 0 } ) ] t ^ { 2 } + 3 \alpha _ { 0 } t + x _ { 0 } ,
$$

and

$$
y ( t ) = [ 2 ( y _ { 0 } - y _ { 1 } ) + 3 ( \beta _ { 0 } + \beta _ { 1 } ) ] t ^ { 3 } + [ 3 ( y _ { 1 } - y _ { 0 } ) - 3 ( \beta _ { 1 } + 2 \beta _ { 0 } ) t ^ { 2 } + 3 \beta _ { 0 } t + y _ { 0 } ,
$$

for $0 \leq t \leq 1$ ,but this change is transparent to the user of the system.

Algorithm 3.6 constructs a set of Bezier curves based on the parametric equations in (3.24) and (3.25).

# Bézier Curve

To construct the cubic Bezier curves ${ \cal C } _ { 0 } , \ldots , { \cal C } _ { n - 1 }$ in parametric form, where $C _ { i }$ is represented by

$$
( x _ { i } ( t ) , y _ { i } ( t ) ) = ( a _ { 0 } ^ { ( i ) } + a _ { 1 } ^ { ( i ) } t + a _ { 2 } ^ { ( i ) } t ^ { 2 } + a _ { 3 } ^ { ( i ) } t ^ { 3 } , b _ { 0 } ^ { ( i ) } + b _ { 1 } ^ { ( i ) } t + b _ { 2 } ^ { ( i ) } t ^ { 2 } + b _ { 3 } ^ { ( i ) } t ^ { 3 } ) ,
$$

for $0 \leq t \leq 1$ , as determined by the left endpoint $( x _ { i } , y _ { i } )$ , left guidepoint $( x _ { i } ^ { + } , y _ { i } ^ { + } )$ ,right endpoint $( x _ { i + 1 } , y _ { i + 1 } )$ , and right guidepoint $( x _ { i + 1 } ^ { - } , y _ { i + 1 } ^ { - } )$ for each $i = 0 , 1 , \ldots , n - 1$

$$
n ; { \bigl ( } x _ { 0 } , y _ { 0 } { \bigr ) } , \ldots , { \bigl ( } x _ { n } , y _ { n } { \bigr ) } ; { \bigl ( } x _ { 0 } ^ { + } , y _ { 0 } ^ { + } { \bigr ) } , \ldots , { \bigl ( } x _ { n - 1 } ^ { + } , y _ { n - 1 } ^ { + } { \bigr ) } ; { \bigl ( } x _ { 1 } ^ { - } , y _ { 1 } ^ { - } { \bigr ) } , \ldots , { \bigl ( } x _ { n } ^ { - } , y _ { n } ^ { - } { \bigr ) } .
$$

OUTPUT coeffcients $\{ a _ { 0 } ^ { ( i ) } , a _ { 1 } ^ { ( i ) } , a _ { 2 } ^ { ( i ) } , a _ { 3 } ^ { ( i ) } , b _ { 0 } ^ { ( i ) } , b _ { 1 } ^ { ( i ) } , b _ { 2 } ^ { ( i ) } , b _ { 3 } ^ { ( i ) } , \mathrm { f o r } 0 \le i \le n - 1 \} .$

Step 1 For each $i = 0 , 1 , \ldots , n - 1$ do Steps 2 and 3.

$$
\begin{array} { r l } & { b _ { 0 } ^ { ( i ) } = y _ { i } ; } \\ & { a _ { 1 } ^ { ( i ) } = 3 ( x _ { i } ^ { + } - x _ { i } ) ; } \\ & { b _ { 1 } ^ { ( i ) } = 3 ( y _ { i } ^ { + } - y _ { i } ) ; } \\ & { a _ { 2 } ^ { ( i ) } = 3 ( x _ { i } + x _ { i + 1 } ^ { - } - 2 x _ { i } ^ { + } ) ; } \\ & { b _ { 2 } ^ { ( i ) } = 3 ( y _ { i } + y _ { i + 1 } ^ { - } - 2 y _ { i } ^ { + } ) ; } \\ & { a _ { 3 } ^ { ( i ) } = x _ { i + 1 } - x _ { i } + 3 x _ { i } ^ { + } - 3 x _ { i + 1 } ^ { - } ; } \\ & { b _ { 3 } ^ { ( i ) } = y _ { i + 1 } - y _ { i } + 3 y _ { i } ^ { + } - 3 y _ { i + 1 } ^ { - } ; } \end{array}
$$

Step 3 OUTPUT $( a _ { 0 } ^ { ( i ) } , a _ { 1 } ^ { ( i ) } , a _ { 2 } ^ { ( i ) } , a _ { 3 } ^ { ( i ) } , b _ { 0 } ^ { ( i ) } , b _ { 1 } ^ { ( i ) } , b _ { 2 } ^ { ( i ) } , b _ { 3 } ^ { ( i ) } ) .$ Step 4 STOP.

Three-dimensional curves are generated in a similar manner by additionally specifying third components $z _ { 0 }$ and $z _ { 1 }$ for the nodes and $z _ { 0 } + \gamma _ { 0 }$ and $z _ { 1 } \sim \gamma _ { 1 }$ for the guidepoints. The more difficult problem involving the representation of three-dimensional curves concerns the loss of the third dimension when the curve is projected onto a two-dimensional computer screen. Various projection techniques are used,but this topic lies within the realm of computer graphics. For an introduction to this topic and ways that the technique can be modified for surface representations,see one of the many books on computer graphics methods, such as [Hill,F].

# EXERCISE SET 3.5

1.Let $( x _ { 0 } , y _ { 0 } ) = ( 0 , 0 )$ and $( x _ { 1 } , y _ { 1 } ) = ( 5 , 2 )$ be the endpoints of a curve.Use the given guidepoints to construct parametric cubic Hermite approximations $( x ( t ) , y ( t ) )$ to the curve,and graph the approximations.

a.(1,1) and (6,1) b.(0.5,0.5) and (5.5,1.5) c.(1,1) and (6,3) d. (2,2) and (7,0)

2.Repeat Exercise 1 using cubic Bézier polynomials.

3.Construct and graph the cubic Bézier polynomials given the following points and guidepoints.

a. Point (1,1) with guidepoint (1.5,1.25) to point (6,2) with guidepoint (7,3)   
$\mathbf { b } .$ Point (1,1) with guidepoint (1.25,1.5) to point (6,2) with guidepoint (5,3)   
c. Point (O,O) with guidepoint (0.5,0.5） to point (4,6) with entering guidepoint (3.5,7) and exiting guidepoint (4.5,5) to point (6,1） with guidepoint (7,2)   
d. Point $( 0 , 0 )$ with guidepoint (0.5,0.5) to point (2,1） with entering guidepoint (3,1) and exiting guidepoint (3,1）) to point (4, O) with entering guidepoint (5,1) and exiting guidepoint $( 3 , - 1 )$ to point $( 6 , - 1 )$ with guidepoint (6.5,-0.25)

4.Use the data in the following table and Algorithm 3.6 to approximate the shape of the letter $\varkappa$

$$
 \begin{array} { l } { { \frac { i } { 0 } } \qquad x _ { i } \quad | \begin{array} { l } { { y _ { i } } } \end{array} | \begin{array} { l } { \alpha _ { i } \quad | \begin{array} { l } { { \boldsymbol { \beta _ { i } } } } \end{array} | \begin{array} { l } { \alpha _ { i } ^ { \prime } \quad | \begin{array} { l } { { \boldsymbol { \beta _ { i } ^ { \prime } } } } \end{array} | \begin{array} { l } { \beta _ { i } ^ { \prime } } \end{array} } } \\ { { \begin{array} { l } { { 3 } } \\ { { 2 } } \end{array} } | \begin{array} { l } { { 6 } } \end{array} | \begin{array} { l } { { 3 . 3 } } \\ { { 2 . 8 } } \end{array} | \begin{array} { l } { { 3 . 0 } } \\ { { 5 . 0 } } \end{array} | \begin{array} { l } { { 2 . 5 } } \\ { { 5 . 0 } } \end{array} } } \\ { {  { 3 } } \\ { { 4 } \quad | \begin{array} { l } { { 5 } } \end{array} | \begin{array} { l } { { 2 } } \\ { { 3 } } \end{array} | \begin{array} { l } { { 5 . 8 } } \\ { { 5 . 5 } } \end{array} | \begin{array} { l } { { 2 . 2 } } \\ { { 2 . 2 } } \end{array} | \begin{array} { l } { { 4 . 5 } } \\ { { 6 . 4 } } \end{array} | \begin{array} { l } { { 2 . 5 } } \end{array} } \end{array} } \end{array} \end{array}
$$

5. Suppose a cubic Bézier polynomial is placed through $( u _ { 0 } , v _ { 0 } )$ and $( u _ { 3 } , v _ { 3 } )$ with guidepoints $( u _ { 1 } , v _ { 1 } )$ and $( u _ { 2 } , v _ { 2 } )$ ,respectively.

a. Derive the parametric equations for $u ( t )$ and $v ( t )$ assuming that

$$
\begin{array} { r } { u ( 0 ) = u _ { 0 } , \quad u ( 1 ) = u _ { 3 } , \quad u ^ { \prime } ( 0 ) = u _ { 1 } - u _ { 0 } , \quad u ^ { \prime } ( 1 ) = u _ { 3 } - u _ { 2 } } \end{array}
$$

and

$$
\begin{array} { r } { v ( 0 ) = v _ { 0 } , \quad v ( 1 ) = v _ { 3 } , \quad v ^ { \prime } ( 0 ) = v _ { 1 } - v _ { 0 } , \quad v ^ { \prime } ( 1 ) = v _ { 3 } - v _ { 2 } . } \end{array}
$$

b.Let $\begin{array} { r } { f ( \frac { 1 } { 3 } i ) = u _ { i } } \end{array}$ ,for $i = 0 , 1 , 2 , 3$ and $g ( \textstyle { \frac { 1 } { 3 } } i ) = v _ { i }$ ,for $i = 0 , 1 , 2 , 3$ . Show that the Bernstein polynomial of degree 3 in $t$ for $f$ is $u ( t )$ and the Bernstein polynomial of degree three in $t$ for $g$ is $v ( t )$ . (See Exercise 29 of Section 3.1.)

# 3.6 Survey of Methods and Software

In this chapter we have considered approximating a function using polynomials and piecewise polynomials. The function can be specified by a given defining equation or by providing points in the plane through which the graph of the function passes. A set of nodes Xo,x1,.., xn is given in each case,and more information, such as the value of various derivatives, may also be required. We need to find an approximating function that satisfies the conditions specified by these data.

The interpolating polynomial $P ( x )$ is the polynomial of least degree that satisfies, for a function $f$ ，

$$
P ( x _ { i } ) = f ( x _ { i } ) , \quad { \mathrm { f o r e a c h } } i = 0 , 1 , \dots , n .
$$

Although this interpolating polynomial is unique,it can take many different forms.The Lagrange form is most often used for interpolating tables when $\pmb { n }$ is small and for deriving formulas for approximating derivatives and integrals.Neville's method is used for evaluating several interpolating polynomials at the same value of $x$ . Newton's forms of the polynomial are more appropriate for computation and are also used extensively for deriving formulas for solving differential equations.However, polynomial interpolation has the inherent weaknesses of oscillation, particularly if the number of nodes is large. In this case there are other methods that can be better applied.

The Hermite polynomials interpolate a function and its derivative at the nodes. They can be very accurate but require more information about the function being approximated. When there are a large number of nodes,the Hermite polynomials also exhibit oscillation weaknesses.

The most commonly used form of interpolation is piecewise-polynomial interpolation. If function and derivative values are available, piecewise cubic Hermite interpolation is recommended.This is the preferred method for interpolating values of a function that is the solution to a differential equation. When only the function values are available, free cubic spline interpolation can be used. This spline forces the second derivative of the spline to be zero at the endpoints. Other cubic splines require additional data. For example, the clamped cubic spline needs values of the derivative of the function at the endpoints of the interval.

Other methods of interpolation are commonly used. Trigonometric interpolation, in particular the Fast Fourier Transform discussed in Chapter 8,is used with large amounts of data when the function has a periodic nature. Interpolation by rational functions is also used. If the data are suspected to be inaccurate, smoothing techniques can be applied, and some form of least squares fit of data is recommended. Polynomials, trigonometric functions,rational functions,and splines can be used in least squares fitting of data. We consider these topics in Chapter 8.

Interpolation routines included in the IMSL Library are based on the book A Practical Guide to Splines by Carl de Boor [Deb] and use interpolation by cubic splines. The subroutine CSDEC is for interpolation by cubic splines with user-supplied end conditions, CSPER is for interpolation by cubic splines with periodic end conditions,and CSHER is for interpolation by quasi-Hermite piecewise polynomials. The subroutine CSDEC incorporates Algorithms 3.4 and 3.5. The subroutine CSINT uses the not-a-knot condition mentioned at the end of Section 3.4. There are also cubic splines to minimize oscillations and to preserve concavity. Methods for two-dimensional interpolation by bicubic splines are also included.

The NAG library http://www.netlib.org contains the subroutines EO1AEF for polynomial and Hermite interpolation,EO1BAF for cubic spline interpolation,and EO1BEF for piecewise cubic Hermite interpolation. The subroutine EO1ABF is used to interpolate data at equally spaced points. The routine EO1AAF is applied if the data are given at unequally spaced points.NAG also contains subroutines for interpolating functions of two variables.

The netlib library contains the subroutines cubspl.f under the package pppack to compute the cubic spline with various endpoint conditions. Under the package slatec, polint.f produces the Newton's divided difference coefficients for a discrete set of data points and under the package slatec/pchip are various routines for evaluating Hermite piecewise polynomials.

The MATLAB function INTERPl can be used to interpolate a discrete set of data points, using either nearest neighbor interpolation, linear interpolation, cubic spline interpolation,or cubic interpolation. INTERP1 outputs the polynomial evaluated at a discrete set of points.POLYFIT, based on a least squares approximation (see Section 8.1), can be used to find an interpolating function of degree at most $\pmb { n }$ that passes through $n + 1$ specified points. Cubic splines can be produced with the function SPLINE.

Maple is used to construct an interpolating polynomial using the command

>interp(x,Y,x);

where X is the list $[ \mathbf { x } [ 0 ] , \mathbf { x } [ 1 ] , \dots , \mathbf { x } [ \mathbf { n } ] ] ,$ ,Yis the list[f(x[o]),f(x[1]),..,f(x[n])], and $\pmb { \mathrm { x } }$ is the variable to be used.

The natural cubic spline can also be constructed with Maple. First enter >readlib(spline); to make the package available. With ${ \tt X }$ and $\mathtt { Y }$ as in the preceding paragraph the command >spline(x,Y,x,3); constructs the natural cubic spline interpolating X = [x[O],...,x[n]] and Y = [y[0], $\dots , y [ n ] ]$ ,where $\pmb { x }$ is the variable and 3 refers to the degree of the cubic spline. Lineai and quadratic splines can also be created.

General references to the methods in this chapter are the books by Powell $[ \mathbf { P o } ]$ and by Davis [Da]. The seminal paper on splines is due to Schoenberg [Scho]. Important books on splines are by Schultz [Schul], De Boor [Deb],Diercx [Di],and Schumaker [Schum].

CHAPTER

4

# Numerical Differentiation and Integration

Asee aluminum into one whose cross section has the form of a sine wave.

![](images/dc2b3428dd999361304f91198577a69699b0efbd673afa20ed9646b5c455a484.jpg)

A corrugated sheet 4 ft long is needed, the height of each wave is 1 in. from the center line, and each wave has a period of approximately $2 \pi$ in. The problem of finding the length of the initial flat sheet is one of determining the length of the curve given by $f ( x ) = \sin x$ from $x = 0$ in. to $x = 4 8$ in. From calculus we know that this length is

$$
L = \int _ { 0 } ^ { 4 8 } { \sqrt { 1 + \left( f ^ { \prime } ( x ) \right) ^ { 2 } } } d x = \int _ { 0 } ^ { 4 8 } { \sqrt { 1 + \left( \cos x \right) ^ { 2 } } } d x ,
$$

so the problem reduces to evaluating this integral. Although the sine function is one of the most common mathematical functions, the calcu-lation of its length involves an elliptic integral of the second kind, which cannot be evaluated by ordinary methods. Methods are developed in this chapter to approximate the solution to problems of this type. This particular problem is considered in Exercise 21 of Section 4.4 and Exercise 10 of Section 4.5.

We mentioned in the introduction to Chapter 3 that one reason for using algebraic polynomials to approximate an arbitrary set of data is that, given any continuous function defined on a closed interval, there exists a polynomial that is arbitrarily close to the function at every point in the interval. Also, the derivatives and integrals of polynomials are easily obtained and evaluated. It should not be surprising, then, that most procedures for approximating integrals and derivatives use the polynomials that approximate the function.

# 4.1Numerical Differentiation

The derivative of the function $f$ at $x _ { 0 }$ is

$$
f ^ { \prime } ( x _ { 0 } ) = \operatorname* { l i m } _ { h \to 0 } { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } } .
$$

This formula gives an obvious way to generate an approximation to $f ^ { \prime } ( x )$ : simply compute

$$
\frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h }
$$

for small values of $h$ . Although this may be obvious,it is not very successful. due to our old nemesis, roundoff error. But it is certainly the place to start.

To approximate $f ^ { \prime } ( x _ { 0 } )$ , suppose first that $x _ { 0 } \in ( a , b )$ ，where $f \in C ^ { z } [ a , b ]$ and that $x _ { 1 } = x _ { 0 } + h$ for some $h \neq 0$ that is sufficiently small to ensure that $x _ { \{ \in \atop \bigcup \cdot \in \cdot \bigcup \cdot \} }$ We construct the first Lagrange polynomial $P _ { 0 , 1 } ( x )$ for $f$ determined by $x _ { 0 }$ and $. \dot { \iota _ { 1 } }$ .with its error term:

$$
\begin{array} { r l } & { f ( x ) = P _ { 0 , 1 } ( x ) + \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) } { 2 ! } f ^ { \prime \prime } ( \xi ( x ) ) } \\ & { \qquad = \displaystyle \frac { f ( x _ { 0 } ) ( x - x _ { 0 } - h ) } { - h } + \frac { f ( x _ { 0 } + h ) ( x - x _ { 0 } ) } { h } + \frac { ( x - x _ { 0 } ) ( x - x _ { 0 } - h ) } { 2 } f ^ { \prime \prime } ( \xi ( x ) ) } \end{array}
$$

for some $\xi ( x )$ in $[ a , b ]$ . Differentiating gives

$$
\begin{array} { l } { { f ^ { \prime } ( x ) = \displaystyle \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } + D _ { x } \left[ \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 0 } - h ) } { 2 } f ^ { \prime \prime } ( \xi ( x ) ) \right] } } \\ { { \displaystyle ~ = \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } + \displaystyle \frac { 2 ( x - x _ { 0 } ) - h } { 2 } f ^ { \prime \prime } ( \xi ( x ) ) } } \\ { { \displaystyle ~ + \frac { ( x - x _ { 0 } ) ( x - x _ { 0 } - h ) } { 2 } D _ { x } ( f ^ { \prime \prime } ( \xi ( x ) ) ) , } } \end{array}
$$

s0

$$
f ^ { \prime } ( x ) \approx { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } } .
$$

One difficulty with this formula is that we have no information about $D _ { x } f ^ { \prime \prime } ( \xi ( x ) )$ ,so the truncation error cannot be estimated. When $x$ is $x _ { 0 }$ ,however,the coefficient of $D _ { x } f ^ { \prime \prime } ( \xi ( x ) )$ is O,and the formula simplifies to

$$
f ^ { \prime } ( x _ { 0 } ) = { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } } - { \frac { h } { 2 } } f ^ { \prime \prime } ( \xi ) .
$$

For small values of $h$ , the difference quotient $[ f ( x _ { 0 } + h ) - f ( x _ { 0 } ) ] / h$ can be used to approximate $f ^ { \prime } ( x _ { 0 } )$ with an error bounded by $M | h | / 2$ ,where $M$ is a bound on $\mid f ^ { \prime \prime } ( x ) \mid$ for $x \in [ a , b ]$ . This formula is known as the forward-difference formula if $h > 0$ (see Figure 4.1) and the backward-difference formula if $h < 0$

![](images/e71ae92fddda51a25b34c6d901545e3845b7739e43398a2b05687f9712b58920.jpg)  
Figure 4.1

Let $f ( x ) = \ln x$ and $x _ { 0 } = 1 . 8$ . The forward-difference formula

$$
\frac { f ( 1 . 8 + h ) - f ( 1 . 8 ) } { h }
$$

is used to approximate $f ^ { \prime } ( 1 . 8 )$ with error

$$
\frac { | h f ^ { \prime \prime } ( \xi ) | } { 2 } = \frac { | h | } { 2 \xi ^ { 2 } } \le \frac { | h | } { 2 ( 1 . 8 ) ^ { 2 } } , \quad \mathrm { w h e r e } \quad 1 . 8 < \xi < 1 . 8 + h .
$$

The results in Table 4.1 are produced when $h = 0 . 1$ ,0.01, and 0.001.

Table 4.1

<table><tr><td rowspan="2">h</td><td rowspan="2">f(1.8 + h)</td><td>f(1.8+h)- f(1.8)</td><td>h</td></tr><tr><td>h</td><td>2(1.8)2</td></tr><tr><td>0.1</td><td>0.64185389</td><td>0.5406722</td><td>0.0154321</td></tr><tr><td>0.01</td><td>0.59332685</td><td>0.5540180</td><td>0.0015432</td></tr><tr><td>0.001</td><td>0.58834207</td><td>0.5554013</td><td>0.0001543</td></tr></table>

Since $f ^ { \prime } ( x ) = 1 / x$ , the exact value of $f ^ { \prime } ( 1 . 8 )$ is 0.555, and the error bounds are quite close to the true approximation error.

To obtain general derivative approximation formulas, suppose that $\{ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } \}$ are $( n + 1 )$ distinct numbers in some interval $I$ and that $f \in C ^ { n + 1 } ( I )$ . From Theorem 3.3,

$$
f ( x ) = \sum _ { k = 0 } ^ { n } f ( x _ { k } ) L _ { k } ( x ) + { \frac { ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( \xi ( x ) ) ,
$$

for some $\xi ( x )$ in $I$ , where $L _ { k } ( x )$ denotes the $k$ th Lagrange coeficient polynomial for $f$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ . Differentiating this expression gives

$$
\begin{array} { l } { f ^ { \prime } ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } f ( x _ { k } ) L _ { k } ^ { \prime } ( x ) + D _ { x } \left[ \frac { ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( n + 1 ! ) } \right] f ^ { ( n + 1 ) } ( \xi ( x ) ) } \\ { + \displaystyle \frac { ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( n + 1 ) ! } D _ { x } [ f ^ { ( n + 1 ) } ( \xi ( x ) ) ] . } \end{array}
$$

Again, we have a problem estimating the truncation error unless $x$ is one of the numbers $x _ { j }$ . In this case, the term multiplying $D _ { x } \{ f ^ { ( n + 1 ) } ( \xi ( x ) ) \}$ is O,and the formula becomes

$$
f ^ { \prime } ( x _ { j } ) = \sum _ { k = 0 } ^ { n } f ( x _ { k } ) L _ { k } ^ { \prime } ( x _ { j } ) + { \frac { f ^ { ( n + 1 ) } ( \xi ( x _ { j } ) ) } { ( n + 1 ) ! } } \prod _ { k = 0 } ^ { n } ( x _ { j } - x _ { k } ) ,
$$

which is called an $( n + 1 )$ -point formula to approximate $f ^ { \prime } ( x _ { j } )$

In general, using more evaluation points in Eq. (4.2) produces greater accuracy, although the number of functional evaluations and growth of roundoff error discourages this somewhat. The most common formulas are those involving three and five evaluation points.

We first derive some useful three-point formulas and consider aspects of their errors. Since

$$
L _ { 0 } ( x ) = { \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) } } , \quad { \mathrm { w e ~ h a v e } } \quad L _ { 0 } ^ { \prime } ( x ) = { \frac { 2 x - x _ { 1 } - x _ { 2 } } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) } } .
$$

Similarly,

$$
L _ { 1 } ^ { \prime } ( x ) = { \frac { 2 x - x _ { 0 } - x _ { 2 } } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) } } \quad { \mathrm { a n d } } \quad L _ { 2 } ^ { \prime } ( x ) = { \frac { 2 x - x _ { 0 } - x _ { 1 } } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } } .
$$

Hence, from Eq. (4.2),

$$
\begin{array} { c c c } { { f ^ { \prime } ( x _ { j } ) = f ( x _ { 0 } ) \left[ \displaystyle \frac { 2 x _ { j } - x _ { 1 } - x _ { 2 } } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) } \right] + f ( x _ { 1 } ) \left[ \displaystyle \frac { 2 x _ { j } - x _ { 0 } - x _ { 2 } } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) } \right] } } \\ { { + f ( x _ { 2 } ) \left[ \displaystyle \frac { 2 x _ { j } - x _ { 0 } - x _ { 1 } } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } \right] + \displaystyle \frac { 1 } { 6 } f ^ { ( 3 ) } ( \xi _ { j } ) \displaystyle \prod _ { k = 0 } ^ { 2 } ( x _ { j } - x _ { k } ) , } } \end{array}
$$

for each $j = 0 , 1 , 2$ ， where the notation $\xi _ { j }$ indicates that this point depends on $x _ { j }$

The three formulas from Eq. (4.3) become especially useful if the nodes are equally spaced,that is,when

$$
x _ { 1 } = x _ { 0 } + h { \mathrm { a n d } } x _ { 2 } = x _ { 0 } + 2 h , \quad { \mathrm { f o r ~ s o m e ~ } } h \neq 0 .
$$

We will assume equally spaced nodes throughout the remainder of this section.

Using Eq. (4.3) with $x _ { j } = x _ { 0 } , x _ { 1 } = x _ { 0 } + h$ ,and $x _ { 2 } = x _ { 0 } + 2 h$ gives

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { h } \left[ - \frac { 3 } { 2 } f ( x _ { 0 } ) + 2 f ( x _ { 1 } ) - \frac { 1 } { 2 } f ( x _ { 2 } ) \right] + \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 0 } ) .
$$

Doing the same for $x _ { j } = x _ { 1 }$ gives

$$
f ^ { \prime } ( x _ { 1 } ) = \frac { 1 } { h } \left[ - \frac { 1 } { 2 } f ( x _ { 0 } ) + \frac { 1 } { 2 } f ( x _ { 2 } ) \right] - \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) ,
$$

and for $x _ { j } = x _ { 2 }$ ，

$$
f ^ { \prime } ( x _ { 2 } ) = \frac { 1 } { h } \left[ \frac { 1 } { 2 } f ( x _ { 0 } ) - 2 f ( x _ { 1 } ) + \frac { 3 } { 2 } f ( x _ { 2 } ) \right] + \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 2 } ) .
$$

Since $x _ { 1 } = x _ { 0 } + h$ and $x _ { 2 } = x _ { 0 } + 2 h$ ,these formulas can also be expressed as

$$
\begin{array} { c } { { f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 1 } { h } \left[ - \frac { 3 } { 2 } f ( x _ { 0 } ) + 2 f ( x _ { 0 } + h ) - \displaystyle \frac { 1 } { 2 } f ( x _ { 0 } + 2 h ) \right] + \displaystyle \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 0 } ) , } } \\ { { f ^ { \prime } ( x _ { 0 } + h ) = \displaystyle \frac { 1 } { h } \left[ - \displaystyle \frac { 1 } { 2 } f ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } f ( x _ { 0 } + 2 h ) \right] - \displaystyle \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) , \quad \mathrm { a n d } } } \\ { { f ^ { \prime } ( x _ { 0 } + 2 h ) = \displaystyle \frac { 1 } { h } \left[ \displaystyle \frac { 1 } { 2 } f ( x _ { 0 } ) - 2 f ( x _ { 0 } + h ) + \displaystyle \frac { 3 } { 2 } f ( x _ { 0 } + 2 h ) \right] + \displaystyle \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 2 } ) . } } \end{array}
$$

As a matter of convenience,the variable substitution $x _ { 0 }$ for $x _ { 0 } + h$ is used in the middle equation to change this formula to an approximation for $f ^ { \prime } ( x _ { 0 } )$ . A similar change, $x _ { 0 }$ for $x _ { 0 } + 2 h$ ,is used in the last equation. This gives three formulas for approximating $f ^ { \prime } ( x _ { 0 } )$

$$
\begin{array} { l } { { f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 1 } { 2 h } [ - 3 f ( x _ { 0 } ) + 4 f ( x _ { 0 } + h ) - f ( x _ { 0 } + 2 h ) ] + \displaystyle \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 0 } ) , } } \\ { { \displaystyle f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 1 } { 2 h } [ - f ( x _ { 0 } - h ) + f ( x _ { 0 } + h ) ] - \displaystyle \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) , \quad \mathrm { a n d } } } \\ { { \displaystyle f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 1 } { 2 h } [ f ( x _ { 0 } - 2 h ) - 4 f ( x _ { 0 } - h ) + 3 f ( x _ { 0 } ) ] + \displaystyle \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 2 } ) . } } \end{array}
$$

Finally, note that since the last of these equations can be obtained from the first by simply replacing $h$ with $- h$ , there are actually only two formulas:

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 2 h } [ - 3 f ( x _ { 0 } ) + 4 f ( x _ { 0 } + h ) - f ( x _ { 0 } + 2 h ) ] + \frac { h ^ { 2 } } { 3 } f ^ { ( 3 ) } ( \xi _ { 0 } ) ,
$$

where $\xi _ { 0 }$ lies between $x _ { 0 }$ and $x _ { 0 } + 2 h$ , and

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 2 h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] - \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) ,
$$

where $\xi _ { 1 }$ lies between $( x _ { 0 } - h )$ and $( x _ { 0 } + h )$

Although the errors in both (4.4) and (4.5)are $O ( h ^ { 2 } )$ , the error in Eq. (4.5) is approx-imately half the error in Eq. (4.4). This is because Eq. (4.5) uses data on both sides of $x _ { 0 }$ and Eq. (4.4) uses data on only one side. Note also that $f$ needs to be evaluated at only two points in Eq. (4.5), whereas in Eq. (4.4) three evaluations are needed. Figure 4.2 gives an illustration of the approximation produced from Eq. (4.5). The approximation in Eq. (4.4) is useful near the ends of an interval, since information about $f$ outside the interval may not be available.

![](images/ca61908b8ffb7e03c3cda6413413da49d3c31306f4b00aee2fba7e9bff444061.jpg)  
Figure 4.2

The methods presented in Eqs. (4.4) and (4.5) are called three-point formulas (even though the third point $f ( x _ { 0 } )$ does not appear in Eq. (4.5)). Similarly, there are five-point formulas that involve evaluating the function at two more points, whose error term is $O ( h ^ { 4 } )$ . One is

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } [ f ( x _ { 0 } - 2 h ) - 8 f ( x _ { 0 } - h ) + 8 f ( x _ { 0 } + h ) - f ( x _ { 0 } + 2 h ) ] + \frac { h ^ { 4 } } { 3 0 } f ^ { ( 5 ) } ( \xi - \xi ) ,
$$

where $\xi$ lies between $x _ { 0 } \mathrm { ~ - ~ } 2 h$ and $x _ { 0 } + 2 h$ ，whose derivation is considered in Section 4.2. The other five-point formula is useful for end-point approximations, particularly with regard to the clamped cubic spline interpolation of Section 3.4. It is

$$
\begin{array} { c } { { f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 1 } { 1 2 h } [ - 2 5 f ( x _ { 0 } ) + 4 8 f ( x _ { 0 } + h ) - 3 6 f ( x _ { 0 } + 2 h ) } } \\ { { \displaystyle + 1 6 f ( x _ { 0 } + 3 h ) - 3 f ( x _ { 0 } + 4 h ) ] + \displaystyle \frac { h ^ { 4 } } { 5 } f ^ { ( 5 ) } ( \xi ) , } } \end{array}
$$

where $\xi$ lies between $x _ { 0 }$ and $x _ { 0 } + 4 h$ . Left-endpoint approximations are found using this formula with $h > 0$ and right-endpoint approximations with $h < 0$

# EXAMPLE 2

# Table 4.2

Values for $f ( x ) = x e ^ { x }$ are given in Table 4.2.   

<table><tr><td>f(x) x</td></tr><tr><td>1.8 10.889365</td></tr><tr><td>1.9 12.703199</td></tr><tr><td>2.0 14.778112</td></tr><tr><td>2.1 17.148957</td></tr><tr><td>2.2 19.855030</td></tr></table>

Since $f ^ { \prime } ( x ) = ( x + 1 ) e ^ { x }$ , we have $f ^ { \prime } ( 2 . 0 ) = 2 2 . 1 6 7 1 6 8$ . Approximating $f ^ { \prime } ( 2 . 0 )$ using the various three- and five-point formulas produces the following results.

# Three-Point Formulas

Using (4.4) with $\begin{array} { r } { h = 0 . 1 : \frac { 1 } { 0 . 2 } [ - 3 f ( 2 . 0 ) + 4 f ( 2 . 1 ) - f ( 2 . 2 ) ] = 2 2 . 0 3 2 3 1 0 , } \end{array}$ Using (4.4) with $\begin{array} { r } { h = - 0 . 1 : \frac { 1 } { - 0 . 2 } [ - 3 f ( 2 . 0 ) + 4 f ( 1 . 9 ) - f ( 1 . 8 ) ] = 2 2 . 0 5 4 5 2 . } \end{array}$ 5, Using (4.5) with $\begin{array} { r } { h = 0 . 1 : \frac { 1 } { 0 . 2 } [ f ( 2 . 1 ) - f ( 1 . 9 ) ] = 2 2 . 2 2 8 7 9 0 , } \end{array}$ Using (4.5) with $\begin{array} { r } { h = 0 . 2 : \frac { 1 } { 0 . 4 } [ f ( 2 . 2 ) - f ( 1 . 8 ) ] = 2 2 . 4 1 4 1 6 3 . } \end{array}$

The errors in the formulas are approximately

$1 . 3 5 \times 1 0 ^ { - 1 } , \quad 1 . 1 3 \times 1 0 ^ { - 1 } , \quad - 6 . 1 6 \times 1 0 ^ { - 2 } , \quad \mathrm { a n d } \quad - 2 . 4 7 \times 1 0 ^ { - 1 } ,$ respectively.

# Five-Point Formula

Using (4.6) with $h = 0 . 1$ (the only five-point formula applicable):

$$
\frac { 1 } { 1 . 2 } [ f ( 1 . 8 ) - 8 f ( 1 . 9 ) + 8 f ( 2 . 1 ) - f ( 2 . 2 ) ] = 2 2 . 1 6 6 9 9 6 .
$$

The error in this formula is approximately

$$
1 . 6 9 \times 1 0 ^ { - 4 } .
$$

The five-point formula is clearly superior. Note also that the error from Eq. (4.5) with $h = 0 . 1$ is approximately half of the magnitude of the error produced using Eq. (4.4) with either $h = 0 . 1$ or $h = - 0 . 1$ 1

Methods can also be derived to find approximations to higher derivatives of a function using only tabulated values of the function at various points. The derivation is algebraically tedious, however, so only a representative procedure will be presented.

Expand a function $f$ in'a third Taylor polynomial about a point $x _ { 0 }$ and evaluate at $x _ { 0 } + h$ and $x _ { 0 } - h$ . Then

$$
f ( x _ { 0 } + h ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) h + \frac { 1 } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) h ^ { 3 } + \frac { 1 } { 2 4 } f ^ { ( 4 ) } ( \xi _ { 1 } ) h ^ { 4 }
$$

and

$$
f ( x _ { 0 } - h ) = f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) h + \frac { 1 } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } - \frac { 1 } { 6 } f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 3 } + \frac { 1 } { 2 4 } f ^ { ( 4 ) } ( \xi _ { - 1 } ) h ^ { 4 } ,
$$

where $x _ { 0 } - h < \xi _ { - 1 } < x _ { 0 } < \xi _ { 1 } < x _ { 0 } + h$

If we add these equations, the term involving $f ^ { \prime } ( x _ { 0 } )$ cancels and we obtain

$$
f ( x _ { 0 } + h ) + f ( x _ { 0 } - h ) = 2 f ( x _ { 0 } ) + f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } + \frac { 1 } { 2 4 } [ f ^ { ( 4 ) } ( \xi _ { 1 } ) + f ^ { ( 4 ) } ( \xi _ { - 1 } ) ] h ^ { 4 } .
$$

Solving this equation for $f ^ { \prime \prime } ( x _ { 0 } )$ gives

$$
f ^ { \prime \prime } ( x _ { 0 } ) = \frac { 1 } { h ^ { 2 } } [ f ( x _ { 0 } - h ) - 2 f ( x _ { 0 } ) + f ( x _ { 0 } + h ) ] - \frac { h ^ { 2 } } { 2 4 } [ f ^ { ( 4 ) } ( \xi _ { 1 } ) + f ^ { ( 4 ) } ( \xi _ { - 1 } ) ] .
$$

Suppose $f ^ { ( 4 ) }$ is continuous on $[ x _ { 0 } - h , x _ { 0 } + h ]$ . Since $\textstyle { \frac { 1 } { 2 } } [ f ^ { ( 4 ) } ( \xi _ { 1 } ) + f ^ { ( 4 ) } ( \xi _ { - 1 } ) ]$ is between $f ^ { ( 4 ) } ( \xi _ { 1 } )$ and $f ^ { ( 4 ) } ( \pmb { \xi } _ { - 1 } )$ , the Intermediate Value Theorem implies that a number $\xi$ exists between $\xi _ { 1 }$ and $\xi _ { - 1 }$ , and hence in $( x _ { 0 } - h , x _ { 0 } + h )$ ,with

$$
f ^ { ( 4 ) } ( \xi ) = \frac { 1 } { 2 } \left[ f ^ { ( 4 ) } ( \xi _ { 1 } ) + f ^ { ( 4 ) } ( \xi _ { - 1 } ) \right] .
$$

This permits us to rewrite Eq. (4.8) as

$$
f ^ { \prime \prime } ( x _ { 0 } ) = \frac { 1 } { h ^ { 2 } } [ f ( x _ { 0 } - h ) - 2 f ( x _ { 0 } ) + f ( x _ { 0 } + h ) ] - \frac { h ^ { 2 } } { 1 2 } f ^ { ( 4 ) } ( \xi ) ,
$$

for some $\pmb { \xi }$ ，where $x _ { 0 } - h < \xi < x _ { 0 } + h$

# EXAMPLE 3

For the data given in Example 2, for $f ( x ) = x e ^ { x }$ , we can use Eq. (4.9) to approximate $f ^ { \prime \prime } ( 2 . 0 )$ . Since $f ^ { \prime \prime } ( x ) = ( x + 2 ) e ^ { x }$ , the exact value is $f ^ { \prime \prime } ( 2 . 0 ) = 2 9 . 5 5 6 2 2 4 . \ : \mathrm { U }$ Jsing (4.9) with $h = 0 . 1$ gives

$$
f ^ { \prime \prime } ( 2 . 0 ) \approx { \frac { 1 } { 0 . 0 1 } } [ f ( 1 . 9 ) - 2 f ( 2 . 0 ) + f ( 2 . 1 ) ] = 2 9 . 5 9 3 2 0 0 ,
$$

and using (4.9) with $h = 0 . 2$ gives

$$
f ^ { \prime \prime } ( 2 . 0 ) \approx { \frac { 1 } { 0 . 0 4 } } [ f ( 1 . 8 ) - 2 f ( 2 . 0 ) + f ( 2 . 2 ) ] = 2 9 . 7 0 4 2 7 5 .
$$

The errors are approximately $- 3 . 7 0 \times 1 0 ^ { - 2 }$ and $- 1 . 4 8 \times 1 0 ^ { - 1 }$ , respectively.

A particularly important subject in the study of numerical differentiation is the effect roundoff error plays in the approximation.Let us examine Eq. (4.5),

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 2 h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] - \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) ,
$$

more closely. Suppose that in evaluating $f ( x _ { 0 } + h )$ and $f ( x _ { 0 } - h )$ we encounter roundoff errors $e ( x _ { 0 } + h )$ and $e ( x _ { 0 } - h )$ . Then our computed values $\tilde { f } ( x _ { 0 } + h )$ and $\tilde { f } ( x _ { 0 } - h )$ are

related to the true values $f ( x _ { 0 } + h )$ and $f ( x _ { 0 } - h )$ by the formulas

$$
f ( x _ { 0 } + h ) = \tilde { f } ( x _ { 0 } + h ) + e ( x _ { 0 } + h )
$$

and

$$
f ( x _ { 0 } - h ) = \tilde { f } ( x _ { 0 } - h ) + e ( x _ { 0 } - h ) .
$$

The total error in the approximation,

$$
f ^ { \prime } ( x _ { 0 } ) - \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } - h ) } { 2 h } = \frac { e ( x _ { 0 } + h ) - e ( x _ { 0 } - h ) } { 2 h } - \frac { h ^ { 2 } } { 6 } f ^ { ( 3 ) } ( \xi _ { 1 } ) ,
$$

is due in part to roundoff error and in part to truncation error. If we assume that the roundoff errors $e ( x _ { 0 } \pm h )$ are bounded by some number $\varepsilon > 0$ and that the third derivative of $f$ is bounded by a number $M > 0$ , then

$$
\left| f ^ { \prime } ( x _ { 0 } ) - \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } - h ) } { 2 h } \right| \leq \frac { \varepsilon } { h } + \frac { h ^ { 2 } } { 6 } M .
$$

To reduce the truncation error, $h ^ { 2 } M / 6$ , we must reduce $h$ .But as $h$ is reduced, the roundoff error $\varepsilon / h$ grows. In practice, then, it is seldom advantageous to let $h$ be too small since the roundoff error will dominate the calculations.

# EXAMPLE 4

Consider using the values in Table 4.3 to approximate $f ^ { \prime } ( 0 . 9 0 0 )$ , where $f ( x ) = \sin x$ .The true value is cos $0 . 9 0 0 = 0 . 6 2 1 6 1$

Table 4.3   

<table><tr><td>X</td><td>sin x</td><td>X</td><td>sin x</td></tr><tr><td>0.800</td><td>0.71736</td><td>0.901</td><td>0.78395</td></tr><tr><td>0.850</td><td>0.75128</td><td>0.902</td><td>0.78457</td></tr><tr><td>0.880</td><td>0.77074</td><td>0.905</td><td>0.78643</td></tr><tr><td>0.890</td><td>0.77707</td><td>0.910</td><td>0.78950</td></tr><tr><td>0.895</td><td>0.78021</td><td>0.920</td><td>0.79560</td></tr><tr><td>0.898</td><td>0.78208</td><td>0.950</td><td>0.81342</td></tr><tr><td>0.899</td><td>0.78270</td><td>1.000</td><td>0.84147</td></tr></table>

Using the formula

$$
f ^ { \prime } ( 0 . 9 0 0 ) \approx \frac { f ( 0 . 9 0 0 + h ) - f ( 0 . 9 0 0 - h ) } { 2 h } ,
$$

with different values of $h$ , gives the approximations in Table 4.4.

The optimal choice for $h$ appears to lie between 0.005 and 0.05. If we perform some analysis on the error term,

$$
e ( h ) = \frac { \varepsilon } { h } + \frac { h ^ { 2 } } { 6 } M ,
$$

Table 4.4   

<table><tr><td>h</td><td>Approximation to f&#x27;(0.900) Error</td></tr><tr><td>0.001 0.62500</td><td>0.00339</td></tr><tr><td>0.002</td><td>0.62250 0.00089</td></tr><tr><td>0.005</td><td>0.62200 0.00039</td></tr><tr><td>0.010</td><td>0.62150 -0.00011</td></tr><tr><td>0.020</td><td>0.62150 -0.00011</td></tr><tr><td>0.050</td><td>0.62140 -0.00021</td></tr><tr><td>0.100</td><td>0.62055 -0.00106</td></tr></table>

we can use calculus to verify (see Exercise 23)that a minimum for $e$ occurs at $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ ， where

$$
M = \operatorname* { m a x } _ { x \in [ 0 . 8 0 0 , 1 . 0 0 ] } | f ^ { \prime \prime \prime } ( x ) | = \operatorname* { m a x } _ { x \in [ 0 . 8 0 0 , 1 . 0 0 ] } | \cos x | = \cos 0 . 8 \approx 0 . 6 9 6 7 1 .
$$

Since values of $f$ are given to five decimal places,it is reasonable to assume that the roundoff error is bounded by $\varepsilon = 0 . 0 0 0 0 0 5$ . Therefore,the optimal choice of $h$ is approximately

$$
h = \sqrt [ 3 ] { \frac { 3 ( 0 . 0 0 0 0 0 5 ) } { 0 . 6 9 6 7 1 } } \approx 0 . 0 2 8 ,
$$

which is consistent with the results in Table 4.4.

In practice, we cannot compute an optimal $h$ to use in approximating the derivative, since we have no knowledge of the third derivative of the function. But we must remain aware that reducing the step size will not always improve the approximation.

We have considered only the roundoff-error problems that are presented by the threepoint formula Eq. (4.5), but similar difficulties occur with all the differentiation formulas. The reason can be traced to the need to divide by a power of h. As we found in Section 1.2 (see,in particular,Example 3), division by smal numbers tends to exaggerate roundoff error and this operation should be avoided if possible. In the case of numerical differentiation,it is impossible to avoid the problem entirely, although the higher-order methods reduce the difficulty.

Keep in mind that as an approximation method, numerical differentiation is unstable, since the small values of $h$ needed to reduce truncation error also cause the roundoff error to grow.This is the first class of unstable methods we have encountered,and these techniques would be avoided if it were possible. However, in addition to being used for computational purposes,the formulas are needed for approximating the solutions of ordinary and partialdifferential equations.

# ExERcise SEt 4.1

1.Use the forward-diference formulas and backward-difference formulas to determine each missing entry in the following tables.

<table><tr><td>a.</td><td>f(x) X</td><td>f&#x27;(x)</td><td>b. x</td><td>f(x）</td><td>f&#x27;(x)</td></tr><tr><td></td><td>0.5 0.4794</td><td></td><td>0.0</td><td>0.00000</td><td></td></tr><tr><td>0.6</td><td>0.5646</td><td></td><td>0.2</td><td>0.74140</td><td></td></tr><tr><td>0.7</td><td>0.6442</td><td></td><td>0.4</td><td>1.3718</td><td></td></tr></table>

2. The data in Exercise l were taken from the following functions. Compute the actual errors in Exercise 1,and find error bounds using the error formulas.

a. $f ( x ) = \sin { x }$ $\ b . \quad f ( x ) = e ^ { x } - 2 x ^ { 2 } + 3 x - 1$

3.Use the most accurate three-oint formula to determine each missing entry in the following tables.

<table><tr><td rowspan=13 colspan=1>a.c.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=2>X</td><td rowspan=1 colspan=2>f(x)</td><td rowspan=1 colspan=2>f&#x27;(x)                               b.</td><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1>f(x)</td><td rowspan=2 colspan=1>f&#x27;(x)</td></tr><tr><td rowspan=1 colspan=2>1.1</td><td rowspan=1 colspan=2>9.025013</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>8.1</td><td rowspan=1 colspan=1>16.94410</td></tr><tr><td rowspan=1 colspan=2>1.2</td><td rowspan=1 colspan=2>11.02318</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>8.3</td><td rowspan=4 colspan=1>17.5649218.1905618.82091</td><td rowspan=4 colspan=1></td></tr><tr><td rowspan=2 colspan=2>1.3</td><td rowspan=2 colspan=2>13.46374</td><td rowspan=2 colspan=2></td><td rowspan=2 colspan=1>8.5</td></tr><tr></tr><tr><td rowspan=1 colspan=2>1.4</td><td rowspan=1 colspan=2>16.44465</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>8.7</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=2 colspan=3>f(x)</td><td rowspan=2 colspan=2>f&#x27;(x)                            d.     X</td><td rowspan=2 colspan=1>f(x)</td><td rowspan=2 colspan=1>f&#x27;(x)</td></tr><tr><td rowspan=1 colspan=2>X</td></tr><tr><td rowspan=1 colspan=2>2.9</td><td rowspan=2 colspan=3>-4.827866-4.240058</td><td rowspan=1 colspan=2>2.0</td><td rowspan=4 colspan=1>3.68879833.69057013.66881923.6245909</td><td rowspan=4 colspan=1></td></tr><tr><td rowspan=1 colspan=2>3.0</td><td rowspan=1 colspan=2>2.1</td></tr><tr><td rowspan=1 colspan=2>3.1</td><td rowspan=1 colspan=3>-3.496909</td><td rowspan=1 colspan=2>2.2</td></tr><tr><td rowspan=1 colspan=2>3.2</td><td rowspan=1 colspan=3>-2.596792</td><td rowspan=1 colspan=2>2.3</td></tr></table>

4. The data in Exercise 3 were taken from the following functions. Compute the actual errors in Exercise 3,and find error bounds using the error formulas.

a.f(x)=e2x c. $\begin{array} { l } { f ( x ) = e ^ { 2 x } } \\ { f ( x ) = x \cos x - x ^ { 2 } \sin x } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \quad } & { { } f ( x ) = x \ln x } \\ { \mathbf { d } . \quad } & { { } f ( x ) = 2 ( \ln x ) ^ { 2 } + 3 \sin x } \end{array}$

5. Use the formulas given in this section to determine, as accurately as possble, approximations for each missing entry in the following tables.

<table><tr><td>a.</td><td>X</td><td>f(x)</td><td>f&#x27;(x)</td><td>b. x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td></td><td>2.1</td><td>-1.709847</td><td></td><td>-3.0</td><td>9.367879</td><td></td></tr><tr><td></td><td>2.2</td><td>-1.373823</td><td></td><td>-2.8</td><td>8.233241</td><td></td></tr><tr><td></td><td>2.3</td><td>-1.119214</td><td></td><td>-2.6</td><td>7.180350</td><td></td></tr><tr><td></td><td>2.4</td><td>-0.9160143</td><td></td><td>-2.4</td><td>6.209329</td><td></td></tr><tr><td></td><td>2.5</td><td>-0.7470223</td><td></td><td>12.2</td><td>5.320305</td><td></td></tr><tr><td></td><td>2.6</td><td>-0.6015966</td><td></td><td>12.0</td><td>4.513417</td><td></td></tr></table>

6. The data in Exercise 5 were taken from the following functions.Compute the actual errors in Exercise 5,and find error bounds using the error formulas and Maple.

a. $f ( x ) = \tan x$ $\begin{array} { r l } { \mathbf { b } . \ } & { { } f ( x ) = e ^ { x / 3 } + x ^ { 2 } } \end{array}$

7.Use the following data and the knowledge that the first five derivatives of $f$ are bounded on [1,5] by 2,3,6,12 and 23,respectively, to approximate $f ^ { \prime } ( 3 )$ as accurately as possible. Find a bound for the error.

$$
\frac { x } { f ( x ) } \ | \begin{array} { l } { { 1 } } \\ { { 2 . 4 1 4 2 } } \end{array} | \ 2 . 6 7 3 4 \ | \begin{array} { l } { { 3 } } \\ { { 2 . 8 9 7 4 } } \end{array} | \begin{array} { l } { { 4 } } \\ { { 3 . 0 9 7 6 } } \end{array} | \ 3 . 2 8 0 4
$$

8.Repeat Exercise 7,assuming instead that the third derivative of $f$ is bounded on [1, 5] by 4.

9.Repeat Exercise 1 using four-digit rounding arithmetic,and compare the errors to those in Exercise 2.

10.Repeat Exercise 3 using four-digit chopping arithmetic,and compare the errors to those in Exercise 4.

11.Repeat Exercise 5 using four-digit rounding arithmetic, and compare the errors to those in Exercise 6.

12.Consider the following table of data:

<table><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.0</td></tr><tr><td rowspan=1 colspan=1>f(x)</td><td rowspan=1 colspan=1>0.9798652</td><td rowspan=1 colspan=1>0.9177710</td><td rowspan=1 colspan=1>0.808038</td><td rowspan=1 colspan=1>0.6386093</td><td rowspan=1 colspan=1>0.3843735</td></tr></table>

a.Use allthe appropriate formulas given in this section to approximate $f ^ { \prime } ( 0 . 4 )$ and $f ^ { \prime \prime } ( 0 . 4 )$ $\mathbf { b } _ { \bullet }$ Use allthe appropriate formulas given in this section to approximate $f ^ { \prime } ( 0 . 6 )$ and $f ^ { \prime \prime } ( 0 . 6 )$

13.Let $f ( x ) = \cos \pi x$ . Use Eq. (4.9) and the values of $f ( x )$ at $\ x \ = \ 0 . 2 5$ , 0.5,and 0.75 to approximate $f ^ { \prime \prime } ( 0 . 5 )$ . Compare this result to the exact value and to the approximation found in Exercise 11 of Section 3.4.Explain why this method is particularly accurate for this problem, and find a bound for the error.

14.Let $f ( x ) = 3 x e ^ { x } - \cos x$ . Use the following data and Eq. (4.9) to approximate $f ^ { \prime \prime } ( 1 . 3 )$ with $h = 0 . 1$ and with $h = 0 . 0 1$ ·

<table><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>1.20</td><td rowspan=1 colspan=1>1.29</td><td rowspan=1 colspan=1>1.30</td><td rowspan=1 colspan=1>1.31</td><td rowspan=1 colspan=1>1.40</td></tr><tr><td rowspan=1 colspan=1>f(x）</td><td rowspan=1 colspan=1>11.59006</td><td rowspan=1 colspan=1>13.78176</td><td rowspan=1 colspan=1>14.04276</td><td rowspan=1 colspan=1>14.30741</td><td rowspan=1 colspan=1>16.86187</td></tr></table>

Compare your results to $f ^ { \prime \prime } ( 1 . 3 )$

15.Consider the following table of data:

<table><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>1.0</td></tr><tr><td rowspan=1 colspan=1>f(x）</td><td rowspan=1 colspan=1>0.9798652</td><td rowspan=1 colspan=1>0.9177710</td><td rowspan=1 colspan=1>0.8080348</td><td rowspan=1 colspan=1>0.6386093</td><td rowspan=1 colspan=1>0.3843735</td></tr></table>

a. Use Eq. (4.7) to approximate $f ^ { \prime } ( 0 . 2 )$ $\mathbf { b } .$ Use Eq. (4.7) to approximate $f ^ { \prime } ( 1 . 0 )$ c. Use Eq. (4.6) to approximate $f ^ { \prime } ( 0 . 6 )$ ，

16. Derive an $O ( h ^ { 4 } )$ five-point formula to approximate $f ^ { \prime } ( x _ { 0 } )$ that uses $f ( x _ { 0 } - h ) , f ( x _ { 0 } ) , f ( x _ { 0 } +$ $h _ { i }$ ， $f ( x _ { 0 } + 2 h )$ , and $f ( x _ { 0 } + 3 h )$ . [Hint: Consider the expression $A f ( x _ { 0 } - h ) + B f ( x _ { 0 } + h ) +$ $C f ( x _ { 0 } + 2 h ) + D f ( x _ { 0 } + 3 h )$ . Expand in fourth Taylor polynomials,and choose $A , B , C$ , and $D$ appropriately.]

17.Use the formula derived in Exercise 16and the data of Exercise 15 to approximate $f ^ { \prime } ( 0 . 4 )$ and $f ^ { \prime } ( 0 . 8 )$

18.a.Analyze the roundoff errors, as in Example4,for the formula

$$
f ^ { \prime } ( x _ { 0 } ) = { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } ) } { h } } - { \frac { h } { 2 } } f ^ { \prime \prime } ( \xi _ { 0 } ) .
$$

b.Find an optimal $h > 0$ for the function given in Example 2.

19.In Exercise 7 of Section 3.3 data were given describing a car traveling on a straight road.That problem asked to predict the position and speed of the car when $t = 1 0 \ s$ . Use the following times and positions to predict the speed at each time listed.

$$
{ \frac { { \mathrm { T i m e } } } { \mathrm { D i s t a n c e } } } \left| { \begin{array} { l l l l l } { 0 } \\ { 0 } \end{array} } \right| \quad { \begin{array} { l } { 3 } \\ { 2 2 5 } \end{array} } \quad { \left| { \begin{array} { l l l l } { 5 } \\ { 3 8 3 } \end{array} } \right| } \quad { \begin{array} { l } { 8 } \\ { 6 2 3 } \end{array} } \left| { \begin{array} { l } { 1 0 } \\ { 7 4 2 } \end{array} } \right| \quad { \mathrm { 9 9 3 } }
$$

20.In a circuit with impressed voltage $\mathcal { E } ( t )$ and inductance $L$ , Kirchoffs first law gives the relationship

$$
\mathcal { E } ( t ) = L \frac { d i } { d t } + R i ,
$$

where $R$ is the resistance in the circuit and $i$ is the current. Suppose we measure the current for several values of $t$ and obtain:

$$
\frac { t } { i } | \begin{array} { c } { 1 . 0 0 } \\ { 3 . 1 0 } \end{array} | \begin{array} { c } { 1 . 0 1 } \\ { 3 . 1 2 } \end{array} | \begin{array} { c } { 1 . 0 2 } \end{array} | \begin{array} { c } { 1 . 0 3 } \\ { 3 . 1 8 } \end{array} | \begin{array} { c } { 1 . 0 } \\ { 3 . 2 4 } \end{array}
$$

where $t$ is measured in seconds, $i$ is in amperes,the inductance $L$ is a constant 0.98 henries, and the resistance is O.142 ohms. Approximate the voltage $\mathcal { E } ( t )$ when $t = 1 . 0 0$ ,1.01, 1.02, 1.03, and 1.04.

21.All calculus students know that the derivative of a function $f$ at $x$ can be defined as

$$
f ^ { \prime } ( x ) = \operatorname* { l i m } _ { h \to 0 } { \frac { f ( x + h ) - f ( x ) } { h } } .
$$

Choose your favorite function $f$ ， nonzero number $x$ ，and computer or calculator. Generate approximations $f _ { n } ^ { \prime } ( x )$ to $f ^ { \prime } ( x )$ by

$$
f _ { n } ^ { \prime } ( x ) = { \frac { f ( x + 1 0 ^ { - n } ) - f ( x ) } { 1 0 ^ { - n } } } ,
$$

for $n = 1 , 2 , \ldots , 2 0$ , and describe what happens.

22. Derive a method for approximating $f ^ { \prime \prime \prime } ( x _ { 0 } )$ whose error term is of order $h ^ { 2 }$ by expanding the function $f$ in a fourth Taylor polynomial about $x _ { 0 }$ and evaluating at $x _ { 0 } \pm h$ and $x _ { 0 } \pm 2 h$

23. Consider the function

$$
e ( h ) = \frac { \varepsilon } { h } + \frac { h ^ { 2 } } { 6 } M ,
$$

where $M$ is a bound for the third derivative of a function. Show that $e ( h )$ has a minimum at $\sqrt [ 3 ] { 3 \varepsilon / M }$

# 4.2 Richardson's Extrapolation

Richardson's extrapolation is used to generate high-accuracy results while using loworder formulas. Although the name attached to the method refers to a paper writen by L.F. Richardson and J.A. Gaunt [RG] in 1927,the idea behind the technique is much older. An interesting article regarding the history and application of extrapolation can be found in [Joy].

Extrapolation can be applied whenever it is known that an approximation technique has an error term with a predictable form, one that depends on a parameter, usually the step size h. Suppose that for each number $h \neq 0$ we have a formula $N ( h )$ that approximates an unknown value $M$ and that the truncation error involved with the approximation has the form

$$
M - N ( h ) = K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot ,
$$

for some collection of unknown constants $\cal { K } _ { 1 } , \cal { K } _ { 2 } , \cal { K } _ { 3 } , . . .$ ：

Since the truncation error is $O ( h )$ , we would expect, for example, that

$$
M - N ( 0 . 1 ) \approx 0 . 1 K _ { 1 } , \quad M - N ( 0 . 0 1 ) \approx 0 . 0 1 K _ { 1 } ,
$$

and, in general, $M - N ( h ) \approx K _ { 1 } h$ , unless tere was a large variation in magnitude among the constants $K _ { 1 } , K _ { 2 } , K _ { 3 } , \ldots$ ：

The object of extrapolation is to find an easy way to combine the rather inaccurate $O ( h )$ approximations in an appropriate way to produce formulas with a higher-order truncation error. Suppose, for example,we could combine the $N ( h )$ formulas so as to produce an $O ( h ^ { 2 } )$ approximation formula, $\hat { N } ( h )$ ,for $M$ with

$$
M - \hat { N } ( h ) = \hat { K } _ { 2 } h ^ { 2 } + \hat { K } _ { 3 } h ^ { 3 } + \cdots ,
$$

for some,again unknown, collection of constants $\hat { K } _ { 1 } , \hat { K } _ { 2 }$ ,.... Then we would have

$$
M - \hat { N } ( 0 . 1 ) \approx 0 . 0 1 \hat { K } _ { 2 } , \quad M - \hat { N } ( 0 . 0 1 ) \approx 0 . 0 0 0 1 \hat { K } _ { 2 } ,
$$

and so on. If the constants $K _ { 1 }$ and $\hat { K } _ { 2 }$ are roughly of the same magnitude, then the $\hat { N } ( h )$ approximations would be much bettr than the corresponding $N ( h )$ approximations. The extrapolation continues by combining the $\hat { N } ( h )$ approximations in a manner that produces formulas with $O ( h ^ { 3 } )$ truncation error, and so on.

To see specifically how we can generate these higher-order formulas,let us consider the formula for approximating $M$ of the form

$$
M = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot .
$$

Since the formula is assumed to hold for all positive $h$ , consider the result when we replace the parameter $\pmb { h }$ by half its value.Then we have the formula

$$
M = N \left( { \frac { h } { 2 } } \right) + K _ { 1 } { \frac { h } { 2 } } + K _ { 2 } { \frac { h ^ { 2 } } { 4 } } + K _ { 3 } { \frac { h ^ { 3 } } { 8 } } + \cdot \cdot \cdot .
$$

Subtracting (4.1O) from twice this equation eliminates the term involving $K _ { 1 }$ and gives

$$
M = \left[ N \left( { \frac { h } { 2 } } \right) + \left( N \left( { \frac { h } { 2 } } \right) - N ( h ) \right) \right] + K _ { 2 } \left( { \frac { h ^ { 2 } } { 2 } } - h ^ { 2 } \right) + K _ { 3 } \left( { \frac { h ^ { 3 } } { 4 } } - h ^ { 3 } \right) + \cdots .
$$

To facilitate the discussion, we define $N _ { 1 } ( h ) \equiv N ( h )$ and

$$
N _ { 2 } ( h ) = N _ { 1 } \left( \frac { h } { 2 } \right) + \left[ N _ { 1 } \left( \frac { h } { 2 } \right) - N _ { 1 } ( h ) \right] .
$$

Then we have the $O ( h ^ { 2 } )$ approximation formula for $M$ ：

$$
M = N _ { 2 } ( h ) - \frac { K _ { 2 } } { 2 } h ^ { 2 } - \frac { 3 K _ { 3 } } { 4 } h ^ { 3 } - \cdot \cdot \cdot .
$$

If we now replace $h$ by $h / 2$ in this formula, we have

$$
M = N _ { 2 } \left( \frac { h } { 2 } \right) - \frac { K _ { 2 } } { 8 } h ^ { 2 } - \frac { 3 K _ { 3 } } { 3 2 } h ^ { 3 } - \cdots .
$$

This can be combined with Eq.(4.11) to eliminate the $h ^ { 2 }$ term. Specifically, subtracting (4.11) from 4 times Eq.(4.12) gives

$$
3 M = 4 N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) + \frac { 3 K _ { 3 } } { 8 } h ^ { 3 } + \cdot \cdot \cdot ,
$$

and dividing by 3 gives an $O ( h ^ { 3 } )$ formula for approximating $M$ ：

$$
M = \left[ N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { N _ { 2 } ( h / 2 ) - N _ { 2 } ( h ) } { 3 } \right] + \frac { K _ { 3 } } { 8 } h ^ { 3 } + \cdot \cdot \cdot .
$$

By defining

$$
N _ { 3 } ( h ) \equiv N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { N _ { 2 } ( h / 2 ) - N _ { 2 } ( h ) } { 3 } ,
$$

we have the $O ( h ^ { 3 } )$ formula:

$$
M = N _ { 3 } ( h ) + \frac { K _ { 3 } } { 8 } h ^ { 3 } + \cdots .
$$

The process is continued by constructing an $O ( h ^ { 4 } )$ approximation

$$
N _ { 4 } ( h ) = N _ { 3 } \left( \frac { h } { 2 } \right) + \frac { N _ { 3 } ( h / 2 ) - N _ { 3 } ( h ) } { 7 } ,
$$

an $O ( h ^ { 5 } )$ approximation

$$
N _ { 5 } ( h ) = N _ { 4 } \left( \frac { h } { 2 } \right) + \frac { N _ { 4 } ( h / 2 ) - N _ { 4 } ( h ) } { 1 5 } ,
$$

and so on. In general, if $M$ can be written in the form

$$
M = N ( h ) + \sum _ { j = 1 } ^ { m - 1 } K _ { j } h ^ { j } + O ( h ^ { m } ) ,
$$

then for each $j = 2 , 3 , \dots , m$ ，we have an $O ( h ^ { j } )$ approximation of the form

$$
N _ { j } ( h ) = N _ { j - 1 } \left( \frac { h } { 2 } \right) + \frac { N _ { j - 1 } ( h / 2 ) - N _ { j - 1 } ( h ) } { 2 ^ { j - 1 } - 1 } .
$$

These approximations are generated by rows in the order indicated by the numbered entries in Table 4.5.This is done to take best advantage of the highest-order formulas.

Extrapolation can be applied whenever the truncation error for a formula has the form

$$
\sum _ { j = 1 } ^ { m - 1 } K _ { j } h ^ { \alpha _ { j } } + O ( h ^ { \alpha _ { m } } ) ,
$$

# Table 4.5

<table><tr><td>0(h)</td><td>0(h2)</td><td>0(h3)</td><td>0(h4)</td></tr><tr><td>1: Ni(h) = N(h)</td><td></td><td></td><td></td></tr><tr><td>2:N(）N(）</td><td>3: N(h)</td><td></td><td></td></tr><tr><td>4:N(）=N(）</td><td>5: N2（）</td><td>6: N(h)</td><td></td></tr><tr><td>7: N(）= N(）</td><td>8:N（）</td><td>9: N(）</td><td>10: N4(h)</td></tr></table>

for a collection of constants $K _ { j }$ and when $\alpha _ { 1 } < \alpha _ { 2 } < \alpha _ { 3 } < \cdot \cdot \cdot < \alpha _ { m }$ . In the next example we have $\alpha _ { j } = 2 j$

# EXAMPLE 1

The centered difference formula in Eq. (4.5) to approximate $f ^ { \prime } ( x _ { 0 } )$ can be expressed with an error formula:

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 2 h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] - \frac { h ^ { 2 } } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) - \frac { h ^ { 4 } } { 1 2 0 } f ^ { ( 5 ) } ( x _ { 0 } ) - \cdots .
$$

Since this error formula contains only even powers of $h$ ,extrapolation is more effective than as outlined in the opening discussion. In this case,we have the $O ( h ^ { 2 } )$ approximation

$$
f ^ { \prime } ( x _ { 0 } ) = N _ { 1 } ( h ) - \frac { h ^ { 2 } } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) - \frac { h ^ { 4 } } { 1 2 0 } f ^ { ( 5 ) } ( x _ { 0 } ) - \cdot \cdot \cdot ,
$$

where

$$
N _ { 1 } ( h ) \equiv N ( h ) = \frac { 1 } { 2 h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] .
$$

Replacing $h$ by $h / 2$ in this formula gives the approximation

$$
f ^ { \prime } ( x _ { 0 } ) = N _ { 1 } \left( { \frac { h } { 2 } } \right) - { \frac { h ^ { 2 } } { 2 4 } } f ^ { \prime \prime \prime } ( x _ { 0 } ) - { \frac { h ^ { 4 } } { 1 9 2 0 } } f ^ { ( 5 ) } ( x _ { 0 } ) - \cdot \cdot \cdot .
$$

Subtracting (4.15) from 4 times this equation eliminates the $O ( h ^ { 2 } )$ term that involves $f ^ { \prime \prime \prime } ( x _ { 0 } )$ and gives

$$
3 f ^ { \prime } ( x _ { 0 } ) = 4 N _ { 1 } \left( \frac { h } { 2 } \right) - N _ { 1 } ( h ) + \frac { h ^ { 4 } } { 1 6 0 } f ^ { ( 5 ) } ( x _ { 0 } ) + \cdot \cdot \cdot .
$$

Dividing by 3 provides an ${ \cal O } ( h ^ { 4 } )$ formula

$$
f ^ { \prime } ( x _ { 0 } ) = N _ { 2 } ( h ) + \frac { h ^ { 4 } } { 4 8 0 } f ^ { ( 5 ) } ( x _ { 0 } ) + \cdots ,
$$

where

$$
N _ { 2 } ( h ) = N _ { 1 } \left( \frac { h } { 2 } \right) + \frac { N _ { 1 } ( h / 2 ) - N _ { 1 } ( h ) } { 3 } .
$$

Continuing this procedure gives,for each $j = 2 , 3 , \dots$ ,an $O ( h ^ { 2 j } )$ approximation

$$
N _ { j } ( h ) = N _ { j - 1 } \left( \frac { h } { 2 } \right) + \frac { N _ { j - 1 } ( h / 2 ) - N _ { j - 1 } ( h ) } { 4 ^ { j - 1 } - 1 } .
$$

Notice that the denominator of the quotient is $4 ^ { j - 1 } - 1$ instead of $2 ^ { j - 1 } - 1$ because we are now eliminating powers of $h ^ { 2 }$ instead of powers of $\pmb { h }$ . Since $( h / 2 ) ^ { 2 } = h ^ { 2 } / 4$ , the multipliers used to eliminate the powers of $h ^ { 2 }$ are powers of 4 instead of 2.

Suppose that $x _ { 0 } = 2 . 0 , h = 0 . 2$ ,and $f ( x ) = x e ^ { x }$ . Then

$$
N _ { 1 } ( 0 . 2 ) = N ( 0 . 2 ) = { \frac { 1 } { 0 . 4 } } [ f ( 2 . 2 ) - f ( 1 . 8 ) ] = 2 2 . 4 1 4 1 6 0 ,
$$

$$
N _ { 1 } ( 0 . 1 ) = N ( 0 . 1 ) = 2 2 . 2 2 8 7 8 6 ,
$$

and

$$
N _ { 1 } ( 0 . 0 5 ) = N ( 0 . 0 5 ) = 2 2 . 1 8 2 5 6 4 .
$$

The extrapolation table for these data is shown in Table 4.6. The exact value of $f ^ { \prime } ( x ) =$ $x e ^ { x } + e ^ { x }$ at $x _ { 0 } = 2 . 0$ to six decimal places is 22.167168, so al the digits of $N _ { 3 } ( 0 . 2 )$ are exact, even though the best original approximation, $N _ { 1 } ( 0 . 0 5 )$ ,has only one decimal place of accuracy.

Table 4.6   

<table><tr><td colspan="3">N(0.2) = 22.414160</td></tr><tr><td>Ni(0.1) = 22.228786</td><td>N(0.1)- N1(0.2) N2(0.2) = N(0.1) +</td><td></td></tr><tr><td rowspan="2">N(0.05) = 22.182564</td><td>3 = 22.166995</td><td></td></tr><tr><td>N1(0.05)-N(0.1) N2(0.1)= N(0.05) +</td><td>N2(0.1) - N(0.2) N3(0.2) = N2(0.1) +</td></tr><tr><td></td><td>3 = 22.167157</td><td>15 = 22.167168</td></tr></table>

Since each column beyond the first in the extrapolation table is obtained by a simple averaging process, the technique can produce high-order approximations with minimal computational cost. However, as $k$ increases,the roundoff error in $N _ { 1 } ( h / 2 ^ { k } )$ will generally increase because the instability of numerical differentiation is related to the step size $h / 2 ^ { k }$

In Section 4.1, we discussed both three- and five-point methods for approximating $f ^ { \prime } ( x _ { 0 } )$ given various functional values of $f$ . The three-point methods were derived by differentiating a Lagrange interpolating polynomial for $f$ . The five-point methods can be obtained in a similar manner, but the derivation is tedious. Extrapolation can be used to derive these formulas more easily.

Suppose we expand the function $f$ in a fourth Taylor polynomial about $x _ { 0 }$ . Then

$$
\begin{array} { l } { { f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) ^ { 2 } + \displaystyle \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) ^ { 3 } } } \\ { { \displaystyle ~ + \displaystyle \frac { 1 } { 2 4 } f ^ { ( 4 ) } ( x _ { 0 } ) ( x - x _ { 0 } ) ^ { 4 } + \displaystyle \frac { 1 } { 1 2 0 } f ^ { ( 5 ) } ( \xi ) ( x - x _ { 0 } ) ^ { 5 } , } } \end{array}
$$

for some number $\pmb { \xi }$ between $\pmb { x }$ and $\pmb { x _ { 0 } }$ .Evaluating $f$ at $x _ { 0 } + h$ and $x _ { 0 } - h$ gives

$$
\begin{array} { l } { { f ( x _ { 0 } + h ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) h + \displaystyle \frac { 1 } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } + \displaystyle \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) h ^ { 3 } } } \\ { { \displaystyle ~ + \displaystyle \frac { 1 } { 2 4 } f ^ { ( 4 ) } ( x _ { 0 } ) h ^ { 4 } + \displaystyle \frac { 1 } { 1 2 0 } f ^ { ( 5 ) } ( \xi _ { 1 } ) h ^ { 5 } } } \end{array}
$$

and

$$
\begin{array} { l } { { f ( x _ { 0 } - h ) = f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) h + \displaystyle \frac { 1 } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } - \displaystyle \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) h ^ { 3 } } } \\ { { \displaystyle ~ + \displaystyle \frac { 1 } { 2 4 } f ^ { ( 4 ) } ( x _ { 0 } ) h ^ { 4 } - \displaystyle \frac { 1 } { 1 2 0 } f ^ { ( 5 ) } ( \xi _ { 2 } ) h ^ { 5 } , } } \end{array}
$$

where $x _ { 0 } - h < \xi _ { 2 } < x _ { 0 } < \xi _ { 1 } < x _ { 0 } + h$ . Subtracting Eq. (4.17) from Eq. (4.16) produces

$$
f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) = 2 h f ^ { \prime } ( x _ { 0 } ) + \frac { h ^ { 3 } } { 3 } f ^ { \prime \prime } ( x _ { 0 } ) + \frac { h ^ { 5 } } { 1 2 0 } [ f ^ { ( 5 ) } ( \xi _ { 1 } ) + f ^ { ( 5 ) } ( \xi _ { 2 } ) ] .
$$

If $f ^ { ( 5 ) }$ is continuous on $[ x _ { 0 } - h , x _ { 0 } + h ]$ , the Intermediate Value Theorem implies thal a number $\tilde { \pmb { \xi } }$ in $( x _ { 0 } - h , x _ { 0 } + h )$ exists with

$$
f ^ { ( 5 ) } ( \tilde { \xi } ) = \frac { 1 } { 2 } [ f ^ { ( 5 ) } ( \xi _ { 1 } ) + f ^ { ( 5 ) } ( \xi _ { 2 } ) ] .
$$

As a consequence, Eq.(4.18) can be solved for $f ^ { \prime } ( x _ { 0 } )$ to give the $O ( h ^ { 2 } )$ approximation

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 2 h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] - \frac { h ^ { 2 } } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) - \frac { h ^ { 4 } } { 1 2 0 } f ^ { ( 5 ) } ( \tilde { \xi } ) .
$$

Although the approximation in Eq. (4.19) is the same as that given in the three-point formula in Eq. (4.5), the unknown evaluation point occurs now in $f ^ { ( 5 ) }$ , rather than in $f ^ { \prime \prime \prime }$ · Extrapolation takes advantage of this by first replacing $h$ in Eq. (4.19) with $2 h$ to give the new formula

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 4 h } [ f ( x _ { 0 } + 2 h ) - f ( x _ { 0 } - 2 h ) ] - \frac { 4 h ^ { 2 } } { 6 } f ^ { \prime \prime \prime } ( x _ { 0 } ) - \frac { 1 6 h ^ { 4 } } { 1 2 0 } f ^ { ( 5 ) } ( \hat { \xi } ) ,
$$

where $\hat { \pmb { \xi } }$ is between $x _ { 0 } - 2 h$ and $x _ { 0 } + 2 h$

Multiplying Eq. (4.19) by 4 and subtracting Eq. (4.20) produces

$$
\begin{array} { c } { { 3 f ^ { \prime } ( x _ { 0 } ) = \displaystyle \frac { 2 } { h } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) ] - \displaystyle \frac { 1 } { 4 h } [ f ( x _ { 0 } + 2 h ) - f ( x _ { 0 } - 2 h ) ] } } \\ { { - \displaystyle \frac { h ^ { 4 } } { 3 0 } f ^ { ( 5 ) } ( \tilde { \xi } ) + \displaystyle \frac { 2 h ^ { 4 } } { 1 5 } f ^ { ( 5 ) } ( \hat { \xi } ) . } } \end{array}
$$

If $f ^ { ( 5 ) }$ is continuous on $[ x _ { 0 } - 2 h , x _ { 0 } + 2 h ]$ , an alternative method can be used to show that $f ^ { ( 5 ) } ( \tilde { \xi } )$ and $f ^ { ( 5 ) } ( \hat { \xi } )$ can be replaced by a common value $f ^ { ( 5 ) } ( \xi )$ . Using this result and dividing by 3 produces the five-point formula

$$
{ \mathrm { } ^ { \prime \prime } } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } [ f ( x _ { 0 } - 2 h ) - 8 f ( x _ { 0 } - h ) + 8 f ( x _ { 0 } + h ) - f ( x _ { 0 } + 2 h ) ] + \frac { h ^ { 4 } } { 3 0 } f ^ { ( 5 ) } ( \xi ) ,
$$

which is the five-point formula given as Eq.(4.6). Other formulas for first and higher derivatives can be derived in a similar manner. Some of these are considered in the exercises.

The technique of extrapolation is used throughout the text. The most prominent applications occur in approximating integrals in Section 4.5 and for determining approximate solutions to differential equations in Section 5.8.

# ExErcise Set 4.2

1. Apply the extrapolation process described in Example 1 to determine $N _ { 3 } ( h )$ , an approximation to $f ^ { \prime } ( x _ { 0 } )$ , for the following functions and stepsizes.

$$
\begin{array} { l l l } { { f ( x ) = \ln x , x _ { 0 } \pm 1 . 0 , h = 0 . 4 \qquad } } & { { { \bf b . } } } & { { f ( x ) = x + e ^ { x } , x _ { 0 } = 0 . 0 , h = 0 . 4 } } \\ { { f ( x ) = 2 ^ { x } \sin x , x _ { 0 } = 1 . 0 5 , h = 0 . 4 \qquad } } & { { { \bf d . } } } & { { f ( x ) = x ^ { 3 } \cos x , x _ { 0 } = 2 . 3 , h = 0 . 4 } } \end{array}
$$

2.Add another line to the extrapolation table in Exercise 1 to obtain the approximation $N _ { 4 } ( h )$

3.Repeat Exercise 1 using four-digit rounding arithmetic..

4.Repeat Exercise 2 using four-digit rounding arithmetic.

5.The following data give approximations to the integral

$$
M = \int _ { 0 } ^ { \pi } \sin x \ d x .
$$

$$
\mathsf { V } _ { 1 } ( h ) = 1 . 5 7 0 7 9 6 , \quad N _ { 1 } \left( \frac { h } { 2 } \right) = 1 . 8 9 6 1 1 9 , \quad N _ { 1 } \left( \frac { h } { 4 } \right) = 1 . 9 7 4 2 3 2 , \quad N _ { 1 } \left( \frac { h } { 8 } \right) = 1 . 9 9 3 5 7 0 .
$$

Assuming $M = N _ { 1 } ( h ) + K _ { 1 } h ^ { 2 } + K _ { 2 } h ^ { 4 } + K _ { 3 } h ^ { 6 } + K _ { 4 } h ^ { 8 } + O ( h ^ { 1 0 } )$ , construct an extrapolation table to determine $N _ { 4 } ( h )$ ·

6.The following data can be used toapproximate the integral

$$
M = \int _ { 0 } ^ { 3 \pi / 2 } \cos { x } d x .
$$

$$
\begin{array} { l c l } { { N _ { 1 } ( h ) = 2 . 3 5 6 1 9 4 , } } & { { N _ { 1 } \left( \displaystyle \frac { h } { 2 } \right) = - 0 . 4 8 7 9 8 3 7 , } } \\ { { } } & { { } } \\ { { N _ { 1 } \left( \displaystyle \frac { h } { 4 } \right) = - 0 . 8 8 1 5 7 3 2 , } } & { { N _ { 1 } \left( \displaystyle \frac { h } { 8 } \right) = - 0 . 9 7 0 9 1 5 7 . } } \end{array}
$$

Assume a formula exists of the type given in Exercise 5 and determine $N _ { 4 } ( h )$

7．Show that the five-point formula in Eq. (4.6)applied to $f ( x ) = x e ^ { x }$ at $x _ { 0 } = 2 . 0$ gives $N _ { 2 } ( 0 . 2 )$ in Table 4.6 when $h = 0 . 1$ and $N _ { 2 } ( 0 . 1 )$ when $h = 0 . 0 5$

8.The forward-difference formula can be expressed as

$$
f ^ { \prime } ( x _ { 0 } ) = { \frac { 1 } { h } } [ f ( x _ { 0 } + h ) - f ( x _ { 0 } ) ] - { \frac { h } { 2 } } f ^ { \prime \prime } ( x _ { 0 } ) - { \frac { h ^ { 2 } } { 6 } } f ^ { \prime \prime \prime } ( x _ { 0 } ) + O ( h ^ { 3 } ) .
$$

Use extrapolation to derive an ${ \cal O } ( h ^ { 3 } )$ formula for $f ^ { \prime } ( x _ { 0 } )$

9.Suppose that $N ( h )$ is an approximation to $M$ for every $h > 0$ and that

$$
M = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot ,
$$

for some constants $K _ { 1 } , K _ { 2 } , K _ { 3 }$ ,... Uuse te values $\begin{array} { r } { N ( h ) , N \left( \frac { h } { 3 } \right) } \end{array}$ ,and $N \left( { \frac { h } { 9 } } \right)$ to produce an $O ( h ^ { 3 } )$ approximation to $M$

10.Suppose that $N ( h )$ is an approximation to $M$ for every $\hbar > 0$ and that

$$
M = N ( h ) + K _ { 1 } h ^ { 2 } + K _ { 2 } h ^ { 4 } + K _ { 3 } h ^ { 6 } + \cdot \cdot \cdot ,
$$

for some constants $K _ { 1 } , K _ { 2 } , K _ { 3 } ,$ ... Use the values $\begin{array} { r } { N ( h ) , N \left( \frac { h } { 3 } \right) } \end{array}$ ,and $N \left( { \frac { h } { 9 } } \right)$ to produce an $O ( h ^ { 6 } )$ approximation to $M$

11.In calculus, we learn that $\begin{array} { r } { e = \operatorname* { l i m } _ { h \to 0 } ( 1 + h ) ^ { ! / h } } \end{array}$

a.Determine approximations to $e$ corresponding to $h = 0 . 0 4 , 0 . 0 2$ and 0.01.

$\scriptstyle \mathbf { b } .$ Use extrapolation on the approximations, assuming that constants $K _ { 1 } , K _ { 2 } , \ldots$ , exist with $e = ( 1 + h ) ^ { 1 / h } + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot _ { \cdot }$ to produce an $O ( h ^ { 3 } )$ approximation to $e$ ， where $h = 0 . 0 4$

c.Do you think that the assumption in part (b) is correct?

12.a.Show that

$$
\operatorname* { l i m } _ { h \to 0 } \left( { \frac { 2 + h } { 2 - h } } \right) ^ { 1 / h } = e .
$$

b. Compute approximations to $\pmb { e }$ using the formula $\begin{array} { r } { N ( h ) = \left( \frac { 2 + h } { 2 - h } \right) ^ { 1 / h } } \end{array}$ ,for $h = 0 . 0 4$ ,0.02, and 0.01.

c.Assume that $e = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot$ Use extrapolation, with at least 16 digits of precision,tocomputean $O ( h ^ { 3 } )$ approximation to $e$ with $h = 0 . 0 4$ . Do you think the assumption is correct?

d. Show that $N ( - h ) = N ( h )$

e. Use part (d) to show that $K _ { 1 } = K _ { 3 } = K _ { 5 } = \cdot \cdot = 0$ in the formula

$$
e = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } K _ { 4 } h ^ { 4 } + K _ { 5 } h ^ { 5 } + \cdot \cdot \cdot ,
$$

so that the formula reduces to

$$
e = N ( h ) + K _ { 2 } h ^ { 2 } + K _ { 4 } h ^ { 4 } + K _ { 6 } h ^ { 6 } + \cdot \cdot \cdot .
$$

f.Use theresults of part (e)and extrapolation to compute an $O ( h ^ { 6 } )$ approximation to $e$ with $h = 0 . 0 4$

13.Suppose the following extrapolation table has been constructed to approximate the number M with $M = N _ { 1 } ( h ) + K _ { 1 } h ^ { 2 } + K _ { 2 } h ^ { 4 } + K _ { 3 } h ^ { 6 }$ ：

$$
\begin{array} { l } { { { \displaystyle \bigwedge } N _ { 1 } ( h ) } } \\ { { } } \\ { { N _ { 1 } \left( \displaystyle { \frac { h } { 2 } } \right) } } \\ { { { \displaystyle N _ { 1 } \left( \displaystyle { \frac { h } { 4 } } \right) } } } \end{array} \quad N _ { 2 } ( h ) \qquad { \displaystyle \bigwedge } _ { 3 ( h ) }
$$

a. Showthat thelinearinterpolating polyomal $P _ { 0 , 1 } ( h )$ through $( h ^ { 2 } , N _ { 1 } ( h ) )$ and $( h ^ { 2 } / 4 , N _ { 1 } ( h / 2 ) )$ satisfies $P _ { 0 , 1 } ( 0 ) = N _ { 2 } ( h )$ . Similarly, show that $P _ { 1 , 2 } ( 0 ) = N _ { 2 } ( h / 2 )$

b.Show thathelinearinterpolatig polynomial $P _ { 0 , 2 } ( h )$ through $( h ^ { 4 } , N _ { 2 } ( h ) )$ and $( h ^ { 4 } / 1 6 , N _ { 2 } ( h / 2 ) )$ satisfies $P _ { 0 , 2 } ( 0 ) = N _ { 3 } ( h )$

14.Suppose that $N _ { 1 } ( h )$ is a formula that produces $O ( h )$ approximations to a number $M$ and that

$$
M = N _ { 1 } ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + \cdots ,
$$

for a collection of positive constants $K _ { 1 } , K _ { 2 }$ ，.... Then $N _ { 1 } ( h ) , N _ { 1 } ( h / 2 ) , N _ { 1 } ( h / 4 ) , . .$ .are all lower bounds for $M$ . What can be said about the extrapolated approximations $N _ { 2 } ( h )$ ， $N _ { 3 } ( h ) , \ldots \ldots 2$

15. The semiperimeters of regular polygons with $k$ sides that inscribe and circumscribe the unit circle were used by Archimedes before 2OO B.C. to approximate $\pi$ ， the circumference of a semicircle. Geometry can be used to show that the sequence of inscribed and circumscribed semiperimeters $\{ p _ { k } \}$ and $\{ P _ { k } \}$ ,respectively, satisfy

$$
p _ { k } = k \sin \left( \frac { \pi } { k } \right) \quad \mathrm { a n d } \quad P _ { k } = k \tan \left( \frac { \pi } { k } \right) ,
$$

with $p _ { k } < \pi < P _ { k }$ ,whenever $k \geq 4$

a. Show that $p _ { 4 } = 2 \sqrt { 2 }$ and $P _ { 4 } = 4$

b.Show that for $k \geq 4$ ,the sequences satisfy the recurrence relations

$$
P _ { 2 k } = { \frac { 2 p _ { k } P _ { k } } { p _ { k } + P _ { k } } } \quad { \mathrm { a n d } } \quad p _ { 2 k } = { \sqrt { p _ { k } P _ { 2 k } } } .
$$

$\pmb { \mathbb { c } _ { \bullet } }$ Approximate $\pi$ to within $1 0 ^ { - 4 }$ by computing $p _ { k }$ and $P _ { k }$ until $P _ { k } - p _ { k } < 1 0 ^ { - 4 }$

d.Use Taylor Series to show that

$$
\pi = p _ { k } + { \frac { \pi ^ { 3 } } { 3 ! } } \left( { \frac { 1 } { k } } \right) ^ { 2 } - { \frac { \pi ^ { 5 } } { 5 ! } } \left( { \frac { 1 } { k } } \right) ^ { 4 } + \cdot \cdot \cdot
$$

and

$$
\pi = \ P _ { k } - { \frac { \pi ^ { 3 } } { 3 } } \left( { \frac { 1 } { k } } \right) ^ { 2 } + { \frac { 2 \pi ^ { 5 } } { 1 5 } } \left( { \frac { 1 } { k } } \right) ^ { 4 } - \cdots .
$$

e.Use extrapolation with $h = 1 / k$ to better approximate $\pi$

# 4.3 Elements of Numerical Integration

The need often arises for evaluating the definite integral of a function that has no explicit antiderivative or whose antiderivative is not easy to obtain. The basic method involved in approximating $\textstyle \int _ { a } ^ { b } f ( x ) d x$ is called numerical quadrature. It uses a sum

$$
\sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } )
$$

to approximate $\textstyle \int _ { a } ^ { b } f ( x ) d x$

The methods of quadrature in this section are based on the interpolation polynomials given in Chapter 3. We first select a set of distinct nodes $\{ x _ { 0 } , \ldots , x _ { n } \}$ from the interval

$[ a , b ]$ . Then we integrate the Lagrange interpolating polynomial

$$
P _ { n } ( x ) = \sum _ { i = 0 } ^ { n } f ( x _ { i } ) L _ { i } ( x )
$$

and its truncation error term over $[ a , b ]$ to obtain

$$
\begin{array} { r } { \displaystyle \int _ { a } ^ { b } f ( x ) d x = \int _ { a } ^ { b } \sum _ { i = 0 } ^ { n } f ( x _ { i } ) L _ { i } ( x ) d x + \int _ { a } ^ { b } \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } d x } \\ { = \displaystyle \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) + \frac { 1 } { ( n + 1 ) ! } \int _ { a } ^ { b } \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) f ^ { ( n + 1 ) } ( \xi ( x ) ) d x , } \end{array}
$$

where $\xi ( x )$ is in $[ a , b ]$ for each $x$ and

$$
a _ { i } = \int _ { a } ^ { b } L _ { i } ( x ) d x , \quad { \mathrm { f o r } } \operatorname { e a c h } i = 0 , 1 , \dots , n .
$$

The quadrature formula is, therefore,

$$
\int _ { a } ^ { b } f ( x ) d x \approx \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) ,
$$

with error given by

$$
E ( f ) = { \frac { 1 } { ( n + 1 ) ! } } \int _ { a } ^ { b } \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) f ^ { ( n + 1 ) } ( \xi ( x ) ) d x .
$$

Before discussing the general situation of quadrature formulas,let us consider formulas produced by using first and second Lagrange polynomials with equally spaced nodes. This gives the Trapezoidal rule and Simpson's rule, which are commonly introduced in calculus courses.

To derive the Trapezoidal rule for approximating $\textstyle \int _ { a } ^ { b } f ( x ) \ d x$ ,let $x _ { 0 } = a , x _ { 1 } = b $ $h = b \dot { - } a$ and use the linear Lagrange polynomial:

$$
P _ { 1 } ( x ) = { \frac { ( x - x _ { 1 } ) } { ( x _ { 0 } - x _ { 1 } ) } } f ( x _ { 0 } ) + { \frac { ( x - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) } } f ( x _ { 1 } ) .
$$

Then,

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } f ( x ) d x = \int _ { x _ { 0 } } ^ { x _ { 1 } } \left[ \frac { ( x - x _ { 1 } ) } { ( x _ { 0 } - x _ { 1 } ) } f ( x _ { 0 } ) + \frac { ( x - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) } f ( x _ { \mathrm { I } } ) \right] d x } \\ { \displaystyle \qquad + \frac { 1 } { 2 } \int _ { x _ { 0 } } ^ { x _ { 1 } } f ^ { \prime \prime } ( \xi ( x ) ) ( x - x _ { 0 } ) ( x - x _ { 1 } ) d x . } \end{array}
$$

Since $( x - x _ { 0 } ) ( x - x _ { 1 } )$ does not change sign on $[ x _ { 0 } , x _ { 1 } ]$ , the Weighted Mean Value Theorem for Integrals can be applied to the error term to give,for some $\xi$ in $( x _ { 0 } , x _ { 1 } )$ ，

$$
{ \begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } f ^ { \prime \prime } ( \xi ( x ) ) ( x - x _ { 0 } ) ( x - x _ { 1 } ) d x = f ^ { \prime \prime } ( \xi ) \int _ { x _ { 0 } } ^ { x _ { 1 } } ( x - x _ { 0 } ) ( x - x _ { 1 } ) d x } \\ { = f ^ { \prime \prime } ( \xi ) \left[ { \frac { x ^ { 3 } } { 3 } } - { \frac { ( x _ { 1 } + x _ { 0 } ) } { 2 } } x ^ { 2 } + x _ { 0 } x _ { 1 } x \right] _ { x _ { 0 } } ^ { x _ { 1 } } } \\ { = - { \frac { h ^ { 3 } } { 6 } } f ^ { \prime \prime } ( \xi ) . } \end{array} }
$$

Consequently, Eq. (4.21) implies that

$$
\begin{array} { c } { { \displaystyle { \int _ { a } ^ { b } f ( x ) d x = \left[ \frac { ( x - x _ { 1 } ) ^ { 2 } } { 2 ( x _ { 0 } - x _ { 1 } ) } f ( x _ { 0 } ) + \frac { ( x - x _ { 0 } ) ^ { 2 } } { 2 ( x _ { 1 } - x _ { 0 } ) } f ( x _ { 1 } ) \right] _ { x _ { 0 } } ^ { x _ { 1 } } - \frac { h ^ { 3 } } { 1 2 } f ^ { \prime \prime } ( \xi ) } } } \\ { { { = \displaystyle { \frac { ( x _ { 1 } - x _ { 0 } ) } { 2 } [ f ( x _ { 0 } ) + f ( x _ { 1 } ) ] - \frac { h ^ { 3 } } { 1 2 } f ^ { \prime \prime } ( \xi ) . } } } } \end{array}
$$

Since $h = x _ { 1 } - x _ { 0 }$ , we have the following rule:

# Trapezoidal Rule:

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { h } { 2 } } [ f ( x _ { 0 } ) + f ( x _ { 1 } ) ] - { \frac { h ^ { 3 } } { 1 2 } } f ^ { \prime \prime } ( \xi ) .
$$

This is called the Trapezoidal rule because when $f$ is a function with positive values, $\textstyle \int _ { a } ^ { b } f ( x ) d x$ is approximated by the area in a trapezoid, as shown in Figure 4.3.

![](images/8e8a49acfafb6f15f349285c31ea41866bb322e908502e072ec1363ba91def80.jpg)  
Figure 4.3

Since the error term for the Trapezoidal rule involves $f ^ { \prime \prime }$ ， the rule gives the exact result when applied to anyfunction whose second derivative is identically zero, that is,any polynomial of degree one or less.

Simpson's rule results from integrating over $[ a , b ]$ the second Lagrange polynomial with nodes $x _ { 0 } = a$ ， $x _ { 2 } = b$ , and $x _ { 1 } = a + h$ ,where $h = ( b - a ) / 2$ . (See Figure 4.4.)

![](images/1f84ac4385c50e9fac6bda9af7d3ba8067b285ea175000e612cd1ede7660deb4.jpg)  
Figure 4.4

Therefore,

$$
{ \begin{array} { r l } { \displaystyle \int _ { a } ^ { b } f ( x ) d x = \int _ { x _ { 0 } } ^ { x _ { 2 } } \left[ { \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) } } f ( x _ { 0 } ) + { \frac { ( x - x _ { 0 } ) ( x - x _ { 2 } ) } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) } } f ( x _ { 1 } ) \right. } & { } \\ { \displaystyle \qquad + \left. { \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } } f ( x _ { 2 } ) \right] d x } & { } \\ { \displaystyle \qquad + \int _ { x _ { 0 } } ^ { x _ { 2 } } { \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) ( x - x _ { 2 } ) } { 6 } } f ^ { ( 3 ) } ( \xi ( x ) ) d x . } \end{array} }
$$

Deriving Simpson's rule in this manner, however, provides only an $O ( h ^ { 4 } )$ error term involving $\pmb { f } ^ { ( 3 ) }$ .By approachingthe probleminanother way,ahigher-order terminvolving $f ^ { ( 4 ) }$ can be derived.

To illustrate this alternative formula, suppose that $f$ is expanded in the third Taylor polynomial about $x _ { 1 }$ . Then for each $\pmb { x }$ in $[ x _ { 0 } , x _ { 2 } ]$ , a number $\xi ( x )$ in $( x _ { 0 } , x _ { 2 } )$ exists with

$$
f ( x ) = f ( x _ { 1 } ) + f ^ { \prime } ( x _ { 1 } ) ( x - x _ { 1 } ) + \frac { f ^ { \prime \prime } ( x _ { 1 } ) } { 2 } ( x - x _ { 1 } ) ^ { 2 } + \frac { f ^ { \prime \prime \prime } ( x _ { 1 } ) } { 6 } ( x - x _ { 1 } ) ^ { 3 } + \frac { f ^ { ( 4 ) } ( \xi ( x ) ) } { 2 4 } ( x - x _ { 1 } ) ^ { 2 } .
$$

and

$$
\begin{array} { r l r } {  { \int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = [ f ( x _ { 1 } ) ( x - x _ { 0 } ) + \frac { f ^ { \prime } ( x _ { 1 } ) } { 2 } ( x - x _ { 1 } ) ^ { 2 } + \frac { f ^ { \prime \prime } ( x _ { 1 } ) } { 6 } ( x - x _ { 1 } ) ^ { 3 }  } } \\ & { } & { \quad  + \frac { f ^ { \prime \prime \prime } ( x _ { 1 } ) } { 2 4 } ( x - x _ { 1 } ) ^ { 4 } ] _ { x _ { 0 } } ^ { x _ { 2 } } + \frac { 1 } { 2 4 } \int _ { x _ { 0 } } ^ { x _ { 2 } } f ^ { ( 4 ) } ( \xi ( x ) ) ( x - x _ { 1 } ) ^ { 4 } d x . } \end{array}
$$

Since $( x - x _ { 1 } ) ^ { 4 }$ is never negative on $[ x _ { 0 } , x _ { 2 } ]$ , the Weighted Mean Value Theorem for Inte. grals implies that

$$
{ \frac { 1 } { 2 4 } } \int _ { x _ { 0 } } ^ { x _ { 2 } } { f ^ { ( 4 ) } ( \xi ( x ) ) ( x - x _ { 1 } ) ^ { 4 } } d x = { \frac { f ^ { ( 4 ) } ( \xi _ { 1 } ) } { 2 4 } } \int _ { x _ { 0 } } ^ { x _ { 2 } } ( x - x _ { 1 } ) ^ { 4 } d x = { \frac { { f ^ { ( 4 ) } ( \xi _ { 1 } ) } } { 1 2 0 } } { ( x - x _ { 1 } ) ^ { 5 } } \Biggr ] ,
$$

for some number $\xi _ { 1 }$ in $( x _ { 0 } , x _ { 2 } )$

However, $h = x _ { 2 } - x _ { 1 } = x _ { 1 } - x _ { 0 }$ ,so

$$
( x _ { 2 } - x _ { 1 } ) ^ { 2 } - ( x _ { 0 } - x _ { 1 } ) ^ { 2 } = ( x _ { 2 } - x _ { 1 } ) ^ { 4 } - ( x _ { 0 } - x _ { 1 } ) ^ { 4 } = 0 ,
$$

whereas

$$
( x _ { 2 } - x _ { 1 } ) ^ { 3 } - ( x _ { 0 } - x _ { 1 } ) ^ { 3 } = 2 h ^ { 3 } \quad \mathrm { a n d } \quad ( x _ { 2 } - x _ { 1 } ) ^ { 5 } - ( x _ { 0 } - x _ { 1 } ) ^ { 5 } = 2 h ^ { 5 } .
$$

Consequently, Eq. (4.22) can be rewritten as

$$
\int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = 2 h f ( x _ { 1 } ) + { \frac { h ^ { 3 } } { 3 } } f ^ { \prime \prime } ( x _ { 1 } ) + { \frac { f ^ { ( 4 ) } ( \xi _ { 1 } ) } { 6 0 } } h ^ { 5 } .
$$

If we now replace $f ^ { \prime \prime } ( x _ { 1 } )$ by the approximation given in Eq. (4.9) of Section 4.1, we have

$$
\begin{array} { l } { { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = 2 h f ( x _ { 1 } ) + \frac { h ^ { 3 } } { 3 } \bigg \{ \frac { 1 } { h ^ { 2 } } [ f ( x _ { 0 } ) - 2 f ( x _ { 1 } ) + f ( x _ { 2 } ) ] - \frac { h ^ { 2 } } { 1 2 } f ^ { ( 4 ) } ( \xi _ { 2 } ) \bigg \} + \frac { f ^ { ( 4 ) } ( \xi _ { 1 } ) } { 6 0 } } } \\ { { \displaystyle \qquad = \frac { h } { 3 } [ f ( x _ { 0 } ) + 4 f ( x _ { 1 } ) + f ( x _ { 2 } ) ] - \frac { h ^ { 5 } } { 1 2 } \left[ \frac { 1 } { 3 } f ^ { ( 4 ) } ( \xi _ { 2 } ) - \frac { 1 } { 5 } f ^ { ( 4 ) } ( \xi _ { 1 } ) \right] . } } \end{array}
$$

It can be shown by alternative methods (see Exercise 18) that the values $\xi _ { 1 }$ and $\xi _ { 2 }$ in this expression can be replaced by a common value $\pmb { \xi }$ in $( x _ { 0 } , x _ { 2 } )$ . This gives Simpson's rule.

# Simpson's Rule:

$$
\int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = { \frac { h } { 3 } } [ f ( x _ { 0 } ) + 4 f ( x _ { 1 } ) + f ( x _ { 2 } ) ] - { \frac { h ^ { 5 } } { 9 0 } } f ^ { ( 4 ) } ( \xi ) .
$$

Since the error term involves the fourth derivative of $f$ , Simpson's rule gives exact results when applied to any polynomial of degree three or less.

# EXAMPLE 1

The Trapezoidal rule for a function $f$ on the interval [0, 2] is

$$
\int _ { 0 } ^ { 2 } f ( x ) d x \approx f ( 0 ) + f ( 2 ) ,
$$

and Simpson's rule for $f$ on [0,2] is

$$
\int _ { 0 } ^ { 2 } f ( x ) d x \approx { \frac { 1 } { 3 } } [ f ( 0 ) + 4 f ( 1 ) + f ( 2 ) ] .
$$

The results to three places for some elementary functions are summarized in Table 4.7.   
Notice that in each instance Simpson's Rule is significantly better.

# Table 4.7

<table><tr><td>f(x)</td><td>x²</td><td>x4</td><td>1/(x +1)</td><td>√1+x2</td><td>sin x</td><td>et</td></tr><tr><td>Exact value</td><td>2.667</td><td>6.400</td><td>1.099</td><td>2.958</td><td>1.416</td><td>6.389</td></tr><tr><td>Trapezoidal</td><td>4.000</td><td>16.000</td><td>1.333</td><td>3.326</td><td>0.909</td><td>8.389</td></tr><tr><td>Simpson&#x27;s</td><td>2.667</td><td>6.667</td><td>1.111</td><td>2.964</td><td>1.425</td><td>6.421</td></tr></table>

The standard derivation of quadrature error formulas is based on determining the class of polynomials for which these formulas produce exact results. The next definition is used to facilitate the discussion of this derivation.

# Definition 4.1

The degree of accuracy, or precision, of a quadrature formula is the largest positive inte-ger n such that the formulais exact for xk,for each k = O,1,..., n.

Definition 4.1 implies that the Trapezoidal and Simpson's rules have degrees of preci-sion one and three, respectively.

Integration and summation are linear operations; that is,

$$
\int _ { a } ^ { b } ( \alpha f ( x ) + \beta g ( x ) ) d x = \alpha \int _ { a } ^ { b } f ( x ) d x + \beta \int _ { a } ^ { b } g ( x ) d x
$$

and

$$
\sum _ { i = 0 } ^ { n } ( \alpha f ( x _ { i } ) + \beta g ( x _ { i } ) ) = \alpha \sum _ { i = 0 } ^ { n } f ( x _ { i } ) + \beta \sum _ { i = 0 } ^ { n } g ( x _ { i } ) ,
$$

for each pair of integrable functions f and g and each pair of real constants α and β. This implies (see Exercise 19) that the degree of precision of a quadrature formula is n if and only if the error E(P(x)) = O for all polynomials P(x) of degree k = 0,1,..., n, but $E ( P ( x ) ) \neq 0$ for some polynomial $P ( x )$ of degree $n + 1$ ·

The Trapezoidal and Simpson's rules are examples of a class of methods known as Newton-Cotes formulas. There are two types of Newton-Cotes formulas, open and closed.

The (n + 1)-point closed Newton-Cotes formula uses nodes xi = xo + ih, for i = 0,1,...,n, where xo = a, xn = b and h = (b -a)/n.(See Figure 4.5.) It is called closed because the endpoints of the closed interval [a,b] are included as nodes.The formula

![](images/1d1ed23dbd65392dfbf410a0d325b6ec9032d905fe2d48997c78980d70b8a129.jpg)  
Figure 4.5