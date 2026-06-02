# 424 Variable stepsize

If a sequence of approximations has already been computed using a specific stepsize and, for some reason, a decision is made to alter the stepsize, then a number of options arise as to how this might be done. For example, if a doubling of the stepsize is called for, then the necessary data might already be available without further computation. Halving the stepsize is not so convenient because new approximations to $y ( x )$ and $y ^ { \prime } ( x )$ are required at points intermediate to the information that has already been computed. However, both these are special cases and it is usually required to change the stepsize by a ratio that is perhaps greater than 0.5 and less than 2.0. We consider a very simple model example in which new values are simply found by interpolation and the integration resumed using the modified data. Another approach which we will also consider is where a generalized version of the numerical method is defined specific to whatever sequence of stepsizes actually arises.

We now examine some basic stability questions arising from the interpolation option applied to an Adams method. At the end of step $n$ , besides an approximation to $y ( x _ { n } )$ , approximations are available for $h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } \textrm { -- } h )$ , . . . , $h y ^ { \prime } ( x _ { n } \textrm { -- } ( p \textrm { -- } 1 ) h )$ . We need to replace these derivative approximations by approximations to $r h y ^ { \prime } ( x _ { n } )$ , $r h y ^ { \prime } ( x _ { n } - r h )$ , . . . , $r h y ^ { \prime } ( x _ { n } -$ $( p - 1 ) r h )$ , and these can be evaluated by the interpolation formula

$$
\left[ \begin{array} { c } { r h y ^ { \prime } ( x _ { n } ) } \\ { r h y ^ { \prime } ( x _ { n } - r h ) } \\ { \vdots } \\ { r h y ^ { \prime } ( x _ { n } - ( p - 1 ) r h ) } \end{array} \right] \approx { \cal V } D ( r ) { \cal V } ^ { - 1 } \left[ \begin{array} { c } { h y ^ { \prime } ( x _ { n } ) } \\ { h y ^ { \prime } ( x _ { n } - h ) } \\ { \vdots } \\ { h y ^ { \prime } ( x _ { n } - ( p - 1 ) h ) } \end{array} \right] ,
$$

where $V$ is the Vandermonde matrix

$$
V = { \left[ \begin{array} { l l l l l l } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 2 } & { 2 ^ { 2 } } & { \cdots } & { 2 ^ { p - 1 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { p - 1 } & { ( p - 1 ) ^ { 2 } } & { \cdots } & { ( p - 1 ) ^ { p - 1 } } \end{array} \right] }
$$

and

$$
D ( r ) = \mathrm { d i a g } ( r , r ^ { 2 } , r ^ { 3 } , \ldots , r ^ { p } ) .
$$

The additional errors introduced into the computation by this change of stepsize technique can be significant. However, we are concerned here by the effect on stability. With constant stepsize, the stability of the difference equation system related to the derivative approximations is determined by

the influence matrix

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right]
$$

and because $J$ is nilpotent, the dependence of quantities computed in a particular step eventually becomes insignificant. However, whenever the stepsize is altered by a factor $r$ , the influence matrix becomes

$$
V D ( r ) V ^ { - 1 } J ,
$$

and this is, in general, not nilpotent. If, for example, the interpolation approach with stepsize ratio $r$ is repeated over many steps, then (424a) might not be power-bounded and unstable behaviour will result. In the case $p = 3$ , (424a) becomes

$$
\left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 2 r ^ { 2 } - r ^ { 3 } } } & { { - \frac { 1 } { 2 } r ^ { 2 } + \frac { 1 } { 2 } r ^ { 3 } } } & { { 0 } } \\ { { 4 r ^ { 2 } - 4 r ^ { 3 } } } & { { - r ^ { 2 } + 2 r ^ { 3 } } } & { { 0 } } \end{array} \right] ,
$$

and this is not power-bounded unless $r \leq 1 . 6 9 5 6 2 0 7 6 9 5 5 9 8 6$ , a zero of the polynomial $r ^ { 3 } - r ^ { 2 } - 2$ .

As an example of the alternative technique, in which the numerical method is modified to allow for irregular mesh spacing, consider the BDF3 method. Suppose that approximate solution values are known at $x _ { n - 1 }$ , $x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } )$ and $x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } + ( r _ { 2 } r _ { 1 } ) ^ { - 1 } )$ , where $r _ { 2 }$ and $r _ { 1 }$ are the most recent stepsize ratios. We now wish to compute $y ( x _ { n } )$ using a formula of the form

$$
\begin{array} { r } { y ( x _ { n } ) \approx h \beta y ^ { \prime } ( x _ { n } ) + \alpha _ { 1 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ) + \alpha _ { 2 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } ) ) } \\ { + \alpha _ { 3 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } + ( r _ { 2 } r _ { 1 } ) ^ { - 1 } ) ) . } \end{array}
$$

Using a result equivalent to Hermite interpolation, we find that, to maintain third order accuracy,

$$
\begin{array} { l } { \alpha _ { 1 } = \displaystyle \frac { ( r _ { 2 } + 1 ) ^ { 2 } ( r _ { 1 } r _ { 2 } + r _ { 1 } + 1 ) ^ { 2 } } { ( 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 ) ( r _ { 1 } + 1 ) } , } \\ { \alpha _ { 2 } = - \displaystyle \frac { r _ { 2 } ^ { 2 } ( r _ { 1 } r _ { 2 } + r _ { 1 } + 1 ) ^ { 2 } } { 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 } , } \\ { \alpha _ { 3 } = \displaystyle \frac { r _ { 2 } ^ { 2 } r _ { 1 } ^ { 3 } ( r _ { 2 } + 1 ) ^ { 2 } } { ( 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 ) ( r _ { 1 } + 1 ) } . } \end{array}
$$

Stability of this variable stepsize version of the BDF3 method will hinge on the boundedness of products of matrices of the form

$$
M = \left[ \begin{array} { c c c } { { \alpha _ { 1 } } } & { { \alpha _ { 2 } } } & { { \alpha _ { 3 } } } \\ { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \end{array} \right] ,
$$

where the values of $r _ { 1 }$ and $r _ { 2 }$ for successive members of the product sequence are appropriately linked together.

An extreme case will be where $r _ { 1 }$ and $r _ { 2 }$ are equal and as large as possible, subject to $M$ having bounded powers. It is easy to verify that this greatest rate of continual increase in stepsize corresponds to

$$
r _ { 1 } = r _ { 2 } = r ^ { * } = { \frac { 1 + { \sqrt { 5 } } } { 2 } } .
$$

It is interesting that an arbitrary sequence of stepsize change ratios, in the interval $( 0 , r ^ { * } ]$ , still guarantees stable behaviour.

# Exercises 42

42.1 Let $C ( \theta )$ denote the error constant for the third order linear multistep method (1−(1−θ)z −θz2, 5−θ12 $\begin{array} { r } { ( 1 - ( 1 - \theta ) z - \theta z ^ { 2 } , \frac { 5 - \theta } { 1 2 } + \frac { 2 + 2 \theta } { 3 } + \frac { 5 \theta - 1 } { 1 2 } z ^ { 2 } ) } \end{array}$ 5θ−112 z2). Show that C = $\begin{array} { r } { C = \frac { 1 - \theta } { 2 4 ( 1 + \theta ) } } \end{array}$ .

42.2 Show that weakly stable behaviour is experienced with the linear multistep method $( 1 - z ^ { 3 } , \frac { 3 } { 8 } ( 1 + z ) ^ { 3 } )$ .

42.3 Show that the norm of the product of an arbitrary sequence of matrices of the form (424b) is bounded as long as each $r$ lies in the interval $[ 0 , r ^ { * } ]$ , where $r ^ { * } \approx 1 . 6 9 5 6 2 0 7 6 9 5 5 9 8 6$ .
