Lemma 4.4. If $z = r e ^ { \imath \theta }$ and $r  \infty$ ,then $z \in A$ for $\pi / 2 < \theta < 3 \pi / 2$ and $z \not \in A$ $f o r \ : - \pi / 2 < \theta < \pi / 2$ . The border $\partial A$ possesses only two branches which $g o$ to infinity. If

$$
R ( z ) = K z ^ { \ell } + \mathcal O ( z ^ { \ell - 1 } ) \qquad \mathrm { f o r } \quad z \to \infty ,
$$

these branches asymptotically approach

$$
x = \log | K | + \ell \log | y |
$$

Proof. The first assertion is the well-known fact that the exponential function, for $\mathrm { R e } z  \pm \infty$ is much stronger than any polynomial or rational function. In order to show the uniqueness of the border lines, we consider for $r  \infty$ the two functions

$$
\begin{array} { l } { { \varphi _ { 1 } ( \theta ) = | e ^ { z } | ^ { 2 } = e ^ { 2 r \cos \theta } } } \\ { { \varphi _ { 2 } ( \theta ) = | R ( z ) | ^ { 2 } = R ( r e ^ { \imath \theta } ) R ( r e ^ { - \imath \theta } ) . } } \end{array}
$$

Differentiation gives

$$
\frac { \varphi _ { 1 } ^ { \prime } } { \varphi _ { 1 } } = - 2 r \sin \theta , \qquad \frac { \varphi _ { 2 } ^ { \prime } } { \varphi _ { 2 } } = 2 r \mathrm { R e } \left( i e ^ { \imath \theta } \cdot \frac { R ^ { \prime } ( r e ^ { i \theta } ) } { R ( r e ^ { i \theta } ) } \right) .
$$

Since $| R ^ { \prime } / R |  0$ for $r  \infty$ , we have

$$
\frac { d } { d \theta } \log \varphi _ { 1 } ( \theta ) < \frac { d } { d \theta } \log \varphi _ { 2 } ( \theta ) \qquad \mathrm { f o r } \quad \theta \in [ \varepsilon , \pi - \varepsilon ] .
$$

Hence in this interval there can only be one value of $\theta$ with $\varphi _ { 1 } ( \theta ) = \varphi _ { 2 } ( \theta )$ .Formula (4.4) is obtained from (4.3) by

$$
| K | ( x ^ { 2 } + y ^ { 2 } ) ^ { \ell / 2 } \approx e ^ { x } , \qquad \log | K | + { \frac { \ell } { 2 } } \log ( x ^ { 2 } + y ^ { 2 } ) \approx x
$$

and by neglecting $x ^ { 2 }$ ，which is justified because $x / y  0$ whenever $x + i y$ tends to infinity on the border of $A$ . □

It is clear from the maximum principle that each bounded “finger” of $A$ in Fig. 4.2 must contain a pole of $q ( z )$ . A still stronger result is the following:

Lemma 4.5. Each bounded subset $F \subset A$ with common boundary $\partial F \subset \partial A$ collecting m sectors at the origin must contain at least m poles of $q ( z )$ (each counted according to its multiplicity). Analogously, each bounded “white" subset $F \subset \mathbb { C } \backslash A$ with m sectors at the origin must contain at least m zeros of $q ( z )$

Proof.Suppose first that $\partial F$ is represented by a parametrized positively oriented loop $c ( t )$ ， $t _ { 0 } \leq t \leq t _ { 1 }$ .Let $\vec { a } = \left( c _ { 1 } ^ { \prime } ( t ) , c _ { 2 } ^ { \prime } ( t ) \right)$ be the tangent vector and $\vec { n } = \left( c _ { 2 } ^ { \prime } ( t ) , - c _ { 1 } ^ { \prime } ( t ) \right)$ an exterior normal vector. We write

$$
q ( z ) = r ( x , y ) \cdot e ^ { \imath \varphi ( x , y ) } , \qquad z = x + i y
$$

so that $\log q ( z ) = \log r ( x , y ) + i \varphi ( x , y )$ . Since the modulus increases inside $F$ ， we have

$$
\frac { \partial ( \log r ) } { \partial \vec { n } } \leq 0 .
$$

Now the Cauchy-Riemann diferential equations for $\log q$ are

$$
{ \frac { \partial ( \log r ) } { \partial x } } = { \frac { \partial \varphi } { \partial y } } ; \qquad { \frac { \partial ( \log r ) } { \partial y } } = - { \frac { \partial \varphi } { \partial x } } ,
$$

so that (4.6) becomes

$$
\frac { \partial \varphi } { \partial \vec { a } } \leq 0 .
$$

This inequality is strict except at a finite number of points,because $q ^ { \prime } ( c ( t ) ) \cdot c ^ { \prime } ( t ) =$ $i \cdot q ( c ( t ) ) \cdot \partial \varphi / \partial \vec { a }$ and the number of zeros of $q ^ { \prime } ( z )$ is finite. Thus the argument of $q$ decreases along $c$ . If the contour curve $c ( t )$ returns $m$ times to the origin, where the argument is a multiple of $2 \pi$ , the vector $q ( z )$ must perform at least $m$ complete revolutions in the negative sense (Fig.4.3). Thus the argument principle (an idea which we have already encountered in Sect.I.13; see Volume I, pages 81 and 382), ensures the presence of at least $m$ poles inside $\boldsymbol { F }$ (there are no zeros, because these are not in $A$ ).

If the boundary curve is represented by several curves, all rotation numbers are added up. For“white” subsets the proof is similar, just that $\partial ( \log r ) / \partial { \vec { n } } > 0$ and the argument rotates in the other sense. □

![](images/c58e7fd32341071483be7bde2645eab71254b925606273d323a3faa2f4111650.jpg)  
Fig. 4.3. SDIRK methods, order 3; arrows indicate direction of $q ( z )$

Fig. 4.3 gives an illustration of two order stars for the SDIRK methods of order 3 (Table 3.1, case e). Here, $q ( z )$ possesses a double pole at $z = 1 / \gamma$ . However, for $\gamma = ( 3 - \sqrt { 3 } ) / 6$ , the bounded component $F$ of $A$ collects only one sector at the origin. Since the vector $q ( z )$ performs two rotations, there is in addition to the origin a second point on $\partial { \cal F }$ for which $\arg ( q ) = 0$ ,i.e., $\arg ( R ( z ) ) = \arg ( e ^ { z } )$ Thus, because $| R ( z ) | = | e ^ { z } |$ on $\partial A$ , we have $R ( z ) = e ^ { z }$ . These points are called exponential fitting points. Another version of Lemma 4.5 is thus (Iserles 1981):

Lemma $4 . 5 ^ { \circ }$ . Each bounded subset $F \subset A$ with $\partial F \subset \partial A$ contains exactly as many poles as there are exponential fitting points on its boundary. □

# Order and Stability for Rational Approximations

In the sequel we suppose $R ( z )$ to be an arbitrary rational approximation of order $p$ with $k$ zeros and $j$ poles.

Theorem 4.6. If $R ( z )$ is $A$ -stable, then $p \leq 2 k _ { 1 } + 2$ ，where $k _ { 1 }$ is the number of different zeros of $R ( z )$ in $\mathbb { C } ^ { - }$

Proof. At least $\left[ ( p + 1 ) / 2 \right]$ sectors of $A$ start in $\mathbb { C } ^ { - }$ (Lemma 4.3). By $A$ -stability these have to be infinite and enclose at least $[ ( p + 1 ) / 2 ] - 1$ bounded white fingers, each containing at least one zero by Lemma 4.5. Therefore $[ ( p + 1 ) / 2 ] - 1 \le k _ { 1 }$ □

Theorem 4.7. If $R ( z )$ is $I$ -stable, then $p \leq 2 j _ { 1 }$ ，where $j _ { 1 } ^ { \mathrm { ~ ~ } }$ is the number of poles of $R ( z )$ in $\mathbb { C } ^ { + }$ .

Proof. At least $\{ ( p + 1 ) / 2 \}$ sectors of $A$ start in $\mathbb { C } ^ { + }$ ．They cannot cross $i \mathbb { R }$ and must therefore be bounded (Lemma 4.4). Again by Lemma 4.5 we have $[ ( p +$ $1 ) / 2 ] \leq j _ { 1 }$ · □

Theorem 4.8. Suppose that $p \geq 2 j - 1$ and $| R ( \infty ) | \leq 1$ . Then, $R ( z )$ is $A$ -stable.

Proof. By Proposition 3.6 the function $R ( z )$ is $I$ -stable. Applying Theorem 4.7 we get $j _ { 1 } \geq j$ so that $I$ -stability implies $A$ -stability. □

Theorem 4.9 (Crouzeix & Ruamps 1977). Suppose $p \geq 2 j - 2$ ， $| R ( \infty ) | \leq 1$ ,and the coefficients of the denominator $Q ( z )$ have alternating signs. Then, $R ( z )$ is A-stable.

Proof. A similar argument as in the foregoing proof allows at most one pole in $\mathbb { C } ^ { - }$ ： It would then be real and its existence would contradict the hypothesis on signs of $Q ( z )$ □

Theorem 4.10. Suppose $p \ge 2 j - 3 , R ( z$ $R ( z )$ is $I$ -stable,and thecoefficientsof $Q ( z )$ have alternating signs. Then, $R ( z )$ is $A$ -stable.

Proof.For $p \geq 2 j - 3$ the argument of the foregoing proof is still valid. However Proposition 3.6 is no longer applicable and we need the hypothesis on $I$ -stability.

We see from Fig.4.2 that all poles and all zeros for Padé approximations must be simple. Whenever two poles coalesce, the corresponding sectors create a bounded white finger between them with the need for an additional zero. Thus the presence of multiple zeros or poles will require an order reduction.

Theorem 4.11. Let $R ( z )$ possess $k _ { 0 }$ distinct zeros and $j _ { 0 }$ distinct poles. Then, $p \leq k _ { 0 } + j _ { 0 }$

![](images/2561eecb3c37c7a2b26e1830ecffb96105ace9e7a920274531a4aeb38f4be604.jpg)  
Fig.4.4. Order star on Gaussian sphere

Proof. We identify the complex plane with the Gaussian sphere and the order star with a CW-complex decomposition of this sphere (Fig. 4.4). Let $s _ { 2 }$ be the number of 2-cells $f _ { i } , s _ { 1 }$ the number of 1-cells $l _ { i }$ (paths),and $s _ { 0 }$ the number of vertices. Then Euler's polyhedral formula ( ${ } ^ { 6 6 } \mathrm { S i }$ enim numerus angulorum solidorum fuerit $= S$ , numerus acierum $= A$ et numerus hedrarum $= H$ , semper habetur $S + H =$ $A + 2$ , hincque vel $S = A + 2 - H$ vel $H = A + 2 - S$ vel $A = S + H - 2$ ,quae relationis simplicitas ob demonstrationis difficultatem ...",Euler(1752)),implies

$$
s _ { 0 } - s _ { 1 } + s _ { 2 } = 2 .
$$

Modern versions are in any book on algebraic topology,for particularly easy read-ing see e.g. Massey (1980, p.87, Corollary 4.4). Formula (4.9) is only true if all $f _ { i }$ are homeomorphic to disks. Otherwise, they have to be cut into disks by additional paths (dotted in Fig. 4.4). So, in general, we have

$$
s _ { 0 } - s _ { 1 } + s _ { 2 } \geq 2 .
$$

Since each vertex is reached by at least 2 paths, the origin by hypothesis by $2 p + 2$ ， and since every path has two extremities, we have

$$
s _ { 1 } - s _ { 0 } \geq p .
$$

By Lemma 4.5 each 2-cell, with the exception of two (the two “infinite"ones) must contain at least a pole or a zero, so we have

$$
s _ { 2 } \leq k _ { 0 } + j _ { 0 } + 2 .
$$

These three inequalities give $p \leq k _ { 0 } + j _ { 0 }$

# Stability of Padé Approximations

... evidence is given to suggest that these are the only L-acceptable Padé approximations to the exponential.

(B.L.Ehle 1973)

Theorem 4.12. A Padé approximation $R _ { k j } ( z )$ ， given in (3.30), is A-stable if and only if $k \leq j \leq k + 2$ . All zeros and all poles are simple.

Proof. The “if-part is a consequence of Theorem 4.9. The “only if"-part follows from Theorem 4.6 since $p = k + j$ . For the same reason Theorem 4.11 shows that all poles and zeros are simple. □

# Comparing Stability Domains

Da ist der allerärmste Mann dem ander'n viel zu reich, das Schicksal setzt den Hobel an und hobelt beide gleich.

(F.Raimund,das Hobellied)

Jeltsch & Nevanlinna (1978) proved the following“disk theorem": If $S$ is the stability domain of an s -stage explicit Runge-Kutta method and $D$ the disk with centre -s and radius s (i.e the stability domain of $s$ explicit Euler steps with step size $h / s )$ ,then

$$
S \nsim D
$$

unless $S = D$ and the method in question is Euler's method. This curious result expresses the fact that Euler's method is “the most stable” of all methods with equal numerical work. After the discovery of order stars it became clear that the result is much more general and that any method has the same property (Jeltsch & Nevanlinna 1981). We shall also see in Chapter V that this result generalizes to many multistep methods. The main tool of this theory is

Definition 4.13. Let $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ be rational approximations to $e ^ { z }$ ,then their relative order star is defined as

$$
B = \left. z \in \mathbb { C } \textrm { ; } \left| \frac { R _ { 1 } ( z ) } { R _ { 2 } ( z ) } \right| > 1 \right. .
$$

Here, the stability function for method 1 is compared to the stability function for method 2 instead of to the exact solution $e ^ { z }$ . The following order relations

lead, by subtraction, to

$$
\begin{array} { r } { e ^ { z } - R _ { 1 } ( z ) = C _ { 1 } z ^ { p _ { 1 } + 1 } + \dots } \\ { e ^ { z } - R _ { 2 } ( z ) = C _ { 2 } z ^ { p _ { 2 } + 1 } + \dots . } \end{array}
$$

$$
\frac { R _ { 1 } ( z ) } { R _ { 2 } ( z ) } = 1 - C z ^ { p + 1 } + . . .
$$

where $p = \operatorname* { m i n } ( p _ { 1 } , p _ { 2 } )$ and

$$
C = \left\{ \begin{array} { l l } { C _ { 1 } - C _ { 2 } } & { \mathrm { i f } \ p _ { 1 } = p _ { 2 } } \\ { C _ { 1 } } & { \mathrm { i f } \ p _ { 1 } < p _ { 2 } } \\ { - C _ { 2 } } & { \mathrm { i f } \ p _ { 1 } > p _ { 2 } . } \end{array} \right.
$$

Remark 4.14. The statement of Lemma 4.3 remains unchanged for $B$ ，whenever $C \neq 0$ . Since the fraction $R _ { 1 } ( z ) / R _ { 2 } ( z )$ has no essential singularity at infinity, there is no analogue of Lemma 4.4. Further, the boundedness assumption on $\boldsymbol { F }$ can be omitted in Lemmas 4.5 and $4 . 5 '$ (if $\infty$ is a pole of $R _ { 1 } ( z ) / R _ { 2 } ( z )$ , it has to be counted also). With the correspondences displayed in Table 4.1, the statements of Theorems 4.6 and 4.7 remain true for $B$ .

Table 4.1. Correspondences between $A$ and $B$   

<table><tr><td>order star A (4.1)</td><td>←</td><td>relative order star B (4.13)</td></tr><tr><td>imaginary axis</td><td>←</td><td>aS2</td></tr><tr><td>Ci</td><td>←→</td><td>interior of S2</td></tr><tr><td>C+</td><td>←→</td><td>exterior of S2</td></tr><tr><td>method A-stable</td><td>←</td><td>S1U S2</td></tr><tr><td>p</td><td>←</td><td>min(p1,P2)</td></tr></table>

Theorem 4.15. If $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ are polynomial stability functions of degree s and orders $\geq 1$ ,then the corresponding stability domains satisfy

$$
S _ { 1 } \not \supset S _ { 2 } \qquad a n d \qquad S _ { 1 } \not \subset S _ { 2 } .
$$

Proof. Suppose that $S _ { 1 } \supset S _ { 2 }$ (i.e., by Table 4.1, suppose “ $A$ -stability"). Then the analogue of Theorem 4.7 requires that $R _ { 1 } ( z ) / R _ { 2 } ( z )$ have a pole outside $S _ { 2 }$ . Since

$R _ { 1 } ( z )$ and $R _ { 2 } \{ z \}$ have the same degree, $R _ { 1 } ( z ) / R _ { 2 } ( z )$ has no pole at infinity. Therefore the only poles of $R _ { 1 } ( z ) / R _ { 2 } ( z )$ are the zeros of $R _ { 2 } \{ z \}$ and these are inside $S _ { 2 }$ . This is a contradiction and proves the first part of (4.16). The second part is obtained by exchanging $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ □

In order to compare numerical methods with different numerical work, we consider scaled stability domains.

Definition 4.16. Let $R \{ z \}$ be the stability function of degree $s$ of an explicit Runge-Kutta method (usually with $s$ stages), then

$$
S ^ { s c a l } = \left\{ z \ ; \ | R ( s z ) | \leq 1 \right\} = \left\{ z \ ; \ s \cdot z \in S \right\} = \frac { 1 } { s } S
$$

will be called the scaled stability domain of the method.

![](images/2febbcb81146ca03c14f1f7778f884448dd145e45a8e0f48f63cd767166733d6.jpg)  
Fig. 4.5. Scaled stability domains for Taylor methods (2.12)

Theorem 4.17 (Jeltsch & Nevanlinna 1981). If $R _ { 1 } ( z )$ and $R _ { 2 } \{ z \}$ are the stability functions of degrees $s _ { 1 }$ resp. $s _ { 2 }$ of two explicit Runge-Kutta methods of orders $\geq 1$ , then

$$
S _ { 1 } ^ { s c a l } \not \supset S _ { 2 } ^ { s c a l } \qquad a n d \qquad S _ { 1 } ^ { s c a l } \not \subset S _ { 2 } ^ { s c a l } ,
$$

i.e., a scaled stability domain can never completely contain another.

The interesting interpretation of this result is that for any two methods, there exists a differential equation $y \prime = \lambda y$ such that one of them performs better than the other.No “miracle” method is possible.

Proof. We compare $s _ { 2 }$ steps of method 1 with step size $h / s _ { 2 }$ to $s _ { 1 }$ steps of method 2 with step size $h / s _ { 1 }$ . Both procedures then have comparable numerical work for the same advance in step size. Applied to $y ^ { \prime } = \lambda y$ , this compares

$$
\left( R _ { 1 } \big ( \frac { z } { s _ { 2 } } \big ) \right) ^ { s _ { 2 } } \qquad 1 0 \qquad \left( R _ { 2 } \big ( \frac { z } { s _ { 1 } } \big ) \right) ^ { s _ { 1 } }
$$

of the same degree. Theorem 4.15 now gives

$$
s _ { 2 } \cdot S _ { 1 } \ \not \supset \ s _ { 1 } \cdot S _ { 2 } \qquad \mathrm { o r } \qquad S _ { 1 } ^ { s c a l } \not \supset S _ { 2 } ^ { s c a l } .
$$

As an illustration to this theorem,we present in Fig.4.5 the scaled stability domains for the Taylor methods of orders 1,2,3,4 (compare with Fig.2.1). It can clearly be observed that none of them contains another.

# Rational Approximations with Real Poles

The surprising result is that the maximum reachable order is $m + 1$ ， (Ngrsett & Wolfbrandt 1977)

The stability functions of diagonally implicit Runge-Kutta methods (DIRK methods), i.e., methods with $a _ { i j } = 0$ for $i < j$ ,are

$$
R ( z ) = \frac { P ( z ) } { ( 1 - \gamma _ { 1 } z ) ( 1 - \gamma _ { 2 } z ) \ldots ( 1 - \gamma _ { s } z ) } ,
$$

where $\gamma _ { i } = a _ { i \ i } \ ( i = 1 , \dots , s )$ and degree $P \leq s$ . This follows at once from Formula (3.3) of Proposition 3.2, since the determinant of a triangular matrix is the product of its diagonal elements. Thus $R ( z )$ possesses real poles $1 / \gamma _ { 1 } , 1 / \gamma _ { 2 } , \ldots , 1 / \gamma _ { s } .$ Such approximations to $e ^ { z }$ will also appear in the next sections as stability func-tions of Rosenbrock methods and so-called singly-implicit Runge-Kutta methods. They thus merit a more thorough study. Research on these real-pole approximations was started by Ngrsett (1974) and Wolfbrandt (1977). Many results are collected in their joint paper Norsett & Wolfbrandt (1977).

If the method is of order at least $s$ ， $P ( z )$ is given by (3.18). We shall here, and in the sequel, very often write the formulas for $s = 3$ without always mentioning how trivial their extension to arbitrary $s$ is. Hence for $s = 3$

$$
R ( z ) = \frac { 1 + z \Big ( \displaystyle \frac { S _ { 0 } } { 1 ! } - \displaystyle \frac { S _ { 1 } } { 0 ! } \Big ) + z ^ { 2 } \Big ( \displaystyle \frac { S _ { 0 } } { 2 ! } - \displaystyle \frac { S _ { 1 } } { 1 ! } + \displaystyle \frac { S _ { 2 } } { 0 ! } \Big ) + z ^ { 3 } \Big ( \displaystyle \frac { S _ { 0 } } { 3 ! } - \displaystyle \frac { S _ { 1 } } { 2 ! } + \displaystyle \frac { S _ { 2 } } { 1 ! } - \displaystyle \frac { S _ { 3 } } { 0 ! } \Big ) } { 1 - z S _ { 1 } + z ^ { 2 } S _ { 2 } - z ^ { 3 } S _ { 3 } }
$$

where

$$
S _ { 0 } = 1 , \qquad S _ { 1 } = \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } , \qquad S _ { 2 } = \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } , \qquad S _ { 3 } = \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } .
$$

The error constant is for ${ p } = s$

$$
C = { \frac { S _ { 0 } } { 4 ! } } - { \frac { S _ { 1 } } { 3 ! } } + { \frac { S _ { 2 } } { 2 ! } } - { \frac { S _ { 3 } } { 1 ! } } .
$$

Theorem 4.18. Let $R ( z )$ be an approximation to $e ^ { z }$ of order $p$ with real poles only and let $k$ be the degree of its numerator. Then,

$$
p \leq k + 1 .
$$

Proof. If a sector of the order star $A$ ends up with a pole on the real axis, then by symmetry the complex conjugate sector must join the first one. All white sectors enclosed by these two must therefore be finite (Fig.4.6.). The same is true for sectors joining the infinite part of $A$ . There is thus on each side of the real axis at most one white sector which can be infinite. Thus the remaining $p - 1$ white sectors require together at least $p - 1$ zeros by Lemma 4.5, i.e., we have $p - 1 \leq k$

![](images/d435798c465addee2a3eaedcbc1b6ceb92f6983f32220a511f6bf08375d32eae.jpg)  
Fig.4.6. An approximation with real poles, 3 zeros, order 4

Remark 4.19. If $p { \ge } k$ , then at least one white sector must be unbounded. This is then either the first sector on the positive real axis, or, by symmetry, there is a pair of two sectors. By the proof of Theorem 4.18 the pair is unique and we shall call it Cary Grant's part.

![](images/17f7d7a12b47252512fe3123ad49db2af64f8062e9c55d1472c16e70edb30148.jpg)

Remark 4.20. If $p = k + 1$ , the optimal case, there are $k + 2$ white sectors, two of them are infinite. Hence each of the remaining $k$ sectors must then contain exactly one root of $P ( z )$ . As a consequence, $C < 0$ iff $P ( z )$ has no positive real root between the origin and the first pole.

# The Real-Pole Sandwich

We now analyze the approximations (4.19) with order $p \geq s$ in more detail (Ngrsett & Wanner 1979). We are interested in two sets:

Definition 4.21. Let $L$ be the set of $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ for which $\deg P ( z )$ in (4.20) is $\leq s - 1$ ,i.e., $R ( \infty ) = 0$ for $\gamma _ { i } \neq 0 ~ ( i = 1 , \ldots , s )$

Definition 4.22. Denote by $H$ the set of $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ for which the error constant (4.21) is zero, i.e., for which the approximation has highest possible order $p =$ $s + 1$ ，

A consequence of Theorem 4.18 is

$$
L \cap H = \emptyset .
$$

Written for the case $s = 3$ (generalizations to arbitrary $s$ are straightforward) and using (4.20) and (4.21) the sets $L$ and $H$ become

$$
\begin{array} { r } { L = \Big \{ ( \gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } ) ; \frac { 1 } { 3 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } } { 2 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } } { 1 ! } - \frac { \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } } { 0 ! } = 0 \Big \} } \\ { H = \Big \{ ( \gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } ) ; \frac { 1 } { 4 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } } { 3 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } } { 2 ! } - \frac { \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } } { 1 ! } = 0 \Big \} . } \end{array}
$$

Theorem 4.23 (Ngrsett & Wanner 1979). The surfaces $H$ and $I$ are each composed of $s$ disjoint connected sheets

$$
L = L _ { 1 } \cup L _ { 2 } \cup . . . \cup L _ { s } , \qquad H = H _ { 1 } \cup H _ { 2 } \cup . . . \cup H _ { s } .
$$

Ifa direction $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { s } )$ is chosen with all $\delta _ { \imath } \neq 0$ and if $k$ ofthem are positive, then the ray

$$
X = \left\{ ( \gamma _ { 1 } , \dots , \gamma _ { s } ) ; \quad \gamma _ { \imath } = t \delta _ { \imath } , 0 \leq t < \infty \right\}
$$

intersects the sheets $H _ { 1 } , L _ { 1 } , H _ { 2 } , L _ { 2 } , . . . , H _ { k } , L _ { k }$ in this order and no others.

![](images/56ad069f5acd9ed65bcae742761df25c8d91c1d1042b9d8ee40888de374a53b4.jpg)  
Fig.4.7. Formation of the sandwich

Proof. When the $\delta _ { \iota }$ have been chosen,inserting $\gamma _ { \imath } = t \delta _ { \imath }$ into (4.23) gives

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 3 ! } - t \frac { \delta _ { 1 } + \delta _ { 2 } + \delta _ { 3 } } { 2 ! } + t ^ { 2 } \frac { \delta _ { 1 } \delta _ { 2 } + \delta _ { 1 } \delta _ { 3 } + \delta _ { 2 } \delta _ { 3 } } { 1 ! } - t ^ { 3 } \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 0 ! } = 0 } \\ { \displaystyle \frac { 1 } { 4 ! } - t \frac { \delta _ { 1 } + \delta _ { 2 } + \delta _ { 3 } } { 3 ! } + t ^ { 2 } \frac { \delta _ { 1 } \delta _ { 2 } + \delta _ { 1 } \delta _ { 3 } + \delta _ { 2 } \delta _ { 3 } } { 2 ! } - t ^ { 3 } \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 1 ! } = 0 } \end{array}
$$

for $L$ and $H$ , respectively. These are third (in general $s$ th) degree polynomials whose positive roots we have to study. We vary the $\delta \mathbf { \dot { s } } _ { \mathrm { \scriptsize { : } } }$ ，and hence the ray $X$ ， starting with all $\delta \mathbf { \hat { s } }$ negative. The polynomials (4.26) then have all coeficients positive and obviously no positive real roots. When now one delta, say $\delta _ { 3 }$ , changes sign, the leading coefficients of (4.26) become zero and one root becomes infinite for each equation and satisfies asymptotically

![](images/32389165b20953684959f68edd5da660d2b3b1bcb106b701ba7d3c279945a907.jpg)  
Fig.4.8. The sandwich for $s = 3 \ldots$

![](images/7b1ad9665a126d38e562c0045379ff23f070bd34e0c6e881b4dbf9142b8c934f.jpg)  
and for $s = 5$

$$
\begin{array} { r l r } { \frac { \delta _ { 1 } \delta _ { 2 } } { 1 ! } - t \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 0 ! } \approx 0 } & { { } } & { \Longrightarrow } & { { } \quad t \approx \frac { 1 } { \delta _ { 3 } } } \\ { \frac { \delta _ { 1 } \delta _ { 2 } } { 2 ! } - t \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 1 ! } \approx 0 } & { { } } & { \Longrightarrow } & { { } \quad t \approx \frac { 1 } { 2 \delta _ { 3 } } } \end{array}
$$

for $L$ and $H$ , respectively. Thus $H$ comes below and $L$ comes above. Because of $L \cap H = \emptyset$ (4.22) these two roots can never cross and must therefore remain in this configuration (see Fig. 4.7).

When then successively $\delta _ { 2 }$ and $\delta _ { \mathbf { 1 } }$ change sign, the same scene repeats itself again and again, always two sheets of $H$ and $I$ descend from above in that order and are layed on the lower sheets like slices of bread and ham of a giant sandwich. Because $L \cap H = \emptyset$ , these sheets can never cross, two roots for $I$ or $H$ can never come together and become complex. So all roots must remain real and the theorem must be true.

A three-dimensional view of these surfaces is given in Fig.4.8.

The following theorem describes the form of the corresponding order star in all these sheets.

Theorem 4.24. Let $G _ { 1 } , \ldots , G _ { s }$ be the open connected components of $\mathbb { R } ^ { s } \backslash H$ such that $L _ { \imath }$ lies in $G _ { \imath }$ , and let $G _ { 0 }$ be the component containing the origin. Then the order star of $R ( z )$ given by (4.20) possesses exactly $k$ bounded fingers to the right of Cary Grant's part if and only if

$$
( \gamma _ { 1 } , \dots , \gamma _ { s } ) \in G _ { k } \cup H _ { k } .
$$

Proof. We prove this by a continuity argument letting the point $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ travel through the sandwich. Since Cary Grant's part is always present (Remark 4.19), the number of bounded sectors can change only where the error constant $C$ (4.21) changes sign,i.e., on the surfaces $H _ { 1 } , H _ { 2 } , \dots , H _ { s }$ . Fig. 4.9 gives some snap-shots from this voyage for $s = 3$ and $\gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma$ . In this case the equations (4.23) become

$$
\begin{array} { c } { { \displaystyle { \frac { 1 } { 3 ! } } - { \frac { 3 \gamma } { 2 ! } } + { \frac { 3 \gamma ^ { 2 } } { 1 ! } } - { \frac { \gamma ^ { 3 } } { 0 ! } } = 0 } } \\ { { \displaystyle { \frac { 1 } { 4 ! } } - { \frac { 3 \gamma } { 3 ! } } + { \frac { 3 \gamma ^ { 2 } } { 2 ! } } - { \frac { \gamma ^ { 3 } } { 1 ! } } = 0 } } \end{array}
$$

whose roots

$$
\begin{array} { r l r l r l } & { \lambda _ { 1 } = 0 . 1 5 8 9 8 4 , \quad } & { \lambda _ { 2 } = 0 . 4 3 5 8 6 7 , \quad } & { \lambda _ { 3 } = 2 . 4 0 5 1 5 } \\ & { \chi _ { 1 } = 0 . 1 2 8 8 8 6 , \quad } & { \chi _ { 2 } = 0 . 3 0 2 5 3 5 , \quad } & { \chi _ { 3 } = 1 . 0 6 8 5 8 } \end{array}
$$

do interlace nicely as required by Theorem 4.23. The afrmation of Theorem 4.24 for $s = 3$ can be clearly observed in Fig.4.9.

For the proof of the general statement we also put $\gamma _ { 1 } = . . . = \gamma _ { s } = \gamma$ and investigate the two extreme cases:

1. $\gamma = 0 \colon \mathrm { H e r e } \ R ( z )$ is the Taylor polynomial $1 + z + \dots + z ^ { s } / s !$ whose order star has no bounded sector at all.

2. $\gamma \to \infty$ : The numerator of $R ( z )$ in (4.20) becomes for $s = 3$

$$
P ( z ) = 1 + z \Big ( \frac { 1 } { 1 ! } - \frac { 3 \gamma } { 0 ! } \Big ) + z ^ { 2 } \Big ( \frac { 1 } { 2 ! } - \frac { 3 \gamma } { 1 ! } + \frac { 3 \gamma ^ { 2 } } { 0 ! } \Big ) + z ^ { 3 } \Big ( \frac { 1 } { 3 ! } - \frac { 3 \gamma } { 2 ! } + \frac { 3 \gamma ^ { 2 } } { 1 ! } - \frac { \gamma ^ { 3 } } { 0 ! } \Big ) .
$$

If we let $\gamma \to \infty$ , this becomes with $z \gamma = w$

$$
1 - w \Big ( 3 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) + w ^ { 2 } \Big ( 3 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) - w ^ { 3 } \Big ( 1 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) .
$$

Therefore all roots $w _ { i } \to 1$ ,hence $z _ { \imath }  1 / \gamma$ (see the last picture of Fig.4.9). Therefore no zero of $R ( z )$ can remain left of Cary Grant's part and we have $s$ bounded fingers.

Since between these extreme cases, there are at most $s$ crossings of the surface $H$ , Theorem 4.24 must be true. □

![](images/33de41f42dc6bea76acfd837a96054640f1391ae85c2f0073f26e41a586dc049.jpg)  
Fig. 4.9. Order stars for $\gamma$ travelling through the sandwich

Theorem 4.25. The function $R ( z )$ defined by (4.20) can be $I$ -stable only if

$$
( \gamma _ { 1 } , \dots , \gamma _ { s } ) \in H _ { q } \cup G _ { q } \cup H _ { q + 1 } \qquad i f \ s = 2 q - 1
$$

and

$$
\begin{array} { r } { ( \gamma _ { 1 } , \ldots , \gamma _ { s } ) \in G _ { q } \cup H _ { q + 1 } \cup G _ { q + 1 } \quad i f \ s = 2 q . } \end{array}
$$

Proof. The reason for this result is similar to Theorem 4.12. For $\boldsymbol { I }$ -stability the imaginary axis cannot intersect the order star and must therefore reach the origin through Cary Grant's part. Thus $I$ -stability (and hence $A$ -stability) is only possible (roughly) in the middle of the sandwich. Since at most $\{ ( p + 2 ) / 2 \}$ and at least $\{ ( p + 1 ) / 2 \}$ of the $p + 1$ sectors of $A$ start in $\mathbb { C } ^ { + }$ , the number $k$ of bounded fingers satisfies

$$
\left[ { \frac { p + 2 } { 2 } } \right] \geq k \qquad { \mathrm { a n d } } \qquad \left[ { \frac { p + 1 } { 2 } } \right] \leq k .
$$

Inserting $p = s + 1$ on $H$ and $p = s$ on $G$ we get the above results.

# Multiple Real-Pole Approximations

... the next main result is obtained, saying that the least value of $C$ is obtained when all the zeros of the denominator are equal (Ngrsett & Wolfbrandt 1977)

Approximations for whichall poles are equal,i.e.,for which $\gamma _ { 1 } = \gamma _ { 2 } = . ~ . ~ = \gamma _ { s } = \gamma$ are called “multiple" real-pole approximations (Ngrsett 1974). We again consider only approximations for which the order is $\geq s$ . These satisfy, for $s = 3$ ，

$$
R ( z ) = \frac { P ( z ) } { ( 1 - \gamma z ) ^ { 3 } }
$$

where $P ( z )$ is given by (4.3O),and their error constant is

$$
C = \frac { 1 } { 4 ! } - \frac { 3 \gamma } { 3 ! } + \frac { 3 \gamma ^ { 2 } } { 2 ! } - \frac { \gamma ^ { 3 } } { 1 ! } .
$$

Approximations with multiple poles have many computational advantages (the linear systems to be solved in Rosenbrock or DIRK methods have all the same matrix (see Sections IV.6 and IV.7)). We are now pleased to see that they also have the smallest error constants (Ngrsett & Wolfbrandt 1977).

Theorem 4.26. On each ofthe surfaces $L _ { \imath }$ and $H _ { \imath }$ $\mathcal { I } _ { \iota } \left( i = 1 , \dots , s \right)$ the error constant $C$ of(4.20) is minimized (in absolute value) when $\gamma _ { 1 } = \gamma _ { 2 } = . \cdot . = \gamma _ { s }$

Proof. Our proof uses relative order stars (similar to (4.13))

$$
B = \Big \{ z \in \mathbb { C } \ ; \ | q ( z ) | > 1 \Big \} , \qquad q ( z ) = \frac { R _ { n e w } ( z ) } { R _ { o l d } ( z ) } ,
$$

where $R _ { o l d } ( z )$ is a real-pole approximation of order $p = s + 1$ corresponding to $\gamma _ { 1 } , \ldots , \gamma _ { s }$ and $R _ { n e w } ( z )$ is obtained by an infinitely small change of the $\gamma \mathbf { \bar { s } }$ We assume that not all $\gamma _ { \imath }$ are identical and shall show that then the error constant can be decreased. After a permutation of the indices, we assume $\gamma _ { 1 } = \operatorname* { m a x } ( \gamma _ { \imath } )$ (by Theorem $4 . 2 3 \ \gamma _ { 1 } > 0$ ,so that $1 / \gamma _ { 1 }$ represents the pole on the positive real axis which is closest to the origin) and $\gamma _ { s } < \gamma _ { 1 }$ . We don't allow arbitrary changes of the $\gamma \mathbf { \bar { s } }$ but we decrease $\gamma _ { 1 }$ ,keep $\gamma _ { 2 } , \ldots , \gamma _ { s - 1 }$ fixed and determine $\gamma _ { s }$ by the defining equations for $H$ (see (4.23)). For example, for $s = 3$ we have

$$
\gamma _ { 3 } = \frac { \displaystyle \frac { 1 } { 4 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } } { 3 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } } { 2 ! } } { \displaystyle \frac { 1 } { 3 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } } { 2 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } } { 1 ! } } .
$$

Since the poles and zeros of $R _ { o l d } ( z )$ depend continuously on the $\gamma _ { \imath }$ ， poles and zeros of $q ( z )$ appear always in pairs (we call them dipoles). By the maximum principle or by Remark 4.14,each boundary curve of $B$ leaving the origin must lead to at least one dipole before it rejoins the origin. Since there are $s + 2 = p + 1$ dipoles of $q ( z )$ (identical poles for $R _ { o l d } ( z )$ and $R _ { n e w } ( z )$ don't give rise to a dipole of $q ( z ) )$ and $p + 1$ pairs of boundary curves of $B$ leaving the origin (Remark 4.14), each such boundary curve passes through exactly one dipole before rejoining the origin. As a consequence no boundary curve of $B$ can cross the real axis except at dipoles.

If the error constant of $R _ { o l d } ( z )$ satisfies $C _ { o l d } < 0$ ，then,by Remark 4.20, $R _ { o l d } ( z )$ has no zero between $1 / \gamma _ { 1 }$ and the origin. Therefore also $q ( z )$ possesses no dipole in this region. Since the pole of $R _ { n e w } ( z )$ is slightly larger than $1 / \gamma _ { 1 }$ (that of $R _ { o l d } ( z ) )$ , the real axis between $1 / \gamma _ { 1 }$ and the origin must belong to the complement of $B$ . Thus we have $C _ { n e w } - C _ { o l d } > 0$ by (4.14) and (4.15).

If $C _ { o l d } > 0$ there is one additional dipole of $q ( z )$ between $1 / \gamma _ { 1 }$ and the origin (see Remark 4.2O). As above weconclude this time that $C _ { n e w } - C _ { o l d } < 0$

In both cases $| C _ { n e w } | < | C _ { o l d } |$ , since by continuity $C _ { n e w }$ is near to $C _ { o l d }$ As a consequence no $( \gamma _ { 1 } , \dotsc , \gamma _ { s } ) \in H$ with at least two different $\gamma _ { \imath }$ can minimize the error constant. As it becomes large in modulus when at least one $\gamma _ { \imath }$ tends to $\infty$ (this follows from Theorem 4.18 and from the fact that in this case $R ( z )$ tends to an approximation with $s$ replaced by $s - 1 )$ the minimal value of $C$ must be attained when all poles are identical.

The proof for $L$ is the same, there are only $s - 1$ zeros of $R ( z )$ and the order is $p = s$ □

An illustration of the order star $B$ compared to $A$ is given in Fig.4.10. Another advantage of multiple real-pole approximations is exhibited by the following theorem:

Theorem 4.27 (Keeling 1989). On each surface $H _ { \imath } \cap \{ ( \gamma _ { 1 } , \ldots , \gamma _ { s } ) ; \gamma _ { \jmath } > 0 \}$ the value $\mid R ( \infty ) \mid$ of (4.20) is minimized when $\gamma _ { 1 } = \gamma _ { 2 } = . ~ . . = \gamma _ { s }$

![](images/0ef5519a7c6a93a73057d011a8c3cbed782710be02efba660c928040fb004c9a.jpg)  
Fig. 4.10. Order star $A$ compared to $B$

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>left pictures: Cold &lt; 0</td><td rowspan=1 colspan=1>right pictures: Cold &gt; 0</td></tr><tr><td rowspan=1 colspan=1>Rold</td><td rowspan=1 colspan=1>Y1 =1.272 = 1.1Y3 = 0.9455446</td><td rowspan=1 colspan=1>Y1 = 0.3572 =0.33Y3 =0.2406340</td></tr><tr><td rowspan=1 colspan=1>Rnew</td><td rowspan=1 colspan=1>Y1 = 1.1772 = 1.1Y3 =0.9628661</td><td rowspan=1 colspan=1>Y1 = 0.34572 = 0.33Y3 = 0.2440772</td></tr></table>

Proof. The beginning of the proof is identical to that of Theorem 4.26. Besides $1 / \gamma _ { 1 }$ and $1 / \gamma _ { s }$ there is at best an even number of dipoles on the positive real axis to the right of $1 / \gamma _ { 1 }$ . As in the proof above we conclude that a right-neighbourhood of $1 / \gamma _ { 1 }$ belongs to $B$ so that $\infty$ must lie in its complement (cf. Fig.4.10). This implies

$$
\mid R _ { n e w } ( \infty ) \mid < \mid R _ { o l d } ( \infty ) \mid
$$

As a consequence no element of $H \cap \{ ( \gamma _ { 1 } , \cdot \cdot \cdot , \gamma _ { s } ) ; \ \gamma _ { j } > 0 \}$ with at least two $\gamma _ { j }$ different can minimize $\mid R ( \infty ) \mid$ .Also $| R ( \infty ) \ |$ increases if $\gamma _ { 1 }  \infty$ . The statement now follows from the fact that $| R ( \infty ) \mid$ tends to infinity when at least one $\gamma _ { j }$ approaches zero. □

# Exercises

1. (Ehle 1968)． Compute the polynomial $E ( y )$ for the third and fourth Padé subdiagonal $R _ { k , k + 3 } ( z )$ and $R _ { k , k + 4 } ( z )$ (which, by Proposition 3.4 consists of two terms only). Show that these approximations violate (3.6) and cannot be $A$ -stable.

2.Prove the general formula

$$
E ( y ) = \Big ( \frac { k ! } { ( k + j ) ! } \Big ) ^ { 2 } \sum _ { r = \big [ ( k + j + 2 ) / 2 \big ] } ^ { j } \frac { ( - 1 ) ^ { j - r } } { ( j - r ) ! } \Bigg ( \prod _ { q = 1 } ^ { j - r } ( j - q + 1 ) ( k + q ) ( r - k - q ) \Bigg ) y ^ { 2 r }
$$

for the Padé approximations $R _ { k j } \ ( j \geq k )$

3. (For the fans of mathematical precision). Derive the following formulas for the roots $\lambda _ { i }$ and $\chi _ { \imath }$ of(4.28)

$$
\begin{array} { l l l } { { \chi _ { 1 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { 1 3 \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 1 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta + 2 \pi } { 3 } \Big ) , } } \\ { { \chi _ { 2 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { 2 5 \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 2 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta + 4 \pi } { 3 } \Big ) , } } \\ { { \chi _ { 3 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 3 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta } { 3 } \Big ) , } } \end{array}
$$

where $\theta = \arctan ( \sqrt { 2 } / 4 )$

Hint. Use the Cardano-Viete formula (e.g., Hairer & Wanner (1995), page 66).

4．Prove that all zeros of

$$
\frac { x ^ { s } } { s ! } - S _ { 1 } \frac { x ^ { s - 1 } } { ( s - 1 ) ! } + S _ { 2 } \frac { x ^ { s - 2 } } { ( s - 2 ) ! } - \ldots \pm S _ { s }
$$

are real and distinct whenever all zeros of

$$
Q ( z ) = 1 - z S _ { 1 } + z ^ { 2 } S _ { 2 } - \ldots \pm z ^ { s } S _ { s } , \qquad S _ { s } \neq 0
$$

are real. Also,both polynomials have the same number of positive (and negative) zeros (Ngrset & Wanner 1979,Bales,Karakashian & Serbin 1988).

Hint. Apply Theorem 4.23. This furnishes a geometric proof of a classical result (see e.g., Pólya & Szegoö (1925), Volume II, Part V, No.65) and allows us to interpret $R ( z )$ as the stability function of a (real) collocation method.

5. Prove that $( \gamma , \dots , \gamma ) \in L$ (Definition 4.21) if and only if $L _ { s } ( 1 / \gamma ) = 0$ ,where $L _ { s } ( x )$ denotes the Laguerre polynomial of degree $s$ (see Abramowitz & Stegun (1964),Formula 22.3.9 or Formula (6.11) below).

# IV.5 Construction of Implicit Runge-Kutta Methods

Although most of these methods appear at the moment to be largely of theoretical interest ... (B.L. Ehle 1968)

In Sect. II.7 the first implicit Runge-Kutta methods were introduced. As we saw in Sect.IV.3, not all of them are suitable for the solution of stiff differential equations. This section is devoted to the collection of several classes of fully implicit Runge-Kutta methods possessing good stability properties.

The construction of such methods relies heavily on the simplifying assumptions

$$
\begin{array} { l l l l } { { } } & { { \displaystyle B ( p ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } = \frac { 1 } { q } } } & { { q = 1 , \ldots , p ; } } \\ { { } } & { { } } & { { } } \\ { { C ( \eta ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { q - 1 } = \frac { c _ { i } ^ { q } } { q } } } & { { i = 1 , \ldots , s , \quad q = 1 , \ldots , \eta ; } } \\ { { } } & { { } } & { { } } \\ { { D ( \zeta ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } a _ { i j } = \frac { b _ { \eta } } { q } ( 1 - c _ { j } ^ { q } ) } } & { { j = 1 , \ldots , s , \quad q = 1 , \ldots , \zeta . } } \end{array}
$$

Condition $B ( p )$ simply means that the quadrature formula $( b _ { \imath } , c _ { i } )$ is of order $p$ The importance of the other two conditions is seen from the following fundamental theorem, which was derived in Sect. II.7.

Theorem 5.1(Butcher 1964). If the coefficients $b _ { i } , c _ { i } , a _ { i j }$ of a Runge-Kutta method satisfy $B ( p ) , C ( \eta ) , D ( \zeta )$ with $p \leq \eta + \zeta + 1$ and $p \leq 2 \eta + 2$ , then the method is of order $p$ □

# Gauss Methods

These processes, named “Kuntzmann-Butcher methods” in Sect.II.7, are colloca-tion methods based on the Gaussian quadrature formulas, i.e., $c _ { 1 } , \ldots , c _ { s }$ are the zeros of the shifted Legendre polynomial of degree $s$ ，

$$
{ \frac { d ^ { s } } { d x ^ { s } } } \left( x ^ { s } ( x - 1 ) ^ { s } \right) .
$$

For the sake of completeness we present the first of these in Tables 5.1 and 5.2.

Table 5.1. Gauss methods of order 2 and 4   
Table 5.2. Gauss method of order 6   

<table><tr><td></td><td>-65-6 1</td><td>4</td><td>V3 4 6</td></tr><tr><td>1</td><td>1-2 1-2 +</td><td>4 V3 +</td><td>4</td></tr><tr><td></td><td></td><td>6 1</td><td>1</td></tr></table>

<table><tr><td>1 √15 10 1 1 √15 + 10</td><td>5 36 3 V15 + 24 5 √15 + 30</td><td>2-9 √15 15 2 2-9 √15 + 15</td><td>5 √15 36 30 5 √15 36 24 5</td></tr><tr><td></td><td>5 18</td><td>4-9</td><td>36 5 18</td></tr></table>

Theorem 5.2 (Butcher 1964, Ehle 1968). The s -stage Gauss method is of order $2 s$ . Its stability function is the $\left( s , s \right)$ -Padé approximation and the method is Astable.

Proof. The order result has already been proved in Sect.II.7. Since the degrees of the numerator and the denominator are not larger than $s$ for any $s$ -stage Runge-Kutta method, the stability function of this $2 s$ -order method is the $\left( \mathscr { s } , \mathscr { s } \right)$ -Padé approximation by Theorem 3.11. $A$ -stability thus follows from Theorem 4.12.□

# Radau IA and Radau IIA Methods

Butcher (1964) introduced Runge-Kutta methods based on the Radau and Lobatto quadrature formulas. He called them processes of type I, II or III according to whether $c _ { 1 } , \ldots , c _ { s }$ are the zeros of

$$
\begin{array} { r l } & { \mathrm { I : } \quad \frac { d ^ { s - 1 } } { d x ^ { s - 1 } } \bigg ( x ^ { s } ( x - 1 ) ^ { s - 1 } \bigg ) , \quad \quad \mathrm { ( R a d a u l e f t ) } } \\ & { \mathrm { I I : } \quad \frac { d ^ { s - 1 } } { d x ^ { s - 1 } } \bigg ( x ^ { s - 1 } ( x - 1 ) ^ { s } \bigg ) , \quad \quad \mathrm { ( R a d a u r i g h t ) } } \\ & { \mathrm { I I I : } \quad \frac { d ^ { s - 2 } } { d x ^ { s - 2 } } \bigg ( x ^ { s - 1 } ( x - 1 ) ^ { s - 1 } \bigg ) . \quad \mathrm { ( L o b a t t o ) } } \end{array}
$$

The weights $b _ { 1 } , \dots , b _ { s }$ are chosen such that the quadrature formula satisfies $B ( s )$ ， which implies $B ( 2 s - 1 )$ in the Radau case and $B ( 2 s - 2 )$ in the Lobatto case (see Lemma 5.15 below). Unfortunately, none of these methods of Butcher turned out to be $A$ -stable (see e.g. Table 3.1). Ehle (1969) took up the ideas of Butcher and constructed methods of type I, II and II with excellent stability properties. Independently, Axelsson (1969) found the Radau IIA methods together with an elegant proof of their $A$ -stability.

The $s$ -stage Radau IA method is of type I, where the coefficients $a _ { i j }$ ， $( i , j =$ $1 , \ldots , s )$ are defined by condition $D ( s )$ . This is uniquely possible since the $c _ { \iota }$ are distinct and the $b _ { \imath }$ not zero. Tables 5.3 and 5.4 present the first of these methods.

![](images/504807479b58471ad51af4181dc72bb8ecba0deacf6c466585059758ae2b410c.jpg)

Table 5.3. Radau IA methods of orders 1 and 3   
Table 5.4. Radau IA method of order 5   

<table><tr><td rowspan="6">0 6-√6 10 6+√6</td><td rowspan="5">1 9 1 1</td><td>-1-√6</td><td>-1+√6</td></tr><tr><td>18</td><td>18</td></tr><tr><td>88+7√6</td><td>88-43√6</td></tr><tr><td>360</td><td>360</td></tr><tr><td>88+43√6</td><td>88-7√6</td></tr><tr><td>10</td><td>9 360</td><td>360</td></tr><tr><td rowspan="2"></td><td>1</td><td>16+√6</td><td>16-√6</td></tr><tr><td>9</td><td>36</td><td>36</td></tr></table>

Ehle's type II processes are obtained by imposing condition $C ( s )$ . By Theorem II.7.7 this results in the collocation methods based on the zeros of (5.2). They are called Radau IIA methods. Examples are given in Tables 5.5 and 5.6. For $s = 1$ we obtain the implicit Euler method.

Theorem 5.3. The s -stage Radau IA method and the $s$ -stage Radau IIA method are of order $2 s - 1$ . Their stability function is the $( s - 1 , s )$ subdiagonal Padé approximation. Both methods are $A$ -stable.

Proof. The stated orders follow from Theorem 5.1 and Lemma 5.4 below. Since $c _ { 1 } = 0$ for the Radau IA method, $D ( s )$ with $j = 1$ and $B ( 2 s - 1 )$ imply (3.14). Similarly, for the Radau IA method, $c _ { s } = 1$ and $C ( s )$ imply (3.13).Therefore,in both cases, the numerator of the stability function is of degree $\leq s - 1$ by Proposition 3.8. The statement now follows from Theorem 3.11 and Theorem 4.12. □

Table 5.5. Radau IIA methods of orders 1 and 3   

<table><tr><td>1-3 1</td><td>52 1 12 4 1 4</td></tr><tr><td></td><td>4 4</td></tr></table>

![](images/af81b6851ceabdf5e1d35411a3d109df0418fbb258a09dc917aea82ec0e5bfa4.jpg)

Table 5.6. Radau IIA method of order 5   

<table><tr><td>4-√6</td><td>88-76</td><td>296-169√6</td><td>-2+3√6</td></tr><tr><td>10</td><td>360</td><td>1800</td><td>225</td></tr><tr><td>4+√6</td><td>296+169√6</td><td>88+7√6</td><td>-2-3√6</td></tr><tr><td>10</td><td>1800</td><td>360</td><td>225</td></tr><tr><td>1</td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td>9</td></tr><tr><td></td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td>9</td></tr></table>

Lemma 5.4. Let an $s$ -stage Runge-Kutta method have distinct $c _ { 1 } , \ldots , c _ { s }$ and nonzero weights $b _ { 1 } , \dots , b _ { s }$ . Then we have

$a$ ） $C ( s )$ and $B ( s + \nu )$ imply $D ( \nu )$ ; b) $D ( s )$ and $B ( s + \nu )$ imply $C ( \nu )$ ·

Proof. Put

$$
d _ { \jmath } ^ { ( q ) } : = \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } a _ { \imath \jmath } - \frac { b _ { \jmath } } { q } ( 1 - c _ { \jmath } ^ { q } ) .
$$

Conditions $C ( s )$ and $B ( s + \nu )$ imply

$$
\sum _ { \jmath = 1 } ^ { s } d _ { \jmath } ^ { ( q ) } c _ { \jmath } ^ { k - 1 } = 0 \qquad \mathrm { f o r } \quad k = 1 , \dots , s \mathrm { a n d } q = 1 , \dots , \nu .
$$

The vector $( d _ { 1 } ^ { ( q ) } , \dots , d _ { s } ^ { ( q ) } )$ must vanish, because it is the solution of a homoge-neous linear system with a non singular matrix of Vandermonde type. This proves $D ( \nu )$

For part (b) one defines

$$
e _ { \ i } ^ { ( \boldsymbol { q } ) } : = \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } c _ { \jmath } ^ { \boldsymbol { q } - 1 } - \frac { c _ { \imath } ^ { \boldsymbol { q } } } { \boldsymbol { q } }
$$

and applies a similar argument to

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } c _ { \ i } ^ { k - 1 } e _ { \ i } ^ { ( q ) } = 0 , \qquad k = 1 , \dots , s , \quad q = 1 , \dots , \nu .
$$

# Lobatto IIIA, IIIB and IIC Methods

For all type III processes the $c _ { \iota }$ are the zeros of the polynomial (5.3） and the weights $b _ { \imath }$ are such that $B ( 2 s - 2 )$ is satisfied.

The coefficients $a _ { \scriptscriptstyle { \imath \jmath } }$ are defined by $C ( s )$ for the Lobatto IIA methods. It is therefore a collocation method. For the Lobato IIIB methods we impose $D ( s )$ and, finally, for the Lobatto IIIC methods we put

$$
a _ { \imath 1 } = b _ { 1 } \quad \mathrm { f o r } \quad i = 1 , \ldots , s
$$

and determine the remaining $a _ { \imath \jmath }$ by $C ( s - 1 )$ . Ehle (1969) introduced the first two classes,and presented the IIIC methods for $s \leq 3$ . The general definition of the IIIC methods is due to Chipman (1971); see also Axelsson (1972). Examples are given in Tables 5.7-5.12.

Table 5.7. Lobatto IIA methods of orders 2 and 4   

<table><tr><td></td><td>0</td><td rowspan="8">0 0 54</td><td>0</td></tr><tr><td>0 0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>24</td></tr><tr><td>1 1</td><td>1 1</td><td>GA 1 6</td></tr><tr><td>1-2 1 2</td><td></td><td>1 2 1 6 6</td></tr></table>

Table 5.8.Lobatto IIIA method of order 6   

<table><tr><td>0 5-√5</td><td>0 11+√5</td><td>0 25-√5</td><td>0 25-13√5</td><td>0 -1+√5</td></tr><tr><td>10</td><td>120 11-√5</td><td>120</td><td>120</td><td>120</td></tr><tr><td>5+√5 10</td><td>120</td><td>25+13√5 120</td><td>25+√5</td><td>-1-√5</td></tr><tr><td></td><td>1</td><td>5</td><td>120</td><td>120</td></tr><tr><td>1</td><td>12</td><td>12</td><td>5 12</td><td>1 12</td></tr><tr><td></td><td></td><td>5</td><td>5</td><td></td></tr><tr><td></td><td>12</td><td>12</td><td>12</td><td>1 12</td></tr></table>

Theorem 5.5. The s -stage Lobatto IIIA, IIIB and IIIC methods are of order $2 s - 2$ The stability function for the Lobatto IlIA and IIIB methods is the diagonal $( s -$ $1 , s - 1 )$ -Padé approximation. For the Lobatto IIIC method it is the $\left( s - 2 , s \right)$ -Pade approximation. All these methods are A-stable.

Proof. We first prove that the IIIC methods satisfy $D ( s - 1 )$ Condition (5.5) implies $d _ { 1 } ^ { ( q ) } = 0 ~ ( q = 1 , \dots , s - 1 )$ for $d _ { 1 } ^ { ( q ) }$ given by (5.4). Conditions $C ( s - 1 )$

Table 5.9. Lobatto IIIB methods of orders 2 and 4   

<table><tr><td colspan="3"></td><td>0</td><td></td><td>1-6 0</td></tr><tr><td>0</td><td>0</td><td></td><td>1</td><td>GR</td><td>0</td></tr><tr><td>1</td><td>1-21-2 0</td><td></td><td>1</td><td></td><td>0</td></tr><tr><td></td><td>1 1</td><td></td><td></td><td>1 2-3</td><td>1</td></tr></table>

Table 5.10.Lobatto IIIB method of order 6   

<table><tr><td>0</td><td>1 12</td><td>-1-√5 24</td><td>-1+√5 24</td><td>0</td></tr><tr><td>5-√5 10</td><td>1 12</td><td>25+√5 120</td><td>25-13√5 120</td><td>0</td></tr><tr><td>5+√5 10</td><td>1 12</td><td>25 +13√5 120</td><td>25-√5 120</td><td>0</td></tr><tr><td></td><td>1</td><td>11-√5</td><td>11+√5</td><td>0</td></tr><tr><td>1</td><td>12</td><td>24</td><td>24</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td>5</td><td>5</td><td>1</td></tr><tr><td>12</td><td>12</td><td>12</td><td>12</td></tr></table>

Table 5.11. Lobatto IIC methods of orders 2 and 4   

<table><tr><td></td><td></td><td>0</td><td>1</td><td>1-3</td><td>1-6</td></tr><tr><td rowspan="2">0</td><td>1</td><td>1</td><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>12</td></tr><tr><td>1</td><td>N 1-2</td><td>1</td><td>G</td><td>1</td><td>1 6</td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 1</td><td></td><td>1-6</td><td>2-3</td><td>1</td></tr></table>

Table 5.12. Lobatto IIIC method of order 6   

<table><tr><td>0 5-√5</td><td>1 12 1</td><td>-√5 12 1</td><td>V5 12 10-7√5</td><td>1 √5</td></tr><tr><td>10</td><td>12</td><td>4</td><td>60</td><td>60</td></tr><tr><td>5+√5 10</td><td>1</td><td>10+7√5</td><td>1 4</td><td>-√5</td></tr><tr><td></td><td>12</td><td>60 5</td><td>5</td><td>60 1</td></tr><tr><td>1</td><td>1 12</td><td>12</td><td>12</td><td>12</td></tr><tr><td></td><td></td><td>5</td><td>5</td><td>1</td></tr><tr><td></td><td>1 12</td><td>12</td><td>12</td><td>12</td></tr></table>

and $B ( 2 s - 2 )$ then yield

$$
\sum _ { \ i = 2 } ^ { s } d _ { \ j } ^ { ( q ) } c _ { \ j } ^ { k - 1 } = 0 \qquad \mathrm { f o r } \quad k = 1 , \dots , s - 1 \mathrm { a n d } q = 1 , \dots , s - 1 .
$$

As in the proof of Lemma 5.4 we deduce $D ( s - 1 )$ ．All order statements now follow from Lemma 5.4 and Theorem 5.1.

By definition, the first row of the Runge-Kutta matrix $A$ vanishes for the IIIA methods,and its last column vanishes for the IIB methods. The denominator of the stability function is therefore of degree $\le s - 1$ . Similarly, the last row of $A - \mathbb { 1 } b ^ { T }$ vanishes for IIIA,and the first column of $A - \mathbb { 1 } b ^ { T }$ for IIIB.Therefore, the numerator of the stability function is also of degree $\leq s - 1$ by Formula (3.3). It now follows from Theorem 3.11 that both methods have the $( s - 1 , s - 1 )$ -Padé approximation as stability function.

For the IIC process the first column as well as the last row of $A - \mathbb { 1 } b ^ { T }$ van-ish. Thus the degree of the numerator of the stability function is at most $s - 2$ by Formula (3.3). Again,Theorem 3.11 and Theorem 4.12 imply the statement.□

For a summary of these statements see Table 5.13.

Table 5.13. Fully implicit Runge-Kutta methods   

<table><tr><td>method</td><td>simplifying assumptions</td><td>order</td><td>stability function</td></tr><tr><td>Gauss Radau IA Radau IIA Lobatto IIIA Lobatto IIIB Lobatto IIIC</td><td>B(2s) C(s) D(s) B(2s-1) C(s-1) D(s） B(2s-1) C(s) D(s-1) B(2s-2) C(s) D(s-2) B(2s-2) C(s-2) D(s) B(2s-2) C(s-1) D(s-1)</td><td>2s 2s-1 2s-1 2s-2 2s-2 2s-2</td><td>(s,s)-Padé (s-1,s)-Padé (s-1,s)-Padé (s-1,s-1)-Padé (s-1,s-1)-Padé (s-2,s)-Padé</td></tr></table>

# The W -Transformation

We now attack the explicit construction of all Runge-Kutta methods covered by Theorem 5.1. The first observation is (Chipman 1971, Burrage 1978) that $C ( \eta )$ can be written as

$$
\left( \begin{array} { l l l l l } { a _ { 1 1 } } & { \dots } & { a _ { 1 s } } \\ { \vdots } & & { \vdots } \\ { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { \dots } & { a _ { s s } } \end{array} \right) \left( \begin{array} { l l l l l } { 1 } & { c _ { 1 } } & { \dots } & { c _ { 1 } ^ { \eta - 1 } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta - 1 } } \end{array} \right) = \left( \begin{array} { l l l l l } { 1 } & { c _ { 1 } } & { \dots } & { c _ { 1 } ^ { \eta } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta } } \end{array} \right) \left( \begin{array} { l l l l l } { 0 } & { 0 } & { \dots } & { 0 } \\ { 1 } & { 0 } & { \dots } & { 0 } \\ { 0 } & { \frac { 1 } { 2 } } & { \dots } & { 0 } \\ { \vdots } & { \vdots } & & { \ddots } & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta } } \end{array} \right) .
$$

Hence, if $V$ is the Vandermonde matrix

$$
V = \left( \begin{array} { c c c c } { { 1 } } & { { c _ { 1 } } } & { { \dots } } & { { c _ { 1 } ^ { s - 1 } } } \\ { { } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 1 } } & { { c _ { s } } } & { { \dots } } & { { c _ { s } ^ { s - 1 } } } \end{array} \right) ,
$$

then the first $\eta$ (for $\eta \leq s - 1$ ) columns of $V ^ { - 1 } A V$ must have the special structure (with many zeros) of the rightmost matrix in (5.6). This $^ { 6 6 } V$ -transformation" already considerably simplifies the discussion of order and stability of methods governed by $C ( \eta )$ with $\eta$ close to $s$ (Burrage 1978). Thus, collocation methods $( \eta = s )$ are characterized by

$$
V ^ { - 1 } A V = \left( \begin{array} { c c c c c } { { 0 } } & { { } } & { { } } & { { } } & { { - \varrho _ { 0 } / s } } \\ { { 1 } } & { { 0 } } & { { } } & { { } } & { { - \varrho _ { 1 } / s } } \\ { { } } & { { 1 / 2 } } & { { 0 } } & { { } } & { { - \varrho _ { 2 } / s } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ddots } } & { { 0 } } & { { - \varrho _ { s - 2 } / s } } \\ { { } } & { { } } & { { } } & { { 1 / ( s - 1 ) } } & { { - \varrho _ { s - 1 } / s } } \end{array} \right)
$$

where the $\varrho$ 's are the coeficients of $\begin{array} { r } { M ( t ) = \prod _ { \ i = 1 } ^ { s } ( t - c _ { \ i } ) } \end{array}$ and appear when the $c _ { \iota } ^ { s }$ in (5.6) are replaced by lower powers. Whenever some of the columns of $V ^ { - 1 } A V$ are not as in (5.7), a nice idea of Ngrsett allows one to interpret the method as a perturbed collocation method (see Ngrsett & Wanner (1981) for more details).

However, the $V$ -transformation has some drawbacks: it does not allow a similar characterization of $D ( \zeta )$ ，and the discussions of $A -$ and $B$ -stability remain fairly complicated (see e.g. the above cited papers). It was then discovered (Hairer & Wanner 1981, 1982) that nicer results are obtained,if the Vandermonde matrix $V$ is replaced by a matrix $W$ whose elements are orthogonal polynomials evaluated at $c _ { \imath }$ . We therefore use the (non standard) notation

$$
P _ { k } ( x ) = { \frac { { \sqrt { 2 k + 1 } } } { k ! } } { \frac { d ^ { k } } { d x ^ { k } } } { \Big ( } x ^ { k } ( x - 1 ) ^ { k } { \Big ) } = { \sqrt { 2 k + 1 } } \sum _ { \jmath = 0 } ^ { k } ( - 1 ) ^ { \jmath + k } { \binom { k } { \jmath } } { \binom { j + k } { j } } x ^ { \jmath }
$$

for the shifted Legendre polynomials normalized so that

$$
\int _ { 0 } ^ { 1 } P _ { k } ^ { 2 } ( x ) d x = 1 .
$$

These polynomials satisfy the integration formulas

$$
\begin{array} { l l } { \displaystyle \int _ { 0 } ^ { x } P _ { 0 } ( t ) d t = \xi _ { 1 } P _ { 1 } ( x ) + \frac { 1 } { 2 } P _ { 0 } ( x ) } \\ { \displaystyle \int _ { 0 } ^ { x } P _ { k } ( t ) d t = \xi _ { k + 1 } P _ { k + 1 } ( x ) - \xi _ { k } P _ { k - 1 } ( x ) } & { \ k = 1 , 2 , . . . } \end{array}
$$

with

$$
\xi _ { k } = { \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } }
$$

(Exercise 1). Instead of (5.7) we now have the following result.

Theorem 5.6. Let W be defined by

$$
w _ { \iota \jmath } = P _ { \jmath - 1 } ( c _ { \imath } ) , \qquad i = 1 , \ldots , s , \quad \jmath = 1 , \ldots , s ,
$$

and let $A$ be the coefficient matrix for the Gauss method of order $2 s$ . Then,

$$
W ^ { - 1 } A W = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { - \xi _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \xi _ { 2 } } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 0 } } & { { - \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { 0 } } \end{array} \right) = : X _ { G } .
$$

Proof. We first write $C ( \eta )$ in the form

$$
\sum _ { \ i = 1 } ^ { s } a _ { \ i \ i } p ( c _ { \ i } ) = \int _ { 0 } ^ { c _ { \ i } } p ( x ) d x \qquad { \mathrm { i f } } \quad \deg ( p ) \leq \eta - 1 ,
$$

which,by (5.10),is equivalent to

$$
\begin{array} { l } { \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } P _ { 0 } ( c _ { \jmath } ) = \xi _ { 1 } P _ { 1 } ( c _ { \imath } ) + \frac { 1 } { 2 } P _ { 0 } ( c _ { \imath } ) } \\ { \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } P _ { k } ( c _ { \jmath } ) = \xi _ { k + 1 } P _ { k + 1 } ( c _ { \imath } ) - \xi _ { k } P _ { k - 1 } ( c _ { \imath } ) \qquad k = 1 , \dots , \eta - 1 . } \end{array}
$$

For $\eta = s$ , inserting (5.12), and using matrix notation, this becomes

$$
\begin{array} { r l r } { \left( \begin{array} { c c c } { a _ { 1 1 } } & { \ldots } & { a _ { 1 s } } \\ { \vdots } & { \vdots } \\ { \vdots } & { \vdots } \\ { a _ { s 1 } } & { \ldots } & { a _ { s s } } \end{array} \right) \left( \begin{array} { c c c } { w _ { 1 1 } } & { \ldots } & { w _ { 1 s } } \\ { \vdots } & { \vdots } \\ { \vdots } & { \vdots } \\ { w _ { s 1 } } & { \ldots } & { w _ { s s } } \end{array} \right) = } & { { } } \\ { \left( \begin{array} { c c c } { w _ { 1 1 } } & { \ldots } & { w _ { 1 s } } & { P _ { s } ( c _ { 1 } ) } \\ { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } \\ { w _ { s 1 } } & { \ldots } & { w _ { s s } } & { P _ { s } ( c _ { s } ) } \end{array} \right) \left( \begin{array} { c c c } { 1 / 2 } & { - \xi _ { 1 } } & { \ldots } & { } \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } \\ { \vdots } & { \xi _ { 2 } } & { \ddots } & { \vdots } \\ { \xi _ { s 1 } } & { \ddots } & { \xi _ { s - 1 } } & { 0 } \\ { w _ { s 1 } } & { \ldots } & { \xi _ { s } } \end{array} \right) . } \end{array}
$$

Since for the Gauss processes we have $P _ { s } ( c _ { 1 } ) = \ldots = P _ { s } ( c _ { s } ) = 0$ , the last column respectively row of the right hand matrices can be dropped and we obtain (5.13).

In what follows we shall study similar results for other implicit Runge-Kutta methods. We first formulate the following lemma, which is an immediate consequence of (5.15) and (5.16).

Lemma 5.7. Let A be the coefficient matrix of an implicit Runge-Kutta method and let W be a nonsingular matrix with

$$
w _ { \iota _ { 2 } } = P _ { \jmath - 1 } ( c _ { \iota } ) \qquad f o r \quad i = 1 , \ldots , s , \quad j = 1 , \ldots , \eta + 1 .
$$

Then $C ( \eta )$ (with $\eta \leq s - 1 )$ is equivalent to the fact that the first $\eta$ columns of $W ^ { - 1 } A W$ are equal to those of $X _ { G }$ in (5.13). □

The second type of simplifying assumption, $D ( \zeta )$ , is now written in the form

$$
\sum _ { \ i = 1 } ^ { s } b _ { i } p ( c _ { \ i } ) a _ { i \ i } = b _ { j } \int _ { c _ { \ j } } ^ { 1 } p ( x ) d x \qquad { \mathrm { i f } } \quad \deg ( p ) \leq \zeta - 1 .
$$

The integration formulas (5.10) together with orthogonality relations

$$
\int _ { 0 } ^ { 1 } P _ { 0 } ( x ) d x = 1 , \quad \int _ { 0 } ^ { 1 } P _ { k } ( x ) d x = \int _ { 0 } ^ { 1 } P _ { 0 } ( x ) P _ { k } ( x ) d x = 0 \quad { \mathrm { f o r } } \quad k = 1 , 2 , \dots .
$$

show that $D ( \zeta )$ (i.e.,(5.17)) is equivalent to

$$
\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { s } P _ { 0 } ( c _ { _ 2 } ) b _ { \imath } a _ { \imath j } = \Big ( \frac { 1 } { 2 } P _ { 0 } ( c _ { j } ) - \xi _ { 1 } P _ { 1 } ( c _ { _ 2 } ) \Big ) b _ { j } } } \\ & { \overset { s } { \underset { i = 1 } { \sum } } P _ { k } ( c _ { _ 1 } ) b _ { \imath } a _ { \imath j } = \Big ( \xi _ { k } P _ { k - 1 } ( c _ { _ 2 } ) - \xi _ { k + 1 } P _ { k + 1 } ( c _ { j } ) \Big ) b _ { j } } & { \quad k = 1 , \ldots , \zeta - 1 . } \end{array}
$$

This can be stated as

Lemma 5.8. As in the preceding lemma, let W be a nonsingular matrix with

$$
w _ { \ i \ i } = P _ { \jmath - 1 } ( c _ { \ i } ) \qquad f o r ~ i = 1 , \dots , s , ~ j = 1 , \dots , \zeta + 1 ,
$$

and let $B = \mathrm { d i a g } ( b _ { 1 } , \dots , b _ { s } )$ with $b _ { i } \neq 0$ . Then $D ( \zeta )$ (with $\zeta \leq s - 1 )$ is equivalent to the condition that the first $\zeta$ rows of the matrix $( W ^ { T } B ) A ( W ^ { T } B ) ^ { - 1 }$ are equal to those of $X _ { G }$ in (5.13) $( i f B$ is singular, we still have (5.19) below).

Proof. Formulas (5.18), writen in matrix form, give

$$
\begin{array} { r } { W ^ { T } B A = \left( \begin{array} { c c c c c c c } { 1 / 2 } & { - \xi _ { 1 } } & & & & \\ { \xi _ { 1 } } & { 0 } & { . . } & & & \\ & { . . } & { . . } & { - \xi _ { \zeta - 1 } } & & \\ & & { \xi _ { \zeta - 1 } } & { 0 } & { - \xi _ { \zeta } } & \\ { * } & { * } & { . . } & { . . } & { . . } & { * } \\ { * } & { * } & { . . } & { . . } & { . . } & { * } \end{array} \right) W ^ { T } B . } \end{array}
$$

It is now a natural and interesting question, whether both transformation matrices of the foregoing lemmas can be made equal, i.e., whether

$$
\begin{array} { r } { W ^ { T } B = W ^ { - 1 } \qquad \mathrm { o r } \qquad W ^ { T } B W = I . } \end{array}
$$

A first result is:

Lemma 5.9. For any quadrature formula of order $\geq 2 s - 1$ the matrix

$$
\boldsymbol { W } = \left( P _ { \jmath - 1 } ( c _ { \imath } ) \right) _ { \imath , \jmath = 1 , \ . \ , s }
$$

satisfies (5.20).

Proof.If the quadrature formula is of sufficiently high order, the polynomials $P _ { k } ( x ) P _ { l } ( x )$ $( k + l \le 2 s - 2 )$ are integrated exactly,i.e.,

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } P _ { k } ( c _ { \ i } ) P _ { l } ( c _ { \ i } ) = \int _ { 0 } ^ { 1 } P _ { k } ( x ) P _ { l } ( x ) d x = \delta _ { k l } ;
$$

this, however, is simply $W ^ { T } B W = I .$

Unfortunately, Condition (5.20) is too restrictive for many methods. We therefore relax our requirements as follows:

Definition 5.10. Let $\eta$ ， $\zeta$ be given integers between O and $s - 1$ . We say that an $s \times s$ -matrix $W$ satisfies $T ( \eta , \zeta )$ for the quadrature formula $( b _ { \imath } , c _ { \imath } ) _ { i = 1 } ^ { s }$ if

$$
\left. \begin{array} { l l } { W \mathrm { i s ~ n o n s i n g u l a r } } \\ { w _ { \iota \jmath } = P _ { \jmath - 1 } ( c _ { \iota } ) } & { i = 1 , \ldots , s , \quad \displaystyle \ j = 1 , \ldots , \mathrm { m a x } ( \eta , \zeta ) + 1 } \\ { W ^ { T } B W = \binom { I } { 0 } } & { 0 } \\ { 0 } & { R } \end{array} \right\}
$$

where $I$ is the $\left( \zeta + 1 \right) \times \left( \zeta + 1 \right)$ identity matrix; $R$ is an arbitrary $\left( s - \zeta - 1 \right) \times$ $\left( s - \zeta - 1 \right)$ matrix.

The main result is given in the following theorem. Together with Theorem 5.1 it is very helpful for the construction of high order methods (see Examples 5.16 and 5.24, and Theorem 13.15).

Theorem 5.11. Let W satisfy $T ( \eta , \zeta )$ for the quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right) _ { \imath = 1 } ^ { s } .$ Then for a Runge-Kutta method based on $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right)$ we have, for the matrix $X =$ $W ^ { - 1 } A W$ ，

a) the first n columns of $X$ are those of $X _ { G } \quad \Longleftrightarrow \quad C ( \eta )$ ， b)the first $\zeta$ rows of $X$ are those of $X _ { G } \quad \Longleftrightarrow \quad D ( \zeta )$

Proof. The equivalence of (a) with $C ( \eta )$ follows from Lemma 5.7. For the proof of (b) we multiply (5.19) from the right by $W$ and obtain

$$
\boldsymbol { W } ^ { T } \boldsymbol { B } \boldsymbol { W } \cdot \boldsymbol { X } = \boldsymbol { \widetilde { X } } \cdot \boldsymbol { W } ^ { T } \boldsymbol { B } \boldsymbol { W }
$$

where $\widetilde { X }$ is the large matrix of (5.19). Because of Condition (c) of $T ( \eta , \zeta )$ the first $\zeta$ rows of $\widetilde { X }$ and $X$ must be the same (write them as block matrices). The statement now follows from Lemma 5.8. □

We have stilleft open the question of the existence of $W$ satisfying $T ( \eta , \zeta )$ · The following two lemmas and Theorem 5.14 give an answer.

Lemma 5.12. If the quadrature formula has distinct nodes $c _ { i }$ and all weights positive $\left( \boldsymbol { b } _ { \imath } > \boldsymbol { 0 } \right)$ and if it is of order $p$ with $p \geq 2 \eta + 1$ and $p \geq 2 \zeta + 1$ ， then the matrix

$$
W = \Big ( p _ { \jmath - 1 } ( c _ { \imath } ) \Big ) _ { \imath , \jmath = 1 , \ldots , s }
$$

possesses property $T ( \eta , \zeta )$ and satisfies (5.20). Here $p _ { j } ( x )$ is the polynomial of degree $j$ orthonormalized for the scalar product

$$
\langle p , r \rangle = \sum _ { \imath = 1 } ^ { s } b _ { \imath } p ( c _ { \imath } ) r ( c _ { \imath } ) .
$$

Proof. The positivity of the $b ^ { \prime } s$ makes (5.24) a scalar product on the space of polynomials of degree $\leq s - 1$ .Because of the order property (compare with (5.22))， the orthonormalized $p _ { \jmath } ( x )$ must coincide for $j \le \operatorname* { m a x } ( \eta , \zeta )$ with the Legendre polynomials $P _ { \jmath } ( x )$ . Orthonormality with respect to (5.24) means that $W ^ { T } B W = I$ . □

Lemma 5.13. If the quadrature formula has distinct nodes $c _ { \imath }$ and is of order $p \ge s + \zeta$ ,then $W$ defined by (5.21) has property $T ( \eta , \zeta )$ ·

Proof. Because of $p \ge s + \zeta$ , (5.22) holds for $k = 0 , \ldots , s - 1$ and $l = 0 , \ldots , \zeta$ This ensures (c) of Definition 5.10. □

Theorem 5.14. Let the quadrature formula be of order $p$ . Then there exists a transformation with property $T ( \eta , \zeta )$ if and only if

$$
p \geq \eta + \zeta + 1 \qquad a n d \qquad p \geq 2 \zeta + 1 ,
$$

and at least $\mathrm { m a x } ( \eta , \zeta ) + 1$ numbers among $c _ { 1 } , \ldots , c _ { s }$ are distinct.

Proof. Set $\nu = \operatorname* { m a x } ( \eta , \zeta )$ and denote the columns of the transformation $W$ by $w _ { 1 } , \dots , w _ { s }$ . In virtue of (b) of $T ( \eta , \zeta )$ we have

$$
\boldsymbol { w } _ { j } = \left( P _ { \jmath - 1 } ( c _ { 1 } ) , \ldots , P _ { j - 1 } ( c _ { s } ) \right) ^ { T } \qquad \mathrm { f o r } \quad j = 1 , \ldots , \nu + 1 .
$$

These $\nu + 1$ columns are linearlyindependentonlyifat least $\nu + 1$ among $c _ { 1 } , . . . ,$ $c _ { s }$ are distinct. Now condition (c) of $T ( \eta , \zeta )$ means that $w _ { 1 } , \dotsc , w _ { \zeta + 1 }$ are orthonormal to $w _ { 1 } , \ldots , w _ { s }$ for the bilinear form $u ^ { T } B v$ . In particular, the orthonormality of $w _ { 1 } , \ldots , w _ { \zeta + 1 }$ t0 $w _ { 1 } , \ldots , w _ { \nu + 1 }$ (compare with (5.22)) means that the quadrature formula is exact for all polynomials of degree $\nu + \zeta$ . Therefore, $p \geq$ $\nu + \zeta + 1$ (which is the same as (5.25)) is a necessary condition for $T ( \eta , \zeta )$

To show its sufficiency, we complete $w _ { 1 } , \dots , w _ { \nu + 1 }$ to a basis of $\mathbb { R } ^ { s }$ . The new basis vectors $\widehat { w } _ { \nu + 2 } , \ldots , \widehat { w } _ { s }$ are then projected into the orthogonal complement of $\operatorname { s p a n } \langle w _ { 1 } , \dotsc , w _ { \zeta + 1 } \rangle$ with respect to $u ^ { T } B v$ by a Gram-Schmidt type orthogonalization. This yields

$$
\boldsymbol { w } _ { \boldsymbol { \jmath } } = \widehat { \boldsymbol { w } } _ { \boldsymbol { \jmath } } - \sum _ { k = 1 } ^ { \zeta + 1 } ( \boldsymbol { w } _ { k } ^ { T } \boldsymbol { B } \widehat { \boldsymbol { w } } _ { \boldsymbol { \jmath } } ) \boldsymbol { w } _ { k } \qquad \mathrm { f o r } \ j = \nu + 2 , \dots , s .
$$

# Construction of Implicit Runge-Kutta Methods

For the construction of implicit Runge-Kutta methods satisfying $B ( p ) , C ( \eta )$ and $D ( \zeta )$ with the help of Theorem 5.11, we first have to choose a quadrature formula of order $p$ . The following lemma is the basic result for Gaussian integration.

Lemma 5.15. Let $c _ { 1 } , \ldots , c _ { s }$ be real and distinct and let $b _ { 1 } , \dots , b _ { s }$ be determined by condition $B ( s )$ (i.e.,the formula is “interpolatory"). Then this quadrature formula is of order $2 s - k$ if and only if the polynomial $M ( x ) = ( x - c _ { 1 } ) ( x -$ $c _ { 2 } ) \ldots ( x - c _ { s } )$ is orthogonal to all polynomials of degree $\leq s - k - 1$ , i.e., if and only if

$$
M ( x ) = C \Bigl ( P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \ldots + \alpha _ { k } P _ { s - k } ( x ) \Bigr ) .
$$

For a proof see Exercise 2.

We see from (5.26) that all quadrature formulas of order $2 s - k$ can be specified in terms of $k$ parameters $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$

Next, if the integers $\eta$ and $\zeta$ satisfy $\eta + \zeta + 1 \leq 2 s - k$ and $2 \zeta + 1 \leq 2 s - k$ (cf. (5.25)), we can compute a matrix $W$ satisfying $T ( \eta , \zeta )$ from Theorem 5.14 (or one of Lemmas 5.12 and 5.13). Finally a matrix $X$ is chosen which satisfies (a) and (b) of Theorem 5.11. Then the Runge-Kutta method with coefficients $A = W X W ^ { - 1 }$ is of order at least $\operatorname* { m i n } ( \eta + \zeta + 1 , 2 \eta + 2 )$ by Theorem 5.1.

Example 5.16. We search for all implicit Runge-Kutta methods satisfying $B ( 2 s -$ 2), $C ( s - 1 )$ and $D ( s - 2 )$ , i.e.， methods which are of order at least $2 s - 2$ by Theorem 5.1. As in (5.26), we put

$$
M ( x ) = C \left( P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x ) \right) .
$$

If $\alpha _ { 2 }$ satisfies

$$
\alpha _ { 2 } < \frac { s - 1 } { s } \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } } ,
$$

then the roots of $M$ are real and distinct (see Exercise 7). The matrix $W$ given in (5.21) has Property $T ( s - 1 , s - 2 )$ by Lemma 5.13. Finally we put

$$
X = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { \cdot } } & { { } } & { { } } & { { } } \\ { { } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { - \xi _ { s - 2 } } } & { { } } \\ { { } } & { { } } & { { \xi _ { s - 2 } } } & { { 0 } } & { { \beta _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { \beta _ { s } } } \end{array} \right)
$$

(see Theorem 5.11), and obtain with $A = W X W ^ { - 1 }$ a family of implicit Runge-Kutta methods of order 2s - 2 with the four parameters α1,α2,βg, βg-1\*

All methods of Table 5.13 (with the exception of Lobatto IIIB) must be special cases. The corresponding parameter values are indicated in Table 5.14 (for their computation see Exercise 3). If we put $\alpha _ { \mathbf { 1 } } = 0$ and $\alpha _ { 2 } = - \sqrt { 2 s + 1 } / \sqrt { 2 s - 3 }$ (Lobato quadrature), we obtain the two-parameter family of Chipman (1976).

Table 5.14. Special cases of method (5.27,5.28)   

<table><tr><td rowspan=1 colspan=1>Method</td><td rowspan=1 colspan=1>α1</td><td rowspan=1 colspan=1>α2</td><td rowspan=1 colspan=1>β</td><td rowspan=1 colspan=1>β-1</td></tr><tr><td rowspan=1 colspan=1>GaussRadau IARadau IIALobatto IIIALobatto IIIC</td><td rowspan=1 colspan=1>0√2s+1/√2s-1√2s+1/√2s-100</td><td rowspan=1 colspan=1>000√2s+1/√2s-3</td><td rowspan=1 colspan=1>01/(4s-2)1/(4s-2)0</td><td></td></tr></table>

# Stability Function

We try to express the stability function of an implicit Runge-Kutta method in terms of the transformed Runge-Kutta matrix $X = W ^ { - 1 } A W$ . From (b) and (c) of Property $T ( \eta , \zeta )$ it follows that

$$
\boldsymbol { W } \boldsymbol { e } _ { 1 } = \mathbb { 1 } , \qquad \boldsymbol { W } ^ { T } \boldsymbol { B } \mathbb { 1 } = \boldsymbol { e } _ { 1 } , \qquad \boldsymbol { e } _ { 1 } = ( 1 , 0 , \dots , 0 ) ^ { T } .
$$

Hence Formulas (3.2) and (3.3)become

$$
R ( z ) = 1 + z e _ { 1 } ^ { T } ( I - z X ) ^ { - 1 } e _ { 1 } ,
$$

$$
R ( z ) = \frac { \operatorname* { d e t } ( I - z X + z e _ { 1 } e _ { 1 } ^ { T } ) } { \operatorname* { d e t } ( I - z X ) } .
$$

The stability function depends only on $X$ and not on the underlying quadrature formula. Hence,the stability function of the method of Example 5.16 depends on $\beta _ { s }$ and $\beta _ { s - 1 }$ only.Formula (5.31) becomes more symmetric (Hairer & Turke 1984) if we introduce the arithmetic mean of the matrices $X$ and $X - e _ { 1 } e _ { 1 } ^ { T }$ and define

$$
\boldsymbol { Y } = \boldsymbol { X } - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ,
$$

which is just the matrix $X$ without the $1 / 2$ in the $( 1 , 1 )$ -position.

Proposition 5.17. For a Runge-Kutta method (3.1) let $W$ satisfy $T ( \eta , \zeta )$ for some $\eta$ ， $\zeta \geq 0$ , and let $Y$ be given by(5.32) where $X = W ^ { - 1 } A W$ . The stability function then satisfies

$$
R ( z ) = { \frac { 1 + { \frac { 1 } { 2 } } \Psi ( z ) } { 1 - { \frac { 1 } { 2 } } \Psi ( z ) } }
$$

with

$$
\Psi ( z ) = z e _ { 1 } ^ { T } ( I - z Y ) ^ { - 1 } e _ { 1 } .
$$

Proof. Applying the Runge-Kuta method to the test equation (2.9) yields

$$
g = \mathbb { 1 } y _ { 0 } + z A g , \qquad y _ { 1 } = y _ { 0 } + z b ^ { T } g .
$$

With $W ^ { - 1 } g = \widehat { g } = ( \widehat { g } _ { 1 } , \dots , \widehat { g } _ { s } ) ^ { T }$ this becomes

$$
( I - z Y ) \widehat { g } = e _ { 1 } \bigl ( y _ { 0 } + \frac { z } { 2 } \widehat { g } _ { 1 } \bigr ) , \qquad y _ { 1 } = y _ { 0 } + z \widehat { g } _ { 1 } ,
$$

where we have used (5.29). Computing $\widehat { g } _ { 1 }$ from the first equation of (5.35）) and inserting this into the second one gives the result. □

If the Runge-Kutta method satisfies $B ( 2 \nu + 1 ) , C ( \nu )$ and $D ( \nu )$ for some integer $\nu$ ,then $Y$ is given by (see Theorem 5.11)

$$
Y = \left( \begin{array} { c c c c c } { { 0 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { \cdot _ { \cdot } } } & { { \cdot _ { \cdot } } } & { { } } & { { } } \\ { { } } & { { \cdot _ { \cdot } } } & { { 0 } } & { { - \xi _ { \nu } } } \\ { { } } & { { } } & { { } } & { { \xi _ { \nu } } } & { { \boxed { Y _ { \nu } } } } \end{array} \right) .
$$

In this case the computation of (5.34) for the $\left( s , s \right)$ -matrix $Y$ can be reduced to that of the smaller $\bigl ( s - \nu , s - \nu \bigr )$ -matrix $Y _ { \nu }$ as follows:

Theorem 5.18. If $Y$ is given by (5.36), the function $\Psi ( z )$ of(5.34) has the continued fraction representation

$$
\Psi ( z ) = { \frac { z \Big | } { | 1 } } + { \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } \Big | } { | \ 1 \ } } + \ldots + { \frac { \xi _ { \nu - 1 } ^ { 2 } z ^ { 2 } \Big | } { | \ 1 \ } } + \xi _ { \nu } ^ { 2 } z \Psi _ { \nu } ( z )
$$

where $\Psi _ { \nu } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \nu } ) ^ { - 1 } e _ { 1 } .$

Proof. Let $Y _ { \jmath }$ (for $0 \leq j \leq \nu + 1 ,$ ）denote the $\left( s - j , s - j \right)$ principal minors of $Y$ , where the first $j$ rows and columns are suppressed. Expanding the determinant of $I - z Y _ { \jmath - 1 }$ with respect to the first row (and then the first column) gives for $j = 1 , \dots , \nu$

$$
\operatorname* { d e t } ( I - z Y _ { \jmath - 1 } ) = \operatorname* { d e t } ( I - z Y _ { \jmath } ) + \xi _ { \jmath } ^ { 2 } z ^ { 2 } \operatorname* { d e t } ( I - z Y _ { \jmath + 1 } ) .
$$

By Cramer's rule, the functions $\Psi _ { \jmath } ( z )$ can also be written as

$$
\Psi _ { j } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \jmath } ) ^ { - 1 } e _ { 1 } = z \frac { \operatorname * { d e t } ( I - z Y _ { \jmath + 1 } ) } { \operatorname * { d e t } ( I - z Y _ { \jmath } ) } .
$$

Dividing (5.38) by $\operatorname* { d e t } ( I - z Y _ { \jmath } )$ yields

$$
\Psi _ { \jmath - 1 } ( z ) = \frac { z } { 1 + \xi _ { \jmath } ^ { 2 } z \Psi _ { \jmath } ( z ) } .
$$

A repeated use of (5.40) gives (5.37) since $\Psi ( z ) = \Psi _ { 0 } ( z )$

We are thus naturally led to continued fraction expansions, a technique which was historically the earliest one.Birkhoff & Varga(1965) used it in their proof of the $A$ -stability of the diagonal Padé approximations. Later, Ehle (1969,1973) tried to extend “Varga's proof" to verify the $A$ -stability of the first and second subdiagonals of the Padé table ("This was unsuccessful because the resulting continued fraction expansions were not easily related to one another."). Therefore, Ehle (1973),Ehle & Picel (1975),proved $A$ -stability results for the first and second subdiagonal and some generalizations by a completely different method. The following study of $A$ -stability (see Butcher 1977,Hairer 1982, Hairer & Turke 1984) combines the above continued fraction expansion with properties of positive functions.

# Positive Functions

Many stability conditions for numerical methods can be expressed in the form that some associated function is positive.

(G. Dahlquist 1978)

$A$ -stability ofan implicit Runge-Kutta method is defined bythe property

$$
| R ( z ) | < 1 \qquad \mathrm { f o r } \quad \mathrm { R e } z < 0 .
$$

Since the transformation $( 1 + \zeta ) / ( 1 - \zeta )$ occurring in (5.33） maps the negative half-plane onto the open unit disc, (5.41) is equivalent to

$$
\operatorname { R e } \Psi ( z ) < 0 \qquad \operatorname { f o r } \quad \operatorname { R e } z < 0 .
$$

This condition means that $- \Psi ( - z )$ is a positive function; for rational functions the concept of positivity can be defined as follows:

Definition 5.19.A rational function $f ( z )$ is called positive if

$$
\operatorname { R e } f ( z ) > 0 \qquad { \mathrm { f o r } } \quad \operatorname { R e } z > 0 .
$$

A nice survey on the relevance of positive functions to numerical analysis is given by Dahlquist (1978). The following lemmas collect some properties of positive functions.

Lemma 5.20. Let $f ( z )$ and $g ( z )$ be positive functions. Then we have

a） $\alpha f ( z ) + \beta g ( z )$ is positive, if $\alpha > 0$ and $\beta \geq 0$ ；   
$b _ { . }$ ） $1 / f ( z )$ is positive;   
c） $f ( g ( z ) )$ is positive.

Observe that the poles of a positive function cannot lie in the positive half-plane, but poles on the imaginary axis are possible, e.g., the function $1 / z$ is positive.

Lemma 5.21. Suppose that

$$
f ( z ) = \frac { c } { z } + g ( z ) w i t h g ( z ) = { \cal O } ( 1 ) \mathrm { f o r } z  0 ,
$$

and $g ( z ) \not \equiv 0$ . Then $f ( z )$ is positive if and only if $c \geq 0$ and $g ( z )$ is positive.

Proof. The “if-part" follows from Lemma 5.20. Suppose now that $f ( z )$ is positive. The constant $c$ has to be non-negative, since for small positive values of $z$ we have R $\mathrm { ~ e ~ } f ( z ) > 0$ . On the imaginary axis we have (apart from poles) $\operatorname { R e } g ( i y ) =$ $\\\\\\\\\\\\mathrm  { t e } f ( i y ) \geq 0$ or more precisely

$$
\operatorname* { l i m } _ { z \to i y , \mathrm { \tiny ~ R e } } z _ { > 0 } \mathrm { R e } g ( z ) \geq 0 \qquad \mathrm { f o r } \quad y \in \mathbb { R } .
$$

The maximum principle for harmonic functions then implies that either $g ( z ) \equiv 0$ or $g ( z )$ is positive. □

A consequence of this lemma is the following characterization of $A$ -stability.

Theorem 5.22. Consider a Runge-Kutta method whose stability function is given by (5.33) with $Y$ as in (5.36). It is $A$ -stable if and only if

$$
\operatorname { R e } \Psi _ { \nu } ( z ) < 0 \qquad f o r \quad \operatorname { R e } z < 0
$$

where $\Psi _ { \nu } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \nu } ) ^ { - 1 } e _ { 1 } ~ a s ~ i n \left( 5 . 3 7 \right.$ ）.

Proof. We consider the submatrices $Y _ { j }$ of $Y$ and the functions $\Psi _ { j } ( z )$ of (5.39). As we prefer to work with positive functions we put

$$
\chi _ { \ j } ( z ) = - \Psi _ { \ j } ( - z ) = z e _ { 1 } ^ { T } ( \MakeUppercase { \romannumeral 1 } + z Y _ { \nu } ) ^ { - 1 } e _ { 1 } .
$$

By (5.42), $A$ -stability is equivalent to the positivity of $\chi _ { 0 } ( z )$ and condition (5.43) means that $\chi _ { \nu } ( z )$ is a positive function. Relation (5.40) becomes

$$
\big ( \chi _ { j - 1 } ( z ) \big ) ^ { - 1 } = \frac { 1 } { z } + \xi _ { j } ^ { 2 } \chi _ { j } ( z ) .
$$

Since all $\chi _ { \ j } ( z )$ are bounded near the origin and do not vanish identically (see (5.44)), it follows from Lemma 5.21 that $\chi _ { \jmath } ( z )$ is a positive function iff $\chi _ { \ j - 1 } ( z )$ is positive. This proves the theorem. □

Example 5.23. For the Runge-Kuta method of Example 5.16 with $X$ given by (5.28) we have

$$
\Psi _ { s - 2 } ( z ) = \frac { z ( 1 - \beta _ { s } z ) } { 1 - \beta _ { s } z - \xi _ { s - 1 } \beta _ { s - 1 } z ^ { 2 } } .
$$

Since

$$
\Big ( \Psi _ { s - 2 } ( z ) \Big ) ^ { - 1 } = \frac { 1 } { z } - \xi _ { s - 1 } \beta _ { s - 1 } \frac { z } { 1 - \beta _ { s } z }
$$

it follows from Lemma 5.21 and Theorem 5.22 that the method is $A$ -stable iff

$$
\beta _ { s - 1 } = 0 ~ \mathrm { o r } ~ ( \beta _ { s - 1 } < 0 ~ \mathrm { a n d } ~ \beta _ { s } \geq 0 ) .
$$

Comparing this result with Tables 5.14 and 5.13 leads to a second proof for the $A$ -stability of the diagonal and the first two subdiagonal Padé approximations for $e ^ { z }$ (see Theorem 4.12).

Example 5.24 (Construction of all $A$ -stable Runge-Kutta methods satisfying $B ( 2 s - 4 )$ ， $C ( s - 2 )$ and $D ( s - 3 ) .$ ). We take a quadrature formula of order $2 s - 4$ and construct, by Theorem 5.14, a matrix $W$ satisfying Property $T ( s - 2 , s - 3 )$ The Runge-Kutta matrix $A$ is then of the form

$$
A = W ( Y + \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ) W ^ { - 1 }
$$

with $Y$ given by (5.36), $\nu = s - 3$ and

$$
Y _ { s - 3 } = \left( \begin{array} { c c c } { { 0 } } & { { \gamma _ { s - 2 } } } & { { \beta _ { s - 2 } } } \\ { { \xi _ { s - 2 } } } & { { \gamma _ { s - 1 } } } & { { \beta _ { s - 1 } } } \\ { { 0 } } & { { \gamma _ { s } } } & { { \beta _ { s } } } \end{array} \right) .
$$

For the study of $A$ -stability we have to compute $\Psi _ { s - 3 } ( z )$ from (5.39). Expanding $\operatorname* { d e t } ( I - z Y _ { s - 3 } )$ with respect to its first column we obtain

$$
\displaystyle \left( \Psi _ { s - 3 } ( z ) \right) ^ { - 1 } = \frac { 1 } { z } + \frac { z \xi _ { s - 2 } ( g _ { 0 } - g _ { 1 } z ) } { 1 - f _ { 1 } z + f _ { 2 } z ^ { 2 } }
$$

where

$$
\begin{array} { r l } & { f _ { 1 } = \beta _ { s } + \gamma _ { s - 1 } , \qquad f _ { 2 } = \beta _ { s } \gamma _ { s - 1 } - \beta _ { s - 1 } \gamma _ { s } , } \\ & { g _ { 0 } = - \gamma _ { s - 2 } , \qquad g _ { 1 } = - \beta _ { s } \gamma _ { s - 2 } + \beta _ { s - 2 } \gamma _ { s } . } \end{array}
$$

By Lemma 5.21 and Theorem 5.22 we have $A$ -stability iff either $g _ { 0 } = g _ { 1 } = 0$ or

$$
\frac { z ( g _ { 0 } + g _ { 1 } z ) } { 1 + f _ { 1 } z + f _ { 2 } z ^ { 2 } }
$$

is a positive function, which is equivalent to (see Exercise 4b)

$$
g _ { 0 } > 0 , \quad g _ { 1 } \geq 0 , \quad f _ { 2 } \geq 0 , \quad g _ { 0 } f _ { 1 } - g _ { 1 } \geq 0 .
$$

A similar characterization of $A$ -stable Runge-Kutta methods of order $2 s - 4$ is given in Wanner (1980).

# Exercises

1. Verify the integration formulas (5.10) for the shifted Legendre polynomials.

Hint. By orthogonality $\int _ { 0 } ^ { x } P _ { k } ( t ) d t$ must be a linear combination of $P _ { k + 1 } , P _ { k }$ and $P _ { k - 1 }$ only. The coefficient of $P _ { k }$ vanishes by symmetry. For the rest just look at the coefficients of $x ^ { k + 1 }$ and $x ^ { k - 1 }$

2. Give a proof of Lemma 5.15.

Hint (Jacobi 1826). If $f ( x )$ is a polynomial of degree $2 s - k - 1$ ,and $r ( x )$ the interpolation polynomial of degree $s - 1$ , then $\begin{array} { r } { f ( x ) = q ( x ) M ( x ) + r ( x ) } \end{array}$ ， where deg $q ( x ) \leq s - k - 1$

3.Let $R ( z )$ be the stability function of the Runge-Kutta method of Example 5.16.

a) The degree of its denominator is $\leq s - 1$ iff $\beta _ { s } = \beta _ { s - 1 } \xi _ { s - 1 } 2 ( 2 s - 3 )$

Hint. Use Formula (5.31) and the fact that $\operatorname* { d e t } ( I - z X _ { G } )$ is the denominator of the diagonal Padé approximation.

b) The degree of the numerator of $R ( z )$ is $\leq s - 1$ iff

$$
\beta _ { s } = - \beta _ { s - 1 } \xi _ { s - 1 } 2 ( 2 s - 3 ) .
$$

c) The degree of the numerator of $R ( z )$ is $\leq s - 2$ iff in addition to (5.49) it holds $\beta _ { s } = 1 / ( 2 s - 2 )$

d) Verify the entries of Table 5.14.

4．a) The function

$$
s ( z ) = \frac { \alpha + \beta z } { \gamma + \delta z }
$$

with $\gamma > 0$ satisfies $\operatorname { R e } s ( z ) \geq 0$ for $\mathrm { R e } z > 0$ iff $\alpha \ge 0 , \beta \ge 0$ and $\delta \ge 0$ b) Use the identity (for $g _ { 0 } > 0$ ）

$$
{ \frac { 1 + f _ { 1 } z + f _ { 2 } z ^ { 2 } } { z ( g _ { 0 } + g _ { 1 } z ) } } - { \frac { 1 } { z g _ { 0 } } } = { \frac { ( f _ { 1 } - g _ { 1 } / g _ { 0 } ) + f _ { 2 } z } { g _ { 0 } + g _ { 1 } z } }
$$

to verify that the function given in (5.47) is positive iff(5.48) holds.

5. Suppose that

$$
f ( z ) = c z + g ( z ) \qquad { \mathrm { w i t h } } \qquad g ( z ) = { \mathcal { O } } ( 1 ) \qquad { \mathrm { f o r ~ } } z \to \infty
$$

and $g ( z ) \not \equiv 0$ . Using the transformation $z  1 / z$ in Lemma 5.21, show that $f ( z )$ is a positive function, if and only if $c \geq 0$ and $g ( z )$ is positive.

6. Give an alternative proof of the Routh criterion (Theorem 13.4 of Chapter I): All zeros of the real polynomial

$$
p ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \ldots + a _ { n } \quad ( a _ { 0 } > 0 )
$$

lie in the negative half-plane Re $z < 0$ if and only if

$$
c _ { \imath 0 } > 0 \qquad \mathrm { f o r } i = 0 , 1 , . . . , n .
$$

The $c _ { \imath \jmath }$ are the coefficients of the polynomials

$$
p _ { \ i } ( z ) = c _ { \ i 0 } z ^ { n - 1 } + c _ { \ i 1 } z ^ { n - \ i - 2 } + c _ { \ i 2 } z ^ { n - \ i - 4 } + . . .
$$

where

$$
\begin{array} { l l } { { p _ { 0 } ( z ) = a _ { 0 } z ^ { n } + a _ { 2 } z ^ { n - 2 } + \ldots , ~ } } & { { i . e . , ~ c _ { 0 \jmath } = a _ { 2 \jmath } } } \\ { { { } } } & { { { } p _ { 1 } ( z ) = a _ { 1 } z ^ { n - 1 } + a _ { 3 } z ^ { n - 3 } + \ldots , ~ } } & { { i . e . , ~ c _ { 1 \jmath } = a _ { 2 \jmath + 1 } . } } \end{array}
$$

and

$$
p _ { \iota + 1 } ( z ) = c _ { \iota 0 } p _ { \iota - 1 } ( z ) - c _ { \iota - 1 , 0 } z p _ { \iota } ( z ) , \qquad i = 1 , \ldots , n - 1 .
$$

Hint. By the maximum principle for harmonic functions the condition ${ } ^ { * } p ( z ) \neq$ 0 for $\mathrm { R e } z \ge 0 ^ { 3 }$ is equivalent to ‘ $^ { \prime } | p ( - z ) / p ( z ) | < 1$ for $\mathrm { R e } z > 0 ^ { , , }$ and the condition that $p _ { 0 } ( z )$ and $p _ { 1 } ( z )$ are irreducible. Using the transformation (5.33) this becomes equivalent to the positivity of $p _ { 0 } ( z ) / p _ { 1 } ( z )$ . Now divide (5.50) by $c _ { \imath - 1 , 0 } p _ { \imath } ( z )$ and use Exercise 5 recursively.

7. Show that

$$
\alpha _ { 2 } < \frac { s - 1 } { s } \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } }
$$

is a suficient condition for $M ( x ) = P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x )$ to have real and pairwise distinct roots.

Hint. (See “Lemma $1 8 ^ { \circ }$ of Ngrsett & Wanner 1981). Consider the set $D$ of all pairs $\left( \alpha _ { 1 } , \alpha _ { 2 } \right)$ for which the roots $c _ { \imath }$ of $M ( x )$ are real and distinct, and the corresponding interpolatory quadrature formula has positive $b _ { \imath }$ . Verify that $( 0 , 0 ) \in D$ ， and show that for $( \alpha _ { 1 } , \alpha _ { 2 } ) \in \partial D$ either one $b _ { i }$ becomes zero or two $c _ { \imath }$ coalesce but the quadrature formula remains of order $2 s - 2$ . Therefore it must be the Gaussian formula with $s - 1$ nodes of order $2 s - 2$ and we must have

$$
P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x ) = c ( x - \beta ) P _ { s - 1 } ( x ) .
$$

Now use the three-term recursion formula

$$
s \xi _ { s } P _ { s } ( x ) = ( x - 1 / 2 ) P _ { s - 1 } ( x ) - ( s - 1 ) \xi _ { s - 1 } P _ { s - 2 } ( x )
$$

(bramowitz&Stegnp82modfd)t $x P _ { s - 1 }$ on the rght of (5.52)Thenobaibyompingtheoeentsof $P _ { s } , P _ { s - 1 }$ and $P _ { s - 2 }$

$$
c = { \frac { 1 } { s \xi _ { s } } } \qquad \alpha _ { 1 } = { \frac { 1 } { s \xi _ { s } } } \Big ( { \frac { 1 } { 2 } } - \beta \Big ) , \qquad \alpha _ { 2 } = { \frac { s - 1 } { s } } { \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } } } .
$$

If $\beta$ is one of the roots of $P _ { s - 1 }$ ,then (5.52) has adouble root and the estimate (5.51) for $\alpha _ { 2 }$ is optimal.

# IV.6Diagonally Implicit RK Methods

... they called their methods “diagonally implicit”,a term which is reserved here for the special case where all diagonal entries are equal ... (R.Alexander 1977)

We continue to quote from this nice paper: “To integrate a system of $\mathscr { n }$ differential equations, an implicit method with a full $s \times s$ matrix requires the solution of ns simultaneous implicit (in general nonlinear) equations in each time step(...） One way to circumvent this difficulty is to use a lower triangular matrix $( a _ { i j } )$ (i.e., a matrix with $a _ { \scriptscriptstyle \imath \jmath } = 0$ for $i < j )$ ; the equations may then be solved in $s$ successive stages with only an $\mathscr { n }$ -dimensional system to be solved at each stage". In accordance with many authors,and in disaccordance with others (see above),we call such a method diagonally implicit (DIRK).

"In solving the $n$ -dimensional systems by Newton-type iterations one solves linear systems at each stage with a coeficient matrix of the form $I - h a _ { i \imath } \partial f / \partial y$ If all $a _ { \ i i }$ are equal one may hope to use repeatedly the stored LU-factorization of a single such matrix". When we want to emphasize this additional property for a DIRK method, we shall call it a singly diagonally implicit (SDIRK) method.

It is a curious coincidence that in the early seventies at least four theses dedi-cated a large part of their research to DIRK and SDIRK methods, very often having in mind their usefulness for the treatment of partial differential equations (R. Alt 1971,M. Crouzeix 1975,A. Kurdi 1974, S.P. Ngrsett 1974). The classical paper on the subject is Alexander (1977).

# Order Conditions

The traditional problem of choosing the coefficients leads to a nonlinear algebraic jungle,to which civilization and order were brought in the pioneering work of J.C. Butcher, further refined in the Thesis of M. Crouzeix. (R.Alexander 1977)

We want to make the“jungle” still a little more civilized by the following idea: consider a SDIRK scheme

<table><tr><td rowspan="2">C1 C2</td><td colspan="4">Y</td></tr><tr><td>a21</td><td>Y</td><td></td><td></td></tr><tr><td>：</td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td>：</td><td></td><td></td><td></td></tr><tr><td>cs</td><td></td><td></td><td></td><td>Y</td></tr><tr><td></td><td>ag1</td><td>ag2</td><td></td><td></td></tr><tr><td></td><td>b</td><td>b2</td><td></td><td>8</td></tr></table>

with $s$ stages. The order conditions (see Vol. I, Sect.II.2) consist of sums such as

$$
\sum _ { \jmath , k , l } b _ { \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } .
$$

Because there are now more non-zero entries in the matrix $A$ than for explicit methods, this sum contains far more terms as it did before. The trick is to transfer all expressions containing a $\gamma$ to the right-hand side of (6.1). The resulting sum, denoted by $\sum ^ { \prime }$ , is then only built upon the subdiagonal entries as for explicit Runge-Kutta methods. The right-hand side becomes (for this example)

$$
{ \sum _ { j , k , l } } ^ { \prime } b _ { _ { j } } a _ { _ { j k } } a _ { k l } = \sum _ { j , k , l } b _ { _ { j } } ( a _ { _ { j k } } - \gamma \delta _ { _ { j k } } ) ( a _ { k l } - \gamma \delta _ { _ { k l } } )
$$

where $\delta _ { \ j \ k }$ denotes the Kronecker delta. Multiplying out we obtain

$$
\sum _ { \jmath , k , l } { ^ { \prime } b } _ { \jmath } a _ { \jmath k } a _ { k l } = \sum _ { \jmath , k , l } b _ { \jmath } a _ { \jmath k } a _ { k l } - \gamma \Big ( \sum _ { \jmath , l } b _ { j } a _ { j l } + \sum _ { \jmath , k } b _ { \jmath } a _ { \jmath k } \Big ) + \gamma ^ { 2 } \sum _ { j } b _ { \jmath } .
$$

For all sums on the right we insert order conditions (e.g. from Theorem 2.1 of Sect.II.2) and obtain

$$
\sum _ { \jmath , k , \ell } { } ^ { \prime } b _ { \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } - \gamma + \gamma ^ { 2 } .
$$

The general rule is that there appears an alternating polynomial in $\gamma$ whose coefficients are sums of $1 / \gamma ( u )$ ，where $u$ runs through all trees which are obtained by “short-circuiting” one, two, three,etc. vertices of $t$ (with exception of the root). The conditions for order 4 obtained in this way are summarized in Table 6.1. For $s \approx 2$ ， $p = 3$ and $s \simeq 3$ ， $p = 4$ these simplified conditions have only very few nonzero terms and the equations become especially simple to solve (see Exercise 1).

# Stiffly Accurate SDIRK Methods

Our main interest here lies in methods satisfying

$$
a _ { s _ { 3 } } = b _ { _ { _ { J } } } \quad \mathrm { f o r } \quad j = 1 , \ldots , s ,
$$

i.e., in methods for which the numerical solution $y _ { 1 }$ is identical to the last internal stage. A first consequence of this property is that $R ( \infty ) = 0$ (see Proposition 3.8). The order conditions for such methods can, instead of (6.1"), be simplified still further: consider again the example (6.1), which can now be written as

$$
\sum _ { \jmath , k , l } a _ { s \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } .
$$

Table 6.1. Order conditions for SDIRK methods   

<table><tr><td>t ·</td><td></td><td>e(t）|previous conditions</td><td>simplified conditions</td></tr><tr><td rowspan="5">广 m m /m k</td><td>∑bj=1 1 2 3</td><td>∑b;=1</td></tr><tr><td>∑bjak=1</td><td>∑&#x27;bajk=-γ</td></tr><tr><td>∑bajka=1</td><td>∑&#x27;bjajajl=-γ+²</td></tr><tr><td>∑bajkakl= 3</td><td>∑&#x27;byajkakl=-γ+²</td></tr><tr><td>∑bjakajlajm= ∑bajkakiam=</td><td>∑&#x27;bakalagm=1-Y+2²-3 ∑&#x27;bajkaklaym=-x+2γ²-3</td></tr></table>

This time we have, instead of (6.1')

$$
\begin{array} { r l } {  { \sum _ { j , k , l } a _ { s _ { j } } a _ { j k } a _ { k l } = \sum _ { j , k , l } ( a _ { s _ { j } } - \gamma \delta _ { s _ { j } } ) ( a _ { j k } - \gamma \delta _ { j k } ) ( a _ { k l } - \gamma \delta _ { k l } ) } } \\ & { = \sum _ { j , k , l } a _ { s j } a _ { j k } a _ { k l } - \gamma \Bigl ( \sum _ { j , k } a _ { s _ { j } } a _ { j k } + \sum _ { j , l } a _ { s j } a _ { j l } + \sum _ { k , l } a _ { s k } a _ { k l } \Bigr ) } \\ & { + \gamma ^ { 2 } \Bigl ( \sum _ { j } a _ { s j } + \sum _ { k } a _ { s k } + \sum _ { l } a _ { s l } \Bigr ) - \gamma ^ { 3 } \cdot 1 . } \end{array}
$$

Again inserting known order conditions, we now obtain

$$
{ \sum _ { \jmath , k , l } } ^ { \prime } a _ { s \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } - \frac { 3 } { 2 } \gamma + 3 \gamma ^ { 2 } - \gamma ^ { 3 } .
$$

The general rule is similar to the one above: the difference is that $a l l$ vertices (including the root) are now available for being short-circuited. Another example, for the tree $t _ { 4 2 }$ , is sketched in Fig.6.1 and leads to the following right-hand side:

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 8 } - \gamma \Big ( \frac { 1 } { 3 } + \frac { 1 } { 3 } + 1 \cdot \frac { 1 } { 2 } + \frac { 1 } { 6 } \Big ) + \gamma ^ { 2 } \Big ( \frac { 1 } { 2 } + 1 \cdot 1 + 1 \cdot 1 + \frac { 1 } { 2 } + \frac { 1 } { 2 } + \frac { 1 } { 2 } \Big ) } \\ { \displaystyle - \gamma ^ { 3 } ( 1 + 1 + 1 + 1 ) + \gamma ^ { 4 } = \frac { 1 } { 8 } - \frac { 4 } { 3 } \gamma + 4 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } . } \end{array}
$$

The order conditions obtained in this manner are displayed in Table 6.2 for all trees of order $\leq 4$ . The expressions $\sum ^ { \prime }$ are written explicitly for the SDIRK method

![](images/29783c2197496d29ab17e9eab06b5cfa1d17bcfcc1a88391bfe2de1ed8bbb3db.jpg)  
Fig. 6.1. Short-circuiting tree $\displaystyle t _ { 4 2 }$

(6.3)with $s \approx 5$ satisfying condition (6.2)

![](images/e1597db1bfe94a070ca257cf1f442e3018edb8ee51a120b4e7ed4f7f83367bba.jpg)

Observe that they become very similar to those of Formulas (1.11) in Sect. II.1.

![](images/1f7a44ca1ab69124eaad0fc093d00c94d6f1fbd309467a00085515247276922a.jpg)

$$
\begin{array} { r l } & { \sum ^ { \prime } a _ { 3 j } - b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = p _ { 1 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 1 } - b _ { 2 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } + b _ { 3 } c _ { g _ { 4 } ^ { \prime } } ^ { \prime } = p _ { 2 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 2 } + b _ { 2 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } + b _ { 4 } c _ { g _ { 4 } ^ { \prime } } ^ { \prime 2 } = p _ { 3 } } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } c _ { g _ { 1 } } a _ { g _ { 1 } } - b _ { 3 } a _ { g _ { 1 } } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 4 } ( a _ { 4 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + a _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } ) = p _ { 4 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 1 } a _ { 1 } - b _ { 3 } a _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 2 } + b _ { 4 } ( a _ { 4 } c _ { g _ { 1 } ^ { \prime } } ^ { 2 } + a _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } ) = p _ { 4 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } a _ { 1 ^ { \prime } } a _ { 1 ^ { \prime } m } - b _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 3 } a _ { 1 } - b _ { 4 } c _ { g _ { 1 } ^ { \prime } } ^ { 4 } a _ { 1 ^ { \prime } } = p _ { 5 } } \\ &  \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } a _ { 1 ^ { \prime } } a _ { 1 m } - b _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 4 } a _ { 3 } c _  \end{array}
$$

$$
\begin{array} { l } { p _ { 5 } = \displaystyle \frac { 1 } { 4 } - 2 \gamma + \frac { 9 } { 2 } \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 6 } = \displaystyle \frac { 1 } { 8 } - \frac { 4 } { 3 } \gamma + 4 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 7 } = \displaystyle \frac { 1 } { 1 2 } - \gamma + \frac { 7 } { 2 } \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 8 } = \displaystyle \frac { 1 } { 2 4 } - \frac { 2 } { 3 } \gamma + 3 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \end{array}
$$

Solution of Equations (6.4). By clever elimination from equations (6.4;4） and (6.4;6) as well as (6.4;4) and (6.4;7) we obtain

$$
\begin{array} { r l } & { b _ { 3 } a _ { 3 2 } c _ { 2 } ^ { \prime } \big ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } \big ) = c _ { 4 } ^ { \prime } p _ { 4 } - p _ { 6 } } \\ & { b _ { 4 } c _ { 3 } ^ { \prime } a _ { 4 3 } \big ( c _ { 2 } ^ { \prime } - c _ { 3 } ^ { \prime } \big ) = c _ { 2 } ^ { \prime } p _ { 4 } - p _ { 7 } . } \end{array}
$$

Multiplying these two equations and using (6.4;8) gives

$$
p _ { 8 } b _ { 3 } ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } ) ( c _ { 2 } ^ { \prime } - c _ { 3 } ^ { \prime } ) c _ { 3 } ^ { \prime } = ( c _ { 4 } ^ { \prime } p _ { 4 } - p _ { 6 } ) ( c _ { 2 } ^ { \prime } p _ { 4 } - p _ { 7 } ) .
$$

We now compute $b _ { 2 } , b _ { 3 } , b _ { 4 }$ from (6.4;2), (6.4;3), (6.4;5). This gives

$$
b _ { 3 } = \left( - p _ { 2 } c _ { 2 } ^ { \prime } c _ { 4 } ^ { \prime } + p _ { 3 } ( c _ { 4 } ^ { \prime } + c _ { 2 } ^ { \prime } ) - p _ { 5 } \right) / \left( c _ { 3 } ^ { \prime } ( c _ { 3 } ^ { \prime } - c _ { 2 } ^ { \prime } ) ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } ) \right)
$$

and $b _ { 2 }$ as well as $b _ { 4 }$ by cyclic permutation. Comparing the last two equations leads to

$$
c _ { 4 } ^ { \prime } = \frac { p _ { 8 } p _ { 3 } c _ { 2 } ^ { \prime } - p _ { 8 } p _ { 5 } - c _ { 2 } ^ { \prime } p _ { 6 } p _ { 4 } + p _ { 6 } p _ { 7 } } { p _ { 8 } p _ { 2 } c _ { 2 } ^ { \prime } - p _ { 8 } p _ { 3 } - c _ { 2 } ^ { \prime } p _ { 4 } p _ { 4 } + p _ { 4 } p _ { 7 } } .
$$

We now choose $\gamma , c _ { 2 } ^ { \prime }$ and $c _ { 3 } ^ { \prime }$ as free parameters. Then $c _ { 4 } ^ { \prime }$ is obtained from (6.7); $b _ { 2 } , b _ { 3 } , b _ { 4 }$ from (6.6), $b _ { 1 }$ from (6.4;1), $a _ { 3 2 }$ and $a _ { \scriptscriptstyle 4 3 }$ from (6.5), $a _ { 4 2 }$ from (6.4;4), and finally $a _ { 2 1 } , a _ { 3 1 } , a _ { 4 1 }$ from (6.3).

Embedded 3rd order formula: As proposed by Cash (1979),we can append to the above formula a third order expression

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \sum _ { \iota = 1 } ^ { 4 } \widehat { b } _ { i } k _ { \iota }
$$

(thus by omitting the term $b _ { 5 } = \gamma$ )for the sake of step size control. The coefficients $\widehat { b } _ { 1 } , \ldots , \widehat { b } _ { 4 }$ are simply obtained by solving the first 4 equations of Table 6.1 (linear system). Continuous embedded 3rd order formulas can be obtained in this way too (see Theorem 6.1 of Sect.II.6)

$$
y ( x _ { 0 } + \theta h ) \approx y _ { 0 } + h \sum _ { \imath = 1 } ^ { 4 } b _ { i } ( \theta ) k _ { \imath } .
$$

The coefficients $b _ { 1 } ( \theta ) , \dots , b _ { 4 } ( \theta )$ are obtained by solving the first 4 (simplified) conditions of Table 6.1, with the right-hand sides replaced by

$$
\theta , \quad \frac { \theta ^ { 2 } } { 2 } - \gamma \theta , \quad \frac { \theta ^ { 3 } } { 3 } - \gamma \theta ^ { 2 } + \gamma ^ { 2 } \theta , \quad \frac { \theta ^ { 3 } } { 6 } - \gamma \theta ^ { 2 } + \gamma ^ { 2 } \theta ,
$$

respectively. The continuous solution obtained in this way becomes $\widehat { y } _ { 1 }$ for $\theta =$ 1 instead of the $4$ -th order solution $y _ { 1 }$ . The global continuous solution would therefore be discontinuous. In order to avoid this discontinuity, we add $b _ { 5 } ( \theta )$ and include the fifth equation from Table 6.1 with right-hand side

$$
\frac { \theta ^ { 4 } } { 4 } - \gamma \theta ^ { 3 } + \frac { 3 \gamma ^ { 2 } \theta ^ { 2 } } { 2 } - \gamma ^ { 3 } \theta .
$$

# The Stability Function

By Formula (3.3), the stability function $R ( z )$ for a DIRK method is of the form

$$
R ( z ) = \frac { P ( z ) } { ( 1 - a _ { 1 1 } z ) ( 1 - a _ { 2 2 } z ) \dots ( 1 - a _ { s s } z ) } ,
$$

because the determinant of a triangular matrix is the product of its diagonal entries. The numerator $P ( z )$ is a polynomial of degree $s$ at most. If the method is of order $p \geq s$ ，this polynomial is uniquely determined by Formula (3.18). It is simply obtained from the first terms of the power series for $( 1 - a _ { 1 1 } z ) \dots ( 1 - a _ { s s } z ) \cdot e ^ { z }$

For SDIRK methods, with $a _ { 1 1 } = \dots = a _ { s s } = \gamma$ , we obtain (see also Formula (3.18) with $q _ { \jmath } = { \left( - \gamma \right) } ^ { j } { \binom { s } { j } }$ ）

$$
P ( z ) = ( - 1 ) ^ { s } \sum _ { \jmath = 0 } ^ { s } L _ { s } ^ { ( s - j ) } \Big ( { \frac { 1 } { \gamma } } \Big ) ( \gamma z ) ^ { \jmath }
$$

with error constant

$$
C = \frac { \gamma ^ { s } ( - 1 ) ^ { s + 1 } } { s + 1 } L _ { s + 1 } ^ { ( 1 ) } \biggl ( \frac { 1 } { \gamma } \biggr )
$$

where

$$
L _ { s } ( x ) = \sum _ { j = 0 } ^ { s } ( - 1 ) ^ { j } \binom { s } { j } \frac { x ^ { j } } { j ! }
$$

is the $s$ -degree Laguerre polynomial. $L _ { s } ^ { ( k ) } ( x )$ denotes its $k$ -th derivative. Since the function (6.9) is analytic in $\mathbb { C } ^ { - }$ for $\gamma > 0$ ， $A$ -stability is equivalent to

$$
E ( y ) = Q ( i y ) Q ( - i y ) - P ( i y ) P ( - i y ) \geq 0 \qquad { \mathrm { ~ f o r ~ a l l ~ } } y _ { \mathrm { i } }
$$

(see (3.8)). This is an even polynomial of degree $2 s$ (in general) and subdegree $2 j$ where $j = [ ( p + 2 ) / 2 ]$ (see Proposition 3.4). We therefore define the polynomial $F ( x )$ by

$$
F ( y ^ { 2 } ) = E ( y ) / y ^ { 2 j } \quad j = [ ( p + 2 ) / 2 ] .
$$

and check the condition $F ( x ) \geq 0$ for $x \ge 0$ using Sturm sequences. We display the results obtained (similar to Burrage 1978) in Table 6.3.

For completeness, we give the following explicit formulas for $E ( y )$

$$
{ \begin{array} { r l } { s = 1 ; p = 1 : } & { } \\ & { E = y ^ { 2 } ( 2 \gamma - 1 ) } \\ { s = 2 ; p = 2 : } \\ & { { \phantom { s p a c e } } E = y ^ { 4 } \left( - { \frac { 1 } { 4 } } + 2 \gamma - 5 \gamma ^ { 2 } + 4 \gamma ^ { 3 } \right) = y ^ { 4 } { \left( 2 \gamma - 1 \right) } ^ { 2 } \left( \gamma - { \frac { 1 } { 4 } } \right) } \\ { s = 3 ; p = 3 : } \\ & { { \phantom { s p a c e } } E = y ^ { 4 } \left( { \frac { 1 } { 1 2 } } - \gamma + 3 \gamma ^ { 2 } - 2 \gamma ^ { 3 } \right) + y ^ { 6 } \left( - { \frac { 1 } { 3 6 } } + { \frac { \gamma } { 2 } } - { \frac { 1 3 \gamma ^ { 2 } } { 4 } } + { \frac { 2 8 \gamma ^ { 3 } } { 3 } } - 1 2 \gamma ^ { 4 } + 6 \gamma ^ { 5 } \right) } \end{array} }
$$

Table 6.3. $A$ -stability of (6.9),order $p \geq s$   

<table><tr><td>S</td><td>A -stability</td><td>A -stability and p = s +1</td></tr><tr><td>1</td><td>1/2≤γ&lt;8</td><td>1/2</td></tr><tr><td>2</td><td>1/4≤γ&lt;8</td><td>(3+√3)/6</td></tr><tr><td>3</td><td>1/3≤γ ≤1.06857902</td><td>1.06857902</td></tr><tr><td>4</td><td>0.39433757 ≤ γ ≤ 1.28057976</td><td></td></tr><tr><td>5</td><td>{0.24650519≤γ≤0.36180340 0.42078251≤γ≤0.47326839</td><td>0.47326839</td></tr><tr><td>6</td><td>0.28406464 ≤ γ ≤ 0.54090688</td><td></td></tr><tr><td>7</td><td></td><td></td></tr><tr><td>8</td><td>0.21704974 ≤ γ ≤ 0.26471425</td><td></td></tr></table>

$$
\begin{array} { r l } & { 4 ; \ p = 4 : } \\ & { E = y ^ { 6 } \left( \frac { 1 } { 7 2 } - \frac { \chi } { 3 } + \frac { 1 7 \gamma ^ { 2 } } { 6 } - \frac { 3 2 \gamma ^ { 3 } } { 3 } + 1 7 \gamma ^ { 4 } - 8 \gamma ^ { 5 } \right) } \\ & { \quad + y ^ { 8 } \left( - \frac { 1 } { 5 7 6 } + \frac { \gamma } { 1 8 } - \frac { 2 5 \gamma ^ { 2 } } { 3 6 } + \frac { 1 3 \gamma ^ { 3 } } { 3 } - \frac { 1 7 3 \gamma ^ { 4 } } { 1 2 } + \frac { 7 6 \gamma ^ { 5 } } { 3 } - 2 2 \gamma ^ { 6 } + 8 \gamma ^ { 7 } \right) . } \end{array}
$$

$A$ -stability means here that all coefficients must be non-negative.A general formula is as follows.

Lemma 6.1. The $E$ -polynomial for (6.8) with $a _ { 1 1 } = \dots = a _ { s s } = \gamma$ and $p \geq s$ satisfies

$$
\begin{array} { l } { { \displaystyle { E ( y ) = \Big ( 1 - L _ { s } \Big ( \frac { 1 } { \gamma } \Big ) ^ { 2 } \Big ) ( \gamma y ) ^ { 2 s } } } } \\ { { \mathrm { - 2 } \sum _ { \jmath = \lbrack { ( p + 2 ) / 2 } \rbrack } ^ { s - 1 } ( - 1 ) ^ { s + j } ( \gamma y ) ^ { 2 j } \int _ { 0 } ^ { 1 / \gamma } L _ { s } ( x ) L _ { s } ^ { ( 2 s + 1 - 2 \jmath ) } ( x ) d x . } }  \end{array}
$$

Proof. Inserting Formula (6.9) into the definition of $E ( y )$

$$
\begin{array} { l } { { \displaystyle E ( y ) = ( 1 + \gamma ^ { 2 } y ^ { 2 } ) ^ { s } - P ( i y ) P ( - i y ) } } \\ { { \displaystyle \qquad = ( 1 + \gamma ^ { 2 } y ^ { 2 } ) ^ { s } - \sum _ { k } \sum _ { l } L _ { s } ^ { ( s - k ) } \left( \frac 1 \gamma \right) L _ { s } ^ { ( s - l ) } \left( \frac 1 \gamma \right) ( \gamma i y ) ^ { k + l } ( - 1 ) ^ { l } } } \end{array}
$$

and using integration by parts for the verification of

$$
2 \int _ { 0 } ^ { \alpha } { \cal L } _ { s } ( x ) { \cal L } _ { s } ^ { ( 2 s + 1 - 2 j ) } ( x ) d x = ( - 1 ) ^ { s } \sum _ { k + l = 2 \atop { } } ( - 1 ) ^ { l } { \cal L } _ { s } ^ { ( s - k ) } ( x ) { \cal L } _ { s } ^ { ( s - l ) } ( x ) \Big | _ { 0 } ^ { \alpha }
$$

one obtains the result, since

$$
\sum _ { k + l = 2 j } ( - 1 ) ^ { l } L _ { s } ^ { ( s - k ) } ( 0 ) L _ { s } ^ { ( s - l ) } ( 0 ) = ( - 1 ) ^ { j } { \binom { s } { j } } .
$$

# Multiple Real-Pole Approximations with $R ( \infty ) = \mathbf { 0 }$

For methods satisfying (6.2) we have $R ( \infty ) = 0$ . Therefore the highest coefficient of $P ( z )$ in (6.9) is zero. If the order of the method is known to be $p \geq s - 1$ ，the remaining coefficients of $P ( z )$ are still uniquely determined by $\gamma$ and we have

$$
P ( z ) = ( - 1 ) ^ { s } \sum _ { j = 0 } ^ { s - 1 } L _ { s } ^ { ( s - _ { j } ) } \Bigl ( \frac { 1 } { \gamma } \Bigr ) ( \gamma z ) ^ { j }
$$

with error constant

$$
C = ( - 1 ) ^ { s } L _ { s } \Bigl ( { \frac { 1 } { \gamma } } \Bigr ) \gamma ^ { s } .
$$

The first polynomials $E ( y )$ of (6.12) are now:

$$
\begin{array} { r l } & { s = 2 , \ p = 1 ; } \\ & { \qquad E = y ^ { 2 } ( - 1 + 4 \gamma - 2 \gamma ^ { 2 } ) + y ^ { 4 } \gamma ^ { 4 } } \\ & { s = 3 , \ p = 2 ; } \\ & { \qquad E = y ^ { 4 } \left( - \frac { 1 } { 4 } + 3 \gamma - 1 2 \gamma ^ { 2 } + 1 8 \gamma ^ { 3 } - 6 \gamma ^ { 4 } \right) + y ^ { 6 } \gamma ^ { 6 } } \\ & { s = 4 , \ p = 3 ; } \\ & { E = y ^ { 4 } \left( \frac { 1 } { 1 2 } - \frac { 4 \gamma } { 3 } + 6 \gamma ^ { 2 } - 8 \gamma ^ { 3 } + 2 \gamma ^ { 4 } \right) } \\ & { \qquad + y ^ { 6 } \left( - \frac { 1 } { 3 6 } + \frac { 2 \gamma } { 3 } - 6 \gamma ^ { 2 } + \frac { 7 6 \gamma ^ { 3 } } { 3 } - 5 2 \gamma ^ { 4 } + 4 8 \gamma ^ { 5 } - 1 2 \gamma ^ { 6 } \right) + y ^ { 8 } \gamma ^ { 8 } . } \end{array}
$$

The regions of $\gamma$ for $A$ -(and hence $L - )$ stability are displayed in Table 6.4.

Table 6.4. $I$ -stability of $R ( z )$ with $P$ from (6.14), order $p \geq s - 1$   

<table><tr><td>S</td><td>L -stability</td><td>L-stab. and p = s</td></tr><tr><td>2</td><td>(2-√2)/2≤γ≤(2+√2)/2</td><td>γ =(2±√2)/2</td></tr><tr><td>3</td><td>0.18042531 ≤ γ ≤ 2.18560010</td><td>Y = 0.43586652</td></tr><tr><td>4</td><td>0.22364780 ≤ γ ≤ 0.57281606</td><td>Y = 0.57281606</td></tr><tr><td>5</td><td>0.24799464 ≤ γ ≤ 0.67604239</td><td>Y= 0.27805384</td></tr><tr><td>6</td><td>0.18391465≤ γ ≤0.33414237</td><td>Y= 0.33414237</td></tr><tr><td>7</td><td>0.20408345 ≤ γ ≤ 0.37886489</td><td></td></tr><tr><td>8</td><td>0.15665860 ≤ γ ≤ 0.23437316</td><td>Y= 0.23437316</td></tr></table>

# Choice of Method

We now determine the free parameters for method (6.3） with $s \approx 5$ and order 4. For a good choice of $\gamma$ , we have displayed in Fig. 6.2 the error constant $C$ as well as the regions for $A \cdot$ and $A ( 0 )$ -stability.

![](images/7c2fa09cf30bf2edc8c3ad36030fa0d4e13a6277a2655b66c38e9b78c911ad29.jpg)  
Fig. 6.2 Error constant and $A$ -stability domain for $s = 5 , p = 4$

This suggests that $\gamma$ between O.25 and O.29 is a good choice. The method is then $L$ -stable and the error constant is small. For various values of $\gamma$ in this range, we determined (by a nonlinear Gauss-Newton code) $c _ { 2 } ^ { \prime }$ and $c _ { 3 } ^ { \prime }$ in order to minimize the fifth-order error terms. It turned out that

$$
c _ { 2 } ^ { \prime } = 0 . 5 , \qquad c _ { 3 } ^ { \prime } = 0 . 3
$$

is close to optimal. With this we coded two different choices of $\gamma \colon \gamma = 4 / 1 5 =$ 0.2666..., which was numerically the better choice and $\gamma = 1 / 4$ , which gave, via Formulas (6.4), (6.5),(6.6) and (6.7),especially nice rational coefficients. These latter are displayed in Table 6.5. We have included a continuous solution to this method

$$
y ( x _ { 0 } + \theta h ) \approx y _ { 0 } + h \sum _ { \jmath = 1 } ^ { 5 } b _ { j } ( \theta ) k _ { \jmath } ,
$$

which is third order for $0 < \theta < 1$ and updates to the fourth order approximation $y _ { 1 }$ for $\theta \approx 1$

Table 6.5. $L$ -stable SDIRK method of order 4   

<table><tr><td></td><td></td><td>4 1 25</td><td></td><td></td></tr><tr><td></td><td>371 1360</td><td>137 2720</td><td>1 544</td><td>4</td></tr><tr><td>1</td><td></td><td>4</td><td>125</td><td>85 1-4</td></tr><tr><td></td><td></td><td></td><td>16</td><td>12</td></tr><tr><td>y1 二</td><td></td><td></td><td>125</td><td>85</td></tr><tr><td></td><td>25242524598</td><td></td><td>16</td><td>14 12</td></tr><tr><td>y 二</td><td></td><td></td><td>225</td><td>85 0</td></tr><tr><td></td><td></td><td></td><td>32 12</td><td></td></tr><tr><td>err 二</td><td>3</td><td>49148171627132</td><td>2 0</td><td>4</td></tr></table>

$$
\begin{array} { l } { { b _ { 1 } ( \theta ) = \displaystyle { \frac { 1 1 } { 3 } } \theta - \frac { 4 6 3 } { 7 2 } \theta ^ { 2 } + \frac { 2 1 7 } { 3 6 } \theta ^ { 3 } - \frac { 2 0 } { 9 } \theta ^ { 4 } } } \\ { { b _ { 2 } ( \theta ) = \displaystyle { \frac { 1 1 } { 2 } } \theta - \frac { 3 8 5 } { 1 6 } \theta ^ { 2 } + \frac { 6 6 1 } { 2 4 } \theta ^ { 3 } - 1 0 \theta ^ { 4 } } } \\ { { b _ { 3 } ( \theta ) = \displaystyle { - \frac { 1 2 5 } { 1 8 } } \theta + \frac { 2 0 1 2 5 } { 4 3 2 } \theta ^ { 2 } - \frac { 8 8 7 5 } { 2 1 6 } \theta ^ { 3 } + \frac { 2 5 0 } { 2 7 } \theta ^ { 4 } } } \\ { { b _ { 4 } ( \theta ) = \displaystyle { - \frac { 8 5 } { 4 } } \theta ^ { 2 } + \frac { 8 5 } { 6 } \theta ^ { 3 } } } \\ { { b _ { 5 } ( \theta ) = \displaystyle { - \frac { 1 1 } { 9 } } \theta + \frac { 5 5 7 } { 1 0 8 } \theta ^ { 2 } - \frac { 3 5 9 } { 5 4 } \theta ^ { 3 } + \frac { 8 0 } { 2 7 } \theta ^ { 4 } . } } \end{array}
$$

# Exercises

1.(Crouzeix & Raviart 1980). Compute the SDIRK methods (Table 6.1) for $s =$ 3, $p = 4$ . Obtain also (for $s = 2 , p = 3$ ） once again the method of Table 7.2, Sect. I1.7.

Result. The last order condition is in both cases just a polynomial in $\gamma$ . Among the different solutions, the following presents an $A$ -stable scheme:

$$
\begin{array} { l } { \gamma = \displaystyle \frac { 1 } { \sqrt { 3 } } \cos \left( \frac { \pi } { 1 8 } \right) + \frac { 1 } { 2 } } \\ { \delta = \displaystyle \frac { 1 } { 6 ( 2 \gamma - 1 ) ^ { 2 } } . } \end{array}
$$

2． Verify all details of Tables 6.1 and 6.2.

3. The four cases of $A$ -stable SDIRK methods of order $p = s + 1$ indicated in Table 6.3 (right) are the only ones existing. This fact has not yet been rigorously proved, because the “proof" given in Wanner, Hairer & Nprsett (1978) uses an asymptotic formula without error estimation. Do better.

4. Cooper & Sayfy (1979) have derived many DIRK (which they call “semiexplicit") methods of high order. Their main aim was to minimize the number of implicit stages and not to maximize stability. One of their methods is

<table><tr><td>6-√6 10</td><td colspan="4">6-√6 10</td></tr><tr><td>6+9√6</td><td>-6+5√6</td><td>6-√6</td><td></td><td></td></tr><tr><td>35</td><td>14 888+607√6</td><td>10 126-161√6</td><td>6-√6</td><td></td></tr><tr><td>1</td><td>2850</td><td>1425</td><td>10</td><td></td></tr><tr><td>4-6 10</td><td>3153-3082√6 14250</td><td>3213+1148√6 28500</td><td>-267+88√6 500</td><td>6-√6 10</td></tr><tr><td>4+√6</td><td>-32583+14638√6</td><td>-17199+364√6</td><td>1329-544√6</td><td>-96+131√6 6-√6</td></tr><tr><td>10</td><td>71250</td><td>142500</td><td>2500</td><td>625 10</td></tr><tr><td>1</td><td>： 0 市</td><td>0</td><td>小</td><td>16-√6 16+√6 0</td></tr></table>

Show that it is of order 5 and $A$ -stable, but not $L$ -stable.

5. It can be seen in Table 6.4 that for $s = 2 , 4 , 6$ ,and 8 the $L$ -stability superconvergence point coincides with the right end of the $A$ -stability interval. Explain this with the help of order star theory (Fig. 6.3.a).

Further, for $s \simeq 7$ ，a superconvergence point is given by $\gamma = 0 . 2 0 4 0 6 6 9 3$ ， which misses the $A$ -stability interval given there by less than $2 \cdot 1 0 ^ { - 5 }$ . Should the above argument also apply here and must there be a computation error somewhere? Study the corresponding order star to show that this is not the case (Fig. 6.3.b).

![](images/35ab1256c9ed7df36e876e4266cd5919f0f773838703d57c284f8b3560021513.jpg)  
Fig. 6.3.a. Multiple pole order star $s = 8$ ，Y= 0.23437316

![](images/d7e02e84f33d2abbc059cc3c03d392d27627cf1268348f4a2f045ef158fb0b7b.jpg)  
Fig. 6.3.b. Multiple pole order star

When the functions $\varphi$ are non-linear, implicit equations can in general be solved only by iteration. This is a severe drawback, as it adds to the problem of stability,that of convergence of the iterative process.An alternative,which avoids this difficulty, is (H.H. Rosenbrock 1962/63)

... is discussed in this section. Among the methods which already give satisfactory results for stiff equations, Rosenbrock methods are the easiest to program. We shall describe their theory in this section, which will lead us to our first “stiff code. Rosenbrock methods belong to a large class of methods which try to avoid nonlinear systems and replace them by a sequence of linear systems. We therefore call these methods linearly implicit Runge-Kutta methods. In the literature such methods are often called “semi-implicit” (or was it “semi-explicit"?), or “generalized" or “modified” or “adaptive” or “additive" Runge-Kutta methods.

# Derivation of the Method

We start, say, with a diagonally implicit Runge-Kutta method

$$
\begin{array} { l l } { { \displaystyle k _ { \imath } = h f \biggl ( y _ { 0 } + \sum _ { j = 1 } ^ { \imath - 1 } a _ { \imath j } k _ { \jmath } + a _ { \imath \imath } k _ { \imath } \biggr ) \quad } } & { { \displaystyle i = 1 , \ldots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { s } b _ { \imath } k _ { \imath } } } & { { \displaystyle } } \end{array}
$$

applied to the autonomous differential equation

$$
y ^ { \prime } = f ( y ) .
$$

The main idea is to linearize Formula (7.1). This yields

$$
\begin{array} { l } { { \displaystyle k _ { \imath } = h f ( g _ { i } ) + h f ^ { \prime } ( g _ { \imath } ) a _ { i \imath } k _ { \imath } } } \\ { { \displaystyle g _ { i } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { i - 1 } a _ { \imath j } k _ { \jmath } , } } \end{array}
$$

and can be interpreted as the application of one Newton iteration to each stage in （7.1） with starting values $k _ { i } ^ { ( 0 ) } = 0$ . Instead of continuing the iterations until convergence, we consider (7.3) as a new class of methods and investigate anew its order and stability properties.

Important computational advantage is obtained by replacing the Jacobians $f ^ { \prime } ( g _ { \imath } )$ by $J = f ^ { \prime } ( y _ { 0 } )$ , so that the method requires its calculation only once (Calahan 1968). Many methods of this type and much numerical experience with them have been obtained by van der Houwen (1973), Cash (1976) and Ngrsett (1975).

We gain further freedom by introducing additional linear combinations of the terms $J k _ { \ j }$ into (7.3)(Ngrsett & Wolfbrandt 1979,Kaps & Rentrop 1979). We then arrive at the following class of methods:

Definition 7.1. An $s$ -stage Rosenbrock method is given by the formulas

$$
\begin{array} { r l } & { k _ { \iota } = h f \biggl ( y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { \iota - 1 } \alpha _ { \iota _ { j } } k _ { j } \biggr ) + h J \displaystyle \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \iota _ { j } } k _ { \jmath } , \qquad i = 1 , \dots , s } \\ & { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { \jmath } k _ { \jmath } } \end{array}
$$

where $\alpha _ { \iota _ { 2 } } , \gamma _ { \iota _ { 2 } } , b _ { \iota }$ are the determining coeficients and $J = f ^ { \prime } ( y _ { 0 } )$

Each stage of this method consists of a system of linear equations with unknowns $k _ { \imath }$ and with matrix $I - h \gamma _ { \imath \imath } J$ . Of special interest are methods for which $\gamma _ { 1 1 } = . . . = \gamma _ { s s } = \gamma$ , so that we need only one LU-decomposition per step.

Non-autonomous problems. The equation

$$
y ^ { \prime } = f ( x , y )
$$

can be converted to autonomous form by adding $x ^ { \prime } = 1$ . If method (7.4) is applied to the augmented system, the components corresponding to the $x$ -variable can be computed explicitly and we arrive at

$$
\begin{array} { l } { { \displaystyle k _ { \scriptscriptstyle 3 } = h f \bigg ( x _ { 0 } + \alpha _ { \scriptscriptstyle 3 } h , y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \scriptscriptstyle 3 \jmath } k _ { \jmath } \bigg ) + \gamma _ { \scriptscriptstyle 3 } h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) + h \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { \imath \jmath } k _ { \jmath } } } \\ { { \displaystyle y _ { \scriptscriptstyle 1 } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } k _ { \jmath } , ~ } } \end{array}
$$

where the additional coeficients are given by

$$
\alpha _ { \ i } = \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } , \qquad \gamma _ { \imath } = \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { \imath \jmath } .
$$

Implicit differential equations. Suppose the problem is of the form

$$
M y ^ { \prime } = f ( x , y )
$$

where $M$ is a constant matrix (nonsingular for the moment). If we formally multiply (7.2b) with $M ^ { - 1 }$ , apply method (7.4a),and then multiply the resulting formula

with $M$ , we obtain

$$
\begin{array} { c } { { M k _ { \iota } = h f \displaystyle \bigg ( x _ { 0 } + \alpha _ { \iota } h , y _ { 0 } + \sum _ { j = 1 } ^ { i - 1 } \alpha _ { \iota j } k _ { \iota } \bigg ) + \gamma _ { \iota } h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) + h \displaystyle \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \sum _ { j = 1 } ^ { \iota } \gamma _ { \iota j } k _ { j } } } \\ { { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } k _ { j } . } } \end{array}
$$

An advantage of this formulation is that the inversion of $M$ is avoided and that possible band-structures of the matrices $M$ and $\partial f / \partial y$ are preserved.

# Order Conditions

Conditions on the free parameters which ensure that the method is of order $p$ ,i.e., the local error satisfies

$$
y ( x _ { 0 } + h ) - y _ { 1 } = \mathcal { O } \bigl ( h ^ { p + 1 } \bigr ) , \qquad 
$$

can be obtained either by straightforward differentiation or by the use of the theorems on $B$ -series (Sect. II.12). We follow here the first approach, since it requires only the knowledge of Sect. II.2. The second possibility is sketched in Exercise 2.

As in Sect.II.2, we write the system (7.2) in tensor notation and Method (7.4) as1

$$
\begin{array} { l } { { \displaystyle k _ { \jmath } ^ { J } = h f ^ { J } ( g _ { \jmath } ) + h \sum _ { K } f _ { K } ^ { J } ( y _ { 0 } ) \sum _ { k } \gamma _ { \jmath k } k _ { k } ^ { K } } } \\ { { \displaystyle g _ { \imath } ^ { J } = y _ { 0 } ^ { J } + \sum _ { \jmath } \alpha _ { \imath \jmath } k _ { \jmath } ^ { J } , } } \\ { { \displaystyle y _ { 1 } ^ { J } = y _ { 0 } ^ { J } + \sum _ { \jmath } b _ { \jmath } k _ { \jmath } ^ { J } . } } \end{array}
$$

Again,we use Leibniz's rule (cf. (I1.2.4))

$$
\left. ( k _ { \ j } ^ { J } ) ^ { ( q ) } \right| _ { h = 0 } = q \big ( f ^ { J } ( g _ { \ j } ) \big ) ^ { ( q - 1 ) } \big | _ { h = 0 } + q \sum _ { K } f _ { K } ^ { J } ( y _ { 0 } ) \sum _ { k } \gamma _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( q - 1 ) } \big | _ { h = 0 }
$$

and have from the chain rule(cf. Sect.II.2,(2.6;1),(2.6;2))

$$
\begin{array} { l } { { \displaystyle \left( f ^ { J } ( g _ { \jmath } ) \right) ^ { \prime } = \sum _ { K } f _ { K } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime } } } \\ { { \displaystyle \left( f ^ { J } ( g _ { \jmath } ) \right) ^ { \prime \prime } = \sum _ { K , L } f _ { K L } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime } \cdot ( g _ { \jmath } ^ { L } ) ^ { \prime } + \sum _ { K } f _ { K } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime \prime } } } \end{array}
$$

etc.Inserting this into (7.6) we obtain recursively

$$
\begin{array} { l } { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 0 ) } | _ { i = 0 } = 0 } } \\ { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 1 ) } | _ { k = 0 } = f ^ { J } } } \\ { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 2 ) } | _ { k = 0 } = 2 \sum _ { K } ^ { J } f _ { K } ^ { J } f ^ { K } \sum _ { k } \alpha _ { j k } + 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } \gamma _ { j k } } } \\ { { \displaystyle ~ = 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } ^ { K } \langle \alpha _ { k } + \gamma _ { j k } \rangle } } \\ { { \displaystyle \big ( k _ { j } ^ { J } \rangle ^ { ( 3 ) } \big ) | _ { k = 0 } = 3 \sum _ { K , L } ^ { J } f _ { K L } ^ { J } f ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { j k } \alpha _ { j l } } } \\ { { \displaystyle ~ + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } ^ { K } \big ( \alpha _ { k } + \gamma _ { j k } \big ) \big ( \alpha _ { k l } + \gamma _ { k k } \big ) } } \end{array}
$$

etc. All elementary differentials are evaluated at $y _ { 0 }$ . Comparing the derivatives of the numerical solution $( q \ge 1 )$

$$
( y _ { 1 } ^ { J } ) ^ { ( q ) } | _ { h = 0 } = \sum _ { j } b _ { \jmath } ( k _ { \jmath } ^ { J } ) ^ { ( q ) } | _ { h = 0 }
$$

with those of the true solution (Sect. I.2, Formula (2.7;1), (2.7;2), (2.7;3)), we arrive at the following conditions for order three:

$$
\begin{array} { c c c c } { { \cdot _ { \jmath } } } & { { } } & { { } } & { { \sum b _ { \jmath } = 1 } } \\ { { } } & { { } } & { { } } & { { \sum b _ { \jmath } ( \alpha _ { \jmath k } + \gamma _ { \jmath k } ) = { \frac { 1 } { 2 } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \iota _ { \mathcal { N } _ { \jmath } ^ { l } } } } & { { } } & { { } } & { { \sum b _ { \jmath } \alpha _ { \jmath k } \alpha _ { \jmath l } = { \frac { 1 } { 3 } } } } \\ { { } } & { { } } & { { } } & { { \sum b _ { \jmath } ( \alpha _ { \jmath k } + \gamma _ { \jmath k } ) ( \alpha _ { k l } + \gamma _ { k l } ) = { \frac { 1 } { 6 } } . } } \end{array}
$$

The only difference with the order conditions for Runge-Kutta methods is that at singly-branched vertices of the corresponding trees $\alpha _ { \ j k }$ is replaced by $\alpha _ { \ j k } + \gamma _ { \ j k } .$ In order to arrive at a general result, the formulas obtained motivate the following definition:

Definition 7.2. Let $t$ be a labelled tre of order $q$ with root $j$ ; we denote by

$$
\Phi _ { j } ( t ) = \sum _ { k , l , \dots } \varphi _ { \jmath , k , l , \dots }
$$

the sum over the remaining $q - 1$ indices $k , l , \ldots$ etc. The summand $\varphi _ { \ j , k , l , \dots }$ is a product of $q - 1$ factors,which are

$\alpha _ { k l } + \gamma _ { k l }$ if $l$ is the only son of $k$ ；   
αkl if $l$ is a son of $k$ and $k$ has at least two sons.

Using the recursive representation of trees (Def.I.2.12) we have $\Phi _ { \jmath } ( \tau ) = 1$ for the only tree of order 1 and,as in (I1.2.19),

$$
\Phi _ { j } ( t ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { k _ { 1 } , \dots , k _ { m } } \alpha _ { _ { j k _ { 1 } } } \dots \alpha _ { _ { j k _ { m } } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \dots \Phi _ { k _ { m } } ( t _ { m } ) } & { \mathrm { i f } t = [ t _ { 1 } , \dots , t _ { m } ] , } \\ { \displaystyle \sum _ { k } ( \alpha _ { _ { j k } } + \gamma _ { j k } ) \Phi _ { k } ( t _ { 1 } ) } & { \mathrm { i f } t = [ t _ { 1 } ] . } \end{array} \right.
$$

Theorem 7.3. The derivatives of $k _ { \jmath } ^ { J }$ , given by (7.4), satisfy

$$
( k _ { \jmath } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = \sum _ { t \in L T _ { q } } \gamma ( t ) \Phi _ { j } ( t ) F ^ { J } ( t ) ( y _ { 0 } )
$$

and the numerical solution $y _ { 1 } ^ { J }$ satisfies

$$
( y _ { 1 } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = \sum _ { t \in L T _ { q } } \gamma ( t ) \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) F ^ { J } ( t ) ( y _ { 0 } ) ,
$$

where $F ^ { J } ( t )$ are the elementary differentials (Definition II.2.3).

Proof. Because of (7.8) we only have to prove the first formula. This is done by induction on $q$ and follows exactly the lines of the proof of Theorem I1.2.11. We use (7.6), replace the expression $f ^ { J } ( g _ { _ { J } } ) ^ { ( q - 1 ) }$ by Faa di Bruno's formula (Lemma I.2.8), use

$$
( g _ { j } ^ { K } ) ^ { ( \delta ) } = \sum _ { k } \alpha _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( \delta ) }
$$

for the derivatives of $g _ { \jmath }$ and insert the induction hypothesis $( 7 . 7 ; \delta )$ with $\delta \leq q - 1$ This gives

$$
\begin{array} { l } { { \displaystyle \left( k _ { j } ^ { J } \right) ^ { ( q ) } \Big \} _ { h = 0 } = q \displaystyle \sum _ { u \in L S _ { q } } \displaystyle \sum _ { t _ { 1 } \in L T _ { \delta _ { 1 } } } \displaystyle \sum _ { \substack { t _ { m } \in L T _ { \delta _ { m } } } } \gamma ( t _ { 1 } ) \ldots \gamma ( t _ { m } ) } } \\ { ~ \cdot \displaystyle \sum _ { k _ { 1 } } \alpha _ { \jmath k _ { 1 } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \ldots \displaystyle \sum _ { k _ { m } } \alpha _ { \jmath k _ { m } } \Phi _ { k _ { m } } ( t _ { m } ) }  \\ { ~ \cdot \displaystyle \sum _ { \substack { k _ { 1 } , \ldots , K _ { m } } } f _ { K _ { 1 } \dots K _ { m } } ^ { J } ( \jmath _ { 0 } ) F ^ { K _ { 1 } } ( t _ { 1 } ) ( \jmath _ { 0 } ) \ldots F ^ { K _ { m } } ( t _ { m } ) ( \jmath _ { 0 } ) }  \\ { ~ + q \displaystyle \sum _ { t _ { 1 } \in L T _ { \delta ^ { - 1 } } } \gamma ( t _ { 1 } ) \sum _ { k } \gamma _ { \jmath k } \Phi _ { k } ( t _ { 1 } ) \sum _ { K } f _ { K } ^ { \gamma } ( \jmath _ { 0 } ) F ^ { K } ( t _ { 1 } ) ( \jmath _ { 0 } ) . } \end{array}
$$

The one-to-one correspondence between the summation set $\{ ( u , t _ { 1 } , \dots , t _ { m } ) | u \in L S _ { q }$ ， $t _ { j } \in L T _ { \delta _ { j } } \}$ and $L T _ { q }$ together with the recursion formulas (7.9), (II.2.17), (II.2.i8) now yields the result. □

Comparing Theorems 7.3 and II.2.6 we obtain:

Table 7.1. Trees and order conditions up to order 5   

<table><tr><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>t）</td><td rowspan=1 colspan=1>Pt()</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>可</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>t21</td><td rowspan=1 colspan=1>”</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>MBjk</td><td rowspan=1 colspan=1>1/2- γ</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>t31t32</td><td rowspan=1 colspan=1>兴</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>∑kQkajlMk,Bkβkl</td><td rowspan=1 colspan=1>1/31/6-γ+γ²</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>t41t42t43t44</td><td rowspan=1 colspan=1>k  m山X宝</td><td rowspan=1 colspan=1>481224</td><td rowspan=1 colspan=1>∑k,,makaj1am∑klmajkβklagm∑k,L,mBjkakakm∑k,,mBkβkiBIm</td><td rowspan=1 colspan=1>1/41/8-γ/31/12- γ/31/24-γ/2+3γ²/2-γ3</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>t51东县t52t53t54t55t5657t58t59</td><td rowspan=1 colspan=1>东县3</td><td rowspan=1 colspan=1>5东县10153020204060120</td><td rowspan=1 colspan=1>ΣajkaJlαjmα Jp∑ajkβkiα jmαJp∑αJkaklαkmαjpMaJkβkiβImαjp∑aJkβkiajmβmp∑βjkaklQkmQkp∑Bkakiβimakp∑βkβkiaimalp∑βJkβkiβimβmp</td><td rowspan=1 colspan=1>1/51/10- ~/41/151/30 - γ/4+ γ²/31/20- γ/4+ γ²/31/20- γ/41/40-5γ/24+ γ²/31/60- γ/6+γ²/31/120-γ/6+γ²-2γ³+γ4</td></tr></table>

# Theorem 7.4. A Rosenbrock method (7.4) with $J = f ^ { \prime } ( y _ { 0 } )$ is of order $p$ if

$$
\sum _ { \ j } b _ { \ j } \Phi _ { \ j } ( t ) = \frac { 1 } { \gamma ( t ) } \qquad f o r \quad \varrho ( t ) \leq p .
$$

The expressions $\Phi _ { j } ( t )$ simplify, if we introduce the abbreviation

$$
\beta _ { \imath \jmath } = \alpha _ { \imath j } + \gamma _ { \imath j } .
$$

The order conditions (7.11) for all trees up to order 5 are given in Table 7.1.

A further simplification of the order conditions (7.11) is possible if

$$
\gamma _ { i i } = \gamma \qquad { \mathrm { f o r ~ a l l } } i
$$

(It is unfortunate that in the current literature the letter $\gamma$ is used for the parameter in (7.4) as well as for $\gamma ( t )$ in (7.11) and we hope that no confusion will arise). In the same way as for DIRK methods, the summations in the expressions for $\Phi _ { j } ( t )$

in the 5th column of Table 7.1 again contain more terms than the corresponding ex-pressions for explicit Runge-Kutta methods, since the matrix $\gamma _ { \imath \jmath }$ (and hence $\beta _ { i j } )$ contains non-zero elements in the diagonal. The difference is that here these diagonal $\gamma$ appear only for singly-branched vertices (see Definition 7.2). Therefore the procedure explained in Sect.IV.6 (see Formulas (6.1') and (6.1") must be slightly modified and leads to order conditions of the form

$$
\sum _ { j } ^ { } { } ^ { b _ { j } } \Phi _ { j } ( t ) = p _ { t } ( \gamma )
$$

where the polynomials $p _ { t } ( \gamma )$ are listed in the last column of Table 7.1.

# The Stability Function

If we apply Method (7.4） to the test equation $y ^ { \prime } = \lambda y$ and if we assume $J =$ $f \prime ( y _ { 0 } ) = \lambda$ then the numerical solution becomes $y _ { 1 } = R ( h \lambda ) y _ { 0 }$ with

$$
R ( z ) = 1 + z b ^ { T } ( I - z B ) ^ { - 1 } \mathbb { 1 }
$$

where we have used the notation $b ^ { T } = \left( b _ { 1 } , \ldots , b _ { s } \right)$ and $B = ( \beta _ { i j } ) _ { \imath , j = 1 } ^ { s }$ . Since $B$ is alower triangular matrix, the stability function (7.14) is equal to that of a DIRKmethod with RK-matrix $B$ . Properties of such stability functions have already been investigated in Sect.IV.6.

# Construction of Methods of Order 4

In order to construct 4-stage Rosenbrock methods of order 4 we list, for convenience,the whole set of order conditions (c.f. Table 7.1.).

$$
\begin{array} { r l r l } & { \ddots } & & { \hat { b } _ { 1 } + \hat { b } _ { 2 } + \hat { b } _ { 3 } + \hat { b } _ { 4 } = 1 } \\ & { \Biggl . \hfill } & & { \Biggl . \int } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 2 } - \gamma = \mathcal { P } _ { 2 1 } ( \gamma ) } \\ & { \times } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 2 } - \gamma = \mathcal { P } _ { 2 1 } ( \gamma ) } \\ & { \searrow } & & { \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } ( 3 4 \partial _ { 4 } \partial _ { 2 } ^ { ( 0 ) } - \partial _ { 4 } \partial _ { 3 } ^ { ( 0 ) } ) = \frac { 1 } { 2 0 } - \gamma + \gamma ^ { 2 } = \mathcal { P } _ { 3 2 } ( \gamma ) } \\ & { \ddots } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 4 } } \\ & { \searrow } & & { \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \alpha _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } \alpha _ { 4 } ( \alpha _ { 4 } \partial _ { 2 } ^ { ( 0 ) } + \alpha _ { 4 } \partial _ { 3 } ^ { ( 0 ) } ) = \frac { 1 } { 8 } - \frac { \gamma } { 3 } - \gamma = \mathcal { P } _ { 4 2 } ( \gamma ) } \\ & {  \times } & &  \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \alpha _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } ( 3 \alpha _ { 4 } ^ { ( 0 ) } \alpha _ { 2 } ^ { ( 0 ) } + \beta _ { 3 } \gamma \alpha _ { 3 }  \end{array}
$$

Here we have used the abbreviations

$$
\alpha _ { i } = \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } , \qquad \beta _ { i } ^ { \prime } = \sum _ { \jmath = 1 } ^ { i - 1 } \beta _ { \imath \jmath } .
$$

For the sake of step size control we also look for an embedded formula (Wolfbrandt 1977,Kaps & Rentrop 1979)

$$
\widehat { y } _ { 1 } = y _ { 0 } + \sum _ { j = 1 } ^ { s } \widehat { b } _ { \jmath } k _ { j }
$$

which uses the same $k _ { j }$ -values as (7.4), but has different weights. This method should have_order 3,i.e.,the four conditions (7.15a)-(7.15d) should be satisfied also for the $\widehat { b } _ { \iota }$ . These equations constitute the linear system

$$
\left( { \begin{array} { c c c c } { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { \beta _ { 2 } ^ { \prime } } & { \beta _ { 3 } ^ { \prime } } & { \beta _ { 4 } ^ { \prime } } \\ { 0 } & { \alpha _ { 2 } ^ { 2 } } & { \alpha _ { 3 } ^ { 2 } } & { \alpha _ { 4 } ^ { 2 } } \\ { 0 } & { 0 } & { \beta _ { 3 2 } \beta _ { 2 } ^ { \prime } } & { \sum ^ { \prime } \beta _ { 4 j } \beta _ { j } ^ { \prime } } \end{array} } \right) { \left( \begin{array} { c } { { \widehat { b } _ { 1 } } } \\ { { \widehat { b } _ { 2 } } } \\ { { \widehat { b } _ { 3 } } } \\ { { \widehat { b } _ { 4 } } } \end{array} \right) } = \left( { \begin{array} { c } { 1 } \\ { 1 / 2 - \gamma } \\ { 1 / 3 } \\ { 1 / 6 - \gamma + \gamma ^ { 2 } } \end{array} } \right) .
$$

Whenever the matrix in (7.18) is regular, uniqueness of the solutions of the linear system implies $\widehat { b } _ { \iota } = b _ { i } \ ( i = 1 , \dots , 4 )$ and the approximation $\widehat { y } _ { 1 }$ cannot be used for step size control. We therefore have to require that the matrix (7.18) be singular, i.e.,

$$
( \beta _ { 2 } ^ { \prime } \alpha _ { 4 } ^ { 2 } - \beta _ { 4 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) \beta _ { 3 2 } \beta _ { 2 } ^ { \prime } = ( \beta _ { 2 } ^ { \prime } \alpha _ { 3 } ^ { 2 } - \beta _ { 3 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) \sum _ { j = 2 } ^ { 3 } \beta _ { 4 j } \beta _ { j } ^ { \prime } .
$$

This condition guarantees the existence of a 3rd order embedded method (7.17), whenever (7.15) possesses a solution.The computation of the coefficients $\sigma _ { \imath \jmath } ,$ $\beta _ { i _ { 1 } } , \gamma , b _ { \iota }$ satisfying (7.15),(7.16) and (7.19) is now done in the following steps:

Step 1. Choose $\gamma > 0$ such that the stability function (7.14) has desirable stability properties (c.f. Table 6.3).

Step 2. Choose $\alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 }$ and $b _ { 1 } , b _ { 2 } , b _ { 3 } , b _ { 4 }$ in such a way that the three conditions (7.15a),(7.15c), (7.15e) are fulfilled. One obviously has four degrees of freedom in this choice. Observe that the $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { \alpha } _ { \imath } \right)$ need not be the coeficients of a standard quadrature formula, since $\sum b _ { \imath } \alpha _ { \imath } = 1 / 2$ need not be satisfied.

Step 3. Take $\beta _ { 4 3 }$ as a free parameter and compute $\beta _ { 3 2 } \beta _ { 2 } ^ { \prime }$ from (7.15h)， then $\left( \beta _ { 4 2 } \beta _ { 2 } ^ { \prime } + \beta _ { 4 3 } \beta _ { 3 } ^ { \prime } \right)$ from(7.15d). These expressions, inserted into (7.19) yield a second relation between $\beta _ { 2 } ^ { \prime } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ (the first one is (7.15b)). Eliminating $\left( b _ { 4 } \beta _ { 4 2 } + \right.$ $b _ { 3 } \beta _ { 3 2 } )$ from (7.15d) and (7.15g) gives

$$
b _ { 4 } \beta _ { 4 3 } ( \beta _ { 2 } ^ { \prime } \alpha _ { 3 } ^ { 2 } - \beta _ { 3 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) = \beta _ { 2 } ^ { \prime } p _ { 4 3 } ( \gamma ) - \alpha _ { 2 } ^ { 2 } p _ { 3 2 } ( \gamma ) ,
$$

a third linear relation for $\beta _ { 2 } ^ { \prime } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ . The resulting linear system is regular if $b _ { 4 } \beta _ { 4 3 } \alpha _ { 2 } \gamma ( 3 \gamma - 1 ) \neq 0$

Step 4. Once the $\beta _ { i } ^ { \prime }$ are known we can find $\beta _ { 3 2 }$ and $\beta _ { 4 2 }$ from the values of $\beta _ { 3 2 } \beta _ { 2 } ^ { \prime }$ ， $\left( \beta _ { 4 2 } \beta _ { 2 } ^ { \prime } + \beta _ { 4 3 } \beta _ { 3 } ^ { \prime } \right)$ obtained in Step 3.

Step 5. Choose $\alpha _ { 3 2 } , \alpha _ { 4 2 } , \alpha _ { 4 3 }$ according to (7.15f). One has two degrees of freedom to do this. Finally, the values $\alpha _ { \imath } , \beta _ { \imath } ^ { \prime }$ yield $\alpha _ { \imath 1 } , \beta _ { \imath 1 }$ via condition (7.16).

Table 7.2 Rosenbrock methods of order 4   

<table><tr><td rowspan=1 colspan=1>method</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>parameter choices</td><td rowspan=1 colspan=1>A(a)-stable</td><td rowspan=1 colspan=1>|R(00）</td></tr><tr><td rowspan=1 colspan=1>GRK4A(Kaps-Rentrop 79)GRK4T(Kaps-Rentrop 79)Shampine (1982)Veldhuizen (1984)Veldhuizen (1984)L-stable method</td><td rowspan=1 colspan=1>0.3950.2310.50.2257080.50.572816</td><td rowspan=1 colspan=1>α2 = 0.438,α3 = 0.87b4 = 0.25α2=2γ，(7.22),b=0α2=2γ,(7.22),b3=0α2 =2γ，(7.22),b3=0α2 =2γ,α3=0.5,b3=0α2 =2γ,(7.22),b3 =0</td><td rowspan=1 colspan=1>π/289.3°π/289.5°π/2π/2</td><td rowspan=1 colspan=1>0.9950.4541/30.241/30</td></tr></table>

Most of the popular Rosenbrock methods are special cases of this construction (see Table 7.2). Usually the remaining free parameters are chosen as follows: if we require

$$
\alpha _ { 4 3 } = 0 , \qquad \alpha _ { 4 2 } = \alpha _ { 3 2 } \quad \mathrm { a n d } \quad \alpha _ { 4 1 } = \alpha _ { 3 1 }
$$

then the argument of $f$ in （7.4） is the same for $i = 3$ and $i = 4$ .Hence,the number of function evaluations is reduced by one. Further free parameters can be determined so that several order conditions of order five are satisfied. Multiplying the condition (7.15g) with $\alpha _ { 2 }$ and subtracting it from the order condition for the tree $t _ { 5 6 }$ yields

$$
b _ { 4 } \beta _ { 4 3 } \alpha _ { 3 } ^ { 2 } ( \alpha _ { 3 } - \alpha _ { 2 } ) = p _ { 5 6 } ( \gamma ) - \alpha _ { 2 } p _ { 4 3 } ( \gamma ) .
$$

This determines $\beta _ { 4 3 }$ ．The order condition for $t _ { 5 1 }$ can also easily be fulfilled in Step 2. If $\alpha _ { 3 } = \alpha _ { 4 }$ (see (7.20) this leads to the restriction

$$
\alpha _ { 3 } = \frac { 1 / 5 - \alpha _ { 2 } / 4 } { 1 / 4 - \alpha _ { 2 } / 3 } .
$$

In Table 7.2 we collect some well-known methods. All of them satisfy (7.20) and (7.21） (Only exception: the second method of van Veldhuizen for $\gamma = 0 . 5$ has $\beta _ { 4 3 } = 0$ instead of (7.21)). The definition of the remaining free parameters is given in the first two columns. The last columns indicate some properties of the stability function.

# Higher Order Methods

As for explicit Runge-Kutta methods the construction of higher order methods is facilitated by the use of simplifying assumptions. First, the condition

$$
\sum _ { \ i = \ i } ^ { s } b _ { \ i } \beta _ { \ i \jmath } = b _ { \jmath } ( 1 - \alpha _ { \jmath } ) , \qquad \ i = 1 , \dots , s
$$

plays a role similar to that of (II.1.12) for explicit Runge-Kutta methods. It implies that the order condition of the left-hand tree in Fig.7.1 is a consequence of the two on the right-hand side. A difference to Runge-Kutta methods is that here the vertex directly above the root has to be multiply-branched.

The second typeofsimplifing asumptionis (with $\begin{array} { r } { \beta _ { k } = \sum _ { l = 1 } ^ { k } \beta _ { k l } ) } \end{array}$

$$
\sum _ { k = 1 } ^ { \jmath - 1 } \alpha _ { \jmath k } \beta _ { k } = \frac { \alpha _ { \jmath } ^ { 2 } } { 2 } , \qquad j = 2 , \ldots , s .
$$

It has an effect similar to that of (II.5.7). As a consequence of (7.24) the order conditions of the two trees in Fig.7.2 are equivalent. Again the vertex marked by an arrow has to be multiply-branched.

The use of the above simplifying assumptions has been exploited by Kaps & Wanner (1981） for their construction of methods up to order 6. Still higher order methods would need generalizations of the above simplifying assumptions (in analogy to $C ( \eta )$ and $D ( \zeta )$ of Sect.I1.7).

![](images/24e1ac3dd4d2f0e54838dab6227c35443a00064ba2728ee38a2f2e5f50dbad9c.jpg)  
Fig. 7.1. Reduction with (7.23)

![](images/6f67bcddd10b07db4518f9c97ea88e439631c8f64308c5af0ef70c16e4c1d75f.jpg)  
Fig. 7.2. Reduction with (7.24)

# Implementation of Rosenbrock-Type Methods

A direct implementation of (7.4) requires,at each stage, the solution of a linear system with the matrix $I - h \gamma _ { \imath \imath } J$ and also the matrix-vector multiplication $J$ $\sum \gamma _ { \imath \jmath } k _ { \jmath }$ . The latter can be avoided by the introduction of the new variables

$$
u _ { \ i \ i } = \sum _ { \jmath = 1 } ^ { \ i } \gamma _ { \imath \jmath } k _ { \jmath } , \qquad i = 1 , \ldots , s .
$$

If $\gamma _ { \imath \imath } \neq 0$ for all $i$ , the matrix $\boldsymbol { \Gamma } = ( \gamma _ { \imath \jmath } )$ is invertible and the $k _ { \imath }$ can be recovered from the $u _ { \iota }$ ：

$$
k _ { \ i } = \frac { 1 } { \gamma _ { \ i \ i } } u _ { \ i } - \sum _ { \ j = 1 } ^ { \ i - 1 } c _ { \ i j } u _ { \ j } , \qquad C = \mathrm { d i a g } ( \gamma _ { 1 1 } ^ { - 1 } , \ldots , \gamma _ { s s } ^ { - 1 } ) - \Gamma ^ { - 1 } .
$$

Inserting this formula into (7.4) and dividing by $h$ yields

$$
\begin{array} { c } { { \displaystyle \left( \frac { 1 } { h \gamma _ { \scriptscriptstyle { \vphantom { \bigg ( } } I } } { \cal I } - { \cal J } \right) u _ { \scriptscriptstyle { \vphantom { \bigg ( } } I } \left( y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \iota _ { \jmath } } u _ { \jmath } \right) + \sum _ { \jmath = 1 } ^ { \imath - 1 } \left( \frac { c _ { \iota _ { \jmath } } } { h } \right) u _ { \jmath } , \qquad i = 1 , \dots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { s } m _ { \jmath } u _ { \jmath } , } } \end{array}
$$

where

$$
( a _ { \imath j } ) = ( \alpha _ { \imath j } ) \Gamma ^ { - 1 } , \qquad ( m _ { 1 } , \ldots , m _ { s } ) = ( b _ { 1 } , \ldots , b _ { s } ) \Gamma ^ { - 1 } .
$$

Compared to (7.4) the formulation (7.25) of a Rosenbrock method avoids not only the above mentioned matrix-vector multiplication, but also the $n ^ { 2 }$ multiplications for $\{ \gamma _ { \imath \imath } h \} J$ . Similar transformations were first proposed by Wolfbrandt (1977), Kaps & Wanner (1981) and Shampine (1982). The formulation (7.25) can be found in Kaps,Poon & Bui (1985).

For non-autonomous problems this transformation yields

$$
\begin{array} { r } { \Big ( \displaystyle \frac { 1 } { h \gamma _ { \eta _ { 2 } } } I - \displaystyle \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \Big ) u _ { \iota } = f \Big ( x _ { 0 } + \alpha _ { \iota } h , y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { \iota _ { j } } u _ { j } \Big ) } \\ { + \displaystyle \sum _ { j = 1 } ^ { \iota - 1 } \Big ( \displaystyle \frac { c _ { \iota j } } { h } \Big ) u _ { j } + \gamma _ { \iota } h \displaystyle \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) } \end{array}
$$

with $\alpha _ { \iota }$ and $\gamma _ { i }$ given by (7.5).

For implicit differential equations of the form (7.2b) the transformed Rosenbrock method becomes

$$
\begin{array} { l } { \displaystyle \left( \frac { 1 } { h \gamma _ { \scriptscriptstyle { \mathscr { N } _ { \tau } } } } { M } - \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \right) u _ { \scriptscriptstyle { \tau } } = f \Big ( x _ { 0 } + \alpha _ { i } h , y _ { 0 } + \sum _ { \tau = 1 } ^ { \tau - 1 } a _ { \scriptscriptstyle { \tau \mathscr { I } } } u _ { \tau } \Big ) } \\ { \displaystyle + { M \sum _ { \tau = 1 } ^ { i - 1 } \left( \frac { c _ { \tau _ { \mathscr { I } } } } { h } \right) u _ { \scriptscriptstyle { \tau } } } + \gamma _ { \scriptscriptstyle { \tau } } h \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) . } \end{array}
$$

Coding. Rosenbrock methods are nearly as simple to implement as explicit Runge-Kutta methods. The only difference is that at each step the Jacobian $\partial f / \partial y$ has to be evaluated and $s$ linear systems have to be solved. Thus, one can take an explicit RK code (say DOPRI5),add four lines which compute $\partial f / \partial y$ by finite differences (or call a user-supplied subroutine JAC which furnishes it analytically); add further a call to a Gaussian DEComposition routine, and add to each evaluation-stage a call to a linear SOLver. Since the method is of order 4(3), the step size prediction formula

$$
h _ { n e w } = h \cdot \operatorname* { m i n } \Bigl \{ 6 . , \operatorname* { m a x } \Bigl ( 0 . 2 , 0 . 9 \cdot ( T o l / e r r ) ^ { 1 / 4 } \Bigr ) \Bigr \}
$$

seems appropriate.

However, we want the code to work economically for non-autonomous problems as well as for implicit equations. Further, if the dimension of the system is large, it becomes crucial that the linear algebra be done,whenever possible, in banded form. All these possibilities,autonomous or not, implicit or explicit, $\partial f / \partial y$ banded or not, $B$ banded or not, $\partial f / \partial y$ analytic or not,("... that is the question") lead to $2 ^ { 5 }$ different cases, for each of which the code contains special parts for high efficiency. Needless to say, it works well on all stiff problems of Sect.IV.1. A more thorough comparison and testing will be given in Sect.IV.10.

# The“Hump"

On some very stiff equations, however, the code shows a curious behaviour: con-sider the van der Pol equation in singular perturbation form(1.5'） with

$$
\varepsilon = 1 0 ^ { - 6 } , \quad y _ { 1 } ( 0 ) = 2 , \quad y _ { 2 } ( 0 ) = - 0 . 6 6 .
$$

We further select method GRK4T (Table 7.2; each other method there behaves similarly)and $T o l = 7 \cdot 1 0 ^ { - 5 }$ . Fig.7.3 shows the numerical solution $y _ { 1 }$ as well as the step sizes chosen by the code. There all rejected steps are indicated by an $\times$

![](images/ee80221625c1291378fc33ce9ed6e8c522a014bc01be786c1f4335f0a56c4d77.jpg)  
Fig. 7.3. Step sizes for GRK4T at Equation (1.5')

Curious step size drops (by a factor of about $1 0 ^ { - 3 }$ ) occur without any apparent exterior reason. Further, these drops are accompanied by a huge number of step rejections (up to 2O). In order to understand this phenomenon, we present in the left picture of Fig.7.4 the exact local error as well as the estimated local error $\| y _ { 1 } - { \widehat { y } } _ { 1 } \|$ at $x = 0 . 5 5 1 3 9$ as a function of the step size $h$ (both in logarithmic scale). The current step size is marked by large symbols. The error behaves like $C \cdot h ^ { 5 }$ only for very small $h \left( \leq 1 0 ^ { - 6 } = \varepsilon \right)$ .Between $h = 1 0 ^ { - 5 }$ and the step size actually used $\left\{ \approx 1 0 ^ { - 2 } \right\}$ the error is more or less constant. Whenever this constant is larger than $T o l$ (horizontal broken line), the code is forced to decrease the step size until $h \approx \varepsilon$ . As a first remedy, we accelerate this lengthy process, as Shampine (1982) also did,by more drastical step size reductions $\left( h _ { n e w } = h / 1 0 \right)$ after each second consecutive step rejection. It also turns out (see right picture of Fig.7.4) that the effect disappears in the neighbourhood of the actual step size for the $L$ - stable method (where $R ( \infty ) = 0 ,$ ).Methods with $R ( \infty ) = 0$ and also ${ \widehat { R } } ( \infty ) = 0$ have been derived by Kaps & Ostermann (1990).

![](images/4fc7cdf4f5ba909f0bfec76a7cd816cf2f5473c07b9117f37c79b5cd9b5af1d6.jpg)  
Fig.7.4. Study of local error for (1.5') at $x = 0 . 5 5 1 3 9$

A more thorough understanding of these phenomena is possible by the consideration of singular perturbation problems (Chapter VI).

# Methods with Inexact Jacobian(W -Methods)

The relevant question is now, what is the cheapest type of implicitness we have to require. (Steihaug& Wolfbrandt 1979)

All the above theory is built on the assumption that $J$ is the exact Jacobian $\partial f / \partial y$ This implies that the matrix must be evaluated at every step,which can make the computations costly. The following attempt, due to Steihaug & Wolfbrandt (1979), searches for order conditions which assure classical order for all approximations $A$ of $\partial f / \partial y$ . The latter is then maintained over several steps and is just used to assure stability. The derivation of the order conditions must now be done somewhat differently: if $J$ is replaced by an arbitrary matrix $A$ ,Formula(7.6) becomes

$$
( k _ { \jmath } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = q ( f ^ { J } ( g _ { \jmath } ) ) ^ { ( q - 1 ) } | _ { h = 0 } + q \sum _ { K } A _ { K } ^ { J } \sum _ { k } \gamma _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( q - 1 ) } | _ { h = 0 }
$$

where $A = ( A _ { K } ^ { J } ) _ { J , K = 1 } ^ { n }$ , and we obtain

$$
( k _ { \ j } ^ { J } ) ^ { ( 2 ) } \big | _ { \phantom { h = 0 } h = 0 } = 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } \alpha _ { \ j k } + 2 \sum _ { K } A _ { K } ^ { J } f ^ { K } \sum _ { k } \gamma _ { \ j k } .
$$

Inserted into (7.8), the first term must equal the derivative of the exact solution and

the second must be zero. Similarly, we obtain instead of (7.7;3)

$$
\begin{array} { l } { { \displaystyle \left( k _ { _ { J } } ^ { J } \right) ^ { ( 3 ) } \big | _ { h = 0 } = 3 \sum _ { K , L } f _ { K L } ^ { J } f ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \alpha _ { _ { J l } } } } & { { ( 7 . 3 1 ; 2 ) } } \\ { { \displaystyle \qquad + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \alpha _ { _ { k l } } + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } A _ { L } ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \gamma _ { k l } } } \\ { { \displaystyle \qquad + 3 \cdot 2 \sum _ { K , L } A _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } \gamma _ { _ { J k } } \alpha _ { _ { k l } } + 3 \cdot 2 \sum _ { K , L } A _ { K } ^ { J } A _ { L } ^ { K } f ^ { L } \sum _ { k , l } \gamma _ { _ { J k } } \gamma _ { _ { k l } } } } & { { ( 7 . 3 1 \sqrt { \frac { J } { \alpha _ { K } } } ) ^ { 2 } } } \end{array}
$$

and the order conditions for order three become

$$
\begin{array} { r l } & { \sum _ { b _ { 2 } = 1 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } = 1 / 2 } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } = 0 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 3 } \in \mathcal { S } _ { k } \in \mathcal { R } _ { f } = 1 / 3 } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \in \mathcal { K } _ { k } = 1 / 6 } } \\ & { \sum _ { b _ { 3 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 3 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 3 } \in \mathcal { T } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 4 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 . } } \end{array}
$$

For a graphical representation of the elementary differentials in (7.31;q) and of the order conditions (7.32) we need trees with two different kinds of vertices (one representing $f$ and the other $A$ ). As in Sect.II.15 we use “meagre” and “fat’ vertices (see Definitions I.15.1 to I.15.4). Not all trees with meagre and fat vertices ( $. P \mathrm { - }$ trees) have to be considered. From the above derivation we see that fat vertices have to be singly-branched (derivatives of the constant matrix $A$ are zero) and that they cannot be at the end of a branch. We therefore use the notation

$$
\begin{array} { r l } & { T W = \left\{ \begin{array} { l l } { P \mathrm { - t r e e s } ; \mathrm { ~ e n d \mathrm { - v e r t i c e s } ~ a r e ~ m e a g r e ~ a n d } } \\ { \mathrm { ~ f a t ~ v e r t i c e s ~ a r e ~ s i n g l y \mathrm { - } b r a n c h e d } \ } } \end{array} } \end{\right\array} \end{array}
$$

and if the vertices are labelled monotonically, we write $L T W$

Definition 7.5. The elementary differentials for trees $t \in T W$ are defined recursively by $F ^ { J } ( \tau ) ( y ) = f ^ { J } ( y )$ and

$$
F ^ { J } ( t ) ( y ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { K _ { 1 } , \ldots , K _ { m } } f _ { K _ { 1 } , \ldots , K _ { m } } ^ { J } ( y ) \cdot \left( F ^ { K _ { 1 } } ( t _ { 1 } ) ( y ) , \ldots , F ^ { K _ { m } } ( t _ { m } ) ( y ) \right) } & \\ { \quad } & { \mathrm { i f } t = \medspace _ { a } [ t _ { 1 } , \ldots , t _ { m } ] \quad \mathrm { ( m e a g r e ~ r o o t ) } } \\ { \displaystyle \sum _ { K } A _ { K } ^ { J } \cdot F ^ { K } ( t _ { 1 } ) ( y ) } & { \mathrm { i f } t = \medskip _ { b } [ t _ { 1 } ] \quad \mathrm { ( f a t ~ r o o t ) } . } \end{array} \right.
$$

Definition 7.6. For $t \in T W$ we let $\Phi _ { j } ( \tau ) = 1$ and

$$
\Phi _ { \ j } ( t ) = \left\{ \begin{array} { l l } { { \displaystyle \sum _ { k _ { 1 } , \ldots , k _ { m } } \alpha _ { \ j  k _ { 1 } } \ldots \alpha _ { \ j k _ { m } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \ldots \Phi _ { k _ { m } } ( t _ { m } ) } } & { { \mathrm { ~ i f ~ } t = \int _ { a } [ t _ { 1 } , \ldots , t _ { m } ] \ldots \Phi _ { k _ { m } } ( t _ { m } ) \mathrm { ~ d ~ } } } \\ { { \displaystyle \sum _ { k } \gamma _ { \jmath k } \Phi _ { k } ( t _ { 1 } ) } } & { { \mathrm { ~ i f ~ } t = \phantom { \left( \sum _ { k _ 1 } \right) } \mathrm { d } } } \end{array} \right.
$$

We remark that $T$ (the set of trees as considered for Runge-Kutta methods) is a subset of TW and that the above definitions coincide with Definitions II.2.3 and I1.2.9 (c.f. also Formulas (I1.2.18) and (II.2.19)). The general result is now the following

Theorem 7.7. A W -method (7.4) with $J = A$ arbitrary is of order $p$ iff

$$
\begin{array} { r l r } & { \displaystyle \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) = \frac { 1 } { \gamma ( t ) } \qquad } & { f o r t \in T \ w i t h \ \varrho ( t ) \le p , \ a n d } \\ & { \displaystyle \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) = 0 \qquad } & { f o r t \in T { \cal W } \setminus T \ w i t h \ \varrho ( t ) \le p . } \end{array}
$$

The proof is essentially the same as for Theorems 7.3 and 7.4.

Table 7.3. Number of order conditions for W-methods   

<table><tr><td>order p</td><td>12345 6 7 8</td></tr><tr><td>no. of conditions</td><td>3 21 58 166 498 1540</td></tr></table>

The number of order conditions for $W$ -methods is rather large (see Table 7.3), since each tree of $T$ with $\kappa$ singly-branched vertices gives rise to $2 ^ { \kappa }$ order conditions (in the case of symmetry some may be identical). Therefore, $W$ -methods of higher order are best obtained by extrapolation (see Sect. IV.9).

The stability investigation for linearly implicit methods with $A \neq f ^ { \prime } ( y _ { 0 } )$ is very complicated. If we linearize the differential equation (as in the beginning of Sect.IV.2) and assume the Jacobian to be constant,we arrive at a recursion of the form

$$
y _ { 1 } = R ( h f ^ { \prime } ( y _ { 0 } ) , h A ) y _ { 0 } .
$$

Since, in general, the matrices $f ^ { \prime } ( y _ { 0 } )$ and $A$ cannot be diagonalized simultaneously, the consideration of scalar test equations is not justified. Stability investigations for the case when $\left\| f ^ { \prime } ( y _ { 0 } ) - A \right\|$ is small will be considered in Sect.IV.11.

# Exercises

1. (Kaps 1977). There exists no Rosenbrock method (7.4) with $s \approx 4$ and $p = 5$ Prove this.

2.(Ngrsett & Wolfbrandt 1979). Generalize the derivation of order conditions for Runge-Kutta methods with the help of B-series (Sect.II.11, page 247) to Rosenbrock methods.

Hint. Prove that, foraB-series $B ( \mathbf { a } , y _ { 0 } )$ with $\mathbf { a } : T \longrightarrow \mathbb { R }$ satisfying $\mathbf { a } ( \emptyset ) = 0$

$$
h f ^ { \prime } ( y _ { 0 } ) B ( \mathbf { a } , y _ { 0 } ) = B ( \widehat { \mathbf { a } } , y _ { 0 } )
$$

is again a B-series with coefficients

$$
\widehat { \mathbf { a } } ( t ) = \left\{ \begin{array} { l l } { \varrho ( t ) \mathbf { a } ( t _ { 1 } ) } & { \mathrm { i f } t = [ t _ { 1 } ] } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right.
$$

3. Cooper & Sayfy (1983) consider additive Runge-Kut methods

$$
\begin{array} { l l } { { g _ { \scriptscriptstyle 4 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \scriptscriptstyle 4 \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) + h J \displaystyle \sum _ { \jmath = 1 } ^ { \imath } \eta _ { \scriptscriptstyle 4 \jmath } g _ { \jmath } ~ } } & { { i = 1 , \ldots , s + 1 } } \\ { { { } } } & { { { } } } \\ { { y _ { 1 } = g _ { s + 1 } ~ } } & { { { ( 7 . 3 - 1 ) } } } \end{array}
$$

wlose cofciertsi $\begin{array} { r } { \sum _ { j = 1 } ^ { \imath - 1 } \alpha _ { i j } = c _ { i } , \sum _ { j = 1 } ^ { \imath } \eta _ { \imath j } = 0 . } \end{array}$

a) Prove that (7.34) is equivalent to (7.4) whenever $\alpha _ { s + 1 , i } = b _ { i }$ and

$$
\left( \eta _ { \iota _ { 2 } } \right) \left( \alpha _ { i j } \right) = \left( \alpha _ { i j } \right) \left( \gamma _ { i j } \right) .
$$

Here all matrices are of dimension $( s + 1 ) \times ( s + 1 )$ . The last line of $( \gamma _ { i j } )$ need not be specified since the last column of $\left( \alpha _ { \iota j } \right)$ is zero.

b) If the coefficients of (7.34) satisfy $\alpha _ { i , i - 1 } \neq 0$ for all $i$ , then we can always find an equivalent method of type (7.4).

4.(Verwer 1980,Verwer & Scholz 1983)． Derive order conditions for Rosenbrock methods “with time-lagged Jacobian”,i.e., methods of type (7.4) where $J$ is assumed to be $f ^ { \prime } ( y ( x _ { 0 } - \omega h ) )$ . If $\omega$ is the step ratio $h _ { o l d } / h$ ,this allows re-use of the Jacobian of the previous step.

5.(Kaps & Ostermann 1989). Show that some order conditions of (7.32) can be shifted to higher orders if it is assumed that

$$
f ^ { \prime } ( y _ { 0 } ) - J = { \mathcal { O } } ( h ) .
$$

This makes the conditions of Exercise 4 independent of $\omega$ ·

Result. The number of order-shifts is equal to the number of fat nodes

# IV.8 Implementation of Implicit Runge-Kutta Methods

These have not been used to any great extent ..

(S.P. Ngrsett 1976)

However, the implementation difficulties of these methods have precluded their general use; ... (J.M. Varah 1979)

Although Runge-Kutta methods present an attractive alternative, especially for stiff problems，... it is generally believed that they will never be competitive with multistep methods.

(K. Burrage, J.C. Butcher & FH. Chipman 1980)

Runge-Kutta methods for stiff problems, we are just beginning to explore them ... (L. Shampine in Aiken 1985)

If the dimension of the differential equation $y \prime = f ( x , y )$ is $n$ ， then the s-stage fully implicit Runge-Kutta method (3.1） involves a $n \cdot s$ -dimensional nonlinear system for the unknowns $g _ { 1 } , \dots , g _ { s }$ . An efficient solution of this system is the main problem in the implementation of an implicit Runge-Kutta method.

Among the methods discussed in Sect.IV.5, the processes Radau IIA of Ehle, which are $L$ -stable and of high order, seem to be particularly promising. Most of the questions arising (starting values and stopping criteria for the simplified Newton iterations, efficient solution of the linear systems,and the selection of the step sizes) are discussed here for the particular Ehle method with $s \approx 3$ and $p = 5$ . This then constitutes a description of the code RADAU5 of the appendix. An adaptation of the described techniques to other fully implicit Runge-Kutta methods is more or less straight-forward, if the Runge-Kutta matrix has at least one real eigenvalue. We also describe briefly our implementation of the diagonal implicit method SDIRK4 (Formula (6.16)).

# Reformulation of the Nonlinear System

In order to reduce the influence of round-off errors we prefer to work with the smaller quantities

$$
z _ { \imath } = g _ { \imath } - y _ { 0 } .
$$

Then (3.1a) becomes

$$
z _ { \imath } = h \sum _ { \jmath = 1 } ^ { \ast } a _ { \imath _ { \jmath } } f ( x _ { 0 } + c _ { \jmath } h , y _ { 0 } + z _ { \jmath } ) \qquad i = 1 , \dots , s .
$$

Whenever the solution $z _ { 1 } , \dots , z _ { s }$ of the system (8.2a) is known, then (3.1b) is an explicit formula for $y _ { 1 }$ .A direct application of this requires s additional function evaluations. These can be avoided, if the matrix $A = \left( a _ { \imath j } \right)$ of the Runge-Kutta

coefficients is nonsingular. Indeed,(8.2a) can be written as

$$
\binom { z _ { 1 } } { \vdots } = A \left( \begin{array} { c } { { h f ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } } \\ { { \vdots } } \\ { { h f ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } } \end{array} \right) ,
$$

so that (3.1b) is seen to be equivalent to

$$
y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { s } d _ { \imath } z _ { \imath }
$$

where

$$
( d _ { 1 } , \dotsc , d _ { s } ) = ( b _ { 1 } , \dotsc , b _ { s } ) A ^ { - 1 } .
$$

For the 3-stage Radau IIA method(Table 5.6) the vector $d$ is simply $( 0 , 0 , 1 )$ ,since $b _ { \imath } = a _ { s \imath }$ for all $i$ .

Another advantageofFormula (8.2b)is the following: thequantities $z _ { 1 } , \dots , z _ { s }$ are computed iteratively and are therefore affected by iteration errors. The evaluation of $f ( x _ { 0 } + c _ { \iota } h , y _ { 0 } + z _ { \iota } )$ in Eq.(3.1b) would then, due to the large Lipschitz constant of $f$ ,amplify these errors, which then “can be disastrously inaccurate for a stiff problem" (L.F. Shampine 1980).

# Simplified Newton Iterations

For a general nonlinear differential equation the system (8.2a) has to be solved iteratively. In the stone-age of stiff computation (i.e., before 1967) people were usually thinking of simple fixed-point iteration. But this transforms the algorithm into an explicit method and destroys the good stability properties. The paper of Liniger & Willoughby (197O) then showed the advantages of using Newton's method for this purpose. Newton's method applied to system (8.2a) needs for each iteration the solution of a linear system with matrix

$$
\left( \begin{array} { c c c } { I - h a _ { 1 1 } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } & { \dots } & { - h a _ { 1 s } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } \\ { \vdots } & { } & { \vdots } \\ { - h a _ { s 1 } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } & { \dots } & { I - h a _ { s s } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } \end{array} \right) .
$$

$\begin{array} { r } { \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { \iota } h , y _ { 0 } + z _ { \iota } ) } \end{array}$ by an

$$
J \approx { \frac { \partial f } { \partial y } } ( x _ { 0 } , y _ { 0 } ) .
$$

Then the simplified Newton iterations for (8.2a) become

$$
\begin{array} { c } { { ( I - h A \otimes J ) \Delta Z ^ { k } = - Z ^ { k } + h ( A \otimes I ) F ( Z ^ { k } ) } } \\ { { Z ^ { k + 1 } = Z ^ { k } + \Delta Z ^ { k } . } } \end{array}
$$

Here $Z ^ { k } = ( z _ { 1 } ^ { k } , \dots , z _ { s } ^ { k } ) ^ { T }$ is the $k$ -th approximation tothesolution,and $\Delta Z ^ { k } =$ $( \Delta z _ { 1 } ^ { k } , \ldots , \ \Delta z _ { s } ^ { k } ) ^ { T }$ are the increments. $F ( Z ^ { k } )$ is an abbreviation for

$$
F ( Z ^ { k } ) = \left( f ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ^ { k } ) , \dots , f ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ^ { k } ) \right) ^ { T } .
$$

Each iteration requires $s$ evaluations of $f$ and the solution of a $n \cdot s$ -dimensional linear system. The matrix $\left( I - h A \otimes J \right)$ is the same for all iterations. Its LUdecomposition is done only once and is usually very costly.

Starting Values for the Newton Iteration. A natural and simple choice for the starting values in the iteration (8.4) (or equivalently (8.13) below), since the exact solution of (8.2a) satisfies $z _ { \imath } = \mathcal { O } ( h )$ ,would be

$$
z _ { \ i } ^ { 0 } = 0 , \qquad i = 1 , \ldots , s .
$$

However, better choices are possible in general. If the implicit Runge-Kutta method satisfies the condition $C ( \eta )$ (see Sections IV.5 and II.7) for some $\eta \leq s$ ,then

$$
z _ { \imath } = y ( x _ { 0 } + c _ { \imath } h ) - y _ { 0 } + \mathcal { O } ( h ^ { \eta + 1 } ) .
$$

Suppose now that $c _ { \iota } \neq 0 \ ( i = 1 , \ldots , s )$ and consider the interpolation polynomial of degree $s$ , defined by

$$
q ( 0 ) = 0 , \qquad q ( c _ { \ i } ) = z _ { \ i } \qquad i = 1 , \ldots , s .
$$

Since the interpolation error is of size $\mathcal { O } ( h ^ { s + 1 } )$ we obtain together with (8.6)

$$
y ( x _ { 0 } + t h ) - y _ { 0 } - q ( t ) = \mathcal { O } ( h ^ { \eta + 1 } )
$$

(cf. Theorem 7.10 of Chapter $\amalg$ for collocation methods)． We use the values of $q ( t )$ also beyond the interval $[ 0 , 1 ]$ and take

$$
z _ { \imath } ^ { 0 } = q ( 1 + w c _ { \imath } ) + y _ { 0 } - y _ { 1 } , \quad i = 1 , \ldots , s , \quad w = h _ { n e w } / h _ { o l d }
$$

as starting values for the Newton iteration in the subsequent step. Numerical experiments with the 3-stage Radau IIA method have shown that (8.5') usually leads to a faster convergence than (8.5).

Stopping Criterion. This question is closely related to an estimation of the iteration error. Since convergence is linear, we have

$$
\begin{array} { r } { \| \Delta Z ^ { k + 1 } \| \leq \Theta \| \Delta Z ^ { k } \| , \quad \mathrm { \ h o p e f u l l y ~ w i t h ~ } \quad \Theta < 1 . } \end{array}
$$

Applying the triangle inequality to

$$
Z ^ { k + 1 } - Z ^ { * } = ( Z ^ { k + 1 } - Z ^ { k + 2 } ) + ( Z ^ { k + 2 } - Z ^ { k + 3 } ) + . . .
$$

(where $Z ^ { \ast }$ is the exact solution of (8.2a)) yields the estimate

$$
\| Z ^ { k + 1 } - Z ^ { * } \| \leq \frac { \Theta } { 1 - \Theta } \| \Delta Z ^ { k } \| .
$$

The convergence rate $\Theta$ can be estimated by the computed quantities

$$
\begin{array} { r } { \Theta _ { k } = \| \Delta Z ^ { k } \| / \| \Delta Z ^ { k - 1 } \| , \qquad k \geq 1 . } \end{array}
$$

It is clear that the iteration error should not be larger than the local discretization error, which is usually kept close to $T o l$ . We therefore stop the iteration when

$$
\eta _ { k } \| \Delta Z ^ { k } \| \le \kappa \cdot T o l \quad \mathrm { w i t h } \quad \eta _ { k } = \frac { \Theta _ { k } } { 1 - \Theta _ { k } }
$$

and accept $Z ^ { k + 1 }$ as approximation to $Z ^ { * }$ . This strategy can only be applied after at least two iterations. In order to be able to stop the computations after the first iteration already (which is especially advantageous for linear systems) we take for $k = 0$ the quantity

$$
\eta _ { 0 } = \left( \operatorname* { m a x } ( \eta _ { o l d } , U r o u n d ) \right) ^ { 0 . 8 }
$$

where $\eta _ { o l d }$ is the last $\eta _ { k }$ of the preceding step. It remains to make a good choice for the parameter $\kappa$ in (8.10). To this end we applied the code RADAU5 for many different values of $\kappa$ between 10 and $1 0 ^ { - 4 }$ and with some different tolerances Tol to several differential equations. The observation was that the code works most efficiently for values of $\kappa$ around $1 0 ^ { - 1 }$ or $1 0 ^ { - 2 }$

It is our experience that the code becomes more efficient when we allow a relatively high number of iterations (eg., $k _ { m a x } = 7$ or 10). During these $k _ { m a x }$ iterations, the computations are interrupted and restarted with a smaller stepsize (for example with $h : = h / 2 )$ if one of the following situations occurs a) there is a $k$ with $\Theta _ { k } \ge 1$ (the iteration “diverges"); b) for some $k$ ，

$$
\frac { \Theta _ { k } ^ { k _ { m a x } - k } } { 1 - \Theta _ { k } } \| \Delta Z ^ { k } \| > \kappa \cdot T o l .
$$

The left-hand expression in (8.11) is a rough estimate of the iteration error to be expected after $k _ { m a x } - 1$ iterations.The norm,used in all these formulas,should be the same as the one used for the local error estimator.

If only one Newton iteration was necessary to satisfy (8.1O) or if the last $\Theta _ { k }$ was very small, say $\leq 1 0 ^ { - 3 }$ ， then we don't recompute the Jacobian in the next step. As a consequence, the Jacobian is computed only once for linear problems with constant coeffcients (as long as no step rejection occurs).

# The Linear System

An essential gain of numerical work for the solution of the linear system (8.4) is obtained by the following method, introduced independently by Butcher (1976) and Bickart (1977),which exploits with much profit the special structure of the matrix $I - h A \otimes J$ in (8.4).

The idea is to premultiply (8.4) by $( h A ) ^ { - 1 } \otimes I$ (we suppose here that $A$ is invertible) and to transform $A ^ { - 1 }$ to a simple matrix (diagonal, block diagonal, triangular or Jordan canonical form)

$$
{ \cal T } ^ { - 1 } A ^ { - 1 } { \cal T } = \Lambda .
$$

With the transformed variables $W ^ { k } = ( T ^ { - 1 } \otimes I ) Z ^ { k }$ , the iteration (8.4) becomes equivalent to

$$
\begin{array} { c } { { ( h ^ { - 1 } \Lambda \otimes I - I \otimes J ) \Delta W ^ { k } = - h ^ { - 1 } ( \Lambda \otimes I ) W ^ { k } + ( T ^ { - 1 } \otimes I ) F ( ( T \otimes I ) W ^ { k } ) } } \\ { { W ^ { k + 1 } = W ^ { k } + \Delta W ^ { k } . } } \end{array}
$$

We also replace $Z ^ { k }$ and $\Delta Z ^ { k }$ by $W ^ { k }$ and $\Delta W ^ { k }$ in the formulas (8.7)-(8.11) (and thereby again save some work).

For the sequel, we suppose that the matrix $A ^ { - 1 }$ has one real eigenvalue $\widehat { \gamma }$ and one complex conjugate eigenvalue pair ${ \widehat { \alpha } } \pm i { \widehat { \beta } }$ . This is a typical situation for 3-stage implicit Runge-Kutta methods such as Radau IA. With $\gamma = h ^ { - 1 } \widehat { \gamma }$ ， $\alpha =$ $h ^ { - 1 } \widehat { \alpha } , \beta = h ^ { - 1 } \widehat { \beta }$ the matrix in (8.13) becomes

$$
\left( \begin{array} { c c c } { { \gamma I - J } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \alpha I - J } } & { { - \beta I } } \\ { { 0 } } & { { \beta I } } & { { \alpha I - J } } \end{array} \right)
$$

so that (8.13) splits into two linear systems of dimension $n$ and $2 n$ , respectively. Several ideas are possible to exploit the special structure of the $2 n \times 2 n$ -submatrix. The easiest and numerically most stable way has turned out to be the following: transform the real subsystem of dimension $2 n$ into an $n$ -dimensional, complex system

$$
\big ( ( \alpha + i \beta ) I - J \big ) ( u + i v ) = a + i b
$$

and apply simple Gaussan elimination. For machines without complex arithmetic, one just has to modify the linear algebra routines. Then a complex multiplication consists of 4 real multiplications and the amount of work for the solution of (8.14') becomes approximately $4 n ^ { 3 } / 3$ operations. Thus the total work for system (8.14) is about $5 n ^ { 3 } / 3$ operations. Compared to $( 3 n ) ^ { 3 } / 3$ , which would be the number of operations necessary for decomposing the untransformed matrix $I - h A \otimes J$ in (8.4), we gain a factor of about 5 in arithmetical operations. Observe that the transformations, such as $Z ^ { k } = ( T \otimes I ) W ^ { k }$ ， need only $\mathcal { O } ( n )$ additions and multiplications. The gain is still more drastic for methods with more than 3 stages.

Transformation to Hessenberg Form. For large systems with a full Jacobian $J$ a further gain is possible by transforming $J$ to Hessenberg form

$$
S ^ { - 1 } J S = H = \left( \begin{array} { l l l l } { { \ast } } & { { \cdot \cdot } } & { { \ast } } & { { \ast } } \\ { { \ast } } & { { } } & { { } } & { { \ast } } \\ { { } } & { { \cdot _ { \cdot } } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ast } } & { { \ast } } \end{array} \right) .
$$

This procedure was originally proposed for multistep methods by Enright (1978) and extended to the Runge-Kutta case by Varah (1979). With the code ELMHES, taken from LINPACK, this is performed with $2 n ^ { 3 } / 3$ operations. Because the multiplication of $S$ with a vector needs only $n ^ { 2 } / 2$ operations (observe that $S$ is triangular) the solution of (8.13) is found in $\mathcal { O } ( n ^ { 2 } )$ operations, if the Hessenberg matrix $H$ is known. This transformation is especially advantageous, if the Jacobian $J$ is not changed during several steps.

# Step Size Selection

One possibility to select the step sizes is Richardson extrapolation (cf. Sect.II.4). We describe here the use of an embedded pair of methods which is easier to pro-gram and which makes the code more flexible. The following formulas are for the special case of the 3-stage Radau IIA methods; the same ideas are applicable to all implicit Runge-Kutta methods, whose Runge-Kutta matrix has at least one real eigenvalue.

Embedded Formula. Since our method is of optimal order, it is impossible to embed it efficiently into one of still higher order. Therefore we search for a lower order method of the form

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \left( \widehat { b } _ { 0 } f ( x _ { 0 } , y _ { 0 } ) + \sum _ { \iota = 1 } ^ { 3 } \widehat { b } _ { \iota } f ( x _ { 0 } + c _ { \iota } h , g _ { \iota } ) \right)
$$

where $g _ { 1 } , g _ { 2 } , g _ { 3 }$ are the values obtained from the Radau IIA method and $\widehat { b } _ { 0 } \not = 0$ (the choice $\widehat { b } _ { 0 } = \gamma _ { 0 } = \widehat { \gamma } ^ { - 1 }$ ，where $\widehat { \gamma }$ is the real eigenvalue of the matrix $A ^ { - 1 }$ ， again saves some multiplications). The difference

$$
{ \widehat { y } } _ { 1 } - y _ { 1 } = \gamma _ { 0 } h f ( x _ { 0 } , y _ { 0 } ) + \sum _ { i = 1 } ^ { 3 } ( { \widehat { b } } _ { \imath } - b _ { \imath } ) h f ( x _ { 0 } + c _ { \imath } h , g _ { i } ) ,
$$

which can also be written in the form

$$
\begin{array} { r } { \widehat { y } _ { 1 } - y _ { 1 } = \gamma _ { 0 } h f ( x _ { 0 } , y _ { 0 } ) + e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } , } \end{array}
$$

then serves for error estimation. In order that $\widehat { y } _ { 1 } - y _ { 1 } = \mathcal { O } ( h ^ { 4 } )$ the coefficients have to satisfy

$$
\displaystyle { \big ( e _ { 1 } , e _ { 2 } , e _ { 3 } \big ) = \frac { \gamma _ { 0 } } { 3 } ( - 1 3 - 7 \sqrt { 6 } , - 1 3 + 7 \sqrt { 6 } , - 1 ) } .
$$

Unfortunately, for $y ^ { \prime } = \lambda y$ and $h \lambda  \infty$ the difference (8.17) behaves like $\widehat { y } _ { 1 } -$ $y _ { 1 } \approx \gamma _ { 0 } h \lambda y _ { 0 }$ ，which is unbounded and therefore not suitable for stiff equations. We propose (an idea of Shampine) to use instead

$$
e r r = ( I - h \gamma _ { 0 } J ) ^ { - 1 } ( \widehat { y } _ { 1 } - y _ { 1 } ) .
$$

The LU-decomposition of $\left( ( h \gamma _ { 0 } ) ^ { - 1 } I - J \right)$ is available anyway from the previous work, so that the computation of (8.19) is cheap. For $h  0$ we still have $e r r =$ $\mathcal { O } ( h ^ { 4 } )$ ,and for $h \lambda  \infty$ (if $y ^ { \prime } = \lambda y$ and $J = \lambda$ ) we obtain $e r r  - 1$

This behaviour (for $h \lambda  \infty )$ ） is already much beter than that for $\widehat { y } _ { 1 } - y _ { 1 }$ ， but it is not good enough in order to avoid the “hump” phenomenon, described in Sect.IV.7. In the first step and after every rejected step for which $\left\| e r r \right\| > 1$ ，we therefore use instead of (8.19) the expression

$$
\widetilde { e r r } = ( I - h \gamma _ { 0 } J ) ^ { - 1 } \big ( \gamma _ { 0 } h f \big ( x _ { 0 } , y _ { 0 } + e r r \big ) + e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } \big )
$$