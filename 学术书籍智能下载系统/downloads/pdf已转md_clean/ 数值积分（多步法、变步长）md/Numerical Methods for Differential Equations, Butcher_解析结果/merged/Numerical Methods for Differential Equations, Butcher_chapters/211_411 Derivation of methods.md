# 411 Derivation of methods

Given the relationship between the coefficients in the $\alpha$ and $\beta$ polynomials under the condition that they have a specified order, the choice of actual methods remains. The first approach we consider is when $\alpha$ is given and $\beta$ is then chosen to achieve the required order. In Subsection 412 we consider the derivation of backward difference methods, in which $\beta$ is first specified and $\alpha$ is then derived.

To find the coefficients in Adams–Moulton methods, use $\alpha ( z ) = 1 - z$ , so

that from Theorem 410D we find

$$
{ \begin{array} { r l } & { \beta ( 1 + z ) = { \cfrac { 1 } { 1 - { \frac { 1 } { 2 } } z + { \frac { 1 } { 3 } } z ^ { 2 } - { \frac { 1 } { 4 } } z ^ { 3 } + { \frac { 1 } { 5 } } z ^ { 4 } - { \frac { 1 } { 6 } } z ^ { 5 } + \cdots } } } \\ & { \qquad = 1 + { \frac { 1 } { 2 } } z - { \frac { 1 } { 1 2 } } z ^ { 2 } + { \frac { 1 } { 2 4 } } z ^ { 3 } - { \frac { 1 9 } { 7 2 0 } } z ^ { 4 } + { \frac { 3 } { 1 6 0 } } z ^ { 5 } } \\ & { \qquad - { \frac { 8 6 3 } { 6 0 4 8 0 } } z ^ { 6 } + { \frac { 2 7 5 } { 2 4 1 9 2 } } z ^ { 7 } - { \frac { 3 3 9 5 3 } { 3 6 2 8 8 0 0 } } z ^ { 8 } } \\ & { \qquad + { \frac { 8 1 8 3 } { 1 0 3 6 8 0 0 } } z ^ { 9 } - { \frac { 3 2 5 0 4 3 3 } { 4 7 9 0 0 1 6 0 0 } } z ^ { 1 0 } + \cdots . } \end{array} }
$$

It is clear that order $k + 1$ can be obtained using a $k$ -step method because the expansion can be truncated at the term in $z ^ { k }$ , leading to an $O ( z ^ { k + 1 } )$ error and degree $k$ polynomial $\beta ( 1 + z )$ . For example, for $k = 1$ we have

$$
\begin{array} { r } { \beta ( 1 + z ) = 1 + \frac { 1 } { 2 } z , } \end{array}
$$

implying that

$$
\begin{array} { r } { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) = \frac { 1 } { 2 } + \frac { 1 } { 2 } z , } \end{array}
$$

giving the coefficients $\beta _ { 0 } = \beta _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ . If $k = 2$ we have

$$
\beta ( 1 + z ) = 1 + \textstyle { \frac { 1 } { 2 } } z - \textstyle { \frac { 1 } { 1 2 } } z ^ { 2 }
$$

and

$$
\begin{array} { r } { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) - \frac { 1 } { 1 2 } ( z - 1 ) ^ { 2 } = \frac { 5 } { 1 2 } + \frac { 2 } { 3 } z + - \frac { 1 } { 1 2 } z ^ { 2 } , } \end{array}
$$

giving $\beta _ { 0 } = \frac { 5 } { 1 2 }$ , $\beta _ { 1 } = \textstyle { \frac { 2 } { 3 } }$ , $\beta _ { 2 } = - \frac { 1 } { 1 2 }$ . In general, we can find the coefficients by rewriting (411a) in the form

$$
\begin{array} { r l } & { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) - \frac { 1 } { 1 2 } ( z - 1 ) ^ { 2 } + \frac { 1 } { 2 4 } ( z - 1 ) ^ { 3 } - \frac { 1 9 } { 7 2 0 } ( z - 1 ) ^ { 4 } } \\ & { \qquad + \frac { 3 } { 1 6 0 } ( z - 1 ) ^ { 5 } - \frac { 8 6 3 } { 6 0 4 8 0 } ( z - 1 ) ^ { 6 } + \frac { 2 7 5 } { 2 4 1 9 2 } ( z - 1 ) ^ { 7 } - \frac { 3 3 9 5 3 } { 3 6 2 8 8 0 0 } ( z - 1 ) ^ { 8 } } \\ & { \qquad + \frac { 8 1 8 3 } { 1 0 3 6 8 0 0 } ( z - 1 ) ^ { 9 } - \frac { 3 2 5 0 4 3 3 } { 4 7 9 0 0 1 6 0 0 } ( z - 1 ) ^ { 1 0 } + \cdots , } \end{array}
$$

and truncating at the term in $( z - 1 ) ^ { k }$ to obtain the coefficients in the $k$ -step order $k + 1$ method.

For Adams–Bashforth methods, in which $\beta _ { 0 }$ necessarily vanishes, we write $\beta ( z ) = z { \widehat { \beta } } ( z )$ , where $\widehat { \beta }$ has degree $k - 1$ for a $k$ -step method. In this case Theorem 410D can be written in the form

$$
\frac { z } { ( 1 + z ) \log ( 1 + z ) } \frac { \alpha ( 1 + z ) } { z } + \widehat { \beta } ( 1 + z ) = O ( z ^ { p } ) ,
$$

and we aim for order $p = k$ . It is found that

$$
{ \begin{array} { r l } & { { \widehat { \beta } } ( 1 + z ) = { \frac { 1 } { ( 1 + z ) \left( 1 - { \frac { 1 } { 2 } } z + { \frac { 1 } { 3 } } z ^ { 2 } - { \frac { 1 } { 4 } } z ^ { 3 } + \cdots \right) } } } \\ & { \qquad = 1 - { \frac { 1 } { 2 } } z + { \frac { 5 } { 1 2 } } z ^ { 2 } - { \frac { 3 } { 8 } } z ^ { 3 } + { \frac { 2 5 1 } { 7 2 0 } } z ^ { 4 } - { \frac { 9 5 } { 2 8 8 } } z ^ { 5 } } \\ & { \qquad + { \frac { 1 9 0 8 7 } { 6 0 4 8 0 } } z ^ { 6 } - { \frac { 5 2 5 7 } { 1 7 2 8 0 } } z ^ { 7 } + { \frac { 1 0 7 0 0 1 7 } { 3 6 2 8 8 0 0 } } z ^ { 8 } } \\ & { \qquad - { \frac { 2 5 7 1 3 } { 8 9 6 0 0 } } z ^ { 9 } + { \frac { 2 6 8 4 2 2 5 3 } { 9 5 8 0 0 3 2 0 } } z ^ { 1 0 } - \cdots , } \end{array} }
$$

so that the coefficients $\beta _ { 1 }$ , $\beta _ { 2 } , \ldots , \beta _ { k }$ can be found by selecting the coefficients of $z ^ { 0 }$ , $z ^ { 1 }$ , . . . , $z ^ { k - 1 }$ in the truncation to the term in $( z - 1 ) ^ { k - 1 }$ in the expansion

$$
\begin{array} { r } { \ddot { \beta } ( z ) = 1 - \frac { 1 } { 2 } ( z - 1 ) + \frac { 5 } { 1 2 } ( z - 1 ) ^ { 2 } - \frac { 3 } { 8 } ( z - 1 ) ^ { 3 } + \frac { 2 5 1 } { 7 2 0 } ( z - 1 ) ^ { 4 } } \end{array}
$$

$$
\begin{array} { r } { - \frac { 9 5 } { 2 8 8 } ( z - 1 ) ^ { 5 } + \frac { 1 9 0 8 7 } { 6 0 4 8 0 } ( z - 1 ) ^ { 6 } - \frac { 5 2 5 7 } { 1 7 2 8 0 } ( z - 1 ) ^ { 7 } + \frac { 1 0 7 0 0 1 7 } { 3 6 2 8 8 0 0 } ( z - 1 ) ^ { 8 } } \end{array}
$$

$$
- { \frac { 2 5 7 1 3 } { 8 9 6 0 0 } } ( z - 1 ) ^ { 9 } + { \frac { 2 6 8 4 2 2 5 3 } { 9 5 8 0 0 3 2 0 } } ( z - 1 ) ^ { 1 0 } - \cdot \cdot \cdot .
$$

For example, when $k = 2$ we have $\begin{array} { r } { { \widehat { \beta } } ( z ) = 1 - \frac { 1 } { 2 } ( z - 1 ) = \frac { 3 } { 2 } - \frac { 1 } { 2 } z } \end{array}$ leading to $\beta _ { 1 } = \begin{array} { l } { \frac { 3 } { 2 } } \end{array}$ and $\beta _ { 2 } = - \frac { 1 } { 2 }$ for the Adams–Bashforth method with order $p = 2$ . When $k = 3$ we have $\textstyle \beta ( z ) = 1 - { \frac { 1 } { 2 } } ( z - 1 ) + { \frac { 5 } { 1 2 } } ( z - 1 ) ^ { 2 } = { \frac { 2 3 } { 1 2 } } - { \frac { 4 } { 3 } } z + { \frac { 5 } { 1 2 } } z ^ { 2 }$ so that, for the Adams–Bashforth method with order $p = 3$ , we have $\beta _ { 1 } = \textstyle { \frac { 2 3 } { 1 2 } }$ , $\beta _ { 2 } = - \frac { 4 } { 3 }$ , $\beta _ { 3 } = \textstyle { \frac { 5 } { 1 2 } }$ .

Values of the Adams–Bashforth and Adams–Moulton coefficients have previously been given in Tables 244(I) and 244(II), respectively.
