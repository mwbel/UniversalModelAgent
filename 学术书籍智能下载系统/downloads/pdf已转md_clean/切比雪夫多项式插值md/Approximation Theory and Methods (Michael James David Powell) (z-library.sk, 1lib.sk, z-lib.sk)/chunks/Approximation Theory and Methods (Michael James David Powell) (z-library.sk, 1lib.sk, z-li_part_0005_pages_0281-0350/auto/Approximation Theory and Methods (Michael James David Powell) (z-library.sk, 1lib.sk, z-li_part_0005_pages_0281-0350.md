Because the function $\{ K ( \theta ) ; x _ { t } \leqslant \theta \leqslant x _ { t } + 2 h \}$ does not change sign, the mean value theorem gives the equation

$$
\begin{array} { c } { { { \displaystyle { \cal L } ( f ) = f ^ { \prime \prime \prime } ( \xi ) \int _ { x _ { t } } ^ { x _ { t } + 2 h } K ( \theta ) \mathrm { d } \theta } } } \\ { { { = \frac { 5 } { 1 2 } h ^ { 3 } f ^ { \prime \prime \prime } ( \xi ) , } } } \end{array}
$$

where $\xi$ is a point in the interval $[ x _ { t } , x _ { t } + 2 h ]$ .This result is stronger than the approximation (22.7).

# 22.2 The Peano kernel theorem

The notation $L ( f )$ is used in equation (22.5), because the righthand side is a linear functional of $f .$ We let $L$ be a general linear functional such that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k }$ If $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ we write it in the form

$$
f ( x ) = \sum _ { j = 0 } ^ { k } { \frac { ( x - a ) ^ { j } } { j ! } } f ^ { ( j ) } ( a ) + { \frac { 1 } { k ! } } \int _ { a } ^ { x } { ( x - \theta ) ^ { k } } f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta ,
$$

$$
a \leqslant x \leqslant b .
$$

When $L$ is applied to this equation, the contribution from the sum on the right-hand side is zero. Hence $L f$ is expressed in terms of $f ^ { ( k + 1 ) }$

The Peano kernel theorem states a useful form of this construction. It depends on a function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ that is defined in the following way. For any value of $\pmb \theta _ { \mathrm { i } }$ ， which in fact need not be in $[ a , b ] ,$ we let $\bullet _ { \pmb { \theta } }$ be the function

$$
\begin{array} { r } { s _ { \theta } ( x ) = ( x - \theta ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b . } \end{array}
$$

The number $\pmb { K } ( \pmb \theta )$ is obtained by applying the operator $L$ to the function $s _ { \theta } / k !$ , which gives the value

$$
K ( \theta ) = { \frac { 1 } { k ! } } L ( s _ { \theta } ) , \qquad a \leqslant \theta \leqslant b .
$$

It is convenient to introduce a notation that allows expressions (22.13) and (22.14) to be combined. Therefore we write the equation

$$
K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} , \qquad a \leqslant \theta \leqslant b ,
$$

where the notation $L _ { x } \{ \dots \}$ indicates that the expression in the braces is to be regarded as a function of $x$ on which $L$ operates.

Because it is sometimes useful to let $k = 0$ in equation (22.15),it may be necessary for $L ( f )$ to be defined when $f$ is in the space $\mathcal { V } [ a , b ] ,$ ，which is the space of real-valued functions on $[ a , b ]$ that are of bounded variation.

This condition is assumed in the next theorem, and it is assumed also that $L$ is bounded, which means that there is a constant $\| L \| _ { \infty }$ such that the inequality

$$
\begin{array} { r } { \left| L ( f ) \right| \leqslant \left\| L \right\| _ { \infty } \left\| f \right\| _ { \infty } , \qquad f \in \mathcal { V } [ a , b ] , } \end{array}
$$

holds, where $\| f \| _ { \infty }$ is the norm

$$
\| f \| _ { \infty } = \operatorname* { s u p } _ { a \leqslant x \leqslant b } { \big | } f ( x ) { \big | } , \qquad f \in { \mathcal { V } } [ a , b ] .
$$

These conditions on $L$ ，however，are too restrictive for general use, because they do not allow $L$ to depend on derivatives. Therefore another version of the Peano kernel theorem is given later.

# Theorem 22.1 (Peano kernel)

Let $k$ be any non-negative integer,and let $L$ be a bounded linear functional from $\mathcal { V } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ , such that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k }$ ,and such that the function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ ，which is defined by equation (22.15), is of bounded variation.Then, f $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ , the functional $L ( f )$ has the value

$$
L ( f ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta .
$$

Proof.By applying $L$ to expression (22.12) we obtain the equation

$$
L ( f ) = { \frac { 1 } { k ! } } L _ { x } { \Big \{ } { \int _ { a } ^ { b } ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta { \Big \} } } .
$$

Therefore it is sufficient to show that the operator $L _ { x }$ can be exchanged with the integration sign. The bounded variation conditions in the statement of the theorem, and also the fact that the variation of the function $\left\{ ( x - \theta ) _ { + } ^ { k } \right.$ ； $a \leqslant \theta \leqslant b \}$ is uniformly bounded for all $x$ in $[ a , b ] ,$ are needed in order to approximate integrals by Reimann sums. Thus,for any $\varepsilon > 0$ ，there exist points $\{ \theta _ { t } ; t = 1 , 2 , \ldots , m \}$ in $[ a , b ]$ such that the expression

$$
\bigg \vert \int _ { a } ^ { b } { ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } - \frac { ( b - a ) } { m } \sum _ { t = 1 } ^ { m } { ( x - \theta _ { t } ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta _ { t } ) } \bigg \vert = \eta ( x ) ,
$$

say, is less than $\pmb \varepsilon$ for all $x$ in $[ a , b ] ,$ , and such that the inequality

$$
\bigg | \displaystyle \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \bf d } \theta - \frac { ( b - a ) } { m } \sum _ { t = 1 } ^ { m } K ( \theta _ { t } ) f ^ { ( k + 1 ) } ( \theta _ { t } ) \bigg | \leqslant \varepsilon
$$

holds.Because the linearity of $L$ and the definition (22.15） give the identity

$$
\begin{array} { c } { { { \displaystyle { \cal L } _ { x } \bigg \{ \sum _ { t = 1 } ^ { m } ( x - \theta _ { t } ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta _ { t } ) \bigg \} = \sum _ { t = 1 } ^ { m } { \cal L } _ { x } \{ ( x - \theta _ { t } ) _ { + } ^ { k } \} f ^ { ( k + 1 ) } ( \theta _ { t } ) } } } \\ { { { = k ! \sum _ { t = 1 } ^ { m } K ( \theta _ { t } ) f ^ { ( k + 1 ) } ( \theta _ { t } ) , } } } \end{array}
$$

it follows from the accuracy of the Riemann sums that, if the equation

$$
L _ { x } { \Big \{ } \int _ { a } ^ { b } { ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } { \Big \} } = k ! \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

is not satisfied, then the difference between the two sides is bounded by the number

$$
\left| L _ { x } \{ \eta ( x ) \} \right| + k ! \varepsilon \leqslant ( \| L \| _ { \infty } + k ! ) \varepsilon .
$$

Since $\pmb \varepsilon$ can be arbitrarily small, equation (22.23) is valid.It follows from expression (22.19) that $L ( f )$ does have the value (22.18),which is the required result.□

This theorem gives useful expressions for the errors of many inter-polation and integration procedures. We have noted, however, that if $L$ depends on some derivatives of $f ,$ which is the case in example (22.5),and which is usual when one analyses the local truncation errors of linear multistep methods for solving ordinary differential equations, then $L$ is nct bounded, nor is it a mapping from ${ \mathcal { W } } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ . A suitable extension to Theorem 22.1 can be obtained by expressing $L ( f )$ in terms of a derivative of $f .$ For example, we can write equation (22.5) in the form

$$
\begin{array} { l } { { \displaystyle { \cal L } ( f ) = \int _ { x _ { t } + h } ^ { x _ { t } + 2 h } f ^ { \prime } ( x ) \mathrm { d } x - h \big [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) \big ] } } \\ { { \displaystyle ~ = M ( f ^ { \prime } ) , } } \end{array}
$$

say. It is important to notice that the linear operator $M$ is bounded, even though $L$ is not. Therefore it is valid to replace $L$ by $M$ and $f$ by $f ^ { \prime }$ in the statement of Theorem 22.1.Thus $\begin{array} { r } { M ( f ^ { \prime } ) = L ( f ) } \end{array}$ can be expressed in terms of $f ^ { \prime \prime }$ ，where $f$ is any function in $\mathcal { C } ^ { ( 3 ) } [ a , b ]$

This technique applies generally to operators $L$ that have the form

$$
L ( f ) = M ( f ^ { ( j ) } ) , \qquad f \in \mathcal { V } ^ { ( j ) } [ a , b ] ,
$$

where $\mathcal { V } ^ { ( j ) } [ a , b ]$ is the linear space of functions whose jth derivatives are of bounded variation, and where $M$ is a bounded linear operator from $\mathcal { V } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ . The generalization is given in the following theorem.

# Theorem 22.2

Let $L$ be the operator (22.26), where $M$ satisfies the conditions that have just been stated,and let $k$ be any integer that is greater than or equal to $j .$ If $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k } ,$ ,and if the function (22.15) is of bounded variation, then,for all functions $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ，the linear functional $L ( f )$ has the value that is given in Theorem 22.1.

Proof. Equations (22.15) and (22.26) give the relation

$$
\begin{array} { l } { { \displaystyle { K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} } } } \\ { { \displaystyle { \ = \frac { 1 } { ( k - j ) ! } M _ { x } \{ ( x - \theta ) _ { + } ^ { k - j } \} , \qquad a \leqslant \theta \leqslant b . } } } \end{array}
$$

Because,by hypothesis, this function is of bounded variation,and because of the conditions that are satisfied by $M ,$ we may replace $L$ by $M , f$ $\boldsymbol { \mathsf { b y } } \boldsymbol { f } ^ { ( i ) }$ and $\pmb { k }$ by $( k - j )$ in the statement of Theorem 22.1. Hence we obtain the value

$$
M ( f ^ { ( j ) } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

It follows from equation (22.26) that the theorem is true.□

The refinements of bounded variation and the differences between Theorems 22.1 and 22.2 are usually ignored in practice. The standard way of applying the Peano kernel theorem is to check first that $L$ is a linear operator, that $L ( f )$ is zero if $f$ is any polynomial of degree $k$ and that $L$ does not depend on any derivatives of degree greater than $\pmb { k }$ If these conditions hold, then $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ is calculated from equation (22.15). This function,which is called the ‘kernel function',is substituted into equation (22.18). Thus $L ( f )$ is expressed in terms of the derivative $\{ f ^ { ( k + 1 ) } ( \pmb { \theta } ) ; a \leqslant \pmb { \theta } \leqslant b \}$

There is a neat way of verifying that the condition

$$
L ( f ) = 0 , \qquad f \in \mathcal { P } _ { k } ,
$$

holds. It is the reason for the remark, made immediately before equation (22.13), that the value of $\pmb \theta$ need not be in the range $[ a , b ]$ .We consider the definition

$$
K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} , \qquad - \infty < \theta < \infty .
$$

If $\theta < a$ , then the function $\left\{ ( { \pmb x } - { \pmb \theta } ) _ { + } ^ { k } \right.$ ； $a \leqslant x \leqslant b \}$ is in $\mathcal { P } _ { k } ,$ and, if $\pmb \theta > b$ ,then

it is the zero function. Hence the equations

$$
\left. \begin{array} { c } { { K ( \theta ) = 0 , \theta < a } } \\ { { K ( \theta ) = 0 , \theta > b } } \end{array} \right\}
$$

should be obtained. Because the space $\mathcal { P } _ { k }$ is spanned by the polynomials $\{ ( x - \theta _ { t } ) ^ { k } ; - \infty < x < \infty ; t = 0 , 1 , \ldots , k \}$ ,where $\left\{ \theta _ { t } ; t = 0 , 1 , \ldots , k \right\}$ is any set of distinct real numbers that are less than $^ { a }$ ,the first line of expression (22.31) is both a necessary and a sufficient condition for $L ( f )$ to be zero when $f$ is in $\mathcal { P } _ { k }$

When $k = 2$ ,and when $L$ is the functional (22.5), the definition (22.30) is the equation

$$
\begin{array} { r } { K ( \theta ) = \frac { 1 } { 2 } \{ ( x _ { t } + 2 h - \theta ) _ { + } ^ { 2 } - ( x _ { t } + h - \theta ) _ { + } ^ { 2 } \quad } \\ { - h [ 3 ( x _ { t } + h - \theta ) _ { + } - ( x _ { t } - \theta ) _ { + } ] \} , ~ - \infty < \theta < \infty . } \end{array}
$$

It is straightforward to verify that $\pmb { K } ( \pmb \theta )$ is zero when $\pmb \theta$ is less than $\boldsymbol { x } _ { t } .$ If $\pmb \theta$ is increased through the value $\pmb \theta = \pmb x _ { t } ,$ then the term $( x _ { t } - \theta ) _ { + }$ in expression (22.32) is the only one that causes a discontinuity in $\pmb { K } ( \pmb \theta )$ . This remark is useful, because it provides a convenient way of calculating the first line of equation (22.10).

# 22.3 Application to divided differences and to polynomial interpolation

Theorem 5.1 states that, if $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ , then the divided difference $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ]$ is equal to $f ^ { ( k + 1 ) } ( \xi ) / ( k + 1 ) !$ for some number $\xi .$ Hence $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ]$ is zero when $f$ is in $\mathcal { P } _ { k }$ It follows from Theorem 22.1 that the following useful and interesting relation is obtained between divided differences and $\pmb { B }$ -splines.

# Theorem 22.3

f $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ and if $\{ x _ { i } ; i = 0 , 1 , \ldots , k + 1 \}$ is a set of distinct points in $[ a , b ] ,$ , then the equation

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k + 1 } ] { = } { \frac { 1 } { k ! } } \int _ { a } ^ { b } B ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

is satisfied, where $\pmb { B }$ is the $\pmb { B }$ -spline

$$
B ( \theta ) = \sum _ { i = 0 } ^ { k + 1 } \bigg \{ ( \theta - x _ { i } ) _ { + } ^ { k } \bigg / \prod _ { { j = 0 } \atop { j \ne i } } ^ { k + 1 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leqslant \theta \leqslant b .
$$

Proof. By equation (5.2) the divided difference is the expression

$$
\begin{array} { c } { { f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ] = \displaystyle \sum _ { i = 0 } ^ { k + 1 } \left\{ f ( x _ { i } ) \Biggl / \prod _ { j = 0 \atop j \ne i } ^ { k + 1 } ( x _ { i } - x _ { j } ) \right\} } } \\ { { = { \cal L } ( f ) , } } \end{array}
$$

say. Therefore,for any fixed and distinct points $\{ x _ { i } ; i = 0 , 1 , \ldots , k + 1 \}$ ， $L$ is a bounded linear operator from $\mathcal { V } [ a , b ]$ to $\mathcal { R } ^ { 1 }$ , and the function (22.15） is of bounded variation. It follows from Theorem 22.1 that equation (22.18) is satisfied, where $\pmb { K } ( \pmb \theta )$ has the value

$$
K ( \theta ) = { \frac { 1 } { k ! } } \sum _ { i = 0 } ^ { k + 1 } \Big \{ ( x _ { i } - \theta ) _ { + } ^ { k } \Big / \prod _ { j = 0 \atop j \neq i } ^ { k + 1 } ( x _ { i } - x _ { j } ) \Big \} , \qquad a \leqslant \theta \leqslant b .
$$

Equation (22.18) shows that the required relation (22.33) is valid if and only if the function (22.34) is equal to $k ! K .$ We substitute the identity

$$
\left( x _ { i } - \theta \right) _ { + } ^ { k } = \left( x _ { i } - \theta \right) ^ { k } + \left( - 1 \right) ^ { k + 1 } \left( \theta - x _ { i } \right) _ { + } ^ { k }
$$

into expression (22.36) for $i = 0 , 1 , \ldots , k + 1$ ， which gives the equation

$$
K ( \theta ) = \frac { 1 } { k ! } [ L _ { x } \{ \left( x - \theta \right) ^ { k } \} + B ( \theta ) ] , \qquad a \leqslant \theta \leqslant b .
$$

The term $L _ { x } \{ { ( x - \theta ) } ^ { k } \}$ is zero,because the function $\{ ( x - \theta ) ^ { k } ; a \leqslant x \leqslant b \}$ is in $\mathcal { P } _ { k }$ .Therefore the theorem is true.□

This theorem is more general than Theorem 5.1, because equation (22.33) does not depend on the unknown number $\xi .$ Further,Theorem 5.1 can be deduced from Theorem 22.3 in the following way. We recall that $B$ -splines are non-negative. Therefore,by applying the mean value theorem to equation (22.33), the relation

$$
f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ] { = } \frac { 1 } { k ! } { \biggl [ } \int _ { a } ^ { b } B ( \theta ) \mathrm { d } \theta { \biggl ] } f ^ { ( k + 1 ) } ( \xi )
$$

is obtained, where $\pmb { \xi }$ is in the interval $[ a , b ]$ .Because this relation holds in the particular case when $f$ is the polynomial $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b $ ,and because of the original definition of a divided difference, the integral of the $\pmb { B }$ -spline has the value

$$
\int _ { a } ^ { b } B ( \theta ) { \bf d } \theta = 1 / ( k + 1 ) .
$$

Hence Theorem 5.1 is true.

Theorem 22.3 is also useful to the main subject of Chapters 23 and 24, which is the problem of obtaining good approximations from the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ when $^ { m }$ is large.For example, we may have to choose the weights $\{ w _ { t } ; t = 1 , 2 , \dots , m \}$ in formula (22.1),and it may be suitable to force the approximation to be exact only when $f$ is a polynomial of degree $k$ ,where $k$ is much smaller than $_ m$ . In this case a suitable technique,for taking up the freedom in the weights, is to apply the Peano kernel theorem to express the error of the approximation in terms of the derivative $\{ f ^ { ( k + 1 ) } ( \theta ) ; a \leqslant \theta \leqslant b \}$ ,and then to use the freedom to make the kernel function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ small. It is convenient to write the approximation (22.1) in the form

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x \approx \sum _ { t = 1 } ^ { k + 1 } u _ { t } f ( x _ { t } ) + \sum _ { t = 1 } ^ { m - k - 1 } v _ { t } f [ x _ { t } , x _ { t + 1 } , \ldots , x _ { t + k + 1 } ] ,
$$

because then the freedom in the weights allows arbitrary values of the parameters $\{ v _ { t } ; t = 1 , 2 , \ldots , m - k - 1 \}$ .Theorem 22.3 shows the change to the kernel function that is caused by adjustments to the parameters $\{ v _ { t } ; t = 1 , 2 , \ldots , m - k - 1 \} .$

This theorem also gives an expression for the error of polynomial interpolation. As in Theorem 5.2,we let $\{ p _ { k } ( x )$ ； $a \leqslant x \leqslant b $ be the polynomial in $\mathcal { P } _ { k }$ that satisfies the interpolation conditions

$$
p _ { k } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , k ,
$$

and we let $x _ { k + 1 }$ be any point of $[ a , b ]$ that is not in the set $\{ x _ { i } ; i = 0$ ， $1 , \ldots , k \}$ . Because Theorem 5.2 implies the equation

$$
f ( x _ { k + 1 } ) = p _ { k } ( x _ { k + 1 } ) + \bigg \{ \prod _ { j = 0 } ^ { k } { \left( x _ { k + 1 } - x _ { j } \right) } \bigg \} f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k + 1 } ] ,
$$

it follows from Theorem 22.3 that the difference $\{ f ( x _ { k + 1 } ) - p _ { k } ( x _ { k + 1 } ) \}$ has the value

$$
\begin{array} { c } { { f ( x _ { k + 1 } ) - p _ { k } ( x _ { k + 1 } ) = \displaystyle \frac { 1 } { k ! } \bigg \{ \prod _ { j = 0 } ^ { k } \left( x _ { k + 1 } - x _ { j } \right) \bigg \} \displaystyle \int _ { a } ^ { b } B ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } } \\ { { = \displaystyle \frac { 1 } { ( k + 1 ) ! } \bigg \{ \prod _ { j = 0 } ^ { k } \left( x _ { k + 1 } - x _ { j } \right) \bigg \} f ^ { ( k + 1 ) } ( \xi ) , } } \\ { { \xi \in [ a , b ] , \qquad ( 2 } } \end{array}
$$

where the last line depends on the condition $\{ B ( \pmb \theta ) \geq 0$ ； $a \leqslant \theta \leqslant b \}$ , on the mean value theorem,and on equation (22.4O). Both lines of this expression are useful,and we see that the second one is the same as the statement of Theorem 4.2.

It is important to note that often the linear functional $L$ and the value of $k$ are such that the kernel function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ of equation (22.18) changes sign. For example, the possibility that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k + 1 }$ does not impair the validity of Theorem 22.1. If this possibility occurs, and if we let $f$ be the function $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b \}$ ,then equation (22.18) implies the identity

$$
\int _ { a } ^ { b } K ( \theta ) { \bf d } \theta = 0 .
$$

In general, therefore, one should not expect the equation

$$
L ( f ) = \int _ { a } ^ { b } K ( \theta ) \mathrm { d } \theta f ^ { ( k + 1 ) } ( \xi )
$$

to be satisfied for some value of $\xi$ in $[ a , b ]$

# 22.4 Application to cubic spline interpolation

In order to show the usefulness of the Peano kernel theorem, it is applied in this section to bound the error of a cubic spline approximation that is defined by interpolation. We consider the procedure,described in Section 18.2, where the knots of the spline have the values

$$
x _ { j } = j h , \qquad j = 0 , \pm 1 , \pm 2 , \ldots ,
$$

and where the interpolation conditions are the equations

$$
s ( x _ { j } ) = f ( x _ { j } ) , \qquad j = 0 , \pm 1 , \pm 2 , . . . .
$$

We recall that $\pmb { s }$ can be expressed in the form

$$
s ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad - \infty < x < \infty ,
$$

where the cardinal spline $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ is symmetric about $\boldsymbol { x } = \boldsymbol { x } _ { j } ,$ and has the properties that are shown in Figure 18.2.In particular, the fact that the tails of the cardinal function reduce by the factor $( { \sqrt { 3 } } - 2 )$ per knot gives the conditions

$$
\begin{array} { r l r l } & { l _ { j } ( x - h ) = ( \sqrt { 3 } - 2 ) l _ { j } ( x ) , } & & { x \leqslant x _ { j - 1 } } \\ & { l _ { j } ( x + h ) = ( \sqrt { 3 } - 2 ) l _ { j } ( x ) , } & & { x \geqslant x _ { j + 1 } } \end{array} \bigg \} .
$$

Because the Peano kernel theorem concerns linear functionals,we study the error of the interpolation procedure for a particular value of the variable $\pmb { x } .$ .Therefore we let $L$ be the functional

$$
\begin{array} { l } { { \displaystyle { \cal L } ( f ) = f ( \xi ) - s ( \xi ) } } \\ { { \displaystyle ~ = f ( \xi ) - \sum _ { j = - \infty } ^ { \infty } l _ { j } ( \xi ) f ( x _ { j } ) , } } \end{array}
$$

where $\xi$ is a fixed real number,which, for convenience, is chosen in the interval $[ 0 , h ]$ . Although the range of the variable is infinite, it is assumed that the Peano kernel theorem can be applied.Hence, if $f$ is in $\mathcal { C } ^ { ( 4 ) } ( - \infty , \infty )$ , then the equation

$$
f ( \xi ) - s ( \xi ) = \int _ { - \infty } ^ { \infty } K ( \theta ) f ^ { ( 4 ) } ( \theta ) { \bf d } \theta
$$

is satisfied, where $\pmb { K }$ is the function

$$
K ( \theta ) = \frac { 1 } { 3 ! } \biggl [ ( \xi - \theta ) _ { + } ^ { 3 } - \sum _ { j = - \infty } ^ { \infty } l _ { j } ( \xi ) ( x _ { j } - \theta ) _ { + } ^ { 3 } \biggr ] , \qquad - \infty < \theta < \infty .
$$

We derive some properties of this kernel function,in order to obtain bounds on the error (22.52).

First it is proved that the form of $\{ K ( \theta ) ; - \infty < \theta < \infty \}$ is similar to the form of a cardinal function when $| \pmb \theta |$ is large.Because the behaviour of the cardinal functions that gives expression (22.50) also implies the equation

$$
l _ { j } ( \xi ) = ( \surd 3 - 2 ) l _ { j - 1 } ( \xi ) , \qquad j \geq 3 ,
$$

it follows from the definition (22.53) that, for $\pmb \theta \geqslant x _ { 1 }$ ,the relation

$$
\begin{array} { l } { { \displaystyle K ( \theta + h ) = - \frac { 1 } { 6 } \sum _ { j = 3 } ^ { \infty } l _ { j } ( \xi ) ( x _ { j } - \theta - h ) _ { + } ^ { 3 } } } \\ { { \displaystyle \quad = - \frac { 1 } { 6 } ( \surd 3 - 2 ) \sum _ { j = 3 } ^ { \infty } l _ { j - 1 } ( \xi ) ( x _ { j - 1 } - \theta ) _ { + } ^ { 3 } } } \\ { { \displaystyle \quad = ( \surd 3 - 2 ) K ( \theta ) } } \end{array}
$$

is obtained.A remarkable result can now be deduced from the fact that, if $p$ is any cubic polynomial, then the identity

$$
\begin{array} { c } { { 1 2 [ p ( x _ { j + 1 } ) - p ( x _ { j } ) ] = ( 6 + 2 \sqrt { 3 } ) h [ p ^ { \prime } ( x _ { j + 1 } ) - ( \sqrt { 3 } - 2 ) p ^ { \prime } ( x _ { j } ) ] } } \\ { { - ( \sqrt { 3 } + 1 ) h ^ { 2 } [ p ^ { \prime \prime } ( x _ { j + 1 } ) - ( \sqrt { 3 } - 2 ) p ^ { \prime \prime } ( x _ { j } ) ] } } \end{array}
$$

holds. We let $j$ be any positive integer, and we let $p$ be the polynomial $\left\{ K ( \theta ) \right.$ ； $x _ { j } \leqslant \theta \leqslant x _ { j + 1 } \}$ . Because equation (22.55） implies that the righthand side of expression (22.56) is zero, the numbers $K ( x _ { j } )$ and $\pmb { K } ( \pmb { x } _ { j + 1 } )$ are equal. However, condition (22.55) has to hold when $\theta = x _ { j } .$ Hence the equations

$$
K ( x _ { j } ) = 0 , \qquad j = 1 , 2 , 3 , \ldots ,
$$

Figure 22.1.A kernel function for cubic spline interpolation.

![](images/50f54a38e1151941cf9b02c59ec64e93fdd752637049dc340e23e98115b23cdb.jpg)

are satisfied. By symmetry, or by applying the technique that depends on expression (22.37) in the proof of Theorem 22.3,we also deduce the conditions $\{ K ( x _ { j } ) = 0 ; j = 0 , - 1 , - 2 , . . . \}$ and $\left\{ K ( \theta - h ) = ( \sqrt { 3 } - 2 ) K ( \theta ) \right.$ $\theta \leqslant x _ { 0 } \}$ . These properties are displayed in Figure 22.1, but the form of $\kappa$ in the interval $[ 0 , h ]$ requires further analysis.

Equation (22.53)and the figure imply that there exist parameters $\lambda , \mu$ and $^ d$ such that $\pmb { K }$ is the function

$$
K ( \theta ) = \left\{ \begin{array} { l l } { \lambda ~ \sigma ( - \theta / h ) , \qquad \theta \leqslant 0 } \\ { \mu ~ \sigma ( \theta / h ) + \frac { 1 } { 6 } ( \xi - \theta ) ^ { 3 } + \frac { 1 } { 6 } d ( h - \theta ) ^ { 3 } , \qquad 0 \leqslant \theta \leqslant \xi } \\ { \mu ~ \sigma ( \theta / h ) + \frac { 1 } { 6 } d ( h - \theta ) ^ { 3 } , \qquad \xi \leqslant \theta \leqslant h } \\ { \mu ~ \sigma ( \theta / h ) , \qquad \theta \geqslant h , } \end{array} \right.
$$

where $\{ \sigma ( x ) ; 0 \leqslant x < \infty \}$ is defined in equation (21.49). Because $\mathbf { \partial } \kappa , \mathbf { \partial } \kappa ^ { \prime }$ and $\pmb { K } ^ { \prime \prime }$ are continuous at $\pmb \theta = 0$ , it follows that the parameters have the values

$$
\left. \begin{array} { l } { d = - \xi ^ { 3 } / h ^ { 3 } } \\ { \lambda = \frac { 1 } { 1 2 } [ - \sqrt { 3 } \xi h ^ { 2 } + 3 \xi ^ { 2 } h - ( 3 - \sqrt { 3 } ) \xi ^ { 3 } ] } \\ { \mu = \frac { 1 } { 1 2 } [ \sqrt { 3 } \xi h ^ { 2 } + 3 \xi ^ { 2 } h - ( 3 + \sqrt { 3 } ) \xi ^ { 3 } ] } \end{array} \right\} .
$$

We note that, for all $\xi$ in $( 0 , h ) , \lambda$ is negative and $\pmb { \mu }$ is positive. Hence $\pmb { K } ( \pmb \theta )$ has the correct sign in Figure 22.1,except perhaps when $0 < \theta < h$ In this interval $\pmb { K } ( \pmb \theta )$ is positive, but there seems to be no short way of proving this statement. One method begins with the remark that, because $\pmb { K } ( 0 ) = 0$ ， $K ^ { \prime } ( 0 ) { > } 0$ and $K ^ { \prime \prime \prime } ( 0 + ) < 0$ ,there is at most one zero of $\pmb { K }$ in the interval $( 0 , \xi ]$ .Direct calculation gives $\pmb { K } ( \pmb { \xi } ) > 0 .$ Hence $\pmb { K }$ has no zeros in $( 0 , \xi ]$ ，Similarly there are no zeros in $[ \xi , h )$ ，which completes the justification of the signs that are shown in Figure 22.1.

It is now straightforward to calculate the integral

$$
I ( \xi ) = \int _ { - \infty } ^ { \infty } \left| K ( \theta ) \right| \mathrm { d } \theta , \qquad 0 \leqslant \xi \leqslant h ,
$$

in order to bound the error (22.52) by a multiple of $\| f ^ { ( 4 ) } \| _ { \infty }$ . Because the function (21.49) satisfies the equation

$$
\sigma ( x + 1 ) = ( \sqrt { 3 - 2 } ) \sigma ( x ) , \qquad x \geqslant 0 ,
$$

expression (22.58),Figure 22.1, and the definition of $\sigma$ give the value

$$
\begin{array} { l } { { \displaystyle I ( \xi ) = \left( \left| \lambda \right| + \left| \mu \right| \right) \Biggl [ \int _ { 0 } ^ { h } \sigma ( \theta / h ) \mathrm { d } \theta \Biggr ] \Biggl [ \sum _ { j = 0 } ^ { \infty } \left| \surd 3 - 2 \right| ^ { j } \Biggr ] } } \\ { { \displaystyle \qquad + \frac { 1 } { 6 } \int _ { 0 } ^ { \xi } \left( \xi - \theta \right) ^ { 3 } \mathrm { d } \theta + \frac { 1 } { 6 } d \int _ { 0 } ^ { h } \left( h - \theta \right) ^ { 3 } \mathrm { d } \theta } } \\ { { \displaystyle \qquad = \left( \left| \lambda \right| + \left| \mu \right| \right) \frac { 1 } { 1 2 } \sqrt { 3 } h + \frac { 1 } { 2 4 } ( \xi ^ { 4 } + d h ^ { 4 } ) . } } \end{array}
$$

It follows from equations (22.52) and (22.59) that the bound

$$
\begin{array} { r l } & { \left| f ( \xi ) - s ( \xi ) \right| \leqslant I ( \xi ) \left\| f ^ { ( 4 ) } \right\| _ { \infty } } \\ & { \qquad = \frac { 1 } { 2 4 } ( \xi ^ { 4 } - 2 \xi ^ { 3 } h + \xi h ^ { 3 } ) \left\| f ^ { ( 4 ) } \right\| _ { \infty } , \quad \quad 0 \leqslant \xi \leqslant h , } \end{array}
$$

is obtained. Therefore, because the right-hand side takes its maximum value when $\xi = { \textstyle \frac { 1 } { 2 } } h .$ ，and because all intervals between data points are similar,the error of the spline approximation is bounded by the inequality

$$
\| f - s \| _ { \infty } \leqslant \frac { 5 h ^ { 4 } } { 3 8 4 } \| f ^ { ( 4 ) } \| _ { \infty } .
$$

In order to check most of the work of this section, we let $f$ be a quartic polynomial, and we deduce the error $f ( \xi ) - s ( \xi )$ from equations (22.52), (22.58) and (22.59). Because $f ^ { ( 4 ) } ( x )$ is constant the equation

$$
f ( \xi ) - s ( \xi ) = J ( \xi ) f ^ { ( 4 ) } ( x ) , 0 \leqslant \xi \leqslant h ,
$$

is satisfied, where $\pmb { J } ( \pmb { \xi } )$ is the integral

$$
\begin{array} { l } { { \displaystyle { J ( \xi ) = ( \lambda + \mu ) \biggl [ \int _ { 0 } ^ { h } \sigma ( \theta / h ) \mathrm { d } \theta \biggl ] \biggl [ \sum _ { j = 0 } ^ { \infty } ( \sqrt { 3 - 2 } ) ^ { j } \biggr ] } } } \\ { { \displaystyle ~ + \frac { 1 } { 6 } \int _ { 0 } ^ { \xi } ( \xi - \theta ) ^ { 3 } \mathrm { d } \theta + \frac { 1 } { 6 } d \int _ { 0 } ^ { h } \left( h - \theta \right) ^ { 3 } \mathrm { d } \theta } }  \\ { { = ( \lambda + \mu ) \frac { 1 } { 1 2 } h + \frac { 1 } { 2 4 } ( \xi ^ { 4 } + d h ^ { 4 } ) } } \\ { { = \frac { 1 } { 2 4 } \xi ^ { 2 } ( \xi - h ) ^ { 2 } . } } \end{array}
$$

The check on the calculation is that we have verified the first line of expression (21.43).

Inequality (22.64) provides a substantial improvement on the bound (20.52), where $\mathcal { S }$ is the space of cubic splines whose knots are the points

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = 0 , 1 , \ldots , n ,
$$

and where $f$ is any function in $\mathcal { C } ^ { ( 4 ) } [ \xi _ { 0 } , \xi _ { n } ]$ .The analysis for the infinite range is applicable to this case, because we may extend $f$ to the infinite range in any way that does not increase $\| f ^ { ( 4 ) } \| _ { \infty }$ ,and we may let $\pmb { S }$ be the spline (22.49). The restriction of $\pmb { S }$ to the interval $[ \xi _ { 0 } , \xi _ { n } ]$ is an element of ${ \mathcal { S } } .$ Hence $d ^ { * } ( \mathcal { S } , f )$ is bounded above by $\| f - s \| _ { \infty }$ . It follows from inequality (22.64) that the constant in expression (20.52) can be reduced from $\frac { 7 3 } { 3 8 4 }$ t0 $\frac { 5 } { 3 8 4 }$

One unusual feature of the example of this section is that all the zeros of the kernel function (22.53) occur at points where a derivative of $\pmb { K }$ is discontinuous. In general, if equation (22.18) holds,and if one requires the value of the constant (22.3) in the bound

$$
{ \big | } L ( f ) { \big | } \leqslant c { \big | } { \big | } f ^ { ( k + 1 ) } { \big | } { \big | } _ { \infty } ,
$$

then it is necessary to find the values of $\pmb \theta$ at which $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ changes sign by solving a polynomial equation. Some examples are $\mathtt { \mathtt { s i v e n } }$ in the exercises.

# 22 Exercises

22.1Let $p ( { \scriptstyle { \frac { 1 } { 2 } } } ) = { \scriptstyle { \frac { 1 } { 2 } } } [ f ( 0 ) + f ( 1 ) ] .$ where $f$ is a function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ .Find the smallest constants $c _ { 0 } , \ : c _ { 1 }$ and $c _ { 2 }$ such that the error bounds

$$
\begin{array} { r } { \big | f ( \frac { 1 } { 2 } ) - p ( \frac { 1 } { 2 } ) \big | \leqslant c _ { k } \big \| f ^ { ( k ) } \big \| _ { \infty } , \qquad k = 0 , 1 , 2 , } \end{array}
$$

are valid.

22.2 Let $f$ be any function in $\mathcal { C } ^ { ( 4 ) } [ 0 , 2 ]$ 、 Show that the error of Simpson's integration rule satisfies the equation

$$
\begin{array} { r } { \displaystyle \int _ { 0 } ^ { 2 } f ( x ) \mathrm { d } x - \frac { 1 } { 3 } [ f ( 0 ) + 4 f ( 1 ) + f ( 2 ) ] = - \frac { 1 } { 9 0 } f ^ { ( 4 ) } ( \xi ) , } \end{array}
$$

where $\xi$ is a point of the range [0,2].

22.3 Calculate the values of the coefficients $w _ { 0 } , w _ { 1 }$ and $w _ { 3 }$ such that the inequality

$$
\left| f ( 2 ) - \left[ w _ { 0 } f ( 0 ) + w _ { 1 } f ( 1 ) + w _ { 3 } f ( 3 ) \right] \right| \leqslant \mu \| f ^ { \prime \prime } \| _ { 2 }
$$

holds for all functions $f$ in $\mathscr { C } ^ { ( 2 ) } [ 0 , 3 ]$ , where the degree of freedom in the coefficients is used to minimize the constant $\pmb { \mu }$ . You should obtain the bound

$$
\begin{array} { r } { { \left| f ( 2 ) + \frac { 1 } { 4 } f ( 0 ) - \frac { 7 } { 8 } f ( 1 ) - \frac { 3 } { 8 } f ( 3 ) \right| \leqslant \sqrt { ( \frac { 5 } { 4 8 } ) } \left\| f ^ { \prime \prime } \right\| } _ { 2 } . } \end{array}
$$

22.4 Prove Theorem 22.3 by integrating the right-hand side of equation (22.33) by parts.

Show by an example that the constant $\frac { 5 } { 3 8 4 }$ in expression (22.64) cannot be reduced. There exists a suitable function $f$ that is zero at all the knots.

22.6 Let $f$ be a function in $\mathcal { C } ^ { ( 4 ) } [ 0 , 1 ]$ . Calculate the third derivative of the cubic polynomial $p$ that interpolates the data $\left\{ f ( 0 ) , f ^ { \prime } ( 0 ) \right.$ ， $f ( 1 ) , f ^ { \prime } ( 1 ) \}$ . Prove that the inequality

$$
\begin{array} { r } { \left| f ^ { \prime \prime \prime } ( \xi ) - p ^ { \prime \prime \prime } ( \xi ) \right| \leqslant ( \frac { 1 } { 2 } - \xi + 2 \xi ^ { 3 } - \xi ^ { 4 } ) \| f ^ { ( 4 ) } \| _ { \infty } } \end{array}
$$

is satisfied, where $\pmb { \xi }$ is any point in [O,1]. Find a function $f$ with a piecewise continuous fourth derivative for which this inequality holds as an equation.

22.7 Calculate the values of the parameters $w _ { 1 } , w _ { 2 } , w _ { 3 }$ and $w _ { 4 }$ that minimize the number $\pmb { \mu }$ in the bound

$$
\bigg \vert \int _ { 0 } ^ { 1 } f ( x ) \mathrm { d } x - w _ { 1 } f ( 0 ) - w _ { 2 } f ^ { \prime } ( 0 ) - w _ { 3 } f ( 1 ) - w _ { 4 } f ^ { \prime } ( 1 ) \bigg \vert \leqslant \mu \| f ^ { \prime \prime } \| _ { \infty } ,
$$

where $f$ is any function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ . Show that the least value of $\pmb { \mu }$ is $\scriptstyle { \frac { 1 } { 3 2 } }$

22.8 Prove that the right-hand side of the final inequality of Exercise 22.3 can be replaced by the expression $\begin{array} { r } { \sqrt { \left( \frac { 5 } { 4 8 } \right) [ \| f ^ { \prime \prime } \| _ { 2 } ^ { 2 } - 9 ( f [ 0 , 1 , 3 ] ) ^ { 2 } ] ^ { \frac { 1 } { 2 } } } , } \end{array}$ which is a useful improvement because the divided difference $\textstyle f [ 0 , 1 , 3 ]$ can be calculated from the function values $f ( 0 ) , f ( 1 )$ and $f ( 3 )$ . One method of proof comes from expressing $f ^ { \prime \prime }$ in the form $f ^ { \prime \prime } ( \theta ) = \alpha B ( \theta ) + \{ f ^ { \prime \prime } ( \theta ) - \alpha B ( \theta ) \} , \qquad 0 \leqslant \theta \leqslant 3 ,$ where $\pmb { B }$ is the kernel function that occurs when Theorem 22.3 is used to express $f [ 0 , 1 , 3 ]$ in terms of $f ^ { \prime \prime }$ ,and where the multiplier $_ \alpha$ is such that the term in the braces is orthogonal to $f ^ { \prime \prime }$ . Verify that the two sides of the new inequality are equal when $f$ is the function $\{ f ( x ) = x ^ { 3 } - 3 ( x - 2 ) _ { + } ^ { 3 }$ ； $0 \leqslant x \leqslant 3 \}$ and explain why this happens.

22.9 Investigate the validity of the assumption, made immediately before equation (22.52), that the Peano kernel theorem can be applied when the range of the variable $x$ is infinite,given the condition that the derivatives of $f$ are bounded.

22.10 For any bounded function $f$ in $\mathcal { C } ^ { ( 3 ) } ( - \infty , \infty )$ ,let $\pmb { s }$ be the quadratic spline with knots at the points (18.35),that satisfies the interpolation conditions $\{ s ( x _ { j } ) = f ( x _ { j } ) = f ( j h )$ ； $\dot { \mathbf { \theta } } = 0 , \mathbf { \theta } \pm 1 , \mathbf { \eta } \pm 2$ ， .. .},and that is studied in Section 18.4. Prove that the value of the spline at a knot is bounded by the inequality

$$
\big | f ( \xi _ { i } ) - s ( \xi _ { i } ) \big | \mathrm { \leqslant } \frac { h ^ { 3 } } { 2 4 } \big \| f ^ { \prime \prime \prime } \big \| _ { \infty } .
$$

# 23

# Natural and perfect splines

# 23.1 A variational problem

A very early result in the study of spline approximations is that a cubic spline is the solution of the following variational problem. Given the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ in the interval $[ a , b ] ,$ satisfying the conditions

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b ,
$$

and given the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ，calculate the function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that minimizes the integral

$$
\int _ { a } ^ { b } \left[ s ^ { \prime \prime } ( x ) \right] ^ { 2 } \mathrm { d } x ,
$$

subject to the interpolation equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

If one knows the solution to this problem in advance, then there is a short way of showing that one has the required function, which is given in the proof of Theorem 23.2.In this section, however, the solution is derived without foresight or intuition,because the method that is used has other applications.

We assume that $m > 2$ ,because otherwise the integral (23.2) can be made zero, by letting $\pmb { \mathscr { s } }$ be any straight line that interpolates the data. When $m > 2$ ， then it is necessary to identify the restrictions that the conditions (23.3） impose on the second derivative $\{ s ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ Because Theorem 22.3 shows that divided differences can be expressed in terms of derivatives, the equations

$$
s [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

which follow from condition (23.3)，are really constraints on $\pmb { s } ^ { \prime \prime }$ Specifically,applying the theorem to expression (23.4） gives the constraints

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) s ^ { \prime \prime } ( \theta ) { \mathrm d } \theta = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

where $\scriptstyle B _ { p }$ is the first degree $\pmb { B }$ -spline

$$
B _ { p } ( \theta ) = \sum _ { i = p } ^ { p + 2 } \bigg \{ ( \theta - x _ { i } ) _ { + } \bigg / \prod _ { \stackrel { j = p } { j \neq i } } ^ { p + 2 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leq \theta \leqslant b .
$$

Therefore we seek the function $\{ u ( x ) ; a \leqslant x \leqslant b \}$ that minimizes the integral

$$
I ( u ) = \int _ { a } ^ { b } \left[ u ( x ) \right] ^ { 2 } \mathrm { d } x ,
$$

subject to the conditions

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) u ( \theta ) { \mathrm d } \theta = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 .
$$

If $\pmb { u }$ is not of the form

$$
u ( x ) = \sum _ { j = 1 } ^ { m - 2 } \lambda _ { j } B _ { j } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

then there is a function, $v$ say, that is orthogonal to the splines $\{ B _ { j } ; j =$ $1 , 2 , \ldots , m - 2 \}$ ，but that is not orthogonal to $\pmb { u }$ 、Hence the equations (23.8) hold if $\pmb { u }$ is replaced by $\left( u + \alpha v \right)$ , where $_ { \alpha }$ is any real number, but $_ \alpha$ can be chosen so that $I ( u + \alpha v )$ is less than $I ( u )$ . It follows that equation (23.9) is satisfied.

In order to calculate the values of the parameters $\left\{ \lambda _ { j } ; j = 1 , 2 , \ldots , \right.$ $m - 2 \}$ of expression (23.9),we note that the conditions (23.8) give a square system of linear equations in the parameters. If the matrix of the system is singular, then there exist numbers $\{ \mu _ { j } ; j = 1 , 2 , \ldots , m - 2 \}$ ,that are not al zero, such that the equations

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) \bigg [ \sum _ { j = 1 } ^ { m - 2 } \mu _ { j } B _ { j } ( \theta ) \bigg ] { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

hold. These equations, however, imply the identity

$$
\int _ { a } ^ { b } \left[ \sum _ { j = 1 } ^ { m - 2 } \mu _ { j } B _ { j } ( \theta ) \right] ^ { 2 } \mathrm { d } \theta = 0 ,
$$

which contradicts Theorem 19.2. Therefore the parameters of the function (23.9) are defined by the constraints (23.8).

The function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is obtained by integrating $\{ u ( x )$ ； $a \leqslant x \leqslant$ $b \}$ twice,where the constants of integration are chosen so that $\pmb { s } ( \pmb { x } _ { 1 } )$ and $\pmb { s } ( \pmb { x } _ { 2 } )$ are equal to $f ( { \pmb x } _ { 1 } )$ and $f ( x _ { 2 } )$ respectively.By applying the conditions (23.4) in sequence, it follows that the equations $\{ s ( x _ { p + 2 } ) = f ( x _ { p + 2 } ) ; p = 1$ ， $2 , \ldots , m - 2 \}$ are obtained. Hence $\pmb { s }$ is the function, interpolating the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ， that minimizes the integral (23.2). It is a cubic spline,because its second derivative is the continuous piecewise linear function (23.9). It is called a natural spline because it solves the variational problem of this section. The characteristic properties of natural cubic splines,which are implied by equation (23.9),are that their second derivatives are zero at $x _ { 1 }$ and $x _ { m }$ ,and that, if $x _ { 1 }$ and $x _ { m }$ are interior points of $[ a , b ] ,$ , then the cubic polynomial pieces degenerate to straight lines on each of the intervals $[ a , x _ { 1 } ]$ and $[ x _ { m } , b ]$

The degree of a natural spline is always odd. A spline $\pmb { s }$ of degree $( 2 k + 1 )$ on the interval $[ a , b ]$ is called a natural spline if it satisfies the conditions

$$
{ s } ^ { ( j ) } ( x _ { 1 } ) = { s } ^ { ( j ) } ( x _ { m } ) = 0 , \qquad k + 1 \leqslant j \leqslant 2 k ,
$$

where $x _ { 1 }$ and $x _ { m }$ are the extreme knots.Further, when $a < x _ { 1 }$ and when $x _ { m } < b$ ,then $\pmb { s }$ must be a polynomial of degree $k$ on the intervals $[ a , x _ { 1 } ]$ and $[ x _ { m } , b ]$ respectively.It is shown in the next section that natural splines give solutions to two variational problems.

If the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy condition (23.1),then the notation $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is used for the linear space of natural splines of degree $( 2 k + 1 )$ that have these points as knots: Sometimes we shorten the notation to $\mathcal { S } _ { \mathbf { N } }$ .It is proved in Theorem 23.1 that,if $m \geq k + 1$ , then the dimension of $\mathcal { S } _ { \mathbf { N } }$ is equal to $_ m$

# 23.2 Properties of natural splines

Natural spline approximations to functions are calculated by interpolation at the knots. The following theorem states that, except when $m \leqslant k$ ,the interpolation problem has a unique solution.

# Theorem 23.1

Let $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ be any set of real numbers that satisfy expression (23.1),and let $k$ be any integer in the range $[ 1 , m - 1 ]$ . Then, for any $f$ in $\mathcal { C } [ a , b ] ,$ ,there is exactly one function $\pmb { s }$ in the space $\mathcal { S } _ { \mathbf { N } } ( 2 k + 1 ,$ $x _ { 1 } , x _ { 2 } , \ldots , x _ { m } )$ that satisfies the interpolation conditions

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

Proof. If $\mathbf { \boldsymbol { a } } < \mathbf { \boldsymbol { x } } _ { 1 }$ , then the form of a natural spline on the interval $[ a , x _ { 1 } ]$ is defined uniquely by the form of the spline on $[ x _ { 1 } , x _ { 2 } ]$ A similar condition holds at the other end of the range $[ a , b ]$ . Therefore there is no loss of generality in assuming that $x _ { 1 } = a$ and $x _ { m } = b$ . It has been noted already that the dimension of the space $\mathcal { S } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . ~ , x _ { m } )$ of ordinary splines is equal to $( 2 k + m )$ . Natural splines, however,are splines that satisfy the linear homogeneous conditions (23.12)． Therefore the dimension of $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is not less than m. If the dimension exceeds $^ { m }$ ,then the equations

$$
\bar { s } ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m , \ldots \quad \bar { s } \in \mathcal { S } _ { \mathrm { N } } ,
$$

have a non-trivial solution. Therefore we ask whether these equations imply that $\bar { s }$ is the zero function.

We evaluate the integral

$$
I ( \bar { s } ^ { ( k + 1 ) } ) = \int _ { x _ { 1 } } ^ { x _ { m } } \left[ \bar { s } ^ { ( k + 1 ) } ( x ) \right] ^ { 2 } \mathrm { d } x
$$

by parts. It follows from conditions (23.12),from the fact that $\bar { s } ^ { ( 2 k + 1 ) }$ is constant on each of the intervals $\{ ( x _ { i } , x _ { i + 1 } ) ; i = 1 , 2 , . . . , m - 1 \}$ ,and from equation (23.14), that the integral has the value

$$
\begin{array} { l } { { I ( \bar { s } ^ { ( k + 1 ) } ) = ( - 1 ) ^ { k } \displaystyle \int _ { x _ { 1 } } ^ { x _ { m } } \bar { s } ^ { \prime } ( x ) \bar { s } ^ { ( 2 k + 1 ) } ( x ) \mathrm { d } x } } \\ { { \qquad = ( - 1 ) ^ { k } \displaystyle \sum _ { i = 1 } ^ { m - 1 } \bar { s } ^ { ( 2 k + 1 ) } ( x _ { i } + ) \displaystyle \int _ { x _ { i } } ^ { x _ { i + 1 } } \bar { s } ^ { \prime } ( x ) \mathrm { d } x } } \\ { { \qquad = ( - 1 ) ^ { k } \displaystyle \sum _ { i = 1 } ^ { m - 1 } \bar { s } ^ { ( 2 k + 1 ) } ( x _ { i } + ) [ \bar { s } ( x _ { i + 1 } ) - \bar { s } ( x _ { i } ) ] } } \\ { { \qquad = 0 , } } \end{array}
$$

where $x _ { i } +$ is any point in the interval $\left( x _ { i } , x _ { i + 1 } \right)$ .Therefore,because $\bar { s } ^ { ( k + 1 ) }$ is a continuous function,equations (23.15)and (23.16) imply that s(k+1) is identically zero.Hence $\bar { s }$ isin $\mathcal { P } _ { k }$ ，but $\bar { s }$ also satisfies the conditions (23.14). Thus, because $m \geq k + 1 , \mathrm { { : } }$ $\bar { s }$ is the zero function, which completes the proof that the dimension of the space $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is equal to $^ { m }$

We now know that the number of conditions (23.13) on $\pmb { S }$ is equal to the dimension of $\mathcal { S } _ { \mathbf { N } }$ . It follows from the method of proof of Theorem 5.4 that these conditions define $\pmb { s }$ uniquely,unless the equations (23.14) have a non-trivial solution. Because we have shown already that $\bar { s }$ can only be the zero function, the theorem is proved.□

The next theorem shows that interpolating natural splines are the solution to the kind of variational problem that is studied in Section 23.1.

# Theorem 23.2

Let the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , m \}$ be given, and let $k$ be an integer in $[ 1 , m - 1 ]$ The function $\pmb { s }$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ that minimizes the integral

$$
\int _ { a } ^ { b } [ s ^ { ( k + 1 ) } ( x ) ] ^ { 2 } { \mathrm { d } } x ,
$$

subject to the interpolation conditions (23.13), is the natural spline that is defined in Theorem 23.1.

Proof. We let $\pmb { s }$ be the natural spline that is the subject of Theorem 23.1, and we let $\pmb { g }$ be any function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ that interpolates the data. Hence the equations

$$
g ( x _ { i } ) - s ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m ,
$$

are satisfied. Because the definition of the 2-norm gives the identity

$$
\begin{array} { r } { \| g ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } = \big \| s ^ { ( k + 1 ) } \big \| _ { 2 } ^ { 2 } + \big \| g ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \big \| _ { 2 } ^ { 2 } + 2 \big ( g ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } , s ^ { ( k + 1 ) } \big ) , } \end{array}
$$

where the last term is twice the scalar product

$$
\int _ { a } ^ { b } \left[ g ^ { ( k + 1 ) } ( x ) - s ^ { ( k + 1 ) } ( x ) \right] s ^ { ( k + 1 ) } ( x ) \mathrm { d } x ,
$$

it is sufficient to show that this scalar product is zero. By applying integration by parts,by using the conditions

$$
s ^ { ( j ) } ( a ) = s ^ { ( j ) } ( b ) = 0 , \qquad k + 1 \leqslant j \leqslant 2 k ,
$$

which are obtained because $\pmb { s }$ is a natural spline,and by noting that $s ^ { ( 2 k + 1 ) } ( x )$ is zero if $x$ is in the interval $( a , x _ { 1 } )$ or $( x _ { m } , b )$ ,i folows that the integral (23.20) has the value

$$
( - 1 ) ^ { k } \int _ { x _ { 1 } } ^ { x _ { m } } \left[ g ^ { \prime } ( x ) - s ^ { \prime } ( x ) \right] s ^ { ( 2 k + 1 ) } ( x ) \mathrm { d } x .
$$

Therefore, because of condition (23.18), the method that gives the last three lines of expresson (23.16) implies also that the present integral is zero,which completes the proof of the theorem.□

One result that can be deduced from the proof is useful later. It is obtained from equation (23.19) and the fact that expression (23.20) is zero. It is that, if $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ and if $\pmb { s }$ is the natural spline that is defined in Theorem 23.1, then the identity

$$
\| f ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } = \| s ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } + \| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 }
$$

is satisfied.

The most remarkable property of natural splines is their relevance to an approximation problem that is mentioned in Section 22.3.In this problem a linear functional $L$ is estimated by the expression

$$
L ( f ) \approx \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) ,
$$

where the values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ are given,but the weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ have to be chosen. We recall that, if the estimate is to be exact when $f$ is in $\mathcal { P } _ { k }$ ,and if $^ { m }$ is much larger than $k$ ,then a suitable way of fixing the degrees of freedom in the weights is to minimize a norm of the kernel function

$$
K ( \theta ) = { \frac { 1 } { k ! } } { \bigg [ } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} - \sum _ { i = 1 } ^ { m } w _ { i } ( x _ { i } - \theta ) _ { + } ^ { k } { \bigg ] } , \qquad a \leqslant \theta \leqslant b ,
$$

of the relation

$$
L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

Natural splines give a direct and convenient method of calculating the approximation (23.24), when the weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ have the values that minimize the 2-norm

$$
\left\| K \right\| _ { 2 } = \bigg \{ \int _ { a } ^ { b } \left[ K \left( \theta \right) \right] ^ { 2 } \mathrm { d } \theta \bigg \} ^ { \frac { 1 } { 2 } } .
$$

The importance of natural splines to this calculation is shown usually by a detailed analysis of the conditions for the least value of $\| \pmb { K } \| _ { 2 }$ .However, because a similar analysis is given in Chapter 24,we prefer a different and much shorter approach, that depends on knowing that the required approximation to $L ( f )$ is $L ( s )$ , where $\pmb { s }$ is the natural spline that is defined in Theorem 23.1. This approximation does have the form (23.24), because,if the natural splines $\{ s _ { i } ; i = 1 , 2 , \ldots , m \}$ are the cardinal functions of the interpolation procedure of Theorem 23.1, then $\ b { L } ( s )$ is the expression

$$
\begin{array} { l } { { \displaystyle { \cal L } ( s ) = { \cal L } \bigg \{ \sum _ { i = 1 } ^ { m } f ( x _ { i } ) s _ { i } \bigg \} } } \\ { ~ } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } { \cal L } ( s _ { i } ) f ( x _ { i } ) } } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } \bar { w } _ { i } f ( x _ { i } ) } , } \end{array}
$$

say. We let $\{ { \bar { K } } ( \theta ) ; a \leqslant \theta \leqslant b \}$ be the kernel function that is obtained by seting $\left\{ w _ { i } = \bar { w } _ { i } ; i = 1 , 2 , \ldots , m \right\}$ in equation (23.25). The following theorem shows that $L ( s )$ is the required approximation.

# Theorem 23.3

Let $L$ be any linear functional from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to $\mathcal { R } ^ { 1 }$ ,and let $\bar { K }$ be the kernel function that has just been defined.Let expression (23.24) be any approximation to $L ( f )$ ,that is exact when $f$ is in $\mathcal { P } _ { k }$ . Then the norm of the kernel function (23.25)is bounded below by the inequality

$$
\| { \bar { K } } \| _ { 2 } \leqslant \| K \| _ { 2 } .
$$

Proof. Equation (23.26) implies the bound

$$
\bigg | L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant \| K \| _ { 2 } \| f ^ { ( k + 1 ) } \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] .
$$

By replacing $f \operatorname { \bf { b y } } f - s ,$ where $\pmb { s }$ is defined in Theorem 23.1, we obtain the relation

$$
{ \biggl | } L ( f ) - L ( s ) - \sum _ { i = 1 } ^ { m } w _ { i } [ f ( x _ { i } ) - s ( x _ { i } ) ] { \biggr | } \leqslant \| K \| _ { 2 } \| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 } .
$$

Because $\pmb { s }$ satisfies the interpolation conditions (23.13),and because equation (23.23） shows that $\| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 }$ is bounded above by $\| f ^ { ( k + 1 ) } \| _ { 2 }$ ,it follows thattheinequality

$$
\begin{array} { r } { \big \vert L ( f ) - L ( s ) \big \vert \leqslant \big \| K \big \| _ { 2 } \big \| f ^ { ( k + 1 ) } \big \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] , } \end{array}
$$

is satisfied. The proof is completed by making a particular choice of $f ,$ namely a function $\bar { f }$ such that $\bar { f } ^ { ( k + 1 ) }$ is equal to $\bar { \kappa } .$ Hence expressions (23.28) and (23.32) give the relation

$$
\left| L ( { \bar { f } } ) - \sum _ { i = 1 } ^ { m } { \bar { w } } _ { i } { \bar { f } } ( x _ { i } ) \right| \leqslant \| K \| _ { 2 } \| { \bar { K } } \| _ { 2 } .
$$

Because the kernel function $\bar { K }$ is defined by the equation

$$
L ( f ) - \sum _ { i = 1 } ^ { m } { \bar { w } } _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } { \bar { K } } ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] ,
$$

the choice of $\bar { f }$ implies the identity

$$
L ( \overline { { f } } ) - \sum _ { i = 1 } ^ { m } \bar { w } _ { i } \overline { { f } } ( x _ { i } ) = \| \bar { K } \| _ { 2 } ^ { 2 } .
$$

It follows from condition (23.33) that the theorem is true.[

If $c$ is any constant that can replace $\| \pmb { K } \| _ { 2 }$ in inequality (23.30), then $\| K \| _ { 2 }$ may be replaced by $^ c$ throughout the proof of the theorem. Therefore,for every set of weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ that allows an error bound of the form

$$
\bigg | L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant c \| f ^ { ( k + 1 ) } \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

the constant $^ { c }$ is not less than $\| \bar { K } \| _ { 2 }$ .Equation (23.34) shows that the least value $c = \| \bar { \pmb { K } } \| _ { 2 }$ is achieved when the weights have the values $\left\{ w _ { i } = \bar { w } _ { i } = \right.$ $L ( s _ { i } ) ; i = 1 , 2 , \ldots , m \}$ .Hence the approximation $\pmb { { \cal L } } ( \pmb { s } )$ to $L ( f )$ is the one that minimizes the constant $^ { c }$ of expression (23.36).

It is interesting that, if $L ( f )$ is the point function value $f ( \xi )$ ,where $\pmb { \xi }$ is any fixed point of $[ a , b ] ,$ ，then the estimate of $f ( \xi )$ that minimizes the right-hand side of expresson (23.36) is the same as the value at $\pmb { \xi }$ of the function that solves the variational problem of Theorem 23.2.The fact that these two different techniques give the same estimate of $f ( \xi )$ isa consequence of the dependence of the work of this section on the 2-norm of f(k+1）

# 23.3 Perfect splines

Perfect splines are obtained from a variational problem that is closely related to the one that is the subject of Theorem 23.2. The new variational problem is to calculate a function $\pmb { s }$ that minimizes $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ,$ subject to the interpolation conditions (23.3),where $m > k$ ,and where the abscissae of the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ satisfy expression (23.1). We consider this calculation,and we find that, at least on a part of the range $[ a , b ] , s$ is.a spline function of degree $( k + 1 )$

As in Section 23.1，divided differences are used to express the interpolationconditionsintermsof $\pmb { s } ^ { ( k + 1 ) }$ Therefore, leting $\{ z ( x ) = s ^ { ( k + 1 ) } ( x )$ ； $a \leqslant x \leqslant b \}$ ,the least value of the norm

$$
J ( z ) = \operatorname* { m a x } _ { a \leqslant x \leqslant b } { \left| z ( x ) \right| }
$$

is required, subject to the conditions

$$
\begin{array} { r l } {  { \int _ { a } ^ { b } B _ { p } ( \theta ) z ( \theta ) \mathrm { d } \theta = k ! f [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ] } } \\ & { \quad = c _ { p } , \qquad p = 1 , 2 , \ldots , m - k - 1 , } \end{array}
$$

say,where $\scriptstyle B _ { p }$ is the $\pmb { B }$ -spline that has the form (19.1O) and the knots $\{ x _ { j } ; j = p , p + 1 , \ldots , p + k + 1 \}$ . Expressions (23.37） and (23.38) correspond to equations (23.7) and (23.8).

Because there is an unknown function to be found, and because the number of constraints is finite, it is useful to apply duality theory to the calculation of $z$ .We note, therefore, that the constraints (23.38) imply that, for all values of the multipliers $\{ \lambda _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ the inequality

$$
\begin{array} { r } { \displaystyle \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } c _ { p } = \int _ { a } ^ { b } \left[ \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right] z ( \theta ) \mathrm { d } \theta } \\ { \displaystyle \leqslant \left\| z \right\| _ { \infty } \int _ { a } ^ { b } \left. \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right. \mathrm { d } \theta } \end{array}
$$

must hold,which gives the bound

$$
\left\| z \right\| _ { \infty } \geqslant \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } c _ { p } \bigg / \int _ { a } ^ { b } \left| \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right| \mathrm { d } \theta .
$$

Because the calculation of $z$ is a continuous version of a linear programming problem, it follows from the duality that necessary and sufficient conditions for $z$ to be optimal are that the constraints (23.38) are satisfied,and that there exist values of the parameters $\begin{array} { r } { \left\{ \lambda _ { p } ; p = 1 \right. } \end{array}$ ， $2 , \ldots , m - k - 1 \}$ such that inequality (23.40) becomes an equation. In this case the two lines of expression (23.39) are equal. Therefore, provided that equation (23.38) holds, the condition that characterizes the optimal $z$ is that there is a function

$$
\eta ( \theta ) = \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that is not identically zero, such that, if $\pmb \theta$ is any point of $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero, then $z ( \theta )$ has the value

$$
z \left( \theta \right) = \| z \| _ { \infty } \operatorname { s i g n } { \left[ \eta \left( \theta \right) \right] } .
$$

The following theorem gives a useful version of this result that depends on properties of $\pmb { B }$ -splines. In order to state the theorem, we require the definition of a ‘perfect spline'.

The function $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ on the interval $[ a , b ] ,$ if it is a spline of degree $( k + 1 )$ ,and if the constant sections of $\pmb { s } ^ { ( k + 1 ) }$ all have the same absolute value. Thus the equation

$$
{ \big | } s ^ { ( k + 1 ) } ( x ) { \big | } = \| s ^ { ( k + 1 ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b ,
$$

is satisfied, except perhaps at the knots of $\pmb { S } .$ If $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ , we adopt the convention that a point of $[ a , b ]$ is a knot of $\pmb { s }$ ， onlifitistetfetedf $\pmb { s } ^ { ( k + 1 ) }$ actually changes sign at the point. It is convenient sometimes,for example in the statement of Theorem 23.4, to call an element of $\mathcal { P } _ { k + 1 }$ a perfect spline of degree $( k + 1 )$

# Theorem 23.4

Let the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ be given, where the abscissae satisfy condition (23.1),and let $k$ be an integer in $[ 1 , m - 2 ]$ Let $\pmb { \mathcal { A } }$ be the set of functions that have bounded $( k + 1 )$ th derivatives,and that interpolate the data. The function $\pmb { s }$ in $\mathscr { A }$ gives the least value of the derivative norm $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; \boldsymbol { s } \in \mathcal { A } \big \}$ ,if andonlyifthereexistdata points $x _ { q }$ and $x _ { r } ,$ such that $r - q \geqslant k + 1$ ,and such that,on the interval $[ x _ { q } , x _ { r } ] _ { : }$ sisa perfect spline of degree $( k + 1 )$ that satisfies the following two conditions. The equation

$$
\begin{array} { r } { \big | s ^ { ( k + 1 ) } ( x ) \big | = \big \| s ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad x _ { q } < x < x _ { r } , } \end{array}
$$

holds,except perhaps at the knots of $\pmb { s }$ ,where the norm on the right-hand side refers to the whole interval $[ a , b ] ,$ and $\pmb { S }$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$

Proof. First we consider the case when $\pmb { s }$ minimizes $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; \boldsymbol { s } \in \mathcal { A } \big \}$ The function z = s(k+1) gives the least value of expression (23.37) subject to the constraints (23.38), because otherwise,if $\bar { z }$ is a solution to this optimization problem,then,by integrating $\bar { z } \ \left( k + 1 \right)$ times,as in the solution to the variational problem of Section 23.1, we obtain an element of $\mathscr { A }$ whose $( k + 1 ) \operatorname { t h }$ derivative is smaller than $s ^ { ( k + 1 ) }$ . It follows from the discussion at the beginning of this section that there is a function $\pmb { \eta }$ of the form (23.41), that is not identically zero, sich that, if $\pmb \theta$ is any point of $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero, then $z ( \theta )$ has the value (23.42). We let $x _ { 0 }$ and $x _ { m + 1 }$ be fixed points that are less than $x _ { 1 }$ and greater than $x _ { m }$ respectively,and, if necessary,we extend the definition (23.41） to the range $[ x _ { 0 } , x _ { m + 1 } ]$ .Hence there exist integers $\pmb q$ and $r$ in the interval $[ 1 , m ] ,$ such that $\pmb { \eta }$ has a finite number of zeros in the range $( x _ { q } , x _ { r } )$ ,but $\eta$ is identically zero on $[ x _ { q - 1 } , x _ { q } ]$ and $[ x _ { r } , x _ { r + 1 } ]$ .Because $z = s ^ { ( k + 1 ) }$ , it follows from equation (23.42) that $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ on the interval $[ x _ { q } , x _ { r } ] ,$ ,and that condition (23.44) is satisfied, except perhaps at the knots of $\pmb { S } ,$ ，Further,by applying Theorem 19.1 to $\pmb { \eta }$ ，the condition $r \geq ( q + k + 1 )$ holds,and the number of zeros of $\pmb { \eta }$ in $( x _ { q } , x _ { r } )$ is at most $( r - q - k - 1 )$ .Equation (23.42) shows that these zeros are the only points at which z = s(k+1) can change sign. Hence $\pmb { \mathscr { s } }$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$ , which completes one of the two parts of the proof.

To prove the second part of the theorem, we let $\pmb { s }$ be an element of $\mathcal { A }$ ， that is a perfect spline of degree $( k + 1 )$ on the interval $[ x _ { q } , x _ { r } ] ,$ ，where $r - q \geqslant k + 1$ ，where equation (23.44） holds,and where $\pmb { s }$ has at most $( r - q - k - 1 )$ knots in $( x _ { q } , x _ { r } )$ . We have to show that $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty }$ is as small as possible.It follows from the remarks on duality, that are made before the statement of the theorem, that it is sufficient to find a non-zero function of the form (23.41), such that equation (23.42) is satisfied if $\pmb { \eta } ( \pmb \theta )$ is nonzero, where $z$ is still the derivative $\pmb { s } ^ { ( k + 1 ) }$ The relation $\left| z ( \theta ) \right| = \left\| z \right\| _ { \infty }$ that is required by condition (23.42) is obtained from expression (23.44) by choosing $\pmb { \eta }$ so that $\pmb { \eta } ( \pmb \theta )$ is non-zero only if $\pmb \theta$ is in the interval $( x _ { q } , x _ { r } )$ Therefore we have to show that the sign of $\eta ( \theta )$ can satisfy equation (23.42).

There is no loss of generality in increasing the integer $q$ and in decreasing the integer $r$ ,until the difference $( r - q )$ is as small as possible, subject to the condition $r - q \geqslant k + 1$ , and subject to the number of knots of $\pmb { s }$ in $( x _ { q } , x _ { r } )$ being not more than $( r - q - k - 1 )$ . We assume that this is done. The number of knots is equal to $( r - q - k - 1 )$ ,because otherwise a further reduction in $\left( r - q \right)$ can be made. If the number of knots is zero, then $\boldsymbol { s } ^ { ( k + 1 ) } = \boldsymbol { z }$ is constant on the interval $( x _ { q } , x _ { r } )$ . Therefore the required sign of $\pmb { \eta }$ can be obtained by letting $\pmb { \eta }$ be a non-zero multiple of the $\pmb { B }$ -spline $\left\{ B _ { q } ( \vartheta ) ; a \leqslant \theta \leqslant b \right\}$ ,which has the form (23.41).Because $\eta ( \theta )$ is zero when $\pmb \theta$ is not in $( x _ { q } , x _ { r } )$ , the theorem is proved in the special case when $r - q = k + 1$

When $( r - q - k - 1 )$ is positive, we let the knots of $\pmb { s }$ in $( x _ { q } , x _ { r } )$ have the values $\{ \xi _ { j } ; j = q , q + 1 , \ldots , r - k - 2 \}$ .Because the assumption that is made in the previous paragraph prevents an increase in $q$ to $( j + 1 )$ ,where $j$ is any one of the integers $\{ q , q + 1 , \dots , r - k - 2 \}$ ,the spline $\pmb { s }$ has at least $( r - j - k - 1 )$ knots in $\left( x _ { j + 1 } , x _ { r } \right)$ .Hence the inequality $\xi _ { j } > x _ { j + 1 }$ is satisfied. By giving similar consideration also to the possibility of decreasing $r _ { \mathrm { { : } } }$ it follows that the bounds

$$
x _ { j + 1 } < \xi _ { j } < x _ { j + k + 1 } , \qquad j = q , q + 1 , \ldots , r - k - 2 ,
$$

are obtained. We require a function of the form

$$
\eta ( \theta ) = \sum _ { p = q } ^ { r - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that changes sign at the knots $\{ \xi _ { j } ; j = q , q + 1 , \ldots , r - k - 2 \}$ . Therefore it must satisfy the conditions

$$
\eta ( \xi _ { j } ) = 0 , \qquad j = q , q + 1 , \ldots , r - k - 2 ,
$$

where some or all of the parameters $\left\{ \lambda _ { p } ; p = q , q + 1 , \ldots , r - k - 1 \right\}$ are non-zero,which is possible because there are fewer conditions than parameters. Expression (23.45) is useful, for it implies that the knots $\{ \xi _ { j } ; j = q , q \ { \scriptscriptstyle \circ } \ i , \ldots , r - k - 2 \}$ are the only zeros of the function (23.46) in the interval $( x _ { q } , x _ { r } )$

In order to prove this statement, we suppose that $\pmb { \xi }$ is another zero, and we let $\{ \zeta _ { p } ; p = q , q + 1 , \ldots , r - k - 1 \}$ be the numbers $\pmb { \xi }$ and $\{ \xi _ { j } ; j = q ,$ $q + 1 , \ldots , r - k - 2 \}$ ，arranged in ascending order. It follows from expression (23.45） and from the form of $\pmb { B }$ -splines that the numbers $\{ B _ { p } ( \zeta _ { p } ) ; p = q , q + 1 , \ldots , r - k - 1 \}$ are all non-zero. Therefore Theorem 19.4 states that there is exactly one set of parameters $\{ \mu _ { p } ; p = q , q + 1$ ， $\ldots , r - k - 1 \}$ that satisfies the equations

$$
\sum _ { p = q } ^ { r - k - 1 } \mu _ { p } B _ { p } ( \zeta _ { j } ) = 0 , \qquad j = q , q + 1 , \ldots , r - k - 1 .
$$

This is a contradiction, because, in addition to the trivial solution $\{ \mu _ { p } =$ $0 ; p = q , q + 1 , \ldots , r - k - 1 \}$ ，the points $\{ \zeta _ { i } ; j = q , q + 1 , \ldots , r - k - 1 \}$ are all zeros of the function (23.46). Hence the zeros of $\pmb { \eta }$ in $( x _ { q } , x _ { r } )$ are just the points $\{ \xi _ { i } ; j = q , q + 1 , \ldots , r - k - 2 \}$

Finally, we have to show that $\pmb { \eta }$ changes sign at the zeros $\{ \xi _ { j } ; j = q , q + 1$ ， $\cdots , r - k - 2 \}$ . Because the work of the last paragraph rules out the possibility that $\pmb { \eta }$ is identically zero on a subinterval of $( x _ { q } , x _ { r } )$ ,and because $\pmb { \eta }$ has the form (23.46), the method of proof of Theorem 19.1 may be applied to $\pmb { \eta }$ on $[ x _ { q } , x _ { r } ]$ .Hence the total number of zeros inside the interval does not exceed $( r - q - k - 1 )$ ,even if zeros at which $\pmb { \eta }$ does not change sign are counted twice. It follows that the points $\{ \xi _ { j } ; j = q ,$ $q + 1 , \ldots , r - k - 2 \}$ are all simple zeros.Hence,in $( x _ { q } , x _ { r } )$ ，the sign changes of the function (23.46) occur at the same points as the sign changes of $\pmb { s } ^ { ( k + 1 ) }$ .Therefore,because $\pmb { \eta }$ is identically zero outside $( x _ { q } , x _ { r } )$ ， and because equation (23.44) is satisfied, it is possible to choose $\pmb { \eta }$ so that condition (23.42) is obtained for all values of $\pmb \theta$ in $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero.The theorem is proved.□

Although the variational problem of Theorem 23.2 always has a unique solution, there can be many functions $\pmb { s }$ in the set $\mathcal { A }$ of Theorem 23.4 that minimize $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty }$ . For example, if $k = 0$ , and if the data have the values that are shown by the small circles in Figure 23.1,then both the dashed and the solid lines of the figure minimize $\| s ^ { \prime } \| _ { \infty }$ ,where the two lines coincide between the third and fourth data points. The solid line shows the only perfect spline of degree one on the interval $[ x _ { 1 } , x _ { m } ] ;$ , that solves the variational problem and that has not more than $( m - 2 )$ krots.

More generally, if $k \geqslant 0$ ,if $m \geq k + 2$ ,and if condition (23.1) is satisfied, there is a perfect spline of degree $( k + 1 )$ on the full range $[ a , b ]$ ，that interpolates the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , m \}$ ,and that has not more than $( m - k - 2 )$ knots. Theorem 23.4 states that this perfect spline minimizes $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; s \in \mathcal { A } \big \}$ . References to proofs of the existence of the perfect spline are given in Appendix B.A condition for uniqueness is the subject ofExercise 23.10.

A strong disadvantage of using a perfect spline of degree $( k + 1 )$ to approximate a function $f$ in $\mathcal { C } [ a , b ]$ is that, if it is necessary for the $( k { + } 1 )$ th derivative of the spline to be large on a part of $[ a , b ] ,$ then, by the definition of a perfect spline, the derivative is large throughout the range. This disadvantage is shown in Figure 23.1. However， some of the theoretical properties of perfect splines are useful. In particular they give error bounds on the interpolation method that is considered in the next chapter.

# 23 Exercises

23.1 Prove that, if $f$ is a function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ that has the values $f ( 0 ) = 0 , f ( \textstyle { \frac { 1 } { 2 } } ) = 1$ and $f ( 1 ) = 1$ , then the inequality

$$
\int _ { 0 } ^ { 1 } { [ f ^ { \prime \prime } ( x ) ] ^ { 2 } } \mathrm { d } x \geqslant 1 2
$$

holds.

23.2 Let the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy condition (19.1),and let $f$ be a function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ Prove that there is a spline, $s ^ { * }$ say， in the space $\mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . ~ . ~ . , \xi _ { n } )$ that satisfies the equations $\{ s ^ { * } ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \}$ $\{ s ^ { * ^ { ( j ) } } ( a ) = f ^ { ( j ) } ( a ) ; j = 1 , 2 , \ldots , k \} _ { \mathrm { \scriptsize {  } } }$ and $\{ s ^ { * ( j ) } ( b ) = f ^ { ( j ) } ( b ) ; j = 1 , 2 , \ldots , k \}$ Prove also that $s ^ { * }$ minimizes the integral

![](images/9188c47b2308605878f1264b8ed58c6fb043d777d330d280efb0f25f4625ba64.jpg)  
Figure 23.1. Two solutions to a variational problem.

$$
\int _ { a } ^ { b } \left[ f ^ { ( k + 1 ) } ( x ) - s ^ { ( k + 1 ) } ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad s \in \mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . . . , \xi _ { n } ) .
$$

23.3 Verify that the coefficients $w _ { 0 } , w _ { 1 }$ and $w _ { 3 }$ that solve Exercise 22.3 are such that $\left[ w _ { 0 } f ( 0 ) + w _ { 1 } f ( 1 ) + w _ { 3 } f ( 3 ) \right]$ is the value at $\scriptstyle x = 2$ of the natural cubic spline that interpolates $f ( 0 ) , f ( 1 )$ and $f ( 3 )$

23.4 Let $f$ be a function in $\mathcal { C } ^ { ( 3 ) } [ - 2 , 2 ]$ that has the values $f ( - 2 ) =$ $f ( - 1 ) = f ( 1 ) = f ( 2 ) = 0$ and $f ( 0 ) = 1$ . Show that the inequality $\| f ^ { \prime \prime \prime } \| _ { \infty } \geqslant 4 . 5$ is satisfied. If it is known also that $f ^ { \prime } ( - 2 ) = f ^ { \prime } ( 2 ) = 0 { \mathrm { . } }$ ， show that the lower bound on $\| f ^ { \prime \prime \prime } \| _ { \infty }$ may be increased to 6.425 ...,which is the number $( 2 3 1 + 9 \sqrt { 3 3 } ) / 4 4$

23.5 Let $m = 4$ and $k = 1$ in the statement of Theorem 23.4,and let $s ^ { * }$ be the function in $\mathcal { A }$ that minimizes $\big \{ \big \| \boldsymbol { s } ^ { \prime \prime } \big \| _ { \infty } ; s \in \mathcal { A } \big \}$ . Prove that the inequality

$$
{ \| s ^ { * } \prime \prime \| _ { \infty } } { \leqslant } 4 \operatorname* { m a x } { \{ \left| f [ x _ { 1 } , x _ { 2 } , x _ { 3 } ] \right| , \left| f [ x _ { 2 } , x _ { 3 } , x _ { 4 } ] \right| \} }
$$

holds,and that, if $f$ can be any function in $\mathcal { C } [ a , b ] ,$ ，then the constant 4 on the right-hand side cannot be replaced by a smaller number.

Calculate the function $\pmb { s }$ in $\mathcal { C } [ 0 , 2 ]$ that minimizes the integral

$$
\int _ { 0 } ^ { 2 } \{ [ s ^ { \prime \prime } ( x ) ] ^ { 2 } / ( 1 + x ) \} \mathrm { d } x ,
$$

subject to the conditions $s ( 0 ) = 0 , s ( 1 ) = 0$ and $s ( 2 ) = 1 6$ .You should find the piecewise polynomial

$$
s ( x ) = { \Big \{ } _ { 6 - 1 9 x + 1 2 x ^ { 2 } + 2 x ^ { 3 } - x ^ { 4 } , 1 \leqslant x \leqslant 2 . } ^ { - 3 x }  ^ { - 3 x } \qquad \leqslant x \leqslant 1 .
$$

23.7 Let $\pmb { \sigma }$ be the spline in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that minimizes the integral

$$
\| g - s \| _ { 2 } ^ { 2 } = \int _ { a } ^ { b } \left[ g ( x ) - s ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad s \in \mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } ) ,
$$

where inequality (19.1) holds,and where $\pmb { g }$ is any fixed function in $\mathcal { C } [ a , b ]$ .If $f$ is a $( k + 1 )$ -fold integral of $\pmb { g } .$ and if $s ^ { * }$ is the spline in $\mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . ~ . ~ . , \xi _ { n } )$ that is defined in Exercise 23.2, then $\pmb { \sigma }$ is equal to $\pmb { s } ^ { * ( k + 1 ) }$ . Prove that,if it isnot possible toreduce the error $\| g - \sigma \| _ { 2 }$ by altering the positions of the interior knots $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ ,then,not only does $s ^ { * }$ satisfy the equations of Exercise 23.2，but also the derivative conditions $\{ s ^ { * } { } ^ { \prime } ( \xi _ { i } ) = f ^ { \prime } ( \xi _ { i } ) ; i = 1 , 2 , . . . , n - 1 \}$ are obtained.

23.8Let the points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ of the quadrature formula

$$
\int _ { x _ { 0 } } ^ { x _ { n } } f ( x ) { \mathrm { d } } x \approx \sum _ { i = 0 } ^ { n } w _ { i } f ( x _ { i } ) , \qquad f \in \mathcal { C } ^ { ( 2 ) } [ x _ { 0 } , x _ { n } ] ,
$$

satisfy the conditions $\{ x _ { i } = x _ { 0 } + i h ; i = 1 , 2 , \dots , n \}$ ，and let the weights $\{ w _ { i } ; i = 0 , 1 , \ldots , n \}$ have the values that minimize the multiple of $\left\| f ^ { \prime \prime } \right\| _ { 2 }$ that bounds the error of the quadrature formula. Show that $w _ { 0 } = w _ { n }$ ,and that the equations

$$
w _ { i } = h [ 1 + \beta ( \sqrt { 3 - 2 } ) ^ { i } + \beta ( \sqrt { 3 - 2 } ) ^ { n - i } ] , \qquad i = 1 , 2 , \ldots , n - 1 ,
$$

are obtained, where $\beta$ is a number that does not depend on $i ,$

23.9 Prove the necessary and sufficient conditions that are stated in the sentence that follows inequality (23.40).

.10Let the conditions of Theorem 23.4 be satisfied,and let $\bar { \mathcal { A } }$ be the set of perfect splines of degree $( k + 1 )$ on the full range $[ a , b ]$ ,that interpolate the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ，and that have not more than $( m - k - 2 )$ knots. Let $\bar { s }$ be an element of $\{ { \bar { \alpha } } ,$ let $z$ be the derivative s(k+1), ，and let the function (23.41） have the property that equation (23.42) is satisfied for all points $\pmb \theta$ in $[ a , b ]$ at which $\eta ( \theta )$ is non-zero.Prove that,if $\pmb { \eta }$ has only a finite number of zeros in $[ a , b ] ,$ ,then $\bar { s }$ is the only element of $\boldsymbol { \bar { \mathcal { A } } } .$ Express this condition as a relation between the knots of $\bar { s }$ and the positions of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ . Investigate relations between the knots of $\pmb { \bar { s } }$ and the data points that allow $\bar { \mathcal { A } }$ to contain more than one element.

# Optimal interpolation

# 24.1 The optimal interpolation problem

If one is given many values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ of a function $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ if it is known that $\| f ^ { ( k + 1 ) } \| _ { \infty }$ is not very large,and if an estimate of $f ( \xi )$ is required, where $\xi$ is any point of $[ a , b ] ,$ , then one may make an approximation of the form

$$
f ( \xi ) \approx \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) ,
$$

where the multipliers $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ are such that the approximation is exact when $f$ is in $\mathcal { P } _ { k }$ . In this case the Peano kernel theorem shows that there is a number $^ c$ ,that is independent of $f ,$ such that the bound

$$
\bigg | f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant c \big \| f ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

is satisfied. When $m > k + 1$ ,there is some freedom in the values of the multipliers. If this freedom is used to minimize $^ c$ ，the approximation (24.1) is said to be ‘optimal'. We reserve the notation $\{ w _ { i } ( \pmb { \xi } ) ; i = 1$ ,2, $\cdots , m \}$ for the optimal multipliers, we let $s ( \xi )$ be the optimal estimate

$$
s ( \xi ) = \sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) f ( x _ { i } ) , \qquad a \leqslant \xi \leqslant b ,
$$

of $f ( \xi )$ ，and we let $c ( \xi )$ be the least value of $c$ 、We find later that the optimal multipliers are unique for each $\xi .$

Because the optimal interpolation procedure can be applied for all values of $\xi \mathrm { i n } [ a , b ] ,$ ,the function (24.3) can be regarded as an approximation to the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ .It is shown in Section 24.3 that this approximation is a spline of degree $k$ that has $( m - k - 1 )$ knots whose positions are independent of $f .$ It is highly satisfactory that $\pmb { s }$ is a spline of the lowest degree that is allowed by an error bound of the form (24.2).We recall,however, that natural splines that are obtained by minimizing the number $\boldsymbol { c } _ { 2 }$ in the bound

$$
{ \biggl | } f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) { \biggr | } \leqslant c _ { 2 } \| f ^ { ( k + 1 ) } \| _ { 2 }
$$

are less convenient, because they are of degree $( 2 k + 1 )$ ,and because their end conditions force errors to occur when $f$ is in $\mathscr { P } _ { 2 k + 1 }$ but not in $\mathcal { P } _ { k }$ ·

Another remark that we recall from Section 23.2 is that the minimization of $c _ { 2 }$ gives the same estimate of $f ( \xi )$ as the solution to the variational problem of Theorem 23.2.If an analogous result were true when $\| f ^ { ( k + 1 ) } \| _ { 2 }$ is replaced by $\| f ^ { ( k + 1 ) } \| _ { \infty }$ , then,by Theorem 23.4,the function (24.3) would be a perfect spline of degree $( k + 1 )$ on a subinterval of $[ a , b ] _ { \mathrm { : } }$ ，but the degree of $\pmb { s }$ is only $k$ .Nevertheless, the properties of perfect splines are important to optimal interpolation.In particular, it willbe shown that the function $\{ c ( \pmb { \xi } )$ ； $a \leqslant \xi \leqslant b \}$ is the modulus of a perfect spline of degree $( k + 1 )$

When $\pmb { \xi }$ is a variable whose range is $[ a , b ] ,$ ,then the functions $\{ w _ { i } ; i = 1$ ， $2 , \ldots , m \}$ in expression (24.3) are the cardinal functions of the optimal interpolation procedure. We have called $w _ { i } ( \xi )$ a multiplier, however, instead of a cardinal function, because, from now until the beginning of Section $2 4 . 3 , \xi$ is treated as a fixed point of $[ a , b ]$ .The main properties of optimal interpolation are derived from the following theorem.

# Theorem 24.1

Let the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy the conditions

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b ,
$$

let $\xi$ be any point of $[ a , b ] ,$ and let $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ be multipliers, such that the estimate (24.1) is exact when $f$ is in $\mathcal { P } _ { k }$ .Let $\pmb { K }$ be the kernel function

$$
K ( \theta ) = \frac { 1 } { k ! } \Bigl [ ( \xi - \theta ) _ { + } ^ { k } - \sum _ { i = 1 } ^ { m } w _ { i } ( x _ { i } - \theta ) _ { + } ^ { k } \Bigr ] , \qquad a \leqslant \theta \leqslant b .
$$

Then the multipliers have the values that minimize the constant $^ c$ in inequality (24.2),if and only if they minimize the norm

$$
\| K \| _ { 1 } = \int _ { a } ^ { b } \left| K ( \theta ) \right| \mathrm { d } \theta .
$$

Proof.Theorem 22.1 implies the equation

$$
f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

Hence,for any particular choice of the multipliers,the least constant $c$ in inequality (24.2) has the value (24.7). It follows that the problems of choosing the multipliers to minimize $c$ and to minimize $\left\| K \right\| _ { 1 }$ are equivalent.□

In order to minimize $\left\| K \right\| _ { 1 }$ , we make use of an idea that is given in Chapter 22. It is to express the approximation (24.1) in the form

$$
f ( \xi ) \approx \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) + \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } f [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ] ,
$$

where $f [ x _ { p } , x _ { p + 1 } , \dotsc , x _ { p + k + 1 } ]$ is a divided difference. This approximation is exact when $f$ is in $\mathcal { P } _ { k }$ , if and only if the coefficients $\{ u _ { i } ; i = 1 , 2 , \ldots ,$ $k + 1 \}$ satisfy the condition

$$
f ( \xi ) = \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) , \qquad f \in \mathcal { P } _ { k } .
$$

Because the right-hand side of this condition can only be the value at $\xi$ of the polynomial in $\mathcal { P } _ { k }$ that interpolates the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , k + 1 \} _ { } ,$ it follows that, as in equation (22.43),the identity

$$
f ( \xi ) - \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } { ( \xi - x _ { i } ) \bigg \} } f [ x _ { 1 } , x _ { 2 } , \ldots , x _ { k + 1 } , \xi ]
$$

holds for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .Therefore the error of the estimate (24.9) is the expression

$$
\begin{array} { r l r } {  { \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} f [ x _ { 1 } , x _ { 2 } , \dots , x _ { k + 1 } , \xi ] } } \\ & { } & { - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } f [ x _ { p } , x _ { p + 1 } , \dots , x _ { p + k + 1 } ] . } \end{array}
$$

Theorem 22.3 shows that, when $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ this expression may be written in the form

$$
\frac { 1 } { k ! } \int _ { a } ^ { b } \bigg [ \bigg \{ \prod _ { i = 1 } ^ { k + 1 } \left( \xi - x _ { i } \right) \bigg \} B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \theta ) \bigg ] f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta ,
$$

where the knots of the $B$ -splines are the arguments of the corresponding divided differences.It follows from Theorem 24.1 that the approximation (24.9) is the optimal interpolation formula, if and only if the coefficients $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ minimize the norm

$$
\int _ { a } ^ { b } | { \Big \{ } \prod _ { i = 1 } ^ { k + 1 } { ( \xi - x _ { i } ) } { \Big \} } B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \theta ) { \Big | } \ \mathbf { d } \theta .
$$

Thus the optimal interpolation problem is equivalent to calculating the best $L _ { 1 }$ approximation to the function $\left\{ B ( \theta ) ; \ a \leqslant \theta \leqslant b \right\}$ by a linear combination of the $B$ -splines $\{ B _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \} .$

# $2 4 . 2 \ L _ { 1 }$ approximation by $\pmb { B }$ -splines

The main result of this section is that the required parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ in expression (24.14） are defined by the linear equations

$$
\sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \xi _ { j } ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} B ( \xi _ { j } ) , \qquad j = 1 , 2 , \ldots , m - k - 1 ,
$$

where the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are independent of $\xi .$ The result is a corollary of Theorem 14.4, but this theorem requires the set of approximating functions to be a Chebyshev set. Therefore it is necessary to show that the $B$ -splines $\{ B _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are sufficiently close to a Chebyshev set for Theorem 14.4 to be useful.

# Theorem 24.2

Let $k$ and $_ { m }$ be positive integers such that $m > k + 1$ , let the points $\{ x _ { i } ; \ i = 1 , 2 , \dots , m \}$ satisfy condition (24.5)，and for $1 \leqslant p \leqslant$ $m - k - 1$ let $\scriptstyle B _ { p }$ be the $\pmb { B }$ -spline

$$
B _ { p } ( \theta ) = \sum _ { i = p } ^ { p + k + 1 } \bigg \{ ( \theta - x _ { i } ) _ { + } ^ { k } \bigg / \prod _ { \stackrel { j = p } { j \neq i } } ^ { p + k + 1 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leqslant \theta \leqslant b .
$$

For any $\varepsilon > 0$ ,there exists a Chebyshev set of functions $\{ \phi _ { p } ; p = 1 , 2 $ $\ldots , m - k - 1 \}$ such that the inequalities

$$
\| B _ { p } - \phi _ { p } \| _ { \infty } \leqslant \varepsilon , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

hold.

Pro0f. Let $q = m - k - 1$ , and let $\psi$ be the function

$$
\psi ( \alpha ) = M \mathrm { e } ^ { - \pi M ^ { 2 } \alpha ^ { 2 } } , \qquad - \infty < \alpha < \infty ,
$$

where $M$ is a parameter. For $p = 1 , 2 , \ldots , q ;$ we let $\phi _ { p }$ have the form

$$
\phi _ { p } ( \theta ) = \int _ { - \infty } ^ { \infty } \psi ( \alpha - \theta ) B _ { p } ( \alpha ) \mathrm { d } \alpha , \qquad a \leqslant \theta \leqslant b ,
$$

where $B _ { p } ( \alpha )$ is zero if $\pmb { \alpha }$ is outside $[ a , b ]$ .Because the area under the curve $\{ \psi ( \alpha ) ; - \infty < \alpha < \infty \}$ is one, because $\psi$ tends to a delta function as $M$ tends to infinity,and because the functions $\{ B _ { p } ; p = 1 , 2 , \ldots , q \}$ are continuous and bounded,we can choose $M$ to be so large that the conditions (24.17) are satisfied for any fixed positive value of $\pmb \varepsilon$ .Therefore it is sufficient to prove that the set $\{ \phi _ { p } ; p = 1 , 2 , \ldots , q \}$ is a Chebyshev set. We show that property (4) of Section 7.3 is obtained,which is that, if the numbers $\{ \theta _ { j } ; j = 1 , 2 , \ldots , q \}$ satisfy the inequalities

$$
a \leqslant \theta _ { 1 } < \theta _ { 2 } < . . . < \theta _ { q } \leqslant b ,
$$

then the $q \times q$ matrix $\pmb { A }$ ,whose elements have the values $A _ { p j } = \phi _ { p } ( \theta _ { j } )$ ,is non-singular.

Because $B _ { p } ( \alpha )$ is zero unless $_ \alpha$ is in the interval $( a , b )$ , the matrix $\pmb { A }$ has the form

$$
\begin{array}{c} \begin{array} { r l } {  \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 1 } - \theta _ { 1 } ) B _ { 1 } ( \alpha _ { 1 } ) \mathrm { d } \alpha _ { 1 }  } & { \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 2 } - \theta _ { 2 } ) B _ { 1 } ( \alpha _ { 2 } ) \mathrm { d } \alpha _ { 2 } . . . } \\ {  \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 1 } - \theta _ { 1 } ) B _ { 2 } ( \alpha _ { 1 } ) \mathrm { d } \alpha _ { 1 }  } & { \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 2 } - \theta _ { 2 } ) B _ { 2 } ( \alpha _ { 2 } ) \mathrm { d } \alpha _ { 2 } . . . } \\ { \vdots } & { \vdots } \end{array} ) .  \end{array}
$$

We consider the value of its determinant. If all of the columns of $\pmb { A }$ are fixed except for the jth column, then the determinant is a linear functional of the jth column.It follows that the integral over $\alpha _ { j }$ can be taken outside the determinant, and this can be done for each $j .$ Hence we obtain the identity

$$
\operatorname* { d e t } A = \int _ { a } ^ { b } \cdot \cdot \cdot \int _ { a } ^ { b } \bigg \{ \prod _ { j = 1 } ^ { q } \psi ( \alpha _ { j } - \theta _ { j } ) \bigg \} \operatorname* { d e t } H \mathrm { d } \alpha _ { 1 }  \cdot \cdot \cdot \mathrm { d } \alpha _ { q } ,
$$

where $H$ is the $q \times q$ matrix whose elements are $H _ { p j } = B _ { p } ( \alpha _ { j } )$ .Because the numbers $\{ \psi ( \alpha _ { j } - \theta _ { j } ) ; j = 1 , 2 , \ldots , q \}$ are all positive,and because det $\pmb { H }$ is a continuous function of the variables $\{ \alpha _ { j } ; j = 1 , 2 , \ldots , q \}$ ,it is sufficient to prove that det $\pmb { H }$ is not identically zero and does not change sign in the range of integration of expression (24.22).

The matrix $H$ is similar to the one that occurs in the linear system of equations (19.37) of the Schoenberg-Whitney theorem. It follows from the proof of Theorem 19.4 that det $H ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { q } )$ is non-zero if and only if the numbers $\{ B _ { p } ( \alpha _ { p } )$ ； $p = 1 , 2 , \ldots , q \}$ are all positive. If det $H ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { q } )$ is positive, but det $H ( \beta _ { 1 } , \beta _ { 2 } , \dots , \beta _ { q } )$ is negative, then，by continuity， there exists a number $r$ in [O,1] such that det $H ( \gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { q } )$ is zero， where $\begin{array} { r } { \{ \gamma _ { p } = r \alpha _ { p } + ( 1 - r ) \beta _ { p } } \end{array}$ ； $p = 1$ ,2, $\cdots , q \}$ . However, because $B _ { p } ( \alpha _ { p } )$ and $B _ { p } ( \beta _ { p } )$ are both positive,and because $\scriptstyle B _ { p }$ is a $\pmb { B }$ -spline, the number $B _ { p } ( \gamma _ { p } )$ must also be positive for $p = 1 , 2 , \ldots , q ;$ ，which gives a contradiction. Hence det $\pmb { H }$ does not change sign in the range of the integral (24.22). The theorem is proved.□

In order to apply Theorem 14.4 to the minimization of expression (24.14), we let $\xi$ be a point of $[ a , b ]$ that is not in the set $\left\{ x _ { i } ; ~ i = \right.$

$1 , 2 , \ldots , m \}$ ，we let $M$ be a large number,we define the functions $\{ \phi _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ by equation (24.19), and we let $\phi$ be the function

$$
\phi \left( \theta \right) = \int _ { a } ^ { b } \psi ( \alpha - \theta ) ~ B \left( \alpha \right) \mathrm { d } \alpha , \qquad a \leqslant \theta \leqslant b .
$$

By inserting $\xi$ into the sequence $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ，it follows from Theorem 24.2 that the linear space that is spanned by the functions $\phi$ and $\{ \phi _ { p } ; ~ p = 1 , 2 , \ldots , m - k - 1 \}$ satisfies the Haar condition. We deduce from Theorem 14.4 that there exist points $\{ \xi _ { j } ( M ) ; j = 1 , 2 , \ldots ,$ $m - k - 1 \}$ ,that are independent of $\xi ,$ such that a necessary and sufficient condition for the coeffcients $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ to minimize the norm

$$
\int _ { a } ^ { b } | { \Big \{ } \prod _ { i = 1 } ^ { k + 1 } { \big ( } \xi - x _ { i } { \big ) } { \Bigg \} } \phi ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \phi _ { p } ( \theta ) { \Bigg | } \ \mathrm { d } \theta
$$

is that the interpolation conditions

$$
\sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \phi _ { p } ( \xi _ { j } [ M ] ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} \phi ( \xi _ { j } [ M ] ) ,
$$

$$
j = 1 , 2 , \ldots , m - k - 1 ,
$$

are satisfied. Because $\{ \phi _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ and $\phi$ tend to $\{ B _ { p } ; p =$ $1 , 2 , \ldots , m - k - 1 \}$ and $\pmb { B }$ respectively as $M$ tends to infinity, it seems to be appropriate to let the interpolation points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ of equation (24.15) be a limit of the set $\{ \xi _ { j } ( M ) ; j = 1 , 2 , \ldots , m - k - 1 \}$ as $M$ becomes large, where the inequalities

$$
a \leqslant \xi _ { 1 } ( M ) < \xi _ { 2 } ( M ) < \ldots < \xi _ { m - k - 1 } ( M ) \leqslant b
$$

hold.The remainder of this section shows that it is suitable to define the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ in this way. First it is proved that the matrix of the system of equations (24.15) is non-singular.

# Theorem 24.3

Let the conditions of Theorem 24.2 hold, let $\{ M _ { t } ; t = 1 , 2 , 3 , . . . \}$ be a monotonically increasing divergent sequence of positive real numbers,and let $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ be a limit of the sequence of sets $[ \{ \xi _ { j } ( M _ { t } ) ; j = 1 , 2 , \ldots , m - k - 1 \} ;$ $t = 1 , 2 , 3 , \ldots ] ,$ ,where the numbers $\{ \xi _ { j } ( M _ { t } ) ; j = 1 , 2 , \ldots , m - k - 1 \}$ have just been defined.Then the numbers $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are all different, and they satisfy the conditions

$$
x _ { j } < \xi _ { j } < x _ { j + k + 1 } , \qquad j = 1 , 2 , \ldots , m - k - 1 .
$$

Proof. Let $M$ be any positive number,for $1 \leqslant p \leqslant m - k - 1$ let $\phi _ { p }$ be the function (24.19),and let $z _ { M }$ be the sign function

$$
z _ { M } ( \theta ) = \left\{ \begin{array} { l l } { { 1 , ~ } } & { { a \leqslant \theta < \xi _ { 1 } ( M ) } } \\ { { ( - 1 ) ^ { j } , ~ } } & { { \xi _ { j } ( M ) < \theta < \xi _ { j + 1 } ( M ) , ~ 1 \leqslant j \leqslant m - k - 2 ~ } } \\ { { ( - 1 ) ^ { m - k - 1 } , ~ } } & { { \xi _ { m - k - 1 } ( M ) < \theta \leqslant b } } \\ { { 0 , ~ } } & { { \mathrm { o t h e r w i s e } . } } \end{array} \right.
$$

Theorems 14.1, 14.4 and 24.2 imply that the equations

$$
\int _ { a } ^ { b } z _ { M } ( \theta ) \phi _ { p } ( \theta ) { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

hold.By taking the limit as $M$ tends to infinity,it follows that the conditions

$$
\int _ { a } ^ { b } z ( \theta ) B _ { p } ( \theta ) { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

are obtained,where $z$ is the function

$$
z \left( \theta \right) = \left\{ \begin{array} { l l } { 1 , \qquad a \leqslant \theta < \xi _ { 1 } } \\ { ( - 1 ) ^ { i } , \qquad \xi _ { j } < \theta < \xi _ { j + 1 } , \qquad 1 \leqslant j \leqslant m - k - 2 } \\ { ( - 1 ) ^ { m - k - 1 } , \qquad \xi _ { m - k - 1 } < \theta \leqslant b } \\ { 0 , \qquad \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

We let $\sigma$ be a perfect spline of degree $( k + 1 )$ that satisfies the equation

$$
\sigma ^ { ( k + 1 ) } ( \theta ) = z ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

except perhaps when $\pmb \theta$ is in the set $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \} .$

The notation $z$ is chosen for the $( k + 1 ) \mathrm { t h }$ derivative of the perfect spline,in order to make use of the second half of the proof of Theorem 23.4. This proof shows that, if there are data points $x _ { q }$ and $x _ { r }$ such that $r - q \geqslant k + 1$ , and such that $\sigma$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$ , then there is a function of the form

$$
\eta ( \theta ) = \sum _ { p = q } ^ { r - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that is not identically zero,and that has the property that equation (23.42) holds when $\pmb { \eta } ( \pmb \theta )$ is non-zero. Hence the inequality

$$
{ \int _ { a } ^ { b } z ( \theta ) \eta ( \theta ) \operatorname { d } \theta } = { \int _ { a } ^ { b } \left| \eta ( \theta ) \right| \operatorname { d } \theta }
$$

is obtained. This inequality, however, contradicts equations (24.30) and (24.33).Hence there is a relation between the knots of $\sigma$ and the positions of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ,which we find is sufficient to complete the proof.

Specifically, because of the possibility that $q = 1$ and $r = m$ , the spline $\sigma$ must have more than $( m - k - 2 )$ knots,which proves that the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are all different. Moreover, if there is an integer $j$ in the range[1, $m - k - 1 ]$ such that $\xi _ { j } \leqslant x _ { j } ,$ then letting $q = j$ and $r = m$ also gives a contradiction. Similarly，by letting $q = 1$ and $r =$ $j + k + 1$ , there is a contradiction if $\pmb { \xi } _ { j } \geq \pmb { x } _ { j + k + 1 }$ .Hence inequality (24.27) is satisfied. The proof is complete.□

We let the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ satisfy the conditions of Theorem 24.3.It follows from Theorem 19.4 that the system of equations (24.15) defines the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ uniquely. We have to show that these parameters are the ones that minimize $\| K \| _ { 1 }$ ， where $\kappa$ is the kernel function

$$
K ( \theta ) = \frac { 1 } { k ! } \biggl [ \Bigl \{ \prod _ { i = 1 } ^ { k + 1 } \left( \xi - x _ { i } \right) \Bigr \} B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \ B _ { p } ( \theta ) \biggr ] , \qquad a \leqslant \theta
$$

Theorem 14.1 states that it is sufficient to prove that,for any values of the parameters $\{ \lambda _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ ,the function

$$
\eta ( \theta ) = \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } \ B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

satisfies the inequality

$$
\left| \int _ { a } ^ { b } t ( \theta ) \eta ( \theta ) { \bf d } \theta \right| \leqslant \int _ { \mathcal { Z } } \left| \eta ( \theta ) \right| { \bf d } \theta ,
$$

where $t$ is the sign function

$$
t ( \theta ) = \left\{ \begin{array} { r l } { 1 , \quad } & { { } K ( \theta ) > 0 } \\ { 0 , \quad } & { { } K ( \theta ) = 0 \quad } & { a \leqslant \theta \leqslant b , } \\ { - 1 , \quad } & { { } K ( \theta ) < 0 , } \end{array} \right.
$$

and where $\mathcal { Z }$ is the set

$$
{ \mathcal { L } } = \{ \theta colon K ( \theta ) = 0 , a \leqslant \theta \leqslant b \} .
$$

Inequality (24.37） is not a direct consequence of equation (24.30), because of the possibility that $\pmb { K }$ is identically zero on some subintervals of $[ a , b ]$ .We have to apply Theorem 19.1 again. Therefore we let $x _ { 0 }$ and $x _ { m + 1 }$ be fixed points such that the conditions

$$
\left. \begin{array} { l } { x _ { 0 } < \operatorname* { m i n } \left[ x _ { 1 } , \xi \right] } \\ { x _ { m + 1 } > \operatorname* { m a x } \left[ x _ { m } , \xi \right] } \end{array} \right\}
$$

hold,and if necessary we extend the range of $\pmb \theta$ in the definition (24.35) so that it includes the points $x _ { 0 }$ and $x _ { m + 1 }$ ·

The kernel function (24.35) is a spline of degree $k$ whose knots are $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ and $\xi ,$ and,due to equation (24.15),it has zeros at $\{ \xi _ { j }$ ； $j = 1 , 2 , \ldots , m - k - 1 \} .$ If $\pmb { p }$ and $q$ are integers such that $\pmb { K }$ is identically zero on $[ x _ { p - 1 } , x _ { p } ]$ and $[ x _ { q } , x _ { q + 1 } ]$ ,but if $\pmb { K }$ has a finite number of zeros in $( x _ { p } , x _ { q } )$ ,then condition (24.27) implies that the number of zeros in $( x _ { p } , x _ { q } )$ is not less than $( q - p - k )$ . It follows from Theorem 19.1 that $\kappa$ has at least $( q - p )$ knots in $( x _ { p } , x _ { q } )$ . Because only $( q - p - 1 )$ of the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ are in this interval, $\xi$ is also in $( x _ { p } , x _ { q } )$ . Therefore, either $\kappa$ is identically zero,which happens when $\xi$ is in the point set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ , or there exist numbers $\pmb { \alpha }$ and $\beta$ in $[ a , b ]$ such that $\pmb { K }$ is non-zero only in $( \alpha , \beta )$ ,and in this interval the number of zeros of $\pmb { K }$ is finite.In the first case inequality (24.37) is satisfied because $\{ t ( \theta ) = 0$ ； $a \leqslant \theta \leqslant b \}$ , but the second case requires further consideration.

The only zeros of $\pmb { K }$ in the interval $( \alpha , \beta )$ are in the set $\{ \xi _ { j } ; j = 1$ ， $2 , \ldots , m - k - 1 \}$ ,and all these zeros are simple, because otherwise, by extending the argument of the previous paragraph that depends on Theorem 19.1,we find that $\pmb { K }$ has insufficient knots. It follows from the definitions (24.31） and (24.38) that either $\{ t ( \theta ) = z ( \theta )$ ； $\alpha < \theta < \beta \}$ or $\{ t ( \theta ) = - z ( \theta )$ ： $\alpha < \theta < \beta \}$ . Therefore, because $t$ is zero on $( a , \alpha )$ and $( \beta , b )$ , and because equations (24.30) and (24.36) imply the value

$$
\int _ { a } ^ { b } z \left( \theta \right) \eta \left( \theta \right) { \bf d } \theta = 0 ,
$$

the identity

$$
\begin{array} { l } { { \displaystyle { \left| \int _ { a } ^ { b } t ( \theta ) \eta ( \theta ) { \bf d } \theta \right| = \left| \int _ { \alpha } ^ { \beta } z ( \theta ) \eta ( \theta ) { \bf d } \theta \right| } } } \\ { { \displaystyle { \qquad = \left| \int _ { a } ^ { \alpha } z ( \theta ) \eta ( \theta ) { \bf d } \theta + \int _ { \beta } ^ { b } z ( \theta ) \eta ( \theta ) { \bf d } \theta \right| } } } \end{array}
$$

is satisfied. We note that the set (24.39) contains the intervals $( a , \alpha )$ and $( \beta , b )$ ,and that $\| z \| _ { \infty }$ is one. Hence inequality (24.37) is a consequence of equation (24.42). Therefore equation (24.15) does define the parameters of the optimal interpolation formula.

We require later that the definition (24.38), and the properties of $K , t$ and $z$ that are given in the previous two paragraphs, imply the equation

$$
\begin{array} { c } { \displaystyle \| { \boldsymbol { K } } \| _ { 1 } = \int _ { a } ^ { b } { \boldsymbol { K } } ( \theta ) t ( \theta ) { \mathrm { d } } \theta } \\ { \displaystyle = \left| \int _ { a } ^ { b } { \boldsymbol { K } } ( \theta ) z ( \theta ) { \mathrm { d } } \theta \right| . } \end{array}
$$

# 24.3 Properties of optimal interpolation

Instead of calculating the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ of the optimal interpolation formula from equation (24.15),and then obtaining the coefficients $\{ w _ { i } ( \xi ) ; i = 1 , 2 , \dots , m \}$ from the equivalence of the approximations (24.1) and (24.9), it is better to determine $\{ w _ { i } ( \xi )$ ； $i = 1 , 2 , \ldots , m \}$ directly from the properties that define the optimal values of $\{ u _ { i } ; i = 1 , 2 , \ldots , k + 1 \}$ and $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ .These properties are that equation (24.1O) must hold,and that the kernel function (24.35) is zero when $\{ \theta = \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ ,where the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are independent of $\xi .$ Because equation (24.10) states that the approximation (24.1) is exact when $f$ is in $\mathcal { P } _ { k } ,$ it is equivalent to the conditions

$$
\sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) x _ { i } ^ { r } = \xi ^ { r } , \qquad r = 0 , 1 , \ldots , k ,
$$

and, because expressions (24.6) and (24.35） must be the same, the relations that determine $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are the equations

$$
\sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) ( x _ { i } - \xi _ { j } ) _ { + } ^ { k } = ( \xi - \xi _ { j } ) _ { + } ^ { k } , \qquad j = 1 , 2 , \ldots , \dot { m } - k - 1 .
$$

The formulae (24.44) and (24.45) give a square system of linear equations in the unknowns $\{ w _ { i } ( \xi ) ; \ i = 1 , 2 , \dots , m \}$ ，which is non-singular, because equivalent equations define $\{ u _ { i } ; i = 1 , 2 , \ldots , k + 1 \}$ and $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ uniquely. The matrix elements of the system are the numbers $\{ x _ { i } ^ { r } ; r = 0 , 1 , \ldots , k \}$ and $\left\{ \left( x _ { i } - \xi _ { j } \right) _ { + } ^ { k } \right.$ ； $j = 1 , 2 , \dots ,$ $m - k - 1 \}$ ,where $1 \leqslant i \leqslant m$ .They are mentioned explicitly, because it is important to notice that they are independent of $\xi .$ Therefore, if the system is multiplied by the inverse matrix, which is also independent of $\xi ,$ it follows that each of the coefficient functions $\{ w _ { i } ( \pmb { \xi } )$ ； $a \leqslant \xi \leqslant b$ ； $i = 1 , 2 , \dots , m \}$ is in the linear space that is spanned by $\{ \xi ^ { r } ; a \leqslant \xi \leqslant b$ ； $r = 0 , 1 , \ldots , k \}$ and $\{ ( \pmb { \xi } - \pmb { \xi } _ { j } ) _ { + } ^ { k }$ ； $a \leqslant \xi \leqslant b ; j = 1 , 2 , \ldots , m - k - 1 \} ,$ Thus, letting $\xi _ { 0 } = a$ and $\xi _ { m - k } = b$ ,the functions $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ are all in the space that we call $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { m - k } )$ . It follows that the optimal interpolating function (24.3) is also a spline of degree $k$ .Because there is no error in the optimal interpolation formula when $\pmb { \xi }$ is one of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ， the optimal interpolating function satisfies the conditions

$$
s ( \boldsymbol { x } _ { i } ) = f ( \boldsymbol { x } _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

The number of equations is equal to the dimension of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { m - k } )$ ，Therefore, instead of calculating $\{ w _ { i } ( \pmb { \xi } ) ; i = 1$ ， $2 , \ldots , m \}$ in order to determine $\pmb { S } _ { \mathrm { i } }$ , one can calculate $\pmb { s }$ directly from the system (24.46), provided that the knots $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are known. Because the indirect procedure defines $\pmb { s }$ uniquely, the equations (24.46) are non-singular. Alternatively, one can turn to Theorem 19.4 to check whether the equations have a solution. We find that the conditions on $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ ,that are required by Theorem 19.4,are equivalent to the ones that occur in Theorem 24.3.

In order to determine the knots of $\pmb { S } _ { 3 }$ ，we consider the conditions that they have to satisfy. Theorem 24.1 states that it is necessary and sufficient for the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ to have the property that, if the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are defined by equation (24.15), then the norm (24.14) is minimized.It follows from the discussion that follows the proof of Theorem 24.3 that it is sufficient if the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ satisfy the bounds (24.27),and if equation (24.30) holds, where $z$ is the sign function (24.31). Moreover, Theorem 24.3 shows that such points exist. However, instead of calculating $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ directly from the non-linear equations that are implied by expressions (24.30) and (24.31), it is usually easier to seek a perfect spline $\pmb { \sigma }$ of degree $( k + 1 )$ whose knots are $\{ \xi _ { j } ; j = 1 , 2 , \ldots ,$ $m - k - 1 \}$ .The relation (24.32） between $\sigma$ and $z$ has to be satisfied, but this relation allows any polynomial from $\mathcal { P } _ { k }$ to be added to $\pmb { \sigma }$ Therefore we impose the conditions $\{ \pmb { \sigma } ( \pmb { x } _ { i } ) = 0$ ； $i = 1 , 2 , \ldots , k + 1 \}$ Hence,because equation (24.3O) implies that the divided differences $\{ \sigma [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ]$ $p = 1 , 2 , \ldots , m - k - 1 \}$ are all zero, it follows that all the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ are zeros of $\pmb { \sigma }$ ，Thus the required knots $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ of the optimal interpolating function (24.3) are the knots of a perfect spline $\pmb { \sigma }$ of degree $( k + 1 )$ that satisfies the equations

$$
\begin{array} { l } { \sigma ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m } \\ { \| { \boldsymbol { \sigma } } ^ { ( k + 1 ) } \| _ { \infty } = 1 } \end{array} \biggr \} .
$$

It'is particularly useful that the converse of the last remark is true. In other words, if $\sigma$ is a perfect spline of degree $( k + 1 )$ that has $( m - k - 1 )$ knots,and that satisfes condition (24.47)， then its knots $\{ \xi _ { j } ; ~ j = 1$ ， $2 , \ldots , m - k - 1 \}$ are suitable knots for the spline $\pmb { s }$ of the optimal interpolation procedure. In order to prove this statement it is sufficient to show that expressions (24.27) and (24.30) are valid, where $z$ and $\scriptstyle B _ { p }$ are the functions (24.31) and (24.16). The first line of equation (24.47) and Theorem 22.3 imply the identities

$$
\int _ { a } ^ { b } \sigma ^ { ( k + 1 ) } ( \theta ) B _ { p } ( \theta ) \mathrm { d } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 .
$$

Therefore,because the function (24.31) is a muliple of $\sigma ^ { ( k + 1 ) }$ , equation (24.30) is satisfied. It follows from the last two paragraphs of the proof of Theorem 24.3 that inequality (24.27) is also valid.

The next theorem summarises these properties of optimal interpolation,and it gives one new result.

# Theorem 24.4

Let $k$ and $_ m$ be positive integers such that $m \geq k + 1$ , let the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy condition (24.5),and let $\sigma$ be a perfect spline of degree $( k + 1 )$ on $[ a , b ]$ that has $( m - k - 1 )$ knots $\{ \xi _ { j } ; j = 1$ ， $2 , \ldots , m - k - 1 \}$ ，and that satisfies equation (24.47). If $f$ is any function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ,then the interpolation conditions (24.46) define a unique approximation $\pmb { s }$ in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \xi _ { 2 } , . ~ . ~ . , \xi _ { m - k - 1 } , \xi _ { m - k } )$ ，whose error is bounded by the inequality

$$
\big | f ( \xi ) - s ( \xi ) \big | \leqslant \big | \sigma ( \xi ) \big | \big \| f ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad a \leqslant \xi \leqslant b ,
$$

where $\xi _ { 0 } = a$ and $\xi _ { m - k } = b$ .Further,if the parameters $\{ w _ { i } ; ~ i = 1 , 2 ,$ $\cdots , m \}$ and $^ c$ have any values such that condition (24.2） is valid for all $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ then $^ c$ is not less than $| \sigma ( \xi ) |$

Proof. The only result that has not been proved already is that, if $\pmb { \xi }$ is any fixed point of $[ a , b ]$ ,then $\| K \| _ { 1 }$ is equal to $\left| \sigma ( \xi ) \right|$ ,where the kernelfunction $\pmb { K }$ is defined by the equation

$$
f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

and where the notation (24.3） is used for the optimal interpolating function in order to show its dependence on $f .$ . We express $\| K \| _ { 1 }$ in terms of $\sigma$ .The sign function $z$ ,defined by equation (24.31), changes sign at the knots of $\pmb { \sigma } _ { : }$ ,and the absolute values of $z$ and $\sigma ^ { ( k + 1 ) }$ are equal to one almost everywhere. Therefore equation (24.43) gives the value

$$
\| K \| _ { 1 } = \left| \int _ { a } ^ { b } K ( \theta ) \sigma ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta \right| .
$$

The proof is completed by obtaining an identity from equation (24.50) in the particular case when $f = \sigma .$ .The equation is valid in this case,even though g(k+1) is not continuous, because otherwise one can deduce a contradiction by letting $f$ be a function that satisfies the conditions $\{ f ( x _ { i } ) = \sigma ( x _ { i } ) ; i = 1 , 2 , . . . , m \} , f ($ $f ( \pmb { \xi } ) = \pmb { \sigma } ( \pmb { \xi } )$ and the inequality

$$
\left| \int _ { a } ^ { b } K \left( \theta \right) \left[ f ^ { ( k + 1 ) } ( \theta ) - \sigma ^ { ( k + 1 ) } ( \theta ) \right] \mathrm { d } \theta \right| < \varepsilon ,
$$

where $\varepsilon$ is a sufficiently small positive constant. Because the terms $\{ \sigma ( x _ { i } )$ ； $i = 1 , 2 , \ldots , m \}$ are all zero, substituting $f = \sigma$ in expression (24.50) gives the value

$$
\sigma ( \xi ) = \int _ { a } ^ { b } K ( \theta ) \sigma ^ { ( k + 1 ) } ( \theta ) { \bf d } \theta .
$$

It follows from equation (24.51) that the numbers $\| K \| _ { 1 }$ and $\left. \sigma ( \xi ) \right.$ are equal. The theorem is proved.□

Some examples on the use of the optimal interpolation procedure are given in the exercises. They show that the error bounds of optimal interpolation are not much smaller than those that are obtained by simpler algorithms. Therefore the value of the optimal interpolation method may be questioned. One good reason for studying optimal procedures is that they can indicate directly whether it is possible to make substantial improvements to more convenient algorithms. Moreover, the work of this chapter gives excellent theoretical support to the strong practical reasons for employing spline approximations in computer calculations.

# 24 Exercises

24.1 Let $\{ B _ { 1 } ( \theta ) ; 0 \leqslant \theta \leqslant 3 \}$ be the linear $B$ -spline of the form (24.16) that has knots at the points $\{ x _ { 1 } = 0 , x _ { 2 } = 1 , x _ { 3 } = 3 \}$ . Calculate the value of $\xi _ { 1 }$ that satisfies the equation

$$
\int _ { 0 } ^ { \xi _ { 1 } } B _ { 1 } ( \theta ) { \bf d } \theta = \int _ { \xi _ { 1 } } ^ { 3 } B _ { 1 } ( \theta ) { \bf d } \theta .
$$

Let $\{ \sigma ( \xi ) ; 0 \leqslant \xi \leqslant 3 \}$ be a perfect spline of degree two that has only one knot, and that has zeros at the points $\{ x _ { i } ; i = 1 , 2 , 3 \}$ Verify that the knot of $\pmb { \sigma }$ is at $\xi _ { 1 }$

24.2 Calculate from Theorem 24.4 and from Exercise 24.1 the numbers $w _ { 1 } , w _ { 2 } , w _ { 3 }$ and $c$ ,such that the value of $c$ is as small as possible in the inequality

$$
\big | f ( 2 ) - w _ { 1 } f ( 0 ) - w _ { 2 } f ( 1 ) - w _ { 3 } f ( 3 ) \big | \leqslant c \big \| f ^ { \prime \prime } \big \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( 2 ) } [ 0 , 3 ] .
$$

Compare the term on the right-hand side with the error expres-sion of Theorem 4.2 for the approximation $f ( 2 ) { \approx } \frac { 1 } { 2 } [ f ( 1 ) + f ( 3 ) ]$

24.3 Find the form of the optimal linear spline approximation to the function values $\{ f ( - 1 ) , f ( - 1 + \varepsilon ) , f ( 1 - \varepsilon ) , f ( 1 ) \}$ ，where $\varepsilon$ isa constant from the open interval $( 0 , \textstyle { \frac { 2 } { 3 } } )$ . Show that the $\infty$ -norm of the optimal interpolation operator has the value $[ - \frac { 1 } { 2 } + \varepsilon ^ { - 1 } ]$

24.4 Extend Theorem 24.4 to the case when the data points satisfy the condition

$$
a \leqslant x _ { 1 } \leqslant x _ { 2 } \leqslant \ldots \leqslant x _ { m } \leqslant b
$$

instead of inequality (24.5),assuming that no number is repeated more than $( k + 1 )$ times in the set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ If repeats occur, then the conditions (24.46) on $\pmb { s }$ are replaced bythe equations $\begin{array} { r } { \{ s ^ { ( j ) } ( x _ { i } ) = f ^ { ( j ) } ( x _ { i } ) ; \quad j = 0 , 1 , \dots , r ( i ) - 1 , } \end{array}$ ： $i = 1 , 2 , \ldots , m \}$ ，where $\pmb { r } ( i )$ is the number of occurrences of the number $x _ { i }$ in the set of data points.

24.5 The values $f ( 0 ) , f ^ { \prime } ( 0 ) , f ^ { \prime \prime } ( 0 )$ and $f ( 1 )$ of a function $f$ in $\mathcal { C } ^ { ( 3 ) } [ 0 , 1 ]$ are given. For any $\pmb { \xi }$ in [0, 1], let $s ( \xi )$ be the estimate of $f ( \xi )$ that minimizes the value of $c ( \xi )$ in the error bound

$$
\left| f ( \xi ) - s \left( \xi \right) \right| < c \left( \xi \right) \left\| f ^ { \prime \prime \prime } \right\| _ { \infty } .
$$

Calculate the functions $\{ s ( \xi ) ; 0 \leqslant \xi \leqslant 1 \}$ and $\{ c ( \xi ) ; 0 \leqslant \xi \leqslant 1 \}$

24.6 Let $f$ be a function that is defined on the range $( - \infty , \infty )$ and that has a bounded and continuous fourth derivative,and let the function values $\{ f ( x _ { i } ) = f ( i h ) ; i = 0 , \pm 1 , \pm 2 , . . . \}$ be given, where $\pmb { h }$ is a positive constant. Let $\{ s ( \xi ) ; \ - \infty < \xi < \infty \}$ be the best estimate of $\{ f ( \xi ) ; - \infty < \xi < \infty \}$ that can be obtained from the data,in the sense that the multiple of $\| f ^ { ( 4 ) } \| _ { \infty }$ that bounds the error $\left| f ( \pmb { \xi } ) - s ( \pmb { \xi } ) \right|$ is minimized. Prove that $\pmb { s }$ is the cubic spline that has knots at the points $\{ x _ { i } = i h ; i = 0 , \pm 1 , \pm 2 , . . . \}$ and that interpolates $f$ at its knots. Obtain the analogous property of the quadratic spline interpolation procedure whose cardinal functions have the form that is shown in Figure 18.4.

Let the conditions of Exercise 24.6 be satisfied except that only the function values $\{ f ( x _ { i } ) = f ( i h ) ; \ i = 1 , 2 , . . . , m \}$ are given, where $m \geqslant 4$ . Hence the optimal interpolating function $\{ \pmb { s } ( \pmb { \xi } )$ $x _ { 1 } \leqslant \xi \leqslant x _ { m } \}$ is a cubic spline that has $( m - 4 )$ knots. Let $\bar { s }$ be the cubic spline in the space $\mathcal { S } ( 3 , x _ { 1 } , x _ { 2 } , \ldots , x _ { m } )$ that interpolates the data, and whose third derivative is continuous at $x _ { 2 }$ and at $x _ { m - 1 }$ .Let $\mathcal { S } _ { 0 }$ be the two-dimensional subspace of $\mathcal { S }$ that contains splines that are zero at the knots $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ . Let ${ \pmb S } _ { \pmb { \alpha } }$ and $s _ { \beta }$ be the elements of $\mathcal { S } _ { 0 }$ whose third derivative discontinuities at $\pmb { x } _ { 2 }$ and $x _ { m - 1 }$ are one and zero and zero and one respectively. By comparing $\pmb { s }$ and $\bar { s }$ with the cubic spline that is considered in Exercise 24.6, prove that there exists a number $\pmb { \mu }$ ,independent of $f , h$ and $^ { m }$ ,such that the bound

$\big | f ( \xi ) - \bar { s } ( \xi ) \big | \leqslant \{ \big | \sigma ( \xi ) \big | + \mu h [ \big | s _ { \alpha } ( \xi ) \big | + \big | s _ { \beta } ( \xi ) \big | ] \} \{ \big | f ^ { ( 4 ) } \big | \big | _ { \infty } , \quad \ x _ { 1 } \leqslant \xi \leqslant x _ { m } ,$ is satisfied,where $\pmb { \sigma }$ is defined in Theorem 24.4.

24.8 The argument that follows Theorem 24.3 proves that the equa-tions (24.15) define the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ that minimize the norm (24.14). Another way of obtaining this result depends on the fact that the system (24.15) is the limit as $M$ tends to infinity of the system (24.25). Make this alternative argument rigorous.

24.9 Show that, except for an overall change of sign, there is only one perfect spline $\pmb { \sigma }$ that satisfies the conditions of Theorem 24.4. It is suitable to combine the method of proof of Theorem 14.4 with the orthogonality conditions (24.48).

24.10 Let $f$ be a function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ,let the function values $\{ f ( x _ { i } )$ $i = 1 , 2 , \ldots , m \}$ be given, where $m \geq k + 1$ , and let $L$ be a linear functional. The approximation to $L f$ by a linear combination of the function values is required, such that the error of the approx-imation is bounded by the smallest possible multiple of $\| f ^ { ( k + 1 ) } \| _ { \infty }$ Investigate conditions on $L$ that imply that $L s$ is the required approximation to $L f ,$ where $\pmb { s }$ is the spline function that is defined in Theorem 24.4.

# APPENDIX A

# The Haar condition

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear space in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ In Section $\mathbf { 7 . 3 \ d }$ is defined to satisfy the Haar condition if the following property is obtained.

Condition $\mathbf { \Omega } ( \pmb { 1 } )$ If $\phi$ is any element of $\mathcal { A }$ that is not identically zero, then the number of roots of the equation $\{ \phi ( { \pmb x } ) = 0$ ； $a \leqslant x \leqslant b $ is less than $( n + 1 )$

The purpose of this appendix is to prove that the following three conditions are implied by Condition (1),and also that Condition (3) and Condition (4) are each equivalent to Condition (1).

Condition (2). If $\pmb { k }$ is any integer in $[ 1 , n ]$ and if $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ is any set of distinct points from the open interval $( a , b )$ ,then there exists an element of $\scriptstyle { \mathcal { A } }$ that changes sign at these points,and that has no other zeros.Moreover, there is a function in $\mathcal { A }$ that has no zeros in $[ a , b ]$

Condition $( { \pmb 3 } )$ If $\phi$ is any element of $\mathscr { A }$ that is not identically zero, if the number of roots of the equation $\{ \phi ( { \pmb x } ) = 0$ ； $a \leqslant x \leqslant b \}$ is equal to $j ,$ and if $\pmb { k }$ of these roots are interior points of $[ a , b ]$ at which $\phi$ does not change sign, then $( j + k )$ is less than $( n + 1 )$

Condition (4). If $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is any basis of $\scriptstyle { \mathcal { A } } .$ and if $\{ \xi _ { i } ; j = 0 , 1 , \ldots , n \}$ is any set of $( n + 1 )$ distinct points in $[ a , b ] ,$ then the $( n + 1 ) \times ( n + 1 )$ matrix whose elements have the values $\{ \phi _ { i } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is non-singular.

It is clear that Condition (3) implies Condition (1). First it is proved that Conditions (1) and (4) are equivalent.Secondly it is shown that Conditions (1) and (4) together imply Condition (3).Finally we deduce Condition (2)from Condition (3). The final stage depends on limits of sequences of functions.

The equivalence of Conditions $( { \pmb { 1 } } )$ and (4). Suppose that Condition (1) holds but Condition (4) fails. Then there exist $( n + 1 )$ distinct points $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ in $[ a , b ] ,$ ，such that the matrix $\{ \phi _ { i } ( \xi _ { j } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is singular.

where $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is a basis of $\mathcal { A } .$ Therefore there exist multipliers $\left\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \right\}$ ,that are not all zero,and that satisfy the equations

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( \xi _ { j } ) = 0 , \qquad j = 0 , 1 , \ldots , n .
$$

It follows that the function

$$
\phi \left( x \right) = \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

has zeros at the points $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ ,but this conclusion contradicts Condition (1).

Conversely,if Condition (1) fails, then there is a function of the form (A.2) that is not identically zero,and that has zeros at the points $\{ \xi _ { i } ; j = 0 , 1 , \ldots , n \}$ say. Hence equation (A.1） is satisfied,which implies that the matrix $\{ \phi _ { i } ( \pmb { \xi } _ { i } ) ; i = 0 \}$ ， $1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is singular.Therefore there is also a contradiction if Condition (1） fails but Condition (4） holds,which completes the proof that Conditions (1) and (4) are equivalent.

Conditions $( { \pmb { 1 } } )$ and (4) imply Condition $( { \pmb 3 } )$ .It is sufficient to show a contradiction if Conditions (1） and (4） hold,but Condition (3） is not satisfied.When Condition (3) is not obtained,there is a function $\phi$ in $\mathscr { A }$ that is not identically zero, that has double zeros at the points $\{ \eta _ { i } ; i = 1 , 2 , \ldots , k \}$ and that has simple zeros at the points $\{ \eta _ { i } ; i = k + 1 , k + 2 , \ldots , j \} $ where $( j + k ) \geqslant ( n + 1 )$ ,and where a zero is said to be simple if it is a point at which $\phi$ changes sign,or if it is one of the ends of the range $[ a , b ]$ 、Because Condition (1） is contradicted if $j \geq ( n + 1 )$ ，we only consider the case when $j \leqslant n$ .Therefore there is at least one double zero.We let $\pmb \varepsilon$ be a positive number such that, for each integer $_ i$ in the range $1 \leqslant i \leqslant k .$ the function $\phi$ is zero at only one point of the interval $[ \eta _ { i } - \varepsilon , \eta _ { i } + \varepsilon ] ,$ namely the point $\eta _ { i } ,$ and we let $c _ { i }$ be any non-zero number whose sign is the same as the sign of the function $\phi$ on the interval $[ \eta _ { i } - \varepsilon , \eta _ { i } + \varepsilon ] .$ Further,we let $\{ \xi _ { t } ; t = 0 , 1 , \ldots , n \}$ be any set of distinct points of $[ a , b ]$ that includes the points $\left\{ \xi _ { t } = \eta _ { t + 1 } \right.$ ； $\scriptstyle t = 0$ ， $1 , \ldots , j - 1 \}$

Condition (4) implies that there is a unique element of $\mathcal { A } , \psi$ say, that is defined by the equations

$$
\psi ( \xi _ { t } ) = \left\{ { \begin{array} { l } { c _ { t + 1 } , \quad t = 0 , 1 , \ldots , k - 1 } \\ { 0 , \quad t = k , k + 1 , \ldots , n . } \end{array} } \right.
$$

We consider the function $\left\{ \phi ^ { * } ( x ) = \phi ( x ) - \theta \psi ( x ) ; a \leqslant x \leqslant b \right\}$ ，where $\pmb \theta$ is a small positive number that satisfies the inequalities

$$
\begin{array} { l } { { \theta { | \psi ( { { \eta } _ { i } } - \varepsilon ) | } < { | \phi ( { { \eta } _ { i } } - \varepsilon ) | } } } \\ { { \theta { | \psi ( { { \eta } _ { i } } + \varepsilon ) | } < { | \phi ( { { \eta } _ { i } } + \varepsilon ) | } } } \end{array}  , \qquad i = 1 , 2 , \ldots , k .
$$

By construction $\phi ^ { * }$ changes sign in each of the intervals $\{ ( \eta _ { i } - \varepsilon , \eta _ { i } ) ; i = 1$ ， $2 , \ldots , k \}$ and $\{ ( \eta _ { i } , \eta _ { i } + \varepsilon ) ; i = 1 , 2 , \dots , k \}$ ，and also it has zeros at the points $\{ \eta _ { i } ; i = k + 1 , k + 2 , \ldots , j \}$ .Hence it has at least $( j + k )$ zeros,which contradicts Condition (1). The proof that Condition (3) is a consequence of Conditions (1) and (4) is complete.

Proof that Condition (2) is satisfied. Let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , n \}$ be any set of distinct points in $[ a , b ]$ .Because the dimension of $\scriptstyle { \mathcal { A } }$ is $( n + 1 )$ ,there exists a function $\psi$ in $\mathcal { A }$ that is not identically zero and that satisfies the equations

$$
\psi ( \zeta _ { j } ) = 0 , \qquad j = 1 , 2 , \ldots , n .
$$

It follows from Condition (3) that $\psi$ has no other zeros in $[ a , b ]$ ,and that it changes sign at those zeros that are interior points of $[ a , b ]$ .Therefore Condition (2) holds when $k = n$

When $k = n - 1$ , we let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ be interior points of $[ a , b ] .$ and we let $\psi _ { a }$ and $\psi _ { b }$ be non-zero functions in $\mathscr { A }$ that have zeros at the points $\{ \zeta _ { i } ; j =$ $1 , 2 , \ldots , k \}$ and at one other point, namely $^ { a }$ and $^ { b }$ respectively. Condition (3) implies that the overall sign of $\psi _ { b }$ may be chosen to satisfy the inequality $\{ \psi _ { a } ( x ) \psi _ { b } ( x ) { \geq } 0$ ； $a \leqslant x \leqslant b $ .Hence the function $\psi = { \textstyle \frac { 1 } { 2 } } ( \psi _ { a } + \psi _ { b } )$ shows that Condition (2) is valid when $k = n - 1$

The method of proof for smaller values of $k$ depends on the following statement. If $k$ and $t$ are non-negative integers such that $k + 2 t = n$ and if $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ are distinct points of $[ a , b ]$ where all the points $\{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ are in the open interval $( a , b )$ ,then there exists a function $\psi$ in $\mathcal { A }$ that has simple zeros at $\left\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \right\}$ and that has double zeros at $\{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ . In order to prove it we let $\bar { \varepsilon }$ be a positive constant such that, for each integer $i$ in $[ 1 , t ] , \eta _ { i }$ is the only one of the points $\{ \zeta _ { j } ; j = 1$ ， $2 , \ldots , k \}$ $\cdot \cdot , k \} , \{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ ， $^ { a }$ and $^ { b }$ that are in the interval $\left[ \eta _ { i } - { \bar { \varepsilon } } , \ \eta _ { i } + { \bar { \varepsilon } } \right]$ Further,for any $\pmb \varepsilon$ in $( 0 , \bar { \varepsilon } )$ , we let $\psi _ { \epsilon }$ be a function in $\mathcal { A }$ that has zeros at the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ ， $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ and $\left\{ \eta _ { j } + \varepsilon ; j = 1 , 2 , \dots , t \right\}$ .This function is scaled so that the coefficients of the expression

$$
\psi _ { \varepsilon } ( x ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } ( \varepsilon ) \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

satisfy the condition

$$
\sum _ { i \mathop { = } 0 } ^ { n } [ \lambda _ { i } ( \varepsilon ) ] ^ { 2 } = 1 ,
$$

where $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is a basis of $\mathcal { A } .$ Because Condition (3) implies that all the zeros of $\psi _ { \varepsilon }$ are simple, the products $\{ \psi _ { \varepsilon } ( \eta _ { j } - \delta ) \psi _ { \varepsilon } ( \eta _ { j } + \delta ) ; j = 1 , 2 , \dots , t \}$ are all positive,where $\pmb { \delta }$ is any number in $( \varepsilon , \bar { \varepsilon } )$

We let $\{ \varepsilon _ { q } ; q = 1 , 2 , 3 , \ldots \}$ be a sequence of numbers from the interval $( 0 , \bar { \varepsilon } )$ that tends to zero. Condition (A.7) implies that the sequence of parameters $[ \{ \lambda _ { i } ( \pmb { \varepsilon } _ { q } ) ; i = 0 , 1 , . . . , n \}$ ； $q = 1$ ,2,3,.. .] has a limit point $\{ \lambda _ { i } ^ { * } ; i = 0 , 1 , \dots , n \}$ It will be shown that it is suitable to let $\psi$ be the function

$$
\psi ( x ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } ^ { * } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Equation (A.7) implies that $\psi$ is not the zero function. Moreover,the definition of each $\psi _ { \epsilon }$ implies that $\psi$ has zeros at the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j =$ $1 , 2 , \ldots , t \}$ . It remains,therefore,to rule out the possibility that one or more of the points $\{ \eta _ { i } ; j = 1 , 2 , \dots , \ \}$ are simple zeros. If $\pmb { \eta _ { j } }$ is a simple zero,there exists $\pmb \delta$ in $( 0 , \bar { \varepsilon } )$ such that the product $[ \psi ( \eta _ { j } - \delta ) \psi ( \eta _ { j } + \delta ) ]$ is negative.However, we have noted already that the product $\left[ \psi _ { \varepsilon } ( \eta _ { j } - \delta ) \psi _ { \varepsilon } ( \eta _ { j } + \delta ) \right]$ is positive if $\pmb \varepsilon$ is less than $\delta$ ， so it is non-negative in the limit as $\pmb \varepsilon$ tends to zero. This contradiction completes the proof that the function (A.8) has the required zeros.

In order to show that Condition (2) holds when $n - k = 2 t$ is a positive even integer,we choose interior points $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ of $[ a , b ]$ that are different from the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and we let $\psi$ be a function in $\pmb { \mathcal { A } }$ that has the zeros that have just been considered.It is important to notice that, because of Condition (3), $\psi$ has no other zeros.Further we let $( \eta _ { j } ^ { + } ; j = 1 , 2 , \dots , t \}$ be a set of points in $( a , b )$ that has no points in common with the sets $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ and we let $\psi ^ { + }$ be a function in $\pmb { \mathcal { A } }$ that has simple zeros at $\{ \zeta _ { j }$ ； $j = 1 , 2 , \dots , k \}$ and double zeros at $\{ \eta _ { j } ^ { + } ; j = 1 , 2 , \dots , t \}$ .This function also has no other zeros: Because both $\psi$ and $\psi ^ { + }$ change sign only at the points $\{ \zeta _ { j } ; j = 1$ ， $2 , \ldots , k \}$ ，either the function $( \psi - \psi ^ { + } )$ or the function $( \psi + \psi ^ { + } )$ proves that Condition (3) is obtained when $( n - k )$ is an even integer.

Alternatively, if $n - k = 2 t + 1$ is an odd integer,we follow the method of the last paragraph, except that we add the point $^ { a }$ to the set $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ before defining $\psi _ { : }$ and we add $^ { b }$ to the set $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ before defining $\psi ^ { + }$ .The remainder of the proof is as before.Because these techniques can be used even when $k = 0$ , it follows that the last statement of Condition (2) is valid.The proofs of the relations between Conditions (1), (2),(3) and (4) are now complete.

# APPENDIX B

# Related work and references

Many excellent books are published on approximation theory and methods. The general texts that are particularly valuable to the present work are the ones by Achieser [2],Cheney [35],Davis [50],Handscomb (ed.)[74],Hayes (ed.)[77], Hildebrand [78],Holland & Sahney [81],Lorentz [100],Rice [132] and [134], Rivlin [138] and Watson [161]. Detailed references and suggestions for further reading are given in this appendix.

Most of the theory in Chapter 1 is taken from Cheney[35] and from Rice [132]. If one prefers an introduction to approximation theory that shows the relations to functional analysis, then the paper by Buck [32] is recommended.We give further attention only in special cases to the interesting problem, mentioned at the end of Section 1.1,of investigating how well any member of $\mathcal { B }$ can be approximated from $\mathscr { A }$ ; a more general study of this problem is in Lorentz[1OO] and in Vitushkin [160]. The development of the Polya algorithm,which is the subject of Exercise 1.10, into a useful computational procedure is considered by Fletcher, Grant & Hebden [57].

In Chapter 2,as in Chapter 1,much of the basic theory is taken from Cheney [35].For a further study of convexity the book by Rockafellar [142] is recommended.Several excellent examples of the non-uniqueness of best approximation with respect to the 1- and the $\infty$ -norms are given by Watson [161]. An interesting case of Exercise 2.1, namely when $\mathcal { B }$ is the space ${ \mathcal { R } } ^ { n }$ and the unit ball $\{ f \colon \| f \| \leqslant 1$ ； $f \in { \mathcal { B } } \}$ is a polyhedron,is considered by Anderson & Osborne [5].

The point of view in Chapter 3 that approximation algorithms can be regarded as operators is treated well by Cheney [35],and more advanced work on this subject can be found in Cheney & Price [37]. Several references to applications of Theorem 3.1 are given later, including properties of polynomial approximation operators that are defined by interpolation conditions. A comparison of the advantages of preferring rational to polynomial approximations is made by Hastings [76]. There is now a vast literature on spline functions,including interesting books by Ahlberg,Nilson & Walsh [4],de Boor [26],Prenter[127] and Schultz[151]. For a short introduction to splines the papers by Birkhoff & de Boor [15]and by Greville [70] are recommended. An excellent summary of more advanced properties of spline functions is given by Schoenberg [149].

The theory of Lagrange interpolation, considered in Chapter 4, is in most text-books on numerical analysis; see Hildebrand [78],for instance.These books include also many properties of Chebyshev polynomials.A careful analysis of Runge's example (4.19) is given by Steffensen [155]. The norms of polynomial interpolation operators are used by Powell[121] to draw attention to some of the advantages of the Chebyshev interpolation points.Further properties of the Lebesgue function $\{ \Sigma | l _ { k } ( x ) |$ ; $a \leqslant x \leqslant b \}$ ,when the Chebyshev interpolation points are used,are derived by Brutman [31]. The solution to the problem of Exercise 4.10 was conjectured by Bernstein in 1931, but the conjecture was not proved until 1977,by de Boor & Pinkus [28] and by Kilgore [89] independently.

Because the divided difference theory and methods of Chapter 5 were used extensively for the construction of tables, some of the best accounts of this work are in the older numerical analysis text-books,such as Steffensen [155]. The use of divided differences to detect errors in equally spaced data is explained by Miller [115],and an extension to allow unequal spacing between data points is made by Blanch [16]. More recent applications of divided differences are included in our study of spline approximations.A comparison of methods of representing polynomials in terms of coefficients is given by Gautschi [64]; the criterion of the comparison has several other applications.An algorithm for the Hermite interpolation method of Section 5.5 is described by Krogh [93]. A particularly elegant solution to Exercise 5.9,on the divided difference of a product,is in the book by de Boor [26]. Further information on the rational interpolation problem of Exercise 5.10 can be found in Mayers [110], Meinguet [111] and Wuytack [165].

The method of proof of the Weierstrass theorem, given in Chapter 6, is taken from Cheney [35]. The advantages of the Bernstein approximation method in interactive computing are explained by Gordon & Riesenfeld [68]. The convergence of the derivatives of the Bernstein approximations to the derivatives of the function that is being approximated is proved by Davis [5O],and the variation diminishing properties of Bernstein approximations are studied by Schoenberg [143].Many further properties of Bernstein polynomials are given by Lorentz [99].

The theory of Chapter 7 on minimax approximations is similar to the treatment in Rice [132]. An alternative approach, which is preferred by Cheney [35], by Rivlin & Shapiro [141] and by Watson [161], makes use of the properties of convex hulls. This approach is based on a necessary and sufficient condition for best minimax approximation, given by Kirchberger [9o], that depends only on the extreme values of the error function. Therefore our remark, that one only need consider extreme values of the error function to decide whether an approximation is optimal, has been known for many years. For further information on Chebyshev systems the book by Karlin & Studden [85] is recommended. A paper by Stiefel [156] directed attention to the usefulness of the bounds of Theorem 7.7.An extension of the result of Exercise 7.2 to the case when $\mathscr { A }$ is not a linear space is given by Curtis & Powell [47]. A good discussion of non-uniqueness of best approximations when the linear space $\mathscr { A }$ does not satisfy the Haar condition, which is the subject of Exercise 7.9, is in Watson [161].

It is mentioned in Chapter 8 that there are several versions of the exchange algorithm. The version that we give most attention to,that exchanges only one point of the reference on each iteration,and that brings into the reference a point where the current error function takes its maximum value, is due to Stiefel[156]. Another one-point method,which is proposed by Curtis & Frank [49] for minimax approximation on a discrete point set, is to alter the points of the reference in rotation. The version that can alter all of the reference on each iteration is studied by Murnaghan & Wrench [116]. Methods for updating matrix factorizations, in order to reduce the work of solving the system (8.4) on every iteration,are reviewed by Gill, Golub,Murray & Saunders [65]. For further reading on telescoping,the book by Lanczos [95] is recommended.Moreover, the gain in accuracy that can be obtained by calculating directly the best polynomial approximation of degree m to a polynomial of degree $\pmb { n }$ ,where $m \leqslant n - 2$ ,instead of using the telescoping technique $( n - m )$ times,is considered by Clenshaw [38], Lam & Elliott [94] and Talbot [158]. In order to apply the work of Section 8.5, one may replace a continuous interval $[ a , b ]$ by a set of discrete points; the effect of this replacement on the best minimax approximation is studied by Chalmers [33],Dunham [51]and Rivlin & Cheney[140].The relations between the discrete exchange algorithm and linear programming are explained by Rabinowitz [129], and a Fortran subroutine that is suitable for discrete minimax approximation is given by Barrodale &.Phillips [9].

The proof of the convergence of the exchange algorithm, given in the first two sections of Chapter 9,is similar to the theory of Dunham [52]. The analysis of the rate of convergence of the one-point exchange algorithm is new, but the quadratic rate of convergence of the version of the exchange algorithm that can alter all the reference points on each iteration was established by Veidinger [159]. The zero off-diagonal elements of the final second derivative matrix of the levelled reference error, which are stated in Exercise 9.8,were found by Curtis & Powell [48]. The presence of these zero second derivatives is implied by the convergence rate of the one-point exchange algorithm.

The book by Achieser [2] is recommended for the basic theory of rational approximation that is omitted from Chapter 10. Many descriptions of the exchange algorithm for the calculation of minimax rational approximations have been published,for instance see Curtis [44] and Maehly[1O5], because both of these papers give attention to the practical dificulties of the algorithm.An Algol listing of the algorithm is given by Werner,Stoer& Bommas [162].A good solution to the problem of replacing the eigenvalue calculation (10.16） by a suitably accurate finite calculation is proposed by Curtis & Osborne [46]. Methods for determining whether a system of linear constraints is consistent, which are required by the elementary linear programming methods of Section 10.4,are reviewed by Wolfe [164]. The differential correction algorithm is due to Cheney & Loeb [36],and the advantages of expression (10.38) over expression (10.36) are shown by Barrodale,Powell & Roberts [10].A numerical comparison of several algorithms for minimax rational approximation is made by Lee & Roberts [98], but more recently a procedure has been proposed by Kaufman, Leeming & Taylor [86], that combines the advantages of the exchange and the differential correction methods.Some of the diffculties that arise,if one prefers best rational approximations with respect to the 1-norm or 2-norm,are explained by Barrodale [8] and by Fraser [60].

The basic material of Chapter 11 is in many books on approximation theory and on numerical analysis,for example see Cheney [35],Davis [5O],Lawson & Hanson [97] and Rice [132]. There are also many publications on the numerical solution of discrete linear least squares problems without forming the normal equations,in particular the paper by Golub[67] is recommended.The application of the three-term recurrence relation of Theorem 11.3 to data fitting by polynomials was proposed by Forsythe [58].

Most of the results of Chapter 12 are in Hildebrand [78],which is an excellent book for further reading on Gaussian quadrature and special families of orthogonal polynomials. More properties of orthogonal polynomials are given by Szego [157]. The practical dificulties of adaptive quadrature are discussed by de Boor [2O],and he gives a suitable algorithm for this calculation.The material of Section 12.4 is one of the main topics of books on Chebyshev polynomials,for instance see Fox& Parker[59],Rivlin [139] and Snyder[153].The behaviour of the coefficients of the expansion of $\textstyle R _ { n } f$ in terms of Chebyshev polynomials when $f$ is analytic is studied by Elliott [53],and the relations between $\textstyle R _ { n } f$ and the best minimax approximation from ${ \mathcal { P } } _ { n }$ to $f$ are considered by Clenshaw [38]. The expression for $\| L _ { n } \| _ { \infty }$ in Exercise 12.6 is derived by Powell [121],and the Erdos-Turan theorem, which is the subject of Exercise 12.7,is proved in Cheney [35]. The calculation of polynomials that are orthogonal with respect to some ‘non-classical' weight functions is studied by Price [128],who suggests a technique that is similar to the one that is mentioned in Exercise 12.8.

The work of Chapter 13 is in most text-books on approximation,for instance see Cheney[35]and Rice [132]. For further reading on the theory of the Fourier series operator the book by Lanczos [96] is recommended. Interest in the FFT method has been strong during the last fteen years,due to the wide range of applications that were stimulated by the fundamental paper of Cooley & Tukey [39]. There is a book on Fast Fourier Transforms by Brigham [3O],an error analysis of the main procedure is given by Ramos [130], recent developments for the case when the number of data is not a power of two are in Winograd[163],and extensions for vector computers are considered by Korn & Lambiotte [91].

Except for Rice [132] and Watson [161],approximation books give little attention to the theory of best $L _ { 1 }$ approximations. These two books, however, cover the theory of Chapter 14.Further, the characteristic property that best $L _ { 1 }$ approximations depend on the sign of the error function is shown well by Barrodale [7]. The calculation of best $L _ { 1 }$ approximations by interpolation to $f$ at points that are independent of $f ,$ .which is suggested at the end of Section 14.3, is not restricted to the case when $\mathscr { A }$ satisfies the Haar condition, because Hobby & Rice [79]show the existence of interpolation points that may be suitable when $\mathcal { A }$ is any finite-dimensional linear space.

The proof of Jackson's first theorem, given in the first two sections of Chapter 15,is taken from Cheney [35],and the theory of discrete $L _ { 1 }$ approximation is in Rice[132],for instance. The application of linear programming methods to the solution of discrete $L _ { 1 }$ calculations was proposed by Barrodale & Young[13],and it is now an active field of research. The geometric view of linear programming, taken in Section 15.4,can be found in Abdelmalek [1] and in Bloomfield & Steiger [17]. The linear programming test for optimality,which is composed of a finite number of linear inequalities, is expressed in terms of the original $\scriptstyle { L _ { 1 } }$ approximation problem by Powell & Roberts [126]. The by-passing of vertices, recommended in Section 15.4,is included in the algorithm of Barrodale & Roberts [11], which has since been extended to allow general linear constraints on the parameters of the approximating function [12]. This algorithm defines each trial approximation by interpolation conditions,but Bartels, Conn & Sinclair[14] prefer a technique that reduces the $L _ { 1 }$ error on each iteration without the restriction of moving from vertex to vertex of the feasible region. A solution to Exercise 15.7,on the number of zeros of a best $L _ { 1 }$ approximation in the continuous case,is in Ascher [6].

The material of Chapter 16 can all be found in Cheney [35]. The optimality of the constant $\pi / 2 ( n + 1 )$ in inequality (16.2) is due to Achieser & Krein [3] and to Favard [54]. It is shown by Korneicuk [92] that the constant $\scriptstyle { \frac { 3 } { 2 } }$ in the bound (16.11) can be reduced to one. Substantial improvements to expression (16.5O) are made by Fisher[55]; he considers the construction of the least number $c ( k , n )$ such that $d _ { n } ^ { * } ( g )$ is bounded above $c ( k , n ) \| g ^ { ( k ) } \| _ { \infty }$ ，and he finds that the optimal value depends on properties of perfect splines,which are considered in Chapter 23.The optimal value of $c ( k , n )$ when $k = n + 1$ ,which is the subject of Exercise 16.5,is given by Phillips [119] and by Riess & Johnson [137].

The elementary theory of the first section of Chapter 17 can be found in most text-books on analysis,but the proof of the uniform boundedness theorem in Section 17.2 is new. Theorems 17.3 and 17.4 are taken from Cheney [35], who states that the minimum norm property of the Fourier series operator is due to Lozinski [1O1]. The problem of finding the linear projection operator from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to ${ \mathcal { P } } ^ { n }$ of least norm,which is suggested in Section 17.4,is considered briefly by Chalmers & Metcalf [34]. Because Theorems 17.2 and 17.4 imply that no prescribed interpolation method for calculating a sequence of polynomial approximations can give uniform convergence for all continuous functions, it is interesting that the Erdos-Turan theorem, stated in Exercise 12.7,shows that some interpolation methods give convergence in the 2-norm; similar convergence properties for other norms are studied by Nevai [118].

Due to the construction and the use of tables of function values,the methods of Section 18.1 are a smallsample from the techniques that are proposed in the older numerical analysis books for piecewise polynomial interpolation.Most of the material on spline functions in Chapter 18 can be found in de Boor [26]. The papers by Curtis [45] and Lucas [1O2] are also recommended for consideration of the two end-conditions of cubic spline interpolation. There are many publications on interpolation by splines of degree greater than three: for instance,in the case of equally spaced data,Richards [136] studies the norm of the interpolation operator,and Powell[123]draws attention to the deterioration of the localization properties.The unboundedness of the interpolation operator for unevenly spaced data points, mentioned in Exercise 18.2,is shown by Marsden [108] to apply also to cubic spline interpolation,but Kammerer & Reddien [83] prove that the accuracy of cubic spline interpolation is excellent, even for irregularly spaced data,when the approximand has a continuous fourth derivative.The bicubic splines of Exercise 18.10 are highly useful for surface approximation; many of their properties are studied by de Boor [18] and [26].

The theory of the first three sections of Chapter 19,on the properties of $\pmb { B } \mathrm { . }$ -splines and on the important idea of using them as a basis of a space of splie functions,is in Curry & Schoenberg [43]. A stronger form of Theorem 19.1,on the number of zeros of spline functions,is given by Schumaker [152]. The recurrence relation of Section 19.4 for the stable evaluation of $\pmb { B }$ -splines was proposed by de Boor [21] and Cox [40]; in later papers Cox [42] suggests another stable technique for the calculation of a linear combination of $\pmb { B }$ -splines,and de Boor [25] gives Fortran programs that calculate $\pmb { B } \mathrm { . }$ -splines and their derivatives. Theorem 19.4, on conditions for the solution of the general spline interpolation problem,is due to Schoenberg & Whitney[15O]. An algorithm for general spline interpolation is described by Cox [41],and de Boor [23] studies the norm of the general spline interpolation operator. The geometric interpretation of $\pmb { B }$ -splines, given in Exercise 19.1,was found by Curry & Schoenberg[43]. Rice[133] proves the theorem of Exercise 19.6 on the characterization of a best minimax approximation.The expression for the indefinite integral of a $\pmb { B }$ -spline that is stated in Exercise 19.8 is due to Gaffney[61].Exercise 19.10 shows some of the features of least squares spline approximations.There are several publications on this useful subject; for instance,the localization properties are studied by Powell[124] in the case when the knot spacing is constant, Reid [131] describes a way of organizing the calculation to take full advantage of the band matrices that come from the use of $\pmb { B }$ -splines,and de Boor [26] gives some computer programs.

So much has been published on the accuracy of spline approximations, that Chapter 2O gives only a small sample of the convergence theorems and the techniques of analysis.Many of our theorems have been proved in other ways.For example de Boor [19] uses divided differences to establish Theorem 20.1,and Marsden [107] strengthens Theorem 20.2 by applying Schoenberg's[147] ‘variation diminishing method'.This technique sets each variable $\scriptstyle { \pmb { x _ { p } } }$ in the definition (20.11) to the average of the non-trivial knots of $N _ { p }$ ,in order that $\pmb { s }$ is equal to $f$ for any $f$ in ${ \mathcal { P } } _ { 1 }$ ,see Marsden [1O6].Thus the accuracy and some variational properties of $\pmb { s }$ are similar to those of a Bernstein polynomial approximation to $f ,$ but $\pmb { \mathscr { s } }$ has the advantage that each $s ( x )$ depends only on the form of $f$ in a neighbourhood of $x .$ .Therefore Gordon & Riesenfeld [69] recommend the use of spline approximations in computer aided design.The method that is used in Section 20.2,to establish the order of convergence of best spline approximations when $f$ is differentiable,is taken from de Boor[19].For further reading on the construction and applications of local spline approximations, which are studied in Section 20.3, the papers by de Boor & Fix [27] and Lyche & Schumaker [103] are recommended. Substantial improvements to the error bounds of Section 20.4 are given in Chapter 22,and in Kammerer & Reddien [83] and Lucas [102].

The advantages of suiting the knot positions of spline approximations to singularities of the approximand,which are considered in Section 21.1,are shown well by Rice [135]. Moreover,Rice [134] explains clearly the behaviour of the functions in the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ when the knots tend to coincide. Theorem 21.2,on the norm of a quadratic spline interpolation operator, is due to Marsden [1O9]. The adaptive method for the calculation of a cubic spline approximation,given in Section 21.3,is described by Curtis [45]. An algorithm that uses a similar disposition of knots is proposed by Powell [125] for least squares approximation to discrete data. An alternative to inserting knots near a singularity is to adjust the positions of a fixed number of knots; Jupp [82] considers the application of general optimization procedures to this calculation, and de Boor & Rice [29] present a tailored algorithm,where in both cases the least squares norm of the error function is minimized.Some theoretical properties of optimal knot positions in minimax and least squares approximation are given by Handscomb [75] and Powell[122] respectively.

Conditions for the validity of the Peano kernel theorem,which is studied in Chapter 22,are in Davis [50] for instance.Applications of this important theorem are plentiful in the numerical analysis literature; in particular the analysis of the accuracy of Bernstein polynomial approximation that is given by Stancu [154], and Kershaw's [88]results on estimating derivatives of a function by differentiating a spline approximation to the function,are both highly relevant to our studies. Theorem 22.3,stating that a $\pmb { B }$ -spline is the Peano kernel of a divided difference, is in Curry & Schoenberg [43]. The calculation of Section 22.4 is not new, the constant $\frac { 5 } { 3 8 4 }$ of expression (22.64) being derived by both Hall [71] and Schultz [151].An interesting generalization of a property that is shown in Figure 22.1 is proved by Hall & Meyer [73]; it is that the Peano kernel function of cubic spline interpolation changes sign at the data points even when the spacing of the data is irregular,provided that the knots of the spline remain at the data points.

Many publications are relevant to the work of Chapter 23.The solution of the variational problem of Section 23.1 is due to Holladay [8O],and it was generalized by Schoenberg [144] to give the properties of natural splines that are stated in Theorems 23.1 and 23.2. Theorem 23.3 is also due to Schoenberg [145], but a different approach to functional approximation by Golomb & Weinberger [66] had already established a similar result. This theorem is applied in many papers to calculate the weights of quadrature formulae; see Schoenberg[148] for a review of this field. The accuracy of natural spline interpolation is analysed by Schoenberg[146], but not making full use of the degrce of the spline at the ends of the range is a disadvantage.However,both Hall [72]and Kershaw [87] show that,for cubic spline interpolation to equi-spaced data, the disadvantage is negligible at any interior point of the range in the limit as the interval between data points tends to zero.The norm of the natural spline interpolation operator for general data points is studied by Neuman [117]. The fact that perfect splines solve the variational problem of Theorem 23.4 was proved by de Boor [22] and [24] and Karlin [84] independently,allowing for the Hermite interpolation case where suitable derivatives of $f$ are given if data points coincide.For further reading on perfect splines, including results on uniqueness,the papers by Fisher & Jerome [56], Karlin [84], McClure [104] and Pinkus [120] are recommended.

The optimal interpolation problem, that is studied in Chapter 24,was solved independently and differently by Gaffney & Powell [63] and by Micchelli,Rivlin & Winograd [114], but several properties of the solution were known already, see Meinguet [112] for instance.Most of the theory of Section 24.2 is in Karlin & Studden [85],including the relation between $\pmb { B }$ -splines and Chebyshev sets that is stated in Theorem 24.2. An algorithm that calculates the optimal interpolating function in the way that is suggested by Theorem 24.4 is given by Gaffney [62].

The uniqueness of the perfect spline $\pmb { \sigma } _ { : }$ ,stated in Exercise 24.9,is proved by Karlin [84] and by Micchelli [113].

# References

solutions of overdetermined linear equations', J. Approx. Theory, 11 (1974) 38-53.   
[2] N. I. Achieser, Theory of Approximation (1947), translation published by Ungar, New York (1956).   
[3] N. I. Achieser & M. G. Krein, ‘Best approximation of differentiable periodic functions by means of trigonometric sums',Doklady Akad. Nauk SSSR,15 (1937) 107-111.   
[4] J. H. Ahlberg,E. N. Nilson & J.L. Walsh, The Theory of Splines and their Applications, Academic Press,New York (1967).   
[5] D.H. Anderson & M. R. Osborne,‘Discrete linear approximation problems in polyhedral norms',Numer.Math.,26 (1976) 179-189.   
[6] U. Ascher,On the invariance of the interpolation points of the discrete $L _ { 1 }$ approximation',J. Approx. Theory,24 (1978) 83-91.   
[7] I. Barrodale,‘On computing best $L _ { 1 }$ approximations', in Approximation Theory,ed.A. Talbot, Academic Press,London (1970).   
[8] I. Barrodale,Best rational approximation and strict quasi-convexity', SIAM J. Numer. Anal.,10 (1973) 8-12.   
[9] I. Barrodale & C.Phillips,‘Solution of an overdetermined system of linear equations in the Chebyshev norm',ACM Trans.Math. Software,1(1975) 264-270.   
[10]I.Barrodale,M. J.D.Powell & F.D.K.Roberts，‘The differential correction algorithm for rational $L _ { \infty }$ approximation', SIAM J. Numer. Anal.,9 (1972) 493-504.   
[11] I. Barrodale & F.D. K. Roberts,‘An improved algorithm for discrete $L _ { 1 }$ linear approximation', SIAM J. Numer. Anal.,10 (1973) 839-848.   
[12] I. Barrodale & F.D.K. Roberts,‘An efficient algorithm for discrete $L _ { 1 }$ linear approximation with linear constraints', SIAM J. Numer. Anal., 15 (1978) 603-611.   
[13] I. Barrodale & A. Young,‘Algorithms for best $L _ { 1 }$ and $L _ { \infty }$ linear approximations on a discrete set, Numer. Math.,8 (1966) 295-306.   
[14] R.H. Bartels,A.R. Conn & J.W. Sinclair,‘Minimization techniques for piecewise differentiable functions: the $L _ { 1 }$ solution to an overdetermined linear system', SIAM J. Numer. Anal.,15 (1978) 224-241.   
[15] G.Birkhoff & C.de Boor,‘Piecewise polynomial interpolation and approximation', in Approximation of Functions,ed. H.L. Garabedian, Elsevier Publishing Co.,Amsterdam (1965).   
[16] G. Blanch,‘On modified divided differences I', Maths. of Comp.,8 (1954) 1-11.   
[17] P. Bloomfield & W. Steiger,‘Least absolute deviations curve-fitting', SIAM Stat. Comp., in press.   
[18] C. de Boor,‘Bicubic spline interpolation', J. of Maths.and Physics, 41 (1962) 212-218. (1968) 219-235.   
[20] C.deBoorOnwritinganautomaticintegrationalgorithm,inMatheatical Software, ed. J. R. Rice, Academic Press, New York (1971).   
[21] C. de Boor,‘On calculating with $B$ -splines', J. Approx. Theory,6 (1972) 50-62.   
[22] C.de Boor,'Aremark concerning perfect splines',Bull.Amer. Math.Soc., 80 (1974) 724-727.   
[23] C.de Boor,'On bounding spline interpolation’, J. Approx. Theory,14 (1975) 191-203.   
[24] C.de Boor,‘On "best" interpolation',J. Approx. Theory,16(1976) 28-42.   
[25] C. de Boor,‘Package for calculating with $\pmb { B }$ splines', SIAM J. Numer. Anal.,14 (1977) 441-472.   
[26] C.de Boor,A Practical Guide to Splines, Springer-Verlag, New York (1978).   
[27] C. de Boor & G.J. Fix,‘Spline approximation by quasi-interpolants', J. Approx. The0ry,8 (1973) 19-45.   
[28] C.de Boor & A. Pinkus,‘Proof of the conjectures of Bernstein and Erdos concerning the_optimal nodes for polynomial interpolation', J. Approx. Theory,24 (1978) 289-303.   
[29] C. de Boor & J. R. Rice,Least squares cubic spline approximation IIvariable knots'，Report No.CSD TR 21， Purdue University，Indiana (1968).   
[30] E.O. Brigham, The Fast Fourier Transform,Prentice-Hall, Englewood Cliffs, N.J. (1974).   
[31] L. Brutman,‘On the Lebesgue function for polynomial interpolation', SIAM J. Numer. Anal., 15 (1978) 694-704.   
[32] R. C. Buck,Linear spaces and approximation theory', in On Numerical Approximation,ed.R.E.Langer, University of Wisconsin Press, Madison (1959).   
[33] B.A.Chalmers,On the rate of convergence of discretization in Chebyshev approximation', SIAM J. Numer. Anal.,15 (1978) 612-617.   
[34] B.L. Chalmers & F. T. Metcalf,‘On the computation of minimal pro-jections from $\mathcal { C } [ 0 , 1 ]$ to $\mathcal { P } _ { n } [ 0 , 1 ] ^ { , }$ ,in Approximation Theory II, eds.G.G. Lorentz,C.K. Chui & L.L. Schumaker,Academic Press,New York (1976).   
[35] E.W.Cheney,Introduction to Approximation Theory, McGraw-Hil, New York (1966).   
[36] E.W. Cheney & H. L. Loeb,‘On rational Chebyshev approximation, Numer. Math.,4 (1962) 124-127.   
[37] E.W. Cheney & K. H. Price, Minimal projections', in Approximation Theory, ed. A. Talbot, Academic Press,London (1970).   
[38] C.W. Clenshaw,‘A comparison of "best" polynomial approximations witl. truncated Chebyshev series expansions', SIAMJ. Numer. Anal.,1·(1964) 26-37.   
[39] J. W. Cooley & J. W. Tukey,‘An algorithm for the machine calculation of complex Fourier series',Maths.of Comp.,19 (1965) 297-301.   
[40] M. G. Cox,‘The numerical evaluation of $B$ -splines'， J. Inst. Maths. Applics.,10 (1972) 134-149.   
[41] M. G.Cox,An algorithm for spline interpolation',J. Inst. Maths. Applics., 15 (1975) 95-108.   
[42] M. G. Cox,‘The numerical evaluation of a spline from its $\pmb { B }$ -spline representation',J. Inst. Maths.Applics.,21(1978) 135-143.   
[43] H. B. Curry & I. J. Schoenberg,‘On Polya frequency functions IV. The fundamental spline functions and their limits’,J.d'Analyse Math.,17 (1966) 71-107.   
[44] A. R. Curtis,‘Theory and calculation of best rational approximations',in Methods of Numerical Approximation, ed. D. C. Handscomb, Pergamon Press,Oxford (1966).   
[45] A. R. Curtis,‘The approximation of a function of one variable by cubic splines', in Numerical Approximation to Functions and Data, ed. J.G. Hayes,The Athlone Press,London (1970).   
[46] A.R. Curtis & M. R. Osborne,‘The construction of minimax rational approximations to functions', Computer Journal,9 (1966) 286-293.   
[47] A. R. Curtis & M. J. D. Powell,‘Necessary conditions for a minimax approximation', Computer Journal,8 (1966) 358-361.   
[48] A.R. Curtis & M. J. D. Powell, On the convergence of exchange algorithms for calculating minimax approximations', Computer Journal, 9 (1966) 78-80.   
[49] P.C. Curtis & W.L. Frank,‘An algorithm for the determination of the polynomial of best minimax approximation to a function defined on a finite point set',J.Assoc. Comp.Mach.,6 (1959) 395-404.   
[50] P.J. Davis,Interpolation and Approximation, Blaisdell Publishing Co., Waltham,Mass. (1963).   
[51] C. B. Dunham,‘Efficiency of Chebyshev approximation on finite subsets', J. Assoc. Comp. Mach.,21 (1974) 311-313.   
[52] C. B. Dunham,‘Convergence of Stiefel's exchange method on an infinite set', SIAM J. Numer. Anal.,11(1974) 729-731.   
[53] D.Elliott,‘The evaluation and estimation of the coefficients in the Chebyshev series expansion of a function’, Maths. of Comp.,18 (1964) 274-284.   
[54] J.Favard, Sur les meilleurs proceédés d'approximation de certaines classes de fonctions par des polynomes trigonometriques'， Bull. des Sciences Math.,61 (1937) 209-224.   
[55] S.D. Fisher,‘Best approximation by polynomials', J. Approx. Theory,21 (1977)43-59.   
[56] S.D.Fisher & J.W. Jerome,‘Perfect spline solutions to $L _ { \infty }$ extremal problems', J. Approx. Theory,12(1974) 78-90.   
[57] R. Fletcher, J.A. Grant & M. D. Hebden, Linear minimax approximation as the limit of best $L _ { p }$ -approximation', SIAM J. Numer. Anal.,11 (1974) 123-136.   
[58] G.E. Forsythe,‘Generation and use of orthogonal polynomials for data fitting with a digital computer', SIAM Journal, 5 (1957) 74-88.   
[Jy」 L. rux & 1. D. raikei, Cnevysnev rolynomiuis in vumericul Analysis, Oxford University Press,London (1968).   
[60] W.Fraser,‘Examples of best discrete $L _ { 1 }$ and $L _ { 2 }$ rational approximations', J. Approx. The0ry,27 (1979) 249-253.   
[61] P.W. Gafney,The calculation of indefinite integrals of $B ^ { \prime }$ -splines', J. Inst. Maths. Applics.,17 (1976) 37-41.   
[62] P. W. Gaffney,To compute the optimal interpolation formula', Maths. of Comp., 32 (1978) 763-777.   
[63] P.W. Gaffney & M. J.D.Powell,‘Optimal interpolation', in Numerical Analysis Dundee 1975,Lecture Notes in Mathematics No. 506, ed. G. A. Watson, Springer-Verlag, Berlin (1976).   
[64] W. Gautschi, The condition of polynomials in power form', Maths. of Comp., 33 (1979) 343-352.   
[65] P. E. Gill, G.H. Golub,W. Murray & M. A. Saunders,‘Methods for modifying matrix factorizations',Maths.of Comp.,28 (1974) 505-535.   
[66] M. Golomb & H. F. Weinberger,‘Optimal approximation and error bounds', in On Numerical Approximation, ed.R.E.Langer,University of Wisconsin Press,Madison (1959).   
[67] G. H. Golub,‘Numerical methods for solving linear least squares problems',Numer. Math.,7 (1965) 206-216.   
[68] W. J. Gordon & R.F. Riesenfeld,‘Bernstein-Bézier methods for the computer-aided design of free-form curves and surfaces', J. Assoc. Comp. Mach.,21 (1974) 293-310.   
[69] W. J. Gordon & R.F. Riesenfeld,‘B-spline curves and surfaces', in Computer Aided Geometric Design, eds. R.E. Barnhill& R.F.Riesenfeld, Academic Press, New York (1974).   
[70] T. N. E. Greville,Introduction to spline functions', in Theory and Applications of Spline Functions, ed. T. N. E. Greville, Academic Press, New York (1969).   
[71] C. A. Hall :On error bounds for spline iterpolation’, J. Approx. Theory,1 (1968)209-218.   
[72] C. A. Hall,‘Natural cubic and bicubic spline interpolation’, SIAM J. Numer. Anal.,10 (1973) 1055-1060.   
[73] C. A. Hall & W. W. Meyer,‘Optimal error bounds for cubic spline interpolation',J. Approx. Theory,16 (1976) 105-122.   
[74] D. C. Handscomb (ed.), Methods of Numerical Approximation, Pergamon Press,Oxford (1966).   
[75] D. C. Handscomb,‘Characterization of best spline approximations with free knots', in Approximation Theory, ed. A. Talbot, Academic Press, London (1970).   
[76] C. Hastings,Approximations for Digital Computers, Princeton University Press, Princeton (1955).   
[77] J. G. Hayes (ed.), Numerical Approximation to Functions and Data, The Athlone Press,London (1970).   
[78] F. B. Hildebrand,Introduction to Numerical Analysis,McGraw-Hill, New York (1956).   
[/y」C. K. nuvvy & J.K. rice,A imuent piuvie m $L _ { 1 }$ approxiauon,rroc. Amer. Math. Soc.,16 (1965) 665-670.   
[80] J. C. Holladay,‘A smoothest curve approximation', Maths. of Comp., 11 (1957) 233-243.   
[81] A.S. B. Holland & B. N. Sahney, The General Problem of Approximation and Spline Functions, Krieger Publishing Co., Huntington, N.Y. (1979).   
[82] D.L. B. Jupp,‘Approximation to data by splines with free knots', SIAMJ. Numer. Anal.,15 (1978) 328-343.   
[83] W.J. Kammerer & G. W. Reddien,‘Local convergence of smooth cubic spline interpolates', SIAM J. Numer. Anal.,9 (1972) 687-694.   
[84] S. Karlin,‘Interpolation properties of generalized perfect splines and the solutions of certain extremal problems', Trans. Amer. Math. Soc. 206 (1975) 25-66.   
[85] S. Karlin & W.J. Studden, Tchebyscheff Systems: with Applications in Analysis and Statistics, Interscience,New York (1966).   
[86] E.H. Kaufman, D.L. Leeming & G.D. Taylor,‘A combined Remes - differential correction algorithm for rational approximation', Maths. of Comp.,32 (1978) 233-242.   
[87] D. Kershaw,'A note on the convergence of interpolatory cubic splines', SIAMJ. Numer. Anal., 8 (1971) 67-74.   
[88] D. Kershaw,The orders of approximation of the first derivative of cubic splines at the knots,Maths. of Comp.,26 (1972) 191-198.   
[89] T. A. Kilgore, A characterization of the Lagrange interpolating pro-jection with minimal Tchebycheff norm', J. Approx. Theory,24 (1978) 273-288.   
[90] P. Kirchberger，'Uber Tchebychefsche annaherungsmethoden'， Math. Ann., 57 (1903) 509-540.   
[91] D.G. Korn & J.L.Lambiotte,Computing the Fast Fourier Transform on a vector computer',Maths.of Comp., 33 (1979) 977-992.   
[92] N.P. Korneichuk, The exact constant in D. Jackson's theorem on best uniform approximation of continuous periodic functions',Doklady Akad. Nauk SSSR,145 (1962) 514-515.   
[93] F. T. Krogh,‘Eficient algorithms for polynomial interpolation and numerical differentiation', Maths. of Comp., 24 (1970) 185-190.   
[94] B.Lam & D.Ellott, Onaconjectureof C. W.Clenshaw',SIAMJ. Numer. Anal.,9 (1972) 44-52.   
[95] C.Lanczos, Applied Analysis，Prentice-Hall, Englewood Clifs，N.J. (1956).   
[96] C.Lanczos,Discourse on Fourier Series,Oliver & Boyd,Edinburgh (1966).   
[97] C.L.Lawson & R.J. Hanson, Solving Least Squares Problems, Prentice-Hall,Englewood Cliffs,N.J. (1974).   
[98] C.M.Lee & F.D. K. Roberts, A comparison of algorithms for rational $L _ { \infty }$ approximation', Maths.of Comp.,27 (1973) 111-121.   
[99] G. G.Lorentz,Bernstein Polynomials, University of Toronto Press, Toronto (1953).   
100] G. G. Lorentz, Approximation of Functions, Holt, Rinehart & Winston, New York (1966).   
[101] S. M. Lozinski, ‘On a class of linear operators', Doklady Akad. Nauk SSSR,61 (1948) 193-196.   
[102] T. R. Lucas,‘Error bounds for interpolating cubic splines under various end conditions', SIAM J. Numer. Anal.,11 (1974) 569-584.   
[103] T. Lyche & L. L. Schumaker,‘Local spline approximation methods',J. Approx.The0ry,15 (1975) 294-325.   
[104] D. E. McClure,‘Perfect spline solutions of $L _ { \infty }$ extremal problems by control methods',J. Approx. Theory,15 (1975) 226-242.   
[105]H.J. Maehly,‘Methods for fiting rational approximations,Parts II and III',J. Assoc. Comp. Mach.,10 (1963) 257-277.   
[106] M. J. Marsden,‘An identity for spline functions with applications_to variation-diminishing spline approximation',J.Approx. Theory,3 (1970) 7-49.   
[107] M. J. Marsden,‘On uniform spline approximation', J. Approx. Theory, 6 (1972) 249-253.   
[108] M. J. Marsden,‘Cubic spline interpolation of continuous functions, J. Approx. The0ry,10 (1974) 103-111.   
[109]M.J.Marsden,Quadraticspline interpolation',Bull.Amer.Math.Soc,80 (1974) 903-906.   
[110] D.F. Mayers,‘Interpolation by rational functions',in Methods of Numerical Approximation,ed.D.C.Handscomb,Pergamon Press,Oxford (1966).   
[111] J. Meinguet,‘On the solubility of the Cauchy interpolation problem', in Approximation Theory,ed.A. Talbot,Academic Press, London (1970).   
[112] J. Meinguet,Optimal approximation and interpolation in normedspaces', in Numerical Approximation to Functions and Data,ed. J. G. Hayes, The Athlone Press,London (1970).   
[113] C. A. Micchelli, 'Best $\mathbf { { { L } } _ { 1 } }$ approximation by weak Chebyshev systems and the uniqueness of interpolating perfect splines', J. Approx. Theory, 19 (1977) 1-14.   
[114] C. A. Miccheli, T. J. Rivlin & S. Winograd, The optimal recovery of smooth functions',Numer. Math., 26 (1976) 191-200.   
[115] J. C.P.Miller,Checking by differences I', Maths. of Comp.,4 (1950) 3-11.   
[116] F. D. Murnaghan & J. W. Wrench, The determination of the Chebyshev approximating polynomial for a differentiable function', Maths. of Comp., 13 (1959) 185-193.   
[117] E. Neuman,Bounds for the norm of certain spline projections',J. Approx. Theory,27 (1979) 135-145.   
[118] G. P. NevaiMean convergence of Lagrange interpolation,I',J. Approx. Theory,18 (1976) 363-377.   
[119]G.M.Phillips，‘Estimate of the maximum error in best polynomial approximations',Computer Journal,11(1968) 110-111.   
[120] A. Pinkus,‘Some extremal properties of perfect splines and the pointwise Landau problem on the finite interval',J. Approx. Theory,23 (1978) 37-64.   
[121] M. J. D. Powell, On the maximum errors of polynomial approximations defined by interpolation and by least squares criteria', Computer Journal,9 (1967) 404-407. Mathematik, Differentialgleichungen, Approximationstheorie, Birkhauser Verlag,Basel (1968).   
[123] M. J. D. Powell, A comparison of spline approximations with classical interpolation methods', in Proceedings IFIP Congress,Edinburgh,1968, North-Holland,Amsterdam (1969).   
[124]M. J. D. Powell,‘The local dependence of least squares cubic splines', SIAM J. Numer. Anal.,6 (1969) 398-413.   
[125] M. J. D. Powell,‘Curve fiting by splines in one variable', in Numerical Approximation to Functions and Data, ed.J.G. Hayes,The Athlone Press, London (1970).   
[126] M. J. D. Powell & F.D.K. Roberts,A discrete characterization theorem for the discrete $L _ { 1 }$ linear approximation problem', J. Approx. Theory, in press.   
[127] P. M. Prenter,Splines and Variational Methods, John Wiley & Sons Inc., New York (1975).   
[128]T.E. Price,‘Orthogonal polynomials for nonclasical weight functions, SIAMJ. Numer. Anal.,16 (1979) 999-1006.   
[129] P.Rabinowitz,'Applicationsof linear programming to numerical analysis', SIAM Review,10 (1968) 121-159.   
[130] G. U. Ramos,Roundoff error analysis of the Fast Fourier Transform', Maths. of Comp.,25 (1971) 757-768.   
[131] J. K. Reid,‘A note on the least squares solution of a band system of linear equations by Householder reductions',Computer Journal,1o (1967) 188-189.   
[132] J. R. Rice, The Approximation of Functions: vol.1, Linear Theory, Addison-Wesley Publishing Co., Reading,Mass. (1964).   
[133] J. R. Rice,‘Characterization of Chebyshev approximations by splines', SIAM J. Numer. Anal., 4 (1967) 557-565.   
[134] J. R. Rice, The Approximation of Functions: vol. 2, Nonlinear and Multivariate Theory,Addison-Wesley Publishing Co.,Reading,Mass. (1969).   
[135] J. R. Rice,‘On the degree of convergence of nonlinear spline approximation',in Approximation with Special Emphasis on Spline Functions,ed. I. J. Schoenberg, Academic Press, New York (1969).   
[136] F. Richards,The Lebesgue constants for cardinal spline interpolation', J. Approx. Theory,14 (1975) 83-92.   
[137]R.D.Riess &L.W.Johnson,Errors ininterpolatingfunctions atthezeros of $T _ { n + 1 } ( x ) ^ { \prime }$ , SIAM J. Numer. Anal., 11 (1974) 244-253.   
[138] T.J. Rivlin,An Introduction to the Approximation of Functions, Blaisdell Publishing Co., Waltham, Mass. (1969).   
[139] T. J. Rivlin, The Chebyshev Polynomials,John Wiley & Sons Inc., New York (1974).   
[140] T.J. Rivlin& E. W. Cheney,‘A comparison of uniform approximations on an interval and a finite subset thereof', SIAM J. Numer. Anal., 3 (1966) 311-320.   
[141] T. J. Rivlin & H. S. Shapiro,‘A unified approach to certain problems of approximation and minimization', SIAM Journal, 9 (1961) 670-699.

[142] R.T.Rockafellar, Convex Analysis,Princeton University Press,Princeton (1970).

[143] I.J.Schoenberg,‘On variation diminishing approximation methods, in $o _ { n }$ Numerical Approximation, ed. R.E. Langer, University of Wisconsin Press, Madison (1959).   
[144] I. J. Schoenberg,‘On interpolation by spline functions and its minimal properties', in On Approximation Theory,eds. P.L. Butzer & J. Korevaar, Birkhäuser Verlag, Stuttgart (1964).   
[145] I.J.Schoenberg,‘Spline interpolation and best quadrature formulae',Bull. Amer. Math. Soc.,70 (1964) 143-148.   
[146] I. J. Schoenberg,‘Spline interpolation and the higher derivatives', Proc. Nat. Acad. Sci. U.S.A.,51 (1964) 24-28.   
[147] I. J. Schoenberg,‘On spline functions', in Inequalities, ed. O. Shisha, Academic Press,New York (1967).   
[148] I. J. Schoenberg,‘Monosplines and quadrature formulae', in Theory and Applications of Spline Functions, ed. T.N. E. Greville, Academic Press, New York (1969).   
[149] I. J. Schoenberg, Cardinal Spline Interpolation, Regional Conference Series in Applied Mathematics No.12, SIAM,Philadelphia (1973).   
[150] I. J. Schoenberg & A.Whitney,‘On Polya frequency functions, II. The positivity of translation determinants with an application to the inter-polation problem by spline curves', Trans. Amer. Math. Soc.,74 (1953) 246-259.   
[151] M. H. Schultz, Spline Analysis, Prentice-Hall, Englewood Cliffs,N.J. (1973).   
[152] L. L. Schumaker,‘Zeros of spline functions and applications', J. Approx. Theory,18 (1976) 152-168.   
[153] M.A.Snyder, Chebyshev Methods in Numerical Approximation,Prentice-Hall,Englewood Cliffs,N.J. (1966).   
[154] D.D. Stancu,Evaluation of the remainder term in approximation formulas by Bernstein polynomials',Maths. of Comp.,17 (1963) 270-278.   
[155] J. F. Steffensen, Interpolation,Chelsea Publishing Co., New York (1927).   
[156] E.L. Stiefel,‘Numerical methods of Tchebychef approximation', in On Numerical Approximation,ed.R.E. Langer, University of Wisconsin Press, Madison (1959).   
[157] G. Szego, Orthogonal Polynomials,Amer. Math. Soc. Colloquium Publications,No.23 (1939).   
[158] A. Talbot,The uniform approximation of polynomials by polynomials of lower degree', J. Approx. Theory,17 (1976) 254-279.   
[159] L. Veidinger,On the numerical determination of the best approximations in the Chebyshev sense', Numer. Math.,2 (1960) 99-105.   
[160] A.G. Vitushkin, Theory of the Transmission and Processing of Information (transl.), Pergamon Press, Oxford (1961).   
[161] G.A. Watson,Approximation Theory and Numerical Methods,John Wiley & Sons,Chichester (1980).   
[162] H. Werner,J. Stoer & W. Bommas,‘Rational Chebyshev approximation', Numer. Math.,10 (1967) 289-306.   
[163] S.Winograd,‘On computing the discrete Fourier transform',Maths. of Comp.,32 (1978) 175-199.   
[164] P.Wolfe, The composite simplex algorithm', SIAM Review,7 (1965) 42-54.   
[165] L.Wuytack,‘On some aspects of the rational interpolation problem', SIAMJ. Numer. Anal.,11 (1974) 52-60.

# algebraic polynomial, see polynomial

$\pmb { B }$ -splines basis of space of splines 231-4 calculation of values and recurrence relation 234-6 definite integral 275 definition 229 derivation by divided differences 236 Haar condition 301-2 in analysis of optimal interpolation 300-6 in analysis of perfect splines 290-4 indefinite integral 240 in minimization of $\left\| s ^ { \prime \prime } \right\| _ { 2 }$ subject to interpolation conditions 283-5 in proof of uniform convergence of spline approximation 241-3 non-negativity conditions 229-31 Peano kernel of divided difference 274-6,283-5,290-1,300   
basis functions in least squares calculations 126-31, 240 in polynomial approximation 33,51-3, 131-3 in spline approximation 29-30, 227-8, 231-4   
Bernstein approximation 65-9   
Bessel's inequality 155   
best approximation characterization,see characterization theorems continuity of operator 16-17 definition and existence 4-6 geometric view 9-11 uniqueness of solution 14-16   
bicubic splines 226   
bounds,see error bounds and norm of operator   
cardinal functions in analysis of Gaussian quadrature 138-40 piecewise polynomial interpolation 214-15 polynomial interpolation 33-5 spline interpolation 216-19,222-3   
characterization theorems for $L _ { 1 }$ approximation 165-9,181-2 least squares approximation 125-6,296 minimax approximation 75-7,79,112- 13,120-1,239-40 orthogonal polynomials 141   
Chebyshev interpolation points 39-41   
Chebyshev polynomials definition and recurrence relation 38-9, 142 in telescoping 92 in the Chebyshev least squares operator $R _ { n }$ 144-5 minimal property 78 orthogonality conditions 144   
Chebyshev set,see Haar condition   
continuity_of best approximation operator 16-17   
convergence,see also order of convergence and uniform convergence of Fourier series 155-6,193 of the differential correction algorithm 120-2 of the exchange algorithm 93,101-2, 105-8, 116-17   
convexity 13-19   
cubic polynomial defined by Hermite interpolation 213   
cubic spline,see spline approximation by Bernstein derivative 67-9 approximation by spline derivative 253 conditions in Hermite interpolation 53-7 discontinuities of spline functions 220, 224,261-5 minimal property of natural spline 283- 5,287-90 minimal property of perfect spline 292-5 relation to divided difference 47   
difference,see divided difference   
diferential correction algorithm 119-22   
Dini-Lipschitz theorem 193   
discrete approximation by a rational function 112-13,117-20 by a trigonometric polynomial 156-61 by the exchange algorithm 92-4,117 in the $L _ { 1 }$ -norm 18-19,181-6 in the least squares norm 124-5,133, 157-8 in the minimax norm 19,79,92-4, 112-13,118-20 linear programming methods,see lineal programming to continuous problems 118-19,156, 186   
distance function 4-5,11   
divided difference checking of tables 47,59 definition 46 derivation of $\pmb { B }$ -splines 236 expression from the Peano kernel theorem 274-6,283-5,290-1,300 for Newton's interpolation method 48-9 of equi-spaced data 59 of product 59,236 recurrence relation 49-51 relation to derivative 47 when there are repeated arguments 55-7   
eigenvalue problem in rational exchange algorithm 113-15   
end conditions in spline interpolation 216,219-21,223-5,285   
equivalence of operators 201-2   
Erdos-Turan theorem 148   
error bounds,see also order of convergence for linear projection operators 24-5 in cubic spline interpolation 277-81 in optimal interpolation 309-10 I uc canang aiguiiu o1-, ov,v, 113   
error estimates in cubic spline interpolation 261-5   
error expressions derived by the Peano kernel theorem 268,276-82 for Gaussian quadrature 147 for polynomial interpolation 35-6,276 in the exchange algorithm,see levelled reference error   
Euclidean,see least squares   
exchange algorithm,see also levelled reference error adjustment of reference 87-8,93,112 bounds on the minimax error 81-2, 86, 90,113 description 85-8,93,112-15 initial reference 85,90-1 in the discrete case 92-4,117 in the rational case 112-18 minimax approximation on a reference 79,85-6,112-13 numerical example 88-90 proof of convergence 93,101-2, 116-17 rate of convergence 105-8 separation of reference points 100-1   
existence of best approximations 4-6 minimax rational approximations 12, 113   
extended space of spline functions 255-7   
fast Fourier transform 158-61   
Fejer operator 162-3   
first derivative recurrence relation of cubic spline 216   
Fourier series Bessel's inequality 155 convergence properties 155-6,193 Dini-Lipschitz theorem 193 fast Fourier transform 158-61 in the continuous case 152-6 in the discrete case 156-8 minimal property of norm 206-8 norms and their bounds 155,192-3   
Gaussian quadrature derivation 138-9 error expression 147 positive coefficients 140   
geometric view of linear programming 184-6 norms and best approximation 9-11   
Haar condition definition and properties 76-7,313-16 in analysis of the exchange algorithm 98-108 in $L _ { 1 }$ approximation 169-72,175 in minimax approximation 77,79-82, 90 of space of $\pmb { B }$ -splines 301-2   
Hermite interpolation by a cubic polynomial 213 an extension of Newton's method 53-7   
Hermite polynomials 143   
Hilbert space 17,123-6   
ill-conditioning of a spline basis 227-8 of normal equations 127-8,134   
increase in levelled reference error 87, 97-9, 116-17   
integrals and integration, see quadrature   
interpolation by a piecewise polynomial 29,212-15 by a polynomial,see polynomial interpolation by a rational function 44-5,59-60 bya spline,see spline interpolation by a trigonometric polynomial 161 cardinal functions 33-5,214-19,222-3 optimal, see optimal interpolation points for $L _ { 1 }$ approximation 170-4, 301-6   
Jackson's theorems extension to algebraic polynomials 195-8 for a continuous function 189-93, 196-7 for a differentiable function 179-81, 197-8 fora highly differentiable function 194- 5,197-8 for a Lipschitz continuous function 190, 196-7   
Jacobi polynomials 142   
kernel functions Fejer kernel 162-3 Fourier series kernel 154-5 Peano kernel 270-4   
knots of spline functions algorithm for choosing them automatically 261-6 change of spacing in cubic spline interpolation 263-5 coincident knots 255-7 definition 29-30 extra knots for $\pmb { B }$ -spline basis231-4 fitting to a singularity 254-7,266-7 in best least squares approximation 296 in optimal interpolation 308-9 in perfect spline interpolation 294-5 in quadratic spline interpolation 221-4, 257-61 relation to zeros of spline 230-1,237- 8,293-4,306   
$L _ { 1 }$ approximation byalgebraic polynomials172-4 by linear combination of $\pmb { B }$ -splines 300-6 by trigonometric polynomials 176 characterization theorems 165-9, 181-2 definition of $L _ { 1 }$ -norm 6-7,164 example for proof of Jackson's theorem 177-9 interpolation points 170-4,301-6 in the discrete case 18-19,181-6 methods of calculation 171-2,177-9, 183-6 non-uniqueness of best approximation 18-19,187 relation to least squares approximation 168 uniqueness of best approximation 170, 175 when the Haar condition holds 169-72, 175   
$L _ { 2 }$ approximation,see least squares approximation   
$L _ { \infty }$ approximation, see minimax approximation   
$L _ { p }$ approximation condition for best approximation 168-9 definition of norm 6-7 uniqueness of best approximation 16   
Lagrange interpolation description 33-5 discussion of stability 52-3   
Laguerre polynomials 143   
least maximum approximation,see minimax approximation   
least squares approximation basis functions 126-31,240 by algebraic polynomials 131-3 by spline functions 240,296 by the Chebyshev operator $\scriptstyle { R _ { n } }$ 143-7 by trigonometric polynomials 152-61 characterization theorem 125-6 definition of norm 6-7,123-5 Erdos-Turan theorem 148 in the discrete case 124-5,133,157-8   
least squares approximation (cont.) methods of calculation 126-33,158-61 normal equations 127-9 uniqueness of best apprjximation 17- 18,123-4,126   
Lebesgue constants and functions 24-5, 41-3,218-19   
Legendre polynomials 142,149   
levelled reference error bounds on its value 81-2 definition 87 diagonal second derivative matrix 110 explicit expression and its multipliers 97-9,101 in analysis of exchange algorithm 101-2 in rational approximation 112-17 methods of calculation 85-6,113-15 monotonic increase 87,97-9,116-17   
linear programming duality 94,291 for $\scriptstyle { L _ { 1 } }$ approximation 183-6 for minimax approximation 94,118-20 for rational approximation 118-20 geometric view 184-6 to derive minimal property of perfect spline 291   
local spline approximation bya combination of $\pmb { B }$ -splines 243, 248-51 by interpolation 225,246-8   
metric space 3-5,16   
minimal properties of Chebyshev polynomials 78 natural splines 287-90 perfect splines 290-5 the norm of $s _ { n }$ 206-8   
minimax approximation by algebraic polynomials 26-8,76-9 byrational functions 111-21 by spline functions 239-40 by trigonometric polynomials 162,196 characterization theorems 75-7,79, 112-13,120-1,239-40 definition of norm 7,72 in the discrete case 19,79,92-4,112- 13,118-20 methods of calculation 12,85-8, 92-4, 112-15,118-20 non-uniqueness of best approximation 18-19,83 on a reference 79,85-6,112-13 uniqueness of best approximation 79- 81,108-9,113 when Haar condition holds 77,79-82, 90   
monotone operator 62-5,162-3   
multivariate approximation 71,226   
natural spline definition 285 interpolation conditions 219,285-6 minimal properties 287-90   
Newton's method for polynomial interpolation description 48-51 discussion of stability 52-3 extension to Hermite interpolation 53-7   
non-uniqueness of best approximations 11 best $\scriptstyle { L _ { 1 } }$ approximations 18-19,187 best minimax approximations 19,83   
normal equations in least squares calculations 127-9   
normed linear space 5-6,9-11,13-15, 17-19   
norm of operator definition 23 for polynomial interpolation 23-4, 41-3 for spline interpolation 218-19,225, 257-9 in the error bound that depends on the least maximum error 24 in the uniform boundedness theorem 203-4 values and bounds for $\| R _ { n } \|$ and $\| \pmb { S _ { n } } \|$ 145-7, 155,192-3   
norm of space definition 5 geometric view 9-11 relation between norms 7-9,11 strictly convex norm 14-19 the $\scriptstyle { L _ { 1 } }$ -norm6-7,18-19,164 the $L _ { p }$ norm 6-7,16 the least squares norm 6-7,17-18, 123-5 the minimax norm 7,18-19,72   
numerical integration,see quadrature   
one-point exchange algorithm,see exchange algorithm   
operator best approximation operators 16-17 equivalence of operators 201-2 linear operators 22-3 monotone operators 62-5, 162-3 norm,see norm of operator projection operators 22-5,206-10 the Bernstein operator 65-9 the Chebyshev least squares operator $\scriptstyle { R _ { n } }$ 143-7,155,208-9   
operator (cont.) the discrete Fourier series operator 156-8 the Fejer operator 162-3 the Fourier series operator $s _ { n }$ 152-6, 192-3,206-8   
optimal interpolation definition 298 derivation of interpolation formula 299-309 error bounds 309-10 knot positions 308-9 method of calculation 307-8   
order of convergence of polynomial approximation 26-8, 195-8 of spline approximation 30,241-6 of trigonometric approximation,see Jackson's theorems   
orthogonality definition 125 in least squares approximations 125-31 of algebraic polynomials 131-3,141-3 of Chebyshev polynomials 144 of trigonometric polynomials 153,158   
orthogonal polynomials characterization theorem 141 Chebyshev,see Chebyshev polynomials elementary theory 136-8 Hermite polynomials 143 in Gaussian quadrature 138-40 in least squares approximation 131-3 Jacobi polynomials 142 Laguerre polynomials 143 Legendre polynomials 142,149 properties of zeros 137-8,147 recurrence relation 131-3 Rodrigue's formula 142 approximation discussion of applications 28-9 interpolation procedures 29, 212-15   
Polya algorithm12   
polynomial approximation basis functions33,51-3,131-3 Bernstein operator 65-9 best in the $\pmb { L } _ { 1 }$ norm 166-7, 172-4 best in the least squares norm 125-6 131-3 best in the minimax norm 26-8,76-! by interpolation,see polynomial interpolation characterization theorems 77,125-6. 166-7 methods of calculation 34,48-51, 5s 6,65,85-8,92-3, 131-3, 174 order of convergence 26-8,195-8 orthogonality of polynomials 131-3, 141-4 telescoping 92, 148 trigonometric,see trigonometric polynomials uniform convergence 61-7, 196-7   
polynomial interpolation by a straight line 23-4, 29,213-14 cardinal functions 33-5 choice of interpolation points 37-41 effect of data errors 34 error expressions 35-6,276 Hermite interpolation 53-7 Lagrange formula 33-5, 52-3 Newton'smethod 48-57 norm of operator 41-3,208-10 to obtain convergence in the least squares norm 148 uniqueness of solution 33-4, 54-5   
product divided difference formula 59, 236   
projection operator 22-5,206-10   
quadratic spline interpolation 221-5, 257-61,282   
quadrature Gaussian 138-40,147 of $\pmb { B }$ -splines 240, 275 of trigonometric functions 156-7   
$\pmb { R _ { n } }$ operator (Chebyshev least squares) 143-7,155,208-9   
rational approximation by interpolation 44-5,59-60 comparison with polynomial approximation 28,111-12 diferential correction algorithm 119- exchange algorithm 112-18   
Peano kernel theorem description and proof 270-4 discussion and applications 268-70, 273-81 for cubic spline interpolation 277-81 for divided differences 274-5 for polynomial interpolation 276 minimization of the $L _ { 1 }$ -norm of the kernel 299-306 minimization of the least squares norm of the kernel 288-90   
perfect splines definition 291-2 error bound and knots for optimal interpolation 308-10 minimal property 292-4 uniqueness 294-5,297,312   
rational approximation(cont.) minimax approximation on areference 112-13 minimax theory 12,111-13,117, 120-1   
recurrence relation for B-splines 234-6 Chebyshev polynomials_39 divided differences 49-51 Legendre polynomials 149 orthogonal polynomials 131-3 spline interpolation 216,222-3,258   
reference,see exchange algorithm and levelled reference error   
Remes’algorithm,see exchange algorithm   
Rodrigue's formula 142   
Rolle's theorem 35-6,47   
Runge's example 37-41   
$s _ { n }$ operator (Fourier series) 152-6,192- 3,206-8   
scalar product 17,123-5,168   
Schoenberg-Whitney.theorem 223, 236-8,294,302,305   
sign alternation in minimax approximation 77,79,87-8,98,112   
spline approximation $\pmb { B }$ -splines, see $\pmb { B }$ -splines basis functions 29-30,227-8,231-4 best in the least squares norm 240,296 best in the minimax norm 239-40 bicubic splines 226 definition of a spline function 29-30 derivative discontinuities 220,224, 261-5 extended space of spline functions 255-7 interpolation,see spline interpolation knots,see knots of spline functions local methods 225,243,246-51 methods of calculation 215-16,220, 222-4,238-9,257,261-6,307-8 natural splines,see natural splines neara singularity 254-7 order of convergence 30,241-6 perfect splines,see perfect splines uniform convergence 241-3 zeros of spline functions 230-1   
spline interpolation by a cubic spline 215-21, 224,261-6, 277-81 by a natural spline 219,285-6 bya perfect spline 294-5 by a quadratic spline 221-5,257-61, 282 cardinal functions 216-19,222-3

end conditions 216,219-21,223-5, 285 error bounds 277-82,309-10 error estimates for cubic splines 261-5 general data points 236-9,259-61 localization properties 218, 220-4, 246-7 norm of operator 218-19,225,257-9 on an infinite range 216-19,221-3, 277-80 optimal, see optimal interpolation recurrence relations 216,222-3,258 Schoenberg-Whitney theorem 236-8 to surfaces 226 uniqueness of solution 216, 237-8, 285-6 strict convexity 13-19 surface approximation 71,226

Tchebycheff,see Chebyshev   
telescoping 92,148   
third derivative discontinuities of cubic splines 220,224,261-5   
three term recurrence relation for orthogonal polynomials 131-3   
trigonometric polynomials,see also Fourier series approximation to discrete data 156-61 best in the $L _ { 1 }$ -norm 176 best in the least squares norm 152-3, 157-8 best in the minimax norm 162,196 interpolation 161 methods of calculation 156-61 order of convergence,see Jackson's theorems orthogonality conditions 153,158 quadrature 156-7 relation to algebraic polynomials 151- 2,195-8 uniform convergence 151-2,162-3, 190-1 zeros of trigonometric polynomials 15c 161   
unicity,see uniqueness   
uniform approximation,see minimax approximation   
uniform boundedness theorem 203-4   
uniform convergence of Bernstein approximations 66 linear operators 202-4 monotone operators 62-5,162-3 polynomial approximations 61-7, 196-7   
uniform convergence of (cont.) spline approximations 241-3 trigonometric approximations 151-2, 162-3,190-1   
uniqueness of best approximations 13-17 best $\scriptstyle { L _ { 1 } }$ approximations 170,175 best least squares approximations 17- 18,123-4,126 best minimax approximations 79-81, 108-9,113 general spline interpolation 237-8 $\scriptstyle { L _ { 1 } }$ interpolation points 170-2 natural spline functions 285-6 orthogonal polynomials 136-7 perfect splines 294-5,297, 312 polynomial interpolation 33-4, 54-5   
variational problems minimal properties of natural splines 287-90 minimal property of perfect splines 290-5 minimization of $\left\| s ^ { \prime \prime } \right\| _ { 2 }$ subject to interpolation conditions 283-5   
Weierstrass theorem 25,61-2,66-7,191   
zeros of error function in best $\scriptstyle { L _ { 1 } }$ approximation 169-72,182-3 functions in a Chebyshev set 76-7, 313-16 orthogonal polynomials 137-8, 147 spline functions 230-1 trigonometric polynomials 150,161