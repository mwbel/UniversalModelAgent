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
