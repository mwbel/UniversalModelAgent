# 222 Greater dependence on previous values

After the first step of a numerical method has been completed, approximations are available, to be used in the computation of $y _ { n }$ , not only for $y ( x _ { n - 1 } )$ and $y ^ { \prime } ( x _ { n - 1 } )$ but also for $y ( x _ { n - 2 } )$ and $y ^ { \prime } ( x _ { n - 2 } )$ . After further steps, even more previous information is available. Instead of computing $y _ { n }$ in a complicated manner from just the value of $y _ { n - 1 }$ , we could consider making more use of the values computed in past steps, as they become available.

In the generalization of the Euler method, introduced in Subsection 221, we were, in effect, using an approximation to the derivative not at $x _ { n - 1 }$ , but at $x _ { n - \frac { 1 } { 2 } } ~ = ~ x _ { n - 1 } + \frac { 1 } { 2 } h$ . One way of doing a similar adjustment, but using past information, is to note that existing data indicates that the value of $y ^ { \prime } ( x )$ is changing by about $f ( x _ { n - 1 } , y _ { n - 1 } ) - f ( x _ { n - 2 } , y _ { n - 2 } )$ per step. It therefore seems reasonable to assume that, as $x$ advances from $x _ { n - 1 }$ to $\scriptstyle x _ { n - { \frac { 1 } { 2 } } }$ , the approximation to the derivative at $x _ { n - 1 }$ , given as $f ( x _ { n - 1 } , y _ { n - 1 } )$ , should be increased by ${ \begin{array} { l } { { \frac { 1 } { 2 } } \left( f ( x _ { n - 1 } , y _ { n - 1 } ) - f ( x _ { n - 2 } , y _ { n - 2 } ) \right) } \end{array} }$ to obtain a usable approximation to $y ^ { \prime } ( x _ { n - \frac { 1 } { 2 } } )$ . This means that we could approximate the derivative at $x _ { n - { \frac { 1 } { 2 } } }$ , the mid-point of the interval, by $\frac { 3 } { 2 } f ( x _ { n - 1 } , y _ { n - 1 } ) ~ -$ ${ \scriptstyle { \frac { 1 } { 2 } } } f ( x _ { n - 2 } , y _ { n - 2 } )$ , to yield the numerical method

$$
y _ { n } = y _ { n - 1 } + h \bigl ( { \frac { 3 } { 2 } } f ( x _ { n - 1 } , y _ { n - 1 } ) - { \frac { 1 } { 2 } } f ( x _ { n - 2 } , y _ { n - 2 } ) \bigr ) .
$$

This method is an example of a ‘linear multistep method’.

Before we can carry out numerical tests with this method, we first need some procedure for carrying out the first step of the computation. Once $y _ { 1 }$ is calculated, the information that is needed for the computation of $y _ { 2 }$ , and subsequently the solution at later steps, will be available as needed. In the

Errors in the numerical solution of the orbital problem (201d) 2(I)with zero eccentricity through a half period using (222a)

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y1error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y2 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>0.002959760.000374720.000046740.000005830.000000730.00000009</td><td rowspan=1 colspan=1>7.89878.01688.02178.01368.0074</td><td rowspan=1 colspan=1>0.005373470.002241140.000674650.000182940.000047510.00001210</td><td rowspan=1 colspan=1>2.39763.32193.68793.85033.9267</td></tr><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>y3 error</td><td rowspan=1 colspan=1>Ratio</td><td rowspan=1 colspan=1>y4 error</td><td rowspan=1 colspan=1>Ratio</td></tr><tr><td rowspan=1 colspan=1>32641282565121024</td><td rowspan=1 colspan=1>-0.00471581-0.00215339-0.00066358-0.00018155-0.00004734-0.00001208</td><td rowspan=1 colspan=1>2.18993.24513.65513.83513.9194</td><td rowspan=1 colspan=1>-0.00154957-0.00019419-0.00002391-0.00000295-0.00000037-0.00000005</td><td rowspan=1 colspan=1>7.97978.12218.10178.06208.0339</td></tr></table>

experiments we report here, the first step is taken using the Runge–Kutta method introduced in the previous subsection.

The errors are shown in Table 222(I) and we see that, for this problem at least, the results are just as good as for the Runge–Kutta method (221a) and (221b), even though only one derivative is computed in each step. In fact, for components 1 and 4, better than second order convergence is observed.
