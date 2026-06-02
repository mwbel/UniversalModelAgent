# 533 An example of the algebraic approach to order

We will consider the modification of a Runge–Kutta method given by (502c). Denote the method by $M$ and a possible starting method by $S$ . Of the two quantities passed between steps, the first is clearly intended to approximate the exact solution and we shall suppose that the starting method for this approximation is the identity method, denoted by 1. The second approximation is intended to be close to the scaled derivative at a nearby point and we will assume that this is represented by $\theta : T ^ { \# } \to \mathbb { R }$ , where $\theta ( \varnothing ) = 0$ , $\theta ( \tau ) = 1$ . The values of $\theta ( t )$ for other trees we will keep as parameters to be chosen. Are there possible values of these parameters for which $M$ has order $p = 4$ , relative to $S$ ?

Calculations to verify order $p = 4$ for (502c)   

<table><tr><td>i</td><td>01</td><td>2</td><td>3</td><td></td><td></td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>ti</td><td>D.</td><td></td><td>：</td><td>?</td><td></td><td>Y</td><td>！</td><td>丫</td><td>：</td></tr><tr><td>S1</td><td>10</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S2</td><td>01</td><td>0</td><td></td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td></tr><tr><td>m1</td><td>1 0</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>n1D</td><td>0 1</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>m2</td><td>1</td><td>1 1</td><td>02</td><td>103</td><td>-104</td><td>-105</td><td>-106</td><td>-107</td><td>-108</td></tr><tr><td>n2D</td><td>0</td><td>1 1</td><td></td><td>4</td><td>-102</td><td></td><td>-02</td><td>-103</td><td>-104</td></tr><tr><td>n3</td><td>11</td><td>1+02</td><td></td><td>1+004-20</td><td></td><td>1+05</td><td>06-102</td><td>07-103</td><td>08-104</td></tr><tr><td>nD</td><td>01</td><td>1</td><td>1</td><td></td><td>1+02</td><td>1</td><td>1+02 +120</td><td>2+0</td><td>04-102</td></tr><tr><td>S</td><td>11 01</td><td>1 1</td><td>1 i</td><td></td><td>-102</td><td>1 </td><td>0</td><td>1 -103</td><td>120 -104</td></tr><tr><td>E1</td><td>11</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td>E2</td><td>01</td><td>1+02</td><td>1+202 +03</td><td></td><td>+02 +04</td><td>1+302</td><td>+0 +303+05+03+04+06+204+07+04+08</td><td>+0</td><td>+0</td></tr></table>

We will start with $\xi _ { 1 } = 1$ and $\xi _ { 2 } = \theta$ and compute in turn $\eta _ { 1 }$ , $\eta _ { 1 } D$ , $\eta _ { 2 }$ , $\eta _ { 2 } D$ , $\eta _ { 3 }$ , $\eta _ { 3 } D$ and finally the representatives of the output approximations, which we will write here as $\widehat { \xi _ { 1 } }$ and $\widehat { \xi _ { 2 } }$ . The order requirements are satisfied if and only if values of the free $\theta$ values can be chosen so that $\widehat { \xi _ { 1 } } = E \xi _ { 1 }$ and $\widehat { \xi _ { 2 } } = E \xi _ { 2 }$ . Reading from the matrix of coefficients for the method, we see that

$$
\begin{array} { r l r l } & { \eta _ { 1 } = \xi _ { 1 } , \qquad } & & { \eta _ { 2 } = \xi _ { 1 } - \frac { 1 } { 4 } \xi _ { 2 } + \frac { 3 } { 4 } \eta _ { 1 } D , } \\ & { \eta _ { 3 } = \xi _ { 1 } + \xi _ { 2 } - 2 \eta _ { 1 } D + 2 \eta _ { 2 } D , } \\ & { \widehat { \xi } _ { 1 } = \xi _ { 1 } + \frac { 1 } { 6 } \eta _ { 1 } D + \frac { 2 } { 3 } \eta _ { 2 } D + \frac { 1 } { 6 } \eta _ { 3 } D , \qquad } & & { \widehat { \xi } _ { 2 } = \eta _ { 2 } D . } \end{array}
$$

The details of these calculations are shown in Table 533(I). Comparing the entries in the $\widehat { \xi _ { 1 } }$ and $E \xi _ { 1 }$ rows in this table, we see that we get agreement if and only if $\theta _ { 2 } = - \frac { _ 1 } { 2 }$ . Moving now to the $\widehat { \xi _ { 2 } }$ and $E \xi _ { 2 }$ rows, we find that these agree only with specific choices of $\theta _ { 3 }$ , $\theta _ { 4 }$ , . . . , $\theta _ { 8 }$ . Thus the method has order 4 relative to $S$ for a unique choice of $\xi _ { 2 } = \theta$ , which is found to be

$$
\begin{array} { r } { [ \theta _ { 0 } ~ \theta _ { 1 } ~ \theta _ { 2 } ~ \theta _ { 3 } ~ \theta _ { 4 } ~ \theta _ { 5 } ~ \theta _ { 6 } ~ \theta _ { 7 } ~ \theta _ { 8 } ] = [ 0 ~ 1 ~ - \frac { 1 } { 2 } ~ \frac { 1 } { 4 } ~ \frac { 1 } { 8 } ~ - \frac { 1 } { 8 } ~ - \frac { 1 } { 1 6 } ~ - \frac { 7 } { 4 8 } ~ - \frac { 7 } { 9 6 } ] . } \end{array}
$$

It might seem from this analysis, that a rather complicated starting method is necessary to obtain fourth order behaviour for this method. However, the method can be started successfully in a rather simple manner. For $S _ { 1 }$ , no computation is required at all and we can consider defining $S _ { 2 }$ using the generalized Runge–Kutta method

$$
{ \frac { - { \frac { 1 } { 2 } } \ - { \frac { 1 } { 2 } } \ } { 0 \ { \left| \begin{array} { l l } { \ 0 } & { 1 } \end{array} \right. } } } .
$$

This starter, combined with a first step of the general linear method $M$ , causes this first step of the method to revert to the Runge–Kutta method (502b), which was used to motivate the construction of the new method.
