# 213 Convergence of the Euler method

We consider a sequence of approximations to $y ( { \overline { { x } } } )$ . In each of these approximations, a computation using the Euler method is performed, starting from an approximation to $y ( x _ { 0 } )$ , and taking a sequence of positive steps. Denote approximation number $n$ by $\widetilde { y } _ { n }$ .

The only assumption we will make about $\widetilde { y } _ { n }$ , for each specific value of $n$ , is that the initial error $y ( x _ { 0 } ) - \widetilde { y } _ { n } ( x _ { 0 } )$ is bounded in norm by $K _ { n }$ and that the greatest stepsize is bounded by $H _ { n }$ . It is assumed that, as $n \longrightarrow \infty$ , $H _ { n } \to 0$ and $K _ { n }  0$ . As always, we assume that $f$ satisfies a Lipschitz condition.

Denote by $D _ { n }$ the value of $\| y ( \overline { { x } } ) - \widetilde { y } _ { n } ( \overline { { x } } ) \|$ .

Theorem 213A Under the conditions stated in the above discussion, $D _ { n } \to 0$ as $n \longrightarrow \infty$ .

Proof. This result follows immediately from the bound on accumulated errors given by Theorem 212A. $\sqcup$

The property expressed in this theorem is known as ‘convergence’. In searching for other numerical methods that are suitable for solving initial value problems, attention is usually limited to convergent methods. The reason for this is clear: a non-convergent method is likely to give increasingly meaningless results as greater computational effort is expended through the use of smaller stepsizes.

Because the bound used in the proof of Theorem 213A holds not only for $x = { \overline { { x } } }$ , but also for all $x \in [ x _ { 0 } , { \overline { { x } } } ]$ , we can state a uniform version of this result.

Theorem 213B Under the conditions of Theorem 213A,

$$
\operatorname* { s u p } _ { x \in [ x _ { 0 } , { \overline { { x } } } ] } \| y ( x ) - { \widetilde { y } } _ { n } ( x ) \| \to 0
$$

as $n \longrightarrow \infty$ .

An example of enhanced order for problem (214a)   

<table><tr><td>n</td><td>[Error|</td><td>Ratio</td></tr><tr><td>20</td><td>1130400.0252×10-10</td><td>4.4125</td></tr><tr><td>40</td><td>256178.9889×10-10</td><td>4.1893</td></tr><tr><td>80</td><td>61150.2626×10-10</td><td>4.0904</td></tr><tr><td>160</td><td>14949.6176×10-10</td><td>4.0442</td></tr><tr><td>320</td><td>3696.5967×10-10</td><td>4.0218</td></tr><tr><td>640</td><td>919.1362 × 10-10</td><td>4.0108</td></tr><tr><td>1280</td><td>229.1629 × 10-10</td><td>4.0054</td></tr><tr><td>2560</td><td>57.2134× 10-10</td><td>4.0026</td></tr><tr><td>5120</td><td>14.2941×10-10</td><td>4.0003</td></tr><tr><td>10240</td><td>3.5733×10-10</td><td></td></tr></table>
