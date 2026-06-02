# 204 Calculations with the implicit Euler method

As we have pointed out, the Euler method approximates the integral of $y ^ { \prime } ( x )$ , over each subinterval $[ x _ { n - 1 } , x _ { n } ]$ , in terms of the width of the interval, multiplied by an approximation to the height of the integrand at the left-hand end. We can consider also the consequences of using the width of this interval, multiplied by the height at the right-hand end.

This would mean that the approximation at $x _ { 1 }$ would be defined by $y ( x _ { 1 } ) \approx y _ { 1 }$ , where $y _ { 1 } = y _ { 0 } + h f ( x _ { 1 } , y _ { 1 } ) $ . This results in what is known as the ‘implicit Euler method’. The complication is, of course, that the solution approximation at the end of the step is defined not by an explicit formula, but as the solution to an algebraic equation.

For some problems, we can evaluate by simple (‘fixed point’) iteration. That is, we calculate a sequence of approximations $Y ^ { \left[ 0 \right] }$ , $Y ^ { \left[ 1 \right] }$ , $Y ^ { \left[ 2 \right] }$ , . . . using the formula

$$
Y ^ { [ k ] } = y _ { 0 } + h f ( x _ { 1 } , Y ^ { [ k - 1 ] } ) , \quad k = 1 , 2 , 3 , \dots x .
$$

Assuming that the sequence of approximations converges, to within a required tolerance, to a limiting value $Y$ , then we take this limit as the value of $y _ { 1 }$ . The starting value in the sequence may be taken, for simplicity and convenience, as $y _ { 0 }$ .

Some results for this method, as applied to the initial value problem (201a), are given in Table 204(I). In this table, all approximations are made for the solution at $x = 0 . 5$ and, for each number of steps $n$ , the calculation is carried out using both the Euler method and the implicit form of the Euler method. The total errors for the two methods are shown. In the case of the implicit method, the total number of iterations to achieve convergence, to within a tolerance of $1 0 ^ { - 6 }$ , is also given. If a tolerance as high as $1 0 ^ { - 4 }$ had been specified, there would have been only about two, rather than three, iterations per step, but the cost would still be approximately twice as great as for the explicit Euler method.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/613b726b7fefffea7015667200c5194821c31402f8ff8d38599c49688745950f.jpg)  
Norm error against $n ^ { - 1 }$ for the ‘mildly stiff’ problem (203a) using the method (204a)

As we see from these results, there is no advantage in the implicit form of the Euler method, in the case of this problem. On the contrary, there is a serious disadvantage, because of the very much greater computing cost, as measured in terms of $f$ evaluations, for the implicit as compared with the explicit form of the method.

For stiff problems, such as that given by (203a), the implicit Euler method shows itself to advantage. Since this problem is linear, it is possible to write the answer for the approximation computed at the end of a step explicitly. In the step going from $x _ { 0 }$ to $x _ { 1 } = x _ { 0 } + h$ , with solution approximations going from $y _ { 0 } = [ ( y _ { 0 } ) _ { 1 } , ( y _ { 0 } ) _ { 2 } ] ^ { 1 }$ to $y _ { 1 } = [ ( y _ { 1 } ) _ { 1 } , ( y _ { 1 } ) _ { 2 } ] ^ { 1 }$ , we have the relations between these quantities given by

$$
\stackrel { \scriptscriptstyle ( y _ { 1 } ) _ { 1 } } { \scriptscriptstyle ( y _ { 1 } ) _ { 2 } } \stackrel { \scriptscriptstyle } { = } h \left[ \stackrel { \displaystyle - 1 6 } { \displaystyle 1 2 } \quad \stackrel { \mathrm { \scriptsize ~ 1 2 } } { \scriptscriptstyle - 9 } \right] \stackrel { \displaystyle } { \left[ ( y _ { 1 } ) _ { 2 } \right] } + \stackrel { \displaystyle \left[ ( y _ { 0 } ) _ { 1 } \right] } { \scriptscriptstyle ( y _ { 0 } ) _ { 2 } } + h \left[ \stackrel { \displaystyle 1 6 \cos ( x _ { 1 } ) - 1 3 \sin ( x _ { 1 } ) } { \displaystyle - 1 1 \cos ( x _ { 1 } ) + 9 \sin ( x _ { 1 } ) } \right] ,
$$

so that

$$
\left[ 1 + 1 6 h - 1 2 h \right] \left[ ( y _ { 1 } ) _ { 1 } \right] = \left[ ( y _ { 0 } ) _ { 1 } + 1 6 h \cos ( x _ { 1 } ) - 1 3 h \sin ( x _ { 1 } ) \right] ,
$$

and the new approximation is found using a linear equation solution.

The results for this calculation, presented in Figure 204(i), show that this method is completely satisfactory, for this problem. Note that the largest stepsize used is $\pi$ , so that only a single step is taken.

# Exercises 20

20.1 On a copy of Figure 200(i), plot the points corresponding to the solution computed by the Euler method with $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 4 } } \end{array}$ , $\textstyle h = { \frac { 1 } { 5 } }$ .

20.2 Write the initial value problem (200b) in the form

$$
\begin{array} { l l } { { \frac { d x } { d t } \ = \ 1 + x , \qquad } } & { { x ( 0 ) \ = \ 0 , } } \\ { { \frac { d y } { d t } \ = \ y - 2 x y ^ { 2 } , \qquad } } & { { y ( 0 ) \ = \ \frac 1 2 . } } \end{array}
$$

Using this alternative formulation, recalculate the solution, using five equal steps of the Euler method, from $t = 0$ to $t = \ln 2$ . Plot the solution points after each step on a graph in the $( x , y )$ plane.

20.3 Continue the calculations in Table 201(I) to the point $x = 1$ .

20.4 It is known that $E = \textstyle { \frac { 1 } { 2 } } ( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } ) - 1 / { \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } }$ , the total energy, and $A = y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 }$ , the angular momentum, are invariants of the system (201d); that is, for any value of $x$ the values of each of these will be equal respectively to the values they had at the initial time. The quality of a numerical method for solving this problem can be measured by calculating by how much these theoretical invariants actually change in the numerical computation. Repeat the calculations in Tables 201(II), 201(III) and 201(IV) but with the deviation in the values of each of these quantities used in place of the errors.
