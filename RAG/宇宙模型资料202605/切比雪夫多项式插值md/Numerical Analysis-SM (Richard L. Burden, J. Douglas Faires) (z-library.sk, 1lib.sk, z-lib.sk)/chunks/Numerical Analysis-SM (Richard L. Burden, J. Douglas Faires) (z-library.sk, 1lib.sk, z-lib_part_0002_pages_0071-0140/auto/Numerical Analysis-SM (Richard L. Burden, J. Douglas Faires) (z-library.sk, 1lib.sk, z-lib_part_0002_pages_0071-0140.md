The coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1</td><td>0</td><td>-5.193321</td><td>2.028118</td></tr><tr><td>0.25</td><td>0.7071068</td><td>-2.216388</td><td>-3.672233</td><td>4.896310</td></tr><tr><td>0.5</td><td>0</td><td>-3.134447</td><td>0</td><td>4.896310</td></tr><tr><td>0.75</td><td>-0.7071068</td><td>-2.216388</td><td>3.672233</td><td>2.028118</td></tr></table>

We have

$$
\int _ { 0 } ^ { 1 } s ( x ) d x = 0 . 0 0 0 0 0 0 , \quad s ^ { \prime } ( 0 . 5 ) = - 3 . 1 3 4 4 5 \quad { \mathrm { a n d } } \quad s ^ { \prime \prime } ( 0 . 5 ) = 0 . 0 0 0 0 0 0 .
$$

Also,

$$
\int _ { 0 } ^ { 1 } \cos \pi x d x = 0 , \quad f ^ { \prime } ( 0 . 5 ) = - \pi , \quad \mathrm { a n d } \quad f ^ { \prime \prime } ( 0 . 5 ) = 0 .
$$

18. Assume that the equation of the spline is

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$

The coefficients are given in the following table.

<table><tr><td>xi</td><td>ai</td><td>b</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.00000</td><td>-1.00000</td><td>0.499440</td><td>-0.154515</td></tr><tr><td>0.25</td><td>0.778801</td><td>-0.779251</td><td>0.383555</td><td>-0.101580</td></tr><tr><td>0.75</td><td>0.472367</td><td>-0.471881</td><td>0.231185</td><td>-0.0618174</td></tr></table>

We have

$$
\int _ { 0 } ^ { 1 } s ( x ) d x = 0 . 6 2 3 0 7 8 , \quad s ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 6 5 2 0 , \quad \mathrm { a n d } \quad s ^ { \prime \prime } ( 0 . 5 ) = 0 . 6 1 4 7 4 0 .
$$

Also,

$$
\int _ { 0 } ^ { 1 } e ^ { - x } d x = 0 . 6 3 2 1 2 0 5 , \quad f ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 6 5 3 0 7 \quad \mathrm { a n d } \quad f ^ { \prime \prime } ( 0 . 5 ) = 0 . 6 0 6 5 3 0 7 .
$$

19. Let $f ( x ) = a + b x + c x ^ { 2 } + d x ^ { 3 }$ . Clearly, $f$ satisfies properties (a), (c), (d), and (e) of Definition 3.10, and $f$ interpolates itself for any choice of $x _ { 0 } , \ldots , x _ { n }$ . Since (ii) of property (f) in Definition 3.10 holds, $f$ must be its own clamped cubic spline. However, $f ^ { \prime \prime } ( x ) = 2 c + 6 d x$ can be zero only at $x = - c / 3 d$ . Thus, part (i) of property (f) in Definition 3.10 cannot hold at two values $x _ { 0 }$ and $x _ { n }$ . Thus, $f$ cannot be a natural cubic spline.

20. The free cubic spline must be the linear function $L ( x )$ through all the data $\{ x _ { i } , f ( x _ { i } ) \} _ { i = 1 } ^ { n }$ since $L ^ { \prime \prime } ( x ) = 0$ for all $x$ . So properties (a), (b), (c), (d), (e), (f), (i) of Definition 3.10 would be satisfied.

If $f$ is linear, then $f$ is its own clamped cubic spline. If, for example, $f$ satisfies $f ( 0 ) = 0$ $f ( 1 ) = 1$ , $f ( 2 ) = 2$ , $f ^ { \prime } ( 0 ) = 1$ , and $f ^ { \prime } ( 2 ) = 0$ , then the data lie on a straight line but the function $f$ is not linear. In that case the spline is

$$
\begin{array} { r } { s ( x ) = \left\{ \begin{array} { l l } { x - \frac { 1 } { 4 } x ^ { 2 } + \frac { 1 } { 4 } x ^ { 3 } , \quad 0 \leq x \leq 1 } \\ { 1 + \frac { 5 } { 4 } ( x - 1 ) + \frac { 1 } { 2 } ( x - 1 ) ^ { 2 } - \frac { 3 } { 4 } ( x - 1 ) ^ { 3 } , \quad 1 \leq x \leq 2 , } \end{array} \right. } \end{array}
$$

which is not a linear function.

21. The piecewise linear approximation to $f$ is given by

$$
F ( x ) = { \left\{ \begin{array} { l l } { 2 0 ( e ^ { 0 . 1 } - 1 ) x + 1 , } & { { \mathrm { f o r ~ } } x { \mathrm { ~ i n ~ } } [ 0 , 0 . 0 5 ] } \\ { 2 0 ( e ^ { 0 . 2 } - e ^ { 0 . 1 } ) x + 2 e ^ { 0 . 1 } - e ^ { 0 . 2 } , } & { { \mathrm { f o r ~ } } x { \mathrm { ~ i n ~ } } ( 0 . 0 5 , 1 ] . } \end{array} \right. }
$$

We have

$$
\int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x = 0 . 1 1 0 7 9 3 6 \quad { \mathrm { ~ a n d ~ } } \int _ { 0 } ^ { 0 . 1 } f ( x ) \ d x = 0 . 1 1 0 7 0 1 4 .
$$

22. We have

$$
| f ( x ) - F ( x ) | \leq \frac { M } { 8 } \operatorname* { m a x } _ { 0 \leq j \leq n - 1 } | x _ { j + 1 } - x _ { j } | ^ { 2 } ,
$$

where $M = \mathrm { m a x } _ { a \leq x \leq b } | f ^ { \prime \prime } ( x ) |$ .

Error bounds for Exercise 21 are on $[ 0 , 0 . 1 ]$ , $| f ( x ) - F ( x ) | \leq 1 . 5 3 \times 1 0 ^ { - 3 }$ and

$$
\left| \int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x - \int _ { 0 } ^ { 0 . 1 } e ^ { 2 x } \ d x \right| \leq 1 . 5 3 \times 1 0 ^ { - 4 } .
$$

$^ { * } 2 3$ . Insert the following before Step 7 in Algorithm 3.4 and Step 8 in Algorithm 3.5: For $j = 0 , 1 , \ldots , n - 1$ set

Set

$^ { * } 2 4$ . Before STEP 7 in Algorithm 3.4 and STEP 8 in Algorithm 3.5 insert the following:

Set $I = 0$ ; For $j = 0 , \ldots , n - 1$ set

$$
I = a _ { j } h _ { j } + \frac { b _ { j } } { 2 } h _ { j } ^ { 2 } + \frac { c _ { j } } { 3 } h _ { j } ^ { 3 } + \frac { d _ { j } } { 4 } h _ { j } ^ { 4 } + I . \left( A c c u m u l a t e \int _ { x _ { j } } ^ { x _ { j + 1 } } S ( x ) d x . \right)
$$

OUTPUT (I).

25. (a) On $[ 0 , 0 . 0 5 ]$ , we have $s ( x ) ~ = ~ 1 . 0 0 0 0 0 0 + 1 . 9 9 9 9 9 9 x + 1 . 9 9 8 3 0 2 x ^ { 2 } + 1 . 4 0 1 3 1 0 x ^ { 3 }$ , and on $( 0 . 0 5 , 0 . 1 ]$ , we have $s ( x ) = 1 . 1 0 5 1 7 0 + 2 . 2 1 0 3 4 0 ( x - 0 . 0 5 ) + 2 . 2 0 8 4 9 8 ( x - 0 . 0 5 ) ^ { 2 } +$ $1 . 5 4 8 7 5 8 ( x - 0 . 0 5 ) ^ { 3 }$ . (b) $\begin{array} { r } { \int _ { 0 } ^ { 0 . 1 } s ( x ) \ d x = 0 . 1 1 0 7 0 1 } \end{array}$ (c) $1 . 6 \times 1 0 ^ { - 7 }$ (d) On $[ 0 , 0 . 0 5 ]$ , we have $S ( x ) = 1 + 2 . 0 4 8 1 1 x + 2 2 . 1 2 1 8 4 x ^ { 3 }$ , and on (0.05, 0.1], we have $S ( x ) = 1 . 1 0 5 1 7 1 + 2 . 2 1 4 0 2 8 ( x - 0 . 0 5 ) + 3 . 3 1 8 2 7 7 ( x - 0 . 0 5 ) ^ { 2 } - 2 2 . 1 2 1 8 4 ( x - 0 . 0 5 ) ^ { 3 }$ . $S ( 0 . 0 2 ) =$ 1.041139 and $S ( 0 . 0 2 ) = 1 . 0 4 0 8 1 1$ .

26. The five equations are

$$
a _ { 0 } = f ( x _ { 0 } ) , \quad a _ { 1 } = f ( x _ { 1 } ) , \quad a _ { 1 } + b _ { 1 } ( x _ { 2 } - x _ { 1 } ) + c _ { 1 } ( x _ { 2 } - x _ { 1 } ) ^ { 2 } = f ( x _ { 2 } ) .
$$

$$
a _ { 0 } + b _ { 0 } ( x _ { 1 } - x _ { 0 } ) + c _ { 0 } ( x _ { 1 } - x _ { 0 } ) ^ { 2 } = a _ { 1 } , \quad \mathrm { a n d } \quad b _ { 0 } + 2 c _ { 0 } ( x _ { 1 } - x _ { 0 } ) = b _ { 1 } .
$$

If $S \in C ^ { 2 }$ , then $S$ is a quadratic on $[ x _ { 0 } , x _ { 2 } ]$ and the solution may not be meaningful.

27. We have

$$
S ( x ) = \left\{ \begin{array} { l l } { 2 x - x ^ { 2 } , } & { 0 \leq x \leq 1 } \\ { 1 + ( x - 1 ) ^ { 2 } , } & { 1 \leq x \leq 2 } \end{array} \right.
$$

28. (a)

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>1950</td><td>151326</td><td>2906.50</td><td>0.00000</td><td>-1.06802</td></tr><tr><td>1960</td><td>179323</td><td>2586.10</td><td>-32.0407</td><td>1.32212</td></tr><tr><td>1970</td><td>203302</td><td>2341.92</td><td>7.62287</td><td>-0.94145</td></tr><tr><td>1980</td><td>226542</td><td>2211.94</td><td>-20.6208</td><td>3.03370</td></tr><tr><td>2000</td><td>249633</td><td>2709.63</td><td>70.3902</td><td>-2.34634</td></tr></table>

$S ( 1 9 4 0 ) = 1 2 3 , 3 2 9$ , $S ( 1 9 7 5 ) = 2 1 5 , 0 8 4$ , and $S ( 2 0 1 0 ) = 3 3 0 , 9 2 2$ .

(b) This is much better than using Lagrange interpolation, but still probably not very accurate.

29. The spline has the equation

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>0</td><td>75</td><td>-0.659292</td><td>0.219764</td></tr><tr><td>3</td><td>225</td><td>76.9779</td><td>1.31858</td><td>-0.153761</td></tr><tr><td>5</td><td>383</td><td>80.4071</td><td>0.396018</td><td>-0.177237</td></tr><tr><td>8</td><td>623</td><td>77.9978</td><td>-1.19912</td><td>0.0799115</td></tr></table>

The spline predicts a position of $s ( 1 0 ) = 7 7 4 . 8 4$ ft and a speed of $s ^ { \prime } ( 1 0 ) \ = \ 7 4 . 1 6 \ \mathrm { f t / s }$ s. To maximize the speed, we find the single critical point of $s ^ { \prime } ( x )$ , and compare the values of $s ( x )$ at this point and the endpoints. We find that max $s ^ { \prime } ( x ) = s ^ { \prime } ( 5 . 7 4 4 8 ) = 8 0 . 7 ~ \mathrm { f t / s } = 5 5 $ mi/h. The speed 55 mi/h was first exceeded at approximately 5.5 s.

30. (a) We have

The coefficients of the spline are given in the following table.

<table><tr><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0.00000000</td><td>0.01100783</td><td>0.00000000</td><td>-0.00000024</td></tr><tr><td>0.25000000</td><td>0.01062142</td><td>-0.00001681</td><td>0.00000016</td></tr><tr><td>0.50000000</td><td>0.01009276</td><td>-0.00000499</td><td>0.00000004</td></tr><tr><td>1.00000000</td><td>0.00990986</td><td>0.00000135</td><td>-0.00000002</td></tr></table>

This gives

$s _ { 0 } ( t ) = 0 . 0 1 1 0 0 7 8 3 t - 0 . 0 0 0 0 0 0 2 4 t ^ { 3 }$ , $s _ { 1 } ( t ) = 0 . 5 0 + 0 . 0 1 0 6 2 1 4 2 ( t - 4 7 . 2 3 ) - 0 . 0 0 0 0 1 6 8 1 ( t - 4 7 . 2 3 ) ^ { 2 } + 0 . 0 0 0 0 0 0 1 6 ( t - 4 7 . 2 3 ) ^ { 3 }$ , $s _ { 2 } ( t ) = 1 . 0 0 + 0 . 0 0 9 9 0 9 8 6 ( t - 9 7 . 4 9 ) + 0 . 0 0 0 0 0$ $\mathrm { . 0 0 0 0 0 1 3 5 ( } t - 9 7 . 4 9 ) ^ { 2 } - 0 . 0 0 0 0 0 0 0 2 ( t - 9 7 . 4 9 ) ^ { 3 }$ .

(b) The predicted time at the three-quarter mile pole is $1 : 1 2 . 2 5$ , which compares well with the actual time of $1 : 1 2 : 0 9$ .

(c) The starting speed is predicted to be $3 9 . 6 3 \ \mathrm { m i / h }$ and the speed at the finish line is predicted to be $3 5 . 7 8 \ \mathrm { m i / h }$ .

31. The equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

Sample 1   
Sample 2   

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>6.67</td><td>-0.44687</td><td>0</td><td>0.06176</td><td>6.67</td><td>1.6629</td><td>0</td><td>-0.00249</td></tr><tr><td>6</td><td>17.33</td><td>6.2237</td><td>1.1118</td><td>-0.27099</td><td>16.11</td><td>1.3943</td><td>-0.04477</td><td>-0.03251</td></tr><tr><td>10</td><td>42.67</td><td>2.1104</td><td>-2.1401</td><td>0.28109</td><td>18.89</td><td>-0.52442</td><td>-0.43490</td><td>0.05916</td></tr><tr><td>13</td><td>37.33</td><td>-3.1406</td><td>0.38974</td><td>-0.01411</td><td>15.00</td><td>-1.5365</td><td>0.09756</td><td>0.00226</td></tr><tr><td>17</td><td>30.10</td><td>-0.70021</td><td>0.22036</td><td>-0.02491</td><td>10.56</td><td>-0.64732</td><td>0.12473</td><td>-0.01113</td></tr><tr><td>20</td><td>29.31</td><td>-0.05069</td><td>-0.00386</td><td>0.00016</td><td>9.44</td><td>-0.19955</td><td>0.02453</td><td>-0.00102</td></tr></table>

$^ { * } 3 2$ . The three clamped splines have equations of the form

$$
s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the values of the coefficients are given in the following tables.

Spline 1   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>1.0</td><td>-0.347</td><td>-0.049</td><td>1.0</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td>0.447</td><td>-0.206</td><td>0.027</td><td></td></tr><tr><td>2</td><td>5</td><td>3.9</td><td>-0.074</td><td>0.033</td><td>0.342</td><td></td></tr><tr><td>3</td><td>6</td><td>4.2</td><td>1.016</td><td>1.058</td><td>-0.575</td><td></td></tr><tr><td>4</td><td>7</td><td>5.7</td><td>1.409</td><td>-0.665</td><td>0.156</td><td></td></tr><tr><td>5</td><td>8</td><td>6.6</td><td>0.547</td><td>-0.196</td><td>0.024</td><td></td></tr><tr><td>6</td><td>10</td><td>7.1</td><td>0.048</td><td>-0.053</td><td>-0.003</td><td></td></tr><tr><td>7</td><td>13</td><td>6.7</td><td>-0.339</td><td>-0.076</td><td>0.006</td><td></td></tr><tr><td>8</td><td>17</td><td>4.5</td><td></td><td></td><td></td><td>-0.67</td></tr></table>

Spline 2   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>17</td><td>4.5</td><td>3.0</td><td>-1.101</td><td>-0.126</td><td>3.0</td></tr><tr><td>1</td><td>20</td><td>7.0</td><td>-0.198</td><td>0.035</td><td>-0.023</td><td></td></tr><tr><td>2</td><td>23</td><td>6.1</td><td>-0.609</td><td>-0.172</td><td>0.280</td><td></td></tr><tr><td>3</td><td>24</td><td>5.6</td><td>-0.111</td><td>0.669</td><td>-0.357</td><td></td></tr><tr><td>4</td><td>25</td><td>5.8</td><td>0.154</td><td>-0.403</td><td>0.088</td><td></td></tr><tr><td>5</td><td>27</td><td>5.2</td><td>-0.401</td><td>0.126</td><td>-2.568</td><td></td></tr><tr><td>6</td><td>27.7</td><td>4.1</td><td></td><td></td><td></td><td>-4.0</td></tr></table>

Spline 3   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>27.7</td><td>4.1</td><td>0.330</td><td>2.262</td><td>-3.800</td><td>0.33</td></tr><tr><td>1</td><td>28</td><td>4.3</td><td>0.661</td><td>-1.157</td><td>0.296</td><td></td></tr><tr><td>2</td><td>29</td><td>4.1</td><td>-0.765</td><td>-0.269</td><td>-0.065</td><td></td></tr><tr><td>3</td><td>30</td><td>3.0</td><td></td><td></td><td></td><td>-1.5</td></tr></table>

33. The three natural splines have equations of the form

$$
S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the values of the coefficients are given in the following tables.

Spline 1   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>0.786</td><td>0.0</td><td>-0.086</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td>0.529</td><td>-0.257</td><td>0.034</td></tr><tr><td>2</td><td>5</td><td>3.9</td><td>-0.086</td><td>0.052</td><td>0.334</td></tr><tr><td>3</td><td>6</td><td>4.2</td><td>1.019</td><td>1.053</td><td>-0.572</td></tr><tr><td>4</td><td>7</td><td>5.7</td><td>1.408</td><td>-0.664</td><td>0.156</td></tr><tr><td>5</td><td>8</td><td>6.6</td><td>0.547</td><td>-0.197</td><td>0.024</td></tr><tr><td>6</td><td>10</td><td>7.1</td><td>0.049</td><td>-0.052</td><td>-0.003</td></tr><tr><td>7</td><td>13</td><td>6.7</td><td>-0.342</td><td>-0.078</td><td>0.007</td></tr><tr><td>8</td><td>17</td><td>4.5</td><td></td><td></td><td></td></tr></table>

Spline 2   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17</td><td>4.5</td><td>1.106</td><td>0.0</td><td>-0.030</td></tr><tr><td>1</td><td>20</td><td>7.0</td><td>0.289</td><td>-0.272</td><td>0.025</td></tr><tr><td>2</td><td>23</td><td>6.1</td><td>-0.660</td><td>-0.044</td><td>0.204</td></tr><tr><td>3</td><td>24</td><td>5.6</td><td>-0.137</td><td>0.567</td><td>-0.230</td></tr><tr><td>4</td><td>25</td><td>5.8</td><td>0.306</td><td>-0.124</td><td>-0.089</td></tr><tr><td>5</td><td>27</td><td>5.2</td><td>-1.263</td><td>-0.660</td><td>0.314</td></tr><tr><td>6</td><td>27.7</td><td>4.1</td><td></td><td></td><td></td></tr></table>

Spline 3   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>27.7</td><td>4.1</td><td>0.749</td><td>0.0</td><td>-0.910</td></tr><tr><td>1</td><td>28</td><td>4.3</td><td>0.503</td><td>-0.819</td><td>0.116</td></tr><tr><td>2</td><td>29</td><td>4.1</td><td>-0.787</td><td>-0.470</td><td>0.157</td></tr><tr><td>3</td><td>30</td><td>3.0</td><td></td><td></td><td></td></tr></table>

# Exercise Set 3.6, page 170

1. The parametric cubic Hermite approximations are as follows.

$$
\begin{array} { l } { x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , y ( t ) = - 2 t ^ { 3 } + 3 t ^ { 2 } + t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 4 . 5 t ^ { 2 } + 0 . 5 t , y ( t ) = - 3 t ^ { 3 } + 4 . 5 t ^ { 2 } + 0 . 5 t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , y ( t ) = - 4 t ^ { 3 } + 5 t ^ { 2 } + t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 3 t ^ { 2 } + 2 t , y ( t ) = 2 t } \end{array}
$$

2. The parametric cubic B´ezier approximations are as follows.

$$
\begin{array} { r l } & { x ( t ) = - 1 0 t ^ { 3 } + 1 2 t ^ { 2 } + 3 t , \quad y ( t ) = 2 t ^ { 3 } - 3 t ^ { 2 } + 3 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 1 3 . 5 t ^ { 2 } + 1 . 5 t , \quad y ( t ) = - t ^ { 3 } + 1 . 5 t ^ { 2 } + 1 . 5 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 1 2 t ^ { 2 } + 3 t , \quad y ( t ) = - 4 t ^ { 3 } + 3 t ^ { 2 } + 3 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 9 t ^ { 2 } + 6 t , \quad y ( t ) = 8 t ^ { 3 } - 1 2 t ^ { 2 } + 6 t } \end{array}
$$

3. The parametric cubic B´ezier approximations are as follows.

(a) $\begin{array} { l } { x ( t ) = - 1 1 . 5 t ^ { 3 } + 1 5 t ^ { 2 } + 1 . 5 t + 1 , y ( t ) = - 4 . 2 5 t ^ { 3 } + 4 . 5 t ^ { 2 } + 0 . 7 5 t + 1 } \\ { x ( t ) = - 6 . 2 5 t ^ { 3 } + 1 0 . 5 t ^ { 2 } + 0 . 7 5 t + 1 , y ( t ) = - 3 . 5 t ^ { 3 } + 3 t ^ { 2 } + 1 . 5 t + 1 } \end{array}$   
(b)   
(c) For $t$ between $( 0 , 0 )$ and $( 4 , 6 )$ , we have

$$
x ( t ) = - 5 t ^ { 3 } + 7 . 5 t ^ { 2 } + 1 . 5 t , y ( t ) = - 1 3 . 5 t ^ { 3 } + 1 8 t ^ { 2 } + 1 . 5 t ,
$$

and for $t$ between $( 4 , 6 )$ and $( 6 , 1 )$ , we have

$$
x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t + 4 , y ( t ) = 4 t ^ { 3 } - 6 t ^ { 2 } - 3 t + 6 .
$$

(d) For $t$ between $( 0 , 0 )$ and $( 2 , 1 )$ , we have

$$
\begin{array} { r } { x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t , y ( t ) = - 0 . 5 t ^ { 3 } + 1 . 5 t , } \end{array}
$$

for $t$ between $( 2 , 1 )$ and $( 4 , 0 )$ , we have

$$
x ( t ) = - 4 t ^ { 3 } + 3 t ^ { 2 } + 3 t + 2 , \quad y ( t ) = - t ^ { 3 } + 1 ,
$$

and for $t$ between $( 4 , 0 )$ and $( 6 , - 1 )$ , we have

$$
x ( t ) = - 8 . 5 t ^ { 3 } + 1 3 . 5 t ^ { 2 } - 3 t + 4 , y ( t ) = - 3 . 2 5 t ^ { 3 } + 5 . 2 5 t ^ { 2 } - 3 t .
$$

4. Between $( 3 , 6 )$ and $( 2 , 2 )$ , we have

$$
x ( t ) = 0 . 5 t ^ { 3 } - 2 . 4 t ^ { 2 } + 0 . 9 t + 3 , y ( t ) = 6 . 5 t ^ { 3 } - 1 2 t ^ { 2 } + 1 . 5 t + 6 ;
$$

between $( 2 , 2 )$ and $( 6 , 6 )$ , we have

$$
x ( t ) = - 5 . 9 t ^ { 3 } + 8 . 4 t ^ { 2 } + 1 . 5 t + 2 , y ( t ) = - 3 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t + 2 ;
$$

between $( 6 , 6 )$ and $( 5 , 2 )$ , we have

$$
x ( t ) = - 2 . 5 t ^ { 3 } + 4 . 5 t ^ { 2 } - 3 t + 6 , y ( t ) = 6 . 8 t ^ { 3 } - 1 0 . 2 t ^ { 2 } - 0 . 6 t + 6 ;
$$

and between $( 5 , 2 )$ and $( 6 . 5 , 3 )$ , we have

$$
x ( t ) = - 4 . 2 t ^ { 3 } + 7 . 2 t ^ { 2 } - 1 . 5 t + 5 , y ( t ) = 0 . 1 t ^ { 3 } - 0 . 6 t ^ { 2 } + 1 . 5 t + 2 .
$$

\*5. (a) Using the forward divided difference gives the following table.

<table><tr><td>0</td><td>uo</td><td></td><td></td></tr><tr><td>0</td><td>uo</td><td>3(u1-uo)</td><td></td></tr><tr><td>1</td><td>u3</td><td>u3-uo</td><td>U3 -3u1+ 2uo</td></tr><tr><td>1</td><td>u3</td><td>3(u3-u2)</td><td>2u3-3u2+uo u3-3u2+3u1-uo</td></tr></table>

Therefore,

$$
\begin{array} { r l r } {  { u ( t ) = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( u _ { 3 } - 3 u _ { 1 } + 2 u _ { 0 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 2 } ( t - 1 ) } } \\ & { } & \\ & { } & { \quad = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( - 6 u _ { 1 } + 3 u _ { 0 } + 3 u _ { 2 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 3 } . \quad } \end{array}
$$

Similarly, $v ( t ) = v _ { 0 } + 3 ( v _ { 1 } - v _ { 0 } ) t + ( 3 v _ { 2 } - 6 v _ { 1 } + 3 v _ { 0 } ) t ^ { 2 } + ( v _ { 3 } - 3 v _ { 2 } + 3 v _ { 1 } - v _ { 0 } ) t ^ { 3 } .$

(b) Using the formula for Bernstein polynomials gives, for $f$ ,

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 0 } ^ { 3 } \binom { 3 } { k } u _ { k } t ^ { k } ( 1 - t ) ^ { 3 - k } = u _ { 0 } ( 1 - t ) ^ { 3 } + 3 u _ { 1 } t ( 1 - t ) ^ { 2 } + 3 u _ { 2 } t ^ { 2 } ( 1 - t ) + u _ { 3 } t ^ { 3 } } } \\ { { { } } } \\ { { = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( 3 u _ { 2 } - 6 u _ { 1 } + 3 u _ { 0 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 3 } } } \\ { { { } } } \\ { { = u ( t ) } } \end{array}
$$

and, for $g$

$$
\begin{array} { r l } { \displaystyle \sum _ { k = 0 } ^ { 3 } \binom { 3 } { k } v _ { k } t ^ { k } ( 1 - t ) ^ { 3 - k } = v _ { 0 } ( 1 - t ) ^ { 3 } + 3 v _ { 1 } t ( 1 - t ) ^ { 2 } + 3 v _ { 2 } t ^ { 2 } ( 1 - t ) + v _ { 3 } t ^ { 3 } } & { } \\ { = v _ { 0 } + 3 ( v _ { 1 } - v _ { 0 } ) t + ( 3 v _ { 2 } - 6 v _ { 1 } + 3 v _ { 0 } ) t ^ { 2 } + ( v _ { 3 } - 3 v _ { 2 } + 3 v _ { 1 } - v _ { 0 } ) t ^ { 3 } } & { } \\ { = v ( t ) . } \end{array}
$$

# Numerical Differentiation and Integration

Exercise Set 4.1, page 182

1. From the forward-backward difference formula (4.1), we have the following approximations:

(a) $f ^ { \prime } ( 0 . 5 ) \approx 0 . 8 5 2 0$ , $f ^ { \prime } ( 0 . 6 ) \approx 0 . 8 5 2 0$ , $f ^ { \prime } ( 0 . 7 ) \approx 0 . 7 9 6 0$ (b) $f ^ { \prime } ( 0 . 0 ) \approx 3 . 7 0 7 0$ , $f ^ { \prime } ( 0 . 2 ) \approx 3 . 1 5 2 0$ , $f ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 2 0$

2. The approximations are in the following tables

<table><tr><td colspan="2">*(a) x</td><td>f(x)</td><td>f&#x27;（x）</td></tr><tr><td colspan="2"></td><td></td><td></td></tr><tr><td colspan="2">1 0.3 -0.2</td><td>1.9507 2.0421</td><td>0.9140 0.1800</td></tr><tr><td colspan="2">-0.1</td><td>2.0601</td><td>0.1800</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>X</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.0</td><td>1.0000</td><td>1.3125</td></tr><tr><td>1.2</td><td>1.2625</td><td>1.3125</td></tr><tr><td>1.4</td><td>1.6595</td><td>1.9850</td></tr></table>

3. The approximations are in the following tables.

<table><tr><td rowspan="7">(a)</td><td></td></tr><tr><td>x Actual Error</td><td>Error] Bound</td></tr><tr><td>0.5 0.0255</td><td>0.0282</td></tr><tr><td>0.6 0.0267</td><td>0.0282</td></tr><tr><td>0.7 0.0312</td><td>0.0322</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>0.0</td><td>0.2930</td><td>0.3000</td></tr><tr><td></td><td>0.2</td><td>0.2694</td><td>0.2779</td></tr><tr><td></td><td>0.4</td><td>0.2602</td><td>0.2779</td></tr></table>

4. (a)

<table><tr><td>X Actual Error</td><td></td><td>Error Bound</td></tr><tr><td>-0.3</td><td>0.34457</td><td>0.36842</td></tr><tr><td>-0.2</td><td>0.35633</td><td>0.36842</td></tr><tr><td>-0.1</td><td>0.38533</td><td>0.39203</td></tr></table>

<table><tr><td>X</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.0</td><td>0.31250</td><td>0.33646</td></tr><tr><td>1.2</td><td>0.32507</td><td>0.33646</td></tr><tr><td>1.4</td><td>0.35712</td><td>0.36729</td></tr></table>

5. For the endpoints of the tables, we use Formula (4.4). The other approximations come from Formula (4.5).

\*(a) $f ^ { \prime } ( 1 . 1 ) \approx 1 7 . 7 6 9 7 0 5$ , $f ^ { \prime } ( 1 . 2 ) \approx 2 2 . 1 9 3 6 3 5$ , $f ^ { \prime } ( 1 . 3 ) \approx 2 7 . 1 0 7 3 5 0$ , $f ^ { \prime } ( 1 . 4 ) \approx 3 2 . 1 5 0 8 5 0$ (b) $f ^ { \prime } ( 8 . 1 ) \approx 3 . 0 9 2 0 5 0$ , $f ^ { \prime } ( 8 . 3 ) \approx 3 . 1 1 6 1 5 0$ , $f ^ { \prime } ( 8 . 5 ) \approx 3 . 1 3 9 9 7 5$ , $f ^ { \prime } ( 8 . 7 ) \approx 3 . 1 6 3 5 2 5$ (c) $f ^ { \prime } ( 2 . 9 ) \approx 5 . 1 0 1 3 7 5$ , $f ^ { \prime } ( 3 . 0 ) \approx 6 . 6 5 4 7 8 5$ , $f ^ { \prime } ( 3 . 1 ) \approx 8 . 2 1 6 3 3 0$ , $f ^ { \prime } ( 3 . 2 ) \approx 9 . 7 8 6 0 1 0$ (d) $f ^ { \prime } ( 2 . 0 ) \approx 0 . 1 3 5 3 3 1 5 0 , f ^ { \prime } ( 2 . 1 ) \approx - 0 . 0 9 9 8 9 5 5 0 , f ^ { \prime } ( 2 . 2 ) \approx - 0 . 3 2 9 8 9 6 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 5 5 4 6 7 0 0 9 6 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 1 9 5 3 6 7 0 2 4 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 3 2 5 3 3 8 9 6 0 0 , f ^ { \prime } ( 2 . 3 )$

6. For the endpoints of the tables, we use Formula (4.4). The other approximations come from Formula (4.5).

<table><tr><td rowspan="3">(a)</td><td colspan="3"></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>- 0.3</td><td>-0.27652</td><td>-0.06030</td></tr><tr><td rowspan="2">-0.2</td><td></td><td></td><td>0.57590</td></tr><tr><td>-0.1</td><td>-0.25074 -0.16134</td><td>1.25370</td></tr><tr><td rowspan="2"></td><td>0.0</td><td>0.0</td><td>1.97310</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(xc)</td></tr><tr><td>7.4</td><td>-68.3193</td><td>-16.6933</td></tr><tr><td>7.6</td><td>-71.6982</td><td>-17.0958</td></tr><tr><td>7.8</td><td>-75.1576</td><td>-17.4980</td></tr><tr><td>8.0</td><td>-78.6974</td><td>-17.9000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3"></td></tr><tr><td>C</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.1</td><td>1.52918</td><td>1.34360</td></tr><tr><td>1.2</td><td>1.64024</td><td>0.87760</td></tr><tr><td>1.3</td><td>1.70470</td><td>0.36265</td></tr><tr><td>1.4</td><td>1.71277</td><td>-0.20125</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>f(x)</td><td>f&#x27;(xc)</td></tr><tr><td colspan="2">-2.7</td><td>0.054797</td><td>-0.915178</td></tr><tr><td colspan="2">-2.5</td><td>0.11342</td><td>1.50141</td></tr><tr><td colspan="2">-2.3</td><td>0.65536</td><td>2.17825</td></tr><tr><td colspan="2">-2.1</td><td>0.98472</td><td>1.11535</td></tr></table>

7. The errors and error bounds are given in the following tables.

<table><tr><td colspan="2">*（a)</td><td colspan="2"></td></tr><tr><td colspan="2">x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">1.1</td><td>0.280322</td><td>0.359033</td></tr><tr><td colspan="2">1.2</td><td>0.147282</td><td>0.179517</td></tr><tr><td colspan="2">1.3</td><td>0.179874</td><td>0.219262</td></tr><tr><td colspan="2">1.4</td><td>0.378444</td><td>0.438524</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>8.1</td><td>0.00018594</td><td>0.000020322</td></tr><tr><td></td><td>8.3</td><td>0.00010551</td><td>0.000010161</td></tr><tr><td></td><td>8.5</td><td>9.116 × 10-5</td><td>0.000009677</td></tr><tr><td></td><td>8.7</td><td>0.00020197</td><td>0.000019355</td></tr></table>

<table><tr><td colspan="2">(c) x</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">2.9</td><td>0.011956</td><td>0.0180988</td></tr><tr><td colspan="2">3.0</td><td>0.0049251</td><td>0.00904938</td></tr><tr><td colspan="2">3.1</td><td>0.0004765</td><td>0.00493920</td></tr><tr><td colspan="2">3.2</td><td>0.0013745</td><td>0.00987840</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2">X</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">2.0</td><td>0.00252235</td><td>0.00410304</td></tr><tr><td colspan="2">2.1</td><td>0.00142882</td><td>0.00205152</td></tr><tr><td colspan="2">2.2</td><td>0.00204851</td><td>0.00260034</td></tr><tr><td colspan="2">2.3</td><td>0.00437954</td><td>0.00520068</td></tr></table>

8. The errors and error bounds are given in the following tables.

<table><tr><td colspan="3">(a) Error Bound</td></tr><tr><td colspan="3">x Actual Error</td></tr><tr><td></td><td></td><td></td></tr><tr><td>- 0.3</td><td>0.028638</td><td>0.029692</td></tr><tr><td>-0.2</td><td>0.014097</td><td>0.014846</td></tr><tr><td>-0.1</td><td>0.013577</td><td>0.014130</td></tr><tr><td>0.0</td><td>0.026900</td><td>0.028260</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>7.4</td><td></td><td>0.000032</td></tr><tr><td>7.6</td><td>0.000367 0.000083</td><td>0.000016</td></tr><tr><td>7.8</td><td>0.000041</td><td>0.000015</td></tr><tr><td></td><td></td><td></td></tr><tr><td>8.0</td><td>0.000000</td><td>0.000030</td></tr></table>

<table><tr><td rowspan="3">(c)</td><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.1</td><td>0.033886</td><td>0.034784</td></tr><tr><td>1.2</td><td></td><td>0.016791</td><td>0.017392</td></tr><tr><td></td><td>1.3</td><td>0.015740</td><td>0.016817</td></tr><tr><td></td><td>1.4</td><td>0.030920</td><td>0.033633</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td rowspan="5"></td><td>-2.7</td><td>0.511122</td><td>1.440958</td></tr><tr><td>-2.5</td><td>0.435980</td><td>0.720479</td></tr><tr><td>-2.3</td><td>0.632733</td><td>0.720479</td></tr><tr><td>-2.1</td><td>1.044472</td><td></td></tr><tr><td></td><td></td><td>1.440958</td></tr></table>

9. The approximations and the formulas used are:

(a) $f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 9 9 3 4 4$ from (4.7) $f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 7 6 8 7 6$ from (4.7) $f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 7 0 4$ from (4.6) $f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 7 7 5 6$ from (4.6) $f ^ { \prime } ( 2 . 5 ) \approx 1 . 5 4 4 2 1 0$ from (4.7) $f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 5 5 4 9 6$ from (4.7)

(b) $f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 7 7 3 5 8$ from (4.7) $f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 8 9 3 3$ from (4.7) $f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 8 8 4$ from (4.6) $f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 2 2 3$ from (4.6) $f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 3 9 9 1 1$ from (4.7) $f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 2 8 8 5 3$ from (4.7)

10. The approximations are in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.05</td><td>-1.709847</td><td>7.798690</td></tr><tr><td>1.10</td><td>-1.373823</td><td>5.753747</td></tr><tr><td>1.15</td><td>-1.119214</td><td>4.499409</td></tr><tr><td>1.20</td><td>-0.9160143</td><td>3.675512</td></tr><tr><td>1.25</td><td>-0.7470223</td><td>3.088414</td></tr><tr><td>1.30</td><td>-0.6015966</td><td>2.710997</td></tr></table>

<table><tr><td rowspan="15"></td><td></td><td></td><td></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>-3.0</td><td>16.08554</td><td>-19.08087</td></tr><tr><td>-2.8</td><td>12.64465</td><td>-15.44088</td></tr><tr><td>-2.6</td><td>9.863738</td><td>-12.46303</td></tr><tr><td>-2.4</td><td>7.623176</td><td>-10.02259</td></tr><tr><td>-2.2</td><td>5.825013</td><td>-8.02097</td></tr><tr><td>-2.0</td><td>4.389056</td><td>-6.38573</td></tr></table>

11. The approximations are in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>2.1</td><td>0.0242312</td><td>0.109271</td></tr><tr><td>2.2</td><td>0.0105138</td><td>0.0386885</td></tr><tr><td>2.3</td><td>0.0029352</td><td>0.0182120</td></tr><tr><td>2.4</td><td>0.0013262</td><td>0.00644808</td></tr><tr><td>2.5</td><td>0.0138323</td><td>0.109271</td></tr><tr><td>2.6</td><td>0.0064225</td><td>0.0386885</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td></td><td>C</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td></td><td>-3.0</td><td>1.55 × 10-5</td><td>6.33 × 10-7</td></tr><tr><td></td><td>-2.8</td><td>1.32 × 10-5</td><td>6.76 × 10-7</td></tr><tr><td></td><td>-2.6</td><td>7.95 × 10-7</td><td>1.05 × 10-7</td></tr><tr><td></td><td>-2.4</td><td>6.79 × 10-7</td><td>1.13 × 10-7</td></tr><tr><td></td><td>-2.2</td><td>1.28 × 10-5</td><td>6.76 × 10-7</td></tr><tr><td></td><td>-2.0</td><td>7.96 × 10-6</td><td>6.76 ×10-7</td></tr></table>

<table><tr><td rowspan="7">12. (a)</td><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.05</td><td>0.0484600</td><td>0.2185438</td></tr><tr><td>1.10</td><td>0.0210325</td><td>0.0773769</td></tr><tr><td>1.15</td><td>0.0058693</td><td>0.0364240</td></tr><tr><td>1.20</td><td>0.0026524</td><td>0.0128962</td></tr><tr><td>1.25</td><td>0.0276704</td><td>0.2185438</td></tr><tr><td></td><td>1.30</td><td>0.0128401</td><td>0.0773769</td></tr></table>

<table><tr><td colspan="2">C</td><td>Actual Error Error</td><td>Bound</td></tr><tr><td rowspan="7"></td><td></td><td></td><td></td></tr><tr><td>-3.0 -2.8</td><td>0.004666 0.003763</td><td>0.006427 0.005262</td></tr><tr><td>-2.6</td><td>0.000711</td><td>0.001071</td></tr><tr><td>-2.4</td><td>0.000591</td><td>0.000877</td></tr><tr><td>-2.2</td><td>0.004041</td><td>0.006427</td></tr><tr><td>-2.0</td><td>0.003329</td><td>0.005262</td></tr><tr><td></td><td></td><td></td></tr></table>

\*13. $\begin{array} { r } { f ^ { \prime } ( 3 ) \approx \frac { 1 } { 1 2 } [ f ( 1 ) - 8 f ( 2 ) + 8 f ( 4 ) - f ( 5 ) ] = 0 . 2 1 0 6 2 } \end{array}$ , with an error bound given by

$$
\operatorname* { m a x } _ { 1 \leq x \leq 5 } { \frac { | f ^ { ( 5 ) } ( x ) | h ^ { 4 } } { 3 0 } } \leq { \frac { 2 3 } { 3 0 } } = 0 . 7 { \overline { { 6 } } } .
$$

14. $\begin{array} { r } { f ^ { \prime } ( 3 ) \approx \frac { 1 } { 2 } [ f ( 4 ) - f ( 2 ) ] = 0 . 2 1 2 1 0 } \end{array}$ , with an error bound given by

$$
\operatorname* { m a x } _ { 1 \leq x \leq 5 } { \frac { | f ^ { \prime \prime \prime } ( x ) | h ^ { 2 } } { 6 } } \leq { \frac { 4 } { 2 } } = 0 . 6 { \overline { { 6 } } } .
$$

15. From the forward-backward difference formula (4.1), we have the following approximations:

$$
\begin{array} { r l } & { { { \mathfrak { r } } } ^ { \prime } ( 0 . 5 ) \approx 0 . 8 5 2 , { \{ } ^ { \prime } } ( 0 . 6 ) \approx 0 . 8 5 2 , { \{ } ^ { \prime }  ( 0 . 7 ) \approx 0 . 7 9 6 0  \\ & { { { \mathfrak { r } } } ^ { \prime } ( 0 . 0 ) \approx 3 . 7 0 7 , { \{ } ^ { \prime } } ( 0 . 2 ) \approx 3 . 1 5 3 , { \ f } ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 3  \end{array}
$$

16. For the endpoints of the tables, we use Formula (4.7). The other approximations come from Formula (4.6).

$$
\begin{array} { r l } & { f ^ { \prime } ( 1 . 1 ) \approx 1 7 . 7 5 , f ^ { \prime } ( 1 . 2 ) \approx 2 2 . 1 7 , f ^ { \prime } ( 1 . 3 ) \approx 2 7 . 1 0 , f ^ { \prime } ( 1 . 4 ) \approx 3 2 . 5 0 , } \\ & { f ^ { \prime } ( 8 . 1 ) \approx 3 . 0 7 5 , f ^ { \prime } ( 8 . 3 ) \approx 3 . 1 2 5 , f ^ { \prime } ( 8 . 5 ) \approx 3 . 1 5 0 , f ^ { \prime } ( 8 . 7 ) \approx 3 . 1 5 0 , } \\ & { f ^ { \prime } ( 2 . 9 ) \approx 5 . 0 8 0 , f ^ { \prime } ( 3 . 0 ) \approx 6 . 6 5 5 , f ^ { \prime } ( 3 . 1 ) \approx 8 . 2 2 0 , f ^ { \prime } ( 3 . 2 ) \approx 9 . 7 6 0 , } \\ & { f ^ { \prime } ( 2 . 0 ) \approx 0 . 1 6 0 0 , f ^ { \prime } ( 2 . 1 ) \approx - 0 . 1 0 0 0 , f ^ { \prime } ( 2 . 2 ) \approx - 0 . 3 3 0 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 5 5 0 0 , } \end{array}
$$

17. For the endpoints of the tables, we use Formula (4.7). The other approximations come from Formula (4.6).

$$
\begin{array} { r l } & { f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 8 4 \quad f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 9 6 \quad f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 \quad f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 6 \quad f ^ { \prime } ( 2 . 5 ) \approx 1 . 5 5 0 } \\ & { f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 4 8 } \\ & { f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 8 3 \quad f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 7 \quad f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 \quad f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 } \\ & { f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 0 8 \quad f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 7 5 } \end{array}
$$

18. (a)

<table><tr><td></td><td>f&#x27;(0.4)</td><td>f&quot;(0.4)</td></tr><tr><td>(4.1)</td><td>h =0.6</td><td>-0.8889958 (4.8) h= 0.2 -1.191050</td></tr><tr><td></td><td>h= 0.4</td><td>-0.6979043</td></tr><tr><td></td><td>h= 0.2</td><td>-0.5486810</td></tr><tr><td></td><td>h=-0.2</td><td>-0.3104710</td></tr><tr><td>(4.4)</td><td>h = 0.2</td><td>-0.3994578</td></tr><tr><td>(4.5)</td><td>h = 0.2</td><td>-0.4295760</td></tr></table>

<table><tr><td></td><td></td><td>f&#x27;(0.4)</td><td>f&quot;(0.4)</td></tr><tr><td>(4.1)</td><td>h= 0.4</td><td>-1.059153 (4.8)</td><td>h= 0.4 -1.573943</td></tr><tr><td></td><td>h= 0.2</td><td>-0.8471275</td><td>h= 0.2 -1.492233</td></tr><tr><td></td><td>h=-0.2</td><td>-0.5486810</td><td></td></tr><tr><td></td><td>h = -0.4</td><td>-0.4295760</td><td></td></tr><tr><td>(4.4)</td><td>h= 0.2</td><td>-0.6351018</td><td></td></tr><tr><td></td><td>h=-0.2</td><td>-0.6677860</td><td></td></tr><tr><td>(4.5)</td><td>h= 0.4</td><td>-0.7443646</td><td></td></tr><tr><td></td><td>h= 0.2</td><td>-0.6979043</td><td></td></tr><tr><td>(4.6)</td><td>h= 0.2</td><td>-0.6824175</td><td></td></tr></table>

19. The approximation is $- 4 . 8 \times 1 0 ^ { - 9 }$ . $f ^ { \prime \prime } ( 0 . 5 ) = 0$ . The error bound is 0.35874. The method is very accurate since the function is symmetric about $x = 0 . 5$ .

20. With $h = 0 . 1$ , we have 36.641, and with $h = 0 . 0 1$ , we have 36.5. The actual value is 36.5935.

21. (a) $f ^ { \prime } ( 0 . 2 ) \approx - 0 . 1 9 5 1 0 2 7 \qquad \mathrm { ( b ) } f ^ { \prime } ( 1 . 0 ) \approx - 1 . 5 4 1 4 1 5 \qquad \mathrm { ( c ) } f ^ { \prime } ( 0 . 6 ) \approx - 0 . 6 8 2 4 1 7 5 \qquad \mathrm { ( b ) }$

$^ { * } 2 2$ . We have the Taylor expansions:

$$
\begin{array} { c } { { \displaystyle f ( x _ { 0 } - h ) = f ( x _ { 0 } ) - h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) - \displaystyle \frac { 1 } { 6 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + h ) = f ( x _ { 0 } ) + h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 6 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + 2 h ) = f ( x _ { 0 } ) + 2 h f ^ { \prime } ( x _ { 0 } ) + 2 h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 4 } { 3 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 } { 3 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + 3 h ) = f ( x _ { 0 } ) + 3 h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 9 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 9 } { 2 } h ^ { 3 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 7 } { 8 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) . } } \end{array}
$$

Thus,

$$
\begin{array} { l } { { A f ( x _ { 0 } - h ) + B f ( x _ { 0 } + h ) + C f ( x _ { 0 } + 2 h ) + D f ( x _ { 0 } + 3 h ) = } } \\ { { \qquad f ( x _ { 0 } ) ( A + B + C + D ) + f ^ { \prime } ( x _ { 0 } ) h [ - A + B + 2 C + 3 D ] + f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } \left( \frac { 1 } { 2 } A + \frac { 1 } { 2 } B + 2 C + \frac { 1 } { 2 } B + 2 C \right) + } } \\ { { \qquad + f ^ { \prime \prime \prime } ( x _ { 0 } ) h ^ { 3 } \left( - \frac { 1 } { 6 } A + \frac { 1 } { 6 } B + \frac { 4 } { 3 } C + \frac { 9 } { 2 } D \right) + f ^ { ( 4 ) } ( x _ { 0 } ) h ^ { 4 } \left( \frac { 1 } { 2 4 } A + \frac { 1 } { 2 4 } B + \frac { 2 } { 3 } C + \frac { 2 7 } { 8 } D \right) . } } \end{array}
$$

We want to eliminate the terms involving $f ^ { \prime \prime } ( x _ { 0 } )$ , $f ^ { \prime \prime \prime } ( x _ { 0 } )$ , and $f ^ { ( 4 ) } ( x _ { 0 } )$ and have the coefficient

of $f ^ { \prime } ( x _ { 0 } )$ equal 1. Thus,

$$
\begin{array} { c } { - A + B + 2 C + 3 D = 1 } \\ { \displaystyle \frac { 1 } { 2 } A + \frac { 1 } { 2 } B + 2 C + \frac { 9 } { 2 } D = 0 } \\ { - \frac { 1 } { 6 } A + \frac { 1 } { 6 } B + \frac { 4 } { 3 } C + \frac { 9 } { 2 } D = 0 } \\ { \displaystyle \frac { 1 } { 2 4 } A + \frac { 1 } { 2 4 } B + \frac { 2 } { 3 } C + \frac { 2 7 } { 8 } D = 0 . } \end{array}
$$

The solution to this linear system is

$$
A = - { \frac { 1 } { 4 } } , \quad B = { \frac { 3 } { 2 } } , \quad C = - { \frac { 1 } { 2 } } , \quad \mathrm { a n d } \quad D = { \frac { 1 } { 1 2 } } .
$$

Thus

$$
- { \frac { 1 } { 4 } } f ( x _ { 0 } - h ) + { \frac { 3 } { 2 } } f ( x _ { 0 } + h ) - { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) + { \frac { 1 } { 1 2 } } f ( x _ { 0 } + 3 h ) = f ( x _ { 0 } ) \left( - { \frac { 1 } { 4 } } + { \frac { 3 } { 2 } } - { \frac { 1 } { 2 } } + { \frac { 1 } { 1 2 } } \right) + h f ^ { \prime } ( x _ { 0 } ) + { \frac { 3 } { 4 } } f ( x _ { 0 } - 2 h ) + h f ^ { \prime } ( x _ { 0 } )
$$

Solving for $f ^ { \prime } ( x _ { 0 } )$ gives

$$
f ^ { \prime } ( x _ { 0 } ) = - { \frac { 1 } { h } } \left[ f ( x _ { 0 } ) { \frac { 1 0 } { 1 2 } } + { \frac { 1 } { 4 } } f ( x _ { 0 } - h ) - { \frac { 3 } { 2 } } f ( x _ { 0 } + h ) + { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) - { \frac { 1 } { 1 2 } } f ( x _ { 0 } + 3 h ) \right] + O \left( h ^ { 4 } \right) .
$$

Finally,

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } \left[ - 3 f ( x _ { 0 } - h ) - 1 0 f ( x _ { 0 } ) + 1 8 f ( x _ { 0 } + h ) - 6 f ( x _ { 0 } + 2 h ) + f ( x _ { 0 } + 3 h ) \right] + O \left( h ^ { 4 } \right) .
$$

23. $f ^ { \prime } ( 0 . 4 ) \approx - 0 . 4 2 4 9 8 4 0$ and $f ^ { \prime } ( 0 . 8 ) \approx - 1 . 0 3 2 7 7 2$ .

$^ { * } 2 4$ . (a) Assume that the computed values ${ \ddot { f } } ( x _ { 0 } + h )$ and $\ddot { f } ( x _ { 0 } )$ are related to the true values $f ( x _ { 0 } + h )$ and $f ( x _ { 0 } )$ by the formulas $f ( x _ { 0 } + h ) = f ( x _ { 0 } + h ) + e ( x _ { 0 } + h )$ and $f ( x _ { 0 } ) =$ $f ( x _ { 0 } ) + e ( x _ { 0 } )$ . The total error in the approximation becomes

$$
f ^ { \prime } ( x _ { 0 } ) - { \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } ) } { h } } = { \frac { e ( x _ { 0 } + h ) - e ( x _ { 0 } ) } { h } } - { \frac { h } { 2 } } f ^ { \prime \prime } ( \xi _ { 0 } ) .
$$

If $| e ( x _ { 0 } + h ) | < \varepsilon$ , $| e ( x _ { 0 } ) | < \varepsilon$ , and $| f ^ { \prime \prime } ( \xi _ { 0 } ) | \le M$ , then

$$
\left| f ^ { \prime } ( x _ { 0 } ) - \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } ) } { h } \right| \leq \frac { 2 \varepsilon } { h } + \frac { h M } { 2 } .
$$

(b) The function in Example 2 is

$$
f ( x ) = x e ^ { x } , \quad { \mathrm { f o r } } \quad 1 . 8 \leq x \leq 2 . 2 .
$$

We have $f ^ { \prime } ( x ) = x e ^ { x } + e ^ { x }$ and $f ^ { \prime \prime } ( x ) = x e ^ { x } + 2 e ^ { x }$ . Thus,

$$
M = \operatorname* { m a x } _ { 1 . 8 \leq x \leq 2 . 2 } | f ^ { \prime \prime } ( x ) | = f ^ { \prime \prime } ( 2 . 2 ) = 3 7 . 9 0 5 0 5 6 7 .
$$

The numbers in the table are given to 6 decimal places, so it is reasonable to let $\varepsilon =$ 0.0000005. The optimal value of $h$ is

$$
h = 2 { \sqrt { \frac { \varepsilon } { M } } } = 2 { \sqrt { \frac { 0 . 0 0 0 0 0 0 5 } { 3 7 . 9 0 5 0 5 6 7 } } } = 0 . 0 0 0 2 2 9 7 0 3 .
$$

25. The three-point formulas give the results in the following table.

<table><tr><td>Time</td><td>0</td><td>3</td><td>5</td><td>8</td><td>10</td><td>13</td></tr><tr><td>Speed</td><td>79</td><td>82.4</td><td>74.2</td><td>76.8</td><td>69.4</td><td>71.2</td></tr></table>

26. The three-point formulas give the results in the following table.

<table><tr><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.01</td><td rowspan=1 colspan=1>1.02</td><td rowspan=1 colspan=1>1.03</td><td rowspan=1 colspan=1>1.04</td></tr><tr><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>2.400</td><td rowspan=1 colspan=1>2.403</td><td rowspan=1 colspan=1>3.386</td><td rowspan=1 colspan=1>5.352</td><td rowspan=1 colspan=1>7.320</td></tr></table>

$^ { * } 2 7$ . The approximations eventually become zero since the numerator becomes zero.

28. By averaging the Taylor polynomials we have

$$
f ^ { \prime \prime \prime } ( x _ { 0 } ) = { \frac { 1 } { h ^ { 3 } } } \bigg [ - { \frac { 1 } { 2 } } f ( x _ { 0 } - 2 h ) + f ( x _ { 0 } - h ) - f ( x _ { 0 } + h ) + { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) \bigg ] - { \frac { h ^ { 2 } } { 4 } } f ^ { ( 5 ) } ( \xi ) ,
$$

where $\xi$ is between $x _ { 0 } - 2 h$ and $x _ { 0 } + 2 h$ .

$^ { * } 2 9$ . Since $e ^ { \prime } ( h ) = - \varepsilon / h ^ { 2 } + h M / 3$ , we have $e ^ { \prime } ( h ) = 0$ if and only if $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ . Also, $e ^ { \prime } ( h ) < 0$ if $h < \sqrt [ 3 ] { 3 \varepsilon / M }$ and $e ^ { \prime } ( h ) > 0$ if $h > \sqrt [ 3 ] { 3 \varepsilon / M }$ , so an absolute minimum for $e ( h )$ occurs at $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ .

# Exercise Set 4.2, page 191

1. \*(a) $f ^ { \prime } ( 1 ) \approx 1 . 0 0 0 0 1 0 9$ (b) $f ^ { \prime } ( 0 ) \approx 2 . 0 0 0 0 0 0 0$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 7 5 1 4 5 9$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 4 6 7 9 9$

2. (a) $f ^ { \prime } ( 1 ) \approx 0 . 9 9 9 9 9 9 9 9 8$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 9 9 9 9 9 9$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 7 5 1 4 5 8$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 4 6 7 9 6$

3. (a) $f ^ { \prime } ( 1 ) \approx 1 . 0 0 1$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 9$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 8 3$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 1$

4. (a) $f ^ { \prime } ( 1 ) \approx 0 . 9 9 9 9$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 7$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 8 2$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 6$ $^ { * } 5$ . $\int _ { 0 } ^ { \pi } \sin x \ d x \approx 1 . 9 9 9 9 9 9$

6. $\int _ { 0 } ^ { 3 \pi / 2 } \cos { x } ~ d x \approx - 1 . 0 0 0 1 3 5$

7. With $h = 0 . 1$ , Formula (4.6) becomes

$$
f ^ { \prime } ( 2 ) \approx { \frac { 1 } { 1 . 2 } } \left[ 1 . 8 e ^ { 1 . 8 } - 8 \left( 1 . 9 e ^ { 1 . 9 } \right) + 8 ( 2 . 1 ) e ^ { 2 . 1 } - 2 . 2 e ^ { 2 \cdot 2 } \right] = 2 2 . 1 6 6 9 9 5 .
$$

With $h = 0 . 0 5$ , Formula (4.6) becomes

$$
f ^ { \prime } ( 2 ) \approx { \frac { 1 } { 0 . 6 } } \left[ 1 . 9 e ^ { 1 . 9 } - 8 \left( 1 . 9 5 e ^ { 1 . 9 5 } \right) + 8 ( 2 . 0 5 ) e ^ { 2 . 0 5 } - 2 . 1 e ^ { 2 . 1 } \right] = 2 2 . 1 6 7 1 5 7 .
$$

8. The formula $\begin{array} { r } { f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } \left[ f ( x _ { 0 } + 4 h ) - 1 2 f ( x _ { 0 } + 2 h ) + 3 2 f ( x _ { 0 } + h ) - 2 1 f ( x _ { 0 } ) \right] } \end{array}$ is $O \left( h ^ { 3 } \right)$

9. Let

$$
N _ { 2 } ( h ) = N \left( \frac { h } { 3 } \right) + \left( \frac { N \left( \frac { h } { 3 } \right) - N ( h ) } { 2 } \right) \quad \mathrm { a n d } \quad N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 3 } \right) + \left( \frac { N _ { 2 } \left( \frac { h } { 3 } \right) - N _ { 2 } ( h ) } { 8 } \right) .
$$

Then $N _ { 3 } ( h )$ is an $O ( h ^ { 3 } )$ approximation to $M$ .

10. Let $\begin{array} { r } { N _ { 2 } ( h ) = N \left( \frac { h } { 3 } \right) + \frac { 1 } { 8 } \left( N \left( \frac { h } { 3 } \right) - N ( h ) \right) } \end{array}$ and $\begin{array} { r } { N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 3 } \right) + \frac { 1 } { 8 0 } \left( N _ { 2 } \left( \frac { h } { 3 } \right) - N _ { 2 } ( h ) \right) } \end{array}$ . Then $N _ { 3 } ( h )$ is an $O \left( h ^ { 6 } \right)$ approximation to $M$ .

11. Let $N ( h ) = ( 1 + h ) ^ { 1 / h }$ , $\begin{array} { r } { N _ { 2 } ( h ) = 2 N \left( \frac { h } { 2 } \right) - N ( h ) , N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 3 } ( N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) ) . } \end{array}$

(a) $N ( 0 . 0 4 ) = 2 . 6 6 5 8 3 6 3 3 1$ , $N ( 0 . 0 2 ) = 2 . 6 9 1 5 8 8 0 2 9$ , $N ( 0 . 0 1 ) = 2 . 7 0 4 8 1 3 8 2 9$   
(b) N2(0.04) = 2.717339727, $N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 0 3 9 6 2 \Omega$ . The $O ( h ^ { 3 } )$ approximation is $N _ { 3 } ( 0 . 0 4 ) =$ 2.718272931.   
(c) Yes, since the errors seem proportioned to $h$ for $N ( h )$ , to $h ^ { 2 }$ for $N _ { 2 } ( h )$ , and to $h ^ { 3 }$ for $N _ { 3 } ( h )$ .

$^ { * } 1 2$ . (a) We have

$$
\operatorname* { l i m } _ { h \to 0 } { \frac { \ln ( 2 + h ) - \ln ( 2 - h ) } { h } } = \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { 2 + h } } + { \frac { 1 } { 2 - h } } = 1 ,
$$

so

$$
\operatorname* { l i m } _ { h \to 0 } \left( { \frac { 2 + h } { 2 - h } } \right) ^ { 1 / h } = \operatorname* { l i m } _ { h \to 0 } e ^ { { \frac { 1 } { h } } [ \ln ( 2 + h ) - \ln ( 2 - h ) ] } = e ^ { 1 } = e .
$$

(b) $N ( 0 . 0 4 ) = 2 . 7 1 8 6 4 4 3 7 7 2 2 1 2 1 9$ , $N ( 0 . 0 2 ) = 2 . 7 1 8 3 7 2 4 4 4 8 0 0 6 0 7$ , $N ( 0 . 0 1 ) = 2 . 7 1 8 3 0 4 4 8 1 2 4 1 6 8 5$   
(c) Let $\begin{array} { r } { N _ { 2 } ( h ) = 2 N \left( \frac { h } { 2 } \right) - N ( h ) } \end{array}$ and $\begin{array} { r } { N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 3 } \left[ N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) \right] } \end{array}$ . Then $N _ { 2 } ( 0 . 0 4 ) =$ 2.718100512379995, $N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 2 3 6 5 1 7 6 8 2 7 6 3$ and $N _ { 3 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 5 2 7 8 3 6 8 5$ . $N _ { 3 } ( 0 . 0 4 )$ is an $O \left( h ^ { 3 } \right)$ approximation satisfying $| e - N _ { 3 } ( 0 . 0 4 ) | \le 0 . 5 \times 1 0 ^ { - 7 }$ .

$$
N ( - h ) = \left( { \frac { 2 - h } { 2 + h } } \right) ^ { 1 / - h } = \left( { \frac { 2 + h } { 2 - h } } \right) ^ { 1 / h } = N ( h )
$$

(e) Let

$$
e = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot .
$$

Replacing $h$ by $- h$ gives

$$
e = N ( - h ) - K _ { 1 } h + K _ { 2 } h ^ { 2 } - K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot ,
$$

but $N ( - h ) = N ( h )$ , so that

$$
e = N ( h ) - K _ { 1 } h + K _ { 2 } h ^ { 2 } - K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot .
$$

Thus,

$$
K _ { 1 } h + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot = - K _ { 1 } h - K _ { 3 } h ^ { 3 } \cdot \cdot \cdot ,
$$

and it follows that $K _ { 1 } = K _ { 3 } = K _ { 5 } = \cdot \cdot \cdot = 0$ and

$$
e = N ( h ) + K _ { 2 } h ^ { 2 } + K _ { 4 } h ^ { 4 } + \cdot \cdot \cdot .
$$

(f) Let

$$
N _ { 2 } ( h ) = N \left( { \frac { h } { 2 } } \right) + { \frac { 1 } { 3 } } \left( N \left( { \frac { h } { 2 } } \right) - N ( h ) \right)
$$

and

$$
N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 1 5 } \left( N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) \right) .
$$

Then

$$
N _ { 2 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 0 0 6 6 0 4 0 2 , N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 2 8 1 8 2 6 7 2 2 0 4 3
$$

and

$$
N _ { 3 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 2 8 4 5 9 4 8 7 .
$$

$N _ { 3 } ( 0 . 0 4 )$ is an $O \left( h ^ { 6 } \right)$ approximation satisfying

$$
| e - N _ { 3 } ( 0 . 0 4 ) | \leq 0 . 5 \times 1 0 ^ { - 1 2 } .
$$

\*13. (a) We have

$$
P _ { 0 , 1 } ( x ) = { \frac { \left( x - h ^ { 2 } \right) N _ { 1 } \left( { \frac { h } { 2 } } \right) } { { \frac { h ^ { 2 } } { 4 } } - h ^ { 2 } } } + { \frac { \left( x - { \frac { h ^ { 2 } } { 4 } } \right) N _ { 1 } ( h ) } { h ^ { 2 } - { \frac { h ^ { 2 } } { 4 } } } } , \quad \mathrm { s o } \quad P _ { 0 , 1 } ( 0 ) = { \frac { 4 N _ { 1 } \left( { \frac { h } { 2 } } \right) - N _ { 1 } ( h ) } { 3 } } .
$$

Similarly,

$$
P _ { 1 , 2 } ( 0 ) = \frac { 4 N _ { 1 } \left( \frac { h } { 4 } \right) - N _ { 1 } \left( \frac { h } { 2 } \right) } { 3 } .
$$

(b) We have

$$
P _ { 0 , 2 } ( x ) = { \frac { \left( x - h ^ { 4 } \right) N _ { 2 } \left( { \frac { h } { 2 } } \right) } { { \frac { h ^ { 4 } } { 1 6 } } - h ^ { 4 } } } + { \frac { \left( x - { \frac { h ^ { 4 } } { 1 6 } } \right) N _ { 2 } ( h ) } { h ^ { 4 } - { \frac { h ^ { 4 } } { 1 6 } } } } , \quad { \mathrm { ~ s o ~ } } \quad P _ { 0 , 2 } ( 0 ) = { \frac { 1 6 N _ { 2 } \left( { \frac { h } { 2 } } \right) - N _ { 2 } ( h ) } { 1 5 } } .
$$

14. All the approximations of the form $N _ { 2 i } \left( h / 2 ^ { j } \right)$ , for $i = 1 , 2 , \dots$ and $j = 0 , 1 , 2 , . . .$ , will be upper bounds for $M$ , and all the approximations of the form $N _ { 2 i + 1 } \left( { \frac { h } { 2 ^ { j } } } \right)$ , for $i = 0 , 1 , 2 , \ldots$ and $j = 0 , 1 , 2 , \ldots$ , will be lower bounds for $M$ .

15. (a) We have

$$
p _ { 4 } = 4 \sin \left( { \frac { \pi } { 4 } } \right) = 4 { \frac { \sqrt { 2 } } { 2 } } = 2 { \sqrt { 2 } } \quad { \mathrm { a n d } } \quad P _ { 4 } = 4 \tan \left( { \frac { \pi } { 4 } } \right) = 4 \cdot 1 = 4 .
$$

(b) We have

$$
{ \frac { 2 p _ { k } P _ { k } } { p _ { k } + P _ { k } } } = { \frac { 2 k \sin \left( { \frac { \pi } { k } } \right) \cdot k \tan \left( { \frac { \pi } { k } } \right) } { k \sin \left( { \frac { \pi } { k } } \right) + \tan \left( { \frac { \pi } { k } } \right) } } = { \frac { 2 k ^ { 2 } \left( \sin \left( { \frac { \pi } { k } } \right) \right) ^ { 2 } } { k \sin \left( { \frac { \pi } { k } } \right) \left( 1 + \cos \left( { \frac { \pi } { k } } \right) \right) } } = { \frac { 2 k \sin \left( { \frac { \pi } { k } } \right) } { 1 + \cos \left( { \frac { \pi } { k } } \right) } }
$$

and

$$
\begin{array} { l } { P _ { 2 k } = 2 k \tan \left( \frac { \pi } { 2 k } \right) = 2 k \frac { \sin \left( \frac { \pi } { 2 k } \right) } { \cos \left( \frac { \pi } { 2 k } \right) } = 2 k \sqrt { \frac { 1 - \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } } \\ { = 2 k \sqrt { \displaystyle \frac { 1 - \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } \cdot \sqrt { \frac { 1 + \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } = 2 k \frac { \sqrt { 1 - \left( \cos \left( \frac { \pi } { k } \right) \right) ^ { 2 } } } { 1 + \cos \left( \frac { \pi } { k } \right) } = \frac { 2 k \sin \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } . } \end{array}
$$

In addition,

$$
\begin{array} { c } { { \sqrt { p _ { k } P _ { 2 k } } = \sqrt { k \sin \left( \displaystyle \frac { \pi } { k } \right) \cdot 2 k \tan \left( \displaystyle \frac { \pi } { 2 k } \right) } = k \sqrt { \left( 2 \sin \left( \displaystyle \frac { \pi } { 2 k } \right) \cos \left( \displaystyle \frac { \pi } { 2 k } \right) \right) \cdot 2 \left( \displaystyle \frac { \sin \left( \displaystyle \frac { \pi } { 2 k } \right) } { \cos \left( \displaystyle \frac { \pi } { 2 k } \right) } \right) } } } \\ { { = 2 k \sqrt { \left( \sin \left( \displaystyle \frac { \pi } { 2 k } \right) \right) ^ { 2 } } = 2 k \sin \left( \displaystyle \frac { \pi } { 2 k } \right) = p _ { 2 k } . } } \end{array}
$$

\*(c) The polygonal approximations are in the following table.

<table><tr><td>k</td><td>4</td><td>8</td><td>16</td><td>32</td><td>64</td><td>128</td><td>256</td><td>512</td></tr><tr><td>Pk</td><td>2√2</td><td>3.0614675</td><td>3.1214452</td><td>3.1365485</td><td>3.1403312</td><td>3.1412723</td><td>3.1415138</td><td>3.1415729</td></tr><tr><td>Pk</td><td>4</td><td>3.3137085</td><td>3.1825979</td><td>3.1517249</td><td>3.144184</td><td>3.1422236</td><td>3.1417504</td><td>3.1416321</td></tr></table>

\*(d) Values of $p _ { k }$ and $P _ { k }$ are given in the following tables, together with the extrapolation results: For $p _ { k }$ we have :

<table><tr><td>2.8284271</td><td></td><td></td><td></td><td></td></tr><tr><td>3.0614675</td><td>3.1391476</td><td></td><td></td><td></td></tr><tr><td>3.1214452</td><td>3.1414377</td><td>3.1415904</td><td></td><td></td></tr><tr><td>3.1365485</td><td>3.1415829</td><td>3.1415926</td><td>3.1415927</td><td></td></tr><tr><td>3.1403312</td><td>3.1415921</td><td>3.1415927</td><td>3.1415927</td><td>3.1415927</td></tr></table>

For $P _ { k }$ we have :

<table><tr><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td>3.3137085</td><td>3.0849447</td><td></td><td></td><td></td></tr><tr><td>3.1825979</td><td>3.1388943</td><td>3.1424910</td><td></td><td></td></tr><tr><td>3.1517249</td><td>3.1414339</td><td>3.1416032</td><td>3.1415891</td><td></td></tr><tr><td>3.1441184</td><td>3.1415829</td><td>3.1415928</td><td>3.1415926</td><td>3.1415927</td></tr></table>

# Exercise Set 4.3, page 202

1. The Trapezoidal rule gives the following approximations.

(a) 0.265625  
(b) −0.2678571  
\*(c) 0.228074  
(d) 0.1839397  
(e) −0.8666667  
(f) −0.1777643  
(g) 0.2180895  
(h) 4.1432597

2. The Trapezoidal rule gives the following approximations.

(a) 0.4693956405  
(b) 0.08664339760  
(c) −0.03702425262  
(d) 0.2863341726

3. For the approximations in Exercise 1 we have the following.   

<table><tr><td></td><td>Actual error</td><td>Error bound</td></tr><tr><td>(a)</td><td>0.071875</td><td>0.125</td></tr><tr><td>(b)</td><td>7.943 × 10-4</td><td>9.718 × 10-4</td></tr><tr><td>*（c）</td><td>0.0358146</td><td>0.0396972</td></tr><tr><td>(d)</td><td>0.0233369</td><td>0.1666667</td></tr><tr><td>(e)</td><td>0.1326975</td><td>0.5617284</td></tr><tr><td>(f)</td><td>9.443 × 10-4</td><td>1.0707 × 10-3</td></tr><tr><td>(g)</td><td>0.0663431</td><td>0.0807455</td></tr><tr><td>(h)</td><td>1.554631</td><td>2.298827</td></tr></table>

4. For the approximations in Exercise 2 we have the following.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0203171288</td><td>0.02083333333</td></tr><tr><td>(b） 0.03407359031</td><td>0.0625</td></tr><tr><td>0.01664745664 (d) 0.0138202920</td><td>0.02444080544 0.02904245657</td></tr></table>

5. Simpson’s rule gives the following approximations.

(a) 0.1940104  
(b) −0.2670635  
\*(c) 0.1922453  
(d) 0.16240168  
(e) −0.7391053  
(f) −0.1768216  
(g) 0.1513826  
(h) 2.5836964

6. Simpson’s rule gives the following approximations.

(a) 0.4897985467  
(b) 0.05285463857  
(c) −0.02027158961  
(d) 0.2762704525

7. Simpson’s rule gives the following approximations.

<table><tr><td></td><td>Actual error</td><td>Error bound</td></tr><tr><td>(a)</td><td>2.604 ×10-4</td><td>2.6042 × 10-4</td></tr><tr><td>(b)</td><td>7.14 × 10-7</td><td>9.92 ×10-7</td></tr><tr><td>*（c）</td><td>1.406 × 10-5</td><td>2.170 × 10-5</td></tr><tr><td>(d)</td><td>1.7989 × 10-3</td><td>4.1667 × 10-4</td></tr><tr><td>(e)</td><td>5.1361 × 10-3</td><td>0.063280</td></tr><tr><td>(f)</td><td>1.549 × 10-6</td><td>2.095 × 10-6</td></tr><tr><td>(g)</td><td>3.6381 × 10-4</td><td>4.1507 × 10-4</td></tr><tr><td>(h)</td><td>4.9322 × 10-3</td><td>0.1302826</td></tr></table>

8. Simpson’s rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0000857774</td><td>0.0000868056</td></tr><tr><td>(b） 0.00028483128</td><td>0.001215277778</td></tr><tr><td>0.00010520637</td><td>0.0001147849363</td></tr><tr><td>(d） 0.0001565719</td><td>0.0005334208049</td></tr></table>

9. The Midpoint rule gives the following approximations.

(a) 0.1582031  
(b) −0.2666667  
\*(c) 0.1743309  
(d) 0.1516327  
(e) −0.6753247  
(f) −0.1768200  
(g) 0.1180292  
(h) 1.8039148

10. The Midpoint rule gives the following approximations.

(a) 0.5  
(b) 0.03596025906  
(c) −0.01189525810  
(d) 0.2658385924

11. The Midpoint rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0355469</td><td>0.0625</td></tr><tr><td>(b) 3.961 × 10-4</td><td>4.859×10-4</td></tr><tr><td>*（c） 0.0179285</td><td>0.0198486</td></tr><tr><td>(d) 8.9701 × 10-3</td><td>0.0833333</td></tr><tr><td>(e) 0.0564448</td><td>0.2808642</td></tr><tr><td>(f) 4.698×10-4</td><td>5.353 × 10-4</td></tr><tr><td>(g) 0.0337172</td><td>0.0403728</td></tr><tr><td>(h) 0.7847138</td><td>1.1494136</td></tr></table>

12. The Midpoint rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0102872307</td><td>0.01041666667</td></tr><tr><td>(b） 0.01660954823 0.00848153788</td><td>0.03125</td></tr><tr><td>C (d） 0.0066752882</td><td>0.01222040272 0.01452122828</td></tr></table>

\*13. $\begin{array} { r } { f ( 1 ) = \frac { 1 } { 2 } } \end{array}$

14. Simpson’s rule gives the result $\textstyle { \frac { 1 3 } { 3 } }$ .

$^ \mathrm { * } \mathrm { 1 5 }$ . The degree of precision is 3.

16. The degree of precision is 3.

$^ *$ 17. $\begin{array} { r } { c _ { 0 } = \frac { 1 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 1 } = \frac { 4 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$

18. $\begin{array} { r } { c _ { 0 } = \frac { 7 } { 3 } } \end{array}$ , $c _ { 1 } = - \textstyle { \frac { 2 } { 3 } }$ , $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$

$^ { * } 1 9$ . $\begin{array} { r } { c _ { 0 } = \frac { 1 } { 4 } } \end{array}$ , $\begin{array} { r } { c _ { 1 } = \frac { 3 } { 4 } } \end{array}$ , and $\begin{array} { r } { x _ { 1 } = \frac { 2 } { 3 } } \end{array}$ gives the highest degree of precision, which is 2.

20. $\begin{array} { r } { c _ { 1 } = \frac { 1 } { 2 } } \end{array}$ , $x _ { 0 } = 0 . 2 1 1 3 2 4 8 6 5$ and $x _ { 1 } = 0 . 7 8 8 6 7 5 1 3 5$ give the highest degree of precision, 3.

21. The following approximations are obtained from Formula (4.25) through Formula (4.32), respectively.

(a) 0.1024404, 0.1024598, 0.1024598, 0.1024598, 0.1024695, 0.1024663, 0.1024598, and 0.1024598   
(b) 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, and 0.7853982   
(c) 1.497171, 1.477536, 1.477529, 1.477523, 1.467719, 1.470981, 1.477512, and 1.477515   
(d) 4.950000, 2.740909, 2.563393, 2.385700, 1.636364, 1.767857, 2.074893, and 2.116379   
(e) 3.293182, 2.407901, 2.359772, 2.314751, 1.965260, 2.048634, 2.233251, and 2.249001   
(f) 0.5000000, 0.6958004, 0.7126032, 0.7306341, 0.7937005, 0.7834709, 0.7611137, and 0.7593572

22. We have

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td><td></td></tr><tr><td>(4.23)</td><td>(4.24)</td><td>(4.26)</td><td>(4.27)</td><td>(4.29)</td></tr><tr><td>5.43476</td><td>5.03420</td><td>5.03292</td><td>4.83393</td><td>5.03180</td></tr></table>

23. The errors in Exercise 16 are $1 . 6 \times 1 0 ^ { - 6 }$ , $5 . 3 \times 1 0 ^ { - 8 }$ , $- 6 . 7 \times 1 0 ^ { - 7 }$ , $- 7 . 2 \times 1 0 ^ { - 7 }$ , and $- 1 . 3 \times 1 0 ^ { - 6 }$ , respectively.

\*24. For

$$
\begin{array} { l } { f ( x ) = x : a _ { 0 } x _ { 0 } + a _ { 1 } ( x _ { 0 } + h ) + a _ { 2 } ( x _ { 0 } + 2 h ) = 2 x _ { 0 } h + 2 h ^ { 2 } ; } \\ { f ( x ) = x ^ { 2 } : a _ { 0 } x _ { 0 } ^ { 2 } + a _ { 1 } ( x _ { 0 } + h ) ^ { 2 } + a _ { 2 } ( x _ { 0 } + 2 h ) ^ { 2 } = 2 x _ { 0 } ^ { 2 } h + 4 x _ { 0 } h ^ { 2 } + \frac { 8 h ^ { 3 } } { 3 } ; } \\ { f ( x ) = x ^ { 3 } : a _ { 0 } x _ { 0 } ^ { 3 } + a _ { 1 } ( x _ { 0 } + h ) ^ { 3 } + a _ { 2 } ( x _ { 0 } + 2 h ) ^ { 3 } = 2 x _ { 0 } ^ { 3 } h + 6 x _ { 0 } ^ { 2 } h ^ { 2 } + 8 x _ { 0 } h ^ { 3 } + 4 h ^ { 4 } . } \end{array}
$$

Solving this linear system for $a _ { 0 } , \ a _ { 1 }$ , and $a _ { 2 }$ gives $\begin{array} { l } { { a _ { 0 } ~ = ~ \frac { h } { 3 } , a _ { 1 } ~ = ~ \frac { 4 h } { 3 } } } \end{array}$ , and $\begin{array} { l } { { a _ { 2 } ~ = ~ { \frac { h } { 3 } } } } \end{array}$ . Using $f ( x ) = x ^ { 4 }$ gives $f ^ { ( 4 ) } ( \xi ) = 2 4$ , so

$$
\frac { 1 } { 5 } \left( x _ { 2 } ^ { 5 } - x _ { 0 } ^ { 5 } \right) = \frac { h } { 3 } \left( x _ { 0 } ^ { 4 } + 4 x _ { 1 } ^ { 4 } + x _ { 2 } ^ { 4 } \right) + 2 4 k .
$$

Replacing $x _ { 1 }$ with $x _ { 0 } + h$ , $x _ { 2 }$ with $x _ { 0 } + 2 h$ and simplifying gives $k = - h ^ { 5 } / 9 0$

25. If $E ( x ^ { k } ) = 0$ , for all $k = 0 , 1 , \ldots , n$ and $E ( x ^ { n + 1 } ) \neq 0$ , then with $p _ { n + 1 } ( x ) = x ^ { n + 1 }$ , we have a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Let $p ( x ) = a _ { n } x ^ { n } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 }$ b e any polynomial of degree less than or equal to $n$ . Then $E ( p ( x ) ) = a _ { n } E ( x ^ { n } ) + \cdot \cdot \cdot + a _ { 1 } E ( x ) +$ $a _ { 0 } E ( 1 ) = 0$ . Conversely, if $E ( p ( x ) ) = 0$ , for all polynomials of degree less than or equal to $n$ , it follows that $E ( x ^ { k } ) = 0$ , for all $k = 0 , 1 , \ldots , n$ . Let $p _ { n + 1 } ( x ) = a _ { n + 1 } x ^ { n + 1 } + \cdot \cdot \cdot + a _ { 0 }$ be a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Since $a _ { n + 1 } \neq 0$ , we have

$$
x ^ { n + 1 } = { \frac { 1 } { a _ { n + 1 } } } p _ { n + 1 } ( x ) - { \frac { a _ { n } } { a _ { n + 1 } } } x ^ { n } - \cdot \cdot \cdot - { \frac { a _ { 0 } } { a _ { n + 1 } } } .
$$

Then

$$
\begin{array} { r c l } { E ( x ^ { n + 1 } ) } & { = } & { \displaystyle \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) - \frac { a _ { n } } { a _ { n + 1 } } E ( x ^ { n } ) - \cdots - \frac { a _ { 0 } } { a _ { n + 1 } } E ( 1 ) } \\ & & { = } & { \displaystyle \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) \neq 0 . } \end{array}
$$

Thus, the quadrature formula has degree of precision $n$ .

\*26. Using $n = 3$ in Theorem 4.2 gives

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { 3 } a _ { i } f ( x _ { i } ) + \frac { h ^ { 5 } f ^ { ( 4 ) } ( \xi ) } { 2 4 } \int _ { 0 } ^ { 3 } t ( t - 1 ) ( t - 2 ) ( t - 3 ) d t .
$$

Since

$$
\int _ { 0 } ^ { 3 } t ( t - 1 ) ( t - 2 ) ( t - 3 ) d t = - \frac { 9 } { 1 0 } ,
$$

the error term is

$$
- 3 h ^ { 5 } f ^ { ( 4 ) } ( \xi ) / 8 0 .
$$

Also,

$$
a _ { i } = \int _ { x _ { 0 } } ^ { x _ { 3 } } \prod _ { { j = 0 } \atop { j \neq i } } ^ { 3 } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } d x , \mathrm { ~ f o r ~ e a c h ~ } i = 0 , 1 , 2 , 3 .
$$

Using the change of variables $x = x _ { 0 } + t h$ gives

$$
a _ { i } = h \int _ { 0 } ^ { 3 } \prod _ { { j = 0 } \atop { j \ne i } } ^ { 3 } \frac { t - j } { i - j } d t , \mathrm { ~ f o r ~ e a c h ~ } i = 0 , 1 , 2 , 3 .
$$

Evaluating the integrals gives

$$
a _ { 0 } = \frac { 3 h } { 8 } , \quad a _ { 1 } = \frac { 9 h } { 8 } , \quad a _ { 2 } = \frac { 9 h } { 8 } , \quad \mathrm { a n d } \quad a _ { 3 } = \frac { 3 h } { 8 } .
$$

# Exercise Set 4.4, page 210

1. The Composite Trapezoidal rule approximations are:

(a) 0.639900  
(b) 31.3653  
(c) 0.784241  
(d) −6.42872  
(e) −13.5760  
(f) 0.476977  
(g) 0.605498  
(h) 0.970926

2. The Composite Trapezoidal rule approximations and actual values are:   

<table><tr><td>Composite Trapezoidal Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.91193343</td><td>0.92073549</td></tr><tr><td>*(b) 0.09363001</td><td>0.08802039</td></tr><tr><td>（c） -0.66468785</td><td>-0.66293045</td></tr><tr><td>(d) 0.36487225</td><td>0.36423547</td></tr></table>

3. The Composite Simpson’s rule approximations are:

(a) 0.99999998   
(b) 1.9999999   
(c) 2.2751458   
(d) −19.646796

4. We have

<table><tr><td>Composite Simpson&#x27;s Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.92088605</td><td>0.92073549</td></tr><tr><td>*（b） 0.08809221</td><td>0.08802039</td></tr><tr><td>(c） -0.66292308</td><td>-0.66293045</td></tr><tr><td>(d） 0.36423967</td><td>0.36423547</td></tr></table>

5. The Composite Midpoint rule approximations are:

(a) 0.633096  
(b) 11.1568  
(c) 0.786700  
(d) −6.11274  
(e) −14.9985  
(f) 0.478751  
(g) 0.602961  
(h) 0.947868

6. We have

<table><tr><td>Composite Midpoint Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.92862909</td><td>0.92073549</td></tr><tr><td>*(b) 0.08177145</td><td>0.08802039</td></tr><tr><td>（c） -0.66067279</td><td>-0.66293045</td></tr><tr><td>(d） 0.36342511</td><td>0.36423547</td></tr></table>

7. (a) The Composite Trapezoidal rule approximation is 3.15947567. (b) The Composite Simpson’s rule approximation is 3.10933713. (c) The Composite Midpoint rule approximation is 3.00906003.   
\*8. (a) The Composite Trapezoidal rule approximation is 0.4215820. (b) The Composite Simpson’s rule approximation is 0.4227162. (c) The Composite Midpoint rule approximation is 0.4249845.

\*9. $\alpha = 1 . 5$

10. $\operatorname { - 1 } ) = 1 , \ f ( - 0 . 5 ) = 2 , \ f ( 0 ) = 6 , \ f ( 0 . 5 ) = 3 , \ f ( 1 ) = 1$

11. (a) The Composite Trapezoidal rule requires $h < 0 . 0 0 0 9 2 2 2 9 5$ and $n \geq 2 1 6 8$ . (b) The Composite Simpson’s rule requires $h < 0 . 0 3 7 6 5 8$ and $n \geq 5 4$ . (c) The Composite Midpoint rule requires $h < 0 . 0 0 0 6 5 2 1 6$ and $n \geq 3 0 6 6$ .

12. (a) The Composite Trapezoidal rule requires $h < 0 . 0 0 6 9 6 6 9$ and $n \geq 4 5 1$ (b) The Composite Simpson’s rule requires $h < 0 . 1 3 2 7 4 9$ and $n \geq 2 4$ . (c) The Composite Midpoint rule requires $h < 0 . 0 0 4 9 2 6 3$ and $n \geq 6 3 6$ .

13. (a) The Composite Trapezoidal rule requires $h < 0 . 0 4 3 8 2$ and $n \geq 4 6$ . The approximation is 0.405471. (b) The Composite Simpson’s rule requires $h < 0 . 4 4 2 6 7$ and $n \geq 6$ . The approximation is 0.405466. (c) The Composite Midpoint rule requires $h < 0 . 0 3 0 9 8$ and $n \geq 6 4$ . The approximation is 0.405460.

14. (a) The Composite Trapezoidal rule requires $h < 0 . 0 1 0 9 5$ and $n \geq 9 1$ . With $n = 9 1$ , the approximation is 0.6363013. (b) The Composite Simpson’s rule requires $h \ < \ 0 . 1 7 3 2 0 5$ and $n \geq 6$ . With $n = 6$ , the approximation is 0.6362975. (c) The Composite Midpoint rule requires $h < 0 . 0 0 7 7 4 6 0$ and $n > 1 2 8$ . With $n = 1 3 0$ , the approximation is 0.6362875.

15. (a) Because the right and left limits at 0.1 and 0.2 for $f , \ f ^ { \prime }$ , and $f ^ { \prime \prime }$ are the same, the functions are continuous on $[ 0 , 0 . 3 ]$ . However,

$$
f ^ { \prime \prime \prime } ( x ) = { \left\{ \begin{array} { l l } { 6 , } & { 0 \leq x \leq 0 . 1 } \\ { 1 2 , } & { 0 . 1 < x \leq 0 . 2 } \\ { 1 2 , } & { 0 . 2 < x \leq 0 . 3 } \end{array} \right. }
$$

is discontinuous at $x = 0 . 1$

(b) We have 0.302506 with an error bound of $1 . 9 \times 1 0 ^ { - 4 }$ .

(c) We have 0.302425, and the value of the actual integral is the same.

$^ *$ 16. To show that the sum

$$
\sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h
$$

is a Riemann Sum, let $y _ { i } = x _ { 2 i }$ , for $i = 0 , 1 , \ldots { \frac { \pi } { 2 } }$ . Then $\Delta y _ { i } = y _ { i + 1 } - y _ { i } = 2 h$ and $y _ { i - 1 } \leq \xi _ { i } \leq$ $y _ { i }$ . Thus,

$$
\sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) \Delta y _ { j } = \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h
$$

is a Riemann Sum for $\textstyle { \int _ { a } ^ { b } f ^ { ( 4 ) } ( x ) d x }$ . Hence

$$
E ( f ) = - { \frac { h ^ { 5 } } { 9 0 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) = - { \frac { h ^ { 4 } } { 1 8 0 } } { \bigg [ } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h { \bigg ] } \approx - { \frac { h ^ { 4 } } { 1 8 0 } } \int _ { a } ^ { b } f ^ { ( 4 ) } ( x ) d x = - { \frac { h ^ { 4 } } { 1 8 0 } } { \big [ } f ^ { \prime \prime \prime } ( b ) - f ^ { \prime \prime } ( b ) { \big ] }
$$

17. (a) For the Composite Trapezoidal rule, we have

$$
E ( f ) = - { \frac { h ^ { 3 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) h = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j } ,
$$

where $\Delta x _ { j } = x _ { j + 1 } - x _ { j } = h$ for each $j$ . Since $\textstyle \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j }$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ , we have

$$
E ( f ) \approx - { \frac { h ^ { 2 } } { 1 2 } } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

(b) For the Composite Midpoint rule, we have

$$
E ( f ) = { \frac { h ^ { 3 } } { 3 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) = { \frac { h ^ { 2 } } { 6 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h ) .
$$

But $\textstyle \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h )$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ , so

$$
E ( f ) \approx \frac { h ^ { 2 } } { 6 } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

18. (a) Composite Trapezoidal Rule: With $h = 0 . 0 0 6 9 6 6 9$ , the error estimate is $2 . 5 4 1 \times 1 0 ^ { - 5 }$ . (b) Composite Simpson’s Rule: With $h = 0 . 1 3 2 7 4 9$ , the error estimate is $3 . 2 5 2 \times 1 0 ^ { - 5 }$ . (c) Composite Midpoint Rule: With $h = 0 . 0 0 4 9 2 6 3$ , the error estimate is $2 . 5 4 1 \times 1 0 ^ { - 5 }$ .

19. (a) The estimate using the Composite Trapezoidal rule is $- \textstyle { \frac { 1 } { 2 } } h ^ { 2 } \ln 2 = - 6 . 2 9 6 \times 1 0 ^ { - 6 }$ . (b) The estimate using the Composite Simpson’s rule is $- \textstyle { \frac { 1 } { 2 4 0 } } h ^ { 2 } = - 3 . 7 5 \times 1 0 ^ { - 6 }$ . (c) The estimate using the Composite Midpoint rule is $\textstyle { \frac { 1 } { 6 } } h ^ { 2 } \ln 2 = 6 . 9 3 2 \times 1 0 ^ { - 6 }$ .

20. (a) 0.68269822 obtained using $n = 1 0$ in Composite Simpson’s rule. (b) 0.95449101 obtained using $n = 1 4$ in Composite Simpson’s rule. (c) 0.99729312 obtained using $n = 2 0$ in Composite Simpson’s rule.

21. The length is approximately 15.8655.

$^ *$ 22. The length of the track is approximately 9858 ft.

23. Composite Simpson’s rule with $h = 0 . 2 5$ gives 2.61972 s.

24. An approximation for $T$ is 1054.694.

25. The length is approximately 58.47082, using $n = 1 0 0$ in the Composite Simpson’s rule.

$^ *$ 26. (a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 6 } = 1 . 6 4 4 8 5 4$ with $n = 2 0$ in the Composite Simpson’s rule. (b) For $p _ { 0 } = 0 . 5$ , we have $p _ { 6 } = 1 . 6 4 5 0 8 5$ with $n = 4 0$ in the Composite Trapezoidal rule.

# Exercise Set 4.5, page 218

1. Romberg integration gives $R _ { 3 , 3 }$ as follows:

\*(a) 0.1922593  
(b) 0.1606105  
(c) −0.1768200  
(d) 0.08875677  
(e) 2.5879685  
(f) −0.7341567  
(g) 0.6362135  
(h) 0.6426970

2. Romberg integration gives $R _ { 3 , 3 }$ as follows:

(a) 1.45281435   
(b) 0.32795861   
(c) −10.51261013   
(d) 0.52681555

3. Romberg integration gives $R _ { 4 , 4 }$ as follows:

\*(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875528  
(e) 2.5886272  
(f) −0.7339728  
(g) 0.6362134  
(h) 0.6426991

4. Romberg integration gives $R _ { 4 , 4 }$ as follows:

(a) 1.45466031   
(b) 0.32456706   
(c) −10.52012212   
(d) 0.52659385

5. Romberg integration gives:

(a) 0.19225936 with $n = 4$ (b) 0.16060279 with $n = 5$ (c) −0.17682002 with $n = 4$ (d) 0.088755284 with $n = 5$ (e) 2.5886286 with $n = 6$ (f) −0.73396918 with $n = 6$ (g) 0.63621335 with $n = 4$ (h) 0.64269908 with $n = 5$

6. (a) $R _ { 6 , 6 } = 1 . 4 5 4 6 4 8 7 1$ , Actual Integral= 1.454648713 (b) $R _ { 7 , 7 } = 0 . 3 2 4 3 3 2 1 6$ , Actual Integral= 0.3243321549 (c) $R _ { 6 , 6 } = - 1 0 . 5 2 0 0 1 5 2 1$ , Actual Integral= −10.52001520 (d) $R _ { 6 , 6 } = 0 . 5 2 6 5 8 9 0 3$ , Actual Integral= 0.5265890342

7. $R _ { 3 3 } = 1 1 . 5 2 4 6$ \*8. $R _ { 2 1 } = 0 . 2 3 6 1$ \*9. $f ( 2 . 5 ) \approx 0 . 4 3 4 5 7$

10. $f ( 1 / 2 ) = 5 . 5$

11. $R _ { 3 1 } = 5$

12. Romberg integration gives:

(a) 62.4373714, 57.2885616, 56.4437507, 56.2630547, and 56.2187727 yields a prediction of 56.2.   
(b) 55.5722917, 56.2014707, 56.2055989, and 56.2040624 yields a prediction of 56.20.   
(c) 58.3626837, 59.0773207, 59.2688746, 59.3175220, 59.3297316, and 59.3327870 yields a prediction of 59.330.   
(d) 58.4220930, 58.4707174, 58.4704791, and 58.4704691 yields a prediction of 58.47047.   
(e) Consider the graph of the function.

\*13. We have

$$
\begin{array} { r c l } { { R _ { k , 2 } } } & { { = } } & { { \displaystyle \frac { 4 R _ { k , 1 } - R _ { k - 1 , 1 } } { 3 } = \frac { 1 } { 3 } \left[ R _ { k - 1 , 1 } + 2 h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( i - 1 / 2 ) ) h _ { k - 1 } \right] \Bigg \} , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 3 } \bigg [ \frac { h _ { k - 1 } } { 2 } ( f ( a ) + f ( b ) ) + h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } - 1 } f ( a + i h _ { k - 1 } ) + 2 h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( i - 1 / 2 ) h _ { k - 1 } ) \bigg ] , } } \end{array}
$$

Hence

$$
\begin{array} { r c l } { { R _ { k , 2 } } } & { { = } } & { { \displaystyle \frac { 1 } { 3 } \left[ h _ { k } ( f ( a ) + f ( b ) ) + 2 h _ { k } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } - 1 } f ( a + 2 i h _ { k } ) + 4 h _ { k } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( 2 i - 1 ) h ) \right] } } \\ { { } } & { { = } } & { { \displaystyle \frac { h } { 3 } \left[ f ( a ) + f ( b ) + 2 \sum _ { i = 1 } ^ { M - 1 } f ( a + 2 i h ) + 4 \sum _ { i = 1 } ^ { M } f ( a + ( 2 i - 1 ) h ) \right] , } } \end{array}
$$

where $h = h _ { k }$ and $M = 2 ^ { k - 2 }$ .

14. First consider

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { 2 N - 1 } g ( i ) = g ( 1 ) + g ( 2 ) + g ( 3 ) + \cdots + g ( 2 N - 2 ) + g ( 2 N - 1 ) } } \\ { { \displaystyle \qquad = [ g ( 1 ) + g ( 3 ) + \cdots + g ( 2 N - 1 ) ] + [ g ( 2 ) + g ( 4 ) + \cdots + g ( 2 N - 2 ) ] } } \\ { { \displaystyle \qquad = \sum _ { i = 1 } ^ { N } g ( 2 i - 1 ) + \sum _ { i = 1 } ^ { N - 1 } g ( 2 i ) . } } \end{array}
$$

The result follows by setting

$$
g ( i ) = f \bigg ( a + \frac { i } { 2 } h _ { k - 1 } \bigg ) \quad \mathrm { a n d } \quad N = 2 ^ { k - 2 } .
$$

15. Equation (4.34) follows from

$$
\begin{array} { r c l } { { R _ { k , 1 } } } & { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + i \hbar _ { k - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + \frac { i } { 2 } \hbar _ { i - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + i \hbar _ { k - i } ) + 2 \sum _ { i = 1 } ^ { \infty } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { 1 } { 2 } \left\{ \frac { \hbar _ { k - 1 } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 2 } \sum _ { i = 1 } ^ { j - 1 } f ( \alpha + i \hbar _ { k - 1 } ) \right] + \hbar _ { k - 1 } \sum _ { i = 1 } ^ { \infty - 2 } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right\} } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { 1 } { 2 } \left[ \hbar _ { k - 1 , 1 } + \hbar _ { k - 1 } \sum _ { i = 1 } ^ { \infty - 2 } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right] . } } \end{array}
$$

16. The approximation $\mathrm { e r f ( 1 ) } \approx 0 . 8 4 2 7 0 0 7 9$ is obtained using $n = 6$ .

# Exercise Set 4.6, page 227

1. Simpson’s rule gives

\*(a) $S ( 1 , 1 . 5 ) = 0 . 1 9 2 2 4 5 3 0$ , $S ( 1 , 1 . 2 5 ) = 0 . 0 3 9 3 7 2 4 3 4$ , $S ( 1 . 2 5 , 1 . 5 ) = 0 . 1 5 2 8 8 6 0 2$ , and the actual value is 0.19225935.   
(b) $S ( 0 , 1 ) = 0 . 1 6 2 4 0 1 6 8$ , $S ( 0 , 0 . 5 ) = 0 . 0 2 8 8 6 1 0 7 1$ , $S ( 0 . 5 , 1 ) = 0 . 1 3 1 8 6 1 4 0$ , and the actual value is 0.16060279.   
(c) $S ( 0 , 0 . 3 5 ) = - 0 . 1 7 6 8 2 1 5 6$ , $S ( 0 , 0 . 1 7 5 ) = - 0 . 0 8 7 7 2 4 3 8 2$ , $S ( 0 . 1 7 5 , 0 . 3 5 ) = - 0 . 0 8 9 0 9 5 7 3 6$ , and the actual value is $- 0 . 1 7 6 8 2 0 0 2$ .   
(d) $\begin{array} { r } { S ( 0 , \frac { \pi } { 4 } ) = 0 . 0 8 7 9 9 5 6 6 9 } \end{array}$ , $\begin{array} { r } { S ( 0 , \frac { \pi } { 8 } ) = 0 . 0 0 5 8 3 1 5 7 9 7 } \end{array}$ , $\begin{array} { r } { S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 0 . 0 8 2 8 7 7 6 2 4 } \end{array}$ , and the actual value is 0.088755285.   
(e) $\begin{array} { r } { S ( 0 , \frac { \pi } { 4 } ) = 2 . 5 8 3 6 9 6 4 } \end{array}$ , $\begin{array} { r } { S ( 0 , \frac { \pi } { 8 } ) = 0 . 3 3 0 8 8 9 2 6 } \end{array}$ , $\begin{array} { r } { S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 2 . 2 5 6 8 1 2 1 } \end{array}$ , and the actual value is 2.5886286.   
(f) $S ( 1 , 1 . 6 ) = - 0 . 7 3 9 1 0 5 3 3$ , $S ( 1 , 1 . 3 ) = - 0 . 2 6 1 4 1 2 4 4$ , $S ( 1 . 3 , 1 . 6 ) = - 0 . 4 7 3 0 5 3 5 1$ , and the actual value is $- 0 . 7 3 3 9 6 9 1 7$ .   
(g) $S ( 3 , 3 . 5 ) \ : = \ : 0 . 6 3 6 2 3 8 7 3$ , $S ( 3 , 3 . 2 5 ) \ : = \ : 0 . 3 2 5 6 7 0 9 5$ , $S ( 3 . 2 5 , 3 . 5 ) \ : = \ : 0 . 3 1 0 5 4 4 1 2$ , and the actual value is 0.63621334.   
(h) $\begin{array} { c } { { S ( 0 , { \frac { \pi } { 4 } } ) ~ = ~ 0 . 6 4 3 2 6 9 0 5 } } \end{array}$ , $\begin{array} { r } { S ( 0 , { \frac { \pi } { 8 } } ) = 0 . 3 7 3 1 5 0 0 2 } \end{array}$ , $S ( \textstyle { \frac { \pi } { 8 } } , \textstyle { \frac { \pi } { 4 } } ) \ = \ 0 . 2 6 9 5 8 2 7 0$ , and the actual value is 0.64269908.

2. Adaptive quadrature gives:

\*(a) 0.19226  
(b) 0.16072  
(c) −0.17682  
(d) 0.088709  
(e) 2.58770  
(f) −0.73447  
(g) 0.63622  
(h) 0.64273

3. Adaptive quadrature gives:

(a) 108.555281   
(b) 1724.966983   
(c) 15.306308   
(d) −18.945949

4. Adaptive quadrature gives:

<table><tr><td>Adaptive Quadrature Approximation</td><td>Actual Integral</td></tr><tr><td>(@)</td><td>2.00000103</td></tr><tr><td>(b）</td><td>2.00000000 1.37296499</td></tr><tr><td>（c）</td><td>1.372964103 0.23222150</td></tr><tr><td>(d)</td><td>5.113832671</td></tr></table>

5. Adaptive quadrature gives:

<table><tr><td></td><td>Simpson&#x27;s rule</td><td>Number evaluation</td><td>Error</td><td>Adaptive quadrature</td><td>Number evaluation</td><td>Error</td></tr><tr><td>(a)</td><td>-0.21515695</td><td>57</td><td>6.3 ×10-6</td><td>-0.21515062</td><td>229</td><td>1.0 ×10-8</td></tr><tr><td>(b）</td><td>0.95135226</td><td>83</td><td>9.6 ×10-6</td><td>0.95134257</td><td>217</td><td>1.1 × 10-7</td></tr><tr><td>（C）</td><td>-6.2831813</td><td>41</td><td>4.0 × 10-6</td><td>-6.2831852</td><td>109</td><td>1.1 × 10-7</td></tr><tr><td>(d)</td><td>5.8696024</td><td>27</td><td>2.6×10-6</td><td>5.8696044</td><td>109</td><td>4.0 × 10-9</td></tr></table>

\*6. Adaptive quadrature gives

$$
\int _ { 0 . 1 } ^ { 2 } \sin { \frac { 1 } { x } } d x \approx 1 . 1 4 5 4 \quad { \mathrm { a n d } } \quad \int _ { 0 . 1 } ^ { 2 } \cos { \frac { 1 } { x } } d x \approx 0 . 6 7 3 7 8 .
$$

7. $\int _ { 0 } ^ { 2 \pi } u ( t ) ~ d t \approx 0 . 0 0 0 0 1$

8. (a) $c _ { 1 } = - \textstyle { \frac { 1 } { 4 0 } }$ 140 , c 2 = $\begin{array} { r } { c _ { 2 } = \frac { 9 } { 6 8 0 } } \end{array}$ (b) $\int _ { 0 } ^ { 2 \pi } u ( t ) \ d t \approx - 0 . 0 2 3 4 8 1 9 4$

9. We have, for $h = b - a$

$$
\left| T ( a , b ) - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { h ^ { 3 } } { 1 6 } } \left| f ^ { \prime \prime } ( \mu ) \right|
$$

and

$$
\left| \int _ { a } ^ { b } f ( x ) \ d x - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { h ^ { 3 } } { 4 8 } } \left| f ^ { \prime \prime } ( \mu ) \right| .
$$

So

$$
\left| \int _ { a } ^ { b } f ( x ) ~ d x - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { 1 } { 3 } } \left| T ( a , b ) - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| .
$$

10. For $t$ between o and 1 we have the following values.

<table><tr><td>t</td><td>c(t)</td><td>s(t)</td></tr><tr><td>0.1</td><td>0.0999975</td><td>0.000523589</td></tr><tr><td>0.2</td><td>0.199921</td><td>0.00418759</td></tr><tr><td>0.3</td><td>0.299399</td><td>0.0141166</td></tr><tr><td>0.4</td><td>0.397475</td><td>0.0333568</td></tr><tr><td>0.5</td><td>0.492327</td><td>0.0647203</td></tr><tr><td>0.6</td><td>0.581061</td><td>0.110498</td></tr><tr><td>0.7</td><td>0.659650</td><td>0.172129</td></tr><tr><td>0.8</td><td>0.722844</td><td>0.249325</td></tr><tr><td>0.9</td><td>0.764972</td><td>0.339747</td></tr><tr><td>1.0</td><td>0.779880</td><td>0.438245</td></tr></table>

# Exercise Set 4.7, page 234

1. Gaussian quadrature gives:

(a) 0.1922687  
\*(b) 0.1594104  
(c) −0.1768190  
(d) 0.08926302  
(e) 2.5913247  
(f) −0.7307230  
(g) 0.6361966  
(h) 0.6423172

2. Gaussian quadrature with $n = 3$ gives:

(a) 0.1922594  
\*(b) 0.1605954  
(c) −0.1768200  
(d) 0.08875385  
(e) 2.5892580  
(f) −0.7337990  
(g) 0.6362132  
(h) 0.6427011

3. Gaussian quadrature gives:

(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875529  
(e) 2.5886327  
(f) −0.7339604  
(g) 0.6362133  
(h) 0.6426991

4. Gaussian quadrature with $n = 5$ gives:

(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875528  
(e) 2.5886286  
(f) −0.7339687  
(g) 0.6362133  
(h) 0.6426991

\*5. $a = 1$ , $b = 1$ , $c = \frac { 1 } { 3 }$ , $d = - { \frac { 1 } { 3 } }$ 6. $a = { \frac { 7 } { 1 5 } }$ , $b = { \frac { 1 6 } { 1 5 } }$ , $c = \frac { 7 } { 1 5 }$ , $d = \frac { 1 } { 1 5 }$ , e 15 1 $^ { * } 7$ . The Legendre polynomials $P _ { 2 } ( x )$ and $P _ { 3 } ( x )$ are given by

$$
P _ { 2 } ( x ) = \frac { 1 } { 2 } \left( 3 x ^ { 2 } - 1 \right) \quad \mathrm { a n d } \quad P _ { 3 } ( x ) = \frac { 1 } { 2 } \left( 5 x ^ { 3 } - 3 x \right) ,
$$

so their roots are easily verified.

For $n = 2$ ,

$$
c _ { 1 } = \int _ { - 1 } ^ { 1 } { \frac { x + 0 . 5 7 7 3 5 0 2 6 9 2 } { 1 . 1 5 4 7 0 0 5 } } ~ d x = 1
$$

and

$$
c _ { 2 } = \int _ { - 1 } ^ { 1 } { \frac { x - 0 . 5 7 7 3 5 0 2 6 9 2 } { - 1 . 1 5 4 7 0 0 5 } } ~ d x = 1 .
$$

For $n = 3$ ,

$$
c _ { 1 } = \int _ { - 1 } ^ { 1 } { \frac { x ( x + 0 . 7 7 4 5 9 6 6 6 9 2 ) } { 1 . 2 } } ~ d x = { \frac { 5 } { 9 } } ,
$$

$$
c _ { 2 } = \int _ { - 1 } ^ { 1 } { \frac { ( x + 0 . 7 7 4 5 9 6 6 6 9 2 ) ( x - 0 . 7 7 4 5 9 6 6 6 9 2 ) } { - 0 . 6 } } d x = { \frac { 8 } { 9 } } ,
$$

and

$$
c _ { 3 } = \int _ { - 1 } ^ { 1 } { \frac { x ( x - 0 . 7 7 4 5 9 6 6 6 9 2 ) } { 1 . 2 } } ~ d x = { \frac { 5 } { 9 } } .
$$

8. Let $\begin{array} { r } { P ( x ) = \prod _ { i = 1 } ^ { n } ( x - x _ { i } ) ^ { \cdot 2 } } \end{array}$ . Then $Q ( P ) = 0$ and $\textstyle \int _ { - 1 } ^ { 1 } P ( x ) \ d x \neq 0$

$^ { * } 9$ . (a) The approximations and errors using Maple’s routine with

$f : = x ^ { 2 } \cdot e x p ( x ) ; a : = - 1 ; b : = 1$ ; Quadrature(f $' ( x ) , x = a . . b , m e t h o d = g a u s s i a n | n | ,$ partition = p, output = information)

give the following approximations to the exact 10-digit value 0.878884623.

<table><tr><td>n</td><td>p</td><td>Number of Function Evaluations</td><td>Approximation</td><td>Error</td></tr><tr><td>8</td><td>1</td><td>8</td><td>0.878884623</td><td>0.0</td></tr><tr><td>4</td><td>2</td><td>8</td><td>0.878884546</td><td>8×10-8</td></tr><tr><td>2</td><td>8</td><td>8</td><td>0.878387796</td><td>5×10-4</td></tr></table>

(b) Gaussian quadrature chooses the evaluation points in an optimal way for the given interval. If the interval is partitioned it uses then uses points that are not optimal in the Gaussian sense, and less accuracy is to be expected.

# Exercise Set 4.8, page 248

1. Algorithm 4.4 with $n = m = 4$ gives:

(a) 0.3115733   
(b) 0.2552526   
\*(c) 16.50864   
(d) 1.476684

2. Algorithm 4.4 gives:

(a) 0.3115733 with $n = m = 2$ (b) 0.2552526 with $n = m = 4$ (c) 16.50864 with $n = m = 4$ (d) No result since it requires $n , m > 8 0 0$ .

3. Algorithm 4.4 with $n = 4$ and $m = 8$ , $n = 8$ and $m = 4$ , and $n = m = 6$ gives:

(a) 0.5119875, 0.5118533, 0.5118722  
(b) 1.718857, 1.718220, 1.718385  
(c) 1.001953, 1.000122, 1.000386  
(d) 0.7838542, 0.7833659, 0.7834362  
(e) −1.985611, −1.999182, −1.997353  
(f) 2.004596, 2.000879, 2.000980  
(g) 0.3084277, 0.3084562, 0.3084323  
(h) −22.61612, −19.85408, −20.14117

4. Algorithm 4.4 gives:

(a) 0.51184555 with $n = m = 1 4$ (b) 1.7182827 with $n = m = 2 0$ (c) 1.00000081 with $n = m = 2 8$ (d) 0.78333417 with $n = m = 2 0$ (e) −1.99999913 with $n = m = 4 4$ (f) 2.00000092 with $n = m = 3 4$ (g) 0.30842563 with $n = m = 1 2$ (h) −19.73920977 with $n = m = 1 4 4$

5. Algorithm 4.5 with $n = m = 2$ gives:

(a) 0.3115733   
(b) 0.2552446   
\*(c) 16.50863   
(d) 1.488875

6. Algorithm 4.5 gives:

(a) 0.3115733 with $n = m = 2$ and 4 function evaluations (b) 0.2552519 with $n = m = 3$ and 9 function evaluations (c) 16.508640 with $n = m = 3$ and 9 function evaluations (d) no result, since it requires $n , m > 5$

7. Algorithm 4.5 with $n = m = 3$ , $n = 3$ and $m = 4$ , $n = 4$ and $m = 3$ , and $n = m = 4$ gives:

(a) 0.5118655, 0.5118445, 0.5118655, 0.5118445, $2 . 1 \times 1 0 ^ { - 5 }$ , $1 . 3 \times 1 0 ^ { - 7 }$ , $2 . 1 \times 1 0 ^ { - 5 }$ , $1 . 3 \times 1 0 ^ { - 7 }$ (b) 1.718163, 1.718302, 1.718139, 1.718277, $1 . 2 \times 1 0 ^ { - 4 }$ , $2 . 0 \times 1 0 ^ { - 5 }$ , $1 . 4 \times 1 0 ^ { - 4 }$ , $4 . 8 \times 1 0 ^ { - 6 }$ (c) 1.000000, 1.000000, 1.0000000, 1.000000, 0, 0, 0, 0  
(d) 0.7833333, 0.7833333, 0.7833333, 0.7833333, 0, 0, 0, 0  
(e) $- 1 . 9 9 1 8 7 8 , - 2 . 0 0 0 1 2 4 , - 1 . 9 9 1 8 7 8 , - 2 . 0 0 0 1 2 4 , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 } , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 }$ (f) 2. $0 0 1 4 9 4 , 2 . 0 0 0 0 8 0 , 2 . 0 0 1 3 8 8 , 1 . 9 9 9 9 8 4 , 1 . 5 \times 1 0 ^ { - 3 } , 8 \times 1 0 ^ { - 5 } , 1 . 4 \times 1 0 ^ { - 3 } , 1 . 6 \times 1 0 ^ { - 5 }$ (g) 0.3084151, 0.3084145, 0.3084246, 0.3084245, $1 0 ^ { - 5 }$ , $5 . 5 \times 1 0 ^ { - 7 }$ , $1 . 1 \times 1 0 ^ { - 5 }$ , $6 . 4 \times 1 0 ^ { - 7 }$ (h) −12.74790, −21.21539, −11.83624, −20.30373, 7.0, 1.5, 7.9, 0.564

8. Algorithm 4.5 with $n = m = 5$ gives:

(a) 0.51184464, error $3 \times 1 0 ^ { - 1 0 }$ (b) 1.7182816, error $2 . 2 \times 1 0 ^ { - 7 }$ (c) 1.0000000, error 0  
(d) 0.78333333, error 0  
(e) −1.9999989, error $1 . 1 \times 1 0 ^ { - 6 }$ (f) 2.0000001, error $1 . 1 \times 1 0 ^ { - 7 }$ (g) 0.30842509, error $4 . 3 \times 1 0 ^ { - 8 }$ (h) 19.712428, error 0.0268

9. Algorithm 4.4 with $n = m = 1 4$ gives 0.1479103, and Algorithm 4.5 with $n = m = 4$ gives 0.1506823.

\*10. $\begin{array} { r } { \iint _ { R } { \sqrt { x y + y ^ { 2 } } } \ d A \approx 1 3 . 1 5 2 2 9 } \end{array}$

11. The approximation to the center of mass is $( { \overline { { x } } } , { \overline { { y } } } )$ , where $\overline { { x } } = 0 . 3 8 0 6 3 3 3$ and $\overline { { y } } = 0 . 3 8 2 2 5 5 8$ .

12. The approximation from Algorithm 4.5 with $n = m = 5$ is $\overline { { x } } = 0 . 3 8 2 0 5 4 7$ and $\overline { { y } } = 0 . 3 8 1 3 9 7 6$ .

13. The area is approximately 1.0402528.

14. The area approximation from Algorithm 4.5 is 1.0402523.

15. Algorithm 4.6 with $n = m = p = 2$ gives the first listed value. The second is the exact result.

(a) 5.204036, $e ( e ^ { 0 . 5 } - 1 ) ( e - 1 ) ^ { 2 }$ (b) 0.08429784, $\textstyle { \frac { 1 } { 1 2 } }$

(c) 0.08641975, $\textstyle { \frac { 1 } { 1 4 } }$ (d) 0.09722222, $\textstyle { \frac { 1 } { 1 2 } }$ (e) 7.103932, $2 + { \textstyle { \frac { 1 } { 2 } } } \pi ^ { 2 }$ (f) 1.428074, $\begin{array} { r } { \frac { 1 } { 2 } ( e ^ { 2 } + 1 ) - e } \end{array}$

16. Gaussian quadrature with $n = m = p = 3$ gives:

(a) 5.206442   
(b) 0.08333333   
(c) 0.07166667   
(d) 0.08333333   
(e) 6.928161   
(f) 1.474577

17. Algorithm 4.6 with $n = m = p = 4$ gives the first listed value. The second is from Algorithm 4.6 with $n = m = p = 5$ .

(a) 5.206447, 5.206447   
(b) 0.08333333,0.08333333   
(c) 0.07142857,0.07142857   
(d) 0.08333333,0.08333333   
(e) 6.934912,6.934801   
(f) 1.476207, 1.476246

18. Gaussian quadrature with $n = m = p = 4$ gives 3.0521250. The exact result is 3.0521249.

19. The approximation 20.41887 requires 125 functional evaluations.

# Exercise Set 4.9, page 254

1. The Composite Simpson’s rule gives:

\*(a) 0.5284163   
(b) 4.266654   
(c) 0.4329748   
(d) 0.8802210

2. The Composite Simpson’s Rule gives:

(a) 1.076163   
(b) 20.07458

3. The Composite Simpson’s rule gives:

\*(a) 0.4112649  
(b) 0.2440679  
(c) 0.05501681  
(d) 0.2903746

4. The Composite Simpson’s Rule gives:

\*(a) 1.1107218 with $n = 1 6$ (b) 0.58904782 with $n = 1 2$

5. The escape velocity is approximately 6.9450 mi/s.

\*6. The polynomial $L _ { n } ( x )$ has $n$ distinct zeros in $| 0 , \infty )$ . Let $x _ { 1 } , . . . , x _ { n }$ be the $n$ distinct zeros of $L _ { n }$ and define, for each $i = 1 , . . . , n$ ,

$$
c _ { n , i } = \int _ { 0 } ^ { \infty } e ^ { - x } \prod _ { j = 1 \atop j \neq i } ^ { n } { \frac { ( x - x _ { j } ) } { ( x _ { i } - x _ { j } ) } } d x .
$$

Let $P ( x )$ be any polynomial of degree $n - 1$ or less, and let $P _ { n - 1 } ( x )$ be the $( n - 1 )$ th Lagrange polynomial for $P$ on the nodes $x _ { 1 } , . . . , x _ { n }$ . As in the proof of Theorem 4.7,

$$
\int _ { 0 } ^ { \infty } P ( x ) e ^ { - x } \ d x = \int _ { 0 } ^ { \infty } P _ { n - 1 } ( x ) e ^ { - x } \ d x = \sum _ { i = 1 } ^ { n } c _ { n , i } P ( x _ { i } ) ,
$$

so the quadrature formula is exact for polynomials of degree $n - 1$ or less.

If $P ( x )$ has degree $2 n - 1$ or less, then $P ( x )$ can be divided by the $n$ th Laguerre polynomial $L _ { n } ( x )$ to obtain

$$
P ( x ) = Q ( x ) L _ { n } ( x ) + R ( x ) ,
$$

where $Q ( x )$ and $R ( x )$ are both polynomials of degree less than $n$ . As in proof of Theorem 4.7, the orthogonality of the Laguerre polynomials on $[ 0 , \infty )$ implies that

$$
Q ( x ) = \sum _ { i = 0 } ^ { n - 1 } d _ { i } L _ { i } ( x ) ,
$$

for some constants $d _ { i }$ .

Thus

$$
{ \begin{array} { r l } { \displaystyle \int _ { 0 } ^ { \infty } e ^ { - x } P ( x ) \ d x = } & { \displaystyle \int _ { 0 } \sum _ { i = 0 } ^ { \infty } d _ { i } L _ { i } ( x ) L _ { n } ( x ) e ^ { - x } \ d x + \int _ { 0 } ^ { \infty } e ^ { - x } R ( x ) \ d x } \\ & { \quad \quad = \displaystyle \sum _ { i = 0 } ^ { n - 1 } d _ { i } \int _ { 0 } ^ { \infty } L _ { i } ( x ) L _ { n } ( x ) e ^ { - x } \ d x + \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) } \\ & { \quad \quad = \displaystyle 0 + \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) = \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) . } \end{array} }
$$

But

$$
P ( x _ { i } ) = Q ( x _ { i } ) L _ { n } ( x _ { i } ) + R ( x _ { i } ) = 0 + R ( x _ { i } ) = R ( x _ { i } ) ,
$$

so

$$
\int _ { 0 } ^ { \infty } e ^ { - x } P ( x ) \ d x = \sum _ { i = 1 } ^ { n } c _ { n , i } P ( x _ { i } ) .
$$

Hence the quadrature formula has degree of precision $2 n - 1$ .

7. With $n = 2$ we have

$$
\int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 8 5 3 5 5 3 4 f ( 0 . 5 8 5 7 8 6 4 ) + 0 . 1 4 6 4 4 6 6 f ( 3 . 4 1 4 2 1 3 6 ) ,
$$

and with $n = 3$ we have

$$
\int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 7 1 1 0 9 3 0 f ( 0 . 4 1 5 7 7 4 6 ) + 0 . 2 7 8 5 1 7 7 f ( 2 . 2 9 4 2 8 0 4 ) . + 0 . 0 1 0 3 8 9 3 f ( 6 . 2 8 9 9 4 5 1 ) ^ { \prime }
$$

8. For $n = 2$ we have 0.9238795. For $n = 3$ we have 0.9064405.

9. For $n = 2$ we have 2.9865139. For $n = 3$ we have 2.9958198.

# Initial-Value Problems for Ordinary Differential Equations

Exercise Set 5.1, page 264

1. \*(a) Since $f ( t , y ) = y \cos t$ , we have ${ \frac { \partial f } { \partial y } } ( t , y ) = \cos t$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 1$ on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = e ^ { \sin t }$

(b) Since $f ( t , y ) = { \frac { \mathit { \omega } ^ { 2 } } { t } } y + t ^ { 2 } e ^ { t }$ , we have ${ \frac { \partial f } { \partial y } } = { \frac { 2 } { t } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = t ^ { 2 } ( e ^ { t } - e )$ .

(c) Since $f ( t , y ) = - \frac { 2 } { t } y + t ^ { 2 } e ^ { t }$ , we have ${ \frac { \partial f } { \partial y } } = - { \frac { 2 } { t } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is

$$
y ( t ) = ( t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } + ( \sqrt { 2 } - 9 ) e ) / t ^ { 2 } .
$$

(d) Since $f ( t , y ) = \frac { 4 t ^ { 3 } y } { 1 + t ^ { 4 } }$ we have $\frac { \partial f } { \partial y } = \frac { 4 t ^ { 3 } } { 1 + t ^ { 4 } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = 1 + t ^ { 4 }$ .

2. (a) Since $f ( t , y ) = e ^ { t - y }$ , we have $\frac { \partial f } { \partial y } ( t , y ) = - e ^ { t - y }$ , and $f$ does not satisfies a Lipschitz condition in $y$ o n

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is $y ( t ) = \ln ( e ^ { t } - 1 + e )$ .

(b) Since $f ( t , y ) = t ^ { - 2 } ( \sin ( 2 t ) - 2 t y )$ , we have $\frac { \partial f } { \partial y } = - 2 / t$ = −2/t, and f satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = \frac { 1 } { 2 } ( 4 + \cos 2 -$ $\cos ( 2 t ) ) t ^ { - 2 }$ .

(c) Since $f ( t , y ) = - y + t y ^ { 1 / 2 }$ , we have $\frac { \partial f } { \partial y } = - 1 + ( t / 2 ) y ^ { - 1 / 2 }$ , and $f$ does not satisfies a Lipschitz condition in $y$ on

$$
D = \{ ( t , y ) | 2 \leq t \leq 3 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is $y ( t ) = \left( t - 2 + \sqrt { 2 } e ^ { 1 - t / 2 } \right) ^ { 2 }$ .

(d) Since $f ( t , y ) = { \frac { t y + y } { t y + t } }$ , we have $\frac { \partial f } { \partial y } = \frac { t + 1 } { t ( y + 1 ) ^ { 2 } }$ and $f$ does not satisfies a Lipschitz condition in $y$ o n

$$
D = \{ ( t , y ) | 2 \leq 4 \leq 1 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is implicitly given by $y ( t ) - t - 2 = \ln ( 2 t / y ( t ) )$

3. (a) Lipschitz constant $L = 1$ ; it is a well-posed problem. (b) Lipschitz constant $L = 1$ ; it is a well-posed problem. (c) Lipschitz constant $L = 1$ ; it is a well-posed problem. (d) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used.

4. (a) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used. (b) Lipschitz constant $L = 1$ ; it is a well-posed problem. (c) Lipschitz constant $L = 1$ ; it is a well-posed problem. (d) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used.

5. $^ { * } ( \mathrm { a } )$ Differentiating

$$
y ^ { 3 } t + y t = 2 \quad { \mathrm { g i v e s } } \quad 3 y ^ { 2 } y ^ { \prime } t + y ^ { 3 } + y ^ { \prime } t + y = 0 .
$$

Solving for $y ^ { \prime }$ gives the original differential equation, and setting $t = 1$ and $y = 1$ verifies the initial condition. To approximate $y ( 2 )$ , use Newton’s method to solve the equation $y ^ { 3 } + y - 1 = 0$ . This gives $y ( 2 ) \approx 0 . 6 8 2 3 2 7 8$ .

(b) Differentiating

$$
y \sin t + t ^ { 2 } e ^ { y } + 2 y - 1 = 0 \quad { \mathrm { g i v e s } } \quad y ^ { \prime } \sin t + y \cos t + 2 t e ^ { y } + t ^ { 2 } e ^ { y } y ^ { \prime } + 2 y ^ { \prime } = 0 .
$$

Solving for $y ^ { \prime }$ gives the original differential equation, and setting $t = 1$ and $y = 0$ verifies the initial condition. To approximate $y ( 2 )$ , use Newton’s method to solve the equation $( 2 + \sin 2 ) y + 4 e ^ { y } - 1 = 0$ . This gives $y ( 2 ) \approx - 0 . 4 9 4 6 5 9 9$ .

$^ { * } 6$ . Let $( t , y _ { 1 } )$ and $( t , y _ { 2 } )$ be in $D$ . Holding $t$ fixed, define $g ( y ) = f ( t , y )$ . Suppose $y _ { 1 } < y _ { 2 }$ . Since the line joining $( t , y _ { 1 } )$ to $( t , y _ { 2 } )$ lies in $D$ and $f$ is continuous on $D$ , we have $g \in C [ y _ { 1 } , y _ { 2 } ]$ .

Further, g′(y) = ∂f (t, y) . Using the Mean Value Theorem on g, a number ξ, for y1 < ξ < y2, ∂y   
exists with

$$
g ( y _ { 2 } ) - g ( y _ { 1 } ) = g ^ { \prime } ( \xi ) ( y _ { 2 } - y _ { 1 } ) .
$$

Thus

$$
f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) = \frac { \partial f ( t , \xi ) } { \partial y } ( y _ { 2 } - y _ { 1 } )
$$

and

$$
| f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) | \leq L \left| y _ { 2 } - y _ { 1 } \right| .
$$

The proof is similar if $y _ { 2 } < y _ { 1 }$ . Therefore, $f$ satisfies a Lipschitz condition on $D$ in the variable $y$ with Lipschitz constant $L$ .

7. Let $( t _ { 1 } , y _ { 1 } )$ and $( t _ { 2 } , y _ { 2 } )$ be in $D$ , with $a \leq t _ { 1 } \leq b$ , $a \leq t _ { 2 } \leq b$ , $- \infty < y _ { 1 } < \infty$ , and $- \infty < y _ { 2 } <$ $\infty$ .

For $0 \leq \lambda \leq 1$ , we have

$$
( 1 - \lambda ) a \leq ( 1 - \lambda ) t _ { 1 } \leq ( 1 - \lambda ) b \quad \mathrm { a n d } \quad \lambda a \leq \lambda t _ { 2 } \leq \lambda b .
$$

Hence

$$
a = ( 1 - \lambda ) a + \lambda a \leq ( 1 - \lambda ) t _ { 1 } + \lambda t _ { 2 } \leq ( 1 - \lambda ) b + \lambda b = b .
$$

Also, $- \infty < ( 1 - \lambda ) y _ { 1 } + \lambda y _ { 2 } < \infty$ , so $D$ is convex.

8. (a) Since $y ( t ) = 1 - e ^ { - t }$ , we have

$$
z ( t ) = 1 - e ^ { - t } + \delta \left( t - 1 + e ^ { - t } \right) + \varepsilon _ { 0 } e ^ { - t } \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \leq 2 | \delta | + | \varepsilon _ { 0 } | < 3 \varepsilon ,
$$

so the problem is well posed.

(b) Since $y ( t ) = - t - 1$ , we have

$$
z ( t ) = - t - 1 + \delta \left( - t - 1 + e ^ { t } \right) + \varepsilon _ { 0 } e ^ { t } \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \leq 4 . 4 | \delta | + 7 . 4 | \varepsilon _ { 0 } | < 1 1 . 8 \varepsilon ,
$$

so the problem is well posed.

(c) Since $y ( t ) = t ^ { 2 } \left( e ^ { t } - e \right)$ , we have

$$
z ( t ) = t ^ { 2 } \left( e ^ { t } - e \right) + t ^ { 2 } \left( \varepsilon _ { 0 } + \delta \ln t \right) \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \le 4 ( | \varepsilon _ { 0 } | + \ln 2 | \delta | ) < 6 . 8 \varepsilon ,
$$

so the problem is well posed.

(d) Since

$$
y ( t ) = \frac { t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } } { t ^ { 2 } } + \frac { \left( \sqrt { 2 } - 9 \right) e } { t ^ { 2 } } ,
$$

we have

$$
z ( t ) = { \frac { t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } } { t ^ { 2 } } } + { \frac { \left( { \sqrt { 2 } } - 9 \right) e } { t ^ { 2 } } } + { \frac { 1 } { 4 } } \delta t ^ { 2 } + { \frac { \varepsilon _ { 0 } - \delta / 4 } { t ^ { 2 } } }
$$

and

$$
| y ( t ) - z ( t ) | \leq | \delta | + | \varepsilon _ { 0 } | + | \delta | / 4 < 2 . 2 5 \varepsilon ,
$$

so the problem is well posed.

$^ { * } 9$ . (a) Since $y ^ { \prime } = f ( t , y ( t ) )$ , we have

$$
\int _ { a } ^ { t } y ^ { \prime } ( z ) \ d z = \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z .
$$

So

$$
y ( t ) - y ( a ) = \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z
$$

and

$$
y ( t ) = \alpha + \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z .
$$

The iterative method follows from this equation.

(b) We have

$$
y _ { 0 } ( t ) = 1 , y _ { 1 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } , y _ { 2 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } - { \frac { 1 } { 6 } } t ^ { 3 } , \mathrm { a n d } y _ { 3 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } - { \frac { 1 } { 6 } } t ^ { 3 } + { \frac { 1 } { 2 4 } } t ^ { 4 } .
$$

(c) We have

$$
y ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } - \frac { 1 } { 6 } t ^ { 3 } + \frac { 1 } { 2 4 } t ^ { 4 } - \frac { 1 } { 1 2 0 } t ^ { 5 } + \cdots .
$$

# Exercise Set 5.2, page 273

1. Euler’s method gives the approximations in the following tables.

<table><tr><td rowspan="7">*(a)</td><td colspan="3">y(ti)</td></tr><tr><td>i</td><td>ti</td><td>Wi</td></tr><tr><td>1 2</td><td>0.500</td><td>0.0000000 0.2836165</td></tr><tr><td>1.000</td><td>1.1204223</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td rowspan="3">(b) i</td><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>2.500</td><td>2.0000000</td><td>1.8333333</td></tr><tr><td>2</td><td>3.000</td><td>2.6250000</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="4">C</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.250</td><td>2.7500000</td><td>2.7789294</td></tr><tr><td>2</td><td>1.500</td><td>3.5500000</td><td>3.6081977</td></tr><tr><td>3</td><td>1.750</td><td>4.3916667</td><td>4.4793276</td></tr><tr><td>4</td><td>2.000</td><td>5.2690476</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi 1.2500000</td><td>y(ti) 1.3291498</td></tr><tr><td>1 2</td><td>0.250 0.500</td><td>1.6398053</td><td>1.7304898</td></tr><tr><td>3</td><td>0.750</td><td>2.0242547</td><td>2.0414720</td></tr><tr><td>4</td><td>1.000</td><td>2.2364573</td><td>2.1179795</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

2. Euler’s method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>ti Wi</td></tr><tr><td>0.5 1.183939721</td></tr><tr><td>1.0</td><td>1.436252216</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td>1.5 2.333333333</td></tr><tr><td>2.0</td><td>2.708333333</td></tr><tr><td rowspan="3">(c)</td><td></td></tr><tr><td>ti Wi</td></tr><tr><td>2.25 2.207106781</td></tr><tr><td>2.50</td><td>2.490998908</td></tr><tr><td>2.75</td><td>2.854680348</td></tr><tr><td>3.00</td><td>3.302596464</td></tr></table>

<table><tr><td rowspan="3">(d) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td></td></tr><tr><td>1.25</td><td>1.227324357</td></tr><tr><td>1.50</td><td>0.8321501572</td></tr><tr><td>1.75</td><td>0.5704467722</td></tr><tr><td>2.00</td><td>0.3788266146</td></tr></table>

3. The actual errors and error bounds for the approximations in Exercise 1 are given in the following tables.

<table><tr><td colspan="4">*(a)</td></tr><tr><td>t</td><td>Actual error</td><td>Error bound</td><td></td></tr><tr><td>0.5</td><td></td><td>0.2836165</td><td>11.3938</td></tr><tr><td>1.0</td><td>2.0986771</td><td></td><td>42.3654</td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td rowspan="3"></td><td>Actual</td><td>error</td><td>Error rbound</td></tr><tr><td>t</td><td></td><td></td></tr><tr><td>2.5 3.0</td><td>0.166667 0.125000</td><td>0.429570 1.59726</td></tr></table>

<table><tr><td colspan="4">(c)</td></tr><tr><td>t</td><td>Actual</td><td>error Error</td><td>bound</td></tr><tr><td></td><td>1.25</td><td>0.0289294</td><td>0.0355032</td></tr><tr><td>1.50</td><td></td><td>0.0581977</td><td>0.0810902</td></tr><tr><td></td><td>1.75</td><td>0.0876610</td><td>0.139625</td></tr><tr><td></td><td>2.00</td><td>0.117247</td><td>0.214785</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td>t</td><td>Actual error</td></tr><tr><td>0.25</td><td>0.0791498</td></tr><tr><td>0.50</td><td>0.0906844</td></tr><tr><td>0.75</td><td>0.0172174</td></tr><tr><td>1.00</td><td>0.118478</td></tr></table>

For Part (d), error bound formula (5.10) cannot be applied since $L = 0$ .

4. The actual errors and error bounds for the approximations in Exercise 1 are given in the following tables.

<table><tr><td>(a) ti</td><td>lwi-y(ti)l</td><td>Error bound</td></tr><tr><td>0.5 1.0</td><td>0.030083340 0.053627909</td><td>0.06651369683 0.3254413801</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td colspan="2"></td></tr><tr><td>|wi-y(ti)l</td><td>Error bound</td></tr><tr><td>1.5</td><td>0.020768633 0.02518894623</td></tr><tr><td>2.0</td><td>0.033324054</td><td>0.05494617010</td></tr></table>

<table><tr><td colspan="2">C</td><td colspan="2">Error bound</td></tr><tr><td>ti 2.25</td><td></td><td>lwi-y(ti)l 0.037014328</td><td>0.04985076072</td></tr><tr><td>2.50</td><td></td><td>0.073453039</td><td>0.1100812516</td></tr><tr><td>2.75</td><td></td><td>0.110513485</td><td>0.1828526997</td></tr><tr><td></td><td>3.00</td><td>0.148690185</td><td>0.2707763338</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2">Error bound</td></tr><tr><td>ti</td><td></td><td>lwi-y(ti)l</td><td></td></tr><tr><td>1.25 1.50</td><td></td><td>0.175874613 0.1842599898</td><td>0.3053253946 0.8087218666</td></tr><tr><td>1.75</td><td></td><td>0.1675629993</td><td>1.638682338</td></tr><tr><td>2.00</td><td></td><td>0.1508604834</td><td>3.007055822</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

5. Euler’s method gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>1.200</td><td>1.0082645</td><td>1.0149523</td></tr><tr><td>4 6</td><td>1.400</td><td>1.0385147 1.0784611</td><td>1.0475339 1.0884327</td></tr><tr><td>8</td><td>1.600 1.800</td><td>1.1232621</td><td>1.1336536</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>2.000</td><td>1.1706516</td><td>1.1812322</td></tr></table>

<table><tr><td rowspan="8">*(b) ti</td><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>i</td><td>Wi</td><td>y(ti) 0.4896817</td></tr><tr><td>2 4</td><td>1.400 0.4388889 1.800 1.0520380</td><td>1.1994386</td></tr><tr><td>6 2.200</td><td>1.8842608</td><td>2.2135018</td></tr><tr><td>8 2.600</td><td>3.0028372</td><td>3.6784753</td></tr><tr><td>10 3.000</td><td>4.5142774</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="4">C</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>0.400</td><td>-1.6080000</td><td>-1.6200510</td></tr><tr><td>4</td><td>0.800</td><td>-1.3017370</td><td>-1.3359632</td></tr><tr><td>6</td><td>1.200</td><td>-1.1274909</td><td>-1.1663454</td></tr><tr><td>8</td><td>1.600</td><td>-1.0491191</td><td>-1.0783314</td></tr><tr><td>10</td><td>2.000</td><td>-1.0181518</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2 4</td><td>0.2</td><td>0.1083333 0.1620833</td><td>0.1626265 0.2051118</td></tr><tr><td>6</td><td>0.4 0.6</td><td>0.3455208</td><td>0.3765957</td></tr><tr><td>8</td><td></td><td></td><td>0.6461052</td></tr><tr><td></td><td>0.8</td><td>0.6213802</td><td></td></tr><tr><td>10</td><td>1.0</td><td>0.9803451</td><td>1.0022460</td></tr></table>

6. Euler’s method gives the approximations in the following tables.

<table><tr><td colspan="4">(a) 0.2</td></tr><tr><td></td><td>i</td><td>ti</td><td>Wi</td></tr><tr><td colspan="4">2</td></tr><tr><td colspan="2">3</td><td>0.3</td><td>1.513709064</td></tr><tr><td colspan="2">9 10</td><td>0.9 1.0</td><td>1.631412128 1.579669485</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td></td><td>Wi</td></tr><tr><td>3</td><td>2</td><td>1.2</td><td>-1.253297013</td></tr><tr><td></td><td>1.3</td><td></td><td>-1.181899131</td></tr><tr><td>9</td><td>1.9</td><td></td><td>-0.9150285539</td></tr><tr><td>10</td><td>2.0</td><td></td><td>-0.8861569244</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td rowspan="2"></td></tr><tr><td>5</td><td>2.0</td><td>-1.248872291</td></tr><tr><td>6</td><td></td><td>2.2</td><td>-1.217791320</td></tr><tr><td>8</td><td>2.6</td><td></td><td>-1.174414016</td></tr><tr><td>9</td><td>2.8</td><td></td><td>-1.158657534</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td></tr><tr><td>5</td><td>0.5</td><td>1.255609618</td></tr><tr><td>6</td><td>0.6</td><td>1.352114314</td></tr><tr><td>9</td><td>0.9</td><td>1.624904878</td></tr><tr><td>10</td><td>1.0</td><td>1.700214869</td></tr></table>

7. The actual errors for the approximations in Exercise 3 are in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>t Actual error</td></tr><tr><td>1.2</td></tr><tr><td>1.5</td><td>0.0066879 0.0095942</td></tr><tr><td>1.7</td><td>0.0102229</td></tr><tr><td>2.0</td><td>0.0105806</td></tr><tr><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>*(b)</td><td rowspan=1 colspan=1>t   Actual error</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.4   0.0507928</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0    0.2240306</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.4    0.4742818</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0    1.3598226</td></tr></table>

<table><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>t   Actualerror</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4   0.0120510</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0    0.0391546</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.4    0.0349030</td></tr><tr><td rowspan=1 colspan=2>2.0    0.0178206</td></tr></table>

<table><tr><td rowspan="3">(d)</td><td></td></tr><tr><td></td></tr><tr><td>t Actual error</td></tr><tr><td>0.2</td><td>0.0542931</td></tr><tr><td>0.5 0.7</td><td>0.0363200</td></tr><tr><td></td><td>0.0273054</td></tr><tr><td>1.0</td><td>0.0219009</td></tr></table>

8. The actual errors for the approximations in Exercise 5 are in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>t Actual error</td></tr><tr><td>0.2</td></tr><tr><td rowspan="4">0.3 1.0</td><td>0.028103580</td></tr><tr><td>0.045819156</td></tr><tr><td>0.9 0.084450802</td></tr><tr><td>0.079669485</td></tr></table>

<table><tr><td rowspan="4">(b)</td><td></td></tr><tr><td>Actual error</td></tr><tr><td>t</td></tr><tr><td>1.2 0.015002391</td></tr><tr><td>1.3</td><td>0.018712043</td></tr><tr><td>1.9</td><td>0.0241936829</td></tr><tr><td>2.0</td><td>0.0240823020</td></tr></table>

<table><tr><td rowspan=1 colspan=1>C)</td><td rowspan=1 colspan=1>t   Actual error</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0  0.084461042</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.2  0.076326327</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.6  0.0636812222.8  0.058733770</td></tr></table>

<table><tr><td rowspan=1 colspan=1>(d)</td><td rowspan=1 colspan=1>t   Actualerror</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5  0.034195658</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  0.028816902</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.9  0.007708304</td></tr><tr><td rowspan=1 colspan=2>1.0  0.001655184</td></tr></table>

$^ { * } 9$ . Euler’s method gives the approximations in the following table.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>0.271828</td><td>0.345920</td></tr><tr><td>5</td><td>1.5</td><td>3.18744</td><td>3.96767</td></tr><tr><td>6</td><td>1.6</td><td>4.62080</td><td>5.70296</td></tr><tr><td>9</td><td>1.9</td><td>11.7480</td><td>14.3231</td></tr><tr><td>10</td><td>2.0</td><td>15.3982</td><td>18.6831</td></tr></table>

(b) Linear interpolation gives the approximations in the following table.

<table><tr><td>t</td><td>Approximation</td><td>y(t)</td><td>Error</td></tr><tr><td>1.04</td><td>0.108731</td><td>0.119986</td><td>0.01126</td></tr><tr><td>1.55</td><td>3.90412</td><td>4.78864</td><td>0.8845</td></tr><tr><td>1.97</td><td>14.3031</td><td>17.2793</td><td>2.976</td></tr></table>

(c) $h < 0 . 0 0 0 6 4$

10. (a) We have

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9500000</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9045353</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6263495</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6049486</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.4850416</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.4712186</td><td>-0.5000000</td></tr></table>

(b) (i) $y ( 1 . 0 5 2 ) \approx - 0 . 9 4 8 1 8 1 4$ (ii) $y ( 1 . 5 5 5 ) \approx - 0 . 6 2 4 2 0 9 4$ (iii) $y ( 1 . 9 7 8 ) \approx - 0 . 4 7 7 3 0 0 7$

11. (a) Euler’s method produces the following approximation to $y ( 5 ) = 5 . 0 0 6 7 4$

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>h= 0.2</td><td rowspan=1 colspan=1>h=0.1</td><td rowspan=1 colspan=1>h=0.05</td></tr><tr><td rowspan=1 colspan=1>WN</td><td rowspan=1 colspan=1>5.00377</td><td rowspan=1 colspan=1>5.00515</td><td rowspan=1 colspan=1>5.00592</td></tr></table>

(b) $h = { \sqrt { 2 \times 1 0 ^ { - 6 } } } \approx 0 . 0 0 1 4 1 4 2 .$

$^ { * } 1 2$ . For $t > 0$ , the approximations are zero and are not adequate approximations until the solution becomes close to zero. This behavior does not violate Theorem 5.9.

13. (a) $1 . 0 2 1 9 5 7 = y ( 1 . 2 5 ) \approx 1 . 0 1 4 9 7 8$ , $1 . 1 6 4 3 9 0 = y ( 1 . 9 3 ) \approx 1 . 1 5 3 9 0 2$ \*(b) $1 . 9 2 4 9 6 2 = y ( 2 . 1 ) \approx 1 . 6 6 0 7 5 6$ , $4 . 3 9 4 1 7 0 = y ( 2 . 7 5 ) \approx 3 . 5 2 6 1 6 0$ (c) $- 1 . 1 3 8 2 7 7 = y ( 1 . 3 ) \approx - 1 . 1 0 3 6 1 8 , - 1 . 0 4 1 2 6 7 =$ $- 1 . 1 0 3 6 1 8 , - 1 . 0 4 1 2 6 7 = y ( 1 . 9 3 ) \approx - 1 . 0 2 2 2 8 3$ (d) 0.3140018 = y(0.54) ≈ 0.2828333, $0 . 8 8 6 6 3 1 8 = y ( 0 . 9 4 ) \approx 0 . 8 6 6 5 5 2 1$

14. (a) $1 . 4 1 1 7 6 4 7 0 6 = y ( 0 . 2 5 ) \approx 1 . 4 4 3 9 8 3 2 4 5 , 1 . 5 3 3 5 9 4 2 9 5 = y ( 0 . 9 3 ) \approx 1 . 6 1 5 8 8 9 3 3 5$ (b) $- 1 . 2 3 3 1 5 1 7 3 1 = y ( 1 . 2 5 ) \approx - 1 . 2 1 7 5 9 8 0 7 2$ , $- 0 . 9 3 0 2 3 0 4 6 1 4 = y ( 1 . 9 3 ) \approx - 0 . 9 0 6 3 6 7 0 6 5 0$ (c) $- 1 . 3 1 2 5 = y ( 2 . 1 0 ) \approx , - 1 . 2 3 3 3 3 1 8 0 6 - 1 . 2 2 2 2 2 2 2 2 2 = y ( 2 . 7 5 ) \approx - 1 . 1 6 2 5 9 6 6 5 4 . 9 9 9 6 9$ 4 (d) $1 . 3 2 6 1 9 6 8 5 2 = y ( 0 . 5 4 ) \approx 1 . 2 9 4 2 1 1 4 9 6 , 1 . 6 6 1 3 6 1 7 5 1 = y ( 0 . 9 4 ) \approx 1 . 6 5 5 0 2 8 8 7 4$

15. (a) h = 10−n/2 (b) The minimal error is $1 0 ^ { - n / 2 } ( e - 1 ) + 5 e 1 0 ^ { - n - 1 }$ . (c)

<table><tr><td>t</td><td>w(h = 0.1)</td><td>w(h = 0.01)</td><td>y(t)</td><td>Error (n= 8)</td></tr><tr><td>0.5</td><td>0.40951</td><td>0.39499</td><td>0.39347</td><td>1.5 ×10-4</td></tr><tr><td>1.0</td><td>0.65132</td><td>0.63397</td><td>0.63212</td><td>3.1 ×10-4</td></tr></table>

16. We have

<table><tr><td>j</td><td>tj</td></tr><tr><td></td><td>Wj</td></tr><tr><td>20 2</td><td>0.702938</td></tr><tr><td>40 4</td><td>-0.0457793</td></tr><tr><td>60 6</td><td>0.294870</td></tr><tr><td>80 8</td><td>0.341673</td></tr><tr><td>100 10</td><td>0.139432</td></tr></table>

17. (b) $w _ { 5 0 } = 0 . 1 0 4 3 0 \approx p ( 5 0 )$ (c) Since $p ( t ) = 1 - 0 . 9 9 e ^ { - 0 . 0 0 2 t }$ , $p ( 5 0 ) = 0 . 1 0 4 2 1$ .

# Exercise Set 5.3, page 281

1. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td rowspan="3">*(a)</td><td>ti Wi</td><td>y(ti)</td></tr><tr><td>0.50 0.12500000</td><td>0.28361652</td></tr><tr><td>1.00 2.02323897</td><td>3.21909932</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td></td></tr><tr><td>2.50 1.75000000 3.00 2.42578125</td><td>1.83333333 2.50000000</td></tr></table>

<table><tr><td colspan="2">C ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>1.25</td><td>2.78125000</td><td>2.77892944</td></tr><tr><td></td><td>1.50</td><td>3.61250000</td><td>3.60819766</td></tr><tr><td></td><td>1.75</td><td>4.48541667</td><td>4.47932763</td></tr><tr><td></td><td>2.00</td><td>5.39404762</td><td>5.38629436</td></tr></table>

<table><tr><td colspan="2">(d) ti</td><td></td><td>y(ti)</td></tr><tr><td>0.25</td><td></td><td>1.34375000</td><td>1.32914981</td></tr><tr><td></td><td>0.50</td><td>1.77218707</td><td>1.73048976</td></tr><tr><td></td><td>0.75</td><td>2.11067606</td><td>2.04147203</td></tr><tr><td>1.00</td><td></td><td>2.20164395</td><td>2.11797955</td></tr></table>

2. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50</td><td>1.2130077</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4893295</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2437184</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5634054</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9633902</td><td>2.9651394</td></tr><tr><td>3.00</td><td>3.4486992</td><td>3.4512866</td></tr></table>

<table><tr><td rowspan="3">(b) ti 1.50</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.3564815</td><td>2.3541020</td></tr><tr><td>2.00 2.7454763</td><td>2.7416574</td></tr></table>

<table><tr><td rowspan="2">ti</td><td colspan="2">Wi y(ti)</td></tr><tr><td></td><td>1.4031990</td></tr><tr><td>1.25 1.50</td><td>1.4626530 1.0785177</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.79184185</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.574516240</td><td>0.52968710</td></tr></table>

3. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">*(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.50</td><td>0.25781250</td><td>0.28361652 3.21909932</td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.50</td><td>1.81250000</td><td>1.83333333</td></tr><tr><td></td><td>3.00</td><td>2.48591644</td><td>2.50000000</td></tr></table>

<table><tr><td colspan="3">ti Wi</td><td rowspan="2">y(ti)</td></tr><tr><td colspan="3">C</td></tr><tr><td></td><td>1.25</td><td>2.77897135</td><td>2.77892944</td></tr><tr><td></td><td>1.50</td><td>3.60826562</td><td>3.60819766</td></tr><tr><td></td><td>1.75</td><td>4.47941561</td><td>4.47932763</td></tr><tr><td></td><td>2.00</td><td>5.38639966</td><td>5.38629436</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.25</td><td>1.32893880</td><td>1.32914981</td></tr><tr><td></td><td>0.50</td><td>1.72966730</td><td>1.73048976</td></tr><tr><td></td><td>0.75</td><td>2.03993417</td><td>2.04147203</td></tr><tr><td></td><td>1.00</td><td>2.11598847</td><td>2.11797955</td></tr></table>

4. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2140485</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4898968</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541059</td><td>2.3541020</td></tr><tr><td></td><td>2.00</td><td>2.7416702</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2441297</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5644662</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9652116</td><td>2.9651394</td></tr><tr><td>3.00</td><td>3.4513065</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4090648</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0217897</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.74234451</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.53314083</td><td>0.52968710</td></tr></table>

5. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td></td><td colspan="3">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1 2</td><td>1.1 1.2</td><td>1.214999 1.465250</td><td>1.215886 1.467570</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.5</td><td>0.5000000</td><td>0.5158868</td></tr><tr><td>2</td><td>1.0</td><td>1.076858</td><td>1.091818</td></tr></table>

<table><tr><td colspan="4">*（c)</td></tr><tr><td></td><td colspan="3">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1 2</td><td>1.5</td><td>-2.000000</td><td>-1.500000</td></tr><tr><td></td><td>2.0</td><td>-1.777776</td><td>-1.333333</td></tr><tr><td>3</td><td>2.5</td><td>-1.585732</td><td>-1.250000</td></tr><tr><td>4</td><td>3.0</td><td>-1.458882</td><td>-1.200000</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td>i</td><td>ti</td><td>Order 2 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.25</td><td>1.093750</td><td>1.087088</td></tr><tr><td>2</td><td>0.50</td><td>1.312319</td><td>1.289805</td></tr><tr><td>3</td><td>0.75</td><td>1.538468</td><td>1.513490</td></tr><tr><td>4</td><td>1.0</td><td>1.720480</td><td>1.701870</td></tr></table>

6. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td rowspan="2">(a)</td><td colspan="3"></td></tr><tr><td></td><td></td></tr><tr><td>i 2</td><td>ti</td><td>Wi 1.3492187</td></tr><tr><td>4</td><td>0.2</td><td>1.5546191</td></tr><tr><td>6</td><td>0.4</td><td>1.6184028</td></tr><tr><td></td><td>0.6</td><td>1.5840995</td></tr><tr><td>8</td><td>0.8</td><td></td></tr><tr><td>10</td><td>1.0</td><td>1.4976289</td></tr></table>

<table><tr><td colspan="2">(b)</td></tr><tr><td>i ti</td><td>Wi</td></tr><tr><td>2</td><td>1.2 -1.2697379</td></tr><tr><td>4</td><td>1.4 −1.1441477</td></tr><tr><td>6</td><td>1.6 -1.0485714</td></tr><tr><td>8</td><td>1.8 -0.97321601</td></tr><tr><td>10 2.0</td><td>-0.91214217</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">i ti</td></tr><tr><td>2 1.4</td><td>Wi -1.6024604</td></tr><tr><td>4</td><td>1.8 -1.4206863</td></tr><tr><td>6</td><td>2.2</td></tr><tr><td></td><td>-1.3217746 -1.2601896</td></tr><tr><td>8</td><td>2.6 -1.2182831</td></tr><tr><td colspan="2">10 3.0</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2">i ti Wi</td></tr><tr><td>2 0.2</td><td>1.0581740</td></tr><tr><td>4 0.4</td><td>1.2044189</td></tr><tr><td>6</td><td>1.3846529</td></tr><tr><td>0.6 8 0.8</td><td>1.5584034</td></tr><tr><td>10 1.0</td><td>1.7043395</td></tr></table>

7. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>1.215883</td><td>1.215886</td></tr><tr><td>2</td><td>1.2</td><td>1.467561</td><td>1.467570</td></tr></table>

<table><tr><td colspan="4">*（c)</td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.5</td><td>-2.000000</td><td>-1.500000</td></tr><tr><td>2</td><td>2.0</td><td>-1.679012</td><td>-1.333333</td></tr><tr><td>3</td><td>2.5</td><td>-1.484493</td><td>-1.250000</td></tr><tr><td>4</td><td>3.0</td><td>−1.374440</td><td>−1.200000</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.5</td><td>0.5156250</td><td>0.5158868</td></tr><tr><td>2</td><td>1.0</td><td>1.091267</td><td>1.091818</td></tr></table>

<table><tr><td colspan="4">(d) Order 4</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.25</td><td>1.086426</td><td>1.087088</td></tr><tr><td>2</td><td>0.50</td><td>1.288245</td><td>1.289805</td></tr><tr><td>3</td><td>0.75</td><td>1.512576</td><td>1.513490</td></tr><tr><td>4</td><td>1.0</td><td>1.701494</td><td>1.701870</td></tr></table>

8. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td></tr><tr><td colspan="2">i</td></tr><tr><td>ti 2 0.2</td><td>Wi</td></tr><tr><td>4</td><td>1.3461270 0.4 1.5517144</td></tr><tr><td>6</td><td>0.6 1.6176616</td></tr><tr><td>8 0.8</td><td>1.5853873</td></tr><tr><td>10 1.0</td><td>1.5000175</td></tr></table>

<table><tr><td colspan="1" rowspan="1">(b)</td><td colspan="1" rowspan="1">i    ti         Wi</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">2   1.2   -1.2683126</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4   1.4   -1.1422607</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">6   1.6   -1.0465749</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8   1.8  -0.97124644</td></tr><tr><td colspan="2" rowspan="1">10 2.0  -0.91025180</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">i</td></tr><tr><td>ti 1.4</td><td>Wi</td></tr><tr><td>2 4</td><td>-1.5618034 1.8 -1.3887436</td></tr><tr><td>6</td><td>2.2 -1.2971040</td></tr><tr><td>8 2.6</td><td>-1.2404156</td></tr><tr><td>10 3.0</td><td>-1.2018912</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2">i ti</td></tr><tr><td>2 0.2</td><td>Wi</td></tr><tr><td>4 0.4</td><td>1.0571619 1.2014475</td></tr><tr><td>6</td><td>1.3809015</td></tr><tr><td>0.6 8 0.8</td><td>1.5550142</td></tr><tr><td>10 1.0</td><td>1.7018616</td></tr></table>

\*9. (a) Taylor’s method of order two gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>0.3397852</td><td>0.3459199</td></tr><tr><td>5</td><td>1.5</td><td>3.910985</td><td>3.967666</td></tr><tr><td>6</td><td>1.6</td><td>5.643081</td><td>5.720962</td></tr><tr><td>9</td><td>1.9</td><td>14.15268</td><td>14.32308</td></tr><tr><td>10</td><td>2.0</td><td>18.46999</td><td>18.68310</td></tr></table>

(b) Linear interpolation gives

$y ( 1 . 0 4 ) \approx 0 . 1 3 5 9 1 3 9 , \quad y ( 1 . 5 5 ) \approx 4 . 7 7 7 0 3 3 \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) \approx 1 7 . 1 7 4 8 0 .$

Actual values are

$$
y ( 1 . 0 4 ) = 0 . 1 1 9 9 8 7 5 , \quad y ( 1 . 5 5 ) = 4 . 7 8 8 6 3 5 \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) = 1 7 . 2 7 9 3 0 .
$$

(c) Taylor’s method of order four gives the results in the following table.

<table><tr><td>i ti</td><td>Wi</td></tr><tr><td>1</td><td>1.1 0.3459127</td></tr><tr><td>5</td><td>1.5 3.967603</td></tr><tr><td>6</td><td>5.720875</td></tr><tr><td>9</td><td>1.6 1.9 14.32290</td></tr><tr><td>10</td><td>2.0 18.68287</td></tr></table>

(d) Cubic Hermite interpolation gives

$$
y ( 1 . 0 4 ) \approx 0 . 1 1 9 9 7 0 4 , \quad y ( 1 . 5 5 ) \approx 4 . 7 8 8 5 2 7 , \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) \approx 1 7 . 2 7 9 0 4 .
$$

10. (a) Taylor’s method of order two gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9525000</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9093138</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6459788</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6258649</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.5139781</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.5011957</td><td>-0.5000000</td></tr></table>

(b) Linear interpolation gives

$y ( 1 . 0 5 2 ) \approx - 0 . 9 5 0 7 7 2 6 , \quad y ( 1 . 5 5 5 ) \approx - 0 . 6 4 3 9 6 7 4 ,$ and $y ( 1 . 9 7 8 ) \approx - 0 . 5 0 6 8 1 9 9$

Actual values are

y(1.052) = −0.9505703, $y ( 1 . 5 5 5 ) = - 0 . 6 4 3 0 8 6 8$ , and $y ( 1 . 9 7 8 ) = - 0 . 5 0 5 5 6 1 2$

(c) Taylor’s method of order four gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9523813</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9090914</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6451629</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6250017</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.5128226</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.5000022</td><td>-0.5000000</td></tr></table>

(d) Cubic Hermite interpolation gives

y(1.052) ≈ −0.9505706, y(1.555) ≈ −0.6430884, and $y ( 1 . 9 7 8 ) \approx - 0 . 5 0 5 5 6 3 3$

11. (a) The approximations for the velocity are in the following table.

<table><tr><td>i</td><td>ti</td><td>Order 2</td><td>Order 4</td></tr><tr><td>2</td><td>0.2</td><td>5.86595</td><td>5.86433</td></tr><tr><td>5</td><td>0.5</td><td>2.82145</td><td>2.81789</td></tr><tr><td>7</td><td>0.7</td><td>0.84926</td><td>0.84455</td></tr><tr><td>10</td><td>1.0</td><td>-2.08606</td><td>-2.09015</td></tr></table>

(b) The maximum height occurs at approximately 0.8 s.

12. Taylor’s method of order two gives the following:

<table><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.5</td><td>0.5146389</td></tr><tr><td>5 10</td><td>1.0</td><td>1.249305</td></tr><tr><td>15</td><td>1.5</td><td>2.152599</td></tr><tr><td>20</td><td>2.0</td><td>2.095185</td></tr></table>

# Exercise Set 5.4, page 291

1. The Modified Euler method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>0.5</td><td>0.5602111 0.2836165</td></tr><tr><td>1.0</td><td>5.3014898</td><td>3.2190993</td></tr></table>

<table><tr><td rowspan="3">(b) t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>2.5</td><td>1.8125000</td></tr><tr><td>3.0</td><td>2.4815531</td><td>1.8333333 2.5000000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3"></td></tr><tr><td>t</td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>1.25 1.50</td><td>2.7750000</td><td>2.7789294 3.6081977</td></tr><tr><td>1.75</td><td>3.6008333 4.4688294</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3728586</td><td></td></tr><tr><td></td><td></td><td>5.3862944</td></tr></table>

<table><tr><td rowspan="2">t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>0.25</td><td>1.3199027</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7070300</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0053560</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.0770789</td><td>2.1179795</td></tr></table>

2. The Modified Euler method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) ti</td><td></td><td></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50 1.2181261 1.00 1.4975545</td><td>1.2140231 1.4898801</td></tr></table>

<table><tr><td colspan="2">(b) ti Wi</td><td></td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541667</td><td>2.3541020</td></tr><tr><td>2.00</td><td></td><td>2.7417451</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="2">(c) ti Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2454995</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5671560</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9691945</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4565684</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(d) ti Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4160751</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0310111</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.75226668</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.54324500</td><td>0.52968710</td></tr></table>

3. The Modified Euler method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td></td><td>1.0147137</td><td>1.0149523</td></tr><tr><td></td><td>1.5</td><td>1.0669093</td><td>1.0672624</td></tr><tr><td>1.7</td><td></td><td>1.1102751</td><td>1.1106551</td></tr><tr><td>2.0</td><td></td><td></td><td>1.1812322</td></tr><tr><td></td><td></td><td>1.1808345</td><td></td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td colspan="2">Modified Euler</td></tr><tr><td rowspan="2"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td colspan="2"></td><td></td></tr><tr><td>2.0</td><td>1.4</td><td>0.4850495 1.6384229</td><td>0.4896817 1.6612818</td></tr><tr><td>2.4</td><td></td><td>2.8250651</td><td>2.8765514</td></tr><tr><td>3.0</td><td></td><td>5.7075699</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6229206</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2442903</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1200763</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0391938</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1742708</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2878200</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5088359</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0096377</td><td>1.0022460</td></tr></table>

4. The Modified Euler method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.597265955</td><td>1.6</td></tr><tr><td>0.6</td><td>1.615015699</td><td>1.617647059</td></tr><tr><td>0.9</td><td>1.545108042</td><td>1.546961326</td></tr><tr><td>1.0</td><td>1.498430678</td><td>1.5</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347996027</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268565970</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9395411781</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9105471247</td><td>-0.9102392264</td></tr></table>

<table><tr><td></td><td colspan="4"></td><td></td></tr><tr><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.72</td><td>-1.714285714</td><td>0.5</td><td>1.289770701</td><td>1.289805276</td></tr><tr><td>1.4</td><td>-1.561272503</td><td>-1.555555556</td><td>0.6</td><td>1.380583709</td><td>1.380931216</td></tr><tr><td>2.8</td><td>-1.219717333</td><td>-1.217391304</td><td>0.9</td><td>1.631230851</td><td>1.632613182</td></tr><tr><td>3.0</td><td>-1.202119310</td><td>-1.2</td><td>1.0</td><td>1.700210296</td><td>1.701870053</td></tr></table>

5. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="2">(a) t</td><td>y(t)</td></tr><tr><td></td><td>Midpoint 0.2646250</td><td></td></tr><tr><td>0.5 1.0</td><td>3.1300023</td><td>0.2836165 3.2190993</td></tr></table>

<table><tr><td rowspan="3">(b) t</td><td colspan="2"></td></tr><tr><td>Midpoint</td><td>y(t)</td></tr><tr><td>2.5 1.7812500</td><td>1.8333333</td></tr><tr><td>3.0</td><td>2.4550638</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="2">C</td><td></td></tr><tr><td rowspan="3">t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>1.25 2.7777778</td><td>2.7789294</td></tr><tr><td>3.6060606</td><td>3.6081977</td></tr><tr><td>1.50 1.75</td><td>4.4763015</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3824398</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="2"></td><td></td></tr><tr><td>t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>0.25</td><td>1.3337962</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7422854</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0596374</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1385560</td><td>2.1179795</td></tr></table>

6. The Midpoint method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) ti</td><td></td><td></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50 1.2154305</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4932390</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2446171</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.562980</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9663178</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4526648</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(b) ti Wi</td><td></td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3552632</td><td>2.3541020</td></tr><tr><td>2.00</td><td></td><td>2.7435126</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4365103</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0516739</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.76935826</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.55667863</td><td>0.52968710</td></tr></table>

7. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="4">(a) Midpoint</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">ti</td></tr><tr><td colspan="4">1.2</td></tr><tr><td colspan="4">1.5</td></tr><tr><td colspan="2">1.7</td><td>1.0677427 1.1111478</td><td>1.0672624 1.1106551</td></tr><tr><td colspan="4">2.0 1.1817275</td></tr></table>

<table><tr><td colspan="2">*（b) Midpoint ti</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>1.4</td><td>0.4861770</td><td>0.4896817</td></tr><tr><td></td><td>2.0</td><td>1.6438889</td><td>1.6612818</td></tr><tr><td></td><td>2.4</td><td>2.8364357</td><td>2.8765514</td></tr><tr><td></td><td>3.0</td><td>5.7386475</td><td>5.8741000</td></tr></table>

<table><tr><td rowspan="7">C ti 0.4</td><td></td></tr><tr><td>Midpoint Wi y(ti)</td></tr><tr><td></td></tr><tr><td>-1.6192966 -1.6200510</td></tr><tr><td>-1.2402470 -1.2384058</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>1.0</td><td></td></tr><tr><td>1.4 -1.1175165</td><td>-1.1146484</td></tr><tr><td>2.0 -1.0382227</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="2">(d) Midpoint</td><td></td></tr><tr><td colspan="3">ti Wi</td></tr><tr><td>0.2</td><td></td><td>y(ti)</td></tr><tr><td>0.5</td><td>0.1722396 0.2848046</td><td>0.1626265 0.2773617</td></tr><tr><td>0.7</td><td>0.5056268</td><td>0.5000658</td></tr><tr><td></td><td></td><td></td></tr><tr><td>1.0</td><td>1.0063347</td><td>1.0022460</td></tr></table>

8. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td>ti</td><td></td><td>Midpoint Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.5</td><td>1.599403030</td><td>1.6</td></tr><tr><td></td><td>0.6</td><td>1.616526285</td><td>1.617647059</td></tr><tr><td></td><td>0.9</td><td>1.544954509</td><td>1.546961326</td></tr><tr><td></td><td>1.0</td><td>1.497941308</td><td>1.5</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3">Midpoint</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.348356626</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.269137742</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9403364427</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9113264950</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="2">(c)</td></tr><tr><td colspan="2">Midpoint</td></tr><tr><td>ti</td><td>Wi y(ti)</td></tr><tr><td>1.2</td><td>-1.738181818 -1.714285714</td></tr><tr><td>1.4 -1.579759806</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.227670824 -1.217391304</td></tr><tr><td>3.0</td><td>-1.209389666 -1.2</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Midpoint Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.5</td><td>1.291506468</td><td>1.289805276</td></tr><tr><td colspan="2">0.6</td><td>1.382581697</td><td>1.380931216</td></tr><tr><td colspan="2">0.9</td><td>1.633368805</td><td>1.632613182</td></tr><tr><td colspan="2">1.0</td><td>1.702247783</td><td>1.701870053</td></tr></table>

9. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50</td><td>0.2710885</td><td>0.2836165</td></tr><tr><td>1.00</td><td>3.1327255</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="3">（b)</td></tr><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td rowspan="2">ti</td><td></td><td>y(ti)</td></tr><tr><td>Wi</td><td></td></tr><tr><td>2.50</td><td>1.8464828</td><td>1.8333333</td></tr><tr><td>3.00</td><td>2.5094123</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>2.7788462</td><td>2.7789294</td></tr><tr><td>1.50</td><td>3.6080529</td><td>3.6081977</td></tr><tr><td>1.75</td><td>4.4791319</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3860533</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.3295717</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7310350</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0417476</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1176975</td><td>2.1179795</td></tr></table>

10. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2139924</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4897542</td><td>1.4898801</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td colspan="2"></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td>2.3540516 2.3541020</td></tr><tr><td>2.00</td><td>2.7415759</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25 2.50</td><td>2.2441050 2.5644270</td><td>2.2441211 2.5644520</td></tr><tr><td>2.75</td><td>2.9651642</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4512546</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="3">d</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.3981322</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0114609</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.7338609</td><td>0.7380098</td></tr><tr><td>2.00</td><td>0.5262880</td><td>0.5296871</td></tr></table>

11. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>1.0149305</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672363</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106289</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812064</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="3">*(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>1.4</td><td>0.4895074</td><td>0.4896817</td></tr><tr><td>2.0</td><td>1.6602954</td><td>1.6612818</td></tr><tr><td>2.4</td><td>2.8741491</td><td>2.8765514</td></tr><tr><td>3.0</td><td>5.8652189</td><td>5.8741000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6201023</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2383500</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1144745</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0357989</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td colspan="4">Heun</td></tr><tr><td rowspan="5"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1614497</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2765100</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.4994538</td><td></td></tr><tr><td>1.0</td><td>1.0018114</td><td>0.5000658 1.0022460</td></tr></table>

12. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.5</td><td>1.599939902</td><td>1.6</td></tr><tr><td colspan="2">0.6</td><td>1.617600330</td><td>1.617647059</td></tr><tr><td colspan="2">0.9</td><td>1.546961530</td><td>1.546961326</td></tr><tr><td colspan="2">1.0</td><td>1.500010266</td><td>1.5</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347797247</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268261121</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9391794862</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9101980983</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.710175817</td><td>-1.714285714</td></tr><tr><td>1.4</td><td>-1.551807512</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.216030469</td><td>-1.217391304</td></tr><tr><td>3.0</td><td>-1.198763172</td><td>-1.2</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.289772720</td><td>1.289805276</td></tr><tr><td>0.6</td><td>1.380888251</td><td>1.380931216</td></tr><tr><td>0.9</td><td>1.632584856</td><td>1.632613182</td></tr><tr><td></td><td></td><td></td></tr><tr><td>1.0</td><td>1.701855837</td><td>1.701870053</td></tr></table>

13. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Runge-Kutta Wi</td><td>y（(ti)</td></tr><tr><td colspan="2">0.5</td><td>0.2969975</td><td>0.2836165</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4">Runge-Kutta</td></tr><tr><td>ti</td><td></td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.5</td><td></td><td>1.8333234</td><td>1.8333333</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>3.0</td><td></td><td>2.4999712</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>2.7789095</td><td>2.7789294</td></tr><tr><td>1.50</td><td>3.6081647</td><td>3.6081977</td></tr><tr><td>1.75</td><td>4.4792846</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3862426</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Runge-Kutta Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.3291650</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7305336</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0415436</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1180636</td><td>2.1179795</td></tr></table>

14. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2140409</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4899213</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2441194</td><td>2.2441211</td></tr><tr><td>2.50 2.75</td><td>2.5644488 2.9651894</td><td>2.5644519 2.9651938</td></tr><tr><td>3.00</td><td>3.4512811</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541032</td><td>2.3541020</td></tr><tr><td></td><td>2.00</td><td>2.7416591</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4033566</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0165586</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.73813168</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.52978556</td><td>0.52968710</td></tr></table>

15. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td rowspan="2">y(ti)</td></tr><tr><td>ti</td><td>Runge-Kutta Wi</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672620</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106547</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812319</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="2">*(b)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Runge-Kutta Wi</td><td>y(ti)</td></tr><tr><td></td><td></td><td>0.4896842</td><td>0.4896817</td></tr><tr><td></td><td>1.4 2.0</td><td>1.6612651</td><td>1.6612818</td></tr><tr><td></td><td>2.4</td><td>2.8764941</td><td>2.8765514</td></tr><tr><td></td><td>3.0</td><td>5.8738386</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td></tr><tr><td colspan="2">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi y(ti)</td></tr><tr><td>0.4</td><td>-1.6200576 -1.6200510</td></tr><tr><td>1.0 -1.2384307</td><td>-1.2384058</td></tr><tr><td>1.4 -1.1146769</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0359922 -1.0359724</td></tr></table>

<table><tr><td colspan="2">(d)</td><td rowspan="2"></td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td></td><td>ti</td><td>Wi</td></tr><tr><td>0.2</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2774767</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5001579</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0023207</td><td>1.0022460</td></tr></table>

16. The Runge-Kutta method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.599998664</td><td>1.6</td></tr><tr><td>0.6</td><td>1.617645445</td><td>1.617647059</td></tr><tr><td>0.9</td><td>1.546959536</td><td>1.546961326</td></tr><tr><td>1.0</td><td>1.499998299</td><td>1.5</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347822676</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268299357</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9392221816</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9102391733</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.714245180</td><td>-1.714285714</td></tr><tr><td>1.4</td><td>-1.555522884</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.217380872</td><td>-1.217391304</td></tr><tr><td>3.0</td><td>-1.199990539</td><td>-1.2</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.289807149</td><td>1.289805276</td></tr><tr><td>0.6</td><td>1.380932547</td><td>1.380931216</td></tr><tr><td>0.9</td><td>1.632611867</td><td>1.632613182</td></tr><tr><td>1.0</td><td>1.701867708</td><td>1.701870053</td></tr></table>

17. Linear interpolation gives the following results.

(a) $1 . 0 2 2 1 1 6 7 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 0 3 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 0 8 6 5 0 0 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , \ 4 . 3 1 0 5 9 1 3 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 6 1 4 3 4 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8$ , $- 1 . 0 4 5 4 8 5 4 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 2 7 1 4 7 0 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8$ , $0 . 8 9 6 7 0 7 3 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

18. Linear interpolation gives the following results.

(a) $1 . 6 0 4 3 6 5 8 5 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 6 4 3 7 0 9 6 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 7 4 6 0 6 2 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 0 8 4 2 9 6 2 1 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 4 0 6 3 6 2 5 2 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 8 2 7 8 6 1 8 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 0 9 5 9 0 4 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ , $1 . 6 5 8 8 2 2 6 2 9 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

19. Linear interpolation gives the following results.

(a) $1 . 0 2 2 7 8 6 3 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 9 2 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 1 5 3 7 4 9 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , ~ 4 . 3 3 1 2 9 3 9 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 3 2 0 7 0 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 4 3 7 4 3 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 2 4 0 8 3 9 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , \ 0 . 8 9 3 4 1 5 2 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

20. Linear interpolation gives the following results.

(a) $1 . 6 0 5 2 5 2 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 6 1 4 9 2 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 5 3 7 9 3 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 1 6 3 3 4 6 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 5 8 9 7 0 8 \approx y ( 1 . 3 ) = - 1 . 6 2 5 , \ : \ : - 1 . 2 1 5 7 8 8 1 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 7 9 3 6 6 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2 .$ , $1 . 6 6 0 9 2 0 4 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

21. Linear interpolation gives the following results.

(a) $1 . 0 2 2 3 5 9 8 5 0 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 4 0 3 7 0 6 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 8 8 0 8 4 8 0 4 9 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6$ , $4 . 4 0 8 4 2 6 1 1 5 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 0 3 4 6 9 5 6 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 1 8 2 0 2 5 6 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 1 6 2 5 6 9 8 9 7 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , \ 0 . 8 8 8 6 6 1 3 4 2 6 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

22. Linear interpolation gives the following results.

(a) $1 . 6 0 7 0 0 4 0 7 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8 , \ 1 . 5 2 8 1 8 1 0 2 4 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 4 1 3 9 2 9 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- . 9 3 0 4 8 5 0 6 9 8 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 3 0 9 9 1 6 6 4 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 4 8 0 6 7 2 6 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 2 1 8 9 3 2 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ , $1 . 6 6 0 2 9 3 2 4 8 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

23. Linear interpolation gives the following results.

(a) $1 . 0 2 2 3 8 2 6 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 4 2 9 2 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 3 7 3 6 7 2 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6$ , $4 . 4 1 3 4 7 4 5 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 0 5 2 5 2 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 2 0 2 1 1 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 1 7 1 6 5 2 6 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8$ , $0 . 8 8 9 1 9 7 3 0 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

24. Linear interpolation gives the following results.

(a) $1 . 6 0 7 0 5 7 3 7 6 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 8 1 7 5 0 4 1 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 4 5 5 2 3 8 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 0 5 2 7 2 7 9 1 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 3 4 8 8 4 0 3 2 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 6 0 7 7 1 5 6 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 2 5 7 3 0 8 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ $9 6 8 5 2 , 1 . 6 6 0 3 1 4 2 0 3 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 .$ 1

25. Cubic Hermite interpolation gives the following results.

(a) $1 . 0 2 1 9 5 6 9 = y ( 1 . 2 5 ) \approx 1 . 0 2 1 9 5 5 0$ , $1 . 1 6 4 3 9 0 2 = y ( 1 . 9 3 ) \approx 1 . 1 6 4 3 8 9 8$ \*(b) $1 . 9 2 4 9 6 1 7 = y ( 2 . 1 0 ) \approx 1 . 9 2 4 9 2 1 7 ,$ $4 . 3 9 4 1 6 9 7 = y ( 2 . 7 5 ) \approx 4 . 3 9 3 9 9 4 3$ (c) $- 1 . 1 3 8 2 6 8 = y ( 1 . 3 ) \approx - 1 . 1 3 8 3 0 3 6$ , $- 1 . 0 4 1 2 6 6 6 = y ( 1 . 9 3 ) \approx - 1 . 0 4 1 2 8 6 2$ (d) $0 . 3 1 4 0 0 1 8 4 = y ( 0 . 5 4 ) \approx 0 . 3 1 4 1 0 5 7 9 , 0 . 8 8 6 6 3 1 7 6 = y ( 0 . 9 4 ) \approx 0 . 8 8 6 7 0 6 5 3$

26. Cubic Hermite interpolation gives the following results.

(a) $1 . 6 1 0 4 0 3 1 0 8 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 8 9 8 7 6 2 2 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 3 1 4 9 6 2 0 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1 , \ : \ : - 0 . 9 3 0 2 3 0 2 4 7 4 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4 7 3 . \ : ( 1 . 9 3 3 )$ (c) $- 1 . 6 2 4 8 0 6 7 4 6 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 1 4 6 4 2 6 0 1 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 1 9 5 3 9 0 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2 , 1 . 6 6 1 3 5 8 5 5 8 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

27. The Modified Euler method and the Midpoint method give the same results when applied to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) = - y + t + 1 , \quad \mathrm { f o r } \quad 0 \leq t \leq 1 \quad \mathrm { a n d } \quad y ( 0 ) = 1
$$

with any choice of $h$ because the equation is linear in both $y$ and $t$ .

The equation for the Midpoint method has $w _ { 0 } = 1$ and

$$
\begin{array} { r l } & { w _ { i + 1 } = w _ { i } + h f ( t _ { i } + 0 . 5 h , w _ { i } + 0 . 5 h f ( t _ { i } , w _ { i } ) ) } \\ & { \qquad = w _ { i } + h f ( t _ { i } + 0 . 5 h , w _ { i } + 0 . 5 h ( - w _ { i } + t _ { i } + 1 ) ) } \\ & { \qquad = w _ { i } + h ( - w _ { i } - 0 . 5 h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + 0 . 5 h + 1 ) } \\ & { \qquad = w _ { i } ( 1 - h + 0 . 5 h ^ { 2 } ) + t _ { i } ( h - 0 . 5 h ^ { 2 } ) + h . } \end{array}
$$

The equation for the Modified Euler method has $w _ { 0 } = 1$ and

$$
\begin{array} { l } { w _ { i + 1 } = w _ { i } + 0 . 5 h \big ( f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i } + h f ( t _ { i } , w _ { i } ) \big ) } \\ { \qquad = w _ { i } + 0 . 5 h \big ( - w _ { i } + t _ { i } + 1 - w _ { i } - h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + h + 1 \big ) } \\ { \qquad = w _ { i } + 0 . 5 h \big ( - w _ { i } + t _ { i } + 1 - w _ { i } - h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + h + 1 \big ) } \\ { \qquad = w _ { i } ( 1 - h + 0 . 5 h ^ { 2 } ) + t _ { i } ( h - 0 . 5 h ^ { 2 } ) + h . } \end{array}
$$

28. (a) The water level is 6.526747 ft. (b) The tank will be empty in 25 min.

29. In 0.2 seconds we have approximately 2099 units of KOH.

$^ *$ 30. Using the notation $y _ { i + 1 } = y ( t _ { i + 1 } )$ , $y _ { i } = y ( t _ { i } )$ , and $f _ { i } = f ( t _ { i } , y ( t _ { i } ) )$ , we have

$$
h \tau _ { i + 1 } = y _ { i + 1 } - y _ { i } - a _ { 1 } f _ { i } - a _ { 2 } f ( t _ { i } + \alpha _ { 2 } , y _ { i } + \delta _ { 2 } f _ { i } ) .
$$

Expanding $y _ { i + 1 }$ and $f ( t _ { i } + \alpha _ { 2 } , y _ { i } + \delta _ { 2 } f _ { i } )$ in Taylor series about $t _ { i }$ and $f ( t _ { i } , y _ { i } )$ gives

$$
\begin{array} { r l } { h \tau _ { + 1 } = ( h - a _ { 1 } - a _ { 2 } ) f _ { i } + \frac { h ^ { 2 } } { 2 } \int _ { - } ^ { t } d \sigma _ { 2 } c _ { 2 } f _ { i } ( i _ { 2 } , y _ { i } ) } \\ { - \sigma _ { 2 } \dot { \sigma } _ { 2 } f _ { i } \dot { \sigma } _ { 1 } ( i _ { 2 } , y _ { i } ) + \frac { h ^ { 3 } } { 6 } \int _ { - } ^ { t } d \sigma _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { - \sigma _ { 2 } \sigma _ { 2 } \dot { \sigma } _ { 2 } f _ { i } f _ { i } ( i _ { 4 } , y _ { i } ) - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \int _ { - } ^ { t } d \sigma _ { 2 } ( i _ { 2 } , y _ { i } ) + i \cdots } \\ { = ( h - a _ { 1 } - a _ { 2 } ) f _ { i } + \bigg ( \frac { h ^ { 2 } } { 2 } - a _ { 2 } \sigma _ { 2 } \bigg ) f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \bigg ( \frac { h ^ { 2 } } { 2 } - a _ { 2 } \dot { \sigma } _ { 2 } \bigg ) f _ { i } f _ { i } ( i _ { 4 } , y _ { i } ) + \bigg ( \frac { h ^ { 3 } } { 6 } - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \bigg ) f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \bigg ( \frac { h ^ { 3 } } { 8 } - a _ { 2 } \sigma _ { 2 } \dot { \sigma } _ { 2 } \bigg ) f _ { i } f _ { i } \dot { \sigma } _ { 1 } ( i _ { 4 } , y _ { i } ) + \bigg ( \frac { h ^ { 3 } } { 6 } - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \bigg ) f _ { i } ^ { 2 } f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \frac { h ^ { 3 } } { 6 } \left( f _ { i } ( i _ { 4 } , y _ { i } ) f _ { i } ( i _ { 4 } , y _ { i } ) + f _ { i } ^ { 2 } f _ { i } ^ { 2 } ( i _ { 5 } , y _ { i } ) \right) + \cdots } \end{array}
$$

Regardless of the choice of $u _ { 1 } , u _ { 2 } , \alpha _ { 2 }$ , and $\delta _ { 2 }$ , the term

$$
\frac { h ^ { 3 } } { 6 } \left[ f _ { t } ( y _ { i } , t _ { i } ) f _ { y } ( t _ { i } , y _ { i } ) + f _ { i } f _ { y } ^ { 2 } ( t _ { i } , y _ { i } ) \right]
$$

cannot be canceled.

31. The appropriate constants are

$$
\alpha _ { 1 } = \delta _ { 1 } = \alpha _ { 2 } = \delta _ { 2 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma _ { 4 } = \gamma _ { 5 } = \gamma _ { 6 } = \gamma _ { 7 } = \frac { 1 } { 2 } \quad \mathrm { a n d } \quad \alpha _ { 3 } = \delta _ { 3 } = 1 .
$$

# Exercise Set 5.5, page 300

1. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2093900</td><td>0.0298184</td><td>0.2093900</td><td>0.0298337</td></tr><tr><td>3</td><td>0.5610469</td><td>0.4016438</td><td>0.1777496</td><td>0.4016860</td></tr><tr><td>5</td><td>0.8387744</td><td>1.5894061</td><td>0.1280905</td><td>1.5894600</td></tr><tr><td>7</td><td>1.0000000</td><td>3.2190497</td><td>0.0486737</td><td>3.2190993</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>2.2500000</td><td>1.4499988</td><td>0.2500000</td><td>1.4500000</td></tr><tr><td>2</td><td>2.5000000</td><td>1.8333332</td><td>0.2500000</td><td>1.8333333</td></tr><tr><td>3</td><td>2.7500000</td><td>2.1785718</td><td>0.2500000</td><td>2.1785714</td></tr><tr><td>4</td><td>3.0000000</td><td>2.5000005</td><td>0.2500000</td><td>2.5000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.2500000</td><td>2.7789299</td><td>0.2500000</td><td>2.7789294</td></tr><tr><td>2</td><td>1.5000000</td><td>3.6081985</td><td>0.2500000</td><td>3.6081977</td></tr><tr><td>3</td><td>1.7500000</td><td>4.4793288</td><td>0.2500000</td><td>4.4793276</td></tr><tr><td>4</td><td>2.0000000</td><td>5.3862958</td><td>0.2500000</td><td>5.3862944</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2500000</td><td>1.3291478</td><td>0.2500000</td><td>1.3291498</td></tr><tr><td>2</td><td>0.5000000</td><td>1.7304857</td><td>0.2500000</td><td>1.7304898</td></tr><tr><td>3</td><td>0.7500000</td><td>2.0414669</td><td>0.2500000</td><td>2.0414720</td></tr><tr><td>4</td><td>1.0000000</td><td>2.1179750</td><td>0.2500000</td><td>2.1179795</td></tr></table>

2. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.0500000</td><td>1.1038574</td><td>0.0500000</td><td>1.1038574</td></tr><tr><td>2</td><td>1.1000000</td><td>1.2158864</td><td>0.0500000</td><td>1.2158863</td></tr><tr><td>3</td><td>1.1500000</td><td>1.3368393</td><td>0.0500000</td><td>1.3368393</td></tr><tr><td>4</td><td>1.2000000</td><td>1.4675697</td><td>0.0500000</td><td>1.4675696</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2500000</td><td>0.2522868</td><td>0.2500000</td><td>0.2522868</td></tr><tr><td>2</td><td>0.5000000</td><td>0.5158867</td><td>0.2500000</td><td>0.5158868</td></tr><tr><td>3</td><td>0.7500000</td><td>0.7959445</td><td>0.2500000</td><td>0.7959446</td></tr><tr><td>4</td><td>1.0000000</td><td>1.0918182</td><td>0.2500000</td><td>1.0918183</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.1382206</td><td>-1.7834313</td><td>0.1382206</td><td>-1.7834282</td></tr><tr><td>3</td><td>1.6364797</td><td>-1.4399709</td><td>0.3071709</td><td>-1.4399551</td></tr><tr><td>5</td><td>2.6364797</td><td>-1.2340532</td><td>0.5000000</td><td>-1.2340298</td></tr><tr><td>6</td><td>3.0000000</td><td>-1.2000195</td><td>0.3635203</td><td>-1.2000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.5000000</td><td>0.0416667</td><td>0.5000000</td><td>0.0416667</td></tr><tr><td>2</td><td>1.0000000</td><td>0.3333333</td><td>0.5000000</td><td>0.3333333</td></tr><tr><td>3</td><td>1.5000000</td><td>1.1250000</td><td>0.5000000</td><td>1.1250000</td></tr><tr><td>4</td><td>2.0000000</td><td>2.6666667</td><td>0.5000000</td><td>2.6666667</td></tr></table>

3. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.1101946</td><td>1.0051237</td><td>0.1101946</td><td>1.0051237</td></tr><tr><td>5</td><td>1.7470584</td><td>1.1213948</td><td>0.2180472</td><td>1.1213947</td></tr><tr><td>7</td><td>2.3994350</td><td>1.2795396</td><td>0.3707934</td><td>1.2795395</td></tr><tr><td>11</td><td>4.0000000</td><td>1.6762393</td><td>0.1014853</td><td>1.6762391</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>4</td><td>1.5482238</td><td>0.7234123</td><td>0.1256486</td><td>0.7234119</td></tr><tr><td>7</td><td>1.8847226</td><td>1.3851234</td><td>0.1073571</td><td>1.3851226</td></tr><tr><td>10</td><td>2.1846024</td><td>2.1673514</td><td>0.0965027</td><td>2.1673499</td></tr><tr><td>16</td><td>2.6972462</td><td>4.1297939</td><td>0.0778628</td><td>4.1297904</td></tr><tr><td>21</td><td>3.0000000</td><td>5.8741059</td><td>0.0195070</td><td>5.8741000</td></tr></table>