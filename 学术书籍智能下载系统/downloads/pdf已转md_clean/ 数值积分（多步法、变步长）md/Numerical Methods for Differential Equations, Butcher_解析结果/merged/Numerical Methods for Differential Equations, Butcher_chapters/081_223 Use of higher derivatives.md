# 223 Use of higher derivatives

For many practical problems, it is possible to derive formulae for the second and higher derivatives of $y$ , making use of the formula for $y ^ { \prime }$ given by a differential equation. This opens up many computational options, which can be used to enhance the performance of multistage (Runge–Kutta) and multivalue (multistep) methods. If these higher derivatives are available, then the most popular option is to use them to evaluate a number of terms in Taylor’s theorem. Even though we consider this idea further in Section 25, we present a simple illustrative example here.

Consider the initial value problem

$$
y ^ { \prime } = y x + y ^ { 2 } , \qquad y ( 0 ) = \frac { 1 } { 2 } ,
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/f7d820eb193caa421e353fdb5c7f7c233232d49b25904715a587ef41e7096fef.jpg)  
Errors in problem (223a) using Taylor series with orders $p = 1 , 2 , 3 , 4$

with solution

$$
y ( x ) = \frac { \exp ( \frac { 1 } { 2 } x ^ { 2 } ) } { 2 - \int _ { 0 } ^ { x } \exp ( \frac { 1 } { 2 } x ^ { 2 } ) d x } .
$$

By differentiating (223a) once, twice and a third time, it is found that

$$
\begin{array} { r l } & { y ^ { \prime \prime } = ( x + 2 y ) y ^ { \prime } + y , } \\ & { y ^ { \prime \prime \prime } = ( x + 2 y ) y ^ { \prime \prime } + ( 2 + 2 y ^ { \prime } ) y ^ { \prime } , } \\ & { y ^ { ( 4 ) } = ( x + 2 y ) y ^ { \prime \prime \prime } + ( 3 + 6 y ^ { \prime } ) y ^ { \prime \prime } . } \end{array}
$$

We illustrate the Taylor series method by solving (223a) with output point $\overline { { x } } = 1$ . Using $n$ steps and stepsize $h = 1 / n$ , for $n = 8$ , 16, 32, . . . , $2 ^ { 2 0 }$ , the method was used with orders $p = 1$ , $2$ , 3 and 4. For example, if $p = 4$ , then

$$
\begin{array} { r } { y _ { n } = y _ { n - 1 } + h y ^ { \prime } + \frac { h ^ { 2 } } { 2 } y ^ { \prime \prime } + \frac { h ^ { 3 } } { 6 } y ^ { \prime \prime \prime } + \frac { h ^ { 2 } } { 2 4 } y ^ { ( 4 ) } , } \end{array}
$$

where $y ^ { \prime }$ , $y ^ { \prime \prime }$ , $y ^ { \prime \prime \prime }$ and $y ^ { ( 4 ) }$ are given by (223a), (223b), (223c) and (223d) with $x _ { n - 1 }$ and $y _ { n - 1 }$ substituted for $x$ and $y$ , respectively.

The results for these experiments are shown in Figure 223(i). In each case the error is plotted, where we note that the exact result is

$$
\exp ( \frac { 1 } { 2 } ) / \big ( 2 - \int _ { 0 } ^ { 1 } \exp ( \frac { 1 } { 2 } x ^ { 2 } ) d x \big ) ,
$$

with numerical value 2.04799324543883.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/9f0960271c22ed8239bfdcef9786c39cf73075f1b327da9430c10d9172d3836f.jpg)  
Classification of general method types
