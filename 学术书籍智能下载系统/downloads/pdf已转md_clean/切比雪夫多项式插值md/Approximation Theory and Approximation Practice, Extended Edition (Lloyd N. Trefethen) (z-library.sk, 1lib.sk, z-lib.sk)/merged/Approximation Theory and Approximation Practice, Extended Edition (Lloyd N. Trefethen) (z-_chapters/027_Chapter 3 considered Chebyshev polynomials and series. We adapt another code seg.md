Chapter 3 considered Chebyshev polynomials and series. We adapt another code segment from Chapter 17 to illustrate how a Chebyshev polynomial $T _ { n } ( x )$ compares to the corresponding transformed polynomial $T _ { n } ( g ^ { - 1 } ( x ) )$ . For this we need the inverse map $g ^ { - 1 }$ .

$\tt { g i } = \tt { i n v } ( \tt { g } )$ ; $\mathrm { T 5 0 ~ = }$ chebpoly(50); subplot(2,1,1), plot(T50), plot(T50(gi),'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/092327442afbae877400180cee5b60fe4a6be53b3d8330b4fa60397ff6f8ac7d.jpg)

Notice that the lower curves are more like uniform sine waves than the upper ones.

Theorem 3.1 summarized some basic facts about Chebyshev series, and these carry over immediately to a theorem for transformed Chebyshev series. The theorem as stated assumes $g$ is analytic, though in fact, continuous differentiability would be enough.

Theorem 22.1. Transformed Chebyshev series. Let $g$ be an analytic function on $[ - 1 , 1 ]$ mapping $[ - 1 , 1 ]$ to itself with $g ^ { \prime } ( s ) > 0$ . Then if $f$ is Lipschitz continuous on $[ - 1 , 1 ]$ , it has a unique representation as an absolutely convergent series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } { \bigl ( } g ^ { - 1 } ( x ) { \bigr ) } ,
$$

and the coefficients are given for $k \geq 1$ by the formula

$$
a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( g ( s ) ) T _ { k } ( s ) } { \sqrt { 1 - s ^ { 2 } } } d s
$$

and for $k = 0$ by the same formula with the factor $2 / \pi$ changed to $1 / \pi$

Proof. This is a consequence of Theorem 3.1.

For many functions $f$ , the transformed series are $2 0 - 3 0 \%$ more efficient than the originals. For example, Chebyshev interpolation of $( 2 + \cos ( 2 0 x + 1 ) ) ^ { - 1 }$ requires about 520 terms for 15-digit accuracy:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/3ee084befebde40f7769f1c49fbec04e681c07b84f3dd47adcbe9f25b88c3522.jpg)

For the transformed interpolants the number is closer to 400:

plotcoeffs(f(g),'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/5990e9478385f1faccb15819b7e9b302f53d5ac8e689fd5c34b060a28adc0027.jpg)
