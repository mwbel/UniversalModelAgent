# 344 Methods based on Radau and Lobatto quadrature

It will be shown in Subsection 353 that the Gauss methods have stability regions equal to exactly the left half-plane, and they are therefore A-stable.

For many stiff problems, it is desirable to sacrifice order to gain L-stability, so that the stability function satisfies the property $\begin{array} { r } { \operatorname* { l i m } _ { | z | \to \infty } | R ( z ) | = 0 } \end{array}$ . We explore methods based on quadrature formulae of orders $2 s - 1$ or $2 s \textrm { -- } 2$ . Instead of choosing $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ to obtain as high a degree as possible for polynomials $\phi$ such that

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) ,
$$

we choose either (i) $c _ { 1 } = 0$ , (ii) ${ c _ { s } = 1 }$ or (iii) $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ . The remaining unspecified $c _ { i }$ are then chosen to make (344a) true for a polynomial of degree as high as is still possible.

A ‘Radau I quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ ; a ‘Radau II quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and a ‘Lobatto quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ . Note that ‘Lobatto’ is sometimes referred to as ‘Lobatto III’, to bring the naming of these formulae into a consistent pattern. These three quadrature formulae are the ones sought. We have:

Theorem 344A Let $c _ { 1 } < c _ { 2 } < \cdots < c _ { s }$ be chosen as abscissae of the Radau   
I, the Radau II or the Lobatto quadrature formula, respectively. Then: I For the Radau $I$ formula, $c _ { 1 } = 0$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
II For the Radau II formula, ${ c _ { s } = 1 }$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
III For the Lobatto formula, $c _ { 1 } ~ = ~ 0 , c _ { s } ~ = ~ 1$ . This formula is exact for polynomials of degree up to $2 s - 3$ .   
Furthermore, for each of the three quadrature formulae, $c _ { i } ~ \in ~ [ 0 , 1 ]$ , for   
$i = 1 , 2 , \dots , s$ , and $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ .

Proof. The fact that $x = 1$ is a zero of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b). The fact that $x = 0$ is a zero of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b) and (342c), with $x = 1$ . Let $\phi$ denote an arbitrary polynomial of degree not exceeding $2 s - 2$ in the Radau cases or $2 s - 3$ in the Lobatto case. Divide this by the polynomial satisfied by the abscissae and write $Q$ for the quotient and $R$ for the remainder. We have in the three cases,

$$
\begin{array} { r l r l } & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { L o b a t t o ~ c a s e } . } \end{array}
$$

Methods in the Radau and Lobatto families   

<table><tr><td>Name</td><td>Choice of b&#x27;and c</td><td>Choice of A</td></tr><tr><td>Radau I</td><td>Radau I quadrature</td><td>C(s)</td></tr><tr><td>Radau IA</td><td>Radau I quadrature</td><td>Thereflections of Radau II</td></tr><tr><td>Radau II</td><td>Radau II quadrature</td><td>D(s)</td></tr><tr><td>Radau IA</td><td>Radau II quadrature</td><td>The reflections of Radau I</td></tr><tr><td>Lobatto III</td><td>Lobatto quadrature</td><td>C(s-1)，a1s = a2s=..=αss =0</td></tr><tr><td>Lobatto IIIA</td><td>Lobatto quadrature</td><td>C(s)</td></tr><tr><td>Lobatto IIIB</td><td>Lobatto quadrature</td><td>D(s)</td></tr><tr><td>Lobatto IIIC</td><td>Lobatto quadrature</td><td>Thereflections ofLobatto III</td></tr></table>

Evaluate the approximate integral of $\phi$ written in this form, and the terms involving $Q$ are zero because of orthogonality, and the terms involving $R$ are exact because of the interpolational nature of the quadrature.

In the Radau cases, to prove that the abscissae are always in $\lfloor 0 , 1 \rfloor$ and that the weights are positive, use a homotopy $t \mapsto P _ { s } ^ { * } \pm t P _ { s - 1 } ^ { * }$ , where the upper sign is used for Radau I and the lower sign for Radau II. If any of the weights becomes zero, then for this value of $t$ , the quadrature formula has a greater order than is possible. Furthermore, no abscissae can move outside $[ 0 , 1 ]$ , until $t$ reaches a value $t = 1$ . The proof is slightly more complicated in the Lobatto case, where we use the homotopy $t \mapsto P _ { s } ^ { * } - t P _ { s - 2 } ^ { * }$ . Because of the symmetry of the quadrature formula for all $t$ , $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ both occur at the same time and this is when $t = 1$ . If a weight passes through zero, then we again obtain a contradiction to the optimality of Gaussian quadrature because two weights vanish simultaneously. The one case not covered by this argument is when $s$ is odd and the weight corresponding to $\begin{array} { r } { c _ { ( s + 1 ) / 2 } = \frac { 1 } { 2 } } \end{array}$ vanishes. However, it is impossible that as $t$ moves from 0 to $1$ , it passes through a point for which this happens because in this case the remaining abscissae would have to be the zeros of $P _ { s - 1 } ^ { * }$ . By (342f), this occurs only for $t = - ( n - 1 ) / n$ , and this has the wrong sign. 

Given the choice of $c$ and $b ^ { \top }$ in accordance with the requirements of Radau I, Radau II or Lobatto quadrature, the choice of $A$ to yield a Runge–Kutta of the same order as for the underlying quadrature formula remains. The most obvious choice, of making the methods as close to explicit as possible, is inappropriate for stiff problems, but makes the method more efficient for nonstiff problems. Other choices can be made in terms of the $C$ and $D$ conditions, and in terms of specific choices of specific elements of $A$ . To distinguish these from the simple (closest to explicit) choices, a letter A, B or C is added to the designation for the method. A summary of many of the methods in the Radau and Lobatto families is given in Table 344(I).

Selected examples of these methods are as follows, where we note that Lobatto IIIB with $s = 2$ does not exist:

$$
\mathrm { R a d a u } \mathrm { ~ I ~ } \qquad ( s = 2 , p = 3 ) ,
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/f203af32647fc4e925753f71395de816b9168e09faaa76f5c879fb36d1348986.jpg)

Radau IA ( $s = 2 , p = 3$ ),

Radau II ( $s = 2 , p = 3$ ),

$$
\begin{array} { r } { { \frac { 1 } { 3 } } ~ { \left| \begin{array} { l l } { { \frac { 1 } { 3 } } } & { 0 } \\ { 1 } & { 0 } \end{array} \right| } } \\ { { \frac { 1 } { 4 } } ~ { \frac { 1 } { 4 } } } \end{array}
$$

Radau IIA ( $s = 2 , p = 3$ ),

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/d49b79b2c9447690cb0534a32535b4ff31a050cc9cac856b6b52e17a882190ca.jpg)

Radau I ( $s = 3 , p = 5$ ),

Radau IA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">0 6-√6 10</td><td rowspan="2">1 G</td><td rowspan="2">-1-√6 18 88+7√6 360</td><td>-1+√6 18</td></tr><tr><td>88-43√6 360</td></tr><tr><td>6+√6 10</td><td></td><td>88+43√6 360</td><td>88-7√6</td></tr><tr><td></td><td></td><td>16+√6</td><td>360</td></tr><tr><td></td><td>1</td><td>36</td><td>16-√6 36</td></tr></table>

$$
\mathrm { R a d a u \ I I } \qquad ( s = 3 , p = 5 ) ,
$$

<table><tr><td>4-√6 10 4+V6</td><td>24-√6 120 24+11√6</td><td>24-11√6 120 24+√6</td><td>0</td></tr><tr><td>10 1</td><td>120 6-√6</td><td>120 6+√6</td><td>0 0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td></td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td></td></tr></table>

Radau IIA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">4-√6 10 4+√6 10</td><td rowspan="2">88-7√6 360 296+169√6 1800 16-√6</td><td>296-169√6 1800</td><td>-2+3√6 225</td></tr><tr><td>88+7√6 360</td><td>-2-3√6 225</td></tr><tr><td rowspan="2">1</td><td>36</td><td>16+√6 36</td><td>1</td></tr><tr><td>16-√6 36</td><td>16+√6 36</td><td>1</td></tr></table>

Lobatto III ( $s = 2 , p = 2$ ),

<table><tr><td>0 1</td><td>0 0 1 0</td></tr><tr><td></td><td>1 1</td></tr></table>

Lobatto IIIA ( $s = 2 , p = 2$ ),

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/786cc1641957243644dabdad9f5e83e2ec1595e38cc7239060923684af77638e.jpg)

Lobatto IIIC ( $s = 2 , p = 2$ ),

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/345a7d6c870c6a20ef53fef71a5c1d598e76aefe70ff84b3724613edd711806c.jpg)

$$
\mathrm { L o b a t t o ~ I I I } \qquad ( s = 3 , p = 4 ) ,
$$

<table><tr><td></td><td>0 0</td><td>0</td></tr><tr><td>0</td><td>4 4 0 1</td><td>0 0</td></tr><tr><td></td><td>1 2</td><td>1</td></tr></table>

Lobatto IIIA ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>0 </td></tr><tr><td></td><td>D</td></tr><tr><td></td><td></td></tr><tr><td></td><td>1</td></tr></table>

Lobatto IIIB ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>G</td><td>N 0 0</td></tr><tr><td></td><td>1</td><td>0 1</td></tr></table>

Lobatto IIIC ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>GU</td><td>美</td><td>广</td></tr><tr><td rowspan="3"></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

Lobatto III ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td>0 5+√5 60</td><td>0 </td><td>0 15-7√5 60</td><td>0 0</td></tr><tr><td rowspan="3">5+√5 10 1</td><td>5-5 60</td><td>15+7√5 60</td><td>1</td><td>0</td></tr><tr><td>1</td><td>5-5</td><td>5+√5</td><td>0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td rowspan="3"></td><td>1</td><td>品</td><td>品</td><td>1 12</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

Lobatto IIIA ( $s = 4 , p = 6$ ),

<table><tr><td rowspan="2">0 5-√5 10</td><td rowspan="2">0 11+√5 120</td><td>0</td><td>0</td><td>0</td></tr><tr><td>25-√5 120</td><td>25-13√5 120</td><td>-1+√5 120</td></tr><tr><td>5+√5 10</td><td>11-√5 120</td><td>25+13√5 120</td><td>25+√5 120</td><td>-1-√5 120</td></tr><tr><td rowspan="2">1</td><td>1 12</td><td>5 12</td><td>5 12</td><td>1</td></tr><tr><td>12</td><td>5 12</td><td>品</td><td>12 1 12</td></tr></table>

Lobatto IIIB ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td></td><td>-1-√5 24 25+√5 120</td><td>-1+√5 24 25-13√5 120</td><td>0 0</td></tr><tr><td>5+√5 10</td><td></td><td>25+13√5 120 11-√5</td><td>25-√5 120 11+√5</td><td>0</td></tr><tr><td>1</td><td></td><td>120</td><td>120</td><td>0</td></tr><tr><td></td><td>1</td><td>5</td><td>5 12</td><td>1 12</td></tr><tr><td></td><td>12</td><td>12</td><td></td><td></td></tr></table>

Lobatto IIIC ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10 5+√5 10 1</td><td>中</td><td>长 12 4 10+7√5 60 5 12 5</td><td>60 1 12 5</td><td></td></tr></table>

Lobatto III

<table><tr><td>(s=5,p=8), 0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7-√21</td><td>立前</td><td></td><td>13-3√21</td><td>14-3√21</td><td></td></tr><tr><td>14</td><td></td><td>1</td><td>63</td><td>126</td><td>0</td></tr><tr><td>1</td><td></td><td>91+21√21</td><td>美</td><td>91-21V21</td><td>0</td></tr><tr><td></td><td></td><td>576</td><td>13+3V21</td><td>576</td><td></td></tr><tr><td>7+√21</td><td>1 14</td><td>14+3√21</td><td>63</td><td></td><td>0</td></tr><tr><td>14</td><td></td><td>126 7</td><td></td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>18</td><td>2</td><td>18</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td>49</td><td>16</td><td>49</td><td>1</td></tr><tr><td>20</td><td>180</td><td>45</td><td>180</td><td>20</td></tr></table>

Lobatto IIIA ( $s = 5 , p = 8$ ),

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td colspan="2">0</td></tr><tr><td>7-√21 14</td><td>119+3√21</td><td>343-9√21</td><td>392-96√21</td><td>343-69√21</td><td colspan="2">-21+3√21</td></tr><tr><td>1</td><td>1960</td><td>2520 392+105√21</td><td>2205</td><td>2520 392-105√21</td><td colspan="2">1960</td></tr><tr><td>2</td><td>13 320</td><td></td><td>8</td><td></td><td colspan="2">3</td></tr><tr><td>7+√21</td><td>119-3√21</td><td>2880 343+69√21</td><td>45 392+96√21</td><td>2880</td><td colspan="2">320</td></tr><tr><td>14</td><td></td><td></td><td></td><td>343+9√21</td><td colspan="2">-21-3√21</td></tr><tr><td></td><td>1960 1</td><td>2520</td><td>2205</td><td>2520</td><td colspan="2">1960</td></tr><tr><td>1</td><td></td><td>49</td><td>16</td><td>49</td><td colspan="2">1</td></tr><tr><td rowspan="2"></td><td>20</td><td>180</td><td>45</td><td>180</td><td colspan="2">20</td></tr><tr><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td colspan="2">1 20</td></tr><tr><td colspan="4">LobattoIIIB (s=5, P1-2015151-201 =8)，</td><td rowspan="2">-7+√21</td><td rowspan="2">0</td></tr><tr><td>0 7-√21</td><td></td><td>27-√21 120</td><td>15</td></tr><tr><td rowspan="12"></td><td></td><td>343+9√21</td><td>56-15√21</td><td>120 343-69√21</td><td rowspan="2">0</td></tr><tr><td></td><td>2520</td><td>315</td><td>2520</td></tr><tr><td>14</td><td></td><td>49+12√12</td><td>49-12√12</td><td>0</td></tr><tr><td>1</td><td>360</td><td>8 45</td><td>360</td><td></td></tr><tr><td>7+√21</td><td>343+69√21</td><td>56+15√21</td><td>343-9√21</td><td>0</td></tr><tr><td>14</td><td>2520</td><td>315</td><td>2520</td><td></td></tr><tr><td>1</td><td>119-3√21</td><td>13</td><td>119+3√21</td><td>0</td></tr><tr><td></td><td></td><td>360</td><td>45</td><td>360</td><td></td></tr><tr><td></td><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td>1 20</td></tr></table>

Lobatto IIIC ( $s = 5 , p = 8$ ),

<table><tr><td>0 7-√21 14 1 7+√21</td><td>中</td><td>7 60 29 180 329+105√21 2880 203+30√21</td><td>2 15 47-15√21 315 73 360 47+15√21 315</td><td>7 60 203-30√21 1260 329-105√21 2880</td><td>六 140 3 160</td></tr></table>

# Exercises 34

34.1 Show that there is a unique Runge–Kutta method of order 4 with $s = 3$ for which $A$ is lower triangular with $a _ { 1 1 } = a _ { 3 3 } = 0$ . Find the tableau for this method.

34.2 Show that the implicit Runge–Kutta given by the tableau

<table><tr><td>0 A</td><td>0 0</td></tr><tr><td>1</td><td>云 0 0</td></tr><tr><td></td><td></td></tr><tr><td>0</td><td>0</td></tr><tr><td>1 32 14 81</td><td>药 0 250 5</td></tr></table>

has order 5.

34.3 Find the tableau for the Gauss method with $s = 4$ and $p = 8$ .

34.4 Show that Gauss methods are invariant under reflection.
