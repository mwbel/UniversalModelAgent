# 35 Stability of Implicit Runge–Kutta Methods

350 $A$ -stability, $A ( \alpha )$ -stability and L-stability

We recall that the stability function for a Runge–Kutta method (238b) is the rational function

$$
R ( z ) = 1 + z b ^ { \top } ( I - z A ) ^ { - 1 } \mathbf { 1 } ,
$$

and that a method is A-stable if

$$
| R ( z ) | \leq 1 , \quad { \mathrm { w h e n e v e r ~ } } \mathrm { R e } ( z ) \leq 0 .
$$

For the solution of stiff problems, A-stability is a desirable property, and there is sometimes a preference for methods to be L-stable; this means that the method is A-stable and that, in addition,

$$
R ( \infty ) = 0 .
$$

Where A-stability is impossible or difficult to achieve, a weaker property is acceptable for the solution of many problems.

Definition 350A Let $\alpha$ denote an angle satisfying $\alpha \in ( 0 , \pi )$ and let $S ( \alpha )$ denote the set of points $x + i y$ in the complex plane such that $x \ \leq \ 0$ and $- \tan ( \alpha ) | x | \leq y \leq \tan ( \alpha ) | x |$ . A Runge–Kutta method with stability function $R ( z )$ is $A ( \alpha )$ -stable if $| R ( z ) | \leq 1$ for all $z \in S ( \alpha )$ .

The region $S ( \alpha )$ is illustrated in Figure 350(i) in the case of the Runge–Kutta method

<table><tr><td rowspan="4">入 1+ 2 1</td><td>入</td><td>0</td><td>0</td></tr><tr><td>1-</td><td>入</td><td>0</td></tr><tr><td>2 (1-λ)(1-9λ+6)²)</td><td>2(1-λ)(1-6λ+6λ²)</td><td></td></tr><tr><td>1-3入+6λ2</td><td>1-3入+6λ2</td><td>入</td></tr><tr><td rowspan="3"></td><td></td><td>2(1-3&gt;)</td><td></td></tr><tr><td>1+3&gt; 6(1-)2</td><td>3(1-&gt;)2</td><td>1-3入+6λ² 6(1-λ)2</td></tr><tr><td></td><td></td><td></td></tr></table>

where $\lambda \approx 0 . 1 5 8 9 8 4$ is a zero of $6 \lambda ^ { 3 } - 1 8 \lambda ^ { 2 } + 9 \lambda - 1$ . This value of $\lambda$ was chosen to ensure that (350b) holds, even though the method is not A-stable. It is, in fact, $\mathrm { A } ( \alpha )$ -stable with $\alpha \approx 1 . 3 1 9 4 6 \approx 7 5 . 5 9 9 6 ^ { \circ }$ .
