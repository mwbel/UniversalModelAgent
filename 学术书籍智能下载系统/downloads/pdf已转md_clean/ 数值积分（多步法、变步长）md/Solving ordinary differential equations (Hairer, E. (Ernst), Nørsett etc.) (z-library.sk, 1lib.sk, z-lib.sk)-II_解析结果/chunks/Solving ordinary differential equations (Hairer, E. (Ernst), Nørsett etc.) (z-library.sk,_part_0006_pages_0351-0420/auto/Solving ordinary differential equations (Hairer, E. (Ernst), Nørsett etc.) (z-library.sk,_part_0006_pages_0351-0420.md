The use of the discrete resolvent allows elegant convergence proofs for linear multistep methods. We shall demonstrate this for the linear problem (7.26) where the matrix $A$ satisfies

$$
\| ( s I - A ) ^ { - 1 } \| \leq { \frac { M } { 1 + | s | } } \qquad { \mathrm { f o r } } \quad | \arg ( s - c ) | \leq \pi - \alpha ^ { \prime }
$$

with some $c \in \mathbb { R }$ ． This is a common assumption in the theory of holomorphic semigroups for parabolic problems (see e.g., Kato (1966) or Pazy (1983)). If all eigenvalues $\lambda _ { \iota }$ of $A$ satisfy $| \arg ( \lambda _ { \iota } - c ) - \pi | < \alpha ^ { \prime }$ then Condition (7.47) is satisfied with a constant $M$ depending on the matrix $A$ (Exercise 2). The following theorem,which was communicated to us by Ch. Lubich, is an improvement of results of Crouzeix & Raviart (1976).

Theorem 7.10. Let the multistep method be of order $p \geq 1$ ， $A ( \alpha )$ -stable and strictly stable at zero and at infinity. If the matrix $A$ of (7.26) satisfies (7.47) with $\alpha ^ { \prime } < \alpha$ , then there exist constants $C$ ， $h _ { 0 }$ ，and $\gamma \left\{ \gamma \right\}$ of the same sign as c in (7.47)), which depend only on $M , c , \alpha ^ { \prime }$ and the method, such that for $h \leq h _ { 0 }$ the global error satisfies

$$
\begin{array} { r l r } {  { \| y ( x _ { m } ) - y _ { m } \| } } \\ & { } & { \leq C \big ( e ^ { \gamma x _ { m } } \displaystyle \operatorname* { m a x } _ { 0 \leq \jmath < k } \| y ( x _ { \jmath } ) - y _ { \jmath } \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } e ^ { \gamma ( x _ { m } - \xi ) } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \big ) . } \end{array}
$$

Moreover, if $c \leq 0$ ,then $h _ { 0 }$ can be chosen arbitrarily.

Proof. The global error $e _ { m } = y ( x _ { m } ) - y _ { m }$ satisfies

$$
\sum _ { \imath = 0 } ^ { k } ( \alpha _ { \imath } - h A \beta _ { i } ) e _ { m + \imath } = d _ { m + k }
$$

where

$$
\| d _ { m + k } \| \leq C h ^ { p } \int _ { x _ { m } } ^ { x _ { m + k } } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi , \qquad m \geq 0
$$

and $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the $e _ { \mathfrak { g } }$ and $h A e _ { j }$ with $j < k$ We split these expressions into

$$
d _ { \ell } = d _ { \ell } ^ { \prime } + h A d _ { \ell } ^ { \prime \prime } \qquad { \mathrm { f o r } } \quad \ell < k ,
$$

so that $d _ { \ell } ^ { \prime }$ and $d _ { \ell } ^ { \prime \prime }$ are linear combinations of the $e _ { \mathscr { j } } ^ { \mathrm { ~ ~ } } \left( \ j < k \right)$ only. We also put $d _ { \ell } ^ { \prime } = d _ { \ell }$ and $d _ { \ell } ^ { \prime \prime } = 0$ for $\ell \geq k$ . The analysis at the' beginning of this subsection (Eq.(7.43)) then shows that

$$
e \mathopen { } \mathclose \bgroup \left( \zeta \aftergroup \egroup \right) = r \mathopen { } \mathclose \bgroup \left( \zeta , h A \aftergroup \egroup \right) d ^ { \prime } ( \zeta ) + r \mathopen { } \mathclose \bgroup \left( \zeta , h A \aftergroup \egroup \right) h A d ^ { \prime \prime } ( \zeta ) ,
$$

where as in the scalar case

$$
r ( \zeta , h A ) = ( \delta ( \zeta ) I - h A ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \sum _ { \jmath \geq 0 } r _ { \jmath } ( h A ) \zeta ^ { \jmath } .
$$

We now apply Lemma 7.11 below with $\Phi ( s ) = ( s I - A ) ^ { - 1 }$ .By assumption the estimate(7.57) holds with $\beta = 1$ so that

$$
\| r _ { \jmath } ( h A ) \| \leq C e ^ { \gamma j h } .
$$

The second term in (7.49) can be written as

$$
r ( \zeta , h A ) h A ( \delta ( \zeta ) ) ^ { - 1 } \delta ( \zeta ) d ^ { \prime \prime } ( \zeta ) = r ^ { \prime } ( \zeta , h A ) \widehat { d } ( \zeta )
$$

where

$$
\begin{array} { r l r } {  { r ^ { \prime } ( \zeta , h A ) = ( \delta ( \zeta ) I - h A ) ^ { - 1 } h A ( \delta ( \zeta ) ) ^ { - 1 } \displaystyle \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \sum _ { \jmath \geq 0 } r _ { \jmath } ^ { \prime } ( h A ) \zeta ^ { \jmath } } } \\ & { } & { \widehat { d } ( \zeta ) = \delta ( \zeta ) d ^ { \eta } ( \zeta ) = \displaystyle \sum _ { \jmath \geq 0 } \widehat { d } _ { \jmath } \zeta ^ { \jmath } . } \end{array}
$$

We apply Lemma 7.11 again, this time to

$$
\Phi ( s ) = ( s I - A ) ^ { - 1 } A s ^ { - 1 } = ( s I - A ) ^ { - 1 } - s ^ { - 1 } I .
$$

Condition (7.57) is satisfied with $\beta = 1$ so that

$$
\| r _ { \jmath } ^ { \prime } ( / { a } A ) \| \leq C ^ { \prime } e ^ { \gamma \jmath h } .
$$

The coefficients $\delta _ { \jmath }$ of $\delta ( \zeta )$ are exponentially decaying because all zeros of $\sigma ( \zeta )$ lie in $\vert \zeta \vert < 1$ . Consequently, we have

$$
\| \widehat { d } _ { \boldsymbol { \jmath } } \| \leq \kappa ^ { \boldsymbol { \jmath } } \widehat { C } \operatorname* { m a x } _ { 0 \leq \ell < k } \| e _ { \ell } \|
$$

with some $\kappa _ { \mathrm { { s } } } < 1$ . The coeficient of $\zeta ^ { m }$ in (7.49) gives

$$
e _ { m } = \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ( h A ) d _ { \jmath } ^ { \prime } + \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ^ { \prime } ( h A ) \widehat { d } _ { \jmath } .
$$

Inserting the estimates (7.48), (7.51), (7.54),and (7.55) proves the statement.

We still have to prove the estimates for $r _ { \mathrm { \lambda _ { 1 } } } ( h A )$ and $r _ { j } ^ { \prime } ( h . A )$ . For this we let $\Phi ( s )$ be some analytic (scalar-, vector-, or matrix-valued function and consider the coefficients of

$$
\Phi \big ( \delta \big ( \zeta \big ) / h \big ) \cdot \frac { \zeta ^ { - k } } { \sigma \big ( \zeta ^ { - 1 } \big ) } = h \sum _ { \jmath \geq 0 } \varphi _ { \jmath } \big ( h \big ) \zeta ^ { \jmath } .
$$

We then have the following result.

Lemma 7.11 (Lubich 1991). Assume that the multistep method is $A ( \alpha )$ -stable and strictly stable at zero and at infinity. Further suppose that $\Phi ( s )$ is analytic in a sector $| \arg ( s - c ) | < \pi - \alpha ^ { \prime }$ with ${ \mathfrak { x } } ^ { \prime } < \alpha$ ， $c \in \mathbb { R }$ and there satisfies

$$
| | \Phi ( s ) | | \leq M \cdot | s | ^ { - \beta } \qquad f o r s o m e \quad \beta > 0 .
$$

Then the coefficients $\varphi _ { \jmath } ( h )$ of (7.56) are bounded for $h \leq h _ { 0 }$ (sufficiently small) by

$$
\| \varphi _ { \ j } ( h ) \| \leq C \cdot ( j h ) ^ { \beta - 1 } e ^ { \gamma \ j h } \qquad f o r \quad j \geq 1 ,
$$

and for $j = 0$ the same bound holds as for $j = 1$ . The constants $C , \gamma$ ,and $h _ { 0 }$ depend only on $\alpha ^ { \prime } , c , M , \beta$ ， and the multistep method. Moreover, if $c < 0$ , then also $\gamma < 0$ ， and the result holds for arbitrary $h _ { 0 }$

Proof.By $A ( \alpha )$ -stability we have $\beta _ { k } / \alpha _ { k } > 0$ ,so that $\delta ( 0 ) / h$ lies in the region of analyticity of $\Phi$ for $h \leq h _ { 0 }$ . Cauchy's integral formula thus gives

$$
\Phi ( \delta ( \zeta ) / h ) = \frac { 1 } { 2 \pi i } \int _ { \Gamma } ( \delta ( \zeta ) / h - \lambda ) ^ { - 1 } \Phi ( \lambda ) d \lambda
$$

where $\Gamma$ is a suitable contour from $^ { * * } \infty \cdot e ^ { -- i ( \pi - \alpha ^ { \prime } } ) ^ { " }$ to $^ { 6 6 } \infty \cdot e ^ { \imath ( \pi - \alpha ^ { \prime } ) ^ { 3 9 } }$ within the sector of analyticity of $\Phi$ and does not meet the origin (see Fig.7.1; observe that $\Phi ( s )$ decays suficiently rapidly at infinity). Multiplying (7.59) by $\zeta ^ { - k } / \sigma ( \zeta ^ { - 1 } )$ and comparing coefficients of equal powers of $\zeta$ yields the representation

$$
\varphi _ { j } ( h ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } r _ { \jmath } ( h \lambda ) \Phi ( \lambda ) d \lambda , \qquad j \geq 0 ,
$$

which is a discrete analogue of the Laplace inversion formula. We next substitute $\omega = j h \lambda$ (for $j = 0$ we put $\omega = h \lambda$ ) so that with $\Gamma _ { j } = j \boldsymbol { h } \cdot \boldsymbol { \Gamma }$ Eq.(7.60) becomes

$$
\varphi _ { \ j } ( h ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { \ j } } r _ { \ j } \left( { \frac { \omega } { j } } \right) \Phi \Big ( { \frac { \omega } { j h } } \Big ) { \frac { d \omega } { j h } } , \qquad j \geq 1 ,
$$

and the use of (7.57) yields

$$
\Vert \varphi _ { \ j } ( h ) \Vert \leq \frac { M } { 2 \pi } ( j h ) ^ { \beta - 1 } \int _ { \Gamma _ { \ j } } \left. r _ { j } \Big ( \frac { \omega } { j } \Big ) \right. \cdot \vert \omega \vert ^ { - \beta } \cdot \vert d \omega \vert .
$$

![](images/9cbb6ebcef9b8091f7d666dda28f44cb2c558a78278945216ff59fb0fe598f3f.jpg)  
Fig. 7.1. Contour $\Gamma$ in Formula (7.59)

We still have to show that the integral in (7.62) is bounded by $C \cdot e ^ { \gamma \ j h }$ .For this we split it into two parts: the first one corresponds to those $\omega$ such that $\omega / j$ lies in a closed subset of the interior of the stability domain of the method. There we can use Lemma $7 . 9 \mathrm { b }$ so that the corresponding part of the integral in (7.62) is bounded by

$$
j \cdot \kappa ^ { \jmath } \int | \omega | ^ { - \beta - 1 } | d \omega | \leq C e ^ { \gamma \jmath h } \qquad \mathrm { f o r } \quad h \leq h _ { 0 } .
$$

For the remaining part, the argument $\omega / j = h \lambda$ of $r _ { \jmath }$ in (7.62) lies,for sufficiently small $h _ { 0 }$ ，in a neighbourhood $V$ of the origin, where the estimate of Lemma $7 . 9 \mathrm { c }$ holds. For $j h \ge 1$ we thus obtain the bound

$$
\int e ^ { \operatorname { R e } \omega + a | \omega | ^ { 2 } / \jmath } | \omega | ^ { - \beta } | d \omega | \leq C e ^ { \gamma \jmath h } ,
$$

because $\operatorname { R e } \omega = j h \operatorname { R e } \lambda$ ， $| \omega | ^ { 2 } / j \le j h \cdot C o n s t$ and $| \omega | \ge | \lambda |$ is bounded away from the origin. For small $j h$ the contour $\Gamma _ { j }$ comes arbitrarily close to the origin so that a more refined estimate is required." The idea is to replace the corresponding part of $\Gamma _ { \jmath }$ (in (7.61) and hence also in (7.62)) by an equivalent contour which is independent of $j h \in \{ h , 1 \}$ , has a positive distance to the origin and remains in the neighbourhood $V$ . The corresponding integral is thus bounded by some constant.

Remark 7.12. In Lemma 7.11 it is sufficient to require the analyticity of $\Phi ( s )$ and the estimate(7.57) in a sector $| \arg ( s - c ) | < \pi - \alpha ^ { \prime }$ ， where some compact neighbourhood of the origin is removed. We just have to take the contour $\Gamma$ in (7.59) so that it lies outside this compact neighbourhood of O. In this situation, the constant $\gamma$ may be positive also if $c < 0$

# Exercises

1. Prove the Cauchy integral formula (7.18) in the case where all eigenvalues $\lambda$ of $A$ satisfy $| \lambda | \leq 1$ and the contour of integration is the circle $| z | = \varrho$ with $\varrho > 1$

Hint. Integrate the identity

$$
z ^ { n } ( z I - A ) ^ { - 1 } = \sum _ { \jmath = 0 } ^ { \infty } A ^ { \jmath } z ^ { n - j - 1 } .
$$

2. (Kato 1960). For a non-singular $k \times k$ -matrix $B$ show that in the Euclidean norm

$$
\| B ^ { - 1 } \| \leq { \frac { \| B \| ^ { k - 1 } } { | \operatorname* { d e t } B | } } .
$$

Hint. Use the singular value decomposition of $B$ ,i.e., $B = U ^ { T } \Lambda V$ ,where $U$ and $V$ are orthogonal and $\boldsymbol { \Lambda } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { k } \right)$ with $\sigma _ { 1 } \geq \sigma _ { 2 } \geq . . . > \sigma _ { k } > 0$

3.A method $( \varrho , \sigma )$ is called $A$ -contractive in the norm $\| \cdot \| _ { G }$ (Nevanlinna & Liniger 1978-79,Dahlquist & Soderlind 1982),if

$$
\| C ( \mu ) \| _ { G } \leq 1 \qquad \mathrm { ~ f o r ~ } \quad \operatorname { R e } \mu \leq 0
$$

where $C ( \mu )$ is the companion matrix (7.13).

a) Prove that a method $\left( \varrho , \sigma \right)$ is $A$ -contractive for some positive definite matrix $G$ , if and only if it is $A$ -stable.

b) Compute the contractivity region

$$
\left\{ \mu \in \mathbb { C } \mathrm { : } \ \| C ( \mu ) \| _ { G } \leq 1 \right\}
$$

for the 2-step BDF method with $G$ given in (6.20). Observe that it is strictly smaller than the stability domain.

Result. The contractivity region is $\{ \mu \in \mathbb { C } \mathrm { : \mathrm { ~ } R e } \mu \leq 0 \}$

4. Give a direct proof for the statement of Lemma $7 . 9 \mathrm { a }$

Hint. Observe that

$$
r ( \zeta , \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \prod _ { \ i = 1 } ^ { k } \frac { 1 } { ( 1 - \zeta \cdot \zeta _ { \ i } ( \mu ) ) } ,
$$

where $\zeta _ { 1 } ( \mu ) , \ldots , \zeta _ { k } ( \mu )$ are the $k$ zeros of $\varrho ( \zeta ) - \mu \sigma ( \zeta )$ .If $\mu _ { 0 } \in \operatorname { I n t } S$ then there exists a neighbourhood $\mathcal { U }$ of $\mu _ { 0 }$ such that $| \zeta _ { \imath } ( \mu ) | \leq a < 1$ for all $i$ and $\mu \in \mathcal { U }$ ． Hence the coefficients $r _ { \jmath } ( \mu )$ are bounded. For $\mu _ { 0 } \in \partial S$ we have $\left| \zeta _ { \imath } ( \mu _ { 0 } ) \right| = 1$ for, say, $i = 1 , \ldots , \ell$ with $1 \leq \ell \leq k$ . These $\ell$ zeros are simple for all $\mu$ in a sufficiently small neighbourhood $\mathcal { U }$ of $\mu _ { 0 }$ and the other zeros satisfy $| \zeta _ { i } ( \mu ) | \leq a < 1$ for $\mu \in \mathcal { U } \cap S$ . A partial fraction decomposition

$$
r ( \zeta , \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \left( \sum _ { \iota = 1 } ^ { \ell } \frac { c _ { i } ( \mu ) } { 1 - \zeta \cdot \zeta _ { \iota } ( \mu ) ) } + s ( \zeta , \mu ) \right)
$$

shows that

$$
r _ { \jmath } ( \mu ) = \frac { 1 } { \alpha _ { k } - \mu \beta _ { k } } \biggl ( \sum _ { \imath = 1 } ^ { \ell } c _ { \imath } ( \mu ) ( \zeta _ { i } ( \mu ) ) ^ { j } + s _ { \jmath } ( \mu ) \biggr ) ,
$$

where $s _ { \jmath } \left( \mu \right)$ are the coefficients of $s ( \zeta , \mu )$ . Since the function $s ( \zeta , \mu )$ is uniformly bounded for $| \zeta | \le 1$ and $\mu \in \mathcal { U } \cap S$ , it follows from Cauchy's integral formula with integration along $| \zeta | = 1$ that $s _ { \jmath } ( \mu )$ is bounded. The statement thus follows from(7.64)and thefactthatafinitesetof thefamily $\{ \mathcal { U } \} _ { \mu _ { 0 } \in S }$ covers $S$ (Heine-Borel).

# V.8 Convergence for Nonlinear Problems

In Sect. V.6 we have seen a convergence result for one-leg methods (Theorem 6.10) applied to nonlinear problems satisfying a one-sided Lipschitz condition. An extension to linear multistep methods has been given in Theorem 6.11. A different and direct proof of this result will be the first goal of this section. Unfortunately, such a result is valid only for $A$ -stable methods (whose order cannot exceed two). The subsequent parts of this section are then devoted to convergence results for nonlinear problems,where the assumptions on the method are relaxed (e.g., $A ( \alpha )$ \~ stability), but the class of problems considered is restricted. We shall present two different theories: the multiplier technique of Nevanlinna & Odeh (1981) and Lubich's perturbation approach via the discrete variation of constants formula (Lubich 1991).

# Problems Satisfying a One-Sided Lipschitz Condition

Suppose that the differential equation $y ^ { \prime } = f ( x , y )$ satisfies

$$
{ \mathrm { R e } } \left. f ( x , y ) - f ( x , z ) , y - z \right. \leq \nu \Vert y - z \Vert ^ { 2 }
$$

for some inner product. We consider the linear multistep method

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y _ { m + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f ( x _ { m + \imath } , y _ { m + \imath } )
$$

together with its perturbed formula

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } \widehat { y } _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } f ( x _ { m + \ i } , \widehat { y } _ { m + \ i } ) + d _ { m + k } .
$$

The perturbations $d _ { m + k }$ can be interpreted as the influence of round-off, as the error due to the iterative solution of the nonlinear equation, or as the local discretization error (compare Eq.(7.5)). Taking the difference of (8.3) and (8.2) we obtain (for $m \geq 0$ ）

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } \Delta y _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \Delta f _ { m + \ i } + d _ { m + k } ,
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $\mathit { I I }$ Springer Series in Computat1onal Mathematics 14, DOI 10.1007/978-3-642-05221-7_23, $©$ Springer-Verlag Berlin Heidelberg 2010

where we have introduced the notation

$$
\Delta y _ { \jmath } = \widehat { y } _ { \jmath } - y _ { \jmath } , \qquad \Delta f _ { \jmath } = f ( x _ { \jmath } , \widehat { y } _ { \jmath } ) - f ( x _ { \jmath } , y _ { \jmath } ) .
$$

The one-sided Lipschitz condition cannot be used directly, because several $\Delta f _ { \jmath }$ appear in (8.4) (in contrast to one-leg methods). In order to express one $\Delta f _ { m }$ in terms of $\Delta y _ { \jmath }$ only we introduce the formal power series

$$
\Delta y ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta y _ { \jmath } \zeta ^ { \jmath } , \quad \Delta f ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta f _ { \jmath } \zeta ^ { j } , \quad d ( \zeta ) = \sum _ { \jmath \geq 0 } d _ { \jmath } \zeta ^ { \jmath } .
$$

It is convenient to assume that $\Delta y _ { \jmath } = 0 , \Delta f _ { \jmath } = 0 , d _ { \jmath } = 0$ for negative indices and that $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined by Eq. (8.4) with $m \in \{ - k , \ldots , - 1 \}$ . Then Eq. (8.4) just compares the coeficient of $\zeta ^ { m }$ in the identity

$$
\varrho \big ( \zeta ^ { - 1 } \big ) \Delta y ( \zeta ) = h \sigma ( \zeta ^ { - 1 } ) \Delta f ( \zeta ) + \zeta ^ { - k } d ( \zeta ) .
$$

Dividing (8.4') by $\sigma ( \zeta ^ { - 1 } )$ and comparing the coefficients of $\zeta ^ { m }$ yields

$$
\sum _ { \jmath = 0 } ^ { m } \delta _ { m - j } \Delta y _ { j } = h \Delta f _ { m } + \widetilde { d } _ { m } ,
$$

where

$$
\frac { \varrho \big ( \zeta ^ { - 1 } \big ) } { \sigma \big ( \zeta ^ { - 1 } \big ) } = \delta ( \zeta ) = \sum _ { j \geq 0 } \delta _ { j } \zeta ^ { j }
$$

as in (7.45) and

$$
\frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } d ( \zeta ) = \widetilde { d } ( \zeta ) = \sum _ { \jmath \geq 0 } \widetilde { d } _ { \jmath } \zeta ^ { \jmath } .
$$

In (8.6) $\Delta f _ { m }$ is now isolated as desired and we can take the scalar product of (8.6) with $\Delta y _ { m }$ . We then exploit the assumption (8.1) and obtain

$$
\sum _ { \jmath = 0 } ^ { m } \delta _ { m - \jmath } \mathrm { R e } \langle \Delta y _ { \jmath } , \Delta y _ { m } \rangle \leq h \nu \| \Delta y _ { m } \| ^ { 2 } + \mathrm { R e } \langle \widetilde { d } _ { m } , \Delta y _ { m } \rangle .
$$

This allows us to prove the following estimate.

Lemma 8.1. Let $\{ \Delta y _ { \jmath } \}$ and $\{ \Delta f _ { \jmath } \}$ satisfy (8.6) with $\delta _ { \jmath }$ given by (8.7). If

$$
\begin{array} { r } { \mathrm { R e } \left. \Delta f _ { m } , \Delta y _ { m } \right. \leq \nu \| \Delta y _ { m } \| ^ { 2 } , \qquad m \geq 0 , } \end{array}
$$

and the method is $A$ -stable,then there exist constants $C$ and $C _ { 0 } > 0$ such that for $m h \leq x _ { \mathrm { e n d } } - x _ { 0 }$ and $h \nu \leq C _ { 0 }$ ，

$$
\| \Delta y _ { m } \| \leq C \sum _ { \jmath = 0 } ^ { m } \| \widetilde { d } _ { \jmath } \| .
$$

Proof. We firstreformulate theleft-handsideof(8.9).For this weintroduce $\{ \Delta z _ { _ { \jmath } } \}$ by the relation

$$
\sum _ { \ i = 0 } ^ { k } \beta _ { \ i } \Delta z _ { m + \ i } = \Delta y _ { m } , \qquad m \ge 0
$$

and assume that $\Delta z _ { _ { \jmath } } = 0$ for $j < k$ .With $\begin{array} { r } { \Delta z ( \zeta ) = \sum _ { j } \Delta z _ { j } \zeta ^ { j } } \end{array}$ this means that $\sigma ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) = \Delta y \bar { ( \zeta ) }$ . Consequently we also have

$$
\begin{array} { r } { \delta ( \zeta ) \Delta y ( \zeta ) = \varrho ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) , } \end{array}
$$

which is equivalent to

$$
\sum _ { j = 0 } ^ { m } \delta _ { m - j } \Delta y _ { \jmath } = \sum _ { i = 0 } ^ { k } \alpha _ { i } \Delta z _ { m + i } .
$$

Inserting (8.11) and (8.10) into (8.9) yields

$$
\begin{array} { r l r } {  { \mathrm { R e } \Big \langle \sum _ { i = 0 } ^ { k } \alpha _ { \iota } \Delta z _ { m + i } , \sum _ { i = 0 } ^ { k } \beta _ { \iota } \Delta z _ { m + i } \Big \rangle } } \\ & { } & { \leq \displaystyle h \nu \bigg \| \sum _ { i = 0 } ^ { k } \beta _ { \iota } \Delta z _ { m + \iota } \bigg \| ^ { 2 } + \mathrm { R e } \Big \langle \widetilde { d } _ { m } , \sum _ { i = 0 } ^ { k } \beta _ { i } \Delta z _ { m + i } \Big \rangle . } \end{array}
$$

By Theorem 6.7 the method $( \varrho , \sigma )$ is $G$ -stable,so that Eq.(6.21) can be applied. As in the proof of Lemma 6.9 this yields for $\Delta Z _ { m } = ( \Delta z _ { m + k - 1 } , . . . , \Delta z _ { m } ) ^ { T }$ and $\nu \geq 0$

$$
\| \Delta Z _ { m + 1 } \| _ { G } \leq \big ( 1 + C _ { 1 } h \nu \big ) \| \Delta Z _ { m } \| _ { G } + C _ { 2 } \| \widetilde { d } _ { m } \| ,
$$

(if $\nu < 0$ replace $\nu$ by $\nu = 0$ ). But this implies

$$
\lVert \Delta Z _ { m + 1 } \rVert _ { G } \leq C _ { 3 } \Big ( \lVert \Delta Z _ { 0 } \rVert _ { G } + \sum _ { j = 0 } ^ { m } \lVert \widetilde { d } _ { j } \rVert \Big ) .
$$

By definition of $\Delta z _ { j }$ we have $\Delta Z _ { 0 } = 0$ . The statement now follows from the fact that $\begin{array} { r } { \| \Delta y _ { m } \| \leq C _ { 4 } \left( \| \Delta Z _ { m + 1 } \| _ { G } + \| \Delta Z _ { m } \| _ { G } \right) } \end{array}$ □

This lemma allows a direct proof for the convergence of $A$ -stable multistep methods which are strictly stable at infinity (compare Theorem 6.11).

Theorem 8.2. Consider an $A$ -stable multistep method of order $p$ which is strictly stable at infinity. Suppose that the differential equation satisfies (8.1). Then there exists $C _ { 0 } > 0$ such that for $h \nu \leq C _ { 0 }$

$$
\| y _ { m } - y ( x _ { m } ) \| \leq C { \big ( } \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - y ( x _ { j } ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \| { \big ) } + M h ^ { p } .
$$

The constant $C$ depends on the method and, for $\nu > 0$ ，on the length ${ x _ { m } } - { x _ { 0 } }$ of the integration interval; the constant $M$ depends in addition on bounds for the $( p + 1 )$ -th derivative of the exact solution.

Proof. We put ${ \widehat { y } } _ { m } = y ( x _ { m } )$ in (8.3). The perturbations thus become the local truncation errors $d _ { m + k } = \delta _ { L M } ( x _ { m } )$ ， where

$$
\delta _ { L M } ( x ) = \sum _ { i = 0 } ^ { k } \alpha _ { \ i } y ( x + i h ) - h \sum _ { \ i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x + i h ) .
$$

If the zeros of $\sigma ( \zeta )$ all lie in the open unit disk,the coefficients of $\zeta ^ { - k } / \sigma ( \zeta ^ { - 1 } )$ are absolutely summable and by (8.8) we have

$$
\sum _ { j = 0 } ^ { m } \| \widetilde { d } _ { j } \| \leq C _ { 1 } \sum _ { \jmath = 0 } ^ { m } \| d _ { j } \| .
$$

The statement then follows from Lemma 8.1, from $\| \delta _ { L M } ( x ) \| \le M h ^ { p + 1 }$ ，and from the fact that $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the $y _ { j } - y ( x _ { j } )$ and ${ } h \left( f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \right)$ for $j < k$ · □

# Multiplier Technique

... the best of all multipliers would be $\{ 1 , - \eta \}$ with a very small $\eta > 0$ ；. (Nevanlinna & Odeh 1981)

The above convergence proof is based on Eq.(8.6) and on the $A$ -stability of the multistep method. How can we modify this proof in order to get convergence results also for methods which are not $A$ -stable? This can be done by the so-called “multiplier technique",introduced by Nevanlinna & Odeh (1981） and based on previous ideas of Nevanlinna (1977) and Odeh & Liniger (1977).

The main idea is the following: instead of multiplying scalarly the identity (8.6) by $\Delta y _ { m }$ , we multiply it by

$$
\sum _ { \jmath = 0 } ^ { m } \mu _ { m - j } \Delta y _ { \jmath }
$$

where $\{ { \mu } _ { \jmath } \}$ are the coefficients of a rational function (the multiplier)

$$
\mu ( \zeta ) = \sum _ { j \geq 0 } \mu _ { j } \zeta ^ { j } = \frac { \eta ( \zeta ^ { - 1 } ) } { \tau ( \zeta ^ { - 1 } ) }
$$

（ $\eta$ and $\tau$ are polynomials).We obtain

$$
\begin{array} { r } { \mathrm { R e } \Big \langle \displaystyle \sum _ { j = 0 } ^ { m } \delta _ { m - , \ j } \Delta y _ { j } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle = h \mathrm { R e } \Big \langle \Delta f _ { m } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle } \\ { + \Big \langle \widetilde { d } _ { m } , \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - , \ j } \Delta y _ { j } \Big \rangle . } \end{array}
$$

Our next aim is to introduce new variables $\Delta z _ { j }$ such that the left-hand side of (8.14) becomes

$$
\Big \langle \sum _ { j = 0 } ^ { m } \delta _ { m - j } \Delta y _ { \ j } , \sum _ { \ j = 0 } ^ { m } \mu _ { m - j } \Delta y _ { j } \Big \rangle = \Big \langle \sum _ { i = 0 } ^ { \ell } \widetilde { \alpha } _ { i } \Delta z _ { m + i } , \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { i } \Delta z _ { m + i } \Big \rangle .
$$

Denoting

$$
\widetilde { \varrho } ( \zeta ) = \sum _ { i = 0 } ^ { \ell } \widetilde { \alpha } _ { i } \zeta ^ { i } , \qquad \widetilde { \sigma } ( \zeta ) = \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { \iota } \zeta ^ { i } ,
$$

the identity (8.15) certainly holds,if

$$
\begin{array} { r l } & { \varrho ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \sigma ( \zeta ^ { - 1 } ) \widetilde { \varrho } ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) } \\ & { \eta ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \tau ( \zeta ^ { - 1 } ) \widetilde { \sigma } ( \zeta ^ { - 1 } ) \Delta z ( \zeta ) . } \end{array}
$$

Dividing these two relations motivates the following definition of the new generating polynomials

$$
\begin{array} { r } { \widetilde { \varrho } ( \zeta ) = \varrho ( \zeta ) \tau ( \zeta ) / \chi ( \zeta ) , \qquad \widetilde { \sigma } ( \zeta ) = \sigma ( \zeta ) \eta ( \zeta ) / \chi ( \zeta ) . } \end{array}
$$

Here $\chi ( \zeta )$ denotes the greatest common divisor of $\varrho ( \zeta ) \tau ( \zeta )$ and $\sigma ( \zeta ) \eta ( \zeta )$ . If we define $\Delta z _ { _ { \jmath } } = 0$ for $j < 0$ and the remaining $\Delta z _ { j }$ by

$$
\chi ( \zeta ^ { - 1 } ) \Delta y ( \zeta ) = \sigma ( \zeta ^ { - 1 } ) \tau ( \zeta ^ { - 1 } ) \Delta z ( \zeta )
$$

the identity (8.15) holds for all $m$ . Suppose now that the multistep method $( \widetilde { \varrho } , \widetilde { \sigma } )$ is $A$ -stable, then the left hand side of (8.14) can be minorized by the $G$ -stability estimate (6.21) and we shall be able to derive convergence results. This motivates the following

Definition 8.3. The rational function $\mu ( \zeta )$ of (8.13) is called amultiplier for $( \varrho , \sigma )$ if $\mu ( \zeta ) \not \equiv \varrho ( \zeta ^ { - 1 } ) / \sigma ( \zeta ^ { - 1 } )$ and if the method $( \widetilde { \varrho } , \widetilde { \sigma } )$ ， given by (8.18) is $A$ -stable, i.e.,if

$$
\operatorname { R e } \left( \frac { 1 } { \mu ( \zeta ^ { - 1 } ) } \cdot \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \right) > 0 \qquad \mathrm { f o r } \quad | \zeta | > 1 .
$$

A continuation of the above analysis yields the following convergence result.

Lemma 8.4. Let $\{ \Delta y _ { j } \}$ and $\{ \Delta f _ { j } \}$ satisfy (8.6) with $\delta _ { j }$ given by (8.7). If

$$
\sum _ { m = 0 } ^ { N } \sum _ { j = 0 } ^ { m } \mu _ { m - j } \mathrm { R e } \left. \Delta f _ { m } , \Delta y _ { j } \right. \leq 0 \qquad f o r a l l \quad N \geq 0
$$

and if $\mu ( \zeta )$ is $a$ multiplier for the method, then there exists a constant $C$ such that for $m h \leq x _ { \mathrm { e n d } } - x _ { 0 }$

$$
\lVert \Delta y _ { m } \rVert \leq C \sum _ { j = 0 } ^ { m } \lVert \widetilde { d } _ { j } \rVert .
$$

Proof. Inserting (8.15) into (8.14) and using the estimate (6.21) for the $A$ -stable method $( \widetilde { \varrho } , \widetilde { \sigma } )$ yields for $\Delta Z _ { m } = ( \Delta z _ { m + \ell - 1 } , . . . , \Delta z _ { m } ) ^ { T }$

$$
\begin{array} { r } { \| \Delta Z _ { m + 1 } \| _ { G } ^ { 2 } - \| \Delta Z _ { m } \| _ { G } ^ { 2 } \leq h \mathrm { R e } \left. \Delta f _ { m } , \displaystyle \sum _ { \jmath = 0 } ^ { m } \mu _ { m - \jmath } \Delta y _ { \jmath } \right. } \\ { + \| \widetilde { d } _ { m } \| \cdot \Big \| \displaystyle \sum _ { i = 0 } ^ { \ell } \widetilde { \beta } _ { i } \Delta z _ { m + i } \Big \| . } \end{array}
$$

Summing up this inequality from $m \simeq 0$ to $m \simeq N$ gives

$$
\| \Delta \boldsymbol { Z } _ { N + 1 } \| _ { G } ^ { 2 } \leq C _ { 1 } \sum _ { m = 0 } ^ { N } \| \widetilde { d } _ { m } \| \cdot \big ( \| \Delta \boldsymbol { Z } _ { m + 1 } \| _ { G } + \| \Delta \boldsymbol { Z } _ { m } \| _ { G } \big ) ,
$$

because $\Delta Z _ { 0 } = 0$ by (8.19). This also implies

$$
\operatorname* { m a x } _ { N \leq M } \| \Delta Z _ { N + 1 } \| _ { G } ^ { 2 } \leq 2 C _ { 1 } \sum _ { m = 0 } ^ { M } \| \widetilde { d } _ { m } \| \cdot \operatorname* { m a x } _ { m \leq M } \| \Delta Z _ { m + 1 } \| _ { G } .
$$

A division by $\mathrm { m a x } _ { N \leq M } \| \Delta Z _ { N + 1 } \| _ { G }$ yields the desired estimate, because $\Delta y _ { M }$ is alinearcombinationoftheelementsof $\Delta Z _ { M + 1 }$ □

The proof of Theorem 8.2 applied to the $A$ -stable method $( \widetilde { \varrho } , \widetilde { \sigma } )$ now yields:

Theorem 8.5 (Nevanlinna & Odeh 1981). Consider $a$ linear multistep method (8.2) of order $p$ ， which is strictly stable at infinity and has a multiplier $\mu ( \zeta )$ . Suppose that the differential equation satisfies

$$
\sum _ { m = 0 } ^ { N } \sum _ { \substack { j = 0 } } ^ { m } \mu _ { m - j } \mathrm { R e } \left. f ( x _ { m } , u _ { m } ) - f ( x _ { m } , v _ { m } ) , u _ { j } - v _ { j } \right. \leq 0
$$

for all $N \geq 0$ and for all sequences $\{ u _ { j } \}$ and $\{ v _ { \jmath } \}$ . Then we have

$$
\| y _ { m } - y ( x _ { m } ) \| \leq C { \Big ( } \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - y ( x _ { j } ) \| + h \operatorname* { m a x } _ { 0 \leq j < k } \| f ( x _ { j } , y _ { j } ) - y ^ { \prime } ( x _ { j } ) \| { \Big ) } + M h ^ { p } ,
$$

In the next two subsections we shall study the existence and construction of multipliers,and try to better understand the condition (8.22).

Construction of Multipliers. Obviously $\mu ( \zeta ) = 1$ is a multiplier iff the method itself is $A$ -stable. Moreover, the limit $| \zeta |  \infty$ in (8.20) shows that $\mu ( 0 )$ must have the same sign as $\alpha _ { k } / \beta _ { k }$ (which we always assume to be positive). Therefore, the simplest (and most important) nontrivial multiplier has the form

$$
\mu ( \zeta ) = 1 - \eta \zeta .
$$

Suppose now that the method $( \varrho , \sigma )$ is stable at infinity. The maximum principle for harmonic functions then implies that (8.23) is a multiplier for $( \varrho , \sigma )$ iff $| \eta | \leq 1$ and

$$
\operatorname { R e } \left( \left( 1 - \eta e ^ { \iota t } \right) { \frac { \varrho { \big ( } e ^ { \iota t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) \geq 0 \qquad { \mathrm { f o r ~ a l l } } \quad t \in \mathbb { R } .
$$

This condition motivates the study of

$$
\gamma ( t ) = { \Bigg ( } \mathrm { R e } \left( { \frac { \varrho { \big ( } e ^ { i t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) , - \mathrm { R e } \left( e ^ { i t } { \frac { \varrho { \big ( } e ^ { i t } { \big ) } } { \sigma { \big ( } e ^ { i t } { \big ) } } } \right) { \Bigg ) } ,
$$

which is called the modified root-locus curve by Nevanlinna & Odeh (1981). We then have:

Criterion 8.6. Consider a method which is stable at infinity. The function (8.23) is a multiplier for $( \varrho , \sigma )$ iff $| \eta | \leq 1$ and the modified root-locus curve lies to the right of the straight line through the origin with slope $- 1 / \eta$

![](images/1a4bc43bcef68c3a617bbb54baddd37ec68c8f1a33cdb7c0941fb49f278aac4c.jpg)  
Fig.8.1. Modified root-locus curve for BDF schemes

Fig.8.1 shows the modified root-locus curves for the BDF schemes for $2 \le k \le$ }. The optimal values for $\eta$ are given in Table 8.1.

Table 8.1. Multiplier for BDF schemes   

<table><tr><td>k</td><td>m</td><td>A(α)-stable arccos n</td></tr><tr><td>2</td><td>0 π/2</td><td>π/2</td></tr><tr><td>3</td><td>0.0836</td><td>85.20° 86.03°</td></tr><tr><td>4</td><td>0.2878 73.27°</td><td>73.35°</td></tr><tr><td>5</td><td>0.8160</td><td>35.32° 51.84°</td></tr><tr><td>6</td><td>5.0130</td><td>17.84° 一</td></tr></table>

Proposition 8.7. If $\mu ( \zeta )$ is $a$ multiplier for $( \varrho , \sigma )$ and we have

$$
| \arg \mu ( \zeta ) | \leq { \frac { \pi } { 2 } } - \alpha \qquad f o r \quad | \zeta | \leq 1
$$

then the method is $A ( \alpha )$ -stable.

Proof. Condition (8.20) together with (8.25) implies that

$$
\bigg | \arg \bigg ( \frac { \varrho ( \zeta ) } { \sigma ( \zeta ) } \bigg ) - \pi \bigg | \geq \alpha \qquad \mathrm { f o r } \quad | \zeta | \geq 1 .
$$

But this condition implies $A ( \alpha )$ -stability.

A simple calculation shows that the multiplier(8.23) satisfies (8.25) with $\alpha =$ arccos $\eta$ . For the BDF schemes we have included these values in Table 8.1 together with the $\alpha$ -values for linear stability.

# Multipliers and Nonlinearities

We still have to investigate the problem under what conditions on the multiplier $\mu ( \zeta )$ and on the function $f ( x , y )$ one has (8.22) for all sequences $\{ u _ { \mathfrak { j } } \}$ and $\{ v _ { \jmath } \}$ To get an idea of the nature of (8.22) we first look, following Nevanlinna & Odeh (1981),at the linear problem $y ^ { \prime } = A y$

Proposition 8.8. If the multiplier $\mu ( \zeta )$ satisfies (8.25) and if the range of the matrix $A$ lies in the sector $| \arg \langle A u , u \rangle - \pi | \leq \alpha$ for all $u \in \mathbb { C } ^ { n }$ , then we have

$$
\sum _ { m = 0 } ^ { N } \sum _ { \jmath = 0 } ^ { m } \mu _ { m - j } \operatorname { R e } \left. A u _ { m } , u _ { \jmath } \right. \leq 0
$$

for all $N \geq 0$ and all sequences $\{ u _ { \mathfrak { z } } \}$

Proof. A direct computation shows that the expression in (8.26) equals

$$
\operatorname { R e } \left( \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mu ( e ^ { i t } ) \langle A \widehat { u } _ { N } ( t ) , \widehat { u } _ { N } ( t ) \rangle d t \right)
$$

where

$$
\widehat { u } _ { N } ( t ) = \sum _ { \jmath = 0 } ^ { N } e ^ { - \imath j t } u _ { j }
$$

denotes the Fourier transform of $( u _ { 0 } , u _ { 1 } , \ldots , u _ { N } )$ . The assumptions on $\mu ( \zeta )$ and on $A$ imply that the integrand in (8.27) has non-positive real part. This proves (8.26). □

Problems which satisfy (8.22) for some multiplier $\mu ( \zeta )$ must also satisfy the one-sided Lipschitz condition (8.1） with $\nu \simeq 0$ (this is seen by putting $N \approx 0$ in (8.22)).A class of nonlinear problems,for which (8.22) holds,is given by the following perturbation result.

Proposition 8.9． Let $f ( x , y ) = - A y + A g ( x , y )$ where $A$ is $a$ symmetric and positive semi-definite matrix. With $\| u \| _ { A } ^ { 2 } = u ^ { T } A u$ suppose that

$$
\| g ( x , y ) - g ( x , z ) \| _ { A } \leq L \| y - z \| _ { A } .
$$

Then Condition (8.22) holds if

$$
L \cdot \operatorname* { m a x } _ { | \zeta | = 1 } | \mu ( \zeta ) | \leq \operatorname* { m i n } _ { | \zeta | = 1 } \mathrm { R e } \mu ( \zeta ) .
$$

Remark. For the multiplier (8.23) Condition (8.29) is equivalent to $L \cdot ( 1 + \eta ) \leq ( 1 - \eta )$

Proof. As in the proof of Proposition8.8 we get for w,=uj-Uj

$$
\begin{array} { r l r } {  { - \sum _ { m = 0 } ^ { N } \sum _ { \jmath = 0 } ^ { m } \mu _ { m - \jmath } \operatorname { R e }  A w _ { m } , w _ { \jmath }  = - \operatorname { R e } ( \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mu ( e ^ { \imath t } ) \big \langle A \widehat { w } _ { N } ( t ) , \widehat { w } _ { N } ( t ) \big \rangle d t ) } } \\ & { } & { \leq - m _ { 0 } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \langle A \widehat { w } _ { N } ( t ) , \widehat { w } _ { N } ( t ) \rangle d t = - m _ { 0 } \sum _ { \jmath = 0 } ^ { N } \langle A w _ { j } , w _ { \jmath } \rangle \qquad ( 8 . 3 0 } \end{array}
$$

where $m _ { 0 } = \operatorname* { m i n } \mathrm { R e } \mu ( e ^ { \ i t } )$ . On the other hand, the inequality of Cauchy-Schwarz gives

$$
\begin{array} { r l r } {  { \sum _ { m = 0 } ^ { N } \mathrm { R e } \Big \langle A \big ( g ( x _ { m } , u _ { m } ) - g ( x _ { m } , v _ { m } ) \big ) , \sum _ { p = 0 } ^ { m } \mu _ { m - , \ j } ( u _ { \ j } - v _ { j } ) \Big \rangle } } \\ & { } & { \leq \bigg ( \displaystyle \sum _ { m = 0 } ^ { N } \| g ( x _ { m } , u _ { m } ) - g ( x _ { m } , v _ { m } ) \| _ { A } ^ { 2 } \bigg ) ^ { 1 / 2 } \cdot \bigg ( \displaystyle \sum _ { m = 0 } ^ { N } \Big \| \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - j } ( u _ { j } - v _ { j } ) \Big \| _ { A } ^ { 2 } \bigg ) ^ { 1 / 2 } . } \end{array}
$$

The last term in (8.31) can be estimated as (for the moment put $w _ { j } = 0$ for $j > N )$

$$
\begin{array} { r } { \displaystyle \sum _ { m = 0 } ^ { N } \Big \| \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - j } w _ { j } \Big \| _ { A } ^ { 2 } \leq \frac { 1 } { 2 \pi } \displaystyle \int _ { 0 } ^ { 2 \pi } \Big \| \displaystyle \sum _ { m \geq 0 } e ^ { - \imath m t } \displaystyle \sum _ { j = 0 } ^ { m } \mu _ { m - \jmath } w _ { \jmath } \Big \| _ { A } ^ { 2 } d t } \\ { = \displaystyle \frac { 1 } { 2 \pi } \displaystyle \int _ { 0 } ^ { 2 \pi } | \mu ( e ^ { - i t } ) | ^ { 2 } \cdot \Big \| \displaystyle \sum _ { j \geq 0 } e ^ { - i j t } w _ { j } \Big \| _ { A } ^ { 2 } d t \leq M ^ { 2 } \displaystyle \sum _ { j = 0 } ^ { N } \| w _ { j } \| _ { A } ^ { 2 } } \end{array}
$$

where $M = \operatorname* { m a x } \left| \mu ( e ^ { - i t } ) \right|$ . These estimates together with (8.28) show that the expression in (8.22) is majorized by

$$
( L \cdot M - m _ { 0 } ) \sum _ { j = 0 } ^ { N } \| u _ { j } - v _ { j } \| _ { A } ^ { 2 } .
$$

This is non-positive if (8.29) holds.

# Discrete Variation of Constants and Perturbations

We now turn our attention to the perturbation approach of Lubich (1991), which extends the ideas of Sect. V.7 (discrete variation of constants) to nonlinear problems. For this we consider nonlinear differential equations written in the form

$$
y ^ { \prime } = A y + g ( t , y ) .
$$

Inserting this equation into Formulas (8.2), (8.3),and (8.4) we get

$$
\sum _ { i = 0 } ^ { k } ( \alpha _ { i } I - h A \beta _ { i } ) \Delta y _ { m + i } = h \Delta g _ { m + k } + d _ { m + k } ,
$$

where

$$
\Delta g _ { m + k } = \sum _ { i = 0 } ^ { k } \beta _ { i } \Bigl ( g ( x _ { m + i } , \widehat { y } _ { m + i } ) - g ( x _ { m + \imath } , y _ { m + i } ) \Bigr )
$$

for $m \geq 0$ . We further put $\Delta g _ { \jmath } = 0$ for $j < k$ . Recall that $d _ { \jmath }$ (for $j \geq k )$ are usually the local truncation errors and $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined by (8.33) with $m \in \{ - 1 , \ldots , - k \}$ . The differences $\Delta y _ { j }$ are then the global errors of the method. If we introduce the formal power series

$$
\Delta y ( \zeta ) = \sum _ { j \geq 0 } \Delta y _ { j } \zeta ^ { j } , \quad \Delta g ( \zeta ) = \sum _ { \jmath \geq 0 } \Delta g _ { \jmath } \zeta ^ { j } , \quad d ( \zeta ) = \sum _ { j \geq 0 } d _ { \jmath } \zeta ^ { j }
$$

then the recursion (8.33) can be written as

$$
\Delta y ( \zeta ) = r ( \zeta , h A ) { \big ( } h \Delta g ( \zeta ) + d ( \zeta ) { \big ) } .
$$

The resolvent $r ( \zeta , h A )$ was introduced in (7.44) and (7.50). The coefficient of $\zeta ^ { m }$ in (8.35) then yields

$$
\Delta y _ { m } = h \sum _ { j = 0 } ^ { m } r _ { m - j } ( h A ) \Delta g _ { \jmath } + \sum _ { j = 0 } ^ { m } r _ { m - j } ( h A ) d _ { j } .
$$

The second sum on the right-hand side of (8.36) can be estimated as in Sect.V.7. In order to estimate the first term we have to combine estimates for $r _ { \jmath } ( h A )$ with a Lipschitz condition for $g ( x , y )$ . This will lead to a Gronwall-type inequality, whose resolution gives the desired estimates for $\Delta y _ { m }$ . Let us illustrate this procedure in a simple situation.

Theorem 8.10. Let the multistep method and the matrix $A$ satisfy the assumptions of Theorem 7.10. If the nonlinearity $g ( x , y )$ satisfies

$$
\| g ( x , y ) - g ( x , z ) \| \leq L \| y - z \|
$$

then there exist constants $C , \ h _ { 0 }$ and $\gamma$ as in Theorem 7.10, and A ( $h _ { 0 }$ and $\Lambda$

depend on $L$ )such that

$$
\begin{array} { r l r } {  { \| y ( x _ { m } ) - y _ { m } \| } } \\ & { } & { \quad \le C e ^ { \Lambda x _ { m } } \Big ( \operatorname* { m a x } _ { 0 \le j < k } \| y ( x _ { j } ) - y _ { j } \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { m } } e ^ { \gamma ( x _ { m } - \xi ) } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \Big ) . } \end{array}
$$

Proof. It follows from the proof of Theorem 7.10 and from (8.36) that

$$
\| \Delta y _ { m } \| \leq h L C _ { 1 } \sum _ { j = 0 } ^ { m } e ^ { \gamma ( m - j ) h } \| \Delta y _ { j } \| + C _ { 2 } \sum _ { j = 0 } ^ { m } e ^ { \gamma ( m - j ) h } \varepsilon _ { j } ,
$$

where (with $0 \leq \kappa < 1$ ）

$$
\varepsilon _ { m } = C _ { 0 } \Biggl ( \kappa _ { \quad 0 \leq j < k } ^ { m } \| \Delta y _ { j } \| + h ^ { p } \int _ { x _ { m - k } } ^ { x _ { m } } \| y ^ { ( p + 1 ) } ( \xi ) \| d \xi \Biggr ) .
$$

Application of Exercise 1 to the sequence $\left\{ e ^ { - \gamma m h } \| \Delta y _ { m } \| \right\}$ yields the statement of the theorem. □

Lubich (1991) has shown how the above estimates can be improved to obtain convergence results for singularly perturbed problems (see Sect. VI.2) and for discretized nonlinear parabolic equations,as we shall see in the sequel.

# Convergence for Nonlinear Parabolic Problems

We consider the initial value problem

$$
y ^ { \prime } + A y = g ( t , y ) , \qquad y ( 0 ) = y _ { 0 }
$$

obtained by space discretization of a parabolic differential equation. The matrix $A$ is assumed to satisfy for some $\alpha ^ { \prime } \in ( 0 , \pi / 2 )$

$$
\| ( s I + A ) ^ { - 1 } \| \leq { \frac { M } { 1 + | s | } } \qquad { \mathrm { ~ f o r ~ } } \qquad | \arg s | \leq \pi - \alpha ^ { \prime }
$$

(compare (7.47)). In order to motivate our assumptions on $g ( t , y )$ we begin with two examples.

Burgers' Equation. For this problem (Burgers 1948)

$$
u _ { t } + u u _ { x } = \mu u _ { x x } \qquad \mathrm { o r } \qquad u _ { t } + \left( \frac { u ^ { 2 } } { 2 } \right) _ { x } = \mu u _ { x x } , \qquad \mu > 0 ,
$$

we consider the discretization

$$
\dot { u } _ { i } = - \frac { u _ { \iota + 1 } ^ { 2 } - u _ { \iota - 1 } ^ { 2 } } { 4 \Delta x } + \mu \frac { u _ { i + 1 } - 2 u _ { \iota } + u _ { i - 1 } } { ( \Delta x ) ^ { 2 } } \ .
$$

It is of the form (8.39) with

$$
A = \frac { \mu } { \Delta x ^ { 2 } } \left( \begin{array} { c c c c c } { 2 } & { - 1 } & & & \\ { - 1 } & { 2 } & { - 1 } & & \\ & { - 1 } & { 2 } & { \ddots } & \\ & & & { \ddots } & { \ddots } & { - 1 } \\ & & & & { - 1 } & { 2 } \end{array} \right) , \qquad g ( t , y ) = \frac { 1 } { 4 \Delta x } \left( \begin{array} { c } { y _ { 2 } ^ { 2 } - y _ { 0 } ^ { 2 } } \\ { y _ { 3 } ^ { 2 } - y _ { 1 } ^ { 2 } } \\ { \vdots } \\ { y _ { n + 1 } ^ { 2 } - y _ { n - 1 } ^ { 2 } } \end{array} \right) ,
$$

where $\mu > 0$ is a given constant, $\Delta x = 1 / ( n + 1 )$ and, due to homogeneous boundary conditions, $y _ { 0 } = y _ { n + 1 } = 0$ . In this situation we work with the scaled norm (on $\mathbb { R } ^ { n } )$

$$
\begin{array} { r } { \| u \| = \sqrt { \Delta x \sum _ { i = 1 } ^ { n } | u _ { i } | ^ { 2 } } , } \end{array}
$$

which tends to that of $L ^ { 2 } ( 0 , 1 )$ for $n \to \infty$ . As the eigenvalues of the symmetric matrix $A$ are real and positive,condition (8.4O) is verified for every $\alpha ^ { \prime } > 0$ ， uniformly in $\Delta x$

The presence of the denominator $\Delta x$ in $g ( t , y )$ of (8.41) does not allow a Lipschitz condition (8.37) uniformly in $\Delta x > 0$ (not even in a neighbourhood of the exact solution). However, using the energy norm $\| A ^ { 1 / 2 } u \|$ ，which already contains the factor $1 / \Delta x$ , we show that

$$
| | g ( t , y ) - g ( t , z ) | | \leq \mu ^ { - 1 } r \cdot | | A ^ { 1 / 2 } ( y - z ) | | \qquad \mathrm { f o r } \quad | | A ^ { 1 / 2 } y | | + | | A ^ { 1 / 2 } z | | \leq r .
$$

For the proof of this relation we consider the bilinear map $b : \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ whose $\iota$ th component is defined by

$$
b _ { i } ( u , v ) = ( 4 \Delta x ) ^ { - 1 } ( u _ { i + 1 } + u _ { \ i - 1 } ) ( v _ { \ i + 1 } - v _ { i - 1 } )
$$

(again we put $u _ { 0 } = v _ { 0 } = u _ { n + 1 } = v _ { n + 1 } = 0 \mathrm { { ; } }$ ). Then

$$
g ( t , y ) - g ( t , z ) = b ( y , y ) - b ( z , z ) = b ( y , y - z ) + b ( y - z , z ) ,
$$

and we need an estimate for $\left| \left| b ( u , v ) \right| \right|$ . Using

$$
\begin{array} { r } { | ( u _ { i + 1 } + u _ { \iota - 1 } ) ( v _ { i + 1 } - v _ { \iota - 1 } ) | \leq 2 \cdot | v _ { \iota + 1 } - v _ { \iota - 1 } | \cdot \operatorname* { m a x } _ { j } | u _ { j } | , } \end{array}
$$

and the estimates of Exercise 3 we obtain

$$
\| b ( u , v ) \| \leq \| u \| _ { \infty } \cdot \| D v \| \leq \mu ^ { - 1 } \cdot \| A ^ { 1 / 2 } u \| \cdot \| A ^ { 1 / 2 } v \| .
$$

where

$$
D = \frac { 1 } { 2 \Delta x } \left( \begin{array} { c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 0 } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { 0 } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } & { { 0 } } \end{array} \right)
$$

represents the first central difference operator. The estimate (8.45) applied to (8.44) proves (8.43).

Incompressible Navier-Stokes Equation. The motion of a viscous incompressible fluid in a domain $\Omega \subset \mathbb { R } ^ { d }$ is governed by the equations of Navier(1823)and Stokes (1845)

$$
\frac { \partial \mathbf { u } } { \partial t } + \sum _ { \ i = 1 } ^ { d } u _ { \ i } \frac { \partial \mathbf { u } } { \partial x _ { \ i } } = \Delta \mathbf { u } - \mathbf { g r a d } p , \qquad \mathrm { d i v } \ \mathbf { u } = 0
$$

where $\mathbf { u } = ( u _ { 1 } , \ldots , u _ { d } ) ^ { T }$ . We denote by $P$ the orthogonal projection from $L ^ { 2 } ( \Omega ) ^ { d }$ onto $X$ ，where $X$ is the subspace of functions with div ${ \bf u } \simeq 0$ (more precisely: the closure of the set of smooth functions with vanishing divergence and support contained in $\Omega$ ). If we apply $P$ to Eq. (8.47), grad $p$ is eliminated and we obtain

$$
\frac { \partial \mathbf { u } } { \partial t } - P \Delta \mathbf { u } = - P \Big ( \sum _ { \ i = 1 } ^ { d } u _ { \ i } \frac { \partial \mathbf { u } } { \partial x _ { i } } \Big ) .
$$

These equations are now precisely of the form (8.39), where $A = - P \Delta$ (or some discretization of it） and $g ( t , y )$ is the right-hand side of (8.48). Lipschitz estimations for this nonlinear term have been obtained by Sobolevskii (1959) and Fujita & Kato (1964). They are of the form

$$
\| g ( t , u ) - g ( t , v ) \| _ { \beta - \gamma } \leq \ell ( r ) \cdot \| u - v \| _ { \beta } \qquad \mathrm { f o r } \quad \| u \| _ { \beta } + \| v \| _ { \beta } \leq r
$$

where $\| \cdot \| _ { \beta }$ denotes the norm

$$
\| u \| _ { \beta } = \| A ^ { \beta } u \| .
$$

In particular, for $d \approx 3$ , condition (8.49) is true for $\beta = 1 / 2 , \gamma \geq 3 / 4$ as well as for $\beta = \gamma > 3 / 4$ (Fujita & Kato 1964, pp.272-273).

Motivated by these examples we consider the initial value problem (8.39) on $\mathbb { R } ^ { n }$ ，where $A$ is supposed to satisfy (8.40) for some $\alpha ^ { \prime } \in ( 0 , \pi / 2 )$ and the nonlinearity $g ( t , y )$ is assumed to satisfy the Lipschitz condition (8.49).

Application of a linear multistep method to (8.39) yields

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { m + \ i } + h A \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } y _ { m + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } g ( t _ { m + \ i } , y _ { m + \ i } ) .
$$

Instead of comparing the numerical solution $\{ y _ { m } \}$ with the analytic solution $y ( t )$ of (8.39), it is more interesting to compare it with the exact solution of the original partial differential equation. We therefore denote by $\eta ( t )$ a projection of the solution of the PDE into the finite-dimensional space under consideration. In this way we obtain

$$
\eta ^ { \prime } + A \eta = g ( t , \eta ) + s ( t )
$$

where $s ( t )$ is the spatial discretization error.

Theorem 8.11 (Lubich 1991). Consider the problem (8.39) with $A$ and $g ( t , y )$ satisfying (8.40) and (8.49) with $\gamma < 1$ ， respectively. Assume that the multistep method is of order $p$ ， $A ( \alpha )$ -stable for some $\alpha > \alpha ^ { \prime }$ ， and strictly stable at infinity. Then,the full discretization error is bounded by

$$
\begin{array} { r l r } {  { \| y _ { m } - \eta ( t _ { m } ) \| _ { \beta } \leq C \cdot \bigg ( \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - \eta ( t _ { j } ) \| _ { \beta } + h ^ { p } \int _ { 0 } ^ { t _ { m } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t } } \\ & { } & { + \| A ^ { - 1 } s ( 0 ) \| _ { \beta } + \int _ { 0 } ^ { t _ { m } } \| A ^ { - 1 } s ^ { \prime } ( t ) \| _ { \beta } d t \bigg ) . \quad \quad ( \mathrm { ~ } } \end{array}
$$

The estimate holds for $t _ { m } = m h \leq T$ provided that $h \leq h _ { 0 }$ and the expression in brackets on the right-hand side is bounded by $\varepsilon$ ，where $h _ { 0 }$ and $\varepsilon$ are sufficiently small. The constants $C , \ h _ { 0 }$ and $\varepsilon$ depend on $\operatorname* { m a x } _ { 0 \leq t \leq T } \| \eta ( t ) \| _ { \beta }$ and $M$ of (8.40), but are otherwise independent of $A$ and the dimension of the system, and independent of m and $h$ .

Proof. a) The projected solution $\eta ( t )$ of the PDE,inserted into (8.51), gives

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } \eta ( t _ { m + i } ) = h \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } \Bigl ( - A \eta ( t _ { m + \iota } ) + g \bigl ( t _ { m + \iota } , \eta ( t _ { m + \iota } ) \bigr ) + s ( t _ { m + \iota } ) \Bigr ) + d _ { m + k }
$$

where

$$
\| d _ { m + k } \| _ { \beta } \leq C _ { 0 } h ^ { p } \int _ { t _ { m } } ^ { t _ { m + k } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t , \qquad m \geq 0 .
$$

The same analysis which was necessary for (8.36) now gives for the error $\Delta y _ { m } =$ $\eta ( t _ { m } ) - y _ { m }$ the relation

$$
\Delta y _ { m } = h \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) \Delta g _ { \jmath } + h \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) \Delta s _ { \jmath } + h \sum _ { \jmath = 0 } ^ { m } r _ { m - \jmath } ( - h A ) d _ { \jmath } .
$$

As in (8.34) the quantities $\Delta g _ { \jmath }$ and $\Delta s _ { _ { \jmath } }$ are defined by

$$
\begin{array} { l } { \displaystyle \Delta g _ { m + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Big ( g \big ( t _ { m + \imath } , \eta \big ( t _ { m + \imath } \big ) \big ) - g \big ( t _ { m + \imath } , y _ { m + \imath } \big ) \Big ) } \\ { \displaystyle \Delta s _ { m + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } s \big ( t _ { m + \imath } \big ) } \end{array}
$$

for $m \geq 0$ ,and $\Delta g _ { \jmath } = 0 , \Delta s _ { \jmath } = 0$ for $j < k$ . The values $d _ { 0 } , \ldots , d _ { k - 1 }$ are defined as usual (see their definition before (8.4')). The following three parts of the proof treat the three terms in the right-hand side of (8.54) separately.

b) The Lipschitz condition (8.49) can be written as

$$
\begin{array} { r } { \big \| \boldsymbol A ^ { - \gamma } \big ( \boldsymbol g ( t , \boldsymbol y ) - \boldsymbol g ( t , \boldsymbol z ) \big ) \big \| _ { \beta } \leq \ell ( r ) \cdot \| \boldsymbol y - \boldsymbol z \| _ { \beta } \qquad \mathrm { f o r } \qquad \| \boldsymbol y \| _ { \beta } + \| \boldsymbol z \| _ { \beta } \leq r . } \end{array}
$$

We put $\varrho = \operatorname* { m a x } _ { 0 \leq t \leq T } \| \eta ( t ) \| _ { \beta }$ and assume that for $h m \leq T$ the numerical solution $y _ { m }$ exists and is bounded by $\| y _ { m } \| \leq \varrho + 1$ (this will be verified recursively in part

(f) of the proof) so that

$$
\| A ^ { - \gamma } \Delta g _ { m + k } \| _ { \beta } \leq \ell ( 2 \varrho + 1 ) \cdot \sum _ { i = 0 } ^ { k } | \beta _ { i } | \cdot \| \Delta y _ { m + i } \| _ { \beta } .
$$

Consequently we have to find an estimate for $\| r _ { m - j } ( - h A ) A ^ { \gamma } \| _ { \beta }$ (for the matrix norm corresponding to the vector norm ${ \big \{ } \cdot { \big \} } { \big \{ } _ { \beta } \cdot$ ； see Sect.I.9). We note that $\| r _ { m - j } ( - h A ) A ^ { \gamma } \| _ { \beta } = \| A ^ { \gamma } r _ { m - j } ( - h A ) \|$ and recall that $A ^ { \gamma } r _ { j } ( - h A )$ is the coefficient of $\zeta ^ { j }$ in the series for

$$
A ^ { \gamma } r ( \zeta , - h A ) = A ^ { \gamma } \left( \delta ( \zeta ) I + h A \right) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } .
$$

In order to apply Lemma 7.11 we have to estimate $\Phi ( s ) = A ^ { \gamma } ( s I + A ) ^ { - 1 }$ .If $A$ can be transformed to diagonal form with an orthogonal matrix (as it is the case for (8.41)), we have for $| \arg s | \leq \pi - \alpha ^ { \prime }$ $( 0 < \alpha ^ { \prime } < \alpha )$

$$
\| A ^ { \gamma } ( s I + A ) ^ { - 1 } \| \leq \operatorname* { s u p } _ { a \geq 0 } { \frac { a ^ { \gamma } } { | s + a | } } \leq M _ { 1 } \cdot | s | ^ { \gamma - 1 } .
$$

For the general case we refer the reader to Henry (1981, pp. 26-28). Application of Lemma 7.11 (see also Remark 7.12) yields

$$
\| r _ { \jmath } ( - h A ) A ^ { \gamma } \| _ { \beta } \leq C _ { 1 } { \big ( } ( j + 1 ) h { \big ) } ^ { - \gamma } \qquad { \mathrm { f o r ~ } } \jmath \geq 0 .
$$

Together with the Lipschitz condition (8.55) this gives with $L = C _ { 1 } \cdot \ell ( 2 \varrho + 1 )$

$$
h \Big | \Big | \sum _ { j = 0 } ^ { m } r _ { m - j } ( - h A ) \Delta g _ { j } \Big | \Big | _ { \beta } \leq h ^ { 1 - \gamma } L \sum _ { j = 0 } ^ { m } ( m - j + 1 ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } .
$$

c) The second term in (8.54) is the coefficient of $\zeta ^ { m }$ in

$$
h r ( \zeta , - h A ) \Delta s ( \zeta ) = \widetilde { r } ( \zeta ) \widetilde { \Delta s } ( \zeta )
$$

where we have introduced

$$
\begin{array} { r l } & { \widetilde { r } ( \zeta ) = \left( \delta ( \zeta ) I + h A \right) ^ { - 1 } h A \delta ( \zeta ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } = \displaystyle \sum _ { j \geq 0 } \widetilde { r } _ { j } \zeta ^ { j } } \\ & { \widetilde { \Delta } s ( \zeta ) = \displaystyle \delta ( \zeta ) A ^ { - 1 } \Delta s ( \zeta ) = \displaystyle \sum _ { j \geq 0 } \widetilde { \Delta } s _ { j } \zeta ^ { j } . } \end{array}
$$

In order to estimate $\| \widetilde { \boldsymbol { r } } _ { j } \| _ { \beta }$ (matrix norm) we note that $\vert \vert \widetilde { r } _ { j } \vert \vert _ { \beta } = \vert \vert \widetilde { r } _ { j } \vert \vert$ .In view of an application of Lemma 7.11 we have to consider $\Phi ( s ) { \overset { } { = } } ( s I + { \bar { A } } ) ^ { - 1 } A s ^ { - 1 } =$ $s ^ { - 1 } I - ( s I + A ) ^ { - 1 }$ which, because of (8.4O), is bounded by $( M + 1 ) / \vert s \vert$ . Lemma 7.11 thus yields $\| \widetilde { r } _ { j } \| _ { \beta } \le C _ { 2 }$ . Further we have

$$
\widetilde { \Delta s } ( \zeta ) = \frac { \delta ( \zeta ) } { 1 - \zeta } \cdot \Big ( A ^ { - 1 } \Delta s _ { k } \zeta ^ { k } + \sum _ { j \geq k + 1 } A ^ { - 1 } \big ( \Delta s _ { j } - \Delta s _ { j - 1 } \big ) \zeta ^ { j } \Big )
$$

where the coefficients of $\delta ( \zeta ) / ( 1 - \zeta )$ are absolutely summable, because the zeros of $\sigma ( \zeta )$ lie all inside $| \zeta | < 1$ . Combining all these estimates we get

$$
\begin{array} { r l } {  { \Big \| \sum _ { j = 0 } r _ { m - j } ( - h A ) \Delta s _ { j } \Big \| _ { \beta } = \Big \| \sum _ { j = 0 } \widetilde { r } _ { m - j } \widetilde { \Delta s } _ { j } \Big \| _ { \beta } } } \\ & { \leq C _ { 3 } \Big ( \| A ^ { - 1 } \Delta s _ { k } \| _ { \beta } + \displaystyle \sum _ { j = k + 1 } ^ { m } \big \| A ^ { - 1 } \big ( \Delta s _ { j } - \Delta s _ { j - 1 } \big ) \big \| _ { \beta } \Big ) } \\ & { \leq C _ { 4 } \Big ( \| A ^ { - 1 } s ( 0 ) \| _ { \beta } + \int _ { 0 } ^ { t _ { m } } \| A ^ { - 1 } s ^ { \prime } ( t ) \| _ { \beta } d t \Big ) . } \end{array}
$$

d) The last term in (8.54) can be estimated in the same way as the correspond-ing term in the proof of Theorem 7.10. We just have to take the norm (8.50) and get

$$
h \Big \| \sum _ { j = 0 } ^ { m } r _ { m - \jmath } ( - h A ) d _ { j } \Big \| _ { \beta } \leq C _ { 5 } \bigg ( \operatorname* { m a x } _ { 0 \leq j < k } \| y _ { j } - \eta ( t _ { j } ) \| _ { \beta } + h ^ { p } \int _ { 0 } ^ { t _ { m } } \| \eta ^ { ( p + 1 ) } ( t ) \| _ { \beta } d t \bigg ) .
$$

e) Inserting (8.56), (8.57),and (8.58) into (8.54) gives

$$
\| \Delta y _ { m } \| _ { \beta } \leq h ^ { 1 - \gamma } L \sum _ { j = 0 } ^ { m } ( m - j + 1 ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } + C _ { 6 } \varepsilon _ { m }
$$

where $C _ { 6 } = \operatorname* { m a x } ( C _ { 4 } , C _ { 5 } )$ and $\varepsilon _ { m }$ denotes the expresson in brackets on the righthand side of (8.52). For $h \leq h _ { 0 }$ and $h _ { 0 } ^ { 1 - \gamma } L < 1$ this Gronwall-type inequality can be solved (Exercise 2) and gives $\| \Delta y _ { m } \| \le C _ { 7 } \varepsilon _ { m }$ , the desired result.

f) We now justify recurively our assumption $\| y _ { m } \| _ { \beta } \leq \varrho + 1$ used in (b). Sup-pose that $\| y _ { j } \| _ { \beta } \leq \varrho + 1$ for $j = 0 , 1 , \ldots , m - 1$ ,then it follows from $h ^ { 1 - \gamma } L < 1$ and the contraction mapping theorem that a unique solution $y _ { m }$ of (8.54) exists. This solution verifies $\| y _ { m } \| _ { \beta } \leq \| \eta ( t _ { m } ) \| _ { \beta } + \| \Delta y _ { m } \| _ { \beta } \leq \varrho + 1$ if $\varepsilon$ is small enough, more precisely, if $C _ { 7 } \varepsilon < 1$ □

Remark. A different approach to convergence results of multistep methods for nonlinear parabolic equations is given by Le Roux (198O). A corresponding theorem for Runge-Kutta methods is proved in Lubich & Ostermann (1993).

# Exercises

1. Let $L \geq 0$ and consider two sequences $\{ u _ { \ j } \}$ and $\{ \varepsilon _ { j } \}$ of nonnegative numbers which satisfy

$$
u _ { m } \leq h L \sum _ { j = 0 } ^ { m } u _ { j } + \sum _ { j = 0 } ^ { m } \varepsilon _ { j } \mathrm { f o r } m \geq 0 .
$$

Prove that for $h L \leq 1 - C ^ { - 1 }$

$$
u _ { m } \leq C e ^ { L C m h } \sum _ { j = 0 } ^ { m } \varepsilon _ { j } .
$$

Hint.Showby induction hat $\begin{array} { r } { v _ { m } \leq h \Lambda \sum _ { j = 0 } ^ { m - 1 } v _ { j } + M } \end{array}$ implies Um ≤M(1+hA)m ≤MeAmh .

2.Consider the inequality (8.59) with $\gamma < 1 , L \geq 0 , \varepsilon _ { m } \geq 0$ and $h > 0$ . Under the assumptions $h \leq h _ { 0 }$ and $h _ { 0 } ^ { 1 - \gamma } L < 1$ prove that there exists a constant $C$ such that $\| \Delta y _ { m } \| _ { \beta } \le C \varepsilon _ { m }$ for $m h \le T$

Hint. Move the term $h ^ { 1 - \gamma } L \| \Delta y _ { m } \| _ { \beta }$ to the left and divide the inequality by $\left( 1 - h ^ { 1 - \gamma } L \right)$ . This yields

$$
\| \Delta y _ { m } \| _ { \beta } \leq h ^ { 1 - \gamma } \hat { L } \sum _ { j = 0 } ^ { m - 1 } ( m - j ) ^ { - \gamma } \| \Delta y _ { j } \| _ { \beta } + \hat { \varepsilon } \quad \mathrm { f o r } \quad m \geq 0 .
$$

Show that $\| \Delta y _ { m } \| _ { \beta } \leq \widehat { \varepsilon } u ( m h )$ , where $u ( x )$ is the solution of

$$
u ( x ) = 1 + \widehat { L } \int _ { 0 } ^ { x } ( x - t ) ^ { - \gamma } u ( t ) d t .
$$

Estimate the solution of (8.60) (see Henry 1981, pp.188-190).

3. Let $A$ and $D$ be the matrices of (8.41) (suppose $\mu = 1$ ) and (8.46). Prove that for all $u \in \mathbb { R } ^ { n }$

$$
\begin{array} { r } { \| u \| _ { \infty } \leq \| A ^ { 1 / 2 } u \| , \qquad \mathsf { b } ) \quad \| D u \| \leq \| A ^ { 1 / 2 } u \| , } \end{array}
$$

where $\left\| u \right\| _ { \infty } = \operatorname* { m a x } _ { i } \left| u _ { i } \right|$ and $\| \cdot \|$ is the norm of (8.42).

H $u _ { 0 } = 0$ $\begin{array} { r } { \boldsymbol { u } _ { \iota } = \sum _ { j = 1 } ^ { i } ( \boldsymbol { u } _ { j } - \boldsymbol { u } _ { j - 1 } ) } \end{array}$

$$
\| u \| _ { \infty } ^ { 2 } \leq \sum _ { j = 1 } ^ { n } \Bigl ( \frac { u _ { j } - u _ { j - 1 } } { \Delta x } \Bigr ) ^ { 2 } = u ^ { T } A u .
$$

b） The inequality $u ^ { T } A u \geq \| D u \| ^ { 2 }$ is a consequence of the algebraic identity$( u _ { 0 } = u _ { n + 1 } = 0 )$ ）

$$
\begin{array} { c } { 4 \displaystyle \sum _ { \imath = 1 } ^ { n } ( 2 u _ { i } ^ { 2 } - u _ { \imath } u _ { i + 1 } - u _ { i } u _ { i - 1 } ) - \displaystyle \sum _ { i = 1 } ^ { n } ( u _ { i + 1 } - u _ { \imath - 1 } ) ^ { 2 } } \\ { = \displaystyle \sum _ { i = 1 } ^ { n } ( u _ { \imath + 1 } - 2 u _ { i } + u _ { \imath - 1 } ) ^ { 2 } + 2 u _ { 1 } ^ { 2 } + 2 u _ { n } ^ { 2 } . } \end{array}
$$

# V.9Algebraic Stability of General Linear Methods

General linear methods were originally introduced as a means of unifying and generalizing existing theories for traditional methods. (J.C.Butcher 1987)

In Sections IV.12 and V.6 we have studied the nonlinear stability of Runge-Kutta methods ( $B$ -stability) and of one-leg methods ( $G$ -stability). It is natural to ask whether these theories can be combined within the class of general linear methods. This work was initiated by Burrage & Butcher (1980).

We consider the differential equation ${ \boldsymbol { y } } ^ { \prime } { = } f ( { \boldsymbol { x } } , { \boldsymbol { y } } )$ where $y$ and $f$ are complexvalued vectors and we assume the one-sided Lipschitz condition

$$
\operatorname { R e } { \big \langle } f ( x , y ) - f ( x , z ) , y - z { \big \rangle } \leq \nu \| y - z \| ^ { 2 } .
$$

General linear methods are defined by (see Example 8.5 of Sect. II.8)

$$
\begin{array} { r l r } { \displaystyle } & { { } \displaystyle u _ { i } ^ { ( n + 1 ) } = \sum _ { j = 1 } ^ { k } a _ { i j } u _ { j } ^ { ( n ) } + h \sum _ { j = 1 } ^ { s } b _ { i j } f ( x _ { n } + c _ { j } h , v _ { j } ^ { ( n ) } ) , } & { i = 1 , \ldots , k } \\ { \displaystyle v _ { i } ^ { ( n ) } = \sum _ { j = 1 } ^ { k } \widetilde a _ { i j } u _ { j } ^ { ( n ) } + h \sum _ { j = 1 } ^ { s } \widetilde b _ { i j } f ( x _ { n } + c _ { j } h , v _ { j } ^ { ( n ) } ) , } & { i = 1 , \ldots , s . } \end{array}
$$

Here,un= (u（m)， $u _ { n } = ( u _ { 1 } ^ { ( n ) } , \ldots , u _ { k } ^ { ( n ) } ) ^ { T }$ cot vious step. The intermal stages $( v _ { 1 } ^ { ( n ) } , \ldots , v _ { s } ^ { ( n ) } )$ )，edyb)e computation of $u _ { n + 1 }$ in (9.2a).

# $\pmb { G }$ -Stability

As in Sect. V.6, we consider inner product norms

$$
\| u _ { n } \| _ { G } ^ { 2 } = \sum _ { i = 1 } ^ { k } \sum _ { j = 1 } ^ { k } g _ { i j } \big \langle u _ { i } ^ { ( n ) } , u _ { j } ^ { ( n ) } \big \rangle ,
$$

where $G = ( g _ { i j } )$ is a real, symmetric and positive definite matrix.

Definition 9.1. The general linear method (9.2) is called $G$ -stable, if there exists a real, symmetric and positive definite matrix $G$ , such that for two numerical solutions $\{ u _ { n } \}$ and $\{ \widehat { u } _ { n } \}$ ，

$$
\lVert u _ { n + 1 } - \widehat { u } _ { n + 1 } \rVert _ { G } \leq \lVert u _ { n } - \widehat { u } _ { n } \rVert _ { G }
$$

for all step sizes $h > 0$ and for all differential equations satisfying (9.1) with $\nu = 0$ ·

For Runge-Kutta methods (where $k \approx 1$ and apart from a scaling factor $G =$ (1)）this definition reduces to $B$ -stability as introduced in Definition IV.12.2.For one-leg methods (where $s \simeq 1$ and $\boldsymbol { u } _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T } )$ it is equivalent to Definition 6.3.

Many methods can be written in different ways as general linear methods and the above definition of $G$ -stability may depend on the particular formulation. For example, the trapezoidal rule

$$
y _ { n + 1 } = y _ { n } + { \frac { h } { 2 } } { \bigl ( } f ( x _ { n } , y _ { n } ) + f ( x _ { n + 1 } , y _ { n + 1 } ) { \bigr ) }
$$

can be considered as a Runge-Kutta method (with $u _ { n } = y _ { n }$ ). In this case it is not $G$ -stable (because it is not $B$ -stable, see Theorem IV.12.12). However, if we let $u _ { n } = ( y _ { n } , h y _ { n } ^ { \prime } )$ where $y _ { n } ^ { \prime } = f ( x _ { n } , y _ { n } )$ , then the trapezoidal rule satisfies (9.4) with

$$
G = \left( \begin{array} { c c } { { 1 } } & { { 1 / 2 } } \\ { { 1 / 2 } } & { { 1 / 4 } } \end{array} \right) .
$$

This follows from the fact that whenever $\left\{ y _ { n } \right\}$ is the solution obtained by the trapezoidal rule, then $\begin{array} { r } { z _ { n } = y _ { n } + \frac { \displaystyle h } { \displaystyle 2 } y _ { n } ^ { \prime } } \end{array}$ is a solution of the implicit midpoint rule, which is known to be $B$ -stable (see Example IV.12.3 or Theorem IV.12.9). Therefore

$$
\| y _ { n + 1 } + { \frac { h } { 2 } } y _ { n + 1 } ^ { \prime } \| \leq \| y _ { n } + { \frac { h } { 2 } } y _ { n } ^ { \prime } \|
$$

which proves the statement. The matrix $G$ in (9.5) is singular and thus not strictly positive definite. Burrage & Butcher (198O), however, admit non-zero non-negative definite matrices $G$ in their definition of $G$ -stability (which they call monotonicity). Therefore the trapezoidal rule is $G$ -stable in their definition.

# Algebraic Stability

In addition to (9.2） we consider a second numerical solution (marked with hats) produced by the same method using different starting values. We denote the differences by

$$
\begin{array} { r l r l } & { \Delta u _ { \imath } ^ { ( n ) } = u _ { \imath } ^ { ( n ) } - \widehat { u } _ { \imath } ^ { ( n ) } , } & & { \Delta u _ { n } = u _ { n } - \widehat { u } _ { n } } \\ & { \Delta v _ { \imath } ^ { ( n ) } = v _ { \imath } ^ { ( n ) } - \widehat { v } _ { \imath } ^ { ( n ) } , } & & { \Delta f _ { \imath } ^ { ( n ) } = h \big ( f ( x _ { n } + c _ { \imath } h , v _ { \imath } ^ { ( n ) } ) - f ( x _ { n } + c _ { \imath } h , \widehat { v } _ { \imath } ^ { ( n ) } ) \big ) . } \end{array}
$$

The following lemma states an identity which will be essential in the study of $G$ - stability.

Lemma 9.2 (Burrage & Butcher 1980). Let $G$ be a real, symmetric matrix and $D = \mathrm { d i a g } \left( d _ { 1 } , \dots , d _ { s } \right)$ be a real diagonal matrix. The difference of two solutions of(9.2) then satisfies

$$
\| \Delta u _ { n + 1 } \| _ { G } ^ { 2 } - \| \Delta u _ { n } \| _ { G } ^ { 2 } = 2 \sum _ { \iota = 1 } ^ { s } d _ { i } \operatorname { R e } \left. \Delta f _ { i } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \right. - \sum _ { \iota , j = 1 } ^ { s + k } m _ { i j } \langle w _ { i } , w _ { \jmath } \rangle
$$

where $( w _ { 1 } , \dots , w _ { s + k } ) = \big ( \Delta u _ { 1 } ^ { ( n ) } , \dots , \Delta u _ { k } ^ { ( n ) } , \Delta f _ { 1 } ^ { ( n ) } , \dots , \Delta f _ { s } ^ { ( n ) } \big )$ and the matrix $M = ( m _ { \imath \jmath } )$ is given by

$$
M = \left( \begin{array} { c c } { { G - A ^ { T } G A } } & { { \widetilde { A } ^ { T } D - A ^ { T } G B } } \\ { { D \widetilde { A } - B ^ { T } G A } } & { { D \widetilde { B } + \widetilde { B } ^ { T } D - B ^ { T } G B } } \end{array} \right) .
$$

Proof. We consider the identity

$$
\begin{array} { r l } & { \displaystyle \| \Delta u _ { n + 1 } \| _ { G } ^ { 2 } - \| \Delta u _ { n } \| _ { G } ^ { 2 } - 2 \sum _ { \iota = 1 } ^ { s } d _ { \iota } \mathrm { R e } \left. \Delta f _ { \iota } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \right. } \\ & { \qquad = \displaystyle \sum _ { \iota , \eta = 1 } ^ { k } g _ { \iota j } \big \langle \Delta u _ { \iota } ^ { ( n + 1 ) } , \Delta u _ { \jmath } ^ { ( n + 1 ) } \big \rangle - \sum _ { \iota , \eta = 1 } ^ { k } g _ { \iota \jmath } \big \langle \Delta u _ { \iota } ^ { ( n ) } , \Delta u _ { \jmath } ^ { ( n ) } \big \rangle } \\ & { \qquad - \displaystyle \sum _ { \iota = 1 } ^ { s } d _ { \iota } \big \langle \Delta f _ { \iota } ^ { ( n ) } , \Delta v _ { \iota } ^ { ( n ) } \big \rangle - \sum _ { \iota = 1 } ^ { s } d _ { \iota } \big \langle \Delta v _ { \iota } ^ { ( n ) } , \Delta f _ { \iota } ^ { ( n ) } \big \rangle } \end{array}
$$

and insert the formulas (9.2). This gives

$$
\ldots = \sum _ { i , j = 1 } ^ { k } g _ { i j } \Bigl \langle \sum _ { \ell = 1 } ^ { k } a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } , \sum _ { \ell = 1 } ^ { k } a _ { j \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } b _ { j \ell } \Delta f _ { \ell } ^ { ( n ) } \Bigr \rangle
$$

$$
\begin{array} { c } { { \displaystyle \phantom { \displaystyle \sum _ { i , j = 1 } ^ { k } \sum _ { \ell = 1 } ^ { \ell = 1 } } \varepsilon _ { \ell = 1 } } } \\ { { \displaystyle - \sum _ { \imath , \jmath = 1 } ^ { k } g _ { i j } \bigl \langle \Delta u _ { i } ^ { ( n ) } , \Delta u _ { j } ^ { ( n ) } \bigr \rangle - \sum _ { i = 1 } ^ { s } d _ { i } \Bigl \langle \Delta f _ { \imath } ^ { ( n ) } , \sum _ { \ell = 1 } ^ { k } \widetilde a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } \widetilde b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } \Bigr \rangle } } \\ { { \displaystyle - \sum _ { i = 1 } ^ { s } d _ { i } \Bigl \langle \sum _ { \ell = 1 } ^ { k } \widetilde a _ { i \ell } \Delta u _ { \ell } ^ { ( n ) } + h \sum _ { \ell = 1 } ^ { s } \widetilde b _ { i \ell } \Delta f _ { \ell } ^ { ( n ) } , \Delta f _ { i } ^ { ( n ) } \Bigr \rangle . } } \end{array}
$$

Multiplying out and collecting suitable terms proves the statement.

Definition 9.3. The general linear method (9.2) is called algebraically stable, if there exist a real, symmetric and positive definite matrix $G$ and a real non-negative definite diagonal matrix $D$ , such that the matrix $M$ of (9.6) is non-negative definite.

An immediate consequence of our assumption (9.1） with $\nu = 0$ and of Lem-$\mathrm { \ m a } 9 . 2$ is the following result.

Theorem 9.4. Algebraic stability implies $G$ -stability.

For a given method it may be difficult to find matrices $D$ and $G$ such that $M$ of (9.6) is non-negative definite. The following lemma shows some useful relations, which hold if the method is assumed to be preconsistent, i.e.,if there exists a vector $\xi _ { 0 } \in \mathbb { R } ^ { k }$ such that

$$
A \xi _ { 0 } = \xi _ { 0 } , \qquad \widetilde A \xi _ { 0 } = 1 1
$$

(cf. Eq. (8.25) of Sect.II.8).

Lemma 9.5. If $a$ general linear method is preconsistent and algebraically stable, then the matrices $D$ and $G$ satisfy

i） $( d _ { 1 } , \ldots , d _ { s } ) ^ { T } = D \mathbb { 1 } = B ^ { T } G \xi _ { 0 } ,$   
$i i )$ $( I - A ^ { T } ) G \xi _ { 0 } = 0$ ,i.e.， $G \xi _ { 0 }$ is $a$ left-eigenvector of $A$ corresponding to the eigenvalue $l$

Proof. i) Let $\eta \in \mathbb { R } ^ { s }$ and $\varepsilon \in \mathbb { R }$ be arbitrary. The non-negativity of $M$ ， given by (9.6), implies

$$
( \xi _ { 0 } ^ { T } , \varepsilon \eta ^ { T } ) M \left( \xi _ { 0 } \atop \varepsilon \eta \right) \geq 0
$$

so that

$$
\begin{array} { r } { \xi _ { 0 } ^ { T } ( G - A ^ { T } G A ) \xi _ { 0 } + 2 \varepsilon \eta ^ { T } ( D \widetilde { A } - B ^ { T } G A ) \xi _ { 0 } + \varepsilon ^ { 2 } \eta ^ { T } ( D \widetilde { B } + \widetilde { B } ^ { T } D - B ^ { T } G B ) \eta \ge 0 . } \end{array}
$$

Since the $\varepsilon$ -independent term vanishes (due to $A \xi _ { 0 } = \xi _ { 0 } )$ , the coefficient of $\varepsilon$ must be zero and since this holds for all $\eta$ , the result follows.

ii) A similar argument applied to

$$
( \xi _ { 0 } + \varepsilon \xi _ { 1 } ) ^ { T } ( G - A ^ { T } G A ) ( \xi _ { 0 } + \varepsilon \xi _ { 1 } ) \geq 0 \quad \mathrm { ~ f o r ~ a l l ~ } \quad \xi _ { 1 } \in \mathbb { R } ^ { k } , \ \varepsilon \in \mathbb { R }
$$

implies the second statement.

# $\mathbf { \nabla } A \mathcal { N }$ -Stability and Equivalence Results

It is interesting to study in which situation algebraic stability is also necessary for $G$ -stability. For this we consider the differential equation

$$
y ^ { \prime } = \lambda ( x ) y \qquad { \mathrm { w i t h } } \qquad { \mathrm { R e } } \lambda ( x ) \leq 0 .
$$

If we apply the general linear method (9.2) to this problem, we obtain

$$
u _ { n + 1 } = S ( Z ) u _ { n }
$$

where $Z = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right) , z _ { j } = h \lambda ( x _ { n } + c _ { j } h )$ and

$$
S ( Z ) = A + B Z ( I - \widetilde { B } Z ) ^ { - 1 } \widetilde { A } .
$$

In the sequel we assume that the abscissae $c _ { \ j }$ are related to the other coefficients of the method by (see also Remark III.8.17)

$$
\begin{array} { r } { \left( c _ { 1 } , \dots , c _ { s } \right) ^ { T } = c = \widetilde { A } \xi _ { 1 } + \widetilde { B } \mathbb { 1 } , } \end{array}
$$

where $\xi _ { 1 } \in \mathbb { R } ^ { k }$ is the second coeficient vector of the exact value function

$$
z ( x , h ) = y ( x ) \xi _ { 0 } + h y ^ { \prime } ( x ) \xi _ { 1 } + \mathcal { O } ( h ^ { 2 } ) .
$$

This means that the internal stages approximate the exact solution as $v _ { \jmath } ^ { ( n ) } = y ( x _ { n } + c _ { j } h ) + { \mathcal O } ( h ^ { 2 } ) .$

Definition 9.6. A general linear method is called $A N$ -stable,if there exists a real, symmetric and positive definite matrix $G$ such that

$$
\begin{array} { r l r l } & { \| S ( Z ) u \| _ { G } \le \| u \| _ { G } } & & { \mathrm { f o r ~ a l l ~ } Z = \mathrm { d i a g } \left( z _ { 1 } , \ldots , z _ { s } \right) \mathrm { ~ s a t i s f y i } } \\ & { } & & { ( j = 1 , \ldots , s ) \mathrm { a n d ~ } z _ { j } = z _ { k } \mathrm { ~ w h e n e v e } } \end{array}
$$

Other possible definitions of $A N$ -stability are given in Butcher (1987).For example,if the condition $\| S ( Z ) u \| _ { G } \leq \| u \| _ { G }$ is replaced by the powerboundedness of the matrix $S ( Z )$ , the method is called weakly $A N$ -stable. This definition, however, does not allow the values $z _ { \jmath } = h \lambda ( x _ { n } + c _ { j } h )$ to change at each step. Another modification is to consider arbitrary norms (instead of inner product norms only) in the definition of $A N$ -stability. Butcher (1987) has shown that this does not lead to a larger class of $A N$ -stable methods,but makes the analysis much more difficult.

We are now interested in the relations between the various stability definitions: the implications

are either trivial or follow from Theorem 9.4. We also know that $A$ -stability does not, in general, imply $A N$ -stability (see e.g.,Theorem IV.12.12). The following result shows that the other two implications are (nearly always) reversible.

Theorem 9.7 (Butcher 1987). For preconsistent and non-confluent general linear methods (i.e., methods with distinct $c _ { j }$ ) we have

Proof. It is sufficient to prove that $A N$ -stability implies algebraic stability. For this we take the matrix $G$ ，whose existence is known by the definition of $A N \mathrm { ~ - ~ }$ stability, and show that the matrices $D$ and $M$ ， given by Lemma 9.5i and (9.6), are non-negative definite.

In order to prove $d _ { \jmath } \geq 0$ we put $z _ { \jmath } = - \varepsilon \ ( \varepsilon > 0 )$ and $z _ { k } = 0$ for $k \neq j$ .We further let $\Delta u _ { n } = \xi _ { 0 }$ (eecoss) $\Delta f _ { \ell } ^ { ( n ) } = z _ { \ell } \Delta v _ { \ell } ^ { ( n ) }$ so hat $\Delta u _ { n + 1 } = S ( Z ) \xi _ { 0 }$ and $\Delta v _ { \ell } ^ { ( n ) } = 1 + \mathcal { O } ( \varepsilon )$ . Using

$$
M \binom { \xi _ { 0 } } { 0 } = 0 ,
$$

which is a consequence of Lemma 9.5, the identity of Lemma 9.2 yields

$$
\lVert S ( Z ) \xi _ { 0 } \rVert _ { G } ^ { 2 } - \lVert \xi _ { 0 } \rVert _ { G } ^ { 2 } = - 2 \varepsilon d _ { \jmath } + \mathcal { O } ( \varepsilon ^ { 2 } ) .
$$

Since the left-hand side of this equation is non-positive by $A N$ -stability, we obtain $d _ { \jmath } \geq 0$

We next put $z _ { \ell } = i \varepsilon \eta _ { \ell }$ where $\eta = ( \eta _ { 1 } , \ldots , \eta _ { s } ) ^ { T } \in \mathbb { R } ^ { s }$ is arbitrary and $\mathcal { E }$ isa small real parameter. We further put $\Delta u _ { n } = \xi _ { 0 } + \imath \varepsilon _ { k }$ with $\mu \in \mathbb { R } ^ { k }$ and $\Delta f _ { \ell } ^ { ( n ) } =$ ${ \boldsymbol { z } } _ { \ell } \Delta { \boldsymbol { v } } _ { \ell } ^ { ( n ) }$ This aganimplies $\Delta v _ { \ell } ^ { ( n ) } = 1 + \mathcal { O } ( \varepsilon )$ The identyofLema9.2t10- gether with (9.11) gives

$$
\begin{array} { c } { { \| S ( Z ) \xi _ { 0 } \| _ { G } ^ { 2 } - \| \xi _ { 0 } \| _ { G } ^ { 2 } = - \big ( \xi _ { 0 } - i \varepsilon \mu , \iota \varepsilon \eta + { \mathcal O } ( \varepsilon ^ { 2 } ) \big ) M \biggl ( \begin{array} { c } { { \xi _ { 0 } + i \varepsilon \mu } } \\ { { i \varepsilon \eta + { \mathcal O } ( \varepsilon ^ { 2 } ) } } \end{array} \biggr ) = } } \\ { { = - \varepsilon ^ { 2 } ( \mu , \eta ) ^ { T } M \biggl ( \begin{array} { c } { { \mu } } \\ { { \eta } } \end{array} \biggr ) + { \mathcal O } ( \varepsilon ^ { 3 } ) . } } \end{array}
$$

Since this relation holds for all $\mu$ and $\eta$ ， the matrix $\mathcal { M }$ has to be non-negative definite. □

Example 9.8. Let us investigate the $G$ -stability of multistep collocation methods as introduced in Sect. V.3. We consider here the case $k = 2$ and $s  2$ ,and fix one collocation point at $c _ { 2 } \simeq 1$ . The method is then given by

$$
\begin{array} { r l } & { ( \begin{array} { c } { \varepsilon _ { ( g _ { n + 1 } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \end{array} ) = \overbrace { ( \begin{array} { c c } { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } & { \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } \\ { 1 } & { 0 } \end{array} ) } ^ { \mathcal { A } } \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n } ) } } \\ { g _ { n - 1 } } \end{array} \bigg ) } ^ { \mathcal { B } }  \\ & { \qquad + \hbar \overbrace { ( \begin{array} { c c } { \varphi _ { ( 1 ) } ^ { \varepsilon } ( 1 ) } & { \varphi _ { ( 2 ) } ^ { \varepsilon } ( 1 ) } \\ { 0 } & { \varphi _ { ( 2 ) } ^ { \varepsilon } ( 1 ) } \end{array} ) } ^ { g _ { n } } \bigg ( \overbrace { f ( \varepsilon _ { ( g _ { n } ) } + \varepsilon _ { ( h , \varphi _ { ( 1 ) } ) } } ^ { \mathcal { B } } \bigg ) } \\ & { \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n } ) } } \\ { \varepsilon _ { ( g _ { n } ) } } \end{array} ) = \underbrace { ( \begin{array} { c c } { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon } } & { \varphi _ { ( 1 ) } ^ { \varepsilon } } \\ { 1 - \varphi _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } & { \varphi _ { ( 1 ) } ^ { \varepsilon } } \end{array} ) } _ { \mathcal { A } } \bigg ( \begin{array} { c } { \varepsilon _ { ( g _ { n - 1 } ) } } \\ { g _ { n - 1 } } \end{array} \bigg ) } \\ &  \qquad + \hbar \underbrace  \bigg ( \begin{array} { c c } { \Phi _ { 1 } ( \varepsilon _ { ( 1 ) } ^ { \varepsilon } } & { \psi _ { ( 1 ) } ^ { \varepsilon } ( \varepsilon _ { ( g _ { n } ) } ^ { \varepsilon } ) } \\  \Phi _ { 1 } ( \underset { \varepsilon _ { ( 1 ) } ^ { \varepsilon ( 1 ) } } { \varepsilon _ { ( g _ { n } ) } ^ { \varepsilon _ { ( 1 ) } } } &  \psi _ \end{array} \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle \varphi ( x ) = - \frac { 6 } { 5 + 9 c _ { 1 } } \left( \frac { x ^ { 3 } } { 3 } - \frac { x ^ { 2 } } { 2 } ( 1 + c _ { 1 } ) + x c _ { \mathrm { t } } \right) } \\ { \displaystyle \psi _ { \mathrm { I } } ( x ) = \frac { x ( x + 1 ) } { ( 1 - c _ { 1 } ) ( 5 + 9 c _ { 1 } ) } \left( 5 - 3 x \right) } \\ { \displaystyle \psi _ { \mathrm { 2 } } ( x ) = \frac { x ( x + 1 ) } { ( 1 - c _ { 1 } ) ( 5 + 9 c _ { 1 } ) } \left( ( 2 c _ { \mathrm { t } } + 1 ) x - c _ { \mathrm { t } } ( 3 c _ { 1 } + 2 ) \right) . } \end{array}
$$

Wc know from Exercise V.3.7 that the method is $A$ -stable if and only if $c _ { 1 } \geq$ $( \sqrt { 1 7 } - 1 ) / 8$ . For the study of its $G$ -stability we assume that after an appropriate

scaling of $G$ ， $g _ { 1 1 } = 1$ . By Lemma 9.5ii the matrix $G$ must then be of the form (recall that $\xi _ { 0 } = ( 1 , 1 ) ^ { T } .$ ）

$$
G = \left( \begin{array} { c c } { { 1 } } & { { \gamma - 1 } } \\ { { \gamma - 1 } } & { { ( \varphi ( 1 ) - 1 ) \gamma + 1 } } \end{array} \right) .
$$

A necessary condition for $G$ to be positive definite is that det $G > 0$ .For $c _ { 1 } \geq 0$ this is equivalent to

$$
0 < \gamma < \frac { 6 ( 1 + c _ { 1 } ) } { 5 + 9 c _ { 1 } } .
$$

Next we use Lemma 9.5i which implies that

$$
d _ { 1 } = \gamma \psi _ { 1 } ( 1 ) , \qquad d _ { 2 } = \gamma \psi _ { 2 } ( 1 ) .
$$

Inserting (9.13) and (9.15) into the matrix $M$ of (9.6) yields for its lower right block

$$
\left( \begin{array} { c c } { { \psi _ { 1 } ( 1 ) } } & { { 0 } } \\ { { 0 } } & { { \psi _ { 2 } ( 1 ) } } \end{array} \right) \left( \begin{array} { c c } { { 2 \gamma \chi _ { 1 } - 1 } } & { { ( \chi _ { 2 } + 1 ) \gamma - 1 } } \\ { { ( \chi _ { 2 } + 1 ) \gamma - 1 } } & { { . } } \end{array} \right) \left( \begin{array} { c c } { { \psi _ { 1 } ( 1 ) } } & { { 0 } } \\ { { 0 } } & { { \psi _ { 2 } ( 1 ) } } \end{array} \right) \nonumber
$$

where

$$
\chi _ { 1 } = \frac { \psi _ { 1 } ( c _ { 1 } ) } { \psi _ { 1 } ( 1 ) } = \frac { 1 } { 4 } c _ { 1 } ( c _ { 1 } + 1 ) ( 5 - 3 c _ { 1 } ) , \qquad \chi _ { 2 } = \frac { \psi _ { 2 } ( c _ { 1 } ) } { \psi _ { 2 } ( 1 ) } = \frac { c _ { 1 } ^ { 2 } ( c _ { 1 } + 1 ) ^ { 2 } } { 2 ( 3 c _ { 1 } ^ { 2 } - 1 ) } .
$$

A direct computation (see Exercise 2) shows that this $2 \times 2$ matrix can not be non-negative definite for $c _ { 1 } \geq ( \sqrt { 1 7 } - 1 ) / 8$ and $\gamma$ satisfying (9.14). Consequently the considered methods are never $G$ -stable.

In the next subsections we shall show how high-order algebraically stable general linear methods can be constructed.

# Multistep Runge-Kutta Methods

An interesting extension of multistep collocation methods are the so-called multi-step Runge-Kutta methods. They are defined by the formulas

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } y _ { n + 1 - \jmath } + h \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ^ { ( n ) } ) } } \\ { { \displaystyle v _ { \imath } ^ { ( n ) } = \sum _ { \jmath = 1 } ^ { k } \widetilde a _ { \imath \jmath } y _ { n + 1 - \jmath } + h \sum _ { \jmath = 1 } ^ { s } \widetilde b _ { \imath \jmath } f ( x _ { n } + c _ { \jmath } h , v _ { \jmath } ^ { ( n ) } ) . } } \end{array}
$$

They obviously form a subclass of the general linear methods (9.2). This is seen by putting $u _ { n } = ( y _ { n } , y _ { n - 1 } , \ldots , y _ { { n - k + 1 } } ) ^ { T }$ so that the exact value function is

$$
z ( x , h ) = \bigl ( y ( x ) , y ( x - h ) , \ldots , y ( x - ( k - 1 ) h ) \bigr ) ^ { T } .
$$

Further, the matrices $A$ and $B$ have the special form

$$
A = \left( \begin{array} { c c c c } { { \alpha _ { 1 } } } & { { \cdot \cdot \cdot } } & { { \cdot \cdot \cdot } } & { { \alpha _ { k } } } \\ { { 1 } } & { { } } & { { } } & { { 0 } } \\ { { } } & { { \cdot \cdot } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { 1 } } & { { 0 } } \end{array} \right) , \qquad B = \left( \begin{array} { c c c } { { b _ { 1 } } } & { { \cdot \cdot \cdot } } & { { b _ { s } } } \\ { { 0 } } & { { \cdot \cdot } } & { { 0 } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { 0 } } & { { \ldots } } & { { 0 } } \end{array} \right) .
$$

The order conditions for such methods were derived in Theorem III.8.14. It follows from this theorem that the method (9.17) is of order $p$ ,iff

$$
1 = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } { \left( 1 - j \right) } ^ { \varrho { \left( t \right) } } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } { \mathbf { v } _ { \jmath } ^ { \prime } } { \left( t \right) } \quad { \mathrm { ~ f o r ~ } } \quad t \in T , \varrho { \left( t \right) } \leq p .
$$

The values $\mathbf { v } _ { \ j } ^ { \prime } ( t )$ are given recursively by

$$
\mathbf { v } _ { \ i } ( t ) = \sum _ { \jmath = 1 } ^ { k } \widetilde { a } _ { \imath \jmath } ( 1 - \jmath ) ^ { \varrho ( t ) } + \sum _ { \jmath = 1 } ^ { s } \widetilde { b } _ { \imath \jmath } \mathbf { v } _ { \jmath } ^ { \prime } ( t ) .
$$

Recall from Corollary II.12.7 that

$$
\begin{array} { r l r } & { \mathbf v _ { \ j } ^ { \prime } ( \emptyset ) = 0 , \qquad \mathbf v _ { \ j } ^ { \prime } ( \tau ) = 1 } \\ & { \mathbf v _ { \ j } ^ { \prime } ( t ) = \varrho ( t ) \mathbf v _ { \ j } ( t _ { 1 } ) \cdot \dots \cdot \mathbf v _ { \ j } ( t _ { m } ) } & { \mathrm { ~ i f ~ } \quad t = [ t _ { 1 } , \dots , t _ { m } ] . } \end{array}
$$

The order conditions (9.19) constitute a system of nonlinear equations in the coefficients of the method. Without any preparation, solving them may be difficult. We therefore introduce additional assumptions which simplify the construction of multistep Runge-Kutta methods.

# Simplifying Assumptions

The conditions $B ( p ) , C ( \eta )$ and $D ( \xi )$ of Sect.IV.5 were useful for the construction of high-order implicit Runge-Kutta methods. Burrage （1988） showed how these simplifying assumptions can be extended to general linear methods. In the sequel we specialize his approach to multistep Runge-Kutta methods. We consider the assumptions

$$
\begin{array} { l l l l l } { { } } & { { } } & { { \displaystyle { B ( p ) : \frac { q \overset { A } { \sum } b _ { j } c _ { j } ^ { q - 1 } + \sum _ { j = 1 } ^ { k } \alpha _ { j } ( 1 - j ) ^ { q } = 1 } } } } & { { \quad \mathrm { ~ } } } & { { \mathrm { ~ } q = 1 , \ldots , p ; } } \\ { { } } & { { } } & { { \displaystyle { C ( \eta ) : \frac { s } { \eta = 1 } \widetilde b _ { j } c _ { j } ^ { q - 1 } + \sum _ { j = 1 } ^ { k } \widetilde a _ { j } ( 1 - j ) ^ { q } = c _ { i } ^ { q } } } } & { { \quad \mathrm { ~ } q = 1 , \ldots , \eta , \mathrm { ~ a l l ~ i ; } } } \\ { { } } & { { } } &   \displaystyle { \begin{array} { l } { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { { ~ } } \mathcal { ~ } \mathcal { ~ } { ~ } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle { \mathcal { ~ } { D } _ { \mathrm { { a } } } ( \xi ) : \frac { s } { \mathcal { } } \sum _ { j = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } \widetilde a _ { i j } = \alpha _ { j } \left( 1 - ( 1 - j ) ^ { q } \right) } } } & { { \quad \mathrm { ~ } } } & { { \mathrm { ~ } q = 1 , \ldots , \xi , \mathrm { ~ a l l ~ } j ; } } \\ { { } } & { { } } &   \displaystyle  \begin{array} { l } { { \mathrm { ~ } } } \\  { \mathrm { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal { { ~ } } \mathcal    \end{array} \end{array} \end{array}
$$

Condition $B ( p )$ is equivalent to the order conditions (9.19) for bushy trees.Condition $C ( \eta )$ means that $\mathbf { v } _ { \jmath } ( t )$ ,defined by (9.20),satisfies

$$
\mathbf { v } _ { \boldsymbol { \jmath } } ( t ) = c _ { \boldsymbol { j } } ^ { \varrho ( t ) } \quad \mathrm { ~ f o r ~ } \quad \varrho ( t ) \leq \boldsymbol { \eta } .
$$

We remark that the preconsistency condition (9.7) with $\xi _ { 0 } = ( 1 , \ldots , 1 ) ^ { T }$ ，

$$
\sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } = 1 , \qquad \sum _ { \jmath = 1 } ^ { k } { \widetilde a } _ { \imath \jmath } = 1 \quad \mathrm { f o r } \quad i = 1 , \dots , s ,
$$

is obtained by putting $q = 0$ in $B ( p )$ and $C ( \eta )$ . The condition $D ( \xi )$ for Runge-Kutta methods splits into $D _ { A } ( \boldsymbol { \xi } )$ and $D _ { B } ( \boldsymbol { \xi } )$ . However, under certain assumptions one of these conditions is automatically satisfied.

Lemma 9.9. Suppose that the coefficients $c _ { 1 } , \ldots , c _ { s }$ of a multistep Runge-Kutta method are distinct and $\boldsymbol { b } _ { \imath } \neq 0$ . Then,

$$
\begin{array} { r l } & { B ( \xi + k - 1 ) , C ( k - 1 ) , D _ { B } ( \xi ) \Longrightarrow D _ { A } ( \xi ) , } \\ & { B ( \xi + s ) , C ( s ) , D _ { A } ( \xi ) \Longrightarrow D _ { B } ( \xi ) , } \\ & { B ( \eta + s ) , D _ { A } ( s ) , D _ { B } ( s ) \Longrightarrow C ( \eta ) . } \end{array}
$$

Proof. The first two implications are aconsequence of the identity

$$
\begin{array} { c } { { \displaystyle \sum _ { \jmath = 1 } ^ { k } \biggl ( q \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \widetilde a _ { \imath \jmath } - \alpha _ { \jmath } \bigl ( 1 - ( 1 - j ) ^ { q } \bigr ) \biggr ) ( 1 - j ) ^ { \ell } } } \\ { { = - \ell \displaystyle \sum _ { \jmath = 1 } ^ { s } \biggl ( q \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \widetilde b _ { \imath \jmath } - b _ { \jmath } \bigl ( 1 - c _ { \jmath } ^ { q } \bigr ) \biggr ) c _ { \jmath } ^ { \ell - 1 } } } \end{array}
$$

which holds under the assumptions $C ( \ell )$ and $B ( q + \ell )$ . The last implication can be proved similarly. □

The fundamental theorem, which generalizes Theorem IV.5.1, is

Theorem 9.10 (Burrage 1988). If the coefficients of $a$ multistep Runge-Kutta method (9.17) satisfy the simplifying assumptions $B ( p )$ ， $C ( \eta )$ ， $D _ { A } ( \boldsymbol { \xi } )$ ， $D _ { B } ( \boldsymbol { \xi } )$ with $p \leq \eta + \xi + 1$ and $p \leq 2 \eta + 2$ ,then the method is of order $p$

Proof. The conditions $C ( \eta )$ and $D _ { A } ( \xi ) , D _ { B } ( \xi )$ allow the reduction of order conditions of trees as sketched in Fig.7.1 and Fig.7.2 of Sect.I.7,respectively. Under the restrictions $p \leq \eta + \xi + 1$ and $p \leq 2 \eta + 2$ all order conditions reduce to those for bushy trees which are satisfied by $B ( p )$ □

Remember that we are searching for high-order algebraically stable methods. Due to the Daniel-Moore conjecture (Theorem V.4.4) the order is restricted by $p \leq 2 s$ . It is therefore natural to look for methods satisfying $B ( 2 s )$ ， $C ( s )$ and

$D _ { A } ( s ) , D _ { B } ( s )$ . They will be of order $2 . 5$ by Theorem 9.10 and are an extension of the Runge-Kuta methods based on Gauss quadrature. Let us begin by studying the condition $B ( 2 s )$

# Quadrature Formulas

Because of (9.23) condition $B ( p )$ of the preceding subsection is equivalent to

$$
\sum _ { j = 1 } ^ { s } b _ { \ u _ { j } } f ( c _ { \ u _ { j } } ) = \sum _ { j = 1 } ^ { k } \alpha _ { \ u _ { j } } \int _ { 1 - j } ^ { 1 } f ( x ) d x , \qquad \deg f \le p - 1 ,
$$

where $f$ stands for a polynomial of degree at most $p - 1$ . For the construction of such quadrature formulas it is useful to consider the bilinear form

$$
\langle f , g \rangle = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } f ( x ) g ( x ) d x = \int _ { 1 - k } ^ { 1 } \omega ( x ) f ( x ) g ( x ) d x ,
$$

where $\omega ( x )$ is the step-function sketched in Fig.9.1. Under the assumption

$$
\alpha _ { k } \geq 0 , \quad \alpha _ { k } + \alpha _ { k - 1 } \geq 0 , \ldots , \quad \alpha _ { k } + \ldots + \alpha _ { 2 } \geq 0 , \quad \alpha _ { k } + \ldots + \alpha _ { 1 } = 1 ,
$$

$\omega ( x )$ is non-negative and (9.25) becomes an inner product on the space of real polynomials. We call the quadrature formula (9.24) interpolatory if $B ( s )$ holds. This implies that

$$
b _ { \imath } = \int _ { 1 - k } ^ { 1 } \omega ( x ) \ell _ { i } ( x ) d x . \qquad \ell _ { \imath } ( x ) = \prod _ { \imath = 1 } ^ { s } \frac { ( x - c _ { \imath } ) } { ( c _ { \imath } - c _ { \imath } ) } .
$$

![](images/95bb9af32ca7f9a90f861f13d645fbd650a2e406a493de09a933000aaa87e583.jpg)  
Fig.9.1. Weight function for the inner product (9.25)

The following results on Gaussian quadrature and orthogonal polynomials are classical.

Lemma 9.11. Let $M ( x ) = ( x - c _ { 1 } ) \cdot . . . \cdot ( x - c _ { s } )$ . An interpolatory quadrature formula satisfies $B ( s + m )$ if and only if

$$
\sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } M ( x ) x ^ { q - 1 } d x = 0 \quad f o r \quad q = 1 , \ldots , m .
$$

Let $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ be the polynomial of degree s which is orthogonal with respect to (9.25) to all polynomials of degree $s \sim 1$ . Lemma 9.11 then states that a quadrature formula (9.24) is of order 2s iff $M ( x )$ is a scalar multiple of $p _ { s } ( x )$ .The polynomials $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ which depend on $\alpha _ { 1 } , \ldots , \alpha _ { k }$ via the bilinear form (9.25) can be computed from a standard three term recursion

$$
p _ { 0 } ( x ) = 1 , \qquad p _ { 1 } ( x ) = x - \beta _ { 0 }
$$

$$
p _ { s + 1 } ( x ) = ( x - \beta _ { s } ) p _ { s } ( x ) - \gamma _ { s } p _ { s - 1 } ( x )
$$

where

$$
\beta _ { s } = \frac { \langle x p _ { s } , p _ { s } \rangle } { \langle p _ { s } , p _ { s } \rangle } , \qquad \gamma _ { s } = \frac { \langle p _ { s } , p _ { s } \rangle } { \langle p _ { s - 1 } , p _ { s - 1 } \rangle } .
$$

Obviously this is only possible if $\langle p _ { \jmath } , p _ { \jmath } \rangle \neq 0$ for $j = 1 , \dots , s$ . This is certainly the case under the assumption (9.26).

Lemma 9.12. If $\alpha _ { 1 } , \ldots , \alpha _ { k }$ satisfy (9.26) then all zeros of $p _ { s } ( x )$ are real, simple and lie in the open interval $( 1 - k , 1 )$ □

For the construction of algebraically stable methods, quadrature formulas with positive weights willbe of particular interest. Suficient conditions for this property are given in the following theorem.

Theorem 9.13. If the quadrature formula (9.24) is of order $p \geq 2 s - 1$ and if $\alpha _ { 1 } , \ldots , \alpha _ { k }$ satisfy (9.26), then

$$
b _ { \imath } > 0 \qquad f o r \qquad i = 1 , \ldots , s .
$$

# Algebraically Stable Methods of Order $\pmb { 2 s }$

... the analysis of the algebraic stability properties of multivalue methods... is not as dificult as was generally thought ...

(Burrage 1987)

Following Burrage (1987） we consider the following class of multistep Runge-Kutta methods.

Definition 9.14. Let $\alpha _ { 1 } , \ldots , \alpha _ { k }$ with $\sum \alpha _ { \ j } = 1$ and $\alpha _ { k } \neq 0$ be given such that the zeros $c _ { 1 } , \ldots , c _ { s }$ of $\boldsymbol { p } _ { s } ( \boldsymbol { x } )$ (Formula(9.28))are real and simple. We then denote

by $E ( \alpha _ { 1 } , \dots , \alpha _ { k } )$ the multistep Runge-Kutta method (9.17) whose coeficients are given by

$$
\begin{array} { r l } & { \displaystyle b _ { \imath } = \sum _ { j = 1 } ^ { k } \alpha _ { \jmath } \int _ { 1 - \jmath } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s , } \\ & { \displaystyle \widetilde a _ { \imath \jmath } = \frac { \alpha _ { \jmath } } { b _ { \jmath } } \int _ { 1 - \jmath } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s ; \ \jmath = 1 , \ldots { / k } } \\ & { \displaystyle \widetilde b _ { \imath } = \frac { b _ { \jmath } } { b _ { \jmath } } \int _ { c _ { \jmath } } ^ { 1 } \ell _ { \imath } ( x ) d x , \qquad \imath = 1 , \ldots , s ; \ j = 1 , \ldots s } \end{array}
$$

where $\boldsymbol { \ell } _ { \boldsymbol { \imath } } ( \boldsymbol { x } )$ is the function of (9.27).

The definitions of $c _ { \iota }$ and $b _ { \imath }$ imply $B ( 2 s )$ by Lemma 9.11. The formulas for a and $\widetilde { \boldsymbol { b } } _ { \iota \boldsymbol { j } }$ are equivalent to $D _ { A } ( s )$ and $D _ { B } ( s )$ , respectively. Lcmma 9.9ii thus implies $\check { C } ( s )$ and Theorem 9.1O finally proves that the considered methods are of order $2 \mathit { s }$ . The following theorem gives sufficient conditions for the algebraic stability of these methods.

Theorem 9.15 (Burrage 1987).If $\alpha _ { _ { \mathscr { I } } } \geq 0$ for $j = 1 , \dots , k ^ { \prime }$ ， then the method $E ( \alpha _ { 1 } , \dots , \alpha _ { k } )$ is $G$ -stable with

$$
G = \mathrm { d i a g } ( 1 , \alpha _ { 2 } + \ldots + \alpha _ { k } , \ldots , \alpha _ { k - 1 } + \alpha _ { k } , \alpha _ { k } ) .
$$

Proof. For multistep Runge-Kutta methods the preconsistency vector is given by $\xi _ { 0 } = ( 1 , 1 , \dots , 1 ) ^ { T }$ . With the matrix $G$ of (9.30) it therefore follows from Lemma 9.5 that

$$
d _ { \ i } = b _ { \ i } \qquad \mathrm { f o r } \qquad i = 1 , \ldots , s .
$$

By Theorem 9.13 this implies $d _ { i } > 0$ so that the first condition for algebraic stability is satisfied. In order to verify that the matrix $M$ of (9.6) is non-negative definite, we transform it by a suitable matrix. We put

$$
V = \left( c _ { \iota } ^ { \jmath - 1 } \right) _ { \iota , \jmath = 1 , \ . , s } \quad \mathrm { ~ a n d ~ } \quad \alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { k } ) ^ { T } .
$$

A straightforward calculation using the simplifying assumptions $D _ { \Lambda } ( s ) , D _ { \cal B } ( s )$ and $B ( 2 s )$ shows that

$$
\left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { V ^ { T } } } \end{array} \right) M \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} \right) = \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W ^ { T } } } \end{array} \right) \widehat { M } \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W } } \end{array} \right)
$$

where

$$
W = \left( \frac { 1 } { \jmath } ( 1 - i ) ^ { \jmath } \right) _ { \imath = 1 , \ldots , k }
$$

and the $2 k \times 2 k$ matrix $\widehat { M }$ is given by

$$
{ \widehat { M } } = \left( { \begin{array} { l l } { Z } & { Z } \\ { Z } & { Z } \end{array} } \right) , \qquad Z = \mathrm { d i a g } \left( \alpha _ { 1 } , \ldots , \alpha _ { k } \right) - \alpha \alpha ^ { T } .
$$

Since $\alpha _ { \ j } \geq 0$ and $\sum \alpha _ { j } = 1$ it follows from the Cauchy-Schwarz inequality that

$$
x ^ { T } Z x = \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } x _ { \jmath } ^ { 2 } - \left( \sum _ { \jmath = 1 } ^ { k } \alpha _ { \jmath } x _ { \jmath } \right) ^ { 2 } \geq 0
$$

Therefore the matrix $Z$ ， and hence also $\widehat { M }$ ， are non-negative definite matrices.   
This completes the proof of the theorem.

One can ask what are the advantages of the methods $E ( \alpha _ { 1 } , \ldots , \alpha _ { k } )$ with $k > 1$ over the $s$ -stage Gauss Runge-Kutta methods of order $2 s$ . All these methods have the same order and are algebraically stable for $\alpha _ { _ { \mathscr { I } } } \geq 0$ ·

· The Gauss methods have a stability function whose value at infinity satisfies $| R ( \infty ) | = 1$ . In contrast, the new methods allow the spectral radius $\varrho ( S ( \infty ) )$ to be smaller than 1, which improves stability at infinity. For example, numerical investigations of the case $s \simeq 2$ ， $k = 2$ show that $\varrho ( S ( \infty ) )$ has the minimal value $\sqrt { 2 } - 1 \approx 0 . 4 1 4 2 1$ for $\alpha _ { 1 } = 1 2 \sqrt { 2 } - 1 6$ and $\alpha _ { 2 } = 1 - \alpha _ { 1 }$ (see Exercise 7). There are some indications that $L$ -stable methods do not exist: if we could find methods with an internal stage, say $v _ { s } ^ { ( n ) }$ ,equal to $y _ { n + 1 }$ , then the method would be $I$ -stable. Unfortunately, this would imply $c _ { s } = 1$ , which is in contradiction to Lemma 9.12 and to $\alpha _ { _ { \mathscr { I } } } \geq 0$

· The eigenvalues of the Runge-Kutta matrix of the Gauss methods are com-plex (with the exception of one real eigenvalue,if $s$ is odd). Can we hope that, for a suitable choice of $\alpha _ { _ { \mathscr { I } } } \geq 0$ ， all eigenvalues of $\widetilde { B }$ become real? Numerical computations for $s \simeq 2$ and $k = 2$ indicate that this is not possible.

# $B$ -Convergence

Many results of Sections IV.14 and IV.15 have a straightforward extension to general linear methods. The following theorem corresponds to Theorems IV.14.2, IV.14.3,and IV.14.4 and is proved in the same way:

Theorem 9.16. Let $f$ be continuously differentiable and satisfy (9.1). If the matrix $\widetilde { B }$ of method (9.2) is invertible and if

$$
h \nu < \alpha _ { 0 } \big ( \widetilde { B } ^ { - 1 } \big ) ,
$$

then the nonlinear system $( 9 . 2 b )$ has a unique solution.

The next results give estimates of the local and global errors. We formulate these results only for multistep Runge-Kutta methods,because in this case the definitions of $C ( \eta )$ and $B ( p )$ are already available. In analogy to Runge-Kutta

methods we say that method (9.17) has stage order $q$ ,if $C ( q )$ and $B ( q )$ are satisfied. Recall that for the definition of the local error

$$
\delta _ { h } ( x ) = y _ { 1 } - y ( x + h )
$$

one assumes that $y _ { \ i } = y ( x + i h )$ for $i = 1 - k , \dots , 0$ lie on the exact solution.

Theorem 9.17. Suppose that the differential equation satisfies (9.1). If the matrix $\widetilde { B }$ is invertible,if $\overset { \bullet } { \alpha } _ { 0 } \mathopen { } \mathclose \bgroup \left( \widetilde { B } ^ { - 1 } \aftergroup \egroup \right) > 0$ and if the stage order is $q$ , then the local error of method (9.17) satisfies

$$
\| \delta _ { h } ( x ) \| \leq C h ^ { q + 1 } \operatorname* { m a x } _ { \xi \in [ x - ( k - 1 ) h , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| \quad f o r \quad h \nu \leq \alpha < \alpha _ { 0 } ( \widetilde { B } ^ { - 1 } )
$$

where $C$ depends only on the coefficients of the method and on $\alpha$ ·

This result, which corresponds to Proposition IV.15.1, is of particular interest for multistep collocation methods,for which the stage order $\ : q = s + k - 1 \ :$ is maximal. The global error allows the following estimate,which extends Theorem IV.15.3.

Theorem 9.18. Suppose, in addition to the assumptions of Theorem 9.17, that the method (9.17) is algebraically stable.

a)If $\nu > 0$ then the global error satisfies for $h \nu \leq \alpha < \alpha _ { 0 } ( \widetilde { B } ^ { - 1 } )$

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } \frac { e ^ { C _ { 1 } \nu ( x _ { n } - x _ { 0 } ) } - 1 } { C _ { 1 } \nu } C _ { 2 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

b)If $\nu \leq 0$ then (for all $h > 0$ ）

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } ( x _ { n } - x _ { 0 } ) C _ { 2 } \max _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

The constants $C _ { 1 }$ and $C _ { 2 }$ depend only on the coefficients of the method and (for case a) on $\alpha$ □

In contrast to the results of Sect.IV.15 the above theorem holds only for a constant step size implementation.

# Exercises

1. Show that for Runge-Kutta methods, where $A = ( 1 )$ ， $\stackrel { \sim } { A } = \mathbb { 1 }$ , both definitions of algebraic stability (IV.12.5 and V.9.3) are the same.

2. Prove in detail the statement of Example 9.8, that the 2-step 2-stage collocation methods with $c _ { 2 } = 1$ (and $c _ { 1 } \neq 1$ ) are not $G$ -stable.

Hint. The non-negativity of the matrix (9.16) implies $\gamma \geq 1 / 2$ and by considering its determinant,

$$
\gamma \bigl ( 4 \chi _ { 1 } - ( 1 + \chi _ { 2 } ) ^ { 2 } \bigr ) \geq 2 ( \chi _ { 1 } - \chi _ { 2 } ) .
$$

This inequality contradicts (9.14).

3. If a multistep Runge-Kutta method with distinct $c _ { \iota }$ and $c _ { \iota } \geq 0$ satisfies the assumptions $B ( s + k + \xi )$ and $C ( s + k - 1 )$ , then it also satisfies $D _ { B } ( \boldsymbol { \xi } )$

Hint. Show that

$$
\sum _ { j = 1 } ^ { k } \biggl ( q \sum _ { \iota = 1 } ^ { s } b _ { \iota } c _ { \iota } ^ { q - 1 } \widetilde a _ { \iota _ { j } } - \alpha _ { \jmath } ( 1 - ( 1 - j ) ^ { q } ) \biggr ) \bigl ( r ( 1 ) - r ( 1 - j ) \bigr ) = 0
$$

for all polynomials $r ( x )$ of degree $\leq s + k - 1$ which satisfy $r ( c _ { 1 } ) = \ldots =$ $r ( c _ { s } ) = 0$ . For given $j$ , construct such a polynomial which also satisfies

$$
r ( 1 - j ) = 1 , \quad r ( 1 - i ) = 0 \quad \mathrm { f o r } \quad i = 1 , \dots , k \quad \mathrm { a n d } \quad i \neq j .
$$

4.Disprove the conjecture of Burrage (1988) that for every $k$ and $s$ there exist zero-stable multistep Runge-Kutta methods of order $2 s + k - 1$

Hint. Consider the case $s \approx 1$ so that these methods are equivalent to one-leg methods and consult a result of Dahlquist (1983).

5. (Burrage 1988). Show that there exists a zero-stable multistep Runge-Kutta method with $s \simeq 2$ and $k = 2$ which is of order 5.

Result. $c _ { 1 , 2 } = ( \sqrt { 7 } \pm \sqrt { 2 } ) / 5$

6. (Stability at infinity). If a multistep Runge-Kutta method satisfies $D _ { A } ( s )$ and $D _ { B } ( s )$ then we have, e.g., for $s \simeq 2$ and $k = 2$ ，

$$
S ( \infty ) = \left( \begin{array} { c c } { { \alpha _ { 1 } } } & { { \alpha _ { 2 } } } \\ { { 1 } } & { { 0 } } \end{array} \right) - \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c c } { { 1 - c _ { 1 } } } & { { 1 - c _ { 2 } } } \\ { { 1 - c _ { 1 } ^ { 2 } } } & { { 1 - c _ { 2 } ^ { 2 } } } \end{array} \right) ^ { - 1 } \left( \begin{array} { c c } { { \alpha _ { 1 } } } & { { 2 \alpha _ { 2 } } } \\ { { \alpha _ { 1 } } } & { { 0 } } \end{array} \right) .
$$

Formulate this result also for general $s$ and $k$ .

7. Verify that for the method $E ( \alpha _ { 1 } , \alpha _ { 2 } )$ with $0 \leq \alpha _ { 1 } \leq 1$ ， $\alpha _ { 2 } = 1 - \alpha _ { 1 }$ , the spectral radius $\varrho ( S ( \infty ) )$ is minimal for $\alpha _ { 1 } = 1 2 \sqrt { 2 } - 1 6$ .

# Chapter VI. Singular Perturbation Problems and Index 1 Problems

![](images/8e848ab1b8930cb68894ad5f233dbb7f620663acd0b804aee4bbe5464e4e9256.jpg)  
(Drawing by G.Di Marzo)

Singular perturbation problems (SPP) form a special class of problems containing a parameter ε.When this parameter is small, the corresponding differential equation is stiff; when $\varepsilon$ tends to zero, the differential equation becomes differential algebraic. This chapter investigates the numerical solution of such singular perturbation problems. This allows us to understand many phenomena observed for very stiff problems. Much insight is obtained by studying the limit case $\varepsilon = 0$ ("the reduced system” or“problem of index 1") which is usually much easier to analyze.

We start by considering the limit case $\varepsilon = 0$ . Two numerical approaches - the $\varepsilon$ -embedding method and the state space form method - are investigated in Sect. VI.1. We then analyze multistep methods in Sect.VI.2, Runge-Kutta methods in Sect. VI.3, Rosenbrock methods in Sect. VI.4 and extrapolation methods in Sect. VI.5. Convergence is studied for singular perturbation problems and for semiexplicit differential-algebraic systems of "index 1".

# VI.1 Solving Index 1 Problems

Singular perturbation problems (SPP) have several origins in applied mathematics. One comes from fluid dynamics and results in linear boundary value problems containing a small parameter $\varepsilon$ (the coefficient of viscosity） such that for $\varepsilon \to 0$ the differential equation loses the highest derivative (see Exercise 1 below). Others originate in the study of nonlinear oscillations with large parameters (van der Pol 1926,Dorodnicyn 1947） or in the study of chemical kinetics with slow and fast reactions (see e.g., Example (IV.1.4)).

# Asymptotic Solution of van der Pol's Equation

The classical paper of Dorodnicyn (1947) studied the van der Pol Equation (IV.1.5) with large $\mu$ ,i.e., with small $\varepsilon$ . The investigation becomes a little easier if we use Lienard's coordinates (see Exercise I.16.8). In Eq.(IV.1.5'), writen here as

$$
\varepsilon z ^ { \prime \prime } + ( z ^ { 2 } - 1 ) z ^ { \prime } + z = 0 ,
$$

we insert the identity

$$
\varepsilon z ^ { \prime \prime } + ( z ^ { 2 } - 1 ) z ^ { \prime } = { \frac { d } { d x } } \underbrace { \left( \varepsilon z ^ { \prime } + ( { \frac { z ^ { 3 } } { 3 } } - z ) \right) } _ { : = y }
$$

so that (1.1) becomes

$$
\begin{array} { l l } { { y ^ { \prime } = - z } } & { { = : f ( y , z ) } } \\ { { \varepsilon z ^ { \prime } = y - \displaystyle \left( { \frac { z ^ { 3 } } { 3 } } - z \right) } } & { { = : g ( y , z ) . } } \end{array}
$$

Fig.1.1 shows solutions of Eq.(1.2) with $\varepsilon = 0 . 0 3$ in the $( y , z )$ -plane. One ob-serves rapid movements towards the manifold $M$ defined by $y = z ^ { 3 } / 3 - z$ ,close to which the solution becomes smooth. In order to approximate the solution for very small $\varepsilon$ , we set $\varepsilon = 0$ in (1.2) and obtain the so-called reduced system

$$
\begin{array} { l l } { { y ^ { \prime } = - z } } & { { = f ( y , z ) } } \\ { { \displaystyle 0 = y - \left( { \frac { z ^ { 3 } } { 3 } } - z \right) } } & { { = g ( y , z ) . } } \end{array}
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $\mathit { I I }$ ， Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_25, $©$ Springer-Verlag Berlin Heidelberg 2010

![](images/362a30f8f35a30aa0c9e99a9931d53c0a3de239e36f150d9c9bbf5a1ab036b7f.jpg)  
Fig.1.1. Solutions of SPP (1.2)

![](images/1f0803de82e5539ff368c723176eae1a8e44eb42b143b6747a52fb28dfa607f7.jpg)  
Fig.1.2. Reduced problem (1.2')

While(1.2) has no analytic solution, (1.2') can easily be solved to give

$$
y ^ { \prime } = - z = ( z ^ { 2 } - 1 ) z ^ { \prime } \quad \mathrm { o r } \quad \ln | z | - { \frac { z ^ { 2 } } { 2 } } = x + C .
$$

Equation (1.2') is called a differential algebraic equation (DAE), since it combines a differential equation (first line) with an algebraic equation (second line). Such a problem only makes sense if the initial values are consistent, i.e., lie on the manifold $M$ . The points of $M$ with coordinates $y = \pm 2 / 3$ ， $z = \mp 1$ are of special interest (Fig. 1.2): at these points the partial derivative $g _ { z } = \partial g / \partial z$ vanishes and the defining manifold is no longer “transversal’ to the direction of the fast movement. Here the solutions of (1.2'） cease to exist, while the solutions of the full problem(1.2) for $\varepsilon \to 0$ jump with “infinite” speed to the opposite manifold. For $- 1 < z < 1$ the manifold $M$ is unstable for the solution of (1.2) (here $g _ { z } > 0$ ）， otherwise $M$ is stable $( g _ { z } < 0 )$

We demonstrate the power of the reduced equation by answering the question:

what is the period $T$ of the limit cycle solution of van der Pol's equation for $\varepsilon \to 0 \ ?$ Fig.1.2 shows that the asymptotic value of $T$ is just twice the time which $z ( x )$ of (1.3) needs to advance from $z = - 2$ to $z = - 1$ ,i.e.,

$$
T = 3 - 2 \ln 2 .
$$

This is the first term of Dorodnicyn's asymptotic formula. We also see that $z ( x )$ reaches its largest values (i.e.， crosses the Poincaré cut $z ^ { \prime } = 0$ ， see Fig.I.16.2) at $z = \pm 2$ . We thus have the curious result that the limit cycle of van der Pol's equation (1.1) has the same asymptotic initial value $z \approx 2$ and $z ^ { \prime } = 0$ for $\varepsilon  0$ and for $\varepsilon \to \infty$ (see Eq. (I.16.10)).

# The $\varepsilon$ -Embedding Method for Problems of Index 1

We now want to study the behaviour of the numerical solution for $\varepsilon  0$ .This will give us insight into many phenomena encountered for very stiff equations and also suggest advantageous numerical procedures for stiff and differential-algebraic equations. Let an arbitrary singular perturbation problem be given,

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { \varepsilon z ^ { \prime } = g ( y , z ) , } \end{array}
$$

where $y$ and $z$ are vectors； suppose that $f$ and $g$ are sufficiently often differentiable vector functions of the same dimensions as $y$ and $z$ ，respectively. The corresponding reduced equation is the DAE

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) , } \end{array}
$$

whose initial values are consistent if $0 = g ( y _ { 0 } , z _ { 0 } )$ ． A general assumption of the present chapter will be that the Jacobian

$$
g _ { z } ( y , z ) \mathrm { i s \ i n v e r t i b l e }
$$

in a neighbourhood of the solution of (1.6). Equation (1.6b) then possesses a locally unique solution $z = G ( y )$ ("Implicit Function Theorem") which inserted into (1.6a) gives

$$
y ^ { \prime } = f { \bigl ( } y , G ( y ) { \bigr ) } ,
$$

the so-called “state space form”,an ordinary differential system. Under the as-sumption (1.7),Eq.(1.6) is said to be a differential-algebraic equation of index $l$

An interesting approach for solving (1.6) is to apply some numerical method to the SPP (1.5) and to put $\varepsilon = 0$ in the resulting formulas. Let us illustrate this approach for Runge-Kutta methods. Applied to the system (1.5) we obtain

$$
Y _ { n \imath } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { \imath j } \ f ( Y _ { n j } , Z _ { n \jmath } )
$$

$$
\begin{array} { r c l } { { } } & { { } } & { { \varepsilon Z _ { n \scriptscriptstyle 1 } = \varepsilon z _ { n } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } g \left( Y _ { n \jmath } , Z _ { n \jmath } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { y _ { n + 1 } = y _ { n } + h \displaystyle \sum _ { \imath = 1 } ^ { s } b _ { \imath } f \left( Y _ { n \imath } , Z _ { n \imath } \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \varepsilon z _ { n + 1 } = \varepsilon z _ { n } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \imath } g \left( Y _ { n \imath } , Z _ { n \jmath } \right) . } } \end{array}
$$

We now suppose that the RK matrix $\left( { { a _ { \iota } } _ { \ j } } \right)$ is invertible and obtain from (1.9b)

$$
h g ( Y _ { n \imath } , Z _ { n \imath } ) = \varepsilon \sum _ { \jmath = 1 } ^ { s } \omega _ { \imath \jmath } ( Z _ { n \jmath } - z _ { n } ) ,
$$

where the $\omega _ { \imath \jmath }$ are the elements of the inverse of $\left( { { a _ { \iota } } _ { \jmath } } \right)$ .Inserting this into (1.9d) makes the definition of $z _ { n + 1 }$ independent of $\varepsilon$ . We thus put without more ado $\varepsilon = 0$ and obtain

$$
\begin{array} { c } { { { \cal Y } _ { n \displaystyle i } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i _ { j } } ~ f \left( Y _ { n _ { 2 } } , Z _ { n _ { 2 } } \right) } } \\ { { 0 = g ( Y _ { n i } , Z _ { n _ { 1 } } ) } } \\ { { y _ { n \displaystyle + 1 } = y _ { n } + h \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ f } } ~ f \left( Y _ { n \mathrm { } } , Z _ { n \mathrm { } } \right) } } \\ { { { } } } \\ { { z _ { n \displaystyle + 1 } = \left( 1 - \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ r } } \omega _ { \mathrm { n } j } \right) z _ { n } + \displaystyle \sum _ { \mathrm { \scriptsize ~ r = 1 } } ^ { s } b _ { \mathrm { \scriptsize ~ w } _ { \mathrm { i } j } } ~ Z _ { n _ { 2 } } . } } \end{array}
$$

Here

$$
1 - \sum _ { i , \ j = 1 } ^ { s } b _ { i } \omega _ { \ i \ j } = R ( \infty )
$$

(see Eq.(IV.3.15), where $R ( z )$ is the stability function of the method.

# State Space Form Method

The numerical solution $( y _ { n + 1 } , z _ { n + 1 } )$ of the above approach will usually not lie on the manifold $g ( y , z ) = 0$ . However,this can easily be repaired by replacing (1.11d) by the condition

$$
0 = g ( y _ { n + 1 } , z _ { n + 1 } ) .
$$

Then, we do not only have $Z _ { n } \mathrm {                                          } _ { } = G ( Y _ { n } \mathrm { \ } _ { \mathrm { } n } )$ (see (1.11b), but also $z _ { n + 1 } = G ( y _ { n + 1 } )$ In this case the method (1.11a-c),(1.12) is identical to the solution of the state space form (1.8) with the same Runge-Kutta method. This will be called the state space form method. The whole situation is summarized in the following diagram:

SPP (1.5) m↑0 DAE (1.6) z=G(y） → ODE (1.8)   
RK RK √   
Sol. (1.9) →0 $\varepsilon$ -embedding method state space form method Sol. (1.12)

Of special importance here are stifly accurate methods,i.e., methods which satisfy

$$
a _ { s \imath } = b _ { \imath } \qquad \mathrm { f o r } \quad i = 1 , \ldots , s .
$$

This means that $y _ { n + 1 } = Y _ { n s } , z _ { n + 1 } = Z _ { n s }$ and(12)isicefor stiffly accurate methods the $\varepsilon$ -embedding method and the state space form method are identical. For this reason, Griepentrog & März（1986) denote such methods IRK(DAE).

Both approaches have their own merits. Theoretical results for the $\varepsilon$ -embedding method yield insight into the method when applied to singular perturbation problems. Moreover, this approach can easily be extended to more general situa-tions,where the algebraic relation is not explicitly separated from the differential equation (see below). The state space form method, on the other hand, has the advantage that it is not restricted to implicit methods. Applying an explicit Runge-Kutta method or a multistep method to Eq.(1.8) is certainly a method of choice for semi-explicit index 1 equations. No new theory is necessary in this case.

# A Transistor Amplifier

...auf eine merkwirdige Tatsache aufmerksam machen, das ist die auBerordentlich grosse Zahl berihmter Mathematiker, die aus Konigsberg stammen ...: Kant 1724, Richelot 1808, Hesse 1811, Kirchhoff 1824, Carl Neumann 1832, Clebsch 1833,Hilbert 1862. (F. Klein, Entw. der Math., p.159)

Very often, differential-algebraic problems arising in practice are not at once in the semi-explicit form(1.6),but rather in the form $M u ^ { \prime } = \varphi ( u )$ where $M$ is a constant singular matrix.

As an example we compute the amplifier of Fig.1.3, where $U _ { e } ( t )$ is the entry voltage, $U _ { b } = 6$ the operating voltage, $U _ { i } ( t ) ~ ( i = 1 , 2 , 3 , 4 , 5 )$ the voltages at the nodes 1,2,3,4,5,and $U _ { 5 } ( t )$ the output voltage. The current through a resistor satisfies $I = U / R$ $( \mathrm { O h m ~ } 1 8 2 7 )$ , the current through a capacitor $I = C \cdot d U / d t$ ， where $R$ and $C$ are constants and $U$ the voltage. The transistor acts as amplifier in that the current from node 4 to node 3 is 99 times larger than that from node 2 to node 3 and depends on the voltage difference $U _ { 3 } - U _ { 2 }$ in a nonlinear way. Kirchhoff's law (a Konigsberg discovery) says that the sum of currents entering a node vanishes. This law applied to the 5 nodes of Fig.1.3 leads to the following equations:

![](images/0bbfd3ba238d96433ac51fa1ba5b5594c36fb5a272aff7ac94a0ca8f406b1220.jpg)  
Fig.1.3. A transistor amplifier

$$
\begin{array} { r l } { \textnormal { e l . } } & { \frac { U _ { k } } { R _ { 0 } } - \frac { U _ { 1 } } { R _ { 0 } } + C _ { 1 } ( U _ { 2 } ^ { \prime } - U _ { 1 } ^ { \prime } ) = 0 } \\ { \textnormal { e 2 . } } & { \frac { U _ { k } } { R _ { 2 } } - U _ { 2 } \left( \frac { 1 } { R _ { 1 } } + \frac { 1 } { R _ { 2 } } \right) + C _ { 1 } ( U _ { 1 } ^ { \prime } - U _ { 2 } ^ { \prime } ) - 0 . 0 1 f ( U _ { 2 } - U _ { 3 } ) = 0 } \\ { \textnormal { e 3 . } } & { f ( U _ { 2 } - U _ { 3 } ) - \frac { U _ { 3 } } { R _ { 3 } } - C _ { 2 } U _ { 3 } ^ { \prime } = 0 } \\ { \textnormal { e 4 . } } & { \frac { U _ { k } } { R _ { 4 } } - \frac { U _ { 4 } } { R _ { 4 } } + C _ { 3 } ( U _ { 5 } ^ { \prime } - U _ { 4 } ^ { \prime } ) - 0 . 9 9 f ( U _ { 2 } - U _ { 3 } ) = 0 } \\ { \textnormal { e 5 . } } & { - \frac { U _ { 5 } } { R _ { 5 } } + C _ { 3 } ( U _ { 4 } ^ { \prime } - U _ { 5 } ^ { \prime } ) = 0 . } \end{array}
$$

As constants we adopt the values reported (for a similar problem) by Rentrop, Roche & Steinebach(1989)

$$
\begin{array} { r l } & { f ( U ) = 1 0 ^ { - 6 } \left( \exp \left( \frac { U } { 0 . 0 2 6 } \right) - 1 \right) } \\ & { R _ { 0 } = 1 0 0 0 , \quad R _ { 1 } = \ldots = R _ { 5 } = 9 0 0 0 } \\ & { C _ { k } = k \cdot 1 0 ^ { - 6 } , \quad k = 1 , 2 , 3 , } \end{array}
$$

and the initial signal is chosen as

$$
U _ { e } ( t ) = 0 . 4 \cdot \sin ( 2 0 0 \pi t ) .
$$

Equations (1.14) are of the form $M \mathfrak { u } ^ { \prime } = \varphi ( \mathfrak { u } )$ where

$$
{ \cal M } = \left( \begin{array} { c c c c c } { { - C _ { 1 } } } & { { C _ { 1 } } } & { { } } & { { } } & { { } } \\ { { C _ { 1 } } } & { { - C _ { 1 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - C _ { 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { - C _ { 3 } } } & { { C _ { 3 } } } \\ { { } } & { { } } & { { } } & { { C _ { 3 } } } & { { - C _ { 3 } } } \end{array} \right)
$$

is obviously a singular matrix of rank 3. The sum of the first two and of the last two equations leads directly to two algebraic equations. Introducing e.g.,

$$
U _ { 1 } - U _ { 2 } = y _ { 1 } , \quad U _ { 3 } = y _ { 2 } , \quad U _ { 4 } - U _ { 5 } = y _ { 3 } , \quad U _ { 1 } = z _ { 1 } , \quad U _ { 4 } = z _ { 2 } ,
$$

transforms equations (1.14) to the form (1.6). Consistent initial values must thus satisfy $\varphi _ { 1 } ( u ) + \varphi _ { 2 } ( u ) = 0$ and $\varphi _ { 4 } ( u ) + \varphi _ { 5 } ( u ) = 0$ . If we put $U _ { 2 } ( 0 ) = U _ { 3 } ( 0 )$ ，we have $f ( U _ { 2 } ( 0 ) - U _ { 3 } ( 0 ) ) = 0$ . Since $U _ { e } ( 0 ) = 0$ , we then easily find consistent initial values, e.g., as

$$
U _ { 1 } ( 0 ) = 0 , \quad U _ { 2 } ( 0 ) = U _ { 3 } ( 0 ) = \frac { U _ { b } R _ { 1 } } { R _ { 1 } + R _ { 2 } } , \quad U _ { 4 } ( 0 ) = U _ { b } , \quad U _ { 5 } ( 0 ) = 0 .
$$

# Problems of the Form $M \boldsymbol { u } ^ { \prime } = \varphi ( \boldsymbol { u } )$

Numerical methods for problems of the form

$$
M u ^ { \prime } = \varphi ( u ) ,
$$

where $M$ is a constant matrix,can be derived as follows: we assume that $M$ is regular, apply an ODE method to $u ^ { \prime } = M ^ { - 1 } \varphi ( u )$ and multiply the resulting formulas by $M$ . For Runge-Kutta methods we obtain in this way

$$
M ( U _ { n \imath } - u _ { n } ) = h \sum _ { j = 1 } ^ { s } a _ { \imath j } \varphi ( U _ { n j } )
$$

$$
u _ { n + 1 } = \bigg ( 1 - \sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } \bigg ) u _ { n } + \sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } U _ { n j } ,
$$

where again $( \omega _ { i j } )$ is the inverse of $\left( a _ { \imath \jmath } \right)$ . The second formula was obtained from

$$
M ( u _ { n + 1 } - u _ { n } ) = h \sum _ { i = 1 } ^ { s } b _ { i } \varphi ( U _ { n \ i } )
$$

in exactly the same way as above (see (1.10)).

Formulas (1.18) also make sense formally when $M$ is a singular matrix. In this case,problem (1.17) is mathematically equivalent to a semi-explicit system (1.6) and method (1.18) corresponds to method (1.11). This can be seen as follows: we decompose the matrix $M$ (e.g., by Gaussian elimination with total pivoting) as

$$
M = S \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) T ,
$$

where $S$ and $T$ are invertible matrices and the dimension of $I$ represents the rank of $M$ . Inserting this into (1.17), multiplying by $S ^ { - 1 }$ , and using the transformed variables

$$
T u = { \left( \begin{array} { l } { y } \\ { z } \end{array} \right) } 
$$

gives

$$
{ \binom { y ^ { \prime } } { 0 } } = S ^ { - 1 } \varphi \Bigl ( T ^ { - 1 } { \binom { y } { z } } \Bigr ) = : \left( { \begin{array} { l } { f ( y , z ) } \\ { g ( y , z ) } \end{array} } \right) ,
$$

a problem of type (1.6). An initial value $u _ { 0 }$ is consistent if $\varphi ( u _ { 0 } )$ lies in the range of the matrix $M$

Similarly,if (1.19) is inserted into (1.18),and the variables

$$
T U _ { n j } = \left( \begin{array} { l } { { Y _ { n j } } } \\ { { Z _ { n j } } } \end{array} \right) , \qquad T u _ { n } = \left( \begin{array} { l } { { y _ { n } } } \\ { { z _ { n } } } \end{array} \right)
$$

are introduced, Eq.(1.18b) (for $Z _ { n + 1 } )$ and Eq.(1.18c) (for $Y _ { n + 1 } )$ lead precisely to equations (1.11). This means that the diagram

$$
\{ u _ { n } \}
$$

commutes. An important consequence of this commutativity is that all results for semi-explicit systems (1.6) and the $\varepsilon$ -embedding method (1.11) (existence of a numerical solution, convergence,asymptotic expansions,.. .） also apply to implicit problems (1.17) with singular $M$ and method (1.18).

All codes,such as RADAU5,which have an option for implicit differential equations (1.17) can thus be applied directly. This has been done for problem (1.14) with initial values (1.16),integration interval $0 \le x \le 0 . 2$ , and $T o l = 1 0 ^ { - 4 }$ · The code computed the solution $U _ { 5 } ( t )$ displayed in Fig.1.4 in 556 (accepted) steps. The comparison with the entry voltage $U _ { e } ( t )$ shows that our amplifier is working. See also Hairer,Lubich & Roche (1989),p.108-111 for a more elaborate example.

![](images/a9cdc848062e5b556107f12d2c92277b92f6394ac0b773d8bb6eaecb06a85d8c.jpg)  
Fig.1.4. Computed solution of amplifier problem (1.14)

# Convergence of Runge-Kutta Methods

If the method is stiffly accurate, the numerical solutions (1.11） are equivalent to those of the ordinary equation (1.8). Therefore the convergence of the solutions is described by Theorems II.3.4 and II.3.6 as

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) ,
$$

where $p$ is the classical order of the method (the second formula follows from a Lipschitz condition for $G$ ). For general methods,the estimate (1.24) remains valid for $y _ { n }$ ,because (1.11a,b,c) are independent of $z _ { n }$ and do not change if (1.11d) is replaced by (1.12). Thus we only have to prove a convergence result for $z _ { n }$ .An essential ingredient of the following theorem is the stage order $q$ of the method, i.e., condition $C ( q )$ of Sect. II.7 or IV.5.

Theorem 1.1. Suppose that the system (1.6) satisfies(1.7) in a neighbourhood of the exact solution $( y ( x ) , z ( x ) )$ and assume the initial values are consistent. Consider a Runge-Kutta method of order $p$ ， stage order $q$ and with invertible matrix $A$ . Then the numerical solution of(1.1la-d) has global error

$$
z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { r } ) \quad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t ,
$$

where

$a$ ） $r = p$ for stiffly accurate methods,   
$b _ { . }$ ） $r = \operatorname* { m i n } ( p , q + 1 )$ if the stability function satisfes $- 1 \leq R ( \infty ) < 1$ $c _ { , }$ ） $r = \operatorname* { m i n } ( p - 1 , q )$ f $R ( \infty ) = + 1$ .   
d）1f $\dot { | } R ( \infty ) | > 1$ , the numerical solution diverges.

Proof. Part (a) has already been discussed. For the remaining cases we proceed as follows: we first observe that Condition $C ( q )$ and order $p$ imply

$$
z ( x _ { n } + c _ { \imath } h ) = z ( x _ { n } ) + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } z ^ { \prime } ( x _ { n } + c _ { \jmath } h ) + { \mathcal O } ( h ^ { q + 1 } )
$$

$$
z ( x _ { n + 1 } ) = z ( x _ { n } ) + h \sum _ { i = 1 } ^ { s } b _ { \imath } z ^ { \prime } ( x _ { n } + c _ { \imath } h ) + \mathcal { O } ( h ^ { p + 1 } ) .
$$

Since $A$ is invertible we can compute $z ^ { \prime } ( x _ { n } + c _ { \jmath } h )$ from(1.26a) and insert it into (1.26b). This gives

$$
z ( x _ { n + 1 } ) = \varrho z ( x _ { n } ) + b ^ { T } A ^ { - 1 } \widehat Z _ { n } + \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { q + 1 } )
$$

where $\varrho = 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } = R ( \infty )$ and $\widehat { Z } _ { n } = ( z ( x _ { n } + c _ { 1 } h ) , \ldots , z ( x _ { n } + c _ { s } h ) ) ^ { T }$ .We then denote the global error by $\Delta z _ { n } = z _ { n } - z ( x _ { n } )$ ， and $\Delta Z _ { n } = Z _ { n } - \widehat { Z } _ { n }$ . Subtracting (1.27) from (1.11d) yields

$$
\begin{array} { r } { \Delta z _ { n + 1 } = \varrho \Delta z _ { n } + b ^ { T } A ^ { - 1 } \Delta Z _ { n } + \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { q + 1 } ) . } \end{array}
$$

Our next aim is to estimate $\Delta Z _ { n }$ . For this we have to consider the $y$ -component of the system. Due to (1.11a-c) the values $y _ { n } , Y _ { n \imath }$ are those of the Runge-Kutta method applied to (1.8). It thus follows from Theorem II.8.1 that $y _ { n } - y ( x _ { n } ) =$ $e _ { p } ( x _ { n } ) h ^ { p } + { \mathcal { O } } ( h ^ { p + 1 } )$ . Since Eq.(1.26a) also holds with $z ( x )$ replaced by $y ( x )$ ， we can subtract this formula from (1.11a) and so obtain

$$
\begin{array} { r l } {  { Y _ { n \imath } - y ( x _ { n } + c _ { \imath } h ) = y _ { n } - y ( x _ { n } ) } } \\ & { \quad + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \Big ( f \big ( Y _ { n \jmath } , G ( Y _ { n \jmath } ) \big ) - f \big ( y ( x _ { n } + c _ { \jmath } h ) , G ( y ( x _ { n } + c _ { \jmath } h ) ) \Big ) + \mathcal O ( h ^ { q + 1 } ) . } \end{array}
$$

This implies that

$$
Y _ { n \imath } - y ( x _ { n } + c _ { \imath } h ) = { \mathcal O } ( h ^ { \nu } ) \qquad { \mathrm { w i t h } } \quad \nu = \operatorname* { m i n } ( p , q + 1 ) .
$$

Because of (1.11b) we get

$$
Z _ { n \ i } - z ( x _ { n } + c _ { \ i } h ) = G ( Y _ { n \ i } ) - G \big ( y ( x _ { n } + c _ { \ i } h ) \big ) = \mathcal { O } ( h ^ { \nu } )
$$

and Eq.(1.28) becomes

$$
\Delta z _ { n + 1 } = \varrho \Delta z _ { n } + \delta _ { n + 1 } , \qquad \mathrm { w h e r e } \quad \delta _ { n + 1 } = \mathcal { O } \big ( h ^ { \nu } \big ) .
$$

Repeated insertion of this formula gives

$$
\Delta z _ { n } = \sum _ { \imath = 1 } ^ { n } \varrho ^ { n - \imath } \delta _ { \imath } ,
$$

because $\Delta z _ { 0 } = 0$ . This proves the statement for $\varrho \neq - 1$ . For the case $\varrho = - 1$ the error $\Delta z _ { n }$ is a sum of differences $\delta _ { \jmath + 1 } - \delta _ { j }$ . Since $\delta _ { n + 1 }$ is actually of the form $\delta _ { n + 1 } = d ( x _ { n } ) h ^ { \nu } + \mathcal { O } ( h ^ { \nu + 1 } )$ we have $\begin{array} { r } { \dot { \delta } _ { \jmath + 1 } - \dot { \delta } _ { \jmath } = \mathcal { O } ( h ^ { \nu + 1 } ) } \end{array}$ and the statement also follows in this situation. □

The order reduction in the $z$ -component (for non stiffly accurate methods) was first studied by Petzold (1986) in a more general context.

# Exercises

1. Compute the solutions of the boundary value problems

$$
\begin{array} { c c c } { { \varepsilon y ^ { \prime \prime } + y ^ { \prime } + y = 1 } } & { { \mathrm { r e s p e c t i v e l y } } } & { { \varepsilon y ^ { \prime \prime } - y ^ { \prime } + y = 1 } } \\ { { } } & { { } } & { { y ( 0 ) = y ( 1 ) = 0 , \quad \mathrm { f o r } \quad \varepsilon > 0 . } } \end{array}
$$

Observe that the solutions possess, for $\varepsilon \to 0$ ,a"boundary layer”on one of the two sides of [O,1] and that the limit solutions for $\varepsilon = 0$ satisfy

$$
y ^ { \prime } + y = 1 \qquad { \mathrm { r e s p e c t i v e l y } } \qquad - y ^ { \prime } + y = 1
$$

with one of the two boundary conditions being lost.

# VI.2 Multistep Methods

The aim of this section is to study convergence of multistep methods when applied to singular perturbation problems (Runge-Kutta methods will be treated in Sect. VI.3). We are interested in estimates that hold uniformly for $\varepsilon \to 0$ . The re-sults of the previous chapters cannot be applied. Since the Lipschitz constant of the singular perturbation problem (1.5) is of size $\mathcal { O } ( \varepsilon ^ { - 1 } )$ ， the estimates of Sect. III.4 are useless. Also the one-sided Lipschitz constant is in general $\mathcal { O } ( \varepsilon ^ { - 1 } )$ , so that the convergence results of Sect. V.8 can neither be applied. Let us start by considering the reduced problem.

# Methods for Index 1 Problems

A multistep method applied to the system $y ^ { \prime } = f ( y , z )$ ， $\varepsilon z ^ { \prime } = g ( y , z )$ gives

$$
\begin{array} { c } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } y _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f ( y _ { n + \imath } , z _ { n + \imath } ) } } \\ { { \displaystyle \varepsilon \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } z _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } g ( y _ { n + \imath } , z _ { n + \imath } ) . } } \end{array}
$$

By putting $\varepsilon \approx 0$ we obtain ( $\varepsilon$ -embedding method)

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { n + \ i } = h \sum _ { \ i = 0 } ^ { k } \beta _ { \ i } f ( y _ { n + \ i } , z _ { n + \ i } )
$$

$$
0 = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } g ( y _ { n + \imath } , z _ { n + \imath } )
$$

which allows us to apply a multistep method to the differential-algebraic system (1.6). This approach was first proposed (for the BDF methods) by Gear (1971).

Theorem 2.1. Suppose that the system (1.6) satisfies (1.7). Consider a multistep method of order $p$ which is stable at the origin and at infinity(O and $\infty$ are in the stability region) and suppose that the error of the starting values $y _ { \jmath } , z _ { \jmath }$ for $j = 0 , \ldots , k - 1$ is $\mathcal { O } ( h ^ { p } )$ . Then the global error of(2.2) satisfies

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } )
$$

for $x _ { n } - x _ { 0 } = n h \leq C o n s t .$

Proof.Formula (2.2b) is a stable recursion for $\delta _ { n } = g ( y _ { n } , z _ { n } )$ , because $\infty$ lies in the stability region of the method. This together with the assumption on the starting values implies that $\delta _ { n } = \mathcal { O } ( h ^ { p } )$ for all $n \geq 0$ . By the Implicit Function Theorem $g ( y _ { n } , z _ { n } ) = \delta _ { n }$ can be solved for $z _ { n }$ and yields

$$
z _ { n } = G ( y _ { n } ) + \mathcal { O } ( h ^ { p } )
$$

with $G ( y )$ as in (1.8). Inserting (2.3) into (2.2a) gives the multistep formula for the differential equation (1.8) with an $\mathcal { O } ( h ^ { p + 1 } )$ perturbation. The statement then follows from the convergence proof of Sect. III.4. □

For the implicit index l problem (1.17) the multistep method becomes

$$
M \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } u _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \varphi ( u _ { n + \imath } )
$$

and convergence without any order reduction for methods satisfying the hypotheses of Theorem 2.1 follows from the transformation (1.20) and the diagram (1.23).

The state space from approach is also possible for multistep methods. We just have to replace (2.2b) by

$$
g ( y _ { n + k } , z _ { n + k } ) = 0 .
$$

Method $( 2 . 2 \mathsf { a } , \mathsf { c } )$ is equivalent to the solution of(1.8) by the above multistep method. Hence,we have convergence as for nonstiff ordinary differential equations. The assumption $^ { 6 6 } \infty \in S ^ { \prime \prime }$ is no longer necessary and even explicit methods can be applied.

# Convergence for Singular Perturbation Problems

The error propagation has been studied by Soderlind & Dahlquist (1981) using $G$ stability estimates. Convergence results were first obtained by Lotstedt (1985) for BDF methods. The following convergence result by Lubich (1991), based on the smoothness of the exact solution and thus uniform in $\varepsilon$ as long as we stay away from transient phases,gives optimal error bounds for arbitrary multistep methods.

The Jacobian of the system (1.5) is of the form

$$
\left( \begin{array} { c c } { { f _ { y } } } & { { f _ { z } } } \\ { { \varepsilon ^ { - 1 } g _ { y } } } & { { \varepsilon ^ { - 1 } g _ { z } } } \end{array} \right)
$$

and its dominant eigenvalues are seen to be close to ${ \varepsilon } ^ { - 1 } \lambda$ where $\lambda$ represents the eigenvalues of $g _ { z }$ . For reasons of stability we assume throughout this subsection that the eigenvalues of $g _ { z }$ have negative real part. More precisely, we assume that

for $( y , z )$ in a neighbourhood of the considered solution. We then have the following result for method (2.1a,b):

Theorem 2.2 (Lubich 1991). Suppose that the multistep method is of order $p$ ， $A ( \alpha )$ -stable and strictly stable at infinity. If the problem (1.5) satisfies (2.5), then the error is bounded for $h \geq \varepsilon$ and $n h \le \overline { { x } } - x _ { 0 }$ by

$$
\begin{array} { r l } {  { \| y _ { n } - y ( x _ { n } ) \| + \| z _ { n } - z ( x _ { n } ) \| } } \\ & { \leq C \Big ( \underset { 0 \leq \jmath < k } { \operatorname* { m a x } } \ \| y _ { \jmath } - y ( x _ { \jmath } ) \| + h ^ { p } \int _ { x _ { 0 } } ^ { x _ { n } } \| y ^ { ( p + 1 ) } ( x ) \| d x } \\ & { \qquad + ( h + \varrho ^ { n } ) \underset { 0 \leq \jmath < k } { \operatorname* { m a x } } \ \| z _ { \jmath } - z ( x _ { \jmath } ) \| + \varepsilon h ^ { p } \underset { x _ { 0 } \leq x \leq x _ { n } } { \operatorname* { m a x } } \| z ^ { ( p + 1 ) } ( x ) \| \Big ) } \end{array}
$$

with $0 < \varrho < 1$ . This estimate holds for $h \leq h _ { 0 }$ （ $h _ { 0 }$ sufficiently small, but independent of $\varepsilon$ ), and provided that the starting values are in $a$ sufficiently small, $h$ - and $\varepsilon$ -independent neighbourhood of the exact solution. The constants $C$ and $\varrho$ are independent of $\varepsilon$ and $h$

Proof. The proof is divided into several parts: in part (a) we shall derive recursive estimates for the global error, these will be solved in part (b); part (c) proves an inequality which is needed in (a).

a) First we insert the exact solution of(1.5) into the method (2.1) and so obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { i } y ( x _ { n + \imath } ) = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f \bigl ( y ( x _ { n + \imath } ) , z ( x _ { n + \imath } ) \bigr ) + d _ { n + k } } } \\ { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } z ( x _ { n + \imath } ) = \frac { h } { \varepsilon } \sum _ { \imath = 0 } ^ { k } \beta _ { i } g \bigl ( y ( x _ { n + i } ) , z ( x _ { n + \imath } ) \bigr ) + e _ { n + k } , } } \end{array}
$$

where the perturbations $d _ { n + k } , e _ { n + k }$ can be estimated (for $n \geq 0$ as

$$
\begin{array} { l } { \| d _ { n + k } \| \leq C _ { 1 } h ^ { p } \displaystyle \int _ { x _ { n } } ^ { x _ { n + k } } \| y ^ { ( p + 1 ) } ( x ) \| d x } \\ { \| e _ { n + k } \| \leq C _ { 2 } h ^ { p + 1 } \displaystyle \operatorname* { m a x } _ { x _ { n } \leq x \leq x _ { n + k } } \| z ^ { ( p + 1 ) } ( x ) \| . } \end{array}
$$

We then denote the global errors by $\Delta y _ { n } = y _ { n } - y ( x _ { n } )$ ， $\Delta z _ { n } = z _ { n } - z ( x _ { n } )$ and introduce the differences

$$
\Delta f _ { n + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Bigl ( f ( y _ { n + \imath } , z _ { n + \imath } ) - f \bigl ( y ( x _ { n + \imath } ) , z ( x _ { n + \imath } ) \bigr ) \Bigr ) , \qquad n \geq 0 ,
$$

$\Delta f _ { \jmath } = 0$ for $j < k$ . Subtraction of (2.6a) from (2.1a) yields for $n \geq 0$

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } \Delta y _ { n + \imath } = h \Delta f _ { n + k } - d _ { n + k } .
$$

Guided by previous experience (see (V.7.41)), we define $d _ { 0 } , \ldots , d _ { k - 1 }$ so that (2.8)

also holds for negative $n$ . Solving for $\Delta y _ { n }$ gives

$$
\Delta y _ { n } = h \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } ( 0 ) \Delta f _ { \jmath } - \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } ( 0 ) d _ { \jmath }
$$

where $r _ { \jmath } ( 0 )$ is defined in (V.7.44). These numbers are the coefficients of $r ( \zeta , 0 ) =$ $\zeta ^ { - k } / \varrho \big ( \breve { \zeta } ^ { - 1 } \big )$ . By zero-stability of the method, the sequence $\{ r _ { \jmath } ( 0 ) \}$ is bounded, so that a Lipschitz condition for $f ( y , z )$ implies the estimate

$$
\| \Delta y _ { n } \| \leq h \sum _ { \jmath = 0 } ^ { n } \bigl ( M \| \Delta y _ { \jmath } \| + N \| \Delta z _ { \jmath } \| \bigr ) + C _ { 3 } \sum _ { \jmath = 0 } ^ { n } \| d _ { \jmath } \| .
$$

A more refined estimate is necessary for the $z$ -component. We take the difference of (2.1b) and (2.6b) and then subtract from both sides the quantity

$$
\frac { h } { \varepsilon } \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } J \Delta z _ { n + \iota } \qquad \mathrm { w h e r e } \quad J = g _ { \iota } ( y _ { 0 } , z _ { 0 } ) .
$$

This yields

$$
\sum _ { \ i = 0 } ^ { k } \bigl ( \alpha _ { \ i } I - \beta _ { \ i } { \frac { h } { \varepsilon } } J \bigr ) \Delta z _ { n + \ i } = { \frac { h } { \varepsilon } } \Delta g _ { n + k } - e _ { n + k }
$$

where

$$
\Delta g _ { n + k } = \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } \Big ( g \big ( y _ { n + \imath } , z _ { n + \imath } \big ) - g \big ( y \big ( x _ { n + \imath } \big ) , z \big ( x _ { n + \imath } \big ) \big ) - J \Delta z _ { n + \imath } \Big ) ,
$$

and $\Delta g _ { \jmath } = 0$ for $\jmath < k$ . We again define $e _ { 0 } , \ldots , e _ { k - 1 }$ such that (2.11) holds for negative $\mathscr { n }$ ,and we then solve (2.11) for $\Delta z _ { n }$ . This gives

$$
\Delta z _ { n } = \frac { h } { \varepsilon } \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } \left( \frac { h } { \varepsilon } J \right) \Delta g _ { \jmath } - \sum _ { \jmath = 0 } ^ { n } r _ { n - \jmath } \left( \frac { h } { \varepsilon } J \right) e _ { \jmath }
$$

where the matrices $\begin{array} { r } { r _ { \jmath } \left( \frac { h } { \varepsilon } \boldsymbol { J } \right) } \end{array}$ are defined by (see Formula (V.7.50))

$$
{ \frac { h } { \varepsilon } } \sum _ { \jmath \geq 0 } r _ { \jmath } \left( { \frac { h } { \varepsilon } } \ J \right) \zeta ^ { \jmath } = \left( { \frac { \varepsilon } { h } } \delta ( \zeta ) I - J \right) ^ { - 1 } { \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } }
$$

with $\delta ( \zeta )$ given in (V.7.45). In part (c) below we shall prove that

$$
\frac { h } { \varepsilon } \left\| r _ { \ j } \left( \frac { h } { \varepsilon } \ j \right) \right\| \leq C \kappa ^ { \ j } \qquad \mathrm { w i t h } \quad 0 < \kappa < 1 .
$$

Inserted into (2.13) we thus get

$$
\| \Delta z _ { n } \| \leq \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \big ( L \| \Delta y _ { \jmath } \| + \ell \| \Delta z _ { \jmath } \| \big ) + C _ { 4 } \frac { \varepsilon } { h } \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \| e _ { \jmath } \| .
$$

It is important to remark that the Lipschitz constant $\ell$ can be made arbitrarily small by shrinking the considered interval.

b) In ordertosolvetheinequalities (2.9)and (2.16)we definesequences $\{ u _ { n } \}$ and $\{ v _ { n } \}$ by

$$
\begin{array} { l } { \displaystyle { u _ { n } = h \sum _ { \jmath = 0 } ^ { n } ( M u _ { \jmath } + N v _ { \jmath } ) + C _ { 3 } \sum _ { \jmath = 0 } ^ { n } \| d _ { \jmath } \| , } } \\ { \displaystyle { v _ { n } = \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } ( L u _ { \jmath } + \ell v _ { \jmath } ) + C _ { 4 } \frac { \varepsilon } { h } \sum _ { \jmath = 0 } ^ { n } \kappa ^ { n - \jmath } \| e _ { \jmath } \| . } } \end{array}
$$

An induction argument shows that

$$
\| \Delta y _ { n } \| \leq u _ { n } , \qquad \| \Delta z _ { n } \| \leq v _ { n }
$$

provided $\ell < 1$ and $h \leq h _ { 0 }$ . We then rewrite (2.17) as

$$
\begin{array} { l l } { { u _ { n } = u _ { n - 1 } + h M u _ { n } + h N v _ { n } + C _ { 3 } \| d _ { n } \| , \qquad u _ { - 1 } = 0 , } } \\ { { \displaystyle v _ { n } = \kappa v _ { n - 1 } + L u _ { n } + \ell v _ { n } + C _ { 4 } \frac { \varepsilon } { h } \| e _ { n } \| , \qquad v _ { - 1 } = 0 . } } \end{array}
$$

Solving for $u _ { n } , v _ { n }$ we get (with $\varrho = \kappa / ( 1 - \ell ) )$

$$
\left( \begin{array} { c } { { u _ { n } } } \\ { { v _ { n } } } \end{array} \right) = A ( h ) \left( \begin{array} { c } { { u _ { n - 1 } } } \\ { { v _ { n - 1 } } } \end{array} \right) + \left( \begin{array} { c } { { \widehat { d } _ { n } } } \\ { { \widehat { e } _ { n } } } \end{array} \right) , \qquad A ( h ) = \left( \begin{array} { c c } { { 1 + { \mathcal O } ( h ) } } & { { { \mathcal O } ( h ) } } \\ { { { \mathcal O } ( 1 ) } } & { { \varrho + { \mathcal O } ( h ) } } \end{array} \right)
$$

where

$$
| \widehat { d } _ { n } | \leq C _ { 5 } \big ( \| d _ { n } \| + \varepsilon \| e _ { n } \| \big ) , \qquad | \widehat { e } _ { n } | \leq C _ { 6 } \big ( \| d _ { n } \| + \frac \varepsilon h \| e _ { n } \| \big ) .
$$

Inserting (2.18) repeatedly we obtain

$$
\left( \begin{array} { l } { u _ { n } } \\ { v _ { n } } \end{array} \right) = \sum _ { j = 0 } ^ { n } A ( h ) ^ { n - j } \left( \begin{array} { l } { \widehat { d } _ { j } } \\ { \widehat { e } _ { j } } \end{array} \right) .
$$

If $\ell$ is small enough so that $\varrho = \kappa / ( 1 - \ell ) < 1$ and if $h \leq h _ { 0 }$ , then the eigenvalues of $A ( h )$ are distinct and $A ( h )$ can be diagonalized as

$$
A ( h ) = T ^ { - 1 } ( h ) \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { 0 } \\ { 0 } & { \varrho + \mathcal { O } ( h ) } \end{array} \right) T ( h ) , \quad T ( h ) = \left( \begin{array} { c c } { 1 } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { 1 } \end{array} \right) .
$$

Inserted into (2.20) this yields

$$
u _ { n } + v _ { n } \leq C o n s t . \left( \sum _ { \jmath = 1 } ^ { n } \widehat { d } _ { \jmath } + \sum _ { \jmath = 1 } ^ { n } ( h + \varrho ^ { n - \jmath } ) \widehat { e } _ { \jmath } \right) .
$$

Since $d _ { 0 } , \ldots , d _ { k - 1 }$ are linear combinations of the values $\Delta y _ { 0 } , \ldots , \Delta y _ { k - 1 }$ ，and $e _ { 0 } , \ldots , e _ { k - 1 }$ are linear combinations of the $\Delta z _ { \jmath }$ and $\begin{array} { r } { \frac { h } { \varepsilon } \Delta z _ { \jmath } } \end{array}$ , the statement of the theorem follows from (2.19） and (2.7). Because of our assumption on $\ell$ (that $\varrho = \kappa / ( 1 - \ell ) < 1 )$ ）we have proved the theorem for sufficiently small (but $\varepsilon \cdot$ independent） intervals. Compact intervals $\left\{ x _ { 0 } , { \overline { { x } } } \right\}$ can be covered by repeated application of the above estimates.

c) It still remains to prove (2.15). More generally, we shall show that

$$
\frac { h } { \varepsilon } \left\| r _ { \ j } \left( \frac { h } { \varepsilon } g _ { z } ( y , z ) \right) \right\| \leq C \kappa ^ { \ j } \qquad \mathrm { w i t h } \quad 0 < \kappa < 1
$$

holds uniformly in a compact neighbourhood of the solution. This is necessary, if the above estimates are applied to several subintervals.In order to prove (2.21) we remember that $\begin{array} { r } { r _ { \mathcal { I } } \left( \frac { h } { \varepsilon } J \right) } \end{array}$ is defined by (2.14). If we are able to show that

$$
\bigg \vert \bigg \vert \bigg ( \frac { \varepsilon } { h } \delta ( \zeta ) I - g _ { z } ( y , z ) \bigg ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - k } ) } \bigg \vert \bigg \vert \leq C \qquad \mathrm { f o r } \ \quad \vert \zeta \vert \leq 1 / \kappa
$$

then the estimate (2.21) follows immediately from Cauchy's integral formula

$$
\frac { h } { \varepsilon } r _ { j } \Big ( \frac { h } { \varepsilon } J \Big ) = \frac { 1 } { 2 \pi i } \int _ { | \zeta | = 1 / \kappa } \Big ( \frac { \varepsilon } { h } \delta ( \zeta ) I - J \Big ) ^ { - 1 } \frac { \zeta ^ { - k } } { \sigma ( \zeta ^ { - 1 } ) } \cdot \zeta ^ { - j - 1 } d \zeta .
$$

By definition of the stability region $S$ of a multistep method, the value $\delta ( \zeta )$ lies outside of $S$ whenever $| \zeta | < 1$ . Recall that the method is $A ( \alpha )$ -stable and strictly stable at infinity,and the differential equation satisfies (2.5). Therefore the set of eigenvalues of $g _ { z } ( y , z )$ (with $( y , z )$ varying in a compact neighbourhood of the solution) is well separated from $\{ \gamma \delta ( \zeta ) : \gamma \leq 1 , | \zeta | \leq 1 \}$ . It is even separated from $\{ \gamma \delta ( \zeta ) ; \gamma \leq 1 , | \zeta | \leq 1 / \kappa \}$ with some $\kappa < 1$ . Together with Exercise 2 of Sect.V.7 this proves (2.22). □

# Exercises

1. (Lubich 1991). Prove that for the BDF-schemes the estimate of Theorem 2.2 (for $n \geq k )$ is valid with $\left( h + \varrho ^ { \pi } \right)$ replaced by $\varepsilon ( 1 + \varrho ^ { n } / \hbar )$ in the factor multiplying the $z$ -component of the errors in the starting values. Hint. Give a direct proof for $n \in \{ k , \ldots , 2 k - 1 \}$ ; then apply Theorem 2.2 to shifted starting values.

# VI.3Epsilon Expansions for Exact and RK Solutions

In the preceding section we have proved convergence of multistep methods for singular perturbation problems. The same techniques do not yield optimal estimates for Runge-Kutta methods. We therefore investigate more thoroughly the structure of the solutions of singular perturbation problems. A first systematic study of the qualitative aspects of such problems is due to Tikhonov (1952). Asymptotic expansions were then analyzed by Vasil'eva (1963). Classical books on this subject are Wasow (1965), O'Malley (1974),and Tikhonov, Vasil'eva & Sveshnikov(1985).

# Expansion of the Smooth Solution

Tihonov's theorem is only the first step ... The actual approximate solution of such problems in series form is still a difficult question. It has been analyzed in a series of papers by Vasil'eva (W. Wasow 1965)

We consider the singular perturbation problem

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { \varepsilon z ^ { \prime } = g ( y , z ) , \qquad 0 < \varepsilon \ll 1 } } \end{array}
$$

where $f$ and $g$ are sufficiently differentiable. The functions $f , g$ and the initial values $y ( 0 )$ ， $z ( 0 )$ may depend smoothly on $\varepsilon$ . For simplicity of notation we suppress this dependence. The corresponding equation for $\varepsilon \approx 0$ ，

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) , } \end{array}
$$

is the reduced problem. In order to guarantee the solvability of (3.2),we assume that $g _ { z } ( y , z )$ is invertible (in a neighbourhood of the solution of (3.2).

We are mainly interested in smooth solutions of (3.1), which are of the form

$$
\begin{array} { l } { { y ( x ) = y _ { 0 } ( x ) + \varepsilon y _ { 1 } ( x ) + \varepsilon ^ { 2 } y _ { 2 } ( x ) + \dots . } } \\ { { z ( x ) = z _ { 0 } ( x ) + \varepsilon z _ { 1 } ( x ) + \varepsilon ^ { 2 } z _ { 2 } ( x ) + \dots . } } \end{array}
$$

Inserting (3.3) into (3.1) and collecting equal powers of $\varepsilon$ yields

$$
\left. \begin{array} { r l } { \varepsilon ^ { 0 } : } & { { } \quad y _ { 0 } ^ { \prime } = f \big ( y _ { 0 } , z _ { 0 } \big ) } \\ { 0 = g \big ( y _ { 0 } , z _ { 0 } \big ) } \end{array} \right\}
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_27, $©$ Springer-Verlag Berlin Heidelberg 2010

$$
\begin{array} { r l r } {  { \varepsilon ^ { 1 } : \quad } } & { y _ { 1 } ^ { \prime } = f _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { 1 } + f _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { 1 } \quad } & { \mathrm { ( } } \\ & { } & { z _ { 0 } ^ { \prime } = g _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { 1 } + g _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { 1 } \quad \} } \\ & { } & { \quad \cdot \cdot \cdot } \\ & { \quad } & { y _ { \nu } ^ { \prime } = f _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { \nu } + f _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { \nu } + \varphi _ { \nu } \big ( y _ { 0 } , z _ { 0 } , \ldots , y _ { \nu - 1 } , z _ { \nu - 1 } \big ) \quad } \\ & { } & { z _ { \nu - 1 } ^ { \prime } = g _ { y } \big ( y _ { 0 } , z _ { 0 } \big ) y _ { \nu } + g _ { z } \big ( y _ { 0 } , z _ { 0 } \big ) z _ { \nu } + \psi _ { \nu } \big ( y _ { 0 } , z _ { 0 } , \ldots , y _ { \nu - 1 } , z _ { \nu - 1 } \big ) \quad } \end{array}
$$

As expected, we see from (3.4a) that $y _ { 0 } ( x ) , \ z _ { 0 } ( x )$ is a solution of the reduced system. Since $g _ { z }$ is invertible, the second equation of (3.4b) can be solved for $z _ { 1 }$ .By inserting $z _ { 1 }$ into the upper relation of(3.4b) we obtain a linear differential equation for $y _ { 1 } ( x )$ . Hence, $y _ { 1 } ( x )$ and $z _ { 1 } ( x )$ are determined. Similarly, we get $y _ { 2 } ( x ) , z _ { 2 } ( x )$ from (3.4c), etc.

This construction of the coefficients of (3.3） shows that we can choose the initial values $y _ { \jmath } ( 0 )$ arbitrarily,but that there is no freedom in the choice of $z _ { \jmath } ( 0 )$ · Consequently, not every solution of (3.1) can be written in the form (3.3).

# Expansions with Boundary Layer Terms

To construct a uniform asymptotic expansion we must combine the Maclaurin expansion with another expansion of special form. The terms in this expansion are exponential functions that are appreciable inside the boundary layer,but negligibly small outside it. (A.B. Vasil'eva 1963)

Example 3.1. We consider the problem (IV.1.1), written in the form

$$
\varepsilon z ^ { \prime } = - z + \cos x .
$$

Its analytic solution

$$
\begin{array} { c } { { z ( x ) = ( 1 + \varepsilon ^ { 2 } ) ^ { - 1 } ( \cos x + \varepsilon \sin x ) + C e ^ { - x / \varepsilon } } } \\ { { { } } } \\ { { = \cos x + \varepsilon \sin x - \varepsilon ^ { 2 } \cos x - \varepsilon ^ { 3 } \sin x + \ldots + C e ^ { - x / \varepsilon } } } \end{array}
$$

is a superposition of a smooth solution of the form (3.3) and of a rapidly decaying function. This additional term (transient phase, boundary layer) compensates the missing freedom in the choice of the initial values $z _ { \jmath } \left( 0 \right)$

Motivated by this example, we seek solutions of the general problem (3.1) which are of the form

$$
\begin{array} { l } { { \displaystyle y ( x ) = \sum _ { j \ge 0 } \varepsilon ^ { j } y _ { j } ( x ) + \varepsilon \sum _ { j \ge 0 } \varepsilon ^ { j } \eta _ { j } ( x / \varepsilon ) } } \\ { { \displaystyle z ( x ) = \sum _ { j \ge 0 } \varepsilon ^ { j } z _ { j } ( x ) + \sum _ { j \ge 0 } \varepsilon ^ { j } \zeta _ { j } ( x / \varepsilon ) , } } \end{array}
$$

where $y _ { \jmath } ( x ) , z _ { \jmath } ( x )$ are determined by (3.4) and the $\varepsilon$ -independent functions $\eta _ { \jmath }$ $\zeta _ { j }$ are assumed to satisfy

$$
\| \eta _ { \ j } ( \xi ) \| \le e ^ { - \kappa \xi } , \qquad \| \zeta _ { \ j } ( \xi ) \| \le e ^ { - \kappa \xi }
$$

with some $\kappa > 0$ . Inserting (3.6) into (3.1) and using (3.4) we obtain formally

$$
\begin{array} { l } { { \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } ^ { \prime } \left( \frac { x } { \varepsilon } \right) = f \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) + \varepsilon \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } \left( \frac { x } { \varepsilon } \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) + \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } \left( \frac { x } { \varepsilon } \right) \right) } } \\ { { \displaystyle \qquad - f \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) \right) } } \\ { { \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } ^ { \prime } \left( \frac { x } { \varepsilon } \right) = g \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) + \varepsilon \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \eta _ { j } \left( \frac { x } { \varepsilon } \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) + \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } \zeta _ { j } \left( \frac { x } { \varepsilon } \right) \right) } } \\ { { \displaystyle \qquad - g \left( \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } y _ { j } \left( x \right) , \displaystyle \sum _ { j \geq 0 } \varepsilon ^ { 2 } z _ { j } \left( x \right) \right) } . } \end{array}
$$

We then replace $x$ by the stretched variable

$$
\xi = x / \varepsilon
$$

and compare like powers of $\varepsilon$ in (3.8). This gives for $\varepsilon ^ { 0 }$

$$
\begin{array} { r l } & { \eta _ { 0 } ^ { \prime } ( \xi ) = f { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) { \big ) } - f { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) { \big ) } } \\ & { \zeta _ { 0 } ^ { \prime } ( \xi ) = g { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) { \big ) } - g { \big ( } y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) { \big ) } . } \end{array}
$$

At this point it is necessary to introduce some stability assumption for (3.1) in order to obtain (3.7). We shall require that the logarithmic norm of $g _ { z }$ satisfy

$$
\mu \big ( g _ { z } ( y , z ) \big ) \leq - 1
$$

in an $\varepsilon$ -independent neighbourhood of the solution of (3.2) (any negative bound other than $- 1$ can be normalized by re-scaling $\varepsilon$ ).By Theorem I.10.6 Eqs. (3.10b) and (3.11) imply

$$
\begin{array} { r } { \| \zeta _ { 0 } ( \xi ) \| \le \| \zeta _ { 0 } ( 0 ) \| e ^ { - \xi } . } \end{array}
$$

Since $f ( y , z )$ satisfies locally a Lipschitz condition, the right-hand side of (3.10a), denoted by $\varphi ( \xi )$ , is bounded by $\| \varphi ( \xi ) \| \le L \| \zeta _ { 0 } ( 0 ) \| e ^ { - \xi }$ . Consequently, there is only one solution of (3.10a) which satisfies (3.7), namely

$$
\eta _ { 0 } ( \xi ) = \int _ { 0 } ^ { \xi } \varphi ( s ) d s - \int _ { 0 } ^ { \infty } \varphi ( s ) d s .
$$

A comparison of the powers of $\varepsilon ^ { 1 }$ in (3.8) yields

$$
\begin{array} { r l } & { \eta _ { 1 } ^ { \prime } ( \xi ) = f _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) + \eta _ { 0 } ( \xi ) \big ) } \\ & { \qquad + f _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) + \zeta _ { 1 } ( \xi ) \big ) } \\ & { \qquad - f _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) \big ) } \\ & { \qquad - f _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) \big ) } \\ & { \zeta _ { 1 } ^ { \prime } ( \xi ) = g _ { y } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) + \eta _ { 0 } ( \xi ) \big ) } \\ & { \qquad + g _ { z } \big ( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) + \zeta _ { 0 } ( \xi ) \big ) \big ( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) + \zeta _ { 1 } ( \xi ) \big ) } \end{array}
$$

$$
\begin{array} { r l } & { - g _ { y } \left( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \right) \left( y _ { 1 } ( 0 ) + \xi y _ { 0 } ^ { \prime } ( 0 ) \right) } \\ & { - g _ { z } \left( y _ { 0 } ( 0 ) , z _ { 0 } ( 0 ) \right) \left( z _ { 1 } ( 0 ) + \xi z _ { 0 } ^ { \prime } ( 0 ) \right) . } \end{array}
$$

Eq.(3.13b) is a linear differential equation for $\zeta _ { 1 } ( \xi )$ . Its defect, for $\zeta _ { 1 }$ replaced by 0, is bounded by $C e ^ { - \xi }$ . Therefore,an application of Theorem I.10.6 yields

$$
\begin{array} { r } { \| \zeta _ { 1 } ( \xi ) \| \le e ^ { - \xi } \big ( \| \zeta _ { 1 } ( 0 ) \| + C \xi \big ) , } \end{array}
$$

which implies (3.7) for any $\kappa < 1$ . The right-hand side of (3.13a) is then bounded by $C _ { 1 } e ^ { - \kappa \xi }$ ． As in (3.12) we obtain a unique solution to (3.13a),which satisfies (3.7). This procedure can be continued to construct all further $\eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ . At each step, the value of $\kappa$ in (3.7) may become smaller. This is no serious difficulty, because we are only interested in a finite part of the series (3.6).

We point out that for the construction of $\eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ we can choose $\zeta _ { \mathcal { I } } ( 0 )$ arbitrarily, but that there is no freedom in the choice of $\mathfrak { \eta } _ { \jmath } ( 0 )$ ·

As a consequence,for an arbitrary initial value for (3.1) with expansion

$$
\begin{array} { l } { { y ( 0 ) = y _ { 0 } ^ { 0 } + \varepsilon y _ { 1 } ^ { 0 } + \varepsilon ^ { 2 } y _ { 2 } ^ { 0 } + \dots . } } \\ { { z ( 0 ) = z _ { 0 } ^ { 0 } + \varepsilon z _ { 1 } ^ { 0 } + \varepsilon ^ { 2 } z _ { 2 } ^ { 0 } + \dots . } } \end{array}
$$

the coeficients of the series (3.6) can be constructed as follows: put $x = 0$ in (3.6) to obtain the necessary relations

$$
y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 } , \qquad y _ { \ j } ( 0 ) + \eta _ { \ j - 1 } ( 0 ) = y _ { \ j } ^ { 0 } , \qquad z _ { \ j } ( 0 ) + \zeta _ { \ j } ( 0 ) = z _ { \ j } ^ { 0 } .
$$

This initial value $y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 }$ determines $z _ { 0 } ( 0 )$ by (3.4a), $\zeta _ { 0 } ( 0 )$ is then given by (3.15), $\eta _ { 0 } ( 0 )$ by (3.12), $y _ { 1 } ( 0 )$ by (3.15), $z _ { 1 } ( 0 )$ by (3.4b), $\zeta _ { 1 } ( 0 )$ by (3.15), $\eta _ { 1 } ( 0 )$ by (3.13a) and (3.7), $y _ { 2 } ( 0 )$ by (3.15), etc.

# Estimation of the Remainder

The following result gives a rigorous estimate of the remainder in (3.6), when only a truncated series is considered.

Theorem 3.2. Consider the initial value problem (3.1), (3.14), and suppose that (3.11) holds in an $\varepsilon$ -independent neighbourhood of the solution $y _ { 0 } ( x )$ ， $z _ { 0 } ( x )$ $[ 0 \leq$ $x \leq \overline { { x } } )$ of the reduced problem $( y _ { 0 } ( 0 ) = y _ { 0 } ^ { 0 } )$ .If $( y _ { 0 } ^ { 0 } , z _ { 0 } ^ { 0 } )$ lies in this neighbourhood, then the problem (3.1),(3.14) has $a$ unique solution for $\varepsilon$ sufficiently small and for $0 \leq x \leq \overline { { x } }$ ， which is of the form

$$
\begin{array} { l } { { \displaystyle y ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } y _ { j } ( x ) + \varepsilon \sum _ { j = 0 } ^ { N - 1 } \varepsilon ^ { j } \eta _ { j } ( x / \varepsilon ) + \mathcal { O } ( \varepsilon ^ { N + 1 } ) } } \\ { { \displaystyle z ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } z _ { j } ( x ) + \sum _ { j = 0 } ^ { N } \varepsilon ^ { j } \zeta _ { j } ( x / \varepsilon ) + \mathcal { O } ( \varepsilon ^ { N + 1 } ) . } } \end{array}
$$

The coefficients $y _ { 3 } ( x ) , z _ { 3 } ( x ) , \eta _ { 3 } ( \xi ) , \zeta _ { 3 } ( \xi )$ are given by (3.4), (3.10), (3.13), and satisfy (3.7).

Proof. We denote the truncated series by

$$
\begin{array} { l } { { \displaystyle { \widehat { y } } ( x ) = \sum _ { j = 0 } ^ { N } \varepsilon ^ { \jmath } y _ { \jmath } ( x ) + \varepsilon \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } \eta _ { j } ( x / \varepsilon ) } } \\ { { \displaystyle { \widehat { z } } ( x ) = \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } z _ { \jmath } ( x ) + \sum _ { \jmath = 0 } ^ { N } \varepsilon ^ { \jmath } \zeta _ { \jmath } ( x / \varepsilon ) } . } \end{array}
$$

By our construction of $y _ { j } ( x ) , z _ { \jmath } ( x ) , \eta _ { \jmath } ( \xi ) , \zeta _ { \jmath } ( \xi )$ we have

$$
\begin{array} { c } { { \widehat { y } ^ { \prime } ( x ) = f \big ( \widehat { y } ( x ) , \widehat { z } ( x ) \big ) + { \mathcal O } ( { \varepsilon } ^ { N + 1 } ) } } \\ { { \varepsilon \widehat { z } ^ { \prime } ( x ) = g \big ( \widehat { y } ( x ) , \widehat { z } ( x ) \big ) + { \mathcal O } ( { \varepsilon } ^ { N + 1 } ) . } } \end{array}
$$

Subtracting (3.1) from (3.18) and exploiting Lipschitz conditions for $f$ and $g$ we obtain

$$
\begin{array} { r l } & { \quad D _ { + } \| \widehat { y } ( x ) - y ( x ) \| \leq L _ { 1 } \| \widehat { y } ( x ) - y ( x ) \| + L _ { 2 } \| \widehat { z } ( x ) - z ( x ) \| + C _ { 1 } \varepsilon ^ { N + 1 } } \\ & { \quad \varepsilon D _ { + } \| \widehat { z } ( x ) - z ( x ) \| \leq L _ { 3 } \| \widehat { y } ( x ) - y ( x ) \| - \| \widehat { z } ( x ) - z ( x ) \| + C _ { 2 } \varepsilon ^ { N + 1 } . } \end{array}
$$

Here, $D _ { + }$ denotes the Dini derivate introduced in Section I.1O. We have used $D _ { + } \| w ( x ) \| \leq \| w ^ { \prime } ( x ) \|$ (see Eq.(I.10.4)) and, for the second inequality of (3.19), Formula (I.10.17) together with (3.11).

In order to solve inequality (3.19) we replace $\leq { \mathfrak { b y } } =$ and so obtain

$$
\begin{array} { r l } { u ^ { \prime } = L _ { 1 } u + L _ { 2 } v + C _ { 1 } \varepsilon ^ { N + 1 } , \quad } & { u _ { 0 } = \| \widehat { y } ( 0 ) - y ( 0 ) \| = \mathcal { O } ( \varepsilon ^ { N + 1 } ) } \\ { \varepsilon v ^ { \prime } = L _ { 3 } u - v + C _ { 2 } \varepsilon ^ { N + 1 } , \quad } & { v _ { 0 } = \| \widehat { z } ( 0 ) - z ( 0 ) \| = \mathcal { O } ( \varepsilon ^ { N + 1 } ) . } \end{array}
$$

This system is quasimonotone,it thus follows from Exercise 7 (Sect.I.10) that

$$
\| { \widehat { y } } ( x ) - y ( x ) \| \leq u ( x ) , \qquad \| { \widehat { z } } ( x ) - z ( x ) \| \leq v ( x ) .
$$

Transforming (3.20) to diagonal form one easily finds its analytic solution and verifies that $u ( x ) = \mathcal { O } ( \varepsilon ^ { N + 1 } )$ ， $v ( x ) = \mathcal { O } ( \varepsilon ^ { N + 1 } )$ on compact intervals. Inserted into (3.21) this proves the statement. □

# Expansion of the Runge-Kutta Solution

After having understood the structure of the analytic solution of (3.1),we turn our attention to its numerical counterpart. We consider the Runge-Kutta method

$$
\left( { \begin{array} { l } { y _ { n + 1 } } \\ { z _ { n + 1 } } \end{array} } \right) = \left( { \begin{array} { l } { y _ { n } } \\ { z _ { n } } \end{array} } \right) + h \sum _ { \iota = 1 } ^ { \ s } b _ { \iota } \left( { \begin{array} { l } { k _ { n \iota } } \\ { \ell _ { n \iota } } \end{array} } \right)
$$

where

$$
\binom { k _ { n \imath } } { \varepsilon \ell _ { n \imath } } = \binom { f ( Y _ { n \imath } , Z _ { n \imath } ) } { g ( Y _ { n \imath } , Z _ { n \imath } ) }
$$

and the internal stages are given by

$$
{ \binom { Y _ { n \imath } } { Z _ { n \imath } } } = { \binom { y _ { n } } { z _ { n } } } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \left( { k _ { n \jmath } \atop \ell _ { n \jmath } } \right) .
$$

For arbitrary initial values,the solution possesses a transient phase (as described by Theorem 3.2),and the numerical method has anyway to take small step sizes of magnitude $\mathcal O ( \varepsilon )$ . We shall therefore focus on the situation where the transient phase is over and the method has reached the smooth solution within the given tolerance.We thus suppose that the initial values lie on the smooth solution (ie., that an expansion of the form (3.3) holds) and that the step size $h$ is large compared to $\varepsilon$ ．Our first goal is an $\varepsilon$ -expansion of the numerical solution. To this end, we formally expand all occuring quantities into powers of $\varepsilon$ with $\varepsilon$ -independent coefficients (see Hairer,Lubich & Roche 1988)

$$
\begin{array} { c } { { y _ { n } = y _ { n } ^ { 0 } + \varepsilon y _ { n } ^ { 1 } + \varepsilon ^ { 2 } y _ { n } ^ { 2 } + . . . } } \\ { { \nonumber Y _ { n \imath } = Y _ { n \imath } ^ { 0 } + \varepsilon Y _ { n \imath } ^ { 1 } + \varepsilon ^ { 2 } Y _ { n \imath } ^ { 2 } + . . . } } \\ { { \nonumber k _ { n i } = k _ { n \imath } ^ { 0 } + \varepsilon k _ { n i } ^ { 1 } + \varepsilon ^ { 2 } k _ { n \imath } ^ { 2 } + . . . } } \end{array}
$$

and similarly for $z _ { n } , Z _ { n } , \ell _ { n i }$ . Because of the linearity of the relations (3.22) and (3.24) we have

$$
\left( { y _ { n + 1 } ^ { \nu } \atop z _ { n + 1 } ^ { \nu } } \right) = \left( { y _ { n } ^ { \nu } \atop z _ { n } ^ { \nu } } \right) + h \sum _ { i = 1 } ^ { s } b _ { \imath } \left( { k _ { n \atop \ell _ { n } ^ { \nu } } ^ { \nu } } \right)
$$

and

$$
\binom { Y _ { n \iota } ^ { \nu } } { Z _ { n \iota } ^ { \nu } } = \binom { y _ { n } ^ { \nu } } { z _ { n } ^ { \nu } } + h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \binom { k _ { n j } ^ { \nu } } { \ell _ { n \jmath } ^ { \nu } } .
$$

Inserting (3.25b, c) into (3.23) and comparing equal powers of $\varepsilon$ we obtain

$$
\begin{array} { r l r } { \varepsilon ^ { 0 } : } & { k _ { n \tau } ^ { 0 } = f ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) \ \biggr \} } & { ( 3 . 2 8 \mathfrak { a } ) } \\ & { 0 = g ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) \ \biggr \} } & { ( 3 . 2 8 \mathfrak { a } ) } \\ & { k _ { n \tau } ^ { 1 } = f _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { 1 } + f _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n i } ^ { 1 } \ \biggr \} } & { ( 3 . 2 8 \mathfrak { b } ) } \\ { \varepsilon ^ { 1 } : } & { \ell _ { n \tau } ^ { 0 } = g _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n i } ^ { 1 } + g _ { z } ( Y _ { n i } ^ { 0 } , Z _ { n i } ^ { 0 } ) Z _ { n \tau } ^ { 1 } \ \biggr \} } \\ & { \cdot \cdot \cdot } & { \cdot \cdot } \\ & { k _ { n \tau } ^ { \nu } = f _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { \nu } + f _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n \tau } ^ { \nu } + \varphi _ { \nu } ( Y _ { n \tau } ^ { 0 } , Z _ { n i } ^ { 0 } , . . . , Y _ { n \tau } ^ { \nu - 1 } , Z _ { n \tau } ^ { \nu - 1 } ) \ \biggr \} } \\ { \varepsilon ^ { \nu } : } & { \ell _ { n \tau } ^ { \nu - 1 } = g _ { y } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Y _ { n \tau } ^ { \nu } + g _ { z } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } ) Z _ { n \tau } ^ { \nu } + \psi _ { \nu } ( Y _ { n \tau } ^ { 0 } , Z _ { n \tau } ^ { 0 } , . . . , Y _ { n \tau } ^ { \nu - 1 } , Z _ { n \tau } ^ { \nu - 1 } ) \ \biggr \} } \end{array}
$$

Since (3.23) has the same form as the differential equation (3.1),it is obvious that the formulas of (3.28) are exactly the same as those of (3.4). An interesting interpretation of this fact is the following:thecoeficients $y _ { n } ^ { 0 } , z _ { n } ^ { 0 } , y _ { n } ^ { 1 } , z _ { n } ^ { 1 } , . .$ repre-sent the numerical solution of the Runge-Kutta method applied to the differentialalgebraic system (3.4) ( $\varepsilon$ -embedding method of Sect. VI.1). This can be expressed by the commutativity of the following diagram:

Subtracting (3.25a) from(3.3) we get formally

$$
\begin{array} { l } { { \displaystyle y _ { n } - y ( x _ { n } ) = \sum _ { \nu \geq 0 } \varepsilon ^ { \nu } \left( y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) \right) } } \\ { { \displaystyle z _ { n } - z ( x _ { n } ) = \sum _ { \nu \geq 0 } \varepsilon ^ { \nu } \left( z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) \right) } . } \end{array}
$$

In order to study this error we first investigate the differences $y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) , z _ { n } ^ { \nu } -$ $z _ { \nu } ( x _ { n } )$ (next subsection). A rigorous estimate of the remainder in (3.29) will then follow. The presentation follows that of Hairer,Lubich & Roche (1988).

# Convergence of RK-Methods for Diferential-Algebraic Systems

The first differences $y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } )$ ， $z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } )$ in the expansions of (3.29) are just the global errors of the Runge-Kutta method applied to the reduced system (3.4a). By assumption (3.11) this system is of index 1. Therefore,the following result is an immediate consequence of Theorem 1.1.

Theorem 3.3. Consider a Runge-Kutta method of (classical) order $p$ , with invertible coefficient matrix $( { a } _ { \iota _ { \mathcal { I } } } )$ . Suppose that Problem $( 3 . 4 a )$ satisfies (3.11) and that the initial values are consistent.

$a$ ) If the method is stiffly accurate (i.e.,， $a _ { s _ { 2 } } = b _ { \tau }$ for $\iota = 1 , \ldots , s )$ then the global error satisfies

$$
y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) , \qquad z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) .
$$

$^ { b ) }$ If the stability function satisfes $| R ( \infty ) | < 1$ ， and the stage order is $q$ $1 ( q < p )$ ， then

$$
y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \qquad z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) = { \mathcal { O } } ( h ^ { q + 1 } ) .
$$

In both cases the estimates hold uniformly for $n h \le C o n s t$

Estimating the second differences $y _ { n } ^ { 1 } - y _ { 1 } ( x _ { n } )$ ， $z _ { n } ^ { 1 } - z _ { 1 } ( x _ { n } )$ is not as simple, because the enlarged system (3.4a,b) with differential variables $y _ { 0 } , z _ { 0 } , y _ { 1 }$ and algebraic variable $z _ { 1 }$ ,is no longer of index 1. It is actually of index 2, as will become clear in Sect. VII.1 below (Exercise 5). In principle it is possible to consult the re-sults of Sect. VI.4 (Theorems VII.4.5 and VII.4.6). For the special system $_ { ( 3 . 4 a , b ) }$ ， however, a simpler proof is possible. It also extends more easily to the higher-index problems (3.4a-c).

Theorem 3.4 (Hairer, Lubich & Roche 1988). Consider a Runge-Kuta method of order $ { p }$ ， stage order $q$ $( q < p )$ ， such that $\left( { a _ { \iota } } _ { \jmath } \right)$ is invertible and the stability function satisfies $| R ( \infty ) | < 1$ .If $\left( 3 . l I \right)$ holds and if the initial values of the differentialalgebraic system $\left( 3 . 4 a \cdot c \right)$ are consistent, then the global error of method (3.26)- (3.28) satisfies for $1 \leq \iota / \leq \ q + 1$

$$
y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) = \mathcal { O } ( h ^ { q + 2 - \nu } ) , \qquad z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) = \mathcal { O } ( h ^ { q + 1 - \nu } ) .
$$

Proof. We denote the differences to the exact solution values by

$$
\begin{array} { r l r } & { \Delta y _ { n } ^ { \nu } = y _ { n } ^ { \nu } - y _ { \nu } ( x _ { n } ) , } & { \Delta z _ { n } ^ { \nu } = z _ { n } ^ { \nu } - z _ { \nu } ( x _ { n } ) , } \\ & { \Delta Y _ { n \imath } ^ { \nu } = Y _ { n \imath } ^ { \nu } - y _ { \nu } ( x _ { n } + c _ { \imath } h ) , } & { \Delta Z _ { n \imath } ^ { \nu } = Z _ { n \imath } ^ { \nu } - z _ { \nu } ( x _ { n } + c _ { \imath } h ) , } \\ & { \Delta k _ { n \imath } ^ { \nu } = k _ { n \imath } ^ { \nu } - y _ { \nu } ^ { \prime } ( x _ { n } + c _ { \imath } h ) , } & { \Delta \ell _ { n \imath } ^ { \nu } = \ell _ { n \imath } ^ { \nu } - z _ { \nu } ^ { \prime } ( x _ { n } + c _ { \imath } h ) . } \end{array}
$$

Since the quadrature formula with nodes $c _ { \imath }$ and weights $b _ { \imath }$ is of order $ { p }$ , we have from (3.26)

$$
\left( \begin{array} { c } { \Delta y _ { n + 1 } ^ { \nu } } \\ { \Delta z _ { n + 1 } ^ { \nu } } \end{array} \right) = \left( \begin{array} { c } { \Delta y _ { n } ^ { \nu } } \\ { \Delta z _ { n } ^ { \nu } } \end{array} \right) + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \left( \begin{array} { c } { \Delta k _ { n i } ^ { \nu } } \\ { \Delta \ell _ { n i } ^ { \nu } } \end{array} \right) + \mathcal { O } ( h ^ { p + 1 } ) .
$$

Similarly, the definition of the stage order implies

$$
\left( \begin{array} { c } { \Delta Y _ { n } ^ { \nu } } \\ { \Delta Z _ { n \imath } ^ { \nu } } \end{array} \right) = \left( \begin{array} { c } { \Delta y _ { n } ^ { \nu } } \\ { \Delta z _ { n \imath } ^ { \nu } } \end{array} \right) + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \left( \begin{array} { c } { \Delta k _ { n \jmath } ^ { \nu } } \\ { \Delta \ell _ { n \jmath } ^ { \nu } } \end{array} \right) + \mathcal { O } ( h ^ { q + 1 } ) .
$$

It follows from Theorem 3.3 (see also the proof of Theorem 1.1) that

$$
\begin{array} { r l r l r l } & { \Delta y _ { n } ^ { 0 } = \mathcal { O } ( h ^ { p } ) , } & & { \Delta Y _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta k _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) } \\ & { \Delta z _ { n } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta Z _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q + 1 } ) , } & & { \Delta \ell _ { n \ i } ^ { 0 } = \mathcal { O } ( h ^ { q } ) . } \end{array}
$$

a) We frst consider the case $\imath / = 1$ Replacing n (3.28b) $Y _ { n i } ^ { ( 0 ) }$ ， $Z _ { n \uparrow } ^ { ( \ l ) }$ by $y _ { 0 } ( x _ { n } +$ $c _ { i } h ) + \Delta Y _ { n i } ^ { 0 }$ ， $z _ { 0 } ( x _ { n } + c _ { \imath } h ) + \Delta Z _ { n \imath } ^ { 0 }$ andsubtractingEquation (3.4b)ateposition $x = x _ { n } + c _ { \imath } \hbar$ ,we obtain with the help of (3.35)

$$
\begin{array} { r l } & { \Delta k _ { n \imath } ^ { 1 } = f _ { y } ( x _ { n } + c _ { i } h ) \Delta Y _ { n \imath } ^ { 1 } + f _ { z } ( x _ { n } + c _ { \imath } h ) \Delta Z _ { n \imath } ^ { 1 } } \\ & { \qquad \quad + \mathcal { O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta Y _ { n \imath } ^ { 1 } \| + h ^ { q + 1 } \| \Delta Z _ { n \imath } ^ { 1 } \| ) } \\ & { \Delta \ell _ { n \imath } ^ { 0 } = g _ { y } ( x _ { n } + c _ { \imath } h ) \Delta Y _ { n \imath } ^ { 1 } + g _ { z } ( x _ { n } + c _ { \imath } h ) \Delta Z _ { n \imath } ^ { 1 } } \\ & { \qquad \quad + \mathcal { O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta Y _ { n \imath } ^ { 1 } \| + h ^ { q + 1 } \| \Delta Z _ { n \imath } ^ { 1 } \| ) . } \end{array}
$$

Here we have used the abbreviations $f _ { y } ( x ) = f _ { y } ( y _ { 0 } ( x ) , z _ { 0 } ( x ) )$ ， etc. Computing $\Delta Z _ { n i } ^ { 1 }$ from the second relation of (3.36) and inserting it into the first one yields

$$
\begin{array} { r l } & { \Delta k _ { n \ i } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + c _ { i } h ) \Delta \ell _ { n \ i } ^ { 0 } } \\ & { \qquad = ( f _ { y } - f _ { z } g _ { z } ^ { - 1 } g _ { y } ) ( x _ { n } + c _ { i } h ) \Delta \boldsymbol { \Upsilon } _ { n \ i } ^ { - 1 } + { \mathcal O } ( h ^ { q + 1 } + h ^ { q + 1 } \| \Delta \boldsymbol { \Upsilon } _ { n \ i } ^ { \prime 1 } \| ) . } \end{array}
$$

Using (3.34) we can eliminate $\Delta Y _ { n \imath } ^ { 1 }$ and obtain (with (3.35))

$$
\Delta k _ { n \ i } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + c _ { \ i } h ) \Delta \ell _ { n \ i } ^ { 0 } = \mathcal { O } ( \| \Delta y _ { n } ^ { 1 } \| ) + \mathcal { O } ( h ^ { q + 1 } ) .
$$

Since $\Delta \ell _ { n \imath } ^ { 0 }$ is of size $\mathcal { O } ( h ^ { q } )$ ， we only have $\Delta k _ { n \imath } ^ { 1 } = \mathcal { O } ( \vert \vert \Delta y _ { n } ^ { 1 } \vert \vert ) + \mathcal { O } ( h ^ { q } )$ ，and a direct estimation of $\Delta y _ { n } ^ { 1 }$ in (3.33） would lead to $\Delta y _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ ,which is not optimal. We therefore introduce the new variable

$$
\Delta u _ { n } ^ { 1 } = \Delta y _ { n } ^ { 1 } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \Delta z _ { n } ^ { 0 } .
$$

From (3.33) we get

$$
\begin{array} { l } { \displaystyle \Delta u _ { n + 1 } ^ { 1 } = \Delta u _ { n } ^ { 1 } + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } \big ( \Delta k _ { n } ^ { 1 } - \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } ) \Delta \ell _ { n a } ^ { 0 } \big ) } \\ { \displaystyle - \left( \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } + h ) - \big ( f _ { z } g _ { z } ^ { - 1 } \big ) ( x _ { n } ) \right) \Delta z _ { n + 1 } ^ { 0 } + \mathcal { O } \big ( h ^ { p + 1 } \big ) . } \end{array}
$$

The estimates (3.35), (3.37)and the fact that $\Delta y _ { n } ^ { 1 } = \Delta u _ { n } ^ { 1 } + \mathcal { O } ( h ^ { q + 1 } )$ imply that

$$
\begin{array} { r } { \| \Delta u _ { n + 1 } ^ { 1 } \| \leq ( 1 + C h ) \| \Delta u _ { n } ^ { 1 } \| + \mathcal { O } ( h ^ { q + 2 } ) . } \end{array}
$$

Standard techniques now show that $\Delta u _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q + 1 } )$ for $n h \le C o n s t$ (observe that the initial values are assumed to be consistent, i.e., $\Delta u _ { 0 } ^ { 1 } = 0 .$ ),so that by (3.38) and (3.35) also $\Delta y _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q + 1 } )$ . This implies $\Delta k _ { n \ i } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ by (3.37) and $\Delta Y _ { n \ i } ^ { 1 } =$ $\mathcal { O } ( h ^ { q + 1 } )$ by (3.34). The second relation of (3.36) then proves that $\Delta Z _ { n \imath } ^ { 1 } = \mathcal { O } ( \bar { h ^ { q } } )$ . In order to estimate $\Delta z _ { n } ^ { 1 }$ ，we compute $\Delta \ell _ { n \imath } ^ { 1 }$ from (3.34) and insert it into (3.33). Using $\Delta Z _ { n \imath } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ this gives

$$
\Delta z _ { n + 1 } ^ { 1 } = ( 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } ) \Delta z _ { n } ^ { 1 } + { \cal O } ( h ^ { q } ) ,
$$

and it follows from $\vert 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 } \vert = \vert R ( \infty ) \vert < 1$ that $\Delta z _ { n } ^ { 1 } = \mathcal { O } ( h ^ { q } )$ . We have thus proved the case $\nu \simeq 1$

b) The proof for general $\nu$ is by induction.We shall show that

$$
\begin{array} { r l } { \Delta y _ { n } ^ { \nu } = \mathcal { O } ( h ^ { q + 2 - \nu } ) , \quad } & { \Delta Y _ { n \ i } ^ { \nu } = \mathcal { O } \big ( h ^ { q + 2 - \nu } \big ) } \\ { \Delta z _ { n \ i } ^ { \nu } = \mathcal { O } ( h ^ { q + 1 - \nu } ) , \quad } & { \Delta Z _ { n \ i } ^ { \nu } = \mathcal { O } \big ( h ^ { q + 1 - \nu } \big ) } \end{array}
$$

holds for $\nu = 1 , \ldots , q + 1$ . The main difference to the case $\nu = 1$ consists in the additional inhomogeneities $\varphi _ { \nu }$ and $\psi _ { \nu }$ in (3.4c). Using their Lipschitz continuity one obtains an aditional term of size $\mathcal { O } ( h ^ { q + 2 - \nu } )$ in (3.36). Otherwise the proof is identical to that for $\nu = 1$ □

We next study the existence and local uniqueness of the solution of the Runge-Kutta method (3.22)-(3.24). Further, we investigate the influence of perturbations in (3.24) to the numerical solution. This will be important for the estimation of the remainder in the expansion (3.29).

# Existence and Uniqueness of the Runge-Kutta Solution

For $h$ small compared to $\varepsilon$ , the existence of a unique numerical solution of (3.23), (3.24) follows from standard fixed point iteration (e.g., Theorem II.7.2). For the (more interesting) case where the step size $h$ is large compared to $\varepsilon$ ,we suppose that $( y _ { n } , z _ { n } )$ are known,denote it by $( \eta , \zeta )$ ，and prove the cxistence of $\left( y _ { n + 1 } , z _ { n + 1 } \right)$ as follows:

Theorem 3.5 (Hairer,Lubich & Roche 1988)． Assume that $y ( \eta , \zeta ) = \mathcal { O } ( h )$ ， $\mu ( g _ { z } ( \eta , \zeta ) ) \leq - 1$ and that the eigenvalues of the Runge-Kuta matrix $\left( \boldsymbol { a } _ { i j } \right)$ have positive real part. Then, the nonlinear system

$$
\left( { \begin{array} { l } { \displaystyle Y _ { \imath } - \eta } \\ { \varepsilon ( Z _ { \imath } - \zeta ) } \end{array} } \right) = h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \left( { \begin{array} { l } { f ( Y _ { \jmath } , Z _ { \jmath } ) } \\ { g ( Y _ { \jmath } , Z _ { \jmath } ) } \end{array} } \right)
$$

possesses a locally unique solution for $h \leq h _ { 0 }$ ，where $h _ { 0 }$ is sufficiently small but independent of $\xi$ . This solution satisfies

$$
Y _ { \imath } - \eta = \mathcal { O } ( h ) , \qquad Z _ { \imath } - \zeta = \mathcal { O } ( h ) .
$$

Proof. We apply Newton's method to the nonlinear system (3.43), whose second equation is divided by $l _ { l }$ . The existence and uniqueness statement can then be deduced from the theorem of Newton-Kantorovich (Kantorovich & Akilov 1959, Ortega &Rheinboldt 1970)asfollows:forthestarting valuesY( =n， $Z _ { 1 } ^ { ( 0 ) } = 5$ the Jacobian of the system is of the form

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { ( \varepsilon / h ) I - A \otimes g _ { z } ( \eta , \zeta ) } \end{array} \right) .
$$

Since $\mu ( g _ { z } ( \eta , \zeta ) ) \leq - 1$ it follows from the matrix-valued theorem of von Neumann (Theorem V.7.8) that

$$
\big \| \big ( \kappa I - A \otimes g _ { z } ( \eta , \zeta ) \big ) ^ { - 1 } \big \| \leq \operatorname* { m a x } _ { \mathrm { R e } \mu \leq - 1 } \| ( \kappa I - \mu A ) ^ { - 1 } \| .
$$

The right-hand side of (3.46) is bounded by a constant independent of $r _ { i } \geq 0$ ,bccause the eigenvalues of $A$ are assumed to have positive real part. Consequently, also the inverse of (3.45) is uniformly bounded for $\varepsilon > 0$ and $l _ { l } \le h _ { 0 }$ . This together with $g \left( \uparrow \jmath , \zeta \right) = \mathcal { O } \left( h \right)$ implies that the first increment (of Newton's method) is of size $\mathcal { O } ( h )$ .Hence, for sufficiently small $h$ , the Ncwton-Kantorovich assumptions are fulfilled. □

# Influence of Perturbations

For the perturbed Runge-Kutta method

$$
\binom { \widehat { Y } _ { \scriptscriptstyle 2 } - \widehat { \eta } } { \varepsilon ( \widehat { Z } _ { \scriptscriptstyle 1 } - \widehat { \zeta } ) } = h \sum _ { \scriptscriptstyle 2 = 1 } ^ { s } a _ { \scriptscriptstyle 1 \jmath } \left( { f ( \widehat { Y } _ { \scriptscriptstyle \jmath } , \widehat { Z } _ { \scriptscriptstyle \jmath } ) } \right) + h \left( { \delta _ { \scriptscriptstyle \imath } } \right)
$$

we have the following result.

Theorem 3.6 (Hairer, Lubich & Roche 1988). Let $Y _ { \imath } , Z _ { \imath }$ be given by (3.43) and consider perturbed values ${ \widehat { Y } } _ { \imath } , { \widehat { Z } } _ { \imath }$ satisfying (3.47). In addition to the assumptions of Theorem 3.5 suppose that $\widehat { \eta } - \eta = \mathcal { O } ( h )$ ， $\widehat { \zeta } - \zeta = \mathcal { O } ( h )$ ， $\delta _ { \mathfrak { \imath } } = \mathcal { O } ( { \mathfrak { 1 } } )$ ,and $\theta _ { \imath } =$ $\mathcal O ( h )$ . Then we have for $h \leq h _ { 0 }$

$$
\begin{array} { r l } & { \| \widehat { Y } _ { \iota } - Y _ { \iota } \| \leq C ( \| \widehat { \eta } - \eta \| + \varepsilon \| \widehat { \zeta } - \zeta \| ) + h C ( \| \delta \| + \| \theta \| ) } \\ & { \| \widehat { Z } _ { \iota } - Z _ { \iota } \| \leq C ( \| \widehat { \eta } - \eta \| + \frac { \varepsilon } { h } \| \widehat { \zeta } - \zeta \| ) + C ( h \| \delta \| + \| \theta \| ) . } \end{array}
$$

Here $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { s } ) ^ { T }$ and $\boldsymbol { \theta } = ( \theta _ { 1 } , \ldots , \theta _ { s } ) ^ { T }$ ·

Proof. The essential idea is to consider the homotopy

$$
\left( { { Y } _ { \iota } } - \eta \atop \varepsilon ( { \boldsymbol { Z } _ { i } } - \zeta ) \right) - h \sum _ { \jmath = 1 } ^ { s } { { a } _ { \iota _ { \boldsymbol { \jmath } } } } \left( { { f } ( { \boldsymbol { Y } } _ { \boldsymbol { \jmath } } , { \boldsymbol { Z } } _ { \boldsymbol { \jmath } } ) } \right) = \tau \left( \begin{array} { c } { \widehat { \eta } - \eta + h { \delta } _ { \iota } } \\ { \varepsilon ( \widehat { \zeta } - \zeta ) + h { \theta } _ { \iota } } \end{array} \right)
$$

which relates the system (3.43) for $\tau = 0$ to the perturbed system (3.47) for $\tau \approx 1$ . The solutions $Y _ { \imath }$ and $Z _ { \imath }$ of (3.49) are functions of $\tau$ . If we differentiate (3.49) with respect to $\tau$ and divide its second formula by $h$ ，we obtain the differential equation

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { M ( \varepsilon / h , Y , Z ) } \end{array} \right) \left( \begin{array} { c } { \dot { Y } } \\ { \dot { Z } } \end{array} \right) = \left( \begin{array} { c } { \mathbb { 1 } \cdot ( \widehat { \eta } - \eta ) + h \delta } \\ { ( \varepsilon / h ) \mathbb { 1 } \cdot ( \widehat { \zeta } - \zeta ) + \theta } \end{array} \right)
$$

where $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T } , Y = ( Y _ { 1 } , \ldots , Y _ { s } ) ^ { T } , Z = ( Z _ { 1 } , \ldots , Z _ { s } ) ^ { T }$ and

$$
M ( \kappa , Y , Z ) = \kappa I - A \otimes I \cdot \left( \begin{array} { c c c } { { g _ { z } ( Y _ { 1 } , Z _ { 1 } ) } } & { { } } & { { 0 } } \\ { { } } & { { \ddots } } & { { } } \\ { { 0 } } & { { } } & { { g _ { z } ( Y _ { s } , Z _ { s } ) } } \end{array} \right) .
$$

Whenever $\| Y _ { \imath } - \eta \| \leq d$ and $\| Z _ { \iota } - \zeta \| \leq d$ for all $i$ , we have

$$
M ( \kappa , Y , Z ) = \kappa I - A \otimes g _ { z } ( \eta , \zeta ) + { \mathcal O } ( d )
$$

and it follows from (3.46) that $M ^ { - 1 } ( \kappa , Y , Z )$ is uniformly bounded for $\kappa \geq 0$ ,if $d$ is sufficiently small. Hence,the inverse of the matrix in (3.50) satisfies

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { M ( \varepsilon / h , Y , Z ) } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { \mathcal { O } ( 1 ) } \end{array} \right)
$$

and the statement (3.48) follows from the fact that

$$
{ \widehat { Y } } - Y = \int _ { 0 } ^ { 1 } { \dot { Y } } ( \tau ) d \tau , \qquad { \widehat { Z } } - Z = \int _ { 0 } ^ { 1 } { \dot { Z } } ( \tau ) d \tau .
$$

Remark 3.7. If the Runge-Kutta matrix $A$ is only assumed to be invertible, the results of Theorems 3.5 and 3.6 still hold for $\varepsilon \leq \bar { K } \bar { h }$ ，where $\bar { \Lambda } ^ { \gamma }$ is any constant smaller than the modulus of the smallest eigenvalue of $A$ (i.e., $K ^ { \prime } < | \lambda _ { \operatorname* { m i n } } | )$ .In this situation, the right-hand side of (3.48) is also bounded,and the same conclusions hold.

# Estimation of the Remainder in the Numerical Solution

We are now in the position to estimate the remainder in (3.29). The result is the following.

Theorem 3.8 (Hairer, Lubich & Roche 1988). Consider the stiff problem (3.1), (3.11) with initial values $y ( 0 )$ ， $\approx ( 0 )$ admitting $a$ smooth solution. Apply the Runge-Kutta method (3.22)-(3.24) of classical order $p$ and stage order $q$ $( 1 \leq q < p )$ Assume that the method is $A$ -stable, that the stability function satisfies $| R ( \infty ) | < 1$ ， and that the eigenvalues of the coefficient matrix $A$ have positive real part. Then for any fixed constant $c > 0$ the global error satisfies for $\varepsilon \leq c h$ and $\nu \leq q + 1$

$$
\begin{array} { r l } & { y _ { n } - y ( x _ { n } ) = \Delta y _ { n } ^ { 0 } + \varepsilon \Delta y _ { n } ^ { 1 } + . . . + \varepsilon ^ { \nu } \Delta y _ { n } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { z _ { n } - z ( x _ { n } ) = \Delta z _ { n } ^ { 0 } + \varepsilon \Delta z _ { n } ^ { 1 } + . . . + \varepsilon ^ { \nu } \Delta z _ { n } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) . } \end{array}
$$

Here $\Delta y _ { n } ^ { 0 } = y _ { n } ^ { 0 } - y _ { 0 } ( x _ { n } ) , \ \Delta z _ { n } ^ { 0 } = z _ { n } ^ { 0 } - z _ { 0 } ( x _ { n } ) , . . .$ (see Formulu (3.32)) are the global errors of the method applied to the system (3.4). The estimates (3.53) hold uniformly for ${ \boldsymbol { h } } \leq h _ { 0 }$ and $r \ i h \le C o n s t$

Proof. By Theorem 3.4 it suffices to prove the result for $\nu = q + 1$ . We denote thc truncated series of (3.25) by

$$
\begin{array} { c } { { \widehat { y } _ { n } = y _ { n } ^ { 0 } + \varepsilon y _ { n } ^ { 1 } + \ldots + \varepsilon ^ { \nu } y _ { n } ^ { \prime \prime } } } \\ { { { } } } \\ { { { \widehat { Y } } _ { n \imath } = Y _ { n \imath } ^ { 0 } + \varepsilon Y _ { n \imath } ^ { - 1 } + \ldots + \varepsilon ^ { \nu } Y _ { n \imath } ^ { \nu } } } \\ { { { } } } \\ { { { \widehat { k } } _ { n \imath } = k _ { n \imath } ^ { 0 } + \varepsilon k _ { n \imath } ^ { 1 } + \ldots + \varepsilon ^ { \nu } k _ { n \imath } ^ { \nu } } } \end{array}
$$

and similarly ${ \widehat { z } } _ { n } , { \widehat { Z } } _ { n \imath } , { \widehat { \ell } } _ { n \imath }$ . Further we denote

$$
\Delta y _ { n } = { \widehat { y } } _ { n } - y _ { n } , \qquad \Delta Y _ { n \ i } = { \widehat { Y } } _ { n \ i } - Y _ { n \ i } , \qquad \Delta k _ { n \ i } = { \widehat { k } } _ { n \ i } - k _ { n i } , \dots
$$

Using (3.3) and Theorem 3.4 the statement (3.53) is then equivalent to

$$
\Delta y _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) , \qquad \Delta z _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

a) We first estimate the differences $\Delta Y _ { n i } , \Delta Z _ { n \imath }$ of the internal stages. For this we investigate the defect when (3.54) is inserted into (3.23). By our construction (3.28) it follows from (3.42) and $\nu = q + 1$ that

$$
\begin{array} { r l } & { \widehat { k } _ { n \iota } = f ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { \varepsilon \widehat { \ell } _ { n \iota } = g ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) + \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

From (3.42) and (3.27) we know that $\ell _ { n \ i } ^ { \nu } = \mathcal { O } ( h ^ { - 1 } )$ .Together with (3.27) this implies

$$
\left( \begin{array} { c } { \widehat { Y } _ { n \ i } - \widehat { y } _ { n } } \\ { \varepsilon ( \widehat { Z } _ { n \ i } - \widehat { z } _ { n } ) } \end{array} \right) = h \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } \left( \begin{array} { c } { f ( \widehat { Y } _ { n j } , \widehat { Z } _ { n \jmath } ) } \\ { g ( \widehat { Y } _ { n \jmath } , \widehat { Z } _ { n \jmath } ) } \end{array} \right) + \left( \begin{array} { c } { \mathcal { O } ( h \varepsilon ^ { \nu + 1 } ) } \\ { \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \end{array} \right) ,
$$

which is of the form (3.47). Application of Theorem 3.6 yields

$$
\begin{array} { r l } & { \| \Delta Y _ { n \imath } \| \leq C ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) } \\ & { \| \Delta Z _ { n \imath } \| \leq C ( \| \Delta y _ { n } \| + \displaystyle \frac { \varepsilon } { h } \| \Delta z _ { n } \| ) + \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) } \end{array}
$$

provided that $\Delta y _ { n }$ and $\Delta z _ { n }$ are of size ${ \mathcal { O } } ( h )$ . This will be justifed in part (c).

b) Our next aim is to prove the recursion

$$
\begin{array} { r } { \left( \left. \Delta y _ { n + 1 } \right. \right) \leq \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( \varepsilon ) } \\ { \mathcal { O } ( 1 ) } & { \alpha + \mathcal { O } ( \varepsilon ) } \end{array} \right) \left( \left. \Delta y _ { n } \right. \right) + \left( \mathcal { O } ( \varepsilon ^ { \nu + 1 } / h ) \right) } \end{array}
$$

where we assume again that $\Delta y _ { n }$ and $\Delta z _ { n }$ are of size $\mathcal O ( h )$ . The value $\alpha < 1$ will be given in Formula (3.63) below. The upper relation of (3.60) follows from

$$
\Delta y _ { n + 1 } = \Delta y _ { n } + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \Big ( f ( \widehat { Y } _ { n \iota } , \widehat { Z } _ { n \iota } ) - f ( Y _ { n \iota } , Z _ { n \iota } ) \Big ) + \mathscr { O } ( h \varepsilon ^ { \nu + 1 } )
$$

by the use of (3.59) and a Lipschitz condition for $f$ ·

For the verification of the second relation in (3.60) we subtract (3.57) from (3.23),and use (3.59) and (3.42) to obtain

$$
\varepsilon \Delta \ell _ { n \iota } = g _ { z } ( x _ { n } ) \Delta Z _ { n \iota } + { \mathcal O } ( \| \Delta Y _ { n \iota } \| + h \| \Delta Z _ { n \iota } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

Here we use the notation $g _ { z } ( x ) = g _ { z } ( y _ { 0 } ( x ) , z _ { 0 } ( x ) )$ Inserting $\Delta Z _ { n \imath } = \Delta z _ { n \imath } +$ $\boldsymbol { h } \sum \boldsymbol { a } _ { \iota \jmath } \Delta \ell _ { n \jmath }$ into this relation and using (3.59) again we obtain

$$
\varepsilon \Delta \ell _ { n \ i } - h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } g _ { \boldsymbol z } ( { \boldsymbol x } _ { n } ) \Delta \ell _ { n \jmath } = g _ { \boldsymbol z } ( { \boldsymbol x } _ { n } ) \Delta z _ { n } + { \mathcal O } ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) .
$$

We now solve for $h \Delta \ell _ { n \imath }$ and insert it into $\begin{array} { r } { \Delta z _ { n + 1 } = \Delta z _ { n } + h \sum b _ { \imath } \Delta \ell _ { n \imath } } \end{array}$ . Since the matrix $( \varepsilon / h ) I - A \otimes g _ { z } ( x _ { n } )$ has a bounded inverse by (3.46), this gives

$$
\Delta z _ { n + 1 } = R \Big ( \frac { h } { \varepsilon } g _ { z } ( x _ { n } ) \Big ) \Delta z _ { n } + { \mathcal O } ( \| \Delta y _ { n } \| + \varepsilon \| \Delta z _ { n } \| ) + { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) ,
$$

where $R ( \mu )$ is the stability function of the method. Because of (3.11) we can apply von Neumann $\mathbf { \dot { s } }$ theorem (Corollary IV.11.4) to estimate

$$
\left\| R { \Big ( } { \frac { h } { \varepsilon } } g _ { z } ( x _ { n } ) { \Big ) } \right\| \leq \operatorname* { s u p } \{ | R ( \mu ) | ; \operatorname { R e } \mu \leq - h / \varepsilon \} \leq \alpha < 1 .
$$

The bound $\alpha$ is strictly smaller than 1,because $| R ( \infty ) | < 1$ and $- h / \varepsilon \le - 1 / c < 0$ The triangle inequality applied to (3.62) completes the proof of Formula (3.60).

c) Applying Lemma 3.9 below to the difference inequality (3.60) gives

$$
\Delta y _ { n } = { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h ) , \qquad \Delta z _ { n } = { \mathcal O } ( \varepsilon ^ { \nu + 1 } / h )
$$

for $n h \leq C o n s t$ . We are now in a position to justify the assumption $\Delta y _ { n } = \mathcal { O } ( h )$ and $\Delta z _ { n } = \mathcal { O } ( h )$ of the beginning of the proof. Indeed, this follows by induction on $n$ $( \Delta y _ { 0 } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$ ， $\Delta z _ { 0 } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) )$ and from (3.64), because $\nu = q + 1 \ge 2$

d) Formula (3.64) proves the desired result (3.56) for the $z$ -component. However, the estimate (3.64) is not yet optimal for the $y$ -component. The proof for the correct estimate is similar to that of Theorem 3.4. We have to treat more carefully the expression which gives rise to the ${ \mathcal O } ( \varepsilon ^ { \nu + 1 } / h )$ term in (3.61). Using (3.59) and (3.64) the same calculations which gave (3.61), now yield

$$
\begin{array} { c } { \Delta k _ { n \ i } = f _ { y } ( x _ { n } ) \Delta Y _ { n \ i } + f _ { z } ( x _ { n } ) \Delta Z _ { n \ i } + \mathcal O ( \varepsilon ^ { \nu + 1 } ) } \\ { \varepsilon \Delta \ell _ { n \ i } = g _ { y } ( x _ { n } ) \Delta Y _ { n \ i } + g _ { z } ( x _ { n } ) \Delta Z _ { n \ i } + \varepsilon ^ { \nu + 1 } \ell _ { n \ i } ^ { \nu } + \mathcal O ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

We compute $\Delta Z _ { n \imath }$ from (3.65b) and insert it into (3.65a). This gives

$$
\begin{array} { r l } & { \qquad \Delta k _ { n \iota } - \bigl ( f _ { z } g _ { z } ^ { - 1 } \bigr ) ( x _ { n } ) \bigl ( \varepsilon \Delta \ell _ { n \iota } - \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } \bigr ) } \\ & { \qquad = \bigl ( f _ { y } - f _ { z } g _ { z } ^ { - 1 } g _ { y } \bigr ) ( x _ { n } ) \Delta Y _ { n \iota } + \mathcal { O } ( \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

Guided by this formula we put

$$
\Delta u _ { n } = \Delta y _ { n } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \big ( \varepsilon \Delta z _ { n } - \varepsilon ^ { \nu + 1 } z _ { n } ^ { \nu } \big ) .
$$

Since

$$
\begin{array} { r l r } {  { \Delta u _ { n + 1 } = \Delta u _ { n } + h \sum _ { \iota = 1 } ^ { s } \underline { b } _ { \iota } \Big ( \Delta k _ { n \iota } - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) \big ( \varepsilon \Delta \ell _ { n \iota } - \varepsilon ^ { \nu + 1 } \ell _ { n \iota } ^ { \nu } \big ) \Big ) } } \\ & { } & { \qquad - ( ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } + h ) - ( f _ { z } g _ { z } ^ { - 1 } ) ( x _ { n } ) ) ( \varepsilon \Delta z _ { n + 1 } - \varepsilon ^ { \nu + 1 } z _ { n + 1 } ^ { \nu } ) } \end{array}
$$

it follows from (3.66),(3.64),and (3.42) that

$$
\begin{array} { r } { \| \Delta u _ { n + 1 } \| \leq ( 1 + c h ) \| \Delta u _ { n } \| + \mathcal { O } ( h \varepsilon ^ { \nu + 1 } ) . } \end{array}
$$

As in the proof of Theorem 3.4 we deduce $\Delta u _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$ and $\Delta y _ { n } = \mathcal { O } ( \varepsilon ^ { \nu + 1 } )$

In the above proof we used the following result.

Lemma 3.9. Let $\{ u _ { n } \}$ ， $\{ v _ { n } \}$ be two sequences of non-negative numbers satisfying (componentwise)

$$
\begin{array} { r } { \left( \begin{array} { c } { u _ { n + 1 } } \\ { v _ { n + 1 } } \end{array} \right) \leq \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( \varepsilon ) } \\ { \mathcal { O } ( 1 ) } & { \alpha + \mathcal { O } ( \varepsilon ) } \end{array} \right) \left( \begin{array} { c } { u _ { n } } \\ { v _ { n } } \end{array} \right) + M \left( \begin{array} { c } { h } \\ { 1 } \end{array} \right) } \end{array}
$$

with $0 \leq \alpha < 1$ and $M \geq 0$ . Then the following estimates hold for $\varepsilon \leq c h , h \leq h _ { 0 }$ and $n h \le C o n s t$

$$
\begin{array} { r l } & { u _ { n } \leq C ( u _ { 0 } + \varepsilon v _ { 0 } + M ) } \\ & { v _ { n } \leq C ( u _ { 0 } + ( \varepsilon + \alpha ^ { n } ) v _ { 0 } + M ) . } \end{array}
$$

Proof. We transform the matrix in (3.69) to diagonal form and so obtain

$$
\left( \begin{array} { c } { u _ { n } } \\ { v _ { n } } \end{array} \right) \leq T ^ { - 1 } \left( \begin{array} { c c } { \lambda _ { 1 } ^ { n } } & { 0 } \\ { 0 } & { \lambda _ { 2 } ^ { n } } \end{array} \right) T \left( \begin{array} { c } { u _ { 0 } } \\ { v _ { 0 } } \end{array} \right) + M \sum _ { \jmath = 1 } ^ { n } T ^ { - 1 } \left( \begin{array} { c c } { \lambda _ { 1 } ^ { n - \jmath } } & { 0 } \\ { 0 } & { \lambda _ { 2 } ^ { n - \jmath } } \end{array} \right) T \left( \begin{array} { c } { h } \\ { 1 } \end{array} \right)
$$

where $\lambda _ { 1 } = 1 + \mathcal { O } ( h ) , \lambda _ { 2 } = \alpha + \mathcal { O } ( \varepsilon )$ are the eigenvalues and the transformation matrix $T$ (composed of eigenvectors) satisfies

$$
T = \left( \begin{array} { c c } { { 1 } } & { { \mathcal { O } ( \varepsilon ) } } \\ { { \mathcal { O } ( 1 ) } } & { { 1 } } \end{array} \right) .
$$

The statement now follows from the fact that $( \alpha + \mathcal { O } ( \varepsilon ) ) ^ { n } = \mathcal { O } ( \alpha ^ { n } ) + \mathcal { O } ( \varepsilon )$ for $\varepsilon \leq c h$ and $n h \le C o n s t$ □

By combining Theorems 3.3,3.4 and 3.8 we get the following result.

Corollary 3.10 (Hairer, Lubich & Roche 1988). Under the assumptions of Theorem 3.8 the global error of a Runge-Kutta method satisfies

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon h ^ { q + 1 } ) , \qquad z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { q + 1 } ) .
$$

If in addition $a _ { s _ { 1 } } = b _ { \ i }$ for all $i$ , we have

$$
z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon h ^ { q } ) .
$$

Remarks. a) If the $A$ -stability assumption is dropped and the coefficient matrix $A$ is only assumed to be invertible, then the estimates of Corollary 3.10 still hold for $\varepsilon \leq \bar { k } \tilde { h }$ where $\bar { k } ^ { \ast }$ is a method-dependent constant (see Remark 3.7).

b) $A$ -stability and the invertibility of the matrix $A$ imply in general that the eigenvalues of $A$ have positive real part. Otherwise the stability function would have to be reducible.

c) For several Runge-Kutta methods satisfying $a _ { s _ { 1 } } = b _ { \ i }$ the estimate (3.71) for the $y$ -component can be improved. E.g., for Radau IIA and for Lobatto IIC one has $y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon ^ { 2 } h ^ { q } )$ . This follows from Table VII.4.1 below.

d) A completely different proof of the estimates (3.71) is given by Nipp & Stoffer (1995). They show that the Runge-Kutta method, considered as a discrete

dynamical system, admits an attractive invariant manifold $M _ { h , \varepsilon }$ ， which is close to the invariant manifold $M _ { \varepsilon }$ of the problem (3.1). Studying the closeness of the two manifolds, they obtain the error estimates (3.71) without considering $\varepsilon$ -expansions.

e) The analogues of Theorem 3.8 and Corollary 3.10 for Rosenbrock methods are given in Hairer,Lubich & Roche (1989).

f) Estimates for $p = q$ are given in Exercise 3 below.

# Numerical Confirmation

The estimates of Corollary 3.10 can be observed numerically. As an example of (3.1) we choose the van der Pol equation

$$
\begin{array} { c } { { y ^ { \prime } = z } } \\ { { \varepsilon z ^ { \prime } = ( 1 - y ^ { 2 } ) z - y } } \end{array}
$$

with $\varepsilon = 1 0 ^ { - 5 }$ and initial values

$$
y ( 0 ) = 2 , \qquad z ( 0 ) = - 0 . 6 6 6 6 5 4 3 2 1 1 2 1 1 7 2
$$

on the smooth solution (Exercise 2).

Table 3.1 shows the methods of our experiment together with the theoretical error bounds. In Fig.3.1 we have plotted the relative global error at $x _ { e n d } = 0 . 5$ as a function of the step size $h$ ，which was taken constant over the considered interval. The use of logarithmic scales in both directions makes the curves appear as straight lines of slope $\mathscr { r }$ ， whenever the leading term of the global error behaves like $C o n s t \cdot h ^ { r }$ . The figures show complete agreement with our theoretical results.

Table 3.1. Global errors predicted by Corollary 3.10   

<table><tr><td>Method</td><td>ag=b</td><td>y -comp.</td><td>z -comp.</td></tr><tr><td>Radau IA</td><td>no</td><td>h2s-1+eh8</td><td>h</td></tr><tr><td>Radau IIA</td><td>yes</td><td>h2g-1+e²h8</td><td>h2s-1+eh</td></tr><tr><td>Lobatto IIIC</td><td>yes</td><td>h2s-2+e²h8-1</td><td>h²s-2+eh8-1</td></tr><tr><td>SDIRK (IV.6.16)</td><td>yes</td><td>h4+h²</td><td>h4+εh</td></tr><tr><td>SDIRK (IV.6.18)</td><td>no</td><td>h4+h²</td><td>h2</td></tr></table>