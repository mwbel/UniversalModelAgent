of $\mathbb { C } ^ { n }$ . Then we define the matrix $Z$ by

$$
Z u _ { 1 } : = f / \| g \| , \qquad \quad Z u _ { \mathit { \iota } } : = x u _ { \iota } - \langle u _ { \iota } , f \rangle u _ { 1 } / \| g \| , \quad \quad i = 2 , \ldots , n .
$$

We have $Z g = f$ , and one readily verifies that $\operatorname { R e } \langle Z v , v \rangle \leq x \| v \| ^ { 2 }$ for all $v =$ $\textstyle \sum _ { \imath = 1 } ^ { n } \alpha _ { \imath } u _ { \imath }$

Lower Bound. We first consider nonconfluent Runge-Kutta methods. For given $Z _ { 1 } , \dots , Z _ { s }$ with $\mu ( Z _ { \imath } ) \leq x$ let $A ( x )$ be a continuous function satisfying $h A ( x _ { 0 } +$ $c _ { \ i } h ) = Z _ { i }$ and $\mu ( A ( x ) ) \leq x$ for all $_ x$ （ $\vert A ( x )$ is,for example, obtained by linear interpolation). Then we have $\Delta y _ { 1 } = K ( Z _ { 1 } , \dots , Z _ { s } ) \Delta y _ { 0 }$ and, consequently, also $\varphi _ { B } ( x ) \geq \| K ( Z _ { 1 } , \ldots , Z _ { s } ) \|$ for all $Z _ { 1 } , \dots , Z _ { s }$ with $\mu ( Z _ { i } ) \leq x$

For confluent methods the proof is more complicated. Without loss of general-  
ity we can assume that the method is irreducible, because neither the value $\varphi _ { B } ( x )$   
nor the right-hand expression of Eq.(12.41) change, when the method is replaced   
by an equivalent one. The main observation is now that the Lemmata 12.20 and $Z _ { 1 } , \dots , Z _ { s }$ $\mu ( Z _ { \imath } ) \leq x$ $\begin{array} { r } { \Delta g _ { \ i } = \Delta y _ { 0 } + \sum _ { \ j = 1 } ^ { s } a _ { i \ j } Z _ { \ j } \Delta \bar { g } _ { \it j } } \end{array}$ $f : \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$   
which satisfies (12.39) with $\nu \simeq x$ (we put $h = 1$ )and $f ( g _ { \imath } ) - f ( \widehat { g } _ { \imath } ) = Z _ { \imath } ( g _ { \imath } - \widehat { g } _ { \imath } )$   
This completes the proof of the theorem. □

For 1 -stage methods ( $( s = 1 )$ ）the Theorem of von Neumann (Corollary 11.4) implies that it is sufficient to consider scalar, complex-valued $z _ { 1 }$ in Eq. (12.41). Since $\begin{array} { r } { K ( z ) = R ( z ) } \end{array}$ in this case, we have

$$
\varphi _ { B } ( x ) = \varphi _ { R } ( x ) \qquad { \mathrm { f o r ~ a l l ~ 1 \mathrm { - } s t a g e ~ m e t h o d s . } }
$$

For the moment it is not clear, whether one can restrict the supremum in Eq.(12.41) to scalar, complex-valued $z _ { \imath }$ also for $s \geq 2$ . This would require a generalization of the Theorem of von Neumann to functions of more than one variables (Hairer & Wanner 1996). We shall come back to this question later in this section.

Theorem 12.24 (Hairer & Zennaro 1996). For $B$ -stable Runge-Kutta methods the error growth function is superexponential, i.e., $\varphi _ { B } ( 0 ) = 1$ and

$$
\varphi _ { B } ( x _ { 1 } ) \varphi _ { B } ( x _ { 2 } ) \leq \varphi _ { B } ( x _ { 1 } + x _ { 2 } ) \qquad f o r ~ x _ { 1 } , x _ { 2 } ~ h a \nu i n g ~ t h e ~ s a m e ~ s i g n .
$$

Proof. The property $\varphi _ { B } ( 0 ) = 1$ follows from Definition 12.5. For the proof of the inequality we consider the rational function

$$
S ( z ) = u _ { A } ^ { * } K ( A _ { 1 } - z I , \ldots , A _ { s } - z I ) v _ { A } u _ { B } ^ { * } K ( B _ { 1 } + z I , \ldots , B _ { s } + z I ) v _ { B } ,
$$

where the matrices $A _ { \ j } , B _ { \ j }$ satisfy $\mu ( A _ { \ j } ) \leq x _ { 1 } + x _ { 2 }$ and $\mu ( B _ { \jmath } ) \leq 0$ ,and $u _ { A } , v _ { A } ,$ $u _ { B } , v _ { B }$ are arbitrary vectors of $\mathbb { C } ^ { n }$ .Using the property $\mu ( { \dot { A } } _ { \ j } - z I ) = \mu ( A _ { \ j } ) -$ $\mathrm { R e } z$ and the fact that $\begin{array} { r } { \| C \| = \operatorname* { s u p } _ { \| u \| = 1 , \| v \| = 1 } \left| u ^ { * } C v \right| } \end{array}$ , the inequality is obtained exactly as in the proof of Theorem 11.6. □

The fact that $\varphi _ { B } ( x )$ is superexponential together with $\varphi _ { B } ( - \infty ) = | R ( \infty ) |$ (see Exercise 8) allows us to draw the same conclusions on asymptotic stability of numerical solutions as in Sect.IV.11.

# Computation of $\varphi _ { B } ( { \pmb x } )$

The idea is to search for the maximum of $\| \Delta y _ { 1 } \|$ under the restriction (12.39). More precisely, we consider the following inequality constrained optimization problem:

$$
\begin{array} { r l } & { \| \Delta y _ { 1 } \| ^ { 2 } \to \operatorname* { m a x } , } \\ & { \operatorname { R e } \left. \Delta f _ { i } , \Delta g _ { \ i } \right. \le x \| \Delta g _ { \ i } \| ^ { 2 } , \quad i = 1 , \ldots , s . } \end{array}
$$

Here $\Delta f _ { 1 } , \ldots , \Delta f _ { s }$ are regarded as independent variables in $\mathbb { C } ^ { n } , \Delta y _ { 1 }$ and $\Delta g _ { \imath }$ are defined by (12.5), and $\Delta y _ { 0 }$ is considered as a parameter. A classical approach for solving the optimization problem (12.43) is to introduce Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ , and to consider the Lagrangian

$$
\begin{array} { r l r } & { } & { \mathcal { L } ( \Delta f , D ) = \displaystyle \frac { 1 } { 2 } \| \Delta y _ { 1 } \| ^ { 2 } - \sum _ { \imath = 1 } ^ { s } d _ { \imath } \left( \mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { \imath } \right. - x \| \Delta g _ { \imath } \| ^ { 2 } \right) } \\ & { } & { = - \displaystyle \frac { 1 } { 2 } \left( \Delta y _ { 0 } ^ { * } , \Delta f ^ { * } \right) \left( \left( \begin{array} { c c } { \alpha } & { u ^ { T } } \\ { u } & { W } \end{array} \right) \otimes I \right) \left( \begin{array} { c } { \Delta y _ { 0 } } \\ { \Delta f } \end{array} \right) , } \end{array}
$$

where $\Delta f = ( \Delta f _ { 1 } , \dots , \Delta f _ { s } ) ^ { T }$ ， $D = \operatorname { d i a g } \left( d _ { 1 } , \dots , d _ { s } \right)$ , and

$$
\begin{array} { r l } & { \alpha = - 1 - 2 x \mathbb { 1 } ^ { T } D \mathbb { 1 } , } \\ & { \quad u = D \mathbb { 1 } - b - 2 x A ^ { T } D \mathbb { 1 } , } \\ & { \quad W = D A + A ^ { T } D - b b ^ { T } - 2 x A ^ { T } D A . } \end{array}
$$

Theorem 12.25 (Burrage & Butcher 1980). If the matrix

$$
\left( \begin{array} { c c } { { \alpha + \varphi ^ { 2 } } } & { { u ^ { T } } } \\ { { u } } & { { W } } \end{array} \right) \qquad i s p o s i t i v e s e m i - d e f t n i t e
$$

for some $d _ { 1 } \geq 0 , \ldots , d _ { s } \geq 0$ ， then it holds $\| \Delta y _ { 1 } \| \le \varphi \| \Delta y _ { 0 } \|$ for all problems satisfying (12.39) with $h \nu \leq x$ . Consequently, we have $\varphi _ { B } ( x ) \leq \varphi$

Proof. Substracting $\varphi ^ { 2 } \| \Delta y _ { 0 } \| ^ { 2 } / 2$ from both sides of (12.44) yields

$$
\frac { 1 } { 2 } \Big ( \| \Delta y _ { 1 } \| ^ { 2 } - \varphi ^ { 2 } \| \Delta y _ { 0 } \| ^ { 2 } \Big ) - \sum _ { \iota = 1 } ^ { s } d _ { \iota } \Big ( \mathrm { R e } \left. \Delta f _ { \iota } , \Delta g _ { \iota } \right. - x \| \Delta g _ { \iota } \| ^ { 2 } \Big ) \leq 0 .
$$

The statement then follows from $d _ { \imath } \geq 0$ and $\mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { \imath } \right. \leq x \| \Delta g _ { \imath } \| ^ { 2 }$

With the help of this theorem, Burrage & Butcher (1980) computed an upper bound of $\varphi _ { B } ( x )$ for many 2-stage methods. It turned out that for al these 2 -stage methods $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ ,where

$$
\varphi _ { K } ( x ) = \operatorname* { s u p } _ { \substack { \mathrm { R e } z _ { 1 } \leq x , \dots , \mathrm { R e } z _ { s } \leq x } } | K ( z _ { 1 } , \dots , z _ { s } ) | .
$$

There naturally arises the question: is it true that $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ for all Runge-Kutta methods? If we want to check the validity of $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ for a given Runge-Kutta method, we have to find non-negative Lagrange multipliers $d _ { \imath }$ ,such that (12.46) is satisfied. The following lemmas will be useful for this purpose.

We denote by $z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 }$ the values, for which the supremum in Eq.(1.47) is attained. By the maximum principle we have $z _ { \jmath } ^ { 0 } = x + i y _ { \jmath } ^ { 0 }$ $( y _ { \jmath } ^ { 0 } = \infty$ is admitted). We further put $z ^ { 0 } = ( z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 } )$ and let $\partial _ { j } K ( z ^ { 0 } )$ be the derivative of $K ( z _ { 1 } , \ldots , z _ { s } )$ with respect to the $j$ th argument, evaluated at $z ^ { 0 }$ ·

Lemma 12.26. Let x be fxed with $\varphi _ { K } ( x ) < \infty$ . The condition (12.46) with $\varphi = \varphi _ { K } ( x )$ then uniquely determines the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ (see $E q . \left( l 2 . 5 3 \right) b e l o w \rangle$ . They are real and positive.

Proof. Consider the identity (12.44) for the special case,where $\Delta f _ { \jmath }$ is scalar, $\Delta f _ { _ { \jmath } } = z _ { _ { \jmath } } \Delta g _ { _ { \jmath } }$ ,and hence $\Delta y _ { 1 } = K ( z _ { 1 } , \dots , z _ { s } )$ . For $\operatorname { R e } z _ { \jmath } = x$ this identity becomes

$$
| K ( z _ { 1 } , \dots , z _ { s } ) | ^ { 2 } - \varphi ^ { 2 } = - ( 1 , \Delta f ^ { * } ) \binom { \alpha + \varphi ^ { 2 } } { u } \binom { u ^ { T } } { \Delta f } \cdot
$$

Putting $\varphi : = \varphi _ { K } ( x )$ and $z _ { \jmath } : = z _ { \jmath } ^ { 0 }$ (eventually one has to consider limits) the lefthand expression of Eq.(12.48) vanishes. This together with assumption (12.46) implies that $u + W \Delta f = 0$ ,i.e.,

$$
D \mathbb { 1 } - \boldsymbol { b } - 2 x \boldsymbol { A } ^ { T } \boldsymbol { D } \mathbb { 1 } + \left( \boldsymbol { D } \boldsymbol { A } + \boldsymbol { A } ^ { T } \boldsymbol { D } - \boldsymbol { b } \boldsymbol { b } ^ { T } - 2 x \boldsymbol { A } ^ { T } \boldsymbol { D } \boldsymbol { A } \right) \Delta f = 0 .
$$

Collecting suitable terms, and using $\Delta f = Z _ { 0 } \Delta g$ and $\Delta g = \mathbb { 1 } + A \Delta f$ , where $Z _ { 0 } =$ diag $\big ( z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 } \big )$ ,this relation becomes

$$
D \Delta g = ( I - A ^ { T } Z _ { 0 } ^ { * } ) ^ { - 1 } \boldsymbol { b } \cdot \boldsymbol { K } ( z ^ { 0 } ) .
$$

We shall show that all components of $\Delta g = ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 }$ are different from zero, so that (12.49) uniquely determines the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ ·

Expanding $K ( z _ { 1 } , \ldots , z _ { s } )$ into a Taylor series with respect to $z _ { \jmath }$ , we obtain

$$
K ( z _ { 1 } ^ { 0 } , \ldots , z _ { j } , \ldots , z _ { s } ^ { 0 } ) = K ( z ^ { 0 } ) \Bigl ( 1 + c ( z _ { j } - z _ { j } ^ { 0 } ) + \mathcal { O } \bigl ( ( z _ { j } - z _ { j } ^ { 0 } ) ^ { 2 } \bigr ) \Bigr ) ,
$$

where $c = \partial _ { j } K ( z ^ { 0 } ) / K ^ { \prime } ( z ^ { 0 } )$ . Since $| K ( z _ { 1 } ^ { 0 } , \dots , z _ { \jmath } , \dots , z _ { s } ^ { 0 } ) | \le | K ^ { \prime } ( z ^ { 0 } ) |$ for $\mathrm { R e } z _ { j } \le$ $\mathrm { R e } z _ { \jmath } ^ { 0 }$ ，we have $c > 0$ , and consequently also

$$
\partial _ { j } K ( z ^ { 0 } ) \neq 0 , \qquad 0 < \partial _ { \ j } K ( z ^ { 0 } ) / K ( z ^ { 0 } ) < \infty .
$$

Differentiating $K ( z _ { 1 } , \dots , z _ { s } ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 }$ 1 with respect to $z _ { \jmath }$ yields

$$
\partial _ { \ j } K ( z ^ { 0 } ) = b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } \boldsymbol { e } _ { \jmath } \boldsymbol { e } _ { \jmath } ^ { T } ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 } ,
$$

and we obtain from (12.50) that

$$
b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } e _ { \jmath } \neq 0 , \qquad \quad \Delta g _ { \jmath } = e _ { \jmath } ^ { T } ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 } \neq 0 ,
$$

so that $d _ { 1 } , \ldots , d _ { s }$ are uniquely determined by(12.49). Dividing the $j$ th component of (12.49) by $\Delta g _ { \jmath }$ , it follows from (12.51) that

$$
d _ { \jmath } = | b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } e _ { \jmath } | ^ { 2 } \cdot \frac { K ( z ^ { 0 } ) } { \partial _ { \jmath } K ( z ^ { 0 } ) } ,
$$

which is a strictly positive real number by (12.50) and (12.52).

In this proof we have implicitly assumed that all $z _ { \jmath } ^ { 0 }$ are finite. If $z _ { \jmath } ^ { 0 } = x + i \infty$ for some $j$ ， one has to apply the standard transformation $\omega _ { \ j } = x + \mathrm { 1 } / ( z _ { \ j } - x )$ ， which maps the half-plane $\mathrm { R e } z _ { \jmath } \leq x$ onto $\mathrm { R e } \omega _ { \ j } \leq x$ ,and $\infty$ into $0$ □

Lemma 12.27. If the matrix W of Eq. $( l 2 . 4 5 c )$ with $d _ { 1 } , \ldots , d _ { s }$ given by Lemma 12.26, is positive semi-definite, then we have $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$

Proof. It follows from

$$
\left( \begin{array} { c c } { { \alpha + \varphi _ { k } ^ { 2 } ( x ) } } & { { u ^ { T } } } \\ { { u } } & { { W } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { \Delta f } } \end{array} \right) = 0
$$

(see Eq.(12.48)) and from $v ^ { T } W v \geq 0$ for all $v \in \mathbb { R } ^ { s }$ that the matrix in (12.54) is positive semi-definite. The statement then follows from Theorem 12.25. □

With the above results it is possible to check for a given Runge-Kutta method, whether $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ is satisfied. This can be done by the following algorithm:

compute $\varphi = \varphi _ { K } ( x )$ of Eq. (12.47) either numerically or with help of a formula manipulation program;   
， compute the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ from Lemma 12.26;   
· check, whether the matrix $W$ of Eq.(12.45c) is positive semi-definite. If this is the case, it holds $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ by Lemma 12.27.

Example 12.28. For the two-stage Radau IIA method (see Table 5.5) the function $K ( z _ { 1 } , z _ { 2 } )$ is given by

$$
K ( z _ { 1 } , z _ { 2 } ) = \frac { 1 + z _ { 1 } / 3 } { 1 - 5 z _ { 1 } / 1 2 - z _ { 2 } / 4 + z _ { 1 } z _ { 2 } / 6 } .
$$

The maximum of $\left| { \cal K } ( z _ { 1 } , z _ { 2 } ) \right|$ on the set $\mathrm { R e } z _ { \imath } \leq x$ is attained at

$$
\begin{array} { r l } & { z _ { 1 } ^ { 0 } = \left\{ \begin{array} { l l } { x + i \infty } & { \mathrm { f o r } x \leq \xi } \\ { x + \imath x \sqrt { \displaystyle \frac { 4 5 - 4 2 x + 8 x ^ { 2 } } { 9 + 1 8 x - 8 x ^ { 2 } } } } & { \mathrm { f o r } \xi \leq x < 3 / 2 } \end{array} \right. } \\ & { z _ { 2 } ^ { 0 } = \left\{ \begin{array} { l l } { x } & { \mathrm { f o r } x \leq \xi } \\ { x + i \displaystyle \frac { x \sqrt { \displaystyle ( 4 5 - 4 2 x + 8 x ^ { 2 } ) ( 9 + 1 8 x - 8 x ^ { 2 } ) } } { 8 x ^ { 2 } - 6 x - 9 } } & { \mathrm { f o r } \xi \leq x < 3 / 2 } \end{array} \right. } \end{array}
$$

(the value $\xi = ( 9 - 3 \sqrt { 1 7 } ) / 8$ is a root of $9 + 1 8 x - 8 x ^ { 2 } = 0 { \mathrm { : } }$ and it is given by

$$
\varphi _ { k } ( x ) = \left\{ \begin{array} { l l l } { \displaystyle \frac { 4 } { 5 - 2 x } } & { \mathrm { i f } } & { x \leq \xi } \\ { \displaystyle \frac { 3 + 4 x } { \sqrt { ( 3 - 2 x ) ( 3 + 4 x - 2 x ^ { 2 } ) } } } & { \mathrm { i f } } & { \xi \leq x < 3 / 2 . } \end{array} \right.
$$

The function $K ( z _ { 1 } , z _ { 2 } )$ is not bounded on $\mathrm { R e } z _ { \imath } \leq x$ for $x \ge 3 / 2$ . From the proof of Lemma 12.26 we compute $d _ { \mathrm { { i } } }$ and $d _ { 2 }$ ,and obtain

$$
d _ { 1 } = \left\{ \begin{array} { l l } { \displaystyle \frac { 9 } { ( 3 - x ) ( 5 - 2 x ) } } & { \mathrm { f o r } x \le \xi } \\ { \displaystyle \frac { ( 3 + 4 x ) ^ { 2 } } { 4 ( 3 + 4 x - 2 x ^ { 2 } ) } } & { \mathrm { f o r } \xi \le x } \end{array} \right. \qquad d _ { 2 } = \left\{ \begin{array} { l l } { \displaystyle \frac { 2 } { 5 - 2 x } } & { \mathrm { f o r } x \le \xi } \\ { \displaystyle \frac { 3 + 4 x } { 4 ( 3 + 4 x - 2 x ^ { 2 } ) } } & { \mathrm { f o r } \xi \le x . } \end{array} \right.
$$

With these values one checks straight-forwardly that the matrix $W$ of Eq.(12.45c) is semi-definite positive,so that $\varphi _ { B } ( x ) = \varphi _ { \bar { \Lambda } ^ { \prime } } ( x )$ ； see also Burrage & Butcher (1980). Actually, the matrix $W$ is non-singular for $x < \xi$ ,and of rank one for $\xi \le x < 3 / 2$

A comparison with Eq.(11.15) shows that we do not obtain the same estimate as for linear autonomous problems.

The above algorithm can easily be applied to other two-stage methods. We thus obtain for the two-stage Gauss method

$$
\mathrm { i f } \ - \infty < x \leq 0
$$

$$
\varphi _ { B } ( x ) = \left\{ \begin{array} { l l } { 1 } \\ { \displaystyle \frac { 2 x + \sqrt { 9 + 3 x ^ { 2 } } } { 3 - x } } \end{array} \right.
$$

and for the two-stage Lobatto IIIC method

$$
\varphi _ { B } ( x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { 1 } { 1 - x + x ^ { 2 } } \quad } & { \mathrm { i f } \ - \infty < x \leq 0 } \\ { \displaystyle \frac { 1 } { 1 - x } \quad } & { \mathrm { i f } \ 0 \leq x < 1 . } \end{array} \right.
$$

For methods with more than two stages, explicit formulas are dificult to obtain, and one has to apply numerical methods for the computation of $z _ { \jmath } ^ { 0 }$ (supremum in Eq.(12.47)).

# Exercises

1. Prove, directly from Def.12.2, that the implicit Euler method is $B$ -stable.

2. Let $M$ be a symmetric $s \times s$ -matrix and $\langle \cdot , \cdot \rangle$ the scalar product of $\mathbb { R } ^ { n }$ . Then $M$ is non-negative definite, if and only if

$$
\sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { \iota _ { \jmath } } \langle u _ { \iota } , u _ { \jmath } \rangle \geq 0 \quad \mathrm { f o r ~ a l l } \quad u _ { \iota } \in \mathbb { R } ^ { n } .
$$

Hint. Use $M = Q ^ { T } D Q$ where $D$ is diagonal.

3. Give a simple proof for the $B$ -stability of the Radau IIA methods by extending the ideas of Example 12.3.

Hint. For the quadrature,based on the zeros of (5.2),we have

$$
\int _ { 0 } ^ { 1 } \varphi ( x ) d x = \sum _ { \iota = 1 } ^ { s } b _ { \iota } \varphi ( c _ { \iota } ) + C \varphi ^ { ( 2 s - 1 ) } ( \xi ) , \quad 0 < \xi < 1 .
$$

with $C < 0$ (see e.g. Abramowitz & Stegun (1964,Formula 25.4.31).

4.(Dahlquist & Jeltsch 1987). Prove that Method Iof Table 12.4 is $S$ -reducible with respect to the partition $( \{ 1 \} , \{ 2 , 3 \} )$ . The reduced method II itself is $D J$ - reducible and reduces to Method III.

For the initial value problem $y ^ { \prime } = f ( y )$ ， $y ( 0 ) = 1$ ,where $f ( y ) = y ^ { 2 }$ for $y \geq 0$ and $f ( y ) = 0$ for $y < 0$ ,and for $h \approx 2$ , Methods I and III have unique solutions which are different. Explain this apparent contradiction.

0 0 0 0   
1/2 0 1 -1/2 0 0 0   
1/2 0 1/2 0 1/2 0 1/2 0 0 1 6 -b 1 0 1 Method I Method II Method III

5. Give a counterexample of an irreducible $A N$ -stable but not algebraically stable,and hence not $B$ -stable method.

Hint. Start with any algebraically stable method with，say, two stages and modify it as indicated in Table 12.5. Find conditions on the free parameters $d , e , \alpha$ such that the two methods are identical for equations $y ^ { \prime } = \lambda ( x ) y$ . This ensures $A N$ -stability of the second method. Then play with the parameters to destroy algebraic stability.

6. Show that the method of Table 12.1 is $D J$ -reducible, but not $S$ -reducible; show that it is algebraically stable together with the reduced method.

Table 12.5. Construction of $A N$ -stable but not $B$ -stable method

$$
\begin{array} { r } { \underbrace { c _ { 1 } } _ { \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & & & & { \Rightarrow } & & & { c _ { 1 } } & {  } & { a _ { 1 1 } } & { a _ { 1 2 } \alpha } & & { a _ { 1 2 } ( 1 - \alpha ) } & & \\ { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & & & & { c _ { 2 } } & & & { c _ { 2 } } & & { d \alpha } & & { d ( 1 - \alpha ) } & \\ { b _ { 1 } } & { b _ { 2 } } & & & & { \Rightarrow } & & & { c _ { 2 } } & & & { b _ { 2 } \alpha } & & { e ( 1 - \alpha ) } & & \end{array} } } \end{array}
$$

Show that the method of Table 12.2 is $S$ -reducible, but not $D J$ -reducible;   
show that it is not algebraically stable,but that the reduced method is.

7. (Sandberg & Shichman 1968,Vanselow 1979,Hundsdorfer 1985). Prove that Rosenbrock methods are not $B$ -stable in the sense of Definition 11.2.

Hint. Apply the method to the scalar problem $y ^ { \prime } = f ( y )$ ， $y _ { 0 } = 1$ where $f ( y )$ is a non-increasing function satisfying (for a small $\varepsilon$ ）

$$
f ( y ) = { \left\{ \begin{array} { l l } { - y } & { { \mathrm { ~ i f ~ } } \ \left| y - 1 \right| \geq 2 \varepsilon } \\ { - 1 } & { { \mathrm { ~ i f ~ } } \ \left| y - 1 \right| \leq \varepsilon . } \end{array} \right. }
$$

8.(Hairer & Zennaro 1996). For irreducible,algebraically stable Runge-Kutta methods the error growth function satisfies

$$
\varphi _ { B } ( x ) \leq { \frac { { \sqrt { 1 - 2 x \gamma ( 1 - \varrho ^ { 2 } ) } } - 2 x \gamma \varrho } { 1 - 2 x \gamma } }
$$

where $\varrho = \vert R ( \infty ) \vert \ ( R ( z )$ is the stability fuction), $\begin{array} { r } { \gamma = \left( \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } ^ { - 1 } v _ { \jmath } ^ { 2 } \right) ^ { - 1 } } \end{array}$ and $\begin{array} { r } { ( v _ { 1 } , \ldots , v _ { s } ) ^ { T } = \operatorname* { l i m } _ { \varepsilon \to 0 } b ^ { T } ( A + \varepsilon I ) ^ { - 1 } } \end{array}$

Hint. From(12.7) we have $\begin{array} { r } { \| \Delta y _ { 1 } \| ^ { 2 } \leq \| \Delta y _ { 0 } \| ^ { 2 } + 2 x \sum _ { \imath } b _ { \imath } \| \Delta g _ { \imath } \| ^ { 2 } } \end{array}$ . Then, compute $\Delta f _ { \imath }$ from (12.5b) (if $A$ is invertible), insert it into (12.5a) and conclude $\begin{array} { r } { \Delta y _ { 1 } = R ( \infty ) \Delta y _ { 0 } + \sum _ { \jmath } ( \sum _ { \imath } b _ { \imath } \omega _ { \imath \jmath } ) \Delta g _ { \jmath } } \end{array}$ ，where $( \omega _ { \imath \jmath } ) = A ^ { - 1 }$ . The Cauchy-Schwarz inequality yields $\begin{array} { r } { \sum _ { \ i } b _ { \ i } \| \Delta g _ { \ i } \| ^ { 2 } \geq \gamma \big ( \| \Delta y _ { 1 } \| - \varrho \| \Delta y _ { 0 } \| \big ) ^ { 2 } } \end{array}$ which, in-serted into the first estimate, gives a second degree inequality for $\Delta y _ { 1 }$

9.Prove that for the 3-stage Gauss method we have for $x \ge 0$

$$
\varphi _ { B } ( x ) \geq ( 1 + x / 2 ) / ( 1 - x / 2 ) .
$$

Hint. Using (12.18), compute $\bar { K } ( Z )$ for $z _ { 1 }  - \infty , z _ { 2 } = x , z _ { 3 }  - \infty$

10. If the matrix $W$ of Eq.(12.45c),with $d _ { 1 } , \ldots , d _ { s }$ given by Lemma 12.26,is either non-singular or of rank $\leq 1$ , then it holds $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$

Hint. Exploit the fact that the expression in Eq.(12.48) with $\varphi = \varphi _ { K } ( x )$ is non-positive for all $z _ { \jmath }$ with $\mathrm { R e } z _ { \jmath } \leq x$ ·

11. Show that for a non-negative definite symmetric matrix $M = ( m _ { \imath \jmath } )$ one has

$$
| m _ { \imath \jmath } | \leq \sqrt { m _ { \imath \imath } m _ { \jmath \jmath } } .
$$

# IV.13 Positive Quadrature Formulas and B-Stable RK-Methods

Bien que le probleme (des quadratures) ait une durée de deux cents ans ä peu pres,bien qu'il était l'objet de nombreuses recherches de plusieurs géometres: Newton, Cotes, Gauss, Jacobi, Hermite,Tchebychef, Christoffel, Heine,Radeau [sic],A.Markov, T. Stitjes [sic], C. Possé, C. Andréev, N. Sonin et d'autres, il ne peut étre considéré, cependant, comme suffisamment épuisé.

(V. Steklov 1917)

We shall give a constructive characterization of all irreducible $B$ -stable Runge-Kutta methods (Theorem 13.15). Because of Theorem 12.16 we first have to study quadrature formulas with positive weights.

# Quadrature Formulas and Related Continued Fractions

Steklov (1916) proved that a family of interpolatory quadrature formulas converges for all Riemann integrable functions,if all weights of the formulas are positive ("Il faut remarquer cependant que de tels théoremes généraux ne peuvent avoir aucune valeur pratique ..."). This theorem, rediscovered around 1922 by Fejér, initiated an extensive search for quadrature formulas with positive weights. Fejer (1933, “weiter habe ich noch auf sehr kurzem Wege das folgende Resultat erhalten ...") found the result:

“if $P _ { s } ( z )$ are the Legendre polynomials normalized as in(13.4) and $c _ { 1 } , \ldots , c _ { s }$ are the zeros of $M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z )$ with $\alpha _ { 2 } \leq 0$ , then the weights $b _ { i }$ are all positive".

The theory of $B$ -stable methods renewed the interest in positive quadrature formulas and Burrage (1978) obtained the sharp bound

$$
\alpha _ { 2 } < \frac { ( s - 1 ) ^ { 2 } } { 4 ( 2 s - 1 ) ( 2 s - 3 ) }
$$

for the positivity of the $b _ { \imath }$ in the above case. This is the same as condition (5.51) in a different normalization. A short proof of this result (see “Lemma $1 8 ^ { \circ }$ of Norsett & Wanner 1981） then led to a complete characterization of positive quadrature formulas by Sottas & Wanner (1982). An independent proof of an equivalent result was found by Peherstorfer (1981). In what follows,we give a new approach using continued fractions.

Consider a quadrature formula

$$
\sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( c _ { \jmath } ) \approx \int _ { 0 } ^ { 1 } f ( x ) d x
$$

with distinct nodes $c _ { \imath }$ and non-zero weights $b _ { \imath }$ . The main idea is to consider the rational function

$$
Q ( z ) = \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \frac { 1 } { z - c _ { \jmath } } = \frac { N ( z ) } { M ( z ) }
$$

where, as usual, $M ( z ) = ( z - c _ { 1 } ) \cdot . . . \cdot ( z - c _ { s } )$ . We first express the order of the quadrature formula in terms of the function $Q ( z )$

Lemma 13.1. A quadrature formula is of order $p$ if and only if $Q ( z )$ ， defined by (13.2), satisfies

$$
Q ( z ) = - \log \left( 1 - \frac { 1 } { z } \right) + \mathcal { O } \left( \frac { 1 } { z ^ { p + 1 } } \right) \qquad f o r \quad z \to \infty .
$$

Proof. Inserting the geometric series for $( 1 - c _ { \jmath } / z ) ^ { - 1 }$ into (13.2) we obtain

$$
Q ( z ) = \sum _ { k \geq 1 } \Big ( \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { k - 1 } \Big ) \frac { 1 } { z ^ { k } } .
$$

Therefore (13.3) is equivalent to

$$
\sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { k - 1 } = \frac 1 k \qquad \mathrm { f o r } \quad k = 1 , \dots , p .
$$

We now study the case of the Gaussian quadrature formulas, where the function (13.2) will be denoted by $Q _ { s } ^ { G } ( z ) = N _ { s } ^ { G } ( z ) / M _ { s } ^ { G } ( z )$ ; here the $c _ { \imath }$ are the zeros of the $s$ -degree shifted Legendre polynomial

$$
P _ { s } ( z ) = \frac { s ! } { ( 2 s ) ! } \frac { d ^ { s } } { d z ^ { s } } \big ( z ^ { s } ( z - 1 ) ^ { s } \big ) ,
$$

which is normalized so that the coefficient of $z ^ { s }$ is 1．The polynomials (13.4) satisfy the recurrence relation (see Eq.(5.53) or Abramowitz & Stegun, p. 782)

$$
P _ { s + 1 } ( z ) = \Big ( z - \frac { 1 } { 2 } \Big ) P _ { s } ( z ) - \tau _ { s } P _ { s - 1 } ( z ) , \qquad \tau _ { s } = \frac { s ^ { 2 } } { 4 ( 4 s ^ { 2 } - 1 ) }
$$

and $P _ { 0 } ( z ) = 1 , P _ { - 1 } ( z ) = 0$ . Since this quadrature formula is of optimal order $2 s$ ， it follows from (13.3) that

$$
N _ { s } ^ { G } ( z ) = - M _ { s } ^ { G } ( z ) \log \left( 1 - \frac { 1 } { z } \right) + \mathcal { O } \left( \frac { 1 } { z ^ { s + 1 } } \right) .
$$

We now insert $M _ { s } ^ { G } ( z ) = P _ { s } ( z )$ (see (13.2)) into (13.5) and multiply by $\log ( 1 -$ $1 / z )$ (which is $\mathcal { O } ( 1 / z )$ for $z \to \infty$ ). A comparison with (13.6) shows that the polynomials $N _ { s } ^ { G } ( z )$ must also satisfy the recurrence formula (13.5) (with $N _ { 0 } ^ { G } ( z ) = 0$ ， $N _ { 1 } ^ { G } ( z ) = 1 )$ .It thus follows from elementary properties of continued fractions (Exercise 1 or Perron (1913), page 4) that

$$
Q _ { s } ^ { G } ( z ) = \frac { 1 } { | z - \frac { 1 } { 2 } } - \frac { \tau _ { 1 } } { | z - \frac { 1 } { 2 }  } - \ldots - \frac { \tau _ { s - 1 } } { | { z - \frac { 1 } { 2 } }  } .
$$

For an arbitrary quadrature formula we have

Lemma 13.2. An irreducible rational function $Q ( z ) = N ( z ) / M ( z )$ (with deg M = $s$ ，deg $N = s - 1$ ) satisfies (13.3) with $p \geq 2 ( s - k )$ ， if and only if

$$
Q ( z ) = { \frac { 1 } { | z - { \frac { 1 } { 2 } } - { \frac { \tau _ { 1 } } { | z - { \frac { 1 } { 2 } }  } } - \ldots - { \frac { \tau _ { s - k - 1 } } { | z - { \frac { 1 } { 2 } } - { \frac { g ( z ) } { | f ( z )  } }  } } } } - { \frac { g ( z ) } { | f ( z )  } }
$$

with deg $f = k$ and deg $g \le k - 1$

Proof. From Lemma 13.1 we know that $Q ( z ) = Q _ { s } ^ { G } ( z ) + \mathcal { O } \bigl ( 1 / z ^ { 2 ( s - k ) + 1 } \bigr )$ . Therefore the first $2 ( s - k )$ coefficients in the continued fraction expansions for $Q ( z )$ and $Q _ { s } ^ { G } ( z )$ must be the same. □

Endlich sei noch die folgende Formel wegen ihrer häufigen Anwendungen ausdricklich hervorgehoben:

(O. Perron 1913, page 5)

Lemma 13.3. The functions $M ( z )$ and $N ( z )$ of Lemma 13.2 are related to $f ( z )$ and $g ( z )$ of(13.7') as follows:

$$
\begin{array} { r } { M ( z ) = P _ { s - k } ( z ) f ( z ) - P _ { s - k - 1 } ( z ) g ( z ) , } \\ { N ( z ) = N _ { s - k } ^ { G } ( z ) f ( z ) - N _ { s - k - 1 } ^ { G } ( z ) g ( z ) . } \end{array}
$$

Proof. This follows from the recursion (13.30)and Exercise 1 below,if we put there $b _ { 0 } = 0$ ， $b _ { 1 } = \ldots = b _ { s - k } = z - 1 / 2 , b _ { s - k + 1 } = f ( z )$ and $a _ { 1 } = 1$ ， $a _ { _ { 2 } } = - \tau _ { _ { 2 ^ { - 1 } } } ( j =$ $2 , \ldots , s - k )$ ， $a _ { s - k + 1 } = - g ( z )$ □

Solving the linear system (13.8) for $f ( z )$ and $g ( z )$ gives, with the use of Exercise 2,

$$
\begin{array} { r l } & { f ( z ) \cdot \tau _ { 1 } \cdot \cdot \cdot \tau _ { s - k - 1 } = N ( z ) P _ { s - k - 1 } ( z ) - M ( z ) N _ { s - k - 1 } ^ { G } ( z ) } \\ & { g ( z ) \cdot \tau _ { 1 } \cdot \cdot \cdot \tau _ { s - k - 1 } = N ( z ) P _ { s - k } ( z ) - M ( z ) N _ { s - k } ^ { G } ( z ) . } \end{array}
$$

# Number of Positive Weights

For a given rational function (13.2), the weights are determined by

$$
b _ { \imath } = \frac { N ( c _ { \imath } ) } { M ^ { \prime } ( c _ { \imath } ) } .
$$

But we want our theory to work also for confluent nodes for which $M ^ { \prime } ( c _ { \imath } ) = 0$ ·

Therefore we suppose that $c _ { 1 } , \ldots , c _ { m } \ ( m \leq s )$ are the real and distinct zeros of $M ( z )$ of multiplicities $l _ { 1 } , \ldots , l _ { m }$ . Then we let

$$
b _ { \imath } = \frac { N ( c _ { \imath } ) } { M ^ { ( l _ { \imath } ) } ( c _ { \imath } ) } \qquad i = 1 , \ldots , m .
$$

For $l _ { \ i } = 1$ this is just (13.1O); otherwise we are considering the weights for the highest derivative of a Hermitian quadrature formula (see Exercise 3).

The main idea (following Sottas & Wanner 1982) is now to consider the path $\gamma ( t ) = ( f ( t ) , g ( t ) )$ in the plane $\mathbb { R } ^ { 2 }$ ,where $f$ and $g$ are the polynomials of (13.7'). For $t \to \pm \infty$ this path tends to infinity with horizontal limiting directions,since the degree of $f$ is higher than that of $g$ . Equation (13.8) tells us that for an irreducible $Q ( z )$ this path does not pass through the origin.

Definition 13.4. The rotation number $r$ of $\gamma$ is the integer for which $r \pi$ is the total angle of rotation around the origin for the path $\gamma ( t ) \left( - \infty < t < \infty \right)$ measured in the negative (clockwise) sense. Counter-clockwise rotations are negative.

An algebraic definition of $r$ is possible as

$$
r = \sum _ { \iota } \mathrm { s i g n } \left( f ^ { ( { \iota } _ { \iota } ) } ( t _ { \iota } ) g ( t _ { \iota } ) \right) ,
$$

where the summation is over allreal zeros of $f ( t )$ with odd multiplicity $l _ { \ i }$

Theorem 13.5 (Sottas & Wanner 1982). Let $Q ( z ) = N ( z ) / M ( z )$ be an irreducible rational function as in Lemma 13.2. Suppose that $c _ { 1 } , \ldots , c _ { m }$ are the (distinct) real zeros of $M ( z )$ with odd multiplicity and denote by $n _ { + }$ (respectively $n _ { - }$ ）the number of positive (respectively negative) $b _ { \imath }$ . Further, let $r$ be the rotation number of $\gamma = ( f , g )$ (Definition 13.4). Then

$$
n _ { + } - n _ { - } = s - k + r .
$$

Proof. The proof is by counting the number of crossings of the vectors $\gamma ( t ) =$ $( f ( t ) , g ( t ) )$ and $\beta ( t ) = ( P _ { s - k - 1 } ( t ) , P _ { s - k } ( t ) )$ , like the crossings of hands on a Swiss cuckoo clock.

From(13.9) we see that when $t$ equals a zero $c _ { \imath }$ of $M$ ， these two vectors are parallel in the same sense $( N ( c _ { \imath } ) > 0 )$ or in the opposite sense $( N ( c _ { \imath } ) < 0 )$ · From (13.8) we observe that $M ( t )$ is just the exterior product $\gamma ( t ) \times \beta ( t )$ .By elementary geometry,and taking into account Formula (13.10')，we see that at every zero $c _ { \imath }$ with odd multiplicity we have

i） $b _ { \imath } > 0$ , if the crossing of $\gamma ( t )$ with $\beta ( t )$ is clockwise;   
ii) $b _ { \imath } < 0$ , if this crossing is counter-clockwise.   
Zeros of $M ( t )$ with even multiplicity don't give rise to crossings.

Since the zeros of $P _ { s - k }$ and $P _ { s - k - 1 }$ interlace (see.g. Theorem 3.3.2 of Szego 1939),the vector $\beta ( t )$ turns counter-clockwise with a total angle of $- ( s -$ $k \pi$ (see Fig.13.1). The vector $\gamma ( t )$ turns with a total angle rπr measured clockwise (Definition 13.4). Since the limiting directions of $\gamma ( t )$ and $\beta ( t )$ are different (horizontal for $\gamma ( t )$ and vertical for $\boldsymbol { \beta } ( t )$ ）， $\gamma ( t )$ must cross $\beta ( t )$ ，as $t$ increases from $- \infty$ to $+ \infty$ ，exactly $s - k + r$ times more often clockwise than counterclockwise. This gives Formula (13.11). □

![](images/edfa93f029e03908a8c081103eafcbce4d78afd88eed38ad2539f4fbf3c9ffc9.jpg)  
Fig. 13.1. The path $( P _ { s - k - 1 } ( t ) , P _ { s - k } ( t ) )$ for $s - k = 7$

Corollary 13.6. Under the assumptions of Theorem 13.5, all zeros of $M ( z )$ are real and simple, and the $b _ { \imath }$ are positive if and only if

$$
r = k .
$$

Proof. $r = k$ means by (13.11) that $n _ { + } - n _ { -- } = s$ . Because of $n \geq 0$ and $\eta _ { i } \leq s ,$ this is equivalent to $n _ { + } = s$ and $n _ { \dots } = 0$ ， □

# Characterization of Positive Quadrature Formulas

The following theorem gives a constructive characterization of all quadrature formulas with positive weights.

# Theorem 13.7. Let

$$
\sigma _ { 1 } < \varrho _ { 1 } < \sigma _ { 2 } < \varrho _ { 2 } < . . . < \varrho _ { k - 1 } < \sigma _ { k }
$$

be arbitrary real numbers and $C$ a positive constant. Then, putting

$$
f ( z ) = ( z - \sigma _ { 1 } ) \ldots ( z - \sigma _ { k } ) , \quad g ( z ) = C ( z - \varrho _ { 1 } ) \ldots ( z - \varrho _ { k - 1 } ) ,
$$

computing $M ( z ) , \ N ( z )$ from (13.8), taking $c _ { 1 } , \ldots , c _ { s }$ as the zeros of $M ( z )$ and $b _ { i } f r o m ( I 3 . I O ) ,$ one obtains all quadrature formulas with positive weights of order $p \geq 2 ( s - k )$ .If $C = \tau _ { s - k }$ the order is $p \ge 2 ( s - k ) + 1$

Proof. The functions $f ( z )$ and $g ( z )$ are irreducible, so that also the fraction $N ( z ) / M ( z )$ is irreducible by (13.9). The statement now follows from Corollary 13.6,since the polynomials (13.12）are all possible polynomials for which $r \approx k$ . The stated order properties follow from Lemma 13.2. □

Example 13.8. Let $c _ { 1 } , \ldots , c _ { s }$ be the zeros of

$$
M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z ) .
$$

In order to study when the corresponding quadrature formula has positive weights, we use (13.5) to write (13.13) as

$$
M ( z ) = P _ { s - 1 } ( z ) \Big ( z - \frac { 1 } { 2 } + \alpha _ { 1 } \Big ) - P _ { s - 2 } ( z ) \big ( \tau _ { s - 1 } - \alpha _ { 2 } \big ) .
$$

Consequently $f ( z ) = z - 1 / 2 + \alpha _ { 1 } , g ( z ) = \tau _ { s - 1 } - \alpha _ { 2 }$ and Theorem 13.7 implies that the zeros of $M ( z )$ arerealandthe weightspositive,ifandoyif $\alpha _ { 2 } < \tau _ { s - 1 }$ ， hence (13.1) is proved.

For $k > 1$ the rotation number $r$ of $( f ( t ) , g ( t ) )$ can be computed with Sturm's algorithm (Lemma 13.3 of Sect. I.13). Consider, for example,

$$
\begin{array} { r l r } {  { M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z ) + \alpha _ { 3 } P _ { s - 3 } ( z ) } } \\ & { } & { = P _ { s - 2 } ( z ) \big [ ( z - \frac { 1 } { 2 } ) ( z - \frac { 1 } { 2 } + \alpha _ { 1 } ) + \alpha _ { 2 } - \tau _ { s - 1 } \big ] \qquad } \\ & { } & { \qquad - P _ { s - 3 } ( z ) \big [ \tau _ { s - 2 } ( z - \frac { 1 } { 2 } + \alpha _ { 1 } ) - \alpha _ { 3 } \big ] . } \end{array}
$$

Application of Lemma I.13.3 to the polynomials $f ( z ) = ( z - { \textstyle \frac { 1 } { 2 } } ) ( z - { \textstyle \frac { 1 } { 2 } } + \alpha _ { 1 } ) +$ $\alpha _ { 2 } - \tau _ { s - 1 }$ and $g ( z ) = \tau _ { s - 2 } ( z - \textstyle { \frac { 1 } { 2 } } + \alpha _ { 1 } ) - \alpha _ { 3 }$ shows that the corresponding quadrature formula has positive weights iff

$$
\frac { \alpha _ { 3 } } { \tau _ { s - 2 } } \Big ( \alpha _ { 1 } - \frac { \alpha _ { 3 } } { \tau _ { s - 2 } } \Big ) - \alpha _ { 2 } + \tau _ { s - 1 } > 0 ,
$$

a result first found by Burrage (1978).

# Necessary Conditions for Algebraic Stability

We now turn our attention to algebraic stability. We again use the notation $B ( p )$ ， $C ( \eta ) , D ( \xi )$ of Sect. IV.5.

Lemma 13.9 (Burrage 1982). Consider Runge-Kutta methods, which satisfy $B ( 2 )$ and the second condition for algebraic stability (i.e. M non-negative). Then,

$a$ ） $C ( k )$ implies $B ( 2 k - 1 )$ ； b） $D ( k )$ implies $B ( 2 k - 1 )$

Proof. Instead of considering $M$ ， we work with the transformed matrix $\widehat { M } =$ $V ^ { T } M V$ where $V = ( c _ { \imath } ^ { \jmath - 1 } ) _ { \imath , \jmath = 1 } ^ { s }$ 1),J=1 is the Vandermonde matrix. The elements of M are given by

$$
\widehat { m } _ { q r } = \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { r - 1 } + \sum _ { j = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } \sum _ { \imath = 1 } ^ { s } a _ { \jmath \imath } c _ { \imath } ^ { q - 1 } - \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } .
$$

We further introduce

$$
g _ { r } = r \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } - 1
$$

so that $B ( \nu )$ is equivalent to $g _ { r } = 0 \ ( r = 1 , \ldots , \nu )$ . Then $C ( k )$ simplifies (13.15) to

$$
\widehat { m } _ { q r } = \frac { 1 } { q \cdot r } \left( g _ { q + r } + 1 - ( g _ { q } + 1 ) ( g _ { r } + 1 ) \right) \qquad q \leq k , r \leq k .
$$

Similarly, $D ( k )$ implies

$$
\widehat { m } _ { q r } = - \frac { 1 } { q \cdot r } \left( g _ { q + r } + g _ { q } \cdot g _ { r } \right) \qquad q \leq k , r \leq k .
$$

We now start with the hypothesis $B ( 2 )$ ,i.e., $B ( 2 l )$ for ${ \mathit { l } } = 1$ .This means that $g _ { 1 } = . . . = g _ { 2 l } = 0$ , so that, in both cases, $\widehat { m } _ { l l } = 0$ . But if for a non-negative definite matrix a diagonal element is zero, the whole corresponding column must also be zero (see Exercise 11 of Sect.IV.12). This leads to $g _ { l + q } = 0$ for $q = 1 , \ldots , k ;$ so we have $B ( k + l )$ . We then repeat the argument inductively until we arrive at $B ( 2 k - 1 )$ □

Since $s$ -stage collocation methods satisfy $B ( s )$ and $C ( s )$ (see Theorem 7.8 of Chapter II) we have

Corollary 13.10 (Burrage 1978). An $s$ -stage algebraically stable collocation method must be of order at least $2 s - 1$ . □

Because symmetric methods have even order this gives:

Corollary 13.11 (Ascher & Bader 1986). $A$ symmetric algebraically stable collocation scheme has to be at Gaussian points. □

The next result states the necessity of the simplifying assumption $C ( k )$ . Ob-serve that by Theorem 12.16 the weights $b _ { \imath }$ of $D J$ -irreducible,algebraically stable methods have to be positive.

Lemma 13.12. If a Runge-Kutta method of order $p \geq 2 k + 1$ satisfies $b _ { i } > 0$ for $i = 1 , \dots , s$ , then the condition $C ( k )$ holds.

Proof (Dahlquist & Jeltsch (1979) atribute this idea to Butcher). The order conditions (see Sect. II.2)

$$
\sum _ { \ i = 1 } ^ { s } b _ { i } c _ { \ i } ^ { 2 q } = \frac { 1 } { 2 q + 1 }
$$

$$
\begin{array} { l } { { \displaystyle \sum _ { i , \jmath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q } a _ { \imath \jmath } c _ { \jmath } ^ { q - 1 } = \frac { 1 } { ( 2 q + 1 ) q } } } \\ { { \displaystyle \sum _ { \imath , j , m = 1 } ^ { s } b _ { \imath } a _ { i \jmath } c _ { \jmath } ^ { q - 1 } a _ { \imath m } c _ { m } ^ { q - 1 } = \frac { 1 } { ( 2 q + 1 ) q ^ { 2 } } } } \end{array}
$$

imply that

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } \bigg ( \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { q - 1 } - \frac { c _ { \imath } ^ { q } } { q } \bigg ) ^ { 2 } = 0
$$

for $2 q + 1 \leq p$ . Since the $b _ { \imath }$ are positive,the individual terms of this sum must be zero for $q \leq k$ . □

A simple consequence of this lemma are the following order barriers for diagonally implicit DIRK $\mathbf { \rho } ( a _ { \imath \jmath } = 0$ for $i < j \}$ ）and singly diagonally implicit SDIRK $( a _ { \iota _ { \mathcal { I } } } = 0$ for $i < j$ and $a _ { \scriptscriptstyle 2 2 } = \gamma$ for all $i$ ） methods.

# Theorem 13.13 (Hairer 1980).

$a$ ）A DIRK method with all $b _ { \imath }$ positive has order at most $\boldsymbol { \delta }$ $b$ ）An SDIRK method with all $b _ { \imath }$ positive has order at most 4; $c$ ） An algebraically stable DIRK method has order at most 4.

Proof. a) Suppose the order is greater than 6 and let $i$ be the smallest index such that $c _ { \imath } \neq 0$ . Then by Lemma 13.12

$$
a _ { { } _ { 1 2 } } c _ { { } _ { 2 } } = { \frac { c _ { \imath } ^ { 2 } } { 2 } } , \qquad a _ { { } _ { 1 2 } } c _ { { } _ { \imath } } ^ { 2 } = { \frac { c _ { \imath } ^ { 3 } } { 3 } } ,
$$

contradicting $c _ { \imath } \neq 0$ ·

b) As above,we arrive for order greater than 4 at

$$
a _ { \scriptscriptstyle { \imath \imath } } c _ { \scriptscriptstyle { \imath } } = \frac { c _ { \scriptscriptstyle { \imath } } ^ { 2 } } { 2 } \quad \mathrm { o r } \quad a _ { \scriptscriptstyle { \imath \imath } } = \frac { c _ { \scriptscriptstyle { \imath } } } { 2 } ( \ne 0 ) .
$$

Since for SDIRK methods we have $a _ { \scriptscriptstyle { \imath 2 } } = a _ { \scriptscriptstyle { 1 1 } }$ , this leads to $c _ { 1 } = a _ { 1 1 } \neq 0$ , hence i= 1. Now a11 = c1/2 contradicts α = C1:

c) It is sufficient to consider $D J$ -ireducible methods, since the reduction process (see Table 12.3) leaves the class of DIRK methods invariant. From Theorem 12.16 and Lemma 13.12 we obtain that algebraic stability and order greater than 4 imply

$$
a _ { 1 1 } = c _ { 1 } , \qquad a _ { 1 1 } c _ { 1 } = \frac { c _ { 1 } ^ { 2 } } { 2 } ,
$$

and hence $a _ { 1 1 } = 0$ . Inserted into $m _ { 1 1 }$ this yields $m _ { 1 1 } = - b _ { 1 } ^ { 2 } < 0$ , contradicting the non-negativity of the matrix $M$ . □

Similarly to Lemma 13.12 we have the following result for the second type of simplifying assumptions.

Lemma 13.14. Ifa Runge-Kutta method of order $p \ge 2 k + 1$ is algebraically stable and satisfies $b _ { \imath } > 0$ for all $i$ ， then the condition $D ( k )$ holds.

Proof. The main idea is to use the $W$ -transformation of Sect.IV.5 and to consider $W ^ { T } M W$ instead of $M$ (see also the proof of Theorem 12.8). By Theorem 5.14 there exists a matrix $W$ satisfying $T ( k , k )$ (see Definition 5.10).With the help of Lemma 13.12 and Theorem 5.11a we obtain that the first $k$ diagonal elements of

$$
\begin{array} { r } { W ^ { T } M W = ( W ^ { T } B W ) X + X ^ { T } ( W ^ { T } B W ) ^ { T } - e _ { \mathbf { l } } e _ { \mathbf { l } } ^ { T } } \end{array}
$$

are zero. Since $M$ and hence also $W ^ { T } M W$ is non-negative definite, the first $k$ columns and rows of $W ^ { T } M W$ have to vanish. Thus the matrix $( W ^ { T } B W ) X$ must be skew-symmetric in these regions (with exception of the first element). Because of $C ( k )$ the first $k$ columns and rows of $( W ^ { T } B W ) X$ and $X$ are identical. Thus the result follows from Theorem 5.11. □

# Characterization of Algebraically Stable Methods

Theorem 12.16, Lemma 13.12 and Lemma 13.14 imply that $D J$ -irreducible and algebraically stable RK-methods of order $p \geq 2 k + 1$ satisfy $b _ { \imath } > 0$ for all $i$ , and the simplifying assumptions $C ( k )$ and $D ( k )$ . These properties allow the following constructive characterization of all irreducible $B$ -stable RK-methods.

Theorem 13.15 (Hairer & Wanner 1981). Consider a pth order quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right) _ { \imath = 1 } ^ { s }$ with positive weights and let W satisfy Property $T ( k , k )$ of Definition $5 . 1 0$ with $k = [ ( p - 1 ) / 2 ]$ . Then all $p$ th order algebraically stable Runge-Kuta methods corresponding to this quadrature formula are given by

$$
A = W X W ^ { - 1 }
$$

where

$$
( W ^ { T } B W ) X = \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ~ + ~ \left( \begin{array} { l l l l } { { 0 } } & { { - \xi _ { 1 } } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { \ddots } } & { { 0 } } & { { - \xi _ { k } } } \\ { { } } & { { } } & { { \xi _ { k } \left| ~ \overline { { { Q } } } ~ \right.}  } \end{array} \right)
$$

and $Q$ is an arbitrary matrix of dimension $s - k$ for which $Q + Q ^ { T }$ is non-negative definite. For $p$ even we have to require that $q _ { 1 1 } = 0$ .

Proof. Algebraic stability and the positivity of the weights $b _ { \imath }$ imply $C ( k )$ and $D ( k )$ with $k = [ ( p - 1 ) / 2 ]$ . The matrix $A$ of such a method can be written as (13.17) with $X$ given by (13.18). This follows from Theorem 5.11 and the fact that multiplication with $W ^ { T } B W$ does not change the first $k$ columns and rows of $X$ .This method is algebraically stable iff $M$ (or $W ^ { T } M W )$ is non-negative definite.By (13.16) this means that $Q + Q ^ { T }$ is non-negative definite.

Conversely,any Runge-Kutta method given by (13.17), (13.18) with $Q + Q ^ { T }$ non-negative definite is algebraically stable and satisfies $C ( k )$ and $D ( k )$ . There-fore it follows from Theorem 5.1 in the case of odd $p { = } 2 k + 1$ that the Runge-Kutta method is of order $p$

If $p$ is even, say $p { = } 2 k { + } 2$ , the situation is slightly more complicated. Because of

$$
q _ { 1 1 } = \sum _ { i , j = 1 } ^ { s } b _ { \imath } P _ { k } ( c _ { \imath } ) a _ { i j } P _ { k } ( c _ { j } )
$$

it follows from $B ( 2 k + 2 ) , C ( k ) , D ( k )$ that the order condition (13.19) below (with $\xi = \eta = k \AA$ ） is equivalent to $q _ { 1 1 } = 0$ . The stated order $p$ of the RK-method now follows from Lemma 13.16. □

In the above proof we used the following modification of Theorem 5.1.

Lemma 13.16. If the coefficients $b _ { \imath } , c _ { \imath } , a _ { i j }$ of an RK-method satisfy

$$
\sum _ { \ i , \ i = 1 } ^ { s } b _ { \ i } c _ { \ i } ^ { \xi } a _ { i \ i } c _ { \ j } ^ { \eta } = \frac { 1 } { ( \eta + \xi + 2 ) ( \eta + 1 ) }
$$

and $B ( p )$ ，C(n）， $D ( \xi )$ with $p \leq \eta + \xi + 2$ and $p \leq 2 \eta + 2$ ,then the method is oforder $p$

Proof. The reduction process with the help of $C ( \eta )$ and $D ( \xi )$ as described in Sect.II.7 (Volume I) reduces all trees to the bushy trees covered by $B ( p )$ .The only exception is the tree corresponding to order condition (13.19). □

Example 13.17 (Three-stage $B$ -stable SIRK methods). Choose a third order quadrature formula with positive weights and let $W$ satisfy $W ^ { T } B W = I$ .Then (13.18) becomes

$$
X = \left( \begin{array} { c c c } { { \frac { 1 } { 2 } } } & { { - \xi _ { 1 } } } & { { 0 } } \\ { { \xi _ { 1 } } } & { { a } } & { { b } } \\ { { 0 } } & { { c } } & { { d } } \end{array} \right) , \qquad \xi _ { 1 } = \frac { 1 } { 2 \sqrt { 3 } } .
$$

The method is $B$ -stable if $X ^ { T } + X - e _ { 1 } e _ { 1 } ^ { T }$ is non-negative, i.e. if

$$
a \geq 0 , \quad d \geq 0 , \quad 4 a d \geq ( c + b ) ^ { 2 } .
$$

If we want this method to be singly-implicit, we must have for the characteristic polynomial of $A$

$$
\chi _ { A } ( z ) = ( 1 - \gamma z ) ^ { 3 } = 1 - 3 \gamma z + 3 \gamma ^ { 2 } z ^ { 2 } - \gamma ^ { 3 } z ^ { 3 } .
$$

This means that (see (13.17))

$$
\begin{array} { r } { \displaystyle \frac { 1 } { 2 } + a + d = 3 \gamma } \\ { \displaystyle \frac { a } { 2 } + \frac { 1 } { 1 2 } + \frac { d } { 2 } + a d - c b = 3 \gamma ^ { 2 } } \\ { \displaystyle \frac { a d - c b } { 2 } + \frac { 1 } { 1 2 } d = \gamma ^ { 3 } . } \end{array}
$$

Some elementary algebra shows that these equations can be solved and the inequalities (13.20) satisfied if $1 / 3 \le \gamma \le 1 . 0 6 8 5 7 9 0 2$ , i.e., exactly if the corresponding rational approximation is $A$ -stable(cf. Table 6.3; see also Hairer & Wanner(1981), where the analogous case with $s = p = 5$ is treated).

# The “Equivalence" of $\pmb { A }$ - and $B$ -Stability

Many $A$ -stable RK-methods are not $B$ -stable (e.g., the trapezoidal rule, the Lobatto IIIA and Lobatto IIIB methods; see Theorem 12.12). On the other hand there is the famous result of Dahlquist (1978),saying that every $A$ -stable one-legmethod is $B$ -stable, which we shall prove in Sect.V.6. We have further seen in Example 13.17 that for a certain class of $A$ -stable methods there is always a $B$ - stable method with the same stability function. The general truth of this result was conjectured for many years and is as follows:

Theorem 13.18 (Hairer & Turke 1984, Hairer 1986).Let $R ( z ) = P ( z ) / Q ( z )$ $( P ( 0 ) = Q ( 0 ) = 1$ ， $\deg P \leq s$ ， $\deg Q = s$ ) be an irreducible, $A$ -stable function satisfying $R ( z ) - e ^ { z } = \mathcal { O } ( z ^ { p + 1 } )$ for some $p \geq 1$ . Then there exists an s-stage $B$ -stable Runge-Kutta method of order $p$ with $R ( z )$ as stability function.

Proof. Since $R ( z )$ is an approximation to $e ^ { z }$ of order $p$ , it can be written in the form

$$
R ( z ) = \frac { 1 + \frac { 1 } { 2 } \Psi ( z ) } { 1 - \frac { 1 } { 2 } \Psi ( z ) } , \qquad \Psi ( z ) = \frac { z \Big | } { | 1 } + \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } | } { 1 } + . . . + \frac { \xi _ { k - 1 } ^ { 2 } z ^ { 2 } | } { 1 } + \xi _ { k } ^ { 2 } z \Psi _ { k } ( z )
$$

where $k = [ ( p - 1 ) / 2 ]$ ， $\xi _ { \ j } ^ { 2 } = 1 / ( 4 ( 4 j ^ { 2 } - 1 ) )$ and $\Psi _ { k } ( z ) = z g ( z ) / f ( z )$ with $g ( 0 ) =$ $f ( 0 ) = 1$ ，d $\operatorname { s g } f \leq s - k$ ,deg $\cdot g \leq s - k - 1$ (for $p$ even we have in addition $g ^ { \prime } ( 0 ) =$ $f ^ { \prime } ( 0 ) )$ . For the diagonal Padé-approximation $R ^ { G } ( z )$ of order $2 s$ this follows from Theorem 5.18 with $\nu = s - 1$ and $\Psi _ { \nu } = z$ ：

$$
R ^ { G } ( z ) = \frac { 1 + \frac { 1 } { 2 } \Psi ^ { G } ( z ) } { 1 - \frac { 1 } { 2 } \Psi ^ { G } ( z ) } , \qquad \Psi ^ { G } ( z ) = \frac { z \Big | } { | 1 } + \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } | } { 1 } + \ldots + \frac { \xi _ { s - 1 } ^ { 2 } z ^ { 2 } | } { 1 } .
$$

For an arbitrary $R ( z )$ (satisfying the assumptions of the theorem) this is then a con-sequence of $R ( z ) = R ^ { G } ( z ) + \mathcal { O } ( z ^ { p + 1 } )$ , or equivalently $\Psi ( z ) = \Psi ^ { G } ( z ) + \mathcal { O } ( z ^ { p + 1 } )$

The function $R ( z )$ of (13.21) is $A$ -stable iff(Theorem 5.22)

$$
\operatorname { R e } \Psi _ { k } ( z ) < 0 \quad { \mathrm { f o r } } \quad \operatorname { R e } z < 0 .
$$

Therefore,the function $\chi ( z ) = - \Psi _ { k } ( - 1 / z )$ is positive (c.f. Definition 5.19) and by Lemma 13.19 below there exists an $\left( s - k \right)$ -dimensional matrix $Q$ such that

$$
\chi ( z ) = e _ { 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { 1 } \quad \mathrm { a n d } \quad Q + Q ^ { T }
$$

We now fix an arbitrary quadrature formula of order $p$ with positive weights $b _ { i }$ and (for the sake of simplicity) distinct nodes $c _ { i }$ . We let $W$ be a matrix satisfying $W ^ { T } B W = I$ and Property $T ( k , k )$ with $k = [ ( p - 1 ) / 2 ]$ (c.f. Lemma 5.12),and define the Runge-Kutta coefficients $\left( { a _ { \iota j } } \right)$ by (13.17) and (13.18). This Runge-Kutta method is algebraically stable, because $Q + Q ^ { T }$ is non-negative definite and of order $p$ (observe that $g ^ { \prime } ( 0 ) = f ^ { \prime } ( 0 )$ implies that the upper left element of $Q$ vanishes). Finally, it follows from Theorem 5.18 and $\Psi _ { k } ( z ) = - \chi ( - 1 / z ) =$ $z e _ { 1 } ^ { T } ( I - z Q ) ^ { - 1 } e _ { 1 }$ that its stability function is $R ( z )$ □

It remains to prove the following lemma.

Lemma 13.19. Let $\chi ( z ) = \alpha ( z ) / \beta ( z )$ be an irreducible rational function with real polynomials

$$
\alpha ( z ) = z ^ { n - 1 } + \alpha _ { 1 } z ^ { n - 2 } + \ldots , \quad \beta ( z ) = z ^ { n } + \beta _ { 1 } z ^ { n - 1 } + \ldots .
$$

Then $\chi ( z )$ is a positive function iff there exists an $\mathscr { n }$ -dimensional real matrix $Q$ ， such that

$$
\chi ( z ) = e _ { 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { 1 } \quad a n d \quad Q + Q ^ { T } \quad n o n { \cdot } n e g a t i v e d e f i n i t e .
$$

Proof. a) The sufficiency follows from

$$
\mathrm { R e } \chi ( z ) = q ( z ) ^ { \ast } \{ \mathrm { R e } z \cdot I + { \textstyle { \frac { 1 } { 2 } } } ( Q + Q ^ { T } ) \} q ( z )
$$

with $q ( z ) = ( Q + z I ) ^ { - 1 } e _ { 1 }$ ， since $Q + Q ^ { T }$ is non-negative definite.

b) For the proof of necessity, the hard part, we use Lemma 6.8 of Sect. V.6 below. This lemma is the essential ingredient for Dahlquist's equivalence result and willbe proved in the chapter on multistep methods. It states that the positivity of $\chi ( z )$ is equivalent to the existence of real, symmetric and non-negative definite matrices $A$ and $B$ , such that for arbitrary $z , w \in \mathbb { C }$ $\boldsymbol { \Xi } \mathbb { C } ( \vec { z } = ( z ^ { n - 1 } , \dots , z , 1 ) ^ { T }$ ， $\vec { w } =$ $( w ^ { n - 1 } , \ldots , w , 1 ) ^ { T } )$ ，

$$
\alpha ( z ) \beta ( w ) + \alpha ( w ) \beta ( z ) = ( z + w ) \vec { z } ^ { T } A \vec { w } + \vec { z } ^ { T } B \vec { w } .
$$

The matrix $A$ is positive definite, if $\alpha ( z )$ and $\beta ( z )$ are relatively prime.

Comparing the coeficients of $w ^ { n }$ in (13.25) we get

$$
\alpha ( z ) = \vec { z } ^ { T } A e _ { 1 }
$$

and observe that the first column of $A$ consists of the coefficients of $\alpha ( z )$ . For the Cholesky decomposition of $A$ ， $A = U ^ { T } U$ （ $U$ is an upper triangular matrix） we

thus have $U e _ { \mathbf { 1 } } = e _ { \mathbf { 1 } }$ .We next consider the possible computation of the matrix $Q$ from the relation

$$
( Q + z I ) U \vec { z } = \beta ( z ) \cdot e _ { 1 }
$$

or equivalently

$$
Q U \overrightarrow { z } = \beta ( z ) \cdot e _ { 1 } - z U \overrightarrow { z } .
$$

The right-hand side of(13.28) is a known polynomial of degree $n - 1$ ,since $U e _ { \mathbf { 1 } } =$ $e _ { 1 }$ . Therefore,a comparison of the coefficients in(13.28) yields the matrix $Q U$ and hence also $Q$ . It remains to prove that this matrix $Q$ satisfies (13.24).

Using (13.27), the formula $A e _ { 1 } = U ^ { T } U e _ { 1 } = U ^ { T } e _ { 1 }$ and (13.26) we obtain

$$
e _ { \bf 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { \bf 1 } \cdot \beta ( z ) = e _ { \bf 1 } ^ { T } U \vec { z } = e _ { \bf 1 } ^ { T } A ^ { T } \vec { z } = \alpha ( z ) ,
$$

which verifies the first relation of (13.24). Further,from (13.27) and $\alpha ( z ) = e _ { 1 } ^ { T } U \vec { z }$ we get

$$
\vec { z } ^ { T } U ^ { T } ( Q + w I ) U \vec { w } = \alpha ( z ) \beta ( w ) .
$$

Inserting this formula and the analogous one (with $z$ and $w$ exchanged） into (13.25) yields $0 = \vec { z } ^ { T } \big ( B - U ^ { T } \big ( Q + Q ^ { T } \big ) U \big ) \vec { w }$ , so that $B = U ^ { T } ( Q + Q ^ { T } ) U$ .This verifies the second relation of (13.24), since $B$ is symmetric and non-negative definite. □

# Exercises

1. (Perron (1913) attributes this result to Wallis,Arithmetica infinitorum 1655 and Euler 1737). Let the sequences $\{ A _ { k } \}$ and $\{ B _ { k } \}$ be given by

$$
\begin{array} { l l } { { A _ { k } = b _ { k } A _ { k - 1 } + a _ { k } A _ { k - 2 } , \quad } } & { { A _ { - 1 } = 1 , \quad A _ { 0 } = b _ { 0 } } } \\ { { B _ { k } = b _ { k } B _ { k - 1 } + a _ { k } B _ { k - 2 } , \quad } } & { { B _ { - 1 } = 0 , \quad B _ { 0 } = 1 } } \end{array}
$$

then

$$
{ \frac { A _ { n } } { B _ { n } } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| b _ { 1 } \right. } } + \ldots + { \frac { a _ { n } } { \left| b _ { n } \right. } } .
$$

Hint. Let $x = ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n + 1 } ) ^ { T }$ be the solution of $M x = ( 0 , \ldots , 0 , 1 ) ^ { T }$ ， where

$$
M = \left( \begin{array} { c c c c c c c } { { 1 } } & { { - b _ { 0 } } } & { { - a _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { - b _ { 1 } } } & { { - a _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - b _ { n - 1 } } } & { { - a _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { 1 } } & { { - b _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } & { { } } \end{array} \right) \ .
$$

One easily finds

$$
{ \frac { x _ { 0 } } { x _ { 1 } } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| x _ { 1 } / x _ { 2 } \right. } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| { b _ { 1 } } \right. } } + { \frac { a _ { 2 } } { \left| x _ { 2 } / x _ { 3 } \right. } } = \dots
$$

so that ${ x _ { 0 } } / { x _ { 1 } }$ is equal to the right hand side of (13.31). The statement now follows from the fact that

$$
\begin{array} { l } { { ( A _ { - 1 } , A _ { 0 } , \ldots , A _ { n } ) M = ( 1 , 0 , \ldots , 0 ) } } \\ { { ( B _ { - 1 } , B _ { 0 } , \ldots , B _ { n } ) M = ( 0 , 1 , 0 , \ldots , 0 ) . } } \end{array}
$$

implying $x _ { 0 } = A _ { n }$ and $x _ { 1 } = B _ { n }$

2. Let $P _ { s } ( z )$ be the Legendre polynomial (13.4) and $N _ { s } ^ { G } ( z )$ defined by the recursion (13.5) with $N _ { 0 } ^ { G } ( z ) = 0$ ， $N _ { 1 } ^ { G } ( z ) = 1$ . Prove that

$$
N _ { s - k } ^ { G } ( z ) P _ { s - k - 1 } ( z ) - N _ { s - k - 1 } ^ { G } ( z ) P _ { s - k } ( z ) = \tau _ { 1 } \cdot \tau _ { 2 } \cdot . . . \cdot \tau _ { s - k - 1 } .
$$

Hint. Use the relation

$$
\left( { \begin{array} { c c } { N _ { m } ^ { G } ( z ) } & { P _ { m } ( z ) } \\ { N _ { m - 1 } ^ { G } ( z ) } & { P _ { m - 1 } ( z ) } \end{array} } \right) = \left( { \begin{array} { c c } { z - \frac { 1 } { 2 } } & { - \tau _ { m - 1 } } \\ { 1 } & { 0 } \end{array} } \right) \left( { \begin{array} { c c } { N _ { m - 1 } ^ { G } ( z ) } & { P _ { m - 1 } ( z ) } \\ { N _ { m - 2 } ^ { G } ( z ) } & { P _ { m - 2 } ( z ) } \end{array} } \right) .
$$

3. Consider the Hermitian quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = b _ { 1 } f ( c _ { 1 } ) + \alpha f ( c _ { 2 } ) + \beta \frac { f ^ { \prime } ( c _ { 2 } ) } { 1 ! } + \gamma \frac { f ^ { \prime \prime } ( c _ { 2 } ) } { 2 ! } .
$$

Replace $f ^ { \prime } ( c _ { 2 } )$ and $f ^ { \prime \prime } ( c _ { 2 } )$ by finite divided differences based on $f ( c _ { 2 } - \varepsilon )$ ， $f ( c _ { 2 } ) , f ( c _ { 2 } + \varepsilon )$ to obtain a quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = \overline { { { b } } } _ { 1 } f ( c _ { 1 } ) + \overline { { { b } } } _ { 2 } f ( c _ { 2 } - \varepsilon ) + \overline { { { b } } } _ { 3 } f ( c _ { 2 } ) + \overline { { { b } } } _ { 4 } f ( c _ { 2 } + \varepsilon ) .
$$

a) Compute $Q ( z )$ for Formula(13.33) and obtain,by letting $\varepsilon \to 0$ , an expres-sion which generalizes (13.2) to Hermitian quadrature formulas.

b) Compute the values of $b _ { 1 }$ and $b _ { 2 }$ $( l _ { 1 } = 1 , l _ { 2 } = 3 )$ of (13.10').

c) Show that $n _ { + } - n _ { - }$ (see Theorem 13.5) is the same for (13.32) and (13.33) with $\varepsilon$ sufficiently small.

Results.

$$
\begin{array} { l l l } { \displaystyle Q ( z ) = \frac { b _ { 1 } } { z - c _ { 1 } } + \frac { \alpha } { z - c _ { 2 } } + \frac { \beta } { ( z - c _ { 2 } ) ^ { 2 } } + \frac { \gamma } { ( z - c _ { 2 } ) ^ { 3 } } } \\ { \displaystyle b _ { 1 } = b _ { 1 } \quad \mathrm { ( s i c ! ) } , \quad b _ { 2 } = \gamma / 3 ! . } \end{array}
$$

4.The rational function $\chi ( z ) = \alpha ( z ) / \beta ( z )$ with $\alpha ( z ) = z + \alpha _ { 1 }$ ， $\beta ( z ) = z ^ { 2 } +$ $\beta _ { 1 } z + \beta _ { 2 }$ is positive, iff $\alpha _ { 1 } \geq 0 , \quad \beta _ { 2 } \geq 0$ $\beta _ { 1 } - \alpha _ { 1 } \ge 0$ (compare (5.48))

a) Find real, symmetric and non-negative definite matrices $A$ and $B$ such that (13.25) holds.   
b） Show that these matrices are,in general, not unique.   
c） As in the proof of Lemma 13.19,compute the matrix $Q$ such that (13.24) holds. Hint. Begin with the construction of $B$ by putting $w = - z$ in (13.25).

# IV.14 Existence and Uniqueness of IRK Solutions

Jusqu'ä présent, nous avons supposé que le schéma admettait une solution. Pour en démontrer l'existence ... (Crouzeix & Raviart 1980)

Since contractivity without feasibility makes little sense .. (M.N. Spijker 1985)

Since the Runge-Kutta methods studied in the foregoing sections are all implicit, we have to ensure that the numerical solutions, for which we have derived so many nice results, also really exist. The existence theory for implicit Runge-Kutta methods, presented in Volume I(Theorem II.7.2), is for the non-stiff case only, where $h L$ is small( $I$ the Lipschitz constant). This is not a reasonable assumption for the stiff case.

We shallstudy the existence of a Runge-Kutta solution,defined implicitly by

$$
\begin{array} { l } { { g _ { i } = y _ { 0 } + \displaystyle h \sum _ { j = 1 } ^ { s } a _ { \iota _ { j } } f \big ( x _ { 0 } + c _ { j } h , g _ { \jmath } \big ) , \quad i = 1 , \dots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f \big ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } \big ) , } } \end{array}
$$

for differential equations which satisfy the one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 } .
$$

# Existence

It was first pointed out by Crouzeix & Raviart (198O) that the coercivity of the Runge-Kutta matrix $A$ (or of its inverse) plays an important role for the proof of existence.

Definition 14.1. We consider the inner product $\langle u , v \rangle _ { D } = u ^ { T } D v$ ，where $D =$ diag $( d _ { 1 } , \ldots , d _ { s } )$ with $d _ { \imath } > 0$ . We then denote by $\alpha _ { D } ( A ^ { - 1 } )$ the largest number $\alpha$ such that

$$
\begin{array} { r } { \langle u , A ^ { - 1 } u \rangle _ { D } \geq \alpha \langle u , u \rangle _ { D } \qquad \mathrm { f o r ~ a l l } \quad u \in \mathbb { R } ^ { s } . } \end{array}
$$

We also set

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { s u p } _ { D > 0 } \alpha _ { D } ( A ^ { - 1 } ) .
$$

The first existence results for the above problem were given by Crouzeix & Raviart (1980),Dekker (1982)and Crouzeix,Hundsdorfer & Spijker (1983). Their results can be summarized as follows:

Theorem 14.2. Let $f$ be continuously differentiable and satisfy (l4.2). If the Runge-Kutta matrix $A$ is invertible and

$$
h \nu < \alpha _ { 0 } ( A ^ { - 1 } )
$$

then the nonlinear system $( l 4 . l a )$ possesses a solution $( g _ { 1 } , \ldots , g _ { s } )$

Proof. The original proofs are based on the “uniform monotonicity theorem”or on similar results. We present here a more elementary version which, however, has the disadvantage of requiring the differentiability hypothesis for $f$ . The idea is to consider the homotopy

$$
g _ { \imath } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , g _ { \jmath } ) + ( \tau - 1 ) h \sum _ { \jmath = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , y _ { 0 } ) ,
$$

which is constructed in such a way that for $\tau = 0$ the system (14.6) has the solution $g _ { i } \simeq y _ { 0 }$ ,and for $\tau \simeq 1$ it is equivalent to (14.1a). We consider $g _ { \imath }$ as functions of $\tau$ and differentiate (14.6) with respect to this parameter. This gives

$$
{ \dot { g } } _ { i } = h \sum _ { j = 1 } ^ { s } a _ { i j } { \frac { \partial f } { \partial y } } ( x _ { 0 } + c _ { j } h , g _ { j } ) \cdot { \dot { g } } _ { j } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , y _ { 0 } )
$$

or equivalently

$$
\left( I - h ( A \otimes I ) \{ f _ { y } \} \right) \dot { g } = h ( A \otimes I ) f _ { 0 }
$$

where we have used the notations

$$
\dot { \boldsymbol g } = ( \dot { g } _ { 1 } , \dots , \dot { g } _ { s } ) ^ { T } , \qquad \boldsymbol f _ { 0 } = \big ( f ( \boldsymbol x _ { 0 } + c _ { 1 } h , y _ { 0 } ) , \dots , f ( \boldsymbol x _ { 0 } + c _ { s } h , y _ { 0 } ) \big ) ^ { T }
$$

(more precisely, $\dot { g }$ should be written as $( \dot { g } _ { 1 } ^ { T } , \dots , \dot { g } _ { s } ^ { T } ) ^ { T } )$ and

$$
\{ f _ { y } \} = \mathrm { b l o c k d i a g } \Big ( \frac { \partial f } { \partial y } \big ( x _ { 0 } + c _ { 1 } h , g _ { 1 } \big ) , \ . . . , \frac { \partial f } { \partial y } \big ( x _ { 0 } + c _ { s } h , g _ { s } \big ) \Big ) .
$$

In order to show that $\dot { g }$ can be expressed as ${ \dot { g } } = G ( g )$ with a globally bounded $G ( g )$ , we take a $D$ satisfying $h \nu < \alpha _ { D } ( A ^ { - 1 } )$ , multiply (14.7) by $\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I )$ and so obtain

$$
\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I ) \dot { g } - h \dot { g } ^ { T } ( D \otimes I ) \{ f _ { y } \} \dot { g } = h \dot { g } ^ { T } ( D \otimes I ) f _ { 0 } .
$$

We now estimate the three individual terms of this equation.

The estimate

$$
\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I ) \dot { g } \geq \alpha _ { D } ( A ^ { - 1 } ) \| \dot { g } \| _ { D } ^ { 2 } ,
$$

where we have introduced the notation $\| \dot { \boldsymbol { g } } \| _ { D } ^ { 2 } = \dot { g } ^ { T } ( D \otimes I ) \dot { \boldsymbol { g } }$ ,is (14.3) in the case of scalar differential equations (absence of $^ { 6 6 } \otimes I ^ { 5 7 } )$ . In the general case we must apply the ideas of Exercise 1 of Sect.IV.12 to the matrix ${ \scriptstyle { \frac { 1 } { 2 } } } ( D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } ) -$ $\alpha _ { D } ( A ^ { - 1 } ) D$ ，which is non-negative definite by Definition 14.1. It follows from (14.2) with $y = z + \varepsilon u$ that

$$
\left. \varepsilon \frac { \partial f } { \partial y } \left( x , z \right) u + o ( \varepsilon ) , \varepsilon u \right. \leq \nu \varepsilon ^ { 2 } \| u \| ^ { 2 } .
$$

Dividing by $\varepsilon ^ { 2 }$ and taking the limit $\varepsilon \to 0$ we obtain $\begin{array} { r } { \langle u , \frac { \partial f } { \partial y } ( x , z ) u \rangle \leq \nu \| u \| ^ { 2 } } \end{array}$ for all $( x , z )$ and all $u$ . Consequently we also have

$$
\dot { g } ^ { T } ( D \otimes I ) \{ f _ { y } \} \dot { g } \leq \nu \| \dot { g } \| _ { D } ^ { 2 } .
$$

The right-hand term of (14.8) is bounded by $h \| \dot { g } \| _ { D } \cdot \| f _ { 0 } \| _ { D }$ by the Cauchy-Schwarz-Bunjakowski inequality.

Inserting these three estimates into (14.8) yields

$$
\left( \alpha _ { D } ( A ^ { - 1 } ) - h \nu \right) \| | { \dot { g } } \| | _ { D } ^ { 2 } \leq h \| { \dot { g } } \| _ { D } \cdot \| | f _ { 0 } \| _ { D } .
$$

This proves that $\dot { g }$ can be written as ${ \dot { g } } = G ( g )$ with

$$
\| G ( g ) \| _ { D } \leq { \frac { h \| f _ { 0 } \| _ { D } } { \alpha _ { D } ( A ^ { - 1 } ) - h \nu } } .
$$

It now follows from Theorem 7.4 (Sect.I.7) that this differential equation with initial values $g _ { i } ( 0 ) = y _ { 0 }$ possesses a solution for all $\tau$ , in particular also for $\tau \simeq 1$ This proves the existence of a solution of (14.1a). □

Remark. It has recently been shown by Kraaijevanger & Schneid (1991, Theorem 2.12) that Condition (14.5) is “essentially optimal".

# A Counterexample

After our discussion that Monday afternoon (October 1980) I went for a walk and I got the idea for the counterexample.

(M.N. Spijker)

The inequality in (14.5) is strict, therefore Theorem 14.2 (together with Exercise 1 below) does not yet answer the simple question: “does a $B$ -stable method on a contractive problem $( \nu = 0 )$ always admit a solution". A first counterexample to this statement has been given by Crouzeix,Hundsdorfer & Spijker (1983). An easy idea for constructing another counterexample is to use the $W$ -transformation (see Sections IV.5 and IV.13) as follows:

We put $s \approx 4$ and take a quadrature formula with positive weights, say,

$$
( c _ { \imath } ) = ( 0 , 1 / 3 , 2 / 3 , 1 ) , ~ ( b _ { \imath } ) = ( 1 / 8 , 3 / 8 , 3 / 8 , 1 / 8 ) .
$$

We then construct a matrix $W$ satisfying property $T ( 1 , 1 )$ according to Lem-ma 5.12. This yields for the above quadrature formula

$$
W = \left( \begin{array} { c c c c } { { 1 } } & { { - \sqrt { 3 } } } & { { \sqrt { 3 } } } & { { - 1 } } \\ { { 1 } } & { { - \sqrt { 3 } / 3 } } & { { - \sqrt { 3 } / 3 } } & { { 1 } } \\ { { 1 } } & { { \sqrt { 3 } / 3 } } & { { - \sqrt { 3 } / 3 } } & { { - 1 } } \\ { { 1 } } & { { \sqrt { 3 } } } & { { \sqrt { 3 } } } & { { 1 } } \end{array} \right) .
$$

Finally, we put (with $\xi _ { 1 } = 1 / ( 2 \sqrt { 3 } ) )$

$$
\begin{array} { r } { A = W X W ^ { - 1 } \quad \mathrm { w i t h } \quad X = \left( \begin{array} { c c c c } { 1 / 2 } & { - \xi _ { 1 } } & { 0 } & { 0 } \\ { \xi _ { 1 } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \beta } \\ { 0 } & { 0 } & { \beta } & { 0 } \end{array} \right) . } \end{array}
$$

For $\beta = 1 / ( 4 \sqrt { 3 } )$ this gives nice rational coefficients for the RK-matrix,namely

$$
A = \frac { 1 } { 4 8 } \left( \begin{array} { c c c c } { { 3 } } & { { 0 } } & { { 3 } } & { { - 6 } } \\ { { 6 } } & { { 9 } } & { { 0 } } & { { 1 } } \\ { { 5 } } & { { 1 8 } } & { { 9 } } & { { 0 } } \\ { { 1 2 } } & { { 1 5 } } & { { 1 8 } } & { { 3 } } \end{array} \right) .
$$

It follows from Theorem 13.15 that this method is algebraically stable and of order 4. However,± $i \beta$ is an eigenvalue pair of $X$ and hence also of $A$ .

We thus choose the differential equation

$$
y ^ { \prime } = J y + f ( x ) \quad \mathrm { w i t h } \quad J = \left( { \begin{array} { c c } { 0 } & { - 1 / \beta } \\ { 1 / \beta } & { 0 } \end{array} } \right) ,
$$

which satisfies (14.2) with $\nu = 0$ independent of the choice of $f ( x )$ . If we apply the above method with $h \approx 1$ to this problem and initial values $x _ { 0 } = 0$ ， $y _ { 0 } = ( 0 , 0 ) ^ { T }$ ， Eq.(14.1a) becomes equivalent to the linear system

$$
( I - A \otimes J ) g = ( A \otimes I ) f _ { 0 } ,
$$

where $g = ( g _ { 1 } , \ldots , g _ { 4 } ) ^ { T }$ and $f _ { 0 } = ( f ( c _ { 1 } ) , \ldots , f ( c _ { 4 } ) ) ^ { T }$ . The matrix $\left( I - A \otimes J \right)$ is singular because the eigenvalues of $I - A \otimes J$ are just $1 - \lambda \mu$ where $\lambda$ and $\mu$ are the eigenvalues of $A$ and $J$ ,respectively. However, $A$ is regular, therefore it is possible to choose $f ( x )$ in such a way that this equation does not have a solution.

# Influence of Perturbations and Uniqueness

Our next problem is the question, how perturbations in the Runge-Kutta equations influence the numerical solution. Research into this problem was initiated independently by Frank, Schneid & Ueberhuber (preprint 1981, published 1985) and Dekker (1982).

As above, we use the notations

$$
\begin{array} { r l r } & { \| u \| _ { D } = \sqrt { u ^ { T } D u } = \sqrt { \langle u , u \rangle _ { D } } \quad } & { u \in \mathbb { R } ^ { s } } \\ & { \| g \| _ { D } = \sqrt { g ^ { T } ( D \otimes I ) g } \quad } & { g \in \mathbb { R } ^ { s n } } \end{array}
$$

and $\| A \| _ { D }$ for the corresponding matrix norm.

Theorem 14.3 (Dekker 1984). Let $g _ { i }$ and $y _ { 1 }$ be given by (14.1) and consider perturbed values $\widehat { g } _ { i }$ and $\widehat { y } _ { 1 }$ satisfying

$$
\begin{array} { l } { { \displaystyle { \widehat { g } } _ { i } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f \big ( x _ { 0 } + c _ { j } h , \widehat { g } _ { j } \big ) + \delta _ { i } } } \\ { { \displaystyle { \widehat { y } } _ { 1 } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } b _ { j } f \big ( x _ { 0 } + c _ { j } h , \widehat { g } _ { j } \big ) } . } \end{array}
$$

If the Runge-Kutta matrix $A$ is invertible,if the one-sided Lipschitz condition(14.2) is satisfied, and $h \nu < \alpha _ { D } ( A ^ { - 1 } )$ for some positive diagonal matrix $D$ , then we have the estimates

$$
\begin{array} { r l } & { \left\| \left. \widehat { g } - g \right. \right\| _ { D } \leq \frac { \left\| A ^ { - 1 } \right\| _ { D } } { \alpha _ { D } \left( A ^ { - 1 } \right) - h \nu } \left\| \delta \right\| _ { D } } \\ & { \left\| \widehat { y } _ { 1 } - y _ { 1 } \right\| \leq \| b ^ { T } A ^ { - 1 } \| _ { D } \Bigg ( 1 + \frac { \left\| A ^ { - 1 } \right\| _ { D } } { \alpha _ { D } \left( A ^ { - 1 } \right) - h \nu } \Bigg ) \left\| \left. \delta \right. \right\| _ { D } , } \end{array}
$$

$$
g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T } , { \widehat { g } } = ( { \widehat { g } } _ { 1 } , \ldots , { \widehat { g } } _ { s } ) ^ { T } , a n d \delta = ( \delta _ { 1 } , \ldots , \delta _ { s } ) ^ { T } .
$$

Proof. With the notation $\Delta g = \widehat { g } - g$ and

$$
\Delta f = \left( f ( x _ { 0 } + c _ { 1 } h , \widehat g _ { 1 } ) - f ( x _ { 0 } + c _ { 1 } h , g _ { 1 } ) , \ldots , f ( x _ { 0 } + c _ { s } h , \widehat g _ { s } ) - f ( x _ { 0 } + c _ { s } h , g _ { s } ) \right) ^ { T }
$$

the difference of (14.11a) and (14.1a) can be written as

$$
\Delta g = h ( A \otimes I ) \Delta f + \delta .
$$

As in the proof of Theorem 14.2 we multiply this equation by $\Delta g ^ { T } ( D A ^ { - 1 } \otimes I )$ and obtain

$$
\Delta g ^ { T } ( D A ^ { - 1 } \otimes I ) \Delta g - h \Delta g ^ { T } ( D \otimes I ) \Delta f = \Delta g ^ { T } ( D A ^ { - 1 } \otimes I ) \delta .
$$

This equation is very similar to Eq.(14.8) and we estimate it in the same way: since $D$ is a diagonal matrix with positive entries,it follows from (14.2) that

$$
\Delta g ^ { T } ( D \otimes I ) \Delta f \leq \nu \| \Delta g \| _ { D } ^ { 2 } .
$$

Inserting (14.15) and (14.9) (with $\dot { g }$ replaced by $\Delta g$ ） into (14.14) we get

$$
\left( \alpha _ { D } ( A ^ { - 1 } ) - h \nu \right) \| | \Delta g \| | _ { D } ^ { 2 } \leq \| \Delta g \| _ { D } \| | ( A ^ { - 1 } \otimes I ) \delta \| _ { D }
$$

which implies (14.12). The estimate (14.13) then follows immediately from

$$
\begin{array} { r } { \widehat { y } _ { 1 } - y _ { 1 } = h ( \boldsymbol { b } ^ { T } \otimes I ) \Delta f = ( \boldsymbol { b } ^ { T } A ^ { - 1 } \otimes I ) ( \Delta g - \delta ) . } \end{array}
$$

Putting $\delta \simeq 0$ in Theorem 14.3 we get the following uniqueness result.

Theorem 14.4. Consider a differential equation satisfying (14.2). If the Runge-Kutta matrix $A$ is invertible and $h \nu < \alpha _ { 0 } ( A ^ { - 1 } )$ , then the system $( l 4 . l a )$ possesses at most one solution. □

# Computation of $\alpha _ { 0 } ( A ^ { - 1 } )$

... the determination of a suitable matrix $D$ ... This task does not seem easy at first glance ... (K.Dekker 1984)

The value $\alpha _ { D } ( A ^ { - 1 } )$ of Definition 14.1 is the smallest eigenvalue of the symmetric matrix $\left( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } + ( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } ) ^ { T } \right) / 2$ .The computation of $\alpha _ { 0 } ( A ^ { - 1 } )$ is more difficult, because the optimal $D$ is not known in general.

An upper bound for $\alpha _ { 0 } \big ( A ^ { - 1 } \big )$ is

$$
\alpha _ { 0 } ( A ^ { - 1 } ) \leq \operatorname* { m i n } _ { i = 1 , \ldots , s } \omega _ { \ i i }
$$

where $\omega _ { \imath j }$ are the entries of $A ^ { - 1 }$ . This follows from (14.3) by putting $u \approx e _ { i }$ ,the $i$ th unit vector.

Lower bounds for $\alpha _ { 0 } ( A ^ { - 1 } )$ were first given by Frank, Schneid & Ueberhuber in 1981. Following are the exact values due to Dekker (1984), Dekker & Verwer (1984, p.55-164),and Dekker & Hairer (1985) (see also Liu & Kraaijevanger 1988 and Kraaijevanger & Schneid 1991).

Theorem 14.5. For the methods of Sect. IV.5 we have:

<table><tr><td>Gauss</td><td>α(A-1)=.min</td><td>i=m,， 2c(1-c）</td><td>1</td></tr><tr><td>Radau IA</td><td>α0(A-1)=</td><td>1 1 2（1-c2）</td><td>if s=1, if s&gt;1,</td></tr><tr><td>Radau IA</td><td>α0(A-1) =</td><td>（1 1 2cg-1</td><td>if s=1, if s&gt;1,</td></tr><tr><td>Lobatto IIIC</td><td></td><td></td><td>if s= 2, if s &gt;2.</td></tr></table>

Proof. a) Gauss methods: written out in “symmetricized form”,estimate (14.3) reads

$$
\frac { 1 } { 2 } u ^ { T } \big ( D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } \big ) u \geq \alpha u ^ { T } D u .
$$

Evidently the sharpest estimates come out if $D$ is such that the left-hand matrix is as “close to diagonal as possble". After many numerical computations, Dekker had the nice surprise that with the choice $D = B ( C ^ { - 1 } - I )$ ，where $B =$ diag $\left( b _ { 1 } , \ldots , b _ { s } \right)$ and $C = \operatorname { d i a g } \left( c _ { 1 } , \ldots , c _ { s } \right)$ , the matrix

$$
D A ^ { - 1 } + \left( D A ^ { - 1 } \right) ^ { T } = B C ^ { - 2 }
$$

becomes completely diagonal. Then the optimal $\alpha$ is simply obtained by testing the unit vectors $u \simeq e _ { k }$ ,which gives

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { m i n } _ { i } { \frac { b _ { i } } { 2 c _ { i } ^ { 2 } d _ { i } } } = \operatorname* { m i n } _ { i } { \frac { b _ { i } } { 2 c _ { i } ^ { 2 } b _ { i } ( 1 / c _ { i } - 1 ) } } = \operatorname* { m i n } _ { i } { \frac { 1 } { 2 c _ { i } ( 1 - c _ { i } ) } } .
$$

It remains to prove (14.17): we verify the equivalent formula

$$
V ^ { T } ( A ^ { T } D + D A - A ^ { T } B C ^ { - 2 } A ) V = 0
$$

where $V = ( c _ { \imath } ^ { \jmath - 1 } )$ is the Vandermonde matrix. The $( l , m )$ -element of the matrix (14.18) is

$$
\begin{array} { r } { \displaystyle \sum _ { \imath , \jmath } b _ { \jmath } \Big ( \frac { 1 } { c _ { j } } - 1 \Big ) a _ { \jmath i } c _ { \imath } ^ { l - 1 } c _ { \jmath } ^ { m - 1 } + \displaystyle \sum _ { \imath , j } b _ { \imath } \Big ( \frac { 1 } { c _ { \imath } } - 1 \Big ) a _ { \imath j } c _ { i } ^ { l - 1 } c _ { \jmath } ^ { m - 1 } } \\ { - \displaystyle \sum _ { \imath , \jmath , k } b _ { \imath } \frac { 1 } { c _ { \imath } ^ { 2 } } a _ { \imath k } c _ { k } ^ { l - 1 } a _ { \imath j } c _ { \jmath } ^ { m - 1 } . } \end{array}
$$

With the help of the simplifying assumptions $C ( s )$ and $B ( 2 s )$ the expression (14.19) can be seen to be zero.

b) For the Radau IA methods we take $D = B ( I - C )$ and show that

$$
D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } = B + e _ { 1 } e _ { 1 } ^ { T } .
$$

The stated formula for $\alpha _ { 0 } ( A ^ { - 1 } )$ then follows from $0 = c _ { 1 } < c _ { 2 } < . . . < c _ { s }$ and from

$$
{ \frac { b _ { 1 } + 1 } { b _ { 1 } } } \geq { \frac { 1 } { 1 - c _ { 2 } } } ,
$$

which is a simple consequence of $b _ { 1 } = 1 / s ^ { 2 }$ (see Abramowitz & Stegun (1964), Formula 25.4.31). For the verification of (14.20) one shows that $V ^ { T } ( D A ^ { - 1 } +$ $( D A ^ { - 1 } ) ^ { T } - B - e _ { 1 } e _ { 1 } ^ { T } ) V = 0$ . Helpful formulas for this verification are $A ^ { - 1 } V e _ { 1 } =$ $b _ { 1 } ^ { - 1 } e _ { 1 }$ ， $V ^ { T } e _ { 1 } = e _ { 1 }$ and $A ^ { - 1 } V e _ { \jmath } = ( j - 1 ) V e _ { \jmath - 1 }$ for $j \geq 2$

c) Similarly, the statement for the Radau IIA methods follows with $D = B C ^ { - 1 }$ from the identity

$$
D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } = B C ^ { - 2 } + e _ { s } e _ { s } ^ { T } .
$$

d) As in part (b) one proves for the Lobatto IIIC methods that

$$
\boldsymbol { B A } ^ { - 1 } + ( \boldsymbol { B A } ^ { - 1 } ) ^ { T } = \boldsymbol { e } _ { 1 } \boldsymbol { e } _ { 1 } ^ { T } + \boldsymbol { e } _ { s } \boldsymbol { e } _ { s } ^ { T } .
$$

Since this matrix is diagonal, we obtain $\alpha _ { 0 } ( A ^ { - 1 } ) = 1$ for $s \approx 2$ and $\alpha _ { 0 } { \left( A ^ { - 1 } \right) } = 0$ for $s > 2$ . □

For diagonally implicit Runge-Kuta methods we have the following result.

Theorem 14.6 (Montijano 1983). For a DIRK-method with positive $a _ { \ i i } \ m e$ have

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { m i n } _ { \imath = 1 , \imath \to \imath } \frac { 1 } { a _ { \imath i } } .
$$

Proof. With $D = \operatorname { d i a g } \left( 1 , \varepsilon ^ { 2 } , \varepsilon ^ { 4 } , \dots , \varepsilon ^ { 2 s - 2 } \right)$ we obtain

$$
D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } + ( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } ) ^ { T } = \mathrm { d i a g } ( a _ { 1 1 } ^ { - 1 } , \ldots , a _ { s s } ^ { - 1 } ) + { \mathcal O } ( { \varepsilon } ) ,
$$

so that $\alpha _ { 0 } ( A ^ { - 1 } ) \geq \operatorname* { m i n } _ { \ i } a _ { i \ i } ^ { - 1 } + { \mathcal { O } } ( \varepsilon )$ . This inequality for $\varepsilon \to 0$ and (14.16) prove the statement. □

# Methods with Singular $\mathbf { A }$

For the Lobatto IIIA methods the first stage is explicit (the first row of $A$ vanishes) and for the Lobatto IIB methods the last stage is explicit (the last column of $A$ vanishes). For these methods the Runge-Kutta matrix is of the form

$$
A = \left( \begin{array} { l l } { { 0 } } & { { 0 } } \\ { { a } } & { { \widetilde { A } } } \end{array} \right) \qquad \mathrm { o r } \qquad A = \left( \begin{array} { l l } { { \widetilde { A } } } & { { 0 } } \\ { { a ^ { T } } } & { { 0 } } \end{array} \right)
$$

and we have the following variant of Theorem 14.2.

Theorem 14.7． Let $f$ be continuously differentiable and satisfy (14.2). If the Runge-Kutta matrix is given by one of the matrices in (14.23) with invertible $\widetilde { A }$ ， then the assumption

$$
h \nu < \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } )
$$

implies that the nonlinear system $( l 4 . l a )$ has a solution.

Proof. The explicit stage poses no problem for the existence of a solution. To obtain the result we repeat the proof of Theorem 14.2 for the $s - 1$ implicit stages (i.e., $A$ is replaced by $\widetilde { A }$ and the inhomogenity in (14.6) may be different). □

An explicit formula for $\alpha _ { 0 } { \big ( } { \overset { \sim } { A } } ^ { - 1 } { \big ) }$ for the Lobatto IIIB methods has been given by Dekker & Verwer (1984),and for the Lobatto IIIA methods by Liu,Dekker & Spijker (1987). The result is

Theorem 14.8. We have for

$$
\begin{array} { r l } & { \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } ) = \left\{ \begin{array} { l l } { 2 \quad \quad \quad } & { i f s = 2 , } \\ { c _ { s - 1 } ^ { - 1 } \quad \quad } & { i f s > 2 , } \end{array} \right. } \\ & { \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } ) = \left\{ \begin{array} { l l } { 2 \quad \quad } & { i f s = 2 , } \\ { ( 1 - c _ { 2 } ) ^ { - 1 } \quad \quad } & { i f s > 2 . } \end{array} \right. } \end{array}
$$

Proof. For the Lobatto IIA methods we put $D = \widetilde { B } \widetilde { C } ^ { - 2 }$ with the diagonal matrices $\widetilde { \boldsymbol B } = \mathrm { d i a g } \left( \boldsymbol b _ { 2 } , \dots , \boldsymbol b _ { s } \right)$ and $\widetilde { C } = \mathrm { d i a g } \left( \bar { c _ { 2 } } , \dots , c _ { s } \right)$ . As in part (a) of the proof of Theorem 14.5 we get

$$
D \widetilde { A } ^ { - 1 } + ( D \widetilde { A } ^ { - 1 } ) ^ { T } = e _ { s - 1 } e _ { s - 1 } ^ { T } + 2 \widetilde { B } \widetilde { C } ^ { - 3 }
$$

which implies the formula for $\alpha _ { 0 } ( \stackrel { \sim } { A } ^ { - 1 } )$ ， because $b _ { \pmb { s } } = ( \pmb { s } ( \pmb { s } - 1 ) ) ^ { - 1 }$ and $( 1 +$ $2 b _ { s } ) \geq b _ { s } / c _ { s - 1 }$ for $s > 2$

For the Lobatto IB methods the choice $D = \widetilde { B } ( I - \widetilde { C } ) ^ { 2 }$ (with the matrices $\widetilde { B } = \mathrm { d i a g } \left( b _ { 1 } , \ldots , b _ { s - 1 } \right)$ ， $\widetilde { C } = \mathrm { d i a g } \left( c _ { 1 } , \dots , c _ { s - 1 } \right) )$ leads to

$$
D \widetilde { A } ^ { - 1 } + ( D \widetilde { A } ^ { - 1 } ) ^ { T } = e _ { 1 } e _ { 1 } ^ { T } + 2 \widetilde { B } ( I - \widetilde { C } ) .
$$

This proves the second statement.

Methods with explicit stages (such as Lobatto IIIA and IIB) don't allow estimates of the numerical solution in the presence of arbitrary perturbations. They are usually not $A N$ -stable and $K ( Z )$ is not bounded (see Theorem 12.12). Nevertheless we have the following uniqueness result.

Theorem 14.9. Consider a differential equation satisfying (14.2). If the Runge-Kutta matrix is of the form (14.23) with invertible $\widetilde { A }$ and if $h \nu < \alpha _ { 0 } \big ( \widetilde { A } ^ { - 1 } \big )$ ，then the nonlinear system $( l 4 . l a )$ has at most one solution.

Proof. Suppose, there exists a second solution ${ \widehat { g } } _ { \imath }$ satisfying (14.11a) with $\delta _ { \imath } = 0$ . a) If the first stage is explicit we have $\widehat { g } _ { 1 } = g _ { 1 }$ . The difference of the two Runge-Kutta formulas then yields

$$
\Delta g = h ( \widetilde { A } \otimes I ) \Delta f
$$

with $\Delta g = ( \widehat { g } _ { \imath } - g _ { \imath } ) _ { \imath = 2 } ^ { s }$ and $\Delta f = ( f ( x _ { 0 } + c _ { \imath } h , \widehat { g } _ { \imath } ) - f ( x _ { 0 } + c _ { \imath } h , g _ { \imath } ) ) _ { \imath = 2 } ^ { s }$ . As in the proof of Theorem 14.3 we then conclude that $\Delta g = 0$

b) In the second case we can apply Theorem 14.3 to the first $s - 1$ stages, which yields uniqueness of $g _ { 1 } , \ldots , g _ { s - 1 }$ . Clearly, $g _ { s }$ also is unique, because the last stage is explicit. □

# Lobatto IIC Methods

For the Lobatto IIIC methods with $s \geq 3$ we have $\alpha _ { 0 } \big ( A ^ { - 1 } \big ) = 0$ (see Theorem 14.5). Since these methods are algebraically stable it is natural to ask whether the non-linear system (14.1a) also has a solution for differential equations satisfying (14.2) with $\nu = 0$ ． A positive answer to this question has been given by Hundsdorfer & Spijker (1987) for the case $s = 3$ , and by Liu & Kraaijevanger (1988) for the general case $s \geq 3$ (see Exercise 6 below; see also Kraaijevanger & Schneid 1991).

# Exercises

1. Prove that $\alpha _ { 0 } ( A ) \geq 0$ for algebraically stable Runge-Kutta methods. Also, $\alpha _ { 0 } ( A ^ { - 1 } ) \geq 0$ if in addition the matrix $A$ is invertible.

2.Let $A$ be a real matrix. Show that $\alpha _ { 0 } ( A ) \leq \operatorname { R e } \lambda$ ,where $\lambda$ is an eigenvalue of $A$

3. (Hundsdorfer 1985,Cooper 1986). Prove that Theorem 14.2 remains valid for singular $A$ ,if $h \nu < \alpha$ with $\alpha$ satisfying

$$
\langle u , A u \rangle _ { D } \geq \alpha \langle A u , A u \rangle _ { D } \qquad { \mathrm { f o r ~ a l l } } \quad u \in \mathbb { R } ^ { s } .
$$

Hint. Use the transformation $g = \mathbb { 1 } \otimes y _ { 0 } + ( A \otimes I ) k$ and apply the ideas of the proof of Theorem 14.2 to the homotopy

$$
k _ { i } = f ( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum _ { \jmath = 1 } ^ { \ s } a _ { \imath j } k _ { j } ) + ( \tau - 1 ) f ( x _ { 0 } + c _ { i } h , y _ { 0 } ) .
$$

4. (Barker, Berman & Plemmons 1978, Montijano 1983). Prove that for any twostage method the condition

$$
a _ { 1 1 } > 0 , \qquad a _ { 2 2 } > 0 , \qquad \operatorname* { d e t } ( A ) > 0
$$

is equivalent to $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$

Remark. For a generalization of this result to three-stage methods see Kraaijevanger (1991).

5.For the two-stage Radau IIA method we have $\alpha _ { 0 } ( A ^ { - 1 } ) = 3 / 2$ . Construct a differential equation $y ^ { \prime } = \lambda ( x ) y$ with $\operatorname { R e } \lambda ( x ) = 3 / 2 + \varepsilon$ $\vert \varepsilon > 0$ arbitrarily small) such that the Runge-Kutta equations do not admit a unique solution for all $h > 0$

6. Prove that for the Lobatto IIIC methods (with $s \geq 3$ ） the matrix

$$
I - ( A \otimes I ) J \quad { \mathrm { w i t h } } \quad J = { \mathrm { b l o c k d i a g } } \left( J _ { 1 } , \dots , J _ { s } \right)
$$

is non-singular, if $\mu _ { 2 } ( J _ { k } ) \leq 0$ . This implies that the Runge-Kutta equations (14.1a) have a unique solution for all problems $y ^ { \prime } = A ( x ) y + f ( x )$ with $\mu _ { 2 } ( A ( x ) ) \leq 0$

Hint (Liu & Kraaijevanger 1988,Liu,Dekker & Spijker 1987).Let $v =$ $( v _ { 1 } , \ldots , v _ { s } ) ^ { T }$ be a solution of $( I - ( A \otimes I ) J ) v = 0$ . With the help of (14.21) show first that $v _ { 1 } = v _ { s } = 0$ . Then consider the $\left( s - 2 \right)$ -dimensional submatrix $\widetilde { A } = ( a _ { i j } ) _ { i , \jmath = 2 } ^ { s - 1 }$ and prove $\alpha _ { 0 } \big ( \widetilde { A } ^ { - 1 } \big ) > 0$ byconsideringthediagoalmatrix $\widetilde { D } =$ diag $\ ( b _ { \ i } ( c _ { i } ^ { - 1 } - 1 ) ^ { 2 } ) _ { i = 2 } ^ { s - 1 }$

7. Consider an algebraically stable Runge-Kutta method with invertible $A$ and apply it to the differential equation $y ^ { \prime } { = } ( J ( x ) { - } \varepsilon I ) y + f ( x )$ where $\mu ( J ( x ) ) \leq$ $0$ and $\varepsilon > 0$ . Prove that the numerical solution $y _ { 1 } \left( \varepsilon \right)$ converges to a limit for $\varepsilon \to 0$ , whereas the internal stages $g _ { \imath } ( \varepsilon )$ need not converge.

Hint. Expand the $g _ { \imath } ( \varepsilon )$ in a series $g _ { i } ( \varepsilon ) = \varepsilon ^ { - 1 } g _ { i } ^ { ( - 1 ) } + g _ { i } ^ { ( 0 ) } + \varepsilon g _ { \imath } ^ { ( 1 ) } + \ldots .$ and prove the implication

$$
\begin{array} { c } { { g = \left( A \otimes I \right) J g \quad \Longrightarrow \quad ( b ^ { T } \otimes I ) J g = 0 } } \\ { { \mid = \mathrm { b l o c k d i a g } \left( J ( x _ { 0 } + c _ { 1 } h ) , \ldots , J ( x _ { 0 } + c _ { s } h ) \right) . } } \end{array}
$$

In using $A$ -stable one-step methods to solve large systems of stiff nonlinear differential equations, we have found that - (a) some $A$ -stable methods give highly unstable solutions,and 一 (b) the accuracy of the solutions obtained when the equations are stiff often appears to be unrelated to the order of the method used.

This has caused us to re-examine the form of stability required when stiff systems of equations are solved,and to question the relevance of the concept of (nonstiff) order of accuracy for stiff problems. (A.Prothero & A.Robinson 1974)

Prothero & Robinson (1974) were the first to discover the order reduction of implicit Runge-Kutta methods when applied to stiff differential equations. Frank, Schneid & Ueberhuber(1981) then introduced the “concept of $B$ -convergence", which furnishes global error estimates independent of the stiffness.

# The Order Reduction Phenomenon

For the study of the accuracy of Runge-Kutta methods applied to stiff differential equations, Prothero & Robinson (1974) proposed considering the problem

$$
y ^ { \prime } = \lambda { \bigl ( } y - \varphi ( x ) { \bigr ) } + \varphi ^ { \prime } ( x ) , \qquad y ( x _ { 0 } ) = \varphi ( x _ { 0 } ) , \qquad { \mathrm { R e ~ } } \lambda \leq 0 .
$$

This allows explicit formulas for the local and global errors and provides much new insight.

Applying a Runge-Kutta method to (15.1) yields

$$
\begin{array} { l } { { g _ { i } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i _ { j } } \left( \lambda \big ( g _ { \jmath } - \varphi ( x _ { 0 } + c _ { j } h ) \big ) + \varphi ^ { \prime } \big ( x _ { 0 } + c _ { j } h \big ) \right) } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \left( \lambda \big ( g _ { \jmath } - \varphi ( x _ { 0 } + c _ { j } h ) \big ) + \varphi ^ { \prime } \big ( x _ { 0 } + c _ { j } h \big ) \right) } . } \end{array}
$$

If we replace here the $g _ { \imath } , y _ { 0 }$ and $y _ { 1 }$ by the exact solution values $\varphi ( x _ { 0 } + c _ { \iota } h )$ ， $\varphi ( x _ { 0 } )$ and $\varphi ( x _ { 0 } + h )$ , respectively, we obtain a defect which is given by

$$
\begin{array} { r } { \varphi ( x _ { 0 } + c _ { \iota } h ) = \varphi ( x _ { 0 } ) + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { i j } \varphi ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) + \Delta _ { i , h } ( x _ { 0 } ) } \\ { \varphi ( x _ { 0 } + h ) = \varphi ( x _ { 0 } ) + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { j } \varphi ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) + \Delta _ { 0 , h } ( x _ { 0 } ) . } \end{array}
$$

Taylor series expansion of the functions in (15.3) shows that

$$
\Delta _ { 0 , h } ( x _ { 0 } ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad \Delta _ { \iota , h } ( x _ { 0 } ) = \mathcal { O } ( h ^ { q + 1 } ) ,
$$

where $p$ is the order of the quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right)$ and $q$ is the largest number such that the condition $C ( q )$ (see Sect. IV.5), i.e.,

$$
\sum _ { \jmath = 1 } ^ { s } a _ { \imath j } c _ { \jmath } ^ { k - 1 } = \frac { c _ { \imath } ^ { k } } { k } \qquad \mathrm { f o r } \quad k = 1 , \dots , q \quad \mathrm { a n d ~ a l l } \quad \imath ,
$$

holds. The minimum of $q$ and $p$ is often called the stage order of the Runge-Kutta method. Subtracting (15.3) from (15.2) and eliminating the internal stages we get

$$
y _ { 1 } - \varphi ( x _ { 0 } + h ) = R ( z ) ( y _ { 0 } - \varphi ( x _ { 0 } ) ) - z b ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x _ { 0 } ) - \Delta _ { 0 , h } ( x _ { 0 } )
$$

where we have used the notation $z \approx \lambda h$ ， $R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 }$ for the stability function and $\Delta _ { h } ( x ) = ( \Delta _ { 1 , h } ( x ) , \dots , \Delta _ { s , h } ( x ) ) ^ { T }$ . We also denote the local error, which we get from(15.6) on putting $y _ { 0 } = \varphi ( x _ { 0 } )$ ,by

$$
\delta _ { h } ( x ) = - z b ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x ) - \Delta _ { 0 , h } ( x ) .
$$

If we repeat the above calculation with $x _ { n }$ instead of $x _ { 0 }$ we obtain the recursion

$$
y _ { n + 1 } - \varphi ( x _ { n + 1 } ) = R ( z ) ( y _ { n } - \varphi ( x _ { n } ) ) + \delta _ { h } ( x _ { n } )
$$

which leads to the following formula for the global error

$$
y _ { n + 1 } - \varphi ( x _ { n + 1 } ) = R ( z ) ^ { n + 1 } { \bigl ( } y _ { 0 } - \varphi ( x _ { 0 } ) { \bigr ) } + \sum _ { \jmath = 0 } ^ { n } R ( z ) ^ { n - \jmath } \delta _ { h } ( x _ { \jmath } ) .
$$

The classical (non-stiff) theory treats the case where $z = \mathcal { O } ( h )$ and in this situation the global error behaves like $\mathcal { O } ( h ^ { p } )$ .When solving stiff differential equations one is interested in step sizes $h$ which are much larger than $| \lambda | ^ { - 1 }$ . We therefore study the global error (15.9) under the assumption that simultaneously $h  0$ and $z = \lambda h  \infty$ . In Table 15.1 we collect the results for the Runge-Kutta methods of Sect.IV.5. There in the last column (variable $h$ ) the symbols $h$ and $z$ have to be interpreted as max $h _ { \iota }$ and $z = \lambda \operatorname* { m i n } h _ { \iota }$ . We remark that Formulas (15.7) and (15.8) (but not (15.9)) remain valid for variable $h$ ,if $z$ is replaced by $z _ { n } = h _ { n } \lambda$

Table 15.1. Error for (15.1） when $h  0$ and $z = h \lambda \to \infty$   

<table><tr><td colspan="2">Method</td><td>local error</td><td colspan="2">global error</td></tr><tr><td colspan="2">odd</td><td></td><td>constant h {h8+1</td><td>variable h</td></tr><tr><td colspan="2">s Gauss even s</td><td>h8+1</td><td>h</td><td>h</td></tr><tr><td colspan="2">Radau IA</td><td>h</td><td>h</td><td>h</td></tr><tr><td colspan="2">Radau IA odd</td><td>x-1h8+1</td><td>z-1h8+1 {x-1h8</td><td>z-1h8+1</td></tr><tr><td colspan="2">Lobatto IIIA s s even</td><td>x-1h8+1</td><td>z-1h8+1</td><td>x-1h8</td></tr><tr><td rowspan="3">LobattoIIIB s</td><td>odd S</td><td>zh8-2 zh8-1</td><td></td><td>zh8-2</td></tr><tr><td>even</td><td>zh-1</td><td></td><td></td></tr><tr><td>x-1h</td><td>x-1h8</td><td></td><td>x-1hg</td></tr></table>

# Verification of Table 15.1.

Gauss. Since the Runge-Kutta matrix $A$ is invertible, we have $- z b ^ { T } ( I - z A ) ^ { - 1 } =$ $b ^ { T } A ^ { - 1 } + { \mathcal { O } } ( z ^ { - 1 } )$ and (15.4) inserted into (15.7) gives $\begin{array} { r } { \boldsymbol { \mathcal { S } } _ { h } \left( \boldsymbol { x } \right) = \boldsymbol { \mathcal { O } } ( h ^ { s + 1 } ) } \end{array}$ (observe that $q = s$ ). It then follows from (15.8) (for constant and variable $h$ ) that the global error behaves like $\mathcal { O } ( h ^ { s } )$ because $| R ( z ) | \le 1$ . For odd $s$ we have $R ( \infty ) = - 1$ and the global error estimate can be improved in the case of constant step sizes. This follows from partial summation

$$
\sum _ { p = 0 } ^ { n } \varrho ^ { n - \jmath } \delta ( x _ { \jmath } ) = { \frac { 1 - \varrho ^ { n + 1 } } { 1 - \varrho } } \delta ( x _ { 0 } ) + \sum _ { \jmath = 1 } ^ { n } { \frac { 1 - \varrho ^ { n + 1 - \jmath } } { 1 - \varrho } } \big ( \delta ( x _ { \jmath } ) - \delta ( x _ { \jmath - 1 } ) \big )
$$

of the sum in (15.9) and from the fact that $\delta _ { h } ( x _ { \jmath } ) - \delta _ { h } ( x _ { \jmath - 1 } ) = { \mathcal O } ( h ^ { q + 2 } ) .$

Radau IA. The local error estimate follows in the same way as for the Gauss methods. Since $R ( z ) = \mathcal { O } ( z ^ { - 1 } )$ the error propagation in (15.8) is negligible and the local and global errors have the same asymptotic behaviour.

Radau IIA and Lobatto IIIC. These methods have $a _ { s _ { 2 } } = b _ { \iota }$ for all $i$ . Therefore the last internal stage is identical to the numerical solution and the local error can be written as

$$
\delta _ { h } ( x ) = - e _ { s } ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x ) .
$$

Since $A$ is invertible this formula shows the presence of $z ^ { - 1 }$ in the local error. Again we have $R ( \infty ) = 0$ , so that the global error is essentially cqual to the local error.

Lobatto IIIA. The first stage is explicit, $g _ { 1 } = y _ { 0 }$ ,and is done without introducing an error. Therefore $\Delta _ { 1 , h } ( x ) = 0$ and (because of $a _ { s _ { 1 } } = b _ { _ { 2 } }$ ） the local error has the form

$$
\delta _ { h } ( x ) = - e _ { s - 1 } ^ { T } ( I - z \widetilde { A } ) ^ { - 1 } \widetilde { \Delta } _ { h } ( x )
$$

where $\stackrel { \sim } { A } = ( a _ { \iota \jmath } ) _ { \iota , \jmath = 2 } ^ { \mathfrak { s } }$ and $\widetilde { \Delta } _ { h } = ( \Delta _ { 2 , h } , \ldots , \Delta _ { s , h } ) ^ { T }$ . The statements of Table 15.1 now follow as for the Gauss methods.

Lobatto IB. The matrix $A$ is singular (its last column vanishes), therefore the two" $z ^ { \dprime }$ in (15.7) do not simply cancel for $z  \infty$ . A more detailed analysis (see Exercise 5 below） shows that the local error is not bounded if $z  \infty$ .Although $A$ -stable, these methods are not suited for the solution of stiff problems. □

We observe from Table 15.l that the order of convergence for problem (15.1) with large $\lambda$ is considerably smaller than the classical order. Further we see that methods satisfying $a _ { s _ { 2 } } = b _ { \ i }$ (Radau IIA, Lobatto IIIA and Lobatto IIIC) give an asymptotically exact result for $z  \infty$ ．Prothero & Robinson（1974） call such methods stiffly accurate. The importance of this condition will appear again when we treat singularly perturbed and differential-algebraic problems (Chapter VI).

# The Local Error

Das besondere Schmerzenskind sind die Fehlerabschatzungen.

(L. Collatz 1950)

Our next aim is to extend the above results to general nonlinear differential equations $y \prime = f ( x , y )$ satisfying a one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 } .
$$

The following analysis,begun by Frank, Schneid & Ueberhuber (1981), was elaborated by Frank, Schneid & Ueberhuber (1985) and Dekker & Verwer (1984). We again denote the local error by

$$
\delta _ { h } ( x ) = y _ { 1 } - y ( x + h ) ,
$$

where $y _ { 1 }$ is the numerical solution with initial value $y _ { 0 } = y ( x )$ on the exact solution.

Proposition 15.1. Consider a differential equation which satisfies (15.11). Assume that the Runge-Kutta matrix $A$ is invertible, $\alpha _ { 0 } ( A ^ { - 1 } ) \geq 0$ (see Definition $I 4 . I )$ ， and that the stage order is $q$

$a \mathrm { , }$ 1f $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ then

$$
\| \delta _ { h } ( x ) \| \leq C h ^ { q + 1 } \operatorname* { m a x } _ { \xi \in [ x , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| \quad f o r \quad h \nu \leq \alpha < \alpha _ { 0 } ( A ^ { - 1 } ) .
$$

$b _ { . }$ ）If $\alpha _ { D } ( A ^ { - 1 } ) = 0$ for some positive diagonal matrix $D$ and $\nu < 0$ then

$$
\| \delta _ { h } ( x ) \| \leq C \Big ( h + \frac { 1 } { | \nu | } \Big ) h ^ { q } \operatorname* { m a x } _ { \xi \in [ x , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| .
$$

In both cases the constant $C$ depends only on the coefficients of the Runge-Kuta matrix and on $\alpha$ (for case $\left( a \right) .$ ）.

Remarks. a) The crucial fact in these estimates is that the right-hand side depends only on derivatives of the exact solution and not on the stiffness of the problem. These estimates are useful when a “smooth” solution of a stiff problem has to be approximated.

b) The hypothesis $\alpha _ { D } ( A ^ { - 1 } ) = 0$ (see case (b))is stronger than $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ (see Exercise 4 below). For the Lobatto IIIC methods,for which $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ $\mathit { \Pi } _ { s } ^ { ' } >$ 2), we have $\alpha _ { D } ( A ^ { - 1 } ) = 0$ with $D \approx B$ (see (14.21)). For stiffly accurate methods the estimate of part (b) can be improved by using (14.12) instead of (14.13).

c) In the estimates of the above proposition the maximum is taken over $\xi \in \mathbf { \Xi }$ $[ x , x + h ]$ . In the case where $0 \leq c _ { i } \leq 1$ is not satisfied, this interval must of course be correspondingly enlarged.

Proof. We put $\widehat { g } _ { \iota } = y \big ( x _ { 0 } + c _ { i } h \big )$ , so that the relation (14.11a) is satisfied with

$$
\delta _ { \imath } = y ( x _ { 0 } + c _ { \imath } h ) - y ( x _ { 0 } ) - h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } y ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) .
$$

Taylor expansion shows that

$$
\| \delta _ { i } \| \leq C _ { \iota } h ^ { q + 1 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { 1 } ] } \| y ^ { ( q + 1 ) } ( x ) \|
$$

where $\begin{array} { r } { C _ { \imath } = ( \vert c _ { \imath } \vert ^ { q + 1 } + ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } \vert a _ { \imath \jmath } \vert \cdot \vert c _ { \jmath } \vert ^ { q } ) / ( q + 1 ) ! } \end{array}$ is a method-dependent constant. Similarly, the value $\widehat { y } _ { 1 }$ of (14.11b) satisfies

$$
y ( x _ { 0 } + h ) - \widehat { y } _ { 1 } = y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h \sum _ { j = 1 } ^ { s } b _ { j } y ^ { j } ( x _ { 0 } + c _ { j } h ) = { \cal O } ( h ^ { q + 1 } ) ,
$$

because the order of the quadrature formula $\left( b _ { \imath } , c _ { i } \right) \mathrm { i } \mathrm { s } \geq q$ . Since

$$
\| \delta _ { h } ( x ) \| \leq \| y _ { 1 } - { \widehat { y } } _ { 1 } \| + \| { \widehat { y } } _ { 1 } - y ( x _ { 0 } + h ) \|
$$

the desired estimates follow from (14.13) of Theorem 14.3.

# Error Propagation

At the end of Sect.IV.12 we derived for some particular Runge-Kutta methods sharp estimates of the form

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \varphi _ { B } \big ( h \nu \big ) \| \widehat { y } _ { 0 } - y _ { 0 } \| ,
$$

where ${ \widehat { y } } _ { 1 } , y _ { 1 }$ are the numerical solutions corresponding to ${ \widehat { y } } _ { 0 } , y _ { 0 }$ ,respectively, and where the differential equation satisfies (15.11). We give here a simple proof of a crude estimate of $\varphi _ { B } ( h \nu )$ which, however, will be suficient to derive interesting convergence results.

Proposition 15.2 (Dekker & Verwer 1984). Suppose that the differential equation satisfies (15.11) and apply an algebraically stable Runge-Kutta method with invertible $A$ and $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ . Then for any $\alpha$ with $0 < \alpha < \alpha _ { 0 } \bigl ( A ^ { - 1 } \bigr )$ there exists $a$ constant $C > 0$ such that

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \big ( 1 + C h \nu \big ) \| \widehat { y } _ { 0 } - y _ { 0 } \| \qquad f o r \quad 0 \leq h \nu \leq \alpha .
$$

Proof. From (12.7) we have (using the notation of the proof of Theorem 12.4)

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { \iota = 1 } ^ { s } b _ { \iota } \langle \Delta f _ { \iota } , \Delta g _ { \iota } \rangle - \sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { i \jmath } \langle \Delta f _ { \iota } , \Delta f _ { \jmath } \rangle .
$$

By algebraic stability the last term in (15.14) is non-positive and can be neglected. Using (15.11) and the estimate (14.12) with $\delta _ { i } = \widehat { y } _ { 0 } - y _ { 0 }$ we obtain

$$
\begin{array} { r l r } {  { 2 \sum _ { \imath = 1 } ^ { s } b _ { \imath } \langle \Delta f _ { \imath } , \Delta g _ { \imath } \rangle \le 2 h \nu \sum _ { \imath = 1 } ^ { s } b _ { \imath } \| \Delta g _ { \imath } \| ^ { 2 } } } \\ & { } & { \leq 2 h \nu C _ { 1 } \| \Delta g \| _ { D } ^ { 2 } \le \frac { 2 h \nu C _ { 2 } } { ( \alpha _ { D } ( A ^ { - 1 } ) - h \nu ) ^ { 2 } } \| \Delta y _ { 0 } \| ^ { 2 } . } \end{array}
$$

Inserting this into (15.14) yields

$$
\| \Delta y _ { 1 } \| \leq \left( 1 + \frac { h \nu C _ { 2 } } { ( \alpha _ { D } ( A ^ { - 1 } ) - h \nu ) ^ { 2 } } \right) \| \Delta y _ { 0 } \|
$$

which proves the desired estimate.

# $B$ -Convergence for Variable Step Sizes

We are now in a position to present the main result of this section.

Theorem 15.3. Consider an algebraically stable Runge-Kutta method with invertible $A$ and stage order $q \leq p$ and suppose that (15.11) holds. $a _ { \scriptscriptstyle \perp }$ If $0 < \alpha < \alpha _ { 0 } \bigl ( A ^ { - 1 } \bigr )$ and $\nu > 0$ then the global error satisfies

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } \frac { \left( e ^ { C _ { 1 } \nu ( x _ { n } - x _ { 0 } ) } - 1 \right) } { C _ { 1 } \nu } C _ { 2 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| \quad f o r \quad h \nu \leq \alpha .
$$

$^ { b ) }$ 1f $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ and $\nu \leq 0$ then

$$
\Vert y _ { n } - y ( x _ { n } ) \Vert \leq h ^ { q } ( x _ { n } - x _ { 0 } ) C _ { 2 } \ \operatorname* { m a x } _ { x \in \{ x _ { 0 } , x _ { n } \} } \Vert y ^ { ( q + 1 ) } ( x ) \Vert \quad f o r a l l \quad h > 0 .
$$

$c ) I f \alpha _ { D } ( A ^ { - 1 } ) = 0$ for some positive diagonal matrix $D$ and $\nu < 0$ then

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q - 1 } C \Big ( h + \frac { 1 } { | \nu | } \Big ) ( x _ { n } - x _ { 0 } ) \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

The constants $C _ { 1 } , C _ { 2 } , C$ depend only on the coefficients of the Runge-Kutta matrix. In the case of variable step sizes, $h$ has to be interpreted as $h = \operatorname* { m a x } h _ { \ i }$

Proof. This convergence result is obtained in exactly the same way as that for nonstiff problems (Theorem I1.3.6). For the transported errors $E _ { \jmath }$ (see Fig. II.3.2) we have the estimate (for $\nu \geq 0$ ）

$$
\| E _ { \jmath } \| \leq e ^ { C \nu \left( x _ { n } - x _ { \jmath } \right) } \| \delta _ { h _ { \jmath - 1 } } ( x _ { \jmath - 1 } ) \|
$$

by Proposition 15.2, because $1 + C h \nu \leq e ^ { C \nu h }$ . We next insert the local error estimate of Proposition 15.1 into (15.15) and sum up the transported errors $E _ { \jmath }$ . This

yields the desired estimate for $\nu \geq 0$ because

$$
\begin{array} { r l } { \displaystyle \sum _ { \jmath = 1 } ^ { n } h _ { \jmath - 1 } e ^ { C \nu ( x _ { n } - x _ { \jmath } ) } \leq \int _ { x _ { 0 } } ^ { x _ { n } } e ^ { C \nu ( x _ { n } - x ) } d x } \\ { \displaystyle } & { \qquad = \left\{ \left( e ^ { C \nu ( x _ { n } - x _ { 0 } ) } - 1 ) / ( C \nu ) \right. \right. \left. \mathrm { f o r } \nu > 0 \right. } \\ { \displaystyle } & { \qquad \mathrm { f o r } \nu = 0 . } \end{array}
$$

f $\nu < 0$ we have $\| E _ { \jmath } \| \leq \| \delta _ { h _ { \jmath - 1 } } ( x _ { \jmath - 1 } ) \|$ by algebraic stability and the same arguments apply. □

Motivated by this result we define the order of $B$ -convergence as follows:

Definition 15.4 (Frank, Schneid & Ueberhuber 1981). A Runge-Kutta method is called $B$ -convergent of order $r$ for problems $y ^ { \prime } = f ( x , y )$ satisfying (15.11),if the global error admits an estimate

$$
\| y _ { n } - y ( x _ { n } ) \| \| \leq h ^ { r } \gamma ( x _ { n } - x _ { 0 } , \nu ) \operatorname* { m a x } _ { \substack { \jmath = 1 , \dots , l } } \operatorname* { m a x } _ { \substack { x \in [ x _ { 0 } , x _ { n } ] } } \| y ^ { ( \jmath ) } ( x ) \| \quad \mathrm { f o r } \quad h \nu \leq \alpha ,
$$

where $h = \operatorname* { m a x } h _ { \ i }$ .Here $\gamma$ is a method-dependent function and $\alpha$ also depends only on the coefficients of the method.

As an application of the above theorem we have

Theorem 15.5. The Gauss and Radau IIA methods are $B$ -convergent of order $s$ (number of stages). The Radau IA methods are $B$ -convergent of order $s - 1$ . The 2-stage Lobatto IIIC method is $B$ -convergent of order $l$ □

For the Lobatto IIC methods with $s \geq 3$ stages $\left( \alpha _ { 0 } ( A ^ { - 1 } ) = 0 \right.$ and $q = s - 1 \AA .$ ） Theorem 15.3 shows $B$ -convergence of order $s - 2$ if $\nu < 0$ . This is not an optimal result. Spijker (1986) proved $B$ -convergence of order $s - 3 / 2$ for $\nu < 0$ and constant step sizes. Schneid (1987) improved this result to $s - 1$ . Recently, Dekker, Kraaijevanger & Schneid (1991) showed that these methods are $B$ -convergent of order $s - 1$ for general step size sequences, if one allows the function $\gamma$ in Definition 15.4 to depend also on the ratio max $h _ { \imath } / \operatorname* { m i n } h _ { \imath }$

The Lobatto IIIA and IIB methods cannot be $B$ -convergent since they are not algebraically stable. This will be the content of the next subsection.

# $B$ -Convergence Implies Algebraic Stability

In order to find necessry conditions for $B$ -convergence we consider the problem

$$
y ^ { \prime } = \lambda ( x ) { \bigl ( } y - \varphi ( x ) { \bigr ) } + \varphi ^ { \prime } ( x ) , \qquad \operatorname { R e } \lambda ( x ) \leq \nu
$$

with exact solution $\varphi ( x ) = x ^ { q + 1 }$ . We apply a Runge-Kutta method with stage order $q$ and obtain for the global error $\varepsilon _ { n } = y _ { n } - \varphi ( x _ { n } )$ the simple recursion

$$
\varepsilon _ { n + 1 } = { \cal K } ( Z _ { n } ) \varepsilon _ { n } - { \cal L } ( Z _ { n } ) h ^ { q + 1 }
$$

(cf.Eq.(15.8) of the beginning of this section,where the case $\lambda ( x ) = \lambda$ was treated). Here $Z _ { n } = \mathrm { d i a g } \left( h \lambda ( x _ { n } + c _ { 1 } h ) , \ldots , h \lambda ( x _ { n } + c _ { s } h ) \right)$ and

$$
K ( Z ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 } , \quad L ( Z ) = d _ { 0 } + b ^ { T } Z ( I - A Z ) ^ { - 1 } d .
$$

The function $\bar { \cal K } ( Z )$ was already encountered in Definition 12.10, when treating $A N$ -stability. The vector $d = ( d _ { 1 } , \ldots , d _ { s } ) ^ { T }$ and $d _ { 0 }$ in $L ( Z )$ characterize the local error and are given by

$$
d _ { 0 } = 1 - ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { q } , \qquad d _ { \imath } = c _ { \imath } ^ { q + 1 } - ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { q } .
$$

Observe that by definition of the stage order we have either $d _ { 0 } \neq 0$ or $d \neq 0$ (or both). We are now in the position to prove

Theorem 15.6 (Dekker, Kraaijevanger & Schneid 1991). Consider a $D J$ -irreducible Runge-Kutta method which satisfies $0 \leq c _ { 1 } < c _ { 2 } < . . . < c _ { s } \leq 1 $ If,for some $r$ ， $l$ and $\nu < 0$ , the global error satisfies the $B$ -convergence estimate $( l 5 . l 6 )$ ,then the method is algebraically stable.

Proof. Suppose that the method is not algebraically stable. Then,by Theorem 12.13 and Lemma 15.17 below, there exists $Z = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right)$ with $\mathrm { R e } z _ { \jmath } < 0$ such that $( I - A Z ) ^ { - 1 }$ exists and

$$
| K ( Z ) | > 1 , \qquad L ( Z ) \ne 0 .
$$

We consider the interval $[ 0 , ( 1 + \theta ) / 2 ]$ and for even $N$ the step size sequence $( h _ { n } ) _ { n = 0 } ^ { N - 1 }$ given by

$$
h _ { n } = 1 / N \quad ( \mathrm { f o r } n \mathrm { e v e n } ) , \quad h _ { n } = \theta / N \quad ( \mathrm { f o r } n \mathrm { o d d } ) .
$$

If $N$ is sufficiently large it is possible to define a function $\lambda ( x )$ which satisfies $\operatorname { R e } \lambda ( x ) \leq \nu$ and

$$
\lambda ( x _ { n } + c _ { \iota } h _ { n } ) = { \left\{ \begin{array} { l l } { N z _ { \iota } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ e v e n } } } \\ { N z _ { s + 1 - \iota } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ o d d } } . } \end{array} \right. }
$$

Because of (15.18) the global error $\varepsilon _ { n } = y _ { n } - \varphi ( x _ { n } )$ for the problem (15.17) sat-

isfies (with $h = 1 / N _ { \cdot }$ ）

$$
\begin{array} { l } { { \varepsilon _ { n + 1 } = K ( Z ) \varepsilon _ { n } - h ^ { q + 1 } L ( Z ) \quad \mathrm { f o r } n \mathrm { e v e n } } } \\ { { \varepsilon _ { n + 1 } = K ( \widetilde { Z } ) \varepsilon _ { n } - h ^ { q + 1 } L ( \widetilde { Z } ) \quad \mathrm { f o r } n \mathrm { o d d } } } \end{array}
$$

where $\widetilde { Z } = \operatorname { d i a g } \left( \theta z _ { s } , \dots , \theta z _ { 1 } \right)$ . Consequently we have

$$
\varepsilon _ { 2 m + 2 } = K ( \widetilde { Z } ) K ( Z ) \varepsilon _ { 2 m } - h ^ { q + 1 } ( K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) )
$$

and the error at $X = ( 1 + \theta ) / 2$ is given by

$$
\varepsilon _ { N } = - \frac { 1 } { N ^ { q + 1 } } \left( K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) \right) \frac { ( K ( \widetilde { Z } ) K ( Z ) ) ^ { N / 2 } - 1 } { K ( \widetilde { Z } ) K ( Z ) - 1 } .
$$

If $\theta$ is suficiently small, $K ( \widetilde { Z } ) \to 1$ and $L ( \widetilde { Z } ) \to d _ { 0 }$ , so that by (15.21)

$$
| K ( \widetilde { Z } ) K ( Z ) | > 1 \quad \mathrm { a n d } \quad K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) \ne 0 .
$$

Therefore $| \varepsilon _ { N } | \to \infty$ as $N \to \infty$ $N$ even), which contradicts the estimate (15.16) of $B$ -convergence.

To complete the above proof we give the following lemma:

Lemma 15.7 (Dekker, Kraaijevanger & Schneid 1990). Consider a $D J$ -irreducible Runge-Kutta method and suppose

$$
b ^ { T } Z ( I - A Z ) ^ { - 1 } d = 0
$$

for all $\boldsymbol { Z } = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right)$ with $I - A Z$ invertible; then $d = 0$

Proof. We define

$$
T = \big \{ j \big | b _ { i _ { 1 } } a _ { \iota _ { 1 } i _ { 2 } } a _ { i _ { 2 } i _ { 3 } } \cdot \cdot \cdot a _ { i _ { k - 1 } i _ { k } } = 0 \quad \mathrm { ~ f o r ~ a l l ~ } k \mathrm { ~ a n d ~ } i _ { l } \mathrm { ~ w i t h ~ } i _ { k } = j \big \} .
$$

Putting $k = 1$ we obtain $b _ { j } = 0$ for $j \in T$ . Further,if $i \not \in T$ and $j \in T$ there exists $( i _ { 1 } , \dots , i _ { k } )$ with $i _ { k } = i$ such that

$$
b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } \neq 0 , \quad b _ { \iota _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } a _ { i j } = 0
$$

implying $a _ { \scriptscriptstyle { \imath \jmath } } = 0$ . Therefore the method is $D J$ -reducible if $T \neq \emptyset$ . For the proof of the statement it thus suffices to show that $d \neq 0$ implies $T \neq \emptyset$ ·

Replacing $( I - A Z ) ^ { - 1 }$ by its geometric series, assumption (15.23) becomes equivalent to

$$
b ^ { T } Z ( A Z ) ^ { k - 1 } d = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } k { \mathrm { ~ a n d ~ } } Z = \operatorname { d i a g } { \big ( } z _ { 1 } , \ldots , z _ { s } { \big ) } .
$$

Comparing the coefficient of $z _ { i _ { 1 } } \cdots z _ { i _ { k } }$ gives

$$
\sum b _ { j _ { 1 } } a _ { j _ { 1 } j _ { 2 } } \cdot \cdot \cdot a _ { j _ { k - 1 } j _ { k } } d _ { j _ { k } } = 0 ,
$$

where the summation is over all permutations $( j _ { 1 } , \dots , j _ { k } )$ of $( i _ { 1 } , \dots , i _ { k } )$ Sup-pose now that $d _ { j } \neq 0$ for some index $j$ . We shall prove by induction on $k$ that

$$
b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \quad i _ { \ell } ( \ell = 1 , \dots , k ) \quad { \mathrm { w i t h } } \quad i _ { k } = j ,
$$

so that $j \in T$ and consequently $T \neq \emptyset$

For $k \simeq 1$ this follows immediately from (15.25)． In order to prove (15.26) for $k + 1$ we suppose, by contradiction, that $( i _ { 1 } , \dots , i _ { k + 1 } )$ with $i _ { k + 1 } = j$ exists such that $b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k } i _ { k + 1 } } \ne 0$ .The relation (15.25)then implies the existence of apermutation(k+1)of (ik1)suchthatb ， too. We now denote by $q$ the smallest index for which $i _ { q } \neq j _ { q }$ .Then $i _ { q } = j _ { r }$ for some $r > q$ and

$$
b _ { i _ { 1 } } a _ { i _ { 1 } \ i _ { 2 } } \cdot \cdot \cdot a _ { i _ { q - 1 } i _ { q } } a _ { j _ { r } j _ { r + 1 } } \cdot \cdot \cdot a _ { j _ { k } j _ { k + 1 } } \neq 0
$$

contradicts the induction hypothesis, because the expression in (15.27) contains at most $k$ factors. □

# The Trapezoidal Rule

The trapezoidal rule

$$
y _ { k + 1 } = y _ { k } + { \frac { h _ { k } } { 2 } } { \Big ( } f { \big ( } x _ { k } , y _ { k } { \big ) } + f { \big ( } x _ { k + 1 } , y _ { k + 1 } { \big ) } { \Big ) }
$$

is not algebraically stable. Therefore (Theorem 15.6) it cannot be $B$ -convergent in the sense of Definition 15.4. Nevertheless it is possible to derive estimates (15.16), if we restrict ourselves to special step size sequences (constant, monotonic,...). This was first proved by Stetter (unpublished) and investigated in detail by Kraai-jevanger (1985). The result is

Theorem 15.8 (Kraaijevanger 1985). If the differential equation satisfies (15.11), then the global error of the trapezoidal rule permits for $h _ { j } \nu \leq \alpha < 2$ the estimate

$$
\Vert y _ { n } - y ( x _ { n } ) \Vert \leq C \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \Vert y ^ { ( 3 ) } ( x ) \Vert \sum _ { k = 0 } ^ { n - 1 } \Big ( \prod _ { \substack { j = k + 1 } } ^ { n - 1 } \operatorname* { m a x } \left( 1 , h _ { j } / h _ { j - 1 } \right) \Big ) h _ { k } ^ { 3 } .
$$

Proof. We denote by ${ \widehat { y } } _ { k } = y ( x _ { k } )$ the exact solution at the grid points. From the Taylor expansion we then get

$$
\widehat { y } _ { k + 1 } = \widehat { y } _ { k } + \frac { h _ { k } } { 2 } \Big ( f \big ( x _ { k } , \widehat { y } _ { k } \big ) + f \big ( x _ { k + 1 } , \widehat { y } _ { k + 1 } \big ) \Big ) + \delta _ { k }
$$

where

$$
\| \delta _ { k } \| \leq \frac { 1 } { 1 2 } h _ { k } ^ { 3 } \operatorname* { m a x } _ { x \in [ x _ { k } , x _ { k + 1 } ] } \| y ^ { ( 3 ) } ( x ) \| .
$$

The main idea is now to introduce the intermediate values

$$
\begin{array} { l } { { y _ { k + 1 / 2 } = y _ { k } + \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k } , y _ { k } ) = y _ { k + 1 } - \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k + 1 } , y _ { k + 1 } ) } } \\ { { \widehat { y } _ { k + 1 / 2 } = \widehat { y } _ { k } + \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k } , \widehat { y } _ { k } ) + \delta _ { k } = \widehat { y } _ { k + 1 } - \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k + 1 } , \widehat { y } _ { k + 1 } ) . } } \end{array}
$$

The transition yk-1/2 → Yk+1/2

$$
y _ { k + 1 / 2 } = y _ { k - 1 / 2 } + { \frac { 1 } { 2 } } { ( h _ { k - 1 } + h _ { k } ) f ( x _ { k } , y _ { k } ) }
$$

can then be interpreted as one step of the $\theta$ -method

$$
y _ { m + 1 } = y _ { m } + h f \bigl ( x _ { m } + \theta h , y _ { m } + \theta ( y _ { m + 1 } - y _ { m } ) \bigr )
$$

with $\theta = h _ { \boldsymbol k - 1 } / ( h _ { \boldsymbol k - 1 } + h _ { \boldsymbol k } )$ and step size $h = ( h _ { k - 1 } + h _ { k } ) / 2$ . A similar calculation shows that the same $\theta$ -method maps $\widehat { y } _ { k - 1 / 2 }$ t0 $\widehat { y } _ { k + 1 / 2 } - \delta _ { k }$ . Therefore we have

$$
\begin{array} { r } { \| \widehat { y } _ { k + 1 / 2 } - y _ { k + 1 / 2 } - \delta _ { k } \| \leq \varphi _ { B } ( h \nu ) \ \| \widehat { y } _ { k - 1 / 2 } - y _ { k - 1 / 2 } \| , } \end{array}
$$

where the growth function $\varphi _ { B } ( h \nu )$ is given by (see Eqs.(12.42) and (11.13))

$$
\begin{array} { l } { \displaystyle \varphi _ { B } \big ( h \nu \big ) = \operatorname* { m a x } \bigl \{ \big ( 1 - \theta \big ) / \theta , \big ( 1 + ( 1 - \theta ) h \nu \big ) / \big ( 1 - \theta h \nu \big ) \bigr \} } \\ { \displaystyle = \operatorname* { m a x } \bigl \{ h _ { k } / h _ { k - 1 } , \big ( 1 + \frac 1 2 h _ { k } \nu \big ) / \big ( 1 - \frac 1 2 h _ { k - 1 } \nu \big ) \bigr \} = : \varphi _ { k } . } \end{array}
$$

By the triangle inequality we also get

$$
\begin{array} { r } { \| \widehat { y } _ { k + 1 / 2 } - y _ { k + 1 / 2 } \| \leq \varphi _ { k } \| \widehat { y } _ { k - 1 / 2 } - y _ { k - 1 / 2 } \| + \| \delta _ { k } \| . } \end{array}
$$

Further it follows from(15.31) with $k = 0$ and from $\widehat { y } _ { 0 } = y _ { 0 }$ that

$$
\| \widehat { y } _ { 1 / 2 } - y _ { 1 / 2 } \| = \| \delta _ { 0 } \| ,
$$

whereas the backward Euler steps $y _ { n - 1 / 2 } \to y _ { n }$ and $\widehat { y } _ { n - 1 / 2 } \to \widehat { y } _ { n }$ (see ( imply

$$
\Vert \widehat { y } _ { n } - y _ { n } \Vert \leq \frac { 1 } { \left( 1 - \frac { 1 } { 2 } h _ { n - 1 } \nu \right) } \Vert \widehat { y } _ { n - 1 / 2 } - y _ { n - 1 / 2 } \Vert
$$

again by Example 12.24 with $\theta = 1$ . A combination of (15.33), (15.34) and (15.35) yields

$$
\left\| \widehat { y } _ { n } - y _ { n } \right\| \leq \frac { 1 } { \left( 1 - \frac { 1 } { 2 } h _ { n - 1 } \nu \right) } \sum _ { k = 0 } ^ { n - 1 } \Big ( \prod _ { \substack { \jmath = k + 1 } } ^ { n - 1 } \varphi _ { \jmath } \Big ) \| \delta _ { k } \| .
$$

For $\nu \leq 0$ we have $\varphi _ { k } \leq \operatorname* { m a x } ( 1 , h _ { k } / h _ { k - 1 } )$ and the statement follows if we insert (15.30) into (15.36). For $\nu \geq 0$ we use the estimate $\left( h _ { k - 1 } \nu \leq 1 \right)$

$$
\frac { 1 + \frac 1 2 h _ { k } \nu } { 1 - \frac 1 2 h _ { k - 1 } \nu } = \frac { 1 + \frac 1 2 h _ { k - 1 } \nu } { 1 - \frac 1 2 h _ { k - 1 } \nu } \cdot \frac { 1 + \frac 1 2 h _ { k } \nu } { 1 + \frac 1 2 h _ { k - 1 } \nu } \le e ^ { 2 h _ { k - 1 } \nu } \cdot \operatorname* { m a x } \Bigl ( 1 , \frac { h _ { k } } { h _ { k - 1 } } \Bigr )
$$

so that the statement holds with $C = e ^ { 2 \nu ( x _ { n } - x _ { 0 } ) } / 1 2$

Crla $\left( h _ { k } \right) _ { k = 0 } ^ { N - 1 }$ is constant or monotonic,then for $h = \operatorname* { m a x } h _ { i }$

$$
\| y _ { n } - y ( x _ { n } ) \| \leq C \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( 3 ) } ( x ) \| \cdot h ^ { 2 } .
$$

# Order Reduction for Rosenbrock Methods

Obviously, Rosenbrock methods (Definition 7.1） cannot be $B$ -convergent in the sense of Definition 15.4 (see also Exercise 7 of Sect.IV.12). Nevertheless it is interesting to study their behaviour on stiff problems such as the Prothero & Robinson model (15.1). Since this equation is non-autonomous we have to use the formulation (7.4a). A straightforward calculation shows that the global error $\varepsilon _ { n } =$ $y _ { n } - \varphi ( x _ { n } )$ satisfies the recursion

$$
\varepsilon _ { n + 1 } = R ( z ) \varepsilon _ { n } + \delta _ { h } ( x _ { n } )
$$

where $R ( z )$ is the stability function (7.14)and the local error is given by

$$
\delta _ { h } ( x ) = \varphi ( x ) - \varphi ( x + h ) + b ^ { T } ( I - z B ) ^ { - 1 } \Delta
$$

with $B = ( \alpha _ { i j } + \gamma _ { \imath \jmath } ) , b = ( b _ { 1 } , \ldots , b _ { s } ) ^ { T } , \Delta = ( \Delta _ { 1 } , \ldots , \Delta _ { s } ) ^ { T }$ and

$$
\Delta _ { i } = z ( \varphi ( x ) - \varphi ( x + \alpha _ { \iota } h ) - \gamma _ { i } h \varphi ^ { \prime } ( x ) ) + h \varphi ^ { \prime } ( x + \alpha _ { i } h ) + \gamma _ { \iota } h ^ { 2 } \varphi ^ { \prime \prime } ( x ) .
$$

Taylor expansion gives the following result.

Lemma 15.10. The local error $\delta _ { h } ( x )$ of a Rosenbrock method applied to (15.1) satisfies for $h  0$ and $z = \lambda h  \infty$

$$
\delta _ { h } ( x ) = \Bigl ( \sum _ { i , j } b _ { i } \omega _ { i j } \alpha _ { j } ^ { 2 } - 1 \Bigr ) \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + \mathcal { O } \bigl ( h ^ { 3 } \bigr ) + \mathcal { O } \Bigl ( \frac { h ^ { 2 } } { z } \Bigr ) ,
$$

where $\omega _ { \imath \jmath }$ are the entries of $B ^ { - 1 }$ ·

Remarks. a) Unless the Rosenbrock method satisfies the new order condition

$$
\sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } \alpha _ { j } ^ { 2 } = 1 ,
$$

the local error and the global error (if $| R ( \infty ) | < 1 )$ are of size $\mathcal { O } ( h ^ { 2 } )$ . Since none of the classical Rosenbrock methods of Sect.IV.7 satisfies (15.39), their order of convergence is only 2 for the problem (15.1) if $\lambda$ is very large.

b) A convenient way to satisfy (15.39) is to require

$$
\alpha _ { s i } + \gamma _ { s i } = b _ { i } ( i = 1 , \ldots , s ) \quad \mathrm { a n d } \quad \alpha _ { s } = 1 .
$$

This is the analogue of the condition $a _ { s _ { 1 } } = b _ { \ i }$ for Runge-Kutta methods. It implies not only (15.39) but even

$$
\begin{array} { r } { \delta _ { h } ( x ) = \mathcal { O } \Big ( \frac { h ^ { 2 } } { z } \Big ) , } \end{array}
$$

so that such methods yield asymptotically exact results for $z  \infty$

c) A deeper understanding of Eq.(15.39) will be possible when studying the error of Rosenbrock methods for singular perturbation and differential-algebraic problems (Chapter VI). We shall construct there methods satisfying (15.40).

d) Scholz (1989) writes the local error $\delta _ { h } \{ x \}$ in the form

$$
\delta _ { \hbar } ( x ) = \sum _ { j \geq 2 } C _ { j } ( z ) \hbar ^ { j } \varphi ^ { ( j ) } ( x )
$$

and investigates the possibility of having $C _ { \ j } ( \ j z ) \equiv 0$ for $j = 2$ (and also $j > 2$ ). Hundsdorfer (1986) and Strehmel & Weiner(1987) extend the above analysis to semi-linear problems (11.21) which satisfy (11.22). Their results are rather technical but allow the construction of “ $B$ -convergent" methods of order $p > 1$ ·

# Exercises

1. Prove that the stage order of an SDIRK method is at most 1, that of a DIRK method at most 2.

2. Consider a Runge-Kuta method with $0 \leq c _ { 1 } < . . . < c _ { s } \leq 1$ which has stage order $q$ ． Prove that the method cannot be $B$ -convergent (for variable step sizes) of order $q + 1$

Hint. Use Formula (15.22) and prove that

$$
\frac { I \tilde { \mathcal { ( Z ) } } L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) } { I \tilde { \mathcal { ( Z ) } } I \tilde { \mathcal { ( Z ) } } - 1 }
$$

cannot be uniformly bounded for

$$
Z = \mathrm { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right) , \qquad { \widetilde { Z } } = \mathrm { d i a g } \left( { \widetilde { z } } _ { 1 } , \dots , { \widetilde { z } } _ { s } \right)
$$

with $\mathrm { R e } z _ { \imath } \leq 0 , \mathrm { R e } \tilde { z } _ { \imath } \leq 0$ (in the case ${ { c } _ { 1 } } = 0$ and $c _ { s } = 1$ one has to prove this under the restriction $\hat { z } _ { 1 } = \theta z _ { s }$ ， $\tilde { z } _ { s } \simeq \theta z _ { 1 }$ ). For this consider valucs $\tilde { \mathbf { \Xi } } _ { \tilde { \mathbf { \Lambda } } _ { 1 } } , \ \widetilde { \boldsymbol { z } } _ { 1 }$ close to the origin.

3.(Burrage & Hundsdorfer 1987).Assume $c _ { i } \sim c _ { j }$ is not an integer for $1 \leq i <$ $\jmath \leq s$ ,and the order of $B$ -convergence (for constant step sizes) of a Runge-Kutta method is $q + 1$ （ $q$ denotes the stage order). Then $d _ { 0 } = 0$ and all components of $\boldsymbol { d } = ( d _ { 1 } , \ldots , d _ { s } ) ^ { T }$ are equal (see (15.20) for the definition of $d _ { j }$ ).

Hint. Study the uniform boundedness of the function $L ( Z ) / ( K ( Z ) - 1 )$

4. (Kraaijevanger). Show that for

$$
A ^ { - 1 } = { \left( \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } \end{array} \right) }
$$

we have $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ , but there exists no positive diagonal matrix $D$ such that $\alpha _ { D } ( A ^ { - 1 } ) = 0$ . For more insight see “Corollary $2 . 1 5 ^ { \circ }$ of Kraaijevanger & Schneid (1991).

5. Prove that for the Lobatto IIIB methods, with

$$
A = \left( \begin{array} { l l } { \widetilde { A } } & { 0 } \\ { a ^ { T } } & { 0 } \end{array} \right)
$$

the dominant term of the local error (15.7) is (for $h \to 0$ and $z = h \lambda \to \infty$ ）

$$
z b _ { s } ( a ^ { T } \widetilde { A } ^ { - 1 } c ^ { q + 1 } - 1 ) \frac { h ^ { q + 1 } } { ( q + 1 ) ! } \varphi ^ { ( q + 1 ) } ( x ) .
$$

Here $q = s - 2$ is the stage order and $\boldsymbol { c } = ( c _ { 1 } , \dots , c _ { s - 1 } ) ^ { T }$ . Show further that

$$
\begin{array} { r l r l } & { { } a ^ { T } \widetilde { A } ^ { - 1 } c ^ { k } = 1 } & { } & { { } \mathrm { f o r } \quad k = 1 , 2 , \ldots , q } \\ & { { } a ^ { T } \widetilde { A } ^ { - 1 } c ^ { k } \neq 1 } & { } & { { } \mathrm { f o r } \quad k = q + 1 . } \end{array}
$$

Hint. Equation (15.44) follows from $C ( q )$ . Show (15.45) by supposing that $a ^ { T } \tilde { A } ^ { - 1 } c ^ { q + 1 } = 1$ which together with (15.44) implies that

$$
\sum _ { \ i = 1 } ^ { s - 1 } d _ { \ i } p ( c _ { \ i } ) = p ( 1 ) \qquad \mathrm { w h e r e } \quad d ^ { T } = a ^ { T } \widetilde { A } ^ { - 1 }
$$

for every polynomial of $\deg p \leq q + 1 = s - 1$ satisfying $p ( 0 ) = 0$ . Arrive at a contradiction with

$$
p ( x ) = ( x - c _ { 1 } ) ( x - c _ { 2 } ) \cdot \ldots \cdot ( x - c _ { s - 1 } ) .
$$

# Chapter V. Multistep Methods for Stiff Problems

Multistep methods (BDF) were the first numerical methods to be proposed for stiff differential equations (Curtiss & Hirschfelder 1952) and since Gear's book (1971) computer codes based on these methods have been the most prominent and most widely used for all stiff computations.

This chapter introduces the linear stability theory for multistep methods in Sect.V.1,and arrives at the famous theorem of Dahlquist which says that $A$ -stable multistep methods cannot have high order. Attempts to circumvent this barrier proceed mainly in two directions: either study methods with slightly weaker stability requirements (Sect. V.2) or introduce new classes of methods (Sect. V.3). Order star theory on Riemann surfaces (Sect. V.4) then helps to extend Dahlquist's barrier to generalized methods and to explain various properties of stability domains. Sec-tion V.5 presents numerical experiments with several codes based on the methods introduced.

Since allthe foregoing stability theory is based uniquely on linear autonomous problems $y ^ { \prime } = A y$ , the question arises of their validity for general nonlinear problems. This leads to the concepts of $G$ -stability for multistep methods (Sect. V.6) and algebraic stability for general linear methods (Sect. V.9).

Another important subject is convergence estimates for $h  0$ which are independent of the stiffness (the analogue of $B$ -convergence in Sect.IV.15). We describe various techniques for obtaining such estimates in Sections V.7 (for linear problems) as well as V.6 and V.8 (for nonlinear problems). These techniques are: use of $G$ -stability, the Kreiss matrix theorem,the multiplier technique and, last but not least, a discrete variation of constants formula.

# V.1 Stability of Multistep Methods

A general $k$ -step multistep method is of the form

$$
\alpha _ { k } y _ { m + k } + \alpha _ { k - 1 } y _ { m + k - 1 } + \ldots + \alpha _ { 0 } y _ { m } = h ( \beta _ { k } f _ { m + k } + \ldots + \beta _ { 0 } f _ { m } ) .
$$

For this method, we can do the same stability analysis as in Sect.IV.2 for Euler's method. This means that we apply it to the linearized and autonomous system

$$
y ^ { \prime } = J y
$$

(see (IV.2.2')); this gives

$$
\alpha _ { k } y _ { m + k } + . . . + \alpha _ { 0 } y _ { m } = h J ( \beta _ { k } y _ { m + k } + . . . + \beta _ { 0 } y _ { m } ) .
$$

We again introduce a new basis for the vectors $y _ { m + \imath }$ consisting of the eigenvectors of $J$ . Then for the coefficients of $y _ { m + \imath }$ ， with respect to an eigenvector $v$ f $J$ ， we obtain exactly the same reccurrence equation as (1.3), with $J$ replaced by the corresponding eigenvalue $\lambda$ . This gives 1

$$
( \alpha _ { k } - \mu \beta _ { k } ) y _ { m + k } + \hdots + ( \alpha _ { 0 } - \mu \beta _ { 0 } ) y _ { m } = 0 , \qquad \mu = h \lambda
$$

and is the same as Method (1.1) applied to Dahlquist's test equation

$$
y ^ { \prime } = \lambda y .
$$

# The Stability Region

The difference equation (1.4) is solved using Lagrange's method (see Volume I, Sect. II1.3): we set $y _ { \jmath } = \zeta ^ { \jmath }$ , divide by $\zeta ^ { m }$ and obtain the characteristic equation

$$
( \alpha _ { k } - \mu \beta _ { k } ) \zeta ^ { k } + . . . + ( \alpha _ { 0 } - \mu \beta _ { 0 } ) = \varrho ( \zeta ) - \mu \sigma ( \zeta ) = 0
$$

which depends on the complex parameter $\mu$ . The polynomials $\varrho ( \zeta )$ and $\sigma ( \zeta )$ are our old friends from (III.2.4). The difference equation (1.4) has stable solutions (for arbitrary starting values) iff all roots of (1.6) are $\leq 1$ in modulus. In addition, multiple roots must be strictly smaller than 1 (see Volume I, Sect.III.3,Exercise 1).

# Definition 1.1. The set

$$
S = \{ \mu \in \mathbb { C } \ ; \ \operatorname { a l l } \ \mathrm { r o o t s } \ \zeta _ { \ j } ( \mu ) \ \mathrm { o f } \ ( 1 . 6 ) \ \mathrm { s a t i s f y } \ | \zeta _ { \ j } ( \mu ) | \le 1 , \} \}
$$

is called the stability domain or stability region or region of absolute stability of Method (1.1). We have $A$ -stability if $S \supset \mathbb { C } ^ { - }$

It is sometimes desirable to consider $S$ as a subset of the compactified complex plane $\overrightarrow { \mathbb { C } }$ . In this case, for $\mu  \infty$ , the roots of Eq.(l.6) tend to those of $\sigma ( \zeta ) = 0$

For $\mu = 0$ ,Eq. (1.6) becomes $\varrho \big ( \zeta \big ) = 0$ . Thus the usual stability (in the sense of Definition III.3.2) is equivalent to $0 \in S$

Theorem 1.2. All numerical solutions of Method (1.1) are bounded for the linearized equation (1.2) with a diagonalizable matrix $J$ 讲 $h \lambda \in S$ for all eigenvalues $\lambda$ of $J$ □

We explain the computation of the stability domain at a particular example, the explicit Adams method of order 4 (see Sect. II.1, Eq.(1.5)),

$$
y _ { m + 4 } = y _ { m + 3 } + h \Bigl ( { \frac { 5 5 } { 2 4 } } f _ { m + 3 } - { \frac { 5 9 } { 2 4 } } f _ { m + 2 } + { \frac { 3 7 } { 2 4 } } f _ { m + 1 } - { \frac { 9 } { 2 4 } } f _ { m } \Bigr ) ,
$$

for which Eq.(1.6) becomes

$$
\zeta ^ { 4 } - \Bigl ( 1 + { \frac { 5 5 } { 2 4 } } \mu \Bigr ) \zeta ^ { 3 } + { \frac { 5 9 } { 2 4 } } \mu \zeta ^ { 2 } - { \frac { 3 7 } { 2 4 } } \mu \zeta + { \frac { 9 } { 2 4 } } \mu = 0 .
$$

In Fig.1.1 we display the complicated behavior of the roots of this equation. We choose the $1 6$ values as the dots surrounding the white horse,and plot the corresponding 4 roots $\zeta _ { 1 } , \zeta _ { 2 } , \zeta _ { 3 } , \zeta _ { 4 }$ in the $\zeta$ -plane,which can be obscrved to emerge from the roots $1 , 0 , 0 , 0$ of the $\varrho$ -polynomial.

Complex mappings are conformal, i.e., preserve angles and orientation. The angle of rotation and the magnification of a complex map is (locally) determined by its derivative. Differentiating(1.8) with respect to $\mu$ and putting $\mu = 0 , \zeta = 1$ gives

$$
\varrho ^ { \prime } ( 1 ) \cdot \zeta _ { 1 } ^ { \prime } ( 0 ) - \sigma ( 1 ) = 0 ,
$$

hence $\zeta _ { 1 } ^ { \prime } ( 0 ) = 1$ (because of the consistency conditions $\varrho ^ { \prime } ( 1 ) \neq 0$ ， $\sigma ( 1 ) \stackrel { \triangledown } { = } \varrho ^ { \prime } ( 1 )$ ， see Volume I, Eq. (III.2.6)). This explains the fact that the map $\mu (  ) \zeta _ { 1 }$ is close to $1 + \mu$ in the neighbourhood of $\mu = 0$ ,and $\zeta _ { 1 } ( \mu )$ moves inside the unit disc when $\mu$ moves inside $\mathbb { C } ^ { - }$

The Root Locus Curve. The key for computing $S$ is the fact that the inverse map $\zeta \mapsto \mu$ ,since(1.8) is linear in $\mu$ , can easily be computed and is one-valued

$$
\mu = \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } = \frac { \zeta ^ { 4 } - \zeta ^ { 3 } } { \frac { 5 5 } { 2 4 } \zeta ^ { 3 } - \frac { 5 9 } { 2 4 } \zeta ^ { 2 } + \frac { 3 7 } { 2 4 } \zeta - \frac { 9 } { 2 4 } } .
$$

The outside of the unit circle in the $\zeta$ -plane mapped back into the $\mu$ -plane by this formula (see the zodiac of gray horses in Fig.1.1) produces the forbidden $\mu$ -values, for which at least one root $\zeta _ { \imath } ( \mu )$ generates instability. The image of the boundary curve of the unit circle $\zeta = e ^ { \imath \theta }$ ， $0 \leq \theta \leq 2 \pi$ ， is called the root locus curve. It must be considered as an oriented curve and the stability region, whenever it is not empty, must lie to the left of it.

![](images/3c848d6ae2d9fd06db1368e423fd4cb07efb70c99aa82fb5fdd0362a3df622ea.jpg)  
Fig.1.1. Plot of the stability function (1.8) with root locus curve

We conclude that the stability domain of Adams4 is precisely the small diamond shaped region surrounded by the root locus curve in the positive direction located between the origin and the point $\mu = 2 \cdot 2 4 / ( - 5 5 - 5 9 - 3 7 - 9 ) = - 0 . 3$

# Adams Methods

The explicit Adams methods (III.1.5) applied to $y ^ { \prime } = \lambda y$ give

$$
y _ { n + 1 } = y _ { n } + \mu \sum _ { \jmath = 0 } ^ { k - 1 } \gamma _ { \jmath } \nabla ^ { j } y _ { n } , \qquad \gamma _ { 0 } = 1 , \ \gamma _ { 1 } = \frac { 1 } { 2 } , \ \gamma _ { 2 } = \frac { 5 } { 1 2 } , \ \gamma _ { 3 } = \frac { 3 } { 8 } , \ \cdot \ \cdot \ .
$$

or, after putting $y _ { n } = \zeta ^ { n }$ and dividing by $\zeta ^ { n }$ ，

$$
\zeta - 1 = \mu \Big ( \gamma _ { 0 } + \gamma _ { 1 } \Big ( 1 - \frac { 1 } { \zeta } \Big ) + \gamma _ { 2 } \Big ( 1 - \frac { 2 } { \zeta } + \frac { 1 } { \zeta ^ { 2 } } \Big ) + \dots \Big ) .
$$

Hence the root locus curve becomes

$$
\mu = { \frac { \zeta - 1 } { \sum _ { \jmath = 0 } ^ { k - 1 } \gamma _ { \jmath } ( 1 - 1 / \zeta ) ^ { j } } } , \qquad \zeta = e ^ { i \theta } .
$$

For $k \approx 1$ we again obtain the circle of Euler's method, centred at $- 1$ .These curves are plotted in Fig.1.2 for $k = 2 , 3 , \ldots , 6$ and show stability domains of rapidly decreasing sizes. These methods are thus surely not appropriate for stiff problems.

![](images/809de5caa87a11046cdf49feda2e3f2e102da9e2ed850e93acf35b3f107c74e0.jpg)  
Fig.1.2. Stability domains for explicit Adams methods

![](images/2c71023b15a7e81415189ad2a2a0967e8d72ffa81fa0ca6d37489d1c54993206.jpg)  
Fig.1.3. Stability domains of implicit Adams methods, compared to those of the explicit ones

The implicit Adams methods (II.1.8) lead to

$$
y _ { n + 1 } = y _ { n } + \mu \sum _ { \jmath = 0 } ^ { k } \gamma _ { \jmath } ^ { \ast } \nabla ^ { \jmath } y _ { n + 1 } , \qquad \gamma _ { 0 } ^ { \ast } = 1 , \ \gamma _ { \mathbf { I } } ^ { \ast } = - \frac { 1 } { 2 } , \ \gamma _ { 2 } ^ { \ast } = - \frac { 1 } { 1 2 } , \dots
$$

Here we put $y _ { n } = \zeta ^ { n }$ and divide by $\zeta ^ { n + 1 }$ . This gives

$$
\mu = \frac { 1 - 1 / \zeta } { \sum _ { \jmath = 0 } ^ { k } \gamma _ { j } ^ { * } \big ( 1 - 1 / \zeta \big ) ^ { \jmath } } , \qquad \zeta = e ^ { \imath \theta } .
$$

For $k = 1$ this is the implicit trapezoidal rule and is $A$ -stable. For $k = 2 , 3 , \ldots , 6$ the stability domains, though much larger than those of the explicit methods, do not cover $\mathbb { C } ^ { - }$ (see Fig.1.3). Hence these methods are not $A$ -stable.

# Predictor-Corrector Schemes

The inadequacy of the theory incorporating the effect of the corrector equation only for predictor-corrector methods was first discovered through experimental computations on the prototype linear equation

$$
y ^ { \prime } = f ( x , y ) = - 1 0 0 y + 1 0 0 , \quad y ( 0 ) = 0 ,
$$

(...）Very poor correlation of actual errors with the errors expected on the basis of the properties of the corrector equation alone was obtained. This motivated the development of the theory (P.E. Chase 1962)

As we have seen in Sect.II.1, the classical way of computing $y _ { n + 1 }$ from the implicit equations (III.1.8) is to use the result $y _ { n + 1 } ^ { * }$ of the explicit Adams method as a predictor in $\beta _ { k } f ( x _ { n + 1 } , y _ { n + 1 } )$ . This destroys a good deal of the stability properties of the method (Chase 1962). The stability analysis changes as follows: the predictor formula

$$
y _ { n + 1 } ^ { * } = y _ { n } + \mu \bigl ( \gamma _ { 0 } y _ { n } + \gamma _ { 1 } ( y _ { n } - y _ { n - 1 } ) + \gamma _ { 2 } ( y _ { n } - 2 y _ { n - 1 } + y _ { n - 2 } ) + . . . \bigr )
$$

must be inserted into the corrector formula

$$
\begin{array} { r l } & { y _ { n + 1 } = y _ { n } + \mu \Bigl ( \gamma _ { 0 } ^ { * } y _ { n + 1 } ^ { * } + } \\ & { \qquad \gamma _ { 1 } ^ { * } ( y _ { n + 1 } ^ { * } - y _ { n } ) + } \\ & { \qquad \gamma _ { 2 } ^ { * } ( y _ { n + 1 } ^ { * } - 2 y _ { n } + y _ { n - 1 } ) + } \\ & { \qquad \gamma _ { 3 } ^ { * } ( y _ { n + 1 } ^ { * } - 3 y _ { n } + 3 y _ { n - 1 } - y _ { n - 2 } ) + . . . \Bigr ) . } \end{array}
$$

Since there is a $\mu$ in (1.12) and in (1.13), we obtain this time,by putting $y _ { n } = \zeta ^ { n }$ and dividing by $\zeta ^ { n }$ , a quadratic equation for $\mu$ ，

$$
\begin{array} { c } { { A \mu ^ { 2 } + B \mu + C = 0 , } } \\ { { A = \Big ( \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \Big ) \Big ( \displaystyle \sum _ { p = 0 } ^ { k - 1 } \gamma _ { j } \big ( 1 - \frac { 1 } { \zeta } \big ) ^ { p } \Big ) , } } \\ { { B = \big ( 1 - \zeta \big ) \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } + \zeta \displaystyle \sum _ { j = 0 } ^ { k } \gamma _ { j } ^ { * } \big ( 1 - \frac { 1 } { \zeta } \big ) ^ { p } , } } \\ { { C = 1 - \zeta . } } \end{array}
$$

For each $\zeta = e ^ { \imath \theta }$ ,Eq.(1.14) has two roots. These give rise to two root locus curves which determine the stability domain. These curves are represented in Fig.1.4 and compared to those of the original implicit methods. It can be seen that we loose a lot of stability. In particular, for $k \approx 1$ the trapezoidal rule becomes an explicit second order Runge Kutta method and the $A$ -stability is destroyed.

While Chase (1962) studied real eigenvalues only, the general complex case has been stated by Crane & Klopfenstein (1965) and, with beautiful figures, by

![](images/bc87e9f1668cd23900e224c5e32bd4bc47f2fd3a218ec9d5cf5efd2a7a852a29.jpg)  
Fig.1.4. Stability domains for PECE compared to original implicit methods

Krogh (1966). All three papers also searched for procedures with increased stabil-ity domains. This research was brought to perfection by Stetter (1968).

# Nystrim Methods

Thus we see that Milne's method will not handle so simple an equation as $y ^ { \prime } = - y$ ， $y ( 0 ) = 1$ (R.W. Hamming 1959)

... Milne's method has a number of virtues not possessed by its principal rival, the Runge-Kutta method,which are especially important when the order of the system of equations is fairly high $( \mathrm { N } { = } 1 0$ to 30 or more）... (R.W. Hamming 1959)

The explicit Nystrom method (II.1.13) for $k \approx 1$ and 2 is the “explicit midpoint rule”

$$
y _ { n + 1 } = y _ { n - 1 } + 2 h f _ { n }
$$

and leads to the root locus curve

$$
\mu = { \frac { e ^ { i \theta } - e ^ { - i \theta } } { 2 } } = i \sin \theta .
$$

This curve moves up and down the imaginary axis between $\pm i$ and leaves as stability domain just the interval $( - i , + i )$ (see Fig.1.5). All eigenvalues in the interior of the negative half plane lead to instabilities. This is caused by the second root $- 1$ of $\varrho \{ \zeta \}$ which moves out of the unit circle when $\mu$ goes West. This famous phenomenon is called the“weak instability” of the midpoint rule and was the “entry point” of Dahlquist's stability-career (Dahlquist 1951). The graphs of Fig.II.9.2 nicely show the (weak) instability of the numerical solution.

The implicit Milne-Simpson method (III.1.15) for $k \approx 2$ and 3 is

$$
y _ { n + 1 } = y _ { n - 1 } + h \Big ( \frac { 1 } { 3 } f _ { n + 1 } + \frac { 4 } { 3 } f _ { n } + \frac { 1 } { 3 } f _ { n - 1 } \Big )
$$

and has the root locus curve

$$
\mu = { \frac { e ^ { i \theta } - e ^ { - i \theta } } { { \frac { 1 } { 3 } } e ^ { i \theta } + { \frac { 4 } { 3 } } + { \frac { 1 } { 3 } } e ^ { - i \theta } } } = 3 i ~ { \frac { \sin \theta } { \cos \theta + 2 } } ,
$$

which moves up and down the imaginary axis between $\pm i \sqrt { 3 }$ . Thus its behaviour is similar to the explicit Nystrom method with a slightly larger stability interval.

The higher order Nystrom and Milne-Simpson methods have root locus curves which are oriented the wrong way round (see Fig.1.5). Their stability domains therefore reduce to the smallest possible set (for stable methods): just the origin.

![](images/a1346895f7d9be2820a61877cbc06e369193149d27d2d15c603a404b5d25d9ca.jpg)  
Fig.1.5. Root locus curves for Nystrom and Milne methods

![](images/6e76881778dc8923fdc8151af5b3d3b5a48d857112d3215739facf11d346fa05.jpg)  
Fig.1.6. Root locus curves and stability domains of BDF methods

# BDF

The backward differentiation formulas $\begin{array} { r } { \sum _ { j = 1 } ^ { k } \frac { 1 } { j } \nabla ^ { j } y _ { n + 1 } = h f _ { n + 1 } } \end{array}$ (see Equation (III.1.22')) have the root locus curves given by

$$
\mu = \sum _ { j = 1 } ^ { k } { \frac { 1 } { j } } \left( 1 - { \frac { 1 } { \zeta } } \right) ^ { j } = \sum _ { j = 1 } ^ { k } { \frac { 1 } { j } } \left( 1 - e ^ { - i \theta } \right) ^ { j } .
$$

For $k = 1$ we have the implicit Euler method with stability domain $S = \{ \mu ; | \mu -$ $1 | \geq 1 \}$ .For $k = 2$ the root locus curve (see Fig.1.6) has $\operatorname { R e } \left( \mu \right) = { \textstyle { \frac { 3 } { 2 } } } - 2 \cos \theta +$ ${ \frac { 1 } { 2 } } \cos 2 \theta$ $\geq 0$ $\theta$ $A$   
$k = 3 , 4 , 5$   
stability on a part of the imaginary axis. For $k \geq 7$ , as we know, the formulas are unstable anyway, even at the origin.

# The Second Dahlquist Barrier

I searched for a long time, finally Professor Lax showed me the Riesz-Herglotz theorem and I knew that I had my theorem.

(G. Dahlquist 1979)

Theorem 1.3. If the multistep method (1.1) is $A$ -stable, then

$$
\mathrm { R e } \left( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \qquad f o r \qquad | \zeta | > 1 .
$$

For irreducible methods the converse is also true: (1.18) implies $A$ -stability.

Proof. If the method is $A$ -stable then all roots of (1.6) must satisfy $\vert \zeta \vert \le 1$ whenever $\operatorname { R e } \mu \leq 0$ . The logically equivalent statement ( $\mathrm { \ R e } \mu > 0$ whenever $| \zeta | > 1 )$ yields (1.18) since by (1.6) $\mu = \varrho ( \zeta ) / \sigma ( \zeta )$

Suppose now that (1.18) holds and that the method is irreducible. Fix a $\mu _ { 0 }$ with $\mathrm { R e } \mu _ { 0 } \leq 0$ and let $\zeta _ { 0 }$ be a root of (1.6). We then have $\sigma ( \zeta _ { 0 } ) \neq 0$ (otherwise the method would be reducible). Hence $\mu _ { 0 } = \varrho ( \zeta _ { 0 } ) / \sigma ( \zeta _ { 0 } )$ and it follows from (1.18) that $| \zeta _ { 0 } | \le 1$ . We still have to show that $\zeta _ { 0 }$ is a simple root if $| \zeta _ { 0 } | = 1$ By a continuity argument it follows from (1.18） that $| \zeta _ { 0 } | = 1$ and $\mathrm { R e } \mu _ { 0 } < 0$ are contradictory. Therefore, it remains to prove that for $\mathrm { R e } \mu _ { 0 } = 0$ a root satisfying $| \zeta _ { 0 } | = 1$ must be simple. In a neighbourbood of such a root we have

$$
\frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } - \mu _ { 0 } = C _ { 1 } ( \zeta - \zeta _ { 0 } ) + C _ { 2 } ( \zeta - \zeta _ { 0 } ) ^ { 2 } + . . .
$$

and (1.18) implies that $C _ { 1 } \neq 0$ . This,however, is only possible if $\zeta _ { 0 }$ is a simple root of (1.6). □

In all the above examples we have not yet seen an $A$ -stable multistep formula of order $p \geq 3$ . The following famous theorem explains this observation.

Theorem 1.4 (Dahlquist 1963). An $A$ -stable multistep method must be of order $p \leq 2$ . If the order is 2, then the error constant satisfies

$$
C \leq - { \frac { 1 } { 1 2 } } .
$$

The trapezoidal rule is the only $A$ -stable method of order 2 with $C = - 1 / 1 2$

Proof. Dahlquist's first proof of this theorem is difficult. More elementary versions emerged in Widlund (1967),in lecture notes of W. Liniger (Univ. of Neuchatel 1971) and in the book of Grigorieff (1977, vol.2, p. 218).

We start by recalling some formulas from Volume I: Eq. (ii) of Theorem III.2.4 and Eq. (III.2.7) yield

$$
\varrho \big ( e ^ { h } \big ) - h \sigma \big ( e ^ { h } \big ) = C _ { p + 1 } h ^ { p + 1 } + \ldots \qquad \mathrm { f o r } \quad h  0 .
$$

From the consistency conditions (III.2.6) we have

$$
\varrho \big ( e ^ { h } \big ) = \varrho \big ( 1 + h + \ldots \big ) = \varrho ( 1 ) + \varrho ^ { \prime } ( 1 ) h + \ldots = \sigma ( 1 ) h + \ldots .
$$

We divide (1.20) by $h \varrho ( e ^ { h } )$ and obtain

$$
{ \frac { 1 } { h } } - { \frac { \sigma ( e ^ { h } ) } { \varrho ( e ^ { h } ) } } = C h ^ { p - 1 } + \ldots \qquad { \mathrm { f o r } } \quad h \to 0
$$

where $C$ is the error constant (III.2.13). With $\zeta = e ^ { h }$ this becomes

$$
{ \frac { 1 } { \log \zeta } } - { \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } = C ( \zeta - 1 ) ^ { p - 1 } + . . . \qquad { \mathrm { f o r } } \quad \zeta \to 1 .
$$

In this formula we put $p = 2$ . Whenever the method is of higher order,we have $C = 0$ . When the order of the method is one,we have nothing to prove. The same formula for the trapezoidal rule for which $\varrho _ { \mathcal { T } } ( \zeta ) = \zeta - 1$ ， $\sigma _ { \mathscr { T } } ( \zeta ) \overset { = } { = } \frac { 1 } { 2 } \big ( \zeta + 1 \big )$ ， becomes by series expansion (or by using Table III.2.1)

$$
\frac { 1 } { \log \zeta } - \frac { \sigma _ { T } ( \zeta ) } { \varrho _ { T } ( \zeta ) } = - \frac { 1 } { 1 2 } ( \zeta - 1 ) + \dots . \qquad \mathrm { f o r } \quad \zeta \to 1 .
$$

The idea is now to subtract the two formulas and obtain

$$
d ( \zeta ) : = \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } - \frac { \sigma _ { T } ( \zeta ) } { \varrho _ { T } ( \zeta ) } = \left( - C - \frac { 1 } { 1 2 } \right) ( \zeta - 1 ) + \ldots \quad \quad \mathrm { f o r } \quad \zeta \to 1 .
$$

From(1.18) we have that

$$
\operatorname { R e } \left( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \quad \mathrm { ~ o r ~ e q u i v a l e n t l y } \quad \operatorname { R e } \left( \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right) > 0 \quad \mathrm { f o r ~ } | \zeta | > 1 .
$$

The point here is that for the trapezoidal rule this $\operatorname { R e } \left( \dots \right)$ is zero for $| \zeta | = 1$ since this method has precisely $\mathbb { C } ^ { - }$ as stability domain. Hence from (1.24) we obtain

$$
\operatorname* { l i m } _ { | \zeta | > 1 } \mathrm { R e } d ( \zeta ) \geq 0 \qquad \mathrm { f o r } \quad | \zeta _ { 0 } | = 1 .
$$

The poles of $d ( \zeta )$ are the roots of $\varrho ( \zeta )$ , which,by stability,are not allowed outside the unit circle. Thus,by the maximum principle,(1.26) remains true everywhere outside the unit circle. Choosing then $\zeta = 1 + \varepsilon$ with $\mathrm { R e } \varepsilon > 0$ and $| \varepsilon |$ small, we see from (1.24) that either $- C - { \textstyle { \frac { 1 } { 1 2 } } } > 0$ or $d ( \zeta ) \equiv 0$ . This concludes the proof.□

# Exercises

1. The Milne-Simpson methods for $k = 4$ and 5 satisfy $\mathrm { R e } \left( \varrho ( \zeta ) / \sigma ( \zeta ) \right) \geq 0$ for $| \zeta | = 1$ ． Since their order is higher than 2,this seems to be in contradiction with the above proof of Theorem 1.4. Explain.

2.For the explicit midpoint rule (1.15),do the endpoints $\pm i$ of the stability region belong to $S : ?$ Study the (possible) stability of this method applied with $h = 1$ to $u ^ { \prime } = v$ ， $v ^ { \prime } = - u$ .

3. Compute for the explicit and implicit Adams methods the largest $\lambda _ { 0 } \in \mathbb { R }$ such that the real interval $[ - \lambda _ { 0 } , 0 ]$ lies in $S$ . Show that for the $k$ -step explicit Adamsmthods we hae $\lambda _ { 0 } = 2 / u _ { k }$ with $\begin{array} { r } { \mathcal { U } _ { k } = \sum _ { \jmath = 0 } ^ { k - 1 } 2 ^ { \jmath } \gamma _ { \jmath } } \end{array}$ $u _ { 1 } = 1$ $u _ { 2 } = 2$ $u _ { 3 } = 1 1 / 3$ ， $u _ { 4 } = 2 0 / 3$ ， $u _ { 5 } = 5 5 1 / 4 5 , \ldots )$ . The use of generating functions (see Sect.III.1) allow us to show that

$$
\sum _ { j = 1 } ^ { \infty } u _ { k } t ^ { k } = \left( - 1 + { \frac { 2 } { 1 - t } } - { \frac { 1 } { 1 - 2 t } } \right) \log ( 1 - 2 t ) ,
$$

a series with convergence radius $1 / 2$ . This explains why these stability domains decrease so rapidly.

Hint. Just set $\theta = \pi$ in the root locus curve.

4.Prove that the stability region of the $k$ -step,implicit Adams methods is of finite size for every $k \geq 2$ Hint. Show that $( - 1 ) ^ { k } \sigma ( - 1 ) < 0$ , so that $\sigma$ has a real negative root, smaller than $- 1$ .

5. a) Show that all 2-step methods of order 2 are given by

$$
\begin{array} { l } { \varrho ( \zeta ) = ( \zeta - 1 ) ( \alpha \zeta + 1 - \alpha ) \qquad } \\ { \sigma ( \zeta ) = ( \zeta - 1 ) ^ { 2 } \beta + ( \zeta - 1 ) \alpha + ( \zeta + 1 ) / 2 } \end{array}
$$

(which are irreducible for $\alpha \neq 2 \beta$ ).

b) The method is stable at O iff $\alpha \ge 1 / 2$

c) The method is stable at $\infty$ iff

$$
\alpha \geq 1 / 2 \qquad \mathrm { a n d } \qquad \beta > \alpha / 2 .
$$

Apply the Schur-Cohn criterion (Sect.II.3, Exercise 4).

d) The method is $A$ -stable iff (1.27) holds.

Hint.

$$
{ \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } = { \frac { 1 } { 2 } } \cdot { \frac { \zeta + 1 } { \zeta - 1 } } + \bigl ( \beta - { \frac { \alpha } { 2 } } \bigr ) \cdot { \frac { \zeta - 1 } { \alpha \zeta + 1 - \alpha } } .
$$

# V.2“Nearly” A-Stable Multistep Methods

We are not atempting to disprove Dahlquist's theorems but are trying to get round the conditions they impose ...

(J. Cash 1979)

Dahlquist's condition $p \leq 2$ for the order of an $A$ -stable linear multistep method is a severe restriction for efficient practical calculations of high precision. There are only two ways of "breaking” this barrier:

either weaken the condition;   
$\bullet$ or strengthen the method.

These two points will occupy our attention in this and in the following section.

# $A ( \alpha )$ -Stability and Stiff Stability

It is the purpose of this note to show that a slightly different stability requirement permits methods of higher accuracy.

(O. Widlund 1967)

The angle $\alpha$ is only one of a number of parameters which have been proposed for measuring the extent of the stability region. But it is probably the best such measure ...

(Skeel& Kong 1977)

Many important classes of practical problems do not require stability on the entire left half-plane $\mathbb { C } ^ { - }$ . Further,for eigenvalues on the imaginary axis, the solutions are often highly oscillatory and one is then forced anyhow to restrict the step size “to the highest frequency present in order to represent the signal" (Gear 1971, p. 214).

Definition 2.1 (Widlund 1967). A convergent linear multistep method is $A ( \alpha ) -$ stable, $0 < \alpha < \pi / 2$ ,if

$$
S \supset S _ { \alpha } = \{ \mu ; | \arg ( - \mu ) | < \alpha , \mu \neq 0 \} .
$$

A method is $A ( 0 )$ -stable if it is $A ( \alpha )$ -stable for some (sufficiently small) $\alpha > 0$ ·

Similarly, Gear (1971) required in his famous concept of“stiff stability”that

$$
S \supset \{ \mu ; \mathrm { R e } \mu < - D \}
$$

for some $D > 0$ and that the method be “accurate” in a rectangle $- D \leq \operatorname { R e } \mu \leq$ $a , \ - \theta \leq \operatorname { I m } \mu \leq \theta$ for some $a > 0$ and $\theta$ about $\pi / 5$ . Many subsequent writers

didn't like the inaccurate meaning of “accurate” in this definition and replaced it by something else. For example Jeltsch (1976) required that in addition to (2.2),

$$
| \zeta _ { 1 } ( \mu ) | > | \zeta _ { \iota } ( \mu ) | , \quad i = 2 , \ldots , k \qquad \mathrm { i n } \quad | \mathrm { R e } \mu | \leq a , | \mathrm { I m } \mu | \leq \theta ,
$$

where $\zeta _ { 1 } ( \mu )$ is the analytic continuation of the principal root $\zeta _ { 1 } ( 0 ) = 1$ of (1.6). Also, the rectangle given by

$$
| \mathrm { I m } \mu | \leq \theta , \qquad - D \leq \mathrm { R e } \mu \leq - a
$$

should belong to $S$

Other concepts are $A _ { 0 }$ -stable (Cryer 1973) if

$$
| \zeta _ { \ i } ( x ) | < 1 , \quad i = 1 , \ldots , k \qquad \mathrm { f o r } \quad - \infty < x < 0
$$

and $\mathring { A }$ -stable (a joke of O. Nevanlinna 1979) if

$$
( - \infty , 0 ] \subset S .
$$

Of course, we have

$$
A ( 0 ) { \mathrm { - s t a b l e } } \ \Longrightarrow \ A _ { 0 } { \mathrm { - s t a b l e } } \ \Longrightarrow \ \mathring { A } { \mathrm { - s t a b l e } }
$$

but neither implication is reversible (Exercise 3; see also “Theorem $1 ^ { \circ }$ of Jeltsch 1976).

The BDF methods (1.18) satisfy (2.1） for $A ( \alpha )$ -stability and (2.2) for stiff stability with the values

<table><tr><td>k</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>α</td><td>90°</td><td>90°</td><td>86.030</td><td>73.350</td><td>51.84°</td><td>17.84°</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0.083</td><td>0.667</td><td>2.327</td><td>6.075</td></tr></table>

# High Order $A ( \alpha )$ -Stable Methods

Dill and Gear ... and Jain and Srivastava ... have used computers to construct stiffly stable methods of orders eight and eleven, respectively, but were unable to construct higher order stiffly stable methods. Even though we have shown here that $A _ { 0 }$ -stable methods of arbitrarily high order exist,we conjecture that $A ( 0 ) \cdot$ stable linear multistep methods of higher order, of order greater than 20 say,do not exist. (Cryer 1973)

Widlund (1967) showed that for every $\alpha < \pi / 2$ ， $\alpha$ arbitrarily close to $\pi / 2$ , there exist $A ( \alpha )$ -stable multistep methods of order $p = k$ for $p = 3$ and $p = 4$ . It is now an interesting question whether such methods also exist for higher orders. Well, the answer consists of good news and bad news.

First the good news. The conjecture of Cryer (see quotation) was quickly dis-proved by combining Cryer's $A _ { 0 }$ -stable methods with the result of Jeltsch (1976)

which says that certain $A _ { 0 }$ -stable methods are also $A ( \alpha )$ -stable. The following theorem shows that $\alpha$ can even be chosen arbitrarily close to $\pi / 2$ ：

Theorem 2.2 (Grigorieff & Schroll 1978). Let $\alpha < \pi / 2$ be given. Then for every $k \in \mathbb { N }$ there exists an $A ( \alpha )$ -stable linear $k$ -step method of order $p = k$

Proof. For $p = k = 2$ the two-step BDF method which is $A$ -stable,and hence $A ( \alpha _ { 2 } )$ -stable for every $\alpha _ { 2 } \leq \pi / 2$ ， does the job. For $k$ arbitrary,we intercalate $k - 2$ values between $\alpha$ and $\pi / 2$ ，

$$
\alpha < \alpha _ { k - 1 } < \alpha _ { k - 2 } < \ldots < \alpha _ { 3 } < \alpha _ { 2 } \leq { \frac { \pi } { 2 } } ,
$$

and extend the method step by step with the help of Lemma 2.3.

Lemma 2.3. Suppose an $A ( \alpha )$ -stable $k$ -step method of order $p$ is given with

$$
\begin{array} { r l } { \varrho ( \zeta ) \neq 0 \quad } & { { } i f | \zeta | = 1 , \zeta \neq 1 } \\ { \sigma ( \zeta ) \neq 0 \quad } & { { } i f | \zeta | = 1 . } \end{array}
$$

Then for every $\widetilde { \alpha } < \alpha$ there exists an $A ( \widetilde { \alpha } )$ -stable $\left( k + 1 \right)$ -step method of order $p + 1$ which also satisfies (2.9).

The proof follows very closely the ideas of Jeltsch & Nevanlinna (1982): Let $\varrho ( \zeta )$ and $\sigma ( \zeta )$ represent the given $k$ -step method with order condition

$$
\frac { \varrho ( \zeta ) } { \log \zeta } - \sigma ( \zeta ) = C _ { p + 1 } ( \zeta - 1 ) ^ { p } + \mathcal { O } \big ( ( \zeta - 1 ) ^ { p + 1 } \big ) .
$$

If we multiply $\varrho$ and $\sigma$ by $( \zeta - 1 )$ we formally increase the order by 1 and at the same time leave the root locus curve unchanged. Everything seems to be proved. However, the new $\varrho$ -polynomial would have a double root at $\zeta = 1$ and would thus lead to an unstable method. We therefore choose $\varepsilon > 0$ and multiply (2.10） by $\left( \zeta - 1 + \varepsilon \right)$ ，which moves the root slightly inside the unit circle. We then obtain a new method of order $p + 1$ if we put

$$
\begin{array} { r l } & { \widetilde { \varrho } ( \zeta ) = \varrho ( \zeta ) \left( \zeta - 1 + \varepsilon \right) } \\ & { \widetilde { \sigma } ( \zeta ) = \sigma ( \zeta ) \left( \zeta - 1 + \varepsilon \right) + \varepsilon C _ { p + 1 } ( \zeta - 1 ) ^ { p } . } \end{array}
$$

Since $p = k + 2$ is excluded (by Theorem III.3.9 methods with $p = k + 2$ are symmetric and violate Hypothesis (2.9a)),both polynomials $\widetilde { \varrho }$ and $\widetilde { \sigma }$ are of degree $\leq k + 1$ . Now the formula

$$
\frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } = \frac { \varepsilon C _ { p + 1 } ( \zeta - 1 ) ^ { p } } { \varrho ( \zeta ) ( \zeta - 1 + \varepsilon ) }
$$

allows us to compare, for $\varepsilon$ small, the root-locus curves of the two methods. The fact that we are working with $\sigma ( e ^ { i \theta } ) / \varrho ( e ^ { \imath \theta } ) = 1 / \mu$ instead of $\mu = \varrho \big ( e ^ { \imath \theta } \big ) / \sigma \big ( e ^ { \imath \theta } \big )$

does not matter, because the transformation $\mu \mapsto 1 / \mu$ maps the sector of Definition 2.1 onto itself. Because of Hypothesis (2.9a),1 is the only (simple) root of $\varrho ( \zeta )$ on the unit circle, therefore

$$
\left| { \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } } - { \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } } \right| \leq C \cdot \varepsilon { \frac { | \zeta - 1 | ^ { p - 1 } } { | \zeta - 1 + \varepsilon | } } \qquad { \mathrm { f o r } } \quad \zeta = e ^ { \imath \theta } .
$$

A small obstacle still separates us from “endless pleasure,endless love,Semele enjoys above": the denominator $| \zeta - 1 + \varepsilon |$ ，which becomes small for $\varepsilon \to 0$ and $\theta  0$ .For $p > 1$ ,this “small’ denominator is simply balanced by one of the factors $| \zeta - 1 |$ from the numerator and we have

$$
\left| \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right| \leq \widehat { C } \cdot \varepsilon
$$

which means uniform pointwise convergence of ${ \widetilde \sigma } ( \zeta ) / { \widetilde \varrho ( \zeta ) }$ to $\sigma ( \zeta ) / \varrho ( \zeta )$ if $\varepsilon \to 0$ Since $\sigma ( \zeta ) / \varrho ( \zeta )$ is bounded away from the origin (Hypothesis (2.9b)), this also means uniform convergence of the angles.

This is already sufficient to prove Theorem 2.2, where we always have $p \geq 2$ . However,Lemma 2.3 remains valid for $p = 1$ too: the critical region is when $\theta  0$ ， in which case $\left| \sigma ( e ^ { \imath \theta } ) / \varrho ( e ^ { \imath \theta } ) \right|$ and $| \widetilde { \sigma } ( e ^ { \imath \theta } ) / \widetilde { \varrho } ( e ^ { \imath \theta } ) |$ tend to infinity like $C o n s t / \theta$ ， Instead of (2.14) we have for $p = 1$

$$
\left| \frac { \widetilde { \sigma } ( \zeta ) } { \widetilde { \varrho } ( \zeta ) } - \frac { \sigma ( \zeta ) } { \varrho ( \zeta ) } \right| \leq \frac { C \varepsilon } { | \zeta - 1 + \varepsilon | } = \mathcal { O } \Big ( \frac { \varepsilon } { \theta } \Big ) .
$$

Thus the angle (seen from the origin) between $\widetilde { \sigma } ( \zeta ) / \widetilde { \varrho } ( \zeta )$ and $\sigma ( \zeta ) / \varrho ( \zeta )$ is $\mathcal { O } ( \varepsilon )$

# Approximating Low Order Methods with High Order Ones

The above proof of Lemma 2.3 actually shows more than angle-boundedness of the root locus curve, namely uniform convergence of the root locus curve of a high order method to that of a lower order one. This leads to the following theorem of Jeltsch & Nevanlinna (1982):

Theorem 2.4. Let a linear stable $k$ -step method of order $p$ and stability domain $S$ be given which satisfies $( 2 . 9 a )$ Then to any closed set $\Omega \subset \operatorname { I n t } S \subset { \overline { { \mathbb { C } } } }$ and any $K \in \mathbb { N }$ there exists a linear $k + K$ -step method of order $p + K$ whose stability domain $\widetilde { S }$ satisfies

$$
\widetilde { S } \supset \Omega .
$$

Moreover if the first method is explicit, the higher-order method is also explicit.

Proof. The proof is similar to that of Lemma 2.3. Instead of the sequence (.8) we use a sequence of embedded closed and open subsets between $\Omega$ and $S$ (Urysohn's Lemma). Hypothesis (2.9b) is ruled out by passing to the compactified topology of $\overline { { \mathbb { C } } } = \mathbb { C } \cup \{ \infty \}$ □

Remark. No method with non-empty Int $S$ of practical interest violates Hypothesis (2.9a). Nevertheless, Theorem 2.4 remains valid without this hypothesis, but the proof becomes more complicated (see “Lemma $3 . 6 ^ { \mathfrak { s } }$ of Jeltsch & Nevanlinna 1982).

# A Disc Theorem

Another weakening of $A$ -stability is to require stability for

$$
D _ { r } = \{ \mu \ ; \ | \mu + r | \leq r \} ,
$$

which is a disc of radius $\mathscr { r }$ in $\mathbb { C } ^ { - }$ tangent to the imaginary axis at the origin. Theorems about stability in $D _ { r }$ are stronger than theorems about $A ( \alpha )$ -stability for eigenvalues close to the origin. The following result is,again,due to Jeltsch & Nevanlinna (1982):

Theorem 2.5. Let a linear $k$ -step method of order $p$ be given with $S \supset D _ { r }$ . Then for any $\widetilde r < r$ and any $K \in \mathbb { N }$ there exists_ a linear $k + { \bar { k } } ^ { \prime }$ -step method of order $p + K$ whose stability domain $\widetilde { S }$ satisfies $ { \widetilde { S } } \supset D _ {  { \widetilde { r } } }$ ·

Proof. The map $\mu \mapsto 1 / \mu$ used in the proof of Lemma 2.3 maps the exterior of $D _ { r }$ onto the half-plane

$$
\left\{ \mu \in \mathbb { C } \mathrm { ~ ; ~ } \operatorname { R e } \mu > - \frac { 1 } { 2 r } \right\} .
$$

Therefore the uniform convergence established in (2.14) also covers the new situation if $p > 1$ . The case $p = 1$ , however, needs a more careful study and we refer to the original paper of Jeltsch & Nevanlinna (1982, pp. 277-279). □

# Accuracy Barriers for Linear Multistep Methods

Now here is the “bad news": high order $A ( \alpha )$ -stable methods, for $\alpha$ close to $\pi / 2$ , cannot be of practical use,or in other words: “the second Dahlquist barrier cannot be broken". The reason is simply that high order alone is not sufficient for high accuracy,because the methods then have enormous error constants. Jeltsch & Nevanlinna (1982) give an impressive staccato (from“Theorem $4 . 1 ^ { \circ }$ to “Lemma 4.15"） of lower bounds for error constants and Peano kernels of methods having large stability domains. The Peano kernels, the most serious measures for the error, are defined by the formulas (see (III.2.15) and (III.2.3) of Volume I)

$$
\begin{array} { r l r } & { } & { L ( x ) = h ^ { q + 1 } \displaystyle \int _ { - \infty } ^ { \infty } \check { K } _ { q } ( - s ) y ^ { ( q + 1 ) } ( x + s h ) d s } \\ & { } & { \quad = \displaystyle \sum _ { j = 0 } ^ { k } \bigl ( \alpha _ { j } y ( x + \jmath h ) - h \beta _ { j } y ^ { \prime } ( x + j h ) \bigr ) . } \end{array}
$$

The kernels $\check { K } _ { q } ( - s ) = K _ { q } ( s )$ are zero outside the interval $0 \le s \le k$ and are piecewise polynomials given by complicated formulas (see (II.2.16)) which appear not very attractive to work with.

However, the formulas simplify if we use the Fourier transform which, for a function $f ( x )$ , is defined by

$$
{ \widehat { f } } ( \xi ) = \int _ { - \infty } ^ { \infty } e ^ { - \imath x \xi } f ( x ) d x .
$$

We obtain $\widehat { L }$ from (2.17) by insertion of the definitions,several integrations by parts and transformations of double integrals:

$$
\begin{array} { c } { { \widehat { L } ( \xi ) = h ^ { q + 1 } \widehat { K _ { q } } ( h \xi ) \cdot y ^ { ( q + 1 ) } ( \xi ) } } \\ { { = \widehat { K _ { q } } ( h \xi ) ( i h \xi ) ^ { q + 1 } \widehat { y } ( \xi ) , } } \end{array}
$$

and from (2.18)

$$
\widehat { L } ( \xi ) = \big ( \varrho \big ( e ^ { \imath h \xi } \big ) - i h \xi \sigma \big ( e ^ { \imath h \xi } \big ) \big ) \cdot \widehat { y } \big ( \xi \big ) .
$$

Thus (2.20) and (2.22) give

$$
\widehat { K _ { q } } ( - \xi ) = \widehat { K _ { q } } ( \xi ) = \big ( \varrho \big ( e ^ { \imath \xi } \big ) - i \xi \sigma \big ( e ^ { \imath \xi } \big ) \big ) \big ( i \xi \big ) ^ { - ( q + 1 ) } ,
$$

a nice formula, involving the polynomials $\varrho$ and $\sigma$ ， with which we are better acquainted.

What about the usefulness of $\widehat { \bar { K _ { q } } }$ for error estimates? Well, it is the Parseval identity (Exercise 4)

$$
\| f \| _ { L ^ { 2 } ( - \infty , \infty ) } = \frac { 1 } { \sqrt { 2 \pi } } \| \widehat { f } \| _ { L ^ { 2 } ( - \infty , \infty ) }
$$

which allows us to obtain the $L ^ { 2 }$ -estimate for the error

$$
\begin{array} { r } { \| L \| _ { L ^ { 2 } ( - \infty , \infty ) } \leq h ^ { q + 1 } \| \widehat { K _ { q } } \| _ { L ^ { \infty } } \cdot \| y ^ { ( q + 1 ) } \| _ { L ^ { 2 } } , } \end{array}
$$

as follows:

$$
\begin{array} { l } { \displaystyle | | L | | _ { L ^ { 2 } ( - \infty , \infty ) } ^ { 2 } = \frac { 1 } { 2 \pi } | | \widehat { L } | | _ { L ^ { 2 } ( - \infty , \infty ) } ^ { 2 } } \\ { \displaystyle = \frac { h ^ { 2 q + 2 } } { 2 \pi } \int _ { - \infty } ^ { \infty } \left| \widehat { K } _ { q } ( \xi ) \right| ^ { 2 } | y ^ { ( q + 1 ) } ( \xi ) | ^ { 2 } d \xi } \\ { \displaystyle \leq \frac { h ^ { 2 q + 2 } } { 2 \pi } \operatorname* { m a x } | \widehat { K } _ { q } ( \xi ) | ^ { 2 } \cdot \int _ { - \infty } ^ { \infty } \left| y ^ { ( q + 1 ) } ( \xi ) \right| ^ { 2 } d \xi } \\ { \displaystyle = \frac { h ^ { 2 q + 2 } } { 2 \pi } | | \widehat { K } _ { q } | | _ { L ^ { \infty } } ^ { 2 } \cdot | | y ^ { ( q + 1 ) } | | _ { L ^ { 2 } } ^ { 2 } } \\ { \displaystyle = h ^ { 2 q + 2 } | | \widehat { K } _ { q } | | _ { L ^ { \infty } } ^ { 2 } \cdot | | y ^ { ( q + 1 ) } | | _ { L ^ { 2 } } ^ { 2 } . } \end{array}
$$

In order that the obtained estimates (2.25) for $L$ express the actual errors of the numerical solution, we adopt throughout this section the normalization $\sigma ( 1 ) = 1$ (cf. Eq. (III.2.13)).

And here is the theorem which tells us that linear multistep methods of order $p > 2$ and“large” stability domain cannot be precise:

Theorem 2.6 (Jeltsch & Nevanlinna 1982). Consider $k$ -step methods of order $p >$ 2, normalized by $\sigma ( 1 ) = 1$ ,for which the disc $D _ { r }$ of(2.15) is in the stability domain $S$ . Then there exists a constant $C > 0$ (depending on $k , p , q$ ; but independent of $\mathscr { r }$ )such that the Fourier transform of the Peano kernel $K _ { q } ^ { \prime } ~ ( \it q \leq p ) ~ s a t i s f i e s$

$$
\| \widehat { K _ { q } } \| _ { \infty } \geq C \Big ( \frac { r } { 3 } \Big ) ^ { p - 2 } .
$$

The proof of Jeltsch & Nevanlinna is in two steps:

a) The stability requirement forces some coefficients $a _ { \scriptscriptstyle 3 }$ of $R ( z )$ to be large (Lemma 2.7 below), where as in (I.3.17)

$$
\begin{array} { l } { { \displaystyle R ( z ) = \left( \frac { z - 1 } 2 \right) ^ { k } \varrho \left( \frac { z + 1 } { z - 1 } \right) = \sum _ { j = 0 } ^ { k } a _ { j } z ^ { j } } } \\ { { \displaystyle S ( z ) = \left( \frac { z - 1 } 2 \right) ^ { k } \sigma \left( \frac { z + 1 } { z - 1 } \right) = \sum _ { j = 0 } ^ { k } b _ { j } z ^ { j } } . }  \end{array}
$$

b） $\| \widehat { \bar { K _ { q } } } \| _ { L ^ { \infty } }$ can be bounded from below by $\operatorname* { m a x } _ { \boldsymbol { \jmath } } a _ { \boldsymbol { \jmath } }$ (Lemma 2.8).

Lemma 2.7. If $D _ { r } \subset S$ and $p > 2$ then

$$
a _ { k - \jmath } \geq \left( { \frac { r } { 3 } } \right) ^ { \jmath - 1 } \cdot a _ { k - 1 } = \left( { \frac { r } { 3 } } \right) ^ { \jmath - 1 } \cdot 2 ^ { 1 - k } \qquad f o r \quad j = 2 , \ldots , p - 1 .
$$

Proof. Stability in $D _ { r }$ means that for $\mu \in D _ { r }$ all roots of $\varrho \big ( \zeta \big ) - \mu \sigma \big ( \zeta \big ) = 0$ lie in $| \zeta | \le 1$ . Hence

$$
\varrho ( \zeta ) / \sigma ( \zeta ) \notin D _ { r } \qquad \mathrm { f o r } \quad | \zeta | > 1 .
$$

Applying the Graeco-Roman transformation $\zeta = ( z + 1 ) / ( z - 1 )$ and using (2.16) this means that

$$
\mathrm { R e } \frac { S ( z ) } { R ( z ) } > - \frac { 1 } { 2 r } \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0
$$

or

$$
\mathrm { R e } \ \frac { 2 r S ( z ) + R ( z ) } { R ( z ) } > 0 \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0 .
$$

Next, we must consider the order conditions (Lemma III.3.7 and Exercise $9$ of Sect. III.3)

$$
R ( z ) \Big ( \frac { z } { 2 } - \frac { 1 } { 6 z } - \frac { 2 } { 4 5 z ^ { 3 } } - \ldots \Big ) - S ( z ) = { \mathcal O } \Big ( \Big ( \frac { 1 } { z } \Big ) ^ { p - k } \Big ) , \quad z \to \infty .
$$

This shows that $R ( z ) = \mathcal { O } ( z ^ { k - 1 } )$ ， $S ( z ) = \mathcal { O } ( z ^ { k } )$ ,but $2 S ( z ) - z R ( z ) = \mathcal { O } \left( z ^ { k - 1 } \right) .$ Thus we subtract $\mathscr { r } z$ from (2.32) in order to lower the degree of the numerator. The

resulting function again satisfies

$$
\mathrm { R e } \ \frac { r ( 2 S ( z ) - z R ( z ) ) + R ( z ) } { R ( z ) } > 0 \qquad \mathrm { f o r } \quad \mathrm { R e } z > 0
$$

because of $\mathrm { R e } \left( r z \right) = 0$ on $z = i y$ and the maximum principle (an idea similar to that of Lemma IV.5.21). The function (2.34) can therefore have no zeros in $\mathbb { C } ^ { + }$ (since by Taylor expansion all arguments of a function appear in a complex neighbourhood of a zero). Therefore the numerator of (2.34) must have non-negative coefficients (cf. the proof of Lemma II.3.6). Multiplying out (2.33) and (2.34) we obtain for the coeficient of $z ^ { k - 1 } \ ( j \leq p - 1 )$ ：

$$
0 \leq r \left( - \frac 1 3 a _ { k - \jmath + 1 } - \frac { 4 } { 4 5 } a _ { k - \jmath + 3 } - . . . \right) + a _ { k - \jmath }
$$

or by simplifying (cf. Lemmas III.3.8 and III.3.6)

$$
\frac { r } { 3 } a _ { k - \jmath + 1 } \leq a _ { k - \jmath } .
$$

Using $a _ { k - 1 } = 2 ^ { 1 - k } ~ \varrho ^ { \prime } ( 1 ) = 2 ^ { 1 - k }$ (see Lemma II.3.6), this leads to (2.29).

Lemma 2.8. There exists $C > 0$ (depending on $k , p$ and $q$ with $q = 0 , 1 , \ldots , p )$ with the following property: if $0 \in S$ ,then

$$
\| \widehat { K _ { q } } \| _ { L ^ { \infty } } \geq C \cdot \operatorname* { m a x } _ { \jmath } a _ { \jmath } .
$$

Proof. We set $e ^ { \imath \xi } = \zeta , \xi = - \imath \log \zeta$ in Eq.(2.23) so that the maximum must be taken over the set $| \zeta | = 1$ . Then we introduce $\zeta = ( z + 1 ) / ( z - 1 )$ and take the maximum over the imaginary axis. This gives with (2.27) and (2.28)

$$
\big \| \widehat { K _ { q } } \big \| _ { L ^ { \infty } } = \operatorname* { s u p } _ { t } \underbrace { \bigg | \frac { 1 } { ( i t ) ^ { k } } \left( \frac { R ( i t ) } { \log \frac { i t + 1 } { t t - 1 } } - S ( i t ) \right) \bigg | } _ { \Phi ( t ) } \cdot \underbrace { \bigg | \left( \frac { 2 i t } { i t - 1 } \right) ^ { k } \bigg | \cdot \bigg | \log \left( \frac { i t + 1 } { i t - 1 } \right) \bigg | ^ { - q } } _ { \Psi ( t ) } .
$$

We now insert, for $| t | > 1$ ,Eqs. (III.3.19),(III.3.21) and (III.3.22) to obtain

$$
\left| \Phi ( t ) \right| = \left| P _ { k } { \Big ( } { \frac { 1 } { i t } } { \Big ) } + { \frac { d _ { 1 } } { ( i t ) ^ { k + 1 } } } + { \frac { d _ { 2 } } { ( i t ) ^ { k + 2 } } } + \dots \right|
$$

where $P _ { k }$ is a polynomial of degree $k$ and subdegree $p$ (see Lemma III.3.7), determined by the method. Since we want our estimates to be true for $a l l$ methods, we treat $P _ { k }$ as an arbitrary polynomial. Separating real and imaginary parts and substituting $1 / t = s$ gives

$$
\begin{array} { c } { { | \Phi ( t ) | ^ { 2 } = \left| Q _ { k - 1 } ( s ) + d _ { 1 } s ^ { k + 1 } - d _ { 3 } s ^ { k + 3 } + \mathrm {  ~ \Gamma ~ } \right| ^ { 2 } } } \\ { { { } } } \\ { { + \left| Q _ { k } ( s ) + d _ { 2 } s ^ { k + 2 } - d _ { 4 } s ^ { k + 4 } + \mathrm {  ~ \Gamma ~ } \right| ^ { 2 } = | \Phi _ { 1 } ( t ) | ^ { 2 } + | \Phi _ { 2 } ( t ) | ^ { 2 } } } \end{array}
$$

where $Q _ { k - 1 } ( s )$ and $Q _ { k } ( s )$ are arbitrary (even or odd) polynomials of subdegree $p$ and degree $k - 1$ and $k$ ,respectively. Both terms are minorized separately, e.g. for the first we write

$$
| \Phi _ { 1 } ( t ) | \geq | Q _ { k - 1 } ( s ) + d _ { 1 } s ^ { k + 1 } | - | d _ { 3 } s ^ { k + 3 } - d _ { 5 } s ^ { k + 5 } + - \dots | .
$$

Since $\mu _ { 1 } < \mu _ { 3 } < \mu _ { 5 } < . ~ . . < 0$ (Exercise 6 below) and $a _ { \imath } \geq 0$ we have from (II1.3.22)

$$
d _ { 1 } \leq d _ { 3 } \leq d _ { 5 } \leq \ldots \leq 0 \quad { \mathrm { a n d } } \quad d _ { 2 } \leq d _ { 4 } \leq d _ { 6 } \leq \ldots \leq 0 .
$$

Therefore,the second term in (2.39) is majorized by the alternating series argument for $0 < s < 1$ as

$$
| d _ { 3 } s ^ { k + 3 } - d _ { 5 } s ^ { k + 5 } + - \ldots | \leq | d _ { 3 } | s ^ { k + 3 } \leq | d _ { 1 } | s ^ { k + 3 } .
$$

Since $Q _ { k - 1 } ( s )$ is an arbitrary polynomial, we can replace it by $| d _ { 1 } | Q _ { k - 1 } ( s )$ s0 that $\left| d _ { 1 } \right|$ becomes a common factor of the whole expression

$$
\begin{array} { r } { \left| \Phi _ { 1 } ( t ) \right| \geq \left| d _ { 1 } \right| \left( \left| Q _ { k - 1 } ( s ) + s ^ { k + 1 } \right| - s ^ { k + 3 } \right) . } \end{array}
$$

This suggests that we define the constants

$$
\begin{array} { l } { { D _ { \mathrm { I } } = \displaystyle \operatorname* { i n f } _ { Q _ { k - 1 } } \left\{ \operatorname* { s u p } _ { 0 < s < 1 } \left[ \left( \left| Q _ { k - 1 } ( s ) + s ^ { k + 1 } \right| - s ^ { k + 3 } \right) \left( \frac 2 { \sqrt { 1 + s ^ { 2 } } } \right) ^ { k } \left( \frac 1 { 2 \arctan s } \right) ^ { q } \right] \right\} } } \\ { { D _ { \mathrm { 2 } } = \displaystyle \operatorname* { i n f } _ { Q _ { k } } \left\{ \operatorname* { s u p } _ { 0 < s < 1 } \left[ \left( \left| Q _ { k } ( s ) + s ^ { k + 2 } \right| - s ^ { k + 4 } \right) \left( \frac 2 { \sqrt { 1 + s ^ { 2 } } } \right) ^ { k } \left( \frac 1 { 2 \arctan s } \right) ^ { q } \right] \right\} _ { \mathrm { - ~ c ~ o ~ c ~ t ~ a ~ n ~ } } } } \end{array}
$$

where the inf is taken over all polynomials $Q _ { k - 1 } ( s ) = c _ { k - 1 } s ^ { k - 1 } + c _ { k - 3 } s ^ { k - 3 } +$ $c _ { k - 5 } s ^ { k - 5 } + \ldots$ respectively $Q _ { k } ( s ) = c _ { k } s ^ { k } + c _ { k - 2 } s ^ { k - 2 } + c _ { k - 4 } s ^ { k - 4 } + . . .$ of subdegree $p$ . The last two factors represent $\Psi ( t )$ of (2.36). Since $s ^ { k + 1 }$ dominates $s ^ { k + 3 }$ for small $s , D _ { 1 }$ and $D _ { 2 }$ are positive constants (see Exercise 8). We then have from (2.38) and (2.36)

$$
\| \widehat { K } _ { q } \| _ { L ^ { \infty } } \geq \sqrt { d _ { 1 } ^ { 2 } D _ { 1 } ^ { 2 } + d _ { 2 } ^ { 2 } D _ { 2 } ^ { 2 } }
$$

Since both $d _ { 1 }$ and $d _ { 2 }$ are sums of $a _ { \scriptscriptstyle 3 }$ with negative coefficients (see (I.3.22) and Lemma II.3.8), $\| \widehat { K } _ { q } \| _ { \infty }$ must be large if one of the coefficient $a _ { \scriptscriptstyle \mathscr { I } }$ is large.

This concludes the proof of Theorem 2.6 which, by the way, also proves Theorem 1.4 again. □

# Exercises

1. Show that no explicit method can be $A ( 0 )$ -stable.

2. Show that $\beta _ { k } / \alpha _ { k } > 0$ is a necessary condition for an $A ( \alpha )$ -stable linear $k$ -step method.

3.a) Show that the method

$$
y _ { n + 2 } - y _ { n + 1 } = { \frac { h } { 4 } } ( f _ { n + 2 } + 2 f _ { n + 1 } + f _ { n } )
$$

has a stability domain bounded by a parabola. It is therefore $A _ { 0 }$ -stable, but not $A ( 0 )$ -stable (Cryer 1973).

b) Find a“deformation”of the 5th order BDF scheme

$$
\sum _ { \jmath = 1 } ^ { 5 } \frac { 1 } { j } \nabla ^ { \jmath } y _ { n + 1 } + \beta \nabla ^ { 6 } y _ { n + 1 } = h f _ { n + 1 }
$$

with $\beta \approx 0 . 2 3 2 \ldots$ . which is $\mathring { A }$ -stable, but not $A _ { 0 }$ -stable.

c) Find a method which is $A _ { 0 }$ -stable, but not stable at infinity.

Hint for $( c )$ . If you “lift up your heads, o ye gates” (just a few lines, not to heaven), the answer is easy to find.

4.(Parseval 1799). Prove the identity (2.24).

Hint. Insert the definitions into

$$
\| \widehat { f } \| _ { L ^ { 2 } } ^ { 2 } = \int _ { - \infty } ^ { \infty } \widehat { f } ( \xi ) \overline { { { \widehat { f } } } } ( \xi ) d \xi
$$

to get a triple integral. Two of these integrals then disappear with the Fourier inversion formula.

Remark. You may be astonished to see that Parseval's identity is older than Fourier series and Fourier transforms. Well, Parseval's identity was originally a formula between an infinite sum and an integral, which was later re-interpreted and generalized to become what it is today.

5. Substitute $\xi = \pi$ in Formula (2.23) to obtain an easy minorization for $\| \widehat { K _ { q } } \| _ { L ^ { \infty } }$ Then compute for the methods defined in the proof of Lemma 2.3 (normalized by $\sigma ( 1 ) = 1 \dot { } .$ ）the value $\sigma ( - 1 )$ for $\varepsilon$ small. This then shows that $\widehat { K _ { q } }$ becomes very large.

6. Use the formula (see the proof of Lemma III.3.8)

$$
\mu _ { 2 \jmath + 1 } = \int _ { - 1 } ^ { + 1 } x ^ { 2 \jmath } \left( \left( \log \frac { 1 + x } { 1 - x } \right) ^ { 2 } + \pi ^ { 2 } \right) ^ { - 1 } d x
$$

to show that $\mu _ { 1 } > \mu _ { 3 } > \mu _ { 5 } > . . . > 0$ ·

7. Show that for $q \simeq p$ Eq.(2.23) becomes, by substituting $i \xi = h$ and letting $h  0$ in Eq. (1.20), $\widehat { K _ { p } } ( 0 ) = C _ { p + 1 }$ ， where $C _ { p + 1 }$ is, for $\sigma ( 1 ) = 1$ , the error constant.

Formula (2.36) then provides, for $p = k$ and $t \to \infty$ ,lower bounds for the error constant (see “Theorem $4 . 5 ^ { \prime \prime }$ of Jeltsch & Nevanlinna 1982).

8.For $p = k + 1$ ， the polynomials $Q _ { k - 1 }$ and $Q _ { k }$ in (2.42） vanish identically, because the subdegree must be $p$ . Compute in this case the constants $D _ { \imath }$ and $D _ { 2 }$ . It is also easy to compute them for $p = k - 1$ . In the general case the optimal solution satisfies a sort of “Tchebysheff alternative".

Results.

Case $p = k + 1 ~ ( Q = 0 )$   

<table><tr><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=2>p=3 p=4 p=5 p=6         D2k=2 k=3k=4k=5</td><td rowspan=1 colspan=1>p=3 p=4 p=5 p=6k=2 k=3 k=4 k=5</td></tr><tr><td rowspan=2 colspan=1>q=0q=1q=2q=3q=4q=5q=6</td><td rowspan=2 colspan=2>0.47420.56950.7020 0.8813       q=00.3876 0.4435 0.52980.6505       q=10.3524 0.3659 0.41520.4933       q=20.5000 0.3381 0.34590.3891       q=30.5000 0.32510.3275       q=40.5000 0.3131       q=50.5000       q=6</td><td rowspan=2 colspan=1>0.36070.45010.57060.73190.27540.33470.41630.52630.22050.25700.310880.38520.1935 0.2075 0.2400 0.28880.1849 0.1956 0.22440.1770 0.18450.1698</td></tr><tr><td rowspan=1 colspan=1>0.5000 0.3131       q=5</td></tr></table>

Case $p = k - 1$ (one free constant in $Q$ ）：

<table><tr><td>D1</td><td>p=3 p=4 p=5 p=6 k=4 k=5 k=6 k=7</td><td></td><td>D2</td><td>p=3 p=4 p=5 p=6 k=4 k=5 k=6 k=7</td></tr><tr><td>q=0</td><td>0.0511</td><td>0.0362 0.0262 0.0193</td><td>q=0</td><td>0.0195 0.0142 0.01040.0077 0.0191 0.0138 0.0101</td></tr><tr><td></td><td>0.0727 0.0499 0.0353</td><td>0.0256</td><td>q=1 0.0269</td></tr><tr><td>q=1</td><td></td><td></td></tr><tr><td>q=2</td><td>0.1100 0.0709 0.0486 0.0344</td><td>0.0384 0.0263 0.0186 0.0135 q=2</td></tr><tr><td>0.2031 0.1070 0.0691 0.0474 q=3</td><td>q=3</td></tr><tr><td>q=4</td><td>0.0583 0.0374 0.0256 0.0181</td></tr><tr><td>q=5</td><td>q=4</td></tr><tr><td>0.1962 0.1041 0.0673 0.1894 0.1012 0.1828 q=6</td><td>0.0567 0.0365 0.0250 0.0552 0.0356</td></tr><tr><td>q=6</td><td>q=5</td></tr></table>

Case $p = k - 3$ (two free constants in $Q$ ）：

<table><tr><td>D1</td><td>p=3 p=4 p=5 p=6 k=6k=7k=8k=9</td><td></td><td>D2</td><td></td><td>p=3 p=4 p=5 p=6 k=6k=7 k=8 k=9</td><td></td></tr><tr><td>q=0</td><td></td><td>0.00300.00140.0007 0.0003</td><td></td><td>q=0</td><td>0.0007 0.00040.0002 0.0001</td><td></td></tr><tr><td>q=1</td><td></td><td>0.0066 0.0029 0.0014 0.0007</td><td>q=1</td><td></td><td>0.0015 0.0007 0.0003</td><td>0.0002</td></tr><tr><td>q=2</td><td></td><td>0.0160 0.0066 0.0029 0.0014</td><td></td><td>q=2</td><td>0.0034 0.0015 0.0007 0.0003</td><td></td></tr><tr><td>q=3</td><td>0.0457 0.0158 0.0065 0.0029</td><td></td><td></td><td>q=3</td><td>0.0082 0.0034 0.0015 0.0007</td><td></td></tr><tr><td>q=4</td><td></td><td>0.0448 0.0156 0.0064</td><td></td><td>q=4</td><td>0.0081 0.0033 0.0015</td><td></td></tr><tr><td>q=5</td><td></td><td>0.0439 0.0154</td><td></td><td>q=5</td><td></td><td>0.0080 0.0033</td></tr><tr><td>q=6</td><td></td><td></td><td>0.0431</td><td>q=6</td><td></td><td>0.0079</td></tr></table>

# V.3 Generalized Multistep Methods

The Dahlquist bound of two on the order of $A$ -stable multistep methods was the imperative to propound ... weaker stability properties，... An alternative approach for circumventing Dahlquist's bound is to modify the class of methods,rather than the property.

(T.A. Bickart & W.B.Rubin 1974)

The search for higher order $A$ -stable multistep methods is carried out in two main directions:

Use higher derivatives of the solutions; Throw in additional stages, off-step points, super-future points and the like, which leads into the large field of general linear methods.

# Second Derivative Multistep Methods of Enright

Hermite's formulas are rediscovered and republished every four years. (P.J. Davis 1963)

Differentiation of a differential equation

$$
y ^ { \prime } = f ( x , y )
$$

with respect to $x$ gives the second derivative of the solution

$$
y ^ { \prime \prime } { = } f _ { x } + f _ { y } \cdot f = : g ( x , y ) ,
$$

which we shall denote by $g$ . Now a straightforward generalization of both multistep formulas (1.1) and, say, the Taylor series method (see I.8.13)

$$
y _ { n + 1 } = y _ { n } + h f _ { n } + { \frac { h ^ { 2 } } { 2 ! } } g _ { n }
$$

can be written in the form

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { n + \ i } = \hbar \sum _ { i = 0 } ^ { k } \beta _ { \ i } f _ { n + i } + \hbar ^ { 2 } \sum _ { \ i = 0 } ^ { k } \gamma _ { i } g _ { n + i }
$$

where the $\alpha _ { \ i } , \beta _ { \ i } , \gamma _ { \ i }$ are parameters which must be chosen appropriately. Most of the theory of linear multistep methods (Sect.III.2） generalizes without difficulty. Taylor expansion similar to (II.2.5) shows that method (3.3) is of order $p$ if and only if

$$
\sum _ { i = 0 } ^ { k } \alpha _ { \ i } i ^ { q } = q \sum _ { i = 0 } ^ { k } \beta _ { \ i } i ^ { q - 1 } + q ( q - 1 ) \sum _ { i = 0 } ^ { k } \gamma _ { \ o { i } } i ^ { q - 2 }
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_18, $©$ Springer-Verlag Berlin Heidelberg 2010

for $0 \leq q \leq p$ . The first two of these formulas are identical to (I1.2.6),ie., to

$$
\varrho ( 1 ) = 0 , \qquad \varrho ^ { \prime } ( 1 ) = \sigma ( 1 ) .
$$

The error constant (seeEq. (II.2.13) and Exercise2 of Sect. I.4) is given by

$$
C = { \frac { 1 } { \sigma ( 1 ) ( p + 1 ) ! } } \left( \sum _ { i = 0 } ^ { k } \alpha _ { i } i ^ { p + 1 } - ( p + 1 ) \sum _ { \iota = 0 } ^ { k } \beta _ { i } i ^ { p } - ( p + 1 ) p \sum _ { \iota = 0 } ^ { k } \gamma _ { \iota } i ^ { p - 1 } \right) .
$$

A search for a good choice of the free parameters $\alpha _ { \imath } , \beta _ { \imath } , \gamma _ { \imath }$ was undertaken by Enright (1974) with the following ideas:

(i) Set $\alpha _ { k } = 1$ ， $\alpha _ { k - 1 } = - 1$ ， $\alpha _ { k - 2 } = . . . = \alpha _ { 0 } = 0$ to ensure reasonable stability in a neighbourhood of the origin as in the standard Adams formulas;   
(ii) Set $\gamma _ { k } \neq 0$ ， $\gamma _ { k - 1 } = . . . = \gamma _ { 0 } = 0$ to ensure stability at infinity as in the BDF formulas;   
(iii) Determine the remaining $k + 2$ coefficients $\gamma _ { k } , \beta _ { k } , \beta _ { k - 1 } , . . . , \beta _ { 0 }$ from Equations (3.4) for $q = 1 , 2 , \ldots , k + 2$ （ $q = 0$ is satisfied with (i)) to ensure a reasonably high order.

The result is a class of $k$ -step formulas of order $k + 2$ , which are of the form

$$
y _ { n + 1 } = y _ { n } + h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f _ { n + \imath - k + 1 } + h ^ { 2 } \gamma _ { k } g _ { n + 1 } .
$$

The first few of these methods are

$$
\begin{array} { r l } & { k = 1 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 2 } { 3 } \int _ { n + 1 } + \frac { 1 } { 3 } \int _ { n } \biggr ) - \frac { 1 } { 6 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 2 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 2 9 } { 4 8 } \int _ { n + 1 } + \frac { 5 } { 1 2 2 } f _ { n } - \frac { 1 } { 4 8 } f _ { n - 1 } \biggr ) - \frac { 1 } { 8 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 3 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 3 0 7 } { 5 4 0 } f _ { n + 1 } + \frac { 1 9 } { 4 0 } f _ { n } - \frac { 1 } { 2 0 } f _ { n - 1 } + \frac { 7 } { 1 0 8 0 } f _ { n - 2 } \biggr ) } \\ & { \qquad - \frac { 1 9 } { 1 8 0 } \hbar ^ { 2 } g _ { n + 1 } } \\ & { k = 4 \colon y _ { n + 1 } = y _ { n } + \hbar \biggl ( \frac { 3 1 3 3 } { 5 7 6 0 } f _ { n + 1 } + \frac { 4 7 7 } { 9 0 } f _ { n } - \frac { 4 1 } { 4 8 0 } f _ { n - 1 } + \frac { 1 } { 4 5 } f _ { n - 2 } } \\ & { \qquad \quad - \frac { 1 7 } { 5 7 6 0 } f _ { n - 3 } \biggr ) - \frac { 3 } { 3 2 5 } \hbar ^ { 2 } g _ { n + 1 } } \end{array}
$$

For a general expression, see Eq.(3.12) below and Exercise 1.

The stability analysis for second derivative methods is again done by linearizing and leads to

$$
y ^ { \prime } = \lambda y \qquad \mathrm { f o r ~ w h i c h } \qquad y ^ { \prime \prime } = \lambda ^ { 2 } y .
$$

This, inserted into (3.3), gives as the characteristic equation

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - \mu \beta _ { \imath } - \mu ^ { 2 } \gamma _ { \imath } ) \zeta ^ { \imath } = 0 , \qquad \mu = h \lambda
$$

instead of (1.6). Equation (3.9) is, for $\zeta = e ^ { \imath \theta }$ , a quadratic equation which gives rise to two root locus curves which, together, describe the stability domain. The Enright methods (3.7) turn out to be $A$ -stable for $k \approx 1$ and 2 (hence for $p = 3$ and 4) and are stiffly stable for $k \approx 3$ , 4, 5,6 and 7. The corresponding values $\alpha$ (for $A ( \alpha )$ -stability), $D$ and the error constants $C$ are given in Table 3.1. Pictures are shown in Fig.3.1.

Table 3.1. Stability characteristics and error constants for Enright methods   

<table><tr><td>k</td><td>1 2 3 4 5 6 7</td></tr><tr><td>3 P</td><td>8 9</td></tr><tr><td>4 5 6 7</td><td></td></tr><tr><td>90° 90° 87.88° 82.03° Q D 0. 0. 0.103</td><td>73.10° 59.95° 37.61° 0.526 1.339 2.728 5.182</td></tr></table>

![](images/d5d811e41c4f2d48a0c176b805bbe487d23e5731eceadf0e4fbf40cb51796ed9.jpg)  
Fig.3.1. Stability domains of Enright methods

Dense Output for Enright Methods. We have seen in Sect.II.1 that Newton's interpolation formula,basedonthedata $x _ { n + 1 } , x _ { n } , \ldots , x _ { n - k + 1 } ,$

· when integrated from $x _ { n }$ t0 $x _ { n + 1 }$ , leads to the implicit Adams methods;   
$\bullet$ when differentiated at $x _ { n + 1 }$ ,leads to the BDF methods.

It is natural to apply the same idea to Hermite interpolation (Addison 1979): guided by much previous experience (see above) we choose the data points

$$
x _ { n + 1 } ( { \mathrm { d o u b l e ~ n o d e } } ) , x _ { n } , x _ { n - 1 } , \cdot \cdot \cdot , x _ { n - k + 1 } ( { \mathrm { s i m p l e ~ n o d e s } } ) .
$$