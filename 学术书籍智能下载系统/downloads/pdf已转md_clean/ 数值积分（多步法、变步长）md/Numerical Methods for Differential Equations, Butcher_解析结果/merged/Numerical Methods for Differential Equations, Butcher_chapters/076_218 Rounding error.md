# 218 Rounding error

The mathematical analysis of the behaviour of a numerical method, such as the Euler method, is usually idealized to exact arithmetic. However, in practical computation, the nature of computer arithmetic can play a significant, and possibly overwhelming, part. Thus the discussion of error growth, given in Subsection 212, is deficient in this respect. Let $\alpha _ { n }$ denote the total error in the result, computed at step $n$ , and $\beta _ { n }$ the corresponding error in the derivative, computed at this step. Thus,

$$
\begin{array} { l } { \alpha _ { n } = y ( x _ { n } ) - y _ { n } , } \\ { \beta _ { n } = f ( x _ { n } , y ( x _ { n } ) ) - f ( x _ { n } , y _ { n } ) . } \end{array}
$$

The sequences of exact and approximate values are interrelated by

$$
\begin{array} { c } { { y _ { n } = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) - r _ { n } , } } \\ { { y ( x _ { n } ) = y ( x _ { n - 1 } ) + h f ( x _ { n - 1 } , y ( x _ { n - 1 } ) ) + l _ { n } , } } \end{array}
$$

where $r _ { n }$ is the rounding error, otherwise known as the round-off error, committed in this step, and $l _ { n }$ is the truncation error that we have already discussed.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/52580f2b56f66bc5b51ce7203fa0b4edfacc83f9dee48f6b5e13c783af2c35a9.jpg)  
Schema showing effects of rounding error

These lead to the difference equation

$$
\alpha _ { n } = \alpha _ { n - 1 } + h \beta _ { n - 1 } + l _ { n } + r _ { n } .
$$

Even though we know something about $l _ { n }$ , in particular that it behaves asymptotically like a constant times $h ^ { 2 }$ , very little is known about $r _ { n }$ .

A somewhat pessimistic model of rounding error would bound its magnitude in terms of the magnitude of $y _ { n }$ . It would also assume that its sign (or direction, in the high-dimensional case) is always such as to reinforce errors already accumulated. Bounding the magnitude of the rounding error, in terms of the magnitude of $y _ { n }$ , is quite reasonable, because the greatest contribution to the total rounding error will usually arise from the final addition of $h f ( x _ { n - 1 } , y _ { n - 1 } )$ to $y _ { n - 1 }$ . Of these two terms, $y _ { n - 1 }$ is usually far the greater in magnitude. Thus, the rounding error will have a magnitude approximately equal to $\| y _ { n - 1 } \| \epsilon \approx | | y _ { n } | | \epsilon$ , where $\epsilon$ is the machine round-off constant defined as the smallest positive number which satisfies the inequality $1 + \epsilon > 1$ , in computer arithmetic.

The other aspect of this model, that rounding errors always conspire to produce the worst possible outcome, is, of course, too severe an assumption. An alternative is to treat the rounding errors arising in different steps as being independently and randomly distributed.

The pessimistic assumption adds an additional term to the accumulated error of $C h ^ { - 1 }$ , for $C$ a constant, because the local error will be more or less the same in each step and the number of steps is inversely proportional to $h$ . The randomness assumption will lead to the rounding error contribution being replaced by a term of the form $C h ^ { - 1 / 2 }$ . A detailed analysis of the probabilistic model of rounding error in initial value problem calculations is presented in Henrici (1962).

Under either the deterministic or the probabilistic model, it is clear that the conclusion of the convergence of computed solutions to the exact solution, as the stepsize tends to zero, will have to be reconsidered. If truncation error alone was significant, the error behaviour would be very much as shown by the dashed line in Figure 218(i). On the other hand, if there were no appreciable

# α Simple version of Euler

<table><tr><td>for i = 1:n</td></tr><tr><td></td></tr><tr><td>term = h*f(y);</td></tr><tr><td></td></tr><tr><td>y = y + term; end</td></tr></table>

β Sophisticated version of Euler using compensated summation truncation error, the accumulated rounding error would be very much like the dotted line. The solid line shows the combined effect of these two sources of error. Since a logarithmic scale is used for both stepsize and error, the two individual error components will be approximately straight lines whose slope will depend on the order of the method, one in the case of Euler, and whether the pessimistic or the probabilistic model of rounding error growth is assumed.

<table><tr><td>Z = zeros(size(y));</td><td></td></tr><tr><td>for i = 1:n</td><td></td></tr><tr><td>term = h*f(y)+ Z;</td><td></td></tr><tr><td>newy = y + term;</td><td></td></tr><tr><td>Z = term - (newy - y);</td><td></td></tr><tr><td>y = newy;</td><td></td></tr><tr><td>end</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

Rather than attempting to carry out this analysis, we remark that it is possible, to a large extent, to overcome the worst effects of the accumulation of rounding errors, as steps are computed in sequence. This is done by estimating the value of $r _ { n }$ in any particular step, and then adding this to the value of $h f ( x _ { n } , y _ { n } )$ , before this is added in the following step. This improved technique, which can be used for many situations involving the summation of a large number of small numbers, is sometimes known as the Gill–Møller algorithm (Gill, 1951; Møller, 1965, 1965a), but is now more often referred to as ‘compensated summation’. An analysis, in the context of floating point arithmetic, was carried out by Kahan (1965) and particular applications to initial value problems were considered in Vitasek (1969). A modern survey of compensated summation, with further references, is available in Higham (1993).

We show how this is done by presenting two fragments of MATLAB code, of which the first, referred to as Algorithm $2 1 8 \alpha$ , computes the solution naively, and the second, Algorithm $2 1 8 \beta$ , makes the improvement that we have referred to. In each case, the problem is assumed to be written in autonomous form; this is convenient because, if it were not the case, the updating of the $\mathbf { x }$ variable would need to be done in a similar way to the y variable. It is assumed that the statement f(y) yields the value of the derivative vector for given y.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/6684464ee5f54006d07a9e530b3cd94d3d26d9b0bfd8ecdfdd314d70958c1298.jpg)  
Errors for naive (◦) and sophisticated ( $\bullet$ ) forms of the Euler method

Although each of these algorithms is coded to work in a vector setting, it will be adequate, for illustrative purposes, to confine ourselves to numerical experiments with a scalar problem. Specifically, we use the problem given by (201a), using a sequence of stepsizes, $h = 2 ^ { - 2 }$ , $h = 2 ^ { - 3 }$ , $\cdot \cdot \cdot$ , $h = 2 ^ { - 2 4 }$ . Each of the two algorithms was used, and the errors were plotted on the same graph, which is presented in Figure 218(ii). To avoid the necessity of using abnormally small stepsizes, before rounding error becomes significant, the calculations were performed in an arithmetic system in which it was possible to force an accuracy of only nine significant decimal digits. It is seen that the naive form of the method produces results that are increasingly infected by rounding for stepsizes less than $2 ^ { - 1 5 }$ . For the Gill–Møller (compensated summation) algorithm, on the other hand, there is no sign of accumulated rounding error at all. It can also be seen that the naive version of the method gives results much as was anticipated in Figure 218(i).

To give additional insight into how compensated summation works, a further calculation on the initial value problem (201a) was performed, using modified arithmetic in which the computations were consistently rounded to three significant decimal digits. Using the notation in Algorithm $2 1 8 \beta$ , these results are shown in Table 218(I) for the first ten steps, using stepsize 0.01. The crucial step in the calculation, the evaluation of $_ { \textrm { z } }$ , can be expected to be performed with little or no error. The reason for this is that each of the two subtractions, newy - y and term - (newy - y), has operands which are close to being equal, and these subtractions are usually performed without rounding error. Exceptions may occur when two operands are almost equal, but where the exponent parts of the floating point representations differ by one; but this situation will be relatively rare. If we also concede that the errors generated in the addition of two small quantities, in the statement term $=$ $\mathtt { h * f } \left( \mathtt { y } \right) ~ + ~ z$ , are not of great significance, then we see that, although y might not be accurate as an approximation to y at the end of a step, the value of y $+ \ z$ , if it could be evaluated accurately, would be a very good approximation, because the statement term - (newy - y) effectively increases the old value of $\texttt { y + z }$ by $\mathtt { h } * \mathtt { f } \left( \mathtt { y } \right)$ , to form the new value of $\texttt { y + z }$ .

Ten steps of sophisticated Euler to three significant decimals   

<table><tr><td>X</td><td>y</td><td>h*f(y)</td><td>term</td><td>newy</td><td>Z</td></tr><tr><td>0.00</td><td>1.00</td><td>0.0100</td><td>0.0100</td><td>1.01</td><td>0.0000</td></tr><tr><td>0.01</td><td>1.01</td><td>0.0102</td><td>0.0102</td><td>1.02</td><td>0.0002</td></tr><tr><td>0.02</td><td>1.02</td><td>0.0104</td><td>0.0106</td><td>1.03</td><td>0.0006</td></tr><tr><td>0.03</td><td>1.03</td><td>0.0106</td><td>0.0112</td><td>1.04</td><td>0.0012</td></tr><tr><td>0.04</td><td>1.04</td><td>0.0108</td><td>0.0120</td><td>1.05</td><td>0.0020</td></tr><tr><td>0.05</td><td>1.05</td><td>0.0110</td><td>0.0130</td><td>1.06</td><td>0.0030</td></tr><tr><td>0.06</td><td>1.06</td><td>0.0112</td><td>0.0142</td><td>1.07</td><td>0.0042</td></tr><tr><td>0.07</td><td>1.07</td><td>0.0114</td><td>0.0156</td><td>1.09</td><td>-0.0044</td></tr><tr><td>0.08</td><td>1.09</td><td>0.0116</td><td>0.0072</td><td>1.10</td><td>-0.0028</td></tr><tr><td>0.09</td><td>1.10</td><td>0.0118</td><td>0.0090</td><td>1.11</td><td>-0.0010</td></tr><tr><td>0.10</td><td>1.11</td><td></td><td></td><td></td><td></td></tr></table>

As further evidence in support of the use of compensated summation, we present the results of an extended calculation, with the same three decimal arithmetic system used to produce Table 218(I). In this calculation, 100 steps were taken, so that the numerical approximations are now extended to the interval $[ 0 , 1 ]$ . Shown in Figure 218(iii) are the computed values of y, found using each of Algorithms $2 1 8 \alpha$ and $2 1 8 \beta$ . In each case a rounding-free version of the same results was subtracted to isolate the error due to rounding alone. The sum of y and $_ { \textrm { z } }$ , for the sophisticated algorithm, is also given. Because the values of these quantities vary widely, a scale is used for which a value $\epsilon$ corresponds to a rounding error of $\epsilon \exp ( 1 0 ^ { 4 } | \epsilon | )$ . It is clear that, in this example, the sophisticated version of Euler performs overwhelmingly better than the crude version.

# Exercises 21

21.1 For the differential equation $y ^ { \prime } = y$ , $y ( 0 ) = 1$ , find the function $\widetilde { y }$ , given by (212a), where $n = 4$ and $[ x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ] = [ 0 , { \scriptstyle { \frac { 1 } { 4 } } } , { \scriptstyle { \frac { 1 } { 2 } } } , { \scriptstyle { \frac { 3 } { 4 } } } , 1 ]$  and $\widetilde y ( 0 ) = y ( 0 )$ .

21.2 For the same problem as in Exercise 21.1, but with $n$ an arbitrary positive integer and $x _ { k } ~ = ~ k / n$ , for $k = 0 , 1 , 2 , \ldots , n$ , find the value of $\widetilde { y } ( 1 ) - y ( 1 )$ and show that this converges to $0$ as $n \longrightarrow \infty$ .

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/2796455e5c95609983dd999621d1cbf3dc3267451a92806a518806cf91798f27.jpg)  
Accumulation of rounding errors in low accuracy calculations with sophisticated Euler, showing y (dashed line) and y $+ z$ (solid line); also, for comparison, crude Euler (dotted line)

21.3 Prove (211a), using integration by parts.

21.4 Assuming that $L = 0$ , prove (212f), using induction on $k$

21.5 Repeat the calculation in Subsection 218, but making the correction in the Gill–Møller algorithm only every second step.
