# 327 Methods of orders greater than 6

Methods with order 7 must have at least nine stages. It is possible to construct such a method using the principles of Subsection 323, extending the approach used in Subsection 326. The abscissa vector is chosen as

$$
\begin{array} { r } { c = [ 0 \quad \frac { 1 } { 3 } c _ { 4 } \quad \frac { 2 } { 3 } c _ { 4 } \quad c _ { 4 } \quad c _ { 5 } \quad c _ { 6 } \quad c _ { 7 } \quad 0 \quad 1 ] ^ { \intercal } , } \end{array}
$$

and the orders of stages numbered $4 , 5 , \dots , 9$ are forced to be 3. To achieve consistency of the conditions

$$
\begin{array} { c } { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } a _ { j k } c _ { k } ( c _ { k } - c _ { 4 } ) ( c _ { k } - c _ { 5 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 4 \cdot 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } } { 3 \cdot 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 3 \cdot 4 \cdot 5 } , } } \\ { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) ( c _ { j } - c _ { 6 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } + c _ { 6 } } { 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } + c _ { 4 } c _ { 6 } + c _ { 5 } c _ { 6 } } { 3 \cdot 4 \cdot 5 } - \frac { c _ { 4 } c _ { 5 } c _ { 6 } } { 2 \cdot 3 \cdot 4 } , } } \\ { { { } } } \\ { { \displaystyle \sum b _ { i } ( 1 - c _ { i } ) c _ { i } a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) = \frac { 1 } { 4 \cdot 6 \cdot 7 } - \frac { c _ { 4 } } { 3 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 4 \cdot 5 } } } \end{array}
$$

it is found that

$$
c _ { 6 } = \frac { u - 1 2 v + 7 u v } { 3 - 1 2 u + 2 4 v + 1 4 u ^ { 2 } - 7 0 u v + 1 0 5 v ^ { 2 } } ,
$$

where $u = c _ { 4 } + c _ { 5 }$ and $v = c _ { 4 } c _ { 5 }$ . The value of $c _ { 7 }$ is selected to ensure that

$$
\int _ { 0 } ^ { 1 } x ( 1 - x ) ( x - c _ { 4 } ) ( x - c _ { 5 } ) ( x - c _ { 6 } ) ( x - c _ { 7 } ) d x = 0 .
$$

The tableau for a possible method derived along these lines is

<table><tr><td>0 G</td><td rowspan="16"></td><td colspan="2"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td></tr><tr><td>1 0</td><td>1</td><td></td></tr><tr><td>1</td><td>0 3</td><td></td></tr><tr><td></td><td>0 150</td><td></td></tr><tr><td></td><td>148 0</td><td>1331</td><td>56</td><td></td><td></td></tr><tr><td></td><td>1331 404</td><td>170</td><td>1331</td><td></td><td></td></tr><tr><td></td><td>243</td><td>27</td><td>4024 1701</td><td>10648</td><td></td></tr><tr><td></td><td>2466</td><td>1242</td><td>19176</td><td>1701 51909</td><td>1053</td></tr><tr><td></td><td>2401</td><td>0 343</td><td>16807</td><td></td><td></td></tr><tr><td>0</td><td>5</td><td>0</td><td></td><td>96</td><td>16807 1815</td><td>2401 405</td><td>49</td></tr><tr><td></td><td>154</td><td></td><td>0</td><td>539</td><td>20384</td><td>2464</td><td>1144</td></tr><tr><td>1</td><td>113</td><td>0</td><td>195</td><td>32</td><td>29403</td><td>729</td><td>1029 21</td></tr><tr><td></td><td>32</td><td></td><td>22</td><td></td><td></td><td>512</td><td>1408</td></tr><tr><td></td><td></td><td></td><td></td><td>7</td><td>3584</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>32</td><td>1771561</td><td>243</td><td>16</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td>16807 77</td></tr><tr><td></td><td></td><td></td><td></td><td>105</td><td>6289920</td><td>2560</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>74880</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1440</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Order 8 requires 11 stages, and methods of this order were derived by Curtis (1970)and Cooper and Verner (1972). In each case the abscissae were based on the Lobatto quadrature formula with three internal points. We quote the method of Cooper and Verner in Table 327(I).

Although order 9 has not attracted much interest, and it is unknown how many stages are required to achieve this order, order 10 has posed a challenge. In Curtis (1975) a method of order 10 was presented with 18 stages. However, using an ingenious combination of various simplifying assumptions, Hairer (1978) accomplished this feat in 17 stages. It is still not known if fewer stages are possible.

# Exercises 32

32.1 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 2 } } } , 1 ]$ .

32.2 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 3 } } } , 1 ]$ .

32.3 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $\textstyle c _ { 2 } = { \frac { 1 } { 5 } }$ .

32.4 Find a method with $s = p = 4$ such that $b _ { 2 } = 0$ and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ .

32.5 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $c _ { 3 } = 0$ .

32.6 Show that Lemma 322A can be used to prove that $c _ { 4 } = 1$ , if $s = p \geq 4$ .

32.7 Show that Lemma 322A can be used to prove that $c _ { 5 } = 1$ , if $s = p \geq 5$ leading to an alternative proof of Theorem 324B.

<table><tr><td>% 08I I 6</td><td>贵</td><td>08 6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>81 12-65</td><td>亚 227281</td><td>Z</td><td>2 2223125533173153111</td><td>业 18781</td><td>81 2+2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>I</td></tr><tr><td></td><td>2</td><td>99</td><td>509</td><td>2555</td><td></td><td></td><td></td><td></td><td>红</td><td>V</td></tr><tr><td></td><td></td><td>2173121111111-1113171112111311111-1111</td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>T</td><td>1+2</td></tr><tr><td></td><td></td><td>82 35533211</td><td>1111 12712188</td><td>兴</td><td>99 110-16</td><td>0</td><td>0</td><td>0</td><td>2 T</td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td>I</td></tr><tr><td></td><td></td><td></td><td></td><td>1213531</td><td>1241</td><td>0</td><td>0</td><td>0</td><td>T</td><td>1A-2</td></tr><tr><td></td><td></td><td></td><td></td><td>0</td><td>0 1271111451</td><td>06</td><td>118 227222231</td><td>0</td><td>W</td><td>V</td></tr><tr><td></td><td></td><td></td><td></td><td>32731351</td><td></td><td>3575555315</td><td></td><td></td><td>-01</td><td>1-2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>08 122-99</td><td>098 22245223111</td><td>9 1+6</td><td>0</td><td>8</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+9</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>222</td><td>9 1+81</td><td>0</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>-2</td><td>6</td><td>86</td><td>+</td><td>+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+1</td><td>120-2-</td><td>1</td><td>1+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>
