$a _ { i j }$ are for $j = 1$ and for $j$ corresponding to a member of row $k - 1$ . Thus, the quadrature formula associated with this row has the form

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { k - 1 } w _ { j } \phi ( \xi _ { j } )
$$

and the coefficients are chosen to make this exact for $\phi$ a polynomial of degree $k - 1$ . For $i$ a member of row $k = m + 1 , m + 2 , \ldots , 2 m$ , the non-zero $a _ { i j }$ are found in a similar way based on the quadrature formula

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { m } w _ { j } \phi ( \xi _ { j } ) .
$$

The method constructed in this way has order, or generalized order, respectively, equal to $p = 2 m + 1$ . To see this, let ${ \widetilde { Y } } _ { i }$ denote the approximation to $y ( x _ { n - 1 } + h \xi _ { i } )$ in stage $1 + i$ of the order $2 m + 1$ Radau I method (in case I) or the order $2 m + 2$ Lobatto method (in case II). It is easy to see that the stages corresponding to row $k$ approximate the $\widetilde { Y }$ quantities to within $O ( h ^ { k + 1 } )$ . Thus the full method has order $2 m + 1$ in case I and generalized order $2 m + 1$ in case II. Add one more stage to the case II methods, as in Theorem 323B, and we obtain order $p = 2 m + 2$ with $s = { \textstyle { \frac { 1 } { 2 } } } ( 3 m ^ { 2 } + m + 4 )$ stages compared with $p = 2 m + 1$ and $\begin{array} { r } { s = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) } \end{array}$ stages in case I. This gives the result of the theorem. 

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

# 326 Methods of order 6

The first methods of order 6 were derived by Huˇta (1956, 1957). Although his methods used $s = 8$ stages, it is possible to find methods of this order with $s = 7$ . Just as for order 5, we assume the modified $C ( 2 )$ condition and the $D ( 1 )$ condition. We also assume the quadrature conditions so that the only order conditions that remain are $\Phi ( t ) = 1 / \gamma ( t )$ for the trees

$$
t = \{ \begin{array} { c c c c c c } { \ddot { \bigtriangledown } , } & { \ddot { \bigtriangledown } , } & { \ddot { \bigtriangledown } ^ { \prime } } & { \mathrm { ~  ~ \nabla ~ } _ { \mathrm { a n d } } } & { \ddot { \bigtriangledown } ^ { \prime } . } \end{array} \}
$$

Linear combinations of these with other order conditions whose truth is automatic appear in (326h)–(326k) below, where we have listed all the conditions we need to specify a method:

$$
\begin{array} { c } { { b _ { 2 } = 0 , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 3 } ) ( c _ { i } - c _ { 4 } ) c _ { i } = } } \\ { { \displaystyle \frac { 1 } { 3 0 } - \frac { c _ { 3 } + c _ { 4 } + c _ { 6 } } { 2 0 } + \frac { c _ { 3 } c _ { 4 } + c _ { 3 } c _ { 6 } + c _ { 4 } c _ { 6 } } { 1 2 } - \frac { c _ { 3 } c _ { 4 } c _ { 6 } } { 6 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 4 } ) c _ { i } = \frac { 1 } { 2 0 } - \frac { c _ { 4 } + c _ { 6 } } { 1 2 } + \frac { c _ { 4 } c _ { 6 } } { 6 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 6 } ) c _ { i } = \frac { 1 } { 1 2 } - \frac { c _ { 6 } } { 6 } , } } \end{array}
$$

$$
\begin{array} { c c } { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) c _ { i } ( \varepsilon - \omega _ { i } ^ { \prime } ) } } \\ { { \le } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \Delta ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) c _ { i } - \frac { 1 } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } - \frac { c _ { i } ^ { \prime } } { \omega _ { i } } } } \\ { { \le } } \\  { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^ { \prime } ) } \\ { { \le } } \\   \displaystyle \sum _ { i = 1 } ^ { n } \omega _ { i , j } ( 1 - c ) \omega _ { i , j } ( \varepsilon - \omega _ { i } ^  \prime  \end{array}
$$

$$
\begin{array} { r l } { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( n _ { k } ( \xi ) - c _ { k } ) ( \xi - c _ { k } ) ( \xi - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta - c _ { k } } { 1 2 } + \frac { c _ { k } \Delta c _ { k } } { 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( 1 - c _ { k } ) ( \xi ) , \quad \quad k = - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad + \frac { c _ { k } \Delta c _ { k } } { 2 ( \xi - \xi ) } + \frac { \Delta } { 1 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad + \frac { c _ { k } \Delta c _ { k } } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , } & { \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } , \quad \quad \quad ) } & { \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } - \frac { \Delta } { 1 2 } ) , \quad \quad } \\ { \sum _ { k = 1 } ^ { n } ( 1 - c _ { k } ) ( \xi - \frac { 1 } { 2 ( \xi - \xi ) } ) , \quad \quad } \\  \sum _  k = 1 \end{array}
$$

This rather formidable set of equations can be solved in a systematic and straightforward manner except for one detail: there are three equations, (326i), (326j) and (326k), each involving $a _ { 5 4 }$ and $a _ { 6 5 }$ and no other elements of $A$ . Hence, we need to ensure, by restricting the choice of $c$ , that these equations are consistent. To find the consistency condition, note that the left-hand sides of these equations are related by (3 $2 6 \mathrm { i } ) \times ( 3 2 6 \mathrm { j } ) = ( 3 2 6 \mathrm { b } ) \times ( 3 2 6 \mathrm { k } )$ . The consistency condition, found from the right-hand sides, simplifies to

$$
\begin{array} { r } { ( c _ { 6 } - 1 ) \left( c _ { 4 } ( 2 - 1 0 c _ { 3 } + 1 5 c _ { 3 } ^ { 2 } ) - c _ { 3 } \right) = 0 . } \end{array}
$$

We can eliminate the factor $c _ { 6 } - 1$ because, if it were zero, then it would follow that $\begin{array} { r } { c _ { 3 } = \frac { 1 } { 3 } } \end{array}$ and that $c _ { 4 } = 1$ , which are consistent with the vanishing of the second factor, which leads to

$$
c _ { 4 } = \frac { c _ { 3 } } { 2 - 1 0 c _ { 3 } + 1 5 c _ { 3 } ^ { 2 } } .
$$

Having chosen $c _ { 3 }$ , and therefore $c _ { 4 }$ , together with arbitrary $c _ { 2 }$ , $c _ { 5 }$ and $c _ { 6 }$ and the known value $c _ { 7 } = 1$ , excluding some impossible cases, we can solve for the components of $b ^ { \intercal }$ from (326a)–(326g). We can then solve for $a _ { 5 4 }$ , $a _ { 6 4 }$ and $a _ { 6 5 }$ from the consistent equations (326h)–(326k). We then solve for $a _ { 3 2 }$ from (326l) and then for $a _ { 4 2 }$ , $a _ { 4 3 }$ , $a _ { 5 2 }$ , $a _ { 5 3 }$ , $a _ { 6 2 }$ and $a _ { 6 3 }$ from (326l) with $i = 4 , 5 , 6$ and from (326o), (326p) and (326q). It remains to compute the first column of $A$ from (326m) and the last row from (326n).

The following example is of a method derived from these equations:

<table><tr><td>0 D</td><td>1 0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>中</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>24</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>33</td><td>43</td><td></td><td>118</td><td>花 195</td><td>80</td><td></td></tr><tr><td></td><td>260</td><td>13</td><td>156</td><td></td><td>39</td><td></td><td>39</td><td></td></tr><tr><td></td><td>13 200</td><td>0</td><td>11 40</td><td></td><td>11 40</td><td>A</td><td>A</td><td>13 200</td></tr></table>

It is possible to derive sixth order methods in other ways. For example, Huˇta used the $C ( 3 )$ with subsidiary conditions for stages 2 and 3. However, he used $s = 8$ , and this gave him more freedom in the choice of $c$ .

The alternative example of a method of this order that we give uses $C ( 2 )$ and $D ( 2 )$ with subsidiary conditions to repair the gaps in the order conditions caused by $C ( 2 )$ not applying to stage 2 and $D ( 2 )$ not holding for stage 6. It is necessary to choose $b _ { 2 } = 0$ , and to require that $c _ { 3 }$ , $c _ { 4 }$ and $c _ { 5 }$ are related so that the right-hand side vanishes in the equations

$$
\begin{array} { c } { { \displaystyle \sum _ { i , j = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 5 } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \frac { 1 } { 9 0 } - \frac { c _ { 3 } } { 4 0 } - \frac { c _ { 5 } } { 6 0 } + \frac { c _ { 3 } c _ { 5 } } { 2 4 } , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { 7 } b _ { i } ( 1 - c _ { i } ) ( c _ { i } - c _ { 3 } ) ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 5 } ) c _ { i } = } } \\ { { \displaystyle \frac { 1 } { 3 0 } - \frac { c _ { 3 } + c _ { 4 } + c _ { 5 } } { 2 0 } + \frac { c _ { 3 } c _ { 4 } + c _ { 3 } c _ { 5 } + c _ { 4 } c _ { 5 } } { 1 2 } - \frac { c _ { 3 } c _ { 4 } c _ { 5 } } { 6 } , } } \end{array}
$$

because the left-hand sides are identically zero. A method derived along these lines is as follows:

<table><tr><td>0 #</td><td rowspan="11"></td><td rowspan="4">2 4</td><td rowspan="4"></td><td rowspan="4">65</td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4">19</td></tr><tr><td>0 110</td></tr><tr><td>169</td></tr><tr><td>1458 44</td></tr><tr><td></td><td>729 88</td><td>1458 76</td><td>336</td><td></td></tr><tr><td>15</td><td>675</td><td>135 351</td><td>325</td><td></td></tr><tr><td>0</td><td>21</td><td>0 105</td><td>324</td><td>45</td></tr><tr><td></td><td>106</td><td>689</td><td>689</td><td>106</td></tr><tr><td>1</td><td>2517</td><td>55</td><td>10615 567</td><td>7245</td></tr><tr><td></td><td>4864</td><td>38</td><td>31616</td><td>7904</td><td>4864</td><td>2597 2432</td></tr><tr><td></td><td>0</td><td>0</td><td>1375 4992</td><td>6561 20384</td><td>3375 12544</td><td>53 768 294</td></tr></table>

# 327 Methods of orders greater than 6

Methods with order 7 must have at least nine stages. It is possible to construct such a method using the principles of Subsection 323, extending the approach used in Subsection 326. The abscissa vector is chosen as

$$
\begin{array} { r } { c = [ 0 \quad \frac { 1 } { 3 } c _ { 4 } \quad \frac { 2 } { 3 } c _ { 4 } \quad c _ { 4 } \quad c _ { 5 } \quad c _ { 6 } \quad c _ { 7 } \quad 0 \quad 1 ] ^ { \intercal } , } \end{array}
$$

and the orders of stages numbered $4 , 5 , \dots , 9$ are forced to be 3. To achieve consistency of the conditions

$$
\begin{array} { c } { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } a _ { j k } c _ { k } ( c _ { k } - c _ { 4 } ) ( c _ { k } - c _ { 5 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 4 \cdot 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } } { 3 \cdot 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 3 \cdot 4 \cdot 5 } , } } \\ { { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) ( c _ { j } - c _ { 6 } ) = } } \\ { { { } } } \\ { { \displaystyle \frac { 1 } { 5 \cdot 6 \cdot 7 } - \frac { c _ { 4 } + c _ { 5 } + c _ { 6 } } { 4 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } + c _ { 4 } c _ { 6 } + c _ { 5 } c _ { 6 } } { 3 \cdot 4 \cdot 5 } - \frac { c _ { 4 } c _ { 5 } c _ { 6 } } { 2 \cdot 3 \cdot 4 } , } } \\ { { { } } } \\ { { \displaystyle \sum b _ { i } ( 1 - c _ { i } ) c _ { i } a _ { i j } c _ { j } ( c _ { j } - c _ { 4 } ) ( c _ { j } - c _ { 5 } ) = \frac { 1 } { 4 \cdot 6 \cdot 7 } - \frac { c _ { 4 } } { 3 \cdot 5 \cdot 6 } + \frac { c _ { 4 } c _ { 5 } } { 2 \cdot 4 \cdot 5 } } } \end{array}
$$

it is found that

$$
c _ { 6 } = \frac { u - 1 2 v + 7 u v } { 3 - 1 2 u + 2 4 v + 1 4 u ^ { 2 } - 7 0 u v + 1 0 5 v ^ { 2 } } ,
$$

where $u = c _ { 4 } + c _ { 5 }$ and $v = c _ { 4 } c _ { 5 }$ . The value of $c _ { 7 }$ is selected to ensure that

$$
\int _ { 0 } ^ { 1 } x ( 1 - x ) ( x - c _ { 4 } ) ( x - c _ { 5 } ) ( x - c _ { 6 } ) ( x - c _ { 7 } ) d x = 0 .
$$

The tableau for a possible method derived along these lines is

<table><tr><td>0 G</td><td rowspan="16"></td><td colspan="2"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td></tr><tr><td>1 0</td><td>1</td><td></td></tr><tr><td>1</td><td>0 3</td><td></td></tr><tr><td></td><td>0 150</td><td></td></tr><tr><td></td><td>148 0</td><td>1331</td><td>56</td><td></td><td></td></tr><tr><td></td><td>1331 404</td><td>170</td><td>1331</td><td></td><td></td></tr><tr><td></td><td>243</td><td>27</td><td>4024 1701</td><td>10648</td><td></td></tr><tr><td></td><td>2466</td><td>1242</td><td>19176</td><td>1701 51909</td><td>1053</td></tr><tr><td></td><td>2401</td><td>0 343</td><td>16807</td><td></td><td></td></tr><tr><td>0</td><td>5</td><td>0</td><td></td><td>96</td><td>16807 1815</td><td>2401 405</td><td>49</td></tr><tr><td></td><td>154</td><td></td><td>0</td><td>539</td><td>20384</td><td>2464</td><td>1144</td></tr><tr><td>1</td><td>113</td><td>0</td><td>195</td><td>32</td><td>29403</td><td>729</td><td>1029 21</td></tr><tr><td></td><td>32</td><td></td><td>22</td><td></td><td></td><td>512</td><td>1408</td></tr><tr><td></td><td></td><td></td><td></td><td>7</td><td>3584</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>32</td><td>1771561</td><td>243</td><td>16</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td>16807 77</td></tr><tr><td></td><td></td><td></td><td></td><td>105</td><td>6289920</td><td>2560</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>74880</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1440</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Order 8 requires 11 stages, and methods of this order were derived by Curtis (1970)and Cooper and Verner (1972). In each case the abscissae were based on the Lobatto quadrature formula with three internal points. We quote the method of Cooper and Verner in Table 327(I).

Although order 9 has not attracted much interest, and it is unknown how many stages are required to achieve this order, order 10 has posed a challenge. In Curtis (1975) a method of order 10 was presented with 18 stages. However, using an ingenious combination of various simplifying assumptions, Hairer (1978) accomplished this feat in 17 stages. It is still not known if fewer stages are possible.

# Exercises 32

32.1 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 2 } } } , 1 ]$ .

32.2 Find a method with $s = p = 3$ such that $c = [ 0 , { \scriptstyle { \frac { 1 } { 3 } } } , 1 ]$ .

32.3 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $\textstyle c _ { 2 } = { \frac { 1 } { 5 } }$ .

32.4 Find a method with $s = p = 4$ such that $b _ { 2 } = 0$ and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ .

32.5 Find a method with $s = p = 4$ such that $b _ { 1 } = 0$ and $c _ { 3 } = 0$ .

32.6 Show that Lemma 322A can be used to prove that $c _ { 4 } = 1$ , if $s = p \geq 4$ .

32.7 Show that Lemma 322A can be used to prove that $c _ { 5 } = 1$ , if $s = p \geq 5$ leading to an alternative proof of Theorem 324B.

<table><tr><td>% 08I I 6</td><td>贵</td><td>08 6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>81 12-65</td><td>亚 227281</td><td>Z</td><td>2 2223125533173153111</td><td>业 18781</td><td>81 2+2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>I</td></tr><tr><td></td><td>2</td><td>99</td><td>509</td><td>2555</td><td></td><td></td><td></td><td></td><td>红</td><td>V</td></tr><tr><td></td><td></td><td>2173121111111-1113171112111311111-1111</td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>T</td><td>1+2</td></tr><tr><td></td><td></td><td>82 35533211</td><td>1111 12712188</td><td>兴</td><td>99 110-16</td><td>0</td><td>0</td><td>0</td><td>2 T</td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td>I</td></tr><tr><td></td><td></td><td></td><td></td><td>1213531</td><td>1241</td><td>0</td><td>0</td><td>0</td><td>T</td><td>1A-2</td></tr><tr><td></td><td></td><td></td><td></td><td>0</td><td>0 1271111451</td><td>06</td><td>118 227222231</td><td>0</td><td>W</td><td>V</td></tr><tr><td></td><td></td><td></td><td></td><td>32731351</td><td></td><td>3575555315</td><td></td><td></td><td>-01</td><td>1-2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>08 122-99</td><td>098 22245223111</td><td>9 1+6</td><td>0</td><td>8</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+9</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>222</td><td>9 1+81</td><td>0</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>-2</td><td>6</td><td>86</td><td>+</td><td>+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1+1</td><td>120-2-</td><td>1</td><td>1+2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>N</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 33 Runge–Kutta Methods with Error Estimates

# 330 Introduction

Practical computations with Runge–Kutta methods usually require a means of local error estimation. This is because stepsizes are easy to adjust so as to follow the behaviour of the solution, but the optimal sequence of stepsizes depends on the local truncation error. Of course, the exact truncation error cannot realistically be found, but asymptotically correct approximations to it can be computed as the integration proceeds. One way of looking at this is that two separate approximations to the solution at a step value $x _ { n }$ are found. Assuming that the solution value at the previous point is regarded as exact, because it is the local error that is being approximated, denote the two solutions found at the current point by $y _ { n }$ and ${ \hat { y } } _ { n }$ . Suppose the two approximations have orders $p$ and $q$ , respectively, so that

$$
y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } ) , \qquad { \widehat { y } } _ { n } = y ( x _ { n } ) + O ( h ^ { q + 1 } ) .
$$

Then, if $q > p$

$$
{ \widehat { y } } _ { n } - y _ { n } = y ( x _ { n } ) - y _ { n } + O ( h ^ { p + 2 } ) ,
$$

which can be used as an approximation to the error committed in the step. Furthermore, the approximation becomes increasingly accurate as $h$ becomes small. Thus ${ \widehat { y } } _ { n } - y _ { n }$ is used as the error estimator.

Even though we emphasize the construction of method pairs for which $q = p + 1$ , and for which it is $y _ { n }$ (rather than the asymptotically more accurate approximation ${ \widehat { y } } _ { n }$ ) that is propagated as the numerical approximation at $x _ { n }$ , customary practice is to use the higher order as the propagated value. This is sometimes interpreted as ‘local extrapolation’, in the sense that the error estimate is added to the approximate solution as a correction. While the estimator is still used as a stepsize controller, it is now no longer related asymptotically to the local truncation error.

We review the ‘deferred approach to the limit’ of Richardson (1927) and then consider specially constructed Runge–Kutta tableaux, which combine two methods, with orders one apart, built into one. The classical method of this type is due to Merson (1957), but we also consider built-in estimators due to Fehlberg (1968, 1969), Verner (1978) and Dormand and Prince (1980). Some of the methods derived for the author’s previous book (Butcher, 1987) will also be recalled.

# 331 Richardson error estimates

Richardson extrapolation consists of calculating a result in a manner that depends on a small parameter, and for which the error in the calculation varies systematically as the parameter varies. By using a sequence of values of the parameter, much of the effect of the errors can be eliminated so that improved accuracy results. In numerical quadrature, for example, the method of Romberg (1955) is based on calculating an integral $\begin{array} { r } { I = \int _ { a } ^ { b } \phi ( x ) d x } \end{array}$ using the trapezoidal rule with a stepsize $h$ equal to an integer divisor of $b - a$ . For a single choice of $h$ , the result computed can be expanded by an asymptotic formula of the form

$$
T ( h ) = I + C _ { 1 } h ^ { 2 } + C _ { 2 } h ^ { 4 } + \cdot \cdot \cdot ,
$$

so that, using a sequence $\begin{array} { l l l } { { h } } & { { = } } & { { H , 2 ^ { - 1 } H , 2 ^ { - 2 } H , . . . . } } \end{array}$ , we arrive at the approximations $T _ { 0 } = T ( H )$ , $T _ { 1 } = T ( \textstyle { \frac { 1 } { 2 } } H )$ , $T _ { 2 } = T ( \textstyle { \frac { 1 } { 4 } } H ) _ { ; }$ . . . with expansions

$$
\begin{array} { c } { { T _ { 0 } = I + C _ { 1 } H ^ { 2 } + C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 1 } = I + \frac { 1 } { 4 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 1 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 2 } = I + \frac { 1 } { 1 6 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 2 5 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { \vdots } } \\ { { { } } } \end{array}
$$

By forming

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 } = \frac { 4 } { 3 } T _ { 1 } - \frac { 1 } { 3 } T _ { 0 } } , } \\ { ~ } \\ { { \displaystyle T _ { 1 2 } = \frac { 4 } { 3 } T _ { 2 } - \frac { 1 } { 3 } T _ { 1 } } , } \\ { ~ } \\ { { \displaystyle \quad \vdots \qquad } } \end{array}
$$

we obtain an ‘improved’ sequence in which the $C _ { 1 } H ^ { 2 }$ terms are eliminated from the asymptotic expansions so that convergence towards the exact result $I$ is more rapid as terms in the sequence are calculated. Similarly, a second sequence of improved approximations can be found from

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 2 } = \frac { 1 6 } { 1 5 } T _ { 1 2 } - \frac { 1 } { 1 5 } T _ { 0 1 } } , } \\ { { \displaystyle T _ { 1 2 3 } = \frac { 1 6 } { 1 5 } T _ { 2 3 } - \frac { 1 } { 1 5 } T _ { 1 2 } } , } \\ { { \displaystyle \quad \quad \quad \quad \quad \vdots } } \end{array}
$$

This idea has an application to Runge–Kutta methods for ordinary differential equations on the small scale of a single step, repeated with two steps and half the original value of $h$ . Let $y _ { n - 1 }$ denote an incoming approximation for $y ( x _ { n - 1 } )$ and $y _ { n }$ the solution computed as an approximation to $y ( x _ { n } ) = y ( x _ { n - 1 } + h )$ using a Runge–Kutta method with tableau

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} \right| \overset { \phantom { = } } \longrightarrow \left| \begin{array} { c c c c c } { 0 } \\ { a _ { 2 1 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \ddots } & { a _ { s , s - 1 } } \\ { b _ { 1 } } & { b _ { 2 } } & { \ddots } & { b _ { s - 1 } } & { b _ { s } } \end{array} \right. . } \end{array}
$$

Repeating the calculation with $h$ replaced by ${ \frac { 1 } { 2 } } h$ but carrying out two steps, rather than only one, is equivalent to taking a single step with the original $h$ , but using the tableau

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & \end{array}
$$

Denote the result computed by this $2 s$ -stage method by ${ \hat { y } } _ { n }$ , and note that if the local truncation error in $y _ { n }$ is $C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ , so that

$$
y _ { n } = y ( x _ { n } ) - C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

then

$$
\widehat { y } _ { n } = y ( x _ { n } ) - 2 ^ { - p } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

because the error in computing ${ \hat { y } } _ { n }$ is $2 ^ { - p - 1 } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ contributed from each of two steps.

From the difference of (331a) and (331b) we find

$$
\widehat { y } _ { n } - y _ { n } = ( 1 - 2 ^ { - p } ) C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

so that the local truncation error in $y _ { n }$ can be approximated by

$$
( 1 - 2 ^ { - p } ) ^ { - 1 } ( { \widehat { y } } _ { n } - y _ { n } ) .
$$

This seems like an expensive way of computing the error in the result computed using an $s$ -stage method, because the additional computations required for the estimation take twice as long as the result itself. However, the additional cost becomes more reasonable when we realize that it is not $y _ { n }$ but ${ \widehat { y } } _ { n }$ that should be propagated. The additional cost on this basis is something like $5 0 \%$ . Actually, it is slightly less than this because the calculation of the derivative of $y _ { n - 1 }$ is shared by each of the two methods, and needs to be carried out only once.

# 332 Methods with built-in estimates

Instead of using the Richardson technique it is possible to combine two methods into one by constructing a tableau with common stages but two alternative output coefficient vectors. The following method, due to Merson (1957), seems to have been the first attempt at constructing this type of stepsize control mechanism:

<table><tr><td>1</td><td>R 1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>0 0</td><td>GR 0</td><td>2 2</td><td>1</td></tr><tr><td></td><td>1</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

The interpretation of this tableau, which contains two $b ^ { \scriptscriptstyle 1 }$ vectors, is that it combines two methods given by

<table><tr><td rowspan=1 colspan=1>0 1-3:1-3:1-2 1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1  0    0    2  1</td></tr></table>

and by

<table><tr><td>0 N</td><td></td><td>1 0</td><td></td><td></td><td></td></tr><tr><td></td><td>BU</td><td>0</td><td>G</td><td>2</td><td></td></tr><tr><td></td><td>1 10</td><td>0</td><td>1</td><td>2</td><td>1</td></tr></table>

![](images/a11978509f5592fc936d87d83461fb155c52032813e0ec83d846e80c2154f654.jpg)  
Two alternative stepsize control mechanisms based on Richardson (dashed line) and built-in (solid line) error estimates

In Merson’s derivation of this method, (332a) was shown to be of order 4. Although (332b) has order only 3, it becomes effectively of order 5 if used to solve linear problems with constant coefficients. The difference between the results computed by the two methods can, it is suggested, be used as a local error estimator. To show how well the method works in practice, an experiment using this technique has been carried out and the results summarized in Figure 332(i). The three problems attempted are the Kepler orbit problem with eccentricities $e = 0 . 1$ , $e = 0 . 5$ and $e = 0 . 9$ , respectively.

# 333 A class of error-estimating methods

In the search for efficient step-control mechanisms, we consider $( s + 1 )$ -stage methods of the form

with order $p + 1$ , with the coefficients chosen so that the embedded method

has order $p$

Even though this method formally has $s ~ + ~ 1$ stages, in terms of computational cost it can be regarded as having only $s$ , because the derivative calculation needed for stage $s + 1$ is identical to the first derivative calculation in the succeeding step. It is convenient to write order conditions for the embedded method pair in terms of the number $\boldsymbol { B } = \boldsymbol { b } _ { s + 1 }$ and the artificial tableau

$$
\begin{array}{c} { \begin{array} { r l } & { { \begin{array} { l } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} } } \\ & { { \begin{array} { r l } { c _ { 3 } } \\ { c _ { 3 } } \\ { \vdots } \end{array} } } \\ & { { \begin{array} { r l } { c _ { s } } \\ { b _ { 1 } } & { a _ { s 2 } } \end{array} } } & { \cdots \quad a _ { s , s - 1 } } \\ & { { \begin{array} { r l } { b _ { 2 } } & { \ddots \quad } \\ { b _ { 1 } } & { b _ { 2 } } & { \ddots \quad } \end{array} } } \end{array} } .  \end{array} 
$$

An elementary weight, computed using this tableau, differs from that of the full method by a single term. This additional term is formed by multiplying $B$ by the derivative of the order result found by the method represented by $p$   
(333b). This enables us to form modified order conditions for (333c), which will ensure that both (333a) and (333b) satisfy the correct conditions. We denote the elementary weights for (333c) by $\Phi ( t )$ .

Theorem 333A If (333b) has order $p$ and (333a) has order $p + 1$ and $\boldsymbol { B } = \boldsymbol { b } _ { s + 1 }$ , then

$$
\Phi ( t ) = \frac { 1 - B r ( t ) } { \gamma ( t ) } , \qquad r ( t ) \leq p + 1 .
$$

Conversely, if (333d) holds with $c _ { s } \neq 1$ and $B \neq 0$ and, in addition,

$$
\begin{array} { l } { { b _ { s + 1 } = B , } } \\ { { a _ { s + 1 , s } = B ^ { - 1 } b _ { s } ( 1 - c _ { s } ) , } } \\ { { a _ { s + 1 , j } = B ^ { - 1 } \left( b _ { j } ( 1 - c _ { j } ) - \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } a _ { i j } \right) , \qquad j = 1 , 2 , \ldots , s - 1 , } } \end{array}
$$

then (333b) has order $p$ and (333a) has order $p + 1$ .

Proof. For a given tree $t$ , let $\widehat { \Phi } ( t )$ denote the elementary weight for (333a) and $\overline { { \Phi } } ( t )$ the elementary weight for (333b). Because the latter method has order $p$ , it follows that for a tree $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ , with order not exceeding $p + 1$ , we have $\overline { { \Phi } } ( t _ { i } ) = 1 / \gamma ( t _ { i } )$ , for $i = 1 , 2 , \dots , m$ . Hence, for a method identical with (333a) except for $b ^ { \top }$ replaced by the basis vector $e _ { s + 1 } ^ { \prime }$ , the elementary weight corresponding to $t$ will be

$$
\prod _ { i = 1 } ^ { m } { \frac { 1 } { \gamma ( t _ { i } ) } } = { \frac { r ( t ) } { \gamma ( t ) } } .
$$

Adding $B$ multiplied by this quantity to $\Phi ( t )$ gives the result

$$
\Phi ( t ) + B \frac { r ( t ) } { \gamma ( t ) } = \widehat { \Phi } ( t ) = \frac { 1 } { \gamma ( t ) } ,
$$

which is equivalent to (333d).

To prove the converse, we first note that, because $B \neq 0$ , the previous argument can be reversed. That is, if (333b) has order $p$ then (333d) implies that (333a) has order $p + 1$ . Hence, it is only necessary to prove that (333b) has order $p$ . We calculate $\overline { { \Phi } } ( t )$ , for $r ( t ) \leq p$ as follows, where we have written $\chi _ { i } ( t )$ for the coefficient of $b _ { i }$ in $\Phi ( t )$

$$
\begin{array} { l } { \displaystyle \overline { { \Phi } } ( t ) = B ^ { - 1 } \sum _ { j = 1 } ^ { s } b _ { j } ( 1 - c _ { j } ) \chi _ { j } ( t ) - B ^ { - 1 } \sum _ { i = 1 } ^ { s } \sum _ { j = 1 } ^ { s - 1 } b _ { i } a _ { i j } \chi _ { j } ( t ) } \\ { \displaystyle \quad = B ^ { - 1 } ( \Phi ( t ) - \Phi ( t \tau ) - \Phi ( \tau t ) ) } \\ { \displaystyle \quad = B ^ { - 1 } \left( \frac { 1 - B r ( t ) } { \gamma ( t ) } - \frac { r ( t ) ( 1 - B ( 1 + r ( t ) ) ) } { ( 1 + r ( t ) ) \gamma ( t ) } - \frac { 1 - B ( 1 + r ( t ) ) } { ( 1 + r ( t ) ) \gamma ( t ) } \right) } \\ { \displaystyle \qquad = \frac { 1 } { \gamma ( t ) } . } \end{array}
$$

Although the derivation is carried out from a modified version of the order conditions, it is convenient to display a particular method in the format

$$
\begin{array} { r l } & { \left| \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { \frac { - - 1 - \frac { \lambda } { a _ { s - } } - \dots - \dots - \dots - } { a _ { s , s - 1 } } } \\ { \frac { c _ { s } } { c _ { s } } \left| \frac { b _ { 1 } } { d _ { 3 } } - \frac { 1 - \lambda } { d _ { 2 } } - \dots - \frac { b _ { s - 1 } } { d _ { s - 1 } } - \frac { b _ { s } } { d _ { s } } \right. } \end{array} \right| } \end{array}
$$

where

$$
\left[ d _ { 1 } \quad d _ { 2 } \quad \cdots \quad d _ { s - 1 } \quad d _ { s } \right] = \left[ b _ { 1 } - a _ { s 1 } \quad b _ { 2 } - a _ { s 2 } \quad \cdots \quad b _ { s - 1 } - a _ { s , s - 1 } \quad b _ { s } \right]
$$

is the vector of coefficients in the proposed error estimator. That is, $\textstyle h \sum _ { i = 1 } ^ { s } d _ { i } f ( Y _ { i } )$ is used to evaluate the difference between the order $p$ approximation $\begin{array} { r } { y _ { n - 1 } + h \sum _ { i = 1 } ^ { s } a _ { s + 1 , i } f ( Y _ { i } ) } \end{array}$ and the supposedly more accurate −approximation of order $p + 1$ given by $\begin{array} { r } { y _ { n - 1 } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } ) } \end{array}$ . The dashed line above row number $s$ of the tableau is intended to indicate that the row below it is the approximation to be propagated and, of course, the dashed line below the $b ^ { \intercal }$ vector separates the order $p { + 1 }$ approximation from the error estimator.

Now let us look at some example of these embedded methods. Methods of orders $^ { 1 }$ and 2 are easy to derive and examples of each of these are as follows:

$$
\frac { - \llangle 1 } { \vert - \frac { 1 } { 2 } - \frac { 1 } { 2 } \vert }
$$

and

$$
\begin{array} { r }  \frac { 0 } { \frac { 1 } { 2 } } | \begin{array} { l } { 1 } \\ { \frac { 1 } { 2 } } \\ { - \frac { 1 } { 1 } - 0 - \frac { 1 } { 0 } -- 0 } \\ { \frac { 1 } { | \frac { 1 } { 6 } - \frac { 1 } { 3 } - \frac { 1 } { 3 } - \frac { 1 } { 3 } - \frac { 1 } { 6 } } \\ { - \frac { 1 } { 6 } - \frac { 1 } { 3 } - \frac { 2 } { 3 } - \frac { 1 } { 6 } } \end{array}  } \end{array} .
$$

Observe that for the second order method, the third order method in which it is embedded is actually the classical fourth order method.

Order 3 embedded in order 4 requires $s = 4$ stages. From the modified order conditions we find that

$$
\begin{array} { c } { { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = \displaystyle { \left( \frac { 1 } { 4 } - B \right) - ( c _ { 2 } + c _ { 4 } ) \left( \frac { 1 } { 3 } - B \right) + c _ { 2 } c _ { 4 } \left( \frac { 1 } { 2 } - B \right) } , } } \\ { { b _ { 4 } a _ { 4 3 } c _ { 3 } ( c _ { 3 } - c _ { 2 } ) = \displaystyle { \left( \frac { 1 } { 1 2 } - \frac { B } { 3 } \right) - c _ { 2 } \left( \frac { 1 } { 6 } - \frac { B } { 2 } \right) } , } } \\ { { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) a _ { 3 2 } c _ { 2 } = \displaystyle { \left( \frac { 1 } { 8 } - \frac { B } { 2 } \right) - c _ { 4 } \left( \frac { 1 } { 6 } - \frac { B } { 2 } \right) } , } } \\ { { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \displaystyle { \left( \frac { 1 } { 2 4 } - \frac { B } { 6 } \right) } , } } \end{array}
$$

so that, equating the products (333h) $\times$ (333k) and (333i) $\times$ (333j) and simplifying, we find the consistency condition

$$
c _ { 4 } = \frac { 1 - 7 B + 1 2 B ^ { 2 } } { 1 - 6 B + 1 2 B ^ { 2 } } .
$$

For example, choosing $B = \textstyle { \frac { 1 } { 1 2 } }$ to give $c _ { 4 } = \textstyle { \frac { 6 } { 7 } }$ , together with $c _ { 2 } = { \frac { 2 } { 7 } }$ and $\textstyle c _ { 3 } = { \frac { 4 } { 7 } }$ , yields the tableau

<table><tr><td></td><td colspan="5"></td></tr><tr><td>G5</td><td>中</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>G</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>35</td><td></td><td>立</td></tr><tr><td></td><td></td><td></td><td>96</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>5</td><td></td><td></td></tr><tr><td></td><td>品</td><td></td><td>96</td><td></td><td></td></tr></table>

Order 4 embedded in order 5 requires $s = 6$ . That is, there are seven stages overall, but the last stage derivative is identical to the first stage derivative for the following step. To derive a method of this type, make the simplifying assumption

$$
\sum _ { j = 1 } ^ { 6 } a _ { i j } c _ { j } = { \frac { 1 } { 2 } } c _ { i } ^ { 2 } , \qquad i \neq 2 ,
$$

together with the subsidiary conditions

$$
b _ { 2 } = \sum _ { i = 3 } ^ { 6 } b _ { i } a _ { i 2 } = \sum _ { i = 3 } ^ { 6 } b _ { i } c _ { i } a _ { i 2 } = \sum _ { i = 4 } ^ { 6 } \sum _ { j = 3 } ^ { i - 1 } b _ { i } a _ { i j } a _ { j 2 } = 0 .
$$

Also, impose order conditions for the trees but instead of the corresponding conditions for the trees $\gamma _ { \textit { v } } \gamma _ { \textit { i } } \gamma _ { \textit { i } } ^ { \textit { v } } \}$ , use linear combinations as follows:

$$
\begin{array} { c } { { \displaystyle \sum _ { 6 \geq i > j \geq 4 } b _ { i } a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \left( \frac 1 { 1 2 } - \frac 1 3 B \right) - c _ { 3 } \left( \frac 1 6 - \frac 1 2 B \right) , } } \\ { { \displaystyle \sum _ { 5 \geq i \geq 5 } b _ { i } c _ { i } ( c _ { i } - c _ { 6 } ) ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 3 } ) = \left( \frac 1 5 - B \right) - \left( c _ { 6 } + c _ { 4 } + c _ { 3 } \right) \left( \frac 1 4 - B \right) } } \\ { { + ( c _ { 6 } c _ { 4 } + c _ { 6 } c _ { 3 } + c _ { 4 } c _ { 3 } ) \left( \frac 1 3 - B \right) } } \\ { { - c _ { 6 } c _ { 4 } c _ { 3 } \left( \frac 1 2 - B \right) , } } \end{array}
$$

$$
\begin{array} { r l r } { \sum _ { } } & { } & { b _ { i } ( c _ { i } - c _ { 6 } ) a _ { i j } c _ { j } ( c _ { j } - c _ { 3 } ) = \left( \frac { 1 } { 1 5 } - \frac { 1 } { 3 } B \right) - c _ { 6 } \left( \frac { 1 } { 1 2 } - \frac { 1 } { 3 } B \right) } \\ { \frac { } { 5 \geq i > j \geq 4 } } & { } & { - c _ { 3 } \left( \frac { 1 } { 8 } - \frac { 1 } { 2 } B \right) + c _ { 6 } c _ { 3 } \left( \frac { 1 } { 6 } - \frac { 1 } { 2 } B \right) , } \end{array}
$$

$$
\begin{array} { r l r } {  { \sum _ { 6 \geq i > j \geq 5 } b _ { i } a _ { i j } c _ { j } ( c _ { i } - c _ { 4 } ) ( c _ { j } - c _ { 3 } ) = ( \frac { 1 } { 2 0 } - \frac { 1 } { 4 } B ) - ( c _ { 4 } + c _ { 3 } ) ( \frac { 1 } { 1 2 } - \frac { 1 } { 3 } B ) } } \\ & { } & { + c _ { 4 } c _ { 3 } ( \frac { 1 } { 6 } - \frac { 1 } { 2 } B ) , } \end{array}
$$

$$
\sum _ { 6 \geq i > j > k \geq 4 } b _ { i } a _ { i j } a _ { j k } c _ { k } ( c _ { k } - c _ { 3 } ) = \left( \textstyle { \frac { 1 } { 6 0 } } - \frac { 1 } { 1 2 } { \cal B } \right) - c _ { 3 } \left( \textstyle { \frac { 1 } { 2 4 } } - \frac { 1 } { 6 } { \cal B } \right) .
$$

The left-hand sides of (333m)–(333p) consist of only a single term and we see that the product of (333m) and (333p) is equal to the product of (333n) and (333o). Thus we obtain consistency conditions for the values of $a _ { 6 5 }$ and $a _ { 5 4 }$ by comparing the products of the corresponding right-hand sides. After considerable manipulation and simplification, we find that this consistency condition reduces to

$$
c _ { 6 } = 1 - \frac { q _ { 0 } B } { q _ { 0 } - q _ { 1 } B + q _ { 2 } B ^ { 2 } } ,
$$

with

$$
\begin{array} { r l } & { q _ { 0 } = 1 0 c _ { 3 } ^ { 2 } c _ { 4 } + 2 c _ { 4 } - 8 c _ { 3 } c _ { 4 } - c _ { 3 } , } \\ & { q _ { 1 } = 6 0 c _ { 3 } ^ { 2 } c _ { 4 } - 5 6 c _ { 3 } c _ { 4 } + 1 6 c _ { 4 } - 8 c _ { 3 } , } \\ & { q _ { 2 } = 1 2 0 c _ { 3 } ^ { 2 } c _ { 4 } - 1 2 0 c _ { 3 } c _ { 4 } + 4 0 c _ { 4 } - 2 0 c _ { 3 } . } \end{array}
$$

Construction of the method consists of selecting $c _ { 2 }$ , $c _ { 3 }$ , $c _ { 4 }$ , $c _ { 5 }$ and $B$ ; choosing $c _ { 6 }$ in accordance with (333q); evaluating $a _ { 6 5 }$ and $a _ { 5 4 }$ from the consistent equations (333n), (333o) and (333p); and then evaluating $a _ { 6 4 }$ from (333l). The remaining coefficients are then evaluated using the remaining conditions that have been stated.

An example of a method in this family is

$$
 \begin{array} { r l } & { { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \frac { 1 } { 4 } } \end{array} \right] } \qquad { \begin{array} { r l } { 1 } & { } \\ { \frac { 1 } { 4 } } \end{array} } } \\ & { { \left[ \begin{array} { l l l l l l } { 1 } & { } & { } & { } & { } & { } & { } \\ { 0 } & { } { } & { } & { } & { } & { } & { } \\ { { \frac { 1 } { 4 } } } \end{array} \right] } \qquad { \begin{array} { r l } { 1 } & { } & { } & { } & { } & { } \\ { { \frac { 1 } { 8 } } } & { } & { } & { } & { } & { } & { } \\ { 0 } & { } { } & { } { - { \frac { 1 } { 2 } } } \end{array} } } \\ & { } &   \begin{array} { r l } { { \frac { 1 3 } } } & { } { 1 3 } & { } & { } & { } & { } & { } \\ { { \frac { 1 0 3 } { 2 0 } } } & { } { } & { - { \frac { 2 9 9 9 } { 1 0 0 0 } } } & { } & { { \frac { 7 8 } { 1 2 5 } } } & { } { \qquad { \frac { 1 3 } { 8 0 } } } & { } \\ { - { \frac { 6 } { 1 5 4 } } - { \frac { 7 4 1 5 } { 3 7 5 } } - { \frac { 6 8 5 } { 2 5 } } - { \frac { 5 7 2 5 } { 6 } } - { \frac { 5 7 2 } { 6 } } - { \frac { 5 7 5 } { 6 } } - { \frac { 5 7 5 } { 6 } } - - { \frac { 5 7 5 } { 6 } } } \\ { - { \frac { 5 7 3 } { 3 1 2 } } - } & { } & { } & { } & { } & { } \\ { { \frac { 1 0 1 } { 3 4 2 } } } & { } & { 0 } & { { \frac { 1 6 } { 3 8 } } } & { - { \frac { 1 6 0 } { 1 5 0 0 } } - { \frac { 5 7 5 } { 1 5 0 0 } } - { \frac { 1 3 } { 1 5 0 0 } } - { \frac { 1 3 } { 1 5 0 } } - { \frac { 7 5 7 } { 5 7 5 } } - \cdots } \\  - { \frac { 7 5 } { 3 1 0 } } - { \frac { 7 5 } { 6 } } - { \frac { 1 } { 1 5 0 } } - { \frac { 1 5 } { 1 3 5 } } -  \end{array} \end{array}
$$

For $p = 5$ , that is, a fifth order method embedded within a sixth order method, $s = 8$ seems to be necessary. We present a single example of a method satisfying these requirements. For all stages except the second, the stage order is at least 2, and for stages after the third, the stage order is at least 3. Under these assumptions, together with subsidiary conditions, it is found that for consistency, a relation between $c _ { 4 }$ , $c _ { 5 }$ , $c _ { 6 }$ , $c _ { 8 }$ and $B$ must hold. Given that these are satisfied, the derivation is straightforward but lengthy and will not be presented here. The example of a method pair constructed in this way is shown in the following tableau:

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 1-</td><td></td><td>1 18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td>0</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>2</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>15</td><td>0</td><td>63</td><td></td><td>7</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>8</td><td></td><td>8</td><td></td><td></td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>93</td><td>0</td><td>24921</td><td></td><td>10059</td><td>735</td><td>735</td><td></td><td></td><td></td></tr><tr><td>4</td><td>22</td><td></td><td>1408</td><td></td><td>704</td><td>1408</td><td>704</td><td></td><td></td><td></td></tr><tr><td>17</td><td>86547313055</td><td>0</td><td></td><td>96707067 15526951598 27949088</td><td></td><td></td><td></td><td>452648800 270189568 467982711</td><td></td><td></td></tr><tr><td>19</td><td>10295610642</td><td></td><td>2867062</td><td></td><td>571978869</td><td>81711267</td><td>245133801</td><td></td><td>390963</td><td></td></tr><tr><td></td><td>98 765</td><td>0</td><td>0</td><td></td><td>9 83</td><td>071 1600</td><td>75</td><td>64 225</td><td>2257600</td><td></td></tr><tr><td></td><td>188</td><td></td><td></td><td></td><td>1593</td><td>2943</td><td>197</td><td>576</td><td>2476099</td><td>2</td></tr><tr><td></td><td>3315</td><td></td><td>0</td><td></td><td>7553</td><td>20800</td><td>975</td><td>2275</td><td>29348800</td><td>39</td></tr><tr><td></td><td>142</td><td></td><td></td><td></td><td>2412</td><td>549</td><td>68</td><td>128</td><td>130321</td><td>2</td></tr><tr><td></td><td></td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>39</td></tr><tr><td></td><td>1989</td><td></td><td></td><td></td><td>7553</td><td>1040</td><td>195</td><td>4095</td><td>1467440</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 334 The methods of Fehlberg

Early attempts to incorporate error estimators into Runge–Kutta methods are exemplified by the work of Fehlberg (1968, 1969). In writing the coefficients of methods from this paper, a tabular form is used as follows:

$$
\begin{array} { r } { \frac { c } { \vert \vert \mathbf { \epsilon } \vert } . } \\ { \frac { \vert \widehat { b } ^ { \intercal } } { \vert \widehat { b } ^ { \intercal } } . } \end{array}
$$

The significance of this augmented tableau is that

$$
\frac { c \mid A } { b ^ { \top } }
$$

is a Runge–Kutta method of order $p$ , while

$$
\frac { c \dag A } { \ d b ^ { \dagger } }
$$

is a Runge–Kutta method of order $p + 1$ . The additional vector $\boldsymbol { d } ^ { \intercal } = \widehat { \boldsymbol { b } } ^ { \intercal } - \boldsymbol { b } ^ { \intercal }$ is used for error estimation. The fifth order method, with additional sixth order output for error estimation, recommended by Fehlberg, is

<table><tr><td>0 D</td><td rowspan="16"></td><td rowspan="4"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>提</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>中</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>144</td><td>-4</td><td>花</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>361</td><td>25 18</td><td>407</td><td></td><td>55</td><td></td><td></td><td></td></tr><tr><td>1</td><td>320</td><td>5</td><td>128</td><td></td><td>128</td><td></td><td></td><td></td></tr><tr><td>0</td><td>11</td><td></td><td>11</td><td>11</td><td>11</td><td>0</td><td></td><td></td></tr><tr><td></td><td>640</td><td>0</td><td>256</td><td>160</td><td>256</td><td></td><td></td><td></td></tr><tr><td>1</td><td>93</td><td>18</td><td>803</td><td>11</td><td>99</td><td>0</td><td>1</td><td></td></tr><tr><td rowspan="4"></td><td>640</td><td>5</td><td>256</td><td>160</td><td>256</td><td></td><td></td><td></td></tr><tr><td>31</td><td>0</td><td>1125</td><td></td><td>125</td><td>5</td><td>0</td><td>0</td></tr><tr><td>384 7</td><td></td><td>2816</td><td>品</td><td>768 125</td><td>66</td><td>5</td><td>5</td></tr><tr><td></td><td>0</td><td>1125 2816</td><td></td><td>品</td><td>768</td><td>0</td><td>66</td><td>66</td></tr><tr><td rowspan="2"></td><td>1408</td><td></td><td></td><td></td><td></td><td></td><td>5</td><td>5</td><td>5</td></tr><tr><td>5 66</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>66</td><td>66</td><td>66</td></tr></table>

We also present a similar method with $p ~ = ~ 7$ . This also comes from Fehlberg’s paper, subject to the correction of some minor misprints. The augmented tableau is

<table><tr><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0 0</td><td>靠</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td>0</td><td></td><td>2</td><td>云</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>25</td><td>0</td><td>0</td><td></td><td>125</td><td></td><td>125</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td></td><td>108</td><td></td><td>54</td><td>13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>31 300</td><td>0</td><td>0</td><td>0</td><td></td><td>61 225</td><td>2</td><td>900</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td></td><td>53</td><td></td><td>704</td><td>107</td><td>67</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2</td><td></td><td>0</td><td>6</td><td></td><td>45</td><td>9</td><td>90</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>91</td><td>0</td><td>0</td><td>23</td><td></td><td>976</td><td>311</td><td>19</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td>108</td><td></td><td>135</td><td>54</td><td>60</td><td>北</td><td></td><td>45</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2383</td><td>0</td><td>0</td><td>341</td><td></td><td>4496</td><td>301</td><td>2133</td><td>82</td><td>164</td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td>4100 3</td><td>0</td><td></td><td>164</td><td></td><td>1025</td><td>82 6</td><td>4100 3</td><td>3</td><td>3</td><td></td><td></td><td>0</td><td></td><td></td></tr><tr><td>0</td><td>205</td><td></td><td>0</td><td>0</td><td></td><td>0</td><td>41</td><td>205</td><td>41</td><td>41</td><td>A</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>1777</td><td>0</td><td>0</td><td>341</td><td></td><td>4496</td><td>289</td><td>2193</td><td>51</td><td>33</td><td>12</td><td></td><td>0</td><td>1</td><td></td></tr><tr><td></td><td>4100 41</td><td>0</td><td></td><td>164</td><td></td><td>1025</td><td>82 34</td><td>4100 9</td><td>82 9</td><td>164 9</td><td>41 9</td><td></td><td>41</td><td>0</td><td>0</td></tr><tr><td></td><td>840</td><td></td><td>0</td><td>0</td><td></td><td>0</td><td>105 34</td><td>35 9</td><td>35 9</td><td>280 9</td><td>280 9</td><td>840</td><td></td><td>41</td><td>41</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td>0</td><td>105</td><td>35</td><td>35</td><td>280</td><td>280</td><td>0</td><td></td><td>840</td><td>840</td></tr><tr><td></td><td>41</td><td>0</td><td>0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>41</td><td>41</td><td>41 840</td></tr><tr><td></td><td>840</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>840</td><td>840</td><td></td></tr></table>

The two methods presented here, along with some of the other Runge– Kutta pairs derived by Fehlberg, have been criticized for a reason associated with computational robustness. This is that the two quadrature formulae characterized by the vectors $b ^ { \intercal }$ and $\hat { b } ^ { \top }$ are identical. Hence, if the differential equation being solved is approximately equal to a pure quadrature problem, then error estimates will be too optimistic.

Although the methods were intended by Fehlberg to be used as order $p$ schemes together with asymptotically correct error estimators, such methods are commonly implemented in a slightly different way. Many numerical analysts argue that it is wasteful to propagate a low order approximation when a higher order approximation is available. This means that the method $( A , \widehat { b } ^ { \intercal } , c )$ , rather than $( A , b ^ { \prime } , c )$ , would be used to produce output values. The order $p + 1$ method will have a different stability region than that of the order $p$ method, and this needs to be taken into account. Also there is no longer an asymptotically correct error estimator available. Many practical codes have no trouble using the difference of the order $p$ and order $p + 1$ approximations to control stepsize, even though it is the higher order result that is propagated.

# 335 The methods of Verner

The methods of Verner overcome the fault inherent in many of the Fehlberg methods, that the two embedded methods both have the same underlying quadrature formula. The following method from Verner (1978) consists of a fifth order method which uses just the first six stages together with a sixth order method based on all of the eight stages. Denote the two output coefficient vectors by $b ^ { \scriptscriptstyle 1 }$ and $\widehat { b } ^ { \intercal }$ , respectively. As usual we give the difference $\widehat { b ^ { \intercal } } - b ^ { \intercal }$ which is used for error estimation purposes:

<table><tr><td rowspan="9">0 1 18 GR 1</td><td>369</td></tr><tr><td>中</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>8</td></tr><tr><td></td><td>81</td></tr><tr><td>五</td><td>56 54</td></tr><tr><td></td><td>11</td></tr><tr><td>11 7 5380 219</td><td>12285 2695</td></tr><tr><td>73 656</td><td>584 1752 52</td></tr><tr><td>8716 891 297 9</td><td>39520 416</td></tr><tr><td>8 1 3015</td><td>27 891 11 4219 5985</td></tr><tr><td>256</td><td>539 0 128 384</td></tr><tr><td>3 80</td><td>78 4 243 77 73 700</td></tr><tr><td></td><td>0</td></tr><tr><td></td><td>25 1120</td></tr><tr><td>57 640</td><td>160 16 1377 121</td></tr><tr><td></td><td>0 891</td></tr><tr><td>0 33 0 640</td><td>2240 320 8320</td></tr></table>

As for the Fehlberg methods, we have a choice as to whether we use the fifth or sixth order approximation as output for propagation purposes. Even though the sixth order choice leaves us without an asymptotically correct local error estimator, the use of this more accurate approximation has definite advantages. In Figure 335(i) the stability regions for the two approximations are plotted. It is clear that stability considerations favour the higher order method.

![](images/15da8a01811fb95f49f1d23ac0f93efbbdcc497a4af4adbf5de2e0e5b57e4f14.jpg)  
Stability regions of embedded Verner method with orders 5 and 6

# 336 The methods of Dormand and Prince

If it is accepted that in using a Runge–Kutta pair, comprising methods of orders $p$ and $p + 1$ , it is the higher order member of the pair that is going to be propagated, then it is logical to take some care over the properties of this order $p { + 1 }$ method. In the methods introduced in Dormand and Prince (1980), this point of view is adopted. The first of these method pairs, referred to by the authors as ‘RK5(4)7M’, is designed to have a low value of the 2-norm of the vector of sixth order error coefficients. This method has the tableau

<table><tr><td>0</td><td>嘉</td><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>中</td><td>44 45</td><td>40 56 15 25360</td><td>32 9 64448</td><td></td><td>212</td><td></td><td></td><td></td></tr><tr><td></td><td>19372 6561</td><td>2187</td><td>6561</td><td></td><td>729</td><td></td><td></td><td></td></tr><tr><td></td><td>9017</td><td>355</td><td>46732</td><td></td><td>49</td><td>5103</td><td></td><td></td></tr><tr><td></td><td>3168</td><td>33</td><td>5247</td><td></td><td>176</td><td>18656</td><td></td><td></td></tr><tr><td>1</td><td>35</td><td>0</td><td>500</td><td></td><td>125</td><td>2187</td><td>11</td><td></td></tr><tr><td></td><td>384</td><td></td><td>1113</td><td>192</td><td></td><td>6784</td><td>84</td><td></td></tr><tr><td></td><td>35</td><td>0</td><td>500</td><td>125</td><td></td><td>2187</td><td>11</td><td>0</td></tr><tr><td></td><td>384</td><td></td><td>1113</td><td></td><td>192</td><td>6784</td><td>84</td><td></td></tr><tr><td></td><td>5179</td><td>0</td><td>7571</td><td></td><td>393</td><td>92097</td><td>187</td><td>1</td></tr><tr><td></td><td>57600</td><td></td><td>16695</td><td></td><td>640</td><td>339200</td><td>2100</td><td>40</td></tr><tr><td></td><td>71</td><td>0</td><td>71</td><td></td><td>71</td><td>17253</td><td>22</td><td>1</td></tr><tr><td></td><td>57600</td><td></td><td></td><td></td><td>1920</td><td>339200</td><td>525</td><td>40</td></tr><tr><td></td><td></td><td></td><td>16695</td><td></td><td></td><td></td><td></td><td></td></tr></table>

It is emphasized that the first of the output approximations has order $p { + } 1 = 5$ and is the result propagated. This method, like those derived in Subsection 333, have the so-called FSAL (‘first same as last’) property in which the vector $b ^ { \scriptscriptstyle 1 }$ , corresponding to the output approximation, has its last component zero and is in fact identical to the last row of $A$ . This means that, while this particular method has seven stages, it operates as though it only had six because the evaluation of the seventh and last stage derivative can be retained to serve as the first stage derivative for the subsequent step.

An alternative choice of free parameters leads to the following method:

<table><tr><td>G 1</td><td rowspan="11"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>G</td><td></td><td>美</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>55 324</td><td></td><td>品</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>108</td><td></td><td></td><td>9</td><td></td><td></td><td></td></tr><tr><td>83 330</td><td>13</td><td></td><td></td><td>110</td><td></td><td></td><td></td></tr><tr><td>19</td><td>22</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td>4</td><td></td><td>1</td><td>27</td><td>22</td><td></td><td></td></tr><tr><td>1</td><td>19</td><td>0</td><td>3</td><td>243</td><td>33</td><td>7</td><td></td></tr><tr><td rowspan="4"></td><td>200</td><td></td><td></td><td>400</td><td>40</td><td>80</td><td></td></tr><tr><td>19</td><td>0</td><td></td><td>243</td><td>33</td><td>7</td><td>0</td></tr><tr><td>200 431</td><td></td><td>333</td><td>400 7857</td><td>40 957</td><td>80 193</td><td>1</td></tr><tr><td>5000</td><td>0</td><td>500</td><td>10000</td><td>1000</td><td>2000</td><td>50</td></tr><tr><td rowspan="2"></td><td>11</td><td></td><td>33</td><td>891</td><td>33</td><td>9</td><td>1</td></tr><tr><td>1250</td><td>0</td><td>500</td><td>5000</td><td>250</td><td>1000</td><td>50</td></tr></table>

Although this has larger error constants overall (as measured by the 2-norm of the sixth order error vector), it has the advantage of a longer stability interval than that of (336a).

For comparison, a method pair with exactly six stages (but of course without the FSAL property) was also presented in the Dormand and Prince paper. This method, given by

<table><tr><td>0</td><td rowspan="16"></td><td colspan="6"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>中</td><td>广 9</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>40</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>9</td><td>6</td><td></td><td></td><td></td></tr><tr><td></td><td>10</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>226</td><td>25</td><td>880</td><td>55</td><td></td><td></td></tr><tr><td></td><td>729</td><td>27</td><td>729</td><td>729</td><td></td><td></td></tr><tr><td></td><td>181</td><td>5</td><td>266</td><td>91</td><td>189</td><td></td></tr><tr><td></td><td>270</td><td></td><td>297</td><td>27</td><td>55</td><td></td></tr><tr><td></td><td>19</td><td>0</td><td>1000</td><td>125</td><td>81</td><td>5</td></tr><tr><td></td><td>216</td><td></td><td>2079</td><td>216</td><td>88</td><td>56</td></tr><tr><td></td><td>31</td><td>0</td><td>190</td><td>145</td><td>351</td><td>1</td></tr><tr><td></td><td>540</td><td></td><td>297</td><td>108</td><td>220</td><td>20</td></tr><tr><td></td><td>11</td><td>0</td><td>10</td><td>55</td><td>27</td><td>11</td></tr><tr><td></td><td>360</td><td></td><td>63</td><td>72</td><td>40</td><td>280</td></tr></table>

seems to be less efficient than the FSAL method.

In the derivation of these method pairs, some attention is devoted to the properties of the approximation which is not propagated. In particular, care is taken to ensure that this approximation has an acceptable stability region. In any implementation of these methods, $\widehat { b } ^ { \intercal }$ does not play a direct role because stepsize is controlled using the vector of coefficients $\boldsymbol { d } ^ { \intercal } = \widetilde { \boldsymbol { b } } ^ { \intercal } - \boldsymbol { b } ^ { \intercal }$ . Rescaling this vector by a non-zero factor is then equivalent to rescaling the userimposed tolerance. From this point of view, the restriction of methods to those for which the non-propagated approximation has good stability properties is unnecessary.

# Exercises 33

33.1 To overcome the perceived disadvantage of using Richardson extrapolation as in Subsection 331, is it feasible to modify the method so that a proportion of the estimated error (331c) is subtracted from the result ${ \hat { y } } _ { n }$ ?   
33.2 Find a problem for which the Merson method gives reasonable error estimating performance.   
33.3 Find a problem which exposes the error estimating deficiencies of the Merson method.   
33.4 Find a method of order 3 embedded in order 4, based on equations (333h)–(333k) with $\begin{array} { r } { B = \frac { 1 } { 6 } } \end{array}$ , $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 3 } = \frac { 1 } { 3 } } \end{array}$ .   
33.5 Find an example of a differential equation system for which the methods given in Subsection 334 are likely to have misleading error estimates.

# 34 Implicit Runge–Kutta Methods

# 340 Introduction

The possibility that the coefficient matrix $A$ in a Runge–Kutta method might not be strictly lower triangular has very important consequences. These more general methods, known as ‘implicit Runge–Kutta methods’, are difficult to actually use, because the explicit stage-by-stage implementation scheme enjoyed by explicit methods is no longer available and needs to be replaced by an iterative computation. However, there are several very good reasons, both theoretical and practical, for moving these methods into the centre of our attention. Perhaps the most important theoretical reason for regarding implicit methods as the standard examples of Runge–Kutta methods is the fact that implicit methods have a group structure. We explore this in detail in Section 38. In the explicit case, methods do not have explicit methods as inverses, and thus explicit methods possess only a semi-group structure. Stiff problems cannot be solved efficiently using explicit methods: this fact is the most important practical reason for paying special attention to implicit methods. However, there are other problem classes, such as differentialalgebraic equations, for which implicit Runge–Kutta methods also have a vital role.

# 341 Solvability of implicit equations

As we have remarked, explicit evaluation of the stages is not, in general, possible for an implicit Runge–Kutta method. However, under mild assumptions on the smoothness of the function $f$ it is easy to see that, for sufficiently small $h$ , the values of $Y _ { 1 }$ , $Y _ { 2 }$ , $\cdot \cdot \cdot$ , $Y _ { s }$ , and hence the output from a step, exist and are unique. Suppose that $f$ satisfies a Lipschitz condition

$$
\| f ( \eta ) - f ( \overline { { \eta } } ) \| \leq L \| \eta - \overline { { \eta } } \|
$$

and consider the stages in a step with size $h$ from initial value $y _ { 0 }$ . We can identify the values of $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , as comprising the components of a vector in $\mathbb { R } ^ { s N }$ which is a fixed point of the mapping

$$
Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] \mapsto \phi ( Y ) = \left[ \begin{array} { c } { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 1 i } f ( Y _ { i } ) } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 2 i } f ( Y _ { i } ) } \\ { \vdots } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { s i } f ( Y _ { i } ) } \end{array} \right] .
$$

Define a metric on $\mathbb { R } ^ { s N }$ by the formula

$$
\rho ( Y , \overline { { Y } } ) = \operatorname* { m a x } _ { i = 1 } ^ { s } \| Y _ { i } - \overline { { Y } } _ { i } \| ,
$$

and estimate $\rho ( \phi ( Y ) , \phi ( { \overline { { Y } } } ) )$ as follows:

$$
\begin{array} { r l } { \displaystyle \rho ( \phi ( Y ) , \phi ( \overline { { Y } } ) ) = \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \parallel \underset { j = 1 } { \overset { s } { \sum } } h a _ { i j } \parallel f ( Y _ { j } ) - \overline { { f } } ( Y _ { j } ) \parallel } & { } \\ { \displaystyle \leq | h | \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \sum _ { j = 1 } ^ { s } | a _ { i j } | L \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \underset { j = 1 } { \overset { s } { \operatorname* { m a x } } } \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \rho ( Y , \overline { { Y } } ) , } \end{array}
$$

so that the conditions for the contraction mapping principle are satisfied as long as

$$
| h | \leq ( L \| A \| _ { \infty } ) ^ { - 1 } .
$$

In practice, this result is of little value, because implicit Runge–Kutta methods are usually used only for stiff problems for which $L$ is typically unreasonably large. In this case it is usually more efficient to use some variant of the Newton method. We discuss this question further in Subsection 360.

# 342 Methods based on Gaussian quadrature

We recall the Legendre polynomials on the interval $[ 0 , 1 ]$

$$
\begin{array} { l } { { P _ { 0 } ^ { * } ( x ) = 1 , } } \\ { { P _ { 1 } ^ { * } ( x ) = 2 x - 1 , } } \\ { { P _ { 2 } ^ { * } ( x ) = 6 x ^ { 2 } - 6 x + 1 , } } \\ { { P _ { 3 } ^ { * } ( x ) = 2 0 x ^ { 3 } - 3 0 x ^ { 2 } + 1 2 x - 1 , } } \\ { { \ } } \\ { { \vdots \ } } \end{array}
$$

where we use the notation $P _ { n } ^ { * }$ for the member of the sequence with degree $n$ . Note that $P _ { n } ^ { * }$ is related to $P _ { n }$ , the Legendre polynomials on the standard symmetric interval $[ - 1 , 1 ]$ , by $P _ { n } ^ { * } ( x ) = P _ { n } ( 2 x - 1 )$ . Amongst the rich collection of properties of this polynomial sequence, we state:

Lemma 342A There exist polynomials $P _ { n } ^ { * } : | 0 , 1 | \to \mathbb { R }$ , of degrees $n$ , for $n = 0 , 1 , 2 , \ldots$ with the properties that

$$
\begin{array} { c } { { \displaystyle { \int _ { 0 } ^ { 1 } P _ { m } ^ { * } ( x ) P _ { n } ^ { * } ( x ) d x = 0 , \qquad m \neq n , } } } \\ { { \displaystyle { P _ { n } ^ { * } ( 1 ) = 1 , \qquad n = 0 , 1 , 2 , \ldots . } } } \end{array}
$$

Furthermore, the polynomials defined by (342a) and (342b) have the following additional properties:

$$
\begin{array} { l } { { P _ { n } ^ { * } ( 1 - x ) = ( - 1 ) ^ { n } P _ { n } ^ { * } ( x ) , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } P _ { n } ^ { * } ( x ) ^ { 2 } d x = \frac { 1 } { 2 n + 1 } , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle P _ { n } ^ { * } ( x ) = \frac { 1 } { n ! } \left( \frac { d } { d x } \right) ^ { n } ( x ^ { 2 } - x ) ^ { n } , \qquad n = 0 , 1 , 2 , \dots , } } \\ { { \displaystyle n P _ { n } ^ { * } ( x ) = ( 2 x - 1 ) ( 2 n - 1 ) P _ { n - 1 } ^ { * } ( x ) - ( n - 1 ) P _ { n - 2 } ^ { * } ( x ) , ~ n = 2 , 3 , 4 , \dots , } } \end{array}
$$

$P _ { n } ^ { * }$ has n distinct real zeros in the interval $( 0 , 1 ) , \quad n { = } 0 , 1 , 2 , \ldots .$

Proof. We give only outline proofs of these well-known results. The orthogonality property (342a), of the polynomials defined by (342e), follows by repeated integration by parts. The value at $x = 1$ follows by substituting $x = 1 + \xi$ in (342e) and evaluating the coefficient of the lowest degree term. The fact that $P _ { n } ^ { * }$ is an even or odd polynomial in $2 x - 1$ , as stated in (342c), follows from (342e). The highest degree coefficients in $P _ { n } ^ { * }$ and $P _ { n - 1 } ^ { * }$ can be compared so that $n P _ { n } ^ { * } ( x ) - ( 2 x - 1 ) ( 2 n - 1 ) P _ { n - 1 } ^ { * } ( x )$ is a polynomial, $Q$ say, of degree less than $n$ . Because $Q$ has the same parity as $n$ , it is of degree less than $n - 1$ . A simple calculation shows that $Q$ is orthogonal to $P _ { k } ^ { * }$ for $k < n - 2$ . Hence, (342f) follows except for the value of the $P _ { n - 2 } ^ { * }$ coefficient, which is resolved by substituting $x = 1$ . The final result (342g) is proved by supposing, on the contrary, that $P _ { n } ^ { * } ( x ) = Q ( x ) R ( x )$ , where the polynomial factors $Q$ and $R$ have degrees $m < n$ and $n - m$ , respectively, and where $R$ has no zeros in $( 0 , 1 )$ . We now find that $\begin{array} { r } { \int _ { 0 } ^ { 1 } P _ { n } ^ { * } ( x ) Q ( x ) d x = 0 } \end{array}$ , even though the integrand is not zero and has a constant sign. 

In preparation for constructing a Runge–Kutta method based on the zeros $c _ { i }$ , $i = 1 , 2 , \dots , s$ of $P _ { s } ^ { * }$ , we look at the associated quadrature formula.

Lemma 342B Let $c _ { 1 }$ , $c _ { 2 } , . . .$ denote the zeros of $P _ { s } ^ { * }$ . Then there exist positive numbers $b _ { 1 }$ , $b _ { 2 }$ , . . . , $b _ { s }$ such that

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) ,
$$

for any polynomial of degree less than $2 s$ . The $b _ { i }$ are unique.

Proof. Choose $b _ { i }$ , $i = 1 , 2 , \dots , s$ , so that (342h) holds for any $\phi$ of degree less than $s$ . Because the $c _ { i }$ are distinct the choice of the $b _ { i }$ is unique. To prove that (342h) holds for degree up to $2 s - 1$ , write

$$
\phi ( x ) = P _ { s } ^ { * } ( x ) Q ( x ) + R ( x ) ,
$$

where the quotient $Q$ and the remainder $R$ have degrees not exceeding $s - 1$ . We now have

$$
\begin{array} { l } { \displaystyle ^ { \int ^ { 1 } } \phi ( x ) d x = \int _ { 0 } ^ { 1 } P _ { s } ^ { * } ( x ) Q ( x ) d x + \int _ { 0 } ^ { 1 } R ( x ) d x = 0 + \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } R ( c _ { i } ) = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) . } \end{array}
$$

To prove the $b _ { i }$ are positive, let $\phi ( x )$ denote the square of the polynomial formed by dividing $P _ { s } ^ { * } ( x )$ by $x - c _ { i }$ . Substitute into (342h), and the result follows. 

We note that the choice of the $c _ { i }$ as the zeros of $P _ { s } ^ { * }$ is the only one possible for (342h) to hold for $\phi$ of degree as high as $2 s - 1$ . If this were not the case, let

$$
S ( x ) = \prod _ { i = 1 } ^ { s } ( x - c _ { i } )
$$

and substitute $\phi ( x ) = S ( x ) Q ( x )$ for any polynomial $Q$ of degree less than $s$ . It is found that $S$ is orthogonal to all polynomials of lower degree and hence, apart from a scale factor, is identical to $P _ { s } ^ { * }$ .

We now consider the possibility of constructing an $s$ -stage implicit Runge– Kutta method with order $2 s$ . If such a method exists, then the values of the

vectors $c$ and $b ^ { \prime }$ are known. In the case $s = 2$ we can explore the possibility of choosing the only free parameters that remain, to satisfy four additional order conditions. Surprisingly, this can be done. Write the tableau in the form

$$
{ \frac { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } } { \frac { 1 } { 2 } + { \frac { \sqrt { 3 } } { 6 } } } } \left| { \begin{array} { c c } { a _ { 1 1 } } & { { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } - a _ { 1 1 } } } \\ { { { \frac { 1 } { 2 } } + { \frac { \sqrt { 3 } } { 6 } } - a _ { 2 2 } } } & { a _ { 2 2 } } \\ { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 2 } } } } \end{array} } \right.  .
$$

For the trees $\bullet , \mathtt { l } , \mathtt { V } , \Psi$ , the order conditions are satisfied. These are just the $B ( 4 )$ conditions introduced in Subsection 321. The remaining trees and the conditions that result from substituting the values from (342i) and simplifying are:

$$
\begin{array} { r l r } { \updownarrow } & { } & { a _ { 1 1 } = a _ { 2 2 } , } \\ { \Updownarrow } & { } & { ( 1 - \sqrt { 3 } ) a _ { 1 1 } + ( 1 + \sqrt { 3 } ) a _ { 2 2 } = \frac { 1 } { 2 } , } \\ { \updownarrow } & { } & { a _ { 1 1 } = a _ { 2 2 } , } \\ { \updownarrow } & { } & { ( 1 + \sqrt { 3 } ) a _ { 1 1 } + ( 1 - \sqrt { 3 } ) a _ { 2 2 } + 2 \sqrt { 3 } ( a _ { 1 1 } ^ { 2 } - a _ { 2 2 } ^ { 2 } ) = \frac { 1 } { 2 } . } \end{array}
$$

These are all satisfied by $\begin{array} { r } { a _ { 1 1 } = a _ { 2 2 } = \frac { 1 } { 4 } } \end{array}$

We also notice that $C ( 2 )$ and $D ( 2 )$ are satisfied by these values, and it is natural to ask if it is possible, in general, to satisfy both $C ( s )$ and $D ( s )$ assuming that the $b ^ { \intercal }$ and $c$ vectors have been chosen to satisfy the quadrature conditions. A crucial link in the chain connecting these conditions is $E ( s , s )$ , given by (321c), and we present a result which expresses the essential connections between them. It will be convenient to write $G ( \eta )$ to represent the fact that a given Runge–Kutta method has order $\eta$ .

# Theorem 342C

$$
\begin{array} { r l r } & { } & { G ( 2 s ) \Rightarrow B ( 2 s ) , } \\ & { } & { G ( 2 s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge C ( s ) \wedge D ( s ) \Rightarrow G ( 2 s ) , } \\ & { } & { B ( 2 s ) \wedge C ( s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge E ( s , s ) \Rightarrow C ( s ) , } \\ & { } & { B ( 2 s ) \wedge D ( s ) \Rightarrow E ( s , s ) , } \\ & { } & { B ( 2 s ) \wedge E ( s , s ) \Rightarrow D ( s ) . } \end{array}
$$

Proof. The first two results (342j), (342k) are consequences of the order conditions. Given that $C ( s )$ is true, all order conditions based on trees containing the structure $\cdots \left[ \tau ^ { k - 1 } \right] \cdot \cdot \cdot$ , with $k \leq s$ , can be removed, as we saw in Subsection 321. Similarly, the condition $D ( s )$ enables us to remove from consideration all trees of the form $[ \tau ^ { k - 1 } [ \cdot \cdot \cdot ] ]$ . Hence, if both $C ( s )$ and $D ( s )$ are true, the only trees remaining are those associated with the trees covered by $B ( 2 s )$ . Hence, (342l) follows. Multiply the matrix of quantities that must be zero according to the $C ( s )$ condition

![](images/71923baf9d87d0db6b0f710dce5d05a07efdb04f42f6b951c4912ea7d5042abd.jpg)  
Schema representing Theorem 342C

$$
{ \left[ \begin{array} { l l l l } { \sum _ { j } a _ { 1 j } - c _ { 1 } } & { \sum _ { j } a _ { 1 j } c _ { j } - { \frac { 1 } { 2 } } c _ { 1 } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { 1 j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { 1 } ^ { s } } \\ { \sum _ { j } a _ { 2 j } - c _ { 2 } } & { \sum _ { j } a _ { 2 j } c _ { j } - { \frac { 1 } { 2 } } c _ { 2 } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { 2 j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { 2 } ^ { s } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \sum _ { j } a _ { s j } - c _ { s } } & { \sum _ { j } a _ { s j } c _ { j } - { \frac { 1 } { 2 } } c _ { s } ^ { 2 } } & { \cdots } & { \sum _ { j } a _ { s j } c _ { j } ^ { s - 1 } - { \frac { 1 } { s } } c _ { s } ^ { s } } \end{array} \right] }
$$

by the non-singular matrix

$$
\left[ \begin{array} { c c c c } { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \\ { b _ { 1 } c _ { 1 } } & { b _ { 2 } c _ { 2 } } & { \cdots } & { b _ { s } c _ { s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { b _ { 1 } c _ { 1 } ^ { s - 1 } } & { b _ { 2 } c _ { 2 } ^ { s - 1 } } & { \cdots } & { b _ { s } c _ { s } ^ { s - 1 } } \end{array} \right]
$$

and the result is the matrix of $E ( s , s )$ conditions. Hence, (342m) follows and, because the matrix multiplier is non-singular, (342n) also follows. The final results (342o) and (342p) are proved in similar way. 

A schema summarizing Theorem 342C is shown in Figure 342(i). To turn this result into a recipe for constructing methods of order $2 s$ we have:

Corollary 342D A Runge–Kutta method has order $2 s$ if and only if its coefficients are chosen as follows:

(i) Choose $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ as the zeros of $P _ { s } ^ { * }$ .   
(ii) Choose $b _ { 1 }$ , $b _ { 2 }$ , . . . , $b _ { s }$ to satisfy the $B ( s )$ condition.   
(iii) Choose $a _ { i j }$ , $i , j = 1 , 2 , \dots , s$ , to satisfy the $C ( s )$ condition.

Proof. If the method has order $2 s$ then $B ( 2 s )$ is satisfied. This implies (i) and (ii). Because the order is $2 s$ , $E ( s , s )$ is satisfied and this, together with $B ( 2 s )$ , implies (iii). Conversely, if (i) and (ii) are satisfied, then $B ( 2 s )$ holds and this in turn implies $E ( s , s )$ . This fact, together with $B ( 2 s )$ , implies $D ( s )$ . Finally, use (342l) to complete the proof. 

We conclude this introduction to the Gauss methods by listing the tableaux for $s = 1 , 2 , 3$ and orders $2 , 4 , 6$ , respectively:

$$
s = 1 , \quad p = 2 ,
$$

$$
{ \frac { { \frac { 1 } { 2 } } \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { 1 } } \end{array} \right. } ; }
$$

$$
s = 2 , \quad p = 4 , 
$$

$s = 3 , \quad p = 6 ,$

# 343 Reflected methods

Given a Runge–Kutta method,

$$
{ \begin{array} { r } { c _ { 1 } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { \rule { 0 ex } { 1. 5 ex } } \\ { b _ { 1 } } \end{array} } { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| }
$$

we construct a method which exactly undoes the work of the given method. If the signs of the coefficients are then all reversed, the resulting method is known as the ‘reflection’ (Scherer, 1977, 1978) of the original method. Because the exact solution is its own reflection, it is natural to consider whether Runge–Kutta methods that have this property have any advantage over other methods. In particular, the Gauss methods are their own reflections, as we will see. Reflected methods are now commonly known as ‘adjoint methods’; for references to modern applications and research, see Hairer, Lubich and Wanner (2006).

For method (343a), the stages and the final output at the end of step $n$ are given by

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ) , \quad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } b _ { j } f ( Y _ { j } ) . } } \end{array}
$$

Subtract (343c) from (343b) so that the stage values are written in terms of the result found at the end of the step. Also rearrange (343c) so that it gives $y _ { n - 1 }$ in terms of $y _ { n }$ . Thus, the result that works in the reverse direction is given by the equations

$$
\begin{array} { c } { { Y _ { i } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) f ( Y _ { j } ) , \quad i = 1 , 2 , \ldots , s , } } \\ { { } } \\ { { y _ { n - 1 } = y _ { n } + h \displaystyle \sum _ { j = 1 } ^ { s } ( - b _ { j } ) f ( Y _ { j } ) . } } \end{array}
$$

This reversed method has tableau

$$
\begin{array} { c } { { c _ { 1 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { c _ { 2 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { c _ { s } - \sum _ { j = 1 } ^ { s } b _ { j } \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { 1 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 1 s } - b _ { s } } } \\ { { a _ { 2 1 } - b _ { 1 } } } & { { a _ { 2 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 2 s } - b _ { s } } } \end{array} \right| } } \\ { { - b _ { 1 } \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad } } \\ { { \frac { c _ { s } - \sum _ { j = 1 } ^ { s } b _ { j } } { - b _ { 1 } } \left| \begin{array} { c c c c c } { { a _ { s 1 } - b _ { 1 } } } & { { a _ { s 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { s s } - b _ { s } } } \\ { { - b _ { 1 } } } & { { - b _ { 2 } } } & { { \cdots } } & { { - b _ { s } } } \end{array} \right| } . } \end{array}
$$

Reverse the signs and we have the tableau for the reflection of (343a)

$$
\begin{array} { r } { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { 1 } } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { 2 } } \\ { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { s } } \\ { \sum _ { j = 1 } ^ { s } b _ { j } - c _ { s } } \end{array}
$$

It is easy to verify the following result, which we present without proof.

Theorem 343A The reflection of the reflection of a Runge–Kutta method is the original method.

If a method satisfies some of the simplifying assumptions introduced in Subsection 321, then we consider the possibility that the reflection of the method satisfies corresponding conditions. To enable us to express these connections conveniently, we write $\widetilde { B } ( \eta )$ , $\bar { C } ( \eta )$ , $\widetilde { D } ( \eta )$ and $\widetilde { E } ( \eta , \zeta )$ to represent $B ( \eta )$ , $C ( \eta )$ , $D ( \eta )$ and $E ( \eta , \zeta )$ , respectively, but with reference to the reflected method. We then have:

Theorem 343B If $\eta$ and $\zeta$ are positive integers, then

$$
\begin{array} { r l r } & { } & { B ( \eta ) \Rightarrow \widetilde { B } ( \eta ) , } \\ & { } & { B ( \eta ) \wedge C ( \eta ) \Rightarrow \widetilde { C } ( \eta ) , } \\ & { } & { B ( \eta ) \wedge D ( \eta ) \Rightarrow \widetilde { D } ( \eta ) , } \\ & { } & { B ( \eta + \zeta ) \wedge E ( \eta , \zeta ) \Rightarrow \widetilde { E } ( \eta , \zeta ) . } \end{array}
$$

Proof. Let $P$ and $Q$ be arbitrary polynomials of degrees less than and $\eta$ less than $\zeta$ , respectively. By using the standard polynomial basis, we see that $B ( \eta ) , C ( \eta ) , D ( \eta )$ and $E ( \eta , \zeta )$ are equivalent respectively to the statements

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } P ( c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) d x , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } P ( c _ { j } ) = \int _ { 0 } ^ { c _ { i } } P ( x ) d x , \quad \quad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P ( c _ { i } ) a _ { i j } = b _ { j } \int _ { c _ { j } } ^ { 1 } P ( x ) d x , \quad \quad j = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } P ( c _ { i } ) a _ { i j } Q ( c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { 0 } ^ { x } Q ( x ) d x \right) d x . } } \end{array}
$$

In each part of the result $B ( \eta )$ holds with $\eta \geq 1$ , and hence we can assume that $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } = 1$ . Hence the reflected tableau can be assumed to be

$$
\begin{array} { r } { { 1 } - c _ { 1 } \left| \begin{array} { c c c c } { b _ { 1 } - a _ { 1 1 } } & { b _ { 2 } - a _ { 1 2 } } & { \cdots } & { b _ { s } - a _ { 1 s } } \\ { 1 - c _ { 2 } } \end{array} \right| } \\ { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad } & { \vdots \qquad } \\ { { 1 } - c _ { s } \left| \begin{array} { c c c c } { b _ { 1 } - a _ { 1 1 } } & { b _ { 2 } - a _ { 1 2 } } & { \cdots } & { b _ { s } - a _ { s s } } \\ { b _ { 1 } - a _ { 2 1 } } & { b _ { 2 } - a _ { 2 2 } } & { \cdots } & { b _ { s } - a _ { 2 s } } \end{array} \right| } \\ { \qquad \quad \textmd { b } _ { 1 } \qquad \textmd { b } _ { 2 } \qquad \textcsc \qquad \textmu _ { s } } \end{array} .
$$

To prove (343d) we have, using (343h),

$$
\sum _ { j = 1 } ^ { s } b _ { j } P ( 1 - c _ { j } ) = \int _ { 0 } ^ { 1 } P ( 1 - x ) d x = \int _ { 0 } ^ { 1 } P ( x ) d x .
$$

To prove (343e) we use (343i) to obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } ( b _ { j } - a _ { i j } ) P ( 1 - c _ { j } ) = \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 0 } ^ { c _ { i } } P ( 1 - x ) d x } } \\ { ~ } \\ { { \displaystyle ~ = \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 1 - c _ { i } } ^ { 1 } P ( x ) d x } } \\ { { \displaystyle ~ = \int _ { 0 } ^ { 1 - c _ { i } } P ( x ) d x . } } \end{array}
$$

Similarly, we prove (343f) using (343j):

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P ( 1 - c _ { i } ) ( b _ { j } - a _ { i j } ) = b _ { j } \int _ { 0 } ^ { 1 } P ( x ) d x - b _ { j } \int _ { c _ { j } } ^ { 1 } P ( 1 - x ) d x } } \\ { { \displaystyle \qquad = b _ { j } \left( \int _ { 0 } ^ { 1 } P ( x ) d x - \int _ { 0 } ^ { 1 - c _ { j } } P ( x ) d x \right) } } \\ { { \displaystyle \qquad = b _ { j } \int _ { 1 - c _ { j } } ^ { 1 } P ( x ) d x . } } \end{array}
$$

Finally, use (343k) to prove (343g):

$$
\begin{array} { l } { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } P ( 1 - c _ { i } ) ( b _ { j } - a _ { i j } ) Q ( 1 - c _ { j } ) } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( 1 - x ) \left( \int _ { 0 } ^ { x } Q ( 1 - x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( 1 - x ) \left( \int _ { 1 - x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { 1 } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) d x \int _ { 0 } ^ { x } Q ( x ) d x - \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { x } ^ { 1 } Q ( x ) d x \right) d x } \\ { \displaystyle = \int _ { 0 } ^ { 1 } P ( x ) \left( \int _ { 0 } ^ { x } Q ( x ) d x \right) d x . } \end{array}
$$

# 344 Methods based on Radau and Lobatto quadrature

It will be shown in Subsection 353 that the Gauss methods have stability regions equal to exactly the left half-plane, and they are therefore A-stable.

For many stiff problems, it is desirable to sacrifice order to gain L-stability, so that the stability function satisfies the property $\begin{array} { r } { \operatorname* { l i m } _ { | z | \to \infty } | R ( z ) | = 0 } \end{array}$ . We explore methods based on quadrature formulae of orders $2 s - 1$ or $2 s \textrm { -- } 2$ . Instead of choosing $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ to obtain as high a degree as possible for polynomials $\phi$ such that

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) ,
$$

we choose either (i) $c _ { 1 } = 0$ , (ii) ${ c _ { s } = 1 }$ or (iii) $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ . The remaining unspecified $c _ { i }$ are then chosen to make (344a) true for a polynomial of degree as high as is still possible.

A ‘Radau I quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ ; a ‘Radau II quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and a ‘Lobatto quadrature formula’ is an interpolational quadrature formula on $[ 0 , 1 ]$ where the abscissae are chosen as the zeros of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ . Note that ‘Lobatto’ is sometimes referred to as ‘Lobatto III’, to bring the naming of these formulae into a consistent pattern. These three quadrature formulae are the ones sought. We have:

Theorem 344A Let $c _ { 1 } < c _ { 2 } < \cdots < c _ { s }$ be chosen as abscissae of the Radau   
I, the Radau II or the Lobatto quadrature formula, respectively. Then: I For the Radau $I$ formula, $c _ { 1 } = 0$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
II For the Radau II formula, ${ c _ { s } = 1 }$ . This formula is exact for polynomials of degree up to $2 s - 2$ .   
III For the Lobatto formula, $c _ { 1 } ~ = ~ 0 , c _ { s } ~ = ~ 1$ . This formula is exact for polynomials of degree up to $2 s - 3$ .   
Furthermore, for each of the three quadrature formulae, $c _ { i } ~ \in ~ [ 0 , 1 ]$ , for   
$i = 1 , 2 , \dots , s$ , and $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ .

Proof. The fact that $x = 1$ is a zero of $P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b). The fact that $x = 0$ is a zero of $P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x )$ and of $P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x )$ follows from (342b) and (342c), with $x = 1$ . Let $\phi$ denote an arbitrary polynomial of degree not exceeding $2 s - 2$ in the Radau cases or $2 s - 3$ in the Lobatto case. Divide this by the polynomial satisfied by the abscissae and write $Q$ for the quotient and $R$ for the remainder. We have in the three cases,

$$
\begin{array} { r l r l } & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) + P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 1 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { R a d a u ~ I I ~ c a s e } , } \\ & { \phi ( x ) = Q ( x ) ( P _ { s } ^ { * } ( x ) - P _ { s - 2 } ^ { * } ( x ) ) + R ( x ) , } & & { \mathrm { L o b a t t o ~ c a s e } . } \end{array}
$$

Methods in the Radau and Lobatto families   

<table><tr><td>Name</td><td>Choice of b&#x27;and c</td><td>Choice of A</td></tr><tr><td>Radau I</td><td>Radau I quadrature</td><td>C(s)</td></tr><tr><td>Radau IA</td><td>Radau I quadrature</td><td>Thereflections of Radau II</td></tr><tr><td>Radau II</td><td>Radau II quadrature</td><td>D(s)</td></tr><tr><td>Radau IA</td><td>Radau II quadrature</td><td>The reflections of Radau I</td></tr><tr><td>Lobatto III</td><td>Lobatto quadrature</td><td>C(s-1)，a1s = a2s=..=αss =0</td></tr><tr><td>Lobatto IIIA</td><td>Lobatto quadrature</td><td>C(s)</td></tr><tr><td>Lobatto IIIB</td><td>Lobatto quadrature</td><td>D(s)</td></tr><tr><td>Lobatto IIIC</td><td>Lobatto quadrature</td><td>Thereflections ofLobatto III</td></tr></table>

Evaluate the approximate integral of $\phi$ written in this form, and the terms involving $Q$ are zero because of orthogonality, and the terms involving $R$ are exact because of the interpolational nature of the quadrature.

In the Radau cases, to prove that the abscissae are always in $\lfloor 0 , 1 \rfloor$ and that the weights are positive, use a homotopy $t \mapsto P _ { s } ^ { * } \pm t P _ { s - 1 } ^ { * }$ , where the upper sign is used for Radau I and the lower sign for Radau II. If any of the weights becomes zero, then for this value of $t$ , the quadrature formula has a greater order than is possible. Furthermore, no abscissae can move outside $[ 0 , 1 ]$ , until $t$ reaches a value $t = 1$ . The proof is slightly more complicated in the Lobatto case, where we use the homotopy $t \mapsto P _ { s } ^ { * } - t P _ { s - 2 } ^ { * }$ . Because of the symmetry of the quadrature formula for all $t$ , $c _ { 1 } = 0$ and ${ c _ { s } = 1 }$ both occur at the same time and this is when $t = 1$ . If a weight passes through zero, then we again obtain a contradiction to the optimality of Gaussian quadrature because two weights vanish simultaneously. The one case not covered by this argument is when $s$ is odd and the weight corresponding to $\begin{array} { r } { c _ { ( s + 1 ) / 2 } = \frac { 1 } { 2 } } \end{array}$ vanishes. However, it is impossible that as $t$ moves from 0 to $1$ , it passes through a point for which this happens because in this case the remaining abscissae would have to be the zeros of $P _ { s - 1 } ^ { * }$ . By (342f), this occurs only for $t = - ( n - 1 ) / n$ , and this has the wrong sign. 

Given the choice of $c$ and $b ^ { \top }$ in accordance with the requirements of Radau I, Radau II or Lobatto quadrature, the choice of $A$ to yield a Runge–Kutta of the same order as for the underlying quadrature formula remains. The most obvious choice, of making the methods as close to explicit as possible, is inappropriate for stiff problems, but makes the method more efficient for nonstiff problems. Other choices can be made in terms of the $C$ and $D$ conditions, and in terms of specific choices of specific elements of $A$ . To distinguish these from the simple (closest to explicit) choices, a letter A, B or C is added to the designation for the method. A summary of many of the methods in the Radau and Lobatto families is given in Table 344(I).

Selected examples of these methods are as follows, where we note that Lobatto IIIB with $s = 2$ does not exist:

$$
\mathrm { R a d a u } \mathrm { ~ I ~ } \qquad ( s = 2 , p = 3 ) ,
$$

![](images/f203af32647fc4e925753f71395de816b9168e09faaa76f5c879fb36d1348986.jpg)

Radau IA ( $s = 2 , p = 3$ ),

Radau II ( $s = 2 , p = 3$ ),

$$
\begin{array} { r } { { \frac { 1 } { 3 } } ~ { \left| \begin{array} { l l } { { \frac { 1 } { 3 } } } & { 0 } \\ { 1 } & { 0 } \end{array} \right| } } \\ { { \frac { 1 } { 4 } } ~ { \frac { 1 } { 4 } } } \end{array}
$$

Radau IIA ( $s = 2 , p = 3$ ),

![](images/d49b79b2c9447690cb0534a32535b4ff31a050cc9cac856b6b52e17a882190ca.jpg)

Radau I ( $s = 3 , p = 5$ ),

Radau IA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">0 6-√6 10</td><td rowspan="2">1 G</td><td rowspan="2">-1-√6 18 88+7√6 360</td><td>-1+√6 18</td></tr><tr><td>88-43√6 360</td></tr><tr><td>6+√6 10</td><td></td><td>88+43√6 360</td><td>88-7√6</td></tr><tr><td></td><td></td><td>16+√6</td><td>360</td></tr><tr><td></td><td>1</td><td>36</td><td>16-√6 36</td></tr></table>

$$
\mathrm { R a d a u \ I I } \qquad ( s = 3 , p = 5 ) ,
$$

<table><tr><td>4-√6 10 4+V6</td><td>24-√6 120 24+11√6</td><td>24-11√6 120 24+√6</td><td>0</td></tr><tr><td>10 1</td><td>120 6-√6</td><td>120 6+√6</td><td>0 0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td></td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td></td></tr></table>

Radau IIA ( $s = 3 , p = 5$ ),

<table><tr><td rowspan="2">4-√6 10 4+√6 10</td><td rowspan="2">88-7√6 360 296+169√6 1800 16-√6</td><td>296-169√6 1800</td><td>-2+3√6 225</td></tr><tr><td>88+7√6 360</td><td>-2-3√6 225</td></tr><tr><td rowspan="2">1</td><td>36</td><td>16+√6 36</td><td>1</td></tr><tr><td>16-√6 36</td><td>16+√6 36</td><td>1</td></tr></table>

Lobatto III ( $s = 2 , p = 2$ ),

<table><tr><td>0 1</td><td>0 0 1 0</td></tr><tr><td></td><td>1 1</td></tr></table>

Lobatto IIIA ( $s = 2 , p = 2$ ),

![](images/786cc1641957243644dabdad9f5e83e2ec1595e38cc7239060923684af77638e.jpg)

Lobatto IIIC ( $s = 2 , p = 2$ ),

![](images/345a7d6c870c6a20ef53fef71a5c1d598e76aefe70ff84b3724613edd711806c.jpg)

$$
\mathrm { L o b a t t o ~ I I I } \qquad ( s = 3 , p = 4 ) ,
$$

<table><tr><td></td><td>0 0</td><td>0</td></tr><tr><td>0</td><td>4 4 0 1</td><td>0 0</td></tr><tr><td></td><td>1 2</td><td>1</td></tr></table>

Lobatto IIIA ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>0 </td></tr><tr><td></td><td>D</td></tr><tr><td></td><td></td></tr><tr><td></td><td>1</td></tr></table>

Lobatto IIIB ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>G</td><td>N 0 0</td></tr><tr><td></td><td>1</td><td>0 1</td></tr></table>

Lobatto IIIC ( $s = 3 , p = 4$ ),

<table><tr><td>0</td><td>GU</td><td>美</td><td>广</td></tr><tr><td rowspan="3"></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

Lobatto III ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td>0 5+√5 60</td><td>0 </td><td>0 15-7√5 60</td><td>0 0</td></tr><tr><td rowspan="3">5+√5 10 1</td><td>5-5 60</td><td>15+7√5 60</td><td>1</td><td>0</td></tr><tr><td>1</td><td>5-5</td><td>5+√5</td><td>0</td></tr><tr><td></td><td>12</td><td>12</td><td></td></tr><tr><td rowspan="3"></td><td>1</td><td>品</td><td>品</td><td>1 12</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

Lobatto IIIA ( $s = 4 , p = 6$ ),

<table><tr><td rowspan="2">0 5-√5 10</td><td rowspan="2">0 11+√5 120</td><td>0</td><td>0</td><td>0</td></tr><tr><td>25-√5 120</td><td>25-13√5 120</td><td>-1+√5 120</td></tr><tr><td>5+√5 10</td><td>11-√5 120</td><td>25+13√5 120</td><td>25+√5 120</td><td>-1-√5 120</td></tr><tr><td rowspan="2">1</td><td>1 12</td><td>5 12</td><td>5 12</td><td>1</td></tr><tr><td>12</td><td>5 12</td><td>品</td><td>12 1 12</td></tr></table>

Lobatto IIIB ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10</td><td></td><td>-1-√5 24 25+√5 120</td><td>-1+√5 24 25-13√5 120</td><td>0 0</td></tr><tr><td>5+√5 10</td><td></td><td>25+13√5 120 11-√5</td><td>25-√5 120 11+√5</td><td>0</td></tr><tr><td>1</td><td></td><td>120</td><td>120</td><td>0</td></tr><tr><td></td><td>1</td><td>5</td><td>5 12</td><td>1 12</td></tr><tr><td></td><td>12</td><td>12</td><td></td><td></td></tr></table>

Lobatto IIIC ( $s = 4 , p = 6$ ),

<table><tr><td>0 5-√5 10 5+√5 10 1</td><td>中</td><td>长 12 4 10+7√5 60 5 12 5</td><td>60 1 12 5</td><td></td></tr></table>

Lobatto III

<table><tr><td>(s=5,p=8), 0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7-√21</td><td>立前</td><td></td><td>13-3√21</td><td>14-3√21</td><td></td></tr><tr><td>14</td><td></td><td>1</td><td>63</td><td>126</td><td>0</td></tr><tr><td>1</td><td></td><td>91+21√21</td><td>美</td><td>91-21V21</td><td>0</td></tr><tr><td></td><td></td><td>576</td><td>13+3V21</td><td>576</td><td></td></tr><tr><td>7+√21</td><td>1 14</td><td>14+3√21</td><td>63</td><td></td><td>0</td></tr><tr><td>14</td><td></td><td>126 7</td><td></td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>18</td><td>2</td><td>18</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td>49</td><td>16</td><td>49</td><td>1</td></tr><tr><td>20</td><td>180</td><td>45</td><td>180</td><td>20</td></tr></table>

Lobatto IIIA ( $s = 5 , p = 8$ ),

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td colspan="2">0</td></tr><tr><td>7-√21 14</td><td>119+3√21</td><td>343-9√21</td><td>392-96√21</td><td>343-69√21</td><td colspan="2">-21+3√21</td></tr><tr><td>1</td><td>1960</td><td>2520 392+105√21</td><td>2205</td><td>2520 392-105√21</td><td colspan="2">1960</td></tr><tr><td>2</td><td>13 320</td><td></td><td>8</td><td></td><td colspan="2">3</td></tr><tr><td>7+√21</td><td>119-3√21</td><td>2880 343+69√21</td><td>45 392+96√21</td><td>2880</td><td colspan="2">320</td></tr><tr><td>14</td><td></td><td></td><td></td><td>343+9√21</td><td colspan="2">-21-3√21</td></tr><tr><td></td><td>1960 1</td><td>2520</td><td>2205</td><td>2520</td><td colspan="2">1960</td></tr><tr><td>1</td><td></td><td>49</td><td>16</td><td>49</td><td colspan="2">1</td></tr><tr><td rowspan="2"></td><td>20</td><td>180</td><td>45</td><td>180</td><td colspan="2">20</td></tr><tr><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td colspan="2">1 20</td></tr><tr><td colspan="4">LobattoIIIB (s=5, P1-2015151-201 =8)，</td><td rowspan="2">-7+√21</td><td rowspan="2">0</td></tr><tr><td>0 7-√21</td><td></td><td>27-√21 120</td><td>15</td></tr><tr><td rowspan="12"></td><td></td><td>343+9√21</td><td>56-15√21</td><td>120 343-69√21</td><td rowspan="2">0</td></tr><tr><td></td><td>2520</td><td>315</td><td>2520</td></tr><tr><td>14</td><td></td><td>49+12√12</td><td>49-12√12</td><td>0</td></tr><tr><td>1</td><td>360</td><td>8 45</td><td>360</td><td></td></tr><tr><td>7+√21</td><td>343+69√21</td><td>56+15√21</td><td>343-9√21</td><td>0</td></tr><tr><td>14</td><td>2520</td><td>315</td><td>2520</td><td></td></tr><tr><td>1</td><td>119-3√21</td><td>13</td><td>119+3√21</td><td>0</td></tr><tr><td></td><td></td><td>360</td><td>45</td><td>360</td><td></td></tr><tr><td></td><td>1 20</td><td>49 180</td><td>16 45</td><td>49 180</td><td>1 20</td></tr></table>

Lobatto IIIC ( $s = 5 , p = 8$ ),

<table><tr><td>0 7-√21 14 1 7+√21</td><td>中</td><td>7 60 29 180 329+105√21 2880 203+30√21</td><td>2 15 47-15√21 315 73 360 47+15√21 315</td><td>7 60 203-30√21 1260 329-105√21 2880</td><td>六 140 3 160</td></tr></table>

# Exercises 34

34.1 Show that there is a unique Runge–Kutta method of order 4 with $s = 3$ for which $A$ is lower triangular with $a _ { 1 1 } = a _ { 3 3 } = 0$ . Find the tableau for this method.

34.2 Show that the implicit Runge–Kutta given by the tableau

<table><tr><td>0 A</td><td>0 0</td></tr><tr><td>1</td><td>云 0 0</td></tr><tr><td></td><td></td></tr><tr><td>0</td><td>0</td></tr><tr><td>1 32 14 81</td><td>药 0 250 5</td></tr></table>

has order 5.

34.3 Find the tableau for the Gauss method with $s = 4$ and $p = 8$ .

34.4 Show that Gauss methods are invariant under reflection.

# 35 Stability of Implicit Runge–Kutta Methods

350 $A$ -stability, $A ( \alpha )$ -stability and L-stability

We recall that the stability function for a Runge–Kutta method (238b) is the rational function

$$
R ( z ) = 1 + z b ^ { \top } ( I - z A ) ^ { - 1 } \mathbf { 1 } ,
$$

and that a method is A-stable if

$$
| R ( z ) | \leq 1 , \quad { \mathrm { w h e n e v e r ~ } } \mathrm { R e } ( z ) \leq 0 .
$$

For the solution of stiff problems, A-stability is a desirable property, and there is sometimes a preference for methods to be L-stable; this means that the method is A-stable and that, in addition,

$$
R ( \infty ) = 0 .
$$

Where A-stability is impossible or difficult to achieve, a weaker property is acceptable for the solution of many problems.

Definition 350A Let $\alpha$ denote an angle satisfying $\alpha \in ( 0 , \pi )$ and let $S ( \alpha )$ denote the set of points $x + i y$ in the complex plane such that $x \ \leq \ 0$ and $- \tan ( \alpha ) | x | \leq y \leq \tan ( \alpha ) | x |$ . A Runge–Kutta method with stability function $R ( z )$ is $A ( \alpha )$ -stable if $| R ( z ) | \leq 1$ for all $z \in S ( \alpha )$ .

The region $S ( \alpha )$ is illustrated in Figure 350(i) in the case of the Runge–Kutta method

<table><tr><td rowspan="4">入 1+ 2 1</td><td>入</td><td>0</td><td>0</td></tr><tr><td>1-</td><td>入</td><td>0</td></tr><tr><td>2 (1-λ)(1-9λ+6)²)</td><td>2(1-λ)(1-6λ+6λ²)</td><td></td></tr><tr><td>1-3入+6λ2</td><td>1-3入+6λ2</td><td>入</td></tr><tr><td rowspan="3"></td><td></td><td>2(1-3&gt;)</td><td></td></tr><tr><td>1+3&gt; 6(1-)2</td><td>3(1-&gt;)2</td><td>1-3入+6λ² 6(1-λ)2</td></tr><tr><td></td><td></td><td></td></tr></table>

where $\lambda \approx 0 . 1 5 8 9 8 4$ is a zero of $6 \lambda ^ { 3 } - 1 8 \lambda ^ { 2 } + 9 \lambda - 1$ . This value of $\lambda$ was chosen to ensure that (350b) holds, even though the method is not A-stable. It is, in fact, $\mathrm { A } ( \alpha )$ -stable with $\alpha \approx 1 . 3 1 9 4 6 \approx 7 5 . 5 9 9 6 ^ { \circ }$ .

# 351 Criteria for $A$ -stability

We first find an alternative expression for the rational function (350a).

Lemma 351A Let $( A , b , c )$ denote a Runge–Kutta method. Then its stability function is given by

$$
R ( z ) = \frac { \operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) } { \operatorname* { d e t } ( I - z A ) } .
$$

![](images/690e3faa45b81170a17aa11fe62c25aaa19bbb6d6d05478e2f1d8e6565fb4688.jpg)  
Figure 350(i) $\mathrm { A } ( \alpha )$ stability region for the method (350c)

Proof. Because a rank 1 $s \times s$ matrix $u v ^ { \top }$ has characteristic polynomial $\operatorname* { d e t } ( I w - u v ^ { \intercal } ) = w ^ { s - 1 } ( w - v ^ { \intercal } u )$ , a matrix of the form $I + u v ^ { \prime }$ has characteristic polynomial $( w - 1 ) ^ { s - 1 } ( w - 1 - v ^ { \mathsf { I } } u )$ and determinant of the form $1 + v ^ { \intercal } u .$ Hence,

$$
\operatorname* { d e t } \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) = 1 + z b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \mathbf { 1 } = R ( z ) .
$$

We now note that

$$
I + z ( \mathbf { 1 } b ^ { \mathsf { T } } - A ) = \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) ( I - z A ) ,
$$

so that

$$
\operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) = R ( z ) \operatorname* { d e t } ( I - z A ) .
$$

Now write the stability function of a Runge–Kutta method as the ratio of two polynomials

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

and define the E-polynomial by

$$
E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) .
$$

Theorem 351B A Runge–Kutta method with stability function $\begin{array} { r l } { R ( z ) } & { { } = } \end{array}$ $N ( z ) / D ( z )$ is A-stable if and only if (a) all poles of $R$ (that is, all zeros of $D$ ) are in the right half-plane and (b) $E ( y ) \ge 0$ , for all real $y$ .

Proof. The necessity of (a) follows from the fact that if $z ^ { * }$ is a pole then $\begin{array} { r } { \operatorname* { l i m } _ { z \to z ^ { * } } | R ( z ) | = \infty } \end{array}$ , and hence $| R ( z ) | > 1$ , for $z$ close enough to $z ^ { * }$ . The necessity of (b) follows from the fact that $E ( y ) < 0$ implies that $| R ( i y ) | > 1$ , so that $| R ( z ) | > 1$ for some $z = - \epsilon + i y$ in the left half-plane. Sufficiency of these conditions follows from the fact that (a) implies that $R$ is analytic in the left half-plane so that, by the maximum modulus principle, $| R ( z ) | > 1$ in this region implies $| R ( z ) | > 1$ on the imaginary axis, which contradicts (b). $\boxed { \begin{array} { r l } \end{array} }$

# 352 Pad´e approximations to the exponential function

Given a function $f$ , assumed to be analytic at zero, with $f ( 0 ) \neq 0$ , and given non-negative integers $\it l$ and $m$ , it is sometimes possible to approximate $f$ by a rational function

$$
f ( z ) \approx { \frac { N ( z ) } { D ( z ) } } ,
$$

with $N$ of degree $\it l$ and $D$ of degree $m$ and with the error in the approximation equal to $O ( z ^ { l + m + 1 } )$ . In the special case $m = 0$ , this is exactly the Taylor expansion of $f$ about $z ~ = ~ 0$ , and when $\mathit { l } \mathit { \Theta } = \mathit { \Theta } 0$ , $D ( z ) / N ( z )$ is the Taylor expansion of $1 / f ( z )$ .

For some specially contrived functions and particular choices of the degrees $\it l$ and $m$ , the approximation will not exist. An example of this is

$$
f ( z ) = 1 + \sin ( z ) \approx 1 + z - { \frac { 1 } { 6 } } z ^ { 3 } + \cdots ,
$$

with $l = 2$ , $m = 1$ because it is impossible to choose $a$ to make the coefficient of $z ^ { 3 }$ equal to zero in the Taylor expansion of $( 1 + a z ) f ( z )$ .

When an approximation

$$
f ( z ) = \frac { N _ { l m } ( z ) } { D _ { l m } ( z ) } + O ( z ^ { l + m + 1 } )
$$

exists, it is known as the ‘ $( l , m )$ Pad´e approximation’ to $f$ . The array of Pad´e approximations for $l , m = 0 , 1 , 2 , \ldots$ is referred to as ‘the Pad´e table’ for the function $f$ .

Pad´e approximations to the exponential function are especially interesting to us, because some of them are equal to the rational functions of some important Gauss, Radau and Lobatto methods. We show that the full Pad´e table exists for this function and, at the same time, we find explicit values for the coefficients in $N$ and $D$ and for the next two terms in the Taylor series for $N ( z ) - \exp ( z ) D ( z )$ . Because it is possible to rescale both $N$ and $D$ by an arbitrary factor, we specifically choose a normalization for which $N ( 0 ) = D ( 0 ) = 1$ .

Theorem 352A Let $l , m \geq 0$ be integers and define polynomials $N _ { l m }$ and $D _ { l m }$ by

$$
\begin{array} { l } { { \displaystyle N _ { l m } ( z ) = \frac { l ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { l } \frac { ( l + m - i ) ! } { i ! ( l - i ) ! } z ^ { i } , } } \\ { { \displaystyle D _ { l m } ( z ) = \frac { m ! } { ( l + m ) ! } \sum _ { i = 0 } ^ { m } \frac { ( l + m - i ) ! } { i ! ( m - i ) ! } ( - z ) ^ { i } . } } \end{array}
$$

Also define

$$
C _ { l m } = ( - 1 ) ^ { m } \frac { l ! m ! } { ( l + m ) ! ( l + m + 1 ) ! } .
$$

Then

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + \frac { m + 1 } { l + m + 2 } C _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) .
$$

Proof. In the case $m = 0$ , the result is equivalent to the Taylor series for $\exp ( z )$ ; by multiplying both sides of (352d) by $\exp ( - z )$ we find that the result is also equivalent to the Taylor series for $\exp ( - z )$ in the case ${ \mathit { l } } = 0$ . We now suppose that $l \geq 1$ and $m \geq 1$ , and that (352d) has been proved if $\it l$ is replaced by ${ \mathit { l } } - 1$ or $m$ replaced is by $m - 1$ . We deduce the result for the given values of $\it l$ and $m$ so that the theorem follows by induction.

Because the result holds with $\it l$ replaced by ${ \mathit { l } } - 1$ or with $m$ replaced by $m - 1$ , we have

$$
\begin{array} { r l r } & { } & { N _ { l - 1 , m } ( z ) - \exp ( z ) D _ { l - 1 , m } ( z ) + \left( 1 + \frac { m + 1 } { l + m + 1 } z \right) C _ { l - 1 , m } z ^ { l + m } = O ( z ^ { l + m + 2 } ) , } \\ & { } & { ( 3 5 2 } \\ & { } & { N _ { l , m - 1 } ( z ) - \exp ( z ) D _ { l , m - 1 } ( z ) + \left( 1 + \frac { m } { l + m + 1 } z \right) C _ { l , m - 1 } z ^ { l + m } = O ( z ^ { l + m + 2 } ) . } \end{array}
$$

Multiply (352e) by $l / ( l + m )$ and (352f) by $m / ( l + m )$ , and we find that the coefficient of $z ^ { l + m }$ has the value

$$
\frac { l } { l + m } C _ { l - 1 , m } + \frac { m } { l + m } C _ { l , m - 1 } = 0 .
$$

The coefficient of $z ^ { l + m + 1 }$ is found to be equal to $C _ { l m }$ . Next we verify that

$$
\frac { l } { l + m } N _ { l - 1 , m } ( z ) + \frac { m } { l + m } N _ { l , m - 1 } ( z ) - N _ { l m } ( z ) = 0
$$

and that

$$
\frac { l } { l + m } D _ { l - 1 , m } ( z ) + \frac { m } { l + m } D _ { l , m - 1 } ( z ) - D _ { l m } ( z ) = 0 .
$$

Pad´e approximations $N _ { l m } / D _ { l m }$ for $l , m = 0 , 1 , 2 , 3$   

<table><tr><td>m</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>1</td><td>1+z</td><td>1+z+ 1 22 2</td><td>1+z+ 1 + 6 1 2 心 23</td></tr><tr><td>1</td><td>1 1-x</td><td>1+ 1 之</td><td>1+ 2 z+ 1 6</td><td>1+ 3 2 + 1 之 2 + 1 4 4 24 </td></tr><tr><td>2</td><td>1</td><td>1- 1+ </td><td>1 2 1+ z+ 1 2</td><td>1 4 z 1+ 3 z+ 3 2 2 + 1</td></tr><tr><td></td><td>1-z+ 1 22</td><td>1- 2 z+ T 22</td><td>12 1- 1 z+ 1 22 12</td><td>20 60 2 z+ 20 1 22</td></tr><tr><td>3</td><td>1</td><td></td><td>1+ 2 z+ 1 20 2</td><td>1+ 1 z+ 1 × 1 2 2</td></tr><tr><td></td><td></td><td></td><td></td><td>10 120</td></tr><tr><td></td><td>1 1-z+ 2 22 2</td><td>1- 4 22 1 23 24</td><td>3 z+ 3 22 23 20 60</td><td>1- 1 z+ 10 22 120 23</td></tr></table>

The coefficient of $z ^ { i }$ in (352g) is

$$
\frac { ( l - 1 ) ! ( l + m - i - 1 ) ! } { ( l + m ) ! i ! ( l - i ) ! } \big ( l ( l - i ) + m l - l ( l + m - i ) \big ) = 0 ,
$$

so that (352g) follows. The verification of (352h) is similar and will be omitted. It now follows that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) + C _ { l m } z ^ { l + m + 1 } + { \frac { m + 1 } { l + m + 2 } } \widetilde { C } _ { l m } z ^ { l + m + 2 } = O ( z ^ { l + m + 3 } ) ,
$$

and we finally need to prove that $\widetilde { C } _ { l m } = C _ { l m }$ . Operate on both sides of (352i) with the operator $( d / d z ) ^ { l + 1 }$ and multiply the result by $\exp ( - z )$ . This gives

$$
\begin{array} { r } { P ( z ) + \left( \frac { m + 1 } { l + m + 2 } \frac { ( l + m + 2 ) ! } { ( m + 1 ) ! } \widetilde { C } _ { l m } - \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } \right) z ^ { m + 1 } = O ( z ^ { m + 2 } ) , } \end{array}
$$

where $P$ is the polynomial of degree $m$ given by

$$
P ( z ) = \frac { ( l + m + 1 ) ! } { m ! } C _ { l m } z ^ { m } - \left( 1 + \frac { d } { d z } \right) ^ { l + 1 } D _ { l m } ( z ) .
$$

It follows from (352j) that $\widetilde { C } _ { l m } = C _ { l m }$ .

The formula we have found for a possible $( l , m )$ Pad´e approximation to $\exp ( z )$ is unique. This is not the case for an arbitrary function $f$ , as the example of the function given by (352a) shows; the $( 2 , 1 )$ approximation is not unique. The case of the exponential function is covered by the following result:

Theorem 352B The function $N _ { l m } / D _ { l m }$ , where the numerator and denominator are given by (352b) and (352c), is the unique $( l , m )$ Pad´e approximation to the exponential function.

Proof. If $\hat { N } _ { l m } / \hat { D } _ { l m }$ is a second such approximation then, because these functions differ by $O ( z ^ { l + m + 1 } )$ ,

$$
N _ { l m } \widehat { D } _ { l m } - \widehat { N } _ { l m } D _ { l m } = 0 ,
$$

Diagonal members of the Pad´e table $N _ { m m } / D _ { m m }$ for $m = 0 , 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td></td><td></td><td></td><td>Nmm Dmm</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td>1+</td><td>1 1</td></tr><tr><td>1</td><td></td><td>1 1 × 2</td><td>1 2 z 2 12</td><td></td></tr><tr><td>2</td><td></td><td>1 + 1</td><td>1 2 12 1 2 2 1 北</td><td>心</td></tr><tr><td>3</td><td></td><td>1 1 z 1 22 10</td><td>10</td><td>120 2 1 120 2</td></tr><tr><td>4</td><td></td><td>1 X 1 z + 28 1 3 2 2 比</td><td>3 + 比 28 心</td><td>1 + 1 84 2 1680 24</td></tr><tr><td>5</td><td>1</td><td>X 1 2 1 1 + 北 72</td><td>1 30240 6 25</td><td>84 2</td><td>1680 1 1008</td></tr><tr><td></td><td>1</td><td>125 1 2 + 一</td><td>22</td><td>1 + 72 20 1</td><td>1 1 1008 2 30240 1</td></tr><tr><td>6</td><td>1 + Z 1 2 1 2</td><td>1 44 北 66 5 1</td><td>66 23 </td><td>× 792 1 792 24 </td><td>× 15840 1 + 15840 25 1 1 × 25</td></tr></table>

because the expression on the left-hand side is $O ( z ^ { l + m + 1 } )$ , and is at the same time a polynomial of degree not exceeding $\boldsymbol { l } + \boldsymbol { m }$ . Hence, the only way that two distinct approximations can exist is when they can be cancelled to a rational function of lower degrees. This means that for some $( l , m )$ pair, there exists a Pad´e approximation for which the error coefficient is zero. However, since $\exp ( z )$ is not equal to a rational function, there is some higher exponent $k$ and a non-zero constant $C$ such that

$$
N _ { l m } ( z ) - \exp ( z ) D _ { l m } ( z ) = C z ^ { k } + O ( z ^ { k + 1 } ) ,
$$

with $k \geq l + m + 2$ . Differentiate (352k) $k - m - 1$ times, multiply the result by $\exp ( - z )$ and then differentiate a further $m + 1$ times. This leads to the contradictory conclusion that $C = 0$ . 

Expressions for the $( l , m )$ Pad´e approximations are given in Table 352(I) for $l , m = 0 , 1 , 2 , 3$ . To extend the information further, Table 352(II) is presented to give the values for $l = m = 0 , 1 , 2 , . . . , 7$ . Similar tables are also given for the first and second sub-diagonals in Tables 352(III) and 352(IV), respectively, and error constants corresponding to entries in each of these three tables are presented in Table 352(V).

First sub-diagonal members of the Pad´e table $N _ { m - 1 , m } / D _ { m - 1 , m }$ for $m = 1 , 2 , \ldots , 7$   

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-1,m Dm-1,m</td><td colspan="4"></td></tr><tr><td>1</td><td colspan="3"></td><td colspan="2">1 1-z</td><td colspan="4"></td></tr><tr><td>2</td><td colspan="3"></td><td>1+</td><td colspan="2"></td><td colspan="3" rowspan="4"></td></tr><tr><td></td><td></td><td></td><td>2-325</td><td>z 1 2 2 1 北</td><td></td></tr><tr><td>3 4</td><td></td><td>35 2 3 十 20 3 1 + 1 2 + 14</td><td>十 比</td><td>2 比 60 1</td><td>20 </td></tr><tr><td>5</td><td></td><td>2 1 4 2 十</td><td>比 5 5 心 23</td><td>22 1 126</td><td>210 2 105 23 840 24 1 1 3024</td></tr></table>

For convenience, we write $V _ { m n } ( z )$ for the two-dimensional vector whose first component is $N _ { l m } ( z )$ and whose second component is $D _ { l m } ( z )$ . From the proof of Theorem 352A, it can be seen that the three such vectors $V _ { l - 1 , m } ( z )$ , $V _ { l , m - 1 } ( z )$ and $V _ { l , m } ( z )$ are related by

$$
l V _ { l - 1 , m } ( z ) + m V _ { l , m - 1 } ( z ) = ( l + m ) V _ { l , m } ( z ) .
$$

Many similar relations between neighbouring members of a Pad´e table exist, and we present three of them. In each case the relation is between three Pad´e vectors of successive denominator degrees.

Theorem 352C If $l , m \geq 2$ then

$$
\begin{array} { l } { { \displaystyle V _ { l m } ( z ) = \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad + \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

Second sub-diagonal members of the Pad´e table

<table><tr><td>m</td><td colspan="2"></td><td colspan="2">Nm-2,m Dm-2,m</td></tr><tr><td>2</td><td></td><td>1 1-x+ 12 22</td></tr><tr><td>3</td><td>4 1 2 4</td><td>1+ 4 z 28</td></tr><tr><td>4</td><td>1 + z 十 1 30 1 2 2 1 一 十 + 心 30 28 1+ 3 3 2 1 </td></tr><tr><td>5</td><td>56 336 1 5 品 5 2 × 22 168 23 336 24 1+ 2 z X 1 1 + 1 15 180 1 1</td></tr><tr><td>6 7</td><td>1 3 Z 1 一 + 1 22 36 2 336 5040 151200 1+ 5 5 2 2 4 1 12 66 2 132 2376 2 95040 7 2 × 7 7 × 7 7 1 12 44 比 264 23 2376 24 31680 25 95040 26</td></tr></table>

Proof. Let

$$
\begin{array} { l } { { \displaystyle V ( z ) = V _ { l m } ( z ) - \Big ( 1 + \frac { m - l } { ( l + m ) ( l + m - 2 ) } z \Big ) V _ { l - 1 , m - 1 } ( z ) } } \\ { { \displaystyle \qquad - \frac { ( l - 1 ) ( m - 1 ) } { ( l + m - 1 ) ( l + m - 2 ) ^ { 2 } ( l + m - 3 ) } z ^ { 2 } V _ { l - 2 , m - 2 } ( z ) . } } \end{array}
$$

It is easy to verify that the coefficients of $z ^ { 0 }$ , $z ^ { 1 }$ and $z ^ { 2 }$ vanish in both components of $V ( z )$ . We also find that

$$
\begin{array} { r l } { [ 1 } & { { } - \exp ( z ) ] V ( z ) = O ( z ^ { l + m - 1 } ) . } \end{array}
$$

If $V ( z )$ is not the zero vector, we find that

$$
z ^ { - 2 } \big [ 1 \  - \exp ( z ) \big ] V ( z ) = O ( z ^ { l + m - 3 } ) ,
$$

contradicting the uniqueness of Pad´e approximations of degrees $( l - 2 , m - 2 )$

Theorems 352D and $3 5 2 \mathrm { E }$ which follow are proved in the same way as Theorem 352C and the details are omitted.

Error constants for diagonal and first two sub-diagonals   

<table><tr><td>m</td><td>Cm-2,m</td><td>m-1,m</td><td>mm</td></tr><tr><td>0</td><td></td><td></td><td>1</td></tr><tr><td>1</td><td></td><td></td><td>1 12</td></tr><tr><td>2</td><td>1</td><td></td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>720 1</td></tr><tr><td>4</td><td>480 1</td><td>7200 1</td><td>100800 1</td></tr><tr><td>5</td><td>75600 1</td><td>1411200 1</td><td>25401600 1</td></tr><tr><td>6</td><td>20321280 1</td><td>457228800 1</td><td>10059033600 1</td></tr><tr><td>7</td><td>8382528000 1 4931800473600</td><td>221298739200 1</td><td>5753767219200 1 4487938430976000</td></tr></table>

Theorem 352D If $l \geq 1$ and $m \geq 2$ then

$$
\begin{array} { l } { \displaystyle { V _ { l m } ( z ) = \left( 1 - \frac { l } { ( l + m ) ( l + m - 1 ) } z \right) V _ { l , m - 1 } ( z ) } } \\ { \displaystyle { \qquad + \frac { l ( m - 1 ) } { ( l + m ) ( l + m - 1 ) ^ { 2 } ( l + m - 2 ) } z ^ { 2 } V _ { l - 1 , m - 2 } ( z ) . } } \end{array}
$$

Theorem 352E If $l \geq 0$ and $m \geq 2$ then

$$
V _ { l m } ( z ) = \Bigl ( 1 - \frac { 1 } { l + m } z \Bigr ) V _ { l + 1 , m - 1 } ( z ) + \frac { m - 1 } { ( l + m ) ^ { 2 } ( l + m - 1 ) } z ^ { 2 } V _ { l , m - 2 } ( z ) .
$$

# 353 A-stability of Gauss and related methods

We consider the possible A-stability of methods whose stability functions correspond to members on the diagonal and first two sub-diagonals of the Pad´e table for the exponential function. These include the Gauss methods and the Radau IA and IIA methods as well as the Lobatto IIIC methods. A corollary is that the Radau IA and IIA methods and the Lobatto IIIC methods are L-stable.

Theorem 353A Let s be a positive integer and let

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

denote the $( s - d , s )$ member of the Pad´e table for the exponential function, where $d = 0$ , $1$ or 2. Then

$$
| R ( z ) | \leq 1 ,
$$

for all complex $\mathcal { L }$ satisfying $\mathrm { R e } z \le 0$ .

Proof. We use the E-polynomial. Because $N ( z ) = \exp ( z ) D ( z ) + O ( z ^ { 2 s - d + 1 } )$ , we have

$$
\begin{array} { l } { { E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) \nonumber } } \\ { { \nonumber } } \\ { { = D ( i y ) D ( - i y ) - \exp ( i y ) D ( i y ) \exp ( - i y ) D ( - i y ) + { \cal O } ( y ^ { 2 s - d + 1 } ) } } \\ { { \nonumber } } \\ { { = { \cal O } ( y ^ { 2 s - d + 1 } ) . } } \end{array}
$$

Because $E ( y )$ has degree not exceeding $2 s$ and is an even function, either $E ( y ) = 0$ , in the case $d = 0$ , or $E ( y ) = C y ^ { 2 s }$ with $C > 0$ , in the cases $d = 1$ and $d = 2$ . In all cases, $E ( y ) \ge 0$ for all real $y$ .

To complete the proof, we must show that the denominator of $R$ has no zeros in the left half-plane. Without loss of generality, we assume that $\mathrm { R e } z < 0$ and we prove that $D ( z ) \neq 0$ . Write $D _ { 0 }$ , $D _ { 1 }$ , $\cdot \cdot \cdot$ , $D _ { s }$ for the denominators of the sequence of Pad´e approximations given by

$$
V _ { 0 0 } , V _ { 1 1 } , \ldots , V _ { s - 1 , s - 1 } , V _ { s - d , s } ,
$$

so that $D ( z ) = D _ { s } ( z )$ . From Theorems 352C, 352D and 352E, we have

$$
D _ { k } ( z ) = D _ { k - 1 } ( z ) + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } D _ { k - 2 } , \quad k = 2 , 3 , \ldots , s - 1 ,
$$

and

$$
D _ { s } ( z ) = ( 1 - \alpha z ) D _ { s - 1 } + \beta z ^ { 2 } D _ { s - 2 } ,
$$

where the constants $\alpha$ and $\beta$ will depend on the value of $d$ and $s$ . However, $\alpha = 0$ if $d = 0$ and $\alpha > 0$ for $d = 1$ and $d = 2$ . In all cases, $\beta > 0$ .

Consider the sequence of complex numbers, $\zeta _ { k }$ , for $k = 1 , 2 , \dots , s$ , defined by

$$
\begin{array} { l } { \displaystyle \zeta _ { 1 } = 1 - \frac 1 2 z , } \\ { \displaystyle \zeta _ { k } = 1 + \frac 1 { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } \zeta _ { k - 1 } ^ { - 1 } , \qquad k = 2 , 3 , \ldots , s - 1 , } \\ { \displaystyle \zeta _ { s } = ( 1 - \alpha z ) + \beta z ^ { 2 } \zeta _ { s - 1 } ^ { - 1 } . } \end{array}
$$

This means that $\zeta _ { 1 } / z = - 1 / 2 + 1 / z$ has negative real part. We prove by induction that $\zeta _ { k } / z$ also has negative real part for $k = 2 , 3 , \ldots , s$ . We see this by noting that

$$
\begin{array} { l } { \displaystyle \frac { \zeta _ { k } } { z } = \frac { 1 } { z } + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } \left( \frac { \zeta _ { k - 1 } } { z } \right) ^ { - 1 } , \qquad k = 2 , 3 , \dots , s - 1 , } \\ { \displaystyle \frac { \zeta _ { s } } { z } = \frac { 1 } { z } - \alpha + \beta \left( \frac { \zeta _ { s - 1 } } { z } \right) ^ { - 1 } . } \end{array}
$$

The fact that $D _ { s } ( z )$ cannot vanish now follows by observing that

$$
\begin{array} { r } { D _ { s } ( z ) = \zeta _ { 1 } \zeta _ { 2 } \zeta _ { 3 } \cdot \cdot \cdot \zeta _ { s } . } \end{array}
$$

Hence, $D = D _ { s }$ does not have a zero in the left half-plane.

Alternative proofs of this and related results have been given byAxelsson (1969, 1972), Butcher (1977), Ehle (1973), Ehle and Picel (1975), Watts and Shampine (1972) and Wright (1970).

# 354 Order stars

We have identified some members of the Pad´e table for the exponential function for which the corresponding numerical methods are A-stable. We now ask: are there other members of the table with this property? It will be seen that everything hinges on the value of $m - l$ , the degree of the denominator minus the degree of the numerator. It is clear that if $m - l < 0$ , A-stability is impossible, because in this case

$$
| R ( z ) | \to \infty ,
$$

as $z  \infty$ , and hence, for some $z$ satisfying $\mathrm { R e } z < 0$ , $| R ( z ) |$ is greater than $^ { 1 }$ . For $m - l \in \{ 0 , 1 , 2 \}$ , A-stability follows from Theorem 353A. Special cases with $m - l > 2$ suggest that these members of the Pad´e table are not A-stable. For the third sub-diagonal, this was proved by Ehle (1969), and for the fourth and fifth sub-diagonals by Nørsett (1974). Based on these observations, Ehle (1973) conjectured that no case with $m - l > 2$ can be A-stable. This result was eventually proved by Wanner, Hairer and Nørsett (1978), and we devote this subsection to introducing the approximations considered in that paper and to proving the Ehle conjecture.

In Subsection 216, we touched on the idea of an order star. Associated with the stability function $R ( z )$ for a Runge–Kutta method, we consider the set of points in the complex plane such that

$$
| \exp ( - z ) R ( z ) | > 1 .
$$

This is known as the ‘order star’ of the method, and the set of points such that

$$
| \exp ( - z ) R ( z ) | < 1
$$

is the ‘dual order star’. The common boundary of these two sets traces out an interesting path, as we see illustrated in Figure 354(i), for the case of the $( 1 , 3 )$ Pad´e approximation given by

$$
R ( z ) = { \frac { 1 + { \frac { 1 } { 4 } } z } { 1 - { \frac { 3 } { 4 } } z + { \frac { 1 } { 4 } } z ^ { 2 } - { \frac { 1 } { 2 4 } } z ^ { 3 } } } .
$$

![](images/245bb3fc37091066fe93197cfed019393d414bf7d740ed1ff3e9f33fd1156ad7.jpg)  
Order star for the $( 1 , 3 )$ Pad´e approximation to exp

In this diagram, the dual order star, which can also be described as the ‘relative stability region’, is the interior of the unshaded region. The order star is the interior of the shaded region.

In Butcher (1987) an attempt was made to present an informal survey of order stars leading to a proof of the Ehle result. In the present volume, the discussion of order stars will be even more brief, but will serve as an introduction to an alternative approach to achieve similar results. In addition to Wanner, Hairer and Nørsett (1978), the reader is referred to Iserles and Nørsett (1991) for fuller information and applications of order stars.

The ‘order star’, for a particular rational approximation to the exponential function, disconnects into ‘fingers’ emanating from the origin, which may be bounded or not, and similar remarks apply to ‘dual fingers’ which are the connected components of the dual star. The following statements summarize the key properties of order stars for applications of the type we are considering. Because we are including only hints of the proofs, we refer to them as remarks rather than as lemmas or theorems. Note that $S$ denotes the order star for a specific ‘method’ and $I$ denotes the imaginary axis.

Remark 354A A method is $A$ -stable if and only if $S$ has no poles in the negative half-plane and $S \cup I = \emptyset$ , because the inclusion of the exponential factor does not alter the set of poles and does not change the magnitude of the stability function on $I$ .

Remark 354B There exists $\rho _ { 0 } ~ > ~ 0$ such that, for all $\rho ~ \geq ~ \rho _ { 0 }$ , functions $\theta _ { 1 } ( \rho )$ and $\theta _ { 2 } ( \rho )$ exist such that the intersection of $S$ with the circle $| z | = \rho$ is the set $\{ \rho \exp ( i \theta ) : \theta _ { 1 } < \theta < \theta _ { 2 } \}$ and where $\begin{array} { l } { \operatorname* { l i m } _ { \rho \to \infty } \theta _ { 1 } ( \rho ) ~ = ~ \pi / 2 } \end{array}$ and $\operatorname* { l i m } _ { \rho \to \infty } \theta _ { 2 } ( \rho ) = 3 \pi / 2$ , because at a great distance from the origin, the behaviour of the exponential function multiplied by the rational function on which the order star is based is dominated by the exponential factor.

![](images/478ddae7b9c90a9cb8002184e20f54a267f735bc8144ad38f973845d858b99b8.jpg)  
Relation between order arrows and order stars

Remark 354C For a method of order $p$ , the arcs $\{ r \exp ( i ( j + \frac { 1 } { 2 } ) \pi / ( p + 1 ) ) :$ $0 \leq r \}$ , where $j = 0 , 1 , \ldots , 2 p + 1$ , are tangential to the boundary of $S$ at 0, because $\exp ( - z ) R ( z ) = 1 + C z ^ { p + 1 } + O \big ( | z | ^ { p + 2 } \big )$ , so that $| \exp ( - z ) R ( z ) | =$ $1 + \mathrm { R e } ( C z ^ { p + 1 } ) + O ( | z | ^ { p + 2 } )$ .

It is possible that $m$ bounded fingers can join together to make up a finger of multiplicity $m$ . Similarly, $m$ dual fingers in $\overline { S }$ can combine to form a dual finger with multiplicity $m$ .

Remark 354D Each bounded finger of $S$ , with multiplicity $_ { m }$ , contains at least m poles, counted with their multiplicities, because, by the Cauchy– Riemann conditions, the argument of $\exp ( - z ) R ( z )$ increases monotonically as the boundary of the order star is traced out in a counter-clockwise direction.

In the following subsection, we introduce a slightly different tool for studying stability questions. The basic idea is to use, rather than the fingers and dual fingers as in order star theory, the lines of steepest ascent and descent from the origin. Since these lines correspond to values for which $R ( z ) \exp ( - z )$ is real and positive, we are, in reality, looking at the set of points in the complex plane where this is the case.

We illustrate this by presenting, in Figure 354(ii), a modified version of Figure 354(i), in which the boundary of the order star is shown as a dashed line and the ‘order arrows’, as we call them, are shown with arrow heads showing the direction of ascent.

# 355 Order arrows and the Ehle barrier

For a stability function $R ( z )$ of order $p$ , define two types of ‘order arrows’ as follows:

Definition 355A The locus of points in the complex plane for which $\phi ( z ) =$ $R ( z ) \exp ( - z )$ is real and positive is said to be the ‘order web’ for the rational function $R$ . The part of the order web connected to 0 is the ‘principal order web’. The rays emanating from 0 with increasing value of $\phi$ are ‘up arrows’ and those emanating from 0 with decreasing $\phi$ are ‘down arrows’.

The up and down arrows leave the origin in a systematic pattern:

Theorem 355B Let $R$ be a rational approximation to exp of exact order $p$ so that

$$
R ( z ) = \exp ( z ) - C z ^ { p + 1 } + O ( z ^ { p + 2 } ) ,
$$

where the error constant $C$ is non-zero. If $C ~ < ~ 0$ ( $C ~ > ~ 0$ ) there are up (down) arrows tangential at $0$ to the rays with arguments $k 2 \pi i / ( p + 1 )$ , $k ~ = ~ 0 , 1 , \ldots , p$ , and down (up) arrows tangential at $0$ to the rays with arguments $( 2 k + 1 ) \pi i / ( p + 1 )$ , $k = 0 , 1 , \dotsc , p$ .

Proof. If, for example, $C ~ < ~ 0$ , consider the set $\{ r \exp ( i \theta ) : r > 0 , \theta \in$ $[ k 2 \pi i / ( p + 1 ) - \epsilon , k 2 \pi i / ( p + 1 ) + \epsilon \}$ , where $\epsilon$ and $r$ are both small and $k \in \{ 0 , 1 , 2 , \ldots , p \}$ . We have

$$
R ( z ) \exp ( - z ) = 1 + ( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) + O ( r ^ { p + 2 } ) .
$$

For $r$ sufficiently small, the last term is negligible and, for $\epsilon$ sufficiently small, the real part of $( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) )$ is positive. The imaginary part changes sign so that an up arrow lies in this wedge. The cases of the down arrows and for $C > 0$ are proved in a similar manner. $\boxed { \begin{array} { r l } \end{array} }$

Where the arrows leaving the origin terminate is of crucial importance.

Theorem 355C The up arrows terminate either at poles of $R$ or at $- \infty$ .   
The down arrows terminate either at zeros of $R$ or at $+ \infty$ .

Proof. Consider a point on an up arrow for which $| z |$ is sufficiently large to ensure that it is not possible that $z$ is a pole or that $z$ is real with $( d / d z ) ( R ( z ) \exp ( - z ) ) ~ = ~ 0$ . In this case we can assume without loss of generality that $\operatorname { I m } ( z ) \geq 0$ . Write $R ( z ) = K z ^ { n } + O ( \vert z \vert ^ { n - 1 } )$ and assume that $K > 0$ (if $K < 0$ , a slight change is required in the details which follow). If $z = x + i y = r \exp ( i \theta )$ , then

$$
\begin{array} { l } { w ( z ) = R ( z ) \exp ( - z ) } \\ { \quad = K r ^ { n } \exp ( - x ) \big ( 1 + O ( r ^ { - 1 } ) \big ) \exp \big ( i ( n \theta - y + O ( r ^ { - 1 } ) ) \big ) . } \end{array}
$$

Because $\theta$ cannot leave the interval $[ 0 , \pi ]$ , then for $w$ to remain real, $y$ is bounded as $z \longrightarrow \infty$ . Furthermore, $w \to \infty$ implies that $x \to - \infty$ .

The result for the down arrows is proved in a similar way.

We can obtain more details about the fate of the arrows from the following result.

Theorem 355D Let $R$ be a rational approximation to exp of order $p$ with numerator degree $n$ and denominator degree $d$ . Let $\widehat { n }$ denote the number of down arrows terminating at zeros and $\hat { d }$ the number of up arrows terminating at poles of R. Then

$$
\widehat { n } + \widehat { d } \geq p .
$$

Proof. There are $p + 1 - \widehat { n }$ down arrows and $p + 1 - { \acute { d } }$ up arrows terminating at $+ \infty$ and $- \infty$ , respectively. Let $\theta$ and $\phi$ be the minimum angles with the properties that all the down arrows which terminate at $+ \infty$ lie within $\theta$ on either side of the positive real axis and all the up arrows which terminate at $- \infty$ lie within an angle $\phi$ on either side of the negative real axis. Hence

$$
2 \theta \geq \frac { ( p - \widehat { n } ) 2 \pi } { p + 1 } , 2 \phi \geq \frac { ( p - \widehat { d } ) 2 \pi } { p + 1 } .
$$

Because up arrows and down arrows cannot cross and, because there is a wedge with angle equal to at least $\pi / ( p + 1 )$ between the last down arrow and the first up arrow, it follows that $2 \theta + 2 \phi + 2 \pi / ( p + 1 ) \le 2 \pi$ . Hence we obtain the inequality

$$
\frac { 2 p + 1 - \widehat { n } - \widehat { d } } { p + 1 } 2 \pi \leq 2 \pi ,
$$

and the result follows.

For Pad´e approximations we can obtain precise values of $\widehat { n }$ and $\hat { d }$ .

Theorem 355E Let $R ( z )$ denote a Pad´e approximation to $\exp ( z )$ , with degrees n (numerator) and d (denominator). Then n of the down arrows terminate at zeros and $d$ of the up arrows terminate at poles.

Proof. Because $p = n + d$ , $n \geq \widetilde n$ and $d \geq \widehat { d }$ , it follows from Theorem 355D that

$$
p = n + d \geq \widetilde { n } + \widetilde { d } \geq p
$$

and hence that $( n - \widetilde { n } ) + ( d - \overset { . } { d } ) = 0$ . Since both terms are non-negative they must be zero and the result follows. 

Before proving the ‘Ehle barrier’, we establish a criterion for A-stability based on the up arrows that terminate at poles.

Theorem 355F A Runge–Kutta method is A-stable only if all poles of the stability function $R ( z )$ lie in the right half-plane and no up arrow of the order web intersects with or is tangential to the imaginary axis.

Proof. The requirement on the poles is obvious. If an up arrow intersects or is tangential to the imaginary axis then there exists $y$ such that

$$
| R ( i y ) \exp ( - i y ) | > 1 .
$$

Because $| \exp ( - i y ) | = 1$ , it follows that $| R ( i y ) | > 1$ and the method is not A-stable. $\sqcup$

We are now in a position to prove the result formerly known as the Ehle conjecture (Ehle, 1973),but which we will also refer to as the ‘Ehle barrier’.

Theorem 355G Let $R ( z )$ denote the stability function of a Runge–Kutta method. If $R ( z )$ is an $( n , d )$ Pad´e approximation to $\exp ( z )$ then the Runge– Kutta is not $A$ -stable unless $d \leq n + 2$ .

Proof. If $d \geq n + 3$ and $p = n + d$ , it follows that $d \geq \frac { 1 } { 2 } ( p + 3 )$ . By Theorem 355E, at least $d$ up arrows terminate at poles. Suppose these leave zero in directions between $- \theta$ and $+ \theta$ from the positive real axis. Then

$$
2 \theta \geq \frac { 2 \pi ( d - 1 ) } { p + 1 } \geq \pi ,
$$

and at least one up arrow, which terminates at a pole, is tangential to the imaginary axis or passes into the left half-plane. If the pole is in the left halfplane, then the stability function is unbounded in this half-plane. On the other hand, if the pole is in the right half-plane, then the up arrow must cross the imaginary axis. In either case, the method cannot be A-stable, by Theorem 355F. 

# 356 AN-stability

Linear stability analysis is based on the linear test problem

$$
y ^ { \prime } ( x ) = q y ( x ) ,
$$

so that

$$
y _ { n } = R ( z ) y _ { n - 1 } ,
$$

where $z = h q$ . Even though this analysis provides useful information about the behaviour of a numerical method when applied to a stiff problem, even more is learned from generalizing this analysis in two possible ways. The first

of these generalizations allows the linear factor $q$ to be time-dependent so that the test problem becomes

$$
y ^ { \prime } ( x ) = q ( x ) y ( x ) .
$$

A second generalization, which we explore in Subsection 357, allows the differential equation to be non-linear.

When (356a) is numerically solved using an implicit Runge–Kutta method $( A , b ^ { \prime } , c )$ , the stage values satisfy the equations

$$
Y _ { i } = y _ { n - 1 } + \sum _ { j = 1 } ^ { s } a _ { i j } h q ( x _ { n - 1 } + h c _ { j } ) Y _ { j } , \qquad i = 1 , 2 , \dots , s ,
$$

and the output result is

$$
y _ { n } = y _ { n - 1 } + \sum _ { i = 1 } ^ { s } b _ { i } h q ( x _ { n - 1 } + h c _ { i } ) Y _ { i } .
$$

Let $Z$ denote the diagonal matrix given by

$$
{ \cal Z } = \left[ \begin{array} { c c c c c } { { h q ( x _ { n - 1 } + h c _ { 1 } ) } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { h q ( x _ { n - 1 } + h c _ { 2 } ) } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { h q ( x _ { n - 1 } + h c _ { s } ) } } \end{array} \right] ~ ,
$$

This makes it possible to write the vector of stage values in the form

$$
Y = y _ { n - 1 } { \bf 1 } + A Z Y ,
$$

so that

$$
Y = ( I - A Z ) ^ { - 1 } \mathbf { 1 } y _ { n - 1 } .
$$

The output value is given by

$$
y _ { n } = y _ { n - 1 } + b ^ { \mathsf { T } } Z Y = \left( 1 + b ^ { \mathsf { T } } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } \right) y _ { n - 1 } = R ( Z ) y _ { n - 1 } .
$$

The function $R ( Z )$ introduced here is the non-autonomous generalization of the linear stability function.

We are mainly concerned with situations in which the stage abscissae are distinct and where they do not interfere with the stages of adjoining steps. This means that we can regard the diagonal elements of $Z$ as different from each other and independent of the values in the steps that come before or after the current step. With this in mind, we define a non-autonomous counterpart of A-stability that will guarantee that we obtain stable behaviour as long as the real part of $q ( x )$ is never positive. This is appropriate because the exact solution to (356a) is never increasing under this assumption, and we want to guarantee that this property carries over to the computed solution.

Definition 356A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘AN-stable’ if the function

$$
R ( Z ) = 1 + b ^ { \intercal } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } ,
$$

where $Z = \operatorname { d i a g } \left( \left[ z _ { 1 } \quad z _ { 2 } \quad \cdots \quad z _ { s } \right] \right)$ is bounded in magnitude by 1 whenever $z _ { 1 }$ , $z _ { 2 }$ , . . . , $z _ { s }$ are in the left half-plane.

It is interesting that a simple necessary and sufficient condition exists for AN-stability. In Theorem 356C we state this criterion and prove it only in terms of necessity. Matters become complicated if the method can be reduced to a method with fewer stages that gives exactly the same computed result. This can happen, for example, if there exists $j ~ \in ~ \{ 1 , 2 , \ldots , s \}$ such that $b _ { j } = 0$ , and furthermore, $a _ { i j } = 0$ for all $i = 1 , 2 , \dots , s$ , except perhaps for $i = j$ . Deleting stage $j$ has no effect on the numerical result computed in a step. We make a detailed study of reducibility in Subsection 381, but in the meantime we identify ‘irreducibility in the sense of Dahlquist and Jeltsch’, or ‘DJ-irreducibility’, (Dahlquist and Jeltsch, 1979) as the property that a tableau cannot be reduced in the sense of Definition 356B.

Definition 356B A Runge–Kutta method is ‘DJ-reducible’ if there exists a partition of the stages

$$
\{ 1 , 2 , \ldots , s \} = S \cup S _ { 0 } ,
$$

with $S _ { 0 }$ non-empty, such that if $i \in S$ and $j \in S _ { 0 }$ ,

$$
b _ { j } = 0 \ a n d \ a _ { i j } = 0 .
$$

The ‘reduced method’ is the method formed by deleting all stages numbered by members of the set $S _ { 0 }$ .

The necessary condition to be given in Theorem 356C will be strengthened under DJ-irreducibility in Corollary 356D.

Theorem 356C Let $( A , b ^ { \prime } , c )$ be an implicit Runge–Kutta method. Then the method is AN-stable only if

$$
b _ { j } \geq 0 , \qquad j = 1 , 2 , \ldots , s ,
$$

and the matrix

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is positive semi-definite.

Proof. If $b _ { j } < 0$ then choose $Z = - t \mathrm { d i a g } ( e _ { j } )$ , for $t$ positive. The value of $R ( Z )$ becomes

$$
R ( Z ) = 1 - t b _ { j } + O ( t ^ { 2 } ) ,
$$

which is greater than $^ { 1 }$ for $t$ sufficiently small. Now consider $Z$ chosen with purely imaginary components

$$
Z = i \mathrm { d i a g } ( v t ) ,
$$

where $v$ has real components and $t$ is a small positive real. We have

$$
\begin{array} { c } { { R ( Z ) = 1 + i t b ^ { \top } \mathrm { d i a g } ( v ) { \bf 1 } - t ^ { 2 } b ^ { \top } \mathrm { d i a g } ( v ) A \mathrm { d i a g } ( v ) { \bf 1 } + O ( t ^ { 3 } ) } } \\ { { { } } } \\ { { = 1 + i t b ^ { \top } v - t ^ { 2 } v ^ { \top } \mathrm { d i a g } ( b ) A v + O ( t ^ { 3 } ) , } } \end{array}
$$

so that

$$
| R ( Z ) | ^ { 2 } = 1 - t ^ { 2 } v ^ { \top } M v + O ( t ^ { 3 } ) .
$$

Since this cannot exceed $^ { 1 }$ for $t$ small and any choice of $v$ , $M$ is positive semi-definite. 

Since there is no practical interest in reducible methods, we might look at the consequences of assuming a method is irreducible. This result was published in Dahlquist and Jeltsch (1979):

Corollary 356D Under the same conditions of Theorem 356C, with the additional assumption that the method is DJ-irreducible,

$$
b _ { j } > 0 , \qquad j = 1 , 2 , \ldots , s .
$$

Proof. Suppose that for $i \leq \overline { { s } }$ , $b _ { i } > 0$ , but that for $i > { \overline { { s } } }$ , $b _ { i } = 0$ . In this case, $M$ can be written in partitioned form as

$$
\begin{array} { r } { M = \left[ \begin{array} { c c } { \overline { { M } } } & { N } \\ { N ^ { \top } } & { 0 } \end{array} \right] } \end{array}
$$

and this cannot be positive semi-definite unless $N = 0$ . This implies that

$$
a _ { i j } = 0 , \quad { \mathrm { w h e n e v e r ~ } } i \leq { \overline { { s } } } < j ,
$$

implying that the method is reducible to a method with only $\overline { { s } }$ stages.

# 357 Non-linear stability

The second generalization of A-stability we consider is the assumption that, even though the function $f$ is non-linear, it satisfies the condition that

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

where $\langle \cdot \rangle$ denotes a semi-inner product, with corresponding semi-norm defined by

$$
| \boldsymbol { u } | = \langle \boldsymbol { u } , \boldsymbol { u } \rangle ^ { 1 / 2 } .
$$

The reason for our interest in the assumption (357a) is that if there are two solutions $y$ and $z$ to the same differential equations, but with possibly different initial values, then the norm difference of $y$ and $z$ satisfies the bound

$$
| y ( x ) - z ( x ) | \leq | y ( x _ { 0 } ) - z ( x _ { 0 } ) | ,
$$

because

$$
{ \frac { d } { d x } } | y ( x ) - z ( x ) | ^ { 2 } = 2 \langle f ( y ( x ) ) - f ( z ( x ) ) , y ( x ) - z ( x ) \rangle \leq 0 .
$$

The corresponding property for a Runge–Kutta method would be that the sequences of computed solutions satisfy

$$
| y _ { n } - z _ { n } | \leq | y _ { n - 1 } - z _ { n - 1 } | .
$$

It would equally be possible to use a simpler type of test problem, such as $Y ^ { \prime } ( x ) = F ( Y ( x ) )$ , where

$$
\begin{array} { r } { \langle \langle g ( U ) , U \rangle \rangle \leq 0 , } \end{array}
$$

because (357a) can be expressed using (357c). If $\langle \cdot \rangle$ is the semi-inner product on $\mathbb { R } ^ { N }$ used in (357a), with $| \cdot |$ the corresponding semi-norm, then we can define a quasi-inner product $\langle \langle \cdot \rangle \rangle$ on $\mathbb { R } ^ { 2 N }$ , with corresponding norm $\| \cdot \|$ , by the formula

$$
\left. \left. \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] , \left[ \begin{array} { l } { \widetilde { u } } \\ { \widetilde { v } } \end{array} \right] \right. \right. = \langle u , \widetilde { u } \rangle - \langle u , \widetilde { v } \rangle - \langle v , \widetilde { u } \rangle + \langle v , \widetilde { v } \rangle .
$$

The semi-norms defined from these quasi-inner products are related by

$$
\left\| \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] \right\| = \langle \langle u - v , u - v \rangle \rangle = | u - v | ^ { 2 } ,
$$

and we can write the condition (357a) in the form

$$
\left. \left. G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right]}  \right) , { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right. \right. \leq 0 ,
$$

where $G$ is defined by

$$
G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right) = { \left[ \begin{array} { l } { f ( u ) } \\ { f ( v ) } \end{array} \right] } .
$$

Furthermore, the requirement on a numerical method (357b) can be written in the form

$$
\| Y _ { n } \| \leq \| Y _ { n - 1 } \| .
$$

Hence we lose no generality in using a test problem which satisfies (357c) rather than the formally more complicated condition (357a). We therefore adopt this requirement, but revert to the more conventional notation of using $\langle \cdot \rangle$ for a standard semi-inner product with $\| \cdot \|$ the corresponding norm.

Even though we have simplified the notation in one way, it is appropriate to generalize it in another. We really need to avoid the use of autonomous problems because of the intimate relationship that will be found between ANstability and the type of non-linear stability we are discussing here. When Definition 357A was first introduced, it was referred to as ‘B-stability’, because it is one step more stringent than A-stability. In the non-autonomous form in which it seems to be a more useful concept, a more natural name is BNstability.

Definition 357A A Runge–Kutta $( A , b ^ { \intercal } , c )$ is ‘BN-stable’ if for any initial value problem

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

satisfying the condition

$$
\langle f ( x , u ) , u \rangle \leq 0 ,
$$

the sequence of computed solutions satisfies

$$
\left\| y _ { n } \right\| \leq \left\| y _ { n - 1 } \right\| .
$$

The crucial result is that for an irreducible non-confluent method, ANstability and BN-stability are equivalent. Because of the fundamental importance of the necessary and sufficient conditions for a Runge–Kutta method to have either, and therefore both, of these properties, we formalize these conditions:

Definition 357B A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘algebraically stable’ if $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ , and if the matrix $M$ , given by

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top } ,
$$

is positive semi-definite.

We now show the sufficiency of this property.

Theorem 357C If a Runge–Kutta method is algebraically stable then it is BN-stable.

Proof. Let $F _ { i } = f ( x _ { n - 1 } + h c _ { i } , Y _ { i } )$ . We note that if $M$ given by (357d) is positive semi-definite, then there exist vectors $v _ { l } \in \mathbb { R } ^ { s }$ , $l = 1 , 2 , \ldots , \overline { { s } } \leq s$ , such that

$$
M = \sum _ { l = 1 } ^ { \overline { { s } } } \mu _ { l } \mu _ { l } ^ { \intercal } .
$$

This means that a quadratic form can be written as the sum of squares as follows:

$$
\xi ^ { \mathsf { T } } M \xi = \sum _ { l = 1 } ^ { \overline { { s } } } ( \mu _ { l } ^ { \mathsf { T } } \xi ) ^ { 2 } .
$$

Furthermore, a quadratic form of inner products

$$
\sum _ { i , j = 1 } ^ { s } m _ { i j } \langle U _ { i } , U _ { j } \rangle
$$

is equal to

$$
\sum _ { l = 1 } ^ { \overline { { s } } } \Big \| \sum _ { i = 1 } ^ { s } \mu _ { l i } U _ { i } \Big \| ^ { 2 } ,
$$

and cannot be negative. We show that

$$
\| y _ { n } \| - \| y _ { n - 1 } \| ^ { 2 } = 2 h \sum _ { i = 1 } ^ { s } b _ { i } \langle Y _ { i } , F _ { i } \rangle - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } \langle F _ { i } , F _ { j } \rangle ,
$$

so that the result will follow. To prove (357e), we use the equations

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } } , } \\ { { \displaystyle Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) F _ { j } } , } \end{array}
$$

which hold for $i = 1 , 2 , \dots , s$ . In each case, form the quasi-inner product with $F _ { i }$ , and we find

$$
\begin{array} { l } { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n - 1 } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \langle F _ { i } , F _ { j } \rangle , } } \\ { { } } \\ { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) \langle F _ { i } , F _ { j } \rangle . } } \end{array}
$$

Hence,

$$
\begin{array} { c } { { 2 h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \big \langle Y _ { i } , F _ { i } \big \rangle = \Big \langle y _ { n } + y _ { n - 1 } , h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } \Big \rangle } } \\ { { = h ^ { 2 } \displaystyle \sum _ { i , j = 1 } ^ { s } ( 2 b _ { i } a _ { i j } - b _ { i } b _ { j } ) \big \langle F _ { i } , F _ { j } \big \rangle . } } \end{array}
$$

Substitute $y _ { n }$ and $y _ { n - 1 }$ from (357f) and (357g) and rearrange to deduce (357e).

Our final aim in this discussion of non-autonomous and non-linear stability is to show that BN-stability implies AN-stability. This will give the satisfactory conclusion that algebraic stability is equivalent to each of these concepts.

Because we have formulated BN-stability in terms of a quasi-inner product over the real numbers, we first need to see how (356a) can be expressed in a suitable form. Write the real and imaginary parts of $q ( x )$ as $\alpha ( x )$ and $\beta ( x )$ , respectively. Also write $y ( x ) = \xi ( x ) + i \eta ( x )$ and write $\zeta ( x )$ for the function with values in $\mathbb { R } ^ { 2 }$ whose components are $\xi ( x )$ and $\eta ( x )$ , respectively.

Thus, because

$$
\begin{array} { c } { { y ^ { \prime } ( x ) = ( \alpha ( x ) + i \beta ( x ) ) ( \xi ( x ) + i \eta ( x ) ) } } \\ { { { } } } \\ { { { } = ( \alpha ( x ) \xi ( x ) - \beta ( x ) \eta ( x ) ) + i ( \beta ( x ) \xi ( x ) + \alpha ( x ) \eta ( x ) ) , } } \end{array}
$$

we can write

$$
\zeta ^ { \prime } ( x ) = Q \zeta ,
$$

where

$$
Q = \left[ \begin{array} { c c } { { \alpha ( x ) } } & { { - \beta ( x ) } } \\ { { \beta ( x ) } } & { { \alpha ( x ) } } \end{array} \right] .
$$

Using the usual inner product we now have the dissipativity property

$$
\begin{array} { r } { \langle Q v , v \rangle = \alpha \| v \| ^ { 2 } \leq 0 , } \end{array}
$$

if $\alpha \leq 0$

What we have found is that the test problem for AN-stability is an instance of the test problem for BN-stability. This means that we can complete the chain of equivalences interconnecting AN-stability, BN-stability and algebraic stability. The formal statement of the final step is as follows:

Theorem 357D If an irreducible non-confluent Runge–Kutta method is BNstable, then it is AN-stable.

# 358 BN-stability of collocation methods

In the case of methods satisfying the collocation conditions

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad \quad \quad i , k = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \quad \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \qquad \quad \quad k = 1 , 2 , \ldots , s , } } \end{array}
$$

a congruence transformation of $M$ , using the Vandermonde matrix

$$
V = { \left[ \begin{array} { l l l l l } { \mathbf { 1 } } & { c } & { c ^ { 2 } } & { \cdots } & { c ^ { s - 1 } } \end{array} \right] } ,
$$

where powers of $c$ are interpreted in a componentwise manner, leads to considerable simplification. Denote

$$
\epsilon _ { k } = \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } - \frac { 1 } { k } , \qquad k = 1 , 2 , \ldots , 2 s ,
$$

so that $\epsilon _ { 1 } = \epsilon _ { 2 } = \cdot \cdot \cdot = \epsilon _ { s } = 0$ . Calculate the $( k , l )$ element of $V ^ { \prime } M V$ . This has the value

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 1 } ^ { s } c _ { i } ^ { k - 1 } \sum _ { j = 1 } ^ { s } c _ { j } ^ { l - 1 } \big ( b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } \big ) } & { } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } \frac { 1 } { l } b _ { i } c _ { i } ^ { k + l - 1 } + \sum _ { j = 1 } ^ { s } \frac { 1 } { k } b _ { j } c _ { j } ^ { k + l - 1 } - \frac { 1 } { k l } } & { } \\ { } & { = \displaystyle \frac { 1 } { l ( k + l ) } + \frac { 1 } { l } \epsilon _ { k + l } + \frac { 1 } { k ( k + l ) } + \frac { 1 } { k } \epsilon _ { k + l } - \frac { 1 } { k l } } \\ { } & { = \displaystyle \frac { k + l } { k l } \epsilon _ { k + l } . } \end{array}
$$

Thus,

$$
{ \boldsymbol { r } } ^ { \mathsf { T } } M V = { \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } \\ & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ & & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { \cdots } & { { \frac { 2 s - 2 } { ( s - 1 ) ^ { 2 } } } \epsilon _ { 2 s - 2 } } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } \\ & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } & { \cdots } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } & { { \frac { 2 s } { s ^ { 2 } } } \epsilon _ { 2 s } } \end{array} \right] } .
$$

A symmetric positive semi-definite matrix cannot have a zero diagonal element unless all the elements on the same row and column are also zero. Hence, we deduce that $\epsilon _ { i } = 0$ for $i = s + 1 , s + 2 , \ldots , 2 s - 1$ . Thus, the only way for $M$ to be positive semi-definite is that

$$
V ^ { \top } M V = \frac { 2 s } { s ^ { 2 } } \epsilon _ { 2 s } e _ { s } e _ { s } ^ { \top }
$$

and that

$$
\epsilon _ { 2 s } \geq 0 .
$$

Combining these remarks with a criterion for (358a), we state:

Theorem 358A A collocation Runge–Kutta method is algebraically stable if and only if the abscissae are zeros of a polynomial of the form

$$
\begin{array} { r } { P _ { s } ^ { * } - \theta P _ { s - 1 } ^ { * } , } \end{array}
$$

where $\theta \geq 0$ .

Proof. Because $\epsilon _ { i } = 0$ for $i = 1 , 2 , \ldots , 2 s - 1$ , it follows that

$$
\int _ { 0 } ^ { 1 } P ( x ) \phi ( x ) d x = 0 ,
$$

where $\phi ( x )$ is a polynomial of degree $s$ , with positive leading coefficient and zeros $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ and $P$ is any polynomial of degree not exceeding $s - 2$ . Furthermore, if $P$ is a polynomial of degree $s - 1$ and positive leading coefficient, the integral in (358c) has the same sign as $- \epsilon _ { 2 s }$ . Because of the orthogonality of $\phi$ and polynomials of degree less than $s - 1$ , $\phi$ is a positive constant multiple of (358b). Apart from a positive factor, we can now evaluate the integral in (358c), with $P ( x ) = P _ { s - 1 } ^ { * } ( x )$ ,

$$
\int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ( P _ { s } ^ { * } ( x ) - \theta P _ { s - 1 } ^ { * } ( x ) ) d x = - \theta \int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ^ { 2 } d x ,
$$

which has the opposite sign to $\theta$ .

A consequence of this result is that both Gauss and Radau IIA methods are algebraically stable. Many other methods used for the solution of stiff problems have stage order lower than $s$ and are therefore not collocation methods. A general characterization of algebraic stable methods is found by using a transformation based not on the Vandermonde matrix $V$ , but on a generalized Vandermonde matrix based on the polynomials that are essentially the same as $P _ { i } ^ { * }$ , for $i = 0 , 1 , 2 , \ldots , s - 1$ .

# 359 The $V$ and $W$ transformations

We refer to the transformation of $M$ using the Vandermonde matrix $V$ to form $V ^ { \prime } M V$ , as the $V$ transformation’. We now introduce the more sophisticated $W$ transformation.

We recall Corollary 356D, which enables us to confine our attention to irreducible methods in which $b ^ { \intercal }$ has only positive elements. Construct a sequence of polynomials $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ with degrees 0, 1, . . . , $s \mathrm { ~ - ~ } 1$ , respectively, which are orthonormal in the sense that

$$
\sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } , \qquad k , l = 1 , 2 , \ldots , s .
$$

We can assume that the leading coefficients are all positive. Define $W$ as the generalized Vandermonde matrix

$$
\begin{array} { r l } { W = [ P _ { 0 } ( c ) \quad P _ { 1 } ( c ) \quad \cdots \quad P _ { s - 1 } ( c ) ] } \\ & { \qquad = \left[ \begin{array} { c c c c } { P _ { 0 } ( c _ { 1 } ) } & { P _ { 1 } ( c _ { 1 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 1 } ) } \\ { P _ { 0 } ( c _ { 2 } ) } & { P _ { 1 } ( c _ { 2 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 2 } ) } \\ { \vdots } & { \vdots } & { \vdots } \\ { P _ { 0 } ( c _ { s } ) } & { P _ { 1 } ( c _ { s } ) } & { \cdots } & { P _ { s - 1 } ( c _ { s } ) } \end{array} \right] . } \end{array}
$$

This matrix can be constructed using the Gram–Schmidt process, or what is algebraically equivalent, from a QR factorization

$$
B ^ { 1 / 2 } V = ( B ^ { 1 / 2 } W ) R ,
$$

where $B ^ { 1 / 2 } = \mathrm { d i a g } ( \sqrt { b _ { 1 } } , \sqrt { b _ { 2 } } , \cdot \cdot \cdot , \sqrt { b _ { s } } )$ and $R$ is upper triangular with positive elements on the diagonal. Note that the coefficients in $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ can be read off from the columns of $R$ .

If $b ^ { \prime }$ and $c$ are weight and abscissa vectors for a Runge–Kutta method of order $p$ , then as long as $k + l \le p + 1$ , (359a) implies that

$$
\int _ { 0 } ^ { 1 } P _ { k - 1 } ( x ) P _ { l - 1 } ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } ,
$$

implying that $P _ { 0 }$ , $P _ { 1 }$ , . . . , $P _ { \left[ \left( p - 1 \right) / 2 \right] }$ are orthonormal with respect to integration on $[ 0 , 1 ]$ . This means that they are necessarily the normalized Legendre polynomials on this interval, given by

$$
P _ { k } ( z ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k - i } { \binom { k } { i } } { \binom { k + i } { i } } z ^ { i } .
$$

In particular, $P _ { 0 } ( x ) \ = \ 1$ and the first column of $W$ is $\mathbf { 1 }$ . Because of orthonormality, it follows that $\mathbf { 1 } ^ { \prime } B W = e _ { 1 } ^ { \mathsf { T } }$ .

We now focus our attention on the matrix $X = W ^ { \prime } B A W$ . This is significant because

$$
\begin{array} { r } { W ^ { \mathsf { T } } M W = X + X ^ { \mathsf { T } } - ( W ^ { \mathsf { T } } B \mathbf { 1 } ) ( \mathbf { 1 } ^ { \mathsf { T } } B W ) = ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) + ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) ^ { \mathsf { T } } . } \end{array}
$$

Because $M$ , and therefore $W ^ { \prime } M W$ , is the zero matrix for the Gauss method, it follows that $\begin{array} { r } { X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top } } \end{array}$ is skew-symmetric. Denote $X$ by $X _ { \mathrm { G } }$ in this special case. We now evaluate $X _ { \mathrm { G } }$ in full.

# Lemma 359A Let

$$
\begin{array} { r } { X _ { G } = W ^ { \top } B A W , } \end{array}
$$

where $A$ and $B = \mathrm { d i a g } ( b )$ are as for the Gauss method of order 2s. Also let

$$
\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } , \qquad k = 1 , 2 , \ldots , s - 1 .
$$

Then

$$
\begin{array} { r } { { \cal X } _ { G } = \left[ \begin{array} { c c c c c c c c } { \frac 1 2 } & { - \xi _ { 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { \xi _ { 2 } } & { 0 } & { - \xi _ { 3 } } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - \xi _ { s - 1 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { \xi _ { s - 1 } } & { 0 } \end{array} \right] . } \end{array}
$$

Proof. From linear combinations of identities included in the condition $E ( s , s )$ , given by (321c), we have

$$
\sum _ { i = 1 } ^ { s } \sum _ { j = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) a _ { i j } \psi ( c _ { j } ) = \int _ { 0 } ^ { 1 } \phi ( u ) \int _ { 0 } ^ { u } \psi ( v ) d v d u ,
$$

for polynomials $\phi$ and $\psi$ each with degree less than $s$ . Use the polynomials $\phi = P _ { k - 1 }$ , $\psi = P _ { l - 1 }$ and we have a formula for the $( k , l )$ element of $X _ { \mathrm { G } }$ . Add to this the result for $k$ and $\it l$ interchanged and use integration by parts. We have

$$
( X _ { \mathrm { G } } ) _ { k l } + ( X _ { \mathrm { G } } ) _ { l k } = \int _ { 0 } ^ { 1 } P _ { k - 1 } ( u ) d u \int _ { 0 } ^ { 1 } P _ { l - 1 } ( v ) d v = \delta _ { k 1 } \delta _ { l 1 } .
$$

This result determines the diagonal elements of $X _ { \mathrm { G } }$ , and also implies the skew-symmetric form of $X _ { \mathrm { G } } ~ - ~ \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top }$ . We now determine the form of the lower triangular elements. If $k > l + 1$ , the integral $\int _ { 0 } ^ { u } P _ { l - 1 } ( v ) d v$ has lower degree than $P _ { k - 1 }$ and is therefore orthogonal to it. Thus, in this case, $( X _ { \mathrm { G } } ) _ { k l } = 0$ . It remains to evaluate $( X _ { \mathrm { G } } ) _ { k , k - 1 }$ for $k = 1 , 2 , \ldots , s - 1$ . The integral $\int _ { 0 } ^ { u } P _ { k - 1 } ( v ) d v$ is a polynomial in $u$ of degree $k$ and can be written in the form $\theta P _ { k } ( u )$ added to a polynomial of degree less than $k$ . The integral of $P _ { k } ( u )$ multiplied by the polynomial of degree less than $k$ is zero, by orthogonality, and the integral reduces to

$$
\int _ { 0 } ^ { 1 } \theta P _ { k } ( u ) ^ { 2 } d u = \theta .
$$

is The value of $\sqrt { 2 k - 1 } \binom { 2 k - 2 } { k - 1 }$ $\theta$ can be found by noting that the coefficient of , with a similar formula for the leading coefficient of in $P _ { k - 1 } ( v )$ $P _ { k } ( u )$

Hence,

$$
( X _ { \mathrm { G } } ) _ { k , k - 1 } = \theta = { \frac { { \frac { 1 } { k } } { \sqrt { 2 k - 1 } } { \binom { 2 k - 2 } { k - 1 } } } { { \sqrt { 2 k + 1 } } { \binom { 2 k } { k } } } } = { \frac { 1 } { 2 { \sqrt { 4 k ^ { 2 } - 1 } } } } .
$$

The computation of elements of $X ~ = ~ W ^ { \top } B A W$ for any Runge–Kutta method, for which $W$ makes sense, will lead to the same $( k , l )$ elements as in $X _ { \mathrm { G } }$ as long as $k + l \le p + 1$ . We state this formally.

Corollary 359B Let $( A , b , c )$ denote a Runge–Kutta method for which $B =$ $\mathrm { d i a g } ( b )$ is positive definite and for which the abscissae are distinct. Define $W$ by (359b) and $X$ by $X = W ^ { \prime } B A W$ . Then $X _ { k l } ~ = ~ ( X _ { G } ) _ { k l }$ , as long as $k + l \le p + 1$ .

The $W$ transformation is related in an interesting way to the $C ( m )$ and $D ( m )$ conditions, which can be written in the equivalent forms

$$
\begin{array} { c c } { { C ( m ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } P _ { k - 1 } ( c _ { j } ) = \int _ { 0 } ^ { c _ { i } } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ i = 1 , 2 , \ldots , s , } } \\ { { D ( m ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) a _ { i j } = b _ { j } \int _ { c _ { j } } ^ { 1 } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ j = 1 , 2 , \ldots , s . } } \end{array}
$$

It follows from these observations that, if $B ( m )$ and $C ( m )$ are true, then the first $m$ columns of $X$ will be the same as for $X _ { \mathrm { G } }$ . Similarly, if $B ( m )$ and $D ( m )$ , then the first $m$ rows of $X$ and $X _ { \mathrm { G } }$ will agree.

Amongst the methods known to be algebraically stable, we have already encountered the Gauss and Radau IIA methods. We can extend this list to include further methods.

Theorem 359C The Gauss, Radau IA, Radau IIA and Lobatto IIIC methods are algebraically stable.

Proof. We have already settled the Gauss and Radau IIA cases, using the $V$ transformation, making use of the $C ( s )$ and $B ( p )$ conditions, as in Theorem 358A.

To prove the result for Radau IA methods, use the $D ( s )$ and $B ( 2 s - 1 )$ conditions:

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } & { } \\ { = \displaystyle \frac { 1 } { k } \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \displaystyle \frac { 1 } { l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ^ { l } ) c _ { i } ^ { k - 1 } - \displaystyle \frac { 1 } { k l } } & { } \\ { \displaystyle } & { = \displaystyle \frac { 1 } { k l } - \frac { k + l } { k l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } . } \end{array}
$$

The value of this expression is zero if $k + l \le 2 s - 1$ . Although it can be verified directly that the value is positive in the remaining case $k = l = s$ , it is enough to show that the $( 1 , 1 )$ element of $M$ is positive, because this will have the same sign as the only non-zero eigenvalue of the rank 1 matrix $V ^ { \prime } M V$ . We note that all values in the first column of $A$ are equal to $b _ { 1 }$ because these give the unique solution to the $D ( s )$ condition applied to the first column. Hence, we calculate the $( 1 , 1 )$ element of $M$ to be

$$
2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = b _ { 1 } ^ { 2 } > 0 .
$$

In the case of the Lobatto IIIC methods, we can use a combination of the $C ( s - 1 )$ and $D ( s - 1 )$ conditions to evaluate the $( k , l )$ and $( l , k )$ elements of $M$ , where $k \le s - 1$ and $l \leq s$ . The value of these elements is

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \frac { 1 } { k } \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = 0 . } } \end{array}
$$

The final step of the proof is the same as for the Radau IA case, because again $a _ { i 1 } = b _ { 1 }$ , for $i = 1 , 2 , \dots , s$ . 

The $V$ transformation was used to simplify questions concerning algebraic stability in Butcher (1975) and Burrage (1978). The $W$ transformation was introduced in Hairer and Wanner (1981, 1982). Recent results on the $W$ transformation, and especially application to symplectic methods, were presented in Hairer and Leone (2000) .

# Exercises 35

35.1 Show that a Runge–Kutta method with $R ( z ) ~ = ~ N ( z ) / D ( z )$ , where $N$ and $D$ have no common factors, cannot be A-stable unless the coefficients in $D ( z )$ alternate in sign.

35.2 Show that the error constant for the $( s - d , s )$ Pad´e approximation to the exponential function has sign $( - 1 ) ^ { s }$ . Deduce that, if $d > 0$ and $d = 3$ (mod 4) or $d = 0$ (mod 4), then $| R ( i y ) | > 0$ , for sufficiently small real $y$ .

35.3 Show that the implicit Runge–Kutta method with tableau

<table><tr><td>#云</td><td>A 2</td></tr><tr><td>1</td><td></td></tr><tr><td>1</td><td></td></tr><tr><td></td><td>1</td></tr></table>

is A-stable but not AN-stable.

35.4 For the $( 0 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 5$ .

35.5 For the $( 1 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 7$ .

# 36 Implementable Implicit Runge–Kutta Methods

360 Implementation of implicit Runge–Kutta methods

Because of the implicit nature of these methods, every step requires the solution of an algebraic system. For an $s$ -stage method with an $N$ -dimensional problem, there are $s N$ unknowns to evaluate and these satisfy $s N$ equations. If $f$ is nonlinear, then the large system of equations to be solved is also nonlinear. However, there are linear parts of it, and it may be possible to exploit this in their numerical solution. Let $A$ denote the coefficient matrix; then the stage values need to be computed as solutions to the system of equations

$$
\begin{array} { l } { { \displaystyle Y _ { 1 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 1 j } f ( Y _ { j } ) } . } \\ { ~ } \\ { { \displaystyle Y _ { 2 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 2 j } f ( Y _ { j } ) } . } \\ { { \displaystyle \quad \vdots \qquad } } \\ { { \displaystyle Y _ { s } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { s j } f ( Y _ { j } ) } . } \end{array}
$$

For an $N$ -dimensional differential equation system, this amounts to a system of $s N$ non-linear equations.

We consider how to solve these equations using a full Newton method. This requires going through the following steps: