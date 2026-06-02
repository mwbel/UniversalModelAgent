# 322 Methods of order 4

It is an interesting consequence of the fourth order conditions for a method with $s \ = \ 4$ stages, that $c _ { 4 } ~ = ~ 1$ and that $D ( 1 )$ holds. This fact reduces significantly the number of conditions that remain to be solved; furthermore, it is possible to segment the derivation into two phases: the solution of the remaining order conditions and the evaluation of the elements in the final row of $A$ to ensure that $D ( 1 )$ is actually satisfied. Assuming that the method

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { c _ { 4 } } \\ { b _ { 1 } } \end{array} \right| a _ { 2 1 } \qquad \eqno { 3 } 2 } \end{array}
$$

satisfies the fourth order conditions, then we can compute the values of

$$
\begin{array} { r l } & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) ( c _ { i } - c _ { 2 } ) c _ { i } = \frac { 1 } { 4 } - \frac { c _ { 2 } + c _ { 4 } } { 3 } + \frac { c _ { 2 } c _ { 4 } } { 2 } , } \\ & { b _ { 4 } a _ { 4 3 } ( c _ { 3 } - c _ { 2 } ) c _ { 3 } = \displaystyle \sum b _ { i } a _ { i j } ( c _ { j } - c _ { 2 } ) c _ { j } \qquad = \frac { 1 } { 1 2 } - \frac { c _ { 2 } } { 6 } , } \\ & { b _ { 3 } ( c _ { 3 } - c _ { 4 } ) a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } ( c _ { i } - c _ { 4 } ) a _ { i j } c _ { j } \qquad = \frac { 1 } { 8 } - \frac { c _ { 4 } } { 6 } , } \\ & { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \displaystyle \sum b _ { i } a _ { i j } a _ { j k } c _ { k } \qquad = \frac { 1 } { 2 4 } . } \end{array}
$$

In each of these calculations, the first column is the only non-zero term in the middle column, while the final column is found by expanding the middle column into a linear combination of elementary weights and equating each of these to the right-hand sides of the corresponding order conditions. For example, (322a) is evaluated from the trees $\blacktriangledown$ , $\blacktriangledown$ and $\natural$ and uses the combination of order conditions

$$
\Phi ( { \pmb { \Psi } } ) - ( c _ { 2 } + c _ { 4 } ) \Phi ( { \pmb { \Psi } } ) + c _ { 2 } c _ { 4 } \Phi ( { \pmb { \updownarrow } } ) = \frac { 1 } { \gamma ( { \pmb { \Psi } } ) } - \frac { c _ { 2 } + c _ { 4 } } { \gamma ( { \pmb { \ Y } } ) } + \frac { c _ { 2 } c _ { 4 } } { \gamma ( { \pmb { \updownarrow } } ) } .
$$

From the first columns of (322a)–(322d), we observe that $\mathrm { { ( 3 2 2 a ) } } \times \mathrm { { ( 3 2 2 d ) } } =$ (322b) $\times$ (322c) so that, from the last columns, we find

$$
\left( { \frac { 1 } { 4 } } - { \frac { c _ { 2 } + c _ { 4 } } { 3 } } + { \frac { c _ { 2 } c _ { 4 } } { 2 } } \right) \left( { \frac { 1 } { 2 4 } } \right) - \left( { \frac { 1 } { 1 2 } } - { \frac { c _ { 2 } } { 6 } } \right) \left( { \frac { 1 } { 8 } } - { \frac { c _ { 4 } } { 6 } } \right) = 0 .
$$

This relation simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$ which, because $c _ { 2 } = 0$ is incompatible with (322d), implies $c _ { 4 } = 1$ .

An alternative proof of this result, is found by using the following:

Lemma 322A If $P$ and $Q$ are each $3 \times 3$ matrices such that their product has the form

$$
P Q = \left[ \begin{array} { c c c } { r _ { 1 1 } } & { r _ { 1 2 } } & { 0 } \\ { r _ { 2 1 } } & { r _ { 2 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

where

$$
\operatorname* { d e t } \left( { \left[ \begin{array} { l l } { r _ { 1 1 } } & { r _ { 1 2 } } \\ { r _ { 2 1 } } & { r _ { 2 2 } } \end{array} \right] } \right) \neq 0 ,
$$

then either the last row of $P$ is zero or the last column of $Q$ is zero.

Proof. Because $P Q$ is singular, either $P$ is singular or $Q$ is singular. In the first case, let $u ^ { \prime } \ne 0$ be such that $u ^ { \prime } P = 0$ , and therefore $u ^ { \intercal } P Q = 0$ ; in the second case, let $v \neq 0$ be such that $Q v = 0$ , and therefore $P Q v = 0$ . Because of the form of $P Q$ , this implies that the first two components of $u ^ { \intercal }$ (or, respectively, the first two components of $v$ ) are zero. $\boxed { \begin{array} { r l } \end{array} }$

To obtain the result that $D ( 1 )$ necessarily holds if $s = p = 4$ , we apply Lemma 322A with

$$
\begin{array}{c} \mathbf { \Phi } ^ { \mathcal { P } } = \left[ \begin{array} { c c c } { b _ { 2 } } & { b _ { 3 } } & { b _ { 4 } } \\ { b _ { 2 } c _ { 2 } } & { b _ { 3 } c _ { 3 } } & { b _ { 4 } c _ { 4 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { i = 1 } & { i } & { i = 1 } \end{array} \right] \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 3 } - b _ { 3 } ( 1 - c _ { 3 } ) \quad \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } )  \end{array}
$$

and

$$
\begin{array} { r } { Q = \left[ \begin{array} { c c c c c } { c _ { 2 } } & { c _ { 2 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } } \\ { c _ { 3 } } & { c _ { 3 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 3 j } c _ { j } - \frac { 1 } { 2 } c _ { 3 } ^ { 2 } } \\ { c _ { 4 } } & { c _ { 4 } ^ { 2 } } & { \sum _ { j = 1 } ^ { 4 } a _ { 4 j } c _ { j } - \frac { 1 } { 2 } c _ { 4 } ^ { 2 } } \end{array} \right] . } \end{array}
$$

The value of the matrix $P Q$ can be calculated from the order conditions. For example, the $( 2 , 2 )$ element is equal to

$$
\left[ b _ { 2 } c _ { 2 } b _ { 3 } c _ { 3 } b _ { 4 } c _ { 4 } \right] \left[ c _ { 2 } ^ { 2 } c _ { 3 } ^ { 2 } c _ { 4 } ^ { 2 } \right] ^ { \intercal } = \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 3 } = { \frac { 1 } { 4 } } .
$$

The elements in the last row and last column are a little more complicated to evaluate because they depend on linear combinations of elementary weights, but the relation of these elements in the product to the $C ( 2 )$ and $D ( 1 )$ conditions simplifies each of these elements to a zero value. In summary, the product of $P$ and $Q$ is

$$
P Q = \left[ \begin{array} { l l l } { \frac 1 2 } & { \frac 1 3 } & { 0 } \\ { \frac 1 3 } & { \frac 1 4 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] ,
$$

so that the conditions of Lemma 322A are satisfied. The conclusion is that the last roeither $P$ of  or $Q$ r, this means that. These simplify to $\begin{array} { r } { \sum _ { i = 1 } ^ { 4 } b _ { i } a _ { i 4 } - b _ { 4 } ( 1 - c _ { 4 } ) = 0 } \end{array}$ $\begin{array} { r } { \sum _ { j = 1 } ^ { 4 } a _ { 2 j } c _ { j } - \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ $b _ { 4 } ( 1 - c _ { 4 } ) = 0$ or to $\begin{array} { r } { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = 0 } \end{array}$ , respectively. It is impossible that $c _ { 2 } = 0$ or that $b _ { 4 } = 1$ , and hence $c _ { 4 } = 1$ and the $D ( 1 )$ condition holds.

Since $D ( 1 )$ holds, the set of additional equations we need to satisfy reduce to those associated with the trees , , $\curlyvee$ and $\blacktriangledown$ as well as with the $\operatorname { t r e e } \sqrt { \frac { \pi } { 2 } }$ . The order condition associated with the last of these is $\begin{array} { r } { \sum b _ { i } c _ { i } a _ { i j } c _ { j } = \frac { 1 } { 8 } } \end{array}$ . It turns out to be more convenient to use, instead of this condition, the difference between this and with the condition associated with $\nmid$ , that is, $\begin{array} { r } { \sum b _ { i } a _ { i j } c _ { j } = \frac { 1 } { 6 } } \end{array}$ , which is a consequence of other assumptions and of the $D ( 1 )$ condition. Hence we assume $\begin{array} { r } { \sum b _ { i } ( 1 - c _ { i } ) a _ { i j } c _ { j } = \frac { 1 } { 2 4 } } \end{array}$ .

The steps we need to carry out to derive one of these methods are as follows:

(a) Choose $c _ { 2 }$ and $c _ { 3 }$ , noting that $c _ { 1 } = 0$ and $c _ { 4 } = 1$ . (b) Choose $b _ { 1 }$ , $b _ { 2 }$ , $b _ { 3 }$ , $b _ { 4 }$ to satisfy $\sum b _ { i } c _ { i } ^ { k - 1 } = 1 / k$ for $k = 1 , 2 , 3 , 4$ . (c) Choose $a _ { 3 2 }$ so that $\begin{array} { r } { b _ { 3 } ( 1 - c _ { 3 } ) a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } } \end{array}$ . (d) Choose $a _ { 4 1 }$ , $a _ { 4 2 }$ , $a _ { 4 3 }$ , so that $\begin{array} { r } { \sum _ { i } b _ { i } a _ { i j } = b _ { j } \bigl ( 1 - c _ { j } \bigr ) } \end{array}$ for $j = 1 , 2 , 3$

Carrying out this programme might present some difficulties. For example, if in step (a) the $c _ { i }$ are not distinct, then there might not exist a solution in step (b). It might also happen that the value of $b _ { 4 }$ , found in step (b), is zero, and this will make it impossible to carry out either step (c) or step (d). Even if a solution exists for the sub-problem that arises in each step, the solution might not be unique, and there could turn out to be a family of solutions. The general solution, which is valid except in these exceptional cases, is given by the following coefficients:

$$
\begin{array} { r l } & { a _ { 2 1 } = c _ { 2 1 } , } \\ & { a _ { 3 1 } = \frac { c _ { 3 } \left( c _ { 3 } + 4 c _ { 2 } ^ { 2 } - 3 c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 3 2 } = - \frac { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) } { 2 c _ { 2 } \left( 2 c _ { 2 } - 1 \right) } , } \\ & { a _ { 4 1 } = \frac { - 1 2 c _ { 3 } c _ { 2 } ^ { 2 } + 1 2 c _ { 3 } ^ { 2 } c _ { 2 } ^ { 2 } + 4 c _ { 2 } ^ { 2 } - 6 c _ { 2 } + 1 5 c _ { 2 } c _ { 3 } - 1 2 c _ { 3 } ^ { 2 } c _ { 2 } + 2 + 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } } { 2 c _ { 2 } c _ { 3 } \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 2 } = \frac { \left( c _ { 2 } - 1 \right) \left( 4 c _ { 3 } ^ { 2 } - 5 c _ { 3 } + 2 - c _ { 2 } \right) } { 2 c _ { 2 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \\ & { a _ { 4 3 } = - \frac { \left( 2 c _ { 2 } - 1 \right) \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - 1 \right) \left( c _ { 3 } - 1 \right) } { c _ { 3 } \left( c _ { 3 } - c _ { 2 } \right) \left( - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } \right) } , } \end{array}
$$

$$
\begin{array} { l } { b _ { 1 } = \cfrac { 6 c _ { 3 } c _ { 2 } - 2 c _ { 3 } - 2 c _ { 2 } + 1 } { 1 2 c _ { 3 } c _ { 2 } } , } \\ { b _ { 2 } = - \cfrac { \left( 2 c _ { 3 } - 1 \right) } { 1 2 c _ { 2 } \left( c _ { 2 } - 1 \right) \left( c _ { 3 } - c _ { 2 } \right) } , } \\ { b _ { 3 } = \cfrac { \left( 2 c _ { 2 } - 1 \right) } { 1 2 c _ { 3 } \left( c _ { 2 } - c _ { 3 } c _ { 2 } + c _ { 3 } ^ { 2 } - c _ { 3 } \right) } , } \\ { b _ { 4 } = \cfrac { - 4 c _ { 3 } + 6 c _ { 3 } c _ { 2 } + 3 - 4 c _ { 2 } } { 1 2 \left( c _ { 3 } - 1 \right) \left( c _ { 2 } - 1 \right) } . } \end{array}
$$

Kutta identified five special cases where a solution is certain to exist:

$$
\begin{array} { l l l } { { \mathrm { ~ I ~ } } } & { { c _ { 2 } \notin \{ 0 , \frac { 1 } { 2 } , \frac { 1 } { 2 } \pm \frac { \sqrt { 3 } } { 6 } , 1 \} , } } & { { c _ { 3 } = 1 - c _ { 2 } , } } \\ { { \mathrm { ~ I I ~ } } } & { { b _ { 2 } = 0 , } } & { { c _ { 2 } \neq 0 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ I I I ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = \frac { 1 } { 2 } , \quad c _ { 3 } = 0 , } } \\ { { \mathrm { ~ I V ~ } } } & { { b _ { 4 } \neq 0 , } } & { { c _ { 2 } = 1 , \quad c _ { 3 } = \frac { 1 } { 2 } , } } \\ { { \mathrm { ~ V ~ } } } & { { b _ { 3 } \neq 0 , } } & { { c _ { 2 } = c _ { 3 } = \frac { 1 } { 2 } . } } \end{array}
$$

The coefficient tableaux are for case I,

<table><tr><td>0</td><td colspan="3"></td></tr><tr><td>1-C3</td><td colspan="3">1-C3</td></tr><tr><td>C3</td><td>C3(1-2c3)</td><td>C3 2(1-c3）</td><td></td></tr><tr><td rowspan="2">1</td><td colspan="3">2(1-c3）</td></tr><tr><td>12c-24c+17c3-4</td><td>C3(1-2c3)</td><td>1-C3</td></tr><tr><td colspan="3"></td><td></td></tr><tr><td rowspan="2"></td><td>2(1-c3)(6c3-1-6c) 6c3-1-6c</td><td>2(1-c3）(6c3-1-6c2）</td><td>6cg-1-6c2</td></tr><tr><td>1 12c3(1-c3) 12c3(1-c3)</td><td>1 12c3(1-c3)</td><td>6cg-1-6c 12c3(1-c3)</td></tr></table>

for case II,

$$
{ \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { { \frac { 1 } { 2 } } } \\ { 1 } \\ { { \frac { 1 } { 2 c _ { 2 } } } - 1 \quad - { \frac { 1 } { 2 c _ { 2 } } } \quad { \mathrm { ~ 2 ~ } } } \\ { { \frac { 1 } { 6 } } } \end{array} } ;
$$

for case III,

for case IV,

$$
\begin{array} { r }   \begin{array} { c } { 0 } \\ { 1 } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} | _ { \begin{array} { c c c c c c } { \frac { 3 } { 8 } } & { \frac { 1 } { 8 } } & { } & { } & { } \\ { 1 - \frac { 1 } { 4 b _ { 4 } } } & { - \frac { 1 } { 1 2 b _ { 4 } } } & { \frac { 1 } { 3 b _ { 4 } } } & { } & { } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 6 } - b _ { 4 } } & { \frac { 2 } { 3 } } & { b _ { 4 } } \end{array} \} } \end{array}
$$

and for case V,

$$
\begin{array} { r l } & { \left. \begin{array} { c } { 0 } \\ { \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } \\ { 1 } \end{array} \right| \frac { 1 } { 2 } - \frac { 1 } { 6 b _ { 3 } } \qquad \frac { 1 } { 6 b _ { 3 } } } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad 1 - 3 b _ { 3 } \quad 3 b _ { 3 } \quad \right. } \\ & { \left. \qquad \frac { 1 } { 6 } \qquad \frac { 2 } { 3 } - b _ { 3 } \quad b _ { 3 } \quad \frac { 1 } { 6 } \qquad \right. } \end{array} .
$$

Some interesting special choices within these cases are $\begin{array} { r } { c _ { 3 } = \frac { 2 } { 3 } } \end{array}$

and $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 4 } } \end{array}$ in case II,

$$
\begin{array} { r } { { \frac { 1 } { 4 } } { \left| \begin{array} { l l l l } { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ } & { { \frac { 1 } { 2 } } } \end{array} \right| } ~ 0 \quad { { \frac { 1 } { 2 } } } } \\ { { \frac { 1 } { 6 } } { \frac { 1 } { 6 } } { \frac { - 2 } { 0 } } { \frac { 2 } { 3 } } { \begin{array} { l } { { \frac { 1 } { 6 } } } \end{array} } . } \end{array}
$$

A further, and somewhat eccentric, special choice in case II, is $c _ { 2 } = - \frac { 1 } { 2 }$

<table><tr><td>0 中</td><td></td></tr><tr><td></td><td>1 1</td><td>2</td><td></td></tr><tr><td></td><td>#</td><td>2</td><td></td></tr><tr><td></td><td>1</td><td></td><td>1</td></tr></table>

The interest in this method, as for a similar method with $c _ { 2 } = - 1$ , is that it is possible to eliminate one stage of computation, by replacing $F _ { 2 }$ by a quantity found in the previous step. The method contrived in this way is no longer a Runge–Kutta method, and has poorer stability, but it is more efficient in terms of order achieved per stages computed.

We also present the choices $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 1 2 } } \end{array}$ in case III,

$$
\begin{array} { r } { { \left. \begin{array} { c } { { 0 } } \\ { { \frac { 1 } { 2 } } } \\ { { 0 } } \\ { { 1 } } \end{array} \right| } \quad \frac { 1 } { 2 } \quad { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { 1 } } \end{array} \right. } } \\ { { \left. \begin{array} { l l l l l l } { { \frac { 1 } { 1 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { \left. \begin{array} { l } { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 1 2 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 1 2 } } } & { { \frac { 1 } { 6 } } } \end{array} \right. } } \end{array} \right. , } } \end{array}
$$

and $\begin{array} { r } { b _ { 4 } = \frac { 1 } { 6 } } \end{array}$ in case IV,

Amongst the methods in case V, the ‘classical Runge–Kutta method’ is especially notable. The tableau is

$$
\begin{array} { r } { \frac { 0 } { 2 } \left| \begin{array} { l l l l l } { ~ } & { ~ } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } & { ~ } \\ { ~ 0 } & { \frac { 1 } { 2 } } & { ~ } & { ~ } & { ~ } \\ { \frac { 1 } { 0 } } & { 0 } & { 1 } & { ~ } & { ~ } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 6 } } & { . ~ } \end{array} \right. } \end{array}
$$

Also in case V is a special method derived by Gill (1951), for the special purpose of reducing memory requirements for large problems. Gill found that by using a value $\begin{array} { r } { b _ { 3 } = \frac { 1 } { 3 } + \frac { \sqrt { 2 } } { 6 } } \end{array}$ , or the conjugate of this which was rejected as having larger errors, it was possible to solve an $N$ -dimensional system using only $3 N$ stored numbers. For a general method with $s = p = 4$ , the corresponding memory needs are $4 N$ . The tableau for Gill’s method is

$$
{ \begin{array} { c } { { \mathrm { ~ 0 ~ } } } \\ { { \frac { 1 } { 2 } } } \\ { { \mathrm { ~ 1 ~ } } } \\ { { \mathrm { ~ 1 ~ } } } \end{array} } { \frac { 1 } { 2 } } { \left| \begin{array} { l l l l l } { { \underline { { { \mathrm { ~ 1 ~ } } } } } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { \mathrm { ~ 2 ~ } } { 2 } } } & { { \underline { { { 2 \mathrm { - } } } } } { \sqrt { \underline { { { 2 } } } } } } & { { } } & { { } } \\ { { 0 } } & { { - { \frac { { \sqrt { 2 } } } { 2 } } } } & { { { \underline { { { 2 \mathrm { + } { \sqrt { 2 } } } } } } } } & { { } } \\ { { { \frac { 1 } { 6 } } } } & { { { \frac { { 2 \mathrm { - } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { { 2 \mathrm { + } } { \sqrt { 2 } } } { 6 } } } } & { { { \frac { 1 } { 6 } } } } \end{array} \right. }
$$

and is characterized by the condition

$$
\operatorname * { d e t } \left( { \left[ \begin{array} { l l l } { 1 } & { a _ { 3 1 } } & { a _ { 3 2 } } \\ { 1 } & { a _ { 4 1 } } & { a _ { 4 2 } } \\ { 1 } & { b _ { 1 } } & { b _ { 2 } } \end{array} \right] } \right) = 0
$$

which, for a method in case V, imposes the constraint

$$
1 8 b _ { 3 } ^ { 2 } - 1 2 b _ { 3 } + 1 = 0 ,
$$

with solutions

$$
b _ { 3 } = { \frac { 2 \pm { \sqrt { 2 } } } { 6 } } .
$$
