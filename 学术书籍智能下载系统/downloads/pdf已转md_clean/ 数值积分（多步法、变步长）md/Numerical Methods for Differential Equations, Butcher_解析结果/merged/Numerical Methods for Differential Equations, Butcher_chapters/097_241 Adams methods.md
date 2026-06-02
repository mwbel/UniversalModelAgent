# 241 Adams methods

The most important linear multistep methods for non-stiff problems are of Adams type. That is, the solution approximation at $x _ { n }$ is defined either as

$$
\begin{array} { r } { y _ { n } = y _ { n - 1 } + h ( \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) \qquad } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) , } \end{array}
$$

or as

$$
\begin{array} { c } { y _ { n } = y _ { n - 1 } + h ( \beta _ { 0 } f ( x _ { n } , y _ { n } ) + \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) , } \end{array}
$$

where, in each case, the constants ( $\beta _ { 0 }$ ), $\beta _ { 1 }$ , $\beta _ { 2 }$ , . . . , $\beta _ { k }$ are chosen to give the highest possible order.

The meaning of order, and how it is achieved in particular cases, is straightforward in the case of methods of the form (241a), which are known as ‘Adams–Bashforth’ methods. Assuming that no errors have yet been introduced when the approximation at $x _ { n }$ is about to be calculated, we can replace the terms on the right-hand side by the quantities they are supposed to approximate, that is, by $y ( x _ { n - 1 } )$ , $y ^ { \prime } ( x _ { n - 1 } )$ , $y ^ { \prime } ( x _ { n - 2 } )$ , . . . , $y ^ { \prime } ( x _ { n - k } )$ , respectively. The amount by which the approximation, written in this form, differs from $y ( x _ { n } )$ is the error generated in this particular step. If this error can be estimated for a smooth problem as $O ( h ^ { p + 1 } )$ , then the method is regarded as having order $p$ .

For the methods given by (241b), which are known as ‘Adams–Moulton’ methods, the term involving $f ( x _ { n } , y _ { n } )$ is a complication in this understanding of order. However, the conclusion turns out to be exactly the same as for Adams–Bashforth methods: if every term in (241b) is replaced by the quantity it is supposed to be approximating and the two sides of this equation differ by an amount that can be estimated as $O ( h ^ { p + 1 } )$ , then the method has order $p$ .

To obtain a simple criterion for a given order, we can write all terms in

$$
\begin{array} { r l r } {  { y ( x _ { n } ) - y ( x _ { n - 1 } ) - h \big ( \beta _ { 0 } y ^ { \prime } ( x _ { n } ) + \beta _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + \beta _ { 2 } y ^ { \prime } ( x _ { n - 2 } ) } } \\ & { } & { \qquad + \cdot \cdot + \beta _ { k } y ^ { \prime } ( x _ { n - k } ) \big ) } \end{array}
$$

as Taylor series about, for example, $x _ { n }$ . This gives an expression of the form

$$
C _ { 1 } h y ^ { \prime } ( x _ { n } ) + C _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot + C _ { p } h ^ { p } y ^ { ( p ) } ( x _ { n } ) + O ( h ^ { p + 1 } ) ,
$$

and the conditions for order $p$ will be that $C _ { 1 } = C _ { 2 } = \cdot \cdot \cdot = C _ { p } = 0$ .

It can be shown that an equivalent criterion is that (241c) vanishes whenever $y$ is a polynomial of degree not exceeding $p$ .

We will use these criteria to derive Adams–Bashforth methods with $p = k$ for $k = 2 , 3 , 4$ , and Adams–Moulton methods with $p = k + 1$ for $k = 1 , 2 , 3$ .

For $k = 4$ , the Taylor expansion of (241c) takes the form

$$
\begin{array} { r l } & { h y ^ { \prime } ( x _ { n } ) ( 1 - \beta _ { 0 } - \beta _ { 1 } - \beta _ { 2 } - \beta _ { 3 } - \beta _ { 4 } ) } \\ & { \qquad + h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) \big ( - \frac 1 2 + \beta _ { 1 } + 2 \beta _ { 2 } + 3 \beta _ { 3 } + 4 \beta _ { 4 } \big ) } \\ & { \qquad + h ^ { 3 } y ^ { ( 3 ) } ( x _ { n } ) \big ( \frac 1 6 - \frac 1 2 ( \beta _ { 1 } + 4 \beta _ { 2 } + 9 \beta _ { 3 } + 1 6 \beta _ { 4 } ) \big ) } \\ & { \qquad + h ^ { 4 } y ^ { ( 4 ) } ( x _ { n } ) \big ( - \frac 1 { 2 4 } + \frac 1 6 ( \beta _ { 1 } + 8 \beta _ { 2 } + 2 7 \beta _ { 3 } + 6 4 \beta _ { 4 } ) \big ) + O ( h ^ { 5 } ) , } \end{array}
$$

so that

$$
\begin{array} { r l } & { C _ { 1 } = 1 - \beta _ { 0 } - \beta _ { 1 } - \beta _ { 2 } - \beta _ { 3 } - \beta _ { 4 } , } \\ & { C _ { 2 } = - \frac { 1 } { 2 } + \beta _ { 1 } + 2 \beta _ { 2 } + 3 \beta _ { 3 } + 4 \beta _ { 4 } , } \\ & { C _ { 3 } = \frac { 1 } { 6 } - \frac { 1 } { 2 } ( \beta _ { 1 } + 4 \beta _ { 2 } + 9 \beta _ { 3 } + 1 6 \beta _ { 4 } ) , } \\ & { C _ { 4 } = - \frac { 1 } { 2 4 } + \frac { 1 } { 6 } ( \beta _ { 1 } + 8 \beta _ { 2 } + 2 7 \beta _ { 3 } + 6 4 \beta _ { 4 } ) . } \end{array}
$$

For the Adams–Bashforth methods the value of $\beta _ { 0 }$ is zero; for $k = 2$ we also have $\beta _ { 3 } = \beta _ { 4 } = 0$ and we must solve the equations $C _ { 1 } = C _ { 2 } = 0$ . This gives $\beta _ { 1 } = \textstyle { \frac { 3 } { 2 } }$ and $\beta _ { 2 } = - \frac { 1 } { 2 }$ . For $k = 3$ we allow $\beta _ { 3 }$ to be non-zero and we require that $C _ { 1 } = C _ { 2 } = C _ { 3 } = 0$ $\beta _ { 3 } = \textstyle { \frac { 5 } { 1 2 } }$ $k = 4$ . The solutions of these equations is $C _ { 1 } = C _ { 2 } = C _ { 3 } = C _ { 4 } = 0$ $\beta _ { 1 } = \textstyle { \frac { 2 3 } { 1 2 } }$ , $\beta _ { 2 } = - \textstyle { \frac { 4 } { 3 } }$ $\beta _ { 1 } = \textstyle { \frac { 5 5 } { 2 4 } }$ 3 5 , $\beta _ { 2 } = - \frac { 5 9 } { 2 4 }$ $\textstyle \beta _ { 3 } = { \frac { 3 7 } { 2 4 } }$ $\beta _ { 4 } = - \textstyle { \frac { 3 } { 8 } }$

the Adam) we have milar man $\beta _ { 0 }$ $k = 1$ $p = 2$ $\beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } = 0$ $C _ { 1 } = C _ { 2 } = 0$ $\begin{array} { r } { \beta _ { 0 } = \beta _ { 1 } = \frac { 1 } { 2 } } \end{array}$ and for $k = 3$ ( $p = 4$ ) that $\begin{array} { r } { \beta _ { 0 } = \frac { 3 } { 8 } } \end{array}$ $k = 2$ , $\beta _ { 1 } = \textstyle { \frac { 1 9 } { 2 4 } }$ $p = 3$ ） $\beta _ { 2 } = - \frac { 5 } { 2 4 }$ $\beta _ { 0 } = \textstyle { \frac { 5 } { 1 2 } }$ , $\beta _ { 3 } = \textstyle { \frac { 1 } { 2 4 } }$ $\beta _ { 1 } = \textstyle { \frac { 2 } { 3 } }$ . $\beta _ { 2 } = - \frac { 1 } { 1 2 }$
