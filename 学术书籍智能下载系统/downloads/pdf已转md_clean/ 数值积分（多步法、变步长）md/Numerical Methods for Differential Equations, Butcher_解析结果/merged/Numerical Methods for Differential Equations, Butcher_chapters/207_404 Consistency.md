# 404 Consistency

Just as the initial value problem $y ^ { \prime } ( x ) = 0$ , with initial condition $y ( x _ { 0 } ) = 0$ , motivated the concept of stability, so the same problem, with initial value $y ( x _ { 0 } ) = 1$ , can be used to introduce preconsistency. We want to ensure that this problem can be solved exactly, starting from the exact initial value. Suppose the numerical solution is known to have the correct value at $x =$ $x _ { n - k } , x _ { n - k + 1 } , . . . , x _ { n - 1 }$ so that $y _ { i } = y ( x _ { i } ) = 1$ , for $i = n { - } k , n { - } k { + } 1 , \ldots , n { - } 1$ . Under these assumptions, the result computed at step $n$ will be

$$
y _ { n } = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } ,
$$

and this will equal the correct value $y _ { n } = 1$ if and only if

$$
1 = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } .
$$

Definition 404A A linear multistep method satisfying (404a) is said to be ‘preconsistent’.

Now consider the differential equation

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( x _ { 0 } ) = 0 ,
$$

with exact solution at the step values

$$
y _ { i } = h i .
$$

If this solution has been found for $i = n - k , n - k + 1 , \ldots , n - 1$ , then it is also correct for $i = n$ if and only if

$$
\iota h = \alpha _ { 1 } ( n - 1 ) h + \alpha _ { 2 } ( n - 2 ) h + \cdot \cdot \cdot + \alpha _ { k } ( n - k ) h + h \big ( \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } \big ) .
$$

Assuming the method is preconsistent, the factor $h$ can be cancelled and then $n$ times (404a) can be subtracted. We then find

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } = \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } .
$$

This leads to the following definition:

Definition 404B A linear multistep method satisfying (404a) and (404b) is said to be ‘consistent’.

Another way of looking at the consistency conditions is to suppose that $y _ { i } =$ $y ( x _ { i } ) { + } O ( h ^ { 2 } )$ and that $f ( x _ { i } , y _ { i } ) = y ^ { \prime } ( x _ { i } ) \ – O ( h )$ , for $i = n { - } k , n { - } k { + } 1 , \ldots , n { - } 1$ , and to consider the computation of $y _ { n }$ using the equation

$$
{ \begin{array} { r l } & { y _ { n } - h \beta _ { 0 } f ( x _ { n } , y _ { n } ) } \\ & { \qquad = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ & { \qquad + h ( \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) } \\ & { \qquad = \alpha _ { 1 } y ( x _ { n - 1 } ) + \alpha _ { 2 } y ( x _ { n - 2 } ) + \cdot \cdot \cdot + \alpha _ { k } y ( x _ { n - k } ) } \\ & { \qquad + h ( \beta _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + \beta _ { 2 } y ^ { \prime } ( x _ { n - 2 } ) + \cdot \cdot \cdot + \beta _ { k } y ^ { \prime } ( x _ { n - k } ) ) . } \end{array} }
$$

Expand the right-hand side by Taylor’s theorem about $x _ { n }$ , and we find

$$
\begin{array} { r l r } {  { \big ( \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } \big ) y ( x _ { n } ) } } \\ & { } & { \qquad + \big ( \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } - \alpha _ { 1 } - 2 \alpha _ { 2 } - \cdot \cdot \cdot - k \alpha _ { k } \big ) h y ^ { \prime } ( x _ { n } ) + O ( h ^ { 2 } ) . } \end{array}
$$

This will give the correct answer of

$$
y ( x _ { n } ) - h \beta _ { 0 } y ^ { \prime } ( x _ { n } ) ,
$$

to within $O ( h ^ { 2 } )$ , if and only if

$$
\alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } = 1
$$

and

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } = \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } .
$$

Hence, we can view the two requirements of consistency as criteria that the computed solution is capable of maintaining accuracy to within $O ( h ^ { 2 } )$ over one step, and therefore over several steps.
