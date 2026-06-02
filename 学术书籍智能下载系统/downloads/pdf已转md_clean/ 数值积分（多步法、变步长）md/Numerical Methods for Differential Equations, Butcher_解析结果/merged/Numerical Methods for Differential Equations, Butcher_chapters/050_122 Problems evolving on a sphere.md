# 122 Problems evolving on a sphere

Given a function $H ( y )$ , we will explore situations in which solutions to $y ^ { \prime } ( x ) \ = \ f ( y )$ preserve the value of $H ( y ( x ) )$ . In the special case in which $H ( y ) ~ = ~ \textstyle { \frac { 1 } { 2 } } \| y \| ^ { 2 }$ , this will correspond to motion on a sphere. We recall the standard notation

$$
\begin{array} { r } { \nabla ( H ) = \left[ \begin{array} { c } { \frac { \partial H } { \partial y _ { 1 } } } \\ { \frac { \partial H } { \partial y _ { 2 } } } \\ { \vdots } \\ { \frac { \partial H } { \partial y _ { N } } } \end{array} \right] } \end{array}
$$

and consider problems of the ‘Poisson’ form

$$
y ^ { \prime } = L ( x , y ) \nabla ( y ) ,
$$

where $L ( x , y )$ is always a skew-symmetric matrix. For such problems $H ( y ( x ) )$ is invariant. To verify this, calculate

$$
{ \frac { d } { d x } } H ( y ( x ) ) = \sum _ { i = 1 } ^ { N } { \frac { \partial H } { \partial y _ { i } } } y _ { i } ^ { \prime } ( x ) = \nabla ( H ) ^ { \top } L ( x , y ) \nabla ( y ) = 0 ,
$$

because of the skew-symmetry of $L$ .

The Euler equations, discussed in Subsection 107, provide two examples of this. To show that $E ( w )$ is invariant write $\begin{array} { r } { H ( w ) = \frac { 1 } { 2 } E ( w ) } \end{array}$ , and to show that $F ( w )$ is invariant write $\begin{array} { r } { H ( w ) = \frac { 1 } { 2 } F ( w ) } \end{array}$ . The problem reverts to the form of (122a), with $y$ replaced by $w$ , where $L ( x , w )$ is given by

$$
\left[ \begin{array} { c c c } { { 0 } } & { { \frac { I _ { 3 } w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { - \frac { I _ { 2 } w _ { 2 } } { I _ { 1 } I _ { 3 } } } } \\ { { - \frac { I _ { 3 } w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { 0 } } & { { \frac { I _ { 1 } w _ { 1 } } { I _ { 2 } I _ { 3 } } } } \\ { { \frac { I _ { 2 } w _ { 2 } } { I _ { 1 } I _ { 3 } } } } & { { - \frac { I _ { 1 } w _ { 1 } } { I _ { 2 } I _ { 3 } } } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { c c c } { { 0 } } & { { - \frac { w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { \frac { w _ { 2 } } { I _ { 1 } I _ { 3 } } } } \\ { { \frac { w _ { 3 } } { I _ { 1 } I _ { 2 } } } } & { { 0 } } & { { - \frac { w _ { 1 } } { I _ { 2 } I _ { 3 } } } } \\ { { - \frac { w _ { 2 } } { I _ { 1 } I _ { 3 } } } } & { { \frac { w _ { 1 } } { I _ { 2 } I _ { 3 } } } } & { { 0 } } \end{array} \right] ,
$$

respectively.

We now revert to the special case $\begin{array} { r } { H ( x ) = \frac { 1 } { 2 } y ^ { \intercal } y } \end{array}$ , for which (122a) becomes

$$
y ^ { \prime } = L ( x , y ) y .
$$

An example is the contrived problem

$$
{ \left[ \begin{array} { l } { y _ { 1 } ^ { \prime } } \\ { y _ { 2 } ^ { \prime } } \\ { y _ { 3 } ^ { \prime } } \end{array} \right] } = { \left[ \begin{array} { l l l } { ~ 0 } & { - y _ { 1 } } & { - \sin ( x ) } \\ { ~ y _ { 1 } } & { ~ 0 } & { ~ - 1 } \\ { \sin ( x ) } & { 1 } & { ~ 0 } \end{array} \right] } ~ { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right] } , ~ { \left[ \begin{array} { l } { y _ { 1 } ( 0 ) } \\ { y _ { 2 } ( 0 ) } \\ { y _ { 3 } ( 0 ) } \end{array} \right] } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } ,
$$

with solution $y _ { 1 } ( x ) = \cos ( x )$ , $y _ { 2 } ( x ) = \cos ( x ) \sin ( x )$ , $y _ { 3 } ( x ) = \sin ^ { 2 } ( x )$ . The solution values for $x \in [ 0 , 1 . 4 \pi ]$ are shown in Figure $1 2 2 ( \mathrm { i } )$ .

Problems of the form (122b) are a special case of

$$
Y ^ { \prime } = L ( x , Y ) Y ,
$$

where $Y$ has a number of columns. In this case the inner product of two specific columns will be invariant. In particular, if $Y ( x )$ is a square matrix,

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/58c07b19b162bdabedb36b15be96c20ca928769870cb6435e0e5d7c7784ef5a8.jpg)  
Solution to problem (122c) with $_ { y 3 }$ pointing out of the page

initially orthogonal, and $L ( x , Y )$ is always skew-symmetric, then $Y ( x )$ will remain orthogonal. Denote the elements of $Y$ by $y _ { i j }$ . An example problem of this type is

$$
Y ^ { \prime } ( x ) = \left[ \begin{array} { c c c c } { { 0 } } & { { - 1 } } & { { \mu y _ { 2 1 } } } \\ { { 1 } } & { { 0 } } & { { - \mu y _ { 1 1 } } } \\ { { - \mu y _ { 2 1 } } } & { { \mu y _ { 1 1 } } } & { { 0 } } \end{array} \right] Y , \qquad Y ( 0 ) = I ,
$$

with $\mu$ a real parameter. The solution to (122e) is

$$
Y ( x ) = \left[ \begin{array} { c c c c } { \cos ( x ) } & { - \sin ( x ) \cos ( \mu x ) } & { } & { \sin ( x ) \sin ( \mu x ) } \\ { \sin ( x ) } & { \cos ( x ) \cos ( \mu x ) } & { - \cos ( x ) \sin ( \mu x ) } \\ { 0 } & { \sin ( \mu x ) } & { } & { \cos ( \mu x ) } \end{array} \right] .
$$
