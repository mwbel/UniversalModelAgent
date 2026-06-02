# 325 Methods of order 5

We saw in Theorem 324B that for orders greater than 4, $s = p$ is impossible. Hence, we assume that $s = 6$ . We assume the $D ( 1 )$ condition and the $C ( 2 )$ condition applied to all stages except the second. We also need to assume the subsidiary conditions $\begin{array} { r } { b _ { 2 } = \sum _ { i = 3 } ^ { 5 } b _ { i } ( 1 - c _ { i } ) a _ { i 2 } = 0 } \end{array}$ . These conditions dispose of all conditions except those associated with the trees

$$
\bar { \cdot } , \bar { \bf \Xi } _ { \ast } , \bar { \bf \Xi } _ { \ast } , \bar { \bf \Xi } _ { \ast } \Psi , \bar { \bf \Xi } _ { \ast } \Psi .
$$

The second and third of these turn out to be consequences of the $D ( 1 )$ and $C ( 2 )$ conditions, and we find that some of the elements in the final row can be evaluated in two different but consistent ways. The condition associated with $\gamma$ can be replaced by the difference of this condition and the automatically satisfied condition associated with ; see (325h) below. This last modification of the order conditions we actually solve has the advantage that it removes the last row of the $A$ matrix from the calculation until, at the end, we compute this row using the $D ( 1 )$ condition.

Collecting these comments together, we summarize the defining equations for a fifth order method. Where we write ‘choose’ one of the coefficients, we mean that it can be set to an arbitrary value, excluding only a finite set of possibilities. We do not state in detail what constitute the exceptional cases, but these can be identified with little difficulty:

$$
\begin{array} { c } { { c _ { 6 } = 1 , } } \\ { { \mathrm { C h o o s e ~ } c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 6 } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , ~ k = 1 , 2 , . . . , 5 , } } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 2 } ^ { i - 1 } a _ { i j } c _ { j } = \frac { 1 } { 2 } c _ { i } ^ { 2 } , ~ i = 3 , 4 , 5 , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { i j } = c _ { i } , ~ i = 2 , 3 , 4 , 5 , } } \\ { { \displaystyle \sum _ { i = 3 } ^ { 5 } b _ { i } ( 1 - c _ { i } ) a _ { i 2 } = 0 , } } \\ { { \displaystyle b _ { 3 } ( 1 - c _ { 5 } ) a _ { 5 4 } c _ { 1 } ( c _ { 4 } - c _ { 5 } ) = \frac { 1 } { 6 0 } - \frac { c _ { 3 } } { 2 4 } , } } \\ { { \displaystyle \sum _ { i = j + 1 } ^ { 5 } b _ { i } a _ { i j } = b _ { j } ( 1 - c _ { i } ) , ~ j = 1 , 2 , 3 , 4 , 5 . } } \end{array}
$$

The following schema shows which of these various defining equations are used in the choice of particular coefficients of the method:

<table><tr><td>0 (325b) (325b) (325b) (325b)</td><td>(325f) (325f) (325f) (325f)</td><td>(325e) (325d) (325g) (325i)</td><td>(325e) (325e) (325i)</td><td>(325h) (325i)</td><td>(325i)</td></tr><tr><td>(325a)</td><td>(325i) (325c)</td><td>0</td><td>(325c)</td><td>(325c) (325c)</td><td>(325c)</td></tr></table>

We give a single example of a method derived in this manner:

<table><tr><td></td><td colspan="5"></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>云</td><td>1</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>3</td><td></td><td>GR</td><td></td></tr><tr><td></td><td>16</td><td>GR</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td></td><td>7 90</td><td>0</td><td>1</td><td>1</td><td>1 7 90</td></tr></table>

The first methods of this order, derived by Kutta (1901), have a different structure. One of these, as corrected by Nystr¨om (1925), is

<table><tr><td>0 </td><td rowspan="16"></td><td rowspan="4"></td><td rowspan="4">2</td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td><td></td><td>3</td><td>影</td><td></td></tr><tr><td></td><td>中</td><td></td><td></td><td>0</td></tr><tr><td rowspan="2"></td><td></td><td rowspan="2"></td><td rowspan="2">15452万</td><td></td></tr><tr><td>0</td><td>27</td></tr><tr><td rowspan="2"></td><td>23 192</td><td rowspan="2"></td><td rowspan="2">125 192</td><td>64</td><td>125 192</td></tr><tr><td></td><td>0</td><td></td></tr></table>

As we have pointed out in Subsection 316, the order conditions for a scalar first order differential equation are less restrictive than for the general vector case, if orders of 5 or more are under consideration. This suggests the existence of methods whose orders, when applied to a single first order differential equation, may be 5, whereas it is only 4 when applied to a higher-dimensional system. An example of such a method is given in Butcher (1995).
