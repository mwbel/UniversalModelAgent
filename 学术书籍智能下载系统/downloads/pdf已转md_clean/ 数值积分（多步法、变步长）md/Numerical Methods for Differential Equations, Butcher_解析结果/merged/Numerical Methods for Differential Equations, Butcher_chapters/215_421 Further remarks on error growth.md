# 421 Further remarks on error growth

In Subsection 420 we gave an informal argument that, over many steps, there is a contribution to the accumulated error from step $n$ of approximately $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 }$ . Since we are interested in the effect of this contribution at some future point $\scriptstyle { \overline { { x } } }$ , we can consider the differential equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

with two possible initial values at the point $ { \boldsymbol { x } } \ = \  { \boldsymbol { x } } _ { n }$ . These possible initial values are

$$
y ( x _ { n } ) \qquad { \mathrm { a n d } } \qquad y ( x _ { n } ) + \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 } ,
$$

and correspond respectively to the exact solution and to the solution perturbed by the error introduced in step $n$ .

This suggests the possibility of analysing the development of numerical errors through the differential equation

$$
z ^ { \prime } ( x ) = { \frac { \partial f ( y ( x ) ) } { \partial y } } z ( x ) + y ^ { ( p + 1 ) } ( x ) , \qquad z ( x _ { 0 } ) = 0 .
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/ad95689aaa97c28acc8b441c3510fb2dcad8aa2b56d959957216ee28cd73602b.jpg)  
Development of accumulated errors in a single step

Using this equation, we might hope to be able to approximate the error after $n$ steps have been performed as

$$
- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p } z ( x _ { n } ) ,
$$

because the linear term in (421a) expresses the rate of growth of the separation of an already perturbed approximation and the non-linear term, when scaled by $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p }$ , expresses the rate at which new errors are introduced as further steps are taken. The negative sign is consistent with the standard convention that errors are interpreted to mean the exact solution minus the approximation.

To turn this idea into a formal result it is possible to proceed in two steps. In the first step, asymptotic approximations are made. In the second, the errors in making these approximations are bounded and estimated so that they can all be bundled together in a single term which tends to zero more rapidly as $h  0$ than the asymptotic approximation to the error.

The second of these steps will not be examined in detail and the first step will be described in terms of the diagram given in Figure $4 2 1 ( \mathrm { i } ) .$ In this figure, $y ( x )$ is the exact solution and ${ \widehat { y } } ( x )$ is the function $y ( x ) + \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p } z ( x )$ .

The function ${ \overline { { y } } } ( x )$  is the exact solution to the differential equation but with initial value at $x _ { n - 1 }$ set to $\widehat { y } ( x _ { n - 1 } )$ . In the single step from $x _ { n - 1 }$ to $x _ { n }$ , the perturbed approximation $\overline { y }$ drifts away from $y$ at an approximate rate $\left( \partial f ( y ( x ) ) / \partial y \right) \left( \overline { { y } } ( x ) - y ( x ) \right)$ , to reach a value $\overline { { y } } ( x _ { n } )$ . Add to this the contribution of local truncation error, corresponding to this step, denoted by $\begin{array} { r c l } { { \delta _ { n } } } & { { = } } & { { \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 } } } \end{array}$ . With this local error added, the accumulated error moves to a value ${ \widehat { y } } ( x _ { n } )$ . However, following the smoothedout curve ${ \widehat { y } } ( x )$ over the interval $[ x _ { n - 1 } , x _ { n } ]$ leads to the same point, to within $O ( h ^ { p + 2 } )$ .
