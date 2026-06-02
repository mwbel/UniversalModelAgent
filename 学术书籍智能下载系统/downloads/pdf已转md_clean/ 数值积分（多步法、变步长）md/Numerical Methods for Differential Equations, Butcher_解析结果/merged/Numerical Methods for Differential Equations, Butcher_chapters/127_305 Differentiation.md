# 305 Differentiation

We need to develop fairly intricate formulae involving derivatives of vectorvalued functions of vector arguments. Hence, in this subsection and the next, we review basic calculus ideas in a vector setting. We start with the elementary notions of the derivative of a real-valued function of a single real variable, and the partial derivatives of a real-valued function of several real variables. A real-valued function $f$ , whose domain contains an open interval around the real number $a$ , is differentiable at $a$ if there exists a number $f ^ { \prime } ( a )$ , referred to as the derivative of $f$ at $a$ , such that $| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta | / | \delta | \to 0$ a s $| \delta | \to 0$ . This definition is extended in two ways. First, $f$ can take values in $\mathbb { R } ^ { N }$ , in which case $f$ is differentiable if each of its components is differentiable. Furthermore, $f ^ { \prime } ( a ) \in \mathbb { R } ^ { N }$ is equal to the vector made up from the derivatives of the components of $f$ . Another way of writing this is

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { | \delta | } } \to 0 \quad { \mathrm { a s ~ } } | \delta | \to 0 .
$$

When the domain of $f$ is generalized to $X \subset \mathbb { R } ^ { M }$ , such that $a \in O \subset X$ , where $O$ is an open set, such as a product of open intervals, then $f ^ { \prime } ( a )$ , if it

exists, is a linear operator, $f ^ { \prime } ( a ) : \mathbb { R } ^ { M } \longrightarrow \mathbb { R } ^ { N }$ , such that

$$
{ \frac { \| f ( a + \delta ) - f ( a ) - f ^ { \prime } ( a ) \delta \| } { \| \delta \| } } \to 0 \quad { \mathrm { a s ~ } } \| \delta \| \to 0 .
$$

If the components of $a$ and $f$ are written as

$$
a = \left[ \begin{array} { c } { { a ^ { 1 } } } \\ { { a ^ { 2 } } } \\ { { \vdots } } \\ { { a ^ { M } } } \end{array} \right] , \qquad f = \left[ \begin{array} { c } { { f ^ { 1 } } } \\ { { f ^ { 2 } } } \\ { { \vdots } } \\ { { f ^ { N } } } \end{array} \right] ,
$$

then the linear operator $f ^ { \prime } ( a )$ is represented by the matrix of partial derivatives

$$
{ \bf \\xi } ^ { \prime } ( a ) = \left[ { \begin{array} { c c c c } { f _ { 1 } ^ { 1 } ( a ) } & { f _ { 2 } ^ { 1 } ( a ) } & { \cdots } & { f _ { M } ^ { 1 } ( a ) } \\ { f _ { 1 } ^ { 2 } ( a ) } & { f _ { 2 } ^ { 2 } ( a ) } & { \cdots } & { f _ { M } ^ { 2 } ( a ) } \\ { \vdots } & { \vdots } & & { \vdots } \\ { f _ { 1 } ^ { N } ( a ) } & { f _ { 2 } ^ { N } ( a ) } & { \cdots } & { f _ { M } ^ { N } ( a ) } \end{array} } \right] = \left[ { \begin{array} { c c c c } { { \frac { \partial f ^ { 1 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 1 } } { \partial a ^ { M } } } } \\ { { \frac { \partial f ^ { 2 } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { 2 } } { \partial a ^ { M } } } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { { \frac { \partial f ^ { N } } { \partial a ^ { 1 } } } } & { { \frac { \partial f ^ { N } } { \partial a ^ { 2 } } } } & { \cdots } & { { \frac { \partial f ^ { N } } { \partial a ^ { M } } } } \end{array} } \right] .
$$

Second and higher derivatives are bilinear and multilinear operators. In the tensor representation

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } ( a ) = { \frac { \partial ^ { k } f ^ { i } } { \partial a _ { j _ { 1 } } \partial a _ { j _ { 2 } } \cdot \cdot \cdot \partial a _ { j _ { k } } } } ,
$$

the argument ( $a$ ) is omitted, for convenience, if its value is understood.

Finally, inoperating wicollection of this subsech the order arguments $k$ $f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i }$ at eva, as a gives $k$ uation of the result of-linear operator, on thehe expression $k$ $v _ { 1 } , v _ { 2 } , \ldots , v _ { k } \in \mathbb { R } ^ { M }$

$$
\sum _ { j _ { 1 } = 1 } ^ { M } \sum _ { j _ { 2 } = 1 } ^ { M } \cdot \cdot \cdot \sum _ { j _ { k } = 1 } ^ { M } f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

The complicated appearance of (305a) can be alleviated by omitting all the summation symbols and regarding them as implied. This is the wellknown ‘summation convention’, and we use this notational simplification freely throughout this book. Thus we write, instead of (305a),

$$
f _ { j _ { 1 } j _ { 2 } \cdots j _ { k } } ^ { i } v _ { 1 } ^ { j _ { 1 } } v _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot v _ { k } ^ { j _ { k } } .
$$

Members of $\mathcal { I } _ { 2 }$ and their symmetries

$$
\sigma ( I ) | \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { I } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } &  { } \end{array}
$$
