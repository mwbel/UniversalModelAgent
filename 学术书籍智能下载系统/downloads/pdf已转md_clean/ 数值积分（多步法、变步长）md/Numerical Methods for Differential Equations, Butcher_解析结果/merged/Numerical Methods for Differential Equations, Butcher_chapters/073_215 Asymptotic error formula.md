# 215 Asymptotic error formula

In a numerical approximation to the solution to a differential equation, using the Euler method, contributions to the total error are typically produced in every step. In addition to this, there may be errors introduced at the very start of the integration process, due to an inaccuracy in the numerical initial value. We attempt to model the development of this error using an asymptotic approach. That is, we assume that the magnitude of all contributions to the error are bounded in terms of some small parameter. We consider only the limiting case, as all stepsizes tend to zero. Consider a step which advances the approximate solution from $x$ to $x + h$ . Because the local truncation error in this step is approximately $\scriptstyle { \frac { 1 } { 2 } } y ^ { \prime \prime } ( x ) h ^ { 2 }$ , the rate at which errors are being generated, as $x$ increases, will be approximately $y ^ { \prime \prime } ( x ) h$ .

We suppose that for a step starting at $x$ , the stepsize is equal to $H s ( x )$ , where $0 ~ < ~ s ( x ) ~ \le ~ 1$ throughout the integration. We use $H$ as the small parameter, referred to above, and assume that the initial error is equal to a constant, which we denote by $v _ { 0 }$ , times $H$ . Using the integrated form of the differential equation,

$$
y ( x ) = y ( x _ { 0 } ) + \int _ { x _ { 0 } } ^ { x } f ( x , y ( x ) ) d x ,
$$

we write the perturbation to $y$ , defining the numerical approximation, as $y ( x ) + H v ( x )$ . Thus $y ( x ) + H v ( x )$ is approximately equal to

$$
y ( x ) + H v ( x ) = y ( x _ { 0 } ) + H v _ { 0 } + \int _ { x _ { 0 } } ^ { x } { \Big ( } f ( x , y ( x ) + H v ( x ) ) + { \frac { 1 } { 2 } } H s ( x ) y ^ { \prime \prime } ( x ) { \Big ) } d x
$$

Because $H$ is small, we approximate $f ( x , y ( x ) + H v ( x ) )$ by $f ( x , y ( x ) ) +$ $H ( \partial f / \partial y ) v ( x )$ :

$$
\begin{array} { l } { \displaystyle { y ( x ) + H v ( x ) = y ( x _ { 0 } ) + H v _ { 0 } } } \\ { \displaystyle { \qquad + \int _ { x _ { 0 } } ^ { x } \Big ( f ( x , y ( x ) ) + H \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } H s ( x ) y ^ { \prime \prime } ( x ) \Big ) d x . } } \end{array}
$$

Subtract (215a) from (215b), divide the difference by $H$ , and we find

$$
v ( x ) = v _ { 0 } + \int _ { x _ { 0 } } ^ { x } \left( \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } s ( x ) y ^ { \prime \prime } ( x ) \right) d x ,
$$

so that $v$ satisfies the initial value problem

$$
v ^ { \prime } ( x ) = \frac { \partial f } { \partial y } v ( x ) + \frac { 1 } { 2 } s ( x ) y ^ { \prime \prime } ( x ) , \quad v ( x _ { 0 } ) = v _ { 0 } .
$$

We use this result in an attempt to understand the contribution to the total error of local errors introduced at various points on the trajectory. This is done by writing $\Phi ( \xi , { \overline { { x } } } )$ for the solution at $\scriptstyle { \overline { { x } } }$ to the differential equation

$$
w ^ { \prime } ( x ) = \frac { \partial f } { \partial y } w ( x ) , \quad w ( \xi ) = I ,
$$

where $w$ takes values in the space of $N \times N$ matrices. In the special case where $\partial f / \partial y$ is a constant matrix $M$ , the solution is

$$
\Phi ( \xi , \overline { { { x } } } ) = \exp ( ( \overline { { { x } } } - \xi ) M ) .
$$

We can now write the solution at $x = { \overline { { x } } }$ of (215c) in the form

$$
v ( \overline { { { x } } } ) = \Phi ( x _ { 0 } , \overline { { { x } } } ) v _ { 0 } + \frac { 1 } { 2 } \int _ { x _ { 0 } } ^ { \overline { { { x } } } } \Phi ( x , \overline { { { x } } } ) s ( x ) y ^ { \prime \prime } ( x ) d x .
$$

This suggests that $s$ should be chosen, as closely as possible, to maintain a constant value of $\| \Phi ( x , \overline { { x } } ) s ( x ) y ^ { \prime \prime } ( x ) \|$ , if the norm of the total error is to be kept low for a given number of steps performed.
