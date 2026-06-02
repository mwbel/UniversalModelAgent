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
