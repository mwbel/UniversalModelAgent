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

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/71923baf9d87d0db6b0f710dce5d05a07efdb04f42f6b951c4912ea7d5042abd.jpg)  
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
