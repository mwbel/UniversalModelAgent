where $N$ and the numbers $x _ { 1 } , x _ { 2 } , \ldots , x _ { N }$ are given, is described by the following:

INPUT $N , x _ { 1 } , x _ { 2 } , \ldots , x _ { n } .$

OUTPUT $\begin{array} { r } { S U M = \sum _ { i = 1 } ^ { N } x _ { i } } \end{array}$

Step 1 Set $S U M = 0$ ( Initialize accumulator.)

Step 2 For $i = 1$ ,2,..., $N$ do set $S U M = S U M + x _ { i }$ .(Add the next term.)

Step 3OUTPUT (SUM); STOP.

# EXAMPLE 2

The $N$ th Taylor polynomial for $f ( x ) = \ln x$ expanded about $x _ { 0 } = 1$ is

$$
P _ { N } ( x ) = \sum _ { i = 1 } ^ { N } \frac { ( - 1 ) ^ { i + 1 } } { i } ( x - 1 ) ^ { i } ,
$$

and the value of In 1.5 to eight decimal places is 0.40546511. Suppose we want to compute the minimal value of $N$ required for

$$
| \ln 1 . 5 - P _ { N } ( 1 . 5 ) | < 1 0 ^ { - 5 }
$$

without using the Taylor polynomial remainder term. From calculus we know that if $\sum \limits _ { n = 1 } ^ { \infty } a _ { n }$ is analteatigsereswihlit $\pmb { A }$ whosetersdeaseinmgitudet $A$ and te Nth partial sum $\begin{array} { r } { A _ { N } = \sum _ { n = 1 } ^ { N } a _ { n } } \end{array}$ diferbyse $( N + 1 ) \mathsf { s t }$ term; that is,

$$
| A - A _ { N } | \leq | a _ { N + 1 } | .
$$

The following algorithm uses this bound.

INPUTvalue $\pmb { x }$ , tolerance TOL, maximum number of iterations $M$ .   
OUTPUT degree $N$ of the polynomial or a message of failure.   
Step 1 Set $N = 1$ ； $y = x - 1 ;$ $S U M = 0$ ； $P O W E R = y ;$ $T E R M = y$ $S I G N = - 1$ .(Used to implement alternation of signs.)

Step 2 While $N \leq M$ do Steps 3-5.

Step 3 Set $S I G N = - S I G N ;$ (Alternate the signs.) $S U M = S U M + S I G N \cdot T E R M ;$ (Accumulate the terms.) $P O W E R = P O W E R \cdot y ;$ $T E R M = P O W E R / ( N + 1 )$ (Calculate the next term.)

Step 4 If $| T E R M | < T O L$ then (Test for accuracy.) OUTPUT $( N )$ ； STOP. (The procedure was successful.)

Step 5Set $N = N + 1$ .(Prepare for the next iteration.)

Step 6OUTPUT("Method Failed')； (The procedure was unsuccessful.) STOP.

The input for our problem is $x = 1 . 5$ ， $T O L = 1 0 ^ { - 5 }$ , and perhaps $M = 1 5$ . This choice of $M$ provides an upper bound for the number of calculations we are willing to perform, recognizing that the algorithm is likely to fail if this bound is exceeded. Whether the output is a value for $N$ or the failure message depends on the precision of the computational device being used. ■

We are interested in choosing methods that will produce dependably accurate results for a wide range of problems. One criterion we will impose on an algorithm whenever possible is that small changes in the initial data produce correspondingly small changes in the final results.An algorithm that satisfies this property is called stable; otherwise it is unstable. Some algorithms are stable only for certain choices of initial data. These are called conditionally stable. We willcharacterize the stability properties of algorithms whenever possible.

To further consider the subjectof roundoferror growthandits connection to algorithm stability, suppose an error with magnitude $E _ { 0 } ~ > ~ 0$ is introduced at some stage in the calculations and that the magnitude of the error after $\pmb { n }$ subsequent operations is denoted by $E _ { n }$ . The two cases that arise most often in practice are defined as follows.

# Definition 1.17

Suppose that $E _ { 0 } > 0$ denotes an initial error and $E _ { n }$ represents the magnitude of an error after $\pmb { n }$ subsequent operations. If $E _ { n } \approx C n E _ { 0 }$ ,where $C$ is a constant independent of $\pmb { n }$ ,then the growth of error is said to be linear. If $E _ { n } \approx C ^ { n } E _ { 0 }$ , for some $C > 1$ , then the growth of error is called exponential.

Linear growth of error is usually unavoidable, and when $C$ and $E _ { 0 }$ are small the results are generally acceptable. Exponential growth of error should be avoided, since the term $C ^ { n }$ becomes large for even relatively small values of $\pmb { n }$ . This leads to unacceptable inaccuracies, regardless of the size of $E _ { 0 }$ . As a consequence,an algorithm that exhibits linear growth of error is stable, whereas an algorithm exhibiting exponential error growth is unstable. (See Figure 1.13 on page 34.)

EXAMPLE 3 The recursive equation

$$
p _ { n } = { \frac { 1 0 } { 3 } } p _ { n - 1 } - p _ { n - 2 } , \quad { \mathrm { f o r } } n = 2 , 3 , \dots
$$

has the solution

$$
p _ { n } = c _ { 1 } \left( { \frac { 1 } { 3 } } \right) ^ { n } + c _ { 2 } 3 ^ { n } ,
$$

![](images/45cbffac985cabc95c06b9fbd71017d3329a8c7f2e440a291d9683185339d627.jpg)  
Figure 1.13

for any constants $c _ { 1 }$ and $c _ { 2 }$ since

$$
\begin{array} { l } { { \displaystyle { \frac { 1 0 } { 3 } } p _ { n - 1 } - p _ { n - 2 } = \ \frac { 1 0 } { 3 } \left[ c _ { 1 } \left( \frac 1 3 \right) ^ { n - 1 } + c _ { 2 } 3 ^ { n - 1 } \right] - \left[ c _ { 1 } \left( \frac 1 3 \right) ^ { n - 2 } + c _ { 2 } 3 ^ { n - 2 } \right] } } \\ { { \mathrm { } } } \\ { { \mathrm { } = c _ { 1 } \left( \frac 1 3 \right) ^ { n - 2 } \left[ \frac { 1 0 } { 3 } \cdot \frac 1 3 - 1 \right] + c _ { 2 } 3 ^ { n - 2 } \left[ \frac { 1 0 } { 3 } \cdot 3 - 1 \right] } } \\ { { \mathrm { } } } \\ { { \mathrm { } = c _ { 1 } \left( \frac 1 3 \right) ^ { n - 2 } \left( \frac 1 9 \right) + c _ { 2 } 3 ^ { n - 2 } ( 9 ) = c _ { 1 } \left( \frac 1 3 \right) ^ { n } + c _ { 2 } 3 ^ { n } = p _ { n } . } } \end{array}
$$

If $p _ { 0 } = 1$ and $\begin{array} { r } { p _ { 1 } = \frac { 1 } { 3 } } \end{array}$ , we have $c _ { 1 } = 1$ and $c _ { 2 } = 0$ ,so $\begin{array} { r } { p _ { n } = \left( \frac { 1 } { 3 } \right) ^ { n } } \end{array}$ for all $n$ . Suppose that five-digit rounding arithmetic is used to compute the terms of the sequence given by this equation. Then $\hat { p } _ { 0 } = 1 . 0 0 0 0$ and $\hat { p } _ { 1 } = 0 . 3 3 3 3 3$ ， which requires modifying the constants to $\hat { c } _ { 1 } = 1 . 0 0 0 0$ and $\hat { c } _ { 2 } = - 0 . 1 2 5 0 0 \times 1 0 ^ { - 5 }$ . The sequence $\{ \hat { p } _ { n } \} _ { n = 0 } ^ { \infty }$ generated is then given by

$$
\hat { p } _ { n } = 1 . 0 0 0 0 \left( \frac { 1 } { 3 } \right) ^ { n } - 0 . 1 2 5 0 0 \times 1 0 ^ { - 5 } ( 3 ) ^ { n } ,
$$

and the roundoff error,

$$
p _ { n } - \hat { p } _ { n } = 0 . 1 2 5 0 0 \times 1 0 ^ { - 5 } ( 3 ^ { n } ) ,
$$

grows exponentially with $n$ . This is reflected in the extreme inaccuracies after the first few terms,as shown in Table 1.5..

On the other hand, the recursive equation

$$
p _ { n } = 2 p _ { n - 1 } - p _ { n - 2 } , \quad { \mathrm { f o r } } n = 2 , 3 , \ldots
$$

Table 1.5   

<table><tr><td>n</td><td>Computed Pn</td><td>Correct Pn</td><td>Relative Error</td></tr><tr><td>0</td><td>0.10000 × 101</td><td>0.10000 × 101</td><td></td></tr><tr><td>1</td><td>0.33333 × 100</td><td>0.33333 × 100</td><td></td></tr><tr><td>2</td><td>0.11110 × 10°</td><td>0.11111 × 100</td><td>9 ×10-5</td></tr><tr><td>3</td><td>0.37000 × 10-1</td><td>0.37037 × 10-1</td><td>1×10-3</td></tr><tr><td>4</td><td>0.12230 × 10-1</td><td>0.12346 × 10-1</td><td>9× 10-3</td></tr><tr><td>5</td><td>0.37660 × 10-2</td><td>0.41152 × 10-2</td><td>8×10-2</td></tr><tr><td>6</td><td>0.32300 × 10-3</td><td>0.13717× 10-2</td><td>8×10-1</td></tr><tr><td>7</td><td>--0.26893× 10-2</td><td>0.45725 × 10-3</td><td>7×100</td></tr><tr><td>8</td><td>-0.92872 × 10-2</td><td>0.15242 × 10-3</td><td>6 ×101</td></tr></table>

has the solution $p _ { n } = c _ { 1 } + c _ { 2 } n$ for any constants $c _ { 1 }$ and $c _ { 2 }$ because

$$
\begin{array} { c } { { 2 p _ { n - 1 } - p _ { n - 2 } = 2 ( c _ { 1 } + c _ { 2 } ( n - 1 ) ) - ( c _ { 1 } + c _ { 2 } ( n - 2 ) ) } } \\ { { { } } } \\ { { = c _ { 1 } ( 2 - 1 ) + c _ { 2 } ( 2 n - 2 - n + 2 ) = c _ { 1 } + c _ { 2 } n = p _ { n } . } } \end{array}
$$

If $p _ { 0 } = 1$ and $\begin{array} { r } { p _ { 1 } = \frac { 1 } { 3 } } \end{array}$ ,teostants iisqai $c _ { 1 } = 1$ and $c _ { 2 } = - \frac { 2 } { 3 }$ so $p _ { n } = 1 - { \frac { 2 } { 3 } } n$ . Five-digit rounding arithmetic in this case results in $\hat { p } _ { 0 } = 1 . 0 0 0 0$ and $\hat { p } _ { 1 } = 0 . 3 3 3 3 3$ . As a consequence, the five-digit rounding constants are $\hat { c } _ { 1 } = 1 . 0 0 0 0$ and $\hat { c } _ { 2 } = - 0 . 6 6 6 6 7$ . Thus,

$$
\hat { p } _ { n } = 1 . 0 0 0 0 - 0 . 6 6 6 6 7 n ,
$$

and the roundoff error is

$$
p _ { n } - { \hat { p } } _ { n } = \left( 0 . 6 6 6 6 7 - { \frac { 2 } { 3 } } \right) n ,
$$

which grows linearly with $\pmb { n }$ . This is reflected in the stability found in Table 1.6.

# Table 1.6

<table><tr><td>n</td><td>Computed pn</td><td>Correct Pn</td><td>Relative Error</td></tr><tr><td>0</td><td>0.10000 × 101</td><td>0.10000 × 101</td><td></td></tr><tr><td>1</td><td>0.33333× 100</td><td>0.33333×100</td><td></td></tr><tr><td>2</td><td>-0.33330 × 100</td><td>-0.33333 × 100</td><td>9×10-5</td></tr><tr><td>3</td><td>-0.10000× 101</td><td>--0.10000 × 10l</td><td>0</td></tr><tr><td>4</td><td>-0.16667 × 101</td><td>-0.16667 × 10l</td><td>0</td></tr><tr><td>5</td><td>-0.23334 × 101</td><td>-0.23333× 101</td><td>4×10-5</td></tr><tr><td>6</td><td>-0.30000 × 101</td><td>-0.30000 × 10l</td><td>0</td></tr><tr><td>7</td><td>-0.36667 × 101</td><td>-0.36667 × 10l</td><td>0</td></tr><tr><td>8</td><td>-0.43334 × 101</td><td>-0.43333 × 10l</td><td>2 ×10-5</td></tr></table>

The effects of roundoff error can be reduced by using high-order-digit arithmetic such as the double- or multiple-precision option available on most computers. Disadvantages in using double-precision arithmetic are that it takes more computation time and the growth of roundoff error is not eliminated but is only postponed until subsequent computations are performed.

One approach to estimating roundoff error is to use interval arithmetic (that is, to retain the largest and smallest possible values at each step), so that, in the end, we obtain an interval that contains the true value. Unfortunately, a very smallinterval may be neded for reasonable implementation.

Since iterative techniques involving sequences are often used, this section concludes with a brief discussion of some terminology used to describe the rate at which convergence occurs when employing a numerical technique. In general, we would like the technique to converge as rapidly as possible. The following definition is used to compare the convergence rates of various methods.

Suppose $\{ \beta _ { n } \} _ { n = 1 } ^ { \infty }$ is a sequence known to converge to zero, and $\{ \alpha _ { n } \} _ { n = 1 } ^ { \infty }$ converges to a number $\pmb { \alpha }$ . If a positive constant $K$ exists with

$$
| \alpha _ { n } - \alpha | \leq K | \beta _ { n } | , \quad { \mathrm { f o r ~ l a r g e ~ } } n ,
$$

then we say that $\{ \alpha _ { n } \} _ { n = 1 } ^ { \infty }$ converges to $\pmb { \alpha }$ with rate of convergence $O ( \beta _ { n } )$ . (This expression is read "big oh of $\beta _ { n } \cdot \gamma )$ It is indicated by writing $\alpha _ { n } = \alpha + O ( \beta _ { n } )$

AlthoughDefinition1.18peits $\{ \alpha _ { n } \} _ { n = 1 } ^ { \infty }$ to be compared with an arbitrary sequence $\{ \beta _ { n } \} _ { n = 1 } ^ { \infty }$ , in nearly every situation we use

$$
\beta _ { n } = { \frac { 1 } { n ^ { p } } } ,
$$

for some number $p > 0$ . We are generallyiterestedin telargst valueof $p$ with $\alpha _ { n } =$ $\alpha + O ( 1 / n ^ { p } )$

Suppose that, for $n \geq 1$ ，

$$
\alpha _ { n } = \frac { n + 1 } { n ^ { 2 } } \quad \mathrm { a n d } \quad \hat { \alpha } _ { n } = \frac { n + 3 } { n ^ { 3 } } .
$$

Although both $\textstyle \operatorname* { l i m } _ { n \to \infty } \alpha _ { n } = 0$ and $\mathrm { l i m } _ { n  \infty } \hat { \alpha } _ { n } = 0$ , the sequence $\{ \hat { \alpha } _ { n } \}$ converges to this limit much faster than the sequence $\{ \alpha _ { n } \}$ ,using five-digit rounding arithmetic,as shown in Table 1.7.

Table 1.7

<table><tr><td>n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>an</td><td>2.00000</td><td>0.75000</td><td>0.44444</td><td>0.31250</td><td>0.24000</td><td>0.19444</td><td>0.16327</td></tr><tr><td>&amp;n</td><td>4.00000</td><td>0.62500</td><td>0.22222</td><td>0.10938</td><td>0.064000</td><td>0.041667</td><td>0.029155</td></tr></table>

If we let $\beta _ { n } = 1 / n$ and ${ \hat { \beta } } _ { n } = 1 / n ^ { 2 }$ , we see that

$$
| \alpha _ { n } - 0 | = { \frac { n + 1 } { n ^ { 2 } } } \leq { \frac { n + n } { n ^ { 2 } } } = 2 \cdot { \frac { 1 } { n } } = 2 \beta _ { n }
$$

and

$$
| { \hat { \alpha } } _ { n } - 0 | = { \frac { n + 3 } { n ^ { 3 } } } \leq { \frac { n + 3 n } { n ^ { 3 } } } = 4 \cdot { \frac { 1 } { n ^ { 2 } } } = 4 { \hat { \beta } } _ { n } ,
$$

so

$$
\alpha _ { n } = 0 + O \left( { \frac { 1 } { n } } \right) \quad { \mathrm { ~ a n d ~ } } \quad { \hat { \alpha } } _ { n } = 0 + O \left( { \frac { 1 } { n ^ { 2 } } } \right) .
$$

The rate of convergence of $\left\{ \alpha _ { n } \right\}$ to zero is similar to the convergence of $\{ 1 / n \}$ to zero, whereas $\{ \hat { \alpha } _ { n } \}$ converges to zero at a rate similar to the more rapidly convergent sequence $\{ 1 / n ^ { 2 } \}$

We also use the“big oh" notation to describe the rate at which functions converge.

finition 1.19Suppose that $\begin{array} { r } { \operatorname* { l i m } _ { h \to 0 } G ( h ) = 0 } \end{array}$ and $\begin{array} { r } { \operatorname* { l i m } _ { h  0 } F ( h ) = L } \end{array}$ . If a positive constant $\pmb { K }$ exists with

then we write $F ( h ) = L + O ( G ( h ) )$

The functions we use for comparison generally have the form $G ( h ) ~ = ~ h ^ { p }$ ，where $p > 0$ . We are interested in the largest value of $p$ for which $F ( h ) = L + O ( h ^ { p } )$

# EXAMPLE 5

In Example 3(b) of Section 1.1 we found that the third Taylor polynomial gives

$$
\cos h = 1 - \frac { 1 } { 2 } h ^ { 2 } + \frac { 1 } { 2 4 } h ^ { 4 } \cos \tilde { \xi } ( h ) ,
$$

for some number $\tilde { \xi } ( h )$ between zero and $h$ . Consequently,

$$
\cos h + \frac { 1 } { 2 } h ^ { 2 } = 1 + \frac { 1 } { 2 4 } h ^ { 4 } \cos \tilde { \xi } ( h ) .
$$

This result implies that

$$
\cos h + \frac { 1 } { 2 } h ^ { 2 } = 1 + O ( h ^ { 4 } ) ,
$$

since $\begin{array} { r } { | ( \cos h + \frac 1 2 h ^ { 2 } ) - 1 | = | \frac { 1 } { 2 4 } \cos \tilde { \xi } ( h ) | h ^ { 4 } \le \frac { 1 } { 2 4 } h ^ { 4 } } \end{array}$ . The implication is that as $h  0$ ， $\textstyle \cos h + { \frac { 1 } { 2 } } h ^ { 2 }$ converges to its limit,1,about as fast as $h ^ { 4 }$ converges to 0.

# ExERCIsE SEt 1.3

1.a.Use thre-digit chopping arithmetic to compute the sum $\textstyle \sum _ { i = 1 } ^ { 1 0 } ( 1 / i ^ { 2 } )$ first by $\frac { 1 } { 1 } + \frac { 1 } { 4 } +$ $\cdots + { \frac { 1 } { 1 0 0 } }$ and then by $\textstyle { \frac { 1 } { 1 0 0 } } + { \frac { 1 } { 8 1 } } + \cdots + { \frac { 1 } { 1 } }$ . Which method is more accurate, and why?

b. Writeaies

2.The number $e$ is defined by $\textstyle e = \sum _ { n = 0 } ^ { \infty } ( 1 / n ! )$ ,where $n ! = n ( n - 1 ) \cdots 2 \cdot 1$ for $n \neq 0$ and $0 ! = 1$ . Use four-digit chopping arithmetic to compute the following approximations to $e$ ,and determine the absolute and relative errors.

$\begin{array} { r l } { \mathbf { a } . } & { { } e \approx \displaystyle \sum _ { n = 0 } ^ { 5 } \frac { 1 } { n ! } } \\ { \mathbf { c } . } & { { } e \approx \displaystyle \sum _ { n = 0 } ^ { 1 0 } \frac { 1 } { n ! } } \end{array}$ $\begin{array} { l l } { { { \bf b . } } } & { { e \approx \displaystyle \sum _ { j = 0 } ^ { 5 } \frac { 1 } { ( 5 - j ) ! } } } \\ { { { \bf d . } } } & { { e \approx \displaystyle \sum _ { j = 0 } ^ { 1 0 } \frac { 1 } { ( 1 0 - j ) ! } } } \end{array}$

3.The Maclaurin series for the arctangent function converges for $- 1 < x \leq \dot { 1 }$ and is given by

$$
\arctan x = \operatorname* { l i m } _ { n \to \infty } { \cal P } _ { n } ( x ) = \operatorname* { l i m } _ { n \to \infty } \sum _ { i = 1 } ^ { n } ( - 1 ) ^ { i + 1 } { \frac { x ^ { 2 i - 1 } } { 2 i - 1 } } .
$$

a. Use the fact that tan $\pi / 4 = 1$ to determine the number of $\pmb { n }$ terms of the series that need to be summed to ensure that $| 4 P _ { n } ( 1 ) - \pi | < 1 0 ^ { - 3 }$ ·   
b. The $\mathbf { C } + +$ programming language requires the value of $\pi$ to be within $1 0 ^ { - 1 0 }$ . How many terms of the series would we need to sum to obtain this degree of accuracy?

4.Exercise 3 details a rather inefficient means of obtaining an approximation to $\pi$ . The method can be improved substantially by observing that $\pi / 4 = \arctan { \frac { 1 } { 2 } } + \arctan { \frac { 1 } { 3 } }$ and evaluating the series for the arctangent at $\frac { 1 } { 2 }$ and at $\frac { 1 } { 3 }$ . Determine the number of terms that must be summed to ensure an approximation to π to within 10-3.

5.Another formula for computing $\pi$ can be deduced from the identity $\pi / 4 \ = \ 4 \arctan { \frac { 1 } { 5 } } \ -$ arctan 2g. Determine the number of terms that must be summed to ensure an approximation to $\pmb { \pi }$ to within $1 0 ^ { - 3 }$

6.Find the rates of convergence of the following sequences as $n  \infty$

a. $\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { n \to \infty } \sin \frac { 1 } { n } = 0 } \\ { \displaystyle \operatorname* { l i m } _ { n \to \infty } \left( \sin \frac { 1 } { n } \right) ^ { 2 } = 0 } \end{array}$ ${ \begin{array} { r l } & { { \mathrm { \bf { b } } } , \quad \operatorname* { l i m } _ { n \to \infty } \sin { \frac { 1 } { n ^ { 2 } } } = 0 } \\ & { { \mathrm { \bf { d } } } , \quad \operatorname* { l i m } _ { n \to \infty } [ \ln ( n + 1 ) - \ln ( n ) ] = 0 } \end{array} }$   
c.

7.Find the rates of convergence of the following functions as $h  0$

a. $\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { h \to 0 } \frac { \sin h } { h } = 1 } \\ { \displaystyle \operatorname* { l i m } _ { h \to 0 } \frac { \sin h - h \cos h } { h } = 0 } \end{array}$ $\begin{array} { l } { { \displaystyle { \bf b } . \operatorname* { l i m } _ { h  0 } \frac { 1 - \cos h } { h } = 0 } } \\ { { \displaystyle { \bf d } . \operatorname* { l i m } _ { h  0 } \frac { 1 - e ^ { h } } { h } = - 1 } } \end{array}$   
c.

8.a.How many multiplications and additions are required to determine a sum of the form

$$
\sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { i } a _ { i } b _ { j } ?
$$

b.Modify the sum in part (a) to an equivalent form that reduces the number of computations.

9. Let $P ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 }$ be a polynomial, and let $\pmb { x _ { 0 } }$ be given. Construct an algorithm to evaluate $P ( x _ { 0 } )$ using nested multiplication.

10.Example 5 of Section 1.2 gives alternative formulas for the roots $x _ { 1 }$ and $x _ { 2 }$ of $a x ^ { 2 } + b x + c = 0$ Construct an algorithm with input $a , b , c$ and output $x _ { 1 } , x _ { 2 }$ that computes the roots $x _ { 1 }$ and $x _ { 2 }$ (which may be equal or be complex conjugates) using the best formula for each root.

11. Construct an algorithm that has as input an integer $n \geq 1$ ， numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ,and a number $\pmb { x }$ and that produces as output the product $( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } )$

12.Assume that

$$
{ \frac { 1 - 2 x } { 1 - x + x ^ { 2 } } } + { \frac { 2 x - 4 x ^ { 3 } } { 1 - x ^ { 2 } + x ^ { 4 } } } + { \frac { 4 x ^ { 3 } - 8 x ^ { 7 } } { 1 - x ^ { 4 } + x ^ { 8 } } } + \cdots = { \frac { 1 + 2 x } { 1 + x + x ^ { 2 } } } ,
$$

for $x \ < \ 1$ ,and let $x = 0 . 2 5$ . Write and execute an algorithm that determines the number of terms needed on the left side of the equation so that the left side differs from the right side by less than $1 0 ^ { - 6 }$

13.a.Suppose that $0 < q < p$ and that $\alpha _ { n } = \alpha + O \left( n ^ { - p } \right)$ . Show that $\alpha _ { n } = \alpha + O \left( n ^ { - q } \right)$ b. Make a table listing $1 / n , 1 / n ^ { 2 } , 1 / n ^ { 3 }$ ,and $1 / n ^ { 4 }$ for $n = 5$ ,10,100,and 1000,and discuss the varying rates of convergence of these sequences as $\pmb { n }$ becomes large.

14.a.Suppose that $0 < q < p$ and that $F ( h ) = L + O \left( h ^ { p } \right)$ . Show that $F ( h ) = L + O \left( h ^ { q } \right) ,$ b. Make a table listing $h , h ^ { 2 } , h ^ { 3 }$ ,and $h ^ { 4 }$ for $h = 0 . 5 , 0 . 1 , 0 . 0 1$ ,and 0.001,and discuss the varying rates of convergence of these powers of $h$ as $h$ approaches zero.

15.Suppose that as $x$ approaches zero,

$$
F _ { 1 } ( x ) = L _ { 1 } + O ( x ^ { \alpha } ) \quad { \mathrm { ~ a n d ~ } } \quad F _ { 2 } ( x ) = L _ { 2 } + O ( x ^ { \beta } ) .
$$

Let $c _ { 1 }$ and $c _ { 2 }$ be nonzero constants,and define

$$
F ( x ) = c _ { 1 } F _ { 1 } ( x ) + c _ { 2 } F _ { 2 } ( x ) \quad { \mathrm { a n d } } \quad G ( x ) = F _ { 1 } ( c _ { 1 } x ) + F _ { 2 } ( c _ { 2 } x ) ,
$$

Show that if $\gamma =$ minimum $\{ \alpha , \beta \}$ ,then as $x$ approaches zero,

$$
F ( x ) = c _ { 1 } L _ { 1 } + c _ { 2 } L _ { 2 } + O ( x ^ { \gamma } ) \qquad \mathbf { b . } \quad G ( x ) = L _ { 1 } + L _ { 2 } + O ( x ^ { \gamma } ) .
$$

16. The sequence $\{ F _ { n } \}$ described by $F _ { 0 } = 1 , F _ { 1 } = 1$ ，and $F _ { n + 2 } = F _ { n } + F _ { n + 1 }$ ,if $n \geq 0$ , is called a Fibonacci sequence.Its terms occur naturally in many botanical species,particularly those with petals or scales arranged in the form of a logarithmic spiral. Consider the sequence $\{ x _ { n } \}$ ， where $x _ { n } = F _ { n + 1 } / F _ { n }$ . Assuming that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } x _ { n } = x$ exists,show that $x = ( 1 + { \sqrt { 5 } } ) / 2$ . This number is called the golden ratio.

17.The Fibonacci sequence also satisfies the equation

$$
F _ { n } \equiv { \tilde { F } } _ { n } = { \frac { 1 } { \sqrt { 5 } } } \left[ \left( { \frac { 1 + { \sqrt { 5 } } } { 2 } } \right) ^ { n } - \left( { \frac { 1 - { \sqrt { 5 } } } { 2 } } \right) ^ { n } \right] .
$$

a. Write a Maple procedure to calculate $F _ { 1 0 0 }$ b. Use Maple with the default value of Digits followed by evalf to calculate $\tilde { F } _ { 1 0 0 }$ c. Why is the result from part (a) more accurate than the result from part (b)? d. Why is the result from part (b) obtained more rapidly than the result from part (a)? e. What results when you use the command simplify instead of evalf to compute $\tilde { F } _ { 1 0 0 } ?$

18.The harmonic series $1 + { \textstyle { \frac { 1 } { 2 } } } + { \textstyle { \frac { 1 } { 3 } } } + { \textstyle { \frac { 1 } { 4 } } } + \cdots$ diverges, but the sequence $\gamma _ { n } = 1 + { \frac { 1 } { 2 } } + \cdot \cdot \cdot + { \frac { 1 } { n } } - \ln n$ converges, since $\{ \gamma _ { n } \}$ is a bounded, nonincreasing sequence. The limit $\gamma = 0 . 5 7 7 2 1 5 6 6 4 9 \ldots$ of the sequence $\{ \gamma _ { n } \}$ is called Euler's constant.

a. Use the default value of Digits in Maple to determine the value of $n$ for $\gamma _ { n }$ to be within $1 0 ^ { - 2 } \ \mathsf { o f } \ \gamma$   
b. Use the default value of Digits in Maple to determine the value of $\pmb { n }$ for $\gamma _ { n }$ to be within $1 0 ^ { - 3 }$ of $\gamma$   
c. What happens if you use the default value of Digits in Maple to determine the value of $\pmb { n }$ for $\gamma _ { n }$ to be within $1 0 ^ { - 4 }$ of $\gamma ?$

# 1.4 Numerical Software

Computer software packages for approximating the numerical solutions to problems are available in many forms. With this book,we have provided programs written in C,FOR-TRAN, Maple,Mathematica,MATLAB,and Pascal that can be used to solve the problems given in the examples and exercises.These programs will give satisfactory results for most problems that you may need to solve, but they are what we call special-purpose programs. We use this term to distinguish these programs from those available in the standard mathematical subroutine libraries. The programs in these packages will be called general purpose.

The programs in general-purpose software packages differ in their intent from the algorithms and programs provided with this book. General-purpose software packages consider ways to reduce errors due to machine rounding,underflow,and overflow. They also describe the range of input that will lead to results of a certain specified accuracy. Since these are machine-dependent characteristics, general-purpose software packages use parameters that describe the floating-point characteristics of the machine being used for computations.

To illustrate some differences between programs included in a general-purpose pack-age and a program that we would provide for use in this book,let us consider an algorithm that computes the Euclidean norm of an $\pmb { n }$ -dimensional vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ . This norm is often required within larger programs and is defined by

$$
\lvert \lvert \mathbf { x } \rvert \rvert _ { 2 } = \left[ \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right] ^ { 1 / 2 } .
$$

The norm gives a measure for the distance from the vector $\mathbf { x }$ to the vector 0. For example, the vector $\mathbf { x } = ( 2 , 1 , 3 , - 2 , - 1 ) ^ { t }$ has

$$
| | { \bf x } | | _ { 2 } = [ 2 ^ { 2 } + 1 ^ { 2 } + 3 ^ { 2 } + ( - 2 ) ^ { 2 } + ( - 1 ) ^ { 2 } ] ^ { 1 / 2 } = \sqrt { 1 9 } ,
$$

so its distance from $\mathbf { 0 } = ( 0 , 0 , 0 , 0 , 0 ) ^ { t }$ is ${ \sqrt { 1 9 } } \approx 4 . 3 6$

An algorithm of the type we would present for this problem is given here.It includes no machine-dependent parameters and provides no accuracy assurances, but it will give accurate results “most of the time.”

OUTPUT NORM.

Step 1 Set $S U M = 0$

Step 2 For $i = 1 , 2 , \dots , n$ set $S U M = S U M + x _ { i } ^ { 2 }$

Step3 Set $N O R M = S U M ^ { 1 / 2 }$

Step 4OUTPUT (NORM); STOP.

A program based on this algorithm is easy to write and understand. However, the pro-gram could fail to give sufficient accuracy for a number of reasons.For example, the magnitude of some of the numbers might be too large or too small to be accurately represented in the floating-point system of the computer. Also,the normal order for performing the calculations might not produce the most accurate results,or the standard software square-root routine might not be the best available for the problem. Matters of this type are considered by algorithm designers when writing programs for general-purpose software. These pro-grams are often used as subprograms for solving larger problems, so they must incorporate controls that we will not need.

Let us now consider an algorithm for a general-purpose software program for computing the Euclidean norm. First, it is possible that although a component $x _ { i }$ of the vector is within the range of the machine,the square of the component is not. This can occur when some $\left. x _ { i } \right.$ is so small that $x _ { i } ^ { 2 }$ causes underflow or when some $\left| x _ { i } \right|$ is so large that $\boldsymbol { x } _ { i } ^ { 2 }$ causes overflow.It is also possible for all these terms to be within the range of the machine,but overflow occurs from the addition of a square of one of the terms to the previously com-puted sum.

Since accuracy criteria depend on the machine on which the calculations are being performed, machine-dependent parameters are incorporated into the algorithm. Suppose we are working on a hypothetical computer with base 1O, having $t \geq 4$ digits of precision, a minimum exponent emin,and a maximum exponent emax. Then the set of floating-point numbers in this machine consists of O and the numbers of the frm

$$
x = f \cdot 1 0 ^ { e } , \quad { \mathrm { w h e r e } } \quad f = \pm ( f _ { 1 } 1 0 ^ { - 1 } + f _ { 2 } 1 0 ^ { - 2 } + \cdot \cdot \cdot + f _ { t } 1 0 ^ { - t } ) ,
$$

where $1 \leq f _ { 1 } \leq 9$ and $0 \leq f _ { i } \leq 9$ ,for each $i = 2 , \dots , t$ ,and where em $\dot { n } \le e \le e m a x$ These constraints imply that the smallest positive number represented in the machine is $\sigma ~ = ~ 1 0 ^ { e m i n - 1 }$ ， so any computed number $x$ with $| x | < \sigma$ causes underflow and results in $x$ being set to O. The largest positive number is $\lambda = ( 1 - 1 0 ^ { - t } ) 1 0 ^ { e m a x }$ , and any computed number $x$ with $| x | > \lambda$ causes overflow. When underflow occurs, the program will continue, often without a significant loss of accuracy. If overflow occurs, the program will fail.

The algorithm assumes that the floating-point characteristics of the machine are described using parameters $N , s , S , y$ ,and $Y$ . The maximum number of entries that can be summed with at least $t / 2$ digits of accuracy is given by $N$ . This implies the algorithm will proceed to find the norm of a vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ only if $n \leq N$ . To resolve the underflow-overflow problem,the nonzero floating-point numbers are partitioned into three groups: small-magnitude numbers $x$ , those satisfying $0 \ < \ | x | \ < \ y$ ; medium-magnitude numbers $x$ ,where $y \ \leq \ | x | \ < \ Y$ ; and large-magnitude numbers $x$ ，where $Y ~ \leq ~ | x |$ . The parameters $y$ and $Y$ are chosen so that there will be no underflow-overflow problem in squaring and summing the medium-magnitude numbers. Squaring smal-magnitude numbers can cause underflow, so a scale factor $s$ much greater than 1 is used with the result that $( S x ) ^ { 2 }$ avoids the underflow even when $x ^ { 2 }$ does not. Summing and squaring numbers having a large magnitude can cause overflow,so in this case,a positive scale factor $s$ much smaller than 1 is used to ensure that $( s x ) ^ { 2 }$ does not cause overflow when calculated or incorporated into a sum, even though $x ^ { 2 }$ would.

To avoid unnecessary scaling，y and $Y$ are chosen so that the range of mediummagnitude numbers is as large as possible. The algorithm that follows is a modification of one described in [Brow, W, p. 471]. It incorporates a procedure for scaling the compo-nents of the vector that are small in magnitude until a component with medium magnitude is encountered. It then unscales the previous sum and continues by squaring and summing small and medium numbers until a component with a large magnitude is encountered. Once a component with large magnitude appears,the algorithm scales the previous sum and proceeds to scale,square,and sum the remaining numbers. The algorithm assumes that, in transition from smal to medium numbers,unscaled small numbers are negligible when compared to medium numbers. Similarly,in transition from medium to large numbers, un-scaled medium numbers are negligible when compared to large numbers. Thus, the choices of the scaling parameters must be made so that numbers are equated to O only when they are truly negligible.Typical relationships between the machine characteristics as described by $t , \sigma , \lambda$ , emin, emax, and the algorithm parameters $N , s , S , y$ ,and $Y$ are given after the algorithm.

The algorithm uses three flags to indicate the various stages in the summation process. These flags are given initial values in Step 3 of the algorithm.FLAG 1 is 1 until a medium or large component is encountered; then it is changed to 0. FLAG 2 is O while small numbers are being summed, changes to 1 when a medium number is first encountered,and changes back to O when a large number is found. FLAG 3 is initially O and changes to 1 when'a large number is first encountered. Step 3 also introduces the flag DONE,which is O until the calculations are complete,and then changes to 1.

INPUT $N , s , S , y , Y , \lambda , n , x _ { 1 } , x _ { 2 } , . . . , x _ { n } .$

OUTPUTNORM or an appropriate error message.

Step 1 If $n \leq 0$ then OUTPUT（‘The integer $\pmb { n }$ must be positive.'); STOP.

Step 2 If $n \geq N$ then OUTPUT(The integer $\pmb { n }$ is too large.); STOP.

Step 3 Set $S U M = 0$ ； $F L A G 1 = 1$ ；  (The small numbers are being summed.) $F L A G 2 = 0$ ； $F L A G 3 = 0$ ； $D O N E = 0$ ： $i = 1$ .

Step 4While $( i \leq n$ and $F L A G 1 = 1$ do Step 5.

Step 5If $| x _ { i } | < y$ then set $S U M = S U M + ( S x _ { i } ) ^ { 2 }$ ； $i = i + 1$ else set $F L A G 1 = 0$ (A non-small number encountered.)

Step $\sigma$ $i > n$ then set $N O R M = ( S U M ) ^ { 1 / 2 } / S ;$ $D O N E = 1$ else set $S U M = ( S U M / S ) / S$ (Scale for larger numbers.) $F L A G 2 = 1 $

Step 7 While $( i \leq n$ and $F L A G 2 = 1 \quad$ )do Step 8. (Sum the medium-sized numbers.)

Step8If $| x _ { i } | < Y$ then set $\begin{array} { l } { S U M = S U M + x _ { i } ^ { 2 } ; } \\ { i = i + 1 } \end{array}$ else set $F L A G 2 = 0$ .(A large number has been encountered.)

Step 9 If $D O N E = 0$ then

$$
D O N E = 1
$$

Step 10 While $( i \leq n$ and $F L A G 3 = 1$ )do Step 11.

Step 11 Set $S U M = S U M + ( s x _ { i } ) ^ { 2 }$ ;(Sum the large numbers.) $i = i + 1$

Step 12 If $D O N E = 0$ then

if $S U M ^ { 1 / 2 } < \lambda s$ then set $N O R M = ( S U M ) ^ { 1 / 2 } / s$ ； $D O N E = 1$ else set $S U M = \lambda$ .(The norm is too la)

Step 13If $D O N E = 1$ then OUTPUT (‘Norm is’,NORM) else OUTPUT( $\mathbf { \partial } ^ { \prime } \mathbf { N o r m } \geq \mathbf { \partial } ^ { \prime }$ ,NORM,‘overflow occurred').

Step 14 STOP.

The relationships between the machine characteristics $t , \sigma , \lambda$ , emin, emax, and the algorithm parameters $N , s , S , y$ ,and $Y$ were chosen in [Brow, W, p. 471] as:

$N = 1 0 ^ { e _ { N } }$ ，where $e _ { N } = \lfloor ( t - 2 ) / 2 \rfloor$ ，the greatest integer less than or equal to $( t - 2 ) / 2$ ；   
$s = 1 0 ^ { e _ { s } }$ ，where $e _ { s } = \lfloor - ( e m a x + e _ { N } ) / 2 \rfloor ;$   
$S = 1 0 ^ { e _ { S } }$ ，where $e _ { S } = \lceil ( 1 - e m i n ) / 2 \rceil$ ，the smallest integer greater than or equal to $( 1 - e m i n ) / 2$ ；   
$y = 1 0 ^ { e _ { y } }$ ，w $\begin{array} { l l } { { \mathrm { h e r e } } } & { { e _ { y } = \lceil ( e m i n + t - 2 ) / 2 \rceil ; } } \\ { { \mathrm { h e r e } } } & { { e _ { Y } = \lfloor ( e m a x - e _ { N } ) / 2 \rfloor . } } \end{array}$   
$Y = 1 0 ^ { e \gamma }$ ，w

The eliability built into this algorithm has greatly increased the complexity compared to the algorithm given earlier in the section.

There are many forms of general-purpose numerical software available commercially and in the public domain. Most of the early software was written for mainframe computers, and a good reference for this is Sources and Development of Mathematical Software, edited by Wayne Cowell [Co]. Now that the desktop computer has become sufficiently powerful, standard numerical software is available for personal computers and workstations. Most of this numerical software is written in FORTRAN, although some packages are written in C, $\mathbf { C } { \neq } { + }$ , and FORTRAN90.

ALGOL procedures were presented for matrix computations in 1971 in [WR]. A pack-age of FORTRAN subroutines based mainly on the ALGOL procedures was then developed into the EISPACK routines. These routines are documented in the manuals published by Springer-Verlag as part of their Lecture Notes in Computer Science series $[ \mathsf { S m } , \mathbf { B } ]$ and [Gar]. The FORTRAN subroutines are used to compute eigenvalues and eigenvectors for a variety of different types of matrices. The EISPACK project was the first large-scale numerical software package to be made available in the public domain and led the way for many packages to follow. EISPACK is maintained by netlib and can be found on the Internet at http://www.netlib.org/eispack.

LINPACK is a package of FORTRAN subroutines for analyzing and solving systems of linear equations and solving linear least squares problems. The documentation for this package is contained in [DBMS] and located at http://www.netlib.org/linpack. A step-bystep introduction to LINPACK,EISPACK,and BLAS (Basic Linear Algebra Subprograms) is given in [CV].

The LAPACK package, first available in 1992, is a library of FORTRAN subroutines that supercedes LINPACK and EISPACK by integrating these two sets of algorithms into a unified and updated package. The software has been restructured to achieve greater efficiency on vector processors and other high-performance or shared-memory multiprocessors.LAPACK is expanded in depth and breadth in version 3.0,which is available in FORTRAN, FORTRAN90, C, $\sum + +$ ， and JAVA. FORTRAN90, C,and JAVA are only available as language interfaces or translations of the FORTRAN libraries of LAPACK. The package BLAS is not a part of LAPACK, but the code for BLAS is distributed with LAPACK. The LAPACK User's Guide, 3rd ed. [An] is available from SIAM or on the Internet at http://www.netlib.org/lapack/lug/lapack_lug.html. The complete LAPACK or individual routines from LAPACK can be obtained through netlib at netlibornl.gov, netlibresearch.att.com, or http://www.netlib.org/lapack.

Other packages for solving specific types of problems are available in the public domain. Information about these programs can be obtained through electronic mail by sending the line “help" to one of the following addresses: netlibresearch.att.com, netlibornl.gov, netlibnac.no, or netlibdraci.cs.uow.edu.au or to the uucp address uunet!research!netlib. As an alternative to netlib,you can use Xnetlib to search the database and retrieve software. More information can be found in the article Software Distribution using Netlib by Dongarra, Roman,and Wade [DRW].

These software packages are highly efficient, accurate, and reliable. They are thoroughly tested,and documentation is readily available. Although the packages are portable, it is a good idea to investigate the machine dependence and read the documentation thoroughly. The programs test for almost all special contingencies that might result in error and failures. At the end of each chapter we will discuss some of the appropriate generalpurpose packages.

Commercially available packages also represent the state of the art in numerical methods.Their contents are often based on the public-domain packages but include methods in libraries for almost every type of problem.

IMSL (International Mathematical and Statistical Libraries） consists of the libraries MATH, STAT, and SFUN for numerical mathematics,statistics,and special functions; respectively. These libraries contain more than 9OO subroutines originally available in FOR-TRAN 77 and now available in C, FORTRAN90, and JAVA. These subroutines solve the most common numerical analysis problems. In 1970 IMSL became the first large-scale scientific library for mainframes. Since that time,the libraries have been made available for computer systems ranging from supercomputers to personal computers. The libraries are available commercially from Visual Numerics, 9990 Richmond Ave S400, Houston,

TX 77042-4548,with Intermet address http://www.vni.com. The packages are delivered in compiled form with extensive documentation. There is an example program for each routine as well as background reference information. IMSL contains methods for linear systems, eigensystem analysis, interpolation and approximation,integration and differentiation, differential equations, transforms, nonlinear equations,optimization,and basic matrix/vector operations. The library also contains extensive statistical routines.

The Numerical Algorithms Group (NAG) has been in existence in the United Kingdom since 1970. NAG offers more than 1O00 subroutines in a FORTRAN 77 library，about 400 subroutines in a C library, over 2OO subroutines in a FORTRAN 90 library,and an MPI FORTRAN numerical library for parallel machines and clusters of workstations or personal computers. A subset of their FORTRAN 77 library (the NAG Foundation Library) is available for personal computers and workstations where work space is limited. The NAG C Library, the FORTRAN 90 library, and the MPI FORTRAN library offer many of the same routines as the FORTRAN Library. The NAG user's manual includes instructions and examples, along with sample output for each of the routines. A useful introduction to the NAG routines is [Ph]. The NAG library contains routines to perform most standard numerical analysis tasks in a manner similar to those in the IMSL. It also includes some statistical routines and a set of graphic routines. The library is commercially available from Numerical Algorithms Group, Inc.,1400 Opus Place,Suite 2O0, Downers Grove,IL 60515-5702, with Internet address http://www.nag.com.

The IMSL and NAG packages are designed for the mathematician, scientist, or engi-neer who wishes to cal high-quality FORTRAN subroutines from within a program. The documentation available with the commercial packages illustrates the typical driver pro-gram required to use the library routines. The next three software packages are stand-alone environments. When activated, the user enters commands to cause the package to solve a problem. However, each package allows programming within the command language.

MATLAB is a matrix laboratory that was originally a Fortran program published by Cleve Moler [Mo].The laboratory is based mainly on the EISPACK and LINPACK subroutines,although functions such as nonlinear systems, numerical integration, cubic splines, curve fiting,optimization, ordinary differential equations,and graphical tools have been incorporated. MATLAB is currently written in C and assembler, and the PC version of this package requires a numeric coprocessor. The basic structure is to perform matrix operations,such as finding the eigenvalues of a matrix entered from the command line or from an external file via function calls. This is a powerful self-contained system that is especially useful for instruction in an applied linear algebra course.MATLAB has been available since 1985 and can be purchased from The MathWorks Inc., Cochituate Place,24 Prime Park Way,Natick,MA O1760.The electronic mail address of The Mathworks is infomathworks.com, and the Internet address is http://www.mathworks.com. MATLAB software is designed to run on many computers, including IBM PC compatibles,APPLE Macintosh, and SUN workstations. A student version of MATLAB does not require a coprocessor but will use one if it is available.

The second package is GAUSS, a mathematical and statistical system produced by Lee E.Ediefson and Samuel D. Jones in 1985.It is coded mainly in assembler and based primarily on EISPACK and LINPACK. As in the case of MATLAB,integration/differentiation, nonlinear systems,fast Fourier transforms,and graphics are available. GAUSS is oriented less toward instruction in linear algebra and more toward statistical analysis of data. This package also uses a numeric coprocessor if one is available. It can be purchased from Aptech Systems, Inc., 23804 S.E. Kent-Kangley Road, Maple Vally, WA 98038 (infoaptech.com).

The third package is Maple,a computer algebra system developed in 1980 by the Symbolic Computational Group at the University of Waterloo. The design for the original Maple system is presented in the paper by B.W. Char,K.O. Geddes,W.M. Gentlemen,and G.H. Gonnet [CGGG]. Maple has been available since 1985 and can be purchased from Waterloo Maple Inc., 57 Erb Street, Waterloo,ON N2L 6C2. The electronic mail address of Waterloo Maple is infomaplesoft.com, and the Internet address is http://www.maplesoft.com.Maple,which is written in C,has the ability to manipulate information in a symbolic manner. This symbolic manipulation allows the user to obtain exact answers instead of numerical values.Maple can give exact answers to mathematical problems such as integrals,differential equations,and linear systems. It contains a programming structure and permits text, as well as commands,to be saved in its worksheet files.These worksheets can then be loaded into Maple and the commands executed. Because of the properties of symbolic computation, numerical computation,and worksheets, Maple is the language of choice for this text. Throughout the book Maple commands will be embedded into the text.

Numerous packages are available that can be classified as supercalculator packages for the PC. These should not be confused, however, with the general-purpose software listed here. If you have an interest in one of these packages, you should read Supercalculators on the PC by B. Simon and R. M. Wilson [SW].

Additional information about software and software libraries can be found in the books by Cody and Waite [CW] and by Kockler [Ko],and in the 1995 article by Dongarra and Walker [DW]. More information about floating-point computation can be found in the book by Chaitini-Chatelin and Frayse [CF] and the article by Goldberg [Go].

Books that address the application of numerical techniques on parallel computers include those by Schendell [Sche], Philips and Freeman [PF],and Golub and Ortega [GO].

CHAPTER

# 2

# Solutions of Equations in One Variable

■ ■ 1

by assuming that the population grows continuously with time at a rate proportional to the number present at that time. If we let $\pmb { M } ( t )$ denote the number at time t and $\pmb { \lambda }$ denote the constant birth rate of the population, then the population satisfies the differential equation

$$
\frac { d N ( t ) } { d t } = \lambda N ( t ) .
$$

The solution to this equation is $N ( t ) = N _ { 0 } e ^ { \lambda t }$ , where ${ \pmb { N } } _ { \pmb { \mathbb { 0 } } }$ denotes the initial population.

![](images/020fd44b9a294b43eddeb2fa20661d2d5998de31a59c5babeee01f6a018af9b6.jpg)

![](images/851faed33f9c2123d0b17a4d80d7b76ead6a0bc1567584aea208bc2dcedcbe5f.jpg)

This exponential model is valid only when the population is isolated, with no immigration. If immigration is permitted at a constant rate $\pmb { \nu }$ ， then the differential equation becomes

$$
\frac { d N ( t ) } { d t } = \lambda N ( t ) + \nu ,
$$

whose solution is

$$
N ( t ) = N _ { 0 } e ^ { \lambda t } + \frac { \nu } { \lambda } ( e ^ { \lambda t } - 1 ) .
$$

Suppose a certain population contains 1,0oo,ooo individuals ini-tially, that 435,oo0 individuals immigrate into the community in the first year, and that 1,564,0oO individuals are present at the end of one year. To determine the birth rate of this population, we must solve for $\lambda$ in the equation

$$
1 , 5 6 4 , 0 0 0 = 1 , 0 0 0 , 0 0 0 e ^ { \lambda } + \frac { 4 3 5 , 0 0 0 } { \lambda } ( e ^ { \lambda } - 1 ) .
$$

The numerical methods discussed in this chapter are used to approximate solutions of equations of this type, when the exact solutions cannot be obtained by algebraic methods. The solution to this particular problem is considered in Exercise 20 of Section 2.3.

# 2.1 The Bisection Method

In this chapter, we consider one of the most basic problems of numerical approximation, the root-finding problem. This process involves finding a root,or solution, of an equation of the form $f ( x ) = 0$ , for a given function $f$ . A root of this equation is also called a zero of the function $f$ . The problem of finding an approximation to the root of an equation can be traced back at least as far as 17OO B.C.A cuneiform table in the Yale Babylonian Colection dating from that period gives a sexigesimal (base-6O) number equivalent to 1.414222 as an approximation to $\sqrt { 2 }$ ,a result that is accurate to within $1 0 ^ { - 5 }$ . This approximation can be found by applying a technique described in Exercise 19 of Section 2.2.

The first technique,based on the Intermediate Value Theorem, is called the Bisection, or Binary-search, method. Suppose $f$ is a continuous function defined on the interval $[ a , b ]$ ，with $f ( a )$ and $f ( b )$ of opposite sign.By the Intermediate Value Theorem, there exists a number $p$ in $( a , b )$ with $f ( p ) = 0$ . Although the procedure will work when there is more than one root in the interval $( a , b )$ ， we assume for simplicity that the root in this interval is unique. The method calls for a repeated halving of subintervals of $[ a , b ]$ and,at each step, locating the half containing $p$

To begin, set $a _ { 1 } = a$ and $b _ { 1 } = b$ , and let $p _ { 1 }$ be the midpoint of $[ a , b ]$ ; that is,

$$
p _ { 1 } = a _ { 1 } + \frac { b _ { 1 } - a _ { 1 } } { 2 } = \frac { a _ { 1 } + b _ { 1 } } { 2 } .
$$

If $f ( p _ { 1 } ) = 0$ ,then $p = p _ { 1 }$ , and we are done. If $f ( p _ { 1 } ) \neq 0$ ,then $f ( p _ { 1 } )$ has the same sign as either $f ( a _ { 1 } )$ or $f ( b _ { 1 } )$ . When $f ( p _ { 1 } )$ and $f ( a _ { 1 } )$ have the same sign, $p \in ( p _ { 1 } , b _ { 1 } )$ ，and we set $a _ { 2 } = p _ { 1 }$ and $b _ { 2 } = b _ { 1 }$ . When $f ( p _ { 1 } )$ and $f ( a _ { 1 } )$ have opposite signs, $p \in ( a _ { 1 } , p _ { 1 } )$ ， and we set $a _ { 2 } = a _ { 1 }$ and $b _ { 2 } = p _ { 1 }$ . We then reapply the process to the interval $\{ a _ { 2 } , b _ { 2 } ]$ . This produces the method described in Algorithm 2.1. (See Figure 2.1.)

![](images/dfe05380bb13ee4a14db4b01a009c8be41984565b1eebbb95311bfcd5f43edab.jpg)  
Figure 2.1

# Bisection

To find a solution to $f ( x ) = 0$ given the continuous function $f$ on the interval $[ a , b ]$ ,where $f ( a )$ and $f ( b )$ have opposite signs:

INPUT endpoints $a , b$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$ ·

OUTPUT approximate solution $p$ or message of failure.

Step 1 Set $i = 1$ ；$F A = f ( a ) .$

Step2 While $i \leq N _ { 0 }$ do Steps 3-6.

Step 3Set $p = a + ( b - a ) / 2$ (Compute pi.) $F P = f ( p )$

Step 4 If $F P = 0$ or $( b - a ) / 2 < T O L$ then OUTPUT $( p )$ ；  (Procedure completed successfully.) STOP.

Step 5Set $i \simeq i + 1$

Step 6If $F A \cdot F P > 0$ then set $a = p$ ； (Compute ai, bi.)$F A = F P$ else set $b = p$

Step 7OUTPUT(Method failed after $N _ { 0 }$ iterations, $N _ { 0 } = , N _ { 0 } )$ ； (The procedure was unsuccessful.) STOP.

Other stopping procedures can be applied in Step 4 of Algorithm 2.1 or in any of the iterative techniques in this chapter. For example,we can select a tolerance $\epsilon > 0$ and generate $p _ { 1 } , \ldots , p _ { N }$ until one of the following conditions is met:

$$
\begin{array} { r l } & { | p _ { N } - p _ { N - 1 } | < \epsilon , } \\ & { ~ } \\ & { \frac { | p _ { N } - p _ { N - 1 } | } { | p _ { N } | } < \epsilon , ~ p _ { N } \neq 0 , \quad \mathrm { ~ o r ~ } } \\ & { ~ } \\ & { | f ( p _ { N } ) | < \epsilon . } \end{array}
$$

Unfortunately, difficulties can arise using any of these stopping criteria. For example, there are sequences $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ with the property that the differences $p _ { n } \mathrm { ~ - ~ } p _ { n - 1 }$ converge to zero while the sequence itself diverges. (See Exercise 15.) It is also possible for $f ( p _ { n } )$ to be close to zero while $p _ { n }$ differs significantly from $p$ . (See Exercise 14.) Without additional knowledge about $f$ or $p$ , Inequality (2.2) is the best stopping criterion to apply because it comes closest to testing relative error.

When using a computer to generate approximations, it is good practice to set an upper bound on the number of iterations.This will eliminate the possibility of entering an infinite loop,a situation that can arise when the sequence diverges (and also when the program is incorrectly coded). This was done in Step 2 of Algorithm 2.1 where the bound $N _ { 0 }$ was set and the procedure terminated if $i > N _ { 0 }$

Note that to start the Bisection Algorithm,an interval $[ a , b ]$ must be found with $f ( a ) \cdot$ $f ( b ) < 0$ .At each step the length of the interval known to contain a zero of $f$ is reduced by a factor of 2; hence it is advantageous to choose the initial interval $[ a , b ]$ as small as possible.For example,if $f ( x ) = 2 x ^ { 3 } - x ^ { 2 } + x - 1$ , we have both

$$
f ( - 4 ) \cdot f ( 4 ) < 0 \quad \mathrm { a n d } \quad f ( 0 ) \cdot f ( 1 ) < 0 ,
$$

so the Bisection Algorithm could be used on either of the intervals $\{ - 4 , 4 \}$ or [0,1]. Starting the Bisection Algorithm on [0,1] instead of $[ - 4 , 4 ]$ will reduce by 3 the number of iterations required to achieve aspecified accuracy.

The following example ilustrates the Bisection Algorithm. The iteration in this example is terminated when the relative error is less than O.0o0l; that is, when

$$
{ \frac { | p - p _ { n } | } { | p | } } < 1 0 ^ { - 4 } .
$$

# EXAMPlE 1

The equation $f ( x ) = x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ has a root in [1,2] since $f ( 1 ) = - 5$ and $f ( 2 ) = 1 4$ . The Bisection Algorithm gives the values in Table 2.1.

Table 2.1   

<table><tr><td>n</td><td>an</td><td>bn</td><td>Pn</td><td>f(pn)</td></tr><tr><td>1</td><td>1.0</td><td>2.0</td><td>1.5</td><td>2.375</td></tr><tr><td>2</td><td>1.0</td><td>1.5</td><td>1.25</td><td>-1.79687</td></tr><tr><td>3</td><td>1.25</td><td>1.5</td><td>1.375</td><td>0.16211</td></tr><tr><td>4</td><td>1.25</td><td>1.375</td><td>1.3125</td><td>-0.84839</td></tr><tr><td>5</td><td>1.3125</td><td>1.375</td><td>1.34375</td><td>-0.35098</td></tr><tr><td>6</td><td>1.34375</td><td>1.375</td><td>1.359375</td><td>-0.09641</td></tr><tr><td>7</td><td>1.359375</td><td>1.375</td><td>1.3671875</td><td>0.03236</td></tr><tr><td>8</td><td>1.359375</td><td>1.3671875</td><td>1.36328125</td><td>-0.03215</td></tr><tr><td>9</td><td>1.36328125</td><td>1.3671875</td><td>1.365234375</td><td>0.000072</td></tr><tr><td>10</td><td>1.36328125</td><td>1.365234375</td><td>1.364257813</td><td>-0.01605</td></tr><tr><td>11</td><td>1.364257813</td><td>1.365234375</td><td>1.364746094</td><td>-0.00799</td></tr><tr><td>12</td><td>1.364746094</td><td>1.365234375</td><td>1.364990235</td><td>-0.00396</td></tr><tr><td>13</td><td>1.364990235</td><td>1.365234375</td><td>1.365112305</td><td>-0.00194</td></tr></table>

After 13 iterations, $p _ { 1 3 } = 1 . 3 6 5 1 1 2 3 0 5$ approximates the root $p$ with an error

$$
| p - p _ { 1 3 } | < | b _ { 1 4 } - a _ { 1 4 } | = | 1 . 3 6 5 2 3 4 3 7 5 - 1 . 3 6 5 1 1 2 3 0 5 | = 0 . 0 0 0 1 2 2 0 7 0 .
$$

Since $| a _ { 1 4 } | < | p |$ ，

$$
\frac { | p - p _ { 1 3 } | } { | p | } < \frac { | b _ { 1 4 } - a _ { 1 4 } | } { | a _ { 1 4 } | } \leq 9 . 0 \times 1 0 ^ { - 5 } ,
$$

so the approximation is correct to at least four significant digits. The correct value of $p$ ， to nine decimal places, is $p = 1 . 3 6 5 2 3 0 0 1 3 .$ Note that $p _ { 9 }$ is closer to $p$ than is the final approximation $p _ { 1 3 }$ . You might suspect this is true since $| f ( p _ { 9 } ) | < | f ( p _ { 1 3 } ) |$ ,but we cannot be sure of this unless the true answer is known.

The Bisection method, though conceptually clear, has significant drawbacks. It is slow to converge (that is, $N$ may become quite large before $\vert p - p _ { N } \vert$ is sufficiently small), and a good intermediate approximation can be inadvertently discarded. However, the method has the important property that it always converges to a solution, and for that reason it is often used as a starter for the more effcient methods we willpresent later in this chapter.

# Theorem 2.1

Suppose that $f \in C [ a , b ]$ and $f ( a ) \cdot f ( b ) < 0 ;$ The Bisection method generates a sequence $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ approximating a zero $p$ of $f$ with

$$
| p _ { n } - p | \leq { \frac { b - a } { 2 ^ { n } } } , \quad { \mathrm { w h e n } } \quad n \geq 1 .
$$

Proof For each $n \geq 1$ , we have

$$
b _ { n } - a _ { n } = { \frac { 1 } { 2 ^ { n - 1 } } } ( b - a ) \quad { \mathrm { a n d } } \quad p \in ( a _ { n } , b _ { n } ) .
$$

Since $\begin{array} { r } { p _ { n } = \frac { 1 } { 2 } ( a _ { n } + b _ { n } ) } \end{array}$ for all $n \geq 1$ , it follows that

$$
| p _ { n } - p | \leq { \frac { 1 } { 2 } } ( b _ { n } - a _ { n } ) = { \frac { b - a } { 2 ^ { n } } } .
$$

Since

$$
| p _ { n } - p | \leq ( b - a ) { \frac { 1 } { 2 ^ { n } } } ,
$$

the sequence $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ converges to $p$ with rate of convergence $O \left( { \frac { 1 } { 2 ^ { n } } } \right)$ ; that is,

$$
p _ { n } = p + O \left( { \frac { 1 } { 2 ^ { n } } } \right) .
$$

It is important to realize that Theorem 2.1 gives only a bound for approximation error and that this bound may be quite conservative. For example, this bound applied to the problem in Example 1 ensures only that

$$
| p - p 9 | \leq \frac { 2 - 1 } { 2 ^ { 9 } } \approx 2 \times 1 0 ^ { - 3 } ,
$$

but the actual error is much smaller:

$$
| p - p 9 | = | 1 . 3 6 5 2 3 0 0 1 3 - 1 . 3 6 5 2 3 4 3 7 5 | \approx 4 . 4 \times 1 0 ^ { - 6 } .
$$

To determine the number of iterations necessary to solve $f ( x ) = x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ with accuracy $1 0 ^ { - 3 }$ using $a _ { 1 } = 1$ and $b _ { 1 } = 2$ requires finding an integer $N$ that satisfies

$$
| p _ { N } - p | \leq 2 ^ { - N } ( b - a ) = 2 ^ { - N } < 1 0 ^ { - 3 } .
$$

To determine $N$ we will use logarithms. Although logarithms to any base would suf-fice, we will use base-10 logarithms since the tolerance is given as a power of 10. Since $2 ^ { - N } < 1 0 ^ { - 3 }$ implies that $\log _ { 1 0 } 2 ^ { - N } < \log _ { 1 0 } 1 0 ^ { - 3 } = - 3$ ,we have

$$
- N \log _ { 1 0 } 2 < - 3 \quad \mathrm { a n d } \quad N > \frac { 3 } { \log _ { 1 0 } 2 } \approx 9 . 9 6 .
$$

Hence, ten iterations will ensure an approximation accurate to within $1 0 ^ { - 3 }$ . Table 2.1 on page 51 shows that the value of $p _ { 9 } = 1 . 3 6 5 2 3 4 3 7 5$ is accurate to within $1 0 ^ { - 4 }$ . Again, it is important to keep in mind that the error analysis gives only a bound for the number of iterations,and in many cases this bound is much larger than the actual number required.

The bound for the number of iterations for the Bisection method assumes that the calculations are performed using infinite-digit arithmetic. When implementing the method on a computer, consideration must be given to the effects of roundoff error. For example, the computation of the midpoint of the interval $[ a _ { n } , b _ { n } ]$ should be found from the equation

$$
p _ { n } = a _ { n } + { \frac { b _ { n } - a _ { n } } { 2 } }
$$

instead of from the algebraically equivalent equation

$$
p _ { n } = { \frac { a _ { n } + b _ { n } } { 2 } } .
$$

The first equation adds a small correction, $( b _ { n } - a _ { n } ) / 2$ , to the known value $a _ { n }$ . When $b _ { n } - a _ { n }$ is near the maximum precision of the machine this correction might be in error, but the error would not significantly afect the computed value of ${ p _ { n } }$ . However, when $b _ { n } - a _ { n }$ is near the maximum precision of the machine, it is possible for $( a _ { n } + b _ { n } ) / 2$ to return a midpoint that is not even in the interval $[ a _ { n } , b _ { n } ]$

As a final remark, to determine which subinterval of $[ a _ { n } , b _ { n } ]$ contains a root of $f$ ,it is better to make use of the signum function, which is defined as

$$
\operatorname { s g n } ( x ) = { \left\{ \begin{array} { l l } { - 1 , } & { { \mathrm { i f ~ } } x < 0 , } \\ { 0 , } & { { \mathrm { i f ~ } } x = 0 , } \\ { 1 , } & { { \mathrm { i f ~ } } x > 0 . } \end{array} \right. }
$$

The test

$$
\operatorname { s g n } \left( f ( a _ { n } ) \right) \operatorname { s g n } \left( f ( p _ { n } ) \right) < 0 \qquad { \mathrm { i n s t e a d ~ o f } } \qquad f ( a _ { n } ) f ( p _ { n } ) < 0
$$

gives the same result but avoids the possbility of overflow or underflow in the multiplication of $f ( a _ { n } )$ and $f ( p _ { n } )$ ·

# Exercise set 2.1

1.Use the Bisection method to find $p _ { 3 }$ for $f ( x ) = { \sqrt { x } } - \cos x$ on [0, 1].

2.Let $f ( x ) = 3 ( x + 1 ) ( x - { \textstyle { \frac { 1 } { 2 } } } ) ( x - 1 )$ . Use the Bisection method on the following intervals to find $p _ { 3 }$

a. [-2,1.5] $\begin{array} { r l } { \mathbf { b } . \ } & { { } [ - 1 . 2 5 , 2 . 5 ] } \end{array}$

3.Use the Bisection method to find solutions accurate to within $1 0 ^ { - 2 }$ for $x ^ { 3 } - 7 x ^ { 2 } + 1 4 x - 6 = 0$ on each interval.

a.[0,1] b.[1,3.2] c.[3.2,4]

4.Use the Bisection method to find solutions accurate to within $1 0 ^ { - 2 }$ for $x ^ { 4 } - 2 x ^ { 3 } - 4 x ^ { 2 } + 4 x +$ ${ \pmb 4 } = { \pmb 0 }$ on each interval.

a.[-2,-1] b.[0,2] c.[2,3] $\mathbf { d } . \quad \ [ - 1 , 0 ]$

5.Use the Bisection method to find a solution accurate to within $1 0 ^ { - 3 }$ for $x = \tan x $ on [4, 4.

$6$ Use the Bisection method to find a solution accurate to within $1 0 ^ { - 3 }$ for $2 + \cos ( e ^ { x } - 2 ) - e ^ { x } = 0$ on [0.5, 1.5].

7.Use the Bisection method to find solutions accurate to within $1 0 ^ { - 5 }$ for the following problems.

a. $x - 2 ^ { - x } = 0 \quad { \mathrm { ~ f o r ~ } } 0 \leq x \leq 1$   
$\mathbf { b } _ { \bullet }$ $e ^ { x } - x ^ { 2 } + 3 x - 2 = 0 \quad { \mathrm { ~ f o r ~ } } 0 \leq x \leq 1$   
${ \pmb { \mathfrak { c } } } _ { \ast }$ $\begin{array} { r l } & { 2 x \cos ( 2 x ) - ( x + 1 ) ^ { 2 } = 0 \quad \mathrm { ~ f o r } - 3 \leq x \leq - 2 \quad \mathrm { ~ a n d ~ } \quad - 1 \leq x \leq 0 } \\ & { x \cos x - 2 x ^ { 2 } + 3 x - 1 = 0 \quad \mathrm { ~ f o r } 0 . 2 \leq x \leq 0 . 3 \quad \mathrm { ~ a n d ~ } \quad 1 . 2 \leq x \leq 1 . 3 } \end{array}$ d.

8. Let $f ( x ) = ( x + 2 ) ( x + 1 ) ^ { 2 } x ( x - 1 ) ^ { 3 } ( x - 2 )$ . To which zero of $f$ does the Bisection method converge when applied on the following intervals?

a. [-1.5,2.5] b. [-0.5,2.4] $\begin{array} { r l } { \mathbf { c } . \quad } & { { } [ - 0 . 5 , 3 ] \qquad \mathbf { d } . \quad [ - 3 , - 0 . 5 ] } \end{array}$

9.Let $f ( x ) = ( x + 2 ) ( x + 1 ) x ( x - 1 ) ^ { 3 } ( x - 2 )$ . To which zero of $f$ does the Bisection methoc converge when applied on the following intervals?

a.[-3,2.5] $b , \ \{ - 2 . 5 , 3 \}$ $\begin{array} { r l } { \mathbf { c } . \quad } & { { } [ - 1 . 7 5 , 1 . 5 ] } \end{array} \qquad \begin{array} { r l } { \mathbf { d } . \quad } & { { } [ - 1 . 5 , 1 . 7 5 ] } \end{array}$

10.Find an approximation to $\sqrt { 3 }$ correct to within $1 0 ^ { - 4 }$ using the Bisection Algorithm. [Hint: Consider $f ( x ) = x ^ { 2 } - 3 . ]$

1．Find an approximation to $\sqrt [ 3 ] { 2 5 }$ correct to within $1 0 ^ { - 4 }$ using the Bisection Algorithm.

12. Use Theorem 2.1 to find a bound for the number of iterations needed to achieve an approximation with accuracy $1 0 ^ { - 3 }$ to the solution of $x ^ { 3 } + x - 4 = 0$ lying in the interval [1,4].Find an approximation to the root with this degree of accuracy.

13. Use Theorem 2.1 to find a bound for the number of iterations needed to achieve an approximation with accuracy $1 0 ^ { - 4 }$ to the solution of $x ^ { 3 } - x - 1 = 0$ lying in the interval [1,2].Find an approximation to the root with this degree of accuracy.

14.Let $f ( x ) = ( x - 1 ) ^ { 1 0 }$ ， $p = 1$ ,and $p _ { n } = 1 + 1 / n$ . Show that $| f ( p _ { n } ) | < 1 0 ^ { - 3 }$ whenever $n > 1$ but that $| p - p _ { n } | < 1 0 ^ { - 3 }$ requires that $n > 1 0 0 0$

15.Let $\{ p _ { n } \}$ be the sequence defined by $\begin{array} { r } { p _ { n } \ = \ \sum _ { k = 1 } ^ { n } \frac { 1 } { k } } \end{array}$ . Show that $\{ p _ { n } \}$ diverges even though $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } ( p _ { n } - p _ { n - 1 } ) = 0 } \end{array}$

16.The function defined by $f ( x ) = \sin \pi x$ has zeros at every integer. Show that when $- 1 < a <$ 0 and $2 < b < 3$ , the Bisection method converges to

$$
\begin{array} { r } { 0 , \quad \mathrm { i f } \quad a + b < 2 \qquad \mathbf { b } . \quad 2 , \quad \mathrm { i f } \quad a + b > 2 \qquad \mathbf { c } . \quad 1 , \quad \mathrm { i f } \quad a + b = 2 } \end{array}
$$

17.A trough of length $L$ has a cross section in the shape of a semicircle with radius $r$ (See the accompanying figure.) When filled with water to within a distance $h$ of the top, the volume $V$ of water is

$$
V = L \left[ 0 . 5 \pi r ^ { 2 } - r ^ { 2 } \arcsin ( h / r ) - h ( r ^ { 2 } - h ^ { 2 } ) ^ { 1 / 2 } \right] .
$$

![](images/871d4eff5290c09ca6e75189ef9111cd4da21e4d4e6a52a26742550c2639f025.jpg)

Suppose $L = 1 0$ ft, $r = 1$ ft,and $V = 1 2 . 4 ~ \mathrm { f t } ^ { 3 }$ . Find the depth of water in the trough to within 0.01 ft.

18.A particle starts at rest on a smooth inclined plane whose angle $\theta$ is changing at a constant rate

$$
\frac { d \theta } { d t } = \omega < 0 .
$$

At the end of $t$ seconds,the position of the object is given by

$$
x ( t ) = - \frac { g } { 2 \omega ^ { 2 } } \left( \frac { e ^ { w t } - e ^ { - w t } } { 2 } - \sin { \omega t } \right) .
$$

Suppose the particle has moved 1.7 ft in 1 s.Find, to within 10-5,the rate ω at which θ changes. Assume that g = 32.17 ft/s².

![](images/faae15d9b7b75205da2f3365b3dce4ee06c5dcedfcede1c904773eb49aa6c6f3.jpg)

# 2.2 Fixed-Point Iteration

A number p is a fixed point for a given function g if g(p) = p. In this section we consider the problem of finding solutions to fixed-point problems and the connection between the fixed-point problems and the root-finding problems we wish to solve.

Root-finding problems and fixed-point problems are equivalent classes in the following sense:

Given a root-finding problem $f ( p ) = 0$ ， we can define functions $\pmb { g }$ with a fixed point at p in a number of ways,for example,as g(x)= x - f(x) or as g(x)= x +3f(x). Conversely, if the function $\pmb { g }$ has a fixed point at $p$ , then the function defined by $f ( x ) =$ $x - g ( x )$ has a zero at $p$ ·

Although the problems we wish to solve are in the root-finding form, the fixed-point form is easier to analyze, and certain fixed-point choices lead to very powerful root-finding techniques.

We first need to become comfortable with this new type of problem and to decide when a function has a fixed point and how the fixed points can be approximated to within a specified accuracy.

The function $g ( x ) = x ^ { 2 } - 2 .$ for $- 2 \leq x \leq 3$ , has fixed points at $x = - 1$ and $x = 2$ since

$$
g ( - 1 ) = ( - 1 ) ^ { 2 } - 2 = - 1 \quad \mathrm { ~ a n d ~ } \quad g ( 2 ) = 2 ^ { 2 } - 2 = 2 .
$$

This can be seen in Figure 2.2.

![](images/133b26b7dc85e6b39e43e2775b26bfb5db5e750314b97772058ec17400117af2.jpg)  
Figure 2.2

The following theorem gives sufficient conditions for the existence and uniqueness of a fixed point.

a.If $g \in C [ a , b ]$ and $g ( x ) \in [ a , b ]$ for all $x \in [ a , b ]$ then $\pmb { g }$ has a fixed point in $[ a , b ]$ b.If, in addition, $g ^ { \prime } ( x )$ exists on $( a , b )$ and a positive constant $k < 1$ exists with

$$
| g ^ { \prime } ( x ) | \leq k , \quad { \mathrm { f o r ~ a l l ~ } } x \in ( a , b ) ,
$$

then the fixed point in $[ a , b ]$ is unique. (See Figure 2.3.)

![](images/915b2ed102f963ec2cbb29f11daa8894a0ae2b03c8b28238d0ffb0b4ce450e54.jpg)  
Figure 2.3

# Proof

a.If $g ( a ) = a$ or $g ( b ) = b$ ,then $\pmb { g }$ has a fixed point at an endpoint. If not, then $g ( a ) > a$ and $g ( b ) < b$ . The function $h ( x ) = g ( x ) - x$ is continuous on $[ a , b ]$ ， with

$$
h ( a ) = g ( a ) - a > 0 \quad { \mathrm { a n d } } \quad h ( b ) = g ( b ) - b < 0 .
$$

The Intermediate Value Theorem implies that there exists $p \in ( a , b )$ for which $h ( p ) = 0$ . This number $p$ is a fixed point for $\pmb { g }$ since

$$
0 = h ( p ) = g ( p ) - p \quad { \mathrm { i m p l i e s ~ t h a t } } \quad g ( p ) = p .
$$

b. Suppose, in addition, that $| g ^ { \prime } ( x ) | \leq k < 1$ and that $p$ and $\pmb q$ are both fixed points in $[ a , b ]$ .If $p \neq q$ ,then the Mean Value Theorem implies that a number $\pmb { \xi }$ exists between $p$ and $\pmb q$ , and hence in $[ a , b ]$ ,with

$$
{ \frac { g ( p ) - g ( q ) } { p - q } } = g ^ { \prime } ( \xi ) .
$$

Thus,

$$
| p - q | = | g ( p ) - g ( q ) | = | g ^ { \prime } ( \xi ) | | p - q | \leq k | p - q | < | p - q | ,
$$

which is a contradiction. This contradiction must come from the only suppositin, $p \neq q$ . Hence, $p = q$ and the fixed point in $[ a , b ]$ is unique. ■

a. Let $g ( x ) = ( x ^ { 2 } - 1 ) / 3$ on $[ - 1 , 1 ]$ . The Extreme Value Theorem implies that the absolute minimum of $\pmb { \mathrm { g } }$ occurs at $x = 0$ and $\begin{array} { r } { g ( 0 ) = - \frac { 1 } { 3 } } \end{array}$ . Similarly,the absolute maximum of $\pmb { g }$ occurs at $x = \pm 1$ and has the value $g ( \pm 1 ) = 0$ . Moreover, $\pmb { g }$ is continuous and

$$
| g ^ { \prime } ( x ) | = \left| { \frac { 2 x } { 3 } } \right| \leq { \frac { 2 } { 3 } } , \quad { \mathrm { f o r ~ a l l ~ } } x \in ( - 1 , 1 ) .
$$

So $g$ satisfies all the hypotheses of Theorem 2.2 and has a unique fixed point in $[ - 1 , 1 ]$

In this example, the unique fixed point $p$ in the interval [-1,1] can be determined algebraically. If

$$
p = g ( p ) = \frac { p ^ { 2 } - 1 } { 3 } , \quad \mathrm { t h e n } \quad p ^ { 2 } - 3 p - 1 = 0 ,
$$

which, by the quadratic formula, implies that

$$
p = { \frac { 1 } { 2 } } ( 3 - \sqrt { 1 3 } ) .
$$

Note that $\pmb { \cal { g } }$ also has a unique fixed point $p = { \frac { 1 } { 2 } } ( 3 + { \sqrt { 1 3 } } )$ for the interval [3,4]. However,g(4) = 5and g'(4) =  > 1,so g does not satisfy the hypotheses of Theorem 2.2 on [3,4]. Hence, the hypotheses of Theorem 2.2 are sufficient to guarantee a unique fixed point but are not necessary. (See Figure 2.4.)

![](images/7c142c4aee74ffeeff6e6609806501e1ce8791540368e64703f3411da48b80bc.jpg)  
Figure 2.4

b. Let $g ( x ) = 3 ^ { - x }$ . Since $g ^ { \prime } ( x ) = - 3 ^ { - x } \ln 3 < 0$ on [0,1],the function $g$ is decreasing on [0,1]. So

$$
g ( 1 ) = \frac { 1 } { 3 } \leq g ( x ) \leq 1 = g ( 0 ) , \quad \mathrm { f o r } \quad 0 \leq x \leq 1 .
$$

Thus, for $x \in \left\{ 0 , 1 \right\}$ , we have $g ( x ) \in [ 0 , 1 ]$ ,and $g$ has a fixed point in [O,1]. Since

$$
g ^ { \prime } ( 0 ) = - \ln 3 = - 1 . 0 9 8 6 1 2 2 8 9 ,
$$

![](images/81e7d60c00aa3dccdfb38e1b5d7527a9e4a8f0fc0eac7e9c262527ce9e8c452b.jpg)  
Figure 2.5

$| g ^ { \prime } ( x ) | \not \leq 1 \mathrm { o n } ( 0 , 1 )$ ,and Theorem 2.2 cannot be used to determine uniqueness. However, $g$ is always decreasing,and it is clear from Figure 2.5 that the fixed point must be unique.

To approximate the fixed point of a function $g$ ，we choose an initial approximation $p _ { 0 }$ and generate the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ by letting $p _ { n } = g ( p _ { n - 1 } )$ , for each $n \geq 1$ . If the sequence converges to $p$ and $\pmb { g }$ is continuous, then

$$
p = \operatorname* { l i m } _ { n \to \infty } p _ { n } = \operatorname* { l i m } _ { n \to \infty } g ( p _ { n - 1 } ) = g \left( \operatorname* { l i m } _ { n \to \infty } p _ { n - 1 } \right) = g ( p ) ,
$$

and a solution to $x = g ( x )$ is obtained. This technique is called fixed-point iteration, or functional iteration. The procedure is detailed in Algorithm 2.2 and illustrated in Figure 2.6.

![](images/95a7ea05cc68b8ac359b49e0488dcf4980745c5ac2ffdd7289854fe52478c109.jpg)  
Figure 2.6

![](images/4a51dac14136890655629b493c3db9855487f4cc540f27108d2d9720db2ea5a5.jpg)

# Fixed-Point Iteration

To find a solution to $p = g ( p )$ given an initial approximation $p _ { 0 }$ ：

INPUTinitial approximation $p _ { 0 }$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$ OUTPUTapproximate solution $p$ or message of failure.

Step 1 Set $i = 1$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-6.

Step 3 Set $p = g ( p _ { 0 } )$ (Compute pi.)

Step 4If $| p - p _ { 0 } | < T O L$ then OUTPUT $( p )$ ;(The procedure was successful.)

STOP.

Step 5Set $i = i + 1$

Step 6 Set $p _ { 0 } = p$ (Update po.)

Step 7OUTPUT('The method failed after $N _ { 0 }$ iterations, $N _ { 0 } = , N _ { 0 }$ ； (The procedure was unsuccessful.) STOP.

The following example illustrates functional iteration.

# EXAMPlE 3

The equation $x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ has a unique root in[1,2]. There are many ways to change the equation to the fixed-point form $x = g ( x )$ using simple algebraic manipulation. For example, to obtain the function $\pmb { g }$ described in part (c),we can manipulate the equation $x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ as follows:

$$
4 x ^ { 2 } = 1 0 - x ^ { 3 } , \quad \mathrm { } s o \quad x ^ { 2 } = { \frac { 1 } { 4 } } ( 1 0 - x ^ { 3 } ) ,
$$

and

$$
x = \pm \frac { 1 } { 2 } ( 1 0 - x ^ { 3 } ) ^ { 1 / 2 } .
$$

To obtain a positive solution, ${ \pmb g } _ { 3 } ( { \pmb x } )$ is chosen. It is not important to derive the functions shown here,but you should verify that the fixed point of each is actually a solution to the original equation, $x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$

a. b $\begin{array} { l } { { x = g _ { 1 } ( x ) = x - x ^ { 3 } - 4 x ^ { 2 } + 1 0 } } \\ { { \displaystyle x = g _ { 2 } ( x ) = \left( \frac { 1 0 } { x } - 4 x \right) ^ { 1 / 2 } } } \end{array}$ c. $x = g _ { 3 } ( x ) = \frac { 1 } { 2 } ( 1 0 - x ^ { 3 } ) ^ { 1 / 2 }$ $x = g _ { 4 } ( x ) = \left( \frac { 1 0 } { 4 + x } \right) ^ { 1 / }$ )1/2 d e. $x = g _ { 5 } ( x ) = x - { \frac { x ^ { 3 } + 4 x ^ { 2 } - 1 0 } { 3 x ^ { 2 } + 8 x } }$

With $p _ { 0 } = 1 . 5$ ,Table 2.2 lists the results of the fixed-point iteration for all five choices of $g$

The actual root is 1.365230013,as was noted in Example 1 of Section 2.1. Comparing the results to the Bisection Algorithm given in that example, it can be seen that excellent results have been obtained for choices (c), (d),and (e), since the Bisection method requires 27 iterations for this accuracy. It is interesting to note that choice (a) was divergent and that (b) became undefined because it involved the square root of a negative number.

Even though the various functions in Example 3 are fixed-point problems for the same root-finding problem, they differ vastly as techniques for approximating the solution to the root-finding problem. Their purpose is to illustrate the true question that needs to be answered:

Table 2.2   

<table><tr><td>n</td><td>（a)</td><td>(b)</td><td>(c）</td><td>(d)</td><td>(e)</td></tr><tr><td>0</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td><td>1.5</td></tr><tr><td>1</td><td>-0.875 6.732</td><td>0.8165</td><td>1.286953768</td><td>1.348399725</td><td>1.373333333</td></tr><tr><td>2</td><td>-469.7</td><td>2.9969</td><td>1.402540804</td><td>1.367376372</td><td>1.365262015</td></tr><tr><td>3</td><td>1.03 × 108</td><td>(-8.65)1/2</td><td>1.345458374</td><td>1.364957015</td><td>1.365230014</td></tr><tr><td>4</td><td></td><td></td><td>1.375170253</td><td>1.365264748</td><td>1.365230013</td></tr><tr><td>5</td><td></td><td></td><td>1.360094193</td><td>1.365225594</td><td></td></tr><tr><td>6</td><td></td><td></td><td>1.367846968</td><td>1.365230576</td><td></td></tr><tr><td>7</td><td></td><td></td><td>1.363887004</td><td>1.365229942</td><td></td></tr><tr><td>8</td><td></td><td></td><td>1.365916734</td><td>1,365230022</td><td></td></tr><tr><td>9</td><td></td><td></td><td>1.364878217</td><td>1.365230012</td><td></td></tr><tr><td>10</td><td></td><td></td><td>1.365410062</td><td>1.365230014</td><td></td></tr><tr><td>15</td><td></td><td></td><td>1.365223680</td><td>1.365230013</td><td></td></tr><tr><td>20</td><td></td><td></td><td>1.365230236</td><td></td><td></td></tr><tr><td>25</td><td></td><td></td><td>1.365230006</td><td></td><td></td></tr><tr><td>30</td><td></td><td></td><td>1.365230013</td><td></td><td></td></tr></table>

How can we find a fixed-point problem that produces a sequence that reliably and rapidly converges to a solution to a given root-finding problem?

The following theorem and itscorolary give us some clues concerning the paths we should pursue and, perhaps more importantly, some we should reject.

# Theorem 2.3

# (Fixed-Point Theorem)

Let $g \in C [ a , b ]$ be such that $g ( x ) \in [ a , b ]$ , for all $\pmb { x }$ in $[ a , b ]$ . Suppose, inaddition, that $g ^ { \prime }$ exists on $( a , b )$ and that a constant $0 < k < 1$ exists with

$$
| g ^ { \prime } ( x ) | \leq k , \quad { \mathrm { f o r ~ a l l ~ } } x \in ( a , b ) .
$$

Then, for any number $p _ { 0 }$ in $[ a , b ]$ ,the sequence defined by

$$
p _ { n } = g ( p _ { n - 1 } ) , \quad n \ge 1 ,
$$

converges to the unique fixed point $p$ in $[ a , b ]$

Proof Theorem 2.2 implies that a unique fixed point exists in $[ a , b ]$ . Since $\pmb { g }$ maps $[ a , b ]$ into itself, the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is defined for all $n \geq 0$ ,and $p _ { n } \in [ a , b ]$ for all $\pmb { n }$ .Using the fact that $| g ^ { \prime } ( x ) | \leq k$ and the Mean Value Theorem, we have, for each $\pmb { n }$ ，

$$
| p _ { n } - p | = | g ( p _ { n - 1 } ) - g ( p ) | = | g ^ { \prime } ( \xi _ { n } ) | | p _ { n - 1 } - p | \leq k | p _ { n - 1 } - p | ,
$$

where $\xi _ { n } \in ( a , b )$ . Applying this inequality inductively gives

$$
| p _ { n } - p | \leq k | p _ { n - 1 } - p | \leq k ^ { 2 } | p _ { n - 2 } - p | \leq \cdots \leq k ^ { n } | p _ { 0 } - p | .
$$

Since $0 < k < 1$ , we have $\scriptstyle \operatorname* { l i m } _ { n \to \infty } k ^ { n } = 0$ and

$$
\operatorname* { l i m } _ { n \to \infty } | p _ { n } - p | \leq \operatorname* { l i m } _ { n \to \infty } k ^ { n } | p _ { 0 } - p | = 0 .
$$

Hence, $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to $p$

# Corollary 2.4

If $\pmb { g }$ satisfies tehypothesesofTeorm2.3,tenbpundsfortheerrr ivoldinusing $p _ { n }$ to approximate $p$ are given by

$$
| p _ { n } - p | \leq k ^ { n } \operatorname* { m a x } \{ p _ { 0 } - a , b - p _ { 0 } \}
$$

and

$$
| p _ { n } - p | \leq { \frac { k ^ { n } } { 1 - k } } | p _ { 1 } - p _ { 0 } | , \quad { \mathrm { f o r ~ a l l } } \quad n \geq 1 .
$$

Proof Since $p \in [ a , b ]$ ,the first bound follows from Inequality (2.4):

$$
\begin{array} { r } { \vert p _ { n } - p \vert \leq k ^ { n } \vert p _ { 0 } - p \vert \leq k ^ { n } \operatorname* { m a x } \{ p _ { 0 } - a , b - p _ { 0 } \} . } \end{array}
$$

For $n \geq 1$ , the procedure used in the proof of Theorem 2.3 implies that

$$
| p _ { n + 1 } - p _ { n } | = | g ( p _ { n } ) - g ( p _ { n - 1 } ) | \leq k | p _ { n } - p _ { n - 1 } | \leq \cdots \leq k ^ { n } | p _ { 1 } - p _ { 0 } | .
$$

Thus, for $m > n \geq 1$ ，

$$
\begin{array} { r l } & { \lfloor p _ { m } - p _ { n } \rfloor = \lfloor p _ { m } - p _ { m - 1 } + p _ { m - 1 } - \cdot \cdot \cdot + p _ { n + 1 } - p _ { n } \rfloor } \\ & { \qquad \le \lfloor p _ { m } - p _ { m - 1 } \rfloor + \lfloor p _ { m - 1 } - p _ { m - 2 } \rfloor + \cdot \cdot \cdot + \lfloor p _ { n + 1 } - p _ { n } \rfloor } \\ & { \qquad \le k ^ { m - 1 } | p _ { 1 } - p _ { 0 } | + k ^ { m - 2 } | p _ { 1 } - p _ { 0 } | + \cdot \cdot \cdot + k ^ { n } | p _ { 1 } - p _ { 0 } | } \\ & { \qquad = k ^ { n } | p _ { 1 } - p _ { 0 } | \left( 1 + k + k ^ { 2 } + \cdot \cdot \cdot + k ^ { m - n - 1 } \right) . } \end{array}
$$

By Theorem 2.3, $\scriptstyle \operatorname* { l i m } _ { m \to \infty } p _ { m } = p$ ,so

$$
| p - p _ { n } | = \operatorname* { l i m } _ { m  \infty } | p _ { m } - p _ { n } | \leq \operatorname* { l i m } _ { m  \infty } k ^ { n } | p _ { 1 } - p _ { 0 } | \sum _ { i = 0 } ^ { m - n - 1 } k ^ { i } \leq k ^ { n } | p _ { 1 } - p _ { 0 } | \sum _ { i = 0 } ^ { \infty } k ^ { i } .
$$

But $\sum _ { i = 0 } ^ { \infty } k ^ { i }$ is a geometric series with ratio $k$ and $0 < k < 1$ . This sequence converges to $1 / ( 1 - k )$ , which gives the second bound:

$$
| p - p _ { n } | \leq { \frac { k ^ { n } } { 1 - k } } | p _ { 1 } - p _ { 0 } | .
$$

Both inequalities inthecorollary relate therate at which $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to the bound $k$ on the first derivative. The rate of convergence depends on the factor $k ^ { n }$ .The smaller the value of $k$ , the faster the convergence, which may be very slow if $k$ is close to 1. In the following example, the fixed-point methods in Example 3 are reconsidered in light ofthe results presented in Theorem 2.3 and its corollary.

a. For $g _ { 1 } ( x ) = x - x ^ { 3 } - 4 x ^ { 2 } + 1 0$ , we have $g _ { 1 } ( 1 ) = 6$ and $g _ { 1 } ( 2 ) = - 1 2$ ， $\mathbf { s o } \ g _ { 1 }$ does not map [1, 2] into itself. Moreover, $g _ { 1 } ^ { \prime } ( x ) = 1 - 3 x ^ { 2 } - 8 x$ ， $\mathfrak { s o } | g _ { 1 } ^ { \prime } ( x ) | > 1$ for all $x$ in [1,2]. Although Theorem 2.3 does not guarantee that the method must fail for this choice of $\pmb { g }$ , there is no reason to expect convergence.

b.With $g _ { 2 } ( x ) = [ ( 1 0 / x ) - 4 x ] ^ { 1 / 2 }$ , we can see that ${ \pmb g } _ { 2 }$ does not map [1, 2] into [1,2], and the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is not defined when $p _ { 0 } = 1 . 5$ . Moreover, there is no interval containing $p \approx 1 . 3 6 5$ such that

$$
| g _ { 2 } ^ { \prime } ( x ) | < 1 , \quad \mathrm { s i n c e } \quad | g _ { 2 } ^ { \prime } ( p ) | \approx 3 . 4 .
$$

There is no reason to expect that this method will converge.

c. For the function $\begin{array} { r } { g _ { 3 } ( x ) = \frac { 1 } { 2 } ( 1 0 - x ^ { 3 } ) ^ { 1 / 2 } , } \end{array}$

$$
g _ { 3 } ^ { \prime } ( x ) = - \frac { 3 } { 4 } x ^ { 2 } ( 1 0 - x ^ { 3 } ) ^ { - 1 / 2 } < 0 \quad \mathrm { o n } [ 1 , 2 ] ,
$$

so ${ \pmb g } _ { 3 }$ is strictly decreasing on [1,2]. However, $| g _ { 3 } ^ { \prime } ( 2 ) | \approx 2 . 1 2$ ， so the condition $| g _ { 3 } ^ { \prime } ( x ) | \le k < 1$ failson[1,2]Acoereaaooftesequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ starting with $p _ { 0 } = 1 . 5$ shows that it suffices to consider the interval [1, 1.5] instead of [1,2]. On this interval it is still true that $g _ { 3 } ^ { \prime } ( x ) < 0$ and $g _ { 3 }$ is strictly decreasing, but, additionally,

$$
1 < 1 . 2 8 \approx g _ { 3 } ( 1 . 5 ) \leq g _ { 3 } ( x ) \leq g _ { 3 } ( 1 ) = 1 . 5 ,
$$

for all $x \in [ 1 , 1 . 5 ]$ . This shows that $g _ { 3 }$ maps the interval [1, 1.5] into itself. Since it is also true that $| g _ { 3 } ^ { \prime } ( x ) | \le | g _ { 3 } ^ { \prime } ( 1 . 5 ) | \approx 0 . 6 6$ On this interval, Theorem 2.3 confirms the convergence of which we were already aware.

d.For $g _ { 4 } ( x ) = ( 1 0 / ( 4 + x ) ) ^ { 1 / 2 }$ , we have

$$
| g _ { 4 } ^ { \prime } ( x ) | = \left| \frac { - 5 } { \sqrt { 1 0 } ( 4 + x ) ^ { 3 / 2 } } \right| \leq \frac { 5 } { \sqrt { 1 0 } ( 5 ) ^ { 3 / 2 } } < 0 . 1 5 , \quad \mathrm { f o r ~ a l l } \quad x \in \{ 1 , 2 \} .
$$

The bound on the magnitude of $g _ { 4 } ^ { \prime } ( x )$ is much smaller than the bound (found in (c)) on the magnitude of ${ \pmb g } _ { 3 } ^ { \prime } ( { \pmb x } )$ , which explains the more rapid convergence using $g _ { 4 }$ ·

e. The sequence defined by

$$
g _ { 5 } ( x ) = x - { \frac { x ^ { 3 } + 4 x ^ { 2 } - 1 0 } { 3 x ^ { 2 } + 8 x } }
$$

converges much more rapidly than our other choices. In the next sections we will see where this choice came from and why it is so effective.

# EXERCIsE Set 2.2

1. Use algebraic manipulation to show that each of the following functions has a fixed point at $p$ precisely when $f ( p ) = 0$ ，where $f ( x ) = x ^ { 4 } + 2 x ^ { 2 } - x - 3 .$

$$
\begin{array} { l l l } { { } } & { { \begin{array} { l l l l } { } & { { \mathrm { P } ^ { \scriptscriptstyle 4 , 5 } < \cdots < x \leq w \leq z ) \ , \ \mathrm { w } ^ { \scriptscriptstyle 5 } , \ \cdots > \ \cdots < \ > \ , \ \cdots < \ x > w \leq z } \ , \ \mathrm { w } ^ { \scriptscriptstyle 7 } \cdots > \ } } & { { \mathrm { } \stackrel { } { } } } & { {  } } \\ { { } } & { { } } & { { } } \\ { { \mathrm { \bf 4 . } \quad g _ { 1 } ( x ) = ( 3 + x - 2 x ^ { 2 } ) ^ { 1 / 4 } } } & { { \mathrm { } } } & { { \mathrm { \bf \bf { b . } } \quad g _ { 2 } ( x ) = ( { \frac { x + 3 - x ^ { 4 } } { 2 } } ) ^ { 1 / 2 } } } \end{array} }  \end{array}
$$

$$
g _ { 3 } ( x ) = \left( { \frac { x + 3 } { x ^ { 2 } + 2 } } \right) ^ { 1 / 2 } \qquad \mathrm { d . } \quad g _ { 4 } ( x ) = { \frac { 3 x ^ { 4 } + 2 x ^ { 2 } + 3 } { 4 x ^ { 3 } + 4 x - 1 } }
$$

2. $\clubsuit _ { \bullet }$ Perform four iterations,if possible, on each of the functions $\pmb { \ 8 }$ defined in Exercise 1. Let $p _ { 0 } = 1$ and $p _ { n + 1 } = g ( p _ { n } )$ ,for $n _ { \cdot } = 0 , 1 , 2 , 3$

b.Which function do you think gives the best approximation to the solution?

3.The following four methods are proposed to compute $2 1 ^ { 1 / 3 }$ . Rank them inorder, based on their apparent speed of convergence, assuming $p _ { 0 } = 1$

$$
\begin{array} { l } { { p _ { n } = { \displaystyle \frac { 2 0 p _ { n - 1 } + 2 1 / p _ { n - 1 } ^ { 2 } } { 2 1 } } \qquad \qquad \mathrm { b . } \quad p _ { n } = p _ { n - 1 } - { \displaystyle \frac { p _ { n - 1 } ^ { 3 } - 2 1 } { 3 p _ { n - 1 } ^ { 2 } } } } } \\ { { p _ { n } = p _ { n - 1 } - { \displaystyle \frac { p _ { n - 1 } ^ { 4 } - 2 1 p _ { n - 1 } } { p _ { n - 1 } ^ { 2 } - 2 1 } } \qquad \qquad \mathrm { d . } \quad p _ { n } = \left( { \displaystyle \frac { 2 1 } { p _ { n - 1 } } } \right) ^ { 1 / 2 } } } \end{array}
$$

4. The following four methods are proposed to compute $7 ^ { 1 / 5 }$ . Rank them in order, based on their apparent speed of convergence, assuming $p _ { 0 } = 1$ ·

$$
\begin{array} { l l } { { p _ { n } = \displaystyle \left( 1 + \frac { 7 - p _ { n - 1 } ^ { 3 } } { p _ { n - 1 } ^ { 2 } } \right) ^ { 1 / 2 } \qquad } } & { { \mathrm { b } , \quad p _ { n } = p _ { n - 1 } - \frac { p _ { n - 1 } ^ { 5 } - 7 } { p _ { n - 1 } ^ { 2 } } } } \\ { { p _ { n } = p _ { n - 1 } - \frac { p _ { n - 1 } ^ { 5 } - 7 } { 5 p _ { n - 1 } ^ { 4 } } \qquad } } & { { \mathrm { d } , \quad p _ { n } = p _ { n - 1 } - \frac { p _ { n - 1 } ^ { 5 } - 7 } { 1 2 } } } \end{array}
$$

5. Use a fixed-point iteration method to determine a solution accurate to within $1 0 ^ { - 2 }$ for $x ^ { 4 } -$ $3 x ^ { 2 } - 3 = 0$ on [1, 2]. Use $p _ { 0 } = 1$

6. Use a fixed-point iteration method to determine a solution accurate to within $1 0 ^ { - 2 }$ for $x ^ { 3 } - x -$ $1 = 0$ on [1, 2]. Use $p _ { 0 } = 1$

7.Use Theorem 2.2 to show that $g ( x ) = \pi + 0 . 5 \sin ( x / 2 )$ has a unique fixed point on $[ 0 , 2 \pi ]$ Use fixed-point iteration to find an approximation to the fixed point that is accurate to within $1 0 ^ { - 2 }$ .Use Corollary 2.4 to estimate the number of iterations required to achieve $1 0 ^ { - 2 }$ accuracy, and compare this theoretical estimate to the number actually needed.

8. Use Theorem 2.2 to show that $g ( x ) = 2 ^ { - x }$ has a unique fixed point on $[ \frac { 1 } { 3 }$ ,1]. Use fixed-point iteration to find an approximation to the fixed point accurate to within $1 0 ^ { - 4 }$ . Use Corollary 2.4 to estimate the number of iterations required to achieve $1 0 ^ { - 4 }$ accuracy, and compare this theoretical estimate to the number actually needed.

9.Use a fixed-point iteration method to find an approximation to $\sqrt { 3 }$ that is accurate to within $1 0 ^ { - 4 }$ . Compare your result and the number of iterations required with the answer obtained in Exercise 10 of Section 2.1.

10. Use a fixed-point iteration method to find an approximation to $\sqrt [ 3 ] { 2 5 }$ that is accurate to within $1 0 ^ { - 4 }$ . Compare your result and the number of iterations required with the answer obtained in Exercise 11 of Section 2.1.

11.For each of the following equations, determine an interval $[ a , b ]$ on which fixed-point iteration will converge. Estimate the number of iterations necessary to obtain approximations accurate to within $1 0 ^ { - 5 }$ , and perform the calculations.

a. $\begin{array} { l } { x = \frac { 2 - e ^ { x } + x ^ { 2 } } { 3 } } \\ { x = ( e ^ { x } / 3 ) ^ { 1 / 2 } } \\ { x = 6 ^ { - x } } \end{array}$ $\begin{array} { r l } { \mathbf { b } . } & { { } x = \displaystyle \frac { 5 } { x ^ { 2 } } + 2 } \\ { \mathbf { d } . } & { { } x = 5 ^ { - x } } \\ { \mathbf { f } . } & { { } x = 0 . 5 ( \sin x + \cos x ) } \end{array}$   
c.   
e.

12. For each of the following equations, determine a function $\pmb { g }$ and an interval $[ a , b ]$ on which fixed-point iteration wil converge to a positive solution of the equation.

$$
3 x ^ { 2 } - e ^ { x } = 0 \qquad \mathbf { b } _ { \mathbf { \cdot } } \quad x - \cos x = 0
$$

Find the solutions to within $1 0 ^ { - 5 }$ ，

13.Find all the zeros of $f ( x ) = x ^ { 2 } + 1 0 \cos x$ by using the fixed-point iteration method for an appropriate iteration function $\pmb { g }$ . Find the zeros accurate to within $1 0 ^ { - 4 }$

14.Use a fixed-point iteration method to determine a solution accurate to within $1 0 ^ { - 4 }$ for $x \ =$ tan $x$ ,for $x$ in [4,5].

15.Use a fixed-point iteration method to determine a solution accurate to within $1 0 ^ { - 2 }$ for 2 sin $\pi x + x = 0$ on [1,2]. Use $p _ { 0 } = 1$

16.Let $\pmb { A }$ be a given positive constant and $g ( x ) = 2 x \sim A x ^ { 2 }$

a. Show that if fixed-point iteration converges to a nonzero limit, then the limit is $p = 1 / A$ ， so the inverse of a number can be found using only multiplications and subtractions.   
b. Find an interval about $1 / A$ for which fixed-point iteration converges, provided $p _ { 0 }$ is in that interval.

17.Find a function $\pmb { \ 8 }$ defined on [O,1] that satisfies none of the hypotheses of Theorem 2.2 but still has a unique fixed point on [0,1].

18.a.Show that Theorem 2.2 is true if the inequality $| g ^ { \prime } ( x ) | \leq k$ is replaced by $g ^ { \prime } ( x ) \leq k$ ,for all $x \in ( a , b )$ . [Hint: Only uniqueness is in question.] b. Show that Theorem 2.3 may not hold if inequality $| g ^ { \prime } ( x ) | \leq k$ is replaced by $g ^ { \prime } ( x ) \leq k$ [Hint: Show that $g ( x ) = 1 - x ^ { 2 }$ ,for $\pmb { \chi }$ in [0,1], provides a counterexample.]

19.a.Use Theorerm 2.3 to show that the sequence defined by

$$
x _ { n } = { \frac { 1 } { 2 } } x _ { n - 1 } + { \frac { 1 } { x _ { n - 1 } } } , \quad { \mathrm { f o r ~ } } n \geq 1 ,
$$

converges to $\sqrt { 2 }$ whenever $x _ { 0 } > { \sqrt { 2 } }$

b. Use the fact that $0 < ( x _ { 0 } - { \sqrt { 2 } } ) ^ { 2 }$ whenever $x _ { 0 } \neq { \sqrt { 2 } }$ to show that if $0 < x _ { 0 } < \sqrt { 2 }$ ，then $x _ { 1 } > { \sqrt { 2 } }$

c. Use the results of parts (a) and (b) to show that the sequence in (a) converges to $\sqrt { 2 }$ whenever $x _ { 0 } > 0$

20.a.Show that if $\pmb { A }$ is any positive number,then the sequence defined by

$$
x _ { n } = { \frac { 1 } { 2 } } x _ { n - 1 } + { \frac { A } { 2 x _ { n - 1 } } } , \quad { \mathrm { f o r ~ } } n \geq 1 ,
$$

converges to $\sqrt { A }$ whenever $x _ { 0 } > 0$

b. What happens if $x _ { 0 } < 0 ?$

21.Replace the assumption in Theorem 2.3 that $\mathbf { \ " } \mathbf { a }$ positive number $k < 1$ exists with $| g ^ { \prime } ( x ) | \leq k ^ { \prime \prime }$ with $^ { * } g$ satisfies a Lipschitz condition on the interval $[ a , b ]$ with Lipschitz constant $L \ < 1$ .” (See Exercise 25, Section 1.1.) Show that the conclusions of this theorem are still valid.

22. Suppose that $\pmb { g }$ is continuously differentiable on some interval $( c , d )$ that contains the fixed point $p$ of $\pmb { g }$ . Show that if $| g ^ { \prime } ( p ) | < 1$ , then there exists a $\delta > 0$ such that if $| p _ { 0 } - p | \leq \delta$ ,then the fixed-point iteration converges.

23. An object falling vertically through the air is subjected to viscous resistance as wellas to the force of gravity. Assume that an object with mass $\mathbf { \nabla } m$ is dropped from a height ${ \pmb S } _ { \mathbf { \widetilde { \mu } } }$ and that the height of the object after $t$ seconds is

$$
s ( t ) = s _ { 0 } - \frac { m g } { k } t + \frac { m ^ { 2 } g } { k ^ { 2 } } ( 1 - e ^ { - k t / m } ) ,
$$

where $g = 3 2 . 1 7 ~ \mathrm { f t } / \mathrm { s } ^ { 2 }$ and $k$ represents the coeficient of air resistance in lb-s/ft. Suppose $s _ { 0 } = 3 0 0$ ft, $m = 0 . 2 5$ Ib, and $k \simeq 0 . 1$ Ib-s/ft. Find, to within $0 . 0 1 \ \mathbf { s } ,$ the time it takes this quarter-pounder to hit the ground.

24.Let $g \in C ^ { 1 } [ a , b ]$ and $p$ be in $( a , b )$ with $g ( p ) = p$ and $| g ^ { \prime } ( p ) | > 1$ . Show that there exists a $\delta > 0$ such that if $0 < | p _ { 0 } - p | < \delta$ ,then $| p _ { 0 } - p | < | p _ { 1 } - p |$ . Thus, no matter how close the initial approximation $p _ { 0 }$ is to $p$ , the next iterate $p _ { 1 }$ is farther away,so the fixed-point iteration does not converge if $p _ { 0 } \neq p$

# 2.3 Newton's Method

Newton's (or the Newton-Raphson) method is one of the most powerful and well-known numerical methods for solving a root-finding problem. There are many ways of introducing Newton's method.If we only want an algorithm, we can consider the technique graphically, as is often done in calculus. Another possbility is to derive Newton's method as a technique to obtain faster convergence than offered by other types of functional iteration,as is done in Section 2.4.A third means of introducing Newton's method, which is discussed next, is based on Taylor polynomials.

Suppose that $f \in C ^ { 2 } [ a , b ]$ .Let $\mathbf { \partial } : \overline { { \boldsymbol { x } } } \in [ a , b ]$ be an approximation to $p$ such that $f ^ { \prime } ( \overline { { x } } ) \neq$ 0 and $| p - { \overline { { x } } } |$ is “small.” Consider the first Taylor polynomial for $f ( x )$ expanded about $\overline { { x } }$ ，

$$
f ( x ) = f ( \overline { { { x } } } ) + ( x - \overline { { { x } } } ) f ^ { \prime } ( \overline { { { x } } } ) + \frac { ( x - \overline { { { x } } } ) ^ { 2 } } { 2 } f ^ { \prime \prime } ( \xi ( x ) ) ,
$$

where $\xi ( x )$ lies between $\pmb { x }$ and $\widehat { x }$ . Since $f ( p ) = 0$ , this equation with ${ x } = p$ gives

$$
0 = f ( \overline { { { x } } } ) + ( p - \overline { { { x } } } ) f ^ { \prime } ( \overline { { { x } } } ) + \frac { ( p - \overline { { { x } } } ) ^ { 2 } } { 2 } f ^ { \prime \prime } ( \xi ( p ) ) .
$$

Newton's method is derived by assuming that since $| p - { \bar { x } } |$ is small, the term involving $( p - { \overline { { x } } } ) ^ { 2 }$ is much smaller, so

$$
0 \approx f ( { \overline { { x } } } ) + ( p - { \overline { { x } } } ) f ^ { \prime } ( { \overline { { x } } } ) .
$$

Solving for $p$ gives

$$
p \approx \overline { { x } } - \frac { f ( \overline { { x } } ) } { f ^ { \prime } ( \overline { { x } } ) } .
$$

This sets the stage for Newton's method, which starts with an initial approximation $p _ { 0 }$ and generates the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ ,by

$$
p _ { n } = p _ { n - 1 } - { \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } } , \quad { \mathrm { f o r } } n \geq 1 .
$$

Figure 2.7 illustrates how the approximations are obtained using successive tangents. (Also see Exercise 11.) Starting with the initial approximation $p _ { 0 }$ , the approximation $p _ { \mathrm { 1 } }$ is the $x$ -intercept of the tangent line to the graph of $f$ at $( p _ { 0 } , f ( p _ { 0 } ) )$ . The approximation $p _ { 2 }$ is the $\pmb { x }$ -intercept of the tangent line to the graph of $f$ at $( p _ { 1 } , f ( p _ { 1 } ) )$ and so on. Algorithm 2.3 follows this procedure.

![](images/61556f3fccd3a85fcdfc2931ec3c8120b6d2f79ec284b7c49cdcf8ff4d2cb1f0.jpg)  
Figure 2.7

# Newton's

To find a solution to $f ( x ) = 0$ given an initial approximation $p _ { 0 }$ ：

INPUTinitial approximation $p _ { 0 }$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$ OUTPUTapproximate solution $p$ or message of failure.

Step 1 Set $i = 1$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-6.

Step 3 Set $p = p _ { 0 } - f ( p _ { 0 } ) / f ^ { \prime } ( p _ { 0 } ) . \quad ( C o m p u t e p _ { i } . )$

Step 4 If $| p - p _ { 0 } | < T O L$ then OUTPUT $( p )$ ；  (The procedure was successful.) STOP.

Step 5Set $i = i + 1$

Step 6 Set $p _ { 0 } = p$ (Update po.)

Step 7OUTPUT(The method failed after $N _ { 0 }$ iterations, $N _ { 0 } = , N _ { 0 }$ ； (The procedure was unsuccessful.) STOP.

The stopping-technique inequalities given with the Bisection method are applicable to Newton's method. That is, select a tolerance $\varepsilon > 0$ , and construct $p _ { 1 } , \dotsc p _ { N }$ until

$$
| p _ { N } - p _ { N - 1 } | < \varepsilon ,
$$

$$
\frac { | p _ { N } - p _ { N - 1 } | } { | p _ { N } | } < \varepsilon , \quad p _ { N } \neq 0 ,
$$

$$
| f ( p _ { N } ) | < \varepsilon .
$$

A form of Inequality (2.6) is used in Step 4 of Algorithm 2.3. Note that inequality (2.8) may not give much information about the actual error $| p _ { N } - p |$ . (See Exercise 14 in Section 2.1.)

Newton's method is a functional iteration technique of the form $p _ { n } = g ( p _ { n - 1 } )$ ,for which

$$
g ( p _ { n - 1 } ) = p _ { n - 1 } - { \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } } , \quad { \mathrm { f o r ~ } } n \geq 1 .
$$

Infact,this isthefunctioaliterationtechniquethat was usedtogivetherapidconvergence we saw in part (e) of Example 3 in Section 2.2.

It is clear from equation (2.9) that Newton's method cannot be continued if $f ^ { \prime } ( p _ { n - 1 } ) =$ 0 for some $\pmb { n }$ .In fact, we willsethatthe mehodismosteffective when $f ^ { \prime }$ is bounded away from zero near $p$ ·

Suppose we would like to approximate a fixed point of $g ( x ) = \cos x$ . The graph in Figure 2.8 implies that a single fixed-point $p$ lies in $[ 0 , \pi / 2 ]$

![](images/b521007a5a6a96421e59e5c307b4a76beb94e426d190fc87591807aa901d5771.jpg)  
Figure 2.8

Table 2.3 shows the results of fixed-point iteration with $p _ { 0 } = \pi / 4$ . The best we could conclude from these results is that $p \approx 0 . 7 4$

To approach this problem differently, define $f ( x ) = \cos x - x$ and apply Newton's method. Since $f ^ { \prime } ( x ) = - \sin x - 1$ , the sequence is generated by

$$
p _ { n } = p _ { n - 1 } - { \frac { \cos p _ { n - 1 } - p _ { n - 1 } } { - \sin p _ { n - 1 } - 1 } } , \quad { \mathrm { f o r } } n \geq 1 .
$$

With $p _ { 0 } = \pi / 4$ , the approximations in Table 2.4 are generated. An excellent approximation is obtained with $n = 3$ . We would expect this result to be accurate to the places listed because of the agreement of $p _ { 3 }$ and $p _ { 4 }$ ： ■

Table 2.3   

<table><tr><td>n</td><td>Pn</td></tr><tr><td>0</td><td>0.7853981635</td></tr><tr><td>1</td><td>0.7071067810</td></tr><tr><td>2</td><td>0.7602445972</td></tr><tr><td>3</td><td>0.7246674808</td></tr><tr><td>4</td><td>0.7487198858</td></tr><tr><td>5</td><td>0.7325608446</td></tr><tr><td>6</td><td>0.7434642113</td></tr><tr><td>7</td><td>0.7361282565</td></tr></table>

Table 2.4   

<table><tr><td>n</td></tr><tr><td>0 0.7853981635</td></tr><tr><td>1 0.7395361337</td></tr><tr><td>0.7390851781</td></tr><tr><td>0.7390851332</td></tr><tr><td>0.7390851332</td></tr><tr><td></td></tr></table>

The Taylor series derivation of Newton's method at the beginning of the section points out the importance of an accurate initial approximation. The crucial assumption is that the term involving $( p - { \overline { { x } } } ) ^ { 2 }$ is,by comparison with $| p - { \overline { { x } } } |$ , so small that it can be deleted. This will clearly be false unless $\overline { { x } }$ is a good approximation to $p$ .If $p _ { 0 }$ is not sufficiently close to the actual root, there is litle reason to suspect that Newton's method will converge to the root. However, in some instances, even poor initial approximations will produce convergence. (Exercises 12 and 16 illustrate some of these possibilities.)

The following convergence theorem for Newton's method illustrates the theoretical importance of the choice of $p _ { 0 }$

# Theorem 2.5

Let $f \in C ^ { 2 } [ a , b ]$ .If $p \in \{ a , b \}$ is such that $f ( p ) = 0$ and $f ^ { \prime } ( p ) \neq 0$ , then there exists a $\delta > 0$ such that Newton's method generates a sequence $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ converging to $p$ for any initial approximation $p _ { 0 } \in [ p - \delta , p + \delta ]$

Proof The proof is based on analyzing Newton's method as the functional iteration scheme $p _ { n } = g ( p _ { n - 1 } )$ ,for $n \geq 1$ ,with

$$
g ( x ) = x - { \frac { f ( x ) } { f ^ { \prime } ( x ) } } .
$$

Let $k$ be in (O,1). We first find an interval $[ p - \delta , p + \delta ]$ that $g$ maps into itself and for which $| g ^ { \prime } ( x ) | \leq k$ ,for all $x \in ( p - \delta , p + \delta )$

Since $f ^ { \prime }$ is continuous and $f ^ { \prime } ( p ) \neq 0$ ,part (a) of Exercise 27 in Section 1.1 implies that there exists a $\delta _ { 1 } > 0$ ,such that $f ^ { \prime } ( x ) \neq 0$ for $x \in [ p - \delta _ { 1 } , p + \delta _ { 1 } ] \subseteq [ a , b ]$ . Thus, $\pmb { g }$ is defined and continuous on $[ p - \delta _ { 1 } , p + \delta _ { 1 } ]$ . Also,

$$
g ^ { \prime } ( x ) = 1 - { \frac { f ^ { \prime } ( x ) f ^ { \prime } ( x ) - f ( x ) f ^ { \prime \prime } ( x ) } { [ f ^ { \prime } ( x ) ] ^ { 2 } } } = { \frac { f ( x ) f ^ { \prime \prime } ( x ) } { [ f ^ { \prime } ( x ) ] ^ { 2 } } } ,
$$

for $x \in [ p - \delta _ { 1 } , p + \delta _ { 1 } ]$ ,and, since $f \in C ^ { 2 } [ a , b ]$ , we have $g \in C ^ { 1 } [ p - \delta _ { 1 } , p + \delta _ { 1 } ]$

By assumption, $f ( p ) = 0$ ,so

$$
g ^ { \prime } ( p ) = { \frac { f ( p ) f ^ { \prime \prime } ( p ) } { [ f ^ { \prime } ( p ) ] ^ { 2 } } } = 0 .
$$

Since $g ^ { \prime }$ is continuous and $0 < k < 1$ , part (b)of Exercise 27 in Section 1.1 implies that there exists a $\pmb { \delta }$ ，with $0 < \delta < \delta _ { 1 }$ ,and

$$
| g ^ { \prime } ( x ) | \leq k , \quad { \mathrm { ~ f o r ~ a l l ~ } } x \in [ p - \delta , p + \delta ] .
$$

It remains to show that $\pmb { g }$ maps $[ p - \delta , p + \delta ]$ into $[ p - \delta , p + \delta ]$ .If $x \in [ p - \delta , p + \delta ]$ ,the Mean Value Theorem implies that for some number $\pmb { \xi }$ between $\pmb { x }$ and $p , | g ( x ) - g ( p ) | =$ $| g ^ { \prime } ( \xi ) | | x - p |$ . S0

$$
| g ( x ) - p | = | g ( x ) - g ( p ) | = | g ^ { \prime } ( \xi ) | | x - p | \leq k | x - p | < | x - p | .
$$

Since $x \in [ p - \delta , p + \delta ]$ , it follows that $| x - p | < \delta$ and that $| g ( x ) - p | < \delta$ . Hence, $\pmb { g }$ maps $[ p - \delta , p + \delta ]$ into $[ p - \delta , p + \delta ]$

All the hypotheses of the Fixed-Point Theorem are now satisfied, so the sequence $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ , defined by

$$
p _ { n } = g ( p _ { n - 1 } ) = p _ { n - 1 } - \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } , \quad \mathrm { f o r } n \geq 1 ,
$$

converges to $p$ for any $p _ { 0 } \in [ p - \delta , p + \delta ]$

Theorem 2.5 states that, under reasonable assumptions, Newton's method converges provided a sufficiently accurate initial approximation is chosen. It also implies that the constant $k$ that bounds the derivative of $g$ , and,consequently, indicates the speed of convergence of the method, decreases to O as the procedure continues. This result is important for the theory of Newton's method, but it is seldom applied in practice since it does not tell us how to determine δ. In a practical application, an initial approximation is selected, and successive approximations are generated by Newton's method. These will generally either converge quickly to the root, or it will be clear that convergence is unlikely.

Newton's method is an extremely powerful technique, but it has a major weakness: the need to know the value of the derivative of $f$ at each approximation. Frequently, $f ^ { \prime } ( x )$ is far more diffcult and needs more arithmetic operations to calculate than $f ( x )$

To circumvent the problem of the derivative evaluation in Newton's method, we introduce a slight variation.By definition,

$$
f ^ { \prime } ( p _ { n - 1 } ) = \operatorname* { l i m } _ { x \to p _ { n - 1 } } { \frac { f ( x ) - f ( p _ { n - 1 } ) } { x - p _ { n - 1 } } } .
$$

Letting $x = p _ { n - 2 }$ , we have

$$
f ^ { \prime } ( p _ { n - 1 } ) \approx { \frac { f ( p _ { n - 2 } ) - f ( p _ { n - 1 } ) } { p _ { n - 2 } - p _ { n - 1 } } } = { \frac { f ( p _ { n - 1 } ) - f ( p _ { n - 2 } ) } { p _ { n - 1 } - p _ { n - 2 } } } .
$$

Using this approximation for $f ^ { \prime } ( p _ { n - 1 } )$ in Newton's formula gives

$$
p _ { n } = p _ { n - 1 } - \frac { f ( p _ { n - 1 } ) ( p _ { n - 1 } - p _ { n - 2 } ) } { f ( p _ { n - 1 } ) - f ( p _ { n - 2 } ) } .
$$

This technique is called the Secant method and is presented in Algorithm 2.4. (See Figure 2.9.） Starting with the two initial approximations $p _ { 0 }$ and $p _ { 1 }$ , the approximation $p _ { 2 }$ is the $\pmb { x }$ -intercept of the line joining $( p _ { 0 } , f ( p _ { 0 } ) )$ and $( p _ { 1 } , f ( p _ { 1 } ) )$ . The approximation $p _ { 3 }$ is the $\pmb { x }$ -intercept of the line joining $( p _ { 1 } , f ( p _ { 1 } ) )$ and $( p _ { 2 } , f ( p _ { 2 } ) )$ , and so on.

![](images/d4347db3d38f9e32afff85a04489cca32dbfe3853d2c63dbe56d7d2da1a380fc.jpg)  
Figure 2.9

# Secant

To find a solution to $f ( x ) = 0$ given initial approximations $p _ { 0 }$ and $p _ { 1 }$ ：

INPUTinitial approximations $p _ { 0 } , p _ { 1 }$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$ OUTPUTapproximate solution $p$ or message of failure.

Step 1 Set $i = 2$ ；$\begin{array} { r } { q _ { 0 } = f ( p _ { 0 } ) ; } \\ { q _ { 1 } = f ( p _ { 1 } ) . } \end{array}$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-6.

$$
p = p _ { 1 } - q _ { 1 } ( p _ { 1 } - p _ { 0 } ) / ( q _ { 1 } - q _ { 0 } ) . \quad ( C o m p u t e ~ p _ { i } . )
$$

Step 4If $| p - p _ { 1 } | < T O L$ then OUTPUT $( p )$ ；(The procedure was successful.) STOP.

Step 5Set $i = i + 1$

Step $\sigma$ Set $\begin{array} { r c l } { { } } & { { : p _ { 0 } = p _ { 1 } ; } } & { { ( U p d a t e ~ p _ { 0 } , q _ { 0 } , p _ { 1 } , q _ { 1 } . ) } } \\ { { } } & { { } } & { { q _ { 0 } = q _ { 1 } ; } } \\ { { } } & { { } } & { { p _ { 1 } = p ; } } \\ { { } } & { { } } & { { q _ { 1 } = f ( p ) . } } \end{array}$

Step 7OUTPUT('The method failed after $N _ { 0 }$ iterations, $N _ { 0 } = , N _ { 0 } ,$ ； (The procedure was unsuccessful.) STOP.

The next example involves a problem considered in Example 1, where we used Newton's method with $p _ { 0 } = \pi / 4$