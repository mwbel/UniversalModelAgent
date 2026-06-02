# 134 Iterative solutions of a polynomial equation

We discuss the possible solution of the polynomial equation

$$
x ^ { 2 } - 2 = 0 .
$$

Of course this is only an example, and a similar discussion would be possible with other polynomial equations. Consider the difference equations

$$
\begin{array} { l l l } { { y _ { n } = y _ { n - 1 } - \displaystyle \frac { 1 } { 2 } y _ { n - 1 } ^ { 2 } + 1 , } } & { { y _ { 0 } = 0 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = y _ { n - 1 } - \displaystyle \frac { 1 } { 2 } y _ { n - 1 } ^ { 2 } + 1 , } } & { { y _ { 0 } = 4 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = y _ { n - 1 } - y _ { n - 1 } ^ { 2 } + 2 , } } & { { y _ { 0 } = \displaystyle \frac { 3 } { 2 } , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = \displaystyle \frac { y _ { n - 1 } } { 2 } + \displaystyle \frac { 1 } { y _ { n - 1 } } , } } & { { y _ { 0 } = 1 0 0 , } } \\ { { \ } } & { { \ } } \\ { { y _ { n } = \displaystyle \frac { y _ { n - 1 } y _ { n - 2 } + 2 } { y _ { n - 1 } + y _ { n - 2 } } , } } & { { y _ { 0 } = 0 , } } \end{array}
$$

Note that each of these difference equations has $\sqrt { 2 }$ as a stationary point. That is, each of them is satisfied by $y _ { n } = { \sqrt { 2 } }$ , for every $n$ . Before commenting further, it is interesting to see what happens if a few values are evaluated numerically for each sequence. These are shown in Table 134(I).

Note that (134a) seems to be converging to $\sqrt { 2 }$ , whereas (134b) seems to have no hope of ever doing so. Of course the starting value, $y _ { 0 }$ , is the distinguishing feature, and we can perhaps investigate which values converge and which ones do not. It can be shown that the fate of the iterates for various starting values can be summarized as follows:

The first few terms in the solutions of some difference equations   

<table><tr><td></td><td></td><td>Equation (134a）Equation (134b） Equation (134c) Equation (134d) Equation (134e)</td><td></td><td></td></tr><tr><td>yo</td><td>0.0000000000</td><td>4.0000000000</td><td>1.50000000001.000000×10²0.0000000000</td><td></td></tr><tr><td>y1</td><td>1.0000000000 -3.0000000000</td><td></td><td>1.25000000005.001000×101.0000000000</td><td></td></tr><tr><td>y2</td><td>1.5000000000 -6.5000000000</td><td></td><td>1.68750000002.502500×102.0000000000</td><td></td></tr><tr><td>Y3</td><td>1.3750000000 -2.662500×10</td><td></td><td>0.8398437500 1.255246×101.3333333333</td><td></td></tr><tr><td>y4</td><td></td><td></td><td>1.4296875000 -3.800703×1022.1345062256 6.3558946949 1.4000000000</td><td></td></tr><tr><td>Y5</td><td></td><td></td><td>1.4076843262 -7.260579×104 -0.4216106015 3.3352816093 1.4146341463</td><td></td></tr><tr><td>y6</td><td></td><td></td><td></td><td>1.4168967451 -2.635873×1091.4006338992 1.9674655622 1.4142114385</td></tr></table>

$$
\begin{array} { l l } { y _ { 0 } \in \{ - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } \} } & { { \mathrm { C o n v e r g e n c e ~ t o ~ } } x = - { \sqrt { 2 } } } \\ { y _ { 0 } \in ( - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } ) { : } } & { { \mathrm { C o n v e r g e n c e ~ t o ~ } } x = { \sqrt { 2 } } } \\ { y _ { 0 } \notin [ - { \sqrt { 2 } } , 2 + { \sqrt { 2 } } ] { : } } & { { \mathrm { D i v e r g e n c e } } } \end{array}
$$

Note that the starting value $y _ { 0 } = - { \sqrt { 2 } }$ , while it is a fixed point of the mapping given by (134a), is unstable; that is, any small perturbation from this initial value will send the sequence either into instability or convergence to $+ \sqrt { 2 }$ . A similar remark applies to $y _ { 0 } = 2 + { \sqrt { 2 } }$ , which maps immediately to $y _ { 1 } = - { \sqrt { 2 } }$ .

The difference equation (134c) converges to $\pm \sqrt { 2 }$ in a finite number of steps for $y _ { 0 }$ in a certain countable set; otherwise the sequence formed from this equation diverges.

Equation (134d) is the Newton method and converges quadratically to $\sqrt { 2 }$ for any positive $y _ { 0 }$ . By quadratic convergence, we mean that $| y _ { n } - { \sqrt { 2 } } |$ divided by $| y _ { n - 1 } - { \sqrt { 2 } } | ^ { 2 }$ is bounded. In fact, in the limit as $n \longrightarrow \infty$ ,

$$
{ \frac { y _ { n } - { \sqrt { 2 } } } { ( y _ { n - 1 } - { \sqrt { 2 } } ) ^ { 2 } } } \to { \frac { \sqrt { 2 } } { 4 } } .
$$

The iteration scheme given by (134e) is based on the secant method for solving non-linear equations. To solve $\phi ( y ) ~ = ~ 0$ , $y _ { n }$ is found by fitting a straight line through the two points $( y _ { n - 2 } , \phi ( y _ { n - 2 } ) )$ and $( y _ { n - 1 } , \phi ( y _ { n - 1 } ) )$ and defining $y _ { n }$ as the point where this line crosses the horizontal axis. In the case $\phi ( y ) = y ^ { 2 } - 2$ , this results in (134e).

It is interesting to ask if there exists an ‘order’ $k$ for this sequence. In other words, assuming that convergence is actually achieved, does $k \geq 1$ exist such that

$$
\frac { | y _ { n } - { \sqrt { 2 } } | } { | y _ { n - 1 } - { \sqrt { 2 } } | k }
$$

has a limiting value as $n \to \infty$ ? For the secant method $k$ does exist, and has the value $\textstyle k = { \frac { 1 } { 2 } } ( { \sqrt { 5 } } + 1 )$ .
