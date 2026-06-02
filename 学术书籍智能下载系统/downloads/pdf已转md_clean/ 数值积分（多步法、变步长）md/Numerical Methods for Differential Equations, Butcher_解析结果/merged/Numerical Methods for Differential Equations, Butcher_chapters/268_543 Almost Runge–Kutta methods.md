# 543 Almost Runge–Kutta methods

The characteristic feature of explicit Runge–Kutta methods, that only minimal information computed in a step is passed on as input to the next step, is a great advantage of this type of method but it is also a perceived disadvantage. The advantage lies in excellent stability properties, while the disadvantage lies in the low stage order to which the second and later stages are restricted. Almost Runge–Kutta methods (ARK) are an attempt to retain the advantage but overcome some of the disadvantages.

Recall the method (505a). Evaluate its stability matrix and we find

$$
{ \begin{array} { r l } & { M ( z ) = V + z B ( I - z A ) ^ { - 1 } U } \\ & { = { \left[ \begin{array} { l l } { 1 + { \frac { 5 } { 6 } } z + { \frac { 1 } { 3 } } z ^ { 2 } + { \frac { 1 } { 4 8 } } z ^ { 3 } } & { { \frac { 1 } { 6 } } + { \frac { 1 } { 6 } } z + { \frac { 7 } { 4 8 } } z ^ { 2 } + { \frac { 1 } { 4 8 } } z ^ { 3 } } & { { \frac { 1 } { 4 8 } } z ^ { 2 } + { \frac { 1 } { 9 6 } } z ^ { 3 } } \\ { z + { \frac { 5 } { 6 } } z ^ { 2 } + { \frac { 1 } { 3 } } z ^ { 3 } + { \frac { 1 } { 4 8 } } z ^ { 4 } } & { { \frac { 1 } { 6 } } z + { \frac { 1 } { 6 } } z ^ { 2 } + { \frac { 7 } { 4 8 } } z ^ { 3 } + { \frac { 1 } { 4 8 } } z ^ { 4 } } & { { \frac { 1 } { 4 8 } } z ^ { 3 } + { \frac { 1 } { 9 6 } } z ^ { 4 } } \\ { z + { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 7 } { 1 2 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } } & { - 1 + { \frac { 1 } { 2 } } z - { \frac { 1 } { 1 2 } } z ^ { 2 } + { \frac { 5 } { 2 4 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } } & { { \frac { 1 } { 4 8 } } z ^ { 4 } } \end{array} \right] } . } \end{array} }
$$

The eigenvalues of this matrix are

$$
\sigma ( M ( z ) ) = \left\{ 1 + z + { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 1 } { 6 } } z ^ { 3 } + { \frac { 1 } { 2 4 } } z ^ { 4 } , 0 , 0 \right\} ,
$$

Calculation of stages and stage derivatives for the method (505a)   

<table><tr><td rowspan="2">α</td><td colspan="9"></td></tr><tr><td>α(0）</td><td>α(.)</td><td>a(1</td><td>a(v）</td><td>a(E）</td><td>α()</td><td>a(）</td><td>α（Y）</td><td>(） α</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>D</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>S</td><td>0</td><td>0</td><td>1</td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td></tr><tr><td>m1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>04 2</td><td>0 2</td><td>0 2</td><td>电</td><td>中</td></tr><tr><td>n1D</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1 2</td><td>美品 2</td><td></td></tr><tr><td>m2</td><td>1</td><td>1</td><td></td><td>1+0 16</td><td>1+204 32</td><td>1+05 16</td><td>1+206 32</td><td>03+207 32</td><td>04+208 32</td></tr><tr><td>m2D</td><td>0</td><td>1</td><td>#</td><td>1</td><td>1</td><td>1854</td><td>1</td><td>1+0 16</td><td>1+204 32</td></tr><tr><td>m3</td><td>1</td><td>1</td><td></td><td>1-0 4</td><td>1-204</td><td></td><td></td><td>1-207 8</td><td>1-408 16</td></tr><tr><td>m3D</td><td>0</td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td>1-0</td><td>1-204</td></tr><tr><td>m4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>G5</td><td>1 4</td><td></td><td>4</td><td>8</td></tr><tr><td>m4D</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>立</td><td>24 1</td></tr><tr><td>E</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>14</td><td>1</td><td>1</td><td>2</td></tr><tr><td>E</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>12</td><td></td></tr><tr><td>E</td><td>0</td><td>0</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>2 0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">cs&lt;c&lt;cB</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>0</td><td>0</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1 4</td></tr></table>

so that it is RK stable. Other features of the method are that the minimal information passed between steps is enough to push the stage order up to 2, and that the third input and output vector need not be evaluated to great accuracy because of what will be called ‘annihilation conditions’. These conditions ensure that errors like $O ( h ^ { 3 } )$ in the input vector $y _ { 3 } ^ { [ n - 1 ] }$ only affect the output results by $O ( h ^ { 5 } )$ .

Assume that the three input approximations are represented by $\xi _ { 1 } = 1$ , $\xi _ { 2 } = D$ and $\xi _ { 3 }$ , where we assume only that

$$
\xi _ { 3 } ( \emptyset ) = \xi _ { 3 } ( \bullet ) = 0 \qquad \mathrm { a n d } \qquad \xi _ { 3 } ( { \mathfrak { s } } ) = 1 .
$$

Thus, y[1 $y _ { 1 } ^ { [ n - 1 ] } = y ( x _ { n - 1 } ) , y _ { 2 } ^ { [ n - 1 ] } = h y ^ { \prime } ( x _ { n - 1 } ) , y _ { 3 } ^ { [ n - 1 ] } = h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { 3 } )$ . The output approximations are computed by first evaluating the representations of the stage values and stage derivatives. Since we are only working to order 5 accuracy in the output results, it will be sufficient to evaluate the stages only up to order 4. Denote the representations of the four stage values by $\eta _ { i }$ , $i = 1 , 2 , 3 , 4$ . Also, denote the values of $\xi _ { 3 } ( t )$ for trees of orders 3 and 4 by $\theta _ { i }$ , $i = \dag { 3 , 4 , . . . , 8 }$ . Details of the calculation of stage values are shown in Table 543(I).

Output and input values for (505a) evaluated at fifth order trees   

<table><tr><td>α</td><td colspan="8">a(）a(） a（）a（j） a（）a（Y）a（y）（）a（）</td></tr><tr><td></td><td colspan="8"></td></tr><tr><td>S3</td><td>0g 010 1</td><td>011</td><td>012</td><td>013</td><td>014</td><td>015</td><td>016</td><td>017</td></tr><tr><td>R</td><td>1 240</td><td>1+503</td><td>1+1004 480</td><td>1 480</td><td>1 120</td><td>1 240</td><td>1+503</td><td>1+1004</td></tr><tr><td></td><td>120</td><td>240 0</td><td>0</td><td></td><td>0</td><td>0</td><td>240</td><td>480</td></tr><tr><td></td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td></tr><tr><td></td><td>-1</td><td></td><td></td><td></td><td>1</td><td>-1</td><td>4</td><td>1</td></tr><tr><td></td><td></td><td>-</td><td></td><td>-</td><td>1</td><td></td><td></td><td></td></tr></table>

The output results are intended to represent approximations to $E \xi _ { 1 }$ , $E \xi _ { 2 }$ and $E \xi _ { 3 }$ . Write the representation of $y _ { i } ^ { \left[ n \right] }$ by $E \hat { \xi } _ { i }$ , for $i = 1 , 2 , 3 .$ . We calculate $\widehat { \xi } _ { i }$ up to order 5 trees so that we not only verify fourth order behaviour, but also obtain information on the principal terms in the local truncation error. As a first step in this analysis, we note that, to order 4, $E \widehat { \xi } _ { 1 } = E$ and hence $\widehat { \xi _ { 1 } } = 1$ . Similarly $\widehat { \xi _ { 2 } } = D$ to fourth order. Up to fourth order, we have calculated the value of $\begin{array} { r } { E \xi _ { 3 } = - \frac 1 3 \eta _ { 1 } D - \frac 2 3 \eta _ { 3 } D + 2 \eta _ { 4 } D - \xi _ { 2 } } \end{array}$ and $\widehat { \xi _ { 3 } }$ is also given in Table 543(I).

If the calculations are repeated using the specific values $\lvert \theta _ { 3 } , \theta _ { 4 } , \theta _ { 5 } , \theta _ { 6 } , \theta _ { 7 } , \theta _ { 8 } \rvert$ $= [ - 1 , - \frac { 1 } { 2 } , 1 , \frac { 1 } { 2 } , \frac { 1 } { 2 } , \frac { 1 } { 4 } ]$ , then we have $\widehat { \xi _ { i } } = \xi _ { i } + H _ { 4 }$ so that, relative to a starting method defined by $\xi _ { i }$ , $i = 1 , 2 , 3$ , the method has order 4. However, a starting value defined for arbitrary values of $\theta _ { 3 }$ , $\theta _ { 4 }$ , . . . , $\theta _ { 8 }$ produces the specific choice given by the components of $\widehat { \xi _ { 3 } }$ after a single step. To investigate this method more precisely, the values of $\xi _ { 1 }$ , $\widehat { \xi _ { 2 } }$ and $\widehat { \xi _ { 3 } }$ have been calculated also for fifth order trees and these are shown in Table 543(II).

A reading of this table suggests that the method not only exhibits fourth order behaviour but also has reliable behaviour in its principal error terms. This is in spite of the fact that the starting method provides incorrect contributions of third and higher order elementary differentials, because these inaccuracies have no long term effect. The components of the error terms in the first output component depend on $\theta _ { 3 }$ and $\theta _ { 4 }$ after a single step, but this effect disappears in later steps.

In Subsection 544 we consider order 3 ARK methods, and we then return in Subsection 545 to a more detailed study of order 4 methods. However, we first discuss some questions which apply to both orders.

Because we will require methods in these families to have stage order 2, the matrix $U$ will need to be of the form

$$
U = [ \mathbf { 1 } \quad c - A \mathbf { 1 } \quad { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c ]
$$

and we will assume this throughout. We also note that the stability matrix $M ( z ) = V + z B ( I - z A ) ^ { - 1 } U$ is always singular because $z e _ { 1 } ^ { \intercal } - e _ { 2 } ^ { \intercal }$ is an eigenvalue of this matrix. We see this by observing that $z e _ { p } ^ { \intercal } ( I - z A ) = ( - z e _ { 1 } ^ { \intercal } + e _ { 2 } ^ { \intercal } ) B$ and $( z e _ { 1 } ^ { 1 } - e _ { 2 } ^ { 1 } ) V = z e _ { p } ^ { 1 } U$ .

544 Third order, three-stage ARK methods

Since $r = s = 3$ , we will write the coefficient matrices as follows:

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { 0 } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { u _ { 1 2 } } & { u _ { 1 3 } } \\ { 1 } & { u _ { 2 2 } } & { u _ { 2 3 } } \\ { 1 } & { b _ { 0 } } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } \end{array} \right] } .
$$

Denote the abscissa vector by $\boldsymbol { c } = [ c _ { 1 } , c _ { 2 } , 1 ] ^ { \scriptscriptstyle 1 }$ and also write $\boldsymbol { b } ^ { \intercal } = [ b _ { 1 } , b _ { 2 } , 0 ]$ and $\beta ^ { \uparrow } = [ \beta _ { 1 } , \beta _ { 2 } , \beta _ { 3 } ]$ .

Because we will require the method to have stage order 2, the matrix $U$ will need to be of the form given by (543a). For the method to have order 3, and at the same time be RK stable, it is necessary that the trace of $M$ is equal to the Taylor expansion of the non-zero eigenvalue. Thus,

$$
\mathrm { r } ( M ) = \mathrm { t r } ( V ) + z \mathrm { t r } ( B U ) + z ^ { 2 } \mathrm { t r } ( B A U ) + z ^ { 3 } \mathrm { t r } ( B A ^ { 2 } U ) = 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } ,
$$

and it follows that

$$
\begin{array} { c c c } { \operatorname { t r } ( B U ) = 1 , } & { \operatorname { t r } ( B A U ) = \frac { 1 } { 2 } , } & { \operatorname { t r } ( B A ^ { 2 } U ) = \frac { 1 } { 6 } , } \end{array}
$$

where we note that $\operatorname { t r } ( V ) = 1$ , because of the form of $V$ .

To obtain order 3 accuracy for the first output value, it is only necessary that

$$
\begin{array} { r } { b _ { 0 } + b _ { 1 } + b _ { 2 } = 1 , \quad b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } , \quad b _ { 1 } c _ { 1 } ^ { 2 } + b _ { 2 } c _ { 2 } ^ { 2 } = \frac { 1 } { 3 } , } \end{array}
$$

and to obtain an order 2 approximation to the scaled second derivative for the third output value, we require that

$$
\begin{array} { r } { \beta _ { 0 } + \boldsymbol { \beta } ^ { \top } \mathbf { 1 } = 0 , } \\ { \boldsymbol { \beta } ^ { \top } c = 1 . } \end{array}
$$

Note that $\begin{array} { r } { b ^ { \intercal } A c = \frac { 1 } { 6 } } \end{array}$ does not arise as an order condition, because the method has stage order 2. Expand the equations given in (544a), making use of (544b), and we find

$$
\begin{array} { r } { \beta ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { \beta ^ { \top } A ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { b ^ { \top } A c + \beta ^ { \top } A ^ { 2 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = \frac { 1 } { 6 } . } \end{array}
$$

Eliminating terms known to be zero, we see that (544g) simplifies to

$$
b _ { 2 } a _ { 2 1 } c _ { 1 } = \frac { 1 } { 6 ( 1 + \frac { 1 } { 2 } \beta _ { 3 } c _ { 1 } ) } .
$$

Consider the vector $v ^ { \mathsf { T } } = \beta _ { 3 } e _ { 3 } ^ { \mathsf { T } } - \beta ^ { \mathsf { T } } ( I + \beta _ { 3 } A )$ and note that $v ^ { \prime } x _ { 1 } = v ^ { \prime } x _ { 2 } =$ $c ^ { \mathsf { T } } x _ { 3 } = 0$ , where $x _ { 1 } = e _ { 3 }$ , $\begin{array} { r } { x _ { 2 } = \frac { 1 } { 2 } c ^ { 2 } - A c } \end{array}$ and $x _ { 3 } = A ( { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c ) .$ It is not possible that $x _ { 1 } , x _ { 2 } , x _ { 3 }$ are linearly dependent because this would imply $\beta _ { 1 } = \beta _ { 2 } = 0$ , which is inconsistent with $\beta ^ { 1 } { \bf 1 } = 0$ and $\beta ^ { \mathsf { I } } c = 1$ . Hence, $v ^ { \mapsto } = 0$ and we arrange this in the form

$$
\beta ^ { \intercal } = \beta _ { 3 } e _ { 3 } ^ { \intercal } ( I + \beta _ { 3 } A ) ^ { - 1 } = \beta _ { 3 } e _ { 3 } ^ { \intercal } - \beta _ { 3 } ^ { 2 } b ^ { \intercal } + \beta _ { 3 } ^ { 3 } b ^ { \intercal } A .
$$

Multiply (544i) by $c$ and use (544d), (544h) to obtain a relationship between $\beta _ { 3 }$ and $c _ { 1 }$ :

$$
c _ { 1 } = \frac { - 2 ( 1 - \beta _ { 3 } + \frac { 1 } { 2 } \beta _ { 3 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 3 } ^ { 3 } ) } { \beta _ { 3 } ( 1 - \beta _ { 3 } + \frac { 1 } { 2 } \beta _ { 3 } ^ { 2 } ) } .
$$

The ingredients for constructing an ARK method with $p = r = s = 3$ are now all available and they are put together as follows:

1. Choose the value of $\beta _ { 3 }$ .   
2. Evaluate $c _ { 1 }$ from (544j).   
3. Choose the value of $c _ { 2 }$ .   
4. Evaluate $b _ { 0 }$ , $b _ { 1 }$ , $b _ { 2 }$ to satisfy (544b).   
5. Evaluate $a _ { 2 1 }$ to satisfy (544h).   
6. Evaluate the remaining elements of $\beta ^ { \sf I }$ from (544i).   
7. Evaluate the elements of $U$ and $V$ .

together with the choice The following example method is found from $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ : $\beta _ { 3 } = 2$ , leading to $c _ { 1 } = \textstyle { \frac { 1 } { 3 } }$

$$
\begin{array} { r } { [ \begin{array} { c c c c c c } { 0 } & { 0 } & { 0 } & { | ~ 1 } & { \frac { 1 } { 3 } } & { \frac { 1 } { 1 8 } } \\ { \frac { 1 } { 2 } } & { 0 } & { 0 } & { | ~ 1 } & { \frac { 1 } { 6 } } & { \frac { 1 } { 1 8 } } \\ { 0 } & { \frac { 3 } { 4 } } & { 0 } & { 1 } & { \frac { 1 } { 4 } } & { 0 } \\ { 0 } & { \frac { 3 } { 4 } } & { 0 } & { 1 } & { \frac { 1 } { 4 } } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 3 } & { - 3 } & { 2 } \end{array} | ~ . } \end{array}
$$

Further examples of third order ARK methods, together with details on possible interpolation techniques, can be found in Rattenbury (2005).
