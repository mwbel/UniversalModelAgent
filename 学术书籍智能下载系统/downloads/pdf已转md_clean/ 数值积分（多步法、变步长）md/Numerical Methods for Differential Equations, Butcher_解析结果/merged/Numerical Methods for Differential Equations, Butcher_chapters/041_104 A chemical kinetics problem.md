# 104 A chemical kinetics problem

We next consider a model of a chemical process consisting of three species, which we denote by $A$ , $B$ and $C$ . The three reactions are

$$
\begin{array} { c } { A  B , } \\ { B + C  A + C , } \\ { B + B  C . } \end{array}
$$

Let $y _ { 1 }$ , $y _ { 2 }$ and $y _ { 3 }$ denote the concentrations of $A$ , $B$ and $C$ , respectively. We assume these are scaled so that the total of the three concentrations is $^ { 1 }$ , and that each of three constituent reactions will add to the concentration of any of the species exactly at the expense of corresponding amounts of the reactants. The reaction rate of (104a) will be denoted by $k _ { 1 }$ . This means that the rate at which $y _ { 1 }$ decreases, and at which $y _ { 2 }$ increases, because of this reaction, will be equal to $k _ { 1 } y _ { 1 }$ . In the second reaction (104b), $C$ acts as a catalyst in the production of $A$ from $B$ and the reaction rate will be written as $k _ { 2 }$ , meaning that the increase of $y _ { 1 }$ , and the decrease of $y _ { 3 }$ , in this reaction will have a rate equal to $k _ { 2 } y _ { 2 } y _ { 3 }$ . Finally, the production of $C$ from $B$ will have a rate constant equal to $k _ { 3 }$ , meaning that the rate at which this reaction takes place will be $k _ { 3 } y _ { 2 } ^ { 2 }$ . Putting all these elements of the process together, we find the system of differential equations for the variation with time of the three concentrations to be

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = - k _ { 1 } y _ { 1 } + k _ { 2 } y _ { 2 } y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = k _ { 1 } y _ { 1 } - k _ { 2 } y _ { 2 } y _ { 3 } - k _ { 3 } y _ { 2 } ^ { 2 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } . } \end{array}
$$

If the three reaction rates are moderately small numbers, and not greatly different in magnitude, then this is a straightforward problem. However, vastly different magnitudes amongst $k _ { 1 }$ , $k _ { 2 }$ and $k _ { 3 }$ can make this problem complicated to understand as a chemical model. Also, as we shall see, the problem then becomes difficult to solve numerically. This problem was popularized by Robertson (1966), who used the reaction rates

$$
k _ { 1 } = 0 . 0 4 , \qquad k _ { 2 } = 1 0 ^ { 4 } , \qquad k _ { 3 } = 3 \times 1 0 ^ { 7 } .
$$

Before looking at the problem further we note that, even though it is written as a three-dimensional system, it would be a simple matter to rewrite it in two dimensions, because $y _ { 1 } + y _ { 2 } + y _ { 3 }$ is an invariant and is usually set to a value of 1, by an appropriate choice of the initial values. We always assume this value for $y _ { 1 } + y _ { 2 } + y _ { 3 }$ . Furthermore, if the initial value has non-negative values for each of the three components, then this situation is maintained for all positive times. To see why this is the case, write (104d), (104e) and (104f) in the forms

$$
\begin{array} { c } { \frac { d \left( \exp \left( k _ { 1 } x \right) y _ { 1 } \right) } { d x } = \exp ( k _ { 1 } x ) k _ { 2 } y _ { 2 } y _ { 3 } , } \\ { \frac { d \left( \exp \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x \right) y _ { 2 } \right) } { d x } = \exp \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x \right) F , } \\ { \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } , } \end{array}
$$

where

$$
F = k _ { 1 } y _ { 1 } + \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) y _ { 1 } y _ { 2 } + \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) - k _ { 2 } \right) y _ { 2 } y _ { 3 } + \left( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) - k _ { 3 } \right) y
$$

so that each of $\exp ( k _ { 1 } x ) y _ { 1 }$ , $\exp ( \operatorname* { m a x } ( k _ { 2 } , k _ { 3 } ) x ) y _ { 2 }$ and $y _ { 3 }$ is non-decreasing.

An interesting feature of this problem is that a small perturbation that does not disturb the invariance of $y _ { 1 } + y _ { 2 } + y _ { 3 }$ is damped out rapidly. To see why this is the case, eliminate $y _ { 1 }$ so that the differential equation system in the remaining two components becomes

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 2 } } { d x } = k _ { 1 } ( 1 - y _ { 2 } - y _ { 3 } ) - k _ { 2 } y _ { 2 } y _ { 3 } - k _ { 3 } y _ { 2 } ^ { 2 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = k _ { 3 } y _ { 2 } ^ { 2 } . } \end{array}
$$

The Jacobian matrix, the matrix of partial derivatives, is given by

$$
J ( x ) = \left[ \begin{array} { c c } { - k _ { 1 } - k _ { 2 } y _ { 3 } - 2 k _ { 3 } y _ { 2 } } & { - k _ { 1 } - k _ { 2 } y _ { 2 } } \\ { 2 k _ { 3 } y _ { 2 } } & { 0 } \end{array} \right] ,
$$

and the characteristic polynomial is

$$
\lambda ^ { 2 } + ( k _ { 1 } + k _ { 2 } y _ { 3 } + 2 k _ { 3 } y _ { 2 } ) \lambda + 2 k _ { 3 } y _ { 2 } ( k _ { 1 } + k _ { 2 } y _ { 2 } ) .
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/c2d5ba9e5d7f8de9498dae2edaaa7e3d1771347e634ad8169d8ae066d4bb5de6.jpg)  
Solution and most negative eigenvalue for the Robertson problem

An analysis of the discriminant of (104i) indicates that for $y _ { 2 } , y _ { 3 } \in ( 0 , 1 ]$ , both zeros are real and negative. Along the actual trajectory, one of the eigenvalues of $J ( x )$ , denoted by $\lambda$ , rapidly jumps to a very negative value, with the second eigenvalue retaining a small negative value. Consider a small perturbation $z$ to the solution, so that the solution becomes $y + z$ . Because the two components of $z$ are small we can approximate $f ( y + z )$ by $f ( y ) + ( \partial f / \partial y ) z$ . Hence, the perturbation itself satisfies the equation

$$
{ \left[ \begin{array} { l } { { \cfrac { d z _ { 2 } } { d x } } } \\ { { \cfrac { d z _ { 3 } } { d x } } } \end{array} \right] } = J ( x ) { \left[ \begin{array} { l } { z _ { 2 } } \\ { z _ { 3 } } \end{array} \right] }
$$

and the negative eigenvalues of $J ( x )$ guarantee the decay of the components of $z$ .

The solution to this problem, together with the value of $\lambda$ , is shown in Figure 104(i).
