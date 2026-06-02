# 214 Order of convergence

It is interesting to know not only that a numerical result is convergent, but also how quickly it converges. In the case of a constant stepsize $h$ , the bound on the global error given in Theorem 212A is proportional to $h$ . We describe this by saying that the order of the Euler method is (at least) 1.

That the order is exactly 1, and that it is not possible, for a general differential equation, to obtain error behaviour proportional to some higher power of $h$ , can be seen from a simple example. Consider the initial value problem

$$
y ^ { \prime } ( x ) = 2 x , \qquad y ( 0 ) = 0 ,
$$

with exact solution $y ( x ) = x ^ { 2 }$ . If $\overline { { x } } ~ = ~ 1$ , and $n$ steps are performed with stepsize $h = n ^ { - 1 }$ , the computed solution is

$$
h \sum _ { k = 0 } ^ { n - 1 } { \frac { 2 k } { n } } = { \frac { n - 1 } { n } } .
$$

This differs from the exact solution by $1 / n = h$ .

In spite of the fact that the order is only 1, it is possible to obtain higher order behaviour in special specific situations. Consider the initial value problem

$$
y ^ { \prime } ( x ) = - y ( x ) \tan ( x ) - { \frac { 1 } { \cos ( x ) } } , \qquad y ( 0 ) = 1 ,
$$

with solution $y ( x ) = \cos ( x ) - \sin ( x )$ . Because of an exact cancellation of the most significant terms in the error contributions, at different parts of the trajectory, the computed results for this problem are consistent with the order being 2 rather than 1, if the output value is taken as $\overline { { x } } \approx 1 . 2 9 2 6 9 5 7 1 9 3 7 3$ . Note that $\scriptstyle { \overline { { x } } }$ was chosen to be a zero of $\exp ( x ) \cos ( x ) = 1$ . As can be seen from Table 214(I), as the number of steps doubles, the error reduces by a factor approximately equal to $2 ^ { - 2 }$ . This is consistent with second order, rather than first order, behaviour. The errors are also plotted in Figure 214(i).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/19b474494e72d9441d08b8d2cb6b7b913482f958c5221c79f2884158e4269233.jpg)  
Error versus stepsize for problem (214a) at two alternative output points

An analysis of the apparent cancellation of the most significant component of the global truncation error is easy to carry out if we are willing to do the estimation with terms, which decrease rapidly as $h  0$ , omitted from the calculation. A more refined analysis would take these additional terms into account, but would obtain bounds on their effect on the final result. In step $k$ , from a total of $n$ steps, the local truncation error is approximately $- { \textstyle { \frac { 1 } { 2 } } } h ^ { 2 } ( \cos ( x _ { k } ) - \sin ( x _ { k } ) )$ . To find the contribution this error makes to the accumulated error at $x _ { n } = { \overline { { x } } }$ , multiply by the product

$$
{ \big ( } 1 - h \tan ( x _ { n - 1 } ) { \big ) } { \big ( } 1 - h \tan ( x _ { n - 2 } ) { \big ) } \cdots { \big ( } 1 - h \tan ( x _ { k } ) { \big ) } .
$$

We have the approximation

$$
{ \frac { \cos ( x + h ) } { \cos ( x ) } } = \cos ( h ) - \sin ( h ) \tan ( x ) \approx 1 - h \tan ( x ) ,
$$

so that (214b) can be written approximately as

$$
{ \frac { \cos ( x _ { n } ) } { \cos ( x _ { n - 1 } ) } } { \frac { \cos ( x _ { n - 1 } ) } { \cos ( x _ { n - 2 } ) } } \cdot \cdot \cdot { \frac { \cos ( x _ { k + 1 } ) } { \cos ( x _ { k } ) } } = { \frac { \cos ( x _ { n } ) } { \cos ( x _ { k } ) } } .
$$

An example of reduced order for problem (214c)   

<table><tr><td>n</td><td>[Error]</td><td>Ratio</td></tr><tr><td>8</td><td>0.3012018700</td><td>1.4532</td></tr><tr><td>16</td><td>0.2072697687</td><td>1.4376</td></tr><tr><td>32</td><td>0.1441738248</td><td>1.4279</td></tr><tr><td>64</td><td>0.1009724646</td><td>1.4220</td></tr><tr><td>128</td><td>0.0710078789</td><td>1.4186</td></tr><tr><td>256</td><td>0.0500556444</td><td>1.4166</td></tr><tr><td>512</td><td>0.0353341890</td><td>1.4155</td></tr><tr><td>1024</td><td>0.0249615684</td><td>1.4149</td></tr><tr><td>2048</td><td>0.0176414532</td><td></td></tr><tr><td>4096</td><td>0.0124709320</td><td>1.4146</td></tr><tr><td></td><td></td><td>1.4144</td></tr><tr><td>8192</td><td>0.0088169646</td><td>1.4143</td></tr><tr><td>16384 32768</td><td>0.0062340372 0.0044079422</td><td>1.4143</td></tr></table>

Multiply this by the error in step $k$ and add over all steps. The result is

$$
- { \frac { 1 } { 2 } } h ^ { 2 } \cos ( \overline { { x } } ) \sum _ { k = 1 } ^ { n } { \frac { \cos ( x _ { k } ) - \sin ( x _ { k } ) } { \cos ( x _ { k } ) } } ,
$$

which is approximately equal to the integral

$$
- \frac { 1 } { 2 } h \cos ( \overline { x } ) \int _ { 0 } ^ { \overline { x } } \frac { \cos ( x ) - \sin ( x ) } { \cos ( x ) } d x = - \frac { 1 } { 2 } h \cos ( \overline { x } ) ( \overline { x } + \mathrm { l n } \cos ( \overline { x } ) ) .
$$

This vanishes when $\exp ( { \overline { { x } } } ) \cos ( { \overline { { x } } } ) = 1$ .

For comparison, results are also given in Figure 214(i) for a similar sequence of $h$ values, but at the output point $\overline { { x } } = \pi / 4$ . This case is unsurprising, in that it shows typical order 1 behaviour.

Finally, we present a problem for which an order, even as high as $1$ , is not observed. The initial value problem is

$$
y ^ { \prime } ( x ) = - { \frac { x y } { 1 - x ^ { 2 } } } , \qquad y ( 0 ) = 1 ,
$$

with exact solution $y = { \sqrt { 1 - x ^ { 2 } } }$ . The solution is sought at $\overline { { x } } = 1$ and the numerical results are shown in Table 214(II). It is seen that, as the number of steps doubles, the error reduces by a factor of approximately $2 ^ { - 1 / 2 }$ . Thus, the order seems to have been reduced from 1 to $\textstyle { \frac { 1 } { 2 } }$ . The reason for the loss of order for this problem is that the Lipschitz condition does not hold at the end of the trajectory (at $x = 1$ , $y = 0$ ). As for any initial value problem, the error in the approximate solution at this point develops from errors generated at every time step. However, in this case, the local truncation error in the very last step is enough to overwhelm the contributions to the error inherited from all previous steps. In fact the local truncation error for the final step is

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/0aa0245d3b7d862b6af9892fa01f524c3f766a68dbae33e01c32c0fb7ee25b16.jpg)  
Error versus stepsize for problem (214c) at two alternative output points

$$
\begin{array} { c } { y ( 1 ) - y ( 1 - h ) - h f ( 1 - h , y ( 1 - h ) ) } \\ { \displaystyle = - \sqrt { 1 - ( 1 - h ) ^ { 2 } } + h ( 1 - h ) \frac { \sqrt { 1 - ( 1 - h ) ^ { 2 } } } { 1 - ( 1 - h ) ^ { 2 } } , } \end{array}
$$

which simplifies to

$$
- { \frac { 1 } { \sqrt { 2 - h } } } h ^ { \frac { 1 } { 2 } } \approx - 2 ^ { - { \frac { 1 } { 2 } } } h ^ { \frac { 1 } { 2 } } .
$$

Thus, the order $\textstyle { \frac { 1 } { 2 } }$ behaviour can be explained just by the error contributed by the last step.

A second computation, for the solution at $\begin{array} { r } { \overline { { x } } = \frac { 1 } { 2 } } \end{array}$ , causes no difficulty and both results are shown in Figure 214(ii).
