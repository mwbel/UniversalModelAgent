# 254 The use of $f$ derivatives

In this subsection, we consider an autonomous differential equation system $y ^ { \prime } ( x ) = f ( y ( x ) )$ . As we remarked in Subsection 224, the use of derivatives of $f$ is more general than the use of higher derivatives of $y$ . Methods that use $f ^ { \prime }$ directly have mainly been proposed for the solution of stiff problems by onestep methods. If an implicit Runge–Kutta method is used, the implementation requires the solution of non-linear equations, typically by a Newton-type method. It was proposed by Rosenbrock (1963) that the Newton iterations could be replaced by a single iteration involving the inverse of a matrix such as $I - h \gamma f ^ { \prime } ( y ( x _ { n - 1 } ) )$ . Methods formed in this way use this linear operation as an intrinsic part of the order requirement for the method. We give a single example in which modified derivatives $F _ { 1 }$ and $F _ { 2 }$ , and the final result at the end of a step, are computed by the formulae

$$
\begin{array} { r l } & { \left( I - h \big ( 1 - \frac { \sqrt { 2 } } { 2 } \big ) f ^ { \prime } ( y _ { n - 1 } ) \right) F _ { 1 } = f ( y _ { n - 1 } ) , } \\ & { \left( I - h \big ( 1 - \frac { \sqrt { 2 } } { 2 } \big ) f ^ { \prime } ( y _ { n - 1 } ) \right) F _ { 2 } = f \Big ( y _ { n - 1 } + h \big ( \frac { \sqrt { 2 } } { 2 } - \frac { 1 } { 2 } \big ) F _ { 1 } \Big ) , } \\ & { \qquad y _ { n } = y _ { n - 1 } + h F _ { 2 } . } \end{array}
$$

Methods of various orders have been derived by Rosenbrock and others. These are known collectively as Rosenbrock methods, although the ambiguous name ‘implicit Runge–Kutta methods’ is sometimes applied to them.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/f497cd364d3071fb5ed754c21de6505f2a4bd04e1331e08fb9557c9ef3f9f68e.jpg)  
Predictor–corrector multiderivative methods

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/8922fc1e84669bce4d380397aae166d9f2674a29b0b22cf687525c3d0e5cf123.jpg)  
Rosenbrock method given by (254a)–(254c)
