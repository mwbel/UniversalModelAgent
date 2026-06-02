# 432 Examples of the boundary locus method

The first example is for the second order Adams–Bashforth method (430a) for which (431c) takes the form

$$
w \mapsto \frac { 1 - w ^ { - 1 } } { \frac { 3 } { 2 } w ^ { - 1 } - \frac { 1 } { 2 } w ^ { - 2 } } .
$$

For $w = \exp ( i \theta )$ and $\theta \in [ 0 , 2 \pi ]$ , for points on the unit circle, we have $z$ values on the (possibly extended) boundary of the stability region given by

$$
z = \frac { \exp ( 2 i \theta ) - \exp ( i \theta ) } { \frac { 3 } { 2 } \exp ( i \theta ) - \frac { 1 } { 2 } } .
$$

The MATLAB code given in Algorithm $4 3 2 \alpha$ shows how this is done, and the boundary traced out is exactly as in Figure 430(i).

No confusion is possible as to which part of the complex plane divided by the boundary locus is the inside and which is the outside because, using an argument based on the Cauchy–Riemann equations, we note that the inside is always to the left of the path traced out as $w$ increases from 0 to $2 \pi$ . If we had used (431d) in place of (431c) then, of course, the path would have been traced in the opposite direction and the inside of the stability region would have been on the right. Note that in Algorithm $4 3 2 \alpha$ the third and fourth order cases are traced in the reverse direction. The stability region of the third Adams–Bashforth method, as computed by this algorithm, is given as the unshaded region of Figure 432(i).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/e77f29dc130d7a2a35381330699d26765121ccaa34ee6e9abd8c387db9d332c1.jpg)  
Stability region for the third order Adams–Bashforth method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/07ff1f92256924a1071a6f8d9511c39ea29bb5b69f8f4de78b511851fd15c853.jpg)  
Stability region for the fourth order Adams–Bashforth method

In the case of the fourth order method in this family, the root locus method traces out more than the boundary of the stability region, as we see in Figure 432(ii). Because crossing the locus corresponds to the shift of one of the growth factors from stable to unstable, the more heavily shaded region is doubly unstable in that it contains two unstable terms.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/09e8b8d4758e6c8c9f7d092e1999510f9725d3ab6153c8191ab1e0af41fa0838.jpg)  
Stability region for the third order Adams–Moulton method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/e2847c06f9e73a7cf714b1df68beb7981b1376cd92baaad159e0aee554c17ba5.jpg)  
Stability region for the second order backward difference method

We present three final examples. The Adams–Moulton method of order 3 is given in Figure 432(iii); we see that even though this method is implicit it has a bounded stability region.

Now look at the stability regions of the backward difference methods of orders 2 and 3. The first of these, shown in Figure 432(iv), indicates that the second order method is A-stable and the second, Figure 432(v), shows that the third order method is not A-stable.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/a966dc9c5a14da42a517c57e7dceef80612cb0da827417a8f79cb492916ce7ec.jpg)  
Stability region for the third order backward difference method
