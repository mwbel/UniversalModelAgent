[YG]Young, D. M.and R.T. Gregory,A survey of numerical mathematics. Vol. 1,Addison-Wesley, Reading,MA,1972,533 pp. QA297.Y63102   
[ZM] Zienkiewicz, O. C. and K. Morgan,Finite elements and approximation, John Wiley & Sons, New York,1983,328 pp. QA297.5.Z53739, 742

# Answers for Selected Exercises

# Exercise Set 1.1 (Page 15)

1. For each part, $f \in C [ a , b ]$ on the given interval. Since $f ( a )$ and $f ( b )$ are of opposite sign, the Intermediate Value Theorem implies that a number $c$ exists with $f ( c ) = 0$

3. For each part, $f \in C [ a , b ] , .$ $f ^ { \prime }$ exists on $( a , b )$ and $f ( a ) = f ( b ) = 0$ .Rolle's Theorem implies that a number $c$ exists in $( a , b )$ with $f ^ { \prime } ( c ) = 0$ .For part (d), we can use $[ a , b ] = [ - 1 , 0 ]$ or $[ a , b ] = [ 0 , 2 ]$

5. For $x < 0$ ， $f ( x ) < 2 x + k < 0$ ， provided that $x < - { \frac { 1 } { 2 } } k$ . Similarly, for $x > 0$ ， $f ( x ) > 2 x + k > 0$ ，provided that $\textstyle x > - { \frac { 1 } { 2 } } k$ . By Theorem 1.13, there exists a number $\pmb { c }$ with $f ( c ) = 0$ If $f ( c ) = 0$ and $f ( c ^ { \prime } ) = 0$ for some $c ^ { \prime } \neq c$ ， then by Theorem 1.7, there exists a number $p$ between $c$ and $c ^ { \prime }$ with $f ^ { \prime } ( p ) = 0$ .However, $f ^ { \prime } ( x ) = 3 x ^ { 2 } + 2 > 0$ for all $x$

7.a. $P _ { 2 } ( x ) = 0$ b. $R _ { 2 } ( 0 . 5 ) = 0 . 1 2 5$ ; actual $\mathrm { e r r o r } = 0 . 1 2 5$ c. $P _ { 2 } ( x ) = 1 + 3 ( x - 1 ) + 3 ( x - 1 ) ^ { 2 }$ d. $R _ { 2 } ( 0 . 5 ) = - 0 . 1 2 5$ ; actual e $\mathrm { \ a r c o r } = - 0 . 1 2 5$

9. Since

$$
P _ { 2 } ( x ) = 1 + x \quad { \mathrm { a n d } } \quad R _ { 2 } ( x ) = { \frac { - 2 e ^ { \xi } ( \sin \xi + \cos \xi ) } { 6 } } x ^ { 3 }
$$

for some $\xi$ between $x$ and O,we have the following:

a. $P _ { 2 } ( 0 . 5 ) = 1 . 5$ and $| f ( 0 . 5 ) - P _ { 2 } ( 0 . 5 ) | \le 0 . 0 5 3 2$   
b. $| f ( x ) - P _ { 2 } ( x ) | \leq 1 . 2 5 2$ ：  
c. $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) \ d x \approx 1 . 5 . } \end{array}$   
d. $\begin{array} { r } { \mid \int _ { 0 } ^ { 1 } f ( x ) \ d x - \int _ { 0 } ^ { 1 } P _ { 2 } ( x ) \ d x \mid \leq \int _ { 0 } ^ { 1 } | R _ { 2 } ( x ) | d x \leq 0 . 3 1 3 . } \end{array}$ ， and the actual error is 0.122.

11. $P _ { 3 } ( x ) = ( x - 1 ) ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } ( x - 1 ) ^ { 3 }$ a. $P _ { 3 } ( 0 . 5 ) = 0 . 3 1 2 5 0 0$ ， $f ( 0 . 5 ) = 0 . 3 4 6 5 7 4$ . An error bound is 0.2916,and the actual error is 0.034074. b. $| f ( x ) - P _ { 3 } ( x ) | \leq 0 . 2 9 1 { \overline { { 6 } } }$ on [0.5, 1.5] c. $\begin{array} { r } { \int _ { 0 . 5 } ^ { 1 . 5 } P _ { 3 } ( x ) \ d x = 0 . 0 8 \overline { { 3 } } , \ \int _ { 0 . 5 } ^ { 1 . 5 } ( x - 1 ) \ln x \ d x = 0 . 0 8 8 0 2 0 } \end{array}$ d. An error bound is O.0583,and the actual error is $4 . 6 8 7 \times 1 0 ^ { - 3 }$

13. $P _ { 4 } ( x ) = x + x ^ { 3 }$ a. $| f ( x ) - P _ { 4 } ( x ) | \leq 0 . 0 1 2 4 0 5$ $\begin{array} { r } { \int _ { 0 } ^ { 0 . 4 } P _ { 4 } ( x ) \ d x = 0 . 0 8 6 4 , \ \int _ { 0 } ^ { 0 . 4 } x e ^ { x ^ { 2 } } \ d x = 0 . 0 8 6 7 5 5 } \end{array}$ c. $8 . 2 7 \times 1 0 ^ { - 4 }$ d. $P _ { 4 } ^ { \prime } ( 0 . 2 ) = 1 . 1 2$ ， $f ^ { \prime } ( 0 . 2 ) = 1 . 1 2 4 0 7 6$ . The actual error is $4 . 0 7 6 \times 1 0 ^ { - 3 }$

15. Since $4 2 ^ { \circ } = 7 \pi / 3 0$ radians,use $x _ { 0 } = \pi / 4$ . Then

$$
\left| R _ { n } \left( \frac { 7 \pi } { 3 0 } \right) \right| \leq \frac { \left( \frac { \pi } { 4 } - \frac { 7 \pi } { 3 0 } \right) ^ { n + 1 } } { ( n + 1 ) ! } < \frac { ( 0 . 0 5 3 ) ^ { n + 1 } } { ( n + 1 ) ! } .
$$

For $\textstyle { \big | } R _ { n } { \big ( } { \frac { 7 \pi } { 3 0 } } { \big ) } { \big | } < 1 0 ^ { - 6 }$ , it suffices to take $n = 3$ .To 7 digits,cos $4 2 ^ { \circ } = 0 . 7 4 3 1 4 4 8$ and $\begin{array} { r } { P _ { 3 } ( 4 2 ^ { \circ } ) = P _ { 3 } ( \frac { 7 \pi } { 3 0 } ) = 0 . 7 4 3 1 4 4 6 . } \end{array}$ ，so the actual error is $2 \times 1 0 ^ { - 7 }$

17. a. $\begin{array} { r } { P _ { 3 } ( x ) = \ln ( 3 ) + \frac { 2 } { 3 } ( x - 1 ) + \frac { 1 } { 9 } ( x - 1 ) ^ { 2 } - \frac { 1 0 } { 8 1 } ( x - 1 ) ^ { 3 } } \end{array}$ b. $\begin{array} { r } { \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) - P _ { 3 } ( x ) | = | f ( 0 ) - P _ { 3 } ( 0 ) | = 0 . 0 2 6 6 3 3 6 6 } \end{array}$ c. $\begin{array} { r } { \tilde { P } _ { 3 } ( x ) = \ln ( 2 ) + \frac { 1 } { 2 } x ^ { 2 } } \end{array}$ d. $\begin{array} { r } { \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) - \tilde { P } _ { 3 } ( x ) | = | f ( 1 ) - \tilde { P } _ { 3 } ( 1 ) | = 0 . 0 9 4 5 3 4 8 9 } \end{array}$ e. $P _ { 3 } ( 0 )$ approximates $f ( 0 )$ better than $\tilde { P } _ { 3 } ( 1 )$ approximates $f ( 1 )$

19. $P _ { n } ( x ) = \sum _ { k = 0 } ^ { n } { \frac { 1 } { k ! } } x ^ { k } , \ n \geq 7$

21.A bound for the maximum error is 0.0026.

23. Since $\begin{array} { r } { R _ { 2 } ( 1 ) = \frac { 1 } { 6 } e ^ { \xi } } \end{array}$ , for some $\xi$ in (0,1), we have $\begin{array} { r } { | E - R _ { 2 } ( 1 ) | = \frac { 1 } { 6 } | 1 - e ^ { \xi } | \leq \frac { 1 } { 6 } ( e - 1 ) } \end{array}$

25.a. Let $x _ { 0 }$ be any number in $\{ a , b \}$ . Given $\epsilon > 0$ ,let $\delta = \epsilon / L$ .If $| x - x _ { 0 } | < \delta$ and $a \leq x \leq b$ ，then $| f ( x ) - f ( x _ { 0 } ) | \leq L | x - x _ { 0 } | < \epsilon$

b. Using the Mean Value Theorem,we have

$$
| f ( x _ { 2 } ) - f ( x _ { 1 } ) | = | f ^ { \prime } ( \xi ) | | x _ { 2 } - x _ { 1 } | ,
$$

for some $\xi$ between $x _ { 1 }$ and $x _ { 2 }$ ,so

$$
| f ( x _ { 2 } ) - f ( x _ { 1 } ) | \leq L | x _ { 2 } - x _ { 1 } | .
$$

c. One example is $f ( x ) = x ^ { 1 / 3 }$ on [0,1].

27. a. Since $f$ is continuous at $p$ and $f ( p ) \neq 0$ ,there exists a $\delta > 0$ with

$$
| f ( x ) - f ( p ) | < { \frac { | f ( p ) | } { 2 } } ,
$$

for $| x - p | < \delta$ and $a < x < b$ . We restrict $\delta$ so that $[ p - \delta , p + \delta ]$ is a subset of $[ a , b ]$ . Thus, for $x \in [ p - \delta , p + \delta ]$ we have $x \in [ a , b ]$ .So

$$
- { \frac { | f ( p ) | } { 2 } } < f ( x ) - f ( p ) < { \frac { | f ( p ) | } { 2 } }
$$

and

$$
f ( p ) - \frac { | f ( p ) | } { 2 } < f ( x ) < f ( p ) + \frac { | f ( p ) | } { 2 } .
$$

If $f ( p ) > 0$ ，then

$$
f ( p ) - \frac { | f ( p ) | } { 2 } = \frac { f ( p ) } { 2 } > 0 , \quad \mathrm { { s o } } \quad f ( x ) > f ( p ) - \frac { | f ( p ) | } { 2 } > 0 .
$$

If $f ( p ) < 0$ ,then $| f ( p ) | = - f ( p )$ ，and

$$
f ( x ) < f ( p ) + \frac { | f ( p ) | } { 2 } = f ( p ) - \frac { f ( p ) } { 2 } = \frac { f ( p ) } { 2 } < 0 .
$$

In either case, $f ( x ) \neq 0$ ,for $x \in \left[ p - \delta , p + \delta \right]$

b. Since $f$ is continuous at $p$ and $f ( p ) = 0$ , there exists a $\delta > 0$ with

$$
| f ( x ) - f ( p ) | < k , \quad \mathrm { f o r } \quad | x - p | < \delta \quad \mathrm { a n d } \quad a < x < b .
$$

We restrict $\delta$ so that $\{ p - \delta , p + \delta \}$ is a subset of $[ a , b ]$ . Thus, for $x \in [ p - \delta , p + \delta ]$ we have

$$
| f ( x ) | = | f ( x ) - f ( p ) | < k .
$$

# Exercise Set 1.2 (Page 26)

<table><tr><td>1.</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>a.</td><td>0.001264</td><td>4.025 × 10-4</td></tr><tr><td>b.</td><td>7.346 × 10-6</td><td>2.338 ×10-6</td></tr><tr><td>c.</td><td>2.818 × 10-4</td><td>1.037 × 10-4</td></tr><tr><td>d.</td><td>2.136 × 10-4</td><td>1.510 × 10-4</td></tr><tr><td>e.</td><td>2.647× 10l</td><td>1.202 × 10-3</td></tr><tr><td>f</td><td>1.454 × 10l</td><td>1.050 × 10-2</td></tr><tr><td>g</td><td>420</td><td>1.042 × 10-2</td></tr><tr><td>h.</td><td>3.343 ×10</td><td>9.213 × 10-3</td></tr></table>

3.The largest intervals area. (149.85,150.15）b. (899.1,900.9）c.(1498.5,1501.5)d.(89.91,90.09)

<table><tr><td>5.</td><td>Approximation</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>a.</td><td>134</td><td>0.079</td><td>5.90 × 10-4</td></tr><tr><td>b.</td><td>133</td><td>0.499</td><td>3.77 × 10-3</td></tr><tr><td>c.</td><td>2.00</td><td>0.327</td><td>0.195</td></tr><tr><td>d.</td><td>1.67</td><td>0.003</td><td>1.79 × 10-3</td></tr><tr><td>e.</td><td>1.80</td><td>0.154</td><td>0.0786</td></tr><tr><td>f.</td><td>-15.1</td><td>0.0546</td><td>3.60 × 10-3</td></tr><tr><td>g.</td><td>0.286</td><td>2.86 × 10-4</td><td>10-3</td></tr><tr><td>h.</td><td>0.00</td><td>0:0215</td><td>1.00</td></tr></table>

<table><tr><td>7.</td><td>Approximation</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>a.</td><td>133</td><td>0.921</td><td>6.88×10-3</td></tr><tr><td>b.</td><td>132</td><td>0.501</td><td>3.78× 10-3</td></tr><tr><td>c.</td><td>1.00</td><td>0.673</td><td>0.402</td></tr><tr><td>d.</td><td>1.67</td><td>0.003</td><td>1.79 × 10-3</td></tr><tr><td>e.</td><td>3.55</td><td>1.60</td><td>0.817</td></tr><tr><td>f.</td><td>-15.2</td><td>0.0454</td><td>0.00299</td></tr><tr><td>g.</td><td>0.284</td><td>0.00171</td><td>0.00600</td></tr><tr><td>h.</td><td>0</td><td>0.02150</td><td>1</td></tr></table>

<table><tr><td>9.</td><td>Approximation</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>a.</td><td>3.14557613</td><td>3.983×10-3</td><td>1.268 × 10-3</td></tr><tr><td>b.</td><td>3.14162103</td><td>2.838 × 10-5</td><td>9.032× 10-6</td></tr></table>

11. a. -2 b. -1.941

$$
\ : \frac { x ( 1 - \frac { 1 } { 2 } x ^ { 2 } ) - ( x - \frac { 1 } { 6 } x ^ { 3 } ) } { x - ( x - \frac { 1 } { 6 } x ^ { 3 } ) } = - 2 \ :
$$

d.The relative error in part (b) is O.029. The relative error in part (c) is O.00050.

<table><tr><td>13.</td><td>X</td><td>Absolute Error</td><td>Relative Error</td><td>x2</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>a.</td><td>92.26</td><td>0.01542</td><td>1.672 × 10-4</td><td>0.005419</td><td>6.273×10-7</td><td>1.157 × 10-4</td></tr><tr><td>b.</td><td>0.005421</td><td>1.264 × 10-6</td><td>2.333×10-4</td><td>-92.26</td><td>4.580 ×10-3</td><td>4.965×10-5</td></tr><tr><td>c.</td><td>10.98</td><td>6.875 × 10-3</td><td>6.257×10-4</td><td>0.001149</td><td>7.566 × 10-8</td><td>6.584 × 10-5</td></tr><tr><td>d.</td><td>-0.001149</td><td>7.566 × 10-8</td><td>6.584×10-5</td><td>-10.98</td><td>6.875×10-3</td><td>6.257 ×10-4</td></tr></table>

15.The machine numbers are equivalent to

a. 3224   
b. -3224   
c. 1.32421875   
d.1.3242187500000002220446049250313080847263336181640625

17.b.The first formula gives -0.00658,and the second formula gives -O.0100.The true three-digit value is --0.0116.

19. The approximate solutions to the systems area. $x = 2 . 4 5 1$ ， $y = - 1 . 6 3 5$ b. $x = 5 0 7 . 7$ ， $y = 8 2 . 0 0$

21.a. In nested form, we have

$$
f ( x ) = ( ( ( 1 . 0 1 e ^ { x } - 4 . 6 2 ) e ^ { x } - 3 . 1 1 ) e ^ { x } + 1 2 . 2 ) e ^ { x } - 1 . 9 9 .
$$

b. --6.79c. --7.07

23.a. $n = 7 7$ b. $n = 3 5$

25 . ${ \binom { m } { k } } = { \frac { m ! } { k ! ( m - k ) ! } } = { \frac { m ( m - 1 ) \cdot \cdot \cdot ( m - k - 1 ) ( m - k ) ! } { k ! ( m - k ) ! } } = \left( { \frac { m } { k } } \right) \left( { \frac { m - 1 } { k - 1 } } \right) \cdot \cdot \cdot \left( { \frac { m - k - 1 } { 1 } } \right) .$ $m = 1 7$ 1） c. $m = 1 8 1 7 0 7$   
d.2,597,000; actual error 1960; relative error $7 . 5 4 1 \times 1 0 ^ { - 4 }$

27.a.124.03b.124.03 c.-124.03d.-124.03 e.0.0065 f.0.0065g. -0.0065h.-0.0065

# Exercise Set 1.3 (Page 37)

1.a.The approximate sums are 1.53 and 1.54,respectively.The actual value is 1.549.Significant roundoff error occurs earlier with the first method.

3.a.2000 termsb.20,000,000,000 terms

5.3 terms

7. The rates of convergence are:

a. $O ( h ^ { 2 } )$ b $O ( h )$ c. O(h²） d. O(h)

13.a. If $| \alpha _ { n } - \alpha _ { 1 } ^ { \downarrow } / ( 1 / n ^ { p } ) \leq K$ ，then $| \alpha _ { n } - \alpha | \leq K ( 1 / n ^ { p } ) \leq K ( 1 / n ^ { q } )$ since $0 < q < p$ . Thus, $| \alpha _ { n } - \alpha | / ( 1 / n ^ { p } ) \leq K$ and $\{ \alpha _ { n } \} _ { n = 1 } ^ { \infty } \to \alpha$ with rate of convergence ${ \cal O } ( 1 / n ^ { p } )$ ·

<table><tr><td>b. n</td><td>1/n</td><td>1/n²</td><td>1/n3 1/n5</td></tr><tr><td>5 0.2</td><td>0.04</td><td>0.008</td><td>0.0016</td></tr><tr><td>10</td><td>0.1</td><td>0.01 0.001</td><td>0.0001</td></tr><tr><td>50 100</td><td>0.02 0.01</td><td>0.0004 8×10-6 10-4 10-6</td><td>1.6 × 10-7 10-8</td></tr></table>

${ \cal O } ( 1 / n ^ { 4 } )$ is the most rapid convergence rate.

5. Suppose that for sufficiently small $| x |$ we have positive constants $k _ { 1 }$ and $k _ { 2 }$ independent of $x$ , for which

$$
| F _ { 1 } ( x ) - L _ { 1 } | \leq K _ { 1 } | x | ^ { \alpha } \mathrm { a n d } | F _ { 2 } ( x ) - L _ { 2 } | \leq K _ { 2 } | x | ^ { \beta } .
$$

Let $c = \operatorname* { m a x } ( | c _ { 1 } | , | c _ { 2 } | , 1 )$ ， $K = \operatorname* { m a x } ( K _ { 1 } , K _ { 2 } )$ ， and $\delta = \operatorname* { m a x } ( \alpha , \beta )$

a. We have

$$
\begin{array} { r l } & { | F ( x ) - c _ { 1 } L _ { 1 } - c _ { 2 } L _ { 2 } | = | c _ { 1 } ( F _ { 1 } ( x ) - L _ { 1 } ) + c _ { 2 } ( F _ { 2 } ( x ) - L _ { 2 } ) | } \\ & { \qquad \leq | c _ { 1 } | K _ { 1 } | x | ^ { \alpha } + | c _ { 2 } | K _ { 2 } | x | ^ { \beta } } \\ & { \qquad \leq c K [ | x | ^ { \alpha } + | x | ^ { \beta } ] } \\ & { \qquad \leq c K | x | ^ { \gamma } [ 1 + | x | ^ { \delta - \gamma } ] } \\ & { \qquad \leq \tilde { K } | x | ^ { \gamma } , } \end{array}
$$

for sufficiently small $| x |$ and some constant $\tilde { K }$ .Thus, $F ( x ) = c _ { 1 } L _ { 1 } + c _ { 2 } L _ { 2 } + O ( x ^ { \gamma } )$

b. We have

$$
\begin{array} { r l } & { | G ( x ) - L _ { 1 } - L _ { 2 } | = | F _ { 1 } ( c _ { 1 } x ) + F _ { 2 } ( c _ { 2 } x ) - L _ { 1 } - L _ { 2 } | } \\ & { \qquad \leq K _ { 1 } | c _ { 1 } x | ^ { \alpha } + K _ { 2 } | c _ { 2 } x | ^ { \beta } } \\ & { \qquad \leq K c ^ { \delta } [ | x | ^ { \alpha } + | x | ^ { \beta } ] } \\ & { \qquad \leq K c ^ { \delta } | x | ^ { \gamma } [ 1 + | x | ^ { \delta - \gamma } ] } \\ & { \qquad \leq \tilde { K } | x | ^ { \gamma } , } \end{array}
$$

for sufficiently small $| x |$ and some constant $\tilde { K }$ . Thus, $G ( x ) = L _ { 1 } + L _ { 2 } + O ( x ^ { \gamma } )$

17. a. 354224848179261915075 b. $0 . 3 5 4 2 2 4 8 5 3 8 \times 1 0 ^ { 2 1 }$ $\pmb { \mathbb { c } } _ { \pmb { \mathbb { 0 } } }$ The result in part (a)is computed using exact integer arithmetic,and the result in part (b) is computed using 10-digit rounding arithmetic. d. The result in part (a) required traversing a loop 98 times. e. The result is the same as the result in part (a).

# Exercise Set 2.1 (Page 53)

1. $p _ { 3 } = 0 . 6 2 5$

3. The Bisection method gives:a. $p _ { 7 } = 0 . 5 8 5 9$ b. $p _ { 8 } = 3 . 0 0 2$ c. $p _ { 7 } = 3 . 4 1 9$

5.The Bisection method gives $p _ { 9 } = 4 . 4 9 3 2$

7. The Bisection method gives:

a. $p _ { 1 7 } = 0 . 6 4 1 1 8 2$   
b. $p _ { 1 7 } = 0 . 2 5 7 5 3 0$   
c. For the interval $[ - 3 , - 2 ]$ ，we have $p _ { 1 7 } = - 2 . 1 9 1 3 0 7$ ,and for the interval $[ - 1 , 0 ]$ ，we have $p _ { 1 7 } = - 0 . 7 9 8 1 6 4 .$ d. For the interval [0.2,0.3], we have $p _ { 1 4 } = 0 . 2 9 7 5 2 8$ ,and for the interval [1.2,1.3],we have $p _ { 1 4 } = 1 . 2 5 6 6 2 2$

9. a. 2 b. -2 c. -1 d. 1

l1. The third root of 25 is approximately $p _ { 1 4 } = 2 . 9 2 4 0 1$ ,using [2,3].

13.A bound is $n \geq 1 4$ ,and $p _ { 1 4 } = 1 . 3 2 4 7 7$

15. Since $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } ( p _ { n } - p _ { n - 1 } ) = \operatorname* { l i m } _ { n \to \infty } 1 / n = 0 } \end{array}$ ,the difference in the terms goes to zero.However, $p _ { n }$ is the nth term of the divergent harmonic series,so $\scriptstyle \operatorname* { l i m } _ { n \to \infty } p _ { n } = \infty$

17. The depth of the water is 0.838 ft.

# Exercise Set 2.2 (Page 63)

1. For the value of $\pmb { x }$ under consideration we have

$$
x = ( 3 + x - 2 x ^ { 2 } ) ^ { 1 / 4 } \Leftrightarrow x ^ { 4 } = 3 + x - 2 x ^ { 2 } \Leftrightarrow f ( x ) = 0
$$

$$
x = \left( { \frac { x + 3 - x ^ { 4 } } { 2 } } \right) ^ { 1 / 2 } \Leftrightarrow 2 x ^ { 2 } = x + 3 - x ^ { 4 } \Leftrightarrow f ( x ) = 0
$$

$$
x = \left( { \frac { x + 3 } { x ^ { 2 } + 2 } } \right) ^ { 1 / 2 } \Leftrightarrow x ^ { 2 } ( x ^ { 2 } + 2 ) = x + 3 \Leftrightarrow f ( x ) = 0
$$

$$
{ \textbf { d . } } x = { \frac { 3 x ^ { 4 } + 2 x ^ { 2 } + 3 } { 4 x ^ { 3 } + 4 x - 1 } } \Leftrightarrow 4 x ^ { 4 } + 4 x ^ { 2 } - x = 3 x ^ { 4 } + 2 x ^ { 2 } + 3 \Leftrightarrow f ( x ) = 0
$$

3.The order in descending speed of convergence is (b), (d),(a). The sequence in (c) does not converg

5. With $g ( x ) = ( 3 x ^ { 2 } + 3 ) ^ { 1 / 4 }$ and $p _ { 0 } = 1$ ， $p _ { 6 } = 1 . 9 4 3 3 2$ is accurate to within 0.01.

7. Since $\begin{array} { r } { g ^ { \prime } ( x ) = \frac { 1 } { 4 } \cos \frac { x } { 2 } , } \end{array}$ $\pmb { g }$ is continuous and ${ \pmb g } ^ { \prime }$ exists on $[ 0 , 2 \pi ]$ . Further, $g ^ { \prime } ( x ) = 0$ only when $x = \pi$ ，so that $\begin{array} { r } { g ( 0 ) = g ( 2 \pi ) = \pi \leq g ( x ) = \leq g ( \pi ) = \pi + \frac { 1 } { 2 } } \end{array}$ and $\begin{array} { r } { | g ^ { \prime } ( x ) | \le \frac { 1 } { 4 } } \end{array}$ ,for $0 \leq x \leq 2 \pi$ . Theorem 2.2 implies that a unique fixed point $p$ exists in $[ 0 , 2 \pi ]$ .With $\begin{array} { r } { k = \frac { 1 } { 4 } } \end{array}$ and $p _ { 0 } = \pi$ ，we have $\begin{array} { r } { p _ { \mathrm { 1 } } = \pi + \frac { 1 } { 2 } } \end{array}$ . Corollary 2.4 implies that

$$
| p _ { n } - p | \leq { \frac { k ^ { n } } { 1 - k } } | p _ { 1 } - p _ { 0 } | = { \frac { 2 } { 3 } } \left( { \frac { 1 } { 4 } } \right) ^ { n } ;
$$

For the bound to be less than O.1,we need $n \geq 4$ . However, $p _ { 3 } = 3 . 6 2 6 9 9 6$ is accurate to within 0.01.

9. For $p _ { 0 } = 1 . 0$ and $\begin{array} { r } { g ( x ) = 0 . 5 ( x + \frac { 3 } { x } ) } \end{array}$ ,we have $\sqrt { 3 } \approx p _ { 4 } = 1 . 7 3 2 0 5$

11. a. With $[ 0 , 1 ]$ and $p _ { 0 } = 0$ ,we have $p _ { 9 } = 0 . 2 5 7 5 3 1$ . b. With [2.5,3.0] and $p _ { 0 } = 2 . 5$ ,we have $p _ { 1 7 } = 2 . 6 9 0 6 5 0$ c. With [0.25,1] and $p _ { 0 } = 0 . 2 5$ ，we have $p _ { 1 4 } = 0 . 9 0 9 9 9 9$ d. With [0.3, 0.7] and $p _ { 0 } = 0 . 3$ ， we have $p _ { 3 9 } = 0 . 4 6 9 6 2 5$ e. With [0.3,0.6] and $p _ { 0 } = 0 . 3$ ，we have $p _ { 4 8 } = 0 . 4 4 8 0 5 9$ f.With [0,1] and $p _ { 0 } = 0$ ,we have $p _ { 6 } = 0 . 7 0 4 8 1 2$

13. For $g ( x ) = ( 2 x ^ { 2 } - 1 0 \cos x ) / ( 3 x )$ ， we have the following:

$$
p _ { 0 } = 3 \Rightarrow p _ { 8 } = 3 . 1 6 1 9 3 ; ~ p _ { 0 } = - 3 \Rightarrow p _ { 8 } = - 3 . 1 6 1 9 3 .
$$

For $g ( x ) = \operatorname { a r c c o s } ( - 0 . 1 x ^ { 2 } )$ ， we have the following:

$$
p _ { 0 } = 1 \Rightarrow p _ { 1 1 } = 1 . 9 6 8 8 2 ; \quad p _ { 0 } = - 1 \Rightarrow p _ { 1 1 } = - 1 . 9 6 8 8 2 .
$$

15. With $\begin{array} { r } { g ( x ) = \frac { 1 } { \pi } } \end{array}$ arcsin $( - \frac { x } { 2 } ) + 2$ ， we have $p _ { 5 } = 1 . 6 8 3 8 5 5$

17. One of many examples is $g ( x ) = \sqrt { 2 x - 1 }$ on $\left[ \frac { 1 } { 2 } , 1 \right]$

21. Replace the second sentence in the proof with: “Since $\pmb { g }$ satisfies a Lipschitz condition on $[ a , b ]$ with a Lipschitz constant $L < 1$ , we have, for each $\pmb { n }$ ，

$$
| p _ { n } - p | = | g ( p _ { n - 1 } ) - g ( p ) | \leq L | p _ { n - 1 } - p | . ^ { \ast }
$$

The rest of the proof is the same, with $k$ replaced by $L$ ·

23.With $g ( t ) = 5 0 1 . 0 6 2 5 - 2 0 1 . 0 6 2 5 e ^ { - 0 . 4 t }$ and $p _ { 0 } = 5 . 0$ ， $p _ { 3 } = 6 . 0 0 2 8$ is within O.Ol s of the actual time.

# Exercise Set 2.3 (Page 74)

1. $p _ { 2 } = 2 . 6 0 7 1 4$

3. a. 2.45454 b. 2.44444 c. Part (b) is better.

5.a.For $p _ { 0 } = 2$ ， we have $p _ { 5 } = 2 . 6 9 0 6 5$ b. For $p _ { 0 } = - 3$ ,we have $p _ { 3 } = - 2 . 8 7 9 3 9 .$ c. For $p _ { 0 } = 0$ ，we have $p _ { 4 } = 0 . 7 3 9 0 9$ d. For $p _ { 0 } = 0$ ,we have $p _ { 3 } = 0 . 9 6 4 3 4$

7. Using the endpoints of the intervals as $p _ { 0 }$ and $p _ { 1 }$ ，we have:

i. a. $p _ { 1 1 } = 2 . 6 9 0 6 5$ b. $p _ { 7 } = - 2 . 8 7 9 3 9$ c. $p _ { 6 } = 0 . 7 3 9 0 9$ d $p _ { 5 } = 0 . 9 6 4 3 3$ ii. a. $p _ { 1 6 } = 2 . 6 9 0 6 0$ b. $p _ { 6 } = - 2 . 8 7 9 3 8$ c. $p _ { 7 } = 0 . 7 3 9 0 8$ d. $p _ { 6 } = 0 . 9 6 4 3 3$

9. For $p _ { 0 } = 1$ , we have $p _ { 5 } = 0 . 5 8 9 7 5 5$ . The point has the coordinates (0.589755,0.347811).

11. The equation of the tangent line is

$$
y - f ( p _ { n - 1 } ) = f ^ { \prime } ( p _ { n - 1 } ) ( x - p _ { n - 1 } ) .
$$

To complete this problem, set $y = 0$ and solve for ${ \mathfrak { x } } = p _ { n }$

13. a. For $p _ { 0 } = - 1$ and $p _ { 1 } = 0$ ， we have $p _ { 1 7 } = - 0 . 0 4 0 6 5 8 5 0$ and for $p _ { 0 } = 0$ and $p _ { 1 } = 1$ ， we have $p _ { 9 } = 0 . 9 6 2 3 9 8 4$ b. For $p _ { 0 } = - 1$ and $p _ { 1 } = 0$ ，we have $p _ { 5 } = - 0 . 0 4 0 6 5 9 2 9$ ,and for $p _ { 0 } = 0$ and $p _ { \mathrm { l } } = 1$ ， we have $p _ { 1 2 } = - 0 . 0 4 0 6 5 9 2 9$ . c. For $p _ { 0 } = - 0 . 5$ ，we have $p _ { 5 } = - 0 . 0 4 0 6 5 9 2 9$ ,and for $p _ { 0 } = 0 . 5$ ，we have $p _ { 2 1 } = 0 . 9 6 2 3 9 8 9$

15.This formula involves the subtraction of nearly equal numbers in both the numerator and denominator if $p _ { n - 1 }$ and $p _ { n - 2 }$ are nearly equal.

17. Seven iterations are required.

19. For $f ( x ) = \ln ( x ^ { 2 } + 1 ) - e ^ { 0 . 4 x } \cos \pi x$ ， we have the following roots. a.For $p _ { 0 } = - 0 . 5$ we have $p _ { 3 } = - 0 . 4 3 4 1 4 3 1$ b. For $p _ { 0 } = 0 . 5$ ，we have $p _ { 3 } = 0 . 4 5 0 6 5 6 7$ For $p _ { 0 } = 1 . 5$ ，we have $p _ { 3 } = 1 . 7 4 4 7 3 8 1$ For $p _ { 0 } = 2 . 5$ ，we have $p _ { 5 } = 2 . 2 3 8 3 1 9 8 .$ For $p _ { 0 } = 3 . 5$ ，we have $p _ { 4 } = 3 . 7 0 9 0 4 1 2$ c. The initial approximation $n - 0 . 5$ is quite reasonable. d. For $p _ { 0 } = 2 4 . 5$ ，we have $p _ { 2 } = 2 4 . 4 9 9 8 8 7 0$ .

21. The two numbers are approximately 6.512849 and 13.487151.

23. The borrower can afford to pay at most $8 . 1 0 \%$

25.a. solve $( 3 ^ { \widehat { - } } \left( 3 { \ast } \mathbf { x } { + } 1 \right) { - } 7 { \ast } 5 ^ { \widehat { - } } \left( 2 { \ast } \mathbf { x } \right) , \mathbf { x } )$ and fsolve $( 3 ^ { - } \left( 3 { \ast } \mathbf { x } { + } 1 \right) { - } 7 { \ast } 5 ^ { - } \left( 2 { \ast } \mathbf { x } \right) , \mathbf { x } )$ both fail. b. plot $( 3 ^ { - } ( 3 * x + 1 ) - 7 * 5 ^ { - } ( 2 * x )$ ， $x = a , b )$ generally yields no useful information. However, $a = 1 0 . 5$ and $b = 1 1 . 5$ in the plot command show that $f ( x )$ has a root near $x = 1 1$ $\pmb { \mathbb { c } _ { \bullet } }$ With $p _ { 0 } = 1 1$ ， P5 = 11.0094386442681716 is accurate to $1 0 ^ { - 1 6 }$ d. $p = { \frac { \ln ( 3 / 7 ) } { \ln ( 2 5 / 2 7 ) } }$

27. We have $P _ { L } = 2 6 5 8 1 6$ ， $c = - 0 . 7 5 6 5 8 1 2 5$ ，and $k = 0 . 0 4 5 0 1 7 5 0 2$ . The 1980 population is $P ( 3 0 ) = 2 2 2 , 2 4 8 , 3 2 0 ,$ and the 2010 population is $P ( 6 0 ) = 2 5 2 , 9 6 7 , 0 3 0$

29. Using $p _ { 0 } = 0 . 5$ and $p _ { 1 } = 0 . 9$ ,the Secant method gives $p _ { 5 } = 0 . 8 4 2$

# Exercise Set 2.4 (Page 85)

1. a. For $p _ { 0 } = 0 . 5$ ,we have $p _ { 1 3 } = 0 . 5 6 7 1 3 5$ b. For $p _ { 0 } = - 1 . 5$ ,we have $p _ { 2 3 } = - 1 . 4 1 4 3 2 5$

c. For $p _ { 0 } = 0 . 5$ ，we have $p _ { 2 2 } = 0 . 6 4 1 1 6 6$

d. For $p _ { 0 } = - 0 . 5$ ,we have $p _ { 2 3 } = - 0 . 1 8 3 2 7 4$

3. Newton's method with $p _ { 0 } = - 0 . 5$ gives $p _ { 1 3 } = - 0 . 1 6 9 6 0 7$ . Modifed Newton's method in Eq. (2.11) with $p _ { 0 } = - 0 . 5$ gives $p _ { 1 1 } = - 0 . 1 6 9 6 0 7$ ：

5. a. For $k > 0$ ，

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - 0 | } { | p _ { n } - 0 | } } = \operatorname* { l i m } _ { n \to \infty } { \frac { \frac { 1 } { ( n + 1 ) ^ { k } } } { \frac { 1 } { n ^ { k } } } } = \operatorname* { l i m } _ { n \to \infty } \left( { \frac { n } { n + 1 } } \right) ^ { k } = 1 ,
$$

so the convergence is linear.

b. We need to have $N > 1 0 ^ { m / k }$ .

7. Typical examples area. $p _ { n } = 1 0 ^ { - 3 ^ { n } }$ b. $p _ { n } = 1 0 ^ { - \alpha ^ { n } }$

9. This follows from the fact that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \left| { \frac { b - a } { 2 ^ { n + 1 } } } \right| } { \left| { \frac { b - a } { 2 ^ { n } } } \right| } } = { \frac { 1 } { 2 } } .
$$

11.If Pn+1-p $\begin{array} { r } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | ^ { 3 } } = 0 . 7 5 } \end{array}$ and $| p _ { 0 } - p | = 0 . 5$ ，then

$$
| p _ { n } - p | = ( 0 . 7 5 ) ^ { ( 3 ^ { n } - 1 ) / 2 } | p _ { 0 } - p | ^ { 3 ^ { n } } .
$$

To have $| p _ { n } - p | \leq 1 0 ^ { - 8 }$ requires that $n \geq 3$

# Exercise Set 2.5 (Page 90)

1. The results are listed in the following table.

<table><tr><td></td><td>a</td><td>b</td><td>C</td><td>d</td></tr><tr><td>Po</td><td>0.258684</td><td>0.907859</td><td>0.548101</td><td>0.731385</td></tr><tr><td></td><td>0.257613</td><td>0.909568</td><td>0.547915</td><td>0.736087</td></tr><tr><td>B</td><td>0.257536</td><td>0.909917</td><td>0.547847</td><td>0.737653</td></tr><tr><td>p</td><td>0.257531</td><td>0.909989</td><td>0.547823</td><td>0.738469</td></tr><tr><td>P4</td><td>0.257530</td><td>0.910004</td><td>0.547814</td><td>0.738798</td></tr><tr><td>ps</td><td>0.257530</td><td>0.910007</td><td>0.547810</td><td>0.738958</td></tr></table>

3. $p _ { \mathrm { 0 } } ^ { \mathrm { ( 1 ) } } = 0 . 8 2 6 4 2 7$   
5. $p _ { \downarrow } ^ { ( 0 ) } = 1 . 5$

7. For $g ( x ) = \sqrt { 1 + \frac { 1 } { x } }$ and $p _ { 0 } = 1$ ， we have $p _ { 3 } = 1 . 3 2 4 7 2$

9. For $\textstyle g ( x ) = 0 . 5 ( x + { \frac { 3 } { x } } )$ and $p _ { 0 } = 0 . 5$ ， we have $p _ { 4 } = 1 . 7 3 2 0 5$

[1. Aitken's $\Delta ^ { 2 }$ method gives:a. $\hat { p } _ { 1 0 } = 0 . 0 \overline { { 4 5 } }$ b. $\hat { p } _ { 2 } = 0 . 0 3 6 3$

13. We have

$$
{ \frac { | p _ { n + 1 } - p _ { n } | } { | p _ { n } - p | } } = { \frac { | p _ { n + 1 } - p + p - p _ { n } | } { | p _ { n } - p | } } = \left| { \frac { p _ { n + 1 } - p } { p _ { n } - p } } - 1 \right| ,
$$

so

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p _ { n } | } { | p _ { n } - p | } } = \operatorname* { l i m } _ { n \to \infty } \left| { \frac { p _ { n + 1 } - p } { p _ { n } - p } } - 1 \right| = 1 .
$$

15. a. Hint: First show that $\begin{array} { r } { p _ { n } - p = - \frac { 1 } { ( n + 1 ) ! } e ^ { \xi } x ^ { n + 1 } } \end{array}$ ,where $\pmb { \xi }$ is between O and 1.

<table><tr><td>b. n</td></tr><tr><td>0 1</td></tr><tr><td>3 1 2 2.75</td></tr><tr><td>2 2.5 2.72</td></tr><tr><td>3 2.6 2.71875</td></tr><tr><td>4 2.7083 2.7183</td></tr><tr><td>5 2.716 2.7182870</td></tr><tr><td>6 2.71805 2.7182823</td></tr><tr><td>7 2.7182539 2.7182818</td></tr><tr><td>8 2.7182787 2.7182818</td></tr><tr><td>9 2.7182815</td></tr><tr><td>10 2.7182818</td></tr></table>

# Exercise Set 2.6 (Page 99)

1. a. For $p _ { 0 } = 1$ ，we have $p _ { 2 2 } = 2 . 6 9 0 6 5$

b. For $p _ { 0 } = 1$ , we have $p _ { 5 } = 0 . 5 3 2 0 9$ ; for $p _ { 0 } = - 1$ ， we have $p _ { 3 } = - 0 . 6 5 2 7 0$ and for $p _ { 0 } = - 3$ , we have $p _ { 3 } = - 2 . 8 7 9 3 9$   
c. For $p _ { 0 } = 1$ ,we have $p _ { 5 } = 1 . 3 2 4 7 2$   
d. For $p _ { 0 } = 1$ ， we have $p _ { 4 } = 1 . 1 2 4 1 2$ ; and for $p _ { 0 } = 0$ ，we have $p _ { 8 } = - 0 . 8 7 6 0 5$   
e.For $p _ { 0 } = 0$ , we have $p _ { 6 } = - 0 . 4 7 0 0 6$ ; for $p _ { 0 } = - 1$ ， we have $p _ { 4 } = - 0 . 8 8 5 3 3$ ; and for $p _ { 0 } = - 3$ ，we have $p _ { 4 } = - 2 . 6 4 5 6 1$ ，   
f. For $p _ { 0 } = 0$ ， we have $p _ { 1 0 } = 1 . 4 9 8 1 9$

3.The following table lists the initial approximation and the roots.

<table><tr><td></td><td>Po</td><td>P1</td><td>P2</td><td>Approximate Roots</td><td>Complex Conjugate Roots</td></tr><tr><td>a</td><td>-1</td><td>0</td><td>1</td><td>P = -0.34532- 1.31873i</td><td>-0.34532 + 1.31873i</td></tr><tr><td></td><td>0</td><td>1</td><td>2</td><td>P6 = 2.69065</td><td></td></tr><tr><td>b</td><td>0</td><td>1</td><td>2</td><td>P6 = 0.53209</td><td></td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>P9 = -0.65270</td><td></td></tr><tr><td></td><td>-2</td><td>-3</td><td>-2.5</td><td>P4 = -2.87939</td><td></td></tr><tr><td>C</td><td>0</td><td>1</td><td>2</td><td>Ps = 1.32472</td><td></td></tr><tr><td></td><td>12</td><td>-1</td><td>0</td><td>P7 = -0.66236- 0.56228i</td><td>--0.66236 + 0.56228i</td></tr><tr><td>d</td><td>0</td><td>1</td><td>2</td><td>Ps = 1.12412</td><td></td></tr><tr><td></td><td>2</td><td>3</td><td>4</td><td>P12 = -0.12403+ 1.74096i</td><td>-0.12403- 1.74096i</td></tr><tr><td></td><td>12</td><td>0</td><td>-1</td><td>P5 = -0.87605</td><td></td></tr><tr><td>e</td><td>0</td><td>1</td><td>2</td><td>P10 = -0.88533</td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>-0.5</td><td>Ps = -0.47006</td><td></td></tr><tr><td></td><td>-1</td><td>-2</td><td>-3</td><td>Ps = -2.64561</td><td></td></tr><tr><td>f</td><td>0</td><td>1</td><td>2</td><td>P6 = 1.49819</td><td></td></tr><tr><td></td><td>-1</td><td>-2</td><td>13</td><td>P10 = -0.51363-1.09156i</td><td>-0.51363 + 1.09156i</td></tr><tr><td></td><td>1</td><td>0</td><td>-1</td><td>P8= 0.26454- 1.32837i</td><td>0.26454 + 1.32837i</td></tr></table>

5. a. The r00ts are 1.244, 8.847, and $- 1 . 0 9 1$ , and the critical points are O and 6. b. The r00ts are 0.5798,1.521, 2.332,and $- 2 . 4 3 2$ ,and the critical points are 1,2.001,and-1.5.

7. Let $c _ { 1 } = ( 2 + \textstyle { \frac { 2 } { 9 } } \sqrt { 1 2 9 } ) ^ { - 1 / 3 }$ and $c _ { 2 } = ( 2 + { \textstyle \frac { 2 } { 9 } } \sqrt { 1 2 9 } ) ^ { 1 / 3 }$ . The roots are $\begin{array} { r } { c _ { 2 } - \frac { 4 } { 3 } c _ { 1 } , - \frac { 1 } { 2 } c _ { 2 } + \frac { 2 } { 3 } c _ { 1 } + \frac { 1 } { 2 } \sqrt { 3 } ( c _ { 2 } + \frac { 4 } { 3 } c _ { 1 } ) i } \end{array}$ ,and $\begin{array} { r } { - \frac { 1 } { 2 } c _ { 2 } + \frac { 2 } { 3 } c _ { 1 } - \frac { 1 } { 2 } \sqrt { 3 } ( c _ { 2 } + \frac { 4 } { 3 } c _ { 1 } ) i } \end{array}$

9.The methods all find the solution 0.23235.

11. The minimal material is approximately $5 7 3 . 6 4 8 9 5 ~ \mathrm { c m } ^ { 2 }$

# Exercise Set 3.1 (Page 119)

1. a. $P _ { 1 } ( x ) = - 0 . 1 4 8 8 7 8 x + 1 ; P _ { 2 } ( x ) = - 0 . 4 5 2 5 9 2 x ^ { 2 } - 0 . 0 1 3 1 0 0 9 x + 1 ;$ $P _ { 2 } ( x ) = - 0 . 4 5 2 5 9 2 x ^ { 2 } - 0 . 0 1 3 1 0 0 9 x + 1 ; P _ { 1 } ( 0 . 4 5 ) = 0 . 9 3 3 0 0 5$ ；$\vert f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) \vert = 0 . 0 3 2 5 5 8 ; P _ { 2 } ( 0 . 4 5 ) = 0 . 9 0 2 4 5 5 ; \vert f ( 0 . 4 5 ) - \vert$ $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 2 0 0 8$ b. $P _ { 1 } ( x ) = 0 . 4 6 7 2 5 1 x + 1 ; \ P _ { 2 } ( x ) = - 0 . 0 7 8 0 0 2 6 x ^ { 2 } + 0 . 4 9 0 6 5 2 x + 1 ;$ $P _ { 1 } ( 0 . 4 5 ) = 1 . 2 1 0 2 6 3$ ；$| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 0 6 1 0 4 ; P _ { 2 } ( 0 . 4 5 ) = 1 . 2 0 4 9 9 8 ; | f ( 0 . 4 5 ) -$ $= 0 . 0 0 6 1 0 4 ; P _ { 2 } ( 0 . 4 5 ) = 1 . 2 0 4 9 9 8 ; | f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 0 8 3 9$ c. $P _ { 1 } ( x ) = 0 . 8 7 4 5 4 8 x ; P _ { 2 } ( x ) = - 0 . 2 6 8 9 6 1 x ^ { 2 } + 0 . 9 5 5 2 3 6 x ; P _ { 1 } ( 0 . 4 5 ) = 0 . 3 9 3 5 4 5 5 ^ { \circ }$ $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 2 1 2 9 8 3 ; P _ { 2 } ( 0 . 4 5 ) = 0 . 3 7 5 3 9 2$ ； $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 3 8 2 8$ d $P _ { 1 } ( x ) = 1 . 0 3 1 1 2 1 x ; P _ { 2 } ( x ) = 0 . 6 1 5 0 9 2 x ^ { 2 } + 0 . 8 4 6 5 9 3 x ;$ $P _ { 1 } ( 0 . 4 5 ) = 0 . 4 6 4 0 0 4$ ； $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 1 9 0 5 1 \cdot$ $P _ { 2 } ( 0 . 4 5 ) = 0 . 5 0 5 5 2 3$ ； $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 2 2 4 6 8$

<table><tr><td rowspan="7"></td><td>3. a. n</td><td>Xo, x1,...,Xn</td><td>P(8.4)</td></tr><tr><td>1 2</td><td>8.3, 8.6 8.3, 8.6, 8.7</td><td>17.87833 17.87716</td></tr><tr><td>3</td><td>8.3, 8.6, 8.7, 8.1</td><td>17.87714</td></tr><tr><td>c. n</td><td>Xo,X1,...,Xn</td><td>Pn(0.25)</td></tr><tr><td>1</td><td>0.2, 0.3</td><td>-0.13869287</td></tr><tr><td>2</td><td>0.2, 0.3, 0.4</td><td>-0.13259734</td></tr><tr><td>3</td><td>0.2, 0.3, 0.4, 0.1</td><td>-0.13277477</td></tr></table>

<table><tr><td>b. n</td><td>x0,x1,...,Xn</td><td>Pn(-1/3)</td></tr><tr><td>1</td><td>-0.5,-0.25</td><td>0.21504167</td></tr><tr><td>2</td><td>--0.5,-0.25, 0.0</td><td>0.16988889</td></tr><tr><td>3</td><td>-0.5,-0.25, 0.0, -0.75</td><td>0.17451852</td></tr></table>

<table><tr><td>d. n</td><td>Xo,x1,...,Xn</td><td>Pn (0.9)</td></tr><tr><td>1</td><td>0.8, 1.0</td><td>0.44086280</td></tr><tr><td>2</td><td>0.8, 1.0, 0.7</td><td>0.43841352</td></tr><tr><td>3</td><td>0.8, 1.0, 0.7, 0.6</td><td>0.44198500</td></tr></table>

5. $\begin{array} { r } { \sqrt { 3 } \approx P _ { 4 } \left( \frac { 1 } { 2 } \right) = 1 . 7 0 8 \overline { { 3 } } } \end{array}$

<table><tr><td>7. a. n</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td rowspan="5">1 2 c. n</td><td>0.00118 1.367 × 10-5</td><td>0.00120 1.452 × 10-5</td></tr><tr><td>Actual Error</td><td>Error Bound</td></tr><tr><td>I 5.9210 × 10-3</td><td></td></tr><tr><td>1 2</td><td>6.0971 × 10-3</td></tr><tr><td>1.7455 × 10-4</td><td>1.8128 × 10-4</td></tr></table>

<table><tr><td>b. n 1</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td rowspan="2">2 d. n</td><td>4.0523 × 10-2 4.6296 × 10-3</td><td>4.5153 × 10-2 4.6296 × 10-3</td></tr><tr><td>Actual Error</td><td>Error Bound</td></tr><tr><td rowspan="2"></td><td>1 2.7296 × 10-3</td><td>1.4080 × 10-2</td></tr><tr><td>2 5.1789 × 10-3</td><td>9.2215 × 10-3</td></tr></table>

9. $y = 4 . 2 5$

11. $f ( 1 . 0 9 ) \approx 0 . 2 8 2 6$ . The actual error is $4 . 3 \times 1 0 ^ { - 5 }$ , and an error bound is $7 . 4 \times 1 0 ^ { - 6 }$ . The discrepancy is due to the fact that the data are given to only four decimal places,and only four-digit arithmetic is used.

13. $P _ { 2 } = f ( 0 . 7 ) = 6 . 4$

15. a. $P _ { 2 } ( x ) = - 1 1 . 2 2 3 8 8 8 8 9 x ^ { 2 } + 3 . 8 1 0 5 0 0 0 0 x + 1$ ，and an error bound is O.11371294. b. $P _ { 2 } ( x ) = - 0 . 1 3 0 6 3 4 4 1 6 7 x ^ { 2 } + 0 . 8 9 6 9 9 7 9 3 3 5 x - 0 . 6 3 2 4 9$ 693,and an error bound is $9 . 4 5 7 6 2 \times 1 0 ^ { - 4 }$ c. $P _ { 3 } ( x ) = 0 . 1 9 7 0 0 5 6 6 6 7 x ^ { 3 } - 1 . 0 6 2 5 9 0 5 5 x ^ { 2 } + 2$ 2.532453189x -1.666868305,and an error bound is $1 0 ^ { - 4 }$ d. $P _ { 3 } ( x ) = - 0 . 0 7 9 3 2 x ^ { 3 } - 0 . 5 4 5 5 0 6 x ^ { 2 } + 1 . 0 0 6 5 9 9 2 x + 1$ , and an error bound is $1 . 5 9 1 3 7 6 \times 1 0 ^ { - 3 }$ .

[7. The largest possible step size is 0.004291932,so 0.04 would be a reasonable choice.

19. $P _ { 0 , 1 , 2 , 3 } ( 2 . 5 ) = 2 . 8 7 5$

21.The first ten terms of the sequence are 0.038462,0.333671,0.116605,-0.371760,-0.0548919,0.605935, 0.190249，-0.513353,-0.0668173,and 0.448335. Since $f ( 1 + \sqrt { 1 0 } ) = 0 . 0 5 4 5 7 1 6$ ,the sequence does not appear to converge.

25.a. Sample 1:P( $x \rangle = 6 . 6 7 - 4 2 . 6 4 3 4 x + 1 6 . 1 4 2 7 x ^ { 2 } - 2 . 0 9 4 6 4 x ^ { 3 } + 0 . 1 2 6 9 0 2 x ^ { 4 } - 0 . 0 0 3 6 7 1 6 8 x ^ { 5 } + 0 . 0 0 0 0 4$ 09458x6； Sample2: $P _ { 6 } ( x ) = 6 . 6 7 - 5 . 6 7 8 2 1 x + 2 . 9 1 2 8 1 x ^ { 2 } - 0 . 4$ 13799x+0.025 $8 4 1 3 x ^ { 4 } - 0 . 0 0 0 7 5 2 5 4 6 x ^ { 5 } + 0 . 0 0 0 0 0 8 3 6 1 6 0 x ^ { 6 }$ b. Sample $1 \colon 4 2 . 7 1 ~ \mathrm { m g } ;$ Sample 2 $\therefore 1 9 . 4 2 \mathrm { ~ m g }$

27. Since $g ( x ) = g ( x _ { 0 } ) = 0$ , there exists a number $\xi _ { 1 }$ between $x$ and $x _ { 0 }$ ,for which $g ^ { \prime } ( \xi _ { 1 } ) = 0$ Also, $g ^ { \prime } ( x _ { 0 } ) = 0$ ，s0 there exists a number $\xi _ { 2 }$ between $\scriptstyle x _ { 0 }$ and $\pmb { \xi } _ { 1 }$ ,for which $g ^ { \prime \prime } ( \xi _ { 2 } ) = 0$ . The process is continued by induction to show that a number $\xi _ { n + 1 }$ between $x _ { 0 }$ and $\xi _ { n }$ exists with $g ^ { ( n + 1 ) } ( \xi _ { n + 1 } ) = 0$ . The error formula for Taylor polynomials follows.

29. a. (i) $B _ { 3 } ( x ) = x \qquad ( \mathrm { i i } ) \ B _ { 3 } ( x ) = 1$

# Exercise Set 3.2 (Page 131)

1. a. $P _ { 1 } ( x ) = 1 6 . 9 4 4 1 + 3 . 1 0 4 1 ( x - 8 . 1 ) ; P _ { 1 } ( 8 . 4 ) = 1 7 . 8 7 5 3 3$ $P _ { 2 } ( x ) = P _ { 1 } ( x ) + 0 . 0 6 ( x - 8 . 1 ) ( x - 8 . 3 ) ; P _ { 2 } ( 8 . 4 ) = 1 7 . 8 7 7 1 3$ $P _ { 3 } ( x ) = P _ { 2 } ( x ) + - 0 . 0 0 2 0 8 3 3 3 ( x - 8 . 1 ) ( x - 8 . 3 ) ( x - 8 . 6 ) ; P _ { 3 } ( 8 . 4 $ ) = 17.87714b. $P _ { 1 } ( x ) = - 0 . 1 7 6 9 4 4 6 + 1 . 9 0 6 9 6 8 7 ( x - 0 . 6 ) ; P _ { 1 } ( 0 . 9 ) = 0 . 3 9 5 1 4 6$ $P _ { 2 } ( x ) = P _ { 1 } ( x ) + 0 . 9 5 9 2 2 4 ( x - 0 . 6 ) ( x - 0 . 7 )$ ； $P _ { 2 } ( 0 . 9 ) = 0 . 4 5 2 6 9 9 5$ $P _ { 3 } ( x ) = P _ { 2 } ( x ) - 1 . 7 8 5 7 4 1 ( x - 0 . 6 ) ( x - 0 . 7 ) ( x - 0 . 8 ) ; P _ { 3 } ( 0 . 9 ) = 0 . 4 4 1 9 8 5 0$

3. In the following equations, we have $\begin{array} { r } { s = \frac { 1 } { h } ( x - x _ { n } ) } \end{array}$ a. $P _ { 1 } ( s ) = 1 . 1 0 1 + 0 . 7 6 6 0 6 2 5 s ; ~ f ( - { \scriptstyle { \frac { 1 } { 3 } } } ) \approx P _ { 1 } ( - { \scriptstyle { \frac { 4 } { 3 } } } ) = 0 . 0 7 9 5 8 3 3 3$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 4 0 6 3 7 5 s ( s + 1 ) / 2$ ； $f ( - { \textstyle \frac { 1 } { 3 } } ) \approx P _ { 2 } ( - { \textstyle \frac { 4 } { 3 } } ) = 0 . 1 6 9 8 8 8 9$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 9 3 7 5 s ( s + 1 ) ( s + 2 ) / 6 ; \quad f ( - \textstyle { \frac { 1 } { 3 } } ) \approx P _ { 3 } ( - \textstyle { \frac { 4 } { 3 } } ) = 0 . 1 7 4 5$ b. $P _ { 1 } ( s ) = 0 . 2 4 8 4 2 4 4 + 0 . 2 4 1 8 2 3 5 s$ $f ( 0 . 2 5 ) \approx P _ { 1 } ( - 1 . 5 ) = - 0 . 1 1 4 3 1 0 8$ $P _ { 1 } ( s ) = P _ { 1 } ( s ) - 0 . 0 4 8 7 6 4 1 9 s ( s + 1 ) / 2 ; ~ f ( 0 . 2 5 ) \approx P _ { 2 } ( - 1 . 5 ) = - 0 . 1 3 2 5 9 7 3$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) - 0 . 0 0 2 8 3 8 9 1 s ( s + 1 ) ( s + 2 ) / 6 ; \quad f ( 0 . 2 5 ) \approx P _ { 3 } ( - 1 . 5 ) = - 0 . 1 3 2 ,$

5.a. $f ( 0 . 0 5 ) \approx 1 . 0 5 1 2 6$ b. $f ( 0 . 6 5 ) \approx 1 . 9 1 5 5 5 \mathrm { ~ \textbf ~ { ~ c ~ } ~ } f ( 0 . 4 3 ) \approx 1 . 5 3 7 2 5$

7. a. $P ( - 2 ) = Q ( - 2 ) = - 1$ ， $\cdot 1 ) = Q ( - 1 ) = 3 , P ( 0 ) = Q ( 0 ) = 1 , P ( 1 ) = Q ( 1 ) = - 1 , P ( - 1 ) = Q ( - 1 ) = 0$ $P ( 2 ) = Q ( 2 ) = 3$ b. The format of the polynomial is not unique. If $P ( x )$ and $Q ( x )$ are expanded, they are identical. There is only one interpolating polynomial if the degree is lessthan or equal to four for the given data. However, it can be expressed in various ways depending on the application.

9. The coefficient of $x ^ { 2 }$ is 3.5.

11. The approximation to $f ( 0 . 3 )$ should be increased by 5.9375.

13. $f [ x _ { 0 } ] = f ( x _ { 0 } ) = 1$ ， $f [ x _ { 1 } ] = f ( \pmb { x } _ { 1 } ) = 3$ ，f[xo，x]=5

$$
\begin{array} { c } { { { \scriptstyle \mathscr { f } [ x _ { 2 } ] = f [ x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ( x _ { 2 } - x _ { 0 } ) + a _ { 2 } ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) , } } } \\ { { { \scriptstyle f [ x _ { 2 } ] = f [ x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ( x _ { 2 } - x _ { 0 } ) + a _ { 2 } ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) , } } } \\ { { { \scriptstyle a _ { 2 } = \displaystyle \frac { f [ x _ { 2 } ] - f [ x _ { 0 } ] } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } - \displaystyle \frac { f [ x _ { 0 } , x _ { 1 } ] } { ( x _ { 2 } - x _ { 1 } ) } } } } \end{array}
$$

This simplifies to $f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$

17. Let $\begin{array} { r } { \tilde { P } ( x ) = f [ x _ { i _ { 0 } } ] + \sum _ { k = 1 } ^ { n } f [ x _ { i _ { 0 } } , \dotsc , x _ { i _ { k } } ] ( x - x _ { i _ { 0 } } ) \cdot \cdot \cdot ( x - x _ { i _ { k } } ) } \end{array}$ and $\begin{array} { r }  \mathfrak { s } ( x ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } f [ x _ { 0 } , \dotsc , x _ { k } ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k } ) . \ \mathrm { { ~ \} } } \end{array}$ The polynomial $\tilde { P } ( x )$ interpolates $f ( x )$ at the nodes $x _ { i _ { 0 } } , \ldots , x _ { i _ { n } }$ ,and the polynomial $\hat { P } ( x )$ interpolates $f ( x )$ at the nodes $x _ { 0 } , \ldots , x _ { n }$ . Since both sets of nodes are the same and the interpolating polynomial is unique, we have $\tilde { \pmb { P } } ( \pmb { x } ) = \hat { P } ( \pmb { x } )$ . The coefficient of $x ^ { n }$ in $\tilde { P } ( x )$ is $f \{ x _ { i _ { 0 } } , \ldots , x _ { i _ { n } } \} ,$ and the coefficient of $x ^ { n }$ in $\bar { \hat { P } } ( x )$ is $f [ x _ { 0 } , \ldots , x _ { n } ]$ . Thus, $f [ x _ { i _ { 0 } } , \dots , x _ { i _ { n } } ] = f [ x _ { 0 } , \dots , x _ { n } ]$

# Exercise Set 3.3 (Page 139)

1.The coefcients for the polynomials in divided-difference form are given in the following tables.For example,the polynomial in part (a) is

$$
H _ { 3 } ( x ) = 1 7 . 5 6 4 9 2 + 3 . 1 1 6 2 5 6 ( x - 8 . 3 ) + 0 . 0 5 9 4 8 ( x - 8 . 3 ) ^ { 2 } - 0 . 0 0 2 0 2 2 2 ( x - 8 . 3 ) ^ { 2 } ( x - 8 . 3 ) ^ { 3 }
$$

<table><tr><td>a</td><td>b</td><td>C</td><td>d</td></tr><tr><td>17.56492</td><td>0.22363362</td><td>-0.02475</td><td>-0.62049958</td></tr><tr><td>3.116256</td><td>2.1691753</td><td>0.751</td><td>3.5850208</td></tr><tr><td>0.05948</td><td>0.01558225</td><td>2.751</td><td>-2.1989182</td></tr><tr><td>-0.00202222</td><td>-3.2177925</td><td>1</td><td>-0.490447</td></tr><tr><td></td><td></td><td>0</td><td>0.037205</td></tr><tr><td></td><td></td><td>0</td><td>0.040475</td></tr><tr><td></td><td></td><td></td><td>-0.0025277777</td></tr><tr><td></td><td></td><td></td><td>0.0029629628</td></tr></table>

3. a. We have sin $0 . 3 4 \approx H _ { 5 } ( 0 . 3 4 ) = 0 . 3 3 3 4 9$

b. The formula gives an error bound of $3 . 0 5 \times 1 0 ^ { - 1 4 }$ , but the actual error is $2 . 9 1 \times 1 0 ^ { - 6 }$ . The discrepancy is due tc the fact that the data are given to only five decimal places.

c. We have s $\mathrm { i n } 0 . 3 4 \approx H _ { 7 } ( 0 . 3 4 ) = 0 . 3 3 3 5 0$ Although the error bound is now $5 . 4 \times 1 0 ^ { - 2 0 }$ , the accuracy of the given data dominates the calculations. This result is actually less accurate than the approximation in part (b), since sin $0 . 3 4 = 0 . 3 3 3 4 8 7$

5. For 2(a), we have an error bound of $5 . 9 \times 1 0 ^ { - 8 }$ . The error bound for 2(c) is O since $f ^ { ( n ) } ( x ) \equiv 0$ ,for $n > 3$

7. The Hermite polynomial generated from these data is

$$
\begin{array} { l } { { \scriptstyle : + 0 . 2 2 2 2 2 2 x ^ { 2 } ( x - 3 ) - 0 . 0 3 1 1 1 1 1 x ^ { 2 } ( x - 3 ) ^ { 2 } - 0 . 0 0 6 4 4 4 4 4 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) } } \\ { { \scriptstyle : 0 . 0 0 2 2 6 3 8 9 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } - 0 . 0 0 0 9 1 3 1 9 4 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) } } \\ { { \scriptstyle \ : - 0 . 0 0 0 1 3 0 5 2 7 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) ^ { 2 } - 0 . 0 0 0 0 2 0 2 2 3 6 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) ^ { 2 } ( x - 1 ) } } \end{array}
$$

a. The Hermite polynomial predicts a position of $H _ { 9 } ( 1 0 ) = 7 4 3$ ft and a speed of $H _ { 9 } ^ { \prime } ( 1 0 ) = 4 8$ ft/s. Although the position approximation is reasonable, the low speed prediction is suspect.

b. To find the first time the speed exceds $5 5 \ \mathrm { m i h } = 8 0 . { \overline { { 6 } } }$ ft/s,we solve for the smallest value of $t$ in the equation $8 0 . { \overline { { 6 } } } = H _ { 9 } ^ { \prime } ( x )$ . This gives $x \approx 5 . 6 4 8 8 0 9 2$

c. The estimated maximum speed is $H _ { 9 } ^ { \prime } ( 1 2 . 3 7 1 8 7 ) = 1 1 9 . 4 2 3 { \mathrm { ~ f } } \mathrm { { u } } \approx 8 1 . 4 2 5 { \mathrm { ~ m i } } / \mathrm { { h } } .$

9. Let

$$
H ( x ) = f [ z _ { 0 } ] + f [ z _ { 0 } , z _ { 1 } ] ( x - x _ { 0 } ) + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] ( x - x _ { 0 } ) ^ { 2 } + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 } ] ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 0 } ) ^ { 3 } ,
$$

Substituting $f [ z _ { 0 } ] = f ( x _ { 0 } ) , f [ z _ { 0 } , z _ { 1 } ] = f ^ { \prime } ( x _ { 0 } )$ ，

$$
\begin{array} { c } { { f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] = \displaystyle \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } } } \\ { { f [ z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 } ] = \displaystyle \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } } } \end{array}
$$

into $H ( x )$ and simplifying gives

$$
H ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 2 } } } ( x - x _ { 0 } ) ^ { 2 }
$$

$$
+ \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) .
$$

Thus, $H ( x _ { 0 } ) = f ( x _ { 0 } )$ and

$$
\begin{array} { l } { { H ( x _ { 1 } ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) + [ f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) ] } } \\ { { \ ~ } } \\ { { \ = f ( x _ { 1 } ) . } } \end{array}
$$

Further,

$$
{ \begin{array} { r l } & { \ = f ^ { \prime } ( x _ { 0 } ) + 2 { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 2 } } } ( x - x _ { 0 } ) } \\ & { \quad \ + \ { \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } } [ 2 ( x - x _ { 0 } ) ( x - x _ { 1 } ) + ( x - x _ { 0 } ) ^ { 2 } } \end{array} }
$$

so

$$
\begin{array} { r l } & { H ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } ) \quad \mathrm { a n d } } \\ & { H ^ { \prime } ( x _ { 1 } ) = f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 f ( x _ { 1 } ) } { x _ { 1 } - x _ { 0 } } - \frac { 2 f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } - 2 f ^ { \prime } ( x _ { 0 } ) + f ^ { \prime } ( x _ { 1 } ) - \displaystyle \frac { 2 f ( x _ { 1 } ) } { x _ { 1 } - x _ { 0 } } + \frac { 2 f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } + f ^ { \prime } ( x _ { 0 } ) } \\ & { \qquad = f ^ { \prime } ( x _ { 1 } ) . } \end{array}
$$

Thus, $H$ satisfies the requirements of the cubic Hermite polynomial $H _ { 3 }$ , and the uniqueness of $H _ { 3 }$ implies thal $H _ { 3 } = H$

# Exercise Set 3.4 (Page 152)

1. $S ( x ) = x$ on [0,2]

3.The equations of the respective free cubic splines are

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $\pmb { x }$ in $[ x _ { i } , x _ { i + 1 } ]$ ， where the coefficients are given in the following tables.

<table><tr><td>a. i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17.564920</td><td>3.13410000</td><td>0.00000000</td><td>0.00000000</td></tr></table>

<table><tr><td>b. i</td><td>ai</td><td>bi</td><td>Ci</td><td>d</td></tr><tr><td>0</td><td>0.22363362</td><td>2.17229175</td><td>0.00000000</td><td>0.00000000</td></tr></table>

<table><tr><td>c.i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.02475000</td><td>1.03237500</td><td>0.00000000</td><td>6.50200000</td></tr><tr><td>1</td><td>0.33493750</td><td>2.25150000</td><td>4.87650000</td><td>-6.50200000</td></tr><tr><td>d.i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.62049958</td><td>3.45508693</td><td>0.00000000</td><td>-8.9957933</td></tr><tr><td>1</td><td>-0.28398668</td><td>3.18521313</td><td>-2.69873800</td><td>-0.94630333</td></tr><tr><td>2</td><td>0.00660095</td><td>2.61707643</td><td>-2.98262900</td><td>9.9420966</td></tr></table>

5. The equations of the respective clamped cubic splines are

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ ， where the coefficients are given in the following tables.

<table><tr><td></td><td>a.i</td><td>ai</td><td>bi</td><td>Ci</td><td>d</td></tr><tr><td rowspan="5"></td><td>0</td><td>17.564920</td><td>3.1162560</td><td>0.0600867</td><td>-0.00202222</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b. i</td><td>ai</td><td>bi</td><td>Ci</td><td>d</td></tr><tr><td>0</td><td>0.22363362</td><td>2.1691753</td><td>0.65914075</td><td>-3.2177925</td></tr><tr><td>i</td><td></td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td rowspan="6">d.</td><td></td><td>ai</td><td></td><td></td><td></td></tr><tr><td>0</td><td>-0.02475000</td><td>0.75100000</td><td>2.5010000</td><td>,1.0000000</td></tr><tr><td>1</td><td>0.33493750</td><td>2.18900000</td><td>3.2510000</td><td>1.0000000</td></tr><tr><td>i</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>a</td><td>b</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.62049958</td><td>3.5850208</td><td>-2.1498407</td><td>-0.49077413</td></tr><tr><td></td><td>1</td><td>-0.28398668</td><td>3.1403294</td><td>-2.2970730</td><td>-0.47458360</td></tr><tr><td>2</td><td></td><td>0.006600950</td><td>2.6666773</td><td>--2.4394481</td><td>--0.44980146</td></tr></table>

7. $b = - 1$ ， $c = - 3 , d = 1$ 9. $\begin{array} { r } { B = \frac { 1 } { 4 } } \end{array}$ ， $\begin{array} { r } { D = \frac { 1 } { 4 } } \end{array}$ ， $\begin{array} { r } { b = - \frac { 1 } { 2 } } \end{array}$ ， $\begin{array} { r } { d = \frac { 1 } { 4 } } \end{array}$

11. The equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ ，where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.0</td><td>-0.7573593</td><td>0.0</td><td>-6.627417</td></tr><tr><td>0.25</td><td>0.7071068</td><td>-2.0</td><td>-4.970563</td><td>6.627417</td></tr><tr><td>0.5</td><td>0.0</td><td>-3.242641</td><td>0.0</td><td>6.627417</td></tr><tr><td>0.75</td><td>-0.7071068</td><td>-2.0</td><td>4.970563</td><td>-6.627417</td></tr></table>

$\begin{array} { r } { \int _ { 0 } ^ { 1 } S ( x ) d x = 0 . 0 0 0 0 0 0 } \end{array}$ $S ^ { \prime } ( 0 . 5 ) = - 3 . 2 4 2 6 4$ ,and $S ^ { \prime \prime } ( 0 . 5 ) = 0 . 0$

13. The equation of the spline is

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ ， where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.0</td><td>0.0</td><td>-5.193321</td><td>2.028118</td></tr><tr><td>0.25</td><td>0.7071068</td><td>-2.216388</td><td>-3.672233</td><td>4.896310</td></tr><tr><td>0.5</td><td>0.0</td><td>-3.134447</td><td>0.0</td><td>4.896310</td></tr><tr><td>0.75</td><td>-0.7071068</td><td>-2.216388</td><td>3.672233</td><td>2.028118</td></tr></table>

$\begin{array} { r } { \int _ { 0 } ^ { 1 } s ( x ) d x = 0 . 0 0 0 0 0 0 } \end{array}$ $s ^ { \prime } ( 0 . 5 ) = - 3 . 1 3 4 4 5$ and $s ^ { \prime \prime } ( 0 . 5 ) = 0 . 0$

15. Let $f ( x ) = a + b x + c x ^ { 2 } + d x ^ { 3 }$ . Clearly, $f$ satisfies properties (a), (c),(d),and (e)of Definition 3.10and $f$ interpolates itself for any choice of $x _ { 0 } , \ldots , x _ { n }$ Since (ii) of property(f) in Definition3.10 holds, $f$ must be its own clamped cubic spline. However, $f ^ { \prime \prime } ( x ) = 2 c + 6 d x$ can be zero only at $x = - c / 3 d$ . Thus, part (i) of property (f) in Definition 3.10 cannot hold at two values $x _ { 0 }$ and $x _ { n }$ . Thus, $f$ cannot be a natural cubic spline.

17. The piecewise linear approximation to $f$ is given by

$$
F ( x ) = \left\{ \begin{array} { l l } { 2 0 ( e ^ { 0 . 1 } - 1 ) x + 1 , } & { \mathrm { f o r ~ } x \mathrm { ~ i n ~ } [ 0 , 0 . 0 5 ] } \\ { 2 0 ( e ^ { 0 . 2 } - e ^ { 0 . 1 } ) x + 2 e ^ { 0 . 1 } - e ^ { 0 . 2 } , } & { \mathrm { f o r ~ } x \mathrm { ~ i n ~ } ( 0 . 0 5 , 1 ] . } \end{array} \right.
$$

We have

$$
\int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x = 0 . 1 1 0 7 9 3 6 \quad { \mathrm { ~ a n d ~ } } \int _ { 0 } ^ { 0 . 1 } f ( x ) \ d x = 0 . 1 1 0 7 0 1 4 .
$$

21. a.On [0,0.05], we have $s ( x ) = 1 . 0 0 0 0 0 0 + 1 . 9 9 9 9 9 9 x + 1 . 9 9 8 3 0 2 x ^ { 2 } + 1 . 4 0 1 3 1 0 x ^ { 3 } .$ ,and on (0.05,0.1], we have s(x)= 1.105170 $+ 2 . 2 1 0 3 4 0 ( x - 0 . 0 5 ) + 2 . 2 0 8 4 9 8 ( x - 0 . 0 5 ) ^ { 2 } + 1 . 5 4 8 7 5 8 ( x - 0 . 0 5 ) ^ { 2 }$ b. $\begin{array} { r } { \int _ { 0 } ^ { 0 . 1 } s ( x ) \ d x = 0 . 1 1 0 7 0 1 } \end{array}$ c. 1.6 × 10-7 d. On [0,0.05], we have $S ( x ) = 1 + 2 . 0 4 8 1 1 x + 2 2 . 1 2 1 8 4 x ^ { 3 }$ ,and on (0.05,0.1], we have $S ( x ) = 1 . 1 0 5 1 7 1 + 2 . 2 1 4 0 2 8 ( x - 0 . 0 5 ) + 3 . 3 1 8 2 7 7 ( x - 0 . 0 5 ) ^ { 2 } - 2 2 . 1 2 1 8 4 ( x - 0 . 0 5 ) ^ { 3 } . \ 3$ $S ( 0 . 0 2 ) = 1 . 0 4 1 1 3 9$ and $S ( 0 . 0 2 ) = 1 . 0 4 0 8 1 1$

23.

$$
S ( x ) = \left\{ \begin{array} { l l } { 2 x - x ^ { 2 } , } & { 0 \leq x \leq 1 } \\ { 1 + ( x - 1 ) ^ { 2 } , } & { 1 \leq x \leq 2 } \end{array} \right.
$$

25.The spline has the equation

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $\{ x _ { i } , x _ { i + 1 } \}$ ， where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>0</td><td>75</td><td>-0.659292</td><td>0.219764</td></tr><tr><td>3</td><td>225</td><td>76.9779</td><td>1.31858</td><td>-0.153761</td></tr><tr><td>5</td><td>383</td><td>80.4071</td><td>0.396018</td><td>-0.177237</td></tr><tr><td>8</td><td>623</td><td>77.9978</td><td>-1.19912</td><td>0.0799115</td></tr></table>

The spline predicts a position of $s ( 1 0 ) = 7 7 4 . 8 4$ ft and a speed of $s ^ { \prime } ( 1 0 ) = 7 4 . 1 6$ fl/s. To maximize the speed, we find the single critical point of ${ \pmb { s } } ^ { \prime } ( { \pmb x } )$ , and compare the values of $s ( x )$ at this point and the endpoints.We find that max $s ^ { \prime } ( x ) = s ^ { \prime } ( 5 . 7 4 4 8 ) = 8 0 . 7$ ft $\mathit { \check { s } } = 5 5 . 0 2 \mathrm { \ m i } \mathrm { \ l }$ . The speed $\lvert 5 5 \mathrm { \ m i n }$ was first exceeded at approximately $5 . 5 \mathrm { ~ \bf ~ s ~ }$

27.The equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ ， where the coefficients are given in the following table.

Sample 1   
Sample 2   

<table><tr><td>xi</td><td>a</td><td>bi</td><td>Ci</td><td>d</td><td>ai</td><td>bi</td><td>Ci</td><td>d</td></tr><tr><td>0</td><td>6.67</td><td>-0.44687</td><td>0</td><td>0.06176</td><td>6.67</td><td>1.6629</td><td>0</td><td>-0.00249</td></tr><tr><td>6</td><td>17.33</td><td>6.2237</td><td>1.1118</td><td>-0.27099</td><td>16.11</td><td>1.3943</td><td>-0.04477</td><td>-0.03251</td></tr><tr><td>10</td><td>42.67</td><td>2.1104</td><td>-2.1401</td><td>0.28109</td><td>18.89</td><td>-0.52442</td><td>-0.43490</td><td>0.05916</td></tr><tr><td>13</td><td>37.33</td><td>-3.1406</td><td>0.38974</td><td>-0.01411</td><td>15.00</td><td>-1.5365</td><td>0.09756</td><td>0.00226</td></tr><tr><td>17</td><td>30.10</td><td>-0.70021</td><td>0.22036</td><td>-0.02491</td><td>10.56</td><td>-0.64732</td><td>0.12473</td><td>-0.01113</td></tr><tr><td>20</td><td>29.31</td><td>-0.05069</td><td>-0.00386</td><td>0.00016</td><td>9.44</td><td>-0.19955</td><td>0.02453</td><td>-0.00102</td></tr></table>

29. The three natural splines have equations of the form

$$
S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the values of the coefficients are given in the following tables.   

<table><tr><td colspan="6">Spline 1</td></tr><tr><td>i</td><td>Xi</td><td>ai= f(xi）</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>0.786</td><td>0.0</td><td>-0.086</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td>0.529</td><td>-0.257</td><td>0.034</td></tr><tr><td>2</td><td>5</td><td>3.9</td><td>-0.086</td><td>0.052</td><td>0.334</td></tr><tr><td>3</td><td>6</td><td>4.2</td><td>1.019</td><td>1.053</td><td>-0.572</td></tr><tr><td>4</td><td>7</td><td>5.7</td><td>1.408</td><td>-0.664</td><td>0.156</td></tr><tr><td>5</td><td>8</td><td>6.6</td><td>0.547</td><td>-0.197</td><td>0.024</td></tr><tr><td>6</td><td>10</td><td>7.1</td><td>0.049</td><td>-0.052</td><td>-0.003</td></tr><tr><td>7</td><td>13</td><td>6.7</td><td>-0.342</td><td>-0.078</td><td>0.007</td></tr><tr><td>8</td><td>17</td><td>4.5</td><td></td><td></td><td></td></tr><tr><td colspan="6">Spline 2</td></tr><tr><td>i</td><td>xi</td><td>ai = f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17</td><td>4.5</td><td>1.106</td><td>0.0</td><td>-0.030</td></tr><tr><td>1</td><td>20</td><td>7.0</td><td>0.289</td><td>-0.272</td><td>0.025</td></tr><tr><td>2</td><td>23</td><td>6.1</td><td>-0.660</td><td>-0.044</td><td>0.204</td></tr><tr><td>3</td><td>24</td><td>5.6</td><td>-0.137</td><td>0.567</td><td>-0.230</td></tr><tr><td>4</td><td>25</td><td>5.8</td><td>0.306</td><td>-0.124</td><td>-0.089</td></tr><tr><td>5</td><td>27</td><td>5.2</td><td>-1.263</td><td>-0.660</td><td>0.314</td></tr><tr><td>6</td><td>27.7</td><td>4.1</td><td></td><td></td><td></td></tr><tr><td colspan="6"></td></tr><tr><td>i xi</td><td></td><td>ai= f(xi）</td><td>Spline 3 bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>27.7</td><td>4.1</td><td>0.749</td><td>0.0</td><td>-0.910</td></tr><tr><td>1</td><td>28</td><td>4.3</td><td>0.503</td><td>-0.819</td><td>0.116</td></tr><tr><td>2</td><td>29</td><td>4.1</td><td>-0.787</td><td>-0.470</td><td>0.157</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>30</td><td>3.0</td><td></td><td></td><td></td></tr></table>

# Exercise Set 3.5 (Page 162)

1. a. $x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , y ( t ) = - 2 t ^ { 3 } + 3 t ^ { 2 } + t$ b. $x ( t ) = - 1 0 t ^ { 3 } + 1 4 . 5 t ^ { 2 } + 0 . 5 t$ ，y(t)= -3r³+ 4.5t² +0.5t c. $x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , \quad y ( t ) = - 4 t ^ { 3 } + 5 t ^ { 2 } + t$ d. $x ( t ) = - 1 0 t ^ { 3 } + 1 3 t ^ { 2 } + 2 t , y ( t ) = 2 t$

3.a. b. $\begin{array} { l } { x ( t ) = - 1 1 . 5 t ^ { 3 } + 1 5 t ^ { 2 } + 1 . 5 t + 1 , y ( t ) = - 4 . 2 5 t ^ { 3 } + 4 . 5 t ^ { 2 } + 0 . 7 5 t + 1 } \\ { x ( t ) = - 6 . 2 5 t ^ { 3 } + 1 0 . 5 t ^ { 2 } + 0 . 7 5 t + 1 , y ( t ) = - 3 . 5 t ^ { 3 } + 3 t ^ { 2 } + 1 . 5 t + 1 } \end{array}$ c. For $t$ between $( 0 , 0 )$ and (4,6),we have

$$
x ( t ) = - 5 t ^ { 3 } + 7 . 5 t ^ { 2 } + 1 . 5 t , y ( t ) = - 1 3 . 5 t ^ { 3 } + 1 8 t ^ { 2 } + 1 . 5 t ,
$$

and for $t$ between (4,6) and (6,1),we have

$$
x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t + 4 , y ( t ) = 4 t ^ { 3 } - 6 t ^ { 2 } - 3 t + 6 .
$$

d. For t between $( 0 , 0 )$ and (2,1),we have

$$
x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t , y ( t ) = - 0 . 5 t ^ { 3 } + 1 . 5 t ,
$$

for $t$ between (2,1) and (4,0),we have

$$
x ( t ) = - 4 t ^ { 3 } + 3 t ^ { 2 } + 3 t + 2 , \quad y ( t ) = - t ^ { 3 } + 1 ,
$$

and for $t$ between (4,0） and $( 6 , - 1 )$ ，we have

$$
x ( t ) = - 8 . 5 t ^ { 3 } + 1 3 . 5 t ^ { 2 } - 3 t + 4 , y ( t ) = - 3 . 2 5 t ^ { 3 } + 5 . 2 5 t ^ { 2 } - 3 t .
$$

# Exercise Set 4.1 (Page 175)

l.From the forward-backward difference formula (4.1),we have the following approximations:

$$
\begin{array} { r } { 1 . 5 ) \approx 0 . 8 5 2 0 , ~ f ^ { \prime } ( 0 . 6 ) \approx 0 . 8 5 2 0 , ~ f ^ { \prime } ( 0 . 7 ) \approx 0 . 7 9 6 0 } \\ { 1 . 0 ) \approx 3 . 7 0 7 0 , ~ f ^ { \prime } ( 0 . 2 ) \approx 3 . 1 5 2 0 , ~ f ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 2 0 } \end{array}
$$

3.Forthe endpoints of the tables,we use Formula (4.4).The other approximations come from Formula (4.5).

a. f'(1.1) \~ 17.769705, f'(1.2)≈ 22.193635,f'(1.3)\~ 27.107350,f'(1.4) \~32.150850 b. $f ^ { \prime } ( 8 . 1 ) \approx 3 . 0 9 2 0 5 0$ ， $f ^ { \prime } ( 8 . 3 ) \approx 3 . 1 1 6 1 5 0 ,$ $f ^ { \prime } ( 8 . 5 ) \approx 3 . 1 3 9 9 7 5$ ， $f ^ { \prime } ( 8 . 7 ) \approx 3 . 1 6 3 5 2 5$ c. $f ^ { \prime } ( 2 . 9 ) \approx 5 . 1 0 1 3 7 5$ ， $f ^ { \prime } ( 3 . 0 ) \approx 6 . 6 5 4 7 8 5$ ， $f ^ { \prime } ( 3 . 1 ) \approx 8 . 2 1 6 3 3 0$ $f ^ { \prime } ( 3 . 2 ) \approx 9 . 7 8 6 0 1 0$ d. $f ^ { \prime } ( 2 . 0 ) \approx 0 . 1 3 5 3 3 1 5 0$ ， $f ^ { \prime } ( 2 . 1 ) \approx - 0 . 0 9 9 8 9 5 5 0 , \ f ^ { \prime } ( 2 . 2 ) \approx - 0 . 3 2 9 8 9 6 0 , \ f ^ { \prime } ( 2 . 3 ) \approx - 0 . 5 5 4 6 7 0 0$ 5. The approximations and the formulas used are:

a. $f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 9 9 3 4 4$ from (4.7） $f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 7 6 8 7 6$ from (4.7) $f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 7 0 4$ from (4.6) $f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 7 7 5 6$ from (4.6) f'(2.5) \~ 1.544210 fr0m (4.7) $f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 5 5 4 9 6$ from (4.7) b. $f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 7 7 3 5 8$ from(4.7） $f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 8 9 3 3 \ \mathrm { f r o m }$ (4.7) $f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 8 8 4$ from (4.6) $f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 2 2 3$ from (4.6） $f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 3 9 9 1 1 ~ .$ from (4.7) $f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 2 8 8 5 3$ from (4.7)

7. $\begin{array} { r } { f ^ { \prime } ( 3 ) \approx \frac { 1 } { 1 2 } [ f ( 1 ) - 8 f ( 2 ) + 8 f ( 4 ) - f ( 5 ) ] = 0 . 2 1 0 6 2 } \end{array}$ ，with an error bound given by

$$
\operatorname* { m a x } _ { 1 \leq x \leq 5 } \frac { \vert f ^ { ( 5 ) } ( x ) \vert h ^ { 4 } } { 3 0 } \leq \frac { 2 3 } { 3 0 } = 0 . 7 \overline { { 6 } } .
$$

9.From the forward-backward difference formula (4.1),we have the following approximations:

$$
\begin{array} { r l } & { f ^ { \prime } ( 0 . 5 ) \approx 0 . 8 5 2 , \ f ^ { \prime } ( 0 . 6 ) \approx 0 . 8 5 2 , \ f ^ { \prime } ( 0 . 7 ) \approx 0 . 7 9 6 0 } \\ & { f ^ { \prime } ( 0 . 0 ) \approx 3 . 7 0 7 , \ f ^ { \prime } ( 0 . 2 ) \approx 3 . 1 5 3 , \ f ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 3 } \end{array}
$$

11.For the endpoints of the tables, we use Formula (4.7).The other approximations come from Formula (4.6).

a. $f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 8 4$ $\begin{array} { r l } & { f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 9 6 \quad f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 \quad f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 6 \quad f ^ { \prime } ( 2 . 5 ) \approx 1 . 5 5 0 \quad f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 6 , } \\ & { 3 \quad f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 7 \quad f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 \quad f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 \quad f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 4 } \end{array}$ b. $f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 8 3$ $f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 7 5$

13. The approximation is $- 4 . 8 \times 1 0 ^ { - 9 }$ $f ^ { \prime \prime } ( 0 . 5 ) = 0$ . The error bound is 0.35874. The method is very accurate since the function is symmetric about $x = 0 . 5$

15. a. ${ f ^ { \prime } ( 0 . 2 ) \approx - 0 . 1 9 5 1 0 2 7 \quad \mathbf { b . } ~ f ^ { \prime } ( 1 . 0 ) \approx - 1 . 5 4 1 4 1 5 \quad \mathbf { c . } ~ f ^ { \prime } ( 0 . 6 ) \approx - 0 . 6 8 2 4 1 7 5 }$

17. $f ^ { \prime } ( 0 . 4 ) \approx - 0 . 4 2 4 9 8 4 0$ and $f ^ { \prime } ( 0 . 8 ) \approx - 1 . 0 3 2 7 7 2$

19.The three-point formulas give the results in the following table.

$$
\frac { \mathrm { T i m e } } { \mathrm { S p e e d } } \quad \left| \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c }  { } & { 0 } & { } & { } & { 3 } & { } & { } & { 5 } & { } & { } & { 8 } & { } & { } & { 1 0 } & { } & { 1 3 } & { } \\ { } & { 7 9 } & { } & { } & { 8 2 . 4 } & { } & { } & { 7 4 . 2 } & { } & { } & { 7 6 . 8 } & { } & { 6 9 . 4 } & { } & { 7 1 . 2 } & { } & { } & { } \end{array} \right|
$$

21. The approximations eventually become zero since the numerator becomes zero.

23. Since $e ^ { \prime } ( h ) = - \varepsilon / h ^ { 2 } + h M / 3$ ， we have $e ^ { \prime } ( h ) = 0$ if and only if $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ Also, $e ^ { \prime } ( h ) < 0$ if $h < \sqrt [ 3 ] { 3 \varepsilon / M }$ and $e ^ { \prime } ( h ) > 0$ if $h > \sqrt [ 3 ] { 3 \varepsilon / M }$ , so an absolute minimum for $e ( h )$ occurs at $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ ，

# Exercise Set 4.2 (Page 184)

1. a. $f ^ { \prime } ( 1 ) \approx 1 . 0 0 0 0 1 0 9$ b. $f ^ { \prime } ( 0 ) \approx 2 . 0 0 0 0 0 0 0$ c. $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 7 5 1 4 5 9$ d. $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 4 6 7 9 9$

3.a. $f ^ { \prime } ( 1 ) \approx 1 . 0 0 1$ b. $f ^ { \prime } ( 0 ) \approx 1 . 9 9 9$ c. $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 8 3$ d. $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 1$

5. $\begin{array} { r } { \int _ { 0 } ^ { \pi } \sin x \ d x \approx 1 . 9 9 9 9 9 9 9 } \end{array}$

9. $\begin{array} { r } { N _ { 2 } ( h ) = N \left( \frac { h } { 3 } \right) + \left( \frac { N \left( \frac { h } { 3 } \right) - N ( h ) } { 2 } \right) } \end{array}$ and $\begin{array} { r } { N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 3 } \right) + \left( \frac { N _ { 2 } \left( \frac { h } { 3 } \right) - N _ { 2 } ( h ) } { 8 } \right) } \end{array}$ Ten $N _ { 3 } ( h )$ B an $O ( h ^ { 3 } )$ apriain $M$

11. Let $N ( h ) = ( 1 + h ) ^ { 1 / h }$ ， $\begin{array} { r } { N _ { 2 } ( h ) = 2 N \left( \frac { h } { 2 } \right) - N ( h ) , N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 3 } ( N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) ) . } \end{array}$ a. $N ( 0 . 0 4 ) = 2 . 6 6 5 8 3 6 3 3 1 , N ( 0 . 0 2 ) = 2 . 6 9 1 5 8 8 0 2 9 , N ( 0 . 0 1 ) = 2 . 7 0 4 8$ 13829 b. $N _ { 2 } ( 0 . 0 4 ) = 2 . 7 1 7 3 3 9 7 2 7 , N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 0 3 9 6 2 9 . \ ^ { \prime }$ The $O ( h ^ { 3 } )$ approximation is $N _ { 3 } ( 0 . 0 4 ) = 2 . 7 1 8 2 7 2 9 3 1$ c. Yes,since the errors seem proportioned to $h$ for $N ( h )$ ，to $h ^ { 2 }$ for $N _ { 2 } ( h )$ ,and to $h ^ { 3 }$ for $N _ { 3 } ( h )$

<table><tr><td rowspan=3 colspan=1>15.c.kPkP</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>512</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>3.0614675</td><td rowspan=1 colspan=1>3.1214452</td><td rowspan=1 colspan=1>3.1365485</td><td rowspan=1 colspan=1>3.1403312</td><td rowspan=1 colspan=1>3.1412723</td><td rowspan=1 colspan=1>3.1415138</td><td rowspan=1 colspan=1>3.1415729</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3.3137085</td><td rowspan=1 colspan=1>3.1825979</td><td rowspan=1 colspan=1>3.1517249</td><td rowspan=1 colspan=1>3.144184</td><td rowspan=1 colspan=1>3.1422236</td><td rowspan=1 colspan=1>3.1417504</td><td rowspan=1 colspan=1>3.1416321</td></tr></table>

e. Values of $p _ { k }$ and $P _ { k }$ are given in the following tables,together with the extrapolation results Forpk-

2.8284271   
3.0614675 3.1391476   
3.1214452 3.1414377 3.1415904   
3.1365485 3.1415829 3.1415926 3.1415927   
3.1403312 3.1415921 3.1415927 3.1415927 3.1415927

）r $P _ { k }$ 1 4 3.3137085 3.0849447 3.1825979 3.1388943 3.1424910 3.1517249 3.1414339 3.1416032 3.1415891 3.1441184 3.1415829 3.1415928 3.1415926 3.1415927

# Exercise Set 4.3 (Page 195)

1.The Trapezoidal rule gives the folowing approximations.a.0.265625b.-0.2678571 c.-0.17776434

3.Simpson's rule gives the following approximations.a. 0.1940104b. -0.2670635c. 0.19224 d. 0.16240168 e. -0.7391053 f. -0.1768216g. 0.1513826 h. 2.5836964

5.The Midpoint rule gives the following approximations.a. 0.1582031b.-0.2666667 c. 0.1743309 d. 0.1516327 e. -0.6753247f. -0.1768200g. 0.1180292 h. 1.8039148

7. $\begin{array} { r } { f ( 1 ) = \frac { 1 } { 2 } } \end{array}$

9. The degree of precision is 3.

11. $\begin{array} { r } { c _ { 0 } = \frac { 1 } { 3 } , c _ { 1 } = \frac { 4 } { 3 } , c _ { 2 } = \frac { 1 } { 3 } } \end{array}$

13. $\begin{array} { r } { c _ { 0 } = c _ { \mathrm { i } } = \frac { \mathrm { i } } { 2 } } \end{array}$ gives the highest degree of precision, 1.

15.The following approximations are obtained from Formula (4.23) through Formula (4.30),respectively. a. 0.1024404, 0.1024598,0.1024598,0.1024598,0.1024695,0.1024663,0.1024598,and 0.1024598 b. 0.7853982,0.7853982,0.7853982,0.7853982,0.7853982,0.7853982,0.7853982,and 0.7853982 c. 1.497171, 1.477536, 1.477529,1.477523,1.467719,1.470981, 1.477512,and 1.477515 d.4.950000,2.740909,2.563393,2.385700,1.636364,1.767857,2.074893,and 2.116379 e. 3.293182, 2.407901,2.359772,2.314751,1.965260,2.048634， 2.233251,and 2.249001 f.0.5000000,0.6958004, 0.7126032,0.7306341,0.7937005,0.7834709,0.7611137,and 0.7593572

7. The errors in Exercise 16 are $1 . 6 \times 1 0 ^ { - 6 }$ ， $5 . 3 \times 1 0 ^ { - 8 }$ ， $- 6 . 7 \times 1 0 ^ { - 7 }$ ， $- 7 . 2 \times 1 0 ^ { - 7 }$ ,and $- 1 . 3 \times 1 0 ^ { - 6 }$ ,respectively

19.If $E ( x ^ { k } ) = 0$ ,for all $k = 0 , 1 , \ldots , n$ and $E ( x ^ { n + 1 } ) \neq 0$ ,then with $p _ { n + 1 } ( x ) = x ^ { n + 1 }$ ， we have a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Let $p ( x ) = a _ { n } x ^ { n } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 }$ be any polynomial of degree less than or equal to $\pmb { n }$ . Then $E ( p ( x ) ) = a _ { n } E ( x ^ { n } ) + \cdot \cdot \cdot + a _ { 1 } E ( x ) + a _ { 0 } E ( 1 ) = 0$ Conversely, if $E ( p ( x ) ) = 0$ ， for all polynomials of degree less than or equal to $\pmb { n }$ , it follows that $E ( x ^ { k } ) = 0$ , for all $k = 0 , 1 , \ldots , n$ Let $p _ { n + 1 } ( x ) = a _ { n + 1 } x ^ { n + 1 } + \cdot \cdot \cdot + a _ { 0 }$ be a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Since $a _ { n + 1 } \neq 0$ ,we have

$$
x ^ { n + 1 } = { \frac { 1 } { a _ { n + 1 } } } p _ { n + 1 } ( x ) - { \frac { a _ { n } } { a _ { n + 1 } } } x ^ { n } - \cdot \cdot \cdot - { \frac { a _ { 0 } } { a _ { n + 1 } } } .
$$

Then

$$
\begin{array} { c l c r } { { \displaystyle E ( x ^ { n + 1 } ) = \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) - \frac { a _ { n } } { a _ { n + 1 } } E ( x ^ { n } ) - \cdot \cdot \cdot - \frac { a _ { 0 } } { a _ { n + 1 } } E ( 1 ) } } \\ { { \displaystyle } } \\ { { \displaystyle = \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) \neq 0 . } } \end{array}
$$

Thus,the quadrature formula has degree of precision $\pmb { n }$

# Exercise Set 4.4 (Page 203)

1.The Composite Trapezoidal rule approximations are:a. 0.639900 b.31.3653 c. 0.784241d.-6.42872

.The Composite Midpoint rule approximations are:a. 0.633096 b.11.1568 c. 0.786700 d.-6.11274

e. -14.9985f. 0.478751g. 0.602961 h. 0.947868

5. $\alpha = 0 . 7 5$

7.a. The Composite Trapezoidal rule requires $h < 0 . 0 0 0 9 2 2 2 9 5$ and $n \geq 2 1 6 8$ b. The Composite Simpson's rule requires $h < 0 . 0 3 7 6 5 8$ and $n \geq 5 4$ c. The Composite Midpoint rule requires $h < 0 . 0 0 0 6 5 2 1 6$ and $n \geq 3 0 6 6$

9. a. The Composite Trapezoidal rule requires $h < 0 . 0 4 3 8 2$ and $n \geq 4 6$ . The approximation is 0.405471.

b. The Composite Simpson's rule requires $h < 0 . 4 4 2 6 7$ and $n \geq 6$ . The approximation is 0.405466.   
c. The Composite Midpoint rule requires $h < 0 . 0 3 0 9 8$ and $n \geq 6 4$ .The approximation is 0.405460.

I1.a.Because theright and left limitsat O.1 and O.2 for f，f',and f" are the same,thefunctions are continuous on [0, 0.3]. However,

$$
f ^ { \prime \prime } ( x ) = { \left\{ \begin{array} { l l } { 6 , } & { 0 \leq x \leq 0 . 1 } \\ { 1 2 , } & { 0 . 1 < x \leq 0 . 2 } \\ { 1 2 , } & { 0 . 2 < x \leq 0 . 3 } \end{array} \right. }
$$

is discontinuous at $x = 0 . 1$

b. We have O.302506 with an error bound of $1 . 9 \times 1 0 ^ { - 4 }$ ，

c. We have 0.302425,and the value of the actual integral is the same.

13.a. For the Composite Trapezoidal rule, we have

$$
E ( f ) = - { \frac { h ^ { 3 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) h = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j } ,
$$

where $\Delta x _ { j } = x _ { j + 1 } - x _ { j } = h$ for each $j$ . Since $\begin{array} { r } { \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j } } \end{array}$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ ， we have

$$
E ( f ) \approx - { \frac { h ^ { 2 } } { 1 2 } } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

b. For the Composite Midpoint rule, we have

$$
E ( f ) = { \frac { h ^ { 3 } } { 3 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) = { \frac { h ^ { 2 } } { 6 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h ) .
$$

But $\textstyle \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h )$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ so

$$
E ( f ) \approx { \frac { h ^ { 2 } } { 6 } } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

15.a. The estimate using the Composite Trapezoidal rule is $- \textstyle { \frac { 1 } { 2 } } h ^ { 2 } \ln 2 = - 6 . 2 9 6 \times 1 0 ^ { - 6 }$ b.The estimate using the Composite Simpson's uleis $- \textstyle { \frac { 1 } { 2 4 0 } } h ^ { 2 } = - 3 . 7 5 \times 1 0 ^ { - 6 }$ c. The estimate using the Composite Midpoint rule is $\frac { 1 } { 6 } h ^ { 2 } \ln 2 = 6 . 9 3 2 \times 1 0 ^ { - 6 }$

17.The length is approximately 15.8655.

19. Composite Simpson's rule with $h = 0 . 2 5$ gives 2.61972 s.

21. The length is approximately 58.47082,using $n = 1 0 0$ in the Composite Simpson's rule.

# Exercise Set 4.5 (Page 211)

1. Romberg integration gives $R _ { 3 , 3 }$ as follows:a. 0.1922593 b. 0.1606105c.-0.1768200d. 0.08875677

3. Romberg integration gives:a. 0.19225936 with $n = 4$ b. 0.16060279 with $n = 5$ c.-0.17682002 with $n \ne 4$ d. 0.088755284 with $n = 5$ e. 2.5886286 with $n = 6$ f.-0.73396918 with $n = 6$ g. 0.63621335 with $n = 4$ h. 0.64269908 with $n = 5$

5. $R _ { 3 3 } = 1 1 . 5 2 4 6$

7. $f ( 2 . 5 ) \approx 0 . 4 3 4 5 9$

9. $R _ { 3 1 } = 5$

11. We have

$$
\begin{array} { r l } { \bar { H } _ { 1 , 2 } = \frac { 4 \bar { H } _ { 1 , 1 } - \bar { H } _ { 1 , \bar { 1 } + \bar { 1 } } } { 3 } } & { } \\ { = } & { \frac { 1 } { 3 } \left[ \bar { R } _ { \mathrm { e n d ~ \bar { 1 } } } + 2 \bar { R } _ { \mathrm { E } } \frac { \varepsilon ^ { \prime \prime } } { 1 2 } \int ( \alpha + ( \varepsilon - 1 ) L _ { 2 } ) b _ { \mathrm { E } - \bar { 1 } } \right] _ { 1 } ^ { 2 } , \quad \mathrm { f r o m ~ } ( 4 , 3 5 ) , } \\ { = } & { \frac { 1 } { 3 } \Bigg [ \frac { \bar { R } _ { \mathrm { e n d ~ \bar { 1 } } } } { 2 } ( \bar { L } ( \alpha ) + \bar { L } ( \beta ) + \bar { b } _ { \mathrm { t a } } ) \frac { \varepsilon ^ { \prime \prime } } { 1 2 } \int ( \alpha + ( \varepsilon - 1 ) L _ { 2 } ) ( \beta + \bar { L } _ { 1 } ) } \\ & { \quad \quad + 2 \bar { R } _ { \mathrm { i n d ~ \bar { 1 } } } \frac { \varepsilon ^ { \prime \prime } } { 1 2 } \int ( \alpha + ( \varepsilon - 1 ) L _ { 2 } ) \bar { R } _ { \mathrm { i n d ~ \bar { 1 } } - \bar { 1 } } \Bigg ] _ { 1 } ^ { 2 } , \quad \mathrm { f r o m ~ } ( 4 , 3 5 ) , } \\ { = } & { \frac { 1 } { 3 } \left[ \bar { R } _ { \mathrm { i n d ~ \bar { 1 } } } + 2 \bar { R } ( \alpha ) + \bar { L } ( \beta ) + \bar { L } ( \alpha - 1 ) L _ { 2 } \right] _ { 1 } ^ { 2 } , \quad \mathrm { f r o m ~ } ( 4 , 3 5 ) , \mathrm { s u b } \mathrm { d } \mathrm { ~ \bar { 1 } } \mathrm { e x t a } \mathrm { ~ \bar { 1 } ~ i m e t a } \mathrm { ~ \bar { 2 } ~ } t ^ { \prime } , } \\ &  \quad \quad + 2 \bar { R } _ { \mathrm { i n d ~ \bar { 1 } } - 1 } \frac { \varepsilon ^ { \prime \prime } } { 1 2 } \int ( \alpha + ( \varepsilon - 1 ) L _ { 2 } ) \bar { R } _ { \mathrm { i n d ~ \bar { 1 } } - 1 } \int _ { \mathrm { a v } } \bar { L } ( \alpha - 2 \bar { R } \beta ) + d _ { \mathrm { i } , \bar { 1 } } \frac { \varepsilon ^ { \prime \prime } }   \end{array}
$$

where $h = h _ { k }$ and $M = 2 ^ { k - 2 }$

13.Equation (4.35） follows from

$$
\begin{array} { r l } { R _ { \kappa , \lambda } = \displaystyle \frac { h _ { k } } { 2 } [ f ( a ) \dagger ^ { * } ( f ( b ) + 2 \stackrel { x ^ { \lambda - 1 } } { \underset { i = 1 } { \overset { x ^ { \lambda - 1 } } { \sum } } } \ f ( a + i h _ { k } ) ] } & { } \\ { = \displaystyle \frac { h _ { k } } { 2 } [ f ( a ) \dagger ^ { * } \mathit { f } ( b ) + 2 \stackrel { x ^ { \lambda - 1 } } { \underset { i = 1 } { \overset { x ^ { \lambda - 1 } } { \sum } } } \ f ( a + \frac { i } { 2 } h _ { k - 1 } ) ] } & { } \\ { = \displaystyle \frac { h _ { k } } { 2 } [ f ( a ) + \mathit { f } ( b ) + 2 \stackrel { x ^ { \lambda - 1 } } { \underset { i = 1 } { \overset { x ^ { \lambda - 1 } } { \sum } } } \jmath ( a + i h _ { k - 1 } ) + 2 \stackrel { x ^ { \lambda - 2 } } { \underset { i = 1 } { \overset { x ^ { \lambda - 1 } } { \sum } } } \ f ( a + ( i - 1 / 2 ) h _ { k - 1 } ) ] } & { } \\ { = \displaystyle \frac { 1 } { 2 } \{ \frac { h _ { k - 1 } } { 2 } [ f ( a ) + \mathit { f } ( b ) + 2 \stackrel { x ^ { \lambda - 1 } } { \underset { i = 1 } { \overset { x ^ { \lambda - 1 } } { \sum } } } \ f ( a + i h _ { k } ) ] + h _ { k - 1 } \} \frac { \hat { x } ^ { 2 } \hat { x } } { \underset { i = 1 } { \overset { x ^ { \lambda - 2 } } { \sum } } } f ( a + ( i - 1 / 2 ) h _ { k - 1 } ) \} } & { } \\ { = \displaystyle \frac { 1 } { 2 } [ R _ { \kappa - 1 , 1 } + h _ { k - 1 } ] ^ { \frac { \frac { \frac { \lambda } { 2 } } } { \kappa _ { 0 } } } f ( a + ( i - 1 / 2 ) h _ { k - 1 } ) \} . } \end{array}
$$

# Exercise Set 4.6 (Page 219)

1. Simpson's rule gives

a. $S ( 1 , 1 . 5 ) = 0 . 1 9 2 2 4 5 3 0 , ~ S ( 1 , 1 . 2 5 ) = 0 . 0 3 9 3 7 2 4 3 4 , ~ S ( 1 . 2 5 , 1 . 5 ) = 0 . 1 5 2 8 8 6 0 2 ,$ and the actual value is 0.19225935.

b. S(0,1)= 0.16240168，S(0,0.5)= 0.028861071，S(0.5,1)=0.13186140,and the actual value is 0.1606027 c. S(0,0.35)= -0.17682156，S(0,0.175)= -0.087724382,S(0.175,0.35) =-0.089095736,and the actual value is -0.17682002.

d. $\begin{array} { l l l } { S ( 0 , { \frac { \pi } { 4 } } ) = 0 . 0 8 7 9 9 5 6 6 9 , } & { S ( 0 , { \frac { \pi } { 8 } } ) = 0 . 0 0 5 8 3 1 5 7 9 7 , } & { S ( { \frac { \pi } { 8 } } , { \frac { \pi } { 4 } } ) = 0 . 0 8 2 8 7 7 6 2 4 , } \end{array}$ and the actual value is 0.088755285.

e. $\begin{array} { r } { \mathrm { ~ : } ( 0 , \frac { \pi } { 4 } ) = 2 . 5 8 3 6 9 6 4 , \ S ( 0 , \frac { \pi } { 8 } ) = 0 . 3 3 0 8 8 9 2 6 , \ S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 2 . 2 5 6 8 1 2 } \end{array}$ , and the actual value is 2.5886286.

f $S ( 1 , 1 . 6 ) = - 0 . 7 3 9 1 0 5 3 3$ 3， $S ( 1 , 1 . 3 ) = - 0 . 2 6 1 4 1 2 4 4$ ， $S ( 1 . 3 , 1 . 6 ) = - 0 . 4 7 3 0 5 3 5 1$ ,and the actual value is --0.73396917.

g.S(3,3.5)= 0.63623873，S(3,3.25)= 0.32567095，S(3.25,3.5)=0.31054412,and the actual value is 0.63621334.

h. S(0,)= 0.64326905, $\begin{array} { r } { S ( 0 , \frac { \pi } { 8 } ) = 0 . 3 7 3 1 5 0 0 2 } \end{array}$ ， $\begin{array} { r } { S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 0 . 2 6 9 5 8 2 7 0 } \end{array}$ ,and the actual value is 0.64269908

Adaptive quadrature gives: a. 108.555281 b. -1724.966983 c. -15.306308 d. --18.945949

5. Adaptive quadrature gives

$$
\int _ { 0 . 1 } ^ { 2 } \sin { \frac { 1 } { x } } \ d x = 1 . 1 4 5 4 \quad { \mathrm { ~ a n d ~ } } \quad \int _ { 0 . 1 } ^ { 2 } \cos { \frac { 1 } { x } } \ d x = 0 . 6 7 3 7 8 .
$$

7. $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } u ( t ) \ d t \approx 0 . 0 0 0 0 1 } \end{array}$

<table><tr><td>9. f 0.1</td><td>c(t) s(t）</td></tr><tr><td>0.0999975</td><td>0.000523589</td></tr><tr><td>0.2</td><td>0.199921 0.00418759</td></tr><tr><td>0.3</td><td>0.299399 0.0141166</td></tr><tr><td>0.4</td><td>0.397475 0.0333568</td></tr><tr><td>0.5 0.492327</td><td>0.0647203</td></tr><tr><td>0.6 0.581061</td><td>0.110498</td></tr><tr><td>0.7</td><td>0.659650 0.172129</td></tr><tr><td>0.8 0.722844</td><td>0.249325</td></tr><tr><td>0.9 0.764972 1.0</td><td>0.339747 0.779880 0.438245</td></tr></table>

# Exercise Set 4.7 (Page 226)

1.Gaussian quadrature gives:a. 0.1922687 b. 0.1594104 c.--0.1768190 d. 0.08926302 e. 2.5913247 f. -0.7307230g. 0.6361966 h. 0.6423172

3.Gaussian quadrature gives:a. 0.1922594 b.0.1606028 c.-0.1768200 d.0.08875529 e. 2.5886327 f.-0.7339604g. 0.6362133h. 0.6426991

5. $a = 1$ ， $b = 1$ ， $\begin{array} { r } { c = { \frac { 1 } { 3 } } } \end{array}$ ， $\begin{array} { r } { d = - \frac { 1 } { 3 } } \end{array}$

# Exercise Set 4.8 (Page 239)

1.Algorithm 4.4 with n = m= 4 gives: a. 0.3115733 b. 0.2552526 c. 16.50864 d. 1.476684

3.Algorithm 4.4 with $n = 4$ and $m = 8$ ， $n = 8$ and $m = 4$ , and $n = m = 6$ gives: a. 0.5119875，0.5118533, 0.5118722 b. 1.718857, 1.718220, 1.718385 c. 1.001953，1.000122,1.000386 d. 0.7838542, 0.7833659,0.7834362 e. -1.985611, -1.999182, -1.997353 f. 2.004596,2.000879，2.000980 g. 0.3084277，0.3084562，0.3084323 h. -22.61612,-19.85408,-20.14117

5. Algorithm 4.5 with $n = m = 2$ gives:a. 0.3115/33 b. 0.2552446 c. 16.50863 d. 1.488875

7. Algorithm 4.5 with $n = m = 3$ ， $n = 3$ and $m = 4$ ， $n = 4$ and $m = 3$ ，and $n = m = 4$ gives: a. 0.5118655, 0.5118445, 0.5118655, 0.5118445, $2 . 1 \times 1 0 ^ { - 5 }$ ， $1 . 3 \times 1 0 ^ { - 7 }$ ， $2 . 1 \times 1 0 ^ { - 5 }$ ， $1 . 3 \times 1 0 ^ { - 7 }$ b. 1.718163,1.718302, 1.718139,1.718277, $1 . 2 \times 1 0 ^ { - 4 }$ ， $2 . 0 \times 1 0 ^ { - 5 }$ ， $1 . 4 \times 1 0 ^ { - 4 }$ ， $4 . 8 \times 1 0 ^ { - 6 }$ c.1.000000，1.000000,1.0000000,1.000000,0,0,0,0 d. 0.7833333,0.7833333, 0.7833333, 0.7833333,0, 0,0,0 e.-1.991878 $^ { ! } , - 2 . 0 0 0 1 2 4 , - 1 . 9 9 1 8 7 8 , - 2 . 0 0 0 1 2 4 , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 } , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 }$ f.2.001494,2.000080,2.001388,1.999984, $1 . 5 \times 1 0 ^ { - 3 }$ ， $8 \times 1 0 ^ { - 5 }$ ， $1 . 4 \times 1 0 ^ { - 3 }$ ,1.6 × 10-5 g. 0.3084151, 0.3084145, 0.3084246, 0.3084245, $1 0 ^ { - 5 }$ ， $5 . 5 \times 1 0 ^ { - 7 }$ ， $1 . 1 \times 1 0 ^ { - 5 }$ ， $6 . 4 \times 1 0 ^ { - 7 }$ h. -12.74790, -21.21539,-11.83624, -20.30373, 7.0, 1.5, 7.9, 0.564

9. Algorithm 4.4 with $n = m = 1 4$ gives 0.1479103,and Algorithm 4.5 with $n = m = 4$ gives 0.1506823.

1. The approximation to the center of mass is $( { \overline { { x } } } , { \overline { { y } } } )$ ，where $\overline { { x } } = 0 . 3 8 0 6 3 3 3$ and $\overline { { y } } = 0 . 3 8 2 2 5 5 8$

13. The area is approximately 1.0402528.

15.Algorithm 4.6 with $n = m = p = 2$ gives the first listed value. The second is the exact result. a. 5.204036, $e ( e ^ { 0 . 5 } - 1 ) ( e - 1 ) ^ { 2 }$ b. 0.08429784, $\frac { 1 } { 1 2 }$ c. 0.08641975, $\frac { 1 } { 1 4 }$ d. 0.09722222, $\frac { 1 } { 1 2 }$ e. 7.103932, $2 + { \textstyle { \frac { 1 } { 2 } } } \pi ^ { 2 }$ f. 1.428074, $\frac { 1 } { 2 } ( e ^ { 2 } + 1 ) - e$

17. Algorithm 4.6 with $n = m = p = 4$ gives the first listed value. The second is from Algorithm 4.6 witl $n = m = p = 5$ a. 5.206447, 5.206447 b. 0.08333333,0.08333333 c. 0.07142857,0.07142857 d.0.08333333,0.08333333 e. 6.934912,6.934801 f. 1.476207, 1.476246   
19.The approximation 20.41887 requires 125 functional evaluations.

# Exercise Set 4.9 (Page 245)

1.The Composite Simpson's rule gives:a. 0.5284163 b. 4.266654 c. 0.4329748 d. 0.8802210

3.The Composite Simpson's rule gives:a. 0.4112649 b. 0.2440679 c. 0.05501681 d. 0.2903746

5. The escape velocity is approximately $6 . 9 4 5 0 \ \mathrm { m i / s }$

7. a. $\begin{array} { r l } & { \boldsymbol { \mathrm { 1 } } \cdot \displaystyle \int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 8 5 3 5 5 3 4 ~ f ( 0 . 5 8 5 7 8 6 4 ) + 0 . 1 4 6 4 4 6 6 ~ f ( 3 . 4 1 4 2 1 3 6 ) } \\ & { \boldsymbol { \mathrm { 1 } } \cdot \displaystyle \int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 7 1 1 0 9 3 0 ~ f ( 0 . 4 1 5 7 7 4 6 ) + 0 . 2 7 8 5 1 7 7 ~ f ( 2 . 2 9 4 2 8 0 4 ) + 0 . 0 9 9 3 0 2 e ^ { - x } } \end{array}$ b 0103893 f(6.2899451)

9. $n = 2$ : 2.9865139   
$n = 3$ : 2.9958198

# Exercise Set 5.1 (Page 255)

l. a. Since $f ( t , y ) = y \cos t$ ， we have $\begin{array} { r } { \frac { \partial f } { \partial y } ( t , y ) = \cos t } \end{array}$ ,and $f$ satisfies a Lipschitz condition in y with $L = 1$ on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = e ^ { \sin t }$

b. Since $\begin{array} { r } { f ( t , y ) = \frac { 2 } { t } y + t ^ { 2 } e ^ { t } } \end{array}$ , we have $\begin{array} { r } { { \frac { \partial f } { \partial y } } = { \frac { 2 } { t } } } \end{array}$ ,and $f$ satisfies a Lipschitz condition in $\mathfrak { y }$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ ， so there exists a unique solution, which is $y ( t ) = t ^ { 2 } ( e ^ { t } - e )$

:. Since $\begin{array} { r } { f ( t , y ) = - \frac { 2 } { t } y + t ^ { 2 } e ^ { t } } \end{array}$ ， we have $\begin{array} { r } { \frac { \partial f } { \partial y } = - \frac { 2 } { r } } \end{array}$ ,and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution,which is

$$
y ( t ) = ( t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } + ( \sqrt { 2 } - 9 ) e ) / t ^ { 2 } .
$$

d. Since $\begin{array} { r } { f ( t , y ) = \frac { 4 t ^ { 3 } y } { 1 + t ^ { 4 } } } \end{array}$ we have $\begin{array} { r } { \frac { \partial \xi } { \partial y } = \frac { 4 i ^ { 3 } } { 1 + t ^ { 4 } } } \end{array}$ i,and f satisfies a Lipschitz condition in y with L =2on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ ，so there exists a unique solution,which is $y ( t ) = 1 + t ^ { 4 }$

3. a. Differentiating $y ^ { 3 } t + y t = 2$ gives $3 y ^ { 2 } y ^ { \prime } t + y ^ { 3 } + y ^ { \prime } t + y = 0$ Solving for $\mathbf { y } ^ { \prime }$ gives the original differential equation,and setting $t = 1$ and $y = 1$ verifies the initial condition. To approximate $y ( 2 )$ , use Newton's method to solve the equation $y ^ { 3 } + y - 1 = 0$ . This gives $y ( 2 ) \approx 0 . 6 8 2 3 2 7 8$

b. Differentiating $y \sin t + t ^ { 2 } e ^ { y } + 2 y - 1 = 0$ gives $y ^ { \prime } \sin t + y \cos t + 2 t e ^ { y } + t ^ { 2 } e ^ { y } y ^ { \prime } + 2 y ^ { \prime } = 0$ Solving for $y ^ { \prime }$ gives the original differential equation, and setting $\iota = 1$ and ${ \bf { y } } = { \bf { 0 } }$ verifies the initial condition.To approximate ${ \tt y } ( 2 )$ ， use Newton's method to solve the equation $( 2 + \sin 2 ) y + 4 e ^ { y } - 1 = 0$ This gives $y ( 2 ) \approx - 0 . 4 9 4 6 5 9 9$

5. Let $( t _ { 1 } , y _ { 1 } )$ and $( t _ { 2 } , y _ { 2 } )$ be in $D$ ，with $a \leq t _ { 1 } \leq b , a \leq t _ { 2 } \leq b , - \infty < y _ { 1 } < \infty ,$ and $- \infty < y _ { 2 } < \infty$ .For $0 \leq \lambda \leq 1$ ， we have $( 1 - \lambda ) a \leq ( 1 - \lambda ) t _ { 1 } \leq ( 1 - \lambda ) b$ and $\lambda a \le \lambda t _ { 2 } \le \lambda b$ .Hence, $a = ( 1 - \lambda ) a + \lambda a \leq ( 1 - \lambda ) t _ { 1 } + \lambda t _ { 2 } \leq$ $( 1 - \lambda ) b + \lambda b = b$ . Also, $- \infty < ( 1 - \lambda ) y _ { 1 } + \lambda y _ { 2 } < \infty$ ，so $D$ is convex.

7. a. Since $y ^ { \prime } = f ( t , y ( t ) )$ ，we have

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

b. We have $y _ { 0 } ( t ) = 1$ ， $\begin{array} { r } { y _ { 1 } ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } } \end{array}$ ， $\begin{array} { r } { y _ { 2 } ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } - \frac { 1 } { 6 } t ^ { 3 } } \end{array}$ ,and $\begin{array} { r } { y _ { 3 } ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } - \frac { 1 } { 6 } t ^ { 3 } + \frac { 1 } { 2 4 } t ^ { 4 } } \end{array}$ c. We have $\begin{array} { r } { y ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } - \frac { 1 } { 6 } t ^ { 3 } + \frac { 1 } { 2 4 } t ^ { 4 } - \frac { 1 } { 1 2 0 } t ^ { 5 } + \cdot \cdot \cdot } \end{array}$

# Exercise Set 5.2 (Page 263)

1. Euler's method gives the approximations in the following table.

<table><tr><td>a.i</td><td></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td rowspan="8"></td><td>1</td><td>0.500</td><td>0.0000000</td><td>0.2836165</td></tr><tr><td>2</td><td>1.000</td><td>1.1204223</td><td>3.2190993</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>c. i</td><td>ti</td><td>Wi</td><td>y(ti）</td></tr><tr><td>1</td><td>1.250</td><td>2.7500000</td><td>2.7789294</td></tr><tr><td>2</td><td>1.500</td><td>3.5500000</td><td>3.6081977</td></tr><tr><td>3</td><td>1.750</td><td>4.3916667</td><td>4.4793276</td></tr><tr><td>4</td><td>2.000</td><td>5.2690476</td><td>5.3862944</td></tr></table>

<table><tr><td>b. i</td><td></td><td>ti</td><td>Wi</td><td>y(t)</td></tr><tr><td rowspan="4"></td><td>1</td><td>2.500</td><td>2.0000000</td><td>1.8333333</td></tr><tr><td>2</td><td>3.000</td><td>2.6250000</td><td>2.5000000</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>d. i</td><td>i</td><td>Wi</td><td>y(t）</td></tr><tr><td></td><td>1</td><td>0.250</td><td>1.2500000</td><td>1.3291498</td></tr><tr><td rowspan="4">2</td><td></td><td>0.500</td><td>1.6398053</td><td>1.7304898</td></tr><tr><td>3</td><td>0.750</td><td>2.0242547</td><td>2.0414720</td></tr><tr><td>4</td><td></td><td></td><td></td></tr><tr><td></td><td>1.000</td><td>2.2364573</td><td>2.1179795</td></tr></table>

3.Euler's method gives the approximations in the following tables.

<table><tr><td>i a. 2</td><td>t</td><td>W</td><td>y(ti)</td></tr><tr><td>4 6</td><td>1.200 1.400 1.600</td><td>1.0082645 1.0385147 1.0784611</td><td>1.0149523 1.0475339 1.0884327</td></tr><tr><td>8 10</td><td>1.800</td><td>1.1232621</td><td>1.1336536</td></tr><tr><td></td><td>2.000</td><td>1.1706516</td><td>1.1812322</td></tr><tr><td>c. i</td><td>t</td><td></td><td>y(ti)</td></tr><tr><td>2 4</td><td>0.400 0.800</td><td>Wi -1.6080000</td><td>-1.6200510</td></tr></table>

<table><tr><td>b.i</td><td>t</td><td>W;</td><td>y(t)</td></tr><tr><td>2 4</td><td>1.400</td><td>0.4388889</td><td>0.4896817</td></tr><tr><td>6</td><td>1.800 2.200</td><td>1.0520380 1.8842608</td><td>1.1994386 2.2135018</td></tr><tr><td>8</td><td>2.600</td><td>3.0028372</td><td>3.6784753</td></tr><tr><td>10</td><td>3.000</td><td>4.5142774</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>d.i</td><td>t</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>0.2</td><td>0.1083333</td><td>0.1626265</td></tr><tr><td>4</td><td>0.4</td><td>0.1620833</td><td>0.2051118</td></tr><tr><td>6</td><td>0.6</td><td>0.3455208</td><td>0.3765957</td></tr><tr><td>8</td><td>0.8</td><td>0.6213802</td><td>0.6461052</td></tr><tr><td>10</td><td>1.0</td><td>0.9803451</td><td>1.0022460</td></tr></table>

5.Euler's method gives the approximations in the following table.

b. Linear interpolation gives the approximations in the following table.   

<table><tr><td>i a.</td><td>t</td><td>Wi</td><td>y（t）</td></tr><tr><td>1</td><td>1.1</td><td>0.271828</td><td>0.345920</td></tr><tr><td>5</td><td>1.5</td><td>3.18744</td><td>3.96767</td></tr><tr><td>6</td><td>1.6</td><td>4.62080</td><td>5.70296</td></tr><tr><td>9</td><td>1.9</td><td>11.7480</td><td>14.3231</td></tr><tr><td>10</td><td>2.0</td><td>15.3982</td><td>18.6831</td></tr></table>

<table><tr><td>1</td><td>Approximation</td><td>y(t)</td><td>Error</td></tr><tr><td>1.04</td><td>0.108731</td><td>0.119986</td><td>0.01126</td></tr><tr><td>1.55</td><td>3.90412</td><td>4.78864</td><td>0.8845</td></tr><tr><td>1.97</td><td>14.3031</td><td>17.2793</td><td>2.976</td></tr></table>

c. $h < 0 . 0 0 0 6 4$

7. a. Euler's method produces the following approximation to $y ( 5 ) = 5 . 0 0 6 7 4$

$$
\frac { h = 0 . 2 } { w _ { N } } | \begin{array} { c c } { { } } & { { h = 0 . 2 } } \\ { { } } & { { 5 . 0 0 3 7 7 } } \end{array} | \begin{array} { c c } { { h = 0 . 1 } } & { { | \begin{array} { c c } { { } } & { { h = 0 . 0 5 } } \\ { { } } & { { 5 . 0 0 5 1 5 } } \end{array} | } } \\ { { } } & { { 5 . 0 0 5 9 2 } } \end{array} 
$$

b. $h = { \sqrt { 2 \times 1 0 ^ { - 6 } } } \approx 0 . 0 0 1 4 1 4 2 .$

9.a. $h = 1 0 ^ { - n / 2 }$ b. The minimal error is $1 0 ^ { - n / 2 } ( e - 1 ) + 5 e 1 0 ^ { - n - 1 }$

<table><tr><td colspan="4">c.</td><td rowspan="2">Error (n = 8)</td></tr><tr><td>t</td><td>w(h = 0.1)</td><td>w(h = 0.01)</td><td>y(t)</td></tr><tr><td>0.5</td><td>0.40951</td><td>0.39499</td><td>0.39347</td><td>1.5 × 10-4</td></tr><tr><td>1.0</td><td>0.65132</td><td>0.63397</td><td>0.63212</td><td>3.1 × 10-4</td></tr></table>

11. b. $\boldsymbol { w } _ { 5 0 } = 0 . 1 0 4 3 0 \approx p ( 5 0 )$ c. Since $p ( t ) = 1 - 0 . 9 9 e ^ { - 0 . 0 0 2 t }$ ， $p ( 5 0 ) = 0 . 1 0 4 2 1$

# Exercise Set 5.3 (Page 271)

<table><tr><td>1. a.</td><td></td><td>Wi</td><td>y(t)</td></tr><tr><td rowspan="8">c.</td><td>0.50</td><td>0.12500000</td><td>0.28361652</td></tr><tr><td>1.00</td><td>2.02323897</td><td>3.21909932</td></tr><tr><td></td><td></td><td>y(t)</td></tr><tr><td>i 1.25</td><td>Wi 2.78125000</td><td>2.77892944</td></tr><tr><td>1.50</td><td>3.61250000</td><td>3.60819766</td></tr><tr><td>1.75</td><td>4.48541667</td><td>4.47932763</td></tr><tr><td>2.00</td><td></td><td>5.38629436</td></tr><tr><td></td><td>5.39404762</td><td></td></tr></table>

<table><tr><td rowspan="5">b.</td><td></td><td>Wi</td><td>y(t）</td></tr><tr><td>2.50</td><td>1.75000000</td><td>1.83333333</td></tr><tr><td>3.00</td><td>2.42578125</td><td>2.50000000</td></tr><tr><td></td><td></td><td></td></tr><tr><td>d.</td><td>Wi</td><td>y(t）</td></tr><tr><td colspan="2">0.25 0.50 0.75 1.00</td><td>1.34375000 1.77218707</td><td>1.32914981 1.73048976</td></tr></table>

<table><tr><td colspan="2">3.a.</td><td></td><td>Order 2</td><td>Order 4</td><td>y(ti)</td></tr><tr><td rowspan="9">b. c.</td><td>i</td><td>ti</td><td>Wi</td><td>Wi</td><td></td></tr><tr><td>1</td><td>1.1</td><td>1.214999</td><td>1.215883</td><td>1.215886</td></tr><tr><td>2</td><td>1.2</td><td>1.465250</td><td>1.467561</td><td>1.467570</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>i</td><td>t</td><td>Order 2 Wi</td><td>Order 4 Wi</td><td>y(t)</td></tr><tr><td>1</td><td>0.5</td><td>0.5000000</td><td>0.5156250</td><td>0.5158868</td></tr><tr><td>2</td><td>1.0</td><td>1.076858</td><td>1.091267</td><td>1.091818</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>i</td><td></td><td>Order 2</td><td>Order 4</td><td>y(t)</td></tr><tr><td>1</td><td>t</td><td>Wi</td><td></td><td>Wi</td></tr><tr><td></td><td>1.5</td><td>--2.000000</td><td>-2.000000</td><td>-1.500000</td></tr><tr><td>2</td><td>2.0</td><td>-1.777776</td><td>-1.679012</td><td>-1.333333</td></tr><tr><td>3</td><td>2.5</td><td>--1.585732</td><td>-1.484493</td><td>-1.250000</td></tr><tr><td>4</td><td>3.0</td><td>-1.458882</td><td>-1.374440</td><td>-1.200000</td></tr></table>

Answers for Selected Exercises   

<table><tr><td>d. i</td><td></td><td>Order 2</td><td>Order 4</td><td>y(t)</td></tr><tr><td></td><td>t</td><td>Wi</td><td>Wi</td><td></td></tr><tr><td>1 2</td><td>0.25 0.50</td><td>1.093750 1.312319</td><td>1.086426 1.288245</td><td>1.087088 1.289805</td></tr><tr><td>3</td><td>0.75</td><td>1.538468</td><td>1.512576</td><td>1.513490</td></tr><tr><td>4</td><td>1.0</td><td>1.720480</td><td>1.701494</td><td>1.701870</td></tr></table>

5.a. Taylor's method of order two gives the results in the following table.

<table><tr><td>i</td><td></td><td>Wi</td><td>y(t)</td></tr><tr><td>1</td><td>1.1</td><td>0.3397852</td><td>0.3459199</td></tr><tr><td>5</td><td>1.5</td><td>3.910985</td><td>3.967666</td></tr><tr><td>6</td><td>1.6</td><td>5.643081</td><td>5.720962</td></tr><tr><td>9</td><td>1.9</td><td>14.15268</td><td>14.32308</td></tr><tr><td>10</td><td>2.0</td><td>18.46999</td><td>18.68310</td></tr></table>

b. Linear interpolation gives $y ( 1 . 0 4 ) \approx 0 . 1 3 5 9 1 3 9$ ， $y ( 1 . 5 5 ) \approx 4 . 7 7 7 0 3 3$ , and $y ( 1 . 9 7 ) \approx 1 7 . 1 7 4 8 0$ . Actual values are $y ( 1 . 0 4 ) = 0 . 1 1 9 9 8 7 5$ ， $y ( 1 . 5 5 ) = 4 . 7 8 8 6 3 5$ ，and $y ( 1 . 9 7 ) = 1 7 . 2 7 9 3 0$

c. Taylor's method of order four gives the results in the following table.

<table><tr><td rowspan=1 colspan=2>i              ti                      Wi</td></tr><tr><td rowspan=1 colspan=1>1           1.1</td><td rowspan=1 colspan=1>0.3459127</td></tr><tr><td rowspan=1 colspan=1>5           1.5</td><td rowspan=1 colspan=1>3.967603</td></tr><tr><td rowspan=1 colspan=1>6           1.6</td><td rowspan=1 colspan=1>5.720875</td></tr><tr><td rowspan=1 colspan=1>9           1.9</td><td rowspan=1 colspan=1>14.32290</td></tr><tr><td rowspan=1 colspan=2>10           2.0           18.68287</td></tr></table>

d. Cubic Hermite interpolation gives y(1.04) \~ 0.1199704, y(1.55) $\approx$ 4.788527, and $y ( 1 . 9 7 ) \approx 1 7 . 2 7 9 0 4$

<table><tr><td>7. a. i</td><td>t</td><td>Order 2</td><td>Order 4</td></tr><tr><td>2</td><td>0.2</td><td>5.86595</td><td>5.86433</td></tr><tr><td>5</td><td>0.5</td><td>2.82145</td><td>2.81789</td></tr><tr><td>7</td><td>0.7</td><td>0.84926</td><td>0.84455</td></tr><tr><td>10</td><td>1.0</td><td>-2.08606</td><td>-2.09015</td></tr></table>

b. 0.8 s

# Exercise Set 5.4 (Page 280)

<table><tr><td>1. a. i</td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>0.5 1.0</td><td>0.5602111 5.3014898</td><td>0.2836165 3.2190993</td></tr><tr><td>t</td><td></td><td></td></tr><tr><td>c.</td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>1.25 1.50</td><td>2.7750000</td><td>2.7789294</td></tr><tr><td>1.75</td><td>3.6008333</td><td>3.6081977</td></tr><tr><td>2.00</td><td>4.4688294</td><td>4.4793276</td></tr><tr><td></td><td>5.3728586</td><td>5.3862944</td></tr></table>

<table><tr><td rowspan="7">b. d.</td><td>t</td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>2.5</td><td>1.8125000</td><td>1.8333333</td></tr><tr><td>3.0</td><td>2.4815531</td><td>2.5000000</td></tr><tr><td></td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>t 0.25</td><td>1.3199027</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7070300</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0053560</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.0770789</td><td>2.1179795</td></tr><tr><td>3. a.</td><td>t</td><td>Midpoint y(t） 0.2836165</td></tr><tr><td colspan="4">0.5 0.2646250</td></tr><tr><td>1.0</td><td>3.1300023</td><td>3.2190993</td></tr><tr><td></td><td></td><td></td></tr><tr><td>c. t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>1.25 1.50</td><td>2.7777778 3.6060606</td><td>2.7789294 3.6081977</td></tr><tr><td>1.75</td><td>4.4763015</td><td>4.4793276</td></tr><tr><td></td><td></td><td></td></tr><tr><td>2.00</td><td>5.3824398</td><td>5.3862944</td></tr></table>

<table><tr><td rowspan="6">b.</td><td>t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>2.5 3.0</td><td>1.7812500 2.4550638</td><td>1.8333333 2.5000000</td></tr><tr><td></td><td></td><td></td></tr><tr><td>d.</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>0.25</td><td>1.3337962</td><td>1.3291498</td></tr><tr><td>0.50 0.75</td><td>1.7422854 2.0596374</td><td>1.7304898 2.0414720</td></tr></table>

5.a. $1 . 0 2 2 1 1 6 7 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ ， $1 . 1 6 4 0 3 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ b. $1 . 9 0 8 6 5 0 0 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , \ 4 . 3 1 0 5 9 1 3 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ c. $- 1 . 1 4 6 1 4 3 4 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 ,$ -1.0454854 \~ y(1.93) = -1.0412665 d. $0 . 3 2 7 1 4 7 0 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , 0 . 8 9 6 7 0 7 3 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

7. a. $1 . 0 2 2 5 5 3 0 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9 , 1 . 1 6 4 6 1 5 5 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ b. $1 . 9 1 3 2 1 6 7 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , 4 . 3 2 4 6 1 5 2 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ c. $- 1 . 1 4 4 1 7 7 5 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 , \ : \ : - 1 . 0 4 4 7 4 0 3 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ d. $0 . 3 2 5 1 0 4 9 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8$ ， $0 . 8 9 4 5 1 2 5 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

9. a. $1 . 0 2 2 7 8 6 3 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9 , 1 . 1 6 4 9 2 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ b. $1 . 9 1 5 3 7 4 9 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , \ 4 . 3 3 1 2 9 3 9 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ c. $- 1 . 1 4 3 2 0 7 0 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 , \ : \ : - 1 . 0 4 4 3 7 4 3 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 3$ d. $0 . 3 2 4 0 8 3 9 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , \ 0 . 8 9 3 4 1 5 2 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

11. a. The Runge-Kutta method of order four gives the results in the following tables.

<table><tr><td>t</td><td>Runge-Kutta</td><td>y(t)</td><td>b.</td><td>Runge-Kutta</td><td>y(t)</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149523</td><td>1.4</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.4</td><td>1.0475336</td><td>1.0475339</td><td>1.8</td><td>1.1994320</td><td>1.1994386</td></tr><tr><td>1.6</td><td>1.0884323</td><td>1.0884327</td><td>2.2</td><td>2.2134693</td><td>2.2135018</td></tr><tr><td>1.8</td><td>1.1336532</td><td>1.1336536</td><td>2.6</td><td>3.6783790</td><td>3.6784753</td></tr><tr><td>2.0</td><td>1.1812319</td><td>1.1812322</td><td>3.0</td><td>5.8738386</td><td>5.8741000</td></tr><tr><td colspan="4"></td><td></td><td></td></tr><tr><td>c. t</td><td>Runge-Kutta</td><td>y(t）</td><td>d. t</td><td>Runge-Kutta</td><td>y(1)</td></tr><tr><td>0.4</td><td>-1.6200576</td><td>-1.6200510</td><td>0.2</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.8</td><td>-1.3359824</td><td>-1.3359632</td><td>0.4</td><td>0.2052405</td><td>0.2051118</td></tr><tr><td>1.2</td><td>-1.1663735</td><td>--1.1663454</td><td>0.6</td><td>0.3766981</td><td>0.3765957</td></tr><tr><td>1.6</td><td>-1.0783582</td><td>-1.0783314</td><td>0.8</td><td>0.6461896</td><td>0.6461052</td></tr><tr><td>2.0</td><td>-1.0359922</td><td>-1.0359724</td><td>1.0</td><td>1.0023207</td><td>1.0022460</td></tr></table>

15.In $0 . 2 \ s$ we have approximately 2099 units of KOH.

17. The appropriate constants are $\begin{array} { r } { \alpha _ { 1 } = \delta _ { 1 } = \alpha _ { 2 } = \delta _ { 2 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma _ { 4 } = \gamma _ { 5 } = \gamma _ { 6 } = \gamma _ { 7 } = \frac { 1 } { 2 } } \end{array}$ and $\alpha _ { 3 } = \delta _ { 3 } = 1$

# Exercise Set 5.5 (Page 287)

1. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.

<table><tr><td>a.i</td><td></td><td>i</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.2093900</td><td>0.0298184</td><td>0.2093900</td><td>0.0298337</td></tr><tr><td></td><td>3</td><td>0.5610469</td><td>0.4016438</td><td>0.1777496</td><td>0.4016860</td></tr><tr><td></td><td>5</td><td>0.8387744</td><td>1.5894061</td><td>0.1280905</td><td>1.5894600</td></tr><tr><td></td><td>7</td><td>1.0000000</td><td>3.2190497</td><td>0.0486737</td><td>3.2190993</td></tr><tr><td>b.i</td><td colspan="5"></td></tr><tr><td></td><td></td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1 2</td><td>2.2500000 2.5000000</td><td>1.4499988 1.8333332</td><td>0.2500000 0.2500000</td><td>1.4500000</td></tr><tr><td></td><td>3</td><td>2.7500000</td><td>2.1785718</td><td>0.2500000</td><td>1.8333333 2.1785714</td></tr><tr><td></td><td>4</td><td>3.0000000</td><td>2.5000005</td><td>0.2500000</td><td>2.5000000</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>c.i</td><td colspan="5"></td></tr><tr><td></td><td></td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1</td><td>1.2500000</td><td>2.7789299</td><td>0.2500000</td><td>2.7789294</td></tr><tr><td></td><td>2</td><td>1.5000000</td><td>3.6081985</td><td>0.2500000</td><td>3.6081977</td></tr><tr><td></td><td>3</td><td>1.7500000</td><td>4.4793288</td><td>0.2500000</td><td>4.4793276</td></tr><tr><td></td><td>4</td><td>2.0000000</td><td>5.3862958</td><td>0.2500000</td><td>5.3862944</td></tr><tr><td>d.i</td><td colspan="5"></td></tr><tr><td></td><td></td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.2500000</td><td>1.3291478</td><td>0.2500000</td><td>1.3291498</td></tr><tr><td></td><td>2</td><td>0.5000000</td><td>1.7304857</td><td>0.2500000</td><td>1.7304898</td></tr><tr><td></td><td>3</td><td>0.7500000</td><td>2.0414669</td><td>0.2500000</td><td>2.0414720</td></tr><tr><td></td><td>4</td><td>1.0000000</td><td>2.1179750</td><td>0.2500000</td><td>2.1179795</td></tr></table>

3.The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.   

<table><tr><td>a.i</td><td></td><td>t</td><td>Wi</td><td>h</td><td>yi</td></tr><tr><td></td><td>1</td><td>1.1101946</td><td>1.0051237</td><td>0.1101946</td><td>1.0051237</td></tr><tr><td></td><td>5</td><td>1.7470584</td><td>1.1213948</td><td>0.2180472</td><td>1.1213947</td></tr><tr><td></td><td>7</td><td>2.3994350</td><td>1.2795396</td><td>0.3707934</td><td>1.2795395</td></tr><tr><td></td><td>11</td><td>4.0000000</td><td>1.6762393</td><td>0.1014853</td><td>1.6762391</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b. i</td><td></td><td>t</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>4</td><td>1.5482238</td><td>0.7234123</td><td>0.1256486</td><td>0.7234119</td></tr><tr><td></td><td>7</td><td>1.8847226</td><td>1.3851234</td><td>0.1073571</td><td>1.3851226</td></tr><tr><td>10</td><td></td><td>2.1846024</td><td>2.1673514</td><td>0.0965027</td><td>2.1673499</td></tr><tr><td>16</td><td></td><td>2.6972462</td><td>4.1297939</td><td>0.0778628</td><td>4.1297904</td></tr><tr><td>21</td><td></td><td>3.0000000</td><td>5.8741059</td><td>0.0195070</td><td>5.8741000</td></tr></table>

<table><tr><td>c. i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.1633541</td><td>-1.8380836</td><td>0.1633541</td><td>-1.8380836</td></tr><tr><td>5</td><td>0.7585763</td><td>-1.3597623</td><td>0.1266248</td><td>-1.3597624</td></tr><tr><td>9</td><td>1.1930325</td><td>-1.1684827</td><td>0.1048224</td><td>-1.1684830</td></tr><tr><td>13</td><td>1.6229351</td><td>-1.0749509</td><td>0.1107510</td><td>-1.0749511</td></tr><tr><td>17</td><td>2.1074733</td><td>-1.0291158</td><td>0.1288897</td><td>-1.0291161</td></tr><tr><td>23</td><td>3.0000000</td><td>-1.0049450</td><td>0.1264618</td><td>-1.0049452</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>d.i</td><td>i</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.3986051</td><td>0.3108201</td><td>0.3986051</td><td>0.3108199</td></tr><tr><td>3</td><td>0.9703970</td><td>0.2221189</td><td>0.2866710</td><td>0.2221186</td></tr><tr><td>5</td><td>1.5672905</td><td>0.1133085</td><td>0.3042087</td><td>0.1133082</td></tr><tr><td>8</td><td>2.0000000</td><td>0.0543454</td><td>0.0902302</td><td>0.0543455</td></tr></table>

5.a. The number of infectives is $y ( 3 0 ) \approx 8 0 2 9 5 . 7 .$ b. The limiting value for the number of infectives for this model is $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } y ( t ) = 1 0 0 , 0 0 0 } \end{array}$

# Exercise Set 5.6 (Page 300)

1. The Adams-Bashforth methods give the results in the following tables.

<table><tr><td>a.</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t）</td></tr><tr><td>0.2</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td></tr><tr><td>0.4</td><td>0.1200522</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td></tr><tr><td>0.6</td><td>0.4153551</td><td>0.4613866</td><td>0.4960196</td><td>0.4960196</td><td>0.4960196</td></tr><tr><td>0.8</td><td>1.1462844</td><td>1.2512447</td><td>1.2961260</td><td>1.3308570</td><td>1.3308570</td></tr><tr><td>1.0</td><td>2.8241683</td><td>3.0360680</td><td>3.1461400</td><td>3.1854002</td><td>3.2190993</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b. →</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>2.2</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td></tr><tr><td>2.4</td><td>1.6750000</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td></tr><tr><td>2.6</td><td>1.9632431</td><td>1.9794407</td><td>1.9750000</td><td>1.9750000</td><td>1.9750000</td></tr><tr><td>2.8</td><td>2.2323184</td><td>2.2488759</td><td>2.2423065</td><td>2.2444444</td><td>2.2444444</td></tr><tr><td>3.0</td><td>2.4884512</td><td>2.5051340</td><td>2.4980306</td><td>2.5011406</td><td>2.5000000</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6"></td></tr><tr><td>c.</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2734823</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9567107</td><td>3.9514231</td><td>3.9520058</td><td>3.9520058</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6647738</td><td>4.6569191</td><td>4.6582078</td><td>4.6580160</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3949416</td><td>5.3848058</td><td>5.3866452</td><td>5.3862177</td><td>5.3862944</td></tr><tr><td colspan="6"></td></tr><tr><td>d.</td><td>2-step</td><td>3-step</td><td>4-step</td><td> 5-step</td><td>y(t）</td></tr><tr><td>0.2</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5986417</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.9386951</td><td>1.8827238</td><td>1.8750869</td><td>1.8750869</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.1766821</td><td>2.0844122</td><td>2.0698063</td><td>2.0789180</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.2369407</td><td>2.1115540</td><td>2.0998117</td><td>2.1180642</td><td>2.1179795</td></tr></table>

3.The Adams-Bashforth methods give the results in the following tables.   

<table><tr><td>a. 1</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>1.0161982</td><td>1.0149520</td><td>1.0149520</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.4</td><td>1.0497665</td><td>1.0468730</td><td>1.0477278</td><td>1.0475336</td><td>1.0475339</td></tr><tr><td>1.6</td><td>1.0910204</td><td>1.0875837</td><td>1.0887567</td><td>1.0883045</td><td>1.0884327</td></tr><tr><td>1.8</td><td>1.1363845</td><td>1.1327465</td><td>1.1340093</td><td>1.1334967</td><td>1.1336536</td></tr><tr><td>2.0</td><td>1.1840272</td><td>1.1803057</td><td>1.1815967</td><td>1.1810689</td><td>1.1812322</td></tr><tr><td colspan="6"></td></tr><tr><td>b. 1</td><td>2-step</td><td> 3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.4</td><td>0.4867550</td><td>0.4896842</td><td>0.4896842</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.8</td><td>1.1856931</td><td>1.1982110</td><td>1.1990422</td><td>1.1994320</td><td>1.1994386</td></tr><tr><td>2.2</td><td>2.1753785</td><td>2.2079987</td><td>2.2117448</td><td>2.2134792</td><td>2.2135018</td></tr><tr><td>2.6</td><td>3.5849181</td><td>3.6617484</td><td>3.6733266</td><td>3.6777236</td><td>3.6784753</td></tr><tr><td>3.0</td><td>5.6491203</td><td>5.8268008</td><td>5.8589944</td><td>5.8706101</td><td>5.8741000</td></tr></table>

<table><tr><td>c. 一</td><td>2-step</td><td> 3-step</td><td>4-step</td><td>5-step</td><td>y(t）</td></tr><tr><td>0.5</td><td>-1.5357010</td><td>-1.5381988</td><td>-1.5379372</td><td>-1.5378676</td><td>-1.5378828</td></tr><tr><td>1.0</td><td>-1.2374093</td><td>-1.2389605</td><td>-1.2383734</td><td>-1.2383693</td><td>--1.2384058</td></tr><tr><td>1.5</td><td>-1.0952910</td><td>-1.0950952</td><td>-1.0947925</td><td>--1.0948481</td><td>-1.0948517</td></tr><tr><td>2.0</td><td>-1.0366643</td><td>-1.0359996</td><td>-1.0359497</td><td>-1.0359760</td><td>-1.0359724</td></tr></table>

5.The Adams Fourth-order Predictor-Corrector Algorithm gives the results in the following tables.   

<table><tr><td>d.t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t）</td></tr><tr><td>0.2</td><td>0.1739041</td><td>0.1627655</td><td>0.1627655</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.4</td><td>0.2144877</td><td>0.2026399</td><td>0.2066057</td><td>0.2052405</td><td>0.2051118</td></tr><tr><td>0.6</td><td>0.3822803</td><td>0.3747011</td><td>0.3787680</td><td>0.3765206</td><td>0.3765957</td></tr><tr><td>0.8</td><td>0.6491272</td><td>0.6452640</td><td>0.6487176</td><td>0.6471458</td><td>0.6461052</td></tr><tr><td>1.0</td><td>1.0037415</td><td>1.0020894</td><td>1.0064121</td><td>1.0073348</td><td>1.0022460</td></tr></table>

<table><tr><td>a. 一</td><td>w</td><td>y(t)</td><td>b.t</td><td>w</td><td>y(t）</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149523</td><td>1.4</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.4</td><td>1.0475227</td><td>1.0475339</td><td>1.8</td><td>1.1994245</td><td>1.1994386</td></tr><tr><td>1.6</td><td>1.0884141</td><td>1.0884327</td><td>2.2</td><td>2.2134701</td><td>2.2135018</td></tr><tr><td>1.8</td><td>1.1336331</td><td>1.1336536</td><td>2.6</td><td>3.6784144</td><td>3.6784753</td></tr><tr><td>2.0</td><td>1.1812112</td><td>1.1812322</td><td>3.0</td><td>5.8739518</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>c. t</td><td>w</td><td>y(t)</td><td>d.t</td><td>w</td><td>y(t）</td></tr><tr><td>0.5</td><td>-1.5378788</td><td>-1.5378828</td><td>0.2</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>1.0</td><td>-1.2384134</td><td>-1.2384058</td><td>0.4</td><td>0.2048557</td><td>0.2051118</td></tr><tr><td>1.5</td><td>-1.0948609</td><td>-1.0948517</td><td>0.6</td><td>0.3762804</td><td>0.3765957</td></tr><tr><td>2.0</td><td>-1.0359757</td><td>-1.0359724</td><td>0.8</td><td>0.6458949</td><td>0.6461052</td></tr><tr><td></td><td></td><td></td><td>1.0</td><td>1.0021372</td><td>1.0022460</td></tr></table>

7. a. With $h = 0 . 0 1$ , the three-step Adams-Moulton method gives the values in the following table.

<table><tr><td>i</td><td>i</td></tr><tr><td>0.1</td><td>Wi 1.317218</td></tr><tr><td>10</td><td></td></tr><tr><td>20 0.2</td><td>1.784511</td></tr></table>

b. Newton's method willreduce the number of iterations per step from three to two, using the stopping criterion

$$
\lvert w _ { i } ^ { ( k ) } - w _ { i } ^ { ( k - 1 ) } \rvert \leq 1 0 ^ { - 6 } .
$$

13. To derive Milne's method, integrate $y ^ { \prime } ( t ) = f ( t , y ( t ) )$ on the interval $[ t _ { i - 3 } , t _ { i + 1 } ]$ to obtain

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \int _ { t _ { i - 3 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t .
$$

Using the open Newton-Cotes formula (4.29) on page 194,we have

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = { \frac { 4 h [ 2 f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 2 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) ] } { 3 } } + { \frac { 1 4 h ^ { 5 } f ^ { ( 4 ) } ( \xi , y ( t _ { i - 1 } ) ) } { 4 5 } } + f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) - y ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) \leq 0
$$

The difference equation becomes

$$
w _ { i + 1 } = w _ { i - 3 } + { \frac { h [ 8 f ( t _ { i } , w _ { i } ) - 4 f ( t _ { i - 1 } , w _ { i - 1 } ) + 8 f ( t _ { i - 2 } , w _ { i - 2 } ) ] } { 3 } } ,
$$

with local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { 1 4 h ^ { 4 } y ^ { ( 5 ) } ( \xi ) } { 4 5 } .
$$

# Exercise Set 5.7 (Page 306)

1.The Adams Variable Step-Size Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td>i a.</td><td></td><td>t</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.04275596</td><td>0.00096891</td><td>0.04275596</td><td>0.00096887</td></tr><tr><td></td><td>5</td><td>0.22491460</td><td>0.03529441</td><td>0.05389076</td><td>0.03529359</td></tr><tr><td></td><td>12</td><td>0.60214994</td><td>0.50174348</td><td>0.05389076</td><td>0.50171761</td></tr><tr><td></td><td>17</td><td>0.81943926</td><td>1.45544317</td><td>0.04345786</td><td>1.45541453</td></tr><tr><td></td><td>22</td><td>0.99830392</td><td>3.19605697</td><td>0.03577293</td><td>3.19602842</td></tr><tr><td></td><td>26</td><td>1.00000000</td><td>3.21912776</td><td>0.00042395</td><td>3.21909932</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b.</td><td>i</td><td>t</td><td>Wi</td><td>h</td><td>yi</td></tr><tr><td></td><td>1</td><td>2.06250000</td><td>1.12132350</td><td>0.06250000</td><td>1.12132353</td></tr><tr><td></td><td>5</td><td>2.31250000</td><td>1.55059834</td><td>0.06250000</td><td>1.55059524</td></tr><tr><td></td><td>9</td><td>2.62471924</td><td>2.00923157</td><td>0.09360962</td><td>2.00922829</td></tr><tr><td></td><td>13</td><td>2.99915773</td><td>2.49895243</td><td>0.09360962</td><td>2.49894707</td></tr><tr><td>17</td><td></td><td>3.00000000</td><td>2.50000535</td><td>0.00021057</td><td>2.50000000</td></tr></table>

# Answers for Selected Exercises

3.The following tables list representative results from the Adams Variable Step-Size Predictor-Corrector Algorithm.   

<table><tr><td>c. i</td><td></td><td>t</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td></td><td>1.06250000</td><td>2.18941363</td><td>0.06250000</td><td>2.18941366</td></tr><tr><td></td><td>4</td><td>1.25000000</td><td>2.77892931</td><td>0.06250000</td><td>2.77892944</td></tr><tr><td></td><td>8</td><td>1.85102559</td><td>4.84179835</td><td>0.15025640</td><td>4.84180141</td></tr><tr><td></td><td>12</td><td>2.00000000</td><td>5.38629105</td><td>0.03724360</td><td>5.38629436</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>d.i</td><td></td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.06250000</td><td>1.06817960</td><td>0.06250000</td><td>1.06817960</td></tr><tr><td></td><td>5</td><td>0.31250000</td><td>1.42861668</td><td>0.06250000</td><td>1.42861361</td></tr><tr><td></td><td>10</td><td>0.62500000</td><td>1.90768386</td><td>0.06250000</td><td>1.90767015</td></tr><tr><td></td><td>13</td><td>0.81250000</td><td>2.08668486</td><td>0.06250000</td><td>2.08666541</td></tr><tr><td>16</td><td></td><td>1.00000000</td><td>2.11800208</td><td>0.06250000</td><td>2.11797955</td></tr></table>

<table><tr><td>a.</td><td></td><td>ti Wi</td><td>hi</td><td>yi</td></tr><tr><td>5</td><td>1.10431651</td><td>1.00463041</td><td>0.02086330</td><td>1.00463045</td></tr><tr><td>15</td><td>1.31294952</td><td>1.03196889</td><td>0.02086330</td><td>1.03196898</td></tr><tr><td>25</td><td>1.59408142</td><td>1.08714711</td><td>0.03122028</td><td>1.08714722</td></tr><tr><td>35</td><td>2.00846205</td><td>1.18327922</td><td>0.04824992</td><td>1.18327937</td></tr><tr><td>45</td><td>2.66272188</td><td>1.34525123</td><td>0.07278716</td><td>1.34525143</td></tr><tr><td>52</td><td>3.40193112</td><td>1.52940900</td><td>0.11107035</td><td>1.52940924</td></tr><tr><td>57</td><td>4.00000000</td><td>1.67623887</td><td>0.12174963</td><td>1.67623914</td></tr><tr><td>b.i</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>t</td><td>Wi</td><td>hi</td><td>y</td></tr><tr><td>5</td><td>1.18519603</td><td>0.20333499</td><td>0.03703921</td><td>0.20333497</td></tr><tr><td>15</td><td>1.55558810</td><td>0.73586642</td><td>0.03703921</td><td>0.73586631</td></tr><tr><td>25</td><td>1.92598016</td><td>1.48072467</td><td>0.03703921</td><td>1.48072442</td></tr><tr><td>35</td><td>2.29637222</td><td>2.51764797</td><td>0.03703921</td><td>2.51764743</td></tr><tr><td>45</td><td>2.65452689</td><td>3.92602442</td><td>0.03092051</td><td>3.92602332</td></tr><tr><td>55</td><td>2.94341188</td><td>5.50206466</td><td>0.02584049</td><td>5,50206279</td></tr><tr><td>61</td><td>3.00000000</td><td>5.87410206</td><td>0.00122679</td><td>5.87409998</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>c. i</td><td>ti</td><td>wi</td><td>hi</td><td>yi</td></tr><tr><td>5</td><td>0.16854008</td><td>-1.83303780</td><td>0.03370802</td><td>-1.83303783</td></tr><tr><td>17</td><td>0.64833341</td><td>--1.42945306</td><td>0.05253230</td><td>-1.42945304</td></tr><tr><td></td><td>1.06742915</td><td></td><td>0.04190957</td><td>-1.21150932</td></tr><tr><td>27</td><td></td><td>-1.21150951</td><td></td><td></td></tr><tr><td>41</td><td>1.75380240</td><td>-1.05819340</td><td>0.06681937</td><td>-1.05819325</td></tr><tr><td>51</td><td>2.50124702</td><td>-1.01335240</td><td>0.07474446</td><td>-1.01335258</td></tr><tr><td>61</td><td>3.00000000</td><td>-1.00494507</td><td>0.01257155</td><td>-1.00494525</td></tr></table>

<table><tr><td>d.i</td><td></td><td>t</td><td>wi</td><td>hi</td><td>yi</td></tr><tr><td>5</td><td></td><td>0.28548652</td><td>0.32153668</td><td>0.05709730</td><td>0.32153674</td></tr><tr><td>15</td><td></td><td>0.85645955</td><td>0.24281066</td><td>0.05709730</td><td>0.24281095</td></tr><tr><td>20</td><td></td><td>1.35101725</td><td>0.15096743</td><td>0.09891154</td><td>0.15096772</td></tr><tr><td>25</td><td></td><td>1.66282314</td><td>0.09815109</td><td>0.06236118</td><td>0.09815137</td></tr><tr><td>29</td><td></td><td>1.91226786</td><td>0.06418555</td><td>0.06236118</td><td>0.06418579</td></tr><tr><td>33</td><td></td><td>2.00000000</td><td>0.05434530</td><td>0.02193303</td><td>0.05434551</td></tr></table>

5. The current after 2 s is approximately $i ( 2 ) = 8 . 6 9 3$ amperes.

# Exercise Set 5.8 (Page 312)

1. The Extrapolation Algorithm gives the results in the following tables.

<table><tr><td>a. i</td><td></td><td></td><td>wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.25</td><td>0.04543132</td><td>0.25</td><td>3</td><td>0.04543123</td></tr><tr><td></td><td>2</td><td>0.50</td><td>0.28361684</td><td>0.25</td><td>3</td><td>0.28361652</td></tr><tr><td></td><td>3</td><td>0.75</td><td>1.05257634</td><td>0.25</td><td>4</td><td>1.05257615</td></tr><tr><td></td><td>4</td><td>1.00</td><td>3.21909944</td><td>0.25</td><td>4</td><td>3.21909932</td></tr><tr><td></td><td colspan="6"></td></tr><tr><td>b.i</td><td>t</td><td></td><td>Wi</td><td>h</td><td>k</td><td>y</td></tr><tr><td>1</td><td></td><td>2.25</td><td>1.44999987</td><td>0.25</td><td>3</td><td>1.45000000</td></tr><tr><td></td><td>2</td><td>2.50</td><td>1.83333321</td><td>0.25</td><td>3</td><td>1.83333333</td></tr><tr><td></td><td>3</td><td>2.75</td><td>2.17857133</td><td>0.25</td><td>3</td><td>2.17857143</td></tr><tr><td></td><td>4</td><td>3.00</td><td>2.49999993</td><td>0.25</td><td>3</td><td>2.50000000</td></tr><tr><td></td><td colspan="6"></td></tr><tr><td>c.</td><td>i i</td><td></td><td>wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td></td><td>1</td><td>1.25</td><td>2.77892942</td><td>0.25</td><td>3</td><td>2.77892944</td></tr><tr><td></td><td>2</td><td>1.50</td><td>3.60819763</td><td>0.25</td><td>3</td><td>3.60819766</td></tr><tr><td></td><td>3</td><td>1.75</td><td>4.47932759</td><td>0.25</td><td>3</td><td>4.47932763</td></tr><tr><td></td><td>4</td><td>2.00</td><td>5.38629431</td><td>0.25</td><td>3</td><td>5.38629436</td></tr><tr><td></td><td colspan="6"></td></tr><tr><td>d.</td><td>i</td><td></td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.25</td><td>1.32914981</td><td>0.25</td><td>3</td><td>1.32914981</td></tr><tr><td>2</td><td></td><td>0.50</td><td>1.73048976</td><td>0.25</td><td>3</td><td>1.73048976</td></tr><tr><td>3</td><td></td><td>0.75</td><td>2.04147203</td><td>0.25</td><td>3</td><td>2.04147203</td></tr><tr><td>4</td><td></td><td>1.00</td><td>2.11797954</td><td>0.25</td><td>3</td><td>2.11797955</td></tr></table>

# 3.The Extrapolation Algorithm gives the results in the following tables.

<table><tr><td>a.i</td><td>t</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.50</td><td>1.06726237</td><td>0.50</td><td>4</td><td>1.06726235</td></tr><tr><td>2</td><td>2.00</td><td>1.18123223</td><td>0.50</td><td>3</td><td>1.18123222</td></tr><tr><td>3</td><td>2.50</td><td>1.30460372</td><td>0.50</td><td>3</td><td>1.30460371</td></tr><tr><td>4</td><td>3.00</td><td>1.42951608</td><td>0.50</td><td>3</td><td>1.42951607</td></tr><tr><td>5</td><td>3.50</td><td>1.55364771</td><td>0.50</td><td>3</td><td>1.55364770</td></tr><tr><td>6</td><td>4.00</td><td>1.67623915</td><td>0.50</td><td>3</td><td>1.67623914</td></tr></table>

<table><tr><td>b.i</td><td></td><td>t</td><td>Wi</td><td>h</td><td>k</td><td>y</td></tr><tr><td></td><td>1</td><td>1.50</td><td>0.64387537</td><td>0.50</td><td>4</td><td>0.64387533</td></tr><tr><td></td><td>2</td><td>2.00</td><td>1.66128182</td><td>0.50</td><td>5</td><td>1.66128176</td></tr><tr><td></td><td>3</td><td>2.50</td><td>3.25801550</td><td>0.50</td><td>5</td><td>3.25801536</td></tr><tr><td></td><td>4</td><td>3.00</td><td>5.87410027</td><td>0.50</td><td>5</td><td>5.87409998</td></tr><tr><td>c.i</td><td colspan="5"></td></tr><tr><td></td><td></td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td></td><td>0.50</td><td>-1.53788284</td><td>0.50</td><td>4</td><td>-1.53788284</td></tr><tr><td></td><td>2</td><td>1.00</td><td>-1.23840584</td><td>0.50</td><td>5</td><td>-1.23840584</td></tr><tr><td></td><td>3</td><td>1.50</td><td>-1.09485175</td><td>0.50</td><td>5</td><td>-1.09485175</td></tr><tr><td></td><td>4</td><td>2.00</td><td>-1.03597242</td><td>0.50</td><td>5</td><td>--1.03597242</td></tr><tr><td>5</td><td></td><td>2.50</td><td>-1.01338570</td><td>0.50</td><td>5</td><td>-1.01338570</td></tr><tr><td>6</td><td></td><td>3.00</td><td>-1.00494526</td><td>0.50</td><td>4</td><td>-1.00494525</td></tr><tr><td></td><td colspan="6"></td></tr><tr><td></td><td>d.i</td><td>ti</td><td>W</td><td>h</td><td>k</td><td>yi</td></tr><tr><td></td><td>1</td><td>0.50</td><td>0.29875177</td><td>0.50</td><td>4</td><td>0.29875178</td></tr><tr><td></td><td>2</td><td>1.00</td><td>0.21662642</td><td>0.50</td><td>4</td><td>0.21662642</td></tr><tr><td></td><td>3</td><td>1.50</td><td>0.12458565</td><td>0.50</td><td>4</td><td>0.12458565</td></tr><tr><td>4</td><td></td><td>2.00</td><td>0.05434552</td><td>0.50</td><td>4</td><td>0.05434551</td></tr></table>

# Exercise Set 5.9 (Page 322)

1. The Runge-Kutta for Systems Algorithm gives the results in the following tables.

<table><tr><td>a.t</td><td>W1i</td><td>W1i</td><td>W2i</td><td></td><td>u2i</td></tr><tr><td>0.200</td><td>2.12036583</td><td>2.12500839</td><td>1.50699185</td><td>1.51158743</td><td></td></tr><tr><td>0.400</td><td>4.44122776</td><td>4.46511961</td><td>3.24224021</td><td>3.26598528</td><td></td></tr><tr><td>0.600</td><td>9.73913329</td><td>9.83235869</td><td>8.16341700</td><td>8.25629549</td><td></td></tr><tr><td>0.800</td><td>22.67655977</td><td>23.00263945</td><td>21.34352778</td><td>21.66887674</td><td></td></tr><tr><td>1.000</td><td>55.66118088</td><td>56.73748265</td><td>56.03050296</td><td>57.10536209</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>b. W1i t</td><td colspan="5">u1i W2i u2i</td></tr><tr><td>0.500</td><td>0.95671390</td><td>0.95672798</td><td>-1.08381950</td><td>-1.08383310</td><td></td></tr><tr><td>1.000</td><td>1.30654440</td><td>1.30655930</td><td>-0.83295364</td><td>-0.83296776</td><td></td></tr><tr><td>1.500</td><td>1.34416716</td><td>1.34418117</td><td>-0.56980329</td><td>-0.56981634</td><td></td></tr><tr><td>2.000</td><td>1.14332436</td><td>1.14333672</td><td>-0.36936318</td><td>-0.36937457</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td colspan="5"></td></tr><tr><td>t c.</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td><td>W3i</td><td>3i</td></tr><tr><td>0.5</td><td>0.70787076</td><td>0.70828683</td><td>-1.24988663</td><td>-1.25056425</td><td>0.39884862</td><td>0.39815702</td></tr><tr><td>1.0</td><td>-0.33691753</td><td>-0.33650854</td><td>-3.01764179</td><td>-3.01945051</td><td>-0.29932294</td><td>-0.30116868</td></tr><tr><td>1.5</td><td>-2.41332734</td><td>-2.41345688</td><td>-5.40523279</td><td>-5.40844686</td><td>-0.92346873</td><td>-0.92675778</td></tr><tr><td>2.0</td><td>-5.89479008</td><td>-5.89590551</td><td>-8.70970537</td><td>-8.71450036</td><td>-1.32051165</td><td>-1.32544426</td></tr><tr><td>d.ti</td><td>Wii</td><td>u1i</td><td>W2i</td><td>u2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.2</td><td>1.38165297</td><td>1.38165325</td><td>1.00800000</td><td>1.00800000</td><td>-0.61833075</td><td>-0.61833075</td></tr><tr><td>0.5</td><td>1.90753116</td><td>1.90753184</td><td>1.12500000</td><td>1.12500000</td><td>-0.09090565</td><td>-0.09090566</td></tr><tr><td>0.7</td><td>2.25503524</td><td>2.25503620</td><td>1.34300000</td><td>1.34000000</td><td>0.26343971</td><td>0.26343970</td></tr><tr><td>1.0</td><td>2.83211921</td><td>2.83212056</td><td>2.00000000</td><td>2.00000000</td><td>0.88212058</td><td>0.88212056</td></tr></table>

5. The Adams fourth-order predictor-corrector method for systems gives the results in the following tables

<table><tr><td>a.</td><td>t</td><td>W</td><td>y(ti)</td></tr><tr><td rowspan="5"></td><td>0.200</td><td>0.00015352</td><td>0.00015350 0.00743027</td></tr><tr><td>0.500</td><td>0.00743133</td><td>0.03299805</td></tr><tr><td>0.700</td><td>0.03300266</td><td></td></tr><tr><td>1.000</td><td>0.17134711</td><td>0.17132880</td></tr><tr><td></td><td></td><td>y(ti)</td></tr><tr><td rowspan="5">c.</td><td>l</td><td>Wi</td><td></td></tr><tr><td>1.000</td><td>3.73186337</td><td>3.73170445</td></tr><tr><td>2.000</td><td>11.31462595</td><td>11.31452924</td></tr><tr><td></td><td></td><td></td></tr><tr><td>3.000</td><td>34.04548233</td><td>34.04517155</td></tr></table>

<table><tr><td>b. ti 1.200</td><td>W1i 0.96152437</td><td>y(t) 0.96152583</td></tr><tr><td>1.500 1.700 2.000</td><td>0.77796798 0.59373213 0.27258055</td><td>0.77797237 0.59373830 0.27258872</td></tr><tr><td></td><td></td><td></td></tr><tr><td>d. t 1.200</td><td>Wi 0.27273759</td><td>y(t) 0.27273791</td></tr><tr><td>1.500</td><td></td><td></td></tr><tr><td>1.700</td><td>1.08847933</td><td>1.08849259</td></tr><tr><td>2.000</td><td>2.04352376 4.36157310</td><td>2.04353642 4.36157780</td></tr></table>

7. The predicted number of prey, $x _ { 1 i }$ ， and predators, $\boldsymbol { x } _ { 2 i }$ ,are given in the following table.

<table><tr><td>i </td><td>X1i</td></tr><tr><td>10 1.0</td><td>X2i 4393 1512</td></tr><tr><td>20 2.0</td><td>288 3175</td></tr><tr><td>30 3.0</td><td>32 2042</td></tr><tr><td>40 4.0</td><td>25 1258</td></tr></table>

# Exercise Set 5.10 (Page 333)

1. Let $L$ be the Lipschitz constant for $\phi$ . Then

$$
u _ { i + 1 } - v _ { i + 1 } = u _ { i } - v _ { i } + h [ \phi ( t _ { i } , u _ { i } , h ) - \phi ( t _ { i } , v _ { i } , h ) ] ,
$$

S0

$$
\begin{array} { r } { | u _ { i + 1 } - v _ { i + 1 } | \leq ( 1 + h L ) | u _ { i } - v _ { i } | \leq ( 1 + h L ) ^ { i + 1 } | u _ { 0 } - v _ { 0 } | . } \end{array}
$$

3.By Exercise 17 in Section 5.4, we have

$$
\begin{array} { l } { \displaystyle { \phi ( t , w , h ) = \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f \bigg ( t + \frac 1 2 h , w + \frac 1 2 h f ( t , w ) \bigg ) } } \\ { \displaystyle { \qquad + \frac { 1 } { 3 } f \bigg ( t + \frac 1 2 h , w + \frac { 1 } { 2 } h f \bigg ( t + \frac 1 2 h , w + \frac 1 2 h f ( t , w ) \bigg ) \bigg ) } } \\ { \displaystyle { \qquad + \frac { 1 } { 6 } f \bigg ( t + h , w + h f \bigg ( t + \frac 1 2 h , w + \frac 1 2 h f \bigg ( t + \frac 1 2 h , w + \frac 1 2 h f ( t , w ) \bigg ) \bigg ) \bigg ) , } } \end{array}
$$

$$
\phi ( t , w , 0 ) = \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 6 } f ( t , w ) = f ( t , w ) .
$$

5. a. The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } = \frac { 1 } { 4 } h ^ { 3 } y ^ { ( 4 ) } ( \xi _ { i } ) } \end{array}$ ， for some $\xi$ ， where $t _ { i - 2 } < \xi _ { i } < t _ { i + 1 }$ b.The method is consistent but unstable and not convergent.

7. The method is unstable.

# Exercise Set 5.11 (Page 340)

1.Euler's method gives the results in the following tables.

<table><tr><td rowspan="7">a. c.</td><td>t</td><td>Wi</td><td>y</td></tr><tr><td>0.200 0.500 0.700</td><td>0.027182818 0.000027183 0.000000272</td><td>0.449328964 0.030197383 0.004991594</td></tr><tr><td>1.000</td><td>0.000000000</td><td>0.000335463</td></tr><tr><td></td><td></td><td></td></tr><tr><td>i</td><td>Wi</td><td>yi</td></tr><tr><td>0.500 1.000</td><td>16.47925 256.7930</td><td>0.479470939 0.841470987</td></tr><tr><td>1.500 2.000</td><td>4096.142 65523.12</td><td>0.997494987 0.909297427</td></tr></table>

<table><tr><td>b.</td><td>t</td><td>Wi</td><td>yi</td></tr><tr><td rowspan="5"></td><td>0.200</td><td>0.373333333</td><td>0.046105213</td></tr><tr><td>0.500</td><td>-0.093333333</td><td>0.250015133</td></tr><tr><td>0.700</td><td>0.146666667</td><td>0.490000277</td></tr><tr><td>1.000</td><td>1.333333333</td><td>1.000000001</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td>d.</td><td>t Wi</td><td>yi</td></tr><tr><td>0.200</td><td>6.128259</td><td>1.000000001</td></tr><tr><td>0.500</td><td>-378.2574</td><td>1.000000000</td></tr><tr><td>0.700</td><td>-6052.063</td><td>1.000000000</td></tr><tr><td>1.000</td><td>387332.0</td><td>1.000000000</td></tr></table>

# 3.The Adams Fourth-Order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td rowspan=5 colspan=1>a.    i                         Wi                            yi0.200               0.4588119           0.44932900.500            -0.0112813           0.03019740.700               0.0013734           0.00499161.000               0.0023604           0.0003355</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td>b.</td><td>t</td><td>w</td><td>yi</td></tr><tr><td rowspan="5">0.200</td><td>0.0792593</td><td>0.0461052</td><td rowspan="2">0.2500151</td></tr><tr><td>0.500</td><td>0.1554027</td></tr><tr><td></td><td>0.5507445</td><td>0.4900003</td></tr><tr><td>0.700 1.000</td><td>0.7278557</td><td></td></tr><tr><td></td><td></td><td>1.0000000</td></tr></table>

<table><tr><td>d. t</td><td>Wi</td><td>yi</td></tr><tr><td>0.200</td><td>-215.7459</td><td>1.000000001</td></tr><tr><td>0.500</td><td>-682637.0</td><td>1.000000000</td></tr><tr><td>0.700</td><td>-159172736</td><td>1.000000000</td></tr><tr><td>1.000</td><td>-566751172258</td><td>1.000000000</td></tr></table>

<table><tr><td>5. a.ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td></tr><tr><td>0.100</td><td>-96.33011</td><td>0.66987648</td><td>193.6651</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>-28226.32</td><td>0.67915383</td><td>56453.66</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>-8214056</td><td>0.69387881</td><td>16428113</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>-2390290586</td><td>0.71354670</td><td>4780581173</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>-695574560790</td><td>0.73768711</td><td>1391149121600</td><td>-0.36884355</td></tr></table>

<table><tr><td>b. t</td><td>Wi</td><td>ui</td><td>W2i</td><td>u2i</td></tr><tr><td>0.100</td><td>0.61095960</td><td>0.66987648</td><td>-0.21708179</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>0.66873489</td><td>0.67915383</td><td>-0.31873903</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>0.69203679</td><td>0.69387881</td><td>-0.34325535</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>0.71322103</td><td>0.71354670</td><td>-0.35612202</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>0.73762953</td><td>0.73768711</td><td>-0.36872840</td><td>-0.36884355</td></tr></table>

9.a. The Trapezoidal method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { 1 + { \frac { h \lambda } { 2 } } } { 1 - { \frac { h \lambda } { 2 } } } } \ w _ { j } ,
$$

so

$$
Q ( h \lambda ) = \frac { 2 + h \lambda } { 2 - h \lambda } .
$$

Thus, $| Q ( h \lambda ) | < 1$ ， whenever $\mathtt { R e } ( h \lambda ) < 0$

b. The Backward Euler method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { w _ { j } } { 1 - \hbar \lambda } } ,
$$

So

$$
Q ( h \lambda ) = { \frac { 1 } { 1 - h \lambda } } .
$$

Thus, $| Q ( h \lambda ) | < 1$ ，whenever $\mathtt { R e } ( h \lambda ) < 0$

# Exercise Set 6.1 (Page 356)

1.a. Intersecting lines with solution $x _ { 1 } = x _ { 2 } = 1$ b. Intersecting lines with solution $x _ { 1 } = x _ { 2 } = 0$ c. One line,so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = \frac { 3 } { 2 } - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ d. Parallel lines, so there is no solution. e. One line,so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ f. Three lines in the plane that do not intersect at a common point. g. Intersecting lines with solution x1 =  and x2 =-. h.Two planes in space which intersect in a line with $\begin{array} { r } { x _ { 1 } = - \frac { 5 } { 4 } x _ { 2 } } \end{array}$ and $x _ { 3 } = { \textstyle \frac { 3 } { 2 } } x _ { 2 } + 1$

3. Gaussian elimination gives the following solutions.

a. $x _ { 1 } = 1 . 1 8 7 5$ ， $x _ { 2 } = 1 . 8 1 2 5$ ， $x _ { 3 } = 0 . 8 7 5$ with one row interchange required b. $x _ { \textrm { i } } = - 1$ ， $x _ { 2 } = 0$ ， $x _ { 3 } = 1$ with no interchange required c. $x _ { 1 } = 1 . 5$ ， $x _ { 2 } = 2$ ， $x _ { 3 } = - 1 . 2 , x _ { 4 } =$ with no interchange required d $\begin{array} { r } { x _ { 1 } = \frac { 2 2 } { 9 } } \end{array}$ ， $\textstyle x _ { 2 } = - { \frac { 4 } { 9 } }$ ， $\begin{array} { r } { x _ { 3 } = \frac { 4 } { 3 } } \end{array}$ ， $x _ { 4 } = 1$ with onerow interchangerequired e. No unique solution f. $x _ { 1 } = - 1$ ， $x _ { 2 } = 2$ ， $x _ { 3 } = 0$ ， $x _ { 4 } = 1$ with one row interchange required

5.a. When $\alpha = - 1 / 3$ ，there is no solution.

b. When $\alpha = 1 / 3$ ,there is an infinite number of solutions with $x _ { \mathrm { { I } } } = x _ { 2 } + 1 . 5$ and $x _ { 2 }$ is arbitrary.

c. If $\alpha \neq \pm 1 / 3$ , then the unique solution is

$$
x _ { 1 } = \frac { 3 } { 2 ( 1 + 3 \alpha ) } \quad \mathrm { a n d } \quad x _ { 2 } = \frac { - 3 } { 2 ( 1 + 3 \alpha ) } .
$$

9.The Gauss-Jordan method gives the following results.

a. $x _ { 1 } = 0 . 9 8 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$ b. $x _ { 1 } = 1 . 1$ ， $x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

11.b.Theresults for this exercise are listed in thefollowing table.(The abbreviations M/Dand A/S are used for multiplications/divisions and additions/subtractions,respectively.)

<table><tr><td></td><td colspan="2">Gaussian ] Elimination</td><td colspan="2">Gauss-Jordan</td></tr><tr><td>n</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td></tr><tr><td>3</td><td>17</td><td>11</td><td>21</td><td>12</td></tr><tr><td>10</td><td>430</td><td>375</td><td>595</td><td>495</td></tr><tr><td>50</td><td>44150</td><td>42875</td><td>64975</td><td>62475</td></tr><tr><td>100</td><td>343300</td><td>338250</td><td>509950</td><td>499950</td></tr></table>

13.The Gaussian-Elimination-Gauss-Jordan hybrid method gives the following results.

a. $x _ { 1 } = 1 . 0 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$   
b. $x _ { 1 } = 1 . 0$ $1 . 0 , x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

15.a. There is sufficient food to satisfy the average daily consumption. b. We could add 200 of species 1,or 150 of species 2,or 100 of species 3,or 100 of species 4. c.Assuming none of the increases indicated in part (b)was selected,species 2 could be increased by 650,or species 3 could be increased by 150,or species 4 could be increased by 150. d.Assuming none of the increases indicated in parts (b)or (c)were selected,species 3 could be increased by 150. or species 4 couid be increased by 150.

# Exercise Set 6.2 (Page 368)

1.a.none b. Interchange rows 2 and 3. c. none d. Interchange rows 1 and 2.

3. a. Interchange rows 1 and 3, then interchange rows 2 and 3. b. Interchange rows 2 and 3. c. Interchange rows 2 and 3. d.Interchange rows 1 and 3,then interchange rows 2 and 3.

5.Gaussian elimination with three-digit chopping arithmetic gives the following results.

a. $x _ { 1 } = 3 0 . 0$ ， $x _ { 2 } = 0 . 9 9 0$   
b. $x _ { 1 } = 1 . 0 0$ ， $x _ { 2 } = 9 . 9 8$   
c. $x _ { 1 } = 0 . 0 0$ ， $x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 1 4 2$   
d. $x _ { 1 } = 1 2 . 0 , x _ { 2 } = 0 . 4 9 2 , x _ { 3 } = - 9 . 7 8$   
e. $x _ { 1 } = 0 . 2 0 6$ ， $x _ { 2 } = 0 . 0 1 5 4 , x _ { 3 } = - 0 . 0 1 5 6 , x _ { 4 } = - 0 . 7 1 6$ f $x _ { 1 } = 0 . 8 2 8$ $x _ { 2 } = - 3 . 3 2 , x _ { 3 } = 0 . 1 5 3 , x _ { 4 } = 4 . 9 1$

7. Gaussian elimination with partial pivoting and three-digit chopping arithmetic gives the folowing results.

a. $x _ { 1 } = 1 0 . 0$ ， $x _ { 2 } = 1 . 0 0$   
b. $x _ { 1 } = 1 . 0 0$ ， $x _ { 2 } = 9 . 9 8$   
c. $x _ { 1 } = - 0 . 1 6 3$ ， $x _ { 2 } = 9 . 9 8 , x _ { 3 } = 0 . 1 4 2$