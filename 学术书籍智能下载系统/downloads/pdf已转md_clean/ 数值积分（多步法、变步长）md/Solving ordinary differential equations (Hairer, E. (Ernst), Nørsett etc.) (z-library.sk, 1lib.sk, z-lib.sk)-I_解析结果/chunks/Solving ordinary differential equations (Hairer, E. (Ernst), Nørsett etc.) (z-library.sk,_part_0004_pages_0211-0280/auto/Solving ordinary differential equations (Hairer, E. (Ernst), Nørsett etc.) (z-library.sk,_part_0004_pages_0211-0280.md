$$
\sum _ { \substack { \iota = 1 1 , 1 2 , 1 3 , 1 4 , 1 7 } } b _ { i } c _ { i } ^ { k } w _ { i } = \frac { 1 } { ( 7 + k ) 6 } - \sum _ { \substack { i = 6 , 7 , 9 , 1 0 } } b _ { i } c _ { i } ^ { k } \sum _ { j - 1 } ^ { i - 1 } a _ { i j } c _ { j } ^ { 5 }
$$

for $w _ { i }$ . Then use (6.16) together with (6.14) for $i = 1 1 , 1 2 , 1 3 , 1 4 , 1 7$ to compute $\boldsymbol { a } _ { i j }$ with $i = 1 1 , 1 2 , 1 3 , 1 4 , 1 7$ and $j = 6 , \ldots , 1 0$ .Finally use the first equation of (6.14) for $a _ { i 1 }$

For a deeper understanding of the verification of the order conditions we refer to the original paper of Hairer (1978).

Still higher order formulas make less and less sense, if they are not needed for computations of very high precision. The difficulties in obtaining them (very challenging as a mathematical problem） grow more than exponentially and the methods become huge monsters which also make the step size control more and more difficult.

# Embedded formulas of high order

It was mainly the formula manipulation genius Fehlberg who first derived high order embedded formulas. His greatest success was his 7th order formula with 8th order error estimate which is of frequent use in all high precision computations,e.g. in astronomy. It is with pleasure that we reproduce in Table 6.3 the original page of the NASA report (Fehlberg (1968)), also because its later publication in "Computing" contains a printing error.

Fehlberg's methods suffer from two drawbacks:

i) as already mentioned above, they are conceived for continuation with the $p$ -th order form ula with minim ised error coefficients and thus tend to underestimate the error;   
ii) they give identically zero error estimates for quadrature problems $y ^ { \prime } { = } f \left( x \right)$ ·

The first high order embedded formulas which avoid the second drawback were constructed by Verner (1978). His method of order 8(9) is included in the numerical test below.

Excelient numerical results are produced by the 8(7)-method of Prince and Dormand (1981),who have made great efforts to minimize the error coefficients for the 8th order approximation. The coefficients of their formula are reproduced in Table 6.4 (with permission).

A Fortran subroutine (DOPRI8) for this method, with minimized storage requirement (see Exercise 5), is included in the Appendix to this book.

Table 6.3. Fehlberg, order 7(8)   

<table><tr><td>&lt; C</td><td>#</td><td>二</td><td></td><td>雕融喘啡</td><td></td><td></td><td></td><td></td><td>一0</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td>0</td><td></td></tr><tr><td rowspan="5">区</td><td>J</td><td></td><td></td><td></td><td></td><td></td><td>116</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>1-124543117</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>G</td><td></td><td></td><td></td><td>： 56 52352</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 4</td><td></td><td>15</td><td>49 </td><td>9</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td>1-5 6276</td><td>1 30 2 45</td><td>3 1 15</td><td>3 </td><td></td><td>0</td><td></td><td>81 </td><td></td></tr><tr><td></td><td></td><td>== 。</td><td>}些）。。。</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td></td><td></td><td>0 0</td></tr><tr><td>C</td><td></td><td></td><td> ②5丨9丨σ②丨＝　6１6=31З１</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td></td><td></td></tr><tr><td></td><td></td><td>U ~］</td><td>3</td><td>;</td><td>[- 厂</td><td></td><td>9</td><td>10Ⅱ</td><td></td><td></td><td>12</td><td></td></tr></table>

Truncation Error Term: TE 100 +he-n -h )h

<table><tr><td colspan="3">G G b 0 0 G i 0 0</td><td rowspan="9">0 0 。</td><td rowspan="9">。 三 64 64 0</td><td rowspan="9">D GR</td><td rowspan="9"></td><td rowspan="9">D S</td><td rowspan="9">555555551 GO 586566555 D </td><td rowspan="9">585168195 SA GR</td><td rowspan="9"></td><td rowspan="9">G</td><td colspan="2"></td><td>GA S D</td><td rowspan="2">GR G DR</td><td colspan="2">5553131115</td><td>45 0 D 寸</td></tr><tr><td></td><td></td><td>555333555 178153555</td><td>GR D</td><td rowspan="2"></td><td rowspan="4">GA G 8859999996</td><td>0 GE 1115555550</td><td>GR</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan="3">D</td><td rowspan="3">83133531</td><td>G GA</td><td></td><td>GR</td></tr><tr><td></td><td></td><td></td><td>G D </td><td>155593555 DR G</td><td>659669966 G</td></tr><tr><td></td><td></td><td>G G G</td><td>GR G CA</td><td rowspan="2">G D 166771551155</td><td rowspan="2">G S DR DR</td><td>D </td><td>D</td></tr><tr><td rowspan="5">1_18 i 0</td><td rowspan="5">23255355 18336938 西</td><td>D</td><td>D</td><td>DR DA</td><td rowspan="2">GR </td><td rowspan="4">TR</td><td>G 338335511 SA 659996446</td></tr><tr><td>G D</td><td>SR GA 2337355551</td><td rowspan="2">GA D 177555595555 GR</td><td rowspan="2">D 1555111155 115555111</td><td rowspan="2">1055555555 G 553555555</td><td rowspan="2"></td></tr><tr><td>3-20 D 3-16 0 0</td></tr><tr><td rowspan="2">G 。 。</td><td rowspan="2">G GR 。 0</td><td rowspan="2">0 G</td><td rowspan="3">武 0 0</td><td rowspan="3">S 3335655555 GR 0 0 0 GA </td></tr><tr><td rowspan="3"></td></tr><tr><td>0</td><td>0 A GR</td><td>GR GR GR</td><td>0 SR</td><td rowspan="2">6818998701 181441111 20</td><td rowspan="2">450085954 G</td><td rowspan="2">0 TR 1</td></tr><tr><td>18 13 118 12 1-8</td><td>516 516</td><td>3-80 38 5 0</td><td>DR 31 20</td></tr></table>

# A Numerical Example

All above mentioned methods have been coded with a slightly more complicated step size control and run on example (4.16) with tolerances ranging from $1 0 ^ { - 6 }$ to $1 0 ^ { - 1 7 }$ on the Univac 1100/60 computer (machine precision $= 1 . 7 3 \times 1 0 ^ { - 1 8 } )$ . Butcher's 6-th order method, which was the highest order method in Figure 4.3, is now the first method compared to methods of still higher order. It can again be observed in Figure 6.1 that Fehlberg's formula underestimates the error. The method of Prince-Dormand is clearly superior for tolerances up to $1 0 ^ { - 1 3 }$ , later it is surpassed by the 10th order formula.

![](images/0986c384de7bbc6baf1928ecbc20161ebf9f2e70ae11a0b263983475869435bb.jpg)  
Figure 6.1. Function evaluations versus global error for tolerances from $1 0 ^ { - 6 }$ to 10-17

The coeficients of DOPRI8 are not exact rational parameters, but continued fraction approximations accurate to 18 significant figures. The code DOPRI8 must therefore not be used at tolerance requirements below $1 0 ^ { - 1 6 }$ ,say. Figure 6.2 shows the results computed on a high precision CDC machine for ${ y } _ { 1 } ^ { \prime } { = } { y } _ { 2 } / 6$ ， $y _ { 2 } ^ { \prime } { = } { - } y _ { 1 } y _ { 2 } ^ { 2 } / 5 4$ ， $y _ { 1 } ( 4 ) { = } 2$ $y _ { 2 } ( 4 ) { = } 1 . 5$ ， with exact solution $y _ { 1 } ( 9 ) = 3$ ， $y _ { 2 } ( 9 ) = 1$

# Exercises

1. Find conditions on the free coefficients such that the method described in Theorem 6.2 can be equipped with an embedded 4th order expression for error estimates. How can the coeficients be

![](images/195b35a1dfb55abfb7bfbb4a4f6b9caea440d44c09b83a5916be4f698a004750.jpg)  
Figure 6.2. Results for Prince-Dormand (7)8 at high tolerances

chosen such that $b _ { i } \geq 0$ ; such that the 6-th order error coefficients are minimal?

2. Construct a 6-stage 5-th order formula with $c _ { 3 } = 1 / 3 , c _ { 4 } = 1 / 2 ,$ $c _ { \varsigma } { = } 2 / 3$

3. (Butcher). Show that for any RK method of order 5,

$$
\sum _ { i } b _ { i } \big ( \sum _ { j } a _ { i j } c _ { j } - \frac { c _ { i } ^ { 2 } } { 2 } \big ) ^ { 2 } = 0 \ .
$$

(Hint. Multiply out and use order conditions).

Consequently, there exists no ERK of order 5 with all $b _ { i } > 0$

4. Write a code with a high order RK method (or take one) and solve numerically the Arenstorf orbit of the restricted three body problem (0.1) (see the introduction) with initial values

$$
y _ { 1 } ( 0 ) = 0 . 9 9 4 , y _ { 2 } ( 0 ) = y _ { 3 } ( 0 ) = 0 ,
$$

$$
y _ { 4 } ( 0 ) = - 2 . 0 3 1 7 3 2 6 2 9 5 5 7 3 3 6 8 3 5 7 3 0 2 0 5 7 9 2 4 ,
$$

$$
\scriptstyle \mu = 0 . 0 1 2 2 7 7 4 7 1 , \quad \mu ^ { \prime } = 1 - \mu .
$$

Compute the solutions for

$$
x _ { e n d } = 1 1 . 1 2 4 3 4 0 3 3 7 2 6 6 0 8 5 1 3 4 9 9 9 7 3 4 0 4 7 .
$$

The initial values are chosen such that the solution is periodic to this precision. The plotted solution curve has one loop less than the one of the introduction.

5. (Shampine, 1979). Show that the method of Prince-Dormand (7)8 (Table 6.4) can be implemented in such a manner that the storage grows like 9n ， where n is the dimension of the system.

Hint. a) Take advantage of the zero-pattern of the coefficients; b) ("Method I"): after having computed (see (1.8)) $k _ { 1 } , k _ { 2 } , \ldots ,$ $k _ { \mathfrak { g } } ,$ compute the sums

$$
\sum _ { j = 1 } ^ { 9 } a _ { i j } k _ { j } \quad \mathrm { f o r } \quad i = 1 1 , 1 2 , 1 3 , \qquad \sum _ { j = 1 } ^ { 9 } b _ { j } k _ { j } , \qquad \sum _ { j = 1 } ^ { 9 } \hat { b } _ { j } k _ { j } ;
$$

then the memnories occupied by $k _ { 2 } , k _ { 3 } , \ldots$ etc are not needed any longer. See the code DOPRI8 in the Appendix .

# I1.7. Implicit Runge-Kutta methods

‘It has been traditional to consider only explicit   
processes"   
(J.C. Butcher, 1964)   
The high speed computing machines make it possible   
to enjoy the advantage of intricate methods"   
(P.C. Hammer and J.W. Hollingsworth, 1955)

# Introduction

The first implicit RK methods were used by Cauchy (1824) for the sake of - you have guessed correctly - error estimation (Methodes diverses qui peuvent etre employees au Calcul numerique ..; see Exercise 6).  Cauchy inserted thc mean valuc theorem into the integral studied in Sections I.8 and I1.1,

$$
y \left( x  { 1 } \right) = y \left( x  { 0 } \right) + \intop _ { x  { 0 } } ^ { x  { 1 } } f \left( x  { , } y \left( x \right) \right) d x \textrm { , }
$$

to obtain

$$
y _ { 1 } = y _ { 0 } + h f ( x _ { 0 } { + } \Theta h , y _ { 0 } { + } \Theta ( y _ { 1 } { - } y _ { 0 } ) )
$$

with $0 \leq \Theta , \Theta \leq 1$ (the "0-method"). The extreme cases are $\theta = \Theta = 0$ (the explicit Euler method) and $\Theta = \Theta = 1$

$$
y _ { 1 } = y _ { 0 } + h f \left( x _ { 1 } , y _ { 1 } \right) ,
$$

which we call the implicit or backward Euler method.

For the sake of more eficient numerical processes, we apply, as we did in Section II.1, the midpoint rule ( $\Theta = \Theta = 1 / 2$ ） and obtain from (7.2) by setting $k _ { 1 } { = } ( y _ { 1 } { - } y _ { 0 } ) / h$ ：

$$
\begin{array} { l } { { k _ { 1 } = f \left( x _ { 0 } { + } \frac { h } { 2 } , y _ { 0 } { + } \frac { h } { 2 } k _ { 1 } \right) , } } \\ { { y _ { 1 } = y _ { 0 } + h k _ { 1 } . } } \end{array}
$$

This method is called the implicit midpoint rule.

Still another possibility is to approximate (7.1) by the trapezoidal rule and to obtain

$$
y _ { 1 } = y _ { 0 } + { \frac { h } { 2 } } \biggl ( f \left( x _ { 0 } , y _ { 0 } \right) + f \left( x _ { 1 } , y _ { 1 } \right) \biggr ) \ .
$$

Let us also look at the Radau scheme

$$
\begin{array} { l } { \displaystyle { y \left( x _ { 1 } \right) - y \left( x _ { 0 } \right) = \int f \left( x , y \left( x \right) \right) d x } } \\ { \displaystyle { x _ { 0 } } } \\ { \displaystyle { \approx \frac { h } { 4 } \bigg ( f \left( x _ { 0 } , y _ { 0 } \right) + 3 f \left( x _ { 0 } + \frac 2 3 h , y \left( x _ { 0 } + \frac 2 3 h \right) \right) \bigg ) . } } \end{array}
$$

Here we need to approximate $y \left( x _ { 0 } + 2 h / 3 \right)$ . One idea would be the use of quadratic interpolation based on $y _ { 0 } , y _ { 0 } ^ { \prime }$ and $y \left( x _ { 1 } \right)$ ，

$$
y ( x _ { 0 } + { \frac { 2 } { 3 } } h ) \approx { \frac { 5 } { 9 } } y _ { 0 } + { \frac { 4 } { 9 } } y ( x _ { 1 } ) + { \frac { 2 } { 9 } } h f ( x _ { 0 } , y _ { 0 } ) .
$$

The resulting method, given by Hammer and Hollingsworth (1955), is

$$
\begin{array} { r c l } { { } } & { { } } & { { k _ { 1 } = f \left( x _ { 0 } , y _ { 0 } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { k _ { 2 } = f \left( x _ { 0 } { + } \displaystyle \frac { 2 } { 3 } h , y _ { 0 } { + } \displaystyle \frac { h } { 3 } ( k _ { 1 } { + } k _ { 2 } ) \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { y _ { 1 } = y _ { 0 } + \displaystyle \frac { h } { 4 } ( k _ { 1 } { + } 3 k _ { 2 } ) ~ . } } \end{array}
$$

These two schemes are both of the form (1.8) if the summations are extended up to $\because$ ”

Definition 7.1. Let $b _ { i }$ ， $a _ { i j }$ $( i , j = 1 , \dots , s ,$ ） be real numbers. Themethod

$$
\begin{array} { l l } { { k _ { i } = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \right) \quad } } & { { i = 1 , \dots , s } } \\ { { \quad } } & { { \displaystyle y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } } } \end{array}
$$

is called an s-stage RK method. When $a _ { i j } = 0$ for $i \geq j$ we have an explicit (ERK) method. If $a _ { i j } = 0$ for $i > j$ and at least one $a _ { i i } \neq 0$ ,we have a diagonal implicut $R K$ -method (DIRK-method). If in addition all diagonal elements are identical $a _ { i i } = \gamma \quad i = 1 \ , \ \dots , s$ , we speak of a singly diagonal implicit (SDIRK-) method. In al other cases we speak of an implicit RK method (IRK-method).

The tableau of coeficients used above for ERK-methods is obviously extended to include all the other non-zero $a _ { i j }$ 's above the diagonal. For Methods (7.4) and (7.6) it is given in Table 7.1.

Renewed interest in implicit RK-methods arose in connection with stif differential equations (see Volume I).

"Im plicit midpoint rule” "Hammer-Hollingsworth"

Table 7.1. Implicit Runge-Kutta methods   

<table><tr><td>1 2</td><td>2</td></tr><tr><td></td><td></td></tr></table>

<table><tr><td>0 2</td><td>0 1</td><td>0 1</td></tr><tr><td></td><td>3</td><td>3</td></tr><tr><td></td><td>1</td><td>3</td></tr><tr><td></td><td>4</td><td>4</td></tr></table>

# Existence of a numerical solution

For implicit methods, the $k _ { i }$ 's can no longer be evaluated successively, since (7.7) constitutes a system of implicit equations for the determination of $\boldsymbol { k } _ { i }$ . For DIRK-methods we have a sequence of implicit equations of dimension $n$ for $k _ { \mathrm { ~ 1 ~ } }$ , then for $k _ { 2 }$ ， etc. For fuily implicit methods sn unknowns $( k _ { i } , i = 1 , \dots , s$ each of dimension $n$ ） have to be determined simultaneously, which still increases the difculty. A natural question is therefore (the reason for which the original version of Butcher (1964a) was returned by the editors): do Equations (7.7) possess a solution at all ?

Theorem 7.2. Let $f$ be continuous and Lipschitz with constant $L$ in a neighbourhood of the initial value. If

$$
h < \frac { 1 } { L \operatorname* { m a x } _ { i } \sum _ { j } | a _ { i j } | }
$$

there exists an unique solution of (7.7), which can be obtained by iteration. 1f $f \left( x , y \right)$ is $P$ times continuousty differentiable, the functions $k _ { i }$ (as functions of $^ h$ ) are also in $C ^ { p }$

Proof: We prove the existence by iteration ("... on la resoudra facilement par des approximations successives..." (Cauchy 1824))

$$
k _ { i } ^ { \binom { n + 1 } { i } } = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } ^ { \binom { n } { j } } \right) .
$$

We define $K \in \mathbb { R } ^ { s n }$ as $\boldsymbol { K } \ = \ ( k _ { 1 } , \ldots , k _ { s } ) ^ { T }$ and use the norm $\parallel K \parallel = \operatorname* { m a x } ( \parallel k _ { i } \parallel ) .$ . Then (7.7) can be written as $K = F \left( K \right)$ where

$$
F _ { i } ( K ) = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \right) , \qquad i = 1 , \ldots , s .
$$

The Lipschitz condition and a repeated use of the triangle inequality then show that

$$
\| \ F ( \pmb { K } _ { 1 } ) - F ( \pmb { K } _ { 2 } ) \| \ \leq h L \operatorname* { m a x } _ { i } \sum _ { j } \ | a _ { i j } | \cdot \| \ K _ { 1 } - K _ { 2 } | \|
$$

which from (7.8) is a contraction. The contraction mapping principle then ensures the existence and uniqueness of the solution and the convergence of the fixed-point iteration.

The differentiability result is ensured by the Implicit Function Theorem of classical analysis: (7.7) is written as

$$
\Phi ( h , K ) = K - F ( K ) = 0 .
$$

The matrix of partial derivatives dΦ/ak for $h = 0$ is the identity matrix and therefore the solution of $\Phi ( h \ , K \ ) = 0$ ，which for $h = 0$ is $\boldsymbol { k } _ { i } = f \left( \boldsymbol { x } _ { 0 } , \boldsymbol { y } _ { 0 } \right)$ , is continuously differentiable in a neighbourhood of $h = 0$ QED.

The step size restriction (7.8) becomes useless for stiff differential equations ( $L$ large). We return to this question in Volume I1.

The definition of order is the same as for explicit methods and the order conditions are derived in precisely the same way as in Section I1.2.

Example 7.3. Let us study implicit two-stage methods of order 3: the order conditions become (see Theorem 2.1)

$$
\begin{array} { c } { { b _ { 1 } + b _ { 2 } = 1 } } \\ { { { } } } \\ { { b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } = \displaystyle \frac 1 2 } } \\ { { { } } } \\ { { b _ { 1 } c _ { 1 } ^ { 2 } + b _ { 2 } c _ { 2 } ^ { 2 } = \displaystyle \frac 1 3 } } \\ { { { } } } \\ { { { } _ { 1 } c _ { 1 } + a _ { 1 2 } c _ { 2 } ) + b _ { 2 } ( a _ { 2 1 } c _ { 1 } + a _ { 2 2 } c _ { 2 } ) = \displaystyle \frac 1 6 ~ , } } \end{array}
$$

The first three equations imply the following orthogonality relation (from the theory of Gaussian integration):

$$
\int _ { 0 } ^ { 1 } \ ( x - c _ { 1 } ) ( x - c _ { 2 } ) d x \ = 0 \ , \qquad \mathrm { i . e . } c _ { 2 } = \frac { 2 - 3 c _ { 1 } } { 3 - 6 c _ { 1 } }
$$

and

$$
b _ { 1 } = \frac { c _ { 2 } ^ { ~ - 1 / 2 } } { c _ { 2 } ^ { ~ - c _ { 1 } } } ~ , b _ { 2 } ^ { ~ } = \frac { c _ { 1 } ^ { ~ - 1 / 2 } } { c _ { 1 } ^ { ~ - c _ { 2 } } } ~ , ( c _ { 1 } ^ { ~ \mp ~ 1 / 2 , ~ c _ { 1 } ^ { ~ \mp ~ c _ { 2 } } } ) ~ .
$$

In the fourth equation we insert $a _ { 2 1 } = c _ { 2 } - a _ { 2 2 } , \ a _ { 1 1 } = c _ { 1 } - a _ { 1 2 }$ and con. sider $a _ { 1 2 }$ and $c _ { 1 }$ as free parameters. This gives

$$
a _ { 2 2 } = \frac { 1 / 6 - b _ { 1 } ( a _ { 1 2 } ( c _ { 2 } { - } c _ { 1 } ) + c _ { 1 } ^ { 2 } ) } { b _ { 2 } ( c _ { 2 } { - } c _ { 1 } ) } \ ,
$$

Table 7.2. SDIRK method, order 3   

<table><tr><td>Y</td><td>丫</td><td>0</td><td>y= 3±V3</td></tr><tr><td>1-Y</td><td>1-2γ</td><td>Y</td><td>6</td></tr><tr><td></td><td>1</td><td>1</td><td></td></tr><tr><td></td><td>2</td><td>2</td><td></td></tr></table>

If we let $a _ { \scriptscriptstyle 1 2 } = 0$ , we obtain a one-parameter family of DIRK-methods of order 3.A SDIRK method is obtained if we still require d11=a22 (Nbrset (1974), see Table 7.2).

For order 4 there are still 4 conditions to be satisfied, with only two free parameters left. Nevertheless there exists a unique solution. It is given in Table 7.3.

Table 7.3. Hammer-Hollingsworth, order 4   

<table><tr><td>1 √ 2 6 V</td><td>4 1 √ +</td><td>1 V 4 6 1</td></tr><tr><td>1 + 2 6</td><td>4 6</td><td>4</td></tr><tr><td></td><td>1 2</td><td>1 2</td></tr></table>

# The methods of Kuntzmann and Butcher of order 2s

It is clear that Formula (7.4) and the method of Table 7.3 extend the one and two-point Gaussian quadrature formulas respectively. Kuntzmann (1961) (see Ceschino-Kuntzmann (1963)， p.106) and Butcher (1964a) then discovered that for all s there exist IRKmethods of order $2 s$ . The main tools of proof are the following sim-plifying assumptions

$$
C \left( \eta \right) : \quad \ \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { q - 1 } = \frac { c _ { i } ^ { q } } { q } \qquad i = 1 , \dots , s , q = 1 , \dots , \eta
$$

These assumptions are similar to (6.7) and allow the reduction of order conditions of trees as sketched in Figure 7.1; and

$$
D \left( \xi \right) : \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } a _ { i j } = \frac { b _ { j } } { q } ( 1 - c _ { j } ^ { q } ) j = 1 , \ldots , s , q = 1 , \ldots , \xi 
$$

(compare with (6.6) and Lem ma 1.3) which finally reduce all trees as sketched in Figure 7.2 (Try an example).

![](images/f17af97e94193869170bda1d430153fee87b6037e980901c8b22a505cdd33b48.jpg)  
Figure 7.1. Reduction with C (q)

![](images/e9ad3735ba7c39e8fd576ea1c581e56c1c3f6bff9631a5fe12812a16409e3b56.jpg)  
Figure 7.2. Reduction with D (q )

The result is that when $\eta$ and $\xi$ are sufficiently large， all trees reduce to quadrature-order

$$
B \left( p \right) : \qquad \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } = \frac { 1 } { q } \qquad q = 1 , \ldots , p ,
$$

and we have:

Theorem 7.4 (Butcher). If (7.12), (7.13),and (7.14) are satisfied wih $p \leq \xi + \eta + 1$ ， $p \leq 2 \eta + 2$ , then the method is of order $\boldsymbol { p }$ NED.

To obtain the formulas of order $2 s$ , Butcher assumed (7.14) with $p = 2 s$ (i.e. the $c _ { i }$ and $b _ { i }$ are the coeficients of the Gaussian quadrature formula) and (7.12) with $\eta = s$ . Then it can be shown that (7.13) is also satisfied with $\xi = s$ . Then Theorem 7.4 applies with $p \ = 2 s$ (a simple explanation of the order result via the collocation idea will be given below). For $s = 3$ and 4 the methods are given in Tables 7.4 and 7.5. The coefficients can still be expressed by radicals for $s = 5$ and are given in Butcher (1964a), p.57.

Table 7.4. Kuntzmann-Butcher method, order 6

$$
\begin{array} { r } { \frac { 1 } { 2 } - \frac { \sqrt { 1 5 } } { 1 0 } \qquad \frac { 5 } { 3 6 } \qquad \frac { 2 } { 9 } - \frac { \sqrt { 1 5 } } { 1 5 } \quad \frac { 5 } { 3 6 } - \frac { \sqrt { 1 5 } } { 3 0 } } \\ { \frac { 1 } { 2 } \qquad \frac { 5 } { 3 6 } + \frac { \sqrt { 1 5 } } { 2 4 } \qquad \frac { 2 } { 9 } \qquad \frac { 5 } { 3 6 } - \frac { \sqrt { 1 5 } } { 2 4 } } \\ { \frac { 1 } { 2 } + \frac { \sqrt { 1 5 } } { 1 0 } \quad \left. \begin{array} { c c c c } { \frac { 5 } { 3 6 } + \frac { \sqrt { 1 5 } } { 3 0 } } & { \frac { 2 } { 9 } + \frac { \sqrt { 1 5 } } { 1 5 } } & { \frac { 5 } { 3 6 } } \\ { \frac { 5 } { 1 8 } \qquad } & { \frac { 4 } { 9 } \qquad } & { \frac { 5 } { 1 8 } } \end{array} \right. } \end{array}
$$

Impressive numerical results from celestial mechanics for these methods were first reported in the thesis of D. Sommer (see Sommer (1965)).

# IR K methods based on Lobatto quadrature

Lobatto quadrature rules (Lobatto (1852)， Radau (1880)， p.307) modify the idea of Gaussian quadrature by requiring that the first and the last node coincide with the interval ends, i.e. $c _ { 1 } { = } 0 , \ c _ { s } { = } 1$ . These are easier to handle and, in a step-by-step procedure, can be used twice The biornigng $c$ 's arlyhen ad imally the zergs: $\dot { P } _ { s - 2 } ^ { ( 1 , 1 ) } ( \bar { x } )$ $P _ { s - 1 } ^ { \prime } ( x )$ Abramowitz-Stegun (1964), 25.4.32 for the interval [-1,1]) and lead to formulas of order $2 s - 2$ . J.C. Butcher (1964a, p.51), (1964c) then found that Lobatto quadrature rules can be extended to IRK-methods whose coefficient matrix is zero in the first line and the last column. The first and the last stage then become explicit and the number of implicit stages reduces to $s - 2$ ，while the order remains $2 s - 2$ . The methods are characterized by $B \left( 2 s - 2 \right)$ and $C \left( s - 1 \right)$ (see (7.12), (7.13)). For $s = 3$ and 4, the coefficients are given in Table 7.6.

Table 7.5. Kuntzmann-Butcher method, order 8   

<table><tr><td>W2 2 1</td><td>W1</td><td>ω{-εy+ω4 ω}-ε-e4</td><td>ε115 ωje&#x27;s W1-w}-ω4</td></tr><tr><td>w 2</td><td>ε11ε}+eA 国</td></tr><tr><td>1+ 2</td><td>50+ω}+w4 e}+w&#x27;s E</td></tr><tr><td>1+02 2</td><td>w1+5 ε}+εγ+e𝐴 εì+ε丨e𝐴</td></tr><tr><td>2w1 e=1-√30 8 144 35 =2（+23）， 24 ω4=2（+),</td><td>W1 2wi 2w 201 e=1+√30 8+ 144&#x27; =(15-230）</td></tr></table>

Table 7.6. Butcher's Lobatto formulas of orders 4 and 6   

<table><tr><td></td><td></td><td></td><td></td><td>0 5-V5</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>10</td><td>5+√5 60</td><td>1</td><td>15--7V5 60</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>5+V5</td><td>5-V5</td><td>15+7V5</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>10</td><td>60</td><td>60</td><td>6</td><td></td></tr><tr><td>2</td><td>4</td><td>4</td><td></td><td>1</td><td>1</td><td>5-V5</td><td>5+V5</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td></td><td>6</td><td>12</td><td>12</td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td>五</td><td>5</td><td>1</td></tr><tr><td></td><td>1</td><td>2</td><td></td><td></td><td>12</td><td></td><td>12</td><td>12</td></tr></table>

We shall see in Volume II that these methods, although prefer-able as concerns the relation between order and implicit stages，are not sufficiently stable for stiff differential equations.

# IRK as collocation methods

"Es ist erstaunlich dass die Methode trotz ihrer Primitivitat und der geringen Rechenarbeit in vielen Fallen ... sogar gute Ergebnisse liefert."   
(Collatz, 1951)

After 1970 it became clearer and clearer in a series of papers (Wright (1970), Hulme (1972),de Boor and Swartz (1973), Nbrset and Wanner (1979)) that, and how, many IRK methods are equivalent to collocation methods and that their order properties are very natural. Later, in the chapter on stiff equations, we shall see an extension of this idea ("Perturbed Collocation") which covers all RK methods.

The concept of collocation is old and universal in numerical analysis (see e.g. pp. 28,29,32,181,411,453,483,495 of Collatz (1960), Frazer, Jones and Skan (1937)). For ordinary differential equations it consists in searching for a polynomial of degree s whose derivative coincides ("co-locates") at s given points with the vector field of the differential equation:

Definition 7.5. For s a positive integer and $c _ { 1 } , . . . , c _ { s }$ real numbers (typically between O and 1)， the corresponding collocation polynomial $u \left( x \right)$ of degree $s$ is defined by

$$
\begin{array} { l } { { u \left( x _ { 0 } \right) = y _ { 0 } \qquad \mathrm { ( i n i t i a l ~ v a l u e ) } } } \\ { { u ^ { \prime } ( x _ { 0 } { + } c _ { i } h ) = f \left( x _ { 0 } { + } c _ { i } h , u \left( x _ { 0 } { + } c _ { i } h \right) \right) \quad i = 1 , \ldots , s . } } \end{array}
$$

The numerical solution is then given by

$$
y _ { 1 } = u \left( x _ { 0 } { + } h \right) .
$$

If some of the $c$ 's coincide, the collocation condition (7.18.b) will contain higher derivatives and lead to multi-derivative methods (see Section I.12). Accordingly, for the moment, we suppose them all different.

Theorem 7.6. The collocation method (7.18) is equivalent to the sstage IRK method with

$$
a _ { i j } \ = \int \displaylimits _ { 0 } ^ { c _ { i } } l _ { j } ( t ) d t \ , \quad b _ { j } \ = \int \displaylimits _ { 0 } ^ { 1 } l _ { j } ( t ) d t \qquad i , j = 1 , \dots , s \ ,
$$

where the $l _ { j } ( s )$ are the Lagrange polynomials

$$
l _ { j } ( t ) = \prod _ { k \neq j } ( t { - } c _ { k } ) / \prod _ { k \neq j } ( c _ { j } { - } c _ { k } ) .
$$

Proof: Put $\mathbf { \boldsymbol { \mathscr { z } } } ^ { \prime } ( \boldsymbol { \mathscr { x } } _ { 0 } + \boldsymbol { \mathscr { c } } _ { i } \boldsymbol { h } ) = \boldsymbol { \mathscr { k } } _ { i } ,$ so that

Then integrate

$$
u ^ { \prime } ( x _ { 0 } + t h ) = \sum _ { j = 1 } ^ { s } k _ { j } { \cdot } l _ { j } ( t ) \qquad \mathrm { ( L a g r a n g e ) } .
$$

$$
u \left( x _ { 0 } + c _ { i } h \right) = y _ { 0 } + h \intop _ { 0 } ^ { c _ { i } } u \prime ( x _ { 0 } + t h ) d t
$$

and insert into (7.18.b) together with (7.19). The IRK-method (7 then comes out. QED.

Theorem 7.7. An $I R K$ -method with all $c _ { i }$ different and of order at least s is a colocation method iff(7.12) is true for $\eta = s$

Proof: (7.12) determines the $a _ { i j }$ uniquely. We write it as

$$
\sum _ { j = 1 } ^ { s } a _ { i j } p \left( c _ { j } \right) = \intop _ { 0 } ^ { c _ { i } } p \left( s \right) d s
$$

for all polynomials $p$ of degree $\leq s - 1$ The $a _ { i j }$ given by (7.19) satisfy this relation,because (7.19)inserted into (7.21) isjust the Lagrange interpolation formula. QED.

Theorem 7.8. Let M $\scriptstyle ( x \ ) = \prod _ { i = 1 } ^ { s } ( x - c _ { i } )$ and suppose that $M$ is orthogonal to potynomials of degree r-1,

$$
\int _ { 0 } ^ { 1 } M \left( s \right) s ^ { q - 1 } d s = 0 \qquad q = 1 , \ldots , r \ ,
$$

then method (7.18) has order $p = s + r$

Proof: The following proof uses the Grobner-Alekseev formula, which gives nice insight in the background of the result. An alternative proof is indicated in Exercise 7 below. (7.22) means that the quadrature formula

$$
\begin{array} { l } { { \displaystyle x _ { 0 } + h \left( s \right) d s = h \sum _ { j = 1 } ^ { s } b _ { j } g \left( x _ { 0 } + c _ { j } h \right) + e r r \left( g \right) } } \\ { { \displaystyle x _ { 0 } } } \end{array}
$$

is of order $s + r = p$ , and its error is bounded by

$$
\vert e r r ( g ) \vert \leq C h ^ { p + 1 } { \cdot } \mathrm { m a x } | g ^ { ( p ) } ( x ) | ~ .
$$

The principal idea of the proof is now the following: we consider

$$
u ^ { \prime } ( x ) = f \left( x , u \left( x \right) \right) + \biggl ( u ^ { \prime } ( x ) - f \left( x , u \left( x \right) \right) \biggr )
$$

as a perturbation of

$$
y ^ { \prime } ( x ) = f \left( x , y \left( x \right) \right)
$$

and integrate the Grobner-Alekseev formula (I.14.18) with the quadrature formula (7.23). Due to (7.18.b), the result is identically zero, since at the collocation points the defect is zero. Thus from (7.23) and (7.24)

$$
\begin{array} { r } { \left| \left| \textbf { \em y } ( \boldsymbol { x } ) - \boldsymbol { u } \left( \boldsymbol { x } \right) \right| \right| \ = \ \left| \left| \textbf { \ } e r r \left( \boldsymbol { g } \right) \right| \right| \ \leq \ \boldsymbol { C } \cdot \boldsymbol { h } ^ { p + 1 } \mathbf { \cdot } \mathbf { m a x } \left| \left| \textbf { \boldsymbol { g } } ^ { ( p ) } ( \boldsymbol { s } ) \right| \right| \ , } \end{array}
$$

where

$$
g \left( s \right) = D _ { 3 } y \left( x , s , u \left( s \right) \right) \cdot \left( u ^ { \prime } ( s ) - f \left( s , u \left( s \right) \right) \right) \ ,
$$

and $D _ { 3 }$ is the partial derivative with respect to the initial value $u \left( s \right)$ Thus, we see that the local error behaves like $\mathbf { O } ( h ^ { p + 1 } )$

There remains, however, a small technical detail: to show that the derivatives of $g \left( x \right)$ remain bounded for $h  ~ 0$ . These derivatives contain partial derivatives of $f \left( x , y \right)$ and derivatives of $u \left( x \right)$ . We shall see in the next theorem that these derivatives remain bounded for $h  0$ . QED.

Theorem 7.9. (Hulme (1972)). The collocation polynomial $u \left( x \right)$ gives rise to a continuous $J R K$ method of order s, i.e. for all $x _ { 0 } { \le } x \le x _ { 0 } { + } h$ we have

$$
\lVert \ y ( x ) - u ( x ) \rVert \ \leq \ C \cdot h ^ { s + 1 } \ .
$$

M oreover, for the derivatives of $u \left( x \right)$ we have

$$
| |  { y } ^ { ( k ) } ( x ) - u ^ { ( k ) } ( x ) | | \ \le  { C } \cdot h ^ { s + 1 - k } \qquad k = 0 , \ldots , s .
$$

Proof: The exact solution $y \left( x \right)$ satisfies the collocation condition everywhere, hence also at the points $\boldsymbol { x } _ { 0 } + \boldsymbol { c } _ { i } h$ . So, in exactly the same way as in the proof of Theorem 7.6, we apply the Lagrange interpola-tion formula to $y ^ { \prime } ( x )$ ：

$$
y ^ { \prime } ( x ) = \sum _ { j = 1 } ^ { s } f \left( x _ { 0 } + c _ { j } h , y \left( x _ { 0 } + c _ { j } h \right) \right) l _ { j } ( t ) + q \left( x \right) , \qquad x = x _ { 0 } + t h
$$

where the interpolation error， if $y \left( x \right)$ is sufficiently smooth， is $q \left( x \right) = \mathbf { O } \left( h ^ { s } \right) .$ Integration gives for ${ x } = { x _ { 0 } } + t h$

$$
y \left( x \right) = y _ { 0 } + \sum _ { j = 1 } ^ { s } f \left( x _ { 0 } { + } c _ { j } h , y \left( x _ { 0 } { + } c _ { j } h \right) \right) h \int _ { 0 } ^ { t } l _ { j } ( s ) d s + R \left( x \right)
$$

where ${ \textbf { \textsf { P } } } ( x ) = \mathbf { O } ( h ^ { s + 1 } )$ Subtracting from this the coresponding expression for $u \left( x \right)$ we obtain

$$
\begin{array} { l } { { \displaystyle y \left( x \right) - u \left( x \right) = h \sum _ { j = 1 } ^ { s } \left( f \left( x _ { 0 } { + } c _ { j } h , y \left( x _ { 0 } { + } c _ { j } h \right) \right) \right. } } \\ { { \displaystyle \qquad \left. - f \left( x _ { 0 } { + } c _ { j } h , u \left( x _ { 0 } { + } c _ { j } h \right) \right) \right) \int l _ { j } ( s ) d s + R \left( x \right) . } } \end{array}
$$

From here on, our job is done by trivial estimates: let

$$
\begin{array} { r l } & { B _ { \mathrm { ~ 0 ~ } } = \mathrm { ~ \operatorname* { m a x } _ { \mathrm { ~ 0 ~ } } ~ } \sum \big | \int \boldsymbol { l } _ { j } ( s ) d s \big | } \\ & { \qquad \mathrm { ~ \operatorname* { m a x } _ { \mathrm { ~ 0 ~ } } ~ } \boldsymbol { j } \mathbin { \int \displaylimits _ { 0 } ^ { \mathrm { ~ 1 ~ } } } \jmath _ { j } ( s ) d s \big | } \\ & { B _ { k } = \mathrm { ~ \operatorname* { m a x } _ { \mathrm { ~ 0 ~ } } ~ } \sum \big | \boldsymbol { l } _ { j } ^ { ( k - 1 ) } ( t ) \big | \qquad \mathrm { f o r ~ } k = 1 , 2 , \cdots } \\ & { \qquad 0 \le t \le 1 \quad j } \end{array}
$$

and introduce the Lipschitz condition for $f$ , to obtain for

$$
\begin{array} { r } { M \ = \ \underset { x _ { 0 } \leq x \leq x _ { 0 } + h } { \mathrm { m a x } } \ \left. \ y \left( x \right) - u \left( x \right) \right. } \end{array}
$$

the inequality

$$
M \ \leq \ h L B _ { \ 0 } M \ + \ \operatorname* { m a x } \parallel R \left( x \right) \parallel .
$$

This gives (17.26). If we differentiate (17.28) $k$ -times using $R \mathbf { \Lambda } ^ { ( k ) } ( x ) { = } \mathbf { O } ( h ^ { \dot { s } + 1 - k } )$ and estimate, we obtain

$$
\mathrm { a x } \parallel y ^ { ( k ) } ( x ) - u ^ { ( k ) } ( x ) \parallel \perp \perp \perp _ { { \cal L } B _ { k } M } + \mathrm { O } ( h ^ { s + 1 - k } ) ,
$$

which gives (17.27) since ${ \cal M } = 0 ( h ^ { s + 1 } ) .$ QED.

# Exercises

1. Compute the one-point collocation method ( ${ \bf \Phi } _ { s } = 1 { \bf \Phi } _ { s }$ ）with $c _ { i } = 0$ and compare with (7.2). Determine its order in dependence of 0.   
2. Compute all collocation methods with $s = 2$ of order 2 in dependence of $c _ { 1 }$ and $c _ { 2 }$   
3. Specify in the method of Exercise 2 $c _ { 1 } { = } 1 / 3$ ， ${ c _ { 2 } } ^ { = 1 }$ as well as ${ \boldsymbol { c } } _ { 1 } = 0$ ， $c _ { 2 } { = } 2 / 3$ . Determine the orders of the obtained methods and explain.   
4. Interpret the implicit midpoint rule (7.4) and the explicit Euler method as collocation methods. Is Method (7.5) a collocation method? Method (7.6)?

Ehle IIA , order 4

Ehle IIA , order 5   

<table><tr><td>4-V6</td><td>88-7V6</td><td>296-169V6</td><td>-2+3V6</td></tr><tr><td>10</td><td>360</td><td>1800</td><td>225</td></tr><tr><td>4+V6</td><td>296+169V6</td><td>88+7V6</td><td>-2-3V6</td></tr><tr><td>10</td><td>1800</td><td>360</td><td>225</td></tr><tr><td rowspan="2">1</td><td>16-V6</td><td>16+V6</td><td>1</td></tr><tr><td>36</td><td>36</td><td>9</td></tr><tr><td rowspan="2"></td><td>16-V6</td><td>16+V6</td><td>1</td></tr><tr><td>36</td><td>36</td><td>9</td></tr></table>

Table 7.7. Methods of Fhle   

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>5</td><td>1</td><td>1</td></tr><tr><td>2</td><td>24</td><td>3</td><td>24</td></tr><tr><td>1</td><td>1-6</td><td>2</td><td>1</td></tr><tr><td></td><td></td><td>3</td><td>6</td></tr><tr><td></td><td>1</td><td>2</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>6</td><td>3</td><td>6</td></tr></table>

5. Determine the ordcrs of the methods of Tablc 7.7. (Hint. Use Thcorems 7.7 and 7.8). Generalize to arbitrary s (Ehle (1968)).

6.(Cauchy (1824)). Find from Equation (7.2) conditions for the function $f \left( x , y \right)$ such that for scalar differential equations $y _ { 1 }$ (explicit Euler) ≥ y(x1) ≥ y1(implicit Euler). Compute five steps with $h = 0 . 2$ with both methods to obtain upper and lower bounds for y(1), the solution of

$$
y ^ { \prime } = \cos \frac { x + y } { 5 } ~ , ~ y \left( 0 \right) = 0 ~ .
$$

Cauchy's result: $0 . 9 6 5 9 \leq y \left( 1 \right) \leq 0 . 9 8 1 0$ .For one single step with $h = 1$ he obtained $0 . 9 2 6 { \le } y \left( 1 \right) { \le } 1$

Compute the exact solution by elementary integration.

7. (Butcher (1964a)). Give an algebraic proof of Theorem 7.8. Hint. From Theorem 7.7 we have (7.12) for $\eta = s$ . Next the condi-tions (7.14) with $p = s + r$ (Theory of Gaussian quadrature formu-fodr $\xi = r$ tby te vaeters $\begin{array} { r } { u _ { j } = \sum _ { i } b _ { i } c _ { i } ^ { q - 1 } a _ { i j } } \end{array}$ $\nu _ { j } { = } b _ { j } { \big ( } 1 { - } c _ { j } ^ { q } { \big ) } / q$ $( j = 1 , \ldots , s )$ monde matrix

$$
V = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { } } \\ { { c _ { 1 } } } & { { c _ { 2 } } } & { { \cdots } } & { { c _ { s } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots \vdots } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { } } \\ { { c _ { 1 } ^ { s - 1 } } } & { { c _ { 2 } ^ { s - 1 } } } & { { \cdots } } & { { c _ { s } ^ { s - 1 } } } \end{array} \right) .
$$

Finally apply Theorem 7.4.

# 11.8. Asymptotic expansion of the global error

"Mein Verzicht auf das Restglied war leichtsinnig.." (W. Romberg,1979)

Our next goal will be to perfect Richardson's extrapolation method (see Section I.4) by doing repeated extrapolation and elim-inating more and more terms $C h ^ { p + \mathbb { k } }$ of the error. A sound theoretical basis for this procedure is given by the study of the asymptotic behaviour of the global error. For problems of the type $y ^ { \prime } = f \left( x \right)$ ， which lead to integration, the answer is given by the Euler-Maclaurin formula and has been exploited by Romberg (1955) and his successors. The first rigorous treatments for differential equations are due to Henrici (1962) and Gragg (1964) (see also Steter (1973)). We shall foliow here the successive elimination of the error terms given by Hairer and Lubich (1984)， which also generalizes to multistep methods.

# The local error

Suppose we have a one-step method which we write as

$$
y _ { n + 1 } = y _ { n } + h \Phi ( x _ { n } , y _ { n } , h ) .
$$

If the method is of order $\boldsymbol { p }$ , it possesses at each point of the solution $y \left( x \right)$ a local error of the form

$$
\begin{array} { r l } { { } } & { { y ( x + h ) - y ( x ) - h \Phi ( x , y ( x ) , h ) = } } \\ { { } } & { { { d } _ { p + 1 } ( x ) h ^ { p + 1 } + \ldots + { d } _ { N + 1 } ( x ) h ^ { N + 1 } + 0 ( h ^ { N + 2 } ) } } \end{array}
$$

whenever the differential equation is sufficiently differentiable. For Runge-Kutta methods these error terms have becn computed in Section II.2 (see also Theorem 3.2).

# The global error

Let us now set $y _ { n } \ = : y _ { h } \left( x \right)$ for the numerical solution at $x ~ = { x _ { 0 } } ^ { + n h }$ . We then know from Theorem 3.6 that the global error behaves like $h ^ { p }$ . We shall search for a function $e _ { p } ( x )$ such that

$$
y _ { h } ( x ) - y ( x ) = e _ { p } ( x ) h ^ { p } + \mathfrak { o } \left( h ^ { p } \right) .
$$

The main idea is to consider

$$
y _ { h } ( x ) - e _ { p } ( x ) h ^ { p } = : \hat { y } _ { h } ( x )
$$

as the numerical solution of a new method

$$
\hat { y } _ { n + 1 } = \hat { y } _ { n } + h \hat { \Phi } ( x _ { n } , \hat { y } _ { n } , h ) .
$$

By comparison with (8.1), we see that the increment function for the new method is

$$
\hat { \Phi } ( x , \hat { y } , h ) = \Phi ( x , \hat { y } + e _ { p } ( x ) h ^ { p } , h ) - ( e _ { p } ( x + h ) - e _ { p } ( x ) ) h ^ { p - 1 } .
$$

Our task is to find a function $e _ { p } { \varphi } _ { \ast } ( x )$ ,with $e _ { p } ( x _ { 0 } ) = 0$ ， such that the method with increment function $\Phi$ is of order $p + 1$

Expanding the local error of the one-step method $\hat { \Phi }$ into powers of $h$ we obtain

$$
\begin{array} { r l r } { \quad } & { } & { y \left( x + h \right) - y \left( x \right) - h \hat { \Phi } ( x , y \left( x \right) , h ) = } \\ { \quad } & { } & { = \left( d _ { p + 1 } ( x ) - \frac { \partial f } { \partial y } ( x , y \left( x \right) ) e _ { p } ( x ) + e _ { p } ^ { \prime } ( x ) \right) h ^ { p + 1 } + \mathbf { O } ( h ^ { p + 2 } ) } \end{array}
$$

where wc have used

$$
\frac { \partial \Phi } { \partial y } ( x , y , 0 ) = \frac { \partial f } { \partial y } ( x , y ) .
$$

The term in $h ^ { p + 1 }$ vanishes if $e _ { p } ( x )$ is defined as the solution of

$$
\begin{array} { r } { e _ { p } ^ { \prime } ( x ) = \frac { \partial f } { \partial y } ( x , y ( x ) ) e _ { p } ( x ) - d _ { p + 1 } ( x ) , ~ e _ { p } ( x _ { 0 } ) = 0 . } \end{array}
$$

By Theorem $^ \textrm { \scriptsize 3 6 }$ , applied to the method $\hat { \Phi }$ , we now have

$$
y _ { h } ( x ) - y ( x ) = e _ { p } ( x ) h ^ { p } + \mathbf { O } \bigl ( h ^ { p + 1 } \bigr )
$$

and the first term of the desired asymptotic expansion has been determined.

We now repeat the procedure with the method with increment function $\hat { \Phi }$ . It is of order $p + 1$ and again satisfies condition (8.7). The final result of this procedure is the following

Theorem 8.1 (Gragg (1964)). Suppose that a given method wih sufficiently smooth increment function $\Phi$ satisfies the consistency condition $\Phi ( x , y , 0 ) = f ( x , y )$ and possesses an expansion (8.2) for the local error. Then the global error has an asymptotic expansion of the form

$$
y _ { h } ( x ) - y ( x ) = e _ { p } ( x ) h ^ { p } + \cdot \cdot \cdot + e _ { N } ( x ) h ^ { N } + E _ { h } ( x ) h ^ { N + 1 }
$$

where the $e _ { j } ( x )$ are solutions of inhomogeneous differential equations of the form (8.8） with $e _ { j } ( x _ { 0 } ) = 0$ and $E _ { h } \left( x \right)$ is bounded for $x _ { 0 } \leq x \leq x _ { e n d }$ and $0 \leq h \leq h _ { 0 }$ .NED.

The differentiability propertics of the $e _ { j } ( \boldsymbol { x } )$ depend on those of $f$ and $\Phi$ (see (8.8) and (8.2)). The expansion (8.10) will be the theoretical basis for all discussions of extrapolation methods.

# Examples

1. For the equation $y ^ { \prime } { = } y$ and Euler's method we have with $h = 1 / n$ and $x = 1$ ,using the binomial theorem,

$$
y _ { h } ( 1 ) = ( 1 + \frac { 1 } { n } ) ^ { n } = 1 + 1 + ( 1 - \frac { 1 } { n } ) \frac { 1 } { 2 ! } + ( 1 - \frac { 1 } { n } ) ( 1 - \frac { 2 } { n } ) \frac { 1 } { 3 ! } + \cdot \cdot \cdot
$$

By multiplying out, this gives

$$
y _ { h } ( 1 ) - y ( 1 ) = \sum _ { i = 1 } ^ { \infty } h ^ { i } \sum _ { j = 1 } ^ { \infty } { \frac { S _ { i + j } ^ { ( j ) } } { ( i + j ) ! } } = - 1 . 3 5 9 h + 1 . 2 4 6 h ^ { 2 } \pm \cdot \cdot \cdot
$$

where the $s _ { i } ^ { \phantom { \dagger } } { } ^ { ( j ) }$ are the Stirling numbers of thc first kind (1730,see Abramowitz-Stegun (1964)， Section 24.1.3). This is, of course, the Taylor series for the function

$$
\begin{array} { r } { \left( 1 + h \right) ^ { 1 / h } - e \ = \exp ( 1 - \displaystyle \frac { h } { 2 } + \displaystyle \frac { h ^ { 2 } } { 3 } \pm \displaystyle \cdots ) - e } \\ { = e ( - \displaystyle \frac { 1 } { 2 } h + \frac { 1 1 } { 2 4 } h ^ { 2 } - \displaystyle \frac { 7 } { 1 6 } h ^ { 3 } \pm \ \cdots ) } \end{array}
$$

with convergence radius $r \ = 1$

2. For the differential equation $y ^ { \prime } = f \left( x \right)$ and the trapezoidal rule (7.5), the expansion (8.10) becomes

$$
y _ { h } ( 1 ) - \int _ { 0 } ^ { 1 } f \left( x \right) d x \ = \ \sum _ { k = 1 } ^ { N } \frac { h ^ { 2 k } } { ( 2 k ) ! } \ : B _ { 2 k } \left( f ^ { \left( 2 k - 1 \right) } ( 1 ) - f ^ { \left( 2 k - 1 \right) } ( 0 ) \right) \ + \ E r \left( \frac { 1 } { 2 k } + \frac { 1 } { 2 } \right)
$$

the well known Euler-Maclaurin formula (1736). For $N \to \infty$ ,the series will usually diverge, due to the fast growth of the Bernoulli numbers for large $k$ . It may, however, be useful for small values of $N$ and we call it an asymptotic expansion (Poincaré (1893)).

# Variable h

Theorem 8.1 is not only valid for equal step sizes. A reasonable assumption for the case of variable step sizes is the existence of a function $\tau ( x ) > 0$ such that the step sizes depend as

$$
x _ { n + 1 } - x _ { n } = \tau ( x _ { n } ) h
$$

on a parameter h . Then the local error expansion (8.2) becomes

$$
\begin{array} { r l r } & { } & { y \left( x + \tau ( x ) h \right) - y \left( x \right) - h \tau ( x ) \Phi ( x , y \left( x \right) , \tau ( x ) h ) } \\ & { } & \\ & { } & { \qquad = d _ { p + 1 } ( x ) \tau ^ { p + 1 } ( x ) h ^ { p + 1 } + \textrm { . . . } } \end{array}
$$

and instead of (8.5) we have

$$
\begin{array} { l } { { \hat { \Phi } ( x , \hat { y } , \tau ( x ) h ) = \Phi ( x , \hat { y } + e _ { p } ( x ) h ^ { p } , \tau ( x ) h ) } } \\ { { \qquad - \ \frac { h ^ { p } } { h \tau ( x ) } [ e _ { p } ( x + \tau ( x ) h ) - e _ { p } ( x ) ] \ . } } \end{array}
$$

With this the local error expansion for the new method becomes, instead of (8.6),

$$
\begin{array} { r l } & { \qquad y \left( x + \tau ( x ) h \right) - y \left( x \right) - h \thinspace \tau ( x ) \hat { \Phi } ( x \mathrm { , ~ } y \left( x \right) , \tau ( x ) h ) } \\ & { \qquad \displaystyle \tau \left( x \right) \left( d _ { p + 1 } ( x ) \tau ^ { p } ( x ) - \frac { \partial f } { \partial y } ( x \mathrm { , ~ } y \left( x \right) ) e _ { p } ( x ) + e _ { p } ^ { \prime } ( x ) \right) h ^ { p + 1 } + { \sf O } ( h ^ { p + 1 } ) . } \end{array}
$$

and the proof of Theorem 8.1 generalizes with slight modifications.

# Negative h

The most important extrapolation algorithms will use asymptotic expansions with even powers of $h$ . In order to provide a theoretical basis for these methods, we need to explain the meaning of $y _ { h } \left( x \right)$ for h negative.

Motivation: We write (8.1) as

$$
y _ { h } ( x + h ) = y _ { h } ( x ) + h \Phi ( x , y _ { h } ( x ) , h )
$$

and replace h by $- h$ to obtain

$$
y _ { - h } ( x { - } h ) = y _ { - h } ( x ) - h \Phi ( x , y _ { - h } ( x ) , - h ) .
$$

Next we replace x by $x + h$ which gives

$$
y _ { - h } ( x ) = y _ { - h } ( x + h ) - h \Phi ( x + h , y _ { - h } ( x + h ) , - h ) .
$$

This is an implicit equation for $y _ { - h } ( x + h \ )$ ， which possesses a unique solution for sufficiently small h (by the implicit function theorem). We write this solution in the form

$$
y _ { - h } ( x + h ) = y _ { - h } ( x ) + h \Phi ^ { * } ( x , y _ { - h } ( x ) , h ) .
$$

The comparison of (8.12) and (8.13) (with $A = y _ { - h } ( x + h )$ ， $B = \boldsymbol { y } _ { - h } \left( \boldsymbol { x } \right)$ ） leads us to the following definition:

Definition. Let $\Phi ( x , y , h )$ be the increment function of a method. Then we define the increment function $\Phi ^ { * } ( x \ , y \ , h \ )$ of the adjoint method by the pair of formulas

$$
\begin{array}{c} \begin{array} { l } { { B } } \\ { { { \cal B } } } \end{array} = { \cal A } \ - h \Phi ( x + h , A , - h )  \\ { \ } \\ { { \cal A } } \\ { \ = { \cal B } } \end{array}
$$

Example: The adjoint method of explicit Euler is implicit Euler.

Theorem 8.2. Let $\Phi$ be the Runge-Kutta method (7.7) wih coeffi cients $a _ { i j } , b _ { j } , c _ { i }$ $( i , j ~ = ~ 1 ~ , ~ \dots ~ , ~ s$ ). Then the adjoint method $\Phi ^ { * }$ is equivalent to a RK method with s stages and with coeffcients

$$
\begin{array} { r l } & { c _ { i } ^ { * } = 1 - c _ { s + 1 - i } } \\ & { a _ { i j } ^ { * } = b _ { s + 1 - j } - a _ { s + 1 - i , s + 1 - j } } \\ & { b _ { j } ^ { * } = b _ { s + 1 - j } \ . } \end{array}
$$

Proof: The formulas (8.14) indicate that for the definition of the adjoint method we have, starting from (7.7), to exchange yo y1 $h \longleftrightarrow - h$ and replace $x _ { 0 } \to x _ { 0 } + h$ . This then leads to

$$
\begin{array} { l } { { k _ { i } = f ( x _ { 0 } { + } ( 1 { - } c _ { i } ) h , y _ { 0 } + h { \sum _ { j } } ( b _ { j } { - } a _ { i j } ) k _ { j } ) } } \\ { { \qquad y _ { 1 } = y _ { 0 } + h { \sum _ { j } } b _ { j } k _ { j } . } } \end{array}
$$

In order to preserve the usual natural ordering of $c _ { 1 } , \ldots , c _ { s }$ ， we also permute the $k _ { i }$ -values and replace all indices $i$ by $s + 1 - i$ . QED.

# Properties of the adjoint method

Theorem 8.3. $\Phi ^ { * * } = \Phi$

Proof: This property, which is the reason for the name "adjoint", is seen by replacing $h  ~ - h$ and then $x \to \ x + h$ ， $B  A$ ， $A  B$ in (8.14). QED.

Theorem 8.4. The adjoint method has the same order as the original method. Its principal error term is the error term of the first method multiplied by $( - 1 ) ^ { p }$

Proof: We replace $h$ by $- h$ in (8.2), then $x  \ x + h$ and rearrange the terms. This gives (using

$$
\begin{array} { r l } & { \mathfrak { n s . } \mathrm { T h i s ~ g i v e s ~ } ( \mathrm { u s i n g ~ } d _ { p + 1 } ( x + h ) = d _ { p + 1 } ( x ) + \mathfrak { O } ( h ) ) } \\ & { y ( x ) + d _ { p + 1 } ( x ) h ^ { p + 1 } ( - 1 ) ^ { p } + \mathfrak { O } ( h ^ { p + 2 } ) } \\ & { \qquad = y \left( x + h \right) - h \Phi ( x + h , y ( x + h ) , - h ) . } \end{array}
$$

Here we let A be the left-hand side of this identity, $B \ = \ y \left( x \ { + } h \ \right)$ ， and use (8.14). This leads to

$$
( x + h ) = y ( x ) + d _ { p + 1 } ( x ) h ^ { p + 1 } ( - 1 ) ^ { p } + h \Phi ^ { * } ( x , y ( x ) , h ) + { \bf O } ( h ^ { p + 2 } )
$$

which expresses the statement of the theorem. QED.

Theorem 8.5. The adjoint method has exactly the same asymptotic expansion (8.1O) as the original method, with h replaced by $- h$

Proof: We repeat the procedure which led to the proof of Theorem 8.1, with $h$ negative. The first separated term corresponding to (8.9) will be

$$
y _ { - h } ( x ) - y ( x ) = e _ { p } ( x ) ( - h ) ^ { p } + \mathbf { O } ( h ^ { p + 1 } ) \ .
$$

This is true because the solution of (8.8) with initial value $e _ { p } ( x _ { 0 } ) = 0$ has the same sign change as the inhomogenity $d _ { p + 1 } ( x )$ . This settles the first term. To continue, we prove that the transformation (8.4) commutes with the adjunction operation, i.e. that

$$
\hat { \Phi } ^ { * } = ( \Phi ^ { * } ) \hat { \ } .
$$

In order to prove (8.15)，we obtain from (8.4) and the definition of $\hat { \Phi }$

$$
\begin{array} { r l } & { y _ { h } ( x + h ) - e _ { p } ( x + h ) h ^ { p } } \\ & { \quad = y _ { h } ( x ) - e _ { p } ( x ) h ^ { p } + h \hat { \Phi } ( x , y _ { h } ( x ) - e _ { p } ( x ) h ^ { p } , h ) \ . } \end{array}
$$

Here again, we substitute $h  ~ - h$ followed by $x  \ x + h$ . Finally， we apply (8.14） with $B = y _ { - h } ( x ) - e _ { p } ( x ) ( - h ) ^ { p }$ and $A \ = y _ { - h } ( x + h )$ $- e _ { p } ( x + h ) ( - h ) ^ { p }$ to obtain

$$
\begin{array} { r l r } { \boldsymbol { y } _ { - h } ( x + h ) - \boldsymbol { e } _ { p } ( x + h ) ( - h ) ^ { p } = } & { { } } & { ( 8 . 1 \times 1 0 ^ { - 3 } ) } \\ { \boldsymbol { y } _ { - h } ( x ) - \boldsymbol { e } _ { p } ( x ) ( - h ) ^ { p } + \boldsymbol { h } \hat { \Phi } ^ { * } ( x , \boldsymbol { y } _ { - h } ( x ) - \boldsymbol { e } _ { p } ( x ) ( - h ) ^ { p } , h ) . } & { { } } & { } \end{array}
$$

On the other hand, if we perform the transformation (see Theorem 8.4)

$$
{ \hat { y } } _ { - h } ( x ) = y _ { - h } ( x ) - e _ { p } ( x ) ( - h ) ^ { p }
$$

and insert this into (8.13), we obtain (8.16) again, but this time with $( \Phi ^ { * } ) ^ { * }$ instead of $\hat { \Phi } ^ { * }$ This proves (8.15). QED.

# Symmetric methods

Definition 8.6. A method is symmetric if $\boldsymbol \Phi = \boldsymbol \Phi ^ { * }$

Example: The trapezoidal rule (7.5) and the implicit mid-point rule (7.4) are symmetric: the exchanges $y _ { 1 } \longleftrightarrow y _ { 0 } , h \longleftrightarrow - h$ and $x _ { 0 } \longleftrightarrow x _ { 0 } { + h }$ leave these methods invariant. The following two theorems can be found in Wanner (1973):

Theorem 8.7. 1f

$$
a _ { s - i + 1 , s - j + 1 } + a _ { i j } = b _ { s - j + 1 } = b _ { j } ~ ,
$$

then the corresponding RK method is symmetric.

Proof: See Theorem 8.2. The condition $c _ { i } \ = \ 1 \ - \ c _ { s + 1 + i }$ can be verified by adding up (8.17) for $j = 1 \ , \ \dots , \ s$ QED.

Theorem 8.8. A collocation method based on symmetrically distributed collocation points is symmetric.

Proof:If $c _ { i } \ = \ 1 \ - \ c _ { s + 1 - i }$ theLagrangepolynomialssatisfy $l _ { i } ( t ) = l _ { s + 1 - i } ( 1 - t )$ Condition (8.17) is then an easyconsequence of (7.19). QED.

The following important property of symmetric methods, known intuitively for many years, now follows from the above results:

Theorem 8.9. If in addition to the assumptions of Theorem 8.1 the underlying method is symmetric,then the asymptotic expansion (8.10) contains only even powers of h:

$$
y _ { h } ( x ) - y ( x ) = e _ { 2 q } ( x ) h ^ { 2 q } + e _ { 2 q + 2 } ( x ) h ^ { 2 q + 2 } + \cdot \cdot \cdot
$$

with $e _ { 2 j } ( x _ { 0 } ) = 0 .$

Proof: If $\Phi ^ { * } = \Phi$ ,we have $y _ { - h } ( x ) = y _ { h } ( x )$ from (8.13) and the result follows from Theorem 8.5. QED.

Example. The oldest example of such an expansion is the Euler-MacLaurin formula.

# Exercises

1. Assume the one-step method (8.1) to be of order $p \ \geq \ 2$ and in addition to $\Phi ( x , y , 0 ) = f ( x , y )$ assume

$$
\begin{array} { r } { \frac { \partial \Phi } { \partial h } ( x , y , 0 ) = \frac { \partial f } { \partial x } ( x , y ) + \frac { \partial f } { \partial y } ( x , y ) \cdot f \left( x , y \right) . } \end{array}
$$

Show that the principal local error term of the method $\hat { \Phi }$ defined in (8.5) is then given by

$$
\hat { d } _ { p + 2 } ( x ) = d _ { p + 2 } ( x ) - { \textstyle \frac { 1 } { 2 } } { \textstyle \frac { \partial f } { \partial y } } ( x , y ( x ) ) d _ { p + 1 } ( x ) - { \textstyle \frac { 1 } { 2 } } d _ { p + 1 } ^ { \prime } ( x ) .
$$

Verify that (8.19) is satisfied for all RK-methods of order $\geq 2$

2. Consider the second order method

$$
\frac { 1 } { { \left| \begin{array} { l l l } { \displaystyle { \frac { 1 } { 2 } } } & { \displaystyle { \frac { 1 } { 2 } } } & { \displaystyle { \frac { 1 } { 2 } } } \end{array} \right| } }
$$

applied to the problem $y ^ { \prime } = y , y ( 0 ) = 1 .$ Show that

$$
\begin{array} { l l l } { { d _ { 3 } ( x ) = \displaystyle \frac { 1 } { 6 } e ^ { x } ~ , } } & { { d _ { 4 } ( x ) = \displaystyle \frac { 1 } { 2 4 } e ^ { x } ~ , } } \\ { { e _ { 2 } ( x ) = \displaystyle - \frac { 1 } { 6 } x e ^ { x } ~ , } } & { { \hat { d } _ { 4 } ( x ) = \displaystyle - \frac { 1 } { 8 } e ^ { x } ~ . } } \end{array}
$$

3. Consider the sccond order method

$$
{ \begin{array} { r l } & { { \frac { 1 } { 2 } } } \\ & { { \frac { 1 } { 4 } } } \end{array} } { \left| \begin{array} { l l l } { { \frac { 1 } { 2 } } } & { } & { } \\ { 0 } & { 1 } \\ { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 4 } } } \end{array} \right| }
$$

Show that for this method

$$
\begin{array} { c } { { d _ { 3 } ( x ) = \displaystyle \frac { 1 } { 2 4 } \biggl ( F ( t _ { 3 2 } ) ( y ( x ) ) - \frac { 1 } { 2 } F ( t _ { 3 1 } ) ( y ( x ) ) \biggr ) } } \\ { { \displaystyle t _ { 4 } ( x ) = \frac { 1 } { 2 4 } \biggl ( F ( t _ { 4 4 } ) ( y ( x ) ) + \frac { 1 } { 4 } F ( t _ { 4 3 } ) ( y ( x ) ) - \frac { 1 } { 4 } F ( t _ { 4 1 } ) ( y ( x ) ) \biggr ) } } \end{array}
$$

in the notation of Table 2.1. Show that tnis implies

$$
\hat { d } _ { 4 } ( x ) = 0 \quad \mathrm { a n d } \quad e _ { 3 } ( x ) = 0 \ ,
$$

so that one step of Richardson extrapolation increases the order of the method by two. (Find a connection between this method and the GBS-algorithm of Section II.9.)

4. Discuss the symmetry of the other classes of IRK methods of Sec-ticn II.7. (Answer: they are not symmetric.)

# 11.9. Extrapolation methods

# Definition of the method

Let $y ^ { \prime } = f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) = y _ { 0 }$ bc a given differential system and $H > 0$ a basic step size. We choose a sequence of positive integers

$$
n _ { 1 } < n _ { 2 } < n _ { 3 } < \cdots
$$

and define the corresponding step sizes $h _ { 1 } > ~ h _ { 2 } > ~ h _ { 3 } > ~ \cdots .$ by $h _ { i } \ = H / n _ { i }$ . We then choose a numerical method of order $p$ and compute the numerical results of our initial value problem by performing $n _ { i }$ steps with step size $h _ { i }$ to obtain

$$
y _ { h _ { i } } ( x _ { 0 } + H ) = : T _ { i , 1 } .
$$

(The letter $\boldsymbol { r }$ stands for "trapezoidal rule" for historical reasons). We then eliminate as many terms as possible from the asymptotic expansion (8.10) by computing the interpolation polynomial

$$
p \left( h \right) = e _ { 0 } + e _ { p } h ^ { p } + e _ { p + 1 } h ^ { p + 1 } + \cdot \cdot \cdot + e _ { p + k - 2 } h ^ { p + k - 2 }
$$

such that

$$
p \left( h _ { i } \right) = T _ { i , 1 } \quad i = j , j - 1 , . . . , j - k + 1 ~ .
$$

Finally we "extrapolate to the limit" $h  ~ 0$ and use

$$
p \left( 0 \right) = e _ { 0 } = : T _ { j , k }
$$

as numerical result. Conditions (9.4) consist of $k$ linear equations for the k unknowns eo, ep ..\*., $e _ { 0 } , e _ { p } , \ldots , e _ { p + k - 2 }$

Example. For $k = 2$ ， $n _ { 1 } = 1$ ， $n _ { 2 } { = } 2$ the above definition is identical to the procedure in Section I1.4.

Theorem 9.1. The value $T _ { j , k }$ represents a numerical method of order $p + k - 1$

Proof: We compare (9.4) and (9.3) with the asymptotic expansion (8.10) which we write in the form (with $N = p + k - 1$ ）

$$
\begin{array} { c } { { T _ { i , 1 } = y \left( x _ { 0 } { + } H \right) + e _ { p } ( x _ { 0 } { + } H ) h _ { i } ^ { p } + \cdot \cdot \cdot } } \\ { { { } } } \\ { { + e _ { p + k - 2 } ( x _ { 0 } { + } H ) h _ { i } ^ { p + k - 2 } + \Delta _ { i } } } \end{array} ,
$$

where

$$
\Delta _ { i } = e _ { p + k - 1 } ( x _ { 0 } + H ) h _ { i } ^ { p + k - 1 } + E _ { h _ { i } } ( x _ { 0 } + H ) h _ { i } ^ { p + k } = 0 ( H ^ { p + k } )
$$

by the Vandermonde-like matrix

$$
\begin{array} { r } { A { \bf \Sigma } = \left( \begin{array} { c c c c } { 1 } & { \frac { 1 } { n _ { j } ^ { p } } } & { \cdots } & { \frac { 1 } { n _ { j } ^ { p + k - 2 } } } \\ { } & { } & { } & { } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { 1 } & { \frac { 1 } { n _ { j - k + 1 } ^ { p } } } & { \cdots } & { \frac { 1 } { n _ { j - k + 1 } ^ { p + k - 2 } } } \end{array} \right) . } \end{array}
$$

It is the same as (9.4), just with the right-hand side perturbed by the $\mathbb { O } ( H ^ { p + k } )$ -terms $\Delta _ { i }$ The matrix A is invertible (see Exercise 6). Therefore by subtraction we obtain, in particular,

$$
\begin{array} { r } { | y ( x _ { 0 } { + } H ) - e _ { 0 } | \ \leq \ \vert \vert  { A } ^ { - 1 } \vert \vert _ { \infty } \cdot \mathsf { m a x } \vert \Delta _ { i } \vert \ = \mathbf { O } ( H ^ { p + k } ) \ . } \end{array}
$$

QED.

Remark : The case $p = 1$ (as well as $p = 2$ with expansions in $h ^ { 2 }$ ） can also be treated by interpreting the difference $y \left( x _ { 0 } + H \right) - e _ { 0 }$ as an interpolation error (see (9.21)).

A great advantage of the method is that it provides a complete table of numerical results

$$
\begin{array} { c c c c c c c c c c c c c c } { T _ { 1 1 } } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } \\ { T _ { 2 1 } } & { } & { T _ { 2 2 } } & { } & { } & { } & { } & { } & { } & { } & { } \\ { T _ { 3 1 } } & { } & { T _ { 3 2 } } & { } & { } & { T _ { 3 3 } } & { } & { } & { } & { } & { } \\ { \therefore } & { } & { } & { } & { } & { } & { \dots } & { } & { } & { } & { } & { } \end{array}
$$

which form a sequence of embedded methods and allow easy estimates of the local error and strategies for variable order.

Several step-number sequences are in use for (9.1):

The "R omberg sequence" (Romberg (1955)):

The "Bulirsch sequence" (also mentioned by Romberg (1955)):

alternating powers of 2 with 1.5 times $2 ^ { k }$ . This sequence needs fewer function evaluations for higher orders than the previous one and became prominent through the success of the "Gragg-Bulirsch-Stoer algorithm" (Bulirsch - Stoer (1966)).

The above sequences have the property that for integration problem s $y ^ { \prime } = f \left( x \right)$ many function values can be saved and re-used for smaller $h _ { i }$ .Further, $\mathrm { l i m i n f } ( n _ { i + 1 } / n _ { i } )$ remains bounded away from 1 ("Toeplitz condition") which allows convergence proofs for $j = k \to \infty$ (Bauer - Rutishauser - Stiefel (1963)). However, if we work with differential equations and with fixed or bounded order, the most economic sequence is the "harmonic sequence" (Deuflhard (1983))

$$
1 , 2 , 3 , 4 , 5 , 6 , 7 , \cdots .
$$

# The Aitken - Neville algorithm

For the case $p = 1$ , (9.3) and (9.4) become a classical interpolation problem and we can compute the values of $T _ { j , k }$ economically by the use of classical methods. Since only we need the values of thc interpolation polynomials at the point $h = 0$ ， the most economical algorithm is that of "Aitken-Neville" (Aitken (1932)， Neville (1934), based on ideas of Jordan (1928)） which leads to

$$
T _ { j , k + 1 } = T _ { j , k } + { \frac { T _ { j , k } - T _ { j - 1 , k } } { ( n _ { j } / n _ { j - k } ) - 1 } } \ .
$$

# Rational ex trapolation

Many authors in the sixties claimed that it is better to use rational functions instead of polynomials in (9.3). In this case the formula (9.9) must be replaced by (Bulirsch - Stoer (1964))

$$
T _ { j , k + 1 } = T _ { j , k } \ + \ { \frac { T _ { j , k } - T _ { j - 1 , k } } { \left( { \frac { n _ { j } } { n _ { j - k } } } \right) \left[ 1 \ - \ { \frac { T _ { j , k } - T _ { j - 1 , k } } { T _ { j , k } - T _ { j - 1 , k - 1 } } } \right] \ - 1 } }
$$

where

$$
T _ { j , 0 } = 0 \ .
$$

For systems of differential equations the division of vectors is to be understood componentwise.

Later numerical experiments (Deuflhard (1983)) showed that rational extrapolation is nearly never more advantageous than polynomial ex trapolation.

We solve the problem

$$
y ^ { \prime } = { \bigl ( } - y \sin x ~ + 2 \tan x { \bigr ) } y ~ , ~ y { \bigl ( } \pi / 6 { \bigr ) } = { \frac { 2 } { \sqrt { 3 } } }
$$

with true solution $y \left( x \right) = 1 / \cos x$ and basic step size $H = 0 . 2$ by Euler's method. In Figure 9.1 we plot, for the three different step-number sequences (9.6)、 (9.7)， (9.8) respectively， the numerical work $\log _ { 1 0 } ( 1 + n _ { j } - 1 + n _ { j - 1 } - 1 + \ldots + n _ { j - k + 1 } - 1 )$ compared tothe precision $- \mathrm { l o g } _ { 1 0 } ( \ | T _ { j , k } \ - y ( x _ { 0 } { + } H ) | )$ in doublc logarithmic scale.

![](images/75add57eb93720037d410a5a92126b6a1e3e4e24137a08fc084d3a3b5cd2f3bd.jpg)  
Figure 9.1. Precision of extrapolated Euler for Example (9.11)

# Extrapolation with symmetric methods

If the basic method used is symmetric, we know that the underlying asymptotic expansion is in powers of $h ^ { 2 }$ (Theorem 8.9), and each extrapolation eliminates two powers of $h$ We may thus simply replace in (9.3) $h$ by $h ^ { 2 }$ and for $p = 2$ (i.e. $q = 1$ in (8.18)) also use the Aitken-Neville algorithm with this modification. This leads to

$$
T _ { j , k + 1 } = T _ { j , k } \ + \frac { T _ { j , k } \ - \ T _ { j - 1 , k } } { \left( n _ { j } / n _ { j - k } \right) ^ { 2 } - 1 }
$$

instead of (9.9).

Numerical Example. We solve Problem (9.11), using this time the implicit mid-point rule (7.4). This method is implicit, but due to the simple structure of the differential cquation, an application of the method just needs the solution of a quadratic equation. We again use the same basic step size $H = 0 . 2$ as above and the same step-numbcr sequences (9.6), (9.7), (9.8) and present the errors in a similar way in Figure 9.2.

![](images/6f9b21a98957d0458f03b0b7525a5db17b9cb5d95749f1ebb2f6290b00000a60.jpg)  
Figure 9.2. Precision of extrapolated implicit midpoint rule

# The Gragg or GBS method

"Since it is fully explicit GRAGG's algorithm is so ideally suited as a basis for RICHARDSON extrapolation that no other symmetric two-step algorithm can compete with it."

(HJ. Steter, 1970)

Here we can not do better than quote from Stetter (1970): "Expansions in powers of $h ^ { 2 }$ are extremely important for an efficient application of Richardson extrapolation. Therefore it was a great achievement that Gragg proved in 1963 that the quantity $S _ { h } \left( x \right)$ produced by the algorithm $( x = x _ { 0 } + 2 n h , x _ { i } = x _ { 0 } + i h$ ）

$$
\begin{array} { c } { { y _ { 1 } = y _ { 0 } + h f \left( x _ { 0 } , y _ { 0 } \right) } } \\ { { { } } } \\ { { y _ { i + 1 } = y _ { i - 1 } + 2 h f \left( x _ { i } , y _ { i } \right) \qquad i = 1 , 2 , \ldots , 2 n } } \\ { { { } } } \\ { { { \displaystyle S _ { h } \left( x \right) = \frac { 1 } { 4 } ( y _ { 2 n - 1 } + 2 y _ { 2 n } + y _ { 2 n + 1 } ) } } } \end{array}
$$

possesses an asymptotic expansion in even powers of $h$ and has satisfactory stability properties. This led to the construction of the very powerful G(ragg)-B(ulirsch)-S(toer)-ex trapolation algorithm

Gragg's proof of this property was very long and complicated and it was again "a great achievement" that Stetter had the elegant idea of interpreting (9.13b) as a one-step algorithm by rewriting (9.13） in terms of odd and even indices: for this purpose we define

$$
h ^ { \ast } = 2 h , \quad x _ { k } ^ { \ast } = x _ { 0 } + k h ^ { \ast } , \quad u _ { 0 } = \nu _ { 0 } = y _ { 0 } ,
$$

$$
u _ { k } = y _ { 2 k } \ , \quad v _ { k } = y _ { 2 k + 1 } - h f ( x _ { 2 k } , y _ { 2 k } ) = \frac { 1 } { 2 } ( y _ { 2 k + 1 } + y _ { 2 k - 1 } ) \ .
$$

Then the method (9.13) can be rewritten as (see Figure 9.3)

$$
\begin{array} { r } { \left( \begin{array} { l } { u _ { k + 1 } } \\ { \nu _ { k + 1 } } \end{array} \right) ~ = ~ \left( \begin{array} { l } { u _ { k } } \\ { \nu _ { k } } \end{array} \right) ~ + ~ h ^ { * } \left( \begin{array} { l } { f \left( x _ { k } ^ { * } + \frac { h ^ { * } } { 2 } , \nu _ { k } \right. + \left. \frac { h ^ { * } } { 2 } f \left( x _ { k } ^ { * } , u _ { k } \right) \right) } \\ { \displaystyle \frac { 1 } { 2 } [ f \left( x _ { k } ^ { * } + h ^ { * } , u _ { k + 1 } \right) + f \left( x _ { k } ^ { * } , u _ { k } \right) ] } \end{array} \right) _ { ( \mathbb { Q } ) } . } \end{array}
$$

This method, which maps the pair $( u _ { k } , \nu _ { k } )$ to $( u _ { k + 1 } , \nu _ { k + 1 } )$ ，can be seen from Figure 9.3 to be symmetric. The symmetry can also be checked analytically (see Definition 8.6) by exchanging uk +1 uk, $\nu _ { k + 1 }  \nu _ { k }$ ， $h ^ { * } \longleftrightarrow - h ^ { * }$ $x _ { k } ^ { * } \longleftrightarrow x _ { k } ^ { * } + h ^ { * }$ Atrivial calcuatontheshows that this leaves Formula (9.15) invariant. Method (9.15) is consistent with the differential equation (let $h ^ { * } { } _ {  } \ 0$ in the increment function)

![](images/4c629a55b38db0d08a2a4475ce56f7e5b71d4cda2a6d04cd5ed1b9d4648f35ce.jpg)  
Figure 9.3. Symmetry of the Gragg method

$$
\begin{array} { l l } { { u ^ { \prime } = f \left( x , \nu \right) } } & { { u \left( x _ { 0 } \right) = y _ { 0 } } } \\ { { \qquad } } & { { } } \\ { { \nu ^ { \prime } = f \left( x , u \right) } } & { { \nu \left( x _ { 0 } \right) = y _ { 0 } , } } \end{array}
$$

whose exact solution is simply $u \left( x \right) = \nu \left( x \right) = y \left( x \right) .$ Therefore, we have from Theorem 8.9 that

$$
\begin{array} { l } { { \displaystyle y \left( x \right) - u _ { h ^ { * } } ( x ) = \sum _ { j = 1 } ^ { l } a _ { j } ( x ) { \left( h ^ { * } \right) } ^ { 2 j } + { \left( h ^ { * } \right) } ^ { 2 l + 2 } A \left( x , h ^ { * } \right) } } \\ { { \displaystyle y \left( x \right) - { \nu } _ { h ^ { * } } ( x ) = \sum _ { j = 1 } ^ { l } b _ { j } { \left( x \right) } { \left( h ^ { * } \right) } ^ { 2 j } + { \left( h ^ { * } \right) } ^ { 2 l + 2 } B \left( x , h ^ { * } \right) } } \end{array}
$$

and $a _ { j } ( x _ { 0 } ) = b _ { j } ( x _ { 0 } ) = 0$ . We see from (9.14) that $y _ { h } ( x )$ possesses an expansion in even powers of $h$ , provided that the number of steps is even.

# The smoothing step

"The reader is cautioned against possible instabilities especially in Formulas 25.5.2..." (J.P. Davis and 1. Polansky in Abramowitz-Stegun)

The "explicit midpoint rule" (9.13b), used for the above construction,still suffers from a bad reputation of being "weakly unstable". We shall discuss this property in detail in the introduction to Chapter IV (Volume II). The zig-zag behaviour of the error suggested the idea of replacing $y _ { 2 n }$ by a weighted mean over the three values

$$
S _ { h } ( x _ { 0 } + 2 n h ) = \frac { 1 } { 4 } ( y _ { 2 n - 1 } + 2 y _ { 2 n } + y _ { 2 n + 1 } ) = \frac { 1 } { 2 } ( u _ { n } + \nu _ { n } )
$$

(see (9.13c) and (9.14)). From (9.17) we now have the following result of Gragg:

Theorem 9.2. Let $f \left( x , y \right) \in C ^ { 2 l + 2 }$ then the numerical solution defined in (9.13a,b,c) possesses an asymptotic expansion of the form

$$
y \left( x \right) - S _ { h } ( x ) = \sum _ { j = 1 } ^ { l } e _ { j } ( x ) h ^ { 2 j } + h ^ { 2 l + 2 } C \left( x , h \right)
$$

with $e _ { j } ( x _ { 0 } ) { = } 0 \ a n d \ C \ ( x \ , h \ )$ bounded for $x _ { \mathrm { \scriptsize ~ 0 } } \le x \le x$ and 0≤h≤h0.

Proof: By adding (9.17a) and (9.17b) and using $h ^ { * } { = } 2 h$ we obtain (9.18) with $e _ { j } ( x ) = ( a _ { j } ( x ) + b _ { j } ( x ) ) 2 ^ { 2 j - 1 } ,$ QED.

# Numerical algorithm and example

This method can thus be used for Richardson extrapolation in the same way as symmetric methods above: we choose a step-number sequence, with however the condition that the $n _ { j }$ are even, i.e.

set

$$
T _ { i , 1 } : = S _ { h _ { i } } ( x _ { 0 } + H )
$$

and compute the extrapolated expressions $T _ { i , j }$ ， based on the $h ^ { 2 }$ expansion, by the Aitken-Neville formula (9.12).

Numerical example: We again compute the errors of this algorithm applied to Example (9.11) with step size $H = 0 . 2$ and compare them to the numerical work (which, due to the extra function evaluation for the smoothing step, is $1 + n _ { j } + n _ { j - 1 } + \cdot \cdot \cdot + n _ { j - k + 1 }$ ). The results are plotted in Figure 9.4.

These results are nearly identical to those for the implicit mid-point rule, but much more valuable, since here the method is explicit. For all three sequences， a clear superiority over extrapolated Euler can be observed, especially in the diagonal $T _ { k k }$ for large values of $k$

# Asymptotic expansion for odd indices

For completeness, we still want to derive the existence of an $h ^ { 2 }$ expansion for $y _ { 2 k + 1 }$ from (9.17b), although this is of no practical importance for the numerical algorithm described above.

$$
\begin{array} { l } { { \mathsf { r e m } ~ 9 . 3 . ~ ( \mathrm { G r a g g } ) . ~ F o r ~ x ~ = x _ { 0 } + ( 2 k + 1 ) h ~ w e ~ h a \nu e } } \\ { { y ~ ( x ) - y _ { h } ( x ) = \displaystyle \sum _ { j = 1 } ^ { l } \hat { b } _ { j } ( x ) h ^ { 2 j } + h ^ { 2 l + 2 } \hat { B } ( x , h ) } } \end{array}
$$

![](images/bb4f15a74e52ffe0992b952546708a4179553638c354a2edc9dbcf04dbfebf14.jpg)  
Figure 9.4. Precision of extrapolated Gragg method for Example (9.11)

where the coefficients $\hat { b } _ { j }$ are in general different from those for even indices and $\hat { b } _ { j } ( \boldsymbol { x } _ { 0 } ) \neq 0$

Proof: $y _ { 2 k + 1 }$ can be computed (see Figure 9.3) either from $\nu _ { k }$ by a forward step or from $\nu _ { k + 1 }$ by a backward step. For the sake of symmetry, we take the mean of both expressions and write

$$
y _ { 2 k + 1 } = { \frac { 1 } { 2 } } ( \nu _ { k } + \nu _ { k + 1 } ) + { \frac { h } { 2 } } ( f ( x _ { k } ^ { * } , u _ { k } ) - f ( x _ { k + 1 } , u _ { k + 1 } ) ) .
$$

We now subtract the exact solution and obtain

$$
\begin{array} { l } { { 2 ( y _ { h } ( x ) - y ( x ) ) = \nu _ { 2 h } ( x - h ) \displaystyle - y ( x - h ) } } \\ { { \qquad + \nu _ { 2 h } ( x + h ) \displaystyle - y ( x + h ) + y ( x - h ) \displaystyle - 2 y ( x ) + y ( x + h ) } } \\ { { \qquad + h \left[ f ( x - h , u _ { 2 h } ( x - h ) ) - f \left( x + h , u _ { 2 h } ( x + h ) \right) \right] \ : . } } \end{array}
$$

Due to the symmetry of $u _ { 2 h } ( x ) ( u _ { 2 h } ( \xi ) = u _ { - 2 h } ( \xi ) )$ and of $\nu _ { 2 h } ( x )$

the whole expression becomes symmetric in h. Thus the asymptotic expansion for $y _ { 2 k + 1 }$ contains no odd powers of h QED.

Both expressions, for even and for odd indices,can still be com-bined into a single formula (see Exercise 2).

# Existence of explicit RK methods of arbitrary order

Each of the expressions $T _ { j , k }$ clearly represents an explicit RK. method (see Exercise 1). If we apply the well-known error form ula for polynomial interpolation (see e.g. Abramowitz-Stegun (1964), Formula 25.2.27) to (9.18), we obtain

$$
y \left( x _ { 0 } + H \right) - T _ { j , k } \ = \frac { \left( - 1 \right) ^ { k } } { n _ { j } ^ { 2 } \cdot \cdot \cdot n _ { j - k + 1 } ^ { 2 } } e _ { k } \left( x _ { 0 } + H \right) H ^ { 2 k } + \mathbf { O } ( H ^ { 2 k + 2 } ) .
$$

Since $e _ { k } ( x _ { 0 } ) = 0$ ,we have

$$
y \left( x _ { 0 } + H \right) - T _ { j , k } = { \frac { ( - 1 ) ^ { k } } { n _ { j } ^ { 2 } \cdot \cdot \cdot n _ { j - k + 1 } ^ { 2 } } } e _ { k } ^ { \prime } ( x _ { 0 } ) H ^ { 2 k + 1 } + \mathbf { O } ( H ^ { 2 k + 2 } ) .
$$

This shows that $T _ { j , k }$ represents an ERK method of order $2 k$

As an application of this result we have:

Theorem 9.4. (Gragg). For $p$ even, there exists an explicit RK. method of order p with $s = p ^ { 2 } / 4 + 1$ stages.

Proof: This result is obtained by counting the number of necessary function evaluations of the GBS-algorithms using the harmonic sequence and without the final smoothing step. QED.

Remark: The extrapolated Euler method leads to ERK methods with $\scriptstyle s = p ( p - 1 ) / 2 + 1$ stages. This shows once again the importance of the $h ^ { 2 }$ expansion.

# Order and step size control

Extrapolation methods have the advantage that in addition to the step size also the order (i.e. number of columns) can be changed at each step. Due to this double freedom, the practical implementation in an optimal way is more complicated than for fixed-order RKmethods. The first codes were developed by Bulirsch and Stoer (1966) and their students. Very successful extrapolation codes due to P.Deuflhard and his collaborators are described in Deuflhard (1983).

The choice of the step size can be performed in exactly the same way as for fixed-order embedded methods (see Section II.4). If the first $k$ lines of the extrapolation tableau areomputed,wehave $T _ { k k }$ as the highest-order approximation (of order 2k by (9.22) and in addition $T _ { k , k - 1 }$ of order $2 k - 2$ Itisthereforenaturaltousethe expression

$$
e r r _ { k } \ = \ \parallel \ T _ { k , k - 1 } - T _ { k , k } \ \parallel
$$

for step size control. As in II.4 we get for the optimal step size the formula

$$
H _ { k } \ = H \cdot 0 . 9 4 \cdot \big ( 0 . 6 5 \ t o l / e r r _ { k } \big ) ^ { 1 / \left( 2 k - 1 \right) } \ .
$$

Here the safety factor depends partly on the order.

For the choice of an optimal order we need a measurc of work, which allows us to compare different methods. The work for computing $T _ { k k }$ can be measured by the number $\boldsymbol { A } _ { k }$ of function evaluations. For the GBS-algorithm it is given recursively by

$$
\begin{array} { l } { { A _ { \mathrm { \scriptsize ~ 1 } } = n _ { \mathrm { \scriptsize ~ 1 } } + 1 } } \\ { { { } } } \\ { { A _ { k } = A _ { k - 1 } + n _ { k } \ . } } \end{array}
$$

However, a large num ber of function evaluations can be compensated by a large step size $H _ { k }$ , given by (9.24). We therefore consider

$$
W _ { k } \ = \ { \frac { A _ { k } } { H _ { k } } } \ ,
$$

the work per unit step,as a measure of work. The idea is now to choose the order (i.e. the index $k$ ） in such a way that $W _ { k }$ is minimized.

Let us describe the combined order - and step size control in some more detail. We assume that at some point of integration the stcp size $H$ and the index $k$ $k > 2$ ) are proposed. The step is then realtiontableauadsothealu ized in the following way: we first compute ${ \boldsymbol { H } } _ { k - 2 }$ P $W _ { k - 2 }$ $k - 1$ ， $e r r _ { k - 1 }$ lines of the extrapo- $H _ { k - 1 }$ $w _ { k - 1 }$

a) Convergence in line $k - 1$ If $e r r _ { k - 1 } \leq t o l$ ，we accept $T _ { k - 1 , k - 1 }$ as numerical solution and continue the integration with the new proposed quantities

$$
k _ { n e w } = \left\{ \begin{array} { l l } { k \qquad } & { \mathrm { i f } \forall _ { k - 1 } < 0 . 9 { \cdot } W _ { k - 2 } } \\ { \qquad } & { \mathrm { ~ e l s e ~ } } \end{array} \right.
$$

$$
H _ { n e w } \ = \ \left\{ \begin{array} { l l } { H _ { k _ { n e w } } \quad } & { \mathrm { i f } k _ { n e w } \le k - 1 } \\ { H _ { k - 1 } ( A _ { k } / A _ { k - 1 } ) \quad } & { \mathrm { i f } k _ { n e w } = k . } \end{array} \right.
$$

In (9.27), the only non-trivial formula is the choice of the step size ${ \cal H } _ { n e w }$ inthecascofaordeease $k _ { n e w } = k$ In this case we want to avoid the computation of $e r r _ { k }$ ， so that $H _ { k }$ and $W _ { k }$ are unknown. However, since our $k$ is assumed to be close to the optimal value, we have $\mathcal { N } _ { k } \approx W _ { \xi - 1 }$ which leads to the proposed step size increase.

b) Convergence monitor. If $e r r _ { k - 1 } > t o l$ ， we first decide whether we may expect convergence at least in line $k + 1$ . It follows from (9.22) that, asymptotically,

$$
\parallel T _ { k , k - 2 } - T _ { k , k - 1 } \parallel \approx \left( \frac { n _ { 2 } } { n _ { k } } \right) ^ { 2 } e r r _ { k - 1 }
$$

with $e r r _ { k - 1 }$ given by (9.23). Unfortunately, $e m _ { k }$ cannot be compared with (9.28)， since diferent factors (depending on the differential equation to be solved) are involved in the asymptotic formula (cf. (9.22)). If we nevertheless assume that $e r r _ { k }$ is $( n _ { 2 } / n _ { 1 } ) ^ { 2 }$ times smaller than (9.28) we obtain $e r r _ { k } \approx ( n _ { 1 } / n _ { k } ) ^ { 2 } e r r _ { k - 1 }$ We therefore already reject the step at this point, if

$$
e r r _ { k - 1 } > \ \bigg ( \frac { n _ { k + 1 } n _ { k } } { n _ { 1 } n _ { 1 } } \bigg ) ^ { 2 } \ t o l
$$

and restart with $k _ { n e w } \leq k - 1$ and ${ { \cal H } } _ { n e w }$ according to (9.27).If thecon trary of (9.29) holds, we compute the next line of the extrapolation tableau, i.e. $T _ { k , k } , e r r _ { k } , H _ { k }$ and $W _ { k }$

c) Convergence in line $k$ If $e r r _ { k } \ \leq \ t o l$ ， we accept $T _ { k k }$ as numerical solution and continue the integration with the new proposed values

$$
k _ { n e w \ } = \left\{ { \begin{array} { l l } { k - 1 \quad } & { { \mathrm { i f } } W _ { k - 1 } < 0 . 9 { \cdot } W _ { k } } \\ { k + 1 \quad } & { { \mathrm { i f } } W _ { k } < 0 . 9 { \cdot } W _ { k - 1 } } \\ { _ { k } } & { { \mathrm { i n ~ a l l ~ o t h e r ~ c a s e s } } } \end{array} } \right.
$$

$$
H _ { n e w } \ = \ \left\{ \begin{array} { l l } { H _ { k _ { n e w } } \ } & { \ \mathrm { i f } k _ { n e w } \ \leq \ k } \\ { H _ { k } ( A _ { k + 1 } / A _ { k } ) \ } & { \ \mathrm { i f } k _ { n e w } \ = k + 1 \ . } \end{array} \right.
$$

d) Second convergence monitor. If $e r r _ { k } > t o l$ ， we check, as in b), the relation

$$
e r r _ { k } > \left( \frac { n _ { k + 1 } } { n _ { 1 } } \right) ^ { 2 } t o l .
$$

If (9.31) is satisfied, the step is rejected and we restart with $k _ { n e w } \leq k$ and ${ { \cal H } } _ { n e w }$ of (9.30). Otherwise we continue:

e) $H$ ope for convergence in line $k + 1$ We compute $e r r _ { k \textrm { + j } } , \ H _ { k \textrm { + l } }$ and $W _ { k + 1 }$ If $e r r _ { k + 1 } \leq t o l$ ，we accept $T _ { k + 1 , k + 1 }$ as numerical solution and continue the integration with the new proposed order

$$
\begin{array} { r l } & { k _ { n e w } \ : = k } \\ & { \mathrm { i f } \ ( W _ { k - 1 } < 0 . 9 \cdot W _ { k } ) { k _ { n e w } } \ : = k - 1 } \\ & { \mathrm { i f } \ ( W _ { k + 1 } < 0 . 9 \cdot W _ { k _ { n e w } } ) { k _ { n e w } } \ : = k + 1 \ , } \end{array}
$$

If $e r r _ { k + 1 } > t o l$ the step is rejected and we restart with $k _ { n e w } \leq k$ and $H _ { n e w }$ of (9.24).

The following slight modifications of the above algorithm are recom mended:

i) Storage considerations lead to a limitation of the number of columnsoftheextrapotiontabausayby $k _ { \mathrm { \ m a x } }$ (c.g. $k _ { \operatorname* { m a x } } = 9$ ） For the proposed index $k _ { n e w }$ we require $2 \leq k _ { n e w } \leq k _ { \mathrm { \ m a x } } - 1$ This guarantees that e) may be activated at each step.

ii) After a step-rejection the step size and the order may not be increased.

iii) The norm in (9.23) has to be understood as a scaled norm, e.g. the components of the error can be scaled by the maximal value of $1 0 ^ { - 6 }$ (chosen arbitrarily) and the i-th components of the numerical solution at the beginning and end of the considered interval.

# Numerical study of the combined step size and order control

We show in the following examples how the step size and the order vary for the above algorithm. For this purpose we have written the FORTRAN-subroutine ODEX, which is listed in the appendix.

As a first example we again take the Brusselator (cf. Section I1.4). As in Figures 4.1 and 4.2, the picture at the bottom of Figure 9.5 shows the two components of the solution. In the remaining two pictureswehaveplottedthestepsizes $( H _ { \mathrm { m a x } } { = } 1 . 7 $ and orders for the three tolerances (dotted), (broken line） and (full line). One can easily observe that the extrapolation code automatically chooses a suitable order (depending essentially on tol). The vertical lines indicate step-rejections.

We next study the behaviour of the order control near discon-tinuities. In the example

$$
y ^ { \prime } = - s i g n \left( x \right) \left| 1 - \mid x \right| \mid y ^ { 2 } , \quad y \left( - 2 \right) = { \frac { 2 } { 3 } } , \quad - 2 \leq x \leq 2
$$

![](images/c431883cf519e7636a9f56c8d99aa2a56785a4e79a8ce1fbd6c859e44198bac5.jpg)  
Figure 9.5. Solution, step size and order variation obtained by ODEX

we have a discontinuity in the first derivative of $y \left( x \right)$ at $x = 0$ and two discontinuities in the second derivative (at $x = \pm ~ 1$ ). The numerical results are shown in Figure 9.6. The discontinuities at $x = \pm ~ 1$ are not recognized in the computation with $t o l = 1 0 ^ { - 3 }$ . In all other cases one can see that the order drops to 4 (lowest possible) in the neighbourhood of the discontinuities, so that these points are passed rather efficiently .

# Exercises

1. Show that the extrapolated Euler methods $T _ { 3 , 1 } , T _ { 3 , 2 } , T _ { 3 , 3 }$ (with step-number sequence (9.8)) are equivalent to the Runge-Kutta methods of Table 9.1. Compute also the RK schemes correspond-ing to the first elements of the GBS algorithm.

![](images/32a2e807c0cc2d1edd50a342037074b763baaff31a235b081d032cdca5dd875c.jpg)  
Figure 9.6. Solution, step size and order variation obtained by ODEX at the discontinuous example (9.33)   
Table 9.1. Extrapolation methods as Runge-Kutta methods

<table><tr><td></td><td>T 3,1</td><td> order 1</td><td></td><td>T32</td><td>order 2</td><td></td><td></td><td></td><td>T 3,3 0rder 3</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td></td><td></td><td></td><td></td></tr><tr><td>D</td><td></td><td></td><td></td><td>0 1-2 1-3 2-3</td><td>言</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>N</td><td></td><td></td><td></td><td></td><td>0</td><td></td><td>#</td><td></td><td>0</td><td></td><td></td></tr><tr><td>2</td><td></td><td>1</td><td></td><td></td><td></td><td>0</td><td></td><td></td><td>1-2 1-3 1-3</td><td></td><td>1</td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>13</td><td></td><td></td><td>0</td><td>3</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td><td></td></tr><tr><td></td><td>13</td><td>1</td><td></td><td>0</td><td>-1</td><td>1 1</td><td></td><td>0</td><td>-2</td><td></td><td>32</td></tr></table>

2. Combine (9.17a) and (9.19) into the formula

$$
y \left( x \right) - y _ { k } \ = \ \sum _ { j = 1 } ^ { l } \left[ \alpha _ { j } ( x ) + \left( - 1 \right) ^ { k } \beta _ { j } ( x ) \right] h ^ { 2 j } \ + \ h ^ { 2 l + 2 } E _ { N } ( x \ , \ h )
$$

for thc asymptotic expansion of the Gragg method defined by (9.13a and b).

3. (Stetter (1970)). Prove that for every real $^ { b }$ (generally between 0 and 1) the method

$$
\begin{array} { r l } & { y _ { 1 } = y _ { 0 } + h \left[ b f \left( x _ { 0 } , y _ { 0 } \right) + ( 1 - b ) f \left( x _ { 1 } , y _ { 1 } \right) \right] } \\ & { y _ { i + 1 } = y _ { i - 1 } + h \left[ ( 1 - b ) f \left( x _ { i - 1 } , y _ { i - 1 } \right) + 2 b f \left( x _ { i } , y _ { i } \right) \right. } \\ & { \qquad \left. + ( 1 - b ) f \left( x _ { i + 1 } , y _ { i + 1 } \right) \right] \qquad i = 1 , 2 , \cdots } \end{array}
$$

possesses an expansion in powers of $h ^ { 2 }$ . Prove the same property for the smoothing step

$$
~ ( x ~ ) = { \frac { 1 } { 2 } } \left[ y _ { 2 n } ~ + y _ { 2 n - 1 } + h ( 1 - b ) f ( x _ { 2 n - 1 } , y _ { 2 n - 1 } ) ~ + h b f ( x _ { 2 n } , y _ { 2 n } ) \right]
$$

4. (Steter (1970)). Is the Euler step (9.13a) essential for an $h ^ { 2 }$ expansion? Prove that a first order starting procedure

$$
y _ { 1 } = y _ { 0 } + h \Phi ( x _ { 0 } , y _ { 0 } , h ) 
$$

for (9.13a) produces an ${ \mathrm { \Omega } } _ { h } { \mathrm { \Omega } } ^ { 2 }$ expansionif thequantities $^ { y } - 1 ^ { \mathbf { \alpha } = }$ $y _ { 0 } - h \Phi ( x _ { 0 } , y _ { 0 } , - h ) , y _ { 0 } ,$ and $y _ { 1 }$ satisfy (9.13b) for $\textit { i } = 0$

Hint. Stetter's proof argues on a perturbation of the initial values. A more natural possbility is to replace the Euler steps in (9.15) by the new starting procedure.

5. Solve numerically the differential equation

$$
\begin{array} { l l } { { y ^ { \prime } = z } } & { { y \left( 0 \right) = 3 0 } } \\ { { { z ^ { \prime } } = { 0 . 0 3 2 } { - 0 . 4 z } ^ { 2 } } } & { { z \left( 0 \right) = 0 } } \end{array}
$$

with step sizes $h = 0 . 5$ and $h = 0 . 2 5$ , using the method of Exercise 3 in Section I1.8. Compute the error of the solutions and that of the extrapolated result. Verify numerically the statement of this exercisc.

Remark. The exact solution is

$$
\begin{array} { l } { { y \left( x \right) = 3 0 + 2 . 5 \log ( \cosh ( \sqrt { 0 . 0 1 2 8 } \ x ) ) } } \\ { { z \left( x \right) = \sqrt { 0 . 0 8 } \ \operatorname { t a n h } ( \sqrt { 0 . 0 1 2 8 } \ x ) \ . } } \end{array}
$$

6. Show that the determinant of

$$
\begin{array} { r l r } { A } & { = } & { \left( \begin{array} { l l l l } { 1 } & { a _ { 1 } ^ { p } } & { \cdots } & { a _ { 1 } ^ { p + n - 2 } } \\ { 1 } & { a _ { 2 } ^ { p } } & { \cdots } & { a _ { 2 } ^ { p + n - 2 } } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { 1 } & { a _ { n } ^ { p } } & { \cdots } & { a _ { n } ^ { p + n - 2 } } \end{array} \right) \qquad \mathrm { w i t h } \quad 0 < a _ { 1 } < a _ { 2 } < \cdots < a _ { n } } \end{array}
$$

is strictly positive.

Hint. Subtract Column $n - 1$ multiplied by $\alpha _ { \textup { 1 } }$ from Column n , then $a _ { \textup { 1 } }$ times Column $n - 2$ from Column $n - 1$ etc. Finally subtract $a _ { \uparrow } ^ { p }$ times Column 1 from Column 2. Then take out the positive factors $( a _ { 2 } - a _ { 1 } )$ ， $( a _ { 3 } - a _ { 1 } ) \ , \ . \ . \ , ( a _ { n } - a _ { 1 } )$ and show that the determinant of $A$ is a sum of determinants of similar matrices of lower dimension with positive coefficients.

# I1.10. Numerical comparisons

"The code DIFEX1 seems to be the state of the art in   
extrapolation,   
(L.F. Shampine, L.S. Baca, 1984)

Now is the moment to present some numerical comparisons of the codes described above, ODEX (extrapolation code) and DOPRI8 (method of Dormand and Prince of order 8), both of which are listed in the Appendix. We have found it interesting to include in the tests the well-known extrapolation code DIFEX1 due to Deuflhard (1983). Although this code is based on cxactly the same mathematical method as ODEX, its order strategy differs in many details and is based on an information theoretic model.

From the many examples of differential equations which we have tested, we present the results for the following equations:

JACB: the differential equations of the Jacobian elliptic functions sn, cn, dn (see Abramowitz-Stegun (1964), 16.16):

$$
\begin{array} { c c } { { y _ { 1 } ^ { \prime } = y _ { 2 } y _ { 3 } ~ , } } & { { y _ { 1 } ( 0 ) = 0 } } \\ { { } } & { { } } \\ { { y _ { 2 } ^ { \prime } = - y _ { 1 } y _ { 3 } ~ , } } & { { y _ { 2 } ( 0 ) = 1 } } \\ { { } } & { { } } \\ { { y _ { 3 } ^ { \prime } = - 0 . 5 1 { \cdot } y _ { 1 } y _ { 2 } ~ , } } & { { y _ { 3 } ( 0 ) = 1 } } \\ { { } } & { { } } \\ { { 0 \leq x ~ \leq ~ 2 0 ~ . } } & { { } } \end{array}
$$

TWOB: the equations of the two-body problem:

$$
\begin{array} { c c c } { { y _ { 1 } ^ { \prime } = y _ { 3 } ~ , } } & { { y _ { 1 } ( 0 ) = 0 . 5 } } \\ { { } } & { { } } & { { } } \\ { { y _ { 2 } ^ { \prime } = y _ { 4 } ~ , } } & { { y _ { 2 } ( 0 ) = 0 } } \\ { { } } & { { } } & { { } } \\ { { y _ { 3 } ^ { \prime } = - \displaystyle \frac { y _ { 1 } } { \left( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } \right) ^ { 3 / 2 } } ~ , } } & { { y _ { 3 } ( 0 ) = 0 } } \\ { { } } & { { } } & { { } } \\ { { y _ { 4 } ^ { \prime } = - \displaystyle \frac { y _ { 2 } } { \left( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } \right) ^ { 3 / 2 } } ~ , } } & { { y _ { 4 } ( 0 ) = \sqrt { 3 } } } \\ { { } } & { { } } & { { } } \\ { { 0 \leq x ~ x \leq 2 0 ~ . } } \end{array}
$$

VDPL: Van der Pol's equation (see Section I.16):

$$
\begin{array} { r l r } & { \boldsymbol { y } _ { 1 } ^ { \prime } = \boldsymbol { y } _ { 2 } ~ , \quad } & { \boldsymbol { y } _ { 1 } ( 0 ) = 2 } \\ & { \boldsymbol { y } _ { 2 } ^ { \prime } = ( 1 - \boldsymbol { y } _ { 1 } ^ { 2 } ) \boldsymbol { y } _ { 2 } - \boldsymbol { y } _ { 1 } ~ , \quad \boldsymbol { y } _ { 2 } ( 0 ) = 0 } \\ & { \boldsymbol { 0 } \leq \boldsymbol { x } \leq 2 0 ~ . } \end{array}
$$

BRUS: the Brusselator (see Section I.16):

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = 2 + y _ { 1 } ^ { 2 } y _ { 2 } - 9 . 5 3 3 \cdot y _ { 1 } \ , \quad y _ { 1 } ( 0 ) = 1 } \\ & { y _ { 2 } ^ { \prime } = 8 . 5 3 3 \cdot y _ { 1 } - y _ { 1 } ^ { 2 } y _ { 2 } \ , \qquad y _ { 2 } ( 0 ) = 4 . 2 6 6 5 } \\ & { \quad 0 \leq \ x \leq 2 0 \ . } \end{array}
$$

LAGR: Lagrange's equation for the hanging string (see Equation (6.2) of Section I.6 for $n \ = 1 0 , K \ = 1$ ） Initial values: all $y _ { i } ( 0 ) { = } 0$ except $y _ { 8 } ( 0 ) = 1 ,$ Integration interval $0 \leq x \leq 1 0$

PLEI: a celestial mcchanics problem (which we call "the Pleiades"): seven stars in the plane with coordinates $x _ { i } , y _ { i }$ and masscs $\begin{array} { r } { m _ { i } = i \quad ( i = 1 , \dots , 7 ) } \end{array}$ ：

$$
\begin{array} { l } { { \displaystyle x _ { i } ^ { \prime \prime } = \sum _ { j \neq i } m _ { j } ( x _ { j } - x _ { i } ) / r _ { i j } } } \\ { { \displaystyle y _ { i } ^ { \prime \prime } = \sum _ { j \neq i } m _ { j } ( y _ { j } - y _ { i } ) / r _ { i j } } } \end{array}
$$

where

$$
r _ { i j } = { ( ( x _ { i } - x _ { j } ) ^ { 2 } + ( y _ { i } - y _ { j } ) ^ { 2 } ) ^ { 3 / 2 } } \ , \quad i , j = 1 , \ldots , 7 \ .
$$

Initial values:

$$
\begin{array} { r l } &  x  { 1 } ^ { ( 0 ) = 3 , ~ x  { 2 } ^ { ( 0 ) = 3 , ~ x  { 3 } ^ { ( 0 ) = - 1 , ~ x  { 4 } ^ { ( 0 ) = - 3 , ~ x  { 5 } ^ { ( 0 ) = 2 } } } } } \\ & { x  { 6 } ^ { ( 0 ) = - 2 , ~ x  { 7 } ^ { ( 0 ) = 2 } } , } \\ & { y  { 1 } ^ { ( 0 ) = 3 , ~ y  { 2 } ^ { ( 0 ) = - 3 , ~ y }  { 3 } ^ { ( 0 ) = 2 , ~ y } _ { 4 } ( 0 ) = 0 , ~ y  { 5 } ^ { ( 0 ) = 0 } ~ , } } \\ & { y  { 6 } ^ { ( 0 ) = - 4 , ~ y } _ { 7 } ( 0 ) = 4 , } \\ & { x \textsuperscript { ' } _ { i } ^ { ( ( 0 ) = y } _ { i } ^ { ( 0 ) = 0 } \quad \mathrm { ~ f o r ~ a l l ~ } i \mathrm { ~ w i t h ~ t h e ~ e x c e p t i o n ~ o f ~ } } \\ & { x  { 6 } ^ { \prime } ( 0 ) = 1 . 7 5 , ~ x  { 7 } ^ { ( 0 ) = - 1 . 5 , ~ y } _ { 4 } ^ { \prime } ( 0 ) = - 1 . 2 5 , ~ y  { 5 } ^ { ( 0 ) = 1 } ~ . } \end{array}
$$

Integration interval [0,3].

The exact solutions of these problems are plotted in Figure 10.1 as functions of $x$ . An exception is made for the PLEI-problem, whose solutions are displayed in the phase coordinates.

To give a better idea of the numerical difficulties encountered in problem PLEI, we plot in Figure 10.2 the solutions $x _ { i } , y _ { i }$ as well as the derivatives $x _ { i } ^ { \prime } , y _ { i } ^ { \prime }$ as functions of the independent variable.

![](images/b61cb397db489994ad5d33024b5bf924bea0c6e95af81017406eb1ca6637ba1c.jpg)  
Figure 10.1. Exact solutions of the above six problems

# Numerical results

Each of the above examples was computed with local error tolerances $\mathrm { \Delta } t o l = 1 0 ^ { - 3 }$ ， $\mathrm { j } 0 ^ { - 6 }$ ， $1 0 ^ { - 9 }$ P $1 0 ^ { - 1 2 }$ ,aod $1 0 ^ { - 1 5 }$ WAt the endof the integration interval the computed solution was compared to the exact Solution (which was computed with $t o l = 1 0 ^ { - 2 2 }$ on a CDC computer). As a measure of efficiency， we compare the obtained precision $- \mathrm { l o g } _ { 1 0 } ( \mathrm { ~ } | e r r \mathrm { ~ } | )$ with the number of function calls in double logarithmic scale. The results are presented in Figure 10.3. One can observe that both ex trapolation codes (ODEX and DIFEX1) give nearly equivalent results. The fixed-order code DOPRI8 is clearly superior for tolerances ranging from $1 0 ^ { - 3 }$ to about $1 0 ^ { - 1 2 }$ Only for very stringent toler-ances does the high order of the extrapolation codes begin to show its effects.

![](images/ef9f4606f5c9ddaa79723c1d25e0762fc36a03a6cb396d7914f9fc1ced90022f.jpg)  
Figure 10.2. Exact solutions for PLEI

# A discontinuous example

Our next results are for Equation (9.33) which contains three discontinuities in the integration interval. Here, the obtained accuracy is a question of good luck in how the points of discontinuity fall into the integration steps. We have run this example with very many different tolerances $\mathrm { \Delta } t o l = 1 0 ^ { - 3 - i / 1 0 }$ ， $i = 0 , 1 , \ldots , 9 0 )$ and the obtained errors and number of function evaluations show a quite chaotic behaviour. They are represented for the three diferent codes in Figure 10.4.

It can be observed that DIFEX1 uses approximately twice as many function evaluations as the other two codes. There is a slight advantage for ODEX, due to the order reduction in thc neighbourhood of the points of discontinuity.

![](images/8906dbf6ec7b3c0233bc3c1c8ccbd6820a28e70ff55176c3a4d3a719e5639a00.jpg)  
Figure 10.3. Work-precision diagrams for the above examples

![](images/4c2bf0f78880d09c63d4271e0cac2990aefcfbdf32f658ee79d9b4049c7d8dc4.jpg)  
Figure 10.4. Work-precision diagrams for equation (9.33)

# Conclusion

For smooth problems and tolerances between $1 0 ^ { - 3 }$ and $1 0 ^ { - 1 2 }$ , the fixed-order code DOPRI8 is preferable. The automatic order increase of extrapolation codes makes them superior for very stringent tolerances; the automatic order decrease makes the code ODEX superior in the presence of discontinuities.

# I1.11. Composition of B-series

We shall now derive a central theorem on the composition of what we call B-series (in honour of Butcher)，which will have many applications to more general methods (e.g. multiderivative methods (Section II.12)， Rosenbrock methods,.. (Volume II)） and will also replace the theory of order conditions of Section II.2.

# Composition of RK methods

There is no five-stage ERK method of order 5 (Section II.6). This led Butcher (1969) to the idea of searching for different five-stage methods such that a certain composition of these methods behaves as a fifth-order result ("effective order"). Although not of much practical interest (mainly due to the problem of step size changing), this was the starting point of a fascinating algebraic theory of numerical methods.

Suppose we have two methods, say of three stages,

$$
\frac { \hat { c } _ { 3 } } { \hat { c } _ { 3 } } ~ \left| \begin{array} { c c c c c c c } { \hat { a } _ { 2 1 } } & & & & & { \hat { c } _ { 2 } } \\ { \hat { a } _ { 3 1 } } & { \hat { a } _ { 3 2 } } & & & & { \hat { c } _ { 3 } } \\ { \hat { b } _ { 1 } } & { \hat { b } _ { 2 } } & { \hat { b } _ { 3 } } & & & & { \hat { b } _ { 1 } } \end{array} \right| \begin{array} { c c c c c c } { \hat { a } _ { 2 1 } } & & & & \\ { \hat { a } _ { 3 1 } } & { \hat { a } _ { 3 2 } } & & & \\ { \hat { b } _ { 1 } } & { \tilde { b } _ { 2 } } & { \hat { b } _ { 3 } } & & & \end{array}
$$

which are applied one after the other to a starting value $y _ { 0 }$ with the same step size:

$$
\begin{array} { r l } & { g _ { i } = y _ { 0 } + h \displaystyle \sum _ { j } \hat { a } _ { i j } f \left( g _ { j } \right) \ : , \qquad y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { j } \hat { b } _ { j } f \left( g _ { j } \right) } \\ & { l _ { i } = y _ { 1 } + h \displaystyle \sum _ { j } \hat { a } _ { i j } f \left( l _ { j } \right) \ : , \qquad y _ { 2 } = y _ { 1 } + h \displaystyle \sum _ { j } \hat { b } _ { j } f \left( l _ { j } \right) \ : . } \end{array}
$$

If we insert $y _ { 1 }$ from (11.2) into (11.3) and group all $g _ { i } , l _ { i }$ together, we easily see that the composition can be interpreted as a iarge RK method with coefficients

$$
{ \begin{array} { r l } { { \hat { c } } _ { 2 } } & { } \\ { { \hat { c } } _ { 3 } } \\ { \sum _ { \hat { b } _ { i } } } \\ { \hat { b } _ { i } + { \hat { c } } _ { 2 } } \\ { { \hat { b } } _ { i } + { \hat { c } } _ { 3 } } \\ { { \hat { b } } _ { 1 } \hat { b } _ { 2 } \hat { b } _ { 3 } \hat { b } _ { 3 } \hat { a } _ { 3 1 } } \\ { { \hat { b } } _ { 1 } \hat { b } _ { 2 } \hat { b } _ { 3 } \hat { b } _ { 3 } \hat { b } _ { 3 } } \end{array} } \qquad { \begin{array} { r l } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { c _ { 4 } } \\ { c _ { 5 } } \\ { \hat { a } _ { 3 1 } \hat { b } _ { 2 } } \end{array} } { | \begin{array} { l l l l l l l } { a _ { 2 1 } } & { } & { } & { } & { } & { } & { } & { } \\ { a _ { 3 1 } } & { } & { } & { } & { } & { } & { } & { } \\ { \hat { a } _ { 3 1 } } & { } { a _ { 3 2 } } & { } & { } & { } & { } & { } & { } \\ { \hat { b } _ { 4 } } & { } { \hat { a } _ { 4 2 } } & { } & { } & { } & { } & { } & { } & { } \\ { a _ { 5 1 } } & { } { a _ { 5 2 } } & { a _ { 5 3 } } & { a _ { 5 4 } } & { } & { } & { } & { } \\ { a _ { 6 1 } } & { } { a _ { 6 2 } } & { } & { \hat { a } _ { 6 3 } } & { a _ { 8 3 } } & { a _ { 8 3 } } & { a _ { 8 3 } } \\ { \hat { b } _ { 1 } } & { } & { \hat { b } _ { 2 } } & { } & { \hat { b } _ { 3 } } & { \hat { b } _ { 1 } } & { \hat { b } _ { 2 } } & { } & { \hat { b } _ { 3 } } \end{array} | }  | \begin{array} { l l l l l l } { a _ { 1 2 } } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } & { } \\ { b _ { 1 } } & { } &  \hat { b } _  \end{array}
$$

It is now of interest to study the order conditions of the new method. For this, we have to compute the expressions (see Table 2.1)

$$
\textstyle \sum b _ { i } , \ 2 \sum b _ { i } c _ { i } , \ 3 \sum b _ { i } c _ { i } ^ { 2 } , \ 6 \sum b _ { i } a _ { i j } c _ { j } , \ \mathrm { e t c . }
$$

If we insert the values from the upper tableau of (11.4), a computation,which for low orders is still not too difficult, shows that these expressions can be written in terms of the corresponding expressions for the two methods (11.1). We shall denote these expressions for the first method by $\mathbf { a } ( t )$ , for the second method by $\mathbf { b } ( t )$ , and for the composite method by ab(t) :

$$
\begin{array} { r } { { \bf a } ( \tau ) = \sum \hat { b } _ { i } , \quad { \bf a } ( t _ { 2 1 } ) = 2 { \cdot } \sum \hat { b } _ { i } \hat { c } _ { i } , \quad { \bf a } ( t _ { 3 1 } ) = 3 { \cdot } \sum \hat { b } _ { i } \hat { c } _ { i } ^ { 2 } , \cdot \cdot \cdot } \\ { { \bf b } ( \tau ) = \sum \tilde { b } _ { i } , \quad { \bf b } ( t _ { 2 1 } ) = 2 { \cdot } \sum \tilde { b } _ { i } \tilde { c } _ { i } , \quad { \bf b } ( t _ { 3 1 } ) = 3 { \cdot } \sum \tilde { b } _ { i } \tilde { c } _ { i } ^ { 2 } , \cdot \cdot \cdot } \\ { { \bf a } { \bf b } ( \tau ) = \sum b _ { i } , \quad { \bf a } { \bf b } ( t _ { 2 1 } ) = 2 { \cdot } \sum b _ { i } c _ { i } , \quad { \bf a } { \bf b } ( t _ { 3 1 } ) = 3 { \cdot } \sum b _ { i } c _ { i } ^ { 2 } , \cdot \cdot \cdot } \end{array}
$$

where $\tau , t _ { i j }$ are the trees of Table 2.1. The above mentioned formulas are then

$$
\begin{array} { r l } & { \mathbf { a b } ( \tau ) = \mathbf { a } ( \tau ) + \mathbf { b } ( \tau ) } \\ & { \mathbf { a b } ( t _ { 2 1 } ) = \mathbf { a } ( t _ { 2 1 } ) + 2 \mathbf { b } ( \tau ) \mathbf { a } ( \tau ) + \mathbf { b } ( t _ { 2 1 } ) } \\ & { \mathbf { a b } ( t _ { 3 1 } ) = \mathbf { a } ( t _ { 3 1 } ) + 3 \mathbf { b } ( \tau ) \mathbf { a } ( \tau ) ^ { 2 } + 3 \mathbf { b } ( t _ { 2 1 } ) \mathbf { a } ( \tau ) + \mathbf { b } ( t _ { 3 1 } ) } \\ & { \mathbf { a b } ( t _ { 3 2 } ) = \mathbf { a } ( t _ { 3 2 } ) + 3 \mathbf { b } ( \tau ) \mathbf { a } ( t _ { 2 1 } ) + 3 \mathbf { b } ( t _ { 2 1 } ) \mathbf { a } ( \tau ) + \mathbf { b } ( t _ { 3 2 } ) } \end{array}
$$

etc.

It is now, of course, of interest to have a general understanding of these formulas for arbitrary trees. This, however, is not easy in the above framework (".. a tedious calculation shows that..."). Further, there are problems of identifying different methods with identical numerical results (see Exercise 1 below). Also, we want the theory to include more general processes than Runge-Kutta methods, for example the exact solution or multi-derivative methods.

# B-series

All these difficulties can be avoided if we consider the composition of Taylor series of Section II.2 directly. We define by

$$
T \ = \{ \bigotimes \} \ \cup \ T _ { 1 } \cup \ T _ { 2 } \cup \ \cdots .
$$

the set of all trees, where the "empty" tree $\emptyset$ of order O has been included as well. It represents the initial value and the corresponding elementary differential is the identity map $F ( { \mathcal { O } } ) ( y ) = y .$ Similarly let

$$
L T = \{ \emptyset \} \cup L T _ { 1 } \cup L T _ { 2 } \cup \ \cdots \ .
$$

Definition 11.1. (Hairer-Wanner (1974)). Let a $( \emptyset )$ ,a(t), ${ \mathfrak { a } } ( t _ { 2 1 } )$ ， ${ \mathfrak { a } } ( t _ { 3 1 } ) , \dots$ be a sequence of real coefficients defined for all trees a： $T \to \mathbb { R }$ . Then we call the series (see Theorem 2.11, Definitions 2.2, 2.3)

$$
\begin{array} { l } { { { \bf a } ( \emptyset ) { y } ^ { J } \ + \ h { \bf a } ( \tau ) { f } ^ { J } ( y ) \ + \ \displaystyle \frac { { h } ^ { 2 } } { 2 ! } { \bf a } ( t _ { 2 1 } ) { f } _ { K } ^ { J } ( y ) { f } ^ { K } ( y ) \ + \cdot \cdot \cdot } } \\ { { \ \displaystyle \ = \ \sum _ { t \in L T } \displaystyle \frac { { h } ^ { \mathfrak { p } ( t ) } } { \mathfrak { p } ( t ) ! } { \bf a } ( t ) \ { \cal F } ^ { J } ( t ) ( y ) \ { = : \cal B } ^ { J } ( { \bf a } , y ) } } \end{array}
$$

a B-series.

We have seen in Theorems 2.11 and 2.6 that the numerical solution of an RK method as well as the exact solution are B-series. The coefficients of the latter are all equal to 1.

Usually we are only interested in a finite number of terms of these series (only as high as the orders of the methods under consideration,or as far as $f$ is differentiable) and all subsequent results are valid modulo error terms $\mathbf { O } ( { h ^ { k + 1 } } )$ ·

Definition 11.2. Let $t \in L T$ be a labelled trcc of order $q = \mathsf { \rho } _ { \mathsf { p } } ( { \boldsymbol { \imath } } \mathbf { \rho } _ { t } )$ and $0 \leq i \leq q$ be a fixed integer. Then we denote by $s _ { i } \left( t \right) = s$ the subtree formed by the first i indices and by $d _ { i } ( t )$ (the difference set ) the set of subtrees formed by the indices $i + 1 , \ldots , q$ . In the graphical representation we distinguish the subtree $s$ by fat nodes and doubled lines.

$$
\begin{array} { c c c c c } { { \mathrm { E x a m p l e 1 1 . 3 . } } } & { { } } & { { t = } } & { { \displaystyle { \mathbb { R } } \bigwedge ^ { n } } k } & { { } } \\ { { } } & { { } } & { { } } & { { } } \\ { { i = 0 . } } & { { \displaystyle { \mathbb { R } } \big [ \big . \sum _ { j = 1 } ^ { n } \big ] k } } & { { } } & { { } } & { { s _ { 0 } ( t ) = \emptyset , } } \\ { { } } & { { \displaystyle i = 1 \colon } } & { { \rho _ { \mathrm { \tiny ~ R } } \big [ \big . \sum _ { j = 1 } ^ { n } \big ] k } } & { { } } & { { } } & { { \displaystyle i _ { 1 } = \{ \tau _ { \mathrm { \tiny ~ , ~ } } \tau _ { , \mathrm { \tiny ~ { ~ f ~ } ~ 2 1 } } \} } } \\ { { } } & { { \displaystyle i = 2 . } } & { { \big . \sum _ { j \in \mathcal { Y } } \big [ \big . \sum _ { j = 1 } ^ { n } \big ] k } } & { { } } & { { \displaystyle { \sum _ { j = 1 } ^ { n } \delta _ { j } } s _ { i , j } ( t ) = \tau _ { 2 , 1 } , } } & { { \big . d _ { 2 } = \{ \tau _ { \mathrm { \tiny ~ , ~ } } \tau _ { , \mathrm { \tiny ~ { ~ f ~ } ~ } } \} } } \\ { { } } & { { } } & { { } } & { { } } & { { \big . i = 3 ; } } \\ { { } } & { { \displaystyle i = 4 . } } & { { \big . } } & { { \big [ \big . \sum _ { j = 1 } ^ { n } \delta _ { j } \big ] k } } & { { } } & { { \big [ \int _ { j = 1 } ^ { n } \delta _ { j } ( t ) = i _ { 3 1 } , } } & { { \big . d _ { 4 } = \{ \tau _ { \mathrm { \tiny ~ , ~ f ~ } } \} } } \\ { { } } & { { } } & { { } } & { { } } \\ { { i = 5 ; } } & { { \big . } } &   \big [ \begin{array} { c c c } { { \big . } } & { { \big . } } & { { \big . } } & { { \big . } } \\ { { \big . } } & { { \big . } } & { { \big . } } & { { \big . } } \\ { { \big . } } &   \big [ \begin{array} { c c c }    \end{array} \end{array} \end{array}
$$

"And there was light" (Haydn):

Definition 11.4. Let a $: T  \mathbb { R }$ and b $: T \to \mathbb { R }$ be two sequences of coefficients such that ${ \mathfrak { a } } ( { \mathcal { O } } ) = 1$ . Then for a tree $t$ of order $q = \mathsf { \rho } _ { \mathsf { p } } ( t )$ we define the composition

$$
{ \bf a b } ( t ) = \frac { 1 } { \alpha ( t ) } \sum \bigg [ \sum _ { i = 0 } ^ { q } { \binom { q } { i } } { \bf b } ( s _ { i } ( t ) ) \prod _ { z \in d _ { i } ( t ) } { \bf a } ( z ) \bigg ]
$$

where the first summation is over all $\mathbf { \boldsymbol { a } } \left( t \right)$ different labellings of t (see Definition 2.5).

Example 11:5. It is easily seen that the formulas of (11.6) are special cases of (11.8). The tree $\boldsymbol { \varepsilon }$ of Example 11.3 possesses 6 different labellings. These lead to

$$
\begin{array} { r l r } {  { \mathbf { a b } ( \iota _ { 5 2 } ) = \mathbf { b } ( \mathcal { O } ) \mathbf { a } ( \iota _ { 5 2 } ) + 5 \mathbf { b } ( \tau ) \mathbf { a } ( \tau ) ^ { 2 } \mathbf { a } ( \iota _ { 2 1 } ) } } & { ( 1 1 . 9 ) } \\ & { } & { + \ 1 0 [ \frac { 1 } { 2 } \mathbf { b } ( \iota _ { 2 1 } ) \mathbf { a } ( \tau ) \mathbf { a } ( \iota _ { 2 1 } ) + \frac { 1 } { 2 } \mathbf { b } ( \iota _ { 2 1 } ) \mathbf { a } ( \tau ) ^ { 3 } ] } \\ & { } & { + \ 1 0 [ \frac { 1 } { 6 } \mathbf { b } ( \iota _ { 3 1 } ) \mathbf { a } ( \iota _ { 2 1 } ) + \frac { 4 } { 6 } \mathbf { b } ( \iota _ { 3 1 } ) \mathbf { a } ( \tau ) ^ { 2 } + \frac { 1 } { 6 } \mathbf { b } ( \iota _ { 3 2 } ) \mathbf { a } ( \tau ) ^ { 2 } ] } \\ & { } & { + \ 5 [ \frac { 1 } { 2 } \mathbf { b } ( \iota _ { 4 1 } ) \mathbf { a } ( \tau ) \ + \frac { 1 } { 2 } \mathbf { b } ( \iota _ { 4 2 } ) \mathbf { a } ( \tau ) ] + \mathbf { b } ( \iota _ { 5 2 } ) } \end{array}
$$

where the notation of the trees is that of Table 2.1.

Here is the main theorem of this section:

Theorem 11.6. (Hairer-Wanner (1974)). As above, let a:T - R and b: $T \to \mathbb { R }$ be two sequences of coefficients such that a $i ( \mathcal { O } ) { = } 1$ . Then the composition of the two coresponding $B$ -series is again a $\boldsymbol { B }$ -series

$$
B \left( { \mathfrak { h } } , B \left( { \mathfrak { a } } , y \right) \right) = B \left( { \mathfrak { a } } { \mathfrak { b } } , y \right)
$$

where the "product" ab: $T \to \mathbb { R }$ is that of Definition 11.4.

Proof: We denote the inner series by

$$
B \left( { \mathfrak { a } } , y \right) = g \left( h \right) ~ .
$$

Then the proof is very similar to the development of Section I1.2 (see Figure 2.2)， with the difference that, instead of $f ^ { J } \left( g \right)$ , we now start from

$$
B ( \boldsymbol { \mathsf { b } } , \boldsymbol { g } ) = \sum _ { s \in L T } \frac { \boldsymbol { h } ^ { \mathsf { p } ( s ) } } { \mathsf { p } ( s ) ! } \boldsymbol { \mathsf { b } } ( s ) F ( s ) ( \boldsymbol { g } )
$$

and have to compute the derivatives of this function: let us select the term $s = t _ { 3 2 }$ of this series,

$$
\frac { h ^ { 3 } } { 3 ! } \mathbf { b } ( t _ { 3 2 } ) f _ { L } ^ { K } ( g ) f _ { M } ^ { L } ( g ) f ^ { M } ( g ) .
$$

The $q$ -th derivative of this expression, for $h = 0$ ， is by Leibniz’ formula

$$
{ \binom { q } { 3 } } \ln ( t _ { 3 2 } ) { [ f _ { L } ^ { K } ( g ) f _ { M } ^ { L } ( g ) f ^ { M } ( g ) ] } ^ { ( q - 3 ) } \qquad _ { h } \quad 0 \ ^ { - }
$$

We now compute, as we did in Lem ma 2.8, the derivatives of

$$
f _ { L } ^ { K } ( g ) f _ { M } ^ { L } ( g ) f ^ { M } ( g )
$$

using the classical rules of differential calculus; this gives for the first derivative

$$
f _ { L N } ^ { K } \cdot ( g ^ { \aleph } ) ^ { \prime } f _ { M } ^ { L } f ^ { M } \ + f _ { L } ^ { K } f _ { M N } ^ { L } \cdot ( g ^ { N } ) ^ { \prime } f ^ { M } \ + f _ { L } ^ { K } f _ { M } ^ { L } f _ { N } ^ { M } \cdot ( g ^ { N } ) ^ { \prime }
$$

and so on. We again represent this in graphical form in Figure 11.1.

![](images/e8e65d1f8c3b1202a9588906c4cd825ec227862b72a90ca4b900ebabcceb9904.jpg)  
Figure 11.1. Derivatives of (11.15)

We see that we arrive at trees u of order $q$ such that $s _ { 3 } ( u ) = s$ (where $3 = \rho ( s )$ ） and the elements of $\boldsymbol d _ { 3 } ( \boldsymbol u )$ have no ramifications. The corresponding expressions are similar to (2.6;q-1) in Lemma 2.8. We finally have to insert for the derivativcs of $g$ (see (11.11)） and rearrange the terms. Then，as in Figure 2.3, the tall branches of $d _ { 3 } ( u )$ are replaced by trees $z$ of order δ, multiplied by $\mathbf { a } \left( z \mathbf { \Lambda } \right)$ . Thus the coefficient which wc obtain for a given tree t is just given by (11.8).

The factor $1 / \alpha ( t )$ is due to the fact that in $B$ (ab,y) the term with $\mathbf { a b } ( t ) F ( t )$ appears $\mathbf { \boldsymbol { \alpha } } ( t )$ times. QED.

Since $h f \left( y \right) = B \left( \mathbf { b } , y \right)$ is a special B-series with $\mathbf b ( \tau ) = 1$ and all other $\mathbf b ( t ) = 0$ , we have the following

Corollary 11.7. If a: $T \to$ R with ${ \mathfrak { a } } ( { \mathcal { O } } ) = 1$ then

$$
h f \left( B \left( \mathbf { a } , y \right) \right) = B \left( \mathbf { a } ^ { \prime } , y \right)
$$

with

$$
{ \bf a } ^ { \prime } ( \emptyset ) = 0 \ , \mathrm { ~ \ } { \bf a } ^ { \prime } ( \tau ) = 1
$$

$$
\mathbf { a } ^ { \prime } ( [ t _ { 1 } , \dots , t _ { m } ] ) = \mathsf { p } ( t ) \mathbf { a } ( t _ { 1 } ) \cdot \cdot \cdot \mathbf { a } ( t _ { m } )
$$

where $\boldsymbol { t } = [ t _ { 1 } , \dots , t _ { m } ]$ means that $d _ { 1 } ( t ) = \{ t _ { 1 } , t _ { 2 } , \dots , t _ { m } \}$ (see Definition 2.12).

Proof: We obtain (11.16) from (11.8) with $i = 1 , q = \mathsf { p } ( t )$ and the fact that the expression in brackets is independent of the labelling of t. QED.

# Order conditions for RK methods

As an application of Corollary 11.7,wc demonstratc the deriva-tion of order conditions: we write the RK method (2.3) as

$$
g _ { i } ^ { \phantom { } } = y _ { 0 } ^ { \phantom { } } + \sum _ { j } a _ { i j } ^ { \phantom { } } k _ { j } ^ { \phantom { } } , \qquad k _ { i } ^ { \phantom { } } = h f \left( g _ { i } ^ { \phantom { } } \right) .
$$

If we assume both $\boldsymbol { g } _ { t }$ and $k _ { \mathbf { \Phi } _ { l } }$ to be B-series， whose coefficients we denote by ${ \bf g } _ { i } , { \bf k } _ { i }$

$$
g _ { i } = B \left( \mathbf { g } _ { i } , y _ { 0 } \right) , \qquad k _ { i } = B \left( \mathbf { k } _ { i } , y _ { 0 } \right) ,
$$

then Corollary 11.7 irnmediately allows us to transcribe Formulas (11.17) as

$$
\begin{array} { r l } & { \mathbf { g } _ { i } ( \emptyset ) = 1 \ , \qquad \mathbf { g } _ { i } ( t ) = \sum a _ { i j } \mathbf { k } _ { j } ( t ) \ , } \\ & { \mathbf { k } _ { i } ( \tau ) = 1 \ , \qquad \mathbf { k } _ { i } ( t ) = \boldsymbol { \rho } ( t ) \mathbf { g } _ { i } ( t _ { 1 } ) \cdot \cdot \cdot \mathbf { g } _ { i } ( t _ { m } ) } \end{array}
$$

which leads easily to Formulas (2.17),(2.19) and Theorem 2.11

Also, if we put $y \left( h \right) = B \left( \mathbf { y } , \boldsymbol { y } _ { 0 } \right)$ for the true solution, and compare the derivative $h y ^ { \prime } ( h )$ of the series (11.7) with $h f \left( y \right)$ from Corollary 11.7, we immediately obtain $\mathbf { y } ( t ) = 1$ for all $t$ ， so that Theorem 2.13 drops out.

# Butcher's "effective order"

Once the composition of methods has becn understood, wc search for mcthods a and d, such that da=ed up to order 5, where e is a method of order 5. We still construct methods b and c such that $\mathbf { e _ { \lambda _ { 1 } } d = b }$ and $\mathbf { d c } = \mathbf { e } _ { 2 } .$ ,where $\mathrm { e } _ { 1 }$ and $\mathbf { e } _ { 2 }$ are also of 5th order (see Figure 11.2). The numerical result of $\mathbf { b } \mathbf { a } ^ { k ^ { - 2 } } \mathbf { c }$ then behaves numerically as k steps of a 5-th order method (Figure 11.3). A possible set of coefficients, com puted by Butcher (1969), is given in Table 11.1.

![](images/a92c27e1cd04f949a24c6e065f07e1de9daae7fbf3d55815a833eb7d17b067fd.jpg)  
Figure 11.2.

![](images/669d46c022c29b39703e2bf24afeb5e77e63dbde7d3a14231f64c8d8e4cdb74b.jpg)  
Figure 11.3.   
Table 11.1. Butcher's method of effective order 5 Method a Method

<table><tr><td>0</td><td rowspan="2"></td><td colspan="2">MiCtioua</td><td rowspan="2"></td><td colspan="2"></td><td rowspan="2"></td><td rowspan="2">Metodb</td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td></td><td></td><td></td><td>0 1</td></tr><tr><td>G</td><td>15</td><td></td><td></td><td></td><td>5</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>2</td><td></td><td></td><td></td><td>0</td><td>2</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3</td><td>0</td><td>5 16</td><td></td><td></td><td>3</td><td>75</td><td>9</td><td>117</td><td></td></tr><tr><td>2</td><td>16</td><td></td><td></td><td></td><td></td><td>4</td><td>64</td><td>4</td><td>64</td><td></td></tr><tr><td>1</td><td>1 4</td><td>0</td><td>5 4</td><td>2</td><td></td><td>1</td><td>37</td><td>7</td><td>3</td><td>4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>36</td><td>3</td><td>4</td><td>9</td></tr><tr><td></td><td></td><td></td><td>0</td><td>2</td><td>1</td><td></td><td>19</td><td></td><td>25</td><td></td></tr><tr><td></td><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>2</td><td>1</td></tr><tr><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>144</td><td></td><td>48 9</td><td></td></tr></table>

Method c   

<table><tr><td>0 1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>2</td><td></td><td></td><td></td></tr><tr><td>1</td><td>161</td><td>19</td><td>287</td><td></td><td></td></tr><tr><td>4</td><td>192</td><td>12</td><td>192</td><td></td><td></td></tr><tr><td>1</td><td>27</td><td>19</td><td>291</td><td>36</td><td></td></tr><tr><td></td><td>28</td><td>7</td><td>196</td><td>49</td><td></td></tr><tr><td></td><td>7</td><td></td><td>475</td><td></td><td>7</td></tr><tr><td></td><td>48</td><td>0</td><td>1008</td><td>2</td><td>72</td></tr></table>

# Exercises

1. Show that the pairs of methods given in Tables 11.2 - 11.4 pro-duce, at least for $h$ sufficiently small, identical numerical results.

Result. a) is seen by permutation of the stages, b) by neglecting superfluous stages (Dahlquist-Jeltsch (1979))， c) by identifying equal stages (Stetter (1973)， Hundsdorfer-Spijker (1981)). See also the survey on "The Runge-Kutta space" by Butcher (1984).

2. Extend formulas (11.6) by computing the composition ab(t） for all trees of order 4 and 5.

Table 11.2. Equivalent methods a)   

<table><tr><td>0 1</td><td>0</td><td>1</td><td>0</td><td></td><td>1</td></tr><tr><td rowspan="3"></td><td>1 0</td><td></td><td rowspan="3">0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>3</td><td>3</td><td>1</td></tr><tr><td>4 4</td><td></td><td>4</td><td>4</td></tr></table>

Table 11.3. Equivalent methods b)   

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=4 colspan=1>2   -11    1</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=2>0   1</td><td rowspan=1 colspan=2>2</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=5>0   0   12</td><td rowspan=1 colspan=1>1   1</td></tr></table>

Table 11.4. Equivalent methods c)   

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-2</td><td rowspan=4 colspan=1>3   -22   -3</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=2>2    2</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>-2</td></tr><tr><td rowspan=2 colspan=1>1-1</td><td rowspan=1 colspan=2>-1  -1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>-2              1</td></tr><tr><td rowspan=1 colspan=2>-1   2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-3            -1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>4   4</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>44   4</td></tr></table>

3. Verify that the methods given in Table 11.1 satisfy the stated order properties.

4. Prove that the set

$$
G \ = \{ { \tt a } : T  { \tt R } ; { \tt a } ( \emptyset ) { = } 1 \}
$$

together with the composition law of Definition 11.4 is a (noncommutative) group.

Hint. Use Theorem 11.6.

# I1.12. Higher derivative methods

In Section I.8 we studied the com putation of higher derivatives of solutions of

$$
( y ^ { J } ) ^ { \prime } = f ^ { J } ( x , y ^ { 1 } , \ldots , y ^ { n } ) \ , \qquad J = 1 , \ldots , n .
$$

The chain rule

$$
{ \begin{array} { r l } & { { \mathrm { ~ n ~ r u l e } } } \\ & { ( y ^ { J } ) ^ { \prime \prime } = { \frac { \partial f } { \partial x } } { \big ( } x , y { \big ) } + { \frac { \partial f } { \partial y } } ^ { J } ( x , y ) \cdot f ^ { 1 } ( x , y ) + \cdot \cdot \cdot } \\ & { \qquad + \ { \frac { \partial f ^ { J } } { \partial y ^ { n } } } ( x , y ) \cdot f ^ { n } ( x , y ) } \end{array} }
$$

leads to the differential operator $\mathcal { D }$ which, when applied to a function $\Psi ( x , y ) ,$ is given by

$$
{ \begin{array} { l } { \displaystyle ( D \Psi ) ( x , y ) = { \frac { \partial \Psi } { \partial x } } ( x , y ) + { \frac { \partial \Psi } { \partial y } } ( x , y ) \cdot { f ^ { 1 } } ( x , y ) + \cdot \cdot \cdot } \\ { + \ \qquad { \frac { \partial \Psi } { \partial y ^ { n } } } ( x , y ) \cdot { f ^ { n } } ( x , y ) ~ . } \end{array} }
$$

Since $D y ^ { J } = f ^ { J } ,$ we see by extending (12.2) that

$$
( y ^ { J } ) ^ { ( l ) } = ( D ^ { l } y ^ { J } ) ( x , y ) \qquad l = 0 , 1 , 2 , \cdots .
$$

This notation allows us to define a new class of methods which combine features of Runge-Kutta methods as well as Taylor series methods:

Definition 12.1. Let $a _ { i j } ^ { \left( r \right) }$ $b _ { j } ^ { ( r ) }$ $\left( i , j = 1 , \ldots , s , r = 1 , , \ldots , q , \right.$ be real coefficients. Then the method

$$
\begin{array} { l } { { { k _ { i } } ^ { ( l ) } = \displaystyle \frac { h ^ { l } } { l ! } ( D ^ { l } y ) ( x _ { 0 } { + } c _ { i } h , y _ { 0 } + \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } a _ { i j } ^ { ( r ) } k _ { j } ^ { ( r ) } ) } } \\ { { { } } } \\ { { { y _ { 1 } } = y _ { 0 } + \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } b _ { j } ^ { ( r ) } k _ { j } ^ { ( r ) } } } \end{array}
$$

is called an s-stage q-derivative RK method. If all $a _ { i j } ^ { \left( r \right) }$ are zero for $i \leq j ,$ the method is explicit， otherwisc implicit.

A natural extension of (1.9) is here, because of $D x = 1 , \ D ^ { l } x = 0$ （ $l \geq 2$ ），

$$
c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } ^ { ( 1 ) } \ .
$$

Definition 12.1 is from Kastlunger-Wanner (1972)， but special methods of this type have been considered earlier in the literature. In particular, the very successful methods of Fehlberg (1958, 1964) have this structure.

# Collocation methods

A natural way of obtaining s -stage $q$ -derivative methods is to use the collocation idea with multiple nodes,i.e. to replace (7.18.b) by

$$
{ \bf \Phi } _ { t } ^ { ( l ) } ( x _ { 0 } + c _ { i } h ) = ( D ^ { l } y ) ( x _ { 0 } + c _ { i } h , u ( x _ { 0 } + c _ { i } h ) ) \quad i = 1 , . . . , s , l = 1 , . . . , q _ { i }
$$

where u(x) is a polynomial of degree q1+q2+  +qs and q1, ,s, the "multiplicities" of the nodes $c _ { 1 } , . . . , c _ { s }$ ， are given integers. For example ${ \boldsymbol { q } } _ { 1 } = m$ ， $q _ { 2 } = \cdot \cdot \cdot = q _ { s } = 1$ leads to Fehlberg-type methods.

In order to generalize the results and ideas of Section I.7, we have to replace the Lagrange interpolation of Theorem 7.6 by Hermie interpolation (Hermite (1878): "Je me suis propose de trouver un polynome ..."). The reason is that (12.6) can be interpreted as an ordinary collocation condition with clusters of $\boldsymbol { q } _ { i }$ nodes "infinitely" close together (Rolle's theorem). We write Hermite's formula as

$$
p \left( t \right) = \sum _ { j = 1 } ^ { s } \sum _ { r = 1 } ^ { q _ { j } } \frac { 1 } { r ! } l _ { j r } ( t ) p ^ { ( r - 1 ) } ( c _ { j } )
$$

for polynomials $p \left( t \right)$ of degree $\sum { q _ { j } - 1 }$ . Here the "basis" polynomials $l _ { j r } ( t )$ of degree ${ \sum q _ { j } - 1 }$ must satisfy

$$
l _ { j r } ^ { ( k ) } ( c _ { i } ) = \left\{ { \begin{array} { l l } { r ! \qquad } & { \mathrm { i f } i = j \mathrm { a n d } k = r - 1 } \\ { 0 } & { \mathrm { e l s e } } \end{array} } \right.
$$

and are best obtained from Newton's interpolation formula (with multiple nodes). We now use this formula, as we did in Section I.7, for $p \left( t \right) = h \boldsymbol { u } ^ { \prime } ( \boldsymbol { x } _ { 0 } + t h )$ ：

$$
h u ^ { \prime } ( x _ { 0 } { + } t h ) = \sum _ { j = 1 } ^ { s } \sum _ { r = 1 } ^ { q _ { j } } l _ { j r } ( t ) k _ { j } ^ { ( r ) } ,
$$

with

$$
k _ { j } ^ { \ : ( r ) } = \frac { h ^ { r } } { r ! } u ^ { ( r ) } ( x _ { 0 } { ^ { + } } c _ { j } h ) .
$$

If we insert

$$
u \left( x _ { 0 } + c _ { i } h \right) = y _ { 0 } + \intop _ { 0 } ^ { c _ { i } } h u ^ { \prime } ( x _ { 0 } + t h ) d t
$$

together with (12.9) into (12.6), we see that:

Theorem 12.2. The collocation method (12.6) is equivalent to an sstage q-derivative IRK method (12.4) with

$$
\alpha _ { i j } ^ { ( r ) } = \int _ { 0 } ^ { c _ { i } } l _ { j r } ^ { } ( t ) d t \ , b _ { j } ^ { ( r ) } = \int _ { 0 } ^ { 1 } l _ { j r } ^ { } ( t ) d t .
$$

QED.

Theorems 7.7, 7.8, and 7.9 now generalize immediately to the case of "confluent" quadrature formulas; i.e. the $q$ -derivative RK method possesses the same order as the underlying quadrature formula

$$
\begin{array} { r } { \displaystyle { \int _ { 0 } ^ { 1 } p ( t ) d t } \approx \sum _ { j = 1 } ^ { s } { \sum _ { r = 1 } ^ { q _ { j } } { b _ { j } ^ { ( r ) } p ^ { ( r - 1 ) } ( c _ { j } ) } } . } \\ { 0 } \end{array}
$$

The "algebraic" proof of this result (see Exercise 7 of Section II.7) is more complicated and is given， for the case $q _ { j } = q$ ， in Kastlunger-Wanner (1972b).

Thus, the formulas corresponding to (7.12) are given by

$$
\sum _ { j = 1 } ^ { s } \sum _ { r = 1 } ^ { q _ { j } } { \alpha _ { i j } ^ { \left( r \right) } \left( { { \binom { \rho } { r } } } \right) c _ { j } ^ { \rho - r } } = c _ { i } ^ { \rho } \qquad { \mathrm { ~ \rho \rho = 1 , ~ 2 ~ , ~ \ldots , ~ \sum { q _ { i } } ~ } } .
$$

These equations uniquely determine the $a _ { i j } ^ { \left( r \right) }$ , once the $c _ { i }$ have been chosen, by a linear system with a "confluent" Vandermonde matrix (see e.g. Gautschi (1962)). Formula (12.12) is obtained by setting $p \left( t \right) = t ^ { \rho - 1 }$ in (12.7) and then integrating from 0 to $c _ { i }$ ·

Examples of methods: "Gaussian" quadrature formulas with multiple nodes exist for odd $q$ (Stroud-Stancu (1965)) and extend to $q \cdot$ derivative IRK methods (Kastlunger-Wanner(1972b)): for $s = 1$ we have, of course, $c _ { 1 } { = } 1 / 2$ which yields

$$
b _ { 1 } ^ { ~ ( 2 k ) } ~ = 0 ~ , ~ b _ { 1 } ^ { ~ ( 2 k + 1 ) } ~ = 2 ^ { - 2 k } ~ , ~ a _ { 1 1 } ^ { ~ ( k ) } ~ = - { ( - 1 ) } ^ { k } 2 ^ { - k } ~ .
$$

We give also the coefficients for the case $s = 2$ and ${ q _ { 1 } } ^ { \mathrm { ~ } } { = } { q _ { 2 } } ^ { \mathrm { ~ } } { = } 3$ . The nodes $c _ { i }$ and the weights ${ b _ { i } } ^ { ( k ) }$ are those of Stroud-Stancu. The method is of order 8:

$$
\begin{array} { l l } { { c _ { 1 } = 0 . 1 8 5 3 9 4 4 3 5 8 2 5 0 4 5 } } & { { c _ { 2 } = 1 - c _ { 1 } } } \\ { { b _ { 1 } ^ { ( 1 ) } = 0 . 5 } } & { { b _ { 2 } ^ { ( 1 ) } = b _ { 1 } ^ { ( 1 ) } } } \\ { { b _ { 1 } ^ { ( 2 ) } / 2 ! = 0 . 0 2 4 0 7 2 9 4 2 0 8 4 4 9 7 4 } } & { { b _ { 2 } ^ { ( 2 ) } = - b _ { 1 } ^ { ( 2 ) } } } \\ { { b _ { 1 } ^ { ( 3 ) } / 3 ! = 0 . 0 0 3 6 6 2 6 4 9 6 0 6 7 1 7 2 7 } } & { { b _ { 2 } ^ { ( 3 ) } = b _ { 1 } ^ { ( 3 ) } } } \end{array}
$$

$$
\begin{array}{c} { \left( a _ { i k } ^ { \left( 2 \right) } \right) } = { \left( \begin{array} { l l } { 0 . 2 0 1 8 5 4 1 1 5 8 3 1 0 0 5 } & { - 0 . 0 1 6 4 5 9 6 8 0 0 0 5 9 5 9 8 } \\ { 0 . 5 1 6 4 5 9 6 8 0 0 0 5 9 5 9 } & { 0 . 2 9 8 1 4 5 8 8 4 1 6 8 9 9 4 } \end{array} \right) }  \\ { { \left( a _ { i k } ^ { \left( 2 \right) } \right) } = { \left( \begin{array} { l l } { - 0 . 0 2 2 3 4 6 6 5 6 9 0 8 0 5 4 1 } & { 0 . 0 0 8 6 8 8 7 8 7 7 3 0 8 2 4 1 7 } \\ { 0 . 0 5 6 8 3 4 6 7 1 8 9 9 8 1 9 0 } & { - 0 . 0 7 0 4 9 2 5 4 1 0 7 7 0 4 9 0 } \end{array} \right) } } \\ { { \left( a _ { i k } ^ { \left( 3 \right) } \right) } = { \left( \begin{array} { l l } { 0 . 0 1 1 6 7 3 9 6 6 8 4 0 0 9 9 7 } & { - 0 . 0 0 2 1 5 3 5 1 2 5 1 0 6 5 7 8 4 } \\ { 0 . 0 2 4 1 2 9 4 1 0 1 5 0 9 6 1 5 } & { 0 . 0 1 0 3 0 1 9 3 0 8 0 2 0 3 9 } \end{array} \right) } } \end{array}
$$

# Obreschk off methods

We now consider the special case of collocation methods with $s = 2 , \ c _ { 1 } = 0 , \ c _ { 2 } = 1$ . These methods are called Obreschkoff methods and their coefficients can be obtained in closed form by repeated partial integration as follows (Nbrsett (1974a):

Lemma 12.3. Let m be a given positive integer and $F \left( t \right)$ a polyno-mial of exact degree $m$ . Then

$$
\sum _ { j = 0 } ^ { m } h ^ { \ j } ( D ^ { \ j } y ) ( x _ { 1 } , y _ { 1 } ) F ^ { ( m - j ) } ( 0 ) \ = \ \sum _ { j = 0 } ^ { m } h ^ { \ j } ( D ^ { \ j } y ) ( x _ { 0 } , y _ { 0 } ) F ^ { ( m - j ) } ( 0 ) \ = \ \sum _ { j = 0 } ^ { m } h ^ { \ j } ( D ^ { \ j } y ) ( x _ { 0 } , y _ { 1 } ) \ = \ 1 ,
$$

defines a multiderivative method of order $^ m$

Proof: We let $y \left( x \right)$ be the exact solution and start from

$$
h ^ { m + 1 } { \int _ { 0 } ^ { 1 } y ^ { ( m + 1 ) } ( x _ { 0 } { + } h t ) F ( 1 { - } t ) d t } = 0 ( h ^ { m + 1 } ) \ .
$$

This integral is now transformed by repeated partial integration until all derivatives of the polynomial $F \left( 1 - t \right)$ are used up. This leads to

$$
\sum _ { = 0 } ^ { m } h ^ { j } y ^ { ( j ) } ( x _ { 1 } ) F ^ { ( m - j ) } ( 0 ) = \sum _ { j = 0 } ^ { m } h ^ { j } y ^ { ( j ) } ( x _ { 0 } ) F ^ { ( m - j ) } ( 1 ) + { \bf O } ( h ^ { m + 1 } ) .
$$

If this is subtracted from (12.13) we find the difference of the lefthand sides to be $\mathbf { O } ( h ^ { m + 1 } )$ ， which shows by the implicit function theorem that (12.13) determines $y _ { 1 }$ to this order if $\boldsymbol { F } ^ { ( \hat { m } ) }$ ， which is a constant, is $\neq 0$ . QED.

Remark: The argument $1 - t$ in $F$ (instead of the more natural t) has been chosen here to avoid the sign changes which would otherwise appear.

A good choice for $F \left( t \right)$ is,of course, a polynomial for which most derivatives disappear at $\scriptstyle t = 0$ and $t = 1$ .Then the method (12.13)

is, by keeping the same order $m$ , most economical. We write

$$
F ( t ) = \frac { t ^ { k } ( t - 1 ) ^ { l } } { ( k + l ) ! }
$$

and obtain methods which are generally called Obreschkoff methods

$$
\begin{array} { c } { { y _ { 1 } - \displaystyle \frac { l } { k + l } \frac { h } { 1 ! } ( D y ) ( x _ { 1 } , y _ { 1 } ) + \displaystyle \frac { l ( l - 1 ) } { ( k + l ) ( k + l - 1 ) } \frac { h ^ { 2 } } { 2 ! } ( D ^ { 2 } y ) ( x _ { 1 } , y _ { 1 } ) \pm \cdot \cdot \cdot . . } } \\ { { y _ { 0 } + \displaystyle \frac { k } { ( k + l ) } \frac { h } { 1 ! } ( D y ) ( x _ { 0 } , y _ { 0 } ) + \displaystyle \frac { k ( k - 1 ) } { ( k + l ) ( k + l - 1 ) } \frac { h ^ { 2 } } { 2 ! } ( D ^ { 2 } y ) ( x _ { 0 } , y _ { 0 } ) + \cdot \nonumber } } \end{array}
$$

of order $m = k + i$ Aftcr the l-th term in the first line and the $k$ -th term in the second line, the coefficients automatically bccome zero. Special cases of this method are:

$$
\begin{array} { r l r l } { k = 1 , } & { { } } & { l = 0 ; } & { { } \mathrm { ~ e x p l i c i t ~ E u l e r ~ } } \\ { k = 0 , } & { { } } & { l = 1 ; } & { { } \mathrm { ~ i m p l i c i t ~ E u l e r ~ } } \\ { k = 1 , } & { { } } & { l = 1 ; } & { { } \mathrm { ~ t r a p e z o i d a l ~ r u l e r ~ } } \end{array}
$$

# Fehlberg methods

Another class of multiderivative methods is due to Fehlberg (1958,1964): the idea is to subtract from the solution of $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 } m$ terms of the Taylor series (see Section I.8)

$$
\hat { y } \left( x \right) : = y \left( x \right) - \sum _ { i = 0 } ^ { m } Y _ { i } \left( x - x _ { 0 } \right) ^ { i } ,
$$

and to solve the resulting differential equation $\hat { y } ^ { \prime } ( x ) { = } \hat { f } \left( x \mathrm { ~ , ~ } \hat { y } \left( x \mathrm { ~ } \right) \right)$ ， where

$$
\hat { f } \left( \boldsymbol { x } , \hat { y } \left( \boldsymbol { x } \right) \right) = f \left( \boldsymbol { x } , \hat { y } + \sum _ { i = 0 } ^ { m } Y _ { i } \left( \boldsymbol { x } - \boldsymbol { x } _ { 0 } \right) ^ { i } \right) - \sum _ { i = 1 } ^ { m } Y _ { i } \boldsymbol { i } \left( \boldsymbol { x } - \boldsymbol { x } _ { 0 } \right) ^ { i - 1 } ( 1 - \boldsymbol { x } _ { 0 } ) ^ { i } ,
$$

by a Runge-Kutta method. Thus, knowing that the solution of (12.16) and its first $m$ derivatives are zero at the initial value, we can achieve much higher orders.

In order to understand this, we develop the Taylor series of the solution for the non-autonomous case, as we did in Section I.1. We thereby omit the hats and suppose the transformation (12.15） done before. We then have from (1.6) (see also Excrcise 3 of Section I1.2)

$$
\begin{array} { r l } & { f = 0 \ , } \\ & { f _ { x } \ + f _ { y } f \ = 0 \ , } \\ & { f _ { x x } \ + 2 f _ { x y } f \ + f _ { y y } f ^ { 2 } + f _ { y } ( f _ { x } + f _ { y } f ) = 0 \ , \mathrm { e t c . } } \end{array}
$$

These formulas implyrecursivelythat $f = 0 , \quad f _ { x } = 0$ $\partial ^ { m - 1 } f / \partial x ^ { m - 1 } = 0$ All elementary differentialsof order $\leq m$ and most of those of higher orders then become zero and the corresponding order conditions can be omitted. The first non-zero terms are

$$
\begin{array} { r l r } & { \frac { \partial ^ { m } f } { \partial x ^ { m } } , \qquad } & { \mathrm { f o r ~ o r d e r } \quad m + 1 , } \\ & { \frac { \partial ^ { m + 1 } f } { \partial x ^ { m + 1 } } \quad \mathrm { a n d } \quad f _ { y } \cdot \frac { \partial ^ { m } f } { \partial x ^ { m } } \qquad \mathrm { f o r ~ o r d e r } \quad m + 2 , } \end{array}
$$

and so on. The corresponding order conditions are then

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { m } = \frac { 1 } { m + 1 }
$$

for order $m + 1$ ，

$$
\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { m + 1 } = \frac { 1 } { m + 2 } \mathrm { a n d } \sum _ { i , j } b _ { i } a _ { i j } c _ { j } ^ { m } = \frac { 1 } { ( m + 1 ) ( m + 2 ) }
$$

for order $m + 2$ , and so on.

The condition $\scriptstyle \sum a _ { i j } = c _ { i }$ ， which usually allows several terms of (1.6) to be grouped together, is not necessary, because all these othcr terms are zero.

A complete insight is obtained by considering the method as being partitioned applied to the partitioned system $y ^ { \prime } { = } f \left( x , y \right) , \ x ^ { \prime } { = } 1$ This will be expiained in Section I.14 (see Figure 14.4).

Example 12.4. A solution of the (four) conditions with 3 stages for order $m + 3$ is given by Fehlberg (1964). The choice ${ \boldsymbol { c } } _ { 1 } = { \boldsymbol { c } } _ { 3 } = 1$ minimizes the numerical work for the evaluation of (12.16) and the other coefficients are then uniquely determined (see Table 12.1).

Fehlberg (1964) also derived an embedded method with two additional stages of orders $m + 3 \quad ( m + 4 )$ . These methods were widely used in the six ties for scientific computations.

$$
{ \begin{array} { r l } & { { \mathrm { T a b l e ~ 1 2 . 1 . ~ F e h l b e r g , ~ o r d e r ~ } } m + 3 } \\ { 1 } \\ { \vartheta } \\ { 1 } \\ { \displaystyle } & { { \frac { 1 } { m + 1 } } \frac { \vartheta } { m + 1 } \frac { \vartheta } { ( m + 1 ) ( m + 2 ) 2 \vartheta ^ { m } } \qquad \frac { 1 } { 2 m + 4 } } \end{array} }
$$

# General theory of order conditions

For the same reason as in Section II.2 we assume that (12.1) is autonomous. The general form of the order conditions for Method (12.4) was derived in the thesis of Kastlunger (see Kastlunger-Wanner (1972)). It later became a simple application of the composition theorem for B-series (Hairer-Wanner (1974)). The point is that from Theorem 2.6,

$$
{ \frac { h ^ { i } } { i ! } } ( D ^ { i } y ) ( y _ { 0 } ) = \sum _ { t \in L T , \rho ( t ) = i } { \frac { h ^ { i } } { i ! } } F ( t ) ( y _ { 0 } ) = B \left( \delta _ { i } , y _ { 0 } \right)
$$

is a B-series with coefficients

$$
\begin{array} { r } { \mathfrak { d } _ { i } ( t ) = \left\{ \begin{array} { l l } { 1 \quad } & { \mathrm { i f } \quad \rho ( t ) = i } \\ { 0 \quad } & { \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array}
$$

Thus, in extension of Corollary 11.7, we have

$$
\frac { { h ^ { i } } } { i ! } ( { D ^ { i } } _ { y } ) ( B ( { \bf a } , { y } _ { 0 } ) ) = B ( { \bf a } ^ { ( i ) } , { y } _ { 0 } )
$$

where from Formula (11.8) with $q = _ { \rho } ( t )$ 、

$$
{ \bf a } ^ { ( i ) } ( t ) = { \frac { 1 } { \alpha ( t ) } } \left( { \boldsymbol q } ^  \} \right) \sum _ { z \in d _ { i } ( t ) } { \underline { { \bf \Pi } } } { \bf a } ( z ) \ ,
$$

and the sum is over all $\alpha ( t )$ different labellings of t. This allows us to compute recursively the coefficients of the B-series which appear in (12.4).

Example 12.5. The tree $t _ { 4 2 }$ sketched in Figure 12.1 possesses three different labelings, two of which produce the same difference set $\boldsymbol { d } _ { 2 } ( t )$ , so that Formula (12.20) becomes

$$
{ \bf a } ^ { \prime \prime } ( t _ { 4 2 } ) = 2 { \left( 2 ( { \bf a } ( \tau ) { \bf ) } ^ { 2 } + { \bf a } ( t _ { 2 1 } ) \right) } \ .
$$

For all other trees of order $\leq 4$ we have $\textstyle \alpha ( t ) = 1$ and (12.20) leads to the following table of second derivatives (in the notation of Table 2.1)

![](images/5ca038d231be9aaef04b7bf7bfe491fc0c73c0c45741f397fa79dcfad369fec8.jpg)  
Figure 12.1. Different labellings of t 42

$$
\begin{array} { r l } & { \mathbf { a } ^ { \prime \prime } ( \tau ) = 0 } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 2 1 } ) = 1 } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 3 1 } ) = 3 \mathbf { a } ( \tau ) } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 3 2 } ) = 3 \mathbf { a } ( \tau ) } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 4 1 } ) = 6 \mathbf { ( a } ( \tau ) ) ^ { 2 } } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 4 2 } ) = 4 ( \mathbf { a } ( \tau ) ) ^ { 2 } + 2 \mathbf { a } ( t _ { 2 1 } ) } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 4 3 } ) = 6 \mathbf { ( a } ( \tau ) ) ^ { 2 } } \\ & { \mathbf { a } ^ { \prime \prime } ( t _ { 4 4 } ) = 6 \mathbf { a } ( t _ { 2 1 } ) \ . } \end{array}
$$

Once these expressions have been established, we write Formulas (12.4) in the form

$$
\begin{array} { c } { { \displaystyle { k _ { i } ^ { ( l ) } = \frac { h ^ { l } } { l ! } ( D ^ { l } y ) ( g _ { i } ) } } } \\ { { \displaystyle { g _ { i } = y _ { 0 } + \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } a _ { i j } ^ { ( r ) } k _ { j } ^ { ( r ) } } } } \\ { { \displaystyle { y _ { 1 } = y _ { 0 } + \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } b _ { j } ^ { ( r ) } k _ { j } ^ { ( r ) } } } } \end{array}
$$

and suppose the expressions $k _ { i } ^ { \left( l \right) }$ ， $g _ { i } , y _ { 1 }$ to be B-series

$$
k _ { i } ^ { ( l ) } = B \left( \mathbf { k } _ { i } ^ { ( l ) } , y _ { 0 } \right) , \quad g _ { i } = B \left( \mathbf { g } _ { i } , y _ { 0 } \right) , \quad y _ { 1 } = B \left( \mathbf { y } _ { 1 } , y _ { 0 } \right) .
$$

The coeficients of these series are then recursively determined from

$$
\begin{array} { r l } & { \mathbf { k } _ { i } ^ { ( 1 ) } ( t ) = \mathsf { p } ( t ) \mathbf { g } _ { i } ( t _ { 1 } ) \cdot \cdot \cdot \cdot \mathbf { g } _ { i } ( t _ { m } ) \ , \quad \mathbf { k } _ { i } ^ { ( 1 ) } ( \tau ) = 1 \qquad \mathsf { ( s e e } } \\ & { \mathbf { k } _ { i } ^ { ( 2 ) } ( t ) = \mathbf { g } _ { i } ^ { \prime \prime } ( t ) \qquad \mathsf { f r o m } \ ( 1 2 . 2 2 ) } \\ & { \mathbf { k } _ { i } ^ { ( 3 ) } ( t ) = \mathbf { g } _ { i } ^ { \prime \prime \prime } ( t ) \qquad \mathsf { f r o m \ E x e r c i s e \ 1 \ o r \ E x e r c i s e \ 2 , \ e t c } } \\ & { \mathbf { g } _ { i } ( t ) = \displaystyle \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } \alpha _ { i j } ^ { ( r ) } \mathbf { k } _ { j } ^ { ( r ) } ( t ) } \end{array}
$$

and finally

$$
{ \bf y } _ { 1 } ( t ) = \sum _ { r = 1 } ^ { q } \sum _ { j = 1 } ^ { s } b _ { j } ^ { ( r ) } { \bf k } _ { j } ^ { ( r ) } ( t ) \ .
$$

If the method (12.4) satisfies (12.5), then it is of order $p$ if, as usual,

$$
\begin{array} { r } { \mathbf { y } _ { 1 } ( t ) ~ { = } ~ 1 ~ \mathrm { ~ f o r ~ a l l ~ } t ~ \mathrm { w i t h ~ } \mathsf { p } ( t ) { \leq } p ~ . } \end{array}
$$

More details and special methods are given in Kastlunger-Wanner (1972); see also Exercise 3.

# Exercises

1. Extend Example 12.5 and obtain formulas for $\mathsf { a } ^ { ( 3 ) } ( t )$ for all trees of order $\leq 4$

2. (Kastlunger). Prove the following variant form of Formula (12.20) which extends (11.17') morc dircctly and can also be used to obtain the formulas of Exam plc 12.5

$$
\mathbf { a } ^ { ( i ) } ( t ) = { \frac { \operatorname { \mathrm {  ~ \ p } } ( t ) } { i } } \sum _ { \lambda _ { 1 } + \cdots + \lambda _ { m } = i - 1 } \mathbf { a } ^ { ( \lambda _ { 1 } ) } ( t _ { 1 } ) \cdots { \dot { \mathbf { \sigma } } } ^ { ( \lambda _ { m } ) } ( t _ { m } )
$$

if $t = [ i _ { 1 } , \dots , i _ { m } ]$

Hint: see Hairer-Wanner (1973), Section 5.

3. Show that the conditions for order 3 of Method (12.4) are given by

$$
\begin{array} { c } { { \sum b _ { i } ^ { \left( 1 \right) } = 1 } } \\ { { { } _ { i } } } \\ { { 2 \sum b _ { i } ^ { \left( 1 \right) } c _ { i } + \sum b _ { i } ^ { \left( 2 \right) } = 1 } } \\ { { { } _ { i } } } \\ { { 3 \sum b _ { i } ^ { \left( 1 \right) } c _ { i } ^ { 2 } + 3 \sum b _ { i } ^ { \left( 2 \right) } c _ { i } = 1 } } \\ { { { } _ { i } } } \\ { { { \sum { b _ { i } } ^ { \left( 1 \right) } a _ { i j } ^ { \left( 1 \right) } c _ { j } + 3 \sum b _ { i } ^ { \left( 1 \right) } e _ { i } + 3 \sum b _ { i } ^ { \left( 2 \right) } c _ { i } = 1 \ , } } } \end{array}
$$

where

$$
c _ { i } ^ { \phantom { } } = \sum _ { j } ^ { } a _ { i j } ^ { \phantom { } ( 1 ) } , \qquad e _ { i } ^ { \phantom { } } = \sum _ { j } ^ { } a _ { i j } ^ { \phantom { } ( 2 ) } .
$$

4. (Zurmuhl (1952)， Albrccht (1955)). Differentiate a given first order system of differential equations $y ^ { \prime } { = } f \left( x \ , y \right)$ to obtain

$$
y ^ { \prime \prime } = ( D ^ { 2 } y ) ( x , y ) ~ , ~ y ( x _ { 0 } ) = y _ { 0 } ~ , ~ y ^ { \prime } ( x _ { 0 } ) = f _ { 0 } ~ .
$$

Apply to this equation a special method for higher order systems (see the following Section I1.13) to obtain higher-derivative methods. Show that the following method is of order six

$$
\begin{array} { l } { { k _ { 1 } = h ^ { 2 } g ( x _ { 0 } , y _ { 0 } ) } } \\ { { k _ { 2 } = h ^ { 2 } g ( x _ { 0 } + \frac { h } { 4 } , y _ { 0 } + \frac { h } { 4 } f _ { 0 } + \frac { 1 } { 3 2 } k _ { 1 } ) } } \end{array}
$$

$$
\begin{array} { l } { { { k _ { 3 } } = { h ^ { 2 } g ( x _ { 0 } + { \frac { h } { 2 } } , y _ { 0 } + { \frac { h } { 2 } } f _ { 0 } + { \frac { 1 } { 2 4 } } ( - k _ { 1 } + 4 k _ { 2 } ) ) } } } \\  { { k _ { 4 } } = { h ^ { 2 } g ( x _ { 0 } + { \frac { 3 h } { 4 } } , y _ { 0 } + { \frac { 3 h } { 4 } } f _ { 0 } + { \frac { 1 } { 3 2 } } ( 3 k _ { 1 } + 4 k _ { 2 } + 2 k _ { 3 } ) ) } } \\ { { { y _ { 1 } } = y _ { 0 } + h f _ { 0 } + { \frac { 1 } { 9 0 } } ( 7 k _ { 1 } + 2 4 k _ { 2 } + 6 k _ { 3 } + 8 k _ { 4 } ) } } \end{array}
$$

where

$$
( x , y ) = ( D ^ { 2 } y ) ( x , y ) = D f ( x , y ) = f _ { x } ( x , y ) + f _ { y } ( x , y ) \cdot f ( x , y ) ,
$$

# I1.13. Numerical methods for second order differential equations

"Mutationem motus proportionalem esse vi motrici   
impressae"   
(Newton, 1687)

Many differential equations which appear in practice are systems of the second order

$$
y ^ { \prime \prime } = f \left( x , y , y ^ { \prime } \right) .
$$

This is mainly due to the fact that the forces are proportional to acceleration, i.e. to second derivatives. As mentioned in Section I.1, such a system can be transformed into a first order differential equation of doubled dimension by considering the vector $( y , y )$ as the new variable:

$$
{ \binom { y } { y ^ { \prime } } } ^ { \prime } = \begin{array} { l } { { \left( { y ^ { \prime } } \right. } } \\ { { f \left( x , y , y ^ { \prime } \right) } } \end{array} \qquad \begin{array} { l } { { y \left( x _ { 0 } \right) = y _ { 0 } } } \\ { { y ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } } } \end{array} .
$$

In order to solve (13.1) numerically, one can for instance apply a Runge-Kutta method to (13.2). This yields

$$
\begin{array} { l } { { k _ { i } = y _ { 0 } ^ { \prime } + h \sum _ { j } a _ { i j } k _ { j } ^ { \prime } } } \\ { { \ } } \\ { { k _ { i } ^ { \prime } = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum a _ { i j } k _ { j } , y _ { 0 } ^ { \prime } + h \sum a _ { i j } k _ { j } ^ { \prime } \right) } } \\ { { \ } } \\ { { y _ { 1 } = y _ { 0 } + h \sum b _ { i } k _ { i } } } \\ { { \ } } \\ { { y _ { 1 } ^ { \prime } = y _ { 0 } ^ { \prime } + h \sum b _ { i } k _ { i } ^ { \prime } . } } \end{array}
$$

If we insert the first formula of (13.3) into the others we obtain

$$
\begin{array} { l } { { k _ { i } ^ { \prime } = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + c _ { i } h y _ { 0 } ^ { \prime } + h ^ { 2 } \sum _ { j } \overline { { { a } } } _ { i j } k _ { j } ^ { \prime } , y _ { 0 } ^ { \prime } + h \sum _ { j } a _ { i j } k _ { j } ^ { \prime } \right) } } \\ { {  } } \\ { { y _ { 1 } = y _ { 0 } + h y _ { 0 } ^ { \prime } + h ^ { 2 } \sum _ { i } ^ { \prime } \overline { { { b } } } _ { i } k _ { i } ^ { \prime } } } \\ { {  } } \\ { { y _ { 1 } ^ { \prime } = y _ { 0 } ^ { \prime } + h \sum b _ { i } k _ { i } ^ { \prime } } } \end{array}
$$

where

$$
\begin{array} { r } { \overline { { a } } _ { i j } = \displaystyle \sum _ { k } a _ { i k } a _ { k j } \ , \qquad \overline { { b } } _ { i } = \sum _ { j } b _ { j } a _ { j i } \ . } \end{array}
$$

For an implementation the representation (13.4） is preferablc to (13.3)， since about half of the storage can be saved. This may be important, in particular if the dimension of Equation (13.1） is large.

# N ystrom methods

R.H. Merson: ".. I have not seen the paper by Nystrom. Was it in English ?"   
J.M. Bennett: In German actually， not Finnish." (1957)

E.J. Nystrom (1925) was the first to consider methods of the form (13.4) in which the coefficients do not necessarily satisfy (13.5) ("Da bis jetzt die direkte Anwendung der Rungeschen Methode auf den wichtigen Fall von Differentialgleichungen zweiter Ordnung nicht behandelt war,.." Nystrom， 1925). Such direct methods are called Nystrom methods.

Definition 13.1. A Nystrom method (13.4) has order $p$ if for sufficiently smooth problems (13.1)

$$
\begin{array} { r } { y \left( x _ { 0 } + h \right) - y _ { 1 } = \mathbf { O } ( h ^ { p + 1 } ) } \\ { y ^ { \prime } ( x _ { 0 } + h ) - y _ { 1 } ^ { \prime } = \mathbf { O } ( h ^ { p + 1 } ) \ . } \end{array}
$$

An example of a Nystrom method where Condition (13.5) is violated is given in Table 13.1. Nyström claimed that this method would be simpler to apply than "Runge-Kutta's" and reduce the work by about $2 5 \%$ This is, of course, not true if the Runge-Kutta method is applied as in (13.4) (see also Exercise 2).

Table 13.1. Nystrom, order 4   

<table><tr><td>N 0 Ci</td><td>1云</td><td>0</td><td>1 ←aij</td><td>1 0</td><td>↑</td><td></td><td></td><td>a j</td></tr><tr><td></td><td>1</td><td>0</td><td>1 0</td><td></td><td>0</td><td>0</td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td>2</td><td></td><td>←bi</td></tr><tr><td></td><td>b ：一</td><td>1</td><td>1</td><td>0</td><td></td><td>2</td><td></td><td>1</td></tr></table>

A real improvement can be achieved in the case where the righthand-side of (13.1) does not depend on $y ^ { \prime } ,$ i.e.

$$
y ^ { \prime \prime } = f \left( x , y \right) .
$$

Here the Nystrom method becomes

$$
\begin{array} { l } { { { k _ { i } ^ { \prime } } = f \left( x _ { 0 } + c _ { i } h , y _ { 0 } + c _ { i } h y _ { 0 } ^ { \prime } + h ^ { 2 } \sum _ { j } \bar { a } _ { i j } k _ { j } ^ { \prime } \right) } } \\ { { \ } } \\ { { { y _ { 1 } } = y _ { 0 } + h y _ { 0 } ^ { \prime } + h ^ { 2 } \sum _ { i } ^ { - } { \bar { b _ { i } } } k _ { i } ^ { \prime } } } \\ { { \ } } \\ { { { y _ { 1 } ^ { \prime } } = y _ { 0 } ^ { \prime } + h \sum b _ { i } k _ { i } ^ { \prime } . } } \end{array}
$$

and the coefficients $a _ { \ i j }$ are no longer nccdcd. Somc cxamplcs arc given in Tablc 13.2. Thc fifth-order method of Table 13.2 needs only four cvaluations of $f$ . This is a considerable improvement compared to Rungc-Kutta mcthods where at least six evaluations are neccssary (cf. Theorem 6.1).

Table 13.2. Methods for y "=f (x ,y)   

<table><tr><td colspan="4">Nystr8m, order 4</td><td colspan="4">Nystr8m, order 5 ai</td></tr><tr><td rowspan="8">Ci 2 1</td><td rowspan="8">0 1</td><td rowspan="8">1</td><td rowspan="8">aj</td><td>0 1-52-3</td><td></td></tr><tr><td></td><td>1-5017</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>云 9</td></tr><tr><td>3 1</td><td>35</td></tr><tr><td>10</td><td>54</td></tr><tr><td>14</td><td>100 336</td></tr><tr><td rowspan="2">bi</td><td>1</td><td>1 0 3</td><td rowspan="2">bi</td><td>336</td><td>336</td><td rowspan="2">0</td></tr><tr><td></td><td></td><td>14</td><td>125</td></tr><tr><td rowspan="2">bi</td><td>I</td><td>4</td><td>1</td><td rowspan="2">bi 336</td><td>336</td><td>162 35 336</td></tr><tr><td></td><td></td><td></td><td></td><td>336</td></tr></table>

Our next aim is to derive the order conditions for Nystrom methods. For this purpose we extend the theory of Section I.2 to second order differential equations (Hairer-Wanner (1976)).

# The derivatives of the exact solution

As for first order equations we may restrict ourselves to systems of autonomous differential equations

$$
( y ^ { J } ) ^ { \prime \prime } = f ^ { J } ( y ^ { 1 } , \dots , y ^ { n } , y ^ { \prime 1 } , \dots , y ^ { \prime ^ { n } } )
$$

(if necessary， add $x \ ^ { \prime \prime } { = } 0$ ). The superscript index J denotes the $J$ -th componcnt of the corresponding vector. We now calculate the derivativcs of the exact solution of (13.11). The second derivative is given by (13.11):

$$
{ ( y ^ { J } ) } ^ { ( 2 ) } = { f ^ { J } } ( y , y ^ { \prime } ) .
$$