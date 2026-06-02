Chapter 16 will show that Chebyshev interpolants are often as good as best approximations in practice, and this fact may have something to do with why the Remez algorithm is used rather rarely. Chapter 20 will show that if you really want a best approximation, it may be more practical to compute it by CF approximation than by the Remez algorithm, at least if $f$ is smooth. There are also other algorithms for computing best approximations, based, for example, on linear programming, which we shall not discuss.

Summary of Chapter 10. Any $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $p ^ { * } \in \mathcal { P } _ { n }$ with respect to the $\infty$ -norm. If $f$ is real, $p ^ { * }$ is characterized by having an error curve that equioscillates between at least $n + 2$ extreme points.

Exercise 10.1. A function with spikes. Compute numerically the degree 10 polynomial best approximation to $\mathrm { s e c h } ^ { 2 } ( 5 ( x + 0 . 6 ) ) + \mathrm { s e c h } ^ { 4 } ( 5 0 ( x + 0 . 2 ) ) + \mathrm { s e c h } ^ { 6 } ( 5 0 0 ( x - 0 . 2 ) )$ on $[ - 1 , 1 ]$ and plot $f$ together with $p ^ { * }$ as well as the error curve. What is the error? How does this compare with the error in 11-point Chebyshev interpolation?

Exercise 10.2. Best approximation of $| x |$ . (a) Use Chebfun to determine the errors $E _ { n } \ = \ \| f - p _ { n } \|$ in the degree $n$ best approximation of $f ( x ) \ = \ | x |$ on $[ - 1 , 1 ]$ for $n =$ $2 , 4 , 8 , \ldots , 2 5 6$ , and make a table of the values $\beta _ { n } ~ = ~ n E _ { n }$ as a function of $n$ . (b) Use Richardson extrapolation to improve your data. How many digits can you estimate for the limiting number $\beta = \mathrm { l i m } _ { n  \infty } \beta _ { n } \mathrm { : }$ (We shall discuss this problem in detail in Chapter 25.)

Exercise 10.3. de la Vall´ee Poussin lower bound. Suppose an approximation $p \in \mathcal { P } _ { n }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } <$ $s _ { 1 } < \cdot \cdot \cdot < s _ { n + 1 } \leq 1$ at which $f - p$ alternates in sign with $| f ( s _ { j } ) - p ( s _ { j } ) | \geq \varepsilon$ for some $\varepsilon > 0$ . Show that $\| f - p ^ { * } \| \geq \varepsilon$ . (This estimate originates in [de la Vall´ee Poussin 1910].)

Exercise 10.4. Best approximation of even functions. Let $f \in C ( [ - 1 , 1 ] )$ be an even function, i.e., $f ( - x ) = f ( x )$ for all $_ x$ . (a) Prove as a corollary of Theorem 10.1 that for any $n \geq 0$ , the best approximation $\boldsymbol { p } _ { n } ^ { * }$ is even. (b) Prove that for any $n \geq 0$ , $p _ { 2 n } ^ { * } = p _ { 2 n + 1 } ^ { * }$ . (c) Conversely, suppose $f \in C ( [ - 1 , 1 ] )$ is not even. Prove that for all sufficiently large $n$ , its best approximations $\boldsymbol { p } _ { n } ^ { * }$ are not even.

Exercise 10.5. An invalid theorem. The first two figures of this chapter suggest the following “theorem”: if $f$ is an even function on $[ - 1 , 1 ]$ and $p ^ { * }$ is its best approximation of some degree $_ n$ , then one of the extreme points of $| ( f - p ^ { * } ) ( x ) |$ occurs at $x = 0$ . Pinpoint the flaw in the following “proof.” By the argument of Exercise 10.4(b), $p ^ { * }$ is the best approximation to $f$ for all $n$ in some range of the form even $\leq n \leq$ odd, such as $4 \leq n \leq 5$ or $1 0 \leq n \leq 1 3$ . By Theorem 10.1, the maximal number of equioscillation points of $f - p ^ { * }$ must accordingly be of the form $\mathrm { o d d } + 2$ , that is, odd. By symmetry, 0 must be one of these points. Exactly which of these three logical steps is invalid, and why?

Exercise 10.6. Nonlinearity of best approximation operator. We have mentioned that for given $_ n$ , the operator that maps a function $f \in C ( [ - 1 , 1 ] )$ to its best degree $n$ approximation $p _ { n } ^ { * }$ is nonlinear. Prove this (on paper, not numerically) by finding two functions $f _ { 1 }$ and $f _ { 2 }$ and an integer $n \geq 0$ such that the best approximation of the sum in $\mathcal { P } _ { n }$ is not the sum of the best approximations.

Exercise 10.7. Bernstein’s lethargy theorem. Exercise 6.1 considered a function of Weierstrass, continuous but nowhere differentiable. A variant of the same function based on Chebyshev polynomials would be

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } 2 ^ { - k } T _ { 3 ^ { k } } ( x ) .
$$

(a) Show that the polynomial $f _ { 3 ^ { k } }$ obtained by truncating (10.1) to degree $3 ^ { k }$ is the best approximation to $f$ in the spaces $\mathcal { P } _ { n }$ for certain $n$ . What is the complete set of $_ n$ for which this is true? What is the error? (b) Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Prove that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - p _ { n } ^ { * } \| \geq \varepsilon _ { n }$ for all $_ n$ . (Hint: Change the coefficients $2 ^ { - k }$ of (10.1) to values related to $\left\{ \varepsilon _ { n } \right\}$ .)

Exercise 10.8. Continuity of best approximation operator. For any $n \geq 0$ , the mapping from functions $f \in C ( [ - 1 , 1 ] )$ to their best approximants $p ^ { * } \in \mathcal { P } _ { n }$ is continuous with respect to the $\infty$ -norm in $C ( [ - 1 , 1 ] )$ . Prove this by an argument combining the uniqueness of best approximations with compactness. (This continuity result appears in Section I.5 of [Kirchberger 1902]. In fact, the mapping is not just continuous but Lipschitz continuous, a property known as strong uniqueness, but this is harder to prove.)

Exercise 10.9. Approximation of $e ^ { x }$ . Truncating the Taylor series for $e ^ { x }$ gives polynomial approximations with maximum error $E _ { n } \sim 1 / ( n + 1 ) !$ ! on $[ - 1 , 1 ]$ , but the best

approximations do better by a factor of $2 ^ { n }$ :

$$
E _ { n } \sim \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } , \quad n \to \infty .
$$

(a) Derive (10.2) by combining Exercises 3.15 and 10.3 with the asymptotic formula $I _ { k } ( 1 ) \sim$ $1 / ( 2 ^ { n } n ! )$ . (b) Make a table comparing this estimate with the actual values $E _ { n }$ computed numerically for $0 \leq n \leq 1 0$ .

Exercise 10.10. Alternative proof of uniqueness. Prove uniqueness of the degree $_ n$ best approximant to a real continuous function $f$ by a simpler argument than the one given in the proof of Theorem 10.1: suppose $p$ and $q$ are best approximants, and apply the equioscillation characterization to $r = ( p + q ) / 2$ .

Exercise 10.11. Chebyshev polynomials and best approximations. (a) What is the best degree $n$ polynomial approximation to $x ^ { n + 1 }$ on $[ - 1 , 1 ]$ ? What is the error? Derive the answers from Theorem 10.1, using the fact that $T _ { n + 1 }$ oscillates between values $\pm 1$ at $n + 2$ points in $[ - 1 , 1 ]$ . (b) What is the best approximation to 0 among monic polynomials of degree $n + 1$ ? What is the error?

Exercise 10.12. Every best approximant is an interpolant. Let $p$ be the best approximation in $\mathcal { P } _ { n }$ to a real function $f \in C ( [ - 1 , 1 ] )$ . Show that there exist $n + 1$ distinct points $- 1 < x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < 1$ such that $p$ is the interpolant in $\mathcal { P } _ { n }$ to $f$ in the points $\{ x _ { j } \}$ .

Exercise 10.13. A contrast to Faber’s theorem. Although Faber showed that there does not exist an array of nodes in $[ - 1 , 1 ]$ whose polynomial interpolants converge for every $f \in C [ - 1 , 1 ]$ , for any fixed $f$ there exists an array whose interpolants converge to $f$ [Marcinkiewicz 1936–37]. Prove this by combining the Weierstrass approximation theorem with the result of the previous exercise.

Exercise 10.14. Asymptotics of the leading coefficient. Let $\{ p _ { n } ^ { * } \}$ be the sequence of best approximations of a function $f \in C ( [ - 1 , 1 ] )$ , and let $p _ { n } ^ { * }$ have leading Chebyshev coefficient $a _ { n } ^ { * }$ . It is known that $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n  \infty } | a _ { n } ^ { * } | ^ { 1 / n } \leq 1 } \end{array}$ , with strict inequality if and only if $f$ is analytic on $[ - 1 , 1 ]$ [Blatt $\&$ Saff 1986, Thm. 2.1]. Verify this result numerically by estimating $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } | a _ { n } ^ { * } | ^ { 1 / n } } \end{array}$ for $f ( x ) = \left| x \right|$ and $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ .
