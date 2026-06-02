1. Compute approximations to $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ using information available at the start of the step. Denote these ‘predicted’ values by $Y _ { i } ^ { [ 0 ] }$ , $i = 1 , 2 , \dots , s$ .

2. Carry out a sequence of iterations leading to approximations $Y _ { i } ^ { \left[ k \right] }$ , for $k = 1 , 2 , \dots$ , $i = 1 , 2 , \dots , s$ . These are given by the formulae

$$
Y _ { i } ^ { [ k ] } = Y _ { i } ^ { [ k - 1 ] } - \Delta _ { i } ,
$$

where

$$
\sum _ { j = 1 } ^ { s } m _ { i j } \Delta _ { j } = \phi _ { i } , \qquad i = 1 , 2 , \ldots , s ,
$$

with

$$
\phi _ { i } = Y _ { i } ^ { [ k - 1 ] } - y _ { n - 1 } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ^ { [ k - 1 ] } )
$$

and

$$
m _ { i j } = \delta _ { i j } I - h a _ { i j } f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } ) .
$$

3. Test for convergence and terminate when each of $\lVert \Delta _ { 1 } \rVert$ , $| | \Delta _ { 2 } | |$ , . . . , $\| \Delta _ { s } \|$ are sufficiently small. Suppose that this happens in the computation of iteration $k$ .

4. Assign $Y _ { i } ^ { \left[ k \right] }$ to $Y _ { i }$ , for each $i = 1 , 2 , \dots , s$

In a practical calculation, it is usual to simplify this computation in various ways. Most importantly, the solution of (360a), preceded by the evaluation of the elements of $m _ { i j }$ which depend on $f ^ { \prime }$ evaluated at each stage and in each iteration, requires a large number of algebraic operations; these are to be avoided whenever possible.

A typical simplification is to replace the value of $f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } )$ by a constant approximation to this Jacobian matrix. This approximation is maintained at a fixed value over every iteration and over each stage, and possibly over many steps. This means that the $s N \times s N$ matrix with elements built up from the submatrices $m _ { i j }$ can be replaced by a matrix of the form

$$
I _ { s } \otimes I _ { N } - h A \otimes J ,
$$

where $J$ is the Jacobian approximation. The cost, measured solely in terms of linear algebra costs, divides into two components. First, the factorization of the matrix (360b), carried out from time to time during the computation, costs a small multiple of $s ^ { 3 } N ^ { 3 }$ floating point operations. Secondly, the solution of (360a) costs a small multiple of $s ^ { 2 } N ^ { 2 }$ arithmetic operations per iteration.

It is the aim of the study of implementable methods to lower the factors $s ^ { 3 }$ in the occasional part of the cost and to lower the factor $s ^ { 2 }$ in the ‘per iteration’ part of the cost.

# 361 Diagonally implicit Runge–Kutta methods

Because of the excessive cost in evaluating the stages in a fully implicit Runge– Kutta method, we consider the so-called ‘diagonally implicit Runge–Kutta’ or DIRK methods (Alexander, 1977). For these methods, the coefficient matrix $A$ has a lower triangular structure with equal elements on the diagonal. Note that sometimes these methods are referred to as ‘singly diagonally implicit’ or SDIRK, with DIRK methods not necessarily having equal diagonals. Earlier names for methods in this general class are semi-implicit Runge–Kutta methods (Butcher, 1965)and semi-explicit (Nørsett, 1974).

The advantage of these methods is that the stages can be evaluated sequentially rather than as one great implicit system. We consider here the derivation of some low order members of this class with a brief analysis of their stability regions.

To obtain order 2 with two stages, consider the tableau

$$
\frac { \lambda } { \left| \begin{array} { c c c } { \lambda } & { 0 } & { } \\ { c _ { 2 } - \lambda } & { \lambda } & { } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right. } .
$$

The order conditions are

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } = 1 , } \\ { b _ { 1 } \lambda + b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } , } \end{array}
$$

with solution $\begin{array} { r } { b _ { 1 } = \frac { 2 c _ { 2 } - 1 } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ , $\begin{array} { r } { b _ { 2 } = \frac { 1 - 2 \lambda } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ . The method is A-stable if $\lambda \geq \frac { 1 } { 4 }$ and L-stable if $\lambda = 1 \pm \textstyle { \frac { 1 } { 2 } } { \sqrt { 2 } }$ . A particularly attractive choice is $c _ { 2 } = 1 , \lambda = 1 - { \textstyle \frac { 1 } { 2 } } \sqrt { 2 }$ , for which the tableau is

$$
\frac { 1 - \frac 1 2 \sqrt 2 } { 1 } \left| \begin{array} { c c } { 1 - \frac 1 2 \sqrt { 2 } } & { 0 } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \end{array} \right. .
$$

For $s = p = 3$ , the stability function is given by

$$
R ( z ) = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } + ( \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ) z ^ { 3 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial is found to be

$$
\mathrm {  ~ \psi ~ } ( y ) = \biggl ( \frac { 1 } { 1 2 } - \lambda + 3 \lambda ^ { 2 } - 2 \lambda ^ { 3 } \biggr ) y ^ { 4 } + \biggl ( - \frac { 1 } { 3 6 } + \frac { \lambda } { 2 } - \frac { 1 3 \lambda ^ { 2 } } { 4 } + \frac { 2 8 \lambda ^ { 3 } } { 3 } - 1 2 \lambda ^ { 4 } + 6 \lambda ^ { 5 } \biggr ) y ^ { 6 } .
$$

For $E ( y ) \ge 0$ , for all $y > 0$ , it is necessary and sufficient for A-stability that $\lambda \in [ \textstyle { \frac { 1 } { 3 } } , \widetilde { \lambda } ]$ , where $\tilde { \lambda } \approx 1 . 0 6 8 5 7 9 0 2 1 3$ is a zero of the coefficient of $y ^ { 4 }$ in $E ( y )$ . For

L-stability there is only one possible choice in this interval: $\lambda \approx 0 . 4 3 5 8 6 6 5 2 1 5$ , a zero of the coefficient of $z ^ { 3 }$ in the numerator of $R ( z )$ . Assuming $\lambda$ is chosen as this value, a possible choice for the remaining coefficients is given by the tableau

<table><tr><td rowspan=1 colspan=1>入(1+λ)1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4（-6)²+16λ-1）(6λ²-20λ+5）λ</td></tr></table>

# 362 The importance of high stage order

The asymptotic error behaviour of a numerical method underlines the importance of the order $p$ in ensuring high accuracy at minimal computing cost, as long as sufficient accuracy is required. If, for two methods, the asymptotic local truncation errors are, respectively, $C _ { 1 } h ^ { p _ { 1 } + 1 }$ and $C _ { 2 } h ^ { p _ { 2 } + 1 }$ , where $p _ { 2 } > p _ { 1 }$ , then the second method will always be more efficient as long as $h$ is taken to be sufficiently small. This argument ignores the fact that the methods might have differing costs per step, and therefore the stepsizes that make the work done by the methods comparable might be vastly different. It also ignores the fact that $C _ { 1 }$ and $C _ { 2 }$ can have such values that, for moderate stepsizes, the first method may be more efficient. This argument also ignores the fact that it is not just local errors that matter, but rather the accumulated global error after many steps; from the global error point of view it is also true that high orders will always eventually win over low orders. This ignores the case of special problems where there might be a cancellation of errors, so that in effect the order is greater than it would be for a general problem.

If the stage order is significantly lower than the order, then the final result computed will have depended for its value on much less accurate answers evaluated along the way. For non-stiff problems this is not a serious difficulty, because the order conditions take into account the need for the effect of these internal errors to cancel each other out. Asymptotically this also happens for stiff problems, but the magnitude of the stepsize required to enjoy the benefits of this asymptotic behaviour may depend drastically on the nature of the problem and on some quantitative measure of its stiffness.

To investigate this question, Prothero and Robinson (1974) considered a special family of problems of the form

$$
y ^ { \prime } ( x ) = L { \bigl ( } y ( x ) - g ( x ) { \bigr ) } + g ^ { \prime } ( x ) , \qquad y ( x _ { 0 } ) = g ( x _ { 0 } ) ,
$$

where $L$ is a negative constant and $g$ is a smooth function that varies at a moderate rate. We first look at the extreme ‘non-stiff’ case $L = 0$ . In this case the Prothero and Robinson problem becomes

$$
y ^ { \prime } ( x ) = g ^ { \prime } ( x ) ,
$$

and the defining equations for the solution computed by the Runge–Kutta method are

$$
\begin{array} { l } { { Y = y _ { n - 1 } \mathbf { 1 } + h A G ^ { \prime } , } } \\ { { y _ { n } = y _ { 0 } + h b ^ { \top } G ^ { \prime } , } } \end{array}
$$

where $G ^ { \prime }$ is the subvector made up from the values of $g ^ { \prime } ( x )$ evaluated at the stage values. We also write $G$ for the corresponding vector of $G ( x )$ values. Thus

$$
G = \left[ \begin{array} { c } { g ( x _ { n - 1 } + h c _ { 1 } ) } \\ { g ( x _ { n - 1 } + h c _ { 2 } ) } \\ { \vdots } \\ { g ( x _ { n - 1 } + h c _ { s } ) } \end{array} \right] , \qquad G ^ { \prime } = \left[ \begin{array} { c } { g ^ { \prime } ( x _ { n - 1 } + h c _ { 1 } ) } \\ { g ^ { \prime } ( x _ { n - 1 } + h c _ { 2 } ) } \\ { \vdots } \\ { g ^ { \prime } ( x _ { n - 1 } + h c _ { s } ) } \end{array} \right] .
$$

We see that the accuracy of the computation of $y _ { n }$ , as an approximation to $y ( x _ { n } )$ , is independent of the $A$ matrix and is determined by the accuracy of the quadrature formula

$$
\sum _ { i = 1 } ^ { s } b _ { i } \phi ^ { \prime } ( c _ { i } ) \approx \int _ { 0 } ^ { 1 } \phi ^ { \prime } ( \xi ) d \xi ,
$$

which we assume to be of order $p$ . This means that (362c) is exact for $\phi$ a polynomial of degree up to $p$ , and the error will be approximately

$$
{ \frac { 1 } { p ! } } \left( { \frac { 1 } { p + 1 } } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { p } \right) \phi ^ { ( p + 1 ) } ( 0 )
$$

and the error in the Runge–Kutta method for this problem will be

$$
\frac { h ^ { p + 1 } } { p ! } \left( \frac { 1 } { p + 1 } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { p } \right) g ^ { ( p + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) .
$$

Now return to the full Prothero and Robinson problem

$$
y ^ { \prime } ( x ) = L \Bigl ( y ( x ) - g ( x ) \Bigr ) + g ^ { \prime } ( x ) ,
$$

for which the computed results satisfy

$$
\begin{array} { r } { \begin{array} { r l } & { Y = y _ { n - 1 } \mathbf { 1 } + h A \left( L ( Y - G ) + G ^ { \prime } \right) , } \\ & { y _ { n } = y _ { n - 1 } + h b ^ { \top } \left( L ( Y - G ) + G ^ { \prime } \right) . } \end{array} } \end{array}
$$

Eliminate $Y$ , and we find

$$
y _ { n } = \Big ( 1 + h L b ^ { \top } ( I - h L A ) ^ { - 1 } { \bf 1 } \Big ) y _ { n - 1 } + h b ^ { \top } ( I - h L A ) ^ { - 1 } ( G ^ { \prime } - L G ) ,
$$

where the coefficient of $y _ { n - 1 }$ is seen to be the stability function value

$$
R ( h L ) = 1 + h L b ^ { \top } ( I - h L A ) ^ { - 1 } \mathbf { 1 } .
$$

By rearranging this expression we see that

$$
\begin{array} { r l } & { y _ { n } = R ( h L ) \Big ( y _ { n - 1 } - g ( x _ { n - 1 } ) \Big ) + g ( x _ { n - 1 } ) + h b ^ { \top } G ^ { \prime } } \\ & { \qquad + h L b ^ { \top } ( I - h L A ) ^ { - 1 } \Big ( h A G ^ { \prime } - ( G - g ( x _ { n - 1 } ) ) \Big ) } \\ & { \qquad = R ( h L ) \Big ( y _ { n - 1 } - g ( x _ { n - 1 } ) \Big ) + g ( x _ { n } ) - \epsilon _ { 0 } - h L b ^ { \top } ( I - h L A ) ^ { - 1 } \epsilon , } \end{array}
$$

where

$$
\epsilon _ { 0 } = h \int _ { 0 } ^ { 1 } g ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi - h \sum _ { i = 1 } ^ { s } b _ { i } g ^ { \prime } ( x _ { n - 1 } + h c _ { i } )
$$

is the non-stiff error term given approximately by (362d) and $\epsilon$ is the vector of errors in the individual stages with component $i$ given by

$$
h \int _ { 0 } ^ { c _ { i } } g ^ { \prime } ( x _ { n - 1 } + h \xi ) d \xi - h \sum _ { j = 1 } ^ { s } a _ { i j } g ^ { \prime } ( x _ { n - 1 } + h c _ { j } ) .
$$

If $L$ has a moderate size, then $h L b ^ { \mathsf { T } } ( I - h L A ) ^ { - 1 } \epsilon$ can be expanded in the form

$$
h L b ^ { \mathsf { T } } ( I + h L A + h ^ { 2 } L ^ { 2 } A ^ { 2 } + \cdot \cdot \cdot ) \epsilon
$$

and error behaviour of order $p$ can be verified term by term.

On the other hand, if $h L$ is large, a more realistic idea of the error is found using the expansion

$$
( I - h L A ) ^ { - 1 } = - \frac { 1 } { h L } A ^ { - 1 } - \frac { 1 } { h ^ { 2 } L ^ { 2 } } A ^ { - 2 } - \cdot \cdot \cdot ,
$$

and we obtain an approximation to the error, $g ( x _ { n } ) - y _ { n }$ , given by

$$
\begin{array} { c } { { g ( x _ { n } ) - y _ { n } = R ( h L ) \Big ( g ( x _ { n - 1 } ) - y _ { n - 1 } \Big ) + \epsilon _ { 0 } } } \\ { { - b ^ { \top } A ^ { - 1 } \epsilon - h ^ { - 1 } L ^ { - 1 } b ^ { \top } A ^ { - 2 } \epsilon - h ^ { - 2 } L ^ { - 2 } b ^ { \top } A ^ { - 3 } \epsilon - \cdot \cdot \cdot . . ~ . } } \end{array}
$$

Even though the stage order may be low, the final stage may have order $p$ . This will happen, for example, if the final row of $A$ is identical to the vector $b ^ { \prime }$ . In this special case, the term $b ^ { \scriptscriptstyle 1 } A ^ { - 1 } \epsilon$ will cancel $\epsilon _ { 0 }$ .

In other cases, the contributions from $b ^ { \intercal } A ^ { - 1 } \epsilon$ might dominate $\epsilon _ { 0 }$ , if the stage order is less than the order.

Define

$$
\eta _ { n } = \epsilon _ { 0 } + h L b ^ { \dag } ( I - h L A ) ^ { - 1 } \epsilon , \qquad n > 0 ,
$$

with $\eta _ { 0 }$ defined as the initial error $g ( x _ { 0 } ) - y _ { 0 }$ . The accumulated truncation error after $n$ steps is equal to

$$
\sum _ { i = 0 } ^ { n } R ( h L ) ^ { n - i } \eta _ { i } \approx \sum _ { i = 0 } ^ { n } R ( \infty ) ^ { n - i } \eta _ { i } .
$$

There are three important cases which arise in a number of widely use methods. If $R ( \infty ) = 0$ , as in the Radau IA, Radau IIA and Lobatto IIIC methods, or for that matter in any L-stable method, then we can regard the global truncation error as being just the error in the final step. Thus, if the local error is $O ( h ^ { q + 1 } )$ then the global error would also be $O ( h ^ { q + 1 } )$ . On the other hand, for the Gauss method with $s$ stages, $R ( \infty ) = ( - 1 ) ^ { s }$ . For the methods for which $R ( \infty ) = 1$ , then we can further approximate the global error as the integral of the local truncation error multiplied by $h ^ { - 1 }$ . Hence, a local error $O ( h ^ { q + 1 } )$ would imply a global error of $O ( h ^ { q } )$ . In the cases for which $R ( \infty ) = - 1$ we would expect the global error to be $O ( h ^ { q + 1 } )$ , because of cancellation of $\eta _ { i }$ over alternate steps.

We explore a number of example methods to see what can be expected for both local and global error behaviour.

For the Gauss methods, for which $p = 2 s$ , we can approximate $\epsilon _ { \mathrm { 0 } }$ by

$$
\frac { h ^ { 2 s + 1 } } { ( 2 s ) ! } \left( \frac { 1 } { 2 s + 1 } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 s } \right) g ^ { ( 2 s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 2 } ) ,
$$

which equals

$$
\frac { h ^ { 2 s + 1 } s ! ^ { 4 } } { ( 2 s ) ! ^ { 3 } ( 2 s + 1 ) } g ^ { ( 2 s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 2 } ) .
$$

Now consider the term $- b ^ { \intercal } A ^ { - 1 } \epsilon$ . This is found to equal

$$
\frac { h ^ { s + 1 } s ! } { ( 2 s ) ! ( s + 1 ) } g ^ { ( s + 1 ) } ( x _ { n - 1 } ) + O ( h ^ { s + 2 } ) ,
$$

which, if $| h L |$ is large, dominates (362e).

We also consider the important case of the Radau IIA methods. In this case $\epsilon _ { 0 }$ is approximately

$$
\begin{array} { r l r } {  { \frac { h ^ { 2 s } } { ( 2 s - 1 ) ! } ( \frac { 1 } { 2 s } - \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 s - 1 } ) g ^ { ( 2 s ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 1 } ) } } \\ & { } & \\ & { } & { = - \frac { h ^ { 2 s } s ! ( s - 1 ) ! ^ { 3 } } { 2 ( 2 s - 1 ) ! ^ { 3 } } g ^ { ( 2 s ) } ( x _ { n - 1 } ) + O ( h ^ { 2 s + 1 } ) . } \end{array}
$$

As we have remarked, for $| h L |$ large, this term is cancelled by $- b ^ { \intercal } A ^ { - 1 } \epsilon$ . Hence, the local truncation error can be approximated in this case by $- ( h L ) ^ { - 1 } b ^ { \mathsf { T } } A ^ { - 2 } \epsilon .$ . The value of this is

$$
\frac { s ! } { ( s + 1 ) ( 2 s - 1 ) ! } \frac { 1 } { h L } g ^ { ( s ) } ( x _ { n - 1 } ) h ^ { s } + O ( L ^ { - 1 } h ^ { s } ) .
$$

To summarize: for very stiff problems and moderate stepsizes, a combination modelled for the Prothero–Robinson problem by a high value of $h L$ , the stage order, rather than the classical order, plays a crucial role in determining the error behaviour. For this reason, we consider criteria other than superconvergence as important criteria in the identification of suitable methods for the solution of stiff problems. In particular, we look for methods that are capable of cheap implementation.

# 363 Singly implicit methods

We consider methods for which the stage order $q$ and the order are related by $p = q = s$ . To make the methods cheaply implementable, we also assume that

$$
\sigma ( A ) = \{ \lambda \} .
$$

The detailed study of methods for which $A$ has a one-point spectrum and for which $q \geq p - 1$ began with Burrage (1978). The special case $q = p$ was further developed in Butcher (1979), and this led to the implementation of STRIDE described in Burrage, Butcher and Chipman (1980).

Given $q = p$ and (363a), there will be a constraint on the abscissae of the method. To explore this, write down the $C ( s )$ conditions

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad i , k = 1 , 2 , \ldots , s ,
$$

or, more compactly,

$$
A c ^ { k - 1 } = \frac { 1 } { k } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

where $c ^ { k }$ denotes the component-by-component power.

We can now evaluate $A ^ { k - 1 } \mathbf { 1 }$ by induction. In fact,

$$
A ^ { k } \mathbf { 1 } = { \frac { 1 } { k ! } } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

because the case $k = 1$ is just (363b), also with $k = 1$ ; and the case $k > 1$ follows from (363c) with $k$ replaced by $k - 1$ and from (363b).

Because of (363a) and the Cayley–Hamilton theorem, we have

$$
( A - \lambda I ) ^ { s } = 0 .
$$

Laguerre polynomials $L _ { s }$ for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S L(S）</td></tr><tr><td>1 1 -</td></tr><tr><td>2 1 1 + s</td></tr><tr><td>北 3 3 1 1 + 1-6 2-35-3 5</td></tr><tr><td>4 1 + 4</td></tr><tr><td>124524 5 1 1 + 1 m5 120 S</td></tr><tr><td>6 6 1 1 十 1 1 6 20 720</td></tr><tr><td>中 10336° 583524 7 s² 7 5 7 6 1 57 7 1 十 m 4 40 十 720 5040 1</td></tr><tr><td>2 8 14g2 五 1 8 + + 7 × 7 1 1 s 7 + 15 180 630</td></tr></table>

Post-multiply by $\mathbf { 1 }$ and expand using the binomial theorem, and we find

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } A ^ { i } \mathbf { 1 } = \boldsymbol { 0 } .
$$

Using (363c), we find that

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } \frac { 1 } { i ! } c ^ { i } = 0 .
$$

This must hold for each component separately so that, for $i = 1 , 2 , \dots , s$ , $c _ { i } / \lambda$ is a zero of

$$
\sum _ { i = 0 } ^ { s } { \binom { s } { i } } ( - 1 ) ^ { i } \frac { ( - \xi ) ^ { i } } { i ! } .
$$

However, this is just the Laguerre polynomial of degree $s$ , usually denoted by $L _ { s } ( \xi )$ , and it is known that all its zeros are real and positive. For convenience, expressions for these polynomials, up to degree 8, are listed in Table 363(I) and approximations to the zeros are listed in Table 363(II). We saw in Subsection 361 that for $\lambda = \xi ^ { - 1 }$ for the case of three doubly underlined zeros of orders 2 and 3, L-stability is achieved. Double underlining to show similar choices for other orders is continued in the table and these are the only possibilities that exist (Wanner, Hairer and Nørsett, 1978). This means that there are no L-stable methods $^ -$ and in fact there is not even an A-stable method $-$ with $s = p = 7$ or with $s = p > 8$ . Even though fully L-stable methods are confined to the eight cases indicated in this table, there are other choices of $\lambda = \xi ^ { - 1 }$ that give stability which is acceptable for many problems. In each of the values of $\xi$ for which there is a single underline, the method is $\mathrm { A } ( \alpha )$ -stable with $\alpha \geq 1 . 5 5 \approx 8 9 ^ { \circ }$ .

Zeros of Laguerre polynomials for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S</td><td>$1,...,Ss</td><td></td><td></td><td></td></tr><tr><td>1</td><td>1.0000000000</td><td></td><td></td><td></td></tr><tr><td>2</td><td>0.5857864376</td><td>3.4142135624</td><td></td><td></td></tr><tr><td>3</td><td>0.4157745568</td><td>2.2942803603</td><td>6.2899450829</td><td></td></tr><tr><td>4</td><td>0.3225476896</td><td>1.7457611012</td><td>4.5366202969</td><td>9.3950709123</td></tr><tr><td>5</td><td>0.2635603197</td><td>1.4134030591</td><td>3.5964257710</td><td>7.0858100059</td></tr><tr><td>6</td><td>12.6408008443</td><td></td><td></td><td></td></tr><tr><td></td><td>0.2228466042</td><td>1.1889321017</td><td>2.9927363261</td><td>5.7751435691</td></tr><tr><td></td><td>9.8374674184</td><td>15.9828739806</td><td></td><td></td></tr><tr><td>7</td><td>0.1930436766</td><td>1.0266648953</td><td>2.5678767450</td><td>4.9003530845</td></tr><tr><td></td><td>8.1821534446</td><td>12.7341802918</td><td>19.3957278623</td><td></td></tr><tr><td>8</td><td>0.1702796323</td><td>0.9037017768</td><td>2.2510866299</td><td>4.2667001703</td></tr><tr><td></td><td>7.0459054024</td><td>10.7585160102</td><td>15.7406786413</td><td>22.8631317369</td></tr></table>

The key to the efficient implementation of singly implicit methods is the similarity transformation matrix that transforms the coefficient matrix to lower triangular form. Let $T$ denote the matrix with $( i , j )$ element

$$
t _ { i j } = L _ { j - 1 } ( \xi _ { i } ) , \qquad i , j = 1 , 2 , \ldots , s .
$$

The principal properties of $T$ and its relationship to $A$ are as follows:

Theorem 363A The $( i , j )$ element of $T ^ { - 1 }$ is equal to

$$
\frac { \xi _ { j } } { s ^ { 2 } L _ { s - 1 } ( \xi _ { j } ) ^ { 2 } } L _ { i - 1 } ( \xi _ { j } ) .
$$

Let $\widetilde { A }$ denote $T ^ { - 1 } A T$ ; then

$$
\widetilde { A } = \lambda \left[ \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 1 } & { 1 } \end{array} \right] .
$$

Proof. To prove (363d), use the Christoffel–Darboux formula for Laguerre polynomials in the form

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( x ) L _ { k } ( y ) = \frac s { x - y } \big ( L _ { s } ( y ) L _ { s - 1 } ( x ) - L _ { s } ( x ) L _ { s - 1 } ( y ) \big ) .
$$

For $i \neq j$ , substitute $x = \xi _ { i } , y = \xi _ { j }$ to find that rows $i$ and $j$ of $T$ are orthogonal. To evaluate the inner product of row $i$ with itself, substitute $y = \xi _ { i }$ and take the limit as $x \to \xi _ { i }$ . It is found that

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( \xi _ { k } ) ^ { 2 } = - s L _ { s } ^ { \prime } ( \xi _ { i } ) L _ { s - 1 } ( \xi _ { i } ) = \frac { s ^ { 2 } L _ { s - 1 } ( \xi _ { i } ) ^ { 2 } } { \xi _ { i } } .
$$

The value of $T T ^ { \rvert }$ as a diagonal matrix with $( i , i )$ element given by (363f) is equivalent to (363d).

The formula for $\widetilde { A }$ is verified by evaluating

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( \xi _ { j } ) = \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( c _ { j } / \lambda ) } \\ { = \displaystyle \int _ { 0 } ^ { \lambda \xi _ { i } } L _ { k - 1 } ( c _ { j } / \lambda ) d t } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } L _ { k - 1 } ( t ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d t } \\ { = \lambda ( L _ { k - 1 } ( \xi _ { i } ) - L _ { k } ( \xi _ { i } ) ) d t , } \end{array}
$$

where we have used known properties of Laguerre polynomials. The value of this sum is equivalent to (363e). 

For convenience we sometimes write

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right] ,
$$

so that (363e) can be written

$$
{ \widetilde { A } } = \lambda ( I - J ) .
$$

We now consider the possible A-stability or L-stability of singly implicit methods. This hinges on the behaviour of the rational functions

$$
R ( z ) = { \frac { N ( z ) } { ( 1 - \lambda z ) ^ { s } } } ,
$$

where the degree of the polynomial $N ( z )$ is no more than $s$ , and where

$$
N ( z ) = \exp ( z ) ( 1 - \lambda z ) ^ { s } + O ( z ^ { s + 1 } ) .
$$

We can obtain a formula for $N ( z )$ as follows:

$$
N ( z ) = \sum _ { i = 0 } ^ { s - i } ( - \lambda ) ^ { i } L _ { s } ^ { ( s - i ) } \left( \frac { 1 } { \lambda } \right) z ^ { i } ,
$$

where $L _ { n } ^ { ( m ) }$ denotes the $m$ -fold derivative of $L _ { n }$ , rather than a generalized Laguerre polynomial. To verify the L-stability of particular choices of $s$ and $\lambda$ , we note that all poles of $N ( z ) / ( 1 - \lambda z ) ^ { s }$ are in the right half-plane. Hence, it is necessary only to test that $| D ( z ) | ^ { 2 } - | ( 1 - \lambda z ) ^ { s } | ^ { 2 } \ge 0$ , whenever $z$ is on the imaginary axis. Write $z = i y$ and we find the ‘E-polynomial’ defined in this case as

$$
E ( y ) = ( 1 + \lambda ^ { 2 } y ^ { 2 } ) ^ { s } - N ( i y ) N ( - i y ) ,
$$

with $E ( y ) \ge 0$ for all real $y$ as the condition for A-stability. Although Astability for $s = p$ is confined to the cases indicated in Table 363(II), it will be seen in the next subsection that higher values of $s$ can lead to additional possibilities.

We conclude this subsection by constructing the two-stage L-stable singly implicit method of order 2. From the formulae for the first few Laguerre polynomials,

$$
L _ { 0 } ( x ) = 1 , \quad L _ { 1 } ( x ) = 1 - x , \quad L _ { 2 } ( x ) = 1 - 2 x + \frac { 1 } { 2 } x ^ { 2 } ,
$$

we find the values of $\xi _ { 1 }$ and $\xi _ { 2 }$ , and evaluate the matrices $T$ and $T ^ { - 1 }$ . We have

$$
\xi _ { 1 } = 2 - \sqrt { 2 } , \qquad \xi _ { 2 } = 2 + \sqrt { 2 }
$$

and

$$
\begin{array} { r } { \mathrm { ~  ~ { ~ \sigma ~ } ~ } ^ { \prime } = \left[ \begin{array} { l l } { L _ { 0 } ( \xi _ { 1 } ) } & { L _ { 1 } ( \xi _ { 1 } ) } \\ { L _ { 0 } ( \xi _ { 2 } ) } & { L _ { 1 } ( \xi _ { 2 } ) } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { - 1 + \sqrt { 2 } } \\ { 1 } & { - 1 - \sqrt { 2 } } \end{array} \right] , \quad T ^ { - 1 } = \left[ \begin{array} { l l } { \frac { 1 } { 2 } + \frac { \sqrt { 2 } } { 4 } } & { \frac { 1 } { 2 } - \frac { \sqrt { 2 } } { 4 } } \\ { \frac { \sqrt { 2 } } { 4 } } & { - \frac { \sqrt { 2 } } { 4 } } \end{array} \right] . } \end{array}
$$

For L-stability, choose $\begin{array} { r } { \lambda = \xi _ { 2 } ^ { - 1 } = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ , and we evaluate $A = \lambda T ( I - J ) T ^ { - 1 }$ to give the tableau

$$
{ \frac { 3 - 2 { \sqrt { 2 } } } { 1 } } { \frac { \frac { 5 } { 4 } - { \frac { 3 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } + { \frac { 1 } { 4 } } { \sqrt { 2 } } } } { \frac { \frac { 7 } { 4 } - { \frac { 5 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } - { \frac { 1 } { 4 } } { \sqrt { 2 } } } }  .
$$

In the implementation of this, or any other, singly implicit method, the actual entries in this tableau are not explicitly used. To emphasize this point, we look in detail at a single Newton iteration for this method. Let $M = I - h \lambda f ^ { \prime } ( y _ { n - 1 } )$ . Here the Jacobian matrix $f ^ { \prime }$ is supposed to have been evaluated at the start of the current step. In practice, a Jacobian evaluated at an earlier time value might give satisfactory performance, but we do not dwell on this point here. If the method were to be implemented with no special use made of its singly implicit structure, then we would need, instead of the $N \times N$ matrix $M$ , a $2 N \times 2 N$ matrix $\widetilde { M }$ given by

$$
\widetilde { \cal M } = \left[ \begin{array} { c c } { { I - h a _ { 1 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { - h a _ { 1 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \\ { { - h a _ { 2 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { I - h a _ { 2 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \end{array} \right] .
$$

In this ‘fully implicit’ situation, a single iteration would start with the input approximation $y _ { n - 1 }$ and existing approximations to the stage values and stage derivatives $Y _ { 1 }$ , $Y _ { 2 }$ , $h F _ { 1 }$ and $h F _ { 2 }$ . It will be assumed that these are consistent with the requirements that

$$
Y _ { 1 } = y _ { n - 1 } + a _ { 1 1 } h F _ { 1 } + a _ { 1 2 } h F _ { 2 } , \quad Y _ { 2 } = y _ { n - 1 } + a _ { 2 1 } h F _ { 1 } + a _ { 2 2 } h F _ { 2 } ,
$$

and the iteration process will always leave these conditions intact.

# 364 Generalizations of singly implicit methods

In an attempt to improve the performance of existing singly implicit methods, Butcher and Cash (1990) considered the possibility of adding additional diagonally implicit stages. For example, if $s ~ = ~ p + 1$ is chosen, then the coefficient matrix has the form

$$
\begin{array} { r } { A = \left[ \begin{array} { c c } { \lambda \widehat { A } } & { 0 } \\ { b ^ { \top } } & { \lambda } \end{array} \right] , } \end{array}
$$

where $\widehat { A }$ is the matrix

$$
{ \widehat { A } } = T ( I - J ) T ^ { - 1 } .
$$

An appropriate choice of $\lambda$ is made by balancing various considerations. The first of these is good stability, and the second is a low error constant. Minor considerations would be convenience, the avoidance of coefficients with abnormally large magnitudes or with negative signs, where possible, and a preference for methods in which the $c _ { i }$ lie in $[ 0 , 1 ]$ . We illustrate these ideas for the case $p = 2$ and $s = 3$ , for which the general form for a method would be

<table><tr><td>入(2-√2) 入(2+√2)</td><td colspan="3">入(1-√2) 入(1+√②)</td><td>&gt;(1-√2) 入(1+1√②)</td><td>0 0</td></tr><tr><td rowspan="3">1</td><td>2+3√2_ λ(1+√2) 4</td><td>2 2 8</td><td>2-3√2_(1-√2) 4</td><td>3 2</td><td rowspan="3">入 入</td></tr><tr><td>2+3√2</td><td>入(1+√2)</td><td>2-3√2</td><td></td></tr><tr><td>4</td><td>2 2 8</td><td>4</td><td>入(1-√2) 点 + 2</td></tr></table>

![](images/c0b1581105a7e8352a8baf7e761a8469c17426adeb496aeaacbfbe83a5eded4e.jpg)  
Error constant $C ( \lambda )$ for $\lambda \in [ 0 . 1 , 0 . 5 ]$

The only choice available is the value of $\lambda$ , and we consider the consequence of making various choices for this number. The first criterion is that the method should be A-stable, and we analyse this by calculating the stability function

$$
R ( z ) = \frac { N ( z ) } { D ( z ) } = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial

$$
\begin{array} { r } { E ( y ) = | D ( i y ) | ^ { 2 } - | N ( i y ) | ^ { 2 } = \Big ( 3 \lambda ^ { 4 } - \big ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } \big ) ^ { 2 } \Big ) y ^ { 4 } + \lambda ^ { 6 } y ^ { 6 } . } \end{array}
$$

For A-stability, the coefficient of $y ^ { 4 }$ must be non-negative. The condition for this is that

$$
\frac { 3 - { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } \leq \lambda \leq \frac { 3 + { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } ,
$$

or that $\lambda$ lies in the interval [0.180425, 2.185600]. The error constant $C ( \lambda )$ , defined by $\exp ( z ) - R ( z ) = C ( \lambda ) z ^ { 3 } + O ( z ^ { 4 } )$ , is found to be

$$
C ( \lambda ) = \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ,
$$

and takes on values for $\lambda \in [ 0 . 1 , 0 . 5 ]$ , as shown in Figure 364(i).

The value of $b _ { 1 }$ is positive for $\lambda > 0 . 1 2 5 4 4 1$ . Furthermore $b _ { 2 }$ is positive for $\lambda < 0 . 3 6 4 3 3 5$ . Since $b _ { 1 } + b _ { 2 } + \lambda = 1$ , we obtain moderately sized values of all components of $b ^ { \top }$ if $\lambda \in [ 0 . 1 2 5 4 4 1 , 0 . 3 6 4 3 3 5$ ]. The requirement that $c _ { 1 }$ and $c _ { 2 }$ lie in $( 0 , 1 )$ is satisfied if $\lambda < ( 2 - \sqrt { 2 } ) ^ { - 1 } \approx 0 . 2 9 2 8 9 3$ . Leaving aside the question of convenience, we should perhaps choose $\lambda \approx 0 . 1 8 0 4 2 5$ so that the error constant is small, the method is A-stable, and the other minor considerations are all satisfied. Convenience might suggest an alternative value $\textstyle \lambda = { \frac { 1 } { 5 } }$ .

# 365 Effective order and DESIRE methods

An alternative way of forcing singly implicit methods to be more appropriate for practical computation is to generalize the order conditions. This has to be done without lowering achievable accuracy, and the use of effective order is indicated. Effective order is discussed in a general setting in Subsection 389 but, for methods with high stage order, a simpler analysis is possible.

Suppose that the quantities passed from one step to the next are not necessarily intended to be highly accurate approximations to the exact solution, but rather to modified quantities related to the exact result by weighted Taylor series. For example, the input to step $_ { n }$ might be an approximation to

$$
y ( x _ { n - 1 } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n - 1 } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n - 1 } ) .
$$

We could regard a numerical method, which produces an output equal to

$$
y _ { n } = y ( x _ { n } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n } ) + O ( h ^ { p + 1 } ) ,
$$

as a satisfactory alternative to a method of classical order $p$ .

We explore this idea through the example of the effective order generalization of the L-stable order 2 singly implicit method with the tableau (363g). For this method, the abscissae are necessarily equal to $3 - 2 { \sqrt { 2 } }$ and $^ { 1 }$ , which are quite satisfactory for computation. However, we consider other choices, because in the more complicated cases with $s = p > 2$ , at least one of the abscissae is outside the interval $[ 0 , 1 ]$ , for A-stability.

If the method is required to have only effective order 2, then we can assume that the incoming and outgoing approximations are equal to

$$
\begin{array} { c } { { y _ { n - 1 } = y ( x _ { n - 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { p + 1 } ) , } } \\ { { y _ { n } = y ( x _ { n } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n } ) + O ( h ^ { p + 1 } ) , } } \end{array}
$$

respectively. Suppose that the stage values are required to satisfy

$$
Y _ { 1 } = y ( x _ { n - 1 } + h c _ { 1 } ) + O ( h ^ { 3 } ) , \qquad Y _ { 2 } = y ( x _ { n - 1 } + h c _ { 2 } ) + O ( h ^ { 3 } ) ,
$$

with corresponding approximations for the stage derivatives. In deriving the order conditions, it can be assumed, without loss of generality, that $n = 1$ . The order conditions for the two stages and for the output approximation $y _ { n } = y _ { 1 }$ are

$$
\begin{array} { r l } & { y ( x _ { 0 } + h c _ { 1 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h \alpha _ { 1 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h \alpha _ { 1 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 0 } + h c _ { 2 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h a _ { 2 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h a _ { 2 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 1 } ) } \\ & { \qquad = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h b _ { 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h b _ { 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) . } \end{array}
$$

These can be converted into algebraic relations on the various free parameters by expanding by Taylor series about $x _ { 0 }$ and equating coefficients of $h y ^ { \prime } ( x _ { 0 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } )$ . This gives the conditions

$$
\begin{array} { c } { { c _ { 1 } = \alpha _ { 1 } + a _ { 1 1 } + a _ { 1 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 1 } ^ { 2 } = \alpha _ { 2 } + a _ { 1 1 } c _ { 1 } + a _ { 1 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { c _ { 2 } = \alpha _ { 1 } + a _ { 2 1 } + a _ { 2 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = \alpha _ { 2 } + a _ { 2 1 } c _ { 1 } + a _ { 2 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { { 1 + \alpha _ { 1 } = \alpha _ { 1 } + b _ { 1 } + b _ { 2 } , } } } \\ { { { { \frac { 1 } { 2 } + \alpha _ { 1 } + \alpha _ { 2 } = \alpha _ { 2 } + b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } . } } } } \end{array}
$$

Because of the single-implicitness condition $\sigma ( A ) = \{ \lambda \}$ , we also have

$$
\begin{array} { r } { a _ { 1 1 } + a _ { 2 2 } = 2 \lambda , } \\ { a _ { 1 1 } a _ { 2 2 } - a _ { 2 1 } a _ { 1 2 } = \lambda ^ { 2 } . } \end{array}
$$

Assuming that $c _ { 1 }$ and $c _ { 2 }$ are distinct, a solution to these equations always exists, and it leads to the values

$$
\begin{array} { r } { \alpha _ { 1 } = \frac 1 2 ( c _ { 1 } + c _ { 2 } ) - 2 \lambda , \quad \alpha _ { 2 } = \frac 1 2 c _ { 1 } c _ { 2 } - \lambda ( c _ { 1 } + c _ { 2 } ) + \lambda ^ { 2 } , } \end{array}
$$

together with the tableau

$$
\frac { c _ { 1 } \ { \boxed { \begin{array} { r l r l } { { c _ { 2 } } } & { { - \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda + \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } & & { \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } \end{array} } } } { \frac { \lambda } { c _ { 2 } } } } & { \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } { \frac { \lambda } { c _ { 2 } } + \frac { 2 \lambda - \frac { 1 } { 2 } } { c _ { 2 } - c _ { 1 } } }  &  .
$$

In the special case $c ^ { \mathsf { T } } = [ 0 , 1 ]$ , with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ for L-stability, we find $\begin{array} { r } { \alpha _ { 1 } = \sqrt { 2 } - \frac { 3 } { 2 } } \end{array}$ and $\alpha _ { 2 } = \textstyle { \frac { 1 } { 2 } } ( 1 - { \sqrt { 2 } } )$ and the tableau

$$
{ \frac { 1 \left| { \begin{array} { l l } { { \frac { 1 } { 2 } } } ( 4 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } ( { \sqrt { 2 } } - 1 ) } \\ { { \frac { 1 } { 2 } } ( 5 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } { \sqrt { 2 } } } \end{array} \right.}  } { 2 - { \sqrt { 2 } } }  ~ .
$$

Combine the effective order idea with the diagonal extensions introduced in Subsection 364, and we obtain ‘DESIRE’ methods (diagonally extended by the example with implicit Runge–Kutta methods using effective order). These are exemplified $p = 2$ , $s = 3$ and $\textstyle \lambda = { \frac { 1 } { 5 } }$ . For this method, $\alpha _ { 1 } = - \frac { 3 } { 2 0 }$ $\begin{array} { r } { \alpha _ { 2 } = \frac { 1 } { 4 0 0 } } \end{array}$ and the coefficient tableau is

<table><tr><td>0</td><td>31 200</td><td>1 200</td><td>0</td></tr><tr><td rowspan="4"></td><td>81</td><td>49</td><td>0</td></tr><tr><td>200</td><td>200</td><td></td></tr><tr><td>71</td><td>119</td><td></td></tr><tr><td>200</td><td>200</td><td>1</td></tr><tr><td rowspan="2"></td><td>103</td><td>119</td><td>14</td></tr><tr><td>250</td><td>250</td><td>125</td></tr></table>

# Exercises 36

36.1 Derive the tableau for the two-stage order 2 diagonally implicit method satisfying (361a), (361b) with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ and $c _ { 2 } = 3 \lambda$ .

36.2 Rewrite the method in Exercise 36.1 so that the value of $Y _ { 1 }$ in step $n$ is the input and the value of $Y _ { 1 }$ in step $n + 1$ is the output.

36.3 Show that the method derived in Exercise 36.2 has stage order 2.

36.4 Derive a diagonally implicit method with $s = p = 3$ and with $\lambda = c _ { 2 } =$ $\textstyle { \frac { 1 } { 3 } }$ , $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , $c _ { 3 } = 1$ .

36.5 Derive a diagonally implicit method with $s = p = 3$ , $\lambda = 1$ , $c _ { 2 } = { \textstyle { \frac { 1 } { 3 } } }$ , $c _ { 3 } = 1$ , $b _ { 1 } = 0$ .

36.6 Show that for an L-stable method of the type described in Subsection 364 with $p = 3$ , $s = 4$ , the minimum possible value of $\lambda$ is approximately 0.2278955169, a zero of the polynomial

$1 8 5 9 7 6 \lambda ^ { 1 2 } - 1 4 9 0 4 0 0 \lambda ^ { 1 1 } + 4 6 0 1 4 4 8 \lambda ^ { 1 0 } - 7 2 5 7 1 6 8 \lambda ^ { 9 } + 6 8 4 2 8 5 3 \lambda ^ { 8 }$ $- 4 1 8 1 7 6 0 \lambda ^ { 7 } + 1 7 2 4 2 5 6 \lambda ^ { 6 } - 4 8 7 2 9 6 \lambda ^ { 5 } + 9 4 1 7 6 \lambda ^ { 4 } - 1 2 1 9 2 \lambda ^ { 3 } + 1 0 0 8 \lambda ^ { 2 } - 4 8 \lambda + 1 . 0 0 0 9 4 1 6 \lambda ^ { 5 }$ .

# 37 Symplectic Runge–Kutta Methods

# 370 Maintaining quadratic invariants

We recall Definition 357B in which the matrix $M$ plays a role, where the elements of $M$ are

$$
\begin{array} { r } { m _ { i j } = b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } . } \end{array}
$$

Now consider a problem for which

$$
y ^ { \mathsf { T } } Q f ( y ) = 0 ,
$$

for all $y$ . It is assumed that $Q$ is a symmetric matrix so that (370b) is equivalent to the statement that $y ( x ) ^ { 1 } Q y ( x )$ is invariant.

We want to characterize Runge–Kutta methods with the property that $y _ { n } ^ { \mathsf { T } } Q y _ { n }$ is invariant with $n$ so that the the numerical solution preserves the conservation law possessed by the problem. If the input to step $1$ is $y _ { 0 }$ , then the output will be

$$
y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } , 
$$

where the stage derivatives are $F _ { i } = f ( Y _ { i } )$ , with

$$
Y _ { i } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } .
$$

From (370b) it follows that

$$
\boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q y _ { 0 } } = - h \sum _ { j = 1 } ^ { s } a _ { i j } \boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q F } _ { j } .
$$

Use (370c) to calculate $y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 }$ and substitute from (370d) to obtain the result

$$
y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 } = y _ { 0 } ^ { \mathsf { T } } Q y _ { 0 } - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } F _ { i } ^ { \mathsf { T } } Q F _ { j } ,
$$

with $m _ { i j }$ given by (370a).

Thus $M ~ = ~ 0$ implies that quadratic invariants are preserved and, in particular, that symplectic behaviour is maintained. Accordingly, we have the following definition:

Definition 370A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is symplectic if

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is the zero matrix.

The property expressed by Definition 370A was first found by Cooper (1987) and, as a characteristic of symplectic methods, by Lasagni (1988), Sanz-Serna (1988) and Suris (1988).

# 371 Examples of symplectic methods

A method with a single stage is symplectic only if $2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = 0$ . For consistency, that is order at least $^ { 1 }$ , $b _ { 1 } = 1$ and hence $\begin{array} { r } { c _ { 1 } = a _ { 1 1 } = \frac { 1 } { 2 } } \end{array}$ ; this is just the implicit mid-point rule. We can extend this in two ways: by either looking at methods where $A$ is lower triangular or looking at the methods with stage order $s$ .

For lower triangular methods we will assume that none of the $b _ { i }$ is zero. The diagonals can be found from $2 b _ { i } a _ { i i } = b _ { i } ^ { 2 }$ to be $\begin{array} { r } { a _ { i i } = \frac { 1 } { 2 } b _ { i } } \end{array}$ . For the elements of $A$ below the diagonal we have $b _ { i } a _ { i j } = b _ { i } b _ { j }$ so that $a _ { i j } = b _ { j }$ . This gives a tableau

$$
 \begin{array} { r l } { { \frac { 1 } { 2 } } b _ { 1 } } & { { | \begin{array} { l } { { \frac { 1 } { 2 } } b _ { 1 } } \\ { b _ { 1 } + { \frac { 1 } { 2 } } b _ { 2 } } \end{array}  } } &  { | \begin{array} { l l l l l } { { \frac { 1 } { 2 } } b _ { 1 } } & { } & { } & { } & { } \\ { b _ { 1 } } & { { \frac { 1 } { 2 } } b _ { 2 } } & { } & { } & { } \\ { b _ { 1 } } & { b _ { 2 } } & { { \frac { 1 } { 2 } } b _ { 3 } } & { } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } \\ { b _ { 1 } + \cdot \cdot + b _ { s - 1 } + { \frac { 1 } { 2 } } b _ { s } } & { { | \begin{array} { l l l l l l } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { { \frac { 1 } { 2 } } b _ { s } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { b _ { s } } \end{array}  } } \end{array} } \end{array}
$$

This method is identical with $s$ steps of the mid-point rule with stepsizes $b _ { 1 } h$ , $b _ { 2 } h$ , $\cdot \cdot \cdot$ , $b _ { s } h$ .

For methods with order and stage order equal to $s$ , we have, in the notation of Subsection 358, $\epsilon _ { i } = 0$ for $i = s + 1$ , $s + 2$ , $\cdot \cdot \cdot$ , $2 s$ . This follows from the observation that $V ^ { \ I } M V = 0$ . Thus, in addition to $B ( s )$ , $B ( 2 s )$ holds. Hence, the abscissae of the method are the zeros of $P _ { s } ^ { * }$ and the method is the $s$ -stage Gauss method.

# 372 Order conditions

Given rooted trees $t$ , $u$ and a symplectic Runge–Kutta method, we consider the relationship between the elementary weights $\phi ( t u ) , \phi ( u t ) , \phi ( t ) , \phi ( u )$ . Write

$$
\Phi ( t ) = \sum _ { i = 1 } b _ { i } \phi _ { i } , \quad \Phi ( u ) = \sum _ { i = 1 } b _ { i } \psi _ { i } .
$$

Then we find

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) = \sum _ { i , j = 1 } ^ { s } b _ { i } \phi _ { i } a _ { i j } \psi _ { j } , } \\ { \displaystyle \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } b _ { j } \psi _ { j } a _ { j i } \phi _ { i } , } \end{array}
$$

so that

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) + \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } ( b _ { i } a _ { i j } + b _ { j } a _ { j i } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \sum _ { i , j = 1 } ^ { s } ( b _ { i } b _ { j } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \Phi ( t ) \Phi ( u ) . } \end{array}
$$

Assuming the order conditions $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ are satisfied, then

$$
\Phi ( t u ) - \frac { 1 } { \gamma ( t u ) } + \Phi ( u t ) - \frac { 1 } { \gamma ( u t ) } = 0 .
$$

Using this fact, we can prove the following theorem:

Theorem 372A Let $( A , b ^ { \prime } , c )$ be a symplectic Runge–Kutta method. The method has order $p$ if and only if for each non-superfluous tree and any vertex in this tree as root, $\Phi ( t ) = 1 / \gamma ( t )$ , where $t$ is the rooted tree with this vertex.

Proof. We need only to prove the sufficiency of this criterion. If two rooted trees belong to the same tree but have vertices $v _ { 0 }$ , $\widehat { v }$ say, then there is a sequence of vertices $v _ { 0 }$ , $v _ { 1 }$ , $\cdot \cdot \cdot$ , $v _ { m } = \widehat { v }$ , such that $v _ { i - 1 }$ and $v _ { i }$ are adjacent for $i = 1 , 2 , \dots , m$ . This mean that rooted trees $t , u$ exist such that $t u$ is the rooted tree with root $v _ { i - 1 }$ and $u t$ is the rooted tree with root $v _ { i }$ . We are implicitly using induction on the order of trees and hence we can assume that $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ . Hence, if one of the order conditions for the trees $t u$ and $u t$ is satisfied, then the other is. By working along the chain of possible roots $v _ { 0 } , v _ { 1 } , \ldots , v _ { m }$ , we see that the order condition associated with the root $v _ { 0 }$ is equivalent to the condition for $\widehat { v }$ . In the case of superfluous trees, one choice of adjacent vertices would imply that $t = u$ . Hence, (372a) is equivalent to $2 \Phi ( t t ) = 2 / \gamma ( t t )$ so that the order condition associated with $t t$ is satisfied and all rooted trees belonging to the same tree are also satisfied.

The first experiment uses the simple pendulum based on the Hamiltonian $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ and initial value $\left( p , q \right) = \left( 1 , 0 \right)$ . The amplitude is found to be $\pi / 3 \approx 1 . 0 4 7 1 9 8$ and the period to be approximately 6.743001. Numerical solutions, displayed in Figure 373(i), were found using the Euler, implicit Euler and the implicit mid-point rule methods. Only the last of these is symplectic and its behaviour reflects this. That is, like the exact solution which is also shown, the area of the initial set remains unchanged, even though its shape is distorted.

The second experiment is based on problem (122c), which evolves on the unit sphere $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ . The value of $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ is calculated by the Euler method, the implicit Euler method and the implicit mid-point rule method. Only the last of these is symplectic. The computed results are shown in Figure 373(ii). In each case a stepsize $h = 0 . 1$ was used. Although results are shown for only 500 time steps, the actual experiment was extended much further. There is no perceptible deviation from $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ for the first million steps.

![](images/83a6e1ff135a200883a79c61d1e2a5fd54639e36ae4148227af8a545daa4bdd1.jpg)  
Solutions of the Hamiltonian problem $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ . Left: Euler method (grey) and implicit Euler method (white). Right: exact solution (grey) and implicit mid-point method (white). The underlying image depicts the takahe Porphyrio hochstetteri, rediscovered in 1948 after many years of presumed extinction.

![](images/49ea0f5ff0444cf6688a2b9cb532cb3bfd5aa23c33b768de46a5533e41ed7d97.jpg)  
Experiments for problem (122c). The computed value of $\| y _ { n } \| ^ { 2 }$ is shown after $n = 1 , 2 , \ldots$ , steps.

# Exercises 37

37.1 Do two-stage symplectic Runge–Kutta methods exist which have order 3 but not order 4?

37.2 Do three-stage order 3 symplectic Runge–Kutta methods exist for which $A$ is lower triangular?

# 38 Algebraic Properties of Runge–Kutta Methods

# 380 Motivation

For any specific $N$ -dimensional initial value problem, Runge–Kutta methods can be viewed as mappings from $\mathbb { R } ^ { N }$ to $\mathbb { R } ^ { N }$ . However, the semi-group generated by such mappings has a significance independent of the particular initial value problem, or indeed of the vector space in which solution values lie. If a method with $s _ { 1 }$ stages is composed with a second method with $s _ { 2 }$ stages, then the combined method with $s _ { 1 } + s _ { 2 }$ stages can be thought of as the product of the original methods. It turns out that this is not quite the best way of formulating this product, and we need to work with equivalence classes of Runge–Kutta methods. This will also enable us to construct a group, rather than a mere semi-group.

It will be shown that the composition group of Runge–Kutta equivalent classes is homomorphic to a group on mappings from trees to real numbers. In fact the mapping that corresponds to a specific Runge–Kutta method is just the function that takes each tree to the associated elementary weight.

There are several reasons for introducing and studying these groups. For Runge–Kutta methods themselves, it is possible to gain a better understanding of the order conditions by looking at them in this way. Furthermore, methods satisfying certain simplifying assumptions, notably the $C$ and $D$ conditions, reappear as normal subgroups of the main group. An early application of this theory is the introduction of the concept of ‘effective order’. This is a natural generalization from this point of view, but makes very little sense from a purely computational point of view. While effective order was not widely accepted at the time of its discovery, it has been rediscovered (L´opez-Marcos, Sanz-Serna and Skeel, 1996) and has now been seen to have further ramifications.

The final claim that is made for this theory is that it has applications to the analysis of the order of general linear methods. In this guise a richer structure, incorporating an additive as well as a multiplicative operation, needs to be used; the present section also examines this more elaborate algebra.

The primary source for this theory is Butcher (1972), but it is also widely known through the work of Hairer and Wanner (1974). Recently the algebraic structures described here have been rediscovered through applications in theoretical physics. For a review of these developments, see Brouder (2000).

Before proceeding with this programme, we remark that the mappings from trees to real numbers, which appear as members of the algebraic systems introduced in this section, are associated with formal Taylor series of the form

$$
a ( \emptyset ) y ( x ) + \sum _ { t \in T } { \frac { a ( t ) } { \sigma ( t ) } } h ^ { r ( t ) } F ( t ) ( y ( x ) ) .
$$

Such expressions as this were given the name B-series by Hairer and Wanner

(1974) and written

$$
B ( a , y ( x ) ) ,
$$

where $a : T ^ { \# } \to \mathbb { R }$ , with $T ^ { \# }$ denoting the set of rooted trees $T$ together with an additional empty tree $\varnothing$ . Because of the central role of the exact solution series, in which $a ( \emptyset ) = 1$ and $a ( t ) = 1 / \gamma ( t )$ , Hairer and Wanner scale the terms in the series slightly differently, and write

$$
\begin{array} { l l l } { { \displaystyle { \cal B } ( a , y ( x ) ) = a ( \emptyset ) y ( x ) + \sum _ { t \in T } \frac { \alpha ( t ) a ( t ) } { r ( t ) ! } h ^ { r ( t ) } F ( t ) ( y ( x ) ) } } \\ { { \displaystyle ~ = a ( \emptyset ) y ( x ) + \sum _ { t \in T } \frac { a ( t ) } { \gamma ( t ) \sigma ( t ) ! } h ^ { r ( t ) } F ( t ) ( y ( x ) ) , } } \end{array}
$$

where $\alpha ( t )$ is the function introduced in Subsection 302. This means that the B-series representing a Runge–Kutta method with order $p$ will have $a ( t ) = 1$ whenever $r ( t ) \leq p$ . In this book we concentrate on the coefficients themselves, rather than on the series, but it will be the interpretation as coefficients in (380a), and not as coefficients in (380b), that will always be intended.

# 381 Equivalence classes of Runge–Kutta methods

We consider three apparently distinct ways in which two Runge–Kutta methods may be considered equivalent. Our aim will be to define these three equivalence relations and then show that they are actually equivalent equivalence relations. By this we mean that if two methods are equivalent in one of the three senses then they are equivalent also in each of the other senses. We temporarily refer to these three equivalence relations as ‘equivalence’, ‘ $\Phi$ - equivalence’ and $P$ -equivalence’, respectively.

Definition 381A Two Runge–Kutta methods are ‘equivalent’ if, for any initial value problem defined by an autonomous function $f$ satisfying a Lipschitz condition, and an initial value $y _ { 0 }$ , there exists $h _ { 0 } ~ > ~ 0$ such that the result computed by the first method is identical with the result computed by the second method, if $h \leq h _ { 0 }$ .

Definition 381B Two Runge–Kutta methods are $\cdot _ { \Phi }$ -equivalent’ if, for any $t \in T$ , the elementary weight $\Phi ( t )$ corresponding to the first method is equal to $\Phi ( t )$ corresponding to the second method.

In introducing $P$ -equivalence, we need to make use of the concept of reducibility of a method. By this we mean that the method can be replaced by a method with fewer stages formed by eliminating stages that do not contribute in any way to the final result, and combining stages that are essentially the same into a single stage. We now formalize these two types of reducibility.

Definition 381C A Runge–Kutta method $( A , b ^ { \prime } , c )$ is $^ { \small 4 }$ -reducible’ if the stage index set can be partitioned into two subsets $\{ 1 , 2 , \ldots , s \} = P _ { 0 } \cup P _ { 1 }$ such that $b _ { i } = 0$ for all $i \in P _ { 0 }$ and such that $a _ { i j } = 0$ if $i \in P _ { 1 }$ and $j \in \mathcal { P } _ { 0 }$ . The method formed by deleting all stages indexed by members of $P _ { 0 }$ is known as the $^ { \small 4 }$ -reduced method’.

Definition 381D A Runge–Kutta method $( A , b ^ { \prime } , c )$ is $^ { \cdot } P$ -reducible’ if the stage index set can be partitioned into $\{ 1 , 2 , \ldots , s \} = P _ { 1 } \cup P _ { 2 } \cup \ldots \cup P _ { \overline { { s } } }$ and if, for all $I , J = 1 , 2 , \ldots , { \overline { { s } } }$ , $\textstyle \sum _ { j \in P _ { J } } a _ { i j }$ is constant for all $i \in P _ { I }$ . The method $( \overline { { A } } , \overline { { b } } ^ { \intercal } , \overline { { c } } )$ , with $\overline { { s } }$ stages with $\begin{array} { r } { \overline { { a } } _ { I J } = \sum _ { j \in P _ { J } } a _ { i j } } \end{array}$ , for $i \in P _ { I }$ , $\textstyle { \overline { { b } } } _ { I } = \sum _ { i \in P _ { I } } b _ { i }$ and $\overline { { c } } _ { I } = c _ { i }$ , for $i \in P _ { I }$ , is known as the $P$ -reduced method.

Definition 381E A Runge–Kutta method is ‘irreducible’ if it is neither 0-reducible nor $P$ -reducible. The method formed from a method by first carrying out a $P$ -reduction and then carrying out a 0-reduction is said to be the ‘reduced method’.

Definition 381F Two Runge–Kutta methods are $^ { \circ }$ -equivalent’ if each of them reduces to the same reduced method.

Theorem 381G Let $( A , b ^ { \intercal } , c )$ be an irreducible $s$ -stage Runge–Kutta method. Then, for any two stage indices $i , j \in \{ 1 , 2 , \dots , s \}$ , there exists a Lipschitzcontinuous differential equation system such that $Y _ { i } \neq Y _ { j }$ . Furthermore, there exists $t \in T$ , such that $\Phi _ { i } ( t ) \neq \Phi _ { j } ( t )$ .

Proof. If $i , j$ exist such that

$$
\Phi _ { i } ( t ) = \Phi _ { j } ( t ) \quad { \mathrm { f o r ~ a l l ~ } } t \in T ,
$$

then define a partition $P = \{ P _ { 1 } , P _ { 2 } , . . . , P _ { \overline { { s } } } \}$ of $\{ 1 , 2 , \ldots , s \}$ such that $i$ and $j$ are in the same component of the partition if and only if (381a) holds. Let $\mathcal { A }$ denote the algebra of vectors in $\mathbb { R } ^ { s }$ such that, if $i$ and $j$ are in the same component of $P$ , then the $i$ and $j$ components of $v \in { \mathcal { A } }$ are identical. The algebra is closed under vector space operations and under component-bycomponent multiplication. Note that the vector with every component equal to $^ { 1 }$ is also in $\mathcal { A }$ . Let $\hat { \cal A }$ denote the subalgebra generated by the vectors made up from the values of the elementary weights for the stages for all trees. That is, if $t \in T$ , then $v \in \mathbb { R } ^ { s }$ defined by $v _ { i } = \Phi _ { i } ( t )$ , $i = 1 , 2 , \dots , s$ , is in $\hat { \cal A }$ , as are the component-by-component products of the vectors corresponding to any finite set of trees. In particular, by using the empty set, we can regard the vector defined by $v _ { i } = 1$ as also being a member of $\hat { \cal A }$ . Because of the way in which elementary weights are constructed, $v \in \widehat { A }$ implies $A v \in { \widehat { A } }$ . We now show that $\widehat { A } = A$ . Let $I$ and $J$ be two distinct members of $P$ . Then because $t \in T$ exists so that $\Phi _ { i } ( t ) \neq \Phi _ { j } ( t )$ for $i \in I$ and $j \in J$ , we can find $v \in { \mathcal { A } }$ so that $v _ { i } \neq v _ { j }$ . Hence, if $w = ( v _ { i } - v _ { j } ) ^ { - 1 } ( v - v _ { j } 1 )$ , where $1$ in this context represents the vector in $\mathbb { R } ^ { s }$ with every component equal to 1, then $w _ { i } = 1$ and $w _ { j } = 0$ . Form the product of all such members of the algebra for $J \ne I$ and we deduce that the characteristic function of $I$ is a member of $\mathcal { A }$ . Since the $S$ such vectors constitute a basis for this algebra, it follows that $\widehat { A } = A$ . Multiply the characteristic function of $J$ by $A$ and note that, for all $i \in I \in P$ , the corresponding component in the product is the same. This contradicts the assumption that the method is irreducible. Suppose it were possible that two stages, $Y _ { i }$ and $Y _ { j }$ , say, give identical results for any Lipschitz continuous differential equation, provided $h > 0$ is sufficiently small. We now prove the contradictory result that $\Phi _ { i } ( t ) = \Phi _ { j } ( t )$ for all $t \in T$ . If there were a $t \in T$ for which this does not hold, then write $U$ for a finite subset of $T$ containing $t$ as in Subsection 314. Construct the corresponding differential equation as in that subsection and consider a numerical solution using the Runge–Kutta method $( A , b ^ { \prime } , c )$ and suppose that $t$ corresponds to component $k$ of the differential equation. The value of component $k$ of $Y _ { i }$ is $\Phi _ { i } ( t )$ and the value of component $k$ of $Y _ { j }$ is $\Phi _ { j } ( t )$ . 

Now the key result interrelating the three equivalence concepts.

Theorem 381H Two Runge–Kutta methods are equivalent if and only if they are $P$ -equivalent and if and only if they are $\Phi$ -equivalent.

# Proof.

$P$ -equivalence $\Rightarrow$ equivalence. It will enough to prove that if $i , j ~ \in ~ P _ { I }$ , in any $P$ -reducible Runge–Kutta method, where we have used the notation of Definition 381D, then for any initial value problem, as in Definition 381A, $Y _ { i } = Y _ { j }$ , for $h < h _ { 0 }$ . Calculate the stages by iteration starting with $Y _ { i } ^ { \left[ 0 \right] } = \eta$ , for every $i \in \{ 1 , 2 , \ldots , s \}$ . The value of $Y _ { i } ^ { \left[ k \right] }$ in iteration $k$ will be identical for all $i$ in the same partitioned component.

$P$ -equivalence ⇒ Φ-equivalence. Let the stages be partitioned according to $\{ 1 , 2 , \ldots , s \} = P _ { 1 } \cup P _ { 2 } \cup \ldots \cup P _ { \overline { { s } } }$ and assume that a Runge–Kutta method is reducible with respect to this partition. It will be enough to prove that, for all $t \in T$ , $\Phi _ { i } ( t ) = \Phi _ { j } ( t )$ if $i$ and $j$ belong to the same component. This follows by induction on the order of $t$ . It is true for $t = \tau$ because $\Phi _ { i } ( t ) = c _ { i }$ is constant for all $i$ in the same component. For $t = [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ]$ ,

$$
\Phi _ { i } ( [ t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) = \sum _ { j = 1 } ^ { s } a _ { i j } \prod _ { k = 1 } ^ { m } \Phi _ { j } ( t _ { k } )
$$

and this also is constant for all $i$ in the same component.

$\Phi$ -equivalence  P -equivalence. Suppose two methods are $\Phi$ -equivalent but not $P$ -equivalent. Combine the $s$ stages of method 1 and the $\widehat { s }$ stages of method 2, together with the output approximations, into a single method and replace this by a reduced method. Because the original methods are not $P$ - equivalent, the output approximations in the combined method are not in the same partition. Hence, by Theorem 381G, there exists $t \in T$ such that $\Phi _ { i } ( t )$ takes on different values for these two approximations.

$E q u i v a l e n c e \Rightarrow P$ -equivalence. Suppose two methods are equivalent but not $P$ -equivalent. Carry out the same construction as in the immediately previous part of the proof. By Theorem 381G, there is an initial value problem satisfying the requirements of Definition 381A such that $Y _ { i }$ takes on different values for the two output approximations. This contradicts the assumption that the original methods are equivalent. $\sqcup$

# 382 The group of Runge–Kutta methods

Consider two equivalence classes of Runge–Kutta methods and choose a representative member of each of these classes. Because of the results of the previous subsection, equivalence is the same as $\Phi$ -equivalence and the same as $P$ -equivalence. To see how to construct the composition product for the classes, form a tableau

$$
{ \begin{array} { c c c c c c c c c c } { c _ { 1 } } & & & & & & & & & & & & & & \\ { c _ { 2 } } & & { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ & { c _ { 2 } } & & & & & & & & & & \\ { \vdots } & & { \vdots } & & & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ & & & & & & & & & & { c _ { s } } & & { 0 } & { \cdots } & { 0 } \\ & & & & & & & & & & & { \ddots } & { \vdots } \\ & & & & & & & & & & & & { \vdots } \\ { c _ { 3 } } b _ { j } + { \hat { c } } _ { 1 } \ } & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 1 1 } } & { { \hat { a } } _ { 1 2 } } & { \cdots } & { { \hat { a } } _ { 1 s } } \\ { \sum _ { i = 1 } ^ { s } b _ { j } + { \hat { c } } _ { 2 } } & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 2 1 } } & { { \hat { a } } _ { 2 2 } } & { \cdots } & { { \hat { a } } _ { 2 s } } \\ & & & & & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ & & & & & & & { \sum _ { i = 1 } ^ { s } b _ { i } + { \hat { c } } _ { s } \ }  & { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { { \hat { a } } _ { 3 1 } } & { { \hat { a } } _ { 3 2 } } \\ & & & & & & & & { \hat { b } } & { { \hat { b } } _ { 4 3 } } & { \cdots } & { { \hat { b } } _ { 4 3 } } \end{array} 
$$

from the elements of the tableaux for the two methods $( A , b ^ { \iota } , c )$ and $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ , respectively. We have written $s$ and $\widehat { s }$ for the numbers of stages in the first and second method, respectively.

By writing $y _ { 0 }$ for the initial value for the first method and $y _ { 1 }$ for the value computed in a step and then writing $y _ { 2 }$ for the result computed by the second method using $y _ { 1 }$ for its initial value, we see that $y _ { 2 }$ is the result computed by the product method defined by (382a). To see why this is the case, denote the stage values by $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , for the first method and by $\widehat { Y } _ { i }$ , $i = 1 , 2 , \dots , \widehat { s }$ , for the second method. The variables $F _ { i }$ and $\widehat { F } _ { i }$ will denote the values of $f ( Y _ { i } )$ and $f ( \widehat { Y } _ { i } )$ .

The values of the stages and of the final results computed within the first and second steps are

$$
\begin{array} { l } { { Y _ { i } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } , \qquad i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle } } \\ { { y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } F _ { j } , } } \\ { { \displaystyle } } \\ { { \widehat { Y } _ { i } = y _ { 1 } + h \displaystyle \sum _ { j = 1 } ^ { \widehat { s } } \widehat { a } _ { i j } \widehat { F } _ { j } , \qquad i = 1 , 2 , \ldots , \widehat { s } , } } \\ { { \displaystyle } } \\ { { y _ { 2 } = y _ { 1 } + h \displaystyle \sum _ { j = 1 } ^ { \widehat { s } } \widehat { b } _ { j } \widehat { F } _ { j } . } } \end{array}
$$

Substitute $y _ { 1 }$ from (382c) into (382d) and (382e), and we see that the coefficients for the stages in the second step and for the final output value $y _ { 2 }$ are given as in the tableau (382a).

If $m _ { 1 }$ and $m _ { 2 }$ denote the methods $( A , b ^ { \prime } , c )$ and $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ , respectively, write $m _ { 1 } \cdot m _ { 2 }$ for the method defined by (382a). Also, for a given method $m$ , we write $[ m ]$ for the equivalence class containing $m$ . The notation $m \equiv { \overline { { m } } }$ will signify that $m$ and $\overline { { m } }$ are equivalent methods.

We are interested in multiplication of equivalent classes, rather than of particular methods within these classes. Hence, we attempt to use the method given by (382a) as defining a new class of equivalent methods, which we can use as the product of the original two classes. The only possible difficulty could be that the result might depend on the particular choice of representative member for the two original classes. That no such difficulty arises follows from the following theorem:

Theorem 382A Let $m _ { 1 }$ , $_ { I I l 2 }$ , $\overline { { m } } _ { 1 }$ , $\overline { { m } } _ { 2 }$ denote Runge–Kutta methods, such that

$$
m _ { 1 } \equiv \overline { { { m } } } _ { 1 } a n d m _ { 2 } \equiv \overline { { { m } } } _ { 2 } .
$$

Then

$$
[ m _ { 1 } \cdot m _ { 2 } ] = [ { \overline { { m } } } _ { 1 } \cdot { \overline { { m } } } _ { 2 } ] .
$$

Proof. We note that an equivalent statement is

$$
m _ { 1 } \cdot m _ { 2 } \equiv \overline { { { m } } } _ { 1 } \cdot \overline { { { m } } } _ { 2 } .
$$

Let $y _ { 1 }$ and $y _ { 2 }$ denote the output values over the two steps for the sequence of steps constituting $m _ { 1 } \cdot m _ { 2 }$ , and $\overline { { y } } _ { 1 }$ and $\overline { { y } } _ { 2 }$ denote the corresponding output values for ${ \overline { { m } } } _ { 1 } \cdot { \overline { { m } } } _ { 2 }$ . If $f$ satisfies a Lipschitz condition and if $h$ is sufficiently small, then $y _ { 1 } = \overline { { y } } _ { 1 }$ because $m _ { 1 } \equiv \overline { { m } } _ { 1 }$ , and $y _ { 2 } = \overline { { y } } _ { 2 }$ because $m _ { 2 } \equiv \overline { { m } } _ { 2 }$ . Hence, (382g) and therefore (382f) follows. 

Having constructed a multiplicative operation, we now construct an identity element and an inverse for equivalence classes of Runge–Kutta methods. For the identity element we consider the class containing any method $m _ { 0 }$ that maps an initial value to an equal value, for a problem defined by a Lipschitz continuous function, provided that $h$ is sufficiently small. It is clear that $[ { \boldsymbol { m } } _ { 0 } { \boldsymbol { \cdot } } { \boldsymbol { m } } ] = [ { \boldsymbol { m } } { \boldsymbol { \cdot } } { \boldsymbol { m } } _ { 0 } ] = [ { \boldsymbol { m } } ]$ for any Runge–Kutta method $m$ . It will be convenient to denote the identity equivalence class by the symbol 1, where it will be clear from the context that this meaning is intended.

To define the inverse of an equivalence class, start with a particular representative $m = ( A , b ^ { \intercal } , c )$ , with $s$ stages, and consider the tableau

$$
\begin{array} { c } { { c _ { 1 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { c _ { 2 } - \sum _ { j = 1 } ^ { s } b _ { j } } } \\ { { \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \hdots \sum _ { j = 1 } ^ { s } b _ { j } \ \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { 1 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 1 s } - b _ { s } } } \\ { { a _ { 2 1 } - b _ { 1 } } } & { { a _ { 2 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { 2 s } - b _ { s } } } \end{array} \right| } } \\ { { - b _ { 1 } \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots } } \\ { { \hdots \qquad \sum _ { j = 1 } ^ { s } b _ { j } \ \left| \begin{array} { c c c c c } { { a _ { 1 1 } - b _ { 1 } } } & { { a _ { s 2 } - b _ { 2 } } } & { { \cdots } } & { { a _ { s s } - b _ { s } } } \\ { { - b _ { 1 } \qquad - b _ { 2 } } } & { { \cdots } } & { { - b _ { s } } } \end{array} \right| } } \end{array} .
$$

As we saw in Subsection 343, this method exactly undoes the work of $m$ Denote this new method by $m ^ { - 1 }$ , and we prove the following result:

Theorem 382B Let $m$ denote a Runge–Kutta method. Then

$$
[ m \cdot m ^ { - 1 } ] = [ m ^ { - 1 } \cdot m ] = 1 .
$$

Proof. The tableaux for the two composite methods $m \cdot m ^ { - 1 }$ and ${ m ^ { - 1 } } \cdot { m }$ are, respectively,

$$
\begin{array} { r l } & { c _ { 1 } \left| \begin{array} { l l l l l l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right| } \\ & { c _ { s } \left| \begin{array} { l l l l l l l l l } { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } & { \vdots } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { b _ { s } } & { a _ { 1 1 } - b _ { 1 } } & { a _ { 1 2 } - b _ { 2 } } & { \cdots } & { a _ { 1 s } - b _ { s } } \end{array} \right| } \\ & { c _ { 2 } \left| \begin{array} { l l l l l l l l l } { b _ { 1 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { a _ { 2 1 } - b _ { 1 } } & { a _ { 2 2 } - b _ { 2 } } & { \cdots } & { a _ { 2 s } } & { - b _ { s } } \end{array} \right| } \\ & { c _ { 2 } \left| \begin{array} { l l l l l l l l l l } { b _ { 1 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { \vdots } & { 0 } & { \vdots } & { \cdots } & { \vdots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right| } \\ & { c _ { s } \left| \begin{array} { l l l l l l l l l } { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { a _ { s 1 } - b _ { 1 } } & { a _ { s 2 } - b _ { 2 } } & { \cdots } & { a _ { s s } - b _ { s } } & { \cdots } & { b _ { s } } \end{array} \right| } \\ & { b _ { 1 1 } } & { b _ { 2 } \cdots } & { b _ { s } } &  - b _ { 1 } \end{array}
$$

and

$$
 \begin{array} { l }  { \begin{array} { l } { c c c c c c c c c c c c c c } { { } } \\ { { } } \\ { } \\ { { } } \\ { { } } \\ { { } ^ { c _ { 2 } } - \sum _ { j = 1 } ^ { s } b _ { j } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } \sum _ { j = 1 } ^ { s } } \\ { { } } \end{array} } { \left| \begin{array} { l l l l l l l l l l } { a _ { 1 1 } - b _ { 1 } } & { a _ { 1 1 } } & { a _ { 1 2 } - b _ { 2 } } & { \cdots } & { a _ { 1 s } - b _ { s } } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } \vdots } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { a _ { s 1 } - b _ { j } } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } - b _ { 1 } } \end{array} \right| } { \begin{array} { l l l l l l l l l } { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \end{array} }  \begin{array} { l l l l l l l } { { } } & { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\  { } \end{array} \end{array}
$$

Each of these methods is $P$ -reducible to the methods $m$ and $m ^ { - 1 }$ , respectively, but in each case with $b ^ { \top }$ replaced by the zero vector, so that each lies in the equivalence class 1. 

# 383 The Runge–Kutta group

While the group of equivalent classes of Runge–Kutta methods is conceptually very simple, it is difficult to use for detailed manipulations. We turn to a second group that is closely related to it, but which has a more convenient representation.

Let $G _ { 1 }$ denote the set of functions on $T$ , the rooted trees, to the real numbers. We define a binary relation on $G _ { 1 }$ that makes it a group. It is convenient to widen the scope of our discussion by making use of forests. By a ‘forest’, we mean a set of vertices $V$ and a set of edges $E$ such that each edge is an ordered pair of members of $V$ under the restrictions that each vertex appears as the second member of at most one edge. If $[ v _ { 1 } , v _ { 2 } ]$ , $[ v _ { 2 } , v _ { 3 } ]$ , $\cdot \cdot ,$ $[ v _ { n - 1 } , v _ { n } ]$ are edges, we write $v _ { 1 } < v _ { n }$ . We will require this relation to be a partial ordering.

Suppose that $V$ and $E$ can be partitioned as $V ~ = ~ V _ { 1 } \cup V _ { 2 } \cup \dots \cup V _ { k }$ , $E = E _ { 1 } \cup E _ { 2 } \cup \cdot \cdot \cdot \cup E _ { k }$ , where each of $( V _ { i } , E _ { i } )$ , $i = 1 , 2 , \ldots , k$ , is connected and is therefore a rooted tree. A function $\alpha : T  \mathbb { R }$ can be extended multiplicatively to a function on the set of all forests by defining

$$
\alpha { \big ( } ( V , E ) { \big ) } = \prod _ { i = 1 } ^ { k } \alpha { \big ( } ( V _ { i } , E _ { i } ) { \big ) } .
$$

If $( V , E )$ is a forest and $\hat { V }$ is a subset of $V$ , then the sub-forest induced by $\hat { V }$ is the forest $( \widehat { V } , \widehat { E } )$ , where $\widehat { E }$ is the intersection of $\hat { V } \times \hat { V }$ and $E$ . A special

case is when a sub-forest $( \widehat { V } , \widehat { E } )$ satisfies the requirement that for any two vertices $u , v$ of $E$ such that $u < v$ and $v \in \widehat { E }$ , $u$ is also a member of $\widehat { E }$ . In this case we write

$$
( { \widehat { V } } , { \widehat { E } } ) \triangleleft ( V , E ) .
$$

From now on we write forests by single letters $Q$ , $R$ , $S$ , and interpret $R \triangleleft S$ accordingly. If $R \triangleleft S$ then $S \backslash R$ will denote the forest induced by the difference of the vertex sets of $S$ and $R$ , respectively.

We can now define a product of two multiplicative mappings of forests to real numbers. If $\alpha$ and $\beta$ are two such mappings, then we write

$$
( \alpha \beta ) ( S ) = \sum _ { R \diamond S } \alpha ( S \setminus R ) \beta ( R ) .
$$

We need to verify that $\alpha \beta$ is multiplicative if the same is true for $\alpha$ and $\beta$ .

Lemma 383A Let $\alpha$ and $\beta$ be multiplicative mappings from the forests to the real numbers. Then $\alpha \beta$ is multiplicative.

Proof. It will be sufficient to consider the value of $( \alpha \beta ) ( S )$ , where $S = S _ { 1 } \cup S _ { 2 }$ . Each $R \triangleleft S$ can be written as $R = R _ { 1 } \cup R _ { 2 }$ , where $R _ { 1 } \triangleleft S _ { 1 }$ and $R _ { 2 } \triangleleft S _ { 2 }$ . We now have

$$
\begin{array} { l } { { ( \alpha \beta ) ( S ) = \displaystyle \sum _ { R \ll S } \alpha ( S \setminus R ) \beta ( R ) } } \\ { { \ = \displaystyle \sum _ { R _ { 1 } \leqslant S _ { 1 } } \alpha ( S _ { 1 } \setminus R _ { 1 } ) \beta ( R _ { 1 } ) \sum _ { R _ { 2 } \leqslant S _ { 2 } } \alpha ( S _ { 2 } \setminus R _ { 2 } ) \beta ( R _ { 2 } ) } } \\ { { \ = ( \alpha \beta ) ( S _ { 1 } ) ( \alpha \beta ) ( S _ { 2 } ) . } } \end{array}
$$

We next show that the product we have defined is associative.

Lemma 383B Let $\alpha$ , $\beta$ and $\gamma$ be multiplicative mappings from forests to reals. Then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Proof. If $Q \triangleleft R \triangleleft S$ then $( R \setminus Q ) \triangleleft ( S \setminus Q )$ . Hence, we find

$$
\begin{array} { r l } { ( ( \alpha \beta ) \gamma ) ( S ) = \displaystyle \sum _ { Q + \delta } ( \alpha \beta ) ( S \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + S } \sum _ { ( R \backslash Q ) \leqslant ( S \backslash Q ) } \alpha ( ( S \setminus Q ) \setminus ( R \setminus Q ) ) \beta ( R \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + R R \cap Q \leqslant ( S \setminus R ) \beta ( R \setminus Q ) \gamma ( Q ) } } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = ( \alpha ( \beta \gamma ) ) ( S ) . } \end{array}
$$

We can now restrict multiplication to trees, and we note that associativity still remains. The semi-group that has been constructed on the set $G _ { 1 }$ is actually a group because we can construct both left and right inverses, α−1left and $\alpha _ { \mathrm { r i g h t } } ^ { - 1 }$ say, for any $\alpha \in G _ { 1 }$ , which must be equal because

$$
\alpha _ { \mathrm { l e f t } } ^ { - 1 } = \alpha _ { \mathrm { l e f t } } ^ { - 1 } \left( \alpha \alpha _ { \mathrm { r i g h t } } ^ { - 1 } \right) = \left( \alpha _ { \mathrm { l e f t } } ^ { - 1 } \alpha \right) \alpha _ { \mathrm { r i g h t } } ^ { - 1 } = \alpha _ { \mathrm { r i g h t } } ^ { - 1 } .
$$

Lemma 383C Given $\alpha \in G _ { 1 }$ , there exist a left inverse and a right inverse.

Proof. We show, by induction on the order of $t$ , that it is possible to construct $\beta$ such that $( \alpha \beta ) ( t ) = 0$ or $( \beta \alpha ) ( t ) = 0$ , for all $t \in T$ . Because $( \alpha \beta ) ( \tau ) = ( \beta \alpha ) ( \tau ) = \alpha ( \tau ) + \beta ( \tau )$ , the result is clear for order 1. Suppose the result has been proved for all trees of order less than that of $t \neq \tau$ ; then we note that

$$
( \alpha \beta ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \alpha , \beta )
$$

and

$$
( \beta \alpha ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \beta , \alpha ) ,
$$

where $\phi ( t , \alpha , \beta )$ involves the values of $\alpha$ and $\beta$ only for trees with orders less than $r ( t )$ . Hence, it is possible to assign a value to $\beta ( t )$ so that $( \alpha \beta ) ( t ) = 0$ or that $( \beta \alpha ) ( t ) = 0$ , respectively. Thus it is possible to construct $\beta$ as a left inverse or right inverse of $\alpha$ . 

Having established the existence of an inverse for any $\alpha \in G _ { 1 }$ , we find a convenient formula for $\alpha ^ { - 1 }$ . We write $S$ for a tree $t$ , written in the form $( V , E )$ , and ${ \mathcal { P } } ( S )$ for the set of all partitions of $S$ . This means that if $P \in { \mathcal { P } } ( S )$ , then $P$ is a forest formed by possibly removing some of the edges from $E$ . Another way of expressing this is that the components of $P$ are trees $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , where $V$ is the union of $V _ { 1 }$ , $V _ { 2 }$ , $\cdot \cdot \cdot$ , $V _ { n }$ and each $E _ { i }$ is a subset of $E$ . The integer $n$ , denoting the number of components of $P$ , will be written as $\# P$ . We write $t _ { i }$ as the tree represented by $( V _ { i } , E _ { i } )$ .

Lemma 383D Given $\alpha \in G _ { 1 }$ and $t \in T$ , written in the form $( V , E )$ , then

$$
\alpha ^ { - 1 } ( t ) = \sum _ { P \in \mathcal { P } ( S ) } \prod _ { i = 1 } ^ { \# P } ( - \alpha ( t _ { i } ) ) .
$$

Proof. Construct a mapping $\beta \in G _ { 1 }$ equal to the right-hand side of (383b). We show that for any $t \in T$ , $( \alpha \beta ) ( t ) = 0$ so that $\alpha \beta = 1$ . Let $t = ( V , E )$ . For any partition $P$ with components $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , we consider the set of possible combinations of $\{ 1 , 2 , \ldots , n \}$ , with the restriction that if $C$ is such a combination, then no edge $( v _ { 1 } , v _ { 2 } ) \in E$ exists with $v _ { 1 } \in V _ { i }$ and $v _ { 2 } \in V _ { j }$ , with $i$ and $j$ distinct members of $C$ . Let $\mathcal C ( P )$ denote the set of all such combinations of $P \in \mathcal { P } ( t )$ . Given $C \in P$ , denote by $\overline { { C } }$ the complement of $C$ in $P$ .

The value of $( \alpha \beta ) ( t )$ can be written in the form

$$
\sum _ { P \in \mathcal { P } ( t ) } \sum _ { C \in \mathcal { C } ( P ) } \prod _ { i \in C } \alpha ( t _ { i } ) ( - 1 ) ^ { \# \overline { { C } } } \prod _ { j \in \overline { { C } } } \alpha ( t _ { j } ) .
$$

For any particular partition $P$ , the total contribution is

$$
\sum _ { C \in \mathcal { C } ( P ) } ( - 1 ) ^ { n - \# C } \prod _ { i = 1 } ^ { \# P } \alpha ( t _ { i } ) .
$$

This is zero because $\begin{array} { r } { \sum _ { C \in { \mathcal { C } } ( P ) } ( - 1 ) ^ { n - \# C } = 0 } \end{array}$

# 384 A homomorphism between two groups

We show that the groups introduced in Subsections 382 and 383 are related in such a way that the former is isomorphic to a subgroup of the latter. The mapping between elements of the group that provides this homomorphism maps an equivalence class of Runge–Kutta methods to the function on $T$ to $\mathbb { R }$ defined by the elementary weights associated with a representative member of the class. We need to establish that products in the first group are preserved in the second. This means that if $m$ and $\widehat { m }$ are Runge–Kutta methods and $\Phi : T  \mathbb { R }$ and $\widehat \Phi : T  \mathbb { R }$ are the elementary weight functions for $m$ and $\widehat { m }$ , respectively, then $\Phi \widehat \Phi$ is the elementary weight function associated with $m \widehat { m }$ .

Theorem 384A Let $\Phi : T  \mathbb { R }$ be the elementary weight function associated with $( A , b ^ { \prime } , c )$ and $\widehat \Phi : T \to \mathbb { R }$ the elementary weight function associated with $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ . Let $\widetilde { \Phi } : T  \mathbb { R }$ denote the elementary weight function for the product method as represented by (382a). Then

$$
{ \widetilde { \Phi } } = \Phi { \widehat { \Phi } } .
$$

Proof. Denote the $( s + { \widehat { s } } )$ -stage composite coefficient matrices by $( \widetilde { A } , \widetilde { b } ^ { \intercal } , \widetilde { c } )$ with the elements of $\ddot { A }$ and $\widetilde { b } ^ { \intercal }$ given by

$$
\begin{array} { r l } & { \widetilde { a } _ { i j } = \left\{ \begin{array} { l l } { a _ { i j } , } & { i \leq s , j \leq s , } \\ { 0 , } & { i \leq s , j > s , } \\ { b _ { j } , } & { i > s , j \leq s , } \\ { \widehat { a } _ { i - s , j - s } , } & { i > s , j > s . } \end{array} \right. } \\ & { \widetilde { b } _ { i } = \left\{ \begin{array} { l l } { b _ { i } , } & { i \leq s , } \\ { \widehat { b } _ { i - s } , } & { i > s . } \end{array} \right. } \end{array}
$$

For a tree $t$ , such that $r ( t ) = n$ , represented by the vertex–edge pair $( V , E )$ , with root $\rho \in V$ , write the elementary weight $ { \widetilde { \Phi } } ( t )$ in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { i \in I } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

In this expression, $I$ is the set of all mappings from $V$ to the set $\{ 1 , 2 , \ldots , { \widetilde { s } } \}$ and, for $i \in I$ and $v \in V$ , $i ( v )$ denotes the value to which the vertex $v$ maps.

If $v \ < \ w$ and $i ( v ) \leq s < i ( w )$ then the corresponding term in (384a) is zero. Hence, we sum only over $I ^ { \prime }$ defined as the subset of $I$ from which such $i$ are omitted. For any $i \in I ^ { \prime }$ , define $R \triangleleft S = ( V , E )$ such that all the vertices associated with $R$ map into $\{ s + 1 , s + 2 , \ldots , s + \widehat { s } \}$ . Collect together all $i \in I ^ { \prime }$ which share a common $R$ so that (384a) can be written in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { R \leqslant S } \sum _ { i \in I _ { R } } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

For each $R$ , the terms in the sum have total value $\Phi ( S \setminus R ) { \widehat { \Phi } } ( R )$ , and the result follows. $\sqcup$

# 385 A generalization of $G _ { 1 }$

It will be convenient to build an algebraic system similar to $G _ { 1 }$ , but possessing, in addition to the group structure, a vector space structure. We cannot exactly achieve all of this, but we can achieve almost all of it. The way we go about this is to add to $T$ an additional member, known as the ‘empty tree’ and denoted by $\emptyset$ . The augmented set of trees will be denoted by $T ^ { \# }$ . We write $G$ for the set of mappings $T ^ { \# }  \mathbb { R }$ and $G _ { 1 }$ for the set of those members of $G$ for which $\varnothing$ maps to 1. We define the operation $G _ { 1 } \times G \to G$ just as for the group operation except that the coefficient of $\alpha ( t )$ in the formula for $( \alpha \beta ) ( t )$ is $\beta ( \emptyset )$ . With this understanding we retain the associativity property, in cases where it makes sense. That is, if $\alpha , \beta \in G _ { 1 }$ and $\gamma \in G$ , then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Furthermore, left-multiplication by an element of $G _ { 1 }$ is linear in the sense that

$$
\alpha ( \beta + \gamma ) = \alpha \beta + \alpha \gamma ,
$$

whenever $\alpha \in G _ { 1 }$ and $\beta , \gamma \in G$ . Furthermore,

$$
\alpha ( c \beta ) = c \alpha \beta ,
$$

where, for a scalar $c$ , $c \beta$ is the mapping that takes $t$ to $c \beta ( t )$ for all $t \in T ^ { \# }$ .

The generalization we have introduced has a simple significance in terms of Runge–Kutta tableaux and methods. Instead of computing the output value from a step of computation by the formula

$$
y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } ,
$$

where $y _ { 0 }$ is the input value and $F _ { 1 }$ , $F _ { 2 }$ , . . . , $F _ { s }$ are stage derivatives, we can replace (385a) by

$$
b _ { 0 } y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } { \cal F } _ { i } .
$$

To express this in a tableau, we place the coefficient $b _ { 0 }$ in the spare space at the left of the last line. Thus, the tableau would have the form

$$
\begin{array}{c} { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { b _ { 0 } } \end{array} \right| } { a _ { 2 1 } }  & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { { \left| \begin{array} { l l l l l } { \vdots } & { } & { \vdots } & { } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| } } \end{array} 
$$

As a Runge–Kutta method, to be used in the conventional manner as a onestep method for advancing the solution of a differential equation, this makes no sense at all, if $b _ { 0 } \neq 1$ . Indeed, the method would not even be covariant with respect to shifts of origin. However, the process of computing with a single step of this contrived method may play an important role as part of a more sophisticated computation. An important example of a generalized Runge–Kutta method is given by the one-stage tableau

$$
{ \frac { 0 \left| 0 } { 0 \right| 1 } } \ .
$$

This method does nothing other than computing $h$ multiplied by the derivative of the input value. Combined with linear operations, all Runge–Kutta methods can be built up from this basic method. The elementary weights associated with this method are given by

$$
\Phi ( t ) = { \left\{ \begin{array} { l l } { 1 , } & { t = \tau , } \\ { 0 , } & { t \neq \tau . } \end{array} \right. }
$$

# 386 Recursive formula for the product

We consider a formalism for the product on $G _ { 1 } \times G \to G$ , based on the second of the recursive constructions of trees defined in Subsection 300. That is, for

two trees $t$ , $u$ , we define $t u$ as the tree formed by joining the roots of $t$ and $u$ with the root of $t$ regarded as the root of the product. Corresponding to $t \in T ^ { \# }$ , we define $\widehat { t } : G _ { 1 } \to \mathbb { R }$ by the formula

$$
{ \widehat { t } } ( \alpha ) = \alpha ( t ) , \qquad \alpha \in G _ { 1 } .
$$

The set of all $\hat { \boldsymbol { t } }$ , for $t \in T$ , will be denoted by $\widehat { T }$ . We extend the dot-product notation from $T \times T  T$ to ${ \widehat { T } } \times { \widehat { T } }  { \widehat { T } }$ by the formula

$$
\widehat { t } \cdot \widehat { u } = \widehat { t } \widehat { u } .
$$

Since $\widehat { T } ^ { \# }$ denotes a set of linear functionals on $G$ , it is natural to consider also the vector space spanned by such functionals and extend the dot-product notation to make the product of two functionals bilinear. We denote this set of functionals by $G ^ { * }$ .

We can now define a special function, $\lambda : G _ { 1 } \times T \to G ^ { * }$ , by the recursion

$$
\begin{array} { c } { { \lambda ( \alpha , \tau ) = \widehat { \tau } , } } \\ { { \lambda ( \alpha , t u ) = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) . } } \end{array}
$$

This enables us to generate expressions for $\alpha \beta$ for all trees.

Theorem 386A For $\alpha \in G _ { 1 }$ and $\beta \in G$ ,

$$
\begin{array} { l } { { ( \alpha \beta ) ( \emptyset ) = \beta ( \emptyset ) , } } \\ { { ( \alpha \beta ) ( t ) = \lambda ( \alpha , t ) ( \beta ) + \alpha ( t ) \beta ( \emptyset ) . } } \end{array}
$$

Proof. In this proof only, we introduce the notation $R { \dot { < } } S$ to denote $R \triangleleft S$ , with $R \neq \emptyset$ . If a tree $t$ is represented by the set $S$ of vertices, with an implied set of edges, then the notation $t _ { R }$ , where $R \triangleleft S$ , will denote the tree formed from the elements of $R$ , with the induced set of edges. With this terminology, we can write (383a) in the form

$$
( \alpha \beta ) ( t ) = \sum _ { R \doteq S } \alpha ( S \setminus R ) \beta ( R ) + \alpha ( t ) \beta ( \emptyset ) .
$$

Hence, we need to show that

$$
\lambda ( \alpha , t ) = \sum _ { R \mathbin { \dot { \times } } \colon S } \alpha ( S \setminus R ) \widehat { t } _ { R } .
$$

This is obvious in the case $t = \tau$ . We now consider a tree $t u$ with $t$ represented by $S$ and $u$ represented by $Q$ . This means that $t u$ can be represented by the graph $( V , E )$ , where $V$ is the union of the vertex sets associated with $S$ and

The function $\lambda$ for trees of orders 1 to 5   

<table><tr><td>t</td><td></td><td>r(t) λ(α,t)</td><td></td></tr><tr><td>·</td><td>T</td><td>1</td><td></td></tr><tr><td>：</td><td>TT</td><td>2</td><td>T+a（T）</td></tr><tr><td>?</td><td>TT·T</td><td>3</td><td>+2a(T)+a(T)²</td></tr><tr><td>：</td><td>T·TT</td><td>3</td><td>.竹+a(T)T+a(TT)T</td></tr><tr><td>Y</td><td>(TT·T)T</td><td>4</td><td>(T.T)T+3a(T).↑+3a(T)²T+a(T)↑</td></tr><tr><td></td><td>· TT·TT</td><td>4</td><td>T+a(T)T.+a(T).TT+ (a(T)²+a(TT))TT+a(T)a(TT)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT·T)4 T(T.T)+2a(T)T.T+α(T)²TT+α(TT·T)T</td></tr><tr><td></td><td></td><td></td><td>T(T:TT)4 T(T.TT)+α(T)T.T+α(TT)TT+α(T·TT)T</td></tr><tr><td>W</td><td></td><td></td><td>(TT:T)T·T 5 (TT.T)T.T+4a(T)(TT.T)T+6a(T)².T+ 4a(t)+a(T)T</td></tr><tr><td></td><td></td><td></td><td>(TT·T)·TT 5 (TT.T).TT+2α(T)TT.TT+a(T)(TT.T)T+ 2a(T)².↑+(a(T)²+a(TT)).T+</td></tr><tr><td>?</td><td></td><td></td><td>(a(τ)³+2a(T)a(τT))TT+α(τ)²a(TT)T TT·(TT·T) 5 TT.(TT.T)+2a(T)TT.TT+α(T)T(TT.T)+ a(T)².↑+2a(T)².T+</td></tr><tr><td></td><td></td><td></td><td>(a(T)³+α(TT·T))TT+α(T)a(TT·T)T TT·(T.TT） 5 T.(T.TT)+a(T)TT.T+a(T)(T.TT)+ a(TT)TT.↑+a(T)².T+</td></tr><tr><td>V</td><td></td><td></td><td>(a(T)a(TT)+α(T:TT))TT+a(T)a(T·TT)T (T:TT).TT 5 (T.TT).TT+2a(T)TT.T+a(T)².T+ 2a(TT)T.TT+2a(T)a(TT)+α(TT)²↑</td></tr><tr><td></td><td></td><td></td><td>YT·(TT·T)T 5 T.(TT.T)T+3a(T)T(T.T)+3a(T)²TT+ a(T)³TT+a((TT.T)T)T</td></tr><tr><td>丫</td><td></td><td></td><td>T(TT:TT)5 T(TT.T)+a(T)T(TT.T)+α(T)T(T.TT)+</td></tr><tr><td></td><td></td><td></td><td>(a(T)²+α(TT))T.TT+a(T)a(TT)TT+α(TT·TT)T T·T(TT.T） 5 T.T(.T)+2a(T)T(T.TT)+α(T)²T.TT+</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>α(TT·T)TT+α(T(TT·T))T</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>T·T(T·TT) 5 T.T(T.TT)+a(T)T(T.TT)+α(TT)T.TT+</td></tr></table>

$Q$ , and $E$ is the union of the corresponding edge sets together with additional edge connecting the two roots. Temporarily we write $( V , E ) = S Q$ . If $R { \dot { < } } S$ and $P \mathcal { \hat { A } } Q$ then the set of subgraphs related to $S Q$ by the relation $X { \dot { \triangle } } S Q$ are of the form $X = R P$ or of the form $X = R$ . Hence,

Formulae for $( \alpha \beta ) ( t _ { i } )$ up to trees of order 5   

<table><tr><td>ti(αβ)(ti)</td><td>ir(ti)</td><td></td><td></td></tr><tr><td>0</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td>β+α1β0</td></tr><tr><td>2</td><td>2</td><td></td><td>β+α1β1+a2βo</td></tr><tr><td>3</td><td>3</td><td>?</td><td>β+2a1β2+α²β1+α3βo</td></tr><tr><td>4</td><td>3</td><td>…</td><td>β4+α1β+α2β1+a4βo</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>β5 + 3α1β+3a²β+a³β1+α5β0</td></tr><tr><td>6</td><td>4</td><td></td><td>β6+α1β4+α1β+(a²+a2)β+a1a2β1 +a6βo</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>β7 +2α1β4+a²β2+α3β1+α7β0</td></tr><tr><td>8</td><td>4</td><td>：</td><td>β8+a1β4 +a2β2+α4β1 +a8β0</td></tr><tr><td>9</td><td>5</td><td>E</td><td>βg+4a1β5+6a²β+4a³β+a𝑖β1+agβo</td></tr><tr><td>10</td><td>5</td><td></td><td>β10+2α1β6+α1β5 +a²β4+(2a² +α2)β3+ (2α1α2+α²)β+α²α2β1+α10β0</td></tr><tr><td></td><td>115</td><td></td><td>β11 +α1β7+2α1β6+2a²β4+α²β+(a²+α3)β²+</td></tr><tr><td></td><td>125</td><td></td><td>α1α3βi+α11β</td></tr><tr><td></td><td></td><td></td><td>α1α4β1+α12β0</td></tr><tr><td></td><td>135V</td><td></td><td>β13 +2α1β6+2a2β4+α²β+2α1α2β2+α²β1+α13β0</td></tr><tr><td></td><td>145</td><td></td><td>Yβ14+3α1β7+3a²β4+α³β+α5β1+α14/0</td></tr><tr><td>15</td><td>5</td><td></td><td>β15 +α1β8+α1β7+(a²+α2)β4+α1α2β+α6β1+α15β</td></tr><tr><td>165</td><td></td><td></td><td></td></tr><tr><td>17</td><td>5</td><td></td><td>β17 +α1β8+a2β4+α4β2+α8β1+α17β0</td></tr></table>

$$
\begin{array} { r l } { \displaystyle \sum _ { X \mathbin { \vrule d S Q } } \alpha ( S Q \setminus X ) \widehat { t } _ { X } = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P d \setminus P } } \alpha ( S Q \setminus P R ) \widehat { t } _ { P R } + \displaystyle \sum _ { R \mathbin { \vrule d S \widehat { X } } } \alpha ( S Q \setminus R ) \widehat { t } _ { R } } & { } \\ { = \displaystyle \sum _ { P \mathbin { \vrule d Q \setminus P \widehat { t } _ { P } } } \alpha ( Q \setminus P ) \widehat { t } _ { P } \displaystyle \sum _ { R \mathbin { \vrule d S } } \alpha ( S \setminus R ) \widehat { t } _ { R } + \alpha ( ( S \setminus R ) Q ) \displaystyle \sum _ { R \mathbin { \vrule h } } \widehat { t } _ { R } } & { } \\ { = \lambda ( \alpha , t ) \lambda ( \alpha , u ) + \alpha ( u ) \lambda ( \alpha , t ) } & { } \\ { = \lambda ( \alpha , t u ) . } \end{array}
$$

<table><tr><td>ir(ti）</td><td></td><td></td><td>ti(a-1)(ti)</td></tr><tr><td>1</td><td>1</td><td>.</td><td>-α1</td></tr><tr><td>2</td><td>2</td><td></td><td>a²-a2 ：</td></tr><tr><td>3</td><td>3</td><td>Y</td><td>2α1α2 -α² -a3</td></tr><tr><td>4</td><td>3</td><td></td><td>三 2α1α2 -α² -α4</td></tr><tr><td>5</td><td>4</td><td>Y</td><td>3α1α3 -3α2a² +α4 -α5</td></tr><tr><td>6</td><td>4</td><td></td><td>√ a1a3 +α1a4+a²- 3a2a² +a4 -a6</td></tr><tr><td>7</td><td>4</td><td>丫</td><td>2α1α4 +α1α3 -3a²α2 +α𝑖 -α7</td></tr><tr><td>8</td><td>4</td><td></td><td>2α1α4+a²-3a²a2+a4-α8</td></tr><tr><td>9</td><td></td><td>√</td><td>4α1α5 -6a²α3 + 4a²α2 -α𝑖 -α9</td></tr><tr><td>10</td><td>5</td><td></td><td> 2α1a6 +α1a5 +α2a3 -a²α4 - 3a²α3 + 4α1α2 -α− - α10</td></tr><tr><td></td><td></td><td>115</td><td>α1α7 + 2α1α6 +α2α3-2a1α² -α²α3 - 2α²α4+ 4a³α2 -α -α11</td></tr><tr><td></td><td>125</td><td></td><td>4α²α2 -ai -α12</td></tr><tr><td></td><td></td><td>135</td><td>2α1a6+2α2α4-a²ag-2a²α4-3α1α²+4α³α2-a -α13</td></tr><tr><td></td><td>145</td><td></td><td>Y 3α1a7 +α1a5 - 3a²α4 -3a²αg +4a³α2 -α− - α14</td></tr><tr><td></td><td></td><td></td><td>α1a8 +α1α7 +α1a6 +α2α4 - 2α1a² -α²α3 -3a²α4+ 4α²α2 -α -α15</td></tr><tr><td></td><td>165</td><td></td><td>4α²α2 -α -α16</td></tr><tr><td>175</td><td></td><td></td><td>2α1α8 +2a2α4-3a1α² + 4α²α2 -α -α17</td></tr></table>

As examples of the use of the algorithm for evaluating $\lambda$ , and thence values of the product on $G _ { 1 } \times G$ , we find

$$
\begin{array} { r l } & { \quad \quad \lambda ( \alpha , \tau ) = \hat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \tau ) = \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } , } \\ & { \lambda ( \alpha , \tau \tau \cdot \tau ) = ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) \cdot \widehat { \tau } + \alpha ( t ) ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) } \\ & { \quad \quad \quad \quad = \widehat { \tau \tau } \cdot \widehat { \tau } + 2 \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau ) ^ { 2 } \widehat { \tau } , } \\ & { \quad \lambda ( \alpha , \tau \cdot \tau \tau ) = \widehat { \tau } \cdot ( \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau } ) + \alpha ( \tau \tau ) \widehat { \tau } } \\ & { \quad \quad \quad = \widehat { \tau } \cdot \widehat { \tau \tau } + \alpha ( \tau ) \widehat { \tau \tau } + \alpha ( \tau \tau ) \widehat { \tau } . } \end{array}
$$

The values of $\lambda ( \alpha , t )$ are continued in Table 386(I) up to trees of order 5. For convenience, each tree is given in product form as well as in pictorial form.

From (386a)–(386d), we find

$$
\begin{array} { r l } & { \quad ( \alpha \beta ) ( \tau ) = \beta ( \tau ) + \alpha ( \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau ) = \beta ( \tau \tau ) + \alpha ( \tau ) \beta ( \tau ) + \alpha ( \tau \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \tau \cdot \tau ) = \beta ( \tau \tau \cdot \tau ) + 2 \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau ) ^ { 2 } \beta ( \tau ) + \alpha ( \tau \tau \cdot \tau ) \beta ( \emptyset ) , } \\ & { \quad ( \alpha \beta ) ( \tau \cdot \tau \tau ) = \beta ( \tau \cdot \tau \tau ) + \alpha ( \tau ) \beta ( \tau \tau ) + \alpha ( \tau \tau ) \beta ( \tau ) + \alpha ( \tau \cdot \tau \tau ) \beta ( \emptyset ) . } \end{array}
$$

It will be convenient to extend these formulae up to trees of order 5, and we present this in Table 386(II). For convenience, we denote the empty tree by $t _ { 0 }$ and the trees of order 1 to 5 by $t _ { i }$ , $i = 1 , 2 , \dots , 1 7 .$ . We also write $\alpha _ { i }$ and $\beta _ { i }$ for $\alpha ( t _ { i } )$ and $\beta ( t _ { i } )$ , respectively. Note that $\alpha _ { 0 }$ does not appear in this table because it always has the value $\alpha ( \varnothing ) = 1$ .

Because Table 386(II) has reference value, we supplement the information it contains with Table 386(III), which gives the formulae for $( \alpha ^ { - 1 } ) ( t )$ where $r ( t ) \leq 5$ and $\alpha \in G _ { 1 }$ .

# 387 Some special elements of $G$

As we have remarked, $D \in G$ represents the differentiation operation, scaled by the unit stepsize $h$ . If $\xi$ denotes the element in $G _ { 1 }$ corresponding to a generalized Runge–Kutta tableau

$$
{ \frac { c \mid A } { 1 \mid b ^ { \mathsf { T } } } } = { \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \\ { c } \\ { \vdots } \\ { c _ { s } } \\ { 1 } \end{array} } { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| }
$$

then $\xi D$ will correspond to the $s$ -stage tableau

$$
{ \begin{array} { r } { c _ { 1 } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { \sum _ { i = 1 } ^ { s } b _ { i } \ { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } & { 0 } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } & { 0 } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right| } } \end{array} }
$$

The result computed by (387b) is just $h f ( \widehat { y } )$ , where $\widehat { y }$ is the result computed by (387a). With this understanding, we have an alternative means of defining the group element corresponding to each of the stages, as well as the final

result, of a Runge–Kutta method. Denote the members of $G _ { 1 }$ corresponding to the stages $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , of (387a) by $\eta _ { i }$ and the output result by $\xi$ ; then

$$
\begin{array} { l } { { \displaystyle \eta _ { i } = 1 + \sum _ { j = 1 } ^ { s } a _ { i j } \eta _ { j } D , } } \\ { { \displaystyle \xi = 1 + \sum _ { i = 1 } ^ { s } b _ { i } \eta _ { i } D . } } \end{array}
$$

In the case of a generalized method, where $b _ { 0 }$ is the coefficient of $y _ { n - 1 }$ in the formula for $y _ { n }$ , (387c) is replaced by

$$
\xi = b _ { 0 } 1 + \sum _ { i = 1 } ^ { s } b _ { i } \eta _ { i } D ,
$$

where, in this context, $^ { 1 }$ is the group-theoretic identity in $G$ .

In addition to $D$ , it is convenient to introduce an element $E \in G$ , defined by

$$
\begin{array} { l } { \displaystyle E ( \emptyset ) = 1 , } \\ { \displaystyle E ( t ) = \frac { 1 } { \gamma ( t ) } , \qquad t \in T . } \end{array}
$$

This means that $E$ corresponds to the exact solution of the differential equation as represented by the Picard iteration scheme introduced in Section 311. The conditions for order $p$ for the Runge–Kutta method (387a) can now be written in the form

$$
\xi ( t ) = E ( t ) , \qquad r ( t ) \leq p .
$$

Finally, we define a sequence of members of $G$ which correspond to the computation of the Taylor coefficients at the initial point, scaled in terms of powers of $h$ . If $T _ { k }$ corresponds to the method which, on input $y _ { 0 } = y ( x _ { 0 } )$ , computes $h ^ { k } y ^ { ( k ) } ( x _ { 0 } )$ , then we require that

$$
\begin{array} { l } { { T _ { k } ( \emptyset ) = 0 , } } \\ { { T _ { k } ( t ) = \left\{ \begin{array} { l l } { { \alpha ( t ) , } } & { { \quad r ( t ) = k , } } \\ { { 0 , } } & { { \quad r ( t ) \neq k . } } \end{array} \right. } } \end{array}
$$

Obviously, $T _ { 1 } = D$ , but $D ^ { n }$ is not defined for $n \geq 2$ .

We can relate $T _ { 1 }$ , $u _ { 2 } , \ldots .$ with $E$ by writing

$$
E = 1 + \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k ! } } T _ { k } ,
$$

where the result is interpreted as meaning that

$$
E ( t ) = 1 ( t ) + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } T _ { k } ( t ) ,
$$

for any $t \in T$

Since $E$ takes the exact solution to a differential equation through one unit step $h$ , it is natural to ask how we would represent the solution at a general point $\theta h$ advanced from the initial point. We write this as $E ^ { ( \theta ) }$ , and we note that

$$
E ^ { ( \theta ) } ( t ) = \theta ^ { r ( t ) } E ( t ) ,
$$

for all $t \in T$ . We can generalize (387d) in the form

$$
E ^ { ( \theta ) } = 1 + \sum _ { k = 1 } ^ { \infty } \frac { \theta ^ { k } } { k ! } T _ { k } ,
$$

and note that, for $\theta$ an integer $n$ , we have

$$
E ^ { ( n ) } = E ^ { n } .
$$

This property is, to some extent, characteristic of $E$ , and we have:

Theorem 387A If $\alpha \in G _ { 1 }$ such that $\alpha ( \tau ) = 1$ , and $m$ is an integer with $m \not \in \{ 0 , 1 , - 1 \}$ , then $\alpha ^ { ( m ) } = \alpha ^ { m }$ implies that $\alpha = E$ .

Proof. For any tree $t \neq \tau$ , we have $\alpha ^ { ( m ) } ( t ) = r ( t ) ^ { m } \alpha ( t ) + Q _ { 1 }$ and $\alpha ^ { m } ( t ) =$ $m \alpha ( t ) + Q _ { 2 }$ , where $Q _ { 1 }$ and $Q _ { 2 }$ are expressions involving $\alpha ( u )$ for $r ( u ) < r ( t )$ . Suppose that $\alpha ( u )$ has been proved equal to $E ( u )$ for all such trees. Then

$$
\begin{array} { c } { { \alpha ^ { ( m ) } ( t ) = r ( t ) ^ { m } \alpha ( t ) + Q _ { 1 } , } } \\ { { \alpha ^ { m } ( t ) = m \alpha ( t ) + Q _ { 2 } , } } \\ { { E ^ { ( m ) } ( t ) = r ( t ) ^ { m } E ( t ) + Q _ { 1 } , } } \\ { { E ^ { m } ( t ) = m E ( t ) + Q _ { 2 } , } } \end{array}
$$

so that $\alpha ^ { ( m ) } ( t ) = \alpha ^ { m } ( t )$ implies that

$$
( r ( t ) ^ { m } - m ) ( \alpha ( t ) - E ( t ) ) = 0 ,
$$

implying that $\alpha ( t ) ~ = ~ E ( t )$ , because $r ( t ) ^ { m } \neq m$ whenever $r ( t ) ~ > ~ 1$ and $m \not \in \{ 0 , 1 , - 1 \}$ . $\sqcup$

Of the three excluded values of $m$ in Theorem 387A, only $\begin{array} { l } { m ~ = ~ - 1 } \end{array}$ is interesting. Methods for which $\alpha ^ { ( - 1 ) } = \alpha ^ { - 1 }$ have a special property which makes them of potential value as the source of efficient extrapolation

procedures. Consider the solution of an initial value problem over an interval $[ x _ { 0 } , { \overline { { x } } } ]$ using $n$ steps of a Runge–Kutta method with stepsize $h = ( \overline { { x } } - x _ { 0 } ) / n$ . Suppose the computed solution can be expanded in an asymptotic series in $h$ ,

$$
y ( \overline { { x } } ) + \sum _ { i = 1 } ^ { \infty } C _ { i } h ^ { i } .
$$

If the elementary weight function for the method is $\alpha$ , then the method corresponding to $( \alpha ^ { ( - 1 ) } ) ^ { - 1 }$ exactly undoes the work of the method but with $h$ reversed. This means that the asymptotic error expansion for this reversed method would correspond to changing the sign of $h$ in (387e). If $\alpha = ( \alpha ^ { ( - 1 ) } ) ^ { - 1 }$ , this would give exactly the same expansion, so that (387e) is an even function. It then becomes possible to extend the applicability of the method by extrapolation in even powers only.

# 388 Some subgroups and quotient groups

Let $H _ { p }$ denote the linear subspace of $G$ defined by

$$
H _ { p } = \{ \alpha \in G : \alpha ( t ) = 0 , { \mathrm { ~ w h e n e v e r ~ } } r ( t ) \leq p \} .
$$

If $\alpha , \beta \in G$ then $\alpha = \beta + H _ { p }$ will mean that $\alpha - \beta$ is a member of $H _ { p }$ . The subspace is an ideal of $G$ in the sense of the following result:

Theorem 388A Let $\alpha ~ \in ~ G _ { 1 }$ , $\beta \in G _ { 1 }$ , $\gamma \in G$ and $\delta \in G$ be such that $\alpha = \beta + H _ { p }$ and $\gamma = \delta + H _ { p }$ . Then $\alpha \gamma = \beta \delta + H _ { p }$ .

Proof. Two members of $G$ differ by a member of $H _ { p }$ if and only if they take identical values for any $t$ such that $r ( t ) \leq p$ . For any such $t$ , the formula for $( \alpha \gamma ) ( t )$ involves only values of $\alpha ( u )$ and $\gamma ( u )$ for $r ( u ) ~ < ~ r ( t )$ . Hence, $( \alpha \gamma ) ( t ) = ( \beta \delta ) ( t )$ . 

An alternative interpretation of $H _ { p }$ is to use instead $1 + H _ { p } \in G _ { 1 }$ as a subgroup of $G _ { 1 }$ . We have:

Theorem 388B Let $\alpha , \beta \in G _ { 1 }$ ; then

$$
\alpha = \beta + H _ { p }
$$

if and only if

$$
\alpha = \beta ( 1 + H _ { p } ) .
$$

Proof. Both (388a) and (388b) are equivalent to the statement $\alpha ( t ) = \beta ( t )$ for all $t$ such that $r ( t ) \leq p$ . $\sqcup$

Furthermore, we have:

Theorem 388C The subgroup $1 + H _ { p }$ is a normal subgroup of $G _ { 1 }$ .

Proof. Theorem 388B is equally true if (388b) is replaced by $\alpha = ( 1 + H _ { p } ) \beta$ Hence, for any $\beta \in G _ { 1 }$ , $( 1 + H _ { p } ) \beta = \beta ( 1 + H _ { p } )$ . $\boxed { \begin{array} { r l } \end{array} }$

Quotient groups of the form $G _ { 1 } / ( 1 + H _ { p } )$ can be formed, and we consider their significance in the description of numerical methods. Suppose that $m$ and $\overline { { m } }$ are Runge–Kutta methods with corresponding elementary weight functions $\alpha$ and $\overline { \alpha }$ . If $m$ and $\overline { { m } }$ are related by the requirement that for any smooth problem the results computed by these methods in a single step differ by $O ( h ^ { p + 1 } )$ , then this means that $\alpha ( t ) = \overline { { \alpha } } ( t )$ , whenever $r ( t ) \leq p$ . However, this is identical to the statement that

$$
\overline { { \alpha } } \in ( 1 + H _ { p } ) \alpha ,
$$

which means that $\alpha$ and $\overline { \alpha }$ map canonically into the same member of the quotient group $G _ { 1 } / ( 1 + H _ { p } )$ .

Because we also have the ideal $H _ { p }$ at our disposal, this interpretation of equivalent computations modulo $O ( h ^ { p + 1 } )$ can be extended to approximations represented by members of $G$ , and not just of $G _ { 1 }$ .

The $C ( \xi )$ and $D ( \xi )$ conditions can also be represented using subgroups.

Definition 388D $A$ member $\alpha$ of $G _ { 1 }$ is in $C ( \xi )$ if, for any tree $t$ such that $r ( t ) \leq \xi$ , $\alpha ( t ) = \gamma ( t ) ^ { - 1 } \alpha ( \tau ) ^ { r ( t ) }$ and also

$$
\alpha ( [ t t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) = \frac { 1 } { \gamma ( t ) } \alpha ( [ \tau ^ { r ( t ) } t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } ] ) ,
$$

for any $t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { m } \in T$ .

Theorem 388E The set $C ( \xi )$ is a normal subgroup of $G _ { 1 }$

A proof of this result, and of Theorem 388G below, is given in Butcher (1972).

The $D ( \xi )$ condition is also represented by a subset of $G _ { 1 }$ , which is also known to generate a normal subgroup.

Definition 388F A member $\alpha$ of $G _ { 1 }$ is a member of $D ( \xi )$ if

$$
\alpha ( t u ) + \alpha ( u t ) = \alpha ( t ) \alpha ( u ) ,
$$

whenever $t , u \in T$ and $r ( t ) \leq \xi$ .

Theorem 388G The set $D ( \xi )$ is a normal subgroup of $G _ { 1 }$

The importance of these semi-groups is that $E$ is a member of each of them and methods can be constructed which also lie in them. We first prove the following result:

Theorem 388H For any real $\theta$ and positive integer $\xi$ , $E ^ { ( \theta ) } \in C ( \xi )$ and $E ^ { ( \theta ) } \in D ( \xi )$ .

Proof. To show that $E ^ { ( \theta ) } \in C ( \xi )$ , we note that $E ^ { ( \theta ) } ( t ) = \gamma ( t ) ^ { - 1 } \theta ^ { r ( t ) }$ and that if $E ^ { ( \theta ) }$ is substituted for $\alpha$ in (388c), then both sides are equal to

$$
\frac { \theta ^ { r ( t ) + r ( t _ { 1 } ) + \cdots + r ( t _ { m } ) + 1 } } { ( r ( t ) + r ( t _ { 1 } ) + \cdots + r ( t _ { m } ) + 1 ) \gamma ( t ) \gamma ( t _ { 1 } ) \cdots \gamma ( t _ { m } ) } .
$$

To prove that $E ^ { ( \theta ) } \in D ( \xi )$ , substitute $E$ into (388d). We find

$$
\frac { r ( t ) } { ( r ( t ) + r ( u ) ) \gamma ( t ) \gamma ( u ) } + \frac { r ( u ) } { ( r ( t ) + r ( u ) ) \gamma ( t ) \gamma ( u ) } = \frac { 1 } { \gamma ( t ) } \cdot \frac { 1 } { \gamma ( u ) } .
$$

# 389 An algebraic interpretation of effective order

The concept of conjugacy in group theory provides an algebraic interpretation of effective order. Two members of a group, $x$ and $z$ , are conjugate if there exists a member $y$ of the group such that $y x y ^ { - 1 } = z$ . We consider the group $G _ { 1 } / ( 1 + H _ { p } )$ whose members are cosets of $G _ { 1 }$ corresponding to sets of Runge– Kutta methods, which give identical numerical results in a single step to within $O ( h ^ { p + 1 } ) .$ In particular, $E ( 1 + H _ { p } )$ is the coset corresponding to methods which reproduce the exact solution to within $O ( h ^ { p + 1 } )$ . This means that a method, with corresponding group element $\alpha$ , is of order $p$ if

$$
\alpha \in E ( 1 + H _ { p } ) .
$$

If a second method with corresponding group element $\beta$ exists so that the conjugacy relation

$$
\beta \alpha \beta ^ { - 1 } \in E ( 1 + H _ { p } )
$$

holds, then the method corresponding to $\alpha$ has effective order $p$ and the method corresponding to $\beta$ has the role of perturbing method.

We use this interpretation to find conditions for effective orders up to 5. To simplify the calculation, we use a minor result:

Lemma 389A A Runge–Kutta method with corresponding group element $\alpha$ has effective order $p$ if and only if (389a) holds, where $\beta$ is such that $\beta ( \tau ) = 0$ .

Proof. Suppose that (389a) holds with $\beta$ replaced by $\widehat { \beta }$ . Let $\beta = E ^ { ( - \widehat { \beta } ( \tau ) ) } \widehat { \beta }$ , so that $\beta ( \tau ) = 0$ . We then find

$$
\begin{array} { r l } & { \beta \alpha \beta ^ { - 1 } = E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \alpha \left( E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \right) ^ { - 1 } } \\ & { \qquad = E ^ { - \widehat { \beta } ( \tau ) } \widehat { \beta } \alpha \widehat { \beta } ^ { - 1 } E ^ { \widehat { \beta } ( \tau ) } } \\ & { \qquad \in E ^ { - \widehat { \beta } ( \tau ) } E E ^ { \widehat { \beta } ( \tau ) } ( 1 + H _ { p } ) } \\ & { \qquad = E ( 1 + H _ { p } ) . } \end{array}
$$

Once we have found effective order conditions on $\alpha$ and found a corresponding choice of $\beta$ for $\alpha$ satisfying these conditions, we can use Lemma 389A in reverse to construct a family of possible perturbing methods.

To obtain the conditions we need on $\alpha$ we have constructed Table 389(I) based on Table 386(II). In this table, the trees up to order 5 are numbered, just as in the earlier table, and $\beta \alpha \beta ^ { - 1 } \in E ( 1 + H _ { p } )$ is replaced by $\beta \alpha \in E \beta ( 1 + H _ { p } )$ , for convenience. In the order conditions formed from Table 389(I), we regard $\beta _ { 2 }$ , $\beta _ { 3 }$ , . . . as free parameters. Simplifications are achieved by substituting values of $\alpha _ { 1 }$ , $\alpha _ { 2 } , \ldots ,$ as they are found, into later equations that make use of them. The order conditions are

$$
\begin{array} { r l } & { \mathrm { ~ G _ { 1 } ~ - } } \\ & { \mathrm { ~ G _ { 2 } ~ - } } \\ & { \mathrm { ~ G _ { 3 } ~ - } } \\ & { \mathrm { ~ C _ { 4 } ~ - } } \\ & { \mathrm { ~ C _ { 4 } ~ - } } \\ & { \mathrm { ~ C _ { 5 } ~ - } } \\ & { \mathrm { ~ C _ { 6 } ~ - } } \\ & { \mathrm { ~ C _ { 7 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 8 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ & { \mathrm { ~ C _ { 9 } ~ - } } \\ &  \mathrm  ~ C \end{array}
$$

For explicit Runge–Kutta methods with fourth (effective) order, four stages are still necessary, but there is much more freedom than for methods with the same classical order. For fifth effective order there is a real saving in that only five stages are necessary. For the fourth order case, we need to choose the coefficients of the method so that

$$
\begin{array} { l } { \alpha _ { 1 } = 1 , } \\ { \alpha _ { 2 } = \frac { 1 } { 2 } , } \\ { \alpha _ { 4 } = \frac { 1 } { 6 } , } \\ { \alpha _ { 8 } = \frac { 1 } { 2 4 } } \end{array}
$$

Effective order conditions   

<table><tr><td></td><td></td><td>ir(ti) (βa)(ti)</td><td>(Eβ)(ti)</td></tr><tr><td>1</td><td>1</td><td>α1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>α+β</td><td>β+</td></tr><tr><td>3</td><td>3</td><td>α3+β</td><td>β+2β+1</td></tr><tr><td>4</td><td>3</td><td>α4 + βα1+ β4</td><td>β4+β+</td></tr><tr><td>5</td><td>4</td><td>α5+β5</td><td>β5 +3β+3β+</td></tr><tr><td>6</td><td>4</td><td>α6+β2α2+ β6</td><td>β6+β+β+β+</td></tr><tr><td>7</td><td>4</td><td>α7+βα1+β7</td><td>β7+2β4+β+12</td></tr><tr><td>8</td><td>4</td><td>α8+βα2+β4α1+β8</td><td>β8+β+β+</td></tr><tr><td>9</td><td>5</td><td>αg+β</td><td>βg+4β5+6β+4β2+½</td></tr><tr><td>10</td><td>5</td><td>α10 + β2α3+ β10</td><td>β10+2β6+β5+β4+β+2β2+10</td></tr><tr><td>11</td><td>5</td><td>α11 + βα2 + β11</td><td>β11+β7+2β6+2β4+β3+β+15</td></tr><tr><td>12</td><td>5</td><td>α12+β2α3+β4α2+ β12</td><td>β12+β8+β6+β4+β+β+30</td></tr><tr><td>13</td><td>5</td><td>α13+2β2α4+β²α1+ β13</td><td>β13+2β6+β4+β+β+20</td></tr><tr><td>14</td><td>5</td><td>α14 + β5α1+ β14</td><td>β14+3β7+3β4+β+20</td></tr><tr><td>15</td><td>5</td><td>α15 +β2α4++β6α1+ β15</td><td>β15+β8+β+β+β+0</td></tr><tr><td>16</td><td>5</td><td>α16+ βα2+ β7α1+β16</td><td>β16+2β8+β4+β+</td></tr><tr><td>17</td><td></td><td></td><td>α17+β2α4+β4a2+β8α1+β17 β17+β8+1β4+β²+ 120</td></tr></table>

and so that the equation formed by eliminating the various $\beta$ values from the equations for $\alpha _ { 3 }$ , $\alpha _ { 5 }$ , $\alpha _ { 6 }$ an $\alpha _ { 7 }$ is satisfied. This final effective order condition is

$$
\begin{array} { r } { \alpha _ { 3 } - \alpha _ { 5 } + 2 \alpha _ { 6 } - \alpha _ { 7 } = \frac { 1 } { 4 } , } \end{array}
$$

and the five condition equations written in terms of the coefficients in a fourstage method are

$$
\begin{array} { c } { { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } } \\ { { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac 1 2 , } } \\ { { b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } a _ { 4 2 } c _ { 2 } + b _ { 4 } a _ { 4 3 } c _ { 3 } = \frac 1 6 , } } \\ { { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \frac 1 { 2 4 } , } } \\ { { b _ { 2 } c _ { 2 } ^ { 2 } ( 1 - c _ { 2 } ) + b _ { 3 } c _ { 3 } ^ { 2 } ( 1 - c _ { 3 } ) + b _ { 4 } c _ { 4 } ^ { 2 } ( 1 - c _ { 4 } ) } } \\ { { + b _ { 3 } a _ { 3 2 } c _ { 2 } ( 2 c _ { 3 } - c _ { 2 } ) + b _ { 4 } a _ { 4 2 } c _ { 2 } ( 2 c _ { 4 } - c _ { 2 } ) + b _ { 4 } a _ { 4 3 } c _ { 3 } ( 2 c _ { 4 } - c _ { 3 } ) } } \end{array}
$$

Group elements associated with a special effective order 4 method   

<table><tr><td>t</td><td></td><td></td><td>E(t）α(t)β(t)(β-1E)(t)(β-1Eβ())(t)</td><td></td></tr><tr><td>·</td><td>1</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>：</td><td>1</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>?</td><td>N</td><td>1 0</td><td>1</td><td>1</td></tr><tr><td>…</td><td></td><td>1 1</td><td>1</td><td>11+r3 72</td></tr><tr><td>Y</td><td>4</td><td>4 1</td><td>1</td><td>26+r4</td></tr><tr><td>?</td><td></td><td>108</td><td></td><td>108</td></tr><tr><td></td><td>1</td><td>品</td><td>1 13</td><td>26+3r³+r4</td></tr><tr><td>丫 i</td><td></td><td>1</td><td>216 108 1 19</td><td>216 19+6r3-r4</td></tr></table>

We do not attempt to find a general solution to these equations, but instead explore a mild deviation from full classical order. In fact, we assume that the perturbing method has $\beta _ { 2 } = \beta _ { 3 } = 0$ , so that we now have the conditions

$$
\begin{array} { r l r } & { } & { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ & { } & { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac { 1 } { 2 } , } \\ & { } & { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } = \frac { 1 } { 3 } , } \\ & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } a _ { 4 2 } c _ { 2 } + b _ { 4 } a _ { 4 3 } c _ { 3 } = \frac { 1 } { 6 } , } \\ & { } & { b _ { 2 } c _ { 2 } ^ { 3 } + b _ { 3 } c _ { 3 } ^ { 3 } + b _ { 4 } c _ { 4 } ^ { 3 } = \frac { 1 } { 4 } , } \\ & { } & { b _ { 3 } a _ { 3 2 } c _ { 2 } ( 2 c _ { 3 } - c _ { 2 } ) + b _ { 4 } a _ { 4 2 } c _ { 2 } ( 2 c _ { 4 } - c _ { 2 } ) + b _ { 4 } a _ { 4 3 } c _ { 3 } ( 2 c _ { 4 } - c _ { 3 } ) = \frac { 1 } { 4 } , } \\ & { } & { b _ { 4 } a _ { 4 3 } a _ { 3 2 } c _ { 2 } = \frac { 1 } { 2 4 } . } \end{array}
$$

Methods satisfying these more general conditions do not need to have $c _ { 4 } = 1$ and we can find, for example, the tableau

$$
\begin{array}{c} \begin{array} { r } { { \left. \begin{array} { l } { 0 } \\ { \frac { 1 } { 3 } } \\ { \frac { 2 } { 3 } } \\ { \frac { 5 } { 6 } } \end{array} \right| } \ \frac { 1 } { 6 } \quad { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 1 0 } } \quad { \frac { 5 } { 2 4 } } \quad { 0 } \quad { \frac { 5 } { 8 } } } \end{array} \ . \qquad \end{array}
$$

A suitable starting method, which does not advance the solution forward but introduces the correct perturbation so that (389b) faithfully reproduces this perturbation to within order 4, is given by the tableau

$$
\begin{array} { r }  { \left. \begin{array} { c } { 0 } \\ { 1 } \\ { \frac { 2 } { 3 } } \\ { \frac { 1 } { 3 } } \\ { - \frac { 1 } { 2 4 } \end{array}  } _ { \begin{array} { c } { 1 } \\ { \frac { 2 } { 3 } } \\ { - \frac { 1 } { 3 } } \end{array} } \qquad \begin{array} { c } { 2 } \\ { \frac { 2 } { 3 } } \\ { \frac { 1 } { 8 } } \end{array} \qquad . } \end{\right|array} \end{array}
$$

The freedom that lay at our disposal in selecting this starting procedure was used to guarantee a certain simplicity in the choice of finishing procedure. This was in fact decided on first, and has a tableau identical with (389b) except for the $b ^ { \prime }$ vector. The reason for this choice is that no extra work is required to obtain an output value because the stages in the final step will already have been completed. The tableau for this final step is

$$
\begin{array} { r } { { \left. \begin{array} { l } { 0 } \\ { \frac { 1 } { 3 } } \\ { \frac { 2 } { 3 } } \\ { \frac { 5 } { 6 } } \end{array} \right| } _ { \frac { 5 } { 2 4 } } { \left. \begin{array} { l l l l } { 1 } & { } & { } & { } \\ { \frac { 1 } { 3 } } & { } & { } & { } \\ { \frac { 1 } { 6 } } & { \frac { 1 } { 2 } } & { } & { } \\ { \frac { 5 } { 2 4 } } & { 0 } & { \frac { 5 } { 8 } } \\ { \frac { 3 } { 2 0 } } & { \frac { 1 } { 3 } } & { \frac { 1 } { 4 } } & { \frac { 4 } { 1 5 } } \end{array} \right. } . } \end{array}
$$

This example method has not been optimized in any way, and is therefore not proposed for a practical computation. On the other hand, it shows that the search for efficient methods need not be restricted to the class of Runge– Kutta methods satisfying classical order conditions. It might be argued that methods with only effective order cannot be used in practice because stepsize change is not possible without carrying out a finishing step followed by a new start with the modified stepsize. However, if, after carrying out a step with the method introduced here, a stepsize change from $h$ to $r h$ is required, then this can be done by simply adding one additional stage and choosing the vector $b ^ { \top }$ which depends on $r$ . The tableau for this $h$ -adjusting step is

<table><tr><td></td><td colspan="5"></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>5</td><td></td></tr><tr><td></td><td>1</td><td>1</td><td>4</td><td></td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td></tr><tr><td>3+r3-2r4 20</td><td>2-3r3+4r4 6</td><td>1-3r3+2r4 4</td><td>4+3r3-r4 r3-r4 15</td></tr></table>

Rather than carry out detailed derivations of the various tableaux we have introduced, we present in Table 389(II) the values of the group elements in $G _ { 1 } / ( 1 + H _ { 4 } )$ that arise in the computations. These group elements are $\beta$ , corresponding to the starting method (389c), $\alpha$ for the main method (389b), $\beta ^ { - 1 } E$ corresponding to the finishing method (389d) and, finally, $\beta ^ { - 1 } E \beta ^ { ( r ) }$ for the stepsize-adjusting method (389e). For convenience in checking the computations, $E$ is also provided.

# Exercises 38

38.1 Find the B-series for the Euler method

$$
{ \frac { 0 \ \biggr \vert \ 0 } { \biggl \vert \ 1 } } \ .
$$

38.2 Find the B-series for the implicit Euler method

$$
{ \frac { 1 \left| 1 \right| } { 1 } } \ .
$$

38.3 Show that the two Runge–Kutta methods

$$
{ \begin{array} { r l r l r l r l r l } { 0 } & { 0 } & & { 0 } & & { } & & { 0 } \\ { 1 } & { 1 } & { - 1 } & & { 1 } & & { } & & { 1 } \\ { \frac { 1 } { 2 } } & { 1 } & { 1 } & { - 1 } & { } & & { } & & { 0 } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } & { \frac { 1 } { 4 } } & { } & & { } & & { } \end{array} } \qquad { \begin{array} { r l r l r l } { 0 } & { { } } & { 0 } & { { } } & { 1 } & { } & { 0 } & { } \\ { 1 } & { { } } & { { } } & { 0 } & { { } } & { { \frac { 1 } { 4 } } } & { } \\ { 2 } & { { } } & { 0 } & { - 2 } & { } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { { } } & { 1 } & { } & { { } } \end{array} }
$$

are P-equivalent. Find a method with only two stages equivalent to each of them.

38.4 Let $m _ { 1 }$ and $m _ { 2 }$ denote the Runge–Kutta methods

$$
\begin{array} { c }  { { \frac { 1 } { 2 } - \frac { 1 } { 6 } \sqrt { 3 } \left| \begin{array} { c c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \frac { 1 } { 6 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \frac { 1 } { 4 } } } \end{array} \right| \begin{array} { c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 6 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \frac { 1 } { 4 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \frac { 1 } { 4 } } } \end{array} , } } \\ { { { \frac { 1 } { 2 } } } } &  { { \frac { 1 } { 6 } } } \\ { { m _ { 2 } = \underbrace { - \frac { 1 } { 2 } + \frac { 1 } { 6 } \sqrt { 3 } } } } & { { \left| \begin{array} { c c } { { \ - \frac { 1 } { 4 } } } & { { \ - \frac { 1 } { 4 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \ - \frac { 1 } { 4 } + \frac { 1 } { 6 } \sqrt { 3 } } } & { { \ - \frac { 1 } { 4 } } } \end{array} \right| \begin{array} { c } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 6 } - \frac { 1 } { 6 } \sqrt { 3 } } } \\ { { \ - \frac { 1 } { 2 } } } & { { \ - \frac { 1 } { 2 } } } \end{array} . } } \end{array}
$$

Show that $[ m _ { 2 } ] = [ m _ { 1 } ] ^ { - 1 }$ .

38.5 Show that $D \in X$ is the homomorphic partner of $[ m ]$ , where

$$
m = { \frac { 0 } { 0 } } \left| { \begin{array} { l } { 0 } \\ { 1 } \end{array} } \right. .
$$

# 39 Implementation Issues

# 390 Introduction

In this section we consider several issues arising in the design and construction of practical algorithms for the solution of initial value problems based on Runge–Kutta methods.

An automatic code needs to be able to choose an initial stepsize and then adjust the stepsize from step to step as the integration progresses. Along with the need to choose appropriate stepsizes to obtain an acceptable accuracy in a given step, there is a corresponding need to reject some steps, because they will evidently contribute too large an error to the overall inaccuracy of the final result. The user of the software needs to have some way of indicating a preference between cheap, but low accuracy, results on the one hand and expensive, but accurate, results on the other. This is usually done by supplying a ‘tolerance’ as a parameter. We show that this tolerance can be interpreted as a Lagrange multiplier $T$ . If $E$ is a measure of the total error to plan for, and $W$ is a measure of the work that is to be allocated to achieve this accuracy, then we might try as best we can to minimize $E + T W$ . This will mean that a high value of $T$ will correspond to an emphasis on reducing computing costs, and a low value of $T$ will correspond to an emphasis on accuracy. It is possible to achieve something like an optimal value of this weighted objective function by requiring the local truncation error to be maintained as constant from step to step. However, there are other views as to how the allocation of resources should be appropriately allocated, and we discuss these in Subsection 393.

If the local truncation error committed in a step is to be the main determining criterion for the choice of stepsize, then we need a means of estimating the local error. This will lead to a control system for the stepsize, and we need to look at the dynamics of this system to ensure that good behaviour is achieved.

It is very difficult to find suitable criteria for adjusting order amongst a range of alternative Runge–Kutta methods. Generally, software designers are happy to construct fixed order codes. However, it is possible to obtain useful variable order algorithms if the stage order is sufficiently high. This applies especially to implicit methods, intended for stiff problems, and we devote at least some attention to this question.

For stiff problems, the solution of the algebraic equations inherent to the implementation of implicit methods is a major issue. The efficiency of a stiff solver will often depend on the management of the linear algebra, associated with a Newton type of solution, more than on any other aspect of the calculation.

# 391 Optimal sequences

Consider an integration over an interval $[ a , b ]$ . We can interpret $a$ as the point $x _ { 0 }$ at which initial information $y ( x _ { 0 } ) = y _ { 0 }$ is given and $b$ as a final point, which we have generally written as $\overline { { x } }$ where we are attempting to approximate $y ( { \overline { { x } } } )$ . As steps of a Runge–Kutta method are carried out we need to choose $h$ for a new step starting at a point $x \in [ a , b ]$ , assuming previous steps have taken the solution forward to this point. From information gleaned from details of the computation, it will be possible to obtain some sort of guide as to what the truncation error is likely to do in a step from $x$ to $x + h$ and, assuming that the method has order $p$ , the norm of this truncation error will be approximately like $C ( \boldsymbol { x } ) h ^ { p + 1 }$ , where $C$ is some positively valued function. Write the choice of $h$ for this step as $H ( x )$ . Assuming that all stepsizes are sufficiently small, we can write the overall error approximately as an integral

$$
E ( H ) = \int _ { a } ^ { b } C ( x ) H ( x ) ^ { p } d x .
$$

The total work carried out will be taken to be the simply the number of steps. For classical Runge–Kutta methods the cost of carrying out each step will be approximately the same from step to step. However, the number of steps is approximately equal to the integral

$$
W ( H ) = \int _ { a } ^ { b } H ( x ) ^ { - 1 } d x .
$$

To obtain an optimal rule for defining values of $H ( x )$ , as $x$ varies, we have to ensure that it is not possible, by altering $H$ , to obtain, at the same time, lower values of both $E ( H )$ and $W ( H )$ . This means that the optimal choice is the same as would be obtained by minimizing $E ( H )$ , for a specified upper bound on $W ( H )$ , or, dually, minimizing $W ( H )$ , subject to an upper bound on $E ( H )$ . Thus we need to optimize the value of $E ( H ) + T W ( H )$ for some positive value of the Lagrange multiplier $T$ .

From calculus of variation arguments, the optimal is achieved by setting to zero the expression $( d / d H ) ( E ( H ) + T W ( H ) )$ . Assuming that $W ( H )$ has the constant value $p$ , chosen for convenience, this means that

$$
p C ( x ) H ( x ) ^ { p - 1 } = p T H ( x ) ^ { - 2 } ,
$$

for all $x$ . Hence, $C ( x ) H ( x ) ^ { p + 1 }$ should be kept equal to the constant value $T$ . In other words, optimality is achieved by keeping the magnitude of the local truncation error close to constant from step to step. In practice, the truncation error associated with a step about to be carried out is not known. However, an estimation of the error in the last completed step is usually available, using techniques such as those described in Section 33, and this can be taken as a usable guide. On the other hand, if a previous attempt to carry out this step has been rejected, because the truncation error was regarded as excessive, then this gives information about the correct value of $h$ to use in a second attempt.

For robustness, a stepsize controller has to respond as smoothly as possible to (real or apparent) abrupt changes in behaviour. This means that the stepsize should not decrease or increase from one step to the next by an excessive ratio. Also, if the user-specified tolerance, given as a bound on the norm of the local truncation error estimate, is ever exceeded, recomputation and loss of performance will result. Hence, to guard against this as much as possible, a ‘safety factor’ is usually introduced into the computation. If $h$ is the estimated stepsize to give a predicted truncation error equal to the tolerance, then some smaller value, such as $0 . 9 h$ , is typically used instead. Combining all these ideas, we can give a formula for arriving at a factor $r$ , to give a new stepsize $r h$ , following a step for which the error estimate is est. The tolerance is written as tol, and it is assumed that this previous step has been accepted. The ratio $r$ is given by

$$
r = \operatorname* { m a x } { \left( 0 . 5 , \operatorname* { m i n } { \left( 2 . 0 , 0 . 9 { \left( \frac { \mathrm { t o l } } { \mathrm { e s t } } \right) } ^ { 1 / ( p + 1 ) } \right) } \right) } .
$$

The three constants, given here with values 0.5, 2.0 and 0.9, are all somewhat arbitrary and have to be regarded as design parameters.

# 392 Acceptance and rejection of steps

It is customary to test the error estimate in a step against $T$ and to accept the step only when the estimated error is smaller. To reduce the danger of rejecting too many steps, the safety factor in (391a) is inserted. Thus there would have to be a very large increase in the rate of error production for a step to be rejected. We now consider a different way of looking at the question of acceptance and rejection of steps. This is based on removing the safety factor but allowing for the possible acceptance of a step as long as the ratio of the error to the tolerance is not too great. We need to decide what ‘too great’ should mean.

The criterion will be based on attempting to minimize the rate of error production plus $T$ times the rate of doing work. Because we are considering the rejection of a completed step with size $h$ , we need to add the work already carried out to the computational costs in some way. Suppose that the error estimated for the step is $r ^ { - ( p + 1 ) } T$ , and that we are proposing to change the stepsize to $r h$ . This will mean that, until some other change is made, the rate of growth of error $+ \textit { T } \times$ work will be $T ( 1 + p ) / r h$ . By the time the original interval of size $h$ has been traversed, the total expenditure will be $T ( 1 + p ) / r h$ . Add the contribution from the work in the rejected step and the total expenditure will be $T ( ( p + 1 ) / r + p )$ .

If, instead, the step had been accepted, the expenditure (linear combination of error and work) would be $T ( r ^ { - ( p + 1 ) } + p )$ . Comparing the two results, we conclude that the step should be accepted if $r ^ { - ( p + 1 ) } \leq ( p + 1 ) / r$ , that is, when

Minimal value of stepsize ratio and maximal value of error/ $T$ for step acceptance   

<table><tr><td>p (p+1)-1/p</td><td>(p +1)(𝑝+1)/p</td></tr><tr><td>1</td><td>0.500 4.00</td></tr><tr><td>2 0.577</td><td>5.20</td></tr><tr><td>3</td><td>0.630 6.35</td></tr><tr><td>4 0.669</td><td>7.48</td></tr><tr><td>5 0.700</td><td>8.59</td></tr><tr><td>6 0.723</td><td>9.68</td></tr><tr><td>7 0.743</td><td>10.77</td></tr><tr><td>8 0.760</td><td>11.84</td></tr><tr><td>9 0.774</td><td>12.92</td></tr><tr><td>10 0.787</td><td>13.98</td></tr></table>

$$
r \geq ( p + 1 ) ^ { - 1 / p } ,
$$

and rejected otherwise. Looked at another way, the step should be accepted if the error estimated in a step, divided by the tolerance, does not exceed $( p + 1 ) ^ { ( p + 1 ) / p }$ . Values of $( p + 1 ) ^ { - 1 / p }$ and $( p + 1 ) ^ { ( p + 1 ) / p }$ are given in Table 392(I).

# 393 Error per step versus error per unit step

The criterion we have described for stepsize selection is based on the principle of ‘error per step’. That is, a code designed on this basis attempts to maintain the error committed in each step as close to constant as possible. An alternative point of view is to use ‘error per unit step’, in which error divided by stepsize is maintained approximately constant. This idea is attractive from many points of view. In particular, it keeps the rate of error production under control and is very natural to use. In an application, the user has to choose a tolerance which indicates how rapidly he or she is happy to accept errors to grow as the solution approximation evolves with time.

Furthermore, there is a reasonable expectation that, if a problem is attempted with a range of tolerances, the total truncation error will vary in more or less the same ratio as the tolerances. This state of affairs is known as ‘proportionality’, and is widely regarded as being desirable. On the other hand, if the error per step criterion is used we should hope only for the global errors to vary in proportion to $\mathrm { t o l } ^ { p / ( p + 1 ) }$ . The present author does not regard this as being in any way inferior to simple proportionality. The fact that error per step is close to producing optimal stepsize sequences, in the sense we have described, seems to be a reason for considering, and even preferring, this choice in practical codes.

From the user point of view, the interpretation of the tolerance as a Lagrange multiplier is not such a difficult idea, especially if tol is viewed not so much as ‘error per step’ as ‘rate of error production per unit of work’. This interpretation also carries over for algorithms for which $p$ is still constant, but the work might vary, for some reason, from one step to the next.

# 394 Control-theoretic considerations

Controlling the stepsize, using a ratio of $h$ in one step to $h$ in the previous step, based on (391a), can often lead to undesirable behaviour. This can come about because of over-corrections. An error estimate in one step may be accidentally low and this can lead to a greater increase in stepsize than is justified by the estimate found in the following step. The consequent rejection of this second step, and its re-evaluation with a reduced stepsize, can be the start of a series of similarly disruptive and wasteful increases and decreases.

In an attempt to understand this phenomenon and to guard against its damaging effects, an analysis of stepsize management using the principles of control theory was instituted by Gustafsson, Lundh and S¨oderlind (1988). The basic idea that has come out of these analyses is that PI control should be used in preference to I control. Although these concepts are related to continuous control models, they have a discrete interpretation. Under the discrete analogue, I control corresponds to basing each new stepsize on the most recently available error estimate, whereas PI control would make use of the estimates found in the two most recently completed steps.

If we were to base a new stepsize on a simplified alternative to (391a), using the ratio $r = ( \mathrm { e s t / t o l } ) ^ { 1 / ( p + 1 ) }$ , this would correspond to what is known in control theory as ‘dead-beat’ control. On the other hand, using the ratio $r = ( \mathrm { t o l } / \mathrm { e s t } ) ^ { \alpha / ( p + 1 ) }$ , where $0 < \alpha < 1$ , would correspond to a damped version of this control system. This controller would not respond as rapidly to varying accuracy requirements, but would be less likely to change too quickly for future behaviour to deal with. Going further, and adopting PI control, would give a stepsize ratio equal to

$$
r _ { n } = \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 1 } } } \right) ^ { \alpha / ( p + 1 ) } \left( { \frac { \mathrm { t o l } } { \mathrm { e s t } _ { n - 2 } } } \right) ^ { \beta / ( p + 1 ) } .
$$

In this equation, $r _ { n }$ is the stepsize ratio for determining the stepsize $h _ { n }$ to be used in step $n$ . That is, if $h _ { n - 1 }$ is the stepsize in step $n - 1$ , then $h _ { n } = r _ { n } h _ { n - 1 }$ . The quantities $\mathrm { e s t } _ { n - 1 }$ and $\mathrm { e s t } _ { n - 2 }$ , denote the error estimates found in steps $n - 1$ and $n - 2$ , respectively.

For convenience, we work additively, rather than multiplicatively, by dealing with $\log ( h _ { n } )$ and $\log ( r _ { n } )$ rather than with $h _ { n }$ and $r _ { n }$ themselves. Let $\xi _ { n - 1 }$ denote the logarithm of the stepsize that would be adopted in step $n$ , if deadbeat control were to be used. That is,

$$
\xi _ { n - 1 } = \log ( h _ { n - 1 } ) + \frac { 1 } { p + 1 } ( \log ( \mathrm { t o l } ) - \log ( \mathrm { e s t } _ { n - 1 } ) ) .
$$

Now let $\eta _ { n }$ denote the logarithm of the stepsize actually adopted in step $n$ . Thus we can write dead-beat control as

$$
\eta _ { n } = \xi _ { n - 1 }
$$

and the modification with damping factor $\alpha$ as

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } + \alpha \xi _ { n - 1 } .
$$

For the PI controller (394a), we have

$$
\eta _ { n } = ( 1 - \alpha ) \eta _ { n - 1 } - \beta \eta _ { n - 2 } + \alpha \xi _ { n - 1 } + \beta \xi _ { n - 2 } .
$$

Appropriate choices for the parameters $\alpha$ and $\beta$ have been discussed by the original authors. Crucial considerations are the stable behaviour of the homogeneous part of the difference equation (394b) and the ability of the control system to respond sympathetically, but not too sensitively, to changing circumstances. For example, $\alpha = 0 . 7$ and $\beta = - 0 . 4$ , as proposed by Gustafsson (1991), works well. Recently, further work has been done on control-theoretic approaches to stepsize control by S¨oderlind (2002).

# 395 Solving the implicit equations

For stiff problems, the methods of choice are implicit. We discuss some aspects of the technical problem of evaluating the stages of an implicit Runge–Kutta method. For a one-stage method, the evaluation technique is also similar for backward difference methods and for Runge–Kutta and general linear methods that have a lower triangular coefficient matrix.

For these simple methods, the algebraic question takes the form

$$
Y - h \gamma f ( X , Y ) = U ,
$$

where $X$ and $U$ are known. Let $J ( X , Y )$ denote the Jacobian matrix with elements given by

$$
J ( X , Y ) _ { i j } = \frac { \partial f _ { i } } { \partial y _ { j } } ( X , Y ) , \qquad i , j , = 1 , 2 , \ldots , N .
$$

A full Newton scheme would start with the use of a predictor to obtain a first approximation to $Y$ . Denote this by $Y ^ { \left[ 0 \right] }$ and update it with a sequence of approximations $Y ^ { \left\lfloor i \right\rfloor }$ , $i = 1 , 2 , \dots$ , given by

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \Delta ,
$$

where

$$
( I - h \gamma J ( X , Y ^ { [ i - 1 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U .
$$

Although the full scheme has the advantage of quadratic convergence, it is usually not adopted in practice. The reason is the excessive cost of evaluating the Jacobian $J$ and of carrying out the LU factorization of the matrix $I - h \gamma J$ . The Newton scheme can be modified in various ways to reduce this cost. First, the re-evaluation of $J$ after each iteration can be dispensed with. Instead the scheme (395b) can be replaced by

$$
( I - h \gamma J ( X , Y ^ { [ 0 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U ,
$$

and for many problems this is almost as effective as the full Newton method. Even if more iterations are required, the additional cost is often less than the saving in $J$ evaluations and LU factorizations.

Secondly, in the case of diagonally implicit methods, it is usually possible to evaluate $J$ only once per step, for example at the start of the first stage. Assuming the Jacobian is sufficiently slowly varying, this can be almost as effective as evaluating the Jacobian once for each stage.

The third, and most extreme, of the Jacobian update schemes is the use of the same approximation over not just one step but over many steps. A typical algorithm signals the need to re-evaluate $J$ only when the rate of convergence is sufficiently slow as to justify this expenditure of resources to achieve an overall improvement. When $J$ is maintained at a constant value over many steps, we have to ask the further question about when $I \mathrm { ~ - ~ } h \gamma J$ should be refactorized. Assuming that $\gamma$ is unchanged, any change in $h$ will affect the convergence by using a factorization of this matrix which is based not only on an incorrect value of $J$ , but on what may be a vastly different value of $h$ .

It may be possible to delay the refactorization process by introducing a ‘relaxation factor’ into the iteration scheme. That is, when $\Delta$ has been computed in a generalized form of (395b), the update takes the form

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \theta \Delta ,
$$

where $\theta$ is a suitably chosen scalar factor. To analyse how this works, suppose for simplicity that $J$ is constant but that $h$ has changed from $\overline { { h } }$ at the time the factorization took place to $r { \bar { h } }$ at the time a generalized Newton step is being carried out. As a further simplification, assume that $f ( x , y ) = J y + V$ and that we are exploring the behaviour in a direction along along an eigenvector corresponding to an eigenvalue $\lambda$ . Write $z = \overline { { h } } \gamma \lambda$ . Under these assumptions the iteration scheme effectively seeks a solution to an equation of the form

$$
\eta - r z \eta = a ,
$$

with solution $\eta = \eta ^ { * } = a / ( 1 - r )$ , using an iteration scheme which replaces $\eta ^ { * } + \epsilon$ by $\eta ^ { * } + \phi ( z ) \epsilon$ , where

$$
\phi ( z ) = 1 - \theta \frac { 1 - r z } { 1 - z } .
$$

Convergence will depend on the magnitude of $\phi ( z )$ for all $z$ that are likely to arise. Values of $z$ near zero correspond to non-stiff components of the problem, and values of $z$ with large magnitude in the left half-plane correspond to stiff components. Hence, it seems desirable to choose $\theta$ to minimize $| \phi ( z ) |$ for $z$ in the left half-plane. The value that achieves this is

$$
\theta = { \frac { 2 } { 1 + r } } .
$$

For fully implicit Runge–Kutta methods, the problem of evaluating the stages becomes much more complicated and potentially more costly. For a method with coefficient matrix $A$ , we need to consider all stages at the same time. Let $Y$ denote the $s N$ -dimensional vector made up from $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ . Furthermore the approximation sequence will be written as $Y ^ { \left[ j \right] }$ , $j = 0 , 1 , \ldots$ , each also made up from $s$ subvectors, and $\Delta$ will denote a vector in $\mathbb { R } ^ { s N }$ made up from the subtrahends in each of the $s$ components in iteration $i$ . Thus

$$
\begin{array} { r } { Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad Y ^ { [ i ] } = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i ] } } \end{array} \right] , \quad \Delta = \left[ \begin{array} { c } { \Delta _ { 1 } } \\ { \Delta _ { 2 } } \\ { \vdots } \\ { \Delta _ { s } } \end{array} \right] = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i - 1 ] } - Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i - 1 ] } - Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i - 1 ] } - Y _ { s } ^ { [ i ] } } \end{array} \right] . } \end{array}
$$

In place of (395a), the algebraic equations to solve in a step take the form

$$
Y - h A \otimes f ( X , Y ) = U \in \mathbb { R } ^ { s N } .
$$

Note that $f ( X , Y )$ denotes a vector in $\mathbb { R } ^ { s N }$ made up from subvectors of the form $f ( X _ { j } , Y _ { j } )$ , $j = 1 , 2 , \dots , s$ . The iteration scheme consists of solving the equations

$$
\Delta _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } J \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) \Delta _ { k } = Y _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } f \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) - U _ { i } ,
$$

and then carrying out the update $Y _ { j } ^ { [ i ] } = Y _ { j } ^ { [ i - 1 ] } - \Delta _ { j }$ , $j = 1 , 2 , \dots , s$ . If it is assumed that Jacobians are evaluated only once per step, or even less frequently, then we can write (395c) in the simplified form

$$
( I _ { s } \otimes I _ { N } - h A \otimes J ) \Delta = Y ^ { [ i - 1 ] } - h A \otimes F ^ { [ i - 1 ] } - U ,
$$

where $F ^ { [ i - 1 ] }$ is the vector with $k$ th subvector equal to $f \big ( X _ { k } , Y _ { k } ^ { \lfloor i - 1 \rfloor } \big )$ . Here $J$ is a single approximation to the $n \times n$ Jacobian matrix. One of the advantages of using a single $J$ approximation is the fact that it is possible to operate, for example, with similarity transformations, on the coefficient matrix $A$ and $J$ independently.

If no such transformation is carried out, the computational costs can become very severe. The LU factorization of the matrix on the left-hand side of (395d) requires a number of operations proportional to $s ^ { 3 } N ^ { 3 }$ , compared with just $N ^ { 3 }$ if $s = 1$ . However, if $A = T ^ { - 1 } \widehat { A } T$ , where $\widehat { A }$ has a structure close to diagonal, then the cost reduces to something like $s N ^ { 3 }$ .

# Exercises 39

39.1 An implicit Runge–Kutta method is to be implemented for the solution of non-stiff problems using functional iteration to solve the nonlinear equations. How should the stepsize be selected?

39.2 A Runge–Kutta method of order $p$ is used over an interval of length $X$ . Suppose that for a subinterval of length $( 1 - \theta ) X$ the error in a step of length $h$ is $C h ^ { p + 1 }$ , and for the remaining distance $\theta X$ the error is $\alpha C h ^ { 5 }$ . Assume that a large number $N$ of steps are performed, of which $( 1 - \phi ) N$ are in the first subinterval and $\phi N$ are in the second subinterval. Determine the value of $\phi$ which will minimize the total error committed in the integration.

39.3 Compare the result found in Exercise 39.2 with the result that would be obtained from an ‘error per unit step’ argument.

# Chapter 4

# Linear Multistep Methods

# 40 Preliminaries

# 400 Fundamentals

This chapter, devoted entirely to the analysis of linear multistep methods, follows on from the introduction to these methods presented in Section 24. We use the notation and ideas introduced there, but attempt to fill in missing details. In particular, we show in the present section how the concepts of consistency, stability and convergence are interrelated and give more of a theoretical justification for the concept of ‘order’. This analysis depends heavily on the use of difference equations, especially on the conditions for the solution of a linear difference equation to be bounded. For a difference equation,

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } ,
$$

we recall that all solutions are bounded if and only if the polynomial

$$
z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k }
$$

has all its zeros in the closed unit disc and all multiple zeros in the interior of this disc.

The direct applicability of this result to a linear multistep method $[ \alpha , \beta ]$ , in which the approximate solution at $x _ { n }$ is computed by

$$
\begin{array} { r l } & { y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ & { \qquad + \beta _ { 0 } h f ( x _ { n } , y _ { n } ) + \beta _ { 1 } h f ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + \beta _ { k } h f ( x _ { n - k } , y _ { n - k } ) , } \end{array}
$$

is clear. We wish to be able to solve a wide variety of initial value problems in a reliable manner, and amongst the problems for which we need good answers is certainly the simple problem for which $f ( x , y ) = 0$ . In this case the solution approximations are related by (400a), and stable behaviour for this problem becomes essential. It is a remarkable fact that convergence hinges on this stability result alone, as well as on consistency requirements.

As in Section 24 we write the method as $[ \alpha , \beta ]$ , where

$$
\begin{array} { l } { \alpha ( z ) = 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } z ^ { k } , } \\ { \beta ( z ) = \beta _ { 0 } + \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { k } z ^ { k } , } \end{array}
$$

or in the more traditional formulation as $( \rho , \sigma )$ , where

$$
\begin{array} { l } { \rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } , } \\ { \quad } \\ { \sigma ( z ) = \beta _ { 0 } z ^ { k } + \beta _ { 1 } z ^ { k - 1 } + \beta _ { 2 } z ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } . } \end{array}
$$

# 401 Starting methods

As we pointed out in Subsection 246, linear multistep methods require starting methods even to carry out a single step. We consider, in general terms, some of the procedures used to obtain starting values; we then discuss any unifying characteristics they might have.

One obvious approach to starting a $k$ -step method is to carry out $k - 1$ steps with a Runge–Kutta method, preferably of the same order as the linear multistep method itself. An interesting variation of this standard procedure is to use specially constructed Runge–Kutta methods which make it possible to move forward several steps at a time (Gear, 1980).

A second approach, which fits naturally into the style of linear multistep methods, is to solve a system of equations representing the integrals of $y ^ { \prime } ( x )$ from $x _ { 0 }$ to each of $x _ { 1 }$ , $x _ { 2 }$ , . . . , $x _ { k - 1 }$ written, in each case, as a quadrature formula with abscissae at these same points. We illustrate this in the case of the third order Adams–Bashforth method

$$
y _ { n } = y _ { n - 1 } + { \frac { h } { 1 2 } } { \bigl ( } 2 3 f ( x _ { n - 1 } , y _ { n - 1 } ) - 1 6 f ( x _ { n - 2 } , y _ { n - 2 } ) + 5 f ( x _ { n - 3 } , y _ { n - 3 } ) { \bigr ) } ,
$$

for which appropriate quadrature formulae, adapted to a differential equation, are

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + \displaystyle \frac { h } { 1 2 } \big ( 5 f ( x _ { 0 } , y _ { 0 } ) + 8 f ( x _ { 1 } , y _ { 1 } ) - f ( x _ { 2 } , y _ { 2 } ) \big ) , } } \\  { \big \} _ { 2 } = y _ { 0 } + \displaystyle \frac { h } { 3 } \big ( f ( x _ { 0 } , y _ { 0 } ) + 4 f ( x _ { 1 } , y _ { 1 } ) + f ( x _ { 2 } , y _ { 2 } ) \big ) . } \end{array}
$$

These equations are solved by functional iteration to yield approximations $y _ { 1 } \approx y ( x _ { 1 } )$ and $y _ { 2 } \approx y ( x _ { 2 } )$ .

In modern variable order codes, it is usual to start with order 1 or order 2, and to adapt to higher orders when this becomes possible and when it becomes advantageous from an efficiency point of view. This means that order $k$ may be reached after many steps with varying stepsize.

The common feature of these approaches to starting a linear multistep method is that each is, in reality, a Runge–Kutta method possessing multiple outputs, to furnish approximations at a number of equally spaced points. For example, the iteration scheme given by (401a) and (401b) can be represented by the Runge–Kutta scheme

<table><tr><td>：</td><td>0</td><td>0 0</td></tr><tr><td></td><td>中</td><td>1 12</td></tr><tr><td></td><td>G</td><td></td></tr><tr><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td></tr><tr><td rowspan="3"></td><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>中立</td></tr></table>

in which the two output approximations are for $y _ { 1 }$ and $y _ { 2 }$ , respectively. This scheme, like any starting procedure of Runge–Kutta type, has a property we assume for starting schemes used for the definition of convergence. This is that the quantities computed as approximations to $y _ { i }$ , $i = 1 , 2 , \ldots , k - 1$ , all converge to $y ( x _ { 0 } )$ as $h  0$ .

# 402 Convergence

We consider the approximation of $y ( { \overline { { x } } } )$ by a linear multistep method, with $h = ( \overline { { x } } - x _ { 0 } ) / m$ , using initial values

$$
\begin{array} { l } { { y _ { 0 } } = \phi _ { 0 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { y _ { 1 } } = \phi _ { 1 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { \mathrm { ~ } } } \\ { { \vdots \qquad \vdots } } \\ { { y _ { k - 1 } } = \phi _ { k - 1 } { \left( y ( { x _ { 0 } } ) , h \right) } . } \end{array}
$$

After the initial values have been evaluated, the values of $y _ { n }$ , for $n =$ $k , k + 1 , \ldots , m$ , are found in turn, using the linear $k$ -step method $[ \alpha , \beta ]$ . It is assumed that for $i = 1 , 2 , \ldots , k - 1$ ,

$$
\left\| \phi _ { i } \left( y ( x _ { 0 } ) , h \right) - y ( x _ { 0 } ) \right\| \to 0 , \quad { \mathrm { ~ a s ~ } } h \to 0 .
$$

Definition 402A Consider a linear multistep method used with a starting method as described in the previous discussion. Let $Y _ { m }$ denote the approximation to $y ( { \overline { { x } } } )$ found using $_ { T I l }$ steps with $h = ( \overline { { x } } - x _ { 0 } ) / m$ . The function $f$ is assumed to be continuous and to satisfy a Lipschitz condition in its second variable. The linear multistep method is said to be ‘convergent’ if, for any such initial value problem,

$$
\| Y _ { m } - y ( { \overline { { x } } } ) \| \to 0 , \ a s \ m \to \infty .
$$

# 403 Stability

For a general initial value problem, the computed solution satisfies

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } + h \sum _ { i = 0 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ) .
$$

However, for the one-dimensional problem for which $f ( x , y ) = 0$ , we have the simpler difference equation

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } .
$$

Definition 403A A linear multistep method $\lfloor \alpha , \beta \rfloor$ is ‘stable’ if the difference equation (403a) has only bounded solutions.

Because stability concepts of one sort or another abound in the theory of initial value problems, ‘stability’ is often referred to as ‘zero-stability’ $^ -$ for example, in Lambert (1991)) $-$ or as ‘stability in the sense of Dahlquist’.

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

# 405 Necessity of conditions for convergence

We formally prove that stability and consistency are necessary for convergence. Note that the proofs are based on the same simple problems that were introduced in Subsections 403 and 404.

Theorem 405A A convergent linear multistep method is stable.

Proof. If the method were not stable, there would exist an unbounded sequence $\eta$ satisfying the difference equation

$$
\eta _ { n } = \alpha _ { 1 } \eta _ { n - 1 } + \alpha _ { 2 } \eta _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } \eta _ { n - k } .
$$

Define the sequence $\zeta$ by

$$
\zeta _ { n } = \operatorname* { m a x } _ { i = 0 } ^ { n } | \eta _ { i } | ,
$$

so that $\zeta$ converges monotonically to $\infty$ . Consider the solution of the initial value problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 0 ,
$$

with $\overline { { x } } = 1$ . Assuming that $n$ steps are to be performed, we use a stepsize $h = 1 / n$ and initial values $y _ { i } = \eta _ { i } / \zeta _ { n }$ , for $i = 0 , 1 , \ldots , k - 1$ . The condition that $y _ { i } \to 0$ for $0 \leq i \leq k - 1$ is satisfied because $\zeta _ { n }  \infty$ . The approximation computed for $y ( { \overline { { x } } } )$ is equal to $\eta _ { n } / \zeta _ { n }$ . Because the $\zeta$ sequence is unbounded, there will be an infinite number of values of $n$ for which $\left| \zeta _ { n } \right|$ is greater than the greatest magnitude amongst previous members of this sequence. For such values of $n$ , $| \eta _ { n } / \zeta _ { n } | ~ = ~ 1$ , and therefore the sequence $n \mapsto \eta _ { n } / \zeta _ { n }$ cannot converge to $0$ . 

Theorem 405B A convergent linear multistep method is preconsistent.

Proof. By Theorem 405A, we can assume that the method is stable. Let $\eta$ be defined as the solution to the difference equation

$$
\eta _ { n } = \alpha _ { 1 } \eta _ { n - 1 } + \alpha _ { 2 } \eta _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } \eta _ { n - k } ,
$$

with initial values $\eta _ { 0 } = \eta _ { 1 } = \cdot \cdot \cdot = \eta _ { k - 1 } = 1$ . The computed solution of the problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 1 , \qquad { \overline { { x } } } = 1 ,
$$

using $n$ steps, is equal to $y _ { n } = \eta _ { n }$ . Since this converges to $^ { 1 }$ as $n  \infty$ , it follows that, for any $\epsilon > 0$ , there exists an $n$ sufficiently large so that $| y _ { i } - 1 | \le \epsilon$

for $i = n - k$ , $n - k + 1$ , $\cdot \cdot \cdot$ , $n$ . Hence,

$$
\begin{array} { l } { \displaystyle { \left| 1 - \alpha _ { 1 } - \alpha _ { 2 } - \cdots \cdots - \alpha _ { k } \right| \leq \left| \eta _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \eta _ { n - i } \right| + \left( 1 + \sum _ { i = 1 } ^ { k } | \alpha _ { i } | \right) \epsilon } } \\ { \displaystyle { \qquad = \left( 1 + \sum _ { i = 1 } ^ { k } | \alpha _ { i } | \right) \epsilon } . } \end{array}
$$

Because this can be arbitrarily small, it follows that

$$
1 - \alpha _ { 1 } - \alpha _ { 2 } - \cdot \cdot \cdot - \alpha _ { k } = 0 .
$$

Theorem 405C A convergent linear multistep is consistent.

Proof. We note first that

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } \neq 0 ,
$$

since, if the expression were zero, the method would not be stable. Define the sequence $\eta$ by

$$
\eta _ { i } = \frac { \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } } { \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } } i , \qquad i = 0 , 1 , 2 , \ldots .
$$

Consider the numerical solution of the initial value problem

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( 0 ) = 0 ,
$$

with the output computed at $\overline { { x } } = 1$ , and with $n$ steps computed with stepsize $h = 1 / n$ . Choose starting approximations as

$$
y _ { i } = \frac { 1 } { n } \eta _ { i } ,
$$

for $i = 0 , 1 , 2 , \ldots , k - 1$ , so that these values converge to zero as $n \longrightarrow \infty$ . We verify that the computed solution for all values of $i = 0 , 1 , 2 , \ldots , n$ is given also by (405a), and it follows that the approximation at $x = 1$ is

$$
{ \frac { \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } } { \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } } } ,
$$

independent of $n$ . Because convergence implies that the limit of this is $^ { 1 }$ , it follows that

$$
\beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } = \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } .
$$

Given that a linear multistep is stable and consistent, we prove that it is convergent. We assume that the differential equation under consideration has the autonomous form

$$
y ^ { \prime } ( x ) = f ( y ( x ) )
$$

and that $f$ satisfies a Lipschitz condition with constant $L$ . These assumptions can be weakened in various ways with no change to the final result, but with considerable complication to the details. If the Lipschitz condition holds only locally, then it becomes necessary to restrict the stepsize so that it is possible to guarantee that all approximations which enter into the discussion are sufficiently close to the exact trajectory for the condition to apply. If the problem is not autonomous, so that $f ( y )$ is replaced by $f ( x , y )$ , then it is possible to allow $f$ to be Lipschitz continuous in the $y$ variable, but merely continuous in $x$ .

However, we now press ahead with consideration of the possible convergence of the solution to (406a), together with the initial information given at $x _ { 0 }$ and the requirement that the approximate solution is to be evaluated at $\scriptstyle { \overline { { x } } }$ . We always assume that $\overline { { x } } > x _ { 0 }$ , to avoid the inconvenience of having to allow for negative stepsizes.

For the rest of this subsection, it will be assumed, without further comment, that the differential equation we are attempting to solve is (406a) and that the solution is to be approximated on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ with initial value information given at $x _ { 0 }$ . The stepsize $h$ will always be positive, and the Lipschitz condition holds with constant $L$ . We refer to the problem as ‘the standard initial value problem’. One further notation we use throughout is to write $M$ for a bound on $\left\| f ( y ( x ) ) \right\|$ for $x \in [ x _ { 0 } , { \overline { { x } } } ]$ . Such a bound clearly exists because

$$
\| f ( y ( x ) ) - f ( y ( x _ { 0 } ) ) \| \leq L \| y ( x ) - y ( x _ { 0 } ) \| ,
$$

and the latter quantity is bounded.

As a first step towards understanding the relationship between an approximation to $y ( { \overline { { x } } } )$ and the exact value of this quantity, we consider a quantity which measures the error generated in a single step.

Definition 406A Let $[ \alpha , \beta ]$ be a consistent linear multistep method. The ‘local truncation error’ associated with a differentiable function $_ y$ at a point $x$ with stepsize $h$ is the value of

$$
\mathcal { L } ( y , x , h ) = y ( x ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x - i h ) - h \sum _ { i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x - i h ) .
$$

We estimate the value of ${ \mathcal { L } } ( y , x , h )$ when $y$ is the exact solution to (406a), and where not only $x$ but also each $x - h i$ , for $i = 1 , 2 , \ldots , k$ , lies in the interval $[ x _ { 0 } , { \overline { { x } } } ]$ .

Lemma 406B If $y$ is the exact solution to the standard initial value problem and $x \in [ x _ { 0 } + k h , \overline { { x } } ]$ , then

$$
\| \mathcal { L } ( y , x , h ) \| \leq \sum _ { i = 1 } ^ { k } \left( \frac { 1 } { 2 } i ^ { 2 } | \alpha _ { i } | + i | i \alpha _ { i } - \beta _ { i } | \right) L M h ^ { 2 } .
$$

Proof. We first estimate $y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x )$ using the identity

$$
y ( x ) - y ( x - i h ) - h i y ^ { \prime } ( x ) = h \int _ { - i } ^ { 0 } \left( f ( y ( x + h \xi ) ) - f ( y ( x ) ) \right) d \xi ,
$$

so that

$$
\| y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) \| \leq h L \int _ { - i } ^ { 0 } \| y ( x + h \xi ) - y ( x ) \| d \xi ,
$$

and noting, that for $\xi \le 0$ ,

$$
\| y ( x + h \xi ) - y ( x ) \| \leq h \int _ { \xi } ^ { 0 } \| f ( x + h \overline { { \xi } } ) \| d \overline { { \xi } } \leq h | \xi | M ,
$$

so that

$$
\begin{array} { r } { \| y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) \| \leq \frac { 1 } { 2 } i ^ { 2 } h ^ { 2 } L M . } \end{array}
$$

From (406b), we see also that

$$
\| f ( y ( x ) ) - f ( y ( x - i h ) ) \| \leq i h L M .
$$

Because of the consistency of the method, we have $\textstyle \sum _ { i = 1 } ^ { k } \alpha _ { i } \ = \ 1$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { k } ( i \alpha _ { i } - \beta _ { i } ) = \beta _ { 0 } } \end{array}$ . We now write ${ \mathcal { L } } ( y , x , h )$ in the form

$$
\begin{array} { l } { \displaystyle \mathcal { L } ( y , x , h ) = \sum _ { i = 1 } ^ { k } \alpha _ { i } ( y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) ) } \\ { \displaystyle + h \sum _ { i = 1 } ^ { k } ( i \alpha _ { i } - \beta _ { i } ) ( y ^ { \prime } ( x ) - y ^ { \prime } ( x - i h ) ) ; } \end{array}
$$

this is bounded by

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { k } i ^ { 2 } | \alpha _ { i } | L M h ^ { 2 } + \sum _ { i = 1 } ^ { k } i | i \alpha _ { i } - \beta _ { i } | L M h ^ { 2 }
$$

and the result follows.

Theorem 406C Let $\epsilon _ { n }$ denote the vector

$$
\epsilon _ { n } = y ( x _ { n } ) - y _ { n } .
$$

Then for $h _ { 0 }$ sufficiently small so that $h _ { 0 } | \beta _ { 0 } | L < 1$ and $h < h _ { 0 }$ , there exist constants $C$ and $D$ such that

$$
\left\| \epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } \right\| \leq C h \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| + D h ^ { 2 } .
$$

Proof. The value of $\begin{array} { r } { \epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } - h \sum _ { i = 0 } ^ { k } \beta _ { i } ( f ( y ( x _ { n - i } ) ) - f ( y _ { n - i } ) ) } \end{array}$ i s the difference of two terms, of which the first can be bounded by a constant times $h ^ { 2 }$ , by Theorem 406B, and the second is zero. This means that

$$
\epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } = T _ { 1 } + T _ { 2 } + T _ { 3 } ,
$$

where

$$
\begin{array} { r } { \| T _ { 1 } \| = h | \beta _ { 0 } | \| f ( y ( x _ { n } ) ) - f ( y _ { n } ) \| \qquad \leq h L | \beta _ { 0 } | \cdot \| \epsilon _ { n } \| , } \end{array}
$$

$$
\| T _ { 2 } \| = h \Big \| \sum _ { i = 1 } ^ { k } \beta _ { i } \big ( f \big ( y ( x _ { n - i } ) \big ) - f \big ( y _ { n - i } \big ) \big ) \Big \| \leq h L \sum _ { i = 1 } ^ { k } | \beta _ { i } | \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| ,
$$

and $\| T _ { 3 } \|$ can be bounded in terms of a constant times $h ^ { 2 }$ . We now use (406d) twice. First, assuming $h \leq h _ { 0 }$ , obtain a bound on $( 1 - h L | \beta _ { 0 } | ) \| \epsilon _ { n } \|$ in terms of $\operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \|$ and terms that are bounded by a constant times $h ^ { 2 }$ . Hence, obtain a bound on $\| \epsilon _ { n } \|$ . Then, by inserting this preliminary result in the bound on $T _ { 1 }$ , we obtain the result of the theorem. 

Theorem 406D A stable consistent linear multistep method is convergent.

Proof. Write (406c) in the form

$$
\epsilon _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } + \psi _ { n } ,
$$

where, according to Theorem 406C,

$$
\| \psi _ { n } \| \leq C h \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| + D h ^ { 2 } ,
$$

for $h$ sufficiently small. Define $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ as in Subsection 141, and note that, because the method is convergent, the $\theta$ sequence is bounded. From Theorem 141A, we have

$$
\epsilon _ { n } = \sum _ { i = 0 } ^ { k - 1 } \theta _ { n - i } \widetilde { \epsilon } _ { i } + \sum _ { i = k } ^ { n } \theta _ { n - i } \psi _ { i } ,
$$

where $\widetilde { \epsilon } _ { i }$ , for $i = 0 , 1 , \ldots , k - 1$ , are linear combinations of the errors in $y _ { i }$ and tend to zero as $h  0$ . Hence we have

$$
\| \epsilon _ { n } \| \leq \Theta \sum _ { i = 0 } ^ { k - 1 } \| \widetilde { \epsilon } _ { i } \| + \Theta C h k \sum _ { i = k } ^ { n - 1 } \| \epsilon _ { i } \| + \Theta D ( n - k ) h ^ { 2 } ,
$$

where $\Theta = \operatorname* { s u p } _ { i = 1 } ^ { \infty } \left| \theta _ { i } \right|$ and the factor $k$ is introduced in the second summation in (406g) because the same maximum value of $\| \epsilon _ { n - i } \|$ may arise in up to $k$ adjacent terms. We rewrite (406g) in the form

$$
\| \epsilon _ { n } \| \leq \phi ( h ) + \Theta C h k \sum _ { i = 1 } ^ { n - 1 } \| \epsilon _ { i } \| + \Theta D n h ^ { 2 } , \quad \| \epsilon _ { 0 } \| \leq \phi ( h ) ,
$$

where $\phi ( h )$ takes positive values and will converge to zero as $h  0$ . It now follows that $\| \epsilon _ { n } \| \le u _ { n }$ , where the sequence $u$ is defined by

$$
u _ { n } = \Theta C h k \sum _ { i = 1 } ^ { n - 1 } u _ { i } + \Theta D n h ^ { 2 } + \phi ( h ) , \quad u _ { 0 } = \phi ( h ) .
$$

By subtracting (406h) with $n$ replaced by $n - 1$ , we find that

$$
u _ { n } + \frac { D h } { C k } = \left( 1 + \Theta C h k \right) \left( u _ { n - 1 } + \frac { D h } { C k } \right) ,
$$

which leads to the bound

$$
\begin{array} { r l r } & { } & { \| \epsilon _ { n } \| \le u _ { n } = ( 1 + \Theta C h k ) ^ { n } \phi ( h ) + \left( ( 1 + \Theta C h k ) ^ { n } - 1 \right) \displaystyle \frac { D h } { C k } } \\ & { } & \\ & { } & { \le \exp ( \Theta C k n h ) \phi ( h ) + ( \exp ( \Theta C k n h ) - 1 ) \displaystyle \frac { D h } { C k } . } \end{array}
$$

To complete the proof, substitute $n = m$ where $m h = \overline { { x } } - x _ { 0 }$ , so that the error in the approximation at $x = \overline { { x } }$ using $_ { I I }$ steps with stepsize $h$ is bounded by

$$
\exp ( \Theta C k ( \overline { { { x } } } - x _ { 0 } ) ) \phi ( h ) + \exp ( \Theta C k ( \overline { { { x } } } - x _ { 0 } ) ) \frac { D h } { C k } \to 0 .
$$

# Exercises 40

40.1 Find a four-stage Runge–Kutta method with $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 3 } = \frac { 2 } { 3 } } \end{array}$ , $c _ { 4 } = 1$ , which satisfies the order conditions

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } = \xi , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } = \frac 1 2 \xi ^ { 2 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 2 } = \frac 1 3 \xi ^ { 3 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 2 } = \frac 1 3 \xi ^ { 3 } , } \\ { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { i } a _ { i j } c _ { j } = \frac 1 6 \xi ^ { 3 } , } \end{array}
$$

where $\xi$ is a real parameter and the elements of $A$ are independent of $\xi$ . Show how this method can be used as a starter for the predictor– corrector pair consisting of the third order Adams–Bashforth and Adams–Moulton methods.

40.2 For each of the following polynomial pairs, written as $[ \alpha ( z ) , \beta ( z ) ]$ , determine if the corresponding numerical method is consistent and stable:

1. $\left[ 1 - z , 2 z - z ^ { 2 } \right]$ ,   
2. $[ 1 - z ^ { 2 } , 2 z - z ^ { 2 } ]$ ,   
3. $[ 1 + z - 3 z ^ { 2 } + z ^ { 3 } , 3 z - z ^ { 2 } ]$   
4. $[ 1 + z - z ^ { 2 } - z ^ { 3 } , 3 + z ]$ .

40.3 Translate the conditions for stability, preconsistency and consistency from the $[ \alpha , \beta ]$ representation to the $( \rho , \sigma )$ representation.

40.4 For a linear multistep method $[ \alpha , \beta ]$ , define polynomials $a$ and $b$ by

$$
\begin{array} { l } { { a ( z ) = ( 1 + z ) ^ { k } - \alpha _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) - \alpha _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } - \cdots } } \\ { { \qquad - ( 1 - z ) ^ { k } \alpha _ { k } , } } \\ { { b ( z ) = \beta _ { 0 } ( 1 + z ) ^ { k } + \beta _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) + \beta _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } + \cdots } } \\ { { \qquad + ( 1 - z ) ^ { k } \beta _ { k } . } } \end{array}
$$

Find the conditions for stability, preconsistency and stability in terms of the polynomials $a$ and $b$ .

# 41 The Order of Linear Multistep Methods

# 410 Criteria for order

Given a linear multistep method $[ \alpha , \beta ]$ , we seek conditions on the coefficients in the polynomials $\alpha$ and $\beta$ that will guarantee that, locally, errors are $O ( h ^ { p + 1 } )$ . By this we mean that if starting values satisfy $y _ { i } = y ( x _ { i } ) + O ( h ^ { p + 1 } )$ , for $i = 0 , 1 , \ldots , k { - } 1$ , then this will imply that a similar estimate persists for $i \geq k$ . We emphasize that this is a local property in the sense that it cannot be used in a limiting case in which integration is carried to a fixed point $\overline { { x } } > x _ { 0 }$ , because the number of steps required to achieve this is approximately $( { \overline { { x } } } - x _ { 0 } ) / h$ , and this is unbounded as $h  0$ . To verify that $y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } )$ , assuming the same is true for the previous $k$ step values, it will be enough to estimate the value of

$$
y ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x _ { n - i } ) - \sum _ { i = 0 } ^ { k } \beta _ { i } h y ^ { \prime } ( x _ { n - i } )
$$

and to show that, under appropriate smoothness assumptions, it is $O ( h ^ { p + 1 } )$ . The smoothness assumptions will be that the problem under consideration has a solution with continuous derivatives up to order $p + 1$ . This will enable us to expand (410a) in a Taylor series

$$
\begin{array} { r l } & { C _ { 0 } y ( x _ { n } ) + C _ { 1 } h y ^ { \prime } ( x _ { n } ) + C _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot } \\ & { \qquad + C _ { p } h ^ { p } y ^ { ( p ) } ( x _ { n } ) + C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + \cdot \cdot \cdot } \end{array}
$$

and order $p$ will mean that $C _ { 0 } = C _ { 1 } = \cdot \cdot \cdot = C _ { p }$ . The value of $C _ { p + 1 }$ is closely related to the error constant and is non-zero unless the order is actually higher than $p$ .

Theorem 410A The constants $C _ { 0 } , C _ { 1 } , C _ { 2 } , \ldots$ . in (410b) are given by

$$
\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) ) = C _ { 0 } + C _ { 1 } z + C _ { 2 } z ^ { 2 } + \cdot \cdot \cdot .
$$

Proof. The coefficient of in the Taylor expansion of (410a) is equal to $\textstyle 1 - \sum _ { i = 1 } ^ { k } \alpha _ { i }$ , and this equals the constant term in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ . Now suppose that $j = 1 , 2 , \dots$ and calculate the coefficient of $y ^ { ( j ) } ( x _ { n } )$ in the Taylor expansion of (410a). This equals

$$
- \sum _ { i = 1 } ^ { k } \alpha _ { i } { \frac { ( - i ) ^ { j } } { j ! } } - \sum _ { i = 0 } ^ { k } \beta _ { i } { \frac { ( - i ) ^ { j - 1 } } { ( j - 1 ) ! } } ,
$$

where the coefficient of $\beta _ { 0 }$ is $^ { - 1 }$ if $j = 1$ and zero for $j > 1$ . This is identical to the coefficient of $z ^ { j }$ in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ .