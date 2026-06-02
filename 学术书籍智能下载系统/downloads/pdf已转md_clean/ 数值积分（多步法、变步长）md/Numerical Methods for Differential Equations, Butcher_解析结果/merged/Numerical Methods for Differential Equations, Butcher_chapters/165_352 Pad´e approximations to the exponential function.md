# 352 Pad´e approximations to the exponential function

Given a function $f$ , assumed to be analytic at zero, with $f ( 0 ) \neq 0$ , and given non-negative integers $\it l$ and $m$ , it is sometimes possible to approximate $f$ by a rational function

$$
f ( z ) \approx { \frac { N ( z ) } { D ( z ) } } ,
$$

with $N$ of degree $\it l$ and $D$ of degree $m$ and with the error in the approximation equal to $O ( z ^ { l + m + 1 } )$ . In the special case $m = 0$ , this is exactly the Taylor expansion of $f$ about $z ~ = ~ 0$ , and when $\mathit { l } \mathit { \Theta } = \mathit { \Theta } 0$ , $D ( z ) / N ( z )$ is the Taylor expansion of $1 / f ( z )$ .

For some specially contrived functions and particular choices of the degrees $\it l$ and $m$ , the approximation will not exist. An example of this is

$$
f ( z ) = 1 + \sin ( z ) \approx 1 + z - { \frac { 1 } { 6 } } z ^ { 3 } + \cdots ,
$$

with $l = 2$ , $m = 1$ because it is impossible to choose $a$ to make the coefficient of $z ^ { 3 }$ equal to zero in the Taylor expansion of $( 1 + a z ) f ( z )$ .

When an approximation

$$
f ( z ) = \frac { N _ { l m } ( z ) } { D _ { l m } ( z ) } + O ( z ^ { l + m + 1 } )
$$

exists, it is known as the ‘ $( l , m )$ Pad´e approximation’ to $f$ . The array of Pad´e approximations for $l , m = 0 , 1 , 2 , \ldots$ is referred to as ‘the Pad´e table’ for the function $f$ .

Pad´e approximations to the exponential function are especially interesting to us, because some of them are equal to the rational functions of some important Gauss, Radau and Lobatto methods. We show that the full Pad´e table exists for this function and, at the same time, we find explicit values for the coefficients in $N$ and $D$ and for the next two terms in the Taylor series for $N ( z ) - \exp ( z ) D ( z )$ . Because it is possible to rescale both $N$ and $D$ by an arbitrary factor, we specifically choose a normalization for which $N ( 0 ) = D ( 0 ) = 1$ .

Theorem 352A Let $l , m \geq 0$ be integers and define polynomials $N _ { l m }$ and $D _ { l m }$ by

$$
\begin{array} { l } { { \displaystyle N _ { l m } ( z ) = \frac { l ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { l } \frac { ( l + m - i ) ! } { i ! ( l - i ) ! } z ^ { i } , } } \\ { { \displaystyle D _ { l m } ( z ) = \frac { m ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { m } \frac { ( l + m - i ) ! } { i ! ( m - i ) ! } ( - z ) ^ { i } . } } \end{array}
$$

Also define

$$
C _ { l m } = ( - 1 ) ^ { m } \frac { l ! m ! } { ( l + m ) ! ( l + m + 1 ) ! } .
$$

Then

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + \frac { m + 1 } { l + m + 2 } C _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) .
$$

Proof. In the case $m = 0$ , the result is equivalent to the Taylor series for $\exp ( z )$ ; by multiplying both sides of (352d) by $\exp ( - z )$ we find that the result is also equivalent to the Taylor series for $\exp ( - z )$ in the case ${ \mathit { l } } = 0$ . We now suppose that $l \geq 1$ and $m \geq 1$ , and that (352d) has been proved if $\it l$ is replaced by ${ \mathit { l } } - 1$ or $m$ replaced is by $m - 1$ . We deduce the result for the given values of $\it l$ and $m$ so that the theorem follows by induction.

Because the result holds with $\it l$ replaced by ${ \mathit { l } } - 1$ or with $m$ replaced by $m - 1$ , we have

$$
\begin{array} { r l r } & { } & { N _ { l - 1 , m } ( z ) - \exp ( z ) D _ { l - 1 , m } ( z ) + \left( 1 + \frac { m + 1 } { l + m + 1 } z \right) C _ { l - 1 , m } z ^ { l + m } = O ( z ^ { l + m + 2 } ) , } \\ & { } & { ( 3 5 2 } \\ & { } & { N _ { l , m - 1 } ( z ) - \exp ( z ) D _ { l , m - 1 } ( z ) + \left( 1 + \frac { m } { l + m + 1 } z \right) C _ { l , m - 1 } z ^ { l + m } = O ( z ^ { l + m + 2 } ) . } \end{array}
$$

Multiply (352e) by $l / ( l + m )$ and (352f) by $m / ( l + m )$ , and we find that the coefficient of $z ^ { l + m }$ has the value

$$
\frac { l } { l + m } C _ { l - 1 , m } + \frac { m } { l + m } C _ { l , m - 1 } = 0 .
$$

The coefficient of $z ^ { l + m + 1 }$ is found to be equal to $C _ { l m }$ . Next we verify that

$$
\frac { l } { l + m } N _ { l - 1 , m } ( z ) + \frac { m } { l + m } N _ { l , m - 1 } ( z ) - N _ { l m } ( z ) = 0
$$

and that

$$
\frac { l } { l + m } D _ { l - 1 , m } ( z ) + \frac { m } { l + m } D _ { l , m - 1 } ( z ) - D _ { l m } ( z ) = 0 .
$$

Pad´e approximations $N _ { l m } / D _ { l m }$ for $l , m = 0 , 1 , 2 , 3$   

<table><tr><td>m</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>1</td><td>1+z</td><td>1+z+ 1 22 2</td><td>1+z+ 1 + 6 1 2 心 23</td></tr><tr><td>1</td><td>1 1-x</td><td>1+ 1 之</td><td>1+ 2 z+ 1 6</td><td>1+ 3 2 + 1 之 2 + 1 4 4 24 </td></tr><tr><td>2</td><td>1</td><td>1- 1+ </td><td>1 2 1+ z+ 1 2</td><td>1 4 z 1+ 3 z+ 3 2 2 + 1</td></tr><tr><td></td><td>1-z+ 1 22</td><td>1- 2 z+ T 22</td><td>12 1- 1 z+ 1 22 12</td><td>20 60 2 z+ 20 1 22</td></tr><tr><td>3</td><td>1</td><td></td><td>1+ 2 z+ 1 20 2</td><td>1+ 1 z+ 1 × 1 2 2</td></tr><tr><td></td><td></td><td></td><td></td><td>10 120</td></tr><tr><td></td><td>1 1-z+ 2 22 2</td><td>1- 4 22 1 23 24</td><td>3 z+ 3 22 23 20 60</td><td>1- 1 z+ 10 22 120 23</td></tr></table>

The coefficient of $z ^ { i }$ in (352g) is

$$
\frac { ( l - 1 ) ! ( l + m - i - 1 ) ! } { ( l + m ) ! i ! ( l - i ) ! } \big ( l ( l - i ) + m l - l ( l + m - i ) \big ) = 0 ,
$$

so that (352g) follows. The verification of (352h) is similar and will be omitted. It now follows that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + { \frac { m + 1 } { l + m + 2 } } \widetilde { C } _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) ,
$$

and we finally need to prove that $\widetilde { C } _ { l m } = C _ { l m }$ . Operate on both sides of (352i) with the operator $( d / d z ) ^ { l + 1 }$ and multiply the result by $\exp ( - z )$ . This gives

$$
\begin{array} { r } { P ( z ) + \left( \frac { m + 1 } { l + m + 2 } \frac { ( l + m + 2 ) ! } { ( m + 1 ) ! } \widetilde { C } _ { l m } - \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } \right) z ^ { m + 1 } = O ( z ^ { m + 2 } ) , } \end{array}
$$

where $P$ is the polynomial of degree $m$ given by

$$
P ( z ) = \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } z ^ { m } - \left( 1 + \frac { d } { d z } \right) ^ { l + 1 } D _ { l m } ( z ) .
$$

It follows from (352j) that $\widetilde { C } _ { l m } = C _ { l m }$ .

The formula we have found for a possible $( l , m )$ Pad´e approximation to $\exp ( z )$ is unique. This is not the case for an arbitrary function $f$ , as the example of the function given by (352a) shows; the $( 2 , 1 )$ approximation is not unique. The case of the exponential function is covered by the following result:

Theorem 352B The function $N _ { l m } / D _ { l m }$ , where the numerator and denominator are given by (352b) and (352c), is the unique $( l , m )$ Pad´e approximation to the exponential function.

Proof. If $\hat { N } _ { l m } / \hat { D } _ { l m }$ is a second such approximation then, because these functions differ by $O ( z ^ { l + m + 1 } )$ ,

$$
N _ { l m } \widehat { D } _ { l m } - \widehat { N } _ { l m } D _ { l m } = 0 ,
$$

Diagonal members of the Pad´e table $N _ { m m } / D _ { m m }$ for $m = 0 , 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td></td><td></td><td></td><td>Nmm Dmm</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td>1+</td><td>1 1</td></tr><tr><td>1</td><td></td><td>1 1 × 2</td><td>1 2 z 2 12</td><td></td></tr><tr><td>2</td><td></td><td>1 + 1</td><td>1 2 12 1 2 2 1 北</td><td>心</td></tr><tr><td>3</td><td></td><td>1 1 z 1 22 10</td><td>10</td><td>120 2 1 120 2</td></tr><tr><td>4</td><td></td><td>1 X 1 z + 28 1 3 2 2 比</td><td>3 + 比 28 心</td><td>1 + 1 84 2 1680 24</td></tr><tr><td>5</td><td>1</td><td>X 1 2 1 1 + 北 72</td><td>1 30240 6 25</td><td>84 2</td><td>1680 1 1008</td></tr><tr><td></td><td>1</td><td>125 1 2 + 一</td><td>22</td><td>1 + 72 20 1</td><td>1 1 1008 2 30240 1</td></tr><tr><td>6</td><td>1 + Z 1 2 1 2</td><td>1 44 北 66 5 1</td><td>66 23 </td><td>× 792 1 792 24 </td><td>× 15840 1 + 15840 25 1 1 × 25</td></tr></table>

because the expression on the left-hand side is $O ( z ^ { l + m + 1 } )$ , and is at the same time a polynomial of degree not exceeding $\boldsymbol { l } + \boldsymbol { m }$ . Hence, the only way that two distinct approximations can exist is when they can be cancelled to a rational function of lower degrees. This means that for some $( l , m )$ pair, there exists a Pad´e approximation for which the error coefficient is zero. However, since $\exp ( z )$ is not equal to a rational function, there is some higher exponent $k$ and a non-zero constant $C$ such that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) = C z ^ { k } + O ( z ^ { k + 1 } ) ,
$$

with $k \geq l + m + 2$ . Differentiate (352k) $k - m - 1$ times, multiply the result by $\exp ( - z )$ and then differentiate a further $m + 1$ times. This leads to the contradictory conclusion that $C = 0$ . 

Expressions for the $( l , m )$ Pad´e approximations are given in Table 352(I) for $l , m = 0 , 1 , 2 , 3$ . To extend the information further, Table 352(II) is presented to give the values for $l = m = 0 , 1 , 2 , . . . , 7$ . Similar tables are also given for the first and second sub-diagonals in Tables 352(III) and 352(IV), respectively, and error constants corresponding to entries in each of these three tables are presented in Table 352(V).

First sub-diagonal members of the Pad´e table $N _ { m - 1 , m } / D _ { m - 1 , m }$ for $m = 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-1,m Dm-1,m</td><td colspan="4"></td></tr><tr><td>1</td><td colspan="3"></td><td colspan="2">1 1-z</td><td colspan="4"></td></tr><tr><td>2</td><td colspan="3"></td><td>1+</td><td colspan="2"></td><td colspan="3" rowspan="4"></td></tr><tr><td></td><td></td><td></td><td>2-325</td><td>z 1 2 2 1 北</td><td></td></tr><tr><td>3 4</td><td></td><td>35 2 3 十 20 3 1 + 1 2 + 14</td><td>十 比</td><td>2 比 60 1</td><td>20 </td></tr><tr><td>5</td><td></td><td>2 1 4 2 十</td><td>比 5 5 心 23</td><td>22 1 126</td><td>210 2 105 23 840 24 1 1 3024</td></tr></table>

For convenience, we write $V _ { m n } ( z )$ for the two-dimensional vector whose first component is $N _ { l m } ( z )$ and whose second component is $D _ { l m } ( z )$ . From the proof of Theorem 352A, it can be seen that the three such vectors $V _ { l - 1 , m } ( z )$ , $V _ { l , m - 1 } ( z )$ and $V _ { l , m } ( z )$ are related by

$$
l V _ { l - 1 , m } ( z ) + m V _ { l , m - 1 } ( z ) = ( l + m ) V _ { l , m } ( z ) .
$$

Many similar relations between neighbouring members of a Pad´e table exist, and we present three of them. In each case the relation is between three Pad´e vectors of successive denominator degrees.

Theorem 352C If $l , m \geq 2$ then

$$
\begin{array} { l } { { \displaystyle V _ { l m } ( z ) = \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad + \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

Second sub-diagonal members of the Pad´e table

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-2,m Dm-2,m</td></tr><tr><td>2</td><td></td><td>1 1-x+ 12 22</td></tr><tr><td>3</td><td>4 1 2 4</td><td>1+ 4 z 28</td></tr><tr><td>4</td><td>1 + z 十 1 30 1 2 2 1 一 十 + 心 30 28 1+ 3 3 2 1 </td></tr><tr><td>5</td><td>56 336 1 5 品 5 2 × 22 168 23 336 24 1+ 2 z X 1 1 + 1 15 180 1 1</td></tr><tr><td>6 7</td><td>1 3 Z 1 一 + 1 22 36 2 336 5040 151200 1+ 5 5 2 2 4 1 12 66 2 132 2376 2 95040 7 2 × 7 7 × 7 7 1 12 44 比 264 23 2376 24 31680 25 95040 26</td></tr></table>

Proof. Let

$$
\begin{array} { l } { { \displaystyle V ( z ) = V _ { l m } ( z ) - \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad - \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

It is easy to verify that the coefficients of $z ^ { 0 }$ , $z ^ { 1 }$ and $z ^ { 2 }$ vanish in both components of $V ( z )$ . We also find that

$$
\begin{array} { r l } { [ 1 } & { { } - \exp ( z ) ] V ( z ) = O ( z ^ { l + m - 1 } ) . } \end{array}
$$

If $V ( z )$ is not the zero vector, we find that

$$
z ^ { - 2 } \big [ 1 \  - \exp ( z ) \big ] V ( z ) = O ( z ^ { l + m - 3 } ) ,
$$

contradicting the uniqueness of Pad´e approximations of degrees $( l - 2 , m - 2 )$

Theorems 352D and $3 5 2 \mathrm { E }$ which follow are proved in the same way as Theorem 352C and the details are omitted.

Error constants for diagonal and first two sub-diagonals   

<table><tr><td>m</td><td>Cm-2,m</td><td>m-1,m</td><td>mm</td></tr><tr><td>0</td><td></td><td></td><td>1</td></tr><tr><td>1</td><td></td><td></td><td>1 12</td></tr><tr><td>2</td><td>1</td><td></td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>720 1</td></tr><tr><td>4</td><td>480 1</td><td>7200 1</td><td>100800 1</td></tr><tr><td>5</td><td>75600 1</td><td>1411200 1</td><td>25401600 1</td></tr><tr><td>6</td><td>20321280 1</td><td>457228800 1</td><td>10059033600 1</td></tr><tr><td>7</td><td>8382528000 1 4931800473600</td><td>221298739200 1</td><td>5753767219200 1 4487938430976000</td></tr></table>

Theorem 352D If $l \geq 1$ and $m \geq 2$ then

$$
\begin{array} { l } { \displaystyle { V _ { l m } ( z ) = \left( 1 - \frac { l } { ( l + m ) ( l + m - 1 ) } z \right) V _ { l , m - 1 } ( z ) } } \\ { \displaystyle { \qquad + \frac { l ( m - 1 ) } { ( l + m ) ( l + m - 1 ) ^ { 2 } ( l + m - 2 ) } z ^ { 2 } V _ { l - 1 , m - 2 } ( z ) . } } \end{array}
$$

Theorem 352E If $l \geq 0$ and $m \geq 2$ then

$$
V _ { l m } ( z ) = \Bigl ( 1 - \frac { 1 } { l + m } z \Bigr ) V _ { l + 1 , m - 1 } ( z ) + \frac { m - 1 } { ( l + m ) ^ { 2 } ( l + m - 1 ) } z ^ { 2 } V _ { l , m - 2 } ( z ) .
$$
