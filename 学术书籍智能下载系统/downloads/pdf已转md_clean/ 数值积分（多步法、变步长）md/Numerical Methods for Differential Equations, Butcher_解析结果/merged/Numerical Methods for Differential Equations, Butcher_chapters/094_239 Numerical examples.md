# 239 Numerical examples

High order methods generally perform better than low order methods if sufficiently small stepsizes are used. We illustrate this by attempting, with the methods introduced in this section, a solution to the gravitational problem (201d) with initial values corresponding to an eccentricity $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ . Although calculations were performed with each of the seven methods RK21, RK22, RK31, RK32, RK41, RK42, RK5, only results for the four methods RK22, RK31, RK42 and RK5 are actually presented in Figure 239(i). It was observed that for the two methods with each of the orders 2, 3 and 4, there was very little difference between the accuracy achieved and a representative of each order – in fact the slightly more accurate method was chosen in each case $^ -$ is sufficient to illustrate the phenomenon of $h ^ { p }$ dependence. In Figure 239(i), methods RK22, RK31, RK42 and RK5 are denoted by 2, 3, 4 and 5.

For this problem, high order methods are always more accurate than low order methods. However, the relative advantage is exaggerated in that no account is taken of the greater work in completing a step as the order increases. Assuming that the total computational work is proportional to the number of stages in the method, it is a simple matter to compensate for this; all that needs to be done is to multiply the number of steps by the number of stages in each method. The comparisons with this correction made are shown in Figure 239(ii). The general conclusion, that high order is more efficient than low order, still follows from these comparisons, but not to such a marked extent.

Numerical tests, not reported here, indicate similar behaviour for implicit methods. For the initial value problem (201a), with output computed at $x = 1$ , (237a) and (237b) gave slightly worse results than for corresponding explicit methods. However, for the fourth order method (237c), the results were approximately six decimal places better. This suggests that, even though the cost of evaluating the result in each step of an implicit method is significantly higher, the extra cost is sometimes worthwhile for this method.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/220dfd13f2c84d938647042f8ebdc5aacb3eb0105a62709625692e8486650322.jpg)  
Runge–Kutta methods with cost corrections

# Exercises 23

23.1 Repeat the calculation that led to Table 221(I) but using the method given by (231a) and (231b) with $\begin{array} { r } { \theta = \frac { 1 } { 2 } } \end{array}$ .

23.2 Find a solution to the third order conditions (233a), (233b), (233c) and (233d) such that $b _ { 1 } = 0$ , $c _ { 3 } = 1$ .

23.3 Continue Table 234(I) to include trees of order 5.

23.4 Write down the formula for $\Phi ( t )$ and the value of $\gamma ( t )$ for $t$ the order 7 tree

$$
t = \ddagger \ddagger
$$

23.5 By noting that $b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } \cdot b _ { 3 } ( c _ { 4 } - c _ { 3 } ) ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = b _ { 4 } a _ { 4 3 } ( c _ { 3 } - c _ { 2 } ) c _ { 3 }$ · $b _ { 3 } ( c _ { 4 } - c _ { 3 } ) a _ { 3 2 } c _ { 2 }$ , prove that $c _ { 4 } = 1$ for any solution to the fourth order conditions (235a)–(235h).

23.6 Find the order of the implicit method given by the tableau (237a).

23.7 Solve the orbital problem with eccentricity $e ~ = ~ 0$ using the implicit method (237a).
